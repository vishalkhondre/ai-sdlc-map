# Section plan: Enablement (band 4)

Proposed by the architect, 2026-11-28. **Awaiting the author's approval (GR-6.1, D-014).** No page
is written before it. Open questions for the author, each with a recommendation, are numbered at the
end.

- **Section:** enablement, band 4 of the map ("what makes it possible"), the second section of wave 2
  ("Assurance and enablement"), after Assurance (D-033).
- **Edition:** 1.8.0 when the section merges, following Assurance as 1.7.0; follow-ups before
  approval are 1.8.x; the tag is created at approval (D-016). Fix editions that land in between
  (1.6.2 and later) are patches and do not change this number. `release/sections.yml` gains a `"1.8"`
  entry. **One edition, one approval** (GR-6.1); at 14 pages it is larger than Lifecycle 1.5.0 (12),
  so open question 3 offers a smaller fallback and a two-edition split, and recommends neither.
- **Boxes:** all 21 band-4 boxes in `project/COVERAGE.md`: 13 covered, 8 thin, none rated none. The
  assurance plan covers no band-4 box: it owns the *review* of agent permissions and reviewer load *as a
  measure* (band 5); Enablement owns the runtime mechanism and the people side of the same topics.
  One band-4 box, Inspect & Adapt, already has a page (Lifecycle `inspect-and-adapt`) and gets none here.
- **Sources:** every page cites public sources (GR-2). The library informs practice only (GR-1.2), and
  each page's structure is built from public sources and the site's own pages first, using the
  procedure of `assurance.md` ("Library check built in from the start"), with the differences below.
  Borrowed terms keep their credit (GR-2.2): Model Context Protocol (its specification), product owner
  (Scrum Guide), platform team (Skelton and Pais, *Team Topologies*), the SAFe terms (Scaled Agile,
  Inc.), the test terms (ISTQB glossary), automation bias and complacency (Parasuraman and Manzey),
  least privilege (NIST SP 800-53 AC-6), separation of duties (AC-5).
- **The section links, it does not restate (D-030).** Enablement sits beside Core (`adapters`,
  `skills-and-evals`, `harness-engineering`, `workflows`), Lifecycle (`lifecycle-levels`,
  `inspect-and-adapt`, `safe-reference-model`, the phase pages' named roles) and Assurance
  (`agent-permissions`, `reviewer-load`, `ai-use-policy`, `change-controls-and-standards`). An
  Enablement page states what the tool, role or operating practice *is and does*, and links for
  anything those pages or a catalog row already say.

## Why this band is harder than Assurance

Three risks are higher here than in any earlier section, and the plan is shaped by them.

1. **Organisation shape (GR-1.1, D-017).** The covered boxes are role splits, decision rights, a
   train-based operating model and work tracking: the shapes most likely to carry one organisation's
   structure. A role split, approval chain, cadence or team size that no public source gives is a
   fingerprint even when every word is general. Every such list on a page must come from a public
   source (Scrum Guide, SAFe, *Team Topologies*, NIST) or from the map itself.
2. **Tool combinations (GR-3.3, D-017).** D-017 notes that public products whose risk lies only in
   combination cannot be listed in the deny-list. Naming a set of coding agents, model providers, a
   protocol server, a tracker and a knowledge base together could describe one organisation's stack.
   The plan therefore names **no product** in any Enablement page body (open question 4).
3. **Weak public evidence on agents' effect on people.** Little peer-reviewed research describes how
   roles shift with coding agents. Pages present the shift as recommended practice unless a source (DORA's
   AI research, published human-factors research) states it (GR-2.3).

**No fixed enforcement classes (D-034, recorded in the fix edition: rule enforcement is described per
rule, with no fixed set of named enforcement classes).** No page presents a fixed set of permission tiers, approval classes or
enforcement levels as the site's scheme. Pages describe the mechanism (an organisation decides which
actions need which approval, and records it in the registry) and cite a public scheme only as one
example of a category. Core's published report-only and required states are linked, not extended.

## Boundary with the other sections

| Topic | Enablement (this section) | Other section |
|---|---|---|
| Agent permissions | how the runtime grants a scope to an agent identity and a tool; sandbox boundaries; how secrets reach a run without entering the context | Assurance `agent-permissions`: grant, review, revoke as privileged access, and its evidence |
| Review load | automation bias, complacency and deskilling in review, in the human-factors research's own terms | Assurance `reviewer-load`: the measure, its formula and unit |
| Model providers | the category: hosted or self-hosted, what to evaluate, how the runtime binds to a provider | Assurance `ai-use-policy` (data and IP policy), `cost-per-change` (cost) |
| SDD frameworks | the category: what such a framework supplies and where it meets the kit | Glossary `spec-driven-development`; Lifecycle `specification`; Assurance `delivery-templates` |
| CI runner and change host | the tools as the place where enforcement happens: isolated runs, required checks, protected branches | Core `adapters`: the kit's binding layer and its tests |
| Roles | each role as its own public sources describe it (Scrum Guide accountabilities, ISTQB test roles, architecture-role literature, published developer research), and a change with agents only where a source states it | Lifecycle phase pages (the roles each phase names); Core `workflows` (the people a workflow involves) |
| Platform team | the team type and its interaction modes, after *Team Topologies*; platform as a product | Core `engineering-kit` (what the kit holds); catalog W34 (kit upgrade) |
| Cadence and review events | sprints, planning intervals, the sprint review and the system demo as the Scrum Guide, SAFe and the Kanban Guide publish them | Lifecycle `lifecycle-levels`, `inspect-and-adapt`, `safe-reference-model` |
| Work tracking and knowledge base | the category and what an agent needs to read from it | Lifecycle `traceability-spine` (identifiers); Core `rule-registry` |
| Separation of duties and change approval | what separation-of-duties and change-approval controls ask, in their own terms (NIST SP 800-53 AC-5, CM-3, CM-5; ISO/IEC 27001 Annex A only as far as readable) | Assurance `change-controls-and-standards` (a control mapped to rules, checks and records, including agent-authored changes) |
| Risk tier | used, not defined | Context `risk-tier` (glossary `risk-tier` until 1.9.0) |

## Pages

| # | Page id | Type | Map box (bullet) | Coverage | Scope | Leaves to others |
|---|---|---|---|---|---|---|
| 1 | `coding-agents-and-models` | Concept | Coding agents and agentic IDEs; model providers (two anchors) | thin, thin | The category: what a coding agent does (reads, plans, edits, runs tools) and where it runs (editor, terminal, hosted); what a model provider supplies; what to evaluate before adopting either, as questions; how the harness, not the tool, holds the rules. No product named. | Data and IP policy (Assurance); cost (Assurance) |
| 2 | `tool-access-and-isolation` | Concept | Tool access (MCP), sandboxes, permissions, secrets (four anchors) | covered, thin, covered, thin | How an agent reaches tools (MCP as the open protocol the map names) and what bounds it: sandboxed execution, scoped permissions per identity and tool, secrets injected at run time and kept out of model context; excessive agency as the risk. | Permission review (Assurance `agent-permissions`) |
| 3 | `sdd-frameworks` | Concept | Spec-driven development (SDD) frameworks | covered | The category: what such frameworks supply (a sequence from intent to tasks, templates, agent instructions); how they meet the rule registry, the templates and the readiness workflow; staying neutral on which supplies it (glossary). | The sequence itself (glossary, Lifecycle `specification`); templates (Assurance) |
| 4 | `ci-runner-and-change-host` | Concept | CI runner and change host, bound by thin adapters | thin | The two tools where enforcement actually happens: isolated, reproducible runs; required checks and protected branches on the change host; why enforcement must be verified, not assumed; the thin-adapter boundary. | The adapter layer (Core `adapters`) |
| 5 | `product-owner-and-manager` | Concept | PO / PM own intent and open decisions | covered | The product owner as the Scrum Guide (2020) states the accountability (the Product Goal, Product Backlog items and their ordering, transparency of the backlog); product management as product-management literature and SAFe's published role describe it, credited; how the two differ and where they meet. | The specification phase (Lifecycle `specification`) |
| 6 | `architect-role` | Concept | Architects own rules (after the split) | covered | Architecture work as published architecture-role literature describes it: significant decisions and their records (Nygard's ADRs), architectural fitness functions (Ford, Parsons and Kua, *Building Evolutionary Architectures*), recognised-practitioner writing on the architect's role (martinfowler.com, Hohpe); how a recorded decision can become a checkable rule is linked, not restated. | Rule entries (Core `rule-registry`); design conformance (Lifecycle) |
| 7 | `qa-role` | Concept | QA owns scenarios and evals (after the split) | covered | Testing roles as ISTQB describes them (test manager and tester; test analysis, design and the test basis), the whole-team approach to quality (ISTQB Agile Tester syllabus; Crispin and Gregory, *Agile Testing*), and the test oracle problem (Barr et al., IEEE TSE) as the public frame for judging output whose correct result is hard to state. | Evaluation sets for skills (Core `skills-and-evals`); `independent-basis` (glossary) |
| 8 | `engineer-role` | Concept | Engineers direct, verify, turn lessons into gates | covered | The Developers accountability as the Scrum Guide states it (the Sprint Backlog, quality through the Definition of Done, adapting daily); what published research on developers working with AI assistants reports, as findings only where a study states them (DORA's AI research; peer-reviewed studies on readable hosts). | Workflow steps (Core `workflows`, catalog rows) |
| 9 | `platform-team` | Concept | Platform team owns the kit | thin | The platform team as *Team Topologies* defines it (a team type whose purpose is to reduce stream-aligned teams' cognitive load; its interaction modes); platform as a product (CNCF platforms white paper); DORA's platform engineering findings; the kit as such a team's product. | The kit itself (Core `engineering-kit`); kit upgrade (catalog W34) |
| 10 | `automation-bias-and-deskilling` | Concept | Watch: review load, skill erosion, adoption | covered | Two effects named by human-factors research, in that research's terms: automation complacency and automation bias (Parasuraman and Manzey, *Human Factors*, 2010) and the loss of manual skill under automation (Bainbridge, "Ironies of Automation", 1983; studies of manual skill retention in automated cockpits); what published code-review research says about review effort (for example Bacchelli and Bird, ICSE 2013). No fixed list of warning signs; findings only where a study states them. | The measure (Assurance `reviewer-load`); adoption (adoption path) |
| 11 | `scrum-and-kanban-teams` | Concept | Scrum / Kanban teams on an Agile Release Train | covered | The team-level frameworks as their guides define them (Scrum Guide: accountabilities, events, artefacts; Kanban Guide: defining and visualising the workflow, actively managing items, improving flow); teams of teams as SAFe describes the train, credited; where agent-run workflows meet the board or backlog. | Lifecycle levels (Lifecycle `lifecycle-levels`) |
| 12 | `cadence-and-demo` | Concept | PI cadence, system demo, Inspect & Adapt | covered, thin | Cadence and synchronisation as SAFe publishes them; the sprint and sprint review as the Scrum Guide states them; SAFe's system demo, credited; how Kanban treats cadence (Kanban Guide); Inspect & Adapt linked to its Lifecycle page. | Inspect & Adapt (Lifecycle `inspect-and-adapt`) |
| 13 | `work-tracking-and-knowledge-base` | Concept | Work tracking & knowledge base | covered | The category, from public sources: visualising and managing work (Kanban Guide), the Product Backlog as a transparent artefact (Scrum Guide), documentation practice (the documentation chapter of *Software Engineering at Google*; docs-as-code writing); what an agent reads from either as context, linked to Core `harness-engineering`. | Identifiers and the artefact chain (Lifecycle `traceability-spine`) |
| 14 | `separation-of-duties-and-approval` | Concept | Decision rights and approvals; policy wins | covered | What the public controls emphasise: conflicting duties identified and separated, the separation documented, and access authorisations defined to support it (NIST SP 800-53 AC-5; ISO/IEC 27001 Annex A segregation of duties, as far as readable); restricting who can make changes (CM-5); changes approved and recorded by designated roles (CM-3). The page follows those controls' own emphasis and adds no list of its own. | Agent-authored changes under change control (Assurance `change-controls-and-standards`); permission review (Assurance `agent-permissions`) |

**Page types and anchors.** All 14 pages use the Concept template. The Role or practice template
(Purpose, Responsibilities, What shifts with agents, Warning signs) is not used for the people pages:
applied to five roles it would give every role page one shared shape that no public source gives. Each
role page takes its sub-headings inside "How it works" from its own sources (open question 7). Every map
box that shares a page has its own anchor (D-029).

### What was merged, what was kept apart, and why

- **Tool access, sandboxes, permissions and secrets: one page.** One bullet; one question ("what can the
  agent reach, and what stops it"); two of four boxes thin. Splitting would make two thin pages and a
  bullet split.
- **Coding agents and model providers: one page.** One bullet; both thin; both category pages whose
  value is the evaluation questions, which overlap.
- **Architects and QA: two pages.** One bullet, but two roles with different public sources and
  different Core pages to link; the bullet is split on the map.
- **Review load and skill erosion: one page,** because the research it rests on treats complacency
  under automation and the loss of manual skill as effects of the same automation (Bainbridge;
  Parasuraman and Manzey). "Adoption" in the bullet is the adoption path's subject and links there.
- **PO and PM: one page;** one bullet, and the page's value is setting the two descriptions side by side.
- **PI cadence and system demo: one page;** Inspect & Adapt keeps its Lifecycle page.
- **No hub pages for the three column titles.** They head unrelated items; the titles stay plain labels.

### Pages that rely on public sources only

| Page | Why | How it is shaped |
|---|---|---|
| `coding-agents-and-models` | thin, thin | DORA's AI-assisted development research, NIST AI 600-1 (third-party generative AI), published agent-benchmark papers (for what agents are evaluated on, not for scores), recognised-practitioner writing on coding agents (martinfowler.com, Technology Radar). Restricted library pass. |
| `tool-access-and-isolation` (sandboxes, secrets parts) | thin | MCP specification and its security guidance; OWASP on excessive agency and secrets management; NIST SP 800-53 AC-3, AC-6, SC-39 (process isolation), IA-5; NIST SP 800-190 (containers). |
| `ci-runner-and-change-host` | thin | SLSA build and source requirements (isolated builds, protected branches, review), NIST SSDF PO.5 (secure environments), DORA continuous integration capability. |
| `platform-team` | thin | *Team Topologies* (publisher's and authors' public material), the CNCF platforms white paper, DORA's platform engineering findings. |
| `cadence-and-demo` (demo part) | thin | SAFe's public system demo page, credited; the Scrum Guide's sprint review. |
| `automation-bias-and-deskilling` | covered, weak public evidence | Human-factors research on automation and skill (Bainbridge, "Ironies of Automation"; Parasuraman and Manzey on complacency and bias), published code-review studies on readable hosts, DORA's AI research. Restricted pass, as for Assurance's `reviewer-load`. |

## Source access

Same rule as `assurance.md`: a source a session cannot read is a gap, never a claim by memory.

| Source | Status | Handling |
|---|---|---|
| MCP specification | official protocol specification; host not known to be on the allow-list | Request the host (open question 12); until readable, the page says only what the map and a readable secondary source of the specification state |
| OWASP generative AI project (LLM Top 10, agentic guidance) | `genai.owasp.org` not on the allow-list | Use `cheatsheetseries.owasp.org` where it covers the claim |
| *Team Topologies*, Reinertsen, Bainbridge | books and journal text | cite only what a readable page shows (publisher or authors' site, an open copy); otherwise author to confirm |
| SAFe roles and events | public glossary and article pages | follow SAFe's wording, credited; say less where it is silent |
| Kanban Guide, Scrum Guide | public | cite directly |

## Library check

The procedure of `assurance.md` (a) to (g) applies unchanged: briefs from the map and the published
pages only; the public skeleton (outline pass) before any library pass; a concept diff keyed to skeleton
items; the **restricted pass** (confirmations and contradictions only) for the eight thin boxes and for
`automation-bias-and-deskilling`; fresh authors for every rewrite; the sweep ledger; three rounds, then
the author; nothing pushed before sweep E is clean. Differences:

- **No shared skeleton across the people pages.** The outline pass builds each role page from the
  sources named for it in the page table; no heading set is reused from one role page to another, and
  the confidentiality and editorial reviewers flag two people pages with matching structure.
- **Control lists come from the control text.** On `separation-of-duties-and-approval`, every item
  traces to the NIST control text or the ISO Annex A wording as read; nothing is added to it.
- **Five sweep batches,** not four: 14 pages at four a run, then the final run E.
- **No cadence, count or duration** (iteration length, planning-cycle length, team size, review
  deadline) unless SAFe, the Scrum Guide or another cited source publishes it.

| Batch | Pages | Why this order | Sweeps |
|---|---|---|---|
| A | `separation-of-duties-and-approval`, `product-owner-and-manager`, `architect-role`, `qa-role` | covered role and approval boxes: highest fingerprint and closeness risk | two independent runs even when the first is clean, re-sweep after every rewrite |
| B | `engineer-role`, `automation-bias-and-deskilling`, `scrum-and-kanban-teams`, `cadence-and-demo` | covered people and operating-model boxes; the second sits next to the glossary entry `review-fatigue` (on the close list) | two runs for `automation-bias-and-deskilling`, one for the rest |
| C | `work-tracking-and-knowledge-base`, `sdd-frameworks`, `tool-access-and-isolation`, `platform-team` | covered tool boxes and one thin role | one run, re-sweep after any rewrite |
| D | `coding-agents-and-models`, `ci-runner-and-change-host` | thin, restricted pass, public-only structure | one run |
| E | all 14 on final text, with map text, diagram text, glossary entries and every changed passage of a Core, Lifecycle or Assurance page | cross-page edits and back-links | one run, hash-checked |

If two batch-A pages reach a third round, work stops and the architect re-plans the grain with the
author (as in `assurance.md` (e)).

**Running example (GR-3.4).** Facts from published pages only. `tool-access-and-isolation` may use
the export's background worker and its broader query to show a scope that is wider than the task
needs; `product-owner-and-manager` may use the export's open decisions as published pages state them.
No new fact about the export is introduced, and no figure. The architect lists allowed facts per brief.

## Map and link changes

All need the author's approval (ASSUMPTIONS A2); none adds a box.

- **Band 4 bullets become links,** using the bullet linking built for Assurance 1.7.0; the test that
  kept band 4 unlinked is turned round to check that every band 4 bullet is linked. **One bullet
  split,** as Assurance split a measurement bullet: "Architects own rules; QA owns scenarios and evals"
  becomes "Architects own rules" and "QA owns scenarios and evals". The People column then has six
  bullets; the band height grows by one line if needed. If the relabel in open question 13 is approved,
  the split applies to the new labels.
- **Band 4 relabels (open question 13).** The role bullets, the "policy wins" bullet and the band note
  are relabelled in this edition if the author approves, with the matching sentence of `MAP_DESC`.
- **SAFe relabel, deferred to this section by D-029.** "Scrum / Kanban teams on an Agile Release Train"
  becomes "Scrum / Kanban teams on a train"; "PI cadence, system demo, Inspect & Adapt" becomes
  "Planning-cycle cadence, integrated demo, Inspect & Adapt", matching the band 2 wording ("planning
  cycle", "integrated demo"). `MAP_DESC` drops "(PI is a planning interval)". The footer credit line
  keeps SAFe for Inspect & Adapt and drops "Agile Release Train (ART), System Demo" if no map label
  still uses them; the glossary entries for those SAFe terms stay.
- **New `links.yml` entries (13 bullets after the split):** each bullet to its page; the shared
  bullets to the page, not an anchor (anchors are reached from the page's contents).
- **Routing row:** "Lead adoption" gains `separation-of-duties-and-approval` and `product-owner-and-manager`;
  "Build the kit" gains `tool-access-and-isolation` and `ci-runner-and-change-host`.
- **Back-links** (both ways, D-018, D-029), each under a D-011 confirmation review and a sweep of the
  changed passage: Core `adapters` (runner and host page), `harness-engineering` (tool access),
  `rule-registry` (architect role), `skills-and-evals` (QA role, skill erosion), `engineering-kit`
  (platform team); Lifecycle `lifecycle-levels` (teams, cadence), `inspect-and-adapt` (cadence page),
  `specification` (SDD frameworks, PO/PM); Assurance `agent-permissions`, `reviewer-load`,
  `ai-use-policy`, `change-controls-and-standards`. Pages with passages on a close or borderline list
  gain a link in "Related" only. **`safe-reference-model` is not edited** (open question 6).

## Glossary candidates

About ten, each attributed (GR-2.2), each with the page that uses it (D-025): coding agent (common),
Model Context Protocol (its specification), sandbox (common), secret (common; NIST glossary), excessive
agency (OWASP), product owner (Scrum Guide), platform team (*Team Topologies*), separation of duties
(NIST SP 800-53 AC-5), automation bias and automation complacency (Parasuraman and Manzey), test
oracle (ISTQB glossary), knowledge base (common). Existing entries used:
`spec-driven-development`, `skill-erosion`, `adapter`, `rule-registry`, `independent-basis`,
`agile-release-train`, `planning-interval`, `system-demo`, `inspect-and-adapt`, `export-example`.
**`review-fatigue` is not used** until the fix edition has rewritten it.

## Diagrams

Up to two, each with a text alternative and both themes (GR-4.4), swept with the page:

1. `tool-access-and-isolation`: an agent run inside its sandbox boundary, the tools it reaches through
   the protocol, and the scoped credential injected at run time, marking what crosses the boundary and
   what does not. Built from the MCP specification and NIST SP 800-53 SC-39; no product shown.
2. `platform-team`: the platform team and stream-aligned teams with the interaction modes between them,
   after Skelton and Pais (*Team Topologies*), with a credit line (D-009).

## Related pages outside the section

| Page | Exists | Handling |
|---|---|---|
| Core, Lifecycle pages | yes | linked; back-links as above |
| Assurance pages | after 1.7.0 merges | linked; if 1.8.0 is written first, glossary entries stand in |
| Workflow catalog | yes | rows W32, W33, W34 (kit upgrade) linked, never restated (D-030) |
| Context pages (risk tier) | no | glossary `risk-tier` |
| Adoption stages | no | `index.html#adoption` |

## Order of work

0. Plan approved; plan pull request (this file; no page text).
1. Briefs (architect, scratchpad), outline pass, concept diffs and evidence briefs, batch by batch.
2. Batches A to D written and swept; rewrites by fresh authors.
3. Diagrams (up to two).
4. Map: bullet links, the split, the relabel, `links.yml`, `toc.yml` (`enablement` list),
   `release/sections.yml` (`"1.8"`), glossary, routing row, back-links.
5. Sweep E, ledger check, one commit on top of `main`, checks, push.
6. Review in three groups (runtime 1 to 4; people 5 to 10; operating model 11 to 14), three reviewers,
   three rounds, then the author; D-011 confirmation review for back-links.
7. Merge as 1.8.0; the author reviews live; follow-ups as 1.8.x; tag at approval.

## Cost and size

About 85 to 100 agent runs: 14 evidence briefs and first writings, 6 to 10 fresh rewrites, 14 to 20
sweep runs (batch A twice), 18 to 27 reviewer runs in three groups, 3 confirmation reviews, plus briefs,
outline passes and site-builder runs. About 45 to 60 new references. The main variable is the number of
sweep rounds on batch A.

## Risks

- **Fingerprinting by role split, approval chain or cadence** (GR-1.1, D-017). Mitigation: list
  provenance from public sources, no unsourced counts, batch A double sweep, confidentiality reviewer's
  cold checks for combinations across pages (a role split on one page plus a cadence on another).
- **Tool-stack fingerprint** (GR-1.1, GR-3.3). Mitigation: no product names in page bodies.
- **Closeness on covered people boxes** (GR-1.2). Mitigation as above; role pages kept short where the
  template minimum holds.
- **One shape for every role page** (GR-1.2). Role pages take their structure from their own sources,
  not from a shared template; reviewers flag matching structures (open question 7).
- **Restating neighbours** (D-030): `automation-bias-and-deskilling` against Assurance `reviewer-load`
  and the close glossary entry; role pages against Core `workflows` (three roles, on the close list);
  `ci-runner-and-change-host` against Core `adapters`. Links, not restatement; the editorial reviewer
  checks.
- **Fixed enforcement classes** (D-034). No permission tiers or approval levels presented as the
  site's scheme.
- **Weak evidence on agents and people** (GR-2.3). Recommended-practice labels; no claim about how
  roles shift without a source.
- **Dependency on 1.7.0 and the fix editions.** Enablement links Assurance pages and Core passages on
  the close lists; it is written after 1.7.0 merges and after the fix edition that rewrites
  `review-fatigue` and the Core `workflows` passages.
- **Map change.** The relabel touches the footer credit line and `MAP_DESC`; the site tests check every
  `links.yml` label is on the map.

## Open questions for the author

1. **Order and edition.** Enablement after Assurance, as 1.8.0? **Recommendation: yes;** briefs and the
   public skeleton can start while 1.7.0 is in review.
2. **Pages and merges.** Are the 14 pages and their merges approved? **Recommendation: yes.** Fallback,
   12 pages: `scrum-and-kanban-teams` and `cadence-and-demo` merge into one operating-practice page, and
   `ci-runner-and-change-host` becomes a fifth anchor of `tool-access-and-isolation`.
3. **One edition or two?** **Recommendation: one edition (GR-6.1 as written),** reviewed in three
   groups. Alternative: a D-029-style split (runtime and operating model as 1.8.0, people as 1.9.0),
   which moves every later number by one.
4. **Product names.** **Recommendation: no product named in any Enablement page body,** category pages
   included; MCP named as the open protocol on the map; products appear only as the credited source of a
   cited term (D-025), as the map's footer credit for spec-driven development does today. Reason: GR-3.3 and the combination risk D-017 describes.
   Alternative: up to three examples from different vendors on `coding-agents-and-models` and
   `sdd-frameworks` only, each from official documentation, with the product-name list updated.
5. **Map changes.** Linking band 4's bullets, splitting the architects/QA bullet, the SAFe relabel of
   two bullets with the matching `MAP_DESC` and credit-line edits, column titles left plain?
   **Recommendation: yes.**
6. **SAFe reference model page.** Leave it unedited and link to it one way? **Recommendation: yes;**
   any edit to it re-opens the author's pre-push read (D-029), for no reader gain.
7. **Page type for the people pages.** Use Concept for all five role pages and the human-factors page,
   each taking its sub-headings inside "How it works" from its own sources, rather than the Role or
   practice template? **Recommendation: yes;** that template's fixed sections would give every role
   page the same owns / shifts / warning-signs shape, which no public source gives and which the
   library check found close (GR-1.2). The template stays available for practice pages elsewhere.
8. **Inspect & Adapt in band 4.** No new page; the cadence page links the Lifecycle page?
   **Recommendation: yes.**
9. **CI runner and change host.** Its own page rather than linking the bullet to Core `adapters`?
   **Recommendation: own page;** the Core plan's boundary gave the tools themselves to Enablement
   (D-018), and editing a released Core page to hold them costs a confirmation review on the busiest
   page of the close list.
10. **D-034.** D-034 is recorded in the fix edition (rule enforcement described per rule, no fixed
    set of named enforcement classes). The plan applies it as stated above: no permission tiers,
    approval classes or enforcement levels as the site's scheme. **Recommendation: confirm.**
11. **Running example.** Only facts already published, no new fact or figure? **Recommendation: yes.**
12. **Allow-list.** Add the MCP specification host, `genai.owasp.org`, the Kanban Guide host, the
    CNCF platforms white paper host, the *Team Topologies* authors' site and the ISTQB syllabus host?
    **Recommendation: add them;** none is required for the section to be complete.
13. **Band 4 relabels (GR-1.2).** Several band 4 labels state a role or authority claim that the
    library check found close and no public source gives. Relabel, in this edition: "PO / PM own intent
    and open decisions" to "Product owner and product manager"; "Architects own rules; QA owns
    scenarios and evals" to two bullets, "Architects" and "Testers and QA"; "Engineers direct, verify,
    turn lessons into gates" to "Engineers"; "Platform team owns the kit" to "Platform team"; "Watch:
    review load, skill erosion, adoption" to "Automation bias and deskilling in review"; "Decision
    rights and approvals; policy wins" to "Separation of duties and change approval"; and the band
    note "The kit enforces policy; it never holds authority" to "Tools, people and the operating model
    that agent-assisted delivery relies on", with `MAP_DESC` to match. **Recommendation: yes;** role
    names alone let each page say what its sources say. If declined, the current labels stay as link
    text and the pages do not adopt the labels' claims.
