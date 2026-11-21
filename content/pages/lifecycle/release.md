---
id: release
type: phase
band: lifecycle
map_box: Release
title: Release
summary: Release decides whether a candidate is fit to reach its users, on evidence recorded for its exact revision, and leaves a record of that decision; an agent prepares, checks confirm and a named person decides.
key_terms: [ai-sdlc, workflow, three-roles, gate, evidence-record, evidence-handoff, could-not-run, failure-path, export-example]
sources: [sre-book-release-engineering, dora-streamlining-change-approval, keep-a-changelog, keep-a-changelog-2, semver, fowler-feature-toggles, fowler-dark-launching, safe-release-on-demand, dora-continuous-delivery, scrum-guide-2020, nist-ssdf, slsa-provenance, istqb-test-completion, dora-2025-announcement, bockeler-sensors]
related: [deploy, operate, design, definition-of-ready-and-done, traceability-spine, workflows, evidence-schema, validators, software-factory, rule-registry]
review_record: content/reviews/1.5.0-lifecycle.md
---

## Purpose

Release is the phase of the AI SDLC (the software development lifecycle with AI agents doing part
of the work) in which a team decides that a change is fit to reach its users, and records that
decision. The question has two parts. First, does the evidence gathered for this candidate, at its
exact revision, support letting it go? Second, where exposing a change to users is a separate act
from deploying it, is the deployed change now to be switched on for them? The evidence check comes
first and precedes deployment; the decision to expose can coincide with deployment or follow it.
Deploying puts a change into a production environment and releasing makes it available to users;
the two can happen at the same moment or apart, and the [Deploy](deploy.html) page sets out the
distinction with its sources.

The phase produces a record of the release decision that later work can read. Its exit is also
where the release-level [Definition of Done](definition-of-ready-and-done.html#definition-of-done)
is met, which is why the map's DoD tag sits on the Release box.

## Traditional practice

Without agents, release is a controlled step. Google's site reliability engineering book, in its
chapter on release engineering, enforces policy through gated operations, among them approving
source code changes, specifying the actions to perform during a release, creating a new release,
approving the initial integration proposal and subsequent cherry picks, deploying a new release,
and changing a project's build configuration[^sre-book-release-engineering]. The same chapter asks
for hermetic builds: the same revision built on different machines gives identical results,
because a build depends on known versions of its tools and dependencies, and that makes a release
reproducible[^sre-book-release-engineering].

Who approves, and how, varies more. DORA's capability guidance holds that change approvals are
"best implemented through peer review during the development process, supplemented by automation
to detect, prevent, and correct bad changes early", and that heavyweight external approval
processes have "a negative impact on software delivery performance"[^dora-streamlining-change-approval].
The same page names segregation of duties as a common regulatory requirement, treats peer review as
a way to meet it, and keeps a strategic role for the change advisory
board[^dora-streamlining-change-approval].

Release notes tell people what changed. Keep a Changelog, created and maintained by Olivier Lacan,
starts from one principle, "Changelogs are for humans, not machines.", advises against dumping
git logs into a changelog, says there should be an entry for every single version, and groups
changes under six types: Added, Changed, Deprecated, Removed, Fixed and Security[^keep-a-changelog].
It asks a project to mention whether it follows Semantic Versioning rather than requiring
it[^keep-a-changelog]. Under Semantic Versioning, the major version changes when a release makes
incompatible API changes[^semver]. Writing down the known risks a release carries is recommended
practice; no public source read for this page prescribes a form for it.

Exposure can be controlled apart from deployment. Pete Hodgson's article on feature toggles
distinguishes release, experiment, ops and permissioning toggles by how long each lives, and says
release toggles allow "incomplete and un-tested codepaths to be shipped to production as latent
code which may never be turned on"[^fowler-feature-toggles]. Martin Fowler describes dark launching
as "taking a new or changed back-end behavior and calling it from existing users without the users
being able to tell it's being called", and notes that the term has been subject to semantic
diffusion[^fowler-dark-launching]. Canary releases, which expose a change to a small share first,
are covered on the [Deploy](deploy.html) page. In SAFe, release on demand "releases new
functionality immediately or incrementally based on business and customer
needs"[^safe-release-on-demand]. DORA treats the ability behind all of this as a capability:
continuous delivery is "the ability to release changes of all kinds on demand quickly, safely, and
sustainably"[^dora-continuous-delivery].

The Definition of Done, the quality standard an Increment must meet in the 2020 Scrum Guide by Ken
Schwaber and Jeff Sutherland, decides what may be released at all: a Product Backlog item that does
not meet it "cannot be released or even presented at the Sprint Review"[^scrum-guide-2020]. The
Guide also says the Sprint Review "should never be considered a gate to releasing value", and that
where an organisation sets a Definition of Done as a standard, all Scrum Teams follow it as a
minimum[^scrum-guide-2020].

Supply-chain practice adds records of the release itself. NIST's Secure Software Development
Framework asks producers to securely archive the files of each release and to collect, safeguard,
maintain and share its provenance data (practices PS.3.1 and PS.3.2)[^nist-ssdf]. SLSA defines
provenance as "verifiable information about software artifacts describing where, when, and how
something was produced"[^slsa-provenance]. Testing closes here too: the ISTQB glossary defines test
completion, also called test closure, as the activity that makes testware available for later use,
leaves test environments in a satisfactory condition and communicates the results of testing to
relevant stakeholders[^istqb-test-completion]. The catalog row for
[release readiness](workflow-catalog.html#W25) lists the other traditional activities it takes in.

## AI-assisted practice

With coding agents, release keeps its purpose and changes who does the legwork. The work splits the
way it does across this site: an agent prepares, deterministic checks confirm, and a person decides.
What follows is recommended practice; no public study measures it.

An agent suits the high-volume part of release work, where a first attempt is cheap to correct. It
can read the records that each change in the candidate left behind and turn them into a first
version of the release notes and of the statement of known risks; where a record it expects is
absent, it reports the gap instead of filling it. Keep a Changelog's 2.0.0 edition, which still
holds that changelogs are for humans, accepts that a model can draft a changelog from a diff and
draws the line as "machines can draft, but humans curate"; it advises reading a model-drafted
changelog before anyone else does[^keep-a-changelog-2].

Checks take what a tool can decide reliably. The central one is mechanical: every record the
release decision depends on exists and names the candidate's exact revision. The decision then reads
evidence rather than asking around, the evidence hand-off described on the
[Workflows](workflows.html) page. A result for an earlier revision says nothing reliable about the
code as it is now, so a new revision needs new records. The catalog row for release readiness lists
the further checks that run before the decision.

Everything an agent prepares at release is material for the decision, never part of it. The agent
cannot approve the candidate or waive a control the organisation requires, and it never fills a
decision field in the evidence record, the same line the [Software factory](software-factory.html)
page draws across every workflow. The decision stays with a named person, and the
[release readiness](workflow-catalog.html#W25) catalog row records who that is and which
organisational controls stay in force beside it; this split is recommended practice, not a measured
finding.

The stakes rise with volume. DORA's 2025 research puts it this way: "Without robust control systems, like
strong automated testing, mature version control practices, and fast feedback loops, an increase in
change volume leads to instability"[^dora-2025-announcement]. The record of a release decision is
where a reader can see whether those controls ran for the candidate; that reading is recommended
practice, not a DORA finding.

In the running example, the customer-record export, the release decision reads the verification
record for the export change's latest revision instead of asking again which checks ran. A request
to exceed R-017's row limit appears there as pending until the security owner decides, and R-042,
an access rule, is not open to exception.

## Workflows in this phase

Release holds one decision workflow and borders another. In the
[workflow catalog](workflow-catalog.html), whose phase names differ from the map's, both sit in the
phase the catalog calls Release; two cross-lifecycle rows also reach into it.

- [Release readiness](workflow-catalog.html#W25): the decision this phase exists to make.
- [Deployment and post-deploy verification](workflow-catalog.html#W26): the neighbouring decision,
  covered on the [Deploy](deploy.html) page.
- [Change control](workflow-catalog.html#W32): a cross-lifecycle row that a release can fall under.
- [Exception handling](workflow-catalog.html#W33): a cross-lifecycle row; a waiver sought at
  release goes through it.

Each catalog row carries its workflow's own definition, and this page does not repeat it. The
records these workflows leave follow the [evidence schema](evidence-schema.html), and the way one
workflow reads another's records is set out on the [Workflows](workflows.html) page.

## Gates and evidence

Release has one gate at entry and one at exit, and it leaves one record.

**Entry.** A named candidate, fixed at one revision. Everything the phase examines is tied to that
revision. If the candidate changes, the records gathered for the earlier revision stay as history
and new ones are needed, because evidence carries its scope and expires when the revision changes,
as the [Workflows](workflows.html) page explains.

**Exit.** Every required check for that revision has an explicit pass, the person who owns the
decision has made it, and any organisational control in force is satisfied. The exit is also where
the release-level Definition of Done is met; the DoD tag on the map marks it, and what the
definition contains and who owns it are set out under
[Definition of Done](definition-of-ready-and-done.html#definition-of-done). A required check that
could not run is shown as a state of its own and prevents a positive status, as the
[Validators](validators.html)[^bockeler-sensors] page describes; what that state means for a release is set in the
assurance band. Each kind of interruption, from a failed check to a requested exception, has its own
failure path.

**Evidence.** The exit leaves the release record, an evidence record in the shape the
[evidence schema](evidence-schema.html) fixes, kept beside the archived release files and their
provenance. Its value shows later, because an incident review starts from it. In the running
example, a scheduled full export within R-017's limit but far larger than the 50k-row load scenario
times out in production; the review that follows reads back through these records, and the
[Operate](operate.html) page carries the incident from there.

## Roles

Release has one decision owner. This page calls that person the release owner: the named person
whose decision the record carries, who reads the evidence and the agent's drafts and decides. That
single named decision is recommended practice; the catalog row for release readiness records who
holds it.

Public sources set out narrower accountabilities. The Scrum Guide holds Developers "always
accountable for ... Instilling quality by adhering to a Definition of Done"[^scrum-guide-2020], so
meeting the definition is their work before it is anyone's decision. DORA recommends
implementing change approval through peer review during development, supplemented by automation,
and keeps a strategic role for
the change advisory board[^dora-streamlining-change-approval]. Where an operating model names a
board or a designated approver for production change, that party acts through change control. This
page does not split the release decision further than those sources do.

The agent holds no role in the decision. It prepares material, its findings are advisory, and the
identity it runs under has no permission to write a decision.

## Pitfalls

- **Evidence for an earlier revision.** The candidate moved on, but the decision reads results
  recorded for a previous revision. Sign: the revision named in the release record does not match
  the candidate that shipped.
- **Release notes generated from the commit log.** Keep a Changelog advises against dumping git logs
  into a changelog[^keep-a-changelog]. Sign: notes that list commit messages instead of what changed
  for the reader.
- **Agent drafts accepted unread.** Notes or a risk statement written by an agent go out without a
  person reading them, the same failure as treating an agent's review as approval. Keep a
  Changelog's 2.0.0 edition advises reading a model-drafted changelog before anyone else
  does[^keep-a-changelog-2]. Sign: notes published minutes after the draft, with no edits.
- **Release toggles that stay.** Hodgson describes toggles as "inventory which comes with a carrying
  cost", asks teams to be proactive in removing flags that are no longer needed, and says release
  toggles "should generally not stick around much longer than a week or two", while allowing that a
  small number of long-lived kill switches remain[^fowler-feature-toggles]. Sign: release toggles older than
  the releases they were added for.
- **Approval that is either a rubber stamp or a heavyweight outside gate.** DORA finds heavyweight
  external approval harms delivery performance[^dora-streamlining-change-approval]; an approval
  given without reading the evidence fails the other way. Sign: approvals that arrive in seconds, or
  releases that wait days for a meeting.
- **The Definition of Done waived under time pressure.** An item that does not meet the definition
  cannot be released, and an organisational standard is a minimum for every
  team[^scrum-guide-2020]. A departure is an exception with an owner, a reason and an expiry, and a
  rule such as R-042 that is not open to exception is never waived. Sign: "done except for" in the
  release discussion.
- **The Sprint Review used as the release gate.** The Scrum Guide says the Sprint Review should never
  be considered a gate to releasing value[^scrum-guide-2020]. Sign: finished increments held back
  until the end of the Sprint for no other reason.

## Related

- [Deploy](deploy.html): the phase before exposure, and the difference between deploying and
  releasing.
- [Operate](operate.html): the phase after release, where incidents are handled.
- [Design](design.html): an earlier phase in the lifecycle band.
- [Definition of Ready and Definition of Done](definition-of-ready-and-done.html#definition-of-done):
  what the DoD tag at this phase stands for.
- [Traceability spine](traceability-spine.html): the chain of linked artefacts that runs from
  requirement to incident.
- [Workflows](workflows.html), [Evidence schema](evidence-schema.html),
  [Validators](validators.html), [Rule registry](rule-registry.html) and
  [Software factory](software-factory.html): the Core pages behind the records this phase reads.
- Workflow catalog rows: [release readiness](workflow-catalog.html#W25),
  [deployment and post-deploy verification](workflow-catalog.html#W26),
  [change control](workflow-catalog.html#W32) and [exception handling](workflow-catalog.html#W33).

## Sources

- Release engineering and change approval: Google's site reliability engineering book on release
  engineering[^sre-book-release-engineering] and DORA on streamlining change
  approval[^dora-streamlining-change-approval] and continuous delivery[^dora-continuous-delivery].
- Release notes and versions: Keep a Changelog, editions 1.1.0[^keep-a-changelog] and
  2.0.0[^keep-a-changelog-2], and Semantic Versioning[^semver].
- Exposure control: Pete Hodgson on feature toggles[^fowler-feature-toggles], Martin Fowler on dark
  launching[^fowler-dark-launching] and SAFe on release on demand[^safe-release-on-demand].
- Definition of Done and the Sprint Review: the 2020 Scrum Guide[^scrum-guide-2020].
- Release records and test closure: the NIST Secure Software Development Framework[^nist-ssdf], SLSA
  provenance[^slsa-provenance] and the ISTQB glossary[^istqb-test-completion].
- AI-assisted delivery: DORA's announcement of its 2025 report[^dora-2025-announcement].
- The agent's preparatory role, the single named release decision, the known-risks statement and
  the reading of the release record as evidence that controls ran are this site's recommended
  practice; no public source states them.
