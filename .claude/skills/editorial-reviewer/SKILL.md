---
name: editorial-reviewer
description: "GR-3 and GR-4 checklist and report format for section reviews. Used by the editorial-reviewer agent."
---

# Editorial review

Style rules: `.github/instructions/content-style.instructions.md`.

## Checklist

- [ ] GR-3.1 Present tense, third person, plain practitioner English; no organisation's progress;
      none of the avoided phrases.
- [ ] GR-3.2 No provisional language anywhere, including titles, captions and link text.
- [ ] GR-3.3 Vendor-neutral wording.
- [ ] GR-3.4 Only the customer-record export as a worked example.
- [ ] GR-4.1 Every template section present and substantive (quote `check_pages.py` output);
      no section padded to pass the word count.
- [ ] GR-4.2 Each page stands alone for a reader arriving from search.
- [ ] GR-4.3 Every internal link resolves (the site tests); links point where their text says.
- [ ] GR-4.4 Every diagram has a text alternative and reads in both themes.
- [ ] D-013 "Software development lifecycle" spelled out at the first use of "AI SDLC" on each page.
- [ ] Consistency: the page agrees with the map's labels, the glossary, the workflow catalog and
      the other pages of the section; the changelog describes the change accurately.

## Report format

Markdown, in this order: **Scope** (commit, files, pages), **Evidence** (commands run and their
output; what was read and how), **Checks performed**, **Blocking issues**, **Suggestions
(non-blocking)**. Tag every finding with its rule (GR-x.y) and location. End with exactly one line:

    Reviewer verdict: ACCEPT        (or REVISE)

Never write a line that starts with `Verdict:`; only the assembled record carries one.
