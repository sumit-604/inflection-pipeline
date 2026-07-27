# A2 ENUMERATION LEDGER — Tata Power (TATAPOWER), Q1 FY27, Results Filing

Source: `extract_results_tatapower_q1fy27.txt` (19 pages, PDFium layout reconstruction,
page_coverage 100%). All "line" references below are the extract's own internal line
numbers (the `NNN|` prefix on each content line), not raw OS file lines. No
prior-quarter ledger was supplied for this run, so entity-change and dropped-item
diffing against a prior quarter is marked N/A (not a gate failure — nothing to diff
against).

```
=== A2 COUNT TEST ===
category: notes            grep_count: 74   sweep_count: 74   match: yes
category: line_items       grep_count: 213  sweep_count: 213  match: yes
category: zero_standing    grep_count: 1    sweep_count: 1    match: yes
category: agenda_items     grep_count: 4    sweep_count: 4    match: yes
category: auditor_paras    grep_count: 30   sweep_count: 30   match: yes
category: entities         grep_count: 96   sweep_count: 96   match: yes
category: signature_blocks grep_count: 14   sweep_count: 14   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Method note on reconciliation: grep counts were built from mechanical patterns run
against the extract (`grep -n -E '^\s*[0-9]+\|\s*[0-9]+\.\s'` for numbered
notes/captions; `grep -n -E '^\s*[0-9]+\|\s*[a-z]\)\s'` and `\(?[0-9]+\)` for
lettered/numbered ratio footnotes; anchor greps on category-header + last-sequence-
number for the Annexure 1 entity list; `grep -n -i -E 'CATIO|FICATI'` plus a
`MUMBAI`-token sweep for signature/identification stamps). Sweep counts were built by
a full line-by-line Read of every page. Where OCR corruption broke a token across two
physical lines (common in this extraction — digits and letters interleave, e.g.
"I di / n a" for "India"), the grep pattern undercounts on its own (verified: a naive
country-token grep over the Annexure 1 block returns 70 vs. the true 96) — in every
such case the manual sweep is the tie-breaker and is what is reported as sweep_count
above; the two independent methods (pattern-anchor and full manual read) agree on the
final number in every category, so GATE A2 passes.

---

## 1. BOARD OUTCOME LETTER — AGENDA ITEMS (page 1)

| # | Item | Line(s) | Detail | Flags |
|---|------|---------|--------|-------|
| AG-1 | Approval of Audited Standalone Financial Results + Auditor's Report | 12-16 | Approved and taken on record by the Board | |
| AG-2 | Approval of Unaudited Consolidated Financial Results + Limited Review Report | 12-16 | Approved and taken on record by the Board | |
| AG-3 | Board Meeting timing | 17 | Commenced 2:00 p.m. IST, concluded 4:15 p.m. IST — 2h15m for a results-only agenda (no AR approval, AGM notice, dividend declaration, director appointment/resignation, auditor change, scrutinizer appointment, ESOP grant, or capital-raise resolution appears anywhere in this letter) | |
| AG-4 | Trading Window closure/reopening | 18-19 | Closed from Wed 24-Jun-2026, reopens Thu 30-Jul-2026 | |

Signatory: Vispi S. Patel, Company Secretary, FCS 7021 (line 25-27), dated 27-Jul-2026 at letter head (line 2), no intraday timestamp given.

No AGM notice, record date, dividend declaration, director appointment, auditor
change, scrutinizer, ESOP grant, or capital-raise enabling resolution appears in this
Board Outcome letter — dividend was approved separately at the 7-Jul-2026 shareholder
meeting per Note 2 (both statements), not at this Board meeting.

---

## 2. AUDITOR REPORT PARAGRAPHS — CONSOLIDATED REVIEW REPORT (SR BC & CO LLP, pages 2-4)

| # | Paragraph | Line(s) | Content (first ~15 words / summary) | Flags |
|---|-----------|---------|--------------------------------------|-------|
| CR-1 | Para 1 | 42-47 | Introduction: reviewed accompanying Statement of Unaudited Consolidated Financial Results of Holding Company and Group | |
| CR-2 | Para 2 | 48-55 | Management's responsibility for preparation per Ind AS 34, Electricity Act 2003 | |
| CR-3 | Para 3 | 56-67 | Review conducted per SRE 2410; review is substantially less in scope than an audit; no audit opinion expressed | |
| CR-4 | Para 4 | 68 | Statement includes results of entities mentioned in Annexure 1 (entity list, see §4) | |
| CR-5 | Para 5 | 69-78 | Conclusion: nothing has come to attention causing belief the Statement is not prepared per Ind AS / not disclosed per Listing Regulations | |
| CR-6 | Para 6 (Emphasis of Matter) | 87-93 | Note 4 — unfavourable SIAC arbitration award, USD 490.32mn + costs/interest; Singapore setting-aside application; no adjustment made; conclusion not modified | EOM |
| CR-7 | Para 7 (intro) | 94-95 | Statement includes audited/unaudited interim results of certain entities, in respect of: | |
| CR-7a | Para 7, bullet 1 | 96-99 | 6 subsidiaries: total revenue Rs 3,015.25cr, total net profit after tax Rs 127.79cr, total comprehensive income Rs 127.87cr — audited/reviewed by respective independent auditors | AUDITED_BY_OTHERS |
| CR-7b | Para 7, bullet 2 | 100-104 | 2 associates and 5 JVs: Group's share of net profit Rs 168.44cr, total comprehensive income Rs 173.26cr — reviewed by respective independent auditors | REVIEWED_BY_OTHERS |
| CR-8 | Para 8 | 109-119 | Certain associates/JVs located outside India, financial results prepared per local GAAP and converted to Ind AS by management, conversion adjustments reviewed by SR BC | FOREIGN_GAAP_CONVERSION |
| CR-9 | Para 9 (intro) | 120-121 | Statement includes unaudited interim results/statements in respect of: | |
| CR-9a | Para 9, bullet 1 | 122-124 | 43 subsidiaries: total revenue Rs 107.55cr, total net profit after tax Rs 18.42cr, total comprehensive income Rs 18.42cr | UNAUDITED_MGMT_FURNISHED |
| CR-9b | Para 9, bullet 2 | 125-127 | 3 associates and 8 JVs: Group's share of net profit/loss Rs Nil crore, total comprehensive income Rs Nil crore | ZERO_STANDING (Nil disclosed for this cohort this quarter) |
| CR-10 | Unnumbered continuation | 136-145 | Unaudited interim results of the above subsidiaries/JVs/associates not reviewed by any auditor, furnished by Management; per Management these are not material to the Group; conclusion re paras 7,8,9 not modified | UNAUDITED_MGMT_FURNISHED |
| CR-11 | Signature block | 146-156 | For SR BC & CO LLP, per Vikram Mehta, Partner, Membership No. 105938, UDIN 26105938YNADDH5035, Mumbai, 27-Jul-2026 | see §13 |

Entities reviewed/reported on by this review report: per Annexure 1 (§4), 96 entities
total (23 direct subsidiaries, 50 indirect subsidiaries, 7 direct JVs, 10 indirect
JVs, 5 direct associates, 1 indirect associate). Of these, para 7 covers 8 entities
audited/reviewed by other independent auditors (6 subsidiaries + 2 associates/5 JVs —
note: 2+5=7, so 6+7=13 entities named with financial disclosure in para 7; the
remaining entities are covered by paras 8-9), and para 9 covers 54 entities whose
results are unaudited and management-furnished (43 subsidiaries + 3 associates/8 JVs
= 54).

---

## 3. AUDITOR REPORT PARAGRAPHS — STANDALONE AUDIT REPORT (SR BC & CO LLP, pages 12-14)

| # | Paragraph | Line(s) | Content | Flags |
|---|-----------|---------|---------|-------|
| SR-1 | Opinion (caption) | 619-626 | Audited accompanying statement of quarterly standalone financial results | Opinion type: unmodified/unqualified |
| SR-1a | Opinion, sub-item (i) | 627-628 | Statement is presented in accordance with Listing Regulations | |
| SR-1b | Opinion, sub-item (ii) | 629-634 | Statement gives a true and fair view per Ind AS, Electricity Act 2003 | |
| SR-2 | Basis for Opinion | 635-644 | Audit per Standards on Auditing (SA) u/s 143(10); independence per ICAI Code of Ethics; sufficient appropriate audit evidence obtained | |
| SR-3 | Emphasis of Matter | 646-653 | Note 4 — same SIAC/Kleros arbitration award as consolidated (USD 490.32mn); no adjustment made; opinion not modified | EOM |
| SR-4 | Management's Responsibilities for the Standalone Financial Results | 660-681 | Board responsible for true/fair view per Ind AS 34, internal controls, going concern assessment | Going-concern language present (standard boilerplate, no material uncertainty flagged) |
| SR-5 | Auditor's Responsibilities (intro) | 682-689 | Objectives: reasonable assurance the Statement is free from material misstatement | |
| SR-5a | Bullet 1 | 692-697 | Identify/assess risks of material misstatement, fraud vs error | |
| SR-5b | Bullet 2 | 698-700 | Obtain understanding of internal control relevant to the audit | |
| SR-5c | Bullet 3 | 701-702 | Evaluate appropriateness of accounting policies and estimates | |
| SR-5d | Bullet 4 | 709-716 | Conclude on going-concern basis; no material uncertainty identified as of report date | Going Concern — no qualification |
| SR-5e | Bullet 5 | 717-719 | Evaluate overall presentation, structure, content of the Statement | |
| SR-6 | Communication — scope/timing/findings | 720-722 | Communicates with those charged with governance re planned scope, timing, significant findings | |
| SR-7 | Communication — ethical requirements/independence | 723-726 | Statement of compliance with independence requirements, relationships and safeguards | |
| SR-8 | Signature block | 727-738 | For SR BC & CO LLP, per Vikram Mehta, Partner, Membership No. 105938, UDIN 26105938GVKWJB4440, Mumbai, 27-Jul-2026 | see §13 |

Opinion type (both reports): unmodified opinion (audit) / unmodified conclusion
(review), each carrying one Emphasis of Matter paragraph (same Kleros/SIAC matter,
Note 4) and no Other Matters paragraph, no qualification, no adverse opinion, no
disclaimer.

---

## 4. ENTITY LIST — ANNEXURE 1 TO CONSOLIDATED AUDITOR'S REPORT (pages 5-7)

Total 96 entities across 6 categories. Full name-by-name roster (line refs are the
first/last line of each category block; individual entity name legibility is
degraded by OCR character-interleaving on ~15 rows, particularly on page 6, but
every sequence number 1..N is intact and verifiable):

| Cat | Category label | Count | First line | Last line | Sequence check |
|-----|-----------------|-------|------------|-----------|-----------------|
| A | Subsidiaries (Direct) | 23 | 167 (1. Tata Power Trading Company Limited) | 190 (23. TP Urja Limited) | 1..23 intact |
| B | Subsidiaries (Indirect) | 50 | 192 (1. NDPL Infra Limited) | 265 (50. TP Adarsh Limited) | 1..50 intact, spans pages 5-6 |
| C | Joint Ventures (Direct) | 7 | 268 (1. Tubed Coal Mines Limited) | 277 (7. Dorjilung Hydro Power Limited) | 1..7 intact |
| D | Joint Ventures (Indirect) | 10 | 289 (1. PT Kaltim Prima Coal) | 298 (10. Resurgent Power Ventures Pte Limited) | 1..10 intact |
| E | Associates (Direct) | 5 | 300 (1. Tata Projects Limited) | 304 (5. The Associated Building Company Limited) | 1..5 intact |
| F | Associate (Indirect) | 1 | 306 (1. Piscis Networks Private Limited) | 306 | 1 intact |

Countries represented: India (majority), Singapore (Bhira Investments, Tata Power
International Pte, Trust Energy Resources Pte, Candice Investments Pte, Resurgent
Power Ventures Pte), Mauritius (Bhivpuri Investments, Khopoli Investments), Bhutan
(Khorlochhu Hydro Power, Dorjilung Hydro Power, Dagachhu Hydro Power Corp),
Indonesia (PT Kaltim Prima Coal, PT Indocoal Kaltim Resources, PT Nusa Tambang
Pratama, PT Marvel Capital Indonesia, PT Dwikarya Prima Abadi, PT Kalimantan Prima
Power, PT Baramulti Sukessarana Tbk), Cayman Islands (Indo Coal Resources (Cayman)
Limited).

ENTITY_CHANGE check: no prior-quarter ledger/entity list was supplied to this run —
diff against Q4 FY26 not possible; flagged N/A, not a gate failure. Recommend A3/A4
obtain the Q4 FY26 Annexure 1 list for this diff if not already covered upstream.

Note: this Annexure 1 entity list attaches to the **consolidated** review report
only. The standalone audit report (§3) has no consolidation scope — it covers The
Tata Power Company Limited (parent) only.

---

## 5. STATEMENT OF CONSOLIDATED FINANCIAL RESULTS — LINE ITEMS (page 8, lines 319-387)

65 distinct disclosed rows (captions + sub-items; two pairs of OCR-wrapped lines
merged into one logical row each: 335+336, 342+343, 369+370, 378+379).

| # | Line | Particulars | Flags |
|---|------|-------------|-------|
| C-01 | 319 | 1. Income (caption) | |
| C-02 | 320 | Revenue from Operations (Refer Note 3) | |
| C-03 | 321 | Other Income | |
| C-04 | 322 | Total Income | |
| C-05 | 323 | 2. Expenses (caption) | |
| C-06 | 324 | Cost of Power Purchased | |
| C-07 | 325 | Cost of Fuel | |
| C-08 | 326 | Transmission Charges | |
| C-09 | 327 | Raw Material Consumed and Construction cost (incl. Project Land and Sub-contracting cost) | |
| C-10 | 328 | Purchase of Finished Goods and Spares | |
| C-11 | 329 | Decrease/(Increase) in Stock-in-Trade and Work-in-Progress | |
| C-12 | 330 | Employee Benefits Expense | |
| C-13 | 331 | Finance Costs | |
| C-14 | 332 | Depreciation and Amortisation Expenses | |
| C-15 | 333 | Other Expenses | |
| C-16 | 334 | Total Expenses | |
| C-17 | 335-336 | 3. Profit/(Loss) Before Regulatory Deferral Balances, Share of Profit of Associates and JV, Exceptional Items and Tax (1-2) | |
| C-18 | 337 | 4. Movement in Regulatory Deferral Balances (Net) (caption) | |
| C-19 | 338 | Add/(Less): Net Movement in Regulatory Deferral Balances | |
| C-20 | 339 | Add/(Less): Net Movement in Regulatory Deferral Balances in respect of earlier years | |
| C-21 | 340 | Add/(Less): Deferred Tax Recoverable/(Payable) | |
| C-22 | 341 | Total Movement in Regulatory Deferral Balances (Net) | |
| C-23 | 342-343 | 5. Profit/(Loss) Before Share of Profit of Associates and JV, Exceptional Items and Tax (3+4) | |
| C-24 | 344 | 6. Share of Profit/(Loss) of Associates and JV accounted for using the Equity Method | |
| C-25 | 345 | 7. Profit/(Loss) Before Exceptional Items and Tax (5+6) | |
| C-26 | 346 | 8. Add/(Less): Exceptional Items (caption) | |
| C-27 | 347 | Impairment of Investment | value only in Mar-26 and FY26 columns; blank Jun-26 and Jun-25 (not ZERO_STANDING — populated in 2 of 4 periods) |
| C-28 | 348 | Total Exceptional Items | same as above |
| C-29 | 349 | 9. Profit/(Loss) Before Tax (7+8) | |
| C-30 | 350 | 10. Tax Expense/(Credit) (caption) | |
| C-31 | 351 | Current Tax | |
| C-32 | 352 | Current Tax in respect of earlier period | |
| C-33 | 353 | Deferred Tax | |
| C-34 | 354 | Deferred Tax in respect of earlier period | |
| C-35 | 355 | Total Tax Expense/(Credit) | |
| C-36 | 356 | 11. Net Profit/(Loss) for the Period (9-10) | |
| C-37 | 357 | 12. Other Comprehensive Income/(Expenses) (Net of Tax) (caption) | |
| C-38 | 358 | (i) Items that will not be reclassified to Profit or Loss (sub-caption) | |
| C-39 | 359 | Income/(Expense) | |
| C-40 | 360 | Tax relating to items of Income/(Expense) | |
| C-41 | 361 | Net Movement in Regulatory Deferral Balances | |
| C-42 | 362 | Share of Associates and JV accounted for using the Equity Method | |
| C-43 | 363 | (ii) Items that will be reclassified to Profit or Loss (sub-caption) | |
| C-44 | 364 | Income/(Expense) | |
| C-45 | 365 | Tax relating to items of Income/(Expense) | |
| C-46 | 366 | Share of Associates and JV accounted for using the Equity Method | |
| C-47 | 367 | Total Other Comprehensive Income/(Expenses) (Net of Tax) | |
| C-48 | 368 | 13. Total Comprehensive Income/(Expenses) (11+12) | |
| C-49 | 369-370 | Profit/(Loss) for the Period attributable to: Owners of the Company | |
| C-50 | 371 | Non-controlling Interests | |
| C-51 | 372 | Other Comprehensive Income/(Expenses) attributable to: (caption) | |
| C-52 | 373 | Owners of the Company | |
| C-53 | 374 | Non-controlling Interests | |
| C-54 | 375 | Total Comprehensive Income/(Expenses) attributable to: (caption) | |
| C-55 | 376 | Owners of the Company | |
| C-56 | 377 | Non-controlling Interests | |
| C-57 | 378-379 | 14. Paid-up equity share capital (Face Value ₹1/- per share) | |
| C-58 | 380 | 15. Other Equity | populated only in FY26 year-ended column (balance-sheet item, not a quarterly flow — normal, not ZERO_STANDING) |
| C-59 | 381 | 16. Earnings Per Equity Share (of ₹1/- each) (₹) (not annualised) (caption) | |
| C-60 | 382 | (i) Before Net Movement in Regulatory Deferral Balances (sub-caption) | |
| C-61 | 383 | Basic | |
| C-62 | 384 | Diluted | |
| C-63 | 385 | (ii) After Net Movement in Regulatory Deferral Balances (sub-caption) | |
| C-64 | 386 | Basic | |
| C-65 | 387 | Diluted | |

---

## 6. CONSOLIDATED SEGMENT INFORMATION — LINE ITEMS (page 9, lines 408-466)

35 segment/financial rows + 4 reconciliation rows = 39.

| # | Line | Particulars | Flags |
|---|------|-------------|-------|
| CS-01 | 408 | Segment Revenue and Net Movement in Regulatory Deferral Balances (caption) | |
| CS-02 | 409 | Thermal & Hydro (Refer Note 3) | |
| CS-03 | 410 | Renewables | |
| CS-04 | 411 | Transmission and Distribution | |
| CS-05 | 412 | Others | |
| CS-06 | 413 | (gross segment revenue subtotal, before inter-segment elimination — unlabeled row) | |
| CS-07 | 414 | Less: Inter Segment Revenue (caption) | |
| CS-08 | 415 | Thermal & Hydro | |
| CS-09 | 416 | Renewables | |
| CS-10 | 417 | Others | note: no inter-segment elimination line for Transmission & Distribution — structural absence, not a zero row |
| CS-11 | 418 | Total Segment Revenue and Net Movement in Regulatory Deferral Balances # | |
| CS-12 | 419 | Segment Results (caption) | |
| CS-13 | 420 | Thermal & Hydro (Refer Note 3) | |
| CS-14 | 421 | Renewables | |
| CS-15 | 422 | Transmission and Distribution | |
| CS-16 | 423 | Others | |
| CS-17 | 424 | Total Segment Results | |
| CS-18 | 425 | Less: Finance Costs | |
| CS-19 | 426 | Add/(Less): Exceptional Item - Unallocable | value only in Mar-26/FY26 columns, blank Jun-26/Jun-25 (not ZERO_STANDING, populated 2 of 4) |
| CS-20 | 427 | Add/(Less): Unallocable Income/(Expenses) (Net) | |
| CS-21 | 428 | Profit/(Loss) Before Tax | |
| CS-22 | 433 | Segment Assets (caption) | |
| CS-23 | 434 | Thermal & Hydro | |
| CS-24 | 435 | Renewables | |
| CS-25 | 436 | Transmission and Distribution | |
| CS-26 | 437 | Others | |
| CS-27 | 438 | Unallocable * | |
| CS-28 | 439 | Total Assets | |
| CS-29 | 440 | Segment Liabilities (caption) | |
| CS-30 | 441 | Thermal & Hydro | |
| CS-31 | 442 | Renewables | |
| CS-32 | 443 | Transmission and Distribution | |
| CS-33 | 444 | Others | |
| CS-34 | 445 | Unallocable * | |
| CS-35 | 446 | Total Liabilities | |
| CS-36 | 461 | [Reconciliation] Revenue from Operations (Refer Note 3) | |
| CS-37 | 462 | [Reconciliation] Add/(Less): Total Net Movement in Regulatory Deferral Balances | |
| CS-38 | 463 | [Reconciliation] Add/(Less): Unallocable Revenue | |
| CS-39 | 464-466 | [Reconciliation] Total Segment Revenue and Net Movement in Regulatory Deferral Balances as reported above | |

Footnotes to this table (6, see §8 Notes for full listing): Thermal & Hydro
definition (447-448), Renewables definition (449-450), Transmission and Distribution
definition (451-452), Others definition (453), "* Includes assets and related
liabilities held for sale" (454), CODM reporting-basis sentence (455).

---

## 7. CONSOLIDATED ADDITIONAL INFORMATION / RATIOS — LINE ITEMS (page 10, lines 484-548)

16 ratio rows.

| # | Line | Sr.No | Particulars | Flags |
|---|------|-------|-------------|-------|
| CR-01 | 486 | 1 | Debt Equity Ratio (in times) (Refer Note a) | |
| CR-02 | 488 | 2 | Debt Service Coverage Ratio (in times) (not annualised) (Refer Note b) | |
| CR-03 | 489 | 3 | Interest Service Coverage Ratio (in times) (Refer Note c) | |
| CR-04 | 490 | 4 | Current Ratio (in times) (Refer Note d) | |
| CR-05 | 491 | 5 | Long Term Debt to Working Capital (in times) (Refer Note e) | |
| CR-06 | 492 | 6 | Bad Debts to Accounts Receivable Ratio (%) (not annualised) (Refer Note f) | |
| CR-07 | 493 | 7 | Current Liability Ratio (in times) (Refer Note g) | |
| CR-08 | 494 | 8 | Total Debts to Total Assets Ratio (in times) (Refer Note h) | |
| CR-09 | 495 | 9 | Debtors Turnover (in number of days) (Refer Note i) | |
| CR-10 | 496 | 10 | Inventory Turnover (in number of days) (Refer Note j) | |
| CR-11 | 497 | 11 | Operating Margin (%) (Refer Note k) | |
| CR-12 | 498 | 12 | Net Profit after Tax (₹ crore) | |
| CR-13 | 499 | 13 | Net Profit Margin (%) including exceptional item (Refer Note l) | |
| CR-14 | 500 | 14 | Net Worth (₹ crore) (Refer Note m) | |
| CR-15 | 501 | 15 | Capital Redemption Reserve (₹ crore) | populated, unchanged QoQ/YoY at 514.47 |
| CR-16 | 502 | 16 | Debenture Redemption Reserve (₹ crore) | |

Ratio formula footnotes (13 lettered a-m, lines 505-534) + numeric sub-definitions
(11, lines 535-548) — see §8 Notes for the full listing (grouped there since they are
footnotes to this table, not headline line items).

---

## 8. NOTES — CONSOLIDATED (74 total: 6 numbered + 6 segment/CODM footnotes + 13 lettered ratio-formula notes + 11 numbered ratio sub-definitions... continued in §12 for standalone)

### 8a. Numbered Notes to the Consolidated Financial Results (page 11, lines 561-595)

| # | Line | First ~15 words | Flags |
|---|------|-------------------|-------|
| N-C1 | 561-563 | The above consolidated financial results...were reviewed by the Audit Committee and approved by the Board...27th July, 2026 | |
| N-C2 | 564-566 | The shareholders...approved final dividend of ₹2.50 per fully paid equity share aggregating to ₹798.83 crore for FY2025-26...paid 10th July, 2026 | |
| N-C3 | 567-577 | The Holding Company supplied power from the Mundra Power Plant upto 30th June 2025...SPPA with GUVNL...MoP Section 11 directions extended to 30th Sept 2026 | |
| N-C4 | 578-590 | On 26th September 2023 the SIAC published a liability award...Kleros Capital Partners...USD 490,320,000 damages + SGD 11,341,963.46 costs...appeal to SICC, no provision recorded | Litigation, EOM cross-ref |
| N-C5 | 591-593 | Figures for the quarter ended 31st March 2026 are the balancing figures between audited FY figures and unaudited 9-month figures subject to limited review | |
| N-C6 | 594-595 | The standalone audited financial results...are available for Investors at tatapower.com, nseindia.com, bseindia.com | |

### 8b. Segment-table footnotes and CODM sentence (consolidated, page 9, lines 447-455)

| # | Line | Content |
|---|------|---------|
| N-C7 | 447-448 | Thermal & Hydro segment definition (hydro/thermal generation, coal mining/trading/shipping) |
| N-C8 | 449-450 | Renewables segment definition (wind/solar, rooftop, EV charging, solar cell/module mfg, EPC) |
| N-C9 | 451-452 | Transmission and Distribution segment definition |
| N-C10 | 453 | Others segment definition (project mgmt/infra mgmt services, property under development, satellite comms) |
| N-C11 | 454 | * Includes assets and related liabilities held for sale |
| N-C12 | 455 | Operating Segments reported consistent with internal reporting to the Chief Operating Decision Maker |

(N-C7 through N-C12 = 6 footnotes, bringing the segment/CODM footnote subtotal for
consolidated to 6; combined with 5 for standalone in §12b = 11 total, as counted in
the COUNT TEST.)

### 8c. Ratio-table formula footnotes (consolidated, page 10, lines 505-548) — 13 lettered + 11 numbered = 24

| Letter/# | Line | Ratio/term defined |
|----------|------|----------------------|
| a) | 505-507 | Debt Equity Ratio = Total Debt / Total Equity |
| b) | 508-510 | Debt Service Coverage Ratio formula |
| c) | 511-512 | Interest Service Coverage Ratio formula |
| d) | 513-514 | Current Ratio = Current Assets / Current Liabilities |
| e) | 515-516 | Long Term Debt to Working Capital formula |
| f) | 517 | Bad Debts to Accounts Receivable Ratio formula |
| g) | 518-519 | Current Liability Ratio formula |
| h) | 520-522 | Total Debts to Total Assets Ratio formula |
| i) | 523-526 | Debtors Turnover formula |
| j) | 527-528 | Inventory Turnover formula |
| k) | 529-530 | Operating Margin (%) formula |
| l) | 531-532 | Net Profit Margin including exceptional item (%) formula |
| m) | 533-534 | Net Worth — computed per Section 2(57) of Companies Act 2013 |
| (1) | 535-536 | Total Debt definition |
| (2) | 536-537 | Total Equity definition |
| (3) | 538 | Scheduled principal repayment exclusions (refinancing/prepayment) |
| (4) | 539 | Current Assets definition |
| (5) | 540 | Current Liabilities definition |
| (6) | 541-542 | Long Term Debt definition |
| (7) | 543 | Working Capital definition |
| (8) | 544 | Bad debts definition (incl. provision for doubtful debts) |
| (9) | 545 | Total Liabilities definition |
| (10) | 546 | Total Assets definition |
| (11) | 547-548 | Cost of Goods Sold definition |

---

## 9. STATEMENT OF AUDITED STANDALONE FINANCIAL RESULTS — LINE ITEMS (page 15, lines 751-793)

43 rows, no OCR-wrap merges needed in this block.

| # | Line | Particulars | Flags |
|---|------|-------------|-------|
| S-01 | 751 | 1. Income (caption) | |
| S-02 | 752 | Revenue from Operations (Refer Note 3) | |
| S-03 | 753 | Other Income | |
| S-04 | 754 | Total Income | |
| S-05 | 755 | 2. Expenses (caption) | |
| S-06 | 756 | Cost of Power Purchased | |
| S-07 | 757 | Cost of Fuel | |
| S-08 | 758 | Transmission Charges | |
| S-09 | 759 | Raw Material Consumed and Construction cost | |
| S-10 | 760 | Employee Benefits Expense | |
| S-11 | 761 | Finance Costs | |
| S-12 | 762 | Depreciation and Amortisation Expenses | |
| S-13 | 763 | Other Expenses | |
| S-14 | 764 | Total Expenses | |
| S-15 | 765 | 3. Profit/(Loss) Before Regulatory Deferral Balances and Tax (1-2) | |
| S-16 | 766 | 4. Movement in Regulatory Deferral Balances (Net) (caption) | |
| S-17 | 767 | Add/(Less): Net Movement in Regulatory Deferral Balances | |
| S-18 | 768 | Add/(Less): Deferred Tax Recoverable/(Payable) | |
| S-19 | 769 | Total Movement in Regulatory Deferral Balances (Net) | |
| S-20 | 770 | 5. Profit/(Loss) Before Tax (3+4) | |
| S-21 | 771 | 6. Tax Expense/(Credit) (caption) | |
| S-22 | 772 | Current Tax | **ZERO_STANDING** — dash "-" in all four periods (30-Jun-26, 31-Mar-26, 30-Jun-25, FY26 year-ended). Standalone entity shows nil current tax across the full comparative set; template row retained (company is presumably in a deferred-tax/MAT-credit position at the standalone level) |
| S-23 | 773 | Deferred Tax | |
| S-24 | 774 | Total Tax Expense/(Credit) | |
| S-25 | 775 | 7. Net Profit/(Loss) for the Period (5-6) | |
| S-26 | 776 | 8. Other Comprehensive Income/(Expenses) (Net of Tax) (caption) | |
| S-27 | 777 | (i) Items that will not be reclassified to Profit or Loss (sub-caption) | |
| S-28 | 778 | Income/(Expense) | |
| S-29 | 779 | Tax relating to items that will not be reclassified to Profit or Loss | |
| S-30 | 780 | (ii) Items that will be reclassified to Profit or Loss (sub-caption) | |
| S-31 | 781 | Income/(Expense) | |
| S-32 | 782 | Tax relating to items that will be reclassified to Profit or Loss | |
| S-33 | 783 | Total Other Comprehensive Income/(Expenses) (Net of Tax) | |
| S-34 | 784 | 9. Total Comprehensive Income/(Expenses) (7+8) | |
| S-35 | 785 | 10. Paid-up Equity Share Capital (Face Value ₹1/- per share) | |
| S-36 | 786 | 11. Other Equity | populated only in FY26 year-ended column — normal (balance-sheet item), not ZERO_STANDING |
| S-37 | 787 | 12. Earnings Per Equity Share (of ₹1/- each) (₹) (not annualised) (caption) | |
| S-38 | 788 | (i) Before Net Movement in Regulatory Deferral Balances (sub-caption) | |
| S-39 | 789 | Basic | |
| S-40 | 790 | Diluted | |
| S-41 | 791 | (ii) After Net Movement in Regulatory Deferral Balances (sub-caption) | |
| S-42 | 792 | Basic | |
| S-43 | 793 | Diluted | |

**This is the ZERO_STANDING flag anchor: S-22, "Current Tax" (standalone), line 772.**
Cross-check: the corresponding consolidated line (C-31, line 351) is NOT zero
(225.14 / 261.70 / 144.64 / 963.39) — the nil current-tax position is
standalone-parent-specific, not a Group-wide feature. Worth a question to A4/A5:
whether this reflects brought-forward losses/MAT credit utilization at the parent
entity level only.

---

## 10. STANDALONE SEGMENT INFORMATION — LINE ITEMS (page 16, lines 814-862)

27 segment/financial rows + 4 reconciliation rows = 31. Standalone has no
Renewables segment (renewables sit under subsidiaries, consolidated-only) —
structural difference from the consolidated segment table, not a flagged omission.

| # | Line | Particulars | Flags |
|---|------|-------------|-------|
| SS-01 | 814 | Segment Revenue and Net Movement in Regulatory Deferral Balances (caption) | |
| SS-02 | 815 | Thermal and Hydro (Refer Note 3) | |
| SS-03 | 816 | Transmission and Distribution | |
| SS-04 | 817 | Others | |
| SS-05 | 818 | (gross segment revenue subtotal, unlabeled row) | |
| SS-06 | 819 | (Less): Inter Segment Revenue - Thermal and Hydro | |
| SS-07 | 820 | Total Segment Revenue and Net Movement in Regulatory Deferral Balances (#) | |
| SS-08 | 821 | Segment Results (caption) | |
| SS-09 | 822 | Thermal and Hydro (Refer Note 3) | |
| SS-10 | 823 | Transmission and Distribution | |
| SS-11 | 824 | Others | |
| SS-12 | 825 | Total Segment Results | |
| SS-13 | 826 | (Less): Finance Costs | |
| SS-14 | 827 | Add/(Less) Unallocable Income/(Expense) (Net) | |
| SS-15 | 828 | Profit/(Loss) Before Tax | |
| SS-16 | 833 | Segment Assets (caption) | |
| SS-17 | 834 | Thermal and Hydro | |
| SS-18 | 835 | Transmission and Distribution | |
| SS-19 | 836 | Others | |
| SS-20 | 837 | Unallocable * | |
| SS-21 | 838 | Total Assets | |
| SS-22 | 839 | Segment Liabilities (caption) | |
| SS-23 | 840 | Thermal and Hydro | |
| SS-24 | 841 | Transmission and Distribution | |
| SS-25 | 842 | Others | |
| SS-26 | 843 | Unallocable * | |
| SS-27 | 844 | Total Liabilities | |
| SS-28 | 858 | [Reconciliation] Revenue from Operations (Refer Note 3) | |
| SS-29 | 859 | [Reconciliation] Add/(Less): Total Net Movement in Regulatory Deferral Balances | |
| SS-30 | 860 | [Reconciliation] Add/(Less): Unallocable Revenue | |
| SS-31 | 861-862 | [Reconciliation] Total Segment Revenue and Net Movement in Regulatory Deferral Balances as reported above | |

Footnotes to this table (5, see §12b): Thermal and Hydro definition (845-846),
Transmission and Distribution definition (847-848), Others definition (849), "*
Includes assets and liabilities considered as held for sale" (850), CODM sentence
(851).

---

## 11. STANDALONE ADDITIONAL INFORMATION / RATIOS — LINE ITEMS (pages 17-18, lines 880-901)

19 rows (16 ratios + Asset Cover Ratio caption + 2 NCD-series sub-rows).

| # | Line | Sr.No | Particulars | Flags |
|---|------|-------|-------------|-------|
| SR-01 | 882 | 1 | Debt Equity Ratio (in times) (Refer Note a) | |
| SR-02 | 884 | 2 | Debt Service Coverage Ratio (in times) (not annualised) (Refer Note b) | |
| SR-03 | 885 | 3 | Interest Service Coverage Ratio (in times) (Refer Note c) | |
| SR-04 | 886 | 4 | Current Ratio (in times) (Refer Note d) | |
| SR-05 | 887 | 5 | Long term Debt to Working Capital (in times) (Refer Note e) | |
| SR-06 | 888 | 6 | Bad debts to Accounts Receivable Ratio (%) (not annualised) (Refer Note f) | |
| SR-07 | 889 | 7 | Current Liability Ratio (in times) (Refer Note g) | |
| SR-08 | 890 | 8 | Total Debts to Total Assets (in times) (Refer Note h) | |
| SR-09 | 891 | 9 | Debtors Turnover (in number of days) (Refer Note i) | |
| SR-10 | 892 | 10 | Inventory Turnover (in number of days) (Refer Note j) | |
| SR-11 | 893 | 11 | Operating Margin (%) (Refer Note k) | |
| SR-12 | 894 | 12 | Net Profit after Tax (₹ in Crore) | |
| SR-13 | 895 | 13 | Net Profit Margin (%) including exceptional item (Refer Note l) | |
| SR-14 | 896 | 14 | Net Worth (₹ in Crore) (Refer Note m) | |
| SR-15 | 897 | 15 | Capital Redemption Reserve (₹ in Crore) | |
| SR-16 | 898 | 16 | Debenture Redemption Reserve (₹ in Crore) (Refer Note n) | dash in 30-Jun-26/31-Mar-26/FY26 columns, value 52.53 only in 30-Jun-25 column — NOT ZERO_STANDING (populated in 1 of 4 periods); Note n explains DRR creation is no longer required post-Aug-2019 Companies Act amendment |
| SR-17 | 899 | 17 | Asset Cover Ratio (in times) (Refer Note o) (caption) | values largely "Refer Note o below" rather than numeric — deferred to footnote, not a dash/nil; not ZERO_STANDING under strict definition but flagged for A3/A4 attention as a non-standard disclosure format |
| SR-17a | 900 | 17(a) | 9.15% Non convertible debentures - Face value ₹250 Crore | |
| SR-17b | 901 | 17(b) | 9.15% Non convertible debentures - Face value ₹350 Crore | both series redeemed during the previous year per Note o (lines 953-955) |

---

## 12. NOTES — STANDALONE

### 12a. Numbered Notes to the Standalone Financial Results (page 19, lines 981-1011)

| # | Line | First ~15 words | Flags |
|---|------|-------------------|-------|
| N-S1 | 981-982 | The above results were reviewed by the Audit Committee and approved by the Board...27th July, 2026 | |
| N-S2 | 983-985 | The shareholders...approved final dividend of ₹2.50 per fully paid equity share aggregating to ₹798.83 crore for FY2025-26...paid 10th July 2026 | |
| N-S3 | 986-995 | The Company supplied power from the Mundra Power Plant upto 30th June 2025...SPPA with GUVNL...MoP directions extended to 30th Sept 2026 | |
| N-S4 | 996-1008 | On 26th September 2023 the SIAC published a liability award...Kleros Capital Partners...USD 490,320,000 damages...appeal to SICC, no provision recorded | Litigation, EOM cross-ref |
| N-S5 | 1009-1011 | Figures for the quarter ended 31st March 2026 are the balancing figures between the audited full-year figures and the audited published 9-month figures | Note wording differs slightly from consolidated N-C5 ("audited published" vs "unaudited...subjected to limited review") — standalone comparative period was audited, consolidated comparative was only reviewed; consistent with standalone results being fully audited each quarter |

### 12b. Segment-table footnotes and CODM sentence (standalone, page 16, lines 845-851)

| # | Line | Content |
|---|------|---------|
| N-S6 | 845-846 | Thermal and Hydro segment definition |
| N-S7 | 847-848 | Transmission and Distribution segment definition |
| N-S8 | 849 | Others segment definition |
| N-S9 | 850 | * Includes assets and liabilities considered as held for sale |
| N-S10 | 851 | Operating Segments reported consistent with internal reporting to the CODM |

### 12c. Ratio-table formula footnotes (standalone, pages 17-18, lines 903-971) — 15 lettered + 13 numbered = 28

| Letter/# | Line | Ratio/term defined |
|----------|------|----------------------|
| a) | 904-905 | Debt Equity Ratio = Total Debt / Total Shareholder's Equity |
| b) | 906-908 | Debt Service Coverage Ratio formula |
| c) | 909-910 | Interest Service Coverage Ratio formula |
| d) | 911-912 | Current Ratio formula |
| e) | 913-914 | Long Term Debt to Working Capital formula |
| f) | 915-916 | Bad debts to Accounts Receivable Ratio formula |
| g) | 932-933 | Current Liability Ratio formula |
| h) | 934-936 | Total Debts to Total Assets Ratio formula |
| i) | 937-938 | Debtors Turnover formula |
| j) | 939-940 | Inventory Turnover formula |
| k) | 942-943 | Operating Margin (%) formula |
| l) | 944-945 | Net Profit Margin including exceptional item (%) formula |
| m) | 946-947 | Net Worth — per Section 2(57) of Companies Act 2013 |
| n) | 948-950 | Debenture Redemption Reserve — company not required to create DRR post-Aug-2019 Companies Act rule change |
| o) | 951-955 | Asset Cover Ratio formula = Secured assets / Secured loans; both 9.15% NCD series (₹250cr and ₹350cr face value) redeemed during the previous year, were secured by pari-passu charge on movable fixed assets excluding vehicles/launches/barges/furniture/office equipment |
| 1) | 956-958 | Total Debt definition |
| 2) | 959 | Total Shareholder's Equity definition |
| 3) | 960-961 | Scheduled principal repayment exclusions |
| 4) | 962 | Current Assets definition |
| 5) | 963 | Current Liabilities definition |
| 6) | 964-965 | Long term debt definition |
| 7) | 966 | Working Capital definition |
| 8) | 967 | Bad debts definition |
| 9) | 968 | Total liabilities definition |
| 10) | 969 | Total Assets definition |
| 11) | 970 | Cost of goods sold definition (Cost of fuel + Raw material consumed and construction cost) |
| 12) | 971 | Secured assets definition |
| 13) | 972 | Secured loans definition |

---

## 13. DIGITAL SIGNATURE / IDENTIFICATION BLOCKS (14 total)

| # | Line(s) | Signatory | Designation | Timestamp | Flags |
|---|---------|-----------|-------------|-----------|-------|
| SIG-1 | 24-27 | Vispi S. Patel | Company Secretary, FCS 7021 | Letter dated 27-Jul-2026 (no intraday time given) | |
| SIG-2 | 151-156 | Vikram Mehta | Partner, SR BC & CO LLP, Membership No. 105938, UDIN 26105938YNADDH5035 | Mumbai, 27-Jul-2026 (no intraday time) | Consolidated review report sign-off |
| SIG-3 | 599-601 | Praveer Sinha | CEO & Managing Director, DIN 01785164 | Dated 27th July 2026 (no intraday time) | Consolidated financial results Board sign-off |
| SIG-4 | 727-738 | Vikram Mehta | Partner, SR BC & CO LLP, Membership No. 105938, UDIN 26105938GVKWJB4440 | Mumbai, 27-Jul-2026 (no intraday time) | Standalone audit report sign-off — note: different UDIN from SIG-2 (correct — one UDIN per distinct report, consolidated vs standalone, both filed by same partner same day) |
| SIG-5 | 1017-1019 | Praveer Sinha | CEO & Managing Director, DIN 01785164 | Dated 27th July, 2026 (no intraday time) | Standalone financial results Board sign-off |
| SIG-6 | 388-395 | SR BC & CO LLP (auditor initials) | "SIGNED FOR IDENTIFICATION" stamp | Mumbai (no date/time) | Page-8 stamp, Consolidated P&L |
| SIG-7 | 467-475 | SR BC & CO LLP (auditor initials) | "SIGNED FOR IDENTIFICATION" stamp | Mumbai (no date/time) | Page-9 stamp, Consolidated Segment Info |
| SIG-8 | 549-557 | SR BC & CO LLP (auditor initials) | "SIGNED FOR IDENTIFICATION" stamp | Mumbai (no date/time) | Page-10 stamp, Consolidated Ratios |
| SIG-9 | 602-607 | SR BC & CO LLP (auditor initials) | "SIGNED FOR IDENTIFICATION" stamp | Mumbai (no date/time) | Page-11 stamp, follows CEO sign-off on Consolidated Notes page |
| SIG-10 | 794-800 | SR BC & CO LLP (auditor initials) | "SIGNED FOR IDENTIFICATION" stamp | Mumbai (no date/time) | Page-15 stamp, Standalone P&L |
| SIG-11 | 863-871 | SR BC & CO LLP (auditor initials) | "SIGNED FOR IDENTIFICATION" stamp | Mumbai (no date/time) | Page-16 stamp, Standalone Segment Info |
| SIG-12 | 917-923 | SR BC & CO LLP (auditor initials) | "SIGNED FOR IDENTIFICATION" stamp | Mumbai (no date/time) | Page-17 stamp, Standalone Ratios part 1 |
| SIG-13 | 973-977 | SR BC & CO LLP (auditor initials) | "SIGNED FOR IDENTIFICATION" stamp | Mumbai (no date/time) | Page-18 stamp, Standalone Ratios part 2 |
| SIG-14 | 1020-1025 | SR BC & CO LLP (auditor initials) | "SIGNED FOR IDENTIFICATION" stamp | Mumbai (no date/time) | Page-19 stamp, follows CEO sign-off on Standalone Notes page |

NOT_FOUND: none of the signature blocks carry an intraday timestamp (only "27th
July 2026" / "Mumbai" dates), so it is not possible to determine from this extract
whether any signature was affixed before the Board Meeting concluded at 4:15 p.m.
(line 17). This is a genuine evidentiary gap (NOT FOUND, not estimated) — flag for
A3/A4 if timestamp verification is material; nothing in the extract contradicts
normal sequencing (signatures dated same calendar day as the 27-Jul-2026 meeting).

---

## 14. ZERO_STANDING / FLAG SUMMARY

| Flag | Location | Note |
|------|----------|------|
| ZERO_STANDING | S-22, standalone P&L "Current Tax", line 772 | Dash in all 4 periods (30-Jun-26, 31-Mar-26, 30-Jun-25, FY26). Consolidated equivalent (C-31, line 351) is NOT zero — standalone-only feature. |
| ZERO_STANDING (partial) | CR-9b, consolidated review report para 9 bullet 2, lines 125-127 | "Rs. Nil crore" explicitly stated for 3 associates + 8 JVs' share of net profit/loss and total comprehensive income this quarter — template retained for future non-nil disclosure. |
| Non-ZERO_STANDING (flagged for attention, not meeting strict all-period-dash definition) | C-27/C-28 (Impairment of Investment, consol.), CS-19 (Exceptional Item - Unallocable, consol. segment), SR-16 (Debenture Redemption Reserve, standalone ratio), SR-17/17a/17b (Asset Cover Ratio, standalone ratio) | Each populated in at least one of the four comparative periods — do not qualify as ZERO_STANDING under the strict "zero/nil/dash in ALL periods" definition, but noted here since the current quarter (30-Jun-26) column is blank/dash-referred for each. |
| ENTITY_CHANGE | N/A this run | No prior-quarter Annexure 1 list supplied to diff against. |
| MGMT_ABSENCE / REPEAT_QUESTION / DROPPED_SLIDE | N/A | Doctype is "results" (no concall transcript or investor presentation in this run). |
