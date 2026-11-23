---
id: lifecycle-levels
type: concept
band: lifecycle
map_box: Portfolio · Train · Team
title: "Lifecycle levels: portfolio, train and team"
summary: One delivery lifecycle runs at three altitudes, a portfolio that decides what to fund, a train that decides what to plan and demonstrate, and a team that decides what to build and when it is ready and done, with intent and rules flowing down and evidence and lessons flowing up.
key_terms: [lifecycle-levels, agile-release-train, planning-interval, wsjf, workflow, software-factory, feedback-path, steering-loop, evidence-handoff, evidence-record, rule-registry, specification-readiness, risk-tier, export-example]
sources: [safe-portfolio, safe-lpm-discipline, safe-lean-budgets, safe-guardrails, safe-strategic-themes, safe-epic, safe-wsjf, safe-cost-of-delay, safe-art, safe-agile-teams, safe-features, safe-framework, safe-pi-planning, safe-glossary, safe-inspect-and-adapt, safe-story, safe-iteration-planning, safe-iterations, scrum-guide-2020, dora-small-batches, dora-wip-limits, dora-customer-feedback, dora-ai-capabilities-impact, dora-2025-announcement, bockeler-harness, oasis-soa-rm, safe-system-demo]
related: [safe-reference-model, definition-of-ready-and-done, traceability-spine, inspect-and-adapt, idea, specification, design, develop-build-qa, deploy, release, operate, workflows, software-factory, rule-registry, evidence-schema, harness-engineering, engineering-kit]
review_record: content/reviews/1.5.0-lifecycle.md
---

## Definition

The lifecycle levels are three altitudes at which one delivery lifecycle is run: Portfolio, Train
and Team. In the AI SDLC (the software development lifecycle with AI agents doing part of the
work), a portfolio decides which initiatives to fund, in what order and with what budget; a train
decides which features enter a planning cycle and what an integrated demonstration shows; and a
team decides which stories to build in an iteration and when work counts as ready and as done. The
three labels are generic names this site coined for the altitudes. They are not a standard, and a
reader who uses other words for the same decisions loses nothing by keeping them.

The Scaled Agile Framework (SAFe) uses the same altitudes under its own names, and it is cited
here as one framework that does so, not as the origin of the labels. SAFe defines a Portfolio as
"a set of value streams that delivers a continuous flow of valuable solutions to customers within
a common funding and governance model"[^safe-portfolio]. It defines an Agile Release Train (ART) as
"a long-lived team of Agile teams that incrementally develops, delivers, and often operates one or
more solutions in a development value stream"[^safe-art], and an Agile Team as "a cross-functional
group of typically ten or fewer individuals with all the skills necessary to define, build, test,
and deliver value to their customer"[^safe-agile-teams]. The worked mapping from this site's labels
to SAFe's terms, a reference model in the OASIS sense,[^oasis-soa-rm] is on the
[SAFe reference model](safe-reference-model.html) page.

## Why it matters

A decision placed at the wrong level reaches the wrong people, with the wrong evidence and at the
wrong time. A question about one story's edge case, taken to a portfolio review, takes the time of
people who cannot answer it. A question about which initiative to fund, settled inside a team
because the team happens to be the one asking, commits money nobody with authority over it has
weighed. Both are cases of one workflow decision (see [Workflows](workflows.html)) being owned at
an altitude that does not match its size.

Two flows hold the levels together, and each fails in a recognisable way. When intent and rules do
not flow down, each level re-decides what a higher level has already settled, because it has no
record of that decision and no shared rule to read. When evidence and lessons do not flow up, higher
levels decide on status updates instead of records, and the same miss recurs in later work. The reasoning
behind the first follows from how the [rule registry](rule-registry.html) is shared, as the
[Software factory](software-factory.html) page describes; the second follows from the lessons that
never close described there. Both readings are recommended practice, drawn from how
workflows hand work on, not a measured finding.

Agents raise the stakes at every level. DORA notes that "AI can easily generate massive blocks of
code, which are hard to review and test"[^dora-ai-capabilities-impact], and its 2025 report
announcement says that AI "doesn't fix a team; it amplifies what's already there"[^dora-2025-announcement].
More output per day lands on levels that were already short of review time, and an unclear
decision right is amplified along with it. This site found no public study that examines the three
levels with agents, so the level-by-level advice on this page is recommended practice, labelled as
such where it appears, and not a research finding.

## How it works

Each level is described by what it decides, in SAFe's public wording where a definition exists.
Two things then connect the levels: what flows down and up, and the size of the work item. The
customer-record export then shows the flows in one story.

### Portfolio

A portfolio decides which initiatives to fund, in what order, and the budget behind them.

SAFe's definition of a Portfolio is given above[^safe-portfolio]. Its budgeting follows from that
definition: the available portfolio budget is "directly allocated to these value streams rather
than the traditional approach of project-based funding"[^safe-lpm-discipline], and Lean budgets
are a financial governance approach that funds value streams instead of
projects[^safe-lean-budgets]. Lean budget guardrails "describe the policies and practices for
budgeting, spending, and governance for a specific portfolio"[^safe-guardrails]. SAFe describes
strategic themes as portfolio-level business objectives that provide competitive differentiation
and strategic advantage, and as what connects the enterprise strategy to a
portfolio[^safe-strategic-themes].

What a portfolio funds and orders is the epic, which SAFe calls "a significant solution development
initiative"[^safe-epic]. Ordering epics uses weighted shortest job first (WSJF). In SAFe, WSJF "is
estimated as the relative cost of delay divided by the relative job duration"[^safe-wsjf]. Its
inputs are relative user and business value, time criticality, risk reduction and opportunity
enablement, and job size[^safe-wsjf]. Cost of Delay is the money or value lost by delaying or not
doing a job for a time period, relative to other jobs[^safe-cost-of-delay]. SAFe's WSJF page opens
with an epigraph attributed to Don Reinertsen's *The Principles of Product Development
Flow*[^safe-wsjf].

No public study covers portfolio decisions with agents, so what this page says about agents at
this level is recommended practice. Here an agent prepares and people decide. An agent can gather
the evidence records of earlier work that bear on a candidate initiative, so that a funding
discussion reads records rather than status reports, but it does not fund, order or budget
anything; those decisions stay with named people. Two catalog workflows sit closest to these
decisions, [Intake and classification (W01)](workflow-catalog.html#W01) and
[Usage and feedback intake (W30)](workflow-catalog.html#W30), and their rows say what the agent
and the people do in each.

### Train

A train decides which features go into which planning cycle, and what the integrated demonstration
shows. SAFe's definition of an ART is given above[^safe-art].

A Feature is "solution functionality that delivers business value, fulfills a stakeholder need, and
is sized to be delivered by an Agile Release Train within a PI"[^safe-features]. The Planning Interval
(PI) is "a cadence-based timebox in which Agile Release Trains deliver continuous value to
customers in alignment with PI Objectives"[^safe-framework]. SAFe describes it as typically an 8 to
12-week timebox and calls the pattern of planning and iterations a suggestion rather than a strict
rule[^safe-framework]. PI Planning "aligns teams and stakeholders to a shared mission and vision"[^safe-pi-planning]. The System Demo[^safe-system-demo] "provides
stakeholders an integrated view of new features for the most recent iteration delivered by all the
teams on the ART"[^safe-glossary].

### Team

A team decides which stories it builds, in which iteration, and when an item is ready and done. In
SAFe, a story "focuses on a specific behavior that can be developed in incremental steps", and
keeping stories small means they can be completed in a single iteration[^safe-story]. An iteration
is "a standard, fixed-duration timebox during which Agile Teams and ARTs individually and
collectively deliver incremental customer value while working towards the PI
objectives"[^safe-iterations]. In Iteration Planning, "the team defines, organizes, and commits to
the work for the next iteration"[^safe-iteration-planning]. Iteration Goals are "a high-level summary
of the business and technical goals that an Agile Team agrees to accomplish in an
Iteration"[^safe-glossary].

Readiness and done sit at this level. The Scrum Guide says Product Backlog items "that can be Done
by the Scrum Team within one Sprint are deemed ready for selection in a Sprint Planning event", and
describes the Definition of Done as "a formal description of the state of the Increment when it
meets the quality measures required for the product"[^scrum-guide-2020]. The Guide does not use the
term "Definition of Ready". SAFe's glossary defines the Definition of Done as specifying "the
requirements for completeness of a work product or increment of value"[^safe-glossary]. The page
[Definition of Ready and Definition of Done](definition-of-ready-and-done.html) treats both terms.

### What flows down and up

Two things flow down. Intent flows down as the work item narrows: a portfolio funds an initiative,
a train plans the features cut from it, and a team builds the stories cut from those features. In
SAFe's terms that intent starts with the strategic themes described above, which connect the
enterprise strategy to a portfolio[^safe-strategic-themes]. Keeping each story linked to
its feature and each feature to its initiative, so that a team can see which funded intent its work
serves and does not re-decide it, is recommended practice. Rules flow down as one
[rule registry](rule-registry.html) shared by every level; see
[Software factory](software-factory.html#three-things-are-shared).

Two things flow up. Evidence flows up as the evidence record; see
[Evidence schema](evidence-schema.html). Lessons flow up and back as the feedback path; see
[Harness engineering](harness-engineering.html#the-steering-loop-and-the-feedback-path). The
[Inspect and Adapt](inspect-and-adapt.html) page covers the checkpoint where they are collected. In
SAFe, improvement backlog items from Inspect and Adapt go into the ART Backlog for consideration in
the next PI Planning event[^safe-inspect-and-adapt].

Signals from users flow up too, from outside the delivery work itself. DORA places customer
feedback in a wider group of capabilities, with visibility of work in the value stream, working in
small batches and team experimentation, that together represent a lean approach to product
management and, applied together, help predict software delivery and organisational
performance[^dora-customer-feedback]. In this site's workflow catalog, the workflow that handles
those signals is [Usage and feedback intake (W30)](workflow-catalog.html#W30).

### The size of the work item at each level

The item that travels the lifecycle is a different size at each altitude. An epic is "significant"
in SAFe[^safe-epic]. A feature is sized to be delivered by one train within one PI[^safe-features].
A story is kept small enough to complete in a single iteration[^safe-story]. These sizes are one
framework's wording, and fit to the planning cycle is one test of size, not the only one.

A second test applies at every level. DORA advises breaking work "into work units that can be
completed independently and in short timeframes", and says that working in small batches amplifies
the positive impact of AI adoption on product performance[^dora-small-batches]. The same page notes that "large changes are difficult to review, test, and integrate safely"[^dora-small-batches].

DORA's page on work in process limits adds a test for the amount in flight. It advises prioritising
work, limiting how much people work on at once and focusing on completing a small number of
high-priority tasks, and it says research shows that limits on work in process help drive
improvements in software delivery performance, particularly when combined with visual displays and
feedback loops from monitoring[^dora-wip-limits]. Neither DORA page addresses the three levels, so
applying both tests at the portfolio, train and team levels, and not only to a team's own tasks, is
recommended practice.

### The export example across the levels

The customer-record export is a hypothetical feature that lets users export customer records. Its
open decisions are which records, which fields, how large exports behave, what happens on failure
and what is audited. The example does not size the export, place it in a planning cycle or assign
any decision to a level. It shows what travels between the levels.

Intent comes down with the feature: its open decisions, such as which fields an export includes,
are answered against the purpose the feature was approved for rather than re-decided at each step.
Rules come down as registry entries: the access rule R-042 and the volume-limit rule R-017 live in
the [rule registry](rule-registry.html), and the workflows that handle the export read them from
there. Evidence goes up as a record: the pull-request run records R-042 as `failed` and R-017 as
`could_not_run` in its [evidence record](evidence-schema.html#the-customer-record-export), and once
the fixes land and the checks run again, release readiness reads the new record instead of asking
again. Lessons go back after a scheduled full export times out in production: a readiness question
asking every export-like specification for its largest export changes what later export-like
features are asked ([Software factory](software-factory.html#the-running-example-across-workflows)).

## Where it sits on the map

The levels form the top row of band 2, the lifecycle band. Three chips run left to right, Portfolio,
Train and Team, with an arrow between each, and each carries a short subtitle: "initiatives ·
prioritisation · budgets", "features · planning cycle · integrated demo" and "stories · iterations ·
DoR / DoD". Each chip links to its own sub-section on this page. Beneath the level row sit the nine
phases (Idea, Specification, Design, Develop, Build, QA, Deploy, Release and Operate) with the
workflow in each phase. Under them run the traceability spine, from requirement through spec, task,
test, change and release to incident, and a line naming Inspect & Adapt. The map draws the levels
above the phases without assigning any phase or workflow to a level.

The phase boxes link to their pages: [Idea](idea.html), [Specification](specification.html),
[Design](design.html), [Develop, Build and QA](develop-build-qa.html), [Deploy](deploy.html),
[Release](release.html) and [Operate](operate.html). The spine links to [Traceability spine](traceability-spine.html), the
readiness and done tags to [Definition of Ready and Definition of Done](definition-of-ready-and-done.html)
and the Inspect & Adapt line to [Inspect and Adapt](inspect-and-adapt.html).

The map's vocabulary is mixed. Band 2 uses the generic labels from this page. The Operating model
box in the enablement band, band 4, keeps SAFe's own words, such as Scrum or Kanban teams on an
Agile Release Train and PI cadence, so the [SAFe reference model](safe-reference-model.html) page
is the place to read one vocabulary against the other. The core band below the lifecycle band holds the
workflows, rules and records that the levels share.

## Pitfalls

- **Items never cut to the size of the planning cycle they enter.** Work arrives larger than the
  cycle can hold. Sign: the same item carried from one cycle to the next. SAFe sizes a feature to be
  delivered within one PI and keeps stories small enough for a single iteration[^safe-features][^safe-story],
  and DORA advises breaking work into units that can be completed independently and in short
  timeframes[^dora-small-batches]. Reading repeated carry-over as a failure of sizing is
  recommended practice.
- **Prioritising without a measure of the cost of waiting.** Items are ordered by who asked, and no
  one estimates what a delay costs. Sign: priority decided by the order of requests. WSJF and Cost
  of Delay are one public way to measure it[^safe-wsjf][^safe-cost-of-delay]; that having no measure
  is a failure is recommended practice.
- **Evidence stops at the team.** Records are written where the work runs, and higher levels are
  given summaries of them. Sign: portfolio reviews read status updates, not records. The
  [Workflows](workflows.html#pitfalls) page names the same failure at workflow scale as hand-off by
  conversation; the portfolio-review sign is recommended practice.
- **Lessons stay where they were learned.** A lesson changes the work of the team that found it and
  goes no further. Sign: the same kind of miss in a later feature. The
  [Software factory](software-factory.html#pitfalls) page calls this lessons that never close.
- **Agent output outruns the level that must judge it.** Generation is cheap and review is not.
  Sign: batches of generated change larger than a reviewer can read. DORA's warning about code that
  is hard to review and test[^dora-ai-capabilities-impact] and its advice on small
  batches[^dora-small-batches] apply at each level; [Workflows](workflows.html) lists a run too
  large to review.

## Related

- [SAFe reference model](safe-reference-model.html): the worked mapping from these labels to SAFe's
  terms.
- [Definition of Ready and Definition of Done](definition-of-ready-and-done.html): readiness and
  done at team level, in [Definition of Ready](definition-of-ready-and-done.html#definition-of-ready)
  and [Definition of Done](definition-of-ready-and-done.html#definition-of-done).
- [Traceability spine](traceability-spine.html): the link from requirement to incident beneath the
  phases.
- [Inspect and Adapt](inspect-and-adapt.html): the checkpoint where lessons flow up.
- The phases: [Idea](idea.html), [Specification](specification.html), [Design](design.html),
  [Develop, Build and QA](develop-build-qa.html), [Deploy](deploy.html), [Release](release.html)
  and [Operate](operate.html).
- [Workflows](workflows.html) and [Software factory](software-factory.html): the unit of work and
  the operating state that share rules, evidence and feedback across the levels.
- [Rule registry](rule-registry.html), [Evidence schema](evidence-schema.html),
  [Harness engineering](harness-engineering.html) and [Engineering Kit](engineering-kit.html): where
  the rules and records that flow between levels are defined.
- [Workflow catalog](workflow-catalog.html): the entries
  [Intake and classification (W01)](workflow-catalog.html#W01) and
  [Usage and feedback intake (W30)](workflow-catalog.html#W30), named in the sections above.
- Terminology: [lifecycle levels](glossary.html#lifecycle-levels),
  [Agile Release Train](glossary.html#agile-release-train),
  [Planning Interval](glossary.html#planning-interval), [WSJF](glossary.html#wsjf),
  [workflow](glossary.html#workflow) and [feedback path](glossary.html#feedback-path)[^bockeler-harness].
- The [adoption path](index.html#adoption): the order in which a team builds these parts.

## Sources

- SAFe, for the levels and their vocabulary: the Portfolio definition[^safe-portfolio], Lean
  Portfolio Management and budgets[^safe-lpm-discipline][^safe-lean-budgets], guardrails and
  strategic themes[^safe-guardrails][^safe-strategic-themes], epics[^safe-epic], and WSJF and Cost of Delay[^safe-wsjf][^safe-cost-of-delay].
- SAFe, for the train and the team: the Agile Release Train[^safe-art], Features[^safe-features],
  the Planning Interval[^safe-framework], PI Planning[^safe-pi-planning], Agile Teams[^safe-agile-teams],
  Story[^safe-story], Iterations[^safe-iterations], Iteration Planning[^safe-iteration-planning], the
  glossary[^safe-glossary] and Inspect and Adapt[^safe-inspect-and-adapt].
- Readiness and done: the Scrum Guide[^scrum-guide-2020].
- DORA, on small batches, work in process, customer feedback and AI: working in small
  batches[^dora-small-batches], work in process limits[^dora-wip-limits], customer
  feedback[^dora-customer-feedback], the AI capabilities post[^dora-ai-capabilities-impact] and the
  2025 report announcement[^dora-2025-announcement].
- Böckeler on harness engineering and the steering loop[^bockeler-harness].
- The sense in which this site uses "reference model": OASIS[^oasis-soa-rm].
- Carrying intent from initiative to story, what an agent does at portfolio level, and applying
  the batch-size and work-in-process tests at every level are this site's recommended practice;
  no public source states them.
