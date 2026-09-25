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

0. Before the first validation, create `content/reviews/<edition>-<section>.md` with Scope and
   Limitations only, so each page's `review_record` resolves. `release_content.py check` fails
   until the record is bound with an ACCEPT; that is expected until step 4.
1. Commit and push; record the commit hash for the orchestrating session, which starts the
   reviewers (`section-pipeline`).
2. On REVISE or BLOCK: the findings go to `author` or `diagrammer` through the main session;
   rerun validation and return the fix range for confirmation (D-011). Three rounds at most; then
   the author decides.
3. Add each reviewer's report to the record as it arrives.
4. When all three ACCEPT, assemble the record (see `section-pipeline`) and bind it with
   `record-review`.

## Pull request

Title, scope, pages, edition, review summary per reviewer and round, limitations (for example
sources verified by search only), validation output. Merge when CI is green. Tag only when the
author says so.
