# Decision log

Newest last. Each entry: what was decided, why, and what it rules out. Reopen only with the
author.

## D-001 · Independent, public work
The site is the author's independent work. It carries no reference to any employer or its
internal work. Rules out: case studies, internal names, internal numbers (GR-1).

## D-002 · Title, home and licences
"Beyond Faster Coding", hosted at `vishalkhondre.github.io/ai-sdlc`. Prose CC BY 4.0, tooling
MIT. The web edition may diverge from the LinkedIn text.

## D-003 · The one-page map is the site's front door
The five-band AI SDLC map becomes the landing page with every box clickable, following the
Hopsworks documentation overview pattern. The seven-part series stays as the narrative
introduction. Rules out: a blog-style home page.
*The landing-page part is superseded by D-010: the map is the front door of its own site, not
of the series site.*

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
Decided 2026-09-25 by the author; supersedes the landing-page part of D-003.
`vishalkhondre/ai-sdlc` stays as the finished *Beyond Faster Coding* series at
`vishalkhondre.github.io/ai-sdlc/`, maintained only, with cross-links. *AI SDLC on one page* (renamed *The AI SDLC Map* by D-013) is
built in `vishalkhondre/ai-sdlc-map`, served at `vishalkhondre.github.io/ai-sdlc-map/`, with its
own release cycle, review gate and changelog (starting at edition 1.0.0). The map site links to
the series parts and never copies their text; `content/toc.yml` lists the parts with the
references each cites, so the citation gate and the References page stay complete. Reason:
renaming the old repository would break the Pages URL already shared publicly, and the build
needs its own release cycle. Rules out: moving or renaming the series, and duplicating chapter
text across the two sites.

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

## D-018 · Core section plan approved, with changes
Decided 2026-09-25 by the author (D-014). `project/plans/core.md` is approved with two changes.
The Engineering Kit overview page also covers technology profiles, project configuration, the
kit's commands (init, doctor, verify) and the `could_not_run` result; there is no tenth page. The
harness engineering page covers guides and sensors, computational and inferential controls and the
steering loop, and the map's "Feedback path" links to it. The kit's five parts are linked on the
map. The boundary table is approved, with cross-links both ways between core pages and the pages
of the other sections that own each use. Rules out: a separate page for kit commands or profiles.

## D-019 · Disconnect from the series site and repository
Decided 2026-09-25 by the author; supersedes the cross-linking parts of D-010 and D-003.
*Beyond Faster Coding* and the `vishalkhondre/ai-sdlc` repository are no longer part of this
work. This repository and site do not link to or mention them. Map labels that pointed to series
parts point to the matching glossary entries until the Core pages replace them. A check fails on
any link to the series site or the series repository. Rules out: links to, or mention of, the
series anywhere in this repository or on the site.

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
Decided 2026-09-25 by the author (option A). An independent palette, never an employer's design
system. Light tokens: ground `#f6f8f8`, surface `#ffffff`, ink `#15232b`, body text `#34434b`,
muted `#5b6b72`, line `#d8e1e1`, primary teal `#0b6e69` (text on it `#ffffff`), primary tint
`#e2f1ef`, link `#0b6e69`, accent amber `#b7791f`, accent tint `#fbf1df`, accent text `#7a4e0f`.
Dark tokens: ground `#0f1a1d`, surface `#142225`, ink `#e4eeed`, body text `#c3d0cf`, muted
`#8fa3a3`, line `#243639`, primary `#4fc1b9` (text on it `#07201e`), primary tint `#15363a`, link
`#6fd3cb`, accent `#e0a84a`, accent tint `#2e2718`, accent text `#f0c47a`. Teal marks navigation
state, links, primary buttons and "gate"; amber marks judgment, warnings and notes. Fonts:
Atkinson Hyperlegible for text and IBM Plex Mono for code and IDs, bundled with the site. Logo:
five stacked horizontal bars, one per band, in the primary colour, with the wordmark "The AI SDLC
Map". The map's five band colours do not change. Every text pair passes WCAG AA, checked by a
test. Released as v1.3.0; the Core section therefore becomes edition 1.4.0. Rules out: fonts
loaded from a third party at runtime, and any resemblance to an employer's design system.

## D-022 · "Draft" in pages
Decided 2026-09-25 by the author; clarifies GR-3.2. "Draft" fails in a page's title, summary,
headings and link text, where it would label the page; it is allowed in running prose, where
pages describe agents drafting specifications and plans. `scripts/check_pages.py` enforces it.

## D-023 · Keyed deny-list hashes
Decided 2026-09-25 by the author; replaces the published salt of D-012 and D-017. The deny-list
stores HMAC-SHA-256 values keyed by a secret held as the CI secret `DENYLIST_KEY`, so a reader
with a guessed name cannot confirm it. Without the key, a local run warns and skips the check; in
CI a missing key fails the build. Hashes made with the old salt remain in git history. Rules out:
a key in the repository.

## D-024 · Tag protection
Decided 2026-09-25 by the author. A repository ruleset limits creating, updating and deleting
`v*` tags to the author, with a bypass for GitHub Actions so the Release workflow can create a tag
from a manual run (D-016). The author sets the ruleset in the repository settings.

