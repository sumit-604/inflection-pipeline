# KDDL corpus manifest

Company: KDDL Ltd
NSE: KDDL | BSE: 532054 | ISIN: INE291D01011
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
| Investor Presentation FY2027 Q1 | 96ba2a93-5ef2-4830-8ba9-8cc71c372f5c | 18 | 6 | 2026-08-04 |
| Investor Presentation FY2026 Q4 | 0797cf68-3f62-46bd-8517-8da5ef8ffc8a | 7, 20 | none | FY2026 Q4 |
| Investor Presentations FY2026 Q3 | 00674ba8-9e51-4469-ace6-43b88424ff30 / fcb5184a-6ad1-4f9b-87f0-6a7cdf7c6c51 | 8, 18 | none | FY2026 Q3 |
| Financial Results FY2024 Q2 and Q1 (Ethos stake notes) | 4d80a77d-9664-4228-ac66-e49cb7f4bae3 / 2c847ca9-5ec2-4ec5-a956-4d6651d72bb1 | 10, 13, 19 | none | FY2024 |
| Annual Report FY24 (share capital note) | 71be5e85-c27a-44ce-8afa-463020c3936e | 187, 279 | none | FY2024 Q4 |

## Guidance records

Pulled with `get_company_guidance` on 2026-09-23. Each record cites a document
id (first 8 characters) and page. Deliveries are self-reported and do not verify
guidance.

- 0797cf68: pages 5, 7, 8, 12
- 0c42e7b0: pages 6, 7, 12
- 44af3e82: pages 3, 4, 5, 6, 9, 14, 17, 21
- 582181e0: pages 4, 5, 6, 10, 11, 12
- 77e28283: pages 5, 8, 11, 13, 15, 16, 18, 19, 22

## Known gaps

- Current Ethos stake NOT FOUND (last filed 51.34% at Q2 FY24).
- FY26 share count NOT FOUND (FY24 count used, dated).
- Minority-interest line NOT FOUND.
