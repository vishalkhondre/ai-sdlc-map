---
id: deploy
type: phase
band: lifecycle
map_box: Deploy
title: Deploy
summary: The phase that places a verified revision in an environment, confirms that it behaves there as intended and keeps a way back open, kept apart from the decision to release its behaviour to users.
key_terms: [workflow, three-roles, gate, could-not-run, evidence-record, evidence-handoff, adapter, feedback-path, export-example]
sources: [fowler-deployment-pipeline, fowler-ci, twelve-factor-parity, safe-cdp, safe-continuous-deployment, humble-farley-cd, fowler-blue-green, fowler-canary-release, sre-workbook-canarying, sre-book-release-engineering, twelve-factor-config, owasp-secrets-management, fowler-evodb, safe-release-on-demand, tw-radar-decoupling, fowler-feature-toggles, google-agentic-sre, nist-800-53, github-status-checks, bockeler-harness, bockeler-sensors, cockburn-hexagonal]
related: [release, design, develop-build-qa, operate, workflows, evidence-schema, validators, adapters, software-factory]
review_record: content/reviews/1.5.0-lifecycle.md
---

## Purpose

In the AI SDLC (the software development lifecycle with AI agents doing part of the work), Deploy
is the phase in which a revision that has already passed verification is placed in an environment
and observed there. It answers whether that revision, running with its configuration in that
environment, behaves as intended, and it keeps a way back open until the answer is settled. It
produces a running revision and an evidence record of which revision went where, under which
configuration, and what was seen afterwards.

Deploying is not releasing. A revision can run in production while its new behaviour is still
hidden from users; exposing it is a separate decision, taken in [Release](release.html). The
paragraph "Deploying versus releasing" below sets out the distinction.

## Traditional practice

**Environments.** A deployment pipeline breaks the build into stages, each giving more confidence,
usually at the cost of extra time[^fowler-deployment-pipeline]. Continuous integration practice
includes testing in a clone of the production environment[^fowler-ci], and the Twelve-Factor App
asks teams to keep development, staging and production as similar as
possible[^twelve-factor-parity]. The Scaled Agile Framework (SAFe) treats continuous deployment as
one aspect of its Continuous Delivery Pipeline[^safe-cdp], one that "automates the migration of new
functionality from a staging environment to production, where it is made available for release",
with four activities: Deploy, Verify, Monitor and Respond[^safe-continuous-deployment]. Jez Humble
and David Farley's book *Continuous Delivery* (2010) has a chapter titled "Deploying and Releasing
Applications"[^humble-farley-cd].

**Strategies.** Three strategies have widely cited public descriptions.

- *Blue-green deployment.* Two production environments are kept as identical as possible, one of
  them live at any time; the router is switched to the other, and the way back is to switch it
  back[^fowler-blue-green].
- *Canary release.* The change goes to a small subset of users before the entire infrastructure,
  and the way back is to reroute users to the old version[^fowler-canary-release]. Google's Site
  Reliability Workbook defines canarying as "a partial and time-limited deployment of a change in a
  service and its evaluation", in which the part receiving the change, the canary, is judged against
  the rest, the control[^sre-workbook-canarying].
- *Staged rollout across clusters.* Google's Site Reliability Engineering book describes rollouts
  "to successive clusters over a period of several hours", or that start "in one cluster and expand
  exponentially until all clusters are updated"[^sre-book-release-engineering].

The strategy is chosen when the change is designed (see [Design](design.html)); Deploy carries it
out.

**Rollback.** The same SRE chapter describes release engineers and site reliability engineers
working together on canarying changes, on pushing out releases without interrupting services and on
taking back features that show problems[^sre-book-release-engineering]. As recommended practice, the
way back is exercised before it is needed.

**Configuration and secrets.** The Twelve-Factor App calls for "strict separation of config from
code", notes that "Config varies substantially across deploys, code does not", and stores config in
the environment, including credentials and per-deploy values such as the canonical
hostname[^twelve-factor-config]. The OWASP Secrets Management Cheat Sheet says organisations need to
centralise the storage, provisioning, auditing, rotation and management of secrets, under least
privilege[^owasp-secrets-management]. As recommended practice, a deployment records the
configuration it ran with beside the code revision, as the [evidence schema](evidence-schema.html)
keeps a configuration revision apart from the change revision.

**Data changes.** Martin Fowler advises that "The trick is to separate the deployment of schema
changes from application upgrades"[^fowler-blue-green], and evolutionary database design keeps every
database change as a migration script version controlled with the application code[^fowler-evodb].
Running a migration is its own decision, in the [Data change execution](workflow-catalog.html#W16)
workflow.

**Deploying versus releasing.** Several public sources separate the two words. SAFe says continuous
deployment makes functionality "available for release" and that "it's optimal to separate the
deployment process from releasing"[^safe-continuous-deployment]; in its release on demand, "releases
are decoupled from the work to deploy the functionality"[^safe-release-on-demand]. The Thoughtworks
Technology Radar placed "Decoupling deployment from release" in its Adopt ring in November 2015 and
April 2016; the entry is not on the current edition. The April 2016 entry recommends "strictly using
the term Deployment when referring to the act of deploying a change to application components or
infrastructure", says "The term Release should be used when a feature change is released to end
users, with a business impact", and notes that feature toggles and dark launches let teams deploy
more often without releasing features[^tw-radar-decoupling]. Pete Hodgson's article on feature
toggles on martinfowler.com, dated 9 October 2017, calls release toggles "the most common way to
implement the Continuous Delivery principle of 'separating [feature] release from [code]
deployment.'"[^fowler-feature-toggles] This page makes no claim about who drew the distinction
first. This site's reading: deployment is the act of putting a revision into an environment, and
release is exposing its behaviour to users. The two coincide unless a toggle, a canary or a staged
rollout separates them.

## AI-assisted practice

No public study measures agents in deployment, so this section is recommended practice except where
a source is named. The phase keeps the three roles every workflow uses: an agent prepares,
deterministic checks settle what must not be wrong, and a person decides (see
[Workflows](workflows.html)).

**What moves to an agent.** Once a revision runs, the signals multiply: health endpoints, error and
latency measures, logs, and the difference between canary and control. An agent can read more of
them than a person on watch and set out what changed, as input to a decision, not a verdict. Its
task in this phase's workflow is set in the [catalog row](workflow-catalog.html#W26).

**What moves to a deterministic check.** Whatever must not be wrong goes to a deterministic gate,
a tool that answers the same way every run: that the running revision is the one verified, that
the configuration in use is the one recorded, and that the signals the strategy depends on are
reporting at all. SAFe lists
Verify as the activity after Deploy[^safe-continuous-deployment]. A required check that produced no
result is `could_not_run`, a result of its own, never read as healthy (see
[Validators](validators.html)[^bockeler-sensors]).

**What stays with a person.** Whether to proceed or roll back stays with a named person, recorded
under that name; exposing the change to users belongs to [Release](release.html). One operator's
account of agentic AI in its site reliability work says it relies on "having consistent controls to
prevent unwanted mutations of production state", and that an agentic approach "does not necessarily
imply removing people from the process, specifically for higher-risk services and
features"[^google-agentic-sre]. It is one organisation's description, not a study, and reports no
figures.

## Workflows in this phase

The workflow catalog files these under its phase 6, "Release", which groups deployment with release
readiness. Each catalog row holds the workflow's own definition; this page names and links them
only.

- [Deployment and post-deploy verification](workflow-catalog.html#W26): the workflow that decides
  here.
- [Release readiness](workflow-catalog.html#W25): settled for the same revision before deployment.
- [Data change execution](workflow-catalog.html#W16): schema migrations, apart from the application.
- [Incident remediation](workflow-catalog.html#W27): problems that surface after this phase.

## Gates and evidence

**Entry.** The revision's evidence is current: the record names the exact revision, and a new
revision needs a new record (see [Workflows](workflows.html) and
[Evidence schema](evidence-schema.html)). Release readiness is settled for that revision, its
configuration is recorded, the strategy is the one chosen at design, and its way back is known. As
recommended practice, a deployment missing any of these does not start and states what it is
waiting for.

**Exit.** Either the revision is confirmed healthy and the decision to proceed is recorded, or it is
rolled back and the reason recorded. With a canary, "healthy" means judged against the
control[^sre-workbook-canarying]. A `could_not_run` result is not a pass, and the exit stays closed
while it stands; what it means for the decision is set in the assurance band of the map.

**Order with release.** The map draws Deploy before Release. Release readiness reads the evidence
before deployment begins; exposing the change to users can come with deployment or after it,
whenever a toggle, a canary or a staged rollout keeps the two apart (see [Release](release.html)).

**Evidence.** The phase leaves an evidence record naming the revision, environment and
configuration, with each check's result and the person's decision; the next decision reads that
record, the evidence hand-off described on [Workflows](workflows.html). In the customer-record
export, a hypothetical feature that lets users export customer records, the verification record for
the export change is what release readiness reads, and it names the exact revision. The example
also marks this phase's limit: in a hypothetical production incident, a scheduled full export,
within R-017's volume limit but far larger than the 50k-row load scenario, times out. No deployment
check could have caught it, because that volume was never tested. The incident, and the lesson it
sends upstream along the feedback path, the site's name for what Birgitta Böckeler calls the
steering loop[^bockeler-harness], belong to [Operate](operate.html).

## Roles

Public sources name few accountabilities here, so this section keeps to titles, which differ
between organisations. The SRE book has release engineers and site reliability engineers sharing
canarying, releases and taking back faulty features[^sre-book-release-engineering].

- **The people who run production** carry out the deployment and its way back.
- **One accountable owner** holds the deployment workflow, as every workflow has one (see
  [Workflows](workflows.html)).
- **A named person** decides whether to proceed or roll back (see the
  [catalog row](workflow-catalog.html#W26)); exposure to users sits with [Release](release.html).

## Pitfalls

- **"Deployed" read as "released".** New behaviour reaches users before anyone decided to expose it,
  though SAFe and the Radar keep the two apart[^safe-continuous-deployment][^tw-radar-decoupling].
  Sign: users meet a feature before any release decision exists.
- **A schema change shipped with the application that needs it.** Fowler advises separating the
  two[^fowler-blue-green]; shipped together, the old revision may not run on the new schema, and
  the way back closes. Sign: the only way back on record is a restore.
- **Configuration in the code, or different by accident.** Per-environment values are built in, or
  environments drift apart[^twelve-factor-config][^twelve-factor-parity]. Sign: a change passes in
  staging and fails in production with no code difference.
- **A canary with nothing to compare against.** Canarying judges the canary against a
  control[^sre-workbook-canarying]; read alone, a service-wide problem looks like a result about the
  change. Sign: the record holds no control measures.
- **A missing health check read as healthy.** At least one change host reports a job skipped by a
  condition as successful[^github-status-checks], so silence passes for success unless
  `could_not_run` is its own state. Sign: fewer results than expected checks, and a positive status.
- **A way back never exercised.** Its first run is during a failure. Sign: no record of it having
  run for this kind of change.
- **An agent with standing write access to production.** A wrong reading becomes a wrong action.
  Least privilege covers processes acting for users[^nist-800-53], and one operator's account
  stresses controls against unwanted mutations of production state[^google-agentic-sre]. Sign: the
  agent's credential holds rights nobody granted for this deployment.
- **Release toggles left in place.** Hodgson describes teams that "view their Feature Toggles as
  inventory which comes with a carrying cost" and says release toggles "should generally not stick
  around much longer than a week or two"[^fowler-feature-toggles]. Sign: toggles unchanged long
  after the feature was exposed.

## Related

- [Design](design.html), [Develop, build and QA](develop-build-qa.html), [Release](release.html)
  and [Operate](operate.html): the neighbouring phases.
- [Workflows](workflows.html), [Evidence schema](evidence-schema.html),
  [Validators](validators.html), [Adapters](adapters.html)[^cockburn-hexagonal] and
  [Software factory](software-factory.html): the Core pages this phase draws on.
- Workflow catalog: [Deployment and post-deploy verification](workflow-catalog.html#W26),
  [Release readiness](workflow-catalog.html#W25),
  [Data change execution](workflow-catalog.html#W16) and
  [Incident remediation](workflow-catalog.html#W27).
- Terminology: [could_not_run](glossary.html#could-not-run) and
  [feedback path](glossary.html#feedback-path).

## Sources

Environments follow Martin Fowler[^fowler-deployment-pipeline][^fowler-ci], the Twelve-Factor
App[^twelve-factor-parity] and SAFe[^safe-cdp][^safe-continuous-deployment]. Strategies and
rollback draw on Fowler[^fowler-blue-green], Danilo Sato[^fowler-canary-release] and Google's SRE
workbook and book[^sre-workbook-canarying][^sre-book-release-engineering]; configuration, secrets
and data on the Twelve-Factor App[^twelve-factor-config], OWASP[^owasp-secrets-management] and
Pramod Sadalage and Fowler[^fowler-evodb]. Deploying versus releasing cites
SAFe[^safe-release-on-demand], the Thoughtworks Radar[^tw-radar-decoupling], Pete
Hodgson[^fowler-feature-toggles] and, for a chapter title only, Humble and
Farley[^humble-farley-cd]. Agents and permissions cite one operator's account[^google-agentic-sre]
and NIST[^nist-800-53]; skipped checks, one change host's documentation[^github-status-checks]; the
steering loop, Birgitta Böckeler[^bockeler-harness]. Statements marked recommended practice are
this site's own, not findings of any study.
