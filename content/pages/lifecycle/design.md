---
id: design
type: phase
band: lifecycle
map_box: Design
title: Design
summary: Design settles how a specified change is to be built and records the decisions and trade-offs behind that approach; an agent prepares first versions of the written design, while trade-off judgments stay with people.
key_terms: [ai-sdlc, risk-tier, rule-registry, rule-route, gate, fitness-function, architecture-decision-record, project-configuration, consumer-driven-contract, contract-test, workflow, three-roles, evidence-record, export-example]
sources: [bockeler-sensors, sei-atam, sei-atam-2000, nygard-adr, threat-modeling-manifesto, owasp-threat-modeling-cs, nist-ssdf, fowler-evodb, fowler-blue-green, robinson-cdc, fowler-contract-test, istqb-rbt, owasp-asvs, ford-evolutionary-architectures, fitness-function, spec-kit-sdd, bockeler-harness, safe-system-architect, safe-art, scrum-guide-2020]
related: [specification, develop-build-qa, definition-of-ready-and-done, workflows, rule-registry, engineering-kit, harness-engineering, evidence-schema, validators, design-conformance]
review_record: content/reviews/1.5.0-lifecycle.md
---

## Purpose

Design is the phase in which an accepted specification becomes a plan for building it. The phase
chooses a technical approach, weighs what that approach trades away, and records the decisions taken
so that a later reader can see what was chosen and why. Its central decision is [design conformance](design-conformance.html)
([W08](workflow-catalog.html#W08)), which the workflow catalog titles Plan and architecture
conformance.

In the AI SDLC (the software development lifecycle with AI agents doing part of the work), the plan
is also what an agent builds from. Whatever the plan leaves open, an agent building from it decides
on its own, so settling the approach in the plan is recommended practice. The site's account of
[risk tiers](glossary.html#risk-tier), which the phase works with, is under
[Risk tiers: same definition, different cost](workflows.html#risk-tiers-same-definition-different-cost)
on the Workflows page.

## Traditional practice

Without agents, people settle design in documents and review meetings. The practices that hold up
best leave a record that a later reader can check.

**Trade-offs.** The Software Engineering Institute's Architecture Tradeoff Analysis Method (ATAM)
is "a structured technique for understanding the tradeoffs inherent in the architectures of
software-intensive systems"[^sei-atam]; its 2000 description includes a step in which scenarios
are brainstormed and then prioritised by voting[^sei-atam-2000].

**Recording decisions.** Michael Nygard's architecture decision records capture one significant
decision each, with its context, the decision, its status and its consequences. They are numbered
in sequence, and a reversed decision is kept and marked superseded rather than
edited[^nygard-adr].

**Security design.** The Threat Modeling Manifesto's working group poses four questions: What are
we working on? What can go wrong? What are we going to do about it? Did we do a good enough
job?[^threat-modeling-manifesto] OWASP's cheat sheet breaks threat modeling into four basic steps:
application decomposition, threat identification and ranking, mitigations, and review and
validation[^owasp-threat-modeling-cs]. NIST's Secure Software Development Framework (SSDF),
version 1.1, asks teams to "use forms of risk modeling – such as threat modeling, attack modeling,
or attack surface mapping" (task PW.1.1)[^nist-ssdf].

**Independent review.** The same framework asks that a qualified person, or people, who were not
involved with the design review the software design (task PW.2.1)[^nist-ssdf].

**Security requirements.** SSDF task PO.1.2 asks that security requirements be identified and
documented and maintained over time[^nist-ssdf]. Design reads them as an input: the security design
is the team's answer to them.

**Data design.** Evolutionary database design represents every change to the database as a
migration script, version-controlled together with the application code changes[^fowler-evodb].
Fowler's description of blue-green deployment adds that the trick is to separate the deployment of
schema changes from application upgrades[^fowler-blue-green].

**Contracts.** In Ian Robinson's consumer-driven contracts, the consumers of a service state their
expectations, the provider is checked against them, and the service can then change without
breaking its consumers[^robinson-cdc]. Martin Fowler's contract tests check that a test double
still behaves like the real outside service it stands in for[^fowler-contract-test]. Agreeing an
interface before either side builds against it is recommended practice rather than a cited
standard.

**Proportion.** Effort scales with risk. Risk-based testing bases the management, selection,
prioritisation and use of test activities and resources on risk types and risk
levels[^istqb-rbt]. OWASP's Application Security Verification Standard (ASVS) gives a published
precedent for choosing a level of rigour by risk: an organisation should analyse its risks and
decide what level it should be at, where level 1 holds the minimum requirements, level 2 is what
most applications should strive for, and level 3 is for applications that need to demonstrate the
highest levels of security[^owasp-asvs].

**Executable architecture.** Architecture goals written as executable checks are fitness
functions: objective assessments of how well a system keeps an architectural characteristic,
carried out through tests, metrics and similar
mechanisms[^ford-evolutionary-architectures][^fitness-function]. They let a structural decision
made at design time be checked on every later change.

## AI-assisted practice

What changes first is who writes the first version. No public study was found that measures how
well coding agents design, so this section
describes recommended practice, not a finding. In that practice an agent prepares first versions of
the phase's written material, such as candidate decision records, first answers to the
threat-modeling questions and proposed interface or schema changes, each for a person to accept or
reject. The agent's part in the central decision belongs to design conformance
([W08](workflow-catalog.html#W08)) and is not restated here; what follows is how the work divides
among the site's [three roles](workflows.html#the-three-roles-agent-checks-and-people) of agent,
checks and people.

**Constraints on the drafting.** Rules can bind the agent while it writes. One open-source
spec-driven toolkit gives the agent a constitution of principles that includes a simplicity gate and
an anti-abstraction gate, and states that the model "cannot proceed without either passing the
gates or documenting justified exceptions" in a section that tracks complexity[^spec-kit-sdd]. A
departure then has to be argued in writing instead of entering the plan unnoticed.

**What moves to a deterministic check.** A design decision that can be stated precisely can be
checked by a machine on every later change instead of being remembered. Fitness functions turn an
architectural goal into such a check[^ford-evolutionary-architectures][^fitness-function], and in
consumer-driven contracts the consumers' stated expectations of an interface become tests the
provider is run against[^robinson-cdc]. As recommended practice, each design decision that can be
written as a check is written as one, so that the decision holds whether or not an agent that later
builds from the plan has read the reasoning behind it. In the customer-record export, the
volume-limit rule R-017 is checked by a 50k-row load scenario rather than left to a sentence in the
plan (see [Validators](validators.html)).

**What stays with a person.** Whether an approach is right, given what it trades away, has no
mechanical test. Birgitta Böckeler notes that inferential sensors, which use a model to judge the
work, address semantic concerns only partially[^bockeler-harness], so an agent's review of a design
is advice to the person who decides and never an approval (see [Workflows](workflows.html)). The catalog keeps the
trade-off decision as a judgment-only workflow,
[Design and architecture review](workflow-catalog.html#W24), which stays with a person. As
recommended practice, an agent that drafted a plan counts as involved in the design in the sense of
SSDF task PW.2.1[^nist-ssdf], so it cannot serve as the independent reviewer of that plan.

## Workflows in this phase

The workflow catalog uses its own phase names. The rows for this phase sit under the catalog's
phase 2, "Plan & design":

- [Plan and architecture conformance](workflow-catalog.html#W08) (see the [Design conformance](design-conformance.html) page): the phase's central decision,
  which the map draws as the bar labelled "design conformance".
- [API contract design](workflow-catalog.html#W09),
  [Data model and migration plan](workflow-catalog.html#W10) and
  [Security design review](workflow-catalog.html#W11): specialist decisions within the phase.
- [Task traceability and test planning](workflow-catalog.html#W12): the last row of the catalog
  phase, where design meets the build.

One further decision about design sits elsewhere in the catalog.
[Design and architecture review](workflow-catalog.html#W24) is filed under the catalog's phase 5,
"Review". It is judgment-only and stays with a person.

## Gates and evidence

**Entry.** Design starts from a specification that has passed its readiness decision,
[Specification readiness](workflow-catalog.html#W04). The [Specification](specification.html) page
describes that phase and the readiness criteria behind it. A plan written against a specification
that has not passed inherits its open questions.

**Exit.** The phase ends with the design conformance decision ([W08](workflow-catalog.html#W08); see the [Design conformance](design-conformance.html) page),
taken by a named person; what that decision covers is set out in its catalog row. The exit leaves an
evidence record in the common shape the [Evidence schema](evidence-schema.html) sets.

**Decision records.** A significant design decision leaves an architecture decision record; when a
later change reverses it, the old record stays, marked superseded[^nygard-adr].

**Review records.** As recommended practice, the independent design review that the SSDF asks
for[^nist-ssdf] leaves an evidence record naming the reviewer, the conclusion and the revision of the
plan reviewed. The [Evidence schema](evidence-schema.html) fixes the fields; this page adds none.

## Roles

Who owns the plan and who decides at each of the phase's gates is recorded in the catalog rows
linked above, so the assignment is kept in one place. Each [workflow](workflows.html) has one
accountable owner, and every decision is recorded under the name of the person who made it.

Public frameworks set two accountabilities that bear on the phase. The SSDF asks that the design be
reviewed by a qualified person, or people, who were not involved with it[^nist-ssdf], which keeps
the author of a design and its reviewer apart. In SAFe, the system architect is "responsible for
defining and communicating a shared technical and architectural vision for the solutions developed
by an ART"[^safe-system-architect], that is, by an Agile Release Train[^safe-art].

## Pitfalls

- **The agent's summary taken as the design review.** Sign: the review record holds the agent's
  summary and an approval, and nothing of the reviewer's own. See the pitfalls in
  [Workflows](workflows.html#pitfalls).
- **Complexity the change does not need.** A plan adds layers, abstractions or options that no
  requirement asks for. The simplicity and anti-abstraction gates of the toolkit cited above, with
  justified exceptions written down, are one public answer[^spec-kit-sdd]; treating unrequested
  structure as a finding is recommended practice. Sign: a new abstraction with no recorded reason.
- **A schema or interface change made without its safeguards.** Sign: a schema change ships in the same
  deployment as the code that needs it, against the advice to deploy the two
  separately[^fowler-blue-green]; a migration exists only as a manual step rather than as a
  versioned script beside the code[^fowler-evodb]; or a provider changes an interface without
  checking its consumers' stated expectations[^robinson-cdc].
- **Decisions left unrecorded.** Sign: the same design argument returns on later changes, and nobody
  can find why the current approach was chosen. A short decision record per significant choice, kept
  and superseded rather than edited[^nygard-adr], is the recommended practice.

## Related

- [Specification](specification.html): the phase before Design, whose accepted specification is
  Design's input.
- [Develop, Build and QA](develop-build-qa.html): the phase after Design, where the checks run.
- [Definition of Ready and Definition of Done](definition-of-ready-and-done.html): the entrance and
  exit criteria around the phases. The Definition of Done is the Scrum Guide's formal description of
  the state of the Increment when it meets the quality measures required for the
  product[^scrum-guide-2020].
- [Workflows](workflows.html): the decision unit, the three roles and how
  [risk tiers](workflows.html#risk-tiers-same-definition-different-cost) work.
- [Rule registry](rule-registry.html): rules and their routes.
- [Engineering Kit](engineering-kit.html): the project configuration that holds which checks run.
- [Harness engineering](harness-engineering.html): computational and inferential controls.
- [Validators](validators.html): the deterministic checks that hold design decisions on later
  changes.
- [Evidence schema](evidence-schema.html): the fixed shape of every evidence record.
- [Design conformance](design-conformance.html): whether a planned approach fits the decisions already on record.
- Workflow catalog rows [W08](workflow-catalog.html#W08), [W12](workflow-catalog.html#W12) and
  [W24](workflow-catalog.html#W24).
- Terminology: [Risk tier](glossary.html#risk-tier).

## Sources

- Trade-off analysis: the SEI's 1998 ATAM report[^sei-atam] and its 2000 report, cited for scenario
  prioritisation[^sei-atam-2000]. Decision records: Michael Nygard[^nygard-adr].
- Security design and independent review: the Threat Modeling Manifesto[^threat-modeling-manifesto],
  OWASP's Threat Modeling Cheat Sheet[^owasp-threat-modeling-cs] and NIST SP 800-218, SSDF version
  1.1[^nist-ssdf].
- Data and contracts: Sadalage and Fowler on evolutionary database design[^fowler-evodb], Fowler on
  blue-green deployment[^fowler-blue-green], Ian Robinson on consumer-driven
  contracts[^robinson-cdc] and Fowler on contract tests[^fowler-contract-test].
- Scaling effort to risk: the ISTQB glossary[^istqb-rbt] and OWASP ASVS 5.0.0[^owasp-asvs].
- Fitness functions: Ford, Parsons and Kua[^ford-evolutionary-architectures] and Paul and
  Wang[^fitness-function].
- Agents and controls: an open-source spec-driven toolkit[^spec-kit-sdd] and Birgitta Böckeler on
  harness engineering[^bockeler-harness].
- SAFe: Scaled Agile's System Architect page[^safe-system-architect] and its Agile Release Train
  page[^safe-art].
- Definition of Done: the 2020 Scrum Guide by Ken Schwaber and Jeff Sutherland[^scrum-guide-2020].
- Validators: this site's adaptation of Birgitta Böckeler's computational sensors[^bockeler-sensors].
