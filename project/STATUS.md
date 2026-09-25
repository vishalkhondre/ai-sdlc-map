# Status

Update at the end of every session (see `CLAUDE.md`).

## Where things stand

- **Repositories (D-010):** this repository, `vishalkhondre/ai-sdlc-map`, builds *AI SDLC on one
  page* at `vishalkhondre.github.io/ai-sdlc-map/`. The series *Beyond Faster Coding* stays in
  `vishalkhondre/ai-sdlc`, finished and maintained only (its `MAINTENANCE.md`); its home page
  links here ("See the whole picture"), and its session history is in the log below.
- **Live: edition 1.1.0.** Home page: the clickable five-band map (18 linked labels, listed in
  `content/diagrams/map/links.yml`; the rest plain) with the purpose routing row, and the
  adoption path. Also the workflow catalog, terminology and references. The series parts are
  linked, not copied.
- **Review record:** `content/reviews/1.1.0-clickable-map.md` (ACCEPT) is bound in
  `content/release-review.json`, pointing to `1.0.0-seed-confirmation.md`, which points to the
  series' 1.1.0 reviews (D-011).
- **Current wave:** 0 Foundations — first item (clickable map) done; Q1 settled; diagram text
  gated (D-009); hashed deny-list (D-012).

## Next (in order)

1. Follow-up (tooling): links inside the map sit under `role="img"`, which can hide them from
   screen readers; emit `role="group"` for diagrams with links, and add an automated check.
2. Author answers the open questions Q2–Q4 in `ASSUMPTIONS.md`.
3. In `vishalkhondre/ai-sdlc`: the hashed deny-list (GR-1.4), as its own PR, and whether to
   rewrite history there. This repository already uses one (D-012).
4. Wave 0: page templates, `.claude/agents` and skills (folding in `.github/agents`), new checks
   (banned phrases, template structure, link check, review-record gate, GR-2.5 access dates,
   outdated terms).
5. Wave 0: source inventory — every library document mapped to map boxes, gaps listed.

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

- **Open review suggestions from this repository's 1.0.0 and 1.1.0 reviews:** "this series" in
  glossary definitions and reference notes, and bare "Part 5 / Part 6" in two catalog notes, now
  read on a different site; case-folded deny-list hashes; `app.js` header and theme key still
  carry the series name; 404 page relative links at nested paths; "Dependency / CVE fix" could
  also point to W29; "Migration · rollback" could link W16; caption and intro wording on the
  map (S4, S5 of the 1.1.0 review).
- **Deny-list lesson.** The seed first copied plain-text names from `ai-sdlc`; review caught it
  and the seed commit was rebuilt. A commit that briefly held them was pushed to a branch and is
  now unreferenced; GitHub may keep unreferenced objects for a time.

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
| 3 | 2026-09-25 | Split the work (D-010): created and seeded `ai-sdlc-map` from `ai-sdlc` at `4a997c8` without the chapter text; moved `CLAUDE.md` and `project/`; D-010, D-011 (confirmation reviews with `--prior`), D-012 (hashed deny-list); Q1 settled. Seed released as 1.0.0 (review REVISE then ACCEPT); fixed a search race that failed the first deploy; `ai-sdlc` handed over with `MAINTENANCE.md` and a whole-picture link (ACCEPT); clickable map and routing row released as 1.1.0 (ACCEPT) | Merged branches may still need deleting in GitHub (branch deletion is blocked from the session); next: the `role="group"` follow-up |
