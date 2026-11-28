---
id: check-results-and-decisions
type: concept
band: assurance
map_box: passed · failed · skipped · could_not_run
title: Check results and decisions
summary: What passed, failed, skipped and could_not_run are worth to whoever decides whether a revision may merge or a candidate may be released, why only an explicit pass counts in favour, what a risk tier does and does not change, and how an exception sits beside the result it departs from.
key_terms: [ai-sdlc, could-not-run, evidence-record, rule-registry, risk-tier, export-example]
sources: [sarif-2-1-0, github-protected-branches, github-status-checks, fowler-ci, nist-800-53, in-toto-attestation, slsa-verifying, nist-ssdf, istqb-rbt, owasp-asvs]
related: [validators, engineering-kit, evidence-schema, rule-registry, workflows, adapters, pull-request-verification, release-readiness, release, evidence-record, change-controls-and-standards]
review_record: content/reviews/1.7.0-assurance.md
---

## Definition

In an AI SDLC (the software development lifecycle with AI agents doing part of the work), every
check on a change ends in one of four results: passed, failed, skipped or could_not_run. How a check
reaches each one is set out under [how a check reports its result](validators.html#reporting-the-result)
and in the [Engineering Kit](engineering-kit.html#the-could_not_run-result). This page covers the
other side: what each result is worth to the person, or the derived status, that decides whether a
revision may merge or a release candidate may go out. Read for a decision, passed is the only result
that shows a rule held, and failed shows that it did not. Skipped is a declared claim that the rule
does not bear on this change, which a decider may accept or question but never count in favour.
could_not_run tells the decider nothing about the change at all. The name
[could_not_run](glossary.html#could-not-run) is coined by this site. SARIF, the OASIS format for
analysis results, has public relatives: result kinds for a pass, a failure and a rule that does not
apply, and a separate record of whether the tool itself ran.[^sarif-2-1-0]

## Why it matters

A decision that reads a missing verdict as a pass lets through the very change the check was there
to stop. Change hosts do not always prevent it. At least one change host accepts a required status
check reported as skipped as satisfying its branch protection,[^github-protected-branches] and its
documentation notes that a job skipped by a condition reports success.[^github-status-checks] A green
mark on the change host is therefore not, on its own, evidence that a rule held, and what each result
means has to be settled where the decision is taken.

Public practice treats an incomplete result set as incomplete. SARIF warns that when a tool reports a
failure of its own execution, a consumer cannot assume the run's results are complete.[^sarif-2-1-0]
Martin Fowler's account of continuous integration holds that any single failing test is enough to
fail the build,[^fowler-ci] so a mostly passing set is not a pass. Control catalogues go further and
treat a failure of the evidence process as an event in its own right: NIST SP 800-53 control AU-5 asks
an organisation to alert defined personnel or roles within a defined period when audit logging fails,
and to take further actions it defines.[^nist-800-53] AU-5 concerns audit logging, not delivery
checks, but the parallel holds: a check that could not run is a fault in producing evidence, and it
needs a response of its own.

The record outlives the decision. Release, incident review and audit all read it later
([Evidence record](evidence-record.html)), and each assumes a check stood behind every positive
decision. A decision taken without the evidence it expected has to show that it was, or every later
reader is misled; this is recommended practice.

## How it works

### Passed: only an explicit pass counts

The decider starts from the list of checks the record expected, which was fixed before any result
arrived ([expected checks](evidence-schema.html#expected-checks-before-results)), and asks of each
required check whether its result on this revision is passed
([check results](evidence-schema.html#check-results)). The site's published line is that only an
explicit pass counts as a pass ([Workflows](workflows.html#failure-paths)). Public frameworks take the
same stance. in-toto asks that policies be monotonic, so that ignoring a piece of evidence
can never turn a deny into an allow.[^in-toto-attestation] SLSA has verifiers compare provenance with
expectations set in advance, and says that unrecognised external parameters should cause verification
to fail.[^slsa-verifying] NIST's Secure Software Development Framework asks for criteria for security
checks to be defined and tracked, and gives as examples recording approvals, rejections and exception
requests (task PO.4.1).[^nist-ssdf] The overall status that sums up a record is derived by the kit
([overall status](evidence-schema.html#overall-status)); this page adds no status of its own.

### Failed

A failed required check means the rule did not hold on the revision examined. A reviewer's approval
does not stand in for it, as [Pull-request verification](pull-request-verification.html#human-decision)
sets out.

### Skipped

A skip is evidence neither for nor against the change. The decider relies on the declared condition
that made the rule inapplicable being right, which is why the expected list is fixed before results
arrive. SARIF's `notApplicable` kind marks the same case: the rule was not evaluated because it does
not apply.[^sarif-2-1-0] As recommended practice, a decider who believes a skipped rule should have
applied raises it against the project configuration that produced the expected list, not against the
result, which correctly reports what that configuration declared.

### could_not_run

could_not_run means the rule applies and nothing was established. Like a failure, it keeps the record
from reaching a positive overall status ([check results](evidence-schema.html#check-results)).

### What a risk tier changes

A [risk tier](glossary.html#risk-tier) changes which checks are expected for a change and which of
them must pass before it merges. It does not change what a result means once it is reported: a
could_not_run establishes nothing at any tier, and a pass is the same evidence at any tier. This
principle is recommended practice. Public sources place risk in the choice of what to verify. The
ISTQB glossary defines risk-based testing as basing the selection, prioritisation and use of test
activities and resources on risk types and risk levels,[^istqb-rbt] and the OWASP Application
Security Verification Standard leaves the choice of verification level to an organisation's own
analysis of its risks.[^owasp-asvs]

### Departures from a rule

An exception changes the decision; it leaves the result as reported. The record keeps the failed or
could_not_run result, and the exception is a separate decision recorded beside it.
There is no fifth result for a departure. SARIF follows the same pattern: a suppression is a property
of the result it applies to, so the result stays in the log with the suppression recorded beside it,
including its review status (accepted, under review or rejected) and a
justification.[^sarif-2-1-0] NIST SP 800-53 asks organisations to identify, document and approve
deviations from established configuration settings (CM-6c), and to document configuration change
decisions (CM-3c).[^nist-800-53]

The registry logs each exception against the rule it departs from
([Rule registry](rule-registry.html#entering-changing-and-retiring-rules)), and the workflow that
handles the request is [W33](workflow-catalog.html#W33). Whether a rule is open to exception at all is
a property of that rule's own entry. Who may grant an exception is a question of decision rights,
which belongs to the operating model rather than to the record.

### Merge and release

The same reading applies to both decisions. A release decision reads the records for the candidate's
revision only ([Release readiness](release-readiness.html#inputs)), because a record is evidence for
the revision it names ([valid for one revision](evidence-record.html#valid-for-one-revision)). The
conditions on which a release run stops are on
[Release readiness](release-readiness.html#guardrails).

### The customer-record export

The customer-record export is this site's running example, a hypothetical feature that lets users
export customer records; it counts here as one change. The record of its first pull-request run, for
revision `3f9c2e1`, shows the access rule R-042 failed on a background worker's broader query, the
volume-limit rule R-017 returned could_not_run because the load-test tool is missing from the runner
image, and a request to exceed R-017's row limit pending with the security owner
([Evidence schema](evidence-schema.html#the-customer-record-export)).

Read result by result for the merge decision: R-042 failed, so no approval can stand in for it, and
its registry entry admits no exception
([Rule registry](rule-registry.html#entering-changing-and-retiring-rules)); the change has to go back.
R-017 could_not_run, so nothing is known about how the change behaves at volume, and the decision on
that rule waits until the check runs with the tool restored. The pending request concerns R-017's
limit, not its check. Whatever the security owner decides, that decision would not turn the missing
result into a pass.

## Where it sits on the map

The page covers the bullet "passed · failed · skipped · could_not_run" in the Evidence & traceability
column of the assurance band, beside the bullets for the record itself and its validity for one
revision ([Evidence record](evidence-record.html)). The core band produces the results: the
[Engineering Kit](engineering-kit.html) defines them, its checks report them
([how a check reports](validators.html)), [Adapters](adapters.html) carry them to the change host, and
the [Evidence schema](evidence-schema.html) records them. The lifecycle band takes the decisions that
read them, chiefly [Pull-request verification](pull-request-verification.html) and
[Release readiness](release-readiness.html). Change approval under an external control framework is
on [Change controls and standards](change-controls-and-standards.html).

## Pitfalls

The pitfalls of how results are produced and recorded are on
[the page on deterministic checks](validators.html#pitfalls), [Evidence schema](evidence-schema.html#pitfalls) and
[Workflows](workflows.html#pitfalls). These concern the decision.

- **Approval in place of a pass.** A reviewer approves a change whose required check failed, and the
  change merges (recommended practice). Sign: a merged change whose record shows a required failure
  and no exception decision.
- **An exception recorded by altering the result.** The departure is made by changing the failure
  rather than by adding a decision beside it, the opposite of SARIF's suppressions.[^sarif-2-1-0]
  Sign: a record with no failure for a rule and revision against which the registry logs an
  exception.
- **could_not_run settled by judgement.** Someone decides the check would have passed (recommended
  practice). Sign: a positive decision on a revision where a required check produced no verdict and
  no exception exists.
- **A tier lowered to escape a check.** The tier is changed so that a check stops being required
  (recommended practice). Sign: a tier changed after a required check failed or could not run.

## Related

- Core: [Engineering Kit](engineering-kit.html#the-could_not_run-result) (the four results and who
  each goes back to), [how a check reports its result](validators.html#reporting-the-result),
  [Evidence schema](evidence-schema.html) (expected checks, results and overall status),
  [Rule registry](rule-registry.html) (exceptions logged against rules), [Workflows](workflows.html)
  (failure paths) and [Adapters](adapters.html).
- Lifecycle: [Pull-request verification](pull-request-verification.html),
  [Release readiness](release-readiness.html) and [Release](release.html).
- Assurance: [Evidence record](evidence-record.html) and
  [Change controls and standards](change-controls-and-standards.html).
- Catalog: exception handling [W33](workflow-catalog.html#W33).
- Terminology: [could_not_run](glossary.html#could-not-run), [risk tier](glossary.html#risk-tier),
  [evidence record](glossary.html#evidence-record) and the
  [export example](glossary.html#export-example).

## Sources

- Result kinds, run-level execution failure and suppressions kept with their results: SARIF
  2.1.0.[^sarif-2-1-0]
- Skipped checks on one change host, for that host's behaviour only: its documentation on protected
  branches and required status checks.[^github-protected-branches][^github-status-checks]
- A single failing test fails the build: Fowler on continuous integration.[^fowler-ci]
- Monotonic policies and verification against expectations: the in-toto attestation
  framework[^in-toto-attestation] and SLSA on verifying artifacts.[^slsa-verifying]
- Controls: NIST SP 800-53 Rev. 5, AU-5, CM-3c and CM-6c;[^nist-800-53] the NIST Secure Software
  Development Framework, task PO.4.1.[^nist-ssdf]
- Risk and the choice of what to verify: the ISTQB glossary[^istqb-rbt] and the OWASP
  ASVS.[^owasp-asvs]
- The decision reading of each result, keeping a decision without its expected evidence visible, not
  replacing a missing verdict with judgement, the risk-tier principle, and the pitfalls marked as such
  are this site's recommended practice; no public source states them.
