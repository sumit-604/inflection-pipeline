# A3 FORENSIC NOTES: AEQUS Q2 FY27 (doctype: presentation)

Source read: A1 structured extraction (R001-R566) and A1 fulltext lines 1-1216 (layout pages plus the raw-order supplement, lines 889-1216). The source PDF and inputs/ were not opened.
Units: deck is Rs Mn throughout (fulltext lines 153, 281, 422, 1112). Rs Cr = Rs Mn x 0.1.
Ledger reconciliation: 566 of 566 ledger IDs read at their cited lines. Reconciled 100%. No orphan IDs.
Prior-quarter deck: none supplied. DROPPED_SLIDE, entity-diff and verbatim EoM diffs are not testable.

## 0. PIPELINE NOTES (A1 assignment corrections; read before using A1 rows)

| item | A1 row(s) | evidence | correction |
|---|---|---|---|
| P1 | R149, R150 (ASSIGNMENT_BY_AXIS_ORDER) | raw order line 1063-1068 "379 / 734 / 577 / Q2 FY26 Q1 FY27 Q2 FY27 / QoQ 21% / YoY 52%" | Consumer revenue Q1 FY27 = 734, Q2 FY27 = 577. A1 has them reversed. Proof: segments tie to consolidated revenue only this way (3,514 + 577 = 4,091 at line 1114; 3,222 + 734 = 3,956 vs 3,955). Under A1's order Q1 segments sum 3,799, below consolidated 3,955, which no elimination can produce. 577/379 = +52% matches "YoY 52%"; 577/734 = -21% matches "QoQ 21%". |
| P2 | R126, R129, R134, R136 (ASSIGNMENT_BY_LAYOUT) | slide 30 lines 788-795: "13% ... Domestic ... 87% ... Exports" | Exports are 87% of H1 FY27 revenue (89% H1 FY26); domestic 13% (11%). A1's slide-13 reading (exports 13%) is inverted. |
| P3 | R127, R130, R133, R135 | line 351-363 | The Q2 pies match segment shares: Consumer 577/4,091 = 14%, Aerospace 86% (Q2 FY27); 379/2,816 = 13% / 87% (Q2 FY26). This independently confirms P1. |
| P4 | R464 | lines 240-246 | A1 reads "Phase 1 commercial production starting from Q4 FY27". The layout columns read "Investment Phase 1 / Starting from Q4 FY27" (col ~89, above Q4 FY27 at col ~94). "Commercial production / Start of operations" sits at col ~150-160, above the Q3 FY28 to Q4 FY28 columns. Commercial production is not Q4 FY27. |
| P5 | R056, R057 | lines 193-198 | 9% QoQ (col ~90) sits under the order book and ties to the text "Order book grew 9% QoQ" (line 194-195). 4% QoQ (col ~127) sits under Parts Added. |
| P6 | R050, R051 | lines 184-191 | 900 bps (col ~108) sits under the Consumer column ("17%" col ~118); 800 bps (col ~84) sits under Aerospace ("69%" col ~91). Sign not printed. Lean assignment, not proven. |
| P7 | fulltext header | lines 7-8 "unit_convention: Crores ... Crores -> x1" | Wrong. The deck is Rs Mn (structured file line 4 is correct). Any stage using the fulltext header factor overstates Rs Cr by 10x. |
| P8 | R382-R390 SKU split | lines 584-601 | Category assignment uncertain, but 121+601+4,467+283+188+245+73 = 5,978 ties to the total at line 598. |

## 1. ARITHMETIC TIE-OUTS (deck internal)

- P/L Q2 FY27 (line 1114-1131): 4,091 + 106 = 4,197; costs 1,621 + 758 + 1,573 = 3,952; EBITDA 245; 245 - 465 - 206 = (426) vs (427); + 18 = (409); - 113 = (522). Ties within rounding. Q1, Q2 FY26, H1 FY27, H1 FY26 tie the same way. Q1 + Q2 = H1 on every line within 1.
- EBITDA includes other income (line 311). EBITDA ex other income: Q2 FY27 139 (3.4%), Q1 FY27 148 (3.7%), Q2 FY26 286 (10.2%), H1 FY27 287 (3.6%), H1 FY26 557 (10.4%).
- Balance sheet (line 1146-1182): 6,707 + 7,215 = 13,922 vs 13,921; total liabilities 5,248 + 8,570 = 13,818; 13,921 + 13,818 = 27,739 = total assets. Ties.
- Cash flow (line 496-517): CFO -807 + 919 + 381 - 1,302 = (809) vs (808); B = -1,597 + 101 = (1,496); C = 2,373 - 707 - 260 - 403 - 30 + 16 = 989; net (1,316); 3,015 - 1,316 + 11 = 1,710 = BS cash (line 1178). Ties.
- JV-inclusive bridge: JV revenue add-on Q2 389 / Q2 FY26 295 = +32% (matches line 307). JV EBITDA add-on 86 / 70 = +23% vs deck "20%" (line 306); within rounding bounds (85/71 = 19.7%).
- Segment sum vs consolidated EBITDA (unallocated cost): Q2 FY27 (137) = 245 - (783 - 401); Q1 FY27 (155); Q2 FY26 (110); H1 FY27 (291) vs H1 FY26 (178), +63% YoY.
- Key metrics (line 1186-1213): ROE -15 = -1,054 x 2 / 13,921 (ties). ROCE -5 = (460 - 919) x 2 / (13,921 + 5,612 + 2,752 - 1,999) = -4.5% (ties). NWC days 136 = (6,832 + 2,987 - 3,826) / (8,046 x 2) x 365 = 136 (ties exactly). Net debt/equity 0.5 reproduces only with lease liabilities in net debt (see A3-08). Fixed asset turnover 1.5 does not reproduce from slide-17 lines (PPE only 1.70; PPE + ROU 1.36); "Fixed Assets" is undefined (line 1214).

## 2. FINDINGS TABLE

| id | check | ledger row ref | line/slide | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | R349, R352, R351 | 508-511 (slide 18) | "Share issue expense (net) (30) —" ; proceeds "— 1,282" | AMBIGUOUS | Rs 30 Mn issue expense in H1 FY27 with nil equity proceeds. Either residual IPO cost or cost of the Rs 6,500 Mn warrant issue. The proceeds line should carry warrant subscription money next half; upfront % NOT FOUND in deck. |
| A3-02 | F6 | R464, R484, R482, R483 | 240-246 (slide 9) | "HOSUR INDICATIVE ROADMAP ... Investment Phase 1 ... Starting from Q4 FY27 ... Commercial production ... Start of operations" | FORWARD-SIGNAL | Q4 FY27 is the start of Phase 1 investment, not production. The commercial-production marker sits over the Q3 FY28 to Q4 FY28 columns (layout-inferred). No Hosur revenue before late FY28. The roadmap is labelled "indicative". |
| A3-03 | F6 / F16 | R469, R485, R454, R468 | 265, 167, 256 (slides 7, 10) | "Earlier guidance: Q4 FY27" ; "we are recalibrating the path to Consumer EBITDA breakeven" | FORWARD-SIGNAL | The Q4 FY27 consumer EBITDA breakeven guidance is withdrawn and no new date replaces it. The H1 FY28 group PAT breakeven (monitoring checklist) rested on it. |
| A3-04 | F6 | R457, R460, R042, R049 | 172-173, 189-192 (slides 7, 8) | "₹6,500 Mn promoter-group investment through preferential warrants ... supports the Company's next phase of capacity expansion, strategic JV investments and working capital requirements" | FORWARD-SIGNAL | Stated use of funds now includes working capital, not only capex. Tranche timing, conversion price and upfront amount NOT FOUND. |
| A3-05 | F7 | R454, R456, R464, R527 | 165-167, 240; boilerplate hits 83, 96 | "We view this as a timing-related shift" ; "recalibrating" ; "INDICATIVE ROADMAP" | AMBIGUOUS | Lexicon hits are boilerplate only ("subject to" line 83, safe harbour; "evaluating" line 96, non-GAAP). The operative hedges are off-lexicon and new on both dated items: consumer breakeven and Hosur timing. |
| A3-06 | F8 | R242-R247, R254-R258 | 1127, 1129 (slide 16) | "Total tax expense 113 86 134 248 113" against "Profit/(Loss) before tax (409) (120) (>100%) (398) (807) (54)" | FORWARD-SIGNAL | Tax charge on a pre-tax loss in every period. ETR: Q2 FY27 -27.6%, Q1 -33.7%, H1 -30.7%, H1 FY26 -209%. H1 FY27 tax = 308 bps of revenue and 23.5% of the net loss. Profitable entities pay tax; loss-entity losses carry no DTA. Group PAT breakeven needs pre-tax profit above the tax line. A DTA recognised on amalgamation would be a one-off PAT credit. No current/deferred split; cash tax sits inside the working-capital line (line 521). |
| A3-07 | F10 | R273, R274, R353, R042, R049 | 1146, 512, 189 (slides 17, 18, 8) | "Equity share capital 6,707 6,707" ; "₹6,500 Mn promoter-group investment through preferential warrants" | FORWARD-SIGNAL | Paid-up capital unchanged (ESOP exercise 16 Mn is below rounding). New dilutive instrument equal to 46.7% of Sep-26 total equity (13,921). Share count and price NOT FOUND. No EPS on the deck, so the basic/diluted spread is not testable. |
| A3-08 | F11 | R275, R276, R263, R365, R366 | 1147, 1130, 1186-1187 | "Reserves and surplus 7,215 8,149" ; "Net Debt/Equity (x) 0.2 0.5" | NEUTRAL-FACT | Net worth ties. Reserves fell 934 against the H1 loss of 1,054: +120 Mn of non-PAT credits unexplained (candidates: FCTR on US/France subsidiaries, ESOP reserve, OCI actuarial; net of 30 issue expense). Net debt/equity 0.5 reproduces only with leases: (5,612 + 2,752 - 1,999)/13,921 = 0.46; ex-leases 0.26. Definition not footnoted. |
| A3-09 | F11 | R279, R280, R287, R288, R315-R318, R333, R335 | 1151, 1156, 1178-1179, 500-501 | "Borrowings 2,809 1,002" ; "Borrowings 2,803 3,034" ; "Cash flow from operations (A) (808) 479" | FORWARD-SIGNAL | Gross borrowings 4,036 to 5,612 (+39%) in six months. Net debt incl. leases 3,442 to 6,365 (+85%). Cash + bank 3,567 to 1,999. H1 CFO (808) plus capex (1,597) = (2,405) outflow. Current borrowings + current leases 3,523 exceed cash + bank 1,999. The warrant money is the bridge; its timing is NOT FOUND. |
| A3-10 | F12 | R147-R151 | 1063-1068, 1114, 353 (slides 14, 13, 16) | "379 / 734 / 577 ... QoQ 21% ... YoY 52%" | FORWARD-SIGNAL | Consumer revenue fell 21% QoQ, 734 to 577, in Q2 FY27 (see P1 proof). Consumer share of revenue fell from 18.6% (Q1) to 14% (Q2). The ramp went backwards, not slower. |
| A3-11 | F12 | R152-R154, R047, R378 | 1069-1071, 184, 1213 | "-77 -361 -401" ; "17% Consumer Capacity Utilisation" ; Consumer ROCE "-25" | CONFIRMATORY-NEGATIVE | Consumer EBITDA (401) on revenue 577 = -69% margin (Q1 -49%). Utilisation 17%. On deck figures both falsification-line conditions are met: loss Rs 40.1 Cr wider than Rs 36.1 Cr, utilisation 17% at or below 23%. A4 owns the thesis call. |
| A3-12 | F12 | R139, R146, R145, R143, R513, R176, R178 | 1051, 1059, 1081, 1115 | "Note: EBITDA includes Other Income and excludes unallocated cost prior to inter-segment eliminations." | AMBIGUOUS | Aerospace EBITDA margin incl. OI: Q2 FY27 22.3%, Q1 22.7%, Q2 FY26 25.9%; H1 22.5% vs 24.7%. Segment OI is not split out. If all 106 Mn of Q2 OI sat in Aerospace, the ex-OI margin is 19.3%, below the 20% monitorable. Range Q2 19.3-22.3%; Q1 20.6-22.7%. Monitorable 2 cannot be cleared from the deck. |
| A3-13 | F12 | R146, R154, R208; R162, R167, R212 | 1059, 1071, 1121, 1091, 1105 | "EBITDA 245 443 (45%) 215 460 841 (45%)" | NEUTRAL-FACT | Unallocated cost (segment EBITDA sum less consolidated): Q2 FY27 137, Q1 155, Q2 FY26 110; H1 291 vs 178 (+63% YoY). Segment assets and liabilities are not on the deck; only segment ROCE (Aerospace 22, Consumer -25, line 1212-1213). |
| A3-14 | F14 | R126, R129, R428, R429, R517, R365, R366 | 353-363, 788-795, 1214 | "13% ... Domestic ... 87% ... Exports" ; "(1) Fixed Asset Turnover – Revenue from operations/Fixed Assets." | NEUTRAL-FACT | Export/domestic pies carry no per-value labels on slide 13; slide 30 fixes exports at 87%. "Fixed Assets" undefined; FAT 1.5 does not reproduce. Net-debt definition (lease-inclusive) unstated. Individually immaterial; a pattern of unlabelled or undefined metrics. |
| A3-15 | F16 | R079, R099, R176, R178, R208, R211 | 305, 988, 1115, 1121 (slide 11) | "Up 14% QoQ to ₹245 Mn, margin 6% vs 5% in Q1" | FORWARD-SIGNAL | Other income rose 67 to 106 (+39); EBITDA rose 215 to 245 (+30). EBITDA ex-OI fell 148 to 139 (-6% QoQ), margin 3.7% to 3.4%. Other income rose while cash + bank fell 3,567 to 1,999; its source is not on the deck. The "margin improvement" headline is other income. |
| A3-16 | F16 | R151, R147, R074, R065 | 1067, 305, 164-165 | "QoQ 21%" (unsigned) ; "Up 45% YoY and 3% QoQ on sustained Aerospace growth" ; "the Q2 volume ramp progressed slower than anticipated" | AMBIGUOUS | The consumer QoQ label carries no sign on a 21% fall. Slide 11 and slide 7 narrative do not state the revenue decline. Slide 10 names "Toys / Key customer transitioned" (line 267-270) and "Raw material shortages" (line 275). Which line lost the 157 Mn is not disclosed. |
| A3-17 | F16 | R369, R370, R311-R314, R291, R292, R519 | 1193, 1176-1177, 1158, 1216 | "Net Working Capital Days 151 136" ; "H1F27 ratios are annualised" | AMBIGUOUS | Days fall only through the annualised H1 revenue denominator. Absolute NWC (inventory + receivables - payables) rose 5,097 to 5,993 (+896, +18%) in six months. Inventory rose 1,158 (+20%) while Q2 revenue grew 3% QoQ. |
| A3-18 | F16 | R053, R056 | 193-197 (slide 8) | "238 ... Aerospace Parts Added in Q2 FY27 ... 4% QoQ" | AMBIGUOUS | 4% QoQ implies about 229 parts in Q1. The monitoring record has 86 in Q1 FY27 and 433 in Q4 FY26. Either the metric definition changed (cumulative or different scope) or the label is misplaced (R056 ASSIGNMENT_UNRESOLVED). |
| A3-19 | F16 | R515, R512 | 1132-1133, 1034-1037 | "consumer electronics costs are now being expensed following the commencement of commercial operations, compared with the pre-operative phase in FY26" | AMBIGUOUS | FY26 margins (16%) carried capitalised pre-operative consumer cost; the YoY base is not like-for-like. Amount capitalised NOT FOUND. The same treatment can recur during the Hosur build [inference]. |
| A3-20 | F16 | R050, R051, R503 | 190-191, 208 | "900 bps YoY ... 800 bps YoY" ; "Note: Capacity utilisation includes subsidiaries and JVs" | AMBIGUOUS | YoY utilisation changes are unsigned. Layout places 900 bps under Consumer. Lean bear: Consumer down about 9 pp YoY to 17%. The basis includes subsidiaries and JVs; comparability with the 22% Q1 record is unverifiable without the prior deck. |
| A3-21 | F17 | monitoring checklist items 2, 6, 7; tracker items | 1129, 396, 204, 182 (absence points) | see Section 5 table | CONFIRMATORY-NEGATIVE | The deck (dated 26-Oct, line 19) is silent on the S.233 amalgamation rejection (14-Oct), DTA, pledge, the Cookware JV receivable, the Safran award value and the FY27 capex and utilisation targets. Silence count is 1 deck (prior deck not supplied). |
| A3-22 | F6 | R461, R544, R453, R052, R055 | 174, 198-202, 222, 193-195 | "Following quarter-end, new Safran agreements expanded our relationships to six entities." ; "Safran landing gear contract won" | AMBIGUOUS | The order book of USD 1,096 Mn (+9% QoQ from the USD 1,004 Mn record) is at quarter-end. The deck does not say whether it includes the post-quarter Safran agreements or the landing-gear contract. Values of the Safran wheels and landing-gear awards NOT FOUND. |

## 3. CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 | FINDING | 2 ZERO_STANDING rows (R349, R352); Rs 30 Mn issue expense with nil proceeds (A3-01). |
| F2 | N.A. | Deck carries consolidated figures only; no standalone column. The JV-inclusive bridge ties (Section 1). |
| F3 | N.A. | No standalone cost lines to compare. |
| F4 | N.A. | No auditor letter or Other Matters paragraph in a deck; financials marked "Un-audited" (line 37). |
| F5 | N.A. | No EoM or going-concern paragraph; no prior deck. |
| F6 | FINDING | Hosur phase dates, withdrawn consumer breakeven date, warrant use, Safran scope (A3-02, 03, 04, 22); GoK MoU added in loop 1 (P-A3-23). |
| F7 | FINDING | Off-lexicon hedges on both dated items (A3-05). |
| F8 | FINDING | Tax charge on pre-tax losses every period; negative ETR (A3-06). |
| F9 | N.A. | Deck carries no OCI line; the +120 Mn reserve gap is logged under F11. |
| F10 | FINDING | Paid-up flat; Rs 6,500 Mn warrants as new dilutive instrument; no EPS (A3-07). |
| F11 | FINDING | Net worth ties; +120 Mn reserve walk gap; lease-inclusive net debt; leverage near-doubling (A3-08, A3-09). |
| F12 | FINDING | Consumer revenue fell 21% QoQ; consumer margin -69%; aerospace ex-OI margin unprovable; unallocated cost +63% (A3-10 to A3-13); customer concentration added in loop 1 (P-A3-24). |
| F13 | N.A. | No board-outcome document in a deck; board slide gives no term dates. CFO item handled under F17. |
| F14 | FINDING | Unlabelled pies, undefined FAT and net-debt bases (A3-14). |
| F15 | N.A. | No prior-quarter entity list supplied; JV basis named (API, SQuAD, ACPL 50%; Ajna 33%, line 182). |
| F16 | FINDING | Other-income-driven EBITDA headline, unsigned consumer decline, NWC days via denominator, parts-added definition, comparability base, unsigned utilisation (A3-15 to A3-20). |
| F17 | FINDING | Run against the deck at orchestrator request (checklist supplied); 9 items silent (A3-21, Section 5). |

Counts: PASS 0 | FINDING 11 | N.A. 6 | blank 0. Loop 1 adds two findings under F6 and F12; no check status changes.

## 4. COMMITMENT REGISTER (F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| Hosur ground-breaking; Safran landing-gear contract won | Q2 FY27 ("Current quarter") | line 240-243, 222 (R464, R544) | completed (contract won); ground-breaking initiated |
| Hosur Investment Phase 1 | starting Q4 FY27 | line 240-246 (R464, R484) | initiated (indicative) |
| Hosur commercial production / start of operations | Q3-Q4 FY28 columns (layout-inferred); timeline to FY29 | line 240-246 (R465) | not started (indicative) |
| Hosur end objective: second integrated ecosystem, ingot to aero engine and landing gear | undated | line 248 (R466) | under development (line 214) |
| Consumer EBITDA breakeven | was Q4 FY27; now "being recalibrated", no date | line 265, 167, 256 (R469, R485) | withdrawn |
| Consumer capex deployment | recalibrated, no amount or date | line 262-263 (R472) | under review |
| Rs 6,500 Mn promoter warrants: capacity expansion incl. Hosur, JV investments, working capital | tranche dates NOT FOUND | line 172-173, 189-192 (R457, R460) | initiated (EGM approval 22-Oct per tracker) |
| New Safran long-term supply agreements, six entities | signed after 30-Sep-2026 | line 174, 198-202 (R461) | completed |
| Safran A320 wheels agreement, tenure over 15 years | deliveries FY28 per spear record; deck undated | line 159-160, 195-196 (R453) | completed (signed) |
| MoU with GoK for Rs 28,560 Mn investment | MoU signed in the 2026 timeline column (layout-inferred); investment period NOT FOUND | line 560-562 (R473, R379) | MoU signed; investment not started (see P-A3-23) |
| MoU with TN Govt for aero-engine ecosystem | Feb 2026 | line 220, 556-558 (R474, R481) | completed (MoU) |
| Near-term focus: improve consumer utilisation | undated | line 168-169, 269-273 (R455, R471) | ongoing |

## 5. WHAT WAS NOT DISCUSSED (F17 silence audit against the deck)

Silence count: 1 = this deck; prior deck not supplied, so consecutive-quarter counts start here.

| checklist / tracker item | deck coverage | ref | quarters silent |
|---|---|---|---|
| M1 Consumer utilisation vs 40-50% FY27 exit target | 17% shown; target not restated | line 184 | target: 1 |
| M2 Aerospace margin ex other income | NOT DISCLOSED; segment EBITDA includes OI | line 396 | 1 |
| M3 Consumer capex commissioning | "Recalibrating ... Capex deployment", no amount | line 260-263 | partial |
| M4 New aerospace part numbers | 238 shown; definition conflict | line 193-197 | addressed (A3-18) |
| M5 Operating cash vs capex | CFO (808) vs capex (1,597) H1; derived Q2 using checklist Q1: CFO (394), capex 767 | line 500-501 | addressed; negative |
| M6 DTA on merged-entity losses | silent; tax 248 on loss | line 1129 | 1 |
| M7 CFO seat / KMP / CARO | CFO named; KMP filing and CARO not in deck | line 204, 822-828 | partial |
| Falsification line | data present (Rs 40.1 Cr loss, 17%); not framed | line 1071, 184 | met on deck figures |
| Pledge tripwire | silent | n/a (no slide) | 1 |
| Safran award value | tenure stated; value silent | line 159-160 | 1 |
| Amalgamation route (S.233 rejected 14-Oct) | silent in a deck dated 26-Oct | line 19 | 1 |
| Institutional holding / IPO lock-in (about Dec-2026) | silent | n/a | 1 |
| Cookware JV Rs 30.05 Cr receivable at 12% | silent; ACPL still in JV basis | line 182, 661 | 1 |
| FY27 capex plan (about Rs 660 Cr, Rs 500 Cr consumer) | not restated; H1 capex Rs 159.7 Cr | line 172, 501 | 1 |

## 6. NOTES FOR A4 (questions to raise)

From A3-01, 03, 04, 05, 06, 09, 10, 12, 15, 16, 17, 18, 19, 20, 22: the new consumer breakeven date; which customer or line lost the 157 Mn of consumer revenue; the source of the 106 Mn other income and its segment split; aerospace margin ex OI; whether the amalgamation route permits use of losses and DTA; warrant tranche timing and upfront amount; whether the order book includes post-quarter Safran agreements; the parts-added definition; pre-operative cost capitalised in FY26; the sign of the utilisation YoY changes.

## LOOP 1 ADDITIONS (A5 M1, M2)

Correction loop 1. A5 named R379 / R473 and R418 as rows read but not carried into a finding. Both rows were re-read at their fulltext lines. Existing findings A3-01 to A3-22 are unchanged.

| id | check | ledger row ref | line/slide | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| P-A3-23 | F6 | R379, R473, R550, R490 | 560-562, 564 (slide 21) | "▪ Entered into MoU with GoK for investment of ₹28,560 Mn." | AMBIGUOUS | See note M1 below. A headline investment of Rs 2,856 Cr with no period, entity, site, phasing or funding source on the deck. It equals 2.05x Sep-26 total equity (13,921), 4.4x the Rs 6,500 Mn warrants and 17.9x H1 FY27 capex (1,597). No funding source on the deck covers it. |
| P-A3-24 | F12 | R418, R416, R417, R381, R396, R545 | 775-778 (slide 30) | "63% ... Top 5 customer group contribution (H1 FY27)" | AMBIGUOUS | See note M2 below. Five customer groups give 63% of H1 FY27 revenue. The deck gives no segment split, no largest-customer share and no comparative period, so the concentration trend and its segment location are unknown. |

### M1 note: P-A3-23, GoK MoU (R379 / R473)

What the deck says:
- The MoU is with the Government of Karnataka. The stated investment is Rs 28,560 Mn (Rs 2,856 Cr) (line 560-562).
- It sits in the top row of the slide-21 timeline, in the column with the TN aero-engine MoU (line 555-558). Slide 9 dates the TN MoU to Feb 2026 (line 220), so the GoK MoU falls in the 2026 column (line 564). This placement is layout-inferred.
- The slide also says "We operate in 3 unique ... ECOSYSTEMS in India" (line 576). The Karnataka clusters named in the deck are Belagavi, Koppal and Hubballi (line 717-737).

What the deck does not say (NOT FOUND):
- The MoU date, or the period over which the Rs 28,560 Mn is to be spent.
- Which entity invests: Aequs Limited, a subsidiary, JV partners, or third parties in the ecosystem. Slide 9 says Hosur capabilities are "to be added by Aequs and/or JV partners" (line 238). The GoK MoU carries no such statement either way.
- The cluster or site, the segment (aerospace or consumer), and any phasing.
- The funding: equity, debt or state incentives.
- Whether the MoU is binding, and any linked state incentive or land terms.

How it bears on funding versus capex:
- H1 FY27 operating cash flow was (808) and capex was (1,597), an outflow of 2,405 Mn (line 500-501). Lease-inclusive net debt rose from 3,442 to 6,365 Mn (A3-09).
- The only new funding named on the deck is the Rs 6,500 Mn warrants. They are earmarked for "capacity expansion, strategic JV investments and working capital requirements", "including Hosur" (line 172-173, 189-192). The GoK MoU is not named as a use.
- If Aequs funds a material share of Rs 28,560 Mn itself, it needs capital beyond the warrants: new debt or new equity. That conflicts with the "recalibrating ... Capex deployment" stance on consumer (line 262-263) [inference].
- If partners or the state fund most of it, the figure is an ecosystem headline, not Aequs capex. Read conservatively, it is an unfunded intent until the deck states phasing and source.
- Separating observation: a phased capex schedule for the MoU that names the investing entity and the funding source.

Management questions (A4):
1. When was the GoK MoU signed, and over how many years does the Rs 28,560 Mn run?
2. How much of it is Aequs Limited's own capex, and how much is JV-partner, third-party or state money?
3. Which cluster and which segment does it fund, and does any of it sit in the FY27 capex plan?
4. What funds the Aequs share beyond the Rs 6,500 Mn warrants, which are already earmarked for Hosur, JVs and working capital?

### M2 note: P-A3-24, top-5 customer concentration (R418)

What the deck says:
- Top 5 customer groups gave 63% of H1 FY27 revenue (line 775-777).
- The same slide gives 15 total OEM customer groups globally and a 15-year average tenure for the 3 largest groups (line 775-777).
- Aerospace is 84% of H1 FY27 revenue and Consumer 16% (line 584, 639).
- The aerospace roster is Airbus, Boeing, Safran, Collins, Mubea, Bombardier, GKN Aero, Honeywell and Eaton (line 784-790). The consumer roster is one unnamed large consumer electronics player, Tramontina and Wonderchef on slide 30 (line 792-794), plus Mattel on slide 24 (line 659).

What the deck does not say (NOT FOUND):
- How the five groups split between Aerospace and Consumer.
- The largest single customer's share.
- A comparable figure for H1 FY26 or FY26, so the trend cannot be tested.
- Whether the "15 OEM customer groups" count covers Consumer.
- Whether "customer group" consolidates related entities. Safran alone is now six entities (line 198-199). A group count therefore understates entity breadth, and the 63% understates exposure to a single group's procurement decisions.

What it means for concentration across segments [inference, bounded]:
- If all five groups are aerospace OEMs, they hold 63/84 = 75% of aerospace revenue. Aerospace then rests on five groups.
- If the unnamed consumer electronics player is in the top five, Consumer is concentrated too. One customer would then carry much of the 16% consumer slice.
- Slide 10 records a Toys key-customer transition (line 267-270) in the quarter when consumer revenue fell 21% QoQ (A3-10). Customer concentration in Consumer has already shown up in a reported number.
- Read conservatively: 63% across five groups means one programme slip or one customer transition moves group revenue by high single digits or more. The Safran expansion raises dependence on one group at the same time as it lengthens tenure.

Management questions (A4):
1. How do the top 5 customer groups split between Aerospace and Consumer, and what share does the largest single group hold?
2. What was the top-5 share in H1 FY26 and FY26?
3. Is the unnamed consumer electronics customer in the top five? What share of Consumer revenue did it give in Q2 FY27 against Q1 FY27?
4. Was the Toys key customer that transitioned (line 267-270) a top-5 group?

```yaml
stage: A3-forensics
company: "AEQUS"
quarter: "q2fy27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/aequs-q2fy27/work/forensics_presentation_aequs_q2fy27.md"
ledger_reconciled_pct: 100
correction_loop: 1                # A5 MISSING M1 (R379/R473), M2 (R418) added as P-A3-23, P-A3-24
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: N.A.
  F10: FINDING
  F11: FINDING
  F12: FINDING
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: FINDING
counts: {PASS: 0, FINDING: 11, NA: 6, blank: 0, findings_total: 24, forward_signal: 8, ambiguous: 11, confirmatory_negative: 2, neutral_fact: 3}
findings:
  - {id: "A3-01", check: "F1", line: "508-511", classification: "AMBIGUOUS", implication: "Rs 30 Mn share issue expense with nil proceeds; IPO residue or warrant cost; warrant money should appear next half"}
  - {id: "A3-02", check: "F6", line: "240-246", classification: "FORWARD-SIGNAL", implication: "Hosur Q4 FY27 is Phase 1 investment start; commercial production marker sits at Q3-Q4 FY28 (layout); A1 R464 misreads"}
  - {id: "A3-03", check: "F6", line: "265, 167", classification: "FORWARD-SIGNAL", implication: "Q4 FY27 consumer EBITDA breakeven guidance withdrawn with no replacement date"}
  - {id: "A3-04", check: "F6", line: "189-192", classification: "FORWARD-SIGNAL", implication: "Rs 6,500 Mn warrant use includes working capital; tranche timing NOT FOUND"}
  - {id: "A3-05", check: "F7", line: "165-167, 240", classification: "AMBIGUOUS", implication: "off-lexicon hedges (recalibrating, indicative) now on both dated items"}
  - {id: "A3-06", check: "F8", line: "1127, 1129", classification: "FORWARD-SIGNAL", implication: "tax 248 Mn on H1 pre-tax loss 807 Mn (ETR -30.7%, 308 bps of revenue); DTA on amalgamation would be a one-off PAT credit"}
  - {id: "A3-07", check: "F10", line: "1146, 189", classification: "FORWARD-SIGNAL", implication: "paid-up flat at 6,707; warrants equal 46.7% of equity; price and share count NOT FOUND"}
  - {id: "A3-08", check: "F11", line: "1147, 1186-1187", classification: "NEUTRAL-FACT", implication: "net worth ties; +120 Mn non-PAT reserve credit unexplained; net debt/equity 0.5 only with leases"}
  - {id: "A3-09", check: "F11", line: "1151, 1156, 1178-1179, 500-501", classification: "FORWARD-SIGNAL", implication: "net debt incl leases 3,442 to 6,365 Mn (+85%) in six months; H1 CFO plus capex outflow 2,405 Mn; warrants are the bridge"}
  - {id: "A3-10", check: "F12", line: "1063-1068, 1114, 353", classification: "FORWARD-SIGNAL", implication: "consumer revenue fell 21% QoQ (734 to 577); A1 R149/R150 reversed; proven by segment-to-consolidated tie"}
  - {id: "A3-11", check: "F12", line: "1069-1071, 184", classification: "CONFIRMATORY-NEGATIVE", implication: "consumer EBITDA (401) Mn, margin -69%, utilisation 17%; both falsification-line conditions met on deck figures"}
  - {id: "A3-12", check: "F12", line: "1059, 1081, 1115", classification: "AMBIGUOUS", implication: "aerospace margin incl OI 22.3%; ex-OI range 19.3-22.3%; 20% monitorable not provable"}
  - {id: "A3-13", check: "F12", line: "1059, 1071, 1121", classification: "NEUTRAL-FACT", implication: "unallocated cost H1 291 vs 178 Mn (+63%); no segment assets or liabilities on deck"}
  - {id: "A3-14", check: "F14", line: "353-363, 788-795, 1214", classification: "NEUTRAL-FACT", implication: "unlabelled pies (exports actually 87%); FAT and net-debt bases undefined"}
  - {id: "A3-15", check: "F16", line: "305, 1115, 1121", classification: "FORWARD-SIGNAL", implication: "EBITDA +14% QoQ is all other income; ex-OI EBITDA fell 148 to 139 Mn, margin 3.7% to 3.4%"}
  - {id: "A3-16", check: "F16", line: "1067, 305, 164-165", classification: "AMBIGUOUS", implication: "unsigned QoQ 21% on a consumer revenue fall; narrative says slower ramp; Toys key customer transitioned"}
  - {id: "A3-17", check: "F16", line: "1193, 1176-1177, 1216", classification: "AMBIGUOUS", implication: "NWC days 151 to 136 via annualised denominator; absolute NWC +896 Mn (+18%), inventory +1,158 Mn"}
  - {id: "A3-18", check: "F16", line: "193-197", classification: "AMBIGUOUS", implication: "238 parts with 4% QoQ implies Q1 about 229 vs record 86; definition change or misplaced label"}
  - {id: "A3-19", check: "F16", line: "1132-1133", classification: "AMBIGUOUS", implication: "FY26 base carried capitalised pre-operative consumer cost; amount NOT FOUND; may recur at Hosur"}
  - {id: "A3-20", check: "F16", line: "190-191, 208", classification: "AMBIGUOUS", implication: "unsigned utilisation YoY; lean bear consumer down about 9 pp; basis includes subs and JVs"}
  - {id: "A3-21", check: "F17", line: "19, 1129, 396, 182", classification: "CONFIRMATORY-NEGATIVE", implication: "deck silent on S.233 rejection, DTA, pledge, Cookware receivable, Safran value, FY27 capex and utilisation targets"}
  - {id: "A3-22", check: "F6", line: "174, 198-202, 222", classification: "AMBIGUOUS", implication: "order book USD 1,096 Mn (+9% QoQ) may exclude post-quarter Safran agreements; award values NOT FOUND"}
  - {id: "P-A3-23", check: "F6", line: "560-562, 564", classification: "AMBIGUOUS", implication: "GoK MoU Rs 28,560 Mn (2.05x equity, 4.4x warrants, 17.9x H1 capex); period, entity, site, phasing and funding NOT FOUND; unfunded intent on deck evidence"}
  - {id: "P-A3-24", check: "F12", line: "775-778", classification: "AMBIGUOUS", implication: "top 5 customer groups 63% of H1 FY27 revenue; segment split, largest customer and prior period NOT FOUND; if all aerospace, 75% of aerospace revenue"}
forward_signals: ["A3-02", "A3-03", "A3-04", "A3-06", "A3-07", "A3-09", "A3-10", "A3-15"]
ambiguous: ["A3-01", "A3-05", "A3-12", "A3-16", "A3-17", "A3-18", "A3-19", "A3-20", "A3-22", "P-A3-23", "P-A3-24"]
commitments:
  - {commitment: "Hosur ground-breaking; Safran landing-gear contract won", implied_date: "Q2 FY27", ref: "line 240-243, 222", status_word: "completed"}
  - {commitment: "Hosur Investment Phase 1", implied_date: "from Q4 FY27 (indicative)", ref: "line 240-246", status_word: "initiated"}
  - {commitment: "Hosur commercial production / start of operations", implied_date: "Q3-Q4 FY28 columns, timeline to FY29 (layout-inferred)", ref: "line 240-246", status_word: "initiated"}
  - {commitment: "Consumer EBITDA breakeven", implied_date: "was Q4 FY27; no new date", ref: "line 265, 167", status_word: "withdrawn"}
  - {commitment: "Consumer capex deployment recalibration", implied_date: "NOT FOUND", ref: "line 262-263", status_word: "underway"}
  - {commitment: "Rs 6,500 Mn promoter warrants for expansion, JV investments, working capital", implied_date: "tranches NOT FOUND", ref: "line 172-173, 189-192", status_word: "initiated"}
  - {commitment: "New Safran long-term supply agreements, six entities", implied_date: "post 30-Sep-2026", ref: "line 174, 198-202", status_word: "completed"}
  - {commitment: "MoU with GoK for Rs 28,560 Mn investment", implied_date: "MoU in 2026 column (layout); investment period NOT FOUND", ref: "line 560-562, 564", status_word: "initiated"}
gate_a3: pass
blank_checks: []
analyst_note: "Three things change the read. First, A1 reversed consumer revenue: Q2 FY27 is 577 Mn, down 21% QoQ from 734. The proof is arithmetic: only that order ties segments to consolidated revenue, and it matches the printed YoY 52% and the 14% Q2 pie. The deck prints the QoQ label unsigned and calls it a slower ramp. Second, the EBITDA headline (+14% QoQ) is entirely other income; core EBITDA fell to 139 Mn (3.4%). Other income rose while cash halved, so its source matters, and the aerospace ex-OI margin may sit under 20%. Third, cash: H1 CFO (808) with capex (1,597) took lease-inclusive net debt from 3,442 to 6,365 Mn, current debt exceeds cash, and the warrant money is the bridge with no stated timing. The GoK MoU (Rs 28,560 Mn) has no funding source on the deck. The consumer breakeven date is withdrawn. Tax is charged on losses every quarter. Both falsification-line conditions are met on deck figures; A4 owns that call. A1 fulltext header says Crores; the deck is Rs Mn."
```
