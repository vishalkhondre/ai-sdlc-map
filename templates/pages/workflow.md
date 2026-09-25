---
id: <page id, lowercase words joined by hyphens>
type: workflow
band: <context | lifecycle | core | enablement | assurance | adoption>
map_box: <the label on the map this page covers>
title: <page title>
summary: <one sentence for the page header, search and social preview>
key_terms: [<glossary ids used on the page>]
sources: [<reference keys from content/references.yml>]
related: [<page ids on this site>]
review_record: <content/reviews/<edition>-<section>.md>
---

<!-- Template for a Workflow page (project/APPROACH.md). Copy to content/pages/<band>/<id>.md,
     fill every field and every section, and delete every guidance comment.
     scripts/check_pages.py enforces the front matter and the sections, in this order (GR-4.1). -->

## Decision

<!-- The one delivery decision the workflow supports, phrased as a question. -->

## Trigger

<!-- The event that starts a run. -->

## Inputs

<!-- What the run takes from the kit and from the change. -->

## Agent task

<!-- What the agent does, and what it is not allowed to do. -->

## Checks

<!-- The deterministic checks, each with its rule and result states. -->

## Guardrails

<!-- Permissions, limits and stop conditions. -->

## Human decision

<!-- Who decides, on what evidence, and what they may override. -->

## Outputs and evidence

<!-- What the run produces, and the evidence record it leaves. -->

## Failure paths

<!-- What happens when a check fails, cannot run, or the agent stops. -->

## Measures

<!-- What to measure to know the workflow works, with the baseline to compare against. -->

## Owner

<!-- The role that owns the workflow and changes it. -->

## Related

<!-- Neighbouring workflows it takes evidence from or hands evidence to. -->

## Sources

<!-- Reference keys for every claim beyond common knowledge. -->
