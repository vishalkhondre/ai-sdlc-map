---
id: harness-engineering
type: concept
band: core
map_box: Harness engineering
title: Harness engineering
summary: The discipline of designing and maintaining what a coding agent reads, what it may do, what a machine checks and what a person decides, and of improving those controls each time a failure recurs.
key_terms: [harness, harness-engineering, guides-and-sensors, two-kinds-of-machinery, steering-loop, feedback-path, harnessability, requisite-variety, harness-template, gate, validator, skill, review-skill, harness-evaluation, rule-registry, engineering-kit, workflow, software-factory, export-example]
sources: [bockeler-harness, bockeler-harness-memo, bockeler-sensors, bockeler-context, openai-harness, anthropic-context-engineering, tw-radar-feedback-sensors, swe-agent, ashby, fitness-function, fowler-ci, nist-800-53]
related: [engineering-kit, validators, skills-and-evals, rule-registry, workflows, software-factory]
review_record: content/reviews/1.4.0-core.md
---

## Definition

Harness engineering is the discipline of deliberately designing and maintaining the environment
around a coding agent: what the agent reads before it acts, what it is allowed to do, what a
machine checks after it acts, and what a person still decides. The term was already in use before
the vocabulary on this page took shape. One model vendor's published account of building software
with agents popularised it,[^openai-harness] and Birgitta Böckeler's first memo on the subject
responds to that account.[^bockeler-harness-memo] The vocabulary itself comes from Böckeler. She
notes that *harness* has emerged as shorthand for everything in an agent except the model itself
(Agent = Model + Harness), frames harness engineering within the bounded context of using a coding
agent, and presents it as a way to build trust in coding agents. Her terms for that work are
feedforward guides and feedback sensors, computational and inferential controls, the steering loop,
harnessability and harness templates.[^bockeler-harness] In the AI SDLC (the software development
lifecycle with AI agents doing part of the work), harness engineering is the discipline; the
Engineering Kit is the artefact it produces, a workflow is the unit of work it serves, and the
software factory is the operating state it makes possible.

## Why it matters

A coding agent's output depends on more than its model. The same model behaves differently
depending on what it is told, which tools it can use and what happens to its work when it is
wrong. A peer-reviewed study of a software-engineering agent showed how much the interface around
the model matters: among other changes, an edit command that refused edits failing a lint check
improved the agent's resolve rate on one benchmark.[^swe-agent] That is one benchmark and one agent
design, not a general law. The wider claim, that deterministic checks improve agent output, is
presented here as recommended practice, not as a research finding.

The practice is aimed at three problems that this site treats as typical of agent work without a
deliberate harness; the framing is recommended practice rather than a measured result. The first
is hard rules that live only as prose in instruction files, so the agent applies them unevenly and
nobody can tell when it did not. The second is review attention spent re-checking mechanical
details by hand as the volume of agent output grows; the Thoughtworks Technology Radar lists
feedback sensors for coding agents as a technique and gives as its reasons a lighter manual review
burden and agents that can correct their own work.[^tw-radar-feedback-sensors] The third is lessons
from failures that stay in chat threads and retrospectives, so the next run repeats them.

A harness does not remove people. Böckeler notes that it can make explicit only part of what an
experienced developer brings, and that a good harness directs human input to where it matters
most rather than trying to eliminate it.[^bockeler-harness-memo]

## How it works

### What the harness holds

Inside the harness sit the project-wide instruction file and any scoped rule files, the
specification and plan for the change, skills the agent loads on demand, templates and scaffolds,
the tools and permissions the agent runs with, the tests, linters, type checkers and structural
checks that run on its output, review agents, the gates that can stop a merge, and the record of
what ran. Outside it sits the model. A team chooses a model but does not engineer it; everything it
does engineer around the model is harness.

Harness engineering is wider than prompt engineering and context engineering, and contains the
second. Prompt engineering is the craft of writing and organising instructions to a model; context
engineering is curating and maintaining the whole set of information the model sees during
inference, across turns.[^anthropic-context-engineering] Böckeler puts context engineering for
coding agents as curating what the model sees so that the result is better.[^bockeler-context]
Harness engineering adds what the model is subject to but does not see: architectural constraints
enforced by tools, periodic clean-up of the codebase, and the checks on its output. Böckeler's
first note on the term lists context engineering as one part of the harness, next to architectural
constraints and garbage collection of the codebase.[^bockeler-harness-memo] The vendor account that
popularised the term describes the same work across one large repository: documentation kept in the
repository as the agent's main source of knowledge, a short instruction file that points into it,
and a layered architecture enforced mechanically by custom linters and structural tests, with
recurring clean-up runs that look for drift.[^openai-harness]

Because the harness shapes every change, this site recommends giving it the same care as
application code. Its files live in version control, changes to them are reviewed like any other
change, and each change's evidence carries the harness version it ran under, so that a later reader
can reconstruct which controls applied.

### Guides and sensors

Böckeler divides the controls in a harness into two kinds.[^bockeler-harness] Guides are
feedforward: they steer the agent before it acts. Agent instruction files, skills and automated
code modifications are guides. Sensors are feedback: they observe what the agent produced and let
it correct itself. Her examples of sensors include linters, structural tests, type checkers and AI
code review.[^bockeler-harness] The Technology Radar's entry on feedback sensors gives a similar
set: compilers, linters, type checkers, test suites and a reviewer agent.[^tw-radar-feedback-sensors]

A harness needs both. Guides raise the chance that the first attempt is right, but they cannot
anticipate everything. Sensors catch what the guides missed, but a harness made only of sensors
lets the agent make every avoidable mistake first and pays for each correction. Control engineers
combine feedforward and feedback for the same reason: no forward model of a process is complete.
The pairing argument is this site's reasoning, not a claim taken from Böckeler.

In the customer-record export, the access rule R-042 / SEC-004, which says which identities may
export which customer records, is written into the specification and loaded as a skill before the
agent writes any code. Both are guides. After the agent writes the export, a validator checks the
export query against the access rule and a review skill reads the diff against the same rule. Both
are sensors.

### Computational and inferential controls

Böckeler's second distinction is about how a control runs.[^bockeler-harness] Computational
controls are deterministic and fast and run on ordinary compute: tests, linters, type checkers,
structural analysis. They take milliseconds to seconds and their results are reliable. Inferential
controls use a model: semantic analysis, AI code review, a model acting as judge. They are slower,
cost more and are non-deterministic, but they can give richer guidance and add semantic judgement
that no rule engine can.

The two distinctions are independent of each other. A project scaffold or an automated code
modification is a computational guide; an instruction file or a skill is an inferential guide. A
validator is a computational sensor; a review skill is an inferential sensor. Böckeler's worked
examples of maintainability sensors on a real codebase show both kinds of sensor side by
side.[^bockeler-sensors] She also groups what the controls regulate into maintainability,
architecture fitness and behaviour, and calls behaviour, meaning functional correctness, the
hardest to check.[^bockeler-harness] Architecture fitness is what evolutionary-architecture
practice calls fitness functions: architecture goals written as executable tests.[^fitness-function]

Placement follows cost. Computational sensors are cheap and fast enough to run on every change,
alongside the agent. Böckeler suggests running the fast checks while the agent works and before
commit, repeating them after integration, and adding more expensive sensors, such as mutation
testing, later in the pipeline.[^bockeler-harness] Continuous integration supplies the base layer
underneath: a self-testing build that runs on every change, the same way everywhere, and fails
fast.[^fowler-ci]

Böckeler's distinction matters for where a gate belongs: a computational result is the same on
every run, while an inferential one is not,[^bockeler-harness] so a model's verdict used as a gate
could stop a change today and let the identical change through tomorrow. A review skill, an agent that reads the diff
against the rules, still earns its place on questions no rule engine can settle. In Böckeler's
worked examples, though, inferential sensors address semantic concerns such as duplication only
partially,[^bockeler-sensors] so its findings go to the person reviewing the change rather than
deciding the merge.

The same reasoning covers what the agent may touch. The agent runs under an identity whose
permissions cover only what its task needs, so staying in scope does not depend on its obeying an
instruction. This is least privilege, which the NIST control catalogue applies to processes acting
on behalf of users as well as to users themselves.[^nist-800-53] The agent runtime that supplies
those permissions belongs to the enablement band.

In the export example, the validator for R-042 is the gate that can stop the merge. The review
skill's finding is advice to the human reviewer.

### The steering loop and the feedback path

Böckeler calls the ongoing work of improving the harness the steering loop: whenever an issue
happens more than once, the guides and sensors are improved so that it becomes less likely to
happen again, or cannot happen at all.[^bockeler-harness] This site calls the same loop the
feedback path and gives each kind of lesson a defined destination. The list is the site's own
extension of the steering loop, not Böckeler's:

- a defect becomes a regression test;
- a review comment that keeps recurring becomes a rule in the rule registry;
- a rule that keeps being broken becomes a deterministic gate;
- a production failure becomes an evaluation case for the agent and its skills;
- a misunderstood requirement becomes a question that later specifications of the same kind must
  answer;
- a procedure people keep repeating becomes a skill;
- a brittle agent behaviour becomes a change to the harness itself.

In each case the change lands upstream of where the problem appeared. A lesson goes where the miss
started, not where it was noticed: if the requirement itself was wrong, stricter code review would
not have caught it. For a defect that reached production, the team traces it back to the earliest
control that could have stopped it and changes that control, or adds one where none existed.

The loop is run by people, and this site recommends naming who runs it. Each rule has an owner who
can change it, and at the team's usual retrospective cadence someone looks back over recent
failures and asks which control should change. People who review agent work are its main input,
because they see what the agent missed. Two further practices keep the loop honest. Controls are
added in response to evidence, following the steering loop's trigger of an issue that happens more
than once:[^bockeler-harness] a new skill, rule or gate answers a failure that has been seen, while
one added only in anticipation brings context and upkeep without fixing anything known. And the
agent must not be able to satisfy a sensor by changing it: if one change both needs a check to pass
and makes that check easier to pass, that is itself a finding.

The customer-record export shows the loop twice. Before the export was built, human reviewers kept
raising the same finding on changes that read customer data: a background worker that assembles
large result sets used a broader query than the request path, so it could read records the
requesting user may not export. Because the finding recurred, it was written into the access rule
R-042 in the registry, and the validator for R-042 was extended to check background workers'
queries as well as the request path. A recurring comment became a rule, and the rule became a gate.
When the export's first pull request adds a background worker with that broader query, the extended
validator fails on it before a reviewer has to spot it.

The volume-limit rule R-017 has a stated row limit from the start, and the export's first pull
request already carries a load scenario for 50k rows. Later, in a hypothetical production incident,
a scheduled full export, within R-017's limit but far larger than the 50k rows the scenario tested, times out. The follow-up adds a
larger load scenario and an evaluation case, both rerun whenever the export code, its skills or the
model change, and the specification readiness questions gain one about the largest export
expected. R-017's limit was already in place; the incident exposed a volume that nobody had tested
or asked about, and the loop sends each part of that lesson to its own destination.

### Harnessability and requisite variety

Harnessability is Böckeler's word for how far a codebase supports a harness. A codebase written in
a strongly typed, modular way gives the harness more handles to grip, and she argues that
harnessability should be a first-class criterion in technology and architecture
decisions.[^bockeler-harness] Boundaries between layers and modules that a tool can check, tests
strong enough to act as sensors and a local environment the agent can run all make sensors cheap to
add. Where they are missing, for example in old code with little test coverage, or where a change
reaches interfaces that other teams depend on, this site recommends that a person investigates the
affected area before the agent starts.

Harness templates, in Böckeler's proposal, are bundles of guides and sensors set up in advance for
a common service topology, its conventions and its technology stack, so that a larger organisation
can share them.[^bockeler-harness] The Engineering Kit's technology profiles are one concrete form
of that idea.

Böckeler also draws on W. Ross Ashby's law of requisite variety, from *An Introduction to
Cybernetics* (1956): a regulator can control a system only if it has at least as much variety as
the system it governs, summed up as "only variety can destroy variety".[^ashby] Her conclusion is
that committing to specific service topologies narrows the space the agent works in, which makes a
comprehensive harness achievable.[^bockeler-harness] The law does not say that fewer controls are
better; it says the controls must match what they govern. This site's recommendation follows from
shrinking what is governed: narrow what the agent may produce first, on a few well-defined
surfaces, then start with a small set of controls fitted to failures actually seen, and widen both
only as the loop shows gaps. Controls added for every imagined failure bring context load, noise
and upkeep without matching any variety the agent actually produces.

## Where it sits on the map

Harness engineering is a box in the core band, the band that describes what does the work. The
band's row reads Harness engineering, then the Engineering Kit, then Workflows, then the Software
factory: the discipline comes first, before the artefact it produces. The
[Engineering Kit](engineering-kit.html), after it, is a versioned package holding the
[Rule registry](rule-registry.html), [Validators](validators.html),
[Skills with evals](skills-and-evals.html), the [Evidence schema](evidence-schema.html) and
[Adapters](adapters.html). [Workflows](workflows.html) come after the kit and are the unit it
serves: each one runs a delivery decision end to end, consuming guides at each step and followed by
sensors. The [Software factory](software-factory.html) comes last: the operating state that appears
when workflows share rules, evidence and feedback. The feedback path is the steering loop under
this site's name. On the map's adoption path, the "Feedback path proven" stage, where that loop is
proven, links to this section.

On the lifecycle side, specifications and plans are where most guides are written and where a
gate's rule is first stated, even though the gate itself runs after implementation. On the
enablement side, the agent runtime supplies the tools, sandboxes and permissions that the harness
configures. The assurance band reads what the sensors record to decide whether a change is ready;
this page defines the controls, not what their results mean for that decision. The
[workflow catalog](workflow-catalog.html) lists the workflows the harness serves.

## Pitfalls

- **Rules that exist only as prose.** Hard rules sit in instruction files with nothing checking
  them. Sign: reviewers write the same comment on change after change.
- **A model's opinion used as a gate.** A review agent's verdict blocks or approves a merge on its
  own, though another run on the same diff may disagree. Sign: a blocked change passes on a re-run
  with no code change, or a rule is enforced only by a review prompt.
- **Sensors the agent can edit.** The agent reaches a passing result by changing the check instead
  of the code. Sign: the change that makes a check pass also edits or removes that check.
- **A harness grown by anticipation.** Controls are added for failures nobody has seen. Sign:
  skills or rules that cannot be linked to an observed failure, and a project-wide instruction file
  that only ever gets longer.
- **A loop with no owner.** Lessons are recorded but never converted. Sign: retrospective findings
  that never turn into a test, rule, gate or evaluation case.
- **The fix at the wrong layer.** The control is changed where the problem surfaced, not where it
  began. Sign: code review tightened after a defect whose cause was an unstated requirement.
- **An unversioned harness.** Instruction files, skills and checks change without a record. Sign:
  nobody can say which rules and checks applied to a given merged change.
- **A codebase the harness cannot grip.** Boundaries are implicit and tests are weak. Sign: sensors
  are hard to add, and the agent's errors surface only in human review.

## Related

- [Engineering Kit](engineering-kit.html): the versioned package that harness engineering produces.
- [Rule registry](rule-registry.html): every rule with an identifier, a route and an owner.
- [Validators](validators.html): computational sensors as code, and their rollout from report-only
  to required.
- [Skills with evals](skills-and-evals.html): inferential guides and how they are tested.
- [Evidence schema](evidence-schema.html): the fixed shape of what each run records.
- [Adapters](adapters.html): how the kit binds to the tools the harness configures.
- [Workflows](workflows.html): the unit of work the harness serves.
- [Software factory](software-factory.html): the operating state that appears when workflows share
  rules, evidence and feedback.
- [Workflow catalog](workflow-catalog.html): the list of workflows.
- Terminology: [harness engineering](glossary.html#harness-engineering),
  [steering loop](glossary.html#steering-loop), [feedback path](glossary.html#feedback-path),
  [guides and sensors](glossary.html#guides-and-sensors),
  [harnessability](glossary.html#harnessability).

## Sources

- Böckeler, *Harness engineering for coding agent users*: the harness, guides and sensors,
  computational and inferential controls, the steering loop, harnessability, harness templates and
  the use of Ashby's law.[^bockeler-harness]
- Böckeler, *Harness Engineering - first thoughts*: her first memo on the term, responding to a
  model vendor's account; context engineering as one part of the harness, and directing human input
  rather than eliminating it.[^bockeler-harness-memo]
- Böckeler, *Maintainability sensors for coding agents*: worked examples of computational and
  inferential sensors.[^bockeler-sensors]
- Böckeler, *Context Engineering for Coding Agents*: the context an agent reads.[^bockeler-context]
- *Effective context engineering for AI agents*: prompt engineering and context engineering
  distinguished.[^anthropic-context-engineering]
- A model vendor's engineering account of harness engineering in an agent-first codebase: the
  account that popularised the term, repository knowledge and mechanically enforced
  architecture.[^openai-harness]
- *Feedback sensors for coding agents*, Technology Radar Volume 34.[^tw-radar-feedback-sensors]
- Yang et al., *SWE-agent: Agent-Computer Interfaces Enable Automated Software
  Engineering*.[^swe-agent]
- Ashby, *An Introduction to Cybernetics*: the law of requisite variety.[^ashby]
- *Fitness function-driven development*: architecture goals as executable tests.[^fitness-function]
- Fowler, *Continuous Integration*: the self-testing build underneath the harness.[^fowler-ci]
- NIST SP 800-53 Rev. 5, *Security and Privacy Controls for Information Systems and
  Organizations*: the least-privilege control.[^nist-800-53]
