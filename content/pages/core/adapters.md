---
id: adapters
type: concept
band: core
map_box: Engineering Kit · adapters
title: Adapters
summary: The thin layer that binds an Engineering Kit's core to each tool it runs against, so that its rules, validators and evidence schema depend on no one product.
key_terms: [adapter, ports-and-adapters, anticorruption-layer, contract-test, consumer-driven-contract, engineering-kit, validator, evidence-record, could-not-run, mechanism-vs-meaning, harness, export-example]
sources: [cockburn-hexagonal, evans-ddd-reference, bockeler-harness, bockeler-sensors, twelve-factor-backing-services, twelve-factor-parity, mcp-spec, openapi-spec, fitness-function, openai-harness, robinson-cdc, fowler-contract-test, fowler-ci, thoughtworks-pipelines-as-code, junit-assumptions, github-protected-branches, semver, thoughtworks-generic-cloud]
related: [engineering-kit, validators, evidence-schema, workflows, harness-engineering, rule-registry]
review_record: content/reviews/1.4.0-core.md
---

## Definition

An adapter is the thin binding between an Engineering Kit's core and one tool the kit runs
against: the execution surface where the coding agent works, the change host where the pull
request lives, the pipeline runner where checks run unattended, the work tracker, or a tool server
the agent calls. The core holds what the team means: its rules, its validators and its evidence
schema. The adapter holds only what it takes to talk to one product. The idea comes from Alistair
Cockburn's ports and adapters pattern, also called hexagonal architecture, in which a
technology-specific adapter turns whatever arrives at a port into a call the application
understands, so the application does not depend on the device on the other side[^cockburn-hexagonal].
Using "adapter" as the name of one layer of a kit is this site's own usage. The test of an adapter
is how little is in it.

## Why it matters

In an AI SDLC (the software development lifecycle with AI agents doing part of the work), the same
checks have to run wherever the work happens: on a developer's machine, inside the agent's
execution surface, and in the pipeline that guards the merge. A kit that calls one product's
interface from inside its rules is tied to that product's release cycle and vocabulary. When the
product changes its interface, or the team moves to another, the rules have to be rewritten, and
results differ between environments while that work is under way.

Cockburn's motivating problem applies directly. A layer that is promised to hold no business logic,
with nothing in place to detect a breach of that promise, collects business logic over the years,
and logic in the wrong layer can no longer be exercised by automated test suites[^cockburn-hexagonal].
Domain-driven design describes the same risk between models: without an isolating layer, another
system's model can gradually reshape the model that uses it. Eric Evans's anticorruption layer
talks to the other system through its existing interface and translates in both directions, so the
other system's concepts stay outside[^evans-ddd-reference]. For a kit, the outside model is a
tool's own idea of a check, a status, a work item or a permission.

A tool-free core also keeps the harness portable. The tools an agent can call are part of its
harness[^bockeler-harness], and a team's choice of tools changes over time. A kit whose meaning sits
in the core follows those changes by swapping bindings, not by re-deriving its rules. The
Twelve-Factor App makes the parallel point about backing services: code that treats each outside
service as an attached resource can exchange one for another through configuration, without code
changes[^twelve-factor-backing-services].

## How it works

### The bindings a kit needs

No public source lists the bindings an agent engineering kit needs; the list below is recommended
practice. A kit ships one adapter per tool the team uses, not a fixed set.

- **Execution surface.** Installs the kit's guidance and commands in the form the surface loads,
  and lets the agent run the same `verify` command a person runs.
- **Change host.** Reads the change and its metadata, posts each result as a check on the pull
  request, and links the report behind it.
- **Pipeline runner.** Runs the kit's commands unattended, with the same inputs as a local run, and
  collects the evidence record the run produces.
- **Work tracker.** Reads and writes the few work-item fields the kit relies on, such as the link
  between a change and the item it serves.
- **Tool servers.** Connect the agent to capabilities published over an interface. The Model
  Context Protocol is one example: an open protocol in which servers offer tools, resources and
  prompts to client applications using JSON-RPC 2.0 messages[^mcp-spec]. An HTTP API described in
  the OpenAPI Specification, a language-agnostic description of what a service offers, is
  another[^openapi-spec].

### What goes in an adapter, and what stays in the core

The split follows the difference between mechanism and meaning. It is recommended practice, resting
by analogy on Cockburn's and Evans's patterns.

| Stays in the core | Goes in an adapter |
|---|---|
| Rule identifiers, routes and owners (the rule registry) | Endpoints, authentication calls and rate-limit handling |
| Validator logic and the results it returns | Translating the tool's input into the core's interface |
| The evidence schema and what each field means | Translating the core's results into the tool's vocabulary: a check, a status, a comment |
| The four results a check can report: passed, failed, skipped and could_not_run | Packaging the kit in the form the tool loads |

Validators are deterministic checks of the kind Birgitta Böckeler calls computational
sensors[^bockeler-sensors], and they belong in the core. The adapter passes on what validators
return and adds no verdict of its own. It also does not restate a machine-checkable rule as text
for a model to read, since only the validator gives the same answer on every run. Once a rule lives
in a binding, replacing the tool means rewriting the rule.

The boundary is enforced by a check, not by a convention. An architecture rule can be written as an
executable test[^fitness-function], for example a test that fails when any module in the core imports
from an adapter. One model vendor's account of harness engineering describes enforcing
architectural constraints through automated checks in the same way[^openai-harness]. Cockburn's
observation that an unguarded boundary erodes is the reason for making it a check.

Every adapter follows an interface that its owners do not control and has to keep up with it, so,
as recommended practice, a team writes one only for a tool it actually uses and only where
configuration cannot express the need. An integration the tool's users already publish can serve
as the adapter, provided it passes the same contract suite as one the team writes itself.

### How an adapter is tested

Testing follows the same split. The recommended practice below builds on two public patterns.
Ian Robinson's consumer-driven contracts have each consumer of a service state its expectations as
tests that the provider runs, so the provider can change without breaking any of its
consumers[^robinson-cdc]. Martin Fowler's contract test checks that a test double still answers the
way the real outside service does; it runs apart from the main build, at the pace the outside
service changes, and a failure starts work to bring the two back into line rather than necessarily
breaking the build[^fowler-contract-test]. Applied to a kit:

- **One contract suite per binding.** The core states what it expects of any change-host adapter,
  any pipeline-runner adapter and so on, as tests against the core's interface. Every adapter for
  that binding must pass the same suite.
- **A double in the fast checks, the real tool in the contract run.** Checks on the adapter's own
  changes use a double of the tool, so they stay quick and repeatable. The contract run against the
  real tool happens separately, as Fowler describes, and shows when the double has stopped matching.
- **The tool's own failures.** The suite includes runs in which the tool is unreachable or answers
  with an error, and the adapter must report could_not_run with that cause, never failed and never
  passed.

A code-coverage target set for the core fits an adapter poorly. Most of an adapter's lines call a
tool that the fast checks replace with a double, so a high percentage there mostly measures the
double. The measure for an adapter is whether it passes its binding's contract suite, failure runs
included. An adapter that needs many tests of its own to reach a target has usually taken on logic
that belongs in the core. This is recommended practice.

### The same result locally and in CI

Continuous integration expects anyone to be able to check out the sources on a clean machine and
build and test the system with one command, and the same build to run after every push to the
mainline[^fowler-ci]. The Thoughtworks Technology Radar places pipeline configuration treated as
code, kept under source control and tested like any other code, in its Adopt
ring[^thoughtworks-pipelines-as-code]. For a kit, the
pipeline-runner adapter calls the same `verify` a developer runs. It adds scheduling and reporting,
never extra checks or different thresholds, so a difference between a local result and a pipeline
result points at the environment, not at the rules. Adapters do not remove every difference: the
Twelve-Factor App warns that even when adapters appear to hide the differences between backing
services, small incompatibilities let code pass in one environment and fail in another[^twelve-factor-parity].
That is why the contract run against the real tool stays.

### Versions, replacement and synchronisation

An adapter is versioned and released separately from the core, and states the range of core
versions it works with. Semantic Versioning makes such a range readable, because a new major
version marks an incompatible change to a declared public interface[^semver]. When the core or the
tool changes its interface, the contract suite shows whether the adapter still holds. Replacing a
tool means writing a new adapter, passing the same contract suite, and switching. Rules, validators
and schema stay as they are; that is the design intent of the layer, not a measured result.

An adapter that keeps two systems in step, such as the repository and the work tracker, first
settles which system owns each field and copies that field in one direction only. Where a field
can still be edited in both places, a clash goes to a person rather than being settled
automatically, because keeping whichever edit is newer silently throws the other one away. This is
recommended practice.

### Reporting that a tool could not run

Test frameworks already keep "could not run here" apart from "failed": in one widely used
framework, a test whose assumption about the runtime environment does not hold is aborted rather
than failed.[^junit-assumptions] Change hosts, however, have their own list of check states, and
the adapter has to choose one. It never chooses success, and it avoids any state the host treats
as satisfying a required check: at least one change host accepts a skipped or neutral required
check as passing.[^github-protected-branches] So, as recommended practice, the adapter posts
could_not_run in a state that is not successful, names the cause in the check's summary, and links
the evidence. What that state means for the merge is decided in the assurance band of the map.

On the pull request, the change-host adapter posts each check's result, with a link to that
check's evidence, and alongside them the overall status that the evidence record carries. The
adapter computes neither: validators produce the results and the evidence record derives the
overall status. A check new to the team is posted as report-only at first, so its results are
visible without holding changes, and is marked required later. The adapter posts the same result
in both stages; only the label the change host attaches to it differs.

### The running example

The customer-record export arrives as a pull request. The pipeline-runner adapter runs `verify`
unattended, and gets the same result a developer gets locally: the validator for R-042, the access
rule on which identities may export which records, fails because a background worker queries more
records than the requesting user may see. The change-host adapter posts that failure as a check on
the pull request and links the validator's report. The runner image lacks the load-test tool, so
the 50k-row load scenario for R-017, the volume-limit rule, cannot start. The adapter posts that
check as not successful, with could_not_run and the missing tool as its cause, rather than dropping
it or showing it as passed, and posts the record's overall status of blocked beside the two checks.
If the team later moves to another change host, only the change-host adapter is rewritten and
passed through the same contract suite. R-042, R-017, their validators and the evidence schema do
not change.

## Where it sits on the map

Adapters sit in the core band, the part of the map that does the work, inside the Engineering Kit
box as one of its five parts alongside the rule registry, validators, skills with evals and the
evidence schema. Within the kit's four layers (shared core, technology profiles, tool adapters and
project configuration), adapters are the layer that faces outward. On one side are the rules,
validators and schema they carry without changing. On the other side are the tools themselves, the
execution surface, change host, pipeline runner, work tracker and tool servers, whose choice and
configuration belong to the enablement band. So do the permissions and secrets an adapter uses,
which follow the usual rule for automation: each automated actor has its own machine identity with
no more access than its job needs. Adapters also carry the evidence record to the pull request,
where a workflow's human decision is taken, and the assurance band reads the same results to decide
whether a change may merge or release.

## Pitfalls

- **Rules in the binding.** A rule or threshold is written into an adapter, and replacing the tool
  would change what is enforced. Sign: a rule change needs an adapter edit, or two adapters give
  different results for the same change.
- **An adapter that grows a validator.** The adapter starts to judge the product instead of
  translating. Sign: the adapter has tests about product behaviour, or it becomes the subject of
  coverage arguments.
- **A lowest-common-denominator core.** The core's interface is cut down to what every tool
  supports. Thoughtworks places generic cloud usage on Hold for the same reason in a different
  setting: avoiding lock-in at all costs gives up each provider's distinctive
  benefits[^thoughtworks-generic-cloud]. The comparison is an analogy. Sign: a core capability waits
  for the least capable tool.
- **Absence read as a pass.** A tool is missing and the check quietly disappears. Sign: a check
  vanishes from the pull request after a runner image change, or skipped results rise with no
  stated cause.
- **Local and pipeline results drift apart.** The pipeline defines steps of its own. Sign: changes
  pass locally and fail in the pipeline with no code difference.
- **Doubles that no longer match the tool.** The contract suite runs only against doubles. Sign:
  the first sign of a tool's interface change is a failure reported by users.
- **Silent upgrades.** An adapter says nothing about which core versions it works with. Sign: it
  breaks after an upgrade on either side and nobody is sure who fixes it.
- **A sync adapter that settles clashes by itself.** Conflicting edits are resolved by whichever
  came last. Sign: a value in the tracker changes and nobody reviewed the change.
- **The same fix copied from project to project.** Each project patches its tool binding for
  itself. Sign: several near-identical patches, no two quite the same, and no agreed version.

## Related

- [Engineering Kit](engineering-kit.html): the package adapters belong to, its layers and its
  commands.
- [Validators](validators.html): the deterministic checks adapters run and report, including how a
  validator reports that it could not run.
- [Evidence schema](evidence-schema.html): the fixed shape of the record adapters carry to the
  change host, including the overall status it derives.
- [Rule registry](rule-registry.html): the identifiers adapters pass through unchanged.
- [Workflows](workflows.html): the unit of work whose checks and decisions adapters connect to real
  tools.
- [Harness engineering](harness-engineering.html): the discipline the kit and its adapters serve.
- [Terminology: adapter](glossary.html#adapter) and the
  [workflow catalog](workflow-catalog.html).

## Sources

The adapter idea is Alistair Cockburn's ports and adapters pattern[^cockburn-hexagonal], with Eric
Evans's anticorruption layer as the related domain-driven design pattern[^evans-ddd-reference]. The
place of tools in the harness follows Birgitta Böckeler[^bockeler-harness], and validators as
computational sensors follow her worked examples[^bockeler-sensors]. Testing draws on Ian Robinson's
consumer-driven contracts[^robinson-cdc] and Martin Fowler's contract test[^fowler-contract-test];
local and pipeline parity on Fowler's account of continuous integration[^fowler-ci], the Thoughtworks
Technology Radar on pipelines as code[^thoughtworks-pipelines-as-code] and the Twelve-Factor App on
parity and backing services[^twelve-factor-parity][^twelve-factor-backing-services]. Enforcing the
boundary draws on fitness functions[^fitness-function] and one model vendor's account of harness
engineering[^openai-harness]. Version ranges follow Semantic Versioning[^semver]. Tool-server
interfaces cite their own specifications[^mcp-spec][^openapi-spec]; the aborted-versus-failed
precedent cites its framework's documentation[^junit-assumptions]; the behaviour of skipped
required checks cites one change host's documentation[^github-protected-branches]; the lock-in analogy cites the
Radar[^thoughtworks-generic-cloud]. The list of bindings, the split between core and adapter, the
contract-suite approach in place of coverage targets, one-way field ownership in synchronisation and reporting could_not_run
through the change host are recommended practice with no public source that states them for kits.
