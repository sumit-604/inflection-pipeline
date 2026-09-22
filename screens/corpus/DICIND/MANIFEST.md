# DICIND corpus manifest

Company: DIC India Ltd
NSE: DICIND | BSE: 500089 | Calcutta SE: 10013217 | ISIN: INE303A01010
Screened: 2026-09-22

## Corpus rule deviation (operator ruling 2026-09-08 applies)

No egress this session. The network policy answered 403 to the CONNECT for
docs.bull-ai.in, www.bseindia.com, www.screener.in and every rating agency site.
The corpus is the Bull AI chunk reader, which returns page-numbered text of the
same filed PDFs. Page numbers are the source PDF's own. Nobody holds the
original file.

## Documents cited

**Read this column honestly.** Only three documents in the whole run were read as
full pages via `get_document_chunks`: TIRUPATIFL page 3, QLL pages 13 to 15, and
DICIND page 106. Every other page below was sourced from a
`search_company_documents` **snippet**, which carries the document id and the
page number but is a truncated extract, not the full page. The cites are real
and openable. They are not full-page reads.

## Reporting-calendar warning

**DIC India reports to a 31 December year end.** Bull AI's Indian fiscal labels
are wrong for this company: its "FY2025" is the calendar year ended 31 December
2025. Same defect class the 2026-09-21 run recorded for ELANTAS. Every period on
the card is stated as a calendar year.

| Document | Bull AI doc id | Pages cited | Filed / uploaded |
|---|---|---|---|
| Reg. 34(1) Annual Report CY2025 (MD&A, ratios, P&L, equity, dividend) | e67b4bd9-8b53-4590-9ac3-20b577d2a4a3 | 39, 49, 51, 105, 106 | FY2025 label, CY2025 |
| Change in Management, new MD and whole-time director | 277da0a9-213b-44d6-8cd9-4475c44f56d0 | 1, 3 | 2026-07-15 |
| Change in Management, Deputy CEO appointment | a7edde61-2b36-4da3-a735-d7edd9428881 | 1, 2 | 2026-07-04 |
| Outcome of Board Meeting, MD and CEO resignation | b3f28d78-842d-4c7b-abd8-f28c6538fe36 | 2 | 2026-06-02 |
| Financial Results, quarter and year to 31-Dec-2024 | 1844f064-88c2-49be-87a1-6c1273f8de49 | 9 | 2025-02-21 |
| Financial Results, quarter to 31-Mar-2024 | 178b3c64-0228-4779-ac59-b65c400964da | 4 | 2024-05-09 |
| Financial Results, quarter and six months to 30-Jun-2024 (KOPT dispute) | 8d0ce5d9-d334-40e3-8684-ee0f3a124c2d | 6 | 2024-08-13 |
| Reg. 34(1) Annual Report CY2024 (product range) | ee7af539-71ba-4430-9a03-ac97bd608f7c | 11 | FY2024 label |
| Reg. 34(1) Annual Report CY2023 (EPS) | 7bf69c28-c556-4752-9850-7513274dd279 | 103 | FY2023 label |
| Reg. 34(1) Annual Report CY2022 (MD&A, threats, P&L) | f3eaa801-6f27-4157-8464-55091bff063b | 44, 88 | FY2022 label |
| Financial Results, quarter and nine months to 30-Sep-2025 | 94f1b7ae-8aa5-4a08-ba9f-396f9cf313fb | 3 | FY2026 Q2 label |
| Certificate under Reg. 74(5) | c05d5ffb-61fb-4a0e-9208-b5ac738142fb | 1 | 2026-07-08 |

## Known gaps

- **Latest disclosed period is nine months stale.** CY2025 closed 31-Dec-2025.
  The H1 CY2026 result, the first under the new management, is not indexed.
- **Cash flow statement NOT FOUND.** Cash conversion INDETERMINATE and the
  verdict capped accordingly. Every working-capital ratio deteriorated in CY2025.
- **Credit rating NOT FOUND.** Agency sites unreachable. Substitute is the
  company's own audited ratio disclosure: debt-equity 0.01, interest cover 9.23x.
- **Promoter holding percentage NOT FOUND.** The promoter is DIC Corporation of
  Japan; no shareholding pattern is indexed.
- **Zero management guidance records.** No presentation, no earnings call.
- **Allotment of Warrants filing (2026-05-14) indexed and NOT READ.** A debt-free
  company issuing warrants needs explaining. A deep run must retrieve it.
- **A continuous litigation-pendency stream is indexed and NOT READ**, including
  seven filings in FY2026 Q3 alone. The KOPT compensation dispute is partly
  visible: of a Rs 277.95 lakh demand, Rs 142.17 lakh is not acknowledged as debt.
