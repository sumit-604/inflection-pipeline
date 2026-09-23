# KAVDEFENCE corpus manifest

Company: Kavveri Defence & Wireless Technologies Ltd
NSE: KAVDEFENCE | BSE: 590041 | ISIN: INE641C01019
Screened: 2026-09-23

## Corpus rule deviation (operator ruling 2026-09-08 applies)

No egress this session. The network policy answered 403 to docs.bull-ai.in,
www.bseindia.com, www.screener.in and the rating agency sites. The corpus is the
Bull AI chunk reader, which returns page-numbered text of the same filed PDFs.
Page numbers are the source PDF's own. Nobody holds the original file.

## Documents cited

**Read the two page columns honestly.** "Full page" means the page was read whole
with `get_document_chunks`. "Snippet" means the page came from a
`search_company_documents` extract: the id and page are real and openable, the
text is truncated. Some Bull AI labels carry the upload quarter, not the
reporting quarter; the label column says so where it matters.

| Document | Bull AI doc id | Pages, snippet | Pages, full page | Filed / label |
|---|---|---|---|---|
| Outcome of Board Meeting, Q1 FY27 standalone results | d9861a77-81e7-4181-9b63-40efcae38f21 | 3 | none | FY2027 Q1 |
| Financial Results FY2026 Q4 (consolidated) | dfb3a7b0-cebd-4494-858a-cf4eb4e04e15 | 29 | none | FY2026 Q4 |
| Outcome of Board Meeting FY2026 Q4 | 2972f6ba-d54e-4829-a294-cec15f4bb9c4 | 4, 29 | none | FY2026 Q4 |
| Outcome of Board Meeting FY2026 Q4 (second filing) | eaa0d298-5157-42fc-816c-4e4d5c0240c4 | 4, 29 | none | FY2026 Q4 |

## Guidance records

`get_company_guidance` returned zero records on 2026-09-23.

## Known gaps

- Direction of the many SAST filings NOT READ.
- Order book NOT FOUND.
- Credit rating NOT FOUND.
