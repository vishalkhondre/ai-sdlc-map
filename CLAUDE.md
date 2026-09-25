# CLAUDE.md — start here

This repository builds **The AI SDLC Map**, a public reference site published at
<https://vishalkhondre.github.io/ai-sdlc-map/>. The work spans many sessions. This file and the
files in `project/` are how one session hands over to the next.

The narrative series *Beyond Faster Coding* is a separate, finished site in
[`vishalkhondre/ai-sdlc`](https://github.com/vishalkhondre/ai-sdlc), maintained only (see its
`MAINTENANCE.md`). This site links to its parts; it never copies their text (D-010).

## Read before doing anything

| Order | File | What it holds |
|---|---|---|
| 1 | [`project/GOAL.md`](project/GOAL.md) | What is being built, for whom, and what "done" means |
| 2 | [`project/GROUND-RULES.md`](project/GROUND-RULES.md) | Non-negotiable rules. Every check and review cites a rule number from here |
| 3 | [`project/STATUS.md`](project/STATUS.md) | Where the work stands, what is next, and the session log |
| 4 | [`project/APPROACH.md`](project/APPROACH.md) | Information architecture, page types, pipeline, waves |
| 5 | [`project/AGENTS.md`](project/AGENTS.md) | The agent and skill roster, and the handoffs between them |
| 6 | [`project/ASSUMPTIONS.md`](project/ASSUMPTIONS.md) | What is assumed true, and what is still open |
| 7 | [`project/DECISIONS.md`](project/DECISIONS.md) | Decisions already taken, with reasons. Do not reopen without the author |

## Session protocol

**At the start of a session**
1. Read the files above in order.
2. Confirm the session can push to `vishalkhondre/ai-sdlc-map` (`git push --dry-run`). If it cannot,
   say so at once. Work can still proceed and be handed over as a git bundle.
3. Confirm the Google Drive connector is available if the task needs the source library
   (see `project/ASSUMPTIONS.md`, A3).
4. Pick up the top item under **Next** in `project/STATUS.md`, unless the author says otherwise.

**At the end of a session**
1. Update `project/STATUS.md`: move finished items, set **Next**, and add a session-log entry.
2. Record any new decision in `project/DECISIONS.md` and any new assumption in
   `project/ASSUMPTIONS.md`.
3. Run the full validation (below) and commit. A session never ends with a failing build on `main`.

## Validation

```bash
pip install -r scripts/requirements.txt
python -m playwright install chromium
python scripts/check_citations.py
python scripts/release_content.py check --base <base commit>
python site/generate.py
python scripts/render_diagrams.py
python -m unittest discover -s scripts/tests
python scripts/check_browser.py
```

CI (`.github/workflows/validate.yml`) runs the same steps on every pull request and push to `main`.
Content changes need an edition bump, a changelog entry and a recorded reviewer ACCEPT
(`scripts/release_content.py record-review`); see `.github/prompts/update-content.prompt.md`.
Pages deploy only from `main`, via `.github/workflows/deploy-pages.yml`. A section is released
only after the author approves it: on the author's explicit instruction, tag `v<content/VERSION>` on
`main` and push the tag;
`.github/workflows/release.yml` creates the GitHub Release with the changelog notes and a PDF
snapshot of the pages listed in `release/sections.yml` (D-014, D-016).

## The three rules most often broken

1. Nothing in this repository may identify the author's employer or its internal work
   (GROUND-RULES §1). The source library is read for experience and is never copied.
2. Every non-obvious claim needs a public source (GROUND-RULES §2).
3. No page is published incomplete, and nothing on the site says "draft" or "coming soon"
   (GROUND-RULES §3–§4).
