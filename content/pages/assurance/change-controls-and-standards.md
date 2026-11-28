---
id: change-controls-and-standards
type: concept
band: assurance
map_box: SOC 2 change controls · domain standards as they apply
title: Change controls and standards
summary: How the change requirements of an outside control framework, and the requirements of a domain standard, are met through the rules a team keeps, the checks that enforce them, the records each run leaves and the decisions that stay with named people, including when an agent wrote the change.
key_terms: [ai-sdlc, change-control, separation-of-duties, trust-services-criteria, rule-registry, validator, evidence-record, three-roles, export-example]
sources: [nist-800-128, nist-glossary-configuration-control, nist-800-53, nist-glossary-separation-of-duty, nist-oscal, nist-800-53b, nist-oscal-profile, slsa-source-requirements, dora-streamlining-change-approval, dora-2025-announcement, aicpa-soc2, bockeler-sensors]
related: [rule-registry, evidence-schema, workflows, software-factory, release, release-readiness, pull-request-verification, develop-build-qa, agent-permissions, evidence-record, check-results-and-decisions, ai-use-policy]
review_record: content/reviews/1.7.0-assurance.md
---

## Definition

Change control is the documented process for managing and controlling changes to a system's
configuration. NIST SP 800-128 describes it as the "systematic proposal, justification,
implementation, test/evaluation, review, and disposition of changes to the system".[^nist-800-128]
The NIST glossary gives the related term configuration control, from SP 800-53 Rev. 5: the process
for controlling modifications to hardware, firmware, software and documentation, so that the system
is protected against improper modifications before, during and after
implementation.[^nist-glossary-configuration-control] In an AI SDLC (the software development
lifecycle with AI agents doing part of the work), a team may answer to an outside control
framework or a domain standard that asks for such a process. This page describes how those
requirements are met inside the team's own machinery: each outside control is referenced by rules in
the [rule registry](rule-registry.html), each rule is enforced by checks, by a named person who
decides, or both, and the [evidence records](evidence-record.html) that runs leave are what a
reviewer or auditor reads. That chain is this site's model, assembled from the sources below; no
standard prescribes it. The map's example framework is SOC 2, whose Trust Services Criteria are set
by the AICPA's Assurance Services Executive Committee.[^aicpa-soc2]

## Why it matters

Coding agents raise the volume of change, and DORA's 2025 research ties more change, in teams
without strong automated testing, version control and fast feedback, to less stable
delivery.[^dora-2025-announcement] A control met by a meeting or a form has to absorb that volume
too. DORA reports that compliance and security managers rely on change management to validate
compliance requirements, which typically ask for evidence that changes are appropriately
authorised. It also finds that heavyweight approval from outside the team harms delivery performance,
and finds no evidence that a more formal outside review lowers
failures.[^dora-streamlining-change-approval]

Agents also change who stands behind a change. An agent can produce a change in full, but the
principle of separation of duties holds that no one should have enough privilege to misuse a system
alone;[^nist-glossary-separation-of-duty] applied to delivery, the producer of a change is never
its approver. As
recommended practice, evidence written by every run is easier to put in front of a reviewer than
evidence assembled after the fact; no public study measures the difference.

## How it works

### From control to record

Each link of the chain rests on a published page or source.

**Control to rule.** A registry entry has a field for the outside control or standard the rule
implements ([Rule registry](rule-registry.html#what-an-entry-holds)). Controls can themselves be
data: NIST publishes the SP 800-53 Rev. 5 catalogue and its baselines in the OSCAL formats, which
tools can read.[^nist-oscal] With the reference held in the registry, which outside controls have
no rule behind them becomes a question answered from data (recommended practice).

**Rule to check or decider.** The entry says how the rule is enforced: by validators named by
identifier, by a named person who decides, or both, with its known gaps showing where the check
stops ([Rule registry](rule-registry.html#deciding-how-each-rule-is-enforced)).

**Check and decision to record.** Results and decisions land in the evidence record, and each field
has one kind of writer ([Evidence schema](evidence-schema.html#who-writes-each-field)); a decision
names its subject and the person who decides
([Evidence schema](evidence-schema.html#agent-findings-and-decisions)).

**Record to reviewer.** SP 800-128 counts the documentation of approved and implemented changes
among the activities of security-focused configuration management.[^nist-800-128] On this site's reading,
the evidence record is that documentation for each run, and a reviewer or auditor reads it as the
[Evidence record](evidence-record.html#one-record-three-readers) page describes.

### Separation of duties when an agent writes the change

NIST SP 800-53's separation-of-duties control, AC-5, divides functions among different people or
roles, so that misusing privilege takes collusion.[^nist-800-53] How an agent's identity is kept from
accepting its own work is an account question, covered on
[Agent permissions](agent-permissions.html). This section is about the change.

DORA counts segregation of duties, approval by someone other than the change's author, among common
regulatory requirements and accepts peer review as a way to meet it.[^dora-streamlining-change-approval]
SLSA's source track states the strongest form: at its highest level, a change to a protected branch
needs agreement from two or more trusted persons, the uploader and the reviewer must be different
people, and a trusted person is a human the organisation authorises to propose and approve changes.
The requirement covers the final revision, so edits made during review are reviewed
too.[^slsa-source-requirements] SLSA is a graded framework, so this is its top level, not a floor, and
it lets an organisation grant a trusted automated account a perpetual exception; it does not
mention AI.
When an agent wrote the code, the developer who directed it remains the author, so the approver is
someone else ([Develop, Build and QA](develop-build-qa.html#roles)).

What assurance adds is a way of reading the record for a control. The agent's run appears as the
producer of the change and through its advisory findings, the validators as the writers of results,
and a named person as the writer of the decision. Reading these three as separate writers for a
control is this site's recommended practice.

### Approvals that stay with people

SP 800-128 places
the approval of changes with a body that holds "the collective responsibility and authority to review
and approve changes".[^nist-800-128] DORA prefers approval through peer review during development,
backed by automation that catches bad changes early, and keeps a strategic role for the change
advisory board; it does not address an outside control that requires approval by a party outside
the team.[^dora-streamlining-change-approval] Who approves a change under change control is set in
the catalog row [W32](workflow-catalog.html#W32). Who holds authority to approve at all is a matter
of decision rights, which the map places in its enablement band.

### SOC 2 change controls

The map names SOC 2, and with it the AICPA's Trust Services Criteria, as the outside framework whose
change controls it shows.[^aicpa-soc2] This page does not set out what any criterion or point of
focus says: the criteria are published by the AICPA, and the text of the edition an organisation is
examined against is the authority. The mechanism described above rests on the NIST and SLSA sources
cited there, not on the criteria. As recommended practice, a team records each change-related
criterion it answers to as the external reference of the registry entries that serve it, and a
reviewer reads the records those rules produce. Whether a criterion is met is the auditor's
judgment; a mapping by itself shows only where to look.

### Domain standards as they apply

A domain standard enters the machinery the same way as any outside control. Its requirements become
rules whose external reference names the requirement, as R-042's entry names SEC-004
([Rule registry](rule-registry.html#what-an-entry-holds)). Each rule gets an owner and a way of
being enforced. The evidence the standard asks for is then either already in the record, or a gap
that the rule's known-gaps field shows openly
([Rule registry](rule-registry.html#owners-and-known-gaps)).

Choosing which requirements apply to one system has a public analogue in NIST's control
baselines. SP 800-53B gives baselines with tailoring guidance for selecting controls, and guidance on
overlays that customise a baseline for specific communities of interest, technologies and
environments of operation.[^nist-800-53b] An OSCAL profile is the data form of such a selection: a
baseline of controls chosen from one or more catalogues, stating whether and where each is
configured or modified, which a system owner can tailor to one system.[^nist-oscal-profile] Reading
an overlay or a profile as the model for a domain-specific selection of rules is this site's
analogy, not something any domain standard states. Which kinds of product bring which standards is a
matter for the map's context band.

### The customer-record export

The site's running example is a hypothetical feature that lets users export customer records. Walked
once, the chain reads as follows. SEC-004 is an outside requirement the team must meet. R-042, the
access rule, names it as its external reference, and the access validator enforces R-042 as a
required check on every change that touches an export path, including background workers
([Rule registry](rule-registry.html#what-an-entry-holds)). The first pull-request record, for change
revision `3f9c2e1`, shows R-042 failed, with a link to its report
([Evidence schema](evidence-schema.html#the-customer-record-export)). The security owner decides on
the access design. The agent that wrote the export code appears in the record only as the producer
of the change and through its findings, never as a decider
([Workflows](workflows.html#the-three-roles-agent-checks-and-people)). The export counts as one
change.

## Where it sits on the map

The page covers the bullet "SOC 2 change controls; domain standards as they apply" in the Standards
& AI governance column of the assurance band, with an anchor for each half. Beside it sit the
[AI use policy](ai-use-policy.html) and [Agent permissions](agent-permissions.html). It reads from
the core band's [Rule registry](rule-registry.html) and [Evidence schema](evidence-schema.html),
and from the lifecycle band's [Release](release.html) phase, where the catalog rows for change
control ([W32](workflow-catalog.html#W32)) and release readiness
([W25](workflow-catalog.html#W25)) meet. What each check result means for a decision is on
[Check results and decisions](check-results-and-decisions.html).

## Pitfalls

- **The approver is the author.** DORA and SLSA both put approval with someone other than the
  author.[^dora-streamlining-change-approval][^slsa-source-requirements] Sign: a change approved by
  the identity that produced it, or by the person who directed the agent that did.
- **Approval only by an outside meeting.** Heavyweight approval from outside the team harms delivery
  performance.[^dora-streamlining-change-approval] Sign: approvals wait for a meeting while the
  record of checks already exists. The release-side case is among the [Release](release.html#pitfalls)
  pitfalls.
- **An outside control with no rule behind it** (recommended practice). Sign: a control in the
  framework's mapping that no registry entry names as its external reference.
- **Compliance claimed from a mapping** (recommended practice). Sign: a statement that a framework
  is met, with no record a reviewer can open.

## Related

- Lifecycle: [Release](release.html), [Release readiness](release-readiness.html),
  [Pull-request verification](pull-request-verification.html) and
  [Develop, Build and QA](develop-build-qa.html#roles).
- Core: [Rule registry](rule-registry.html), [Evidence schema](evidence-schema.html) and
  [Workflows](workflows.html).
- Assurance: [Agent permissions](agent-permissions.html),
  [Check results and decisions](check-results-and-decisions.html),
  [Evidence record](evidence-record.html) and [AI use policy](ai-use-policy.html).
- Workflow catalog rows: change control ([W32](workflow-catalog.html#W32)), release readiness
  ([W25](workflow-catalog.html#W25)) and exception handling ([W33](workflow-catalog.html#W33)).
- Terminology: [change control](glossary.html#change-control),
  [separation of duties](glossary.html#separation-of-duties),
  [Trust Services Criteria](glossary.html#trust-services-criteria) and the
  [export example](glossary.html#export-example).

## Sources

- Change control and configuration control: NIST SP 800-128[^nist-800-128] and the NIST glossary's
  SP 800-53 Rev. 5 definition.[^nist-glossary-configuration-control]
- Separation of duties: NIST SP 800-53 Rev. 5, AC-5,[^nist-800-53] and the NIST
  glossary.[^nist-glossary-separation-of-duty]
- Controls as data, baselines, overlays and profiles: NIST OSCAL,[^nist-oscal] NIST SP
  800-53B[^nist-800-53b] and the OSCAL profile model.[^nist-oscal-profile]
- Two-party review of the final revision: SLSA's source requirements.[^slsa-source-requirements]
- Change approval, segregation of duties and change volume: DORA on streamlining change
  approval[^dora-streamlining-change-approval] and DORA's announcement of its 2025
  report.[^dora-2025-announcement]
- SOC 2 and the Trust Services Criteria, named with their originator only: the AICPA.[^aicpa-soc2]
- The chain from control to rule to check to record to reviewer, reading the record's three writers
  for a control, external references for framework criteria, the overlay analogy for domain
  standards, evidence written on every run and the pitfalls marked as such are this site's model and
  recommended practice; no public source states them.
- Computational and inferential controls, and the validator and review-skill vocabulary: Böckeler[^bockeler-sensors].
