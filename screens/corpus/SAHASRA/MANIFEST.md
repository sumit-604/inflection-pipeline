# SAHASRA corpus manifest

Company: Sahasra Electronic Solutions Ltd (SESL)
NSE: SAHASRA | ISIN: INE0RBQ01018 | CIN L26202DL2023PLC410521
BSE code: none in the Bull AI record.
Reports half-yearly. Latest financial period ends 31-Mar-2026.
Screened: 2026-09-28

## Corpus rule deviation (operator ruling 2026-09-08 applies)

No egress this session. The corpus is the Bull AI chunk reader over the same
filed PDFs. Page numbers are the source PDF's own. Nobody holds the original.

## Documents read

| Document | Bull AI doc id | Pages read | Period |
|---|---|---|---|
| Earnings call transcript, H2 FY26 and FY26, call of 29-May-2026, filed 02-Jun-2026 | 2d814bc8-2f7c-4b66-ac11-a69b32a4a657 | 1 to 18 | FY2026 Q4 |
| Investor Presentation, FY26 earnings update, filed 28-May-2026 | 6c7e86b9-7c11-4e03-96cb-ac4aa0122c40 | 1 to 40 | FY2026 Q4 |
| Outcome of Board Meeting, interim standalone accounts at 31-Dec-2025 for share valuation (merger) | b97ede2a-8b9b-4d73-9174-d6b41a72ac1d | 22 (snippet), 27, 28 | FY2026 Q4 |
| Outcome of Board Meeting, FY26 consolidated results and audit report | 6a1a6761-55e9-45fb-a881-692ae1c056ce | 4, 11, 13 (search snippets only) | FY2026 Q4 |
| Shareholders meeting, AGM notice with FY26 annual report and RPT approvals | bd13a104-5d35-4432-8884-3f210e780851 | 66, 100, 101 (search snippets only) | FY2027 Q2 index |
| Management guidance records (get_company_guidance) | n/a | 1 period, 5 guidance and 9 delivery records | FY2026 Q4 |

## Known gaps

- **Credit rating NOT FOUND.** No rating filing appears in the availability
  map or in a search for "credit rating". Agency sites unreachable. Step 10
  is empty.
- The FY26 annual report inside bd13a104 returns **empty** from the chunk
  reader at pages 63 to 65, although search indexes pages 66, 100 and 101.
  The standalone and consolidated auditor opinions on FY26 were therefore
  read only as search snippets (6a1a6761 pages 4, 11, 13), which show the
  Other Matters paragraph and no modification.
- The FY25 annual report is indexed; it was not read.
- No H1 FY27 result exists yet. Six months since 31-Mar-2026 are unobserved.
- Merger scheme share count after issue NOT FOUND. Only the promoter
  percentage before and after is filed (deck page 21).

## Reader defects found

- **Guidance tool fabricated figures.** get_company_guidance returned records
  citing deck 6c7e86b9 pages 4, 5, 6, 10, 12, 14, 15, 16, 18 and 22 with
  "record revenue of INR 410.20 crores", "PAT INR 48.50 crores", a "INR 600
  crores" FY27 target, a "18% to 20%" EBITDA corridor, "INR 45 crores" capex,
  "1.5 million units per month in our LED lighting segment" and a 25% export
  target. **None of these appear on the cited pages.** The deck itself says
  Rs 138.8 crore revenue, Rs 12.13 crore PAT and a Rs 300 crore post-merger
  target. The deck has 40+ pages; page 22 is a contents page. Every one of
  those records was discarded. The four records citing the transcript
  2d814bc8 page 2 match the transcript text at page 3. Treat the guidance
  tool as unverified until each quote is read on its page.
- Deck page 7 labels segment revenue "Billion INR". The values are Rs crore
  (they sum to the Rs 138.8 crore total on page 5). Label error.
- Deck page 30 labels units "UNKNOWN". Values match Rs crore on page 36.
- Transcript pages 10 and 11 come back as reader-written summaries
  ("Discussion Summary", "Key Points"), not verbatim text. Page 10's summary
  says "Consolidated PAT margin should be around 15%" and semiconductor
  break-even "in 2027-2028". The verbatim page 8 says "PBT margins of 15%"
  and page 5 says EBITDA break-even "by FY2027 end". The card uses the
  verbatim pages.
- One multi-request chunk call exceeded the response cap and returned an
  error. It is counted as billable.

## Price basis

Not a corpus document. Bull AI company record, market capitalisation
Rs 1,071.81 crore, read 2026-09-28. Used only for steps 11 and 13.

## Bull AI calls

8 billable: 1 guidance, 6 chunk reads (one failed on size), 1 search.
Free: 2 availability maps.
