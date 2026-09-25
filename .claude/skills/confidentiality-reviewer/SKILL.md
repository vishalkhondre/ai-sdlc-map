---
name: confidentiality-reviewer
description: "GR-1 and GR-3.3 checklist and report format for section reviews. Used by the confidentiality-reviewer agent."
---

# Confidentiality review

Read as a member of the public who knows the industry, and as a colleague of the author who
knows the organisation. Either reader recognising the source is a finding.

## Checklist

- [ ] GR-1.1 No organisation, group, product, platform, project, team or people names, internal
      codes, customers or internal figures. The deny-list check passed (quote its output).
- [ ] GR-1.1 No combination of named tools, team shapes, cadences or numbers that together
      fingerprints one organisation.
- [ ] GR-1.2 Nothing reads as copied or closely paraphrased from internal material: unusual
      phrasing, house vocabulary, numbered internal schemes, oddly specific examples.
- [ ] GR-1.2 Practices read as general industry practice, not as one organisation's programme.
- [ ] GR-1.3 No document, excerpt, extract or research note added anywhere in the diff,
      including ignored or scratch folders.
- [ ] GR-1.4 The deny-list is not revealed (no plain names in code, tests, commits or reports).
- [ ] GR-3.3 Products named only on a page about their category, as one example among several.
- [ ] D-015 The SAFe reference model names no origin and is not recognisable.

## Report format

Markdown, in this order: **Scope** (commit, files, pages), **Evidence** (commands run and their
output; what was read and how), **Checks performed**, **Blocking issues**, **Suggestions
(non-blocking)**. Tag every finding with its rule (GR-x.y) and location. End with exactly one line:

    Reviewer verdict: ACCEPT        (or REVISE, or BLOCK for any GR-1.1 or GR-1.2 finding)

Never write a line that starts with `Verdict:`; only the assembled record carries one.
