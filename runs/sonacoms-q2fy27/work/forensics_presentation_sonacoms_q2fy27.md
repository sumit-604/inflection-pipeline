# A3 FORENSIC NOTES: SONACOMS Q2 FY27, doctype PRESENTATION (36-slide earnings deck, 26-Oct-2026)

Agent: A3 forensics | model claude-opus-5-5 | run date 2026-10-28 | revised loop 1 (A5 M1): section 7 added, YAML updated
Inputs read: A1 structured (R001-R317, all 317 rows), A1 fulltext (all 848 lines), A2 ledger (317 IDs, plus M01-M15 in loop 1), Notion COMPANIES MASTER page saved 28-Oct-2026 (operator memory, weighed, never anchored evidence). Prior-quarter fulltext: NOT AVAILABLE. Source PDF and inputs/: not opened.
Line numbers below are A1 fulltext line numbers. "[MEMORY]" marks a comparison drawn from the Notion page, not from this corpus. "[INFERENCE]" marks my reasoning, not a filed statement.

## 1. LEDGER RECONCILIATION

- Rows in A2 ledger: 317 (loop 1: 332 with M01-M15). Rows read in the structured file and checked at their fulltext line: 317 (loop 1: 332). Reconciled: 100%.
- Line cites spot-verified on every slide that carries rows; no wrong line cite found that changes a value.

A2 points resolved:

| A2 point | Resolution |
|---|---|
| R051 = 71 vs bracket R052 "(20+20+31)+4" | No inconsistency. 20+20+31 = 71 (L174). The "+4" is the Q2 net add that takes 71 to 75; Q2 bracket 21+23+31 = 75 (L174). A2's "sums to 75" read the +4 into the Q1 bracket. |
| R104 = 13 "number of programs or page ref" | Page footer. Deck prints slide N's page number as N-1 (p13 shows "12" at L242; p14 shows "13" at L263). R104 is not a program count. |
| p22 cash bridge "cannot be tied out" | It ties to the rupee. 12,690 + 5,935 - 1,479 + 2,509 = 19,655 (L446-448). CFO: 6,588 + 440 - 1,093 = 5,935 (L455-458). FCFO 5,935 - 1,479 = 4,456 (L442). Others: (1,120) + 2,236 + 1,076 + 317 = 2,509 (L454-460). R182 = the Others total. R187-R190 map by top-to-bottom order to Dividend / Borrowings / ESOPs / Interest income and others (L453-456); [MEMORY] corroborates three of four (dividend Rs 1.80 x ~622 mn shares = ~1,120; ESOP cash Rs 107.6 Cr; ST borrowings Rs 234 to 462 Cr). |
| ROCE/ROE scope drift p7 / p23 / p28 | Confirmed. Finding P-A3-F14-01. |
| Slides 8, 9, 12, 15, 17, 19, 25 NO_ROWS | Confirmed: dividers, tab bars, photo captions only. |
| R109 / R110 LABEL_UNMAPPED pies | Sum test: R109 values sum to 149 and R110 to 229; two pies each need 100. Moving the "51%" at L291 from R110 to the H1 FY27 geography pie (10+14+25+51 = 100) and adding the unrowed "22%" at L291 to the product pies makes R110 sum to 200. [INFERENCE] One geography segment reads 51% in FY26 and H1 FY27. Labels are still not recoverable. |

A1 completeness defects (fulltext numbers with no structured row; for orchestrator, not a gate on A3). Loop 1: A2 has now ledgered them as M01-M15 (section 7).
- L291 "22%" (p16 pie value).
- p26 Phase 4 and the right-hand series: L505-507 "Acquisition of NOVELIC and Railway Business", "12 plants", "34 products"; L510 "57,136 H1FY27 (Ann.)"; L512-515 "FY22-H1FY27 Ann. Avg. EBITDA margin 25.1%", "Revenue CAGR 24.1%"; L516-523 44,752 / 35,545 / 31,866 / 26,756 / 21,306 / 28,568 H1FY27.
- By count (28 values for FY99-FY26), R238 10,380 = FY20 and R239 15,663 = FY21 [INFERENCE]. CAGR checks then tie: FY21 15,663 to H1 FY27 ann. 57,136 over 6 years = 24.1%; FY16 3,653 to FY21 15,663 over 5 years = 33.8%; FY11 2,207 to FY16 3,653 = 10.6%; FY21 to FY26 44,752 = 23.4% ("23%", L583).

## 2. FINDINGS TABLE

| id | check | ledger row | line / slide | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| P-A3-F6-01 | F6 | R073-R076 | L201-209, s11 | "₹12,500 mn ... addition in our orderbook ... H2 FY27 Start of Production" | FORWARD-SIGNAL | Nearest-dated SOP in the deck. Extra volumes in two existing E2W/E3W traction-motor programs. First delivery test in Q3/Q4 FY27 results. |
| P-A3-F6-02 | F6 | R063-R072, R081-R090 | L205, L238, s11/s13 | "H1 FY29 ... Start of Production" | FORWARD-SIGNAL | SOP ladder for Q2 itemised wins (Rs 31.2 bn): H2 FY27 12.5; H1 FY28 5.8; H2 FY28 2.6; H1 FY29 10.3. Rs 18.7 bn (60%) starts production in FY28-FY29. Most of the Q2 wins add no revenue for 2-3 years. |
| P-A3-F6-03 | F6 | R063, R067, R125-R127 | L341-342, L366-367, L372 vs L205 | "Product commercialized in Q2FY27" / "Rear Radar Sensor" / "H2 FY28 Start of Production" | AMBIGUOUS | "Commercialized" means first order won, not production. LSD SOP is H1 FY29 and rear radar SOP is H2 FY28. The 26-Oct Notion entry scored promise C3 (ADAS radar) "partly delivered". On the deck, radar revenue starts H2 FY28. C3 scoring needs a definition ruling. |
| P-A3-F6-04 | F6 | R100, R106, R107, R117-R118 | L257, L267, L305 | "to be executed largely within next 12 months" / "₹9 bn (4%)" / "Non-Automotive 31% 29%" | FORWARD-SIGNAL | Railway book Rs 9 bn covers about 0.8 year of railway revenue at the FY26 run-rate [MEMORY: Rs 973 Cr in 10 months; my arithmetic]. Non-automotive share fell 31% to 29%. Railway revenue past about Sep-2027 depends on fresh POs. Tripwire 8. |
| P-A3-F6-05 | F6 | R310-R317 | L753, L792, L798, L826 | "*Product under development" | NEUTRAL-FACT | Traction motor (PV/CV), park gear controller, AGV/AMR drive unit, robot gearbox, eVTOL motor/gearbox, frameless motors stay undated. Hub Wheel Motor carries no asterisk (L798). [INFERENCE + MEMORY] the Q1 deck's H2 FY26 hub-wheel SOP reads as completed. |
| P-A3-F7-01 | F7 | R105, R108 | L263-266, s14 | "We have also applied a discount to accommodate any unforeseen delays or changes in program launches that may happen in the future" | AMBIGUOUS | The size of the delay discount and EOL haircut is undisclosed over a 10-year horizon. Persists from Q1 [MEMORY: N11]. Rs 251 bn cannot be compared with gross order value or with peers. |
| P-A3-F10-01 | F10 | R188-R190, R192 | L453-458, s22 | "ESOPs" / "1,076" | NEUTRAL-FACT | H1 ESOP cash inflow of about Rs 1,076 mn (positional mapping). The deck carries no share count or EPS. A4 should cross-check against Notion allotments and the MD PSP grant of 1,70,747 shares [MEMORY]. |
| P-A3-F14-01 | F14 | R042-R046, R196-R201, R213-R215, R219, R244, R246 | L150-152 vs L485-488 vs L603 | p7: "capital deployed for acquiring NOVELIC)"; p23: "NOVELIC and Railway Business)" ... "LTM PAT is adjusted for one-time impact of ₹301 mn" | AMBIGUOUS | Same 16.4% ROCE and 13.9% ROE (L144 = L469) appear under two different definitions, so at least one footnote is mis-stated. ROE adds back Rs 301 mn of labour-code charge. ROCE is normalised by annualising railway (L492). p28 adds a third ROE basis (20%, 5-year). Un-normalised, un-adjusted ROCE and ROE against the 18% trigger: NOT FOUND in the deck. |
| P-A3-F14-02 | F14 | R078, R080, R084, R088 | L220-221 vs L234, s13 | "adding ₹6.6 billion in orderbook this quarter" vs "₹3,300 mn ... ₹1,600 mn ... ₹2,000 mn" | NEUTRAL-FACT | Tiles sum to Rs 6.9 bn against a Rs 6.6 bn heading. The Rs 0.3 bn gap feeds the bridge question in P-A3-F16-03. |
| P-A3-F14-03 | F14 | R135-R145, R151, R159-R169, R175 | L388-397, L415-429, L406 | "PAT margin percentage calculated from PAT including non-controlling interest" / "14.9%" / "lower by ~0.5%" | AMBIGUOUS | The headline PAT and the margin PAT are on different bases. 1,728 / 11,435 = 15.1%, but the slide prints 14.9%. 2,975 / 19,944 = 14.9%, but the slide prints 14.6%. On the headline-PAT basis, the margin decline is about 0.7 pp in Q2 and 0.8 pp in H1, not "~0.5%". The H1 EBITDA margin decline computes to 1.6 pp (24.65% to 23.06%), not "~1.5%". Each stated decline understates the arithmetic. |
| P-A3-F14-04 | F14 | R032, R044-R046 | L140-152; L35 | "PAT1 ... PAT Margin2 ... RoCE3 ... RoE4" vs notes "2. ROCE ... 1. PAT margin ... 3. ROE" | NEUTRAL-FACT | On p7 the footnote markers do not match the notes, and RoE4 has no note at all. No deck slide labels its numbers consolidated or standalone; only the cover letter (L35) names both. These are small drafting slips, but they add to the Q1 QC pattern [MEMORY: PR-FD4/FD5]. |
| P-A3-F16-01 | F16 | R021, R027, R150, R174 | L404, L438 vs L119-134 | "Revenue includes net gain from foreign exchange" | AMBIGUOUS | The forex qualifier appears on p20/p21 but not on the p6/p7 highlight slides, which carry the same 15,464 and 23.0%. The deck does not give the forex amount. On the deck basis the margin clears the 23.0% bear line by 4 bps. Ex-forex it is 22.5% [MEMORY: forex Rs 10.6 Cr]. This is the same issue as Q1 P-A3-F16-04, so it is a second quarter. The gate result depends on the forex ruling. |
| P-A3-F16-02 | F16 | R091, R097-R100 | L257-258, s14 | "Automotive EV ... ₹152 billion (61%)" | CONFIRMATORY-NEGATIVE | The EV share of the order book eased for a third straight print: about 70% (FY26) to 64% (Q1) [MEMORY] to 61%. In Q2 the EV book fell slightly while about Rs 24 bn of EV orders were added. Tripwire 9. |
| P-A3-F16-03 | F16 | R062-R074, R078-R088, R093-R100 | L248-252, L201-203, L234, L257 | "Orders consumed from matured and ramp-up programs during Q2 FY27" / "25 bn" / "36 bn" | AMBIGUOUS | (a) Itemised adds are 24.3 + 6.9 = Rs 31.2 bn against 36 bn added, so Rs 4.8 bn (13%) is unitemised. (b) The robotics book is Rs 13 bn (5%) against about 3% at Q1 [MEMORY], yet the deck itemises no robotics win. (c) The 25 bn consumed is 1.6x Q2 revenue of 15,464 mn, against about 1.15x in Q1 [MEMORY]. The "consumed" bucket mixes realised revenue, matured drop-outs and, possibly, EOL or volume re-estimates. Leaning bear, part of it may be write-down. |
| P-A3-F16-04 | F16 | R061-R074, R115-R116 | L190-203, L297 | "Indian OEM of ICE and EV 2Ws and 3Ws ... ₹12,500 mn" / "₹3,800 mn" | FORWARD-SIGNAL | Rs 16.3 bn (45% of the 36 bn added) is 2W/3W traction motors and IMC from existing Indian OEM customer(s). The E2W/E3W revenue share rose from 10% to 14%. That concentration is rising. [MEMORY + INFERENCE] The EV-motors and controllers business is being slump-sold into eDrive, where DENSO takes 49%. The deck does not say which entity books these orders. |
| P-A3-F16-05 | F16 | R289-R309 | L700, L703, L718 | "CY24 8.8%  CY25 8.7%" / "CY24 4.4%   CY25 4.2%" / "As per CRISIL report dated Feb 2021" | CONFIRMATORY-NEGATIVE | CY25 is the first dip in the diff-gear share series. Starter-motor share is below its CY21 peak of 4.6%. The India dominance claim still rests on a 2021 source, the same as Q1 [MEMORY: P-A3-F16-01]. |
| P-A3-F16-06 | F16 | R193-R195, R212, R148 | L467, L484, L398-400 | "5.8 4.9 4.7" / "Material margin / (Employee cost + Manpower cost on hiring)" / "positive impact of operating leverage" | CONFIRMATORY-NEGATIVE | Value added per unit of employee cost keeps falling, Mar-25 to Sep-26. The deck claims operating leverage, yet material margin falls faster than labour cost. That fits a structural input-cost and mix drag more than a lag in pass-through. |
| P-A3-F16-07 | F16 | R242-R246 (loop 1: + M07, M08) | L589-593, L605 vs L512-513, L142 | "26% Margins 5-year Avg. EBITDA" / "FY22–H1FY27 Ann. Avg. EBITDA margin 25.1%" | NEUTRAL-FACT | The values slide frames a 26% average (FY22-FY26). The current run-rate is 23.1%, about 3 pp lower. The two averages on adjacent slides cover near-identical windows and differ by 0.9 pp. |
| P-A3-F16-08 | F16 | R181, R207-R210 | L448, L475-477; L205-207, L238 | "(1,479)" / "Fixed Asset Turnover ... 2.9 ... 3.4" | FORWARD-SIGNAL | H1 capex is Rs 1,479 mn, about 5.2% of annualised revenue, and [MEMORY] H1 FY26 was Rs 3,076 mn. Seven dated SOPs run H2 FY27 to H1 FY29. Either capex steps up or new capacity sits outside Sona's own books (eDrive/JV) [INFERENCE]. FAT rose from 2.9 to 3.4. |
| P-A3-F16-09 | F16 | R051-R057, R101-R103, R059 | L172-185, L257-260 | "(20+20+31)2 +4" / "(21+23+31)2" | AMBIGUOUS | Four programs were added, but not-yet-in-production stayed at 31, so about 4 entered production (ramp-up +3, fully ramped +1). The deck names none and shows no robotics SOP (promise C2). The positional order-book counts are 44 EV + 5 robotics = 49, against 75 - 21 = 54 EPIC programs not fully ramped. That is a 5-program gap, with labels positional only. |
| P-A3-F17-01 | F17 | R027, R040, R137-R138, R148, R161-R162, R172 | L123, L142, L390, L398-400 | "The margin was lower due to product mix and higher input prices partially offset by the positive impact of operating leverage" | CONFIRMATORY-NEGATIVE | Q2 margin is 23.0% and H1 23.1%, against the bull line of 24.5% or more: a fail. Q1 by subtraction is 3,026 / 13,104 = 23.09%, so the margin is flat QoQ (-6 bps). Promise C1 (cost pass-through "from Q2") is not delivered in its first scored quarter, and the deck itself names input prices. |
| P-A3-F17-02 | F17 | R180-R190, R038, R202-R204 | L442-460, L138, L479 | "Borrowings" / "2,236" / "∆ Working capital 440" | AMBIGUOUS | The cash leg passes as printed: CFO/PAT is 5,935 / 4,039 = 1.47x and FCFO/PAT 1.10x. But 2,236 of the 6,965 H1 cash build (32%) is new borrowing, taken while opening cash was 12,690. ΔWC of +440 is a net figure [MEMORY: payables +Rs 278.8 Cr, inventory -Rs 176.2 Cr]. Net debt/EBITDA (1.17) hides a rise in gross debt. |
| P-A3-F17-03 | F17 | (none: absence) | whole deck, L1-848 (zero hits for DENSO / eDrive / joint venture); BEV figures L125, L167 | "BEV Revenue ... 6,061 mn ... 129%" | AMBIGUOUS | The deck never mentions the DENSO JV, the eDrive carve-out or the 3-Oct material RPT [MEMORY], although they are the quarter's largest strategic events. It reports BEV and 2W-motor figures as if the business stays wholly owned. Close date, P&L route of the gain and post-close economic share are all missing. |
| P-A3-F17-04 | F17 | R220, R047, R100, R117-R118, R109 | L150, L485, L257, L305, L280-298 | "capital deployed for acquiring NOVELIC" (only mention) | CONFIRMATORY-NEGATIVE | The deck is silent for a second straight quarter on: Novelic impairment (tripwire 3), railway revenue/PAT (tripwire 8), customer-concentration %, forex amount, order-book gross-to-net and corporate guarantees. The geography pie labels cannot be recovered (tripwire 10). See the table in section 5. |
| P-A3-F17-05 | F17 | R119-R120, R099, R103 (loop 1: + M15) | L311, L257-259 | "Robotics and Physical AI 1% 1%" | AMBIGUOUS | Promise C2 (first robotics SOP in Q2) is not evidenced. Robotics revenue stays at 1% of revenue in both FY26 and H1 FY27, while its order book is Rs 13 bn. The conversion timeline is unstated. |

## 3. CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 | N.A. | No ZERO_STANDING rows (A2 count 0). A deck carries no statutory P&L template. Exceptional items appear only as a reason ("exceptional expenses in H1FY26", L433-434). |
| F2 | N.A. | The deck shows only one (unlabelled, consolidated by memory) set of figures. It has no standalone numbers to decompose. |
| F3 | N.A. | No standalone cost lines in the deck. |
| F4 | N.A. | No auditor Other Matters paragraph in a deck. |
| F5 | N.A. | No EoM or going-concern paragraph in a deck. No prior extract. |
| F6 | FINDING | 7 dated SOPs, railway 12-month execution, 10-year order-book horizon, undated development pipeline (F6-01 to F6-05). |
| F7 | FINDING | Order-book delay discount and EOL haircut, size undisclosed (F7-01). Safe-harbor text at L79-90 is boilerplate, not new. |
| F8 | N.A. | No tax line or ETR in the deck. "Tax paid & Others (1,093)" (L457-458) is lumped cash, not an ETR. |
| F9 | N.A. | No OCI in the deck. |
| F10 | FINDING | ESOP cash Rs 1,076 mn in the bridge. No share count or EPS (F10-01). |
| F11 | N.A. | The deck carries no net-worth figure to tie. Net debt/EBITDA is cross-checked under F17-02. |
| F12 | N.A. | No segment assets or liabilities in the deck. Order-book and revenue-mix splits are assessed under F16. |
| F13 | N.A. | A deck has no board outcome. The cover letter is a Reg 30 enclosure only (L31-36). |
| F14 | FINDING | Ratio definition drift, the 6.6 vs 6.9 heading, PAT basis mismatch, scrambled footnotes and no consolidated label (F14-01 to F14-04). |
| F15 | N.A. | No consolidation list in the deck. Entity names (NOVELIC, Railway Business) are consistent. |
| F16 | FINDING | No prior extract, so a verbatim deck diff was not possible. Comparisons use Notion memory, labelled. 9 findings (F16-01 to F16-09). |
| F17 | FINDING | Deck silence audit against the Notion checklist, following the Q1 deck precedent (P-A3-F17-xx) (F17-01 to F17-05). |

## 4. COMMITMENT REGISTER (F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| Traction motors, extra volumes in 2 existing E2W/E3W programs, Rs 12,500 mn | H2 FY27 | s11 L203-209 (R073-R076) | initiated |
| Integrated motor controller E2W, Rs 3,800 mn | H1 FY28 | s11 L201-207 (R069-R072) | initiated |
| Differential gears ICE PV/OHV, Rs 2,000 mn | H1 FY28 | s13 L234-240 (R087-R090) | initiated |
| Rear radar sensor 2W (new customer), Rs 1,000 mn; "commercialized in Q2FY27" | H2 FY28 | s11 L201-207; s18 L366-372 (R065-R068, R126-R127) | initiated (order won; "commercialized" in legend) |
| Differential assembly ICE PV, Rs 1,600 mn | H2 FY28 | s13 L234-240 (R083-R086) | initiated |
| Helical LSD for EV PVs (global EV OEM), Rs 7,000 mn | H1 FY29 | s11 L201-207; s18 L341-342 (R061-R064, R125) | initiated |
| Starter motors ICE PV (NA OEM), Rs 3,300 mn | H1 FY29 | s13 L234-240 (R079-R082) | initiated |
| Railway order book Rs 9 bn executed | within 12 months (~Sep 2027) | s14 L257, L267 (R100, R106-R107) | underway |
| Net order book Rs 251 bn realised | next 10 years | s14 L244, L263 (R091, R105, R108) | underway |
| 31 EPIC programs not yet in production move to SOP | undated | s10 L174 (R055, R059) | initiated |
| Development products (PV/CV traction motor, park gear controller, AMR drive unit, robot gearbox, eVTOL motor/gearbox, frameless motors) | undated | s33-35 L753, L792, L826 (R311, R313, R315) | underway |
| Hub wheel motor E2W (Q1 deck SOP H2 FY26) | H2 FY26 | s35 L798 (no asterisk) [MEMORY] | completed [INFERENCE] |
| Components to subsystems to systems roadmap; vision statement | undated | s18 L324 (R122); s27 L570-577 (R241) | initiated |

## 5. F17 SILENCE AUDIT: WHAT WAS NOT DISCUSSED (deck vs Notion checklist, 26-Oct Key Notes)

Count = consecutive quarters with no numeric answer in the deck lens. The Q1 status comes from Notion memory, because no prior extract exists.

| checklist item | deck treatment | consecutive quarters silent |
|---|---|---|
| Op EBITDA margin bull >=24.5% / bear <23.0% | ADDRESSED: 23.0% Q2 (L123), 23.1% H1 (L142); basis includes forex (L404) | forex amount silent: 2 |
| CFO/PAT >=1.0x | ADDRESSED: 5,935 vs PAT 4,039 = 1.47x (L448, L138) | payables split silent: 1 |
| C1 margin recovery from Q2 | ADDRESSED as a miss: "product mix and higher input prices" (L398) | n/a (delivered: NO) |
| C2 first robotics SOP | NOT ADDRESSED; robotics revenue 1% (L311) | 1 |
| C3 ADAS radar | PARTIAL: 2W rear radar order, SOP H2 FY28 (L205); no PV ADAS | 1 (due Q1; no radar revenue in Q1 or Q2) |
| DENSO close / eDrive deconsolidation | NOT ADDRESSED (zero mentions) | 1 verified in decks (Q1 deck NOT VERIFIABLE) |
| Auditor signing time vs board start | N.A. for deck. Cover letter signed 2026.10.26 16:23:05 (L45-47) | n/a |
| Short-term borrowings | PARTIAL: positional "Borrowings" inflow 2,236 (L454-456); gross debt not shown | 1 |
| EV share of order book | ADDRESSED: 61% (L257-258) | 0 |
| ROCE path to >18% | Number given, 16.4% (L469); no path | 2 |
| Novelic impairment (tripwire 3) | NOT ADDRESSED | 2 |
| Railway revenue/PAT (tripwire 8) | NOT ADDRESSED (only non-auto mix 29%, L305, and book Rs 9 bn) | 2 |
| Customer concentration % | NOT ADDRESSED | 2 |
| India revenue mix (tripwire 10) | Pie labels not machine-recoverable (L280-298) | 2 |
| Order-book gross-to-net discount | NOT ADDRESSED (method only, L265-266) | 2 |
| Corporate guarantees (tripwire 5) | NOT ADDRESSED | 2 |

## 6. A4 HAND-OFF (FORWARD-SIGNAL and AMBIGUOUS ids)

FORWARD-SIGNAL: P-A3-F6-01, P-A3-F6-02, P-A3-F6-04, P-A3-F16-04, P-A3-F16-08.
AMBIGUOUS: P-A3-F6-03, P-A3-F7-01, P-A3-F14-01, P-A3-F14-03, P-A3-F16-01, P-A3-F16-03, P-A3-F16-09, P-A3-F17-02, P-A3-F17-03, P-A3-F17-05.

## 7. Loop 1 addendum: M01-M15 ID confirmation

Trigger: A5 finding M1. A2 appended MISSING_FROM_STRUCTURED rows M01-M15 to the ledger (Table 8). I read each row at its fulltext line. F1-F17 were not re-run. No existing finding changes status, classification or implication. Two finding rows now also cite M-IDs (F16-07, F17-05).

| M-ID | line | verbatim at line | check | status |
|---|---|---|---|---|
| M01 | L291 | "22%" | F16 (pie mix) / F17 (tripwire 10) | Reviewed, no finding. **I disagree with A2's placement.** A2 puts 22% in the H1 FY27 geography pie, but 10+14+25+22 = 71, not 100. 10+14+25+51 = 100 does work, so the "51%" on the same line is the H1 geography value. 22% belongs to the product pies: the R110 values minus 51 plus 22 sum to 200. This supports the section 1 sum test and the "pie labels not recoverable" row in F17-04. |
| M02 | L504 | "Became publicly listed" | F15 (entities) | Reviewed, no finding. Historical event; F15 stays N.A. |
| M03 | L505 | "Acquisition of NOVELIC and Railway Business" | F14 / F15 | Reviewed, no finding. It matches the p23 ROCE denominator scope (L485), so it supports P-A3-F14-01: p7 (L150) leaves out Railway. |
| M04 | L506 | "12 plants" | F16 | Reviewed, no finding. Ties to R252 "12 Manufacturing Plants" (L626). |
| M05 | L507 | "34 products" | F16 | Reviewed, no finding. Up from 10 products in Phase 3 (R224). This is a slogan figure with no reconciliation to the p33-p36 catalogue. |
| M06 | L510 | "57,136 H1FY27 (Ann.)" | F16 | Reviewed. 2 x 28,568 = 57,136, so it ties. It is the end point of the 24.1% CAGR (M08). The annualisation doubles H1 and ignores H2 seasonality. Supports P-A3-F16-07 context. |
| M07 | L512-513 | "FY22–H1FY27 Ann. Avg. EBITDA margin 25.1%" | F16 | Supports **P-A3-F16-07**, which already cited L512-513. |
| M08 | L515 | "Revenue CAGR 24.1%" | F16 | Reviewed. It ties as FY21 15,663 (R239) to 57,136 over 6 years = 24.1%. Supports P-A3-F16-07. No finding change. |
| M09 | L516 | "44,752" | F16 | Reviewed, no finding. Year by position; FY26 also tied in-deck (see note below). |
| M10 | L518 | "35,545" | F16 | Reviewed, no finding. Year by position only (FY25). |
| M11 | L519 | "31,866" | F16 | Reviewed, no finding. Year by position only (FY24). |
| M12 | L520 | "26,756" | F16 | Reviewed, no finding. Year by position only (FY23). |
| M13 | L522 | "21,306" | F16 | Reviewed, no finding. Year by position only (FY22). |
| M14 | L523 | "28,568 H1FY27" | F16 | Reviewed, no finding. Restates R153 and R034 (L413, L138). |
| M15 | L156; L378 | "Our Integrated Motor Controllers, EVTOL Gearbox, and AMR Drive Unit at CES 2026"; "Our Exhibition Booth at Indian Railway Equipment Exhibition (IREE) 2025" | F6 / F17 | Supports **P-A3-F17-05**. The AMR drive unit and eVTOL gearbox are shown at a trade show, but p35 marks both "*Product under development" (L802, L810, L821-826). That is a showcase, not a robotics SOP, so C2 is still not evidenced. The IREE caption has no number. |

**Can the bar years be tied, or only placed by position?**
- In the text layer, no year label sits next to any bar value. The years sit on a separate axis block (L535-564), so a year can be assigned only by count and position. The 28 values for FY99-FY26 plus the H1 bars give FY20 10,380, FY21 15,663, FY22 21,306, FY23 26,756, FY24 31,866, FY25 35,545 and FY26 44,752 [INFERENCE].
- Two end points also tie by arithmetic inside the deck. FY26 = 44,752: Rs 251 bn / 44,752 mn = 5.61x, which matches "5.6x FY26 revenue" (L244). FY21 = 15,663: the 24.1% (M08) and 23% (R242, L583) CAGRs only reproduce from that base.
- The three middle years (FY23-FY25) rest on position and a rising sequence only. No in-deck number ties them.
- A4's use of 44,752 as FY26 is therefore supported by deck arithmetic, not by position alone. [MEMORY] Notion's FY26 revenue of Rs 4,475 Cr agrees.

Reconciliation after loop 1: 332 of 332 ledger rows read (317 R + 15 M) = 100%.

```yaml
stage: A3-forensics
company: "SONACOMS"
quarter: "q2fy27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "C:/Users/SUMIT SHARMA/repos/inflection-pipeline/.claude/worktrees/qr-sonacoms-q2fy27-c7173c/runs/sonacoms-q2fy27/work/forensics_presentation_sonacoms_q2fy27.md"
ledger_reconciled_pct: 100        # loop 1: 332 / 332 (317 R + 15 M)
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: N.A.
  F9: N.A.
  F10: FINDING
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "P-A3-F6-01", check: "F6", line: "L201-209 s11", classification: "FORWARD-SIGNAL", implication: "Traction-motor extra volumes Rs 12,500 mn SOP H2 FY27; nearest delivery test Q3/Q4 FY27"}
  - {id: "P-A3-F6-02", check: "F6", line: "L205, L238 s11/s13", classification: "FORWARD-SIGNAL", implication: "Rs 18.7 bn of Rs 31.2 bn itemised Q2 wins (60%) start production FY28-FY29; revenue lag 2-3 years"}
  - {id: "P-A3-F6-03", check: "F6", line: "L366-372 vs L205", classification: "AMBIGUOUS", implication: "'Commercialized in Q2FY27' means order won; rear radar SOP H2 FY28, LSD H1 FY29; C3 scoring needs definition"}
  - {id: "P-A3-F6-04", check: "F6", line: "L257, L267, L305", classification: "FORWARD-SIGNAL", implication: "Railway book Rs 9 bn ~0.8 yr of FY26 run-rate [MEMORY]; non-auto share 31% to 29%; tripwire 8"}
  - {id: "P-A3-F6-05", check: "F6", line: "L753, L792, L798, L826", classification: "NEUTRAL-FACT", implication: "Development products undated; hub wheel motor no longer under development"}
  - {id: "P-A3-F7-01", check: "F7", line: "L263-266 s14", classification: "AMBIGUOUS", implication: "Order-book delay discount and EOL haircut size undisclosed, second quarter"}
  - {id: "P-A3-F10-01", check: "F10", line: "L453-458 s22", classification: "NEUTRAL-FACT", implication: "ESOP cash ~Rs 1,076 mn H1; no share count or EPS in deck; A4 cross-check dilution"}
  - {id: "P-A3-F14-01", check: "F14", line: "L150-152 vs L485-488 vs L603", classification: "AMBIGUOUS", implication: "Same ROCE 16.4%/ROE 13.9% under two definitions; ROE adds back Rs 301 mn; un-normalised ROCE vs 18% NOT FOUND"}
  - {id: "P-A3-F14-02", check: "F14", line: "L220-221 vs L234", classification: "NEUTRAL-FACT", implication: "Non-electric heading Rs 6.6 bn vs tiles Rs 6.9 bn"}
  - {id: "P-A3-F14-03", check: "F14", line: "L388-397, L415-429, L406", classification: "AMBIGUOUS", implication: "Headline PAT vs margin PAT basis differ; stated margin declines (~0.5%, ~1.5%) understate arithmetic (0.7-0.8 pp, 1.6 pp)"}
  - {id: "P-A3-F14-04", check: "F14", line: "L140-152; L35", classification: "NEUTRAL-FACT", implication: "p7 footnote markers scrambled, RoE4 orphan; no consolidated label on any deck slide"}
  - {id: "P-A3-F16-01", check: "F16", line: "L404, L438 vs L119-134", classification: "AMBIGUOUS", implication: "Forex-in-revenue qualifier absent on highlight slides; gate bear line cleared by 4 bps incl forex, fails ex-forex (22.5% [MEMORY])"}
  - {id: "P-A3-F16-02", check: "F16", line: "L257-258", classification: "CONFIRMATORY-NEGATIVE", implication: "EV share of order book 61%, third easing (~70 to 64 to 61); tripwire 9"}
  - {id: "P-A3-F16-03", check: "F16", line: "L248-252, L201-203, L234, L257", classification: "AMBIGUOUS", implication: "Rs 4.8 bn adds unitemised; robotics book up ~Rs 5 bn with no itemised win; 25 bn consumed = 1.6x revenue, may hold re-estimates"}
  - {id: "P-A3-F16-04", check: "F16", line: "L190-203, L297", classification: "FORWARD-SIGNAL", implication: "Rs 16.3 bn (45% of adds) from Indian 2W/3W OEM(s); E2W/E3W share 10% to 14%; booking entity vs eDrive/DENSO undisclosed"}
  - {id: "P-A3-F16-05", check: "F16", line: "L700, L703, L718", classification: "CONFIRMATORY-NEGATIVE", implication: "CY25 global share dipped in diff gears (8.8 to 8.7) and starters (4.4 to 4.2); India claim on Feb-2021 data"}
  - {id: "P-A3-F16-06", check: "F16", line: "L467, L484, L398-400", classification: "CONFIRMATORY-NEGATIVE", implication: "VA/employee cost 5.8 to 4.9 to 4.7 falls despite claimed operating leverage; structural material-margin drag"}
  - {id: "P-A3-F16-07", check: "F16", line: "L589-605 vs L512-513 (M07, M08), L142", classification: "NEUTRAL-FACT", implication: "Values slide frames 26% 5-yr margin vs 23.1% run-rate; adjacent-slide averages differ 0.9 pp"}
  - {id: "P-A3-F16-08", check: "F16", line: "L448, L475-477", classification: "FORWARD-SIGNAL", implication: "H1 capex Rs 1,479 mn (~5.2% of ann. revenue) vs seven SOPs to H1 FY29; capex step-up or capacity off-book"}
  - {id: "P-A3-F16-09", check: "F16", line: "L172-185, L257-260", classification: "AMBIGUOUS", implication: "~4 programs entered production unnamed; no robotics SOP shown (C2); 49 vs 54 program-count gap (positional labels)"}
  - {id: "P-A3-F17-01", check: "F17", line: "L123, L142, L398-400", classification: "CONFIRMATORY-NEGATIVE", implication: "Margin 23.0% fails bull 24.5%; flat QoQ; C1 pass-through missed, input prices named"}
  - {id: "P-A3-F17-02", check: "F17", line: "L442-460, L479", classification: "AMBIGUOUS", implication: "CFO/PAT 1.47x passes; 32% of cash build is new borrowing Rs 2,236 mn; payables-led WC [MEMORY]"}
  - {id: "P-A3-F17-03", check: "F17", line: "L1-848 (zero hits); L125, L167", classification: "AMBIGUOUS", implication: "Deck silent on DENSO/eDrive carve-out; BEV and 2W-motor figures shown as wholly owned"}
  - {id: "P-A3-F17-04", check: "F17", line: "L150, L485, L257, L305, L280-298", classification: "CONFIRMATORY-NEGATIVE", implication: "Second quarter silent on Novelic impairment, railway P&L, concentration %, forex quantum, gross-to-net, guarantees"}
  - {id: "P-A3-F17-05", check: "F17", line: "L311, L257-259; L156 (M15)", classification: "AMBIGUOUS", implication: "C2 robotics SOP not evidenced; robotics revenue 1% vs Rs 13 bn book; AMR drive unit shown at CES but under development"}
forward_signals: ["P-A3-F6-01", "P-A3-F6-02", "P-A3-F6-04", "P-A3-F16-04", "P-A3-F16-08"]
ambiguous: ["P-A3-F6-03", "P-A3-F7-01", "P-A3-F14-01", "P-A3-F14-03", "P-A3-F16-01", "P-A3-F16-03", "P-A3-F16-09", "P-A3-F17-02", "P-A3-F17-03", "P-A3-F17-05"]
commitments:
  - {commitment: "Traction motors extra volumes, 2 E2W/E3W programs, Rs 12,500 mn", implied_date: "H2 FY27", ref: "s11 L203-209", status_word: "initiated"}
  - {commitment: "Integrated motor controller E2W, Rs 3,800 mn", implied_date: "H1 FY28", ref: "s11 L201-207", status_word: "initiated"}
  - {commitment: "Differential gears ICE PV/OHV, Rs 2,000 mn", implied_date: "H1 FY28", ref: "s13 L234-240", status_word: "initiated"}
  - {commitment: "Rear radar sensor 2W, new customer, Rs 1,000 mn", implied_date: "H2 FY28", ref: "s11 L201-207; s18 L366-372", status_word: "initiated"}
  - {commitment: "Differential assembly ICE PV, Rs 1,600 mn", implied_date: "H2 FY28", ref: "s13 L234-240", status_word: "initiated"}
  - {commitment: "Helical LSD EV PV, global EV OEM, Rs 7,000 mn", implied_date: "H1 FY29", ref: "s11 L201-207", status_word: "initiated"}
  - {commitment: "Starter motors ICE PV, NA OEM, Rs 3,300 mn", implied_date: "H1 FY29", ref: "s13 L234-240", status_word: "initiated"}
  - {commitment: "Railway order book Rs 9 bn executed", implied_date: "within 12 months (~Sep 2027)", ref: "s14 L257, L267", status_word: "underway"}
  - {commitment: "Net order book Rs 251 bn realised", implied_date: "next 10 years", ref: "s14 L244, L263", status_word: "underway"}
  - {commitment: "31 EPIC programs not yet in production reach SOP", implied_date: "undated", ref: "s10 L174", status_word: "initiated"}
  - {commitment: "Development products (PV/CV traction motor, park gear controller, AMR drive unit, robot gearbox, eVTOL, frameless motors)", implied_date: "undated", ref: "s33-35 L753, L792, L826", status_word: "underway"}
  - {commitment: "Hub wheel motor E2W (Q1 deck SOP H2 FY26)", implied_date: "H2 FY26", ref: "s35 L798 [MEMORY]", status_word: "completed"}
gate_a3: pass
blank_checks: []
loop1_note: "A5 M1 correction: M01-M15 read at their lines; 332/332 rows reconciled. No finding changed; M07/M08 support F16-07, M15 supports F17-05, M03 supports F14-01. Disagree with A2 on M01: 22% belongs to product pies, the 51% on L291 is H1 geography (10+14+25+51=100; 10+14+25+22=71). Bar years by position only, except FY26 44,752 (ties to 5.6x on L244) and FY21 15,663 (ties to 24.1% and 23% CAGRs); FY23-FY25 position-only."
analyst_note: "Two readings of the deck. Bull: revenue up 35%, BEV 51%, cash bridge ties exactly, CFO/PAT 1.47x, ROCE 15.4 to 16.4%. Bear: the margin gate depends on the forex ruling (23.0% incl forex, about 22.5% ex). The C1 miss is self-declared (input prices). VA/employee cost keeps falling, which points to a structural drag, not lagged pass-through. A third of the H1 cash build is new debt. Order-book quality is the sleeper issue: 25 bn consumed is 1.6x revenue, Rs 4.8 bn of adds are unitemised, robotics jumped with no itemised win, and the EV share eased again. 45% of adds sit in 2W motors, the business DENSO is buying 49% of, and the deck never names DENSO. The 'commercialized' legend should not count as C3 delivery, since radar SOP is H2 FY28. Pipeline note: A1 left unrowed L291 '22%' and the p26 FY22-FY26 revenue series, 25.1% margin and 24.1% CAGR. A2's R051 query is a misread (20+20+31 = 71). R104 is a page number."
```
