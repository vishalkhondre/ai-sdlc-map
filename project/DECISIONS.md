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
