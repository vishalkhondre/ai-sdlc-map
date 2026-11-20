# KICKOFF: rules for Lifecycle sessions

Read this with `CLAUDE.md` and `project/` at the start of every session that reads sources or
builds Lifecycle pages (editions 1.5.0 and 1.6.0). It holds the rules the author set after the
1.5.0 source check (`project/handover/lifecycle-1.5-source-check-results.md`). Where it is silent,
`project/GROUND-RULES.md` rules.

## (a) Network and the plain-User-Agent rule

**Allow-list.** A cloud session reaches only the hosts its environment allows. The source check
needed these, and they answered a plain request:

| Group | Hosts |
|---|---|
| SAFe | `framework.scaledagile.com`, `scaledagileframework.com` (redirects to the first) |
| DORA, Google | `dora.dev`, `cloud.google.com`, `sre.google` |
| Scrum and agile | `scrumguides.org`, `agilemanifesto.org`, `agilealliance.org`, `keepachangelog.com`, `semver.org`, `xp123.com` |
| NIST, NASA, SEI | `csrc.nist.gov`, `nvlpubs.nist.gov`, `nist.gov`, `www.nist.gov`, `swehb.nasa.gov`, `www.sei.cmu.edu` |
| Practitioners | `martinfowler.com`, `thoughtworks.com`, `www.thoughtworks.com`, `12factor.net`, `www.threatmodelingmanifesto.org`, `slsa.dev`, `cheatsheetseries.owasp.org`, `metr.org` |
| Standards bodies and testing | `docs.oasis-open.org`, `glossary.istqb.org` (its terms load from `api.glossary.istqb.org`), `www.istqb.org`, `www.astqb.org` |
| Research | `arxiv.org`, `www.ipr.mdu.se`, `www.microsoft.com`, `www.anthropic.com` |
| Publishers and records | `www.informit.com`, `www.peoplecert.org`, `www.goodreads.com`, `doi.org` |
| Code hosting | `raw.githubusercontent.com` (GitHub pages themselves refuse a plain request) |
| Also allowed, not needed so far | `iso.org`, `www.iso.org`, `openai.com`, `en.wikipedia.org` |

If the environment is set to unrestricted access this table is moot, but the rules below still
apply.

**Plain User-Agent rule.**

- Fetch with a plain HTTP GET from a client that names itself honestly (for example
  `ai-sdlc-map-source-check/1.0`). Never send a browser User-Agent, never rotate agents, never script
  a browser to get past a block.
- A bot challenge (a Cloudflare "Just a moment" page) or an HTTP 403 is a refusal, not an obstacle.
  Do not work around it. `iso.org`, `www.iso.org`, `openai.com`, `dl.acm.org`,
  `onlinelibrary.wiley.com`, `discovery.ucl.ac.uk` and `www.scrum.org` refuse plain requests.
- Read each source directly and quote only text that was read. Never fall back to search results,
  archives, caches or mirrors. The only substitutions allowed are the ones named in the source-check
  results, and every use is labelled in the entry.
- A request that a session's safety checks block is not retried in another form.

## (b) The unreadable-source policy

A source a session cannot read is a gap in evidence, not a licence to fill it. It never becomes a
page claim by memory or search.

| Case | Rule |
|---|---|
| ISO, IEC and IEEE standards (catalogue pages refuse plain requests) | Their claims stay off the site until a person reads the standards. That covers the 12207 second edition, the 29148 characteristics and their order, the 14764 maintenance types, and the other ISO rows of the results file. A page may name a standard only where the claim stands on a source that was read. |
| SAFe text behind the login wall | A page follows the SAFe glossary wording for the term. Where the glossary is silent, the page says less rather than more. |
| Books | A book claim cites only what the table of contents or a freely readable excerpt shows (for example a chapter title). It does not state what a chapter says. |
| Any other source a script cannot read | The claim is marked **author to confirm**, with the claim and the URL, in the evidence brief and in the "For the author" list in `STATUS.md`. The author reads it in a browser and confirms or corrects the claim. Until then the claim is not on a page. |

Applying the source-check results to page wording:

- Every PARTLY and NOT SUPPORTED finding is applied: the page says what the source says, not what
  the drafted claim said.
- SAFe cadence figures are cited as "typical", never as defaults or requirements.
- No page says SAFe defines a Definition of Ready.
- The SAFe reference model rests on Core SAFe 6.x, with one short cited note on AI-Native SAFe's
  Sense and Respond, which replaces Inspect and Adapt there and absorbs the System Demo's activities.

## (c) The parked backlog

Items the author has parked. None blocks edition 1.5.0, and none is started without the author's
instruction.

1. **Keyed deny-list (D-023).** The author runs `scripts/denylist_rekey.py` in a local clone and
   opens a pull request from `denylist-keyed`. A session then confirms CI is green with the key and
   removes the salted fallback as a reviewed tooling change. The salted-hash check stays in force
   meanwhile.
2. **Delete merged branches on GitHub** (sessions cannot): `claude/bold-maxwell-dy6hmz`,
   `claude/zen-mccarthy-kge7f5`, `claude/eloquent-carson-t78pzu`, `claude/dazzling-brahmagupta-y77u3o`
   and `claude/lifecycle-1.5-source-check`.
3. **GitHub Support purge** of the four unreferenced draft commits (IDs held outside the repository).
4. **Old series repository (`ai-sdlc`).** Remove the plain-text employer names from its check script,
   or make the repository private.
5. **Optional: v1.4.0 tag** at `1ea1e73`.
6. **Optional follow-up edition.** The harness page describes the feedback path as the site's
   extension of the steering loop in all three places; add the dotted precondition line to the
   workflow diagram's legend.
7. **Catalog consistency pass (W12 wording).** The W12 row says "definition of ready" while the map
   and adoption path place it at Specification (D-029, question 8).

### Browser confirmations

None yet. Until the author confirms, pages are written conservatively, and each affected claim is
listed under "G. Author to confirm" in
`project/handover/lifecycle-1.5-source-check-results.md`:

- The Definition of Ready rests on the Scrum Guide and the Agile Alliance glossary page only, with no
  attribution of its origin.
- The three ISO claims (12207 second edition, 29148 characteristics, 14764 maintenance types) stay off
  edition 1.5.0.
- The SAFe wording for the eight PARTLY terms follows the glossary or definition-page wording quoted in
  part C of the results.

The author reads each source in a browser, pastes what it says into chat, and a session adds it in a
later edition.
