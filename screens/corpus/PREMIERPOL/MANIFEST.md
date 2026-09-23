# PREMIERPOL corpus manifest

Company: Premier Polyfilm Ltd
NSE: PREMIERPOL | BSE: 514354 | ISIN: INE309M01020
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
| Financial Results Q1 FY27 (standalone) | 6af25d23-b9e3-4c70-be68-4a5e28a42eaa | 2, 3, 4 | none | FY2027 Q1 |
| Outcome of Board Meeting Q1 FY27 (18 Jul 2026) | 3111b6c9-9dec-43ae-912d-50e694617ba2 | 3, 4, 5 | none | FY2027 Q1 |
| Crisil rating letter, reaffirmation (10 Aug 2026) | a7fb5320-56b2-4056-8f56-89c10b51f22f | 2, 3, 4 | none | FY2027 Q2 |
| Crisil rating rationale | 61ece46a-ee58-4e59-a5c8-2aa6e978c80c | 4, 7, 8 | none | FY2027 Q2 |
| SAST Reg 29(2): D L Millar & Co; Mayank Goenka | 653989a6-1830-4cf8-a048-e448b000c2cc / 376b8a73-acea-4c1c-a5ca-02196b9b5271 / 61da77f2-ed2e-4f22-99f8-51da6f2ece60 | 2, 3 | none | FY2027 Q1 to Q2 |

## Guidance records

`get_company_guidance` returned zero records on 2026-09-23.

## Known gaps

- Total promoter holding NOT FOUND.
- Reason for the two "Reply to Clarification" filings NOT READ.
- No concall, no guidance.
