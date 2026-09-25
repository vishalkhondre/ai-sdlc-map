---
id: workflows
type: concept
band: core
map_box: Workflows
title: Workflows
summary: A workflow is one delivery decision run end to end, with a trigger, an agent task, automated checks, a named human decision, an evidence record and one owner.
key_terms: [workflow, three-roles, risk-tier, failure-path, evidence-handoff, could-not-run, evidence-record, gate, validator, review-skill, specification-readiness, independent-basis, harness-engineering, feedback-path, software-factory, export-example]
sources: [bockeler-harness, bockeler-sensors, openai-harness, fowler-ci, fowler-deployment-pipeline, fowler-nondeterminism, lean-vsm, lean-vs-manager, dora-vsm-guide, dora-2024-report, dora-2025-report, dora-ai-capabilities, dora-metrics, nist-ai-rmf, nist-ai-600-1, nist-800-53, parasuraman-manzey-2010, perry-2023, istqb-rbt, iso-29119-1, spec-kit, github-status-checks]
related: [harness-engineering, engineering-kit, rule-registry, validators, skills-and-evals, evidence-schema, software-factory]
review_record: content/reviews/1.4.0-core.md
---

## Definition

In the AI SDLC (the software development lifecycle with AI agents doing part of the work), a
workflow is one delivery decision carried from the event that starts it to a recorded outcome.
Its definition names nine parts: the trigger, the inputs it reads, the task the coding agent
performs, the automated checks that run, the guardrails that bound the agent, the person who
decides, the evidence it leaves, the place its lessons go, and one accountable owner. "Is this
change ready to merge?" is a workflow. So is "Is this specification ready for planning?" The word
is used here in this narrow sense, which this site coined; the parts list is the site's
recommended definition, not an industry standard.

The idea has a long lineage. Lean value-stream mapping diagrams every step in the material and
information flows needed to deliver a product or service[^lean-vsm], and lean practice gives the
whole stream an accountable manager who may not own the people and resources in it[^lean-vs-manager].
DORA recommends value stream mapping to see how work flows from idea to production and where it
stalls[^dora-vsm-guide]. A workflow is a smaller unit than a value stream: the single step in
which a decision is made, defined tightly enough that an agent can take part in it without
taking the decision.

A workflow is not the same as three nearby things:

- **A pipeline.** A deployment pipeline breaks the build into stages, each adding confidence at
  the cost of more time[^fowler-deployment-pipeline]. A workflow often uses a pipeline to run
  its checks, but it also holds the agent's task, the human decision and the evidence left
  behind, none of which a pipeline owns.
- **A process.** A documented process says how work ought to go. A workflow exists only when it
  runs and leaves evidence each time; a procedure that nobody follows is not one.
- **A prompt.** A prompt asks the agent to behave in a certain way; it enforces nothing. Inside a
  workflow, a prompt is at most one part of the agent's task, and every rule that must hold is
  enforced by a check or decided by a person.

## Why it matters

AI assistance can raise the volume of change without raising a team's capacity to judge it.
DORA's 2024 research estimated that, as AI adoption increased, software delivery
throughput and stability both fell, and it pointed teams back to basics such as small batch
sizes and robust testing[^dora-2024-report]. Its 2025 report, *State of AI-assisted Software
Development*, found AI adoption now goes with higher throughput but still with lower delivery
stability, describes AI as an amplifier of a team's existing strengths and weaknesses, and names
strong automated testing, mature version control practices and fast feedback loops as the
control systems that stop a rise in change volume from turning into instability[^dora-2025-report].

Those control systems need a place to attach. Without a defined workflow, a change advances on a
status flag or a conversation, and a month later the team cannot reconstruct which checks ran or
whose call it was. Agent output is accepted on trust, reviewers spend their time on things a tool
could catch, and a failed check gets waved through or fixed off the record, so it fails the same
way next time. A workflow is the recommended answer:
the smallest unit to which a team can attach checks, a named decision and a record, and then
improve from what that record shows. This is presented as recommended practice; no public study
measures the effect of defining work this way.

## How it works

### The parts of a workflow definition

The table gives each part, what it holds, and how it reads for one running example: verifying a
pull request for the customer-record export, a feature that lets users export customer records
(the pull-request verification entry in the [workflow catalog](workflow-catalog.html#W23)).

| Part | What it holds | In the export example |
|---|---|---|
| Trigger | The event that starts a run | A pull request is marked ready, or its revision changes |
| Inputs | Upstream records and the rules that apply | The readiness record for the export specification; rules R-042 (who may export which records) and R-017 (the volume limit for large exports) |
| Agent task | What the agent does, inside set limits | A review skill reads the diff against the specification and the two rules and writes findings tagged to rule identifiers |
| Checks | Deterministic checks the change's risk tier selects | The R-042 access validator and the R-017 load scenario |
| Guardrails | What the agent may and may not touch | The agent can comment on the pull request; it cannot approve, merge or change the checks |
| Human decision | The named person who decides, and on what | The reviewer decides whether the change is ready; the security owner decides on anything touching R-042 |
| Outputs | The evidence record the run leaves | Each check with its result, the agent's findings and how each was resolved, and the decisions, tied to the revision |
| Feedback | Where a miss is classified and sent | A defect found later is traced back to this run and becomes a new test or a sharper rule |
| Owner | One person accountable for the workflow itself | The engineering lead who owns merge readiness |

The inputs matter as much as the checks. When an agent writes both the code and its tests from
the same incomplete understanding, both can share one mistaken assumption, so verification needs
an independent basis defined apart from the implementation: here, the readiness record and the
two rules. Spec-driven toolkits produce that kind of upstream input by turning requirements into
a specification, a plan and tasks before implementation starts[^spec-kit].

A run is worth starting only if it can reach a decision. As recommended practice, the workflow
first confirms that the records it reads exist and are current, and that the change is small
enough to examine in full. When something is missing, the run stops and states what it is
waiting for, rather than working around the gap. Size matters more once an agent writes the
code: a broader request yields more code, more tests and more prose, while the time a reviewer
can give does not grow to match. Keeping each change within what one reviewer can read in full is
recommended practice rather than a measured finding. It applies, at the scale of one change, the
advice DORA gives when it lists working in small batches among the capabilities that amplify the
benefit of AI[^dora-ai-capabilities].

### The three roles: agent, checks and people

Every workflow splits its work three ways and keeps the three apart.

- **The agent** takes on high-volume work where an imperfect first attempt is cheap to correct,
  such as searching the codebase, writing code and tests, and summarising a diff for review.
  Its output feeds a decision someone else makes.
- **The checks** enforce what a tool can decide reliably and what must not be wrong. Böckeler
  separates computational controls, which are deterministic and fast (tests, linters, type
  checkers), from inferential ones such as AI code review, which are more expensive and
  non-deterministic but give richer semantic judgment[^bockeler-harness]. On this site, a
  deterministic check tied to a rule identifier is a validator, and an agent that reads a diff
  and proposes findings is a review skill[^bockeler-sensors]. The review skill informs a
  decision; it never stands in for a check that must not be wrong.
- **The people** make the calls that depend on context the workflow cannot hold, from accepting
  a specification to letting a change ship; each call is recorded under the name of whoever
  made it.

One model vendor's account of an agent-first team describes the same split as people steering
while agents execute, with constraints enforced by automated checks[^openai-harness]. Risk
frameworks expect it too: the NIST AI Risk Management Framework calls for policies and procedures
that define and differentiate roles and responsibilities for human-AI configurations and the
oversight of AI systems[^nist-ai-rmf].

The agent's limits come from the permissions of the identity it runs under, not from its
instructions. In the export example, the review skill's credential can post comments on the pull
request but holds no merge right and no write access to the check configuration, so no wording
in a prompt can widen what it does. This is least privilege, which NIST's control catalogue
applies to processes acting on behalf of users as well as to the users
themselves[^nist-800-53].

Blurring the roles fails in two ways:

1. **The agent treated as verifier.** NIST's profile for generative AI lists over-reliance and
   automation bias among the risks of human-AI configuration[^nist-ai-600-1]. A widely cited
   review of the research reports that people relying on an imperfect decision aid both miss
   what it misses and follow it when it is wrong, that experts and novices are affected alike,
   and that training or instructions alone do not prevent it[^parasuraman-manzey-2010]. In one
   user study, participants with an AI code assistant wrote less secure code than those without
   one, yet were more likely to believe their code was secure[^perry-2023]. So AI review can
   raise findings but never grants approval.
2. **People treated as checks.** Reviewers re-check formatting, test coverage or rule compliance
   that a tool could enforce, and their attention runs out before the real decisions. Each such
   rule moves to a gate.

What keeps the roles apart is that no party both produces a result and accepts it, the idea
security controls call separation of duties[^nist-800-53]. The agent that wrote the export code
does not decide whether it satisfies R-042: the validator does, and the security owner decides on
the access design.

### Risk tiers: same definition, different cost

A risk tier is a label, set when the change is planned, that decides which checks and which
reviewers a run requires; the workflow's definition stays the same at every tier. Scaling
verification effort to risk is established testing practice: in risk-based testing, the type and
level of risk govern which test activities are selected and how much effort they
receive[^istqb-rbt][^iso-29119-1]. As recommended practice, the tier follows from what the change
touches, such as the data it reads and the rules that apply, and a lower tier never drops a rule
that applies.

In the export example, the change reads customer data and applies an access rule, so its tier
calls for both the R-042 validator and the R-017 load scenario, and adds the owner of the access
rule as a required reviewer. A change to the export button's label would run the same workflow
with fewer checks and one reviewer.

The tier set at planning can turn out wrong once the diff exists, so the recommended practice is
to work it out again for each revision. If a revision of the label change also edits the export
query, the tier rises and the R-042 validator and the security owner join the run.

### Failure paths

A failure path is the defined response to one kind of interruption. Each names who acts next,
and the fix is made where the problem started, not where it was noticed. In the export example:

- **A check finds a violation.** The R-042 validator fails because a background export job reads
  records the requesting user may not see. The change goes back to implementation, is fixed and
  the check reruns.
- **A required check could not run.** The R-017 load scenario reports `could_not_run` because the
  load-test tool is missing from the runner image. The run cannot show a positive status, and
  the runner image's owner is told. The result is neither a pass nor a defect in the code; the
  fix belongs to whoever maintains the runner.
- **A requirement is ambiguous.** The review skill notes that the specification does not say
  whether deleted customers are exported. The specification's owner answers and the
  specification is updated; nobody settles it in code.
- **An agent finding is rejected.** The reviewer rejects a finding as a false alarm. The
  rejection and its reason are recorded, so the review skill can be tuned against real misses.
- **An exception is requested.** The change would let one export go past R-017's row limit. The
  request goes to whoever holds that decision right, and a granted exception is recorded against
  R-017 with an owner, a reason and an expiry. R-042, as an access rule, is not open to exception.

Treating a check that produced no result as a pass is the most damaging mistake on this list,
because a broken check then passes every change it was meant to stop. As recommended practice,
only an explicit pass counts as a pass. A check that times out, crashes or never reports is
shown as a state of its own, so the run cannot show a positive status; what that means for the
merge is set in assurance. Continuous integration practice already treats a broken build as
something to fix at once rather than wave through[^fowler-ci].

Each return also says where the problem started, and as recommended practice the record keeps
that cause. A string of `could_not_run` results traced to one runner image is a platform fix, not
a coding one, and the workflow's owner can see that only if returns are recorded by cause.

### What a workflow hands on

What a workflow produces is a record that later steps can read, rather than a notification that
something is done. The next workflow consults that record; it does not run the checks again or
ask around: the readiness record configures verification, and the verification record for the
export change is what release readiness later reads. This evidence hand-off only works if each
record names the exact revision it describes. A new revision gets a new record and the old one
stays as history, since a result for an earlier revision says nothing reliable about the code as
it is now. The fields a record holds are fixed by the [Evidence schema](evidence-schema.html).

Findings also travel backward. When a defect reaches users, the team works out which workflow
should have caught it and why it did not, and that workflow's owner receives the finding. This
is the feedback path, the site's name for what Böckeler calls the steering
loop[^bockeler-harness].

### When a team has a workflow

As recommended practice, a team has a workflow once every qualifying change goes through it and
leaves a record the next decision reads: for the export feature, anyone can open the verification
record for the pull request's latest revision and see what ran and who decided. Whether the
workflow improves delivery then shows in the team's software delivery performance
measures[^dora-metrics].

The list of workflows across the lifecycle, each with its decision, trigger, agent task, checks,
human decision and evidence, is the [workflow catalog](workflow-catalog.html).

## Where it sits on the map

Workflows sit in the core band, the part of the map that shows what does the work. The band reads
as one row: Harness engineering, then the Engineering Kit, then Workflows, then the Software
factory. Before workflows comes [Harness engineering](harness-engineering.html), the discipline of
deciding what an agent may read and do, what a machine checks and what a person decides. Next,
still before workflows, is the [Engineering Kit](engineering-kit.html), the installable package
every workflow draws on: its [Rule registry](rule-registry.html) supplies the rules a run
applies, its [Validators](validators.html) are the checks, its
[Skills with evals](skills-and-evals.html) shape the agent's task, and its
[Evidence schema](evidence-schema.html) fixes what each run records. After workflows comes the
[Software factory](software-factory.html), the operating state that appears when many workflows
share rules, evidence and feedback.

Outside the core band, the lifecycle band places each workflow in its phase, through the
[workflow catalog](workflow-catalog.html). The assurance band reads the evidence records a
workflow leaves, and the adoption path decides which workflow a team builds first.

## Pitfalls

- **A documented process mistaken for a workflow.** The steps are written down but runs leave no
  record. Sign: nobody can show the evidence record for last week's changes.
- **The agent as approver.** An AI review comment is read as sign-off. Sign: reviewers approve
  within minutes of the agent's summary, with no findings of their own.
- **Reviewers doing a tool's job.** Review threads fill with comments about formatting, missing
  tests or naming rules. Sign: the same kind of comment recurs across many changes; each one is
  a rule waiting to become a gate.
- **Silence read as success.** A required check is missing from the results and the change
  merges anyway. Sign: the list of expected checks is not recorded before results arrive. The
  documentation of at least one widely used change host states that a job skipped because of a
  condition reports its status as success[^github-status-checks], so a check that never ran can
  look like a pass unless it is reported as its own state.
- **A flaky check re-run until it passes.** The pass after a retry is recorded like any other,
  and the check stops meaning anything. Sign: one check fails and passes on the same revision
  with no change in between. Non-deterministic tests erode trust in the whole suite, and
  quarantine is at most a short-term, bounded measure while the cause is
  fixed[^fowler-nondeterminism].
- **Exceptions that never end.** The same waiver is granted change after change. Sign:
  exceptions with no expiry date, or one rule collecting most of the exceptions.
- **A run too large to review.** More is attempted in one change than a reviewer can read with
  care. Sign: time spent reviewing does not grow with change size, or large diffs are approved
  with few comments. The fix is to split the work before it starts.
- **Tiers chosen for convenience.** A change is put in a lighter tier to save time. Sign: the
  recorded tier does not match what the change touched, or a lighter tier carries no reason and
  no name.
- **Hand-off by conversation.** The next workflow asks in chat whether security looked at the
  change. Sign: a downstream decision cites a message rather than an evidence record.

## Related

- [Harness engineering](harness-engineering.html): the discipline a workflow puts into practice.
- [Engineering Kit](engineering-kit.html): the reusable package every workflow draws on.
- [Rule registry](rule-registry.html): where the rules a workflow applies, and their owners, are
  kept.
- [Validators](validators.html): the deterministic checks, and how they report a result that
  could not be produced.
- [Skills with evals](skills-and-evals.html): the packaged guidance behind the agent's task and
  the review skill.
- [Evidence schema](evidence-schema.html): the fixed shape of the record each run leaves.
- [Software factory](software-factory.html): what emerges when many workflows share rules,
  evidence and feedback.
- [Workflow catalog](workflow-catalog.html): the list of workflows across the lifecycle,
  including [pull-request verification](workflow-catalog.html#W23).
- [Workflow in the terminology](glossary.html#workflow): the short definition and its
  attribution.

## Sources

- Lean value-stream practice: the Lean Enterprise Institute's definitions of value-stream
  mapping[^lean-vsm] and the value-stream manager[^lean-vs-manager], and DORA's guide to value
  stream mapping[^dora-vsm-guide].
- Pipelines, continuous integration and test reliability: Martin Fowler on the deployment
  pipeline[^fowler-deployment-pipeline], continuous integration[^fowler-ci] and non-deterministic
  tests[^fowler-nondeterminism].
- AI-assisted delivery: DORA's 2024 findings[^dora-2024-report], its 2025 report[^dora-2025-report],
  its AI Capabilities Model[^dora-ai-capabilities] and its research programme[^dora-metrics].
- Harness vocabulary: Birgitta Böckeler on harness engineering[^bockeler-harness] and on
  sensors[^bockeler-sensors], and one model vendor's account of harness engineering in an
  agent-first team[^openai-harness].
- Human oversight and over-reliance: the NIST AI Risk Management Framework[^nist-ai-rmf], its
  generative AI profile[^nist-ai-600-1], Parasuraman and Manzey's review of automation
  bias[^parasuraman-manzey-2010] and Perry and colleagues' study of AI code
  assistants[^perry-2023].
- Separation of duties and least privilege: NIST's security and privacy control
  catalogue[^nist-800-53].
- Risk-based testing: the ISTQB glossary[^istqb-rbt] and ISO/IEC/IEEE 29119-1[^iso-29119-1].
- Upstream inputs and result states: an open-source spec-driven toolkit[^spec-kit] and one change
  host's documentation on skipped checks[^github-status-checks].
