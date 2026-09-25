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
- [ ] No internal codes: tracker keys, branch or tag patterns, field IDs, page IDs, plan codes,
      decision numbers, technique numbers.
- [ ] No internal figures: counts, percentages, durations, dates of internal events, costs.
- [ ] No document titles and no quotations; nothing close enough to be recognised.
- [ ] No combination of named tools that together fingerprints one organisation's stack.
- [ ] Practices generalised: "a team", "an organisation", never "the programme".
