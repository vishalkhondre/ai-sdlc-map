# Changelog

Content edition history of The AI SDLC Map. Only reader-visible changes to the map, diagrams, catalog, terminology or references bump this version.

## 1.6.0 — 2026-11-27

The Lifecycle section, part two.

- Seven new workflow pages, in reading order: Intake and triage; Specification readiness; Design conformance; Pull-request verification; Deploy verification; Release readiness; and Incident feedback. Each page sets out one workflow's decision, how a run proceeds and fails, the evidence it leaves and the measures that show whether it works, links its workflow catalog row, uses the customer-record export as its example and names its sources. The pages appear in the Lifecycle section's navigation, search, the sitemap and the llms files, and the routing row's Run a workflow route leads to them.
- On the map, the intake & triage, spec readiness, design conformance, pull-request verification, deploy verification, release readiness and incident feedback labels open their workflow pages instead of the workflow catalog.
- The Idea, Specification, Design, Develop, Build and QA, Deploy, Release and Operate pages link to the workflow pages beside the catalog rows they name, and list them under Related. The Workflows and Software factory pages link to the Pull-request verification and Incident feedback pages; the Harness engineering page links to Incident feedback.
- 5 new terminology entries: Canary release (canarying); Postmortem; Pre-integration review; Regression testing; and Service level objective (SLO). Each names its origin.
- 13 new references, each with its title, author or organisation, address and date accessed.
- Corrections to existing references, each read again at its source: the notes for the Scrum Guide, Semantic Versioning, Keep a Changelog (both editions), the SRE book's release engineering chapter, the SRE workbook's postmortem chapter, the SLSA verification and verification summary pages, the NIST SSDF and SP 800-61 Rev. 3, OWASP ASVS, Spec Kit, the Agile Alliance Definition of Ready entry, INVEST, given-when-then, Self Testing Code and DORA's metrics, work in process limits, customer feedback and change approval pages now record the further points they state that the new pages rely on.

## 1.5.0 — 2026-11-21

The Lifecycle section, part one.

- Twelve new reference pages, in reading order: Lifecycle levels: portfolio, train and team; SAFe reference model; Idea; Specification; Design; Develop, Build and QA; Deploy; Release; Operate; Definition of Ready and Definition of Done; Traceability spine; and Inspect and Adapt. Each page uses the customer-record export as its example and names its sources. The Lifecycle section appears in the header tabs, the left navigation, search, the sitemap and the llms files.
- The map's lifecycle band uses generic level labels, portfolio, train and team; SAFe is cited as one framework that uses these levels, and the SAFe reference model is this site's mapping of it onto the band (D-015).
- On the map, the phase, level, Definition of Ready and Definition of Done, traceability spine and Inspect & Adapt labels open their Lifecycle pages.
- 22 new terminology entries: Acceptance criteria; Agile Release Train (ART); Continuous Delivery Pipeline; Dark launching; Definition of Done; Definition of Ready; Deploy versus release; Given, when, then; Hermetic build; Inspect and Adapt; INVEST; Portfolio, train and team levels; PI Planning; Planning Interval (PI); Reference model; Release toggle; Spec-first, spec-anchored, spec-as-source; System Demo; Test pyramid; Testability; Traceability spine; and WSJF (weighted shortest job first). Each names its origin; Portfolio, train and team levels and Traceability spine are coined here, the latter naming requirements traceability as its idea.
- 98 new references, each with its title, author or organisation, address and date accessed.
- Corrections to existing references, each read again at its source: DORA's metrics reference now points to the DORA metrics guide and names its five metrics; the DORA 2024 and 2025 report references point to their current pages and say what those pages state, with the throughput and stability findings credited to the 2025 announcement; the NIST SSDF reference cites version 1.1, the final version, and the tasks relied on; the Spec Kit, OWASP ASVS, SLSA provenance, SAFe Planning Interval, DORA customer-feedback and Google postmortem references have corrected titles, bylines or notes; the AI-assistant security study is checked against its preprint.
- The map's credit lines name SAFe (Scaled Agile, Inc.) for Agile Release Train, System Demo and Inspect & Adapt, and the Scrum Guide for Definition of Done.
- Core pages link to the Lifecycle pages where they mention the traceability spine, the Definition of Ready and Definition of Done, lifecycle levels or Inspect and Adapt.
- Core prose corrections: Software factory states DORA's 2024 and 2025 findings as each source gives them; Workflows says DORA groups its software delivery performance metrics into throughput and instability; Evidence schema bases optional extra fields on SLSA provenance's requirement that consumers ignore fields they do not recognise, and says rule IDs are carried by expected checks, results and findings, not by decisions.

## 1.4.2 — 2026-10-06

Diagrams on five Core pages, and two wording fixes on the home page.

- Harness engineering: a diagram of guides and sensors, computational and inferential controls, who decides, and the feedback path, this site's extension of Böckeler's steering loop, by which a recurring failure changes a guide or a sensor.
- Evidence schema: a diagram of the fields of one evidence record, the kind of writer allowed to fill each, and how the overall status is derived from check results and decisions, never from agent findings.
- Engineering Kit: a diagram of the kit's five parts, its four layers and who may change each, and where the three commands, init, doctor and verify, act.
- Workflows: a diagram of one workflow run from trigger to evidence record, with the agent, the checks and the people kept apart, the input check before the run shown as a precondition, and each failure path naming who acts next.
- Validators: a diagram of one validator called the same way from a developer's machine, an agent's session and CI, its four results, and what each means while the validator is report-only and once it is required.
- Each new diagram has a text description and a credit line for the terms it borrows, and can be downloaded as SVG or PNG.
- Home page: the map's introduction and caption say that underlined labels are links to where each item is covered. The adoption path's closing line states its order as a recommendation: build the floor and the first workflow before adding skills, agents and platforms.

## 1.4.1 — 2026-09-28

Every reference on the site was read again at its source; sentences that said more than their source now say what it says.

- Harness engineering: Böckeler notes that technology and architecture choices shape how governable a codebase is, rather than arguing that harnessability should be a first-class criterion; she calls behaviour "the elephant in the room" rather than the hardest to check; the context-engineering definition is credited to Bharani Subramaniam, whom she quotes; the Technology Radar's list of feedback sensors names structural tests, not type checkers; and the vendor account of harness engineering is described as a prominent use of the term, not the one that popularised it.
- The partial reach of inferential sensors and the cost of computational sensors now cite Böckeler's harness article rather than her sensors article, and on every Core page the review skill's advisory role is labelled as this site's practice.
- Skills with evals: vendor guidance starts from where the agent struggles on representative tasks; writing evaluation cases before the skill text cites only the guidance that says so; a skill explaining why a rule exists is labelled as this site's recommendation.
- Rule registry: the analysis platform's two thresholds are given separately (probation at 10%, switch-off above 25%).
- Workflows, Software factory and Adapters: the Lean definition of value-stream mapping, the thinnest viable platform as its page describes it, and two archived Technology Radar entries in the past tense with their volumes.
- References: bylines, titles and dates corrected, including the volumes and rings of five archived Radar entries; the SAFe note describes only what its page covers; one reference added, DORA's 2025 announcement, for its wording on control systems; the AWS AI-DLC reference now points to the AWS DevOps blog post.

## 1.4.0 — 2026-09-25

- A new Core section with nine reference pages, in reading order: Harness engineering, the Engineering Kit, the kit's five parts (Rule registry, Validators, Skills with evals, Evidence schema, Adapters), Workflows and the Software factory. Each page defines one part of the core band of the map, uses the customer-record export as its example, and names its sources. The Core section appears in the header tabs, the left navigation, search, the sitemap and the llms files.
- On the map, the Harness engineering, Engineering Kit, Workflows and Software factory labels open their Core pages. The Engineering Kit box now shows its five parts as separate labels, and each opens its own page; the box's title opens the kit overview.
- The routing row under the map leads to the new pages: Understand gains Harness engineering; Build the kit leads to the Engineering Kit and its five parts; Run a workflow and Lead adoption lead to the Workflows and Software factory pages.
- New terminology entries: Technology profile, Project configuration, Golden path, Architecture decision record, Fitness function (architectural), LLM-as-a-judge, Ports and adapters, Anticorruption layer, Contract test and Consumer-driven contract, each with its origin.
- Revised terminology entries: Requisite variety no longer says the law favours fewer controls; the Engineering Kit entry names the kit's three commands; could_not_run, Evidence record, Adapter, Validator, Gate, Risk tier, Spec-driven development, Workflow and Software factory are made more precise; Software factory is called an operating state and names the earlier senses of the phrase it does not mean; the Harness engineering entry calls the factory an operating state too. Skill, Harness evaluation and Risk tier point to public descriptions of the practice.
- 94 new references, from standards bodies (OASIS, NIST, OWASP, SLSA, in-toto, ISO), research (DORA, peer-reviewed studies) and practitioners, each with its title, author or organisation, address and date accessed.
- Corrections to three existing references: the fitness-function article is published on thoughtworks.com; the Spec Kit note lists clarification as optional, not as a fixed command; the harness-engineering note names Böckeler's three regulation categories and says the article discusses ambient affordances rather than introducing them.
- The map's credit line names Nygard as the source of architecture decision records and Cockburn as the source of adapters; the Adapter entry is now credited as adapted from Cockburn's ports and adapters pattern.
- On the adoption path, the "Feedback path proven" label opens the Harness engineering page's section on the steering loop and the feedback path.
- Wording in the adoption path, the workflow catalog and the Deterministic gate and Deterministic floor entries now names the kit's verify command and says new validators run report-only before they become required; the floor's first validators are described as a few, for rules the team has broken before.
- Two Technology Radar references are labelled as archived entries, with their volume.

## 1.3.0 — 2026-09-25

- Every link now stays on this site: the navigation, footer, home page, routing row, terminology, references, workflow catalog, search, the not-found page and the downloadable map.
- The map's Harness engineering, Engineering Kit and Software factory labels open their terminology entries. The routing row leads to the AI SDLC entry, the terminology, the workflow catalog and the adoption path.
- Terminology and reference notes speak of "this site"; terms introduced here are labelled "Coined here". The export example, Requisite variety, Harnessability and Guides and sensors entries say what the site itself does. The Harness entry also cites Böckeler's context-engineering article, for the context the agent reads.
- The workflow catalog's introduction quotes the Workflow entry's definition. Two catalog notes are shortened.
- Earlier entries in this changelog were reworded to match.
- Pages use a documentation layout: a sticky header with section tabs and search, a left navigation listing the section's pages, an "On this page" list on pages with sections, breadcrumbs that name the section, and previous and next links. The home page keeps the full-width map and adds a section chooser. On small screens the navigation opens as a drawer. A skip link, labelled navigation landmarks and visible focus support keyboard and screen-reader use, checked with automated accessibility tests. The References page's entries become second-level headings. The text of every page stays the same; the only new words are navigation labels.
- The site has its own look, Slate & Teal: a slate and teal palette with amber for judgment and notes, in light and dark themes that meet WCAG AA contrast; Atkinson Hyperlegible for text and IBM Plex Mono for code, served with the site; a logo of five stacked bars, one per band of the map, with the wordmark; a matching favicon and social preview image. The map's band colours are unchanged.

## 1.2.1 — 2026-09-25

- Every reference now records the date its title, author, date and address were last checked, shown on the References page as "accessed".
- Corrections to seven older references:
  - The fitness-function article is "Fitness function-driven development" by Paula Paul and Rosemary Wang (Thoughtworks, January 2019).
  - The OpenAI harness-engineering account is by Ryan Lopopolo.
  - Spec Kit uses the repository's own title, and its note no longer calls it the origin of spec-driven development.
  - The context-engineering note describes what that article covers, and gains its date (February 2026).
  - The sensors article is dated by month (May 2026), because it was published in parts.
  - Two Böckeler titles now match their published sentence case.
  - Fowler's Continuous Integration note calls it the classic statement of the practice rather than its origin, and gains its revision date (January 2024).
- The Gate entry credits fitness functions to evolutionary-architecture practice, matching its source.

## 1.2.0 — 2026-09-25

- The site is renamed **The AI SDLC Map**, with the subtitle "The AI-assisted software lifecycle, from spec to software factory, on one page." The address does not change. The home page, page titles, social preview text, the map's own title and the downloadable map now carry the new name.
- The home page and the workflow catalog spell out "software development lifecycle (SDLC)" where the term first appears.
- New terminology entry, **AI SDLC**: what the term means on this site, and how it differs from the lifecycle for building AI and machine-learning systems and from AWS's AI-Driven Development Lifecycle (AI-DLC). Three references added: IBM's pages on the AI lifecycle and on AI-DLC, and AWS Builder Center's introduction to AI-DLC. Where one entry cites the same author twice, its source links now add each title.

## 1.1.0 — 2026-09-25

- The map on the home page is clickable. Eighteen underlined labels open the page that covers them: the four core concepts (three core-concept pages and the workflow catalog), the workflow in each lifecycle phase and the two flows that have a workflow of their own (in the workflow catalog), and the five adoption stages. Labels without a page stay plain. The downloadable SVG is unchanged.
- Under the map, a routing row starts readers by purpose: Understand, Build the kit, Run a workflow, Lead adoption, Look it up.

## 1.0.0 — 2026-09-25

- First edition as a site of its own. The home page carries the five-band AI SDLC map and the adoption path, with the SDLC workflow catalog, terminology and references.
