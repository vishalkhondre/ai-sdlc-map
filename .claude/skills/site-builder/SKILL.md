---
name: site-builder
description: "Wiring, validation, review assembly and PR steps for a section. Used by the site-builder agent."
---

# Site builder

## Wire the section

- Render `content/pages/<band>/*.md` into the site (extend `site/generate.py` the first time a
  band gets pages: page chrome, navigation, search index, sitemap, llms files).
- Link each page from its map box in `content/diagrams/map/links.yml`, and from the routing row
  where APPROACH.md routes readers to it.
- Add the section to `release/sections.yml` under its major.minor.

## Validate (every round)

```bash
python scripts/check_citations.py
python scripts/check_pages.py
python scripts/release_content.py check --base <base commit>
python site/generate.py
python scripts/render_diagrams.py
python -m unittest discover -s scripts/tests
python scripts/check_browser.py
```

## Review rounds

1. Commit and push; record the commit hash.
2. Start the three reviewers in fresh contexts, in parallel, each with the commit, the diff
   range, the check output and its skill. Never pass the practice brief.
3. On REVISE or BLOCK: route findings to `author` or `diagrammer`, rerun validation, and send
   the fix range back for confirmation (D-011). Three rounds at most; then the author decides.
4. When all three ACCEPT, assemble the record (see `section-pipeline`) and bind it with
   `record-review`.

## Pull request

Title, scope, pages, edition, review summary per reviewer and round, limitations (for example
sources verified by search only), validation output. Merge when CI is green. Tag only when the
author says so.
