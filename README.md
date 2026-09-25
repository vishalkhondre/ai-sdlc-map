# The AI SDLC Map

**The AI-assisted software lifecycle, from spec to software factory, on one page.**

A vendor-neutral reference for the AI SDLC: the software development lifecycle (SDLC) with AI
agents doing part of the work in every phase. One map in five bands (context, lifecycle, core,
enablement and assurance) and an adoption path, with every source named.

Read it at **https://vishalkhondre.github.io/ai-sdlc-map/**

The narrative introduction, the seven-part series *Beyond Faster Coding*, is published separately
at <https://vishalkhondre.github.io/ai-sdlc/> from
[`vishalkhondre/ai-sdlc`](https://github.com/vishalkhondre/ai-sdlc). This site links to its parts
rather than reproducing them.

The site has:

- **The map and the adoption path** on the home page.
- **SDLC workflow catalog**: 35 workflows across eight phases, each mapped one-to-one to the
  traditional activity it absorbs, filterable by phase, maturity and change type.
- **Terminology and sources**: every term, marked as adopted, adapted, coined or common, with a
  translation table to Birgitta Böckeler's harness-engineering vocabulary on martinfowler.com.
- **References**: every source, with the terms, diagrams and series parts that cite it.

## Working on it

Start with [`CLAUDE.md`](CLAUDE.md) and the files in [`project/`](project/): goal, ground rules,
status, approach, agents, assumptions and decisions.

## How it is built

```
content/
  toc.yml               site identity, and the series parts this site links to (with what each cites)
  glossary.yml          terms, attribution (adopted / adapted / coined / common), sources
  references.yml        canonical references
  workflows/catalog.yml the workflow catalog and traditional-activity map
  diagrams/map/         generator for the map and the adoption path
  diagrams/svg/         diagram SVGs (the map ones are generated)
  reviews/              editorial review reports; release-review.json binds one to the sources
  VERSION, CHANGELOG.md content edition
site/
  generate.py           content/ -> static HTML (inline SVG, no framework, no external requests)
  assets/               one CSS file, one JS file
scripts/
  check_citations.py    attribution, neutrality, diagram-credit, access-date and outdated-terms gate
  check_pages.py        page-template structure and provisional-language gate
  outdated_terms.yml    superseded terms and their replacements
  render_diagrams.py    SVG -> PNG and the OG image
  release_content.py    edition/changelog validation and source-bound editorial acceptance
  release_snapshot.py   release notes and PDF snapshot for a tagged section release
  check_browser.py      browser regressions for the home map, search, catalog and zoom
  tests/                site, citation, reference, page, agent, deny-list and release tests
.github/
  workflows/            validate on every PR; deploy to GitHub Pages from main; release on a v* tag or by hand
  instructions/, prompts/   content rules and procedures for people and agents
release/
  sections.yml          the section and pages each tagged release covers
.claude/
  agents/, skills/      the nine pipeline roles and their checklists (project/AGENTS.md)
templates/pages/        one template per page type (project/APPROACH.md)
```

## Run locally

```bash
pip install -r scripts/requirements.txt
python -m playwright install chromium     # for PNG rendering and browser checks
python scripts/check_citations.py
python scripts/check_pages.py
python site/generate.py
python scripts/render_diagrams.py
python -m unittest discover -s scripts/tests
python scripts/check_browser.py
python -m http.server -d site 8000        # then open http://localhost:8000
```

## Licence

Prose, diagrams and data under CC BY 4.0; tooling under MIT. See [`LICENSE`](LICENSE).
