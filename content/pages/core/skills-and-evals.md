---
id: skills-and-evals
type: concept
band: core
map_box: Engineering Kit · skills with evals
title: Skills with evals
summary: A skill is packaged guidance a coding agent loads when a task calls for it; because it shapes behaviour without guaranteeing it, it ships with a record of scenario evaluations rather than on one passing run.
key_terms: [skill, review-skill, harness-evaluation, llm-as-a-judge, guides-and-sensors, two-kinds-of-machinery, harness, rule-registry, rule-route, validator, feedback-path, independent-basis, engineering-kit, export-example]
sources: [bockeler-harness, bockeler-sensors, bockeler-context, anthropic-agent-skills, github-agent-skills, claude-skill-practices, anthropic-agent-evals, agentskills-evaluating, openai-eval-skills, yao-tau-bench, ouyang-nondeterminism, zheng-llm-judge, husain-evals]
related: [validators, rule-registry, engineering-kit, harness-engineering, evidence-schema, workflows]
review_record: content/reviews/1.4.0-core.md
---

## Definition

A skill is a packaged piece of guidance that a coding agent loads only when the task in hand calls
for it: a short name and description the agent scans, a body of instructions it reads once it
decides the skill applies, and, optionally, scripts and reference files it can use along the
way.[^bockeler-context][^anthropic-agent-skills] The folder-and-file format is published as an
open specification that a range of AI systems use.[^github-agent-skills][^anthropic-agent-skills] In Birgitta
Böckeler's vocabulary a skill is a guide, a control that steers the agent before it acts, as
opposed to a sensor, which observes the result afterwards.[^bockeler-harness] On this site a skill
also names the rules it supports, and it ships with evals: a set of scenarios that test whether an
agent working with the skill behaves as intended, run repeatedly and recorded across versions. A
review skill is the sensor counterpart. It reads a change against the applicable rules and reports
findings, which is what Böckeler calls an inferential sensor.[^bockeler-sensors]

## Why it matters

In an AI SDLC (the software development lifecycle with AI agents doing part of the work), much of
what a team knows about doing the work well has to reach the agent somehow: which records an export
may return, which fields never leave the system, when to stop and ask. Written once as a skill, that know-how reaches every task that
needs it without filling the agent's context on tasks that do not.[^bockeler-context] The risk is
that a team starts treating the skill as a guarantee. Böckeler warns that as long as a language
model is involved, the outcome remains a matter of probability.[^bockeler-context] One vendor's
skill-authoring guidance uses exactly that failure as its worked example: an agent writes a query
and leaves out a filter that the loaded skill tells it to apply.[^claude-skill-practices] The same
prompt can also produce different code from one request to the next, and setting temperature to
zero reduces that variation without removing it.[^ouyang-nondeterminism]

Two things follow. A skill cannot be the thing that enforces a rule, because nothing about loading
it makes the agent comply. And a skill cannot be accepted the way a deterministic check is, on one
green run, because the next run may differ. Without evals, a team cannot tell whether a skill helps,
does nothing, or quietly makes the agent worse, and it cannot tell whether a model upgrade has
changed any of that.[^anthropic-agent-evals]

## How it works

**Route the rule first.** Every rule in the rule registry carries a route: gate, judgment or
guidance. A skill serves the guidance route, and it may also help the agent meet a rule that a gate
enforces. This site recommends a clear division of labour between validators and skills. When a
validator can decide a rule, the validator carries it. A skill that touches the same rule teaches
the agent why the rule exists and what a compliant change looks like, so the validator seldom has
to fail.[^bockeler-sensors][^claude-skill-practices] A skill earns its place in work that turns on
interpretation, where no deterministic check reaches.

**Write the skill for on-demand loading.** Until the agent decides the skill applies, it sees only
the name and description, so the description states plainly which tasks the skill is for. The main
file carries what nearly every use of the skill needs. Material that only some uses need goes in
separate files that the main file points to. Any step that must give an identical result every time
is a script the agent executes, not prose it
interprets.[^anthropic-agent-skills][^claude-skill-practices] The skill cites the identifiers of
the rules it supports, so the registry can list every skill that touches a rule. That link is this site's recommended practice; no public source describes it.

**Build the eval set before trusting the skill.** An eval gives the agent an input, lets it work,
and applies grading logic to the result. Each case pairs a realistic request with a description of
success and one or more graders, and a set tests both the cases where a behaviour should occur and
the cases where it should not.[^anthropic-agent-evals][^agentskills-evaluating] Skill evals also
check activation: some cases name the skill, others are ordinary requests that never mention it, to
see whether the agent picks it up unprompted.[^openai-eval-skills] Practitioner guidance suggests
that a small set of tasks drawn from real failures is enough to start.[^anthropic-agent-evals]
The expected behaviour comes from the specification and the rule, not from the skill's own text,
so that the eval has an independent basis.

For the customer-record export, an access-rule skill supports R-042: it guides the agent to return
only the records the caller may read, and to stop and ask when the specification leaves the access
rule open. Its eval set might hold these cases.

| Case | Input | Passes when |
|---|---|---|
| Access rule left open | A specification for the export that does not say who may read which records | The agent stops and asks instead of choosing a rule |
| Unprompted activation | A plain request to speed up the export, with no mention of access | The agent still loads the skill and keeps the filter |
| Already correct | An export whose access rule is settled and implemented | The agent leaves the filtering as it is |
| Excluded field | A request to add a field the specification leaves out of the export | The agent points out the conflict with the specification |
| Review skill | A change whose background worker runs a broader query than the request path | The review skill reports the broader query against R-042 |

The skill does not enforce R-042; its validator is what fails a change that returns records the
caller may not read. The skill makes that failure less likely, and the evals show by how much.

**Run each case more than once.** Because output varies between runs, each case runs as several
trials.[^anthropic-agent-evals] Two summaries matter. pass@k is the chance that at least one of k
trials succeeds; pass^k, proposed in agent-benchmark research, is the chance that all k succeed, and
it falls as k rises, which makes it the stricter measure of reliability.[^yao-tau-bench][^anthropic-agent-evals]
A case that passes on some runs and fails on others is flaky and needs investigating, not
re-running until it passes.[^agentskills-evaluating]

**Choose the grader to fit the check.** Code-based graders are fast, cheap and reproducible but
brittle to valid variation; model-based graders handle nuance but are themselves non-deterministic
and need calibrating against people; human graders are the most trustworthy and the slowest.
Mechanical checks, such as whether the query filters by caller, belong in
code.[^anthropic-agent-evals][^agentskills-evaluating] A model used as a grader is the practice
Zheng and colleagues studied as LLM-as-a-judge. In their study the strongest judge agreed with
human preferences more than 80% of the time, about as often as people agree with each other, and it
showed position, verbosity and self-enhancement biases.[^zheng-llm-judge] Agreement with human
grading is checked at the start and again from time to time.[^anthropic-agent-evals][^husain-evals]

**Keep an evaluation history.** Each run of the set compares the skill against a baseline: the
same prompts without the skill, or the previous version of the skill.[^agentskills-evaluating]
Guidance on testing skills treats the aim as a score that can be compared over
time.[^openai-eval-skills] This site recommends that the history record, for each skill version,
the version of the eval set, the model and tool versions, the number of trials and the results, and
that a skill ships only with such a history. That bar is recommended practice, not a published
finding.

**Re-run when anything that shapes behaviour changes.** Practitioner guidance runs evals on each
change to the agent and on each model upgrade, and vendor guidance advises testing a skill with
every model it will be used with.[^anthropic-agent-evals][^claude-skill-practices] After a change to
the skill, every case runs again, not only the one that prompted the change.[^agentskills-evaluating]
This site adds two triggers as recommended practice: a change to a tool the skill relies on, and a
change to any rule the skill cites, which also means revising the skill before its evals run. Once
a skill is reliable, its cases become a regression suite that is expected to pass almost every
time.[^anthropic-agent-evals]

**Keep the review skill advisory.** A review skill reads a diff against the rules and reports
findings tagged to rule identifiers. Böckeler's worked examples show inferential sensors addressing
concerns such as semantic duplication only partially, where computational sensors catch duplicate
code and coverage gaps reliably.[^bockeler-sensors] So the review skill proposes and a validator or
a named person decides. It is evaluated like any other skill, with cases where it should raise a
finding and cases where it should stay quiet. Until those results show how often it is right and
how often it raises a false alarm, its findings inform reviewers and nothing more; what weight they
carry after that is set in the assurance band of the map. Every finding costs a human reviewer some
attention, so a noisy review skill is expensive. These are recommended practice.

**Decide when a practice becomes a skill.** The usual trigger is repetition: the team finds itself
typing the same guidance into agent sessions again and again.[^claude-skill-practices] Vendor
guidance also suggests writing the evaluation cases first, from failures already seen, and the
skill text after them.[^anthropic-agent-skills][^claude-skill-practices] Guidance that turns out to
be a checkable rule goes to a validator, as described under routing above. This site recommends
that someone answers for each skill: that person keeps its eval set current and removes the skill
once nothing depends on it.

## Where it sits on the map

Skills with evals is one of the five parts of the Engineering Kit, in the core band, the band that
does the work. The kit is the versioned, installable package that carries a team's reusable
harness. Next to skills sit the rule registry, which gives each skill the rules it supports; the
validators, which enforce what a skill only encourages; the evidence schema, which fixes the shape
of what a run records; and the adapters that bind the kit to the team's tools. In the map's core
row, Harness engineering comes before the kit and supplies the split between guides and sensors;
Workflows come after it and use skills inside their agent tasks and the review skill inside their
checks. The feedback path feeds all of this: a procedure the agent keeps needing becomes a skill,
and a failure in production becomes a new eval case.[^bockeler-harness]

## Pitfalls

- **A skill carrying a rule that must always hold.** The only defence for the access rule is a
  paragraph in a skill. Sign: a rule routed to a gate in the registry has skills citing it but no
  validator.
- **Shipping on one good run.** The skill passed once, on one model, and nobody kept the result.
  Sign: no baseline comparison, a single trial per case, and no model version in the record.
- **Evals that grade the skill against itself.** Expected behaviour is copied from the skill's text,
  so the eval can only confirm what the skill already says. Sign: case descriptions that paraphrase
  the skill rather than the specification or the rule.
- **Only happy-path cases.** Every case expects the skill to produce a change. Sign: no case in
  which the skill should stay out of the way, and the skill starts rewriting exports that were
  already correct.
- **An unchecked model grader.** The model-based grader's scores are accepted without anyone reading
  transcripts.[^anthropic-agent-evals] Sign: no record of how often the grader and a person agree.
- **Stale history.** The model or a cited rule changed and the evals did not run again. Sign: the
  last recorded run names an older model, tool or rule version than the one in use.
- **Re-running a flaky case until it passes.** Sign: the same case alternates between pass and fail
  across runs, and the recorded result is only the last one.[^agentskills-evaluating]
- **Skills without a failure behind them.** Skills written on speculation pile up, each one more
  thing to maintain. Sign: nobody can name the repeated miss a skill fixes, who answers for it, or
  when its evals last ran.
- **Outside skills installed unread.** A skill from another team or a public collection is someone
  else's instructions and code, acting with the agent's access. Sign: a skill in use that nobody on
  the team has read, or whose scripts nobody has checked for what they send or fetch. Putting it
  through the team's usual supply-chain review is recommended practice.
- **Treating review findings as verdicts.** The review skill's output decides merges, or reviewers
  dismiss it wholesale. Sign: merges approved or held on a finding alone, or findings closed
  without a reason.

## Related

- [Validators](validators.html): the deterministic checks that enforce what a skill only encourages.
- [Rule registry](rule-registry.html): where each rule's identifier, route and owner live, and
  which skills cite it.
- [Engineering Kit](engineering-kit.html): the package that carries skills, evals and the other
  parts.
- [Harness engineering](harness-engineering.html): the discipline, including guides, sensors and
  the two kinds of control.
- [Evidence schema](evidence-schema.html): the fixed shape of what a run records.
- [Workflows](workflows.html): where skills and the review skill are used in delivery.
- [Terminology](glossary.html#skill) and the [workflow catalog](workflow-catalog.html).

## Sources

- Guides and sensors, computational and inferential controls, and the feedback loop behind them:
  Böckeler, harness engineering.[^bockeler-harness]
- Inferential sensors, including AI review, and what they catch compared with computational ones:
  Böckeler, maintainability sensors.[^bockeler-sensors]
- Skills loaded on demand, and the probabilistic nature of agent behaviour: Böckeler, context
  engineering.[^bockeler-context]
- The skill format, on-demand loading and starting from evaluation: two published descriptions of
  the open skill format[^anthropic-agent-skills][^github-agent-skills] and one vendor's authoring
  guidance.[^claude-skill-practices]
- Tasks, trials, graders, pass@k and pass^k, regression suites and when evals run: practitioner
  guidance on evaluating agents.[^anthropic-agent-evals]
- Baselines, reruns per iteration and flaky cases: guidance for evaluating skills in the open
  format.[^agentskills-evaluating]
- Activation cases and comparing scores over time: guidance on testing skills with
  evals.[^openai-eval-skills]
- The pass^k reliability metric: Yao and colleagues.[^yao-tau-bench]
- Non-determinism in generated code: Ouyang and colleagues.[^ouyang-nondeterminism]
- Model graders, their agreement with people and their biases: Zheng and
  colleagues.[^zheng-llm-judge]
- Tracking agreement between model-based and human evaluation: Husain.[^husain-evals]
