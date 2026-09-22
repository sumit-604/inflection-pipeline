# QLL corpus manifest

Company: Qualitek Labs Ltd
BSE: 544091 (BSE only, no NSE listing) | ISIN: INE0Q1R01012
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
| Investor Presentation FY2027 Q2 (FY26 results, standalone and consolidated) | 963edab6-e77e-40ef-91d4-625fb09ba902 | 10, 16, 18, 23, 24, 25 | FY2027 Q2 |
| Press Release / Media Release, FY26 MD&A | dd6eb132-e410-4a9b-831c-40224bd109f2 | 2 | FY2027 Q1 |
| Guidance source deck (FY26 deliveries and FY27 targets) | 1cba2683-aa43-4ae8-b351-b8f4c65a2e50 | 4, 7, 23, 24, 25 | FY2026 Q4 |
| Outcome of Board Meeting, audited FY26 results, balance sheet, cash flow | 938a5098-dfd5-492e-9c11-76075faf5958 | 4, 13, 14, 15 | 2026-05-20 |
| Financial Results FY2026 Q4 | b9aa42b4-9348-4105-9a2d-9207339a6f3a | 4 | 2026-05-20 |
| Investor Presentation FY2025 Q4 | 0bbbd347-88db-4b8d-8674-7a9f79942572 | 6 | 2025-05-30 |
| Reg. 34(1) Annual Report FY2024 | 6d619bd7-9bfe-4b15-a964-d94ef1c27092 | 103 | FY2024 Q4 |
| SAST Reg. 31(4) promoter encumbrance declaration | 37c59b6f-30da-40b1-877a-742e6f0e85f2 | 1 | 2026-04-06 |
| General, HDFC credit facility corporate guarantee | b0452740-452e-4dcf-ad60-80ab96f896bc | 1, 2 | 2025-12-11 |

## Known gaps

- **Consolidated balance sheet and cash flow NOT FOUND.** Only the standalone
  statements were located. The subsidiaries hold 46% of group revenue, so group
  leverage and group cash conversion are unobserved. Cash conversion is recorded
  INDETERMINATE and the verdict is capped at PROCEED WITH CAVEATS.
- **No earnings call transcript exists** in the index for this company.
- **Credit rating NOT FOUND.** No rating rationale indexed under any category.
  Agency sites unreachable.
- **Promoter holding percentage NOT FOUND.** No shareholding pattern indexed.
- Company reports half-yearly. Latest period ends 31 March 2026; six months are
  unobserved.
