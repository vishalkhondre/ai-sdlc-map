# Status

Update at the end of every session (see `CLAUDE.md`).

## Where things stand

- **Repositories (D-010):** this repository, `vishalkhondre/ai-sdlc-map`, builds *The AI SDLC Map*
  (D-013) at `vishalkhondre.github.io/ai-sdlc-map/`. The series *Beyond Faster Coding* stays in
  `vishalkhondre/ai-sdlc`, finished and maintained only (its `MAINTENANCE.md`); its home page
  links here ("See the whole picture", now naming The AI SDLC Map), and its session history is
  in the log below.
- **Live: edition 1.2.0** (merged, not yet tagged). The site is The AI SDLC Map, with the
  subtitle "The AI-assisted software lifecycle, from spec to software factory, on one page." Home
  page: the clickable five-band map (18 linked labels in `content/diagrams/map/links.yml`), the
  purpose routing row and the adoption path; also the workflow catalog, terminology (now with
  the AI SDLC entry) and references.
- **Review record:** `content/reviews/1.2.0-rename.md` (confidentiality, accuracy and editorial
  ACCEPT) is bound in `content/release-review.json`, pointing to `1.1.0-clickable-map.md`.
- **Decisions:** Q2–Q4 settled as D-014 (one section at a time; ground rules v1.1), D-015 (SAFe:
  generic labels plus a reference model) and D-016 (a tag and GitHub Release per approved
  section, `.github/workflows/release.yml`).
- **Wave 0 foundations in place:** checks for GR-2.5 access dates and superseded terms
  (`scripts/outdated_terms.yml`); six page templates (`templates/pages/`) and the page gate
  (`scripts/check_pages.py`, in CI); the nine agents and their skills plus `section-pipeline`
  (`.claude/`); the deny-list now case-folded, with word pairs and the inventory's identifiers
  (D-017); the source coverage table (`project/COVERAGE.md`; the inventory itself stays outside
  the repository). Edition 1.2.1 backfilled access dates and corrected five references.
- **Current wave:** 0 Foundations; next is the first section plan.

## Next (in order)

1. Author: tag `v1.2.0` on `main` (or ask a session to), which is also the first run of the
   release workflow (D-016).
2. In `vishalkhondre/ai-sdlc`: the hashed deny-list (GR-1.4), as its own PR, no history rewrite.
3. Relabel the map's lifecycle levels generically (D-015), as a content edition of its own.
4. Architect: propose the first section's page list for the author's approval (D-014).

## Wave 0 retrospective items

Raised during the series' 1.1.0 release in `vishalkhondre/ai-sdlc`; decide at the wave 0
retrospective (GR-5.3).

- **Done in session 4:** the GR-2.5 access-date check and the outdated-terms list are in
  `check_citations.py`; reviewer checklists generated from the ground rules are in the reviewer
  skills; deny-list hashes are case-folded (D-017). The eight older references were checked
  through search results and one direct fetch, because this session's network policy blocks
  martinfowler.com, openai.com, thoughtworks.com and wikipedia.org: re-check them from a session
  that can open the pages (see `content/reviews/1.2.1-wave0.md`).
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
| 3 | 2026-09-25 | Split the work (D-010): created and seeded `ai-sdlc-map` from `ai-sdlc` at `4a997c8` without the chapter text; moved `CLAUDE.md` and `project/`; D-010, D-011 (confirmation reviews with `--prior`), D-012 (hashed deny-list); Q1 settled. Seed released as 1.0.0 (review REVISE then ACCEPT); fixed a search race that failed the first deploy; `ai-sdlc` handed over with `MAINTENANCE.md` and a whole-picture link (ACCEPT); clickable map and routing row released as 1.1.0 (ACCEPT) | `role="group"` follow-up merged (PR #4). Author: delete the merged branches `claude/seed-site`, `claude/fix-search-race`, `claude/clickable-map`, `claude/map-links-a11y` and `claude/status-session-3` in GitHub (branch deletion is blocked from the session) |
| 4 | 2026-09-25 | Renamed the site The AI SDLC Map (D-013) and released edition 1.2.0 (PR #6; three reviewers ACCEPT after one editorial REVISE); renamed the whole-picture link in `ai-sdlc` (its PR #3); recorded D-014 to D-016 with ground rules v1.1 and the release workflow; read the source library for the inventory (kept outside the repository) | Continues in this session: see Next |
