---
name: diagrammer
description: "House rules for diagrams as code. Used by the diagrammer agent."
---

# Diagrammer

- Source: an SVG in `content/diagrams/svg/<id>.svg`, or a generator that writes it (see
  `content/diagrams/map/build_map.py`). Commit the generated SVG with its generator.
- Size by `width`/`height` on the root; ids unique within the diagram.
- `<title>` names the figure; `<desc>` describes it fully in words, including every label that
  carries meaning, and expands abbreviations.
- Palette (fill / stroke / dark text):
  purple agent `#EEEDFE / #534AB7 / #26215C`; coral checks or blocked `#FAECE7 / #993C1D / #4A1B0C`;
  teal people or passing `#E1F5EE / #0F6E56 / #04342C`; grey project meaning
  `#F1EFE8 / #888780 / #2C2C2A`; amber context `#FAEEDA / #8a5a00 / #5a3b00`.
- White background inside the SVG so it reads in both site themes; check the page in dark mode.
- `data-references="<keys>"` on the root; credit lines `<text class="credit" data-references="...">`
  when the diagram is downloadable without a page (D-009).
- Embed in a page as `![caption](diagram:<id>)`.
- Check: `python scripts/check_citations.py`, `python site/generate.py`, `python scripts/render_diagrams.py`.
