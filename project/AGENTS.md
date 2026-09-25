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
| `architect` | Owns the map, the page inventory and section plans; opens page briefs | Map, `STATUS.md`, inventory | `briefs/<page>.md`, inventory, section plan |
| `source-researcher` | Reads the private library for a brief; extracts practice; de-identifies | Brief, Drive library | Practice brief **outside the repo** (session scratch only) |
| `external-researcher` | Finds and verifies public sources for every claim | Brief, web | `content/references.yml` entries, evidence notes in the brief |
| `author` | Writes the page to its template in the site voice | Brief, both research outputs, template | `content/pages/<band>/<page>.md` |
| `diagrammer` | Diagrams as code in the house palette; text alternatives | Page | `content/diagrams/...` |
| `confidentiality-reviewer` | GR-1 and GR-3.3; can BLOCK | Page, diagrams | Verdict in the review record |
| `accuracy-reviewer` | GR-2: every claim sourced, sources say what is claimed | Page, references | Verdict in the review record |
| `editorial-reviewer` | GR-3, GR-4: voice, completeness, standalone, consistency with map and other pages | Page, template, related pages | Verdict in the review record |
| `site-builder` | Wires pages into map and navigation; runs checks and build; opens the PR | Everything | Site code, PR |

## Independence

Reviewers never see the author agent's reasoning, only the page and its sources. Each reviewer
runs in a fresh context. The confidentiality reviewer does not see the practice brief, so it
judges the page as a public reader would.

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
