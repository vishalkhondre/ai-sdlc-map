# Decision log

Newest last. Each entry: what was decided, why, and what it rules out. Reopen only with the
author.

## D-001 · Independent, public work
The site is the author's independent work. It carries no reference to any employer or its
internal work. Rules out: case studies, internal names, internal numbers (GR-1).

## D-002 · Licences
Prose CC BY 4.0, tooling MIT. *The title and home recorded here belonged to the earlier narrative
series; the site's name is set by D-013 and its home by D-010.*

## D-003 · The one-page map is the site's front door
The five-band AI SDLC map becomes the landing page with every box clickable, following the
Hopsworks documentation overview pattern. Rules out: a blog-style home page.
*The landing-page part is superseded by D-010: the map is the front door of its own site.*

## D-004 · Claude Code agents, not GitHub Copilot agents
The source library is reachable only through the Google Drive connector in Claude sessions.
Rules out: a Copilot-only agent fleet for research. CI stays GitHub Actions.

## D-005 · Private sources never enter the repo
Practice briefs drawn from the library live only in session scratch space and are discarded.
Only de-identified, rewritten pages are committed. Rules out: a `content/sources/` folder of
extracts.

## D-006 · Reviewer gate enforced in CI
Every published page needs a review record with ACCEPT from the confidentiality, accuracy and
editorial reviewers, tied to the page hash. Rules out: publishing on author judgment alone
without a record.

## D-007 · Reference register, complete pages only
No provisional language on the site; unwritten map boxes appear as plain labels. Rules out:
"coming soon" markers and partial pages.

## D-008 · Diagrams as code, vendor-neutral
All diagrams are generated from source, with text alternatives. Tool names appear only as
examples on category pages.

## D-009 · Diagram text is gated like prose
From review finding GR-3.3 on the 1.1.0 map (GR-5.3: a recurring finding becomes a check).
`scripts/check_citations.py` now reads every diagram's text, title and description and fails on
the keep-out list or a product name, and each diagram lists the references it relies on in a
`data-references` attribute that the gate resolves. A diagram no chapter embeds must carry a
credit line (`<text class="credit">`) naming the source of every adopted or adapted glossary
term it uses; like a chapter footnote, a credit line may name a source product but never a
keep-out name. Rules out: product names in diagram body text, uncredited borrowed terms in
downloadable diagrams, and references that only a diagram uses being reported as dead.

## D-010 · Separate site for the map
Decided 2026-09-25 by the author; supersedes the landing-page part of D-003. The map is built in
`vishalkhondre/ai-sdlc-map`, served at `vishalkhondre.github.io/ai-sdlc-map/`, with its own release
cycle, review gate and changelog (starting at edition 1.0.0). It was seeded from the earlier
narrative series without that series' text. Reason: a separate repository gives the map its own
URL, release cycle and review gate, and leaves the earlier site's published address unchanged.
Rules out: duplicating another site's text.
*The cross-linking with the series that this decision also set up is superseded by D-019.*

## D-011 · A confirmation review may reuse a prior ACCEPT
Decided 2026-09-25 by the author. A review limited to a diff may rely on an earlier full review
for everything outside that diff, when the release record points to the earlier report.
`scripts/release_content.py record-review --report <confirmation> --prior <earlier report>`
records both; the check fails if the earlier report is missing, no longer says ACCEPT, or has
changed since it was recorded. The confirmation report still binds the current sources and must
state its scope and what it takes from the earlier review. Rules out: re-recording an earlier
report against sources it never saw, and a fresh full review for every small follow-up change.

## D-012 · Hashed deny-list from the first commit of the map site
Decided 2026-09-25 on a seed-review finding (GR-1.1, GR-1.4). This repository never holds the
confidentiality names in plain text. `scripts/denylist.py` stores salted SHA-256 hashes;
`check_citations.py` scans every text file under `content/`, and the site tests scan the built
pages and every tracked file. Matches are reported by position only. Vendor keep-out names stay
in plain text in `check_citations.py`, because they reveal nothing confidential. A salted hash of
a short name can still be found by trying candidate names; the salt only stops precomputed
lists. Rules out: plain-text employer names anywhere in this repository or its history.
*The published salt is replaced by a keyed hash (D-023).*

## D-013 · Name: The AI SDLC Map
Decided 2026-09-25 by the author. The site is called **The AI SDLC Map**, subtitle "The
AI-assisted software lifecycle, from spec to software factory, on one page." The URL
`vishalkhondre.github.io/ai-sdlc-map/` and the repository name do not change. The term is
"AI SDLC", without a hyphen; each page spells out "software development lifecycle" at the first
use of the term in its body text. The glossary entry "AI SDLC" separates it from two nearby uses:
the lifecycle for building AI and machine-learning systems, and AWS's AI-Driven Development
Lifecycle (AI-DLC), one vendor's named methodology (sources: IBM Think and AWS Builder Center,
accessed 2026-09-25). Released as edition 1.2.0 and tag `v1.2.0`. Rules out: "AI SDLC on one
page" as the site name, "AI-SDLC", and following any single vendor's methodology.

## D-014 · Build and approve one section at a time
Decided 2026-09-25 by the author (Q2); replaces the per-page approval in GR-6.1 and removes the
human approver from the GR-5.2 review record (ground rules v1.1). A section is one band of the map (context, lifecycle, core, enablement, assurance) or the
adoption path. The flow for a section: the architect plans it and the author approves the plan (carried over from the approval of
each wave plan);
agents research, write and review every page of it; when every required reviewer returns ACCEPT
it merges to `main` and deploys; the author reviews it on the live site; changes come as
follow-up pull requests, reviewed the same way; the author approves the section; its release is
tagged (D-016). Pages still go live only when complete and agent-accepted (GR-3.2, GR-4.1).
Review loops are capped at three rounds, after which the findings go to the author. Rules out:
author approval of each page before it merges, and publishing part of a section's pages as
incomplete.

## D-015 · SAFe: generic labels on the map, plus one reference model
Decided 2026-09-25 by the author (Q3). The map's lifecycle levels are labelled generically
(portfolio / train / team), with SAFe cited as one framework that uses them; the map today says
"SAFe levels" and "Agile Release Train", so it is relabelled in a content edition of its own. The
lifecycle section adds a worked **SAFe reference model** page that maps the AI SDLC onto SAFe
levels and events. It is informed by the source library (A3), which makes it the page with the
highest confidentiality risk: it is presented only as "a reference
model", its origin is not named, it is de-identified in full, the confidentiality reviewer checks
it against GR-1, and the author confirms it is not recognisable before its section is released
(GR-1.2). Rules out: SAFe-specific labels as the only lifecycle vocabulary, and any wording that
lets a reader identify where the model came from.
*The relabel ships inside the Lifecycle section's first edition, 1.5.0 (D-029).*

## D-016 · A tag and a GitHub Release for each approved section
Decided 2026-09-25 by the author (Q4). `main` deploys continuously; a tag marks the author's
approval. Each approved section gets a semver tag and a GitHub Release, one minor version per
section; the rename to The AI SDLC Map is v1.2.0 (D-013). A section merges as a new minor
edition; follow-up changes before approval bump the patch, so the tag is `v` plus
`content/VERSION` at approval (for example v1.3.2). `release/sections.yml`, keyed by
major.minor, names the section and the pages each release covers. An agent creates a `v*` tag
only on the author's explicit instruction; the workflow refuses a tag that is not on `main`. The
tag can be pushed, or created by running the Release workflow by hand on `main` with the tag as
input.
`.github/workflows/release.yml` runs on a pushed `v*` tag, or by hand on `main` with the tag as
input: it re-runs validation, then creates the
release with the section's changelog entries as notes and attaches a PDF snapshot of the section's
pages (`scripts/release_snapshot.py`). v2.0.0 is released when every box on the map links to a
page. Rules out: releases without the author's approval, and a tag that does not match the
edition.

## D-017 · Deny-list: any case, word pairs, and the inventory's identifiers
Decided 2026-09-25 from the source inventory (GR-1.1, GR-1.4, GR-5.3). `scripts/denylist.py` now
lower-cases every word before hashing it, and also hashes each pair of neighbouring words, so a
name is caught whatever its capitalisation and a two-word name is caught as a pair. It holds the
original names plus the single-word and two-word identifiers the inventory found in the source
library: organisation, product, project-code and people names. It uses a new salt. Identifiers that
are ordinary words, or public products whose risk lies only in combination, cannot be listed
without false alarms: the source researcher and the author, who can see the library, check for
them, and the confidentiality reviewer checks for fingerprinting combinations. Rules out: case-sensitive matching, and an identifier found in the
library but left off the list.
*The published salt is replaced by a keyed hash (D-023).*

## D-018 · Core section plan approved, with changes
Decided 2026-09-25 by the author (D-014). `project/plans/core.md` is approved with two changes.
The Engineering Kit overview page also covers technology profiles, project configuration, the
kit's commands (init, doctor, verify) and the `could_not_run` result; there is no tenth page. The
harness engineering page covers guides and sensors, computational and inferential controls and the
steering loop, and the map's "Feedback path" links to it. The kit's five parts are linked on the
map. The boundary table is approved, with cross-links both ways between core pages and the pages
of the other sections that own each use. Rules out: a separate page for kit commands or profiles.

## D-019 · Disconnect from the series site and repository
Decided 2026-09-25 by the author; supersedes the cross-linking with the series set up by D-002,
D-003 and D-010. Those entries were reworded when this decision was applied, so that they no
longer name the series; their decisions otherwise stand. The earlier narrative series, its site and its repository are no longer part of this work.
This repository and site do not link to or name them. Map labels that pointed to series parts
point to the matching glossary entries until the Core pages replace them. A check fails on any
link to, or naming of, the series site or its repository in a tracked file. The review reports
in `content/reviews/` are exempt: they are historical records bound by hash to the release
record (D-011), are never published, and are not rewritten. Rules out: links to, or naming of,
the series anywhere else in this repository or on the site.

## D-020 · Documentation layout
Decided 2026-09-25 by the author. Pages use a three-column documentation layout, built in the
Python generator with plain CSS and JavaScript: a sticky header with section tabs and search; a
sticky left navigation listing the current section's pages; the content; a sticky right "On this
page" list built from the page's headings; breadcrumbs; previous and next links. The home page
keeps the full-width map with a "choose a section" panel. On small screens the left navigation is
a drawer and the right column is hidden. Accessibility: labelled navigation landmarks,
`aria-current`, a skip link, visible focus and reduced motion. The change of layout must not
change any page's text; a test compares every page's main-content text before and after. Rules
out: a framework, and layout changes that alter content.

## D-021 · Brand: Slate & Teal
*Superseded by D-031.* Decided 2026-09-25 by the author (option A). An independent palette, never an employer's design
system. Light tokens: ground `#f6f8f8`, surface `#ffffff`, ink `#15232b`, body text `#34434b`,
muted `#5b6b72`, line `#d8e1e1`, primary teal `#0b6e69` (text on it `#ffffff`), primary tint
`#e2f1ef`, link `#0b6e69`, accent amber `#b7791f`, accent tint `#fbf1df`, accent text `#7a4e0f`.
Dark tokens: ground `#0f1a1d`, surface `#142225`, ink `#e4eeed`, body text `#c3d0cf`, muted
`#8fa3a3`, line `#243639`, primary `#4fc1b9` (text on it `#07201e`), primary tint `#15363a`, link
`#6fd3cb`, accent `#e0a84a`, accent tint `#2e2718`, accent text `#f0c47a`. Teal marks navigation
state, links, primary buttons and "gate"; amber marks judgment, warnings and notes. Fonts:
Atkinson Hyperlegible for text and IBM Plex Mono for code and IDs, bundled with the site. Logo:
five stacked horizontal bars, one per band, in the primary colour, with the wordmark "The AI SDLC
Map". The map's five band colours do not change. Every text pair passes WCAG AA (4.5:1), checked
by a test; the accent colours `#b7791f` and `#e0a84a` are for non-text marks only (3:1), and text
in the accent family uses `#7a4e0f` and `#f0c47a`. The brand changes only `site/`, not `content/`.
Release v1.3.0 is a site release, not a band section: it covers the disconnect (D-019, content
edition 1.3.0), the layout (D-020) and the brand, and `release/sections.yml` gains a `"1.3"`
entry for it. The Core section therefore becomes edition 1.4.0. Rules out: fonts
loaded from a third party at runtime, and any resemblance to an employer's design system.

## D-022 · "Draft" in pages
Decided 2026-09-25 by the author; clarifies GR-3.2. "Draft" fails in a page's title, summary,
headings and link text, where it would label the page; it is allowed in running prose, where
pages describe agents drafting specifications and plans. `scripts/check_pages.py` enforces it.

## D-023 · Keyed deny-list hashes
Decided 2026-09-25 by the author; replaces the published salt of D-012 and D-017. The deny-list
stores HMAC-SHA-256 values keyed by a secret held as the CI secret `DENYLIST_KEY`, so a reader
with a guessed name cannot confirm it. Without the key, a local run warns and skips the check; in
CI a missing key fails the build; pull requests from forks and from automated dependency tools
receive no Actions secrets and so fail the check; a maintainer re-creates such a change on a branch
of this repository, or the author also adds `DENYLIST_KEY` as a Dependabot secret for dependency
pull requests. The
author generates the key and adds it as the secret. Hashes made with the old salt remain in git
history. Rules out: a key in the repository.

## D-024 · Tag protection
Decided 2026-09-25 by the author. A repository ruleset limits creating, updating and deleting
`v*` tags to the author, with a bypass for GitHub Actions so the Release workflow can create a tag
from a manual run (D-016). "The author" is the repository admin role while the author is the only
admin. The author sets the ruleset in the repository settings and confirms that GitHub Actions
is offered as a bypass actor; if it is not, the manual Release path cannot create tags.

## D-025 · Core section answers
Decided 2026-09-25 by the author, on the questions raised while writing the Core section. The
map's "Feedback path proven" label opens the harness engineering page's steering-loop section.
The reference key `fowler-fitness` is renamed `fitness-function`. "Adapter" is adapted from
Cockburn's ports and adapters pattern and cites it. A repeated timeout reports could_not_run,
except for a rule that is itself a time limit, where it fails. Kit versioning: anything that can
turn an unchanged project red is a major change; a new rule whose validator starts report-only is
minor; switching a rule to required is major. Glossary entries for golden path and LLM-as-a-judge
stay only while a Core page uses them, credited to Spotify Engineering and to Zheng et al. (2023).
Archived Technology Radar entries may be cited with their volume, date and access date, labelled
archived. Wording in earlier editions is aligned with the kit's command names and the report-only
term in 1.4.0. Organisations may be named in page prose only as the credited author or originator of
a cited source or term (for example the Thoughtworks Technology Radar, or Spotify Engineering for the
golden path), never as a recommended product (GR-3.3).

## D-026 · Library sweep before review
Decided 2026-09-25 by the author, after the Core section's first drafts followed the source
library's structure too closely although every brief was de-identified. Authors never read the
library; the source researcher passes concepts only; a paraphrase sweep of every draft page runs
before the first review; nothing is pushed before it passes. The full rule is in `AGENTS.md`
(Source library and the paraphrase sweep) and in `section-pipeline`. If a draft has already been
pushed, the branch is deleted, `git ls-remote` confirms no ref holds it, and the author asks the
host to purge the unreferenced commits. Rules out: using replacement text written by anyone who has
read the library.


## D-027 · The library sweep is part of every content change
Decided 2026-10-06 by the author, at the close of wave 0, after the sweep found about 70 close
passages in the Core section's drafts (D-026). The sweep (step 5a of `section-pipeline`) runs for
every content change, a whole section or a follow-up edition, before the first review and before
any push, and covers new or rewritten page passages, glossary entries and diagrams. The review
record states its result in one standalone line, `Library sweep: CLEAN`, or `Library sweep: NOT
NEEDED - <reason>` when no reader-visible text was written or rewritten. From edition 1.4.2
`scripts/release_content.py` refuses to record or accept a report without that line, and
`scripts/tests/test_agents.py` fails if the step drops out of the pipeline, the update prompt,
the site-builder skill, the diagrammer or the source researcher's skill (GR-5.3: a review-only
rule becomes a check). Rules out: a follow-up edition or a diagram reaching review unswept.

## D-028 · Wave 0 retrospective: foundations closed
Decided 2026-10-06 by the author (GR-5.3, APPROACH.md Waves). Each open retrospective item was
acted on, deferred to the section that owns it, or dropped; the list is in `STATUS.md` (Wave 0
retrospective). Acted on in edition 1.4.2: the library sweep as a gate (D-027); the keyed
deny-list switch prepared (D-023); diagrams on five Core pages; the map's intro and caption
wording; the adoption path's closing line restated as recommended practice (GR-2.3). Wave 0 is
closed; open items now belong to the lifecycle, assurance and adoption sections. Rules out:
carrying a wave-0 list forward without an owner.

## D-029 · Lifecycle section plan approved, shipped as two editions
Decided 2026-10-06 by the author (D-014). `project/plans/lifecycle.md` is approved with one change:
the Lifecycle section ships as two editions, each deployed, reviewed live by the author and tagged
separately. **1.5.0** has 12 pages: the generic level labels (the D-015 relabel), `lifecycle-levels`,
`safe-reference-model`, the seven phase pages, `definition-of-ready-and-done`, `traceability-spine`
and `inspect-and-adapt`. **1.6.0** has the seven workflow pages, each of which must add failure
paths, evidence and measures beyond its catalog row. The paraphrase sweeps (D-026, D-027) are batched
per edition, riskiest first, with a final full sweep of each edition. The workflow links on the map
move to their pages in 1.6.0; Core pages gain back-links in 1.5.0 under a D-011 confirmation review;
the SAFe reference model page uses a closed allow-list of what it may name, with forbidden names
described by category only (GR-1.4), and the author reads its text in chat before its first push;
every map box that shares a page has its own anchor; the W12 wording is left alone and listed on
the backlog as a catalog consistency pass. GR-6.1 describes a section as one band with one
approval: this decision is an exception for Lifecycle, and `GROUND-RULES.md` is not edited here.
The author decides whether GR-6.1 should be amended to allow a section in parts (settled 2026-11-20:
GR-6.1 stays as written; this decision holds the exception). Rules out: pushing
any Lifecycle page text before its edition's sweeps pass and, for 1.5.0, before the author has read
the SAFe page.

## D-030 · Lifecycle pages link to catalog rows and Core pages, never restate them
Decided 2026-11-21 by the author, after the library sweep of the Lifecycle 1.5.0 batch A pages
(D-026, D-027) found close passages in two rounds, many where a page restated a workflow catalog row
or a Core page. A Lifecycle page states its own concept and links to the catalog row
(`workflow-catalog.html#Wnn`) or the Core page for anything those already say: a row's decision,
trigger, agent task, checks, people, evidence or traditional counterpart, and a Core page's
definitions. The grain of the batch A pages shrinks with it: list-shaped passages (readiness layers,
reviewer-load items, per-level intake entries, event-walk steps) are cut without replacement wherever
the page template's minimum still holds. A catalog-row diagnostic sweep checks whether the closeness
starts in the published rows; any row found close is logged in `STATUS.md` as a 1.4.x finding for a
separate fix edition, and the live catalog is not changed by the Lifecycle edition. Rules out:
restating a catalog row or a Core passage on a Lifecycle page, and fixing a published row inside a
section edition.

## D-031 · Brand: AI SDLC design system v1.0
Decided 2026-11-27 by the author, who locked the design system v1.0 as one brand for all his AI
SDLC content; supersedes D-021. Type and colour follow the learn-ontology hero the author chose,
with a soft colour per map band. Light tokens: ground `#fafafb`, surface `#ffffff`, ink `#18181b`,
body text `#3f3f46`, muted `#6b6b75`, line `#e4e4e7`, primary `#3b55d9` (text on it `#ffffff`),
primary tint `#eef1fd`, link `#3b55d9`, accent `#b57a1e`, accent tint `#fdf6e9`, accent text
`#7a4e0e`. Dark tokens: ground `#0f0f12`, surface `#17171b`, ink `#f4f4f5`, body text `#d4d4d8`,
muted `#a1a1aa`, line `#2a2a30`, primary `#8b9cf4` (text on it `#0f0f12`), primary tint `#1c2033`,
link `#a3b1f7`, accent `#e0a84a`, accent tint `#2b2416`, accent text `#f0c47a`. Indigo marks
navigation state, links and focus; the design system's accent `#4c66e6` is used for marks (the
Core band, icons, the gradient), and its link shade `#3b55d9` is the primary token because text in
it must reach 4.5:1 on the tints. Primary buttons are black (`#18181b`, white in dark mode) and
secondary buttons are outlined; the kicker is a pill with a green dot (`#059669`). The gradient
`#312e81 → #4c66e6 → #059669` appears on one headline word and the reading-progress line only.
Amber marks judgment, warnings and notes; the design system's Context amber `#d29a3a` is too light
for a 3:1 mark, so the accent token is the deeper `#b57a1e`. Band colours (stroke, fill, text):
Context `#d29a3a` `#fdf6e9` `#7a4e0e`, Lifecycle `#a1a1aa` `#f7f7f8` `#27272a`, Core `#4c66e6`
`#eef1fd` `#2b3a99`, Enablement `#10a374` `#e8f7f1` `#065f46`, Assurance `#0e8fb0` `#e6f5fa`
`#0b4f63`; text in a band colour uses a darker step of the same hue so it reaches 4.5:1. Fonts:
Inter (400, 500, 600) for text and JetBrains Mono for code, IDs and small capitals labels, bundled
with the site; IBM Plex Mono's arrows file stays for ← → ↔. Logo: the same five bars, in ink.
The diagram sources in `content/` keep their palette: `site/generate.py` maps them onto the brand
when it embeds or writes a diagram, so the brand still changes only `site/` (and the PNG renderer).
An interaction layer in `site/assets/app.js` adds line icons, a hover tooltip and band focus on the
map with a band legend, route and section icons, gentle motion that respects reduced motion, and a
"Back to the map" button on topic pages; every page works the same without it. Band icons and
legend colours are keyed to a band's position on the map, not to its name. The design system
itself is kept in the author's notes, outside this repository. Rules out: fonts loaded from a third
party at runtime, colour as the only carrier of meaning, and any resemblance to an employer's
design system.

## D-032 · How the 1.6.0 workflow pages meet the template without restating catalog rows
Decided 2026-11-27 by the session that built edition 1.6.0, under the author's instruction to complete
the map overnight without waiting for his review; recorded for the author to confirm or reverse. The
workflow template's sections (Decision, Trigger, Agent task, Checks, Human decision, Outputs) match the
catalog-row fields that D-030 forbids restating, and four of the seven rows (W01, W08, W25, W28) carry
1.4.x findings. Each workflow page therefore fills every section from public sources in its own
terms, links its row (`workflow-catalog.html#Wnn`) and the Core Workflows page for the row's own
wording and for how an agent is limited, and keeps list-shaped passages (failure paths, overrides,
agent limits) to what a cited source states or to the template minimum. Design conformance is framed
as consistency with recorded architecture decisions, principles and constraints; its first draft,
built around the row's own framing, was discarded after the sweep. Smaller choices: the seven pages
follow map order in the section navigation; the catalog rows do not yet link to their pages (that
changes the live catalog, so it waits for the 1.4.x fix edition or the author); the SAFe reference
model page is not edited; no new diagram. Rules out: a workflow page that copies its row into the
template's sections.

## D-033 · Assurance section plan approved
Decided 2026-11-27 by the author, who approved pull request #27 ("I approve the PR"). The Assurance
plan (`project/plans/assurance.md`) is approved as written, and the recommendation on each of its
eleven open questions is taken as the answer: Assurance is the first wave-2 section, as edition 1.7.0
after Lifecycle 1.6.0; the 1.4.x fix edition runs before 1.7.0 is written; the 11 pages, the map
changes and the back-links as listed; the SOC 2 page names the criterion's content only if the author
pastes its text before batch C, otherwise it names SOC 2 and carries the mechanism on NIST SP 800-53;
no standard named by clause; no legal conclusions in the AI use policy; the metric block inside Concept
pages, no new template; no benchmark values; the running example counted without figures. The
allow-list additions (question 9) are the author's to make in the environment settings and none is
required. Rules out: building Assurance pages ahead of the 1.4.x fix edition without the author saying so.

## D-034 · Rule enforcement is described per rule, with no named routes
Decided 2026-11-28 by the author ("Reframe it (no named routes)"), after the 1.6.2 library sweep found
that the site's three named rule routes, one per rule, matched the source library's own split in list
membership, order and structure (GR-1.2), and that rewording did not change that. The rule registry
no longer classifies rules into named routes and the site no longer uses "route" for rule
enforcement: each entry names how the rule is enforced, by the check or checks that enforce it
(by validator identifier), by the named person who decides, or both, and a rule with neither is
shown as an unenforced gap. Pages that said a rule was "routed to a gate" say it is enforced by a
required check. The glossary entry for the route is removed. Rules out: reintroducing a fixed set of
named enforcement classes for rules without the author.

## D-035 · Remaining map boxes are re-derived from public sources before their pages are written
Decided 2026-11-28 by the author ("Yes, re-derive and relabel"), after the library check of the draft
Enablement and Context-and-Adoption plans found that much of their closeness to the source library
started in published map labels (the band-4 role bullets, the "policy wins" note, the brownfield
note and the adoption stages). The plans for the remaining bands are rebuilt from public sources and
propose relabels of those boxes as open questions; the author approves the relabels with the plans.
Rules out: writing pages that follow a map label the library check has found close.

## D-036 · Enablement, Context and Adoption plans approved
Decided 2026-11-28 by the author ("I approve PR 30"). The plans `project/plans/enablement.md`
(1.8.0) and `project/plans/context-and-adoption.md` (1.9.0 Context, 2.0.0 Adoption) are approved, and
each open question's recommendation is taken as the answer, including the band 1 and band 4 relabels,
"Embedded and connected products" for the firmware/device box, and the full re-derivation of the
adoption path (whose plan addendum still needs the author's approval before any adoption brief).
Order: 1.6.2, then Assurance 1.7.0, Enablement 1.8.0, Context 1.9.0, Adoption 2.0.0.
