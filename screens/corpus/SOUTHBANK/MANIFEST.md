# SOUTHBANK corpus manifest

Company: The South Indian Bank Ltd
NSE: SOUTHBANK | BSE: 532218 | ISIN: INE683A01023
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
| Investor Presentation FY2026 Q4 | df63309d-384c-4690-88df-8ff0b3a027de | 41, 42, 43 | 37, 38, 39, 40 | 2026-05-06 |
| Investor Presentation FY2027 Q1 | b6415007-a847-474f-bfaf-3c62ed742c9e | 7 | 8 to 16 returned empty chunks | FY2027 Q1 |
| Investor Presentation labelled FY2027 Q2 (Q4 FY26 content) | 5096b805-c834-47f6-b078-0bb0a7ca03d8 | 41, 42 | none | FY2027 Q2 label |
| Earnings Call Transcript labelled FY2027 Q2 (Q4 FY26 call) | 8a56949d-21fe-4774-8e56-ea1b95242a97 | 4 | none | FY2027 Q2 label |

## Guidance records

Pulled with `get_company_guidance` on 2026-09-23. Each record cites a document
id (first 8 characters) and page. Deliveries are self-reported and do not verify
guidance.

- 249f4a17: pages 3, 4, 5, 7, 11, 13, 14
- 7a0c092a: pages 6, 7, 10, 14
- b1d5af82: pages 7, 8, 11, 23, 27, 29
- b3dc776b: pages 2, 3, 8, 9, 11, 16
- df63309d: pages 5, 8, 9, 12, 17, 34
- f223abd0: pages 2, 3, 4, 10, 12, 22

## Known gaps

- Shareholding pattern NOT FOUND.
- Q1 FY27 GNPA, NNPA and P&L page NOT FOUND (deck pages 8 to 16 empty).
- Nature of the Rs 1,300 crore Q4 FY26 GNPA deduction NOT FOUND.
