# Status

Update at the end of every session (see `CLAUDE.md`).

## Where things stand

- **Repository (D-010, D-019):** `vishalkhondre/ai-sdlc-map` builds *The AI SDLC Map* (D-013) at
  `vishalkhondre.github.io/ai-sdlc-map/`. It stands on its own: it does not link to or mention the
  earlier narrative series (D-019).
- **Live: edition 1.4.2, released.** The author approved the Core section (`v1.4.1`) and edition
  1.4.2 (`v1.4.2`, 2026-10-06), each a GitHub Release with its PDF snapshot; released tags are
  `v1.2.0`, `v1.3.0`, `v1.4.1` and `v1.4.2`. The site is
  The AI SDLC Map, with the subtitle "The AI-assisted software lifecycle, from spec to software
  factory, on one page." Home page: the clickable five-band map, the purpose routing row and the
  adoption path; nine Core reference pages; the workflow catalog, terminology and references.
- **Edition 1.4.2 (session 7):** diagrams on five Core pages (harness engineering, evidence schema,
  Engineering Kit, workflows, validators), the map's intro and caption wording, the adoption path's
  closing line as recommended practice; the library sweep as a gate on every content change (D-027);
  the keyed deny-list switch prepared (D-023); the wave 0 retrospective held and wave 0 closed
  (D-028). Review record `content/reviews/1.4.2-foundations.md`.
- **Decisions:** Q2–Q4 settled as D-014 (one section at a time; ground rules v1.1), D-015 (SAFe:
  generic labels plus a reference model) and D-016 (a tag and GitHub Release per approved
  section, `.github/workflows/release.yml`). Session 5 recorded D-018 to D-024: Core plan
  approved, disconnect from the series, documentation layout, Slate & Teal brand, the "draft"
  rule, keyed deny-list, tag protection (ground rules v1.2). Later: D-025 (Core answers), D-026
  (library sweep), D-027 (sweep as a gate on every content change), D-028 (wave 0 closed).
- **Wave 0 foundations in place:** checks for GR-2.5 access dates and superseded terms
  (`scripts/outdated_terms.yml`); six page templates (`templates/pages/`) and the page gate
  (`scripts/check_pages.py`, in CI); the nine agents and their skills plus `section-pipeline`
  (`.claude/`); the deny-list now case-folded, with word pairs and the inventory's identifiers
  (D-017); the source coverage table (`project/COVERAGE.md`; the inventory itself stays outside
  the repository). Edition 1.2.1 backfilled access dates and corrected seven references.
- **Current wave:** wave 0 Foundations is closed (D-028). Wave 1 continues with the lifecycle
  section; the Core section is released.

## Next (in order)

1. A small follow-up edition (optional): make the harness page call the feedback path the site's
   extension of the steering loop in all three places (editorial suggestion on 1.4.2), and add the
   dotted precondition line to the workflow diagram's legend.
2. Keyed deny-list (D-023): the author runs `scripts/denylist_rekey.py` (command in For the author)
   and pushes its result; a session then confirms CI is green with the key, and removes the salted
   fallback from `scripts/denylist.py` as a reviewed tooling change.
3. Relabel the map's lifecycle levels generically (D-015), as a content edition of its own.
4. Lifecycle section plan (architect): phases, their workflows and the SAFe reference model
   (D-015), carrying the deferred retrospective items listed below.

## For the author

- **Keyed deny-list (D-023).** In a local clone, with the names in a file outside the repository
  (one name per line, two-word names with one space), run:

      git checkout main && git pull && git checkout -b denylist-keyed
      python scripts/denylist_rekey.py --terms ~/denylist-terms.txt
      git add scripts/denylist_keyed.txt scripts/denylist_salted.txt
      git commit -m "Keyed deny-list values (D-023)" && git push -u origin denylist-keyed

  then open a pull request from `denylist-keyed`; CI runs the check with the key.

  It asks for `DENYLIST_KEY` without showing it, refuses to write anything unless the file covers
  every current value, writes only hashes and a key check, and deletes the salted list. If the
  key was not kept, generate a new one, replace the `DENYLIST_KEY` secret, and use that.
- **Leftover branch.** `claude/bold-maxwell-dy6hmz` is fully merged into `main`; delete it in
  GitHub (Branches page). Sessions cannot delete branches: the git proxy refuses it.
- **Purge request.** Ask GitHub Support to purge the unreferenced commits of the deleted working
  branch (the list is held for the author outside the repository).
- **The old repository.** It still holds employer names in plain text in a check script; the
  author removes them in the GitHub web editor or makes the repository private.

## Wave 0 retrospective (held 2026-10-06, D-028)

Each open item, with its outcome (GR-5.3).

| Item | Outcome |
|---|---|
| Close-paraphrase lesson: sweep before review | **Acted.** D-026, then D-027: the sweep runs for every content change, diagrams included, and from 1.4.2 a review record without `Library sweep:` fails `release_content.py` |
| Deny-list lesson: plain names once pushed | **Acted.** Keyed deny-list prepared (D-023); the purge request stays with the author |
| Reviewer checklists from the ground rules | **Done** (session 4) |
| Access-date check, outdated terms, case-folded hashes | **Done** (session 4, D-017) |
| References checked by search only | **Done** in 1.4.1 (every reference read at its source). The SOC 2 CC8.1 wording, confirmed only through secondary sources, is **deferred** to the assurance section, which owns that standard |
| Diagrams the Core reviewers asked for | **Acted** in 1.4.2 (five pages) |
| Map intro and caption wording (1.1.0 review, S4, S5) | **Acted** in 1.4.2 |
| "Tend to become the sprawl" read as an unsourced finding | **Acted** in 1.4.2: restated as a recommendation (GR-2.3) |
| `role="img"` / `aria-labelledby` on inlined diagrams | **Done**: inlined figures carry both |
| 404 page relative links at nested paths | **Done**: the 404 page links by absolute address |
| "This series" wording, `app.js` header and theme key | **Done** (D-019) |
| Wider SAFe credit (built-in quality, PI cadence) | **Deferred** to the lifecycle section and its SAFe reference model (D-015) |
| Glossary entries for DoR/DoD, WSJF, flow metrics | **Deferred** to the lifecycle and assurance sections: entries come with the page that uses them (D-025) |
| "Dependency / CVE fix" also to W29; "Migration · rollback" to W16 | **Deferred** to the lifecycle relabel (D-015), which changes those labels |
| DORA metrics guide as a more specific link | **Deferred** to the assurance section's measurement page |
| Visible DORA / SOC 2 credit line on the map | **Dropped**: credit lines name the sources of borrowed terms (D-009); the assurance pages cite DORA and SOC 2 |
| Product name in the changelog | **Dropped**: D-025 allows naming an organisation or product as the source of a cited term; no check is needed |

## Wave tracker

| Wave | State | Pages planned | Pages published |
|---|---|---|---|
| 0 Foundations | closed (D-028) | — | — |
| 1 Core and lifecycle | Core released (`v1.4.1`, `v1.4.2` with diagrams); lifecycle not started | 9 (core) | 9 |
| 2 Assurance and enablement | not started | set by inventory | 0 |
| 3 Context and adoption | not started | set by inventory | 0 |

## Session log

| # | Date | What happened | Handover |
|---|---|---|---|
| 1 | 2026-09-25 | *(in the earlier repository)* Built and released 1.0.0; drew the five-band map and adoption path; reviewed the Hopsworks landing pattern; agreed the goal, ground rules and approach; wrote these project files | Two map commits and this commit need pushing; session could not push (repo not selected at start) |
| 2 | 2026-09-25 | *(in the earlier repository)* Pushed 1.0.0 to GitHub and applied the publishing-and-review-gates patch; removed the Jekyll workflow; merged the map bundle; released 1.1.0 after four citation reviews (REVISE ×3, ACCEPT) plus a confirmation review of the author's reference URLs; diagram text checks and credit lines added (D-009) | Branch deleted after merge; retrospective items above |
| 3 | 2026-09-25 | Split the work (D-010): created and seeded `ai-sdlc-map` from the earlier repository without its chapter text; moved `CLAUDE.md` and `project/`; D-010, D-011 (confirmation reviews with `--prior`), D-012 (hashed deny-list); Q1 settled. Seed released as 1.0.0 (review REVISE then ACCEPT); fixed a search race that failed the first deploy; clickable map and routing row released as 1.1.0 (ACCEPT) | `role="group"` follow-up merged (PR #4). Author: delete the merged branches `claude/seed-site`, `claude/fix-search-race`, `claude/clickable-map`, `claude/map-links-a11y` and `claude/status-session-3` in GitHub (branch deletion is blocked from the session) |
| 4 | 2026-09-25 | Renamed the site The AI SDLC Map (D-013) and released edition 1.2.0 (PR #6; three reviewers ACCEPT after one editorial REVISE); recorded D-014 to D-016 with ground rules v1.1 and the release workflow; read the source library for the inventory (kept outside the repository) | Wave 0 remainder (edition 1.2.1): access-date and outdated-terms checks, page templates and `check_pages.py`, nine agents and ten skills, deny-list D-017, `project/COVERAGE.md`; release workflow run by hand when tag pushes failed (PR #8); v1.2.0 released; 1.2.1 merged (PR #9); Core section plan proposed (`project/plans/core.md`). | See Next and For the author |
| 5 | 2026-09-25 | Recorded D-018 to D-024 (PR #10); disconnected the site from the series (D-019); documentation layout with a page-text guard and axe checks (D-020, PR #13); Slate & Teal brand with bundled fonts, logo, favicon and social card (D-021, PR #14); released v1.3.0 through the Release workflow; pages tooling reviewed in three rounds and merged (PR #15); Core research (nine practice and nine evidence briefs, scratchpad only), nine pages written and integrated; review round 1 REVISE ×3 plus about 70 close paraphrases found by a library sweep; all pages revised | Core on `local/core-pages` (not pushed): re-sweep, review rounds 2–3, PR, merge. Keyed deny-list waits for `DENYLIST_KEY`. See For the author |
| 6 | 2026-09-28 | Applied the author's answers (D-025) and the library-sweep rule (D-026); merged and deployed the Core section as edition 1.4.0 (PR #16) after the superseded draft branch was removed; applied the external reference check as edition 1.4.1 (claim fixes, reference details, the AWS AI-DLC link; three reviewers ACCEPT) | Author: live review, then tag; keyed deny-list hashing script; purge request for the old draft commits |
| 7 | 2026-10-06 | Closed wave 0: STATUS brought up to date (Core released as `v1.4.1`); the library sweep made a gate on every content change (D-027); the keyed deny-list switch built and tested, waiting for the author's hashing run (D-023); wave 0 retrospective held (D-028); diagrams on five Core pages and the home-page wording fixes as edition 1.4.2 | 1.4.2 merged (PR #18) and released as `v1.4.2` on the author's instruction, through the Release workflow (tag pushes are refused by tag protection; the first run's release job failed on a one-off Chromium screenshot error and passed on re-run). Leftover branch could not be deleted from the session. Author: run the rekey command |
