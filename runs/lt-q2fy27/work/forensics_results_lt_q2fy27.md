# A3 FORENSIC NOTES: Larsen & Toubro Limited (LT), Q2 FY27, doctype: results

Inputs read: A1 structured extraction `runs/lt-q2fy27/extracted/lt-results-q2fy27-structured.md` (R001-R2511), A1 fulltext `runs/lt-q2fy27/extracted/lt-results-q2fy27-fulltext.md` (lines 1-1963, read in full), A2 ledger `runs/lt-q2fy27/work/ledger_results_lt_q2fy27.md` (sections 1-12 plus MFS-1..3). No source PDF and nothing under `inputs/` was opened. Prior-quarter fulltext: not held (first LT run). Notion checklist: none (PRE-THESIS READ). F17 uses the operator watch list from the task message.

Units: Rs crore. "Derived" = arithmetic on filed cells; no number below is estimated. Consolidated cash-flow cells (fulltext lines 708-768) are RECONSTRUCTED_FROM_RENDER by A1; A3 re-footed CFO, CFI, CFF, net change and closing cash for both periods, and all tie.

## 0. RECONCILIATION AND FOOTING

**Ledger reconciliation.** The ledger accounts for 2,511 of 2,511 structured IDs plus 3 MISSING_FROM_STRUCTURED rows. A3 read every cited fulltext line (1-1963). MFS-1 (line 92, "Date: 2026.10.27 17:04:53"), MFS-2 (lines 1962-1963, glyph text decodes to 2026.10.27 17:01:26) and MFS-3 (line 1428, parent "Larsen & Toubro Limited") were read at their lines. A3 spot-checked structured rows against the fulltext (R388, R394, R594-R617, R726-R727, R772-R773, R1999, R2030-R2033, R2039, R2124-R2139); all match. Reconciled: 100%.

**Page 12 standalone-items table (consol note iv; R594-R617; lines 603-615): FOOTS. No failure.**
| Test | Q2 FY27 | Q1 FY27 | Q2 FY26 | H1 FY27 | H1 FY26 | FY26 | Result |
|---|---|---|---|---|---|---|---|
| Revenue = standalone P&L line 916 | 43583.58 | 36024.07 | 35115.74 | 79607.65 | 68586.47 | 153680.17 | tie, all 6 |
| PBT pre-exceptional = line 935 | 3999.61 | 5180.05 | 2431.23 | 9179.66 | 6471.32 | 16262.95 | tie, all 6 |
| PBT post-exceptional = line 937 | 3999.61 | 5180.05 | (2981.77) | 9179.66 | 1058.32 | 9141.22 | tie, all 6 |
| PAT = line 943 | 3370.12 | 4455.26 | (3591.17) | 7825.38 | (105.87) | 6287.13 | tie, all 6 |
| Q2 + Q1 = H1 (rev, PBT, PAT) | | | | 79607.65 / 9179.66 / 7825.38 | | | foots |
| Pre-exc + exceptional (line 936) = post-exc | | | 2431.23-5413.00 | | 6471.32-5413.00 | 16262.95-7121.73 | foots |
| PBT - tax (line 942) = PAT | 3999.61-629.49 | 5180.05-724.79 | (2981.77)-609.40 | 9179.66-1354.28 | 1058.32-1164.19 | 9141.22-2854.09 | foots |
Note: lines 604, 606-608, 610-616 carry stamp OCR junk between the rows. The values are clean after it.

**Other footing checks (all tie):** consolidated P&L Q2 expenses to 73415.14 and PBT 7641.06 (lines 473-486); consolidated BS (lines 530-594) and standalone BS (lines 981-1042) sub-totals and totals; consolidated segment revenue 79615.57 and results 7423.25 to PBT 7641.06 (lines 795-819); standalone segment results (lines 1199-1208); consolidated CF (lines 708-768) and standalone CF (lines 1103-1160); Annexure 1 EBITDA 6,845 = revenue 78749.94 less operating expenses 71905.29 (lines 379-380). Standalone segment results show 634.48 twice (I&U Q1 and E-Conv Q2, lines 1199-1200). Both rows foot to totals and to H1, so this is a coincidence, not an OCR copy.

## 1. CASH FLOW AND SEGMENT READ (done first, per task)

| Item (H1) | Consolidated FY27 | Consolidated FY26 | Standalone FY27 | Standalone FY26 | Lines |
|---|---|---|---|---|---|
| Operating profit before WC | 15820.24 | 14855.85 | 5735.21 | 5559.42 | 723 / 1117 |
| Receivables (incr) | (7761.39) | (4172.74) | (4729.30) | (3274.19) | 725 / 1119 |
| Payables incr | 17678.72 | 6165.84 | 8474.44 | 5860.01 | 727 / 1121 |
| FS loan growth | (15858.69) | (9463.02) | n.a. | n.a. | 729 |
| CFO | 5750.53 | 3816.13 | 7617.62 | 6671.33 | 732 / 1124 |
| Capex (gross) | (2563.06) | (2674.72) | (1313.98) | (1436.53) | 734 / 1126 |
| Current investments (net purchase) | (13409.16) | 2321.46 | (6350.82) | 2828.44 | 738 / 1133 |
| Dividends paid | (5227.77) | (4676.22) | (5227.77) | (4676.22) | 760 / 1154 |
| ECL / bad debts | 2353.06 | 1867.74 | 788.56 | 508.32 | 718 / 1114 |

Read: consolidated cash from operations before FS lending rose to 24879.00 from 16212.43 (line 728). The driver is payables and advances: other current liabilities rose 15078.60 in H1 (line 588: 100940.12 vs 85861.52). The group borrowed a net 14731.78 (lines 754-756) and parked 13409.16 in current investments (line 738). Standalone operating profit before WC rose 3.2% on H1 revenue up 16.1%.

Derived net working capital (inventories + trade receivables + other current assets - trade payables - other current liabilities): standalone 1946.07 (Sep-26) vs 5603.17 (Mar-26), 1.2% of TTM revenue 164701.35 vs 3.6% of FY26 revenue. Consolidated (-2139.09) vs 5978.22. The filing gives no company-defined NWC % (see R-33).

## 2. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| R-01 | F1 | R346-R351, R962-R967, R1214-R1219, R1691-R1696 | 487, 936 | "4 Exceptional items [loss] - - - - - (1722.44)"; "Exceptional Items (loss) - - (5413.00) - (5413.00) (7121.73)" | FORWARD-SIGNAL | The exceptional line is nil in every FY27 period, but three pending transactions are its classic classes: the LTMRHL sale (R-11), the Realty slump sale (R-13) and the Vyoma.AI transfer (R-12). Prior-year standalone exceptional losses (5413.00 in Q2 FY26, 7121.73 in FY26) and consolidated (1722.44) in FY26 have no note in this filing. H2 FY27 can carry exceptional gains or losses on standalone and consolidated. Ask what the Q2 FY26 standalone loss was and whether the LTMRHL sale price leaves a further gap to carrying value. |
| R-02 | F1 | R726-R727, R772-R773, R774-R775, R778-R779, R794-R795, R2439 | 720, 745, 746, 748, 757, 877 | "(Gain)/loss on disposal of subsidiary/associate/business undertaking \| (332.93) \| -"; "Consideration received on transfer of business undertaking \| 493.00 \| -" | AMBIGUOUS | Four zero-standing CF lines fired in H1 FY27: disposal gain 332.93, business-undertaking consideration 493.00, subsidiary disposal consideration 3830.99, NCI stake buy (698.99). Test of the presentation A3 claim: a disposal gain exists and bypasses exceptional items (line 487 nil). The filing never names LTTS or SWC. The CF is H1-only, so no quarter is filed. Note IV puts disposal profits in segment revenue only "in the case of Development Pro1ects and Realty segment" (line 877). A TPS business gain therefore sits in other income, but the 332.93 line also covers subsidiaries, so it can include Nabha Power (a DP segment-revenue item). Partly confirmed. Ask for the split of 332.93 by transaction, quarter and P&L line, and which subsidiary's NCI stake was bought for 698.99. |
| R-03 | F1 | R648-R653, R1432-R1437, R1505-R1506, R722-R723 | 632, 1056, 1114, 718 | "6 Bad debts to accounts receivable ratio 0.00 0.00 0.00 0.00 0.00 0.01"; "Bad debts/Allowance for expected credit loss (net) 788.56 508.32" | AMBIGUOUS | The ratio numerator is write-offs only (formula line 668/1079), so it reads 0.00. Standalone ECL plus bad debts rose 55% YoY in H1 (788.56 vs 508.32). Consolidated rose 26% (2353.06 vs 1867.74; most of it is FS credit cost, and the ratio excludes FS). Rising allowances with nil write-offs can come before future write-offs. Ask which E&C counterparties drive the standalone ECL step-up. |
| R-04 | F2 | R394-R399, R612-R617, R1124-R1129, R1549-R1550, R382-R387, R400-R405 | 496, 615, 918, 1143 | "Attributable to: Owners of the Company 5202.10 4122.85 3926.09"; "Dividend received from subsidiaries, joint venture and associate companies 3474.71 1817.40" | NEUTRAL-FACT | The S-vs-C PAT gap swung from (332.41) in Q1 (-7.5% of standalone PAT) to 1831.98 in Q2 (+54.4%), a move of 61.9 pp (>5 pp threshold). The mechanism is intra-group dividends in standalone other income (Q1 4094.41), which consolidation eliminates. The H1 CF is not split by quarter, so the dividend split is NOT FOUND. Standalone PAT is not a clean core-earnings proxy in Q1/Q2. See the table in section 3. |
| R-05 | F2 | R112-R117, R134-R139, R250-R255, R322-R327, R328-R333, R340-R345 | 380, 384, 469, 483, 484 | "6,806 6,845 1% EBITDA"; "3,926 5,202 33% Consolidated Profit After Tax"; "b) Other income (net) 2306.26 2376.73 1384.28" | FORWARD-SIGNAL | Q2 consolidated PBT rose 1304.95. The derived bridge: EBITDA +38.24, other income +921.98, finance costs -289.87, D&A -54.86 (foots). Other income is 71% of the PBT gain and 30.2% of Q2 PBT (21.8% a year ago). EBITDA margin fell to 8.7% from 10.0%. The 33% PAT growth rate holds only if other income, the finance cost fall (R-06) and the tax credit (R-16) all repeat. |
| R-06 | F2 | R322-R327, R1190-R1195, R554-R555, R568-R571, R702, R1911-R1917, R1928-R1929 | 483, 932, 320, 646 | "e) Finance costs 472.94 538.67 762.81"; "(b) Hyderabad Metro till April 30, 2026, in line with the terms of the Share Purchase Agreement" | AMBIGUOUS | Consolidated non-FS finance costs fell 38% YoY. Over the same H1, total borrowings rose 14545.03 (lines 572, 581, 582) and D/E rose to 1.02, or 1.12 with held-for-sale debt (line 646). The derived subsidiary share of finance cost fell to 67.64 from 286.58. [INFERENCE] The fall is mostly LTMRHL leaving the P&L after 30-Apr-2026 under the SPA. This is a perimeter effect, not deleveraging. Ask for LTMRHL's finance cost in Q2 FY26 and how post-30-April LTMRHL results are accounted for. |
| R-07 | F2 | R1589-R1594, R1637-R1642, R824-R829, R890-R895, R150-R151 | 1191, 1200, 224 | "2 Energy - Conventional 634.48 509.04 590.30 1143.52 1335.84 3010.80" | FORWARD-SIGNAL | Standalone E-Conv EBIT margin fell to 5.88% from 8.71% (-283 bps). H1 standalone E-Conv result fell 14.4% on revenue up 44.0%. The derived subsidiary E-Conv margin rose to 8.05% from 6.50%. The press release blames "a higher proportion of orders in early stages of execution within the CarbonLite Solutions business" (line 224). That dilution sits in the parent (domestic BTG). If CarbonLite orders keep ramping, E-Conv margin can fall further before it recovers. |
| R-08 | F2 | R1456-R1461, R1118-R1123, R1208-R1213, R1124-R1129 | 1060, 918 | "10 Operating margin (%) 5.49% 5.31% 6.61% 5.41% 6.87% 8.18%" | FORWARD-SIGNAL | The standalone core margin is compressing. Derived standalone EBITDA rose 3.1% (2391.35 vs 2319.76) on revenue up 24.1%. Standalone PBT excluding other income rose 12.0% (1521.17 vs 1357.70). Other income is 62.0% of standalone Q2 PBT. The watch-list item "core E&C margin" is moving down on the standalone ratio. |
| R-09 | F4 | R1811-R1834, R2312-R2326, R2484-R2487 | 1332-1335, 1345-1354 | "We did not review the interim financial information of 42 subsidiaries" | NEUTRAL-FACT | Paras 6-9 cover components not reviewed by MSKA. Their PAT is 3403.82 of Q2 consolidated PAT 5949.15 (57.2%) and 7490.49 of H1 10937.18 (68.5%), above the 10% threshold. It is structural: the listed subsidiaries (LTM, LTTS, L&T Finance) have their own auditors. 100% of the JV and associate share also rests on other auditors' or management numbers. The prior-period ratio is NOT FOUND (prior LRR not held), so the YoY jump test is not run. Ratios use subsidiary PAT before consolidation adjustments and are indicative. |
| R-10 | F4 | R1835-R1849, R2327-R2335, R2488-R2489 | 1363-1368, 1387 | "total revenue of Rs. 199.00 crore and Rs. 391.94 crore, total net profit after tax of Rs. 238.81 crore and Rs. 541. 98 crore"; "financial information is not material to the Group." | AMBIGUOUS | 41 subsidiaries had no review by any auditor, and their PAT exceeds their revenue (Q2 238.81 on 199.00; H1 541.98 on 391.94). That profit must come from non-revenue items: gains, dividends or tax. H1 541.98 is 5.8% of owners' H1 PAT, yet management calls it "not material". Ask which entities earn it and from what. A disposal gain booked in an unreviewed holding entity would link to R-02. |
| R-11 | F6 | R1928-R1929, R2133, R1933, R2136 | 517, 965 | "The divestment process is underway and the estimated completion date for the transaction has been revised to December 31, 2026" | FORWARD-SIGNAL | The LTMRHL sale to HMRL (SPA 29-Apr-2026) has slipped; "revised" signals a missed earlier date. The prior date is not in this filing (prior quarter not held). Held-for-sale debt keeps D/E at 1.12 (line 646) until close. Close by 31-Dec-2026 is the Q3 milestone to test. |
| R-12 | F6 | R1934-R1935, R2137, R1354-R1355 | 967-970, 1008 | "The transfer is expected to be completed by 03 2026-27." | FORWARD-SIGNAL | The data-centre and cloud business (BTA, 11-Aug-2026) and the L&T Network Services stake are moving to Vyoma.AI, a wholly owned subsidiary, by Q3 FY27 ("03" is OCR for Q3). Standalone held-for-sale assets rose to 2778.35 from 1599.11. [INFERENCE] Building one data-centre vehicle comes before any external capital raise or stake sale (see R-28). Ask whether an outside investor is planned. |
| R-13 | F6 | R1931-R1932, R2135 | 959-963 | "Scheme is subject to approval of the Hon'ble National Company Law Tribunal" | FORWARD-SIGNAL | The Realty Undertaking slump sale to LTRPL was Board-approved 08-Dec-2025, with appointed date 01-Apr-2026, and is still pending NCLT. The note is standalone-only, with no consolidated twin. On completion, standalone can book a transfer gain or loss and segment comparability changes. The consolidated effect is limited to tax and NCI. Ask for the expected NCLT timeline. |
| R-14 | F7 | R140-R141, R146-R147, R152-R153, R174-R175, R184-R185, R2127, R2131 | 190, 234, 305, 349, 387-395 | "the deferment of select targeted orders"; "deferrals in the Solar business"; "some new launches are delayed"; "The Middle East continue to pose varied downside risks" | FORWARD-SIGNAL | One release carries three deferral or delay hedges plus a Middle East risk line. Derived: all of the Q2 order-inflow growth is Energy-Conventional (78,413 vs 38,349). Excluding E-Conv, inflow fell 10.6% (69,252 vs 77,435). I&U fell 13%, E-Green 45%, Realty 12%. Order concentration in one segment and one region is rising. Deferred orders are next quarter's test. |
| R-15 | F7 | R2440, R2480 | 884, 1259 | "In respect of some segments of the Groop. revenue and margin do not accrue uniformly"; "In respect of segments of the Company, revenue and margin do not accrue uniformly" | NEUTRAL-FACT | The lumpiness hedge is broader in standalone (all segments) than in consolidated ("some segments"). Without the prior quarter, A3 cannot tell whether the wording is new. Track the wording next quarter. |
| R-16 | F8 | R358-R375 | 491, 492 | "b) Deferred tax (337.06) 58.23 72.05 (278.83) 87.51 63.45" | FORWARD-SIGNAL | Q2 consolidated ETR was 22.6% vs 28.0% in Q1, 26.0% in Q2 FY26 and the 25.17% statutory rate. The current-tax-only ETR is 27.0%. The deferred credit is a 441 bps shield on Q2 PBT. The YoY deferred swing of 409.11 equals 32% of the owners' PAT increase of 1276.01. The NCI split is NOT FOUND. Standalone contributes (116.25) (line 941); subsidiaries contribute 220.81. ETR can step back up in H2. Ask for the DTA source (losses, MAT, or timing). |
| R-17 | F8 | R1226-R1243, R1489-R1490, R1549-R1550 | 942, 1105 | "Total tax expense 629.49 724.79 609.40 1354.28 1164.19 2854.09" | NEUTRAL-FACT | Standalone ETR is 15.7% in Q2 and 14.8% in H1. The derived ETR on PBT excluding dividends received (3511.13) is 23.9%. [INFERENCE] Intra-group dividends are taxed lightly in the parent (Sec 80M pass-through). No line "tax relating to earlier years" appears in either P&L, so that test is clean. |
| R-18 | F9 | R406-R423, R1250-R1255, R1262-R1267 | 499, 501, 945, 340 | "a) i) Items that will not be reclassified to profit and loss (172.63) 129.59 (31.60) (43.04) (122.28) (115.88)" | AMBIGUOUS | The consolidated Q2 non-reclassifiable OCI loss (172.63) exceeds full FY26 (115.88). Standalone Q2 (187.21) equals 96% of FY26. The reclassifiable line swung by 1,185 (Q1 976.13 to Q2 (208.89)) against FY26 (723.61). [INFERENCE] The RBI raised the repo rate 25 bps (line 340). A rate rise normally gives actuarial gains on the obligation, so a loss points to plan assets or FVOCI equity marks. Verify the discount rate and plan assets at the Annual Report. |
| R-19 | F12 | R112-R117, R140-R179, R932-R955, R250-R255, R328-R333 | 380, 387-393, 815, 816, 818 | "Add: Unallocable corporate income net of expenditure 712.10 731.39 565.24"; "Total 7423.25 6747.50 6564.61" | AMBIGUOUS | Test of the presentation A3 claim: CONFIRMED on filed numbers. Annexure 1 margin x customer revenue gives 7,117.86 for six segments. Add FS result 1318.85 and DP (16) for 8,420.71, vs group EBITDA 6,845, an excess of 1,575.7. In Q2 FY26 the same calculation gives an excess of 726.6. Statement route: segment results 7423.25 + D&A 1036.91 - inter-segment 21.35 = 8438.81 vs EBITDA 6844.65. The residual is 1594.16 = other income 2306.26 minus unallocable net 712.10 (Q1 1645.34; Q2 FY26 819.04; H1 3239.50 vs 1618.60). Segment results rose 13.1% YoY while group EBITDA rose 0.6%. Reading A: corporate cost stepped up about 775 a quarter. Reading B: more other income now sits inside segment results. The split of unallocable income and expenditure, by quarter, separates the two readings. Ask for it. |
| R-20 | F12 | R140-R145, R884-R889, R818-R823, R974-R979, R1046-R1051 | 387, 401, 795, 807, 823, 836 | "Infrastructure & Utilities 40,755 35,509 23,717 25,133 6.2% 5.7%" | FORWARD-SIGNAL | The largest segment is weak on three fronts. Q2 order inflow fell 13% ("deferment", line 190). Q2 EBIT rose 0.7% on gross revenue up 6.0%, and H1 EBIT fell 3.7%. Derived net segment capital rose 12.1% in H1 (21385.35 to 23971.66) against H1 revenue up 1.9%. YoY it is lower (25749.15 at Sep-25), so seasonality is possible. Ask about the receivable and unbilled build in domestic I&U. |
| R-21 | F12 | R980-R991, R1052-R1063, R580-R581, R738-R739 | 824, 825, 837, 838, 588, 727 | "3 Energy - Green 34093.59 25606.08 9878.95" | AMBIGUOUS | In both Energy segments, liabilities exceed assets, and the gap widened. E-Green net capital is (1920.87) at Sep-26 vs 423.52 at Mar-26 and 2164.44 at Sep-25. E-Green liabilities are 3.45x YoY. E-Conv net is (4316.38) vs (2214.80). [INFERENCE] This is customer-advance funding (consolidated other current liabilities +15078.60; CF payables +17678.72). Today's CFO is flattered. As offshore wind and hydrocarbon execution consumes the advances, working capital reverses and cash flows out. Ask for the advance balance and burn schedule. |
| R-22 | F12 | R992-R997, R1064-R1069, R1721-R1726, R1775-R1780, R836-R841, R1308-R1309 | 826, 839, 1217, 982, 404 | "4 Manufacturing & Products 24040.36 21965.28 17697.40" | FORWARD-SIGNAL | Derived M&P net capital rose to 7675.55 from 5026.27 (+52.7% in H1; +42.2% YoY) against H1 gross revenue up 23.7%. H1 EBITDA margin was 15.3% vs 15.8%. Standalone CWIP fell (1439.81 to 974.40), so [INFERENCE] the build is working capital, not plant. Capital is running ahead of revenue in the highest-margin E&C-adjacent segment. Ask what drives it. |
| R-23 | F12 | R1010-R1015, R1082-R1087, R490-R493, R2127 | 829, 842, 532, 533, 305 | "7 Realty 15503.34 14549.67 12165.78" | FORWARD-SIGNAL | Realty assets rose 14.6% and liabilities 24.7% in H1, while Q2 customer revenue fell 43% and launches slipped. Investment property rose to 706.73 from 223.22 as IPUC fell to 377.37 from 897.12, so one commercial asset moved to completed. Inventory is building ahead of delayed launches, and handovers drive margin (54.3% vs 67.6%). |
| R-24 | F12 | R180-R183, R860-R865, R926-R931, R1016-R1021, R1088-R1093, R540-R541, R588-R589, R2128 | 394, 802, 830, 843, 560, 592, 325 | "8 Development Projects 17142.81 17024.32 25186.78"; "as the Green Energy business is in investment phase" | FORWARD-SIGNAL | DP had nil revenue and an EBIT loss of 16 in Q2, with assets of 17142.81 (+0.7% QoQ) and liabilities of 2023.97. [INFERENCE] Most DP assets are the LTMRHL held-for-sale block (consolidated HFS assets 16340.78), with that block's borrowings in HFS liabilities (15714.94), outside segment liabilities. After the LTMRHL close, DP becomes a pre-revenue green-energy build (Panipat Green Hydrogen, L&T Green Energy Kandla). Trend its asset accretion as a capex proxy. |
| R-25 | F14 | R2318-R2326, R1820-R1834 | 1354 | "period from April 01, 2026 and September 30, 2026" | NEUTRAL-FACT | Auditor-letter drafting slip ("and" for "to") in consolidated LRR para 7. Immaterial alone. It counts as one governance data point. |
| R-26 | F14 | R1911-R1917, R2182-R2193, R1928-R1929, R1933 | 320-321, 516-518, 964-966 | "(b) Hyderabad Metro till April 30, 2026, in line with the terms of the Share Purchase Agreement"; "The divestment process is underway" | AMBIGUOUS | Only the press release states the 30-April economic cut-off. Consolidated note (ii) and standalone note (iii) do not state it or its accounting, though it drives the DP nil revenue and part of the finance cost fall (R-06). Ask how post-30-April LTMRHL results are recognised (payable to buyer, or excluded). |
| R-27 | F14 | R164-R173, R184-R187 | 391, 392, 395 | "Financial Services 4,166 5,307 4,166 5,307" | NEUTRAL-FACT | The order-inflow definition counts FS order inflow as equal to revenue, and TPS inflow (14,807) is about equal to its revenue (14,826). So 20,114 (13.6%) of Q2 "order inflow" of 1,47,665 is revenue-equivalent, not backlog. Use E&C-only inflow for book-to-bill. |
| R-28 | F15 | R2031-R2033, R2039, R2344-R2346 | 1579-1581, 1588, 1665-1667 | "Vyoma.AI Limitedc"; "L TN Compute Private Limitede"; "Sovcloud Technologies Limitedd" | FORWARD-SIGNAL | New entities: Vyoma.AI (incorporated 22-Apr-2026), LTN Compute and LTA Data Centres (20-Jun-2026), and associate Sovcloud Technologies (17-Jun-2026). Together with E2E Networks (associate) and the R-12 transfer, a separate data-centre and sovereign-cloud cluster is forming. An associate formed at incorporation implies an outside partner. Name NOT FOUND. Ask who the partner is. |
| R-29 | F15 | R2030, R2343, R778-R779 | 1578, 1664, 748 | "International Green Scapes Limitedb"; "Acquired on April 13, 2026" | AMBIGUOUS | This acquisition has no note. Consolidated CF shows (805.30) paid for subsidiaries "including contingent consideration" in H1. The price, the business and the segment are NOT FOUND. Ask. |
| R-30 | F15 | R1999, R2347, R774-R775, R1914 | 1501, 1668, 746, 319-320 | "60 Nabha Power Limited1"; "Divested w.e.f. June 25, 2026" | NEUTRAL-FACT | Nabha Power was divested in Q1 and is still listed for the period. [INFERENCE] It accounts for most of the 3830.99 disposal consideration. Any gain sits in DP segment revenue per note IV, not in exceptional items. |
| R-31 | F15 | R1945, R1954, R2034-R2036, R2494 | 1435, 1444, 1583-1585, 1663 | "The entities are in the process of liquidation." | NEUTRAL-FACT | Five entities are in liquidation (symbol a): L&T Qatar LLC, L&T Heavy Engineering LLC, Gujarat Leather Industries, L&T Camp Facilities LLC, and L&T Qatar & HBK Contracting. These are cleanup exits, two of them Qatar entities. |
| R-32 | F15 | R1958, R1960-R1962, R1968-R1971, R2027 | 1448, 1450-1452, 1459-1462, 1575 | "19 L TM Limited (formerly known as LTIMindtree Limited)" | NEUTRAL-FACT | Renames: LTIMindtree became LTM, and its subsidiaries were renamed to match. L&T Sapura Shipping became L&T Offshore Marine, which drops the former partner name. [INFERENCE] This may mark a change in the partner relationship. Relationship status NOT FOUND. |
| R-33 | F17 | R001-R030, R2129-R2132 | 129, 152, 159, 330-355, 349 | "International revenues during the quarter were at ₹ 45,870 crore"; "The Middle East continue to pose varied downside risks" | AMBIGUOUS | Silence audit against the operator watch list (table in section 6). The filing does not disclose: the Middle East share (it gives only "International"), any FY27 guidance, or company-defined working capital % of sales. 1 quarter of silence (first LT run). Results filings often omit guidance, so this goes to the concall as questions, not a negative. |

## 3. F2 STANDALONE vs CONSOLIDATED DECOMPOSITION

| Period | C revenue | S revenue | S/C rev | C EBITDA (derived) | S EBITDA (derived) | Subsidiary EBITDA | C owners PAT | S PAT | Gap | Gap % of S PAT |
|---|---|---|---|---|---|---|---|---|---|---|
| Q2 FY27 | 78749.94 | 43583.58 | 55.3% | 6844.65 | 2391.35 | 4453.30 | 5202.10 | 3370.12 | 1831.98 | 54.4% |
| Q1 FY27 | 67941.74 | 36024.07 | 53.0% | 6116.48 | 1914.60 | 4201.88 | 4122.85 | 4455.26 | (332.41) | (7.5%) |
| Q2 FY26 | 67983.53 | 35115.74 | 51.7% | 6806.41 | 2319.76 | 4486.65 | 3926.09 | (3591.17) | 7517.26 | n/m reported; 115.5% on derived pre-exceptional S PAT 1821.83 |
| H1 FY27 | 146691.68 | 79607.65 | 54.3% | | | | 9324.95 | 7825.38 | 1499.57 | 19.2% |
| H1 FY26 | 131662.45 | 68586.47 | 52.1% | | | | 7543.28 | (105.87) | 7649.15 | n/m reported; 42.1% on derived pre-exceptional S PAT 5307.13 |
| FY26 | 285874.36 | 153680.17 | 53.8% | | | | 16083.99 | 6287.13 | 9796.86 | 155.8% (both sides carry exceptional items) |

Derived pre-exceptional standalone PAT assumes the 5413.00 exceptional carried no tax. Basis: total tax 609.40 on pre-exceptional PBT 2431.23 = 25.07% ETR. EBITDA = PBT + finance costs + D&A - other income, which reproduces the filed operating-margin ratios (lines 636, 1060).

H1 FY27 decomposition (derived): standalone PAT 7825.38, less intra-group dividends received 3474.71 (line 1143, eliminated), plus JV/associate share 39.18 (line 494), less NCI 1612.23 (line 497), plus residual subsidiary contribution after eliminations 6547.33, equals owners' PAT 9324.95. For comparison, the auditor-reported PAT of 83 subsidiaries is 6893.66 + 541.98 = 7435.64 (before consolidation adjustments; the 11 MSKA-reviewed subsidiaries are not disclosed). Subsidiary revenue grew 7.0% YoY in Q2 (35166.36 vs 32867.79), while derived subsidiary EBITDA fell 0.7% (margin 12.66% vs 13.65%).

## 4. F4 UNAUDITED CONTRIBUTION

| Para | Scope | Q2 PAT | H1 PAT | Lines |
|---|---|---|---|---|
| 6 | 11 joint operations, other auditors | 37.22 | 6.94 | 1332-1335 |
| 7 | 42 subsidiaries, other auditors | 3089.63 | 6893.66 | 1345-1348 |
| 7 | 2 associates + 2 JVs, other auditors (share) | 24.26 | 19.12 | 1352-1355 |
| 8 | 41 subsidiaries, NOT reviewed | 238.81 | 541.98 | 1363-1366 |
| 8 | 4 associates + 7 JVs, NOT reviewed (share) | 14.77 | 31.99 | 1370-1373 |
| 9 | 23 joint operations, NOT reviewed | (0.87) | (3.20) | 1390-1393 |
| Total outside MSKA review | | 3403.82 (57.2% of 5949.15) | 7490.49 (68.5% of 10937.18) | |
| Of which management-furnished only | | 252.71 (4.2%) | 570.77 (5.2%; 6.1% of owners' PAT) | |
Entity counts tie: joint operations 11 + 23 = 34 consolidated (lines 1611-1646), 10 + 22 = 32 standalone (lines 1812-1843). Associates 2 + 4 = 6 and JVs 2 + 7 = 9 tie to Annexure A. Subsidiaries 42 + 41 = 83 of 94, so MSKA reviews 11 directly.

## 5. CHECKLIST SCORECARD

| Check | Status | One-line basis |
|---|---|---|
| F1 | FINDING | R-01 to R-03. Exceptional line nil with three pending transactions. Four CF M&A lines fired in H1. Bad-debt ratio 0.00 while ECL rose 55% (standalone). Annexure III deviation NIL (line 1946) is clean. |
| F2 | FINDING | R-04 to R-08. PAT gap swing 61.9 pp of standalone PAT. Other income is 71% of PBT growth. Finance cost fall is a perimeter effect. Standalone E-Conv and core margins are compressing. |
| F3 | PASS | No shells. Standalone vs consolidated cost lines differ materially (Q2 employee cost 3283.75 vs 14245.58, lines 929/481; raw materials 8645.17 vs 11255.26). No going-concern EoM to reconcile. |
| F4 | FINDING | R-09, R-10. 57.2% of Q2 PAT outside MSKA review (structural). 41 unreviewed subsidiaries post PAT above revenue. Prior-period trend NOT FOUND. |
| F5 | PASS | Both LRR conclusions unmodified (lines 1317-1323, 1712-1717). No EoM or going-concern paragraph; only Other Matters reliance. Prior-quarter text not held, so no verbatim diff is possible. The in-filing consolidated vs standalone joint-operation paragraphs are consistent. |
| F6 | FINDING | R-11 to R-13. LTMRHL completion revised. Vyoma.AI expected by Q3 FY27. Realty scheme awaits NCLT. Register in section 7. |
| F7 | FINDING | R-14, R-15. Three deferral or delay hedges plus Middle East risk. Lumpiness hedge wording differs between standalone and consolidated. |
| F8 | FINDING | R-16, R-17. Consolidated deferred credit 337.06; Q2 ETR 22.6%. Standalone ETR 15.7%, explained by dividends. No earlier-years tax line. |
| F9 | FINDING | R-18. Q2 consolidated non-reclassifiable OCI loss exceeds full FY26. Reclassifiable swing 1,185. |
| F10 | PASS | Paid-up 275.13 to 275.15 to 275.18 (line 509). The Q2 rise of 0.03 matches 1,65,811 ESOP shares x Rs 2 (line 515). Basic vs diluted spread 0.01 in Q2 and 0.02 in H1 vs 0.03 in H1 FY26 (lines 512-513): not widening. |
| F11 | PASS | Consolidated 275.18 + 112753.67 = 113028.85 (line 566). Sec 2(57) net worth 110724.45 (line 640): gap 2304.40 (2.0%). Standalone 76918.72 vs 75462.76 (line 1064): gap 1455.96 (1.9%). Both below 5%. Candidates: OCI and hedge reserves, capital reserve. Other equity roll-forward ties (standalone within about 6; consolidated gap of about 652 consistent with the NCI stake buy of 698.99). No third-party net worth in the filing. |
| F12 | FINDING | R-19 to R-24. Segment EBITDA exceeds group EBITDA by 1,576 (confirmed). I&U weak. Energy segments are advance-funded. M&P capital +53%. Realty inventory build. DP pre-revenue. FS assets +15,411 vs liabilities +14,325 is borrowing-funded loan growth (12%, line 292). Neutral. |
| F13 | PASS | The board letter approves results only (lines 42-46). No AR, AGM, record date, dividend, director, auditor or capital-raising item. Meeting 14:00-16:45 (line 82); signatures at 17:04:53 (line 92) and 17:01:26 (lines 1962-1963) come after the close. Rs 500 crore unsecured tokenised NCD (lines 1892-1900), fully used with no deviation. |
| F14 | FINDING | R-25 to R-27. LRR date slip. Metro cut-off appears only in the press release. Order-inflow definition includes revenue-equal businesses. Note text and auditor letter agree on "Limited Review" (lines 52, 779, 1171, 1305). |
| F15 | FINDING | R-28 to R-32. Changes come from filed symbols b-f (all dated Q1 FY27) plus liquidations and renames. No prior list, so no true diff. LTMRHL is still a subsidiary (line 1498). |
| F16 | N.A. | Presentation-specific check on a results doctype, and no prior deck is held. The order-inflow definition point is under F14 (R-27). |
| F17 | FINDING | R-33. The doctype default is N.A. The task message directed the silence audit against the operator watch list, so it was applied to the filing. Table in section 6. |

## 6. F17 SILENCE AUDIT (operator watch list vs this filing)

| Watch item | Addressed in filing? | Evidence | Consecutive quarters silent |
|---|---|---|---|
| Order inflow | Yes | 1,47,665, +28% (lines 144, 395). Growth is all E-Conv; ex-E-Conv -10.6% (R-14) | 0 |
| International (Middle East) share | Partly. International yes, Middle East NO | Orders 63%, book 54%, revenue 58% (lines 152, 159, 129). Middle East appears only as a risk (line 349) | 1 (Middle East split) |
| Order book and book-to-bill | Yes (book), derived (ratio) | 8,53,514, +15% vs Mar-26 (line 158). Derived: Q2 inflow/revenue 1.88x, H1 1.74x, book/TTM revenue 300903.59 = 2.84x | 0 |
| Core E&C margin | Yes, by segment | I&U 5.7%, E-Conv 7.4%, E-Green 6.0%, M&P 15.7% (lines 387-390). Standalone operating margin 5.49% vs 6.61% (line 1060). Derived four core segments EBIT 3580.92, +17.9%, margin 6.07% vs 6.18% | 0 |
| Working capital % of sales | NO | Not disclosed. Derived standalone NWC 1.2% of TTM revenue (section 1). Energy advances flatter it (R-21) | 1 |
| Group vs core split | Yes, by segment | Q2 segment results: TPS + FS 3761.36 (50.7%; 48.7% a year ago), four core 3580.92 (48.2%), Realty + DP 80.97 (1.1%) (lines 807-815) | 0 |
| FY27 guidance (inflow, revenue, margin) | NO | The outlook (lines 330-355) carries no company numbers. The CMD says only "well positioned to sustain this growth momentum" (line 172) | 1 |

## 7. COMMITMENT REGISTER (F6)

| Commitment | Implied date | Note / line ref | Status word |
|---|---|---|---|
| Complete LTMRHL divestment to HMRL (SPA 29-Apr-2026) | 31-Dec-2026 (revised) | consol note (ii) line 517; standalone note (iii) line 965 | underway (revised) |
| Transfer data-centre and cloud business (BTA) and LTNS stake to Vyoma.AI (agreements 11-Aug-2026) | Q3 FY27 (by 31-Dec-2026) | standalone note (iv) lines 967-970 | initiated (expected to be completed) |
| Realty Undertaking slump sale to LTRPL (Board 08-Dec-2025; appointed date 01-Apr-2026) | NOT FOUND (NCLT pending) | standalone note (ii) lines 959-963 | initiated (subject to approval) |
| Hyderabad Metro results included only till 30-Apr-2026 per SPA | 30-Apr-2026 (passed) | press release line 320 | completed (cut-off applied) |
| Nabha Power divestment | 25-Jun-2026 | press release line 319-320; Annexure A legend line 1668 | completed |
| Offshore Wind execution | Q2 FY27 | press release line 242 | commenced |
| Green Energy business build (DP) | NOT FOUND | press release line 325 | underway (investment phase) |
| Lakshya 2031 re-segmentation | 01-Apr-2026 | consol segment note (II) line 852; standalone line 1236 | completed (implemented) |
| Liquidation of five entities | NOT FOUND | Annexure A legend line 1663 | in the process of |
| NCD proceeds not to be used for capital markets or land | continuing | Annexure III line 1939 | completed (Rs 500 crore used, no deviation, lines 1892, 1946) |
| Continue to invest in innovation, digital, technology-led businesses | undated | press release line 172-174 | undated intent |

```yaml
stage: A3-forensics
company: "LT"
quarter: "q2fy27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/lt-q2fy27/work/forensics_results_lt_q2fy27.md"
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
  F9: FINDING
  F10: PASS
  F11: PASS
  F12: FINDING
  F13: PASS
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: FINDING
findings:
  - {id: "R-01", check: "F1", line: "487, 936", classification: "FORWARD-SIGNAL", implication: "Exceptional line nil in FY27 while LTMRHL sale, Realty slump sale and Vyoma.AI transfer are pending; prior-year standalone exceptional (5413.00 Q2 FY26; 7121.73 FY26) unexplained in filing; H2 exceptional items likely"}
  - {id: "R-02", check: "F1", line: "720, 745, 746, 757, 877", classification: "AMBIGUOUS", implication: "Disposal gain 332.93 (H1) and undertaking consideration 493.00 bypass exceptional items; filing never names LTTS SWC, no quarter split; 332.93 may also hold Nabha gain (DP segment revenue per note IV); NCI stake buy 698.99 unnamed"}
  - {id: "R-03", check: "F1", line: "632, 1056, 1114, 718", classification: "AMBIGUOUS", implication: "Bad-debt ratio 0.00 counts write-offs only; standalone ECL up 55% (788.56 vs 508.32), consolidated up 26%; allowances can precede write-offs"}
  - {id: "R-04", check: "F2", line: "496, 615, 918, 1143", classification: "NEUTRAL-FACT", implication: "S-vs-C PAT gap swung from -7.5% to +54.4% of standalone PAT (61.9 pp) on intra-group dividend timing (H1 3474.71); standalone PAT not a core proxy"}
  - {id: "R-05", check: "F2", line: "380, 384, 469, 483, 484", classification: "FORWARD-SIGNAL", implication: "Q2 PBT +1304.95: other income +921.98 (71%), finance cost -289.87, D&A -54.86, EBITDA +38.24; EBITDA margin 8.7% vs 10.0%; 33% PAT growth not repeatable on core"}
  - {id: "R-06", check: "F2", line: "483, 932, 320, 646", classification: "AMBIGUOUS", implication: "Finance costs -38% while borrowings +14545 and D/E 1.02 (1.12 incl HFS); subsidiary finance cost 67.64 vs 286.58; likely LTMRHL exit after 30-Apr per SPA, a perimeter effect not deleveraging"}
  - {id: "R-07", check: "F2", line: "1191, 1200, 224", classification: "FORWARD-SIGNAL", implication: "Standalone E-Conv EBIT margin 5.88% vs 8.71% (-283 bps), H1 result -14.4% on revenue +44%; CarbonLite dilution sits in parent; subsidiaries improved to 8.05%"}
  - {id: "R-08", check: "F2", line: "1060, 918", classification: "FORWARD-SIGNAL", implication: "Standalone operating margin 5.49% vs 6.61%; standalone EBITDA +3.1% on revenue +24.1%; other income 62% of standalone PBT"}
  - {id: "R-09", check: "F4", line: "1332-1335, 1345-1354", classification: "NEUTRAL-FACT", implication: "57.2% of Q2 and 68.5% of H1 consolidated PAT outside MSKA review (listed subs own auditors); 100% of JV/associate share; prior trend NOT FOUND"}
  - {id: "R-10", check: "F4", line: "1363-1368, 1387", classification: "AMBIGUOUS", implication: "41 unreviewed subsidiaries post PAT above revenue (H1 541.98 on 391.94), 5.8% of owners PAT, called not material; source of non-revenue profit unknown"}
  - {id: "R-11", check: "F6", line: "517, 965", classification: "FORWARD-SIGNAL", implication: "LTMRHL completion revised to 31-Dec-2026; slippage; HFS debt keeps D/E at 1.12 until close"}
  - {id: "R-12", check: "F6", line: "967-970, 1008", classification: "FORWARD-SIGNAL", implication: "Data-centre/cloud business and LTNS moving to Vyoma.AI by Q3 FY27; standalone HFS 2778.35 vs 1599.11; precursor to possible external raise"}
  - {id: "R-13", check: "F6", line: "959-963", classification: "FORWARD-SIGNAL", implication: "Realty slump sale to LTRPL pending NCLT 10 months after Board approval; standalone gain/loss and segment change on completion"}
  - {id: "R-14", check: "F7", line: "190, 234, 305, 349, 387-395", classification: "FORWARD-SIGNAL", implication: "Three deferral/delay hedges plus Middle East risk; ex-E-Conv order inflow -10.6% YoY; inflow concentration in one segment and region"}
  - {id: "R-15", check: "F7", line: "884, 1259", classification: "NEUTRAL-FACT", implication: "Lumpiness hedge covers all standalone segments vs some consolidated segments; newness untestable without prior quarter"}
  - {id: "R-16", check: "F8", line: "491, 492", classification: "FORWARD-SIGNAL", implication: "Deferred credit 337.06; Q2 ETR 22.6% vs 28.0% Q1 and 25.17% statutory; 441 bps shield; deferred swing = 32% of owners PAT increase; ETR step-up risk in H2"}
  - {id: "R-17", check: "F8", line: "942, 1105", classification: "NEUTRAL-FACT", implication: "Standalone ETR 15.7% Q2 explained by intra-group dividends; ex-dividend ETR 23.9%; no earlier-years tax line"}
  - {id: "R-18", check: "F9", line: "499, 501, 945, 340", classification: "AMBIGUOUS", implication: "Q2 non-reclassifiable OCI loss (172.63) exceeds FY26 (115.88); loss despite rate rise points to plan assets or FVOCI equity; verify assumptions at AR"}
  - {id: "R-19", check: "F12", line: "380, 387-393, 815-818", classification: "AMBIGUOUS", implication: "Presentation A3 confirmed: segment EBITDA exceeds group EBITDA by about 1576 (727 a year ago); residual OI minus unallocable net = 1594.16 vs 819.04; segment results +13.1% vs EBITDA +0.6%; corporate cost step-up vs OI moved into segments"}
  - {id: "R-20", check: "F12", line: "387, 401, 795, 807, 823, 836", classification: "FORWARD-SIGNAL", implication: "I&U orders -13%, Q2 EBIT +0.7% on revenue +6.0%, H1 EBIT -3.7%, net capital +12.1% in H1 vs revenue +1.9%"}
  - {id: "R-21", check: "F12", line: "824, 825, 837, 838, 588, 727", classification: "AMBIGUOUS", implication: "Energy segments advance-funded: E-Green net (1920.87), E-Conv net (4316.38); CFO flattered now, WC reversal risk as advances burn"}
  - {id: "R-22", check: "F12", line: "826, 839, 1217, 982, 404", classification: "FORWARD-SIGNAL", implication: "M&P net capital +52.7% in H1 vs revenue +23.7%; standalone CWIP down so WC build; H1 margin 15.3% vs 15.8%"}
  - {id: "R-23", check: "F12", line: "829, 842, 532, 533, 305", classification: "FORWARD-SIGNAL", implication: "Realty assets +14.6%, liabilities +24.7% with revenue -43% and delayed launches; inventory build ahead of launches"}
  - {id: "R-24", check: "F12", line: "394, 802, 830, 843, 560, 592, 325", classification: "FORWARD-SIGNAL", implication: "DP nil revenue with assets 17142.81 (mostly LTMRHL HFS block); post-close DP is pre-revenue green energy build; trend asset accretion"}
  - {id: "R-25", check: "F14", line: "1354", classification: "NEUTRAL-FACT", implication: "Auditor letter date drafting slip in consolidated para 7; governance data point"}
  - {id: "R-26", check: "F14", line: "320-321, 516-518, 964-966", classification: "AMBIGUOUS", implication: "Metro 30-Apr economic cut-off stated only in press release; notes silent on its accounting though it drives DP nil revenue and finance cost fall"}
  - {id: "R-27", check: "F14", line: "391, 392, 395", classification: "NEUTRAL-FACT", implication: "Order inflow includes FS (= revenue) and TPS (about = revenue): 13.6% of Q2 inflow is not backlog; use E&C-only book-to-bill"}
  - {id: "R-28", check: "F15", line: "1579-1581, 1588, 1665-1667", classification: "FORWARD-SIGNAL", implication: "Data-centre cluster forming: Vyoma.AI, LTN Compute, LTA Data Centres, associate Sovcloud (partner NOT FOUND)"}
  - {id: "R-29", check: "F15", line: "1578, 1664, 748", classification: "AMBIGUOUS", implication: "International Green Scapes acquired 13-Apr-2026 with no note; CF acquisition of subsidiaries 805.30 incl contingent; price and purpose NOT FOUND"}
  - {id: "R-30", check: "F15", line: "1501, 1668, 746", classification: "NEUTRAL-FACT", implication: "Nabha Power divested 25-Jun-2026; likely most of 3830.99 consideration; gain in DP segment revenue, not exceptional"}
  - {id: "R-31", check: "F15", line: "1435, 1444, 1583-1585, 1663", classification: "NEUTRAL-FACT", implication: "Five entities in liquidation incl two Qatar entities; cleanup"}
  - {id: "R-32", check: "F15", line: "1448, 1450-1452, 1459-1462, 1575", classification: "NEUTRAL-FACT", implication: "LTIMindtree renamed LTM; L&T Sapura Shipping renamed L&T Offshore Marine (partner relationship status NOT FOUND)"}
  - {id: "R-33", check: "F17", line: "129, 152, 159, 330-355, 349", classification: "AMBIGUOUS", implication: "Watch-list silence: no Middle East split, no FY27 guidance, no NWC % of sales; 1 quarter; take to concall"}
forward_signals: ["R-01", "R-05", "R-07", "R-08", "R-11", "R-12", "R-13", "R-14", "R-16", "R-20", "R-22", "R-23", "R-24", "R-28"]
ambiguous: ["R-02", "R-03", "R-06", "R-10", "R-18", "R-19", "R-21", "R-26", "R-29", "R-33"]
commitments:
  - {commitment: "Complete LTMRHL divestment to HMRL", implied_date: "2026-12-31 (revised)", ref: "consol note (ii) line 517; standalone note (iii) line 965", status_word: "underway"}
  - {commitment: "Transfer data-centre and cloud business and LTNS stake to Vyoma.AI", implied_date: "Q3 FY27", ref: "standalone note (iv) lines 967-970", status_word: "initiated"}
  - {commitment: "Realty Undertaking slump sale to LTRPL", implied_date: "NOT FOUND (NCLT pending)", ref: "standalone note (ii) lines 959-963", status_word: "initiated"}
  - {commitment: "Hyderabad Metro results included till 30-Apr-2026 per SPA", implied_date: "2026-04-30", ref: "press release line 320", status_word: "completed"}
  - {commitment: "Nabha Power divestment", implied_date: "2026-06-25", ref: "press release lines 319-320; Annexure A line 1668", status_word: "completed"}
  - {commitment: "Offshore Wind execution", implied_date: "Q2 FY27", ref: "press release line 242", status_word: "commenced"}
  - {commitment: "Green Energy business build in Development Projects", implied_date: "NOT FOUND", ref: "press release line 325", status_word: "underway"}
  - {commitment: "Lakshya 2031 re-segmentation", implied_date: "2026-04-01", ref: "consol segment note (II) line 852; standalone line 1236", status_word: "completed"}
  - {commitment: "Liquidation of five entities", implied_date: "NOT FOUND", ref: "Annexure A legend line 1663", status_word: "underway"}
  - {commitment: "NCD proceeds use restriction, Rs 500 crore", implied_date: "continuing", ref: "Annexure III lines 1892, 1939, 1946", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "Headline PAT +33% is not core earnings. Consolidated EBITDA rose 0.6%. Other income is 71% of the PBT gain, lower finance cost 22%, and a Rs 337 cr deferred tax credit cut Q2 ETR to 22.6%. The finance-cost fall likely reflects Hyderabad Metro leaving the P&L after 30-Apr under the SPA; only the press release says so. Segment results grew 13% while group EBITDA was flat. The gap is an unallocated residual (other income minus unallocable net) that doubled to Rs 1,594 cr. This confirms the presentation A3. The filing cannot show whether corporate cost rose or other income moved into segments; that split is the key question. The H1 disposal gain (Rs 333 cr, CF line 720) bypasses exceptional items. The filing never names LTTS SWC and gives no quarter. All order-inflow growth is Energy-Conventional; excluding it, inflow fell 10.6%, with three deferral phrases. Standalone E-Conv EBIT margin fell 283 bps. Energy segments run on customer advances, so later WC reversal is a risk. F17 was applied to the operator watch list; the results-doctype default is N.A. Page 12 footing passed."
```
