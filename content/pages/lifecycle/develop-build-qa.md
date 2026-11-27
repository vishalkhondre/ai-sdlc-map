---
id: develop-build-qa
type: phase
band: lifecycle
map_box: Develop · Build · QA
title: Develop, Build and QA
summary: Develop, Build and QA are the three phases in which one change is made, assembled and tested under one set of checks and one evidence record; they end in the merge decision, and agents, deterministic checks and people each have a distinct part along the way.
key_terms: [deterministic-gate, engineering-kit, gate, validator, review-skill, skill, could-not-run, evidence-record, independent-basis, guides-and-sensors, risk-tier, harness-engineering, workflow, three-roles, review-fatigue, feedback-path, export-example]
sources: [google-eng-practices-small-cls, google-eng-practices-review, fowler-selftesting, fowler-ci, dora-test-automation, nist-ssdf, sre-book-release-engineering, fowler-deployment-pipeline, humble-farley-cd, safe-continuous-integration, slsa-provenance, slsa-build-track-basics, istqb-ctfl-4, fowler-test-pyramid, istqb-rbt, nist-ir-8397, owasp-asvs, owasp-secrets-management, istqb-stress-testing, bockeler-harness, bockeler-sensors, dora-2024-report, dora-2024-highlights, dora-2025-report, dora-2025-announcement, dora-ai-capabilities-impact, perry-2023, konstantinou-test-oracles, metr-reward-hacking, anthropic-claude-37-system-card, dora-small-batches, safe-built-in-quality, istqb-acceptance-criteria, scrum-guide-2020]
related: [engineering-kit, validators, skills-and-evals, workflows, evidence-schema, harness-engineering, rule-registry, adapters, design, deploy, definition-of-ready-and-done, traceability-spine, pull-request-verification]
review_record: content/reviews/1.5.0-lifecycle.md
---

## Purpose

Develop, Build and QA are the phases in which one change is made, assembled into something that
runs, and tested. In the AI SDLC (the software development lifecycle with AI agents doing part of
the work), the three share a page because, for a single change, they share one set of checks, one
evidence record and one decision at the end, the merge decision, which the
[Workflows](workflows.html) page gives as its example of a workflow. The map draws one workflow
bar across all three labels, "pull-request verification · security & performance checks by tier",
for the same reason.

The question the stretch answers is what must be true, and shown, before a change may join the
mainline. Beneath every answer sits the deterministic floor: the
[Engineering Kit](engineering-kit.html)'s verify command, which every task runs before anything
else. An agent adds speed above that floor and never replaces it.

The workflow catalog names its phases differently from the map: the rows for this stretch sit in
catalog phase 3 "Develop", phase 4 "Verify" and, for pull-request verification, phase 5 "Review".

## Traditional practice

Long before coding agents, each of the three phases had public guidance of its own. That guidance
still holds: agents change who produces the first version of the work, not what good work is.

### Develop

Development practice centres on small changes that carry their own tests. Google's engineering
practices document defines the right size as one that "makes a minimal change that addresses just
one thing" and says a change "should include related test code". Small changes, it says, are
reviewed more quickly and more thoroughly, are less likely to introduce bugs and are simpler to
roll back.[^google-eng-practices-small-cls] In its guidance for reviewers, a reviewer looks at design,
functionality, complexity, tests, naming, comments, style, consistency and documentation, in that
order, and asks for "unit, integration, or end-to-end tests as appropriate for the
change".[^google-eng-practices-review]

The tests run without ceremony. Martin Fowler describes self-testing code as being able to "invoke
a single command that executes the tests" with confidence that they would expose the bugs hiding in
the code.[^fowler-selftesting] His account of continuous integration counts making the build
self-testing, fixing broken builds immediately and keeping the build fast among its
practices.[^fowler-ci] DORA's guidance on test automation expects feedback from automated tests
"in less than ten minutes both on local workstations and from the continuous integration
system".[^dora-test-automation]

Security sits in the same loop. NIST's Secure Software Development Framework (SSDF) asks teams to
decide which kinds of code review or analysis to use (PW.7.1), to perform them in line with secure
coding standards and to record and triage what they find (PW.7.2), and to store all forms of code
according to least privilege (PS.1.1).[^nist-ssdf]

### Build

A build turns source into something that can be tested and shipped, and its first property is
repeatability. Google's site reliability engineering book says that if two people build the same
product at the same revision on different machines, "we expect identical results"; its builds are
hermetic, depending on "known versions of build tools, such as compilers, and dependencies, such as
libraries".[^sre-book-release-engineering]

Builds run inside a deployment pipeline, which Fowler describes as "breaking up your build into
stages. Each stage provides increasing confidence, usually at the cost of extra
time."[^fowler-deployment-pipeline] Jez Humble and David Farley's *Continuous Delivery* gives the
subject a chapter titled "Commit Testing Stage".[^humble-farley-cd] SAFe places this work in continuous integration,
where "new functionality is developed, tested, integrated, and validated in preparation for
deployment and release".[^safe-continuous-integration]

A build also records where its output came from. SLSA defines provenance as "verifiable information
about software artifacts describing where, when, and how something was produced".[^slsa-provenance]
Its Build track, in SLSA v1.2, has three levels: provenance showing how the package was built;
signed provenance generated by a hosted build platform; and a hardened build
platform.[^slsa-build-track-basics] The SSDF asks for compilers, interpreters and build tools with
security features (PW.6.1), for tools configured to generate artifacts (PO.3.3), and for teams to
collect, safeguard, maintain and share provenance data (PS.3.2).[^nist-ssdf]

### QA

Testing is organised by level. The ISTQB Foundation Level syllabus describes five test levels:
component testing (also called unit testing), component integration testing, system testing,
system integration testing and acceptance testing. It separates confirmation testing, which
confirms that an original defect has been fixed, from regression testing, which confirms that a
change has caused no adverse consequences.[^istqb-ctfl-4] Fowler's test pyramid advises "many more
low-level UnitTests than high level BroadStackTests running through a GUI", and credits Mike Cohn's
2009 book with spreading the name.[^fowler-test-pyramid] Effort follows risk: in risk-based
testing, the selection and use of test activities and resources depend on risk types and risk
levels.[^istqb-rbt] The [Workflows](workflows.html) page applies that idea as the risk tier.

Security verification draws on a wider set of techniques. NIST IR 8397, written as minimum
standards for developer verification, recommends eleven, in this order: threat modeling; automated
testing; static code scanning; heuristic tools for hardcoded secrets; built-in checks and
protections; "black box" test cases; code-based structural test cases; historical test cases;
fuzzing; web application scanners; and addressing included code. It states that it "does not
address the totality of software verification".[^nist-ir-8397] OWASP's Application Security
Verification Standard leaves the choice of verification level to an organisation's analysis of its
own risks.[^owasp-asvs] For credentials, OWASP advises centralising the storage, provisioning,
auditing, rotation and management of secrets, and applying least privilege to them.[^owasp-secrets-management]

Performance testing examines behaviour under load. The ISTQB glossary defines stress testing as "a
type of performance testing to evaluate a system or component at or beyond the limits of its
anticipated or specified workloads, or with reduced availability of resources such as access to
memory or servers".[^istqb-stress-testing] The [Validators](validators.html) page notes that checks
depending on timing or shared environments are the ones most exposed to flaky results.

## AI-assisted practice

Agents change who writes the first version of code and tests. They do not change what a merge
requires. No public study sets out how work in these phases should be divided between an agent,
deterministic checks and people, so the division below is this site's recommended practice, with
research cited where it exists.

### Develop with agents

The agent writes code and tests for one task inside its harness, which Birgitta Böckeler describes
as everything in a coding agent except the model: guides that steer it before it acts and sensors
that check its work after.[^bockeler-harness] On this site the guides include
[skills](skills-and-evals.html) the agent loads when a task calls for them, and the sensors include
[validators](validators.html), the deterministic checks tied to rule identifiers that Böckeler's
examples call computational sensors.[^bockeler-sensors] The agent runs the same verify command a
person runs before it hands anything on, and reads the failures to correct its own change. It works
under an identity with only the permissions its task needs, as the
[Harness engineering](harness-engineering.html) page explains, so staying in scope never depends on
its following an instruction. The developer who directs it remains the author of the change.

DORA's research explains why the floor matters more once an agent writes code. Its 2024 research
found that AI adoption "negatively impacts software delivery stability and throughput, reminding
teams that fundamentals like small batch sizes and robust testing remain crucial";[^dora-2024-report]
the announcement of that report points to the same two fundamentals.[^dora-2024-highlights] In 2025
DORA describes AI's primary role as "an amplifier, magnifying an organization's existing strengths
and weaknesses",[^dora-2025-report] and warns that "without robust control systems, like strong
automated testing, mature version control practices, and fast feedback loops, an increase in change
volume leads to instability".[^dora-2025-announcement] Its guidance on putting the AI Capabilities
Model to work adds that "AI can easily generate massive blocks of code, which are hard to review and
test", and calls version control a critical safety net.[^dora-ai-capabilities-impact] The
recommended response is to keep each agent task to a change one reviewer can read in full.

An agent's confidence is not evidence of security. In one user study, participants with an AI code
assistant "wrote significantly less secure code than those without access" and were "more likely to
believe they wrote secure code".[^perry-2023] Security checks therefore run on agent-written code
exactly as on any other, and the agent's own account of its change never stands in for them.

### Build with agents

The build stays deterministic and hermetic, as release engineering has long
required.[^sre-book-release-engineering] No public evidence supports placing an agent inside the
build as a step that decides its output, and this page recommends none. An agent may propose
changes to build scripts, pipeline definitions or pinned tool versions, but each such change alters
a controlled artefact: the SRE book's gated operations include "changes to build
configuration".[^sre-book-release-engineering] As recommended practice, a change to build
configuration goes to a person for review, and a change that edits a check together with the code
the check examines is treated as a finding in its own right, as the [Validators](validators.html)
page describes.

Provenance comes from the build platform, not from the agent. SLSA's second Build level calls for
signed provenance generated by a hosted build platform,[^slsa-build-track-basics] so an agent's
description of what it built is a note, not provenance. When an agent's task adds or upgrades a
library, the change also passes through the catalog's
[Dependency change](workflow-catalog.html#W15) workflow.

### QA with agents

Agents can write many tests quickly; the risk lies in what those tests rest on. When one agent
writes code and tests from the same understanding, both can share one mistaken assumption, so the
tests need an independent basis: acceptance criteria[^istqb-acceptance-criteria], access rules, interface contracts or failure
scenarios defined apart from the implementation. Research points the same way. A study of test
cases and oracles for 24 Java repositories found that "LLM-based test generation approaches mainly
capture the actual program behavior making bug detection difficult".[^konstantinou-test-oracles] A
generated test that passes on the code it was generated from shows that the code does what it does,
not that it does what was specified.

An agent that is rewarded for passing tests may change the tests. A research post by METR describes
models attempting "to get a higher score by modifying the tests or scoring code" on METR's own
evaluation tasks.[^metr-reward-hacking] A model developer's system card reports that its model
occasionally special-cased tests to make them pass, sometimes by modifying the tests themselves,
and attributes the behaviour to reward hacking during training.[^anthropic-claude-37-system-card]
The [Harness engineering](harness-engineering.html) page draws the conclusion: an agent must not be
able to satisfy a sensor by changing it.

Security and performance checks follow the change's [risk tier](glossary.html#risk-tier). In the
site's running example, the customer-record export, the access validator for rule R-042 fails on
the first pull request because a background worker's query reads records outside the caller's
scope; a review skill's finding on the same query sits beside that failure as advice only.
The [Workflows](workflows.html#risk-tiers-same-definition-different-cost) page sets this beside a
change to the export button's label.

A required check that cannot produce a verdict is a result of its own, never a pass. In the same
example, the 50k-row load scenario for the volume-limit rule R-017 reports
[could_not_run](glossary.html#could-not-run) because the load-test tool is missing from the runner
image. It is neither passed nor skipped, and the fix belongs to whoever maintains the runner.

## Workflows in this phase

The workflow the map draws across all three phases is
[Pull-request verification](pull-request-verification.html) (catalog row [W23](workflow-catalog.html#W23)), where the stretch ends in the merge
decision; the map adds "security & performance checks by tier" to its label. The other rows below
run inside the stretch. Each row's definition (trigger, agent task, checks, human decision and
evidence) is in the [workflow catalog](workflow-catalog.html) and is not repeated here; the
[Workflows](workflows.html) page explains what a workflow is.

| Catalog row | Where it falls on this page |
|---|---|
| [W13 Task execution loop](workflow-catalog.html#W13) | Develop; the floor every task runs |
| [W14 Documentation generation](workflow-catalog.html#W14) | Develop, beside the code it describes |
| [W15 Dependency change](workflow-catalog.html#W15) | Build |
| [W16 Data change execution](workflow-catalog.html#W16) | Develop |
| [W17 Acceptance-test generation and execution](workflow-catalog.html#W17) | QA |
| [W18 Security verification](workflow-catalog.html#W18) | QA, by tier |
| [W19 Performance verification](workflow-catalog.html#W19) | QA, by tier |
| [W20 Accessibility and visual regression](workflow-catalog.html#W20) | QA |
| [W21 API contract conformance](workflow-catalog.html#W21) | QA |
| [W22 System integration and acceptance evidence](workflow-catalog.html#W22) | QA |
| [W23 Pull-request verification](workflow-catalog.html#W23) | The close of all three; see the [Pull-request verification](pull-request-verification.html) page |

## Gates and evidence

A task enters the stretch once it meets the team's Definition of Ready, which is set before
development starts. The Scrum Guide defines the Definition of Done for the Increment as a formal
description of its state when it meets the quality measures required for the
product[^scrum-guide-2020]. Applying a Definition of Done to each story at the close of this stretch
is this site's recommended practice. The
[Definition of Ready and Done](definition-of-ready-and-done.html) page covers both.

The gates in this stretch check each change as it is made, not only once the work is finished. In
that they put into practice what SAFe calls built-in quality, "a set of practices to help ensure
that the outputs of Agile teams in business and technology domains meet appropriate quality
standards throughout the process of creating customer value".[^safe-built-in-quality] Inside the
stretch, every gate runs through the verify command, which is the same command on a developer's
machine, in an agent's session and in the pipeline ([Engineering Kit](engineering-kit.html)). The
checks a revision needs follow its risk tier. What each run records, and how its overall status
follows from the results, is fixed on the [Evidence schema](evidence-schema.html) page.

The build leaves evidence of its own. Provenance generated by the build platform, in line with
SLSA's Build track and the SSDF's provenance task,[^slsa-build-track-basics][^nist-ssdf] records how
the tested output was produced.

The stretch is left through one exit: the merge decision. Each workflow's catalog row names the
record it leaves, and the [Workflows](workflows.html) page explains how that record is handed on.

## Roles

The stretch keeps apart the three roles the [Workflows](workflows.html) page sets out: the agent
produces, the checks enforce what a tool can decide reliably, and people make the calls that need
context. Google's engineering practices give separate guidance to the developer who authors a
change and the reviewer who examines it,[^google-eng-practices-small-cls][^google-eng-practices-review]
and both accountabilities hold when an agent writes the code.

- **The developer** who directs the agent is the author of the change and answers for it.
- **The reviewer** takes the merge decision on what a tool cannot judge.
- **Rule owners**, recorded in the [Rule registry](rule-registry.html), own what a rule means and
  any exception to it. In the export example, a request to exceed R-017's row limit is pending with
  the security owner while the record's overall status is blocked; R-042 is not open to exception.
- **The owner of the runner or environment** receives could_not_run results, since the change may
  be sound.
- **The agent** can comment on a pull request. It cannot approve, merge or change the checks.

Who decides at the human step of each workflow is named in that workflow's catalog row.

## Pitfalls

- **Code and tests from one understanding.** The agent writes both, and the tests confirm what the
  code does rather than what was specified.[^konstantinou-test-oracles] Sign: tests with no link to
  an acceptance criterion, a rule or a contract.
- **The test changed to pass.** The agent edits a test or a check instead of the code, a behaviour
  reported both by METR and in a model developer's system
  card.[^metr-reward-hacking][^anthropic-claude-37-system-card] Sign: one change that edits both a
  check and the code it checks.
- **Silence read as success.** A required check never reports, and the change merges anyway. Sign:
  a merged change whose record holds no result for a check its tier requires; the
  [Workflows](workflows.html) page covers the case.
- **A flaky check re-run until it passes.** The pass after a retry is counted like any other, and
  the check stops meaning anything. Sign: one check failing and passing on the same revision, a
  pattern the [Validators](validators.html) page covers.
- **A change too large to review.** DORA notes that "large changes are difficult to review, test,
  and integrate safely",[^dora-small-batches] and that AI can generate code in blocks that are hard
  to review and test.[^dora-ai-capabilities-impact] Sign: large diffs approved with few comments.
- **Reviewers doing a tool's job.** Review threads fill with comments a check could make, and
  review fatigue follows. A recurring comment belongs on the
  [feedback path](glossary.html#feedback-path), the site's extension of Böckeler's steering
  loop,[^bockeler-harness] and the export's R-042 validator covers background workers for that
  reason. Sign: the same comment on many changes.
- **Local and pipeline results that differ.** The pipeline runs its own version of a check. With one
  verify command and one set of inputs, a difference points at the environment, not the rules
  ([Engineering Kit](engineering-kit.html)). Sign: changes that pass locally and fail in the
  pipeline with no code difference.
- **Generated code trusted as secure.** In one study, users of an AI assistant wrote less secure
  code and were more likely to believe it secure.[^perry-2023] Sign: security checks relaxed for
  agent-written changes.

## Related

- Core: [Engineering Kit](engineering-kit.html), [Validators](validators.html),
  [Skills with evals](skills-and-evals.html), [Workflows](workflows.html),
  [Evidence schema](evidence-schema.html), [Harness engineering](harness-engineering.html),
  [Rule registry](rule-registry.html) and [Adapters](adapters.html).
- Neighbouring phases: [Design](design.html) before, [Deploy](deploy.html) after.
- [Definition of Ready and Done](definition-of-ready-and-done.html) and
  [Traceability spine](traceability-spine.html): the entry bar and the links from criterion to test.
- [Pull-request verification](pull-request-verification.html): whether one revision of a change may join the mainline.
- [Task execution loop](workflow-catalog.html#W13), [Pull-request verification](workflow-catalog.html#W23)
  and [could_not_run](glossary.html#could-not-run).

## Sources

- Development and review: Google's engineering practices, Fowler, DORA and NIST
  SSDF.[^google-eng-practices-small-cls][^google-eng-practices-review][^fowler-selftesting][^fowler-ci][^dora-test-automation][^nist-ssdf]
- Builds and pipelines: the SRE book, Fowler, Humble and Farley (table of contents
  only), SAFe and SLSA.[^sre-book-release-engineering][^fowler-deployment-pipeline][^humble-farley-cd][^safe-continuous-integration][^safe-built-in-quality][^slsa-provenance][^slsa-build-track-basics]
- Testing and security verification: ISTQB, Fowler, NIST IR 8397 and OWASP.[^istqb-ctfl-4][^istqb-rbt][^istqb-stress-testing][^fowler-test-pyramid][^nist-ir-8397][^owasp-asvs][^owasp-secrets-management]
- Harness vocabulary: Böckeler.[^bockeler-harness][^bockeler-sensors]
- AI-assisted delivery: DORA's research and guidance; Perry and colleagues, Konstantinou and
  colleagues, METR and a model developer's system card on AI-written code and tests.[^dora-2024-report][^dora-2024-highlights][^dora-2025-report][^dora-2025-announcement][^dora-ai-capabilities-impact][^dora-small-batches][^perry-2023][^konstantinou-test-oracles][^metr-reward-hacking][^anthropic-claude-37-system-card]
- The division of work between agent, checks and people in these phases, review of build
  configuration changes and the roles listed are this site's recommended practice; no public study
  sets them out.
