# ADVANCE corpus manifest

Company: Advance Agrolife Ltd
NSE: ADVANCE | BSE: 544562 | ISIN: INE1B0W01010
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
| Investor Presentation FY2027 Q1 (Q1 FY27 deck) | 23387b30-081f-4558-8c37-69ed73c18588 | 6, 15, 17, 20, 22, 23, 25 | 26, 27, 28, 29, 30 | 2026-08-06 |
| Investor Presentation FY2026 Q4 (Q4 FY26 deck) | e7e86360-f49a-45ca-909e-925899ab0098 | 22, 28, 29 | 25 to 30 (mostly images) | 2026-05-01 |
| Investor Presentation FY2026 Q4 (Unit-4 timing, earlier deck) | 409302c5 | 24 | none | FY2026 Q4 |
| RHP (IPO, 2025) | c3b6b935-1cf7-4ac0-a2fb-67098b89f1f1 | 34, 122 | none | FY2026 Q3 |

## Guidance records

Pulled with `get_company_guidance` on 2026-09-23. Each record cites a document
id (first 8 characters) and page. Deliveries are self-reported and do not verify
guidance.

- 23387b30: pages 6, 15, 17, 20, 23
- 409302c5: pages 3, 6, 15, 17, 20, 24, 25

## Known gaps

- Pledge NOT FOUND.
- Credit rating NOT FOUND (agency sites unreachable).
- FY26 working-capital days NOT FOUND (chart cut at FY25).
- No earnings-call transcript read.
