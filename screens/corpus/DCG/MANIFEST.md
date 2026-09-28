# DCG corpus manifest

Company: DCG Cables & Wires Ltd (formerly DCG Copper Industries Pvt Ltd)
NSE: DCG (NSE EMERGE, SME platform) | ISIN: INE0S8401018
CIN L36999GJ2017PLC099290. BSE code: none in the Bull AI record.
Subsidiary: Mangalam Envago Products Pvt Ltd.
Reports half-yearly. Latest financial period ends 31-Mar-2026.
Screened: 2026-09-28

## Corpus rule deviation (operator ruling 2026-09-08 applies)

No egress this session. The corpus is the Bull AI chunk reader over the same
filed PDFs. Page numbers are the source PDF's own. Nobody holds the original.

## Documents read

| Document | Bull AI doc id | Pages read | Period |
|---|---|---|---|
| Outcome of Board Meeting, audited FY26 and H2 FY26 results, standalone and consolidated, 30-May-2026 | 269acade-67ad-4dfe-ab1d-45394eb4a320 | 1 to 20 | FY2026 Q4 |
| Reply to clarification, corrected consolidated audit report, 13-Jul-2026 (filed 17-Jul-2026) | 0fd17a18-313b-4b7f-b6ba-15952309edd8 | 1 to 6; 9, 18, 20 as search snippets | FY2027 Q2 |
| NSE order rejecting fine waiver, 23-Sep-2026 | 89bf2ab5-0cf4-4692-a959-bf3af2ef4ac3 | 3, 5, 6, 8, 9, 10 | FY2027 Q2 |
| AGM notice with FY26 Directors' Report, MD&A, secretarial audit | c2addc5d-1bda-48c2-9146-b0c0b480195c | 58 to 65, 68 to 70; 27, 28, 66, 67, 71 as search snippets | FY2026 Q4 index |
| Intimation, Phase II commencement, 11-Sep-2026 | 0d977298-329f-4fd2-bc2a-0120b01f5738 | 1 | FY2027 Q2 |
| NSE reminder before freezing promoter holdings, 16-Jul-2026 | 9075f704-3218-45c1-bb3e-83a59355bb51 | 6, 7 (search snippets) | FY2027 Q2 |
| Annual Report FY2023-24, MD&A | cc928b32-e1c9-4167-935d-ae065a293e31 | 51 (search snippet) | FY2024 |
| Management guidance records (get_company_guidance) | n/a | returned **zero records** | all |

## Known gaps

- **Credit rating NOT FOUND.** No rating filing in the availability map.
- Promoter holding percentage and pledge NOT FOUND. Promoter names only.
- No investor presentation, no concall transcript, zero guidance records.
- The FY25 annual report (upload 2025-09-06) is indexed; not read.
- Customer concentration NOT FOUND.
- Phase II capacity addition NOT FOUND; the intimation gives no number.
- H1 FY27 is unreported. Six months since 31-Mar-2026 are unobserved.

## Reader defects found

- AGM notice c2addc5d pages 66 and 67: the chunk reader returns **empty**,
  while search returns text from both pages. Page 67 capacity figures are
  taken from the search snippet.
- The consolidated auditor report in 269acade pages 13 and 14 is a **limited
  review report**, not an audit report. This is the company's own filing
  error, confirmed by the company (0fd17a18 p1) and by NSE (89bf2ab5 p8). The
  corrected report is in 0fd17a18.

## Document findings (not reader artefacts)

- The consolidated cash flow statement (269acade p19, p20) shows opening cash
  Rs 563.97 lakh and closing Rs 1,246.60 lakh. The consolidated balance sheet
  (p18) shows Rs 258.37 lakh and Rs 941.00 lakh. Both ends differ by about
  Rs 305.6 lakh. The line items are legible; the totals do not tie. Not
  investigated.

## Price basis

Not a corpus document. Bull AI company record, market capitalisation
Rs 135.40 crore, read 2026-09-28.

## Bull AI calls

8 billable: 1 guidance, 5 chunk reads (one returned empty), 2 searches.
Free: 2 availability maps.
