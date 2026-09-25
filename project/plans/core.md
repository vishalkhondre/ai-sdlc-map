# Section plan: Core (band 3)

Proposed by the architect, 2026-09-25. **Approved by the author with changes, 2026-09-25 (D-018);**
the changes are applied below.

- **Section:** core, band 3 of the map ("what does the work").
- **Edition:** 1.4.0 when the section merges (1.3.0 is the brand release, D-021); follow-ups
  before approval are 1.4.x; the tag is created at approval (D-016). `release/sections.yml`
  gains a `"1.4"` entry naming the section and its pages.
- **Sources:** `project/COVERAGE.md` rates six of the eight core boxes as covered by the source
  library and two as thin. Every page cites public sources for its claims (GR-2); the library
  informs practice only (GR-1.2). Borrowed terms keep their credit: guides and sensors,
  computational and inferential controls, the steering loop and harnessability (Böckeler), and
  fitness functions (evolutionary-architecture practice), as the glossary already records
  (GR-2.2).

## Boundary with the other sections

Core defines each artefact: what it is, what it holds and how it is built. Other sections own how
the artefact is used.

| Topic | Core (this section) | Other section |
|---|---|---|
| Rule IDs | what the registry holds: ID, route, owner | assurance: tracing rule → check → decision |
| Check results | how a validator reports a result, including when it cannot run | assurance: what passed, failed, skipped and could_not_run mean for a decision |
| Evidence | the schema: its fields and who writes them | assurance: the record on every run, its expiry per revision, audit and traceability |
| Adapters | the kit's adapter layer and how it is tested | enablement: the CI runner, change host and tool servers themselves |
| First workflow, hand-offs | what a workflow is and what it hands on | adoption path: which workflow to build first (stage 1), the second and its hand-off (stage 2) |
| When a factory is real | what the operating state is and what it is not | adoption path: stage 4's exit criteria |

## Pages

| # | Page id | Type | Map box | Coverage | Scope | Leaves to others |
|---|---|---|---|---|---|---|
| 1 | `harness-engineering` | Concept | Harness engineering | covered | The discipline: what the agent may read and do, what a machine checks, what a person decides; guides and sensors; computational and inferential controls; the steering loop (the feedback path; which map label links here is confirmed with the author, see STATUS); harnessability; how the discipline relates to the kit, workflows and the factory. | Agent runtime and tools (enablement) |
| 2 | `engineering-kit` | Concept | Engineering Kit | overview of rows 3–7 | The artefact: a versioned, installable package of the reusable environment; its parts; technology profiles; project configuration; the kit's commands (init, doctor, verify); the `could_not_run` result; what installation must prove; versioning and upgrades. The overview for pages 3–7. | Each part's detail (pages 3–7) |
| 3 | `rule-registry` | Concept | Engineering Kit · rule registry | covered | Every rule with an ID, a route (gate, judgment or guidance) and an owner; how rules enter, change and retire; choosing the first rules. | Tracing rule → check → decision (assurance) |
| 4 | `validators` | Concept | Engineering Kit · validators | covered | Deterministic checks as code; the path from observing to blocking; how a validator reports a result, including when it cannot run; timeouts and flaky checks; fitness functions for architecture rules. | What each result means for a decision (assurance) |
| 5 | `skills-and-evals` | Concept | Engineering Kit · skills with evals | covered | Skills as packaged guidance for the agent; why their acceptance bar differs from validators'; evaluation sets; when a practice is ready to become a skill. | Review load and skill erosion (enablement) |
| 6 | `evidence-schema` | Concept | Engineering Kit · evidence schema | covered | The fixed shape of what a run records: its fields, who writes each one, and how the schema is versioned. | The record on every run, expiry per revision, audit (assurance) |
| 7 | `adapters` | Concept | Engineering Kit · adapters | thin | The kit's thin adapter layer, which binds it to a CI runner, change host, work tracker and tool servers without depending on any one product; how adapters are tested. Relies mainly on public sources. | The tools themselves (enablement) |
| 8 | `workflows` | Concept | Workflows | covered | The unit of work: one delivery decision end to end, with trigger, agent task, checks, human decision, evidence and owner; the three roles; failure paths; what a workflow hands to the next. Links to the catalog, which stays the list of workflows. | Which workflow first, and the second (adoption) |
| 9 | `software-factory` | Concept | Software factory | thin | The operating state that emerges when workflows share rules, evidence and feedback; what it is not; the risks that scale with it. Relies mainly on public sources; presented as recommended practice where no evidence exists (GR-2.3). | Exit criteria for stage 4 (adoption) |

The Engineering Kit box holds its five parts as one line of text, and the coverage table rates
the parts, not the box. The plan gives the kit one overview page and one page per part, because
each part has its own practice, its own checks and its own sources, and a reader looking for one
of them should land on it directly.

## Order of work

1. **Tooling first** (STATUS Next item 3): `check_citations.py` covers `content/pages/`
   (references cited only by pages, keep-out and product names in page prose, glossary credit per
   page); `site/generate.py` renders pages (chrome, navigation, search, sitemap, llms files).
   Reviewed and merged on its own, before any page.
2. **Parts before the whole:** pages 3–7 in parallel, then page 2 (the kit overview), which
   summarises them.
3. **Pages 1, 8 and 9** in parallel with step 2.
4. **Map and routes** once every page exists: `links.yml`, and the map change that links the
   kit's five parts (D-018).
5. **Review** of the whole section (three reviewers, three rounds, then the author), merge as
   1.4.0, the author reviews it live, follow-ups as 1.4.x, tag at approval.

The D-015 relabel of the lifecycle levels is a separate content edition, after this section.

## Links and map changes

Approved (D-018): the kit's five parts are linked on the map, and every boundary row is
cross-linked both ways once the other section's page exists.

- **Map links** (`content/diagrams/map/links.yml`): Harness engineering, Engineering Kit and
  Software factory move from their glossary entries (D-019) to these pages. Workflows moves from
  the catalog to the `workflows` page. Each page links on to its glossary entry and to the catalog.
- **Routing row:** "Build the kit" gains the kit pages. Harness engineering moves from "Build the kit" to "Understand", and "Build
  the kit" links the kit overview in its place.
- **Linking the kit's parts (D-018).** Today the whole Engineering Kit box, including its text line, is one link,
  and an SVG link cannot hold other links. Linking the five parts means laying them out as five
  separate labels inside the box, with only the title linked to the overview. That is a small
  redesign of the box in `build_map.py`, five new `links.yml` entries, and the build's check that
  each label is on the map.

## Related pages outside the section

The Evidence & traceability, Measurement and Standards pages (assurance), People & roles and
Agent runtime (enablement), the adoption stages, and the pull-request verification workflow
(lifecycle) do not exist yet. Until they do, core pages link to the catalog and the glossary; no
link points at a page that does not exist (GR-4.3).

## Risks

- **Confidentiality:** the library covers this band in depth, so the risk of close paraphrase is
  highest here. The source researcher's briefs stay in the scratchpad, the author agent writes in
  general practitioner words, and the confidentiality reviewer reads the pages cold, with an
  extra close-paraphrase pass for these covered boxes.
- **Evidence:** adapters and the software factory have little public evidence beyond practitioner
  writing, so those pages present recommended practice as such.
- **Independence:** the pages are reference pages written for this site. They neither link to
  nor draw text from the earlier narrative series (D-019).

## Decisions taken by the author (D-018)

1. The nine pages are approved; no tenth page. The kit overview adds technology profiles,
   project configuration, the kit's commands and the `could_not_run` result; the harness
   engineering page carries guides and sensors, computational and inferential controls and the
   steering loop, and the map's "Feedback path" links to it.
2. The kit's five parts are linked on the map.
3. The boundary table is approved, with cross-links both ways.
