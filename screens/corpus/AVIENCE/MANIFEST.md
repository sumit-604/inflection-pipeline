# AVIENCE corpus manifest

Company: Avience Biomedicals Ltd
NSE SME: AVIENCE (NSE only, not BSE listed) | ISIN: INE0V9I01017 | Listed 25-Jun-2026
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
| Investor Presentation FY2027 Q1 (financial highlights, outlook, revenue mix) | b429aa83-62e4-4201-92cf-a5d35761e5a4 | 22, 24, 28 | 2026-07-24 |
| PROSPECTUS | 78f9e436-8b93-487c-93d0-4daa47488da2 | 89, 91, 93, 367, 379 | 2026-06-25 |
| RHP | 03506277-2c74-462a-88b0-d3c421e38ab9 | 378, 379 | 2026-06-25 |
| DRHP | 3e821dd5-e36a-4cb8-b0c5-da394a77a83b | 88, 90, 91, 353 | 2026-06-12 |

**Full-page verification pass, 2026-09-22.** Read in full via `get_document_chunks`: b429aa83 p22-24. **Reader defect: 78f9e436 p366-368 (restated P&L) returns empty chunks on two attempts.** The FY23-FY25 profit history remains snippet-sourced.

## Known gaps

- **No post-listing financial result of any kind.** The company listed
  25-Jun-2026 and the latest financial period in this corpus ends 31-Mar-2026,
  before listing. The framework's two-period proof test cannot be run.
- **Balance sheet and cash flow NOT FOUND.** Leverage, working capital and cash
  conversion are entirely unobserved. This is the largest gap on the card.
- **Credit rating NOT FOUND.** Agency sites unreachable.
- One earnings call transcript is indexed (FY2026 Q4, uploaded 2026-07-28) and
  was **not read**. A deep run should retrieve it.
- Every competitive claim on the card is an issuer claim and is marked as one.
