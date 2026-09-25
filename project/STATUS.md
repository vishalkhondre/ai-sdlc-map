# Status

Update at the end of every session (see `CLAUDE.md`).

## Where things stand

- **Repositories (D-010):** this repository, `vishalkhondre/ai-sdlc-map`, builds *AI SDLC on one
  page* at `vishalkhondre.github.io/ai-sdlc-map/`. The series *Beyond Faster Coding* stays in
  `vishalkhondre/ai-sdlc`, finished and maintained only; its session history is in the log below.
- **Seed (edition 1.0.0):** site engine, checks, CI, the map generator, glossary, references and
  workflow catalog, seeded from `vishalkhondre/ai-sdlc` at `4a997c8` without the chapter text.
  The home page shows the map and the adoption path as figures; the series parts are linked.
- **Current wave:** 0 Foundations — Q1 settled (generic labels); diagram text gated (D-009);
  confidentiality deny-list hashed and applied to all of `content/`, the built site and every
  tracked file (D-012).

## Next (in order)

1. Wave 0, first item: the clickable five-band map as the home page, with the purpose routing
   row (Understand / Build the kit / Run a workflow / Lead adoption / Look it up). Boxes without
   a page are plain labels (GR-3.2).
2. In `vishalkhondre/ai-sdlc`: replace `project/` with `MAINTENANCE.md` pointing here, and add a
   "See the whole picture" link on the series home page, through a reviewed PR.
3. Author answers the open questions Q2–Q4 in `ASSUMPTIONS.md`.
4. In `vishalkhondre/ai-sdlc`: the hashed deny-list (GR-1.4), as its own PR, and whether to
   rewrite history there. This repository already uses the hashed deny-list (D-012).
5. Wave 0: page templates, `.claude/agents` and skills (folding in `.github/agents`), new checks
   (banned phrases, template structure, link check, review-record gate, GR-2.5 access dates,
   outdated terms).
6. Wave 0: source inventory — every library document mapped to map boxes, gaps listed.

## Wave 0 retrospective items

Raised during the series' 1.1.0 release in `vishalkhondre/ai-sdlc`; decide at the wave 0
retrospective (GR-5.3).

- **Enforce the GR-2.5 access date.** `check_citations.py` should fail a reference without an
  `accessed` date. Only the three 1.1.0 references have one; the eight older entries need
  backfilling, from a real visit, before the check can be switched on.
- **Add an outdated-terms check.** Review 3 caught "program increment" (SAFe 6.0 says planning
  interval) and the map had said "the four DORA keys" after DORA moved to five metrics. A
  maintained list of superseded terms, checked against prose and diagram text, would catch these.
- **Review rounds.** 1.1.0 took four reviews: the first two REVISE on credits and product names,
  which the new diagram checks (D-009) now catch; the third REVISE on accuracy and GR-2.5. Each
  fresh reviewer found new issues rather than repeating old ones. Consider a reviewer checklist
  generated from the ground rules so a first review covers everything once.
- **Open review suggestions, not acted on in 1.1.0:** wider SAFe credit (built-in quality, PI
  cadence); visible DORA / SOC 2 credit line; "tend to become the sprawl" reads as an unsourced
  finding; product name in the changelog (extend D-009 or reword); glossary entries for DoR/DoD,
  WSJF (Reinertsen via SAFe) and flow metrics; `role="img"` / `aria-labelledby` if diagrams are
  ever inlined; DORA metrics guide as a more specific link than the research page.

## Wave tracker

| Wave | State | Pages planned | Pages published |
|---|---|---|---|
| 0 Foundations | in progress | — | — |
| 1 Core and lifecycle | not started | set by inventory | 0 |
| 2 Assurance and enablement | not started | set by inventory | 0 |
| 3 Context and adoption | not started | set by inventory | 0 |

## Session log

| # | Date | What happened | Handover |
|---|---|---|---|
| 1 | 2026-09-25 | *(in `ai-sdlc`)* Built and released 1.0.0; drew the five-band map and adoption path; reviewed the Hopsworks landing pattern; agreed the goal, ground rules and approach; wrote these project files | Two map commits and this commit need pushing; session could not push (repo not selected at start) |
| 2 | 2026-09-25 | *(in `ai-sdlc`)* Pushed 1.0.0 to GitHub and applied the publishing-and-review-gates patch; removed the Jekyll workflow; merged the map bundle; released 1.1.0 after four citation reviews (REVISE ×3, ACCEPT) plus a confirmation review of the author's reference URLs; diagram text checks and credit lines added (D-009) | Branch `claude/hopeful-pasteur-7og55e` deleted after merge; retrospective items above |
