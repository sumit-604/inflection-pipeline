# A2 COMPLETENESS LEDGER — Sterlite Technologies Limited (STLTECH), Q1FY27 results

Source: `extract_results_stltech_q1fy27.txt` (25 pages, 1586 lines, unit Crores, no OCR pages flagged
though several tables — esp. the Security Cover Statement, pages 22-25 — show visible OCR corruption).
Prior-quarter ledger: none (first quarterly-pipeline run for this ticker) — so ENTITY_CHANGE /
DROPPED_SLIDE style diff flags cannot be raised this run; noted, not fabricated.

```
=== A2 COUNT TEST ===
category: notes             grep_count: 24   sweep_count: 24   match: yes
  (raw regex `^\s*[0-9]+\.\s` on notes ranges hit 11/14 due to two OCR artifacts —
   "2.The" no-space after the period in consol Note 2, line 328; and two false positives in the
   standalone range: "8. 50K" NCD-rate table noise at line 629, and "2026. The" a mid-sentence
   year+period false match at line 727. Refined pattern `^\s*[0-9]{1,2}\.` plus manual line-by-line
   confirmation against each "Notes to ... financial results" block converges on 12 consolidated +
   12 standalone = 24 both ways.)
category: line_items         grep_count: 200  sweep_count: 200  match: yes
  (sub-table grep-vs-manual reconciliation shown inline per table below; consol P&L 33/33,
   consol segment data rows 26/26 [+4 section-header lines tracked separately, not counted as
   line items], consol ratios 16/16, standalone P&L 30/30, standalone ratios 16/16, Security Cover
   Pt A assets 13/13, Pt A liabilities 13/13 [+3 summary rows], Pt B assets 13/13, Pt B liabilities
   13/13 [+4 summary rows], Annexure I 5/5, Annexure II 15/15 = 173 core + 7 summary + 5 + 15 = 200)
category: zero_standing       sweep_count: 38  (subset of line_items above, tracked separately)
category: agenda_items       grep_count: 9    sweep_count: 9    match: yes
category: auditor_paras      grep_count: 27   sweep_count: 27   match: yes
  (8 consol review report + 5 standalone review report + 14 security-cover auditors' report)
category: entities            grep_count: 20   sweep_count: 20   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

---

## 1. BOARD OUTCOME / COVER LETTER (page 1, lines 18-75)

| # | Item | Line | Detail | Flags |
|---|------|------|--------|-------|
| 1 | Core resolution | 33-36 | Board approved Unaudited Consolidated and Standalone Financial Results for Q1FY27 (qtr ended June 30, 2026) with Limited Review of Statutory Auditors | |
| 2 | Enclosure (i) | 39 | Press Release on the Unaudited Financial Results | |
| 3 | Enclosure (ii) | 40 | Investors Presentation on the Unaudited Financial Results | (not in this extract — results doctype only; presentation is a separate doctype/run) |
| 4 | Enclosure (iii) | 41 | Unaudited Consolidated and Standalone Financial Results | |
| 5 | Enclosure (iv) | 42 | Limited Review Report on Consolidated and Standalone Results | |
| 6 | Enclosure (v) | 43-45 | Integrated Filing disclosure per SEBI Master Circular, enclosed as Annexure I | |
| 7 | Enclosure (vi) | 46-47 | Statement of Utilisation of Warrant-issue proceeds + Material Deviation statement, Reg 32(1), enclosed as Annexure II | |
| 8 | Enclosure (vii) | 48-51 | Statement of Utilisation of NCD proceeds + Material Deviation statement, Reg 52(7)/(7A), confirms Nil deviation for the quarter | |
| 9 | Enclosure (viii) | 52-55 | Security Cover details for the quarter + Statutory Auditors' certificate, Reg 54(3) | |
| — | Meeting timing | 56 | Commenced 11:50 am, concluded 2:36 pm — a 2 hr 46 min meeting (substantive, not a rubber-stamp) | |
| — | Signatory | 59-69 | Mrunal Asawadekar, Company Secretary & Compliance Officer, Membership A24346; digitally signed 2026.07.24 14:39:55 (i.e., 3 min 55 sec after meeting concluded — consistent, not flagged) | |

Agenda items (core + 8 enclosures) = **9**. No AR approval / AGM notice / record date / dividend /
director appointment / auditor change / scrutinizer / ESOP-grant / capital-raising-enabling
resolution items appear in this letter — this Board Outcome covers results approval only; the
letter contains no other business.

---

## 2. CONSOLIDATED FINANCIAL RESULTS — P&L table (page 4, lines 198-240)

Columns are Q1FY27(June26) / Q4FY26(March26) / Q1FY26(June25) / FY26(March26, audited).

| # | Line item | Line | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|-----------|------|--------|--------|--------|------|-------|
| 1 | Revenue from operations | 198 | 1,910 | 1,441 | 1,019 | 4,745 | |
| 2 | Other income | 199 | 12 | 23 | 8 | 59 | |
| 3 | Total income | 200 | 1,922 | 1,464 | 1,027 | 4,804 | subtotal |
| 4 | Total expenditure | 201 | 1,525 | 1,246 | 887 | 4,176 | subtotal |
| 5 | Cost of raw materials and components consumed | 202 | 805 | 651 | 554 | 2,461 | |
| 6 | Purchase of stock-in-trade | 203 | - | 0 | 0 | 0 | ZERO_STANDING |
| 7 | (Increase)/decrease in inventories of FG/WIP/stock-in-trade | 204-206 | 158 | 68 | (41) | (76) | |
| 8 | Employee benefits expense | 207 | 195 | 178 | 156 | 659 | |
| 9 | Net impairment losses on financial and contract assets | 208 | - | 17 | - | 17 | ZERO_STANDING |
| 10 | Other expenses | 209 | 367 | 332 | 218 | 1,115 | |
| 11 | EBITDA | 210-212 | 397 | 218 | 140 | 628 | subtotal |
| 12 | Finance costs | 213 | 55 | 63 | 50 | 224 | |
| 13 | Depreciation and amortisation expense | 214 | 85 | 77 | 77 | 313 | |
| 14 | Profit/(loss) before exceptional item and tax | 215 | 257 | 78 | 13 | 91 | subtotal |
| 15 | Exceptional items (Refer note 9) | 216 | - | 31 | - | 16 | ZERO_STANDING |
| 16 | Profit/(loss) before tax | 217 | 257 | 109 | 13 | 107 | subtotal |
| 17 | Tax expense/(credit) | 218 | 60 | 50 | 3 | 51 | subtotal |
| 18 | Current tax | 219 | 34 | 5 | 8 | 32 | |
| 19 | Deferred tax (Refer note 10) | 220 | 26 | 45 | (5) | 19 | |
| 20 | Net profit/(loss) for the period/year | 221 | 197 | 59 | 10 | 56 | subtotal |
| 21 | OCI A.i) Items that will be reclassified to P&L | 223 | 66 | 20 | 20 | 90 | |
| 22 | OCI A.ii) Income tax relating to these items | 224 | (14) | 2 | 2 | (1) | |
| 23 | OCI B.i) Items that will not be reclassified to P&L | 225 | 1 | 4 | - | 6 | ZERO_STANDING (Q1FY26) |
| 24 | OCI B.ii) Income tax relating to these items | 226 | (0) | (1) | - | (2) | ZERO_STANDING (Q1FY26; "(0)" itself a sub-rounding value) |
| 25 | Total OCI for the period/year | 227 | 53 | 25 | 22 | 93 | subtotal |
| 26 | Total comprehensive income for the period/year | 228 | 250 | 84 | 32 | 149 | subtotal |
| 27 | Net profit/(loss) attributable to: Owners of the company | 229-230 | 197 | 59 | 10 | 56 | see note below |
| 28 | OCI attributable to: Owners of the company | 231-232 | 53 | 25 | 22 | 93 | |
| 29 | Total comprehensive income attributable to: Owners of the company | 233-234 | 250 | 84 | 32 | 149 | |
| 30 | Paid-up equity share capital (FV Rs 2, fully paid) | 235 | 98 | 98 | 98 | 98 | |
| 31 | Other Equity | 236 | (blank) | (blank) | (blank) | 2,170 | year-end-only disclosure, standard, not dash/zero |
| 32 | Basic EPS (Rs, not annualised) | 238 | 4.03 | 1.21 | 0.20 | 1.15 | |
| 33 | Diluted EPS (Rs, not annualised) | 239 | 3.71 | 1.17 | 0.20 | 1.11 | |
| FN | Footnote: "Amount appearing as '0' is below rounding off norm followed by the Group." | 240 | | | | | |

Note on row 27: no "Non-controlling interest" attribution line appears anywhere in the
attributable-to blocks (229-234) — i.e., the statement shows 100% attribution to Owners across net
profit, OCI and TCI with no NCI row present at all (not even a zero-value NCI row). Flagged for A3/A4
to confirm whether STL Group in fact has no minority-held subsidiaries this quarter (plausible given
all 20 consolidation-list entities are wholly owned, per Section 4 below) — not treated as a dropped
line since no NCI row exists in any period shown, so ZERO_STANDING does not strictly apply (nothing to
be zero), but the absence is recorded here so it is not silently missed.

---

## 3. CONSOLIDATED SEGMENT DISCLOSURE (page 5, lines 267-303)

| # | Item | Line | Detail | Flags |
|---|------|------|--------|-------|
| S1 | Segment definition 1 | 267 | Optical networking business — design/mfg of optical fibre, cables, optical interconnect | |
| S2 | Segment definition 2 | 268 | Digital and technology solutions — digital transformation of telcos/enterprises | |
| H1 | Section header "1. Segment revenue" | 274 | structural label, not a data row | |
| 1 | Segment revenue — Optical networking business | 275 | 1,842 / 1,378 / 961 / 4,486 | |
| 2 | Segment revenue — Digital and technology solutions | 276 | 72 / 69 / 64 / 284 | |
| 3 | Inter segment elimination | 277 | (4) / (6) / (6) / (25) | |
| 4 | Revenue from operations (subtotal, ties to P&L row 1) | 278 | 1,910 / 1,441 / 1,019 / 4,745 | |
| H2 | Section header "2. Segment Results (EBITDA)" | 279 | structural label | |
| 5 | Segment results — Optical networking business | 280 | 401 / 202 / 137 / 606 | |
| 6 | Segment results — Digital and technology solutions | 281 | 2 / 0 / 1 / 3 | ZERO_STANDING (Q4FY26) |
| 7 | Total segment results | 282 | 403 / 202 / 138 / 609 | subtotal |
| 8 | Net unallocated income/(expense) | 283 | (6) / 16 / 2 / 19 | |
| 9 | Total EBITDA (ties to P&L row 11) | 284 | 397 / 218 / 140 / 628 | |
| 10 | Finance cost | 285 | 55 / 63 / 50 / 224 | |
| 11 | Depreciation and amortisation expense | 286 | 85 / 77 / 77 / 313 | |
| 12 | Profit/(loss) before exceptional item and tax | 287 | 257 / 78 / 13 / 91 | |
| 13 | Exceptional items (Refer note 9) | 288 | - / 31 / - / 16 | ZERO_STANDING |
| 14 | Profit/(loss) before tax | 289 | 257 / 109 / 13 / 107 | |
| H3 | Section header "3. Segment assets" | 290 | structural label | |
| 15 | Segment assets — Optical networking business | 291 | 5,947 / 5,399 / 4,523 / 5,399 | |
| 16 | Segment assets — Digital and technology solutions | 292 | 174 / 185 / 146 / 185 | |
| 17 | Total segment assets | 293 | 6,121 / 5,584 / 4,669 / 5,584 | |
| 18 | Inter segment elimination | 294 | (2) / (2) / (162) / (2) | |
| 19 | Unallocated assets | 295 | 2,450 / 764 / 987 / 764 | |
| 20 | Total assets | 296 | 8,569 / 6,346 / 5,494 / 6,346 | |
| H4 | Section header "4. Segment Liabilities" | 297 | structural label | |
| 21 | Segment liabilities — Optical networking business | 298 | 2,271 / 1,969 / 1,429 / 1,969 | |
| 22 | Segment liabilities — Digital and technology solutions | 299 | 197 / 195 / 138 / 195 | |
| 23 | Total segment liabilities | 300 | 2,468 / 2,164 / 1,567 / 2,164 | |
| 24 | Inter segment elimination | 301 | (2) / (2) / (162) / (2) | |
| 25 | Unallocated liabilities | 302 | 2,108 / 1,916 / 2,068 / 1,916 | |
| 26 | Total liabilities | 303 | 4,574 / 4,078 / 3,473 / 4,078 | |

Two-segment structure — no third segment silently dropped (Digital and Technology Solutions is
consistently the smaller, near-breakeven segment across all four periods shown).

---

## 4. NOTES TO CONSOLIDATED FINANCIAL RESULTS (page 6-8, lines 321-493)

| # | Line | First ~15 words | Flags |
|---|------|-----------------|-------|
| 1 | 323-325 | "The aforesaid consolidated financial results...were reviewed by Audit Committee and subsequently approved by the Board..." | |
| 2 | 328-329 | "The above consolidated financial results has been prepared in accordance with...Ind-AS..." | (OCR: "2.The" no space — grep artifact, confirmed present) |
| 3 | 332-334 | "During the quarter...the Company allotted 35,097 equity shares...upon exercise of Employee Stock Options" | |
| 4 | 336-361 | "Details of Secured, Redeemable, Non-Convertible Debentures as at June 30, 2026..." — 8.50% NCD, Rs 290 cr outstanding, 100% security cover, CRISIL "AA-" | contains sub-table: Previous/Next Due Date, Principal, Interest, Installment, Amount |
| 5 | 364-370 | "Subsequent to the quarter ended June 30, 2026, the Company has allotted 25,728,500 equity shares...QIP...Rs 1,500 crores" | promoter stake diluted 44.44% -> 42.29%; subsequent event |
| 6 | 372-384 | "Prysmian Cables and Systems USA, LLC...filed a complaint...against Stephen Szymanski...and against STI" — jury verdict $101.25M total award incl. $4.75M costs, STI appealing, bond $41.53M deposited, "ultimate financial implications...cannot be ascertained" | CONTINGENT_LIABILITY_UNQUANTIFIED |
| 7 | 408-447 | "The disclosures required as per...Regulation 52(4) and 54(2)...are given below" — 16-row ratios table (Section 6 below) | |
| 8 | 449-451 | "During the previous year ended March 31, 2026, the Company and its subsidiary had paid/provided for managerial remuneration...except for...Rs 11 crores. ...will seek necessary approval in...ensuing AGM" | GOVERNANCE_APPROVAL_PENDING |
| 9 | 453-464 | "Exceptional items in the financial results includes:" (i) Labour Codes statutory impact gratuity Rs 12 cr + comp. absences Rs 3 cr (year ended Mar-26); (ii) reversal of impairment Rs 31 cr re: Jiangsu Sterlite Fiber Technology Co. Ltd | |
| 10 | 484-486 | "STL Digital Limited...assessed the recoverability of its deferred tax assets...written-down...Rs 41 crores" (year ended Mar-26) | |
| 11 | 488-490 | "Figures for the quarter ended March 31, 2026 are the balancing figures between the audited...full financial year...and the unaudited...up to December 31, 2025" | |
| 12 | 492-493 | "These consolidated financial results are available on the Company's website..." | |

12 notes confirmed by manual line-by-line read (matches refined-grep count of 12).

---

## 5. STANDALONE FINANCIAL RESULTS — P&L table (page 9, lines 537-575)

| # | Line item | Line | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|-----------|------|--------|--------|--------|------|-------|
| 1 | Revenue from operations | 537 | 929 | 752 | 542 | 2,446 | |
| 2 | Other income | 538 | 49 | 72 | 38 | 179 | |
| 3 | Total income | 539 | 978 | 824 | 580 | 2,625 | subtotal |
| 4 | Total expenditure | 540 | 727 | 689 | 501 | 2,293 | subtotal |
| 5 | Cost of raw materials and components consumed | 541 | 386 | 257 | 241 | 1,098 | |
| 6 | Purchase of stock-in-trade | 542 | 58 | 97 | 62 | 283 | (non-zero here, unlike consolidated row 6) |
| 7 | (Increase)/decrease in inventories of FG/WIP/stock-in-trade | 543-545 | 9 | 52 | (3) | (28) | |
| 8 | Employee benefits expense | 546 | 53 | 50 | 42 | 170 | |
| 9 | Net impairment losses on financial and contract assets | 547 | 4 | 20 | - | 24 | ZERO_STANDING (Q1FY26) |
| 10 | Other expenses | 548 | 217 | 213 | 159 | 746 | |
| 11 | EBITDA | 549-550 | 251 | 135 | 79 | 332 | subtotal |
| 12 | Finance costs | 551 | 36 | 43 | 34 | 152 | |
| 13 | Depreciation and amortisation expense | 552 | 46 | 42 | 42 | 167 | |
| 14 | Profit/(loss) before exceptional item and tax | 553-554 | 169 | 50 | 3 | 13 | subtotal |
| 15 | Exceptional items (refer note 10) | 556 | - | - | - | (10) | ZERO_STANDING (all quarterly periods) |
| 16 | Profit/(loss) before tax | 558 | 169 | 50 | 3 | 3 | subtotal |
| 17 | Tax expense/(credit) | 559 | 44 | 17 | 1 | 1 | subtotal |
| 18 | Current tax | 560 | 1 | 4 | - | 4 | ZERO_STANDING (Q1FY26) |
| 19 | Deferred tax | 561 | 43 | 13 | 1 | (3) | |
| 20 | Net profit/(loss) for the period/year | 562 | 125 | 33 | 2 | 2 | subtotal |
| 21 | OCI A.i) Items reclassified to P&L | 564 | 48 | (30) | (19) | (38) | |
| 22 | OCI A.ii) Income tax relating to these items | 565 | (12) | 7 | 5 | 9 | |
| 23 | OCI B.i) Items not reclassified to P&L | 566 | 1 | 4 | - | 6 | ZERO_STANDING (Q1FY26) |
| 24 | OCI B.ii) Income tax relating to these items | 567 | (0) | (1) | - | (2) | ZERO_STANDING (Q1FY26) |
| 25 | Total OCI for the period/year | 568 | 37 | (20) | (14) | (25) | subtotal |
| 26 | Total comprehensive income for the period/year | 569 | 162 | 13 | (12) | (23) | subtotal |
| 27 | Paid-up equity share capital (FV Rs 2, fully paid) | 570 | 98 | 98 | 98 | 98 | |
| 28 | Other Equity | 571 | (blank) | (blank) | (blank) | 1,428 | year-end-only, standard |
| 29 | Basic EPS (Rs, not annualised) | 573 | 2.56 | 0.68 | 0.05 | 0.04 | |
| 30 | Diluted EPS (Rs, not annualised) | 574 | 2.36 | 0.66 | 0.05 | 0.04 | |
| FN | Footnote: "Amount appearing as '0' is below rounding off norm followed by the Company." | 575 | | | | | |

Standalone has 30 lines vs consolidated's 33 — the 3-line gap is exactly the "attributable to
Owners of the company" sub-block, which does not appear standalone (single entity, no minority
attribution concept applies) — accounted for, not a miss.

---

## 6. NOTES TO STANDALONE FINANCIAL RESULTS (page 10-11, lines 592-736)

| # | Line | First ~15 words | Flags |
|---|------|-----------------|-------|
| 1 | 594-596 | "The aforesaid standalone financial results...reviewed by Audit Committee and subsequently approved by the Board..." | |
| 2 | 599-600 | "Since the segment information as per Ind AS 108...is provided on the basis of consolidated financial results, the same is not provided separately" | |
| 3 | 602-603 | "The above statement has been prepared in accordance with...Ind-AS..." | |
| 4 | 606-608 | "During the quarter...the Company allotted 35,097 equity shares...upon exercise of Employee Stock Options" | |
| 5 | 610-638 | "Details of Secured, Redeemable, Non-Convertible Debentures as at June 30, 2026..." — same 8.50% NCD sub-table as consol Note 4 | |
| 6 | 640-646 | "Subsequent to the quarter ended June 30, 2026, the Company has allotted 25,728,500 equity shares...QIP...Rs 1,500 crores" | subsequent event, promoter dilution |
| 7 | 648-659 | "Prysmian Cables and Systems USA, LLC...filed a complaint...against Stephen Szymanski...and against STI" — same litigation as consol Note 6 | CONTINGENT_LIABILITY_UNQUANTIFIED |
| 8 | 676-716 | "The disclosure required as per...Regulation 52(4) and 54(2)...is given below" — 16-row ratios table (Section 7 below) | |
| 9 | 718-720 | "During the previous year ended March 31, 2026, the Company had paid/provided for managerial remuneration...except for...Rs 3 crores...seek necessary approval in the ensuing AGM" | GOVERNANCE_APPROVAL_PENDING |
| 10 | 723-729 | "On November 21, 2025, the Government of India notified four Labour Codes..." gratuity Rs 8 cr + comp. absences Rs 2 cr (standalone portion, year ended Mar-26) | |
| 11 | 730-732 | "Figures for the quarter ended March 31, 2026 are the balancing figures between the audited...and the unaudited..." | |
| 12 | 734-735 | "These standalone financial results are available on the Company's website..." | |

12 notes confirmed (matches refined-grep count of 12; raw grep of 14 included two OCR false
positives at line 629 "8. 50K..." NCD-rate table text and line 727 "2026. The incremental impact"
mid-sentence — both excluded on manual read).

---

## 7. REGULATORY RATIOS TABLES (Reg 52(4)/54(2)) — CONSOLIDATED (page 7, lines 413-447) and STANDALONE (page 11, lines 681-716)

| # | Ratio | Consol line | Consol Q1FY27/Q4FY26/Q1FY26/FY26 | Standalone line | Standalone Q1FY27/Q4FY26/Q1FY26/FY26 | Flags |
|---|-------|-------------|-----------------------------------|------------------|----------------------------------------|-------|
| 1 | Debt equity ratio | 413 | 0.39 / 0.71 / 0.70 / 0.71 | 681 | 0.34 / 0.68 / 0.65 / 0.68 | |
| 2 | Debt service coverage ratio | 416 | 1.41 / 0.63 / 2.39 / 0.96 | 684 | 1.04 / 0.82 / 2.22 / 1.25 | |
| 3 | Interest service coverage ratio | 419 | 6.07 / 2.68 / 2.74 / 2.51 | 687 | 5.68 / 2.72 / 2.29 / 2.11 | |
| 4 | Current ratio | 422 | 1.38 / 0.98 / 0.91 / 0.98 | 690 | 1.75 / 1.14 / 0.66 / 1.14 | |
| 5 | Long term debt to working capital | 424 | 0.71 / 6.82 / 13.59 / 6.82 | 692 | 0.45 / 3.51 / (0.93) / 3.51 | |
| 6 | Bad debt to accounts receivable ratio | 426 | 0.00 / - / - / 0.01 | 694 | 0.01 / 0.04 / 0.00 / 0.04 | ZERO_STANDING (consol: dash Q4FY26 & Q1FY26) |
| 7 | Current liability ratio | 428 | 0.76 / 0.67 / 0.73 / 0.67 | 696 | 0.74 / 0.62 / 0.82 / 0.62 | |
| 8 | Total debt to total assets | 430 | 0.24 / 0.31 / 0.32 / 0.31 | 698 | 0.23 / 0.30 / 0.28 / 0.30 | |
| 9 | Asset coverage ratio - NCD 8.50% | 432 | 2.78 / 2.64 / 2.77 / 2.64 | 700 | 2.78 / 2.64 / 2.77 / 2.64 | |
| 10 | Asset coverage ratio - NCD 9.35% | 435 | - / - / 1.75 / - | 703 | - / - / 1.75 / - | ZERO_STANDING (dash in 3 of 4 periods both consol & standalone — this NCD series appears redeemed/no longer outstanding after Q1FY26) |
| 11 | Trade receivables turnover ratio | 438 | 5.34 / 5.41 / 5.61 / 4.45 | 706 | 4.63 / 5.38 / 4.19 / 4.37 | |
| 12 | Inventory turnover ratio | 440 | 4.40 / 3.18 / 2.54 / 2.63 | 708 | 4.10 / 4.18 / 3.64 / 3.48 | |
| 13 | Operating margin (%) | 442 | 16% / 12% / 6% / 7% | 710 | 22% / 12% / 7% / 6% | |
| 14 | Net Profit Margin (%) | 444 | 10% / 4% / 1% / 1% | 712 | 13% / 4% / 0% / 0% | ZERO_STANDING (standalone: 0% in Q1FY26 & FY26) |
| 15 | Capital redemption reserve (Rs cr) | 446 | 2 / 2 / 2 / 2 | 714 | 2 / 2 / 2 / 2 | |
| 16 | Net worth (Rs cr) | 447 | 2,166 / 1,966 / 1,914 / 1,966 | 715 | 1,589 / 1,460 / 1,454 / 1,460 | |

16 ratios each table, 32 rows total, grep-verified (16/16 both).

---

## 8. AUDITOR'S REVIEW REPORT — CONSOLIDATED (Price Waterhouse Chartered Accountants LLP, pages 12-14, lines 767-892)

| Para | Line | Content | Flags |
|------|------|---------|-------|
| 1 | 780-787 | Scope: reviewed unaudited consolidated results for Q1FY27, per Reg 33/52/63 | |
| 2 | 788-793 | Management's responsibility; Ind AS 34 basis; auditor's responsibility to express a conclusion | |
| 3 | 794-806 | Conducted per SRE 2410 — review, not audit; moderate (not reasonable) assurance; "we do not express an audit opinion" | |
| 4 | 820-847 | Entity list — Holding Company + 20 entities (11 subsidiaries + 9 step-down subsidiaries — see Section 10) | |
| 5 | 848-855 | Conclusion — unmodified: "nothing has come to our attention..." | opinion type: unmodified/unqualified review conclusion |
| 6 | 856-860 | Emphasis of Matter — Note 6 (Prysmian/Szymanski litigation vs Sterlite Technologies Inc, USA); "possible financial impact...currently not determinable"; "conclusion is not modified" | EoM paragraph; CONTINGENT_LIABILITY_UNQUANTIFIED |
| 7 | 861-868 | Other Matter — 4 subsidiaries (revenue Rs 578 cr, PAT Rs 42 cr, TCI Rs 42 cr) reviewed by OTHER auditors under SRE 2400, unmodified; PW's conclusion on these rests on the other auditors' reports | entities reviewed by other auditors named by aggregate only, not individually |
| 8 | 871-878 | Other Matter — 12 subsidiaries (revenue Rs 94 cr, PAT Rs 1 cr, TCI Rs 1 cr) NOT reviewed by their auditors, management states "not material to the Group"; "conclusion...not modified" | UNAUDITED_ENTITIES — management-furnished, unreviewed figures embedded in consolidated numbers |
| — | 883-892 | Signature: Sachin Parekh, Partner, PW CA LLP, Firm Reg 012754N/N500016, Membership 107038, UDIN 26107038UBWSEF6569, dated July 24, 2026, timestamp 12:59:49 | SIG_BEFORE_MEETING_CONCLUSION (board concluded 14:36; this report signed 12:59:49, ~1h36m before conclusion) |

8 paragraphs (numbered 1-8), one opinion (unmodified/unqualified conclusion), one EoM, two Other
Matter paragraphs, one entity table (20 rows), one UDIN.

### Entity/auditor reconciliation
20 entities total in para 4 list. Para 7 accounts for 4 (reviewed by other auditors). Para 8
accounts for 12 (unreviewed, management-furnished, immaterial). That leaves 4 entities of the 20
unaccounted for in paras 7/8 — presumably reviewed directly by PW itself or dormant/non-trading
shells with no separate review requirement. Not resolved by the extract text; flagged for A3/A4.

---

## 9. AUDITOR'S REVIEW REPORT — STANDALONE (Price Waterhouse Chartered Accountants LLP, pages 15-16, lines 893-972)

| Para | Line | Content | Flags |
|------|------|---------|-------|
| 1 | 906-912 | Scope: reviewed unaudited standalone results for Q1FY27, per Reg 33/52/63 | |
| 2 | 914-918 | Management's responsibility; Ind AS 34 basis | |
| 3 | 920-929 | Conducted per SRE 2410 — moderate assurance, not an audit opinion | |
| 4 | 931-937 | Conclusion — unmodified | opinion type: unmodified/unqualified |
| 5 | 952-956 | Emphasis of Matter — Note 7 (same Prysmian/Szymanski litigation); "possible financial impact...currently not determinable"; conclusion not modified | EoM paragraph; CONTINGENT_LIABILITY_UNQUANTIFIED |
| — | 959-972 | Signature: Sachin Parekh, Partner, Membership 107038, UDIN 26107038JZRUYE6523, dated July 24, 2026, timestamp 13:00:37 | SIG_BEFORE_MEETING_CONCLUSION |

5 paragraphs, single entity (no subsidiary table needed for standalone), one EoM, one UDIN
(different from the consolidated report's UDIN — correctly two separate UDINs for two separate
engagements/opinions by the same partner).

---

## 10. ENTITIES IN THE CONSOLIDATION LIST (para 4 of consolidated review report, lines 820-847)

| Sr | Entity | Relationship | Line | Flags |
|----|--------|--------------|------|-------|
| 1 | Sterlite Global Ventures (Mauritius) Limited | Subsidiary | 824 | |
| 2 | Speedon Network Limited | Subsidiary | 825 | |
| 3 | Elitecore Technologies SDN BHD. (Malaysia) | Subsidiary | 827 | |
| 4 | Sterlite (Shanghai) Trading Company Limited | Subsidiary | 829 | |
| 5 | Sterlite Tech Holding Inc. (USA) | Subsidiary | 831 | |
| 6 | Metallurgica Bresciana S.p.A | Subsidiary | 832 | |
| 7 | STL Digital Limited | Subsidiary | 834 | |
| 8 | Sterlite Tech Cables Solutions Limited | Subsidiary | 835 | |
| 9 | Sterlite Technologies Pty. Ltd | Subsidiary | 836 | |
| 10 | Sterlite Technologies DMCC | Subsidiary | 837 | |
| 11 | STL Tech Solutions Limited, UK | Subsidiary | 838 | |
| 12 | Jiangsu Sterlite Fiber Technology Co. Ltd. | Step down subsidiary | 839 | referenced in consol Note 9(ii) impairment reversal |
| 13 | Elitecore Technologies (Mauritius) Limited | Step down subsidiary | 840 | |
| 14 | Sterlite Technologies Inc. (South Carolina) | Step down subsidiary | 841 | this is "STI", the defendant in the Prysmian litigation (Notes 6/7) |
| 15 | Optotec S.p.A. | Step down subsidiary | 842 | |
| 16 | Optotec International S.A. | Step down subsidiary | 843 | |
| 17 | STL Digital Inc. (USA) | Step down subsidiary | 844 | |
| 18 | STL Optical Connectivity NA, LLC | Step down subsidiary | 845 | |
| 19 | STL Solutions Germany GmbH | Step down subsidiary | 846 | |
| 20 | STL Digital UK Limited | Step down subsidiary | 847 | |

20 entities (11 direct subsidiaries + 9 step-down subsidiaries). No prior-quarter list available for
diff, so ENTITY_CHANGE cannot be evaluated this run — noted as a gap for the next quarter's A2 to
close, not fabricated here.

---

## 11. ANNEXURE I — INTEGRATED FILING (FINANCIALS) (page 17, lines 974-995)

| Item | Line | Content | Flags |
|------|------|---------|-------|
| A | 981-982 | Unaudited Consolidated and Standalone Financial Results — Attached | |
| B | 984-985 | Statement on deviation/variation of preferential-issue (warrant) proceeds — Attached as Annexure II | |
| C | 987 | Disclosure of outstanding default on loans and debt securities — "No default, hence Not Applicable" | ZERO_STANDING |
| D | 989-990 | Related party transactions disclosure (applicable only 2nd/4th qtr) — "Not applicable for this quarter" | ZERO_STANDING |
| E | 992-994 | Statement on impact of audit qualifications (applicable only 4th qtr/annual) — "Not applicable" | ZERO_STANDING |

5 items (A-E).

---

## 12. ANNEXURE II — STATEMENT OF DEVIATION/VARIATION (Warrants) (page 18, lines 1007-1062)

| # | Field | Line | Value | Flags |
|---|-------|------|-------|-------|
| 1 | Name of listed entity | 1011 | Sterlite Technologies Limited | |
| 2 | Mode of Fund Raising | 1013-1014 | Warrants convertible into Equity Shares on Preferential Basis | |
| 3 | Date of Raising Funds | 1015 | March 30, 2026 (date of allotment) | |
| 4 | Amount Raised | 1017-1018 | Rs 1,24,57,50,000 (25% of warrant issue price) | |
| 5 | Report filed for Quarter ended | 1019 | June 30, 2026 | |
| 6 | Monitoring Agency | 1021 | Applicable | |
| 7 | Monitoring Agency Name | 1024 | CARE Ratings Limited | |
| 8 | Is there a Deviation/Variation in use of funds raised | 1026-1027 | No | ZERO_STANDING |
| 9 | If yes, pursuant to change in terms of contract/objects approved by shareholders | 1029-1031 | Not Applicable | ZERO_STANDING |
| 10 | If Yes, Date of shareholder Approval | 1033 | Not Applicable | ZERO_STANDING |
| 11 | Explanation for the Deviation/Variation | 1035 | Not Applicable | ZERO_STANDING |
| 12 | Comments of the Audit Committee after review | 1037 | Nil | ZERO_STANDING |
| 13 | Comments of the auditors, if any | 1039 | Nil | ZERO_STANDING |
| 14 | Object 1 — Repayment/Servicing of financial facilities | 1051-1052 | Original allocation Rs 373.73 cr, Funds utilised Rs 113.3 cr (cumulative), deviation Not Applicable | |
| 15 | Object 2 — General Corporate Purposes | 1054-1055 | Original allocation Rs 124.57 cr, Funds utilised Rs 13.28 cr (cumulative), deviation Not Applicable | |
| FN | Footnotes | 1056-1060 | Rs 124.57 cr (25% of warrant price) received in Q4FY26; no funds received in Q1FY27; utilisation figures are cumulative-to-date, not in-quarter | |

15 fields/rows (13 statement fields + 2 objects).

---

## 13. AUDITORS' REPORT ON SECURITY COVER (Price Waterhouse Chartered Accountants LLP, pages 19-21, lines 1068-1208)

| Para | Line | Content | Flags |
|------|------|---------|-------|
| 1 | 1082 | Engagement letter dated July 23, 2026 | |
| 2 | 1084-1095 | Scope — Statement of Security Cover per SEBI Master Circular, per Debenture Trust Deed dated March 18, 2021 with Axis Trustee Services Limited; examination requested via Company email July 3, 2026; digitally signed for identification only | |
| 3 | 1099-1102 | Management's Responsibility for the Statement (heading + para) | |
| 4 | 1104-1106 | Management's responsibility for SEBI/Agreement compliance | |
| 5 | 1110-1116 | Auditors' Responsibility — limited assurance on book values in columns A-H, Parts A & B | |
| 6 | 1117-1119 | FY27 (year ending March 31, 2027) financial statements subject to separate statutory audit | |
| 7 | 1135-1138 | Examination per 'Guidance Note on Reports or Certificates for Special Purposes' (ICAI), Code of Ethics compliance | |
| 8 | 1140-1142 | Compliance with SQC 1 | |
| 9 | 1144-1148 | Limited assurance engagement — lower level of assurance than reasonable assurance | |
| 10 | 1150-1158 | Procedures performed: traced Col A-H to books; verified Security Cover ratio calculation method; verified mathematical accuracy | |
| 11 | 1160-1163 | Scope exclusion — columns I-O NOT examined, furnished by management; no comment on calculations | management-furnished columns explicitly carved out of assurance |
| 12 | 1167-1172 | Conclusion — unmodified: book values in Col A-H agree with underlying unaudited books | |
| 13 | 1176-1180 | Restriction on Use — obligations separate from statutory audit role | |
| 14 | 1184-1188 | Restriction on Use (cont'd) — issued solely for Debenture Trustee/Stock Exchanges submission | |
| — | 1193-1208 | Signature: Pawankumar Radheshyam Somani, Partner, PW CA LLP, Firm Reg 012754N/N500016, Membership 137654, UDIN 26137654TQSGCG8282, Place: Pune, dated July 24, 2026 (no timestamp visible in extract beyond date) | |

14 paragraphs. Note: columns I-O of the Security Cover Statement (see Section 14/15) are
explicitly management-furnished and NOT covered by this limited-assurance report — carve-out
applies to whichever columns map to I-O in Parts A and B below.

---

## 14. STATEMENT OF SECURITY COVER — PART A: STANDALONE (pages 22-23, lines 1209-1420)

Table formatting is heavily OCR-corrupted (column headers unreadable, scattered garbled characters
throughout, e.g. "L.,." for what is presumably "Nil", "2,"78" for what is presumably "2.78" cover
ratio). OCR_TABLE_GARBLED flagged for this whole section; row labels are legible and are enumerated
below; several numeric cell alignments could not be confirmed with full confidence and are flagged
individually.

### Assets (lines 1340-1365)

| # | Line item | Line | Total (Col P, Rs cr) | Flags |
|---|-----------|------|----------------------|-------|
| 1 | Property, Plant and Equipment | 1341-1345 | 794 | |
| 2 | Capital Work-in-Progress | 1347 | 31 | |
| 3 | Right of Use Assets | 1348 | 44 | |
| 4 | Goodwill | 1349 | - | ZERO_STANDING |
| 5 | Intangible Assets | 1350 | 14 | |
| 6 | Intangible Assets under Development | 1351-1353 | - | ZERO_STANDING |
| 7 | Investments | 1354 | 303 | |
| 8 | Loans | 1355 | 597 | |
| 9 | Inventories | 1356 | 441 | |
| 10 | Trade Receivables | 1357 | 803 | |
| 11 | Cash and Cash Equivalents | 1358-1360 | 1,777 | includes Rs 1,500 cr QIP proceeds per Note 5 below |
| 12 | Bank Balances other than Cash and Cash Equivalents | 1361-1363 | 7 | |
| 13 | Others | 1364 | 417 | |
| 14 | Total | 1365 | 5,981 | subtotal |

### Liabilities (lines 1378-1398)

| # | Line item | Line | Total/value | Flags |
|---|-----------|------|-------------|-------|
| 1 | Debt Securities to which this certificate pertains | 1379-1381 | 297 (Yes flag set) | |
| 2 | Other debt sharing pari-passu charge with above debt | 1382-1384 | - | ZERO_STANDING |
| 3 | Other Debt | 1385 | 1,023 | |
| 4 | Subordinated debt | 1386 | - (blank) | ZERO_STANDING |
| 5 | Borrowings | 1387 | - (blank) | ZERO_STANDING |
| 6 | Bank | 1388 | "Not to be filled" (per format) | |
| 7 | Debt Securities | 1389 | - (blank) | ZERO_STANDING |
| 8 | Others | 1390 | 465 | |
| 9 | Trade payables | 1391 | 703 | |
| 10 | Lease Liabilities | 1392 | 41 | |
| 11 | Provisions | 1393 | 0 | ZERO_STANDING |
| 12 | Others | 1394 | 286 | |
| 13 | Total | 1395 | 2,815 | subtotal |
| 14 | Carrying/Book Value | 1396 | illegible in extract (OCR "L.,.") | OCR_TABLE_GARBLED |
| 15 | Cover on Market Value | 1397 | 2,478 (OCR "2,"78" read as 2,478 based on adjacent context) | OCR_TABLE_GARBLED — value not fully certain |
| 16 | Pari-Passu Security Cover Ratio | 1398 | value not extractable (heading only legible) | OCR_TABLE_GARBLED |

Notes to Part A (lines 1400-1407): 5 numbered notes — (1) statement prepared per Reg 56(1)(d);
(2) figures agree with unaudited books; (3) ratio computed per SEBI Circular method; (4) movable
asset book value used, market value not applicable per trust deed; (5) Cash & Cash Equivalents
includes Rs 1,500 cr QIP proceeds, to be utilised for debt repayment and general corporate purposes.

Signature (lines 1409-1420): Ajay Jhanjhari, Chief Financial Officer, dated July 24, 2026, Place
Mumbai; counter-referenced by Pawankumar Radheshyam Somani (Statutory Auditor, digitally signed for
identification purposes only) timestamp 12:35:44 — SIG_BEFORE_MEETING_CONCLUSION (well before the
14:36 board conclusion).

---

## 15. STATEMENT OF SECURITY COVER — PART B: CONSOLIDATED (pages 24-25, lines 1428-1586)

Same OCR_TABLE_GARBLED condition applies, more severely in the Liabilities section (numbers visibly
scrambled/misaligned, e.g. "1119", "(102", "1017" not cleanly resolvable to columns).

### Assets (lines 1490-1517)

| # | Line item | Line | Total (Rs cr) | Flags |
|---|-----------|------|----------------|-------|
| 1 | Property, Plant and Equipment | 1491-1495 | 794 | |
| 2 | Capital Work-in-Progress | 1496-1498 | 31 | |
| 3 | Right of Use Assets | 1499 | 106 | |
| 4 | Goodwill | 1500 | 195 | non-zero here, unlike Part A standalone (consolidation-level goodwill) |
| 5 | Intangible Assets | 1501 | 78 | |
| 6 | Intangible Assets under Development | 1502-1503 | - | ZERO_STANDING |
| 7 | Investments | 1504 | value illegible (OCR "AIIA") | OCR_TABLE_GARBLED |
| 8 | Loans | 1506 | 1 | |
| 9 | Inventories | 1507 | 876 | |
| 10 | Trade Receivables | 1508 | value illegible (OCR "1AOQ", presumably ~1,409) | OCR_TABLE_GARBLED |
| 11 | Cash and Cash Equivalents | 1510-1512 | 2,021 | includes Rs 1,500 cr QIP proceeds per note below |
| 12 | Bank Balances other than Cash and Cash Equivalents | 1513-1515 | 11 | |
| 13 | Others | 1516 | 734 | |
| 14 | Total | 1517 | 8,569 | ties to Consolidated Segment Total Assets (Section 3, row 20) |

### Liabilities (lines 1530-1554)

| # | Line item | Line | Total/value | Flags |
|---|-----------|------|-------------|-------|
| 1 | Debt Securities to which this certificate pertains | 1531-1533 | 297 (Yes flag) | |
| 2 | Other debt sharing pari-passu charge with above debt | 1534-1536 | - (blank) | ZERO_STANDING |
| 3 | Other Debt | 1537 | 1,653 | |
| 4 | Subordinated debt | 1538 | - (blank) | ZERO_STANDING |
| 5 | Borrowings | 1539 | - (blank) | ZERO_STANDING |
| 6 | Bank | 1540 | "Not to be filled" | |
| 7 | Debt Securities | 1541 | value not resolvable | OCR_TABLE_GARBLED |
| 8 | Others | 1542 | value not resolvable | OCR_TABLE_GARBLED |
| 9 | Trade payables | 1543-1544 | ~1,004 (OCR-garbled figures "2,244"/"(1,240)" nearby) | OCR_TABLE_GARBLED |
| 10 | Lease liabilities | 1550 | 129 (OCR "12Q") | OCR_TABLE_GARBLED — reasonably confident |
| 11 | Provisions | 1551 | 0 | ZERO_STANDING |
| 12 | Others | 1552 | ~1,017 (OCR "1119"/"(102"/"1017") | OCR_TABLE_GARBLED |
| 13 | Total | 1553-1554 | 4,573 | subtotal; ties loosely to Consolidated Segment Total Liabilities (Section 3, row 26 = 4,574 — Rs 1 cr rounding gap between the two statements, immaterial but noted) |
| 14 | Carrying/Book Value | 1555 | not resolvable | OCR_TABLE_GARBLED |
| 15 | Cover on Market Value | 1556 | not resolvable | OCR_TABLE_GARBLED |
| 16 | Exclusive Security Cover Ratio | 1557 | heading only, value not resolvable | OCR_TABLE_GARBLED |
| 17 | Pari-Passu Security Cover Ratio | 1557 | heading only, value not resolvable | OCR_TABLE_GARBLED |

Notes to Part B (lines 1560-1566): 5 numbered notes, same structure as Part A, with note 5
specifying Rs 1,500 cr QIP proceeds received "in the month of June-26" included in Cash & Cash
Equivalents.

Signature (lines 1568-1578): Ajay Jhanjhari, CFO, dated July 24, 2026, Place Mumbai; counter-signed
by Pawankumar Radheshyam Somani, timestamp 12:35:24 — SIG_BEFORE_MEETING_CONCLUSION.

---

## 16. SIGNATURE BLOCKS (all instances found across the extract)

| # | Line(s) | Signatory | Designation | Timestamp | Flags |
|---|---------|-----------|-------------|-----------|-------|
| 1 | 59-69 | Mrunal Asawadekar | Company Secretary & Compliance Officer | 2026.07.24 14:39:55 | after meeting conclusion — consistent |
| 2 | 245-250 | Ankit Agarwal / Sachin Parekh | MD / CFO (consol results, page 1 of 8) | ~13:01:38 | SIG_BEFORE_MEETING_CONCLUSION |
| 3 | 308-313 | Ankit Agarwal / Sachin Parekh | MD / CFO (consol segment, page 2 of 8) | ~13:01:59 | SIG_BEFORE_MEETING_CONCLUSION |
| 4 | 389-398 | Ankit Agarwal / Sachin Parekh | MD / CFO (consol notes, page 3 of 8) | 13:02:19 | SIG_BEFORE_MEETING_CONCLUSION |
| 5 | 469-474 | Ankit Agarwal / Sachin Parekh | MD / CFO (consol notes, page 4 of 8) | 13:02:38 | SIG_BEFORE_MEETING_CONCLUSION |
| 6 | 512-518 | Ankit Agarwal / Sachin Parekh | MD / CFO (consol notes, page 5 of 8) | 13:02:58 | SIG_BEFORE_MEETING_CONCLUSION |
| 7 | 580-585 | Ankit Agarwal / Sachin Parekh | MD / CFO (standalone results, page 6 of 8) | 13:03:16 | SIG_BEFORE_MEETING_CONCLUSION |
| 8 | 664-668 | Ankit Agarwal / Sachin Parekh | MD / CFO (standalone notes, page 7 of 8) | 13:03:34 | SIG_BEFORE_MEETING_CONCLUSION |
| 9 | 740-757 | Sachin Parekh / Ankit Agarwal | CFO / MD (standalone notes, page 8 of 8) | 13:04:06 | SIG_BEFORE_MEETING_CONCLUSION |
| 10 | 881-892 | Sachin Parekh | Partner, PW CA LLP (consol review report), UDIN 26107038UBWSEF6569 | 12:59:49 | SIG_BEFORE_MEETING_CONCLUSION |
| 11 | 959-972 | Sachin Parekh | Partner, PW CA LLP (standalone review report), UDIN 26107038JZRUYE6523 | 13:00:37 | SIG_BEFORE_MEETING_CONCLUSION |
| 12 | 1193-1208 | Pawankumar Radheshyam Somani | Partner, PW CA LLP (security cover report), UDIN 26137654TQSGCG8282 | date only, no time visible | |
| 13 | 1409-1420 | Ajay Jhanjhari / Pawankumar Somani | CFO / Statutory Auditor (Security Cover Part A) | 12:35:44 | SIG_BEFORE_MEETING_CONCLUSION |
| 14 | 1568-1578 | Ajay Jhanjhari / Pawankumar Somani | CFO / Statutory Auditor (Security Cover Part B) | 12:35:24 | SIG_BEFORE_MEETING_CONCLUSION |

14 signature blocks. All 12 financial-document/auditor-report signature timestamps that carry a
visible clock time (items 2-11, 13-14) fall between 12:35 and 13:04 — i.e., roughly 1.5-2 hours
BEFORE the board meeting's stated conclusion at 2:36 pm (14:36, line 56). Only the cover letter's
CS signature (item 1, 14:39:55) postdates the meeting's conclusion, as expected. This is a
mechanical timestamp fact only (not interpreted further here) — flagged as
SIG_BEFORE_MEETING_CONCLUSION for A3/A4 to reconcile against the stated meeting start/end window.

---

## FLAGS SUMMARY

- **ZERO_STANDING** — 38 rows across consolidated/standalone P&L, segment, ratios, Security Cover
  Parts A/B, and Annexures I/II (full list in tables above).
- **SIG_BEFORE_MEETING_CONCLUSION** — 12 of 14 signature blocks (all financial-statement pages,
  both review reports, and both Security Cover statement certifications) carry timestamps between
  12:35 pm and 1:04 pm, before the board meeting's stated 2:36 pm conclusion (line 56).
- **UNAUDITED_ENTITIES** — 12 of 20 consolidated subsidiaries (Rs 94 cr revenue, Rs 1 cr PAT) were
  NOT reviewed by their auditors this quarter; management represents them as immaterial (consol
  review report para 8, lines 871-878).
- **CONTINGENT_LIABILITY_UNQUANTIFIED** — Prysmian/Szymanski US litigation against Sterlite
  Technologies Inc. (STI); jury verdict $101.25 million total award, STI appealing, $41.53 million
  bond deposited, "ultimate financial implications...cannot be ascertained" (consol Note 6 /
  standalone Note 7; EoM paragraph in both review reports).
- **GOVERNANCE_APPROVAL_PENDING** — managerial remuneration paid in FY26 in excess of Schedule V
  limits (Rs 11 cr consolidated / Rs 3 cr standalone), shareholder approval to be sought at ensuing
  AGM (consol Note 8 / standalone Note 9).
- **OCR_TABLE_GARBLED** — Statement of Security Cover, Parts A and B (pages 22-25), especially Part
  B Liabilities; several cell values not confidently extractable from the OCR'd text; row labels
  legible and enumerated, values flagged individually where uncertain.
- **First-run gaps (not fabricated, noted for continuity)**: no prior-quarter ledger exists, so
  ENTITY_CHANGE (consolidation-list diff) and DROPPED_SLIDE-equivalent checks could not be run this
  quarter; four of the 20 consolidated entities are not reconciled to a specific review-status
  paragraph (see Section 8 reconciliation note).

---
