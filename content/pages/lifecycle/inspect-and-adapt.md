---
id: inspect-and-adapt
type: role-or-practice
band: lifecycle
map_box: Inspect & Adapt
title: Inspect and Adapt
summary: The periodic checkpoint where the evidence delivery produced, from the traceability spine and from incident feedback, is read together and a workflow is added or tightened as a result.
key_terms: [inspect-and-adapt, feedback-path, steering-loop, software-factory, could-not-run, failure-path, evidence-handoff, evidence-record, workflow, harness-engineering, export-example]
sources: [safe-inspect-and-adapt, safe-ia-facilitators-guide, safe-rte, safe-iteration-retrospective, safe-glossary, safe-ai-native-sense-and-respond, safe-framework-home, safe-framework, scrum-guide-2020, agile-manifesto-principles, google-sre-postmortem, nist-800-61r3, google-agentic-sre, dora-2025-announcement, dora-ai-capabilities-impact, bockeler-harness, ahmed-incident-llm, chen-rcacopilot, bockeler-sensors, safe-art, oasis-soa-rm, safe-system-demo, safe-pi-planning]
related: [traceability-spine, operate, specification, definition-of-ready-and-done, lifecycle-levels, safe-reference-model, harness-engineering, software-factory, workflows]
review_record: content/reviews/1.5.0-lifecycle.md
---

## Purpose

In the AI SDLC (the software development lifecycle with AI agents doing part of the work), every
workflow leaves evidence behind: check results, human decisions, escaped defects and incident
records. Inspect and Adapt is the checkpoint where the people who own those workflows read that
evidence together and decide which workflow to add or tighten next. It closes one loop, from what
delivery showed to what the next workflow does. Without it, each lesson stays where it was
learned: an incident is reviewed, the review is filed, and the next specification repeats the gap.
The checkpoint is where the feedback path (see [harness engineering](harness-engineering.html))
is reviewed as a whole and not one incident at a time.

The name comes from the Scaled Agile Framework (SAFe). SAFe describes Inspect and Adapt as "a
significant event held at the end of each PI", where a PI is a Planning Interval, SAFe's
cadence-based timebox in which Agile Release Trains deliver value.[^safe-inspect-and-adapt][^safe-framework]
SAFe structures the event "into three parts": the PI System Demo[^safe-system-demo], a quantitative and qualitative
measurement review, and a retrospective and problem-solving workshop.[^safe-inspect-and-adapt]
SAFe defines the System Demo as an integrated view of the new features of the most recent
iteration, delivered by all the teams on the Agile Release Train (ART).[^safe-glossary][^safe-art]
The event's output is "improvement backlog items that go into the ART Backlog for consideration in
the next PI Planning event".[^safe-inspect-and-adapt] SAFe gives the cadence as typical, not fixed:
it calls a Planning Interval of 8 to 12 weeks a good starting point, and the pattern of iterations
within it "a suggestion rather than a strict rule".[^safe-framework] This page uses the name and
the purpose of the event, not its calendar. How often the checkpoint runs, and how it fits team
cadences, belongs to the operating model in the enablement section.

The idea sits on older foundations. The last of the twelve principles behind the Agile Manifesto
reads, "At regular intervals, the team reflects on how to become more effective, then tunes and
adjusts its behavior accordingly."[^agile-manifesto-principles] SAFe's page quotes that principle
and states that "The I&A amplifies the original principle".[^safe-inspect-and-adapt] The 2020
Scrum Guide names "transparency, inspection, and adaptation" as "the empirical Scrum pillars" and
adds that "Inspection without adaptation is considered pointless."[^scrum-guide-2020] The Guide
gives the Sprint Retrospective, the team-level event, this purpose: "to plan ways to increase
quality and effectiveness", and says the team inspects "individuals, interactions, processes,
tools, and their Definition of Done".[^scrum-guide-2020] SAFe's counterpart for teams is the
Iteration Retrospective, "a regular event held at the end of each iteration during which Agile
Teams review their results to identify improvements for future work".[^safe-iteration-retrospective]
Inspect and Adapt as this page uses it works one level above those team events. It reads
evidence across workflows, and the change it makes is to a workflow, a rule, a check or the
harness (the context, tools, permissions and checks around an agent).

One note on SAFe's newer line. In Core SAFe the event is Inspect and Adapt; in AI-Native SAFe a
Sense and Respond event replaces it and also takes on the activities of the System Demo, while
Core SAFe itself is not replaced and continues to provide SAFe's operating model for
scaling Lean and Agile practices.[^safe-ai-native-sense-and-respond][^safe-framework-home]

## Responsibilities

The checkpoint owns one job: turning evidence into changes that have owners. A review that
reports on delivery without changing a workflow, a rule or a check has not done that job.

### What it inspects

The checkpoint reads four kinds of evidence, and each has a page behind it.

- **Incident feedback records, and which conversion landed.** The checkpoint reads whether each
  conversion arrived where it was sent (see incident-to-development feedback,
  [W28](workflow-catalog.html#W28)).
- **Orphans and missing links on the spine, and `could_not_run` results by cause.** The
  [traceability spine](traceability-spine.html) is checked for artefacts with no link on one side.
  Results that could not run are read by cause, as the [workflows](workflows.html) page
  describes.
- **Exceptions.** The checkpoint reads where exceptions to rules cluster. A single exception is a
  decision about one change; the same exception granted to change after change suggests that the
  rule, and not the changes, needs another look, which is for the rule's named owner to settle (see
  [software factory](software-factory.html) and [rule registry](rule-registry.html)).
- **Report-only checks.** The checkpoint reads which of them have earned the right to become
  required (see [software factory](software-factory.html)).

The checkpoint also reads delivery measures; their definitions belong to the assurance band of the
map.

### Who attends and decides

Attendance follows the workflows under review, and each person is present by title.

- **The owner of each workflow under review.** See [workflows](workflows.html).
- **The named owner of each rule under discussion.** See [rule registry](rule-registry.html).
- **The people who decide in the workflows concerned.** Each catalog row names its deciders, for
  example specification readiness ([W04](workflow-catalog.html#W04)), release readiness
  ([W25](workflow-catalog.html#W25)), deployment and post-deploy verification
  ([W26](workflow-catalog.html#W26)) and incident remediation ([W27](workflow-catalog.html#W27)).

SAFe has the Release Train Engineer facilitate its event. The facilitator's guide says the three
parts are "typically facilitated by the Release Train Engineer (RTE)",[^safe-ia-facilitators-guide]
and SAFe describes the RTE as a servant leader and ART coach who facilitates ART events and
processes.[^safe-rte] This page does not fix a facilitator or a rule for who casts the deciding
vote. Decision rights between these titles belong to the operating model in the enablement
section.

### What it may change

The checkpoint may add a workflow or tighten one that already runs. The change it makes follows
the feedback path (see [harness engineering](harness-engineering.html)).

A report-only check becoming required is a further change it may make. The merge, release and
deployment decisions keep the deciders the workflow catalog names (see pull-request verification
([W23](workflow-catalog.html#W23)), release readiness ([W25](workflow-catalog.html#W25)) and
deployment and post-deploy verification ([W26](workflow-catalog.html#W26))). As recommended
practice, the checkpoint changes the workflows around those decisions, not who holds them.

### What it produces and where the output goes

The output is the set of conversions and tightened workflows the checkpoint decides on, each with
one named owner and the workflow it lands in. Google's Site Reliability Workbook notes that
postmortem action items with little or no ownership are less likely to be resolved, and that the
value of a postmortem is proportional to the learning it creates.[^google-sre-postmortem] Each
item goes to the place that holds the thing it changes. For lessons from incidents, the
destinations are those of incident-to-development feedback ([W28](workflow-catalog.html#W28)) and
of the [feedback path](glossary.html#feedback-path). Other frameworks make the same move. SAFe
sends improvement items to the ART backlog,[^safe-inspect-and-adapt] and the Scrum Guide says impactful improvements
"may even be added to the Sprint Backlog for the next Sprint".[^scrum-guide-2020] In incident
response, NIST SP 800-61 Revision 3 (April 2025) says that lessons learned from performing all
activities in all of the CSF 2.0 Functions are fed into Improvement (the ID.IM category).[^nist-800-61r3]

### In the customer-record export

The customer-record export is a hypothetical feature that lets users export customer records.
After a hypothetical production incident in which a scheduled full export times out, three
changes follow upstream: to the load scenario tied to the volume-limit rule R-017, to the agent's
evaluation set, and to what readiness asks of export-like specifications (see
[software factory](software-factory.html)).

At the checkpoint the owners read whether those three landed. For the load scenario, the question
is whether it ran or returned `could_not_run`. On the export's first pull request the R-017 load
scenario returned `could_not_run` (see [workflows](workflows.html)); a repeat for the same cause is
a checkpoint item and not a coding defect. For the evaluation case, the question is whether it
exists and passes (see evaluation rerun, [W35](workflow-catalog.html#W35)). For the readiness change,
the question is whether the next export-like specification was asked the new question. This
reading of the three changes is recommended practice.

Exceptions are read the same way. If the export keeps needing exceptions to R-017's row limit,
the checkpoint treats that as a question about the limit for the owner of R-017, not as one more
request to grant. R-042 gives no such reading, because an access rule is not open to exception
(see the failure paths in [workflows](workflows.html#failure-paths)).

## What shifts with agents

Agents change what is prepared for the checkpoint and add two new things to inspect. They do not
change its purpose or who decides. No public study examines agents and this checkpoint in
particular, so the statements below are recommended practice unless a source is named.

### What an agent prepares

Agents are described as consolidating and summarising incident data, creating handoff documents
and automatically creating drafts of incident postmortems.[^google-agentic-sre] On this site, the
workflow that carries incident lessons back to development is incident-to-development feedback
([W28](workflow-catalog.html#W28)).
Research points the same way for root-cause work. A study presented at ICSE 2023 evaluated large language models for helping engineers find the root cause of production incidents
and recommend mitigations, over more than 40,000 incidents.[^ahmed-incident-llm] A preprint
describes a system that routes an incident to a handler, aggregates diagnostic information,
predicts the incident's root-cause category and gives an explanatory narrative, evaluated on a
year of incidents from one large software company.[^chen-rcacopilot] These sources describe what
such systems do; this page takes no outcome from them as a finding. As recommended practice, a
proposed root cause enters the checkpoint as a hypothesis the owner tests, not as a conclusion.

### What stays with people

Google's account of agents in incident management says that an agentic approach does not
necessarily imply removing people from the process, specifically for higher-risk services and
features.[^google-agentic-sre] At this checkpoint, what stays with people is the judgement it
exists for: choosing which change to make, naming the person who owns it, and accepting or
rejecting what an agent proposes. An agent's summary or proposed root cause is material for that
judgement, never a decision in itself. A change to a rule stays with the rule's named owner (see
[rule registry](rule-registry.html)), and the decisions inside each workflow, such as release
readiness ([W25](workflow-catalog.html#W25)) or incident-to-development feedback
([W28](workflow-catalog.html#W28)), keep the deciders their catalog rows name. These statements
are recommended practice.

### What is new to inspect

- **Agent behaviour.** The checkpoint reads where agents repeatedly stumbled and whether the
  guides, sensors or permissions around them should change (see
  [harness engineering](harness-engineering.html)).[^bockeler-harness]
- **Volume of change against controls.** DORA's 2025 announcement says that without robust control
  systems, such as strong automated testing, mature version control practices and fast feedback
  loops, an increase in change volume leads to instability, and that "AI doesn't fix a team; it
  amplifies what's already there".[^dora-2025-announcement] The same research reports that in 2025
  AI adoption has a positive relationship with delivery throughput and a continued negative
  relationship with delivery stability.[^dora-2025-announcement] DORA also notes that AI can easily
  generate massive blocks of code, which are hard to review and test.[^dora-ai-capabilities-impact]
  At the checkpoint, the question is whether the controls grew with the volume of agent output.
- **Controls on what agents can change in production.** Google's account of agents in incident
  management stresses having consistent controls to prevent unwanted mutations of production
  state.[^google-agentic-sre] The checkpoint reads whether such controls apply to every agent
  that touches production, not only to the first one adopted.

### What does not change

The checkpoint's purpose is the Scrum Guide's: inspection without adaptation is
pointless.[^scrum-guide-2020] A report that produces no change has failed whoever prepared it.

## Warning signs

The checkpoint has become a report with no consequences when these signs appear.

- **Findings without owners, or actions that never reach a workflow.** The list of items from the
  last checkpoint has entries with no single name, or entries that are in no workflow's backlog,
  rule registry or evaluation set. Action items without clear owners are less likely to be
  resolved,[^google-sre-postmortem] and inspection without adaptation is considered
  pointless.[^scrum-guide-2020]
- **The same kind of miss recurs after it was reviewed.** See
  [software factory](software-factory.html).
- **The same exception is granted again for one rule.** See [workflows](workflows.html) and
  [software factory](software-factory.html).
- **`could_not_run` counts rise and nobody is told.** See [evidence schema](evidence-schema.html).
- **Only the demonstration is reviewed.** The meeting shows what shipped, but nobody reads the
  evidence or the conversions. SAFe's event has three parts, of which the demonstration is only
  the first.[^safe-inspect-and-adapt]

## Related

- [Traceability spine](traceability-spine.html): the links from requirement to incident that the
  checkpoint reads for orphans.
- [Operate](operate.html): where incidents and their feedback arise.
- [Specification](specification.html): where a misunderstood requirement turns into a readiness
  question.
- [Definition of Ready and Definition of Done](definition-of-ready-and-done.html): the criteria a
  conversion may tighten.
- [Lifecycle levels](lifecycle-levels.html): the portfolio, train and team levels of work, and the
  lessons that flow up from them to this checkpoint.
- [SAFe reference model](safe-reference-model.html): this site's mapping of the lifecycle onto SAFe,
  including where SAFe's event sits.
- [Harness engineering](harness-engineering.html): the discipline whose steering loop this
  checkpoint reviews.
- [Software factory](software-factory.html): the operating state that the feedback path makes
  possible.
- [Workflows](workflows.html): the unit of work whose owner attends.
- Workflow catalog rows: incident-to-development feedback ([W28](workflow-catalog.html#W28)),
  incident remediation ([W27](workflow-catalog.html#W27)), specification readiness
  ([W04](workflow-catalog.html#W04)), evaluation rerun ([W35](workflow-catalog.html#W35)), release
  readiness ([W25](workflow-catalog.html#W25)), pull-request verification
  ([W23](workflow-catalog.html#W23)) and deployment and post-deploy verification
  ([W26](workflow-catalog.html#W26)).
- [Rule registry](rule-registry.html), [Evidence schema](evidence-schema.html),
  [Skills with evals](skills-and-evals.html) and [Validators](validators.html): where a
  conversion lands.
- [The adoption path](index.html#adoption): the sequence in which a team builds the workflows
  this checkpoint reviews.
- Terminology: [Inspect and Adapt](glossary.html#inspect-and-adapt),
  [feedback path](glossary.html#feedback-path), [steering loop](glossary.html#steering-loop),
  [software factory](glossary.html#software-factory), [could_not_run](glossary.html#could-not-run).

## Sources

- SAFe, Inspect and Adapt: the event as held at the end of each Planning Interval, its three
  parts and its output.[^safe-inspect-and-adapt] SAFe's facilitator's guide for the event, and its
  pages on the Release Train Engineer, the Iteration Retrospective and the System Demo
  entry.[^safe-ia-facilitators-guide][^safe-rte][^safe-iteration-retrospective][^safe-glossary]
  SAFe's Planning Interval page for the typical timebox,[^safe-framework] and its PI Planning page
  for the name of the planning event that receives the event's output.[^safe-pi-planning]
- SAFe's Sense and Respond page and framework home page, for the single note on AI-Native
  SAFe.[^safe-ai-native-sense-and-respond][^safe-framework-home]
- The 2020 Scrum Guide on the empirical pillars and the Sprint Retrospective,[^scrum-guide-2020]
  and the principles behind the Agile Manifesto.[^agile-manifesto-principles]
- Incident learning: the Site Reliability Workbook on postmortem culture,[^google-sre-postmortem]
  NIST SP 800-61 Revision 3,[^nist-800-61r3] and Google's account of agents in incident
  management.[^google-agentic-sre]
- Research on language models for incident root-cause analysis.[^ahmed-incident-llm][^chen-rcacopilot]
- AI adoption and delivery: DORA's 2025 announcement and its AI Capabilities Model
  article.[^dora-2025-announcement][^dora-ai-capabilities-impact]
- Birgitta Böckeler on the steering loop, which this site adapts as the feedback
  path,[^bockeler-harness] and on computational sensors, which this site calls
  validators.[^bockeler-sensors]
- The sense of "reference model" in the name of the SAFe reference model page: the OASIS Reference
  Model for Service Oriented Architecture.[^oasis-soa-rm]
- Statements marked as recommended practice are this site's own and are not findings of any study.
