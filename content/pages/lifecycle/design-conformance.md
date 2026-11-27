---
id: design-conformance
type: workflow
band: lifecycle
map_box: design conformance
title: Design conformance
summary: The workflow that decides, before code is written, whether a planned technical approach is consistent with the architecture decisions, principles and constraints already on record for the system, and leaves a record that verification, release and incident review read later.
key_terms: [ai-sdlc, workflow, architecture-decision-record, fitness-function, consumer-driven-contract, rule-registry, project-configuration, evidence-record, could-not-run, failure-path, three-roles, export-example]
sources: [nygard-adr, tw-radar-adr, threat-modeling-manifesto, owasp-threat-modeling-cs, nist-ssdf, bockeler-harness, ford-evolutionary-architectures, fitness-function, thoughtworks-radar-fitness, robinson-cdc, nist-glossary-least-privilege, safe-system-architect, dora-metrics, bockeler-sensors, fowler-contract-test]
related: [design, spec-readiness, specification, pull-request-verification, release-readiness, incident-feedback, develop-build-qa, workflows, rule-registry, validators, engineering-kit, evidence-schema, harness-engineering]
review_record: content/reviews/1.6.0-lifecycle.md
---

## Decision

Is the technical approach proposed for this change consistent with the architecture decisions,
principles and constraints already recorded for the system? The workflow answers that once for each
revision of the plan. Its catalog entry is [W08](workflow-catalog.html#W08), and the phase it closes
is described on [Design](design.html); what else follows from the decision for the rest of the
change is set out there and in the row.

In an AI SDLC (the software development lifecycle with AI agents doing part of the work), the plan is
what an agent later builds from, so a departure that passes unnoticed here is repeated in code. The
decision judges the plan, not an implementation: no code exists yet. Public practice already treats
consistency with earlier decisions as something to check rather than to remember. Paula Paul and
Rosemary Wang describe fitness functions as describing "how close an architecture is to achieving an
architectural aim", giving continuous feedback for architectural conformance as development happens
rather than after the fact[^fitness-function].

## Trigger

A run starts when the author of a plan offers a revision of it for this decision, on a specification
that has already passed [Specification readiness](spec-readiness.html). A plan written against a
specification that has not passed carries that specification's open questions with it, so the run
does not start without the readiness record ([Design](design.html#gates-and-evidence)).

Two later events start a fresh run, and both are this site's recommended practice. The first is a new
revision of the plan; the earlier record stays with the earlier revision. The second is a change to a
recorded decision the plan relies on. Michael Nygard's architecture decision records are not deleted
when a decision is reversed: the old record is kept and marked superseded[^nygard-adr]. A plan that
rests on a record later marked superseded is therefore resting on a decision the team no longer holds,
and it is judged again.

## Inputs

The run reads the plan revision itself and the records against which it is judged.

- **The readiness record** for the specification revision the plan answers, written by
  [Specification readiness](spec-readiness.html).
- **The architecture decision records in force.** Each records one significant decision with its
  context, status and consequences, and records are numbered without reuse[^nygard-adr]. The
  Thoughtworks Technology Radar recommends keeping them in source control beside the
  code[^tw-radar-adr], which lets the run read the same set the code was built against.
- **The rules the plan touches**, read from their [Rule registry](rule-registry.html) entries,
  including how each rule is enforced ([Choosing a route](rule-registry.html#choosing-a-route)).
- **The project configuration**, which holds the project's own settings and the checks it has
  ([Engineering Kit](engineering-kit.html#project-configuration)).
- **The threat-model answers for the change.** The Threat Modeling Manifesto frames threat modelling
  around four questions: What are we working on? What can go wrong? What are we going to do about it?
  Did we do a good enough job?[^threat-modeling-manifesto] OWASP's cheat sheet says threat modelling
  is ideally performed early, such as during the design phase, and that a threat model is maintained
  and refined alongside the system[^owasp-threat-modeling-cs]. The plan is judged against the answers
  already given, not against a model written for the occasion.

In the customer-record export, the site's hypothetical feature that lets users export customer
records, the rule entries are R-042, the access rule on who may export which records, and R-017, the
volume limit for large exports.

## Agent task

The agent's part in this workflow is set in the catalog row [W08](workflow-catalog.html#W08) and is
not repeated here. How the agent, the checks and people divide the work is set out under
[the three roles](workflows.html#the-three-roles-agent-checks-and-people) on the Workflows page.

This page draws on no study of how well coding agents design, so what follows is recommended
practice, as on [Design](design.html#ai-assisted-practice). The agent prepares first versions of written design
material for a person to accept or reject, and sets the plan beside the decision records and rule
entries it reads, marking where the plan appears to depart from one. That comparison is advice.
Birgitta Böckeler notes that language models "can partially address problems that require semantic
judgment", but expensively and probabilistically, and that such checks catch problems sometimes, "but
not reliably enough to reduce supervision"[^bockeler-harness].

Independence has a public basis. NIST's Secure Software Development Framework (SSDF), task PW.2.1,
asks that "1) a qualified person (or people) who were not involved with the design and/or 2) automated
processes instantiated in the toolchain" review the software design to confirm that it meets all of
the security requirements and addresses the identified risk information[^nist-ssdf]. The bar is
non-involvement, and the framework allows automated review in the toolchain. As this site's
recommended practice, an agent that drafted the plan counts as involved in the design, so its
comparison never stands in for the independent review.

## Checks

A check here settles what a tool can decide from the plan and the records alone. It never settles
whether the approach is the right one.

**A recorded decision, stated precisely, becomes a check.** Neal Ford, Rebecca Parsons and Patrick Kua
introduced the architectural fitness function in *Building Evolutionary
Architectures*[^ford-evolutionary-architectures]; the Thoughtworks Technology Radar describes it as
"an objective integrity assessment of some architectural characteristics", which may draw on unit
tests, metrics and monitors[^thoughtworks-radar-fitness]. A decision that has become such a check
holds on every later change without being argued again. As recommended practice, when the run finds
that a plan adds a decision of that kind, the decision is noted as a candidate for a fitness function
on [Validators](validators.html#fitness-functions-for-architecture-rules)[^bockeler-sensors].

**One concern a tool can test at design time: interface contracts.** In Ian Robinson's
consumer-driven contracts, consumers' expectations of a service become tests that assert each
expectation, so contracts are "described and enforced in a repeatable, automated fashion with each
build"[^robinson-cdc]. When a plan proposes a change to an interface, running those expectations
against the proposed contract tells the provider, before anything is built, which consumer the change
would break. Applying this at design time is recommended practice.

**Each result is one of four.** A check ends passed, failed, skipped or could_not_run, the states
defined under [The could_not_run result](engineering-kit.html#the-could_not_run-result). Only an
explicit pass counts, and a check that never reports is not recorded as passed
([Evidence schema](evidence-schema.html#check-results)). As an example, and as recommended practice: if
the environment that runs consumers' contract tests[^fowler-contract-test] is unavailable, the contract check reports
could_not_run.

**What no check settles.** Whether an approach is right, given what it trades away, has no mechanical
test ([Design](design.html#ai-assisted-practice)). That judgment belongs to the catalog's
judgment-only [Design and architecture review](workflow-catalog.html#W24).

## Guardrails

The agent's permissions follow the [Workflows](workflows.html#the-three-roles-agent-checks-and-people)
page. They rest on least privilege, which NIST's glossary gives as restricting the access privileges
of users, or processes acting on behalf of users, to those needed for their assigned
work[^nist-glossary-least-privilege].

The run also stops in three cases, each this site's recommended practice and each with the reason it
cannot go on.

- **The plan depends on a question the specification left open.** The question goes back to the
  specification; it is not answered in the plan, for the reason the
  [Specification](specification.html#pitfalls) page gives under its pitfall on ambiguity settled in
  code.
- **The plan touches a rule that nothing checks.** A gate proves only what its check inspects
  ([Rule registry](rule-registry.html#owners-and-known-gaps)), so conformance to that rule cannot be
  shown by a result. The run stops and names the rule.
- **The plan would change a check together with the code that check examines.** Such a change goes
  to a person, as [Validators](validators.html#keeping-the-validator-honest) describes.

## Human decision

Who decides is set in the catalog row [W08](workflow-catalog.html#W08) and kept there. Where a person
reviews the design, SSDF task PW.2.1, quoted under Agent task, asks for a qualified person not
involved with the design[^nist-ssdf]; as recommended practice, the decider is therefore never the
plan's author. Frameworks give the accountability different titles; in SAFe, for
example, the System Architect is "responsible for defining and communicating a shared technical and
architectural vision"[^safe-system-architect].

The decider reads the plan revision, the decision records in force, the threat-model answers, the
check results and the agent's comparison, which is marked as advice. That set is recommended
practice.

The decider may reject any departure the agent marked, or accept one the agent missed. A departure
the decider accepts is not left implicit in the plan: it is recorded as a new decision record that
supersedes the old one, which is how Nygard's practice handles a reversed decision[^nygard-adr]. When
the people deciding disagree on a trade-off rather than on conformance, the question goes to the
judgment-only [Design and architecture review](workflow-catalog.html#W24).

## Outputs and evidence

The run leaves one record for the plan revision, in the shape the
[Evidence schema](evidence-schema.html) fixes: the check results, the agent's findings with the
decision on each, the decider's name and conclusion, and any decision records the run produced. New
and superseding architecture decision records sit beside the code, where later readers find
them[^tw-radar-adr].

### Who reads the record

- **[Pull-request verification](pull-request-verification.html)** reads it to judge code against the
  plan that was accepted, not against a plan as someone remembers it.
- **Task traceability and test planning** (catalog [W12](workflow-catalog.html#W12)) builds its tasks
  from the accepted plan.
- **[Release readiness](release-readiness.html)** reads it when it checks that the evidence for a
  release candidate is complete ([Evidence schema](evidence-schema.html#expected-checks-before-results)).
- **[Incident feedback](incident-feedback.html)** opens it when a production miss is traced back, to
  see whether the plan foresaw the case and who accepted it.
- **The workflow's owner** reads the records together for the measures below.

### In the customer-record export

On [Design](design.html#ai-assisted-practice), the volume-limit rule R-017 is checked by a 50k-row
load scenario rather than left to a sentence in the plan. This workflow adds a limit on what the
decision can see. It judges the plan, so it cannot catch the background worker's broader query, which
does not exist until code is written. That query is caught later, when the access validator for
R-042 fails on the first pull request ([Develop, Build and QA](develop-build-qa.html)). The design
record shows what the plan committed to; the verification record shows where the code departed from
it.

## Failure paths

The general failure paths every workflow shares are on [Workflows](workflows.html#failure-paths). For
this decision they take the following form, each with who acts next; the routing is recommended
practice.

- **A check fails.** The plan does not pass as it stands. Next: the plan's author revises it, and the
  revision starts a new run.
- **A check could not run.** The record cannot reach a positive status, and the result is not read as
  a fault in the plan. Next: the owner of the tool or environment restores it, and the check runs again
  on the same revision.
- **The agent stops.** The run halts on one of the cases under Guardrails. Next: the specification's
  owner for an open question; the rule's owner for a rule that nothing checks; the owner of the check
  for a plan that would change it.

## Measures

This page draws on no study of measuring design conformance, so each measure below is recommended
practice, is read against a baseline and carries no target value. DORA advises setting a baseline for current
performance and improving over time, and warns that metrics set as goals invite
gaming[^dora-metrics]; DORA says this of its own delivery metrics, and the site borrows it here by
analogy.

- **Design departures first found at pull-request review or later.** Findings that code breaks a
  recorded decision, where the plan already showed the departure. Fitness function-driven development aims for feedback "as it
  happens, rather than after the fact"[^fitness-function], and a falling count shows the departure
  is being found earlier. Baseline: the same team's count before the workflow ran.
- **Interface breaks found after merge.** Changes that broke a consumer's stated expectation once
  merged. Baseline: the count before the workflow ran.
- **Time from plan offered to recorded decision.** Baseline: the first period in which the workflow
  runs, read so that a growing wait is noticed before people route around it.

## Owner

One accountable owner answers for the workflow, distinct from the person who decides each run
([Workflows](workflows.html#definition)). As recommended practice, the owner is the person accountable
for the system's technical direction, who keeps the recorded decisions and principles current and
changes what the workflow checks.

## Related

- [Specification readiness](spec-readiness.html): the workflow whose record this one reads.
- [Pull-request verification](pull-request-verification.html): the workflow that judges code against
  the accepted plan.
- [Release readiness](release-readiness.html) and [Incident feedback](incident-feedback.html): later
  readers of the record.
- [Design](design.html): the phase this workflow closes; [Specification](specification.html) and
  [Develop, Build and QA](develop-build-qa.html): the phases on either side.
- Core: [Workflows](workflows.html), [Rule registry](rule-registry.html),
  [Validators](validators.html), [Engineering Kit](engineering-kit.html),
  [Evidence schema](evidence-schema.html) and [Harness engineering](harness-engineering.html).
- Workflow catalog: [W08](workflow-catalog.html#W08), API contract design
  [W09](workflow-catalog.html#W09), data model and migration plan [W10](workflow-catalog.html#W10),
  security design review [W11](workflow-catalog.html#W11), task traceability and test planning
  [W12](workflow-catalog.html#W12) and design and architecture review
  [W24](workflow-catalog.html#W24).

## Sources

- Architecture decision records: Michael Nygard[^nygard-adr] and the Thoughtworks Technology
  Radar[^tw-radar-adr].
- Fitness functions: Ford, Parsons and Kua[^ford-evolutionary-architectures], the Thoughtworks
  Technology Radar[^thoughtworks-radar-fitness] and Paul and Wang[^fitness-function].
- Interface contracts: Ian Robinson on consumer-driven contracts[^robinson-cdc].
- Threat modelling: the Threat Modeling Manifesto[^threat-modeling-manifesto] and OWASP's Threat
  Modeling Cheat Sheet[^owasp-threat-modeling-cs].
- Independent design review: NIST SP 800-218, SSDF version 1.1[^nist-ssdf].
- Agents' semantic review: Birgitta Böckeler on harness engineering[^bockeler-harness].
- Least privilege: the NIST glossary[^nist-glossary-least-privilege].
- Framework title for technical direction: Scaled Agile's System Architect
  page[^safe-system-architect].
- Baselines and targets: DORA's software delivery performance metrics[^dora-metrics].
- Validators as computational sensors: Birgitta Böckeler on maintainability
  sensors[^bockeler-sensors].
- Contract tests: Martin Fowler[^fowler-contract-test].
- The re-run triggers, the agent's comparison, the design-time contract check and its example, the
  stop cases, the decider's evidence set, the failure routing, the measures and the owner are this
  site's recommended practice; no public source states them.
