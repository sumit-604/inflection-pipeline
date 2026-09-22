# ISFT corpus manifest

Company: Intrasoft Technologies Ltd
NSE: ISFT | BSE: 533181 | ISIN: INE566K01011
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

| Document | Bull AI doc id | Pages cited | Filed / uploaded |
|---|---|---|---|
| Investor Presentation FY2027 Q2 (Q1 FY27 P&L, business model, targets) | c0b6f688-126f-45b7-9be8-d2f94aa9936c | 4, 9, 10, 13, 16 | 2026-08-13 |
| Outcome of Board Meeting, Q1 FY27 standalone and consolidated results | ef4282bd-60db-495e-ad77-c9a65ed111e2 | 4, 6 | FY2027 Q1 |
| Reply to Clarification - Financial results, audited FY26 | 57d5c8b4-79d8-421d-bf9d-51c22bcf49d5 | 8, 15 | FY2027 Q2 |
| Press Release / Media Release, Q4 and FY26 results | aaf699b1-4252-40fa-bafe-68f1c277a0db | 2 | 2026-05-27 |
| Investor Presentation FY2026 Q4 (transformation narrative, guidance) | f7842b1a-a4e4-4c80-ab16-69bdf059aec4 | 4, 5, 9, 10, 12, 13, 14, 16 | FY2026 Q4 |
| Investor Presentation FY2027 Q2 (second deck) | 5205262b-f7d2-455d-8e27-bb8c98527199 | 10 | FY2027 Q2 |
| Investor Presentation FY2022 Q2 (historic e-commerce P&L) | d43b64d1-e7c6-4dad-b42e-5cc129d7cad7 | 4, 7 | FY2022 Q2 |
| Investor Presentation FY2021 Q4 (historic) | 0e3e9ec9-ed14-41ef-9dd1-5dc99d4be906 / 8bf11832-f554-4049-876a-955c7768fb02 | 4, 7 | FY2021 Q4 |

## Known gaps

- **Balance sheet and cash flow NOT FOUND.** The company claims a working-capital
  transformation out of inventory. The cash flow statement is exactly the
  document that would prove it, and it is absent.
- **Promoter holding percentage NOT FOUND.** No shareholding pattern indexed.
- **Credit rating NOT FOUND.** Agency sites unreachable. The company carries
  almost no debt, which is likely why none exists.
- **The only indexed earnings call transcript is FY2020.** No recent concall.
- **A "Reply to Clarification - Financial results" filing exists for FY2027 Q2.**
  The exchange queried the company about its results. The query and answer were
  not read. A deep run must retrieve them.
- US tariff exposure and currency hedging policy are both NOT FOUND.
