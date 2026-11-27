---
id: operate
type: phase
band: lifecycle
map_box: Operate
title: Operate
summary: The phase in which released software runs in production and is kept in service, where it is monitored, its incidents are handled and reviewed, vulnerabilities and usage are answered, and lessons travel back to earlier work.
key_terms: [feedback-path, steering-loop, harness, software-factory, evidence-handoff, rule-registry, workflow, three-roles, harness-evaluation, export-example]
sources: [sre-book-monitoring, sre-book-being-on-call, sre-book-managing-incidents, google-sre-postmortem, nist-800-61r3, nist-ssdf, dora-monitoring-observability, dora-customer-feedback, dora-metrics, dora-2025-announcement, google-agentic-sre, ahmed-incident-llm, chen-rcacopilot, bockeler-harness, safe-inspect-and-adapt, safe-framework]
related: [harness-engineering, software-factory, workflows, evidence-schema, rule-registry, validators, specification, deploy, release, inspect-and-adapt, traceability-spine, incident-feedback]
review_record: content/reviews/1.5.0-lifecycle.md
---

## Purpose

Operate is the phase in which a released change runs in production and the team keeps it in
service: it watches how the software behaves, responds when it fails and learns from each failure.
The decisions taken here belong to the workflows listed below; the two at the centre of the phase
are incident remediation ([W27](workflow-catalog.html#W27)) and incident-to-development feedback
([W28](workflow-catalog.html#W28); see the [Incident feedback](incident-feedback.html) page), and their catalog rows state them.

In the AI SDLC (the software development lifecycle with AI agents doing part of the work), Operate
is where the lifecycle's loop closes. On the map, a dashed arrow leaves the Operate box and returns
to Specification, carrying the idea that incident feedback changes what Specification asks. The
phase produces incident records and their reviews, responses to vulnerabilities and to how the
product is used, and lessons that travel back upstream along the
[feedback path](glossary.html#feedback-path). The map labels the box Operate and nothing more.
The workflow catalog calls the phase "Operate & sustain": keeping released software in service
belongs here as well.

## Traditional practice

Without agents, people do every part of the phase: they watch the signals, answer the page,
coordinate the response, write the postmortem and decide what it changes.

### Monitoring and on-call

The site reliability engineering (SRE) book sets the purpose of monitoring plainly: "Your
monitoring system should address two questions: what's broken, and why?"[^sre-book-monitoring] It
names four golden signals of monitoring: latency, traffic, errors and saturation.[^sre-book-monitoring]
DORA separates monitoring, "tooling or a technical solution that allows teams to watch and
understand the state of their systems", from observability, which allows teams to actively debug
their system.[^dora-monitoring-observability]

When monitoring pages a person, the on-call engineer acts. The book's chapter on being on call says
that once a page is acknowledged, the engineer is expected to "triage the problem and work toward
its resolution, possibly involving other team members and escalating as needed", and that many
teams have both a primary and a secondary on-call rotation.[^sre-book-being-on-call]

### Managing incidents

An incident too large for one person needs structure. The book's chapter on managing incidents
says that Google's incident management system is based on the Incident Command System, splits the
response into separate roles, and states: "The operations team should be the only group modifying
the system during an incident."[^sre-book-managing-incidents] Where the response is to return to an
earlier version, that decision and its mechanics belong to [deploy](deploy.html).

### Learning after the incident

Once service is restored, a postmortem records what happened and what will change. The SRE
workbook's chapter on postmortem culture states that "The value of a postmortem is proportional to
the learning it creates", and notes that action items without clear owners are less likely to be
resolved.[^google-sre-postmortem]

### Security incidents and vulnerabilities

Security incidents have their own guidance. NIST SP 800-61 Revision 3, published on 3 April 2025
by Alex Nelson, Sanjay Rekhi, Murugiah Souppaya and Karen Scarfone, is titled *Incident Response
Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community
Profile*. In it, all six Functions of the Cybersecurity Framework 2.0 (Govern, Identify, Protect,
Detect, Respond and Recover) play a part in incident response, and lessons learned from all
activities feed the Improvement category. It supersedes Revision 2, withdrawn the same
day.[^nist-800-61r3] Its scope is cybersecurity incidents. A service failure with no security
dimension, such as a job that times out, is handled by the operational practice above.

For weaknesses in software already released, NIST's Secure Software Development Framework (SSDF)
version 1.1 names three practices: RV.1 "Identify and Confirm Vulnerabilities on an Ongoing Basis",
RV.2 "Assess, Prioritize, and Remediate Vulnerabilities" and RV.3 "Analyze Vulnerabilities to
Identify Their Root Causes".[^nist-ssdf]

### Usage, recovery and maintenance

Production also shows how people use the product. DORA places customer feedback in a wider group
of capabilities, with visibility of work, small batches and team experimentation, that together
help predict software delivery performance and organisational performance.[^dora-customer-feedback]
Recovery is measured as well: DORA's current guide lists failed deployment recovery time among its
five software delivery performance metrics, in the throughput group.[^dora-metrics] How such
measures are defined and read belongs to the assurance band, not to this page.

Keeping software in service is work in its own right, and it lasts as long as the software runs.
Much of it is not prompted by a new feature. The SSDF's first response practice asks producers to
identify and confirm vulnerabilities on an ongoing basis,[^nist-ssdf] so a release that passed
every check when it shipped can still need a change long afterwards, and the vulnerability response
workflow ([W29](workflow-catalog.html#W29)) handles that change. Usage evidence of the kind above
is another steady source of upkeep. At the end of a component's life the work is to retire it and
the data it holds, through decommission and data disposal ([W31](workflow-catalog.html#W31)).

## AI-assisted practice

Public evidence on agents in operations is thin: one operator's published account and a small body
of research, none of which reports outcome figures a team could plan on. What follows is
recommended practice unless a source is named. It is sorted by the
[three roles](glossary.html#three-roles) every workflow on this site has: the agent, the
deterministic checks and the people.

### What an agent takes on

Google's SRE organisation describes agents layered on its incident management that consolidate and
summarise data from the places where incident communication happens, create handoff documents and
create drafts of postmortems; in some cases its investigation agents use observability data to
mitigate autonomously.[^google-agentic-sre] It is one operator's account of its own practice, not a
study, and it gives no figures.[^google-agentic-sre]

Research has looked at root-cause work in particular. A study presented at ICSE 2023 evaluated
large language models for helping engineers find the root cause of production incidents and
recommend mitigation steps, over more than 40,000 incidents, in zero-shot, fine-tuned and
multi-task settings, with evaluation by the incidents' owners.[^ahmed-incident-llm] A preprint
describes a tool that matches incoming incidents to handlers by alert type, aggregates runtime
diagnostic information, predicts the incident's root-cause category and writes an explanatory
narrative; its authors report a root-cause accuracy of up to 0.766 on a year's worth of
incidents.[^chen-rcacopilot] Both describe what such systems proposed on the data they were tested
on, not how well they work elsewhere.

On that basis, the work that suits an agent in this phase is work that is costly for a person and
tolerable to get slightly wrong: pulling what monitoring shows into one readable picture, keeping a
running summary for the next person on call, offering a cause as a hypothesis, and preparing the
first version of a postmortem for people to finish.

### What deterministic checks hold

Google's account says its approach relies on "having consistent controls to prevent unwanted
mutations of production state".[^google-agentic-sre] DORA's 2025 research makes the general point:
without robust control systems, such as strong automated testing, mature version control practices
and fast feedback loops, an increase in change volume leads to instability.[^dora-2025-announcement]
In operations, as recommended practice, this means that an agent acts on production only through
permissions granted for its task, which the agent runtime in the enablement band supplies, and
that every action it takes is recorded. A fix written during an incident, by a person or an agent,
is held to the checks the incident remediation row ([W27](workflow-catalog.html#W27)) lists, like
any other change.

### What stays with people

Google's account states that an agentic approach "does not necessarily imply removing people from
the process, specifically for higher-risk services and features".[^google-agentic-sre] The SRE
book's rule that only the operations team modifies the system during an incident[^sre-book-managing-incidents]
extends to agents: an agent that may act on production works inside that team's line of command,
not beside it. People hold the decisions that need context the agent lacks: how to respond while
the incident is open, whether a proposed cause is the real one, and what the lesson should change.

### Where the lesson goes

Once an incident closes, its lesson travels the feedback path, this site's extension of the loop
Birgitta Böckeler calls the steering loop, in which people improve an agent's guides and checks
whenever an issue recurs.[^bockeler-harness] Where each kind of lesson lands is defined on
[harness engineering](harness-engineering.html), and the route from production back to
specification under
[Production feedback reaches specification](software-factory.html#production-feedback-reaches-specification)
on the Software factory page. Operate supplies the starting point: the incident, its review and the
evidence the release left behind.

In the customer-record export, a hypothetical feature that lets users export customer records, the
incident that reaches Operate is the one those pages describe: a scheduled full export, within the
volume-limit rule R-017's limit but far larger than the 50k-row load scenario, times out. The limit
was already in place; the incident exposed a volume nobody had tested or asked about, and the
changes that follow are set out on [software factory](software-factory.html).

## Workflows in this phase

Five rows of the [workflow catalog](workflow-catalog.html) run here. They sit in catalog phase 7,
"Operate & sustain", which corresponds to the map's Operate box; rows that cut across the whole
lifecycle, such as change control and exceptions, belong to no single phase.

- [Incident remediation](workflow-catalog.html#W27): the response while an incident is open.
- [Incident-to-development feedback](workflow-catalog.html#W28) (see the [Incident feedback](incident-feedback.html) page): the lesson once it has closed.
- [Vulnerability response](workflow-catalog.html#W29): security weaknesses found in what is
  running.
- [Usage and feedback intake](workflow-catalog.html#W30): feedback from the people who use the
  product.
- [Decommission and data disposal](workflow-catalog.html#W31): the end of a component's life.

[Incident-to-development feedback](incident-feedback.html) is the workflow the map draws on the Operate box, as the bar
labelled "incident feedback", because it starts the loop back to Specification. The lessons it
carries follow the feedback path defined on [harness engineering](harness-engineering.html). Its
records are read again at the site's [inspect and adapt](inspect-and-adapt.html) checkpoint, where
owners check whether each lesson landed; the name comes from SAFe, which uses it for an event held
at the end of each Planning Interval (PI).[^safe-inspect-and-adapt][^safe-framework] The
[traceability spine](traceability-spine.html) carries the link from the release to the incident and
back to the requirement.

## Gates and evidence

Operate has no merge to gate. Its entry is a release running in production, reached through
[release](release.html) and [deploy](deploy.html), and the record those phases leave is the first
thing an incident review reads; the glossary calls this the
[evidence hand-off](glossary.html#evidence-handoff). Evidence names the revision it covers, so a
review can tell which version of the software was running when the incident began.

Inside the phase there are two kinds of gate. While an incident is open, the gate is on what may
change production: the SRE book confines changes to the operations team,[^sre-book-managing-incidents]
and the controls described above under AI-assisted practice apply to any agent working in that
team. After the incident, the gate is on closure itself. The SRE workbook observes that action
items without clear owners are less likely to be resolved,[^google-sre-postmortem] so, as
recommended practice, a review stays open while any of its actions has no named owner. Where each
lesson lands is set out on the Software factory page, under
[Production feedback reaches specification](software-factory.html#production-feedback-reaches-specification).

Security work closes the same way: NIST's profile sends lessons learned to its Improvement
category,[^nist-800-61r3] and SSDF practice RV.3 asks for the root causes of each
vulnerability.[^nist-ssdf]

Each record takes the shape the [evidence schema](evidence-schema.html) fixes, and this page adds no
field to it.

## Roles

Operate is owned by the people who run the software in production. The on-call engineer answers the
page, triages and works toward resolution, bringing in others and escalating as
needed.[^sre-book-being-on-call] For a larger incident, the SRE book's chapter on managing incidents
names four roles: incident command, operational work, communication (described as "the public face
of the incident response task force") and planning.[^sre-book-managing-incidents] This page uses
those roles as the book names them and adds none.

After the incident, each postmortem action has one named owner, and a lesson that changes a shared
rule goes to that rule's named owner in the [rule registry](rule-registry.html).
Agents hold none of these roles; they prepare material for the people who do. How decision rights
are divided between titles belongs to the operating model in the enablement band.

## Pitfalls

- **Actions with no owner.** The review lists what should change but names nobody to change it,
  and such actions are less likely to be resolved.[^google-sre-postmortem] Sign: actions from
  earlier incidents still open.
- **A lesson that stops at the code.** Sign: the next change of the same kind meets the same miss.
  See
  [software factory](software-factory.html#production-feedback-reaches-specification).
- **An agent that can change production unchecked.** An agent acts on production outside the
  controls that bind people; Google's account relies on consistent controls to prevent unwanted
  mutations of production state.[^google-agentic-sre] Sign: production changes with no recorded
  actor or no permission that covers them.
- **An agent's root cause taken as fact.** A proposed cause drives a change before anyone has
  tested it. Sign: a postmortem whose cause nobody can explain without the agent's narrative. The
  preprint above reports root-cause accuracy of up to 0.766 on the year of incidents it was tested
  on,[^chen-rcacopilot] and the larger study was evaluated by incident
  owners.[^ahmed-incident-llm] As recommended practice, a person confirms the cause before it
  changes anything upstream.
- **Alerts that say nothing useful.** Pages fire, but they do not tell the on-call engineer what is
  broken or why.[^sre-book-monitoring] Sign: every page starts with a search for what it means.
- **A security profile used as the only incident process.** NIST SP 800-61 Revision 3 addresses
  cybersecurity incidents;[^nist-800-61r3] as recommended practice, failures with no security
  dimension keep an operational process of their own. Sign: a service outage with no clear route.

## Related

- [Specification](specification.html): where the loop from Operate lands, as a readiness question.
- [Release](release.html) and [Deploy](deploy.html): the phases before this one; a return to an
  earlier version is decided in Deploy.
- [Inspect and adapt](inspect-and-adapt.html): the checkpoint that reads whether incident lessons
  landed.
- [Traceability spine](traceability-spine.html): the chain from requirement to incident.
- [Harness engineering](harness-engineering.html): the discipline whose steering
  loop[^bockeler-harness] the incident lessons feed.
- [Software factory](software-factory.html): how production feedback reaches specification.
- [Workflows](workflows.html), [Evidence schema](evidence-schema.html),
  [Rule registry](rule-registry.html) and the page on
  [deterministic rule checks](validators.html): the unit of work, its record, the shared rules and
  the checks a lesson can tighten.
- [Incident feedback](incident-feedback.html): which earlier control changes after an incident.
- [Workflow catalog](workflow-catalog.html#W28): incident-to-development feedback, with
  [W27](workflow-catalog.html#W27), [W29](workflow-catalog.html#W29),
  [W30](workflow-catalog.html#W30) and [W31](workflow-catalog.html#W31).
- Terminology: [feedback path](glossary.html#feedback-path),
  [evidence hand-off](glossary.html#evidence-handoff) and
  [three roles](glossary.html#three-roles).

## Sources

- Rob Ewaschuk (edited by Betsy Beyer), *Monitoring Distributed Systems*, chapter 6 of the SRE
  book: the two questions and the four golden signals.[^sre-book-monitoring]
- Andrea Spadaccini (edited by Kavita Guliani), *Being On-Call*, chapter 11 of the SRE book: what
  the on-call engineer does after a page, and primary and secondary
  rotations.[^sre-book-being-on-call]
- Andrew Stribblehill (edited by Kavita Guliani), *Managing Incidents*, chapter 14 of the SRE book:
  the Incident Command System basis, the four roles and the operations team as the only group
  modifying the system.[^sre-book-managing-incidents]
- Daniel Rogers, Murali Suriar, Sue Lueder, Pranjal Deo and Divya Sudhakar, with Gary O'Connor and
  Dave Rensin, *Postmortem Culture: Learning from Failure*, chapter 10 of the SRE workbook: learning
  and action-item ownership.[^google-sre-postmortem]
- Alex Nelson, Sanjay Rekhi, Murugiah Souppaya and Karen Scarfone, NIST SP 800-61 Revision 3
  (3 April 2025): the cybersecurity incident response profile.[^nist-800-61r3]
- Murugiah Souppaya, Karen Scarfone and Donna Dodson, NIST SSDF version 1.1 (SP 800-218): the RV
  practices for responding to vulnerabilities.[^nist-ssdf]
- DORA on monitoring and observability, on customer feedback, and Nathen Harvey's guide to the
  software delivery performance metrics.[^dora-monitoring-observability][^dora-customer-feedback][^dora-metrics]
- DORA's 2025 report announcement on control systems and change volume.[^dora-2025-announcement]
- Stevan Malesevic and Christopher Heiser, *AI in SRE: Where and how Google is deploying agentic AI
  to improve operations* (28 May 2026): one operator's account.[^google-agentic-sre]
- Ahmed and colleagues, ICSE 2023, and Chen and colleagues, an arXiv preprint: language models for
  incident root-cause analysis.[^ahmed-incident-llm][^chen-rcacopilot]
- Birgitta Böckeler on the steering loop.[^bockeler-harness]
- Scaled Agile, Inc. on SAFe's Inspect and Adapt event and the Planning
  Interval.[^safe-inspect-and-adapt][^safe-framework]
- Statements marked as recommended practice are this site's own and are not findings of any study.
