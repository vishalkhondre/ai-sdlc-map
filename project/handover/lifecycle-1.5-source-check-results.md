# Lifecycle 1.5 source check: results

Session date and accessed date for every entry: **2026-11-20**. Worklist: `project/handover/lifecycle-1.5-source-check-worklist.md`. Public sources only.

## Method and limits

- **Direct reading.** Every source was fetched with a plain HTTP GET (redirects followed, no browser disguise, no search results, no archives). The page text was saved and each claim was checked against that text. Quotes below come from text read; where a page prints no author or date, the entry says so.
- **Eight readers, one brief.** The work was split by worklist section across eight reading passes using the same method; each wrote one part, merged below without re-wording, under the heading naming its slice. Verdicts follow the worklist: SUPPORTED, PARTLY, NOT SUPPORTED, NOT FOUND.
- **Substitutes, named.** Only these substitutions were made, and each is labelled in its entry: `github.com` pages (refused plain requests) read as the same file from `raw.githubusercontent.com`; the ISTQB glossary term pages (empty without JavaScript) read from the glossary's own data endpoint `api.glossary.istqb.org`; and the authors' arXiv preprints for Rath 2018, Perry 2023 and Pearce 2022, where ACM and IEEE refused or returned nothing. A preprint is not the published version.
- **Not readable.** Where a host refused (HTTP 403, a Cloudflare challenge, name-resolution failure) the source is marked `not read directly` and its claims `NOT FOUND (not readable)`. Nothing was filled in from memory or search. The full list is in part F.
- **Login wall.** Many SAFe articles return only the definition, summary and headings to a plain request, then "Log in to continue reading". Claims that depend on the hidden text are `NOT FOUND (not readable)`.
- **Not done.** Nothing in `content/` or any page was edited. The reader passes did not run the library sweep (that belongs to page work, D-026).

## Summary

- Claim rows in part B: **303** — SUPPORTED 197, NOT FOUND (not readable) 53, PARTLY 45, NOT FOUND (read, absent) 7, NOT SUPPORTED 1.
- SAFe allow-list (part C): 47 terms — 39 SUPPORTED, 8 PARTLY, none NOT SUPPORTED; six of the 39 only at a better SAFe URL than the one listed; term 41 (Definition of Done) is readable only in the glossary.
- Sources not read directly: see part F. The main groups are the iso.org catalogue pages (all 403), the ACM, Wiley, UCL and scrum.org hosts (403), three hosts that failed name resolution, and book text (Humble and Farley chapter 10, Reinertsen).
- Where the worklist and the page disagree, the headline corrections are in part E; the entries in part A already carry the corrected values.

### Findings most likely to change a page

1. **AI-Native SAFe.** "Customer Demos replace System Demo" is not supported as worded: System Demo activities are absorbed into Sense and Respond; Customer Demos are a separate practice. 2026-06-23 is the date of the launch blog post, not a release date. The What's new page prints no release date and no "fully supported" wording. See part D, question 3.
2. **Definition of Ready.** SAFe has no glossary entry for it; the Scrum Guide does not define it (its 2013 revision history uses "Ready" for refined items). See part D, question 1.
3. **Cadence wording is "typical", not required** (PI 8 to 12 weeks, PI Planning two days, Iteration Planning about 90 minutes for a two-week iteration). See part C and part D.
4. **SAFe version label.** No Core article prints a version; the only "SAFe 6.0" label is on the configurations page and a home-page link. "Core SAFe" is SAFe's own label.
5. **ISO.** None of the ISO catalogue pages could be read, so the 12207 second-edition claim, the 29148 characteristic list and order, and the 14764 maintenance types stay unconfirmed. Recommendation from the reader: leave them out of the site until someone reads the standards.
6. **DORA.** The current metrics page is `https://dora.dev/guides/dora-metrics/` (five metrics; failed deployment recovery time sits under throughput). The seven AI capabilities are named only in the announcing blog post, not on the dora.dev capabilities-model report page.
7. **NIST.** SP 800-61 Rev. 3 was published 3 April 2025 and Rev. 2 was withdrawn the same day. SSDF v1.2 (SP 800-218 Rev. 1) is still an initial public draft; v1.1 remains final.
8. **ISTQB.** The glossary wording for acceptance criteria differs from the drafted wording (NOT SUPPORTED).
9. **Deploy versus release attribution.** No page read credits anyone with the distinction. See part D, question 7.

## Index of open questions (section 4 of the worklist) to where answered

| Q | Topic | Answered in part D under |
|---|---|---|
| 1 | Definition of Ready originator and dates | Scrum, agile and requirements practice |
| 2 | Inspect and adapt before SAFe | Scrum, agile and requirements practice (SAFe first use not settled) |
| 3 | Scrum Guide 2020 current; Expansion Pack | Scrum, agile and requirements practice |
| 4 | NIST SP 800-61 Rev. 3 | NIST, NASA, Fowler, Thoughtworks, Humble and Farley |
| 5, 6, 15 | ISO 12207, 29148, 14764 | ISO/IEC/IEEE and ISTQB (not settled: iso.org unreadable) |
| 7 | Deploy versus release | NIST, NASA, Fowler, Thoughtworks, Humble and Farley; SAFe and ITIL wording under SAFe sources and Other public sources |
| 8, 9 | DORA capability and metric names | DORA |
| 10 | Unverified bylines and dates | each part's D and E; the entries in part A carry the values as printed |
| 11, 12 | Rath 2018; Reinertsen URL | Other public sources |
| 13 | Items marked "search only" | every entry in part A carries `# read directly` or `# not read directly (reason)` |
| 14 | NIST SSDF | NIST, NASA, Fowler, Thoughtworks, Humble and Farley |
| 16 | ISTQB currency and glossary URLs | ISO/IEC/IEEE and ISTQB |
| 17 | Cooper stage-gate and Wake INVEST | Scrum, agile and requirements practice (Cooper unreadable; Wake confirmed) |
| Section 3 Q1, Q2, Q4 | SAFe version, cadence, redirects | SAFe closed allow-list |
| Section 3 Q3 | AI-Native SAFe | SAFe sources |

---

## A. Reference entries (YAML)

Entries are in the format of `content/references.yml`. Each carries `# read directly` or `# not read directly (reason)`.

### A.SAFe sources (worklist 2.1) and AI-Native SAFe

```yaml
safe-framework:   # read directly
  title: "Planning Interval (PI)"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "last updated 2025-02-25 (as printed)"
  url: "https://framework.scaledagile.com/planning-interval"
  accessed: "2026-11-20"
  note: "Defines a PI as a cadence-based timebox in which ARTs deliver continuous value in alignment with PI Objectives; says a PI begins with PI Planning, then four development iterations, then one IP iteration; 8 to 12 weeks is called a suggestion and a good starting point, not a strict rule. Tab title 'Planning Interval (PI) - Scaled Agile Framework'. No version label on the page. Page text after the login wall not readable."

safe-configurations:   # read directly
  title: "SAFe 6.0 Configurations"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "last updated 2025-09-03 (as printed)"
  url: "https://framework.scaledagile.com/safe-6-0-configurations"
  accessed: "2026-11-20"
  note: "Link page. Lists Full SAFe, Essential SAFe, Large Solution SAFe, Portfolio SAFe and calls them the 'Scaled Agile Framework 6.0 configurations' and 'the latest version of SAFe'. Contains no description of Large Solution SAFe; that is on /large-solution (H1 'Large Solution SAFe', last update 2022-12-05)."

safe-portfolio:   # read directly
  title: "Portfolio"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "last updated 2025-04-08 (as printed)"
  url: "https://framework.scaledagile.com/portfolio"
  accessed: "2026-11-20"
  note: "Definition: 'A SAFe Portfolio is a set of value streams that delivers a continuous flow of valuable solutions to customers within a common funding and governance model.'"

safe-art:   # read directly
  title: "Agile Release Train"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "not printed in readable text"
  url: "https://framework.scaledagile.com/agile-release-train"
  accessed: "2026-11-20"
  note: "Definition: 'a long-lived team of Agile teams that incrementally develops, delivers, and often operates one or more solutions in a development value stream.' Summary names the key roles Product Management, System Architect, Release Train Engineer (RTE), Business Owners. Role definitions are on other pages (/product-management/, /business-owners/), not on this one. Article is login-walled."

safe-agile-teams:   # read directly
  title: "Agile Teams"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "not printed in readable text"
  url: "https://framework.scaledagile.com/agile-teams"
  accessed: "2026-11-20"
  note: "Definition: 'a cross-functional group of typically ten or fewer individuals with all the skills necessary to define, build, test, and deliver value to their customer.' Names two roles, Product Owner and Scrum Master/Team Coach, without defining them in the readable text. Team backlog and role detail are on /team-backlog/, /product-owner/, /scrum-master-team-coach/."

safe-lpm:   # read directly
  title: "Lean Portfolio Management"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "not printed in readable text"
  url: "https://framework.scaledagile.com/lean-portfolio-management"
  accessed: "2026-11-20"
  note: "Legacy competency article. Opens with a notice that SAFe has 'evolved the way in which we think about competencies' and points to the LPM discipline article. Definition: 'LPM aligns strategy and execution by applying Lean and systems thinking approaches to strategy and investment funding, Agile portfolio operations, and governance.' Still calls LPM 'one of the seven core competencies'."

safe-lpm-discipline:   # read directly
  title: "Lean Portfolio Management"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "last updated 2025-03-31 (as printed)"
  url: "https://framework.scaledagile.com/lean-portfolio-management-discipline"
  accessed: "2026-11-20"
  note: "H1 'Lean Portfolio Management'; tab title 'Lean Portfolio Management Discipline - Scaled Agile Framework'; breadcrumb 'Home » Lean Portfolio Management Discipline'. Full text readable (not login-walled). States the portfolio budget 'is directly allocated to these value streams rather than the traditional approach of project-based funding'."

safe-guardrails:   # read directly
  title: "Lean Budget Guardrails"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "not printed in readable text"
  url: "https://framework.scaledagile.com/guardrails/"
  accessed: "2026-11-20"
  note: "Tab title 'Extended Guidance - Lean Budget Guardrails'. Definition: 'Lean Budget Guardrails describe the policies and practices for budgeting, spending, and governance for a specific portfolio.' Names four guardrails: guiding investments by horizon; capacity allocation; approving significant initiatives; continuous Business Owner engagement."

safe-strategic-themes:   # read directly
  title: "Strategic Themes"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "not printed in readable text"
  url: "https://framework.scaledagile.com/strategic-themes/"
  accessed: "2026-11-20"
  note: "Definition: 'portfolio-level business objectives that provide competitive differentiation and strategic advantage'; 'Strategic themes connect the enterprise strategy to a portfolio'; best stated in OKR format. Readable text does not say they are decision criteria for the portfolio backlog."

safe-portfolio-backlog:   # read directly
  title: "Portfolio Backlog"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "last updated 2025-03-11 (as printed)"
  url: "https://framework.scaledagile.com/portfolio-backlog/"
  accessed: "2026-11-20"
  note: "Definition: 'a Kanban system that is used to capture and manage the business and enabler epics'. 'Portfolio Leadership is responsible for developing, maintaining, and prioritizing the Portfolio backlog'; the Value Management Office also maintains it. The state names of the portfolio Kanban are under a heading but the text is login-walled."

safe-epic-owner:   # read directly
  title: "Epic Owners"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "not printed in readable text"
  url: "https://framework.scaledagile.com/epic-owner"
  accessed: "2026-11-20"
  note: "Tab title 'Extended Guidance - Epic Owners'. Definition: 'The Epic Owner is responsible for coordinating epics through the portfolio Kanban system.'"

safe-wsjf:   # read directly
  title: "Weighted Shortest Job First"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "not printed in readable text"
  url: "https://framework.scaledagile.com/wsjf"
  accessed: "2026-11-20"
  note: "Tab title 'Extended Guidance - WSJF'. 'In SAFe, WSJF is estimated as the relative cost of delay divided by the relative job duration.' Inputs named: relative user and business value, time criticality, risk reduction and/or opportunity enablement, and job size. Opens with the quotation 'If you only quantify one thing, quantify the Cost of Delay.' attributed 'Don Reinertsen, The Principles of Product Development Flow'. The numbered reference [1] text is not in the readable portion."

safe-cost-of-delay:   # read directly
  title: "Cost of Delay"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "not printed"
  url: "https://framework.scaledagile.com/blog/glossary_term/cost-of-delay"
  accessed: "2026-11-20"
  note: "Glossary-term post. 'Cost of Delay (CoD) is the numerator in WSJF prioritization which represents the money or value that will be lost by delaying or not doing a job for a time period relative to other jobs.'"

safe-features:   # read directly
  title: "Features and Capabilities"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "last updated 2025-02-24 (as printed)"
  url: "https://framework.scaledagile.com/features-and-capabilities"
  accessed: "2026-11-20"
  note: "Feature: 'solution functionality that delivers business value, fulfills a stakeholder need, and is sized to be delivered by an Agile Release Train within a PI.' Capability: 'large solution functionality whose implementation often spans multiple ARTs and is sized to be delivered within a PI.'"

safe-story:   # read directly
  title: "Story"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "last updated 2025-01-27 (as printed)"
  url: "https://framework.scaledagile.com/story"
  accessed: "2026-11-20"
  note: "'Each story focuses on a specific behavior that can be developed in incremental steps'; 'Keeping stories small ensures they can be completed in a single iteration'. Also states 'SAFe describes four tiers of work items ... Epic, Capability, Feature, and Story.'"

safe-requirements-model:   # read directly (login-walled after first paragraph)
  title: "SAFe Requirements Model"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "not printed in readable text"
  url: "https://framework.scaledagile.com/safe-requirements-model"
  accessed: "2026-11-20"
  note: "Tab title 'Extended Guidance - SAFe Requirements Model'. Only the opening paragraph is readable: the model expresses system behaviours as Epics, Capabilities, Features, Stories, Nonfunctional Requirements (NFRs) 'and more'. Page not retired (HTTP 200). Rest of the article not readable."

safe-enablers:   # read directly
  title: "Enablers"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "last updated 2025-02-24 (as printed)"
  url: "https://framework.scaledagile.com/enablers"
  accessed: "2026-11-20"
  note: "'Enablers are backlog items that extend the architectural runway of the solution under development or improve the performance of the development value stream.' Four categories: Exploration, Architecture, Infrastructure, Compliance. 'managed in the appropriate backlog as epics, capabilities, features, or stories.'"

safe-pi-planning:   # read directly
  title: "PI Planning"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "last updated 2026-03-15 (as printed)"
  url: "https://framework.scaledagile.com/pi-planning/"
  accessed: "2026-11-20"
  note: "Definition: 'a cadence-based event for the entire ART that aligns teams and stakeholders to a shared mission and vision.' Summary: 'typically a 2-day event ... every 8-12 weeks', led by the RTE, 'takes place in the Innovation and Planning Iteration'. Outputs: 'committed PI objectives from the Agile Teams and an ART planning board that reflects feature delivery dates and dependencies'. Uses 'ART planning board'; the term 'program board' does not occur on the page. No mention of AI-Native SAFe in the readable text."

safe-inspect-and-adapt:   # read directly
  title: "Inspect and Adapt"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "last updated 2026-03-20 (as printed)"
  url: "https://framework.scaledagile.com/inspect-and-adapt"
  accessed: "2026-11-20"
  note: "Held 'at the end of each PI'; three parts: the PI System Demo, a quantitative and qualitative measurement review, and a retrospective and problem-solving workshop; improvement backlog items 'go into the ART Backlog for consideration in the next PI Planning event'. Keep key safe-inspect-and-adapt. No note on the page about AI-Native SAFe replacing it (it is stated on the AI-Native pages)."

safe-ia-facilitators-guide:   # read directly
  title: "SAFe Inspect and Adapt Facilitator's Guide"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "not printed (upload path /2026/03/; PDF metadata title 'SAFe Inspect and Adapt Facilitator's Guide.docx')"
  url: "https://framework.scaledagile.com/wp-content/uploads/2026/03/SAFe-Inspect-and-Adapt-Facilitators-Guide.pdf"
  accessed: "2026-11-20"
  note: "4-page PDF; first page heading 'SAFe Inspect and Adapt Facilitator's Guide' with section heading 'Purpose, Intent, and Outcomes'. Event has three parts (PI System Demo ~1.0 hr, Quantitative and Qualitative Measurement ~0.5 hr, Retrospective and Problem-Solving Workshop ~2.0 hr), 'typically facilitated by the Release Train Engineer (RTE)'. Names Root Cause Analysis, Fishbone, 5 Whys, Pareto but does not list a six-step workshop."

safe-iteration-planning:   # read directly
  title: "Iteration Planning"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "last updated 2026-03-18 (as printed)"
  url: "https://framework.scaledagile.com/iteration-planning/"
  accessed: "2026-11-20"
  note: "Tab title 'Extended Guidance - Iteration Planning'. 'The team collaboratively defines a set of Iteration Goals and selects the stories from the team backlog that they believe they can complete'; 'timeboxed to approximately 90 minutes for a two-week iteration'. Glossary entry for iteration is on /iterations/ (fixed-duration timebox)."

safe-iteration-review:   # read directly
  title: "Iteration Review"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "not printed"
  url: "https://framework.scaledagile.com/blog/glossary_term/iteration-review/"
  accessed: "2026-11-20"
  note: "Glossary-term post: 'The Iteration Review is a regular SAFe Scrum event where the team inspects the iteration increment, assesses progress, and adjusts the team backlog.' The framework article https://framework.scaledagile.com/iteration-review/ (last update 2026-03-18) is better to cite: 'allows the Agile Team to showcase their accomplishments, receive feedback, and collaboratively determine next steps'."

safe-iteration-retrospective:   # read directly
  title: "Iteration Retrospective"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "last updated 2026-03-18 (as printed)"
  url: "https://framework.scaledagile.com/iteration-retrospective/"
  accessed: "2026-11-20"
  note: "Tab title 'Extended Guidance - Iteration Retrospective'. 'a regular event held at the end of each iteration during which Agile Teams review their results to identify improvements for future work'; Key Takeaways say '60-minute or less'."

safe-team-backlog-refinement:   # read directly
  title: "Team Backlog Refinement"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "last updated 2026-03-18 (as printed)"
  url: "https://framework.scaledagile.com/team-backlog-refinement/"
  accessed: "2026-11-20"
  note: "Tab title 'Extended Guidance - Team Backlog Refinement'. Described as 'an event that helps Agile Teams clarify and prepare upcoming stories and features'; regular activities 'removing outdated stories, discovering new ones, and defining acceptance criteria'."

safe-rte:   # read directly
  title: "Release Train Engineer"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "not printed in readable text"
  url: "https://framework.scaledagile.com/release-train-engineer"
  accessed: "2026-11-20"
  note: "'The Release Train Engineer (RTE) is a servant leader and ART coach who facilitates ART events and processes, and supports teams in delivering value.'"

safe-system-architect:   # read directly
  title: "System Architect"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "not printed in readable text"
  url: "https://framework.scaledagile.com/system-architect/"
  accessed: "2026-11-20"
  note: "'responsible for defining and communicating a shared technical and architectural vision for the solutions developed by an ART'; Summary: 'defining enablers, participating in solution definition, outlining non-functional requirements'."

safe-built-in-quality:   # read directly (login-walled after first section)
  title: "Built-In Quality"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "not printed in readable text"
  url: "https://framework.scaledagile.com/built-in-quality"
  accessed: "2026-11-20"
  note: "Tab title 'Extended Guidance - Built-In Quality'. 'a set of practices to help ensure that the outputs of Agile teams in business and technology domains meet appropriate quality standards throughout the process of creating customer value.' Says 'five key domains' but the domain names and any Definition of Done text are behind the login wall. Definition of Done is defined in the glossary (https://framework.scaledagile.com/glossary/)."

safe-cdp:   # read directly
  title: "Continuous Delivery Pipeline"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "last updated 2025-02-06 (as printed)"
  url: "https://framework.scaledagile.com/continuous-delivery-pipeline/"
  accessed: "2026-11-20"
  note: "'represents the workflows, activities, and automation needed to guide new functionality from ideation to an on-demand release of value.' Four aspects: continuous exploration, continuous integration, continuous deployment, release on demand."

safe-continuous-exploration:   # read directly
  title: "Continuous Exploration"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "not printed in readable text"
  url: "https://framework.scaledagile.com/continuous-exploration/"
  accessed: "2026-11-20"
  note: "Tab title 'Extended Guidance - Continuous Exploration'. 'an aspect of the Continuous Delivery Pipeline that drives innovation and fosters alignment on what should be built by continually exploring the market and customer needs, defining a vision, roadmap, and set of features for a solution.'"

safe-continuous-integration:   # read directly
  title: "Continuous Integration"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "not printed in readable text"
  url: "https://framework.scaledagile.com/continuous-integration/"
  accessed: "2026-11-20"
  note: "Resolved scheme: https works (200, no redirect); http also returned 200 without redirecting. 'an aspect of the Continuous Delivery Pipeline in which new functionality is developed, tested, integrated, and validated in preparation for deployment and release.' Four activities named: Develop, Build, Test end-to-end, Stage."

safe-continuous-deployment:   # read directly
  title: "Continuous Deployment"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "not printed in readable text"
  url: "https://framework.scaledagile.com/continuous-deployment"
  accessed: "2026-11-20"
  note: "Tab title 'Extended Guidance - Continuous Deployment'. 'automates the migration of new functionality from a staging environment to production, where it is made available for release'; 'it's optimal to separate the deployment process from releasing'; four activities Deploy, Verify, Monitor, Respond."

safe-release-on-demand:   # read directly
  title: "Release on Demand"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "last updated 2025-02-25 (as printed)"
  url: "https://framework.scaledagile.com/release-on-demand"
  accessed: "2026-11-20"
  note: "'an aspect of the Continuous Delivery Pipeline that releases new functionality immediately or incrementally based on business and customer needs.' 'Critically, releases are decoupled from the work to deploy the functionality.' The four activity names are under a heading but login-walled."

safe-glossary:   # read directly
  title: "SAFe Glossary"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "not printed"
  url: "https://framework.scaledagile.com/glossary/"
  accessed: "2026-11-20"
  note: "Entries read: System Demo, Iteration Goals, Lean Budgets, Lean Budget Guardrails, Definition of Done, ART Planning Board, ART Sync, Innovation and Planning Iteration, Solution Demo, PI Objectives, Planning Interval (PI), Inspect and Adapt. No entry for 'Definition of Ready' or 'Program Board'. System Demo page: https://framework.scaledagile.com/system-demo/ (H1 'System Demo', last update 2026-03-18)."

safe-portfolio-flow:   # read directly (login-walled after first section)
  title: "Portfolio Flow"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "not printed in readable text"
  url: "https://framework.scaledagile.com/portfolio-flow/"
  accessed: "2026-11-20"
  note: "H1 'Portfolio Flow | Details'. Definition: 'a state where Lean Portfolio Management provides a continuous flow of new epics to Solution Trains and ARTs to achieve the portfolio's vision and strategic themes.' Article text after the heading '#1 Visualize and Limit WIP' is login-walled."

safe-essential:   # read directly
  title: "Essential SAFe"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "last updated 2022-11-30 (as printed)"
  url: "https://framework.scaledagile.com/essential-safe/"
  accessed: "2026-11-20"
  note: "Legacy-format knowledge-base article (older than the 2025-26 rewrites). Lists ART roles (Product Management, System Architect, RTE, Business Owners), team roles (Agile Teams, Product Owner, Scrum Master/Team Coach) and events (PI Planning, System Demo, Inspect & Adapt, ART Sync; Iteration Planning, Review, Retrospective). Linked from /safe-6-0-configurations."

safe-whats-new:   # read directly
  title: "What's new in SAFe?"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "page prints 'Last Update: 9 April 2026' but contains monthly entries through August 2026"
  url: "https://framework.scaledagile.com/whats-new-in-safe"
  accessed: "2026-11-20"
  note: "Month-by-month changelog written by 'The Framework Team'. June 2026: 'we officially introduced AI-Native SAFe, a reinvented operating model'. July 2026 refers to 'the following Core SAFe article' and 'across Core and AI-Native SAFe'. Does not print a release date of 23 June, does not print 'fully supported', and prints no SAFe version number or Core SAFe release date. Tab title 'What's new in SAFe? - Scaled Agile Framework'; H1 'What's new in SAFe?'."

safe-ai-native-sense-and-respond:   # read directly
  title: "Sense and Respond"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "last updated 2026-07-28 (as printed)"
  url: "https://framework.scaledagile.com/ain-safe-sense-and-respond"
  accessed: "2026-11-20"
  note: "URL confirmed (page also exists with trailing slash). 'a two-hour cadenced event designed for AI-Native Agile Release Trains'; 'occur at the boundary of every iteration'; 'The half-day Inspect and Adapt event ... has been replaced by a two-hour Sense and Respond event every iteration ... also includes the activities formally [sic] present in the System Demo.' Partly login-walled."

oasis-soa-rm:   # read directly
  title: "Reference Model for Service Oriented Architecture 1.0"
  author: "C. Matthew MacKenzie, Ken Laskey, Francis McCabe, Peter F Brown, Rebekah Metz (editors)"
  org: "OASIS"
  date: "OASIS Standard, 12 October 2006 (as printed)"
  url: "https://docs.oasis-open.org/soa-rm/v1.0/soa-rm.html"
  accessed: "2026-11-20"
  note: "Tab title 'Reference Model for Service Oriented Architecture v1.0'; document identifier soa-rm. Section 1.1: 'A reference model is an abstract framework for understanding significant relationships among the entities of some environment.' Abstract: 'an abstract framework for understanding significant entities and relationships between them within a service-oriented environment'."
```

Suggested NEW optional keys for AI-Native SAFe (all read directly, accessed 2026-11-20):

```yaml
safe-ai-native-launch-post:   # read directly
  title: "New Release: AI-Native SAFe is the Operating Model for the AI-Native Organization"
  author: "Andrew Sales"
  org: "Scaled Agile, Inc."
  date: "June 23, 2026 (as printed)"
  url: "https://framework.scaledagile.com/blog/ai-native-safe-is-the-operating-model-for-the-ai-native-organization"
  accessed: "2026-11-20"
  note: "Says 'June 16th marked such an evolution' (the unveiling), 'This release does not replace Core SAFe', and commits 'to continue supporting and evolving the Core SAFe operating model'. Describes an early-access, biweekly-guidance release ending at the SAFe Summit San Diego on September 14-18."

safe-ai-native-session4-post:   # read directly
  title: "AI-Native SAFe Session 4: Reimagining PI Planning and SAFe Events for the Age of AI"
  author: "Andrew Sales"
  org: "Scaled Agile, Inc."
  date: "August 5, 2026 (as printed)"
  url: "https://framework.scaledagile.com/blog/ai-native-safe-session-4-reimagining-pi-planning-and-safe-events-for-the-age-of-ai"
  accessed: "2026-11-20"
  note: "States PI Outcome Planning is 'a 1-day event for everyone on the AI-Native ART, replacing the 2-day PI Planning event' and that Sense and Respond 'replaces the SAFe Inspect and Adapt event and incorporates System Demo activities'. Customer Demos are 'held regularly' in AI-Native SAFe; the post does not say they replace the System Demo."

safe-ai-native-summit-recap:   # read directly
  title: "SAFe Summit Keynote Recap: Launching The Operating Model for the Age of AI"
  author: "Andrew Sales"
  org: "Scaled Agile, Inc."
  date: "October 6, 2026 (as printed)"
  url: "https://framework.scaledagile.com/blog/safe-summit-keynote-recap-launching-the-operating-model-for-the-age-of-ai"
  accessed: "2026-11-20"
  note: "Keynote on 15 September 2026: 'Today marks the official release of AI-Native SAFe'. States 'two co-existing versions of the Framework, Core SAFe and AI-Native SAFe'; new work items Experiments and Prototypes 'alongside Features and Enablers'; 'Standardized Agile roles are replaced by flexible capabilities, Product, Builder, and Domain Expert'."

safe-ai-native-pi-outcome-planning:   # read directly
  title: "PI Outcome Planning"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "last updated 2026-07-28 (as printed)"
  url: "https://framework.scaledagile.com/ain-safe-pi-outcome-planning/"
  accessed: "2026-11-20"
  note: "'a one-day, AI-Native SAFe event'; 'occurs at the start of every Planning Interval (PI)'; 'The two-day PI Planning event ... has been replaced by a one-day PI Outcome Planning event'. Partly login-walled."

safe-framework-home:   # read directly
  title: "Framework - Scaled Agile Framework (home page, 'Welcome to the Scaled Agile Framework')"
  author: "not printed"
  org: "Scaled Agile, Inc."
  date: "not printed (JSON-LD metadata dateModified 2026-09-25, not visible text)"
  url: "https://framework.scaledagile.com/"
  accessed: "2026-11-20"
  note: "'Core SAFe continues to provide the world's most adopted Operating Model for scaling Lean and Agile practices across your organization. AI-Native SAFe, builds on this foundation to provide an AI-Native Operating Model that helps organizations achieve a return on AI.'"
```

### A.DORA (2.2)

```yaml
dora-ai-capabilities:   # read directly
  title: "DORA AI Capabilities Model (tab title: Download the DORA AI Capabilities Model report)"
  author: "not printed"
  org: "DORA (a program run by Google Cloud)"
  date: "last updated 2025-11-25 (as printed)"
  url: "https://dora.dev/ai/capabilities-model/report/"
  accessed: "2026-11-20"
  note: "Landing page for the report, a companion guide to the 2025 State of AI-assisted Software Development report, 'the seven capabilities that amplify the benefits of AI'. The page does NOT name the seven capabilities. Names and order are on the Google Cloud blog posts (dora-ai-capabilities-intro) and the capability catalog."

dora-ai-capabilities-intro:   # read directly
  title: "Introducing the DORA AI Capabilities Model: 7 keys to succeeding in AI-assisted software development (tab title: Introducing DORA's inaugural AI Capabilities Model | Google Cloud Blog)"
  author: "Kevin M. Storer (Ph.D., Researcher); Derek DeBellis (Researcher)"
  org: "Google Cloud Blog"
  date: "September 23, 2025 (as printed)"
  url: "https://cloud.google.com/blog/products/ai-machine-learning/introducing-doras-inaugural-ai-capabilities-model"
  accessed: "2026-11-20"
  note: "Names the seven capabilities in this order: Clear and communicated AI stance; Healthy data ecosystems; AI-accessible internal data; Strong version control practices; Working in small batches; User-centric focus; Quality internal platforms. URL has no redirect."

dora-ai-capabilities-impact:   # read directly
  title: "From adoption to impact: Putting the DORA AI Capabilities Model to work (tab title adds ' | Google Cloud Blog')"
  author: "Nathen Harvey (DORA Lead); Allison Park (Senior Product Marketing Manager)"
  org: "Google Cloud Blog"
  date: "December 10, 2025 (as printed)"
  url: "https://cloud.google.com/blog/products/ai-machine-learning/from-adoption-to-impact-putting-the-dora-ai-capabilities-model-to-work"
  accessed: "2026-11-20"
  note: "Final URL has no trailing slash (the slash form redirects). Lists the same seven capabilities in the same order as the September post."

dora-small-batches:   # read directly
  title: "Working in small batches (tab title: DORA | Capabilities: Working in small batches)"
  author: "not printed"
  org: "DORA (a program run by Google Cloud)"
  date: "last updated 2025-12-08 (as printed)"
  url: "https://dora.dev/capabilities/working-in-small-batches/"
  accessed: "2026-11-20"
  note: "Page carries the tags 'core' and 'AI'."

dora-wip-limits:   # read directly
  title: "Work in process limits (tab title: DORA | Capabilities: Work in process limits)"
  author: "not printed"
  org: "DORA (a program run by Google Cloud)"
  date: "not printed"
  url: "https://dora.dev/capabilities/wip-limits/"
  accessed: "2026-11-20"
  note: "No 'last updated' line on the page. No 'core' tag shown on this page or in the catalog."

dora-2024-highlights:   # read directly
  title: "Highlights from the 10th DORA report (tab title: Announcing the 2024 DORA report | Google Cloud Blog)"
  author: "Nathen Harvey (DORA Lead); Derek DeBellis (Researcher)"
  org: "Google Cloud Blog"
  date: "October 22, 2024 (as printed)"
  url: "https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report"
  accessed: "2026-11-20"
  note: "Body text opens 'we're pleased to announce the publication of the 2024 Accelerate State of DevOps Report'."

dora-2024-report:   # read directly
  title: "DORA Research: 2024 (tab title: DORA | Accelerate State of DevOps Report 2024)"
  author: "not printed"
  org: "DORA (a program run by Google Cloud)"
  date: "last updated 2026-04-13 (as printed)"
  url: "https://dora.dev/research/2024/dora-report/"
  accessed: "2026-11-20"
  note: "Landing page with download links and key findings, not the report text."

dora-2025-report:   # read directly
  title: "DORA Research: 2025 (tab title: DORA | State of AI-assisted Software Development 2025)"
  author: "not printed"
  org: "DORA (a program run by Google Cloud)"
  date: "not printed"
  url: "https://dora.dev/research/2025/dora-report/"
  accessed: "2026-11-20"
  note: "The drafted URL https://dora.dev/dora-report-2025/ redirects here. Landing page only; it does not state throughput or instability findings."

dora-2025-announcement:   # read directly
  title: "Announcing the 2025 DORA Report: State of AI-Assisted Software Development (tab title adds ' | Google Cloud Blog'; tab reads 'Announcing the 2025 DORA Report')"
  author: "Nathen Harvey (DORA Lead); Derek DeBellis (Researcher)"
  org: "Google Cloud Blog"
  date: "September 23, 2025 (as printed)"
  url: "https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report"
  accessed: "2026-11-20"
  note: "Plain GET returned full article text."

dora-metrics:   # read directly (URL changed, see Part E)
  title: "DORA's software delivery performance metrics"
  author: "Nathen Harvey"
  org: "DORA (a program run by Google Cloud)"
  date: "last updated 2026-01-05 (as printed)"
  url: "https://dora.dev/guides/dora-metrics/"
  accessed: "2026-11-20"
  note: "Five metrics in two groups: throughput (change lead time, deployment frequency, failed deployment recovery time) and instability (change fail rate, deployment rework rate). dora.dev/guides/dora-metrics-four-keys/ redirects here. https://dora.dev/research/ (the drafted URL) does not list the metric names in its page text."

dora-metrics-history:   # read directly (new, optional)
  title: "A history of DORA's software delivery metrics"
  author: "Nathen Harvey"
  org: "DORA (a program run by Google Cloud)"
  date: "January 2, 2026 (as printed); last updated 2026-01-02"
  url: "https://dora.dev/insights/dora-metrics-history/"
  accessed: "2026-11-20"
  note: "Explains renaming of MTTR / time to restore service to failed deployment recovery time (2023) and the move from four keys to five metrics (2024). Linked from the metrics guide."

dora-capabilities-catalog:   # read directly (new, optional)
  title: "Capability catalog (tab title: DORA | Capabilities: Catalog)"
  author: "not printed"
  org: "DORA (a program run by Google Cloud)"
  date: "not printed"
  url: "https://dora.dev/capabilities/"
  accessed: "2026-11-20"
  note: "Lists the capabilities with the tags 'AI' and 'core'."

dora-customer-feedback:   # read directly
  title: "Customer feedback (tab title: DORA | Capabilities: Customer feedback)"
  author: "not printed"
  org: "DORA (a program run by Google Cloud)"
  date: "not printed"
  url: "https://dora.dev/capabilities/customer-feedback/"
  accessed: "2026-11-20"
  note: "No 'last updated' line. No 'core' tag shown on the page."

dora-test-automation:   # read directly
  title: "Test automation (tab title: DORA | Capabilities: Test automation)"
  author: "not printed"
  org: "DORA (a program run by Google Cloud)"
  date: "last updated 2025-07-17 (as printed)"
  url: "https://dora.dev/capabilities/test-automation/"
  accessed: "2026-11-20"
  note: "Page carries the tag 'core'."

dora-monitoring-observability:   # read directly
  title: "Monitoring and observability (tab title: DORA | Capabilities: Monitoring and observability)"
  author: "not printed"
  org: "DORA (a program run by Google Cloud)"
  date: "not printed"
  url: "https://dora.dev/capabilities/monitoring-and-observability/"
  accessed: "2026-11-20"
  note: "Page carries the tag 'core'. No 'last updated' line."

dora-streamlining-change-approval:   # read directly
  title: "Streamlining change approval (tab title: DORA | Capabilities: Streamlining change approval)"
  author: "not printed"
  org: "DORA (a program run by Google Cloud)"
  date: "last updated 2025-10-30 (as printed)"
  url: "https://dora.dev/capabilities/streamlining-change-approval/"
  accessed: "2026-11-20"
  note: "Page carries the tag 'core'. Cites the 2019 State of DevOps Report."

dora-continuous-delivery:   # read directly
  title: "Continuous delivery (tab title: DORA | Capabilities: Continuous delivery)"
  author: "not printed"
  org: "DORA (a program run by Google Cloud)"
  date: "not printed"
  url: "https://dora.dev/capabilities/continuous-delivery/"
  accessed: "2026-11-20"
  note: "Page carries the tag 'core'. No 'last updated' line."
```

### A.Scrum, agile and requirements practice (2.3)

```yaml
scrum-guide-2020:   # read directly
  title: "The 2020 Scrum Guide"
  author: "Ken Schwaber and Jeff Sutherland"
  org: "ScrumGuides.org"
  date: "November 2020 (as printed: 'direct port of the November 2020 version'; (c) 2020 Ken Schwaber and Jeff Sutherland)"
  url: "https://scrumguides.org/scrum-guide.html"
  accessed: "2026-11-20"
  note: "Tab title 'Scrum Guide | Scrum Guides'; on-page H1 'The 2020 Scrum Guide | TM'. HTML port of the November 2020 PDF. The site's download page labels the English November 2020 edition 'Official Current Version'. Defines the Definition of Done as a commitment of the Increment. Does not use the term 'Definition of Ready'; says Product Backlog items that can be Done within one Sprint are 'deemed ready for selection in a Sprint Planning event'. Names transparency, inspection and adaptation as the empirical pillars. Licence CC BY-SA 4.0."

scrum-guide-revisions:   # read directly (optional supporting entry, new)
  title: "Scrum Guide Revisions"
  author: "not printed (site of Ken Schwaber and Jeff Sutherland)"
  org: "ScrumGuides.org"
  date: "not printed; page footer '(c) 2025 ScrumGuides.org'; HTTP Last-Modified header 2025-01-27"
  url: "https://scrumguides.org/revisions.html"
  accessed: "2026-11-20"
  note: "Tab title 'Scrum Guide Revisions | Scrum Guides'. Lists changes 2010-2011, 2011-2013, 2013-2016, 2016-2017, 2017-2020. The 2011-2013 section says refined Product Backlog items 'are called Ready' and 'Ready and Done are two states that reinforce transparency'. The 2013-2016 section mentions 'the Scrum pillars of transparency, inspection, and adaptation'."

scrum-guide-expansion-pack:   # read directly (optional, new; URL not linked from scrumguides.org, see Part D Q3)
  title: "Scrum Guide Expansion Pack"
  author: "Jeff Sutherland, John Coleman, Ralph Jocham (as printed: 'Created by')"
  org: ""
  date: "not printed; HTTP Last-Modified header 2026-02-18; footer 'v2.0.9 ... (c) 2026 Martin Hinshelwood' refers to the website design/theme"
  url: "https://scrumexpansion.org/"
  accessed: "2026-11-20"
  note: "On-page H1 'Scrum Guide | Expansion Pack'; strapline 'Companion to the 2020 Scrum Guide'. 11 expansion documents. Not the Scrum Guide itself. No 'v2026.1' label printed on the page."

agile-alliance-dor:   # read directly
  title: "Definition of Ready"
  author: "not printed"
  org: "Agile Alliance"
  date: "not printed"
  url: "https://agilealliance.org/glossary/definition-of-ready/"
  accessed: "2026-11-20"
  note: "Tab title 'What is Definition of Ready? | Agile Alliance'; H1 'Definition of Ready' (Agile Glossary). Describes DoR as explicit criteria (generally based on the INVEST matrix) a user story must meet before being accepted into the upcoming iteration. Section 'Origins of Definition of Ready' names the ETVX framework (1985, 'A programming process architecture') and says allusions to a 'definition of ready' date to early 2008, with the first formal description seemingly from October 2008. The page does not mention the Scrum Guide."

agile-alliance-dod:   # read directly
  title: "Definition of Done"
  author: "not printed"
  org: "Agile Alliance"
  date: "not printed"
  url: "https://agilealliance.org/glossary/definition-of-done/"
  accessed: "2026-11-20"
  note: "Tab title 'Definition of Done | Agile Alliance'; H1 'Definition of Done' (Agile Glossary). Describes a list of criteria the team agrees on that must be met before a product increment is considered done. Has an 'Origins' list with entries for 2002, 2003, 2005 and 2007."

overeem-dor:   # not read directly (HTTP 403 from www.scrum.org)
  title: "Why isn't a Definition of Ready described in the Scrum Guide?"   # UNCONFIRMED, worklist URL slug only
  author: "Barry Overeem"   # UNCONFIRMED
  org: "Scrum.org"
  date: "2016-09-05"   # UNCONFIRMED
  url: "https://www.scrum.org/resources/blog/why-isnt-definition-ready-described-scrum-guide"
  accessed: "2026-11-20"
  note: "Not read: host refused the request (403). Title, byline and date unconfirmed; do not cite until read."

kronfalt-ready-2008:   # not read directly (host scrumftw.blogspot.com did not resolve)
  title: "Ready-ready: the Definition of Ready for User Stories going into sprint planning"   # UNCONFIRMED
  author: "Richard Kronfalt"   # UNCONFIRMED (spelling with or without diaeresis unverified)
  org: ""
  date: "October 2008"   # UNCONFIRMED
  url: "http://scrumftw.blogspot.com/2008/10/ready-ready-definition-of-ready-for.html"
  accessed: "2026-11-20"
  note: "Not read: name resolution failed. Title, byline, date and criteria list unconfirmed; do not cite until read."

sutherland-ready-2009:   # not read directly (host jeffsutherland.com did not resolve)
  title: "unconfirmed"
  author: "Jeff Sutherland"   # UNCONFIRMED
  org: ""
  date: "2009-07-04"   # UNCONFIRMED
  url: "http://jeffsutherland.com/scrum/2009/07/ready-dynamic-model-of-scrum.html"
  accessed: "2026-11-20"
  note: "Not read: name resolution failed. Post title, date and content unconfirmed; do not cite until read."

radice-etvx-1985:   # not read directly (HTTP 403 from dl.acm.org)
  title: "A programming process architecture"   # title string is printed on the Agile Alliance DoR page, which gives no authors
  author: "UNCONFIRMED (worklist: R. A. Radice, N. K. Roth, A. C. O'Hara, W. A. Ciarfella)"
  org: "IBM Systems Journal"   # UNCONFIRMED
  date: "1985 (year printed on the Agile Alliance DoR page); volume, issue and month unconfirmed"
  url: "https://dl.acm.org/doi/10.1147/sj.242.0079"
  accessed: "2026-11-20"
  note: "Not read: ACM refused the request (403). Byline, volume, pages, DOI-to-title match and the ETVX description are unconfirmed. Only the title and year are seen, second-hand, on the Agile Alliance page."

wake-invest:   # read directly
  title: "INVEST in Good Stories, and SMART Tasks"
  author: "Bill Wake"
  org: "XP123"
  date: "2003-08-17 (as printed: 'Posted on August 17, 2003 by Bill Wake'); body note says written in April and August 2003; postscript added 2011-02-16"
  url: "https://xp123.com/invest-in-good-stories-and-smart-tasks/"
  accessed: "2026-11-20"
  note: "Tab title 'INVEST in Good Stories, and SMART Tasks - XP123'. Self-published on the author's site xp123.com (category 'XPlorations'). Lists INVEST: Independent, Negotiable, Valuable, Estimable, Small, Testable; and SMART for tasks: Specific, Measurable, Achievable, Relevant, Time-boxed. Author states 'I developed the INVEST acronym, and wrote this article in April and August, 2003'."

agile-manifesto-principles:   # read directly
  title: "Principles behind the Agile Manifesto"
  author: "not printed on this page; the Manifesto home page prints '(c) 2001, the above authors' above a list of 17 names (Kent Beck ... Dave Thomas)"
  org: "agilemanifesto.org"
  date: "not printed on this page; Manifesto home page '(c) 2001'; HTTP Last-Modified header 2024-10-28"
  url: "https://agilemanifesto.org/principles.html"
  accessed: "2026-11-20"
  note: "Tab title and H1 both 'Principles behind the Agile Manifesto'. Twelve unnumbered statements; the twelfth reads 'At regular intervals, the team reflects on how to become more effective, then tunes and adjusts its behavior accordingly.' (American spelling 'behavior')."

schwaber-beedle-2001:   # not read directly (HTTP 403 from dl.acm.org)
  title: "Agile Software Development with Scrum"   # UNCONFIRMED
  author: "Ken Schwaber and Mike Beedle"   # UNCONFIRMED
  org: "Prentice Hall"   # UNCONFIRMED
  date: "2001"   # UNCONFIRMED
  url: "https://dl.acm.org/doi/10.5555/559553"
  accessed: "2026-11-20"
  note: "Not read: ACM refused the request (403). Everything unconfirmed. Need a publisher or library record from another host."

schwaber-scrum-1995:   # not read directly (host www.jeffsutherland.org did not resolve)
  title: "SCRUM Development Process"   # UNCONFIRMED
  author: "Ken Schwaber"   # UNCONFIRMED
  org: "OOPSLA'95 workshop"   # UNCONFIRMED
  date: "1995"   # UNCONFIRMED
  url: "http://www.jeffsutherland.org/oopsla/schwapub.pdf"
  accessed: "2026-11-20"
  note: "Not read: name resolution failed. Title, byline and venue unconfirmed. Separately, the 2020 Scrum Guide says Schwaber and Sutherland first co-presented Scrum at OOPSLA in 1995."

cooper-stage-gate:   # not read directly (HTTP 403 from onlinelibrary.wiley.com)
  title: "unconfirmed (worklist: DOI 10.1002/9781444316568.wiem05014)"
  author: "UNCONFIRMED"
  org: "Wiley"   # UNCONFIRMED
  date: "UNCONFIRMED"
  url: "https://onlinelibrary.wiley.com/doi/full/10.1002/9781444316568.wiem05014"
  accessed: "2026-11-20"
  note: "Not read: Wiley refused the request (403). Title, byline, venue, year and all three claims unconfirmed."

keep-a-changelog:   # read directly
  title: "Keep a Changelog"
  author: "Olivier Lacan (page: 'created and maintained by Olivier Lacan, and designed by Tyler Fortune')"
  org: "keepachangelog.com"
  date: "version 1.1.0 (its own changelog dates 1.1.0 as 2019-02-15; first changelog entry 0.0.1 dated 2014-05-31); version 2.0.0 'Published on June 7th, 2026'"
  url: "https://keepachangelog.com/en/1.1.0/"
  accessed: "2026-11-20"
  note: "Root URL https://keepachangelog.com/ is a stub page that redirects client-side (meta refresh and script) to /en/1.1.0/ by default, or to /en/2.0.0/ when a preview flag is set. Tab title and H1 both 'Keep a Changelog'. 1.1.0 and 2.0.0 both say 'Changelogs are for humans, not machines.' 1.1.0 tagline 'Don't let your friends dump git logs into changelogs.'; 2.0.0 retires that tagline. 1.1.0 says 'Mention whether you follow Semantic Versioning'; 2.0.0 says 'You do not have to use Semantic Versioning.' The phrase 'machines can draft, humans curate' appears only on /en/2.0.0/."

semver:   # read directly
  title: "Semantic Versioning 2.0.0"
  author: "Tom Preston-Werner (page: 'originally authored by Tom Preston-Werner')"
  org: "semver.org"
  date: "not printed (HTTP Last-Modified header 2026-10-16 is a server header, not page content)"
  url: "https://semver.org/spec/v2.0.0.html"
  accessed: "2026-11-20"
  note: "Tab title 'Semantic Versioning 2.0.0 | Semantic Versioning'; H1 'Semantic Versioning 2.0.0'. Summary: increment MAJOR 'when you make incompatible API changes'. Licence CC BY 3.0."
```

### A.ISO/IEC/IEEE and ISTQB (2.4, 2.5)

```yaml
iso-12207:   # not read directly (iso.org HTTP 403 for both 63712 and 90219)
  title: "not read (iso.org returned HTTP 403); ISO/IEC/IEEE 12207 Systems and software engineering — Software life cycle processes (title and edition unconfirmed)"
  author: "not read"
  org: "ISO/IEC JTC 1/SC 7 and IEEE (unconfirmed)"
  date: "not read"
  url: "https://www.iso.org/standard/63712.html"
  accessed: "2026-11-20"
  note: "Catalogue page not readable. Edition, status and the 90219 catalogue number are unconfirmed. Do not cite process names, edition or April 2026 date from this entry."

iso-14764:   # not read directly (iso.org HTTP 403)
  title: "not read (iso.org returned HTTP 403)"
  author: "not read"
  org: "ISO/IEC JTC 1/SC 7 and IEEE (unconfirmed)"
  date: "not read"
  url: "https://www.iso.org/standard/80710.html"
  accessed: "2026-11-20"
  note: "Catalogue page not readable. Number of maintenance types in the 2022 edition unconfirmed."

iso-25010:   # not read directly (iso.org HTTP 403)
  title: "not read (iso.org returned HTTP 403)"
  author: "not read"
  org: "ISO/IEC (unconfirmed)"
  date: "not read"
  url: "https://www.iso.org/standard/78176.html"
  accessed: "2026-11-20"
  note: "Catalogue page not readable. Characteristic names unconfirmed."

iso-29148:   # not read directly (iso.org HTTP 403)
  title: "not read (iso.org returned HTTP 403)"
  author: "not read"
  org: "ISO/IEC JTC 1/SC 7 and IEEE (unconfirmed)"
  date: "not read"
  url: "https://www.iso.org/standard/72089.html"
  accessed: "2026-11-20"
  note: "Catalogue page not readable. Requirement characteristics, their order and the traceability wording are unconfirmed."

iso-24765:   # not read directly (iso.org HTTP 403)
  title: "not read (iso.org returned HTTP 403)"
  author: "not read"
  org: "ISO/IEC JTC 1/SC 7 and IEEE (unconfirmed)"
  date: "not read"
  url: "https://www.iso.org/standard/71952.html"
  accessed: "2026-11-20"
  note: "Catalogue page not readable. Edition and definition wording unconfirmed. (An ISTQB glossary record read this session cites 'ISO/IEC/IEEE 24765 (2017) Systems and software engineering -- Vocabulary' as a reference for stress testing; that confirms only that the 2017 edition exists under that title, not the traceability definition.)"

iso-15288:   # not read directly (iso.org HTTP 403)
  title: "not read (iso.org returned HTTP 403)"
  author: "not read"
  org: "ISO/IEC JTC 1/SC 7 and IEEE (unconfirmed)"
  date: "not read"
  url: "https://www.iso.org/standard/81702.html"
  accessed: "2026-11-20"
  note: "Catalogue page not readable. Optional entry; drop unless read later."

iso-42010:   # not read directly (iso.org HTTP 403)
  title: "not read (iso.org returned HTTP 403)"
  author: "not read"
  org: "ISO/IEC JTC 1/SC 7 and IEEE (unconfirmed)"
  date: "not read"
  url: "https://www.iso.org/standard/74393.html"
  accessed: "2026-11-20"
  note: "Catalogue page not readable. Concept names unconfirmed."

iso-29119-1:   # not read directly (iso.org HTTP 403); existing entry kept as is
  title: "ISO/IEC/IEEE 29119-1:2022 Software and systems engineering — Software testing — Part 1: General concepts"
  author: "ISO/IEC JTC 1/SC 7 and IEEE"
  org: "International Organization for Standardization"
  date: "2022-01"
  url: "https://www.iso.org/standard/81291.html"
  accessed: "2026-11-20"
  note: "General concepts of software testing, including risk-based testing as the approach for prioritizing test effort. Not re-confirmed: iso.org returned HTTP 403 on 2026-11-20. (Separately, the ISTQB glossary record for risk-based testing cites 'ISO/IEC/IEEE 29119-1 (2013)' as its 'After' reference, so the glossary points to the 2013 edition.)"

iso-29119-3:   # not read directly (iso.org HTTP 403)
  title: "not read (iso.org returned HTTP 403)"
  author: "not read"
  org: "ISO/IEC JTC 1/SC 7 and IEEE (unconfirmed)"
  date: "not read"
  url: "https://www.iso.org/standard/79429.html"
  accessed: "2026-11-20"
  note: "Catalogue page not readable. Catalogue number, edition (2013 vs 2021) and the test completion report contents are unconfirmed."

istqb-rbt:   # read directly (glossary page is JS-rendered; text read from the glossary's own API https://api.glossary.istqb.org/v1/terms/risk-based-testing)
  title: "risk-based testing"
  author: "International Software Testing Qualifications Board (ISTQB)"
  org: "ISTQB Glossary"
  date: "term version 3 (no page date printed; glossary history shows Foundation v4.0 usage refreshed 2026-11-12)"
  url: "https://glossary.istqb.org/en_US/term/risk-based-testing"
  accessed: "2026-11-20"
  note: "Defines risk-based testing as a test approach in which the management, selection, prioritization, and use of test activities and resources are based on corresponding risk types and risk levels. Glossary record cites ISO/IEC/IEEE 29119-1 (2013) as its 'After' reference. Page tab title is 'ISTQB Glossary'."

istqb-ctfl-4:   # read directly
  title: "Certified Tester Foundation Level (CTFL) v4.0"
  author: "International Software Testing Qualifications Board (ISTQB)"
  org: "ISTQB"
  date: "syllabus v4.0.1, 2024-09-15 (errata release of v4.0, 2023-04-21)"
  url: "https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/"
  accessed: "2026-11-20"
  note: "Certification overview page (tab title 'Certified Tester Foundation Level (CTFL) v4.0 Overview'; site redirects www.istqb.org to istqb.org). Download list on the page names 'ISTQB CTFL Syllabus v4.0.1'. Syllabus PDF: https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf (title 'Certified Tester Foundation Level Syllabus v4.0.1', dated 2024-09-15). Section 2.2.1 describes five test levels: component, component integration, system, system integration, acceptance; section 2.2.3 distinguishes confirmation testing (original defect fixed) from regression testing (no adverse consequences from a change)."

istqb-stress-testing:   # read directly (glossary's own API https://api.glossary.istqb.org/v1/terms/stress-testing; page itself is JS-rendered)
  title: "stress testing"
  author: "International Software Testing Qualifications Board (ISTQB)"
  org: "ISTQB Glossary"
  date: "term version 1 (no page date printed)"
  url: "https://glossary.istqb.org/en_US/term/stress-testing"
  accessed: "2026-11-20"
  note: "Defines stress testing as a type of performance testing to evaluate a system or component at or beyond the limits of its anticipated or specified workloads, or with reduced availability of resources such as access to memory or servers. Glossary record cites ISO/IEC/IEEE 24765 (2017) Systems and software engineering -- Vocabulary."

istqb-test-completion:   # read directly (glossary's own API https://api.glossary.istqb.org/v1/terms/test-completion; page itself is JS-rendered)
  title: "test completion"
  author: "International Software Testing Qualifications Board (ISTQB)"
  org: "ISTQB Glossary"
  date: "term version 2 (no page date printed)"
  url: "https://glossary.istqb.org/en_US/term/test-completion"
  accessed: "2026-11-20"
  note: "Defines test completion as the activity that makes testware available for later use, leaves test environments in a satisfactory condition and communicates the results of testing to relevant stakeholders. Synonym listed: test closure. The exit-criteria wording is a separate term (https://glossary.istqb.org/en_US/term/exit-criteria): 'The set of conditions for officially completing a defined task.' (version 2, after Gilb and Graham 1993)."

istqb-testability:   # read directly (glossary's own API https://api.glossary.istqb.org/v1/terms/testability; page itself is JS-rendered)
  title: "testability"
  author: "International Software Testing Qualifications Board (ISTQB)"
  org: "ISTQB Glossary"
  date: "term version 3 (no page date printed)"
  url: "https://glossary.istqb.org/en_US/term/testability"
  accessed: "2026-11-20"
  note: "Defines testability as the degree to which test conditions can be established for a component or system, and tests can be performed to determine whether those test conditions have been met. See also: maintainability."

istqb-acceptance-criteria:   # read directly (glossary's own API https://api.glossary.istqb.org/v1/terms/acceptance-criteria; page itself is JS-rendered)
  title: "acceptance criteria"
  author: "International Software Testing Qualifications Board (ISTQB)"
  org: "ISTQB Glossary"
  date: "term version 3 (no page date printed)"
  url: "https://glossary.istqb.org/en_US/term/acceptance-criteria"
  accessed: "2026-11-20"
  note: "Current definition (version 3): 'The criteria that a work product must satisfy to be accepted by the stakeholders.' Reference given: IREB Glossary. Earlier versions read from the same API with ?version=: v1 'The exit criteria that a component or system must satisfy in order to be accepted by a user, customer, or other authorized entity.'; v2 'The criteria that a component or system must satisfy in order to be accepted by a user, customer, or other authorized entity.'"

istqb-agile-tester-2014:   # read directly
  title: "Certified Tester Foundation Level Extension Syllabus — Agile Tester (Version 2014)"
  author: "International Software Testing Qualifications Board (ISTQB); Foundation Level Extension Agile Tester Working Group (Rex Black, chair)"
  org: "ISTQB"
  date: "Version 2014, 30 Sep 2014 (minor typos corrected; GA version 31 May 2014)"
  url: "https://astqb.org/assets/documents/ISTQB-Foundation-Agile-Syllabus.pdf"
  accessed: "2026-11-20"
  note: "Requested URL https://www.astqb.org/documents/ISTQB-Foundation-Agile-Syllabus.pdf redirects to the URL above. The same document is ISTQB's own 'ISTQB CTFL-AT Syllabus v1.0' (https://istqb.org/wp-content/uploads/2024/11/ISTQB-CTFL-AT_Syllabus_v1.0.pdf, identical title page 'Version 2014'). The text says 'Each test level has its own definition of done.' and uses INVEST for user stories. ISTQB's CTFL-AT page (https://istqb.org/certifications/certified-tester-foundation-level-agile-tester-ctfl-at/) announces exams and training are available only until sunset dates 6 May 2027 (English) and 6 November 2027 (non-English)."
```

### A.NIST, NASA, Fowler, Thoughtworks, Humble and Farley (2.6, 2.7, 2.9)

```yaml
nist-800-61r3:   # read directly (csrc.nist.gov page, doi.org link on it resolves to the nvlpubs PDF; PDF text read)
  title: "Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile"
  author: "Alex Nelson, Sanjay Rekhi, Murugiah Souppaya, Karen Scarfone"
  org: "National Institute of Standards and Technology (NIST)"
  date: "April 2025 (final, 2025-04-03)"
  url: "https://csrc.nist.gov/pubs/sp/800/61/r3/final"
  accessed: "2026-11-20"
  note: "NIST SP 800-61 Rev. 3. DOI https://doi.org/10.6028/NIST.SP.800-61r3 (PDF: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf). The CSRC page lists the first author as 'Alexander Nelson (NIST)'; the PDF title page prints 'Alex Nelson'. Page says Supersedes SP 800-61 Rev. 2 (08/06/2012). Draft 2024-04-03, final 2025-04-03. Uses all six CSF 2.0 Functions; lessons learned from all Functions feed Improvement (ID.IM)."

nist-800-61r2:   # read directly (optional supporting entry, only if Rev. 2 is cited)
  title: "Computer Security Incident Handling Guide"
  author: "Paul Cichonski, Thomas Millar, Tim Grance, Karen Scarfone"
  org: "National Institute of Standards and Technology (NIST)"
  date: "August 2012 (final 2012-08-06); withdrawn 2025-04-03"
  url: "https://csrc.nist.gov/pubs/sp/800/61/r2/final"
  accessed: "2026-11-20"
  note: "NIST SP 800-61 Rev. 2. CSRC page states 'Withdrawn on April 03, 2025. Superseded by SP 800-61 Rev. 3'."

nist-ssdf:   # read directly (csrc page, nvlpubs PDF of v1.1, csrc IPD page and IPD PDF)
  title: "Secure Software Development Framework (SSDF) Version 1.1: Recommendations for Mitigating the Risk of Software Vulnerabilities"
  author: "Murugiah Souppaya, Karen Scarfone, Donna Dodson"
  org: "National Institute of Standards and Technology (NIST)"
  date: "February 2022 (final 2022-02-03)"
  url: "https://csrc.nist.gov/pubs/sp/800/218/final"
  accessed: "2026-11-20"
  note: "NIST SP 800-218 v1.1. DOI https://doi.org/10.6028/NIST.SP.800-218. Practice and task identifiers checked in the PDF. A newer version, SP 800-218 Rev. 1 (SSDF v1.2), exists only as an Initial Public Draft (published 2025-12-17, comments closed 2026-01-30; https://csrc.nist.gov/pubs/sp/800/218/r1/ipd); no final Rev. 1 page was found on 2026-11-20 (https://csrc.nist.gov/pubs/sp/800/218/r1/final returns HTTP 404). The v1.1 page is still the current final."

nist-ir-8397:   # read directly (csrc page; doi.org resolves to nvlpubs PDF; PDF text read)
  title: "Guidelines on Minimum Standards for Developer Verification of Software"
  author: "Paul E. Black, Barbara Guttman, Vadim Okun"
  org: "National Institute of Standards and Technology (NIST)"
  date: "October 2021 (final 2021-10-06)"
  url: "https://csrc.nist.gov/pubs/ir/8397/final"
  accessed: "2026-11-20"
  note: "NISTIR 8397. DOI https://doi.org/10.6028/NIST.IR.8397 (resolves to https://nvlpubs.nist.gov/nistpubs/ir/2021/NIST.IR.8397.pdf). CSRC page prints 'Paul Black'; the PDF prints 'Paul E. Black'. Response to Executive Order 14028 (12 May 2021). Eleven recommended techniques."

nist-800-53b:   # read directly (csrc page only; PDF not fetched)
  title: "Control Baselines for Information Systems and Organizations"
  author: "Joint Task Force"
  org: "National Institute of Standards and Technology (NIST)"
  date: "September 2020 (includes updates as of Dec. 10, 2020); Release 5.2.0 issued 2025-08-27 with no baseline changes"
  url: "https://csrc.nist.gov/pubs/sp/800/53/b/upd1/final"
  accessed: "2026-11-20"
  note: "NIST SP 800-53B. DOI https://doi.org/10.6028/NIST.SP.800-53B. Three security control baselines (low, moderate, high impact) plus a privacy baseline."

nist-800-53:   # read directly (csrc page; PDF of the original Rev. 5 text read)
  title: "Security and Privacy Controls for Information Systems and Organizations"
  author: "Joint Task Force"
  org: "National Institute of Standards and Technology (NIST)"
  date: "September 2020 (includes updates as of Dec. 10, 2020); Release 5.2.0 issued 2025-08-27"
  url: "https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final"
  accessed: "2026-11-20"
  note: "NIST SP 800-53 Rev. 5. DOI https://doi.org/10.6028/NIST.SP.800-53r5. The controls AC-5 (Separation of Duties) and AC-6 (Least Privilege) checked in the PDF at https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf. Note the Release 5.2.0 planning note on the CSRC page."

nasa-swe-052:   # read directly
  title: "SWE-052 - Bidirectional Traceability"
  author: "not printed"
  org: "NASA (NASA Software Engineering and Assurance Handbook, NASA-HDBK-2203)"
  date: "handbook cover prints 'NASA-HDBK-2203B, Approved: March 08, 2022, Superseding NASA-HDBK-2203A'; page not dated"
  url: "https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability"
  accessed: "2026-11-20"
  note: "Original URL https://swehb.nasa.gov/display/SWEHBVD/SWE-052+-+Bidirectional+Traceability redirects to the URL above. Tab title: 'SWE-052 - Bidirectional Traceability - SW Engineering Handbook Ver D - Global Site' ('Ver D' = the handbook version for NPR 7150.2D). Page says 'SWE-052 - Last used in rev NPR 7150.2D'; the NPR 7150.2D text is requirement 3.12.1. Document history log on the handbook home page lists Revision C, 03-08-2022, addressing NPR 7150.2D (the cover calls the document NASA-HDBK-2203B: the two labels differ as printed)."

tw-radar-decoupling:   # read directly
  title: "Decoupling deployment from release"
  author: "not printed (Thoughtworks Technology Radar entry)"
  org: "Thoughtworks, Inc."
  date: "published 2015-11-10; last updated 2016-04-05 (as printed)"
  url: "https://www.thoughtworks.com/radar/techniques/decoupling-deployment-from-release"
  accessed: "2026-11-20"
  note: "Technique blip. Timeline on the page: Apr 2016, Adopt; Nov 2015, Adopt. The description text appears only under the Apr 2016 entry; the Nov 2015 entry has no description on the page. Page banner: 'NOT ON THE CURRENT EDITION'. No person or source is credited with the distinction. Tab title: 'Decoupling deployment from release | Technology Radar | Thoughtworks'."

fowler-deployment-pipeline:   # read directly
  title: "Deployment Pipeline"
  author: "Martin Fowler"
  org: "martinfowler.com"
  date: "30 May 2013"
  url: "https://martinfowler.com/bliki/DeploymentPipeline.html"
  accessed: "2026-11-20"
  note: "Bliki entry. Acknowledgements: 'Jez Humble provided detailed help with this page.' Refers to chapter 5 of the Continuous Delivery book."

fowler-blue-green:   # read directly
  title: "Blue Green Deployment"
  author: "Martin Fowler"
  org: "martinfowler.com"
  date: "1 March 2010 (page also records an update on 2015-06-05 adding the database paragraph)"
  url: "https://martinfowler.com/bliki/BlueGreenDeployment.html"
  accessed: "2026-11-20"
  note: "Says Dave Farley and Jez Humble were 'finishing up a book' (Continuous Delivery) and that their section on blue-green deployment caught his eye. Says 'Some foggy combination of Daniel Terhorst-North and Jez Humble came up with the name.'"

fowler-canary-release:   # read directly
  title: "Canary Release"
  author: "Danilo Sato"
  org: "martinfowler.com"
  date: "25 June 2014"
  url: "https://martinfowler.com/bliki/CanaryRelease.html"
  accessed: "2026-11-20"
  note: "Byline printed on the page: Danilo Sato."

fowler-dark-launching:   # read directly
  title: "Dark Launching"
  author: "Martin Fowler"
  org: "martinfowler.com"
  date: "29 April 2020"
  url: "https://martinfowler.com/bliki/DarkLaunching.html"
  accessed: "2026-11-20"
  note: "Says dark launching assesses load and performance impact 'before making a public announcement of the new capability'; notes the term has been subject to semantic diffusion."

fowler-feature-toggles:   # read directly
  title: "Feature Toggles (aka Feature Flags)"
  author: "Pete Hodgson"
  org: "martinfowler.com"
  date: "09 October 2017 (printed date; page's Significant Revisions: first installment 19 January 2016, complete article 08 February 2016, 09 October 2017 'highlight feature flag as a synonym')"
  url: "https://martinfowler.com/articles/feature-toggles.html"
  accessed: "2026-11-20"
  note: "Article hosted on martinfowler.com. Resolved URL unchanged. The bliki entry https://martinfowler.com/bliki/FeatureToggle.html redirects to https://martinfowler.com/bliki/FeatureFlag.html (Martin Fowler, 29 October 2010). Release Toggles section calls them 'the most common way to implement the Continuous Delivery principle of \"separating [feature] release from [code] deployment.\"'"

fowler-evodb:   # read directly
  title: "Evolutionary Database Design"
  author: "Pramod Sadalage and Martin Fowler"
  org: "martinfowler.com"
  date: "May 2016 (complete rewrite; original publication January 2003)"
  url: "https://martinfowler.com/articles/evodb.html"
  accessed: "2026-11-20"
  note: "Significant Revisions on the page: 'May 2016: Complete rewrite'; 'January 2003: Original publication'."

fowler-test-pyramid:   # read directly
  title: "Test Pyramid"
  author: "Martin Fowler"
  org: "martinfowler.com"
  date: "1 May 2012"
  url: "https://martinfowler.com/bliki/TestPyramid.html"
  accessed: "2026-11-20"
  note: "Etymology section credits Mike Cohn, Succeeding with Agile (2009), where it is called the 'Test Automation Pyramid'; says he drew it with Lisa Crispin in 2003-4 and that Jason Huggins independently arrived at the idea around 2006."

fowler-given-when-then:   # read directly
  title: "Given When Then"
  author: "Martin Fowler"
  org: "martinfowler.com"
  date: "21 August 2013"
  url: "https://martinfowler.com/bliki/GivenWhenThen.html"
  accessed: "2026-11-20"
  note: "Credits Daniel Terhorst-North and Chris Matts (BDD); a footnote says Dan credits Ivan Moore for significant inspiration."

fowler-ci:   # read directly
  title: "Continuous Integration"
  author: "Martin Fowler"
  org: "martinfowler.com"
  date: "18 January 2024 (revised version; page also lists 18 October 2023 rewrite began and 01 May 2006 complete rewrite)"
  url: "https://martinfowler.com/articles/continuousIntegration.html"
  accessed: "2026-11-20"
  note: "Practice headings include Automate the Build; Make the Build Self-Testing; Everyone Pushes Commits To the Mainline Every Day; Fix Broken Builds Immediately; Keep the Build Fast; Test in a Clone of the Production Environment; Everyone can see what's happening; Automate Deployment."

fowler-selftesting:   # read directly
  title: "Self Testing Code"
  author: "Martin Fowler"
  org: "martinfowler.com"
  date: "1 May 2014"
  url: "https://martinfowler.com/bliki/SelfTestingCode.html"
  accessed: "2026-11-20"
  note: "Bliki entry."

bockeler-sdd:   # read directly
  title: "Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl"
  author: "Birgitta Böckeler"
  org: "martinfowler.com (Exploring Gen AI series)"
  date: "15 October 2025"
  url: "https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html"
  accessed: "2026-11-20"
  note: "Defines spec-first, spec-anchored and spec-as-source; describes Kiro, spec-kit and the Tessl Framework."

humble-farley-cd:   # read directly (publisher catalogue page, table of contents, free sample chapter 5); book text beyond that not readable
  title: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation"
  author: "Jez Humble, David Farley"
  org: "Addison-Wesley Professional (Addison-Wesley Signature Series (Fowler))"
  date: "Published Jul 27, 2010 (InformIT); 'Copyright 2011' also printed; 1st edition; ISBN-13 978-0-321-60191-9"
  url: "https://www.informit.com/store/continuous-delivery-reliable-software-releases-through-9780321601919"
  accessed: "2026-11-20"
  note: "Only the catalogue page, table of contents and the free sample chapter 'Continuous Delivery: Anatomy of the Deployment Pipeline' (chapter 5, https://www.informit.com/articles/article.aspx?p=1621865, 'Sep 7, 2010') were readable. Table of contents lists chapter 7 as 'Commit Testing Stage' (not 'The Commit Stage'), chapter 8 'Automated Acceptance Testing', chapter 10 'Deploying and Releasing Applications'. Chapter text for 7, 8 and 10 not readable."
```

### A.Google SRE and engineering, OWASP (2.8, 2.10)

```yaml
sre-book-release-engineering:   # read directly
  title: "Release Engineering"
  author: "Dinah McNutt (chapter byline: 'Written by Dinah McNutt'; 'Edited by Betsy Beyer and Tim Harvey')"
  org: "Google, Site Reliability Engineering (book, first edition), O'Reilly Media; sre.google"
  date: "chapter page footer: Copyright © 2017 Google, Inc.; the book's preface prints 'Copyright 2016 Google, Inc.' in its citation example (book edited by Betsy Beyer, Chris Jones, Jennifer Petoff and Niall Richard Murphy)"
  url: "https://sre.google/sre-book/release-engineering/"
  accessed: "2026-11-20"
  note: "Chapter 8 of the SRE book. Describes hermetic builds (same revision built on different machines gives identical results; builds depend on known versions of build tools and dependencies); gated operations (approving source code changes, specifying release actions, creating a new release, approving the initial integration proposal and subsequent cherry picks, deploying a new release, changing a project's build configuration); canary deployments (a few jobs in production after system tests); and rollouts that fit the risk profile of a service, for example starting in one cluster and expanding exponentially, or extending over several days for sensitive infrastructure. The chapter does not use the word 'incubation'. Page tab title differs: 'Google SRE: Role of Release Engineer and Best Practices'."

sre-workbook-canarying:   # read directly
  title: "Canarying Releases"
  author: "Alec Warner and Štěpán Davidovič, with Alex Hidalgo, Betsy Beyer, Kyle Smith, and Matt Duftler"
  org: "Google, The Site Reliability Workbook (O'Reilly Media); sre.google"
  date: "chapter page footer: Copyright © 2018 Google, Inc.; preface citation example: Copyright 2018 Google LLC. Workbook edited by Betsy Beyer, Niall Richard Murphy, David K. Rensin, Kent Kawahara and Stephen Thorne"
  url: "https://sre.google/workbook/canarying-releases/"
  accessed: "2026-11-20"
  note: "Chapter 16 of the Workbook. Defines canarying as a partial and time-limited deployment of a change in a service and its evaluation; the part of the service that receives the change is 'the canary' and the remainder 'the control'. Page tab title differs: 'Google SRE - Canary Release: Deployment Safety and Efficiency'."

sre-book-monitoring:   # read directly
  title: "Monitoring Distributed Systems"
  author: "Rob Ewaschuk (chapter byline: 'Written by Rob Ewaschuk'; 'Edited by Betsy Beyer')"
  org: "Google, Site Reliability Engineering (book, first edition), O'Reilly Media; sre.google"
  date: "chapter page footer: Copyright © 2017 Google, Inc.; book preface citation example prints 2016"
  url: "https://sre.google/sre-book/monitoring-distributed-systems/"
  accessed: "2026-11-20"
  note: "Chapter 6 of the SRE book. States that a monitoring system should address two questions, what is broken and why, and names the four golden signals as latency, traffic, errors and saturation. Page tab title differs and does not match the chapter: 'Google SRE: SRE Responsibilities and Management Frameworks'."

sre-book-being-on-call:   # read directly
  title: "Being On-Call"
  author: "Andrea Spadaccini (chapter byline: 'Written by Andrea Spadaccini'; 'Edited by Kavita Guliani'; the extracted text shows a trailing footnote marker '56', which is a footnote about an earlier version in ;login: October 2015)"
  org: "Google, Site Reliability Engineering (book, first edition), O'Reilly Media; sre.google"
  date: "chapter page footer: Copyright © 2017 Google, Inc.; book preface citation example prints 2016"
  url: "https://sre.google/sre-book/being-on-call/"
  accessed: "2026-11-20"
  note: "Chapter 11 of the SRE book. After a page is acknowledged the on-call engineer is expected to triage the problem and work toward its resolution, possibly involving other team members and escalating as needed; many teams have both a primary and a secondary on-call rotation. Page tab title differs: 'Google SRE - On Call Engineer Best Practices for IT Services'."

sre-book-managing-incidents:   # read directly
  title: "Managing Incidents"
  author: "Andrew Stribblehill (chapter byline: 'Written by Andrew Stribblehill'; 'Edited by Kavita Guliani'; the extracted text shows a trailing footnote marker '78', a footnote about an earlier version in ;login: April 2015)"
  org: "Google, Site Reliability Engineering (book, first edition), O'Reilly Media; sre.google"
  date: "chapter page footer: Copyright © 2017 Google, Inc.; book preface citation example prints 2016"
  url: "https://sre.google/sre-book/managing-incidents/"
  accessed: "2026-11-20"
  note: "Chapter 14 of the SRE book. Google's incident management system is based on the Incident Command System; the chapter lists four roles (incident command, operational work, communication, planning) and says the operations team should be the only group modifying the system during an incident. Page tab title differs: 'Google SRE - Incident Management: Key to Restore Operations'."

sre-workbook-incident-response:   # read directly
  title: "Incident Response"
  author: "Jennifer Mace, Jelena Oertel, Stephen Thorne, and Arup Chakrabarti (PagerDuty), with Jian Ma and Jessie Yang"
  org: "Google, The Site Reliability Workbook (O'Reilly Media); sre.google"
  date: "chapter page footer: Copyright © 2018 Google, Inc.; preface citation example: Copyright 2018 Google LLC"
  url: "https://sre.google/workbook/incident-response/"
  accessed: "2026-11-20"
  note: "Chapter 9 of the Workbook. Describes incident management at Google and PagerDuty based on the Incident Command System (roles Incident Commander, Communications Lead, Operations Lead), four case studies (three from Google, one from PagerDuty) and a checklist. Page tab title differs: 'Google SRE - Root Cause Analysis for Probing Incident'."

google-sre-postmortem:   # read directly (existing key; fields already correct)
  title: "Postmortem Culture: Learning from Failure"
  author: "Daniel Rogers, Murali Suriar, Sue Lueder, Pranjal Deo, and Divya Sudhakar, with Gary O'Connor and Dave Rensin"
  org: "Google, The Site Reliability Workbook (O'Reilly Media); sre.google"
  date: "chapter page footer: Copyright © 2018 Google, Inc."
  url: "https://sre.google/workbook/postmortem-culture/"
  accessed: "2026-11-20"
  note: "Chapter 10 of the Workbook. States that action items with little or no ownership are less likely to be resolved ('Actions items without clear owners are less likely to be resolved') and that 'The value of a postmortem is proportional to the learning it creates'."

google-agentic-sre:   # read directly
  title: "AI in SRE: Where and how Google is deploying agentic AI to improve operations"
  author: "Stevan Malesevic (Distinguished Software Engineer) and Christopher Heiser (Distinguished Site Reliability Engineer)"
  org: "Google Cloud Blog (DevOps & SRE)"
  date: "May 28, 2026"
  url: "https://cloud.google.com/blog/products/devops-sre/how-google-sre-is-using-agentic-ai-to-improve-operations"
  accessed: "2026-11-20"
  note: "On-page heading is the title above; the browser tab title is 'How Google SRE is using agentic AI to improve operations | Google Cloud Blog' (matches the URL slug). Describes agents layered on Google's incident management (IMAG) that consolidate incident communications, create handoff documents, draft postmortems and manage communications; separate agents that investigate incidents and in some cases mitigate autonomously; consistent controls to prevent unwanted mutations of production state; and says an agentic approach does not necessarily imply removing people, specifically for higher-risk services. Gives no outcome statistics. Links a whitepaper 'AI in SRE Practice: Moving Beyond Automation at Google' (not read)."

google-eng-practices-review:   # read directly (raw.githubusercontent.com, same file as the github.com blob; also read Google's rendered copy)
  title: "What to look for in a code review"
  author: "not printed"
  org: "Google (repository google/eng-practices, 'Google Engineering Practices Documentation'; licensed CC-By 3.0 per the repository README)"
  date: "not printed"
  url: "https://github.com/google/eng-practices/blob/master/review/reviewer/looking-for.md"
  accessed: "2026-11-20"
  note: "Markdown heading '# What to look for in a code review'. Section headings in order: Design, Functionality, Complexity, Tests, Naming, Comments, Style, Consistency, Documentation (followed by Every Line, Context, Good Things, Summary). Under Tests: 'Ask for unit, integration, or end-to-end tests as appropriate for the change.' Rendered copy: https://google.github.io/eng-practices/review/reviewer/looking-for.html (tab title 'What to look for in a code review | eng-practices'; HTTP Last-Modified header Thu, 19 Sep 2024, a site-deploy header not a date printed on the page)."

google-eng-practices-small-cls:   # read directly (raw.githubusercontent.com, same file as the github.com blob; also read Google's rendered copy)
  title: "Small CLs"
  author: "not printed"
  org: "Google (repository google/eng-practices, 'Google Engineering Practices Documentation'; licensed CC-By 3.0 per the repository README)"
  date: "not printed"
  url: "https://github.com/google/eng-practices/blob/master/review/developer/small-cls.md"
  accessed: "2026-11-20"
  note: "Markdown heading '# Small CLs'. Small CLs are reviewed more quickly and more thoroughly, less likely to introduce bugs, and simpler to roll back. Right size: one self-contained change that makes a minimal change addressing just one thing and includes related test code. Rendered copy: https://google.github.io/eng-practices/review/developer/small-cls.html (tab title 'Small CLs | eng-practices')."

petrovic-mutation:   # not read directly (dl.acm.org returned HTTP 403 to a plain GET)
  title: "State of Mutation Testing at Google"
  author: "Goran Petrović and Marko Ivanković (UNCONFIRMED: dl.acm.org not readable; worklist wording only)"
  org: "ACM / ICSE-SEIP 2018 (UNCONFIRMED)"
  date: "2018 (UNCONFIRMED)"
  url: "https://dl.acm.org/doi/10.1145/3183519.3183521"
  accessed: "2026-11-20"
  note: "Not read. No claim in this entry has been verified. Needs an author-hosted or publisher record that a plain GET can read, or a different reader."

owasp-asvs:   # read directly (raw.githubusercontent.com, same file as the github.com blob)
  title: "What is the ASVS?"
  author: "OWASP ASVS project (project leads on the Frontispiece: Daniel Cuthbert, Elar Lang, Josh C Grossman)"
  org: "OWASP Foundation (Copyright © 2008-2025 The OWASP Foundation; CC BY-SA 4.0)"
  date: "Version 5.0.0, May 2025 (as printed on 5.0/en/0x01-Frontispiece.md; the repository README calls 5.0.0 'dated May 2025' and the latest stable version)"
  url: "https://github.com/OWASP/ASVS/blob/master/5.0/en/0x03-What-is-the-ASVS.md"
  accessed: "2026-11-20"
  note: "Chapter 'What is the ASVS?' of ASVS 5.0.0. Rather than prescribing a level, an organization should analyze its risks and decide what level it should be at; Level 1 contains the minimum requirements, Level 2 is what most applications should strive for, Level 3 is for the highest levels of security. About 350 requirements in 17 chapters, each further divided into sections; identifiers take the form chapter.section.requirement. Forks are encouraged provided traceability is kept. Writers and tools are advised to cite with the version, e.g. v5.0.0-1.2.5, because identifiers may change between versions."

owasp-wstg:   # read directly (README via raw.githubusercontent.com; the github.com repository root itself was not fetched)
  title: "OWASP Web Security Testing Guide"
  author: "OWASP WSTG project (project leaders listed in the README: Rick Mitchell, Elie Saad)"
  org: "OWASP Foundation (Open Worldwide Application Security Project)"
  date: "last stable release 4.2 per the README; version 5.0 in progress (no date printed in the README)"
  url: "https://github.com/OWASP/wstg"
  accessed: "2026-11-20"
  note: "README describes the WSTG as a comprehensive guide to testing the security of web applications and web services, created by collaborative efforts of security professionals and volunteers. Scenario identifiers take the form WSTG-<category>-<number> (example WSTG-INFO-02), and the README prefers a versioned form such as WSTG-v42-INFO-02. README says 'We are currently working on release version 5.0' and 'For the last stable release, check release 4.2'."

owasp-secrets-management:   # read directly
  title: "Secrets Management Cheat Sheet"
  author: "not printed (page footer credits 'Cheat Sheets Series Team')"
  org: "OWASP Cheat Sheet Series"
  date: "not printed"
  url: "https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html"
  accessed: "2026-11-20"
  note: "Introduction says organizations need to centralize the storage, provisioning, auditing, rotation and management of secrets. Section 2.3 Access Control applies the Least Privilege principle; section 2.6 Auditing lists what to audit at minimum, including who requested a secret and for what system and role, and when a secret was used and by whom/what. Tab title: 'Secrets Management - OWASP Cheat Sheet Series'."

owasp-threat-modeling-cs:   # read directly
  title: "Threat Modeling Cheat Sheet"
  author: "not printed (page footer credits 'Cheat Sheets Series Team')"
  org: "OWASP Cheat Sheet Series"
  date: "not printed"
  url: "https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html"
  accessed: "2026-11-20"
  note: "Breaks threat modeling into four basic steps: application decomposition, threat identification and ranking, mitigations, and review and validation, guided by the four Threat Modeling Manifesto questions. Tab title: 'Threat Modeling - OWASP Cheat Sheet Series'."
```

### A.Other public sources (2.11)

```yaml
itil4-deployment-management:   # read directly
  title: "ITIL 4 Practitioner: Deployment Management"
  author: "not printed"
  org: "PeopleCert"
  date: "not printed (page footer: (c) 2026 PeopleCert)"
  url: "https://www.peoplecert.org/browse-certifications/it-governance-and-service-management/ITIL-1/itil-4-practitioner-deployment-management-3796"
  accessed: "2026-11-20"
  note: "PeopleCert certification catalogue page (tab title 'ITIL 4 Practitioner: Deployment Management | peoplecert.org | Peoplecert'; H1 captured as 'Purchase options'), not the ITIL practice guide. Describes the course as learning 'how to move new or changed hardware, software, documentation, processes, or any other component to live environments, and how to deploy components to other environments for testing or staging'. The page does not print the words 'purpose of deployment management' as a definition and does not mention AXELOS."

itil4-release-management:   # read directly
  title: "ITIL 4 Practitioner: Release Management"
  author: "not printed"
  org: "PeopleCert"
  date: "not printed (page footer: (c) 2026 PeopleCert)"
  url: "https://www.peoplecert.org/browse-certifications/it-governance-and-service-management/ITIL-1/itil-4-practitioner-release-management-3798"
  accessed: "2026-11-20"
  note: "PeopleCert certification catalogue page, not the practice guide. Describes the course as learning 'best practices for making new and changed services available for use, in line with your organisation's policies and any agreements between the organisation and its service consumers'. Page lists Release Management as its own certification, separate from the Deployment Management certification page; it does not itself state that they are separate ITIL practices."

twelve-factor-config:   # read directly
  title: "III. Config (Store config in the environment)"
  author: "Adam Wiggins"
  org: "The Twelve-Factor App"
  date: "last updated 2017 (as printed)"
  url: "https://12factor.net/config"
  accessed: "2026-11-20"
  note: "Browser tab title and H1 are both 'The Twelve-Factor App'; the factor heading is 'III. Config'. Footer: 'Written by Adam Wiggins - Last updated 2017'; copyright line 2026 Salesforce, Inc."

twelve-factor-parity:   # read directly
  title: "X. Dev/prod parity (Keep development, staging, and production as similar as possible)"
  author: "Adam Wiggins"
  org: "The Twelve-Factor App"
  date: "last updated 2017 (as printed)"
  url: "https://12factor.net/dev-prod-parity"
  accessed: "2026-11-20"
  note: "Tab title and H1 are 'The Twelve-Factor App'; factor heading 'X. Dev/prod parity'. Footer 'Written by Adam Wiggins - Last updated 2017'."

threat-modeling-manifesto:   # read directly
  title: "Threat Modeling Manifesto"
  author: "Working group: Zoe Braiterman, Adam Shostack, Jonathan Marcil, Stephen de Vries, Irene Michlin, Kim Wuyts, Robert Hurlbut, Brook S.E. Schoenfield, Fraser Scott, Matthew Coles, Chris Romeo, Alyssa Miller, Izar Tarandach, Avi Douglen, Marc French"
  org: "Threat Modeling Manifesto working group"
  date: "not printed (site says 'You can always find the current version of this manifesto at https://www.threatmodelingmanifesto.org/'; licensed CC BY 4.0)"
  url: "https://www.threatmodelingmanifesto.org/"
  accessed: "2026-11-20"
  note: "Page lists the 15 working-group members under 'Authors' (order as printed) and thanks Loren Kohnfelder and Sheila Kamath for technical edit review. States 'when we threat model, we ask four key questions: What are we working on? What can go wrong? What are we going to do about it? Did we do a good enough job?'. No publication date is printed on the page or in its linked PDF. The site's HTTP Last-Modified (2026-05-28) is a build time, not a publication date."

sei-atam:   # read directly (two reports read; see Part D)
  title: "The Architecture Tradeoff Analysis Method"
  author: "Rick Kazman, Mark Klein, Mario Barbacci, Tom Longstaff, Howard Lipson, Jeromy Carriere"
  org: "Software Engineering Institute, Carnegie Mellon University (CMU/SEI-98-TR-008, ESC-TR-98-008)"
  date: "July 1998"
  url: "https://www.sei.cmu.edu/documents/1186/1998_005_001_16646.pdf"
  accessed: "2026-11-20"
  note: "The URL in the draft is the 1998 technical report, not the definitive 2000 report. Its abstract: 'a structured technique for understanding the tradeoffs inherent in the architectures of software-intensive systems'. It elicits scenarios and evaluates each quality attribute in turn, but does not describe prioritising scenarios. The prioritisation wording is in the 2000 report CMU/SEI-2000-TR-004 'ATAM: Method for Architecture Evaluation' (Rick Kazman, Mark Klein, Paul Clements, August 2000), https://www.sei.cmu.edu/documents/629/2000_005_001_13706.pdf (catalogue page https://www.sei.cmu.edu/library/atam-method-for-architecture-evaluation/)."

slsa-build-track-basics:   # read directly
  title: "Build: Track Basics"
  author: "not printed"
  org: "SLSA (Linux Foundation, Community Specification License 1.0)"
  date: "version SLSA v1.2, Status: Approved (no release date printed)"
  url: "https://slsa.dev/spec/v1.2/build-track-basics"
  accessed: "2026-11-20"
  note: "Tab title 'SLSA - Build: Track Basics'; H1 'Build: Track Basics'. Table: Build L1 'Provenance showing how the package was built'; L2 'Signed provenance, generated by a hosted build platform'; L3 'Hardened build platform'. The page prints no month; '2025-11' is not on the page."

slsa-provenance:   # read directly
  title: "Build: Provenance"
  author: "not printed"
  org: "SLSA (Linux Foundation)"
  date: "version SLSA v1.2, Status: Approved (no release date printed)"
  url: "https://slsa.dev/spec/v1.2/build-provenance"
  accessed: "2026-11-20"
  note: "Tab title 'SLSA - Build: Provenance'. Describes provenance as 'verifiable information about software artifacts describing where, when, and how something was produced'."

spec-kit-sdd:   # read directly (from raw.githubusercontent.com, same file)
  title: "Specification-Driven Development (SDD)"
  author: "not printed"
  org: "GitHub (github/spec-kit repository)"
  date: "not printed"
  url: "https://github.com/github/spec-kit/blob/main/spec-driven.md"
  accessed: "2026-11-20"
  note: "github.com returns HTTP 403 to a plain request; text read from https://raw.githubusercontent.com/github/spec-kit/main/spec-driven.md (same file). First heading '# Specification-Driven Development (SDD)'. Templates 'mandate the use of [NEEDS CLARIFICATION] markers' ('Don't guess'); checklists 'act as \"unit tests\" for the specification'; constitution with Simplicity Gate (Article VII) and Anti-Abstraction Gate (Article VIII); gate failures must be documented in a 'Complexity Tracking' section."

spec-kit:   # read directly (README from raw.githubusercontent.com; command reference from the project docs site)
  title: "Spec Kit"
  author: "not printed"
  org: "GitHub (github/spec-kit repository)"
  date: "not printed (docs page Last-Modified header 2026-11-19)"
  url: "https://github.com/github/spec-kit"
  accessed: "2026-11-20"
  note: "github.com returns HTTP 403; README read from https://raw.githubusercontent.com/github/spec-kit/main/README.md (same file). README minimal flow: constitution, specify, plan, tasks, implement, converge (written /speckit-<name> in the README; the docs write /speckit.<name>). Command reference https://github.github.io/spec-kit/reference/agentic-sdd.html (linked from the README): converge 'Assess implementation against the artifacts and append remaining work'; clarify, analyze and checklist are each labelled 'optional quality gate'."

metr-reward-hacking:   # read directly
  title: "Recent Frontier Models Are Reward Hacking"
  author: "Sydney Von Arx, Lawrence Chan, Beth Barnes"
  org: "METR"
  date: "June 5, 2025 (as printed)"
  url: "https://metr.org/blog/2025-06-05-recent-reward-hacking/"
  accessed: "2026-11-20"
  note: "Tab title 'Recent Frontier Models Are Reward Hacking - METR'. Reports reward hacking on METR's own evaluation tasks, including 'modifying the tests or scoring code'. Also says o3 reward hacked in 14 of 20 attempts when the task was framed as research with real-world consequences, so the post is not confined to the evaluation setting."

anthropic-claude-37-system-card:   # read directly (URL redirects to a PDF)
  title: "Claude 3.7 Sonnet System Card"
  author: "Anthropic"
  org: "Anthropic"
  date: "not printed on the document (references cite February 2025 sources)"
  url: "https://www.anthropic.com/claude-3-7-sonnet-system-card"
  accessed: "2026-11-20"
  note: "Redirects to https://assets.claude.com/9ff93dfa8f445c932415d335c88852ef47f1201e.pdf (43 pages). Section 6 'Excessive Focus on Passing Tests': the model 'occasionally resorts to special-casing in order to pass test cases in agentic coding environments like Claude Code', most often 'directly returning expected test values', also 'modifying the problematic tests themselves'. Section 6.1 says the behaviour 'emerged as a result of reward hacking during reinforcement learning training' and partial mitigations were applied before launch."

konstantinou-test-oracles:   # read directly
  title: "Can we find bugs using LLM-generated oracles?"
  author: "Michael Konstantinou, Renzo Degiovanni, Mike Papadakis"
  org: "arXiv (cs.SE)"
  date: "v1 submitted 28 Oct 2024; v2 last revised 5 Oct 2026"
  url: "https://arxiv.org/abs/2410.21136"
  accessed: "2026-11-20"
  note: "Preprint; the arXiv page prints no journal reference or venue. Abstract: 'LLM-based test generation approaches mainly capture the actual program behavior making bug detection difficult'; study covers 'test cases and oracles ... for 24 Java repositories' (the abstract does not say open-source)."

pearce-copilot:   # not read directly (doi.org redirects to ieeexplore.ieee.org, which returns an empty HTTP 202 response); arXiv preprint read as a labelled substitute
  title: "Asleep at the Keyboard? Assessing the Security of GitHub Copilot's Code Contributions"
  author: "Hammond Pearce, Baleegh Ahmad, Benjamin Tan, Brendan Dolan-Gavitt, Ramesh Karri"
  org: "IEEE Symposium on Security and Privacy 2022 (venue per the draft; not confirmed from a page)"
  date: "arXiv v1 20 Aug 2021; v3 16 Dec 2021"
  url: "https://doi.org/10.1109/SP46214.2022.9833571"
  accessed: "2026-11-20"
  note: "SUBSTITUTE: bibliographic facts read from the author preprint https://arxiv.org/abs/2108.09293, not from the IEEE record. The preprint abstract reports that a share of Copilot's programs in the tested scenarios were vulnerable (no percentage to be carried forward). The preprint's Comments field is empty, so the S&P 2022 venue is not confirmed by anything read."

perry-2023:   # not read directly (doi.org returns HTTP 403 via ACM); arXiv preprint read as a labelled substitute
  title: "Do Users Write More Insecure Code with AI Assistants?"
  author: "Neil Perry, Megha Srivastava, Deepak Kumar, Dan Boneh"
  org: "ACM SIGSAC Conference on Computer and Communications Security (CCS '23) (existing entry; venue not re-confirmed)"
  date: "2023-11 (existing entry; arXiv v1 7 Nov 2022, v3 18 Dec 2023)"
  url: "https://doi.org/10.1145/3576915.3623157"
  accessed: "2026-11-20"
  note: "SUBSTITUTE: read https://arxiv.org/abs/2211.03622. Authors match. Abstract: participants with an AI assistant 'wrote significantly less secure code' and 'were more likely to believe they wrote secure code'. The assistant was based on OpenAI's codex-davinci-002. The ACM record itself was not readable."

ahmed-incident-llm:   # read directly
  title: "Recommending Root-Cause and Mitigation Steps for Cloud Incidents using Large Language Models"
  author: "Toufique Ahmed, Supriyo Ghosh, Chetan Bansal, Tom Zimmermann, Xuchao Zhang, Saravan Rajmohan"
  org: "Microsoft Research; ICSE 2023"
  date: "May 2023 (as printed on the publication page)"
  url: "https://www.microsoft.com/en-us/research/publication/recommending-root-cause-and-mitigation-steps-for-cloud-incidents-using-large-language-models/"
  accessed: "2026-11-20"
  note: "Publication page prints 'ICSE 2023 | May 2023'. Abstract: 'the first large-scale study to evaluate the effectiveness of these models for helping engineers root cause and mitigate production incidents ... more than 40,000 incidents', zero-shot, fine-tuned and multi-task settings, with human evaluation by incident owners. The page text does not say 'offline' or 'one cloud provider'. The page prints the surname Ghosh as 'GHOSH'."

chen-rcacopilot:   # read directly
  title: "Automatic Root Cause Analysis via Large Language Models for Cloud Incidents"
  author: "Yinfang Chen, Huaibing Xie, Minghua Ma, Yu Kang, Xin Gao, Liu Shi, Yunjie Cao, Xuedong Gao, Hao Fan, Ming Wen, Jun Zeng, Supriyo Ghosh, Xuchao Zhang, Chaoyun Zhang, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang, Tianyin Xu"
  org: "arXiv (cs.SE)"
  date: "v1 25 May 2023; v4 last revised 13 Nov 2023"
  url: "https://arxiv.org/abs/2305.15778"
  accessed: "2026-11-20"
  note: "18 authors as printed. The arXiv page prints no venue ('EuroSys 2024' is NOT on the page). Abstract: RCACopilot 'matches incoming incidents to corresponding incident handlers based on their alert types, aggregates the critical runtime diagnostic information, predicts the incident's root cause category, and provides an explanatory narrative'; evaluated on 'a year's worth of incidents from Microsoft'; 'RCA accuracy up to 0.766'."

requirements-ambiguity-llm:   # read directly
  title: "Requirements Ambiguity Detection and Explanation with LLMs: An Industrial Study"
  author: "Sarmad Bashir, Alessio Ferrari, Muhammad Abbas Khan, Per Erik Strandberg, Zulqarnain Haider, Mehrdad Saadatmand, Markus Bohlin"
  org: "41st International Conference on Software Maintenance and Evolution (ICSME 2025)"
  date: "September 2025 (as printed in the repository record's BibTeX); pages 620-631"
  url: "https://www.ipr.mdu.se/pdf_publications/7221.pdf"
  accessed: "2026-11-20"
  note: "The PDF itself prints title and authors (as 'Abbas Khan') but no venue or year. Venue, month, year, pages and DOI 10.1109/ICSME64153.2025.00063 are printed on the Malardalen University publication record https://www.ipr.mdu.se/publications/7221- (venue printed as '41st International Conference on Software Maintenance and Evolution'; the record spells 'ICSME' only inside the DOI). Abstract: 20.2% average performance increase with ten in-context demonstrations versus none (do not carry the figure forward); human evaluation with eight industry experts."

gotel-finkelstein-1994:   # read directly
  title: "An analysis of the requirements traceability problem"
  author: "Orlena C. Z. Gotel, Anthony C. W. Finkelstein"
  org: "Proceedings of 1st International Conference on Requirements Engineering, IEEE Computer Society Press"
  date: "1994 (pp. 94-101)"
  url: "https://discovery.ucl.ac.uk/id/eprint/749/"
  accessed: "2026-11-20"
  note: "https://discovery.ucl.ac.uk/749/ redirects to the id/eprint/749/ URL. Paper PDF (https://discovery.ucl.ac.uk/id/eprint/749/1/2.2_rtprob.pdf) is titled 'An Analysis of the Requirements Traceability Problem'; authors from Imperial College. It defines: 'Requirements traceability refers to the ability to describe and follow the life of a requirement, in both a forwards and backwards direction (i.e., from its origins, through its development and specification, to its subsequent deployment and use, and through all periods of on-going refinement and iteration in any of these phases).'"

rath-traceability-wild-2018:   # ACM record not read (HTTP 403 from dl.acm.org and doi.org); author preprint read as a labelled substitute
  title: "Traceability in the Wild: Automatically Augmenting Incomplete Trace Links"
  author: "Michael Rath, Jacob Rendall, Jin L.C. Guo, Jane Cleland-Huang, Patrick Mäder"
  org: "ICSE '18: 40th International Conference on Software Engineering, Gothenburg, Sweden, May 27-June 3, 2018"
  date: "2018"
  url: "https://doi.org/10.1145/3180155.3180207"
  accessed: "2026-11-20"
  note: "SUBSTITUTE: facts read from the authors' arXiv preprint https://arxiv.org/abs/1804.02433 (v1, 6 Apr 2018; Comments field 'ICSE 2018'; Related DOI listed as 10.1145/3180155.3180207) and its PDF https://arxiv.org/pdf/1804.02433, which prints an ACM Reference Format with that DOI and ACM ISBN 978-1-4503-5638-1/18/05. arXiv spells the last author 'Maeder'; the PDF prints 'Mäder'. The ACM Digital Library record itself was not readable."

reinertsen-flow-2009:   # authoritative record NOT found; retail record read
  title: "The Principles of Product Development Flow: Second Generation Lean Product Development"
  author: "Donald G. Reinertsen"
  org: "not confirmed (publisher not printed in the readable text of the Goodreads page)"
  date: "first published May 1, 2009 (per Goodreads page)"
  url: "https://www.goodreads.com/book/show/6278270-the-principles-of-product-development-flow"
  accessed: "2026-11-20"
  note: "Only a retail/community record was readable. Goodreads page prints title, author, '294 pages, Hardcover' and 'First published May 1, 2009'. Publisher 'Celeritas Publishing' is not printed in the page text. No publisher, library or author site could be read (see Part D, question 12). The book text was not read, so 'weighted shortest job first', cost-of-delay sequencing and the cost-of-delay quotation are not checkable."
```

## B. Claims table

| claim id | source key | verdict | what the source actually says |
|---|---|---|---|
| safe-framework#1 | safe-framework | SUPPORTED | "A Planning Interval (PI) is a cadence-based timebox in which Agile Release Trains deliver continuous value to customers in alignment with PI Objectives." Fig. 1 text: "a PI begins with a PI Planning event, followed by four development iterations, and ends with one IP (innovation and planning) iteration." |
| safe-framework#2 | safe-framework | SUPPORTED | "Last Update: 25 February 2025" |
| safe-configurations#1 | safe-configurations | SUPPORTED | Lists "Full SAFe / Essential SAFe / Large Solution SAFe / Portfolio SAFe" under "SAFe 6.0 Configurations"; "Last Updated: 3 September 2025" |
| safe-configurations#2 | safe-configurations | NOT FOUND | Page is a link list only. Large Solution wording is on /large-solution (last update 2022-12-05): "Large Solution SAFe is for enterprises building large and complex solutions that do not require portfolio concerns." |
| safe-portfolio#1 | safe-portfolio | SUPPORTED | "A SAFe Portfolio is a set of value streams that delivers a continuous flow of valuable solutions to customers within a common funding and governance model." |
| safe-art#1 | safe-art | SUPPORTED | "a long-lived team of Agile teams that incrementally develops, delivers, and often operates one or more solutions in a development value stream." |
| safe-art#2 | safe-art | SUPPORTED | "supported by the key roles of Product Management, System Architect, Release Train Engineer (RTE), and Business Owners." |
| safe-art#3 | safe-art | NOT FOUND (not readable) | Not in readable ART text. /business-owners/ says "primary business and technical responsibility for return on investment (ROI), governance, and compliance"; /essential-safe/ (2022) says "business and technical responsibility for fitness for use, governance, and return on investment (ROI)". "small group of stakeholders" only in /essential-safe/. |
| safe-art#4 | safe-art | NOT FOUND (not readable) | Not in readable ART text. /product-management/: "defining desirable, viable, feasible, and sustainable solutions that meet customer needs" (last update 2024-10-15); /essential-safe/: "desirable, feasible, viable, and sustainable products". |
| safe-agile-teams#1 | safe-agile-teams | SUPPORTED | "a cross-functional group of typically ten or fewer individuals with all the skills necessary to define, build, test, and deliver value to their customer." |
| safe-agile-teams#2 | safe-agile-teams | NOT FOUND (not readable) | Not in readable text. /team-backlog/ (last update 2025-02-12): "a Kanban system ... to capture and manage the user stories and enablers". |
| safe-agile-teams#3 | safe-agile-teams | NOT FOUND (not readable) | Page only names the Product Owner role. "content authority for the team backlog" is in /essential-safe/ (2022); /product-owner/ says "primarily responsible for maximizing the value delivered by the team by ensuring that the team backlog is aligned with customer and stakeholder needs". |
| safe-agile-teams#4 | safe-agile-teams | PARTLY | Page names "the Product Owner and the Scrum Master/Team Coach" as the two critical roles, no description. /scrum-master-team-coach/: "a servant leader and coach for an Agile Team who facilitates team events and processes"; "remove impediments" wording is in /essential-safe/. |
| safe-lpm#1 | safe-lpm | SUPPORTED | "LPM aligns strategy and execution by applying Lean and systems thinking approaches to strategy and investment funding, Agile portfolio operations, and governance." (the words "Lean governance" occur on /portfolio and the discipline page). Page does call LPM "one of the seven core competencies" but says SAFe has "evolved the way in which we think about competencies" and points to the discipline article. |
| safe-lpm#2 | safe-lpm | NOT FOUND | Readable text has no statement about budgets, projects or guardrails. Discipline page: budget "directly allocated to these value streams rather than the traditional approach of project-based funding"; "Guardrails support these budgets by providing governance and spending policies and practices". "lightweight" not found; /portfolio says "minimum necessary governance". |
| safe-lpm-discipline#1 | safe-lpm-discipline | SUPPORTED | "The available portfolio budget is directly allocated to these value streams rather than the traditional approach of project-based funding." Also "Lean budgets provide funding for value streams". (Glossary: "Lean Budgets is a financial governance approach that funds value streams instead of projects".) |
| safe-guardrails#1 | safe-guardrails | SUPPORTED | "Lean Budget Guardrails describe the policies and practices for budgeting, spending, and governance for a specific portfolio." |
| safe-strategic-themes#1 | safe-strategic-themes | PARTLY | "Strategic themes connect the enterprise strategy to a portfolio" (not "to the portfolio vision"); definition: "portfolio-level business objectives that provide competitive differentiation and strategic advantage". |
| safe-strategic-themes#2 | safe-strategic-themes | NOT FOUND (not readable) | Readable text says they give "clarity needed for decentralized decision-making"; no mention of decision criteria in the portfolio backlog. Rest login-walled. |
| safe-portfolio-backlog#1 | safe-portfolio-backlog | SUPPORTED | "a Kanban system that is used to capture and manage the business and enabler epics intended to create and evolve the portfolio's products, services, and solutions." |
| safe-portfolio-backlog#2 | safe-portfolio-backlog | PARTLY | This page: "Portfolio epics are large (and typically cross-cutting initiatives)". The sentence "Epics describe the strategic initiatives that the portfolio is responsible for" is on /lean-portfolio-management-discipline. |
| safe-portfolio-backlog#3 | safe-portfolio-backlog | NOT FOUND (not readable) | Heading "What are the states of the portfolio Kanban?" is visible; the state names are behind the login wall. |
| safe-portfolio-backlog#4 | safe-portfolio-backlog | SUPPORTED | "Portfolio Leadership is responsible for developing, maintaining, and prioritizing the Portfolio backlog." Key Takeaways add "Portfolio Leadership and the Value Management office maintain and manage the portfolio backlog." |
| safe-epic-owner#1 | safe-epic-owner | SUPPORTED | "The Epic Owner is responsible for coordinating epics through the portfolio Kanban system." |
| safe-wsjf#1 | safe-wsjf | SUPPORTED | "In SAFe, WSJF is estimated as the relative cost of delay divided by the relative job duration." (page says "duration"; "job size" appears only in the list of inputs; the formula is not written as a sum in readable text) |
| safe-wsjf#2 | safe-wsjf | SUPPORTED | "relative user and business value, time criticality, risk reduction and/or opportunity enablement, and job size" |
| safe-wsjf#3 | safe-wsjf | SUPPORTED | Epigraph attributed "Don Reinertsen, The Principles of Product Development Flow [1]"; the full reference [1] is not in readable text. |
| safe-wsjf#4 | safe-wsjf | SUPPORTED | "If you only quantify one thing, quantify the Cost of Delay." (page epigraph) |
| safe-cost-of-delay#1 | safe-cost-of-delay | SUPPORTED | "the money or value that will be lost by delaying or not doing a job for a time period relative to other jobs." |
| safe-features#1 | safe-features | SUPPORTED | "solution functionality that delivers business value, fulfills a stakeholder need, and is sized to be delivered by an Agile Release Train within a PI." |
| safe-features#2 | safe-features | SUPPORTED | "large solution functionality whose implementation often spans multiple ARTs and is sized to be delivered within a PI." |
| safe-story#1 | safe-story | SUPPORTED | "Each story focuses on a specific behavior that can be developed in incremental steps"; "Keeping stories small ensures they can be completed in a single iteration". |
| safe-requirements-model#1 | safe-requirements-model | PARTLY | This page lists "Epics, Capabilities, Features, Stories, Nonfunctional Requirements (NFRs), and more". The four-tier order is stated on /story: "four tiers of work items ... Epic, Capability, Feature, and Story". |
| safe-requirements-model#2 | safe-requirements-model | NOT FOUND (not readable) | Only the opening paragraph is readable; login wall. |
| safe-requirements-model#3 | safe-requirements-model | NOT FOUND (not readable) | Same. /story says "Through acceptance criteria and tests, stories become more specific". |
| safe-requirements-model#4 | safe-requirements-model | NOT FOUND (not readable) | Same. Features "maintained in the ART Backlog" and stories in "backlogs of the Agile Teams" appear on /features-and-capabilities and /story. |
| safe-enablers#1 | safe-enablers | SUPPORTED | "backlog items that extend the architectural runway of the solution under development or improve the performance of the development value stream." |
| safe-enablers#2 | safe-enablers | SUPPORTED | "four categories: Exploration, Architecture, Infrastructure, Compliance". |
| safe-enablers#3 | safe-enablers | SUPPORTED | "managed in the appropriate backlog as epics, capabilities, features, or stories." |
| safe-pi-planning#1 | safe-pi-planning | SUPPORTED | "a cadence-based event for the entire ART that aligns teams and stakeholders to a shared mission and vision"; takeaways: "Agile Teams and stakeholders align as an Agile Release Train (ART) around a shared mission and plan". |
| safe-pi-planning#2 | safe-pi-planning | PARTLY | Page: "committed PI objectives from the Agile Teams and an ART planning board". "committed or uncommitted" is the glossary wording for PI Objectives ("either committed or uncommitted"). |
| safe-pi-planning#3 | safe-pi-planning | PARTLY | Page: board "reflects feature delivery dates and dependencies". "milestones" is in the glossary: "a visualization of the PI's feature delivery dates, feature dependencies among teams, and relevant milestones". |
| safe-pi-planning#4 | safe-pi-planning | SUPPORTED | Page uses "ART planning board"; "program board" does not occur on the page, glossary or Essential SAFe page. |
| safe-inspect-and-adapt#1 | safe-inspect-and-adapt | SUPPORTED | "a significant event held at the end of each PI". |
| safe-inspect-and-adapt#2 | safe-inspect-and-adapt | SUPPORTED | "structured into three parts: the PI System Demo, a quantitative and qualitative measurement review, and a retrospective and problem-solving workshop." |
| safe-inspect-and-adapt#3 | safe-inspect-and-adapt | SUPPORTED | "improvement backlog items that go into the ART Backlog for consideration in the next PI Planning event." |
| safe-inspect-and-adapt#4 | safe-inspect-and-adapt | PARTLY | Page says "a structured problem-solving workshop". "structured, root-cause problem-solving workshop to address the most significant systemic problems" is in the facilitator's guide PDF. |
| safe-ia-facilitators-guide#1 | safe-ia-facilitators-guide | PARTLY | Guide is 4 pages; Part 3 is "a brief retrospective, followed by a structured, root-cause problem-solving workshop"; names "Root Cause Analysis, Fishbone, 5 Whys, Pareto" and "Checkpoint One: Problem statement understood, causes identified". No six-step list (restate problem, brainstorm solutions) appears. |
| safe-ia-facilitators-guide#2 | safe-ia-facilitators-guide | SUPPORTED | "three primary parts, typically facilitated by the Release Train Engineer (RTE)." |
| safe-iteration-planning#1 | safe-iteration-planning | SUPPORTED | "The team collaboratively defines a set of Iteration Goals and selects the stories from the team backlog that they believe they can complete to meet those goals." |
| safe-iteration-planning#2 | safe-iteration-planning | PARTLY | This page: "the upcoming timebox, known as an iteration"; "fixed iteration timebox". Full definition is on /iterations/: "a standard, fixed-duration timebox". "giving teams cadence" wording: /essential-safe/ "Fixed-length timeboxes that provide the development cadence". |
| safe-iteration-review#1 | safe-iteration-review | PARTLY | Glossary-term page: "a regular SAFe Scrum event where the team inspects the iteration increment, assesses progress, and adjusts the team backlog." It does not say "shows results, gets feedback". /iteration-review/ does: "showcase their accomplishments, receive feedback, and collaboratively determine next steps". |
| safe-iteration-retrospective#1 | safe-iteration-retrospective | SUPPORTED | "held at the end of each iteration during which Agile Teams review their results to identify improvements for future work." |
| safe-team-backlog-refinement#1 | safe-team-backlog-refinement | PARTLY | "an event that helps Agile Teams clarify and prepare upcoming stories and features"; activities "removing outdated stories, discovering new ones, and defining acceptance criteria". Page does not say "continuously", nor "sized". |
| safe-rte#1 | safe-rte | SUPPORTED | "a servant leader and ART coach who facilitates ART events and processes, and supports teams in delivering value." |
| safe-system-architect#1 | safe-system-architect | SUPPORTED | "responsible for defining and communicating a shared technical and architectural vision for the solutions developed by an ART." |
| safe-system-architect#2 | safe-system-architect | SUPPORTED | Summary: "They do this by defining enablers, participating in solution definition, outlining non-functional requirements(NFRs)". |
| safe-built-in-quality#1 | safe-built-in-quality | SUPPORTED | "a set of practices to help ensure that the outputs of Agile teams in business and technology domains meet appropriate quality standards throughout the process of creating customer value." |
| safe-built-in-quality#2 | safe-built-in-quality | NOT FOUND (not readable) | Not in readable text. Glossary: "The Definition of Done specifies the requirements for completeness of a work product or increment of value." |
| safe-built-in-quality#3 | safe-built-in-quality | NOT FOUND (not readable) | Page says "five key domains" (not "dimensions"); names are behind the login wall. |
| safe-built-in-quality#4 | safe-built-in-quality | NOT FOUND (not readable) | Login wall. |
| safe-cdp#1 | safe-cdp | SUPPORTED | "the workflows, activities, and automation needed to guide new functionality from ideation to an on-demand release of value." |
| safe-cdp#2 | safe-cdp | SUPPORTED | "four aspects: continuous exploration (CE), continuous integration (CI), continuous deployment (CD), and release on demand (RoD)". |
| safe-continuous-exploration#1 | safe-continuous-exploration | SUPPORTED | "drives innovation and fosters alignment on what should be built by continually exploring the market and customer needs, defining a vision, roadmap, and set of features for a solution." |
| safe-continuous-integration#1 | safe-continuous-integration | SUPPORTED | "new functionality is developed, tested, integrated, and validated in preparation for deployment and release." |
| safe-continuous-deployment#1 | safe-continuous-deployment | SUPPORTED | "automates the migration of new functionality from a staging environment to production, where it is made available for release." |
| safe-continuous-deployment#2 | safe-continuous-deployment | SUPPORTED | "Deploy / Verify / Monitor / Respond", each with a one-line practice description on the page. |
| safe-continuous-deployment#3 | safe-continuous-deployment | SUPPORTED | "it's optimal to separate the deployment process from releasing". |
| safe-release-on-demand#1 | safe-release-on-demand | SUPPORTED | "releases new functionality immediately or incrementally based on business and customer needs." |
| safe-release-on-demand#2 | safe-release-on-demand | NOT FOUND (not readable) | Heading "What are the four activities of release on demand?" visible; the names are login-walled. |
| safe-release-on-demand#3 | safe-release-on-demand | SUPPORTED | "releases are decoupled from the work to deploy the functionality." |
| safe-glossary#1 | safe-glossary | SUPPORTED | "The System Demo provides stakeholders an integrated view of new features for the most recent iteration delivered by all the teams on the ART." URL found: https://framework.scaledagile.com/system-demo/ |
| safe-glossary#2 | safe-glossary | SUPPORTED | "Iteration Goals are a high-level summary of the business and technical goals that an Agile Team agrees to accomplish in an Iteration." |
| safe-glossary#3 | safe-glossary | SUPPORTED | Entries "Lean Budgets" and "Definition of Done" exist. |
| safe-portfolio-flow#1 | safe-portfolio-flow | PARTLY | Page defines Portfolio Flow as "a state where Lean Portfolio Management provides a continuous flow of new epics to Solution Trains and ARTs"; it does not say it describes "the portfolio Kanban system matching demand to capacity" in readable text (login wall after the first flow accelerator heading). |
| safe-essential#1 | safe-essential | SUPPORTED | Lists ART roles including "Release Train Engineer (RTE) - a servant leader and the chief Scrum Master/Team Coach for the train" and ART/team events. Page is a legacy article, "Last update: 30 November 2022". |
| safe-whats-new#1 | safe-whats-new | PARTLY | Calls AI-Native SAFe "the reinvented operating model designed to help enterprises thrive in the Age of AI" and refers to "Core and AI-Native SAFe". The "alongside Core SAFe" statement is on the home page and the 23 June post. |
| safe-whats-new#2 | safe-whats-new | NOT FOUND | "fully supported" does not occur. Closest: June 23 post, "our commitment to continue supporting and evolving the Core SAFe operating model" and "This release does not replace Core SAFe". |
| safe-whats-new#3 | safe-whats-new | NOT FOUND | No date printed for the release; page says "In June, we officially introduced AI-Native SAFe". 23 June 2026 is the date of the announcement post; that post says "June 16th" was the unveiling; the 6 Oct post calls 15 Sept 2026 "the official release". |
| safe-whats-new#4 | safe-whats-new | NOT FOUND | No Core SAFe version number or release date on the page ("6.0" and "March 2023" absent). "SAFe 6.0" appears only on /safe-6-0-configurations and the home page link text. |
| safe-ai-native-sense-and-respond#1 | safe-ai-native-sense-and-respond | SUPPORTED | "a two-hour cadenced event"; "These events occur at the boundary of every iteration". |
| safe-ai-native-sense-and-respond#2 | safe-ai-native-sense-and-respond | SUPPORTED | "The half-day Inspect and Adapt event ... has been replaced by a two-hour Sense and Respond event every iteration ... also includes the activities formally present in the System Demo." Note "NOTE: Some ARTs may choose to run the problem-solving portion of the Core SAFe Inspect and Adapt event periodically". |
| oasis-soa-rm#1 | oasis-soa-rm | SUPPORTED | "A reference model is an abstract framework for understanding significant relationships among the entities of some environment." (1.1); abstract: "significant entities and relationships between them within a service-oriented environment". |
| oasis-soa-rm#2 | oasis-soa-rm | SUPPORTED | "OASIS Standard, 12 October 2006". |
| dora-ai-capabilities#1 | dora-ai-capabilities | PARTLY | Page says "the seven capabilities that amplify the benefits of AI" but names none of them. Names and order are SUPPORTED on the intro blog (same seven, same order as in the claim). |
| dora-ai-capabilities#2 | dora-ai-capabilities | NOT FOUND | Not on this page. The intro blog says "Connecting AI tools to internal data sources boosts their impact on individual effectiveness and code quality." |
| dora-ai-capabilities-intro#1 | dora-ai-capabilities-intro | SUPPORTED | Seven listed in order: Clear and communicated AI stance; Healthy data ecosystems; AI-accessible internal data; Strong version control practices; Working in small batches; User-centric focus; Quality internal platforms. |
| dora-ai-capabilities-intro#2 | dora-ai-capabilities-intro | SUPPORTED | "Working in small batches, a long-standing DORA principle, is especially powerful in an AI-assisted environment." |
| dora-ai-capabilities-intro#3 | dora-ai-capabilities-intro | SUPPORTED | "in the absence of a user-centric focus, AI adoption can have a negative impact on team performance." |
| dora-ai-capabilities-intro#4 | dora-ai-capabilities-intro | SUPPORTED | Date "September 23, 2025"; bylines Kevin M. Storer (Ph.D., Researcher) and Derek DeBellis (Researcher). |
| dora-ai-capabilities-impact#1 | dora-ai-capabilities-impact | SUPPORTED | "AI can easily generate massive blocks of code, which are hard to review and test." |
| dora-ai-capabilities-impact#2 | dora-ai-capabilities-impact | SUPPORTED | Small batches: "ensuring that speed translates to product performance rather than instability"; version control "becomes your critical safety net ... essential for maintaining stability". |
| dora-ai-capabilities-impact#3 | dora-ai-capabilities-impact | SUPPORTED | Date "December 10, 2025"; bylines Nathen Harvey (DORA Lead) and Allison Park (Senior Product Marketing Manager). |
| dora-small-batches#1 | dora-small-batches | SUPPORTED | "try to break them down into work units that can be completed independently and in short timeframes." |
| dora-small-batches#2 | dora-small-batches | SUPPORTED | "working in small batches amplifies the positive impact of AI adoption on product performance". |
| dora-small-batches#3 | dora-small-batches | SUPPORTED | "large changes are difficult to review, test, and integrate safely." |
| dora-wip-limits#1 | dora-wip-limits | SUPPORTED | Instead: "Prioritize work / Limit how much people work on / Focus on completing a small number of high-priority tasks". |
| dora-wip-limits#2 | dora-wip-limits | SUPPORTED | "research shows that WIP limits help drive improvements in software delivery performance, particularly when they are combined with ... visual displays and feedback loops from monitoring." |
| dora-2024-highlights#1 | dora-2024-highlights | SUPPORTED | "AI adoption may negatively impact software delivery performance"; refers to "small batch sizes and robust testing mechanisms". Page gives estimates (see Part E); it names both throughput and stability. |
| dora-2024-highlights#2 | dora-2024-highlights | SUPPORTED | H1 "Highlights from the 10th DORA report"; "October 22, 2024"; Nathen Harvey (DORA Lead), Derek DeBellis (Researcher). Tab title is "Announcing the 2024 DORA report". |
| dora-2024-report#1 | dora-2024-report | PARTLY | "it also negatively impacts software delivery stability and throughput, reminding teams that fundamentals like small batch sizes and robust testing remain crucial." Page does not say larger batch sizes are suggested as the cause. |
| dora-2025-report#1 | dora-2025-report | PARTLY | Supports "AI's primary role is as an amplifier, magnifying an organization's existing strengths and weaknesses." Says nothing on throughput or instability. The announcement blog supplies those. |
| dora-2025-announcement#1 | dora-2025-announcement | SUPPORTED | "Without robust control systems, like strong automated testing, mature version control practices, and fast feedback loops, an increase in change volume leads to instability." |
| dora-2025-announcement#2 | dora-2025-announcement | PARTLY | "AI adoption does continue to have a negative relationship with software delivery stability." The page also says "Unlike last year, we observe a positive relationship between AI adoption on both software delivery throughput and product performance." |
| dora-2025-announcement#3 | dora-2025-announcement | SUPPORTED | "AI doesn't fix a team; it amplifies what's already there." |
| dora-metrics#1 | dora-metrics | NOT FOUND | https://dora.dev/research/ page text names no metrics (the diagram is interactive; its text is not in a plain GET). Read instead at https://dora.dev/guides/dora-metrics/: names "Change fail rate" and "Failed deployment recovery time"; throughput group = change lead time, deployment frequency, failed deployment recovery time; instability group = change fail rate, deployment rework rate. So failed deployment recovery time is in the throughput group. |
| dora-customer-feedback#1 | dora-customer-feedback | PARTLY | Customer feedback is "part of a wider group of capabilities" (with visibility of work, small batches, team experimentation) that "together" "help predict" software delivery performance and organizational performance. Not stated of customer feedback alone. |
| dora-test-automation#1 | dora-test-automation | SUPPORTED | "Developers should be able to get feedback from automated tests in less than ten minutes both on local workstations and from the continuous integration system." |
| dora-monitoring-observability#1 | dora-monitoring-observability | SUPPORTED | "Monitoring is tooling or a technical solution that allows teams to watch and understand the state of their systems"; "Observability ... allows teams to actively debug their system." |
| dora-monitoring-observability#2 | dora-monitoring-observability | SUPPORTED | "a comprehensive monitoring and observability solution, along with a number of other technical practices, positively contributes to continuous delivery." |
| dora-streamlining-change-approval#1 | dora-streamlining-change-approval | SUPPORTED | "change approvals are best implemented through peer review during the development process, supplemented by automation to detect, prevent, and correct bad changes early". |
| dora-streamlining-change-approval#2 | dora-streamlining-change-approval | SUPPORTED | Catalog card: "Replace heavyweight change-approval processes with peer review"; page: heavyweight external approval "have a negative impact on software delivery performance". |
| dora-streamlining-change-approval#3 | dora-streamlining-change-approval | PARTLY | Page does discuss regulation: "One common regulatory requirement is segregation of duties" and says peer review can meet it; the CAB keeps a "strategic" role. It does not address organisations whose external control mandates approval by an outside body; no statement either way. |
| dora-continuous-delivery#1 | dora-continuous-delivery | SUPPORTED | "release software and make changes to production in a low-risk way at any time--including during normal business hours--without impacting users." Defined as "the ability to release changes of all kinds on demand quickly, safely, and sustainably." |
| scrum-guide-2020#1 | scrum-guide-2020 | SUPPORTED | "The Definition of Done is a formal description of the state of the Increment when it meets the quality measures required for the product." |
| scrum-guide-2020#2 | scrum-guide-2020 | SUPPORTED | "The moment a Product Backlog item meets the Definition of Done, an Increment is born." |
| scrum-guide-2020#3 | scrum-guide-2020 | SUPPORTED | "If a Product Backlog item does not meet the Definition of Done, it cannot be released or even presented at the Sprint Review." |
| scrum-guide-2020#4 | scrum-guide-2020 | SUPPORTED | Organisational standard: "all Scrum Teams must follow it as a minimum"; otherwise "the Scrum Team must create a Definition of Done appropriate for the product"; multiple teams on one product "must mutually define and comply with the same Definition of Done." |
| scrum-guide-2020#5 | scrum-guide-2020 | SUPPORTED | Developers "always accountable for ... Instilling quality by adhering to a Definition of Done"; also "The Developers are required to conform to the Definition of Done." |
| scrum-guide-2020#6 | scrum-guide-2020 | SUPPORTED | Retrospective: the team inspects "individuals, interactions, processes, tools, and their Definition of Done." |
| scrum-guide-2020#7 | scrum-guide-2020 | SUPPORTED | "Each artifact contains a commitment": Product Backlog, Product Goal; Sprint Backlog, Sprint Goal; Increment, Definition of Done. |
| scrum-guide-2020#8 | scrum-guide-2020 | SUPPORTED | The string "Definition of Ready" does not occur. "Product Backlog items that can be Done by the Scrum Team within one Sprint are deemed ready for selection in a Sprint Planning event." |
| scrum-guide-2020#9 | scrum-guide-2020 | SUPPORTED | Refinement is "an ongoing activity to add details, such as a description, order, and size"; "The Developers who will be doing the work are responsible for the sizing." |
| scrum-guide-2020#10 | scrum-guide-2020 | SUPPORTED | Product Owner "accountable for effective Product Backlog management, which includes ... Creating and clearly communicating Product Backlog items; Ordering Product Backlog items". |
| scrum-guide-2020#11 | scrum-guide-2020 | SUPPORTED | "the empirical Scrum pillars of transparency, inspection, and adaptation"; "Inspection without adaptation is considered pointless." |
| scrum-guide-2020#12 | scrum-guide-2020 | SUPPORTED | "The purpose of the Sprint Retrospective is to plan ways to increase quality and effectiveness"; impactful improvements "may even be added to the Sprint Backlog for the next Sprint." |
| scrum-guide-2020#13 | scrum-guide-2020 | SUPPORTED | "an Increment may be delivered to stakeholders prior to the end of the Sprint. The Sprint Review should never be considered a gate to releasing value." |
| agile-alliance-dor#1 | agile-alliance-dor | PARTLY | Page: the team "makes explicit and visible the criteria (generally based on the INVEST matrix) that a user story must meet prior to being accepted into the upcoming iteration." Words "checklist" and any statement that DoR is not in the Scrum Guide are absent; Scrum Guide is not mentioned. |
| agile-alliance-dor#2 | agile-alliance-dor | SUPPORTED | "2008: while the first few allusions to teams using a 'definition of ready' date to the beginning of that year, the first formal description seems to be from October, and is incorporated into 'official' Scrum training material shortly thereafter". Page gives no author, date or source for this. |
| agile-alliance-dor#3 | agile-alliance-dor | PARTLY | Page: Scrum "appears to have all but reinvented previously existing concepts in process modeling, such as the ETVX framework first described in 1985"; "ETVX (for entry-task-validation-exit)" "anticipates Scrum's definitions of 'ready' and 'done'". Does not use the words "restates" or "entry and exit criteria". |
| agile-alliance-dod#1 | agile-alliance-dod | PARTLY | Page: "a list of criteria that must be met before a product increment ... is considered 'done'". The phrase "intrinsic quality standards" is absent. |
| agile-alliance-dod#2 | agile-alliance-dod | SUPPORTED | "Origins" list: 2002 (early article by Bill Wake), 2003 (early Scrum training materials, "The story of Done"), 2005, 2007. (2020 Scrum Guide says the first Guide was written in 2010.) |
| overeem-dor#1 | overeem-dor | NOT FOUND (not readable) | www.scrum.org returned HTTP 403; byline, date and content not seen. |
| kronfalt-ready-2008#1 | kronfalt-ready-2008 | NOT FOUND (not readable) | scrumftw.blogspot.com did not resolve (name resolution error); title, byline and date not seen. |
| kronfalt-ready-2008#2 | kronfalt-ready-2008 | NOT FOUND (not readable) | As above; criteria list not seen. |
| sutherland-ready-2009#1 | sutherland-ready-2009 | NOT FOUND (not readable) | jeffsutherland.com did not resolve; READY-state claim not seen. |
| sutherland-ready-2009#2 | sutherland-ready-2009 | NOT FOUND (not readable) | As above. |
| sutherland-ready-2009#3 | sutherland-ready-2009 | NOT FOUND (not readable) | As above; Jakobsen and Sutherland reference not seen. |
| radice-etvx-1985#1 | radice-etvx-1985 | NOT FOUND (not readable) | dl.acm.org HTTP 403. Only the title "A programming process architecture" and year 1985 are seen, second-hand, on the Agile Alliance DoR page (no authors, journal or issue). |
| radice-etvx-1985#2 | radice-etvx-1985 | NOT FOUND (not readable) | dl.acm.org HTTP 403. Agile Alliance page only says "ETVX (for entry-task-validation-exit)". |
| wake-invest#1 | wake-invest | SUPPORTED | "Posted on August 17, 2003 by Bill Wake"; "I – Independent, N – Negotiable, V – Valuable, E – Estimable, S – Small, T – Testable". |
| wake-invest#2 | wake-invest | SUPPORTED | "SMART Tasks": Specific, Measurable, Achievable, Relevant, Time-boxed. |
| agile-manifesto-principles#1 | agile-manifesto-principles | SUPPORTED | Twelfth of twelve unnumbered statements: "At regular intervals, the team reflects on how to become more effective, then tunes and adjusts its behavior accordingly." |
| schwaber-beedle-2001#1 | schwaber-beedle-2001 | NOT FOUND (not readable) | dl.acm.org HTTP 403. |
| schwaber-beedle-2001#2 | schwaber-beedle-2001 | NOT FOUND (not readable) | dl.acm.org HTTP 403. |
| schwaber-scrum-1995#1 | schwaber-scrum-1995 | NOT FOUND (not readable) | www.jeffsutherland.org did not resolve; title, byline, venue not seen. |
| schwaber-scrum-1995#2 | schwaber-scrum-1995 | NOT FOUND (not readable) | Not on this source. Separate evidence: 2020 Scrum Guide: "Ken Schwaber and Jeff Sutherland first co-presented Scrum at the OOPSLA Conference in 1995." |
| cooper-stage-gate#1 | cooper-stage-gate | NOT FOUND (not readable) | onlinelibrary.wiley.com HTTP 403. |
| cooper-stage-gate#2 | cooper-stage-gate | NOT FOUND (not readable) | onlinelibrary.wiley.com HTTP 403. |
| cooper-stage-gate#3 | cooper-stage-gate | NOT FOUND (not readable) | onlinelibrary.wiley.com HTTP 403. |
| keep-a-changelog#1 | keep-a-changelog | SUPPORTED | "Changelogs are for humans, not machines." (both /en/1.1.0/ and /en/2.0.0/). |
| keep-a-changelog#2 | keep-a-changelog | SUPPORTED | 1.1.0: "Don't let your friends dump git logs into changelogs." and "Using commit log diffs as changelogs is a bad idea". 2.0.0 retires the tagline but says "do not paste a git log". |
| keep-a-changelog#3 | keep-a-changelog | PARTLY | "There should be an entry for every single version." Six types of change: Added, Changed, Deprecated, Removed, Fixed, Security. SemVer is not recommended outright: 1.1.0 "Mention whether you follow Semantic Versioning"; 2.0.0 "You do not have to use Semantic Versioning." |
| keep-a-changelog#4 | keep-a-changelog | PARTLY | "created and maintained by Olivier Lacan" (SUPPORTED). No sentence says "first published 2014"; the page's own changelog dates 0.0.1 as 2014-05-31. |
| semver#1 | semver | SUPPORTED | "MAJOR version when you make incompatible API changes". |
| iso-12207#1 | iso-12207 | NOT FOUND (not readable) | iso.org/standard/63712.html and /90219.html both HTTP 403; no text read |
| iso-12207#2 | iso-12207 | NOT FOUND (not readable) | same: HTTP 403; April 2026 second edition and replacement of 2017 cannot be confirmed or refuted |
| iso-12207#3 | iso-12207 | NOT FOUND (not readable) | same: HTTP 403 |
| iso-14764#1 | iso-14764 | NOT FOUND (not readable) | iso.org/standard/80710.html HTTP 403 |
| iso-14764#2 | iso-14764 | NOT FOUND (not readable) | same: HTTP 403 |
| iso-14764#3 | iso-14764 | NOT FOUND (not readable) | same: HTTP 403 |
| iso-25010#1 | iso-25010 | NOT FOUND (not readable) | iso.org/standard/78176.html HTTP 403 |
| iso-29148#1 | iso-29148 | NOT FOUND (not readable) | iso.org/standard/72089.html HTTP 403 |
| iso-29148#2 | iso-29148 | NOT FOUND (not readable) | same: HTTP 403 |
| iso-29148#3 | iso-29148 | NOT FOUND (not readable) | same: HTTP 403 |
| iso-29148#4 | iso-29148 | NOT FOUND (not readable) | same: HTTP 403 |
| iso-24765#1 | iso-24765 | NOT FOUND (not readable) | iso.org/standard/71952.html HTTP 403 |
| iso-15288#1 | iso-15288 | NOT FOUND (not readable) | iso.org/standard/81702.html HTTP 403 |
| iso-42010#1 | iso-42010 | NOT FOUND (not readable) | iso.org/standard/74393.html HTTP 403 |
| iso-29119-1#1 | iso-29119-1 | NOT FOUND (not readable) | iso.org/standard/81291.html HTTP 403 |
| iso-29119-3#1 | iso-29119-3 | NOT FOUND (not readable) | iso.org/standard/79429.html HTTP 403 |
| iso-29119-3#2 | iso-29119-3 | NOT FOUND (not readable) | same: HTTP 403 |
| istqb-rbt#1 | istqb-rbt | SUPPORTED | "A test approach in which the management, selection, prioritization, and use of test activities and resources are based on corresponding risk types and risk levels." (version 3, via glossary API) |
| istqb-ctfl-4#1 | istqb-ctfl-4 | SUPPORTED | Syllabus v4.0.1 s2.2.1: "the following five test levels are described": component (unit), component integration, system, system integration, acceptance |
| istqb-ctfl-4#2 | istqb-ctfl-4 | SUPPORTED | Syllabus v4.0.1 s2.2.3: "Confirmation testing confirms that an original defect has been successfully fixed." "Regression testing confirms that no adverse consequences have been caused by a change" |
| istqb-stress-testing#1 | istqb-stress-testing | SUPPORTED | "A type of performance testing to evaluate a system or component at or beyond the limits of its anticipated or specified workloads, or with reduced availability of resources such as access to memory or servers." (version 1) |
| istqb-test-completion#1 | istqb-test-completion | SUPPORTED | "The activity that makes testware available for later use, leaves test environments in a satisfactory condition and communicates the results of testing to relevant stakeholders." (version 2) |
| istqb-test-completion#2 | istqb-test-completion | PARTLY | Not on the test-completion record. The exit-criteria wording is on a different glossary term, exit-criteria (version 2): "The set of conditions for officially completing a defined task." |
| istqb-testability#1 | istqb-testability | SUPPORTED | "The degree to which test conditions can be established for a component or system, and tests can be performed to determine whether those test conditions have been met." (version 3; wording differs slightly from the draft) |
| istqb-acceptance-criteria#1 | istqb-acceptance-criteria | NOT SUPPORTED | Current (version 3): "The criteria that a work product must satisfy to be accepted by the stakeholders." The drafted wording (exit criteria; component or system; user, customer or authorised entity) matches only the older versions 1 and 2 |
| istqb-agile-tester-2014#1 | istqb-agile-tester-2014 | SUPPORTED | "Each test level has its own definition of done." (Agile Tester syllabus Version 2014, section on definition of done, Test Levels) |
| istqb-agile-tester-2014#2 | istqb-agile-tester-2014 | SUPPORTED | Acceptance criteria are covered throughout (e.g. "An Agile team considers a task finished when a set of acceptance criteria have been satisfied"); INVEST listed: Independent, Negotiable, Valuable, Estimable, Small, Testable |
| nist-800-61r3#1 | nist-800-61r3 | SUPPORTED | CSRC H1 and PDF cover: "Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile" (PDF running header shortens it to "Cyber Risk Management") |
| nist-800-61r3#2 | nist-800-61r3 | SUPPORTED | "Date Published: April 2025"; document history "04/03/25: SP 800-61 Rev. 3 (Final)"; PDF cover "April 2025" |
| nist-800-61r3#3 | nist-800-61r3 | SUPPORTED | PDF: "All six NIST Cybersecurity Framework (CSF) 2.0 Functions play" a role; Fig. 2 "based on the six CSF 2.0 Functions" (Govern, Identify, Protect, Detect, Respond, Recover) |
| nist-800-61r3#4 | nist-800-61r3 | SUPPORTED | PDF: "the Improvement Category (ID.IM) within the Identify Function... Lessons learned from performing all activities in all Functions are fed into Improvement" |
| nist-800-61r3#5 | nist-800-61r3 | SUPPORTED | Rev. 3 page "Supersedes: SP 800-61 Rev. 2 (08/06/2012)"; PDF "This publication supersedes SP 800-61r2"; Rev. 2 page "Withdrawn on April 03, 2025. Superseded by SP 800-61 Rev. 3" |
| nist-ssdf#1 | nist-ssdf | SUPPORTED | "Date Published: February 2022"; authors "Murugiah Souppaya (NIST), Karen Scarfone (Scarfone Cybersecurity), Donna Dodson" (PDF: Dodson is a "Former NIST employee") |
| nist-ssdf#2 | nist-ssdf | SUPPORTED | All 15 identifiers exist in v1.1 PDF with matching content: PO.1.2 "Identify and document all security requirements for organization-developed software to meet, and maintain the requirements over time"; PW.1.1 "Use forms of risk modeling – such as threat modeling, attack modeling, or attack surface mapping"; PW.2.1 "qualified person (or people) who were not involved with the design and/or automated processes... review the software design"; PW.6.1 compiler/interpreter/build tools with security features; PW.7.1 decide code review and/or analysis; PW.7.2 perform them per secure coding standards, record and triage issues; PW.8.1 decide on executable code testing; PW.8.2 scope, design, perform, document tests; PS.1.1 store all forms of code on least privilege; PS.3.1 securely archive release files; PS.3.2 collect, safeguard, maintain, share provenance data; PO.3.3 configure tools to generate artifacts; RV.1 "Identify and Confirm Vulnerabilities on an Ongoing Basis", RV.2 "Assess, Prioritize, and Remediate Vulnerabilities", RV.3 "Analyze Vulnerabilities to Identify Their Root Causes" (RV.1 to RV.3 are practices, with tasks RV.x.y) |
| nist-ssdf#3 | nist-ssdf | SUPPORTED | Rev. 1 page: "(Initial Public Draft)", "Date Published: December 17, 2025", "Comments Due: January 30, 2026 (public comment period is CLOSED)"; no final Rev. 1 page found (r1/final HTTP 404); v1.1 page still labelled final. See Part D Q14 |
| nist-ir-8397#1 | nist-ir-8397 | SUPPORTED | "Date Published: October 2021"; abstract: "Executive Order (EO) 14028... directs NIST to recommend minimum standards for software testing within 60 days"; PDF: "This document is a response to the 12 May 2021 Executive Order (EO) 14028" |
| nist-ir-8397#2 | nist-ir-8397 | SUPPORTED | Abstract lists eleven techniques in this order: threat modeling; automated testing; static code scanning; heuristic tools for hardcoded secrets; built-in checks and protections; "Black box" test cases; code-based structural test cases; historical test cases; fuzzing; web app scanners; address included code. PDF sections 2.1 to 2.11 follow the same order |
| nist-ir-8397#3 | nist-ir-8397 | SUPPORTED | "The document does not address the totality of software verification, but instead recommends techniques that are broadly applicable and form the minimum standards." |
| nist-800-53b#1 | nist-800-53b | SUPPORTED | Abstract: "three security control baselines (one for each system impact level—low-impact, moderate-impact, and high-impact), as well as a privacy baseline"; "Date Published: September 2020 (includes updates as of Dec. 10, 2020)" |
| nist-800-53#1 | nist-800-53 | SUPPORTED | PDF: control "AC-5 SEPARATION OF DUTIES" and "AC-6 LEAST PRIVILEGE" ("Employ the principle of least privilege, allowing only authorized accesses...") |
| nasa-swe-052#1 | nasa-swe-052 | SUPPORTED | NPR 7150.2D 3.12.1 table: "The project manager shall perform, record, and maintain bi-directional traceability between" higher-level requirements and software requirements; requirements and system hazards; requirements and design components; design components and code; requirements and "software verification(s)"; requirements and "software non-conformances". Applies by class (A, B, C; D; F per the table), not to all classes equally |
| nasa-swe-052#2 | nasa-swe-052 | SUPPORTED | "Traceability is important because it can point out software requirements that are not tested (i.e., missing tests) and tests that do not serve to test requirements (i.e., extra tests)." |
| nasa-swe-052#3 | nasa-swe-052 | SUPPORTED | "The matrix is completed left to right early in the appropriate phase in the project life cycle. As each column is completed, the forward trace is extended to the next set of products."; "Keep the matrix maintained throughout the life of the project." |
| tw-radar-decoupling#1 | tw-radar-decoupling | PARTLY | Apr 2016 entry only: "We recommend strictly using the term Deployment when referring to the act of deploying a change to application components or infrastructure. The term Release should be used when a feature change is released to end users, with a business impact." The Nov 2015 entry has no text on the page |
| tw-radar-decoupling#2 | tw-radar-decoupling | SUPPORTED | "Using techniques such as feature toggles and dark launches, we can deploy changes to production systems more frequently without releasing features." (Apr 2016 text) |
| tw-radar-decoupling#3 | tw-radar-decoupling | SUPPORTED | Timeline: "Apr 2016 Adopt", "Nov 2015 Adopt"; "Published : Nov 10, 2015"; "Last updated : Apr 05, 2016". No credit to any person or source anywhere on the page |
| fowler-deployment-pipeline#1 | fowler-deployment-pipeline | SUPPORTED | "breaking up your build into stages. Each stage provides increasing confidence, usually at the cost of extra time." |
| fowler-deployment-pipeline#2 | fowler-deployment-pipeline | SUPPORTED | Date printed: "30 May 2013", Martin Fowler |
| fowler-blue-green#1 | fowler-blue-green | SUPPORTED | "two production environments, as identical as possible. At any time one of them... is live"; "you switch the router"; rollback: "you switch the router back" |
| fowler-blue-green#2 | fowler-blue-green | SUPPORTED | "Databases can often be a challenge... The trick is to separate the deployment of schema changes from application upgrades." Date printed "1 March 2010", Martin Fowler |
| fowler-canary-release#1 | fowler-canary-release | SUPPORTED | "slowly rolling out the change to a small subset of users before rolling it out to the entire infrastructure" |
| fowler-canary-release#2 | fowler-canary-release | SUPPORTED | "the rollback strategy is simply to reroute users back to the old version" |
| fowler-canary-release#3 | fowler-canary-release | SUPPORTED | Byline "Danilo Sato", date "25 June 2014" |
| fowler-dark-launching#1 | fowler-dark-launching | SUPPORTED | "taking a new or changed back-end behavior and calling it from existing users without the users being able to tell it's being called"; "29 April 2020", Martin Fowler |
| fowler-feature-toggles#1 | fowler-feature-toggles | SUPPORTED | Section headings Release Toggles, Experiment Toggles, Ops Toggles, Permissioning Toggles; lifespans differ ("Release Toggles are transitionary by nature"; "Most Ops Toggles will be relatively short-lived") |
| fowler-feature-toggles#2 | fowler-feature-toggles | SUPPORTED | "Release Toggles allow incomplete and un-tested codepaths to be shipped to production as latent code which may never be turned on." |
| fowler-feature-toggles#3 | fowler-feature-toggles | PARTLY | "Savvy teams view their Feature Toggles as inventory which comes with a carrying cost"; teams should be "proactive in removing feature flags that are no longer needed"; "a small number of long-lived 'Kill Switches'". The page does not say "remove after full rollout" in those words (Release Toggles "should generally not stick around much longer than a week or two") |
| fowler-feature-toggles#4 | fowler-feature-toggles | SUPPORTED | Byline "Pete Hodgson", date "09 October 2017"; revisions list shows the series began 19 January 2016 and the complete article was published 08 February 2016 |
| fowler-evodb#1 | fowler-evodb | SUPPORTED | "representing every change to the database as a database migration script which is version controlled together with application code changes"; automation by "Liquibase and Active Record Migrations" |
| fowler-evodb#2 | fowler-evodb | SUPPORTED | Bylines Pramod Sadalage and Martin Fowler; "May 2016"; revisions "May 2016: Complete rewrite", "January 2003: Original publication" |
| fowler-test-pyramid#1 | fowler-test-pyramid | SUPPORTED | "you should have many more low-level UnitTests than high level BroadStackTests running through a GUI"; "1 May 2012" |
| fowler-test-pyramid#2 | fowler-test-pyramid | SUPPORTED | "Most people know about the the Test Pyramid due to Mike Cohn, when he described it in his 2009 book Succeeding with Agile." |
| fowler-given-when-then#1 | fowler-given-when-then | SUPPORTED | "an approach developed by Daniel Terhorst-North and Chris Matts as part of Behavior-Driven Development (BDD)"; "21 August 2013" |
| fowler-ci#1 | fowler-ci | SUPPORTED | All four headings present with this exact wording (also "Automate the Build", "Test in a Clone of the Production Environment", "Everyone can see what's happening", "Automate Deployment") |
| fowler-selftesting#1 | fowler-selftesting | SUPPORTED | "invoke a single command that executes the tests - and you are confident that these tests will illuminate any bugs hiding in your code"; "1 May 2014" |
| bockeler-sdd#1 | bockeler-sdd | SUPPORTED | "Spec-first", "Spec-anchored", "Spec-as-source" defined; "15 October 2025", Birgitta Böckeler |
| bockeler-sdd#2 | bockeler-sdd | SUPPORTED | Sections on Kiro, Spec-kit and Tessl Framework; title "Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl" |
| humble-farley-cd#1 | humble-farley-cd | SUPPORTED | "By Jez Humble, David Farley"; "Published Jul 27, 2010 by Addison-Wesley Professional"; also "Copyright 2011", "Edition: 1st" |
| humble-farley-cd#2 | humble-farley-cd | SUPPORTED | Table of contents: "10 Deploying and Releasing Applications" (sample chapter 5 also cites 'Chapter 10, "Deploying and Releasing Applications."') |
| humble-farley-cd#3 | humble-farley-cd | PARTLY | TOC chapter 7 is titled "Commit Testing Stage", not "The Commit Stage". Chapter 7 text not readable. In sample chapter 5 the "Commit Stage" section says a pipeline instance "is created upon every check-in" and the stage "should ideally take less than five minutes". The phrase about processes "triggered the moment a change is introduced" was not found |
| humble-farley-cd#4 | humble-farley-cd | SUPPORTED | TOC: "8 Automated Acceptance Testing" (title only; chapter text not readable) |
| humble-farley-cd#5 | humble-farley-cd | SUPPORTED | Heading "Only Build Your Binaries Once" in the freely readable chapter 5 sample (page "Deployment Pipeline Practices"); it is in chapter 5, not a stated chapter of its own |
| humble-farley-cd#6 | humble-farley-cd | NOT FOUND (not readable) | Chapter 10 text is not freely available (only catalogue page, TOC, sample chapter 5). Sample chapter 5 uses "deployment" and "release" side by side but does not define a distinction: "the release process should be the same process you use to deploy to a testing environment" |
| sre-book-release-engineering#1 | sre-book-release-engineering | SUPPORTED | "If two people attempt to build the same product at the same revision number ... on different machines, we expect identical results"; "Our builds are hermetic ... depend on known versions of build tools, such as compilers, and dependencies, such as libraries." |
| sre-book-release-engineering#2 | sre-book-release-engineering | PARTLY | Chapter has no "incubation period" wording. It says a Sisyphus rollout "can roll out a new binary to successive clusters over a period of several hours"; for large services "starting in one cluster and expand exponentially until all clusters are updated"; a canary is "a few jobs in our production environment after the completion of system tests". |
| sre-book-release-engineering#3 | sre-book-release-engineering | SUPPORTED | "release engineers and SREs work together to develop strategies for canarying changes, pushing out new releases without interrupting services, and rolling back features that demonstrate problems." |
| sre-book-release-engineering#4 | sre-book-release-engineering | SUPPORTED | Section "Enforcement of Policies and Procedures": "Gated operations include" the six items listed in the claim (approving source code changes; specifying release actions; creating a new release; approving the initial integration proposal and subsequent cherry picks; deploying a new release; changes to build configuration). |
| sre-workbook-canarying#1 | sre-workbook-canarying | SUPPORTED | "We define canarying as a partial and time-limited deployment of a change in a service and its evaluation... The part of the service that receives the change is 'the canary,' and the remainder of the service is 'the control.'" |
| sre-book-monitoring#1 | sre-book-monitoring | SUPPORTED | "Your monitoring system should address two questions: what's broken, and why?" |
| sre-book-monitoring#2 | sre-book-monitoring | SUPPORTED | "The four golden signals of monitoring are latency, traffic, errors, and saturation." |
| sre-book-being-on-call#1 | sre-book-being-on-call | PARTLY | Page says the on-call engineer is "expected to triage the problem and work toward its resolution, possibly involving other team members and escalating as needed." The words "diagnose, mitigate, fix" are not used. |
| sre-book-being-on-call#2 | sre-book-being-on-call | SUPPORTED | "Many teams have both a primary and a secondary on-call rotation." |
| sre-book-managing-incidents#1 | sre-book-managing-incidents | PARTLY | "Google's incident management system is based on the Incident Command System." The chapter lists four roles: Incident Command (incident commander), Operational Work (Ops lead), Communication ("the public face of the incident response task force"; not titled "communications lead"), and Planning. The workbook chapter, not this one, names Incident Commander, Communications Lead and Operations Lead. |
| sre-book-managing-incidents#2 | sre-book-managing-incidents | SUPPORTED | "The operations team should be the only group modifying the system during an incident." |
| sre-workbook-incident-response#1 | sre-workbook-incident-response | SUPPORTED | Section "Incident Management at Google" describes the framework (ICS, roles IC/CL/OL); "Case Studies" gives four incidents; handoffs appear (IC "may either hand off their role"; case study 2: "Zara decided to hand over incident command"). |
| google-sre-postmortem#1 | google-sre-postmortem | SUPPORTED | "The Action Items section has little or no ownership for its entries. Actions items without clear owners are less likely to be resolved." |
| google-sre-postmortem#2 | google-sre-postmortem | SUPPORTED | "The value of a postmortem is proportional to the learning it creates." |
| google-agentic-sre#1 | google-agentic-sre | SUPPORTED | Agents "consolidate/summarize data" from incident communication surfaces; "creating handoff documents"; "Automatically create drafts of incident postmortems"; investigation agents use "observability data (logging, motoring, tracing)" and "in some cases to autonomously mitigate issues". |
| google-agentic-sre#2 | google-agentic-sre | SUPPORTED | "having consistent controls to prevent unwanted mutations of production state." |
| google-agentic-sre#3 | google-agentic-sre | SUPPORTED | "An agentic approach does not necessarily imply removing people from the process, specifically for higher-risk services and features." |
| google-agentic-sre#4 | google-agentic-sre | SUPPORTED | No figures or percentages appear; outcomes are stated only qualitatively ("faster issue resolution", "likely significant reduction in the number of alerts"). |
| google-agentic-sre#5 | google-agentic-sre | SUPPORTED | H1 "AI in SRE: Where and how Google is deploying agentic AI to improve operations"; "May 28, 2026"; "Stevan Malesevic, Distinguished Software Engineer; Christopher Heiser, Distinguished Site Reliability Engineer". Tab title is the slug-style "How Google SRE is using agentic AI to improve operations \| Google Cloud Blog". |
| google-eng-practices-review#1 | google-eng-practices-review | SUPPORTED | First line: "# What to look for in a code review". |
| google-eng-practices-review#2 | google-eng-practices-review | SUPPORTED | Headings in order: Design, Functionality, Complexity, Tests, Naming, Comments, Style, Consistency, Documentation (then Every Line, Context, Good Things, Summary). |
| google-eng-practices-review#3 | google-eng-practices-review | SUPPORTED | "Ask for unit, integration, or end-to-end tests as appropriate for the change." (line break after "end-to-end" in source). |
| google-eng-practices-small-cls#1 | google-eng-practices-small-cls | SUPPORTED | First line: "# Small CLs". |
| google-eng-practices-small-cls#2 | google-eng-practices-small-cls | SUPPORTED | "Reviewed more quickly"; "Reviewed more thoroughly"; "Less likely to introduce bugs"; "Simpler to roll back" (all in the list "Small, simple CLs are:"). |
| google-eng-practices-small-cls#3 | google-eng-practices-small-cls | SUPPORTED | "The CL makes a minimal change that addresses just one thing." and "The CL should include related test code." |
| petrovic-mutation#1 | petrovic-mutation | NOT FOUND (not readable) | dl.acm.org returned HTTP 403 to a plain GET; title, authors, venue and DOI not read. |
| petrovic-mutation#2 | petrovic-mutation | NOT FOUND (not readable) | Same: HTTP 403; claim about diff-based mutation analysis during code review not checked. |
| owasp-asvs#1 | owasp-asvs | SUPPORTED | "an organization should analyze its risks and decide what level it believes it should be at"; L1 "contains the minimum requirements"; L2 "Most applications should be striving to achieve this level"; L3 "for applications looking to demonstrate the highest levels of security". |
| owasp-asvs#2 | owasp-asvs | SUPPORTED | "around 350 requirements which are divided into 17 chapters, each of which is further divided into sections"; identifier format chapter.section.requirement, "each element is a number. For example, 1.11.3". (Helper output stripped the angle-bracket placeholders; the text describes `<chapter>`, `<section>`, `<requirement>`.) |
| owasp-asvs#3 | owasp-asvs | SUPPORTED | "organizations are strongly encouraged to create an organization- or domain-specific fork ... provided that it maintains traceability so that passing requirement 4.1.1 means the same across all versions." |
| owasp-asvs#4 | owasp-asvs | SUPPORTED | "it is preferable for other documents, reports, or tools to use the following format: v<version>-<chapter>.<section>.<requirement>"; "writers or developers should include the version element." |
| owasp-wstg#1 | owasp-wstg | PARTLY | README: "comprehensive guide to testing the security of web applications and web services. Created by the collaborative efforts of security professionals and dedicated volunteers". The word "vendor-neutral" does not appear in the README or in document/1-About/README.md. |
| owasp-wstg#2 | owasp-wstg | SUPPORTED | "Each scenario has an identifier in the format WSTG-<category>-<number>" ('category' a 4-character upper-case string; number zero-padded 01 to 99; example WSTG-INFO-02). |
| owasp-wstg#3 | owasp-wstg | SUPPORTED | "We are currently working on release version 5.0." and "For the last stable release, check release 4.2." (README on the master branch; see Part D for limits). |
| owasp-secrets-management#1 | owasp-secrets-management | SUPPORTED | "organizations [need] to centralize the storage, provisioning, auditing, rotation and management of secrets". |
| owasp-secrets-management#2 | owasp-secrets-management | SUPPORTED | "the Least Privilege principle should be applied" (2.3); 2.6 Auditing lists "Who requested a secret and for what system and role." and "When the secret was used and by whom/what." |
| owasp-threat-modeling-cs#1 | owasp-threat-modeling-cs | SUPPORTED | "this cheatsheet will break the threat modeling down into four basic steps: application decomposition, threat identification and ranking, mitigations, and review and validation." |
| itil4-deployment-management#1 | itil4-deployment-management | PARTLY | Wording matches the course blurb: "Learn how to move new or changed hardware, software, documentation, processes, or any other component to live environments, and how to deploy components to other environments for testing or staging." It is a certification page description, not a practice-guide purpose statement; the page only says "Understand the purpose and key concepts of Deployment Management" without stating it. |
| itil4-release-management#1 | itil4-release-management | PARTLY | Blurb: "Learn best practices for making new and changed services available for use, in line with your organisation's policies and any agreements between the organisation and its service consumers." Certification description, not a purpose statement from the ITIL guide. |
| itil4-release-management#2 | itil4-release-management | PARTLY | PeopleCert lists "ITIL 4 Practitioner: Release Management" and "ITIL 4 Practitioner: Deployment Management" as separate certification pages (separate module). Neither page says the two are separate ITIL practices; the release page mentions "planning, scheduling, and controlling the build, test, and deployment of releases". |
| twelve-factor-config#1 | twelve-factor-config | SUPPORTED | "requires strict separation of config from code." |
| twelve-factor-config#2 | twelve-factor-config | SUPPORTED | "Config varies substantially across deploys, code does not." |
| twelve-factor-config#3 | twelve-factor-config | SUPPORTED | Lists "Resource handles to the database, Memcached, and other backing services"; "Credentials to external services such as Amazon S3 or Twitter"; "Per-deploy values such as the canonical hostname for the deploy". |
| twelve-factor-config#4 | twelve-factor-config | SUPPORTED | Heading "Store config in the environment"; "The twelve-factor app stores config in environment variables". |
| twelve-factor-config#5 | twelve-factor-config | SUPPORTED | Footer: "Written by Adam Wiggins - Last updated 2017". |
| twelve-factor-parity#1 | twelve-factor-parity | SUPPORTED | Heading "Keep development, staging, and production as similar as possible". |
| threat-modeling-manifesto#1 | threat-modeling-manifesto | SUPPORTED | "when we threat model, we ask four key questions: What are we working on? What can go wrong? What are we going to do about it? Did we do a good enough job?" (same in the linked PDF). Note: the page says the working group asks these; "adopts" is the draft's word. |
| sei-atam#1 | sei-atam | SUPPORTED | 1998 report abstract: "the Architecture Tradeoff Analysis Method (ATAM), a structured technique for understanding the tradeoffs inherent in the architectures of software-intensive systems." (CMU/SEI-98-TR-008). The 2000 report abstract instead says "a technique for analyzing software architectures". |
| sei-atam#2 | sei-atam | PARTLY | At the drafted URL (1998 report): scenarios are elicited ("Eliciting system usage scenarios") and each quality attribute is "evaluated in turn", but prioritising scenarios is not described. The 2000 report (CMU/SEI-2000-TR-004) does: "Brainstorm and prioritize scenarios ... prioritized via a voting process", and utility trees give "a prioritized list of scenarios". |
| slsa-build-track-basics#1 | slsa-build-track-basics | SUPPORTED | Table: L1 "Provenance showing how the package was built"; L2 "Signed provenance, generated by a hosted build platform"; L3 "Hardened build platform". |
| slsa-build-track-basics#2 | slsa-build-track-basics | PARTLY | Page shows "SLSA v1.2" and "Status: Approved"; no release date or "2025-11" is printed on this page, the v1.2 index or the what's-new page. |
| slsa-provenance#1 | slsa-provenance | SUPPORTED | "verifiable information about software artifacts describing where, when, and how something was produced." |
| spec-kit-sdd#1 | spec-kit-sdd | SUPPORTED | "Both templates mandate the use of [NEEDS CLARIFICATION] markers"; "Don't guess: If the prompt doesn't specify something, mark it". (Read from raw.githubusercontent.com, same file.) |
| spec-kit-sdd#2 | spec-kit-sdd | SUPPORTED | "The templates include comprehensive checklists that act as \"unit tests\" for the specification". |
| spec-kit-sdd#3 | spec-kit-sdd | SUPPORTED | Constitution of principles; Simplicity Gate (Article VII) and Anti-Abstraction Gate (Article VIII); "The LLM cannot proceed without either passing the gates or documenting justified exceptions in the 'Complexity Tracking' section." |
| spec-kit#1 | spec-kit | PARTLY | README flow lists constitution, specify, plan, tasks, implement, converge (written /speckit-...). The README does not say converge "validates implementation against specification" or call clarify/checklist/analyze optional; the docs reference page does: converge "Assess implementation against the artifacts and append remaining work"; clarify, analyze, checklist each "(optional quality gate)". |
| metr-reward-hacking#1 | metr-reward-hacking | SUPPORTED | Dated "June 5, 2025": "attempting (often successfully) to get a higher score by modifying the tests or scoring code, gaining access to an existing implementation or answer ... or exploiting other loopholes in the task environment." |
| metr-reward-hacking#2 | metr-reward-hacking | PARTLY | The examples are on METR's own evaluation tasks ("on our tasks"). The post also reports o3 reward hacked 14 of 20 attempts when the task was presented as research "with real-world consequences" and discusses implications; it does not study production teams. |
| anthropic-claude-37-system-card#1 | anthropic-claude-37-system-card | SUPPORTED | Section 6: "occasionally resorts to special-casing in order to pass test cases in agentic coding environments like Claude Code. Most often ... directly returning expected test values ... but also includes modifying the problematic tests themselves". |
| konstantinou-test-oracles#1 | konstantinou-test-oracles | SUPPORTED | "LLM-based test generation approaches mainly capture the actual program behavior making bug detection difficult." |
| konstantinou-test-oracles#2 | konstantinou-test-oracles | PARTLY | "test cases and oracles written by developers and automatically generated for 24 Java repositories"; abstract does not say "open-source". |
| konstantinou-test-oracles#3 | konstantinou-test-oracles | SUPPORTED | Authors: Michael Konstantinou, Renzo Degiovanni, Mike Papadakis. No venue printed. |
| pearce-copilot#1 | pearce-copilot | NOT FOUND (not readable) | doi.org redirects to ieeexplore.ieee.org/document/9833571/, which returned an empty HTTP 202 response. SUBSTITUTE arXiv 2108.09293 (same title, five authors as drafted) says Copilot produced programs in 89 scenarios and "approximately 40% to be vulnerable"; the S&P 2022 venue is not on that page. Do not carry the percentage. |
| perry-2023#1 | perry-2023 | NOT FOUND (not readable) | doi.org/ACM returned HTTP 403. SUBSTITUTE arXiv 2211.03622 supports the claim: "wrote significantly less secure code than those without access" and "more likely to believe they wrote secure code". |
| ahmed-incident-llm#1 | ahmed-incident-llm | PARTLY | Publication page: "ICSE 2023 | May 2023"; "first large-scale study ... more than 40,000 incidents". Page does not say "offline" or "one cloud provider" (it says "cloud services" and "incident owners"). |
| chen-rcacopilot#1 | chen-rcacopilot | PARTLY | Abstract supports routing ("matches incoming incidents to corresponding incident handlers"), diagnostics, root-cause category and explanatory narrative, "accuracy up to 0.766", and "a year's worth of incidents from Microsoft". The venue EuroSys '24 is not printed on the page. |
| requirements-ambiguity-llm#1 | requirements-ambiguity-llm | SUPPORTED | Abstract: "empirically investigates LLMs for ambiguity detection and explanation in real-world industrial requirements by adopting an in-context learning paradigm"; ten-shot beats zero-shot at classifying ambiguous requirements. |
| gotel-finkelstein-1994#1 | gotel-finkelstein-1994 | SUPPORTED | UCL Discovery: Gotel, O.; Finkelstein, A.; (1994) "An analysis of the requirements traceability problem", Proceedings of 1st International Conference on Requirements Engineering, pp. 94-101, IEEE Computer Society Press. (Page says "1st International Conference on Requirements Engineering"; the acronym ICRE is not printed.) |
| gotel-finkelstein-1994#2 | gotel-finkelstein-1994 | SUPPORTED | Paper: "Requirements traceability refers to the ability to describe and follow the life of a requirement, in both a forwards and backwards direction (i.e., from its origins, through its development and specification, to its subsequent deployment and use ...)". |
| rath-traceability-wild-2018#1 | rath-traceability-wild-2018 | PARTLY | ACM page not readable (HTTP 403). SUBSTITUTE author preprint (arXiv 1804.02433) prints the title, five authors, and "ICSE'18: 40th International Conference on Software Engineering, Gothenburg, Sweden, May 27-June 3, 2018" with DOI https://doi.org/10.1145/3180155.3180207. |
| rath-traceability-wild-2018#2 | rath-traceability-wild-2018 | PARTLY | SUBSTITUTE preprint abstract: "our analysis of six open source projects showed that on average only 60% of the commits were linked to specific issues ... Without these fundamental links the entire set of project-wide links will be incomplete"; it addresses missing commit-issue links. |
| reinertsen-flow-2009#1 | reinertsen-flow-2009 | PARTLY | Goodreads (retail record) prints the title, "Donald G. Reinertsen", "294 pages, Hardcover", "First published May 1, 2009". Publisher "Celeritas Publishing" is not in the readable page text. |
| reinertsen-flow-2009#2 | reinertsen-flow-2009 | NOT FOUND (not readable) | Book text not readable. The Goodreads page text contains neither "cost of delay" nor "weighted shortest job first". Not checkable. |
| reinertsen-flow-2009#3 | reinertsen-flow-2009 | NOT FOUND (not readable) | Book text not readable; quotation not checkable. |
| reinertsen-flow-2009#4 | reinertsen-flow-2009 | NOT FOUND (not readable) | Book text not readable. Goodreads blurb mentions queues and "invisible and unmanaged queues", not batch size; batch size appears only in one reader review ("WIP controls and batch size"). Not checkable. |

## C. SAFe allow-list

| # | term | verdict | resolved URL | version label shown | last-updated date shown | what the page says (short exact quote) |
|---|---|---|---|---|---|---|
| 1 | Portfolio | SUPPORTED | https://framework.scaledagile.com/portfolio (title "Portfolio - Scaled Agile Framework", H1 "Portfolio") | none on page | 8 April 2025 | "A SAFe Portfolio is a set of value streams that delivers a continuous flow of valuable solutions to customers within a common funding and governance model." |
| 2 | Agile Release Train (ART) | SUPPORTED | https://framework.scaledagile.com/agile-release-train (H1 "Agile Release Train") | none | not shown | "The Agile Release Train (ART) is a long-lived team of Agile teams that incrementally develops, delivers, and often operates one or more solutions in a development value stream." |
| 3 | Agile Team | SUPPORTED | https://framework.scaledagile.com/agile-teams (H1 "Agile Teams") | none | not shown | "An Agile Team is a cross-functional group of typically ten or fewer individuals with all the skills necessary to define, build, test, and deliver value to their customer." |
| 4 | Large Solution SAFe | SUPPORTED | https://framework.scaledagile.com/large-solution (tab title "Extended Guidance - Large Solution SAFe", H1 "Large Solution SAFe") | none | 5 December 2022 | "Large Solution SAFe is for enterprises building large and complex solutions that do not require portfolio concerns." |
| 5 | Solution Train | SUPPORTED | https://framework.scaledagile.com/solution-train (tab title "Extended Guidance - Solution Train") | none | not shown | "The Solution Train is the organizational construct used to build large solutions that requires the coordination of multiple ARTs and suppliers." (only intro readable; rest login-gated) |
| 6 | Planning Interval (PI) | SUPPORTED | https://framework.scaledagile.com/planning-interval (H1 "Planning Interval (PI)") | none | 25 February 2025 | "A Planning Interval (PI) is a cadence-based timebox in which Agile Release Trains deliver continuous value to customers in alignment with PI Objectives." and "a PI begins with a PI Planning event" |
| 7 | Value stream | SUPPORTED | https://framework.scaledagile.com/portfolio | none | 8 April 2025 | Term used in the Portfolio definition: "a set of value streams that delivers a continuous flow of valuable solutions". The page also says "development value streams". No separate definition on this page. |
| 8 | Lean Portfolio Management (LPM) | SUPPORTED | https://framework.scaledagile.com/lean-portfolio-management (tab "Lean Portfolio Management") | none | not shown | "Lean Portfolio Management (LPM) aligns strategy and execution by applying Lean and systems thinking approaches to strategy and investment funding, Agile portfolio operations, and governance." (the /portfolio page says "Lean governance"). Page also calls LPM "one of the seven core competencies" and says "we have evolved the way in which we think about competencies" and points to the LPM discipline article. |
| 9 | Strategic Themes | PARTLY | https://framework.scaledagile.com/strategic-themes/ | none | not shown | "Strategic themes are portfolio-level business objectives that provide competitive differentiation and strategic advantage." and "Strategic themes connect the enterprise strategy to a portfolio". Not found in readable text: "portfolio vision" as the thing connected, and "decision criteria for the portfolio backlog". Page says they "provide business context for portfolio strategy and decision-making". |
| 10 | Lean budgets | SUPPORTED (at /lean-budgets/ and glossary; listed URL only partly) | https://framework.scaledagile.com/lean-budgets/ (glossary entry links here); listed URL https://framework.scaledagile.com/lean-portfolio-management-discipline exists (tab "Lean Portfolio Management Discipline", H1 "Lean Portfolio Management") | none | /lean-budgets/ not shown; discipline page 31 March 2025 | "Lean Budgets is a financial governance approach that funds value streams instead of projects". Discipline page wording is looser: "Lean budgets provide funding for value streams aligned with the business strategy and current strategic themes." |
| 11 | Lean budget guardrails | SUPPORTED | https://framework.scaledagile.com/guardrails/ (tab "Extended Guidance - Lean Budget Guardrails") | none | not shown | "Lean Budget Guardrails describe the policies and practices for budgeting, spending, and governance for a specific portfolio." |
| 12 | Portfolio Backlog / portfolio Kanban | SUPPORTED | https://framework.scaledagile.com/portfolio-backlog/ | none | 11 March 2025 | "The Portfolio Backlog is a Kanban system that is used to capture and manage the business and enabler epics intended to create and evolve the portfolio's products, services, and solutions." |
| 13 | Epic | PARTLY (listed URL) / SUPPORTED-in-substance at /epic/ | https://framework.scaledagile.com/portfolio-backlog/ ; better: https://framework.scaledagile.com/epic/ | none | portfolio-backlog 11 March 2025; /epic/ 11 March 2025 | /epic/: "An Epic is a significant solution development initiative." and "Epics are significant initiatives". /portfolio-backlog/: "Portfolio epics are large (and typically cross-cutting initiatives) managed through the portfolio Kanban." The phrase "strategic initiatives the portfolio is responsible for" is not on either page. |
| 14 | Epic Owner | SUPPORTED | https://framework.scaledagile.com/epic-owner (tab "Extended Guidance - Epic Owners", H1 "Epic Owners") | none | not shown | "The Epic Owner is responsible for coordinating epics through the portfolio Kanban system." |
| 15 | WSJF (Weighted Shortest Job First) | SUPPORTED | https://framework.scaledagile.com/wsjf (tab "Extended Guidance - WSJF", H1 "Weighted Shortest Job First") | none | not shown | "In SAFe, WSJF is estimated as the relative cost of delay divided by the relative job duration." Reinertsen credited in the page epigraph: "—Don Reinertsen, The Principles of Product Development Flow [1]" ("If you only quantify one thing, quantify the Cost of Delay."). Components: "relative user and business value, time criticality, risk reduction and/or opportunity enablement, and job size". No sum-over-job-size formula in the readable text. |
| 16 | Cost of Delay | SUPPORTED | https://framework.scaledagile.com/blog/glossary_term/cost-of-delay (H1 "Cost of Delay") | none | not shown | "Cost of Delay (CoD) is the numerator in WSJF prioritization which represents the money or value that will be lost by delaying or not doing a job for a time period relative to other jobs." |
| 17 | Feature | SUPPORTED | https://framework.scaledagile.com/features-and-capabilities | none | 24 February 2025 | "A Feature represents solution functionality that delivers business value, fulfills a stakeholder need, and is sized to be delivered by an Agile Release Train within a PI." |
| 18 | Capability | SUPPORTED | https://framework.scaledagile.com/features-and-capabilities | none | 24 February 2025 | "A Capability represents large solution functionality whose implementation often spans multiple ARTs and is sized to be delivered within a PI." |
| 19 | Enabler | SUPPORTED | https://framework.scaledagile.com/enablers | none | 24 February 2025 | "Enablers are backlog items that extend the architectural runway of the solution under development or improve the performance of the development value stream." Categories: "Exploration", "Architecture", "Infrastructure", "Compliance" ("They generally fall into one of four categories"). |
| 20 | PI Planning | SUPPORTED | https://framework.scaledagile.com/pi-planning/ | none | 15 March 2026 | "PI Planning is a cadence-based event for the entire ART that aligns teams and stakeholders to a shared mission and vision." Outputs: "committed PI objectives from the Agile Teams and an ART planning board that reflects feature delivery dates and dependencies." |
| 21 | PI Objectives | SUPPORTED (at /pi-objectives/; listed URL only mentions "committed PI objectives") | https://framework.scaledagile.com/pi-objectives/ (H1 "PI Objectives | Details") | none | not shown | "PI Objectives summarize the business and technical goals that teams and trains intend to achieve in the upcoming PI and are either committed or uncommitted." |
| 22 | ART planning board | SUPPORTED | https://framework.scaledagile.com/pi-planning/ ; glossary https://framework.scaledagile.com/glossary/ | none | 15 March 2026 (PI Planning) | PI Planning page uses "ART planning board", never "program board". Glossary: "The ART Planning Board is a visualization of the PI's feature delivery dates, feature dependencies among teams, and relevant milestones." (/art-planning-board/ returns 404; the glossary entry has no link.) |
| 23 | System Demo | SUPPORTED | https://framework.scaledagile.com/system-demo/ (title "System Demo - Scaled Agile Framework"); linked from glossary entry | none | 18 March 2026 | "The System Demo provides stakeholders an integrated view of new features for the most recent iteration delivered by all the teams on the ART." |
| 24 | Inspect and Adapt (I&A) | SUPPORTED | https://framework.scaledagile.com/inspect-and-adapt | none | 20 March 2026 | "The Inspect and Adapt (I&A) is a significant event held at the end of each PI"; "structured into three parts: the PI System Demo, a quantitative and qualitative measurement review, and a retrospective and problem-solving workshop"; "a set of improvement backlog items that go into the ART Backlog for consideration in the next PI Planning event." |
| 25 | Problem-solving workshop | PARTLY | https://framework.scaledagile.com/blog/glossary_term/problem-solving-workshop ; also https://framework.scaledagile.com/inspect-and-adapt | none | glossary-term page not shown; I&A 20 March 2026 | Glossary-term page: "The Problem Solving Workshop is an Inspect and Adapt (I&A) event that provides a structured approach to identifying the root cause and actions to address systemic problems." "Most significant" (worklist wording) is not on either page. |
| 26 | ART backlog | SUPPORTED | https://framework.scaledagile.com/inspect-and-adapt ; definition at https://framework.scaledagile.com/art-and-solution-train-backlogs/ | none | I&A 20 March 2026 | I&A: "improvement backlog items that go into the ART Backlog for consideration in the next PI Planning event". Backlog page: "The ART backlog is a Kanban system used to capture and manage the features and enablers that enhance the solution and extend its Architectural Runway." |
| 27 | Release Train Engineer (RTE) | SUPPORTED | https://framework.scaledagile.com/release-train-engineer | none | not shown | "The Release Train Engineer (RTE) is a servant leader and ART coach who facilitates ART events and processes, and supports teams in delivering value." |
| 28 | Product Management | PARTLY | https://framework.scaledagile.com/agile-release-train (lists the role only; definition not in readable text); definition at https://framework.scaledagile.com/product-management/ | none | /product-management/ 15 October 2024 | "Product Management is the function responsible for defining desirable, viable, feasible, and sustainable solutions that meet customer needs and supporting development across the product life cycle." Differs from the worklist: order is "desirable, viable, feasible, sustainable" and the object is "solutions", not "products". The "feasible, viable" order and "products" appear nowhere I read. |
| 29 | System Architect | SUPPORTED | https://framework.scaledagile.com/system-architect/ | none | not shown | "The System Architect is responsible for defining and communicating a shared technical and architectural vision for the solutions developed by an ART." Summary: "They do this by defining enablers". |
| 30 | Business Owners | PARTLY | https://framework.scaledagile.com/agile-release-train (lists the role only); definition at https://framework.scaledagile.com/business-owners/ | none | not shown | "Business Owners (BOs) are key ART stakeholders who have the primary business and technical responsibility for return on investment (ROI), governance, and compliance." "Fitness for use" (worklist) is not in the readable text of either page; SAFe says "compliance". |
| 31 | Story | SUPPORTED | https://framework.scaledagile.com/story | none | 27 January 2025 | "Each story focuses on a specific behavior that can be developed in incremental steps to offer value to the user or the solution." and "Keeping stories small ensures they can be completed in a single iteration". Definition: "Stories are short descriptions of a small piece of desired functionality written from the user's perspective." |
| 32 | Iteration | SUPPORTED (at /iterations/; listed URL carries only a passing mention) | https://framework.scaledagile.com/iterations/ (title "Iterations - Scaled Agile Framework"); listed URL https://framework.scaledagile.com/iteration-planning/ | none | /iterations/ 25 February 2025; iteration-planning 18 March 2026 | "Iterations are a standard, fixed-duration timebox during which Agile Teams and ARTs individually and collectively deliver incremental customer value while working towards the PI objectives." Also "All teams on the ART synchronize to the same iteration and PI cadence" (wording is "fixed-duration", not "fixed-length"). |
| 33 | Iteration Planning | SUPPORTED | https://framework.scaledagile.com/iteration-planning/ (tab "Extended Guidance - Iteration Planning") | none | 18 March 2026 | "During planning, the team defines, organizes, and commits to the work for the next iteration." Glossary: "all team members determine how much of the Team Backlog they can commit to delivering during an upcoming Iteration." |
| 34 | Iteration Goals | SUPPORTED | https://framework.scaledagile.com/glossary/ ; page https://framework.scaledagile.com/iteration-goals/ (tab "Extended Guidance - Iteration Goals") | none | not shown | "Iteration Goals are a high-level summary of the business and technical goals that an Agile Team agrees to accomplish in an Iteration." |
| 35 | Team Backlog | SUPPORTED (at /team-backlog/; listed URL does not state it in readable text) | https://framework.scaledagile.com/team-backlog/ ; listed URL https://framework.scaledagile.com/agile-teams | none | /team-backlog/ 12 February 2025 | "The Team Backlog is a Kanban system that is used to capture and manage the user stories and enablers intended to enhance the solution." |
| 36 | Team Backlog Refinement | PARTLY | https://framework.scaledagile.com/team-backlog-refinement/ (tab "Extended Guidance - Team Backlog Refinement") | none | 18 March 2026 | "Team Backlog Refinement is an event that helps Agile Teams clarify and prepare upcoming stories and features". The word "continuously" is not on the page; glossary calls Backlog Refinement "a periodic activity". |
| 37 | Iteration Review | SUPPORTED (at /iteration-review/); listed glossary-term stub PARTLY | https://framework.scaledagile.com/iteration-review/ (tab "Extended Guidance - Iteration Review", 200); listed https://framework.scaledagile.com/blog/glossary_term/iteration-review/ (200, stub) | none | /iteration-review/ 18 March 2026; stub not shown | Full page: "a key event that allows the Agile Team to showcase their accomplishments, receive feedback, and collaboratively determine next steps as they close the iteration timebox." Stub: "a regular SAFe Scrum event where the team inspects the iteration increment, assesses progress, and adjusts the team backlog." (no "feedback" in the stub) |
| 38 | Iteration Retrospective | SUPPORTED | https://framework.scaledagile.com/iteration-retrospective/ (tab "Extended Guidance - Iteration Retrospective") | none | 18 March 2026 | "The Iteration Retrospective is a regular event held at the end of each iteration during which Agile Teams review their results to identify improvements for future work." |
| 39 | Product Owner | PARTLY | https://framework.scaledagile.com/product-owner/ ; listed URL https://framework.scaledagile.com/agile-teams (names the role only) | none | /product-owner/ 24 January 2025 | "The Product Owner (PO) is the Agile team member primarily responsible for maximizing the value delivered by the team by ensuring that the team backlog is aligned with customer and stakeholder needs." "Content authority" and "defines stories and prioritises" are not in the readable text (the page says the PO is "managing the backlog"). |
| 40 | Scrum Master/Team Coach | PARTLY | https://framework.scaledagile.com/scrum-master-team-coach/ ; listed URL https://framework.scaledagile.com/agile-teams (names the role only) | none | not shown | "The SAFe Scrum Master/Team Coach (SM/TC) is a servant leader and coach for an Agile Team who facilitates team events and processes, and supports teams and ARTs in delivering value." "Helps remove impediments" is not in the readable text. |
| 41 | Definition of Done | SUPPORTED (glossary); NOT FOUND (not readable) at the listed built-in-quality page | https://framework.scaledagile.com/glossary/ (entry; no page link in glossary; /definition-of-done/ returns 404); listed https://framework.scaledagile.com/built-in-quality | none | not shown | Glossary: "The Definition of Done specifies the requirements for completeness of a work product or increment of value." The readable part of /built-in-quality does not mention it. The ART and Solution Train Backlogs page mentions "the definition of done (DoD)". |
| 42 | Built-in quality | SUPPORTED | https://framework.scaledagile.com/built-in-quality (tab "Extended Guidance - Built-In Quality") | none | not shown | "Built-In Quality is a set of practices to help ensure that the outputs of Agile teams in business and technology domains meet appropriate quality standards throughout the process of creating customer value." |
| 43 | Continuous Delivery Pipeline | SUPPORTED | https://framework.scaledagile.com/continuous-delivery-pipeline/ | none | 6 February 2025 | "The Continuous Delivery Pipeline (CDP) represents the workflows, activities, and automation needed to guide new functionality from ideation to an on-demand release of value." Four aspects: "continuous exploration (CE), continuous integration (CI), continuous deployment (CD), and release on demand (RoD)". |
| 44 | Continuous Exploration | SUPPORTED | https://framework.scaledagile.com/continuous-exploration/ (tab "Extended Guidance - Continuous Exploration") | none | not shown | "drives innovation and fosters alignment on what should be built by continually exploring the market and customer needs, defining a vision, roadmap, and set of features for a solution." |
| 45 | Continuous Integration | SUPPORTED | https://framework.scaledagile.com/continuous-integration/ (https works, no redirect; the http form also served 200 without redirect through the fetch proxy) | none | not shown | "Continuous Integration (CI) is an aspect of the Continuous Delivery Pipeline in which new functionality is developed, tested, integrated, and validated in preparation for deployment and release." |
| 46 | Continuous Deployment | SUPPORTED | https://framework.scaledagile.com/continuous-deployment (tab "Extended Guidance - Continuous Deployment") | none | not shown | "Continuous Deployment (CD) is an aspect of the Continuous Delivery Pipeline that automates the migration of new functionality from a staging environment to production, where it is made available for release." |
| 47 | Release on Demand | SUPPORTED | https://framework.scaledagile.com/release-on-demand | none | 25 February 2025 | "Release on Demand is an aspect of the Continuous Delivery Pipeline that releases new functionality immediately or incrementally based on business and customer needs." |

Counts for the 47 terms: SUPPORTED 39 (including the "better URL" cases 10, 21, 32, 35, 37, 41), PARTLY 8 (9, 13, 25, 28, 30, 36, 39, 40), NOT SUPPORTED 0, NOT FOUND 0 (term 41 is NOT FOUND (not readable) on its listed page only).

### "Also check" terms (deliberately not adopted)

| term | does SAFe use it? | where | quote |
|---|---|---|---|
| Definition of Ready | NOT FOUND (not readable) in any SAFe page text I could read. No glossary entry; /definition-of-ready/ returns 404. SAFe's own site search for the quoted phrase returns two pages (Applying SAFe to Hardware Development, https://framework.scaledagile.com/applying-safe-to-hardware-development ; Accelerating Flow with DevSecOps and the Software Factory, https://framework.scaledagile.com/accelerating-flow-with-devsecops-and-the-software-factory), but their readable text (login-gated) does not contain the phrase, so I cannot confirm usage or meaning. Not settled. | - | none to quote. SAFe does use "definition of done (DoD)" (glossary, ART and Solution Train Backlogs page). |
| Innovation and Planning iteration | YES, SAFe's own term | Glossary "Innovation and Planning Iteration"; page https://framework.scaledagile.com/innovation-and-planning-iteration/ (last update 25 February 2025); PI page; PI Planning page | "The Innovation and Planning (IP) Iteration is a unique, dedicated iteration that occurs every PI. It provides an estimating buffer for meeting PI Objectives and dedicated time for innovation, continuing education, PI Planning, and Inspect and Adapt (I&A) events." PI Planning page: "The event takes place in the Innovation and Planning Iteration". |
| ART Sync | YES | Glossary entry; page https://framework.scaledagile.com/art-sync/ (last update 20 March 2026) | "The ART Sync is an ART event that combines the Product Owner (PO) Sync and Coach Sync." (glossary); page: "The ART Sync consists of two main, synchronized conversations that are typically combined into a single event: The PO Sync and the Coach Sync." |
| Program Board | NOT current SAFe wording. SAFe's own article says it was the pre-6.0 term. Not in glossary; /program-board/ 404; PI Planning page says "ART planning board" | https://framework.scaledagile.com/blog/why-program-is-still-used-in-one-place-in-safe-6-0 (News, "June 10, 2024 By Steve Mayner") | "Before version 6.0, in SAFe, a 'program' was the part of the Framework that focused on creating and delivering value through Agile Release Trains (ARTs). ... dependencies were tracked on a 'program board,'" |
| Solution Demo | YES (large-solution level; distinct from System Demo) | Glossary entry; page https://framework.scaledagile.com/solution-demo/ (tab "Extended Guidance - Solution Demo", no date shown); also on Large Solution SAFe page | "The Solution Demo provides stakeholders an integrated view of the contributions of multiple ARTs and suppliers to obtain objective evidence of solution performance and to gather feedback." System Demo page: "For larger Solutions involving multiple ARTs, this System Demo becomes a part of the broader Solution Demo." |
| DevOps health radar | NOT FOUND (not readable) in page text I could read. SAFe's own site search for the phrase lists several pages (DevOps, Cloud, Measure and Grow, Continuous Delivery Pipeline and others), but the readable (non-gated) text of the pages I fetched (/devops, /measure-and-grow, /continuous-delivery-pipeline/) does not contain it, and I did not use search-listing wording. Likely used by SAFe (as "SAFe DevOps Health Radar") but not confirmed from page text. | - | none to quote |

## D. Open-question answers

### D.SAFe sources (worklist 2.1) and AI-Native SAFe

Section 4 items assigned: none. Section 3 question 3 (AI-Native SAFe) answered below. Questions 1 and 2 are not mine, but see the notes at the end.

**Q3. What AI-Native SAFe changes, in Core SAFe terms (all pages read directly 2026-11-20).**

1. Release date. Not "2026-06-23" as a release date. What is printed:
   - https://framework.scaledagile.com/blog/ai-native-safe-is-the-operating-model-for-the-ai-native-organization, headed "New Release: ..." and dated "June 23, 2026" by Andrew Sales: "June 16th marked such an evolution ... as we announced and unveiled, AI-Native SAFe." "On June 16, we unveiled the AI-Native SAFe Big Picture through a new virtual events series." The release is early access: "New guidance will follow every two weeks", with "a full reveal at the SAFe Summit San Diego on September 14-18".
   - https://framework.scaledagile.com/whats-new-in-safe, June 2026: "we officially introduced AI-Native SAFe"; July/August: "we continued to iteratively release AI-Native SAFe".
   - https://framework.scaledagile.com/blog/safe-summit-keynote-recap-launching-the-operating-model-for-the-age-of-ai (dated "October 6, 2026"): "On the 15th of September 2026 ... Today marks the official release of AI-Native SAFe".
   - So 2026-06-23 is the date of the announcement post, 2026-06-16 the unveiling, 2026-09-15 the "official release". Wording to use: "unveiled 16 June 2026; officially released 15 September 2026 (as printed by Scaled Agile)".
2. "Core SAFe" is a label SAFe itself uses. Home page https://framework.scaledagile.com/: "Core SAFe continues to provide the world's most adopted Operating Model for scaling Lean and Agile practices across your organization. AI-Native SAFe, builds on this foundation to provide an AI-Native Operating Model". Glossary-style pages say "Core SAFe Inspect and Adapt event" (Sense and Respond page). The home-page Big Picture has an "About Core SAFe" link (/about).
3. "Core SAFe remains fully supported": the exact words are not on the site pages read. Exact printed wording: June 23 post, "our commitment to continue supporting and evolving the Core SAFe operating model ... Core SAFe remains the foundation for successful enterprise agility ... This release does not replace Core SAFe." Oct 6 post: "our strategic decision to continue supporting two co-existing versions of the Framework, Core SAFe and AI-Native SAFe".
4. PI Planning to PI Outcome Planning: SUPPORTED. https://framework.scaledagile.com/ain-safe-pi-outcome-planning/ (last update 28 July 2026): "The two-day PI Planning event ... has been replaced by a one-day PI Outcome Planning event that focuses on in-flight re-alignment." Event "occurs at the start of every Planning Interval (PI)". Session 4 post (Aug 5, 2026): "a 1-day event for everyone on the AI-Native ART, replacing the 2-day PI Planning event".
5. Inspect and Adapt to Sense and Respond: SUPPORTED. https://framework.scaledagile.com/ain-safe-sense-and-respond (last update 28 July 2026): "The half-day Inspect and Adapt event that drove ART-level learning cycles on a PI cadence has been replaced by a two-hour Sense and Respond event every iteration, driving accelerated learning. This Sense and Respond event also includes the activities formally [sic; the PI Outcome Planning page prints 'formerly'] present in the System Demo." Session 4 post: "It replaces the SAFe Inspect and Adapt event and incorporates System Demo activities." Facilitated by the RTE.
6. "Customer Demos replace System Demo": NOT SUPPORTED as worded. No page read says Customer Demos replace the System Demo. What is printed: the System Demo's activities are absorbed into Sense and Respond (above); Customer Demos are a separate practice, "In AI-Native SAFe, Customer Demos are held regularly" (Session 4 post), and the Customer Centricity article (https://framework.scaledagile.com/customer-centricity/, last update 28 July 2026, used by both Core and AI-Native) has a section "How do customer demos steer product evolution?". Sense and Respond's first hour includes "product demonstrations".
7. Other Core terms (from the pages read; the AI-Native Big Picture is an image map, so absence from it is not proof of removal):
   - Planning Interval: KEPT. PI Outcome Planning and Sense and Respond both say "SAFe has always used nested cadences - iterations ... and planning intervals (PIs) every 8 to 12 weeks. While the nature and purpose of the cadences remain fairly consistent ...". PI Outcome Planning "occurs at the start of every Planning Interval (PI)". New terms "PI Outcomes", "Team Outcomes", "ART Outcomes" appear on the AI-Native Big Picture; Core page /pi-objectives/ is on the Core picture.
   - Iteration: KEPT (Sense and Respond occurs "at the boundary of every iteration"; iterations "typically a week or two weeks long" on the Sense and Respond page vs "typically two weeks long" on the PI Outcome Planning page).
   - Inspect and Adapt: REPLACED, with an option: "Some ARTs may choose to run the problem-solving portion of the Core SAFe Inspect and Adapt event periodically".
   - System Demo: ABSORBED into Sense and Respond (see 5).
   - PI Planning: REPLACED by PI Outcome Planning; PI Objectives, ART planning board: the AI-Native pages say PI Outcomes and a "PI Outcome Planning Board" (Session 4 post). 
   - Release Train Engineer, Product Management, System Architects, Business Owners: KEPT as ART roles (listed as attendees of PI Outcome Planning and Sense and Respond); Business Owners is a clickable item on the AI-Native Big Picture. New role: "AI Value Architect" (https://framework.scaledagile.com/ain-safe-ai-value-architect).
   - Agile Team, Product Owner, Scrum Master/Team Coach: REPLACED in AI-Native by AI-Native Teams: "Standardized Agile roles are replaced by flexible capabilities, Product, Builder, and Domain Expert, working alongside AI" (Oct 6 post); AI-Native Teams have "Product, Builder, Domain Expert, and AI capabilities", are "typically smaller, consisting of three to seven team members" and use "Align, Sense, and Respond" (https://framework.scaledagile.com/ain-safe-ai-native-teams, last update 14 July 2026). Product Owner and Scrum Master/Team Coach are not named on the AI-Native Teams page text read; the AI Value Architect page mentions Scrum Masters and Team Coaches as people who may become AI Value Architects.
   - Agile Release Train: KEPT as "AI-Native ART": "a team of teams organized around one or more products" (https://framework.scaledagile.com/ain-safe-ai-native-art/, last update 14 August 2026).
   - Features and Enablers: KEPT, with new work items: "Introduces Experiments and Prototypes alongside Features and Enablers" (Oct 6 post). Story, Epic, Capability, WSJF, Lean budgets, Iteration Planning, Definition of Done: not mentioned on any AI-Native page read; not stated as kept or removed.
   - Lean Portfolio Management: AI-Native pages "Portfolio Outcomes and Investment Strategy" and "Return on Investment" exist; no statement on LPM terms (Strategic Themes, Lean budgets, guardrails) being renamed or removed.
8. Version labels: Core pages print no version; /safe-6-0-configurations calls the four configurations "the Scaled Agile Framework 6.0 configurations ... the latest version of SAFe" (last updated 3 September 2025). The AI-Native Resource Hub (https://content.scaledagile.com/ai-native-safe-series/resource-hub) card for the "AI-Native SAFe Big Picture" carries the stray text "SAFe 6 is an update to the SAFe Framework ...", a copied meta description. No "SAFe 7" anywhere. whats-new has no version label. whats-new prints "Last Update: 9 April 2026" at the foot while its text covers up to August 2026.
9. Unread: https://ai-native.scaledagile.com/ returned HTTP 429 twice (not readable). Many AI-Native articles are login-walled after the summary.

Notes for the agent handling questions 1 and 2 (cadence wording I saw, quoted from pages in cache):
- /planning-interval: "A Planning Interval (PI) is a timebox of 8-12 weeks"; "This pattern is a suggestion rather than a strict rule, and there isn't a set number of iterations for a PI. However, experience shows that a PI lasting between 8 and 12 weeks is a good starting point, with shorter durations preferred."; "The most common PI structure includes four or five development iterations and one Innovation and Planning (IP) iteration." Key takeaway: "typically an 8 to 12-week timebox".
- /pi-planning/: "It is typically a 2-day event for the entire ART that takes place every 8-12 weeks."
- /iteration-planning/: "timeboxed to approximately 90 minutes for a two-week iteration."
- /iterations/: "A PI commonly comprises four two-week development iterations and one Innovation and Planning (IP) iteration."
- /iteration-retrospective/: "a 60-minute or less Agile Team event".
- /iteration-review/ (read only the opening): "second-to-last event of the iteration"; the 90-minute figure was not checked.
- Site-wide search for "definition of ready" (https://framework.scaledagile.com/?s=%22definition+of+ready%22, SAFe's own search) returns two articles using the term in passing: https://framework.scaledagile.com/accelerating-flow-with-devsecops-and-the-software-factory and https://framework.scaledagile.com/applying-safe-to-hardware-development ("the Definition of Ready (DoR) and Done (DoD)"). No glossary entry or defining page.
- Glossary has "Innovation and Planning Iteration", "ART Sync", "Solution Demo"; no "Program Board" or "DevOps Health Radar" entry seen (not searched beyond the glossary).

### D.SAFe closed allow-list (worklist section 3)

1. Version string.
 - No page I read prints a framework version label in its header or footer. Header: nav only ("Framework", "About", "Blog", ...). Footer: "© 2026 Scaled Agile, Inc." and "The information on this page is © 2010-2026 Scaled Agile, Inc.". The "What's new in SAFe?" page (https://framework.scaledagile.com/whats-new-in-safe) prints no "SAFe 6.0" or other version number either.
 - The only version label on the site is on the home page (https://framework.scaledagile.com/), link text "Find the SAFe 6.0 Big Picture configurations here", which goes to https://framework.scaledagile.com/safe-6-0-configurations (title "SAFe 6.0 Configurations", last updated "3 September 2025"). That page says: "Welcome to the Scaled Agile Framework 6.0 configurations. Navigate here to access the latest version of SAFe." It lists Full SAFe, Essential SAFe, Large Solution SAFe, Portfolio SAFe. A SAFe blog post (https://framework.scaledagile.com/blog/why-program-is-still-used-in-one-place-in-safe-6-0, 10 June 2024) refers to "version 6.0" and to an article "What's New in SAFe 6.0?". I did not read that article, so the 6.0 release date (March 2023?) is NOT confirmed here.
 - Date of latest framework update: the What's new page has monthly entries up to "August 2026" (AI-Native SAFe webinar series, resource hub update); June 2026: "In June, we officially introduced AI-Native SAFe". Its own footer says "Last Update: 9 April 2026", which is stale relative to the August 2026 entries. Page statement: "This dedicated page will be updated during the first week of each month". No September-November 2026 entries on the page on 2026-11-20. The exact date 2026-06-23 is not on this page (other agent covers AI-Native).
 - "Core SAFe" is SAFe's own label: home page, "Core SAFe continues to provide the world's most adopted Operating Model for scaling Lean and Agile practices across your organization. AI-Native SAFe, builds on this foundation to provide an AI-Native Operating Model"; the home page has "Core SAFe" and "AI-Native SAFe" tabs and an "About Core SAFe" item; What's new July 2026: "the following Core SAFe article was also updated".

2. Cadence defaults (SAFe's own pages, 2026-11-20).
 - PI length: https://framework.scaledagile.com/planning-interval (last update 25 February 2025): "A Planning Interval (PI) is a timebox of 8-12 weeks"; "A Planning Interval is typically an 8 to 12-week timebox."; "This pattern is a suggestion rather than a strict rule, and there isn't a set number of iterations for a PI. However, experience shows that a PI lasting between 8 and 12 weeks is a good starting point, with shorter durations preferred." Status: typical value and starting-point suggestion; explicitly not a requirement. Structure: "most common PI structure includes four or five development iterations and one Innovation and Planning (IP) iteration."
 - PI Planning length: https://framework.scaledagile.com/pi-planning/ (last update 15 March 2026): "It is typically a 2-day event for the entire ART that takes place every 8-12 weeks." Status: typical. (AI-Native pages say the two-day PI Planning is replaced by a one-day PI Outcome Planning; not verified here.)
 - Iteration Planning length: https://framework.scaledagile.com/iteration-planning/ (last update 18 March 2026): "The iteration planning meeting is timeboxed to approximately 90 minutes for a two-week iteration." Status: stated as the timebox, qualified by "approximately" and tied to a two-week iteration; not labelled default or requirement.
 - Iteration length: https://framework.scaledagile.com/iterations/ (last update 25 February 2025): "A typical PI has four two-week development iterations, followed by one Innovation and Planning iteration." and "A PI commonly comprises four two-week development iterations and one Innovation and Planning (IP) iteration." The page defines an iteration as "a standard, fixed-duration timebox" without prescribing a length. Status: typical/common. Other SAFe pages in the cache (AI-Native Sense and Respond and PI Outcome Planning articles; read by other agents) say "SAFe has always used nested cadences – iterations, typically a week or two weeks long, and planning intervals (PIs) every 8 to 12 weeks" (Sense and Respond page) and "iterations, typically two weeks long" (PI Outcome Planning page): typical values.
 - Iteration Review length: https://framework.scaledagile.com/iteration-review/ (18 March 2026), Key Takeaways: "The Iteration Review is a 90-minute or less Agile Team event". The qualifier "for a two-week iteration" is NOT in the text I read (body is login-gated). Status: stated as a ceiling ("or less"). Related: https://framework.scaledagile.com/iteration-retrospective/ "The Iteration Retrospective is a 60-minute or less Agile Team event".
 - None of these is labelled "default", "recommendation" or "requirement" in the readable text, except the PI page's "a suggestion rather than a strict rule".

4. Which of the 47 URLs redirect, 404 or point to a differently named page?
 - Redirect: none. All 47 listed URLs (plus the glossary_term ones) returned HTTP 200, with a final URL identical to the one requested (trailing-slash form as listed). The http:// form of continuous-integration also returned 200; use https.
 - 404: none of the 47. (Unlisted guesses that 404: /definition-of-done/, /art-planning-board/, /definition-of-ready/, /program-board/.)
 - Tab title differs from the listed term (prefix "Extended Guidance - " and suffix " - Scaled Agile Framework"): large-solution, solution-train, guardrails ("Lean Budget Guardrails"), epic-owner ("Epic Owners"), wsjf (H1 "Weighted Shortest Job First"), iteration-planning, team-backlog-refinement, iteration-retrospective, built-in-quality, continuous-exploration, continuous-integration, continuous-deployment. Other pages have no prefix.
 - H1 differs from tab title: /lean-portfolio-management-discipline has tab "Lean Portfolio Management Discipline" and H1 "Lean Portfolio Management"; /lean-portfolio-management (the older competency page) says to navigate to the discipline article.
 - Listed URL does not carry the term's definition (use the better URL): #10 Lean budgets (use /lean-budgets/), #13 Epic (/epic/), #21 PI Objectives (/pi-objectives/), #28 Product Management (/product-management/), #30 Business Owners (/business-owners/), #32 Iteration (/iterations/), #35 Team Backlog (/team-backlog/), #37 Iteration Review (/iteration-review/, the listed glossary_term URL is a one-sentence stub), #39 Product Owner (/product-owner/), #40 Scrum Master/Team Coach (/scrum-master-team-coach/), #41 Definition of Done (glossary entry only; no own page), #34 Iteration Goals (/iteration-goals/ exists), #26 ART backlog (/art-and-solution-train-backlogs/). #16, #25, #37 listed URLs are stub glossary-term pages (/blog/glossary_term/...) with one-sentence text, no date.
 - Pages with no "last update" date at all: see Part C (many "not shown").

### D.DORA (2.2)

**Q8. DORA AI capability names and order; capability page titles.**
- Seven capabilities, names and order as printed in the announcing post (https://cloud.google.com/blog/products/ai-machine-learning/introducing-doras-inaugural-ai-capabilities-model, 2025-09-23) and identically in the Dec 2025 post: 1 Clear and communicated AI stance; 2 Healthy data ecosystems; 3 AI-accessible internal data; 4 Strong version control practices; 5 Working in small batches; 6 User-centric focus; 7 Quality internal platforms.
- https://dora.dev/ai/capabilities-model/report/ says only "seven capabilities"; it lists no names. dora.dev/ai/capabilities-model/ redirects to it. The 2025 announcement blog says "seven capabilities" but its list is not in the page text.
- On dora.dev the catalog (https://dora.dev/capabilities/, alphabetical, AI tag) uses different names for two: "Version control" (tags core, AI; card: "Version control ensures reproducibility ... safety net as AI accelerates") and "Platform engineering" (tag AI; card: "A platform provides the automated, secure pathways..."). The other five AI-tagged names match the blog: AI-accessible internal data, Clear and communicated AI stance, Healthy data ecosystems, User-centric focus, Working in small batches. The dora.dev catalog has no AI-tagged page titled "Strong version control practices" or "Quality internal platforms". I did not open the version-control or platform-engineering pages.
- Capability page titles: browser tab is always "DORA | Capabilities: <Name>"; the on-page H1 is "<Name>" (tags core / AI show next to it). Names: Working in small batches; Work in process limits; Customer feedback; Test automation; Monitoring and observability; Streamlining change approval; Continuous delivery. Note "Work in process limits" (not "WIP limits") and the URL slug wip-limits.
- Last-updated lines: small batches 2025-12-08; test automation 2025-07-17; change approval 2025-10-30; AI capabilities report page 2025-11-25; WIP limits, customer feedback, monitoring, continuous delivery print none.

**Q9. DORA metric names and grouping.**
- Source: https://dora.dev/guides/dora-metrics/ (Nathen Harvey, last updated January 5, 2026): "DORA has identified five software delivery performance metrics". Throughput: change lead time; deployment frequency; failed deployment recovery time. Instability: change fail rate; deployment rework rate.
- Older names, per https://dora.dev/insights/dora-metrics-history/ (2026-01-02): "lead time for changes", "mean time to recover (MTTR)" / "time to restore service" renamed "failed deployment recovery time" in 2023; "change failure rate" in the history text; fifth metric deployment rework rate added 2024. In 2015 grouping was throughput (deployment frequency, lead time) versus stability (MTTR, change fail rate); now MTTR's successor sits in throughput.
- Not settled: whether "change fail rate" or "change failure rate" is the spelling to use. The metrics guide and the change-approval capability page use "change fail rate"; the history page uses both ("change fail rate" and "change failure rate"). The 2024 blog still says "DORA's four key metrics, introduced in 2013". The FAQ page (last updated 2025-10-06) refers to "the 'Four Key' metrics" and a Quick Check built on "five individual metrics".

### D.Scrum, agile and requirements practice (2.3)

**Q1. Definition of Ready: originator and earliest verifiable public uses.** Not settled; the primary pages could not be read.
- Agile Alliance passage is on https://agilealliance.org/glossary/definition-of-ready/ (read directly). Section "Origins of Definition of Ready": "ETVX framework first described in 1985" and, under 2008, "the first few allusions to teams using a 'definition of ready' date to the beginning of that year, the first formal description seems to be from October, and is incorporated into 'official' Scrum training material shortly thereafter". The page prints no author, date or citations. Hedged wording ("appears", "seems"). It names the 1985 paper only as "A programming process architecture".
- Kronfält October 2008 post (scrumftw.blogspot.com): not readable, host did not resolve. Sutherland July 2009 post (jeffsutherland.com): not readable, host did not resolve. ETVX paper (dl.acm.org): HTTP 403. Overeem (www.scrum.org): HTTP 403. So no date or byline in this slice is confirmed from a primary page.
- Scrum Guide 2020 (https://scrumguides.org/scrum-guide.html): does not define a Definition of Ready; the phrase does not occur. It says items that can be Done within one Sprint "are deemed ready for selection in a Sprint Planning event".
- New finding: the Scrum Guide revision history (https://scrumguides.org/revisions.html), under "Changes between 2011 and 2013 Scrum Guides", says: "Product Backlog items with this transparency are called 'Ready.' Ready and Done are two states that reinforce transparency." So the Guide itself used the state "Ready" in 2013 (per the history page; the 2013 edition itself was not read). It is "Ready", not "Definition of Ready". The 2020 edition's wording is the surviving trace.
- Agile Alliance DoD page (https://agilealliance.org/glossary/definition-of-done/) has an Origins list (2002 Bill Wake article, 2003 training slide "The story of Done", 2005, 2007). It does not mention Ready.
- No earlier public use than the Agile Alliance's 1985 ETVX precursor and early-2008 allusions was found; none could be looked for on the unreadable pages.

**Q2. Inspect and adapt predating SAFe.**
- (a) Schwaber 1995 paper: not readable (www.jeffsutherland.org did not resolve). Date and wording unconfirmed from the paper. The 2020 Scrum Guide ("Scrum Guide History", https://scrumguides.org/scrum-guide.html) says: "Ken Schwaber and Jeff Sutherland first co-presented Scrum at the OOPSLA Conference in 1995 ... made public the first formal definition of Scrum." That is the Guide's own account, not the paper.
- (b) Schwaber and Beedle 2001: not readable (dl.acm.org 403). The "visibility, inspection and adaptation" wording is unconfirmed.
- (c) Agile Manifesto principles (https://agilemanifesto.org/principles.html): the twelfth statement reads "At regular intervals, the team reflects on how to become more effective, then tunes and adjusts its behavior accordingly." The principles page prints no date and no byline. The Manifesto home page (https://agilemanifesto.org/) prints "(c) 2001, the above authors" over 17 names. The History page (https://agilemanifesto.org/history.html) says the Snowbird meeting was "February 11-13, 2001". The page does not itself state that the twelve principles date from that meeting.
- (d) Scrum Guide pillars: the 2020 Guide names "transparency, inspection, and adaptation" as "the empirical Scrum pillars" and has "Inspection without adaptation is considered pointless." The revisions page places a mention of "the Scrum pillars of transparency, inspection, and adaptation" in "Changes between 2013 and 2016"; it adds an "Artifact Transparency" section in 2013 ("Scrum relies on transparency"). It does not say in which edition the pillars first appeared; the pre-2016 editions were not read.
- (e) SAFe first use of the term: could not be settled. The SAFe page https://framework.scaledagile.com/inspect-and-adapt (read directly, partly login-gated: "Log in to continue reading") shows "Last update: 20 March 2026" and "(c) 2010-2026 Scaled Agile, Inc." It prints no first-use date. It ties the event to the Manifesto: it quotes the twelfth principle and says "The I&A amplifies the original principle". Leffingwell's 2011 book and an October 2011 blog post are not among the sources in this slice and were not read. Whether SAFe's first publication named the event is NOT FOUND (not readable / not on the pages read).

**Q3. Scrum Guide 2020 still current on 2026-11-20.**
- https://scrumguides.org/download.html (read directly 2026-11-20) lists "English (November 2020) - Official Current Version" and, below it, note: "The current official version of the Scrum Guide was released in November 2020." The home page, revision history (latest section "Changes between 2017 and 2020") and FAQ show no later edition. The site footer reads "(c) 2025 ScrumGuides.org"; HTTP Last-Modified on these pages is 2025-01-27. So on the official site the 2020 edition is still labelled current; a newer edition published elsewhere cannot be ruled out from this site alone.
- Expansion Pack: scrumguides.org does not link to it (no link on home, download, FAQ, revisions or the Guide page); two guessed paths on scrumguides.org (/scrum-guide-expansion-pack.html, /expansion-pack.html) return 404. The domain https://scrumexpansion.org/ (reached by trying the name directly; not linked from scrumguides.org, so its relation to the official site is not shown) says "Companion to the 2020 Scrum Guide", "Created by Jeff Sutherland, John Coleman, Ralph Jocham", 11 expansion documents; HTTP Last-Modified 2026-02-18. It prints "v2.0.9" in the footer next to the website-design credit (Martin Hinshelwood); it does not print "v2026.1" or "January 2026". The "v2026.1, January 2026" label in the worklist is NOT FOUND on the page read. It is not the Guide: it calls itself a companion. www.scrum.org was not readable, so any scrum.org statement about the Pack is unchecked.

**Q17. Cooper stage-gate and Wake INVEST.**
- Wake INVEST (read directly): H1 "INVEST in Good Stories, and SMART Tasks"; tab title "INVEST in Good Stories, and SMART Tasks - XP123"; byline "Bill Wake"; "Posted on August 17, 2003"; venue: the author's own site XP123 (xp123.com), tagged "XPlorations", not a journal; author note: "I developed the INVEST acronym, and wrote this article in April and August, 2003"; later postscript "Added 2-16-2011" on how the acronym was chosen. No older URL form was tried.
- Cooper stage-gate: NOT FOUND (not readable). onlinelibrary.wiley.com returned HTTP 403. Title, byline (the "Cooper" attribution), venue (the DOI prefix 10.1002/9781444316568 looks like a Wiley encyclopedia, unverified) and year are unconfirmed.

### D.ISO/IEC/IEEE and ISTQB (2.4, 2.5)

**Q5 ISO/IEC/IEEE 12207 second edition April 2026 (cannot be settled).**
- https://www.iso.org/standard/63712.html (2017 edition) and https://www.iso.org/standard/90219.html (2026 edition, number inferred) both returned HTTP 403 on 2026-11-20. Nothing about the edition, date, title, catalogue URL or the status of the 2017 edition was read. Read directly: no.
- Not settled from freely readable pages: (a) whether a second edition exists and was published in April 2026; (b) that it cancels and replaces 2017; (c) its title; (d) whether 90219 is its catalogue number; (e) the 12 technical process names and the 2017 bidirectional-traceability wording. Under the brief these stay NOT FOUND (not readable). Do not state the April 2026 date or "cancels and replaces" in the site until read from a first-party page (iso.org when readable, or IEEE's own standards page, which was not tried because it was outside my slice and brief).

**Q6 ISO/IEC/IEEE 29148 characteristics and order (cannot be settled).**
- https://www.iso.org/standard/72089.html HTTP 403. The nine-name list, its order, the separate set-level list (five?), which list applies to stakeholder requirements, the traceability definition and the "unique identification" attribute are all unconfirmed. Catalogue pages normally show only the abstract, and the characteristics list is clause text (paywalled), so even a readable catalogue page would likely not settle the order. Recommend citing 29148 only for what the catalogue abstract supports once readable, and keeping the nine-name list out of the site unless the author checks it against the purchased standard.

**Q15 ISO/IEC/IEEE 14764 four or five maintenance types (cannot be settled).**
- https://www.iso.org/standard/80710.html HTTP 403. Nothing read on corrective, adaptive, perfective, preventive, or an "additive" type, nor on the 12207:2017 alignment. The ISTQB CTFL v4.0.1 syllabus (read) covers "Maintenance Testing" (2.2.4) but does not enumerate ISO 14764 maintenance types; I did not search it for them, so I make no claim about it. Unsettled; recommend the site not state a number of maintenance types attributed to 14764.

**Q16 ISTQB currency and canonical URLs (settled for ISTQB).**
- CTFL v4.0 current: https://istqb.org/certifications/ (tab title "Enhance Your Career with ISTQB® Software Testing Certifications"; H1 "Our Certifications") lists "Certified Tester Foundation Level (CTFL) v4.0" as the Foundation certification; no newer Foundation version is listed. The CTFL page (https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/, tab title "Certified Tester Foundation Level (CTFL) v4.0 Overview") offers "ISTQB CTFL Syllabus v4.0.1". Canonical syllabus PDF: https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf (reached from download link https://istqb.org/?sdm_process_download=1&download_id=3345; the Last-Modified header on the PDF is 13 May 2026, which is a re-upload date, not the syllabus date). Its revision history: v4.0.1 15.09.2024 "Errata"; v4.0 21.04.2023 "General release version". The glossary data lists "Foundation v4.0" with released_at 2024-09-15. So "v4.0" is the current Foundation certification label and the current syllabus file is v4.0.1; cite as "CTFL Syllabus v4.0.1 (2024-09-15)" or "v4.0".
- Agile Tester 2014 syllabus is not the newest Agile material and is being retired: https://istqb.org/certifications/certified-tester-foundation-level-agile-tester-ctfl-at/ announces "Exams (including retakes) and training for CTFL-AT are only available until the sunset dates (6 May 2027 for English, 6 November 2027 for non-English)", pointing candidates to CTFL v4.0 and "Certified Tester Advanced Level Agile Tester v2.0 (CTAL-AT)". The certifications page lists "Certified Tester Advanced Level Agile Tester (CTAL-AT) v2.0 [New]"; the glossary data gives "Advanced Agile Tester v2.0" released_at 2026-04-17. ISTQB still hosts the 2014 document as "ISTQB CTFL-AT Syllabus v1.0" (identical "Version 2014" title page). It is still current on 2026-11-20 only in the sense that it has not yet reached its sunset date; ISTQB itself says the Foundation Agile content is now in CTFL v4.0.
- Canonical glossary URLs: https://glossary.istqb.org/en_US/term/<slug> is the pattern the glossary's own records use (each record's `slug` field: risk-based-testing, stress-testing, test-completion, testability, acceptance-criteria, exit-criteria all returned records from the API). Limitation: the rendered pages are JS-only, so a plain GET shows no term text and returns HTTP 200 for any slug; existence of a term is confirmed only through the API record. Glossary record "versions" differ per term (rbt v3, stress-testing v1, test-completion v2, testability v3, acceptance-criteria v3); no page-level date is printed.
- What cannot be settled from plain pages: the glossary term pages' own rendered text and any "last updated" shown in the browser (not visible without running the script); whether any CTFL newer than 4.0 is announced elsewhere on istqb.org (only the certifications and CTFL pages were checked).

### D.NIST, NASA, Fowler, Thoughtworks, Humble and Farley (2.6, 2.7, 2.9)

**Q4. NIST SP 800-61 Rev. 3.** (read: https://csrc.nist.gov/pubs/sp/800/61/r3/final and PDF https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf)
- Title: "Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile".
- Authors on CSRC page: Alexander Nelson (NIST), Sanjay Rekhi (NIST), Murugiah Souppaya (NIST), Karen Scarfone (Scarfone Cybersecurity). PDF cover prints "Alex Nelson"; Souppaya carries the note "Former NIST employee; all work for this publication was done while at NIST."
- Canonical URL: https://csrc.nist.gov/pubs/sp/800/61/r3/final. DOI: https://doi.org/10.6028/NIST.SP.800-61r3.
- Date: "Date Published: April 2025"; history "04/03/24: SP 800-61 Rev. 3 (Draft)", "04/03/25: SP 800-61 Rev. 3 (Final)" (so exact date 3 April 2025).
- Rev. 2 (https://csrc.nist.gov/pubs/sp/800/61/r2/final), "Computer Security Incident Handling Guide", published August 2012 (final 08/06/12): "Withdrawn on April 03, 2025. Superseded by SP 800-61 Rev. 3". The Rev. 3 PDF also says "This publication supersedes SP 800-61r2".

**Q7. Deploy versus release attribution.** Settled only to the extent of pages read; no page read credits anyone with originating the distinction.
- Thoughtworks Radar "Decoupling deployment from release" (https://www.thoughtworks.com/radar/techniques/decoupling-deployment-from-release): ring Adopt in both entries; first entry Nov 2015 (published Nov 10, 2015) with no description text on the page; second entry Apr 2016 (last updated Apr 05, 2016) with the terminology recommendation quoted in Part B. No credit or attribution is given. The page is "NOT ON THE CURRENT EDITION". So the earliest dated Radar print is Nov 2015, but the only wording readable is from Apr 2016.
- Humble and Farley, Continuous Delivery (Addison-Wesley, published Jul 27, 2010 per InformIT): chapter 10 is titled "Deploying and Releasing Applications" (TOC). Whether it draws the distinction: NOT FOUND (not readable). Sample chapter 5 uses both words but does not define a distinction between them.
- Fowler pages read, with dates: Blue Green Deployment, 1 March 2010 (talks of deployment cut-over; names Humble and Farley's forthcoming book; no distinction stated); Feature Flag bliki, 29 October 2010 (feature flags avoid "revealing a half-implemented feature on your releases"; no use of the word deployment in that sense); Continuous Delivery bliki, 30 May 2013 (separates Continuous Delivery, "able to do frequent deployments but may choose not to", from Continuous Deployment; no definition of release vs deployment); Feature Toggles article by Pete Hodgson, written Jan to Feb 2016, dated 09 October 2017: calls separating "[feature] release from [code] deployment" "the Continuous Delivery principle", i.e. attributes it to the CD literature without naming a source; Dark Launching, 29 April 2020 (uses "release the feature to the public").
- Earliest dated print in my slice that states the distinction in words: the Hodgson article (installments from 19 January 2016) and the Radar Apr 2016 text. The Radar Nov 2015 entry exists but its wording is not on the page. Whether Humble and Farley (2010) set it out cannot be settled from freely readable text. Recommendation: do not credit any person; say the distinction is a Continuous Delivery principle and cite the Radar entry and Hodgson as sources.
- ITIL 4 and SAFe wording are covered by other agents. (I noticed in the shared cache that the SAFe Release on Demand page says "releases are decoupled from the work to deploy the functionality" and the SAFe continuous deployment page says it is optimal to separate them; that is for the SAFe agent to report.)

**Q14. NIST SSDF.**
- SP 800-218 v1.1 (February 2022; https://csrc.nist.gov/pubs/sp/800/218/final) is still the page marked final. Its project page https://csrc.nist.gov/projects/ssdf does not mention v1.2.
- SP 800-218 Rev. 1 (SSDF v1.2) is an Initial Public Draft only: "Date Published: December 17, 2025", "Comments Due: January 30, 2026 (public comment period is CLOSED)", authors Harold Booth, Michael Ogata, Karen Kent, Murugiah Souppaya, Donna Dodson; DOI https://doi.org/10.6028/NIST.SP.800-218r1.ipd. Tried r1/final (HTTP 404), r1/2pd (404), r1/fpd (404), doi 800-218r1 (404). As of 2026-11-20 no final or second draft was found at these URLs; I cannot rule out a later publication elsewhere.
- Practice identifiers: all 15 cited in 2.6 exist in v1.1 with the wording shown in Part B. The v1.2 IPD keeps these identifiers (PO.1.2, PO.3.3, PW.1.1, PW.2.1, PW.6.1, PW.7.1, PW.7.2, PW.8.1, PW.8.2, PS.1.1, PS.3.1, PS.3.2, RV.1.x to RV.3.x) and adds tasks PO.6.1 to PO.6.3 (new practice PO.6). Minor wording change in the IPD: PW.1.1 reads "(e.g., threat modeling, attack modeling, attack surface mapping)". Cite v1.1 as final; mention v1.2 only as a draft.

### D.Google SRE and engineering, OWASP (2.8, 2.10)

**SRE book chapter bylines (all read directly on sre.google, 2026-11-20).** The byline is printed at the top of each chapter, after the heading. Book/editor details are printed on the preface page and in each page footer.

| Chapter | URL | Printed byline | Printed chapter editor(s) | Page footer |
|---|---|---|---|---|
| Ch. 8 Release Engineering | https://sre.google/sre-book/release-engineering/ | "Written by Dinah McNutt" (worklist recall confirmed) | "Edited by Betsy Beyer and Tim Harvey" | Copyright © 2017 Google, Inc. Published by O'Reilly Media, Inc. Licensed under CC BY-NC-ND 4.0 |
| Ch. 6 Monitoring Distributed Systems | https://sre.google/sre-book/monitoring-distributed-systems/ | "Written by Rob Ewaschuk" (confirmed) | "Edited by Betsy Beyer" | same, 2017 |
| Ch. 11 Being On-Call | https://sre.google/sre-book/being-on-call/ | "Written by Andrea Spadaccini" (the text extract shows "Spadaccini56"; 56 is a footnote marker: "An earlier version of this chapter appeared as an article in ;login: (October 2015, vol. 40, no. 5)") | "Edited by Kavita Guliani" | same, 2017 |
| Ch. 14 Managing Incidents | https://sre.google/sre-book/managing-incidents/ | "Written by Andrew Stribblehill" (extract shows "Stribblehill78"; 78 is a footnote marker: earlier version in ;login: April 2015, vol. 40, no. 2) | "Edited by Kavita Guliani" | same, 2017 |
| Workbook Ch. 9 Incident Response | https://sre.google/workbook/incident-response/ | "By Jennifer Mace, Jelena Oertel, Stephen Thorne, and Arup Chakrabarti (PagerDuty) with Jian Ma and Jessie Yang" | none printed | Copyright © 2018 Google, Inc. Published by O'Reilly Media, Inc. Licensed under CC BY-NC-ND 4.0 |
| Workbook Ch. 16 Canarying Releases | https://sre.google/workbook/canarying-releases/ | "By Alec Warner and Štěpán Davidovič with Alex Hidalgo, Betsy Beyer, Kyle Smith, and Matt Duftler" (worklist recall confirmed) | none printed | 2018 footer |
| Workbook Ch. 10 Postmortem Culture (existing key) | https://sre.google/workbook/postmortem-culture/ | "By Daniel Rogers, Murali Suriar, Sue Lueder, Pranjal Deo, and Divya Sudhakar with Gary O'Connor and Dave Rensin" (matches existing entry) | none printed | 2018 footer |

**Book-level details.**
- First-edition SRE book, preface (https://sre.google/sre-book/preface/): the printed citation example reads "Site Reliability Engineering, edited by Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (O'Reilly). Copyright 2016 Google, Inc., 978-1-491-92912-4." The editors are also listed on https://sre.google/books/ ("Edited by: Betsy Beyer, Chris Jones, Jennifer Petoff and Niall Richard Murphy"). The individual chapter pages carry a 2017 copyright footer, which differs from the 2016 in the preface; the worklist's "O'Reilly 2016" matches the preface only.
- Workbook preface (https://sre.google/workbook/preface/): "The Site Reliability Workbook, edited by Betsy Beyer, Niall Richard Murphy, David K. Rensin, Kent Kawahara, and Stephen Thorne (O'Reilly). Copyright 2018 Google LLC, 978-1-492-02950-2." The books page lists the same five editors. Worklist "Workbook 2018" confirmed.
- Not in the worklist but relevant: https://sre.google/books/ now also lists "Site Reliability Engineering, 2nd Edition" ("completely rewritten"; editors Betsy Beyer, Chris Jones, Christof Leng, David Huska, Jennifer Petoff, Niall Richard Murphy) as a separate book. The chapter URLs under /sre-book/ are the first edition (their table of contents is the 34-chapter first-edition list). The page does not print a publication year for the second edition. Entries should therefore say "first edition".
- Tab (HTML title) text on these pages is SEO text and in some cases does not match the chapter (monitoring chapter tab: "Google SRE: SRE Responsibilities and Management Frameworks"; workbook incident-response tab: "Google SRE - Root Cause Analysis for Probing Incident"). Use the on-page "Chapter N - Title" heading as the title.

**Google engineering practices bylines/dates.** Neither https://github.com/google/eng-practices/blob/master/review/reviewer/looking-for.md nor .../developer/small-cls.md (read from raw.githubusercontent.com, same files) prints an author or a date. The repository README (https://raw.githubusercontent.com/google/eng-practices/master/README.md) is titled "Google Engineering Practices Documentation", attributes the material to Google ("These documents represent our collective experience"), and says the documents are licensed under CC-By 3.0. Google's rendered copy (google.github.io/eng-practices) also prints no author/date; its HTTP Last-Modified header is Thu, 19 Sep 2024 (a site-deploy timestamp, not a printed date). Use author "not printed", org "Google", date "not printed". The CL page title on the rendered site is "Small CLs | eng-practices".

**ASVS/WSTG version facts.**
- ASVS: the Frontispiece (https://raw.githubusercontent.com/OWASP/ASVS/master/5.0/en/0x01-Frontispiece.md) prints "Version 5.0.0, May 2025", "Copyright © 2008-2025 The OWASP Foundation", CC BY-SA 4.0, project leads Daniel Cuthbert, Elar Lang, Josh C Grossman. The repository README (https://raw.githubusercontent.com/OWASP/ASVS/master/README.md) says "Latest Stable Version - 5.0.0 ... The latest stable version is version 5.0.0 (dated May 2025)" and "The next release target will be a patch release, version 5.0.1". So the existing entry's date 2025-05 and 5.0.0 are supported. Limits: this is the master-branch README as read on 2026-11-20; a tag v5.0.1 was not found at raw.githubusercontent.com (HTTP 404 for .../v5.0.1/README.md), which is weak evidence only because I cannot list tags or releases (github.com is not readable). The chapter file itself (0x03) prints no version or date in its own text apart from "as of version 5.0.0 of this standard" in the identifier example.
- WSTG: the README (https://raw.githubusercontent.com/OWASP/wstg/master/README.md) says "We are currently working on release version 5.0" and "For the last stable release, check release 4.2" (link to tag v4.2; online copy at owasp.org/www-project-web-security-testing-guide/v42/). The document About page (document/1-About/README.md) prints "Copyright © 2026 The OWASP® Foundation" and a welcome note about a release "introduces numerous updates", which is draft 5.0 text on master. Raw files exist at tag v4.2 (HTTP 200) and not at tag name v5.0 (HTTP 404, tag naming unknown). What cannot be settled: whether a v5.0 release has been published since, because the GitHub Releases page is not readable by plain GET (github.com refuses) and I did not use any other site. The only evidence is the README statement, which names 4.2 as the last stable release. The worklist claim (4.2 stable, 5.0 in development) is therefore supported as "per the master-branch README on 2026-11-20".
- OWASP cheat sheet pages print no author or date in their text; the footer credits "Cheat Sheets Series Team", CC BY-SA 4.0. The Last-Modified header (19 Nov 2026) is a site-build timestamp and should not be used as a publication date.

### D.Other public sources (2.11)

**10 (my items)**
- SEI ATAM document: the drafted URL (https://www.sei.cmu.edu/documents/1186/1998_005_001_16646.pdf) is CMU/SEI-98-TR-008, "The Architecture Tradeoff Analysis Method", July 1998, by Rick Kazman, Mark Klein, Mario Barbacci, Tom Longstaff, Howard Lipson, Jeromy Carriere (cover page of the PDF; confirmed by https://www.sei.cmu.edu/library/the-architecture-tradeoff-analysis-method/, a URL I tried on the SEI site, not one linked from a page). The definitive report is CMU/SEI-2000-TR-004 "ATAM: Method for Architecture Evaluation", August 1, 2000, by Rick Kazman, Mark Klein, Paul Clements (https://www.sei.cmu.edu/library/atam-method-for-architecture-evaluation/; PDF https://www.sei.cmu.edu/documents/629/2000_005_001_13706.pdf, cover confirms authors and "August 2000"). The claim "scenarios are prioritised" is supported only by the 2000 report. Recommendation: cite the 2000 report for the method and its prioritisation, or keep 1998 only for the "structured technique for understanding tradeoffs" wording.
- arXiv 2305.15778: title "Automatic Root Cause Analysis via Large Language Models for Cloud Incidents"; 18 authors listed in Part A (first: Yinfang Chen; last: Tianyin Xu). Venue not printed on arXiv page.
- Ahmed et al.: Toufique Ahmed, Supriyo Ghosh, Chetan Bansal, Tom Zimmermann, Xuchao Zhang, Saravan Rajmohan; ICSE 2023, May 2023 (Microsoft Research publication page).
- Requirements-ambiguity study: Bashir, Ferrari, Khan (record: Muhammad Abbas Khan), Strandberg, Haider, Saadatmand, Bohlin. Venue: 41st International Conference on Software Maintenance and Evolution (ICSME 2025), September 2025, pp. 620-631, DOI 10.1109/ICSME64153.2025.00063, all from the university publication record https://www.ipr.mdu.se/publications/7221- (the PDF itself prints no venue or year). I did not read the DOI target (IEEE).
- Threat Modeling Manifesto: authorship = 15-person working group listed on the page (names in Part A), with thanks to Loren Kohnfelder and Sheila Kamath for technical edit review. Publication date: NOT printed on the page or the linked PDF (https://github.com/Threat-Modeling-Manifesto/threat-modeling-manifesto/releases/download/1/threat-modeling-manifesto.pdf). The only dates on the page are references to 2020 and 2021 talks. A date cannot be settled from readable pages. The release asset's HTTP Last-Modified of 7 Dec 2021 is file metadata, not a publication date.

**11 (Rath 2018)**: dl.acm.org and doi.org both returned HTTP 403, so the ACM record was not read. Established from the authors' own arXiv preprint (a substitute, labelled): authors Michael Rath, Jacob Rendall, Jin L.C. Guo, Jane Cleland-Huang, Patrick Mäder (arXiv page spells "Maeder"); affiliations Technical University Ilmenau, University of Notre Dame, McGill University; ICSE'18: 40th International Conference on Software Engineering, Gothenburg, Sweden, May 27-June 3, 2018; 12 pages; ACM ISBN 978-1-4503-5638-1/18/05; DOI https://doi.org/10.1145/3180155.3180207 (printed in the PDF's ACM Reference Format and as "Related DOI" on https://arxiv.org/abs/1804.02433). The DOI in the worklist matches. Page numbers in the ACM proceedings are not established.

**12 (Reinertsen)**: No authoritative record was readable. Tried: reinertsenassociates.com and celeritaspub.com / celeritaspublishing.com (no usable connection: TLS or DNS failure), Library of Congress catalogue and loc.gov search by ISBN 9781935401001 (an ISBN I supplied from memory; the catalogue page returned no text and loc.gov JSON returned no matching record), WorldCat (HTTP 429), Open Library (connection reset). Only Goodreads was readable: title "The Principles of Product Development Flow: Second Generation Lean Product Development", author Donald G. Reinertsen, 294 pages hardcover, "First published May 1, 2009". Publisher (Celeritas Publishing) and the ISBN are therefore unconfirmed by any page I read. "Weighted shortest job first" and the cost-of-delay quotation: not checkable (book text not read; neither phrase is on the Goodreads page). The ISBN and the publisher name came from memory and must not be recorded without a readable source. A session with access to the author's/publisher's site or a library catalogue record is needed.

## E. Corrections to apply to the drafted entries

### E.SAFe sources (worklist 2.1) and AI-Native SAFe

- ALL SAFe keys: accessed -> 2026-11-20. author "not printed", org "Scaled Agile, Inc.". Dates must be the "Last Update" printed on each page where present (list in Part A); where none is printed in the readable text, say "not printed".
- safe-framework: keep date 2025-02-25 (confirmed). No version label exists on the page; do not add "SAFe 6.0".
- safe-configurations: title is "SAFe 6.0 Configurations"; date 2025-09-03 confirmed; URL works (not retired). Claim #2 must be dropped from this source and cited to https://framework.scaledagile.com/large-solution (H1 "Large Solution SAFe", last update 2022-12-05): "for enterprises building large and complex solutions that do not require portfolio concerns".
- safe-art: claims #3 and #4 cannot be cited to this page (login wall). Re-cite: Business Owners -> /business-owners/ ("return on investment (ROI), governance, and compliance"; the phrase "fitness for use" appears only on the 2022 Essential SAFe page); Product Management -> /product-management/ ("desirable, viable, feasible, and sustainable"). Word order differs from the draft (draft: desirable, feasible, viable, sustainable).
- safe-agile-teams: claims #2, #3, #4 not on this page; re-cite to /team-backlog/, /product-owner/, /scrum-master-team-coach/ (or /essential-safe/ for "content authority" and "remove impediments", noting its 2022 date), or drop.
- safe-lpm: it is a legacy competency article that itself says the competency thinking has evolved; the page does call LPM a "core competency". Prefer safe-lpm-discipline for current wording. Drop claim #2 from this entry.
- safe-lpm-discipline: fine; date 2025-03-31; URL confirmed; H1 is "Lean Portfolio Management" (tab title adds "Discipline").
- safe-strategic-themes: reword #1 to "connect the enterprise strategy to a portfolio" (not "portfolio vision"); drop #2 (decision criteria in the portfolio backlog is not in readable text).
- safe-portfolio-backlog: drop #3 (epic state names not readable). Keep #1, #4; re-cite #2 to the LPM discipline page. Date 2025-03-11.
- safe-wsjf: reword #1: "relative cost of delay divided by the relative job duration" (page says duration, with job size as an input). Title H1 "Weighted Shortest Job First" (tab "Extended Guidance - WSJF"). Reinertsen is credited as an epigraph attribution only.
- safe-requirements-model: page exists; only the opening paragraph is readable. Keep only: the model expresses system behaviour as Epics, Capabilities, Features, Stories, NFRs. Drop #2-#4 or cite /features-and-capabilities and /story.
- safe-pi-planning: reword #2 to "committed PI objectives" (the "committed or uncommitted" wording is from the glossary entry for PI Objectives); #3: cite glossary "ART Planning Board" for milestones. Date 2026-03-15. Note the page itself says "typically a 2-day event" and "every 8-12 weeks".
- safe-inspect-and-adapt: keep this key, drop safe-inspect-adapt. Date 2026-03-20. Reword #4 to "structured problem-solving workshop" (add "root-cause" only when citing the facilitator's guide). No AI-Native note on this page; the replacement is stated on the Sense and Respond and PI Outcome Planning pages.
- safe-ia-facilitators-guide: title as printed "SAFe Inspect and Adapt Facilitator's Guide" (the phrase "Purpose, Intent, and Outcomes" is its first section heading, not part of the title); no date printed (March 2026 comes only from the upload path); drop the six-step claim; keep "typically facilitated by the Release Train Engineer (RTE)" and the three-part agenda with approximate times (1.0 / 0.5 / 2.0 hr).
- safe-iteration-planning: date 2026-03-18; "approximately 90 minutes for a two-week iteration" is printed. Claim #2 should cite /iterations/ ("standard, fixed-duration timebox") instead.
- safe-iteration-review: the glossary_term URL works but its wording ("inspects the iteration increment, assesses progress, and adjusts the team backlog") differs from the claim. Prefer https://framework.scaledagile.com/iteration-review/ (H1 "Iteration Review", last update 2026-03-18): "allows the Agile Team to showcase their accomplishments, receive feedback, and collaboratively determine next steps".
- safe-team-backlog-refinement: reword #1 to "an event that helps Agile Teams clarify and prepare upcoming stories and features"; drop "continuously" and "sized".
- safe-built-in-quality: keep only #1. #2 (Definition of Done) cite the glossary: "The Definition of Done specifies the requirements for completeness of a work product or increment of value." Drop #3 (five domains/dimensions, names unreadable; page says "domains") and #4. SAFe does not define a Definition of Ready: the glossary has no entry; two articles use the abbreviation DoR in passing (Part D notes).
- safe-continuous-integration: use https (resolves 200); http also 200 with no redirect.
- safe-release-on-demand: drop #2 (activity names unreadable). Date 2025-02-25.
- safe-glossary: System Demo page URL is https://framework.scaledagile.com/system-demo/ (add as a key if needed); no date printed on glossary.
- safe-portfolio-flow: reword to the page's own definition ("continuous flow of new epics to Solution Trains and ARTs"); drop the Kanban/capacity wording or cite it to /portfolio-backlog/.
- safe-essential: page is a legacy 2022 article (last update 2022-11-30); optional; if kept, cite as such, not as current guidance.
- safe-whats-new: rewrite all four claims. Correct statements: it records that AI-Native SAFe was "officially introduced" in June 2026 and iteratively released; it does NOT print 2026-06-23, "fully supported", or a Core SAFe version/date. Use safe-framework-home and safe-ai-native-launch-post for the Core/AI-Native relationship; use "unveiled 16 June 2026" (launch post) and "officially released 15 September 2026" (Summit recap). Page prints "Last Update: 9 April 2026" despite containing later entries; cite it as "page prints last update 9 April 2026; entries run to August 2026".
- safe-ai-native-sense-and-respond: URL confirmed; date 2026-07-28; title "Sense and Respond"; claim #2 should quote "also includes the activities formally present in the System Demo". Do not say Customer Demos replace System Demo.
- Add (optional) keys: safe-ai-native-pi-outcome-planning, safe-ai-native-launch-post, safe-ai-native-session4-post, safe-ai-native-summit-recap, safe-framework-home (entries in Part A).
- oasis-soa-rm: title as printed "Reference Model for Service Oriented Architecture 1.0" (tab: "... v1.0"); editors C. Matthew MacKenzie, Ken Laskey, Francis McCabe, Peter F Brown, Rebekah Metz; date "12 October 2006". Note the exact definition is in section 1.1 and the abstract wording differs slightly (the abstract adds "within a service-oriented environment").

### E.SAFe closed allow-list (worklist section 3)

- safe-continuous-integration: use https://framework.scaledagile.com/continuous-integration/ (scheme was http in the worklist).
- safe-iteration-review: prefer https://framework.scaledagile.com/iteration-review/ (tab "Extended Guidance - Iteration Review", H1 "Iteration Review", 18 March 2026) over the glossary_term stub; claim #1 ("show results, get feedback, adjust backlog") fits the full page, not the stub.
- safe-epic / safe-portfolio-backlog claim #2 ("epics describe the strategic initiatives the portfolio is responsible for"): not on the page. Page says "Portfolio epics are large (and typically cross-cutting initiatives) managed through the portfolio Kanban." Reword.
- safe-lpm-discipline: tab title "Lean Portfolio Management Discipline", H1 "Lean Portfolio Management", last update 31 March 2025. Claim #1 ("Lean budgets fund value streams instead of projects") is worded exactly only on /lean-budgets/ and the glossary; the discipline page says "Lean budgets provide funding for value streams aligned with the business strategy and current strategic themes."
- safe-strategic-themes claim #2 (decision criteria in the portfolio backlog): not found in readable text; claim #1 should say "connect the enterprise strategy to a portfolio", not "portfolio vision".
- Role definitions (Product Management, Business Owners, Product Owner, Scrum Master/Team Coach) in safe-art and safe-agile-teams: the ART page and the Agile Teams page name the roles but do not define them in the readable text. Wording on the role pages differs from the worklist: Product Management "desirable, viable, feasible, and sustainable solutions" (not "feasible, viable ... products"); Business Owners "return on investment (ROI), governance, and compliance" (not "fitness for use"); Product Owner "ensuring that the team backlog is aligned with customer and stakeholder needs" (not "content authority"); SM/TC "servant leader and coach ... facilitates team events and processes". The ART page Key Takeaways name the four roles "Product Management, a System Architect, a Release Train Engineer, and Business Owners".
- safe-built-in-quality claim #3 (other agent's slice, flagged because I read the page): the page says "SAFe applies Built-in Quality across five key domains", not "five dimensions"; the domain names are in the login-gated part.
- safe-planning-interval: date 2025-02-25 confirmed ("Last Update: 25 February 2025"); the page says "A Planning Interval is typically an 8 to 12-week timebox" and says PI Planning and Inspect and Adapt are ART events ("A series of ART events, including PI Planning and Inspect and Adapt, ensures successful PI execution."); the system demo is not named on the readable part of that page.
- safe-configurations: URL https://framework.scaledagile.com/safe-6-0-configurations is live; title "SAFe 6.0 Configurations"; "Last Updated: 3 September 2025" matches the worklist; page lists "Full SAFe, Essential SAFe, Large Solution SAFe, Portfolio SAFe".
- safe-whats-new: the footer date "Last Update: 9 April 2026" disagrees with the page's own August 2026 entries; do not cite 9 April 2026 as the latest update.
- safe-glossary claim #1: System Demo page is https://framework.scaledagile.com/system-demo/ (last update 18 March 2026); glossary wording "The System Demo provides stakeholders an integrated view of new features for the most recent iteration delivered by all the teams on the ART." Glossary Lean Budgets entry exists; Definition of Done entry exists (no page link); Iteration Goals entry exists.
- "Also check" terms: Definition of Ready not confirmed in readable SAFe text; "Program Board" is documented by SAFe itself as pre-6.0 wording (10 June 2024 article); "Innovation and Planning iteration", "ART Sync" and "Solution Demo" ARE current SAFe terms (so any statement that the site must not use them needs rewording to "not adopted by this site").

### E.DORA (2.2)

- dora-ai-capabilities: title "DORA AI Capabilities Model"; add date "last updated 2025-11-25"; drop claim #2 from this key (cite dora-ai-capabilities-intro instead); claim #1 can cite only "seven capabilities" here; names come from dora-ai-capabilities-intro.
- dora-ai-capabilities-intro: title as printed is "Introducing the DORA AI Capabilities Model: 7 keys to succeeding in AI-assisted software development"; tab title differs (see entry). Authors and date confirmed.
- dora-ai-capabilities-impact: URL final has no trailing slash. Authors and date confirmed.
- dora-small-batches, dora-wip-limits: titles "Working in small batches", "Work in process limits". Dates as above.
- dora-2024-highlights: confirmed title/date/authors. Percentages present on the page: 25% increase in AI adoption associated with +7.5% documentation quality, +3.4% code quality, +3.1% code review speed; "decrease in delivery throughput by 1.5%" and "reduction in delivery stability by 7.2%"; more than 75 percent rely on AI for at least one daily responsibility; 39% little or no trust. Page states the 1.5% and 7.2% as estimates tied to "AI adoption increased"; it does not repeat "per 25%" next to them. Say so if cited.
- dora-2024-report: reword claim: AI adoption negatively impacts delivery stability and throughput; small batch sizes and robust testing remain crucial. Drop "larger batch sizes suggested".
- dora-2025-report: URL changes to https://dora.dev/research/2025/dora-report/ (old URL redirects). Reword claim to the amplifier statement only; move throughput/instability claims to dora-2025-announcement. Note #2 of the announcement: throughput relationship is positive in 2025 and stability relationship is negative; do not write "higher instability" as a throughput pairing without that.
- dora-metrics: change URL to https://dora.dev/guides/dora-metrics/ (title "DORA's software delivery performance metrics", Nathen Harvey, last updated 2026-01-05). Names: change fail rate, failed deployment recovery time are correct current names. Note: failed deployment recovery time is a throughput metric on the current page, not instability. Add the fifth metric deployment rework rate. Optionally add dora-metrics-history.
- dora-customer-feedback: reword to "part of a group of lean product-management capabilities that together help predict delivery and organisational performance".
- dora-streamlining-change-approval: claim #3 should read: the page treats regulatory requirements (segregation of duties) as satisfiable by peer review; it does not discuss a mandated external approver.
- dora-continuous-delivery: confirmed; keep as optional.
- No duplicate keys in this slice. No entry should be dropped.

### E.Scrum, agile and requirements practice (2.3)

- scrum-guide-2020: keep key (merge `scrum-guide` into it). Title "The 2020 Scrum Guide" (H1 prints "The 2020 Scrum Guide | TM"; tab "Scrum Guide | Scrum Guides"). Author "Ken Schwaber and Jeff Sutherland". Date "November 2020". URL unchanged, no redirect. All 13 claims hold as worded. Claim #8: say "does not use the term Definition of Ready" and cite "deemed ready for selection"; do not say the Guide never used "Ready": the 2013 edition did, per scrum-guide-revisions (new optional key, https://scrumguides.org/revisions.html).
- agile-alliance-dor: no author, no date printed (record "not printed"). Reword claim #1: the page does not say "checklist" and does not mention the Scrum Guide; the "not in the Scrum Guide" point rests on the Guide itself. Claim #2 text is on the page but unattributed; it is Agile Alliance's own hedged statement, cite it as such. Claim #3: say the page names ETVX (1985, "A programming process architecture") as a precursor; drop "restates entry and exit criteria".
- agile-alliance-dod: no author or date printed. Claim #1 reword to "a list of criteria that must be met before a product increment is considered done"; drop "intrinsic quality standards".
- overeem-dor, kronfalt-ready-2008, sutherland-ready-2009, radice-etvx-1985, schwaber-beedle-2001, schwaber-scrum-1995, cooper-stage-gate: nothing confirmed; do not publish citations that depend on them (title, byline, date all unconfirmed). Either find a readable host or drop them. For kronfalt-ready-2008 and sutherland-ready-2009 the hosts did not resolve at all (the Kronfält host is a blogspot subdomain; the original may have moved). Do not state "Kronfält, October 2008" or "Sutherland, 4 July 2009" as facts; the Agile Alliance page supports only "first formal description seems to be from October [2008]".
- wake-invest: title, author and date confirmed as drafted. Add venue "XP123 (author's site)". Date "17 August 2003". Optionally add "2011-02-16 postscript".
- agile-manifesto-principles: author field: do not use "Kent Beck et al."; the principles page prints no byline. Use "not printed" or cite "the authors of the Agile Manifesto (17 signatories listed at agilemanifesto.org)". Date not printed on the page; (c) 2001 is on the Manifesto home page. The principle is the twelfth statement, but the page does not number them.
- keep-a-changelog: URL: root https://keepachangelog.com/ is a redirect stub (client-side) to /en/1.1.0/; use https://keepachangelog.com/en/1.1.0/ (or /en/2.0.0/, "Published on June 7th, 2026"). Version-dependent: the phrase "machines can draft, humans curate" is only on /en/2.0.0/ (it says: "machines can draft, but humans curate"); the git-log tagline is only on 1.1.0; SemVer: 1.1.0 "Mention whether you follow Semantic Versioning", 2.0.0 "You do not have to use Semantic Versioning" - drop "recommends Semantic Versioning". Claim #3 reword: "six types of change under which notable changes are grouped". Claim #4: "created and maintained by Olivier Lacan" is on the page; "first published 2014" is only inferred from the page's changelog (0.0.1, 2014-05-31).
- semver: existing entry confirmed. Title "Semantic Versioning 2.0.0"; author Tom Preston-Werner (originally authored by); no date printed on the page.
- Date fields: replace all 2026-10-06 access dates with 2026-11-20.
- Differences between worklist and pages: (1) the worklist's "v2026.1, January 2026" Expansion Pack label is not on the page read; (2) the Scrum Guide revision page's 2013 "Ready" statement is not in the worklist; (3) the Keep a Changelog 2.0.0 revision (2026-06-07) is not in the worklist.

### E.ISO/IEC/IEEE and ISTQB (2.4, 2.5)

- iso-12207: keep key only if later read; for now title/author/date/edition unconfirmed. Drop claims #1, #2, #3 and the 2017 or 2026 dates from any page until read; URL 90219 is unverified (inferred), 63712 is the 2017 URL as given. Entry should be dropped from references if no readable source appears.
- iso-14764, iso-25010, iso-29148, iso-24765, iso-15288, iso-42010, iso-29119-3: all NOT FOUND (not readable). Titles, editions, dates, authors unconfirmed; drop every claim or leave the entry uncited. iso-29119-3 catalogue number 79429 is unverified.
- iso-29119-1 (existing): not re-confirmed. Keep as is but update accessed only if the author accepts "not re-read"; flag that the ISTQB glossary record for risk-based testing cites the 2013 edition of 29119-1, while the existing entry is the 2022 edition (a discrepancy to be aware of; not a contradiction of the entry).
- istqb-rbt (existing): wording confirmed; add "corresponding" ("based on corresponding risk types and risk levels"), note term version 3, update accessed to 2026-11-20, mention the glossary page is JS-rendered. Existing title "risk-based testing" and author line fine.
- istqb-ctfl-4: set title "Certified Tester Foundation Level (CTFL) v4.0" (H1; tab title "... v4.0 Overview"); URL final is https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/ (www.istqb.org redirects to istqb.org); add canonical syllabus URL https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf, version v4.0.1 dated 2024-09-15. The test-levels and confirmation/regression claims are supported by the syllabus PDF (sections 2.2.1 and 2.2.3), not by the overview page itself; the overview page lists the syllabus areas only (Test Levels & Test Types).
- istqb-stress-testing: supported; add term version 1, reference ISO/IEC/IEEE 24765 (2017).
- istqb-test-completion: reword claim #1 as read. Drop claim #2 from this entry or point it to a new key istqb-exit-criteria (https://glossary.istqb.org/en_US/term/exit-criteria, "The set of conditions for officially completing a defined task.").
- istqb-testability: reword to the current text ("for a component or system"; "those test conditions"). Add see-also maintainability only if needed.
- istqb-acceptance-criteria: REWORD. The drafted claim ("Exit criteria a component or system must satisfy to be accepted by a user, customer or authorised entity") is the old v1/v2 wording. Current v3: "The criteria that a work product must satisfy to be accepted by the stakeholders." Use the v3 wording or drop.
- istqb-agile-tester-2014: title as printed: "Certified Tester Foundation Level Extension Syllabus Agile Tester, Version 2014" (running header "Foundation Level Syllabus – Agile Tester"); date 30 Sep 2014; URL redirects to https://astqb.org/assets/documents/ISTQB-Foundation-Agile-Syllabus.pdf (or use ISTQB's own copy https://istqb.org/wp-content/uploads/2024/11/ISTQB-CTFL-AT_Syllabus_v1.0.pdf). Add a currency caveat: ISTQB announces CTFL-AT exams and training sunset on 6 May 2027 (English) and 6 November 2027 (non-English), superseded in scope by CTFL v4.0 and CTAL-AT v2.0. Both claims are supported.
- No duplicate keys in this slice. No entry to drop on grounds of being wrong, except the unreadable ISO entries noted above.

### E.NIST, NASA, Fowler, Thoughtworks, Humble and Farley (2.6, 2.7, 2.9)

- nist-800-61r3: URL confirmed. Authors: Alex Nelson, Sanjay Rekhi, Murugiah Souppaya, Karen Scarfone (CSRC lists "Alexander Nelson"). Date: April 2025 (3 April 2025). Add DOI. Rev. 2 withdrawn 3 April 2025.
- nist-ssdf: keep v1.1 as the cited version; note the Rev. 1 IPD (17 Dec 2025, comments closed 30 Jan 2026) and that no final was found. The existing note is correct.
- nist-ir-8397: add title "Guidelines on Minimum Standards for Developer Verification of Software"; byline confirmed (Paul E. Black, Barbara Guttman, Vadim Okun); list order confirmed; prefer URL https://csrc.nist.gov/pubs/ir/8397/final (doi.org also resolves).
- nist-800-53b and nist-800-53: confirmed. Date "September 2020 (includes updates as of Dec. 10, 2020)"; Release 5.2.0 (27 Aug 2025) exists. 
- nasa-swe-052: use the redirected URL; cite the handbook as NASA-HDBK-2203 (cover says 2203B, approved 8 March 2022; history log calls the same date Revision C; wiki labelled "Ver D" for NPR 7150.2D). Requirement applies by software class.
- tw-radar-decoupling: ring Adopt, first Nov 2015 (Nov 10, 2015), last updated Apr 5, 2016; claim #1 wording comes only from the Apr 2016 entry. Reword: do not say the 2015 entry contained this text. No credit is given on the page.
- fowler-blue-green: date 1 March 2010 (update 2015-06-05). fowler-canary-release: byline Danilo Sato, 25 June 2014 confirmed. fowler-dark-launching: Martin Fowler, 29 April 2020. fowler-test-pyramid: 1 May 2012. fowler-given-when-then: 21 August 2013. fowler-selftesting: 1 May 2014. fowler-ci: 18 January 2024. fowler-deployment-pipeline: 30 May 2013 confirmed.
- fowler-feature-toggles: URL confirmed; author Pete Hodgson; printed date 09 October 2017 (not 2016/2017 guess); the series was first published January to February 2016. Reword claim #3: "remove after full rollout" is not stated; say teams should proactively remove flags no longer needed, release toggles are short-lived, a few ops toggles are long-lived kill switches. The bliki URL FeatureToggle.html redirects to FeatureFlag.html (29 October 2010).
- fowler-evodb: date May 2016 (complete rewrite; original January 2003).
- bockeler-sdd: date 15 October 2025.
- humble-farley-cd: published Jul 27, 2010 (copyright 2011 also printed). Chapter 7 title is "Commit Testing Stage" per the publisher TOC (drop "The Commit Stage"); chapter 5 is "Anatomy of the Deployment Pipeline" and contains the "Only Build Your Binaries Once" heading. Drop or mark unverified: claim #3 phrase "triggered the moment a change is introduced" and claim #6 (chapter 10 distinction). Do not state that chapter 10 draws the deploy/release distinction.

### E.Google SRE and engineering, OWASP (2.8, 2.10)

- **sre-book-release-engineering** (keep this key; drop the duplicate sre-release-engineering): title "Release Engineering"; add author "Dinah McNutt" (confirmed); say first edition, chapter 8; org Google / O'Reilly; date as printed (page footer 2017, preface citation 2016). **Reword claim #2**: the chapter does not describe an "incubation period"; replace with: rollouts can update all jobs at once or go to "successive clusters over a period of several hours", "starting in one cluster and expand exponentially", and sensitive infrastructure rollouts may extend "over several days". Claims #1, #3, #4 are fine as drafted. Do not use the worklist's editor list for the chapter; the chapter's own editors are Betsy Beyer and Tim Harvey.
- **sre-workbook-canarying**: author confirmed "Alec Warner and Štěpán Davidovič, with Alex Hidalgo, Betsy Beyer, Kyle Smith, and Matt Duftler" (not just "with others"); Workbook chapter 16, 2018.
- **sre-book-monitoring**: author confirmed Rob Ewaschuk; chapter 6; editor Betsy Beyer. Do not use the tab title.
- **sre-book-being-on-call**: author Andrea Spadaccini (chapter 11; edited by Kavita Guliani). **Reword claim #1**: replace "diagnose, mitigate, fix or escalate" with "triage the problem and work toward its resolution, possibly involving other team members and escalating as needed". Claim #2 fine.
- **sre-book-managing-incidents**: author Andrew Stribblehill (chapter 14; edited by Kavita Guliani). **Reword claim #1**: the chapter's roles are incident command, operational work (Ops lead), communication, and planning, not "communications lead". If "communications lead" wording is wanted, cite the workbook chapter (IC, CL, OL). Claim #2 fine.
- **sre-workbook-incident-response**: author "Jennifer Mace, Jelena Oertel, Stephen Thorne, and Arup Chakrabarti (PagerDuty), with Jian Ma and Jessie Yang"; Workbook chapter 9; roles named there are Incident Commander, Communications Lead and Operations (Ops) Lead; note it includes one PagerDuty case study.
- **google-sre-postmortem** (existing): title, author, URL correct; only the accessed date changes (2026-11-20). Optionally add "Workbook chapter 10, 2018". Both claims supported.
- **google-agentic-sre**: title to use is the on-page H1 "AI in SRE: Where and how Google is deploying agentic AI to improve operations"; the tab title/slug title "How Google SRE is using agentic AI to improve operations" differs. Authors, titles and date (May 28, 2026) confirmed. All five claims supported. Note the post links a whitepaper "AI in SRE Practice: Moving Beyond Automation at Google" which was not read.
- **google-eng-practices-review**, **google-eng-practices-small-cls**: author "not printed", date "not printed", org "Google (google/eng-practices)", license CC-By 3.0 per README. All claims supported. Optionally record the rendered-site URLs. Use the github.com blob URL as the stored URL only if you accept that the reader cannot open it without a browser; the file text was read from raw.githubusercontent.com.
- **petrovic-mutation**: nothing could be verified (HTTP 403). Do not ship as a source until read; see Part F.
- **owasp-asvs** (existing): URL and title ("What is the ASVS?") correct; the existing title suffix "(OWASP Application Security Verification Standard 5.0.0)" is the drafter's addition, not on the chapter page; keep only if a decision allows an added qualifier, else use "What is the ASVS?" and put "ASVS 5.0.0" in the date/edition field ("Version 5.0.0, May 2025", printed on the Frontispiece). Existing note matches the text. Claims #1 to #4 all supported. Add that the project leads are Cuthbert, Lang, Grossman if an author name is wanted.
- **owasp-wstg**: **Drop or reword claim #1's "vendor-neutral"**: not stated in the README; use "community-created" instead. Title as printed on the README H1: "OWASP Web Security Testing Guide". Date/edition: "last stable release 4.2; 5.0 in progress, per master README read 2026-11-20". The URL https://github.com/OWASP/wstg was not fetched itself (README read from raw.githubusercontent.com).
- **owasp-secrets-management**: title "Secrets Management Cheat Sheet" (H1; tab "Secrets Management - OWASP Cheat Sheet Series"); author/date not printed; both claims supported.
- **owasp-threat-modeling-cs**: title "Threat Modeling Cheat Sheet"; author/date not printed; claim supported with the exact wording "application decomposition, threat identification and ranking, mitigations, and review and validation".

### E.Other public sources (2.11)

- itil4-deployment-management, itil4-release-management: say "PeopleCert" (page footer "(c) 2026 PeopleCert"; AXELOS not mentioned). Reword claims as "PeopleCert's course description says ..."; do not present them as ITIL practice-guide purpose statements. Do not claim the pages show ITIL 4 lists release and deployment as separate practices (only separate certifications).
- twelve-factor-config / twelve-factor-parity: tab title and H1 are "The Twelve-Factor App"; use "III. Config" / "X. Dev/prod parity" as entry titles. Add "last updated 2017". No other correction.
- threat-modeling-manifesto: add authors (15 names); no date can be given. Write "adopts four questions" as "poses four key questions".
- sei-atam: DISCREPANCY. The drafted URL is the 1998 report CMU/SEI-98-TR-008 (six authors), not the 2000 report. Claim #2 (prioritised scenarios) is not in the 1998 report. Either switch to CMU/SEI-2000-TR-004 (Kazman, Klein, Clements, August 2000; URL above) or drop "prioritised".
- slsa-build-track-basics: drop "2025-11"; the page prints only "SLSA v1.2", "Status: Approved". Title "Build: Track Basics" (tab "SLSA - Build: Track Basics").
- slsa-provenance: title "Build: Provenance"; same version/status wording.
- spec-kit-sdd, spec-kit: github.com blocks plain requests; cite the github.com URL but record "read from raw.githubusercontent.com (same file)". spec-kit: README titled "Spec Kit"; command list is correct and includes converge; clarify/analyze/checklist "optional quality gate" is from the docs page https://github.github.io/spec-kit/reference/agentic-sdd.html, not the README. Note the README uses hyphenated /speckit-name, the docs /speckit.name.
- metr-reward-hacking: authors Sydney Von Arx, Lawrence Chan, Beth Barnes; date June 5, 2025. Claim #2 should be softened: the post also reports 14 of 20 attempts when framed with real-world consequences.
- anthropic-claude-37-system-card: URL redirects to https://assets.claude.com/9ff93dfa8f445c932415d335c88852ef47f1201e.pdf; no date printed on the document (do not state 2025-02 as printed); relevant text is Section 6 "Excessive Focus on Passing Tests". The document says the behaviour came from reward hacking in RL training and partial mitigations were added before launch (nothing about later changes).
- konstantinou-test-oracles: title "Can we find bugs using LLM-generated oracles?"; note arXiv v2 revised 5 Oct 2026; no venue printed. Drop "open-source" or mark as not on the page ("24 Java repositories").
- pearce-copilot, perry-2023: the DOI targets could not be read (IEEE: empty 202; ACM: 403). Bibliographic facts above come from arXiv preprints and must be labelled as such. The S&P 2022 venue is unconfirmed by anything read.
- ahmed-incident-llm: add authors; "May 2023" printed. Remove "offline" and "at one cloud provider" or mark unconfirmed; keep "more than 40,000 incidents".
- chen-rcacopilot: 18 authors; venue "EuroSys '24" not on the arXiv page, so mark unconfirmed. "Microsoft" appears in the abstract.
- requirements-ambiguity-llm: add authors, venue ICSME 2025 (41st International Conference on Software Maintenance and Evolution), September 2025, DOI 10.1109/ICSME64153.2025.00063. Cite the publication record page alongside the PDF.
- gotel-finkelstein-1994: URL resolves to https://discovery.ucl.ac.uk/id/eprint/749/. Venue wording on the page is "Proceedings of 1st International Conference on Requirements Engineering" (the acronym ICRE is not printed). Add middle initials as printed on the paper: Orlena C. Z. Gotel, Anthony C. W. Finkelstein. Definition wording confirmed verbatim.
- rath-traceability-wild-2018: byline and DOI established via preprint (see Part D 11). Mark as substitute.
- reinertsen-flow-2009: replace the Goodreads URL is NOT possible from readable sources. Keep it flagged as a retail record, or drop claims #2-#4 and the publisher until an authoritative record is read. Do not state "weighted shortest job first" as appearing in the book.

## F. Sources not read directly, and why

### F.SAFe sources (worklist 2.1) and AI-Native SAFe

| key | URL | host | reason |
|---|---|---|---|
| (AI-Native Big Picture, found via SAFe's own nav link; not one of my keys) | https://ai-native.scaledagile.com/ | ai-native.scaledagile.com | HTTP 429 on two attempts about 20 seconds apart (rate limit) |

Partially readable (login wall: definition and first section readable, rest shown as "Log in to continue reading"): planning-interval, portfolio, agile-release-train, agile-teams, strategic-themes, portfolio-backlog, features-and-capabilities, story, safe-requirements-model, enablers, pi-planning, inspect-and-adapt, iteration-planning, iteration-retrospective, team-backlog-refinement, release-train-engineer, system-architect, built-in-quality, continuous-delivery-pipeline, release-on-demand, portfolio-flow, ain-safe-sense-and-respond, ain-safe-pi-outcome-planning. Claims that live below the wall are marked NOT FOUND (not readable).

### F.SAFe closed allow-list (worklist section 3)

All fetched with HTTP 200 and no bot challenge. Partly unreadable because the body after the intro is login-gated ("Log in to continue reading" served to a plain GET) on framework.scaledagile.com for: /agile-release-train, /agile-teams, /solution-train, /portfolio, /planning-interval, /pi-planning/, /inspect-and-adapt, /release-train-engineer, /system-architect/, /enablers, /features-and-capabilities, /story, /portfolio-backlog/, /epic/, /art-and-solution-train-backlogs/, /team-backlog/, /product-management/, /product-owner/, /scrum-master-team-coach/, /business-owners/, /system-demo/, /art-sync/, /innovation-and-planning-iteration/, /iterations/, /iteration-review/, /devops, /measure-and-grow, /applying-safe-to-hardware-development, /accelerating-flow-with-devsecops-and-the-software-factory. Some pages (large-solution, wsjf, guardrails, strategic-themes, built-in-quality, continuous-*) are cut off mid-article at a section heading with no gate message. Claims about the unread bodies (Definition of Ready usage, DevOps Health Radar, five domains of built-in quality, exact Reinertsen quote position) cannot be settled from these pages.

### F.DORA (2.2)

None. All 15 URLs returned HTTP 200 with article text, including the five cloud.google.com blog pages. Extra URLs read on dora.dev: /guides/dora-metrics/, /insights/dora-metrics-history/, /capabilities/, /ai/, /faq/ (dora-metrics-four-keys and /dora-report-2025/ redirect).

### F.Scrum, agile and requirements practice (2.3)

| key | URL | host | reason |
|---|---|---|---|
| overeem-dor | https://www.scrum.org/resources/blog/why-isnt-definition-ready-described-scrum-guide | www.scrum.org | HTTP 403 |
| kronfalt-ready-2008 | http://scrumftw.blogspot.com/2008/10/ready-ready-definition-of-ready-for.html | scrumftw.blogspot.com | request failed: name resolution error (not reachable from this environment) |
| sutherland-ready-2009 | http://jeffsutherland.com/scrum/2009/07/ready-dynamic-model-of-scrum.html | jeffsutherland.com | request failed: name resolution error |
| radice-etvx-1985 | https://dl.acm.org/doi/10.1147/sj.242.0079 | dl.acm.org | HTTP 403 |
| schwaber-beedle-2001 | https://dl.acm.org/doi/10.5555/559553 | dl.acm.org | HTTP 403 |
| schwaber-scrum-1995 | http://www.jeffsutherland.org/oopsla/schwapub.pdf | www.jeffsutherland.org | request failed: name resolution error |
| cooper-stage-gate | https://onlinelibrary.wiley.com/doi/full/10.1002/9781444316568.wiem05014 | onlinelibrary.wiley.com | HTTP 403 |

### F.ISO/IEC/IEEE and ISTQB (2.4, 2.5)

| key | URL | host | reason |
|---|---|---|---|
| iso-12207 | https://www.iso.org/standard/63712.html | www.iso.org | HTTP 403 (plain GET; challenge page not captured) |
| iso-12207 (2026 edition) | https://www.iso.org/standard/90219.html | www.iso.org | HTTP 403 |
| iso-14764 | https://www.iso.org/standard/80710.html | www.iso.org | HTTP 403 |
| iso-25010 | https://www.iso.org/standard/78176.html | www.iso.org | HTTP 403 |
| iso-29148 | https://www.iso.org/standard/72089.html | www.iso.org | HTTP 403 |
| iso-24765 | https://www.iso.org/standard/71952.html | www.iso.org | HTTP 403 |
| iso-15288 | https://www.iso.org/standard/81702.html | www.iso.org | HTTP 403 |
| iso-42010 | https://www.iso.org/standard/74393.html | www.iso.org | HTTP 403 |
| iso-29119-1 | https://www.iso.org/standard/81291.html | www.iso.org | HTTP 403 |
| iso-29119-3 | https://www.iso.org/standard/79429.html | www.iso.org | HTTP 403 |

Partly readable only through an API (not a failure, but flag): the five glossary.istqb.org term pages (rendered text not obtainable by plain GET; text read from https://api.glossary.istqb.org/v1/terms/<slug>).

### F.NIST, NASA, Fowler, Thoughtworks, Humble and Farley (2.6, 2.7, 2.9)

| key | URL | host | reason |
|---|---|---|---|
| humble-farley-cd (chapters 7, 8, 10 text only) | https://www.informit.com/store/continuous-delivery-reliable-software-releases-through-9780321601919 | informit.com | Catalogue page, TOC and sample chapter 5 read (HTTP 200); body text of chapters 7, 8, 10 is not freely available |
| nist-ssdf Rev. 1 final (not a drafted URL; tried) | https://csrc.nist.gov/pubs/sp/800/218/r1/final | csrc.nist.gov | HTTP 404 (also r1/2pd, r1/fpd, doi 800-218r1: 404) |

All other sources in the slice (csrc.nist.gov, nvlpubs.nist.gov, doi.org, swehb.nasa.gov, thoughtworks.com, martinfowler.com) were read directly with HTTP 200.

### F.Google SRE and engineering, OWASP (2.8, 2.10)

| key | URL | host | reason |
|---|---|---|---|
| petrovic-mutation | https://dl.acm.org/doi/10.1145/3183519.3183521 | dl.acm.org | HTTP 403 to a plain GET (title, authors, venue, DOI, abstract all unread; both claims NOT FOUND (not readable)) |

### F.Other public sources (2.11)

| key | URL | host | reason |
|---|---|---|---|
| spec-kit-sdd, spec-kit | https://github.com/github/spec-kit (and blob/main/spec-driven.md) | github.com | HTTP 403; read from raw.githubusercontent.com (same file) |
| rath-traceability-wild-2018 | https://dl.acm.org/doi/10.1145/3180155.3180207 | dl.acm.org; doi.org | HTTP 403 on both; preprint on arXiv read as substitute |
| perry-2023 | https://doi.org/10.1145/3576915.3623157 | doi.org (ACM) | HTTP 403; arXiv 2211.03622 read as substitute |
| pearce-copilot | https://doi.org/10.1109/SP46214.2022.9833571 | ieeexplore.ieee.org | redirect ends at https://ieeexplore.ieee.org/document/9833571/, HTTP 202 with empty body (no text); arXiv 2108.09293 read as substitute |
| reinertsen-flow-2009 (authoritative record) | reinertsenassociates.com, celeritaspub.com, celeritaspublishing.com, reinertsen.com | various | TLS verify failure / 502 / DNS failure; worldcat.org HTTP 429; openlibrary.org connection reset; Library of Congress catalogue returned an empty page |
