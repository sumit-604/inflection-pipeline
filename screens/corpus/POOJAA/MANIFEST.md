# POOJAA corpus manifest

Company: Poojaa Precision Engg. Limited (formerly Pooja Castings Private Limited)
BSE: 544844, SME platform of BSE | ISIN: INE288301026 | NSE: none
Incorporated 12-Aug-1992. Chakan, Pune.
Screened: 2026-09-28

## Corpus rule deviation (operator ruling 2026-09-08 applies)

No egress this session. The corpus is the Bull AI chunk reader over the same
filed PDF. Page numbers are the source PDF's own. Nobody holds the original.

## Documents read

| Document | Bull AI doc id | Pages read | Period |
|---|---|---|---|
| Red Herring Prospectus | 2e4307f1-c1df-4ba0-bb87-6119c09155a1 | 95 to 100, 135 to 143 (chunk reads); 26, 27, 63, 90, 91, 112, 116, 144, 197, 200, 205, 206, 217, 223, 243, 254, 266 (search snippets) | Uploaded 2026-07-28, indexed FY2027 Q2 |
| Bull AI guidance record (get_company_guidance) | none | n/a | **zero records** |

## This is the whole corpus

`list_document_availability` returned a complete, untruncated map with one
document: the RHP. No results filing, no investor presentation, no transcript,
no annual report, no rating, no listing-day filing. Every competitive and
operating claim on the card is an **issuer claim** from the offer document.

## Bull AI calls

11 billable: 1 guidance, 3 chunk reads (one returned empty), 7 searches.
Availability maps were free.

## Reader defects

- Chunk read of RHP pages 201 to 205 returned zero chunks, though a search
  returned page 205 (the restated cash-flow statement) as a truncated snippet.
  Net cash from operations is NOT FOUND for that reason.
- RHP page 143 ends with a broken customer table ("| 140 |"); page 144 carries
  the clean table and is used.

## Known gaps

- Issue price, final issue size and listing date NOT FOUND (RHP shows [●]).
- Net operating cash flow NOT FOUND (see reader defects).
- Total borrowings at 31-Mar-2026 NOT FOUND as a single figure. Bridge loans of
  Rs 18.75 crore to be repaid from proceeds are on page 98.
- Customer names NOT FOUND (RHP anonymises them).
- **No post-listing result.** SME platform, half-yearly reporting. The latest
  financial period ends 31-Mar-2026. H1 FY27 is not yet reported.
- Credit rating NOT FOUND. Pledge NOT FOUND.

## Price basis

Not a corpus document. Bull AI company record, market capitalisation
Rs 1,627.21 crore, read 2026-09-28.
