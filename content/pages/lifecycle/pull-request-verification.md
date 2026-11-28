---
id: pull-request-verification
type: workflow
band: lifecycle
map_box: pull-request verification · security & performance checks by tier
title: Pull-request verification
summary: The workflow that decides whether one revision of a change may join the mainline, on check results recorded for that exact revision, with a named reviewer deciding and an agent's review as advice.
key_terms: [workflow, three-roles, risk-tier, gate, validator, review-skill, could-not-run, evidence-record, evidence-handoff, failure-path, independent-basis, deterministic-gate, export-example, pre-integration-review]
sources: [fowler-branching-patterns, fowler-ci, google-eng-practices-standard, google-eng-practices-small-cls, google-eng-practices-speed, google-eng-practices-review, bockeler-harness, bockeler-sensors, nist-800-53, metr-reward-hacking, anthropic-claude-37-system-card, nist-ai-600-1, parasuraman-manzey-2010, perry-2023, istqb-rbt, nist-ssdf, owasp-asvs, github-status-checks, sarif-2-1-0, dora-streamlining-change-approval, slsa-build-track-basics, slsa-build-requirements, dora-metrics, dora-trunk-based-development, lean-vs-manager, safe-inspect-and-adapt]
related: [develop-build-qa, spec-readiness, design-conformance, release-readiness, deploy-verification, incident-feedback, workflows, evidence-schema, validators, skills-and-evals, rule-registry, engineering-kit, adapters, traceability-spine, inspect-and-adapt, definition-of-ready-and-done]
review_record: content/reviews/1.6.0-lifecycle.md
---

## Decision

May this revision of the change join the mainline as it stands? The catalog states it as
[W23](workflow-catalog.html#W23).

In the AI SDLC (the software development lifecycle with AI agents doing part of the work), this is
the call that closes the [Develop, Build and QA](develop-build-qa.html) stretch. Martin Fowler
defines the mainline as the codeline a team considers "the current state of the team's code", and
names the practice of peer-reviewing every commit before the mainline accepts it pre-integration
review.[^fowler-branching-patterns] The call matters because continuous integration "can only work
if the mainline is kept in a healthy state".[^fowler-ci] The bar is not perfection. Google's guidance
for reviewers favours approving a change once it definitely improves the overall health of the
code, even if it is not perfect, and never accepting one that definitely makes code health worse,
outside an emergency.[^google-eng-practices-standard]

The decision attaches to one revision, a single identified state of the change, because a result is
evidence only for the code it examined ([Evidence schema](evidence-schema.html#revisions-and-versions)).

## Trigger

A run starts when the author offers a change for merge at a named revision. The usual vehicle is a
pull request, which Fowler describes as a mechanism built to combine feature branching
with pre-integration review.[^fowler-branching-patterns]

Each new revision pushed to the change starts a new run. The record of the earlier run stays with
the earlier revision as history and is never carried onto the new one
([Evidence schema](evidence-schema.html#revisions-and-versions)). A change its author still marks as
a draft, not yet ready for review, may run checks for the author's benefit, but it does not start
the merge decision; this is recommended practice, since no public source sets it out. A mainline that
moves after a run has finished does not restart that run by itself; the case is handled under
Failure paths below.

## Inputs

No public source lists what a merge decision should read, so the set below is this site's
recommended practice, drawn from the pages that describe each input.

- **The diff at the named revision.** Google's guidance describes a reviewable change as one
  self-contained change that addresses one thing and includes the tests related to
  it.[^google-eng-practices-small-cls] Changed behaviour without a changed or added test is
  therefore something the reviewer can see at once.
- **The readiness record** written by [Specification readiness](spec-readiness.html), which gives
  the intent the change is judged against, so the merge decision does not ask the specification's
  questions again.
- **The entries in the [Rule registry](rule-registry.html)** for every rule the change touches.
  Validators and the review skill both cite rules by identifier, so the registry is what lets their
  results line up ([Rule registry](rule-registry.html#how-the-rest-of-the-kit-refers-to-rules)).
- **The kit version and the project configuration**, which the record names separately so a later
  reader knows which rules and thresholds applied
  ([Engineering Kit](engineering-kit.html#project-configuration)).

What the run checks against must be defined apart from the implementation. When one agent writes
code and tests from one understanding, both can carry the same mistake; the term for the remedy is
an [independent basis](glossary.html#independent-basis), and
[Develop, Build and QA](develop-build-qa.html#qa-with-agents) gives the research behind it.

One precondition comes before everything else: each input exists and is current for this
revision. If one is missing or describes an older state, the run stops and says which record it is
waiting for, rather than reaching a decision on a guess
([Workflows](workflows.html#the-parts-of-a-workflow-definition)).

## Agent task

The agent's task in this workflow is set out in [W23](workflow-catalog.html#W23). The agent is a
[review skill](glossary.html#review-skill): an agent that reads the change against the applicable
rules and proposes findings. In Birgitta Böckeler's vocabulary it is an inferential control, of
the kind AI code review belongs to, as opposed to a computational one such as a test or a
linter.[^bockeler-harness][^bockeler-sensors] Each finding carries the identifier of the rule it concerns and sits beside the
validators' results for the same rule, but no finding changes a check's status or the record's
overall status ([Evidence schema](evidence-schema.html#agent-findings-and-decisions)).

Three limits hold, each as this site's recommended practice:

- **It does not approve or merge.** No party both produces a result and accepts it, the principle
  security controls call separation of duties.[^nist-800-53]
- **It does not resolve its own findings.** A person accepts or rejects each finding, and the
  decision is recorded under that person's name.
- **It does not edit a test or a check in the change it reviews.** METR describes models trying to
  raise their score by modifying tests or scoring code,[^metr-reward-hacking] and a model developer's
  system card reports special-casing of tests, sometimes by changing the tests
  themselves.[^anthropic-claude-37-system-card]

Its advice is not verification. NIST's profile for generative AI lists automation bias and
over-reliance among the risks of human-AI configuration;[^nist-ai-600-1] Parasuraman and Manzey's
review finds that people relying on an imperfect aid miss what it misses and follow it when it is
wrong;[^parasuraman-manzey-2010] and in Perry and colleagues' study, users of an AI code assistant
wrote less secure code and were more likely to believe it secure.[^perry-2023] The
[Workflows](workflows.html#the-three-roles-agent-checks-and-people) page sets out what follows for
the split between agent, checks and people.

## Checks

The page describes how the set of checks is formed and reported; what each check does is on
[Validators](validators.html) and in the catalog's QA rows.

**Selected by tier.** Which security and performance checks a revision runs follows from its
[risk tier](glossary.html#risk-tier), as
[Workflows](workflows.html#risk-tiers-same-definition-different-cost) explains. Public frameworks
leave that choice to the team's own judgement of risk. The ISTQB glossary defines risk-based testing
as an approach in which the selection and use of test activities rest on risk;[^istqb-rbt] the SSDF
asks the organisation to determine whether code review or code analysis is used, and whether and
which kinds of executable testing are performed (PW.7.1, PW.8.1);[^nist-ssdf] and the ASVS asks an
organisation to analyse its risks and decide which verification level to aim for.[^owasp-asvs] The
checks themselves are the catalog's QA rows, [W17](workflow-catalog.html#W17) to
[W21](workflow-catalog.html#W21).

**Fixed before results.** The list of checks expected for the revision is written into the record before
any check reports ([Evidence schema](evidence-schema.html#expected-checks-before-results)).

**One explicit pass.** Every result takes one of four states, passed, failed, skipped or
[could_not_run](glossary.html#could-not-run), and only an explicit pass counts as a pass
([Engineering Kit](engineering-kit.html#the-could_not_run-result)). The distinction matters on a
change host: one host's documentation says a job skipped by a condition reports "Success", while a
workflow skipped by path filtering leaves its checks pending and blocks the
merge.[^github-status-checks] SARIF, the OASIS format for analysis results, offers a standard
precedent by recording whether the tool's run itself succeeded, apart from its
results.[^sarif-2-1-0]

**Report-only or required.** A check can report without holding the merge, or hold it. How a check
moves from one to the other is on [Validators](validators.html).

## Guardrails

How a workflow's agent is limited, and its place among the three roles, is described on
[Workflows](workflows.html#the-three-roles-agent-checks-and-people). The bounds below are specific
to a merge run, and each is recommended practice.

- **Checks and code apart.** A change that edits a check or the build configuration together with
  the code that check examines stops for a person, as
  [Develop, Build and QA](develop-build-qa.html#build-with-agents) describes.
- **No write to the mainline.** The run reads, checks and records. Merging is a separate act by a
  person once the decision is taken.

## Human decision

A person takes the merge call on what a tool cannot judge, and the call is recorded under that
person's name ([Evidence schema](evidence-schema.html#agent-findings-and-decisions)). Google's
guidance for reviewers gives the areas to look at, in this order: design, functionality,
complexity, tests, naming, comments, style, consistency and
documentation.[^google-eng-practices-review] It also says how to judge: technical facts and data
overrule opinions and personal preferences, and the style guide is the authority on
style.[^google-eng-practices-standard]

When author and reviewer disagree, Google's sequence is to seek consensus first, then to talk face
to face or by video and record the outcome as a comment on the change, then to escalate to a
broader team discussion or to a technical lead, maintainer or engineering manager, without letting
the change stall.[^google-eng-practices-standard]

Approval does not override a required check's result, and a departure from a rule is a matter for
exception handling ([W33](workflow-catalog.html#W33)); this is recommended practice.

DORA finds change approval best done through peer review during development, supplemented by
automation, and finds heavyweight approval from outside the team harmful to delivery performance;
it treats segregation of duties, approval by someone other than the author, as met by peer
review.[^dora-streamlining-change-approval] When an agent wrote the code, the developer who directed
it remains the author, so the reviewer is still someone else
([Develop, Build and QA](develop-build-qa.html#roles)).

## Outputs and evidence

The run leaves one verification record for the revision, in the shape the
[Evidence schema](evidence-schema.html) fixes: the expected checks and their results, the review
skill's findings, the decisions with their deciders, and the derived overall status. Public
practice expects findings to be kept, not only discussed: the SSDF asks teams to record and triage
issues found by code review and analysis in their workflow or issue tracking system
(PW.7.2).[^nist-ssdf] Provenance of the built output comes from the build platform, not from
whoever writes the record. SLSA's Build track calls for provenance generated by a hosted build
platform,[^slsa-build-track-basics] and its requirements put that generation out of reach of the
tenant whose build it runs.[^slsa-build-requirements]

### Who reads the record

Each later reader takes the record as it stands instead of asking again, the pattern this site
calls the [evidence hand-off](glossary.html#evidence-handoff).

- **[Release readiness](release-readiness.html)** reads the records for the revisions a release
  candidate contains.
- **[Deploy verification](deploy-verification.html)** reads them indirectly, through the release
  record.
- **The [traceability spine](traceability-spine.html#the-link-between-each-adjacent-pair)** takes
  two links from it: the revision named on the record ties each test result to the change, and the
  revisions a release contains tie the change to the release.
- **[Incident feedback](incident-feedback.html)** opens it when a later miss is traced back to this
  run, to see what was checked and who decided.
- **[Inspect and Adapt](inspect-and-adapt.html)**[^safe-inspect-and-adapt] reads could_not_run results by cause and the
  report-only checks that may become required.
- **The workflow's owner** reads the records in aggregate for the measures below.

### In the customer-record export

The customer-record export is the site's running example, a hypothetical feature that lets users
export customer records. On its first revision, the access validator for rule R-042 fails on the
background worker's broader query, the review skill's finding on the same query sits beside it as
advice, the 50k-row load scenario for the volume-limit rule R-017 returns could_not_run because the
load-test tool is missing from the runner image, and a request to exceed R-017's row limit is
pending with the security owner; the overall status is blocked
([Evidence schema](evidence-schema.html#the-customer-record-export)). What this workflow adds is the
shape of what follows. The worker's query is narrowed in a second revision, which gets a record of
its own while the first stays as history. The could_not_run goes to whoever owns the runner image,
not to the change's author. The reviewer, and later release readiness, read the record for the
revision that would merge, not a thread of comments.

## Failure paths

The general failure paths of a workflow are on
[Workflows](workflows.html#failure-paths). The paths below are the ones a merge decision meets in
particular, each with the party who acts next.

- **A new revision arrives during review.** The record of the old revision stays as history and a
  new run starts ([Evidence schema](evidence-schema.html#revisions-and-versions)). Next: the run for
  the new revision; the reviewer reads its record, not the old one.
- **The mainline moves under the change.** Even a clean merge can hide semantic conflicts, which is
  why the merged code is built and the mainline's commit suite run.[^fowler-branching-patterns]
  Every push to the mainline triggers a build of its head, and a failed integration build is fixed at
  once, generally by reverting the commit.[^fowler-ci] A verification result applies to the
  revision it verified; re-verifying the integrated result before merge is recommended practice.
  Next: the author updates the change, which starts a new run.
- **A required check fails.** The record cannot reach a positive status, and the change goes back to
  its author; the fix arrives as a new revision with a record of its own, as the narrowed worker
  query does in the example above (recommended practice). Next: the author.
- **The change edits a check together with the code it checks.** This is a finding in its own
  right ([Develop, Build and QA](develop-build-qa.html#build-with-agents)). Next: a person who owns
  the check decides whether the edit stands.
- **The diff is too large to review.** The reviewer asks for a split; where that is not possible,
  Google's guidance is to comment on the overall design and send the change
  back.[^google-eng-practices-speed] Next: the author.
- **A required check returns could_not_run.** The record cannot reach a positive status, and the
  result goes to the owner of the runner or environment, since the change may be sound
  ([Engineering Kit](engineering-kit.html#the-could_not_run-result),
  [Adapters](adapters.html#reporting-that-a-tool-could-not-run)). Next: that owner restores the tool
  or environment and the check runs again on the same revision.
- **An input is missing or stale.** The run stops and names the record it waits for (recommended
  practice). Next: the workflow that writes that record, for example
  [Specification readiness](spec-readiness.html).
- **Author and reviewer cannot agree.** Google's escalation sequence under Human decision
  applies.[^google-eng-practices-standard] Next: whoever the sequence reaches.

## Measures

No public source gives target values for these measures, and this page gives none. DORA advises
setting a baseline of current performance and improving on it over time, rather than competing with
other teams.[^dora-metrics] Each measure below is compared with the same team's values before the
workflow became required, or with the period named.

- **Delivery performance.** DORA's change lead time, change fail rate and deployment rework
  rate,[^dora-metrics] whose definitions belong to the assurance band of the map. Baseline: the
  team's values for a period before the workflow became required.
- **Time to first review response.** Google's guidance says one business day is the maximum time it
  should take to respond to a review request, and that a fast individual response matters more than
  how long the whole review takes.[^google-eng-practices-speed] DORA counts the time taken to
  approve code changes among its measures for trunk-based
  development,[^dora-trunk-based-development] and suggests tracking time spent waiting for
  approvals.[^dora-streamlining-change-approval] Fowler notes that pre-integration review usually adds
  significant friction to continuous integration,[^fowler-ci] which is why the wait is worth
  watching. Baseline: the same team before the workflow.
- **could_not_run results per required check, by cause.** A rising count for one cause points at
  an environment, not at the code (recommended practice). Baseline: the check's report-only period
  ([Validators](validators.html)).
- **Share of agent findings rejected.** This is an input to the review
  skill's evaluations ([Skills with evals](skills-and-evals.html)), not a target (recommended
  practice). Baseline: the rejection share when the review skill was first introduced.

## Owner

One accountable owner holds and changes the workflow itself, a role distinct from the reviewer who
decides each run ([Workflows](workflows.html#definition)). Lean practice offers the model: a value
stream has an accountable manager who may not own the people and resources in it.[^lean-vs-manager]
DORA names pitfalls of change approval that
such an owner guards against; three of them are treating all changes equally,
failing to apply continuous improvement, and responding to problems by adding more
process.[^dora-streamlining-change-approval]

## Related

- Takes evidence from: [Specification readiness](spec-readiness.html) and
  [Design conformance](design-conformance.html).
- Hands evidence to: [Release readiness](release-readiness.html),
  [Deploy verification](deploy-verification.html) and [Incident feedback](incident-feedback.html).
- Phase: [Develop, Build and QA](develop-build-qa.html).
- Core: [Workflows](workflows.html), [Evidence schema](evidence-schema.html),
  [Validators](validators.html), [Skills with evals](skills-and-evals.html),
  [Rule registry](rule-registry.html), [Engineering Kit](engineering-kit.html) and
  [Adapters](adapters.html).
- Readers of the record: [Traceability spine](traceability-spine.html) and
  [Inspect and Adapt](inspect-and-adapt.html).
- Catalog rows: pull-request verification [W23](workflow-catalog.html#W23); the QA rows it gathers
  results from, [W17](workflow-catalog.html#W17) to [W21](workflow-catalog.html#W21); task
  execution loop [W13](workflow-catalog.html#W13); exception handling
  [W33](workflow-catalog.html#W33).
- Terminology: [review skill](glossary.html#review-skill),
  [could_not_run](glossary.html#could-not-run), [risk tier](glossary.html#risk-tier),
  [evidence record](glossary.html#evidence-record) and
  [pre-integration review](glossary.html#pre-integration-review).

## Sources

- Mainline, pre-integration review and integration: Martin Fowler on branching patterns and on
  continuous integration.[^fowler-branching-patterns][^fowler-ci]
- Code review practice: Google's engineering practices on the standard of code review, the speed of
  reviews, small changes and what to look for.[^google-eng-practices-standard][^google-eng-practices-speed][^google-eng-practices-small-cls][^google-eng-practices-review]
- Change approval, trunk-based development and delivery metrics:
  DORA.[^dora-streamlining-change-approval][^dora-trunk-based-development][^dora-metrics]
- Harness vocabulary: Böckeler.[^bockeler-harness][^bockeler-sensors]
- Over-reliance on automated judgment: NIST's generative AI profile, Parasuraman and Manzey, and
  Perry and colleagues.[^nist-ai-600-1][^parasuraman-manzey-2010][^perry-2023]
- Agents changing tests: METR and a model developer's system
  card.[^metr-reward-hacking][^anthropic-claude-37-system-card]
- Risk-based selection of checks: the ISTQB glossary, the NIST SSDF and the OWASP
  ASVS.[^istqb-rbt][^nist-ssdf][^owasp-asvs]
- Results and provenance: SARIF, SLSA and one change host's documentation on skipped
  checks.[^sarif-2-1-0][^slsa-build-track-basics][^slsa-build-requirements][^github-status-checks]
- Separation of duties: NIST's security and privacy control catalogue.[^nist-800-53]
- Accountable ownership: the Lean Enterprise Institute on the value-stream manager.[^lean-vs-manager]
- Inspect and Adapt: Scaled Agile, Inc.'s page on the event.[^safe-inspect-and-adapt]
- The inputs set, the agent's limits, the guardrails, what approval does not override, the handling
  of a failed check, the stop on a missing input, re-verification after the mainline moves and the
  last two measures are this site's recommended practice; no public source states them.
