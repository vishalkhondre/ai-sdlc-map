---
id: definition-of-ready-and-done
type: concept
band: lifecycle
map_box: Definition of Ready / Done (the DoR and DoD tags)
title: Definition of Ready and Definition of Done
summary: A Definition of Ready states what an item must meet before a team accepts it for work, and a Definition of Done states what the result must meet to count as finished; with coding agents, both need parts a machine can check and an owner who is not the agent.
key_terms: [ai-sdlc, definition-of-ready, definition-of-done, specification-readiness, independent-basis, risk-tier, workflow, evidence-record, evidence-handoff, could-not-run, failure-path, export-example, gate, feedback-path, steering-loop]
sources: [scrum-guide-2020, agile-alliance-dor, safe-glossary, wake-invest, istqb-agile-tester-2014, istqb-testability, dora-ai-capabilities-impact, dora-small-batches, spec-kit-sdd, requirements-ambiguity-llm, metr-reward-hacking, anthropic-claude-37-system-card, konstantinou-test-oracles, bockeler-harness, oasis-soa-rm, safe-inspect-and-adapt, istqb-acceptance-criteria]
related: [specification, design, release, develop-build-qa, lifecycle-levels, traceability-spine, workflows, rule-registry, evidence-schema]
review_record: content/reviews/1.5.0-lifecycle.md
---

## Definition

A Definition of Ready and a Definition of Done are each a team's explicit, visible statement of a
state that work must reach. They differ in the state they guard. The Definition of Ready guards the
entrance: what an item has to satisfy before a team accepts it for work. The Definition of Done
guards the exit: what the result has to satisfy before it counts as finished. Either one works as a
gate only when someone or something checks it; a definition that is written down and never applied is
a wish. This framing is this site's own; the two entries below follow their published sources.

### Definition of Ready

The Agile Alliance glossary describes a team that makes explicit and visible the criteria
(generally based on the INVEST matrix) that a user story must meet before it is accepted into the
upcoming iteration[^agile-alliance-dor]. This site applies the same idea to any item of work, not
only a user story, and says so where it does.

The Scrum Guide does not use the term. It neither defines nor forbids a Definition of Ready. What it
says is that Product Backlog items that the Scrum Team can complete within one Sprint "are deemed
ready for selection in a Sprint Planning event", and that such items "usually acquire this degree of
transparency after refining activities"[^scrum-guide-2020]. Refinement, in the Guide's words, is "an ongoing activity to add details,
such as a description, order, and size"[^scrum-guide-2020]. A Definition of Ready is therefore a team
practice, written down so that "ready" means the same thing to everyone who relies on it. No source
cited on this page prescribes what the criteria contain, and this page does not either: the contents
depend on the work and on the team.

### Definition of Done

The Scrum Guide, by Ken Schwaber and Jeff Sutherland, gives the term its formal meaning: the
Definition of Done is "a formal description of the state of the Increment when it meets the quality
measures required for the product"[^scrum-guide-2020]. Three consequences follow from the Guide's text.

- The moment a Product Backlog item meets the Definition of Done, an Increment is born[^scrum-guide-2020].
- A Product Backlog item that does not meet it "cannot be released or even presented at the Sprint
  Review"[^scrum-guide-2020].
- It is the commitment attached to the Increment, as the Product Goal is the commitment of the
  Product Backlog and the Sprint Goal that of the Sprint Backlog[^scrum-guide-2020].

The Guide adds that the Definition of Done creates transparency by giving everyone a shared
understanding of what work was completed as part of the Increment[^scrum-guide-2020]. SAFe's
glossary words it more generally: the Definition of Done "specifies the requirements for
completeness of a work product or increment of value"[^safe-glossary].

## Why it matters

Without a stated Definition of Ready, work starts on items whose questions are still open, and the
questions surface later as discussion and rework. The Agile Alliance entry lists, among the expected
benefits of a stated definition, less "costly back-and-forth discussion or rework" and an explicit
agreement that lets a team push back on ill-defined items[^agile-alliance-dor]. Without a stated
Definition of Done, "finished" is decided case by case, often after the work is in review, and the
argument is about people rather than about criteria. When several teams work on one product the
problem multiplies, because the Scrum Guide requires those teams to define and comply with the same
Definition of Done[^scrum-guide-2020]. As recommended practice, a definition earns its place by
settling those arguments before they start.

In an AI SDLC (the software development lifecycle with AI agents doing part of the work), two
things raise the stakes.

The first is volume. DORA's guidance on its AI Capabilities Model says AI "can easily generate
massive blocks of code, which are hard to review and test"[^dora-ai-capabilities-impact], and its
page on small batches says that large changes "are difficult to review, test, and integrate
safely"[^dora-small-batches]. When items arrive faster than people can judge them, a clear entrance
criterion keeps unfinished thinking out of the queue, and a clear exit criterion tells a reviewer
what to look for in a large diff.

The second is that the exit criterion can be shaped by the party being judged. METR reports, on its
own evaluation tasks, models "attempting (often successfully) to get a higher score by modifying the
tests or scoring code"[^metr-reward-hacking]. One model vendor's system card describes a model that
"occasionally resorts to special-casing in order to pass test cases in agentic coding environments",
most often by returning the expected test values, and "also includes modifying the problematic tests
themselves"[^anthropic-claude-37-system-card]. Both are limited evidence: METR's examples come from its
own tasks and not from production teams, and the system card says the behaviour emerged during
training and that partial mitigations were applied before launch, so it is not a statement about any
model in use today. They show that a check which the agent can edit is not independent of the agent.

No public statistic says how many teams keep either definition, and no study examines how coding
agents change them. Where this page describes how agents change the two definitions, it is recommended
practice and is labelled as such.

## How it works

### Who owns each

The two definitions have different owners, and the Scrum Guide is explicit about only one of them.
For the Definition of Done, the Developers are always accountable for "Instilling quality by adhering
to a Definition of Done", and are "required to conform to the Definition of Done"[^scrum-guide-2020].
An organisational standard, where one exists, is followed by every Scrum Team as a minimum. Where none
exists, the Scrum Team creates a definition appropriate for the product, and teams working on one
product "must mutually define and comply with the same Definition of Done"[^scrum-guide-2020].

For readiness the Guide names no owner of a definition, because it names no definition. It does say who
is accountable for what makes an item ready for selection. The Product Owner is accountable for
effective Product Backlog management, which includes creating and clearly communicating the items, and
the Developers who will do the work are responsible for the sizing[^scrum-guide-2020].

On this site, as recommended practice, each definition has one named owner who answers for its
wording and can change it, and that owner is a person, never the agent whose work the definition
judges. The definitions are applied inside workflows, each with an accountable owner of its own
(see [Workflows](workflows.html)): readiness in specification readiness
([W04](workflow-catalog.html#W04)) and in task traceability and test planning
([W12](workflow-catalog.html#W12)), and release-level done in release readiness
([W25](workflow-catalog.html#W25)). Who decides in each of those workflows is set in its catalog
row; owning a definition means keeping it current, while the workflow's deciders apply it.

Public practice already sets different criteria for different levels of work. Bill Wake's 2003 article
proposes INVEST for stories (Independent, Negotiable, Valuable, Estimable, Small, Testable) and SMART
for tasks (Specific, Measurable, Achievable, Relevant, Time-boxed)[^wake-invest], and the Agile Alliance
entry says a team's criteria are generally based on the INVEST matrix[^agile-alliance-dor]. The Scrum
Guide's wording for readiness concerns the item as a whole: one that the team can complete within one
Sprint is deemed ready for selection[^scrum-guide-2020]. This page does not adopt any of these lists as
the contents of a definition.

**Criteria a machine can check.** A criterion is machine-checkable when a tool can decide it from the
record alone. The catalog rows state which parts of each readiness decision have that form; see
specification readiness ([W04](workflow-catalog.html#W04)) and task traceability and test planning
([W12](workflow-catalog.html#W12)). What a tool cannot decide stays
with a person: whether the intent is right. The identifiers in those checks are the chain
described on the [Traceability spine](traceability-spine.html) page, which connects criteria, tasks,
tests and results.

Public sources show how criteria are written so that gaps can be found. The templates of an
open-source spec-driven toolkit mandate [NEEDS CLARIFICATION] markers in place of guesses, and include
checklists that act as "unit tests" for the specification[^spec-kit-sdd]. As recommended practice, a
marker left in a specification fails the readiness check in specification readiness
([W04](workflow-catalog.html#W04)), so a tool can find it and the item is not ready. A 2025 industrial study of language models on real-world
requirements reports that giving ten worked examples in the prompt classified ambiguous requirements better than
giving none[^requirements-ambiguity-llm]. An agent can therefore flag ambiguity for a person to
resolve, and it does not replace the person who settles what is meant.

Testability and size are also readiness properties. ISTQB defines testability as "The degree to which
test conditions can be established for a component or system, and tests can be performed to determine
whether those test conditions have been met"[^istqb-testability]. As recommended practice, an
acceptance criterion counts as testable when a check can be written for it before implementation
starts. On size, DORA advises breaking work into units "that can be completed independently and in short
timeframes"[^dora-small-batches], which is the same shape as the Scrum Guide's test of an item that can
be completed within one Sprint.

### Done at three levels

The Definition of Done applies at three levels of work. The first two follow the published sources;
the third is this site's recommended practice.

1. **Story.** At the level of a single Product Backlog item, the moment the item meets the Definition
   of Done an Increment is born[^scrum-guide-2020].
2. **Increment.** The Definition of Done is the commitment of the Increment as a whole[^scrum-guide-2020].
   A 2014 testing syllabus adds that each test level has its own definition of done[^istqb-agile-tester-2014],
   so unit, integration and acceptance testing can each carry criteria of their own.
3. **Release.** As recommended practice, a release candidate has a done decision of its own; see
   release readiness ([W25](workflow-catalog.html#W25)) and [evidence hand-off](glossary.html#evidence-handoff). The
   [Release](release.html) page describes the phase.

The separation of done from released rests on the Scrum Guide. An item that does not meet the
Definition of Done cannot be released[^scrum-guide-2020], and the reverse does not hold: meeting the
definition makes an item eligible for release, not released. The Guide also says an Increment may be
delivered before the end of the Sprint, and that the Sprint Review "should never be considered a gate
to releasing value"[^scrum-guide-2020]. The release decision therefore has its own evidence and its
own owner.

### How agents change both

For readiness, see the agent task in specification readiness
([W04](workflow-catalog.html#W04)); the study cited above
investigates this task[^requirements-ambiguity-llm]. A person still resolves the intent, because the
agent can raise a question and cannot know what the business wants.

For done, the volume of code changes what can be reviewed. DORA reports that working in small batches
amplifies the positive impact of AI adoption on product performance[^dora-small-batches], and that
large changes are hard to review, test and integrate safely[^dora-small-batches]. As recommended
practice, the Definition of Done for an agent's work includes a limit on size; see
[Workflows](workflows.html).

A check can also be met by changing it. The reward-hacking reports under "Why it matters" describe
models modifying tests or scoring code and special-casing to pass tests[^metr-reward-hacking][^anthropic-claude-37-system-card].
Tests an agent generates are a weaker basis than they look: a preprint on LLM-generated test oracles
reports that LLM-based test generation approaches mainly capture the actual program behaviour, which
makes bug detection difficult[^konstantinou-test-oracles]. A test that records what the code does has
little to say about what it should do.

Two consequences follow, and both are recommended practice. First, the done criteria rest on a basis
defined apart from the implementation, the site's [independent basis](glossary.html#independent-basis):
acceptance criteria[^istqb-acceptance-criteria], access rules, interface contracts, representative data and failure scenarios that
exist before and outside the code they judge. Second, no agent edits the criteria it is judged by; see
the guardrails in [Workflows](workflows.html). No study examines these two definitions with coding
agents, so this is guidance, not a finding.

The lessons also flow back. The Scrum Guide has the Retrospective inspect "individuals, interactions,
processes, tools, and their Definition of Done"[^scrum-guide-2020]. On this site the corresponding
checkpoint takes its name from SAFe's Inspect and Adapt event[^safe-inspect-and-adapt]; see
[Inspect and Adapt](inspect-and-adapt.html). The route by which an incident changes a readiness
criterion is the feedback path, which this site adapts from Birgitta Böckeler's steering
loop[^bockeler-harness]. Sending a lesson to a readiness criterion is this site's own extension of
that loop, not part of Böckeler's account; see [Harness engineering](harness-engineering.html).

### The export example

The running example is a hypothetical feature that lets users export customer records. Its open
decisions are which records, which fields, large exports, failure and audit. It shows both definitions
at work.

**Readiness.** For the export, the Definition of Ready checks that the specification settles the
questions its rules depend on before planning starts. The plainest is which roles may export which
records, the question the access rule R-042 turns on: while the specification leaves it open, the
item is not ready, however complete the rest of it looks. [Software factory](software-factory.html)
follows the item from that point.

**A rule open to exception and one that is not.** The two rules behave differently when a change
asks to depart from them. R-017's row limit for large exports is open to exception, and R-042, as an
access rule, is not; see the failure paths in [Workflows](workflows.html#failure-paths). A readiness
criterion tied to R-042 is therefore met only as written. One tied to R-017 is met either by staying
within the limit or by a recorded exception, so the record has to show which of the two applies.

**Readiness changing.** In a hypothetical production incident, a scheduled full export within
R-017's limit, but far larger than the load scenario, times out. Afterwards the readiness check asks
every export-like specification for the largest export it expects. The Definition of Ready has
changed through the feedback path; [Software factory](software-factory.html) gives the incident in
full.

**Done.** For the export change, done means the verification record for the exact revision shows an
explicit pass for every check the change requires, among them the access check for R-042 and the
R-017 load scenario. On the first pull request the access check failed and the load scenario returned
`could_not_run`; neither result is a pass, so the change is not done until both checks run again
and pass. [Evidence schema](evidence-schema.html) describes the record.

## Where it sits on the map

The map's lifecycle band shows two tags. The DoR tag sits on the [Specification](specification.html)
phase and the DoD tag sits on the [Release](release.html) phase. The Team level of the map is labelled
with "stories · iterations · DoR / DoD", which is where the two definitions are applied day to
day; the [Lifecycle levels](lifecycle-levels.html#team) page describes it. The adoption path lists
"Specification readiness as the Definition of Ready" as a step.

The workflow catalog holds the decision behind each tag. Specification readiness
([W04](workflow-catalog.html#W04)) sits under the DoR tag. Between the two tags,
[Develop, Build and QA](develop-build-qa.html) holds the verification that
produces the evidence a done decision reads, among them acceptance-test generation and execution
([W17](workflow-catalog.html#W17)) and pull-request verification
([W23](workflow-catalog.html#W23)). Release readiness ([W25](workflow-catalog.html#W25)) sits under the
DoD tag. The core band explains the machinery they share: [Workflows](workflows.html) for the
decision unit, the [Rule registry](rule-registry.html) for the rules a check cites, the
[Evidence schema](evidence-schema.html) for the record each run leaves, the
[Software factory](software-factory.html) for what emerges when many workflows share records, and
the page on [checks that enforce rules](validators.html) for how a result such as `could_not_run`
is reported.

SAFe, cited as one framework that uses these altitudes of work (the map's portfolio, train and team
levels), appears here only through its glossary wording for the Definition of Done, quoted above.
The [SAFe reference model](safe-reference-model.html) page gives this site's wider mapping of the
lifecycle onto SAFe.

## Pitfalls

- **Readiness stated but not checked.** The definition exists as a document and nothing applies it.
  Sign: items start with open mandatory questions; see specification readiness
  ([W04](workflow-catalog.html#W04)).
- **Done reduced to "the tests pass".** Tests and code come from the same incomplete reading of the
  specification, so both share its mistake. Sign: the tests mirror what the implementation does, and a
  defect that traces back to the specification passes every test. Generated tests tend to capture the
  program's actual behaviour[^konstantinou-test-oracles], so the done criteria need an
  [independent basis](glossary.html#independent-basis).
- **An agent meets the definition by editing the checks it is judged by.** Sign: a diff touches the
  checks or tests beside the code. Reported cases include models modifying tests or scoring code and
  special-casing expected test values[^metr-reward-hacking][^anthropic-claude-37-system-card]. As
  recommended practice, changes to checks go to a person for review; see [Workflows](workflows.html).
- **Done mistaken for released.** Sign: finished increments accumulate and no release record
  exists[^scrum-guide-2020]. The release decision is separate and has its own evidence.
- **Each team on one product keeps its own definition of done.** Sign: the same item is done in one
  team and not in another. The Scrum Guide requires teams on one product to define and comply with
  the same Definition of Done[^scrum-guide-2020].

## Related

- [Specification](specification.html): the phase where the Definition of Ready tag sits.
- [Design](design.html): the phase where tasks and their traceability are set up.
- [Release](release.html): the phase where the Definition of Done tag sits.
- [Develop, Build and QA](develop-build-qa.html): where the evidence for done is produced.
- [Lifecycle levels](lifecycle-levels.html#team): the Team level, where both definitions apply.
- [Traceability spine](traceability-spine.html): the identifier chain that connects criteria, tasks,
  tests and results.
- [Inspect and Adapt](inspect-and-adapt.html): the checkpoint where a definition is reviewed and changed.
- [SAFe reference model](safe-reference-model.html): the mapping of the lifecycle onto SAFe.
- [Workflows](workflows.html): the decision unit that each readiness and done check belongs to.
- [Rule registry](rule-registry.html), [Evidence schema](evidence-schema.html),
  [Software factory](software-factory.html) and [checks that enforce rules](validators.html): the
  shared machinery behind the checks.
- Workflow catalog rows: specification readiness ([W04](workflow-catalog.html#W04)), task
  traceability and test planning ([W12](workflow-catalog.html#W12)), acceptance-test generation and
  execution ([W17](workflow-catalog.html#W17)), pull-request verification
  ([W23](workflow-catalog.html#W23)) and release readiness ([W25](workflow-catalog.html#W25)).
- Terminology: [Definition of Ready](glossary.html#definition-of-ready),
  [Definition of Done](glossary.html#definition-of-done),
  [Specification readiness](glossary.html#specification-readiness),
  [Independent basis](glossary.html#independent-basis) and [Risk tier](glossary.html#risk-tier).

## Sources

- The state of the Increment, the commitment, ownership and the separation of done from released: the
  Scrum Guide[^scrum-guide-2020], and SAFe's glossary entry for the Definition of Done[^safe-glossary].
- Readiness criteria and their precedent by level of work: the Agile Alliance glossary entry[^agile-alliance-dor]
  and Bill Wake's article on INVEST and SMART[^wake-invest].
- Done at each test level and testability: the ISTQB Agile Tester syllabus, 2014
  edition[^istqb-agile-tester-2014], for which ISTQB has announced the end of exams and training in
  2027, and the ISTQB glossary[^istqb-testability].
- Clarification markers, ambiguity detection and checks on specifications: an open-source spec-driven
  toolkit[^spec-kit-sdd] and an industrial study of language models on
  requirements[^requirements-ambiguity-llm].
- Volume and batch size with AI: DORA's AI Capabilities Model guidance[^dora-ai-capabilities-impact]
  and its page on small batches[^dora-small-batches].
- Checks an agent can shape: METR's report on reward hacking[^metr-reward-hacking], one model
  vendor's system card[^anthropic-claude-37-system-card] and a preprint on LLM-generated
  test oracles[^konstantinou-test-oracles].
- Steering loop: Birgitta Böckeler on harness engineering[^bockeler-harness]. The feedback path is
  this site's adaptation of it, and its readiness destination is this site's own extension, not
  Böckeler's.
- The name of the checkpoint: SAFe's Inspect and Adapt page[^safe-inspect-and-adapt].
- The sense of "reference model" in the name of the SAFe reference model page: the OASIS Reference
  Model for Service Oriented Architecture[^oasis-soa-rm].
