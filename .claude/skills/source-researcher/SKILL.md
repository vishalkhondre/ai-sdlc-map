---
name: source-researcher
description: "De-identification rules and the practice-brief format for reading the private source library. Used by the source-researcher agent."
---

# Source researcher

## Before writing anything

- Find the folder `ai-sdlc` in Drive and the documents the brief needs; read them fully enough
  to understand the practice, not only to extract it.
- Write to the session scratchpad only (for example `<scratchpad>/briefs/<page>-practice.md`).

## Practice brief format

```
page: <id>
practices:
  - practice: what is done, in general industry words
    why: the problem it addresses
    evidence: in depth | partial | mention (library strength)
    general_or_local: general practice | local convention (say which)
gaps: what the library does not cover for this page
cautions: anything that would be recognisable if written closely
```

## De-identification checklist (GR-1.1, GR-1.2)

- [ ] No organisation, group, business unit, product, platform, project, team or people names.
- [ ] No internal identifiers of any kind: tracker keys, branch or tag patterns, document or
      section numbers.
- [ ] No internal figures: counts, percentages, durations, dates of internal events, costs.
- [ ] No document titles and no quotations; nothing close enough to be recognised.
- [ ] No combination of named tools that together fingerprints one organisation's stack.
- [ ] Practices generalised: "a team", "an organisation", never "the programme".
- [ ] Concepts only (D-026): no list of rules, conditions or examples reproduced as a set, no step
      order, and no worked example from the library; one concept per entry.

## The paraphrase sweep (D-026)

Before a section's first review, compare every draft page with the library and report each passage
that is close in wording, list, sequence, set of examples or structure, with page and lines and a
one-line topic. Do not write replacement text: close passages are cut and rewritten by an author
who has not read the library. Repeat the sweep until it reports nothing close. Never quote the
library or name its documents in the report.
