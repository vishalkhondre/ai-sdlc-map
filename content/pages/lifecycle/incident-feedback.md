---
id: incident-feedback
type: workflow
band: lifecycle
map_box: incident feedback
title: Incident feedback
summary: The workflow that starts from a reviewed incident or a failure found in production, follows the records back from the running release, and decides which earlier control changes and who owns that change until it has landed.
key_terms: [feedback-path, steering-loop, traceability-spine, evidence-record, evidence-handoff, could-not-run, rule-registry, harness-evaluation, workflow, three-roles, failure-path, export-example, postmortem, regression-testing]
sources: [incident-sre-book-postmortem, google-sre-postmortem, incident-istqb-failure, incident-istqb-defect, incident-istqb-confirmation-testing, incident-istqb-regression-testing, incident-owasp-logging, nist-ssdf, nist-800-61r3, google-agentic-sre, ahmed-incident-llm, chen-rcacopilot, fowler-selftesting, dora-metrics, dora-streamlining-change-approval, sre-book-managing-incidents, gotel-finkelstein-1994, nasa-swe-052, bockeler-harness, bockeler-sensors, safe-inspect-and-adapt]
related: [operate, traceability-spine, inspect-and-adapt, workflows, evidence-schema, rule-registry, skills-and-evals, harness-engineering, software-factory, release-readiness, deploy-verification, pull-request-verification, spec-readiness, design-conformance]
review_record: content/reviews/1.6.0-lifecycle.md
---

## Decision

Which earlier control changes because of this incident or production failure, and who answers for
that change until it has landed? In the AI SDLC (the software development lifecycle with AI agents
doing part of the work), a workflow is one delivery decision run end to end, with checks, a named
human decision, an evidence record and one owner (see [workflows](workflows.html)); this page
describes the workflow that carries a lesson out of production, whose catalog entry is
incident-to-development feedback, [W28](workflow-catalog.html#W28).

The decision exists because a review alone changes nothing. The site reliability engineering (SRE)
book counts among the primary goals of a postmortem "that effective preventive actions are put in
place to reduce the likelihood and/or impact of recurrence",[^incident-sre-book-postmortem] and the
SRE workbook puts the same point from the user's side: "a postmortem without subsequent action is
indistinguishable from no postmortem".[^google-sre-postmortem] The workbook's line that the value of
a postmortem is proportional to the learning it creates is discussed on [Operate](operate.html#learning-after-the-incident).[^google-sre-postmortem]

This workflow begins once service is back. Restoring service while the incident is open, including
a rollback or a fix made on the spot, is incident remediation, [W27](workflow-catalog.html#W27),
described with its phase on [Operate](operate.html).

## Trigger

A run starts when the postmortem of an incident has been reviewed. The SRE book is blunt about the
review step: "An unreviewed postmortem might as well never have existed", and once reviewed, the
postmortem is "added to a team or organization repository of past incidents".[^incident-sre-book-postmortem]
Treating that reviewed record as the start of a run is this site's recommended practice; the book
describes the review and the repository, not a workflow that follows them.

A failure can also reach users without an incident being declared. The ISTQB glossary defines a
failure as "an event in which a component or system does not meet its requirements within specified
limits during its execution",[^incident-istqb-failure] and a defect as "an imperfection or deficiency
in a work product where it does not meet its requirements or specifications or impairs its intended
use".[^incident-istqb-defect] A failure seen in production and traced to a defect that every earlier
check let through, which this page calls an escaped defect, starts a run in the same way. No public glossary
read for this page defines "escaped defect", so the term is used here in its plain sense only.

Security findings arrive by their own route. NIST's Secure Software Development Framework (SSDF)
asks producers to "analyze identified vulnerabilities to determine their root causes" (RV.3.1) and
to review the development process and update it "to prevent (or reduce the likelihood of) the root
cause recurring" (RV.3.4).[^nist-ssdf] A vulnerability reaches this workflow at that second step;
fixing the vulnerability itself is vulnerability response, [W29](workflow-catalog.html#W29).

In the customer-record export, a hypothetical feature that lets users export customer records, the
run starts when the postmortem of a timed-out scheduled full export has been reviewed. The open
incident itself never starts a run.

## Inputs

The run needs records that already exist. Each comes from a workflow earlier in the lifecycle, so
the run reads them and does not rebuild them.

- **The incident record and its reviewed postmortem.** The SRE book defines a postmortem as "a
  written record of an incident, its impact, the actions taken to mitigate or resolve it, the root
  cause(s), and the follow-up actions to prevent the incident from recurring".[^incident-sre-book-postmortem]
- **The release record**, which names the release that was running, from
  [Release readiness](release-readiness.html).
- **The deployment record** for that release, from [Deploy verification](deploy-verification.html).
- **The verification records** of the changes the release contains, from
  [Pull-request verification](pull-request-verification.html).
- **The readiness record** of the specification those changes answered, from
  [Specification readiness](spec-readiness.html).
- **The rule registry entries** the trace passes through, with their owners and known gaps
  ([rule registry](rule-registry.html)), and the evaluation cases that already cover the area
  ([skills with evals](skills-and-evals.html)).

What joins these records is the [traceability spine](traceability-spine.html#the-link-between-each-adjacent-pair):
each record carries the identifier of the next, so the chain can be read from the incident back to
the requirement. That backward reading is part of what requirements traceability means in Gotel and
Finkelstein's definition, which follows a requirement's life "in both a forwards and backwards
direction",[^gotel-finkelstein-1994] and some regulated work requires it, as NASA's software
engineering handbook does for listed pairs of products.[^nasa-swe-052]

A link that cannot be followed is an input too. A record with no link on one side is an orphan (see
[orphans in both directions](traceability-spine.html#orphans-in-both-directions)), and the run
records it as a finding of its own before going on.

For the export, the incident record names the running release, and from there the run reaches the
verification record of the revision that shipped, its results for the volume-limit rule R-017, and
the readiness record of the export specification. The walk itself is set out on the
[traceability spine](traceability-spine.html#the-customer-record-export-left-to-right-and-back) page.

## Agent task

The catalog row states the agent's task ([W28](workflow-catalog.html#W28)). Public accounts show what
agents already do around incidents. Google's SRE organisation describes agents that consolidate and
summarise data from incident communication, create handoff documents and "automatically create drafts
of incident postmortems". Its investigation agents use observability data and system topology,
taxonomy and dependency data "before they can proceed to form hypotheses and propose mitigation
steps".[^google-agentic-sre] It is one operator's account, it reports no outcome figures, and it does
not say that its agents propose root causes.

Research has gone further on causes. A study presented at ICSE 2023 evaluated large language models
for helping engineers root-cause and mitigate production incidents, on more than 40,000 incidents,
with human evaluation by the incidents' owners.[^ahmed-incident-llm] A preprint describes a tool that
predicts an incident's root-cause category with an explanatory narrative and reports accuracy of up
to 0.766 on a year of incidents from its authors' own cloud provider.[^chen-rcacopilot] Both were
evaluated on their authors' own data, so neither says how well such a tool works elsewhere.

On that basis, and as recommended practice, the agent's part in this workflow is preparation: it
gathers the records along the spine into one view for the people who decide, marks any link it could
not follow, and offers a cause as a hypothesis. The same Google account says agents "must be able to
explain and reason about why and how they performed an action, as well as what options were
considered and rejected",[^google-agentic-sre] so the hypothesis carries its reasoning and the
alternatives the agent set aside.

The agent does not confirm a cause, assign an owner, close an action or edit the control the lesson
points at. It proposes the change, and the owner of that control makes it. It holds none of the
incident roles named on [Operate](operate.html#roles). These limits are recommended practice; no
public source sets them.

## Checks

The catalog row has its own check ([W28](workflow-catalog.html#W28)). The properties below are ones
a tool can settle the same way on every run.

- **Every action has an owner and a tracking number.** The SRE workbook's annotated example of a
  better postmortem asks that all action items have both an owner and a tracking number, and the
  chapter notes that actions without clear owners are less likely to be
  resolved.[^google-sre-postmortem] A tool can read it from the tracker. As recommended practice,
  the result is failed while any action has no owner, and the review stays open, as
  [Operate](operate.html#gates-and-evidence) also recommends.
- **Every action states a verifiable end state.** The same example asks for one, and the workbook warns
  that unclear language "makes it difficult to measure and understand success criteria".[^google-sre-postmortem]
  Checking that each action names how its completion will be shown is recommended practice.
- **The trace is complete.** The evidence record links the incident to the running release and on to
  the upstream change it produces, with no orphan on the way (see the
  [traceability spine](traceability-spine.html#orphans-in-both-directions)). As recommended
  practice, a failed result does not stop the run, but the run does not close until each gap is
  recorded with its owner.
- **The miss has a test.** Martin Fowler's practice on a bug found in production is to "write a test
  that exposes the bug, and only then to try to fix it", because "once the bug is fixed it stays
  fixed".[^fowler-selftesting] The ISTQB glossary separates two kinds of change-related testing that
  follow: confirmation testing, to confirm "that a failure caused by that defect does not reoccur",[^incident-istqb-confirmation-testing]
  and regression testing, to detect whether defects have been introduced or uncovered in unchanged
  areas.[^incident-istqb-regression-testing] A tool can confirm that such a test exists, names the
  rule it guards and has a recorded result.

Every result takes one of the states the [evidence schema](evidence-schema.html#check-results)
defines. A reproduction that cannot be carried out is recorded as
[`could_not_run`](glossary.html#could-not-run), never as passed (see Failure paths).

## Guardrails

**Blameless by construction.** The SRE book says a blameless postmortem must "focus on identifying
the contributing causes of the incident without indicting any individual or team for bad or
inappropriate behavior", and "assumes that everyone involved in an incident had good
intentions".[^incident-sre-book-postmortem] The workbook adds that action items "are aimed at
improving the system instead of improving people".[^google-sre-postmortem] As recommended practice,
the agent writes in the same terms: roles, conditions and controls, never a person's name as the
cause.

**Data stays where it is.** Incident data can hold the very records the product protects; for the
export, logs from the failed run may contain customer records. OWASP's logging guidance says
sensitive personal data "should usually not be recorded directly in the logs" and "should be
removed, masked, sanitized, hashed, or encrypted", and that privileges to read log data "should be
restricted and reviewed periodically".[^incident-owasp-logging] As recommended practice, the agent
reads only what its task's permissions grant, and the evidence record points to the incident data
by reference instead of copying it.

**No hand on production.** During an incident, the SRE book confines changes to the operations
team.[^sre-book-managing-incidents] This workflow runs after the incident and has no reason to touch
production at all; its agent holds no write access there, in line with the permission model on
[Operate](operate.html#what-deterministic-checks-hold).

**Stop at another owner's rule.** When the trace reaches a rule, the rule's owner approves any change
to it ([owners and known gaps](rule-registry.html#owners-and-known-gaps)). The run stops and hands
the proposal over; it does not edit the entry. Any proposal that touches R-017 goes to that rule's
owner in the registry.

**Change a control, not the amount of process.** DORA lists "responding to problems by adding more
process" as a pitfall, because it "drives up lead times and batch sizes, creating a vicious cycle",
and advises investing instead "in making it quicker and safer to make changes".[^dora-streamlining-change-approval]
As recommended practice, a run that can only propose a new approval step has not found its control
yet.

## Human decision

The catalog row names who chooses the change ([W28](workflow-catalog.html#W28)). The deciders read
three things: the trace along the spine, the agent's hypothesis marked as a hypothesis, and the
actions from the reviewed postmortem. As recommended practice, a person confirms the cause before it
changes anything upstream, for the reasons given under
[pitfalls on Operate](operate.html#pitfalls).

Public practice puts the approval of actions with people who know the service. The SRE workbook's
checklist asks that action items be "vetted and approved by the technical leads of the
service".[^google-sre-postmortem] This page cites that as one public example, not as a role it
requires.

Two limits hold whoever decides. A change to a rule is for that rule's named owner
([rule registry](rule-registry.html)): for the export, anything touching the access rule R-042 goes
to the security owner, and R-042 is not open to exception. And the deciders may reject the agent's
hypothesis; the rejection is recorded as a decision with its reason, in the form the
[evidence schema](evidence-schema.html#agent-findings-and-decisions) gives decisions, so later runs
and the review skill's tuning can learn from it[^bockeler-sensors]. That recording is recommended practice.

For security incidents, NIST SP 800-61 Revision 3 feeds "lessons learned from performing all
activities in all Functions" into its Improvement category, and its ID.IM-03 outcome reads
"Improvements are identified from the execution of operational processes, procedures, and
activities".[^nist-800-61r3] The decision on this page is where such an improvement gets an owner.

## Outputs and evidence

The run writes one [evidence record](glossary.html#evidence-record) in the shape the
[evidence schema](evidence-schema.html) fixes, and adds no field to it. The record links the
incident, the running release and the upstream change it decided on, names that change's owner,
holds the check results above, and keeps the decisions with their reasons. The SRE book's repository
of reviewed postmortems is the public precedent for keeping such records together where later
reviews can find them.[^incident-sre-book-postmortem]

The actions themselves live in a tracker. The workbook describes action items filed as bugs in a
centralised tracking system and warns that "without a formal tracking process, action items from
postmortems are often forgotten".[^google-sre-postmortem] The evidence record points to those
items; it does not replace them. For security incidents, NIST's profile also asks for an
after-action report that documents the incident and the response and recovery actions
taken.[^nist-800-61r3]

Four readers use the record, each for a different question. This reader set is recommended
practice.

- **The owner of the workflow where the change lands**, for example
  [Specification readiness](spec-readiness.html) or
  [Pull-request verification](pull-request-verification.html), reads what is changing in their
  workflow, why, and by when.
- **The owner of each rule** the trace reached ([rule registry](rule-registry.html)) reads the
  proposal that awaits their decision.
- **[Inspect and Adapt](inspect-and-adapt.html)**,[^safe-inspect-and-adapt] the periodic checkpoint, reads whether each
  lesson landed.
- **The next incident review** reads whether a similar miss was seen before and what was done about
  it.

## Failure paths

The general responses to a failed or missing check are on [workflows](workflows.html#failure-paths).
These are the ones particular to this workflow, each with who acts next. Except where a source is
cited, each response is recommended practice.

- **The failure cannot be reproduced.** The timeout in the export needs a data volume that the
  ordinary test environment may not hold, so the reproduction is recorded as `could_not_run`, not as
  a pass and not as proof that the failure was a one-off. The owner of the test environment acts, and
  the decision waits for a result or for a recorded choice to go on without one.
- **An action has no owner.** The review stays open, as the ownership check requires, and the
  deciders name someone before the run can close.[^google-sre-postmortem]
- **The lesson stops at the code.** The fix ships and nothing upstream changes. The sign of this
  pitfall is described on [Operate](operate.html#pitfalls); the run's own guard is that its record
  cannot close without an upstream change or a recorded decision that none is needed.
- **A link on the spine is missing.** The trace cannot reach the change or the requirement. The gap
  is recorded as an orphan and sent to the owner of the workflow that should have written that link,
  whom the "Written by" column of the [traceability spine](traceability-spine.html) table names.
- **People disagree on the cause.** The workbook advises including all incident participants in
  postmortem authoring, because key contributing factors are easily overlooked "when the postmortem
  is written in isolation".[^google-sre-postmortem] As recommended practice, the record keeps each
  competing hypothesis and the decision taken between them, so a later incident can reopen the
  question with the earlier reasoning in view.
- **The change does not land in time.** An upstream change still open at the next checkpoint is read
  at [Inspect and Adapt](inspect-and-adapt.html). The workbook frames the same concern as a question
  to ask of postmortems: "Are action items taking too long to close?"[^google-sre-postmortem]

## Measures

No public source gives a target value for any of these measures, and DORA warns against setting
metrics as a goal.[^dora-metrics] Each measure is compared with the team's own earlier history, which
is also DORA's advice: set a baseline for the application's current performance, at the level of
the application or service.[^dora-metrics] Formal definitions of delivery measures belong to the
assurance band.

- **Recurrence of a kind of miss already reviewed.** The workbook says that if teams see "failures
  that mirror previous incidents, it's time to dig deeper",[^google-sre-postmortem] and the SRE book
  sets reduced recurrence as a goal of the postmortem.[^incident-sre-book-postmortem] Baseline: the
  incident history before the workflow ran.
- **Closure and age of actions.** How many actions close with a named owner, and how long they stay
  open, the concern behind the workbook's question about action items taking too long to
  close.[^google-sre-postmortem] Baseline: the postmortems written before the workflow.
- **Delivery instability.** DORA's change fail rate and deployment rework rate, the latter defined as
  "the ratio of deployments that are unplanned but happen as a result of an incident in production",
  read with failed deployment recovery time, which DORA places in its throughput
  group.[^dora-metrics] Baseline: the same service's values before the workflow.
- **Trace completeness.** The share of runs whose trace reaches the requirement with no missing link.
  Baseline: the first runs under the workflow, since earlier incidents were not traced this way. This
  measure is recommended practice.
- **Time to the upstream change.** The time from the reviewed postmortem to the upstream change being
  merged. Baseline: earlier incidents, where the dates can be recovered. This measure is recommended
  practice.

## Owner

One person or role owns the workflow itself, as every workflow on this site has one accountable owner
([workflows](workflows.html)). That owner is distinct from the people who decide each run. The
incident roles in the SRE book cover the response itself,[^sre-book-managing-incidents] and each postmortem action has its
own owner (see [Operate](operate.html#roles)).[^google-sre-postmortem]

As recommended practice, the workflow owner keeps the rules for tracing and for closing a run,
reads the measures above, and takes a kind of miss that keeps recurring to
[Inspect and Adapt](inspect-and-adapt.html). SSDF practice RV.3.2 gives the public reason for looking
across runs as well as within one: "Analyze the root causes over time to identify patterns".[^nist-ssdf]

## Related

- Takes evidence from [Release readiness](release-readiness.html),
  [Deploy verification](deploy-verification.html),
  [Pull-request verification](pull-request-verification.html) and incident remediation,
  [W27](workflow-catalog.html#W27).
- Hands evidence to [Specification readiness](spec-readiness.html),
  [Design conformance](design-conformance.html),
  [Pull-request verification](pull-request-verification.html) and
  [Inspect and Adapt](inspect-and-adapt.html).
- Phase: [Operate](operate.html). Chain of records: [Traceability spine](traceability-spine.html).
- Where each kind of lesson lands, and the changes that follow the export incident:
  [the steering loop and the feedback path](harness-engineering.html#the-steering-loop-and-the-feedback-path),
  the site's extension of what Böckeler calls the steering loop.[^bockeler-harness]
- How production feedback reaches specification across many workflows:
  [software factory](software-factory.html#production-feedback-reaches-specification).
- The shared parts a run reads and points to: [Rule registry](rule-registry.html),
  [Skills with evals](skills-and-evals.html) and [Evidence schema](evidence-schema.html).
- Workflow catalog: [W28](workflow-catalog.html#W28), [W27](workflow-catalog.html#W27),
  vulnerability response [W29](workflow-catalog.html#W29) and evaluation rerun
  [W35](workflow-catalog.html#W35).
- Terminology: [feedback path](glossary.html#feedback-path),
  [evidence hand-off](glossary.html#evidence-handoff), [could_not_run](glossary.html#could-not-run)
  and [failure path](glossary.html#failure-path).

## Sources

- Postmortems: *Postmortem Culture: Learning from Failure*, chapter 15 of the SRE book, for the
  definition, the goals, blamelessness, review and the repository of past
  incidents;[^incident-sre-book-postmortem] and the SRE workbook chapter of the same title, for
  action-item ownership, tracking, end states, approval, inclusive authoring and recurrence.[^google-sre-postmortem]
  The SRE book's chapter on managing incidents, for who changes production during an
  incident.[^sre-book-managing-incidents]
- Testing terms and practice: the ISTQB glossary entries for failure, defect, confirmation testing
  and regression testing;[^incident-istqb-failure][^incident-istqb-defect][^incident-istqb-confirmation-testing][^incident-istqb-regression-testing]
  Martin Fowler on self-testing code.[^fowler-selftesting]
- Security: NIST SSDF version 1.1, practices RV.3.1, RV.3.2 and RV.3.4;[^nist-ssdf] NIST SP 800-61
  Revision 3 on lessons learned, Improvement and the after-action report;[^nist-800-61r3] the OWASP
  Logging Cheat Sheet on sensitive data in logs.[^incident-owasp-logging]
- Agents and research: Google's account of agents in SRE;[^google-agentic-sre] Ahmed and colleagues,
  ICSE 2023, and Chen and colleagues, an arXiv preprint.[^ahmed-incident-llm][^chen-rcacopilot]
- Traceability: Gotel and Finkelstein's definition[^gotel-finkelstein-1994] and NASA's software
  engineering handbook on bi-directional traceability.[^nasa-swe-052]
- Measures and proportion: DORA's guide to software delivery performance metrics[^dora-metrics] and
  its capability page on streamlining change approval.[^dora-streamlining-change-approval]
- The steering loop: Birgitta Böckeler.[^bockeler-harness]
- The review skill as an inferential sensor: Birgitta Böckeler.[^bockeler-sensors]
- Inspect and Adapt: Scaled Agile, Inc.'s page on the event.[^safe-inspect-and-adapt]
- Statements marked as recommended practice are this site's own and are not findings of any study.
