# Status

Update at the end of every session (see `CLAUDE.md`).

## Where things stand

- **Repository (D-010, D-019):** `vishalkhondre/ai-sdlc-map` builds *The AI SDLC Map* (D-013) at
  `vishalkhondre.github.io/ai-sdlc-map/`. It stands on its own: it does not link to or mention the
  earlier narrative series (D-019).
- **Edition 1.6.0 (session 11, 2026-11-27): Lifecycle, part two.** The seven workflow pages (intake and
  triage, specification readiness, design conformance, pull-request verification, deploy verification,
  release readiness, incident feedback), the seven map links moved to them, link-only edits in seven
  phase pages and three Core pages, 13 references, 5 glossary entries (D-032). Library sweep clean
  after two rounds and the final D2 sweep; three reviewers in two groups; pull request #28. The author
  asked for it to be deployed without waiting for his review; he reviews it live and tags at approval.
- **Edition 1.5.0, Lifecycle part one, merged and deployed (PR #24, 2026-11-21), not yet tagged.** The
  author's live review and the `v1.5.0` tag are still open.
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
  (library sweep), D-027 (sweep as a gate on every content change), D-028 (wave 0 closed), D-029
  (Lifecycle approved as two editions).
- **Wave 0 foundations in place:** checks for GR-2.5 access dates and superseded terms
  (`scripts/outdated_terms.yml`); six page templates (`templates/pages/`) and the page gate
  (`scripts/check_pages.py`, in CI); the nine agents and their skills plus `section-pipeline`
  (`.claude/`); the deny-list now case-folded, with word pairs and the inventory's identifiers
  (D-017); the source coverage table (`project/COVERAGE.md`; the inventory itself stays outside
  the repository). Edition 1.2.1 backfilled access dates and corrected seven references.
- **Current wave:** wave 0 Foundations is closed (D-028). Wave 1 continues with the lifecycle
  section; the Core section is released. **Lifecycle plan approved 2026-10-06 (D-029, merged in
  PR #19):** edition 1.5.0 (12 pages) and edition 1.6.0 (7 workflow pages), each reviewed live and
  tagged separately.
- **GR-6.1 stays as written (author, 2026-11-20).** D-029 records the two-edition split as an
  exception for Lifecycle, so `GROUND-RULES.md` is not amended. Revisit only if another band needs
  to ship in parts.

## Next (in order)

0. **Assurance plan approved (D-033).** Order: the 1.4.x fix edition first (catalog rows and
   published passages listed under the D-030 diagnostic and the 1.6.0 sweep, plus catalog-row links to
   the workflow pages), then Assurance as edition 1.7.0 through the same pipeline. Author, before
   batch C of 1.7.0: paste the SOC 2 change-management criterion (CC8.1) if wanted. Author: confirm or
   reverse D-032, and say whether workflow pages may name the deciding role themselves
   (spec readiness, release readiness and incident feedback now defer to the catalog row). Live review of 1.5.0 and 1.6.0, then tags.
1. A small follow-up edition (optional): make the harness page call the feedback path the site's
   extension of the steering loop in all three places (editorial suggestion on 1.4.2), and add the
   dotted precondition line to the workflow diagram's legend.
2. Keyed deny-list (D-023): the author runs `scripts/denylist_rekey.py` (command in For the author)
   and pushes its result; a session then confirms CI is green with the key, and removes the salted
   fallback from `scripts/denylist.py` as a reviewed tooling change.
3. **Lifecycle section (D-029), two editions; plan in `project/plans/lifecycle.md`.** 1.5.0 (12
   pages, includes the D-015 relabel) first, then 1.6.0 (the seven workflow pages).
   1. Source check by direct reading: `project/handover/lifecycle-1.5-source-check-worklist.md`,
      results in `project/handover/lifecycle-1.5-source-check-results.md` on a branch, reviewed by
      the author. The environment's allow-list now covers the SAFe, DORA, Scrum Guide, Fowler, SRE
      and NIST hosts; `openai.com` and `iso.org` are listed but answer plain requests with a
      Cloudflare challenge, so ISO catalogue pages are not readable from a session.
   2. Finalise the skeletons from the checked sources, write batch A, run the sweep. The briefs,
      skeletons and library diffs from session 8 exist only in that session's scratchpad (GR-1.3,
      D-026) and cannot be handed over in git; a new session rebuilds them from the plan.
   3. Page work stays on a local branch that is not pushed until the sweeps pass and the author
      has read the SAFe reference model page in chat. Decided: one sentence on AI-Native SAFe; add
      the superseded NIST SP 800-61 Rev. 2 and ISO/IEC/IEEE 12207:2017 to `outdated_terms.yml`
      once their references exist.
   4. 1.5.0: review, merge, author's live review, tag. Then 1.6.0 on the same steps. The deferred
      retrospective items for this section are listed below.

## 1.4.x findings from the D-030 catalog diagnostic (2026-11-21)

The Lifecycle 1.5.0 batch A sweep stopped at round 2 (D-030). On the author's instruction a diagnostic
sweep compared the published rows and passages the batch A pages had restated with the source library.
Locations and verdicts only; the findings name nothing from the library (GR-1.2). They are fixed in a
**separate 1.4.x fix edition** through the full pipeline (sweep, fresh-author rewrite, three reviewers,
D-011 confirmation review); the Lifecycle edition does not change any of them.

| Published item | Fields or heading | Verdict | GR |
|---|---|---|---|
| Catalog W01 | agent, checks, people | close | 1.2 (and 1.1 / D-017, see note) |
| Catalog W08 | agent, checks, people, evidence, notes | close | 1.2 (and 1.1 / D-017) |
| Catalog W12 | decision, agent, checks, people | close | 1.2 (and 1.1 / D-017) |
| Catalog W22 | people, notes | close | 1.2; people field also 1.1 (domain fingerprint) |
| Catalog W25 | people | close | 1.2 (and 1.1 / D-017) |
| Catalog W28 | agent | close | 1.2 |
| Core `workflows` | "Risk tiers: same definition, different cost" | close | 1.2 |
| Core `software-factory` | "Three things are shared" (Rules bullet); "Production feedback reaches specification" | close | 1.2 |
| Glossary `review-fatigue` | the entry | close | 1.2 |

Borderline, to be checked in the same edition: catalog W04, W13, W17, W23, W26 and the borderline
fields of the rows above; Core `workflows` (Guardrails row, Failure paths, What a workflow hands on,
Pitfalls), `software-factory` (People keep the decisions, Pitfalls), `harness-engineering` (feedback-path
destination list), `rule-registry` (entry and identifiers), `validators` (From report-only to required);
glossary `feedback-path`. Clean: W27, W30, W35; `rule-registry` "How the rest of the kit refers to rules";
`evidence-schema` revisions and agent findings.

Note (GR-1.1, D-017): ordinary words that the library uses as its own names appear in close and
borderline fields of W01, W08, W12, W22 and W25. The hashed deny-list cannot catch them; the
confidentiality review of the fix edition reads those fields as a public reader would.

### Added by the 1.6.0 sweep (2026-11-27)

The 1.6.0 sweep flagged page passages that restated published text; they were cut from the new pages,
and the published text they restated is logged here for the same 1.4.x fix edition (locations only):

| Published item | Location | Verdict | GR |
|---|---|---|---|
| Core `workflows` | three-roles section, one sentence | close | 1.2 |
| Glossary `risk-tier` | definition, first sentence | close | 1.2 |
| Catalog W01 | Decision field (already listed above) | close | 1.2 |

## Backlog

- Catalog rows link to their workflow pages (W01, W04, W08, W23, W25, W26, W28): changes the live
  catalog, so it waits for the 1.4.x fix edition or the author (D-032).
- Agent-stop failure path on four workflow pages (spec readiness, pull-request verification, release
  readiness, incident feedback), or once in Core `workflows#failure-paths`: editorial suggestion
  from the 1.6.0 review, for the 1.4.x fix edition.
- Catalog consistency pass (W12 wording): the W12 row says "definition of ready" while the map
  and adoption path place it at Specification (D-029, question 8).

## For the author

- **1.4.x findings (above).** Decide when the fix edition runs; it changes live catalog rows, Core
  passages and one glossary entry, so it may precede or follow 1.5.0.
- **SAFe reference model page (D-029).** Its text is shown in chat for the author to read before it
  is first pushed.
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
| 1 Core and lifecycle | Core released (`v1.4.1`, `v1.4.2`); Lifecycle 1.5.0 deployed (untagged); 1.6.0 in PR #28 | 9 (core) + 12 (1.5.0) + 7 (1.6.0) | 21 (28 with 1.6.0) |
| 2 Assurance and enablement | Assurance plan proposed (draft PR #27), awaiting the author | set by inventory | 0 |
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
| 8 | 2026-10-06 | Planned the Lifecycle section (architect); the author approved it as two editions (D-029) and answered eight questions; updated the Core plan and this file; opened the plan pull request; started the 1.5.0 briefs and public-skeleton research | Page work on a local branch, nothing pushed; SAFe page text to the author in chat before its first push; see Next item 3 |
| 9 | 2026-11-20 | Merged the Lifecycle plan pull request (PR #19); recorded that GR-6.1 stays as written (D-029 holds the exception); brought the wave tracker and Next to the two-edition plan; started the 1.5.0 source check (its results go in their own pull request) | See Next item 3 |
| 10 | 2026-11-27 | Restyled the site with the author's locked AI SDLC design system v1.0 (D-031, supersedes D-021): Inter and JetBrains Mono bundled, new tokens in both themes, the diagram palette mapped onto the band colours at build time, and an interaction layer (map hover and band focus, legend, icons, motion, back to the map). Site only: no content change, no edition bump. Pull request open for the author's review, not merged | Author reviews the preview and the pull request |
| 11 | 2026-11-27 | Overnight, on the author's instruction to complete the map without waiting for him: found that 1.5.0 was merged but STATUS was stale; built edition 1.6.0 (the seven workflow pages) through briefs, public skeletons, library concept diffs, two sweep rounds (five pages had close passages cut and rewritten by fresh authors; design conformance rewritten), the final D2 sweep, and three reviewers in two groups; recorded D-032; proposed the Assurance plan (draft PR #27) | Author: Assurance plan questions, D-032, live review and tags of 1.5.0 and 1.6.0 |
