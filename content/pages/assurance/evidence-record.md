---
id: evidence-record
type: concept
band: assurance
map_box: Evidence record on every run, fixed schema · Rule IDs link rule → check → decision · Valid for one revision; a new push expires it
title: Evidence record
summary: How a release decision, an incident review and an audit read the same per-run record, following a rule ID from the registry to the checks that enforced it and the decisions that relied on them, treating each record as evidence for one revision only, and keeping records intact and retained.
key_terms: [ai-sdlc, evidence-record, evidence-handoff, rule-registry, validator, could-not-run, traceability-spine, export-example]
sources: [nist-800-53, nist-ssdf, slsa-vsa, slsa-verifying, slsa-build-requirements, slsa-source-requirements, github-protected-branches, sarif-2-1-0, nist-oscal, gotel-finkelstein-1994, nasa-swe-052, bockeler-sensors]
related: [evidence-schema, rule-registry, validators, traceability-spine, pull-request-verification, release-readiness, incident-feedback, release, check-results-and-decisions, change-controls-and-standards, agent-permissions]
review_record: content/reviews/1.7.0-assurance.md
---

## Definition

In an AI SDLC (the software development lifecycle with AI agents doing part of the work), an
evidence record is the account one workflow run gives of one revision: which checks were due, how
each came out, what agents flagged and what named people decided. Every run writes it in the same
shape, which the [Evidence schema](evidence-schema.html) page sets out. Read as assurance reads it,
the record is the single account that release, incident review and audit all consult when they ask
what was checked on a revision and who decided. The term is coined by this site. Its public
relatives include SLSA's verification summary attestation, a stored verification outcome that names
the verifier, the policy and the input attestations used and gives a result of passed or
failed,[^slsa-vsa] and the audit records that NIST SP 800-53's audit and accountability controls
require an organisation to review, protect and retain.[^nist-800-53]

## Why it matters

When release, incident review and audit each assemble their own evidence, they end up with three
accounts of the same change, and the accounts can disagree about what was checked and on which
revision. One record, read by all three, removes the disagreement at its source. No public study
compares the two arrangements, so this is recommended practice rather than a finding.

Public frameworks ask for evidence that is kept and protected. NIST's Secure Software Development
Framework asks producers to archive supporting data and provenance for each release (tasks PS.3.1
and PS.3.2), and, for security checks, gives the example of recording approvals, rejections and
exception requests in the workflow and tracking system (PO.4.1).[^nist-ssdf] NIST SP 800-53 asks for
audit information to be protected (AU-9) and audit records retained (AU-11).[^nist-800-53] With
agents doing part of the work, the record is also where a reader tells what automation established
from what a person decided ([Evidence schema](evidence-schema.html#why-it-matters)).

## How it works

### One record, three readers

The map's assurance band carries the caption that auditors, release and incident review all read
the same record ([the map](index.html)). Each reader brings its own question to it.

**Audit.** An auditor asks whether a control was applied to a change, with what result, who
decided, and whether the record itself can be trusted. The answers sit in the
[expected checks](evidence-schema.html#expected-checks-before-results), the
[check results](evidence-schema.html#check-results) and the
[findings and decisions](evidence-schema.html#agent-findings-and-decisions). NIST SP 800-53 asks for
audit records to be reviewed and analysed, at a frequency the organisation defines, for signs of
inappropriate or unusual activity, with findings reported to defined roles (AU-6); AU-9 and AU-11
are what let the auditor trust what it reads.[^nist-800-53]

**Release.** A release decision asks whether every record for the candidate's revision allows a
positive decision, and reads the [overall status](evidence-schema.html#overall-status) of each
([Release readiness](release-readiness.html)). SLSA describes the same stance for provenance: a
verifier compares what was recorded against expectations set in advance, and a failed verification
achieves little unless a person or a system acts on it.[^slsa-verifying]

**Incident review.** An incident review asks what was checked and decided on the revision that was
running when the failure occurred ([Incident feedback](incident-feedback.html)). AU-11 names this
use directly: records are retained to support after-the-fact investigation of
incidents.[^nist-800-53]

Each workflow page lists the readers of its own record:
[Pull-request verification](pull-request-verification.html#who-reads-the-record),
[Release readiness](release-readiness.html#outputs-and-evidence) and
[Incident feedback](incident-feedback.html).

### Rule IDs from rule to check to decision

The forward walk starts at the rule. Its entry in the rule registry names the checks that enforce
it, and every other part of the kit cites the rule by its identifier
([Rule registry](rule-registry.html#how-the-rest-of-the-kit-refers-to-rules)). Next comes the check:
a record lists those checks among its expected checks with the rule ID, and each result carries the
same ID and a link to its report ([Evidence schema](evidence-schema.html#check-results)). SARIF, the
OASIS format for analysis results, puts a rule identifier on every result in the same
way,[^sarif-2-1-0] and NIST publishes its control catalogue as machine-readable data, so that tools
refer to each control by identifier.[^nist-oscal] Last comes the decision: decisions in the same
record were taken with those results in view, and the overall status is derived from both
([Evidence schema](evidence-schema.html#overall-status)).

The backward walk runs from a decision to its record, to the results and findings in it, to their
rule IDs, and to the registry entry as it stood at the record's configuration revision, which fixes
the version of the rule that applied (see Changing under
[Rule registry](rule-registry.html#entering-changing-and-retiring-rules)). Requirements traceability
is defined as following a requirement forwards and backwards through its
life,[^gotel-finkelstein-1994] and NASA's software engineering handbook asks for bidirectional
traceability.[^nasa-swe-052] Both speak of requirements; applying both directions to rule IDs is
this site's practice.

The walk has limits. A decision carries no rule ID of its own
([Traceability spine](traceability-spine.html#rule-ids-as-link-keys)). The record holds no date, so a
question about a period joins records to the change host's dates by change revision (recommended
practice); a question that needs a new field is a schema change made by the kit
([versioning the schema](evidence-schema.html#versioning-the-schema)). Across many records, as
recommended practice, an auditor picks out for one rule the records where its check was expected and
did not pass, and the decisions taken anyway; AU-6's review of audit records for unusual activity is
the public basis for reading records in aggregate.[^nist-800-53]

### Valid for one revision

A record is evidence for the change revision and configuration revision it names, and for nothing
else. A new push makes a new revision, which starts a new run and a new record, while the earlier
record stays with the earlier revision as history
([revisions and versions](evidence-schema.html#revisions-and-versions),
[Pull-request verification](pull-request-verification.html#trigger), and the glossary's
[evidence hand-off](glossary.html#evidence-handoff)). Supply-chain practice binds a result to what
was examined in the same way: SLSA's verification checks that the subject matches the digest of the
artefact in hand.[^slsa-verifying][^slsa-vsa]

A release decision reads only the records for the candidate's revision
([Release readiness](release-readiness.html)). An approval given on an earlier revision does not
carry over: SLSA's source track, at its highest level, applies two-party review to the final
revision submitted and requires changes made during review to be reviewed as
well.[^slsa-source-requirements] At least one change host can dismiss earlier approvals when new
commits change the diff.[^github-protected-branches]

Expiry ends a record's use as input to a new decision, not the record. It remains the evidence of
what was checked on its own revision, which audit and incident review go on reading, the later use
AU-11's retention serves.[^nist-800-53] When only the configuration revision changes, the older
record describes checks against the older rules and thresholds; as recommended practice, a release
that must meet the rules now in force asks for a fresh run. A mainline that moves after a run is
handled under [Pull-request verification](pull-request-verification.html#failure-paths).

### Integrity, retention and correction

**Protection.** Records are protected from unauthorised access, change and deletion, as AU-9 asks of
audit information.[^nist-800-53] For security checks, the SSDF's examples include allowing only
authorised personnel to reach the gathered information and preventing its alteration or deletion
(PO.4.2).[^nist-ssdf] The machine fields are written by the kit, out of reach of what a run
controls ([who writes each field](evidence-schema.html#who-writes-each-field)), after SLSA's rule
that the build platform, not the tenant, generates provenance.[^slsa-build-requirements]

**Retention.** Records are kept for a period the organisation defines, as AU-11 asks, to support
later incident investigation and regulatory and organisational retention
requirements.[^nist-800-53] They sit beside the release's archived files and provenance (SSDF
PS.3.1;[^nist-ssdf] [Release readiness](release-readiness.html#outputs-and-evidence)). Protection
and retention are properties of the store that holds records, not fields in them.

**Correction.** A wrong machine field is put right by a new run, and a value entered by hand names
who entered it ([who writes each field](evidence-schema.html#who-writes-each-field)). What assurance
adds, as recommended practice on the AU-9 basis, is that a correction keeps the earlier record
readable, so an audit sees both the original entry and the correction. A decision changes through a
new decision entry by the named decider, not by altering the old entry; this too is recommended
practice.

### The customer-record export

The customer-record export is this site's running example, a hypothetical feature that lets users
export customer records. Its first pull-request record names change revision `3f9c2e1`: the access
rule R-042 failed with a report link, the volume-limit rule R-017 returned
[could_not_run](glossary.html#could-not-run), a review-skill finding sits under R-042, a request to
exceed R-017's row limit is pending with the security owner, and the overall status is blocked
([Evidence schema](evidence-schema.html#the-customer-record-export)). The narrowed worker query
arrives as a second revision with its own record
([Pull-request verification](pull-request-verification.html#in-the-customer-record-export)). The
export counts as one change.

The release decision reads only the record for the latest revision. For that purpose `3f9c2e1` has
expired, and its R-042 failure counts neither for nor against the candidate. The latest record shows
the R-017 request still pending, so the decision waits ([Release readiness](release-readiness.html)).

An auditor starts at R-042 in the registry and finds it among the expected checks of both records:
on the first, the failure, its report and the review skill's finding beside it; then the second
record's own R-042 entry. The pending R-017 request reads backward the same way, from the decision
to R-017's result in the same record and on to R-017's registry entry, whose owner decides on
requests to exceed the limit ([Rule registry](rule-registry.html#deciding-how-each-rule-is-enforced)).
When the export later times out in production, the incident review starts from the release record
and reads back through the records it names
([Traceability spine](traceability-spine.html#the-customer-record-export-left-to-right-and-back)).

## Where it sits on the map

The page covers three bullets in the Evidence & traceability column of the assurance band: "Evidence
record on every run, fixed schema", "Rule IDs link rule → check → decision" and "Valid for one
revision; a new push expires it", the last two by the anchors above. The band caption names the three
readers. The column's remaining bullet, "passed · failed · skipped · could_not_run", leads to
[Check results and decisions](check-results-and-decisions.html). The core band defines the record
([Evidence schema](evidence-schema.html)) and the identifiers ([Rule registry](rule-registry.html)),
and [validators](validators.html) write the results. The lifecycle band's
[Traceability spine](traceability-spine.html) chains records from requirement to incident, and the
Measurement column derives its measures from records.

## Pitfalls

- **Evidence from an earlier revision accepted.** The pitfall the
  [Release](release.html#pitfalls) page names, seen from the record's side. Sign: the revision in a
  record a decision relied on differs from the candidate's.
- **An approval carried across a push.** Review applies to the final revision
  submitted.[^slsa-source-requirements] Sign: on a merged change, the approval predates the latest
  revision.
- **A record edited in place.** A correction changes the stored entry instead of adding to it, which
  is the modification AU-9 guards against.[^nist-800-53] Sign: a record reads differently from an
  earlier copy, and nothing later in the store says why.
- **Records removed along with their revision.** Records are discarded when a branch or revision is
  cleaned up, before the retention AU-11 asks for has run.[^nist-800-53] Sign: an incident review
  cannot find the record for the release that was running.
- **A rule read at today's wording.** The auditor reads the current registry entry, not the one at
  the record's configuration revision (recommended practice). Sign: an audit finding against a rule
  that changed after the decision was taken.
- **Three readers, three copies.** Release, incident review and audit each keep their own account
  (recommended practice). Sign: release notes, the incident timeline and an audit sample disagree on
  what was checked.

## Related

- Core: [Evidence schema](evidence-schema.html) (the record's fields and writers),
  [Rule registry](rule-registry.html) (rule IDs, enforcing checks, owners) and
  [Validators](validators.html) (the checks that write results).
- [Traceability spine](traceability-spine.html): the chain of artefacts that records link together.
- [Pull-request verification](pull-request-verification.html),
  [Release readiness](release-readiness.html) and [Incident feedback](incident-feedback.html): the
  workflows that write and read the records, and the [Release](release.html) phase.
- [Check results and decisions](check-results-and-decisions.html): what each status means for a
  decision, and how a waiver is recorded.
- [Change controls and standards](change-controls-and-standards.html): how external controls are met
  through rules, checks and records.
- [Agent permissions](agent-permissions.html): reviewing what each agent identity may write.
- Terminology: [evidence record](glossary.html#evidence-record),
  [evidence hand-off](glossary.html#evidence-handoff) and the
  [export example](glossary.html#export-example).

## Sources

- Audit records, their review, protection and retention: NIST SP 800-53 Rev. 5, controls AU-6, AU-9
  and AU-11.[^nist-800-53]
- Release archives, provenance and records of security-check decisions: the NIST Secure Software
  Development Framework, tasks PS.3.1, PS.3.2, PO.4.1 and PO.4.2.[^nist-ssdf]
- Verification, stored verification results and who generates provenance: SLSA on verifying
  artifacts,[^slsa-verifying] verification summary attestations[^slsa-vsa] and build
  requirements.[^slsa-build-requirements]
- Review of the final revision: SLSA's source requirements;[^slsa-source-requirements] dismissal of
  earlier approvals on one change host, for that host only.[^github-protected-branches]
- Rule identifiers and control catalogues: SARIF 2.1.0[^sarif-2-1-0] and NIST OSCAL.[^nist-oscal]
- Tracing in both directions: Gotel and Finkelstein[^gotel-finkelstein-1994] and NASA SWE-052.[^nasa-swe-052]
- One record for three readers, rule IDs traced in both directions, date queries through change-host
  dates, the aggregate audit reading of one rule, a fresh run after a configuration change,
  corrections that keep the earlier record readable, decisions changed by new entries, and the
  pitfalls marked as such are this site's recommended practice; no public source states them.
- Computational and inferential controls, and the validator and review-skill vocabulary: Böckeler[^bockeler-sensors].
