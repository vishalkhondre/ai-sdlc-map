---
id: ai-use-policy
type: concept
band: assurance
map_box: "AI use policy: data sent to models, IP of generated code"
title: AI use policy
summary: The policy an organisation sets for using AI in software delivery, covering which data may be sent to which models and how generated code is checked for provenance and licence, and how that policy becomes rules with owners and evidence in every run's record; it frames legal questions as policy questions and draws no legal conclusion.
key_terms: [ai-sdlc, ai-use-policy, rule-registry, validator, review-skill, evidence-record, workflow, export-example]
sources: [nist-ai-rmf, nist-ai-600-1, nist-800-53, nist-ssdf, slsa-provenance, spdx-overview, spdx-ids, lf-generative-ai, incident-owasp-logging, dora-metrics, bockeler-harness, bockeler-sensors]
related: [agent-permissions, change-controls-and-standards, evidence-record, check-results-and-decisions, rule-registry, evidence-schema, workflows, harness-engineering, incident-feedback, release]
review_record: content/reviews/1.7.0-assurance.md
---

## Definition

An AI use policy, in software delivery, is an organisation's stated position on how AI systems may
take part in delivery work: which data may be given to which models and on what terms, and what
code produced by an AI system must pass, and how it is disclosed, before it is accepted. In an AI
SDLC (the software development lifecycle with AI agents doing part of the work), each point of the
policy is held as a rule with an owner and is enforced by
checks, by a named person who decides, or by both. That person need not sit in the delivery team
where a point belongs to an organisation-wide data or access control. The NIST AI Risk Management
Framework (AI RMF) expects policies, processes, procedures and practices for managing AI risks to be in place,
transparent and implemented effectively (GOVERN 1)[^nist-ai-rmf], and NIST's generative AI profile
speaks of "acceptable use policies" for generative AI that cover proprietary and open-source
technologies and data, including staff from contractors and other third parties
(GV-6.1-010)[^nist-ai-600-1]. "AI use policy" is a common term with no single originator.

## Why it matters

A coding agent sends material to a model as an ordinary part of its task: code, specifications,
sometimes records it was asked to read. What may leave the organisation that way is a policy
decision, and an agent's instructions are not the place to make it. NIST's generative AI profile
names the risks at stake. Its list includes Data Privacy, the leakage or unauthorised use or
disclosure of personal and sensitive data, and Intellectual Property, the eased production or
replication of copyrighted or licensed content without authorisation[^nist-ai-600-1]. It also names
Value Chain and Component Integration: upstream third-party components integrated in ways that are
not transparent or cannot be traced[^nist-ai-600-1]. This site reads a model reached through an
external service as such a component.

The AI RMF asks for policies and procedures that address AI risks from third-party software, data
and entities, including the risk of infringing a third party's intellectual property or other
rights (GOVERN 6 and 6.1)[^nist-ai-rmf]. Delivery teams meet that risk in two places: in what they
send out, and in the generated code they take back in.

Without enforcement the policy suffers the weakness that the
[Rule registry](rule-registry.html#why-it-matters) page describes for any rule held only in prose.

## How it works

The map names two subjects, in this order: data sent to models, and the intellectual property of
generated code. Each becomes a set of policy questions, the questions become rules, and the rules
leave evidence.

### Data sent to models

The first question is which data may be sent to which external service. NIST SP 800-53 treats any
such service through its external system services control: providers must comply with the
organisation's security and privacy requirements, and the organisation monitors their compliance on
an ongoing basis (SA-9a, SA-9c)[^nist-800-53]. NIST's generative AI profile suggests inventorying the
third parties that have access to organisational content and keeping approved lists of providers
(GV-6.1-007)[^nist-ai-600-1]. That is one NIST suggestion, not a scheme this site prescribes.

The second question is on what terms. How long a provider keeps what it receives, and whether it may
use that material to train models, are questions the policy answers in its agreements with
providers; framing them as policy questions is this site's recommended practice. The profile
supports the underlying step, extending procurement due diligence to intellectual property, privacy
and security (GV-6.1-009)[^nist-ai-600-1].

The third question is what should not reach a model at all. Logs are a published case: OWASP's
logging guidance says sensitive personal data should usually not be recorded directly in logs and
that access to log data should be restricted[^incident-owasp-logging], and the
[Incident feedback](incident-feedback.html#guardrails) page applies that to an agent reading
incident data. What an agent's identity may read is on [Agent permissions](agent-permissions.html).

### Generated code: provenance, licence and disclosure

NIST's Secure Software Development Framework asks producers to acquire and maintain well-secured
third-party components, with provenance data such as software bills of materials among its examples
(PW.4.1), and to verify that those components keep meeting requirements throughout their life cycle
(PW.4.4)[^nist-ssdf]. The framework says this about components, not about generated code. As
recommended practice, generated code meets the same checks a third-party component meets.

Provenance records answer part of the question. SSDF's PS.3 keeps each release with its provenance
data[^nist-ssdf], and SLSA defines provenance as verifiable information about where, when and how an
artifact was produced[^slsa-provenance]. Both describe how a release was built, not who or what
wrote a given line, so they place generated code in the release record without marking it as
generated.

Licence needs a check that a tool can run. SPDX, an open standard published as ISO/IEC 5962:2021,
communicates software bill of materials information, licence included[^spdx-overview], and its short
identifiers state a file's licence in one line that people and machines can read[^spdx-ids]. As
recommended practice, a licence check on generated changes and their dependencies is held as a rule
with an enforcing check, which also serves the release readiness decision
([W25](workflow-catalog.html#W25)).

Disclosure is a policy choice. The Linux Foundation's guidance for its projects accepts code
generated with AI tools, asks that it be developed and reviewed like any other code, asks
contributors to confirm that a tool's terms do not conflict with the project's licence, and asks
that third-party material appearing in output be used only with permission, notice and
attribution[^lf-generative-ai]. It does not require generated code to be marked as such. Whether and
how generated contributions are marked therefore remains a question that, as recommended practice,
each policy answers explicitly.

### From policy to rules and evidence

Each policy point enters the registry as an entry with an owner and a stated enforcement
([Rule registry](rule-registry.html#entering-changing-and-retiring-rules)). The
profile suggests connecting generative AI policies to existing software development, legal,
compliance and risk processes (MP-4.1-003)[^nist-ai-600-1], which is why the policy uses the same
registry as other rules rather than a parallel list.

Results and decisions land in each run's record under the rule's identifier
([Evidence schema](evidence-schema.html#check-results)), and what each result means for a merge is on
[Check results and decisions](check-results-and-decisions.html). The record gains no field for the
policy; the reasons the schema stays fixed are under
[Why the schema is fixed](evidence-schema.html#why-the-schema-is-fixed).

As recommended practice, the evidence is read per workflow or per run: which rule held on which
change. It is not read as a report on individual developers. DORA gives related advice for its
delivery metrics, applying them at the level of an application or service and not using them to set
teams against each other[^dora-metrics].

### Who answers the legal questions

Some questions the policy raises are legal: who owns generated code, whether a licence obligation
attaches to it, whether sending some data to a given service is lawful. This page answers none of
them. The AI RMF expects legal and regulatory requirements involving AI to be understood, managed and
documented (GOVERN 1.1), roles, responsibilities and lines of communication to be documented and
clear (GOVERN 2.1), and approaches for mapping the legal risks of components, including
infringement of intellectual property, to be in place (MAP 4.1)[^nist-ai-rmf]. As recommended
practice, each policy point with a legal side names who decides it with counsel, and the registry
entry records that person as the decider.

### The customer-record export

The site's running example is a hypothetical feature that lets users export customer records. Two
policy questions arise from published facts about it, and each is described here without a rule
identifier or result.

*Data.* The review skill, an agent, reads the export's change against its specification and the
rules R-042 and R-017 ([Workflows](workflows.html#the-parts-of-a-workflow-definition)), so the
export's code reaches the model that agent uses. After the production incident, logs from the failed
run may hold customer records ([Incident feedback](incident-feedback.html#guardrails)). Whether those
logs may be given to a model at all, and on what terms, is a point of the AI use policy held as a
rule with an owner; the agent does not decide it (recommended practice).

*Generated code.* The agent that wrote the export code does not decide whether it satisfies R-042
([Workflows](workflows.html#the-three-roles-agent-checks-and-people)). As recommended practice, that
code also passes the provenance and licence checks the policy requires of any change, and their
results appear in the run's record under the rule they enforce.

## Where it sits on the map

The page covers one bullet of the map's assurance band, the band of what must be provable: "AI use
policy: data sent to models, IP of generated code", in the standards and AI governance column. Beside
it are [Change controls and standards](change-controls-and-standards.html), which meets external
control frameworks through the same rules and records, and [Agent permissions](agent-permissions.html),
which governs what an agent's identity may do. The policy reads from the core band's
[Rule registry](rule-registry.html) and [Evidence schema](evidence-schema.html); the
[Evidence record](evidence-record.html) page describes how its evidence is read afterwards. The models
and the agent runtime themselves sit in the enablement band.

## Pitfalls

- **Policy as a document only.** The policy exists but no rule carries it, the weakness the
  [Rule registry](rule-registry.html#why-it-matters) page describes. Sign: no registry entry cites a
  policy point, and no check or named decider enforces one.
- **Data leaving through an agent's context.** Material reaches a model because an agent read it,
  not because anyone chose to send it, one way the Data Privacy risk in NIST's profile can
  arise[^nist-ai-600-1]. Sign: no rule covers what an agent may read and pass to a model
  (recommended practice).
- **Generated code let in more easily than components.** Checks that SSDF practice applies to
  third-party components[^nist-ssdf] are skipped for generated changes. Sign: licence or provenance
  checks that run on dependencies but not on generated code (recommended practice).
- **The policy used to watch people.** Evidence meant to show the policy holds is turned on
  individuals. Sign: policy results reported per developer rather than per workflow or run
  (recommended practice).
- **A legal answer written by engineering alone.** The AI RMF expects legal requirements and roles to
  be documented[^nist-ai-rmf]. Sign: a rule on intellectual property or data with no named decider
  outside the engineering team (recommended practice).

## Related

- [Agent permissions](agent-permissions.html): what an agent's identity may read and do.
- [Change controls and standards](change-controls-and-standards.html): external control frameworks
  met through rules, checks and records.
- [Evidence record](evidence-record.html) and
  [Check results and decisions](check-results-and-decisions.html): how a run's record and its results
  are read.
- [Rule registry](rule-registry.html) and [Evidence schema](evidence-schema.html): where policy points
  are held and where their results land.
- [Workflows](workflows.html) and [Harness engineering](harness-engineering.html): the agent, checks
  and people in each run, and what the agent reads.
- [Incident feedback](incident-feedback.html) and [Release](release.html): incident data handled by an
  agent, and the release record.
- Workflow catalog: release readiness, [W25](workflow-catalog.html#W25).
- Terminology: [AI use policy](glossary.html#ai-use-policy), [rule registry](glossary.html#rule-registry)
  and the [export example](glossary.html#export-example).

## Sources

- Risk framing and governance: the NIST AI Risk Management Framework, GOVERN 1, 1.1, 2.1, 6 and 6.1
  and MAP 4.1[^nist-ai-rmf]; NIST AI 600-1, the generative AI profile, for the Data Privacy,
  Intellectual Property and Value Chain and Component Integration risks and suggested actions
  GV-6.1-007, GV-6.1-009, GV-6.1-010 and MP-4.1-003[^nist-ai-600-1].
- External services: NIST SP 800-53 Rev. 5, SA-9[^nist-800-53].
- Components and provenance: NIST SSDF, PW.4.1, PW.4.4 and PS.3[^nist-ssdf]; SLSA build
  provenance[^slsa-provenance].
- Licence identification: the SPDX overview and SPDX short identifiers[^spdx-overview][^spdx-ids].
- Generated contributions: the Linux Foundation's guidance on generative AI tools[^lf-generative-ai].
- Sensitive data in logs: the OWASP Logging Cheat Sheet[^incident-owasp-logging]. Level at which
  measures are read: DORA's metrics guide[^dora-metrics].
- Retention and training terms as policy questions, applying component checks to generated code, the
  licence check as a rule, explicit disclosure, reading evidence per run, and a named decider for
  legal questions are this site's recommended practice. This page draws no legal conclusion.
- Harness and harness engineering: Böckeler[^bockeler-harness].
- Computational and inferential controls, and the validator and review-skill vocabulary: Böckeler[^bockeler-sensors].
