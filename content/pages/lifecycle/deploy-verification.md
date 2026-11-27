---
id: deploy-verification
type: workflow
band: lifecycle
map_box: deploy verification
title: Deploy verification
summary: The workflow that decides whether a revision now running in an environment stays there or the way back is taken, by comparing it with a control and with the service's objectives, and by treating a missing signal as a result of its own, never as health.
key_terms: [ai-sdlc, workflow, three-roles, gate, could-not-run, evidence-record, evidence-handoff, failure-path, deploy-versus-release, canary-release, service-level-objective, export-example]
sources: [sre-workbook-canarying, sre-book-release-engineering, sre-book-monitoring, twelve-factor-config, deployverif-sre-book-slo, fowler-blue-green, fowler-canary-release, google-agentic-sre, nist-800-53, github-status-checks, sre-book-being-on-call, twelve-factor-parity, dora-metrics, dora-monitoring-observability, bockeler-sensors, incident-sre-book-postmortem]
related: [deploy, release, release-readiness, incident-feedback, operate, traceability-spine, workflows, evidence-schema, validators, adapters]
review_record: content/reviews/1.6.0-lifecycle.md
---

## Decision

In the AI SDLC (the software development lifecycle with AI agents doing part of the work), deploy
verification is the [workflow](glossary.html#workflow) that settles one question for one revision in
one environment: does the revision now running there stay, or is the way back taken? The workflow
catalog states it in brief as deployment and post-deploy verification
([W26](workflow-catalog.html#W26)); this page sets out how the call is reached, what happens when it
cannot be reached cleanly, what the run leaves behind and how a team can tell that the workflow
works.

"Healthy" is never judged in isolation. Google's Site Reliability Workbook defines canarying as "a
partial and time-limited deployment of a change in a service and its evaluation", in which the part
that receives the change, the canary, is judged against the rest, the
control[^sre-workbook-canarying]. The same chapter says it is important to "also use absolute
measures, such as defined SLOs, to ensure the system is operating correctly"[^sre-workbook-canarying].
The decision therefore rests on two readings: the revision relative to a control running at the same
time, and the service against its own objectives.

## Trigger

A run starts when a deployment of a recorded revision begins in an environment (see
[Deploy](deploy.html) for strategies and environments). Each environment is a run of its own. Google's
Site Reliability Engineering (SRE) book describes rollouts that start "in one cluster and expand
exponentially until all clusters are updated"[^sre-book-release-engineering]; as recommended practice,
each step of such a staged rollout is judged before the next one begins, so a result from the first
step is never carried silently to the last.

A configuration change deployed on its own starts a run too. The SRE book counts as a push "Any change
to a service's running software or its configuration"[^sre-book-monitoring], and the Twelve-Factor App
describes config as "everything that is likely to vary between deploys"[^twelve-factor-config].
Because the [evidence schema](evidence-schema.html#revisions-and-versions) keeps the configuration
revision apart from the change revision, a run started by configuration alone still names the code
revision it left in place.

## Inputs

The run reads what earlier work has already settled, and what it needs to compare against.

- **The release record for the same revision.** [Release readiness](release-readiness.html) settles
  it before deployment begins. The run reads that record instead of repeating its work and, as
  recommended practice, stops if the revision deployed is not the revision the record names.
- **The configuration revision** the deployment carries, recorded beside the change revision. The
  Twelve-Factor App notes that "Config varies substantially across deploys, code does
  not"[^twelve-factor-config], which is why the two are read separately.
- **The service's objectives.** The SRE book defines a service level indicator (SLI) as "a carefully
  defined quantitative measure of some aspect of the level of service that is provided" and a
  [service level objective](glossary.html#service-level-objective) (SLO) as "a target value or range of
  values for a service level that is measured by an SLI"[^deployverif-sre-book-slo]. The objectives
  supply the absolute side of the comparison.
- **The control.** In a canary, the control is the part of the service still running the previous
  revision over the same period[^sre-workbook-canarying]. Comparing the new revision with how the
  service behaved before the deployment is weaker: the workbook has a section headed "Before/After
  Evaluation Is Risky", with the example of a Monday release compared against weekend behaviour, where
  the change of day adds noise to the comparison[^sre-workbook-canarying].
- **The signals.** The SRE book's four golden signals are latency, traffic, errors and
  saturation[^sre-book-monitoring]. For canary metrics, the workbook says "We typically recommend using
  SLIs as a place to start thinking about canary metrics", asks for metrics that indicate problems and
  are representative and attributable, and keeps the set small, "perhaps no more than a dozen" in its
  own words[^sre-workbook-canarying].
- **The way back, and whether it is still open.** In blue-green deployment the router is switched
  back[^fowler-blue-green]; in a canary release users are rerouted "back to the old
  version"[^fowler-canary-release]. Fowler advises that "The trick is to separate the deployment of
  schema changes from application upgrades"[^fowler-blue-green]; where that was not done, the previous
  revision may not run on the changed schema, and the way back is closed before the run starts.

## Agent task

The agent's part in this workflow is set in its catalog row ([W26](workflow-catalog.html#W26)); this
page adds how that part is bounded. This page draws on no study of agents in deployment verification,
so what follows is recommended practice except where a source is named.

The case for an agent is volume. Once a canary is live, the signals outnumber what a person on watch
can follow, and an agent can lay out for that person where the canary and the control diverge and
which of those differences the change could plausibly explain, using the workbook's idea of an
attributable metric[^sre-workbook-canarying]. Its account enters the record as advice beside the check
results. It never settles the outcome (see [Deploy](deploy.html)).

One operator's account describes agents in its incident management that "consolidate/summarize data",
create handoff documents and draft postmortems (written records of an incident and its follow-up
actions[^incident-sre-book-postmortem]), and, separately, agents "to investigate incidents, and
in some cases to autonomously mitigate issues"[^google-agentic-sre]. It is one organisation's
description of incident work, not a study of deployment, and it reports no outcome figures. This page
recommends no autonomous agent action on production.

The agent reads the monitoring signals, the release record and the run's own record, and writes only
its account. It does not start, pause or stop a rollout, does not take the way back, and cannot mark
the deployment healthy.

## Checks

The checks are what settles health the same way on every run. Which checks the workflow runs is in the
catalog row; the points below describe how a check in this workflow is built.

### Canary against control, and against objectives

The workbook calls canarying "effectively an A/B testing process"[^sre-workbook-canarying]. A check
therefore compares the canary's metrics with the control's over the same window, and separately holds
both to the service's objectives, rather than reading the canary alone.

### Thresholds come from objectives

The SRE book calls SLIs and SLOs "crucial elements in the control loops used to manage systems", and
says that "The SLO violation rate can be compared against the error budget, with the gap used as an
input to the process that decides when to roll out new releases"[^deployverif-sre-book-slo]. As
recommended practice, each threshold a check applies is derived from an objective and stored in the
configuration revision, which the [evidence schema](evidence-schema.html#revisions-and-versions) uses
for rules and thresholds, so a later reader can see what the revision was held to.

### Attribution

A difference seen during a canary is not always caused by the change. The workbook's example is an
oversubscribed machine shared with the canary: a real problem that monitoring should catch, but not a
canary failure if the change did not cause it[^sre-workbook-canarying]. The check reports the
difference; whether the change caused it is weighed in the human decision.

### Rule IDs and result states

Each check carries the identifier of the rule it enforces, where one exists, and reports a status from
the fixed list on [Evidence schema](evidence-schema.html#check-results). A required signal that reports
nothing is `could_not_run`, never health. At least one change host documents that a job skipped by a
conditional reports "Success"[^github-status-checks], which is why the state has to exist explicitly.

### A halt is a check, not a judgement

As recommended practice, stopping on a threshold is a deterministic [gate](glossary.html#gate) that
answers the same way every run, not an agent's reading. Danilo Sato describes one such practice, the
"cluster immune system" at IMVU, which monitors business metrics and rolls a release back
automatically on a statistically significant regression[^fowler-canary-release]. Where a team automates
a halt or a rollback, the trigger is a rule with a recorded threshold, and the named person still
records the decision that follows.

## Guardrails

**Credentials.** The agent holds read access to signals and records and no write access to production
state. Least privilege applies to processes acting on behalf of users as well as to the users
themselves[^nist-800-53], and one operator's account relies on "consistent controls to prevent unwanted
mutations of production state"[^google-agentic-sre].

**The canary is bounded.** By the workbook's definition it is partial and
time-limited[^sre-workbook-canarying], and the workbook says "We strongly advise running only one
canary deployment at a time"[^sre-workbook-canarying]. As recommended practice, a run judges one
revision, and a second deployment to the same environment waits until the first is decided.

**Stop conditions.** These are recommended practice.

- *No control to compare against.* The run produces no result about the change, since canarying judges
  the canary against the control[^sre-workbook-canarying].
- *A required signal is missing.* The result is `could_not_run` and the rollout does not proceed.
- *The way back is closed*, for example because a schema change shipped with the code that needs
  it[^fowler-blue-green]. The decision is then no longer whether to roll back, and it moves to incident
  handling ([W27](workflow-catalog.html#W27)).

## Human decision

A named person decides, and the record carries that name and the reason, as recommended practice (see
[Deploy](deploy.html)). The catalog row records who holds the decision for this workflow
([W26](workflow-catalog.html#W26)). Public sources describe the work around it: the SRE book's on-call
engineer, once a page is acknowledged, "is expected to triage the problem" and "work toward its
resolution, possibly involving other team members and escalating as needed"[^sre-book-being-on-call],
and release engineers and site reliability engineers "work together to develop strategies for
canarying changes" and share "rolling back features that demonstrate
problems"[^sre-book-release-engineering]. On a bad canary the workbook's options are to "pause and roll
back the deployment, or perhaps contact a human to help troubleshoot the issue"[^sre-workbook-canarying].

**On what evidence.** The check results, the canary-against-control comparison, the reading against
objectives, and the agent's account, marked as advice.

**What the person may do.** Halt or roll back at any time on their own judgement, even when every check
has passed; proceed against the agent's account, with the reason recorded; decide whether a difference
is attributable to the change.

**What the person may not do.** Record the deployment as healthy while a required result is failed or
`could_not_run`. As recommended practice, the deployment stays unconfirmed until the result exists or
the way back is taken.

## Outputs and evidence

The run leaves the revision either confirmed in place or returned to the previous one, and an
[evidence record](glossary.html#evidence-record) in the shape the [evidence schema](evidence-schema.html)
fixes. The record names the change revision, the configuration revision and the environment, and, for a
staged rollout, the step. It lists the expected checks before their results, each result with its rule
identifier and status, the control and the window compared, the agent's account as advisory findings,
and the decision with its decider and reason. As recommended practice, it also states what kinds of
traffic the window covered, so a reader can see what the run did not observe.

Its readers:

- **The release decision**, where exposing the change to users follows deployment
  ([Release](release.html); see also [deploy versus release](glossary.html#deploy-versus-release)).
- **Incident handling and its lessons.** Incident remediation ([W27](workflow-catalog.html#W27)) and
  [Incident feedback](incident-feedback.html) start from what was running. The
  [traceability spine](traceability-spine.html) links an incident to the release that was running, and
  this record says which revision and configuration that was and what verification saw. This is the
  [evidence hand-off](glossary.html#evidence-handoff) in the downstream direction.
- **The workflow's owner**, who reads the records together to compute the measures below.
- **The next run in the same environment**, which reads the last confirmed record to know what the way
  back returns to (recommended practice).

In the customer-record export, a hypothetical feature that lets users export customer records, the
verification record for the export change names the exact revision that went out, as the
[Deploy](deploy.html) page describes.

## Failure paths

The general shape of a failure path is on [Workflows](workflows.html#failure-paths). The paths specific
to this workflow:

- **The canary does worse than the control.** The rollout pauses and the way back is taken. In a canary
  release that means to "reroute users back to the old version until you have fixed the
  problem"[^fowler-canary-release]; the workbook's words are "pause and roll
  back"[^sre-workbook-canarying]. The record keeps the failed results with the revision.
- **The control moves too.** Imperfect isolation means that "bad behavior of the canary deployment can
  also negatively impact the control", and the two can change together, so the comparison alone can
  show no difference while both are worse[^sre-workbook-canarying]. The reading against objectives then
  decides whether the service is within them. The result is recorded and not attributed to the change
  on the comparison alone.
- **No control to compare against.** As recommended practice, the run records no result about the
  change, the rollout does not proceed on it, and the named person who decides the deployment acts
  next, choosing whether a control is set up and the run repeated.
- **A required signal is missing.** The result is `could_not_run` and the rollout does not proceed. As
  recommended practice, whoever owns the monitoring is told; the gap is not a defect in the change.
- **The way back is closed.** Fixing forward or another response is decided in incident handling
  ([W27](workflow-catalog.html#W27)), not in this workflow. Fowler's advice on schema changes explains
  how it closes[^fowler-blue-green].
- **Environments differ by accident.** The Twelve-Factor App warns that "tiny incompatibilities crop
  up, causing code that worked and passed tests in development or staging to fail in
  production"[^twelve-factor-parity]. As recommended practice, a result from one environment is not
  carried to another, and the difference found is recorded.
- **The deployment stalls part-way.** As recommended practice, the record holds the partial state,
  which steps run which revision, and a named person decides whether to continue or go back.

**The method's limit.** The workbook notes that performance defects often show only under heavy load,
so a canary at a quiet time may not trigger them, and that "Some regressions may manifest only during
events not included in the artificial load, leading to gaps in coverage"[^sre-workbook-canarying]. In
the customer-record export, if the export were rolled out to a canary, the comparison would see
ordinary export requests, and a scheduled full export might not run during the canary's window at all.
Deploy verification judges the traffic that reached the canary, not what was never exercised. That is
the limit the Deploy page records: in a hypothetical production incident, a scheduled full export,
within the volume-limit rule R-017's limit but far larger than the 50k-row load scenario, times out,
and no deployment check could have caught it, because that volume was never tested.

## Measures

DORA's guide warns against setting its metrics as targets, and frames them as a way for one
application or service to improve over time rather than a way to compare teams[^dora-metrics]. Each
measure below is read against a baseline; this page sets no target or threshold.

- **Change fail rate, failed deployment recovery time and deployment rework rate**, as DORA names
  them[^dora-metrics]: "the ratio of deployments that require immediate intervention following a
  deployment"; "the time it takes to recover from a deployment that fails and requires immediate
  intervention"; and "the ratio of deployments that are unplanned but happen as a result of an
  incident in production". Baseline: the same service's values before the workflow was in use.
- **Share of runs judged with every required signal present**, with `could_not_run` results counted by
  cause. Baseline: the first deployments under the workflow, since no earlier record exists.
  Recommended practice.
- **Time from a regression appearing in the signals to a recorded decision.** DORA lists time to detect
  among its measures of monitoring[^dora-monitoring-observability]. Baseline: the same interval in
  earlier incidents, where their records allow it. Recommended practice.
- **Rollbacks that worked when used**: the share of times the way back was taken and the service
  returned to its objectives without further action. Baseline: rollbacks before the workflow.
  Recommended practice.
- **Signal quality.** DORA also lists false positives and false negatives among those
  measures[^dora-monitoring-observability]; here, halts that proved unnecessary, and deployments the run
  confirmed that later needed immediate intervention. Baseline: the first deployments under the workflow.

## Owner

The workflow has one accountable owner, as every workflow does (see [Workflows](workflows.html)), drawn
from the people who run production (see [Deploy](deploy.html)). As recommended practice, the owner
changes the required signals, how thresholds are derived from objectives and the baselines, and each
change is recorded as a new configuration revision.

## Related

- [Release readiness](release-readiness.html): settles the record this workflow reads first.
- [Incident feedback](incident-feedback.html) and incident remediation
  ([W27](workflow-catalog.html#W27)): read this workflow's record when something goes wrong later.
- [Deploy](deploy.html), [Release](release.html) and [Operate](operate.html): the phases around it;
  strategies, environments and the deploy-versus-release distinction live on Deploy.
- [Traceability spine](traceability-spine.html): the link from release to incident.
- [Workflows](workflows.html), [Evidence schema](evidence-schema.html), [Validators](validators.html)
  and [Adapters](adapters.html): the Core pages behind the checks, the record and the bindings to the
  pipeline runner and monitoring.
- Workflow catalog: deployment and post-deploy verification ([W26](workflow-catalog.html#W26)),
  release readiness ([W25](workflow-catalog.html#W25)), data change execution
  ([W16](workflow-catalog.html#W16)) and incident remediation ([W27](workflow-catalog.html#W27)).
- Terminology: [could_not_run](glossary.html#could-not-run),
  [canary release](glossary.html#canary-release) and
  [failure path](glossary.html#failure-path).

## Sources

- Canarying, its control, absolute measures, attribution and limits: Alec Warner and Štěpán Davidovič,
  *Canarying Releases*, chapter 16 of the SRE workbook[^sre-workbook-canarying].
- Objectives and error budgets: Chris Jones, John Wilkes and Niall Murphy, with Cody Smith, *Service
  Level Objectives*, chapter 4 of the SRE book[^deployverif-sre-book-slo].
- Signals, pushes, staged rollouts and on-call: chapters of the SRE book by Rob
  Ewaschuk[^sre-book-monitoring], Dinah McNutt[^sre-book-release-engineering] and Andrea
  Spadaccini[^sre-book-being-on-call].
- Rollback and schema changes: Martin Fowler[^fowler-blue-green] and Danilo
  Sato[^fowler-canary-release]; configuration and environment parity: the Twelve-Factor
  App[^twelve-factor-config][^twelve-factor-parity].
- Agents and permissions: one operator's account[^google-agentic-sre] and NIST SP
  800-53[^nist-800-53]; skipped checks: one change host's documentation[^github-status-checks].
- Measures: DORA's guide to software delivery performance metrics[^dora-metrics] and its page on
  monitoring and observability[^dora-monitoring-observability].
- Postmortems: *Postmortem Culture: Learning from Failure*, chapter 15 of the SRE
  book[^incident-sre-book-postmortem].
- Validators as computational sensors: Birgitta Böckeler on maintainability
  sensors[^bockeler-sensors].
- Statements marked recommended practice are this site's own and are not findings of any study.
