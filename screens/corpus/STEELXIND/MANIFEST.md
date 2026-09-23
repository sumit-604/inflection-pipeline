# STEELXIND corpus manifest

Company: Steel Exchange India Ltd
NSE: STEELXIND | BSE: 534748 | ISIN: INE503B01021
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
| Press Release (Revised), Q1 FY27 (21 Jul 2026) | 05f79691-e856-4ece-ad83-678958fdcb80 | 3 | 1, 2 | 2026-07-21 |
| Earnings Call Transcript labelled FY2027 Q2 (Q4 FY26 call) | 3554d050-e523-43ca-8227-20dcf0b1609d | 4, 10, 12 | none | FY2027 Q2 label |
| AGM notice FY2027 Q2 | 90551ca9-092f-46af-b322-624d1f94c9ef | 10 | none | FY2027 Q2 |

## Guidance records

Pulled with `get_company_guidance` on 2026-09-23. Each record cites a document
id (first 8 characters) and page. Deliveries are self-reported and do not verify
guidance.

- 0baf3c20: pages 2, 3
- 68d5aed8: pages 12, 19, 20
- b0c048a8: pages 3, 4, 5, 6, 10, 11, 12, 13

## Known gaps

- Q1 FY27 revenue split, volumes in tonnes NOT FOUND.
- Post-conversion share count and outstanding warrants NOT FOUND.
- Credit rating NOT FOUND.
