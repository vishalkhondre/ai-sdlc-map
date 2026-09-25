---
id: software-factory
type: concept
band: core
map_box: Software factory
title: Software factory
summary: The operating state that appears when delivery workflows share one set of rules, one evidence format and one feedback path, so that what production teaches changes what the next specification asks.
key_terms: [software-factory, workflow, evidence-handoff, feedback-path, steering-loop, harness, harness-template, rule-registry, evidence-record, engineering-kit, harness-engineering, validator, specification-readiness, three-roles, skill-erosion, export-example]
sources: [cusumano-software-factories, greenfield-software-factories, shapiro-five-levels, willison-software-factory, morris-humans-agents-loops, bockeler-harness, bockeler-sensors, dora-2024-report, dora-2025-report, dora-ai-capabilities, dora-customer-feedback, tw-incremental-developer-platform, team-topologies-tvp, google-sre-postmortem, conway-committees, bainbridge-ironies, lee-genai-critical-thinking]
related: [workflows, harness-engineering, engineering-kit, rule-registry, evidence-schema, validators, skills-and-evals, adapters]
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
DORA's 2025 research describes AI's main role as an amplifier that magnifies the strengths of
high-performing organisations and the dysfunctions of struggling ones, and associates higher AI
adoption with increases in both software delivery throughput and
instability[^dora-2025-report]. Its 2024 research associated higher adoption with lower delivery
throughput and stability, and suggested larger batch sizes as a reason[^dora-2024-report]. DORA
also groups customer feedback with value-stream visibility, small batches and team
experimentation as capabilities that help predict delivery and organisational
performance[^dora-customer-feedback]. None of this is a finding about software factories: no
public study shows that connecting agent workflows through shared rules, evidence and feedback
improves outcomes. What follows is recommended practice, built on that adjacent evidence.

## How it works

### It emerges from workflows that already run

No team starts by building a factory. It starts with one workflow that runs on real changes, such
as pull-request verification, and adds another once the first is trusted. Shared parts appear when
a second workflow needs something the first already has: it reads the access rule from the
registry instead of keeping its own copy, and it reads check results in the format the first
workflow already writes. Nothing moves into the shared layer until a workflow in use has needed it.
Guidance on internal platforms points the same way. The Thoughtworks Technology Radar observes that
teams often aim for too much of a platform vision too fast, and recommends growing a platform in
increments[^tw-incremental-developer-platform] from what Team Topologies calls the thinnest viable
platform, the smallest set of APIs, documentation and tools that speeds up the teams using
it[^team-topologies-tvp]. DORA lists quality internal platforms among the capabilities that amplify
the benefits of AI[^dora-ai-capabilities], so the risk lies in building shared parts ahead of the
workflows that show what they must hold, not in having them. Growing the shared layer only from
workflows that already run is this site's recommended practice.

### Three things are shared

- **Rules.** One [rule registry](rule-registry.html) holds the rules that apply across changes,
  each with an identifier, a route (a gate that blocks, a named person's judgment, or guidance)
  and an owner, and every workflow reads that registry rather than a copy of it. Material about a
  single change, such as its specification, plan and evidence, stays in version control with that
  change's code and is reviewed alongside it. Keeping it out of the registry keeps the registry
  small enough for its owners to keep current.
- **Evidence.** Every workflow writes its results in the one shape the
  [evidence schema](evidence-schema.html) fixes, and the next workflow reads that record instead of
  asking the same questions again. A check that produced no verdict is recorded as `could_not_run`
  with its cause, and each human decision carries a reason code from a fixed list rather than free
  text. Because the codes are shared, a later workflow can act on a decision without interpreting
  prose, and a team can count how often each reason recurs across all its workflows. Keeping one
  list of reason codes for every workflow is recommended practice.
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

An incident review asks where the gap first became possible, not only where it showed. If nobody
asked the question that would have exposed it, the action lands in specification readiness; if a
rule existed but nothing checked it, the action becomes a check tied to that rule's identifier. The
site reliability engineering workbook notes that postmortem action items with little or no
ownership are less likely to be resolved[^google-sre-postmortem], so each action names one owner
and the stage it changes. Because every workflow reads the same registry and writes the same
record, one change upstream reaches every later change of that kind.

A new check or a tighter threshold does not start as a gate. It runs report-only first, recording
what it would have blocked, and becomes required once its failures prove to be real problems
rather than noise, since a gate that raises false alarms teaches people to override it. Repeated
exceptions travel the same path: when one rule collects the same exception change after change,
the pattern goes back to the rule's owner as a question about the rule or its route, instead of
being granted once more. Both are this site's recommended practice.

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
traceability spine from requirement to incident, linked by rule identifiers. The enablement band
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
- **Unowned or over-concentrated connections.** The rules, evidence format and feedback path
  between workflows belong to no single workflow. Conway observed that organisations design
  systems that copy their communication structures[^conway-committees], so without an owner the
  connections tend to split along team lines. As recommended practice, the shared rules have one
  accountable owner, recorded by name, and ownership is confirmed again whenever people or teams
  change, not only when something goes wrong. The signs are rule changes queued behind one person,
  the same exception granted repeatedly for one rule, or nobody able to say who approves a change
  to the shared rules.
- **Reading the factory as unattended throughput.** Treating human decision points as the
  bottleneck to remove turns the factory into the lights-out sense this site does not mean, and
  larger batches of generated work were DORA's suggested reason for lower stability as AI adoption
  rose[^dora-2024-report]. The sign is a proposal to waive a check or drop an approval to keep up
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
- [Rule registry](rule-registry.html): the shared rules, each with an identifier, a route and an
  owner.
- [Evidence schema](evidence-schema.html): the fixed shape of the record every workflow writes and
  the next one reads.
- [Validators](validators.html), [Skills with evals](skills-and-evals.html) and
  [Adapters](adapters.html): the kit's other parts.
- [Workflow catalog](workflow-catalog.html): the list of workflows the factory draws on.
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
- DORA's 2024 and 2025 research on AI adoption, its AI capabilities model and its customer
  feedback capability[^dora-2024-report][^dora-2025-report][^dora-ai-capabilities][^dora-customer-feedback].
- Thoughtworks on incremental developer platforms, and Team Topologies on the thinnest viable
  platform[^tw-incremental-developer-platform][^team-topologies-tvp].
- The site reliability engineering workbook on postmortem ownership[^google-sre-postmortem];
  Conway on organisations and system design[^conway-committees].
- Bainbridge, and Lee and colleagues, on automation and critical
  thinking[^bainbridge-ironies][^lee-genai-critical-thinking].
