# Section plan: Context (band 1) and the Adoption path

Proposed by the architect, 2026-11-28. **Awaiting the author's approval (GR-6.1, D-014).** No page
is written before it. Open questions for the author, each with a recommendation, are numbered at the
end.

Wave 3 holds two sections (APPROACH.md, Waves; GR-6.1: a section is one band or the adoption path).
This file plans both so the last two editions fit together; each section is still built, reviewed,
merged, reviewed live and tagged on its own.

- **Section 1, Context:** band 1 ("what kind of work"), **edition 1.9.0**, after Enablement 1.8.0;
  follow-ups 1.9.x. `release/sections.yml` gains `"1.9"`.
- **Section 2, Adoption path:** the footer path and its companion diagram, **edition 2.0.0**. D-016
  says v2.0.0 is released when every box on the map links to a page; this is the edition that links
  the last ones (open question 1). Follow-ups 2.0.x. `release/sections.yml` gains `"2.0"`.
- **Order: Context first.** Adoption pages refer to risk tiers and flows, so they should link settled
  Context pages; and they link into every other band, so they are best written last, when all their
  targets exist.
- **Coverage (`project/COVERAGE.md`).** Context: 16 boxes, 4 covered, 11 thin, 1 none (Data & ML). The
  band relies on public sources more than any other. Adoption: 5 boxes, 4 covered, 1 thin; the opposite
  profile, with the highest closeness risk per page.
- **The sections link, they do not restate (D-030).** Context pages link the catalog rows for the
  workflows a variant changes (W05, W07, W10, W15, W16, W27, W29, W33) and the Lifecycle phase pages.
  Adoption pages link the Core, Lifecycle, Enablement and Assurance pages for everything a stage builds or
  measures, and never restate them.
- **Dependency.** Both sections are written after the fix edition that rewrites the close passages on
  risk tiers (Core `workflows`, glossary `risk-tier`), the software factory (`software-factory`) and the
  feedback path (glossary `feedback-path`), as D-033 did for Assurance (open question 2).

**No fixed enforcement classes (D-034, recorded in the fix edition: rule enforcement is described per
rule, with no fixed set of named enforcement classes).** Neither section gives the site a fixed number
of risk tiers, a fixed set of gates per tier or flow, or fixed approval levels. A risk tier is an
organisation's own classification, framed by public risk-based testing and assurance sources; a graded
public scheme (SLSA levels, the FIPS 199 impact levels) appears only as one example of a category.
Adoption pages state exit conditions without counts or durations unless a public source sets them.

---

# Section 1: Context (band 1), edition 1.9.0

## Boundary

| Topic | Context (this section) | Other section |
|---|---|---|
| Risk tier | what a risk tier is: a classification by likelihood and impact of failure, after ISTQB's risk level; risk informing the selection and priority of assurance activities, as risk-based testing describes; no fixed tier count (D-034) | glossary `risk-tier` and Core `workflows` (published use); Assurance `check-results-and-decisions` (what a result means at a tier) |
| Flows | what each flow changes against the full-feature default | catalog rows; Lifecycle phase and workflow pages |
| Existing code (brownfield, modernisation) | changing code whose behaviour is only partly known (Feathers' characterisation tests and seams); replacing a system step by step (Fowler and colleagues on legacy displacement) | Lifecycle phase pages; Core `rule-registry` |
| Hotfix | the expedited path | catalog W27, W33; Assurance waivers; Lifecycle `incident-feedback` |
| Regulated product types | what changes in delivery for devices and ML models | Assurance `change-controls-and-standards` (domain standards anchor) |
| Data & ML models | ML models as the product being delivered inside this lifecycle (drift as a gate) | Assurance `ai-use-policy` (models used to build software); glossary `ai-sdlc` (the other meaning of "AI SDLC") |
| Platform / shared library | delivering a library or platform that other teams consume | Enablement `platform-team` (the team type, after *Team Topologies*) |

## Pages

All Context-variant pages (What it is · What changes · Gates that move · Risk tier · Workflows
affected), except the risk tier, which is a Concept.

| # | Page id | Type | Map box | Coverage | Scope |
|---|---|---|---|---|---|
| 1 | `risk-tier` | Concept | Risk tier (band note) | covered | A risk tier as an organisation's classification of a change by likelihood and impact of failure (ISTQB risk level); risk-based testing as ISTQB frames it (ISO/IEC/IEEE 29119 named, by no clause, only where a readable source supports it); NIST SSDF's risk-based choice of practices; SLSA levels as an example of a graded scheme of another kind; why the site fixes no tier count or gate set (D-034). |
| 2 | `greenfield` | Context variant | Greenfield | thin | No existing code or constraints to read; the rules and registry start empty, and the page says what that changes, from public sources. |
| 3 | `brownfield` | Context variant | Brownfield | covered | Changing a system whose behaviour is only partly known: characterisation tests that record current behaviour before a change, and seams for getting code under test (Feathers, *Working Effectively with Legacy Code*, from readable material); undocumented behaviour as an input to specification. No coined term for the work before a change. |
| 4 | `modernisation-and-migration` | Context variant | Modernisation / migration | thin | Replacing or moving a system incrementally (strangler fig, legacy displacement patterns); equivalence evidence between old and new. |
| 5 | `web-and-cloud-apps` | Context variant | Web / cloud app | covered | The default product type the site's pages assume; continuous deployment, progressive delivery and rollback as normal. |
| 6 | `embedded-and-connected-products` (if open question 7 is answered as recommended; else `firmware-and-devices`) | Context variant | Firmware / device | thin | Software that ships on hardware: hardware-in-the-loop tests, update integrity and recovery for devices in the field (IETF SUIT, NIST IR 8259, SP 800-193), long-lived fielded versions; why some checks cannot run in an agent's sandbox. |
| 7 | `data-and-ml-models` | Context variant | Data & ML models | none | Delivering a model: data and model versions as artefacts, evaluation as a gate, drift monitoring after release. Public sources only; no library pass (nothing to read). |
| 8 | `platforms-and-shared-libraries` | Context variant | Platform / shared lib | thin | Consumers you do not see: versioning, compatibility, contract tests, deprecation. |
| 9 | `full-feature-flow` | Context variant | Full feature | covered | The default flow every phase page describes; the reference the other flows differ from. |
| 10 | `bug-fix-and-hotfix` | Context variant | Bug fix · Hotfix (two anchors) | thin, thin | A bug fix: reproduce first, a regression test as the independent basis. A hotfix: the same change on the expedited path. |
| 11 | `trivial-and-config-changes` | Context variant | Trivial / config | thin | Configuration held and changed as code, through the same version control and pipeline (Humble and Farley, *Continuous Delivery*; Morris, *Infrastructure as Code*); impact analysis as the public basis for deciding how much a change needs (NIST SP 800-53 CM-4); change management in production as the SRE book describes it. |
| 12 | `spike-and-research` | Context variant | Spike / research | thin | The spike as Extreme Programming describes it (Beck; the public XP rules) and SAFe's enabler spike, credited, each in its own terms; how what a spike learns reaches the backlog, from those sources; links its catalog row. |
| 13 | `refactor-and-tech-debt` | Context variant | Refactor / tech debt | thin | Behaviour-preserving change: the gate is "behaviour unchanged", evidenced by existing tests; debt as a recorded decision. |
| 14 | `dependency-and-cve-fix` | Context variant | Dependency / CVE fix | thin | Updating a dependency, routinely or for a published vulnerability; links W15 and W29 (settles the wave 0 deferral "also to W29"). |
| 15 | `migration-and-rollback` | Context variant | Migration · rollback | thin | A change that moves data or schema under a running system: parallel change, also called expand and contract (Sato, martinfowler.com), and evolutionary database design (Sadalage and Fowler); why reversing a data change differs from redeploying old code (SRE book and workbook on rollback); links its catalog rows. |

**Merged:** bug fix and hotfix share one page (the map's footnote defines a hotfix as the expedited
form of a fix), with an anchor each; 15 pages for 16 boxes. **Two migrations, two pages:**
`modernisation-and-migration` is a project type (a whole system moves), `migration-and-rollback` a
flow (one change moves data); each page says so in its first paragraph.

### Pages that rely on public sources only

Eleven of fifteen pages rest on thin or no coverage; they take the **restricted library pass**
(confirmations and contradictions only) and `data-and-ml-models` takes none. Kinds of source the
external researcher should find:

- **Risk tier:** ISTQB risk level and risk-based testing (already cited by the glossary entry); NIST
  SSDF on choosing practices by risk; NIST FIPS 199 and SP 800-30 (categorisation and risk
  assessment); ISO/IEC/IEEE 29119 named only where a readable source supports the claim; SLSA levels
  as a graded scheme of a different kind.
- **Project types:** martinfowler.com on the strangler fig and patterns of legacy displacement;
  characterisation tests and seams (Feathers, cited only from readable material); DORA capabilities.
- **Product types:** IETF SUIT (RFC 9019, firmware update architecture), NIST IR 8259 (device
  cybersecurity) and SP 800-193 (firmware resiliency); UNECE R156 (software updates) if readable;
  continuous delivery for machine learning (martinfowler.com), "Hidden Technical Debt in Machine
  Learning Systems" (NeurIPS), the ML Test Score paper, model cards (arXiv), NIST AI RMF; Semantic
  Versioning, consumer-driven contracts, the deprecation and dependency chapters of *Software
  Engineering at Google* (free online).
- **Flows:** Google SRE book and workbook (emergency response, canarying, rollback); NIST SP 800-53
  CM-3 and CM-4 (change control, impact analysis); configuration as code (Humble and Farley; Morris);
  Fowler on refactoring and technical debt; Sato on parallel change; Cunningham's technical-debt
  report; XP and SAFe on spikes (credited); NIST SSDF RV.1 to RV.3,
  the CVE Program, FIRST's CVSS and EPSS, CISA's known-exploited list; evolutionary database design
  (martinfowler.com).

ISO, IEC and IEEE standards for devices, medical software and functional safety are not readable
from a session (`assurance.md`, Source access): pages name none by clause and, at most, name a category
("functional-safety standards") with a title the author confirms.

## Library check and batches

As in `assurance.md` (a) to (g). Context's risk is the reverse of Enablement's: the few covered boxes
are the ones a library treats in depth, and on thin boxes a single library passage could become the
only structure. Lists of "gates that move" per flow are the shape most likely to match a library table,
so every gate a page names must come from a public source or a published site page, and pages say
which *kind* of gate moves rather than reproduce a matrix (D-034).

| Batch | Pages | Why | Sweeps |
|---|---|---|---|
| A | `risk-tier`, `brownfield`, `web-and-cloud-apps`, `full-feature-flow` | covered; `risk-tier` borders a close glossary entry and a close Core passage | two independent runs, re-sweep after every rewrite |
| B | `bug-fix-and-hotfix`, `migration-and-rollback`, `dependency-and-cve-fix`, `spike-and-research` | thin, next to catalog rows | one run |
| C | `greenfield`, `modernisation-and-migration`, `refactor-and-tech-debt`, `trivial-and-config-changes` | thin | one run |
| D | `embedded-and-connected-products` (or `firmware-and-devices`), `data-and-ml-models`, `platforms-and-shared-libraries` | thin or none; public-only | one run |
| E | all 15 on final text, map text, diagram, glossary, changed passages elsewhere | cross-page edits | one run, hash-checked |

**Running example (GR-3.4).** The export is a feature of a web application delivered on the full
feature flow, as published pages show; `web-and-cloud-apps`, `full-feature-flow` and `risk-tier` use it.
Other variants use it only where a published page supplies the fact (the later production incident on
`bug-fix-and-hotfix`, the 50k-row load scenario on `risk-tier`); no new fact or figure (open question 10).

## Map and link changes (Context)

- **Chips:** the 15 band-1 chips are linked (`chip()` already calls `linked()`); the label for the
  hotfix chip is "Hotfix *", and both "Bug fix" and "Hotfix *" open `bug-fix-and-hotfix` (the hotfix at
  its anchor). "Spike / research" and "Dependency / CVE fix" move from their catalog rows to their pages,
  which link the rows.
- **Risk tier:** the box has no chip; it is the band note "Together these set the risk tier: …". The
  site-builder splits the note so "risk tier" is its own linked text, as the Lifecycle edition split the
  spine label (open question 5). No new box.
- **Band 1 relabels (open question 6).** The band note's clause after "risk tier" and the brownfield
  note are reworded; the firmware chip is generalised, kept or dropped (open question 7). `MAP_DESC` follows.
- **Column titles** (Project type, Product type, Flow) and the three italic notes stay plain.
- **Routing row:** "Understand" gains `risk-tier`.
- **Back-links**, each under a D-011 confirmation review and a sweep of the changed passage: Lifecycle
  `intake-and-triage`, `spec-readiness`, `design-conformance` (risk tier); `deploy`, `release`, `operate`
  (hotfix, rollback); Assurance `check-results-and-decisions` (tier), `change-controls-and-standards`
  (regulated product types); Enablement `platform-team`. Close-list pages get "Related" only.
- **Glossary:** entries each attributed (GR-2.2) and added with the page that uses it (D-025): risk
  level and risk-based testing (ISTQB glossary); characterisation test and seam (Feathers); strangler
  fig application (Fowler); hardware-in-the-loop testing (common, cited); firmware update manifest
  (IETF SUIT); configuration as code (common, cited);
  model drift (common, cited); hotfix (common); spike (XP, credited); technical debt (Cunningham);
  parallel change (Sato, martinfowler.com); CVE (the CVE Program); Hyrum's law (Wright, via *Software
  Engineering at Google*) only if a page needs it. The existing `risk-tier` entry is used only after the
  fix edition has rewritten it.
- **Diagram:** at most one, on `risk-tier`: the kinds of input a risk assessment reads (likelihood and
  impact, after ISTQB) beside the band's three columns, with no tier count and no gate list drawn
  (D-034); text alternative, both themes (GR-4.4), swept with the page.

---

# Section 2: Adoption path, edition 2.0.0

## Scope

The footer's "ADOPTION PATH" label and stage boxes, the home page's adoption section and the companion
diagram (`ai-sdlc-adoption-path.svg`, built from `STAGES` and `page_path()` in `build_map.py`), which
the section now owns.

## Re-derivation before pages (open question 8)

The library check (D-026) found the published stages close to the private library in their names,
their order, what each stage holds, the end point and the diagram's closing line. Rewriting the
contents under the same names would keep that structure. The section therefore re-derives the path from
public sources before any stage page is planned:

1. **Public outline pass on adoption itself.** `external-researcher` reads what public models say about
   sequencing, measuring and moving on: Forsgren, Humble and Kim, *Accelerate*, which argues for
   capability models over maturity models; DORA's capability catalogue and its guidance on continuous
   improvement (dora.dev); DORA's research on AI-assisted development, including any AI capabilities
   model it publishes; graded public models as examples of the category only, such as OWASP SAMM
   (maturity per practice), SLSA levels and the NIST AI RMF functions (which it does not order); and
   diffusion-of-innovation literature only where a readable source supports the claim. It returns what
   each source says, with nothing taken from the published stages.
2. **Plan addendum.** The architect proposes the hub's framing, whether the path is a sequence at all,
   the number and names of any stages (none fixed in advance), the footer labels and the diagram's
   structure, each traced to a source or labelled recommended practice (GR-2.3). The author approves
   the addendum before any adoption brief (GR-6.1, ASSUMPTIONS A2).
3. **Rebuild in this edition.** `STAGES`, `page_path()`, `PATH_DESC`, the footer `steps` and the
   adoption sentence of `MAP_DESC` are rebuilt from the addendum. The current closing line, the stage
   contents and the counts in its exit conditions ("20+ real changes", "the last three incidents",
   which no public source sets) are not carried over.

| # | Page id | Type | Map box | Coverage | Scope |
|---|---|---|---|---|---|
| 1 | `adoption-path` | Concept | "ADOPTION PATH" footer label | not a box in COVERAGE | The hub: adoption as improving capabilities against a baseline rather than climbing a fixed ladder (*Accelerate*, DORA); how a team picks its next improvement and checks it worked; what each stage page covers; embeds the rebuilt diagram. |
| 2 onward | one page per stage in the addendum, ids fixed there | Adoption stage | each footer box after the relabel | today four covered, one thin; re-rated against the new labels | Each page's "What to build" links the page that defines each item, "How to measure" links the Assurance metric pages (no definition restated, no benchmark), and "Exit criteria" states a condition without a count unless a source gives one (D-034). |

## Library check (Adoption)

1. **No diagnostic sweep of the diagram,** since it is rebuilt. The home page's adoption section text is
   swept before briefs (locations and verdicts only, GR-1.2, GR-1.3) and rewritten by a fresh author if
   close.
2. **Skeleton from the addendum, public sources and site pages** (what each Core, Lifecycle, Enablement
   and Assurance page says a team needs), never from the current `STAGES` lists.
3. **Batches:** A, every stage page (two independent runs each); B, `adoption-path` with the rebuilt
   diagram text (one run; any stage that touches the software factory borders the close
   `software-factory` passages); C, all pages with the diagram and changed passages (one run,
   hash-checked).

Kinds of public source beyond the outline pass: DORA capability pages (continuous integration,
trunk-based development, working in small batches); martinfowler.com on harness engineering and
incremental change; NIST SSDF; SAFe's public implementation material only for a credited contrast,
never as the structure.

## Map and link changes (Adoption)

- **Footer stages:** relabelled per the addendum and each linked to its stage page. "3  Feedback path
  proven" opens the harness engineering steering loop by D-025; the relabel ends that link (open
  question 9).
- **"ADOPTION PATH" footer label** becomes a linked label to `adoption-path` (it is plain text today).
- **Home page:** the adoption section embeds the rebuilt diagram and gains a link to the hub; the
  routing row's "Lead adoption" points to `adoption-path` instead of `#adoption`.
- **Back-links:** Core `workflows`, `software-factory`, `harness-engineering`; Lifecycle
  `pull-request-verification`, `spec-readiness`, `incident-feedback`, `inspect-and-adapt`; Assurance
  `measurement`; Enablement `automation-bias-and-deskilling`. Every page that links
  `index.html#adoption` today switches to the hub or the matching stage page. D-011 confirmation review.
- **Glossary:** adoption stage (*coined*), and any stage term the addendum keeps, marked coined or
  credited. `feedback-path` used only after the fix edition.
- **One rebuilt diagram, no new one;** the hub embeds it.
- **Completion check:** with this edition every `links.yml`-eligible map label has a target, and the
  site-builder adds a test that fails if any map label is unlinked (D-016, APPROACH "Definition of done").

---

## Order of work (both sections)

0. Plan approved; plan pull request (this file; no page text).
1. Context: briefs, outline pass, concept diffs (restricted for thin boxes, none for Data & ML), evidence
   briefs; batches A to D; diagram; map and links; sweep E; one commit on `main`; review in three groups
   (risk tier and project types, 1 to 4; product types, 5 to 8; flows, 9 to 15); merge as 1.9.0; live
   review; tag.
2. Adoption: public outline pass on adoption models; plan addendum approved by the author; diagram and
   footer rebuilt; sweep of the home section; briefs; outline pass per page; batches A to C; map, home
   page and links; completion test; review in one group; merge as 2.0.0; live review; tag `v2.0.0` at
   approval.

The adoption outline pass and addendum may run while Context is in review; adoption pages are written
only once the addendum is approved and the Context pages they link have merged.

## Cost and size

Context: about 80 to 95 agent runs (15 short pages; fewer rewrites expected on public-only pages, more
sweep runs on batch A); about 60 to 80 new references. Adoption: about 40 to 55 runs including the
re-derivation outline pass, the addendum and the diagram rebuild; the page count depends on the
addendum; about 20 to 30 new references.

## Risks

- **Closeness on adoption stages** (GR-1.2). The published stages are close in names, order and
  contents. Re-derivation from public sources before any page, a rebuilt diagram, skeletons never taken
  from the current lists, double sweeps.
- **No public source orders the path** (GR-2.3). *Accelerate* argues against fixed maturity levels; if
  the outline pass finds no source for a sequence, the addendum may propose capabilities without a fixed
  order, and the footer changes accordingly.
- **A gate matrix by flow** (GR-1.2, D-034). A table of which gates each flow adds or drops would match
  a library table and fix enforcement classes. Pages describe kinds of movement with public sources.
- **Thin pages** (GR-4.1, GR-2.3). Eleven thin Context boxes must still be complete; short pages on
  public sources, recommended-practice labels where no evidence exists. Fallback in open question 3.
- **Regulated domains without readable standards.** Device and medical standards are not readable;
  pages describe the delivery change and name no clause.
- **Legal and safety claims.** No safety or regulatory conclusion on device or ML pages; they point to
  the organisation's domain obligations as Assurance does.
- **"AI SDLC" ambiguity** (D-013). `data-and-ml-models` must not read as the lifecycle for building AI
  systems; its first paragraph says it covers ML models as a product type inside this lifecycle.
- **Restating Core** (D-030). Risk tier and any stage touching the software factory border close
  passages; written after the fix edition, linking only.
- **Fingerprinting** (GR-1.1, D-017). A combination of product types, flows and stage history could read
  as one organisation's portfolio; firmware beside web and cloud is the sharpest case (open question
  7). The confidentiality reviewer checks combinations across both sections.

## Open questions for the author

1. **Editions.** Context as 1.9.0, then Adoption as 2.0.0, the edition that links the last map boxes
   (D-016)? **Recommendation: yes.** If any box is left without a page, Adoption is 1.10.0 and 2.0.0
   waits for that box.
2. **Fix edition first.** Write both sections only after the fix edition rewrites the close risk-tier,
   software-factory and feedback-path passages? **Recommendation: yes,** as D-033 decided for Assurance.
3. **Context pages.** 15 pages, one per box except bug fix with hotfix? **Recommendation: yes.**
   Fallback, 11 pages: the five maintenance flows (trivial/config, spike, refactor, dependency/CVE,
   migration and rollback) on one page `maintenance-flows` with an anchor each, at the cost of a
   Context-variant template repeated per flow inside one page.
4. **One edition for Context?** **Recommendation: yes;** the pages are short and the template small.
   Alternative: a D-029-style split (project and product types with the risk tier, then flows).
5. **Risk tier on the map.** Split the band note so "risk tier" becomes a linked label, with no new box?
   **Recommendation: yes.**
6. **Band 1 relabels (GR-1.2).** Two published notes carry wording the library check found close.
   Relabel the band note "Together these set the risk tier: which gates run, how deep, who approves" to
   "Together these inform each change's risk tier", and the brownfield note "brownfield starts with
   pre-flight analysis" to "existing behaviour is pinned by tests before it changes" (after Feathers'
   characterisation tests); `MAP_DESC` to match. **Recommendation: yes;** the pages then follow public
   sources rather than the labels. If declined, the pages still do not adopt the labels' wording.
7. **Firmware / device (GR-1.1).** Firmware and devices beside web and cloud could fingerprint one
   organisation's portfolio. Keep, generalise or drop? **Recommendation: generalise** the chip to
   "Embedded and connected products" and the page to `embedded-and-connected-products`: the public
   sources (IETF SUIT, NIST IR 8259, SP 800-193) are written for connected devices broadly, the reader
   value (checks that cannot run in a sandbox, updates to fielded units) is kept, and the band's
   "(HIL, OTA, drift)" note still applies. Dropping would remove a map box and leave that reader without
   a page; keeping the current label keeps the risk.
8. **Adoption re-derivation.** How is the adoption section re-derived? Options: (a) re-derive from
   public sources as set out above: an outline pass on *Accelerate*, DORA's capability and AI research
   and graded public models, then a plan addendum fixing the hub's framing, whether the path is a
   sequence, the number and names of stages, new footer labels and a rebuilt companion diagram, with
   the current closing line, stage contents and counts dropped; (b) keep the five stage names and
   rebuild only their contents from public sources; (c) drop the stages and keep one hub page with the
   rebuilt diagram. **Recommendation: (a);** the names, order and end point are part of what was found
   close, so (b) keeps the closeness, and (c) loses the stage-by-stage guidance readers come for. Under
   (a), v2.0.0 still requires every footer box to link a page (open question 1).
9. **Stage 3 map link (D-025).** If the relabel removes "3  Feedback path proven", D-025's link from
   that label to the steering loop lapses. **Recommendation:** every footer box links its stage page,
   and the stage that covers incident feedback links the steering loop in its first paragraph; this
   amends D-025 and needs the author's word.
10. **Running example.** Context and Adoption use only published facts about the export, with no new
    fact or figure? **Recommendation: yes.**
11. **Hub page `adoption-path`** and a link on the "ADOPTION PATH" label? **Recommendation: yes.**
    Fallback: no hub; the label stays plain and the home section remains the overview.
12. **D-034.** D-034 is recorded in the fix edition (rule enforcement described per rule, no fixed set
    of named enforcement classes). The plan applies it as "no fixed tier count, gate set per tier or
    flow, or approval levels". **Recommendation: confirm.**
13. **Allow-list.** Add the IETF RFC host, `unece.org`, `papers.nips.cc`, the free online *Software
    Engineering at Google* host and the OWASP SAMM site, if not already reachable? **Recommendation: add
    them;** none is required for completeness.
