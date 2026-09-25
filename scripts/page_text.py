"""Main-content text of every built page, for the layout-change guard (D-020).

A page's main content is the text inside its <main> element, without scripts and styles and
without navigation chrome: the breadcrumb (.crumbs) and elements marked data-chrome with one of
the values in CHROME. Whitespace is collapsed. Diagrams count as content, and so do the text
alternatives readers get (alt, aria-label) and the JSON data a page draws with JavaScript (for
example the workflow catalog): its string values are part of the page. check_browser.py also
compares the catalog's rendered text against a snapshot of its own.

    python scripts/page_text.py           # print {page: text} as JSON
    python scripts/page_text.py --write   # refresh scripts/tests/page_text_snapshot.json

Refresh the snapshot only for a change that is meant to alter page text; a layout change never is.
The guard compares text only: it does not see heading levels or other structure.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import html5lib

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
SNAPSHOT = ROOT / "scripts" / "tests" / "page_text_snapshot.json"
SKIP_TAGS = {"script", "style", "template"}
CHROME = {"pagenav", "choose"}  # the only elements a layout may mark as navigation chrome


def _json_strings(value) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        return [s for v in value.values() for s in _json_strings(v)]
    if isinstance(value, list):
        return [s for v in value for s in _json_strings(v)]
    return []


def _text(el) -> list[str]:
    tag = el.tag.rsplit("}", 1)[-1] if isinstance(el.tag, str) else ""
    chrome = el.get("data-chrome")
    if chrome is not None and chrome not in CHROME:
        raise ValueError(f"data-chrome={chrome!r} is not an allowed chrome element; allowed: {sorted(CHROME)}")
    if tag == "script" and el.get("type") == "application/json":
        return _json_strings(json.loads(el.text or "null")) + ([el.tail] if el.tail else [])
    if tag in SKIP_TAGS or chrome is not None or "crumbs" in (el.get("class") or "").split():
        return [el.tail] if el.tail else []
    out = [el.get(a) for a in ("alt", "aria-label") if el.get(a)]
    out += [el.text] if el.text else []
    for child in el:
        out += _text(child)
    if el.tail:
        out.append(el.tail)
    return out


def _inside(root, target) -> bool:
    return any(el is target for el in root.iter())


def main_text(html: str) -> str:
    doc = html5lib.parse(html, namespaceHTMLElements=False)
    main = doc.find(".//main")
    if main is None:
        return ""
    parts = []
    for child in main:
        parts += _text(child)
    if main.text:
        parts.insert(0, main.text)
    # data the page draws with JavaScript, wherever the generator puts it
    for script in doc.iter("script"):
        if script.get("type") == "application/json" and not _inside(main, script):
            parts += _json_strings(json.loads(script.text or "null"))
    return re.sub(r"\s+", " ", " ".join(p for p in parts if p)).strip()


RENDERED = ROOT / "scripts" / "tests" / "catalog_rendered_snapshot.json"
# Rendered text of the catalog after its script draws every view, compared by check_browser.py.
RENDERED_JS = """() => {
  const main = document.querySelector('main').cloneNode(true);
  main.querySelectorAll('.crumbs, [data-chrome], script, style').forEach(el => el.remove());
  return main.textContent.replace(/\\s+/g, ' ').trim();
}"""


def catalog_rendered(page, base: str) -> str:
    page.goto(base + "/workflow-catalog.html")
    for label in ("Table", "Traditional map", "Map"):
        page.get_by_role("tab", name=label, exact=True).click()
    return page.evaluate(RENDERED_JS)


def snapshot(site: Path = SITE) -> dict[str, str]:
    return {p.name: main_text(p.read_text(encoding="utf-8")) for p in sorted(site.glob("*.html"))}


if __name__ == "__main__":
    data = snapshot()
    if "--write" in sys.argv:
        SNAPSHOT.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Wrote {SNAPSHOT.relative_to(ROOT)} for {len(data)} pages.")
    else:
        print(json.dumps(data, indent=1, ensure_ascii=False))
