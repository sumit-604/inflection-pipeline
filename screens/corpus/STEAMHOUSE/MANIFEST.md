# STEAMHOUSE corpus manifest

Company: Steamhouse India Ltd
NSE: STEAMHOUSE | BSE: 544914 | ISIN: INE0FRO01022 | Listed 17-Sep-2026
Screened: 2026-09-22

## Corpus rule deviation (operator ruling 2026-09-08 applies)

No egress this session. The network policy answered 403 to the CONNECT for
docs.bull-ai.in, www.bseindia.com, www.screener.in and every rating agency site.
The corpus is the Bull AI chunk reader, which returns page-numbered text of the
same filed PDFs. Page numbers are the source PDF's own. Nobody holds the
original file.

## Documents read

**None. The corpus is empty.**

| Check run | Result |
|---|---|
| `search_companies` on "Steamhouse India" | Identity resolved: NSE STEAMHOUSE, BSE 544914, ISIN INE0FRO01022 |
| `list_document_availability`, unfiltered | `"available_documents": []`, `"complete_result": true`, `"truncated": false` |
| `search_company_documents`, business terms | Zero results, no source buckets used |

The index states positively that it holds nothing for this company, in any
category. This is not a truncated answer.

## Known gaps

**Everything.** No prospectus, no RHP, no DRHP, no result, no presentation, no
announcement, no shareholding pattern, no credit rating.

The company listed on 17 September 2026, five days before this screen. The most
likely explanation is that Bull AI has not yet ingested a name five days old.
**This manifest cannot distinguish an index coverage gap from a company that has
filed nothing**, and the card says so.

No card content beyond the ledger was written, because no number would trace to
a file and a page. Under the framework's rule, NOT FOUND is the only valid fill.

## To build this corpus

1. Re-run `list_document_availability` on a later date; the index should populate.
2. Fetch the prospectus from the exchange archive in a session with egress, per
   the BSE announcements path recorded in `screens/README.md`.
3. Run a spear pass with Claude web on live web, which the CLAUDE.md SPEAR GATE
   requires for a new name in any case.
