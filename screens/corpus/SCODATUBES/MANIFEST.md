# SCODATUBES corpus manifest

Company: Scoda Tubes Ltd
NSE: SCODATUBES | BSE: 544411 | ISIN: INE090501011
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
| Investor Presentation FY2027 Q1 (13 Aug 2026) | 033c51c0-70f2-483d-a048-58a982ed839e | 6 | 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | 2026-08-13 |
| Earnings Call Transcript labelled FY2027 Q2 (Q1 FY27 call) | 5d192b4e-d359-4e4d-baba-e89b1d1da2e9 | 4 | none | FY2027 Q2 label |
| RHP (IPO, 2025) | 70f9844b-2fe8-4c0c-b783-c21044140936 | 199, 220 | none | FY2026 Q1 |
| Investor Presentation FY2025 Q4 | a4375a90-6651-4963-b718-83661dfb658a | 6 | none | FY2025 Q4 |

## Guidance records

Pulled with `get_company_guidance` on 2026-09-23. Each record cites a document
id (first 8 characters) and page. Deliveries are self-reported and do not verify
guidance.

- 033c51c0: pages 6, 28, 29
- 1f4fc506: pages 5, 6, 20, 30, 31
- 46b739c5: pages 2, 3, 4, 6, 9, 10
- 46cf27b5: pages 4, 5, 6, 8, 11, 12, 18

## Known gaps

- Q1 FY27 PBT build (depreciation, interest, tax) NOT READ.
- Shareholding pattern NOT READ.
- Current validity of PED, AD 2000 and ISO certificates NOT FOUND (deck page 16 shows lapsed dates).
- Credit rating NOT FOUND.
