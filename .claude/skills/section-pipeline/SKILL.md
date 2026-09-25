---
name: section-pipeline
description: "Runs one section of The AI SDLC Map end to end: plan, research, write, diagram, check, review, merge, author review, release. Use when starting or resuming a section."
---

# Section pipeline (D-014, D-016)

A section is one band of the map or the adoption path. One section is in flight at a time.

| Step | Who | Output | Gate |
|---|---|---|---|
| 1 Plan | `architect` | page list from the map and `project/COVERAGE.md` | **author approves the plan** |
| 2 Brief | `architect` | one page brief per page (scratchpad) | — |
| 3 Research | `source-researcher` ║ `external-researcher` | practice brief (scratchpad only) ║ evidence brief and reference entries | — |
| 4 Write | `author` | `content/pages/<band>/<id>.md` from its template | — |
| 5 Diagram | `diagrammer` | diagrams as code, when they carry meaning | — |
| 6 Check | `site-builder` | full validation (`CLAUDE.md`) green | every check passes |
| 7 Review | `confidentiality-reviewer` ║ `accuracy-reviewer` ║ `editorial-reviewer`, fresh contexts | three reports | all ACCEPT; three rounds, then the author |
| 8 Record | `site-builder` | `content/reviews/<edition>-<section>.md`, bound by `record-review` | `release_content.py check` |
| 9 Merge | `site-builder` | pull request merged, deployed live | CI green |
| 10 Author review | the author | follow-up PRs, each through steps 4–9 (patch editions) | — |
| 11 Release | on the author's instruction | tag `v<content/VERSION>`; the release workflow publishes notes and a PDF | author approval |

## Rules that hold at every step

- Nothing from the source library enters the repository (GR-1.3). Briefs live in the scratchpad.
- Reviewers see the pages, sources and check output, never the author's reasoning or the
  practice brief (AGENTS.md, Independence).
- A section merges only complete: every page of the plan, every section of every template
  (GR-4.1). No page is published as provisional (GR-3.2).
- A section is a new minor edition (`content/VERSION`, `content/CHANGELOG.md`); follow-ups bump
  the patch. Add the section to `release/sections.yml` under its major.minor.
- Update `project/STATUS.md` at the end of each session.

## The assembled record

`content/reviews/<edition>-<section>.md`: a Scope and a Limitations paragraph, then each
reviewer's report under its own heading (every round kept), then a Result line and exactly one
standalone `Verdict: ACCEPT`, written only when every reviewer's latest report says ACCEPT. Bind it:

    python scripts/release_content.py record-review --report content/reviews/<file>.md
