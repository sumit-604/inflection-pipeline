# UGARSUGAR corpus manifest

Company: The Ugar Sugar Works Ltd
NSE: UGARSUGAR | BSE: 530363 | ISIN: INE071E01023
CIN L15421PN1939PLC006738. Registered office Sangli, Maharashtra. Factories at
Ugar Khurd (Belagavi) and Jewargi / Nagarhalli-Malli (Kalaburagi), Karnataka.
Screened: 2026-09-28

## Corpus rule deviation (operator ruling 2026-09-08 applies)

No egress this session. The corpus is the Bull AI chunk reader over the same
filed PDFs. Page numbers are the source PDF's own. Nobody holds the original.

## Documents read

| Document | Bull AI doc id | Pages read | Period |
|---|---|---|---|
| Outcome of Board Meeting, Q1 FY27 unaudited results, 05-Aug-2026 | 2e3c0310-a7b8-4ce0-9282-26148ae3b55c | 1 to 7 | FY2027 Q1 |
| Financial Results, Q4 and FY26 audited, board 12-May-2026 | ff83c2bb-2517-4656-98e7-78947334daa9 | 6 to 13 | FY2026 Q4 |
| Dividend filing carrying the FY26 results | 0a416190-fd31-4d42-b0be-2360ba53386d | 8, 12 (snippets) | FY2027 Q1 |
| Credit Rating Revision, CareEdge press release, 13-Aug-2026 | 2243e0a7-c37f-4040-996d-0954fb05015a | 1 to 7 | FY2027 Q2 |
| Disclosure under SEBI Takeover Regulations, Reg 31(4) | 11cb5fab-60e6-447b-9888-5dc899a467be | 1 (snippet) | FY2027 Q2 |
| Exchange approvals, promoter reclassification, 03-Feb-2026 | df4d2673-da95-4c9a-b019-e92619e97891 | 2 to 4 (snippets) | FY2026 Q4 |
| Shareholders meeting: 86th AGM minutes and voting, 05/06-Aug-2026 | 1453b24e-7b87-40e6-9565-9ad97588858f | 4, 7 to 13, 15, 18 | FY2027 Q2 |
| Reg 34(1) Annual Report FY25 (85th), MD&A | 2e9691d4-cfbe-4a7f-ad4d-e8954922cc3c | 42 to 44 (snippets) | FY2025 |
| Reg 34(1) Annual Report FY24 (84th), MD&A | 6d8e8749-c673-485f-be59-99a555344c7b | 41 to 43 (snippets) | FY2024 |
| Management guidance records (get_company_guidance) | none returned | n/a | n/a |

## Known gaps

- **Zero guidance records.** get_company_guidance returned no record. No
  investor presentation and no concall transcript exist in the index.
- **FY26 annual report not indexed.** The AGM adopted it on 05-Aug-2026 (AGM
  minutes page 9), but the latest AR in Bull AI is FY25. FY26 crushing,
  recovery and distillery volumes are NOT FOUND.
- Q2 FY26 (September 2025 quarter) is derived arithmetically as FY26 less Q1,
  Q3 and Q4. The Q2 FY26 filing itself was not read.
- Sugar realisation per quintal and ethanol price per litre NOT FOUND.
- The availability map is truncated (latest 12 periods per first 12 document
  types). A filtered "Result" query and a post-2026-01-01 query were run to
  close the gap.

## Document and reader defects

- **Company cover letter misstates its own rating.** The 13-Aug-2026 cover
  letter reads "CARE BBB+; Stable". CareEdge's press release in the same
  filing reads "CARE BBB-; Stable" on page 2 and in the Annexure-1 table on
  page 5. The agency document governs. Flag.
- FY26 other comprehensive income prints as (406.96) on the Q1 FY27 filing
  (page 4) and as 406.95 positive on the FY26 filing (page 7). Total
  comprehensive income of 1,768.16 reconciles only with the positive figure.
- The FY26 segment table (FY26 filing page 8) prints the unallocable subtotal
  and the profit before tax on separate rows. The segment lines themselves
  are legible and used.

## Price basis

Not a corpus document. Bull AI company record read 2026-09-28, market
capitalisation Rs 719.78 crore.

## Bull AI calls

9 billable: 1 guidance, 5 searches, 3 chunk reads.
