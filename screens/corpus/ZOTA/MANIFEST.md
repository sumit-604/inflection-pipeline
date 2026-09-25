# ZOTA corpus manifest

Company: Zota Health Care Ltd
NSE: ZOTA | ISIN: INE358U01012 | not BSE listed
Screened: 2026-09-21

## Corpus rule deviation (operator ruling 2026-09-08 applies)

No egress this session. The corpus is the Bull AI chunk reader over the same
filed PDFs. Page numbers are the source PDF's own. Nobody holds the original.

## Documents read

| Document | Bull AI doc id | Pages read | Period |
|---|---|---|---|
| Investor Presentation Q1 FY27 | 02864601-d9a0-490b-8d01-06ec5fd575a3 | 11, 38, 39, 45 | FY2027 Q2 index |
| Investor Presentation Q4 FY26 | 1cbd7eed-1fe8-4725-84b1-280509087d98 | 37, 38, 44, 45 | FY2026 Q4 |
| Earnings Call Transcript Q1 FY27 | b82abc3c-74d7-449e-ba85-8aa6be2b2f21 | 4, 6, 9, 16 | FY2027 Q1 |
| Outcome of Board Meeting, Q1 FY27 consolidated results | 62b9be11-c135-44e7-84c9-488662d0beda | 7, 8 | 2026-08-13 |
| Issue of Securities, warrant conversions at Rs 509 | 5864b5e8 / 47106518 / 681a7869 | 2, 3 | FY2026 Q4 |

## Reader artefact warning

Page 38 of the Q1 FY27 investor presentation returned an "Export Performance
Highlights" table showing exports by region in metric tons, with FDA and EMA
listed among the approvals. It contradicts page 39 of the same deck, which
describes an export business serving CIS, Latin America, Africa and Asia from
one SEZ plant. The page 38 table is treated as a reader artefact and is not
used anywhere in this card.

## Known gaps

- **Credit rating NOT FOUND.** No rating filing appears in the index, and the
  agency sites were unreachable. Step 10 is empty.
- **No annual report read.** Auditor emphasis, related-party detail and the
  promoter shareholding table are NOT FOUND.
- Store-level economics (revenue per store, payback, closure rate) are not
  disclosed in any document held. Step 5 and step 8 are weakened.

## Price basis

Not a corpus document. Bull AI company record, market capitalisation
Rs 3,963.70 crore at the screen date. Used only for the step 11
recognition-gap read, never for a valuation.
