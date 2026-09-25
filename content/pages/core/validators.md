---
id: validators
type: concept
band: core
map_box: Engineering Kit · validators
title: Validators
summary: A validator is a deterministic check, written as code and tied to rule identifiers, that runs the same way locally and in CI, reports passed, failed, skipped or could_not_run, and can block a merge once it has earned trust.
key_terms: [validator, gate, rule-registry, rule-route, could-not-run, two-kinds-of-machinery, guides-and-sensors, review-skill, deterministic-gate, evidence-record, engineering-kit, export-example, fitness-function, mechanism-vs-meaning]
sources: [bockeler-harness, bockeler-sensors, openai-harness, fowler-ci, sarif-2-1-0, github-protected-branches, github-checks-api, gatekeeper-violations, k8s-validating-admission-policy, gitlab-ci-yaml, pytest-timeout, pytest-flaky, fowler-nondeterminism, google-flaky-tests, luo-flaky-2014, ford-evolutionary-architectures, thoughtworks-radar-fitness, fitness-function]
related: [rule-registry, engineering-kit, evidence-schema, skills-and-evals, adapters, harness-engineering, workflows]
review_record: content/reviews/1.4.0-core.md
---

## Definition

A validator is a deterministic check, written as code, that enforces one or more rules from a team's rule registry and names those rule identifiers in every result it reports. It behaves identically on a developer's machine, inside a coding agent's session and in continuous integration (CI). It returns one of four results: passed, failed, skipped or could_not_run. Once it has proved trustworthy, it can block a merge. The term is this site's adaptation of Birgitta Böckeler's computational sensor: a feedback control that is deterministic and fast, run by ordinary computation rather than by a model, in contrast to inferential controls such as AI code review.[^bockeler-harness][^bockeler-sensors] A validator usually wraps an existing tool, such as a linter, a type checker, a test suite or a dependency-rule checker. What turns the tool into a validator is the contract around it: the rule it answers to, the result it reports, and the same behaviour wherever it runs.

A validator differs from its neighbours in specific ways. A unit test checks that code does what its author intended, while a validator checks a rule the team has agreed on, and may use tests to do it. A linter is one possible engine inside a validator; on its own it has no rule identifier and no defined result for "could not run". A review skill, an agent that reads a diff against the rules and reports findings, is inferential: it proposes, and it cannot block.[^bockeler-sensors]

## Why it matters

In an AI SDLC (the software development lifecycle with AI agents doing part of the work), the volume of change rises faster than the capacity to review it. A rule that lives only in a guidance document or in a reviewer's memory is applied unevenly, and the unevenness grows with the volume. Böckeler separates computational controls, which are deterministic and fast, from inferential ones, which are slower, more expensive and less deterministic.[^bockeler-harness] Her worked examples treat computational sensors as cheap enough to run on every change, with inferential review kept for what deterministic tools cannot judge.[^bockeler-sensors] One model vendor's published account of harness engineering on a large codebase describes the same move: architectural constraints enforced through automated checks rather than through reminders.[^openai-harness] Every rule a machine can check the same way each time is one less thing a person has to remember to look for.

The contract around the check is what makes this safe. Without it, familiar failures follow. A check that behaves differently locally and in CI sends developers and agents after failures they cannot reproduce, whereas continuous-integration practice expects any developer to be able to run the mainline build on their own machine.[^fowler-ci] A check that reports a missing tool as "no findings" quietly removes a gate. A check that blocks before anyone trusts it gets bypassed or switched off. A flaky check teaches people to re-run until the result turns green.

## How it works

### One rule, one identifier

Each validator declares the rule identifiers it enforces, and each finding it reports carries the identifier of the rule it concerns. In the customer-record export, rule R-042 says that every query path serving an export filters by the records the caller is allowed to read. The access validator for R-042 reports each finding against R-042, with the file and query that break it. SARIF, the OASIS standard format for static-analysis output, keys results the same way: each result carries a `ruleId`, the stable identifier of the rule that was evaluated to produce it.[^sarif-2-1-0] The site recommends the link for three reasons. A finding leads straight to the rule's text and its owner. The registry can show which rules are enforced by a validator and which still depend on judgment. When a rule retires, the validators that enforce it are easy to find and retire with it.

Not every rule suits a validator. The test is whether a program can detect a violation and give the same verdict every time it runs on the same input. Rules about how code is arranged and what it may depend on usually pass: forbidden imports between modules, committed credentials, disallowed licences, interface schemas that must not break. Rules about purpose usually do not, and they stay with named people. In the export example, R-042 passes the test, because a program can find a query path that reads customer records without the caller's filter; whether the exported fields are the ones users actually need does not. A rule that passes the test is routed to a gate in the [Rule registry](rule-registry.html), and its validator is built next.

### The same run everywhere

A validator has one entry point, pinned tool versions and one configuration. The developer's machine, the agent's session and the CI pipeline all call that entry point; CI calls the check and never redefines it. The Engineering Kit's verify command runs a project's validators this way. The kit supplies the mechanism (the entry point, the four results and the report format), and the project supplies the meaning: which of its rules have validators, and what their limits are. Continuous-integration practice asks for a fast build that any developer can reproduce locally, and a validator inherits both expectations: fast enough to run on every change, and reproducible off the shared build.[^fowler-ci]

### Reporting the result

Every run ends in exactly one of four results, each tagged with the rule identifier:

- **passed**: the rule was evaluated against the change and no violation was found.
- **failed**: a violation was found. The result gives the rule, the location and what is wrong, and links to the full report.
- **skipped**: the rule does not apply to this change, for example because the change touches no export path. The validator decides this from a declared condition, never by guessing.
- **could_not_run**: the rule applies and the check was required, but no verdict was produced, because a tool was missing, an environment was unavailable, the run timed out or the tool crashed.

SARIF draws the same line between "did the tool run" and "what did it find". Each run records whether the tool's execution succeeded separately from its results, and the format has a result kind for a rule that was not evaluated because it does not apply. Its informative appendix warns that when the tool reports an execution error, its results cannot be assumed complete.[^sarif-2-1-0] In SARIF's terms, passed corresponds to `pass`, failed to `fail` and skipped to `notApplicable`. Could_not_run is this site's own term; the nearest SARIF equivalent is an unsuccessful execution.

A validator detects that it cannot run by checking its prerequisites before it evaluates anything: the tool is present at the expected version, the environment answers, and the test data exists. It reads the tool's actual output rather than trusting the exit code alone, since SARIF notes that not every program exits with 0 on success and non-zero on failure.[^sarif-2-1-0] When the validator never starts at all, it cannot report anything, and SARIF expects the component that launched the tool to write the record instead.[^sarif-2-1-0] In practice, the runner treats a required validator that produced no result as could_not_run.

Could_not_run must never be reported as skipped. At least one change host counts a skipped required status check as satisfied,[^github-protected-branches] so a missing environment reported as "skipped" lets the change through unchecked. In the export example, R-017, the volume-limit rule, states a row limit for a single export, and its check runs the 50k-row load scenario. On the first export pull request the load-test tool is missing from the runner image, so the check reports could_not_run and names the missing tool. It does not report failed, because the change is not at fault, and it does not report skipped, because the rule applies. The validator only reports. What each result means for a merge or release decision is set in the assurance band of the map, and the kit-wide definition of could_not_run is on the [Engineering Kit](engineering-kit.html) page.

### From report-only to required

A new validator first runs in report-only mode: it runs on every pull request and its findings are visible, but it cannot stop a merge. Policy engines ship modes for exactly this. One open-source cluster policy engine's dry-run mode lets new constraints be tested in a running cluster without enforcing them, and its warn mode also tells the requester why a request would have been denied.[^gatekeeper-violations] A container orchestrator's built-in admission policies offer deny, warn and audit as separate actions.[^k8s-validating-admission-policy] CI platforms have a weaker counterpart: one platform's documentation describes a job allowed to fail, which shows a warning while the pipeline still counts as successful.[^gitlab-ci-yaml] A finding that shows only as a warning on a passing job is easy to miss, so report-only results need a place where people actually read them.

No public source says when a validator should start to block, so this is recommended practice. A validator enters report-only mode with an owner and a date by which the decision is due. The decision comes from its record, not the calendar. Where its failures pointed at real problems that people fixed in the code, it becomes a required check. Where they were mostly noise, the validator is corrected and the date moves, or the validator is retired. The switch to required is itself a reviewed change, so the evidence shows when the check began to block.

In the export example, the access validator for R-042 is a required check that covers background workers as well as the request path. A background worker's broader query had been a recurring finding in human review, and that repeated finding is why the validator was extended to cover worker queries. On the first export pull request it reports failed, tagged R-042, and points to the worker's query, which reads more records than the caller may see.

### Timeouts

Each validator sets its own time limit and does not rely on a runner's default, which may be far longer than the check needs. A timeout is never a pass. Check platforms keep "timed out" as a conclusion separate from success,[^github-checks-api] and one test runner's timeout plugin ends a hanging test by failing it or by stopping the process.[^pytest-timeout] The site recommends one retry, to rule out a transient fault in the environment. If the retry also times out, the validator reports could_not_run, stating the limit and how far the run got. The exception is a rule that is itself a time budget, such as a response-time limit; there, running out of time is the violation, and the result is failed.

### Flaky checks

A flaky check passes and fails on the same code, so a failure stops being a reliable signal: real failures get overlooked, and time goes on re-runs.[^pytest-flaky] Martin Fowler argues that non-deterministic tests damage trust in the whole suite. He treats quarantine as a short-term measure that needs a limit on how many tests it holds or how long they stay there.[^fowler-nondeterminism] Google's testing team has described re-running failed tests and automatically quarantining the flakiest ones, with a bug filed for each.[^google-flaky-tests] One empirical study of fixes to flaky tests in open-source projects reports asynchronous waits, concurrency and test-order dependency as the most common causes.[^luo-flaky-2014] How a workflow run treats a check that failed and then passed is on the [Workflows](workflows.html) page.

Checks that depend on timing or shared environments, such as the 50k-row load scenario for R-017, are the most exposed, since asynchronous waits and concurrency are among the causes Luo and colleagues found most often.[^luo-flaky-2014]

### Fitness functions for architecture rules

Neal Ford, Rebecca Parsons and Patrick Kua introduced the architectural fitness function in *Building Evolutionary Architectures*, borrowing the idea from evolutionary computing: an objective assessment of how well a system preserves an architectural characteristic, carried out through tests, metrics, monitoring and similar mechanisms.[^ford-evolutionary-architectures][^thoughtworks-radar-fitness] Fitness function-driven development writes these checks first, in the manner of test-driven development, so that architectural conformance gets feedback during development rather than after it.[^fitness-function]

An architecture rule becomes a validator when it is expressed as a structural check that runs with the build, such as an architecture test in the application's own test suite or a dependency-rule checker's configuration. In the export example, such rules might say that the export feature reaches customer records only through the data-access layer, that the domain layer depends on nothing above it, and that no dependency cycles exist between modules. Böckeler's worked examples include dependency rules, written with the agent's help, that enforce a codebase's module layers.[^bockeler-sensors] The recommended practice is to begin with structural rules this codebase has already been seen to break, and to add them one at a time, so that each rule's failures are understood before the next rule arrives. A failure message that names the rule, the offending dependency and the permitted alternative lets a coding agent correct its own change without a person translating.

### Keeping the validator honest

An agent asked to make a check pass may find it easier to change the check than the code. As recommended practice, a validator's code, configuration and limits sit outside what an agent may change unsupervised: a change that alters a validator and the code it checks at the same time goes to a person for review. Tests an agent writes to satisfy a validator are reviewed for what they actually establish, and a test that has never been seen to fail without the behaviour it checks is weak evidence.

### Ready to ship

No public source sets a release bar for a check of this kind, so the following is this site's recommended practice. A validator is ready to ship in the kit, even in report-only mode, when:

- it gives the same result locally, in the agent's session and in CI;
- it has a known-bad example that must fail and a known-good example that must pass, both kept with the validator and run whenever it changes;
- it reports could_not_run for each prerequisite it depends on, and never reports passed or skipped when a prerequisite is missing;
- it has its own time limit and a named owner;
- each failure carries the rule identifier, the location, what is wrong and a link to the evidence.

## Where it sits on the map

Validators sit in the core band, band 3 of the map ("what does the work"), as one of the five parts inside the Engineering Kit box. Before a validator comes its rule: a rule routed to a gate in the [Rule registry](rule-registry.html) becomes a validator here. Alongside are skills, which guide what an agent tries to do rather than checking the result, and so meet a different acceptance bar (see [Skills with evals](skills-and-evals.html)). After the validator, each result lands in the evidence record, whose fields are fixed on the [Evidence schema](evidence-schema.html) page. [Adapters](adapters.html) bind validators to a particular CI runner and change host without making them depend on either. In the vocabulary of [Harness engineering](harness-engineering.html), validators are the computational sensors, while skills and instructions are guides.[^bockeler-harness] Every workflow calls validators at its checks step (see [Workflows](workflows.html)). The assurance band of the map decides what their results mean for merge and release.

## Pitfalls

- **Report-only with no end.** Validators stay non-blocking long after their findings became actionable. Sign to watch: validators past their end date, and report-only findings that nobody acts on.
- **Blocking before trust.** A validator becomes required while it is still noisy. Sign to watch: requests to bypass it, or the check quietly switched off.
- **A missing prerequisite reported as clean.** A validator that could not run reports passed or skipped. Sign to watch: a required check that reports no findings on a run that scanned zero files or never reached its environment.
- **Retry to green.** Failures that pass on a second run are counted as passes. Sign to watch: rising re-run counts, and reports that show only the final pass of a check that failed first.
- **Drift between local and CI.** The pipeline runs its own version of the check. Sign to watch: "it passes on my machine" in pull-request threads, or a CI configuration that repeats the check's logic.
- **Failures nobody can act on.** A red status with no rule identifier, location or evidence link. Sign to watch: questions in the pull request about what failed and why.
- **The check weakened by the change it checks.** An agent relaxes a validator to get a pass. Sign to watch: a single change that edits both a validator or its limits and the code it checks.
- **Orphaned validators.** Checks keep running after their rule has changed or retired. Sign to watch: findings with no rule identifier, or identifiers the registry no longer holds.

## Related

- [Rule registry](rule-registry.html): where each rule gets its identifier, route and owner.
- [Engineering Kit](engineering-kit.html): the package validators ship in, its verify command and the kit-wide could_not_run result.
- [Evidence schema](evidence-schema.html): the fields that record each validator's result.
- [Skills with evals](skills-and-evals.html): the probabilistic counterpart to validators, and why its bar differs.
- [Adapters](adapters.html): how validators bind to a CI runner and change host.
- [Harness engineering](harness-engineering.html): the discipline in which validators are the computational sensors.
- [Workflows](workflows.html): where validators run as the checks step of each delivery decision.
- [Workflow catalog](workflow-catalog.html), the [Validator](glossary.html#validator) entry and the rest of the [Terminology](glossary.html): the list of workflows, and where each term on this page comes from.

## Sources

- Böckeler on computational and inferential controls, guides and sensors.[^bockeler-harness]
- Böckeler's worked examples of computational sensors, dependency rules and inferential review.[^bockeler-sensors]
- One model vendor's published account of enforcing architectural constraints through automated checks.[^openai-harness]
- Fowler on continuous integration: a fast build that any developer can run locally.[^fowler-ci]
- The SARIF 2.1.0 standard: rule identifiers, execution success recorded apart from results, result kinds, incomplete result sets.[^sarif-2-1-0]
- Change-host documentation on required status checks and check conclusions.[^github-protected-branches][^github-checks-api]
- Policy-engine and CI documentation on dry-run, warn, audit and allowed-to-fail modes.[^gatekeeper-violations][^k8s-validating-admission-policy][^gitlab-ci-yaml]
- Test-runner documentation on timeouts and flaky tests.[^pytest-timeout][^pytest-flaky]
- Fowler, Google's testing team, and Luo and colleagues on non-deterministic tests, quarantine and their causes.[^fowler-nondeterminism][^google-flaky-tests][^luo-flaky-2014]
- Ford, Parsons and Kua, the Thoughtworks Technology Radar, and Paul and Wang on architectural fitness functions.[^ford-evolutionary-architectures][^thoughtworks-radar-fitness][^fitness-function]
- The link from each result to a rule identifier, when a report-only validator becomes required, the retry policy for timeouts, keeping the validator out of an agent's reach and the bar for shipping are this site's recommended practice; no public source states them for validators.
