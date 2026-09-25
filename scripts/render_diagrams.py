"""Render every diagram in site/diagrams/*.svg to PNG, and the site's social preview card (og-image.png).

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


def og_card() -> str:
    """The social preview card as HTML, with the bundled fonts inlined so it renders offline."""
    import base64
    import yaml
    fonts = SITE / "assets" / "fonts"
    face = ""
    for weight, name in ((400, "atkinson-hyperlegible-latin-400-normal"), (700, "atkinson-hyperlegible-latin-700-normal")):
        data = base64.b64encode((fonts / f"{name}.woff2").read_bytes()).decode()
        face += f'@font-face{{font-family:A;font-weight:{weight};src:url(data:font/woff2;base64,{data}) format("woff2")}}'
    toc = yaml.safe_load((ROOT / "content" / "toc.yml").read_text(encoding="utf-8"))
    bars = "".join(f'<rect x="2" y="{2 + i * 3.4:.1f}" width="16" height="2.2" rx="1.1"/>' for i in range(5))
    host = toc["site_url"].split("://", 1)[1]
    return f"""<!DOCTYPE html><html><head><style>{face}
    body{{margin:0;width:1200px;height:630px;background:#f6f8f8;font-family:A,sans-serif;color:#15232b;display:flex}}
    .card{{margin:64px;padding:64px 72px;flex:1;background:#fff;border:1px solid #d8e1e1;border-radius:24px;display:flex;flex-direction:column;justify-content:space-between}}
    .row{{display:flex;align-items:center;gap:26px}} svg{{width:104px;height:104px;fill:#0b6e69}}
    h1{{font-size:76px;line-height:1;margin:0;font-weight:700}} p{{font-size:34px;line-height:1.3;color:#34434b;margin:0;max-width:960px}}
    .url{{font-size:24px;color:#0b6e69;font-weight:700}}</style></head><body><div class="card">
    <div class="row"><svg viewBox="0 0 20 20">{bars}</svg><h1>{toc["title"]}</h1></div>
    <p>{toc["tagline"]}</p><div class="url">{host}</div></div></body></html>"""


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
        # Social preview card (D-021): logo, wordmark and subtitle in the brand, 1200x630
        page = browser.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=1)
        page.set_content(og_card())
        page.wait_for_timeout(200)
        page.screenshot(path=str(SITE / "og-image.png"))
        page.close()
        print("  og-image.png  1200x630")
        browser.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
