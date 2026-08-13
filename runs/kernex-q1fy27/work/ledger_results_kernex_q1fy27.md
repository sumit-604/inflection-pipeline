# ENUMERATION LEDGER — KERNEX Q1 FY27 Results Filing (Board Outcome + Un-Audited Standalone & Consolidated Results, 12 pages)
Source: extract_results_kernex_q1fy27.txt (line numbers below refer to this file)

```
=== A2 COUNT TEST ===
category: agenda_items    grep_count: 5    sweep_count: 5    match: yes
category: annexure_fields grep_count: 14   sweep_count: 14   match: yes
category: line_items      grep_count: 63   sweep_count: 63   match: yes   (35 consol data rows + 28 standalone data rows; regex on data-value pattern vs manual row walk, both scoped to lines 184-243 and 462-508)
category: zero_standing   grep_count: 3    sweep_count: 3    match: yes   (all-4-period-dash rows: consol VI.Exceptional Items, consol OCI-NCI; standalone VI.Exceptional Items)
category: notes           grep_count: 19   sweep_count: 19   match: yes   (10 consol + 9 standalone, scoped to note-block line ranges to exclude auditor-report numbered paragraphs)
category: auditor_paras   grep_count: 18   sweep_count: 18   match: yes   (12 consol + 6 standalone; one false-positive "2410" numeral in standalone para 3 continuation excluded from both counts)
category: entities        grep_count: 6    sweep_count: 6    match: yes
category: signature_blocks grep_count: 4   sweep_count: 4    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

---
## 1. BOARD OUTCOME — AGENDA ITEMS (Reg 30/33 letter, page 1)

| # | Line | Item | Detail | Flags |
|---|------|------|--------|-------|
| 1 | L54-55 | (i) | Approved Un-Audited standalone and Consolidated Financial Results for Q1 FY27 (quarter ended 30 June 2026) | |
| 2 | L56-58 | (ii) | Took note of the Limited Review Report on un-audited Standalone and Consolidated Financial Results (Reg 33) | |
| 3 | L59-60 | (iii) | Approved re-appointment of Mr. Badari Narayana Raju Manthena (DIN quoted here: 07992925) as Whole Time Director for further 3 years w.e.f. 2 Sept 2026 | DIN_MISMATCH (see row 3 below vs Annexure A) |
| 4 | L61-62 | (iv) | Approved re-appointment of Mr. Sitarama Raju Manthena (DIN: 08576273) as Whole Time Director for further 3 years w.e.f. 2 Sept 2026 | |
| 5 | L63-64 | (v) | Approved Directors' Report with MD&A, Corporate Governance Report and other annexures | |
| 6 | L70 | Board meeting timing | Commenced 09:45 A.M., concluded 11:50 A.M. — duration 2h05m | |

Note DIN_MISMATCH: Board letter (L59) states DIN **07992925** for Badari Narayana Raju Manthena; Annexure A heading (L88) and table (L91) both state DIN **07993925** for the same person (digit 5 transposed: ...92925 vs ...93925). Mechanical numeric discrepancy within the same document, not resolved by the extract.

---
## 2. ANNEXURE A — DIRECTOR RE-APPOINTMENT DISCLOSURES (Reg 30 / SEBI Circular disclosure format, pages 2-3)

### 2a. Director 1 — Mr. Badari Narayana Raju Manthena (DIN 07993925 per Annexure; 07992925 per cover letter)

| # | Line | Field | Content (verbatim/summarized) | Flags |
|---|------|-------|-------------------------------|-------|
| 1 | L91 | Name and DIN | Mr. Badari Narayana Raju Manthena (DIN: 07993925) | DIN_MISMATCH |
| 2 | L93-95 | Reason for change | Re-appointment, 3 years w.e.f. 2 Sept 2026, current term expires 1 Sept 2026 | |
| 3 | L97-98 | Date & Term of Appointment | 2 Sept 2026; three years from 2 Sept 2026 | |
| 4 | L100-109 | Brief Profile | 25 years with company, Chief Administrative and Commercial Officer, WTD since 20 Nov 2017, Bachelors in Commerce | |
| 5 | L111-113 | Disclosure of relationship between directors | "There is no relationship between the directors and the appointee" | |
| 6 | L115-120 | Listed entities where director holds directorship | Not Applicable | |
| 7 | L122-125 | SEBI debarment confirmation (Circular LISTCOMP/14/2018-19) | Confirmed not debarred by any SEBI order or authority | |

### 2b. Director 2 — Mr. Sitarama Raju Manthena (DIN 08576273)

| # | Line | Field | Content (verbatim/summarized) | Flags |
|---|------|-------|-------------------------------|-------|
| 8 | L135 | Name and DIN | Mr. Sitarama Raju Manthena (DIN: 08576273) | |
| 9 | L137-139 | Reason for change | Re-appointment, 3 years w.e.f. 2 Sept 2026, current term expires 1 Sept 2026 | |
| 10 | L141-142 | Date & Term of Appointment | 2 Sept 2026; three years from 2 Sept 2026 | |
| 11 | L144-150 | Brief Profile | BS Comp Science with Business Admin, 20+ years International Business Development / Project Mgmt | |
| 12 | L152-154 | Disclosure of relationship between directors | Son of Dr. Anji Raju Manthena and Mrs. Parvathi Manthena; brother of Ms. Sreelakshmi Manthena | RELATED_PARTY (disclosed) |
| 13 | L156-161 | Listed entities where director holds directorship | Not Applicable | |
| 14 | L163-166 | SEBI debarment confirmation (Circular LISTCOMP/14/2018-19) | Confirmed not debarred by any SEBI order or authority | |

---
## 3. CONSOLIDATED FINANCIAL RESULTS — STATEMENT LINE ITEMS (page 4, L184-243)
Columns: Q1FY27 (30-Jun-26, UnAud) / Q4FY26 (31-Mar-26, Aud) / Q1FY26 (30-Jun-25, UnAud) / FY26 (31-Mar-26, Aud)

| # | Line | Row label | Type | Values (Q1FY27 / Q4FY26 / Q1FY26 / FY26) | Flags |
|---|------|-----------|------|---|---|
| 1 | L184 | Income | HEADER | — | |
| 2 | L185 | I. Revenue from operations | DATA | 50,358.23 / 25,457.69 / 5,592.99 / 43,022.12 | |
| 3 | L186 | II. Other income | DATA | 48.52 / 92.05 / 36.14 / 224.66 | |
| 4 | L187 | III. Total Income (I+II) | DATA subtotal | 50,406.74 / 25,549.74 / 5,629.13 / 43,246.78 | |
| 5 | L189 | IV. Expenses: | HEADER | — | |
| 6 | L190 | (a) Cost of materials consumed | DATA | 26,803.30 / 11,582.97 / 3,033.06 / 39,476.27 | |
| 7 | L191-192 | (b) Changes in inventories of finished goods, stock-in-trade and work-in-progress | DATA | (2,135.47) / (1,499.19) / (260.23) / (22,256.70) | |
| 8 | L193 | (c) Project execution expenses | DATA | 4,019.13 / 2,396.44 / 711.64 / 5,378.54 | |
| 9 | L194 | (d) Employee benefits expense | DATA | 1,393.29 / 944.17 / 658.56 / 3,243.82 | |
| 10 | L195 | (e) Finance costs | DATA | 1,322.77 / 1,178.91 / 255.38 / 2,815.07 | |
| 11 | L196 | (f) Depreciation and amortization expenses | DATA | 194.41 / 212.95 / 83.76 / 582.22 | |
| 12 | L197 | (g) Other expenses | DATA | 4,093.93 / 1,566.22 / 316.21 / 2,653.56 | includes ₹30.05cr KAVACH/signalling warranty provision per Note 8 |
| 13 | L198 | (h) Amount transferred to capital expenditure | DATA | (98.34) / (44.61) / (124.41) / (350.26) | |
| 14 | L199 | Total Expenses (IV) | DATA subtotal | 35,593.03 / 16,337.86 / 4,673.96 / 31,542.52 | |
| 15 | L201 | V. Profit before exceptional items and tax (III-IV) | DATA subtotal | 14,813.71 / 9,211.88 / 955.18 / 11,704.26 | |
| 16 | L203 | VI. Exceptional Items | DATA | - / - / - / - | **ZERO_STANDING** |
| 17 | L205 | VII. Profit before tax (V-VI) | DATA subtotal | 14,813.71 / 9,211.88 / 955.18 / 11,704.26 | |
| 18 | L207 | VIII. Tax expense: | HEADER | — | |
| 19 | L208 | (a) Current tax expense | DATA | 4,688.31 / 2,271.38 / - / 2,271.38 | |
| 20 | L209 | (b) Adjustment of tax relating to earlier periods | DATA | - / 48.42 / - / 48.42 | |
| 21 | L210 | (c) Deferred tax credit | DATA | (859.17) / 66.99 / 213.97 / 560.16 | |
| 22 | L211 | Total Tax Expense/(Credit) net (VIII) | DATA subtotal | 3,829.14 / 2,386.79 / 213.97 / 2,879.96 | |
| 23 | L213 | IX. Profit for the period/year (VII-VIII) | DATA subtotal | 10,984.57 / 6,825.09 / 741.21 / 8,824.30 | |
| 24 | L215 | X. Other comprehensive income/(loss) | HEADER | — | |
| 25 | L216 | A. Items that will not be reclassified to P&L | HEADER (sub) | — | |
| 26 | L218 | i. Remeasurement gains/(losses) of the defined benefit plans | DATA | - / (86.82) / - / (82.44) | |
| 27 | L219 | ii. Income tax effect on the above | DATA | - / 20.75 / - / 20.75 | |
| 28 | L220 | A. Items that will be reclassified to P&L | DATA | (0.25) / 3.56 / - / (4.37) | label reused "A." in source (should logically be "B."); OCR/drafting artifact, not corrected |
| 29 | L221 | Total other comprehensive income/(loss) (X) | DATA subtotal | (0.25) / (62.51) / - / (66.07) | |
| 30 | L223 | XI. Total comprehensive income for the period/year (IX+X) | DATA subtotal | 10,984.32 / 6,762.59 / 741.21 / 8,758.24 | |
| 31 | L225 | Profit for the year attributable to: | HEADER | — | |
| 32 | L226 | Owners of the Company | DATA | 10,984.60 / 6,825.58 / 746.48 / 8,833.63 | |
| 33 | L227 | Non-controlling interests | DATA | (0.03) / (0.49) / (5.27) / (9.33) | |
| 34 | L229 | Other comprehensive income for the year attributable to: | HEADER | — | |
| 35 | L230 | Owners of the Company | DATA | (0.25) / (62.51) / - / (66.07) | |
| 36 | L231 | Non-controlling interests | DATA | - / - / - / - | **ZERO_STANDING** |
| 37 | L233 | Total comprehensive income for the year attributable to: | HEADER | — | |
| 38 | L234 | Owners of the Company | DATA | 10,984.35 / 6,763.08 / 746.48 / 8,767.57 | |
| 39 | L235 | Non-controlling interests | DATA | (0.03) / (0.49) / (5.27) / (9.33) | |
| 40 | L237 | Paid-up equity share capital (FV ₹10 each) | DATA | 1,680.36 / 1,680.24 / 1,675.94 / 1,680.24 | ties to Note 5 (1,200 ESOP shares allotted) |
| 41 | L238 | Other equity | DATA | (blank) / (blank) / (blank) / 23,131.24 | BLANK_QUARTERLY — annual-only BS line per Ind AS 34 presentation, not zero |
| 42 | L240 | Earnings per equity share (EPS) of ₹10 each | HEADER | — | |
| 43 | L241 | Basic EPS (₹) | DATA | 65.37 / 40.69 / 4.45 / 52.71 | |
| 44 | L242 | Diluted EPS (₹) | DATA | 65.37 / 40.69 / 4.44 / 52.67 | |
| 45 | L243 | [Not Annualised / Annualised qualifier row] | QUALIFIER | Not Annualised / Not Annualised / Not Annualised / Annualised | |

---
## 4. NOTES TO CONSOLIDATED FINANCIAL RESULTS (page 5, L246-278)

| # | Line | Note | First ~15 words | Flags |
|---|------|------|------------------|-------|
| 1 | L248-250 | Note 1 | "The Unaudited Consolidated Financial Results...have been reviewed by the Audit Committee and approved..." | |
| 2 | L251-253 | Note 2 | "The Unaudited Consolidated Financial Results have been prepared in accordance with...Ind AS 34..." | |
| 3 | L254-258 | Note 3 | "The Company is engaged in the manufacture and sale of Safety Systems and Software services for railways..." | operations in India, Egypt, USA; single reportable segment |
| 4 | L259-265 | Note 4 | "Emphasis of Matter – Management's Assessment of Certain Financial Assets..." | EOM cross-ref |
| 4a | L263-264 | Note 4(a) [sub-item] | Trade receivables ₹422.73 lakhs (PY ₹422.73 lakhs), ECL provision ₹334.59 lakhs (PY ₹309.59 lakhs), outstanding >3 years | SUBITEM |
| 4b | L265 | Note 4(b) [sub-item] | Bank guarantees ₹265.03 lakhs given to one customer, under arbitration/conciliation | SUBITEM |
| 5 | L266-267 | Note 5 | "During the quarter, the company has allotted 1,200 equity shares of ₹10 each fully paid-up, on exercise of stock options..." | ties to line 40 of statement |
| 6 | L268-271 | Note 6 | "The consolidated financial results...include the financial results of its Wholly Owned Subsidiary, Avant-Garde Infosystems Inc...Controlled Entities..." | entity list — see Section 9 |
| 7 | L272-273 | Note 7 | "As at the reporting date, the Company's aggregate outstanding order book is ₹3641 Crores (Including GST)..." | CLW major order, 45% supplies completed as on 13-08-2026 |
| 8 | L274-275 | Note 8 | "During this Quarter, the Company has recognised a provision of ₹30.05 Crore towards warranty obligations on KAVACH and signalling systems..." | included in "Other Expenses" (row 12 above) |
| 9 | L276 | Note 9 | "The figures for the corresponding previous periods have been regrouped/reclassified wherever necessary, to make them comparable." | |
| 10 | L277-278 | Note 10 | "The above Financial Results...are available on the company's website and stock exchanges websites BSE...and NSE..." | |

---
## 5. INDEPENDENT AUDITOR'S REVIEW REPORT — CONSOLIDATED (pages 6-8, L291-444)

| # | Line | Paragraph / unit | Content summary | Flags |
|---|------|-------------------|------------------|-------|
| 1 | L304-309 | Para 1 | Reviewed accompanying Statement of unaudited consolidated results, submitted per Reg 33 | |
| 2 | L311-316 | Para 2 | Holding Co management responsible for preparation per Ind AS 34; auditor responsible to express conclusion | |
| 3 | L318-329 | Para 3 | Review per SRE 2410, moderate assurance, less in scope than audit, no audit opinion expressed; also performed Master Circular procedures under Reg 33(8) | |
| 4 | L331-341 | Para 4 | Statement includes results of 6 entities (list) + footnote that KERNEX-BHEPL JV formed 07.03.2026, agreement executed, not yet commenced operations as at 30.06.2026 | ENTITY_CHANGE (KERNEX-BHEPL JV newly formed) |
| 5 | L357-371 | Emphasis of Matter | Note 3 recoverability of financial assets: (a) trade receivables ₹422.73 lakhs (PY ₹422.10 lakhs) ECL ₹334.59 lakhs (PY ₹211.67 lakhs); (b) bank guarantees ₹265.03 lakhs under arbitration; conclusion not qualified | note: PY comparative figures here (₹422.10 lakhs / ₹211.67 lakhs) differ from the figures in Note 4 of the results themselves (₹422.73 lakhs / ₹309.59 lakhs PY) — cross-document figure inconsistency, flagged for A3/A4 |
| 6 | L373-374 | "Other Matter" section heading | Intro to 4 sub-paragraphs on entities not reviewed by NSVR | |
| 7 | L375-385 | Other Matter 1 | Kernex TCAS JV (Controlled entity/Subsidiary) not reviewed by NSVR; revenue Nil, net profit ₹0.39 lakhs, TCI ₹0.39 lakhs; reviewed by other auditors, reports furnished by Management | OTHER_AUDITOR_REVIEWED |
| 8 | L386-395 | Other Matter 2 | VRRC KERNEX CE RVR JV (Joint Operation) not reviewed by NSVR; revenue ₹187.34 lakhs, net loss ₹0.80 lakhs, TCI loss ₹0.80 lakhs; other-auditor reviewed | OTHER_AUDITOR_REVIEWED |
| 9 | L397-406 | Other Matter 3 | KERNEX VRRC JV (Controlled entity/Subsidiary) not reviewed by NSVR; revenue ₹104.84 lakhs, net loss ₹0.53 lakhs, TCI loss ₹0.53 lakhs; other-auditor reviewed | OTHER_AUDITOR_REVIEWED |
| 10 | L413-420 | Other Matter 4 | Avant-Garde Infosystems Inc (WOS, USA) — NOT reviewed by NSVR AND NOT by its own auditors either; revenue ₹154.95 lakhs, net profit ₹27.56 lakhs, TCI ₹27.30 lakhs; management states not material to Group | **UNREVIEWED_UNAUDITED** (distinct from rows 7-9: no auditor of any kind reviewed this entity's figures) |
| 11 | L422-427 | Concluding opinion paragraph | "Nothing has come to our attention...has not disclosed the information required...or that it contains any material misstatement" — unmodified conclusion | |
| 12 | L431-444 | Signature block | For NSVR & Associates LLP; V Gangadhar Rao N, Partner, Membership No. 219486, UDIN 262194860QMYK09252, Place Hyderabad, Date 13-08-2026 | |

---
## 6. STANDALONE FINANCIAL RESULTS — STATEMENT LINE ITEMS (page 9, L462-508)
Columns: Q1FY27 (30-Jun-26, UnAud) / Q4FY26 (31-Mar-26, Aud) / Q1FY26 (30-Jun-25, UnAud) / FY26 (31-Mar-26, Aud)

| # | Line | Row label | Type | Values (Q1FY27 / Q4FY26 / Q1FY26 / FY26) | Flags |
|---|------|-----------|------|---|---|
| 1 | L462 | Income | HEADER | — | |
| 2 | L463 | I. Revenue from operations | DATA | 50,203.27 / 25,457.70 / 5,339.77 / 42,580.96 | |
| 3 | L464 | II. Other income | DATA | 47.88 / 91.92 / 61.90 / 276.56 | |
| 4 | L465 | III. Total Income (I+II) | DATA subtotal | 50,251.15 / 25,549.62 / 5,401.67 / 42,857.52 | |
| 5 | L467 | IV. Expenses: | HEADER | — | |
| 6 | L468 | (a) Cost of materials consumed | DATA | 26,680.78 / 11,585.61 / 2,831.19 / 39,134.81 | |
| 7 | L469-470 | (b) Changes in inventories of finished goods, stock-in-trade and work-in-progress | DATA | (2,135.47) / (1,499.19) / (260.23) / (22,256.70) | |
| 8 | L471 | (c) Project execution expenses | DATA | 4,019.13 / 2,393.80 / 711.64 / 5,375.90 | |
| 9 | L472 | (d) Employee benefits expense | DATA | 1,393.29 / 944.18 / 649.99 / 3,235.09 | |
| 10 | L473 | (e) Finance costs | DATA | 1,322.49 / 1,178.49 / 255.07 / 2,814.22 | |
| 11 | L474 | (f) Depreciation and amortization expenses | DATA | 194.41 / 212.95 / 83.76 / 582.22 | |
| 12 | L475 | (g) Other expenses | DATA | 4,088.56 / 1,935.37 / 304.16 / 3,379.76 | includes ₹30.05cr KAVACH/signalling warranty provision per Note 7 |
| 13 | L476 | (h) Amount transferred to capital expenditure | DATA | (98.34) / (44.61) / (124.41) / (350.26) | |
| 14 | L477 | Total Expenses (IV) | DATA subtotal | 35,464.86 / 16,706.60 / 4,451.17 / 31,915.04 | |
| 15 | L479 | V. Profit before exceptional items and tax (III-IV) | DATA subtotal | 14,786.29 / 8,843.01 / 950.50 / 10,942.47 | |
| 16 | L481 | VI. Exceptional Items | DATA | - / - / - / - | **ZERO_STANDING** |
| 17 | L483 | VII. Profit before tax (V-VI) | DATA subtotal | 14,786.29 / 8,843.01 / 950.50 / 10,942.47 | |
| 18 | L485 | VIII. Tax expense: | HEADER | — | |
| 19 | L486 | (a) Current tax expense | DATA | 4,688.31 / 2,271.38 / - / 2,271.38 | |
| 20 | L487 | (b) Adjustment of tax relating to earlier periods | DATA | - / 48.42 / - / 48.42 | |
| 21 | L488 | (c) Deferred tax credit | DATA | (859.17) / 66.99 / 213.97 / 560.16 | |
| 22 | L489 | Total Tax Expense/(Credit) net (VIII) | DATA subtotal | 3,829.14 / 2,386.79 / 213.97 / 2,879.96 | |
| 23 | L491 | IX. Profit for the period/year (VII-VIII) | DATA subtotal | 10,957.16 / 6,456.23 / 736.53 / 8,062.52 | |
| 24 | L493 | X. Other comprehensive income/(loss) | HEADER | — | |
| 25 | L494 | A. Items that will not be reclassified to P&L | HEADER (sub) | — | |
| 26 | L496 | i. Remeasurement gains/(losses) of the defined benefit plans | DATA | - / (82.44) / - / (82.44) | |
| 27 | L497 | ii. Income tax effect on the above | DATA | - / 20.75 / - / 20.75 | |
| 28 | L498 | Total other comprehensive income/(loss) (X) | DATA subtotal | - / (61.69) / - / (61.69) | |
| 29 | L500 | XI. Total comprehensive income for the period/year (IX+X) | DATA subtotal | 10,957.16 / 6,394.53 / 736.53 / 8,000.82 | |
| 30 | L502 | Paid-up equity share capital (FV ₹10 each) | DATA | 1,680.36 / 1,680.24 / 1,675.94 / 1,680.24 | ties to Note 5 (1,200 ESOP shares allotted) |
| 31 | L503 | Other equity | DATA | (blank) / (blank) / (blank) / 23,950.29 | BLANK_QUARTERLY — annual-only BS line; note standalone Other Equity (23,950.29) > consolidated Other Equity (23,131.24), expected given consol NCI/elimination effects |
| 32 | L505 | Earnings per equity share (EPS) of ₹10 each | HEADER | — | |
| 33 | L506 | Basic EPS (₹) | DATA | 65.21 / 38.49 / 4.39 / 48.07 | |
| 34 | L507 | Diluted EPS (₹) | DATA | 65.21 / 38.49 / 4.38 / 48.07 | |
| 35 | L508 | [Not Annualised / Annualised qualifier row] | QUALIFIER | Not Annualised / Not Annualised / Not Annualised / Annualised | |

STRUCTURAL_DIFFERENCE (expected, not a flag on completeness): standalone statement has no "Profit/OCI/Total CI attributable to Owners/NCI" breakdown rows and no NCI line items — correct, since standalone is single-entity and carries no non-controlling interests.

---
## 7. NOTES TO STANDALONE FINANCIAL RESULTS (page 10, L511-539)

| # | Line | Note | First ~15 words | Flags |
|---|------|------|------------------|-------|
| 1 | L513-515 | Note 1 | "The Unaudited Standalone Financial Results...have been reviewed by the Audit Committee and approved..." | |
| 2 | L516-518 | Note 2 | "The Unaudited Standalone Financial Results have been prepared in accordance with...Ind AS 34..." | |
| 3 | L519-523 | Note 3 | "The Company is engaged in the manufacture and sale of Safety Systems and Software services for railways..." | operations in India and Egypt only (standalone excludes USA, consistent with USA ops sitting in Avant-Garde subsidiary) |
| 4 | L524-530 | Note 4 | "Emphasis of Matter – Management's Assessment of Certain Financial Assets..." | EOM cross-ref |
| 4a | L528-529 | Note 4(a) [sub-item] | Trade receivables ₹422.73 lakhs (PY ₹422.73 lakhs), ECL provision ₹334.59 lakhs (PY ₹309.59 lakhs), outstanding >3 years | SUBITEM — identical figures to consol Note 4(a) |
| 4b | L530 | Note 4(b) [sub-item] | Bank guarantees ₹265.03 lakhs given to one customer, under arbitration/conciliation | SUBITEM — identical to consol Note 4(b) |
| 5 | L531-532 | Note 5 | "During the quarter, the company has allotted 1,200 equity shares of ₹10 each fully paid-up, on exercise of stock options..." | |
| 6 | L533-534 | Note 6 | "As at the reporting date, the Company's aggregate outstanding order book is ₹3641 Crores (Including GST)..." | identical order book figure to consol Note 7 |
| 7 | L535-536 | Note 7 | "During this Quarter, the Company has recognised a provision of ₹30.05 Crore towards warranty obligations on KAVACH and signalling systems..." | included in "Other Expenses" |
| 8 | L537 | Note 8 | "The figures for the corresponding previous periods have been regrouped/reclassified wherever necessary, to make them comparable." | |
| 9 | L538-539 | Note 9 | "The above Financial Results...are available on the company's website and stock exchanges websites BSE...and NSE..." | |

Note: standalone note set has no equivalent of consol Note 6 (subsidiary/JV consolidation entity list) — expected, standalone carries no consolidation scope note.

---
## 8. INDEPENDENT AUDITOR'S REVIEW REPORT — STANDALONE (pages 11-12, L552-641)

| # | Line | Paragraph / unit | Content summary | Flags |
|---|------|-------------------|------------------|-------|
| 1 | L565-568 | Para 1 | Reviewed accompanying statement of unaudited standalone results, submitted per Reg 33 | |
| 2 | L569-575 | Para 2 | Statement is management's responsibility, approved by Board, prepared per Ind AS 34; auditor's responsibility to express conclusion | |
| 3 | L576-584 | Para 3 | Review per SRE 2410, moderate assurance, less in scope than audit, no audit opinion expressed | |
| 4 | L586-599 | Emphasis of Matter | Note 3 recoverability: (a) trade receivables ₹422.73 lakhs (PY ₹422.10 lakhs) ECL ₹334.59 lakhs (PY ₹309.59 lakhs); (b) bank guarantees ₹265.03 lakhs under arbitration; conclusion not qualified | note: same PY figure inconsistency as consol report — EOM cites PY receivable ₹422.10 lakhs vs Note 4 of results citing PY ₹422.73 lakhs; ECL PY figure ₹309.59 lakhs here matches Note 4 (unlike the consol EOM paragraph which cited PY ECL ₹211.67 lakhs — a further cross-report inconsistency between the two auditor reports themselves) |
| 5 | L614-619 | Concluding opinion paragraph | "Nothing has come to our attention...has not disclosed the information required...or that it contains any material misstatement" — unmodified conclusion | |
| 6 | L623-641 | Signature block | For NSVR & Associates LLP, Chartered Accountants; ICAI Firm's Registration No. 003980S/S200060 (OCR-garbled); V Gangadhar Rao N, Partner, Membership No. 219486, UDIN 26219486WIKTGV7858, Place Hyderabad, Date 13-08-2026 | |

Note: standalone report has NO "Other Matter" section and NO entities-list paragraph — expected, single-entity statement, no subsidiaries/JVs to sub-reference.

DISCREPANCY (mechanical, cross-report): standalone report UDIN (26219486WIKTGV7858) differs from consolidated report UDIN (262194860QMYK09252) — expected, distinct UDIN per distinct report/opinion issued same day by same partner. Not a flag, just recorded for completeness.

DISCREPANCY (mechanical, cross-report EOM figures): the consolidated auditor's Emphasis of Matter paragraph (Section 5, row 5) states PY ECL provision of ₹211.67 lakhs, while the standalone auditor's Emphasis of Matter paragraph (this section, row 4) and both results' Note 4 state PY ECL provision of ₹309.59 lakhs for the identical receivable balance. This is an internal inconsistency in the consolidated auditor report specifically — flagged for A3/A4, not resolved here.

---
## 9. CONSOLIDATION ENTITY LIST (per consol Note 6, L268-271, and auditor report Para 4, L331-341)

| # | Entity | Relationship | Kernex Share | First appearance (line) | Flags |
|---|--------|-------------|---------------|--------------------------|-------|
| 1 | Kernex Microsystems (India) Limited | Holding Company (Parent) | 100% | L332 | |
| 2 | Avant-Garde Infosystems Inc. (USA) | Wholly Owned Subsidiary | 100% | L268 / L333 | UNREVIEWED_UNAUDITED (see Section 5 row 10) |
| 3 | Kernex TCAS JV | Controlled Entity (Subsidiary) | 80% | L269 / L334 | OTHER_AUDITOR_REVIEWED |
| 4 | KERNEX-VRRC JV | Controlled Entity (Subsidiary) | 80% | L269 / L335 | OTHER_AUDITOR_REVIEWED |
| 5 | VRRC KERNEX CE RVR JV | Joint Operation | 35% | L269-270 / L336 | OTHER_AUDITOR_REVIEWED |
| 6 | KERNEX-BHEPL JV | Joint Operation | 51% | L270 / L337, L339-341 | **ENTITY_CHANGE** — JV formed 07.03.2026 (agreement executed with Bharat Heavy Engineering Private Limited), not yet commenced operations as at 30.06.2026; no prior-quarter ledger supplied for direct cross-check, but the document's own footnote signals this is a newly added consolidation-scope entity relative to prior quarters |

---
## 10. SIGNATURE BLOCKS

| # | Line | Signatory | Designation | Identifier | Place / Date | Flags |
|---|------|-----------|-------------|------------|---------------|-------|
| 1 | L286-288 | Sreelakshmi Manthena | Managing Director | DIN 07996443 | Houston / 13 Aug 2026 | consol results sign-off; signed from Houston (USA), not Hyderabad — mechanical fact, not interpreted |
| 2 | L547-549 | Sreelakshmi Manthena | Managing Director | DIN 07996443 | Houston / 13 Aug 2026 | standalone results sign-off, identical block |
| 3 | L437-444 | V Gangadhar Rao N | Partner, NSVR & Associates LLP | Membership No. 219486; UDIN 262194860QMYK09252 | Hyderabad / 13-08-2026 | consol auditor report sign-off |
| 4 | L635-641 | V Gangadhar Rao N | Partner, NSVR & Associates LLP | Membership No. 219486; UDIN 26219486WIKTGV7858 | Hyderabad / 13-08-2026 | standalone auditor report sign-off |

No digital-signature timestamp metadata (e.g., "digitally signed at HH:MM:SS") is present anywhere in the extract — only board meeting start/end clock times (Section 1, row 6) and printed signature dates (this section) are available. NOT FOUND for any digital-signature timestamp.

---
## SUMMARY OF FLAGS RAISED
- ZERO_STANDING x3 (consol VI. Exceptional Items; consol OCI attributable to NCI; standalone VI. Exceptional Items)
- ENTITY_CHANGE x1 (KERNEX-BHEPL JV, newly formed 07.03.2026, first quarter appearing not-yet-operational in this consolidation scope)
- DIN_MISMATCH x1 (Badari Narayana Raju Manthena: board letter DIN 07992925 vs Annexure A DIN 07993925)
- UNREVIEWED_UNAUDITED x1 (Avant-Garde Infosystems Inc — not reviewed by NSVR or its own auditors, management-asserted immaterial)
- OTHER_AUDITOR_REVIEWED x3 (Kernex TCAS JV, KERNEX-VRRC JV, VRRC KERNEX CE RVR JV — reviewed by other auditors, reports furnished by management)
- BLANK_QUARTERLY x2 (Other equity line, consol and standalone — annual-only disclosure, not a zero value)
- Cross-report EOM PY-ECL figure inconsistency (₹211.67 lakhs in consol auditor report vs ₹309.59 lakhs in standalone auditor report and both results' Note 4) — flagged for A3/A4, not resolved
- STRUCTURAL_DIFFERENCE (expected) x1 (standalone statement lacks NCI/attribution rows — correct given single-entity scope)
