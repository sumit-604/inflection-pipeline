# A3 FORENSIC NOTES: SUPREMEPWR results h1fy27 (doctype: results)

Company: Supreme Power Equipment Limited (SUPREMEPWR), NSE SME, half-yearly filer.
Period: H1 FY27 (half year ended 30-Sep-2026). Comparatives in filing: H2 FY26, H1 FY26, FY26 (audited).
Inputs read: A1 structured (R001-R554, all rows), A1 fulltext (lines 1-1193, all), A2 ledger (all sections, M01-M35).
Prior-period extract: NONE (ND). Notion checklist: NONE. PRE-THESIS READ. Every quarter-over-quarter diff below is a baseline, not a diff.
Units: Rs Lakhs unless stated. Line numbers = fulltext lines. Source PDF and inputs/ not opened.
Revision: CORRECTION LOOP 1 (2026-10-17). Added section 6 (ledger review register, all 572 ledger IDs), six targeted reviews (6a), M12-M18 review, tables 3d-3f. Amended A3-04, A3-10, A3-13 (reclassified NEUTRAL-FACT), A3-14, A3-15, A3-16. New: A3-17. IDs A3-01 to A3-16 unchanged.
Revision: CORRECTION LOOP 2 (2026-10-17). Disposed ledger rows M19-M35 (section 6d); register now 589 IDs. Ran test (a) audit-status labels vs review scope and test (b) signing dates vs board date 16-10-2026. New: A3-18 (NEUTRAL-FACT). R512 and R532 moved from 6b to 6d (routed A3-18). No other finding changed; F1-F17 statuses unchanged.

## 0. LEDGER RECONCILIATION
- Structured IDs read: 554 of 554 (R001-R554). A2 ledger references 554, orphans 0.
- MISSING_FROM_STRUCTURED rows verified at their fulltext lines: M01 (line 900), M02 (905), M03 (995), M04 (996), M05 (997), M06 (1000), M07 (1001), M08 (1007-1008, 1014-1015; investing total and closing cash unreadable, not estimated), M09 (1063), M10 (124-131), M11 (476-485; ledger cites 478-482, para runs 476-485), M12 (899), M13 (1060), M14 (982), M15 (379; row carries no value, values drift to line 378), M16 (97-102), M17 (440-447), M18 (40; also 295, 660).
- Loop 2 rows verified: M19 (214), M20 (349, 974), M21 (588), M22 (725), M23 (339), M24 (708), M25 (1192), M26 (283; sits before the [page 6] marker at L284, so it is the page 5 SA balance sheet date, twinned by L964; ledger label "page 6 block" is one page off, no effect), M27 (412; twinned by L1027), M28 (649 "Da      6-10-2026"; same page 11 reads "Date: 16-10-2026" at L1143, so the leading 1 is an OCR drop), M29 (157, 159, 881, 882), M30 (1101), M31 (155, 509, 717), M32 (46, 92, 435, 662, 683, 810), M33 (516), M34 (42, 77, 90, 421, 432, 472, 474, 684, 1034), M35 (401-404).
- Ledger IDs accounted for: 589 of 589 (554 R + 35 M). Section 6 disposes of every one.
- ledger_reconciled_pct: 100.

### 0a. Arithmetic checks that contradict A1 rows (route to A1 for re-read; NOT replacement values)
| A1 row | A1 value | Check | Result |
|---|---|---|---|
| R043 | 11,086.31 | Components (lines 887-893) sum 11,056.61; Total income 12,843.98 less PBT 1,787.67 = 11,056.31 | Does not foot. OCR 5/8 confusion likely. R023 312.82 vs 312.52 would close the 0.30 residual. |
| R065 | 0.30 (charge) | H1FY26 PAT 940.87 = PBT 1,227.24 less 286.66 plus 0.30; H1 + H2 deferred = -0.30 + 117.36 = 117.06 (R066) | Sign is a CREDIT (0.30). |
| R106 | 2,870.29 | SA CF trade payables change 1,606.65 (line 991): 7,560.72 less 1,606.65 = 5,954.07 = 2,879.29 + 3,074.78 | OCR reading 2,879.29 (line 937) ties; text-layer 2,870.29 does not. |
| R130 / R153 / R114 / R136 | 4,821.09; (718.82); totals garbled | Mar-26 SA BS foots only with receivables 4,521.09: assets 24,873.69 vs E&L 24,873.68 (text-layer total tail "873.69", line 942). CF cash generated foots only with receivables change (715.82): 2,110.46 less 2,415.67 = (305.21) vs R165 (305.20). | Two independent ties. Both cells show the scan's 5-read-as-8 defect. See A3-13 (now NEUTRAL-FACT). |
| R147 / R148 | H1FY27 NOT LEGIBLE; FY26 (109.73) | FY26 op profit 2,691.87 + 165.26 + 0 + 128.24 - 20.43 - 1.57 = 2,963.37 exactly (R150) without any partnership deduction. SA investment roll 1,267.73 + 274.59 + 109.73 = 1,652.05 (R123) exactly. Minority 12.19 / 10% x 90% = 109.71. | (109.73) belongs to the H1FY27 column; FY26 cell is blank/dash. |
| R141 | 4.37 | Text layer line 354 reads "537". BS-implied gratuity accrual = change in LT provisions 6.12 + change in ST provisions 344.64 - current tax 345.40 = 5.36. Same method ties exactly on CON: 6.59 + 410.69 - 411.44 = 5.84 = R347. | R141 most likely 5.37 (4/5 confusion). With 5.37, op profit = 2,110.41 vs R149 2,110.46; residual 0.05 unresolved. |
| R169 / R195 | (522.9?); 21.98 | Advance tax model (exact on CON, table 3d) gives SA taxes paid 217.76. Then CFO = (305.20) - 217.76 = (522.96), and the cash bridge (522.96) + (1,111.64) + 682.72 = (951.88) closes at 21.91 = BS R131. With R169 (522.90) the bridge closes at 21.97, near R195 21.98. | Residual 0.06-0.07, immaterial. Most consistent set: CFO (522.96), closing 21.91. Not estimated. |
| R185 | 419.51 | SA BS change in short-term borrowings 1,997.42 - 1,578.90 = 418.52 (both dates foot). | Gap 0.99. R185 line 1011 reads "419 St" (garbled). |
| R189 | 682.72 | Components with R185 = 683.78; with BS change 418.52 = 682.79. Full cash bridge needs 682.72. | R189 corroborated by the bridge. R185 is the suspect cell. |
| R190 | 3,557.49 | FY26 components -128.24 + 2,130.06 + 808.82 + 526.86 = 3,337.50. FY26 bridge: 973.79 - 578.13 = 395.66; 395.66 - 2,773.36 + 5,715.20 = 3,337.50. Text layer line 392 reads "Sas49". | R190 most likely 3,337.49 (3 read as 5, twice). Gap 219.99. |
| R382 | 3.39 | CON FY26 interest income adjustment (33.39) (lines 734, 1159). Investing (5,748.04) + 1.60 + 33.39 = (5,713.05) = R384. | R382 = 33.39; leading 3 lost (text layer "339"). Gap 30.00. |
| R383 | (849.08) | Text layer line 756 reads "(849.05)". Components (867.85) + 18.80 = (849.05). Bridge (573.76) + (849.05) + 473.07 = (949.74) = R397. | 849.05 ties; 849.08 is the OCR 5/8 defect. |
| R289 | 2,50,67,330 | OCR line 1087 reads "2,80,67,330"; text layer line 575 "2,50,67.330". Diluted EPS 5.45 = 1,365.10 lakh / 2,50,67,330 = 5.446; with 2,80,67,330 it would be 4.86. | A1 value correct. A1 did not flag the OCR conflict; note only. |
| R252 | 2,851.06 | Item V and VII (M13) read 2,851.66; PAT 2,851.66 - 666.28 - 117.45 - 0.37 = 2,067.56 = R268. | 2,851.66. A1 already flagged. |
| R262 / R264 | 0.37 or -, column unclear | CON PAT arithmetic: H2FY26 1,564.59 - 329.27 - 117.65 = 1,117.67 vs 1,117.29; FY26 2,067.93 vs 2,067.56; H1FY27 and H1FY26 tie at nil | 0.37 charge in H2FY26 and FY26; nil in H1FY27 and H1FY26. |
| R307 | 227.39 (text layer 221.39) | CON BS 30-Sep-26 E&L foots to 30,574.83 only with 227.39 | 227.39 confirmed. |

## 1. FINDINGS TABLE
| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | R187, R391 (ZERO_STANDING H1FY27); routed: R031-R034, R097-R098, R103-R104, R131-R132, R183 | 1012; 1179 | "Proceeds from issuc of share warrants = - 526.86"; "Moneys raised through share warrants - 526 86" | FORWARD-SIGNAL | No warrant exercise in H1FY27. The uncalled 75% balance is 12,47,000 x Rs 126.75 = Rs 1,580.57 lakh, due within 18 months of 27-Aug-2025 (about 27-Feb-2027). SA cash fell 973.79 to 21.91 (line 955), SA gross debt rose 4,572.70 to 5,502.09, and SA finance costs rose 87.08 to 280.11 YoY (3.2x, line 891). The line fills, or the 526.86 is forfeited, inside the next half. Full conversion adds 4.99% to 2,49,91,135 shares. |
| A3-02 | F2 | R003-R006 vs R197-R200; R241-R244 vs R047-R050; routed: R007-R010, R201-R204, R019-R022, R213-R216, R225-R232 | 883; 1042 | "Revenue From Operations 13,530.91 10,644.60 7,519.44 18,164.04" | AMBIGUOUS | CON minus SA revenue: H1FY26 -546.66, H2FY26 -297.03, FY26 -843.69, H1FY27 +817.12. Sign flip, swing 1,363.78 YoY. EBITDA (ex other income) gap as % of SA PAT: 16.8% / 23.5% / 20.4% / 14.5%; narrowed 8.9 pp half-on-half (>5 pp threshold). Two readings: Danya external sales jumped, or SA-to-Danya intercompany sales fell. Separating observation: Danya standalone revenue and intercompany sales H1FY27 vs H1FY26. |
| A3-03 | F2 | R027-R030 vs R221-R224; R039-R042 vs R233-R236 | 890, 1049; 893, 1052 | "Employee Benefits Expenses 420.19 236.24 218.05 454.29" vs "409.27 279.83 152.01 431.84" | AMBIGUOUS | Consolidated cost is BELOW standalone in two cells: employee H2FY26 -43.59; other expenses H1FY26 -43.41 (237.37 vs 280.78). Line-by-line consolidation cannot reduce a cost line unless an intercompany charge is eliminated or H2 (FY26 less H1) carries a year-end reclass. Implied Danya employee cost fell 66.04 (H1FY26) to 10.92 (H1FY27) while SA employee cost rose 2.7x. Ask: staff or charges moved between Danya and the parent? |
| A3-04 | F4 | R530, R539, R529, R269-R272; routed: R265-R268, R335-R336, R359 | 472-474; 1132; 1164 | "is based solely on such unaudited interim financial results and other unaudited financial information" | AMBIGUOUS | Auditor gives no Rs amount for the unaudited subsidiary. Derived Danya PAT (minority 12.19 / 10%) = 121.9 = 8.85% of CON PAT 1,377.29 (H1FY26 9.9%, H2FY26 12.6%, FY26 11.4%). Below 10% this half, above 10% last half. SA reviewed PAT itself carries the 109.73 Danya share (unaudited). Danya-attributable receivables build is 867.82 of the 1,583.64 consolidated build (864.82 on R153 as extracted). Danya-attributable receivables rose 163.42 to 1,031.24 (6.3x) if Mar-26 SA receivables is 4,521.09 (A3-13). That build rests on unaudited numbers. |
| A3-05 | F6 | R462-R465, R468-R470, R417, R426, R506; routed: R095-R096, R301-R302, R188, R392, R409-R416, R422-R425, R453-R454, R479-R480, R501-R503, R518, R552-R554 | 853-854; 314-315 | "Conversion can occur in one or more tranches within 18 months from the date of allotment" | FORWARD-SIGNAL | Dated catalyst: window closes about 27-Feb-2027 (exact ICDR end date NOT FOUND). Status as at 30-Sep-2026: zero conversions, "the Company has received Rs.5,26,85,750/-" (line 848). Promoter vs non-promoter split of the 12,47,000 NOT FOUND (lines 305-307 name both groups). Feeds FTTCP catalyst timeline and the share-count bridge (2,62,38,135 post full conversion). |
| A3-06 | F6 | R403-R407, R471, R549, R551; routed: R548 | 818-825; 834 | "Original allocation 520.31 6.55 Nil" / "establishment and development of Factory premises, Working Capital Requirements and General Corporate Purposes" | FORWARD-SIGNAL | Received 526.86 is 98.8% utilised (520.31), 6.55 unutilised. One blended object (factory, WC, GCP) with no split, so "no deviation" (line 834) cannot be tested by object. The pending 1,580.57 is earmarked to the same blended object; whether it funds the factory (CWIP 3,190.70) or plugs WC is not knowable from the filing. |
| A3-07 | F7 | R519, R540, R466, R467; routed: R105, R107-R108 | 321-322; 686-688 | "are subjected to confirmation and reconciliation and consequent adjustments,if any, will be accounted for" | AMBIGUOUS | Hedge covers trade payables (SA 7,560.72 = 26.2% of total E&L 28,802.45), loans and advances, other current liabilities. Prior text ND, so newness untestable. Adjustments land in "the year of confirmation", possibly the FY27 audit. Ask what share of balances were confirmed at the FY26 audit and what adjustments were booked. |
| A3-08 | F8 | R261-R264 | 1071; 557-559 | "(3) Tax Adjustments for Earlier Years 0.37 - (0.37" | NEUTRAL-FACT | Non-zero prior-year tax: 0.37 charge in CON H2FY26 and FY26 (PAT arithmetic, section 0a). SA line is dash (M02, line 905), so it sits in Danya. Immaterial; rule-mandated FINDING. |
| A3-09 | F8 | R059-R066, R099-R100, R253-R260 | 903-904; 931 | "(1) Current Tax 345.40 244.09 286 66 53075" / "(2) Deferred Tax 717 117.36 30 117.06" | NEUTRAL-FACT | SA ETR H1FY27 23.64% (422.57 / 1,787.67) vs 25.17% statutory; excluding the 109.73 exempt firm-profit share it is 25.18%, so the gap is the partnership share, not a concession. Deferred tax is a persistent CHARGE (DTL 134.93 to 212.10, +77.17 ties): cash-tax deferral of 432 bps of PBT in H1FY27, 801 bps in H2FY26, from capex timing. CON ETR 26.2% (Danya taxed about 35% as a firm). No DTA/credit step-up risk. |
| A3-10 | F10 | R079-R086, R285-R292, R521, R541; routed: R071-R078, R277-R284, R513 | 910-911; 1087; 325-326 | "Diluted no of Shares (Weighted Average) 2.50,67,330 2,50,67,330 2.49.91,135 2,50.67,430" | AMBIGUOUS | Paid-up capital flat at 2,499.11 (no corporate action). Diluted count is identical (2,50,67,330, +76,195 shares) in H2FY26, FY26 and H1FY27; EPS 4.40 / 8.15 / 5.45 recompute on that count. Note 6 says counts weight by days; warrants were allotted 27-Aug-2025, so the FY26 day-weighted count should sit below H2FY26. [INFERENCE] 76,195 = 12,47,000 x (1 - 126.75 / P) at P about Rs 135.00: a treasury-stock count at one average price held fixed for three periods. Separating observation: actual average share price in each period. R289 confirmed (OCR line 1087 "2,80,67,330" fails EPS). Diluted EPS shows 0.3% dilution against 4.99% on full conversion; forward share count should use 12,47,000. |
| A3-11 | F12 | R015-R018, R209-R212, R520, R542, R119-R122, R035-R038; routed: R327-R330 | 887; 323; 948 | "Purchases of Stock in Trade 12,064.96 10,047 21 7,163 52 17,210.72" / "operates only in one business scgment" | AMBIGUOUS | Single segment, so no segment assets or liabilities to trend. All material cost is labelled stock-in-trade; no "cost of materials consumed" line exists in either P&L, for a company named Power Equipment that is building a factory (CWIP 2,797.98 to 3,190.70, +392.72; IAUD +37.41; D&A 35.08 to 199.30 YoY, 5.7x). SA capex 855.85 ties to fixed-asset movement plus D&A (855.83). Two readings: mislabelled raw material (manufacturer) or a trading-heavy mix. Archetype and Section 1B rung depend on the answer. Capex proxy: CWIP +14.0% in the half. |
| A3-12 | F14 | R539, R529, R530, M11; routed: R455, M17 | 684; 434, 473; 476-477 | "[reviewed by the Statutory Auditors / certified by the management]" | AMBIGUOUS | Template placeholder left unresolved in a filed note. Auditor report says "its subsidiaries" (434) and "these subsidiaries" (473) while note 3 says "its only subsidiary" (673). Consolidated conclusion rests on "the statement provided by the management related to Parent & Subsidiary" (476-477). Read together: Danya was most likely management-certified, not auditor-reviewed. Governance data point; ask directly. |
| A3-13 | F14 | R129-R130, R153-R154, R113-R114, R135-R136; routed: R165, R515 | 954; 988; 942; 994 | "(b) Trade Receivables 5,236.9] 4,821.09" vs "Trade Receivables (718 82)" | NEUTRAL-FACT | RESOLVED BY ARITHMETIC, pending A1 re-read (was AMBIGUOUS). Mar-26 SA receivables reads 4,521.09 and the CF change (715.82): the 5-read-as-8 defect in both cells. Tie 1: Mar-26 SA BS foots at 24,873.69 vs 24,873.68 (was a 300.01 gap). Tie 2: CF cash generated 2,110.46 - 2,415.67 = (305.21) vs R165 (305.20). Reading 2 (reclassification, line 957) is eliminated: a reclass cannot leave a filed BS unbalanced. A4 uses neither value until A1 confirms. If A1 re-reads 4,821.09, revert to AMBIGUOUS. |
| A3-14 | F14 | R147-R148, R171-R172, R177-R178, R141-R142, R163-R164, R123-R124; routed: R149-R150, R348, M14 | 983; 950; 1007; 985; 1003, 1006; 979 | "Share of profit and loss from partnership firm or association of persons or limited (109 73)" | AMBIGUOUS | SA CF presentation shifts between columns. H1FY27 is clean: investment roll 1,267.73 + 274.59 cash (line 1007) + 109.73 share (line 983) = 1,652.05 (line 950) exactly, so the share accrues to the capital account and leaves CFO. FY26 deducts no share, yet FY26 SA PAT carries about 211.50 of Danya profit (minority 23.50 x 9), and the FY26 bridge ties. The offset must sit in another line: most likely the 9.23 investment inflow (implying about 220.73 net cash drawn from Danya in FY26) or a receivable from Danya. Either way FY26 SA CFO 2,773.36 likely carries about 211.50 non-cash firm profit. Separating observation: SA non-current investments at 31-Mar-2025 (NOT FOUND in this filing). Capex line switches (855.85 vs 5,746.46); SA FY26 gratuity dash vs CON 17.53 (line 1157); FY26 op profit ties only with (1.57) profit on sale (M14, line 982). |
| A3-15 | F14 | R043, R023, R065, R106; routed: R153, R169, R185, R190, R195, R252, R382, R383, M08, M15 | 894; 904; 937; 1013; 1011; 1173; 756; 999; 1018 | "Total Expenses (IV) r_AT,086.31" / "NET CASH FLOWS FROM (USED IN) FINANCING ACTIVITIES (CQ) : 682.72 ; _ 3,557.49" | NEUTRAL-FACT | Extraction-integrity items (section 0a). Not company findings. Pattern: 5/8 and 3/5 digit confusion on this scan. Material: R190 (219.99), R153 with R130 (300.00, A3-13), R382 (30.00). Small: R383 (0.03), R185 (0.99), R169/R195 (0.06-0.07). M08 SA investing total is unreadable; components give (1,111.64), a derived check, not a filed value. Loop back to A1 before any A4 margin, ETR or cash-flow arithmetic on SA figures. |
| A3-16 | F15 | R456-R458, R393-R394, R303-R304, R123-R124, R179-R180; routed: R145, R183, R305-R306, R311-R312, R351, R387-R390, R427-R429, R452, R538 | 674-675; 1180; 1007; 950; 1108; 1110, 1114 | "(other partners: Mr. Vee Rajmohan 7.5% and Mr. K.V. Pradecp Kumar 2.5%)" / "Net Additional / (Withdrawn) by Other Partners in Subsidiary Firm (20.00) 14 69" | AMBIGUOUS | Entity diff untestable (no prior list); baseline = Danya Electric Company only, 90%. The MD is a 7.5% partner in the sole subsidiary. Capital roll ties to the rupee (table 3e): parent 1,267.73 + 109.73 + 274.59 = 1,652.05; minority 406.76 + 12.19 - 20.00 = 398.95. The parent left its full profit share in Danya and added 274.59 cash; the minority drew 20.00, which is 7.81 above its 12.19 share. Minority capital share fell 24.3% to 19.5%, still about twice its 10% profit share. CON has no investment line and CON reserves equal SA reserves, so all 1,652.05 eliminates against Danya capital (note 3, lines 677-678). [INFERENCE] Debt moved from Danya to the parent: Danya term debt fell 317.80 to 21.35 (-296.45) while the parent borrowed 510.87 term and injected 274.59. In FY26 Danya had added 272.30 term debt. [INFERENCE] The parent books no interest on capital from Danya: SA interest income 18.80 equals CON 18.80 (lines 981, 1159), and 109.73 is exactly 90% of derived Danya PAT 121.92. Whether the minority partners get interest or remuneration before the split is NOT FOUND. Ask. |
| A3-17 | F12 | R109-R110, R161-R162, R317-R318, R369-R370 | 992; 940; 1119; 1169 | "Adjustments for Increase/ (Decrease) in Other Current Liabilities (400 29) 1,455 $3" | AMBIGUOUS | NEW. Single segment, so the entity's liabilities are the segment's. SA other current liabilities fell 400.29 (21.9%, 1,828.83 to 1,428.54) in H1FY27 after a 1,455.53 build in FY26 that supplied 52.5% of FY26 SA CFO 2,773.36. CON fell 402.63 (1,844.40 to 1,441.77; Danya 2.34). Reading 1: customer advances unwound into revenue faster than new advances came in, so order intake lags execution and FY26 CFO was partly borrowed from later halves. Reading 2: non-trade items paid down or re-presented (factory capital creditors, statutory dues, or current maturities moved into short-term borrowings, which rose 418.52 in the same half). Separating observation: OCL breakup (advances from customers, capital creditors, statutory dues, current maturities) at both dates. |
| A3-18 | F14 | M33, M34; routed (loop 2): R512, R532 | 161; 516; 1041; 90-92; 432-435 | "Unaudited Unaudited Unaudited Audited" (L161, whitespace collapsed) / "for the half year ended September 30, 2026" (L91-92) | NEUTRAL-FACT | NEW (loop 2). Test (a) passes: every column label matches the assurance given. H1FY27 / 30-Sep-2026 is "Unaudited" in all six statements (L161, L214, L349, L516, L588, L725) and both review reports cover only that half (L90-92, L432-435). FY26 / 31-Mar-2026 is "Audited" in all six. No column claims an audit for a reviewed period. Letter (L38-42), SA note 1 (L295-296) and CON note 1 (L661-662) all say limited review. The gap: the H2FY26 column (half ended 31-Mar-2026) is labelled "Unaudited", but no note says it is the balancing figure between audited FY26 and the H1FY26 figures, and neither report carries an Other Matter on the comparatives. H2FY26 is a derived column that no auditor signed off at the half level. The H2FY26 cells in A3-03 (CON employee cost 43.59 below SA), A3-02 and A3-09 (801 bps) rest on it. A4 weights H2FY26-based half-on-half deltas lower; no management question needed. |

## 2. CHECKLIST SCORECARD
| check | status | one-line basis |
|---|---|---|
| F1 | FINDING | 13 ZERO_STANDING rows + M01-M07, M09 explained (table 3a); warrant-proceeds dash carries the forward content (A3-01). |
| F2 | FINDING | PAT gap 0.00 every period (SA books the firm share), but revenue gap flips sign and EBITDA gap narrows 8.9 pp HoH; two cost lines consolidate below standalone (A3-02, A3-03). |
| F3 | PASS | Danya is operating: own revenue, purchases, inventory, receivables, borrowings, tax differ from SA; not a shell; no going-concern language. |
| F4 | FINDING | Unaudited subsidiary, no Rs amount given; derived 8.85% of CON PAT (12.6% prior half); review status unresolved (A3-04). |
| F5 | PASS | No EoM, Other Matter, Going Concern or modified conclusion in either report (lines 124-131, 476-485; M16, M17 standard AS 25 responsibility paras). Prior text ND; current text recorded as baseline. |
| F6 | FINDING | Warrant balance and 18-month window; blended-object utilisation 98.8% (A3-05, A3-06). Register in section 4. |
| F7 | FINDING | "subjected to confirmation and reconciliation" covers payables and advances (A3-07). "may not reconcile" (EPS, line 326) is benign. |
| F8 | FINDING | Prior-year tax 0.37 non-zero (CON); ETR gap explained by exempt firm share; persistent deferred charges (A3-08, A3-09). Gross tax presentation ties exactly (table 3d). |
| F9 | N.A. | Indian GAAP (AS); SME exempt from Ind AS (lines 302-304, 667-671); no OCI statement exists. |
| F10 | FINDING | Share capital flat; diluted count frozen across periods, inconsistent with note 6 day-weighting; implied fixed Rs 135 price (A3-10). |
| F11 | PASS | SA net worth 30-Sep-26 = 2,499.11 + 10,159.80 = 12,658.91 (13,185.77 with 526.86 warrant money); reserves move 1,365.10 = H1 PAT 1,365.09 (no dividend); CON funds identical; minority roll ties; Sep-26 SA BS foots at 28,802.45. No third-party number in context. Mar-26 SA footing resolved in A3-13. |
| F12 | FINDING | Single segment, so entity lines stand in for segment lines: stock-in-trade labelling vs factory build, CWIP accretion as capex proxy (A3-11); other current liabilities fell 21.9% after the FY26 build (A3-17). |
| F13 | PASS | Two items only: results and Reg 32 deviation statement (lines 38-48). Audit Committee reviewed and recommended the same day (M18, lines 40, 295, 660). No AR/AGM, dividend, record date, director, auditor, ESOP or enabling resolution. Meeting 14:30-16:30; signed 16:37:54. Loop 2 test (b): all 14 date lines read 16-10-2026 or 2026.10.16 (L19, 62, 147, 283, 339, 412, 497, 649, 708, 872, 964, 1027, 1143, 1192), equal to the board date (L35, 295, 661). |
| F14 | FINDING | Unresolved bracket and plural-subsidiary drafting; SA CF column and line shifts and FY26 firm-profit treatment; A1 OCR items; H2FY26 balancing column carries no note (A3-12 to A3-15, A3-18). Column audit-status labels match the review scope in all six statements. FRN variants 0136235 / 013623S / 0136238 (lines 138, 491, 861) read as OCR of "S", not counted. |
| F15 | FINDING | Prior list ND, diff untestable; baseline recorded; MD is co-partner in sole subsidiary with capital flows against the parent and debt moved from Danya to the parent (A3-16). |
| F16 | N.A. | Results filing, not a presentation. |
| F17 | N.A. | Results filing, not a concall; no Notion checklist exists. |

## 3. SUPPORTING TABLES

### 3a. F1 ZERO_STANDING explanation
| line item | rows | line | template transaction class anticipated | read |
|---|---|---|---|---|
| Exceptional items SA / CON, all periods | R051-R054, R245-R248 | 897, 1058 | Impairment, write-offs, settlements, restructuring | Notes 8/9 (lines 330, 696) affirm none. Standard AS format line. |
| Extraordinary items SA / CON | M01, M09 | 900, 1063 | AS 5 extraordinary events | Standard line; none. |
| Tax adjustments earlier years SA | M02 | 905 | Prior-year assessment true-ups | SA nil; CON 0.37 in H2FY26/FY26 (A3-08). |
| CF gratuity provision SA FY26 | R142 | 979 | Non-cash gratuity accrual | CON FY26 17.53; SA FY26 likely in "change in provisions" 16.92 (A3-14). |
| CF change in provisions SA H1FY27 | R163 | 993 | Provision movements | ST provisions rise 344.64 equals current tax 345.40 less 0.76 (table 3d): the movement is gross tax provision, handled through the tax lines, so the dash is correct. |
| CF purchase of tangible assets SA FY26 / CWIP line H1FY27 | R172, R177 | 1003, 1006 | Capex | Alternating line use (A3-14). |
| CF sale of fixed assets SA/CON H1FY27; CON profit on sale H1FY27 | R175, R379, R355 | 1005, 1172, 1161 | Asset disposals | None this half; FY26 1.60 proceeds, 1.57 profit (SA FY26 profit (1.57) per M14 arithmetic). |
| CF share warrants SA/CON H1FY27 | R187, R391 | 1012, 1179 | Warrant subscription or exercise money | Anticipates the 75% call by about Feb-2027 (A3-01). |
| CF forex difference CON | R353-R354 | 1160 | Import/export exposure | Nil both periods. Raw-material import exposure, if any, NOT FOUND. |
| CF dividends received, interest paid/received (operating), extraordinary proceeds/payments SA | M03-M07 | 995-1001 | Indirect-method template rows | Interest shown in financing/investing instead. No content. |

### 3b. F2 S-vs-C gaps (CON minus SA, Rs Lakhs)
| line | H1FY26 | H2FY26 | FY26 | H1FY27 |
|---|---|---|---|---|
| Revenue | -546.66 | -297.03 | -843.69 | +817.12 |
| Purchases of stock in trade | -263.45 | -352.19 | -615.62 | +588.77 |
| Change in inventories | -472.94 | -279.81 | -752.75 | -48.03 |
| Other income | -80.40 | -106.99 | -187.39 | -103.74 |
| Employee benefits | +66.04 | -43.59 | +22.45 | +10.92 |
| Other expenses | -43.41 | +109.74 | +66.33 | +55.54 |
| Finance costs | +13.72 | +47.34 | +61.06 | +11.68 |
| D&A | +4.52 | +4.46 | +8.98 | +4.80 |
| PBT | +59.83 | +99.96 | +159.79 | +78.34 |
| PAT to owners | 0.00 | 0.00 | 0.00 | +0.01 |
| EBITDA ex OI gap, % of SA PAT | 16.8% | 23.5% | 20.4% | 14.5% |
| Derived Danya PAT (minority x 10) | 93.9 | 141.1 | 235.0 | 121.9 |
| Derived Danya PAT, % of CON PAT | 9.9% | 12.6% | 11.4% | 8.85% |

Decomposition: JV/associate share = none (no JV or associate). Subsidiary = Danya only. SA carries 90% of Danya profit inside other income (H1FY27 109.73), so PAT ties to the rupee; the eliminations show up in revenue, purchases and two cost lines. The H1FY27 derived Danya PBT is 188.07 (1,866.01 - 1,787.67 + 109.73) with tax 66.15 (35.2%), PAT 121.92; minority 10% = 12.19, which ties. H2FY26 column caveat: derived balancing figures with no half-level assurance (A3-18).

### 3c. Balance-sheet and cash context (for A4; not checklist items)
- SA cash 973.79 to 21.91; SA gross debt 4,572.70 to 5,502.09; SA net debt +1,881.27 (+52%).
- SA CFO (522.90) as extracted, (522.96) on table 3d arithmetic, vs PAT 1,365.09; CON CFO (573.76) vs PAT 1,377.29. Driver: SA inventory +2,487.75 (+54.6%); CON receivables +1,583.64 (+33.8%); other current liabilities -400.29 (A3-17).
- SA income taxes paid 217.76 vs current tax 345.40 in the half.

### 3d. Tax provision and advance tax tie-out (reviews of R111-R112, R133-R134, R167-R168, R319-R320, R339-R340, R371-R372)
| entity | change in ST provisions | current tax | residual | change in OCA (BS) | OCA change in CF | difference | income taxes paid |
|---|---|---|---|---|---|---|---|
| SA | +344.64 | 345.40 | -0.76 | +739.73 | 521.97 | 217.76 | 217.76 |
| CON | +410.69 | 411.44 | -0.75 | +705.81 | 495.81 | 210.00 | 210.00 |
| Danya (CON less SA) | +66.05 | 66.04 | +0.01 | -33.92 | -26.16 | -7.76 | -7.76 (net refund) |
Read: tax is shown gross. Current tax builds ST provisions; advance tax paid sits in other current assets. SA ST provisions 883.25 is 99.2% FY26 plus H1FY27 current tax (530.75 + 345.40 = 876.15). Gratuity tie on CON: LT provisions +6.59 plus residual -0.75 = 5.84 = R347. CON taxes paid sit 7.76 below SA because Danya took a net refund; Danya paid 186.24 in FY26 against current tax 135.53 + 0.37. For A4: net ST provisions against advance tax inside OCA before any working-capital ratio; do not count both.

### 3e. Danya capital roll (review of R123-R124)
| | parent (SA investment, R123-R124) | minority (R303-R304) | total |
|---|---|---|---|
| 31-Mar-26 | 1,267.73 | 406.76 | 1,674.49 |
| share of H1FY27 profit | +109.73 (line 983) | +12.19 (line 1073) | 121.92 |
| cash in / (out) | +274.59 (line 1007) | (20.00) (line 1180) | 254.59 |
| 30-Sep-26 | 1,652.05 (line 950) | 398.95 (line 1108) | 2,051.00 |
| capital share Mar-26 to Sep-26 | 75.7% to 80.5% | 24.3% to 19.5% | |
| profit share | 90% | 10% | |
Danya debt (CON less SA): LT 317.80 to 21.35 (-296.45); ST 106.80 to 221.12 (+114.32); net -182.13. FY26 CF: LT +272.30, ST -88.43.

### 3f. Cash bridges (reviews of R185-R186, R189-R190, R195-R196, R383-R384)
| statement | CFO | investing | financing | net change | opening to closing | result |
|---|---|---|---|---|---|---|
| SA H1FY27 | (522.96) recomputed; R169 (522.90) | (1,111.64) derived from components (M08 unreadable) | 682.72 (R189) | (951.88) | 973.79 to 21.91 | Ties to BS R131. R185 off BS by 0.99. |
| SA FY26 | 2,773.36 | (5,715.20) derived | R190 3,557.49; components 3,337.50 | needs 395.66 | 578.13 to 973.79 | Ties only with 3,337.50. |
| CON H1FY27 | (573.76) | (849.05); R383 (849.08) | 473.07 | (949.74) | 974.55 to 24.81 | Ties with 849.05. |
| CON FY26 | 2,590.47 | (5,713.05) with interest 33.39 | 3,517.23 | 394.65 | 579.90 to 974.55 | Ties; R382 3.39 fails. |

## 4. COMMITMENT REGISTER (F6)
| commitment | implied date | note / line ref | status word |
|---|---|---|---|
| Warrant balance Rs 126.75 x 12,47,000 = Rs 1,580.57 lakh payable on exercise; converts to 12,47,000 equity shares (4.99%) | Within 18 months of 27-Aug-2025, about 27-Feb-2027 | SA note 3 lines 306-319; certificate lines 842-857 | initiated (allotted, 25% paid, zero converted at 30-Sep-2026) |
| Warrant proceeds object: factory premises establishment and development, working capital, GCP; allocation Rs 2,107.43 lakh | Received tranche: as at 30-Sep-2026; balance on exercise | Certificate lines 811-825, 834-836 | underway (520.31 of 526.86 utilised, 6.55 unutilised) |
| Adjustments from confirmation and reconciliation of trade payables, loans and advances, other current liabilities | "the year of confirmation" (undated) | SA note 4 lines 321-322; CON note 5 lines 686-688 | in process (undated) |

## 5. QUESTIONS FLAGGED FOR A4 (from FORWARD-SIGNAL and AMBIGUOUS findings)
A3-01, A3-05, A3-06 (warrant call timing, promoter share of the 12,47,000, use split); A3-02, A3-03 (Danya revenue, intercompany flows, staff transfers); A3-04, A3-12 (was Danya auditor-reviewed or management-certified; Danya revenue and PAT in Rs); A3-07 (balance-confirmation coverage); A3-10 (diluted share method and price used); A3-11 (manufacturing vs trading split; why no materials-consumed line); A3-14 (FY26 SA CF treatment of firm profit; SA investment in Danya at 31-Mar-2025); A3-16 (interest or remuneration to the MD from Danya; why the parent took over Danya's term debt and funded the minority withdrawal); A3-17 (other current liabilities breakup; customer advances trend). A3-13 left the question list: it now goes to A1 as an extraction re-read. A3-18 (NEUTRAL-FACT) needs no question; it is a caveat on every H2FY26 cell A4 uses.

## 6. LEDGER REVIEW REGISTER (correction loops 1 and 2)
Every ledger ID appears below exactly once, written out. Dispositions:
- CITED = in a finding's ledger row ref when first raised (154 IDs before loop 1, plus M33, M34 cited by A3-18 in loop 2 = 156).
- ROUTED A3-xx = attached to an existing or new finding in a correction loop (136 in loop 1, plus R512, R532 to A3-18 in loop 2 = 138).
- REVIEWED, NO FINDING = read at its fulltext line; ties or carries no forensic content (282 in loop 1, less R512 and R532, plus 15 loop 2 M rows = 295).
Total 589 = 554 R + 35 M. Every one was read at its cited line in the A1 extract.

### 6a. Targeted reviews (six row groups named by the orchestrator, plus M12-M18)
| rows | outcome |
|---|---|
| R123, R124 (line 950) | Rise 384.32 = 274.59 cash (R179, line 1007) + 109.73 share (line 983), exact. Confirms the 109.73 sits in H1FY27. Against A3-14: H1FY27 treatment is clean; FY26 is not (A3-14 amended with the 211.50 / 9.23 test and the Mar-25 separating observation). Against A3-16: parent left its full share in Danya and injected cash while the minority drew 20.00; capital share 24.3% to 19.5% vs 10% profit share; debt moved from Danya to the parent; no interest on capital to the parent (A3-16 amended). CON has no investment line and reserves are identical, so the elimination is complete with no goodwill or capital reserve. |
| R317, R318, R319, R320 (lines 1119-1120) | OCL -402.63 ties to CON CF R369 exactly; SA -400.30 vs CF 400.29 (0.01). New finding A3-17 (OCL fall after the FY26 build). ST provisions +410.69 = current tax 411.44 less 0.75; Danya +66.05 = Danya current tax 66.04 (table 3d). R319-R320 reviewed, no finding; R317-R318 routed A3-17. |
| R383, R384 (lines 1174, 756) | R383 (849.08) fails; text layer (849.05) ties components and the CON cash bridge. R384 (5,713.05) ties only if R382 is 33.39, not 3.39. R383 and R382 routed A3-15; R384 reviewed, no finding. |
| R185, R186, R189, R190 (lines 1011, 1013) | R185 419.51 is 0.99 above the BS change 418.52. R189 682.72 is corroborated by the full SA cash bridge. R190 3,557.49 fails by 219.99; components and bridge give 3,337.50 (text layer "Sas49"). R186 808.82 ties via the FY26 bridge. R185, R190 routed A3-15; R186, R189 reviewed, no finding. |
| R195, R196 (line 1018) | R195 21.98 vs BS 21.91 and R193 21.91. The advance tax model fixes SA taxes paid at 217.76, so CFO is (522.96) and the bridge closes at 21.91. The 0.07 gap is OCR-grade and immaterial; no company finding. R195 routed A3-15 with R169; R196 973.79 ties to R132 and R191, reviewed, no finding. |
| R289 (line 1087) | A1 value 2,50,67,330 is correct: EPS 5.45 recomputes on it; the OCR reading 2,80,67,330 gives 4.86. Already cited in A3-10 (R285-R292); A3-10 amended with the implied Rs 135.00 fixed price. Note to A1: the row lacks its OCR_UNCERTAIN flag. |
| M12 (899), M13 (1060) | Item VII equals item V in every column (exceptional nil). M13 confirms R252 = 2,851.66. Reviewed, no finding. |
| M14 (982) | Value garbled ("qas7)"); FY26 op-profit arithmetic places (1.57) in FY26 and nil in H1FY27. Not filled. Routed A3-14. |
| M15 (379) | Row has no value; extraordinary items nil (M06, M07), so (A) equals R169. Routed A3-15 with R169. |
| M16 (97-102), M17 (440-447) | Standard AS 25 management-responsibility paragraphs. M17 sits in the report that says "its subsidiaries" (434); routed A3-12. M16 reviewed, no finding. |
| M18 (40; 295, 660) | Audit Committee reviewed and recommended the results on the board date. Composition NOT FOUND in this filing. Reviewed, no finding (F13 basis). |

### 6b. Register: rows NOT cited by a finding before loop 1 (416 IDs after loop 2; R512 and R532 moved to 6d)
| row IDs | ledger item | disposition | basis |
|---|---|---|---|
| R001, R002 | letter date; meeting time | REVIEWED, NO FINDING | F13 basis; 2-hour meeting, signed 16:37:54. |
| R007, R008, R009, R010 | SA other income | ROUTED A3-02 | Table 3b other-income gap; H1FY27 includes 109.73 firm share. R010 233.51 = 96.56 + 136.95. |
| R011, R012, R013, R014 | SA total income | REVIEWED, NO FINDING | Foots within 0.01 each column. |
| R019, R020, R021, R022 | SA changes in inventories | ROUTED A3-02 | Table 3b; (2,487.75) equals BS change and CF R151. |
| R024, R025, R026 | SA other direct expenses H2FY26, H1FY26, FY26 | REVIEWED, NO FINDING | 127.13 + 117.92 = 245.05. |
| R031, R032, R033, R034 | SA finance costs | ROUTED A3-01 | 87.08 to 280.11 YoY (3.2x); 154.50 + 87.08 = 241.58. |
| R044, R045, R046 | SA total expenses H2FY26, H1FY26, FY26 | REVIEWED, NO FINDING | 9,613.96 + 6,935.41 = 16,549.37. |
| R051, R052, R053, R054 | SA exceptional items | REVIEWED, NO FINDING | ZERO_STANDING; table 3a; note 8 line 330. |
| R055, R056, R057, R058 | SA profit before tax | REVIEWED, NO FINDING | Equals R047-R050 and M12. |
| R067, R068, R069, R070 | SA PAT | REVIEWED, NO FINDING | PBT less tax ties (with R065 as credit); equals CON R273-R276. |
| R071, R072, R073, R074, R075, R076, R077, R078 | SA EPS basic and diluted | ROUTED A3-10 | EPS recompute on the frozen diluted count. |
| R087, R088, R089, R090 | SA face value | REVIEWED, NO FINDING | Rs 10 flat. |
| R091, R092 | SA share capital | REVIEWED, NO FINDING | 2,499.11 = 2,49,91,135 x Rs 10; flat. |
| R093, R094 | SA reserves | REVIEWED, NO FINDING | +1,365.10 = PAT 1,365.09 (F11). |
| R095, R096 | SA money against warrants | ROUTED A3-05 | 526.86 both dates; R096 OCR conflict settled by CON R302. |
| R097, R098 | SA long-term borrowings | ROUTED A3-01 | Change 510.87 = CF R183; gross debt build. |
| R101, R102 | SA long-term provisions | REVIEWED, NO FINDING | +6.12 feeds the gratuity tie (0a R141). |
| R103, R104 | SA short-term borrowings | ROUTED A3-01 | Change 418.52; gross debt; tests R185. |
| R105 | SA MSE trade payables Sep-26 | ROUTED A3-07 | Sep-26 BS foots with 3,103.72; payables under confirmation hedge. |
| R107, R108 | SA other trade payables | ROUTED A3-07 | Payables change 1,606.65 = CF R159. |
| R109, R110 | SA other current liabilities | ROUTED A3-17 | 1,828.83 to 1,428.54. |
| R111, R112 | SA short-term provisions | REVIEWED, NO FINDING | Gross tax provision (table 3d). |
| R115, R116, R117, R118 | SA PPE; intangibles | REVIEWED, NO FINDING | Capex 855.85 = fixed-asset movement 656.53 + D&A 199.30 (855.83). |
| R125, R126 | SA other non-current assets | REVIEWED, NO FINDING | Change -103.51 = CF R155. |
| R127, R128 | SA inventories | REVIEWED, NO FINDING | Change 2,487.75 = R019, R151. |
| R131, R132 | SA cash | ROUTED A3-01 | 973.79 to 21.91. |
| R133, R134 | SA other current assets | REVIEWED, NO FINDING | Includes advance tax 217.76 (table 3d). |
| R137, R138, R139, R140 | SA CF PBT; depreciation | REVIEWED, NO FINDING | Equal P&L. |
| R143, R144 | SA CF interest expense | REVIEWED, NO FINDING | Equals interest paid R181-R182. |
| R145 | SA CF interest income H1FY27 | ROUTED A3-16 | 18.80 = CON R351: no interest on capital from Danya. |
| R146 | SA CF interest income FY26 | REVIEWED, NO FINDING | Equals R174 20.43. |
| R149, R150 | SA CF operating profit before WC | ROUTED A3-14 | Places 109.73 in H1FY27 and (1.57) in FY26. |
| R151, R152 | SA CF inventories | REVIEWED, NO FINDING | Ties to BS and P&L. |
| R155, R156, R157, R158, R159, R160 | SA CF ONCA, OCA, payables | REVIEWED, NO FINDING | ONCA and payables tie to BS; OCA ties after advance tax (table 3d). |
| R161, R162 | SA CF other current liabilities | ROUTED A3-17 | (400.29) after FY26 +1,455.53. |
| R165 | SA CF cash generated H1FY27 | ROUTED A3-13 | (305.20) ties only with receivables change (715.82). |
| R166, R167, R168 | SA CF cash generated FY26; taxes paid | REVIEWED, NO FINDING | FY26 foots 3,434.55 vs 3,434.54; taxes paid fit table 3d. |
| R169 | SA CF CFO H1FY27 | ROUTED A3-15 | (522.90) vs (522.96) recomputed. |
| R170 | SA CF CFO FY26 | REVIEWED, NO FINDING | 3,434.54 - 661.18 = 2,773.36. |
| R173, R174, R175, R176 | SA CF interest received; sale proceeds | REVIEWED, NO FINDING | Interest equals income adjustment; R175 ZERO_STANDING (3a). |
| R181, R182 | SA CF interest paid | REVIEWED, NO FINDING | Equals interest expense adjustment. |
| R183 | SA CF LT borrowings H1FY27 | ROUTED A3-16 | Parent borrowed 510.87 as Danya repaid 296.45. |
| R184 | SA CF LT borrowings FY26 | REVIEWED, NO FINDING | FY26 bridge ties. |
| R185 | SA CF ST borrowings H1FY27 | ROUTED A3-15 | 0.99 above BS change. |
| R186 | SA CF ST borrowings FY26 | REVIEWED, NO FINDING | FY26 bridge ties. |
| R188 | SA CF warrant proceeds FY26 | ROUTED A3-05 | 526.86 received FY26. |
| R189 | SA CF financing H1FY27 | REVIEWED, NO FINDING | Corroborated by full cash bridge (3f). |
| R190 | SA CF financing FY26 | ROUTED A3-15 | 3,557.49 vs 3,337.50; gap 219.99. |
| R191, R192, R193, R194 | SA CF opening cash; cash per BS | REVIEWED, NO FINDING | R191 = R132; R192 578.13 fits FY26 bridge; R193 21.91 = R131. |
| R195 | SA CF closing cash H1FY27 | ROUTED A3-15 | 21.98 vs 21.91 (0.07). |
| R196 | SA CF closing cash FY26 | REVIEWED, NO FINDING | 973.79 = R132. |
| R201, R202, R203, R204 | CON other income | ROUTED A3-02 | Table 3b. |
| R205, R206, R207, R208 | CON total income | REVIEWED, NO FINDING | Foots. |
| R213, R214, R215, R216 | CON changes in inventories | ROUTED A3-02 | Table 3b. |
| R217, R218, R219, R220 | CON other direct expenses | REVIEWED, NO FINDING | Danya 8.64-11.06 per half; small. |
| R225, R226, R227, R228, R229, R230, R231, R232 | CON finance costs; D&A | ROUTED A3-02 | Table 3b. |
| R237, R238, R239, R240 | CON total expenses | REVIEWED, NO FINDING | 13,557.36 - 11,691.35 = 1,866.01. |
| R245, R246, R247, R248 | CON exceptional items | REVIEWED, NO FINDING | ZERO_STANDING; note 9 line 696. |
| R249, R250, R251 | CON PBT H1FY27, H2FY26, H1FY26 | REVIEWED, NO FINDING | Equal R241-R243. |
| R252 | CON PBT FY26 | ROUTED A3-15 | 2,851.06 OCR; 2,851.66 by PAT arithmetic. |
| R265, R266, R267, R268 | CON PAT | ROUTED A3-04 | Denominator of the unaudited share. |
| R273, R274, R275, R276 | CON PAT to reserves | REVIEWED, NO FINDING | Equal SA PAT (F2 PAT gap 0). |
| R277, R278, R279, R280, R281, R282, R283, R284 | CON EPS | ROUTED A3-10 | Same counts as SA. |
| R293, R294, R295, R296, R297, R298, R299, R300 | CON face value; share capital; reserves | REVIEWED, NO FINDING | Identical to SA; no goodwill or capital reserve. |
| R301, R302 | CON money against warrants | ROUTED A3-05 | 526.86 both dates. |
| R305, R306 | CON LT borrowings | ROUTED A3-16 | Danya LT 317.80 to 21.35. |
| R307, R308, R309, R310 | CON DTL; LT provisions | REVIEWED, NO FINDING | R307 227.39 confirmed (0a); LT provisions in gratuity tie. |
| R311, R312 | CON ST borrowings | ROUTED A3-16 | Danya ST 106.80 to 221.12. |
| R313, R314, R315, R316 | CON trade payables | REVIEWED, NO FINDING | Change 2,239.25 = CF R367. |
| R317, R318 | CON other current liabilities | ROUTED A3-17 | -402.63 = CF R369. |
| R319, R320, R321, R322, R323, R324, R325, R326 | CON ST provisions; totals; PPE; intangibles | REVIEWED, NO FINDING | Provisions in table 3d; totals foot (R321 OCR 80,574.82 settled). |
| R327, R328, R329, R330 | CON CWIP; IAUD | ROUTED A3-11 | Equal SA; Danya has no CWIP. |
| R331, R332, R333, R334 | CON ONCA; inventories | REVIEWED, NO FINDING | Inventory change = CF R361. |
| R335, R336 | CON trade receivables | ROUTED A3-04 | Danya-attributable 163.42 to 1,031.24. |
| R337, R338, R339, R340, R341, R342, R343, R344, R345, R346, R347 | CON cash; OCA; totals; CF PBT, D&A, gratuity H1FY27 | REVIEWED, NO FINDING | Cash ties to CF; OCA in table 3d; gratuity 5.84 ties. |
| R348 | CON CF gratuity FY26 | ROUTED A3-14 | 17.53 vs SA FY26 dash. |
| R349, R350 | CON CF interest expense | REVIEWED, NO FINDING | Equals interest paid. |
| R351 | CON CF interest income H1FY27 | ROUTED A3-16 | 18.80 = SA. |
| R352, R353, R354, R355, R356, R357, R358 | CON CF interest income FY26; forex; profit on sale; op profit | REVIEWED, NO FINDING | R352 settles R382; R353-R355 ZERO_STANDING (3a); op profit foots. |
| R359 | CON CF receivables H1FY27 | ROUTED A3-04 | 1,583.64 = BS change. |
| R360, R361, R362, R363, R364, R365, R366, R367, R368 | CON CF WC lines | REVIEWED, NO FINDING | Each ties to BS (OCA after advance tax). |
| R369, R370 | CON CF other current liabilities | ROUTED A3-17 | (402.63) after FY26 +1,456.16. |
| R371, R372, R373, R374, R375, R376, R377, R378, R379, R380, R381 | CON CF taxes; cash generated; CFO; capex; sale; interest H1FY27 | REVIEWED, NO FINDING | CFO foots; taxes in table 3d; R379 ZERO_STANDING. |
| R382, R383 | CON CF interest received FY26; investing H1FY27 | ROUTED A3-15 | 3.39 should tie as 33.39; 849.08 as 849.05. |
| R384, R385, R386 | CON CF investing FY26; interest paid | REVIEWED, NO FINDING | Ties (3f). |
| R387, R388, R389, R390 | CON CF LT and ST borrowings | ROUTED A3-16 | Danya debt movements. |
| R392 | CON CF warrants FY26 | ROUTED A3-05 | 526.86. |
| R395, R396, R397, R398, R399, R400, R401, R402 | CON CF financing; net change; opening and closing | REVIEWED, NO FINDING | Bridges tie; OCR variants settled by BS. |
| R408 | NSE circular number | REVIEWED, NO FINDING | Certificate basis. |
| R409, R410, R411, R412, R413, R414, R415, R416 | certificate warrant terms | ROUTED A3-05 | 12,47,000 x Rs 169; 25% received. |
| R418, R419, R420, R421 | certificate auditor identifiers | REVIEWED, NO FINDING | FRN OCR variant (F14 not counted). |
| R422, R423, R424, R425 | SA note 3 warrant terms | ROUTED A3-05 | Match certificate. |
| R427, R428, R429 | Danya profit shares 90 / 7.5 / 2.5 | ROUTED A3-16 | Profit share vs capital share. |
| R430, R431, R432, R433, R434, R435, R436, R437, R438, R439, R440, R441 | auditor identifiers; SEBI circular; SRE 2410; CIN; PIN | REVIEWED, NO FINDING | Identity data. |
| R442, R443, R444, R445, R446, R447, R448, R449, R450, R451 | entities: NSE, symbol, CS, auditors, ICAI, partner, SEBI, company, MCA | REVIEWED, NO FINDING | No change testable (no prior list). |
| R452 | MD Vee Rajmohan | ROUTED A3-16 | Also the 7.5% Danya partner. |
| R453, R454 | warrant allottee groups | ROUTED A3-05 | Split NOT FOUND. |
| R455 | Danya (AS 21, auditor report) | ROUTED A3-12 | Plural-subsidiary report text. |
| R459, R460, R461 | NSE circular; certificate issuer; addressee | REVIEWED, NO FINDING | Certificate data. |
| R472, R473, R474, R475, R476, R477, R478 | dates: letter, meeting, period, signature, review period, SEBI circular, SA report | REVIEWED, NO FINDING | F13 basis. |
| R479, R480 | EGM date; allotment date | ROUTED A3-05 | 27-Aug-2025 starts the 18 months. |
| R481, R482, R483, R484, R485, R486, R487, R488, R489, R490, R491, R492, R493, R494, R495, R496, R497, R498, R499, R500 | approval, signing, period and certificate dates | REVIEWED, NO FINDING | All 16-10-2026 or period-end; consistent. |
| R501, R502, R503 | certificate receipt, allotment, EGM dates | ROUTED A3-05 | Same timeline. |
| R504, R505 | certificate period; date | REVIEWED, NO FINDING | Consistent. |
| R507, R508, R509, R510, R511 | qualifiers: unaudited, signature, review scope, units | REVIEWED, NO FINDING | Standard. (R512 moved to 6d, routed A3-18.) |
| R513 | EPS weighted-average basis | ROUTED A3-10 | Basis of the frozen-count test. |
| R514 | SA BS units | REVIEWED, NO FINDING | Standard. |
| R515 | SA BS reclassification line | ROUTED A3-13 | Reading 2 eliminated. |
| R516, R517 | SA notes 1, 2 | REVIEWED, NO FINDING | Reg 33; Ind AS exemption (F9). |
| R518 | SA note 3 warrants | ROUTED A3-05 | Warrant note. |
| R522, R523, R524, R525, R526, R527, R528 | SA notes 7, 8; CF notes; CON review scope | REVIEWED, NO FINDING | Standard. |
| R531, R533, R534, R535, R536, R537 | CON units, reclass, notes header, notes 1-2 | REVIEWED, NO FINDING | Standard. (R532 moved to 6d, routed A3-18.) |
| R538 | CON note 3 consolidation basis | ROUTED A3-16 | Elimination against partners' capital. |
| R543, R544, R545, R546, R547 | CON notes 8, 9; CF units and notes | REVIEWED, NO FINDING | Standard. |
| R548 | certificate scope | ROUTED A3-06 | Expenditure up to 30-Sep-2026. |
| R550 | certificate units | REVIEWED, NO FINDING | Standard. |
| R552, R553, R554 | certificate receipt basis; notes 1-2 | ROUTED A3-05 | 25% received; balance on exercise. |
| M01, M02, M03, M04, M05, M06, M07 | missing dash rows | REVIEWED, NO FINDING | ZERO_STANDING; table 3a. |
| M08 | SA CF investing, net change, closing (unreadable) | ROUTED A3-15 | Components give (1,111.64); not a filed value. |
| M09, M10 | CON extraordinary dash; SA conclusion | REVIEWED, NO FINDING | Table 3a; F5 unmodified. |
| M12, M13 | item VII SA and CON | REVIEWED, NO FINDING | Equal item V. |
| M14 | SA CF profit on sale | ROUTED A3-14 | (1.57) in FY26 by arithmetic; not filled. |
| M15 | SA CF operating total (A) | ROUTED A3-15 | Equals R169. |
| M16 | SA management-responsibility para | REVIEWED, NO FINDING | Standard AS 25. |
| M17 | CON management-responsibility para | ROUTED A3-12 | Same report as "its subsidiaries". |
| M18 | Audit Committee | REVIEWED, NO FINDING | F13 basis. |

### 6c. Rows already CITED by a finding before loop 1 (154 IDs)
| finding | row IDs |
|---|---|
| A3-01 | R187, R391 |
| A3-02 | R003, R004, R005, R006, R047, R048, R049, R050, R197, R198, R199, R200, R241, R242, R243, R244 |
| A3-03 | R027, R028, R029, R030, R039, R040, R041, R042, R221, R222, R223, R224, R233, R234, R235, R236 |
| A3-04 | R269, R270, R271, R272 (plus R529, R530, R539 listed under A3-12) |
| A3-05 | R417, R426, R462, R463, R464, R465, R468, R469, R470, R506 |
| A3-06 | R403, R404, R405, R406, R407, R471, R549, R551 |
| A3-07 | R466, R467, R519, R540 |
| A3-08 | R261, R262, R263, R264 |
| A3-09 | R059, R060, R061, R062, R063, R064, R065, R066, R099, R100, R253, R254, R255, R256, R257, R258, R259, R260 |
| A3-10 | R079, R080, R081, R082, R083, R084, R085, R086, R285, R286, R287, R288, R289, R290, R291, R292, R521, R541 |
| A3-11 | R015, R016, R017, R018, R035, R036, R037, R038, R119, R120, R121, R122, R209, R210, R211, R212, R520, R542 |
| A3-12 | R529, R530, R539, M11 |
| A3-13 | R113, R114, R129, R130, R135, R136, R153, R154 |
| A3-14 | R141, R142, R147, R148, R163, R164, R171, R172, R177, R178 |
| A3-15 | R023, R043, R106 (R065 listed under A3-09) |
| A3-16 | R123, R124, R179, R180, R303, R304, R393, R394, R456, R457, R458 |

### 6d. Correction loop 2: M19-M35 and the two re-routed R rows (19 IDs)

Test (a): audit-status label vs assurance actually given.
| statement | header line | label as filed | period covered by LRR? | consistent? |
|---|---|---|---|---|
| SA P&L | L161 (R512) | H1FY27 Unaudited; H2FY26 Unaudited; H1FY26 Unaudited; FY26 Audited | H1FY27 only (L90-92) | Yes. H2FY26 is a balancing column with no note (A3-18). |
| SA BS | L214 (M19) | 30-Sep-26 Unaudited; 31-Mar-26 Audited | 30-Sep-26 | Yes |
| SA CF | L349, L974 (M20) | "(Unaudited) Audited)" | H1FY27 | Yes. Missing open bracket appears in both layers; typo, not counted. |
| CON P&L | L516, L1041 (M33, R532) | same four labels as SA P&L | H1FY27 only (L432-435) | Yes. Same H2FY26 gap (A3-18). |
| CON BS | L588 (M21) | Unaudited; Audited | 30-Sep-26 | Yes |
| CON CF | L725 (M22) | Unaudited; Audited | H1FY27 | Yes |
Letter "Un-Audited Financial Results ... Limited Review Report" (L38-42), SA note 1 "Limited Review" (L295-296) and CON note 1 "limited review of the above results for the half year ended September 30, 2026" (L661-662) agree with both report titles (L77-78, L421-423). No note says "audit" where the report says "review".

Test (b): signing dates vs board meeting 16-10-2026 (L35, L295, L661).
| page | document | date line(s) | reads |
|---|---|---|---|
| 1 | board outcome letter | L19; L62 | 16.10.2026; digital 2026.10.16 16:37:54 (after the 16:30 close, L51) |
| 3 | SA review report | L147 | 16-10-2026 |
| 4 | SA P&L | none in either layer (L149-203, L874-916) | no date or signature block captured; cannot separate an undated page from an OCR miss. Note to A1; no finding. |
| 5 | SA BS | L283 (M26); L964 | 16-10-2026 both |
| 6 | SA notes | L339 (M23) | "+ 16-10-2026" (label OCR-lost) |
| 7 | SA CF | L412 (M27); L1027 | 16-10-2026 both |
| 9 | CON review report | L497 | 16-10-2026 |
| 10 | CON P&L | none in either layer (L501-577, L1028-1093) | as page 4; note to A1; no finding. |
| 11 | CON BS | L649 (M28); L1143 | "6-10-2026" text layer; 16-10-2026 re-OCR. OCR drop. |
| 12 | CON notes | L708 (M24) | 16-10-2026 |
| 13 | CON CF | L1192 (M25); text layer L787 has no date line | 16-10-2026 |
| 15 | utilisation certificate | L872 | 16-10-2026 |
Result: 14 of 14 date lines equal the board date. Reports dated on the approval day is normal for a Reg 33 review. No finding; F13 stays PASS.

Register (loop 2).
| row ID | ledger item | disposition | basis |
|---|---|---|---|
| R512 | SA P&L column status (L161) | ROUTED A3-18 (moved from 6b) | H2FY26 "Unaudited" balancing column, no note. |
| R532 | CON P&L column status (L1041) | ROUTED A3-18 (moved from 6b) | Same. |
| M19 | SA BS status header (L214) | REVIEWED, NO FINDING | Labels match LRR scope (test a). |
| M20 | SA CF status header (L349, L974) | REVIEWED, NO FINDING | Labels match; bracket typo not counted. |
| M21 | CON BS status header (L588) | REVIEWED, NO FINDING | Labels match. |
| M22 | CON CF status header (L725) | REVIEWED, NO FINDING | Labels match. |
| M23 | SA notes signing date (L339) | REVIEWED, NO FINDING | 16-10-2026 (test b). |
| M24 | CON notes signing date (L708) | REVIEWED, NO FINDING | 16-10-2026. |
| M25 | CON CF signing date (L1192) | REVIEWED, NO FINDING | 16-10-2026. |
| M26 | SA BS signing date (L283) | REVIEWED, NO FINDING | 16-10-2026; page 5, not page 6 as the ledger labels it. |
| M27 | SA CF signing date (L412) | REVIEWED, NO FINDING | 16-10-2026; twin L1027. |
| M28 | CON BS signing date (L649) | REVIEWED, NO FINDING | OCR "6-10-2026"; twin L1143 reads 16-10-2026. |
| M29 | SA P&L date headers (L157, 159, 881, 882) | REVIEWED, NO FINDING | "2126" at L882 is OCR; L159 reads "September, 2026". Column order matches CON (L511-515). |
| M30 | CON BS date header (L1101) | REVIEWED, NO FINDING | 30-Sep-2026 vs 31-Mar-2026; matches L587. |
| M31 | statement period titles (L155, 509, 717) | REVIEWED, NO FINDING | All half year ended 30-Sep-2026; "39" at L717 is OCR. |
| M32 | period and circular date mentions (L46, 92, 435, 662, 683, 810) | REVIEWED, NO FINDING | All 30-Sep-2026 period end; NSE circular 05-Sep-2024 matches R408. |
| M33 | CON P&L status header, text layer (L516) | CITED A3-18 | "Unaudited Unaudited Unaudited Audited". |
| M34 | Unaudited prose mentions (L42, 77, 90, 421, 432, 472, 474, 684, 1034) | CITED A3-18 | Review scope = H1FY27 only (L90-92, L432-435); L472-474 and L684 already carry A3-04 and A3-12. |
| M35 | SA CF notes, text layer (L401-404) | REVIEWED, NO FINDING | Restates R525, R526. |

Register count check: 6b lists 416 IDs (136 ROUTED + 280 REVIEWED, NO FINDING); 6c lists 154; 6d lists 19 (2 ROUTED A3-18, 2 CITED A3-18, 15 REVIEWED, NO FINDING). 416 + 154 + 19 = 589 = ledger total (554 R + 35 M). Zero rows unaccounted. By disposition: 156 CITED + 138 ROUTED + 295 REVIEWED, NO FINDING = 589.

```yaml
stage: A3-forensics
company: "SUPREMEPWR"
quarter: "h1fy27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/supremepwr-h1fy27/work/forensics_results_supremepwr_h1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: PASS
  F4: FINDING
  F5: PASS
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: N.A.
  F10: FINDING
  F11: PASS
  F12: FINDING
  F13: PASS
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "1012; 1179", classification: "FORWARD-SIGNAL", implication: "No warrant exercise in H1FY27; 75% balance Rs 1,580.57 lakh due by about 27-Feb-2027 while SA cash is 21.91, gross debt 5,502.09 and finance costs 3.2x YoY; full conversion +4.99% shares."}
  - {id: "A3-02", check: "F2", line: "883; 1042", classification: "AMBIGUOUS", implication: "CON minus SA revenue flips from -546.66 (H1FY26) to +817.12; EBITDA gap narrows 8.9 pp of SA PAT HoH; Danya external growth vs lower intercompany sales unresolved."}
  - {id: "A3-03", check: "F2", line: "890, 1049; 893, 1052", classification: "AMBIGUOUS", implication: "Consolidated employee cost (H2FY26 -43.59) and other expenses (H1FY26 -43.41) sit below standalone; intercompany charges or reclass; Danya staff cost 66.04 to 10.92."}
  - {id: "A3-04", check: "F4", line: "472-474; 1132; 1164", classification: "AMBIGUOUS", implication: "Unaudited subsidiary with no Rs amount stated; derived 8.85% of CON PAT (12.6% prior half); Danya-attributable receivables build 867.82 of 1,583.64 (163.42 to 1,031.24) rests on unaudited numbers."}
  - {id: "A3-05", check: "F6", line: "853-854; 314-315", classification: "FORWARD-SIGNAL", implication: "Dated catalyst: 18-month conversion window closes about 27-Feb-2027; zero conversions at 30-Sep-2026; promoter split NOT FOUND."}
  - {id: "A3-06", check: "F6", line: "818-825; 834", classification: "FORWARD-SIGNAL", implication: "98.8% of the 526.86 tranche used under one blended object (factory, WC, GCP); no-deviation claim untestable by object; 1,580.57 pending for same object."}
  - {id: "A3-07", check: "F7", line: "321-322; 686-688", classification: "AMBIGUOUS", implication: "Balance-confirmation hedge over payables (26.2% of SA E&L) and advances; adjustments deferred to year of confirmation."}
  - {id: "A3-08", check: "F8", line: "1071", classification: "NEUTRAL-FACT", implication: "Prior-year tax 0.37 charge in CON H2FY26/FY26 (Danya); immaterial, rule-mandated."}
  - {id: "A3-09", check: "F8", line: "903-904; 931", classification: "NEUTRAL-FACT", implication: "SA ETR 23.64% equals 25.18% ex exempt firm share 109.73; persistent deferred charges defer cash tax 432 bps of PBT (801 bps H2FY26)."}
  - {id: "A3-10", check: "F10", line: "910-911; 1087; 325-326", classification: "AMBIGUOUS", implication: "Diluted count frozen at 2,50,67,330 across H2FY26, FY26, H1FY27 against note 6 day-weighting; implies one fixed price of about Rs 135 under treasury-stock method; diluted EPS shows 0.3% vs 4.99% full-conversion dilution."}
  - {id: "A3-11", check: "F12", line: "887; 323; 948", classification: "AMBIGUOUS", implication: "All material cost labelled stock-in-trade, no materials-consumed line, while a factory is under construction (CWIP 3,190.70, +392.72); archetype and rung hinge on manufacturing vs trading mix."}
  - {id: "A3-12", check: "F14", line: "684; 434, 473; 476-477", classification: "AMBIGUOUS", implication: "Unresolved bracket on subsidiary review status plus plural-subsidiary template text; Danya most likely management-certified only."}
  - {id: "A3-13", check: "F14", line: "954; 988; 942; 994", classification: "NEUTRAL-FACT", implication: "Resolved by arithmetic pending A1 re-read: Mar-26 SA receivables 4,521.09 and CF change (715.82) balance the BS (0.01) and the CF subtotal (305.21 vs 305.20); reclass reading eliminated; A4 uses neither value until A1 confirms."}
  - {id: "A3-14", check: "F14", line: "983; 950; 1007; 985; 1003, 1006; 979", classification: "AMBIGUOUS", implication: "H1FY27 firm-share treatment ties (1,267.73 + 274.59 + 109.73 = 1,652.05); FY26 SA CF removes none of about 211.50 Danya profit, so FY26 SA CFO 2,773.36 likely carries non-cash firm profit offset in the 9.23 investment line; Mar-25 investment NOT FOUND."}
  - {id: "A3-15", check: "F14", line: "894; 904; 937; 1013; 1011; 1173; 756; 999; 1018", classification: "NEUTRAL-FACT", implication: "A1 extraction items fail arithmetic: R043, R065 sign, R106, R153, R190 (219.99), R382 (30.00), R383, R185, R169/R195, R252; loop back to A1 before margin, ETR or cash-flow work."}
  - {id: "A3-16", check: "F15", line: "674-675; 1180; 1007; 950; 1108; 1110, 1114", classification: "AMBIGUOUS", implication: "MD is 7.5% partner in sole subsidiary; parent left its full share in Danya and injected 274.59 while minority drew 20.00 (capital share 19.5% vs 10% profit share); Danya term debt fell 296.45 as the parent borrowed; no interest on capital to the parent; partner payments to MD NOT FOUND."}
  - {id: "A3-17", check: "F12", line: "992; 940; 1119; 1169", classification: "AMBIGUOUS", implication: "Other current liabilities fell 400.29 (21.9%) after a 1,455.53 FY26 build that supplied 52.5% of FY26 SA CFO; customer-advance unwind (order intake lagging) vs capex-creditor or statutory paydown or re-presentation into short-term borrowings."}
  - {id: "A3-18", check: "F14", line: "161; 516; 1041; 90-92; 432-435", classification: "NEUTRAL-FACT", implication: "Audit-status labels match the review scope in all six statements (H1FY27 Unaudited, FY26 Audited); but the H2FY26 column is an unreviewed balancing figure with no balancing-figure note and no Other Matter on comparatives, so H2FY26 cells used in A3-02, A3-03, A3-09 carry no half-level assurance."}
forward_signals: ["A3-01", "A3-05", "A3-06"]
ambiguous: ["A3-02", "A3-03", "A3-04", "A3-07", "A3-10", "A3-11", "A3-12", "A3-14", "A3-16", "A3-17"]
commitments:
  - {commitment: "Warrant balance Rs 126.75 x 12,47,000 = Rs 1,580.57 lakh payable on exercise; 12,47,000 shares (4.99%)", implied_date: "about 27-Feb-2027 (18 months from 27-Aug-2025)", ref: "SA note 3 lines 306-319; certificate lines 842-857", status_word: "initiated"}
  - {commitment: "Warrant proceeds object factory/WC/GCP, allocation Rs 2,107.43 lakh; 520.31 of 526.86 utilised", implied_date: "30-Sep-2026 for received tranche; balance on exercise", ref: "certificate lines 811-825, 834-836", status_word: "underway"}
  - {commitment: "Adjustments from confirmation/reconciliation of payables, loans and advances, other current liabilities", implied_date: "year of confirmation (undated)", ref: "SA note 4 lines 321-322; CON note 5 lines 686-688", status_word: "in process"}
gate_a3: pass
blank_checks: []
analyst_note: "Pre-thesis read; every diff is a baseline. Register covers all 589 ledger IDs (554 R + 35 M): 156 cited, 138 routed, 295 reviewed with no finding. Three items matter. (1) Funding. SA cash fell from 973.79 to 21.91 and CFO was negative against PAT of 1,365.09. The uncalled warrant balance of Rs 1,580.57 lakh, due about 27-Feb-2027, is the nearest funding source. (2) Danya. The MD holds 7.5% of the sole subsidiary, and its numbers are unaudited. The parent capital roll ties: 274.59 cash plus the 109.73 share. Danya repaid 296.45 of term debt and the minority drew 20.00, so parent borrowing replaced Danya debt. FY26 SA CFO may carry about 211.50 of non-cash firm profit. (3) Liabilities. Other current liabilities fell 400.29 after a 1,455.53 FY26 build. Loop 2: audit-status labels match the review scope in all six statements, and all 14 signing-date lines equal the 16-10-2026 board date. H2FY26 is an unreviewed balancing column with no note (A3-18). Route R153, R190, R382, R383 and R185 to A1; they are not replacement values."
```
