# LEDGER — TRANSRAIL Q1 FY27 — Results Filing (Reg 33 Board Outcome + Unaudited Standalone & Consolidated Financial Results + Limited Review Reports)

Source: `extract_results_transrail_q1fy27.txt` (23 pages, 1145 content lines, header offset +13 to file line numbers used below). All line numbers below are **actual file line numbers** (equal to `grep -n` / `cat -n` line numbers on the extract file).

No prior-quarter ledger was supplied for this run (`PRIOR_LEDGER_PATH` not provided / not found under `runs/`). ENTITY_CHANGE flags below are therefore based on **within-filing evidence** (the filing's own notes state an entity was newly acquired this quarter) rather than a ledger diff; this limitation is called out explicitly wherever used.

```
=== A2 COUNT TEST ===
category: notes            grep_count: 31   sweep_count: 31   match: yes
category: line_items       grep_count: 90   sweep_count: 90   match: yes
category: zero_standing    grep_count: 5    sweep_count: 5    match: yes
category: agenda_items     grep_count: 4    sweep_count: 4    match: yes
category: auditor_paras    grep_count: 23   sweep_count: 23   match: yes  (see reconciliation note below)
category: entities          grep_count: 17   sweep_count: 17   match: yes
category: annexures        grep_count: 4    sweep_count: 4    match: yes
category: annexure_rows    grep_count: 13   sweep_count: 13   match: yes
category: signatures       grep_count: 5    sweep_count: 5    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

**Reconciliation note (auditor_paras):** first-pass mechanical grep `^\s*[0-9]+\s+[0-9]\.\s` on the two Limited Review Reports returned 7 top-level paragraphs in the standalone report and 7 in the consolidated report (14 total). Manual sweep read every line of both reports and found an 8th consolidated-report top-level paragraph whose number was OCR'd as **"S."** instead of "5." (file line 554: `S. The Statement includes unaudited standalone financial results of the following entities:`). A second grep pass with an OCR-tolerant character class `[0-9SI]\.` recovered this paragraph, bringing top-level paragraphs to 7 (standalone) + 8 (consolidated) = 15. Adding lettered sub-paragraphs (standalone Other Matters 7a/7b/7c = 3; consolidated Other Matters 8a/8b/8c/8d/8e = 5) gives 15 + 8 = 23, which the manual sweep also confirms. **Flag: OCR_ERROR** — paragraph number "5." misrendered as "S." in the consolidated Limited Review Report at line 554; this is exactly the kind of miss GATE A2 exists to catch. Re-verify against the source PDF (not just OCR text) if paragraph numbering matters downstream.

---

## 1. BOARD OUTCOME LETTER — AGENDA ITEMS

Board meeting held Thursday, August 6, 2026. **Meeting commenced 4:30 p.m., concluded 6:35 p.m.** (line 95) — a ~2h05m meeting covering results approval plus three governance/personnel matters.

| # | Line | Agenda Item | First 15 words | Flags |
|---|------|-------------|-----------------|-------|
| 1 | 39 | Unaudited Financial Results | "Unaudited Financial Results (Standalone & Consolidated) of the Company for the quarter ended June 30..." | — |
| 2 | 44 | Reappointment of Mr. Digambar Chunnilal Bagde as Executive Chairman | "Based on the recommendation of the Nomination & Remuneration Committee, the Board approved the reappointment..." | Reappointment effective Oct 1, 2026–Sep 30, 2027, subject to shareholder approval; details in Annexure II |
| 3 | 54 | Appointment of Statutory Auditors (Joint) | "Based on the recommendation of the Audit Committee, the Board approved and recommended the appointment..." | New joint auditor M/s. G.M. Kapadia & Co. added alongside continuing auditor M/s. Nayan Parikh & Co.; subject to shareholder approval; details in Annexure III |
| 4 | 84 | Cessation of term of Independent Director | "The Board noted that the term of appointment of Major General Dr. Dilawar Singh (Retd.) (DIN:..." | Effective close of business Sep 13, 2026 (term completion, not resignation/removal); details in Annexure IV |

Meeting-timing row (not a numbered agenda item, recorded for completeness): line 95, "The meeting commenced at 4.30 p.m. and concluded at 6.35 p.m."

---

## 2. ANNEXURES AND ANNEXURE TABLE ROWS

| Annexure | Line (heading) | Content | Table rows (Sr. No.) |
|----------|-----------------|---------|------------------------|
| Annexure I | 118 | Standalone & Consolidated Unaudited Financial Results + both Limited Review Reports (enumerated in full in sections 3–6 below) | n/a (composite; content counted separately) |
| Annexure II | 1031 | Reg 30 disclosure — reappointment of Mr. Digambar Chunnilal Bagde as Executive Chairman | 6 |
| Annexure III | 1080 | Reg 30 disclosure — appointment of M/s. G.M. Kapadia & Co. as joint Statutory Auditor | 3 |
| Annexure IV | 1130 | Reg 30 disclosure — cessation of Independent Director Major General Dr. Dilawar Singh (Retd.) | 4 |

### Annexure II rows (Director reappointment)
| Sr. | Line | Particulars | First 15 words |
|-----|------|-------------|-----------------|
| 1 | 1040 | Name of Director | "Mr. Digambar Chunnilal Bagde (DIN: 00122564)" |
| 2 | 1042 | Reason for change | "Re-appointment of Mr. Digambar Chunnilal Bagde (DIN: 00122564) as the Executive Chairman and Whole-time..." |
| 3 | 1050 | Date of appointment/re-appointment/cessation & term | "Date of re-appointment: October 1, 2026. Term: 1 (One) year, from October 1, 2026 to..." |
| 4 | 1054 | Brief Profile | "Mr. Digambar Chunnilal Bagde has over 55 years of experience in the EPC industry..." |
| 5 | 1063 | Disclosure of relationships between directors | "Mr. Digambar Chunnilal Bagde is not related to any Director of the Company." |
| 6 | 1066 | Information per BSE/NSE circulars (debarment) | "Mr. Digambar Chunnilal Bagde is not debarred from holding the office of Director..." |

### Annexure III rows (Statutory Auditor appointment)
| Sr. | Line | Particulars | First 15 words |
|-----|------|-------------|-----------------|
| 1 | 1089 | Reason for change | "The second term of five consecutive years of the existing Statutory Auditors, M/s. Nayan Parikh..." |
| 2 | 1102 | Date of appointment/re-appointment/cessation & term | "M/s. G. M. Kapadia & Co., Chartered Accountants shall be appointed at the ensuing Annual..." |
| 3 | 1108 | Brief profile | "M/s. G. M. Kapadia & Co., Chartered Accountants is a well-reputed firm of Chartered Accountants..." |

### Annexure IV rows (Independent Director cessation)
| Sr. | Line | Particulars | First 15 words |
|-----|------|-------------|-----------------|
| 1 | 1140 | Reason for change | "Completion of his term as an Independent Director of the Company on September 13, 2026." |
| 2 | 1143 | Date of cessation/resignation | "With effect from the close of business hours on September 13, 2026." |
| 3 | 1145 | Brief profile (in case of appointment) | "Not Applicable" — ZERO_STANDING (field template exists for appointment scenario but is N/A for cessation) |
| 4 | 1147 | Disclosure of relationships between directors | "Not Applicable" — ZERO_STANDING (same reasoning) |

---

## 3. STANDALONE LIMITED REVIEW REPORT — AUDITOR M/s. Nayan Parikh & Co. (paragraphs)

Opinion type: **unmodified/unqualified review conclusion** ("nothing has come to our attention... has not disclosed the information required...or that it contains any material misstatement"). Contains **one Emphasis of Matter** and **one Other Matters** paragraph (with 3 sub-parts).

| # | Line | Paragraph | First 15 words | Flags |
|---|------|-----------|------------------|-------|
| 1 | 144 | Scope of review (intro) | "We have reviewed the accompanying statement of Unaudited Standalone Financial Results ("the Statement")..." | Lists branch auditors reviewing 26 named overseas branch locations (Abu Dhabi, Afghanistan, Bangladesh, Benin, Bhutan, Botswana, Cameroon, Djibouti, Eswatini, Ethiopia, Gambia, Ghana, Italy, Jordan, Kenya, Mali, Mozambique, Nepal, Nicaragua, Philippines, Suriname, Thailand, Togo, Tanzania, Tunisia, Uganda) plus one management-certified branch (Niger) |
| 2 | 157 | Management's responsibility | "The Statement is the responsibility of the Company's Management and has been approved by the..." | — |
| 3 | 167 | Auditor's Responsibility | "We conducted our review in accordance with the Standard on Review Engagement (SRE) 2410,..." | — |
| 4 | 191 | SEBI Reg 33(8) procedures | "We also performed procedures in accordance with the circular issued by the SEBI under Regulation..." | — |
| 5 | 195 | Conclusion | "Based on our review conducted and procedures performed as stated in paragraph 3 and 4..." | Unmodified conclusion |
| 6 | 206 | **Emphasis of Matter** | "We draw attention to Note 6 to the standalone financial results regarding the search and..." | EoM re: IT Dept Section 132 search & seizure; conclusion NOT modified |
| 7 | 229 | **Other Matters** (parent para) | "We did not review the financial results of 27 Branches included in the Unaudited Standalone..." | 3 sub-parts below |
| 7a | 230 | Other Matters (a) | "We did not review the financial results of 27 Branches... total revenues of Rs. 279.68..." | 27 branches, unaudited-by-us / reviewed by branch auditors; revenue Rs.279.68cr, PAT Rs.38.25cr; all located outside India |
| 7b | 242 | Other Matters (b) | "We did not review the financial results of one Branch... total revenues of Rs. 15.57..." | 1 branch, **management-furnished / not reviewed by any auditor**; revenue Rs.15.57cr, PAT Rs.5.60cr |
| 7c | 265 | Other Matters (c) | "The Statement includes the results for the quarter ended March 31, 2026, which are the..." | Q4FY26 balancing-figure caveat (standard) |
| — | 273–297 | Sign-off block: For Nayan Parikh & Co., Chartered Accountants, FRN 107023W, Aparna Gandhi, Partner, Membership No. 049687, Mumbai, dated Aug 6, 2026 | — | UDIN: **26049687PLSSSC6820** |

---

## 4. STANDALONE FINANCIAL RESULTS TABLE — LINE ITEMS (38 rows)

Table header: "Statement of Standalone Financial Results for the Quarter ended June 30, 2026" (₹ Crores). Columns: Q1FY27 (Reviewed), Q4FY26 (Refer Note 4), Q1FY26 (Reviewed), FY26 (Audited).

| Line | Item | Type | Flags |
|------|------|------|-------|
| 310 | I. Revenue from Operations | data row | — |
| 311 | II. Other Operating Revenue | data row | — |
| 312 | III. Other Income | data row | — |
| 313 | IV. Total Income (I+II+III) | subtotal | — |
| 314 | V. Expenses: | section header | no values |
| 315 | Cost of Materials Consumed | data row | — |
| 316 | Changes in inventories of finished goods, WIP and Stock-in-Trade | data row | wraps to line 317 |
| 318 | Sub-contracting Expenses | data row | — |
| 319 | Employee Benefits Expenses | data row | — |
| 320 | Finance Costs | data row | — |
| 321 | Depreciation & Amortisation | data row | — |
| 322 | Other Expenses | data row | — |
| 323 | Total Expenses | subtotal | — |
| 324 | VI. Profit Before Exceptional Item and Tax (IV-V) | subtotal | — |
| 325 | VII. Exceptional Item (Refer Note 5) | data row | blank in all 3 quarter columns, populated (17.38) only in FY26 column — PARTIAL_ZERO, not ZERO_STANDING (see Note 5, Labour Code impact) |
| 326 | VIII. Profit Before Tax (VI-VII) | subtotal | — |
| 327 | IX. Tax Expense | subtotal | — |
| 328 | 1. Current Tax | data row | — |
| 329 | 2. Deferred Tax Liability/(Asset) | data row | **blank in all 4 periods — ZERO_STANDING** |
| 330 | 3. (Excess)/Short Provision of Tax | data row | blank in 2 of 4 periods (Q1FY27, Q1FY26 blank; Q4FY26=0.30, FY26=0.30) — not fully zero, PARTIAL_ZERO |
| 331 | X. Profit for the period (VIII-IX) | subtotal | — |
| 332 | XI. Other Comprehensive Income/(loss) | section header | no values |
| 333 | A. OCI to be reclassified to P&L in subsequent periods | sub-header | wraps to line 334, no values |
| 335 | Exchange differences on translation of Financial Statements of Foreign Operations | data row | wraps to line 336 |
| 337 | Tax thereon (exchange differences) | data row | — |
| 338 | [unlabeled subtotal: net exchange difference after tax] | subtotal, unlabeled | label not printed in extraction — likely "Net of tax" caption dropped by OCR |
| 339 | B. OCI not to be reclassified to P&L in subsequent periods | sub-header | wraps to line 340, no values |
| 341 | Re-measurement gains/(losses) on defined benefit plans | data row | — |
| 342 | Tax thereon (remeasurement) | data row | — |
| 343 | [unlabeled subtotal: net remeasurement after tax] | subtotal, unlabeled | label not printed — same OCR gap as line 338 |
| 345 | Total Other Comprehensive Income (A+B) | subtotal | — |
| 348 | XII. Total Comprehensive Income for the period (X+XI) | subtotal | — |
| 349 | XIII. Paid up Equity Capital (Face Value Rs. 2 each) | data row | — |
| 350 | XIV. Other Equity | data row | blank in all 3 quarter columns, populated (2,305.52) only in FY26 column — PARTIAL_ZERO (standard year-end-only disclosure) |
| 351 | XV. Earning Per Equity Share (not annualised except FY) | section header | wraps to line 352, no values |
| 353 | (i) Par Value (Rs.) | data row | — |
| 354 | (ii) Basic (Rs.) | data row | — |
| 355 | (iii) Diluted (Rs.) | data row | — |

Footnote cross-reference (counted under NOTES, section 7 below, not double-counted here): line 357 "See accompanying notes forming part of the Standalone financial result."

---

## 5. CONSOLIDATED LIMITED REVIEW REPORT — AUDITOR M/s. Nayan Parikh & Co. (paragraphs)

Opinion type: **unmodified/unqualified review conclusion**. Contains **one Emphasis of Matter**, **one entity-list paragraph**, and **one Other Matters paragraph (5 sub-parts)**.

| # | Line | Paragraph | First 15 words | Flags |
|---|------|-----------|------------------|-------|
| 1 | 524 | Scope of review (intro) | "We have reviewed the accompanying statement of unaudited consolidated financial results of Transrail Lighting..." | Group = Parent + subsidiaries + share of JVs/associate |
| 2 | 532 | Management's responsibility | "This Statement, which is the responsibility of the Parent's Management and approved by the Parent's..." | — |
| 3 | 541 | Auditor's Responsibility | "Our responsibility is to express a conclusion on the Statement based on our review. We..." | — |
| 4 | 563 | SEBI Reg 33(8) procedures | "We also performed procedures in accordance with the circular issued by the SEBI under Regulation..." | — |
| 5 | 554 | Entity list paragraph | "The Statement includes unaudited standalone financial results of the following entities:" | **OCR_ERROR**: paragraph number rendered "S." not "5." in source extraction (see Count Test reconciliation note above); entity table enumerated in section 8 below |
| 6 | 612 | Conclusion | "Based on our review conducted and procedures performed as stated in paragraph 3 and 4..." | Unmodified conclusion |
| 7 | 623 | **Emphasis of Matter** | "We draw attention to Note 6 to the consolidated financial results regarding the search and..." | Same IT Dept Section 132 search & seizure matter as standalone report; conclusion NOT modified |
| 8 | 639 | **Other Matters** (parent para) | (heading only, sub-parts below) | 5 sub-parts |
| 8a | 629 | Other Matters (a) | "We did not review the financial results of five subsidiaries included in the Unaudited Consolidated..." | 5 subsidiaries unaudited by principal auditor; revenue Rs.3.33cr, **net loss** Rs.3.01cr; reviewed by other auditors, Ind AS adjustments furnished by management |
| 8b | 670 | Other Matters (b) | "We did not review the financial results of one subsidiary included in the Unaudited Consolidated..." | 1 subsidiary, **management-furnished / not reviewed by any auditor**; revenue Rs.0.32cr, PAT Rs.0.03cr |
| 8c | 681 | Other Matters (c) | "We did not review the financial results of five joint ventures whose financial statements reflect..." | 5 JVs unaudited by principal auditor, group share of net loss Rs.0.05cr; reviewed by other auditors |
| 8d | 701 | Other Matters (d) | "The Consolidated financial results also include the group's share of net profit of Rs. 0.01..." | 1 associate (CEDEC Engineering), **management-furnished / not reviewed by any auditor**, group share of profit Rs.0.01cr |
| 8e | 714 | Other Matters (e) | "The Statement includes the results for the quarter ended March 31, 2026 being the balancing..." | Q4FY26 balancing-figure caveat (standard) |
| — | 722–733 | Sign-off block: For Nayan Parikh & Co., Chartered Accountants, FRN 107023W, Aparna Gandhi, Partner, Membership No. 049687, Mumbai, dated Aug 6, 2026 | — | UDIN: **26049687KDJIXM2083** (different from standalone report UDIN, as expected — two distinct engagements same day) |

---

## 6. CONSOLIDATED FINANCIAL RESULTS TABLE — LINE ITEMS (49 rows)

Table header: "Statement of consolidated financial results for the quarter ended June 30, 2026" (₹ Crores). Columns: Q1FY27 (Reviewed), Q4FY26 (Refer Note 4), Q1FY26 (Reviewed), FY26 (Audited).

| Line | Item | Type | Flags |
|------|------|------|-------|
| 759 | I. Revenue from operations | data row | — |
| 760 | II. Other operating revenue | data row | — |
| 761 | III. Other income | data row | — |
| 762 | IV. Total Income (I+II+III) | subtotal | — |
| 763 | V. Expenses: | section header | no values |
| 764 | Cost of materials consumed | data row | — |
| 765 | Changes in inventories of finished goods, WIP and Stock-in-Trade | data row | wraps to line 766 |
| 767 | Sub-contracting expenses | data row | — |
| 768 | Employee benefits expense | data row | — |
| 769 | Finance costs | data row | — |
| 770 | Depreciation & amortisation | data row | — |
| 771 | Other expenses | data row | — |
| 772 | Total expenses | subtotal | — |
| 773 | VI. Profit before share of profit of JV and Associate, Exceptional item and Tax (IV-V) | subtotal | wraps to line 774 |
| 775 | VII. Share of profit of joint venture and Associate | data row | — |
| 776 | VIII. Profit Before Exceptional item and Tax | subtotal | — |
| 777 | IX. Exceptional Item (refer Note 5) | data row | blank in all 3 quarter columns, populated (17.38) only in FY26 column — PARTIAL_ZERO, mirrors standalone line 325 |
| 778 | X. Profit before tax (VIII-IX) | subtotal | — |
| 779 | XI. Tax expense | subtotal | — |
| 780 | 1. Current tax | data row | — |
| 781 | 2. Deferred tax liability/(asset) | data row | **blank in all 4 periods — ZERO_STANDING** |
| 782 | 3. (Excess)/Short provision of tax | data row | blank in 2 of 4 periods — PARTIAL_ZERO |
| 783 | XII. Profit for the period (X-XI) | subtotal | — |
| 784 | XIII. Other comprehensive Income | section header | no values |
| 785 | A. OCI to be reclassified to P&L in subsequent periods | sub-header | wraps to line 786, no values |
| 787 | Exchange differences on translation of financial statements of foreign operations | data row | wraps to line 788 |
| 789 | Tax thereon (exchange differences) | data row | — |
| 790 | [unlabeled subtotal: net exchange difference after tax] | subtotal, unlabeled | same OCR label gap as standalone table |
| 791 | B. OCI not to be reclassified to P&L in subsequent periods | sub-header | wraps to line 792, no values |
| 793 | Re-measurement gains/(losses) on defined benefit plans | data row | — |
| 794 | Tax thereon (remeasurement) | data row | — |
| 795 | [unlabeled subtotal: net remeasurement after tax] | subtotal, unlabeled | same OCR label gap |
| 796 | Total other comprehensive income (A+B) | subtotal | — |
| 799 | XIV. Total comprehensive Income for the period (XII+XIII) | subtotal | — |
| 801 | Profit for the year attributable to: | section header | no values |
| 802 | Owners of the company | data row | — |
| 803 | Non controlling interest | data row | **blank in all 4 periods — ZERO_STANDING** (no NCI in the group; template line retained) |
| 804 | OCI for the year attributable to: | section header | no values |
| 805 | Owners of the company | data row | — |
| 806 | Non controlling interest | data row | **blank in all 4 periods — ZERO_STANDING** |
| 807 | Total comprehensive income for the year attributable to: | section header | no values |
| 808 | Owners of the company | data row | — |
| 809 | Non controlling interest | data row | **blank in all 4 periods — ZERO_STANDING** |
| 811 | XV. Paid up equity capital (face value Rs. 2 each) | data row | — |
| 812 | XVI. Other equity | data row | blank in all 3 quarter columns, populated (2,256.56) only in FY26 column — PARTIAL_ZERO |
| 813 | XVII. Earning per equity share (not annualised except FY) | section header | wraps to line 814, no values |
| 815 | (i) Par value (Rs.) | data row | FY26 column value not captured in extraction (OCR gap) |
| 816 | (ii) Basic (Rs.) | data row | — |
| 817 | (iii) Diluted (Rs.) | data row | Q1FY27 and FY26 values OCR-garbled ("7." / "7. 78"); Q4FY26 blank — flag OCR_ERROR, verify against source PDF |

Footnote cross-reference (counted under NOTES, section 7 below): line 819 "See accompanying notes forming part of the consolidated financial results."

**Standalone vs consolidated PAT note (arithmetic-consistency feed for A5):** Standalone Profit for the period Q1FY27 = 110.55 (line 331); Consolidated Profit for the period Q1FY27 = 107.88 (line 783), difference of 2.67cr consistent with a Rs.0.32cr JV/associate profit pickup and other consolidation adjustments — no NCI line to absorb the gap since NCI is nil/blank throughout. Flag for A4/A5 to reconcile the standalone-to-consolidated PAT bridge given no visible minority interest bridge.

---

## 7. NUMBERED NOTES + UNNUMBERED FOOTNOTES (31 total: 14 standalone + 15 consolidated + 2 cross-reference footnotes)

### Standalone financial results notes (14)
| # | Line | First 15 words | Flags |
|---|------|------------------|-------|
| 1 | 370 | "The above unaudited standalone financial results as reviewed by the Audit Committee were approved..." | — |
| 2 | 373 | "The above unaudited standalone financial results are prepared in accordance with the Indian Accounting..." | — |
| 3 | 380 | "The Statutory Auditors of the Company have carried out a limited review of the standalone..." | Confirms unmodified report |
| 4 | 383 | "The figures for the quarter ended as on March 31, 2026 are the balancing figures..." | Referenced by Q4FY26 column header |
| 5 | 388 | "During the previous year ended March 31, 2026, pursuant to the notification of the Code..." | Labour Codes impact Rs.17.38cr (gratuity Rs.12.85cr + comp. absences Rs.4.53cr), recognised as Exceptional Item in FY26 — feeds line 325 PARTIAL_ZERO |
| 6 | 398 | "During the previous quarter ended March 31, 2026, the Income Tax Department carried out a..." | Section 132 search & seizure; EoM subject; company states no assets attached, no amount surrendered; Block IT Return notice received July 22, 2026, 60-day deadline |
| 7 | 422 | "During the quarter ended June 30, 2026, pursuant to the approval of the Board of..." | Acquisition of 100% stake in Gactel Turnkey Projects Limited from Ajanma Holdings Pvt Ltd, Rs.10cr consideration, effective June 25, 2026 — **ENTITY_CHANGE (ADDED)**, see section 8 |
| 8 | 429 | "During the quarter ended June 30, 2026, the Board of directors, at its meeting held..." | Voluntary winding up approved for Transrail Lighting Malaysia SDN. BHD. (wholly owned, no operations) — entity remains in consolidation list this quarter, pending removal |
| 9 | 436 | "During the quarter ended June 30, 2026, pursuant to the approval of the Board of..." | Further investment AED 12.5mn + AED 15.3mn (~Rs.32.35cr + Rs.40.25cr) in Transrail Trading LLC |
| 10 | 449 | "Subsequent to the quarter ended June 30, 2026, the Nomination and Remuneration Committee of the..." | ESOP 2023 grant of 1,89,000 options (5 shares/option) — subsequent event |
| 11 | 456 | "Subsequent to the quarter ended June 30, 2026, the Board of directors, at its meeting..." | Interim dividend Rs.3/share (FV Rs.2) declared for FY27 — subsequent event |
| 12 | 461 | "Subsequent to the quarter ended June 30, 2026, the Board of directors, at its meeting..." | QIP enabling resolution, up to Rs.600cr — subsequent event |
| 13 | 479 | "In accordance with Ind AS-108 "Operating Segments", the operations of the Company are categorised..." | Single segment: EPC |
| 14 | 482 | "Figures for the previous period have been regrouped to conform to the figures of the..." | Standard regrouping note |

### Consolidated financial results notes (15)
| # | Line | First 15 words | Flags |
|---|------|------------------|-------|
| 1 | 830 | "The above unaudited consolidated financial results as reviewed by the Audit Committee were approved..." | — |
| 2 | 835 | "The above unaudited consolidated financial results are prepared in accordance with the Indian Accounting..." | — |
| 3 | 842 | "The Statutory Auditors of the Company have carried out a limited review of the consolidated..." | Confirms unmodified report |
| 4 | 847 | "The figures for the quarter ended as on March 31, 2026 are the balancing figures..." | Referenced by Q4FY26 column header |
| 5 | 853 | "During the previous year ended March 31, 2026, pursuant to the notification of the Code..." | Same Labour Codes impact as standalone note 5, text says "standalone statement of profit and loss" even within the consolidated notes — possible copy-paste artifact, flag for A3 |
| 6 | 863 | "During the previous quarter ended March 31, 2026, the Income Tax Department carried out a..." | Same Section 132 search & seizure matter (text continues onto line 874 on next page) |
| 7 | 890 | "During the quarter ended June 30, 2026, pursuant to the approval of the Board of..." | Gactel Turnkey Projects Limited acquisition — **additional consolidated-only disclosure**: results restated per Ind AS 103 Appendix C (common control), restated comparatives based on management-certified financials — **ENTITY_CHANGE (ADDED)** |
| 8 | 900 | "During the quarter ended June 30, 2026, the Board of directors, at its meeting held..." | Malaysia SDN BHD voluntary winding up (consolidated-note wording: "not expect... any material impact") |
| 9 | 908 | "During the quarter ended June 30, 2026, pursuant to the approval of the Board of..." | Transrail Trading LLC further investment (same as standalone note 9) |
| 10 | 922 | "Subsequent to the quarter ended June 30, 2026, the Nomination and Remuneration Committee of the..." | ESOP 2023 grant (same as standalone note 10) |
| 11 | 929 | "Subsequent to the quarter ended June 30, 2026, the Board of directors, at its meeting..." | Interim dividend Rs.3/share (same as standalone note 11) |
| 12 | 933 | "Subsequent to the quarter ended June 30, 2026, the Board of directors, at its meeting..." | QIP enabling resolution (same as standalone note 12) |
| 13 | 954 | "a) In accordance with Ind AS-108 "Operating Segments", the operations of the Group are..." | Contains geographic revenue table (3 rows: In India / Outside India / Total, line 964/966/968) — counted in section 6 line_items total (line-items 88–90 of 90); sub-part (b) at line 958 notes non-current assets outside India <10%, not disclosed separately |
| 14 | 974 | "The above unaudited consolidated financial results include unaudited standalone financial results of the following..." | Entity list (see section 8) |
| 15 | 1016 | "Figures for the previous period have been regrouped to conform to the figures of the..." | Standard regrouping note |

### Unnumbered footnotes / cross-references (2)
| Line | Text | Flags |
|------|------|-------|
| 357 | "See accompanying notes forming part of the Standalone financial result" | Cross-reference footnote below standalone P&L table |
| 819 | "See accompanying notes forming part of the consolidated financial results." | Cross-reference footnote below consolidated P&L table |

---

## 8. CONSOLIDATION ENTITY LIST (17 entities; two internal listings cross-checked)

Primary listing = consolidated Limited Review Report para 5/"S." (lines 557–581). Cross-checked against Note 14 to the consolidated results (lines 965–999). Entity counts match (17 = 17) in both listings; two Joint Venture names differ in wording between the two listings **within the same filing** (see Flags column) — this is an internal-consistency issue, not a quarter-over-quarter ENTITY_CHANGE, since no prior-quarter ledger was available for this run.

| Category | # | Line (auditor report list) | Line (Note 14 list) | Entity name (auditor report list) | Flags |
|----------|---|------------------------------|------------------------|-------------------------------------|-------|
| Holding Company | — | 571 | 979 | Transrail Lighting Limited | — |
| Subsidiary | 1 | 573 | 981 | Transrail International FZE | — |
| Subsidiary | 2 | 574 | 982 | Transrail Structures America INC | — |
| Subsidiary | 3 | 575 | 983 | Transrail Lighting Nigeria Limited | — |
| Subsidiary | 4 | 576 | 984 | Transrail Lighting Malaysia SDN BHD | Voluntary winding up approved (Note 8) — pending removal, not yet removed this quarter |
| Subsidiary | 5 | 577 | 985 | Transrail Trading LLC | Further capitalised this quarter (Note 9), AED 27.8mn total |
| Subsidiary | 6 | 578 | 986 | Gactel Turnkey Projects Limited | **ENTITY_CHANGE (ADDED)** — newly acquired 100% stake, effective June 25, 2026 (Note 7); within-filing evidence only, no prior ledger to diff against |
| JV | 1 | 582 | 988–989 | "Transrail -FECP JV- Nigeria" (auditor report) vs "Transrail Lighting Limited - First Capital Energy & Power India limited JV-Nigeria (TLL-FECP JV-Nigeria)" (Note 14) | **Naming inconsistency within filing** — same JV, materially different name strings between the two internal lists; flag for A3 |
| JV | 2 | 583 | 990 | Transrail Hanbaek Consortium | — |
| JV | 3 | 584 | 991 | Railsys Engineers Pvt. Ltd. - Transrail Lighting Ltd. JV - "REPL-TLL JV" | — |
| JV | 4 | 585 | 992 | "METCON-TLL JV" (auditor report) vs "TLL Metcon Pravesh JV" (Note 14) | **Naming inconsistency within filing** — same slot/count position, different name strings; flag for A3 |
| JV | 5 | 586 | 993 | GECPL-TLL JV | — |
| JV | 6 | 587 | 1006 | ALTIS-TLL JV | — |
| JV | 7 | 588 | 1007 | TLL-ALTIS JV | — |
| JV | 8 | 589 | 1008 | ITD Cementation India Limited & Transrail Lighting Limited JV | — |
| JV | 9 | 590 | 1009 | T-G Joint Venture | — |
| Associate | 1 | 594 | 1012 | CEDEC Engineering Private Limited | — |

---

## 9. SIGNATURE / SIGN-OFF BLOCKS (5)

| Line(s) | Signatory | Designation | Timestamp / Date | Flags |
|---------|-----------|-------------|--------------------|-------|
| 98–107 | Monica Gandhi (digital signature block also shows overlapping text "TANAY TANAY GANDHI") | Company Secretary & Compliance Officer | Digitally signed, **2026.08.06 19:20:47 +05'30'** (7:20:47 p.m.) | Signature timestamp (19:20:47) is AFTER stated meeting conclusion (18:35) — no SIGNATURE_BEFORE_MEETING_END flag; but flag **OCR_ARTIFACT** for the garbled overlapping "TANAY TANAY GANDHI" text mixed into the Monica Gandhi digital-signature stamp — verify against source PDF whether this is a second signatory or a rendering artifact |
| 293–297 | Aparna Gandhi | Partner, Nayan Parikh & Co. (FRN 107023W), Membership No. 049687 | Mumbai, dated August 06, 2026 | Standalone Limited Review Report sign-off; UDIN 26049687PLSSSC6820 |
| 742–746 | Aparna Gandhi | Partner, Nayan Parikh & Co. (FRN 107023W), Membership No. 049687 | Mumbai, dated August 06, 2026 | Consolidated Limited Review Report sign-off; UDIN 26049687KDJIXM2083 (distinct UDIN from standalone, correctly two separate engagements) |
| 487–493 | Not named ("For and behalf and the board of directors of" — signatory name/title not captured) | — | Place: Mumbai (OCR: "Muml:J"), Date: August 06, 2026 | Standalone financial results board sign-off block — flag **MISSING_SIGNATORY_NAME** (likely an image-based signature not captured by OCR/extraction; verify against source PDF) |
| 1021–1022 | Not named ("For and behalf and the board of directors of Transrail Lighting Limited") | — | (no explicit date printed in this instance) | Consolidated financial results board sign-off block — flag **MISSING_SIGNATORY_NAME**, same as above |

---

## FLAG SUMMARY

- **ZERO_STANDING** (5): standalone Deferred Tax Liability/(Asset) [line 329]; consolidated Deferred Tax liability/(asset) [line 781]; consolidated Non Controlling Interest x3 [lines 803, 806, 809]
- **ENTITY_CHANGE** (1, within-filing evidence, no prior ledger available): Gactel Turnkey Projects Limited added as subsidiary this quarter [Note 7 standalone/consolidated, line 422/890]
- **OCR_ERROR** (2): consolidated Limited Review Report paragraph "5." rendered as "S." [line 554]; consolidated EPS Diluted row values garbled [line 817]
- **OCR_ARTIFACT** (1): overlapping "TANAY TANAY GANDHI" text within Monica Gandhi's digital signature block [lines 98–105]
- **MISSING_SIGNATORY_NAME** (2): both "for and on behalf of the board" sign-off blocks lack a named signatory [lines 487–493, 1021–1022]
- **Naming inconsistency within filing** (2, not ENTITY_CHANGE): JV #1 and JV #4 named differently between the auditor report entity list and Note 14 entity list [lines 582 vs 988–989; 585 vs 992]
- **PARTIAL_ZERO** (informational, not ZERO_STANDING — blank in quarter columns, populated only in FY column): Exceptional Item (standalone line 325, consolidated line 777); (Excess)/Short Provision of Tax (standalone line 330, consolidated line 782); Other Equity (standalone line 350, consolidated line 812)
- Data point for A5 arithmetic-consistency check: standalone-vs-consolidated PAT bridge (Q1FY27: 110.55 vs 107.88) has no NCI line to explain the gap since NCI is ZERO_STANDING throughout — flagged in section 6.
