# Section plan: Core (band 3)

Proposed by the architect, 2026-09-25, for the author's approval (D-014, GR-6.1). Nothing in
this section is written until the author approves this plan.

- **Section:** core, band 3 of the map ("what does the work").
- **Edition:** 1.3.0 when the section merges; follow-ups before approval are 1.3.x; tag at
  approval (D-016).
- **Sources:** `project/COVERAGE.md` rates six of the eight core boxes as covered by the source
  library and two as thin. Every page cites public sources for its claims (GR-2); the library
  informs practice only (GR-1.2).

## Pages

| # | Page id | Type | Map box | Coverage | Scope |
|---|---|---|---|---|---|
| 1 | `harness-engineering` | Concept | Harness engineering | covered | The discipline: what the agent may read and do, what a machine checks, what a person decides; guides and sensors; computational and inferential controls; the steering loop; harnessability; how the discipline relates to the kit, workflows and the factory. |
| 2 | `engineering-kit` | Concept | Engineering Kit | covered | The artefact: a versioned, installable package of the reusable environment; its layers; what installation must prove; how it is versioned and upgraded; the overview page for pages 3–7. |
| 3 | `rule-registry` | Concept | Engineering Kit · rule registry | covered | Every rule with an ID, a route (gate, judgment, guidance) and an owner; starting with a few high-impact, low-ambiguity rules; how rule IDs tie a rule to its check and decision. |
| 4 | `validators` | Concept | Engineering Kit · validators | covered | Deterministic checks as code; the path from observing to blocking; result states including could_not_run; timeouts and missing results; flaky checks; fitness functions for architecture rules. |
| 5 | `skills-and-evals` | Concept | Engineering Kit · skills with evals | covered | Skills as packaged guidance for the agent; the acceptance bar that differs from validators; evaluation sets with positive, no-op and negative cases; when a practice is ready to become a skill. |
| 6 | `evidence-schema` | Concept | Engineering Kit · evidence schema | covered | The fixed shape of the evidence record a run leaves; its fields; validity for one revision. The assurance section later covers how evidence is used for traceability and audit, and links here. |
| 7 | `adapters` | Concept | Engineering Kit · adapters | thin | Thin adapters that bind the kit to a CI runner, change host, work tracker and tool servers without the kit depending on any one product; testing adapters. Relies mainly on public sources. |
| 8 | `workflows` | Concept | Workflows | covered | The unit of work: one delivery decision end to end, with trigger, agent task, checks, human decision, evidence and owner; the three roles; failure paths; evidence hand-offs; how to choose the first workflow. Links to the catalog, which stays the list of workflows. |
| 9 | `software-factory` | Concept | Software factory | thin | The operating state that emerges when workflows share rules, evidence and feedback; what it is not; the condition that makes it real; the risks that scale with it. Relies mainly on public sources and is presented as recommended practice where no evidence exists (GR-2.3). |

## Links and map changes

- Map links (`content/diagrams/map/links.yml`): Harness engineering, Engineering Kit and Software
  factory move from the series parts to these pages; Workflows moves from the catalog to the
  `workflows` page. Each page links on to its series part and the catalog.
- The kit's five sub-elements are text inside the Engineering Kit box today, not separate
  labels. Linking them from the map needs a small map change (the five phrases become linked
  labels); I propose it with this section. Without it they are reached from the Engineering Kit
  page and the "Build the kit" route.
- Routing row: "Build the kit" gains the kit pages; "Understand" gains Harness engineering.
- `site/generate.py` gains rendering for `content/pages/` the first time (page chrome,
  navigation, search, sitemap, llms files).

## Related pages outside the section

The Evidence & traceability, Measurement and Standards pages (assurance), People & roles and
Agent runtime (enablement), and the pull-request verification workflow (lifecycle) do not exist
yet. Core pages link to the catalog and the series for these until they do; no link points at a
page that does not exist (GR-4.3).

## Risks

- **Confidentiality:** the library covers this band in depth, so the risk of close paraphrase is
  highest here. The source researcher's briefs stay in the scratchpad, and the confidentiality
  reviewer reads the pages cold.
- **Evidence:** adapters and the software factory have little public evidence beyond
  practitioner writing; those pages present recommended practice as such.
- **Overlap with the series:** the pages are reference pages, not the series' narrative. They
  link to the parts and never copy their text (D-010).

## Decisions needed from the author

1. Approve, change or cut the nine pages.
2. Link the kit's five sub-elements on the map (small map change in this section), or not.
3. Keep `evidence-schema` in core (with assurance linking to it), or move evidence entirely to
   the assurance section.
