---
id: agent-permissions
type: role-or-practice
band: assurance
map_box: Agent permissions reviewed as privileged access
title: Agent permissions and access review
summary: The practice of managing every agent identity as an account with an owner, an approved grant and only the access its task needs, and of applying the controls for privileged accounts wherever an agent's identity holds privileged access, so that what an agent may do is reviewed and evidenced like any other account.
key_terms: [ai-sdlc, least-privilege, excessive-agency, workflow, three-roles, evidence-record, export-example]
sources: [nist-800-53, nist-glossary-least-privilege, owasp-llm06-2025, nist-ai-rmf, incident-owasp-logging, bockeler-harness]
related: [harness-engineering, workflows, evidence-schema, engineering-kit, adapters, deploy, deploy-verification, operate, incident-feedback, release, develop-build-qa, design-conformance]
review_record: content/reviews/1.7.0-assurance.md
---

## Purpose

In an AI SDLC (the software development lifecycle with AI agents doing part of the work), a coding
agent reads repositories, calls tools and writes changes under an identity, such as a token or a
service account. What that identity may do is the outer limit of what the agent can do, whatever its
instructions say. This practice manages each such identity as an account: it has an owner, its
rights are granted on approval and recorded, its use is watched, it is reviewed, and it is removed
once nothing needs it.

The practice rests on NIST SP 800-53, the NIST catalogue of security and privacy controls. Its
least-privilege control, AC-6, allows "only authorized accesses for users (or processes acting on
behalf of users) that are necessary to accomplish assigned organizational tasks".[^nist-800-53] An
agent is such a process, so AC-6 applies to it directly; NIST's glossary gives the same principle
as each entity holding the minimum authorisations its function needs.[^nist-glossary-least-privilege]
The account-management control, AC-2, lists service accounts among the account types an
organisation may define.[^nist-800-53] Treating an agent identity as an account under AC-2 is this
site's reading of the two controls; neither mentions agents.

The map's label, "reviewed as privileged access", needs a qualification. NIST does not treat every
account as privileged: AC-2's discussion asks for additional scrutiny of accounts with
administrative privileges, and enhancements to AC-6 restrict privileged accounts to defined
personnel or roles and log the execution of privileged functions.[^nist-800-53] Every agent identity
is a managed account. The privileged-account controls apply where an agent's identity actually holds
privileged access, such as administrative rights over a system. What makes an identity privileged
is what it may do, not its being an agent.

The risk behind the practice has a public name. OWASP's Top 10 for large language model (LLM)
applications calls it *excessive agency*: the vulnerability that enables damaging actions in
response to unexpected, ambiguous or manipulated model output.[^owasp-llm06-2025] Keeping an agent
in scope through its permissions is part of harness design
([Harness engineering](harness-engineering.html#computational-and-inferential-controls)); this page
covers granting, reviewing and removing those permissions, and the evidence each step leaves.

## Responsibilities

The practice owns the account side of every agent identity. The items below follow the order in
which AC-2 lists them, with AC-5 and AC-6 beside it; that is the order of the control's text, not a
sequence of steps NIST prescribes.[^nist-800-53]

- **Account types.** Define which types of account are allowed and which are prohibited (AC-2a),
  including whether agent identities form a type of their own.
- **An owner.** Assign account managers (AC-2b). No person sits behind an agent identity, so a named
  person answers for it. No public source names that role for agents.
- **What each account may do.** Specify each account's users, group and role membership, and access
  authorisations (AC-2d): for an agent, the tools and data its task needs.
- **Approval.** Require approval by people or roles the organisation names for requests to create
  accounts (AC-2e), and restrict privileged accounts to defined personnel or roles (AC-6(5)).
- **Changes.** Create, enable, modify, disable and remove accounts under the organisation's policy
  and criteria (AC-2f).
- **Monitoring.** Monitor account use (AC-2g), log the execution of privileged functions (AC-6(9))
  and audit account actions automatically (AC-2(4)).
- **Notice and disabling.** Notify account managers when an account is no longer required (AC-2h),
  and disable accounts that have expired, lost their user, violate policy or sat inactive for a
  period the organisation sets (AC-2(3)).
- **Review.** Review accounts at a frequency the organisation defines (AC-2j), and review assigned
  privileges to validate the need for them, removing them where necessary (AC-6(7)). NIST sets no
  frequency, period or approver, and this page sets none.
- **Separation of duties.** Define access authorisations that support the separation of duties
  (AC-5), so the identity that produces a change cannot accept it. How the evidence record keeps
  the writers apart is on [Evidence schema](evidence-schema.html#who-writes-each-field).

The audit records of account actions and the log of privileged functions are the evidence the
controls themselves name.[^nist-800-53] As recommended practice, each grant, review outcome and
removal also names the person who decided it, in the form the
[evidence schema](evidence-schema.html#agent-findings-and-decisions) gives decisions. That is one
way to meet the NIST AI Risk Management Framework's call to define roles and responsibilities for
the oversight of AI systems (GOVERN 3.2).[^nist-ai-rmf]

### The customer-record export

In the site's running example, a hypothetical feature that lets application users export customer
records, the published runs already bound the agent's identity: nothing it may do reaches the
decision fields of the evidence record ([Workflows](workflows.html#the-three-roles-agent-checks-and-people)),
and the agents in [deploy verification](deploy-verification.html#guardrails) and
[incident feedback](incident-feedback.html#guardrails) hold no write access to production. This
practice adds the account view: each of those identities has an owner, an approved grant and a
review on record. Logs from the failed export run may contain customer records, and OWASP's logging
guidance says privileges to read log data "should be restricted and reviewed
periodically";[^incident-owasp-logging] the incident-feedback agent's read access to those logs is
reviewed like a person's. The access rule R-042, which says which records an application user may
export, is a separate matter: it governs the product's users, not the agent's identity.

## What shifts with agents

OWASP traces excessive agency to three root causes: excessive functionality, excessive permissions
and excessive autonomy.[^owasp-llm06-2025] As account questions: does the agent hold a tool beyond
its task, such as delete where it only needs to read; a downstream right beyond its task, such as
write where read would do; or the ability to take a high-impact action with no independent check or
user confirmation? A review of an agent's account asks all three.

OWASP's mitigations move decisions out of the agent. Extensions run in the context of the user they
act for, with minimal privileges; high-impact actions need a person's approval; and authorisation is
enforced by the downstream system, not decided by the model, which OWASP calls complete
mediation.[^owasp-llm06-2025] Logging, monitoring and rate limiting limit the damage but, OWASP
notes, do not prevent excessive agency.[^owasp-llm06-2025]

Grants follow tasks rather than people's jobs, since each
[workflow](workflows.html#the-three-roles-agent-checks-and-people) grants its agent only what its
task needs. As recommended practice, the larger number of identities and grants that results makes
automatic audit of account actions (AC-2(4)) matter more. No public source counts agent identities,
and this page gives no figures.

What does not shift is the control set. AC-6 applies least privilege to processes acting on behalf
of users as well as to users,[^nist-800-53] and, on this site's reading, an agent identity still
needs an owner, an approved grant, monitoring, review and removal.

## Warning signs

- **A standing broad credential.** An agent identity holds rights beyond its task (AC-6; OWASP's
  excessive permissions).[^nist-800-53][^owasp-llm06-2025] The production case is among the
  [Deploy](deploy.html#pitfalls) pitfalls.
- **No review on record.** No review date or outcome for the period the organisation set (AC-2j,
  AC-6(7)).[^nist-800-53]
- **An idle or orphaned identity still enabled.** The account is inactive, or the workflow it served
  is gone, and it still works (AC-2(3)).[^nist-800-53]
- **No owner named.** Nobody is recorded as account manager (AC-2b).[^nist-800-53]
- **Unlogged privileged actions.** Privileged functions or account changes leave no record (AC-6(9),
  AC-2(4)).[^nist-800-53]
- **An open-ended tool.** A general-purpose tool, such as an unrestricted shell, where a narrower one
  would do; OWASP advises avoiding open-ended extensions.[^owasp-llm06-2025]
- **Authorisation left to the model.** Whether an action is allowed depends on the agent's
  instructions or its own judgment, not on a check in the system it calls; OWASP's complete
  mediation places that decision in the downstream system.[^owasp-llm06-2025]
- **High-impact actions with nobody approving.** The identity can take a high-impact action with no
  independent check and no person's approval, OWASP's excessive autonomy; OWASP advises requiring
  user approval for such actions.[^owasp-llm06-2025]

## Related

- [Harness engineering](harness-engineering.html#computational-and-inferential-controls) and
  [Workflows](workflows.html#the-three-roles-agent-checks-and-people): least privilege in the harness
  and in each workflow.
- [Evidence schema](evidence-schema.html): who may write each field of the record.
- [Engineering Kit](engineering-kit.html#what-an-installation-must-prove) and
  [Adapters](adapters.html): the permissions an installation must prove.
- Agents near production: [Deploy](deploy.html), [Deploy verification](deploy-verification.html),
  [Operate](operate.html#what-deterministic-checks-hold) and
  [Incident feedback](incident-feedback.html).
- Other phases: [Release](release.html), [Develop, Build and QA](develop-build-qa.html) and
  [Design conformance](design-conformance.html).
- Terminology: [least privilege](glossary.html#least-privilege),
  [excessive agency](glossary.html#excessive-agency) and the
  [export example](glossary.html#export-example).

## Sources

- Account management, least privilege and separation of duties: NIST SP 800-53 Rev. 5, AC-2, AC-2(3),
  AC-2(4), AC-5, AC-6, AC-6(5), AC-6(7) and AC-6(9).[^nist-800-53]
- Least privilege defined: the NIST glossary.[^nist-glossary-least-privilege]
- Excessive agency, its root causes and mitigations: OWASP Top 10 for LLM Applications 2025,
  LLM06.[^owasp-llm06-2025]
- Roles for the oversight of AI systems: the NIST AI Risk Management Framework, GOVERN
  3.2.[^nist-ai-rmf]
- Access to log data: the OWASP Logging Cheat Sheet.[^incident-owasp-logging]
- Treating an agent identity as an account under AC-2, recording the decider of each grant, review and removal, and the added weight of
  automatic audit are this site's reading and recommended practice.
- Harness and harness engineering: Böckeler[^bockeler-harness].
