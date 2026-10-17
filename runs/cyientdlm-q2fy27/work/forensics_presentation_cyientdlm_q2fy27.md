# A3 FORENSIC NOTES: CYIENT DLM (CYIENTDLM) Q2 FY27, doctype PRESENTATION
Agent: A3 forensics, claude-opus-5-5. Date: 2026-10-17.
Inputs read: A1 structured extraction (R001-R372), A1 fulltext (lines 1-468, 18 pages), A2 ledger. No source PDF, nothing under inputs/. Prior-quarter fulltext: not available.
Units: INR Mn (x0.1 to Rs Cr). Cites: "L###" = fulltext line; "p" = PDF page; slide footer = PDF page minus 1.

## 0. LEDGER RECONCILIATION
- 372 of 372 structured IDs read at their cited lines. Every value is present verbatim in the fulltext. Reconciled: 100%.
- A1 line-cite offsets (value correct, line off by 1-2; this report cites the true line): R077 196 (cited 266, true L268); R088 11.7% (267 -> L265); R092 182M (259 -> L260); R094 21,318 (293 -> L294); R110 64 and R111 63 (293 -> L292); R142/R143 62%/29% (354 -> L355); R144 13% (358 -> L359); R147 86% (358 -> L359). No value errors.
- Chart period assignment (A2 CHART_LABEL_JUMBLED, R061-R130). I did not assign periods by position alone. Each assignment below is tied by arithmetic:
  - Revenue (p11): Q1'27 3,738 + Q2'27 3,931 = 7,669 = H1 FY27 (L430). Q1'26 2,784 + Q2'26 3,106 = 5,890 vs H1 FY26 5,891 (L430). Tied.
  - EBITDA (p11): H1 733 - Q2 342 = 391 vs Q1'27 label 392; H1 FY26 563 - 312 = 251 = Q1'26 label. Q3'26 = 309 and Q4'26 = 431 are forced by the margin labels: 309/3,033 = 10.2% and 431/3,691 = 11.7% (L265-267); the swapped pairing gives 14.2% and 8.4%, which the chart does not show.
  - PAT (p11): H1 503 - 340 = 163 = Q1'27 label (L270); H1 FY26 396 - 321 = 75 = Q1'26 label (L272). Q3'26 138 (L271), Q4'26 224 (L269) by column, the remaining two labels.
  - Working-capital days (p12): column positions checked against the identity NWC = DIO + DSO - DPO - Advances. Q2'26 172+72-73-33 = 138 (chart 139); Q3'26 195+76-83-28 = 160 (160); Q4'26 153+74-64-18 = 145 (145); Q1'27 162+77-63-15 = 161 (161); Q2'27 162+73-68-13 = 154 (153); Q1'26 185+74-71-21 = 167 (165, inside four-term rounding). Tied.
  - Pie slices (p13, SLICE_UNASSIGNED): industry slices NOT assigned. Product slices: Box Build = 37% only via the text "Box Build is the 2nd highest share in product category" (L357-358). PCBA = 48% is an [INFERENCE] from "PCBA business share continues to remain high" (L353-354).

Derived tables (from tied values only):

| Quarter | Rev | EBITDA | EBITDA % | PAT rep | Order book | DIO | DSO | DPO | Adv | NWC |
|---|---|---|---|---|---|---|---|---|---|---|
| Q1'26 | 2,784 | 251 | 9.0% | 75 | 21,318 | 185 | 74 | 71 | 21 | 165 |
| Q2'26 | 3,106 | 312 | 10.0% | 321 (196 one-off) | 22,911 | 172 | 72 | 73 | 33 | 139 |
| Q3'26 | 3,033 | 309 (275 + 34 one-off) | 10.2% | 138 | 23,494 | 195 | 76 | 83 | 28 | 160 |
| Q4'26 | 3,691 | 431 | 11.7% | 224 | 24,166 | 153 | 74 | 64 | 18 | 145 |
| Q1'27 | 3,738 | 392 | 10.5% | 163 | 25,989 | 162 | 77 | 63 | 15 | 161 |
| Q2'27 | 3,931 | 342 | 8.7% | 340 (182 one-off) | 28,137 | 162 | 73 | 68 | 13 | 153 |

Cost ratios (% of revenue; Q1 values derived as H1 minus Q2, L375-379, L430-435):

| Line | Q1 FY26 | Q1 FY27 | Q2 FY26 | Q2 FY27 | Q2 YoY |
|---|---|---|---|---|---|
| Material | 59.8% | 62.1% | 58.8% | 62.6% | +379 bps |
| Employee | 20.8% | 17.2% | 17.0% | 17.3% | +24 bps |
| Other expense | 10.5% | 10.2% | 14.1% | 11.4% | -269 bps |
| Gross margin (rev less material) | 40.2% | 37.9% | 41.2% | 37.4% | -379 bps |

## 1. FINDINGS TABLE

| id | check | ledger rows | line / slide | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FN01 | F16 | R319, R152-R166 | L255-257 (p11, slide 10); L375-381 (p14, slide 13) | "EBITDA margin reflects continued investment into sales, strategy and strengthening capabilities" | FORWARD-SIGNAL | The deck attributes the margin to opex investment. The Q2 table says otherwise: material ratio +379 bps YoY, employee +24 bps, other expense -269 bps; net -134 bps (stated -135, L381). Opex fell 245 bps as a share of revenue. The margin loss is a material-cost cause. The p11 commentary repeats the opex cause that the Notion log recorded last time (test 2). |
| FN02 | F7 | R355, R040, R147 | L374-375 (p14); L186 (p8) | "DMC % is variance in Q2FY27 due to one-off Revenue mix impact and purchases towards product development" vs "Box Build +86% YoY drives the shift to higher-value integration" | FORWARD-SIGNAL | The note labels the mix effect "one-off". The same deck calls the Box Build shift the strategy. Two readings: (a) transitory mix plus product-development purchases; (b) Box Build carries more bought-in material, so the material ratio steps up for as long as Box Build outgrows PCBA. Separating observation: Q3 FY27 material ratio with Box Build share at or above 37%. "Purchases towards product development" are booked in material cost; whether this is B2S development spend is not stated. |
| FN03 | F14 | R362, R230-R232, R152-R154 | L430-431 (p16, slide 15) | "DMC % increase is mainly flowing from Q2 FY27" | AMBIGUOUS | Derived Q1 FY27 material ratio 62.1% vs Q1 FY26 59.8% = +226 bps. Q2 adds +379 bps. Both quarters compressed gross margin YoY (40.2% to 37.9%; 41.2% to 37.4%). "Mainly Q2" is true only in size; it hides that Q1 also compressed. Q1 compression was masked by employee-cost leverage (-353 bps). Notion test 2 needs the quarter count: this deck shows 2 consecutive YoY compressions; Q3/Q4 FY26 material cost is NOT FOUND in this deck. |
| FN04 | F16 | R030, R035-R037, R052-R053, R085-R090 | L146, L165 (p7, slide 6); L229-230 (p10); L265-269 (p11) | "Margins ~9–11% · proven core stack"; "Margins ~11–13% · same stack, new sectors"; "8.7%" / "-135 bps YoY" | FORWARD-SIGNAL | Q2 FY27 EBITDA margin 8.7% is the lowest of six charted quarters and below the deck's own "today" band. FY26 (sum of four tied quarters) = 1,303/14,614 = 8.9%, also below the band; trailing four quarters to Q2 FY27 = 1,474/14,393 = 10.2%, inside it. FY27 is year 1 of the 11-13% EXPAND window; Q2 sits 230-430 bps short. The p7 "Margins" metric is not defined (EBITDA? gross?). Notion test 4 (>=100 bps reported EBITDA uplift) not met: Q2 -135 bps, H1 +1 bps (L414). |
| FN05 | F14 | R060, R201-R203, R279-R280, R344, R358, R367, R295-R296 | L384-385 (p14); L447-449 (p16); L237 (p10); L192 (p8) | "Other income includes one-off Earnout reversal in both Q2 FY26 and Q2 FY27 (INR 196M and INR 182M respectively)" | FORWARD-SIGNAL | A "one-off" that recurs in the same quarter two years running. It is 53.5% of Q2 FY27 reported PAT (182/340), 61.1% of Q2 FY26 (196/321), 36.2% of H1 FY27 (182/503). Cumulative 378 Mn (Rs 37.8 Cr). [INFERENCE] An earn-out liability reverses when the acquired business misses its earn-out targets; the deck does not state why. The second reversal lands in the quarter the deck says "Altek Electronics integration completed and renamed" (L192). Forward: (a) goodwill impairment test on the Altek CGU at FY27 close; (b) remaining contingent consideration NOT FOUND; (c) Q2 FY28 reported PAT faces a 182 Mn base. Any multiple on reported PAT overstates operating earnings by about half this quarter. |
| FN06 | F8 | R182-R187, R260-R265 | L387-388 (p14); L446-447 (p16) | "Tax 53 43 22.4%"; "Tax 112 70 61.1%" | NEUTRAL-FACT | Reported ETR: Q2 FY27 13.5%, Q2 FY26 11.8%, H1 FY27 18.2%, H1 FY26 15.0%, vs statutory 25.17%. Ex-earnout ETR: 25.1%, 25.4%, 25.9%, 25.9%. The earnout reversal carries no tax, and normalized PAT deducts it gross (340-182 = 158; 503-182 = 321). No hidden tax shield on operating profit. The deck shows no current/deferred split and no prior-year tax line (NOT FOUND); A4 checks those in the results filing. Reported ETR returns to about 25% once the earnout stops. |
| FN07 | F16 | R118-R123, R106-R111, R124-R129 | L305-315, L287-292 (p12, slide 11) | "Customer Advance (Days)" labels 33, 28, 18, 15, 13 | FORWARD-SIGNAL | Customer advance days fell four quarters in a row: 33 (Q2'26), 28, 18, 15, 13 (Q2'27), down 61%. DPO fell from 83 (Q3'26) to 68. NWC days rose 139 to 153 YoY (+14) while DIO improved 172 to 162 (-10). The YoY NWC rise is mainly the advance loss (+20 days). Bull reading: QoQ NWC improved 161 to 153 and DIO is down 10 YoY. Bear reading: new orders (book at a record, +22.8% YoY) carry fewer advances, so working capital per rupee of revenue rises with growth. Separating observation: advance days in Q3 FY27 against order inflow mix (domestic defence vs ROW). |
| FN08 | F16 | R124-R129, R349 | L284, L305-311 (p12) | "All numbers are in Days and order book in ₹Mn" | AMBIGUOUS | The deck does not define its NWC-days method. Its quarterly series (165, 139, 160, 145, 161, 153) never reaches the 169 days Notion logged for FY26; Q4'26 prints 145. The two numbers sit on different bases. Notion test 1 (<=120 by Q4 FY27 falsifies; >161 confirms) cannot be applied until the basis is fixed. On the deck basis, Q1'27 printed exactly 161 (at, not above, the confirm line) and Q2'27 153; falsifying needs -33 days in two quarters. |
| FN09 | F14 | R357, R365, R176-R178, R254-R256 | L381-382 (p14); L442-443 (p16) | "Finance cost declined 10.4 % YoY, driven by lower working capital borrowings" | AMBIGUOUS | NWC days rose 14 YoY and revenue rose 26.5%, so rupee working capital rose YoY (direction only; amount NOT FOUND). Working-capital borrowings fell at the same time. The funding source for the larger NWC is not stated (internal accruals, cash on hand, parent). Finance cost was flat QoQ at 61 (Q1 derived 122-61). |
| FN10 | F16 | R130, R350 | L325 (p12, slide 11) | "* Operation free cash flow for Q2 FY27: INR 172Mn" | AMBIGUOUS | The asterisk attaches to no chart metric (FOOTNOTE_UNRESOLVED). "Operation free cash flow" is not defined; no H1 or prior-quarter figure is given. 172 = 50% of Q2 EBITDA and above normalized PAT (158). It is not CFO. Notion test 1 needs positive CFO; this number does not satisfy that test by itself. |
| FN11 | F14 | R067-R074, R085-R090, R079-R082, R346-R348 | L250, L253, L256, L267, L271 (p11, slide 10) | "EBITDA (INR Mn) Normalized ... One-off's"; "EBITDA % Normalized" | AMBIGUOUS | Q3'26 EBITDA 309 splits into 275 normalized plus a 34 one-off. The "EBITDA % Normalized" chart shows 10.2% for Q3'26, which is 309/3,033 (one-off included); normalized is 275/3,033 = 9.1%. The PAT chart shows Q3'26 PAT 138 with no one-off split. The 34 Mn Q3 FY26 EBITDA one-off is not explained in this deck. The normalization basis differs across three charts on one slide. |
| FN12 | F16 | R131-R139, R142-R147, R351, R300 | L353-362 (p13, slide 12) | "Others share includes B2S." | AMBIGUOUS | The slide gives YoY growth for Aerospace 62%, Industrial 29%, Defence 13%, Med Tech 14%, PCBA 19%, Box Build 86%. It gives none for Auto & Others, Cables, or Mech & Others (the bucket that holds B2S). [INFERENCE] With Box Build 37% at +86% and PCBA 48% at +19%, the remaining product buckets (15% now) shrank about 12-28% YoY across the rounding range. B2S is the p7 "platform moat" for the 13-18% margin stage; its share is not disclosed. Notion test 4 (design-led share double digits) cannot be measured from this deck. Defence grew at half the company rate. |
| FN13 | F16 | R032-R034, R299, R313 | L153-161 (p7, slide 6) | "4 INDUSTRIES · FOUNDATION" ... "Industrial/Semicon"; "7 INDUSTRIES · +3 NEW" ... "Industrial" ... "Semicon Cap Equipment" | AMBIGUOUS | The foundation stage already lists "Industrial/Semicon". The EXPAND stage counts "Semicon Cap Equipment" as one of 3 new industries and drops "/Semicon" from Industrial. One "new" industry is a carve-out of an existing one. None of the three new industries (semicap, robotics, AI data center) has a revenue line in the p13 segments (L338-346). "Three new logos" (L186) carry no split by area. |
| FN14 | F15 | R295, R296 | L192-194 (p8, slide 7) | "Altek Electronics integration completed and renamed Cyient DLM Electronics Inc." | AMBIGUOUS | Entity rename. It coincides with the second earnout reversal (FN05). Questions for A4: does the rename close the earn-out window; what contingent consideration remains; will the US subsidiary still report separately (Notion test 6 depends on that line under its new name). |
| FN15 | F14 | R343, R353, R360, R355, R362 | L242 (p11); L371, L427 (p14, p16); L374, L430 | "KEY KPI's TREND 1"; "Amount in ₹ Mn"; "DMC %" | NEUTRAL-FACT | Drafting gaps: (a) neither financial table states consolidated or standalone; A4 ties 3,931 to the results filing; (b) marker "1" on the KPI title has no footnote; (c) both notes discuss "DMC %" but no table carries a DMC line or number; (d) the OpFCF asterisk (FN10). Individually small; together, the deck explains a metric it does not print. |
| FN16 | F14 | R005-R009, R025-R027, R368 | L115-116, L127-129, L140 (p6, slide 5) | "Global robotics market by 2030, ~14% CAGR from ~$50 Bn in 2025"; "Upside case 2030 · 9.8% CAGR" | NEUTRAL-FACT | $50 Bn at 14% for five years gives about $96 Bn, not $111 Bn. $649 Bn at 9.8% for five years gives about $1.04 Tn, not "~$1.1 Tn". The base and upside cases come from different sources (L140). Third-party sizing; low weight; no effect on company numbers. |
| FN17 | F6 | R312-R318, R335-R336 | L146-165 (p7); L191-194 (p8) | "Path from ~9–11% to ~13–18% Margins"; "FY27-29"; "integration completed" | FORWARD-SIGNAL | Dated targets for the Role 5 promise-vs-delivery tracker: 11-13% margins in FY27-29, 13-18% in FY30+, 7 industries in FY27-29. FY27 H1 delivered 9.6% EBITDA margin (L413). One status word: Altek integration "completed". See Commitment Register. |
| FN18 | F16 | R140, R141, R148, R352 | L359-361 (p13) | "India business Mix of 7% is primarily contributed from A&D, Auto Segment and Medical" | NEUTRAL-FACT | India is 7% of Q2 FY27 revenue, ROW 93%. This deck gives no prior-period mix. A4 compares against the prior deck and the Notion India-vs-Altek test (6). |

Positive data points in the same deck (stated for symmetry, not findings): order book at a record 28,137 Mn, +2,148 QoQ (L229-230) and +22.8% YoY; implied Q2 inflow = 3,931 + 2,148 = 6,079 Mn, 1.55x [INFERENCE, no cancellations assumed], which ties to the stated 1.6x book-to-bill (L179). Other expense ratio -269 bps YoY (L379). DIO -10 days YoY. OpFCF positive (L325). Normalized PAT +25.8% YoY (L391).

## 2. CHECKLIST SCORECARD

| Check | Status | Basis |
|---|---|---|
| F1 | PASS | 34 P&L lines across two tables (L375-392, L430-451); all non-zero; A2 zero_standing = 0. |
| F2 | N.A. | Deck prints one unlabelled basis; no standalone figures to decompose (basis gap logged at FN15). |
| F3 | N.A. | No standalone cost lines in the deck. |
| F4 | N.A. | No auditor report or Other Matters paragraph in a presentation. |
| F5 | N.A. | No going-concern or EoM paragraph; no prior-quarter extract. |
| F6 | FINDING | FN17; dated margin and industry targets; register below. Lexicon hit "will also be hosted" (L33) is filing boilerplate; "PAT will be INR 158M" (L260, L387) is arithmetic, not a commitment. |
| F7 | FINDING | FN02: "one-off Revenue mix impact" (L374) pre-frames gross-margin compression as transitory. No other lexicon hits outside the confidentiality boilerplate ("might constitute", L76). |
| F8 | FINDING | FN06: reported ETR 11.8-18.2% vs 25.17%, fully explained by the untaxed earnout; ex-earnout ETR 25.1-25.9%. |
| F9 | N.A. | Deck carries no OCI. |
| F10 | N.A. | Deck carries no EPS, share count or paid-up capital. |
| F11 | N.A. | Deck carries no balance sheet or net worth. |
| F12 | N.A. | Deck carries revenue shares only, no segment assets or liabilities (revenue-mix forensics at FN12). |
| F13 | N.A. | No board outcome in a presentation. |
| F14 | FINDING | FN03, FN05, FN09, FN11, FN15, FN16. |
| F15 | FINDING | FN14: Altek Electronics renamed Cyient DLM Electronics Inc. (L192). |
| F16 | FINDING | FN01, FN04, FN07, FN08, FN10, FN12, FN13, FN18. Prior-deck diff (dropped metrics, axis changes) not assessable: no prior extract. |
| F17 | N.A. | Concall-specific; this is a presentation. Notion test coverage annex below is for A4, not a silence score. |

## 3. COMMITMENT REGISTER (F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| EXPAND stage margins ~11-13% ("same stack, new sectors") | FY27-FY29 | p7 slide 6, L150, L165 | initiated (window opened FY27; H1 FY27 EBITDA 9.6%) |
| TRANSFORM stage margins ~13-18% ("B2S platform moat") | FY30+ | p7 slide 6, L150, L165 | initiated (stated target) |
| Go from 4 to 7 industries: +Semicon Cap Equipment, Robotics, AI Data Center | FY27-FY29 | p7 slide 6, L153-161 | underway ("Expanding into", L192) |
| New platforms / "Expanded Electronic Product Capabilities" | FY30+ | p7 slide 6, L162 | initiated |
| Altek Electronics integration, renamed Cyient DLM Electronics Inc. | by Q2 FY27 | p8 slide 7, L192-194 | completed |
| Build next growth engines (AI/data-center, robotics, semicap) and strengthen B2S | undated | p8 slide 7, L191-194 | underway |
| Continued investment into sales, strategy and capabilities (cost line) | ongoing | p11 L255-257; p14 L378-379; p16 L434-436 | underway |

## 4. NOTION TEST COVERAGE IN THIS DECK (annex for A4; F17 is N.A.)

| Notion test | Deck evidence | State |
|---|---|---|
| 1 Cash falsifier (NWC <=120 by Q4 FY27 with positive CFO; >161 confirms) | NWC 161 (Q1'27), 153 (Q2'27), L305-311; OpFCF 172 Mn, L325; no CFO | Not triggered either way on deck basis; basis mismatch with FY26 169 (FN08); CFO NOT FOUND |
| 2 Gross margin third quarter of compression without component-cost explanation | GM -226 bps (Q1) and -379 bps (Q2) YoY; explanation "one-off Revenue mix" and "product development" purchases, L374-375 | Two quarters visible; not a component-cost explanation; quarter count needs prior logs (FN01-FN03) |
| 3 Order book Rs 2,600 Cr, 1.5x at Q1 | 28,137 Mn (Rs 2,813.7 Cr), 1.6x, L229, L179 | Book rising; test not triggered |
| 4 Proof gate (design-led share double digits two quarters; >=100 bps EBITDA uplift) | B2S share undisclosed (L361); EBITDA -135 bps YoY (L230) | Not fired; design-led share not measurable from deck (FN12) |
| 5 Related-party flow to parent Cyient Ltd | No mention in deck | Silent in deck |
| 6 Standalone vs consolidated divergence (India vs Altek) | Basis unstated (L371); India mix 7% (L359); Altek renamed (L192); earnout 182 Mn (L385) | Partial; FN05, FN14, FN15, FN18 |

```yaml
stage: A3-forensics
company: "CYIENTDLM"
quarter: "q2fy27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/cyientdlm-q2fy27/work/forensics_presentation_cyientdlm_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: FINDING
  F16: FINDING
  F17: N.A.
findings:
  - {id: "FN01", check: "F16", line: "L255-257 p11; L375-381 p14", classification: "FORWARD-SIGNAL", implication: "Deck blames margin on opex investment; table shows material ratio +379 bps, opex -245 bps; margin loss is a material-cost cause"}
  - {id: "FN02", check: "F7", line: "L374-375 p14; L186 p8", classification: "FORWARD-SIGNAL", implication: "DMC rise labelled one-off mix while Box Build +86% is the stated strategy; compression may be structural to the mix shift"}
  - {id: "FN03", check: "F14", line: "L430-431 p16", classification: "AMBIGUOUS", implication: "'Mainly Q2' hides Q1 FY27 material ratio +226 bps YoY; two consecutive YoY gross-margin compressions"}
  - {id: "FN04", check: "F16", line: "L146, L165 p7; L229-230 p10", classification: "FORWARD-SIGNAL", implication: "Q2 EBITDA 8.7% below deck's own today band 9-11% in year 1 of 11-13% target; margin metric undefined; proof gate not met"}
  - {id: "FN05", check: "F14", line: "L384-385 p14; L447-449 p16; L192 p8", classification: "FORWARD-SIGNAL", implication: "Recurring 'one-off' earnout reversal = 53.5% of Q2 reported PAT; implies Altek missed earn-out; goodwill test FY27; 182 Mn base for Q2 FY28"}
  - {id: "FN06", check: "F8", line: "L387-388 p14; L446-447 p16", classification: "NEUTRAL-FACT", implication: "Reported ETR 11.8-18.2% is the untaxed earnout; ex-earnout ETR 25.1-25.9%; no shield"}
  - {id: "FN07", check: "F16", line: "L305-315, L287-292 p12", classification: "FORWARD-SIGNAL", implication: "Customer advance days 33 to 13 over four quarters, DPO 83 to 68; NWC +14 days YoY despite DIO -10; growth absorbs more working capital"}
  - {id: "FN08", check: "F16", line: "L284, L305-311 p12", classification: "AMBIGUOUS", implication: "Deck NWC basis (Q4'26 145) differs from Notion FY26 169; falsifier test 1 needs basis ruling; Q1'27 printed 161 at the confirm line"}
  - {id: "FN09", check: "F14", line: "L381-382 p14; L442-443 p16", classification: "AMBIGUOUS", implication: "Lower working-capital borrowings while NWC days and revenue rose; funding source of NWC unstated"}
  - {id: "FN10", check: "F16", line: "L325 p12", classification: "AMBIGUOUS", implication: "OpFCF 172 Mn undefined, unresolved asterisk, no H1 or prior figure; not CFO"}
  - {id: "FN11", check: "F14", line: "L250, L253, L256, L267, L271 p11", classification: "AMBIGUOUS", implication: "Q3'26 34 Mn EBITDA one-off unexplained; 'EBITDA % Normalized' 10.2% includes it (normalized 9.1%); PAT chart not split"}
  - {id: "FN12", check: "F16", line: "L353-362 p13", classification: "AMBIGUOUS", implication: "Growth withheld for Cables, Mech & Others (holds B2S), Auto & Others; residual product buckets implied down ~12-28% YoY; B2S share undisclosed"}
  - {id: "FN13", check: "F16", line: "L153-161 p7", classification: "AMBIGUOUS", implication: "One of '+3 NEW' industries (Semicon Cap Equipment) is carved from foundation 'Industrial/Semicon'; no revenue line for any new industry"}
  - {id: "FN14", check: "F15", line: "L192-194 p8", classification: "AMBIGUOUS", implication: "Altek renamed Cyient DLM Electronics Inc.; earn-out closure, residual contingent consideration and separate reporting unknown"}
  - {id: "FN15", check: "F14", line: "L242 p11; L371, L427; L374, L430", classification: "NEUTRAL-FACT", implication: "Tables do not state consolidated/standalone; marker 1 unresolved; DMC % discussed but never printed"}
  - {id: "FN16", check: "F14", line: "L115-116, L127-129, L140 p6", classification: "NEUTRAL-FACT", implication: "Market-size arithmetic does not tie (robotics ~96 vs 111 Bn; upside ~1.04 vs 1.1 Tn); mixed sources; low weight"}
  - {id: "FN17", check: "F6", line: "L146-165 p7; L191-194 p8", classification: "FORWARD-SIGNAL", implication: "Dated targets 11-13% FY27-29, 13-18% FY30+, 7 industries FY27-29 enter the Role 5 tracker; H1 FY27 EBITDA 9.6%"}
  - {id: "FN18", check: "F16", line: "L359-361 p13", classification: "NEUTRAL-FACT", implication: "India 7% of revenue, ROW 93%; no prior mix in deck; A4 compares for Notion test 6"}
forward_signals: ["FN01", "FN02", "FN04", "FN05", "FN07", "FN17"]
ambiguous: ["FN03", "FN08", "FN09", "FN10", "FN11", "FN12", "FN13", "FN14"]
commitments:
  - {commitment: "EXPAND stage margins ~11-13%", implied_date: "FY27-FY29", ref: "p7 slide 6 L150, L165", status_word: "initiated"}
  - {commitment: "TRANSFORM stage margins ~13-18% (B2S platform moat)", implied_date: "FY30+", ref: "p7 slide 6 L150, L165", status_word: "initiated"}
  - {commitment: "4 to 7 industries: Semicon Cap Equipment, Robotics, AI Data Center", implied_date: "FY27-FY29", ref: "p7 slide 6 L153-161; p8 L192", status_word: "underway"}
  - {commitment: "New platforms / Expanded Electronic Product Capabilities", implied_date: "FY30+", ref: "p7 slide 6 L162", status_word: "initiated"}
  - {commitment: "Altek integration, renamed Cyient DLM Electronics Inc.", implied_date: "by Q2 FY27", ref: "p8 slide 7 L192-194", status_word: "completed"}
  - {commitment: "Build AI/data-center, robotics, semicap engines; strengthen B2S", implied_date: "undated", ref: "p8 slide 7 L191-194", status_word: "underway"}
  - {commitment: "Continued investment in sales, strategy, capabilities", implied_date: "ongoing", ref: "p11 L255-257; p14 L378-379; p16 L434-436", status_word: "underway"}
gate_a3: pass
blank_checks: []
analyst_note: "Two findings carry the weight. First, gross margin: material cost rose 226 bps (Q1) and 379 bps (Q2) YoY, while the deck credits the margin to opex investment (p11) and calls the mix 'one-off' (p14). Opex leverage masked Q1. If Box Build's +86% raises material intensity, the 11-13% EXPAND target needs a lever the deck does not name. Second, earnings quality: the earnout reversal is over half of Q2 reported PAT, recurs each Q2, and implies Altek missed its earn-out. It lands as Altek is renamed, so goodwill and residual consideration are open. Cash: advance days fell 33 to 13 as the book hit a record; on the deck basis NWC is 153, and the Notion 169 sits on another basis, so test 1 needs a basis ruling. All chart periods were tied by arithmetic (H1 sums, NWC identity), not position. Industry pie slices were left unassigned. Bull side: book +22.8% YoY, 1.6x book-to-bill ties to implied inflow, DIO -10 days, other expense -269 bps."
```
