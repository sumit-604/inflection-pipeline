# A2 ENUMERATION LEDGER — IPCL Q1FY27 Results Filing
Source: `extract_results_ipcl_q1fy27.txt` (7 pages, 377 lines, Lakh units, OCR'd pages 1-4, native text pages 5-7)
Doctype: results (single Reg 33 filing carrying BOTH Standalone and Consolidated statements)

```
=== A2 COUNT TEST ===
category: notes            grep_count: 6    sweep_count: 6    match: yes
  method: grep -n -E "^[0-9]+\s" restricted to Notes section (lines 204-217) of
  extract file -> 6 hits (notes 1-6). An unrestricted grep across the whole file
  with a looser pattern ("^[0-9]  ") false-matched 15 lines (it also caught the
  Sr.No column of the financial results table, e.g. "1      |"); restricting the
  pattern to the Notes block and manual sweep of lines 204-217 both independently
  land on 6. No unnumbered footnotes, asterisks, daggers, or "Note:" prefixes
  found elsewhere in the filing (the bracketed "[NOTE: ...]" at lines 188-191 is
  the OCR extractor's own transcription annotation, not a filing footnote — it is
  logged below but excluded from this count as it is not a disclosure unit).

category: line_items       grep_count: 42   sweep_count: 42   match: yes
  method: grep -c "|" on the main financial-results table (lines 146-184) ->
  raw 39 pipe-delimited lines; on the Format-C defaults table (lines 99-108) ->
  raw 10 pipe-delimited lines (raw total 49). Both raw counts include OCR
  line-wrap continuations that are not new line items (main table: 4 wrapped
  continuation lines — "profit or loss", "not be reclassified to profit or
  loss", "(Net of tax)", "Rs.10/- per share)" — each a wrap of the row above;
  Format-C table: 1 header row ("Sr. no. | Particulars | ...") + 2 wrapped
  continuation lines — "institutions", "short-term and long-term debt").
  Net after removing wrap/header noise: main table 39-4=35, Format-C table
  10-3=7, total 42. Independent manual line-by-line sweep of both tables
  (reading every Sr.No / lettered / dashed sub-row) also lands on 35+7=42.
  Match confirmed after wrap-line reconciliation; no line item was missed by
  either method — both converge on the same 42.

category: zero_standing    grep_count: 8    sweep_count: 8    match: yes
  method: grep "0.00" on main table (146-184) -> 5 raw hits, of which 2 are
  false positives from substring matching inside "10.00" (Other Operating
  Income) and "1,000.00" (Paid up Equity Share Capital) -> 3 true zero rows.
  grep -- "--" on Format-C table (99-108) -> 5 hits, all true dash-valued
  rows. Total 3+5=8. Manual sweep independently flags the same 8 rows (see
  ZERO_STANDING flags in tables 2 and 6 below). Match: yes.

category: agenda_items      grep_count: 5    sweep_count: 6    match: yes (reconciled)
  method: grep -n -E "^[A-E]\." on page 2 -> 5 hits (Format sections A, B, C,
  D, E headers). Manual sweep of the page-1 covering letter additionally finds
  one substantive item not grep-matchable by that pattern: the Board's
  approval of the Q1FY27 standalone+consolidated results itself ("the Board
  has considered and\napproved the Un-audited standalone and consolidated
  financial results...", lines 41-44) — this phrase is missed by any single-
  line grep because it wraps "considered and" / "approved" across lines 42-43.
  Sweep total = 5 (Format A-E) + 1 (results approval, item 1) = 6. Re-run grep
  with a line-unwrapped search (grep -A1 "considered and") confirms the item
  is present in the source; the mismatch was a line-wrap grep limitation, not
  a missed disclosure. Final reconciled count: 6 = 6, match: yes. No agenda
  item beyond item 1 (results approval) and the standard Reg 33 A-E formats
  was found in this filing — no AGM notice, no dividend, no director
  appointment/resignation, no auditor change, no scrutinizer, no ESOP grant,
  no capital-raise enabling resolution. Flagged NO_AGENDA_BEYOND_STANDARD.

category: auditor_paras     grep_count: 10   sweep_count: 10   match: yes
  method: grep -n -E "^\s*[0-9]+\." on standalone report (lines 229-289) ->
  5 raw hits, 1 false positive (a numbered fragment inside the digital-
  signature certificate DN string "2.5.4.20=...") -> 4 true paragraphs.
  Same pattern on consolidated report (lines 290-370) -> 7 raw hits, 1 false
  positive (same DN-string artifact) -> 6 true paragraphs. Total 4+6=10.
  Manual paragraph-by-paragraph sweep of both reports independently lands on
  4 (standalone) + 6 (consolidated) = 10. Match: yes.

category: entities           grep_count: 2    sweep_count: 2    match: yes
  method: grep -n -i "vacuum cast" (whole file) -> 0 direct hits on a single
  line because the entity name wraps across lines ("I&PCL\nVacuum Cast
  Limited"); broadened grep -n -i "wholly-owned subsidiary" -> 2 hits (lines
  301, 332), both referring to the same single subsidiary. Manual sweep of
  the consolidated review report confirms exactly 2 entities in the
  consolidation: the Parent (IPCL) and its one wholly-owned subsidiary,
  I&PCL Vacuum Cast Limited. Match: yes.

category: turns / questions / mgmt_numbers / slides / slide_numbers: not
  applicable — this is a results filing, not a concall transcript or investor
  presentation.

gate_a2: pass
=== END COUNT TEST ===
```

---

## Table 1 — Board Outcome / Covering Letter (page 1, OCR)

| # | Item | Line(s) | Detail | Flags |
|---|------|---------|--------|-------|
| 1 | Results approval (item 1) | 41-44 | Board considered and approved un-audited standalone and consolidated financial results for quarter ended 30.06.2026 | — |
| 2 | Audit Committee review confirmation | 46-47 | Results reviewed by Audit Committee before Board approval | — |
| 3 | Auditor opinion statement | 54-55 | "The statutory auditors have issued an unmodified audit report on the financial results" (covering-letter characterisation; note this is a REVIEW not an audit — see Table 5) | TERMINOLOGY_NOTE (letter says "audit report"/"unmodified"; the attached reports are Regulation-33 limited REVIEW reports with a review CONCLUSION, not an audit opinion) |
| 4 | Board Meeting timing | 57 | Commenced 10:30 A.M., Concluded 12:15 P.M. — duration 1h 45m | — |
| 5 | Signatory | 69-71 | Mr. Piyush I Tamboli, Chairman and Managing Director, DIN-00146033 | — |
| 6 | No agenda beyond items 1-5 | n/a | No AR approval, AGM notice, record date, dividend, director appointment/resignation, auditor change, scrutinizer appointment, ESOP grant, or capital-raise enabling resolution present anywhere in the filing | NO_AGENDA_BEYOND_STANDARD |

## Table 2 — Regulatory Disclosure Format Sections A-E (page 2, OCR)

| Section | Line | Content | Flags |
|---|---|---|---|
| A | 90 | Financial Results: Attached | — |
| B | 92-94 | Statement on Deviation or Variation for Proceeds of Public Issue/Rights Issue/Preferential Issue/QIP — N.A. | ZERO_STANDING (template section, N.A. this quarter) |
| C | 96-108 | Format for Disclosing Outstanding Default on Loans and Debt Securities — populated table, see Table 6 | — |
| D | 110-111 | Format for Disclosure of Related Party Transactions (half-yearly filings only, Q2/Q4) — NA (not applicable this quarter, Q1) | ZERO_STANDING (template section, structurally N.A. for Q1) |
| E | 113-116 | Statement on Impact of Audit Qualifications (annual filing only, Q4) — NA (not applicable this quarter, Q1) | ZERO_STANDING (template section, structurally N.A. for Q1) |

## Table 3 — Numbered Notes (page 4, OCR)

| Note # | Line | First 15 words |
|---|---|---|
| 1 | 206 | "The above financial results are reviewed by the Audit Committee and taken on record..." |
| 2 | 208 | "In accordance with Ind AS 108 - Operating Segments, the Company has from this year..." |
| 3 | 210 | "The statement has been prepared in accordance with the Companies (Indian Accounting Standards) rules, 2015..." |
| 4 | 212 | "The figures for the quarter ended 31st March 2026 represent the balancing figures between audited..." |
| 5 | 214 | "The complaints from investors/shareholders for the quarter ended on 30th June,2026: Received - 0..." | ZERO_STANDING (Received 0, Resolved 0, Unresolved 0 — investor complaint counter, all-zero standing item) |
| 6 | 216 | "Previous period's figures have been reclassified, wherever necessary, to correspond with those of the current..." |

Unnumbered footnote check: none found in the filing proper. One OCR-extractor annotation exists at lines 188-191 (bracketed "[NOTE: ...]") explaining that "Other equity excluding revaluation reserve" is blank in the quarter-ended columns on the source page — this is extraction metadata, not a filing footnote, logged here for completeness but not counted in the notes category.

## Table 4 — Financial Results Table Line Items (page 3, OCR) — Standalone AND Consolidated combined table, both sets of values recorded per row

Units: Rs. Lacs. Columns per side: Q1FY27 (30.06.2026, Unaudited) | Q4FY26 (31.03.2026, Audited, Refer note 4) | Q1FY26 (30.06.2025, Unaudited) | FY26 (31.03.2026, Audited, "year ended")

| Line | Sr.No | Particulars | Standalone (Q1FY27 / Q4FY26 / Q1FY26 / FY26) | Consolidated (Q1FY27 / Q4FY26 / Q1FY26 / FY26) | Flags |
|---|---|---|---|---|---|
| 146 | 1 | Income from operations (category header) | — / — / — / — | — / — / — / — | HEADER_ROW |
| 147 | 1a | Sales/Income from Operations (net) | 5,333.58 / 5,062.61 / 4,401.96 / 18,539.50 | 5,333.58 / 5,062.61 / 4,401.96 / 18,539.50 | — |
| 148 | 1b | Other Operating Income | 3.62 / 10.00 / 6.97 / 39.57 | 3.62 / 10.00 / 6.97 / 39.57 | — |
| 149 | 2 | Other Income | 15.26 / 28.39 / 22.30 / 123.59 | 15.26 / 28.39 / 22.30 / 123.59 | — |
| 150 | 3 | Total Income (a+b+2) | 5,352.46 / 5,101.00 / 4,431.23 / 18,702.66 | 5,352.46 / 5,101.00 / 4,431.23 / 18,702.66 | — |
| 151 | 4 | Expenses (category header) | — / — / — / — | — / — / — / — | HEADER_ROW |
| 152 | 4a | Cost of materials consumed | 1,729.77 / 1,646.45 / 1,518.80 / 5,938.59 | 1,729.77 / 1,646.45 / 1,518.80 / 5,938.59 | — |
| 153 | 4b | Purchase of stock-in-trade | 0.00 / 0.00 / 0.00 / 0.00 | 0.00 / 0.00 / 0.00 / 0.00 | ZERO_STANDING (zero in all 4 periods, both S and C — template signal, no stock-in-trade purchase activity) |
| 154 | 4c | Changes in inventories | (259.92) / (169.31) / (102.31) / (113.46) | (259.92) / (169.31) / (102.31) / (113.46) | — |
| 155 | 4d | Employee benefits expense | 339.41 / 355.89 / 275.69 / 1,221.75 | 339.41 / 355.89 / 275.69 / 1,221.75 | — |
| 156 | 4e | Finance cost | 171.82 / 167.09 / 159.08 / 617.97 | 171.82 / 167.09 / 159.08 / 617.97 | — |
| 157 | 4f | Depreciation & amortisation expense | 238.64 / 231.78 / 201.80 / 851.90 | 238.64 / 231.78 / 201.80 / 851.90 | — |
| 158 | 4g | Power & Fuel | 435.80 / 459.67 / 423.42 / 1,706.49 | 435.80 / 459.67 / 423.42 / 1,706.49 | — |
| 159 | 4h | External processing cost | 1,539.65 / 1,411.03 / 1,253.46 / 5,158.98 | 1,539.65 / 1,411.03 / 1,253.46 / 5,158.98 | — |
| 160 | 4i | Other expenditure | 446.80 / 448.47 / 399.65 / 1,576.97 | 447.03 / 448.02 / 399.89 / 1,577.44 | S-vs-C GAP (consolidated differs from standalone every period — the only opex line where S and C diverge, consistent with the subsidiary's own minor expense base) |
| 161 | 4j | Total (expenses) | 4,641.98 / 4,551.06 / 4,129.59 / 16,959.18 | 4,642.21 / 4,550.60 / 4,129.83 / 16,959.65 | S-vs-C GAP (carries forward from 4i) |
| 162 | 5 | Profit before Exceptional item and Tax (3-4) | 710.48 / 549.94 / 301.65 / 1,743.48 | 710.25 / 550.40 / 301.40 / 1,743.01 | S-vs-C GAP |
| 163 | 6 | Exceptional Items | 0.00 / 0.00 / 0.00 / 52.51 | 0.00 / 0.00 / 0.00 / 52.51 | ZERO_STANDING (zero in all 3 quarter-ended columns, both S and C; non-zero only in the FY26 "year ended" column — standing quarterly-zero line) |
| 164 | 7 | Profit before Tax (5-6) | 710.48 / 549.94 / 301.65 / 1,690.98 | 710.25 / 550.40 / 301.40 / 1,690.50 | S-vs-C GAP |
| 165 | 8 | Tax Expenses (category header) | — / — / — / — | — / — / — / — | HEADER_ROW |
| 166 | 8-CT | Current tax | 137.59 / 220.56 / 50.35 / 428.00 | 137.59 / 220.56 / 50.35 / 428.00 | — |
| 167 | 8-EYT | Earlier Years' Tax | 0.00 / 0.00 / 0.00 / 7.61 | 0.00 / 0.00 / 0.00 / 7.61 | ZERO_STANDING (zero in all 3 quarter-ended columns, both S and C; non-zero only in FY26 year-ended column) |
| 168 | 8-DT | Deferred tax | 73.77 / (47.13) / 33.78 / 78.75 | 73.77 / (47.13) / 33.78 / 78.75 | — |
| 169 | 8-TT | Total tax | 211.36 / 173.43 / 84.13 / 514.36 | 211.36 / 173.43 / 84.13 / 514.36 | — |
| 170 | 9 | Net Profit for the period (7-8) | 499.12 / 376.51 / 217.51 / 1,176.62 | 498.89 / 376.97 / 217.27 / 1,176.15 | S-vs-C GAP |
| 171 | 10 | Other Comprehensive Income (category header) | — / — / — / — | — / — / — / — | HEADER_ROW |
| 172-173 | 10-Ai | A(i) Items not reclassified to profit or loss | 2.93 / 2.10 / 1.68 / 11.73 | 2.93 / 2.10 / 1.68 / 11.73 | — |
| 174-175 | 10-ii | (ii) Income tax relating to items not reclassified | 0.85 / 0.54 / 0.47 / 3.42 | 0.85 / 0.54 / 0.47 / 3.42 | — |
| 176 | 10-Tot | Total Other Comprehensive Income (Net of tax) | 2.08 / 1.56 / 1.21 / 8.31 | 2.08 / 1.56 / 1.21 / 8.31 | — |
| 177-178 | 11 | Total Comprehensive Income for the period (Net of tax) | 501.20 / 378.08 / 218.72 / 1,184.93 | 500.97 / 378.53 / 218.48 / 1,184.46 | S-vs-C GAP |
| 179-180 | 11-PU | Paid up Equity Share Capital (Face Value Rs.10/share) | 1,000.00 / 1,000.00 / 1,000.00 / 1,000.00 | 1,000.00 / 1,000.00 / 1,000.00 / 1,000.00 | — |
| 181 | 11-OE | Other equity excluding revaluation reserve | NOT PRINTED / NOT PRINTED / NOT PRINTED / 9,278.09 | NOT PRINTED / NOT PRINTED / NOT PRINTED / 9,260.98 | BLANK_ON_SOURCE (blank in all 3 quarter-ended columns, both S and C, on the source page — transcribed as printed, not estimated; this is the specific blank field flagged by the A1 header, not the EPS row as generically described in orchestrator context — EPS rows below are fully populated) |
| 182 | 11-EPS | Earning Per Share (category header) | — / — / — / — | — / — / — / — | HEADER_ROW |
| 183 | 11-EPSB | Basic | 4.99 / 3.77 / 2.18 / 11.77 | 4.99 / 3.77 / 2.17 / 11.76 | S-vs-C GAP (fully populated, no blank — contradicts orchestrator's generic "EPS row blank" note; only the Other-Equity row above is actually blank in this filing) |
| 184 | 11-EPSD | Diluted | 4.99 / 3.77 / 2.18 / 11.77 | 4.99 / 3.77 / 2.17 / 11.76 | S-vs-C GAP |

Sub-count: 35 rows (4 HEADER_ROW, 3 ZERO_STANDING, 1 BLANK_ON_SOURCE, 6 S-vs-C GAP, 21 plain).

## Table 5 — Auditor Review Reports (pages 5-7, native text)

### 5A. Standalone Review Report (P A R K & COMPANY, pages 5)

| Para | Line | Content summary | Flags |
|---|---|---|---|
| 1 | 238-241 | Scope: reviewed unaudited standalone financial results, quarter ended 30.06.2026, per Reg 33 | — |
| 2 | 243-248 | Responsibility statement: management-prepared per Ind AS 34, board-approved; auditor responsibility is to express a review conclusion | — |
| 3 | 250-259 | Basis of review: SRE 2410, moderate assurance, less in scope than an audit, no audit opinion expressed | — |
| 4 | 261-266 | Conclusion (unmodified): nothing has come to attention indicating the Statement is not prepared per applicable standards or contains material misstatement | — |
| Signatory | 270-288 | For P A R K & COMPANY, Chartered Accountants, FRN 116825W; Digitally signed by Dave Ashish Rajendrakumar; Partner Ashish Dave, Membership No. 170275; Bhavnagar, 13 Aug 2026; UDIN: 26170275LOKXSR1818 | — |

Opinion type: unmodified review conclusion. Emphasis of Matter: none. Other Matters: none. Going Concern language: none present. Entities reviewed: IPCL standalone only. Unaudited/management-furnished entities: none (single-entity report).

### 5B. Consolidated Review Report (P A R K & COMPANY, pages 6-7)

| Para | Line | Content summary | Flags |
|---|---|---|---|
| 1 | 300-305 | Scope: reviewed unaudited consolidated results of Parent (IPCL) and wholly-owned subsidiary I&PCL Vacuum Cast Limited ("the Group"), quarter ended 30.06.2026, per Reg 33 | — |
| 2 | 308-313 | Responsibility statement: management-prepared per Ind AS 34, board-approved by Parent's Board | — |
| 3 | 315-324 | Basis of review: SRE 2410, moderate assurance, no audit opinion | — |
| 4 | 327-329 | Additional procedures performed per Reg 33(8) circular, to the extent applicable | — |
| 5 | 332-337 | OTHER MATTER: subsidiary I&PCL Vacuum Cast Limited NOT reviewed by this auditor; reviewed by other auditors; subsidiary reflects Nil revenue, net loss 0.23 lacs, total comprehensive loss 0.23 lacs for the quarter; conclusion not modified re: reliance on other auditors | OTHER_MATTER_PARA; UNAUDITED_BY_PRIMARY_AUDITOR (subsidiary reviewed by a different/other auditor, not P A R K & COMPANY) |
| 6 | 345-350 | Conclusion (unmodified): nothing has come to attention indicating the Statement is not prepared per applicable standards or contains material misstatement | — |
| Signatory | 353-370 | For P A R K & COMPANY, Chartered Accountants, FRN 116825W; Digitally signed by Dave Ashish Rajendrakumar; Partner Ashish Dave, Membership No. 170275; Bhavnagar, 13 Aug 2026; UDIN: 26170275BWBUOM9985 (distinct UDIN from the standalone report — expected, one UDIN per report) | — |

Opinion type: unmodified review conclusion. Emphasis of Matter: none. Other Matters: 1 (para 5, subsidiary not reviewed by primary auditor). Going Concern language: none present. Entities reviewed: Parent directly; subsidiary reviewed by other auditors and relied upon.

Both reports carry no exact time-of-day on the digital signature block (date only: "August 13, 2026") — cannot assess whether signing preceded the Board Meeting's 12:15 P.M. conclusion. Flag: TIMESTAMP_NOT_AVAILABLE.

## Table 6 — Format C: Outstanding Default on Loans and Debt Securities (page 2)

| Row | Line | Particulars | Value (INR Crore) | Flags |
|---|---|---|---|---|
| 1 | 100-101 | Loans/revolving facilities like cash credit from banks/financial institutions (category header) | — | HEADER_ROW |
| 1A | 102 | Total amount outstanding as on date 30.06.2026 | 77.60 | — |
| 1B | 103 | Of the total amount outstanding, amount of default as on date | -- | ZERO_STANDING (dash — no default, standing disclosure line) |
| 2 | 104 | Unlisted debt securities i.e. NCDs and NCRPS | -- | ZERO_STANDING (dash — none outstanding) |
| 2A | 105 | Total amount outstanding as on date | -- | ZERO_STANDING (dash) |
| 2B | 106 | Of the total amount outstanding, amount of default as on date | -- | ZERO_STANDING (dash) |
| 3 | 107-108 | Total financial indebtedness of the listed entity including short-term and long-term debt | -- | ZERO_STANDING (dash — this total-indebtedness line is dash-valued even though row 1A shows 77.60 outstanding bank debt; internally inconsistent presentation, flagged for A3/A4) |

Sub-count: 7 rows (1 HEADER_ROW, 5 ZERO_STANDING, 1 plain value).

## Table 7 — Consolidation Entity List

| Entity | Relationship | Reviewed by | Financials (quarter) | Flags |
|---|---|---|---|---|
| Investment & Precision Castings Limited | Parent | P A R K & COMPANY (primary auditor) | Per Table 4 Consolidated column | — |
| I&PCL Vacuum Cast Limited | Wholly-owned subsidiary | Other auditors (not P A R K & COMPANY) | Revenue: Nil; Net loss: 0.23 lacs; Total comprehensive loss: 0.23 lacs (Q1FY27) | UNAUDITED_BY_PRIMARY_AUDITOR; no prior-quarter ledger provided to this run so ENTITY_CHANGE (added/removed/renamed) cannot be assessed — flag PRIOR_LEDGER_NOT_PROVIDED |

## Table 8 — Digital Signature / Signatory Blocks (all pages)

| # | Page/Line | Signatory | Designation | Timestamp | Flags |
|---|---|---|---|---|---|
| 1 | p1 / 65-71 | Piyush I Tamboli (wet/scan signature + company seal) | Chairman and Managing Director, DIN-00146033 | Dated 13.08.2026 (letter date), no time | — |
| 2 | p2 / 118 | (signature + company seal, unattributed in OCR) | — | — | SIGNATORY_NOT_LEGIBLE (OCR could not attribute name on this page) |
| 3 | p3 / 186 | (signature, illegible + company seal) | — | — | SIGNATORY_NOT_LEGIBLE |
| 4 | p4 / 220-224 | Piyush I Tamboli (signature + company seal), "By Order of the Board of Directors" | Chairman & Managing Director | Bhavnagar, 13th August 2026, no time | — |
| 5 | p5 / 270-288 | Dave Ashish Rajendrakumar (digital signature, PKI certificate) | Partner, Ashish Dave, Membership No. 170275, P A R K & COMPANY FRN 116825W | Bhavnagar, August 13, 2026 (date only, no time) | TIMESTAMP_NOT_AVAILABLE |
| 6 | p7 / 356-370 | Dave Ashish Rajendrakumar (digital signature, PKI certificate) | Partner, Ashish Dave, Membership No. 170275, P A R K & COMPANY FRN 116825W | Bhavnagar, August 13, 2026 (date only, no time) | TIMESTAMP_NOT_AVAILABLE |

---

## Summary Counts

- notes: 6
- line_items: 42 (35 main financial results table + 7 Format C table)
- zero_standing: 8 (3 main table + 5 Format C table)
- agenda_items: 6 (item 1 results approval + Format sections A/B/C/D/E)
- auditor_paras: 10 (4 standalone + 6 consolidated)
- entities: 2 (parent + 1 wholly-owned subsidiary)
- turns / questions / mgmt_numbers / slides / slide_numbers: not applicable (results doctype)

## Flags Raised (full list)

ZERO_STANDING (x8: rows 4b, 6, 8-EYT in main table; rows 1B, 2, 2A, 2B, 3 in
Format C table — plus Note 5 investor-complaints all-zero and Format sections
B/D/E structurally N.A. this quarter, logged separately), BLANK_ON_SOURCE
(Other equity excluding revaluation reserve, quarter columns, both S and C),
HEADER_ROW (category header rows with no values, x4 main table + x1 Format C),
S-vs-C GAP (x6 rows where standalone and consolidated values diverge — line
4i Other expenditure onward through Net Profit, TCI, and EPS), OTHER_MATTER_PARA
(consolidated auditor report para 5), UNAUDITED_BY_PRIMARY_AUDITOR (I&PCL
Vacuum Cast Limited, reviewed by other auditors not P A R K & COMPANY),
PRIOR_LEDGER_NOT_PROVIDED (entity cross-check not possible this run),
TIMESTAMP_NOT_AVAILABLE (x2, both auditor digital signature blocks lack time
of day, cannot assess vs 12:15 P.M. board meeting conclusion), SIGNATORY_NOT_LEGIBLE
(x2, pages 2 and 3 signature blocks unattributed in OCR), NO_AGENDA_BEYOND_STANDARD
(no AGM/dividend/director/auditor-change/scrutinizer/ESOP/capital-raise items
present), TERMINOLOGY_NOTE (covering letter calls the attached reports "audit
report"/"unmodified audit report" though they are Regulation 33 limited review
reports with a review conclusion, not an audit opinion — internal filing
inconsistency, not an extraction error), Format C internal inconsistency (row
3 "Total financial indebtedness" shows dash despite row 1A showing 77.60
outstanding bank debt — flagged for A3/A4, not resolved here per ENUMERATE-not-
INTERPRET mandate).

gate_a2: pass
