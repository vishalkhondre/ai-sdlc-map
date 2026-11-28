---
id: rule-registry
type: concept
band: core
map_box: Engineering Kit · rule registry
title: Rule registry
summary: The single list of the rules a team relies on, each with a stable identifier, a statement, how it is enforced, an owner and its known gaps, which validators, skills and evidence records refer to by identifier.
key_terms: [rule-registry, architecture-decision-record, gate, validator, skill, review-skill, evidence-record, deterministic-gate, feedback-path, engineering-kit, export-example]
sources: [bockeler-harness, bockeler-sensors, openai-harness, fitness-function, owasp-asvs, owasp-asvs-v4-users, nist-800-53, nist-oscal, cwe-deprecated, nygard-adr, tw-radar-adr, tw-radar-security-policy-as-code, nist-800-37, sadowski-tricorder, sadowski-cacm-2018, sarif-2-1-0, nasa-swe-052, dora-metrics]
related: [engineering-kit, validators, skills-and-evals, evidence-schema, harness-engineering, workflows]
review_record: content/reviews/1.4.0-core.md
---

## Definition

A rule registry is the one place where a team lists the rules its software must keep, one entry
per rule. Each entry carries a stable identifier, a statement of the rule in a sentence or two, a record of how the rule is enforced (the checks that enforce it, the named
person who decides on it, or both), a named owner, and the
known gaps in that enforcement. Other parts of the engineering environment point at entries by
identifier: a validator names the rules it enforces, a skill names the rules it supports, and an
evidence record names the rule checks that ran. "Rule registry" is a working name coined by this site, not an industry term; the registry is one of the five parts of the
[Engineering Kit](engineering-kit.html).

## Why it matters

In an AI SDLC (the software development lifecycle with AI agents doing part of the work), coding
agents produce more changes than people can read line by line, and every change is expected to
respect the same rules: who may see which data, which layers may depend on which, how large an
operation may be. Those rules usually start out scattered across agent instruction files, review
comments, wiki pages and the memory of a few senior engineers. A rule held only as a sentence in an
agent's instructions is kept whenever the agent happens to keep it. Nothing refuses the change that
breaks it, and nobody can say afterwards whether it held.

A registry fixes three things that scattered rules cannot. First, identity: once a rule has an
identifier, a check, a skill and a run record can all say which rule they concern, and the team can
ask which rules have no check at all. Second, strength: the entry says how firmly the rule is held by naming the
checks that enforce it, the person who decides on it, or both, so a rule that rests on nothing more
than a sentence in an instruction file shows up as a gap instead of passing for an enforced one. Third, responsibility: an owner per rule means
a failing or noisy rule is somebody's problem to fix rather than everybody's reason to ignore it.

The idea is familiar from security practice. Requirement and control catalogues give every item an
identifier so that other documents and tools can refer to it precisely[^owasp-asvs][^nist-800-53],
and NIST publishes its control catalogue as structured data that tools can read[^nist-oscal].
Security policy as code applies the same thinking to a team's own policies: they are written as
files, kept under version control and validated automatically in the pipeline[^tw-radar-security-policy-as-code].
A rule registry brings that discipline to the engineering rules a team and its agents work under.

## How it works

### What an entry holds

Every entry has the same fields. The table shows them for the access rule in the site's running
example, a feature that lets users export customer records.

| Field | What it holds | Example: R-042 |
|---|---|---|
| Identifier | A short code that never changes and is never reused | R-042 |
| Statement | The rule in one or two plain sentences | An identity may export only the customer records it may read |
| Enforcement | The checks that enforce the rule, named by validator identifier, the named person or role who decides on it, or both; an entry with neither says so openly | The access validator, a required check on every change that touches an export path, including background workers |
| Owner | The named person or role who answers for the rule | The security owner |
| Known gaps | What the enforcement does not cover, and gaps since closed | None open. The background worker's broader query was recorded here as a gap and closed when the validator was extended to cover it |
| External reference | An outside control or standard the rule implements, if any | SEC-004, the security-standard entry it serves |
| Status | Active, superseded or retired, with a pointer to any replacement | Active |

Two further fields earn their place once the registry is in use. A rule enforced by a check records its rollout
stage, report-only or required; the
[Validators](validators.html) page describes that path. And each entry links to the record of why
the rule exists and how it has changed, in the manner of an architecture decision record: Michael
Nygard's short, numbered records of a decision's context, the decision itself, its status and its
consequences[^nygard-adr].

The registry is held as data in the repository, next to the code it governs, so that tools can read
it and every change to it is reviewed and versioned like any other change. The Thoughtworks
Technology Radar makes the same argument for decision records: kept in source control rather than a
wiki, they stay in step with the code[^tw-radar-adr].

### Identifiers that stay put

An identifier is useful only if it keeps meaning the same rule. Codes that encode a position in a
document tend not to. OWASP's Application Security Verification Standard numbers each requirement
by chapter, section and requirement, and asks other documents and tools to cite the standard's
version alongside the number, because the numbers may change between versions[^owasp-asvs]. When
the standard was restructured for version 5.0, even requirements whose meaning had not changed
received new numbers, and OWASP published mappings between the old and new
schemes[^owasp-asvs-v4-users].

The recommended practice for a registry is therefore an identifier that carries no position: R-042
says nothing about where the rule sits, so the registry can be reorganised without renumbering it.
A rule that is no longer needed is retired, not deleted, and its identifier is never given to
another rule, so that an old run record or review comment still resolves to what it meant at the
time. Public catalogues handle withdrawal in a similar way. NIST SP 800-53 keeps withdrawn controls
in its catalogue under their identifiers, with a note of where their content went[^nist-800-53].
MITRE's weakness list keeps deprecated entries, grouped in a view of their own, each expected to
point to its replacement[^cwe-deprecated]. Nygard's decision records are numbered in sequence, the
numbers are not reused, and a reversed decision is kept and marked superseded[^nygard-adr].

### Deciding how each rule is enforced

For each rule the team asks what can tell, on any given change, whether the rule held. Where a
program can detect a violation and give the same verdict every time on the same input, the rule
suits a validator, and the entry names that validator by its identifier. Rules about layers and
dependencies often qualify, because architecture goals can be written as executable tests that run
with the build[^fitness-function]. Where the answer turns on purpose or context, such as whether the
fields in an export are the ones its users need, the entry names the person or role who decides,
usually at review. Many rules need both: a check for the part a program can see and a named decider
for the rest, with the known-gaps field saying where the check stops.

Whether a check may stop a change is a separate choice from whether it exists. Experience with
static analysis at scale is that a check which breaks the build should be easy to understand, should
point to a fix and should never stop correct code, and that existing violations are cleared from the
codebase before the check is switched on[^sadowski-cacm-2018]. As recommended practice, an entry
records a rule as enforced by a required check, one whose failure stops the change, only once such
a check exists and the change host lists it among the checks a change must pass. Until then the
entry names the check as report-only and names who decides on the rule in the meantime. In the
running example, R-042 is enforced by the access validator as a required check; R-017's row limit
is enforced by the load scenario's check, and the rule's owner decides on any request to exceed it.

A rule with neither an enforcing check nor a named decider is not enforced, however clearly it is
written. As recommended practice, the registry shows such a rule openly, with the missing
enforcement recorded as an open known gap. An instruction file or a skill can still help the agent
keep the rule, but neither counts as enforcement, because nothing refuses the change that breaks it.

How a rule is enforced is a different question from which of Birgitta Böckeler's regulation
categories it falls under; those categories group what a harness regulates into maintainability,
architecture fitness and behaviour[^bockeler-harness]. A category says what a control is about; the
entry's enforcement field says how the rule is enforced. Reading the two together is this site's own
approach, not Böckeler's.

### How the rest of the kit refers to rules

The registry is the kit's connecting structure because every other part cites it by identifier.
A validator declares the rule identifiers it enforces, and its result names them. A skill declares
the rules it helps the agent keep. A review skill, an agent that reads a change against the
applicable rules and proposes findings, tags each finding with a rule identifier. In Böckeler's
vocabulary validators are computational sensors and review skills are inferential
ones[^bockeler-sensors]; as this site's recommended practice, a review skill proposes and does not
block. An evidence record lists which rule checks ran on a change and what each
returned.

With those references in place, questions that are otherwise guesswork have answers read straight
from data: which validator enforces R-042, which rules meant for a required check have no validator yet, which skills
still cite a retired rule. The [Evidence schema](evidence-schema.html) and
[Skills with evals](skills-and-evals.html) pages describe the other end of each reference.

### Entering, changing and retiring rules

**Entering.** A rule enters when someone writes its entry and the owner accepts it. Agent
instruction files are a good first place to look, because they often hold rules in passing: a line
such as "the export job never writes customer email addresses to its logs" is a rule without an
identifier. As recommended practice, each such line becomes an entry that records how the rule is enforced and
names an owner, and
the instruction stays where it is but cites the identifier, so the agent, a check and a reviewer all
refer to the same rule.

**Promoting.** A rule that people have been checking by hand, or that an instruction only reminds
the agent about, gains an enforcing check once a tool can check it and the rule keeps being broken.
One model vendor's published account of harness engineering describes the same move: architectural
constraints enforced through automated checks rather than through reminders[^openai-harness]. As
recommended practice, the new check starts report-only, as the [Validators](validators.html) page
describes, and the entry's enforcement field names it once it is required.

**Demoting.** A check found to be unreliable stops being required until it is fixed, and in the
meantime the entry names the person who decides on the rule, because a check that raises false
alarms trains people to override it. Checks that
block need to be trusted: one large program-analysis platform put an analyser on probation once its
not-useful rate, measured from developer feedback on its findings, reached 10 per cent, and could
switch it off above 25 per cent[^sadowski-tricorder].

**Changing.** A change to a rule is a reviewed change to the registry, made the way a change to code
is made. The pull request shows the old and new statement and the reason, lists the validators and
skills it affects, and is approved by the rule's owner. Because the registry lives in the
repository, the revision an evidence record names also fixes the version of every rule the checks
ran against, so a result is always read against the rule as it stood when the check ran.

**Exceptions.** An exception lets one change depart from a rule without changing the rule. It is
logged against the rule's identifier, with who allowed it and when it lapses. Several live
exceptions against the same rule suggest that the rule, or the way it is enforced, needs another look. A team may
also mark some rules as never open to exception; an access rule such as R-042 is the obvious case.
Who may grant an exception is a question of decision rights, which the map places in the operating
model box of its enablement band; the registry records that an exception was granted.

**Retiring.** A rule that is no longer needed is marked retired, with the recorded reason and a
pointer to any rule that replaces it. It stays in force until that decision is recorded. Its
identifier remains in the registry and is never reused.

### Owners and known gaps

NIST's Risk Management Framework allocates each security control to the system, a part of it or
its environment, so that it is clear where the control is provided[^nist-800-37]. The registry
applies a similar idea to people at the level of a single rule, and as
recommended practice gives each rule one accountable owner. In the entry this is a single name or
role that can be reached, such as the security owner for R-042, never a list or a shared alias. The
owner approves changes to the entry and is the person to ask when its check fails or is noisy.

The known-gaps field records what the enforcement does not see. A gate proves only what its check
inspects, so a passing result is read together with the gaps listed against the rule. When R-042's
validator covered only the export request itself, the background worker's broader query was
written down as a gap; extending the validator closed it, and the entry keeps the note.

As recommended practice, the registry also gives a plain reading of whether its gates are real:
the list of rules recorded as enforced by a required check that no required validator cites by
identifier. A report-only
validator does not count, because it cannot refuse anything. Since each validator declares the
identifiers it enforces, much as each result in the SARIF format for analysis output can carry a
rule identifier[^sarif-2-1-0], the list is read from data rather than compiled by hand.
Requirements traceability rests on the same idea: tracing requirements to their verification shows
the requirements that nothing tests[^nasa-swe-052]. The list is compared with its own earlier
readings, not with a target, in the way DORA advises teams to improve on their own baseline rather
than compete with others[^dora-metrics]. An empty list says only that every rule meant for a required check has a
check; the known gaps say what each check does not see.

## Where it sits on the map

The rule registry sits in the core band of the map, the band that does the work, as one of the five
parts of the Engineering Kit box: rule registry, [Validators](validators.html),
[Skills with evals](skills-and-evals.html), [Evidence schema](evidence-schema.html) and
[Adapters](adapters.html). It is the part the other four refer to. In the band's row,
[Harness engineering](harness-engineering.html) comes before the kit: it is the discipline that
decides what belongs in the registry at all. [Workflows](workflows.html) come after it: they run the
checks and skills that cite the registry, and their records carry rule identifiers onward. Rules
flow into the registry from specifications and their access rules, recurring review comments,
incidents, and the outside standards a team must meet, which an entry can reference as SEC-004 is
referenced by R-042. Tracing a rule through the checks that ran to the decisions they informed is a
matter for audit and traceability, which reads the registry but is not part of it.

## Pitfalls

- **A registry nobody reads.** The list exists as a document, but validators and skills do not cite
  it. Sign: checks whose results name no rule identifier, or rules that appear only in agent
  instruction files.
- **Gates on paper.** A rule is recorded as enforced by a required check, but that check does not
  exist, does not cite the rule's identifier or still runs report-only, so nothing refuses a change
  that breaks it. Sign: rules recorded as enforced by a required check that no required validator
  cites by identifier, or a merged change whose evidence record shows
  that rule's check failed.
- **Rules without a reason.** Entries carry no link to why the rule exists. Sign: nobody can say
  whether a rule is still needed, so nothing is ever retired.
- **Green read as full assurance.** Known gaps are left empty. Sign: a rule whose check covers only
  the place where an operation is triggered, with nothing recorded about other code that reaches the
  same data.
- **Identifiers that change meaning.** A retired identifier is handed to a new rule, or entries are
  renumbered when the registry is reorganised, against the practice under
  [Identifiers that stay put](#identifiers-that-stay-put). Sign: an old run record or review comment
  whose identifier now leads to a rule that says something different.
- **Exceptions in place of change.** The same departure is approved again and again. Sign: several
  live exceptions against one rule identifier.
- **No real owner.** An entry names a team alias or no one. Sign: a failing or noisy rule that stays
  unchanged for weeks.

## Related

- [Engineering Kit](engineering-kit.html): the package the registry belongs to, and its other parts.
- [Validators](validators.html): the deterministic checks that enforce rules, and the path
  from report-only to required.
- [Skills with evals](skills-and-evals.html): packaged guidance for the agent, and how skills cite
  the rules they support.
- [Evidence schema](evidence-schema.html): the record of which rule checks ran on a change.
- [Harness engineering](harness-engineering.html): the discipline of deciding what the agent reads,
  what a machine checks and what a person decides.
- [Workflows](workflows.html): the unit of delivery that runs the checks the registry defines.
- [Terminology](glossary.html#rule-registry): the rule registry and the terms above.
- [Workflow catalog](workflow-catalog.html): every workflow, with the checks and decisions it holds.

## Sources

- Stable identifiers and how catalogues version and withdraw them: [^owasp-asvs],
  [^owasp-asvs-v4-users], [^nist-800-53], [^cwe-deprecated].
- Controls and policies held as data under version control: [^nist-oscal],
  [^tw-radar-security-policy-as-code].
- Recording why a rule exists and superseding rather than editing: [^nygard-adr], [^tw-radar-adr].
- Architecture rules as executable checks: [^fitness-function].
- Regulation categories, sensors, and promoting rules into tooling: [^bockeler-harness],
  [^bockeler-sensors], [^openai-harness].
- Allocating controls to where they are provided: [^nist-800-37].
- Why checks that block need to be trusted, and what makes a check fit to stop a build:
  [^sadowski-tricorder], [^sadowski-cacm-2018].
- Reading enforcement from data, and finding requirements nothing verifies: [^sarif-2-1-0],
  [^nasa-swe-052]; comparing a measure with a team's own baseline: [^dora-metrics].
