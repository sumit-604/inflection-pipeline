# NOCIL corpus manifest

Company: NOCIL Ltd
NSE: NOCIL | BSE: 500730 | ISIN: INE163A01018
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
| Investor Presentation labelled FY2027 Q2 (content is the Q4 FY26 deck) | 03a8fa05-11e7-4929-94d7-8022f6688f26 | 6, 7, 28 | none | FY2027 Q2 label |
| Investor Presentation FY2027 Q1 (Q1 FY27 deck) | 565d872a-55c0-4ad3-a3a5-0396eeb4956b | 7 | none | FY2027 Q1 |
| Earnings Call Transcript labelled FY2027 Q2 (content is the Q3 FY26 call) | 5eb8ac01-78f4-4875-95ec-c811059752f6 | 5, 6 | none | FY2027 Q2 label |

## Guidance records

Pulled with `get_company_guidance` on 2026-09-23. Each record cites a document
id (first 8 characters) and page. Deliveries are self-reported and do not verify
guidance.

- 98be532a: pages 5, 7, 19, 23, 24, 25
- 9f1f8670: pages 4, 6, 10, 11, 12, 13
- bd47e02e: pages 3, 4, 5, 6, 11, 12, 13
- cb0c08df: pages 3, 4, 5, 7, 15, 17, 18
- cf585e0f: pages 6, 7, 9, 14, 15, 21

## Known gaps

- Promoter holding and pledge NOT FOUND.
- Credit rating NOT FOUND.
- Annual report FY26 not in corpus (AR FY21 to FY25 held, not read this run).
