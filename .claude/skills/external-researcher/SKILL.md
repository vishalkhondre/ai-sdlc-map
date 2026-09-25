---
name: external-researcher
description: "Source-preference order, verification rules and the reference-entry format. Used by the external-researcher agent."
---

# External researcher

## Order of preference (GR-2.1)

1. Standards and frameworks: ISO, NIST, OWASP, SLSA, SAFe.
2. Research: DORA, peer-reviewed studies.
3. Recognised practitioners: martinfowler.com, Thoughtworks Technology Radar, established
   engineering blogs.
4. Official tool documentation, for facts about that tool only.

## Evidence brief format

```
page: <id>
claims:
  - claim: the sentence the page will make
    source: <reference key>
    supports: quote or close paraphrase of what the source says
    verified: direct read | search results only (network blocked) | not verified
gaps: claims with no public source (present as recommended practice, GR-2.3)
```

## Reference entry (content/references.yml, GR-2.5)

```yaml
<key>:
  title: "<exact title as published>"
  author: "<person or organisation>"
  org: "<publisher>"
  date: "<publication date, as precise as known>"
  url: "<canonical URL>"
  accessed: "YYYY-MM-DD"
  note: "<what the source covers that the site relies on; nothing it does not say>"
```

- Titles and bylines as published; never inferred from a URL.
- A note describes the source; it never overclaims ("the origin of", "proves").
- Check `scripts/outdated_terms.yml` and the source's current terminology.
