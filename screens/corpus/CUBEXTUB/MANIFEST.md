# CUBEXTUB corpus manifest

Company: Cubex Tubings Ltd
NSE: CUBEXTUB | BSE: 526027 | ISIN: INE144D01012
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
| Annual Report FY26 (filed with AGM notice) | 3abf8f69-b0f9-4381-a94d-4d257cfd0d5a | 20, 54, 63 | none | FY2027 Q2 |
| Annual Report FY25 | ebc06869-db84-4380-b8ce-bdb2e408008d | 6, 17, 73, 75 | none | FY2025 Q4 |
| Integrated Filing, Financial, Q4 FY25 results (15 May 2025) | 110e7f8a-f47a-4957-9349-d8644c339783 | 3 | none | FY2026 Q1 |
| Financial Results FY2025 Q1 | 173d27d3-2d22-40ba-8515-c81c14431dce | 5 | none | FY2025 Q1 |

## Guidance records

`get_company_guidance` returned zero records on 2026-09-23.

## Known gaps

- No quarterly after Q4 FY26, no concall, no guidance.
- Promoter holding and pledge NOT FOUND.
- Credit rating NOT FOUND.
