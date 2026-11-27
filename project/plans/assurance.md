# Section plan: Assurance (band 5)

Proposed by the architect, 2026-11-27, for the author's approval. Nothing in this plan starts before
the author approves it (GR-6.1, D-014). Open questions for the author are numbered at the end.

- **Section:** assurance, band 5 of the map ("what must be provable"), the first section of wave 2
  ("Assurance and enablement"). Enablement (band 4) follows as the second section of the wave; the
  reasons for this order are below.
- **Edition:** 1.7.0 when the section merges, assuming Lifecycle part two ships first as 1.6.0
  (D-029); follow-ups before approval are 1.7.x; the tag is created at approval (D-016).
  `release/sections.yml` gains a `"1.7"` entry naming the section and its pages. If the author puts
  Assurance ahead of 1.6.0 (open question 1), the numbers swap and nothing else in this plan
  changes. **One edition, one approval:** at 11 pages the section is the size of Lifecycle part one,
  so it needs no exception to GR-6.1 of the kind D-029 made.
- **Sources:** `project/COVERAGE.md` rates 9 of the 16 band-5 boxes as covered by the source library
  and 7 as thin; none is rated none. Every page cites public sources for its claims (GR-2). The
  library informs practice only (GR-1.2), and the plan builds each page's structure from public
  sources and from the site's own published pages first, so that the library never supplies it (see
  "Library check built in from the start"). Borrowed terms keep their credit: DORA's software delivery
  metrics (DORA), flow metrics (SAFe's published wording, with the Flow Framework credited to its
  author where SAFe credits it), the Trust Services Criteria (AICPA), least privilege and the control
  identifiers (NIST SP 800-53), the AI RMF functions (NIST); terms this site coins are marked
  *coined* (GR-2.2).
- **Page count:** 11 pages for 16 boxes. Lifecycle part one had 12, Core 9.
- **The section links, it does not restate (D-030).** Band 5 sits on top of Core's evidence schema,
  validators and rule registry, and on Lifecycle's traceability spine. An Assurance page states what
  the evidence *means* for a decision, an audit or a measure, and links to the Core page, the
  Lifecycle page or the catalog row (`workflow-catalog.html#Wnn`) for anything those already say.
  This is the main defence against close paraphrase in this band, because the D-030 diagnostic found
  closeness in published Core passages and catalog rows that an Assurance page would otherwise be
  tempted to rephrase.

## Which band first: Assurance, then Enablement

APPROACH.md lists wave 2 as "enablement (band 4); assurance (band 5)" without fixing an order. The
recommendation is **Assurance first**, for six reasons.

1. **Work already assigned to it.** The wave 0 retrospective (D-028, STATUS) deferred three items to
   this section and none to Enablement: the SOC 2 change-management wording, confirmed so far only
   through secondary sources ("deferred to the assurance section, which owns that standard"); the DORA
   metrics guide as the specific link for delivery metrics; and the glossary entries for flow metrics
   (shared with Lifecycle). Leaving them open for a further section keeps three owned items without a
   date.
2. **Published pages point at it today.** Core `validators` says twice, in running text, that the
   assurance band decides what a result means for a merge or release decision, and links nowhere,
   because no page exists. The Core plan's boundary table gives three of its six rows to assurance
   (rule IDs traced to decisions, what each result means, the record's validity and audit use) and
   two to Enablement (adapters' tools; skills' review load, which Assurance also measures). The
   Lifecycle plan's boundary table gives assurance four rows (records for audit and validity per
   revision, measures, templates, change controls) and Enablement four (cadence, roles, tools, SDD
   frameworks). The difference is that the Lifecycle 1.6.0 workflow pages must each name **measures
   with a baseline** (D-029 acceptance criterion): with Assurance published, all seven gain a link to
   a metric definition instead of carrying their own.
3. **Coverage and closeness risk.** Assurance has 9 covered and 7 thin boxes; Enablement has 13
   covered and 8 thin. The covered Enablement boxes are the people and operating-model boxes (role
   splits, decision rights, the ART operating model, work tracking): the shapes most likely to carry
   one organisation's structure, and a fingerprinting risk under GR-1.1 and D-017 as well as a
   paraphrase risk under GR-1.2. Assurance's covered boxes are mostly measurement, where strong public
   definitions exist to build the skeleton from (DORA, SAFe's flow metrics, the ISTQB glossary).
4. **Public-source availability.** Assurance rests on sources a session has already read or can
   read: DORA (`dora.dev`), NIST SP 800-53 and SP 800-218 (`csrc.nist.gov`), the NIST AI RMF and its
   generative AI profile (`nvlpubs.nist.gov`), SARIF (`docs.oasis-open.org`), SLSA (`slsa.dev`), the
   ISTQB glossary and SAFe's measurement pages. Enablement's tool boxes (coding agents, model
   providers, sandboxes, MCP, SDD frameworks) rest largely on official tool documentation, the lowest
   tier of GR-2.1, usable for facts about that tool only and constrained by GR-3.3 on every page; its
   people boxes have little public research behind them.
5. **Enablement benefits from Assurance, more than the reverse.** Enablement's "Permissions",
   "Secrets", "Watch: review load" and "Decision rights and approvals; policy wins" each meet an
   Assurance page (agent permissions as privileged access, reviewer load, change controls). Written
   second, those Enablement pages link to settled definitions; written first, they would have to
   define the control side themselves and the Assurance pages would later restate or contradict them.
6. **It keeps the map's vocabulary change in one place.** Enablement carries the band 4 SAFe words
   that D-029 left on the map (Agile Release Train, PI cadence, system demo). Doing it second lets the
   Enablement plan settle that relabel together with Lifecycle 1.6.0 lessons, without blocking
   Assurance, which has no SAFe-only labels.

**The case for Enablement first, and why it does not win.** Enablement is the band readers adopting
agents ask about first (tools and roles), and its covered boxes outnumber Assurance's. But its pages
would carry the higher confidentiality risk while the band 5 deferrals stay open, and it would publish
permission and review-load pages without the control and measure definitions they lean on. The
harder source constraints sit in Assurance (SOC 2 and ISO text, see below); they shape a smaller part
of it (two of eleven pages) and the plan handles them by saying less, not by waiting.

## Boundary with the other sections

Assurance says what the evidence proves, to whom, for how long, and how the system is measured. It
does not redefine what Core defines or what Lifecycle places, and it leaves the tools and people to
Enablement.

| Topic | Assurance (this section) | Other section |
|---|---|---|
| Evidence record | the record as its readers use it: release, incident review and audit reading one record; integrity and retention; reading a decision back from rule to check to decision; validity for one revision and expiry on a new push | Core `evidence-schema`: the fields, who writes each, schema versioning. Lifecycle `traceability-spine`: the chain of artefacts and its identifiers |
| Rule IDs | how an auditor or reviewer follows a rule ID from the registry to the checks that enforce it and the decisions that relied on them | Core `rule-registry`: what an entry holds, routes, owners, lifecycle of a rule. Lifecycle `traceability-spine`: rule IDs as link keys |
| Check results | what passed, failed, skipped and could_not_run mean for a merge or release decision, by risk tier; when a result may be waived and how the waiver is recorded | Core `validators` and `adapters`: how a result is produced and reported, timeouts, flaky checks. Catalog W33 (exception handling) stays the row |
| Templates | what the spec, plan, ADR and release-notes templates must hold so a record can be checked, and why the template is fixed | Lifecycle phase pages: which phase produces which artefact. Core glossary: ADR. Enablement: SDD frameworks that generate them |
| Change controls | how an external control framework's change-management criteria are met by rules, checks and records; which approvals stay with people | Catalog W32 (change control) and W25 (release readiness); Lifecycle `release`. Enablement: decision rights and approvals (who holds authority) |
| Domain standards | how a domain standard enters the rule registry and the evidence record, in general terms | Context (band 1): what changes for regulated product types (firmware, device, data and ML) and the risk tier |
| AI use policy | the policy an organisation sets for data sent to models and for generated code, and the evidence that it is followed | Enablement: model providers and the agent runtime as tools |
| Agent permissions | reviewing an agent's permissions as privileged access: grant, review, revoke, evidence | Enablement: how the runtime grants permissions, sandboxes and secrets mechanically |
| Measurement | metric definitions (each with formula, unit and the source of the definition), baselines, how measures derive from evidence records | Lifecycle workflow pages (1.6.0): which measure each workflow names. Adoption path: which measures each stage watches |
| Review load | review load and reviewer concentration as measures | Enablement (people): review load as a strain on the role, and skill erosion |
| Cost | cost per change, including tokens and evaluation runs, as a measure | Enablement: model providers' pricing models (category level only, GR-3.3) |

## Pages

| # | Page id | Type | Map box | Coverage | Scope | Leaves to others |
|---|---|---|---|---|---|---|
| 1 | `evidence-record` | Concept | Evidence record on every run, fixed schema · Rule IDs link rule → check → decision (anchor) · Valid for one revision; a new push expires it (anchor) | Evidence record covered; Rule IDs, Validity thin | The record as assurance reads it: one record per run; the three readers (release decision, incident review, audit) reading the same record; following a rule ID from registry to check to decision; validity for one revision and expiry on push; integrity, retention and who may correct a record. Links to `evidence-schema` for every field. | Fields and schema (Core); the artefact chain (Lifecycle `traceability-spine`) |
| 2 | `check-results-and-decisions` | Concept | passed · failed · skipped · could_not_run | thin | What each status means for a merge or release decision; which statuses block, by risk tier; why skipped and could_not_run never count as passed; waivers and exceptions, who may grant them and what the record shows; the decision Core `validators` defers to this band. | How a validator reports (Core `validators`, `adapters`); exception workflow (catalog W33) |
| 3 | `delivery-templates` | Concept | Templates: spec, plan, ADR, release notes | covered | What a template is for in an AI SDLC (a fixed shape a machine can check and an agent can fill); the minimum each of the four must hold, from public formats (ADR after Nygard, release notes after Keep a Changelog and Semantic Versioning); how templates version with the kit. | Which phase writes which artefact (Lifecycle); SDD frameworks (Enablement) |
| 4 | `change-controls-and-standards` | Concept | SOC 2 change controls · domain standards as they apply (two anchors) | thin, thin | How an external control framework is met through the kit: control → rule → check → record → reviewer; segregation of duties when an agent writes the change; which approvals stay with people; SOC 2 named as the framework the map shows, with criterion content only as far as the source-access rule allows; domain standards in general terms. See "Source access". | Change control and release readiness rows (catalog W32, W25); regulated product contexts (band 1) |
| 5 | `ai-use-policy` | Concept | AI use policy: data sent to models, IP of generated code | thin | What an AI use policy covers for delivery: which data may be sent to which model, retention and training terms as policy questions, provenance and licence checks on generated code, disclosure; how the policy becomes rules in the registry and evidence in the record; risk framing from the NIST AI RMF and its generative AI profile. States no legal conclusion (open question 7). | Model providers and runtime (Enablement) |
| 6 | `agent-permissions` | Role or practice | Agent permissions reviewed as privileged access | covered | The practice of treating each agent identity as a privileged account: least privilege, grant with an owner, periodic review, revocation, and the evidence each step leaves; what shifts when the account is an agent; warning signs (standing broad tokens, shared identities, no review date). Built on NIST SP 800-53 AC-2 and AC-6. | Mechanism of permissions, sandboxes, secrets (Enablement) |
| 7 | `measurement` | Concept | Measurement (column) · Baseline before changing anything (anchor) | covered | Why measure an AI SDLC, and what not to measure (individuals, output volume); the baseline before any change; a small balanced set (speed, stability, quality, human load, cost) linking to pages 8 to 11; deriving measures from evidence records rather than surveys where possible; how a measure misleads when it becomes a target. The hub of the column. | Each family's definitions (pages 8 to 11); stage measures (adoption) |
| 8 | `delivery-metrics` | Concept | Flow metrics and DORA delivery metrics (two anchors) | covered, covered | DORA's software delivery metrics, linked to the DORA guide (the deferred retrospective item), each with definition, unit and what it does not say; flow metrics in SAFe's published wording; how the two families differ (delivery pipeline against the whole value stream); computing them from the evidence record and the change host. No benchmark values (see "Evidence rules for this band"). | Release and deploy practice (Lifecycle) |
| 9 | `escaped-defects` | Concept | Escaped defects | covered | A defect found after the gate meant to catch it; the escape rate per gate, after the ISTQB defect detection percentage; how an escape is traced back through the evidence record to the check that should have caught it, and feeds the incident feedback path. | The incident feedback workflow (Lifecycle, catalog W28) |
| 10 | `reviewer-load` | Concept | Reviewer load and concentration | covered | Review load (time and queue per change, decisions per reviewer) and concentration (share of reviews on the fewest people) as measures; why agent output raises both; what a rising trend signals and what moves work into gates. | Review load as strain on the role, skill erosion (Enablement) |
| 11 | `cost-per-change` | Concept | Cost per change, including tokens and evals | covered | Cost per change as a measure: what goes in (compute, model usage, evaluation reruns, review time), what is attributed per change, why it is read against stability and quality, never alone. Weak public evidence: largely recommended practice (GR-2.3). | Pricing models (Enablement, category level only); evaluation reruns (catalog W35) |

**Anchors.** Every map box that shares a page has its own anchor, as Lifecycle does (D-029): the rule
IDs and validity anchors on `evidence-record`, the SOC 2 and domain-standards anchors on
`change-controls-and-standards`, the baseline anchor on `measurement`, the flow and DORA anchors on
`delivery-metrics`. Each anchor is a heading with a stable slug, covered by the link check (GR-4.3).

**Metric pages and completeness (GR-2.1, GR-4.1).** No metric template exists among the six in
`templates/pages/`. Each metric that pages 8 to 11 define carries the same block inside "How it
works": definition; formula with unit; where the data comes from (which field of the evidence record
or which event of the change host); the source of the definition; how it misleads. The editorial
reviewer checks every block and returns REVISE for a metric without a formula and unit or without the
source of its definition (open question 8 asks whether to make this a template instead).

### What was merged, what was kept apart, and why

- **Evidence & traceability: two pages for four boxes.** The evidence record, rule IDs and validity per
  revision are one object read three ways, and two of the three are thin; Core `evidence-schema` and
  `rule-registry` already define the record and the IDs, so separate pages would mostly restate them
  (D-030). The result states keep their own page: Core `validators` explicitly defers their meaning to
  this band twice, a reader arrives with exactly that question, and the page holds a decision rule set
  (status by tier) the record page does not.
- **SOC 2 and domain standards: one page.** The map draws them on one line; both are the same
  mechanism (an external control mapped to rules, checks and records); both are thin; and both meet the
  same source-access limit, so confining them to one page confines that handling to one file.
- **Flow and DORA metrics: one page.** One bullet on the map; readers most often need the difference
  between the two families, which only a shared page can show without cross-page repetition.
- **Escaped defects and reviewer load: two pages.** The map puts them on one bullet, but one is a
  quality outcome traced through gates and the other a human-capacity measure that Enablement's people
  pages will link to. The bullet is split on the map (see "Map and link changes").
- **No page for the column titles except Measurement.** "Evidence & traceability" and "Standards & AI
  governance" are headings over unrelated boxes; a hub page for each would have no content of its own.
  "Measurement" gets a hub because the baseline box needs a home and the five metric families need a
  common frame (what to measure, what not to). The two other titles stay plain labels.
- **Agent permissions as Role or practice.** An access review is a recurring practice with an owner,
  responsibilities and warning signs; Concept would force a "How it works" that is really a cadence.

### Page type fit

All pages fit an existing template. Two fits are imperfect and need no new template: the metric
pages use Concept with the metric block above; `change-controls-and-standards` uses Concept with one
sub-heading per map box inside "How it works", so the two anchors exist.

### Pages that rely on public sources only

| Page | Why | How it is shaped |
|---|---|---|
| `check-results-and-decisions` | thin | Built from Core `validators` and `evidence-schema` (linked, not restated), SARIF's result kinds (OASIS), NIST SP 800-53 AU-5 (response to audit logging process failures), and SLSA's verification of provenance. The per-tier blocking rule is labelled recommended practice (GR-2.3). |
| `evidence-record` (rule ID and validity parts) | thin | Built from SLSA provenance and verification (evidence bound to a digest), SARIF's revision fields, NIST SP 800-53 AU-9 and AU-11 (protection and retention of audit information) and NIST SSDF PS.3 (archive and provenance). |
| `change-controls-and-standards` | thin, and the source-access limit | Built from NIST SP 800-53 CM-3 (configuration change control), CM-5 (access restrictions for change) and AC-5 (separation of duties) as the readable worked control catalogue; SOC 2 per "Source access" below. |
| `ai-use-policy` | thin | Built from the NIST AI RMF 1.0 and NIST AI 600-1 (generative AI profile), NIST SSDF on third-party components and provenance, and OWASP material on sensitive information disclosure where readable. Jurisdiction-specific law only if read (see "Source access"). |
| `cost-per-change`, `reviewer-load` | covered, but weak public evidence | Treated as public-only in structure: the library would otherwise become the only non-public structure on the page. DORA's AI research, published code-review research (Microsoft Research and arXiv hosts are reachable) and the truck-factor literature; anything else is recommended practice. The library pass is restricted (confirmations only). |

## Source access (KICKOFF part b) and how this plan handles it

Assurance is the band most affected by sources a session cannot read. The rule stands: a source a
session cannot read is a gap in evidence, never a page claim by memory or search (KICKOFF (b)).

| Source | Status | Handling in this plan |
|---|---|---|
| AICPA Trust Services Criteria (SOC 2), including the change-management criterion | The reference `aicpa-soc2` points at a download a session cannot read; the CC8.1 wording was confirmed only through secondary sources (wave 0 retrospective) | **Author to confirm.** Before batch C is written, the author opens the criteria document in a browser and pastes the change-management criterion and its points of focus into chat (open question 5). With that text, the page cites the criterion by number and says what it says, nothing more. Without it, the page names SOC 2 and the Trust Services Criteria as the framework the map shows, makes no statement of their content, and carries the mechanism on NIST SP 800-53, which a session has read. Either way the page is complete (GR-4.1). |
| ISO/IEC/IEEE standards: ISO/IEC 27001, ISO/IEC 42001, safety and medical domain standards | `iso.org` refuses plain requests; IEC and IEEE text is behind paywalls | **Off the site as claims.** A page names a standard only where the claim stands on a source that was read. The domain-standards anchor describes the mechanism (a standard's requirements entering the rule registry with an owner, and its evidence entering the record) without naming clauses; any named standard is an example of a category, with a title the author confirms in a browser (open question 6). |
| EU AI Act (EUR-Lex), national copyright guidance | not on the environment's allow-list | `ai-use-policy` makes no legal statement. If the author adds the hosts and they answer a plain request, a later edition may cite them; until then the page frames IP and data questions as policy questions an organisation answers with counsel, sourced to NIST (open questions 7 and 9). |
| SAFe flow metrics | readable glossary and article pages; deeper material behind the login wall | Follow the SAFe glossary wording; where it is silent, the page says less. |
| Flow Framework book, SPACE paper (ACM) | book text unreadable; `dl.acm.org` refuses plain requests | The book is cited only for what its table of contents shows. SPACE is cited only from a host a session can read (a copy on the authors' institution's site); otherwise its claims are marked author to confirm and stay off the page. |
| OWASP generative AI project pages | `genai.owasp.org` not on the allow-list | Use `cheatsheetseries.owasp.org` where it covers the claim; otherwise an allow-list request (open question 9). |

Every claim that falls under "author to confirm" goes into the evidence brief and the "For the
author" list in `STATUS.md`, as KICKOFF (b) requires, and stays off the page until confirmed.

## Evidence rules for this band

- **No benchmark values.** DORA publishes performance clusters that change each year; quoting them
  would date the page and invite misuse. Pages define metrics and link to the DORA guide and report;
  any figure that does appear carries its source, year and population, and the accuracy reviewer
  checks all three (GR-2.3, GR-2.4).
- **No invented thresholds.** The per-tier blocking rule, review-load warning levels and cost
  attribution are recommended practice where no source sets them, labelled as such (GR-2.3).
- **Vendor-neutral.** No product, cloud service, model provider or tool is named in the body of any
  Assurance page (GR-3.3). Organisations are named only as the credited originator of a cited source
  or term (D-025): DORA, NIST, AICPA, OWASP, OASIS, SAFe, ISTQB.
- **Measure the system, not people.** Metric pages say that reviewer load and cost are read per team
  or workflow, never as an individual performance score; this is a page claim and needs a source
  (DORA guidance on metric use) or the recommended-practice label.

## Library check built in from the start

D-026 and D-027 hold throughout: authors never read the library or notes by anyone who did; the
source researcher passes concepts only; the sweep runs before the first review; nothing is pushed
before it passes; the pushed branch is one commit on top of `main` with a neutral message. D-030
holds too: a page links to a catalog row or a Core or Lifecycle passage and never restates it. The
plan follows the order of work that Lifecycle used and the 1.5.0 lessons (process only, never
passages).

### (a) Public skeleton first

1. The architect writes each brief from the map, the catalog, the glossary and the published Core and
   Lifecycle pages only. The architect does not read the library; `COVERAGE.md` is the only
   library-derived input. A brief never contains library material.
2. An **outline pass** by `external-researcher` runs before any library pass. For each page it returns
   the public skeleton: the content points per heading, each list with its items, any sequence, and
   the examples, each tied to a public source read under the KICKOFF rules (DORA, NIST SP 800-53,
   SP 800-218, AI RMF and AI 600-1, SARIF, SLSA, ISTQB, SAFe, Nygard, Keep a Changelog, Semantic
   Versioning) or to a page of this site. A list, order or example with no public source and no site
   page behind it is not in the skeleton. For metric pages the skeleton holds each metric's
   definition, formula, unit and source before anything else.
3. The `source-researcher` then reads the library **with the skeleton in hand** and returns a diff
   keyed to skeleton item numbers: confirmed general practice, contradicted or not general practice,
   and unordered single concepts the skeleton lacks (three to six words each, no wording). Each added
   concept must get a public source from `external-researcher` or it is dropped (GR-2.1, GR-2.3).
   **Restricted pass** (confirmations and contradictions only, no additions) for the pages or parts that cover the seven thin
   boxes, and for `cost-per-change` and `reviewer-load`, where public evidence is weak and a
   library addition would become the only structure.
4. The author writes from the brief, the skeleton, the evidence brief, the concept diff and the site's
   own pages. The skeleton fixes the order of every list and sequence.

### (b) Sweep per batch, riskiest first

Each sweep run compares at most four pages. Writing order follows risk, so the first sweeps happen
while most pages are unwritten.

| Batch | Pages | Why this order | Sweeps |
|---|---|---|---|
| A | `cost-per-change`, `reviewer-load`, `delivery-templates`, `agent-permissions` | highest risk: covered boxes whose public evidence is weak (cost, review load) or whose shape is a list a library document is likely to hold (template fields, the grant-review-revoke steps of an access review); `reviewer-load` also sits next to the glossary entry `review-fatigue`, which the D-030 diagnostic found close | two independent sweep runs even when the first is clean (a second researcher context aimed at list, order and examples), then a re-sweep after every rewrite |
| B | `measurement`, `delivery-metrics`, `escaped-defects`, `evidence-record` | covered boxes with strong public definitions; the risk is in the set and order of measures and in the record's reader list | one sweep, a re-sweep after any rewrite |
| C | `check-results-and-decisions`, `change-controls-and-standards`, `ai-use-policy` | thin boxes on the restricted pass; written last so the SOC 2 confirmation (open question 5) can arrive first | one sweep, a re-sweep after any rewrite |
| D | all 11 on final text, with the map text, diagram text, glossary entries and every changed passage of a Core or Lifecycle page | catches anything changed by cross-page edits and back-links | one run, hash-checked |

The main session keeps a **sweep ledger** in the scratchpad: page, sha256 of the page text at sweep
time, batch, round, result; hashes and verdicts only, never passages. Before any push the session
confirms every page's current hash matches a clean entry; a page changed since is swept again. Edits
made in review rounds are swept on the changed passages before each push. Lessons from batch A carry
forward as process only (rounds taken, categories flagged); the architect tightens later briefs by
requiring a public citation for every list item, and adds nothing the sweep revealed.

### (c) Who rewrites

When the sweep flags a passage, the main session cuts it and leaves a gap holding only the brief's
question for that heading and the skeleton items. A **fresh author** in a new context, which sees
neither the removed text nor the sweep notes, writes the replacement, which is swept again as new
text. Anyone who has read the library never writes replacement text.

### (d) Exit criterion

A page passes when a fresh sweep run reports no close passage in any of five categories (wording,
list membership and order, step sequence, set of examples, heading structure) for the page text
whose hash is in the ledger. Batch A pages need two consecutive clean runs from two researcher
contexts. The section passes when run D is clean for all 11 pages and every changed Core or Lifecycle
passage, and every ledger hash matches. Nothing is pushed, and no pull request is opened, before
then. This plan's own pull request carries no page text and is not subject to the sweep.

### (e) Budget and the cap

At most three sweep rounds per page. After a third failing round the page goes to the author with
three options: cut the passage without replacement where the template minimum still holds; the
author rewrites it personally; or the box merges into a neighbouring page. If two pages of batch A, or
three pages across B and C, reach a third round, work stops and the architect re-plans the grain with
the author.

### (f) The running example

The customer-record export stays the only worked example (GR-3.4). The facts come from published
pages only: the access rule R-042, the volume rule R-017, the 50k-row load scenario, the broader
background-worker query, the later production incident. Assurance uses them to show the evidence
record read by a release decision and by an auditor (`evidence-record`), a load scenario that could
not run and what that means for the merge (`check-results-and-decisions`, using only what Core says),
and the incident traced back as an escaped defect (`escaped-defects`). Measurement pages count the
export as one change **without figures**: no lead time, cost or review minutes are invented (GR-2.3).
The architect lists the allowed facts in each brief; the source researcher never sees them.

### (g) What the confidentiality reviewer adds

Cold checks it can make without the library: provenance of every list, sequence and table (found in a
cited source or a site page, or flagged); every number, threshold, cadence, role title or acronym
traced to a source or glossary entry; text that reads as one organisation's controls or audit history
(a control set, a review cadence or a role split no public source gives); fingerprinting combinations
across pages (D-017); vendor names (GR-3.3). The reviewer is told the sweep passed and on which hashes,
never what it found.

## Map and link changes

All map changes need the author's approval (ASSUMPTIONS A2); none adds a box.

- **Band 5 bullets become links.** `bullet_col` in `build_map.py` draws each bullet as plain text, and
  `linked()` marks a label only when it matches one `<text>` element. The site-builder changes
  `bullet_col` so that each bullet whose full text is a key in `links.yml` is wrapped, with all of its
  wrapped lines, in one link, and the label underline covers each line. The build's check that every
  `links.yml` label appears on the map then covers bullets too. Band 4's bullets stay unlinked until the
  Enablement section.
- **One bullet split.** "Escaped defects; reviewer load and concentration" becomes two bullets,
  "Escaped defects" and "Reviewer load and concentration", because they open different pages. The
  Measurement column then has five bullets; the band height grows enough for the extra line, and
  `MAP_DESC` is unaffected (it names the column, not the bullets). This is a relabel, not a new box.
- **New `links.yml` entries (14: 13 bullets after the split, covering all 16 boxes, and 1 column title):**
  - "Evidence record on every run, fixed schema" → `evidence-record.html`
  - "Rule IDs link rule → check → decision" → `evidence-record.html#<rule-ids anchor>`
  - "passed · failed · skipped · could_not_run" → `check-results-and-decisions.html`
  - "Valid for one revision; a new push expires it" → `evidence-record.html#<validity anchor>`
  - "Templates: spec, plan, ADR, release notes" → `delivery-templates.html`
  - "SOC 2 change controls; domain standards as they apply" → `change-controls-and-standards.html`
    (one bullet, one link; the second anchor is reached from the page's own contents)
  - "AI use policy: data sent to models, IP of generated code" → `ai-use-policy.html`
  - "Agent permissions reviewed as privileged access" → `agent-permissions.html`
  - the Measurement column title → `measurement.html`; "Baseline before changing anything" →
    `measurement.html#<baseline anchor>`
  - "Flow metrics and DORA delivery metrics" → `delivery-metrics.html`
  - "Escaped defects" → `escaped-defects.html`; "Reviewer load and concentration" → `reviewer-load.html`
  - "Cost per change, including tokens and evals" → `cost-per-change.html`
  Anchor slugs are fixed when the headings are, and the link check covers them (GR-4.3).
- **Column titles.** Only "MEASUREMENT" is linked (it has a hub page). Linking an upper-cased title
  needs `linked()` to match the displayed text; the site-builder keys it by the displayed label.
- **Routing row.** "Lead adoption" gains `measurement`; "Look it up" gains `evidence-record` and
  `check-results-and-decisions`.
- **Back-links to published pages** (both ways, as D-018 and D-029 do), each under a D-011
  confirmation review and a sweep of the changed passage:
  - Core `validators`: the two sentences that defer to "the assurance band of the map" link to
    `check-results-and-decisions`.
  - Core `evidence-schema`: "Where it sits on the map" links to `evidence-record` (validity, audit).
  - Core `rule-registry`: "Related" gains `evidence-record` (rule ID traced to decisions).
  - Core `workflows`, `skills-and-evals`, `software-factory`: "Related" gains `measurement`,
    `reviewer-load` and `cost-per-change` where the page already names those concerns.
  - Lifecycle `traceability-spine` (audit and validity), `release` (change controls), `operate` and
    `deploy` (delivery metrics), `definition-of-ready-and-done` (templates), `develop-build-qa`
    (metric definitions, escaped defects).
  - Lifecycle 1.6.0 workflow pages, if published first: each workflow page's "Measures" links to the
    metric pages. The links are added in 1.7.0, not by restating definitions on the workflow pages.
  - Pages whose passages are listed as close or borderline in the 1.4.x findings (STATUS) gain only a
    link in "Related", never an edit of the flagged passage (open question 2).
- **Credit lines.** The map's footer gains no new line: the Assurance pages cite DORA, AICPA and NIST
  (the wave 0 retrospective dropped a visible DORA / SOC 2 credit line). If the map's band 5 text keeps
  only "DORA delivery metrics" and "SOC 2", the existing rule (D-009) is met by the glossary credit.

## Glossary candidates

About twelve new entries, each with its attribution (GR-2.2). Entries come with the page that uses
them (D-025).

| Entry | Attribution |
|---|---|
| DORA software delivery metrics (one entry naming the five) | DORA |
| Flow metrics | SAFe's published wording; Flow Framework credited where SAFe credits it |
| Baseline | common |
| Escaped defect | common; the escape rate after ISTQB's defect detection percentage |
| Defect detection percentage | ISTQB glossary |
| Reviewer load | *coined* |
| Reviewer concentration | *coined* (may merge with reviewer load) |
| Cost per change | *coined* |
| Evidence validity (valid for one revision) | *coined* |
| Waiver | common |
| Least privilege | NIST SP 800-53 (AC-6) |
| Privileged access review | NIST SP 800-53 (AC-2, AC-6) |
| Trust Services Criteria | AICPA (wording only as far as confirmed, see "Source access") |
| AI use policy | common |

Existing entries the section uses: `evidence-record`, `could-not-run`, `architecture-decision-record`,
`rule-registry`, `risk-tier`, `gate`, `validator`, `skill-erosion`, `traceability-spine`,
`export-example`. **`review-fatigue` is not used** by any Assurance page until the 1.4.x fix edition has
rewritten it (it is on the close list); `reviewer-load` links to its own new entry instead.

## Diagrams

Up to three, each with a text alternative and both themes (GR-4.4), swept with the page:

1. `evidence-record`: one record and its three readers, with the revision line showing that a push
   starts a new record and leaves the old one attached to the old revision.
2. `change-controls-and-standards`: control → rule → check → record → reviewer, with the human
   approval marked.
3. `measurement`: the five measure families and the evidence fields each derives from.

## Related pages outside the section

| Page | Exists | How it is handled |
|---|---|---|
| The nine Core pages | yes | linked directly; back-links as above |
| The twelve Lifecycle 1.5.0 pages | yes | linked directly; back-links as above |
| Lifecycle 1.6.0 workflow pages | after 1.6.0 merges | linked if published before 1.7.0 is written; otherwise the catalog rows (`workflow-catalog.html#W23`, `#W25`, `#W26`, `#W28`) |
| Workflow catalog | yes | rows W02, W25, W28, W32, W33, W35 linked, never restated (D-030) |
| Enablement pages (permissions, review load, decision rights, model providers) | no | no link to a page that does not exist (GR-4.3); glossary entries stand in; Enablement adds the links both ways in its edition |
| Context pages (risk tier, regulated product types) | no | glossary entry `risk-tier` and Core `workflows` |
| Adoption stages | no (home-page `#adoption` only) | link to `index.html#adoption` |

## Order of work

0. **Plan approved; plan pull request** (this file and the decision; no page text).
1. **Briefs** (architect, scratchpad), the **outline pass** (public skeleton), the architect fixing the
   skeleton in each brief; then the library concept diff and the evidence briefs, by batch, batch A
   first. The SOC 2 confirmation request goes to the author at this step.
2. **Batch A** written, swept twice, rewritten, re-swept. **Batch B**, then **batch C** (after the SOC 2
   answer, or on the fallback if the author declines).
3. **Diagrams** (up to three).
4. **Map and routes:** `bullet_col` linking, the bullet split, `links.yml`, `toc.yml` (an `assurance`
   list), `release/sections.yml` (`"1.7"`), glossary entries, routing row, back-links.
5. **Sweep D**, ledger check; the branch rebuilt as one commit on top of `main`; checks run; push.
6. **Review** in fresh contexts in two groups (evidence and standards, pages 1 to 6; measurement, pages 7
   to 11): three reviewers, three rounds, then the author; a D-011 confirmation review for the Core and
   Lifecycle back-links.
7. **Merge as 1.7.0**, the author reviews it live, follow-ups as 1.7.x, tag at approval.

## Cost and size

| Step | Runs | Rounds |
|---|---|---|
| Briefs (architect, per batch) | 3 | 1 |
| Outline pass (external, per batch) | 3 | 1 |
| Library concept diff (source-researcher, grouped) | 4 to 5 | 1 |
| Evidence briefs (external-researcher, one per page) | 11 | 1 |
| Author, first writing | 11 | 1 |
| Author, rewrites after sweeps (fresh contexts) | 5 to 9 | up to 3 per page |
| Diagrammer | 3 | 1 |
| Sweeps (up to 4 pages a run; batch A twice by two contexts) | 10 to 15 | up to 3 per page |
| Site-builder (map, links, glossary, checks, PR) | 3 | 1 |
| Reviewers (3 reviewers x 2 groups; later rounds the groups still open) | 12 to 18 | up to 3 |
| Confirmation review for back-links | 3 | 1 |
| **Total** | **about 70 to 85** | |

About two thirds of Lifecycle 1.5.0. The main variables are the sweep rounds on batch A and the SOC 2
confirmation. New references number about 40 to 60; the author adds them to `content/references.yml`
as before.

## Risks

- **Restating Core and Lifecycle.** The evidence column overlaps `evidence-schema`, `validators`,
  `rule-registry` and `traceability-spine` almost entirely. D-030 applies; the editorial reviewer
  checks each Assurance page for restated definitions, and the grain is kept small (two pages for four
  boxes).
- **Closeness on covered boxes with weak public evidence.** `cost-per-change` and `reviewer-load` are
  where the library could become the only structure. Restricted library pass, batch A double sweep,
  recommended-practice labels.
- **Templates as lists.** The four templates' fields are exactly the list shape a library holds. The
  skeleton takes fields only from public formats (Nygard, Keep a Changelog, Semantic Versioning); a
  field no public format or site page has is left out.
- **Control frameworks without readable text.** SOC 2 and ISO text cannot be read from a session; the
  pages say less rather than fill the gap (KICKOFF (b)). The residual risk is a thinner SOC 2 section
  than readers expect; the page remains complete because its mechanism stands on NIST.
- **Legal-sounding claims.** `ai-use-policy` touches data protection and copyright. It states no legal
  conclusion and frames each point as a policy question (open question 7).
- **One organisation's controls.** A control set, review cadence or approval chain specific enough to
  recognise is a GR-1.1 and D-017 risk; the confidentiality reviewer's cold checks target it, and no
  cadence appears that a public source does not give.
- **Metric misuse.** Pages that define reviewer load and cost could be read as individual scoring;
  each says otherwise with a source or as recommended practice.
- **Dependency on the 1.4.x fix edition.** Several pages Assurance links into carry close or
  borderline passages (STATUS, 1.4.x findings). Linking to them before the fix is harmless to the
  link but ties the review of 1.7.0 to text that will change (open question 2).
- **Map change.** Linking bullets touches the shared `bullet_col`; band 4 must not change. The
  site-builder adds a test that band 4 bullets stay unlinked until Enablement.

## Open questions for the author

1. **Order.** Is Assurance the first section of wave 2, ahead of Enablement? **Recommendation: yes**
   (reasons above). And does it follow Lifecycle 1.6.0 as edition 1.7.0? **Recommendation: yes,**
   keeping D-029's order; Assurance briefs and the public skeleton can be prepared while 1.6.0 is in
   review, and the 1.6.0 workflow pages gain their measure links in 1.7.0.
2. **The 1.4.x fix edition first?** Assurance links into Core passages and a glossary entry on the
   1.4.x close and borderline lists. **Recommendation: run the fix edition before 1.7.0 is written,**
   so back-links land on settled text; if not, Assurance adds links only in "Related" on those pages and
   never uses `review-fatigue`.
3. **Pages and merges.** Are the 11 pages and their merges approved (evidence record with rule IDs and
   validity; SOC 2 with domain standards; flow with DORA metrics; one Measurement hub)?
   **Recommendation: yes.** Fallback for a smaller section, 9 pages: escaped defects and reviewer load
   on one page `quality-and-review-measures`, and cost per change folded into `measurement`.
4. **Map changes.** Are linking band 5's bullets, splitting "Escaped defects; reviewer load and
   concentration" into two bullets, linking only the Measurement column title, and the back-links listed
   above approved? **Recommendation: yes.**
5. **SOC 2 text.** Will the author read the change-management criterion (CC8.1) and its points of focus
   in the AICPA document in a browser and paste them into chat before batch C? **Recommendation: yes;**
   without it the page names SOC 2 and the Trust Services Criteria only and carries the mechanism on
   NIST SP 800-53.
6. **Domain standards.** May the domain-standards anchor name any standard at all, given that no
   ISO/IEC/IEEE text is readable? **Recommendation: name none by clause; name at most a few as examples
   of a category, with titles the author confirms in a browser, or name none** and describe the
   mechanism only.
7. **AI use policy and the law.** Is "no legal conclusions; every IP and data point framed as a policy
   question, sourced to NIST" the right line? **Recommendation: yes.**
8. **Metric block or metric template.** Is the fixed metric block inside Concept pages (definition,
   formula with unit, data source, source of the definition, how it misleads), checked by the editorial
   reviewer, enough, or should a seventh template "Metric" be added with a `check_pages.py` change?
   **Recommendation: the block now; a template only if Enablement or Context also need one.**
9. **Allow-list.** Should the environment's allow-list gain `aicpa-cima.com`, `genai.owasp.org`,
   `eur-lex.europa.eu`, a national copyright office host and `queue.acm.org`? Each is then tested with a
   plain request, and a refusal is handled as KICKOFF (b) says. **Recommendation: add them;** none is
   required for the section to be complete.
10. **Benchmarks.** Is "no benchmark values on any page; metrics defined and linked to DORA's guide and
    report" approved? **Recommendation: yes.**
11. **Running example.** May measurement pages count the export as one change without any figures?
    **Recommendation: yes;** no lead time, cost or review minutes are invented.
