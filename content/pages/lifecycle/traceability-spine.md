---
id: traceability-spine
type: concept
band: lifecycle
map_box: Traceability spine
title: Traceability spine
summary: The chain of seven artefacts from requirement to incident, each pair linked by an identifier and checked for orphans, with rule IDs as the keys that tie checks, findings and decisions to it.
key_terms: [traceability-spine, rule-registry, evidence-record, evidence-handoff, feedback-path, could-not-run, validator, workflow, specification-readiness, software-factory, export-example]
sources: [gotel-finkelstein-1994, nasa-swe-052, rath-traceability-wild-2018, owasp-asvs, owasp-wstg, google-sre-postmortem, nist-ssdf, nist-800-61r3, slsa-provenance, bockeler-harness, bockeler-sensors, safe-inspect-and-adapt, istqb-acceptance-criteria]
related: [rule-registry, evidence-schema, workflows, software-factory, harness-engineering, specification, design, develop-build-qa, release, operate, definition-of-ready-and-done, inspect-and-adapt]
review_record: content/reviews/1.5.0-lifecycle.md
---

## Definition

Requirements traceability is, in Gotel and Finkelstein's definition, "the ability to describe and
follow the life of a requirement, in both a forwards and backwards direction (i.e., from its
origins, through its development and specification, to its subsequent deployment and use
...)".[^gotel-finkelstein-1994] On the map of the AI SDLC (the software development lifecycle with
AI agents doing part of the work), the *traceability spine* is that idea drawn as one line under
the phases. It is a chain of seven kinds of artefact: requirement, spec, task, test, change,
release and incident. An identifier links each artefact to the next, and rule IDs (see
[rule registry](rule-registry.html)) are the keys that tie checks, findings and decisions to the
chain. The idea is requirements traceability. The name "spine", and
the extension of the chain past release to the incident that follows it, are this site's
(adapted from Gotel and Finkelstein[^gotel-finkelstein-1994]).

## Why it matters

Each missing link has its own cost.

- **Requirement without a test.** The requirement ships on trust. Traceability can point out
  requirements that are not tested.[^nasa-swe-052]
- **Test without a requirement.** The test costs time to write, run and maintain, and nobody can
  say what it protects. The same source calls these extra tests.[^nasa-swe-052]
- **Change without a task or criterion.** The reviewer has no stated intent to judge the change
  against, so scope creep and unexplained edits pass as easily as intended ones.
- **Incident without a path to the specification.** The failure is fixed where it showed, and the
  gap that let it through stays open. See [software factory](software-factory.html) and
  [W28](workflow-catalog.html#W28).

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
   [develop, build and QA](develop-build-qa.html).
6. **Release.** The candidate revision, with its records, that is approved and deployed in
   [release](release.html).
7. **Incident.** An event in operation where the software departs from what was expected, handled
   in [operate](operate.html).

### The link between each adjacent pair

The table gives, for each pair, the identifier that links it, the workflow that writes the link and
what shows the link missing; see the [workflow catalog](workflow-catalog.html) and the
[evidence schema](evidence-schema.html).

| Pair | Linking identifier | Written by | Shows the link missing |
|---|---|---|---|
| Requirement to spec | The acceptance-criterion identifier | [Specification readiness](workflow-catalog.html#W04) | See [W04](workflow-catalog.html#W04) |
| Spec to task | The criterion identifier; see [W12](workflow-catalog.html#W12) | [Task traceability and test planning](workflow-catalog.html#W12) | See [W12](workflow-catalog.html#W12) |
| Task to test | The criterion identifier; see [W12](workflow-catalog.html#W12) and [W17](workflow-catalog.html#W17) | Task traceability and test planning; [Acceptance-test generation and execution](workflow-catalog.html#W17) | See [W12](workflow-catalog.html#W12) and [W17](workflow-catalog.html#W17) |
| Test to change | See [W13](workflow-catalog.html#W13) and the [evidence schema](evidence-schema.html) | [Task execution loop](workflow-catalog.html#W13); [Pull-request verification](workflow-catalog.html#W23) | See [W23](workflow-catalog.html#W23), [W13](workflow-catalog.html#W13) and the [evidence schema](evidence-schema.html) |
| Change to release | See [W25](workflow-catalog.html#W25) | [Release readiness](workflow-catalog.html#W25) | See [W25](workflow-catalog.html#W25) |
| Release to incident | See [W26](workflow-catalog.html#W26), [W27](workflow-catalog.html#W27) and [W28](workflow-catalog.html#W28) | [Deployment and post-deploy verification](workflow-catalog.html#W26); [Incident remediation](workflow-catalog.html#W27); [Incident-to-development feedback](workflow-catalog.html#W28) | See [W26](workflow-catalog.html#W26), [W27](workflow-catalog.html#W27) and [W28](workflow-catalog.html#W28) |

Read down the table, the identifiers change class. The upper half is keyed by criterion and task
identifiers, which exist before any code does. The lower half is keyed by revisions and by the rule
IDs on checks, findings and decisions, which exist because a run produced them. The criterion
identifier on a recorded test result is the join between the two halves.

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
tests)".[^nasa-swe-052] See [W12](workflow-catalog.html#W12).

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
rule IDs link checks, findings and decisions to one another and to the requirement they come from.
Using rule IDs as the keys of the spine is this site's own statement, set out on the
[rule registry](rule-registry.html) page. No public standard prescribes it.

See [rule registry](rule-registry.html), [evidence schema](evidence-schema.html) and
[validators](validators.html)[^bockeler-sensors].

Public identifier schemes show the same discipline. OWASP's Application Security Verification
Standard numbers its requirements by chapter, section and requirement, prefixes them with the
version when cited (`v<version>-<chapter>.<section>.<requirement>`), and encourages
organisation-specific forks provided they maintain traceability, so that passing a requirement
means the same across all versions.[^owasp-asvs] The OWASP Web Security Testing Guide, a community-created guide, gives each
test scenario an identifier in the form `WSTG-<category>-<number>`, for example
WSTG-INFO-02.[^owasp-wstg] NIST's Secure Software Development Framework version 1.1 identifies each
practice, for example PO.1.2, "Identify and document all security requirements for
organization-developed software to meet, and maintain the requirements over time", and RV.3,
"Analyze Vulnerabilities to Identify Their Root Causes".[^nist-ssdf] These are cited as examples
of stable identifiers, not as sources of a traceability requirement. They show how a requirement
or practice stays the same thing across documents, tools and versions.

Stable identifiers let each link be written at the moment its artefact is made. This site's
recommended practice is that the workflow producing an artefact records the link in its
[evidence record](glossary.html#evidence-record) as a by-product of the run, so the chain never has
to be rebuilt afterwards; the "Written by" column of the table above names the
[catalog](workflow-catalog.html) row that does this for each pair.

Public data on after-the-fact linking is narrow but points the same way. In the six open-source
projects analysed in the author preprint cited above, on average only 60% of the commits were
linked to specific issues.[^rath-traceability-wild-2018] That is a result about commit-to-issue
links in those projects. It shows how incomplete links can be, and it does not test the
recommendation.

### The customer-record export, left to right and back

The running example is a hypothetical feature that lets users export customer records. Its open
decisions are which records, which fields, how large an export may be, what happens on failure, and
how the feature is audited.

1. **Requirement to spec.** See [rule registry](rule-registry.html), [software factory](software-factory.html)
   and [W04](workflow-catalog.html#W04).
2. **Spec to task, task to test.** See [W12](workflow-catalog.html#W12) and
   [workflows](workflows.html).
3. **Test to change.** See [evidence schema](evidence-schema.html).
4. **Change to release.** See [workflows](workflows.html) and [W25](workflow-catalog.html#W25).
5. **Release to incident, and back.** See [software factory](software-factory.html) and
   [W28](workflow-catalog.html#W28).

## Where it sits on the map

The spine belongs to the lifecycle band, the second band of the map. It is drawn under the phases
as a line of seven labelled nodes, captioned "traceability spine, linked by rule IDs". Above the
phases, a dashed arrow reads "incident feedback changes what Specification asks".

Each link is written in the phase of its workflow; see the
[workflow catalog](workflow-catalog.html). The [workflows](workflows.html) page
describes what a workflow is, and the [workflow catalog](workflow-catalog.html) lists each one.

In the core band, the [rule registry](rule-registry.html) holds the identifiers and the
[evidence schema](evidence-schema.html) holds the fields of each record. The spine is the chain
that reads both. Later workflows read the records of earlier ones, which the glossary calls the
[evidence hand-off](glossary.html#evidence-handoff), and the spine is that hand-off followed from
requirement to incident. The [software factory](software-factory.html) depends on the shared
identifiers for the same reason.

This page covers the release-to-incident link and the link from the incident back to the change.
The feedback path itself[^bockeler-harness] is described in
[harness engineering](harness-engineering.html) and the software factory, and
[inspect and adapt](inspect-and-adapt.html)[^safe-inspect-and-adapt] reviews what has landed. One public anchor for the
return path: NIST's incident response profile feeds lessons learned from all activities back into
the Improvement category of its framework.[^nist-800-61r3] The assurance band reads the records for
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
  the matrix to be maintained throughout the life of the project,[^nasa-swe-052] and the six-project
  analysis of commit-to-issue links shows how incomplete links can be (on average only 60% of
  commits linked to issues).[^rath-traceability-wild-2018] The recommended practice is to have the
  workflow that makes the artefact write the link.
- **Only the forward direction is checked.** Every requirement has a test, so the chain looks
  complete. Sign: tests nobody can tie to a requirement, the extra tests of the NASA
  statement.[^nasa-swe-052] The definition asks for both directions.[^gotel-finkelstein-1994]
- **A change is traced to a branch, not a revision.** A branch moves, so the link changes meaning.
  Sign: the record names a branch. See [evidence schema](evidence-schema.html).
- **An incident closes with no link upstream.** The review writes actions, but none reaches the
  stage that owns the gap. Sign: the same kind of miss recurs. Postmortem action items without
  clear ownership are less likely to be resolved, and the value of a postmortem is proportional to
  the learning it creates.[^google-sre-postmortem]
- **An agent's task-to-criterion mapping is accepted unchecked.** See
  [W12](workflow-catalog.html#W12). A mapping that looks complete is not a verified one. Sign: no
  orphan check ran, or a `could_not_run` result was read as a pass; see [workflows](workflows.html).

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
  [Develop, build and QA](develop-build-qa.html), [Release](release.html) and
  [Operate](operate.html): the phases whose artefacts form the chain.
- [Definition of ready and done](definition-of-ready-and-done.html): the two gates the map marks
  on the phases.
- [Inspect and adapt](inspect-and-adapt.html): the review of what landed.
- [Validators](validators.html): the deterministic checks whose results carry rule IDs.
- [Workflow catalog](workflow-catalog.html): rows
  [W04](workflow-catalog.html#W04), [W12](workflow-catalog.html#W12),
  [W13](workflow-catalog.html#W13), [W17](workflow-catalog.html#W17),
  [W23](workflow-catalog.html#W23), [W25](workflow-catalog.html#W25),
  [W26](workflow-catalog.html#W26), [W27](workflow-catalog.html#W27) and
  [W28](workflow-catalog.html#W28).
- Terminology: [traceability spine](glossary.html#traceability-spine),
  [rule registry](glossary.html#rule-registry), [evidence record](glossary.html#evidence-record),
  [evidence hand-off](glossary.html#evidence-handoff) and
  [feedback path](glossary.html#feedback-path)[^bockeler-harness].

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
- The feedback path and the steering loop: Böckeler.[^bockeler-harness]
- Using rule IDs as the keys of the chain, writing each link as a by-product of the workflow that
  makes the artefact, the effect of agents on traceability, and checking both directions of the
  chain are this site's recommended practice; no public source states them.
