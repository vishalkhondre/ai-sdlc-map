# Approach

## Information architecture

The one-page map is the table of contents. Its five bands become the top-level sections:

| Band | Holds | Typical page types |
|---|---|---|
| 1 Context | project type, product type, change flow | Context variant |
| 2 Lifecycle | portfolio / train / team levels; phases idea → operate; readiness and done; traceability | Phase, Workflow |
| 3 Core | harness engineering, Engineering Kit, rule registry, validators, evidence record, workflows | Concept |
| 4 Enablement | agent runtime and tools, people and roles, operating model | Concept, Role or practice |
| 5 Assurance | evidence and traceability, standards and AI governance, measurement | Concept, Role or practice |

The **adoption path** (stage 0 floor → stage 4 factory) is its own section, and each stage is
a page.

Navigation by purpose sits under the map on the home page:

| Route | Takes the reader to |
|---|---|
| Understand | The map, core concepts, glossary |
| Build the kit | Engineering Kit, rule registry, validators, evidence, kit commands |
| Run a workflow | Workflow catalog and workflow pages |
| Lead adoption | Adoption path, roles, operating model, measurement, change management |
| Look it up | Glossary, references, traditional-to-AI mapping, downloads |

## Page types and templates

Templates live in `templates/pages/` (created in wave 0). Required sections:

| Type | Required sections |
|---|---|
| Concept | Definition · Why it matters · How it works · Where it sits on the map · Pitfalls · Related · Sources |
| Phase | Purpose · Traditional practice · AI-assisted practice · Workflows in this phase · Gates and evidence · Roles · Pitfalls · Related · Sources |
| Workflow | Decision · Trigger · Inputs · Agent task · Checks · Guardrails · Human decision · Outputs and evidence · Failure paths · Measures · Owner · Related · Sources |
| Context variant | What it is · What changes · Gates that move · Risk tier · Workflows affected · Related · Sources |
| Role or practice | Purpose · Responsibilities · What shifts with agents · Warning signs · Related · Sources |
| Adoption stage | What exists · What to build · How to measure · Exit criteria · Risks · Related · Sources |

Every page has front matter: `id`, `type`, `band`, `map_box`, `title`, `summary`,
`key_terms`, `sources`, `related`, `review_record`.

## Sections

Work is planned, built, reviewed and released one **section** at a time (D-014). A section is
one band of the map, or the adoption path. The architect proposes each section's page list from
the source inventory and the author approves it before work starts.

## The pipeline (per page, inside a section)

```
brief ─► research (private source ║ public sources) ─► write ─► diagram
      ─► automated checks ─► reviewers (confidentiality ║ accuracy ║ editorial)
      ─► revise until all ACCEPT (three rounds, then the author)
```

Then, for the section as a whole:

```
every page ACCEPT ─► merge ─► deploy live ─► author reviews live ─► follow-up PRs
                  ─► author approves ─► tag vX.Y.Z ─► GitHub Release (notes + PDF snapshot)
```

1. **Brief.** The architect agent opens a page brief: box, type, scope, key terms, related pages.
2. **Research, in parallel.** The source researcher reads the private library and writes a
   de-identified *practice brief* that stays outside the repo. The external researcher finds
   public sources for every claim the page will make.
3. **Write.** The author agent writes the page from both briefs, to its template.
4. **Diagram.** The diagrammer adds diagrams as code where they carry meaning.
5. **Automated checks.** Deny-list, banned phrases, citations, template structure, links, build.
6. **Review.** Three reviewers work independently and return ACCEPT, REVISE or BLOCK with
   findings tagged by rule number. Confidentiality BLOCK is final until fixed.
7. **Revise** until every reviewer accepts. Loops are capped at three; after that the page goes
   to the author.
8. **Merge and deploy.** The review record is committed with the page; CI verifies it before
   deploying. The page is live once its section merges.
9. **Author review and release.** The author reviews the section on the live site. Changes come
   as follow-up pull requests through the same pipeline. When the author approves, the section's
   release is tagged; the tag and its GitHub Release are the record of approval (D-016).

## Waves

Waves group sections for planning and retrospectives; sections are the unit of approval and
release.

| Wave | Scope | Exit criteria |
|---|---|---|
| 0 Foundations | Ground rules, templates, agents and skills, checks (deny-list hashing, banned phrases, template structure, link check, review-record gate), clickable map as home page, source inventory | All checks run in CI; map live; inventory maps every library document to map boxes |
| 1 Core and lifecycle | Sections: core (band 3); lifecycle (band 2 phases, their workflows and the SAFe reference model, D-015) | Each section released; retrospective held |
| 2 Assurance and enablement | Sections: enablement (band 4); assurance (band 5) | As above |
| 3 Context and adoption | Sections: context (band 1); the adoption path | As above; every map box links to a page |

Each wave ends with a retrospective recorded in `STATUS.md` and any rule or process change
recorded in `DECISIONS.md`.

## Definition of done (site release)

- Every box on the map links to a published page.
- Every page has a passing review record.
- CI is green on `main`, and the release is tagged with a changelog entry.
- Each section is tagged in turn (one minor version each); the site is v2.0.0 when every box on
  the map has a page (D-016).
