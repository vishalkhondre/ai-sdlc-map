---
id: specification
type: phase
band: lifecycle
map_box: Specification
title: Specification
summary: Specification turns intent into a specification a team can plan from, with testable acceptance criteria and its open questions recorded; with coding agents, an agent proposes questions, checks settle what a tool can decide, and named owners decide when the specification is ready.
key_terms: [ai-sdlc, specification-readiness, spec-driven-development, independent-basis, workflow, evidence-record, evidence-handoff, failure-path, harness-evaluation, export-example]
sources: [scrum-guide-2020, wake-invest, istqb-acceptance-criteria, istqb-testability, fowler-given-when-then, nist-ssdf, safe-team-backlog-refinement, agile-alliance-dor, requirements-ambiguity-llm, spec-kit, bockeler-sdd, spec-kit-sdd, dora-small-batches]
related: [idea, design, definition-of-ready-and-done, traceability-spine, workflows, evidence-schema, skills-and-evals, rule-registry]
review_record: content/reviews/1.5.0-lifecycle.md
---

## Purpose

Specification is the phase in which a statement of what someone wants becomes a specification that
a team can plan from. Its output is a set of acceptance criteria that a test can settle, a written
account of which questions were answered and which remain open, and a
[readiness record](glossary.html#specification-readiness) that later phases read. The phase answers
one question: is this specification clear enough to plan from, with the uncertainty that remains made
visible? The decision is taken in the catalog's
[Specification readiness](workflow-catalog.html#W04) workflow.

In an AI SDLC (the software development lifecycle with AI agents doing part of the work), the phase
carries more weight than before. Where a specification is silent, an agent working from it still has
to produce something. This site's recommended practice is to settle ambiguity here, while it is still
a question in a document, rather than leave the agent to choose an answer that nobody sees until the
code is under review.

The map marks this phase with the Definition of Ready tag. The Agile Alliance glossary describes a
Definition of Ready as the criteria, made explicit and visible by the team and generally based on the
INVEST matrix, that a user story must meet before it is accepted into the upcoming
iteration[^agile-alliance-dor]. What such a definition holds and who keeps it are covered under
[Definition of Ready](definition-of-ready-and-done.html#definition-of-ready).

## Traditional practice

Without agents, requirements reach a team as backlog items that are refined until the team can take
them on. The 2020 Scrum Guide calls refinement "an ongoing activity to add details, such as a
description, order, and size", and says that items the Scrum Team can complete within one Sprint "are
deemed ready for selection in a Sprint Planning event"[^scrum-guide-2020]. The Guide makes the Product
Owner accountable for effective Product Backlog management, including creating and clearly
communicating the items, and makes the Developers who will do the work responsible for sizing
it[^scrum-guide-2020].

A user story can be judged against INVEST, the acronym Bill Wake published on his own site in August
2003: a story should be Independent, Negotiable, Valuable, Estimable, Small and
Testable[^wake-invest]. DORA's guidance on working in small batches makes a similar point about
size, advising that work be broken "into work units that can be completed independently and in
short timeframes"[^dora-small-batches].

Each story is paired with acceptance criteria, which the ISTQB glossary defines as "the criteria that
a work product must satisfy to be accepted by the stakeholders"[^istqb-acceptance-criteria]. Whether a
criterion can in fact be checked is a question of testability, "the degree to which test conditions
can be established for a component or system, and tests can be performed to determine whether those
test conditions have been met"[^istqb-testability]. A criterion can be written as a concrete example
in the given, when, then form, which Martin Fowler describes as an approach developed by Daniel
Terhorst-North and Chris Matts as part of Behavior-Driven Development[^fowler-given-when-then].

Security requirements belong to the same work. NIST's Secure Software Development Framework, in task
PO.1.2, asks an organisation to identify and document all security requirements for the software it
develops, and to maintain those requirements over time[^nist-ssdf].

SAFe describes the same preparation as a team-level event. Team backlog refinement is "an event that
helps Agile Teams clarify and prepare upcoming stories and features", and its activities include
"removing outdated stories, discovering new ones, and defining acceptance
criteria"[^safe-team-backlog-refinement].

Some teams also make their readiness criteria explicit and visible as a Definition of
Ready[^agile-alliance-dor]. It is a team practice rather than a framework rule: the 2020 Scrum
Guide does not use the term[^scrum-guide-2020]. The artefacts of the phase, in this traditional form,
are refined backlog items, their acceptance criteria and the security requirements that apply.

## AI-assisted practice

The output of the phase is still a document that people agree on. What changes is who does the first
careful reading. As recommended practice, an agent reads the specification while it is being written
and proposes questions about what it leaves unclear or unsaid, and a person answers them. Public
evidence on the reading itself exists but is narrow: an industrial study presented at ICSME 2025
examined language models detecting and explaining ambiguity in real-world industrial requirements,
and found that giving the model ten examples in the prompt classified ambiguous requirements better
than giving none[^requirements-ambiguity-llm]. No public study measures whether this kind of help
improves delivery outcomes, so the practice on this page is recommended practice, not a finding. The
agent's part in the readiness decision is set out in its
[catalog row](workflow-catalog.html#W04).

This way of working belongs to spec-driven development: making expected behaviour and constraints
explicit before implementation, moving from intent through a specification, a plan and tasks, with
clarification wherever the specification leaves questions open[^spec-kit]. Birgitta Böckeler
distinguishes three degrees of commitment to the specification[^bockeler-sdd]. In spec-first work, a
specification is written before the code and used for the task at hand. In spec-anchored work, the
specification is kept after the task and used as the feature evolves. In spec-as-source work, the
specification is the main artefact a person edits, and the code follows from it. The degree a team
chooses decides whether the specification written in this phase outlives the change it describes.

The templates of one open-source spec-driven toolkit build caution into the document itself. Wherever
a prompt leaves something unspecified, the template requires an explicit clarification marker in
place of a guess ("Don't guess"), and its checklists act as "unit tests" for the
specification[^spec-kit-sdd]. A marker left in the text is something a tool can find. As recommended
practice, whatever a tool can decide from the specification alone moves to a deterministic check, and
whatever needs context stays with a person.

Acceptance criteria and access rules written in this phase have a second use. Defined apart from the
code, they become the [independent basis](glossary.html#independent-basis) against which later tests
and checks judge the implementation, so those tests do not inherit the implementation's mistakes.

What stays with a person is intent. An agent can find that a question is open; it cannot know what the
business wants. As recommended practice, the agent proposes and a named person decides, and the
decision is written under that person's name (see [Evidence schema](evidence-schema.html)). In the
site's running example, a hypothetical feature that lets users export customer records, the
specification does not yet say which roles may export which records. That question is recorded as
open and settled before planning, within the access rule R-042, by the people the
[Specification readiness](workflow-catalog.html#W04) row names
([Software factory](software-factory.html)). An agent handed that specification with the
access rule still open stops and asks rather than choosing a rule, which is one of the evaluation
cases on [Skills with evals](skills-and-evals.html).

## Workflows in this phase

The workflow catalog uses its own phase names; this phase corresponds to the catalog's phase 1,
Specify. Each entry below names a workflow by its catalog title and links its row.

- [Specification readiness](workflow-catalog.html#W04): the decision that closes the phase.
- [Design-to-specification handoff](workflow-catalog.html#W03): where design work feeds the
  specification, at the start of the phase.
- [Brownfield pre-flight analysis](workflow-catalog.html#W05): alongside the writing of the
  specification.
- [Threat modeling](workflow-catalog.html#W06): alongside the writing of the specification.
- [Spike](workflow-catalog.html#W07): whenever the phase needs it.

[Task traceability and test planning](workflow-catalog.html#W12) follows in the catalog's next phase,
Plan & design. The idea of readiness itself is covered under
[Definition of Ready](definition-of-ready-and-done.html#definition-of-ready).

## Gates and evidence

Work enters this phase from [Idea](idea.html) and leaves for [Design](design.html). The phase has one
gate, at its exit: the readiness decision in
[Specification readiness](workflow-catalog.html#W04). What starts that decision, which checks run and
who decides are recorded in the catalog row and are not repeated here. The gate passes when the
required checks have passed and the named owners have decided. A passing check never stands in for an
owner's decision: checks confirm that a specification is complete in form, and only a person can say
that it asks for the right thing.

The Definition of Ready tag marks this gate. The criteria a team applies here are its Definition of
Ready, described under [Definition of Ready](definition-of-ready-and-done.html#definition-of-ready)
and not listed on this page.

The gate leaves a readiness record. Later workflows read that record instead of asking the same
questions again, the [evidence hand-off](glossary.html#evidence-handoff) that lets one workflow rely on
another's result. The fields any such record holds are fixed by the
[Evidence schema](evidence-schema.html).

Acceptance criteria that carry identifiers let the tasks, tests and results of later phases point back
to the criterion they serve. The [Traceability spine](traceability-spine.html) describes that chain of
identifiers.

## Roles

Who decides at the gate is named in the [Specification readiness](workflow-catalog.html#W04) row. The
roles that take part in the phase are these.

- **Product owner.** Accountable for effective Product Backlog management, including creating and
  clearly communicating backlog items[^scrum-guide-2020].
- **Developers.** Responsible for sizing the items they will work on[^scrum-guide-2020].
- **Rule owner.** The owner of a rule the specification touches, such as the access rule R-042;
  rules and their owners are kept in the [Rule registry](rule-registry.html).
- **QA or test lead.** As recommended practice, flags acceptance criteria whose
  testability[^istqb-testability] is in doubt before the gate.

## Pitfalls

- **Ambiguity settled in code.** A question the specification leaves open is answered by whoever
  writes the code, often the agent. Sign: review threads ask what a behaviour should be, and the answer
  changes the code but not the specification. The [failure paths](workflows.html#failure-paths) on the Workflows page
  send such a question back to the specification's owner.
- **Gaps filled by guessing.** The agent picks a plausible answer instead of marking what the
  specification does not say. Sign: a specification with no open questions that still surprises its
  owner in review. One toolkit's templates require a marker in place of a guess for this
  reason[^spec-kit-sdd].
- **Readiness on structure alone.** Every check passes and the item moves on with no owner's decision
  recorded. Sign: readiness records that show passing checks and no named decision.
- **Criteria no test can settle.** Criteria such as "responds quickly" or "easy to use" leave no test
  condition to establish[^istqb-testability]. Sign: test design for the item starts with a question to
  the product owner about what the criterion means.
- **Criteria written from the implementation.** Criteria are written or revised after the code to
  match what it does, so tests built from them share its mistakes. Sign: acceptance criteria change in
  the same change as the code they judge. Keeping the criteria an
  [independent basis](glossary.html#independent-basis) prevents it.
- **Criteria without identifiers.** Later tasks and tests cannot say which criterion they serve. Sign:
  a test whose purpose nobody can trace to a criterion. See the
  [Traceability spine](traceability-spine.html).

## Related

- [Idea](idea.html): the phase before, where work enters the backlog.
- [Design](design.html): the phase after, which plans from the ready specification.
- [Definition of Ready](definition-of-ready-and-done.html#definition-of-ready): the tag on this phase.
- [Traceability spine](traceability-spine.html): the chain from acceptance criteria to tasks, tests
  and results.
- [Workflows](workflows.html): the decision unit each catalog row describes.
- [Evidence schema](evidence-schema.html): the shape of the readiness record and every other record.
- [Skills with evals](skills-and-evals.html): the evaluation cases that test how an agent handles an
  open question.
- [Rule registry](rule-registry.html): where rules such as R-042 and their owners are kept.
- Workflow catalog: [Specification readiness](workflow-catalog.html#W04),
  [Design-to-specification handoff](workflow-catalog.html#W03),
  [Brownfield pre-flight analysis](workflow-catalog.html#W05),
  [Threat modeling](workflow-catalog.html#W06) and [Spike](workflow-catalog.html#W07).
- Terminology: [Specification readiness](glossary.html#specification-readiness),
  [Spec-driven development](glossary.html#spec-driven-development) and
  [Independent basis](glossary.html#independent-basis).

## Sources

- Backlog refinement, readiness for selection and accountabilities: the 2020 Scrum
  Guide[^scrum-guide-2020] and SAFe's page on team backlog refinement[^safe-team-backlog-refinement].
- Story quality and the Definition of Ready: Bill Wake on INVEST[^wake-invest] and the Agile Alliance
  glossary[^agile-alliance-dor].
- Acceptance criteria, testability and examples: the ISTQB glossary[^istqb-acceptance-criteria][^istqb-testability]
  and Martin Fowler on given, when, then[^fowler-given-when-then].
- Security requirements: NIST's Secure Software Development Framework, version 1.1[^nist-ssdf].
- Agents and ambiguity: an industrial study of language models on requirements[^requirements-ambiguity-llm].
- Spec-driven development: an open-source spec-driven toolkit and its description of the
  method[^spec-kit][^spec-kit-sdd], and Birgitta Böckeler on degrees of commitment to a
  specification[^bockeler-sdd].
- Batch size: DORA's page on working in small batches[^dora-small-batches].
