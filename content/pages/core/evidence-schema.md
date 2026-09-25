---
id: evidence-schema
type: concept
band: core
map_box: Engineering Kit · evidence schema
title: Evidence schema
summary: The fixed, versioned shape of what every run records (revisions, kit version, expected checks and their results, agent findings, decisions and an overall status) and who is allowed to write each field.
key_terms: [evidence-record, could-not-run, validator, rule-registry, review-skill, evidence-handoff, engineering-kit, mechanism-vs-meaning, workflow, export-example]
sources: [slsa-provenance, slsa-build-requirements, slsa-verifying, slsa-vsa, in-toto-attestation, in-toto-spec, in-toto-usenix, sarif-2-1-0, nist-ssdf, aicpa-soc2, json-schema-core, semver, fowler-tolerant-reader, bockeler-harness, bockeler-sensors]
related: [engineering-kit, validators, rule-registry, skills-and-evals, workflows, adapters]
review_record: content/reviews/1.4.0-core.md
---

## Definition

An evidence schema is the fixed, versioned shape of the record that each run leaves behind in an
AI SDLC (the software development lifecycle with AI agents doing part of the work). It names
every field that record holds: the revision of the change and of the configuration the run used,
the version of the kit that ran it, the checks expected before the run and the result of each,
findings from agents, decisions pending and taken, and an overall status derived from the rest. It also says which kind of writer fills each field.
This site calls one instance of that shape an *evidence record*, and holds that the schema is the
one part of an Engineering Kit (the versioned package of rules, checks, skills and adapters a team
and its coding agents work inside) that a project cannot customise. Both are working names used on
this site, not industry terms. The idea has close public relatives. Supply-chain provenance is
"verifiable information about software artifacts describing where, when, and how something was
produced",[^slsa-provenance] and a standard results format gives every static-analysis result the
same shape, including the identifier of the rule it concerns.[^sarif-2-1-0]

## Why it matters

Logs and pipeline console output record what tools printed. They answer a question only for
someone prepared to read them, and their shape changes from tool to tool and from run to run. A
reviewer, a release approver or an auditor who needs to know whether the access check ran against
the revision being merged has to piece the answer together from that output, and a check that
never ran can look exactly like one that passed without comment. A record with fixed, named fields
answers the same question by lookup, and it shows a missing result as a missing value. No public
study compares the two approaches directly, so this is recommended practice rather than a
research finding.

Outside requirements point the same way. The SOC 2 change-management criterion CC8.1 covers
authorising, documenting, testing and approving changes.[^aicpa-soc2] It does not prescribe a
record format, but evidence that is incomplete, or shaped differently in every project, makes
those activities harder to demonstrate. NIST's Secure Software Development Framework includes
configuring tools to generate artifacts of their support of secure development practices, and
archiving provenance data for each software release.[^nist-ssdf] Coding agents raise the stakes.
When a machine does part of the work, the record is where a reader separates what automation
established from what a person decided, and that separation holds only if the schema builds it
in.

## How it works

The schema fixes nine fields and one writer for each.

| Field | What it holds | Written by |
|---|---|---|
| Schema version | The version of the schema the record follows | The kit |
| Change revision | The exact revision of the change that the checks examined | The kit |
| Configuration revision | The revision of the rules, thresholds and project configuration the run used | The kit |
| Kit version | The version of the kit, and of the agent tooling it drove | The kit |
| Expected checks | Every check that applies to this change, each with its rule ID, listed before any result | The kit, from the change and the project configuration |
| Check results | For each expected check: rule ID, status (passed, failed, skipped or could_not_run), the reason where it did not run, and a link to the full report | Each validator |
| Agent findings | Each finding, with the rule ID it concerns, its location and its text; advisory only | The review skill, or another agent |
| Decisions | Each decision, with its subject, a named decider, its state (pending or taken) and a reason code | A named person |
| Overall status | One status derived from the results and decisions by a stated rule | The kit |

### Revisions and versions

A result is evidence only for what it examined, so the record names the change revision and the
configuration revision separately. SARIF, the OASIS standard format for static-analysis results,
records a revision identifier that
"uniquely and permanently identifies" the scanned files, and notes that a branch name alone may not
suffice, because a branch points at whatever commit is latest.[^sarif-2-1-0] SLSA provenance
separates the definition of a build (its parameters, split into those a user controls and those
the build platform controls) from the details of the run (the platform that executed it, its
timing and its by-products).[^slsa-provenance] The kit version plays a part similar to the build
platform's identity, and the configuration revision a part similar to the parameters; SLSA has
neither field by these names. Recording the kit version lets a team compare results from before
and after an upgrade. When the change moves to a new revision, the earlier record stays attached
to the earlier revision and is never rewritten onto the new one.

### Expected checks before results

The kit works out which checks apply from the change itself and the rules the project
configuration says apply to it, and writes that list into the record before anything runs.
Results are then written against the list. The record is complete only when every expected check
has a result, and a check with no result stands out as a missing entry. Fixing the list first also
means a run cannot pick its checks once it knows how they turned out. Supply-chain integrity
frameworks also set expectations first. In the in-toto specification, a project owner's layout
sets the required steps and who may carry them out, link metadata records that each step
happened, and verification compares one against the other.[^in-toto-spec] The framework was presented at the 2019 USENIX Security Symposium as a way
for end users to verify a software supply chain from inception to deployment.[^in-toto-usenix]
SLSA likewise has verifiers compare provenance against expectations known in
advance.[^slsa-verifying] Both keep the expectation apart from the record. Holding the expected
list and the results in one record, so that a missing result is visible at a glance, is
recommended practice.

### Check results

Each result carries the rule ID from the rule registry, the stable identifier that SARIF also puts
on every result.[^sarif-2-1-0] Its status comes from a fixed list. A check that timed out, did not
report, or could not start is never recorded as passed. This site keeps could_not_run as a status
of its own, so that an unavailable environment and a real defect stay distinguishable and each
gets the response it needs, and, like a failure, it prevents a positive overall status. No
standard defines a per-check status of this kind. SARIF records whether the analysis tool itself
ran successfully, at the level of the whole run, and states that a consumer must not assume a
failed run contains a complete set of results.[^sarif-2-1-0] Each result also links to the full
report, so anyone who doubts a result can open the evidence behind it; a status that cannot be
followed back to its reports cannot be checked. That link is recommended practice, not a field any
standard defines.

### Agent findings and decisions

A review skill, an agent that reads the change against the rules and reports what it finds, is an
inferential control: it proposes and does not decide.[^bockeler-sensors] Its findings carry rule
IDs, so they sit beside the validator results for the same rules, but no finding changes a check's
status or the overall status.

Decisions live in the record, not in a chat thread or a pull-request comment. Each one names its
subject, the person who decides and whether it is pending or taken, and it carries a reason chosen
from a fixed list, so decisions can be counted and compared across projects. SARIF offers a
precedent: a suppression records whether it is under review, accepted or rejected, with a
justification the user supplies, and the standard warns that such user-supplied text needs care
when it is displayed or shared.[^sarif-2-1-0] Coded reasons are this site's recommended practice.

### Who writes each field

Each field has one kind of writer, so a reader knows what stands behind every value. Supply-chain
practice sets the same boundary for provenance. SLSA requires the build platform, not the tenant
whose build it runs, to generate provenance, and at its highest build level every field must be
generated or verified by the platform, out of reach of the build steps a user controls.[^slsa-build-requirements]
In the evidence record, the kit plays the platform's part for the fields it observes, and the
permissions of each identity enforce the split. A value a person enters where the kit should have
observed it is marked as manual and names who entered it. A wrong machine field is put right by a
new run, not by editing the record. Applying this boundary to validators, agents and people is
recommended practice.

### Overall status

The overall status is derived from the results and decisions by a rule the schema version states.
Nobody sets it directly. SLSA's verification summary attestation shows the same pattern as a
record of its own: it names the verifier, the policy applied, the input attestations used and a
result of passed or failed.[^slsa-vsa] What each overall status means for a release decision
belongs to assurance, not to the schema.

### The customer-record export

The pull-request run for the customer-record export leaves a record like this. The comments show
which writer filled each field.

```yaml
schema_version: "1.2"                      # kit
change_revision: 3f9c2e1                   # kit
configuration_revision: 81ad07b            # kit
kit_version: "2.3.0"                       # kit
expected_checks:                           # kit, from project configuration
  - {rule: R-042, check: access validator}
  - {rule: R-017, check: 50k-row load scenario}
results:                                   # each validator
  - {rule: R-042, status: failed, report: reports/r-042-access.html}
  - {rule: R-017, status: could_not_run, reason: load-test tool missing from runner image}
findings:                                  # review skill (advisory)
  - {rule: R-042, location: background export worker,
     text: the worker's query reads records outside the requesting user's scope}
decisions:                                 # a named person
  - {subject: request to exceed the R-017 row limit,
     decider: security owner, state: pending}
overall_status: blocked                    # kit, derived
```

R-042, the access rule, failed, and its report link leads to the failing case. The 50k-row load
scenario for R-017, the volume-limit rule, could not run because the load-test tool is missing
from the runner image; the record says so rather than showing a pass or leaving a gap. The review
skill's finding on the background worker's query sits under R-042 beside the validator's failure
on the same query. The security owner's judgment on the request to exceed R-017's row limit is
visible as pending. The kit derives the overall status from these entries, and no entry in this
record could turn it positive.

### Versioning the schema

Every record declares the schema version it follows, as a SARIF log names its format version and
the URI of the matching schema,[^sarif-2-1-0] and as JSON Schema's `$schema` keyword identifies the
dialect a schema uses.[^json-schema-core] Semantic Versioning supplies the rule for the number:
the major version changes for incompatible changes, the minor version for backward-compatible
additions and the patch version for backward-compatible fixes.[^semver] For a schema, removing or
renaming a field, or changing what a status means, is a major change; a new optional field is a
minor one.

Readers are written to survive that evolution. The in-toto attestation framework puts the major
version in each type's identifier and requires consumers to ignore fields they do not
recognise.[^in-toto-attestation] SLSA provenance carries the same requirement and keeps its minor
versions backward compatible.[^slsa-provenance] Martin Fowler's Tolerant Reader recommends the same
stance for any consumer: read data from another service as tolerantly as
possible.[^fowler-tolerant-reader] in-toto adds a safety condition. Policies should be monotonic,
so that ignoring a field or an attestation can never turn a deny into an
allow.[^in-toto-attestation] A reader that meets an unknown field in an evidence record may skip
it, but a skipped field must never produce a positive status. Changing a status, a reason code or
a required field means publishing a new schema version. Records are never rewritten into a newer
version; each is read by the version it declares.

### Why the schema is fixed

This site separates what a kit supplies, the mechanism, from what a project supplies, the
meaning. A project decides which rules apply to its work, which checks run and with what
thresholds, and writes its own specification. The kit supplies the machinery that carries those
choices: its commands, its checks, its adapters and this schema. What the evidence must contain,
and what each field means, belongs to that machinery and stays fixed, because records can be
compared, aggregated and audited across teams only when they share one shape. The same reasoning
appears in the public standards. in-toto fixes a common statement layer that binds a subject to
a predicate of a named type, so any consumer can parse any attestation and pick out the types it
understands.[^in-toto-attestation] SLSA verifiers check provenance by comparing named fields
against expected values,[^slsa-verifying] which works only when every producer fills the same
fields. Where a project needs extra data, SLSA's convention of prefixed extension fields that
readers may ignore is one workable pattern,[^slsa-provenance] provided no extension is needed to
derive the overall status. A change to what the evidence requires goes through the kit's own
change process and a new schema version, not a local setting. No public source states this rule
for an engineering kit; it is this site's recommended practice.

## Where it sits on the map

The evidence schema is one of the five parts of the Engineering Kit box in the core band, the band
that does the work. The other four parts feed it. The [rule registry](rule-registry.html) supplies
the IDs that every expected check, result, finding and decision carries.
[Validators](validators.html) write the results, including could_not_run.
[Skills with evals](skills-and-evals.html) include the review skill that writes agent
findings. [Adapters](adapters.html) carry the record between the kit and the pipeline runner and
change host without tying its shape to any one tool. The [Engineering Kit](engineering-kit.html)
overview shows how the parts are packaged and versioned together.

The Core row reads Harness engineering, then the Engineering Kit, then Workflows, then the
Software factory. After the kit, every [workflow](workflows.html) leaves a record in this shape
each time it runs, and later workflows read earlier ones, which the glossary calls the
[evidence hand-off](glossary.html#evidence-handoff). The [software factory](software-factory.html)
depends on that shared shape: workflows can share evidence only when they write it the same way.
The assurance band covers how records are read for audit, traceability and release, and how long
evidence stays valid for a revision.

## Pitfalls

- **The record is a log dump.** The schema stores console output instead of fields. Sign to watch
  for: approvers still open pipeline logs to find out whether a check ran.
- **Absence reads as success.** A check with no result is treated as fine. Sign: a record lists
  fewer results than expected checks and its overall status is still positive.
- **could_not_run is folded into skipped or passed.** Sign: the count of skipped checks rises
  whenever an environment is down, and nobody is told.
- **The summary hides the detail.** Sign: an overall status that cannot be traced to a per-check
  result and its report.
- **An agent can sign off.** Sign: the identity that runs the agent also has permission to write
  decision fields or the overall status.
- **Machine fields are edited by hand.** Sign: the change revision in the record does not match
  the revision on the change host, and nothing marks the entry as manual.
- **Each project reshapes the evidence.** Sign: comparing two teams' records needs a hand-written
  mapping between their fields.
- **Meanings change silently.** Sign: records from different months use the same status or
  reason for different things, with no schema version change between them.

## Related

- [Engineering Kit](engineering-kit.html): the package the schema belongs to, and its other parts.
- [Rule registry](rule-registry.html): where the rule IDs in every record come from.
- [Validators](validators.html): how a check reports a result, including when it cannot run.
- [Skills with evals](skills-and-evals.html): the review skill and the agent findings it
  writes.
- [Adapters](adapters.html): how records move between the kit and the tools that host them.
- [Workflows](workflows.html): the unit of work that leaves a record on every run.
- [Software factory](software-factory.html): the operating state that shared evidence makes
  possible.
- [Harness engineering](harness-engineering.html): the discipline the kit and its schema serve.
- [Terminology](glossary.html#evidence-record) and the [workflow catalog](workflow-catalog.html).

## Sources

- Provenance, verification and who may write it: SLSA's provenance format[^slsa-provenance], build
  requirements[^slsa-build-requirements], artifact verification[^slsa-verifying] and verification
  summary attestation[^slsa-vsa].
- Expected steps checked against recorded ones, fixed attestation shapes and monotonic readers:
  the in-toto specification[^in-toto-spec], the in-toto attestation framework[^in-toto-attestation]
  and the USENIX paper that presented in-toto[^in-toto-usenix].
- Rule IDs per result, run-level execution failure, revision identifiers and suppression status:
  SARIF 2.1.0[^sarif-2-1-0].
- Change-management and secure-development requirements: the SOC 2 Trust Services
  Criteria[^aicpa-soc2] and the NIST Secure Software Development Framework[^nist-ssdf].
- Schema versioning and tolerant readers: JSON Schema[^json-schema-core], Semantic
  Versioning[^semver] and Fowler's Tolerant Reader[^fowler-tolerant-reader].
- Computational and inferential controls, and the validator and review-skill vocabulary:
  Böckeler[^bockeler-harness][^bockeler-sensors].
- The difference between records and logs, expected checks in the same record, report links, the
  per-check could_not_run status, coded decision reasons, one kind of writer per field and the fixed schema are this site's
  recommended practice; no public source states them.
