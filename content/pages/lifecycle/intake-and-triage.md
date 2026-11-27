---
id: intake-and-triage
type: workflow
band: lifecycle
map_box: intake & triage
title: Intake and triage
summary: The workflow that decides whether an arriving request, report or lesson is taken on now, as it stands or broken into smaller items, with an agent's first reading offered as input and the decision recorded under a person's name.
key_terms: [ai-sdlc, workflow, three-roles, risk-tier, evidence-record, evidence-handoff, could-not-run, failure-path, rule-registry, lifecycle-levels, export-example]
sources: [scrum-guide-2020, intake-istqb-defect-management, dora-customer-feedback, nist-ssdf, dora-wip-limits, dora-ai-capabilities-intro, sre-book-being-on-call, dora-small-batches, dora-metrics]
related: [idea, spec-readiness, incident-feedback, lifecycle-levels, traceability-spine, operate, workflows, rule-registry, evidence-schema]
review_record: content/reviews/1.6.0-lifecycle.md
---

## Decision

Is this arriving item taken on now, and if so in what form: as it stands, or broken into smaller
items first? Intake and triage is the workflow that answers that question in an AI SDLC (the
software development lifecycle with AI agents doing part of the work), once for every item that
reaches a team's backlog. "Triage" carries its ordinary meaning here: sorting what
arrives by kind and urgency. How an admitted item then ranks against the rest is a separate call,
the ordering of a backlog the Scrum Guide describes as "an emergent, ordered list of what is needed
to improve the product"[^scrum-guide-2020]. The catalog row
[Intake and classification](workflow-catalog.html#W01) states the decision in the catalog's own
terms; this page adds how a run proceeds, how it fails, what it records and how a team can tell
whether it works.

The decision is not limited to new features. For a reported defect, the ISTQB glossary defines
defect management as "the process of recognizing, recording, classifying, investigating, fixing and
disposing of defects"[^intake-istqb-defect-management]. Read against that sequence, this workflow
does the classifying: the report has been recorded, and nobody has started to investigate it yet.

## Trigger

A run starts when an item arrives in the backlog. Items arrive from more than one direction, and
public guidance stands behind each of the main ones. DORA asks whether a team actively and
regularly gathers feedback from users and acts on it[^dora-customer-feedback]; in this site's
catalog, those signals are handled by [Usage and feedback intake](workflow-catalog.html#W30). NIST's
Secure Software Development Framework recommends gathering information from software acquirers,
users and public sources on potential vulnerabilities and investigating all credible
reports[^nist-ssdf], which the catalog covers in [Vulnerability response](workflow-catalog.html#W29).
Lessons from production come back through the [Incident feedback](incident-feedback.html) workflow.

An item already admitted gets a fresh run when its content changes materially, because the earlier
decision was taken about a different item; this is recommended practice. An incident that is still
in progress is not a trigger at all. It belongs to incident handling, as the Guardrails section
below explains.

## Inputs

A run reads five things:

- **The item as written**, including who raised it and whose need it says it serves.
- **The backlog it would join.** Because the backlog is ordered[^scrum-guide-2020], the run can
  show the decider where the item would sit and which items already there look like it.
- **Earlier items it may repeat**, open or closed. Searching them before admission is recommended
  practice; no public source sets a method.
- **The rules its subject touches**, looked up in the [rule registry](rule-registry.html), so that
  an item that reaches a rule with an owner is visible as such before anyone sizes it.
- **The work already in progress.** DORA's guidance on work in process limits is: "Don't allow more
  WIP in any given part of the process than you have people to work on tasks"[^dora-wip-limits].
  DORA does not single out intake, but admission is the first point at which a team can hold to
  such a limit, so showing the current load beside the item is recommended practice.

## Agent task

This section is recommended practice; it is not drawn from a study of agents at intake. The agent reads the item as written and offers
a first reading, which a person then accepts, changes or rejects. What that reading contains is set
out in the catalog row [Intake and classification](workflow-catalog.html#W01) and is not repeated
here. In the record it is marked as the agent's, so nobody later mistakes it for the decision. In
the customer-record export, the hypothetical feature that lets users export customer records, the
agent's reading notes that the request touches customer data and the access rule R-042.

The agent's limits follow the accountabilities the Scrum Guide sets out[^scrum-guide-2020]:

- It does not order items, because ordering is part of the Product Owner's accountability for
  Product Backlog management.
- It does not size items, because "The Developers who will be doing the work are responsible for
  the sizing".
- It does not admit, reject, close or merge items, and it does not set a
  [risk tier](glossary.html#risk-tier) on its own authority. These limits are recommended practice:
  each is a decision the record attributes to a person, and an agent that took one would leave a
  decision on record that nobody made.

The user need gets a person's attention for a researched reason. DORA reports that "in the absence
of a user-centric focus, AI adoption can have a negative impact on team
performance"[^dora-ai-capabilities-intro]. An agent's text reads equally well whether or not anyone needs what
it describes, so, as recommended practice, a person confirms the need rather than the agent.

## Checks

The checks in this workflow decide only what a tool can tell from the record alone: whether the item
is complete and well formed, never whether it is worth doing (see the
[Idea](idea.html#ai-assisted-practice) phase page). The particular checks are named in the catalog
row; this page describes how they behave.

A check that the item names the user or stakeholder whose need it serves is a form check. It
confirms that a name is present; whether the need is real stays with the person deciding, for the
reason DORA gives above[^dora-ai-capabilities-intro].

Each check reports one of the result states fixed by the [Evidence schema](evidence-schema.html#check-results):
passed, failed, skipped or `could_not_run`. The last is a status of its own, kept apart from a
failure so that an unavailable tool and a real defect each get the right response, and, like a
failure, it blocks a positive overall status. If the rule registry cannot be reached, for example,
the run cannot list the rules an item touches. As recommended practice, the item then waits rather
than being admitted on a guess about which rules apply.

## Guardrails

How a workflow's agent is limited in general is set out on the
[Workflows](workflows.html#the-three-roles-agent-checks-and-people) page. Intake adds bounds of its
own:

- **A time limit on the reading.** If the agent has not produced its reading within a set time, the
  item goes to the decider without one. This is recommended practice; no public source sets the
  limit.
- **Stop on a live incident.** An item that describes something failing in production now leaves
  backlog triage for incident handling (see [Operate](operate.html#managing-incidents)). There, in
  the SRE book's account, the on-call engineer is "expected to triage the problem" and "work toward
  its resolution"[^sre-book-being-on-call]: an urgent, different use of the same word.
- **Stop on data that should not be there.** If an item carries data that should not sit in a
  backlog, the agent stops and flags the item to a person instead of reading further. This is
  recommended practice.

## Human decision

The Scrum Guide places this decision. The Product Owner is accountable for effective Product Backlog
management, which includes creating and clearly communicating Product Backlog items and ordering
them; the Product Owner "may delegate the responsibility to others. Regardless, the Product Owner
remains accountable"[^scrum-guide-2020]. Sizing stays with the Developers who will do the
work[^scrum-guide-2020]. The catalog row [Intake and classification](workflow-catalog.html#W01)
names who decides in the catalog's terms.

As recommended practice, the decider works from four things: the item, the agent's reading marked as
such, the result of each check and the rules the item touches, all in the shape the
[Evidence schema](evidence-schema.html) fixes. The decider may:

- **overrule any part of the agent's reading**, with the reason recorded;
- **split the item before admitting it**, which the Scrum Guide's description of refinement as "the
  act of breaking down and further defining Product Backlog items" supports[^scrum-guide-2020];
- **defer it**, with the reason recorded.

In the export example, the person who orders the backlog accepts the request with the open
questions the [Idea](idea.html) page lists recorded as open, for Specification readiness to settle.

## Outputs and evidence

The run leaves one [evidence record](evidence-schema.html), the shape every workflow on this site
writes. For intake, that record holds the decision under the decider's name, the agent's reading as
an advisory finding, each check's result and the reason wherever the decider overruled the reading.
The admitted item links to it, so anyone who opens the item can see why it was taken on.

Four readers depend on the record the run leaves:

- **[Specification readiness](spec-readiness.html)** starts from it instead of reopening the intake
  decision, the practice this site calls [evidence hand-off](glossary.html#evidence-handoff).
- **The train and portfolio levels** read it when admitted items roll up into larger pieces of work
  (see [Lifecycle levels](lifecycle-levels.html)).
- **The [traceability spine](traceability-spine.html)** takes it as the requirement end of the chain,
  where each requirement needs a named origin.
- **The workflow's owner** reads the records together to compute the measures below; this use is
  recommended practice.

## Failure paths

The general responses to a failed check, a check that could not run and a rejected agent finding are
on the [Workflows](workflows.html#failure-paths) page. At intake, as recommended practice, the
two check results work as follows.

When a check fails, for example because the item does not name whose need it serves, the item goes
back to whoever raised it with the failure stated, and that person acts next. When a check reports
`could_not_run`, as when the rule registry cannot be reached, the item waits rather than being
admitted, and the owner of the unavailable tool acts next; the
[Evidence schema](evidence-schema.html#check-results) keeps that result apart from both a pass and a
failure.

When the agent stops for one of the reasons the Guardrails section defines, the next actor is named
in the same way, as recommended practice. If the reading times out, the decider proceeds without it.
If the item describes a live incident, the on-call engineer or incident owner acts next, through
incident handling on the [Operate](operate.html#managing-incidents) page. If the item carries data
that should not sit in a backlog, whoever owns the backlog's data handling acts next.

## Measures

DORA warns against turning delivery metrics into targets, and treats them as a way for one team to
improve over time rather than to compare teams[^dora-metrics]. Each measure below is therefore
compared with the team's own earlier figure, never with a target. The specific measures are
recommended practice; only their grounding is sourced.

| Measure | Baseline to compare against | What a change suggests |
|---|---|---|
| Time from an item's arrival to a recorded decision, with the number and age of items waiting | The same figures for the backlog before the workflow ran | DORA's guidance on work in process limits asks whether a team knows "the mean lead time and variability for our entire value stream (from idea to customer)"[^dora-wip-limits]; this is the first stretch of that stream |
| How often the kind of work or the tier set at intake is changed later, at readiness or design | The rate in the first period under the workflow | A rising rate points at intake reading too little; a rate of zero over a long period may mean nobody revisits the call |
| Share of admitted items later split because they were too large | The share before the workflow ran | Items are reaching later phases at a size DORA's small-batch guidance argues against[^dora-small-batches] |
| Agreement between the agent's reading and the recorded decision | The rate in the first period, read together with the time each decision took | Very low agreement means the reading is not useful; near-total agreement with near-instant decisions means nobody is weighing it, the pitfall the [Idea](idea.html#pitfalls) page names first |

## Owner

The workflow has one accountable owner, as every workflow on this site does (see
[Workflows](workflows.html)), who changes its checks, the agent's limits and what the record holds.
The Scrum Guide places Product Backlog management with the Product Owner, who may delegate the work
but remains accountable[^scrum-guide-2020]. Making the same person accountable for this workflow
keeps the decision and the way it is made in one pair of hands; that is recommended practice, and a
team may assign the workflow elsewhere as long as one person owns it.

## Related

- [Specification readiness](spec-readiness.html): the next workflow, which reads the record this one
  leaves.
- [Incident feedback](incident-feedback.html): one of the workflows that sends items here.
- [Idea](idea.html): the phase this workflow sits in, including backlog ordering and size.
- [Lifecycle levels](lifecycle-levels.html): the portfolio, train and team levels, including
  [ordering across a portfolio](lifecycle-levels.html#portfolio).
- [Traceability spine](traceability-spine.html): the chain from requirement to incident that starts
  with the items admitted here.
- [Operate](operate.html): where a live incident goes instead of the backlog.
- Core: [Workflows](workflows.html), [Rule registry](rule-registry.html) and
  [Evidence schema](evidence-schema.html).
- Workflow catalog rows: [Intake and classification](workflow-catalog.html#W01),
  [Security discovery and baseline](workflow-catalog.html#W02), [Spike](workflow-catalog.html#W07),
  [Vulnerability response](workflow-catalog.html#W29) and
  [Usage and feedback intake](workflow-catalog.html#W30).
- Terminology: [Risk tier](glossary.html#risk-tier), [could_not_run](glossary.html#could-not-run),
  [Evidence hand-off](glossary.html#evidence-handoff) and
  [The export example](glossary.html#export-example).

## Sources

- Backlog ownership, ordering, delegation, refinement and sizing: the Scrum Guide by Ken Schwaber and
  Jeff Sutherland[^scrum-guide-2020].
- Defect management as a sequence: the ISTQB glossary[^intake-istqb-defect-management].
- Where items come from: DORA on customer feedback[^dora-customer-feedback] and NIST's Secure
  Software Development Framework on vulnerability reports[^nist-ssdf].
- Flow and batch size: DORA on work in process limits[^dora-wip-limits] and on working in small
  batches[^dora-small-batches].
- User focus and AI adoption: the introduction of the DORA AI Capabilities
  Model[^dora-ai-capabilities-intro].
- Incident triage: the Google SRE book on being on call[^sre-book-being-on-call].
- Metrics as signals, not targets: DORA's guide to software delivery performance
  metrics[^dora-metrics].
