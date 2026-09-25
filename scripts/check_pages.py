"""Page gate: template structure (GR-4.1), provisional language (GR-3.2) and page metadata.

Every reference page is content/pages/<band>/<id>.md, written from its type's template in
templates/pages/<type>.md. Fails (exit 1) when a page:
  1. lacks a front-matter field, leaves one empty, keeps a template <placeholder>, or keeps the
     template's instructions
  2. names an unknown type or band, sits in a folder other than its band, or its id is not
     its file name, or two pages share an id
  3. does not have exactly its template's ## sections, in the template's order
  4. has a section that is not substantive: fewer than MIN_WORDS words of prose (fewer for the
     short sections in SHORT_SECTIONS), or, for Related, no link, or, for Sources, no citation
  5. keeps a template guidance comment, or uses provisional language (GR-3.2): the phrases in
     PROVISIONAL anywhere, and "draft" in the title, summary, a heading or link text. Elsewhere
     "draft" is allowed, because agents draft specs and plans and the pages describe that.
  6. cites a key that is not in content/references.yml or not in its `sources`, lists a
     key_term that is not in content/glossary.yml, a related id that is not a page, or a
     review_record that does not exist (the site-builder creates the record, with its scope,
     before the first check; the release gate requires its ACCEPT), or a footnote whose key is not
     lower-case letters, digits and hyphens (it would be published as literal text)
  7. has an id that is not lower-case words joined by hyphens, or one a built page already uses
  8. is missing from content/toc.yml `pages.<band>`, which sets the reading order (D-020), or
     that list names a page that does not exist

The templates themselves are checked too: each has the front-matter fields and a type that
matches its file name. The tests check the templates against the table in project/APPROACH.md.

Run:  python scripts/check_pages.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ["id", "type", "band", "map_box", "title", "summary", "key_terms", "sources", "related", "review_record"]
BANDS = ["context", "lifecycle", "core", "enablement", "assurance", "adoption"]
MIN_WORDS = 25
# Sections that are one decision, one event or one name by design need fewer words (no padding).
SHORT_SECTIONS = {"Decision": 8, "Trigger": 8, "Owner": 5, "Risk tier": 12}
# GR-3.2. "draft" is banned only as a label for the page or its parts: agents write drafts of
# specs and plans, and the pages describe that.
PROVISIONAL = [
    r"\bwork in progress\b", r"\bcoming soon\b", r"\bTBD\b", r"\bTBC\b", r"\bto be added\b", r"\bplaceholder\b",
    r"\bv0\.(?:\d+|x)\b", r"\bunder construction\b", r"\blorem ipsum\b",
    r"\bthis (?:page|section|entry) is (?:a |still )?(?:draft|incomplete)\b", r"\(draft\)", r"\[draft\]",
]


# Built pages a reference page may not overwrite (GR-4.3).
RESERVED_IDS = {"index", "glossary", "references", "workflow-catalog", "404", "sitemap", "robots", "llms", "llms-full", "search-index"}


# In a title, summary, heading or link text, "draft" always labels the page itself (GR-3.2).
DRAFT_LABEL = re.compile(r"\bdraft\b", re.I)


def split_page(text: str) -> tuple[dict, str]:
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise ValueError("no front matter (--- ... ---) at the top")
    meta = yaml.safe_load(m.group(1)) or {}
    if not isinstance(meta, dict):
        raise ValueError("front matter is not a mapping")
    return meta, m.group(2)


def without_code(body: str) -> str:
    return re.sub(r"^```.*?^```[ \t]*$", "", body, flags=re.M | re.S)


def sections(body: str) -> list[tuple[str, str]]:
    """(heading, text) for each ## section outside code fences, in order."""
    parts = re.split(r"^## +(.+?)\s*$", without_code(body), flags=re.M)
    return [(parts[i].strip(), parts[i + 1]) for i in range(1, len(parts), 2)]


def load_templates(root: Path = ROOT) -> tuple[dict[str, list[str]], list[str]]:
    templates, problems = {}, []
    for path in sorted((root / "templates" / "pages").glob("*.md")):
        try:
            meta, body = split_page(path.read_text(encoding="utf-8"))
        except (ValueError, yaml.YAMLError) as exc:
            problems.append(f"templates/pages/{path.name}: {exc}")
            continue
        missing = [f for f in FIELDS if f not in meta]
        if missing:
            problems.append(f"templates/pages/{path.name}: front matter lacks {', '.join(missing)}")
        if meta.get("type") != path.stem:
            problems.append(f"templates/pages/{path.name}: type is {meta.get('type')!r}, expected {path.stem!r}")
        templates[path.stem] = [h for h, _ in sections(body)]
    if not templates:
        problems.append("templates/pages/ holds no templates")
    return templates, problems


def words(text: str) -> int:
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"\]\([^)]*\)", "]", text)  # link targets are not prose
    text = re.sub(r"\[\^[a-z0-9\-]+\]", "", text)
    text = re.sub(r"[#>*_`|\-]", " ", text)
    return len(re.findall(r"[A-Za-z0-9][\w'’]*", text))


def check_page(path: Path, meta: dict, body: str, templates: dict, refs: dict, glossary_ids: set,
               page_ids: set, root: Path) -> list[str]:
    where = path.relative_to(root).as_posix()
    problems = []
    for field in FIELDS:
        value = meta.get(field)
        if value in (None, "", []):
            problems.append(f"{where}: front matter field '{field}' is missing or empty")
        elif re.search(r"<[^>]+>", str(value)):
            problems.append(f"{where}: front matter field '{field}' still holds a template placeholder")
    kind, band = meta.get("type"), meta.get("band")
    if kind not in templates:
        problems.append(f"{where}: unknown type {kind!r}; use one of {', '.join(sorted(templates))}")
    if band not in BANDS:
        problems.append(f"{where}: unknown band {band!r}; use one of {', '.join(BANDS)}")
    elif path.parent.name != band:
        problems.append(f"{where}: band is {band!r} but the page sits in {path.parent.name}/")
    if meta.get("id") != path.stem:
        problems.append(f"{where}: id {meta.get('id')!r} does not match the file name {path.stem!r}")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", str(meta.get("id") or "")):
        problems.append(f"{where}: id {meta.get('id')!r} must be lower-case words joined by hyphens")
    elif meta.get("id") in RESERVED_IDS:
        problems.append(f"{where}: id {meta.get('id')!r} is taken by a built page ({meta.get('id')}.html)")

    found = sections(body)
    if kind in templates:
        headings = [h for h, _ in found]
        if headings != templates[kind]:
            problems.append(f"{where}: sections are {headings}; a {kind} page needs exactly {templates[kind]}, in that order")
    for heading, text in found:
        if heading == "Related":
            if not re.search(r"\]\([^)]+\)", text):
                problems.append(f"{where}: section 'Related' has no link")
        elif heading == "Sources":
            if not re.search(r"\[\^[a-z0-9\-]+\]", text):
                problems.append(f"{where}: section 'Sources' cites no reference")
        elif words(text) < SHORT_SECTIONS.get(heading, MIN_WORDS):
            need = SHORT_SECTIONS.get(heading, MIN_WORDS)
            problems.append(f"{where}: section '{heading}' has {words(text)} words; at least {need} are needed (GR-4.1)")

    full = path.read_text(encoding="utf-8")
    labels = [str(meta.get("title") or ""), str(meta.get("summary") or "")] + [h for h, _ in found]
    labels += re.findall(r"\[([^\]^][^\]]*)\]\(", body)
    for label in labels:
        if DRAFT_LABEL.search(label):
            problems.append(f"{where}: '{label}' labels the page as a draft (GR-3.2)")
    if re.search(r"^# Template for", full, re.M):
        problems.append(f"{where}: the template's instructions are still in the page")
    if "<!--" in body:
        problems.append(f"{where}: a template guidance comment is still in the page")
    for pat in PROVISIONAL:
        for m in re.finditer(pat, full, flags=re.I):
            line = full.count("\n", 0, m.start()) + 1
            problems.append(f"{where}:{line}: '{m.group(0)}' is provisional language (GR-3.2)")

    listed = set(meta.get("sources") or [])
    for key in sorted(listed - refs.keys()):
        problems.append(f"{where}: source '{key}' is not in content/references.yml")
    code_free = without_code(body)
    for key in sorted(set(re.findall(r"\[\^([^\]\s]+)\]", code_free)) - set(re.findall(r"\[\^([a-z0-9\-]+)\]", code_free))):
        problems.append(f"{where}: [^{key}] is not a reference key (lower-case letters, digits and hyphens)")
    for key in sorted(set(re.findall(r"\[\^([a-z0-9\-]+)\]", code_free))):
        if key not in refs:
            problems.append(f"{where}: cites [^{key}], which is not in content/references.yml")
        elif key not in listed:
            problems.append(f"{where}: cites [^{key}] but does not list it under sources")
    for term in meta.get("key_terms") or []:
        if term not in glossary_ids:
            problems.append(f"{where}: key term '{term}' is not in content/glossary.yml")
    for other in meta.get("related") or []:
        if other not in page_ids:
            problems.append(f"{where}: related page '{other}' does not exist")
    record = meta.get("review_record")
    if record and not re.search(r"<[^>]+>", str(record)) and not (root / str(record)).is_file():
        problems.append(f"{where}: review record {record} does not exist")
    return problems


def check(root: Path = ROOT) -> tuple[list[str], int]:
    templates, problems = load_templates(root)
    refs = yaml.safe_load((root / "content/references.yml").read_text(encoding="utf-8")) or {}
    glossary_ids = {g["id"] for g in yaml.safe_load((root / "content/glossary.yml").read_text(encoding="utf-8")) or []}
    pages = []
    for path in sorted((root / "content" / "pages").rglob("*.md")):
        try:
            meta, body = split_page(path.read_text(encoding="utf-8"))
        except (ValueError, yaml.YAMLError) as exc:
            problems.append(f"{path.relative_to(root).as_posix()}: {exc}")
            continue
        pages.append((path, meta, body))
    ids = [meta.get("id") for _, meta, _ in pages]
    for dup in sorted({i for i in ids if ids.count(i) > 1 and i}):
        problems.append(f"content/pages: id '{dup}' is used by more than one page")
    for path, meta, body in pages:
        problems += check_page(path, meta, body, templates, refs, glossary_ids, set(ids), root)
    # toc.yml `pages` gives the reading order per band (D-020): every page listed, nothing else
    toc_path = root / "content/toc.yml"
    toc = (yaml.safe_load(toc_path.read_text(encoding="utf-8")) or {}) if toc_path.is_file() else None
    order = (toc or {}).get("pages") or {}
    for band in BANDS if toc is not None else []:
        listed = list(order.get(band) or [])
        present = [meta.get("id") for _, meta, _ in pages if meta.get("band") == band]
        for pid in sorted(set(present) - set(listed)):
            problems.append(f"content/toc.yml: page '{pid}' is missing from pages.{band}, which sets the reading order")
        for pid in sorted(set(listed) - set(present)):
            problems.append(f"content/toc.yml: pages.{band} lists '{pid}', which is not a {band} page")
    for band in sorted(set(order) - set(BANDS)):
        problems.append(f"content/toc.yml: pages.{band} is not a band")
    return problems, len(pages)


def main() -> int:
    problems, n = check()
    if problems:
        print("Page check FAILED:")
        for p in problems:
            print("  -", p)
        return 1
    print(f"Page check passed: {n} pages against {len(load_templates()[0])} templates.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
