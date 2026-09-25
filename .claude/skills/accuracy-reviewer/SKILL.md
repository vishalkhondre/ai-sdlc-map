---
name: accuracy-reviewer
description: "GR-2 checklist and report format for section reviews. Used by the accuracy-reviewer agent."
---

# Accuracy review

## Checklist

- [ ] GR-2.1 Every claim beyond common knowledge cites a source of the right kind, in the
      preferred order.
- [ ] GR-2.2 Borrowed terms credited to their originator; coined terms marked coined; the
      glossary agrees with the page.
- [ ] GR-2.3 No invented statistics, case studies, quotes or anecdotes; unsourced practice is
      presented as recommended practice.
- [ ] GR-2.4 Each source says what the page claims. Build the table: claim → source → supported?
- [ ] GR-2.5 Each new or changed reference: title, author or organisation, URL, date, accessed;
      title and byline as published. Say how you verified each (direct read, or search only).
- [ ] Current terminology (`scripts/outdated_terms.yml`); flag any superseded term it misses.
- [ ] The citation gate passed (quote its output).

## Report format

Markdown, in this order: **Scope** (commit, files, pages), **Evidence** (commands run and their
output; what was read and how), **Checks performed**, **Blocking issues**, **Suggestions
(non-blocking)**. Tag every finding with its rule (GR-x.y) and location. End with exactly one line:

    Reviewer verdict: ACCEPT        (or REVISE)

Never write a line that starts with `Verdict:`; only the assembled record carries one.
