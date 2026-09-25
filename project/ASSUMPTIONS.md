# Assumptions and open questions

An assumption is held true until evidence or the author says otherwise. When one changes,
record it in `DECISIONS.md`.

## Assumptions

- **A1 Audience.** Practitioners and leaders in organisations of any size; familiarity with
  agile delivery and CI/CD is assumed, familiarity with AI agents is not.
- **A2 Scope.** The five-band map (as drawn in commit `76d0756` of `vishalkhondre/ai-sdlc`, with
  the neutral labels of edition 1.1.0) is the agreed scope. New boxes are
  added only through the architect agent with the author's approval.
- **A3 Source library.** The author's private Google Drive folder `ai-sdlc` is the source of
  practice experience: a delivery framework, executive and organisation-wide summaries, a
  delivery package, runbooks and playbooks. It is reachable only through the Google Drive
  connector in Claude sessions. It is internal material and falls under GR-1 in full.
- **A4 Public evidence exists** for most practices on the map. Where it does not, the page
  presents recommended practice (GR-2.3) rather than dropping the topic.
- **A5 Tooling.** The existing generator (Python, Markdown, YAML, inline SVG, vanilla JS) scales
  to the full site without a framework change.
- **A6 Hosting.** GitHub Pages via GitHub Actions from `main` of `vishalkhondre/ai-sdlc-map`, served
  at `vishalkhondre.github.io/ai-sdlc-map/`. The series stays at `vishalkhondre.github.io/ai-sdlc/`
  (D-010).
- **A7 Sessions.** Work spans many sessions. Continuity lives in this folder, not in any
  session's memory.
- **A8 Push access.** A session can push only to repositories attached to it: selected when the
  session started, or added during it. Otherwise work is handed over as a git bundle.

## Open questions (need the author)

None open.

## Settled

- **Q1 Vendor names on the map.** Settled 2026-09-25: generic labels on the map (for example
  "Spec-driven development (SDD) frameworks", "Work tracking & knowledge base"); named tools only
  on category pages, as examples. Diagram text is gated for product names (D-009).
- **Q2 Approval.** Settled 2026-09-25: one section at a time (a section is one map band, or the
  adoption path). Agents review the whole section; it goes live after every agent reviewer
  accepts; the author reviews it live and approves it by its release tag (D-014; GR-6.1 v1.1).
- **Q3 SAFe on the map.** Settled 2026-09-25: generic portfolio / train / team labels on the map
  with SAFe cited, plus a worked SAFe reference model page, de-identified in full, origin not
  named (D-015).
- **Q4 Release versioning.** Settled 2026-09-25: a semver tag and GitHub Release per approved
  section, one minor version each, with changelog notes and a PDF snapshot; v2.0.0 when every
  map box has a page (D-016).
