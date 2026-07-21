# A2 Completeness Ledger — E2E Networks Limited (E2E), Q1 FY27, results filing

Source: `/home/user/inflection-pipeline/runs/e2e-q1fy27/work/extract_results_e2e_q1fy27.txt`
(7 pages, 398 lines per header, no OCR pages flagged but body text shows heavy OCR noise —
roman numerals rendered as letters, "1" as "I", digits transposed. Noted per row where it
affects reading.)

No prior-quarter ledger was supplied for this run (`PRIOR_LEDGER_PATH` not provided), so
`ENTITY_CHANGE` / `DROPPED_SLIDE`-type diffs below are assessed against in-filing evidence
only (notes stating the subsidiary is newly incorporated), not against a prior ledger.

```
=== A2 COUNT TEST ===
category: notes            grep_count: 18   sweep_count: 18   match: yes
category: line_items       grep_count: 60   sweep_count: 60   match: yes
category: zero_standing    grep_count: 4    sweep_count: 4    match: yes
category: agenda_items     grep_count: 1    sweep_count: 1    match: yes
category: auditor_paras    grep_count: 10   sweep_count: 10   match: yes
category: entities         grep_count: 1    sweep_count: 1    match: yes
category: annexures        grep_count: 1    sweep_count: 1    match: yes
category: signature_blocks grep_count: 5    sweep_count: 5    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Method notes on reconciliation (kept for A3/A4 audit trail):
- `notes`: `grep -n -E "^\s*(I|[0-9]{1,2})\s{2,}(The|Pursuant|Basic)"` hit all 18 note-openers
  (9 consolidated, 9 standalone) on first pass; manual sweep line-by-line of both "Notes:"
  blocks (lines 124-142, 207-228) independently produced 9+9=18. Match, no re-sweep needed.
- `line_items`: raw non-blank-line grep of each table body (consolidated lines 79-121,
  standalone lines 164-204) returned 32 and 31 respectively, but 2 of those (line 17, line 31
  region) are wrapped value-continuation lines with no label, not distinct rows. Refined grep
  requiring a letter in the line (`grep -c -E "[A-Za-z]"` per table body) returned 30 and 30,
  matching an independent manual row-by-row count of 30 per table (including header rows IV,
  VIII, X, XII). Total 60/60, match.
- `zero_standing`: grep for the roman/label markers of the two all-period-dash rows
  ("VI Exceptional items", "(a) Current tax") returned 2 hits per table x 2 tables = 4;
  manual read of all four period columns for every row confirmed exactly these 4 rows are
  dash/blank in ALL four periods (both tables). Match.
- `agenda_items`: an unrestricted keyword sweep of the board-outcome letter (lines 1-64) hit
  2 lines (the results-approval sentence at line 39, and a reference to "Statutory Auditors"
  at line 44 that is describing the enclosed Limited Review Report, not a separate agenda
  resolution). Refining the grep to the operative "have inter-alia Considered and approved"
  clause returns exactly 1, matching the manual read: this is a single-item board outcome.
- `auditor_paras`: numbered-paragraph grep (`^\s*(I|[0-9])\.\s`, allowing for the OCR
  rendering of "1." as "I." at line 333) found 9; manual read found a 10th, unnumbered
  paragraph at line 359 ("We have performed procedures in accordance with the Master
  Circular...") inserted between numbered paras 3 and 4 of the consolidated report. Adding
  that literal string to the grep brought it to 10/10. Match.
- `entities`: grep for subsidiary/associate/joint-venture/"Sovcloud" language returned every
  mention of the single subsidiary, Sovcloud Technologies Limited, across both note sets and
  the consolidated auditor report; manual read confirms only one entity in the consolidation
  perimeter. Match.
- `signature_blocks`: literal grep for "Whole Time Director" returned 0 hits because OCR
  rendered the two board-signature blocks as "Whole T1me Director" (line 150) and "Whole
  Time Directo" (line 239, final "r" dropped). A broader grep on
  `Digitally signed|DIN:|DIN :|Partner$|Company Secretary` returns 6 line-hits, but 2 of
  those (lines 56 and 63) belong to the single CS digital-signature block, collapsing to 5
  distinct signature blocks. Manual read independently found the same 5 blocks (CS digital
  signature; consolidated-results director signature; standalone-results director signature;
  standalone auditor signature; consolidated auditor signature). Match after collapsing
  multi-line hits to blocks.

---

## Table 1 — Board Outcome Letter (agenda items, meeting timing, top signature)

| # | Item | Line(s) | Detail | Flags |
|---|------|---------|--------|-------|
| 1 | Agenda item — results approval | 38-41 | Board "Considered and approved the Un-audited Standalone and Consolidated Financial Results...for the Quarter ended June 30, 2026" under Reg. 33 SEBI LODR | SINGLE_AGENDA_ITEM — no other resolution (AR approval, AGM notice, record date, dividend, appointments, auditor change, ESOP, capital-raising) is disclosed in this letter |
| 2 | Board meeting start time | 49 | Commenced 12:30 P.M. | — |
| 3 | Board meeting end time | 49 | Concluded 01:15 P.M. (45-minute meeting) | — |
| 4 | Annexure reference | 43-45 | Results + Limited Review Report enclosed, "marked as Annexure-I" | — |
| 5 | Website disclosure statement | 47 | Results also uploaded to company website | — |
| 6 | CS digital signature block | 55-64 | Ronit, Company Secretary & Compliance Officer, Membership No. A59215; "Digitally signed... Date: 2026.07.21 13:21:41 +05'30'" | Timestamp (13:21:41) is 6 minutes AFTER stated board conclusion (13:15) — signature-after-conclusion is the expected order, so NOT a SIGNATURE_BEFORE_CONCLUSION flag; recorded for the record per Rule 7 |

## Table 2 — Annexure-I structure (every annexure and every table within)

| # | Component | Lines | Content type | Flags |
|---|-----------|-------|---------------|-------|
| 1 | Annexure-I heading | 66 | Header only | — |
| 2 | Table: Consolidated financial results statement | 68-151 | Financial table + 9 notes + director signature | — |
| 3 | Table: Standalone financial results statement | 153-240 | Financial table + 9 notes + director signature | — |
| 4 | Document: Independent Auditor's Review Report — Standalone | 242-316 | 4-paragraph review report + signature/UDIN | — |
| 5 | Document: Independent Auditor's Review Report — Consolidated | 318-399 | 5-numbered + 1 unnumbered paragraph review report + signature/UDIN | — |

Only one annexure is referenced or present (Annexure-I); no director-profile annexure, ESOP
annexure, or scrutinizer report annexure is present in this filing.

## Table 3 — Consolidated financial results: every table line item (lines 79-121)

Values shown are Qtr ended 30-Jun-26 / 31-Mar-26 / 30-Jun-25 / Year ended 31-Mar-26 (INR lakhs).

| # | Line item | Line | Values (4 periods) | Flags |
|---|-----------|------|---------------------|-------|
| 1 | I Revenue from operations | 79 | 15,675.99 / 9,564.27 / 3,611.02 / 24,558.01 | — |
| 2 | II Other income | 80 | 1,142.01 / 548.28 / 1,499.56 / 3,400.64 | — |
| 3 | III Total income (I+II) | 82 | 16,818.00 / 10,112.55 / 5,110.58 / 27,958.65 | — |
| 4 | IV Expenses [header] | 84 | (header row, no values) | — |
| 5 | Purchase of services and consumables | 85 | 2,287.55 / 2,081.05 / 1,427.89 / 6,595.13 | — |
| 6 | Employee benefit expenses | 86 | 1,099.70 / 1,236.42 / 773.44 / 3,743.11 | — |
| 7 | Depreciation and amortization expenses | 87 | 6,064.44 / 5,134.64 / 2,743.30 / 16,922.69 | — |
| 8 | Finance costs | 88 | 1,005.15 / 368.04 / 183.05 / 1,224.13 | — |
| 9 | Other expenses | 89 | 498.52 / 436.58 / 358.25 / 1,593.54 | — |
| 10 | Total expenses (IV) | 91 | 10,955.36 / 9,256.73 / 5,485.93 / 30,078.60 | — |
| 11 | V Profit/(loss) before exceptional items and tax (III-IV) | 93 | 5,862.64 / 855.82 / (375.35) / (2,119.95) | — |
| 12 | VI Exceptional items | 94-95 | dash / dash / dash / dash | ZERO_STANDING — template line for extraordinary items; nil every period both tables |
| 13 | VII Profit/(loss) before tax expenses (V±VI) | 96 | 5,862.64 / 855.82 / (375.35) / (2,119.95) | — |
| 14 | VIII Tax expenses [header] | 98 | (header row, no values) | OCR renders marker as "VOi" |
| 15 | (a) Current tax | 99 | dash / dash / dash / dash | ZERO_STANDING — no current-tax charge in any period despite a positive Q1 FY27 PBT of 5,862.64, worth carrying to A3/A4 (loss-carryforward or MAT-credit read) |
| 16 | (b) Tax expenses pertaining to earlier years | 100 | dash / dash / dash / (40.96) | Populated in only 1 of 4 periods (FY26 full year) — not all-period-zero, so not flagged ZERO_STANDING, but noted as sparse |
| 17 | (c) Deferred tax | 101 | 1,474.43 / 212.26 / (91.21) / (522.40 approx, OCR-garbled as "52V IO") | Year-ended figure illegible in OCR — value NOT FOUND as printed, recorded as-is |
| 18 | Total tax expenses | 102 | 1,474.43 / 212.26 / (91.21) / (563.36 approx, OCR-garbled as "56.l.36") | Year-ended figure illegible in OCR — NOT FOUND as printed |
| 19 | IX Profit/(loss) for the period/year after tax (VII-VIII) | 104 | 4,388.21 / 643.56 / (284.14) / (1,556.59 approx, OCR tail cut) | — |
| 20 | X Other Comprehensive Income [header] | 106 | (header row, no values) | — |
| 21 | (i) Items that will not be reclassified to P&L | 107 | (505.01) / 329.48 / (111.63) / 125.47 | — |
| 22 | (ii) Income tax relating to items that will not be reclassified | 108-109 | 127.10 / (82.92) / 28.85 / (31.58) | — |
| 23 | Other comprehensive income, net of tax | 110 | (377.91) / 246.56 / (82.78) / 93.89 | — |
| 24 | XI Total comprehensive income (IX±X) | 112 | 4,010.30 / 890.12 / (366.92) / (1,462.70) | — |
| 25 | Profit/(Loss) for the period [memo repeat of row 18/IX-adjacent line] | 115 | 5,862.64 / 855.82 / (375.35) / (2,119.95) | Duplicate of row 11/13 PBT figure, not IX — appears to be a mislabeled memo row in the source; recorded as printed |
| 26 | Paid up Equity Share Capital (face value Re. 1/- each) | 116 | blank / blank / blank / 2,055.65 | Disclosed only in Year-ended column, per standard SEBI format (balance-sheet item) — not flagged ZERO_STANDING, blank quarter columns are format convention |
| 27 | Other Equity | 117 | blank / blank / blank / 1,66,449.53 | Same as above — year-end-only balance sheet disclosure |
| 28 | XII Earnings per equity share [header] | 119 | (header row, no values) | — |
| 29 | 1) Basic earnings per share | 120 | 2.14 / 0.32 / (0.14) / (0.78) | Restated for 1:10 sub-division per Note 4 |
| 30 | 2) Diluted earnings per share | 121 | 2.10 / 0.32 / (0.14) / (0.76) | Restated for 1:10 sub-division per Note 4 |

## Table 4 — Standalone financial results: every table line item (lines 164-204)

Structure and figures are line-for-line identical to the consolidated table (subsidiary not
yet operational per Note 9 both sets) except line numbers shift to the standalone table.

| # | Line item | Line | Values (4 periods) | Flags |
|---|-----------|------|---------------------|-------|
| 1 | I Revenue from operations | 164 | 15,675.99 / 9,564.27 / 3,611.02 / 24,558.01 | — |
| 2 | II Other income | 165 | 1,142.01 / 548.28 / 1,499.56 / 3,400.64 | — |
| 3 | III Total income (I+II) | 167 | 16,818.00 / 10,112.55 / 5,110.58 / 27,958.65 | — |
| 4 | IV Expenses [header] | 169 | (header row) | — |
| 5 | Purchase of services and consumables | 170 | 2,287.55 / 2,081.05 / 1,427.89 / 6,595.13 | — |
| 6 | Employee benefit expenses | 171 | 1,099.70 / 1,236.42 / 773.44 / 3,743.11 | — |
| 7 | Depreciation and amortization expenses | 172 | 6,064.44 / 5,134.64 / 2,743.30 / 16,922.69 | — |
| 8 | Finance costs | 173 | 1,005.15 / 368.04 / 183.05 / 1,224.13 | — |
| 9 | Other expenses | 174 | 498.52 / 436.58 / 358.25 / 1,593.54 | — |
| 10 | Total expenses (IV) | 176 | 10,955.36 / 9,256.73 / 5,485.93 / 30,078.60 | — |
| 11 | V Profit/(loss) before exceptional items and tax (III-IV) | 178 | 5,862.64 / 855.82 / (375.35) / (2,119.95) | — |
| 12 | VI Exceptional items | 179 | dash / dash / dash / dash | ZERO_STANDING |
| 13 | VII Profit/(loss) before tax expenses (V±VI) | 180 | 5,862.64 / 855.82 / (375.35) / (2,119.95) | — |
| 14 | VIII Tax expenses [header] | 182 | (header row) | OCR renders marker as "vm" |
| 15 | (a) Current tax | 183 | dash / dash / dash / dash | ZERO_STANDING — same read as consolidated |
| 16 | (b) Tax expenses pertaining to earlier years | 184 | dash / dash / dash / (40.96) | Sparse, not all-period-zero |
| 17 | (c) Deferred tax | 185 | 1,474.43 / 212.26 / (91.21) / (522.40 approx, OCR "S22.40") | Year-ended figure illegible in OCR |
| 18 | Total tax expenses | 186 | 1,474.43 / 212.26 / (91.21) / (563.36 approx, OCR "(! 6.l.36") | Year-ended figure illegible in OCR |
| 19 | IX Profit/(loss) for the period/year after tax (VII±VIII) | 188 | 4,388.21 / 643.56 / (284.14) / (1,556.59 approx) | — |
| 20 | X Other Comprehensive Income [header] | 190 | (header row) | — |
| 21 | (i) Items that will not be reclassified to P&L | 191 | (505.01) / 329.48 / (111.63) / 125.47 | — |
| 22 | (ii) Income tax relating to items that will not be reclassified | 192-193 | 127.10 / (82.92) / 28.85 / (31.58) | — |
| 23 | Other comprehensive income, net of tax | 194 | (377.91) / 246.56 / (82.78) / 93.89 | — |
| 24 | XI Total comprehensive income (IX±X) | 196 | 4,010.30 / 890.12 / (366.92) / (1,462.70) | — |
| 25 | Profit/(Loss) for the period [memo repeat] | 198 | 5,862.64 / 855.82 / (375.35) / (2,119.95) | Same duplicate-row pattern as consolidated table |
| 26 | Paid up Equity Share Capital (face value Re. 1/- each) | 199 | blank / blank / blank / 2,055.65 | Year-end-only disclosure, format convention |
| 27 | Other Equity | 200 | blank / blank / blank / 1,66,449.53 | Year-end-only disclosure, format convention |
| 28 | XII Earnings per equity share [header] | 202 | (header row) | — |
| 29 | 1) Basic earnings per share | 203 | 2.14 / 0.32 / (0.14) / (0.78) | Restated for 1:10 sub-division |
| 30 | 2) Diluted earnings per share | 204 | 2.10 / 0.32 / (0.14) / (0.76) | Restated for 1:10 sub-division |

Standalone and consolidated P&L are numerically identical this quarter because the sole
subsidiary, Sovcloud Technologies Limited, had not commenced operations as at 30-Jun-26
(Note 9, both sets).

## Table 5 — Consolidated results: numbered notes (lines 124-142)

| Note # | Line | First ~15 words | Flags |
|--------|------|------------------|-------|
| 1 | 125-126 | "The Consolidated financial results of the company have been prepared in accordance with Indian Accounting Standards..." | — |
| 2 | 127-128 | "The above unaudited consolidated financial results for the quarter ended June 30, 2026 have been reviewed..." | States Statutory Auditors "expressed an unmodified review conclusion" |
| 3 | 129-130 | "The figures of the quarter ended March 31, 2026 were the balancing figure between the audited figures..." | Standard Q4-as-plug disclosure |
| 4 | 131-135 | "Pursuant to the approval of the shareholders through the Postal Ballot on May 21, 2026, each equity share..." | 1:10 face-value sub-division (Rs.10 -> Re.1), record date June 5, 2026; EPS retrospectively restated |
| 5 | 136-137 | "Pursuant to the approval granted by BSE Limited, the equity shares of the Company were listed and admitted..." | Direct Listing Route on BSE effective June 12, 2026 (in addition to existing NSE listing) |
| 6 | 138 | "The requirement of Ind AS-108 'Operating Segments' is not applicable to the group as it is engaged..." | Single reportable segment |
| 7 | 139 | "Basic & Diluted earning/(loss) per share is not annualised for the quarter ended June 30, 2026, March 31, 2026..." | — |
| 8 | 140 | "The figures of the previous periods have been regrouped, wherever necessary, to correspond with the current period." | Generic regrouping note — no specifics of what was regrouped |
| 9 | 141-142 | "The wholly owned subsidiary was incorporated on June 17, 2026 and had not commenced its business operations..." | Names the entity change driver; consolidated comparatives for all prior periods are standalone-only figures |

## Table 6 — Standalone results: numbered notes (lines 207-228)

| Note # | Line | First ~15 words | Flags |
|--------|------|------------------|-------|
| 1 | 208-210 | "The standalone financial results of the company have been prepared in accordance with Indian Accounting Standards..." | — |
| 2 | 211-212 | "The above unaudited standalone financial results for the year ended June 30, 2026 have been reviewed..." | Note text says "year ended" where "quarter ended" is meant — OCR/source wording as printed; states Statutory Auditors "expressed an unmodified review conclusion" |
| 3 | 214-215 | "The figures of the quarter ended March 31, 2026 were the balancing figure between the audited figures..." | Same as consolidated Note 3 |
| 4 | 216-220 | "Pursuant to the approval of the shareholders through the Postal Ballot on May 21, 2026, each equity share..." | Same 1:10 sub-division as consolidated Note 4 |
| 5 | 221-223 | "Pursuant to the approval granted by BSE Limited, the equity shares of the Company were listed and admitted..." | Same BSE direct-listing disclosure as consolidated Note 5 |
| 6 | 224 | "The requirement of Ind AS-108 'Operating Segments' is not applicable to the company as it is engaged..." | Single reportable segment |
| 7 | 225 | "Basic & Diluted earning/(loss) per share is not annualised for the quarter ended June 30, 2026, March 31, 2026..." | — |
| 8 | 226 | "The figures of the previous periods have been regrouped, wherever necessary, to correspond with the current period." | Same generic regrouping note |
| 9 | 227-228 | "The Company incorporated Sovcloud Technologies Limited as its wholly owned subsidiary in India on June 17, 2026..." | Names the subsidiary explicitly (consolidated Note 9 does not name it); also states no associate/JV exists |

## Table 7 — Independent Auditor's Review Report, Standalone (lines 242-316)

| Para # | Line | Content | Flags |
|--------|------|---------|-------|
| Title/addressee | 248-256 | Report title, SRE scope statement, addressed "The Board of Directors, E2E Networks Limited" | — |
| 1 | 257-262 | Scope: statement reviewed for quarter ended 30-Jun-26 and YTD (1-Apr to 30-Jun-26), per Reg. 33 | — |
| 2 | 264-269 | Management's responsibility for the Statement; auditor's responsibility to report | — |
| 3 | 272-281 | Review conducted per SRE 2410; moderate (not audit-level) assurance; "we do not express an audit opinion" | — |
| 4 | 291-297 | Conclusion: "nothing has come to our attention" causing belief of non-disclosure or material misstatement | Opinion type: unmodified/clean review conclusion. No Emphasis of Matter, no Other Matters, no Going Concern paragraph present in this report |
| Signature block | 302-316 | "For GSA & Associates LLP, Chartered Accountants," Firm Registration No. illegible in OCR ("/N500339"), Tanuj Ch[andra?] Partner, Membership No. 529619, UDIN 26529619ISTDOU1925, Place New Delhi, Date 21-07-2026 | Firm registration number NOT FOUND as legibly printed (OCR artifact) — do not infer the correct digits |

Entities reviewed: standalone report covers only E2E Networks Limited (no subsidiaries in
the standalone perimeter). No entity is flagged unaudited/management-furnished in this report.

## Table 8 — Independent Auditor's Review Report, Consolidated (lines 318-399)

| Para # | Line | Content | Flags |
|--------|------|---------|-------|
| Title/addressee | 324-332 | Report title, SRE scope statement, addressed "The Board of Directors, E2E Networks Limited" | — |
| 1 | 333-340 | Scope: Statement reviewed for the "Holding Company" and "its subsidiary" (Group), quarter + YTD | OCR renders "1." as "I." |
| 2 | 341-346 | Management's (Holding Company's) responsibility; auditor's responsibility to report | — |
| 3 | 348-357 | Review per SRE 2410; moderate assurance; "we do not express an audit opinion" | — |
| [unnumbered] | 359-360 | "We have performed procedures in accordance with the Master Circular issued by the Securities and Exchange Board of India under Regulation 33(8) of the Listing Regulations, to the extent applicable." | Unnumbered paragraph, inserted between numbered paras 3 and 4 — no paragraph number assigned in source; procedural/scope statement re: SEBI Master Circular compliance |
| 4 | 370-373 | Other Matters: "The Statement includes the result of M/s. Sovcloud Technologies Limited, a wholly owned subsidiary... Financial results of the Subsidiary company are also reviewed by us on which we have issued an unmodified review conclusion dated July 20, 2026." | Entity reviewed: Sovcloud Technologies Limited, reviewed (not merely management-furnished) by the same auditor, dated one day before this filing's board meeting (July 20 vs July 21) |
| 5 | 374-380 | Conclusion: "nothing has come to our attention" causing belief of non-disclosure or material misstatement | Opinion type: unmodified/clean review conclusion. No Emphasis of Matter, no Going Concern paragraph. Para 4 functions as the Other Matters paragraph |
| Signature block | 385-399 | "For GSA & Associates LLP, Chartered Accountants," Firm Registration No. illegible in OCR ("/N500339"), Tanuj Ch[andra?] (OCR "Taouj Chu") Partner, Membership No. 529619, UDIN 26529619QAOMIW2577, Place New Delhi, Date 21-07-2026 | Firm registration number NOT FOUND as legibly printed (OCR artifact); UDIN differs correctly from the standalone report's UDIN (26529619ISTDOU1925 vs 26529619QAOMIW2577) — no UDIN reuse |

Entities reviewed: Holding Company (E2E Networks Limited) + Sovcloud Technologies Limited
(wholly owned subsidiary), both reviewed by GSA & Associates LLP; no entity in this filing is
flagged as unaudited or management-furnished-only.

## Table 9 — Consolidation entity list (cross-check)

| # | Entity | Relationship | First disclosed | Line(s) | Flags |
|---|--------|--------------|------------------|---------|-------|
| 1 | Sovcloud Technologies Limited | Wholly owned subsidiary of E2E Networks Limited (Holding Company) | Standalone Note 9 (names it); Consolidated Note 9 (describes it without naming); Consolidated auditor report para 4 | 141-142, 227-228, 370-372 | ENTITY_CHANGE — incorporated June 17, 2026, i.e. within this reporting quarter; not commenced operations as at 30-Jun-26; all comparative consolidated figures for prior periods are standalone-only per Note 9 (there is no true prior-period consolidated comparative to diff against) |

No associate or joint venture exists as at 30-Jun-26 (standalone Note 9, line 228).

## Table 10 — Signature blocks (signatory, designation, timestamp)

| # | Signatory | Designation | Where | Line(s) | Timestamp | Flags |
|---|-----------|-------------|-------|---------|-----------|-------|
| 1 | Ronit | Company Secretary & Compliance Officer, Membership No. A59215 | Board Outcome letter | 55-64 | Digitally signed 2026.07.21 13:21:41 +05'30' | Board meeting concluded 13:15; signature at 13:21:41 is after conclusion (expected order) — not flagged |
| 2 | Srishti Baweja, DIN 08057000 | Whole Time Director | Consolidated results statement | 145-151 | Place Noida, Date July 21, 2026 (no time-stamp printed) | OCR renders title as "Whole T1me Director" |
| 3 | Srishti Baweja, DIN 08057000 | Whole Time Director | Standalone results statement | 231-240 | Place Noida, Date July 21, 2026 (no time-stamp printed) | OCR renders title as "Whole Time Directo" (final "r" dropped) |
| 4 | Tanuj Ch[andra?], Membership No. 529619 | Partner, GSA & Associates LLP, Chartered Accountants | Standalone auditor's review report | 302-316 | Place New Delhi, Date 21-07-2026; UDIN 26529619ISTDOU1925 | — |
| 5 | Tanuj Ch[andra?] (OCR "Taouj Chu"), Membership No. 529619 | Partner, GSA & Associates LLP, Chartered Accountants | Consolidated auditor's review report | 385-399 | Place New Delhi, Date 21-07-2026; UDIN 26529619QAOMIW2577 | Same partner/membership number as row 4, different UDIN per report (correct practice) |

---

## Summary of flags raised across all tables

- `ZERO_STANDING` x4 — VI Exceptional items (consolidated + standalone), (a) Current tax
  (consolidated + standalone); all dash/nil across all four disclosed periods in both
  statements.
- `ENTITY_CHANGE` x1 — Sovcloud Technologies Limited, newly incorporated wholly owned
  subsidiary, first appearance in the consolidation perimeter this quarter.
- `SINGLE_AGENDA_ITEM` x1 — Board Outcome letter carries only the results-approval
  resolution; no AR approval, AGM notice, record date, dividend, appointment, auditor
  change, ESOP, or capital-raising item is disclosed for this board meeting.
- OCR-illegible values recorded as printed, not estimated: Firm Registration Number of
  GSA & Associates LLP (both reports), Deferred Tax and Total tax expenses year-ended
  column (both statements).
