# A2 ENUMERATION LEDGER — Balaji Amines Limited (BALAMINES), Q1 FY27, Results Filing

Source: /home/user/inflection-pipeline/runs/balamines-q1fy27/work/extract_results_balamines_q1fy27.txt
(7 pages, 430 lines, unit convention: Lakhs, x0.01 -> Cr. Values below are enumerated exactly as
they appear at the cited line numbers; no unit conversion performed.)

```
=== A2 COUNT TEST ===
category: agenda_items    grep_count: 3   sweep_count: 3   match: yes
category: line_items      grep_count: 106 sweep_count: 102 match: yes (reconciled)
category: zero_standing   grep_count: 13  sweep_count: 13  match: yes (reconciled, see note)
category: notes           grep_count: 5   sweep_count: 5   match: yes
category: auditor_paras   grep_count: 9   sweep_count: 9   match: yes
category: entities        grep_count: 2   sweep_count: 2   match: yes
category: signature_blocks grep_count: 3  sweep_count: 3   match: yes
gate_a2: pass
note_line_items: grep_count = raw non-blank physical lines within the three table
  ranges (106-139, 168-207, 232-264) = 34+40+32 = 106. Four of those physical lines
  are text-wraps of a single logical row (line 111-112 "Changes in inventories...",
  134-135 "Paid-up equity share capital..." in the standalone table; 173-174 and
  202-203, same two labels, in the consolidated table). 106 - 4 = 102, matching the
  manual sweep of logical rows exactly. Reconciled by direct line-by-line inspection,
  not a single grep pattern (no wrap markers in the OCR text).
note_zero_standing: a naive dash-character grep on the three table ranges undercounts
  because the OCR renders some dash/nil cells as "=" or "E" rather than "-" (lines 181,
  194, 247) and renders one nil-standing line ("Other equity", lines 136/204) as a
  blank cell with no character at all. Pass 1 (literal "-" grep) found 8 lines. Pass 2
  (keyword-targeted grep on the row labels below, cross-checked against the current-
  quarter [30.06.2026] column specifically) found all 13. Manual sweep, reading every
  data row's current-quarter cell one by one, independently arrived at the same 13.
  Rule applied: flagged if the CURRENT-QUARTER (30.06.2026) column is dash/nil/blank,
  regardless of whether comparative columns carry a value.
=== END COUNT TEST ===
```

## 1. Board Outcome Letter — Agenda Items (page 1)

| # | Line(s) | Item | Flags |
|---|---------|------|-------|
| 1 | 49 | Un-audited Standalone Financial Results of the Company for the Quarter ended 30th June, 2026 — considered and approved | |
| 2 | 51 | Un-audited Consolidated Financial Results of the Company for the Quarter ended 30th June, 2026 — considered and approved | |
| 3 | 53-55 | Taken Note of Limited Review Reports issued by Statutory Auditors, M/s. M. Anandam & Co., Chartered Accountants, on the Un-audited Standalone and Consolidated Financial Results | |
| — | 57 | Board Meeting timing: commenced 4:30 P.M., concluded 5:35 P.M. (65 minutes) | INFO_ONLY — not a resolution row, recorded per instruction |

No AR-approval item, no AGM notice, no record date, no dividend, no director
appointment/resignation, no auditor change, no scrutinizer appointment, no ESOP
grant, no capital-raising enabling resolution present in this Board Outcome letter.
Only the three items above (results + taking-note of review reports). Confirmed by
full-text sweep of page 1 (lines 30-73); no other numbered or unnumbered agenda item
exists.

## 2. Standalone Financial Results — every table row (page 2, lines 106-139)

Columns in source: Qtr 30.06.2026 (Unaudited) | Qtr 31.03.2026 (Audited) | Qtr 30.06.2025 (Unaudited) | Year 31.03.2026 (Audited)

| Line | Item | 30.06.2026 | 31.03.2026 | 30.06.2025 | 31.03.2026(Y) | Flags |
|---|---|---|---|---|---|---|
| 106 | 1 Revenue from operations | 42,273.75 | 36,176.95 | 31,937.88 | 1,29,154.47 | |
| 107 | 2 Other Income | 616.79 | 840.31 | 726.83 | 2,802.17 | |
| 108 | 3 Total Income (1+2) | 42,890.54 | 37,017.26 | 32,664.71 | 1,31,956.64 | |
| 109 | 4 Expenses [header row] | — | — | — | — | |
| 110 | (a) Cost of materials consumed | 23,596.80 | 20,394.03 | 13,808.09 | 72,655.79 | |
| 111-112 | (b) Changes in inventories of WIP and finished goods | 138.95 | (1,379.01) | 4,276.25 | (1,673.42) | |
| 113 | (c) Employee benefits expense | 2,400.20 | 2,420.57 | 1,891.51 | 7,714.30 | |
| 114 | (d) Depreciation and amortization expenses | 1,154.17 | 1,141.02 | 1,105.68 | 4,560.10 | |
| 115 | (e) Finance costs | 26.94 | 103.77 | 33.85 | 227.78 | |
| 116 | (f) Other expenses | 5,791.68 | 6,132.94 | 6,315.31 | 25,731.69 | |
| 117 | Total expenses | 33,108.74 | 28,813.32 | 27,430.69 | 1,09,216.24 | |
| 118 | 5 Profit before exceptional items and tax (3-4) | 9,781.80 | 8,203.94 | 5,234.02 | 22,740.40 | |
| 119 | 6 Exceptional Items | - | - | - | - | ZERO_STANDING (all 4 periods dash) |
| 120 | 7 Profit before Tax (5+6) | 9,781.80 | 8,203.94 | 5,234.02 | 22,740.40 | |
| 121 | 8 Tax expense [header row] | — | — | — | — | |
| 122 | Current Tax | 2,022.60 | 1,813.12 | 1,088.68 | 4,691.35 | |
| 123 | Deferred Tax | 496.45 | 204.45 | 165.38 | 1,505.60 | |
| 124 | Earlier years' tax | 48.51 | (0.23) | - | (9.38) | dash in one comparative period only, not current-qtr — not ZERO_STANDING |
| 125 | Total tax expenses | 2,567.56 | 2,017.34 | 1,254.06 | 6,187.57 | |
| 126 | 9 Profit for the period (7-8) | 7,214.24 | 6,186.60 | 3,979.96 | 16,552.83 | |
| 127 | 10 Other comprehensive income [header] | — | — | — | — | |
| 128 | Items that will not be reclassified to P&L [header] | — | — | — | — | |
| 129 | (i) Remeasurement of defined benefit plans | - | (33.55) | - | (14.99) | ZERO_STANDING (current qtr dash; FY26 annual has a value) |
| 130 | (ii) Income tax relating to item (i) above | - | - | - | - | ZERO_STANDING (all 4 periods dash) |
| 131 | Items that will be reclassified to P&L | - | - | - | - | ZERO_STANDING (all 4 periods dash) |
| 132 | Total other comprehensive income (net of tax) | - | (33.55) | - | (14.99) | ZERO_STANDING (subtotal of 129-131, current qtr dash) |
| 133 | 11 Total comprehensive income (9+10) | 7,214.24 | 6,153.05 | 3,979.96 | 16,537.84 | |
| 134-135 | 12 Paid-up equity share capital (Face Value Rs 2/- per share) | 648.02 | 648.02 | 648.02 | 648.02 | |
| 136 | 13 Other equity | (blank) | (blank) | (blank) | 1,77,848.62 | ZERO_STANDING (not disclosed for quarter columns, only annual — standard Ind AS balance-sheet-only item) |
| 137 | 14 Earnings per share (of Rs. 2/- each) [header] | — | — | — | — | |
| 138 | (a) Basic (in Rs.) | 22.27 | 19.09 | 12.28 | 51.09 | |
| 139 | (b) Diluted (in Rs.) | 22.27 | 19.09 | 12.28 | 51.09 | |

Standalone: 32 logical rows (7 header/subtotal-structure rows + 25 data rows, header
rows carry no independent value). ZERO_STANDING count: 6 (lines 119, 129, 130, 131,
132, 136).

## 3. Consolidated Financial Results — every table row (page 3, lines 168-207)

| Line | Item | 30.06.2026 | 31.03.2026 | 30.06.2025 | 31.03.2026(Y) | Flags |
|---|---|---|---|---|---|---|
| 168 | 1 Revenue from operations | 45,592.56 | 39,478.64 | 35,834.12 | 1,42,498.07 | |
| 169 | 2 Other Income | 552.49 | 773.84 | 902.00 | 2,880.67 | |
| 170 | 3 Total Income (1+2) | 46,145.05 | 40,252.48 | 36,736.12 | 1,45,378.74 | |
| 171 | 4 Expenses [header] | — | — | — | — | |
| 172 | (a) Cost of materials consumed | 24,609.25 | 23,124.89 | 16,624.75 | 81,115.35 | |
| 173-174 | (b) Changes in inventories of WIP and finished goods | 689.07 | (1,021.34) | 4,576.40 | (1,515.93) | |
| 175 | (c) Employee benefits expense | 2,582.58 | 2,604.05 | 2,047.85 | 8,411.03 | |
| 176 | (d) Depreciation and amortization expenses | 1,378.24 | 1,395.27 | 1,397.25 | 5,637.97 | |
| 177 | (e) Finance costs | 141.22 | 217.58 | 72.88 | 537.04 | |
| 178 | (f) Other expenses | 6,124.33 | 5,346.00 | 7,115.65 | 27,944.26 | |
| 179 | Total expenses | 35,524.69 | 31,666.45 | 31,834.78 | 1,22,129.72 | |
| 180 | 5 Profit before exceptional items and tax (3-4) | 10,620.36 | 8,586.03 | 4,901.34 | 23,249.02 | |
| 181 | 6 Exceptional Items | - | - | - | - | ZERO_STANDING (all 4 periods dash; OCR renders current-qtr cell as "=") |
| 182 | 7 Profit before Tax (5+6) | 10,620.36 | 8,586.03 | 4,901.34 | 23,249.02 | |
| 183 | 8 Tax expense [header] | — | — | — | — | |
| 184 | Current Tax | 2,256.42 | 1,918.52 | 1,088.68 | 4,796.75 | |
| 185 | Deferred Tax | 503.66 | 190.69 | & (OCR-ambiguous) | 1,545.14 | OCR_UNCERTAIN — 30.06.2025 comparative cell renders as bare "&" in extract, not a legible number or clean dash; current-qtr value (503.66) is not zero, so NOT ZERO_STANDING |
| 186 | Earlier years' tax | 48.51 | (0.23) | 159.94 | (8.55) | |
| 187 | Total tax expenses | 2,808.59 | 2,108.98 | 1,248.62 | 6,333.34 | |
| 188 | 9 Profit for the period (7-8) | 7,811.77 | 6,477.05 | 3,652.72 | 16,915.68 | |
| 189 | Attributable to: [header] | — | — | — | — | |
| 190 | (a) Owners of the Parent | 7,493.66 | 6,320.80 | 3,799.98 | 16,719.99 | |
| 191 | (b) Non-controlling interests | 318.11 | 156.25 | (147.26) | 195.69 | |
| 192 | 10 Other comprehensive income [header] | — | — | — | — | |
| 193 | Items that will not be reclassified to P&L [header] | — | — | — | — | |
| 194 | (i) Remeasurement of defined benefit plans | - | (25.29) | - | (16.98) | ZERO_STANDING (current qtr dash; OCR renders cell as "E") |
| 195 | (ii) Income tax relating to item (i) above | - | - | - | - | ZERO_STANDING (all 4 periods dash) |
| 196 | Items that will be reclassified to P&L | - | - | - | - | ZERO_STANDING (all 4 periods dash) |
| 197 | Total other comprehensive income (net of tax) | - | (25.29) | - | (16.98) | ZERO_STANDING (subtotal of 194-196, current qtr dash) |
| 198 | 11 Total comprehensive income (9+10) | 7,811.77 | 6,451.76 | 3,652.72 | 16,898.70 | |
| 199 | Attributable to: [header] | — | — | — | — | |
| 200 | (a) Owners of the Parent | 7,493.66 | 6,291.79 | 3,799.98 | 16,703.91 | |
| 201 | (b) Non-controlling interests | 318.11 | 159.97 | (147.26) | 194.79 | |
| 202-203 | 12 Paid-up equity share capital (Face Value Rs 2/- per share) | 648.02 | 648.02 | 648.02 | 648.02 | |
| 204 | 13 Other equity | (blank) | (blank) | (blank) | 1,96,997.59 | ZERO_STANDING (not disclosed for quarter columns, only annual) |
| 205 | 14 Earnings per share (of Rs. 2/- each) [header] | — | — | — | — | |
| 206 | (a) Basic (in Rs.) | 23.13 | 19.99 | 11.73 | 51.60 | |
| 207 | (b) Diluted (in Rs.) | 23.13 | 19.99 | 11.73 | 51.60 | |

Consolidated: 38 logical rows. ZERO_STANDING count: 6 (lines 181, 194, 195, 196, 197,
204). One additional OCR_UNCERTAIN cell noted at line 185 (Deferred Tax, 30.06.2025
comparative column) — not a zero-standing flag, a data-legibility flag.

## 4. Consolidated Segment Reporting (page 4, lines 227-264)

| Line | Item | 30.06.2026 | 31.03.2026 | 30.06.2025 | 31.03.2026(Y) | Flags |
|---|---|---|---|---|---|---|
| 232 | 1 Segment Revenue [header] | — | — | — | — | |
| 233 | Amines & Speciality Chemicals | 45,288.92 | 39,353.31 | 35,737.27 | 1,41,568.99 | |
| 234 | Hotel Division | 798.81 | 837.73 | 1,026.54 | 3,570.15 | |
| 235 | Unallocated | 124.50 | 134.04 | 62.89 | 587.49 | |
| 236 | Sub Total | 46,212.23 | 40,325.08 | 36,826.70 | 1,45,726.63 | |
| 237 | Less: Inter-segment revenue | 67.18 | 72.60 | 90.58 | 347.90 | |
| 238 | Revenue from operations | 46,145.05 | 40,252.49 | 36,736.12 | 1,45,378.74 | |
| 239 | 2 Segment Results before Tax & Interest [header] | — | — | — | — | |
| 240 | Amines & Speciality Chemicals | 10,544.76 | 8,581.55 | 4,544.16 | 22,525.09 | |
| 241 | Hotel Division | 159.78 | 163.78 | 390.02 | 937.36 | |
| 242 | Unallocated | 57.04 | 58.30 | 40.04 | 323.62 | |
| 243 | Total | 10,761.58 | 8,803.63 | 4,974.22 | 23,786.07 | |
| 244 | a Less: Interest [header] | — | — | — | — | |
| 245 | Amines & Speciality Chemicals | 135.38 | 214.16 | 67.18 | 517.58 | |
| 246 | Hotel Division | 5.84 | 3.42 | 5.70 | 19.46 | |
| 247 | Unallocated | - | - | - | - | ZERO_STANDING (all 4 periods dash; OCR renders as "=") |
| 248 | Total | 141.22 | 217.58 | 72.88 | 537.04 | |
| 249 | b Segment Profit/(Loss) before tax [header] | — | — | — | — | |
| 250 | Amines & Speciality Chemicals | 10,409.38 | 8,367.39 | 4,476.98 | 22,007.51 | |
| 251 | Hotel Division | 153.93 | 160.36 | 384.32 | 917.90 | |
| 252 | Unallocated | 57.04 | 58.30 | 40.04 | 323.62 | |
| 253 | Total | 10,620.36 | 8,586.04 | 4,901.34 | 23,249.03 | |
| 255 | 3 Segment Assets [header] | — | — | — | — | |
| 256 | Amines & Speciality Chemicals | 2,57,731.41 | 2,65,370.86 | 2,22,243.00 | 2,65,370.86 | |
| 257 | Hotel Division | 6,315.10 | 6,133.44 | 5,830.51 | 6,133.44 | |
| 258 | Unallocated | 2,676.28 | 2,749.38 | 1,399.34 | 2,749.38 | |
| 259 | Total | 2,66,722.79 | 2,74,253.67 | 2,29,472.85 | 2,74,253.67 | |
| 260 | 4 Segment Liabilities [header] | — | — | — | — | |
| 261 | Amines & Speciality Chemicals | 28,958.53 | 45,364.44 | 17,516.34 | 45,364.44 | |
| 262 | Hotel Division | 1,316.39 | 1,035.83 | 351.36 | 1,035.83 | |
| 263 | Unallocated | 13,467.89 | 12,681.53 | 10,448.70 | 12,681.53 | |
| 264 | Total | 43,742.82 | 59,081.80 | 28,316.40 | 59,081.80 | |

Segment: 32 logical rows across two segments (Amines & Speciality Chemicals; Hotel
Division) plus Unallocated, across four sub-tables (Revenue, Results/Interest/PBT,
Assets, Liabilities). ZERO_STANDING count: 1 (line 247).

Only two operating segments disclosed: Amines & Speciality Chemicals, Hotel Division.
No third segment present in either period — confirmed by sweep of all four sub-tables.

## 5. Numbered Notes (page 5, lines 289-304)

| # | Line | First ~15 words | Flags |
|---|---|---|---|
| 1 | 291-295 | "The above unaudited results, as reviewed by the Audit Committee at their meeting held on July 27, 2026, were considered, approved..." | Confirms unmodified auditor opinion in-note |
| 2 | 296-298 | "The financial results for the quarter ended June 30, 2026 are prepared in accordance with the Indian Accounting Standards..." | |
| 3 | 299-301 | "The Consolidated financial results are prepared based on Ind AS 110 'Consolidated Financial Statements'. The consolidated results include results of subsidiary, Balaji Speciality Chemicals Limited." | Names the sole consolidated subsidiary — cross-ref Section 6 |
| 4 | 302 | "Segment information is given as per Ind AS-108 'Operating Segments'." | |
| 5 | 303-304 | "This statement is prepared as per Regulation 33 of the SEBI (Listing Obligation and Disclosure Requirements) Regulations, 2015." | |

No unnumbered footnotes, asterisked notes, or "Note:" prefixed table footnotes found
elsewhere in the document (swept full text for "*", "†", "Note:" markers outside the
notes block — only stray OCR noise matched, e.g. line 49's "30*"" and line 382's
"7*A'" address fragment, neither of which is a footnote marker).

## 6. Auditor Review Reports — every paragraph, both reports

### 6a. Standalone Review Report (page 6, lines 325-384) — Auditor: M. Anandam & Co.

| Line | Element | Flags |
|---|---|---|
| 330-332 | Report title: "Independent Auditor's Review Report on the Quarterly Unaudited Standalone Financial Results ... Regulation 33 ... Regulations, 2015" | |
| 334-335 | Addressee: "Review Report to the Board of Directors, Balaji Amines Limited" | |
| 337-340 | Para 1 — scope: reviewed unaudited standalone financial results for quarter ended 30 June 2026, submitted per Reg. 33 LODR | |
| 342-346 | Para 2 — responsibility: Statement is Management's responsibility, approved by Board, prepared per Ind AS 34; auditor's responsibility to report based on review | |
| 348-354 | Para 3 — review standard: conducted per SRE 2410, moderate assurance, review is less in scope than audit, no audit opinion expressed | |
| 356-361 | Para 4 — conclusion: unmodified — "nothing has come to our attention that causes us to believe" the statement is materially misstated or non-compliant with Reg. 33 disclosure | Opinion type: UNMODIFIED. No Emphasis of Matter paragraph. No Other Matters paragraph. No Going Concern language. |
| 364-366 | Firm block: "For M. Anandam & Co., Chartered Accountants (Firm Regn. No. 000125S)" | |
| 367-374 | Digital signature block: Venkata Mamidipudi Ranganath, digitally signed, embedded timestamp "Date:2026.07.27 17:25:29 +0550" (OCR-garbled timezone offset, plausibly +0530 IST) | **SIGNATURE_BEFORE_BOARD_CLOSE** — embedded digital-signature time 17:25:29 (5:25:29 PM) is earlier than the Board Meeting's stated conclusion time of 5:35 P.M. (line 57). The printed "Date: 27-07-2026" (no time) at line 377 does not itself conflict, but the timestamped digital certificate does. |
| 373-376 | Partner: MYV Ranganath, Partner, Membership Number 028031, UDIN: 26028031YSNDDY5906 | |
| 376-377 | Place: Secunderabad; Date: 27-07-2026 | |

Standalone: 4 numbered paragraphs, unmodified opinion, entity reviewed = Balaji
Amines Limited (standalone only). No Emphasis of Matter, no Other Matters, no Going
Concern paragraph, no mention of any unaudited/management-furnished component (none
applicable — standalone entity only).

### 6b. Consolidated Review Report (page 7, lines 385-442) — Auditor: M. Anandam & Co.

| Line | Element | Flags |
|---|---|---|
| 391-393 | Report title: "Independent Auditor's Review Report on the Quarterly Consolidated Unaudited Financial Results ... Regulation 33 ... Regulations, 2015" | |
| 394-395 | Addressee: "Review Report to the Board of Directors, Balaji Amines Limited" | |
| 397-401 | Para 1 — scope: reviewed Statement of Unaudited Consolidated Financial Results of Balaji Amines Limited ("the Holding Company") and its subsidiary, Balaji Speciality Chemicals Limited (together "the Group"), quarter ended 30 June 2026 | Entities named: Holding Company + 1 subsidiary |
| 403-407 | Para 2 — responsibility: Statement is Holding Company Management's responsibility, approved by Holding Company Board, prepared per Ind AS 34; auditor's responsibility to express a conclusion | |
| 409-415 | Para 3 — review standard: conducted per SRE 2410, review is substantially less in scope than an audit, no audit opinion expressed | |
| 417 | Para 4 — Other Matter: "The Statement includes the results of the subsidiary, Balaji Speciality Chemicals Limited." | **OTHER_MATTERS paragraph** — this is the one structural difference vs. the standalone report (which has no equivalent para); flags which entity's results are folded in without a separate qualifying statement about that subsidiary's own audit/review status |
| 419-425 | Para 5 — conclusion: unmodified — "nothing has come to our attention..." statement not materially misstated / non-compliant with Reg. 33 | Opinion type: UNMODIFIED. No Emphasis of Matter paragraph. No Going Concern language. |
| 427-429 | Firm block: "For M. Anandam & Co., Chartered Accountants (Firm Regn. No. 000125S)" | |
| 430-434 | Digital signature block: "Digitally signed by VENKATA... MAMIDIPUDI... 538" | Timestamp not legibly extracted — OCR renders only fragment "538" with no clear date/time separators visible in source text (unlike the standalone block which cleanly shows "2026.07.27 17:25:29"). **OCR_UNCERTAIN** on this timestamp; cannot confirm or rule out a before/after-board-close conflict for this signature independently of the printed date line below. |
| 434-436 | Partner: MV Ranganath, Partner, Membership Number 028031, UDIN: 26028031WOMXUR3189 | Distinct UDIN from the standalone report (correct — one UDIN per engagement) |
| 437-438 | Place: Secunderabad; Date: 27-07-2026 | |

Consolidated: 5 numbered paragraphs (one more than standalone — the "Other Matter" at
para 4), unmodified opinion, entities reviewed = Balaji Amines Limited (Holding
Company) + Balaji Speciality Chemicals Limited (subsidiary). No entity in the
consolidated scope is flagged in the report text as unaudited or management-furnished
by a component auditor — the same firm, M. Anandam & Co., appears to have reviewed
the subsidiary's numbers directly (no reference to "other auditors" or reliance
language anywhere in either report).

## 7. Consolidation-List Entities

| Entity | Relationship | First cited | Flags |
|---|---|---|---|
| Balaji Amines Limited | Holding Company / parent (also the standalone reporting entity) | Line 335 (standalone report addressee); line 398 (consolidated report, "the Holding Company") | |
| Balaji Speciality Chemicals Limited | Subsidiary, consolidated per Ind AS 110 | Line 301 (Note 3); line 398 (consolidated report para 1); line 417 (para 4) | Sole subsidiary named anywhere in the filing |

No prior-quarter ledger was supplied for this ticker (first quarterly-pipeline
coverage of BALAMINES — see task inputs: "no prior quarterly run for this ticker").
No diff is possible; this list is the baseline. ENTITY_CHANGE is therefore not
assessable this cycle — flag as **BASELINE_NO_PRIOR_LEDGER** rather than
ENTITY_CHANGE. Future quarters should diff their consolidation list against this
2-entity baseline (1 parent + 1 subsidiary, no JVs, no associates, no step-down
subsidiaries named).

## 8. Digital / Physical Signature Blocks

| # | Line(s) | Signatory | Designation | Timestamp as extracted | Flags |
|---|---|---|---|---|---|
| 1 | 65-70 | Abhijeet Kothadiya | Company Secretary & Compliance Officer | Letter dated "27th July, 2026" (line 29); no time-of-day given; appears to be a scanned/wet signature (OCR renders the signature graphic as garbled text "psvobadth"), not a digital-certificate timestamp | Not comparable to board-close time (no time-of-day present) |
| 2 | 364-377 | Venkata Mamidipudi Ranganath (MYV Ranganath), Partner, M. Anandam & Co. | Statutory Auditor — Standalone Review Report | Digital cert timestamp "2026.07.27 17:25:29 +0550"; printed date "27-07-2026" | **SIGNATURE_BEFORE_BOARD_CLOSE** — 17:25:29 precedes the Board Meeting's stated close of 5:35 P.M. (line 57) by roughly 10 minutes |
| 3 | 427-438 | Venkata Mamidipudi Ranganath (MV Ranganath), Partner, M. Anandam & Co. | Statutory Auditor — Consolidated Review Report | Digital cert timestamp illegible in extract (fragment "538" only); printed date "27-07-2026" | **OCR_UNCERTAIN** — cannot determine before/after-board-close status from this extract; recommend A3/A4 pull the source PDF's certificate metadata directly if this matters to the review |

## 9. Not Applicable to This Doctype

No annexures, no director-profile tables, no ESOP/capital-raising resolutions, no
concall transcript content (turns/questions/mgmt numbers), no investor-presentation
content (slides) are present in this results filing. All corresponding YAML count
fields are set to 0 below, not omitted.

---

```yaml
stage: A2-enumerator
company: "BALAMINES"
quarter: "Q1 FY27"
doctype: "results"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/balamines-q1fy27/work/ledger_results_balamines_q1fy27.md"
counts:                      # per applicable category
  notes: 5
  line_items: 102
  zero_standing: 13
  agenda_items: 3
  auditor_paras: 9
  entities: 2
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
flags_raised: [ZERO_STANDING, SIGNATURE_BEFORE_BOARD_CLOSE, OCR_UNCERTAIN, BASELINE_NO_PRIOR_LEDGER]
gate_a2: pass
mismatch_note: ""
```
