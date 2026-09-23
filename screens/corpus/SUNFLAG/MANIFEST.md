# SUNFLAG corpus manifest

Company: Sunflag Iron & Steel Co Ltd
NSE: SUNFLAG | BSE: 500404 | ISIN: INE947A01014
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
| Financial Results FY2026 Q4, audited (29 May 2026) | 9ac6034b-cd4a-484d-aba7-42e953193904 | 14 | 1 to 8, 10 to 13 | 2026-05-29 |
| Outcome of Board Meeting, Q1 FY27 results (11 Aug 2026) | 3fab0c09-2dad-4094-894b-980d976bafad | 10 | 1 to 4, 7 to 9 | 2026-08-11 |
| Dividend filings FY2027 Q1 (FY26 results enclosure) | c4a8f07d-8372-4d47-a393-63931a92992a / d4c4733c-868a-4272-8f73-7a38e691b27e | 2, 9, 14, 17 | none | FY2027 Q1 |
| Outcome of Board Meeting (Q1 FY27, second filing) | aa6c8e7c-4d0e-492e-a0d6-84b007766cfa | 5, 6 | none | FY2027 Q1 |
| SAST Reg 29(2), Sanghavi group (non-promoter) | da4d061d-22b5-4c18-a57d-82a29ab03be8 / 86be9e70-c5a0-44a5-aa07-b76238af6f79 | 1, 2 | none | FY2027 Q1 / FY2026 Q2 |

## Guidance records

`get_company_guidance` returned zero records on 2026-09-23.

## Known gaps

- Promoter holding NOT FOUND.
- Percentage stake and share count in Lloyds Metals & Energy NOT FOUND.
- No concall, no guidance.
