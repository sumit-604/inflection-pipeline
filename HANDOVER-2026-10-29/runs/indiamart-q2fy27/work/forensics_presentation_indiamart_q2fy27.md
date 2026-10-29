# A3 FORENSIC NOTES: INDIAMART Q2 FY27, doctype PRESENTATION (investor deck, 69 pages)

Inputs read: A1 structured extraction (R001-R1620, all 1,620 rows), A1 fulltext (L1-L1687, every line), A2 ledger (1,620 IDs referenced, 0 orphans). Prior quarter: no Q1 FY27 deck fulltext exists. Prior-quarter facts come from Notion memory (notion_snapshot_2026-10-28.md L985-1205, L1296-1400) and are labelled NOTION MEMORY, not filed evidence. Cross-document ties use work/forensics_results_indiamart_q2fy27.md (labelled RESULTS-A3). The source PDF and inputs/ were not opened.

Line numbers are fulltext lines. Table and chart values cite the render-verified transcription lines (TBL/CHART) that A1 appended. "Derived" means computed from printed rounded values; the rounding band is stated where it matters.

## RECONCILIATION NOTE (A2 ledger vs A1 tags)

- Ledger reconciled: 1,620 of 1,620 row IDs read at their cited lines (100%).
- Discrepancy: A2 reports `zero_standing: 0` ("no 0/nil/dash-valued NUMBER row"). A1 tags eight rows `[ZERO_STANDING]`: R480, R481 (Goodwill FY21/FY22 "-", L844) and R617-R622 (Proceeds from issue of shares, 0, FY22 to H1FY27, L895). A3 treated them as ZERO_STANDING rows under F1. No row is orphaned; this is an A2 classification miss, not a coverage gap.
- A2 FOOTNOTE_UNRESOLVED on R1537, R1538, R1598: confirmed and used in F14.

## FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
| --- | --- | --- | --- | --- | --- | --- |
| F1-01 | F1 | R617-R622, R1573 | L895, L882 | "Proceeds from issue of shares(4)\| FY21=1,052 ; FY22=0 ... H1FY27=0"; "exercise of ESOPs & qualified institutions placement" | NEUTRAL-FACT | The line exists for ESOP exercise money and a QIP. It has been zero since the FY21 QIP (1,052). A non-zero print is a capital event. ESOP proceeds round to 0 (RESULTS-A3 F10: 1 mn). Carried from Q1 (NOTION MEMORY, Q1 deck F1-01). |
| F1-02 | F1 | R480, R481, R479, R1563 | L844, L795 | "Goodwill\| Q1FY27=454 ; Q2FY27=454 ; FY21=- ; FY22=-" | NEUTRAL-FACT | Goodwill appears from FY23 (Busy acquisition) and has been 454 every period since. No impairment this quarter. Thesis-broken #9 (impairment >100 Cr) is untouched. "Exceptional Item" sits inside the Others(3) definition (L795); the template anticipates exceptional items but shows no separate line. |
| F2-01 | F2 | R410/R411 vs R812/R813; R335/R336 vs R717/R718; R402/R403 vs R804/R805; R1563 | L809, L1010, L801, L1000, L808, L1009, L795 | "Net Profit\| Q1FY27=172 ; Q2FY27=91"; "Net Profit\| Q1FY27=176 ; Q2FY27=106" | FORWARD-SIGNAL | Consol-minus-SA PAT gap: Q2 FY27 -15 (-14.2% of SA PAT); Q1 FY27 -4 (-2.3%); Q2 FY26 about -1 (-1%, derived from the 10% and 27% YoY prints); FY26 -50 (-9.5%); FY25 -56 (-9.2%); FY24 -28 (-7.7%); FY23 +12. Widened about 12pp QoQ and 13pp YoY (above 5pp). Deck decomposition, Q2: EBITDA +3 (Busy +4, Others -1), other income +1 ((8) vs (9)), "Others" -20 (61 vs 41: D&A, finance, exceptional, tax, associates loss). Q1: EBITDA -3, other income +19, Others -20. The QoQ widening is the loss of a Q1 subsidiary other-income gain (+19 to +1); the steady -20 is mostly associate losses (RESULTS-A3 F2-01: associates 15.3 Cr in Q2). The deck never shows associate loss as its own line. |
| F2-02 | F2 | R1382, R1386, R980, R984, R738, R757, R280, R1005, R1035, R1054, R767, R786 | L1651, L1124, L1002, L1004, L718, L1159, L1162, L1164 | "Manpower Cost\| ... YoY=(1%)"; "Total Expenses\| ... YoY=(5%)"; "Employees (Nos)\| ... YoY=(6%)" | AMBIGUOUS | SA EBITDA rose 41 Cr YoY (115 to 156) on revenue +29 (360 to 389). Costs fell: total expenses -5%, manpower -1%, S&M -3%, customer service +2%, T&C +1%, headcount -6% (6,098 vs about 6,490 derived). Additive bridge of the +41 [partly INFERENCE]: about 16 base-period one-off in Q2 FY26 SA other expenses (RESULTS-A3 F2-02, INFERENCE) + about 6 lower share-based payment (F10-02) + about 19 operating. Margin expansion is cost-led while paying suppliers and active buyers shrink. Question: is the headcount cut in sales and servicing, and does it link to supplier attrition? |
| F6-01 | F6 | R1500, R965, R988, R989, R966 | L1083, L1091, L1125 | "~20% of deferred revenue gets recognized within next 3 months" | AMBIGUOUS | Realised conversion is lower. Q2: 89% of 389 = 346 from opening deferred revenue 1,858 = 18.6%. Q1: 91% of 376 = 342 on 1,832 = 18.7%. The "~20%" rule overstates realised next-quarter recognition by about 1.3-1.4pp (about 25 Cr a quarter on 1,863). Q3 FY27 revenue from the opening book is about 347 at the realised rate, not 373 at 20%. |
| F6-02 | F6 | R1501-R1503, R1148, R1152, R1154, R054, R1188, R1204 | L1188-1190, L1241, L1240, L1309, L1311, L1313 | "Increase New Licenses Sold"; "Accelerate Revenue growth"; "Busy New License Sold quarterly ... Q2FY26=12 ... Q2FY27=11" | FORWARD-SIGNAL | Busy priorities are undated and the quarter runs against two of them. New licences 11K vs 12K YoY; H1 23K vs 24K (Q1 FY26 12K derived from FY26 45K). Licence base +10% YoY. Revenue +27% YoY in Q2 vs about +47% in Q1 (NOTION MEMORY; RESULTS-A3 F12-03 segment: 49% to 30%): growth decelerated, not accelerated. "Invest in Team" is delivered: Busy manpower +31%, total expenses +38%. Q1 concall guidance (NOTION MEMORY FA-03) was licences +15-20% and Busy CAGR 27-30%. |
| F6-03 | F6 | R1493, R192, R203, R247 | L526, L710, L711, L715 | "Keep expanding buyer & supplier network" | CONFIRMATORY-NEGATIVE | The standing outlook line is undated. Delivery is the reverse: active buyers (7%), unique enquiries (14%), paying suppliers (2%) YoY. No new target or date appears in the deck. |
| F6-04 | F6 | R142, R147, R166, R167, R178, R1551, R1554, R1523, R1524 | L615, L663, L665 | "Includes 3.7% for which the share transfer concluded on 7 October 2026." | AMBIGUOUS | Status word "concluded" = completed, after the balance-sheet date. Agillos E-Commerce (Aerchain) goes from about 23.2% to 26.9%; it stays an associate. The deck counts a post-period stake in the as-of-quarter table. The consideration is not given, and it is unclear whether the 43 Cr at cost includes it. Expect a Q3 FY27 strategic-investment outflow of unstated size. |
| F10-01 | F10 | R429-R439, R1564, R1292, R622, R1288 | L811, L796, L1461, L895, L1403 | "EPS(4) (Rs.)\| Q1FY27=29 ; Q2FY27=15 ; YoY=10%"; "6,01,43,148" | NEUTRAL-FACT | One EPS line, no basic vs diluted split; bonus-adjusted. Check: 91 / 6.0143 cr shares = 15.1, ties. EPS YoY 10% = PAT YoY 10%, so the share count is flat YoY. Share count ties to results paid-up (RESULTS-A3 F10: 601). ESOP overhang is not quantified in the deck ("700+ employees covered in ESOP", March 2026). |
| F10-02 | F10 | R766-R768, R785-R787, R1584 | L1005, L1007, L994 | "Adjusted EBITDA\| ... Q2FY27=161 ; YoY=28%"; "EBITDA\| ... Q2FY27=156 ; YoY=36%"; "Excluding employee share-based payment expense" | AMBIGUOUS | Share-based payment (Adjusted EBITDA minus EBITDA): Q2 FY27 5; Q1 7; Q2 FY26 about 11 (derived, band 9-12); FY26 35; FY25 17; FY24 24. The falling charge adds about 6 Cr to SA EBITDA YoY. It reverses when a new grant cycle starts. RESULTS-A3 F2-04: SBP down about a third in H1. Question: grant pipeline and FY27 SBP run-rate. |
| F12-01 | F12 | R053-R061, R1168-R1272, R1161-R1167 | L1309-L1321, L1268, L213-219 | "Total Expenses\| ... YoY=38%"; "Revenue from Operations\| ... YoY=27%"; "EBITDA Margin(%)\| Q1FY27=9% ; Q2FY27=12% ... FY26=17%" | FORWARD-SIGNAL | Busy costs grow faster than revenue. Derived Q2 FY26 Busy EBITDA about 5.2 (band 4.2-6.1) at about 18% margin, so Q2 FY27 EBITDA 4 at 12% is about -20% YoY and about -6pp. Billing: Q2 46, +20% YoY; Q1 59, about +9% YoY (Q1 FY26 54 derived); H1 105 vs 92, about +14%. Billing fell 22% QoQ. Billing minus revenue ties to the deferred-revenue build (Q2 46-37 = 9 = 155-146; Q1 59-36 = 23 = 146-124 less 1). Checklist #7 values: billing +20% (green above 25%, red below 20%) and margin below FY26. A4 rules. |
| F12-02 | F12 | R962-R973, R1339-R1345, R663/R664, R667/R668, R442, R326 | L1091, L1092, L1590, L925, L812, L800 | "Deferred Revenue Standalone quarterly ... Q1FY27=1,858 ; Q2FY27=1,863" | FORWARD-SIGNAL | SA deferred revenue grew 5 Cr QoQ, the smallest of the four sequential builds shown (Q3 FY26 +21, Q4 +178, Q1 FY27 +26, Q2 +5). SA collections 394 vs revenue 389. Consol collections +9% vs revenue +10% in Q2; H1 collections 906 vs 836, +8.4% (Q1 FY26 revenue 372.1 is NOTION MEMORY, so H1 revenue +10.6%). Current portion 61% vs 62% a year ago. Collections lead revenue, so revenue growth drifts toward high single digits (RESULTS-A3 F12-04 reaches the same reading). |
| F12-03 | F12 | R685-R688, R702-R705, R1459, R1579, R150 | L951, L955, L943, L665 | "Revenue - Others(1)\| FY25=2 ; FY26=7 ; Q1FY27=3 ; Q2FY27=3"; "EBITDA - Others(1)\| ... Q1FY27=(6) ; Q2FY27=(1)" | NEUTRAL-FACT | Other subsidiaries plus eliminations earn 3 Cr revenue a quarter. Livekeeping (103 Cr at cost) has no separate numbers in the deck. EBITDA loss narrowed (11) FY26, (6) Q1, (1) Q2. No shell signal at group level (F3). |
| F14-01 | F14 | R1598, R1597 | L1154 | "Refer to Note No. 31 in Standalone Financial Statements for Q2FY27 for details on the basis of classification of function-wise results" | AMBIGUOUS | The filed standalone results carry 6 numbered notes (results ledger L7); no Note 31 and no function-wise note exist in the filing set. The marker "2" is not on the table body (FOOTNOTE_UNRESOLVED). The basis of the functional P&L (customer service, S&M, T&C, G&A) cannot be checked. Question: where is Note 31 published? |
| F14-02 | F14 | R1415, R1537, R1538, R057, R1266, R103, R106, R1438, R1439, R1440-R1454 | L93, L358-359, L211, L1321, L389, L444, L618, L665 | "IndiaMART InterMESH Limited Limited"; "2) Figures as on March 31, 2026"; "Deferred Revenue & Advances" | NEUTRAL-FACT | Drafting slips, each immaterial: doubled "Limited" in the safe harbour; p16 footnote markers 2 and 3 not on the slide body; Busy "Deferred Revenue & Advances" (p9) vs "Deferred Revenue" (p52) for the same 155; a "4.0" rating on p18 vs "4.8 Play Store Rating" on p22; brand names (p30-31) and legal names (p32) are not mapped in text (brand column is images). Cumulative governance data point only. |
| F15-01 | F15 | R1440, R1441, R148-R151, R1498 | L627-631, L545 | "Subsidiaries ... 1 Busy Infotech 2 Livekeeping Technologies"; "Credit Facilitation" | FORWARD-SIGNAL | The deck's subsidiary list has two entities. The results show a third: IndiaMart Finance Limited, incorporated 04-Aug-2026 (RESULTS-A3 F6-01, F15-01). The deck never names it; the nearest text is "Credit Facilitation" as an undated commerce stage. A new lending perimeter is absent from the investor narrative. Its capitalisation is not disclosed (RESULTS-A3 F3-02: about 20 Cr net into subsidiaries, INFERENCE). |
| F15-02 | F15 | R154, R155, R1443, R140 | L665, L605 | "IB MonotaRO \| 118 \| 18.7%" | AMBIGUOUS | MonotaRO ceased to be an associate on 29 May 2026 (RESULTS-A3 F1-02, F15-02). The deck lists it at cost under "Strategic Investments" with no note. The deck has only two relationship labels (Subsidiaries, Strategic Investments). It cannot show an associate to FVTPL change, so relationship changes are invisible in the deck. Second quarter without a disposal or remeasurement line (NOTION MEMORY Q1 question #1). |
| F15-03 | F15 | R148-R176, R885, R886, R892, R1588, R608 | L665, L1046, L1037, L893 | "Strategic Investments(3)\| Q1FY27=1,460 ; Q2FY27=1,556"; "Includes investment in subsidiaries & associates and others." | AMBIGUOUS | The p32 table sums to 1,442 at cost. SA Strategic Investments are 1,556, a gap of 114 (7.3%). The SA book rolls: 1,474 (FY26) + 102 SA deployment - 20 SA FV loss = 1,556 (RESULTS-A3 F1-01, F3-02). Candidate reconciling items: IndiaMart Finance capital; FVTPL marks on sub-20% holdings; investments outside the table; cost vs carrying basis. The deck table does not bridge to its own balance sheet. |
| F16-01 | F16 | R033, R787, R1393, R1387, R1382, R1072, R748 | L183, L1007, L1652, L1651, L1166, L1003 | "36% YoY"; "EBITDA Standalone quarterly margin\| Q2FY26=32%"; "General & Administration\| Q1FY27=(29) ; Q2FY27=(31) ; FY21=(43)" | AMBIGUOUS | The headline SA EBITDA +36% YoY and margin 32% to 40% use a Q2 FY26 base that likely carries a 16 Cr investment impairment in SA other expenses (RESULTS-A3 F2-02, INFERENCE). Like-for-like growth is about 19% and the margin gain about 4pp. The two cost rows with no YoY cell are SA Other Expenses and G&A. Derived G&A Q2 FY26 about 42 (band 38.5-46), so G&A fell about 19-33% YoY, the one functional line that would show the base effect. Consol EBITDA +23% is the cleaner figure (the impairment is eliminated on consolidation). |
| F16-02 | F16 | R335, R336, R717, R718, R594, R643, R1561, R1571 | L801, L1000, L891, L898, L793, L880 | "Other Income(1)\| Q1FY27=107 ; Q2FY27=(8)"; "Change in Fair Value Gain on Treasury Investments\| ... H1FY27=44" | FORWARD-SIGNAL | Other income swung from 107 to (8) consol and 88 to (9) SA. The cash-generation table now shows H1 only. The Q1 deck showed a Q1 column (NOTION MEMORY: Q1 FV change about 96, realised about 16). Q2 alone [derived with NOTION MEMORY]: FV change about 44 - 96 = -52; realised about 60 - 16 = 44; sum about -8, which ties to the printed (8). About half the Q1 MTM gain reversed in Q2. Checklist #9 red wording (sequential drop >50%) values: 107 to (8). RESULTS-A3 F2-03: rolling 4Q 200.6 Cr. PAT stays exposed to bond-yield moves on about 3,234 Cr treasury. |
| F16-03 | F16 | R1394-R1406, R1620, R201-R203, R050, R051 | L1678, L1679, L1680, L1673, L711 | "Unique Business Enquiries quarterly (Millions)\| Q2FY26=31 ; Q3FY26=28 ; Q4FY26=27 ; Q1FY27=26 ; Q2FY27=27"; "Sum of all such unique quarterly & yearly buyers" | AMBIGUOUS | Same test as Q1. Inside this deck the Q2 print is consistent: 31 to 27 = -12.9% vs printed (14%), inside the rounding band (-9.8% to -15.9%). The Q1 FY26 base is not consistent across decks. By the L1673 definition, yearly = sum of quarters. This deck implies Q1 FY26 = 114 - (31+28+27) = 28 (band 26-30). The Q1 deck series showed 31 and its label (-11%) implied about 29 (NOTION MEMORY). With 31, FY26 would be 117, not 114. Either the Q1 deck series or this deck's FY26 or quarter values were restated without a note. |
| F16-04 | F16 | R059-R061, R1211-R1264 | L217-219, L1314-L1320 | "EBITDA ... 4 Cr ... Net Profit ... 3 Cr ... Cash Flow from Operations ... 12 Cr" (no YoY) | AMBIGUOUS | Busy highlight card and p52 table print no YoY for EBITDA, net profit, CFO or deferred revenue (p52). These are the lines that fell or slowed (F12-01: EBITDA about -20% YoY derived). Second consecutive quarter (NOTION MEMORY Q1 deck F16-03). |
| F16-05 | F16 | R041, R045, R051 | L194, L200, L206 | "2% YoY ... 7% YoY" ; "14% YoY" | NEUTRAL-FACT | Highlight boxes print declines with no minus sign in the text layer. A1's render check reads them as "down", so direction is shown graphically only. Second consecutive quarter (NOTION MEMORY Q1 deck F16-01). Text-only readers and screen scrapers see growth. |
| F16-06 | F16 | R044, R191, R190, R192 | L192, L710 | "Active Buyers - Last 12 Months\| Q1FY27=41 ; Q2FY27=40 ; YoY=(7%)" | AMBIGUOUS | The deck prints active buyers in whole millions. 40 Mn sits exactly on the 40M line used by checklist #2, thesis-broken #4 and watch 8B. A printed 40 covers 39.5 to 40.5. The deck cannot resolve "below 40M". Question: unrounded active buyers for Q1 and Q2 FY27. |
| F16-07 | F16 | R1510, R1537, R100, R1526, R1527, R1528, R1606, R1607, R1610 | L358, L354, L1373, L1398, L1414 | "Figures as on March 31, 2026" | NEUTRAL-FACT | Geography split, sales team (~5,400), ESG, CSR and people data are dated 31 March 2026, now two quarters stale (one quarter in Q1, NOTION MEMORY Q1 F16-04). The sales-team count is not updated in a quarter when headcount fell 6% YoY. |
| F17-01 | F17 | R1293, R1611 | L1469, L1473 | "Promoters and Promoter Group" 49%; "The figures are approximations" | AMBIGUOUS | Promoter holding about 49% (approximate) is shown. Pledge status is not stated. Second consecutive deck silent on pledge (NOTION MEMORY Q1 F17-01). Checklist #8 needs pledge 0%. |
| F17-02 | F17 | R1493, R192, R203, R214, R310 | L526, L710-712, L754 | "Active Buyers - Last 12 Months\| ... YoY=(7%)"; "Business Enquiries Delivered\| ... YoY=(12%)" | CONFIRMATORY-NEGATIVE | Demand KPIs deteriorate again: active buyers YoY -3% (Q4 FY26), -5% (Q1), -7% (Q2) (first two NOTION MEMORY); enquiries (14%); enquiries delivered (12%); fourth straight sequential paying-supplier fall. The deck gives no cause, no target and no date. Second consecutive deck with no forward guidance on demand (NOTION MEMORY Q1 F17-04). |
| F17-03 | F17 | R1563, R152, R153 | L795, L665 | "Others include - Depreciation, Amortization, Finance Cost, Exceptional Item, Tax Expense & Associates Loss" | AMBIGUOUS | Monitors #11 (associate cohort P&L) and #12 (Fleetx mark) get no deck disclosure. Associate loss is folded into "Others"; Fleetx shows only 226 at cost and 25.8%. RESULTS-A3 F2-01: associate losses about 15.3 Cr in Q2, +20% QoQ. The deck is silent on the main driver of the S-vs-C gap (F2-01). |

## CHECKLIST SCORECARD

| check | status | basis |
| --- | --- | --- |
| F1 Zero-value standing | FINDING | A1 tags 8 ZERO_STANDING rows that A2 missed. Share-issuance line zero since FY21 (F1-01); goodwill dash pre-FY23 (F1-02). |
| F2 Standalone vs consolidated | FINDING | The deck carries SA and consol P&L. PAT gap -14.2% vs -2.3% QoQ and about -1% YoY: above 5pp (F2-01). SA EBITDA growth is cost-led (F2-02). |
| F3 Shell-entity | PASS | Consol cost lines exceed SA on every line (manpower 171 vs 156, other expenses 98 vs 76, L803/L1002, L804/L1003). No identical lines, so no shell at group level. No going concern or EoM in the deck. Small "Others" entity noted in F12-03. |
| F4 Unaudited contribution | N.A. | No auditor paragraph in a presentation. Cover letter says "Audited" (L24), consistent with the results (RESULTS-A3 F13). |
| F5 Going concern / EoM | N.A. | No EoM or going-concern text in a presentation. |
| F6 Forward-commitment mining | FINDING | Lexicon hits ("will be", "will not be") are safe-harbour boilerplate (L99, L125, L129). Real forward rows R1493-R1503 and the "concluded" status word (L615, L663) yield F6-01 to F6-04. |
| F7 Hedge-phrase mining | PASS | Hedge lexicon hits ("subject to" L115, "No ... assurance" L124) sit only in safe-harbour boilerplate. The seasonality footnotes (L920, L1551, L1613) are standing and were carried from Q1 (NOTION MEMORY Q1 F7-01). No new hedge on revenue lumpiness or concentration. A verbatim diff is not possible (no prior fulltext). |
| F8 Tax forensics | N.A. | The deck folds tax into "Others" (L795, L995). No tax line, so no ETR or deferred-tax pattern. Tax liabilities 100 to 93 (L851) only. |
| F9 OCI forensics | N.A. | No OCI line in the deck. |
| F10 Share count / dilution | FINDING | Single EPS line; share count 6,01,43,148 ties (F10-01). Falling share-based payment lifts EBITDA (F10-02). |
| F11 Reserves / net-worth tie-out | PASS | Capital & Reserves consol 2,316 (L849) and SA 2,477 (L1048) tie to results net worth 2,316.3 and 2,476.9 (RESULTS-A3 F11). Q1 to Q2 roll: consol 2,220 + 91 + about 5 other; SA 2,365 + 106 + about 6 other. The Q1 dividend payable cleared: Other Liabilities 507 to 150 (L853), H1 distributions (361) (L897). SA exceeds consol by 161 (145 in Q1), consistent with investee losses. No gap above 5%. |
| F12 Segment forensics | FINDING | Applied to the legal-entity view (p41) and the Busy pages, the deck's segment-like disclosure. Busy costs outrun revenue (F12-01); deferred-revenue build slows (F12-02); "Others" entity small (F12-03). |
| F13 Board outcome beyond results | N.A. | A presentation carries no board outcome. The independent-director roster (p58, L1419-1444) has no term dates to map. |
| F14 Note drafting inconsistencies | FINDING | Note 31 reference with no matching filed note (F14-01). Cumulative drafting slips (F14-02). |
| F15 Entity list diffs | FINDING | Applied to the p32 investment portfolio table. IndiaMart Finance absent (F15-01); MonotaRO relationship change invisible (F15-02); table does not bridge to the book (F15-03). |
| F16 Dropped / reframed disclosures | FINDING | F16-01 to F16-07. Main items: headline SA EBITDA on a contaminated base; H1-only treasury column; enquiries base irreconcilable across decks; Busy YoY omitted for a second quarter. |
| F17 Silence audit | FINDING | Checklist and commitment cross-check below. Pledge, demand cause and associate cohort silent (F17-01 to F17-03). |

## COMMITMENT REGISTER (F6)

| commitment | implied date | note/turn ref | status word |
| --- | --- | --- | --- |
| About 20% of deferred revenue is recognised within the next 3 months (realised 18.6%, F6-01) | Q3 FY27 | p45 L1083 (R1500) | none (standing guidance) |
| Busy: Increase New Licenses Sold (Q2 new 11K vs 12K YoY) | undated | p49 L1190 (R1503) | none |
| Busy: Accelerate Revenue growth (27% Q2 vs about 47% Q1) | undated | p49 L1189 (R1502) | none |
| Busy: Invest in Team & Awareness (manpower +31%) | undated | p49 L1188 (R1501) | none |
| Core SME: keep expanding buyer and supplier network | undated | p27 L526 (R1493) | none |
| Brands: focus on large and medium enterprises | undated | p27 L532 (R1494) | none |
| Improve engagement: commerce enablement, fintech and accounting, business enablement SaaS | undated | p27 L523-527 (R1495-R1497) | none |
| Commerce stage: credit facilitation, logistics/tracking (IndiaMart Finance incorporated per results, not named in deck) | undated | p28 L545-547 (R1498) | none |
| Aerchain (Agillos E-Commerce) 3.7% share transfer | 7 October 2026 | p31 L615, p32 L663 (R1551, R1554) | completed ("concluded") |
| FY26 dividend payable settlement (Q1 monitorable, NOTION MEMORY) | Q2 FY27 | p38 L853 (R551), p39 L897 (R636) | completed (Other Liabilities 507 to 150; H1 distributions 361) |

## F17 WHAT WAS NOT DISCUSSED (deck vs Notion checklist, triggers and Q2 monitorables)

| item | deck status | consecutive quarters silent |
| --- | --- | --- |
| #1 Net paying suppliers | ADDRESSED: -615 (L202), -1K (L754), base 217K (L753) | 0 |
| #2 Active buyers | ADDRESSED: 40 Mn, (7%) (L710); rounding at threshold (F16-06) | 0 |
| #3 Unique enquiries | ADDRESSED: 27 Mn, (14%) (L711, L1679) | 0 |
| #4 Top 10% ARPU | ADDRESSED: 365K, +12% (L717) | 0 |
| #5 SA EBITDA margin | ADDRESSED: 40% (L1652) | 0 |
| #6 CFO/PAT rolling 12m | PARTIAL: components only (L1557, L809); ratio not printed | 2 (NOTION MEMORY: Q1 deck also gave no ratio) |
| #7 Busy billing growth and margin | PARTIAL: billing +20% (L1269); margin 12% but no YoY (F16-04) | 2 (margin YoY) |
| #8 Promoter holding and pledge | PARTIAL: about 49%; pledge silent (F17-01) | 2 |
| #9 Treasury OI | PARTIAL: (8) printed; quarterly realised vs MTM split not given (F16-02) | 1 (Q1 deck gave a Q1 column) |
| #10 Auditor commentary | N.A. for a deck (annual item) | n/a |
| #11 Associate cohort P&L | SILENT: folded into "Others" (F17-03) | 2 (NOTION MEMORY: no Q1 deck line) |
| #12 Fleetx mark | SILENT: at cost only (L665) | 2 |
| Supplier churn | SILENT: no churn metric in deck (concall gave silver churn about 7%, NOTION MEMORY FA-06) | 2 |
| Cause of buyer and enquiry decline; dated recovery target | SILENT (F17-02) | 2 |
| IndiaMart Finance Ltd capitalisation | SILENT: entity not named (F15-01) | 2 (Q1 deck also silent, NOTION MEMORY) |
| Bank-verification % vs ladder | SILENT (concall monitorable) | 1 |
| Advertising actual figure | SILENT: S&M 59 only (L1162) | 1 |
| Enquiry-decline residual quantification | SILENT | 1 |

## VALUES FOR A4 TESTS (stated, not ruled)

- Watch 8B, paying-supplier sequential net change (Thousand): Q2 FY26 +4 (R306), Q3 FY26 -1 (R307), Q4 FY26 -1 (R308), Q1 FY27 -2 (R309), Q2 FY27 -1 (R310), all L754. Slide 8: "615 paying suppliers declined this quarter" (R052, L202). Base 217K (R305 L753; R040 L192; R246 L715). Q2 FY27 is the fourth consecutive printed sequential fall in this deck's series.
- Watch 8B, active buyers (LTM): Q2 FY27 40 Mn (R191 L710; R044 L192), Q1 FY27 41 (R190), YoY (7%) (R192; R045). Printed in whole millions (F16-06).
- Thesis-broken #6, unique business enquiries: Q2 FY27 27 Mn (R202 L711; R1404 L1679; R050 L198), YoY (14%) (R203; R1406 L1680; R051). Q1 FY27 26 Mn (R201; R1403). This deck prints no Q1 FY27 YoY. The Q1 deck printed -11% (NOTION MEMORY). This deck's own series implies a Q1 FY26 base of 28, so Q1 FY27 about -7% (F16-03).
- Other checklist values: top 10% ARPU 365K +12% (R268/R269); total ARPU 72K +10% (R257/R258); SA EBITDA margin 40% (R1391); Busy billing 46, +20% (R1165/R1167); Busy EBITDA margin 12% vs FY26 17% (R1220/R1225); Busy licences 465K, +10%, new 11K (R1147/R1154/R1152); consol other income (8) (R336), SA (9) (R718); collections consol 443 +9% (R441/R442), SA 394 +8% (R832/R833); deferred revenue consol 2,029 +16% (R527/R015), SA 1,863 +14% (R966/R973); promoter 49% (R1293); investment table p32 (R148-R177).

```yaml
stage: A3-forensics
company: "INDIAMART"
quarter: "q2fy27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/indiamart-q2fy27/work/forensics_presentation_indiamart_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: PASS
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: N.A.
  F9: N.A.
  F10: FINDING
  F11: PASS
  F12: FINDING
  F13: N.A.
  F14: FINDING
  F15: FINDING
  F16: FINDING
  F17: FINDING
findings:
  - {id: "F1-01", check: "F1", line: "L895/L882 (R617-R622,R1573)", classification: "NEUTRAL-FACT", implication: "Share-issuance line (ESOP+QIP) zero since FY21; non-zero = capital event"}
  - {id: "F1-02", check: "F1", line: "L844/L795 (R479-R481,R1563)", classification: "NEUTRAL-FACT", implication: "Goodwill 454 unchanged since FY23; no impairment; exceptional items folded into Others"}
  - {id: "F2-01", check: "F2", line: "L809/L1010/L801/L1000/L808/L1009 (R411,R813,R336,R718,R403,R805)", classification: "FORWARD-SIGNAL", implication: "Consol-SA PAT gap -14.2% vs -2.3% QoQ and ~-1% YoY; Q1 subsidiary OI gain gone; steady ~20 Cr Others drag is mostly associate losses, never shown as a line"}
  - {id: "F2-02", check: "F2", line: "L1651/L1002/L1004/L718/L1159/L1162/L1164 (R1382,R738,R757,R280)", classification: "AMBIGUOUS", implication: "SA EBITDA +41 Cr YoY is cost-led (headcount -6%, manpower -1%, S&M -3%); bridge ~16 base one-off [INFERENCE] + ~6 SBP + ~19 operating"}
  - {id: "F6-01", check: "F6", line: "L1083/L1091/L1125 (R1500,R965,R989)", classification: "AMBIGUOUS", implication: "'~20%' next-quarter recognition vs realised 18.6% (Q2) / 18.7% (Q1); overstates ~25 Cr a quarter"}
  - {id: "F6-02", check: "F6", line: "L1188-1190/L1241/L1309/L1313 (R1501-R1503,R1152,R1170,R1204)", classification: "FORWARD-SIGNAL", implication: "Busy 'increase new licences' and 'accelerate revenue' contradicted: new licences 11K vs 12K YoY; revenue +27% vs ~+47% Q1"}
  - {id: "F6-03", check: "F6", line: "L526/L710/L711/L715 (R1493,R192,R203,R247)", classification: "CONFIRMATORY-NEGATIVE", implication: "'Keep expanding buyer & supplier network' vs buyers -7%, enquiries -14%, suppliers -2% YoY"}
  - {id: "F6-04", check: "F6", line: "L615/L663/L665 (R142,R167,R1551,R1554)", classification: "AMBIGUOUS", implication: "Aerchain 3.7% transfer concluded 7-Oct-2026 (23.2% to 26.9%); consideration undisclosed; Q3 outflow"}
  - {id: "F10-01", check: "F10", line: "L811/L796/L1461/L895 (R430,R1564,R1292,R622)", classification: "NEUTRAL-FACT", implication: "Single bonus-adjusted EPS line; 91/6.0143 cr = 15.1 ties; share count flat YoY"}
  - {id: "F10-02", check: "F10", line: "L1005/L1007/L994 (R767,R768,R786,R787,R1584)", classification: "AMBIGUOUS", implication: "Share-based payment 5 Cr vs ~11 Q2 FY26 lifts SA EBITDA ~6 Cr YoY; reverses on next grant cycle"}
  - {id: "F12-01", check: "F12", line: "L1309-L1321/L1268/L213-219 (R1169,R1204,R1220,R1165,R1167)", classification: "FORWARD-SIGNAL", implication: "Busy costs +38% vs revenue +27%; EBITDA ~-20% YoY derived, margin ~18% to 12%; billing +20% Q2, ~+14% H1, -22% QoQ"}
  - {id: "F12-02", check: "F12", line: "L1091/L1092/L1590/L925/L812 (R965,R966,R971,R1343,R441,R442)", classification: "FORWARD-SIGNAL", implication: "SA deferred revenue +5 Cr QoQ, smallest build shown; collections growth trails revenue; revenue growth drifting to high single digits"}
  - {id: "F12-03", check: "F12", line: "L951/L955/L943 (R688,R705,R1579)", classification: "NEUTRAL-FACT", implication: "Other subsidiaries ~3 Cr revenue/qtr; Livekeeping (103 Cr) has no separate numbers; EBITDA loss narrowing"}
  - {id: "F14-01", check: "F14", line: "L1154 (R1598)", classification: "AMBIGUOUS", implication: "Functional P&L basis cites 'Note No. 31' that is not in the 6-note filed standalone results; basis unverifiable"}
  - {id: "F14-02", check: "F14", line: "L93/L358-359/L211/L1321/L389/L444 (R1415,R1537,R1538,R057,R103,R106)", classification: "NEUTRAL-FACT", implication: "Cumulative drafting slips; immaterial alone"}
  - {id: "F15-01", check: "F15", line: "L627-631/L545 (R1440,R1441,R1498)", classification: "FORWARD-SIGNAL", implication: "IndiaMart Finance Ltd (incorporated 04-Aug-2026 per results) absent from deck subsidiary list and narrative; lending perimeter and capital undisclosed"}
  - {id: "F15-02", check: "F15", line: "L665/L605 (R154,R155,R140)", classification: "AMBIGUOUS", implication: "MonotaRO associate exit 29-May-2026 invisible; deck has no associate/FVTPL label; second quarter unresolved"}
  - {id: "F15-03", check: "F15", line: "L665/L1046/L1037 (R148-R176,R886,R1588)", classification: "AMBIGUOUS", implication: "p32 table at cost 1,442 vs SA strategic investments 1,556; 114 Cr (7.3%) unbridged"}
  - {id: "F16-01", check: "F16", line: "L183/L1007/L1652/L1651/L1166/L1003 (R033,R787,R1387,R1072,R748)", classification: "AMBIGUOUS", implication: "Headline SA EBITDA +36% on a base with a likely 16 Cr impairment [INFERENCE]; like-for-like ~+19%; YoY cells blank on Other Expenses and G&A"}
  - {id: "F16-02", check: "F16", line: "L801/L1000/L891/L898/L793 (R336,R718,R594,R643)", classification: "FORWARD-SIGNAL", implication: "OI 107 to (8); H1-only table hides Q2 MTM ~-52 Cr (with NOTION MEMORY Q1 96); PAT exposed to yields on ~3,234 Cr treasury"}
  - {id: "F16-03", check: "F16", line: "L1678/L1679/L1680/L1673/L711 (R1399-R1406,R1620,R203)", classification: "AMBIGUOUS", implication: "Q2 (14%) consistent within rounding; Q1 FY26 base is 28 (this deck) vs 31 / ~29 (Q1 deck, NOTION MEMORY); unexplained restatement"}
  - {id: "F16-04", check: "F16", line: "L217-219/L1314-L1320 (R059-R061,R1212,R1234,R1258)", classification: "AMBIGUOUS", implication: "Busy EBITDA/NP/CFO printed without YoY where they fell; second consecutive quarter"}
  - {id: "F16-05", check: "F16", line: "L194/L200/L206 (R041,R045,R051)", classification: "NEUTRAL-FACT", implication: "Declines unsigned in text layer; direction graphic only; second consecutive quarter"}
  - {id: "F16-06", check: "F16", line: "L192/L710 (R044,R191)", classification: "AMBIGUOUS", implication: "Active buyers printed 40 Mn in whole millions, exactly at the 40M trigger line; deck cannot resolve below-40M"}
  - {id: "F16-07", check: "F16", line: "L358/L354/L1373/L1398/L1414 (R1510,R100,R1526-R1528)", classification: "NEUTRAL-FACT", implication: "Geography, sales team, ESG and people data dated 31-Mar-2026, two quarters stale"}
  - {id: "F17-01", check: "F17", line: "L1469/L1473 (R1293,R1611)", classification: "AMBIGUOUS", implication: "Promoter ~49% shown; pledge silent for a second consecutive deck"}
  - {id: "F17-02", check: "F17", line: "L526/L710-712/L754 (R1493,R192,R203,R214,R310)", classification: "CONFIRMATORY-NEGATIVE", implication: "Demand KPIs deteriorate a further quarter; no cause, target or date; second consecutive deck without demand guidance"}
  - {id: "F17-03", check: "F17", line: "L795/L665 (R1563,R152,R153)", classification: "AMBIGUOUS", implication: "Associate cohort P&L and Fleetx mark silent; associate loss folded into Others although it drives the S-vs-C gap"}
forward_signals: ["F2-01", "F6-02", "F12-01", "F12-02", "F15-01", "F16-02"]
ambiguous: ["F2-02", "F6-01", "F6-04", "F10-02", "F14-01", "F15-02", "F15-03", "F16-01", "F16-03", "F16-04", "F16-06", "F17-01", "F17-03"]
commitments:
  - {commitment: "~20% of deferred revenue recognised within next 3 months", implied_date: "Q3 FY27", ref: "p45 L1083 (R1500)", status_word: "none"}
  - {commitment: "Busy: increase new licences sold", implied_date: "undated", ref: "p49 L1190 (R1503)", status_word: "none"}
  - {commitment: "Busy: accelerate revenue growth", implied_date: "undated", ref: "p49 L1189 (R1502)", status_word: "none"}
  - {commitment: "Busy: invest in team and awareness", implied_date: "undated", ref: "p49 L1188 (R1501)", status_word: "none"}
  - {commitment: "Keep expanding buyer and supplier network", implied_date: "undated", ref: "p27 L526 (R1493)", status_word: "none"}
  - {commitment: "Focus on large and medium enterprises", implied_date: "undated", ref: "p27 L532 (R1494)", status_word: "none"}
  - {commitment: "Improve engagement: commerce enablement, fintech and accounting, business enablement SaaS", implied_date: "undated", ref: "p27 L523-527 (R1495-R1497)", status_word: "none"}
  - {commitment: "Commerce stage: credit facilitation, logistics/tracking", implied_date: "undated", ref: "p28 L545-547 (R1498)", status_word: "none"}
  - {commitment: "Aerchain (Agillos E-Commerce) 3.7% share transfer", implied_date: "2026-10-07", ref: "p31 L615, p32 L663 (R1551,R1554)", status_word: "completed"}
  - {commitment: "FY26 dividend payable settlement (Q1 monitorable, NOTION MEMORY)", implied_date: "Q2 FY27", ref: "p38 L853 (R551), p39 L897 (R636)", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "The deck's quarter splits into cost-led standalone margin and shrinking demand volume. The headline +36% SA EBITDA leans on a base that likely carries a 16 Cr impairment (results A3, inference), on a smaller share-based payment charge, and on 6% fewer staff. Like-for-like growth is near 19%. Consolidated PAT growth of 10% absorbed a treasury reversal: Q2 MTM about -52 Cr, using the Q1 MTM figure from Notion memory. The H1-only table hides this. Associate losses now set the S-vs-C gap, and the deck never shows them as a line. Two cross-deck problems need answers: the enquiries Q1 FY26 base (28 here vs 31 in Q1 deck memory) and active buyers printed exactly at 40 Mn. A2 missed 8 ZERO_STANDING tags that A1 set (R480-R481, R617-R622); coverage is unaffected. A4 owns the 8B and #6 rulings; values are listed in the report."
```
