---
id: engineering-kit
type: concept
band: core
map_box: Engineering Kit
title: Engineering Kit
summary: A versioned, installable package of the environment a team's people and coding agents work inside (rule registry, validators, skills with evals, evidence schema and adapters), organised in four layers and run through three commands, init, doctor and verify.
key_terms: [engineering-kit, technology-profile, project-configuration, harness, harness-template, rule-registry, rule-route, validator, skill, review-skill, harness-evaluation, evidence-record, adapter, could-not-run, mechanism-vs-meaning, deterministic-gate, gate, guides-and-sensors, workflow, software-factory, golden-path, export-example]
sources: [bockeler-harness, bockeler-sensors, cncf-platforms, dora-platform-engineering, fowler-ci, fowler-selftesting, dora-test-automation, npm-doctor, homebrew-doctor, flutter-doctor, sarif-2-1-0, python-unittest, github-protected-branches, semver, cockburn-hexagonal, spotify-golden-paths]
related: [rule-registry, validators, skills-and-evals, evidence-schema, adapters, harness-engineering, workflows, software-factory]
review_record: content/reviews/1.4.0-core.md
---

## Definition

An Engineering Kit is a versioned, installable package of the engineering environment that a
team's people and coding agents work inside. It holds five parts: a rule registry, validators,
skills with their evaluation sets, an evidence schema and adapters. It also holds the commands that
install the kit, check that its prerequisites are present and run its checks. The package is
organised in four layers: a shared core that every project receives unchanged, technology profiles
for each supported stack, tool adapters that bind the kit to the tools a team uses (adapted from
Alistair Cockburn's ports and adapters pattern[^cockburn-hexagonal]), and project
configuration, where one project states what the rules mean for it. "Engineering Kit" is a working
name coined by this site, not an industry term. Two established ideas sit close to it. Platform
engineering treats an internal platform as a product: an integrated set of capabilities offered to
the teams that use it and designed and evolved around their needs.[^cncf-platforms] Birgitta
Böckeler calls everything in a coding agent except the model its harness.[^bockeler-harness] The
kit is the part of that harness a team can package once and install in every repository.

## Why it matters

In an AI SDLC (the software development lifecycle with AI agents doing part of the work), every
repository where a coding agent works needs the same things around it: instructions the agent loads, checks that run on what it
produces, a record of what ran, and connections to the pipeline and the change host. The easy way
to provide them is to copy configuration files from one repository to the next. Copies drift. A fix
made in one repository reaches no other. Two machines run slightly different versions of the same
check, so results differ with nothing to explain why. After a few months nobody can say which
version of the rules a repository follows, and the evidence for a merged change cannot name the
controls that applied to it.

Platform engineering answers the same problem for infrastructure. The CNCF platforms white paper
lists "golden path" templates and documentation among a platform's capabilities (the term is associated
with Spotify Engineering's account of reducing tooling fragmentation[^spotify-golden-paths]), and gives as its
goals reducing the cognitive load on product teams and reusing platform tools and knowledge across
many teams.[^cncf-platforms] DORA describes platform engineering in similar terms: shared tools,
services and golden paths, run as an internal product whose customers are
developers.[^dora-platform-engineering] Packaging the harness in the same way gives a team one
version to name in every evidence record, one install path for people and agents, one upgrade path
for every repository, and one place where a fix is made and then shipped. No public study compares
packaged and copied harnesses, so these benefits are recommended practice, not a measured finding.

## How it works

### The five parts

Each part has a page of its own. The table summarises them with the site's running example, a
feature that lets users export customer records. Two rules from that example appear throughout.
R-042 is the access rule: an identity may export only the customer records it may read. R-017 is
the volume-limit rule, which caps the number of rows one export may return.

| Part | What it holds | In the export example |
|---|---|---|
| [Rule registry](rule-registry.html) | Every rule, each with a stable identifier, a statement, a route (gate, judgment or guidance), an owner and its known gaps | R-042 is routed to a gate. R-017's limit is a gate, and a request to exceed it goes to judgment |
| [Validators](validators.html) | Deterministic checks as code, tied to rule identifiers, that report passed, failed, skipped or could_not_run | The access validator fails on a background worker whose query reads more records than the caller may see |
| [Skills with evals](skills-and-evals.html) | Guidance the agent loads when a task calls for it, shipped with scenario evaluations run repeatedly and recorded | An access-rule skill supports R-042. Its evals check that the agent stops and asks when the access rule is unresolved |
| [Evidence schema](evidence-schema.html) | The fixed, versioned shape of what each run records, with one kind of writer per field | The record shows R-042 failed, R-017 could_not_run and an overall status of blocked |
| [Adapters](adapters.html) | Thin bindings to the execution surface, change host, pipeline runner, work tracker and tool servers | The change-host adapter posts the R-042 failure on the pull request with a link to its report |

The parts depend on one another through identifiers. The registry is the connecting structure:
validators name the rules they enforce, skills name the rules they support, and evidence records
name the rule checks that ran. In Böckeler's vocabulary, validators are computational sensors and a
review skill, an agent that reads a change against the rules and proposes findings without
blocking, is an inferential sensor.[^bockeler-sensors] Skills themselves are guides, which steer
the agent before it acts.[^bockeler-harness]

### Four layers

The five parts say what a kit contains. The four layers say who may change what.

| Layer | What it holds | Who changes it |
|---|---|---|
| Shared core | The commands, the evidence schema, the result states, the rule-identifier scheme, and rules and validators that apply to every stack | The kit's maintainers, through a versioned release |
| Technology profiles | Validators, pinned tool versions, skills, scaffolds and default thresholds for one supported stack | The kit's maintainers, with the teams on that stack |
| Tool adapters | One binding per tool the kit runs against | The kit's maintainers, or a team that uses a tool nobody else does |
| Project configuration | Which rules apply, their thresholds, declared exceptions, the chosen profile and adapters | The project |

Each layer may narrow or supply values for the layer above it, and none may redefine it. As
recommended practice, a change is made in the layer closest to the project that can hold it, so
that the parts every project shares change as seldom as possible.

### Technology profiles

A technology profile packages what one stack needs: the validators that suit it, the tool versions
they run with, the skills and scaffolds its agents use, and default thresholds. A web-application
profile might carry a dependency-rule checker configured for its layers, an access-test pattern for
its request handlers, a load-test tool at a pinned version, and a skill for its data-access
conventions.

Böckeler proposes a similar bundle, which she calls a harness template: a set of guides and sensors
that ties a coding agent to the structure, conventions and technology stack of one common service
topology. She notes that organisations often codify those topologies already, in service templates,
and that such templates might grow into harness templates, so the idea is a proposal rather than an
established practice.[^bockeler-harness] A technology profile is one form of that idea, with a rule
registry and an evidence schema underneath it. A profile adds rules and checks for its stack. It
does not change what the shared core's rules mean, and it carries no one project's choices.

### Project configuration

Project configuration is a committed file in the project's repository, reviewed like code. It is
where the project supplies meaning. The kit supplies mechanism: a test pattern, a runner, a rule
identifier, a result format. This site calls the split mechanism versus meaning. A kit can ship an
access-test pattern, but it cannot know which identities may export which records; only the project
knows that.

| A project may | A project may not |
|---|---|
| Declare which rules from the registry apply, and which checks run for each kind of change | Change the evidence schema or add a field the overall status depends on |
| Set thresholds within the bounds the core or profile allows | Redefine what passed, failed, skipped or could_not_run means |
| Record an exception against a rule identifier, with an owner, a reason and an expiry | Waive a rule the registry marks as never open to exception, such as the access rule R-042 |
| Choose its technology profile and its adapters | Count could_not_run as passed, or a missing result as a pass |
| Add project rules, with identifiers of their own | Reuse or renumber an identifier the registry already holds |

The fixed evidence schema is what makes this safe. Records from every project share one shape, so
they can be compared, aggregated and audited across teams, as the
[Evidence schema](evidence-schema.html) page explains. No public source states these limits for an
engineering kit; they are this site's recommended practice.

In the export example, the project configuration names the web-application profile. It declares
that R-042 and R-017 apply to the export feature, and it sets the row limit that R-017 enforces.

### The kit's commands: init, doctor and verify

A kit is used through a small set of commands. The names are this site's and the verbs are common
vocabulary. They belong to the kit's fixed interface: every project uses the same three, and no
project renames them.

**`init`** installs the kit into a repository. It takes a technology profile and a list of adapters,
writes the kit-owned files (the ones the kit will later upgrade), writes a starting
project configuration, and records the kit version and a list of every file it installed. That list
is what makes a later upgrade safe: it separates the files the kit may replace from the files the
project owns. `init` then runs `doctor` and one `verify` as a first check that the install works.

**`doctor`** checks, on the machine where it runs, that everything the project's checks need is
present: the tools a profile pins, at their pinned versions; the services and test environments the
checks call; the credentials each adapter needs, without printing them; a valid project
configuration; and kit-owned files that match the installed release. It runs no checks. It reports
each missing prerequisite together with the checks that will return could_not_run because of it, and
it exits with a failure status when anything required is missing. Environment self-checks of this
kind are an established convention in developer tooling: several package managers and software
development kits ship a command, commonly called doctor, that inspects the local installation and
reports what is missing or broken. At least one of them exits with a non-zero status when it finds a
problem.[^npm-doctor][^homebrew-doctor][^flutter-doctor] The recommended practice is to run `doctor`
when a machine or runner image is set up, and again as the first step of every pipeline run, so that
a missing tool is reported by name before any check depends on it.

**`verify`** runs every check that the project configuration declares for the change, and writes one
evidence record in the kit's schema. It is the same command everywhere: on a developer's machine,
inside a coding agent's session and in the pipeline. The pipeline-runner adapter calls it and adds
scheduling and reporting, never checks or thresholds of its own. Continuous-integration practice
rests on the same idea. Developers run the self-testing build on their own machine before they
integrate, and the integration build runs it again.[^fowler-ci] Martin Fowler describes self-testing
code as tests that a single command runs, giving confidence that they will expose the bugs in the
code.[^fowler-selftesting] DORA's guidance on test automation expects feedback from automated tests
in less than ten minutes, both on local workstations and from the continuous integration
system.[^dora-test-automation] When `verify` is one command with one set of inputs, a difference
between a local result and a pipeline result points at the environment, not at the rules.

In the export example, the team runs `init` with the web-application profile and adapters for its
change host and pipeline runner. Later, `doctor` on the pipeline's runner image reports that the
load-test tool is missing and names the 50k-row load scenario for R-017 as the check it affects.
When `verify` runs on the pull request, the access validator reports R-042 as failed, because the
background worker's query reads records outside the caller's scope. The load scenario reports R-017
as could_not_run, citing the missing tool. It is neither skipped nor passed.

### The could_not_run result

Every check the kit runs ends in exactly one of four results. Could_not_run is the one that most
setups lack.

- **passed**: the rule was evaluated against the change and held.
- **failed**: the rule was evaluated and a violation was found. The change is at fault.
- **skipped**: the rule does not apply to this change, decided from a declared condition.
- **could_not_run**: the rule applies and the check was required, but no verdict was produced,
  because a tool was missing, an environment was unavailable, the run timed out after its retry, or
  the tool crashed.

Could_not_run is a result of its own because each result needs a different response. A failure goes
back to the change's author. Could_not_run goes to whoever owns the environment, since the change
may be fine. Skipped needs no response at all. If could_not_run is folded into failed, developers
chase defects that are not there. If it is folded into skipped, the check silently disappears: at
least one change host treats a skipped required check as satisfied,[^github-protected-branches] so a
broken runner would let changes merge unchecked. If it is folded into passed, the evidence says
something that did not happen.

The distinction is established even though the name is coined. SARIF, the OASIS standard format for
static-analysis results, records whether the tool's execution completed successfully apart from the
results it reports, and records conditions that concern the tool itself as notifications, kept
separate from results about the code.[^sarif-2-1-0] One widely used language's standard unit-testing
framework lists errors (tests that raised an unexpected exception), failures (tests where an
assertion signalled a problem) and skipped tests separately.[^python-unittest] The name
could_not_run is this site's own.

The kit defines the result and makes every part report it the same way. Validators detect a missing
prerequisite before they evaluate anything, adapters carry the result to the change host without
turning it into a pass, and the evidence schema gives it a status of its own that prevents a
positive overall status, as a failure does. What each result means for a merge or release decision
is set in the assurance band of the map, not by the kit.

### What an installation must prove

An installed kit is only useful once a team can rely on its results. No public source sets out what
an installation must demonstrate, so the following is recommended practice. Before a team treats the
kit's results as evidence, the installation shows that:

- the kit version is pinned and recorded, and every kit-owned file matches that release;
- `doctor` passes on every place `verify` runs: developer machines, the agent's execution surface
  and each pipeline runner image;
- `verify` gives the same results for the same revision locally and in the pipeline;
- every rule the project configuration declares has a check that actually runs, so no declared rule
  is left without a check;
- each validator's known-bad example fails and its known-good example passes in this repository,
  which shows the checks can catch what they are meant to catch;
- a deliberately removed prerequisite produces could_not_run, not skipped or passed;
- a run produces an evidence record in the kit's schema, and the change-host adapter shows its
  results on a pull request;
- the identities the agent and the pipeline run under have only the permissions the adapters need.

In the export example, the installation is not proven until the missing load-test tool is either
added to the runner image or recorded as a known gap with an owner. Until then R-017 cannot be
evaluated, and the record says so.

### Versioning

A kit is a dependency of every repository that installs it, so it is versioned like one. Semantic
Versioning uses a major version for incompatible changes, a minor version for backward-compatible
additions and a patch version for backward-compatible fixes, and it requires software that uses it
to declare a public API.[^semver] A kit can follow it by treating as its public API its rule
identifiers and what they mean, its evidence schema, its commands and their results, and the format
of its project configuration. That application is this site's recommended practice, not something
Semantic Versioning itself states.

Read that way, the rule is simple: anything that can turn an unchanged project red is a major
change. A new rule whose validator starts in report-only mode, a new technology profile or a new
optional evidence field is a minor change. A corrected check that stops a false alarm is a patch.
Switching a rule's validator from report-only to required in the kit's defaults, or tightening a
default threshold, can
fail a project that changed nothing, so it goes into a major release. The evidence schema
carries a version of its own, which every record declares, because records outlive the kit release
that wrote them.

### Upgrading a project

Each project pins a kit version and moves to a newer one on purpose; it never follows the latest
release automatically. As recommended practice, an upgrade is a pull request like any other, and
its review answers two questions. The first is what the kit changed: the diff shows each kit-owned
file the new version replaces, and the release notes say why. The second is whether the project's
results changed: `doctor` and `verify` run on the pull request, and the new evidence record is read
beside the last one made under the old version. A difference that the release notes do not explain
is resolved before the upgrade merges. Once it merges, every evidence record names the new version,
so results from before and after it are never confused.

The list of installed files also shows when a project has changed a file the kit owns. As
recommended practice, the upgrade stops at such a file and shows the local edit, rather than
overwriting it or quietly keeping it. The edit is worth reading, because a project seldom patches a
kit file without a reason. Usually it needs a setting that project configuration does not offer, or
a fix the kit has not shipped yet. The kit's maintainers add the setting, so the project can move
its change into its own configuration, or ship the fix, so the local copy can be dropped. An edit
that neither route can absorb suggests the file belongs to the project, not to the kit.

### Testing a change to the kit

A change to the kit reaches every repository that upgrades, so it is tested before it is released.
No public source describes testing an engineering kit, so this is recommended practice. The kit is
software, and its own pipeline treats it that way. Its commands have tests of their own. Each
validator the change adds or alters comes with a known-bad example that must fail and a known-good
example that must pass, the same pair an installation later proves in each repository. Skills in
the change run their evaluation sets, and adapters run their own test suites, as the
[Adapters](adapters.html) page describes.

The most telling test is an upgrade itself. The kit's maintainers keep a few sample repositories
whose results are already known, at least one for each technology profile, and every candidate
release is installed into them. A sample whose results change is either a defect in the release or
an incompatible change, and the versioning rules above decide which release it may go into.

### The smallest useful first release

A kit does not start with all five parts at full depth. The smallest first release worth installing
is the deterministic floor: a rule registry holding a handful of rules drawn from the team's own
recent incidents and review comments, validators for those rules, a `verify` that runs the same way
locally and in the pipeline, and the evidence schema. Skills come after it. Without the floor, a
skill's guidance has nothing to check it, and nobody can tell whether a rule held. The floor is this site's framing. Its ingredients, a
self-testing build that runs from one command locally and on every integration, are long-standing
continuous-integration practice.[^fowler-ci][^fowler-selftesting] Its validators begin in
report-only mode and become required checks once they have earned trust, as the
[Validators](validators.html) page describes.

## Where it sits on the map

The Engineering Kit is a box in the core band of the map, the band that does the work, and its five
parts are labelled inside it: [Rule registry](rule-registry.html), [Validators](validators.html),
[Skills with evals](skills-and-evals.html), [Evidence schema](evidence-schema.html) and
[Adapters](adapters.html). The band reads as one row: Harness engineering, then the Engineering
Kit, then Workflows, then Software factory. [Harness engineering](harness-engineering.html) comes
before the kit: it is the discipline that decides what goes into the kit, and the kit is the
artefact that discipline produces. [Workflows](workflows.html) come after it. They are the units of
delivery that draw on the kit: each one runs its checks through `verify` and leaves an evidence
record. [Software factory](software-factory.html) comes last: it is the operating state that
appears once many workflows share the kit's rules, evidence and feedback.

Outside the core band, the lifecycle band supplies the specifications and access rules that
become registry entries. The enablement band provides the execution surfaces, pipeline runners,
change hosts and tool servers that the adapters bind to, and the people who own the kit. The
assurance band reads the kit's results and records to decide whether a change may merge or release.
The adoption path decides when a team installs the kit and which workflow it builds first.

## Pitfalls

- **Copies instead of an install.** Kit files are copied between repositories by hand. Sign to
  watch: repositories with kit files but no recorded kit version, or the same file differing
  between repositories.
- **A profile that carries one project's meaning.** Thresholds or rules for one project are written
  into a technology profile. Sign: a profile change requested so that one project's build passes.
- **Configuration that reaches into the core.** A project setting changes what a result means or
  reshapes the evidence. Sign: comparing two projects' records needs a mapping between their fields.
- **could_not_run folded into skipped.** A missing tool shows up as a skipped check. Sign: skipped
  counts rise after a runner image changes, and nobody is told.
- **A verify that differs by place.** The pipeline defines checks or thresholds of its own. Sign:
  pipeline configuration that lists checks, or changes that pass locally and fail in the pipeline
  with no code difference.
- **A doctor nobody runs.** Prerequisites are checked only when a check fails. Sign: the first news
  of a missing tool is a could_not_run on a pull request, not a `doctor` report at setup.
- **Floating on the latest release.** Projects pick up new kit versions without an upgrade change.
  Sign: evidence records from the same week naming different kit versions with no recorded upgrade.
- **A breaking change in a minor release.** A default is tightened without a major version. Sign:
  projects that changed nothing go red after a minor upgrade.
- **Local edits to kit-owned files.** Projects patch the kit's files instead of configuring them.
  Sign: every upgrade reports the same edited files, and nobody asks the kit's maintainers for the
  setting those edits stand in for.
- **Skills before the floor.** The first release ships skills but no validators or evidence schema.
  Sign: rules whose only enforcement is a skill, and no record of which checks ran.

## Related

- [Rule registry](rule-registry.html): every rule with an identifier, a route and an owner, and how
  rules enter, change and retire.
- [Validators](validators.html): deterministic checks as code, how they report results, and the path
  from report-only to required.
- [Skills with evals](skills-and-evals.html): packaged guidance for the agent and the evaluation
  history it ships with.
- [Evidence schema](evidence-schema.html): the fixed shape of what each run records, and who writes
  each field.
- [Adapters](adapters.html): the thin bindings between the kit's core and the tools it runs against,
  and how they are tested.
- [Harness engineering](harness-engineering.html): the discipline that decides what the kit holds.
- [Workflows](workflows.html): the unit of delivery that runs the kit's checks and leaves its records.
- [Software factory](software-factory.html): the operating state that shared rules, evidence and
  feedback make possible.
- Terminology: [Engineering Kit](glossary.html#engineering-kit),
  [harness template](glossary.html#harness-template) and
  [could_not_run](glossary.html#could-not-run), with the [workflow catalog](workflow-catalog.html).

## Sources

- The harness, guides and sensors, and harness templates as a proposal per service topology:
  Böckeler.[^bockeler-harness]
- Validators as computational sensors and review skills as inferential sensors: Böckeler's worked
  examples.[^bockeler-sensors]
- Tool adapters: adapted from Cockburn's ports and adapters pattern.[^cockburn-hexagonal]
- The golden path as Spotify Engineering describes it.[^spotify-golden-paths]
- An internal platform as a product, golden path templates and reuse across teams: the CNCF
  platforms white paper[^cncf-platforms] and DORA on platform engineering.[^dora-platform-engineering]
- One build locally and in continuous integration, run from a single command, with fast feedback in
  both places: Fowler on continuous integration[^fowler-ci] and self-testing
  code[^fowler-selftesting], and DORA on test automation.[^dora-test-automation]
- Environment self-check commands in developer tooling, cited as examples of the category
  only.[^npm-doctor][^homebrew-doctor][^flutter-doctor]
- Tool execution recorded apart from results, and errors kept apart from failures and skips: the
  SARIF 2.1.0 standard[^sarif-2-1-0] and one unit-testing framework's documentation.[^python-unittest]
- A change host that counts a skipped required check as satisfied.[^github-protected-branches]
- Major, minor and patch versions against a declared public API: Semantic Versioning.[^semver]
- The four layers, the limits on project configuration, the command set, what an installation must
  prove, upgrading as a reviewed change, how an upgrade treats local edits to kit-owned files,
  testing a change to the kit and the deterministic floor as
  the first release are this site's recommended practice; no public source states them for an
  engineering kit.
