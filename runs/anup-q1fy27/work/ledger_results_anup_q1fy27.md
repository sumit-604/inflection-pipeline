# A2 ENUMERATION LEDGER — The Anup Engineering Limited (ANUP) — Q1 FY27 — Results Filing

Source: `/home/user/inflection-pipeline/runs/anup-q1fy27/work/extract_results_anup_q1fy27.txt`
Prior-quarter ledger: none available — no ENTITY_CHANGE / DROPPED_SLIDE diff possible this run.
Unit convention: Lakhs, as printed (conversion factor to Cr = x0.01, per A1 header). Values below are enumerated AS PRINTED; no conversion performed.

```
=== A2 COUNT TEST ===
category: notes           grep_count: 13   sweep_count: 13   match: yes
category: line_items      grep_count: 71   sweep_count: 71   match: yes
category: agenda_items    grep_count: 1    sweep_count: 1    match: yes
category: auditor_paras   grep_count: 11   sweep_count: 11   match: yes
category: entities        grep_count: 2    sweep_count: 2    match: yes
category: signatures      grep_count: 5    sweep_count: 5    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Method notes:
- notes: grep `^\s*[0-9]+\s` restricted to standalone notes block (L227-256) = 6, consolidated notes block (L436-471) = 7. Manual sweep for unnumbered notes / asterisk / dagger / "Note:" prefixes across the whole 496-line extract returned zero hits — no unnumbered notes exist in this filing.
- line_items: grep `[0-9]+[.,][0-9]{2}` (data rows) + category-header rows (Income/Expenses/Tax Expense/OCI/EPS, which carry Sr. Nos but no numeric value of their own) within each table's line range. Standalone P&L table (L157-200) = 28 data rows + 5 header rows = 33. Consolidated P&L table (L365-408) = 28 data rows + 5 header rows = 33. Note 6 "key numbers of standalone results" sub-table inside the consolidated notes (L457-465) = 5 data rows (the grep hit of 6 on this range includes the column-date header line "30.06.2026 31.03.2026 ..." at L460, which is not a data row — corrected to 5 by manual sweep, reconciled).
- agenda_items: the Board Outcome letter (L19-61) approves a single agenda item — the standalone and consolidated Q1 FY27 results — with no other resolutions (no AGM notice, dividend, director appointment/resignation, auditor change, scrutinizer appointment, ESOP grant, or capital-raising enabling resolution present in this filing).
- auditor_paras: grep `^\s*[0-9]+\.` within each auditor report's paragraph range. Standalone report (L88-138) = 5 numbered paras. Consolidated report (L295-350) = 6 numbered paras.
- entities: consolidated auditor report para 4 (L321-324) lists 2 entities.
- signatures: grep anchors on `Partner|Managing Director|Company Secretary|Digitally signed` = 5 distinct signature blocks.

---

## 1. BOARD OUTCOME LETTER — AGENDA ITEMS

| # | Agenda item | Line | Detail | Flags |
|---|---|---|---|---|
| 1 | Approval of Unaudited Standalone and Consolidated Financial Results for quarter ended 30 June 2026, along with Auditors' reports thereon | 37-41 | Sole agenda item disclosed in the covering letter; Reg 30 & 33 SEBI LODR cited (L34-35) | — |

No further agenda items present: no AR approval, no AGM notice/record date, no dividend, no director appointment/resignation, no auditor change, no scrutinizer appointment, no ESOP grant resolution, no capital-raising enabling resolution appear anywhere in the 496-line extract (confirmed by full-document read).

### Board meeting timing
| Item | Line | Value |
|---|---|---|
| Meeting commenced | 43 | 10:30 A.M. |
| Meeting concluded | 43-44 | 11:40 A.M. |
| Duration | derived | 1 hour 10 minutes |

---

## 2. DIGITAL SIGNATURE / SIGNATORY BLOCKS (all 5)

| # | Block | Lines | Signatory | Designation | Timestamp | Flags |
|---|---|---|---|---|---|---|
| 1 | Board Outcome letter signature | 51-59 | Lay Desai (Membership No. A57117) | Company Secretary | Digitally signed; Date: 2026.08.06 11:49:21 +05'30' | Signed AFTER meeting conclusion (11:40 A.M. < 11:49 A.M.) — timing compliant, no flag |
| 2 | Standalone auditor's review report signature | 125-138 | CA Chokshi Shreyas B. (Membership No. 100892); Firm Regn No. 110417W | Partner, Sorab S. Engineer & Co. | Ahmedabad, August 06, 2026 (date only; time-of-day NOT FOUND — OCR of stamp garbled at L127-135, UDIN string illegible: ".2, 100 1t°12.~'IU<'.nf''/ S 'tl. l.") | — |
| 3 | Standalone notes closing dual signature ("As per our report of even date") | 259-271 | CA Chokshi Shreyas B. (Membership No. 100892) AND Reginaldo Dsouza (DIN 08590850) | Partner, Sorab S. Engineer & Co. / Managing Director, The Anup Engineering Ltd. | Both: Ahmedabad, August 06, 2026 (date only; time-of-day NOT FOUND) | — |
| 4 | Consolidated auditor's review report signature | 338-350 | CA Chokshi Shreyas B. (Membership No. 100892); Firm Regn No. 110417W (illegible at L340, confirmed clear at L480) | Partner, Sorab S. Engineer & Co. | Ahmedabad, August 06, 2026 (date only; time-of-day NOT FOUND; UDIN string illegible: "2 t 1oo gc'{1. l'Y\KTLvfV-1 -,") | — |
| 5 | Consolidated notes closing dual signature ("As per our report of even date") | 472-488 | CA Chokshi Shreyas B. (Membership No. 100892) AND Reginaldo Dsouza (DIN 08590850) | Partner, Sorab S. Engineer & Co. / Managing Director, The Anup Engineering Ltd. | Both: Ahmedabad, August 06, 2026 (date only; time-of-day NOT FOUND) | — |

Note: only block 1 (the covering letter) carries a full digital-signature timestamp with time-of-day, extracted directly from the source's "Digitally signed by" certificate block. Blocks 2-5 are scanned/wet-signature blocks with place + date only as printed; no time-of-day is present in the source text (OCR-legible portions), so time-of-day is recorded NOT FOUND rather than estimated.

---

## 3. AUDITOR REPORTS — PARAGRAPH-BY-PARAGRAPH (11 paragraphs total)

### 3a. Standalone — "Independent Auditor's Review Report on Review of Interim Standalone Financial Results" (L88-143), 5 paragraphs

| Para | Line | Content (summary) | Flags |
|---|---|---|---|
| 1 | 93-96 | Scope: reviewed Statement of Unaudited Standalone Financial Results for quarter ended 30 June 2026, per Reg 33 SEBI LODR | — |
| 2 | 98-103 | Management responsibility; prepared per Ind AS 34; auditor's responsibility is to express a review conclusion | — |
| 3 | 105-111 | Review conducted per SRE 2410; moderate assurance only, less than an audit; no audit opinion expressed | — |
| 4 | 113-118 | Conclusion: unmodified — "nothing has come to our attention" that the Statement is not prepared per Reg 33 or contains material misstatement | Opinion type: UNMODIFIED |
| 5 | 120-122 | Explanatory: Q4 FY26 (quarter ended 31 Mar 2026) figures are the balancing figure between FY26 audited full-year figures and published unaudited 9M FY26 figures | — |

Report signature block: CA Chokshi Shreyas B., Partner, Sorab S. Engineer & Co. (Firm Regn No. 110417W), Membership No. 100892, UDIN illegible (L135), Ahmedabad, August 06, 2026 (L125-138). Entities reviewed: standalone only — The Anup Engineering Limited (parent, single entity, no subsidiaries in scope). No unaudited/management-furnished component entities applicable to the standalone statement.

### 3b. Consolidated — "Independent Auditor's Review Report on Review of Interim Consolidated Financial Results" (L295-350), 6 paragraphs

| Para | Line | Content (summary) | Flags |
|---|---|---|---|
| 1 | 300-304 | Scope: reviewed Statement of Unaudited Consolidated Financial Results of Parent and its subsidiary ("the Group") for quarter ended 30 June 2026, per Reg 33 SEBI LODR | — |
| 2 | 306-311 | Management responsibility (Parent's Management); prepared per Ind AS 34; auditor's responsibility to express a conclusion | — |
| 3 | 313-319 | Review conducted per SRE 2410; moderate assurance, less than audit; no audit opinion expressed | — |
| 4 | 321-324 | Entity list reviewed (see Section 4 below) | Entities enumerated |
| 5 | 326-331 | Conclusion: unmodified — "nothing has come to our attention" that the Statement is not prepared per Reg 33 or contains material misstatement | Opinion type: UNMODIFIED |
| 6 | 333-335 | Explanatory: Q4 FY26 consolidated figures are the balancing figure between FY26 audited full-year figures and published unaudited 9M FY26 figures | — |

Report signature block: CA Chokshi Shreyas B., Partner, Sorab S. Engineer & Co., Membership No. 100892, UDIN illegible (L346), Ahmedabad, August 06, 2026 (L338-350). Same partner and same firm signs both standalone and consolidated reports. No paragraph anywhere in either report states that the subsidiary's figures are unaudited or management-furnished / management-certified — that qualifier is NOT FOUND in this filing (worth flagging to A3/A4 as an interpretive gap, not enumerated here as a disclosed item since it is absent).

---

## 4. CONSOLIDATION ENTITY LIST (2 entities)

| # | Entity | Relationship | Line | Flags |
|---|---|---|---|---|
| 1 | The Anup Engineering Limited | Parent Company | 323 | — |
| 2 | Mabel Engineers Private Limited | Wholly Owned Subsidiary Company | 324 | — |

No prior-quarter ledger available for this run — ENTITY_CHANGE comparison not possible; flag `ENTITY_CHANGE` NOT applicable / not evaluable this run (name it explicitly to A3/A4 as a coverage gap, not a finding).

---

## 5. FINANCIAL STATEMENT TABLES — LINE ITEMS (71 rows total across 3 tables)

### 5a. Standalone Unaudited Financial Results (L151-220), 33 rows

Columns as printed: Quarter Ended 30.06.2026 (Unaudited) | 31.03.2026 (Refer Note 6) | 30.06.2025 (Unaudited) | Year Ended 31.03.2026 (Audited). Units: Rs Lakhs, EPS in Rs (not annualised).

| Sr/Sub | Particulars | Line | 30.06.2026 | 31.03.2026 | 30.06.2025 | 31.03.2026 (YE) | Flags |
|---|---|---|---|---|---|---|---|
| 1 | Income (header) | 157 | — | — | — | — | — |
| 1(a) | Revenue from operations | 158 | 11,789.29 | 19,480.07 | 16,942.21 | 78,943.70 | — |
| 1(b) | Other Income | 159 | 49.74 | 51.52 | 228.34 | 329.89 | — |
| — | Total Income | 161 | 11,839.03 | 19,531.59 | 17,170.55 | 79,273.59 | — |
| 2 | Expenses (header) | 163 | — | — | — | — | — |
| 2(a) | Cost of materials consumed | 164 | 5,050.24 | 9,277.15 | 7,135.88 | 35,335.08 | — |
| 2(b) | Changes in inventories of work-in-progress | 165 | 983.80 | 881.69 | 1,057.76 | 2,959.07 | — |
| 2(c) | Employee benefits expense | 166 | 1,182.34 | 1,044.95 | 1,103.57 | 4,579.92 | — |
| 2(d) | Finance costs | 167 | 143.35 | 212.59 | 84.78 | 830.09 | — |
| 2(e) | Depreciation and amortisation expense | 168 | 727.14 | 742.38 | 636.15 | 2,719.08 | — |
| 2(f) | Other expenses | 169 | 3,631.23 | 4,671.22 | 3,707.61 | 19,150.15 | — |
| — | Total Expenses | 171 | 11,718.10 | 16,829.98 | 13,725.75 | 65,573.39 | — |
| 3 | Profit before exceptional items and tax (1-2) | 173 | 120.93 | 2,701.61 | 3,444.80 | 13,700.20 | — |
| 4 | Exceptional item (net of taxes) (Refer Note 4) | 174 | - | - | - | (130.52) | Dash in 3/4 periods, not all 4 — not ZERO_STANDING |
| 5 | Profit Before Tax (3+4) | 175 | 120.93 | 2,701.61 | 3,444.80 | 13,569.68 | — |
| 6 | Tax Expense (header) | 176 | — | — | — | — | — |
| 6.1 | Current Tax | 177 | 41.00 | 694.00 | 942.34 | 3,369.00 | — |
| 6.2 | Excess provision of tax of earlier years | 178 | - | (533.95) | - | (533.95) | Dash in 2/4 periods, not all 4 — not ZERO_STANDING |
| 6.3 | Deferred Tax Credit | 179 | (30.88) | (5.47) | (50.68) | (40.01) | — |
| — | Total Tax Expense | 180 | 10.12 | 154.58 | 891.66 | 2,795.04 | — |
| 7 | Profit for the period/year (5-6) | 182 | 110.81 | 2,547.03 | 2,553.14 | 10,774.64 | — |
| 8 | Other Comprehensive Income/(Loss) (Net of Tax) (header) | 184 | — | — | — | — | — |
| 8(i) | Re-measurement of defined benefit plans | 186 | 30.84 | 154.56 | (10.41) | 123.34 | — |
| 8(ii) | Income Tax impact relating to above | 187 | (7.76) | (38.90) | 2.62 | (31.04) | — |
| 8(iii) | Remeasurement Income/(loss) of Cash flow hedge reserve | 189 | 269.14 | (159.76) | 166.97 | (264.42) | — |
| 8(iv) | Income tax related to above item | 190 | (67.74) | 40.21 | (42.02) | 66.55 | — |
| — | Total Other Comprehensive Income/(Loss) (Net of Tax) | 192 | 224.48 | (3.89) | 117.16 | (105.57) | — |
| 9 | Total Comprehensive Income for the period/year (7+8) | 194 | 335.29 | 2,543.14 | 2,670.30 | 10,669.07 | — |
| 10 | Paid-up Equity Share Capital (Face Value Rs 10/- per share) | 196 | 2,003.15 | 2,003.15 | 2,002.65 | 2,003.15 | — |
| 11 | Other Equity | 197 | (blank) | (blank) | (blank) | 66,679.19 | Reported only at year-end per standard Ind AS 34 interim practice — blank in all 3 interim columns; not flagged ZERO_STANDING (value exists at year-end, this is a structural interim-reporting omission, not a nil template line) |
| 12 | Earnings Per Share in Rs (Not Annualised) (header) | 198 | — | — | — | — | — |
| 12(a) | - Basic | 199 | 0.55 | 12.72 | 12.75 | 53.80 | — |
| 12(b) | - Diluted | 200 | 0.55 | 12.72 | 12.70 | 53.68 | — |

### 5b. Consolidated Unaudited Financial Results (L358-429), 33 rows

Same column structure as 5a; consolidated ("the Group" = Parent + Mabel Engineers Pvt Ltd).

| Sr/Sub | Particulars | Line | 30.06.2026 | 31.03.2026 | 30.06.2025 | 31.03.2026 (YE) | Flags |
|---|---|---|---|---|---|---|---|
| 1 | Income (header) | 365 | — | — | — | — | — |
| 1(a) | Revenue from operations | 366 | 12,524.92 | 20,785.97 | 17,523.24 | 82,228.77 | — |
| 1(b) | Other Income | 367 | 52.09 | 24.66 | 233.49 | 313.02 | — |
| — | Total Income | 369 | 12,577.01 | 20,810.63 | 17,756.73 | 82,541.79 | — |
| 2 | Expenses (header) | 371 | — | — | — | — | — |
| 2(a) | Cost of materials consumed | 372 | 5,731.19 | 9,659.35 | 7,480.75 | 37,489.79 | — |
| 2(b) | Changes in inventories of work-in-progress | 373 | 463.35 | 840.57 | 897.43 | 1,840.05 | — |
| 2(c) | Employee benefits expense | 374 | 1,331.47 | 1,294.08 | 1,239.18 | 5,127.52 | — |
| 2(d) | Finance costs | 375 | 161.76 | 221.38 | 87.30 | 869.83 | — |
| 2(e) | Depreciation and amortisation expense | 376 | 743.45 | 755.08 | 653.13 | 2,784.10 | — |
| 2(f) | Other expenses | 377 | 4,052.35 | 5,167.50 | 3,870.71 | 20,355.19 | — |
| — | Total Expenses | 379 | 12,483.57 | 17,937.96 | 14,228.50 | 68,466.48 | — |
| 3 | Profit before exceptional items and tax (1-2) | 381 | 93.44 | 2,872.67 | 3,528.23 | 14,075.31 | — |
| 4 | Exceptional item (net of taxes) (Refer Note 4) | 382 | - | - | - | (145.26) | Dash in 3/4 periods, not all 4 — not ZERO_STANDING |
| 5 | Profit Before Tax (3+4) | 383 | 93.44 | 2,872.67 | 3,528.23 | 13,930.05 | — |
| 6 | Tax Expense (header) | 384 | — | — | — | — | — |
| 6.1 | Current Tax | 385 | 41.00 | 740.41 | 963.74 | 3,468.86 | — |
| 6.2 | Excess provision of tax of earlier years | 386 | - | (532.08) | - | (532.08) | Dash in 2/4 periods, not all 4 — not ZERO_STANDING |
| 6.3 | Deferred Tax Charge/(Credit) | 387 | (4.58) | 9.89 | (61.61) | (45.97) | — |
| — | Total Tax Expense | 388 | 36.42 | 218.22 | 902.13 | 2,890.81 | — |
| 7 | Profit for the period/year (5-6) | 390 | 57.02 | 2,654.45 | 2,626.10 | 11,039.24 | — |
| 8 | Other Comprehensive Income/(Loss) (Net of Tax) (header) | 392 | — | — | — | — | — |
| 8(i) | Re-measurement of defined benefit plan | 394 | 33.47 | 164.46 | (10.21) | 133.84 | — |
| 8(ii) | Income Tax impact relating to above items | 395 | (8.42) | (41.39) | 2.57 | (33.68) | — |
| 8(iii) | Remeasurement income/(loss) of Cash flow hedge reserve | 397 | 269.14 | (159.76) | 166.97 | (264.42) | — |
| 8(iv) | Income tax related to above item | 398 | (67.74) | 40.21 | (42.02) | 66.55 | — |
| — | Total Other Comprehensive Income/(Loss) (Net of Tax) | 400 | 226.45 | 3.52 | 117.31 | (97.71) | — |
| 9 | Total Comprehensive Income for the period/year (7+8) | 402 | 283.47 | 2,657.97 | 2,743.41 | 10,941.53 | — |
| 10 | Paid-up Equity Share Capital (Face Value Rs 10/- per share) | 404 | 2,003.15 | 2,003.15 | 2,002.65 | 2,003.15 | — |
| 11 | Other Equity | 405 | (blank) | (blank) | (blank) | 67,097.50 | Reported only at year-end, same as standalone — not flagged ZERO_STANDING |
| 12 | Earnings Per Share in Rs (Not Annualised) (header) | 406 | — | — | — | — | — |
| 12(a) | - Basic | 407 | 0.28 | 13.25 | 13.11 | 55.12 | — |
| 12(b) | - Diluted | 408 | 0.28 | 13.25 | 13.07 | 54.99 | — |

### 5c. Consolidated Note 6 — "Key numbers of standalone financial results of the Parent Company" sub-table (L457-466), 5 rows

This is a distinct embedded table inside consolidated Note 6, restating standalone headline figures for the reader's cross-check within the consolidated notes.

| # | Particulars | Line | 30.06.2026 | 31.03.2026 | 30.06.2025 | 31.03.2026 (YE) | Flags |
|---|---|---|---|---|---|---|---|
| 1 | Revenue from Operations | 461 | 11,789.29 | 19,480.07 | 16,942.21 | 78,943.70 | Ties to standalone table row 1(a), L158 |
| 2 | Profit before tax | 462 | 120.93 | 2,701.61 | 3,444.80 | 13,569.68 | Ties to standalone table row 5, L175 |
| 3 | Profit for the period | 463 | 110.81 | 2,547.03 | 2,553.14 | 10,774.64 | Ties to standalone table row 7, L182 |
| 4 | Other Comprehensive Income/(Loss) (net of tax) | 464 | 224.48 | (3.89) | 117.16 | (105.57) | Ties to standalone table Total OCI, L192 |
| 5 | Total Comprehensive Income for the period | 465 | 335.29 | 2,543.14 | 2,670.30 | 10,669.07 | Ties to standalone table row 9, L194 |

---

## 6. NUMBERED NOTES (13 total: 6 standalone + 7 consolidated)

### 6a. Notes to the Standalone Unaudited Financial Results (L227-256), 6 notes

| Note | Line | First ~15 words | Flags |
|---|---|---|---|
| 1 | 229-231 | "The above standalone unaudited financial results have been prepared in accordance with Indian Accounting Standards..." | — |
| 2 | 232-233 | "The above standalone unaudited financial results have been reviewed and recommended by the Audit Committee..." | Discloses: unmodified conclusion by Statutory Auditors |
| 3 | 236 | "The Company's business activity falls within a single operating business segment of 'Engineering Products'." | Single segment |
| 4 | 237-246 | "The Government of India, vide Notification dated November 21, 2025, has notified The Code on Wages..." | Labour Codes past-service cost of Rs 130.52 lakhs (net of tax Rs 43.90 lakhs) recognised under Exceptional Item |
| 5 | 247-249 | "The Company has issued Nil equity shares during quarter ended June 30, 2026 (Quarter ended March 31..." | ZERO_STANDING — Nil ESOP shares issued in Q1 FY27, Q4 FY26, and Q1 FY26; 5,000 shares issued in FY26 full year — standing disclosure line, nil in current and two comparative quarters |
| 6 | 250-253 | "The figures for the quarter ended March 31, 2026 are the balancing figures between the audited figures..." | Explains Q4 FY26 balancing-figure methodology; also notes regrouping/reclassification of prior-period figures |

### 6b. Notes to the Consolidated Unaudited Financial Results (L436-471), 7 notes

| Note | Line | First ~15 words | Flags |
|---|---|---|---|
| 1 | 438-440 | "The above consolidated unaudited financial results have been prepared in accordance with Indian Accounting Standards..." | — |
| 2 | 441-442 | "The above consolidated unaudited financial results have been reviewed and recommended by the Audit Committee..." | Discloses: unmodified conclusion by Statutory Auditors |
| 3 | 444 | "The Group's business activity falls within a single operating business segment of 'Engineering Products'." | Single segment |
| 4 | 445-453 | "The Government of India, vide Notification dated November 21, 2025, has notified The Code on Wages..." | Labour Codes past-service cost of Rs 145.26 lakhs (net of tax Rs 48.86 lakhs) recognised under Exceptional Item — differs from standalone Rs 130.52 lakhs, delta attributable to subsidiary Mabel Engineers |
| 5 | 454-455 | "The Parent Company has issued Nil equity shares during quarter ended June 30, 2026 (Quarter ended March 31..." | ZERO_STANDING — Nil ESOP shares issued in Q1 FY27, Q4 FY26, and Q1 FY26; 5,000 shares issued in FY26 full year (same disclosure as standalone Note 5, restated at Parent Company level) |
| 6 | 457-465 | "Key numbers of standalone financial results of the Parent Company are as under:" | Contains embedded 5-row sub-table, see Section 5c above |
| 7 | 467-470 | "The figures for the quarter ended March 31, 2026 are the balancing figures between the audited figures..." | Explains Q4 FY26 balancing-figure methodology; also notes regrouping/reclassification of prior-period figures |

---

## 7. RECONCILIATION / GAPS FOR A3-A4

- No prior-quarter ledger supplied — entity-change, dropped-note, and dropped-line-item diffs against Q4 FY26 / Q1 FY26 filings are NOT evaluable in this run. Flag to orchestrator as a coverage gap, not a finding.
- Both UDIN numbers (L135 standalone, L346 consolidated) are OCR-illegible in the source extract — recorded as NOT FOUND rather than guessed. A3/A4 should flag for source-document re-verification if UDIN validation is material to the review.
- Standalone and consolidated auditor reports are silent on whether the subsidiary's (Mabel Engineers Private Limited) financial information was itself independently reviewed vs management-certified/furnished — this qualifier, common in consolidated review reports with subsidiaries, is NOT FOUND in either report's text (paras 1-6 of the consolidated report, L295-350). Do not infer either way.
- Labour Codes exceptional item differs between standalone (Rs 130.52 lakhs / net of tax Rs 43.90 lakhs, Note 4, L242-243) and consolidated (Rs 145.26 lakhs / net of tax Rs 48.86 lakhs, Note 4, L450-451) — the Rs 14.74 lakhs delta is attributable to the subsidiary Mabel Engineers Private Limited layer; both are enumerated as separate note rows above (6a Note 4, 6b Note 4), not collapsed.
