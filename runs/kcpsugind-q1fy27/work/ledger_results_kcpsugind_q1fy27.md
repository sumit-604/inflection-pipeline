# A2 COMPLETENESS LEDGER — K.C.P. Sugar and Industries Corporation Ltd. (KCPSUGIND), Q1 FY27, Results doctype

Source: `/home/user/inflection-pipeline/runs/kcpsugind-q1fy27/work/extract_results_kcpsugind_q1fy27.txt`
(9-page Reg 30/33 Board Outcome letter + Annexure I financial results/segment note (OCR pages 3-4) +
Standalone Limited Review Report + Consolidated Limited Review Report + Annexure 1 entity list)
Prior-quarter ledger: not supplied — no diff possible this run (ENTITY_CHANGE / DROPPED_SLIDE checks marked N/A).

OCR CAVEAT: pages 3 and 4 are OCR'd. Numeral OCR drift was found and is called out explicitly below
wherever it caused a first-pass grep undercount (the auditor's consolidated report paragraph "3." OCR'd
as "J.", the Annexure entity "3" OCR'd as "J.", and one segment sub-item "c)" OCR'd as "¢)"). In every
such case the manual sweep caught the row and a corrected grep (widened to the OCR variant) was re-run
to close the gate. See mismatch notes inline.

```
=== A2 COUNT TEST ===
category: agenda_items         grep_count: 5   sweep_count: 5   match: yes
category: notes                grep_count: 6   sweep_count: 6   match: yes
category: pnl_line_items       grep_count: 37  sweep_count: 37  match: yes
category: segment_categories   grep_count: 4   sweep_count: 4   match: yes
category: segment_line_items   grep_count: 41 (naive) -> 43 (OCR-corrected)   sweep_count: 43   match: yes (after re-sweep; naive grep missed 2 OCR-garbled rows: "(2) Other un-allocable expenditure" and "c) Power & Fuel" in Capital Employed, both re-found on manual sweep and confirmed by widened grep)
category: auditor_paras_standalone     grep_count: 6   sweep_count: 6   match: yes
category: auditor_paras_consolidated   grep_count: 6 (naive) -> 7 (OCR-corrected)   sweep_count: 7   match: yes (after re-sweep; naive grep missed OCR-garbled para "3." rendered as "J.", re-found on manual sweep and confirmed by widened grep)
category: entities              grep_count: 3 (naive) -> 4 (OCR-corrected)   sweep_count: 4   match: yes (after re-sweep; naive grep missed entity #3 "THE EIMCO-K.C.P Limited" whose leading digit OCR'd as "J.", re-found on manual sweep and confirmed by widened grep)
category: signature_blocks      grep_count: 4   sweep_count: 4   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Total line-item disclosure units on this ledger: 5 agenda items + 6 notes + 37 P&L rows (incl. 5
structural header rows) + 4 segment category headers + 1 segment sub-header ("Segment Liabilities") +
43 segment line items + 13 auditor-report paragraphs (6 standalone + 7 consolidated) + 4 Annexure-1
entities + 4 signature blocks = **117 enumerated disclosure units**.

---

## 1. Board Outcome — Agenda Items (Reg 30 & 33 letter, pages 1-2)

Board meeting: commenced 15:30 Hrs, concluded 15:50 Hrs (12 Aug 2026) — 20-minute meeting (line 39-40).

| # | Line(s) | Agenda item | First ~15 words | Flags |
|---|---------|-------------|------------------|-------|
| 1 | 43-50 | Unaudited Financial Results for quarter ended 30.06.2026 | "Unaudited Standalone and Consolidated Financial Results of the Company for the quarter ended 30th June 2026" | — |
| 2 | 52-55 | Annual General Meeting (AGM) | "The 31st AGM of the Company is scheduled to be held on Thursday, 24th September 2026" | — |
| 3 | 57-62 | Dividend | "The Board decided to recommend to the members a final dividend of Re. 0.10/- per equity share" | — |
| 4 | 80-94 | Record date (dividend) | "Pursuant to Regulation 42 of SEBI (LODR), Regulation, 2015, we wish to inform that the Board" | Record date table: Book Closure Fri 18 Sep - Thu 24 Sep 2026; Record Date Thu 17 Sep 2026 (Record Date falling inside/before the book-closure open date as printed — verbatim as filed, worth a forensic look at internal date consistency) |
| 5 | 97-106 | Supply Contract: KCP Sugar & Industries Corp Ltd <-> The EIMCO-KCP Limited | "The Board approved the Supply contract order of Rs. 1,53,40,01,569 ... from The EIMCO-KCP Limited, Wholly owned Subsidiary" | RELATED_PARTY_TRANSACTION — counterparty is the company's own wholly owned subsidiary; order value Rs 153.40 Cr |

Items enumerated: 5/5. No agenda items beyond these five (no director appointment, auditor change,
scrutinizer appointment, ESOP grant, or capital-raising enabling resolution present in this filing).

---

## 2. Notes to the Results (OCR page 4, lines 266-284)

| Note # | Line | First ~15 words | Flags |
|--------|------|------------------|-------|
| 1 | 268-269 | "Sugar Industry being a seasonal industry and of a predominantly cyclical nature, the above results can neither" | — |
| 2 | 271-272 | "The above statement has been prepared to the extent applicable, in accordance with the Companies (Indian Accounting" | — |
| 3 | 274-275 | "The above Unaudited Standalone and Consolidated Financial Results were reviewed by the Audit Committee and approved" | — |
| 4 | 277-278 | "The Statutory Auditor of the Company have carried out a Limited Review of the above Standalone and" | — |
| 5 | 280-281 | "The figures for the quarter ended March 31, 2026 are the balancing figures between Audited Figures" | — |
| 6 | 283 | "Other Income includes Fair Value Gain on Equity Investments to the tune of Rs.5121.91 Lakhs in the" | Material — FV gain on equity investments is 5121.91 Lakhs of a 5477.56 Lakhs standalone Other Income line (~93.5% of the line); flagged for A3/A4 quality read on OCI-driven earnings |

No unnumbered footnotes or asterisked notes found elsewhere in the filing beyond these six.

---

## 3. P&L — Standalone AND Consolidated (single combined statement, OCR page 3, lines 147-200)

Both Standalone (Qtr 30.06.2026 / Qtr 31.03.2026 (Audited, bal. fig. per Note 5) / Qtr 30.06.2025 /
Year 31.03.2026 Audited) and Consolidated (same four periods) values sit in one row per line item.

| # | Line(s) | Caption | Type | Flags |
|---|---------|---------|------|-------|
| 1 | 147 | Revenue From Operations | value | — |
| 2 | 148 | Other Income | value | See Note 6 (FV gain concentration) |
| 3 | 149 | Total Income (I + II) | subtotal | — |
| 4 | 150 | IV. Expenses | header | structural, no own value |
| 5 | 151 | Cost of Materials Consumed | value | — |
| 6 | 152 | Purchase of Stock-In-Trade | value | — |
| 7 | 153-155 | Changes In Inventories of Finished Goods, WIP And Stock-In-Trade | value | — |
| 8 | 156 | Employee Benefits Expense | value | — |
| 9 | 157 | Finance Costs | value | — |
| 10 | 158 | Depreciation and Amortisation Expenses | value | — |
| 11 | 159 | Other Expenses | value | — |
| 12 | 160 | Total Expenses | subtotal | — |
| 13 | 161 | V. Profit Before Exceptional Items & Tax | subtotal | — |
| 14 | 162 | VI. Exceptional Items | value | ZERO_STANDING (dash, standalone AND consolidated, all 4 periods each) |
| 15 | 163 | VII. Profit / (Loss) Before Tax (V-VI) | subtotal | — |
| 16 | 164 | VIII. Tax Expense | header | structural, no own value |
| 17 | 165 | Current Tax | value | ZERO_STANDING (standalone only — dash all 4 standalone periods; consolidated carries values 26.02/225.02/42.49/472.01, NOT zero) |
| 18 | 166 | Deferred Tax (Asset) / Liability | value | — |
| 19 | 167-168 | Reversal of Excess Provision / Provision For Taxation Relating To Earlier Years | value | ZERO_STANDING (standalone, dash all 4 periods); consolidated near-zero (dash/dash/9.61/dash) — not flagged ZERO_STANDING for consolidated per the all-periods rule, but noted as template line |
| 20 | 169-170 | IX. Profit / (Loss) For The Period From Continuing Operations (VII-VIII) | subtotal | — |
| 21 | 171-172 | X. Profit / (Loss) From Discontinued Operations | value | ZERO_STANDING (dash, standalone AND consolidated, all periods) |
| 22 | 173 | XI. Tax Expense Of Discontinued Operations | value | ZERO_STANDING (dash, standalone AND consolidated, all periods) |
| 23 | 174-175 | XII. Profit / (Loss) From Discontinued Operations After Tax (X-XI) | value | ZERO_STANDING (dash, standalone AND consolidated, all periods) |
| 24 | 176 | XIII. Profit / (Loss) For The Period (IX+XII) | subtotal | — |
| 25 | 177 | Other Comprehensive Income | header | structural |
| 26 | 178 | Items That Will Not Be Reclassified To Profit / (Loss) | sub-header | structural |
| 27 | 179-180 | (i) Remeasurement of Defined Benefit Plan - Actuarial Gains / (Losses) | value | Standalone dash in current & year-ago quarters, values only in "Year Ended" columns (56.69/56.69) — a quarter-only zero pattern, noted not flagged |
| 28 | 181 | (ii) Income Tax Relating On Above | value | — |
| 29 | 182-183 | (iii) Equity Instruments Through Other Comprehensive Income | value | Standalone dash ALL 4 periods; consolidated carries values — ZERO_STANDING (standalone only) |
| 30 | 184 | Other Comprehensive Income - Total | subtotal | — |
| 31 | 185-189 | XV. Total Comprehensive Income For The Period | subtotal | — |
| 32 | 190 | XVI. Paid up Equity Share Capital (Face Value) | value | — |
| 33 | 191 | XVII. Other Equity | value | Only "Year Ended" columns populated (35060.35 / 44817.27); no quarter-end figure shown — standard for this line item, not flagged |
| 34 | 192 | Earnings Per Share (EPS) | header | structural |
| 35 | 193-194 | (a) Basic And Diluted EPS From Continuing Operations (Rs.) | value | — |
| 36 | 195-196 | (b) Basic And Diluted EPS From Discontinued Operations (Rs.) | value | ZERO_STANDING (dash, standalone AND consolidated, all periods) |
| 37 | 197-200 | (c) Basic And Diluted EPS From Continuing and Discontinued Operations (Rs.) | subtotal | — |

Correction to prior draft: on re-sweep, row 29 ((iii) Equity Instruments Through OCI) was reclassified
from "no flag" to ZERO_STANDING (standalone-only) — standalone shows dash across all four periods while
consolidated shows 434.41/(116.37)/(1.77)/(148.84); this is a genuine standalone-vs-consolidated
divergence worth an A3/A4 look (equity-investment fair-value routes only through the consolidated book).

P&L rows total: 37 (32 value/subtotal rows + 5 structural header rows). Zero-standing flags in this
table: 8 rows (line refs 162, 165, 167-168, 171-172, 173, 174-175, 182-183, 195-196).

---

## 4. Segment-Wise Revenue, Results, Capital Employed — Standalone AND Consolidated (OCR page 4, lines 207-265)

### 4.0 Segment categories (structural headers)

| Cat # | Line | Caption |
|-------|------|---------|
| 1 | 215 | SEGMENT WISE REVENUE |
| 2 | 225 | SEGMENT RESULT - PROFIT/(LOSS) BEFORE TAX AND INTEREST FROM EACH SEGMENT |
| 3 | 239 | Segment Assets (Liabilities sub-block at line 249, same category, unnumbered) |
| 4 | 258 | CAPITAL EMPLOYED (Segment Assets - Liabilities) |

### 4.1 Segment Wise Revenue (lines 216-224) — 9 rows

| Line | Item | Flags |
|------|------|-------|
| 216 | a) Sugar | — |
| 217 | b) Chemicals | — |
| 218 | c) Power & Fuel | Standalone/Consolidated dash in current & year-ago quarters (both years show 0 or dash for the quarter column); values only in year-ended columns — seasonal power segment, noted not flagged |
| 219 | d) Engineering | — |
| 220 | e) Others | — |
| 221 | f) Unallocated | Dash in current quarter (std & consol), small values (0.32/0.19/0.69) in other 3 periods — not all-periods-zero, not flagged |
| 222 | TOTAL | subtotal |
| 223 | Less: Inter Segment Revenue | value |
| 224 | Sales / Income from Operations | subtotal (ties to P&L row 1) |

### 4.2 Segment Result (lines 226-238) — 13 rows

| Line | Item | Flags |
|------|------|-------|
| 226 | a) Sugar | — |
| 227 | b) Chemicals | — |
| 228 | c) Power & Fuel | — |
| 229 | d) Engineering | — |
| 230 | e) Others | — |
| 231 | f) Unallocated | ZERO_STANDING (dash, standalone AND consolidated, all periods) |
| 232 | (A) Sub Total | subtotal |
| 233 | (1) Finance Cost | value |
| 234 | (2) Other un-allocable expenditure net of un-allocable income | value — OCR-garbled caption ("ba ey Saieniieert meno"); recovered on manual sweep, values intact and reconcile to (B) Sub Total |
| 235 | (B) Sub Total (1+2) | subtotal |
| 236 | Total Profit / (Loss) Before Tax (A-B) | subtotal (ties to P&L row 15) |
| 237 | Tax | value |
| 238 | Total Profit / (Loss) After Tax | subtotal (ties to P&L row 23/24) |

### 4.3 Segment Assets (lines 241-247) — 7 rows

| Line | Item | Flags |
|------|------|-------|
| 241 | a) Sugar | Standalone: 12281.28 / 13896.65 / 11131.63 / **43896.65** — the year-ended figure (43896.65) is ~3.15x the other periods and does not match the consolidated year-ended figure for Sugar (13828.69); arithmetic-consistency flag for A3/A4 (likely an OCR/typo digit insertion, e.g. "4" prefixed to "3896.65") |
| 242 | b) Chemicals | — |
| 243 | c) Power & Fuel | Standalone year-ended shows 4436.47 vs quarter figures ~1300-1400 range — same 4-prefix pattern as row 241, flag for A3/A4 |
| 244 | d) Engineering | — |
| 245 | e) Others | — |
| 246 | f) Unallocated | — |
| 247 | Total | subtotal — standalone total (53314.14 for both 31.03.2026 columns) does not foot cleanly against the sum of the above segment figures once the flagged 43896.65/4436.47 entries are included; flag ARITHMETIC_CHECK for A3 |

### 4.4 Segment Liabilities (lines 249-256, sub-block of category 3) — 7 rows (+1 sub-header at 249)

| Line | Item | Flags |
|------|------|-------|
| 249 | Segment Liabilities | sub-header, structural |
| 250 | a) Sugar | — |
| 251 | b) Chemicals | — |
| 252 | c) Power & Fuel | Consolidated year-ended shows 46.30 vs 16.30 in other consolidated periods — flag ARITHMETIC_CHECK (likely OCR digit swap 1->4) |
| 253 | d) Engineering | — |
| 254 | e) Others | — |
| 255 | f) Unallocated | — |
| 256 | Total | subtotal |

### 4.5 Capital Employed (lines 259-265) — 7 rows

| Line | Item | Flags |
|------|------|-------|
| 259 | a) Sugar | — |
| 260 | b) Chemicals | — |
| 261 | c) Power & Fuel | OCR-garbled leading character ("¢)"), recovered on manual sweep |
| 262 | d) Engineering | — |
| 263 | e) Others | — |
| 264 | f) Unallocated | — |
| 265 | Total Capital Employed in Segments | subtotal — consolidated total shows "4694133" (line 265) vs the 45951.11 comparator columns; almost certainly a decimal-point OCR drop of "46941.33"; flag OCR_SUSPECT for A3 to confirm against source PDF |

Segment line items total: 43 (9+13+7+7+7), plus 4 category headers and 1 sub-header (structural, not
double-counted in the 43).

---

## 5. Limited Review Report — Standalone (pages 5-6, lines 303-390)

| Para # | Line(s) | First ~15 words | Flags |
|--------|---------|------------------|-------|
| 1 | 309-313 | "We have reviewed the accompanying statement of unaudited standalone financial results of K.C.P. SUGAR" | OCR renders leading numeral as "7." — confirmed via manual sweep this is para 1 (opening scope paragraph) |
| 2 | 315-321 | "This Statement which is the responsibility of the Company's Management and approved by the Company's Board" | — |
| 3 | 323-330 | "We conducted our review of the Statement in accordance with the Standard on Review Engagements (SRE) 2410" | — |
| 4 | 332-343 | "In respect of the Company's Sugar unit and the incidental Co-generation unit attached to the Sugar unit" | Discloses deferred off-season expenses: Other expenditure Rs.943.99 Lakhs, Depreciation Rs.58.11 Lakhs — an Emphasis-of-Matter-style disclosure on accounting policy, not a qualification |
| 5 | 345-351 | "It has been explained to us by the Company's Management that, the Sugar Industry and the Incidental" | — |
| 6 | 363-369 | "Based on our review conducted as explained above and after duly considering the practice of recognizing" | Conclusion paragraph — unmodified/unqualified conclusion |

Signature block: KVNS Kishore, Partner, M.No. 206734, for B. Purushottam & Co. (FRN 002B0BS as OCR'd,
likely 002808S), UDIN 26206734DGDZKE9B4B, Place Chennai, Date 12 Aug 2026 (lines 373-390) — see
Section 7, signature block #3.

Standalone report paragraph count: 6/6.

---

## 6. Limited Review Report — Consolidated (pages 7-8, lines 400-502)

| Para # | Line(s) | First ~15 words | Flags |
|--------|---------|------------------|-------|
| 1 | 406-413 | "We have reviewed the accompanying statement of unaudited consolidated financial results of K.C.P. SUGAR" | OCR renders leading numeral as "7." — confirmed via manual sweep this is para 1 |
| 2 | 414-420 | "This Statement which is the responsibility of the Holding Company's Management and approved by the Holding" | — |
| 3 | 423-434 | "We conducted our review of the Statement in accordance with the Standard on Review Engagements (SRE) 2410" | OCR-garbled leading numeral rendered as "J." instead of "3." — MISSED by naive grep, recovered on manual sweep (see COUNT TEST). Also references SEBI Circular CIR/CFD/CMD1/44/2019 dated 29 Mar 2019 (Reg 33(3)(B)) |
| 4 | 436-447 | "In respect of the Holding Company's Sugar unit and the incidental Co-generation unit attached to the" | Same deferred off-season expense disclosure as standalone (Rs.943.99 Lakhs / Rs.58.11 Lakhs) |
| 5 | 454-460 | "It has been explained to us by the Holding Company's Management that, the Sugar Industry and the" | — |
| 6 | 463-469 | "Based on our review conducted as explained above and after duly considering the practice of recognizing" | Conclusion paragraph |
| 7 | 472-483 | "We did not review the interim financial results of 1 step down subsidiary included in the Statement" | OTHER MATTER paragraph — identifies 1 step-down subsidiary NOT reviewed by this auditor: total income (pre-consolidation) Rs.28.93 Lakhs, net loss (pre-consolidation) Rs.5.49 Lakhs, total comprehensive income (pre-consolidation) Rs.(5.49) Lakhs, reviewed by another auditor whose report was furnished to B. Purushottam & Co.; conclusion not modified in respect of this reliance |

Signature block: KVNS Kishore, Partner, M.No. 206734, for B. Purushottam & Co. (FRN OCR'd as 0028085,
likely 002808S), UDIN 26206734HQHINC5732 (OCR'd, contains stray character), Place Chennai, Date 12 Aug
2026 (lines 487-502) — see Section 7, signature block #4.

Consolidated report paragraph count: 7/7 (after re-sweep; naive grep initially returned 6 — see COUNT TEST).

Cross-check: which entities are unaudited / management-furnished — per para 7, ALL entities in the
consolidation are reviewed by the principal or component auditors except the 1 step-down subsidiary
(Quality Engineering, per Annexure 1) whose review was performed by another auditor and furnished to
B. Purushottam & Co. No entity in this filing is flagged as wholly unreviewed/management-furnished
without any auditor sign-off.

---

## 7. Signature / Signatory Blocks

| # | Line(s) | Signatory | Designation | Timestamp | Flags |
|---|---------|-----------|-------------|-----------|-------|
| 1 | 110-117 | T. Karthik Narayanan | Company Secretary | Digitally signed 2026.08.12 16:19:13 +05'30' | Timestamp is AFTER board meeting conclusion (15:50 Hrs) — no flag (expected order); gap ~29 min |
| 2 | 285-293 | Irmgard Velagapudi | Managing Director | Place Chennai, Date 12.08.2026 (no time-stamp; printed/scanned signature under "BY ORDER OF THE BOARD" on the financial results annexure) | — |
| 3 | 373-390 | KVNS Kishore | Partner, B. Purushottam & Co., M.No. 206734 | Place Chennai, Date 12 Aug 2026 (no time-stamp); UDIN 26206734DGDZKE9B4B | Standalone Limited Review Report signature |
| 4 | 487-502 | KVNS Kishore | Partner, B. Purushottam & Co., M.No. 206734 | Place Chennai, Date 12 Aug 2026 (no time-stamp); UDIN 26206734HQHINC5732 (OCR-garbled) | Consolidated Limited Review Report signature |

Signature blocks total: 4/4.

---

## 8. Annexure 1 — List of Entities Included in the Consolidated Statement (page 9, lines 511-519)

| # | Line | Name | Relationship | Flags |
|---|------|------|--------------|-------|
| 1 | 516 | K.C.P Sugar and Industries Corporation Limited | Holding Company | — |
| 2 | 517 | KCP Sugars Agricultural Farms Limited | Subsidiary | — |
| 3 | 518 | THE EIMCO-K.C.P Limited | Subsidiary | Leading digit OCR'd as "J." instead of "3" — MISSED by naive grep, recovered on manual sweep (see COUNT TEST). Note: this is the same EIMCO-KCP entity named as counterparty in Board Outcome agenda item 5 (the Rs.153.40 Cr supply contract) — related-party cross-reference |
| 4 | 519 | Quality Engineering | Step down subsidiary | This is the "1 step down subsidiary" referenced as unreviewed-by-principal-auditor in Consolidated Review Report para 7 (income Rs.28.93 Lakhs, net loss Rs.5.49 Lakhs) |

Entities total: 4/4. No prior-quarter entity list supplied for this run — ENTITY_CHANGE comparison N/A.

---

## FLAGS SUMMARY

- ZERO_STANDING (8 rows): P&L Exceptional Items (both books); P&L Current Tax (standalone only); P&L
  Reversal of Excess Provision (standalone only); P&L Discontinued Operations x3 rows (both books); P&L
  EPS(b) Discontinued (both books); P&L Equity Instruments Through OCI (standalone only); Segment
  Result f) Unallocated (both books).
- ARITHMETIC_CHECK / OCR_SUSPECT (segment tables): Segment Assets — Sugar standalone year-ended
  43896.65 (line 241); Segment Assets — Power & Fuel standalone year-ended 4436.47 (line 243); Segment
  Assets Total does not foot cleanly (line 247); Segment Liabilities — Power & Fuel consolidated
  year-ended 46.30 (line 252); Capital Employed Total consolidated shows truncated "4694133" (line 265).
  All flagged for A3 forensic-notes verification against the source PDF (not resolvable from OCR text
  alone).
- RELATED_PARTY_TRANSACTION: Board Outcome agenda item 5, EIMCO-KCP supply contract Rs.153.40 Cr with
  wholly owned subsidiary (line 97-104); cross-references Annexure 1 entity #3.
- Note 6 concentration: Other Income standalone line is ~93.5% fair-value gain on equity investments
  (line 283) — non-operating, flagged for A4 quality-of-earnings read.
- ENTITY_CHANGE / DROPPED_SLIDE: not applicable — no prior-quarter ledger supplied for comparison.
- MGMT_ABSENCE / REPEAT_QUESTION: not applicable — this is a results doctype, not a concall transcript.

---
Written by A2-enumerator. Ledger is the contract A3 and A4 must reconcile against 100%.
