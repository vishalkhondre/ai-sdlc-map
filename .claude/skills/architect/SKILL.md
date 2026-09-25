---
name: architect
description: "Checklist and templates for planning a section and writing page briefs. Used by the architect agent."
---

# Architect

## Section plan (to the author, for approval)

- Section name and band; the edition it becomes (next minor).
- A table: page id · page type · map box · coverage (from `project/COVERAGE.md`) · one line of
  scope. One page per box; say why if a box is merged into another or split.
- Pages that rely on public sources only (coverage thin or none), and how that shapes them.
- Related pages outside the section that the section links to, and whether they exist yet.
- Map changes the section needs (links, relabels), each needing approval.
- Order of work and risks (confidentiality, weak public evidence).

## Page brief (scratchpad only)

```
page: <id>          type: <template>        band: <band>        map_box: <label>
scope: what the page covers, in two or three sentences
questions: the questions a reader arrives with, which the page must answer
key_terms: glossary ids; new terms to add, with their origin
related: page ids
out_of_scope: what belongs on another page
running_example: where the customer-record export illustrates the page
```
