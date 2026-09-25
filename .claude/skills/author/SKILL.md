---
name: author
description: "Writing rules and the page checklist for reference pages. Used by the author agent."
---

# Author

Voice and neutrality rules are in `.github/instructions/content-style.instructions.md`; they apply
in full.

## Page checklist

- [ ] Copied from `templates/pages/<type>.md`; every guidance comment deleted.
- [ ] Every front-matter field filled; `id` equals the file name; the file sits in its band folder.
- [ ] Every section present, in order, and substantive (at least 25 words; Related has links;
      Sources cites references).
- [ ] First use of "AI SDLC" spells out "software development lifecycle" (D-013).
- [ ] Every claim beyond common knowledge has a `[^key]`; every key is in `sources`.
- [ ] Borrowed terms credited in the glossary; coined terms marked coined (GR-2.2).
- [ ] No invented statistics, case studies, quotes or anecdotes (GR-2.3).
- [ ] No first person, no organisation's progress, present tense (GR-3.1).
- [ ] No provisional language (GR-3.2); no product names outside a category page (GR-3.3).
- [ ] The customer-record export is the only worked example (GR-3.4).
- [ ] The page makes sense to a reader who has read nothing else on the site (GR-4.2).
- [ ] Nothing reads like the source library (GR-1.2).

Run `python scripts/check_pages.py` and `python scripts/check_citations.py` before handing over.
