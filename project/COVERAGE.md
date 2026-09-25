# Source coverage by map box

How well the author's private source library (ASSUMPTIONS A3) covers each box on the map, from
the wave 0 inventory of 2026-09-25. The inventory itself names internal documents, so it stays
outside the repository (GR-1.3, D-005); this table records only the result. The architect uses it
to plan sections: a box rated **thin** or **none** relies on public sources and on recommended
practice (GR-2.3, A4) rather than on library experience.

**Key:** covered = at least one library document treats the box in depth · thin = mentions or
partial treatment only · none = nothing found.

Totals: 55 covered, 31 thin, 1 none (87 boxes).

| Band | Box | Coverage |
|---|---|---|
| 1 Context | Greenfield | thin |
| 1 Context | Brownfield + pre-flight analysis | covered |
| 1 Context | Modernisation / migration | thin |
| 1 Context | Web / cloud app | covered |
| 1 Context | Firmware / device (HIL, OTA) | thin |
| 1 Context | Data & ML models (drift) | none |
| 1 Context | Platform / shared lib | thin |
| 1 Context | Flow: Full feature | covered |
| 1 Context | Flow: Bug fix | thin |
| 1 Context | Flow: Hotfix | thin |
| 1 Context | Flow: Trivial / config | thin |
| 1 Context | Flow: Spike / research | thin |
| 1 Context | Flow: Refactor / tech debt | thin |
| 1 Context | Flow: Dependency / CVE fix | thin |
| 1 Context | Flow: Migration · rollback | thin |
| 1 Context | Risk tier | covered |
| 2 Lifecycle | Portfolio (epics, WSJF, lean budgets) | thin |
| 2 Lifecycle | Agile Release Train (features, PI planning, system demo) | covered |
| 2 Lifecycle | Team (stories, iterations, DoR/DoD) | covered |
| 2 Lifecycle | Idea | covered |
| 2 Lifecycle | Specification | covered |
| 2 Lifecycle | Design | covered |
| 2 Lifecycle | Develop | covered |
| 2 Lifecycle | Build | covered |
| 2 Lifecycle | QA (security, performance) | covered |
| 2 Lifecycle | Deploy | thin |
| 2 Lifecycle | Release | covered |
| 2 Lifecycle | Operate | thin |
| 2 Lifecycle | WF: intake & triage | covered |
| 2 Lifecycle | WF: spec readiness | covered |
| 2 Lifecycle | WF: design conformance | covered |
| 2 Lifecycle | WF: pull-request verification | covered |
| 2 Lifecycle | WF: deploy verification | thin |
| 2 Lifecycle | WF: release readiness | covered |
| 2 Lifecycle | WF: incident feedback | covered |
| 2 Lifecycle | Definition of Ready / Done | covered |
| 2 Lifecycle | Traceability spine | covered |
| 2 Lifecycle | Inspect & Adapt | covered |
| 3 Core | Harness engineering | covered |
| 3 Core | Kit: rule registry | covered |
| 3 Core | Kit: validators | covered |
| 3 Core | Kit: skills with evals | covered |
| 3 Core | Kit: evidence schema | covered |
| 3 Core | Kit: adapters | thin |
| 3 Core | Workflows | covered |
| 3 Core | Software factory | thin |
| 4 Enablement | Coding agents / agentic IDEs | thin |
| 4 Enablement | Model providers | thin |
| 4 Enablement | Tool access / MCP | covered |
| 4 Enablement | Sandboxes | thin |
| 4 Enablement | Permissions | covered |
| 4 Enablement | Secrets | thin |
| 4 Enablement | SDD frameworks | covered |
| 4 Enablement | CI runner and change host adapters | thin |
| 4 Enablement | People: PO/PM | covered |
| 4 Enablement | People: architects | covered |
| 4 Enablement | People: QA | covered |
| 4 Enablement | People: engineers | covered |
| 4 Enablement | People: platform team | thin |
| 4 Enablement | People: review load | covered |
| 4 Enablement | People: skill erosion | covered |
| 4 Enablement | OpModel: Scrum/Kanban on an ART | covered |
| 4 Enablement | OpModel: PI cadence | covered |
| 4 Enablement | OpModel: system demo | thin |
| 4 Enablement | OpModel: I&A | covered |
| 4 Enablement | OpModel: work tracking & knowledge base | covered |
| 4 Enablement | OpModel: decision rights and approvals | covered |
| 5 Assurance | Evidence record | covered |
| 5 Assurance | Rule IDs | thin |
| 5 Assurance | passed/failed/skipped/could_not_run | thin |
| 5 Assurance | Validity per revision | thin |
| 5 Assurance | Templates (spec/plan/ADR/release notes) | covered |
| 5 Assurance | SOC 2 change controls | thin |
| 5 Assurance | Domain standards | thin |
| 5 Assurance | AI use policy | thin |
| 5 Assurance | Agent permissions as privileged access | covered |
| 5 Assurance | Measurement: baseline | covered |
| 5 Assurance | Measurement: flow metrics | covered |
| 5 Assurance | Measurement: DORA metrics | covered |
| 5 Assurance | Measurement: escaped defects | covered |
| 5 Assurance | Measurement: reviewer load | covered |
| 5 Assurance | Measurement: cost per change | covered |
| Adoption | 0 Deterministic floor | covered |
| Adoption | 1 One workflow | covered |
| Adoption | 2 Second workflow + hand-off | covered |
| Adoption | 3 Feedback path proven | covered |
| Adoption | 4 Factory emerges | thin |
