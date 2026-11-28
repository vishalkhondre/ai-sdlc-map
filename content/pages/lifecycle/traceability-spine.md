---
id: traceability-spine
type: concept
band: lifecycle
map_box: Traceability spine
title: Traceability spine
summary: The chain of seven artefacts from requirement to incident, each pair linked by an identifier and checked for orphans in both directions, with rule IDs as the keys that tie checks and findings, and through them decisions, to the chain.
key_terms: [traceability-spine, rule-registry, evidence-record, evidence-handoff, feedback-path, could-not-run, validator, workflow, specification-readiness, software-factory, export-example]
sources: [gotel-finkelstein-1994, nasa-swe-052, rath-traceability-wild-2018, owasp-asvs, owasp-wstg, google-sre-postmortem, nist-ssdf, nist-800-61r3, slsa-provenance, bockeler-harness, bockeler-sensors, safe-inspect-and-adapt, istqb-acceptance-criteria, scrum-guide-2020]
related: [rule-registry, evidence-schema, workflows, software-factory, harness-engineering, specification, design, develop-build-qa, deploy, release, operate, definition-of-ready-and-done, inspect-and-adapt, evidence-record]
review_record: content/reviews/1.5.0-lifecycle.md
---

## Definition

Requirements traceability is, in Gotel and Finkelstein's definition, "the ability to describe and
follow the life of a requirement, in both a forwards and backwards direction (i.e., from its
origins, through its development and specification, to its subsequent deployment and use
...)".[^gotel-finkelstein-1994] On the map of the AI SDLC (the software development lifecycle with
AI agents doing part of the work), the *traceability spine* is that idea drawn as one line under
the phases. It is a chain of seven kinds of artefact: requirement, spec, task, test, change,
release and incident. An identifier links each artefact to the next. Rule IDs, the stable codes
that a [rule registry](rule-registry.html) gives each rule, tie checks and findings to the chain,
and decisions are tied to it through the checks and findings they read. The name is this site's,
coined for the map, and so is the extension of the chain past release to the incident that
follows. Both are built on requirements traceability as Gotel and Finkelstein describe
it.[^gotel-finkelstein-1994]

## Why it matters

Each missing link has its own cost.

- **Requirement without a test.** The requirement ships on trust. Traceability can point out
  requirements that are not tested.[^nasa-swe-052]
- **Test without a requirement.** The test costs time to write, run and maintain, and nobody can
  say what it protects. The same source calls these extra tests.[^nasa-swe-052]
- **Change without a task or criterion.** The reviewer has no stated intent to judge the change
  against, so scope creep and unexplained edits pass as easily as intended ones.
- **Incident without a path to the specification.** The failure is fixed where it showed, and the
  gap that let it through stays open. The catalog workflow for this link is
  [Incident-to-development feedback](workflow-catalog.html#W28).

Following a requirement in both directions is part of the definition: forwards to deployment and
use, backwards to its origins.[^gotel-finkelstein-1994] A chain checked in one direction only
leaves half of these failures invisible.

Public evidence that links go missing when left to habit is limited but concrete. An analysis of
six open-source projects found that on average only 60% of the commits were linked to specific
issues, and its authors note that without these fundamental links the entire set of project-wide
links will be incomplete.[^rath-traceability-wild-2018] The result concerns commit-to-issue links
in six projects. It is from the authors' preprint, and it is not a measure of traceability
practice in general.

Some regulated work requires the practice. NASA's software engineering handbook, on requirement
SWE-052, asks projects to "perform, record, and maintain bi-directional traceability" between
listed pairs of products, and the requirement applies according to software class, not equally to
all software.[^nasa-swe-052] It is one public example, not a rule for every project or
organisation.

Coding agents raise the stakes. They write tasks, tests and changes faster than people can read
them, so more artefacts exist whose reason nobody has checked. No public study measures how agents
affect traceability. Treating the chain as something the workflows write and checks verify,
rather than something people reconstruct, is this site's recommended practice.

## How it works

### The seven artefacts, in the map's order

1. **Requirement.** A need or constraint the product must meet, with a named origin. It enters at
   the idea stage.
2. **Spec.** The [specification](specification.html) that answers the requirement and states its
   acceptance criteria[^istqb-acceptance-criteria].
3. **Task.** A unit of planned work from the [design](design.html) stage, derived from the
   criteria.
4. **Test.** A check that a criterion holds, together with its recorded result.
5. **Change.** A revision of code or configuration made for a task, built and verified in
   [Develop, Build and QA](develop-build-qa.html).
6. **Release.** The candidate revision, with its records, that is approved in
   [Release](release.html) and put into an environment in [Deploy](deploy.html).
7. **Incident.** An event in operation where the software departs from what was expected, handled
   in [Operate](operate.html).

### The link between each adjacent pair

The table gives, for each pair, the identifier that links it, the catalog workflow that writes the
link and what a reader sees when the link is missing. Which identifier links which pair is this
site's model, not a public standard. Each workflow's decision, checks and evidence are in its row
of the [workflow catalog](workflow-catalog.html), and the record fields that carry the links are on
the [evidence schema](evidence-schema.html) page.

| Pair | Linking identifier | Written by | What a missing link looks like |
|---|---|---|---|
| Requirement to spec | The acceptance-criterion identifier. Each criterion in the spec has its own, and names the requirement it answers | [Specification readiness](workflow-catalog.html#W04) | A requirement that no criterion answers, so nothing later in the chain can point back to it |
| Spec to task | The criterion identifier, carried on each task | [Task traceability and test planning](workflow-catalog.html#W12) | Planned work whose purpose cannot be looked up in the spec, which is how scope creep enters |
| Task to test | The criterion identifier, carried on each test and on its recorded result | Task traceability and test planning; [Acceptance-test generation and execution](workflow-catalog.html#W17) | A criterion that is built but never shown to hold, because no recorded result names it |
| Test to change | The change revision named on the evidence record that holds each result; the change in turn cites its task | [Task execution loop](workflow-catalog.html#W13); [Pull-request verification](workflow-catalog.html#W23) | A pass that cannot be tied to the code that merges, because it names another revision or none |
| Change to release | The revisions of the changes the release candidate contains | [Release readiness](workflow-catalog.html#W25) | A release whose contents nobody can list by revision |
| Release to incident | The identifier of the release that was running, recorded on the incident record | [Deployment and post-deploy verification](workflow-catalog.html#W26); [Incident remediation](workflow-catalog.html#W27); [Incident-to-development feedback](workflow-catalog.html#W28) | An incident that cannot be matched to a release, so the trail back to the requirement starts from guesswork |

Read down the table, the identifiers change class. The upper half is keyed by criterion and task
identifiers, which exist before any code does. The lower half is keyed by revisions and release
identifiers, which exist because a run or a build produced them, with rule IDs on every check
result beside them. The criterion identifier on a recorded test result is the join between the
two halves. Read up the table, the same identifiers lead from an incident back to the requirement.

For the pair at the far end, supply-chain provenance is a public relative: "verifiable information
about software artifacts describing where, when, and how something was
produced".[^slsa-provenance] It ties a built artefact back to how it was made. The spine asks a
similar question of the whole chain: where did this artefact come from, and what did it lead to?

### Orphans in both directions

An orphan is an artefact with no link on one side. Orphans point in two directions, and the chain
is checked in both.

A forward orphan is a requirement that no test reaches, so the requirement ships on trust. A
backward orphan is a test, task or change that leads to no requirement, so it costs effort and
protects nothing anyone can name. NASA's handbook describes the same two failures from the side of
testing: traceability "can point out software requirements that are not tested (i.e., missing
tests) and tests that do not serve to test requirements (i.e., extra
tests)".[^nasa-swe-052]

NASA's handbook lists six bi-directional pairs, among them higher-level and software requirements,
requirements and design components, design components and code, and requirements and software
verification.[^nasa-swe-052] That is a public example. This site's seven-artefact chain is its own,
and the pairs are not the same.

Checking is not a one-time act. The handbook describes the matrix as completed left to right early
in the appropriate phase, with the forward trace extended to the next set of products as each
column is completed, and as maintained throughout the life of the project.[^nasa-swe-052] A trace
that is complete at planning and stale at release has not done its job.

### Rule IDs as link keys

The criterion and task identifiers link the upstream half of the chain. Across the downstream half,
rule IDs do the linking. The [evidence schema](evidence-schema.html) puts the ID of the rule
concerned on every expected check, result and finding, so results and findings about the same rule
line up across runs and workflows. A decision carries no rule ID of its own. It is tied to the
chain through the checks and findings it reads, which name the rules. Using rule IDs as the keys of
the spine in this way is this site's recommended practice, and no public standard prescribes it.
The [rule registry](rule-registry.html) page describes how the identifiers are defined and kept
stable, and the results come from [validators](validators.html), deterministic checks this site
adapts from what Böckeler calls computational sensors.[^bockeler-sensors]

Public identifier schemes show the same discipline. OWASP's Application Security Verification
Standard numbers its requirements by chapter, section and requirement, prefixes them with the
version when cited (`v<version>-<chapter>.<section>.<requirement>`), and encourages
organisation-specific forks provided they maintain traceability, so that passing a requirement
means the same across all versions.[^owasp-asvs] The OWASP Web Security Testing Guide, a
community-created guide, gives each test scenario an identifier in the form
`WSTG-<category>-<number>`, for example WSTG-INFO-02.[^owasp-wstg] NIST's Secure Software
Development Framework version 1.1 identifies each practice, for example PO.1.2, "Identify and
document all security requirements for organization-developed software to meet, and maintain the
requirements over time", and RV.3, "Analyze Vulnerabilities to Identify Their Root
Causes".[^nist-ssdf] These are cited as examples of stable identifiers, not as sources of a
traceability requirement. They show how a requirement or practice stays the same thing across
documents, tools and versions.

Stable identifiers let each link be written at the moment its artefact is made. This site's
recommended practice is that the workflow producing an artefact records the link in its
[evidence record](glossary.html#evidence-record) as a by-product of the run, so the chain never has
to be rebuilt afterwards; the "Written by" column of the table above names the
[catalog](workflow-catalog.html) row for each pair. The commit-to-issue analysis cited under "Why
it matters" shows how incomplete links left to habit can be, and it does not test this
recommendation.

### The customer-record export, left to right and back

The running example is a hypothetical feature that lets users export customer records. Its open
decisions are which records, which fields, how large an export may be, what happens on failure, and
how the feature is audited. The walk below names the artefact and the identifier at each step,
using classes of artefact rather than invented identifiers, except the revision shown on the
evidence schema page.

1. **Requirement to spec.** The need that users export only the records they may read is answered
   by the spec's acceptance criterion on who may export which records, and that criterion's
   identifier, with the access rule R-042 it relies on, is the link.
2. **Spec to task, and task to test.** Every task and test written for that criterion carries its
   identifier, and the two checks that guard the rules, the access validator and the 50k-row load
   scenario, carry R-042 and the volume-limit rule R-017.
3. **Test to change.** The pull-request run's evidence record names the change revision `3f9c2e1`
   and records R-042 as `failed` and R-017 as `could_not_run`, so both results belong to that exact
   revision ([evidence schema](evidence-schema.html#the-customer-record-export)).
4. **Change to release.** Once the background worker's query is narrowed and the checks run again,
   release readiness reads the record for the new revision, not the first one, so the release links
   to the change through the revision that ships.
5. **Release to incident, and back.** When a scheduled full export, within R-017's limit but far
   larger than the 50k-row scenario, times out in production, the incident record names the running
   release, and the identifiers lead back through R-017's checks to the specification, where nobody
   had asked how large the largest export would be
   ([software factory](software-factory.html#the-running-example-across-workflows)).

## Where it sits on the map

The spine belongs to the lifecycle band, the second band of the map. It is drawn under the phases
as a line of seven labelled nodes, captioned "traceability spine, linked by rule IDs". Above the
phases, a dashed arrow reads "incident feedback changes what Specification asks".

Each link is written in the phase of its workflow, from Specification through Deploy to Operate.
The [workflows](workflows.html) page describes what a workflow is, and the
[workflow catalog](workflow-catalog.html) lists each one with its phase.

In the core band, the [rule registry](rule-registry.html) holds the identifiers and the
[evidence schema](evidence-schema.html) holds the fields of each record. The spine is the chain
that reads both. Later workflows read the records of earlier ones, which the glossary calls the
[evidence hand-off](glossary.html#evidence-handoff), and the spine is that hand-off followed from
requirement to incident. The [software factory](software-factory.html) depends on the shared
identifiers for the same reason.

This page covers the release-to-incident link and the way the identifiers lead from an incident
back to the requirement and the specification that answered it, which is the route the map's
dashed arrow shows. The feedback path itself, this site's extension of Böckeler's steering
loop,[^bockeler-harness] is described in [harness engineering](harness-engineering.html) and on
the software factory page. The periodic review this site calls Inspect and Adapt, after SAFe's
event of that name,[^safe-inspect-and-adapt] reads what has landed; see
[Inspect and Adapt](inspect-and-adapt.html). One public anchor for the return path is NIST's
incident response profile, which feeds lessons learned from all activities back into the
Improvement category of its framework.[^nist-800-61r3] The assurance band reads the records for
audit and for their validity per revision, which this page does not cover.

## Pitfalls

- **An identifier is reused or reassigned.** A retired rule's code goes to a new rule, or numbers
  are recomputed after a reorganisation. Sign: the same identifier points at different content in
  different months. See [rule registry](rule-registry.html). OWASP's ASVS shows why the
  discipline matters: its requirement numbers may change between versions, so other documents are
  asked to cite the version, and an organisation-specific fork is encouraged only if it maintains
  traceability, so that passing a requirement means the same across all versions.[^owasp-asvs]
- **Links are written afterwards by hand.** The trace is assembled at the end, from memory and
  commit history. Sign: the trace is older than the change it describes. NASA's handbook asks for
  the matrix to be maintained throughout the life of the project,[^nasa-swe-052] and the
  commit-to-issue analysis cited above shows how incomplete links left to habit can
  be.[^rath-traceability-wild-2018] The recommended practice is to have the workflow that makes the
  artefact write the link.
- **Only the forward direction is checked.** Every requirement has a test, so the chain looks
  complete. Sign: tests nobody can tie to a requirement, the extra tests of the NASA
  statement.[^nasa-swe-052] The definition asks for both directions.[^gotel-finkelstein-1994]
- **A change is traced to a branch, not a revision.** A branch moves, so the link changes meaning.
  Sign: the record names a branch. See [evidence schema](evidence-schema.html).
- **An incident closes with no link upstream.** The review writes actions, but none reaches the
  stage that owns the gap. Sign: the same kind of miss recurs. Postmortem action items without
  clear ownership are less likely to be resolved, and the value of a postmortem is proportional to
  the learning it creates.[^google-sre-postmortem]
- **An agent's task-to-criterion mapping is accepted unchecked.** A mapping that looks complete is
  not a verified one. The catalog workflow concerned is
  [Task traceability and test planning](workflow-catalog.html#W12). Sign: no orphan check ran, or a
  `could_not_run` result was read as a pass, which the [workflows](workflows.html) page rules out.

## Related

- [Rule registry](rule-registry.html): where rule IDs are defined, kept stable and owned.
- [Evidence schema](evidence-schema.html): the fields of the record that carries rule IDs and
  revisions.
- [Workflows](workflows.html): the unit of work that writes each link.
- [Software factory](software-factory.html): the operating state that shared identifiers make
  possible.
- [Harness engineering](harness-engineering.html): the discipline that decides what a machine
  checks and what a person decides.
- [Specification](specification.html), [Design](design.html),
  [Develop, Build and QA](develop-build-qa.html), [Deploy](deploy.html), [Release](release.html)
  and [Operate](operate.html): the phases whose artefacts form the chain.
- [Definition of Ready and Definition of Done](definition-of-ready-and-done.html): the two gates
  the map marks on the phases. The Definition of Done is the Scrum Guide's
  term.[^scrum-guide-2020]
- [Inspect and Adapt](inspect-and-adapt.html): the review of what landed.
- [Validators](validators.html): the deterministic checks whose results carry rule IDs.
- [Evidence record](evidence-record.html): how audit, release and incident review read one record,
  valid for one revision.
- [Workflow catalog](workflow-catalog.html): rows
  [W04](workflow-catalog.html#W04), [W12](workflow-catalog.html#W12),
  [W13](workflow-catalog.html#W13), [W17](workflow-catalog.html#W17),
  [W23](workflow-catalog.html#W23), [W25](workflow-catalog.html#W25),
  [W26](workflow-catalog.html#W26), [W27](workflow-catalog.html#W27) and
  [W28](workflow-catalog.html#W28), named in the table above.
- Terminology: [traceability spine](glossary.html#traceability-spine),
  [rule registry](glossary.html#rule-registry), [evidence record](glossary.html#evidence-record),
  [evidence hand-off](glossary.html#evidence-handoff) and
  [feedback path](glossary.html#feedback-path).

## Sources

- The definition of requirements traceability: Gotel and Finkelstein.[^gotel-finkelstein-1994]
- Missing and extra tests, the six bi-directional pairs, how the matrix is built and maintained,
  and the class-based requirement: NASA's software engineering handbook.[^nasa-swe-052]
- Missing links in practice: the preprint of Rath and colleagues, on six open-source
  projects.[^rath-traceability-wild-2018]
- Stable, versioned identifiers: the OWASP Application Security Verification
  Standard,[^owasp-asvs] the OWASP Web Security Testing Guide[^owasp-wstg] and the NIST Secure
  Software Development Framework.[^nist-ssdf]
- Verifiable information about how an artefact was produced: SLSA provenance.[^slsa-provenance]
- Learning from incidents: the site reliability engineering workbook on
  postmortems[^google-sre-postmortem] and NIST's incident response profile.[^nist-800-61r3]
- Acceptance criteria: the ISTQB glossary.[^istqb-acceptance-criteria]
- The steering loop, which this site extends as the feedback path: Böckeler.[^bockeler-harness]
- Computational sensors, from which this site adapts validators: Böckeler.[^bockeler-sensors]
- Inspect and Adapt as an event: Scaled Agile, Inc.[^safe-inspect-and-adapt]
- The Definition of Done: Schwaber and Sutherland, the 2020 Scrum Guide.[^scrum-guide-2020]
- Which identifier links each pair, using rule IDs as the keys of the chain, writing each link as
  a by-product of the workflow that makes the artefact, the effect of agents on traceability, and
  checking both directions of the chain are this site's recommended practice; no public source
  states them.
