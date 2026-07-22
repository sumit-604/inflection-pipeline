# A2 ENUMERATION LEDGER — BANDHAN Q1FY27 — Results filing
Source: extract_results_bandhan_q1fy27.txt (Reg 30 Board Outcome + Reg 33 Unaudited
Financial Results, standalone + Independent Auditor's Limited Review Report + Press Release)
Unit convention per A1 header: Reg 33 tables (pages 4-8) in **Lakhs**; Press Release
(pages 11-13) already in **Rs crore**, stated as-is, NOT converted. Flag `UNIT_MIX` applies
wherever lakhs-tables and crore-press-release figures are read side by side.

Note on GATE A2 process: two tables below (Main P&L, Segment AS-17) initially showed a
grep/sweep mismatch because naive regex patterns missed rows using inconsistent row-label
formats in the OCR text (e.g. "I) Employees Cost" vs "(a) Gross NPAs" vs "5.2" vs "7.2.").
Each was re-swept manually against the raw extract and the regex re-run with a corrected
pattern; all categories below are reported POST-reconciliation with the mismatch explained
inline. Final state: all categories match, GATE A2 = pass.

```
=== A2 COUNT TEST ===
category: notes (Notes section, main numbered 1-16)     grep_count: 16   sweep_count: 16   match: yes
category: agenda_items (Board Outcome letter)            grep_count: 4    sweep_count: 4    match: yes
category: auditor_paras (Review Report paras 1-6)        grep_count: 6    sweep_count: 6    match: yes
category: line_items (all financial tables, combined)    grep_count: 112  sweep_count: 112  match: yes (post re-sweep; naive grep on Main P&L table initially caught 29/34 and on Segment table 31/32 -- missed rows recovered on manual re-sweep, see per-table notes below)
category: zero_standing (subset of line_items)           grep_count: 18   sweep_count: 18   match: yes
category: entities (statutory-review scope)              grep_count: 1    sweep_count: 1    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

---

## 1. BOARD OUTCOME LETTER — AGENDA ITEMS (beyond mere "item 1 = results")

| # | Line(s) | Agenda item | Detail | Flags |
|---|---------|-------------|--------|-------|
| 1 | 41-61 | Approval of Unaudited Financial Results, Q1 ended June 30, 2026 | Board meeting held today (July 21, 2026); enclosures: (i) Unaudited Financial Results, (ii) Limited Review Report by Joint Statutory Auditors, (iii) Press Release; Earnings Update Presentation submitted separately; trading window (closed since July 01, 2026 for DPs/relatives/Auditors/Connected Persons) to reopen 48 hrs after declaration | — |
| 2 | 63-89 | KMP change — CFO | Ref. prior letter BBL/SEC/074/2026-27 dated June 29, 2026 re resignation of Mr. Rajeev Mantri, CFO/KMP, last working day Sept 25, 2026. Board today approved appointment of Mr. Vinay Jain as (Interim) CFO and KMP, effective Sept 26, 2026, till March 31, 2027. Brief profile given (CA, commerce graduate, 20+ yrs; Head-Finance & Accounts at Bandhan since March 2025; prior: DBS Bank, Citibank, ICICI Bank; India + Singapore exposure) | KMP_CHANGE |
| 3 | 92-106 | KMP-adjacent change — Chief of Internal Vigilance (CIV) | Ref. prior letter BBL/SEC/212/2025-26 dated Feb 12, 2026 re interim appointment of Mr. Prakash E as CIV effective Feb 24, 2026 for 6 months/till new CIV joins. Board today approved EXTENSION of Mr. Prakash E's interim CIV term up to Sept 30, 2026 or till new CIV joins, whichever earlier. Brief profile given (~25 yrs experience, joined Bank/Vigilance Nov 21, 2022; BSc Biochemistry + MSc Cyber Forensics, Univ. of Madras; prior: ICICI Bank Financial Crime Prevention Group, Samsung Chief Manager-Global Forensic Audit, Chemplast Sanmar AGM-Special Audits) | — |
| 4 | 109-118 | AGM notice + dividend record date | 12th AGM of Members to be held Monday, Aug 24, 2026, 11:00 a.m. IST via VC/OAVM. Record Date for Dividend purpose fixed as Monday, Aug 17, 2026. Dividend (if declared by Members at AGM) payable within 30 days of declaration | — |

Board meeting timing: commenced 09:45 A.M., concluded 03:35 P.M. (line 124) — approx. **5 hours 50 minutes**, a long meeting consistent with the volume of KMP/governance business layered onto the quarterly results approval.

Signature blocks (4 total, all dated July 21, 2026, Place: Kolkata; none carry an intra-day
timestamp beyond the date, so `SIGNATURE_BEFORE_CONCLUSION` cannot be confirmed or ruled out):
| # | Line(s) | Signatory | Designation | Doc |
|---|---------|-----------|-------------|-----|
| 1 | 133-143 | Indranil Banerjee | Company Secretary | Board Outcome covering letter |
| 2 | 539-544 | (Name obscured by scan artifact) | Managing Director (DIN partially legible "08273...") | Unaudited Financial Results statement |
| 3 | 626-639 | Karthik Srinivasan | Partner, V. Sankar Aiyar & Co. (FRN 109208W), Membership No. 514998, UDIN 26514998ZKYHRU9403 | Limited Review Report |
| 4 | 626-640 | Sunil Singhi | Partner, V. Singhi & Associates (FRN 311017E), Membership No. 060854, UDIN 26060854QEAWDT1141 | Limited Review Report |

---

## 2. NOTES SECTION — NUMBERED NOTES 1-16 (grep = sweep = 16, GATE pass)

| Note # | Line | First ~15 words | Flags |
|--------|------|------------------|-------|
| 1 | 334 | "The financial results for the quarter ended June 30, 2026 have been subjected to Limited Review..." names joint auditors V. Sankar Aiyar & Co. + V. Singhi & Associates; prior-year comparative reviewed by "then" joint auditors Singhi & Co. + V. Sankar Aiyar & Co. | AUDITOR_CHANGE (Singhi & Co. -> V. Singhi & Associates, name/entity differs from predecessor) |
| 2 | 339 | "These financial results have been prepared in accordance with the recognition and measurement principles..." (AS under Sec 133 Companies Act, Banking Regulation Act 1949, RBI guidelines, Reg 33) | — |
| 3 | 346 | "The figures for the quarter ended March 31, 2026 are the balancing figures between audited figures..." (Q4FY26 = FY26 audited minus 9M published, itself only reviewed not audited) | INCOMPLETE_DISCLOSURE (comparative column basis is a balancing figure, not independently reviewed/audited on its own) |
| 4 | 350 | "During the quarter ended June 30, 2026, the Bank has allotted 1,05,686 Equity Shares..." (ESOP exercise; share capital +Rs10.57 lakh, premium +Rs139.95 lakh, Rs60.48 lakh transferred from ESOP-outstanding to securities premium) | — |
| 5 | 355 | "In accordance with RBI guidelines, consolidated Pillar 3 disclosure, Leverage Ratio, Liquidity Coverage Ratio and Net Stable Funding Ratio..." — disclosed on website only, NOT subject to audit/limited review | UNREVIEWED_DISCLOSURE |
| 6 | 361 | "Details of loans transferred and acquired excluding through Inter-Bank Participation Certificate (IBPC)..." per RBI Nov 28, 2025 Master Direction — contains sub-parts (i)-(iv), see Section 4 below | — |
| 7 | 430 | "The Bank has applied its significant accounting policies in the preparation of these financial results consistent with those followed..." (continuity of accounting policy vs FY26 annual accounts) | — |
| 8 | 434 | "In accordance with RBI Direction RBI/2026-27/79 ... the Bank has included the profits earned during the quarter..." for CRAR computation; also transferred Rs21,567.42 lakh from Investment Fluctuation Reserve (IFR) to P&L balance per Second Amendment Directions 2026 | — |
| 9 | 442 | "Disclosure related to Project Finance for the quarter ended June 30, 2026 as per the Reserve Bank of India..." — full table, see Section 5 below | — |
| 10 | 495 | "On November 21, 2025, the Government of India notified the Code on Wages, 2019, the Industrial Relations Code, 2020..." (Labour Codes) — Bank revised salary structure, recognized additional gratuity liability of Rs6,082.72 lakh (Q1FY27) and Rs12,039.04 lakh (FY26) under Employee Cost | — |
| 11 | 505 | "Other Operating Expenses includes -" Office Rent and IT Operating Expenses breakout, see Section 6 below | — |
| 12 | 518 | "Other Income includes profit/loss on investments including provision for revaluation, earnings from foreign exchange..." (narrative composition note, no table) | — |
| 13 | 523 | "As at June 30, 2026, the total number of Branches, Banking Units and ATM network stood at 1988, 4400 and 438 respectively." | — |
| 14 | 527 | "The Bank does not have any Subsidiary, Associate or Joint venture as at June 30, 2026. Accordingly the Bank is not required to..." publish consolidated results | — (drives entities count = 1, standalone only) |
| 15 | 531 | "The above results have been recommended by the Audit Committee at its meeting held on July 20, 2026 and approved by the Board..." (Audit Committee met one day before the Board, July 20 vs July 21, 2026) | — |
| 16 | 535 | "Figures of the previous year/period's have been regrouped / reclassified wherever necessary to conform to current year/period's classification." | — |

Note: the report also contains 6 numbered paragraphs (1-6) INSIDE the Limited Review Report
(lines 561-624) — these are NOT part of the 16 Notes above; they belong to the separate
"auditor_paras" category (Section 7) per the operating rules (never conflate categories).

---

## 3. MAIN P&L / REG 33 FINANCIAL RESULTS TABLE (pages 4, lines 148-234) — 34 line items

Units: Rs Lakhs. Columns: Q1 FY27 (30.06.2026, Unaudited) | Q4 FY26 (31.03.2026, Audited,
Refer Note 3) | Q1 FY26 (30.06.2025, Unaudited) | FY26 (31.03.2026, Audited).

| # | Line | Particular | ZERO/dash in all periods? | Flags |
|---|------|-----------|---------------------------|-------|
| 1 | 162 | Interest Earned (a+b+c+d) | no | — |
| 1a | 164 | Interest/discount on advances/bills | no | — |
| 1b | 166 | Income on Investments | no | — |
| 1c | 167-168 | Interest on balance with RBI and other inter-bank funds | no | — |
| 1d | 170 | Others (interest earned) | no | — |
| 2 | 172 | Other Income | no | — |
| 3 | 174 | Total Income (1+2) | no | — |
| 4 | 176 | Interest Expended | no | — |
| 5 | 178 | Operating Expenses (i+ii) | no | — |
| 5(i) | 180 | Employees Cost | no | — |
| 5(ii) | 182 | Other Operating Expenses | no | — |
| 6 | 183-185 | Total Expenditure (4+5) (Excluding Provisions & Contingencies) | no | — |
| 7 | 186-188 | Operating Profit before Provisions & Contingencies (3-6) | no | — |
| 8 | 190 | Provisions (other than tax) & Contingencies | no | — |
| 9 | 192 | Exceptional Items | YES — dash all 4 periods | **ZERO_STANDING** |
| 10 | 193-195 | Profit from ordinary activities before tax (7-8-9) | no | — |
| 11 | 197 | Tax Expenses | no | — |
| 12 | 198-200 | Net Profit from ordinary activities after tax (10-11) | no | — |
| 13 | 202 | Extraordinary items (net of tax expenses) | YES — dash all 4 periods | **ZERO_STANDING** |
| 14 | 204 | Net Profit for the period (12-13) | no | — |
| 15 | 205-207 | Paid up equity share capital (FV Rs10/- each) | no | — |
| 16 | 209 | Reserve excluding revaluation reserves | value only in FY26 (annual) column, blank in quarterly columns per standard Reg-33 template convention | INCOMPLETE_DISCLOSURE (template convention, not a true zero) |
| 17 | 211 | Analytical Ratios: (header) | n/a | header row |
| 17(i) | 212-213 | Percentage of shares held by Government of India | YES — NIL all 4 periods | **ZERO_STANDING** |
| 17(ii) | 215 | Capital Adequacy Ratio (%) | no | — |
| 17(iii) | 216-218 | Earning per share (Face Value Rs10/- each): (header) | n/a | header row |
| 17(iii)(a) | 219 | Basic EPS before & after extraordinary items* | no | *"figures for quarters not annualised" |
| 17(iii)(b) | 221 | Diluted EPS before & after extraordinary items* | no | *"figures for quarters not annualised" |
| 17(iv) | 223 | NPA Ratios: (header) | n/a | header row |
| 17(iv)(a) | 225 | Gross NPAs | no | — |
| 17(iv)(b) | 227 | Net NPAs | no | — |
| 17(iv)(c) | 229 | % of Gross NPAs to Gross Advances | no | — |
| 17(iv)(d) | 231 | % of Net NPAs to Net Advances | only 2 of 4 period columns populated (Q1FY27, Q4FY26); Q1FY26 and FY26 blank in extract | INCOMPLETE_DISCLOSURE |
| 17(v) | 232 | Return on Assets (average)* | only 1 of 4 period columns populated (Q4FY26: 0.27%) | INCOMPLETE_DISCLOSURE — flag for A3/A4: confirm against source PDF whether Q1FY27 RoA is truly absent from the table or an extraction artifact |

Reconciliation note: initial grep pattern (row-label regexes for "N", "a)", "(i)") caught only
29/34 rows on the first pass, missing 5(i) "I) Employees Cost", 5(ii) "ii) Other Operating
Expenses", 17(i) "(I) Percentage...", 17(ii) "{II) Capital Adequacy...", and 17(iv) "(Iv) NPA
Ratios:" header — all due to inconsistent OCR case/bracket rendering of roman numerals.
Manual re-sweep of the full table (lines 162-232) confirmed 34 total rows; a corrected
grep pattern then also reached 34. GATE A2 pass for this table post-reconciliation.

---

## 4. SEGMENT REPORTING — AS 17 (page 5, lines 236-330) — 32 line items

Units: Rs Lakhs, same 4-column structure as Section 3.

| # | Line | Particular | ZERO/dash all periods? | Flags |
|---|------|-----------|--------------------------|-------|
| 1 | 250 | Segment Revenue (header) | n/a | header |
| 1a | 251 | Treasury | no | — |
| 1b | 252 | Retail Banking | no | — |
| 1c | 253 | Wholesale Banking | no | — |
| 1d | 254 | Other Banking Operations | no | — |
| 1e | 255 | Unallocated | YES — dash all 4 periods | **ZERO_STANDING** |
| — | 256 | Total (Segment Revenue) | no | — |
| — | 257 | Less: Inter segment revenue | no | — |
| — | 258 | Income from operations | no | — |
| 2 | 260 | Segment Results (header) | n/a | header |
| 2a | 261 | Treasury | no | — |
| 2b | 262 | Retail Banking | no | — |
| 2c | 263 | Wholesale Banking | no (negative in all periods, loss-making segment) | — |
| 2d | 264 | Other Banking Operations | no | — |
| 2e | 265 | Unallocated | YES — dash all 4 periods | **ZERO_STANDING** |
| — | 266 | Total Profit Before Tax | no | — |
| 3 | 268 | Segment Assets (header) | n/a | header |
| 3a | 269 | Treasury | no | — |
| 3b | 270 | Retail Banking | no | — |
| 3c | 271 | Wholesale Banking | no | — |
| 3d | 272 | Other Banking Operations | no | — |
| 3e | 273 | Unallocated | no (has values, not zero) | — |
| — | 274 | Total (Segment Assets) | no | — |
| 4 | 276 | Segment Liabilities (header) | n/a | header |
| 4a | 277 | Treasury | no | — |
| 4b | 278 | Retail Banking | no | — |
| 4c | 279 | Wholesale Banking | no | — |
| 4d | 280 | Other Banking Operations | YES — dash all 4 periods | **ZERO_STANDING** |
| 4e | 281 | Unallocated | no (has values) | — |
| — | 282 | Total (Segment Liabilities) | no | — |
| 5 | 286 | Capital, Employees stock options outstanding and Reserves | no | — |
| 6 | 289 | Total (4)+(5) | no | — |

Footnote/definitional rows (lines 292-316, not separately counted as line items):
DBU sub-segmentation not applicable disclosure ("Bank does not have any Digital Banking
Unit"); qualitative definitions of Treasury / Retail Banking / Corporate-Wholesale Banking /
Other Banking Business.

Reconciliation note: initial grep matched 31/32 rows, missing row 5 "Capital, Employees
stock options outstanding and Reserves" (line 286) because it carries no "a)/b)" letter
prefix, no "Segment" keyword, and no "Total/Less/Income from" keyword. Manual re-sweep of
lines 250-289 confirmed 32 total rows. GATE A2 pass post-reconciliation.

---

## 5. NOTE 6 SUB-TABLES — LOAN TRANSFER / ACQUISITION DISCLOSURES (pages 6-7) — 18 line items

### 6(i) Loans acquired through assignment, not in default (lines 365-374) — 5 items
| Line | Particular | Value | Flags |
|------|-----------|-------|-------|
| 369 | Aggregate amount of loans acquired* (Rs lakhs) | 1,87,079.09 | *loans not rated |
| 370 | Weighted average residual maturity (years) | 1.62 | — |
| 371 | Weighted average holding period by originator (years) | 0.49 | — |
| 372 | Retention of beneficial economic interest by originator | 10.00% | — |
| 373 | Tangible security coverage (%) | 35.89% | — |

### 6(ii) Stressed-loan acquisition/transfer activity — narrative nil disclosure (lines 376-377) — 1 item
| Line | Particular | Flags |
|------|-----------|-------|
| 376-377 | "the bank has not acquired any stressed loans (NPA and SMA) and not transferred any loan not in default/SMA" during the quarter | **ZERO_STANDING** (combined nil disclosure covering two transaction types: stressed-loan acquisition and not-in-default/SMA transfer) |

### 6(iii) Stressed loans transferred / SR investment, to ARCs (lines 379-409) — 8 items
| Line | Particular | Value | Flags |
|------|-----------|-------|-------|
| 387 | No of accounts | 2,986 | — |
| 388 | Aggregate principal outstanding of loans transferred (Rs lakhs) | 29,143.83 | — |
| 389 | Weighted average residual tenor of loans transferred (years) | 12.57 | — |
| 390 | Net book value of loans transferred (at time of transfer) (Rs lakhs) | 11,413.00 | — |
| 392 | Sale consideration (Rs lakhs) | 11,948.98 | — |
| 395-396 | Additional consideration realized in respect of accounts transferred in earlier years (Rs lakhs) | dash | **ZERO_STANDING** |
| 397-400 | Excess provisions reversed to Profit and Loss Account (Rs lakhs)* | 535.98 | *quantum accounted per RBI guidelines, max up to portion where cash received exceeds net book value |
| 401 | Investment made in Security Receipts (SR's) (Rs lakhs) | dash | **ZERO_STANDING** |

### 6(iv) Ratings of Security Receipts (SRs) outstanding (lines 412-427) — 4 items
| Line | Rating | Rating Agency | Recovery Rating | Gross value outstanding SRs (Rs lakhs) | Flags |
|------|--------|--------------|------------------|------------------------------------------|-------|
| 418-420 | RR2 | CRISIL | 75%-100% | 26,636.00** | **footnote: gross value of outstanding SRs 100% provided |
| 421 | RR3 | CRISIL | 50%-75% | 20,637.00 | — |
| 422 | RR4 | CRISIL | 25%-50% | 13,550.50 | — |
| 423 | Unrated* | — | — | 55.93 | *face value reduced to Rs1, hence not rated by ARCs |

---

## 6. NOTE 9 — PROJECT FINANCE DISCLOSURE TABLE (page 7-8, lines 442-476) — 16 line items

| Item | Line | Description | No. of accounts | Total outstanding (Rs lakhs) | Flags |
|------|------|-------------|------------------|-------------------------------|-------|
| 1 | 450 | Projects under implementation accounts at beginning of quarter | 40 | 1,70,081.95 | — |
| 2 | 451 | Projects under implementation accounts sanctioned during quarter | 14 | 39,087.88 | — |
| 3 | 452-453 | Projects under implementation accounts where DCCO achieved during quarter | 6 | 21,063.37 | — |
| 4 | 454 | Projects under implementation accounts at end of quarter (1+2-3)* | 48 | 1,92,933.02 | — |
| 5 | 456-457 | Out of '4' — resolution process involving DCCO extension invoked | 6 | 37,566.43 | — |
| 5.1 | 458 | Out of '5' — Resolution plan implemented | 6 | 37,566.43 | — |
| 5.2 | 459 | Out of '5' — Resolution plan under implementation | dash | dash | **ZERO_STANDING** |
| 5.3 | 460 | Out of '5' — Resolution plan failed | dash | dash | **ZERO_STANDING** |
| 6 | 461-463 | Out of '5' — extension invoked due to change in scope/size of project | 1 | 3,606.72 | — |
| 7 | 464-465 | Out of '5' — cost overrun associated with extension was funded | dash | dash | **ZERO_STANDING** |
| 7.1 | 466-467 | Out of '7' — SBCF sanctioned during financial closure and renewed continuously | dash | dash | **ZERO_STANDING** |
| 7.2 | 468 | Out of '7' — SBCF not presanctioned or renewed continuously | dash | dash | **ZERO_STANDING** |
| 8 | 469-470 | Out of '4' — resolution process not involving DCCO extension invoked | dash | dash | **ZERO_STANDING** |
| 8.1 | 471 | Out of '8' — Resolution plan implemented | dash | dash | **ZERO_STANDING** |
| 8.2 | 472 | Out of '8' — Resolution plan under implementation | dash | dash | **ZERO_STANDING** |
| 8.3 | 476 | Out of '8' — Resolution plan failed | dash | dash | **ZERO_STANDING** |

Reconciliation note: naive grep on this table caught 15/16 rows, missing item "7.2." because
the double-period format ("7.2. Out of...") broke a single-digit-then-space regex. Manual
re-sweep confirmed 16 rows (items 1-8 plus sub-items 5.1/5.2/5.3, 6, 7.1/7.2, 8.1/8.2/8.3).
Note the heavy concentration of ZERO_STANDING rows (9 of 16) here — a template signal that
the Bank currently has no cost-overrun-funded, SBCF, or "not-involving-DCCO-extension"
project finance stress, but the line items exist because RBI's disclosure format anticipates
them.

---

## 7. NOTE 11 — OTHER OPERATING EXPENSES BREAKOUT (page 8, lines 505-516) — 2 line items

| Line | Particular | Q1 FY27 (Rs lakhs) | Q1 FY26 (Rs lakhs) | Flags |
|------|-----------|---------------------|----------------------|-------|
| 511-512 | Office Rent | 10,276.18 | 9,454.40 | — |
| 514-515 | IT Operating Expenses | 15,624.06 | 8,116.85 | IT opex nearly doubled YoY — flag for A4 interpretation, not A2 |

---

## 8. AUDITOR'S INDEPENDENT REVIEW REPORT — PARAGRAPHS 1-6 (pages 9-10, lines 554-640) — auditor_paras = 6

Entities reviewed: **Bandhan Bank Limited, standalone only** (Note 14: no subsidiary,
associate, or joint venture as at June 30, 2026 — no consolidated results required).
Joint statutory auditors: V. Sankar Aiyar & Co. (FRN 109208W) and V. Singhi & Associates
(FRN 311017E).

| Para | Line | Content | Type | Flags |
|------|------|---------|------|-------|
| 1 | 561-569 | Scope: reviewed Statement for quarter ended June 30, 2026, per Reg 33; Pillar 3/leverage/LCR disclosures on website NOT reviewed by auditors; Statement "initialled ... for identification purpose only" | Scope paragraph | **UNREVIEWED_DISCLOSURE** (Pillar 3/LCR/leverage/NSFR) |
| 2 | 571-582 | Management's responsibility: Statement prepared per AS 25 "Interim Financial Reporting", Sec 133 Companies Act, Banking Regulation Act 1949, RBI Guidelines; auditor's responsibility is to express a conclusion based on review | Responsibility paragraph | — |
| 3 | 583-593 | Review conducted per SRE 2410; moderate assurance (not audit-level); explicitly "we do not express an audit opinion" | Basis-of-review paragraph | opinion type = LIMITED REVIEW (moderate assurance / negative assurance), NOT an audit opinion |
| 4 | 600-612 | Conclusion: "nothing has come to our attention that causes us to believe" the Statement is non-compliant or materially misstated (clean/unmodified limited-review conclusion); repeats Note 5 Pillar 3/LCR carve-out | Conclusion paragraph | UNMODIFIED conclusion; no going-concern paragraph anywhere in report (absent, not applicable/not disclosed) |
| 5 | 614-617 | Comparative-period note: Q1 FY26 results were "jointly audited" (NB: audited, not merely reviewed) by one of the current joint auditors plus the PREDECESSOR auditor, per their report dated July 18, 2025, unmodified opinion | Other-Matter-type paragraph (not headed "Other Matters") | **AUDITOR_CHANGE** flag (predecessor auditor no longer joint auditor); also note comparative-period figures were audited, current period is only reviewed — a review/audit-level asymmetry across periods |
| 6 | 619-624 | Comparative-period note: Q4 FY26 (31.03.2026) figures per Note 3 are balancing figures between FY26 audited annual figures and published 9M (upto Dec 31, 2025) figures, and the 9M figures "had only been reviewed and not subjected to audit" | Other-Matter-type paragraph (not headed "Other Matters") | INCOMPLETE_DISCLOSURE — Q4FY26 comparative column is a derived balancing figure, not independently audited/reviewed in its own right |

Auditor report structure notes:
- No paragraph is explicitly labeled "Emphasis of Matter" or "Other Matters" — paras 5 and 6
  function as such but are unlabeled. Flag `EOM_UNLABELED`.
- No Going Concern paragraph present anywhere in the report. Flag `GOING_CONCERN_ABSENT`
  (informational — standard for a bank review report, not itself an adverse signal, but
  recorded per the enumerate-everything mandate).
- UDINs: Karthik Srinivasan (V. Sankar Aiyar & Co.) — 26514998ZKYHRU9403; Sunil Singhi
  (V. Singhi & Associates) — 26060854QEAWDT1141. Both dated July 21, 2026, Place: Kolkata.

---

## 9. PRESS RELEASE — "KEY HIGHLIGHTS OF QUARTERLY PERFORMANCE" TABLE (page 12, lines 713-725) — 10 line items

Units: **Rs crore** (per its own header — NOT lakhs; do not double-convert per A1 header
instruction). Flag `UNIT_MIX` applies when reading this table against Sections 3-7 above.

| Line | Particular | Q1 FY27 | Q1 FY26 | YoY Growth |
|------|-----------|---------|---------|------------|
| 716 | Advances | 1,55,555 | 1,33,625 | 16.4% |
| 717 | Deposits | 1,64,886 | 1,54,666 | 6.6% |
| 718 | CASA | 48,479 | 41,858 | 15.8% |
| 719 | Retail Deposits (CASA + RTD) | 1,21,956 | 1,05,519 | 15.6% |
| 720 | Net Interest Income | 2,921 | 2,757 | 5.9% |
| 721 | Net Total Income | 3,524 | 3,483 | 1.2% |
| 722 | Net Profit | 502 | 372 | 34.9% |
| 723 | Gross NPA (%) | 3.1% | 5.0% | -182 bps |
| 724 | Net NPA (%) | 0.9% | 1.4% | -43 bps |
| 725 | CRAR* (Including Profits) | 18.2% | 19.4% | -114 bps |

Also present in the press release narrative (lines 644-712), not re-tabulated as separate
line items but flagged for A3/A4 awareness: 5 headline bullets (PAT +35% YoY at Rs502cr;
gross advances +16% YoY; deposits +7% YoY; retail deposits (CASA+RTD) +16%, retail/total
74%; secured advances +27% YoY at ~57% of loan book; GNPA 3.1%/NNPA 0.9% improved
sequentially); narrative KPIs (CASA ratio >29%, EEB collection efficiency flat at 98.5%,
Provision Coverage Ratio incl. technical write-offs 85.9%, NIM 6.2% flat sequentially, RoA
1.0%, RoE 7.7%, distribution network ~6,400 outlets, >74,500 employees, MD & CEO Partha
Pratim Sengupta quote). YoY growth figure for Net Profit shown in bullet ("35%") vs table
("34.9%") — rounding only, not a discrepancy for A2 purposes but noted for A3/A4.

---

## 10. WHAT THIS FILING DOES NOT CONTAIN (absence, recorded per instructions)
- No consolidated financial results (Note 14: no subsidiary/associate/JV) — entities count = 1.
- No dividend declaration in this filing itself (record date fixed; dividend, if any, to be
  declared by Members at the AGM, Aug 24, 2026) — this is a FUTURE/CONTINGENT item, not a
  ZERO_STANDING line item since there is no dividend line in the Reg 33 table at all.
- No investor-presentation content in this extract (per Board Outcome letter, the Earnings
  Update Presentation is "being submitted separately" — outside this doctype/extract; not
  enumerable here).
- No concall transcript in this doctype (results filing only).

---
Ledger complete. All categories reconciled per GATE A2 (see count test header).
