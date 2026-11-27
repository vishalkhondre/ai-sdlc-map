---
id: release-readiness
type: workflow
band: lifecycle
map_box: release readiness
title: Release readiness
summary: The workflow that decides whether a release candidate, fixed at one revision, is fit to go out, by reading the records already written for that revision rather than asking again, and leaves the release record that deployment and any later incident review start from.
key_terms: [ai-sdlc, workflow, three-roles, gate, evidence-record, evidence-handoff, could-not-run, failure-path, definition-of-done, deploy-versus-release, release-toggle, traceability-spine, export-example]
sources: [scrum-guide-2020, sre-book-release-engineering, semver, nist-ssdf, slsa-provenance, slsa-verifying, slsa-vsa, istqb-test-completion, keep-a-changelog, keep-a-changelog-2, dora-streamlining-change-approval, dora-metrics, fowler-feature-toggles]
related: [release, deploy, pull-request-verification, spec-readiness, design-conformance, deploy-verification, incident-feedback, definition-of-ready-and-done, traceability-spine, evidence-schema, workflows, rule-registry, software-factory]
review_record: content/reviews/1.6.0-lifecycle.md
---

## Decision

Release readiness is a workflow of the AI SDLC (the software development lifecycle with AI agents
doing part of the work) that settles one question: may this release candidate, at this one
revision, go out, on evidence already recorded for that revision? The workflow's definition is the
release readiness row of the workflow catalog ([W25](workflow-catalog.html#W25)). This page sets
out how a run reads its evidence, how it fails, which record it leaves and who reads that record,
and how a team can tell whether the workflow works.

Meeting the Definition of Done does not settle the question on its own. In the 2020 Scrum Guide, a
Product Backlog item that does not meet the definition "cannot be released or even presented at the
Sprint Review", and the moment an item meets it, an Increment is born[^scrum-guide-2020]. Done makes
an item eligible for release; it does not release it. The release-level definition is described
under [Definition of Done](definition-of-ready-and-done.html#definition-of-done). Release readiness
is settled for a revision before that revision's deployment begins, while exposure to users can
come with the deployment or later, as the [Deploy](deploy.html#gates-and-evidence) and
[Release](release.html) pages explain.

## Trigger

A run starts when a release candidate is named and fixed at one revision, which is the entry gate
of the [Release](release.html#gates-and-evidence) phase. Building a release from one revision has
public precedent: Google's site reliability engineering book describes branching "from the mainline
at a specific revision" and rebuilding an older release "at the same revision as the original
build"[^sre-book-release-engineering].

Any change to the candidate's contents makes a new candidate and starts a new run. Semantic
Versioning says that once a versioned package has been released, its contents "MUST NOT be
modified" and any modification "MUST be released as a new version"[^semver]. Applying the same rule
to a named candidate before it is released is this site's recommended practice, by analogy. The SRE
book also describes fixes reaching a release branch as cherry picks, each of which can be approved
or rejected for inclusion[^sre-book-release-engineering]; an accepted cherry pick changes the
contents, so it starts a new run.

## Inputs

The run reads records that other workflows wrote, each named by the revision it describes. The
inputs carry no order of their own.

- **Verification records.** One for every change in the candidate, written by
  [Pull-request verification](pull-request-verification.html). The
  [Traceability spine](traceability-spine.html) links change to release through the revisions of the
  changes the candidate contains.
- **Upstream records.** The [specification readiness](spec-readiness.html) and
  [design conformance](design-conformance.html) records those changes rest on.
- **Provenance.** SLSA defines provenance as "verifiable information about software artifacts
  describing where, when, and how something was produced"[^slsa-provenance]. NIST's Secure Software
  Development Framework asks producers to securely archive the files and supporting data, provenance
  data among them, retained for each software release, and to collect, safeguard, maintain and share
  provenance data for all components of each release (tasks PS.3.1 and PS.3.2)[^nist-ssdf].
- **The release-level Definition of Done**, as the
  [Definition of Done](definition-of-ready-and-done.html#definition-of-done) section describes it.

One rule governs every input: a record is evidence only for the revision it names. When a change
moves to a new revision, its earlier record stays attached to the earlier revision
([evidence schema](evidence-schema.html#revisions-and-versions)), and the evidence it carried
expires with that revision ([evidence hand-off](glossary.html#evidence-handoff)). A record for any
other revision is history, not input.

## Agent task

The task itself is set in the catalog row ([W25](workflow-catalog.html#W25)). Its plainest part is
drafting release notes. Keep a Changelog's 2.0.0 edition says a language model "can draft one from a
diff in seconds, which is useful as a starting point", draws the line as "machines can draft, but
humans curate", and advises: "Then read the result before anyone else does."[^keep-a-changelog-2]
The same edition says not to use a list of commits as a changelog, because a commit records a step
in the source code while a changelog entry records a notable difference written for the people who
use the software[^keep-a-changelog-2]; the 1.1.0 edition calls commit-log diffs "full of
noise"[^keep-a-changelog]. A draft also follows the changelog's own conventions: the 2.0.0
edition, for example, asks for an `Unreleased` section at the top, the release date of each version,
and a yanked release listed rather than hidden[^keep-a-changelog-2]. How the Release phase treats
such drafts is on the [Release](release.html#ai-assisted-practice) page.

What the agent writes stays a draft until a person curates it. How a workflow keeps its agent apart
from the checks and the decision is set out on the
[Workflows](workflows.html#the-three-roles-agent-checks-and-people) page.

## Checks

Each property below is one that a tool settles the same way every time, before anyone decides. The
properties carry no order. The catalog row keeps its own list of checks
([W25](workflow-catalog.html#W25)); these are the properties a team can expect a run to establish.

- **Revision match.** Every record the run reads names the candidate's revision. A record that names
  any other revision fails the property
  ([revisions and versions](evidence-schema.html#revisions-and-versions)).
- **Provenance verified, not merely present.** SLSA says "provenance doesn't do anything unless
  somebody inspects it", and calls that inspection verification. Its steps check the provenance's
  signature, that its subject matches the artefact's digest, its predicate type and the builder's
  level; then compare it with expectations such as builder identity, canonical source repository,
  build type and external parameters; and, optionally, check dependencies
  recursively[^slsa-verifying]. SLSA places verification at upload, at download or in continuous
  monitoring[^slsa-verifying]; running it before the release decision is this site's application.
  The result can be kept as a record of its own: a SLSA verification summary attestation names the
  verifier, the policy, the input attestations and a result of passed or failed, so that a consumer
  can decide about an artefact without reviewing every attestation behind it[^slsa-vsa].
- **Test completion on record.** The ISTQB glossary defines test completion as the activity that
  makes testware available for later use, leaves test environments in a satisfactory condition and
  communicates the results of testing to relevant stakeholders[^istqb-test-completion]. The property
  is that this activity's outcome is recorded for the candidate's revision.

## Guardrails

**Read, do not rerun.** The run reads records; it does not run upstream checks again. When a record
is missing or names another revision, the workflow that owns that record runs again for the
candidate's revision, and release readiness reads the new record. The SRE book offers a precedent
for a recorded result per revision: its release process re-runs the unit tests on the release branch
and creates an audit trail showing that all the tests passed[^sre-book-release-engineering]. Here
the result comes from the owning workflow, and this workflow reads it.

**Stop conditions.** As recommended practice, the run stops when the candidate's revision differs
from the revision any record names, and when a rule not open to exception shows anything but a pass;
in the running example, that is the access rule R-042. A stopped run states what it is waiting for
and leaves the decision open.

**Access to release operations.** The SRE book counts creating a new release and deploying a new
release among the operations it gates by access control[^sre-book-release-engineering]; the full
list is on the [Release](release.html#traditional-practice) page.

## Human decision

The named person who owns the decision takes it. The catalog row
([W25](workflow-catalog.html#W25)) records who that is, and the [Release](release.html#roles) page
explains why a single named decision is recommended practice. That person reads the release record,
the agent's drafts, marked as drafts, and any risk put forward for acceptance.

How heavy the approval should be is a separate question. DORA finds that change approvals "are best
implemented through peer review during the development process", that heavyweight external approval
has "a negative impact on software delivery performance", and treats segregation of duties, under
which "changes must be approved by someone other than the author", as a requirement peer review can
meet[^dora-streamlining-change-approval]. Where a release also falls under an organisation's change
control, the change control row ([W32](workflow-catalog.html#W32)) says who approves it.

In the customer-record export, the running example of this site, the record for the export change's
latest revision shows the request to exceed R-017's row limit as pending until the security owner
decides. While it is pending, the overall status cannot be positive, so the release decision waits.
A general option, not what the example records, is to ship the export as latent code behind a
release toggle: Pete Hodgson describes release toggles as allowing "incomplete and un-tested
codepaths to be shipped to production as latent code which may never be turned
on"[^fowler-feature-toggles]. Exposing the export then becomes a later release decision that reads
the same pending entry.

## Outputs and evidence

The run leaves the release record: an evidence record in the shape the
[evidence schema](evidence-schema.html) fixes, for the candidate's revision, holding the decision and
its reason. It is kept beside the archived files of the release and their provenance, which SSDF task
PS.3.1 asks producers to retain for each release[^nist-ssdf]. Public practice keeps similar records:
the SRE book's change report and test audit trail[^sre-book-release-engineering], and SLSA's
verification summary attestation as a stored verification result[^slsa-vsa].

The record has several readers, in no particular order:

- **[Deploy verification](deploy-verification.html)** reads it for the same revision before
  deployment starts ([Deploy](deploy.html#gates-and-evidence)).
- **[Incident feedback](incident-feedback.html)** and any incident review read it to learn which
  release was running, the release-to-incident link of the
  [traceability spine](traceability-spine.html). In the running example, a scheduled full export,
  within R-017's limit but far larger than the 50k-row load scenario, times out in production; the
  review starts from the release record and reads back through the records it names.
- **The traceability spine** uses it as the link from change to release.
- **Operations and response teams** use the provenance kept beside it; SSDF gives the example of
  making provenance data available to an organisation's operations and response teams to help them
  mitigate vulnerabilities[^nist-ssdf].
- **Assurance** reads release records when it audits how releases were decided, as recommended
  practice.

For people, the run also produces release notes, which a person has curated: "Changelogs are for
humans, not machines."[^keep-a-changelog][^keep-a-changelog-2] Where the project uses Semantic
Versioning, the version number follows it[^semver]; Keep a Changelog 2.0.0 says a project does not
have to use it[^keep-a-changelog-2].

## Failure paths

The general cases, each naming who acts next, are on the [Workflows](workflows.html#failure-paths)
page. Release readiness adds its own.

- **A record names an earlier revision.** The workflow that owns the record runs again for the
  candidate's revision, and the decision waits. It is the Release page's pitfall of evidence for an
  earlier revision ([Release](release.html#pitfalls)).
- **A required result is could_not_run.** The run cannot reach a positive status
  ([could_not_run](glossary.html#could-not-run)), and the owner of the missing environment or tool
  acts, not the author of the change. In the running example, if the 50k-row load scenario for the
  candidate's revision reports could_not_run because the load-test tool is missing from the runner
  image, the runner image's owner restores the tool, the scenario runs again in the owning workflow,
  and release readiness reads the new result.
- **Provenance is missing or fails verification.** The candidate is not fit to go out, and the owner
  of the build platform acts; that routing is recommended practice. SLSA says "Any unrecognized
  externalParameters SHOULD cause verification to fail", and that detecting a failure achieves little
  unless a person or an automated system acts on it[^slsa-verifying].
- **The notes draft is rejected or unread.** A person curates the notes before they are
  published[^keep-a-changelog-2]; a draft nobody has read does not go out.
- **The candidate changes after the run starts.** A new candidate needs a new run, by the Semantic
  Versioning analogy above[^semver], and the record of the abandoned run stays as history.
- **A version already out proves faulty.** Semantic Versioning's FAQ, on a release that broke its
  own compatibility promise, says to fix the problem in a new release and that "it is unacceptable to
  modify versioned releases"[^semver]. Keep a Changelog lists a yanked release, "do not hide
  it"[^keep-a-changelog-2]. A new run starts for the candidate that carries the fix, and
  [Incident feedback](incident-feedback.html) carries the lesson upstream.

## Measures

DORA advises setting a baseline for an application's current performance, applies its metrics at the
application or service level, and lists setting metrics as a goal among its pitfalls[^dora-metrics].
So each measure below is compared with a baseline for the same service, and none carries a target.

- **Change fail rate and deployment rework rate.** Two of DORA's software delivery performance
  metrics, in its instability group[^dora-metrics]. Baseline: the same service's values before the
  workflow was introduced.
- **Time from candidate named to decision recorded, and its spread.** DORA suggests measuring the
  time changes spend waiting for approval from external bodies, and, as approvals move closer to the
  work, the time spent waiting for local reviewers[^dora-streamlining-change-approval]. Baseline:
  earlier releases of the same service. Very short times can signal approval without reading, the
  rubber-stamp pitfall on the [Release](release.html#pitfalls) page.
- **Releases that needed a step outside the workflow.** DORA suggests tracking the percentage of
  changes that do or do not require a manual change to be promoted to
  production[^dora-streamlining-change-approval]. The release-level counterpart, recommended practice
  here, is the share of releases that needed a manual approval or a hand-assembled record. Baseline:
  the first releases run under the workflow.
- **Decisions that asked for evidence outside the record.** The share of decisions in which the
  decider had to ask in a message or a meeting for something the record should have held. Baseline:
  the first releases run under the workflow. Recommended practice; no public source measures it.
- **Release records that match what was deployed.** The share of release records whose revision is
  the revision deploy verification found running. Baseline: earlier releases. Recommended practice;
  a mismatch is the sign of the earlier-revision pitfall on the [Release](release.html#pitfalls)
  page.

## Owner

The workflow has one accountable owner, as every workflow does
([Workflows](workflows.html#definition)). As recommended practice, that owner decides what counts as
current for a candidate and which records a release requires, and changes the workflow when its
measures or failure paths show a gap. This is distinct from the Definition of Done. The Scrum Guide
holds the Developers "always accountable for ... Instilling quality by adhering to a Definition of
Done", and says several Scrum Teams on one product "must mutually define and comply with the same
Definition of Done"[^scrum-guide-2020]. The definition says what done means; the workflow's owner
decides how a release decision reads the evidence.

## Related

- Takes evidence from [Pull-request verification](pull-request-verification.html),
  [Specification readiness](spec-readiness.html) and
  [Design conformance](design-conformance.html).
- Hands evidence to [Deploy verification](deploy-verification.html) and
  [Incident feedback](incident-feedback.html).
- Phases: [Release](release.html), where this decision sits, and [Deploy](deploy.html), which reads
  it for the same revision.
- [Definition of Ready and Definition of Done](definition-of-ready-and-done.html#definition-of-done):
  the release-level definition this workflow reads.
- [Traceability spine](traceability-spine.html): the change-to-release and release-to-incident links
  the release record carries.
- Core: [Evidence schema](evidence-schema.html), [Workflows](workflows.html),
  [Rule registry](rule-registry.html) and [Software factory](software-factory.html).
- Workflow catalog: release readiness ([W25](workflow-catalog.html#W25)), deployment and
  post-deploy verification ([W26](workflow-catalog.html#W26)), change control
  ([W32](workflow-catalog.html#W32)) and exception handling ([W33](workflow-catalog.html#W33)).

## Sources

- Done and release: the 2020 Scrum Guide by Ken Schwaber and Jeff Sutherland[^scrum-guide-2020].
- Release engineering: Google's site reliability engineering book, chapter on release
  engineering[^sre-book-release-engineering].
- Versions and notes: Semantic Versioning[^semver] and Keep a Changelog, editions
  1.1.0[^keep-a-changelog] and 2.0.0[^keep-a-changelog-2].
- Release records and provenance: the NIST Secure Software Development Framework[^nist-ssdf] and SLSA
  on provenance[^slsa-provenance], verifying artifacts[^slsa-verifying] and verification summary
  attestations[^slsa-vsa].
- Test completion: the ISTQB glossary[^istqb-test-completion].
- Change approval and measures: DORA on streamlining change
  approval[^dora-streamlining-change-approval] and on software delivery performance
  metrics[^dora-metrics].
- Release toggles: Pete Hodgson on feature toggles[^fowler-feature-toggles].
- The stop conditions, running provenance verification at release, the routing of failed
  provenance, the handling of a run that cannot complete, the owner's remit and the last three
  measures are this site's recommended practice; no public source states them.
