# Agents and skills

Agents are Claude Code sub-agents in `.claude/agents/`; each has a matching skill in
`.claude/skills/<agent>/SKILL.md` holding its checklist, templates and output format. The skill
`section-pipeline` runs a whole section through them (D-014). Every agent reads `CLAUDE.md`,
`project/GROUND-RULES.md` and this file before working.

Claude Code agents are used because the source library is reachable only through the Google
Drive connector in Claude sessions (see `DECISIONS.md`, D-004).

## Roster

| Agent | Job | Reads | Writes |
|---|---|---|---|
| `architect` | Owns the map, the page inventory and section plans; opens page briefs | Map, `STATUS.md`, `COVERAGE.md` | Section plan (`project/plans/`); page briefs and the source inventory in the session scratchpad only |
| `source-researcher` | Reads the private library for a brief; extracts practice; de-identifies | Brief, Drive library | Practice brief **outside the repo** (session scratch only) |
| `external-researcher` | Finds and verifies public sources for every claim | Brief, web | Evidence brief with drafted reference entries (the author adds them to `content/references.yml`) |
| `author` | Writes the page to its template in the site voice | Brief, both research outputs, template | `content/pages/<band>/<page>.md` |
| `diagrammer` | Diagrams as code in the house palette; text alternatives | Page | `content/diagrams/...` |
| `confidentiality-reviewer` | GR-1 and GR-3.3; can BLOCK | Page, diagrams | Verdict in the review record |
| `accuracy-reviewer` | GR-2: every claim sourced, sources say what is claimed | Page, references | Verdict in the review record |
| `editorial-reviewer` | GR-3, GR-4: voice, completeness, standalone, consistency with map and other pages | Page, template, related pages | Verdict in the review record |
| `site-builder` | Wires pages into map and navigation; runs checks and build; opens the PR | Everything | Site code, PR |

## Orchestration

The main session runs the pipeline (`.claude/skills/section-pipeline`). It starts each agent,
carries each output to the next step, and starts the three reviewers in fresh contexts. Agents do
not start other agents; where an agent file says "return", the output goes back to the main
session.

## Independence

Reviewers never see the author agent's reasoning, only the page and its sources. Each reviewer
runs in a fresh context. The confidentiality reviewer does not see the practice brief, so it
judges the page as a public reader would.

## Source library and the paraphrase sweep (D-026)

This rule holds for every section, because a de-identified brief still carries the source's
structure: its lists, the order of its steps and its examples.

1. **Authors never read the library.** `author` works from the page brief, the evidence brief and
   the site's own pages. It never opens the source library, a practice brief's source documents,
   or notes written by someone who compared text with the library.
2. **The researcher passes concepts only.** `source-researcher` gives `author` the concepts a
   page should cover and which of them are general practice, never the library's wording, lists,
   step order, sets of examples, figures or its own names for things.
3. **The sweep runs before the first review.** After Write and before Check, `source-researcher`
   compares every draft page with the library and reports passages that are close in wording,
   list, sequence, set of examples or structure. Close passages are cut, and rewritten only by an
   author who sees neither the old passage nor the sweep's notes; the sweep then runs again until
   it reports no close passage. Replacement text written by anyone who has read the library is
   never used.
4. **Nothing is pushed before the sweep passes.** Drafts stay on the local machine: no push to any
   remote branch and no pull request until the sweep is clean. The branch that is pushed holds the
   section as one commit on top of `main`, with a neutral message, so no earlier draft is in its
   history.
   If a draft was pushed by mistake, delete the branch, confirm with `git ls-remote` that no ref
   holds it, and ask the host to purge the unreferenced commits.

## Review record

Today one record covers a section: `content/reviews/<edition>-<section>.md` holds each
reviewer's report for every round and one final `Verdict: ACCEPT`, and
`scripts/release_content.py record-review` binds it to the exact sources, so CI fails if any
page changes after review. The planned per-page record, one file per page in
`reviews/<page-id>.yml`, is:

```yaml
page: <page-id>
page_hash: <sha256 of the page source at review time>
pipeline_version: <version of agents and templates>
sources: [<reference keys>]
reviews:
  - reviewer: confidentiality-reviewer
    verdict: ACCEPT        # ACCEPT | REVISE | BLOCK
    findings: []           # each: {rule: GR-x.y, location, issue, resolution}
  - reviewer: accuracy-reviewer
    verdict: ACCEPT
    findings: []
  - reviewer: editorial-reviewer
    verdict: ACCEPT
    findings: []
section: <band or adoption>   # the author's approval is the section's release tag (D-014, D-016)
```

CI fails if a published page has no record, if any verdict is not ACCEPT, or if `page_hash`
does not match the current page (the page changed after review).

## Folded-in assets

- `.github/agents/citation-reviewer.agent.md`, `content-author.agent.md` and
  `content-researcher.agent.md` were folded into `accuracy-reviewer`, `author` and
  `external-researcher` and removed.
- `.github/instructions/content-style.instructions.md` stays as the style source for editors and
  Copilot; the `author` and `editorial-reviewer` skills apply it in full.
