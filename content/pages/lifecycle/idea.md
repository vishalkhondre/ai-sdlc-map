---
id: idea
type: phase
band: lifecycle
map_box: Idea
title: Idea
summary: The first lifecycle phase, where a request becomes an ordered, sized item of work in the backlog with its intake decision recorded, so that specification starts from a record rather than a conversation.
key_terms: [ai-sdlc, workflow, three-roles, risk-tier, evidence-record, evidence-handoff, export-example]
sources: [scrum-guide-2020, safe-continuous-exploration, safe-cdp, safe-features, safe-wsjf, dora-small-batches, dora-ai-capabilities-intro, dora-ai-capabilities-impact, safe-art, safe-framework]
related: [specification, design, lifecycle-levels, definition-of-ready-and-done, workflows, evidence-schema, software-factory, intake-and-triage]
review_record: content/reviews/1.5.0-lifecycle.md
---

## Purpose

Idea is the first phase of the delivery lifecycle in the AI SDLC (the software development
lifecycle with AI agents doing part of the work). It is where a request, a reported problem or a
new possibility turns into an item of work that a team has agreed to carry. The item leaves the
phase with a place in the backlog, an order against everything else waiting there and a size that
the people who will build it accept, and the decision that admitted it is on record under the name
of the person who took it. The decision itself, in the words this site uses for it, is the catalog
row [Intake and classification](workflow-catalog.html#W01) (see the [Intake and triage](intake-and-triage.html) page).

The phase does not settle what the work must do or how it is built. Those questions belong to
[Specification](specification.html) and [Design](design.html). What Idea hands on is a record: the
next phase reads it instead of asking the same questions again, the practice this site calls
[evidence hand-off](glossary.html#evidence-handoff). As in every phase, the work is split three
ways, with an agent drafting, deterministic checks enforcing and named people deciding; the
[Workflows](workflows.html) page explains the split.

## Traditional practice

Without agents, intake is backlog work, and the Scrum Guide describes its ownership plainly. The
Product Backlog is an ordered list of the work needed on a product, and the Product Owner is
accountable for effective Product Backlog management, which includes creating and clearly
communicating its items and ordering them[^scrum-guide-2020]. The Guide calls refinement "an
ongoing activity to add details, such as a description, order, and size", and states that "The
Developers who will be doing the work are responsible for the sizing"[^scrum-guide-2020].

Scaled frameworks describe the front of delivery in broader terms. One framework's view is SAFe's
continuous exploration, which it describes as continually "exploring the market and customer needs,
defining a vision, roadmap, and set of features for a solution"[^safe-continuous-exploration]. SAFe
treats it as one of four aspects of its Continuous Delivery Pipeline, alongside continuous
integration, continuous deployment and release on demand[^safe-cdp]. Its unit at this altitude is
the feature, which it defines as "solution functionality that delivers business value, fulfills a
stakeholder need, and is sized to be delivered by an Agile Release Train within a PI"[^safe-features][^safe-art], where a PI is
SAFe's Planning Interval[^safe-framework]. This is one framework's account, not a definition of the
Idea phase.

Ordering is the other half of intake. In SAFe, weighted shortest job first (WSJF) "is estimated as
the relative cost of delay divided by the relative job duration", with relative user and business
value, time criticality, risk reduction and/or opportunity enablement, and job size as its
inputs[^safe-wsjf]. Where ordering happens across a portfolio rather than one team's backlog, the
[Lifecycle levels](lifecycle-levels.html#portfolio) page covers it.

Size is set here for the first time. DORA advises breaking work "into work units that can be
completed independently and in short timeframes"[^dora-small-batches]. The item admitted at Idea is
the unit that later phases specify, design and build, so Idea is the first point in the lifecycle
where the size of a batch is decided. Splitting an oversized request before it is admitted, rather
than after work has started, is recommended practice.

Not every item is a new feature, and not every kind of work needs every later phase. The classes of
work this site distinguishes at intake are listed in the catalog row
[Intake and classification](workflow-catalog.html#W01); they are the site's own list, and no public
standard defines them.

## AI-assisted practice

No public study was found that measures how well a coding agent sorts or sizes incoming work. Where this section describes what an agent does at Idea, it is recommended practice and not a
research finding; the claims that rest on research are cited to DORA.

**What moves to an agent.** Drafting. The agent reads a request as it was written and proposes a
first reading of it, which a person then accepts, changes or rejects. The exact proposal at intake
is set out in the catalog row [Intake and classification](workflow-catalog.html#W01). It is input
to a decision, never the decision.

**What moves to a deterministic check.** Anything about an item that a tool can decide from the
record alone, such as whether it is complete and well formed rather than whether it is worth doing.
Putting those questions in a check keeps people's attention for the judgments a tool cannot make.
The checks this phase runs are named in the catalog row.

**What stays with people.** Whether the work is worth doing, how it ranks against other work and
how large it is. The Scrum Guide places ordering with the Product Owner and sizing with the
Developers who will do the work[^scrum-guide-2020], and an agent's draft does not move either
accountability. The agent does not record a decision on anyone's behalf; the
[Software factory](software-factory.html#people-keep-the-decisions) page explains why that line
holds across every phase.

**Why size matters more once agents take part.** DORA's AI Capabilities Model names working in
small batches among seven capabilities that amplify the benefits of AI adoption, and calls it "a
long-standing DORA principle" that "is especially powerful in an AI-assisted
environment"[^dora-ai-capabilities-intro]. DORA's guidance on putting the model to work says small
batches help in "ensuring that speed translates to product performance rather than
instability"[^dora-ai-capabilities-impact], and its capability page reports that working in small
batches amplifies the positive impact of AI adoption on product performance[^dora-small-batches].
Keeping each change within what one reviewer can read in full is recommended practice, not a
measured finding; the [Workflows](workflows.html) page sets out the reasoning.

**Why the user need matters more.** The same model reports that "in the absence of a user-centric
focus, AI adoption can have a negative impact on team performance"[^dora-ai-capabilities-intro].
Idea is the phase where a user need is either stated or missing. An agent can write a fluent
request for almost anything, so as recommended practice a person confirms whose need an item
serves before it is admitted.

## Workflows in this phase

The workflow catalog holds this phase's workflows in its phase 0, "Concept & intake", which is the
catalog's name for the map's Idea box. A workflow, in this site's sense, is one delivery decision
run end to end with a named owner; each catalog row gives that decision and its parts, and this
page does not repeat them.

- [Intake and classification](workflow-catalog.html#W01) (see the [Intake and triage](intake-and-triage.html) page): the decision at the centre of this
  phase, and the one every later phase builds on. The map draws it as the bar labelled
  "intake & triage".
- [Security discovery and baseline](workflow-catalog.html#W02): in the same catalog phase,
  alongside intake.

## Gates and evidence

**Entry.** Idea is open by design. A request can come from anyone, and the phase exists to sort
what arrives, so the gate that matters is the one at the exit. The event that starts the intake
workflow is given in its [catalog row](workflow-catalog.html#W01).

**Exit.** An item leaves Idea when the checks named in its catalog row have passed and the intake
decision is recorded under the name of the person who took it. As recommended practice, an agent's
proposal on its own never moves an item on, and the size it carries is one the people who will do
the work have accepted[^scrum-guide-2020]. How a change's [risk tier](glossary.html#risk-tier) is
set and revisited is described on the [Workflows](workflows.html) page.

**Evidence.** The run leaves an [evidence record](evidence-schema.html), the one shape every
workflow on this site writes. That page fixes its fields and who may write each of them; this page
adds none. [Specification](specification.html) reads the record rather than reopening the intake
decision in conversation. Whether the phase works over time is measured under assurance.

**The running example.** In the customer-record export, a hypothetical feature that lets users
export customer records, the item leaves Idea with its main questions still open: which records,
which fields, how large exports behave, what happens on failure and what is audited. Settling them
is Specification's work. What is already visible is that the feature reads customer data and falls
under an access rule, R-042, so it is not a light change; the
[Workflows](workflows.html#risk-tiers-same-definition-different-cost) page compares it with a change
to the export button's label.

## Roles

- **Product Owner.** Accountable for effective Product Backlog management, including creating and
  clearly communicating backlog items and ordering them[^scrum-guide-2020].
- **Developers.** "The Developers who will be doing the work are responsible for the
  sizing"[^scrum-guide-2020].
- **The people who decide in each workflow.** Named in the catalog rows
  [Intake and classification](workflow-catalog.html#W01) and
  [Security discovery and baseline](workflow-catalog.html#W02).

The coding agent holds no role here: it drafts, and people decide, as described in the three roles
on the [Workflows](workflows.html) page. What each role does across the whole lifecycle is covered
in the enablement band, under people and roles.

## Pitfalls

- **The agent's proposal taken as the decision.** A proposal is accepted without anyone weighing it,
  and the record shows a decision nobody made. Sign: the recorded decision matches the agent's
  proposal on almost every item, and decisions follow proposals within moments.
- **Size set without the people who will do the work.** The Scrum Guide gives sizing to the
  Developers who will do the work[^scrum-guide-2020]. When an agent's size estimate stands in for
  theirs, the commitment rests on a number nobody doing the work agreed to; treating that as a
  pitfall in the agent case is recommended practice. Sign: sizes are recorded before any developer
  has seen the item.
- **Oversized items admitted whole.** A request large enough to fill several changes enters as one
  item, and every later phase inherits its size. DORA notes that "large changes are difficult to
  review, test, and integrate safely"[^dora-small-batches]. Sign: items that cannot be completed
  independently in a short timeframe are admitted without being split.
- **Items with no user need behind them.** An agent can always produce a plausible request, so
  items arrive that nobody asked for. DORA links the absence of a user-centric focus to a negative
  effect of AI adoption on team performance[^dora-ai-capabilities-intro]; the link to agent-written
  requests is recommended practice. Sign: an item cannot name the user or stakeholder whose need it
  serves.

## Related

- [Specification](specification.html): the next phase, which starts from the record Idea leaves.
- [Design](design.html): the phase after Specification, where the work is planned and designed.
- [Lifecycle levels](lifecycle-levels.html): the portfolio, train and team altitudes, including
  ordering across a portfolio and the size of the work item at each level.
- [Definition of Ready and Definition of Done](definition-of-ready-and-done.html): the entry and
  exit criteria for work; the ready tag sits on Specification, not on Idea.
- [Workflows](workflows.html): the decision unit, the three roles and risk tiers.
- [Evidence schema](evidence-schema.html): the fixed shape of the record each run leaves.
- [Software factory](software-factory.html): what emerges when workflows share rules, evidence and
  lessons.
- [Intake and triage](intake-and-triage.html): whether an arriving item is taken on now, as it stands or broken into smaller items.
- Workflow catalog rows [Intake and classification](workflow-catalog.html#W01) and
  [Security discovery and baseline](workflow-catalog.html#W02).
- Terminology: [Risk tier](glossary.html#risk-tier), [Three roles](glossary.html#three-roles),
  [Evidence hand-off](glossary.html#evidence-handoff) and
  [The export example](glossary.html#export-example).

## Sources

- Backlog ownership, ordering, refinement and sizing: the Scrum Guide by Ken Schwaber and Jeff
  Sutherland[^scrum-guide-2020].
- One framework's view of the front of delivery: SAFe on continuous
  exploration[^safe-continuous-exploration], the Continuous Delivery Pipeline[^safe-cdp], features
  and capabilities[^safe-features] and weighted shortest job first[^safe-wsjf].
- Small batches and AI-assisted delivery: DORA's capability page on working in small
  batches[^dora-small-batches], the introduction of the DORA AI Capabilities
  Model[^dora-ai-capabilities-intro] and DORA's guidance on putting that model to
  work[^dora-ai-capabilities-impact].
