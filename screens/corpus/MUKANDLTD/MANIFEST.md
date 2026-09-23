# MUKANDLTD corpus manifest

Company: Mukand Ltd
NSE: MUKANDLTD | BSE: 500460 | ISIN: INE304A01026
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
| Outcome of Board Meeting, Q1 FY27 consolidated results (12 Aug 2026) | 7158c4fd-e29c-4e17-a44f-044e0d847350 | 9 | 7, 8 | 2026-08-12 |
| Outcome of Board Meeting, FY26 audited results (14 May 2026) | ad15d838-32f6-403c-b50b-00312a184e3e | 12, 20 | 10, 11 | 2026-05-14 |
| Financial Results FY2026 Q4 | a978dec9-51ff-4a4c-9eec-467a5e7083b1 | 20 | none | FY2026 Q4 |
| Outcome of Board Meeting FY2026 Q4 | 4a02ca43-dfe7-48c1-ab4e-1e5ed78c210f | 20 | none | FY2026 Q4 |
| Dividend filing (FY26 results enclosure) | 21b49ed6-6832-4f8d-9ebf-dcf4058260d8 | 13, 20 | none | FY2027 Q1 |
| Agreements: Kalwa land term sheet (15 Jul 2026) | 9d3c00da-abd2-4ebd-9d9c-6bb54ecd54cb | 1, 3 | none | FY2027 Q2 |
| Update: second tranche received (19 Aug 2026) | dd4c7c0c-d4af-4f1f-9079-fd7d4dbe1fac | 1 | none | FY2027 Q2 |
| Annual Report FY25 | a74cd4a7-5523-4209-b347-b9f7d7087efe | 11 | none | FY2025 Q4 |

## Guidance records

`get_company_guidance` returned zero records on 2026-09-23.

## Known gaps

- Rupee size of the Q1 FY27 Kalwe land gain NOT FOUND.
- Total consideration of the AGP DC Infra Kalwa sale NOT FOUND.
- Promoter holding NOT FOUND. Credit rating NOT FOUND.
