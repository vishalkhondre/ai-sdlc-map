---
id: software-factory
type: concept
band: core
map_box: Software factory
title: Software factory
summary: The operating state that appears when delivery workflows share one set of rules, one evidence format and one feedback path, so that what production teaches changes what the next specification asks.
key_terms: [software-factory, workflow, evidence-handoff, feedback-path, steering-loop, harness, harness-template, rule-registry, evidence-record, engineering-kit, harness-engineering, validator, specification-readiness, three-roles, skill-erosion, export-example]
sources: [cusumano-software-factories, greenfield-software-factories, shapiro-five-levels, willison-software-factory, morris-humans-agents-loops, bockeler-harness, bockeler-sensors, dora-2024-report, dora-2025-report, dora-2025-announcement, dora-ai-capabilities, dora-customer-feedback, tw-incremental-developer-platform, team-topologies-tvp, google-sre-postmortem, conway-committees, lean-vs-manager, nist-ssdf, tw-radar-security-policy-as-code, bainbridge-ironies, lee-genai-critical-thinking, safe-inspect-and-adapt, scrum-guide-2020]
related: [workflows, harness-engineering, engineering-kit, rule-registry, evidence-schema, validators, skills-and-evals, adapters, traceability-spine, inspect-and-adapt, lifecycle-levels, definition-of-ready-and-done, pull-request-verification, incident-feedback]
review_record: content/reviews/1.4.0-core.md
---

## Definition

A software factory, in the sense this site uses, is the operating state that appears when enough
delivery workflows share one set of rules, one format for evidence and one path for feedback, so
that what production teaches changes what the next specification asks. It is not a product, a
platform or a team that can be bought or set up on a given day. It is a property of how workflows
that already run are connected. In an AI SDLC (the software development lifecycle with AI agents
doing part of the work), the factory keeps people at every decision point: what makes it a factory
is the shared thread of rule identifiers, evidence and recorded decisions, not unattended output.

The sense is coined by this site, and the phrase has older meanings that are not intended here.
Cusumano used it for Japanese firms that applied engineering and production-management discipline
to large-scale software development[^cusumano-software-factories]. Greenfield and Short used it
for a configuration of languages, patterns, frameworks and tools that produces variants of a
standard product from models[^greenfield-software-factories]. Both describe standardised,
repeatable production. Recent practitioner writing uses "dark software factory" for the far end of
agent-assisted development, named after a factory run by robots with the lights
out[^shapiro-five-levels], and one publicly described team works to the principles that code is
neither written nor reviewed by people, with validation against scenarios in place of code
review[^willison-software-factory]. This site means neither identical outputs nor removed human
review.

## Why it matters

A single workflow improves one delivery decision. Several workflows that share nothing improve
several decisions separately, and each lesson stays where it was learned. An incident is fixed in
code, and the next specification repeats the gap that let it through. Each workflow keeps its own
copy of the rules, and the copies drift until two workflows enforce different versions of the same
rule. Evidence written in one format cannot be read by the next workflow unless someone copies it
across by hand.

Research on AI adoption suggests why the connections matter more as agents do more of the work.
DORA's 2025 research describes AI's primary role as an amplifier that magnifies an organisation's
existing strengths and weaknesses[^dora-2025-report]. DORA's announcement of that report observes
a positive relationship between AI adoption and software delivery throughput, and a continuing
negative relationship with software delivery stability[^dora-2025-announcement]. Its 2024 research
found that AI adoption negatively affects software delivery stability and throughput, and reminded
teams that fundamentals such as small batch sizes and robust testing remain
crucial[^dora-2024-report]. DORA
also groups customer feedback with value-stream visibility, small batches and team
experimentation as capabilities that help predict delivery and organisational
performance[^dora-customer-feedback]. None of this is a finding about software factories: no
public study shows that connecting agent workflows through shared rules, evidence and feedback
improves outcomes. What follows is recommended practice, built on that adjacent evidence.

## How it works

### It emerges from workflows that already run

No team starts by building a factory. It starts with one workflow that runs on real changes, such
as [pull-request verification](pull-request-verification.html), and adds another once the first is trusted. Shared parts appear when
a second workflow needs something the first already has: it reads the access rule from the
registry instead of keeping its own copy, and it reads check results in the format the first
workflow already writes. Nothing moves into the shared layer until a workflow in use has needed it.
Guidance on internal platforms points the same way. The Thoughtworks Technology Radar observes that
teams often aim for too much of a platform vision too fast, and recommends growing a platform in
increments[^tw-incremental-developer-platform] from what Team Topologies calls the thinnest viable
platform: a platform kept no thicker than its users need, which can start as little more than a
wiki page[^team-topologies-tvp]. DORA lists quality internal platforms among the capabilities that amplify
the benefits of AI[^dora-ai-capabilities], so the risk lies in building shared parts ahead of the
workflows that show what they must hold, not in having them. Growing the shared layer only from
workflows that already run is this site's recommended practice.

### Three things are shared

- **Rules.** Every workflow reads its rules from one [rule registry](rule-registry.html), and the
  checks, skills and records in each workflow cite the same rule identifiers, so a change to a rule
  reaches every workflow at once instead of being copied into each. NIST's secure development
  framework asks for security requirements to be known at all times and maintained over time, so
  that the information is collected once and shared[^nist-ssdf], and security policy as code keeps
  such policies as versioned files that the pipeline validates[^tw-radar-security-policy-as-code].
- **Evidence.** Every workflow writes its results in the one shape the
  [evidence schema](evidence-schema.html) fixes, and the next workflow reads that record instead of
  asking the same questions again. A check that produced no verdict is recorded as `could_not_run`
  with its cause.
- **Feedback.** One feedback path decides where each lesson goes, and the change lands upstream of
  where the problem appeared. Böckeler calls the same practice the steering loop, in which people
  improve the harness (the context, tools, permissions and checks around an agent) based on
  recurring failures[^bockeler-harness]. She also proposes harness templates, bundles of guides and
  sensors for a common type of service, which carry one team's controls to the next service of the
  same kind[^bockeler-harness]. The [Engineering Kit](engineering-kit.html) is the artefact that
  carries the shared rules, the deterministic checks (what Böckeler's sensors writing treats as
  computational sensors[^bockeler-sensors]) and the evidence schema from one workflow and one team
  to the next.

### Production feedback reaches specification

A lesson from production does the most good when it changes a part that many workflows read. When
an incident review finds that a miss began before any code was written, the change it leads to
lands in a shared part, such as a rule in the registry, a readiness question or an evaluation case.
From then on every later change, in every workflow that reads that part, meets the lesson without
anyone having to remember it. That reach is what separates a factory from a set of workflows that
each learn alone; it is this site's model, not a measured finding. The
[Incident feedback](incident-feedback.html) workflow decides which earlier control changes, and the
[feedback path](harness-engineering.html#the-steering-loop-and-the-feedback-path) is how the
finding travels there.

The practice underneath is well established. NIST's secure development framework asks teams to
analyse root causes over time to find patterns, and to review and update the development process
itself so that a root cause does not recur[^nist-ssdf]. Böckeler's steering loop improves the
guides and sensors around an agent whenever an issue happens more than once[^bockeler-harness].
The change also has to be made, not just agreed: Google's site reliability workbook observes that
action items without clear owners are less likely to be resolved, and gives every action item an
owner and a tracking number[^google-sre-postmortem].

### The running example across workflows

In the customer-record export, a hypothetical feature that lets users export customer records,
the specification readiness workflow finds that the specification does not yet say which roles
may export which records, the question the access rule R-042 turns on. The product owner answers
it before planning, because it concerns what the feature is for; the security owner, who owns
R-042, confirms that the answer stays within the rule. The pull-request verification workflow
reads that readiness record and runs the R-042 validator and the 50k-row load scenario tied to the
volume-limit rule R-017. On the first pull request the validator fails on the background worker's
broader query, and the load scenario reports `could_not_run` because the load-test tool is missing
from the runner image. The worker's query is narrowed, the runner image gains the tool, and the
checks run again. The release readiness workflow reads the resulting evidence record instead of
asking the same questions again.

In production, a scheduled full export, within R-017's limit but far larger than the 50k-row scenario, times out. The
incident review traces the miss to specification: nobody asked what the largest export would be,
so the scenario was sized for ordinary requests. Three changes follow. A larger load scenario joins
the checks tied to R-017, the agent's evaluation set gains a case for the long-running export, and
the readiness workflow now asks every export-like specification for the largest export it expects.
The next export-like feature meets that question before planning starts. The identifiers R-042 and
R-017 run through every record in the story; that shared thread, not any tool, is the factory.

### People keep the decisions

In each workflow the agent does the drafting: open questions on a specification, plans, code and
first reviews.
Deterministic checks settle whatever can be settled mechanically, and named people decide what
needs context no workflow holds, such as which roles may export which records. The agent never
fills a decision field in the evidence record. Morris describes the human role as working on the
loop: people build and adjust the loop that produces the work, rather than inspecting every output
or leaving the agents to it[^morris-humans-agents-loops]. Autonomy widens in that direction. When
the same human correction keeps recurring, it becomes a rule and a check, and the person's review
narrows to what the checks cannot decide; the decision point stays, while the mechanical part of
it moves to a gate. Widening autonomy only by turning repeated judgments into checks, never by
dropping an approval, is this site's recommended practice.

## Where it sits on the map

The software factory is the fourth box of the core band (band 3, "what does the work"). The row
reads Harness engineering, then the Engineering Kit, then Workflows, then the software factory:
it comes after the discipline, the artefact and the unit of work. The map labels it the operating
state and draws it with a dashed border, because it emerges from the other three rather than
being built beside them. It is distinct from the operating model box in the enablement band, which
covers team cadence and decision rights. In the lifecycle band, the map places each workflow in its
phase, draws the loop by which incident feedback changes what specification asks, and runs a
traceability spine from requirement to incident, linked by rule identifiers. The spine and the
periodic review of delivery evidence are covered on the
[Traceability spine](traceability-spine.html) and [Inspect and Adapt](inspect-and-adapt.html)[^safe-inspect-and-adapt]
pages. The enablement band
holds the runtime and tools, the people and roles, and that operating model, all of which the
factory depends on. The assurance band holds the evidence record on every run and the measurement
that shows whether the connections help. The adoption path's final stage, "Factory emerges", is
where a team tests whether it has reached this state; that stage sets the criteria.

## Pitfalls

- **Skill erosion.** Bainbridge argued that when automation does most of a task, people are left
  monitoring it, and manual skills they no longer practise deteriorate, which makes taking over
  harder[^bainbridge-ironies]. A survey of knowledge workers found that higher confidence in
  generative AI went with less critical thinking, on self-reported
  data[^lee-genai-critical-thinking]. The factory relies on human judgment at every decision point,
  so as recommended practice the people who hold those decisions still do some of the work
  unaided. The sign is people who struggle to take over when the agent or its checks are
  unavailable.
- **Connections nobody owns.** Each workflow has an owner, but the shared parts between them, the
  rules, the evidence format and the feedback path, have none, so each workflow adjusts them to
  suit itself. Conway observed that a system's design copies the communication structure of the
  organisation that builds it, and that two connected parts need their designers to agree on the
  interface between them[^conway-committees]; on that reading, a connection nobody owns is a
  conversation nobody holds. Lean practice gives a flow that crosses many hands one accountable
  person who need not own its resources[^lean-vs-manager], and as recommended practice each shared
  part has one such owner; who grants that role is a matter for the operating model in the
  enablement band. The sign is two workflows citing different revisions of the same rule.
- **Reading the factory as unattended throughput.** Treating human decision points as the
  bottleneck to remove turns the factory into the lights-out sense this site does not mean, and
  DORA's 2024 research, which found that AI adoption negatively affects delivery stability, reminds
  teams that small batch sizes and robust testing remain crucial[^dora-2024-report]. The sign is a proposal to waive a check or drop an approval to keep up
  with agent output.
- **Lessons that never close.** Incident reviews write actions that never reach the stage that
  owns the gap. The sign is the same kind of miss recurring after it has been reviewed, or actions
  with no single owner[^google-sre-postmortem].

## Related

- [Workflows](workflows.html): the unit of work the factory connects, with its trigger, checks,
  human decision, evidence and owner.
- [Harness engineering](harness-engineering.html): the discipline behind the controls the factory
  shares.
- [Engineering Kit](engineering-kit.html): the versioned package that carries the shared rules,
  checks and evidence schema between workflows and teams.
- [Rule registry](rule-registry.html): the shared rules, each with an identifier, how it is enforced
  and an owner.
- [Evidence schema](evidence-schema.html): the fixed shape of the record every workflow writes and
  the next one reads.
- [Validators](validators.html), [Skills with evals](skills-and-evals.html) and
  [Adapters](adapters.html): the kit's other parts.
- [Workflow catalog](workflow-catalog.html): the list of workflows the factory draws on.
- [Pull-request verification](pull-request-verification.html): whether one revision of a change may join the mainline.
- [Incident feedback](incident-feedback.html): which earlier control changes after an incident.
- [Traceability spine](traceability-spine.html): the chain of linked artefacts from requirement to
  incident.
- [Inspect and Adapt](inspect-and-adapt.html): the periodic checkpoint at which delivery evidence
  is read together.
- [Lifecycle levels](lifecycle-levels.html): the portfolio, train and team levels at which the
  lifecycle runs.
- [Definition of Ready and Definition of Done](definition-of-ready-and-done.html): the entry and
  exit criteria for an item of work, including the Definition of Done from the Scrum
  Guide[^scrum-guide-2020].
- [Terminology](glossary.html#software-factory): the glossary entry and the credit for each term.

## Sources

- Cusumano, *Japan's Software Factories*: an earlier, production-management sense of the
  term[^cusumano-software-factories].
- Greenfield and Short, *Software Factories*: the model-driven sense of the
  term[^greenfield-software-factories].
- Shapiro, the five levels of AI-assisted programming, and Willison's account of a team whose code
  no person writes or reviews: recent senses of the term that differ from this
  site's[^shapiro-five-levels][^willison-software-factory].
- Morris on people working on the loop[^morris-humans-agents-loops]; Böckeler on the steering
  loop, harness templates and sensors[^bockeler-harness][^bockeler-sensors].
- DORA's 2024 and 2025 research on AI adoption, its announcement of the 2025 report, its AI
  capabilities model and its customer feedback
  capability[^dora-2024-report][^dora-2025-report][^dora-2025-announcement][^dora-ai-capabilities][^dora-customer-feedback].
- Thoughtworks on incremental developer platforms, and Team Topologies on the thinnest viable
  platform[^tw-incremental-developer-platform][^team-topologies-tvp].
- The site reliability engineering workbook on postmortem ownership[^google-sre-postmortem];
  Conway on organisations and system design[^conway-committees]; the Lean Enterprise Institute on
  the value-stream manager[^lean-vs-manager].
- NIST's Secure Software Development Framework on shared security requirements and on changing the
  process after root-cause analysis[^nist-ssdf]; the Thoughtworks Technology Radar on security
  policy as code[^tw-radar-security-policy-as-code].
- Bainbridge, and Lee and colleagues, on automation and critical
  thinking[^bainbridge-ironies][^lee-genai-critical-thinking].
- Scaled Agile, Inc., *Inspect and Adapt*: SAFe's Inspect and Adapt event[^safe-inspect-and-adapt].
- Schwaber and Sutherland, *The 2020 Scrum Guide*: the Definition of Done[^scrum-guide-2020].
