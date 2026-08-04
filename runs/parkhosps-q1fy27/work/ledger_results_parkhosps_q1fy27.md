# LEDGER — Park Medi World Limited (PARKHOSPS) — Q1 FY27 — Doctype: results
Source: extract_results_parkhosps_q1fy27.txt (15 pages, 712 lines incl. header; unit Rs Millions, x0.1 to Cr)
Prior-quarter ledger: none (fresh coverage)

```
=== A2 COUNT TEST ===
category: notes             grep_count: 22   sweep_count: 22   match: yes
category: line_items        grep_count: 63   sweep_count: 63   match: yes
category: zero_standing     grep_count: 3    sweep_count: 3    match: yes
category: agenda_items      grep_count: 3    sweep_count: 3    match: yes
category: auditor_paras     grep_count: 12   sweep_count: 12   match: yes
category: entities           grep_count: 23   sweep_count: 23   match: yes
category: annexure_tables   grep_count: 10   sweep_count: 10   match: yes
category: signature_blocks  grep_count: 5    sweep_count: 5    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Reconciliation notes on method (non-interpretive, mechanical):
- `notes`: grep `^[0-9]+\.\s` restricted to the two "Notes to the..." sections (lines 209-278 standalone, 474-554 consolidated) gives 10+12=22, matching manual sweep exactly. A plain unrestricted grep of the whole file for `^[0-9]+\.\s` returns 33 because it also catches numbered auditor-report paragraphs (2,3,4,5 standalone; 1-7 consolidated) — those are counted separately under `auditor_paras`, below.
- `auditor_paras`: the standalone review report's first paragraph is printed as Roman numeral "I." not "1." (line 106), so a plain digit-only grep under-counts standalone paras to 4. A grep pattern matching `^(I|[0-9]+)\.\s` restricted to each report's line range (100-151 standalone, 285-369 consolidated) returns 5+7=12, matching manual sweep. This mismatch was a grep-pattern defect, not a sweep miss; the pattern was corrected before emitting per GATE A2.
- `line_items`: grep `[0-9]+\.[0-9]{2}` under-counts by 3 because 3 rows are all-dash in the periods where the pattern is applied ("Exceptional items" x2, "Income tax relating to previous years" x1 standalone). A pattern also matching label-line-with-terminal "- - - -" strings, restricted to the two P&L table ranges (164-196, 417-461), returns 27+36=63, matching manual sweep.
- `zero_standing`: of the 63 line items, 3 are dash/nil in ALL four period columns (see ZERO_STANDING table).

---

## 1. NOTES TO FINANCIAL RESULTS (numbered notes) — 22 total

### 1A. Standalone notes (10) — lines 211-275
| # | Line | First ~15 words | Flags |
|---|------|------------------|-------|
| 1 | 211 | "The unaudited standalone financial results have been prepared in accordance with the recognition and measurement..." | |
| 2 | 217 | "The unaudited standalone financial results ('the Statement) of Park Medi World Limited... reviewed by Audit committee Aug 3, 2026, unmodified opinion" | |
| 3 | 223 | "The Company has launched a 350 bedded advanced multi-super specialty hospital at Panchkula on April 10, 2026" | |
| 4 | 228 | "Umkal Healthcare Private Limited, the wholly owned subsidiary, has proposed expansion of existing 225-bedded Park Hospital Palam Vihar +100 beds, ~₹250mn, internal accruals" | |
| 5 | 233 | "Park Medicenters and Institutions Private Limited... incorporated wholly owned subsidiary 'Healplus Medical Services Private Limited', CIN U47721DC2026PTC471594, May 20, 2026, not commenced ops" | ENTITY_CHANGE (new step-down entity, not commenced ops, see §6) |
| 6 | 238 | "During the quarter ended June 30, 2026, the Company did not receive any investor complaint. No complaints pending" | |
| 7 | 245 | "The utilisation of the IPO proceeds is summarised below" [table, see §1C] | |
| 8 | 264 | "Subsequent event: acquired 80% of V3 Healthcare Private Limited on July 31, 2026, 'The Medicity Hospital-Rudrapur', 330 beds, ~₹1,770mn" | ENTITY_CHANGE (subsequent, post period-end) |
| 9 | 270 | "Previous period figures have been regrouped/reclassified wherever necessary... rounding off errors have been ignored" | |
| 10 | 273 | "The unaudited standalone financial results... are available on the Company's website... and BSE/NSE websites" | |

### 1B. Consolidated notes (12) — lines 476-551
| # | Line | First ~15 words | Flags |
|---|------|------------------|-------|
| 1 | 476 | "The unaudited Consolidated financial results have been prepared in accordance with the recognition and measurement principles" | |
| 2 | 481 | "The unaudited Consolidated financial results... reviewed by Audit committee Aug 3, 2026... unmodified opinion" | |
| 3 | 486 | "The Company has launched a 350 bedded advanced multi-super specialty hospital at Panchkula on April 10, 2026" | (duplicate content of standalone note 3, verbatim/near-verbatim) |
| 4 | 490 | "RGS Healthcare Limited, the step down subsidiary, has proposed expansion of Mohali unit from 350 to 500 beds, ~₹400mn" + Umkal Palam Vihar expansion repeated | (combines standalone note 4 content + new RGS Mohali item in one numbered note) |
| 5 | 497 | "Park Medicenters and Institutions Private Limited... incorporated 'Heal Plus Medical Services Private Limited'... May 20, 2026" | ENTITY_CHANGE; note spelling "Heal Plus" here vs "Healplus" in standalone note 5 (line 234) |
| 6 | 501 | "Aggarwal Hospital and Research Services Private Limited... divested entire 55% shareholding in Devina Derma Private Limited... ₹0.60 million, completed June 5, 2026" | ENTITY_CHANGE (exit) |
| 7 | 506 | "The Group's business activity primarily falls within a single reportable business segment namely 'Healthcare Service'..." (Ind AS 108 — one segment, one geography) | OCR_GAP (line 514: several words reconstructed from partially obscured scan overlay; meaning unambiguous per A1) |
| 8 | 519 | "The utilisation of the IPO proceeds is summarised below" [table, see §1C] | DISCLOSURE_INCONSISTENCY (table omits the "Total" sub-total row present in standalone table; see §1C) |
| 9 | 537 | "Subsequent event: acquired 80% of V3 Healthcare Private Limited... July 31, 2026... 330 beds, ~₹1,770mn" | ENTITY_CHANGE (subsequent) |
| 10 | 542 | "During the quarter ended June 30, 2026 the Company did not receive any investor complaint" | |
| 11 | 546 | "Previous period figures have been regrouped/reclassified wherever necessary... rounding off errors ignored" | |
| 12 | 549 | "The unaudited Consolidated financial results... available on the Company's website... BSE/NSE websites" | |

### 1C. IPO utilisation sub-tables inside notes (standalone note 7 / consolidated note 8)
| Table | Row | Line | Planned | Utilised to 30-Jun-26 | Pending | Flags |
|---|---|------|--------:|--------:|--------:|-------|
| Standalone | Repayment/prepayment of borrowings | 250 | 3,800.00 | 3,800.00 | - | ZERO_STANDING (pending col) |
| Standalone | Capex — new hospital, Park Medicity (NCR) Pvt Ltd | 252 | 605.00 | 195.19 | 409.81 | |
| Standalone | Capex — medical equipment (Co. + Blue Heavens + Ratangiri) | 255 | 274.59 | 36.08 | 238.51 | SPELLING_INCONSISTENCY: "Ratangiri" here |
| Standalone | Unidentified inorganic acquisitions & general corporate purposes | 256 | 2,453.18 | 2,453.18 | - | ZERO_STANDING (pending col) |
| Standalone | Total (subtotal) | 257 | 7,132.77 | 6,484.45 | 648.32 | |
| Standalone | Issue expenses towards IPO | 258 | 567.23 | 567.23 | - | ZERO_STANDING (pending col) |
| Standalone | Grand Total | 259 | 7,700.00 | 7,051.68 | 648.32 | |
| Consolidated | Repayment/prepayment of borrowings | 524 | 3,800.00 | 3,800.00 | - | ZERO_STANDING (pending col) |
| Consolidated | Capex — new hospital, Park Medicity (NCR) Pvt Ltd | 526 | 605.00 | 195.19 | 409.81 | |
| Consolidated | Capex — medical equipment (Co. + Blue Heavens + Ratnagiri) | 529 | 274.59 | 36.08 | 238.51 | SPELLING_INCONSISTENCY: "Ratnagiri" here (vs "Ratangiri" standalone note line 255 and entity list line 397) |
| Consolidated | Unidentified inorganic acquisitions & general corporate purposes | 530 | 2,453.18 | 2,453.18 | - | ZERO_STANDING (pending col) |
| Consolidated | **[no "Total" subtotal row present]** | — | — | — | — | DISCLOSURE_INCONSISTENCY: standalone table (line 257) has an intermediate "Total: 7,132.77 / 6,484.45 / 648.32" subtotal row before "Issue expenses"; consolidated table (lines 519-532) omits this row entirely and goes straight from the last object line to "Issue expenses" |
| Consolidated | Issue expenses towards IPO | 531 | 567.23 | 567.23 | - | ZERO_STANDING (pending col) |
| Consolidated | Grand Total | 532 | 7,700.00 | 7,051.68 | 648.32 | |

Both tables' Grand Total row ties out identically (7,700.00 / 7,051.68 / 648.32), consistent with the A1 header note that the two tables "agree" numerically — the structural row omission is a formatting difference, not a numeric one.

---

## 2. LINE ITEMS — FINANCIAL STATEMENTS — 63 total (27 standalone + 36 consolidated)
Columns ordered per filing: Q1 FY27 | Q4 FY26 | Q1 FY26 | FY26 (full year). Unit Rs Millions.

### 2A. Standalone P&L — lines 164-196 (27 line items)
| # | Line | Particular | Q1 FY27 | Q4 FY26 | Q1 FY26 | FY26 | Flags |
|---|------|-----------|--------:|--------:|--------:|-----:|-------|
| 1 | 165 | Revenue from operations | 335.32 | 274.34 | 229.69 | 1,289.65 | |
| 2 | 166 | Other income | 46.68 | 82.69 | 2.01 | 103.35 | |
| 3 | 167 | Total Income | 382.00 | 357.03 | 231.70 | 1,393.00 | |
| 4 | 169 | Cost of material/Service consumed | 54.19 | 34.58 | 31.27 | 157.62 | |
| 5 | 170 | Changes in inventories of stock | (0.71) | - | (0.02) | (3.97) | (dash only in Q4FY26 col, not all periods — not ZERO_STANDING) |
| 6 | 171 | Employee benefit expenses | 87.54 | 43.17 | 36.04 | 187.46 | |
| 7 | 172 | Professional and consultancy fees | 51.77 | 15.72 | 16.23 | 101.57 | |
| 8 | 173 | Finance costs | 8.60 | 24.20 | 32.98 | 127.55 | |
| 9 | 174 | Depreciation and amortisation expense | 33.81 | 10.10 | 11.61 | 45.09 | |
| 10 | 175 | Other expenses | 129.69 | 133.13 | 42.66 | 323.27 | |
| 11 | 176 | Total Expenses | 364.89 | 260.90 | 170.77 | 938.59 | |
| 12 | 177 | III Profit/(Loss) before exceptional items and tax (I-II) | 17.11 | 96.13 | 60.93 | 454.41 | |
| 13 | 178 | IV Exceptional items | - | - | - | - | **ZERO_STANDING** |
| 14 | 179 | V Profit/(Loss) before tax (III-IV) | 17.11 | 96.13 | 60.93 | 454.41 | |
| 15 | 181 | Current tax | 3.44 | 22.96 | 12.09 | 112.75 | |
| 16 | 182 | Deferred tax charge/(benefit) | 2.83 | (12.89) | (0.13) | (24.50) | |
| 17 | 183 | Income tax relating to previous years | - | - | - | - | **ZERO_STANDING** |
| 18 | 184 | Total tax expenses | 6.27 | 10.07 | 11.96 | 88.25 | |
| 19 | 185 | VII Profit/(Loss) after tax (V-VI) | 10.84 | 86.06 | 48.97 | 366.16 | |
| 20 | 188 | Remeasurement of employee defined benefit plans (OCI) | (0.98) | 1.34 | 0.50 | 2.00 | |
| 21 | 189 | Income tax relating to above (OCI) | 0.25 | (0.34) | (0.13) | (0.50) | |
| 22 | 190 | Total other comprehensive income/(loss) | (0.73) | 1.00 | 0.37 | 1.50 | |
| 23 | 191 | IX Total comprehensive income/(loss) (VII+VIII) | 10.11 | 87.06 | 49.34 | 367.66 | |
| 24 | 192 | Paid up Equity Share Capital (FV ₹2) | 863.86 | 863.86 | 768.80 | 863.86 | |
| 25 | 193 | Other Equity excluding Revaluation Reserve | (blank) | (blank) | (blank) | 7,736.41 | populated only in annual column per standard interim-reporting convention; quarterly cells blank rather than dash-printed — noted, not flagged ZERO_STANDING (not "-" in source) |
| 26 | 195 | EPS Basic (₹, not annualised) | 0.03 | 0.20 | 0.13 | 0.92 | |
| 27 | 196 | EPS Diluted (₹, not annualised) | 0.03 | 0.20 | 0.13 | 0.92 | |

### 2B. Consolidated P&L — lines 417-461 (36 line items)
| # | Line | Particular | Q1 FY27 | Q4 FY26 | Q1 FY26 | FY26 | Flags |
|---|------|-----------|--------:|--------:|--------:|-----:|-------|
| 1 | 418 | Revenue from operations | 4,757.09 | 4,604.13 | 3,988.45 | 16,793.56 | |
| 2 | 419 | Other income | 76.46 | 75.03 | 68.72 | 316.09 | |
| 3 | 420 | Total Income | 4,833.55 | 4,679.16 | 4,057.17 | 17,109.65 | |
| 4 | 422 | Cost of material/Service consumed | 771.24 | 784.34 | 699.39 | 2,950.61 | |
| 5 | 423 | Changes in inventories of stock | (8.67) | 11.91 | 0.80 | 7.45 | |
| 6 | 424 | Employee benefit expenses | 924.07 | 861.64 | 767.79 | 3,233.97 | |
| 7 | 425 | Professional and consultancy fees | 756.05 | 716.20 | 603.22 | 2,570.74 | |
| 8 | 426 | Finance costs | 98.10 | 139.75 | 151.33 | 588.85 | |
| 9 | 427 | Depreciation and amortisation expense | 188.40 | 175.06 | 147.71 | 624.62 | |
| 10 | 428 | Other expenses | 1,053.52 | 956.35 | 867.94 | 3,587.57 | |
| 11 | 429 | Total Expenses | 3,782.71 | 3,645.26 | 3,238.18 | 13,563.81 | |
| 12 | 430 | III Profit/(Loss) before exceptional items and tax | 1,050.84 | 1,033.90 | 818.99 | 3,545.84 | |
| 13 | 431 | IV Exceptional items | - | - | - | - | **ZERO_STANDING** |
| 14 | 432 | V Profit/(Loss) before tax (III-IV) | 1,050.84 | 1,033.90 | 818.99 | 3,545.84 | |
| 15 | 434 | Current tax | 260.98 | 197.42 | 167.48 | 822.45 | |
| 16 | 435 | Deferred tax charge/(benefit) | (93.40) | 68.25 | (3.55) | (14.51) | |
| 17 | 436 | Income tax relating to previous years | (2.67) | 0.45 | - | 2.33 | non-zero in 3/4 periods — NOT ZERO_STANDING (differs from standalone equivalent, which is all-dash — see flag below) |
| 18 | 437 | Total tax expenses | 164.91 | 266.12 | 163.93 | 810.27 | |
| 19 | 438 | VII Profit/(Loss) after tax (V-VI) | 885.93 | 767.78 | 655.06 | 2,735.57 | |
| 20 | 441 | Remeasurement of employee defined benefit plans (OCI) | (7.76) | 4.15 | (1.04) | 12.88 | |
| 21 | 442 | Income tax relating to above (OCI) | 1.95 | (0.30) | 0.26 | (3.24) | |
| 22 | 443 | Total other comprehensive income/(loss) | (5.81) | 3.85 | (0.78) | 9.64 | |
| 23 | 444 | IX Total comprehensive income/(loss) (VII+VIII) | 880.12 | 771.63 | 654.28 | 2,745.21 | |
| 24 | 446 | X Profit/(Loss) attrib. to: Owners of the parent | 825.07 | 708.64 | 579.83 | 2,581.20 | |
| 25 | 447 | X Profit/(Loss) attrib. to: Non-controlling Interest | 60.86 | 59.14 | 75.23 | 154.37 | |
| 26 | 448 | X Total | 885.93 | 767.78 | 655.06 | 2,735.57 | ties to line 19 (VII total) |
| 27 | 450 | XI OCI attrib. to: Owners of the parent | (5.69) | 3.61 | (0.80) | 9.17 | |
| 28 | 451 | XI OCI attrib. to: Non-controlling Interest | (0.12) | 0.24 | 0.02 | 0.47 | |
| 29 | 452 | XI Total | (5.81) | 3.85 | (0.78) | 9.64 | ties to line 22 (OCI total) |
| 30 | 454 | XII TCI attrib. to: Owners of the parent | 819.38 | 712.25 | 579.04 | 2,590.37 | |
| 31 | 455 | XII TCI attrib. to: Non-controlling Interest | 60.74 | 59.38 | 75.24 | 154.84 | |
| 32 | 456 | XII Total | 880.12 | 771.63 | 654.28 | 2,745.21 | ties to line 23 (IX total) |
| 33 | 457 | Paid up Equity Share Capital (FV ₹2) | 863.86 | 863.86 | 768.80 | 863.86 | |
| 34 | 458 | Other Equity excluding Revaluation Reserve | (blank) | (blank) | (blank) | 19,236.51 | annual-column only, per note on standalone equivalent above |
| 35 | 460 | EPS Basic (₹, not annualised) | 2.05 | 1.78 | 1.70 | 6.87 | |
| 36 | 461 | EPS Diluted (₹, not annualised) | 2.05 | 1.78 | 1.70 | 6.87 | |

**ZERO_STANDING flag detail:** "Income tax relating to previous years" is dash/nil in ALL 4 periods in the standalone statement (row 17, §2A) but is populated (non-zero) in 3 of 4 periods in the consolidated statement (row 17, §2B) — same line label, different zero-standing status between the two statements. Recorded, not interpreted.

---

## 3. ZERO_STANDING LINE ITEMS — 3 total (subset of §2, cross-referenced)
| Line | Statement | Particular | All 4 periods |
|------|-----------|-----------|----------------|
| 178 | Standalone | IV Exceptional items | - / - / - / - |
| 183 | Standalone | Income tax relating to previous years | - / - / - / - |
| 431 | Consolidated | IV Exceptional items | - / - / - / - |

Note: consolidated "Income tax relating to previous years" (line 436) is NOT zero-standing (see §2B row 17) — excluded from this table by design, not a miss.

---

## 4. BOARD OUTCOME — AGENDA ITEMS — 3 total (lines 55-88)
| # | Line | Item | Details | Flags |
|---|------|------|---------|-------|
| 1 | 58-60 | Financial results | Unaudited Standalone and Consolidated Financial Results for quarter ended June 30, 2026; Limited Review Report enclosed as Annexure-I | |
| 2 | 62-66 | Acquisition | Acquisition of "Mehar Hospital-Zirakpur", owned/operated by Mehar Mediserve LLP; details under SEBI Master Circular HO/49/14/14(7)2025-CFD-POD2/I/3762/2026 dated Jan 30, 2026, plus press release, enclosed as Annexure-II | |
| 3 | 68-72 | IPO objects variation | Variation in objects of IPO Proceeds per Prospectus dated Dec 12, 2025, subject to Shareholder approval by Postal Ballot; notice + explanatory statement to follow in due course | |

### 4A. Supplementary context rows (not counted toward agenda_items; recorded per operating rule #3)
| Line | Item | Detail | Flags |
|------|------|--------|-------|
| 53 | Prior intimation reference | "In continuation of our intimation dated July 29, 2026" — prior Reg 29 notice of board meeting date | |
| 74-75 | Board meeting timing | Commenced 08:00 A.M. IST, concluded 09:20 A.M. IST — duration 1 hour 20 minutes | |
| 76 | Availability | Results also to be available on www.parkhospital.in | |

---

## 5. AUDITOR REVIEW REPORTS — PARAGRAPH-BY-PARAGRAPH — 12 total (5 standalone + 7 consolidated)

### 5A. Standalone Independent Auditor's Review Report — lines 100-151 (5 paragraphs)
| Para | Line | Content | Flags |
|------|------|---------|-------|
| I. (printed as Roman numeral, not "1.") | 106 | Scope: reviewed accompanying Statement of Unaudited Standalone Financial Results for quarter ended June 30, 2026, per Reg 33 | OCR/typesetting: para 1 rendered "I." not "1." — plain digit-grep under-counts; corrected pattern used, see COUNT TEST notes |
| 2 | 111 | Management responsibility: Ind AS 34 preparation, Board approval, auditor's responsibility to express conclusion | |
| 3 | 117 | Basis of review: SRE 2410, ICAI; review is substantially less in scope than audit; no audit opinion expressed | |
| 4 | 126 | **Conclusion (opinion)**: "nothing has come to our attention that causes us to believe... has not disclosed the information required... or that it contains any material misstatement" — **Unmodified/Unqualified conclusion** | |
| 5(a)(b) | 133 | (a) Q4 FY26 figures are balancing figures (audited FY26 less reviewed 9M FY26, not itself audited); (b) Q1 FY26 corresponding-quarter figures as previously issued, not subject to limited review | Functions as an Emphasis-of-Matter-type paragraph; not explicitly headed "Emphasis of Matter" in the printed text |
| — Going Concern | n/a | No Going Concern paragraph or language present anywhere in this report | Recorded as NOT FOUND, not silently omitted |
| — Other Matters | n/a | No separate "Other Matters" heading in standalone report | Recorded as NOT FOUND |
| Signature | 139-150 | For Agiwal & Associates, Chartered Accountants, FRN 000181N; P.C. Agiwal, Partner; **Membership Number: [blank — not printed]**; Place: Gurugram; Date: Aug 3, 2026; UDIN: 26080475SIBZRX3355 | Membership number field blank in this report vs "080475" printed in the consolidated report for the same partner (line 365) — flag as field-completeness gap |

### 5B. Consolidated Independent Auditor's Review Report — lines 284-368 (7 paragraphs)
| Para | Line | Content | Flags |
|------|------|---------|-------|
| 1 | 291 | Scope: reviewed accompanying Statement of Unaudited Consolidated Financial Results (Parent + subsidiaries = "Group") for quarter ended June 30, 2026 | |
| 2 | 297 | Management responsibility: Ind AS 34, Board approval, auditor's responsibility to express conclusion | |
| 3 | 305 | Basis of review: SRE 2410, ICAI; also performed procedures per SEBI Reg 33(8) circular; review less in scope than audit, no audit opinion | |
| 4 | 318 | **Entity list reviewed**: "Statement includes the results of the subsidiaries and associates listed in Annexure-I" (23 entities, see §6) | |
| 5(a)(b) | 320 | (a) Q4 FY26 balancing figures (same construct as standalone 5(a)); (b) Q1 FY26 corresponding-quarter figures not subject to limited review | Emphasis-of-Matter-type; not explicitly headed as such |
| 6 | 328 | **Conclusion (opinion)**: "nothing has come to our attention... has not disclosed the information required... or that it contains any material misstatement", based also on other auditors' reports per para 7 — **Unmodified/Unqualified conclusion** | |
| 7 | 342-356 | **Other-Matter-type paragraph (reliance on other auditors)**: interim results of **19 subsidiaries** reviewed by other auditors — unaudited, total revenue Rs.3,749.42mn, PAT Rs.717.68mn, TCI Rs.714.11mn (pre-consolidation-adjustment), reports furnished to principal auditor by Parent's management, conclusion based solely on those other auditors' reports; interim results of **2 subsidiaries** reviewed by the Management of the Company (not by any auditor) — total revenue Rs.163.15mn, PAT Rs.26.00mn, TCI Rs.26.00mn; conclusion "not modified" in respect of reliance on other auditors | Not explicitly headed "Other Matter" in the printed text, but functions as one; identifies which entities are unaudited (all 19+2=21) and which are management-furnished only (the 2) |
| — Going Concern | n/a | No Going Concern paragraph or language present anywhere in this report | Recorded as NOT FOUND |
| Signature | 358-368 | For Agiwal & Associates, Chartered Accountants, FRN 000181N; P.C. Agiwal, Partner; Membership Number: 080475; Place: Gurugram; Date: Aug 3, 2026; UDIN: 26080475JKIYOL3362 | UDIN partially obscured per A1 OCR note (line 370): digits after "2608047" and before "JKIYOL3362" uncertain — transcribed best-legible reading, flag OCR_GAP |

**Reconciliation check (mechanical, not interpretive):** 23 entities in Annexure-I = 1 Parent + 22 subsidiaries/step-down subsidiaries. Para 7 discloses 19 + 2 = 21 subsidiaries with stated review status. 22 − 21 = 1, which reconciles arithmetically to Devina Derma Private Limited (entity #20, footnoted as ceasing to be a subsidiary June 5, 2026 — divested mid-quarter, stub-period consolidation, not itemized in the 19/2 review-status breakdown). Flagged for A3/A4 to confirm interpretively.

---

## 6. CONSOLIDATION ENTITY LIST (Annexure-I, page 8) — 23 total — lines 377-399
| # | Line | Entity | Country | Relationship | Flags |
|---|------|--------|---------|--------------|-------|
| 1 | 377 | Park Medi World Limited | India | Parent | |
| 2 | 378 | Park Medicentres & Institutions Private Limited | India | Subsidiary | |
| 3 | 379 | Aggarwal Hospital & Research Services Private Limited | India | Subsidiary | |
| 4 | 380 | Park Medicity India Private Limited | India | Subsidiary | |
| 5 | 381 | Park Medical Centre Private Limited | India | Subsidiary | |
| 6 | 382 | Park Medicity (North) Private Limited | India | Subsidiary | |
| 7 | 383 | Park Medicity (World) Private Limited | India | Subsidiary | |
| 8 | 384 | Park Medicity (NCR) Private Limited | India | Subsidiary | |
| 9 | 385 | Park Imperial Medi World Private Limited | India | Subsidiary | |
| 10 | 386 | Park Elite Medi World Private Limited | India | Subsidiary | |
| 11 | 387 | Blue Heavens Healthcare Private Limited | India | Subsidiary | |
| 12 | 388 | Kailash Super Speciality Hospital Private Limited | India | Subsidiary | |
| 13 | 389 | Umkal Heathcare Private Limited [sic, "Heathcare"] | India | Subsidiary | spelling as printed |
| 14 | 390 | SVPD Heathcare Private Limited [sic, "Heathcare"] | India | Subsidiary | spelling as printed |
| 15 | 391 | K P S Wellness Private Limited | India | Subsidiary | |
| 16 | 392 | Mahip Hospitals Private Limited | India | Step-down subsidiary | |
| 17 | 393 | DMR Hospitals Private Limited | India | Step-down subsidiary | |
| 18 | 394 | Park Medicity (Haryana) Private Limited | India | Step-down subsidiary | |
| 19 | 395 | RGS Helathcare Limited [sic, "Helathcare"] | India | Step-down subsidiary | spelling as printed |
| 20 | 396-401 | Devina Derma Private Limited* | India | Step-down subsidiary | **ENTITY_CHANGE**: footnote (line 401) — "ceases to be subsidiary with effect from June 5th, 2026 due to divestment"; corroborated by consolidated note 6 (line 501, §1B) |
| 21 | 397 | Ratangiri Innovations Private Limited | India | Step-down subsidiary | SPELLING_INCONSISTENCY — see §1C ("Ratangiri" here vs "Ratnagiri" in consolidated IPO table line 529) |
| 22 | 398 | Narsingh Hospital & Heart Institute Private Limited | India | Step-down subsidiary | |
| 23 | 399 | Durha Vitrak Private Limited | India | Step-down subsidiary | |

### 6A. Entities referenced elsewhere in the filing but NOT in this 23-row list
| Entity | Where referenced | Status as of June 30, 2026 | Flags |
|--------|-------------------|------------------------------|-------|
| Healplus Medical Services Private Limited (CIN U47721DC2026PTC471594) [also spelled "Heal Plus" in consolidated note 5, line 497] | Standalone note 5 (line 233), Consolidated note 5 (line 497) | Incorporated May 20, 2026 as wholly owned subsidiary of Park Medicenters and Institutions Private Limited (itself entity #2 above) — i.e., would be a step-down subsidiary as of quarter-end, but does not appear as a row in the 23-entity Annexure-I list | **ENTITY_CHANGE** — new entity, absent from the entity-list table despite being legally incorporated before period end; note states "no financial impact on the consolidated results" as the stated reason for no financial disclosure, but does not explain the list-omission; flagged for A3/A4 |
| V3 Healthcare Private Limited ("The Medicity Hospital - Rudrapur") | Standalone note 8 (line 264), Consolidated note 9 (line 537) | Acquired (80%) July 31, 2026 — **after** period end (subsequent event) | **ENTITY_CHANGE** (forward-looking) — correctly absent from the June 30, 2026 entity list since acquisition post-dates the quarter |
| Mehar Mediserve LLP / "Mehar Hospital-Zirakpur" | Board Outcome item 2 (line 62), Annexure-II | Acquisition announced same day as results (Aug 3, 2026), target entity, not yet consolidated | Not an entity-list change for this quarter; tracked via Annexure-II (§7) |

---

## 7. ANNEXURES AND THEIR TABLES — 10 total (7 under Annexure-I, 3 under Annexure-II)

### 7A. Annexure-I (Financial Results + Limited Review Report) — pages 2-11
| # | Pages/Lines | Component | Flags |
|---|-------------|-----------|-------|
| 1 | p.2, lines 100-151 | Standalone Independent Auditor's Review Report | see §5A |
| 2 | p.3 (OCR), lines 159-197 | Statement of Unaudited Standalone Financial Results (P&L table) | see §2A |
| 3 | p.4-5 (OCR), lines 209-278 | Notes to standalone financial results (incl. IPO utilisation sub-table) | see §1A, §1C |
| 4 | p.6-7 (OCR), lines 284-368 | Consolidated Independent Auditor's Review Report | see §5B |
| 5 | p.8 (OCR), lines 372-403 | List of entities in unaudited consolidated financial results (itself headed "Annexure-I") | **DUPLICATE_ANNEXURE_LABEL**: this sub-table is headed "Annexure-I" (line 373) — same label as the outer, filing-level Annexure-I (line 91) that encloses the entire Results + Review Report package per the Board Outcome letter (line 60). Naming collision noted, not necessarily an error. |
| 6 | p.9 (OCR), lines 406-462 | Statement of Unaudited Consolidated Financial Results (P&L table) | see §2B |
| 7 | p.10-11 (OCR), lines 473-553 | Notes to consolidated financial results (incl. IPO utilisation sub-table) | see §1B, §1C |

### 7B. Annexure-II (Mehar Hospital-Zirakpur acquisition) — pages 12-15
| # | Pages/Lines | Component | Flags |
|---|-------------|-----------|-------|
| 8 | p.12-13, lines 556-601 | Acquisition disclosure table per SEBI Master Circular (10 rows, Sr. no. 1-10) — see detail table below | |
| 9 | p.13, lines 607-611 | Turnover — last 3 years table (FY2025-26: Rs.19.10 Cr; FY2024-25: Rs.18.87 Cr; FY2023-24: Rs.17.52 Cr) | ties to Sr.no.1 turnover figure (line 567-568) |
| 10 | p.14-15, lines 613-689 | Press release ("Deepening Our Presence in Punjab") — see §8 | |

### 7C. Annexure-II acquisition disclosure table detail — 10 rows, lines 564-596
| Sr. no. | Line | Particular | Detail |
|---|------|-----------|--------|
| 1 | 565 | Target entity name/size/turnover | Mehar Mediserve LLP, LLPIN AAH-6659; FY25-26 turnover Rs.19.10 Cr (unaudited) |
| 2 | 569 | Related party transaction? | Not a related party transaction |
| 3 | 575 | Industry | Healthcare / Hospital |
| 4 | 577 | Objects/impact of acquisition | Consistent with growth strategy — operational synergies, economies of scale |
| 5 | 582 | Governmental/regulatory approvals | Not Applicable |
| 6 | 584 | Indicative completion timeline | December 03, 2026 |
| 7 | 586 | Consideration type | Cash, acquiring 100% stake of Target Entity |
| 8 | 588 | Cost of acquisition | INR 107 Crores approx. |
| 9 | 590 | % shareholding/control acquired | 100% on date of signing revised Partnership deed |
| 10 | 592-601 | Background of entity acquired | Incorporated Oct 10, 2016; operations in Zirakpur, Punjab; owns Mehar Hospital, Singhpura Road, opp. Grandeur Marriage Place, Zirakpur-140603; 150+ bed multi-super speciality institution |

---

## 8. PRESS RELEASE (pages 14-15, lines 613-689) — structural sweep
| Line(s) | Section | Content type | Flags |
|---------|---------|--------------|-------|
| 614 | Headline | "Deepening Our Presence in Punjab - Strengthening the Tricity Cluster" | |
| 615-619 | Lead paragraph | Announces definitive agreement, INR 107 Cr all-cash, commissioning under Park brand expected Nov 2026 | consistent with Annexure-II Sr.no.6 (Dec 3, 2026 completion) vs press release "commissioned... in November 2026" — completion vs commissioning dates differ, both stated; not necessarily inconsistent (signing/completion vs commissioning are distinct milestones) but recorded for A3/A4 |
| 621-624 | "The Asset" | 150+ bed description, Tricity catchment | duplicates Annexure-II Sr.no.10 content verbatim in part |
| 625-630 | Strategy rationale | Synergies, economies of scale, "earnings-accretive" characterization | "earnings-accretive" is a forward-looking characterization made by the company, not an audited/reviewed figure |
| 635-643 | "Why Punjab" | Tricity geography, cluster strategy, references existing facilities at Mohali, Panchkula, Patiala, Bathinda | |
| 646-655 | "A Year of Step-Change Growth" | Enumerates CY2026 acquisitions/commissionings: Bathinda (250 beds, O&M since Jul 2025), Agra (360 beds), Panchkula (350 beds, greenfield), Rudrapur (330 beds), plus pending Zirakpur (150 beds), Narela Delhi (200 beds), Palam Vihar/Park Platinum extension (100 beds); "~1,500 beds... 46% capacity addition over closing bed count of ~3,250 beds in December 2025" | numbers spoken in a promotional/press context, not statement-line figures — flagged for A3/A4 cross-check against filing-note bed counts (Panchkula 350 beds per standalone/consolidated note 3; Palam Vihar +100 beds per note 4; Rudrapur 330 beds per note 8/9; Zirakpur 150+ beds per Annexure-II) |
| 657-666 | Management quote | Dr. Ankit Gupta, Managing Director — quoted commentary on Punjab strategy and the "~1,500 beds... 46% expansion" figure repeated | named individual + designation, not a signature block (no timestamp) — distinct from §9 signature blocks |
| 668-674 | "About Park Group" | 17 hospitals, ~4,300 beds "as on date"; integrating 3 additional hospitals + expanding 3 existing units; ~1,500 beds pipeline; total capacity target ~5,800 beds by March 2028 | |
| 676-686 | Footprint/services description | 15 key cities listed; service line list; expanding into Zirakpur, Gorakhpur, Rohtak | |
| 689 | Contact footer | investor.relations@parkhospital.in | |

---

## 9. DIGITAL SIGNATURE BLOCKS — 5 named/legible total (plus 9 illegible seal/stamp-only graphic markers, listed separately)

### 9A. Named signatory blocks (signatory / designation / timestamp)
| # | Line(s) | Document | Signatory | Designation | Timestamp | Flags |
|---|---------|----------|-----------|-------------|-----------|-------|
| 1 | 82-87 | Board Outcome letter | Abhishek Kapoor | Company Secretary & Compliance Officer | Digitally signed 2026.08.03 09:24:02 +05'30' | Signature is 4 minutes **after** stated board meeting conclusion (09:20 A.M., line 74-75) — not before, so the "signature before meeting concluded" tripwire does NOT trigger; recorded explicitly, no flag |
| 2 | 139-150 | Standalone Auditor's Review Report | P.C. Agiwal, Partner, Agiwal & Associates (FRN 000181N) | Partner | Place: Gurugram, Date: Aug 3, 2026 | Membership Number field blank (line 147) — see §5A flag; UDIN 26080475SIBZRX3355 |
| 3 | 199-206 | Standalone Financial Results (board sign-off) | Dr. Sanjay Sharma | Chief Executive Officer & Whole Time Director, DIN 01813328 | Place: Gurugram, Date: Aug 3, 2026 | seal/stamp graphic overlapping printed text noted illegible per A1 (line 199) |
| 4 | 358-368 | Consolidated Auditor's Review Report | P.C. Agiwal, Partner, Agiwal & Associates (FRN 000181N) | Partner | Place: Gurugram, Date: Aug 3, 2026 | Membership Number: 080475 (present here, blank in #2 above — same partner, same date, inconsistent field completion between the two reports); UDIN 26080475JKIYOL3362 partially obscured (OCR_GAP, line 370) |
| 5 | 464-471 | Consolidated Financial Results (board sign-off) | Dr. Sanjay Sharma | Chief Executive Officer & Whole Time Director, DIN 01813328 | Place: Gurugram, Date: Aug 3, 2026 | seal/stamp graphic overlapping printed text noted illegible per A1 (line 464) |

### 9B. Illegible seal/stamp graphic markers (no legible signatory/designation/timestamp beyond firm name) — 9 occurrences, not counted in §9A
| Line | Context |
|------|---------|
| 199 | Standalone financial results, board signature block area |
| 242 | End of standalone notes page 4 (auditor stamp: Agiwal & Associates, FRN 000181N) |
| 277 | End of standalone notes page 5 (auditor stamp) |
| 334 | End of consolidated review report page 6 (auditor stamp) |
| 362 | Consolidated review report signature area (unlabelled stamp) |
| 403 | End of Annexure-I entity list page 8 (auditor stamp) |
| 464 | Consolidated financial results, board signature block area |
| 516 | End of consolidated notes page 10 (auditor stamp) |
| 553 | End of consolidated notes page 11 (auditor stamp) |

Flag OCR_GAP applies to all 9 — genuine graphic elements the A1 extraction correctly declined to guess at, per its own methodology note (lines 19, 31-32).

---

## 10. CROSS-CUTTING FLAGS SUMMARY
| Flag | Count | Where |
|------|-------|-------|
| ZERO_STANDING | 3 | §2A row 13, §2A row 17, §2B row 13 (Exceptional items x2, standalone Income tax relating to previous years x1) |
| ENTITY_CHANGE | 4 instances | Devina Derma (exit, §6 row 20); Healplus/Heal Plus Medical Services (new, absent from list, §6A); V3 Healthcare (subsequent acquisition, §6A); Mehar Mediserve LLP target (pending acquisition, §7B) |
| SPELLING_INCONSISTENCY | 2 instances | "Ratangiri" (§1C standalone, §6 row 21) vs "Ratnagiri" (§1C consolidated); "Healplus" (§1A note 5) vs "Heal Plus" (§1B note 5) |
| DISCLOSURE_INCONSISTENCY | 1 | Consolidated IPO utilisation table omits "Total" subtotal row present in standalone equivalent (§1C) |
| DUPLICATE_ANNEXURE_LABEL | 1 | Entity list (p.8) headed "Annexure-I", nested inside filing-level "Annexure-I" (§7A row 5) |
| OCR_GAP | 12 instances | Consolidated UDIN partially obscured (§5B); segment-reporting note 7 words reconstructed (§1B note 7); 9 illegible seal/stamp graphics (§9B); standalone Membership Number blank (§5A/§9A #2) |
| — Going Concern | not present | Confirmed absent from both auditor reports (§5A, §5B) — recorded as NOT FOUND per operating rule, not silently omitted |
