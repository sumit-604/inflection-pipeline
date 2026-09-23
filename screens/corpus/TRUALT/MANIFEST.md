# TRUALT corpus manifest

Company: TruAlt Bioenergy Ltd
NSE: TRUALT | BSE: 544545 | ISIN: INE0MWH01014
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
| Earnings Call Transcript labelled FY2027 Q2 (Q4 FY26 call, uploaded 1 May 2026) | 8d721d93-2b96-4c75-b9af-38010a33b9e7 | none | 9, 10 | 2026-05-01 |
| RHP (IPO, 2025) | c81120b8-a087-4ec6-b825-3721e91953a8 | 541 | none | FY2026 Q3 |
| Investor Presentation FY2026 Q2 (Q1 FY26) | 9150e72d-ea21-43c5-9110-45391572ff71 | 10, 12, 13 | none | FY2026 Q2 |
| Investor Presentation FY2026 Q2 (Q2 FY26) | df97dddb-f65a-4f27-b89e-131377807f75 | 26 | none | FY2026 Q2 |

## Guidance records

Pulled with `get_company_guidance` on 2026-09-23. Each record cites a document
id (first 8 characters) and page. Deliveries are self-reported and do not verify
guidance.

- 090cc7a4: pages 7, 13, 14, 25, 27, 30
- 503863ee: pages 5, 6, 7, 8, 9, 10, 14, 16, 23, 29
- 87391b64: pages 3, 15, 20
- c3c690dd: pages 6, 7, 10, 30, 31, 33

## Known gaps

- Q1 FY27 numbers NOT FOUND this run.
- Credit rating (new, filed Apr 2026) listed but NOT READ.
- ESY 2026-27 OMC allocation quantity NOT FOUND.
