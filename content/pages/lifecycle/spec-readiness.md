---
id: spec-readiness
type: workflow
band: lifecycle
map_box: spec readiness
title: Specification readiness
summary: The workflow that decides whether a team can start planning from one revision of a specification, with every open question recorded and either settled or accepted as open by the person accountable for it, and leaves a readiness record.
key_terms: [ai-sdlc, specification-readiness, definition-of-ready, acceptance-criteria, testability, given-when-then, independent-basis, spec-driven-development, workflow, evidence-record, evidence-handoff, could-not-run, failure-path, harness-evaluation, rule-registry, export-example]
sources: [scrum-guide-2020, spec-kit-sdd, requirements-ambiguity-llm, istqb-acceptance-criteria, istqb-testability, fowler-given-when-then, nist-ssdf, owasp-asvs, dora-small-batches, agile-alliance-dor, dora-metrics, bockeler-harness, spec-kit, safe-inspect-and-adapt]
related: [specification, definition-of-ready-and-done, traceability-spine, intake-and-triage, design-conformance, pull-request-verification, incident-feedback, inspect-and-adapt, workflows, skills-and-evals, rule-registry, evidence-schema, engineering-kit]
review_record: content/reviews/1.6.0-lifecycle.md
---

## Decision

Can a team begin planning from this revision of the specification now, knowing exactly which
questions remain open? The workflow answers that once for each revision. Its catalog entry is
[W04](workflow-catalog.html#W04), and the phase it closes is described on
[Specification](specification.html#purpose).

"Ready" has a public anchor. The 2020 Scrum Guide says that Product Backlog items the Scrum Team can
complete within one Sprint "are deemed ready for selection in a Sprint Planning event"; the Guide
does not use the term Definition of Ready[^scrum-guide-2020], which is a team practice described
under [Definition of Ready](definition-of-ready-and-done.html#definition-of-ready).

In an AI SDLC (the software development lifecycle with AI agents doing part of the work), the
decision carries more weight, because an agent given a specification that is silent on a point still
produces something. One open-source spec-driven toolkit[^spec-kit] gives this as the reason its templates mark a
gap instead of filling it: doing so "prevents the common LLM behavior of making plausible but
potentially incorrect assumptions"[^spec-kit-sdd]. Settling such questions before planning, rather
than in code, is this site's recommended practice.

## Trigger

A run starts when someone asks for planning to begin on a named revision of a specification. The
request has to name the revision, because the record the run leaves speaks for that revision and no
other.

Two later events start a fresh run, and both are recommended practice. The first is a new revision
after acceptance. The earlier record stays attached to the earlier revision, as every evidence record
does (see [Evidence schema](evidence-schema.html#revisions-and-versions)), and the new revision is not
ready until its own run decides. The second is a lesson that adds a question for a kind of
specification: every specification of that kind that has not yet been planned is opened again so the
new question can be asked.

A run does not replace refinement. The Scrum Guide calls refinement "the act of breaking down and
further defining Product Backlog items" and treats it as ongoing[^scrum-guide-2020]. A run records
where refinement has reached at the moment planning is requested.

## Inputs

The run reads the change itself, earlier records and parts of the project's kit.

- **The specification revision and its acceptance criteria.** ISTQB defines acceptance criteria as
  "the criteria that a work product must satisfy to be accepted by the stakeholders"[^istqb-acceptance-criteria].
- **The intake record.** What was recorded when the work was taken in, by
  [Intake and triage](intake-and-triage.html) (catalog [W01](workflow-catalog.html#W01)).
- **The rule entries.** The [rule registry](rule-registry.html#what-an-entry-holds) entry for every
  rule the specification touches. For the customer-record export, the site's hypothetical feature
  that lets users export customer records, these are R-042, the access rule on who may export which
  records, and R-017, the volume limit for large exports.
- **The team's Definition of Ready.** No source cited on this site prescribes its contents; see
  [Definition of Ready](definition-of-ready-and-done.html#definition-of-ready).
- **Questions added by earlier lessons.** Questions that past misses added for specifications of this
  kind. They arrive by the feedback path described on
  [Harness engineering](harness-engineering.html#the-steering-loop-and-the-feedback-path)[^bockeler-harness].
- **The security requirements that apply.** NIST's Secure Software Development Framework, practice
  PO.1, asks that security requirements for software development be known at all times, so they can
  be taken into account throughout development and collected once and shared; task PO.1.2 asks an
  organisation to identify and document all security requirements for the software it develops and
  to maintain them over time[^nist-ssdf]. The OWASP Application Security Verification Standard is one
  public catalogue of such requirements for web applications and services. It can be filtered to the
  chapters that apply, and an organisation chooses its level from its own analysis of risk[^owasp-asvs].

## Agent task

What the agent looks for is set out in the catalog row [W04](workflow-catalog.html#W04) and is not
repeated here. How it works is this site's recommended practice, as
[Specification](specification.html#ai-assisted-practice) states it: the agent reads the specification
while it is still being written and raises questions, and a person answers them.

Public evidence on the reading is narrow. An industrial study presented at ICSME 2025 examined
language models detecting and explaining ambiguity in real-world industrial requirements. Giving the
model ten examples in the prompt classified ambiguous requirements better than giving none, and eight
industry experts evaluated what the models wrote[^requirements-ambiguity-llm]. The study does not show
that the practice improves delivery. The toolkit cited above builds the same caution into its
templates: wherever the prompt leaves something unspecified, they require a marker of the form
`[NEEDS CLARIFICATION: specific question]` in place of a guess ("Don't guess")[^spec-kit-sdd].

Two points of the agent's work matter most for this decision, both recommended practice.

- It marks a question and leaves the answer to a person. It can find that something is open; it
  cannot know what the business wants.
- Given a specification with a question still open, it stops and asks. For the export, the evaluation
  case "Access rule left open" on [Skills with evals](skills-and-evals.html) passes only when the agent
  asks instead of choosing an access rule itself.

## Checks

A check here decides what a tool can settle from the document alone. Checks confirm form; they never
confirm that the specification asks for the right thing
([Specification](specification.html#gates-and-evidence)). Which checks the workflow requires is set in
its catalog row; this section describes the properties that make a check usable in this decision.

**A marker can be found.** The toolkit's specification checklist, which it says acts as "unit tests"
for the specification, asks under requirement completeness, in this order, that no clarification
markers remain, that requirements are testable and unambiguous, and that success criteria are
measurable[^spec-kit-sdd]. Only the first can be decided by searching the text. As recommended
practice, it becomes a check, and the other two stay with people.

**A criterion has a checkable shape; whether it is testable stays a judgment.** ISTQB defines
testability as "the degree to which test conditions can be established for a component or system,
and tests can be performed to determine whether those test conditions have been
met"[^istqb-testability]. That degree is a judgment, so a tool looks only at form. Given, when, then
is one such form: Martin Fowler describes it as a style of representing tests in three parts (the state before
the behaviour, the behaviour being specified and the changes expected), developed by Daniel
Terhorst-North and Chris Matts as part of Behavior-Driven Development[^fowler-given-when-then].
Checking the shape is recommended practice; whether the criterion is the right one is a person's call.

**Every result is one of four.** Each check ends passed, failed, skipped or could_not_run, the results
defined under [The could_not_run result](engineering-kit.html#the-could_not_run-result). Could_not_run,
like failed, prevents a positive status. As an example, and as recommended practice: if the rule
registry cannot be read, the run cannot list the rules the specification touches, so a check that
depends on that list reports could_not_run, not passed.

## Guardrails

How a workflow's agent is limited is described on
[Workflows](workflows.html#the-three-roles-agent-checks-and-people). Two stop conditions are
particular to this decision.

**A rule the registry does not hold.** When the specification cites a rule with no registry entry, the
run stops and the gap goes to whoever maintains the registry. This is recommended practice: a rule
exists for the kit only once its entry is written and its owner accepts it
([Rule registry](rule-registry.html#entering-changing-and-retiring-rules)).

**An item too large to plan as one unit.** The run stops and the item goes back for splitting. Two
public sources point the same way. The Scrum Guide ties readiness to what can be completed within one
Sprint[^scrum-guide-2020], and DORA advises breaking work
into units "that can be completed independently and in short timeframes"[^dora-small-batches]. This
page sets no size limit; a team states its own in its Definition of Ready.

## Human decision

Who decides is set in the catalog row [W04](workflow-catalog.html#W04). What public sources and this
site's Core pages add is a set of accountabilities, each with its own basis.

The Scrum Guide makes the Product Owner accountable for creating and clearly communicating Product
Backlog items and for ensuring that the backlog is transparent, visible and understood. The Product
Owner may delegate that work and remains accountable for it[^scrum-guide-2020]. A question about what
the specification is for therefore goes to whoever holds that accountability.

The same Guide makes the Developers who will be doing the work responsible for sizing
it[^scrum-guide-2020]. Whether an item is small enough to plan as one unit is their call, not the
agent's.

Each rule in the [Rule registry](rule-registry.html#owners-and-known-gaps) has one accountable owner,
the person to ask about that rule. When an answer would depart from a rule, an exception, where the
rule allows one, is logged against the rule with who allowed it and when it lapses; some rules, such
as the access rule R-042, are never open to exception
([Rule registry](rule-registry.html#entering-changing-and-retiring-rules)).

When the decider rejects a question the agent raised, the rejection is recorded
with a reason chosen from a fixed list ([Evidence schema](evidence-schema.html#agent-findings-and-decisions)),
and those rejections feed the evaluation of the skill behind the agent
([Skills with evals](skills-and-evals.html)).

The decider may not accept while a required check has failed or reported could_not_run, and may not
accept an answer about R-042 that the rule does not allow: a readiness criterion tied to R-042 is met
only as written ([The export example](definition-of-ready-and-done.html#the-export-example)). Both
limits are recommended practice. The team, for its part, has a public basis for refusing an item: the
Agile Alliance lists among the benefits of a Definition of Ready an explicit agreement that allows a
team to push back on accepting ill-defined features[^agile-alliance-dor].

## Outputs and evidence

The run leaves a readiness record in the shape fixed by the [Evidence schema](evidence-schema.html).
Later workflows read the record instead of asking the same questions again, which is the
[evidence hand-off](glossary.html#evidence-handoff).

Open questions go into the record, not a conversation, for a reason the Scrum Guide gives:
transparency means the work is visible to those performing it and to those receiving it, and low
transparency can lead to decisions that diminish value and increase risk[^scrum-guide-2020]. SSDF
PO.1 gives a similar reason for security requirements: collected once and shared, they spare the
duplicated effort of gathering them again[^nist-ssdf].

The record has six readers.

- [Design conformance](design-conformance.html) (catalog [W08](workflow-catalog.html#W08)) plans
  from the accepted specification.
- [Pull-request verification](pull-request-verification.html) (catalog
  [W23](workflow-catalog.html#W23)) takes the criteria and rules as part of the
  [independent basis](glossary.html#independent-basis) it judges code against.
- Task traceability and test planning (catalog [W12](workflow-catalog.html#W12)) builds its tasks and
  tests from the criteria.
- The [Traceability spine](traceability-spine.html) keys its link from requirement to specification
  by the criterion identifiers the record holds.
- [Incident feedback](incident-feedback.html) (catalog [W28](workflow-catalog.html#W28)) reads it when
  a miss in production traces back to a question nobody asked.
- [Inspect and Adapt](inspect-and-adapt.html)[^safe-inspect-and-adapt], the periodic checkpoint,
  may change what readiness asks of a kind of specification.

In the export example, the first run's record shows the question the access rule turns on, which
roles may export which records, as open, and the specification as not ready. Once the answer is
written into the specification within R-042, the run on that new revision records the question as
settled before planning starts; [Software factory](software-factory.html) follows the item from
there. Later, after a scheduled full export within R-017's limit times out in production, readiness
asks every export-like specification for the largest export it expects
([The export example](definition-of-ready-and-done.html#the-export-example)). The record of the next
run on such a specification shows that question asked and answered before planning, where before the
incident it would not have appeared. The export's other open decisions (which records, which fields,
large exports, failure and audit) are not answered on this page.

## Failure paths

The general failure paths every workflow shares are on [Workflows](workflows.html#failure-paths) and
are not repeated here. For this decision, as recommended practice, two cases need stating.

When a required check fails, for example because a clarification marker is still in the text, the
specification is not ready. The question goes back to whoever is accountable for the item, as
described under Human decision, and a later revision gets its own run.

When a check reports could_not_run, for example because the rule registry cannot be read, the run
cannot show a positive status either. The fix belongs to whoever maintains the registry or the tool,
not to the specification's author. In both cases the record names the check that stopped the run.

## Measures

No public study measures this workflow. Every measure below is recommended practice, each is read
against a baseline, and none carries a target value. The baseline principle is borrowed by analogy:
DORA advises setting a baseline for an application's current performance and improving over time,
rather than competing against other teams[^dora-metrics]. DORA says this of its own delivery metrics,
not of specification readiness.

- **Agent questions accepted and rejected.** The share of each. Baseline: the skill's results on its
  evaluation cases for its current version ([Skills with evals](skills-and-evals.html)). It is an input
  to those evaluations, never a target.
- **Open questions carried into planning.** How many were accepted as open, and how many of those later
  changed the code. Baseline: the same counts over the first period in which the workflow runs.

## Owner

One accountable owner answers for the workflow itself, keeping its question sets and required checks
current, and is distinct from the people who decide each run
([Workflows](workflows.html#definition)). The Definition of Ready it applies has one named owner, a
person and never the agent whose work it judges, and owning it means keeping it current
([Who owns each](definition-of-ready-and-done.html#who-owns-each)). As recommended practice, the
workflow's owner adds a question for a kind of specification when a lesson arrives and decides which
checks are required. Who decides in a given run stays as the catalog row sets it.

## Related

- [Intake and triage](intake-and-triage.html): the workflow whose record this one reads.
- [Incident feedback](incident-feedback.html): the workflow through which a production miss adds a
  question to readiness.
- [Design conformance](design-conformance.html): the workflow that plans from the accepted
  specification.
- [Pull-request verification](pull-request-verification.html): the workflow that judges code against
  the accepted criteria and rules.
- [Specification](specification.html): the phase this workflow closes.
- [Definition of Ready](definition-of-ready-and-done.html#definition-of-ready): the team practice the
  workflow applies.
- [Traceability spine](traceability-spine.html): the chain of identifiers that starts with the
  acceptance criteria.
- [Inspect and Adapt](inspect-and-adapt.html): the checkpoint that may change what readiness asks.
- Core: [Workflows](workflows.html), [Skills with evals](skills-and-evals.html),
  [Rule registry](rule-registry.html), [Evidence schema](evidence-schema.html) and
  [Engineering Kit](engineering-kit.html).
- Workflow catalog: [Specification readiness](workflow-catalog.html#W04),
  [Design-to-specification handoff](workflow-catalog.html#W03),
  [Threat modeling](workflow-catalog.html#W06), [Spike](workflow-catalog.html#W07) and
  [Task traceability and test planning](workflow-catalog.html#W12).

## Sources

- Readiness for selection, refinement, accountabilities and transparency: the 2020 Scrum
  Guide[^scrum-guide-2020].
- The Definition of Ready and its benefits: the Agile Alliance glossary[^agile-alliance-dor].
- Clarification markers and checklists for specifications: an open-source spec-driven toolkit's
  description of its method[^spec-kit-sdd].
- Language models and ambiguous requirements: an industrial study presented at ICSME
  2025[^requirements-ambiguity-llm].
- Acceptance criteria, testability and the shape of a criterion: the ISTQB
  glossary[^istqb-acceptance-criteria][^istqb-testability] and Martin Fowler on given, when,
  then[^fowler-given-when-then].
- Security requirements: NIST's Secure Software Development Framework, version 1.1[^nist-ssdf], and the
  OWASP Application Security Verification Standard[^owasp-asvs].
- Batch size and baselines: DORA's pages on working in small batches[^dora-small-batches] and on
  software delivery performance metrics[^dora-metrics].
- The steering loop: Birgitta Böckeler on harness engineering[^bockeler-harness].
- Spec-driven development: the open-source toolkit the glossary credits with the term[^spec-kit].
- Inspect and Adapt: Scaled Agile, Inc.'s page on the event[^safe-inspect-and-adapt].
