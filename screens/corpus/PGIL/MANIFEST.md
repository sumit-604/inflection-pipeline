# PGIL corpus manifest

Company: Pearl Global Industries Ltd
NSE: PGIL | BSE: 532808 | ISIN: INE940H01022
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
| Investor Presentation labelled FY2027 Q2 (Q4 FY26 deck) | ad02a6fc-d421-45ea-9584-5b15420057e7 | 12, 17 | none | FY2027 Q2 label |
| Earnings Call Transcript labelled FY2027 Q2 (Q4 FY26 call) | 1a5d0e97-b99d-4f12-af13-253823b474f2 | 5, 6 | none | FY2027 Q2 label |
| Investor Presentation FY2026 Q4 (Q3 FY26 deck) | d826469d-bf4f-462f-8982-016f72b49d63 | 13 | none | FY2026 Q4 |
| Investor Presentation FY2026 Q4 (second copy) | 33632b0f-f783-4804-816c-d4c14a48df23 | 12 | none | FY2026 Q4 |

## Guidance records

Pulled with `get_company_guidance` on 2026-09-23. Each record cites a document
id (first 8 characters) and page. Deliveries are self-reported and do not verify
guidance.

- 33632b0f: pages 5, 6, 9, 11, 13
- 4fec8856: pages 3, 4, 5, 8, 12, 15
- 589777bd: pages 6, 7, 9, 10, 33, 34, 35, 48
- 85496042: pages 2, 4, 5, 6, 7, 9, 12, 13
- c1fe07b1: pages 5, 6, 7, 9, 10, 11, 12, 15, 19

## Known gaps

- Q1 FY27 numbers NOT FOUND this run.
- Promoter holding NOT FOUND.
- Credit rating NOT FOUND.
