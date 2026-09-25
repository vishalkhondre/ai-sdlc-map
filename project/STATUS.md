# Status

Update at the end of every session (see `CLAUDE.md`).

## Where things stand

- **Repository (D-010, D-019):** `vishalkhondre/ai-sdlc-map` builds *The AI SDLC Map* (D-013) at
  `vishalkhondre.github.io/ai-sdlc-map/`. It stands on its own: it does not link to or mention the
  earlier narrative series (D-019).
- **Live: edition 1.3.0** (main deploys continuously): the site no longer links to or names the
  earlier series (D-019), pages use the documentation layout (D-020), and the site
  carries the Slate & Teal brand (D-021). The site is The AI SDLC Map, with the
  subtitle "The AI-assisted software lifecycle, from spec to software factory, on one page." Home
  page: the clickable five-band map (18 linked labels in `content/diagrams/map/links.yml`), the
  purpose routing row and the adoption path; also the workflow catalog, terminology (with the AI
  SDLC entry) and references, each showing its access date. Released: `v1.2.0` and `v1.3.0` (tags
  and GitHub Releases with their PDF snapshots). The pages tooling for reference pages is merged
  (PR #15): `check_citations.py` and `check_pages.py` cover `content/pages/`, and `site/generate.py`
  renders them.
- **Review record:** `content/reviews/1.3.0-brand.md` (confidentiality, accuracy and editorial
  ACCEPT) is bound in `content/release-review.json`, pointing to `1.3.0-layout.md`. The
  confidentiality reviewer found the brand resembles no employer's design system (D-021).
- **Decisions:** Q2–Q4 settled as D-014 (one section at a time; ground rules v1.1), D-015 (SAFe:
  generic labels plus a reference model) and D-016 (a tag and GitHub Release per approved
  section, `.github/workflows/release.yml`). Session 5 recorded D-018 to D-024: Core plan
  approved, disconnect from the series, documentation layout, Slate & Teal brand, the "draft"
  rule, keyed deny-list, tag protection (ground rules v1.2).
- **Wave 0 foundations in place:** checks for GR-2.5 access dates and superseded terms
  (`scripts/outdated_terms.yml`); six page templates (`templates/pages/`) and the page gate
  (`scripts/check_pages.py`, in CI); the nine agents and their skills plus `section-pipeline`
  (`.claude/`); the deny-list now case-folded, with word pairs and the inventory's identifiers
  (D-017); the source coverage table (`project/COVERAGE.md`; the inventory itself stays outside
  the repository). Edition 1.2.1 backfilled access dates and corrected seven references.
- **Current wave:** 0 Foundations closing; the Core plan is approved (D-018). Decisions D-018 to
  D-024 recorded 2026-09-25 (session 5).
- **Core section (edition 1.4.0), awaiting the author's live review.** All nine
  pages are written and wired in (map links for the kit's five parts, routing row, 95 references,
  10 terms). Review round 1: confidentiality REVISE (a vendor named in prose), accuracy REVISE
  (term origin, one overstated source, three titles/bylines), editorial REVISE (running-example
  timeline, operating state, mechanism vs meaning, merge meaning on the adapters page).  A
  close-paraphrase check by the source researcher (GR-1.2) led to a full revision of every page
  before review round 2. Lesson: the author agent needs a paraphrase sweep before the
  first review, not after (see retrospective).

## Next (in order)

1. Core section, edition 1.4.0: merged and deployed after three review rounds and confirmations
   (all ACCEPT). The author reviews it live; follow-ups are 1.4.x; tag `v1.4.0` after approval.
2. Keyed deny-list (D-023): `DENYLIST_KEY` is in place; write the one-off local hashing script for
   the author, then switch `scripts/denylist.py` to keyed hashes as a reviewed change.
3. Diagrams for the Core pages the reviewers named (harness engineering, evidence schema,
   Engineering Kit, workflows, validators), as a 1.4.x follow-up.
4. Re-check the references verified by search only, by a direct read, from a session whose
   network reaches the source sites.
5. Relabel the map's lifecycle levels generically (D-015), as a content edition of its own.
6. Wave 0 retrospective (APPROACH.md, Waves).

## For the author

- **Tag protection (D-024):** set by the author.
- **Keyed deny-list (D-023).** The key is added as `DENYLIST_KEY`. Still to do: compute the keyed
  hashes with a one-off local script run by the author (the terms never enter the repository).
- **Purge request.** Ask GitHub Support to purge the unreferenced commits of the deleted working
  branch (the list is held for the author outside the repository).
- **Core questions:** answered by the author (D-025).
- **Network policy.** Most primary sources (martinfowler.com, thoughtworks.com, dora.dev, nist.gov,
  arxiv.org and others) are blocked here; about 46 Core references are checked from search
  results only. Allow those hosts in the environment's network settings, or re-check them from a
  session that can reach them, before the release tag.
- **The old repository.** It still holds employer names in plain text in a check script; the
  author removes them in the GitHub web editor or makes the repository private.

## Wave 0 retrospective items

Raised during earlier releases; decide at the wave 0 retrospective (GR-5.3).

- **Done in session 4:** the GR-2.5 access-date check and the outdated-terms list are in
  `check_citations.py`; reviewer checklists generated from the ground rules are in the reviewer
  skills; deny-list hashes are case-folded (D-017). The eight older references were checked
  through search results and one direct fetch, because this session's network policy blocks
  martinfowler.com, openai.com, thoughtworks.com and wikipedia.org: re-check them from a session
  that can open the pages (see `content/reviews/1.2.1-wave0.md`).
- **Review rounds** (done in session 4: reviewer checklists generated from the ground rules are
  in the reviewer skills). 1.1.0 took four reviews: the first two REVISE on credits and product names,
  which the new diagram checks (D-009) now catch; the third REVISE on accuracy and GR-2.5. Each
  fresh reviewer found new issues rather than repeating old ones. Consider a reviewer checklist
  generated from the ground rules so a first review covers everything once.
- **Open review suggestions, not acted on in 1.1.0:** wider SAFe credit (built-in quality, PI
  cadence); visible DORA / SOC 2 credit line; "tend to become the sprawl" reads as an unsourced
  finding; product name in the changelog (extend D-009 or reword); glossary entries for DoR/DoD,
  WSJF (Reinertsen via SAFe) and flow metrics; `role="img"` / `aria-labelledby` if diagrams are
  ever inlined; DORA metrics guide as a more specific link than the research page.

- **Open review suggestions from this repository's 1.0.0 and 1.1.0 reviews:** "this series" in
  glossary definitions and reference notes and bare part numbers in two catalog notes (done, D-019);
  case-folded deny-list hashes (done, D-017); `app.js` header and theme key (done, D-019); 404 page relative links at nested paths; "Dependency / CVE fix" could
  also point to W29; "Migration · rollback" could link W16; caption and intro wording on the
  map (S4, S5 of the 1.1.0 review).
- **Close-paraphrase lesson (session 5).** The Core authors worked from de-identified practice
  briefs and still reproduced library structure, lists and example sets. The confidentiality
  reviewer cannot see the library, so it cannot catch this. Add a source-researcher paraphrase
  sweep of every draft page to `section-pipeline`, between Write and Check.
- **Deny-list lesson.** The seed first copied plain-text names from its source; review caught it
  and the seed commit was rebuilt. A commit that briefly held them was pushed to a branch and is
  now unreferenced; GitHub may keep unreferenced objects for a time.

## Wave tracker

| Wave | State | Pages planned | Pages published |
|---|---|---|---|
| 0 Foundations | in progress | — | — |
| 1 Core and lifecycle | Core pages written, in review (1.4.0) | 9 (core) | 0 |
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
