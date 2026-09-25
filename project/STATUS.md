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
  SDLC entry) and references, each showing its access date. Released: `v1.2.0` (tag and GitHub
  Release with its PDF snapshot).
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

## Next (in order)

1. Release v1.3.0 on the author's instruction (the Release workflow on `main`).
2. Keyed deny-list (D-023); the author adds the CI secret `DENYLIST_KEY`.
3. Core section (D-018, `project/plans/core.md`), edition 1.4.0: tooling first (pages in
   `check_citations.py` and `site/generate.py`), then the pages through `section-pipeline`;
   deploy when every agent reviewer accepts; the author reviews live; tag after approval.
4. Re-check the references verified by search only, by a direct read, from a session whose
   network reaches the source sites.
5. Relabel the map's lifecycle levels generically (D-015), as a content edition of its own.
6. Wave 0 retrospective (APPROACH.md, Waves).

## For the author

- **Tag protection (D-024).** Settings → Rules → Rulesets → New tag ruleset: target
  `refs/tags/v*`; rules "Restrict creations", "Restrict updates", "Restrict deletions"; bypass
  list: the "Repository admin" role (the author) and the **GitHub Actions** app (it acts as
  `github-actions[bot]`, app ID 15368), mode "Always".
- **Keyed deny-list (D-023).** Generate a key (for example `python -c "import secrets;
  print(secrets.token_hex(32))"`) and add it as the repository secret `DENYLIST_KEY`; a session
  computes the hashes with it from an environment variable, never storing it in the repository.
- **"Feedback path" on the map (D-018).** The only map label containing it is adoption stage 3,
  "Feedback path proven", which links to the adoption path today. Confirm that this label should
  link to the harness engineering page, or name the label meant.
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
- **Deny-list lesson.** The seed first copied plain-text names from its source; review caught it
  and the seed commit was rebuilt. A commit that briefly held them was pushed to a branch and is
  now unreferenced; GitHub may keep unreferenced objects for a time.

## Wave tracker

| Wave | State | Pages planned | Pages published |
|---|---|---|---|
| 0 Foundations | in progress | — | — |
| 1 Core and lifecycle | Core plan approved (D-018) | 9 (core) | 0 |
| 2 Assurance and enablement | not started | set by inventory | 0 |
| 3 Context and adoption | not started | set by inventory | 0 |

## Session log

| # | Date | What happened | Handover |
|---|---|---|---|
| 1 | 2026-09-25 | *(in the earlier repository)* Built and released 1.0.0; drew the five-band map and adoption path; reviewed the Hopsworks landing pattern; agreed the goal, ground rules and approach; wrote these project files | Two map commits and this commit need pushing; session could not push (repo not selected at start) |
| 2 | 2026-09-25 | *(in the earlier repository)* Pushed 1.0.0 to GitHub and applied the publishing-and-review-gates patch; removed the Jekyll workflow; merged the map bundle; released 1.1.0 after four citation reviews (REVISE ×3, ACCEPT) plus a confirmation review of the author's reference URLs; diagram text checks and credit lines added (D-009) | Branch deleted after merge; retrospective items above |
| 3 | 2026-09-25 | Split the work (D-010): created and seeded `ai-sdlc-map` from the earlier repository without its chapter text; moved `CLAUDE.md` and `project/`; D-010, D-011 (confirmation reviews with `--prior`), D-012 (hashed deny-list); Q1 settled. Seed released as 1.0.0 (review REVISE then ACCEPT); fixed a search race that failed the first deploy; clickable map and routing row released as 1.1.0 (ACCEPT) | `role="group"` follow-up merged (PR #4). Author: delete the merged branches `claude/seed-site`, `claude/fix-search-race`, `claude/clickable-map`, `claude/map-links-a11y` and `claude/status-session-3` in GitHub (branch deletion is blocked from the session) |
| 4 | 2026-09-25 | Renamed the site The AI SDLC Map (D-013) and released edition 1.2.0 (PR #6; three reviewers ACCEPT after one editorial REVISE); recorded D-014 to D-016 with ground rules v1.1 and the release workflow; read the source library for the inventory (kept outside the repository) | Wave 0 remainder (edition 1.2.1): access-date and outdated-terms checks, page templates and `check_pages.py`, nine agents and ten skills, deny-list D-017, `project/COVERAGE.md`; release workflow run by hand when tag pushes failed (PR #8); v1.2.0 released; 1.2.1 merged (PR #9); Core section plan proposed (`project/plans/core.md`). | See Next and For the author |
