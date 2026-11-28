---
id: delivery-templates
type: concept
band: assurance
map_box: "Templates: spec, plan, ADR, release notes"
title: Delivery templates
summary: Why delivery with coding agents fixes the shape of its specifications, plans, decision records and release notes, what each shape must hold so a tool can check it and an agent can fill it, and how those shapes are versioned with the kit.
key_terms: [ai-sdlc, delivery-template, architecture-decision-record, acceptance-criteria, testability, spec-driven-development, traceability-spine, engineering-kit, evidence-record, validator, export-example]
sources: [json-schema-object, nygard-adr, tw-radar-adr, keep-a-changelog-2, semver, spec-kit, spec-kit-sdd, istqb-acceptance-criteria, istqb-testability, nist-ssdf, bockeler-sensors]
related: [specification, spec-readiness, design, design-conformance, release, release-readiness, definition-of-ready-and-done, traceability-spine, engineering-kit, evidence-schema, rule-registry, validators]
review_record: content/reviews/1.7.0-assurance.md
---

## Definition

A delivery template is a fixed, versioned outline for one kind of delivery document. It names the
parts a writer fills and marks which of them are required, so that a tool can confirm each required
part is present and well formed, and an agent can write a first version into it for a person to
finish. In an AI SDLC (the software development lifecycle with AI agents doing part of the work), the
map names four such documents: the specification, the plan, the architecture decision record and the
release notes. "Delivery template" is this site's working name, not an industry term. The formats it
draws on have their own originators: decision records follow Michael Nygard[^nygard-adr], changelogs
follow Keep a Changelog, created and maintained by Olivier Lacan[^keep-a-changelog-2], and version
numbers follow Semantic Versioning[^semver].

## Why it matters

Where a document says nothing, an agent working from it still produces something; the
[Specification](specification.html) page sets out why open questions are better settled in the
document than in the code. A fixed outline gives each question a place, so a reader and a tool both
know where to look.

A tool can only check what it can locate. JSON Schema shows this in miniature. By default the
properties a schema lists are not required and any other property is allowed; a document missing a
property is invalid only when the schema's `required` keyword names it, and setting
`additionalProperties` to false refuses extra properties[^json-schema-object]. A template that does
not say which parts are required lets an empty document pass. The evidence record rests on the same
reasoning, set out under [Why the schema is fixed](evidence-schema.html#why-the-schema-is-fixed).

Some content is expected in writing regardless. NIST's Secure Software Development Framework asks an
organisation to identify and document all security requirements for the software it develops and to
maintain them over time[^nist-ssdf]; a template with a place for them makes their absence visible. No
public study measures the effect of fixed document shapes on delivery, so this page's guidance on
what a template holds is recommended practice.

## How it works

Each of the four documents has one outline, kept as a file of the kit. The minimum below names only
parts that a public format or a page of this site already gives. It is not a standard, and a team adds
whatever else its work needs.

### Specification

A specification template holds the acceptance criteria and the security requirements that apply,
and it gives open questions a form a tool can find. Acceptance criteria are, in the ISTQB glossary's
words, the criteria a work product must satisfy to be accepted by the stakeholders[^istqb-acceptance-criteria].
The template gives each criterion a place of its own and an identifier, so that the tasks, tests and
results written later can name the criterion they serve; the chain those identifiers form is on
[Traceability spine](traceability-spine.html). The security part exists because NIST's Secure
Software Development Framework asks for security requirements to be identified and
documented[^nist-ssdf]. As recommended practice, the part is filled even when no security requirement
applies, with a statement saying so, so that a considered answer and a forgotten section look
different.

For open questions, one open-source spec-driven toolkit's templates require an explicit clarification
marker wherever a prompt leaves something unspecified, and the completeness checklist in the same
toolkit starts with the item that no such marker remains[^spec-kit-sdd]. How a remaining marker bears
on whether the work is ready is set out under
[Definition of Ready](definition-of-ready-and-done.html#definition-of-ready); the template only gives
the question a fixed form.

From these parts a tool can decide that the criteria section is present and not empty, that each
criterion carries an identifier no other criterion in the document repeats, that the security part is
present, and whether any marker is left. It cannot decide whether a criterion is testable, which ISTQB
describes as the degree to which test conditions can be established and tests performed to determine
whether they are met[^istqb-testability]. That stays with the people who judge the specification.

### Plan

Spec-driven development places the plan between the specification and the tasks[^spec-kit]. No public
format for the minimum content of a plan was found, so this part is recommended practice. A plan
template names the revision of the specification it answers and the decision records it relies on, so
that a tool can confirm both references resolve. Whether the plan is consistent with those records is
the question the [Design conformance](design-conformance.html) workflow decides; the template only makes
the references findable.

### Architecture decision record

Nygard's parts are given in the glossary entry
[Architecture decision record](glossary.html#architecture-decision-record) and on the
[Design](design.html) page. What a template adds is the part a tool can check: that each section is
present; that the status holds one of the values Nygard names (proposed, accepted, deprecated or
superseded); that sequence numbers rise and are never reused; and that a superseded record is still
there and refers to the record that replaced it[^nygard-adr]. The Thoughtworks Technology Radar
recommends keeping these records in source control beside the code[^tw-radar-adr], where such a check
can read them. The [Rule registry](rule-registry.html) uses the same pattern for the history of a rule.

### Release notes

The principles of a changelog and its types of change are set out on [Release](release.html), and the
drafting of notes for a candidate on [Release readiness](release-readiness.html). The parts a tool can
check come from Keep a Changelog's 2.0.0 edition: an entry for every version, latest first; a release
date for each version in the form YYYY-MM-DD; an Unreleased section at the top; changes grouped by
type; and a yanked release listed rather than hidden[^keep-a-changelog-2]. The version number follows
whatever scheme the project states; the edition says a project does not have to use Semantic
Versioning[^keep-a-changelog-2]. Where a project does, a released version is never modified, and any
change ships as a new version[^semver]. As recommended practice, each entry also links to the changes it
describes, which places the notes on the traceability spine.

### What a shape check decides

A check of a template decides presence and form, never whether the content is right: it can find an
empty security section, not judge the requirements in it. The
[Specification](specification.html#gates-and-evidence) page draws the same line. The kit's
[Validators](validators.html) do this work. As recommended practice, a template is strict when a
document is written and tolerant when an older document is read, as
[Versioning the schema](evidence-schema.html#versioning-the-schema) describes for evidence records.

### Versioning templates with the kit

Templates are files the kit owns, so they change only in a kit release, under the reading of Semantic
Versioning set out in [Versioning](engineering-kit.html#versioning). Applied to templates, as
recommended practice: adding a required part makes previously valid documents invalid, as a newly
required property does under JSON Schema[^json-schema-object], so it is a major change, and so is
removing or renaming one; adding an optional part is minor. A released template version is not
edited; any change becomes a new version[^semver].

Each document names the template version it was written under and is read by that version, as an
evidence record is read by its schema version; it is never rewritten into a newer one. A project's
edit to a kit-owned template comes to light at the next upgrade, whose release notes say why each
kit-owned file changed ([Upgrading a project](engineering-kit.html#upgrading-a-project)).

### The customer-record export

The site's running example is a hypothetical feature that lets application users export customer
records. Two rules from the [Rule registry](rule-registry.html) apply to it: the access rule R-042,
under which an identity may export only the customer records it may read, and the volume-limit rule
R-017. The specification template bears on the export's specification in three ways.

First, the open question. The specification does not at first say which roles may export which
records, the question R-042 turns on, and it is recorded as open and settled before planning
([Specification](specification.html#ai-assisted-practice)). Held as a marker in the place the template
gives open questions, rather than answered by a guess, it is something a tool finds, and the readiness
decision on [Specification readiness](spec-readiness.html) sees it.

Second, the identifiers. Once settled, the criterion on who may export which records has its own
identifier, which the tasks and tests written for it carry, while the access validator and the
50k-row load scenario carry R-042 and R-017. When the first pull request fails because a background
worker's query reads more records than the caller may see, the failure leads back through those
identifiers to the criterion it breaks.

Third, what the template does not hold. Later, in a hypothetical production incident, a scheduled full
export within R-017's limit, but far larger than the 50k-row scenario, times out, and afterwards the
readiness check asks every export-like specification for the largest export it expects
([Definition of Ready and Done](definition-of-ready-and-done.html#the-export-example)). Whether that
question also becomes a part of the specification template is a decision for the kit. As recommended
practice, it would arrive in a kit release, and as a required part it would be a major change under
the versioning described above.

## Where it sits on the map

The box "Templates: spec, plan, ADR, release notes" sits in the assurance band, which covers what must
be provable, in its "Evidence & traceability" column. The documents are written in the lifecycle band:
in [Specification](specification.html), [Design](design.html) and [Release](release.html). The core
band carries the templates as files of the [Engineering Kit](engineering-kit.html), beside the
[Evidence schema](evidence-schema.html). Assurance reads the filled documents when it checks a change
or audits a release, following their identifiers along the
[Traceability spine](traceability-spine.html). Toolkits for
[spec-driven development](glossary.html#spec-driven-development) that generate the documents belong to
the enablement band.

## Pitfalls

- **Nothing is marked required.** The outline lists parts, but none is required, so an empty
  document passes[^json-schema-object]. Sign: a template whose schema names properties and no
  required ones.
- **A shape check read as a content check.** A document passes every structural check and is treated
  as correct. Sign: a reviewer finds that a fully formed specification asks for the wrong behaviour,
  after it has been planned from.
- **A decision record edited in place.** A reversed decision is rewritten instead of being kept and
  marked superseded[^nygard-adr], so the earlier reasoning is lost. Sign: an accepted record whose
  decision text has changed, with no superseding record.
- **A template changed without a new version.** Sign: two documents that claim the same template
  version but have different required parts[^semver].
- **Each project keeps its own copy.** Templates drift until documents from different teams cannot be
  compared. Sign: comparing two teams' specifications needs someone to translate one layout into the
  other.

Release notes drawn from the commit log, and agent drafts published unread, are covered under the
pitfalls on [Release](release.html#pitfalls).

## Related

- [Specification](specification.html) and [Specification readiness](spec-readiness.html): writing
  the specification and judging it ready.
- [Design](design.html) and [Design conformance](design-conformance.html): plans, decision records
  and the check of one against the other.
- [Release](release.html) and [Release readiness](release-readiness.html): changelog principles and
  drafting release notes.
- [Definition of Ready and Done](definition-of-ready-and-done.html): readiness criteria.
- [Traceability spine](traceability-spine.html): identifiers linking documents to tasks, tests and
  results.
- [Engineering Kit](engineering-kit.html): the package that carries and versions the templates.
- [Evidence schema](evidence-schema.html): the fixed, versioned record templates resemble.
- [Rule registry](rule-registry.html): rule history in the decision-record pattern.
- [Validators](validators.html): the deterministic checks that confirm a document's shape.
- Terminology: [Architecture decision record](glossary.html#architecture-decision-record) and
  [Spec-driven development](glossary.html#spec-driven-development).

## Sources

- Required and additional properties in a schema: JSON Schema's reference for the object
  type[^json-schema-object].
- Decision records: Michael Nygard[^nygard-adr] and the Thoughtworks Technology Radar[^tw-radar-adr].
- Changelogs and version numbers: Keep a Changelog 2.0.0[^keep-a-changelog-2] and Semantic
  Versioning 2.0.0[^semver].
- Specifications: the ISTQB glossary on acceptance criteria and
  testability[^istqb-acceptance-criteria][^istqb-testability], NIST's Secure Software Development
  Framework[^nist-ssdf], and an open-source spec-driven toolkit and its description of the
  method[^spec-kit][^spec-kit-sdd].
- The vocabulary of deterministic checks: Birgitta Böckeler on computational and inferential
  sensors[^bockeler-sensors].
- This site's recommended practice, which no public source states: the term delivery template; a
  place for security requirements and open questions in every specification template, with a
  statement in the security part when none applies; an identifier for each acceptance criterion; the
  plan template's minimum; shape checks as checks of form only; links from release-note entries to
  their changes; strict writing with tolerant reading; and versioning templates by Semantic
  Versioning, including how a new required part such as the largest-export question would ship.
