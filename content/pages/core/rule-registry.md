---
id: rule-registry
type: concept
band: core
map_box: Engineering Kit · rule registry
title: Rule registry
summary: The single list of the rules a team relies on, each with a stable identifier, a statement, a route (gate, judgment or guidance), an owner and its known gaps, which validators, skills and evidence records refer to by identifier.
key_terms: [rule-registry, rule-route, architecture-decision-record, gate, validator, skill, review-skill, evidence-record, deterministic-gate, feedback-path, engineering-kit, export-example]
sources: [bockeler-harness, bockeler-sensors, openai-harness, fitness-function, owasp-asvs, owasp-asvs-v4-users, nist-800-53, nist-oscal, cwe-deprecated, nygard-adr, tw-radar-adr, tw-radar-security-policy-as-code, nist-800-37, sadowski-tricorder]
related: [engineering-kit, validators, skills-and-evals, evidence-schema, harness-engineering, workflows]
review_record: content/reviews/1.4.0-core.md
---

## Definition

A rule registry is the one place where a team lists the rules its software must keep, one entry
per rule. Each entry carries a stable identifier, a statement of the rule in a sentence or two, a
route that says how the rule is enforced (a gate, a judgment or guidance), a named owner, and the
known gaps in that enforcement. Other parts of the engineering environment point at entries by
identifier: a validator names the rules it enforces, a skill names the rules it supports, and an
evidence record names the rule checks that ran. "Rule registry" is a working name coined by this
site, not an industry term; it is one of the five parts of the
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
ask which rules have no check at all. Second, strength: the route makes explicit whether a rule is
enforced by a machine, by a named person's call, or only by the agent's good behaviour, so a passing
build is not mistaken for proof that every rule held. Third, responsibility: an owner per rule means
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
| Route | Gate, judgment or guidance, and for a split rule which part takes which route | Gate |
| Owner | The named person or role who answers for the rule | The security owner |
| Known gaps | What the enforcement does not cover, and gaps since closed | None open. The background worker's broader query was recorded here as a gap and closed when the validator was extended to cover it |
| External reference | An outside control or standard the rule implements, if any | SEC-004, the security-standard entry it serves |
| Status | Active, superseded or retired, with a pointer to any replacement | Active |

Two further fields earn their place once the registry is in use. A gated rule records its rollout
stage, report-only or required, and the date by which it is planned to become required; the
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

### Choosing a route

The route is set when a rule enters the registry, and it turns on one question: could a program
tell, from the code, the configuration or the running system, that the rule has been broken, and
give the same answer every time without a stream of false alarms that people learn to ignore? A rule
for which the answer is yes is routed to a gate, a deterministic check that runs locally and in the
pipeline and can block a merge. A rule whose breach only a person with context can recognise is
routed to judgment: a named person decides against written criteria, and the decision is recorded.
Either way, the agent can also be told why the rule exists, through a skill or its instructions, and
that helps it get the change right first time. It is still not enforcement. An instruction asks; a
gate refuses.

A rule routed to guidance alone is one that no tool can check and nobody needs to sign off, such as
a naming preference with no effect on correctness. It is the weakest route, and the registry makes
that visible.

Judgment suits rules whose breach depends on meaning rather than form. A program can list the
columns a customer-record export returns, but whether a newly added column counts as personal data
depends on what it holds and why the requester needs it, and a person decides that. Where a rule
about structure can be written as an executable test, as many architecture goals can[^fitness-function],
it belongs with a gate instead.

A single rule can take two routes. R-017 limits the size of a customer-record export: the limit
itself is a gate, because a check can count rows, while a request to exceed it goes to judgment,
because only a person with the context can weigh a one-off business need against the risk.

The route is a different axis from Birgitta Böckeler's regulation categories, which group what a
harness regulates into maintainability, architecture fitness and behaviour[^bockeler-harness]. A
category says what a control is about; the route says how strongly it is enforced. The pairing is
this site's own reading, not Böckeler's.

### How the rest of the kit refers to rules

The registry is the kit's connecting structure because every other part cites it by identifier.
A validator declares the rule identifiers it enforces, and its result names them. A skill declares
the rules it helps the agent keep. A review skill, an agent that reads a change against the
applicable rules and proposes findings without blocking, tags each finding with a rule identifier.
In Böckeler's vocabulary validators are computational sensors and review skills are inferential
ones[^bockeler-sensors]. An evidence record lists which rule checks ran on a change and what each
returned.

With those references in place, questions that are otherwise guesswork have answers read straight
from data: which validator enforces R-042, which gated rules have no validator yet, which skills
still cite a retired rule. The [Evidence schema](evidence-schema.html) and
[Skills with evals](skills-and-evals.html) pages describe the other end of each reference.

### Entering, changing and retiring rules

**Entering.** A rule enters when someone writes its entry and the owner accepts it. Agent
instruction files are a good first place to look, because they often hold rules in passing: a line
such as "the export job never writes customer email addresses to its logs" is a rule without an
identifier. As recommended practice, each such line becomes an entry with a route and an owner, and
the instruction stays where it is but cites the identifier, so the agent, a check and a reviewer all
refer to the same rule.

**Promoting.** The usual change of route is upward. A rule starts as guidance or judgment and moves
to a gate once a tool can check it and it keeps being broken or keeps coming up in review. This is
one step of the feedback path, in which a recurring review comment becomes a rule and a rule that
keeps being violated becomes a gate. In the export example, reviewers keep writing that exports
should leave out the internal notes fields. The comment enters the registry as a guidance rule with
its own identifier. When the same miss appears in change after change, a validator is written, the
route becomes gate, and the guidance stays behind only to explain why. One published account of
harness engineering reports the same move: review comments and bugs are turned into documentation
or tooling, and a rule is promoted into code when documentation is not enough[^openai-harness].
The recommended practice is to write a gate for a miss that has already happened, rather than for
one that might.

**Demoting.** The route can also go down. A check found to be unreliable is treated as judgment
until it is fixed, because a gate that raises false alarms trains people to override it. Checks that
block need to be trusted: one large program-analysis platform put an analyser on probation, and
could switch it off, once its effective false-positive rate, measured from developer feedback,
reached about 10 per cent[^sadowski-tricorder].

**Changing.** A change to a rule is a reviewed change to the registry, made the way a change to code
is made. The pull request shows the old and new statement and the reason, lists the validators and
skills it affects, and is approved by the rule's owner. Because the registry lives in the
repository, the revision an evidence record names also fixes the version of every rule the checks
ran against, so a result is always read against the rule as it stood when the check ran.

**Exceptions.** An exception lets one change depart from a rule without changing the rule. It is
logged against the rule's identifier, with who allowed it and when it lapses. Several live
exceptions against the same rule suggest that the rule, or its route, needs another look. A team may
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

One simple measure, recommended by this site, shows whether the registry's routes are real: the
number of active rules routed to a gate that no required validator cites. It can be read straight
from the registry and the validators' declarations, and it falls to zero only when every gated rule
is actually enforced.

### Which rules go in first

No public study says how many rules a registry should start with. As recommended practice, the
first entries come from the team's own recent history: the incidents and review comments of the last
few months show which rules actually get broken, and a handful of those is enough to begin. A long
first list tends to produce noise, and a check switched off for noise is hard to switch back on.
These first rules and their validators, with the kit's `verify` command, which runs the same checks
in the same way on a developer's machine and in the pipeline, and an evidence schema, make up the
kit's deterministic floor. The registry then grows one rule at a time, as each new check earns the
team's trust.

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
- **Gates in name only.** An entry says gate, but its validator is missing or has stayed
  report-only past its planned date. Sign: gated rules that no required validator cites.
- **Speculative gates.** Checks are added for rules nobody has seen broken, and the first set is too
  large. Sign: gates that are routinely overridden or switched off, and complaints about noise.
- **Rules without a reason.** Entries carry no link to why the rule exists. Sign: nobody can say
  whether a rule is still needed, so nothing is ever retired.
- **Green read as full assurance.** Known gaps are left empty. Sign: a rule whose check covers only
  the place where an operation is triggered, with nothing recorded about other code that reaches the
  same data.
- **Reused or renumbered identifiers.** An identifier is given to a new rule or recomputed after a
  reorganisation. Sign: old run records or review comments that point at a rule they never meant.
- **Exceptions in place of change.** The same departure is approved again and again. Sign: several
  live exceptions against one rule identifier.
- **No real owner.** An entry names a team alias or no one. Sign: a failing or noisy rule that stays
  unchanged for weeks.

## Related

- [Engineering Kit](engineering-kit.html): the package the registry belongs to, and its other parts.
- [Validators](validators.html): the deterministic checks that enforce gated rules, and the path
  from report-only to required.
- [Skills with evals](skills-and-evals.html): packaged guidance for the agent, and how skills cite
  the rules they support.
- [Evidence schema](evidence-schema.html): the record of which rule checks ran on a change.
- [Harness engineering](harness-engineering.html): the discipline of deciding what the agent reads,
  what a machine checks and what a person decides.
- [Workflows](workflows.html): the unit of delivery that runs the checks the registry defines.
- [Terminology](glossary.html#rule-registry): the rule registry, rule routes and the terms above.
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
- Why checks that block need to be trusted: [^sadowski-tricorder].
