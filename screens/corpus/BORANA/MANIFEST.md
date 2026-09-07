# Corpus manifest: BORANA (Borana Weaves Ltd)

Collected 2026-09-07 via Bull AI MCP (search_company_documents). Operator: Keerti Kaushik.

## Method note (read first)
On this Bull AI account the raw document reader (get_document_chunks) returns
empty. The working reader is search_company_documents, which returns page-cited
passages, not full PDF text. So this corpus is a set of page-cited passages, not
the whole documents. Every passage keeps its doc type, fiscal year, quarter, and
page. Raw PDFs were not downloadable in this container. Credit-rating reports are
not carried by Bull AI, so none is included. Both gaps are marked in the card.

## Passages held (see bullai-extracts.md)
| Source | Type | Period | Pages cited |
|---|---|---|---:|
| Investor Presentation | presentation | FY26 Q4 | 4, 27, 30 |
| Investor Presentation | presentation | FY26 Q3 | 24, 28, 29, 31 |
| Investor Presentation (guidance/AR highlights, HlJATJ) | presentation | FY26 | 6, 28, 29, 32, 33 |
| Investor Presentation | presentation | FY26 Q4 (key strengths) | 9 |
| Earnings Call Transcript | transcript | FY26 Q3 (27-Jan-2026) | 6 |
| Reg. 34(1) Annual Report | annual_report | FY25 | 39, 54, 63 |

## Coverage gaps
- Latest full annual report (FY26) text not retrieved beyond highlights.
- No credit-rating report (not in Bull AI).
- Last-two-results filings not pulled as documents; quarterly numbers taken from
  the investor presentations that report them.
