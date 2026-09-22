# TIRUPATIFL corpus manifest

Company: Tirupati Forge Ltd
NSE: TIRUPATIFL (NSE only, not BSE listed) | ISIN: INE319Y01024
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
| Outcome of Board Meeting, Q1 FY27 results with full P&L and FY26 year column | 3597dd48-b653-4e87-937c-debe8d727c12 | 3, 4, 11 | 2026-08-13 |
| Shareholders meeting, EGM proceedings, promoter warrant issue | 28a5b33f-b129-455c-bcb7-734341a89133 | 3, 4 | 2026-07-31 |
| Shareholders meeting, scrutiniser's report | ba1dec8d-d3d1-489a-8754-1849073569f0 | 4 | FY2027 Q2 |
| Reg. 34(1) Annual Report FY2025 | a9517fdf-19b1-46ee-87fb-7b0a22aa7810 | 58, 59, 63 | FY2025 Q4 |
| Outcome of Board Meeting FY2026 Q4 (capacity and business profile) | d60df1a5-f97b-49e8-bb4b-022de6bf4ae1 | 25, 26 | FY2026 Q4 |
| Outcome of Board Meeting FY2026 Q3 (H1 FY26 results, business profile) | 58f61d4c-e75c-45ba-bc66-57c67e0e7f56 | 5, 21 | 2025-11-11 |
| Outcome of Board Meeting FY2026 Q3 (second filing) | fb9214e2-3b83-43e9-8bfe-25a0be642378 | 21 | FY2026 Q3 |
| Investor Presentation FY2026 Q3 | ce2c446d-8596-498a-9001-de4003611d64 | 7 | 2026-02-01 |
| Financial Results FY2025 Q3 | 06a99561-b125-4bbe-ab37-f7d7bab6bfd4 | 5 | 2024-11-14 |

## Known gaps

- **FY2026 annual report NOT FOUND.** Only the FY2025 annual report is indexed.
- **Balance sheet and cash flow NOT FOUND.** Working capital behind a 41% revenue
  increase is entirely unobserved.
- **Credit rating NOT FOUND.** Agency sites unreachable. The company self-reports
  nil outstanding default on all loan and debt-security lines.
- **Promoter holding percentage NOT FOUND.** No shareholding pattern indexed.
- **Zero management guidance records.** Bull AI holds no guidance of any kind for
  this company. Recorded as a finding on the card.
- **Two filings indexed and not read**, both of which a deep run must retrieve:
  a "Price movement" filing (FY2026 Q3, 2025-10-09) and an "Action(s) initiated
  or orders passed" filing (FY2026 Q2, 2025-08-05).
- No order book and no customer concentration disclosure exists anywhere.
