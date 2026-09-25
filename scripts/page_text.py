"""Main-content text of every built page, for the layout-change guard (D-020).

A page's main content is the text inside its <main> element, without scripts and styles and
without navigation chrome: elements marked data-chrome and the breadcrumb
(.crumbs). Whitespace is collapsed. Diagrams count as content: their text is part of the page.

    python scripts/page_text.py           # print {page: text} as JSON
    python scripts/page_text.py --write   # refresh scripts/tests/page_text_snapshot.json

Refresh the snapshot only for a change that is meant to alter page text; a layout change never is.
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


def _text(el) -> list[str]:
    tag = el.tag.rsplit("}", 1)[-1] if isinstance(el.tag, str) else ""
    if tag in SKIP_TAGS or el.get("data-chrome") is not None or "crumbs" in (el.get("class") or "").split():
        return [el.tail] if el.tail else []
    out = [el.text] if el.text else []
    for child in el:
        out += _text(child)
    if el.tail:
        out.append(el.tail)
    return out


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
    return re.sub(r"\s+", " ", " ".join(p for p in parts if p)).strip()


def snapshot(site: Path = SITE) -> dict[str, str]:
    return {p.name: main_text(p.read_text(encoding="utf-8")) for p in sorted(site.glob("*.html"))}


if __name__ == "__main__":
    data = snapshot()
    if "--write" in sys.argv:
        SNAPSHOT.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Wrote {SNAPSHOT.relative_to(ROOT)} for {len(data)} pages.")
    else:
        print(json.dumps(data, indent=1, ensure_ascii=False))
