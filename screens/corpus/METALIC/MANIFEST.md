# METALIC corpus manifest

Company: Metalic Technoforge Ltd
NSE: METALIC (NSE only, not BSE listed) | ISIN: INE1II801013 | Listed Jul/Aug-2026
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
| RHP | 23039ecc-c804-49dc-8c98-738969c09dc5 | 37, 61, 108, 140, 269, 288 | 2026-07-21 |
| PROSPECTUS | 8ccee046-b098-484b-89ca-8d7619ddb950 | 60, 61, 62, 268, 287, 321 | 2026-07-28 |
| DRHP | 8a8aa7b4-d307-40df-8cbc-4021577e0c31 | 258, 288 | 2026-03-31 |

**Full-page verification pass, 2026-09-22.** Read in full via `get_document_chunks`: 23039ecc p37, p108-110. **Reader defects: 23039ecc p139-141 (peer table) and 8ccee046 p287-288 and p319-322 return empty chunks on two attempts each.** Those remain snippet-sourced.

## Known gaps

- **No post-listing financial result of any kind.** The index holds only the
  three offer documents plus two August 2026 general updates. The framework's
  two-period proof test cannot be run.
- **FY2026 balance sheet and cash flow NOT FOUND.** The FY24 peer table gives
  debt-equity of 1.40 and a current ratio of 1.00, the weakest of four named
  peers on both, but those figures are two years old.
- **Credit rating NOT FOUND.** Agency sites unreachable. No lender no-objection
  letter was located either.
- **Post-issue per-promoter holding is blank** in the document read; only the
  83.62% pre-issue total and the 61.00% post-issue group total are stated.
- **Zero management guidance records.** No forward number in any document.
- **OPERATOR DATA CONFLICT.** The screen list carries "revenue TTM ~Rs 343 cr
  (Jul-2026 data)". The company's own restated FY2026 revenue from operations is
  **Rs 95.55 crore**. The operator figure appears to belong to another entity and
  must be reconciled before any deep run. Flagged at the head of the card.
- Every competitive claim on the card is an issuer claim and is marked as one.
