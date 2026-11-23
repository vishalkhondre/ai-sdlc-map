---
id: safe-reference-model
type: concept
band: lifecycle
map_box: SAFe reference model (no map box; reached from Portfolio · Train · Team)
title: SAFe reference model
summary: A mapping from the levels, events and Continuous Delivery Pipeline of Core SAFe to the lifecycle pages of this site, for readers who plan in SAFe terms and want to see where each delivery decision falls.
key_terms: [reference-model, agile-release-train, planning-interval, pi-planning, wsjf, inspect-and-adapt, system-demo, continuous-delivery-pipeline, lifecycle-levels, workflow, specification-readiness, evidence-record, feedback-path, export-example]
sources: [oasis-soa-rm, safe-framework, safe-framework-home, safe-configurations, safe-ai-native-sense-and-respond, safe-portfolio, safe-art, safe-agile-teams, safe-large-solution, safe-solution-train, safe-lean-budgets, safe-guardrails, safe-strategic-themes, safe-portfolio-backlog, safe-epic, safe-wsjf, safe-cost-of-delay, safe-features, safe-story, safe-team-backlog, safe-iterations, safe-pi-planning, safe-pi-objectives, safe-system-demo, safe-inspect-and-adapt, safe-problem-solving-workshop, safe-art-backlog, safe-iteration-planning, safe-glossary, safe-team-backlog-refinement, safe-built-in-quality, safe-cdp, safe-continuous-exploration, safe-continuous-integration, safe-continuous-deployment, safe-release-on-demand, scrum-guide-2020, dora-2025-announcement, bockeler-harness, bockeler-sensors]
related: [lifecycle-levels, definition-of-ready-and-done, traceability-spine, inspect-and-adapt, workflows, software-factory, idea, specification, design, develop-build-qa, deploy, release, operate, harness-engineering, evidence-schema, rule-registry]
review_record: content/reviews/1.5.0-lifecycle.md
---

## Definition

A reference model, in the sense OASIS gives the term, is "an abstract framework for understanding
significant relationships among the entities of some environment"[^oasis-soa-rm]. OASIS wrote that
definition for service-oriented architecture; this page borrows the sense and not the subject. Here
the environment is delivery work in an AI SDLC (the software development lifecycle with AI agents
doing part of the work). The entities are the levels, events and pipeline aspects of the Scaled
Agile Framework (SAFe), published by Scaled Agile, Inc., on one side, and the lifecycle pages of this
site on the other. The page is "a reference model" in that sense: a mapping that shows which SAFe
item lines up with which page of this site, and why. The mapping is this site's recommended
practice. SAFe prints no such mapping, and no public study known to this site maps SAFe to
agent-assisted delivery.

The SAFe side rests on Core SAFe, the label SAFe's home page uses for the framework that AI-Native
SAFe builds on[^safe-framework-home], as published at framework.scaledagile.com and read on 20
November 2026. The Core SAFe articles used here print no version number, and this page claims none.
SAFe's configurations page is titled "SAFe 6.0 Configurations" and describes its contents as the
latest version of SAFe[^safe-configurations].

One note on AI-Native SAFe. AI-Native SAFe builds on Core SAFe, which continues alongside
it[^safe-framework-home]. In AI-Native SAFe, a two-hour Sense and Respond event at the boundary of
every iteration replaces the Core SAFe event Inspect and Adapt, and also includes the activities that
were in the System Demo[^safe-ai-native-sense-and-respond]. Both events are described below. Every
other statement on this page rests on Core SAFe.

The page is not SAFe guidance, not a prescription and not a description of any organisation. It does
not say how any organisation plans, staffs or runs its delivery. Three SAFe levels are used, each
defined here in SAFe's words so that the page reads without SAFe's own site:

- **Portfolio** is "a set of value streams that delivers a continuous flow of valuable solutions to
  customers within a common funding and governance model"[^safe-portfolio].
- **Agile Release Train (ART)** is "a long-lived team of Agile teams that incrementally develops,
  delivers, and often operates one or more solutions in a development value stream"[^safe-art].
- **Agile Team** is "a cross-functional group of typically ten or fewer individuals with all the skills
  necessary to define, build, test, and deliver value to their customer"[^safe-agile-teams].

SAFe also names Large Solution SAFe, "for enterprises building large and complex solutions that do
not require portfolio concerns"[^safe-large-solution], and the Solution Train, "the organizational
construct used to build large solutions that requires the coordination of multiple ARTs and
suppliers"[^safe-solution-train]. This model maps neither.

## Why it matters

A reader whose organisation plans in SAFe terms meets two vocabularies, the framework's and this
site's, and the delivery decisions that matter run across both. Without a mapping, two things go
wrong. A decision is placed at the wrong level, because a level name does not say which question
belongs to it: a readiness question that one team should settle before it takes the work on is
carried to an event for the whole train, or a funding question is settled inside a team. And events
are copied without the decisions they serve, so a planning or review meeting is held on schedule
while nobody can say which question it answers, which record it draws on or where its outcome is
written down. The mapping below keeps each event tied to the decisions (see
[workflows](workflows.html)) and records it touches. This is recommended-practice reasoning from the structure of the two vocabularies, not a
finding.

The site keeps its own generic level labels, Portfolio, Train and Team, so that its pages do not
depend on one framework's vocabulary. SAFe is cited as one framework whose levels sit at the same
altitudes under its own names: Portfolio, Agile Release Train and Agile Team. This page is where the
two sets of names are joined, so a reader can start from either.

The join matters more once agents do part of the work. DORA's announcement of its 2025 report puts
the risk plainly: "AI doesn't fix a team; it amplifies what's already there"[^dora-2025-announcement].
A team's levels, events and the decisions that belong to each are part of what is already there. If
they are clear, agent assistance speeds them up; if they are blurred, it speeds up the blur. No public
study known to this site maps SAFe to agent-assisted delivery, so the mapping below is this site's
recommended practice, stated as such wherever it makes a join.

## How it works

### What the model takes from SAFe

The model takes three levels (Portfolio, Agile Release Train and Agile Team), a set of SAFe events
and timeboxes, and the four aspects of SAFe's Continuous Delivery Pipeline. It takes the work items
that sit at each level only as far as the levels need them.

SAFe's Planning Interval (PI) is "a cadence-based timebox in which Agile Release Trains deliver
continuous value to customers in alignment with PI Objectives"[^safe-framework]. The three Core SAFe
cadence figures below are typical; none is a default or a requirement.

- A Planning Interval is typically 8 to 12 weeks. SAFe calls 8 to 12 weeks a good starting point and
  describes the pattern it gives for a PI as a suggestion rather than a strict rule[^safe-framework].
- PI Planning is typically two days[^safe-pi-planning].
- Iteration Planning is about 90 minutes for a two-week iteration[^safe-iteration-planning].

One sequence is enough for the mapping. A PI begins with PI Planning[^safe-framework]. Inspect and
Adapt is a significant event held at the end of each PI, and its improvement backlog items go into
the ART backlog for consideration in the next PI Planning event[^safe-inspect-and-adapt]. The model
says nothing about the order of events inside an iteration.

### Levels

The table sets each SAFe level against the generic label this site gives the same altitude and the
decision on this site that lines up with it. The labels link to the sections of the
[lifecycle levels](lifecycle-levels.html) page. Each decision is named as in the
[workflow catalog](workflow-catalog.html), and its identifier links to its row there.

| SAFe level | Label on this site | What SAFe places at the level | Decision on this site that lines up with it |
|---|---|---|---|
| Portfolio, a set of value streams under "a common funding and governance model"[^safe-portfolio] | [Portfolio](lifecycle-levels.html#portfolio): initiatives, prioritisation, budgets | Funding and prioritisation: Lean budgets and their guardrails, Strategic Themes, the Portfolio Backlog of epics, and WSJF[^safe-lean-budgets][^safe-guardrails][^safe-strategic-themes][^safe-portfolio-backlog][^safe-wsjf] | Intake and classification ([W01](workflow-catalog.html#W01)) |
| Agile Release Train, a "long-lived team of Agile teams"[^safe-art] | [Train](lifecycle-levels.html#train): features, planning cycle, integrated demo | Features delivered within a Planning Interval, with PI Planning, PI Objectives, the ART backlog, the System Demo and Inspect and Adapt[^safe-features][^safe-framework][^safe-pi-objectives][^safe-art-backlog][^safe-system-demo][^safe-inspect-and-adapt] | Specification readiness ([W04](workflow-catalog.html#W04)); plan and architecture conformance ([W08](workflow-catalog.html#W08)) |
| Agile Team, a cross-functional group with the skills to define, build, test and deliver value[^safe-agile-teams] | [Team](lifecycle-levels.html#team): stories, iterations, readiness and done | Stories, the Team Backlog, the iteration, Iteration Planning and Team Backlog Refinement[^safe-story][^safe-team-backlog][^safe-iteration-planning] | Task traceability and test planning ([W12](workflow-catalog.html#W12)) |

The decision in the last column sits beside the level's work. The site does not assign workflows to
levels, as the [lifecycle levels](lifecycle-levels.html) page states, so the column says which
decision a level's events and work items line up with and not which altitude runs it. The paragraphs
below give SAFe's own wording for each level's work items.

**Portfolio.** In SAFe the portfolio level holds funding and prioritisation. Lean budgets are "a
financial governance approach that funds value streams instead of projects"[^safe-lean-budgets], and
Lean budget guardrails "describe the policies and practices for budgeting, spending, and governance
for a specific portfolio"[^safe-guardrails]. Strategic Themes are portfolio-level business objectives
that connect the enterprise strategy to a portfolio[^safe-strategic-themes]. The Portfolio Backlog is
"a Kanban system that is used to capture and manage the business and enabler epics intended to create
and evolve the portfolio's products, services, and solutions"[^safe-portfolio-backlog], and an Epic is
"a significant solution development initiative"[^safe-epic]. In SAFe, WSJF (weighted shortest job
first) is estimated as the relative cost of delay divided by the relative job duration, from relative
user and business value, time criticality, risk reduction and/or opportunity enablement, and job
size[^safe-wsjf]. Cost of Delay is the money or value lost by delaying or not
doing a job for a time period, relative to other jobs[^safe-cost-of-delay]. SAFe's WSJF page opens
with an epigraph attributed to Don Reinertsen's *The Principles of Product Development
Flow*[^safe-wsjf], and this site credits WSJF to SAFe. On this site's side, the decision that lines up with this level is intake and classification ([W01](workflow-catalog.html#W01)). The join is recommended practice. Both the SAFe items and the intake
decision concern which work is taken up and how it is classified, and the map labels the level
"initiatives · prioritisation · budgets".

**Agile Release Train.** A Feature is "solution functionality that delivers business value, fulfills
a stakeholder need, and is sized to be delivered by an Agile Release Train within a PI"[^safe-features].
PI Planning is "a cadence-based event for the entire ART that aligns teams and stakeholders to a
shared mission and vision"[^safe-pi-planning], and PI Objectives "summarize the business and technical
goals that teams and trains intend to achieve in the upcoming PI and are either committed or
uncommitted"[^safe-pi-objectives]. The ART backlog is "a Kanban system used to capture and manage the
features and enablers that enhance the solution"[^safe-art-backlog]. The System Demo and Inspect and
Adapt are set against pages of this site in the events table below. On this site's side, the
decisions that line up with this level are specification readiness ([W04](workflow-catalog.html#W04))
and plan and architecture conformance ([W08](workflow-catalog.html#W08)). Their pages are [Specification](specification.html) and
[Design](design.html). The join is recommended practice and is stated only for the records these
decisions leave, which the site offers to a planning event.

**Agile Team.** A Story is a short description of a small piece of desired functionality written from
the user's perspective, and keeping stories small ensures they can be completed in a single
iteration[^safe-story]. The Team Backlog is "a Kanban system that is used to capture and manage the
user stories and enablers intended to enhance the solution"[^safe-team-backlog]. The team level is where stories are taken from
that backlog into an iteration: in Iteration Planning "the team defines, organizes, and commits to the
work for the next iteration"[^safe-iteration-planning]. On this site's side, the decision that lines up with this level
is task traceability and test planning ([W12](workflow-catalog.html#W12)). The map labels the level
"stories · iterations · DoR / DoD". The join is recommended practice.

The model maps decisions, not roles. SAFe defines roles of its own[^safe-art]. This site names the
role accountable for each decision in the workflow catalog, so no row on this page maps one SAFe role
to one role of this site.

### Events and cadence

The table sets each SAFe event the model uses against the page and
[workflow catalog](workflow-catalog.html) row it lines up with on this site. Apart from the sequence
given above, in which a PI begins with PI Planning[^safe-framework], the order of the rows implies no
order of events. Each join is this site's recommended mapping: the column of SAFe's words quotes what SAFe's
pages say an event is or produces, and none of the SAFe pages cited here says that an event reads a
record of this site.

| SAFe event | In SAFe's words | Lines up with on this site | Why the join holds |
|---|---|---|---|
| System Demo | "provides stakeholders an integrated view of new features for the most recent iteration delivered by all the teams on the ART"[^safe-system-demo] | [Release](release.html); release readiness ([W25](workflow-catalog.html#W25)) | Both bring the results of several changes together before a decision. The join is loose: the demo shows working features to stakeholders. |
| Iteration | "a standard, fixed-duration timebox during which Agile Teams and ARTs individually and collectively deliver incremental customer value while working towards the PI objectives"[^safe-iterations] | [Develop, Build and QA](develop-build-qa.html) | The iteration is the container and the three phases are the path one change takes inside it. The site draws one workflow, pull-request verification ([W23](workflow-catalog.html#W23)), across the three phases. |
| Inspect and Adapt | "a significant event held at the end of each PI", "structured into three parts: the PI System Demo, a quantitative and qualitative measurement review, and a retrospective and problem-solving workshop"[^safe-inspect-and-adapt]. The workshop is "a structured approach to identifying the root cause and actions to address systemic problems"[^safe-problem-solving-workshop]. Its output is "improvement backlog items that go into the ART Backlog for consideration in the next PI Planning event"[^safe-inspect-and-adapt], and the ART backlog is a Kanban system for the features and enablers that enhance the solution[^safe-art-backlog] | [Inspect and Adapt](inspect-and-adapt.html); incident-to-development feedback ([W28](workflow-catalog.html#W28)) | Both turn what was learned into changes to a backlog: SAFe's improvement backlog items on one side, and on this site's side a decision on which workflow to add or tighten next. |
| Team Backlog Refinement | "an event that helps Agile Teams clarify and prepare upcoming stories and features"[^safe-team-backlog-refinement] | [Specification](specification.html); specification readiness ([W04](workflow-catalog.html#W04)) | The clarifying and preparing that SAFe's sentence names is the work that answers the specification readiness decision. |
| PI Planning | "a cadence-based event for the entire ART that aligns teams and stakeholders to a shared mission and vision", typically two days long, with outputs of "committed PI objectives from the Agile Teams and an ART planning board that reflects feature delivery dates and dependencies"[^safe-pi-planning]. PI Objectives "summarize the business and technical goals that teams and trains intend to achieve in the upcoming PI and are either committed or uncommitted"[^safe-pi-objectives] | [Specification](specification.html); specification readiness ([W04](workflow-catalog.html#W04)); [Design](design.html); plan and architecture conformance ([W08](workflow-catalog.html#W08)) | PI Planning ends in commitments, and specification readiness and plan and architecture conformance are the decisions on this site that come before work is committed to. |
| Iteration Planning | "the team defines, organizes, and commits to the work for the next iteration", in about 90 minutes for a two-week iteration[^safe-iteration-planning]. Iteration Goals are "a high-level summary of the business and technical goals that an Agile Team agrees to accomplish in an Iteration"[^safe-glossary] | [Definition of Ready and Done](definition-of-ready-and-done.html); task traceability and test planning ([W12](workflow-catalog.html#W12)) | Both concern which work a team takes on. |

The lengths in the table are SAFe's typical figures and not defaults; the Pitfalls section returns to
this.

### The Continuous Delivery Pipeline against the phases

SAFe describes its Continuous Delivery Pipeline as "the workflows, activities, and automation needed
to guide new functionality from ideation to an on-demand release of value", with four aspects in this
order: continuous exploration, continuous integration, continuous deployment and release on
demand[^safe-cdp]. This site draws nine phases, in order: Idea, Specification, Design, Develop,
Build, QA, Deploy, Release and Operate.

| SAFe aspect | In SAFe's words | Phases on this site | Decision that lines up with it |
|---|---|---|---|
| Continuous exploration | "continually exploring the market and customer needs, defining a vision, roadmap, and set of features for a solution"[^safe-continuous-exploration] | [Idea](idea.html), [Specification](specification.html) | Intake and classification ([W01](workflow-catalog.html#W01)) and specification readiness ([W04](workflow-catalog.html#W04)) |
| Continuous integration | "new functionality is developed, tested, integrated, and validated in preparation for deployment and release"[^safe-continuous-integration] | [Develop, Build and QA](develop-build-qa.html) | Pull-request verification ([W23](workflow-catalog.html#W23)) |
| Continuous deployment | "automates the migration of new functionality from a staging environment to production, where it is made available for release"[^safe-continuous-deployment] | [Deploy](deploy.html) | Deployment and post-deploy verification ([W26](workflow-catalog.html#W26)) |
| Release on demand | "releases new functionality immediately or incrementally based on business and customer needs"[^safe-release-on-demand] | [Release](release.html) | Release readiness ([W25](workflow-catalog.html#W25)) |

Two phases have no row. SAFe's four aspects include none named for design or for operation, and the
table does not force a row for either. On this site's side, [Design](design.html) sits between the
first two aspects, and [Operate](operate.html) follows the last.

SAFe separates deployment from release. It states that "it's optimal to separate the deployment
process from releasing"[^safe-continuous-deployment] and that releases are "decoupled from the work to
deploy the functionality"[^safe-release-on-demand]. This site draws the same line: Deploy and Release
are separate phases with separate decisions, deployment and post-deploy verification
([W26](workflow-catalog.html#W26)) and release readiness ([W25](workflow-catalog.html#W25)), and the [Deploy](deploy.html) page sets out
the difference between deploying a build and releasing a change. The join of aspects to phases is this
site's recommended mapping.

### Ready, done and quality

SAFe's glossary defines the Definition of Done as something that "specifies the requirements for
completeness of a work product or increment of value"[^safe-glossary]. The Scrum Guide describes it as
a formal description of the state of the increment[^scrum-guide-2020]. Both treat done as a defined
state that work either meets or does not. The site's Definition of Done, which it takes from the Scrum
Guide, applies that state at three points: a story, an increment and a release. The map places its tag
at Release, and the [Definition of Ready and Done](definition-of-ready-and-done.html#done-at-three-levels)
page sets out each point.

Built-in quality is, in SAFe's words, "a set of practices to help ensure that the outputs of Agile
teams in business and technology domains meet appropriate quality standards throughout the process of
creating customer value"[^safe-built-in-quality]. The counterpart on this site, as recommended
practice, is the set of [validators](validators.html)[^bockeler-sensors] that run in
[Develop, Build and QA](develop-build-qa.html), each leaving an [evidence record](evidence-schema.html).

The entrance to the work is set out on this site's side by the
[Definition of Ready](definition-of-ready-and-done.html#definition-of-ready).

### The export feature through the model

The customer-record export is a hypothetical feature that lets users export customer records. It is
the site's [running example](software-factory.html#the-running-example-across-workflows).

The linked page follows the export through each workflow, and this page adds only where those
workflows sit against SAFe: the export's open readiness question, which roles may export which
records, is settled at specification readiness ([W04](workflow-catalog.html#W04)), the decision the events table sets beside
Team Backlog Refinement and PI Planning. That placement is this site's recommended mapping, not a
statement from SAFe.

## Where it sits on the map

The page has no box on the map. A reader reaches it from the Portfolio, Train and Team labels in the
lifecycle band, whose page, [lifecycle levels](lifecycle-levels.html), names SAFe as one framework
that uses those altitudes. A reader also reaches it from the lifecycle section's navigation and from
the [terminology](glossary.html) entries for the SAFe terms used here, such as the Agile Release Train,
the Planning Interval, WSJF and Inspect and Adapt.

Within the lifecycle band the page connects to the [lifecycle levels](lifecycle-levels.html) page, to
the phase pages named in the pipeline table, to
[Definition of Ready and Done](definition-of-ready-and-done.html), to the
[traceability spine](traceability-spine.html) that ties requirement to incident by identifier, and to
[Inspect and Adapt](inspect-and-adapt.html). In the core band it connects to
[Workflows](workflows.html), the [Software factory](software-factory.html),
[Harness engineering](harness-engineering.html)[^bockeler-harness], the [Evidence schema](evidence-schema.html) and the
[Rule registry](rule-registry.html).

Some labels outside the lifecycle band still carry SAFe's own words. The operating model box in the
enablement band mentions an Agile Release Train, a PI cadence, a system demo and Inspect and Adapt,
while the lifecycle band uses the generic labels Portfolio, Train and Team. A reader moving between
bands therefore meets both vocabularies on the map, and this page is the join between them.

## Pitfalls

- **Reading the mapping as SAFe's own, or as a requirement.** The joins on this page are this site's
  recommended practice and carry no authority from SAFe. A reference model, in the OASIS sense, is a
  framework for understanding relationships. Sign: a plan or a standard cites this page as the
  framework's rule, or attributes one of its joins to Scaled Agile.
- **Treating typical cadence figures as defaults.** SAFe calls 8 to 12 weeks a good starting point
  for a Planning Interval and describes its pattern for a PI as a suggestion rather than a strict
  rule[^safe-framework]. Sign: a calendar is fixed at the typical length of a PI, a planning event or
  an iteration planning meeting, with no reason recorded for the choice.
- **Forcing one workflow per SAFe event.** SAFe defines events by their purpose and timebox, for
  example PI Planning as "a cadence-based event for the entire ART"[^safe-pi-planning] and Inspect and
  Adapt as "a significant event held at the end of each PI"[^safe-inspect-and-adapt]. One event can
  line up with several decisions (see [Workflows](workflows.html)), as PI Planning does with
  specification readiness ([W04](workflow-catalog.html#W04)) and plan and architecture conformance
  ([W08](workflow-catalog.html#W08)) in the events table, and decisions such as pull-request
  verification ([W23](workflow-catalog.html#W23)) and deployment and post-deploy verification
  ([W26](workflow-catalog.html#W26)) line up with a pipeline aspect and with no event. Sign: a
  workflow is named after a meeting, or a decision with no meeting has no workflow.
- **Reading "done" as "released".** The Scrum Guide says an item that does not meet the Definition of
  Done "cannot be released or even presented at the Sprint Review"[^scrum-guide-2020]. Meeting it is a
  condition for a release decision, not the decision, and SAFe keeps deployment and release apart
  for the same reason[^safe-continuous-deployment][^safe-release-on-demand]. Sign: stories are counted
  as delivered before any release decision has been made on them.

## Related

- [Lifecycle levels](lifecycle-levels.html): the three altitudes this page maps, with the decisions
  each one holds.
- [Definition of Ready and Done](definition-of-ready-and-done.html): the readiness and done
  conditions the events and quality rows refer to.
- [Traceability spine](traceability-spine.html): the identifier chain from requirement to incident.
- [Inspect and Adapt](inspect-and-adapt.html): the checkpoint this page lines up with SAFe's event of
  the same name.
- [Idea](idea.html), [Specification](specification.html), [Design](design.html),
  [Develop, Build and QA](develop-build-qa.html), [Deploy](deploy.html), [Release](release.html) and
  [Operate](operate.html): the phases set against the pipeline aspects.
- [Workflows](workflows.html).
- [Software factory](software-factory.html).
- [Harness engineering](harness-engineering.html), [Evidence schema](evidence-schema.html) and
  [Rule registry](rule-registry.html).
- [Workflow catalog](workflow-catalog.html): rows intake and classification
  ([W01](workflow-catalog.html#W01)), specification readiness ([W04](workflow-catalog.html#W04)),
  plan and architecture conformance ([W08](workflow-catalog.html#W08)), task traceability and test
  planning ([W12](workflow-catalog.html#W12)), pull-request verification
  ([W23](workflow-catalog.html#W23)), release readiness ([W25](workflow-catalog.html#W25)),
  deployment and post-deploy verification ([W26](workflow-catalog.html#W26)) and
  incident-to-development feedback ([W28](workflow-catalog.html#W28)).
- [Terminology](glossary.html#reference-model): the reference model, the SAFe terms and their credits.

## Sources

The mapping of SAFe items to the pages of this site, and the statement that no public study known to
this site maps SAFe to agent-assisted delivery, are this site's recommended practice and carry no
source. The sources below support the SAFe-side wording and the two outside definitions.

- The reference-model definition: OASIS[^oasis-soa-rm].
- Core SAFe as a label, the configurations page title, and the AI-Native note:
  [^safe-framework-home], [^safe-configurations], [^safe-ai-native-sense-and-respond].
- Levels and their work items: [^safe-portfolio], [^safe-art], [^safe-agile-teams],
  [^safe-large-solution], [^safe-solution-train], [^safe-lean-budgets], [^safe-guardrails],
  [^safe-strategic-themes], [^safe-portfolio-backlog], [^safe-epic], [^safe-wsjf],
  [^safe-cost-of-delay], [^safe-features], [^safe-story], [^safe-team-backlog].
- Events, timeboxes and cadence figures: [^safe-framework], [^safe-pi-planning],
  [^safe-pi-objectives], [^safe-system-demo], [^safe-inspect-and-adapt],
  [^safe-problem-solving-workshop], [^safe-art-backlog], [^safe-iteration-planning],
  [^safe-team-backlog-refinement], [^safe-iterations], [^safe-glossary].
- The Continuous Delivery Pipeline: [^safe-cdp], [^safe-continuous-exploration],
  [^safe-continuous-integration], [^safe-continuous-deployment], [^safe-release-on-demand].
- Done and quality: [^safe-glossary], [^safe-built-in-quality], [^scrum-guide-2020].
- AI and delivery: [^dora-2025-announcement].
