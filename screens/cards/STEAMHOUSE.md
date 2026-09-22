# STEAMHOUSE — Steamhouse India Ltd

Shallow Analysis Framework v1.0. Screened 2026-09-22 by Claude Code.
NSE STEAMHOUSE | BSE 544914 | ISIN INE0FRO01022. Listed 17-Sep-2026.
Corpus: `screens/corpus/STEAMHOUSE/`. **The corpus is empty.**

---

## This card carries no business verdict

Steamhouse India listed on 17 September 2026, five days before this screen. A
complete, untruncated document-availability check against the Bull AI index
returned **an empty list**: no prospectus, no red herring prospectus, no draft
red herring prospectus, no result, no presentation, no announcement, nothing in
any category.

The check was run without filters and the service returned
`"available_documents": []` with `"complete_result": true` and
`"truncated": false`. That is the index stating positively that it holds nothing
for this company, not a truncated answer.

A follow-up document search on the business terms, "steam nitrogen community
boiler revenue profit business", returned zero results with no source buckets
used.

**No number on this page traces to a filing, because no filing was reachable.**
Under the framework's rule that "NOT FOUND is the only valid fill", this card
records the ledger and stops. Writing a business analysis would breach the rule
that every number traces to a file and a page.

This is the same outcome the 2026-09-21 run recorded for YAASHVI, and the card
takes the same shape.

---

## 1. Corpus ledger

| Item | Status |
|---|---|
| Identity | **Resolved.** Steamhouse India Ltd, NSE STEAMHOUSE, BSE 544914, ISIN INE0FRO01022 |
| Prospectus / RHP / DRHP | **NOT FOUND** in the Bull AI index |
| Annual report | **NOT FOUND** |
| Financial results, any period | **NOT FOUND** |
| Investor presentation | **NOT FOUND** |
| Earnings call transcript | **NOT FOUND** |
| Shareholding pattern | **NOT FOUND** |
| Credit rating | **NOT FOUND** |
| Any Regulation 30 announcement | **NOT FOUND** |

Where it was looked for: `list_document_availability` on identifier STEAMHOUSE,
unfiltered, complete result, empty; `search_company_documents` on the business
description, zero results; and the company's own exchange filings, which this
container cannot reach because the network policy answered 403 to the CONNECT
for www.bseindia.com, www.nseindia.com, www.screener.in and docs.bull-ai.in.

**This card cannot distinguish a Bull AI coverage gap from a company that has
filed nothing yet**, and it says so. A company listed on 17 September 2026 would
certainly have filed a prospectus, so the more likely explanation is that the
index has not yet ingested a name five days old. That is a hypothesis, not a
finding.

## 2 to 11. Not attempted

Steps 2 through 11 require documents. None exist in this corpus. Attempting a
business model, a moat assessment, a promoter check, a financial trajectory, a
ladder placement or a decision-matrix posture from general knowledge would
produce exactly the shallow, unanchored output the framework exists to prevent.

The two facts available come from the operator's own screen list and are
recorded as operator input, not as corpus evidence:

- The business is described as generation and distribution of steam and nitrogen
  through a pipeline network, having pioneered a community boiler system in 2014.
- The listing date is 17 September 2026.

Neither is verified here.

One number is available from a service record rather than a filing: the Bull AI
company record puts market capitalisation at **Rs 2,908.90 crore** at 22
September 2026. It is a service record, not a filed document, and there are no
earnings in this corpus to put beside it.

**One observation is worth carrying forward even so.** If the operator's
description is accurate, a community boiler network selling steam and nitrogen
by pipeline is an **infrastructure utility, not a manufacturer**: contracted
offtake, a regulated or bilateral tariff, and a physical network that is
expensive to duplicate inside an industrial cluster. On the CLAUDE.md archetype
library that is a **licence/scarcity business**, and any later analysis should
open there rather than at a converter or component-maker frame. That is a
hypothesis to test, not a conclusion.

## 12. Verdict card

**WATCH for documents. This is not a business verdict.**

The name is not rejected and it is not endorsed. Nothing has been assessed. A
Rs 2,909 crore market capitalisation on a business model that may well be a
scarce-asset utility is worth a second look, and the second look needs a
prospectus.

**The action is retrieval, not analysis.** Re-screen when any one of these
exists:
1. **The prospectus or red herring prospectus.** For a company listed five days
   ago this is the whole corpus and it carries three years of restated
   financials, the promoter history, the customer contracts and the risk
   factors.
2. **The first post-listing result**, which for a September listing would be the
   quarter to 30 September 2026, due around November 2026.
3. **The shareholding pattern**, due within 21 days of listing.

**How to retrieve, given this container has no live web.** Three routes, in
order of cost:
- Re-run `list_document_availability` on a later date. A five-day-old listing is
  the most likely explanation for the empty index, and it should populate.
- Fetch the prospectus from the exchange archive in a session with egress, using
  `tools/collector/screener_collect.py` or the BSE announcements path recorded
  in `screens/README.md`.
- Ask Claude web to run a spear pass on live web, which is the framework's
  proper first step for an unknown name anyway.

**The SPEAR GATE applies here regardless.** Under the CLAUDE.md gate rule,
`/run-pipeline` and `/fttcp` on a new name require a Spear HIT or an operator
override line in `companies/STEAMHOUSE.md`. No such file exists. For this name
the spear pass is not merely the gate, it is the only way to learn anything at
all, because Claude Code cannot reach live web and the document index is empty.

No load-bearing facts can be named, because no facts were established.

No price. No position.

## 13. Forward view

| Item | Value |
|---|---|
| Last reported PAT | **NOT FOUND** |
| FY27E PAT | **NOT FOUND** |
| Growth | **NOT FOUND** |
| Market capitalisation | Rs 2,908.90 crore (Bull AI service record, 22-Sep-2026) |
| **Forward PE** | **blank** |
| **Basis tier** | **D — NOT FOUND** |

The forward PE is left blank, as tier D requires. It is not filled.

There is no forward basis of any kind. Bull AI holds no guidance records because
it holds no documents. There is no delivered year to grow from, no quarter to
annualise and no trend to extrapolate. Every one of tiers A, B and C is
unavailable for the same reason: the corpus is empty.

The market capitalisation is shown alone, without a multiple beside it,
deliberately. **Pairing a service-record market capitalisation with an invented
earnings figure is precisely the fabrication this step's basis-tier discipline
exists to prevent.**

This name cannot be ranked in the run-wide forward-view table. It appears there
with blanks.
