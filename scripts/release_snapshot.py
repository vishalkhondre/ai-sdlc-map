"""Release notes and the PDF snapshot for a tagged, author-approved section release (D-016).

    python scripts/release_snapshot.py notes v1.3.0            # changelog entry for 1.3.0, as Markdown
    python scripts/release_snapshot.py pdf v1.3.0 out.pdf      # PDF of the section's pages (build the site first)

The tag must be `v` + content/VERSION, and release/sections.yml must list the pages the
release covers. Both commands fail otherwise, so a tag cannot publish a release the
repository does not describe.
"""
from __future__ import annotations

import argparse
import functools
import http.server
import io
import os
import re
import sys
import threading
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SECTIONS = ROOT / "release" / "sections.yml"


def version_for(tag: str, root: Path = ROOT) -> str:
    version = (root / "content/VERSION").read_text(encoding="utf-8").strip()
    if tag != f"v{version}":
        raise ValueError(f"Tag {tag} does not match content/VERSION {version}; tag v{version} instead.")
    return version


def notes(tag: str, root: Path = ROOT) -> str:
    version = version_for(tag, root)
    changelog = (root / "content/CHANGELOG.md").read_text(encoding="utf-8")
    entry = re.search(rf"^## {re.escape(version)}(?:[ \t]+[^\n]*)?\n(.*?)(?=^## |\Z)", changelog, re.M | re.S)
    if not entry or not entry.group(1).strip():
        raise ValueError(f"CHANGELOG.md has no entry for {version}.")
    section = release_section(version, root)
    return (f"**{section['section']}**\n\n{entry.group(1).strip()}\n\n"
            f"This tag marks the author's approval of the section (D-014, D-016). "
            f"The attached PDF is a snapshot of its pages as published.\n")


def release_section(version: str, root: Path = ROOT) -> dict:
    sections = yaml.safe_load((root / "release/sections.yml").read_text(encoding="utf-8")) or {}
    section = sections.get(version)
    if not section or not section.get("section") or not section.get("pages"):
        raise ValueError(f"release/sections.yml needs a section name and pages for {version}.")
    return section


def pdf(tag: str, out: Path, root: Path = ROOT) -> list[str]:
    from playwright.sync_api import sync_playwright
    from pypdf import PdfWriter

    version = version_for(tag, root)
    pages = release_section(version, root)["pages"]
    site = root / "site"
    for page in pages:
        if not (site / page).exists():
            raise ValueError(f"site/{page} does not exist; run site/generate.py first.")

    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *_args):
            pass

    handler = functools.partial(Quiet, directory=str(site))
    writer = PdfWriter()
    with http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler) as server:
        threading.Thread(target=server.serve_forever, daemon=True).start()
        try:
            with sync_playwright() as p:
                options = {}
                if os.environ.get("PLAYWRIGHT_CHROMIUM_EXECUTABLE"):
                    options["executable_path"] = os.environ["PLAYWRIGHT_CHROMIUM_EXECUTABLE"]
                browser = p.chromium.launch(**options)
                tab = browser.new_page()
                for page in pages:
                    tab.goto(f"http://127.0.0.1:{server.server_port}/{page}")
                    tab.emulate_media(media="print")
                    writer.append(io.BytesIO(tab.pdf(format="A4", print_background=True,
                                                     margin={"top": "12mm", "bottom": "12mm", "left": "10mm", "right": "10mm"})))
                browser.close()
        finally:
            server.shutdown()
    writer.add_metadata({"/Title": f"The AI SDLC Map {version}: {release_section(version, root)['section']}"})
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("wb") as fh:
        writer.write(fh)
    return pages


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = parser.add_subparsers(dest="command", required=True)
    n = commands.add_parser("notes")
    n.add_argument("tag")
    s = commands.add_parser("pdf")
    s.add_argument("tag")
    s.add_argument("out", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "notes":
            sys.stdout.write(notes(args.tag))
        else:
            pages = pdf(args.tag, args.out)
            print(f"Wrote {args.out} from {len(pages)} pages: {', '.join(pages)}")
        return 0
    except (ValueError, OSError) as exc:
        parser.exit(1, f"Release snapshot failed: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
