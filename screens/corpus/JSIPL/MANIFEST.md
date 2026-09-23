# JSIPL corpus manifest

Company: Jindal Supreme (India) Ltd
NSE: JSIPL | BSE: 544935 | ISIN: INE1DLO01028
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
| Draft Red Herring Prospectus (restated to 31 Dec 2025) | cd71cb12-77c6-4478-8018-c85603c58e31 | 37, 65, 99, 172, 176, 190, 230, 275, 364 | none | FY2027 Q1 (Apr 2026) |

## Guidance records

`get_company_guidance` returned zero records on 2026-09-23.

## Known gaps

- DRHP only. FY26 audited accounts, RHP, prospectus and listing-day share count NOT FOUND.
- Promoter holding NOT FOUND.
- Credit rating NOT FOUND.
