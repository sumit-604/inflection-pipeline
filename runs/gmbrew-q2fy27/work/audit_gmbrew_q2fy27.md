# A5 ADVERSARY / COMPLETENESS AUDIT: G M Breweries Ltd (GMBREW), Q2 FY27 results

Agent: A5 adversary | model: claude-opus-5-5 | date: 2026-10-17
Inputs read: A4 review (runs/gmbrew-q2fy27/work/review_gmbrew_q2fy27.md), A1 fulltext (runs/gmbrew-q2fy27/extracted/gmbrew-results-q2fy27-fulltext.md, 620 lines), A1 structured (runs/gmbrew-q2fy27/extracted/gmbrew-results-q2fy27-structured.md, R001-R757), A2 ledger (runs/gmbrew-q2fy27/work/ledger_results_gmbrew_q2fy27.md). The source PDF, inputs/ and A3 output were not opened.
Anchor convention: "ft l###" = fulltext line. "rv l###" = A4 review line. "lg l###" = A2 ledger line. "R###" = A1 structured row. Raw values are Rs Lakhs; Rs Cr = Lakhs x 0.01.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

| Brief part | Location in review | Status |
|---|---|---|
| 1. Summary narrative | rv l564-l580, 15 lines (Results protocol governs, so 10-20 lines applies) | present |
| 2. Sector intelligence | rv l582-l589 | present |
| 3. Business-model intelligence | rv l591-l599 | present |
| 4. Competition intelligence | rv l601-l608 | present |
| 5. Forward map | rv l610-l622: make-or-break reading plus 6 dated catalysts, each with a bull and a bear fork | present |

Gate result: PASS. All five parts exist and carry real content. One cosmetic note on the forward map (A5-S6).

---

## 1. COVERAGE AUDIT

Method. I ran a fresh grep pass over the A1 fulltext for each enumeration unit: numbered notes (`^\d\)`), financial-table line items by page, RPT rows, agenda items, numbered auditor paragraphs (`^\d\. `), Statement B-E particulars, entities, dates, forward items and qualifiers. I diffed each count against the A2 ledger. Then I checked every ledger row against the A4 review (R-ID or fulltext-line citation).

Orphan standard. A4's preamble gives a blanket "No unreviewed ledger row" (rv l21). I accept that blanket for identifiers, boilerplate, subtotals and mirror twins. A ledger row that carries a financial value, a governance fact or a qualifier bearing on the review's conclusions, and is neither cited nor marked "reviewed, no finding", is an orphan.

| Category | A2 count | A5 fresh count | Orphan rows (in ledger, absent from A4) | Missing from ledger | Status |
|---|---|---|---|---|---|
| Numbered notes (ex agenda ft l36) | 10 | 10 (ft l114-l117, l126, l420-l423, l432) | none | none | PASS |
| Standalone P&L line items | 22 | 22 (ft l88-l112) | none | none | PASS |
| Consolidated P&L line items | 22 | 22 (ft l394-l418) | none | none | PASS |
| Standalone BS line items | 29 + M1 = 30 | 30 (ft l131-l170, incl. blank l167) | R279-R282 (non-current tax assets; other non-current assets) | none (M1 already logged, lg l267) | FAIL (orphan) |
| Consolidated BS line items | 30 | 30 (ft l437-l475) | twins R341-R344 (same items) | none | FAIL (same orphan) |
| Standalone CF line items | 35 | 35 (ft l194-l235) | R417-R418 (other non-current assets change) | none | FAIL (same orphan) |
| Consolidated CF line items | 35 | 35 (ft l501-l542) | twins R491-R492 | none | FAIL (same orphan) |
| Line items, total | 173 | 173 | as above | none | count match |
| RPT Annexure 1 rows | 10 + total | 10 + total (ft l250-l260) | R539-R568 (rows 1-6) and entities R632-R636 | none | FAIL (orphan) |
| Agenda items | 1 | 1 (ft l36-l45) | none | none | PASS |
| Review-scope statements by the company | 2 (R699, R746) | 2 (ft l43-l45, l295-l298) | R699, R746 | none | FAIL (orphan) |
| Numbered LRR paragraphs | 15 (A2 counted A1 rows R698, R699, R745-R757, lg l17; not a fulltext grep) | 9 (ft l313, l319, l327, l352, l561, l568, l576, l598, l601); 8 have a row | none | consolidated LRR para 2, ft l568-l574 | FAIL (missing from ledger) |
| Statement C particulars | 3 (R601-R603) | 5 (ft l278 1A, l279 1B, l282 2A, l283 2B, l285 item 3) | none | ft l278 and l282, "Total amount outstanding as on date", value blank | FAIL (missing from ledger) |
| Statements B, D, E | 3 | 3 (ft l272, l289, l294) | none | none | PASS |
| Entities | 31 | 31 | R632-R636 sit inside the RPT orphan | none | see RPT row |
| Dates | 50 | 50 | none (signature stamps cited by line, ft l368, l614) | none | PASS |
| Forward | 1 | 1 (ft l48) | none (R647 cited) | none | PASS |
| Qualifiers | 60 | 60 | R699, R746 (above) | none (RPT approval-remark cells, A5-S8) | see scope row |
| Parse fragments | 8 pairs | 8 pairs | n.a. | none | PASS |
| ID accountability | 757 of 757 | 757 parsed | | | PASS |

Coverage findings.

- A5-M1 (MISSING, loop A3). RPT rows 1-6 are orphaned. R539-R568, ft l250-l255. KMP remuneration is 201.90 Lakh in H1 (CMD 90.00, ED Jyoti Almeida Kashyap 66.00, ED Kiran Parashare 18.00, CFO 15.13, CS 12.77). That equals 33.9% of H1 employee benefits of 595 Lakh (ft l97); whether the line includes it is ND. Lease rentals to the CMD are 148.87 Lakh in H1 against 297.74 Lakh approved (ft l255). The balance sheet prints no lease-liability or right-of-use line (ft l131-l170), and H1 finance cost is 11 Lakh (ft l99). So the rentals are most likely expensed in other expenditure [INFERENCE]. That makes them about 5.6% of H1 other expenditure (2,638 Lakh, ft l101), and the one related-party component of the line A4 calls "not split" (rv l195, Q2 rv l477). The review cites RPT rows 7-10 (R569-R580, R585, R587) but never rows 1-6. The word "lease" does not appear in the review.
- A5-M2 (MISSING, loop A3). R279-R282 and R417-R418 are orphaned. (a) Non-current tax assets rose from 95.90 to 136.98 Lakh (+41.08, ft l138). This closes the FN-05 offset exactly. The tax gap is 2,591 expense less 2,300 paid = 291, plus the 41.08 asset rise = 332.08 Lakh. The capex residual is 534.49 less BS-implied additions of 206.25 = 328.24 Lakh, plus the 3.94 Lakh provisions rise that the CF omits = 332.18 Lakh. The two sides differ by 0.10 Lakh. The review shows only 2.91 vs 3.28 Cr (rv l483), so the offset it asserts does not show in its own numbers. (b) Other non-current assets are 4,976.33 Lakh (49.76 Cr, ft l139). That is larger than net PPE of 40.42 Cr and rose in both half-years: CF outflow 404.73 Lakh in H1 FY27 and 669.60 Lakh in H1 FY26 (ft l208). The content is ND. The line is missing from the Step 5 tables and from the Step 7 list of operating capital (rv l434), which names OCA, OCL and other NC financial assets as "must be known first" but not this line.
- A5-M3 (MISSING, loop A3). R699 and R746 are orphaned. The company says twice that the limited review covers the half year. The cover letter says "Limited Review Report ... for Quarter/half year ended September 30, 2026" (ft l43-l45). Section E says the auditors "have issued Limited Review Reports on Financial Statements as prepared under the Companies Act, 2013 ... for the Quarter/ Half year ended September 30, 2026" (ft l295-l298). FN-10, flag 4 and Q12 (rv l78, l325, l549, l487) cite only the auditor's quarter-only wording (ft l311, l559). A bear claim carries the same bar as a bull claim, so both readings belong in FN-10. The auditor's own wording still governs the review status.
- A5-M4 (MISSING, loop A2). Consolidated LRR para 2 (ft l568-l574) has no structured row and no ledger entry. It carries "has been approved by the Board of Directors" (ft l569). That sentence is part of the FN-09 evidence for the consolidated report, which was signed at 10:28:21 and 10:28:32 (ft l590, l614), before the 11:30 board (ft l46). A2's auditor_paras test counted A1 rows, not fulltext paragraphs (lg l17), so the drop passed. A2 should log it as MISSING_FROM_STRUCTURED M2 and re-run the count against the fulltext.
- A5-M5 (MISSING, loop A2). Statement C items 1A and 2A, "Total amount outstanding as on date" (ft l278, l282), have no value in the fulltext and no row. The ledger handled the blank standalone current-tax-liability row as M1 (lg l26, l267). These two blank rows need the same treatment. The item-2 header carries a garbled cell (ft l281); flag it. The debt-free reading still stands on item 3, "Total financial indebtedness ... Nil" (ft l285, R603), and on a balance sheet that prints no borrowings line.

Inherited A1 defect, confirmed and already routed (no A5 loop): EX-1. ft l475 prints 1,28,473.47 (30.09.2026) and 1,22,542.11 (31.03.2026). R387 holds 1,22,542.11 labelled 30.09.2026, and R388 holds ZERO_STANDING labelled 31.03.2026. A2 flagged it (lg l27). A4 isolates it and uses Total Assets instead (rv l20). No review number depends on it.

---

## 2. ARITHMETIC AUDIT

I recomputed every derived cell in A4's tables from the raw Lakh values. Casts first: every P&L total ties in all 12 columns, and H1 = Q1 + Q2 on every line. Both balance sheets foot at both dates. Both cash flows cast A + B + C to the cash change and the closing cash, for both years. The BS changes reconcile to the standalone CF line by line, except the PPE and tax pair (A5-M2).

| Metric (A4 location) | A4 value | Recomputed (from raw Lakhs) | Source lines | Status |
|---|---|---|---|---|
| Net revenue Q2FY26 / Q1FY27 / Q2FY27 / H1FY26 / H1FY27 / FY26 (rv l115) | 180.52 / 199.58 / 213.52 / 343.38 / 413.10 / 747.85 | 18,052 / 19,958 / 21,352 / 34,338 / 41,310 / 74,785 | ft l90 less l98 | PASS |
| Op EBITDA = PBT + D + FC - OI (rv l146) | 44.81 / 46.45 / 49.91 / 75.71 / 96.36 / 180.71 | 4,481 / 4,645 / 4,991 / 7,571 / 9,636 / 18,071 | ft l91, l99, l100, l105 | PASS |
| Op EBITDA margin, gross (rv l147) | 6.24 / 5.79 / 5.80 / 5.58 / 5.79 / 6.07% | 6.242 / 5.785 / 5.799 / 5.584 / 5.793 / 6.071% | ft l90 | PASS |
| Op EBITDA margin, net (rv l148) | 24.82 / 23.27 / 23.37 / 22.05 / 23.33 / 24.16% | 24.823 / 23.274 / 23.375 / 22.048 / 23.326 / 24.164% | derived | PASS |
| Reported EBITDA (rv l149) | 47.84 / 52.00 / 54.05 / 83.87 / 106.05 / 210.95 | 4,784 / 5,200 / 5,405 / 8,387 / 10,605 / 21,095 | ft l99, l100, l105 | PASS |
| Reported EBITDA margin, net (rv l150) | 26.50 / 26.05 / 25.31 / 24.42 / 25.67 / 28.21% | 26.501 / 26.055 / 25.314 / 24.425 / 25.672 / 28.207% | derived | PASS |
| Core PBT = PBT - OI (rv l151) | 43.60 / 44.88 / 48.37 / 73.03 / 93.25 / 175.20 | 4,360 / 4,488 / 4,837 / 7,303 / 9,325 / 17,520 | ft l91, l105 | PASS |
| OI / PBT (rv l152) | 6.50 / 11.01 / 7.88 / 10.05 / 9.41 / 14.72% | 6.498 / 11.005 / 7.884 / 10.050 / 9.413 / 14.720% | ft l91, l105 | PASS |
| ETR (rv l153) | 25.18 / 25.16 / 25.18 / 25.18 / 25.17 / 23.66% | 25.177 / 25.164 / 25.176 / 25.176 / 25.170 / 23.661% | ft l105, l106 | PASS |
| PAT margin, gross / net (rv l154-l155) | 4.86..5.27% / 19.33..20.97% | 4.860 / 4.700 / 4.565 / 4.481 / 4.631 / 5.269%; 19.328 / 18.910 / 18.401 / 17.692 / 18.647 / 20.971% | ft l90, l107 | PASS |
| Gross margin on net revenue (rv l156) | 31.06 / 31.32 / 30.99 / 28.66 / 31.15 / 31.34% | 31.060 / 31.321 / 30.995 / 28.656 / 31.152 / 31.336% | ft l94, l96 | PASS |
| CoM / net revenue (rv l157) | 68.85 / 69.27 / 68.64 / 71.46 / 68.94 / 68.44% | 68.846 / 69.271 / 68.640 / 71.463 / 68.945 / 68.439% | ft l94 | PASS |
| Other expenses / net revenue (rv l158) | 4.51 / 6.57 / 6.21 / 4.89 / 6.39 / 5.49% | 4.509 / 6.569 / 6.215 / 4.893 / 6.386 / 5.486% | ft l101 | PASS |
| Excise intensity (rv l159) | 74.85 / 75.14 / 75.19 / 74.67 / 75.17 / 74.88% | 74.853 / 75.143 / 75.190 / 74.674 / 75.167 / 74.876% | ft l98, l90 | PASS |
| Q2 YoY: gross rev / net rev / Op EBITDA / EBIT / OI / core PBT / PBT / PAT / EPS (rv l171-l183) | +19.89 / +18.28 / +11.38 / +11.01 / +36.63 / +10.94 / +12.61 / +12.61 / +12.64% | +19.889 / +18.281 / +11.381 / +11.007 / +36.634 / +10.940 / +12.610 / +12.611 / +12.639% | ft l90-l112 | PASS |
| Margin change YoY, net / gross (rv l174-l175) | -145 / -44 bps | -144.8 / -44.3 bps | derived | PASS |
| H1 YoY: net rev / Op EBITDA / margin / core PBT / PAT (rv l185) | +20.30% / +27.27% / +128 bps / +27.69% / +26.80% | +20.304% / +27.275% / +127.8 bps / +27.687% / +26.798% | derived | PASS (Op EBITDA within rounding; A5-S1) |
| H2 FY26 OI share (rv l193) | 22.08 Cr, 73.0% | 2,208 Lakh, 73.02% | ft l91 | PASS |
| Other-exp step and share (rv l195) | +63.02%, 1.70 pp | +63.022%, 1.706 pp | ft l101 | PASS (pp within rounding; A5-S1) |
| Derived Q1 FY26: gross / net / margin / core PBT (rv l205) | 638.01 / 162.86 / 18.97% / 29.43 | 63,801 / 16,286 / 18.973% / 2,943 | ft l88, l98, H1 FY26 less Q2 FY26 | PASS |
| H2 FY26: net / per qtr / gross / margin / core PBT / ETR (rv l209) | 404.47 / 202.24 / 1,620.71 / 25.96% / 102.17 / 22.67% | 40,447 / 20,223.5 / 1,62,071 / 25.960% / 10,217 / 22.672% | FY26 less H1 FY26 | PASS |
| QoQ run-rates (rv l206, l209-l211) | +10.84 / +12.03 / -1.31 / +6.98% | +10.844 / +12.029 / -1.313 / +6.985% | derived | PASS |
| H1 run-rate test (rv l216) | 206.55, +3.37% | 20,655, +3.374% | derived | PASS |
| PAT bridge components (rv l226-l238) | +10.25 / -0.14 / +0.12 / -5.13 / +5.10 / -0.30 / -0.03 / +1.11 / +5.88 / -1.48 / +4.40 | +10.250 / -0.140 / +0.12 / -5.13 / +5.10 / -0.30 / -0.03 / +1.11 / +5.88 / -1.481 / +4.40; % of 34.89 all tie | derived | PASS |
| Recurring split; OI reversion (rv l241-l242) | 3.57 (81%) / 0.83 (19%); 38.46, +10.2% | 3.569 (81.1%) / 0.831; 38.460, +10.23% | derived | PASS |
| FY26 tax shield (rv l244) | 3.10 Cr | 309.9 Lakh (20,544 x 25.17% less 4,861) | ft l105, l106 | PASS |
| CFO, CFO/PAT, pre-WC/PAT (rv l258-l260) | 40.03 / 95.53; 0.66x / 1.24x; 0.95x / 0.95x | 4,002.86 / 9,553.02; 0.659x / 1.240x; 0.950x / 0.952x | ft l217, l215 | PASS |
| FCF and FCF after IP (rv l263-l264) | 40.05 / 90.19; 34.05 / 87.94 | 4,004.80 / 9,018.53; 3,405.17 / 8,793.98 | ft l217, l220, l221 | PASS |
| Investments share of CFO (rv l265) | 93% | 93.42% | ft l222, l217 | PASS |
| WC change (rv l266) | -17.68 / +22.17 / +39.85 | -1,768.47 / +2,216.79 / +3,985.26 | ft l202, l214 | PASS |
| Receivable / inventory / payable days, CCC (rv l271-l274) | 1.09 / 2.24; 24.42 / 21.24; 7.92 / 15.89; 17.59 / 7.59 | 1.092 / 2.235; 24.415 / 21.238; 7.912 / 15.894; 17.59 / 7.58 | ft l142, l144, l163; derived | PASS (Sep receivable and Mar payable days within rounding; A5-S1) |
| BS moves: PPE / CWIP / IP / investments / ONCFA / OCA / OCL / OCFL (rv l275-l282) | -1.68 / +0.74 / +2.25 / +89.24 / +12.74 / -41.06 / +4.61 / -18.74 (-52.7%) | -168.02 / +74.37 / +224.55 / +8,923.98 / +1,273.59 / -4,105.50 / +460.89 / -1,874.41 (-52.66%); each equals its CF line | ft l131-l165, l204-l222 | PASS |
| Net cash: cash + bank; incl. investments (rv l284-l285) | (12.16) / (2.05); (582.56) / (661.69) | 1,215.58 / 204.66; 58,255.34 / 66,168.40 | ft l136, l145, l146 | PASS (incl.-investments cells within rounding; A5-S1) |
| Equity, OE roll, dividend share (rv l286-l287) | +58.64; 23.9% | +5,864.21 (PAT 7,703 less dividend 1,839.09 = 5,863.91; 0.30 Lakh is PAT rounding); 23.88% | ft l155, l231 | PASS |
| Consolidated vs standalone gaps (rv l294-l317) | CFO -0.0011; assets +1.0061; liabilities +1.0117; equity -0.0056; OCL CF +1.0105 = R585; CF PBT -0.0042 | -0.11 / +100.61 / +101.17 / -0.56 / +101.05 (561.94 less 460.89) / -0.42 Lakh | ft l524, l455, l474, l460, l519, l212, l259 | PASS |
| P3 non-operating share (rv l392) | 876.36 / 1,283.73 = 68.3% | 87,635.63 / 1,28,372.86 = 68.27% | ft l133, l136, l149 | PASS |
| TTM bases (rv l418-l423) | 157.16 / 173.11 / Rs 75.77 / 817.57 / 201.36 / 31.77 | 15,716 / 17,311 / 75.77 / 81,757 / 20,136 / 3,177 | ft l91, l107, l112 | PASS |
| ROE H1 annualised (rv l433) | 13.9% on 1,107.59 | 15,406 / 1,10,758.47 = 13.91% | ft l107, l155 | PASS |
| Tax gap; capex residual (rv l483, l555) | 2.91; 3.28 | 291; 328.24 Lakh (534.49 less 206.25 BS-implied) | ft l106, l215, l220, l131-l134 | PASS (offset incomplete without R279/R280; A5-M2) |
| Promoter-group dividend share (rv l522) | 15.30 Cr, 83.2% | 1,530.47 / 1,839.09 = 83.22% | ft l256-l258, l231 | PASS (basis caveat A5-S7) |
| Implied shares; EPS-implied gap (rv l55, l58) | 2.2855 Cr; 0.03-0.05% | 2,28,55,400; FY26 228.48 Lakh (-0.03%), Q2 228.43 Lakh (-0.05%) | ft l153, l107, l112 | PASS |

Result: no mismatch above rounding. Five cells were rounded from rounded intermediates; each differs by 0.01 (A5-S1, STYLE).

---

## 3. ADVERSARIAL READ

The three most positive claims in A4's review, each attacked from the same extract.

### Claim 1. Cash is strong: "Cash from operations was Rs 95.53 Cr in the half, 1.24 times profit" (rv l572); FCF 90.19 "Strong in H1" (rv l263); cash direction "positive" (rv l322). The flag attributes the strength to "a seasonal 41.06 Cr OCA release" (rv l547; WC row "Release driven by OCA", rv l266).

Bear counter. The OCA release does not explain the year-on-year jump from 0.66x to 1.24x. OCA released 4,012.75 Lakh in H1 FY26 and 4,105.50 Lakh in H1 FY27 (ft l207), only 92.75 Lakh more. The +3,985.26 Lakh YoY working-capital swing comes from two other lines:
- Other current financial liabilities: outflow -5,785.98 to -1,874.41, a +3,911.57 Lakh swing (ft l213).
- Trade payables: -46.34 to +1,370.88, a +1,417.22 Lakh swing (ft l210). Payable days went from 7.91 to 15.89 (ft l163).
The filing does not disclose the content of either line. The other lines net to -1,343.53 Lakh: OCL -714.39, ONCFA -1,273.59, receivables -281.14, inventories +562.75, ONCA +264.87, ONCL +5.22. Remove only the payables stretch and H1 CFO is 81.82 Cr, 1.06x PAT. Under the FN-05 reading that 3.28 Cr of "capex" is tax paid, CFO is 92.25 Cr, 1.20x. Pre-WC conversion is 0.95x in both years.
Survives: YES. Graft into A4: the YoY driver split in Step 5A/5D and flag 2. Type MISSING (A5-M6).

### Claim 2. Growth is real and stepping up: "The headline growth is real" (rv l190); "About 81% of that gain came from the business" (rv l570); "revenue is stepping up. Q2 FY27 net revenue is the highest quarter on record in this filing" (rv l214).

Bear counter. Against the trailing base the step-up is small, and the profit line sits below it. Q2 FY27 net revenue of 213.52 Cr is only 5.6% above the H2 FY26 quarterly average of 202.24 Cr; Q1 FY27 was 1.3% below it. Q2 FY27 core PBT of 48.37 Cr is 5.3% below the H2 FY26 average of 51.09 Cr. Op EBITDA grew 11.38% on net revenue up 18.28%: negative operating leverage. Q3 and Q4 FY26 cannot be separated (H2 total 404.47 Cr), so either could exceed 213.52 Cr.
Survives: the substance is ALREADY IN A4 (rv l214 margin plateau, rv l218 core PBT below the H2 average, rv l173 growth below revenue). No graft needed. The "highest quarter on record" wording needs a qualifier (A5-S2, STYLE).

### Claim 3. Cost position is strong: "G M Breweries looks strong on cost and cash: debt is nil and buyers pay almost at once [FILED]" (rv l605); "Material cost held steady" (rv l569); "Gross margin is steady near 31% [FILED]" (rv l594).

Bear counter (a). No filed evidence supports "strong on cost". The filing holds no peer data, and A4 itself says "Peer margins and volumes are ND" (rv l608). This quarter shows cost pressure: other expenditure is up 63.0% (ft l101) and the Op EBITDA margin fell 145 bps. The facts after the colon (debt nil, ft l285; receivables 2.2 days, ft l144) support "strong on cash" only. A comparative claim tagged [FILED] with no filed comparator is a claim the extract does not support. Survives: YES. Type FACTUAL (A5-F1).

Bear counter (b). "Steady near 31%" holds only for the three printed quarters. Derived Q1 FY26 (H1 FY26 less Q2 FY26, ft l88, l94, l96, l98):
- Net revenue 16,286 Lakh; CoM 12,111 Lakh (74.36% of net revenue); inventory change -58 Lakh.
- Gross margin 25.99%, against 31.06% in Q2 FY26.
That is a 5.07 pp swing inside FY26. At Q2 FY27 net revenue it is worth about 10.8 Cr a quarter, about twice the 5.13 Cr other-expenditure rise that A4 makes the key test (rv l463-l466). On filed history, material cost is the larger margin variable. A4's own H1 bridge shows it: the CoM ratio fell from 71.46% to 68.94% (rv l246), but the brief calls it steady. Survives: YES. Graft into the Step 3 table, brief part 3 and the 8C "read with" list. Type MISSING (A5-M7).

### Mandatory acquisition-economics probe

No acquisition, merger or stake buy is described. The board outcome has one agenda item, the results (ft l36-l45). No note describes a deal (ft l114-l117), and Statement B is "Not Applicable" (ft l272). Three purchases appear:
- 8,923.98 Lakh of financial-asset investments, counterparty and instrument not disclosed (ft l222).
- 224.55 Lakh of investment property (ft l221).
- A 101.05 Lakh loan to the wholly owned subsidiary Buildfort (ft l259). Buildfort's H1 loss is 0.42 Lakh and its net worth about 0.44 Lakh (derived, rv l317).
No target earnings exist, so price / target PAT is undefined for all three.

Nearest test: the economics of the book that received 93% of H1 CFO.
- Average non-operating book: 951.01 Cr. This is investments + investment property + other NC financial assets + cash and bank, 90,395.62 Lakh at Mar-26 and 99,806.82 Lakh at Sep-26 (ft l133, l136, l137, l145, l146).
- TTM other income: 31.77 Cr (3,024 - 816 + 969 Lakh, ft l91).
- Yield: 31.77 / 951.01 = 3.34% pre-tax, about 2.50% post-tax at the 25.17% interim ETR. The book is carried at about 40x its recognised post-tax earnings.
- On the investments line alone the yield is 5.17% (31.77 / 615.02 average).
- H1 OI is all cash items: interest 487.12 + dividend 38.16 + other non-operating 443.71 = 968.99 Lakh (ft l199-l201). So no fair-value gain is recognised. Dividends are 0.38 Cr on a 659.64 Cr book.
Bear reading: unless unrecognised gains exist (FN-01, category ND), each rupee moved from the liquor business into this book earns 3.3-5.2% pre-tax. That pulls H1 ROE down to 13.9%.
Survives: YES. A4 says "Treasury drags ROE" (rv l433) but gives no return number. Graft the yield into Step 7, FN-06 and the Q3/Q4 rationale. Type MISSING (A5-M8).

---

## 4. FINDINGS BY TYPE

FACTUAL
- A5-F1 [loop A4]. Brief, competition (rv l605): "looks strong on cost" is tagged [FILED] with no filed comparator, and the filing shows cost pressure (ft l101; margin -145 bps). Fix: re-tag "strong on cost" as INFERENCE or drop it. Keep "debt nil, receivables about 2 days [FILED]".

MISSING
- A5-M1 [loop A3]. Orphan RPT rows 1-6 (R539-R568, R632-R636; ft l250-l255): KMP remuneration 201.90 Lakh and CMD lease rentals 148.87 Lakh in H1. No lease-liability line is printed. Needs an FN, a question (property leased, annual rent, term, Ind AS 116 treatment, Q2 FY26 amount) and a governance line.
- A5-M2 [loop A3]. Orphan R279-R282, R417-R418 (twins R341-R344, R491-R492). The non-current tax asset rise of 41.08 Lakh closes the FN-05 offset (332.08 vs 332.18 Lakh). Other non-current assets of 49.76 Cr build every H1, content ND, and are missing from Step 7 operating capital.
- A5-M3 [loop A3]. Orphan R699 and R746 (ft l43-l45, l295-l298): the company says the reviews cover the quarter and half year and the Companies Act financial statements. FN-10, flag 4 and Q12 show only the auditor's quarter-only wording.
- A5-M4 [loop A2]. Missing from ledger: consolidated LRR para 2 (ft l568-l574). The auditor_paras count test was circular (lg l17). Add as MISSING_FROM_STRUCTURED and re-run the count on the fulltext.
- A5-M5 [loop A2]. Missing from ledger: Statement C 1A and 2A "Total amount outstanding as on date" (ft l278, l282), value blank. Treat like M1 and flag the garbled cell at ft l281.
- A5-M6 [loop A4]. Cash attribution (rv l266, l321-l322, l547). The YoY CFO jump comes from OCFL (+39.12 Cr) and payables (+14.17 Cr), not OCA (+0.93 Cr). Add the split and the 1.06x ex-payables reading.
- A5-M7 [loop A4]. Gross-margin volatility (rv l569, l594, l205). Add the derived Q1 FY26 gross margin of 25.99% and the 5.07 pp swing; add gross margin to 8C.
- A5-M8 [loop A4]. Treasury recognised yield (rv l433, l597-l598). Add 3.34% pre-tax on the 951.01 Cr average book (5.17% on investments alone). OI is all cash items, with no fair-value gain.

CONTRADICTION
- none.

STYLE (logged, no loop)
- A5-S1 to A5-S8, listed under STYLE NOTES.

---

## VERDICT

**INCOMPLETE.** Loop back to **A2**, the earliest failing agent. The chain then re-runs A3, A4 and A5.
- A2 (MISSING, small): add the two dropped units (A5-M4, A5-M5) and fix the auditor_paras count to grep the fulltext.
- A3 (MISSING): review the three orphan groups (A5-M1, A5-M2, A5-M3) and update FN-05 and FN-10.
- A4 (FACTUAL and MISSING): fix the "strong on cost [FILED]" tag (A5-F1) and graft the three surviving bear counters (A5-M6, A5-M7, A5-M8).
The arithmetic audit passed. The deliverable gate passed. The protocol verdict PROCEED WITH FLAGS is not challenged on the arithmetic. The A3 and A4 additions may add flags; none of them lifts the cash cap.

---

## STYLE NOTES (logged; no re-run)

- A5-S1. Five cells were rounded from rounded intermediates. Compute from raw Lakhs. H1 Op EBITDA YoY 27.27% (raw 27.275%, rv l185). Other-expense share change 1.70 pp (raw 1.706, rv l195). Sep receivable days 2.24 (raw 2.235, rv l271). Mar payable days 7.92 (raw 7.912, rv l273). Net cash incl. investments 582.56 / 661.69 (raw 582.55 / 661.68, rv l285).
- A5-S2. "Q2 FY27 net revenue is the highest quarter on record in this filing" (rv l214). Q3 and Q4 FY26 are not separable. Say "highest of the quarters the filing prints individually".
- A5-S3. "Q4 is where OI concentrates" (rv l193) and "year-end OI and tax true-up" (rv l215). The filing supports H2 only (22.08 Cr). Say H2, or tag Q4 as INFERENCE.
- A5-S4. "That line explains the whole margin fall" (rv l195). Other expenditure took 171 bps of net revenue against a 145 bps fall; employee-cost leverage (+32 bps) and gross margin (-7 bps) offset. Say "more than the whole fall".
- A5-S5. Direct tax paid of 23.00 and 18.00 Cr is used without row IDs (rv l260, l483). Cite R429 and R430 (ft l215).
- A5-S6. Forward map "Now, FY26 annual report notes" (rv l618). Give a date, or write "date ND" as M2 does (rv l523).
- A5-S7. "Promoter-group dividends 15.30 Cr = 83.2% of 18.39 Cr paid" (rv l522) mixes RPT values (ft l256-l258) with CF cash paid (ft l231). Read as a holding, about 83% would sit above the 75% maximum promoter holding under the minimum public shareholding rule [INFERENCE, regulatory, not in the filing]. Add a caveat that the ratio is not a holding figure; the Q2 shareholding pattern (M1, by 21-Oct-2026) settles it.
- A5-S8. A1 did not capture the RPT text cells "Remarks on approval by audit committee: Approved" and "Value ratified: -" (ft l249-l259). All ten rows show approved, none ratified. Extraction note only.

---

```yaml
stage: A5-adversary
company: "GMBREW"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
verdict: INCOMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
  forward_map: present
coverage:
  orphan_rows:
    - "R539-R568 and R632-R636: RPT rows 1-6, KMP remuneration 201.90 Lakh H1 and CMD lease rentals 148.87 Lakh H1 (ft l250-l255); never cited in A4"
    - "R279-R282 and R417-R418 (twins R341-R344, R491-R492): non-current tax assets +41.08 Lakh, other non-current assets 4,976.33 Lakh, CF -404.73 / -669.60 Lakh (ft l138, l139, l208)"
    - "R699 and R746: company states the LRRs cover the Quarter/Half year and the Companies Act financial statements (ft l43-l45, l295-l298); absent from FN-10, flag 4 and Q12"
  missing_from_ledger:
    - "ft l568-l574: consolidated LRR para 2 (management responsibility, 'has been approved by the Board of Directors', Ind AS 34); no structured row, no ledger entry"
    - "ft l278 and ft l282: Statement C items 1A and 2A 'Total amount outstanding as on date', value blank; no structured row, no ledger entry"
arithmetic_mismatches: []
surviving_bear_counters:
  - claim: "H1 CFO 95.53 Cr = 1.24x PAT, strength attributed to the seasonal 41.06 Cr OCA release (rv l547, l266, l321-l322)"
    counter: "OCA release was flat YoY (4,012.75 to 4,105.50 Lakh, +92.75). The +3,985.26 Lakh YoY WC swing is a smaller OCFL outflow (+3,911.57) and a trade-payables stretch (+1,417.22; payable days 7.91 to 15.89), both of undisclosed content. Ex the payables stretch, CFO/PAT = 1.06x; under the FN-05 tax reading, 1.20x."
    source_line: "ft l207, l210, l213, l217, l163"
    type: MISSING
  - claim: "G M Breweries looks strong on cost and cash [FILED] (rv l605)"
    counter: "No filed comparator exists (peer data ND, rv l608). This quarter other expenditure rose 63.0% and the op margin fell 145 bps. The [FILED] facts (debt nil, receivables about 2 days) support cash only."
    source_line: "ft l101, l144, l285"
    type: FACTUAL
  - claim: "Material cost held steady; gross margin steady near 31% [FILED] (rv l569, l594)"
    counter: "Derived Q1 FY26 gross margin is 25.99% (CoM 74.36% of net revenue) against 31.06% in Q2 FY26: a 5.07 pp swing inside FY26, about 10.8 Cr a quarter at Q2 FY27 net revenue, twice the 5.13 Cr other-expenditure rise."
    source_line: "ft l88, l94, l96, l98 (H1 FY26 less Q2 FY26)"
    type: MISSING
  - claim: "Acquisition-economics probe: 93% of H1 CFO moved into investments (rv l576, l597-l598, l433); no deal, so price/PAT undefined"
    counter: "TTM other income 31.77 Cr on a 951.01 Cr average non-operating book = 3.34% pre-tax (about 2.50% post-tax, about 40x recognised post-tax earnings); 5.17% on investments alone. H1 OI is all cash items (968.99 Lakh), no fair-value gain; dividends 0.38 Cr on a 659.64 Cr book."
    source_line: "ft l91, l133, l136, l137, l145, l146, l199-l201"
    type: MISSING
findings_by_type:
  factual:
    - "A5-F1 [A4] rv l605: 'looks strong on cost' tagged [FILED] with no filed comparator; filing shows other expenditure +63.0% and op margin -145 bps. Re-tag as INFERENCE or drop 'on cost'."
  missing:
    - "A5-M1 [A3] Orphan RPT rows 1-6 (R539-R568, R632-R636; ft l250-l255): KMP remuneration 201.90 Lakh H1 (33.9% of H1 employee benefits 595 Lakh) and CMD lease rentals 148.87 Lakh H1 (297.74 approved); no lease-liability or ROU line (ft l131-l170); rentals likely in other expenditure (INFERENCE)."
    - "A5-M2 [A3] Orphan R279-R282, R417-R418: non-current tax asset +41.08 Lakh closes the FN-05 offset (tax 291 + 41.08 = 332.08 vs capex residual 328.24 + provisions 3.94 = 332.18 Lakh); other non-current assets 49.76 Cr build every H1 (404.73 / 669.60 Lakh), content ND, missing from Step 7 operating capital."
    - "A5-M3 [A3] Orphan R699, R746: company states the LRRs cover the Quarter/Half year and the financial statements (ft l43-l45, l295-l298); FN-10, flag 4 and Q12 cite only the auditor's quarter wording (ft l311, l559)."
    - "A5-M4 [A2] Missing from ledger: consolidated LRR para 2 (ft l568-l574); auditor_paras count test counted A1 rows, not fulltext paragraphs (lg l17); fresh count 9 paragraphs, 8 with rows."
    - "A5-M5 [A2] Missing from ledger: Statement C 1A and 2A 'Total amount outstanding as on date' (ft l278, l282), value blank; treat as M1; flag garbled cell ft l281."
    - "A5-M6 [A4] Cash flag attribution (rv l266, l321-l322, l547): YoY CFO jump is OCFL +39.12 Cr and payables +14.17 Cr, not OCA (+0.93 Cr); add the split and the 1.06x ex-payables reading."
    - "A5-M7 [A4] Gross-margin volatility (rv l569, l594, l205): add derived Q1 FY26 gross margin 25.99% and the 5.07 pp swing; add gross margin to the 8C read-with list."
    - "A5-M8 [A4] Treasury recognised yield (rv l433, l597-l598): add 3.34% pre-tax on the 951.01 Cr average book (5.17% on investments alone); OI all cash items, no fair-value gain."
  contradiction: []
  style:
    - "A5-S1 Five cells rounded from rounded intermediates (rv l185 27.27% vs 27.275%; l195 1.70 vs 1.706 pp; l271 2.24 vs 2.235 days; l273 7.92 vs 7.912 days; l285 582.56/661.69 vs 582.55/661.68)."
    - "A5-S2 rv l214 'highest quarter on record': Q3/Q4 FY26 not separable; say 'highest of the quarters printed individually'."
    - "A5-S3 rv l193, l215 'Q4' / 'year-end' OI concentration: filing supports H2 only; say H2 or tag INFERENCE."
    - "A5-S4 rv l195 'explains the whole margin fall': other expenditure took 171 bps vs a 145 bps fall; say 'more than the whole'."
    - "A5-S5 rv l260, l483 direct tax paid used without row IDs; cite R429/R430 (ft l215)."
    - "A5-S6 rv l618 forward-map catalyst dated 'Now'; give a date or 'date ND'."
    - "A5-S7 rv l522 83.2% promoter-group dividend share mixes RPT values with CF cash paid; caveat that it is not a holding figure (about 83% would exceed the 75% maximum promoter holding, INFERENCE regulatory)."
    - "A5-S8 A1 did not capture RPT text cells 'Approved' / ratification '-' (ft l249-l259); all ten approved, none ratified."
loop_back_to: "A2"
gap: "A2: add MISSING_FROM_STRUCTURED for consolidated LRR para 2 (ft l568-l574) and Statement C 1A/2A (ft l278, l282); re-run auditor_paras count on the fulltext. A3: review orphans R539-R568 (KMP remuneration, CMD lease rentals 148.87 Lakh H1), R279-R282/R417-R418 (NC tax asset closes FN-05; other NC assets 49.76 Cr), R699/R746 (company says review covers half year; weigh in FN-10). A4: fix 'strong on cost [FILED]' (rv l605); graft cash YoY driver split (OCFL +39.12, payables +14.17, OCA +0.93 Cr), Q1 FY26 gross margin 25.99% (5.07 pp swing), treasury yield 3.34-5.17% pre-tax."
style_notes:
  - "A5-S1 round from raw Lakhs (five cells differ by 0.01)"
  - "A5-S2 qualify 'highest quarter on record' (rv l214)"
  - "A5-S3 H2, not Q4, for OI concentration (rv l193, l215)"
  - "A5-S4 'more than the whole' margin fall (rv l195)"
  - "A5-S5 cite R429/R430 for direct tax paid (rv l260, l483)"
  - "A5-S6 date the 'Now' catalyst or mark ND (rv l618)"
  - "A5-S7 caveat the 83.2% dividend share as not a holding figure (rv l522)"
  - "A5-S8 RPT approval-remark cells not extracted (ft l249-l259)"
analyst_note: "Arithmetic is clean. Every derived cell in A4 recomputes from raw Lakhs within 0.01; five were rounded from rounded intermediates (STYLE). Both P&Ls, both balance sheets and both cash flows cast. The failures are coverage and bull-bear balance. Three material ledger groups never reach the review: RPT rows 1-6 (CMD lease rentals 1.49 Cr and KMP remuneration 2.02 Cr in H1); non-current tax assets and other non-current assets (the tax asset closes the FN-05 offset exactly, 332.08 vs 332.18 Lakh); and the company's statement that the reviews cover the half year (ft l43-l45, l295-l298), which FN-10 must weigh. The cash flag credits the OCA release, but OCA was flat YoY; the YoY jump is a smaller OCFL outflow plus a payables stretch. 'Strong on cost [FILED]' has no filed comparator, and gross margin swung 5.07 pp inside FY26. The treasury book earns a recognised 3.3-5.2% pre-tax. A2 missed three fresh-pass rows. The loop starts at A2 as the earliest failing agent; its fix is small, and the material work sits with A3 and A4."
```

---

## LOOP 1 RE-AUDIT

Agent: A5 adversary | model: claude-opus-5-5 | date: 2026-10-17 | fresh context.
Inputs re-read: the amended A4 review (808 lines; LOOP 1 CHANGE LOG at rv l646-l668), the amended A2 ledger (516 lines; LOOP 1 AMENDMENTS at lg l511-l515), the A1 fulltext (620 lines, read in full), and the A1 structured file (spot check of the 31 IDs that loop 1 newly cites; every one maps to the cell A4 uses). The source PDF, inputs/ and A3 output were not opened.
Anchors: in this section, "rv l###" is the AMENDED review's line number. The run-1 text above uses first-pass numbering.
Scope: re-check run-1 items A5-F1, A5-M1 to A5-M8 and A5-S1 to A5-S8; run audits 0-3 over the passages the change log names; recompute every number added in loop 1 from the fulltext.

### R0. Status of run-1 items

| Item | Type | Status | Evidence (amended review / ledger) |
|---|---|---|---|
| A5-F1 | FACTUAL | CLOSED | rv l718-l719. The [FILED] tag now covers cash only (debt nil, receivables about 2 days). Cost position reads "not known ... no peer comparator" [INFERENCE; FILED]. |
| A5-M1 | MISSING | CLOSED | RPT rows 1-6 carried at rv l20, l75 (0D), l200 (Step 2), l235 (Step 4), l365-l382 (5E, FN-12, FN-13), l496 (Step 7), l564 (Q13), l603 and l607 (M2, M6), l638 (flag 11), l689 and l711 (brief). Every value ties to ft l250-l256 (R3 rows 1-7). |
| A5-M2 | MISSING | CLOSED | R279-R282, R417-R418 and twins cited at rv l20, l278, l288-l289, l308, l341, l360, l491, l565, l637, l639, l708. The FN-05 offset now shows both sides (rv l360). Other non-current assets now sit in Step 7 operating capital (rv l491). Residual wording: A5-S9. |
| A5-M3 | MISSING | CLOSED | R699 and R746 cited at rv l20, l81, l363, l563, l631. Both readings are stated, the auditor's wording governs, and the H1 BS and CF are "claimed by the company, not confirmed by the auditor". Residual wording: A5-S12. |
| A5-M4 | MISSING | CLOSED | Ledger M2 added (lg l269, l346). The auditor_paras note now counts fulltext paragraphs: 9, with 8 rows plus M2 (lg l17, l512). My count: ft l313, l319, l327, l352, l561, l568, l576, l598, l601 = 9. Match. Residual label: A5-S15. |
| A5-M5 | MISSING | CLOSED | Ledger M3 (ft l278) and M4 (ft l282) added; garbled ft l281 noted (lg l270-l272, l330-l331, l513). A4 carries both (rv l19, l76). |
| A5-M6 | MISSING | CLOSED | YoY driver table rv l335-l346; readings table rv l350-l356; 5A re-verdicts rv l264-l276; P4 rv l450; Q6 rv l557; flag 2 rv l629; brief rv l683-l684. All numbers recompute (R3 rows 13-20). One new CONTRADICTION in the summary text under the readings table: A5-C1. |
| A5-M7 | MISSING | CLOSED | Q1 FY26 and H2 FY26 gross margins at rv l166, l190, l210, l214, l222-l223, l252, l411, l482, l493, l542, l635, l680, l706. All recompute (R3 rows 21-25). |
| A5-M8 | MISSING | CLOSED | New 7A table rv l501-l516, carried at rv l490, l554-l555, l615, l634, l687, l710. All recompute (R3 rows 26-30). Residual base wording: A5-S10. |
| A5-S1 | STYLE | APPLIED | rv l190 27.28%; l200 1.71 pp; l279 2.23 days; l281 7.91 days; l295 582.55 / 661.68. One 0.01 residue remains: A5-S14. |
| A5-S2 to A5-S7 | STYLE | APPLIED | S2 rv l219; S3 rv l198, l250; S4 rv l200; S5 rv l267, l360, l559; S6 rv l603, l732; S7 rv l602. |
| A5-S8 | STYLE | LOGGED (A1 note) | This is not an A2 or A4 item. A4 records the approval status at rv l378. The A1 structured rows still lack the "Approved" cells. No loop. |

### R1. Deliverable-completeness audit (hard gate)

| Brief part | Location (amended review) | Status |
|---|---|---|
| 1. Summary narrative | rv l674-l692; 17 content lines (l676-l692), inside the 10-20 line band of the Results protocol | present |
| 2. Sector intelligence | rv l694-l701 | present |
| 3. Business-model intelligence | rv l703-l712 | present |
| 4. Competition intelligence | rv l714-l722 | present |
| 5. Forward map | rv l724-l736. A make-or-break reading with bull and bear forks, then 6 catalysts, each with a bull and a bear fork. Five carry a date; one reads "Date ND" (per A5-S6). | present |

Gate result: PASS.

### R2. Coverage audit (re-run)

I repeated the fresh pass over the A1 fulltext for each category that loop 1 touched. Then I grepped the amended review for every run-1 orphan ID.

| Category | A2 count (amended) | A5 fresh count | Orphan rows | Missing from ledger | Status |
|---|---|---|---|---|---|
| Numbered notes | 10 | 10 | none | none | PASS |
| Line items (P&L 44, BS 59 + M1, CF 70) | 173 + M1 | 173 + blank ft l167 | none. R279-R282, R341-R344, R417-R418, R491-R492 now cited (rv l20, l278, l288-l289, l308, l341) | none | PASS (was FAIL) |
| RPT Annexure 1 rows | 10 + total | 10 + total (ft l250-l260) | none. R539-R568 and R632-R636 now cited (rv l20, l75, l369-l375) | none | PASS (was FAIL) |
| Review-scope statements by the company | 2 | 2 (ft l43-l45, l295-l298) | none. R699, R746 cited (rv l81, l363) | none | PASS (was FAIL) |
| Numbered LRR paragraphs | 9 (8 rows + M2) | 9 | none | none | PASS (was FAIL) |
| Statement C particulars | 5 (R601-R603 + M3, M4) | 5 (ft l278, l279, l282, l283, l285) | none | none | PASS (was FAIL) |
| Agenda, Statements B/D/E, entities, dates, forward, qualifiers, parse fragments | unchanged from run 1 | unchanged | none | none | PASS |
| ID accountability | 757 + M1-M4 | 757 parsed | none | none | PASS |

Coverage result: PASS. No orphan rows remain, and the ledger lacks no unit from the fresh pass. Loop 1 added no new enumeration unit.

### R3. Arithmetic audit (every number added in loop 1, recomputed from raw Lakhs)

| # | Metric (rv location) | A4 value | Recomputed (raw Lakhs) | Source lines | Status |
|---|---|---|---|---|---|
| 1 | KMP remuneration H1 / approved (rv l369-l374) | 2.0190 / 4.0379 Cr, 50% | 90.00 + 66.00 + 18.00 + 15.13 + 12.77 = 201.90; 180.00 + 132.00 + 36.00 + 30.25 + 25.54 = 403.79; 50.00% | ft l250-l254 | PASS |
| 2 | CMD lease H1 / approved (rv l375) | 1.4887 / 2.9774, 50% | 148.87 / 297.74 = 50.00% | ft l255 | PASS |
| 3 | RPT rows 1-6 combined (rv l75) | 3.51 | 350.77 | ft l250-l255 | PASS |
| 4 | KMP share of employee cost; of PAT (rv l380) | 33.9%; 2.6% | 201.90 / 595 = 33.93%; 201.90 / 7,703 = 2.62% | ft l97, l107 | PASS |
| 5 | Rent share of other expenditure; of Op EBITDA (rv l381) | 5.6%; 1.5% | 148.87 / 2,638 = 5.64%; 148.87 / 9,636 = 1.54% | ft l101; derived | PASS |
| 6 | Non-current liabilities; H1 finance cost (rv l381) | 1.18; 0.11 | 118.27; 11 (CF 10.82, equal to interest paid) | ft l160, l99, l197, l230 | PASS |
| 7 | CMD non-dividend receipts; rent share; total with dividend (rv l382) | 2.39; 62%; 15.09 | 238.87; 62.32%; 1,508.79 | ft l250, l255, l256 | PASS |
| 8 | Non-current tax assets (rv l288) | 0.96 / 1.37 / +0.41 | 95.90 / 136.98 / +41.08 | ft l138 | PASS |
| 9 | Other non-current assets, BS (rv l289, l308) | 45.72 / 49.76 / +4.05; 3.9% of assets | 4,571.60 / 4,976.33 / +404.73; 4,976.33 / 1,28,372.86 = 3.88% | ft l139, l445, l149 | PASS |
| 10 | Other non-current assets, CF (rv l278, l341) | -6.70 / -4.05 / +2.65 | -669.60 / -404.73 / +264.87 | ft l208 | PASS |
| 11 | FN-05 tax side (rv l360) | 2.91 + 0.41 = 3.32 | 291 + 41.08 = 332.08 | ft l106, l215, l138 | PASS |
| 12 | FN-05 capex side (rv l360) | 5.34 - 2.06 = 3.28; + 0.04 = 3.32 | 534.49 - 206.25 = 328.24; + 3.94 = 332.18 | ft l220, l131-l134, l100, l166 | PASS at 2 dp Cr. "To the paisa" is 0.10 Lakh off (A5-S9) |
| 13 | FN-05 reading A CFO (rv l266, l354) | 92.25; 1.20x (119.8%) | 9,553.02 - 332.08 + 3.94 = 9,224.88; 1.1976x | ft l217, l107 | PASS |
| 14 | CFO and FCF without the payables stretch (rv l353) | 81.82; 1.06x; 76.48 | 8,182.14; 1.0622x; 7,647.65 | ft l210, l217, l220 | PASS |
| 15 | Reading A without the payables stretch (rv l355) | 78.54; 1.02x; 76.48 | 7,854.00; 1.0196x; 7,647.75 | derived | PASS |
| 16 | FN-14 reading B (rv l356) | 99.58; 1.29x; 90.19 | 9,553.02 + 404.73 = 9,957.75; 1.2927x; 9,018.53 | ft l208, l217, l220 | PASS (cell). See A5-C1 for the text under it |
| 17 | YoY WC swings: OCFL / payables / OCA / inventories / ONCA / ONCL / receivables / OCL / ONCFA (rv l337-l345) | +39.12 / +14.17 / +0.93 / +5.63 / +2.65 / +0.05 / -2.81 / -7.14 / -12.74 | +3,911.57 / +1,417.22 / +92.75 / +562.75 / +264.87 / +5.22 / -281.14 / -714.39 / -1,273.59 | ft l204-l213 | PASS |
| 18 | Total WC change; rounded lines sum (rv l346) | -17.68 / 22.17 / +39.85; 39.86 | -1,768.47 / 2,216.79 / +3,985.26; rounded swings sum to 39.86 | ft l202, l214 | PASS |
| 19 | Other six lines net (rv l348) | -14.36 | -1,436.28 | derived | PASS |
| 20 | Payables rise vs Mar (rv l276) | +123.6% | 2,480.40 / 1,109.52 - 1 = 123.56% | ft l163 | PASS |
| 21 | Q1 FY26 derived: gross rev / net rev / gross profit / GM / CoM ratio / inventory change (rv l210) | 638.01 / 162.86 / 42.33 / 25.99% / 74.36% / (0.58) | 63,801 / 16,286 / 4,233 / 25.992% / 74.364% / -58 | ft l88, l94, l96, l98 | PASS |
| 22 | Q1 FY26 Op EBITDA margin (rv l210) | 18.97% (30.90) | 3,090 / 16,286 = 18.973% | ft l91, l99, l100, l105 | PASS |
| 23 | H2 FY26 GM (rv l214) | 33.61% (135.95 / 404.47; CoM 266.43; inventory change 2.09) | 13,595 / 40,447 = 33.612%; 26,643; 209 | ft l94, l96, l98 | PASS |
| 24 | GM swings and value (rv l223) | 5.07 pp; 7.62 pp; 10.82 Cr; 2.1x | 5.068 pp; 7.620 pp; 21,352 x 5.068% = 1,082.1; 2.11x | derived | PASS |
| 25 | H2 vs H1 FY26 (rv l222) | GM +496 bps; Op margin +391 bps | 33.612 - 28.656 = 495.6 bps; 25.960 - 22.048 = 391.2 bps | derived | PASS |
| 26 | Treasury book Mar / Sep / average (rv l505-l507) | 903.96 / 998.07 / 951.01 | 90,395.62 / 99,806.82 / 95,101.22 | ft l133, l136, l137, l145, l146 | PASS |
| 27 | Yield pre-tax / post-tax / multiple (rv l509-l510) | 3.34% / 2.50% (23.77 Cr) / about 40x | 3,177 / 95,101.22 = 3.341%; 3,177 x (1 - 0.25170) = 2,377.3, 2.500%; 40.0x | ft l91, l105, l106 | PASS |
| 28 | Investments-only yield (rv l511-l512) | 615.02; 5.17% | 61,501.75; 5.166% | ft l136, l91 | PASS |
| 29 | H1 OI composition (rv l513) | 4.87 + 0.38 + 4.44 = 9.69 | 487.12 + 38.16 + 443.71 = 968.99 | ft l199-l201, l225-l227 | PASS |
| 30 | No fair-value gain (rv l514) | investments rose exactly by cash spent | 65,963.74 - 57,039.76 = 8,923.98 = CF purchase 8,923.98 | ft l136, l222 | PASS |
| 31 | Signature lead over board start (rv l83, l562) | 61-62 min | 11:30:00 less 10:28:32 = 61.5 min; less 10:27:50 = 62.2 min | ft l46, l344, l368, l590, l614 | PASS |
| 32 | S1 corrections (rv l190, l200, l279, l281, l282, l295) | 27.28%; 1.71 pp; 2.23 (+1.14); 7.91 (+7.98); CCC 7.58 (-10.01); 582.55 / 661.68 (+79.13) | 27.275%; 1.706 pp; 2.2346 (+1.1428); 7.9125 (+7.9814); CCC 7.5790 (-10.0155); 58,255.34 / 66,168.40 (+7,913.06) | ft l90-l101, l142-l146, l163 | PASS (CCC change is -10.02 from raw, 0.01; A5-S14) |

Result: no mismatch above rounding across 32 recomputations.

### R4. Adversarial read (loop 1 passages)

These are the three most positive claims that loop 1 added or changed. Each one is attacked from the same extract.

**Claim A.** rv l358: "On every reading CFO is at or above PAT; the 1.24x print is the high end." rv l625: "it lowers the printed 1.24x to 1.02x-1.20x on the alternative readings and lifts nothing."

Bear counter. The five readings strip liability timing but keep the 41.06 Cr OCA release, which A4 itself calls a seasonal H1 release (rv l274). With all working capital stripped, CFO is 73.36 Cr (9,553.02 - 2,216.79 = 7,336.23 Lakh), or 0.95x PAT, which is below PAT (ft l202, l214, l217). Stripping only the inflows (OCA and payables) gives 40.76 Cr, or 0.53x. That test keeps every outflow, so it is one-sided and is not the fair test. The symmetric bear reading, 0.95x, is already in A4 as "the structural anchor" (rv l267, l358) and in the forward-map bear fork (rv l734). Survives: already in A4. No graft.

Counter from the bull side (Rule J, identical bar). The table directly above the sentence carries FN-14 reading B at 99.58 Cr, 1.29x (rv l356; 9,957.75 / 7,703 Lakh, ft l107, l208, l217). The change log repeats it (rv l656). So 1.24x is not the high end, and one alternative reading does lift. The text contradicts its own table. Every downstream carrier lists only the bear-side readings: flag 2 (rv l629), P4 (rv l450), Step 7 (rv l492), Step 9 (rv l615) and the A4 analyst_note (rv l805). Reading B is weak on the extract. The capex line already reads "including Capital Advances" (ft l219-l220), so capital advances in the operating line would be a second home for the same item. A4 can keep reading B and state the range as 1.02x-1.29x. Or A4 can rank reading B as weakly evidenced and give that reason. A4 cannot keep the table row and also call 1.24x the high end. Type CONTRADICTION (A5-C1), loop A4.

**Claim B.** The FN-10 severity downgrade: "A truncated quote is the likelier cause" (rv l81); "Severity is lower than the first pass stated" (rv l363, l625).

Bear counter. The quarter-only wording appears four times in two reports: both "Re:" lines (ft l310-l311, l558-l559) and both para 1 quotes (ft l313-l314, l561-l564). The consolidated conclusion also names the "standalone" statement (ft l603). A template carried over from a quarter-only report explains four repeats and the para 5 slip at least as well as a one-off truncation. Under either cause, the wording is a drafting defect and not a stated scope limit. So the downgrade holds, and the caveat stays (rv l81, l363). A4 already carries the review-quality pattern (pre-board signatures, para 5 "standalone", quarter-only titles) as flags 3 and 4 and 0D item (b) (rv l82-l83, l630-l631). Survives: in wording only, because "likelier" is an untagged inference. Type STYLE (A5-S12). No graft.

**Claim C.** FN-12 reading A: "a short-term lease under the Ind AS 116 exemption; accounting correct" (rv l381). Also "Nothing exceeds approval" (rv l382).

Bear counter. The rent is approved as an annual 297.74 Lakh, and exactly half was paid in H1 (ft l255), so the arrangement recurs. Opening and closing balances are 0.00 (ft l255), so no deposit or payable shows. A4 states reading B (a multi-year lease without Ind AS 116) and names the observation that separates the two readings (the FY26 AR Ind AS 116 note, Q13). The bull counter to A4's "no lease liability" also fails on the extract. A right-of-use asset could sit inside PPE, but the financing section shows only interest of 10.82 Lakh and the dividend (ft l230-l231). That interest equals the CF finance cost (ft l197), so there is no lease principal or lease interest outflow. Survives: already in A4 as reading B. No graft. One wording point remains: "resets each year at promoter discretion" leaves out the audit-committee approval of the rent (ft l255 "Approved"). Type STYLE (A5-S13).

**Mandatory acquisition-economics probe (re-run).** The amended review adds no deal. The board outcome still has one agenda item (ft l36-l45), and Statement B is still "Not Applicable" (ft l272). Price / target PAT stays undefined. The run-1 nearest test (treasury recognised yield) is now grafted as 7A, and every 7A cell recomputes (R3 rows 26-30). 7A pairs its bull reading (gains recognised only at year-end or on redemption) with the separating observation, the FY26 AR investments note (rv l516). PASS.

### R5. Findings by type (loop 1)

FACTUAL
- none.

MISSING
- none.

CONTRADICTION
- A5-C1 [loop A4]. rv l358 says "the 1.24x print is the high end". rv l625 says the alternative readings give "1.02x-1.20x" and "lift nothing". Both contradict rv l356 (FN-14 reading B, 99.58 Cr, 1.29x) and the change log at rv l656. Recomputed: 9,553.02 + 404.73 = 9,957.75 Lakh; / 7,703 = 1.293x (ft l107, l208, l217). The fix has two options. (a) State the reading range as 1.02x-1.29x around the 1.24x print in 5D (rv l358), the verdict re-check (rv l625) and flag 2 (rv l629). (b) Rank reading B as weakly evidenced, because the capex line already includes capital advances (ft l219-l220), and say so in the same sentence. No table number changes. No cap or verdict moves.

STYLE (logged, no loop)
- A5-S9. rv l360 and l654 say the offset "closes to the paisa"; rv l559, l637 and the YAML flag at rv l798 say "closes exactly". In raw Lakhs, the tax side is 332.08 and the capex side is 332.18, so they differ by 0.10 Lakh (ft l106, l215, l138, l131-l134, l100, l220, l166). The gap equals the 0.10 Lakh fall in intangible assets (ft l134). Say "closes to within 0.10 Lakh".
- A5-S10. The treasury yield base is named loosely. The 3.34% is on the 951.01 Cr average book, which includes other NC financial assets and cash (rv l505-l509). Four places attach it to the 876.36 Cr base of investments plus investment property: brief part 1 ("that book", rv l687), flag 7 ("the book", rv l634), the Step 9 payload (rv l615) and the YAML flag (rv l795). On that base, the average-balance yield is 3.82% (3,177 / 83,061.37 Lakh; ft l91, l133, l136). Name the 951 Cr base wherever 3.3% appears. No number changes.
- A5-S11. Brief part 3 says other non-current assets "grow each half ... [FILED]" (rv l708). The filing shows only two first-half cash flows (ft l208). H2 FY26 is not visible, because the filing prints no Sep-2025 or Mar-2025 balance sheet. Say "grew in both first halves shown". The WC-drag bullet's "seasonal H1 release / H2 rebuild pattern on the one year visible" (rv l359) has the same gap: the filing does not show the OCA H2 rebuild. Tag it INFERENCE.
- A5-S12. In FN-10, "a truncated quote is the likelier cause" (rv l81) carries no tag. Template carry-over fits the four quarter-only repeats and the para 5 "standalone" slip (ft l310-l314, l558-l564, l603). Tag it INFERENCE and name both causes. The same line cites "consolidated l388" for the quarter/half-year title, but l388 prints "September 30, 2025" (FN-11). Say so.
- A5-S13. FN-12 reading A says the rent "resets each year at promoter discretion" (rv l381). The audit committee approved the rent (ft l255). Say "resets each year, subject to audit-committee approval".
- A5-S14. Two rounding residues remain. The CCC change is -10.01 (rv l282), but raw -10.0155 gives -10.02. rv l75 and l380 say "exactly 50%" on every row, but row 4 is 15.13 / 30.25 = 50.02% (ft l253). Both are at the 0.01 level.
- A5-S15. In the ledger count test (lg l17), "grep_count: 16" is the A1 row count (15 rows + M2). The fulltext grep is 9 paragraphs, and it appears only in the parenthesis. Put 9 in the grep field and 16 in a row field. This is A2 wording; no loop.
- A5-S8 (carried). The A1 structured rows lack the RPT "Approved" and ratification cells (ft l249-l259). This is an A1 extraction note; no loop.

### R6. Verdict (loop 1 re-audit)

**INCOMPLETE.** Loop back to **A4** only. Gap: A5-C1 (CONTRADICTION).
- The fix is text in two passages: the 5D reconciliation paragraph (rv l358) and the verdict loop 1 re-check (rv l625). Flag 2 (rv l629) also changes if reading B stays. No A2 or A3 re-run is needed.
- All nine run-1 loop items are CLOSED. Coverage passes, arithmetic passes (32 recomputations), and the deliverable gate passes.
- The fix does not challenge the protocol verdict PROCEED WITH FLAGS or the cash class INDETERMINATE-WITH-DIRECTION. It moves no number and lifts no cap.
- The A5 re-check after the fix covers only rv l356-l358, rv l625 and rv l629.

```yaml
stage: A5-adversary
company: "GMBREW"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
verdict: INCOMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
  forward_map: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters:
  - claim: "FN-10 severity lowered because 'a truncated quote is the likelier cause' (rv l81, l363)"
    counter: "Quarter-only wording repeats four times across both LRRs (ft l310-l311, l313-l314, l558-l559, l561-l564) and the consolidated conclusion names the 'standalone' statement (ft l603); template carry-over fits as well. The downgrade and the caveat hold under either cause; only the untagged 'likelier' fails."
    source_line: "ft l310-l314, l558-l564, l603"
    type: STYLE
findings_by_type:
  factual: []
  missing: []
  contradiction:
    - "A5-C1 [A4] rv l358 'the 1.24x print is the high end' and rv l625 '1.02x-1.20x on the alternative readings and lifts nothing' contradict rv l356 FN-14 reading B 99.58 Cr = 1.29x (9,553.02 + 404.73 = 9,957.75 / 7,703 Lakh; ft l107, l208, l217) and change log rv l656. Fix: state the range 1.02x-1.29x around the 1.24x print (5D, verdict re-check, flag 2), or rank reading B weak with its reason (capex line already includes capital advances, ft l219-l220). No table number changes."
  style:
    - "A5-S9 rv l360, l654 'to the paisa'; rv l559, l637, l798 'exactly': raw 332.08 vs 332.18 Lakh, 0.10 Lakh apart (= intangible decline, ft l134); say 'within 0.10 Lakh'."
    - "A5-S10 3.34% yield is on the 951.01 Cr book (rv l505-l509) but rv l615, l634, l687, l795 attach it to the 876.36 Cr investments + property base, where the average-balance yield is 3.82% (3,177 / 83,061.37 Lakh); name the 951 Cr base."
    - "A5-S11 rv l708 'grow each half [FILED]': filing shows two H1 flows only (ft l208); say 'both first halves shown'. rv l359 OCA 'H2 rebuild' is not visible in the filing; tag INFERENCE."
    - "A5-S12 rv l81 'truncated quote is the likelier cause' untagged; template carry-over fits (ft l310-l314, l558-l564, l603); tag INFERENCE, name both. rv l81 cites consolidated l388 as a 2026 title; l388 prints 2025 (FN-11)."
    - "A5-S13 rv l381 'resets each year at promoter discretion': rent is audit-committee approved (ft l255); say 'subject to audit-committee approval'."
    - "A5-S14 rv l282 CCC change -10.01 vs raw -10.0155 (-10.02); rv l75, l380 'exactly 50%' vs row 4 50.02% (ft l253). 0.01-level residues."
    - "A5-S15 lg l17 grep_count 16 is the A1 row count; the fulltext grep is 9 paragraphs; relabel (A2 wording)."
    - "A5-S8 (carried) A1 structured rows lack RPT 'Approved' / ratification cells (ft l249-l259); A1 note."
loop_back_to: "A4"
gap: "A4 only, A5-C1 (CONTRADICTION): rv l358 calls 1.24x 'the high end' and rv l625 says the alternative readings give 1.02x-1.20x and 'lift nothing', while rv l356 shows FN-14 reading B at 99.58 Cr = 1.29x (9,957.75 / 7,703 Lakh; ft l208, l217). Either state the 1.02x-1.29x range around the 1.24x print in 5D, the verdict re-check and flag 2 (rv l629), or rank reading B weakly evidenced because the CF capex line already includes capital advances (ft l219-l220) and stop calling 1.24x the high end. No table number, cap or verdict changes; no A2/A3 re-run."
style_notes:
  - "A5-S9 'within 0.10 Lakh', not 'to the paisa' / 'exactly' (rv l360, l559, l637, l654, l798)"
  - "A5-S10 name the 951 Cr base for the 3.3% yield (rv l615, l634, l687, l795)"
  - "A5-S11 'both first halves shown' (rv l708); tag OCA H2 rebuild INFERENCE (rv l359)"
  - "A5-S12 tag 'likelier cause' INFERENCE, name template reading; l388 prints 2025 (rv l81)"
  - "A5-S13 rent 'subject to audit-committee approval' (rv l381)"
  - "A5-S14 CCC change -10.02 from raw (rv l282); row 4 50.02% (rv l75, l380)"
  - "A5-S15 ledger auditor_paras grep field should hold 9 (lg l17)"
  - "A5-S8 (carried) RPT approval cells not extracted by A1 (ft l249-l259)"
analyst_note: "All nine run-1 loop items are closed with evidence. Every number added in loop 1 recomputes from raw Lakhs within rounding (32 checks). Coverage now passes: the review cites each run-1 orphan ID, and the ledger carries M2-M4 with a fulltext paragraph count. One new CONTRADICTION fails the audit. The 5D readings table shows FN-14 reading B at 1.29x, but the text below it calls 1.24x the high end, and the verdict re-check says the alternative readings lift nothing. Every carrier (flag 2, P4, Step 7, Step 9, the A4 note) shows only the bear-side readings, which breaks bull-bear symmetry. Reading B is weak on the extract, because the capex line already includes capital advances. So A4 can show the 1.02x-1.29x range or rank reading B weak with that reason. The fix is two sentences plus flag 2. No number, cap or verdict moves, and A2 and A3 do not re-run. Seven new STYLE notes are logged. The main one: the 3.34% yield is on the 951 Cr book, while on investments plus property it is 3.82%, so name the base."
```

---

## LOOP 2 RE-AUDIT

Agent: A5 adversary | model: claude-opus-5-5 | date: 2026-10-17 | fresh context.
Inputs re-read: the loop 2 A4 review (833 lines; LOOP 2 CHANGE LOG at rv l678-l693). The A2 ledger (516 lines, unchanged since loop 1; last amendment block lg l511-l515). The A1 fulltext (620 lines, unchanged; re-read at ft l36-l46, l80-l259, l268-l275, l305-l357, l384-l391, l555-l566, l598-l605, l612-l620). The A1 structured file (spot check of R415-R418, R429, R433, R435, R554-R558; each maps to the cell A4 uses). The source PDF, inputs/ and A3 output were not opened.
Anchors: in this section, "rv l###" is the loop 2 review line number. Earlier sections use earlier numbering.
Scope: close or keep open A5-C1; check A5-S9 to A5-S14; run audits 0-3 over the passages the LOOP 2 CHANGE LOG names; recompute every number that loop 2 changed.

### L0. Status of loop 1 items

| Item | Type | Status | Evidence (loop 2 review) |
|---|---|---|---|
| A5-C1 | CONTRADICTION | CLOSED | rv l358 now says "the readings span 1.02x-1.29x around the 1.24x print". The verdict re-check (rv l631) states the same range and names 1.29x as the high end. Grep: "high end" appears only at rv l454 and l631, both for 1.29x; "lift(s) nothing" and "1.02x-1.20x" are gone. A4 applied both fix options: the range is stated, and reading B is ranked weak with its reason (ft l219-l220). Every carrier is aligned: 5A rv l265, 5D basis cell rv l356, P4 rv l454, Step 7 rv l496, 8A-W rv l532, Step 9 rv l619, flag 2 rv l635, brief rv l710, YAML flag 2 rv l816, analyst_note rv l831. Every number recomputes (L3 rows 1-4). Rank wording residue: A5-S16. |
| A5-S9 | STYLE | APPLIED | rv l364, l563, l643, l660, l798, l824 say "within 0.10 Lakh". Grep finds no "paisa" and no "closes exactly". rv l364 names the cause, the intangible fall from 4.10 to 4.00 Lakh (ft l134). Recomputed at L3 rows 5-6. |
| A5-S10 | STYLE | APPLIED (two residues) | The 951 Cr book is named with the 3.3% yield at rv l494, l558, l619, l640, l713, l736, l793, l821, l831. 876.36 Cr is named as investments plus investment property at rv l640, l821. Residues: A5-S17 (brief "deposits") and A5-S18 (rv l494 "68.3% of assets are non-operating"). |
| A5-S11 | STYLE | APPLIED | "Both first halves shown" or "both H1s shown" at rv l274, l278, l363, l569, l645, l734, l826. The OCA H2 rebuild is tagged INFERENCE at rv l274 and l363. That is correct: the filing prints only H1 cash flows (ft l191-l192) and no Sep-2025 balance sheet (ft l127-l128). |
| A5-S12 | STYLE | APPLIED | rv l81 tags the cause [INFERENCE] and names both readings: a truncated quote, or a template carried over. rv l81 and l367 now say the consolidated title prints "September 30, 2025"; ft l388 confirms it. The four quarter-only repeats sit at ft l310-l311, l313-l314, l558-l559 and l561-l564. The standalone title is at ft l82. |
| A5-S13 | STYLE | APPLIED | rv l385 and l568 say "subject to audit-committee approval" (ft l255 "Approved"). Grep: "promoter discretion" is gone. |
| A5-S14 | STYLE | APPLIED | CCC change -10.02 (rv l282). Row 4 at 50.02% (rv l75, l376, l384). Recomputed at L3 rows 7-8. |
| A5-S15 | STYLE | NOT APPLIED (logged) | lg l17 still reads "grep_count: 16". Loop 2 did not re-run A2. This is A2 wording only, so no loop. |
| A5-S8 | STYLE | CARRIED (A1 note) | No change. The fulltext carries the "Approved" cells (ft l250-l259); the A1 structured rows do not. |

### L1. Deliverable-completeness audit (hard gate)

| Brief part | Location (loop 2 review) | Status |
|---|---|---|
| 1. Summary narrative | rv l699-l718; 18 content lines (l701-l718), inside the 10-20 line band of the Results protocol. Loop 2 added rv l710 and rewrote rv l713. | present |
| 2. Sector intelligence | rv l720-l727 | present |
| 3. Business-model intelligence | rv l729-l738 | present |
| 4. Competition intelligence | rv l740-l748 | present |
| 5. Forward map | rv l750-l762. A make-or-break reading with bull and bear forks, then 6 catalysts, each with a bull and a bear fork. Five carry a date; one reads "Date ND". | present |

Gate result: PASS.

### L2. Coverage audit (re-check)

Loop 2 changed no ledger row, no structured row and no fulltext line. The ledger still ends with the loop 1 amendment block (lg l511-l515). The fulltext still has 620 lines. Loop 2 cites no new row ID. I grepped the loop 2 review for every run-1 orphan ID, to confirm that the rewrites dropped none.

| Category | A2 count | A5 count | Orphan rows | Missing from ledger | Status |
|---|---|---|---|---|---|
| All enumeration categories (notes, line items, RPT rows, scope statements, LRR paragraphs, Statement C, agenda, entities, dates, forward, qualifiers) | unchanged from loop 1 (lg l7-l19) | unchanged from loop 1 (R2 above) | none | none | PASS |
| Run-1 orphan IDs, still cited after loop 2 | n.a. | R279-R282 (rv l20, l288-l289, l364); R417-R418 (rv l20, l278, l341); R341-R344 (rv l20, l308); R539-R568 and R632-R636 (rv l20, l75, l373-l379); R699, R746 (rv l20, l81, l367) | none | none | PASS |
| ID accountability | 757 + M1-M4 (lg l23, l509) | 757 | none | none | PASS |

Coverage result: PASS.

### L3. Arithmetic audit (every number loop 2 changed or re-labelled, from raw Lakhs)

| # | Metric (rv location) | A4 value | Recomputed (raw Lakhs) | Source lines | Status |
|---|---|---|---|---|---|
| 1 | FN-14 reading B CFO and ratio (rv l356, l358, l631, l635) | 99.58; 1.29x | 9,553.02 + 404.73 = 9,957.75; / 7,703 = 1.2927x | ft l217, l208, l107 | PASS |
| 2 | FN-14 reading B FCF (rv l356) | 90.19 | 9,957.75 - (534.49 + 404.73) = 9,957.75 - 939.22 = 9,018.53 | ft l220, l208 | PASS |
| 3 | Range low end: FN-05 reading A without the payables stretch (rv l355, l358, l631) | 78.54; 1.02x | 9,553.02 - 332.08 + 3.94 - 1,370.88 = 7,854.00; / 7,703 = 1.0196x | ft l106, l138, l166, l210, l215, l217 | PASS |
| 4 | Other readings in the range (rv l265, l496, l635, l816) | 1.06x; 1.20x | 8,182.14 / 7,703 = 1.0622x; 9,224.88 / 7,703 = 1.1976x | ft l210, l217, l107 | PASS |
| 5 | S9 tax side (rv l364) | 2.91 + 0.41 = 3.32; 332.08 | (2,591 - 2,300) + (136.98 - 95.90) = 291 + 41.08 = 332.08 | ft l106, l215, l138 | PASS |
| 6 | S9 capex side and gap (rv l364) | 3.28 + 0.04 = 3.32; 332.18; gap 0.10 = intangible fall | 534.49 - [300 - 168.02 + 74.37 - 0.10] = 534.49 - 206.25 = 328.24; + 3.94 = 332.18; 332.18 - 332.08 = 0.10 = 4.10 - 4.00 | ft l220, l100, l131, l132, l134, l166 | PASS |
| 7 | S14 CCC (rv l282) | 17.59 / 7.58 / -10.02 | Mar: 1.0918 + 24.4151 - 7.9124 = 17.5945 (223.70, 3,423.60 and 1,109.52 x 365, over 74,785 and 51,182). Sep: 2.2346 + 21.2383 - 15.8939 = 7.5790 (505.82 x 365 / 82,620; 3,314.45 and 2,480.40 x 365 / 56,962). Change -10.0154, which rounds to -10.02 | ft l88, l90, l94, l98, l142, l144, l163 | PASS |
| 8 | S14 RPT row 4; KMP total (rv l75, l376, l378, l384) | 50.02%; 50% | 15.13 / 30.25 = 50.017%; 201.90 / 403.79 = 50.001% | ft l253 (R554, R555); ft l250-l254 | PASS |
| 9 | S10 bases (rv l494, l640, l713, l736) | 951.01 average; 3.34%; 876.36 = 68.3% | (90,395.62 + 99,806.82) / 2 = 95,101.22; 3,177 / 95,101.22 = 3.341%; 65,963.74 + 21,671.89 = 87,635.63; / 1,28,372.86 = 68.27% | ft l91, l133, l136, l137, l145, l146, l149 | PASS (loop 2 did not change these numbers) |

Result: no mismatch above rounding across 9 recomputations.

### L4. Adversarial read (loop 2 passages)

These are the three most positive claims in the loop 2 text. Each one is attacked from the same extract. A Rule J counter on the new evidence rank follows them.

**Claim A.** rv l362: "On every reading CFO is at or above PAT." rv l631: "No reading takes CFO below PAT."

Bear counter. Every row in the readings table keeps the 41.06 Cr OCA release (ft l207). A4 itself tags an H2 rebuild as INFERENCE (rv l363). With all working capital stripped, CFO is 73.36 Cr (9,553.02 - 2,216.79 = 7,336.23 Lakh), or 0.95x PAT (ft l202, l214, l217). That is below PAT. A4 carries it in the same paragraph as "the structural anchor" (rv l362), in 5A (rv l267) and in the forward-map bear fork (rv l760). Survives: already in A4. No graft.

**Claim B.** rv l364 and l643: "FCF is 90.19 Cr on either reading." rv l831: "FCF of 90.19 Cr holds on both accounting readings."

Bear counter. On FN-05 reading B the 3.32 Cr is not cash paid. It is a tax claim still owed. So cash FCF is right, but an unpaid 3.32 Cr sits behind it. The payables test also cuts FCF to 76.48 Cr (ft l210, l220). A4 carries both: "current liabilities are understated" (rv l364) and the 76.48 Cr row (rv l353). Survives: already in A4. No graft.

**Claim C.** rv l81: "Under either cause the wording is a drafting defect, not a stated scope limit."

Bear counter. Whatever the cause, a report that names only the quarter gives no auditor assurance on the H1 balance sheet and cash flow (ft l310-l314, l558-l564). A4 says so in the same bullet ("CLAIMED BY THE COMPANY, NOT CONFIRMED BY THE AUDITOR"), at rv l367, in flag 4 (rv l637) and in Q12 (rv l567). "Not a stated scope limit" holds on the paragraphs read. The standalone report (ft l313-l357) and the consolidated paragraphs read (ft l561-l566, l598-l605) state no half-year limitation. Para 3 is the standard SRE 2410 text (ft l327-l338). Survives: already in A4. No graft.

**Rule J counter on the new evidence rank (bull side, identical bar).** Loop 2 added a rank of the readings. rv l358 says each reading takes "the same evidence bar". rv l359 calls FN-05 reading A "supported" by the filed tie, and rv l364 calls it "most evidenced". rv l361 calls FN-14 reading B weak, because the capex line already reads "including Capital Advances" (ft l219-l220). rv l631 and l831 repeat the rank.

Counter. The same label also bears on reading A. Reading A says the 3.28 Cr by which the capex line exceeds BS fixed-asset additions is tax booked in the wrong line. The label gives a filed alternative: the excess is capital advances. Every operating working-capital line in the CF equals its raw BS difference. Two examples: other non-current assets (404.73) = 4,976.33 - 4,571.60 (ft l139, l208), and trade payables 1,370.88 = 2,480.40 - 1,109.52 (ft l163, l210). Suppose about 3.28 Cr of capital advances sit in other non-current assets [INFERENCE: their usual Schedule III home, not stated in the filing]. Then l208 counts them a second time in operating, and the round 23.00 Cr tax line (ft l215) is the offset. That reading ties the same way (332.08 vs 332.18 Lakh). It gives CFO of 9,553.02 - 332.08 + 3.94 + 328.24 = 9,553.12 Lakh, which is 95.53 Cr and 1.24x. Capex stays 5.34 Cr and FCF 90.19 Cr. So the tie proves that a plug sits between the tax line and the capex and ONCA lines. It does not pick reading A over this reading.

One phrase in rv l361 is also loose. It says "no filed line shows" a second home for capital advances in operating. But l208 is a filed operating line, and it carries the full ONCA change. What no line does is label an operating item as capital advances.

Survives: in wording only. The 1.02x-1.29x range, FCF of 90.19 Cr, the cash class, the cap and the verdict hold under either reading. Q8 (rv l563) already asks the separating question: what the 5.34 Cr line holds beyond 2.06 Cr of additions. The loop 1 audit gave an untagged rank between two causes the same treatment (A5-S12). Type STYLE (A5-S16). No graft forced.

**Mandatory acquisition-economics probe (re-run).** Loop 2 adds no deal. The board outcome has one agenda item (ft l36-l45). Statement B reads "Not Applicable" (ft l272). Price / target PAT stays undefined. Loop 2 changed only the base labels in the 7A carriers, and every 7A number is unchanged (L3 row 9). PASS.

### L5. Findings by type (loop 2)

FACTUAL
- none.

MISSING
- none.

CONTRADICTION
- none. A5-C1 is CLOSED.

STYLE (logged, no loop)
- A5-S16. Evidence rank (rv l358-l361, l364, l631, l831). A4 uses the capex label (ft l219-l220) against bull reading B only. The label also gives a filed reason for the 3.28 Cr capex excess that bear reading A calls tax. A capital-advance double count through l208, offset by the round tax line (ft l215), fits the same tie. On that reading CFO is about 95.53 Cr (1.24x). Fix: say the tie fits reading A and this reading, and that Q8 separates them. Drop "most evidenced". In rv l361, write "no filed line labels an operating item as capital advances" in place of "no filed line shows one". Also in rv l361, "(M2)" means monitorable M2. But rv l19 and l80 use M2 for ledger M2, the consolidated LRR para 2. Write "monitorable M2".
- A5-S17. Brief parts 1 and 3 say "With deposits and cash added" (rv l713) and "with deposits and cash" (rv l736). The added items are other non-current financial assets of 119.67 Cr (ft l137; content ND; its change sits in operating cash flow, ft l206), other bank balances of 1.22 Cr (ft l146) and cash of 0.83 Cr (ft l145). The filing supports "deposits" only for the bank balances: the FD redemption of 937.32 Lakh equals their fall from 1,058.95 to 121.63 Lakh (ft l146, l223-l224). Say "with other financial assets (content not disclosed), bank balances and cash".
- A5-S18. rv l494 says "68.3% of assets are non-operating", next to the 951.01 Cr non-operating book. The 68.3% is investments plus investment property only (87,635.63 / 1,28,372.86 Lakh; ft l133, l136, l149). On the 7A book at 30-Sep-2026, the share is 77.7% (99,806.82 / 1,28,372.86). Write "investments plus investment property are 68.3% of assets".
- A5-S15 (carried, A2). lg l17 "grep_count: 16" is the A1 row count. The fulltext grep is 9 paragraphs.
- A5-S8 (carried, A1). The A1 structured rows lack the RPT "Approved" and ratification cells (ft l249-l259).

### L6. Verdict (loop 2 re-audit)

**COMPLETE, with style notes recorded.** No FACTUAL, MISSING or CONTRADICTION finding remains.
- A5-C1 is CLOSED. 5D, the verdict re-check, flag 2 and every carrier state the 1.02x-1.29x range. Reading B is ranked weak with its reason.
- A5-S9 to A5-S14 are applied. S10 leaves two base-label residues (A5-S17, A5-S18).
- Coverage passes. Arithmetic passes (9 recomputations). The deliverable gate passes.
- This audit does not challenge the protocol verdict PROCEED WITH FLAGS or the cash class INDETERMINATE-WITH-DIRECTION.
- Five style notes are logged: A5-S16 to A5-S18 are new, and A5-S15 and A5-S8 are carried. None re-runs an agent.
- The review can proceed to the Notion save through the run's operator-approval gate.

```yaml
stage: A5-adversary
company: "GMBREW"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
verdict: COMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
  forward_map: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters:
  - claim: "Loop 2 evidence rank: FN-05 reading A 'supported' by the filed tie and 'most evidenced'; FN-14 reading B weak because the CF capex line already includes capital advances (rv l358-l361, l364, l631, l831)"
    counter: "Rule J bull counter, identical bar. The same label (ft l219-l220) gives a filed reason for the 3.28 Cr capex excess that reading A calls tax. Every CF working-capital line equals its raw BS difference (ONCA 404.73 Lakh, ft l139, l208). If about 3.28 Cr of capital advances sit in other non-current assets [INFERENCE], l208 counts them twice and the round 23.00 Cr tax line (ft l215) offsets. Same tie (332.08 vs 332.18 Lakh); CFO 9,553.12 Lakh = 95.53 Cr, 1.24x; capex 5.34 Cr; FCF 90.19 Cr. Range, FCF, cash class, cap and verdict hold; Q8 (rv l563) separates the readings."
    source_line: "ft l106, l138, l139, l166, l208, l215, l219-l220"
    type: STYLE
findings_by_type:
  factual: []
  missing: []
  contradiction: []
  style:
    - "A5-S16 rv l358-l361, l364, l631, l831: capex label ft l219-l220 used against bull reading B only; a capital-advance double count via l208, offset by the round tax line (ft l215), fits the same tie at CFO 95.53 Cr (1.24x). Say the tie fits both and Q8 separates them; drop 'most evidenced'; rv l361 'no filed line shows one' -> 'no filed line labels an operating item as capital advances'; '(M2)' -> 'monitorable M2'."
    - "A5-S17 rv l713, l736 'deposits and cash': the added items are other NC financial assets 119.67 Cr (ft l137, content ND, operating CF ft l206), other bank balances 1.22 Cr (ft l146) and cash 0.83 Cr (ft l145); 'deposits' is filed only for the bank balances (ft l223-l224). Say 'other financial assets (content not disclosed), bank balances and cash'."
    - "A5-S18 rv l494 '68.3% of assets are non-operating': 68.3% is investments plus investment property (87,635.63 / 1,28,372.86 Lakh; ft l133, l136, l149); the 7A book is 77.7% of assets at Sep-2026 (99,806.82 / 1,28,372.86). Name the base."
    - "A5-S15 (carried, A2) lg l17 grep_count 16 is the A1 row count; the fulltext grep is 9 paragraphs."
    - "A5-S8 (carried, A1) A1 structured rows lack the RPT 'Approved' / ratification cells (ft l249-l259)."
loop_back_to: ""
gap: ""
style_notes:
  - "A5-S16 rank FN-05 reading A and the capital-advance reading equally on the tie; Q8 separates them (rv l359, l361, l364, l631, l831)"
  - "A5-S17 'other financial assets, bank balances and cash', not 'deposits and cash' (rv l713, l736)"
  - "A5-S18 name the 68.3% base as investments plus investment property (rv l494)"
  - "A5-S15 (carried) ledger auditor_paras grep field should hold 9 (lg l17)"
  - "A5-S8 (carried) RPT approval cells not extracted by A1 (ft l249-l259)"
analyst_note: "A5-C1 is closed. The 5D text, the verdict re-check, flag 2 and every carrier now state the range. It runs 1.02x-1.29x around the 1.24x print. Reading B is ranked weak with its reason. S9 to S14 are applied; S10 leaves two small base-label residues (S17, S18). Every loop 2 number recomputes from raw Lakhs in 9 checks. The CCC change is -10.0154, so -10.02 is right. Loop 2 changed no ledger or fulltext line, and every run-1 orphan ID is still cited. The one adversarial point is a Rule J note on the new evidence rank. The capex label weakens bull reading B. It also gives a filed reason for the capex excess that bear reading A calls tax. A capital-advance double count fits the same tie and leaves CFO near the printed 1.24x. I tag it STYLE, as with the loop 1 'likelier cause' rank (S12). No table number, range, FCF, cash class, cap or verdict moves, and Q8 already asks the separating question. If the operator wants the reading carried as a table row, it is a one-line A4 edit. PROCEED WITH FLAGS and INDETERMINATE-WITH-DIRECTION stand."
```
