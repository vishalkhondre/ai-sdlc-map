# Section plan: Lifecycle (band 2)

Proposed by the architect, 2026-10-06. **Approved by the author with changes, 2026-10-06 (D-029);**
the changes are applied below. The author's answers to the eight open questions are at the end of
this file.

- **Section:** lifecycle, band 2 of the map ("where it runs"), **delivered as two editions** (D-029):
  - **1.5.0, 12 pages:** the generic level labels (D-015 relabel), `lifecycle-levels`,
    `safe-reference-model`, the seven phase pages, `definition-of-ready-and-done`,
    `traceability-spine`, `inspect-and-adapt`.
  - **1.6.0, 7 pages:** the seven workflow pages.
  - Each edition is merged, deployed, reviewed live by the author and tagged separately. Follow-ups
    before a tag are patch editions of that minor (1.5.x, 1.6.x); the tag is created at approval
    (D-016). `release/sections.yml` gains a `"1.5"` entry when 1.5.0 merges and a `"1.6"` entry when
    1.6.0 merges, each naming that edition's pages.
- **Sources:** `project/COVERAGE.md` rates 18 of the 22 band-2 boxes as covered by the source
  library and four as thin (Portfolio, Deploy, Operate and the deploy verification workflow). Every page cites public sources for its claims (GR-2). The library
  informs practice only (GR-1.2), and this plan builds each page's structure from public sources
  first so that the library never supplies it (see "Library check built in from the start").
  Borrowed terms keep their credit: SAFe terms (Scaled Agile, Inc.), the Definition of Done
  (Scrum Guide), WSJF (Reinertsen, through SAFe), Inspect & Adapt (SAFe); terms this site coins are
  marked *coined* (GR-2.2).
- **Page count:** 19 pages for 22 boxes plus the SAFe reference model (D-015): 12 in 1.5.0 and 7 in
  1.6.0. Core had 9.
- **Each edition is complete on its own (GR-4.1).** Until 1.6.0, the seven workflow labels on the map
  and the "Workflows in this phase" lists of the phase pages link to the workflow catalog rows; in
  1.6.0 those links move to the workflow pages. 1.6.0 therefore edits pages published in 1.5.0 (the
  phase pages, the map, the Core back-links): those edits are checked by a confirmation review
  (D-011), and by a sweep of the changed passages.

## Boundary with the other sections

Lifecycle says where in the delivery flow each decision falls and what the phase asks of the
workflow that runs in it. It does not redefine what Core defines, and it leaves to later bands what
they own.

| Topic | Lifecycle (this section) | Other section |
|---|---|---|
| What a workflow is | one workflow page per mapped decision: its trigger, inputs, checks, failure paths, measures and owner as they fall in this phase | Core `workflows`: the unit itself, the three roles, the nine-part definition, hand-offs in general |
| Workflow list | the seven mapped workflows in depth | the workflow catalog stays the list of all 35 and the traditional-to-AI table |
| Rule IDs and records | the traceability spine: which identifiers link which artefacts from requirement to incident, and the orphan checks along it | Core `rule-registry` (what the registry holds) and `evidence-schema` (fields of a record); assurance (reading records for audit, validity per revision) |
| Feedback path | the incident feedback workflow and Inspect & Adapt: how a finding is classified and converted, and what each planning interval reviews | Core `harness-engineering` (the steering loop) and `software-factory` (the operating state it produces) |
| The verify command, checks, skills | where they run in Develop, Build and QA | Core `engineering-kit`, `validators`, `skills-and-evals` |
| Risk tier | where a tier is proposed (intake, spec readiness) and where it becomes a gate set (design conformance) | Core `workflows` and the glossary define it; context (band 1) owns the tier and the flows that shorten or skip phases (hotfix, bug fix, spike) |
| Cadence and ceremonies | Inspect & Adapt as the lifecycle's feedback checkpoint: what it inspects and what it may change | enablement (operating model): the PI cadence, system demo, Scrum/Kanban on a train, decision rights |
| Roles | the role accountable at each gate, by title | enablement (people and roles): what each role owns and how it shifts |
| Tools and agent runtime | what the agent does in each phase | enablement: coding agents, MCP, sandboxes, permissions, SDD frameworks |
| Measures | the measures each workflow page names, with a baseline to compare against | assurance (measurement): metric definitions, DORA metrics, escaped defects |
| Templates and audit | which phase produces a spec, plan, ADR or release notes | assurance: the templates, SOC 2 change controls, audit use of records |
| Which workflow first | what each workflow page says it needs before it runs | adoption path: stage 1 builds pull-request verification, stage 2 specification readiness |

## Pages

**Edition 1.5.0:** rows 1 to 9 and 17 to 19 (12 pages). **Edition 1.6.0:** rows 10 to 16 (7 pages).
Row numbers keep the architect's original numbering, which the scope cells cross-refer to.

| # | Page id | Type | Map box | Coverage | Scope | Leaves to others |
|---|---|---|---|---|---|---|
| 1 | `lifecycle-levels` | Concept | Portfolio · Train · Team (three labels, three anchors) | Portfolio thin; Train, Team covered | One lifecycle at three altitudes (generic labels, D-015): what a portfolio decides (initiatives, prioritisation, budgets), what a train decides (features, a planning cycle, an integrated demo), what a team decides (stories, iterations, readiness and done); what flows down (intent, rules) and up (evidence, lessons); which phases and workflows run at which level. SAFe cited as one framework that uses these levels. Portfolio relies mainly on public sources. | The SAFe mapping (page 2); cadence and decision rights (enablement) |
| 2 | `safe-reference-model` | Concept | none (reached from page 1 and the section navigation; see map changes) | informed by the library (D-015) | A worked reference model that maps the AI SDLC onto SAFe levels and events, built from SAFe's published structure and this site's own pages. Presented only as "a reference model". | Cadence and decision rights (enablement); SAFe itself beyond the mapping |
| 3 | `idea` | Phase | Idea | covered | Where an idea becomes a classified, sized item; traditional intake and estimation; what an agent drafts and what a person decides; intake record. | Intake workflow detail (page 10); flows that skip phases (context) |
| 4 | `specification` | Phase | Specification | covered | Intent into a specification a team can plan from; ambiguity, edge cases, testable criteria, open questions; the Definition of Ready tag sits here; readiness record. | Spec-driven tool choices (enablement); templates (assurance); readiness workflow detail (page 11) |
| 5 | `design` | Phase | Design | covered | Technical approach, contracts and data design; where the risk tier becomes the gate set; plan with gate declaration; judgment-only design review stays with a person. | Conformance workflow detail (page 12); architect role (enablement) |
| 6 | `develop-build-qa` | Phase | Develop · Build · QA (security, performance); three labels | covered | The three phases in which one change is made, assembled and tested: the verify command as the deterministic floor, builds, test levels, security and performance checks by tier; one workflow spans all three (the map draws it as one bar). Merged, see below. | Pull-request verification detail (page 13); kit commands (Core); metric definitions (assurance) |
| 7 | `deploy` | Phase | Deploy | thin | Moving a verified build into an environment: environments, strategies (rolling, canary, blue-green), rollback, configuration; the difference between deploying and releasing. Relies mainly on public sources. | Deploy verification workflow detail (page 14); runner and host adapters (enablement) |
| 8 | `release` | Phase | Release | covered | Deciding that a deployed or deployable change is exposed to users: go/no-go, notes, known risks, toggles; the Definition of Done tag sits here; release record. | Release readiness workflow detail (page 15); change controls (assurance) |
| 9 | `operate` | Phase | Operate | thin | Running the change in production: monitoring, incidents, vulnerability and usage feedback, maintenance; the loop by which incident feedback changes what Specification asks. Relies mainly on public sources. | Incident feedback detail (page 16); measurement (assurance) |
| 10 | `intake-and-triage` | Workflow | intake & triage | covered | Decision: what kind of work is this, and which lane does it enter? Adds to catalog W01: inputs, guardrails, failure paths, measures, owner, the export example. | The tier concept (Core, context); flows (context) |
| 11 | `spec-readiness` | Workflow | spec readiness | covered | Decision: is the specification ready to plan from? Adds to W04 the full template with the readiness record. Adoption stage 2 builds it. | Task-level readiness (W12, page 17); adoption order |
| 12 | `design-conformance` | Workflow | design conformance | covered | Decision: is the technical approach acceptable, and which gates apply? Adds to W08 the full template; plan with gate declaration. | Contract and data workflows (catalog only); judgment-only design review (catalog W24) |
| 13 | `pull-request-verification` | Workflow | pull-request verification · security & performance checks by tier | covered | Decision: is this change ready to merge? Adds to W23 the full template; how the results of the acceptance, security and performance checks it aggregates reach the reviewer. Adoption stage 1 builds it. | The checks (Core validators); W17 to W21 stay in the catalog |
| 14 | `deploy-verification` | Workflow | deploy verification | thin | Decision: is the deployment healthy, or do we roll back? Adds to W26 the full template. Relies mainly on public sources. | Deployment strategy (page 7); incident response (catalog W27) |
| 15 | `release-readiness` | Workflow | release readiness | covered | Decision: is this release safe to deploy? Adds to W25 the full template; aggregating evidence per revision; organisational controls stay in force. | Change control and exceptions (catalog W32, W33; assurance) |
| 16 | `incident-feedback` | Workflow | incident feedback | covered | Decision: what must change upstream so this does not recur? Adds to W28 the full template; classification, conversion to a criterion, test, validator or eval; closing the loop. | The steering loop (Core); remediation (catalog W27) |
| 17 | `definition-of-ready-and-done` | Concept | Definition of Ready / Done (the DoR and DoD tags) | covered | What each is, who owns it, how it is written so a machine can check part of it; two layers of readiness (specification, task); done at story, increment and release; how agents change both. | Workflow detail (pages 11, 15); templates (assurance) |
| 18 | `traceability-spine` | Concept | Traceability spine | covered | The chain requirement, spec, task, test, change, release, incident; how identifiers link each pair; orphan checks; what breaks when a link is missing; rule IDs as link keys. | Record fields (Core `evidence-schema`); audit and validity per revision (assurance) |
| 19 | `inspect-and-adapt` | Role or practice | Inspect & Adapt | covered | The checkpoint where evidence from the spine and from incident feedback is reviewed and a workflow is added or tightened; what it inspects, who attends and decides, what shifts with agents, warning signs. | Calendar and cadence (enablement: operating model) |

**Acceptance criterion for the workflow pages (author, D-029).** Each of the seven must add failure
paths, evidence and measures beyond its catalog row: a row names the evidence in one cell and has no
failure paths or measures. The page states the failure paths (including `could_not_run`), the
evidence record it writes and who reads it, and the measures with a baseline. The editorial
reviewer checks this per page and returns REVISE for a page that only restates the row.

**Anchors (author, D-029).** Every map box that shares a page has its own anchor: the three level
labels on `lifecycle-levels` (Portfolio, Train, Team), Develop, Build and QA on `develop-build-qa`,
and the DoR and DoD tags on `definition-of-ready-and-done`. Each anchor is a heading, so its slug
is stable, and the link check covers it (GR-4.3).

### What was merged, what was kept apart, and why

- **Phases: seven pages for nine boxes.** The nine phases get seven pages. Develop, Build and QA
  share one page because the map itself draws one workflow across all three (pull-request
  verification), they share one gate set and one evidence record, and three Phase pages would repeat
  "Workflows in this phase", "Gates and evidence" and "Roles" three times. Each of the three map labels
  links to the page; the page opens each of its "Traditional practice" and "AI-assisted practice"
  sections with one sub-heading per phase, so the reader still finds Develop, Build or QA directly.
  Deploy and Release stay apart: they have different workflows, owners and evidence, and the
  difference between deploying a build and releasing a change is itself a distinction readers look
  up. Idea, Specification, Design and Operate each own one workflow and one set of artefacts.
- **No section overview page.** The band label is not a box and the left navigation already lists the
  section. `lifecycle-levels` and the phase pages carry the orientation a reader needs, and each
  stands alone (GR-4.2). An overview would add a page that has no box.
- **Levels: one page for three boxes.** Portfolio, Train and Team are one idea at three altitudes. Three
  pages would share one definition, and Portfolio has the thinnest evidence. Each label links to its
  own anchor on the page.
- **Workflows: seven pages, not seven catalog links.** The catalog already holds W01, W04, W08, W23,
  W25, W26 and W28 as one row each (decision, trigger, agent task, checks, people, evidence, the
  traditional counterpart). It stays the list, and a Workflow page does not repeat the row. A page
  adds what a row cannot hold and the Workflow template requires: inputs from named upstream records,
  guardrails, failure paths including could_not_run, measures with a baseline, the owner, and the
  export example run through the workflow. Each of the seven is a different decision with a
  different owner and different failure paths, so merging any two would break the template's
  single "Decision". The cost is seven pages; the fallback in open question 2 is five.
- **Concepts and practice.** DoR/DoD and the traceability spine are Concept pages: each is a thing
  defined once and used by many workflows. Inspect & Adapt is a Role or practice page: it is a
  recurring event with participants, decisions and warning signs.
- **The SAFe reference model is a separate page, not a section of `lifecycle-levels`.** D-015 sets
  tighter confidentiality handling for it (double sweep, author's recognisability check). Keeping it
  on its own page confines that handling to one file and keeps the generic levels page vendor-neutral.

### Page type fit

All pages fit one of the six templates. Three fits are imperfect and need no new template:

- `safe-reference-model` uses Concept. "How it works" holds the mapping tables; "Definition" states
  what a reference model is and is not. No Workflow or Phase section applies.
- `develop-build-qa` uses Phase with a sub-heading per phase inside two sections. The template's nine
  H2 sections stay in order (`check_pages.py` enforces them).
- `inspect-and-adapt` uses Role or practice. "Responsibilities" holds who attends and decides.

Phase pages that map to the catalog use the catalog's phase grouping only to point at it: the catalog
groups Develop, Verify and Review as phases 3 to 5 and puts deployment and release readiness both
under Release (phase 6); each phase page says in one sentence which catalog phase holds its workflows.

### Pages that rely on public sources only

| Page | Why | How it is shaped |
|---|---|---|
| `lifecycle-levels` (Portfolio part) | Portfolio is rated thin | Built from SAFe's published portfolio material, the lean budgeting and WSJF sources it cites, and DORA on prioritisation and batch size. Where no public source says how agents change portfolio decisions, the text is labelled recommended practice (GR-2.3). |
| `deploy` | thin | Built from Humble and Farley, Fowler on deployment pipelines, canary and blue-green releases and feature toggles, DORA on deployment practices, and the Google SRE book on canarying and release engineering. |
| `operate` | thin | Built from the Google SRE book and workbook (monitoring, incident response, postmortems), NIST SP 800-61 for incident handling, DORA on recovery, and NIST SSDF for vulnerability response. |
| `deploy-verification` | thin | Built from the same sources as `deploy`; the agent task and the on-call decision are labelled recommended practice. |
| `safe-reference-model` | informed by the library under D-015, but the plan treats it as public-only in structure | Every SAFe-side statement cites SAFe; every AI SDLC-side statement links to a page on this site. The library is consulted only by the sweep. |

For these pages the source researcher's library pass is restricted further (see "Library check"):
a thin box means the library's few passages would become the only non-public structure, which is
where a close paraphrase is most likely.

## Library check built in from the start

D-026 holds throughout: authors never read the library or notes by anyone who did; the source
researcher passes concepts only; the sweep runs before the first review; nothing is pushed before it
passes; the pushed branch is one commit on top of `main` with a neutral message. The plan changes the
order of work, not the rules, so that the sweep catches problems when they are cheap and the lessons
reach later pages.

### (a) Public skeleton first

1. The architect writes each brief from the map, the catalog, the glossary and the published Core
   pages only. The architect does not read the library; `COVERAGE.md` is the only library-derived
   input. A brief never contains library material.
2. An **outline pass** by `external-researcher` runs before any library pass. For each page it
   returns the public skeleton: the headings' content points, each list and its items, the sequence
   where one exists, and the examples, each tied to a public source (standards such as ISO/IEC/IEEE
   29148 and 12207, SAFe, the Scrum Guide, DORA, NIST, the SRE book, Fowler, Humble and Farley,
   ISTQB). The architect fixes the skeleton in the brief. A list, order or example with no public
   source and no site page behind it is not in the skeleton.
3. The `source-researcher` then reads the library **with the skeleton in hand** and returns a diff
   keyed to skeleton item numbers: confirmed general practice, contradicted or not general practice,
   and unordered single concepts the skeleton lacks (three to six words each, no wording). Each added
   concept must then get a public source from `external-researcher` or it is dropped (GR-2.1,
   GR-2.3). For thin boxes the pass returns confirmations and contradictions only, with no additions.
4. The author writes from the brief, the skeleton, the evidence brief, the concept diff and the
   site's own pages. The skeleton fixes the order of every list and sequence.

### (b) Sweep per batch, highest risk first

The sweep runs on batches as soon as they are written, not once at the end. Writing order follows
risk, so the first sweeps happen while most pages are still unwritten. Each edition is swept
separately, in the same way: riskiest batch first, then a final full sweep of the edition's pages
on final text (D-029).

**Edition 1.5.0**

| Batch | Pages | Why this order | Sweeps |
|---|---|---|---|
| A | `safe-reference-model`, `definition-of-ready-and-done`, `traceability-spine`, `inspect-and-adapt`, `lifecycle-levels` | highest risk: D-015 page and the three practice concepts whose lists and sequences a library document is likely to hold | two independent sweep runs even when the first is clean (a second researcher context, aimed at list, order and examples), then a re-sweep after every rewrite |
| B | the seven phase pages | each has a "Traditional" and an "AI-assisted" list and a gates list, the shapes most likely to follow a library's | same as A; the thin pages (`deploy`, `operate`) get the restricted library pass |
| D1 | all 12, on final text, with the map text and diagram text | catches anything changed by cross-page edits | one run, hash-checked (see below) |

**Edition 1.6.0**

| Batch | Pages | Why this order | Sweeps |
|---|---|---|---|
| W1 | `pull-request-verification`, `incident-feedback`, `release-readiness`, `spec-readiness` | the four covered workflows with the longest check, failure-path and measure lists, and the two the adoption path builds first | two independent sweep runs even when the first is clean, then a re-sweep after every rewrite |
| W2 | `intake-and-triage`, `design-conformance`, `deploy-verification` | the template fixes the sections, so structure risk is low, but the checks, failure-path and measure lists are not; `deploy-verification` is thin | one sweep, a re-sweep after any rewrite; `deploy-verification` gets the restricted pass |
| D2 | all 7, plus every passage of a 1.5.0 page that 1.6.0 changes | catches anything changed by cross-page edits | one run, hash-checked |

The 1.6.0 pages are written after 1.5.0 is merged, so the process lessons from 1.5.0 reach their
briefs (the main session carries categories and counts only, never passages).

The main session keeps a **sweep ledger** in the scratchpad: page, sha256 of the page text at sweep
time, batch, round, result. It holds hashes and verdicts, never passages. Before any push the session
confirms that every page's current hash matches a "clean" entry; any page changed since is swept
again. Edits made in review rounds are swept on the changed passages before each push.

What the lessons from batch A may carry forward is limited to process: how many rounds it took, which
categories (wording, list, sequence, examples, structure) were flagged, never the passages. The
architect tightens the later briefs by requiring a public citation for every list item, and does not
add anything the sweep revealed.

### (c) Who rewrites

When the sweep flags a passage, the main session cuts it out and leaves a gap holding only the
brief's question for that heading and the skeleton items. A **fresh author** in a new context, which
sees neither the removed text nor the sweep notes, writes the replacement. The main session routes
the notes and writes no text. The replacement is swept again as new text. Anyone who has read the
library, including the source researcher, never writes replacement text.

### (d) Exit criterion

A page passes when a fresh sweep run reports no close passage in any of five categories (wording,
list membership and order, step sequence, set of examples, heading structure) for the page text
whose hash is in the ledger. For batch A pages the criterion needs two consecutive clean runs from
two researcher contexts (the same applies to batch W1). An edition passes when its final run (D1 or
D2) is clean for all its pages and every ledger hash matches. Nothing of that edition is pushed, and
no pull request is opened for it, before then. The plan's own pull request carries no page text and
is not subject to the sweep; the page work stays on a local branch that is never pushed (D-026).

### (e) The SAFe reference model

- **Skeleton from SAFe alone.** Levels, events, roles and artefacts come from SAFe's published pages,
  each cited with the framework version and access date (GR-2.4, GR-2.5). The mapping to the
  AI SDLC joins each SAFe item to a page of this site. No third-party account of running SAFe with
  agents is used.
- **Closed allow-list.** The brief carries a list of the SAFe terms the page may name, drawn from
  SAFe's own published vocabulary (see open question 4). Any other term, number, cadence, event
  name or role split fails review as an unattributed structure. Cadence figures appear only as
  SAFe's published defaults, with a citation.
- **Mapping only.** The page states what lines up with what and why. It never says how an
  organisation runs it, never counts trains, teams or releases, and uses the export example only as a
  hypothetical feature travelling through the model.
- **Extra checks.** Double sweep (batch A). A confidentiality read with one added question: could a
  reader who knows an organisation tell where the model came from? An accuracy pass against SAFe's
  site for every SAFe-side statement.
- **The author's recognisability check (D-015, GR-1.2).** The author reads the page and answers three
  questions: would anyone who knows the originating organisation recognise it; does any term, number,
  sequence, event name or role split lie outside public SAFe; does any sentence read as a description
  of how one organisation works. **The author reads the page text in chat before its first push**
  (D-029), because after a merge the text is public and in history. The main session shows the full
  page text once it has passed the sweep and before any push of edition 1.5.0, and pushes nothing until
  the author answers. The author's confirmation is recorded in a pull-request comment and a line in
  `STATUS.md`; the release tag then records approval of the edition as D-016 sets out.
- **Forbidden names by category only (D-029).** The brief lists what the page may not name by
  category (no cadence or count SAFe does not publish, no tooling, no organisation structure, no
  account of how any organisation applies SAFe), never by name (GR-1.4).

### (f) The running example

The only worked example is the customer-record export (GR-3.4). The Core pages already define its
facts (open decisions, the access rule R-042, the broader background-worker query, the 50k-row load
scenario, the volume rule R-017, a later production incident). Lifecycle pages carry that one story
through the phases: the request at Idea, the open decisions at Specification, rule conformance at
Design, the worker query caught and the load scenario at Develop to QA, deployment and release, and the
volume incident at Operate. The architect states in each brief the facts the page may use from
existing pages, and adds no new rule IDs, numbers or characters except where the brief names them.
The source researcher never proposes examples and never sees the example facts. The sweep checks the
set of examples on every page, so a worked case that matches the library's fails like any other close
passage.

### (g) What the confidentiality reviewer adds

The reviewer cannot see the library, so it cannot find a close paraphrase. It adds checks it can make
cold:

1. **Provenance of structure.** For each list, sequence and table, find it in a cited public source or
   in a page of this site. A list longer, more specific or differently ordered than its source is
   flagged as unattributed structure (GR-2.1, GR-1.2).
2. **Specifics.** Flag any number, threshold, cadence, count, tool, role title or acronym that no
   source or glossary entry supports.
3. **Voice of one organisation.** Flag text that reads as one organisation's practice rather than
   general practice, and combinations across pages that would fingerprint a setup (D-017).
4. **SAFe page.** Check every term against the allow-list and every SAFe-side statement against the
   cited SAFe page.
5. **Sweep status only.** The reviewer is told that the sweep passed and on which page hashes, never
   what it found.

### (h) Budget and the cap

- At most **three sweep rounds per page** (sweep, rewrite, re-sweep, rewrite, re-sweep). These are
  separate from the three review rounds.
- After the third failing round the page goes to the author with three options: cut the failing
  passages without replacement where the template minimum still holds; the author rewrites the
  passage personally; or the box is merged into a neighbouring page.
- If two or more pages of batch A or W1, or four of batch B, or three of W1 and W2 together, reach a
  third round, the work stops and
  the architect re-plans the grain with the author, because repeated failure suggests the page's
  shape follows a library document.
- Sweep runs compare at most four pages each, so the comparison stays thorough.

## Order of work

0. **Plan approved (D-029); plan pull request** (this file, D-029, STATUS; no page text). The page
   work happens on a local branch that is never pushed.
   **Edition 1.5.0**
1. **Briefs** (architect, scratchpad), then the **outline pass** (public skeleton) by the
   external-researcher, the architect fixing the skeleton in each brief, then the library concept
   diff and the evidence briefs, in parallel by batch, starting with batch A.
2. **Batch A written, swept twice, rewritten, re-swept.** Batch B follows, with the briefs tightened
   by the process lessons from A.
3. **Diagrams** (diagrammer), up to five: the levels against the phases, the traceability spine as an
   identifier chain, the Definition of Ready and Done gates along the lifecycle, deploy against
   release, and the SAFe mapping. Each has a text alternative and both themes (GR-4.4). Diagram text is
   swept with the page.
4. **Map and routes**: the relabel (D-015), the new links, `toc.yml` (a `lifecycle` list),
   `release/sections.yml` (`"1.5"`), glossary entries, the routing row, and the Core back-links.
5. **Sweep D1** on final text, ledger check. **The author reads the SAFe reference model page in
   chat.** Then the branch is rebuilt as **one commit on top of `main`** with a neutral message, and
   only then pushed. `check_citations.py`, `check_pages.py` and the other checks run before the push.
6. **Review** in fresh contexts, split by group (concepts and levels; phases) so no reviewer reads 12
   pages at once: three reviewers, three rounds, then the author. The Core back-links go through a
   D-011 confirmation review. A review-round revision is swept on its changed passages before it is
   pushed.
7. **Merge as 1.5.0**, the author reviews it live, follow-ups as 1.5.x, tag `v1.5.x` at approval.
   **Edition 1.6.0** (starts after 1.5.0 is merged; it need not wait for the 1.5 tag)
8. Briefs, outline pass, library concept diff and evidence briefs for the seven workflow pages,
   batch W1 first; write, sweep (W1 twice, then W2), rewrite, re-sweep.
9. **Map and pages:** the seven workflow links move to their pages; the phase pages' workflow lists
   link to them; the Core back-links to the workflow pages; `release/sections.yml` (`"1.6"`).
10. **Sweep D2**, one commit on top of `main`, push, review (three reviewers; confirmation review for
    the edited 1.5.0 pages and Core), merge as 1.6.0, the author reviews it live, tag at approval.

## Links and map changes

All map changes need the author's approval (ASSUMPTIONS A2); none adds a box.

- **Relabel (D-015).** In `build_map.py`: the band note "SAFe levels, phases, ..." becomes "Portfolio,
  train and team levels, phases, ..."; the three level chips read **Portfolio**, **Train**, **Team**
  (the middle chip is "Agile Release Train" today); their subtitles lose SAFe-only words ("epics ·
  WSJF · lean budgets" becomes "initiatives · prioritisation · budgets"; "features · PI planning ·
  system demo" becomes "features · planning cycle · integrated demo"; the Team subtitle is already
  generic); `MAP_DESC` follows. The footer credit line to SAFe stays, since SAFe remains the credited
  source. The **Inspect & Adapt** label and its note change "each PI" to "each planning cycle". Band 4
  labels that use SAFe words (Agile Release Train, PI cadence, system demo) stay until the enablement
  section, and the plan flags the mixed vocabulary meanwhile (open question 6).
- **New links** in `links.yml`: the nine phase labels (the phase boxes are not linked today, so
  `build_map.py` wraps each in `linked()`); the three level labels, to anchors of `lifecycle-levels`;
  the DoR and DoD tags and the traceability spine and Inspect & Adapt labels. Two labels need the
  build to change: "TRACEABILITY SPINE · linked by rule IDs" and "Inspect & Adapt each PI: ..." are one
  text each, and a link needs a label of its own, so each is split into a linked label and a plain note.
  The DoR and DoD tags are 16 px high, below the 24 px minimum target size, so the site-builder gives
  them a larger hit area or moves the link to a label beside them.
- **Moved links (1.6.0 only, D-029).** In 1.5.0 the seven workflow labels keep their links to
  `workflow-catalog.html#W..`. In 1.6.0 they move to the workflow pages. Each workflow page links
  back to its catalog row, and the catalog row stays.
- **Edition split of the map changes.** 1.5.0: the relabel, the nine phase links, the three level
  anchors, the Develop, Build and QA anchors, the DoR and DoD tags, the spine and Inspect & Adapt
  labels. 1.6.0: the seven workflow links only.
- **SAFe reference model: no new box.** It is reached from `lifecycle-levels`, from the section
  navigation and from the glossary entries for the SAFe terms. If the author wants a map entry, that
  is a new box and needs a separate approval.
- **Core back-links** (both ways, as D-018 does; approved for 1.5.0, D-029): Core `workflows`,
  `software-factory`, `harness-engineering` and `evidence-schema` gain links in "Related" and one or
  two sentences that point to the traceability spine, Inspect & Adapt, the levels and the DoR/DoD
  pages in 1.5.0. The links to the pull-request verification and incident feedback workflow pages
  are added in 1.6.0, the same kind of change under the same confirmation review. These edits change
  the hash of published pages, so they go through a confirmation review under D-011.
- **Glossary (about ten new entries):** definition of ready, definition of done, traceability spine,
  inspect and adapt (SAFe), planning interval (SAFe), WSJF (Reinertsen via SAFe), agile release train
  (SAFe), portfolio, train and team levels (this site's generic labels, marked *coined*), deploy
  versus release. Each carries its attribution.
- **Routing row:** "Understand" gains the levels and traceability pages in 1.5.0; "Run a workflow"
  gains the seven workflow pages in 1.6.0.

## Related pages outside the section

| Page | Exists | How it is handled |
|---|---|---|
| The nine Core pages | yes | linked directly |
| Workflow catalog and glossary | yes | linked directly, including `workflow-catalog.html#W01`, `#W04`, `#W08`, `#W12`, `#W23`, `#W25`, `#W26`, `#W28` |
| Adoption stages | no (home-page `#adoption` anchor only) | link to `index.html#adoption` until the adoption section exists |
| Evidence & traceability, Measurement, Standards (assurance) | no | glossary entries and Core pages stand in; no link to a page that does not exist (GR-4.3) |
| People & roles, Operating model, Agent runtime (enablement) | no | same |
| Risk tier, flows (context) | no | glossary entry `risk-tier` and Core `workflows` |

When a later section publishes a page that owns a boundary row, the lifecycle page gains the link in
that section's edition.

## Cost and size

The table below is for the whole section; about two thirds of it falls in 1.5.0 (12 pages, the
SAFe page, the diagrams and the Core confirmation review) and one third in 1.6.0 (7 pages).

| Step | Runs | Rounds |
|---|---|---|
| Briefs (architect, per batch) | 3 to 4 | 1 |
| Outline pass (external, per batch) | 3 to 4 | 1 |
| Library concept diff (source-researcher, 19 pages, grouped) | 8 to 10 | 1 |
| Evidence briefs (external-researcher, one per page) | 19 | 1 |
| Author, first writing | 19 | 1 |
| Author, rewrites after sweeps (fresh contexts) | 10 to 15 | up to 3 per page |
| Diagrammer | 5 | 1 |
| Sweeps (up to 4 pages a run; batch A twice by two contexts) | 20 to 28 | up to 3 per page |
| Site-builder (map, links, glossary, checks, PR) | 3 to 4 | 1 |
| Reviewers (3 reviewers x 3 groups; round 1 all, later rounds the groups still open) | 18 to 24 | up to 3 |
| Confirmation review for Core back-links | 3 | 1 |
| **Total** | **about 110 to 135** | |

That is roughly twice the Core section by page count. The cost grows if the sweep finds close passages
on many pages, which is the main variable. Where the section has the most uncertainty is the number of
rewrite and re-sweep rounds on batch A and the phase pages. The new references number about 100 to 120,
and the author adds them to `content/references.yml` as for Core.

## Risks

- **Confidentiality, the covered boxes.** Eighteen of the 22 boxes are covered, so the library has
  material on nearly every page. Lists of gates, readiness criteria, event sequences and workflow
  checks are the most likely to match. The mitigations are the public skeleton, the early and double
  sweep, the fresh rewriting author and the page-hash ledger.
- **Confidentiality, the thin boxes.** With thin coverage, the library's few passages would become the
  only non-public structure on Deploy, Operate and deploy verification. The restricted library pass
  (confirmations only) and public-first skeletons address this.
- **Confidentiality, the SAFe reference model.** The mapping is the page's value and the place where a
  recognisable organisation-specific model could show. The allow-list, the SAFe-only skeleton, the
  double sweep and the author's pre-push read address this; the residual risk is that a mapping that
  is natural to one organisation is also natural to the public SAFe text, so the sweep may pass what
  only the author can recognise. Hence the author's check.
- **Weak public evidence.** Portfolio, Deploy, Operate and deploy verification, and the effect of
  agents on any phase, have little public research. Pages say so and present recommended practice
  (GR-2.3). A claim about agents in a phase cites DORA's AI research or is labelled.
- **Inconsistency between map, catalog and pages.** The map has nine phases; the catalog has eight
  with different names. The catalog's W12 decision says "definition of ready", while the map sets the
  DoR tag at Specification and the adoption path ties DoR to spec readiness. The DoR page resolves this
  as two layers (specification, then task); the plan makes no catalog change (open question 8).
- **Mixed vocabulary on the map.** Band 2 turns generic while band 4 keeps SAFe words until the
  enablement section.
- **Overlap with later bands.** Inspect & Adapt, roles, metrics and templates each have a box in a
  later band. The boundary table assigns each; reviewers check for restatement (GR-4.2 stays satisfied
  by a one-sentence definition, not by repetition).
- **Size.** 12 pages in the first review and 7 in the second (D-029), split by group, and each
  edition can be released only when all its pages are accepted (D-014).
- **Edits to published pages in 1.6.0.** 1.6.0 changes phase pages, the map and Core pages that
  1.5.0 published, possibly before the 1.5 tag exists. Each such change is swept and goes through a
  confirmation review, so the author's live review of 1.5.0 is not invalidated silently.
- **Rule text.** GR-6.1 describes a section as one band and one approval. D-029 is an exception by
  the author's decision, and `GROUND-RULES.md` is not edited; the author decides whether to amend
  GR-6.1 (see D-029).
- **Anchor links.** The level, phase and DoR/DoD map links point to heading anchors; a changed heading
  slug breaks them (GR-4.3). The link check catches this at build time.

## Open questions (as put to the author; answers follow)

1. **Does the D-015 relabel ship inside this edition, or as its own edition first?** STATUS "Next"
   item 5 and the Core plan say a content edition of its own. **Recommendation: inside 1.5.0.** The
   relabel cites SAFe as one framework and promises a worked model; it has no link target until the
   levels and SAFe pages exist; it contains no library material, so it adds no sweep work; and a
   separate edition costs a full three-reviewer review for a four-label change. If the author prefers
   the earlier plan, the relabel becomes 1.5.0 and the lifecycle section 1.6.0, and nothing else in this
   plan changes.
2. **Do the seven workflow boxes get one page each?** **Recommendation: yes.** The catalog stays the list; a
   page adds inputs, guardrails, failure paths, measures, owner and the worked example. Fallback if
   the author wants a smaller section: five pages (pull-request verification, spec readiness, release
   readiness, incident feedback and deploy verification), with intake & triage and design conformance
   left as catalog rows. That leaves two map labels linked to the catalog, the rest to pages, and the
   section at 17 pages.
3. **How do the Phase pages relate to the catalog's traditional-to-AI columns?** **Recommendation:**
   each phase page's "Traditional practice" is short prose built from public standards (ISO/IEC/IEEE
   12207 and 29148, ISTQB, NIST SSDF, the SRE book) and does not copy catalog rows; its "Workflows in
   this phase" lists each decision once and links to the workflow page and the catalog row; the
   catalog keeps the full traditional-to-AI table. The catalog's phase names differ from the map's,
   and each phase page states which catalog phase holds its workflows. No catalog change is made.
4. **Does the SAFe reference model page need a word-for-word list of what it may and may not
   name?** **Recommendation: yes for what it may name, by category for what it may not.** The brief
   carries a closed allow-list of the public SAFe nouns the page may use (levels, events, roles,
   artefacts, WSJF, lean budgets and the like), each tied to a SAFe page. What it may not name is
   given by category: no cadence or count not published by SAFe, no tooling, no organisation
   structure, no account of how any organisation applies SAFe. A plain list of forbidden names would
   itself reveal what it protects (GR-1.4), so names stay with the hashed deny-list. The author also
   reads the page on the local file **before the first push**, rather than only before release
   (D-015 says before release; this is an earlier gate).
5. **Is one page for Develop, Build and QA, and one page for the three levels, acceptable?**
   **Recommendation: yes** (reasons above). Alternatives: Develop and Build on one page and QA
   alone (20 pages), or three phase pages (21).
6. **Map changes.** Are the changes under "Links and map changes" approved: linking the nine phase
   labels, the DoR and DoD tags, the spine and Inspect & Adapt, splitting two labels, and no new box
   for the SAFe page? **Recommendation: yes.** Also: should band 4's SAFe words stay until the
   enablement section? **Recommendation: yes.**
7. **May Core pages gain back-links in this edition**, with a D-011 confirmation review?
   **Recommendation: yes**, limited to "Related" and one or two sentences. The Core section is still
   awaiting live review and its tag; if the author would rather not touch Core before tagging it, the
   back-links wait for 1.5.x.
8. **DoR in the catalog.** The W12 row reads "definition of ready", and the map and adoption path
   place it at Specification. **Recommendation: no catalog change.** The DoR page presents two layers
   (specification readiness, task readiness) so both statements hold.

## Decisions taken by the author (D-029)

Approved 2026-10-06 with one change: Lifecycle ships as two editions, each deployed, reviewed live
and tagged separately.

1. The D-015 relabel ships inside 1.5.0. `STATUS.md` and the Core plan are updated to match.
2. All seven workflow pages are written, in 1.6.0. Each must add failure paths, evidence and
   measures beyond its catalog row.
3. Phase pages carry short prose from public standards and do not copy catalog rows (agreed).
4. The SAFe reference model page has a closed allow-list of what it may name; what it may not name is
   described by category only. The author reads the page text in chat before its first push.
5. One page for Develop, Build and QA and one for the three levels, with an anchor per map box.
6. The map changes are approved; the workflow links move to their pages in 1.6.0. Band 4's SAFe
   words stay until the enablement section.
7. Core pages gain back-links in 1.5.0, with a D-011 confirmation review.
8. No catalog change for the W12 wording; "catalog consistency pass (W12 wording)" is on the backlog
   in `STATUS.md`.
