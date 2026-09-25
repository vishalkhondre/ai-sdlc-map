"""Render every diagram in site/diagrams/*.svg to PNG, and copy the map as the site's OG image.

The SVGs are the source of truth (content/diagrams/svg); the PNGs are build artefacts.
Run after site/generate.py.

    python scripts/render_diagrams.py              # all diagrams
    python scripts/render_diagrams.py --only map   # only diagrams whose name contains "map"

Requires playwright + chromium (see scripts/requirements.txt).
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
DIAGRAMS = SITE / "diagrams"


def svg_size(svg: str) -> tuple[int, int]:
    m = re.search(r'<svg[^>]*width="(\d+)"[^>]*height="(\d+)"', svg)
    return (int(m.group(1)), int(m.group(2))) if m else (1200, 628)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="")
    ap.add_argument("--scale", type=int, default=2, help="device scale factor for PNGs")
    args = ap.parse_args()
    from playwright.sync_api import sync_playwright

    svgs = sorted(p for p in DIAGRAMS.glob("*.svg") if args.only in p.name)
    if not svgs:
        print("No diagrams found. Run site/generate.py first.", file=sys.stderr)
        return 1
    with sync_playwright() as p:
        options = {}
        if os.environ.get("PLAYWRIGHT_CHROMIUM_EXECUTABLE"):
            options["executable_path"] = os.environ["PLAYWRIGHT_CHROMIUM_EXECUTABLE"]
        browser = p.chromium.launch(**options)
        for svg_path in svgs:
            svg = svg_path.read_text(encoding="utf-8")
            w, h = svg_size(svg)
            page = browser.new_page(viewport={"width": w, "height": h}, device_scale_factor=args.scale)
            page.set_content(f'<!DOCTYPE html><html><body style="margin:0;background:#fff">{svg}</body></html>')
            page.wait_for_timeout(100)
            out = svg_path.with_suffix(".png")
            page.screenshot(path=str(out), clip={"x": 0, "y": 0, "width": w, "height": h})
            page.close()
            print(f"  {out.name}  {w}x{h}@{args.scale}x")
        # OG image for the home page
        og_src = DIAGRAMS / "ai-sdlc-map.png"
        if og_src.exists():
            (SITE / "og-image.png").write_bytes(og_src.read_bytes())
        browser.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
