# Corpus manifest: AUROIMPEX (Auro Impex & Chemicals Ltd)

Attempted 2026-09-11. Operator: Keerti Kaushik.
STATUS: NOT COLLECTED. NO CARD WRITTEN. This file is a collection ledger, not an analysis.

## Identity, resolved
NSE symbol AUROIMPEX, series SM (the NSE Emerge SME platform). ISIN INE0NUL01018.
No BSE listing. Incorporated 20-Jan-1994 at Kolkata, West Bengal, as Auro Impex & Chemicals
Private Limited. Described in its own exchange filing as "an Auro Group Company".
Identity resolved from cloud search result metadata only. No filed document has been read.

## Why nothing was collected
Two independent routes both closed in this session.

1. Bull AI does not index this company. `search_companies` returns nothing for the name, for
   "AUROIMPEX", or for ISIN INE0NUL01018. `list_document_availability` on AUROIMPEX returns
   "No listed company was found for the supplied identifier." Bull AI's SME Emerge coverage
   misses this scrip. Note that it does carry other SME names, so this is a per-scrip gap,
   not a blanket SME exclusion.
2. The network policy denies egress. CONNECT to www.nseindia.com, nsearchives.nseindia.com
   and the company's own site all fail with the proxy's 403, as they do for screener.in,
   BSE and the rating agencies.

Cloud search still works and was used only for what the funnel rule permits: finding which
documents exist and where. It is not the source of any number, and no number from it appears
in this repository.

## Document ledger, located but NOT fetched
Every URL below came from cloud search result metadata. None has been opened, downloaded or
read. Treat each as a lead for the collector, not as evidence.

Company investor site, auroimpex.com:
| Document | URL |
|---|---|
| Annual report FY2025-26 | https://auroimpex.com/wp-content/uploads/2026/08/Annual-Report-13.pdf |
| Annual report FY2024-25 | https://auroimpex.com/wp-content/uploads/2025/08/Annual_Report_2025.pdf |
| Annual report FY2023-24 | https://auroimpex.com/wp-content/uploads/2024/09/Annual_Report_2023_24.pdf |
| Annual report FY2022-23 | https://auroimpex.com/wp-content/uploads/2023/09/Annual_Report_2022-23.pdf |
| Red Herring Prospectus (2023 IPO) | https://auroimpex.com/wp-content/uploads/2023/06/RHP.pdf |
| Financial statements index | https://auroimpex.com/financial-statement/ |
| Shareholding pattern / corporate governance | https://auroimpex.com/corporate-governance/ |
| Notices and announcements | https://auroimpex.com/notice-announcements/ |
| FY2025-26 financials landing page | https://auroimpex.com/financials/2025-2026/ |
| Group companies | https://auroimpex.com/group-companies/ (path inferred from site navigation, unconfirmed) |

NSE archive (nsearchives.nseindia.com/corporate/):
| Document | File |
|---|---|
| Annual report FY2022-23 | AUROIMPEX_06092023155257_AUROIMPEXANNUALREPORT202223.pdf |
| Reply to an NSE query dated 26-Jun-2023 | AUROIMPEX_04072023111732_NSEReply260623.pdf |
| Pre-AGM newspaper publication, Aug 2026 | AUROIMPEX_18082026162438_Newspaper_Publication_Pre_AGM.pdf |

## What the collector should pull, in priority order
1. Annual report FY2025-26, then FY2024-25 and FY2023-24. Three years gives a trend and the
   related-party schedule.
2. The Red Herring Prospectus. LESSONS.md carries this as law for recently listed names: the
   prospectus holds the promoter and group history plus restated pre-IPO financials, and its
   absence thins the backward baseline. This company listed on Emerge in 2023.
3. The half-yearly results for the half years ended 30-Sep-2025 and 31-Mar-2026, from the
   financial statements page.
4. The shareholding pattern, for promoter holding and pledge.
5. The reply to the NSE query of 26-Jun-2023. An exchange query and its answer is worth
   reading before anything else in the governance file.
6. Any credit rating rationale. None was located; the agency sites are blocked.

## One structural constraint to carry into the read
The company reports HALF-YEARLY, not quarterly. Its own site lists results for the half year
ended 30-Sep-2025 and for the half year and year ended 31-Mar-2026. That is the SME
reporting regime. It gives two observation points a year, not four, so the Role 5 delivery
test and the trailing-four-quarters weighting in CLAUDE.md cannot be run in their normal
form. Decide how to handle that before the read, not during it.
