# A3 FORENSIC NOTES: Heritage Foods (HERITGFOOD) Q2 FY27, doctype CONCALL (ASR transcript, call 16 Oct 2026)

Agent: A3 forensic notes | model: claude-opus-5-5 | run date 2026-10-19
Inputs read: A1 structured `runs/heritgfood-q2fy27/extracted/heritgfood-concall-q2fy27-structured.md`; A1 fulltext `runs/heritgfood-q2fy27/extracted/heritgfood-concall-q2fy27-fulltext.md` (lines 1-853, all read); A2 ledger `runs/heritgfood-q2fy27/work/ledger_concall_heritgfood_q2fy27.md`; F17 checklist substitute: `runs/heritgfood-q2fy27/work/review_heritgfood_q2fy27.md` lines 690-761 (Step 8.5, 34 questions; Monitorables M1-M14).
Not read: source audio or transcript file, anything under `inputs/`. Prior-quarter fulltext: ND (none supplied). No Notion page (PRE-THESIS READ).
Evidence tier: [MGMT, ASR]. Speakers mostly unattributed. Garbled numbers treated as ASR artefacts unless context confirms them. Filings win on any conflict. "L" = fulltext line. "[derived]" = arithmetic on cited numbers. "[INFERENCE]" = reasoned, not stated.

---

## 0. LEDGER RECONCILIATION

| Category | Ledger rows | Read at cited fulltext line | Result |
|---|---|---|---|
| NUMBER | 162 (R001-R162) | 162 | all quotes found at or across the cited line |
| ENTITY | 52 (R163-R214) | 52 | found |
| FORWARD | 60 (R215-R274) | 60 | found |
| DATE | 20 (R275-R294) | 20 | found |
| QUALIFIER | 42 (R295-R336) | 42 | found |
| Total | 336 | 336 | ledger_reconciled_pct = 100 |

Method: every fulltext line from 115 to 853 was read in full (the row-bearing span; lines 1-114 are the A1 header and turn map). Each R### was checked against its cited line. Quotes that wrap a line break (R089 L476-477, R336 L774-775) were read across both lines.

Ledger notes (non-material, no row affected):
- Ledger Section 9 C5 cites turn T055 for R125; Ledger Section 4 and the turn map place R125 (L631) in T054.
- Ledger Section 9 C6 cites T045 for R089/R090; Section 4 places them in T032 (L477), which matches the turn map (T032 = L468-487).
- R140 "70%" (L725) is an analyst figure; context ("can we go to 70% over let's say next 2-3-4 quarters") makes it an ASR artefact for a single-digit margin. Not used.
- R107 "405%" (L568): context ("adding 1 amule size", 75-80k Cr on a 14 lakh Cr industry, L567-571) implies about 5.4-5.7% growth [derived]. Treated as ASR artefact.

---

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| CC-A3-01 | F6 | R230, R253, R121, R326, R110, R111 | L381; L618; L620-621 | "in Q3 at this point in time I think that 11% kind of thing might continue" / "we don't think it will go from 47 to 50 rupees in a quarter" / "average milk procurement price was about 45.55" | FORWARD-SIGNAL | The two statements cannot both hold. 11% YoY on the stated Q3 FY26 base of Rs 45.55 is Rs 50.56/L [derived], above Rs 50. Q2 cost Rs 47.73 is only 4.8% above that base [derived]. Separating observation: Q3 FY27 landed cost at or above Rs 50.5/L confirms the L381 reading (+Rs 2.83/L QoQ); below Rs 50 confirms L618. |
| CC-A3-02 | F6 | R251, R112, R115 | L602-604 | "whatever is EBITDA now is not going to come down because the consumer prices have been increased" | FORWARD-SIGNAL | Dated floor promise for Q3 FY27: Q2 base is EBITDA Rs 74.0 Cr at 5.6% (R005, R006, L163-164). Basis (margin or absolute) not stated; track both. Same answer block hedges it: "possible that we might see ... continued inflation" (L622). |
| CC-A3-03 | F6 | R244, R245, R246, R247, R218 | L479-486; L227-229 | "we had capitalized some large projects and those depreciation is also impacting the P and L" / "another thing that we should keep playing out in the subsequent quarters" / "newly commissioned ice cream facility ... supporting capacity absorption" | FORWARD-SIGNAL | Management concedes PBT/PAT will lag EBITDA in coming quarters ("EBITDA improvement sequential is far better than PVT or VAT", L481-482). New capacity is still being absorbed. No project in progress was named, so the CWIP build (A4 Q2) adds a further D&A step not addressed on the call. Bear lean on FY27 PAT growth. |
| CC-A3-04 | F6 | R226, R227, R070, R256, R308, R309 | L364-367; L638-639 | "the benefit of it will accrue in quarter three" / "In October, we have opened the month with much higher price levels than we had in Q2" / "Based on that, we will take a call" | FORWARD-SIGNAL | Q3 margin rests on the carry-in of September hikes ("much higher than 8%", L364-365, unquantified). No liquid-milk % or effective date given; a new Q3 hike is undecided. Partly answers A4 Q1. Ask: liquid-milk price per litre at 1 Oct vs Q2 average. |
| CC-A3-05 | F6 | R232, R233, R234, R285, R079, R080 | L396-403 | "this is going to take effect only from 1st of November" / "once the KMF takes up the prices of nandini milk we'll also be able to pass on much better to the consumer in Bangalore city" | FORWARD-SIGNAL | Dated third-party catalyst, 1 Nov 2026. Sales-side only: "our procurement footprint in Karnataka is not significant" (L400-401). Track Heritage Bangalore milk price action in November 2026. |
| CC-A3-06 | F6 | R248, R094, R085, R287 | L523-527; L428 | "As far as ghee is concerned you will see that the volume growth has been flat" / "ghee volumes will have a bumper growth coming into Q3" / "close to about 20 percentage revenue increase in gee" | FORWARD-SIGNAL | Q2 ghee growth was price-led (about 20% revenue on flat volume [derived]). Q3 ghee volume is a dated promise tied to Dasara/Diwali timing. If Q3 ghee volume is flat again, the price-elasticity reading in A4 Q17 turns bear. |
| CC-A3-07 | F6 | R257, R258, R291, R292, R053-R057 | L700-709 | "we had a difficult quarter one due to the very, very high cost of the ingredients" / "in September we had taken a very good price hike in all the verticals including our integration as well as the outside general trade market" / "strengthen our PVT during rest of the year in H2" | FORWARD-SIGNAL | Answers A4 Q9: input cost, price hike taken. NutriVate PBT margin Q1 2.6%, Q2 4.3%, H1 3.5% [derived: 19/728, 37/853, 56/1,581 Rs m]. H2 PBT improvement is the tracked promise. "integration" confirms an intra-group channel exists (A4 Q6 split still open). |
| CC-A3-08 | F6 | R149-R154, R265-R268, R293, R294, R334, R335 | L770-774 | "in the next 6 or 7 years we want to get to 500 crores of revenue" / "close 200 crores, so 170, 180 crores" / "in five, six years to get to 500 crores" | AMBIGUOUS | Two horizons and two FY27 bases in one answer. Implied CAGR to Rs 500 Cr is 14% to 24% [derived], against 55-82% growth from "110 crores" last year (L771) [derived]. Either the target is conservative or a sharp slowdown is planned. Ask: FY27 own ice cream revenue, the base year of the 500 Cr vision, and whether supply to Get-A-Way is inside it (see CC-A3-17). |
| CC-A3-09 | F6 | R260, R261, R142, R143, R144 | L727-733 | "employee expenses of percentage of revenue has come down by about 1%. Operating expenses has come down by about 0.6% ... freight also has come down by about 0.1%. So, the only expense which is going up is the raw material" | AMBIGUOUS | Period not stated. If QoQ: a 1.7 pp cost fall against +0.98 pp EBITDA implies raw material up about 0.7 pp of revenue QoQ [derived], which conflicts with the +63 bps QoQ gross-margin gain in A4 (review Q34). If YoY: implies raw material up about 3.0 pp YoY [derived, using op EBITDA 6.94% to 5.61%, review Q4]. A4 ties the ratios to the filed P&L. |
| CC-A3-10 | F6 | R237, R238, R242, R081, R082, R125-R128, R328, R329 | L411-418; L475; L631-633 | "No, we won't have to" (pass back on a cost fall) / "if procurement prices come go up, we will again take consumer prices" / "procuring about 1.8 million liters per day so a 50 price day you know roughly translates to almost 3 crore improvement in bottom line per month right at a 400 to 450 crores of revenue" | NEUTRAL-FACT | Management states a one-way price ratchet and gives its own sensitivity. The "0.7 percent" (L417) is margin points on revenue, not % of PAT. On Q2 volume (17.28 LLPD, 92 days) Rs 1/L of procurement cost = Rs 15.9 Cr = 1.2 pp of Q2 revenue Rs 1,319.6 Cr [derived]. The +Rs 2.83/L path in CC-A3-01 is worth about 3.4 pp before price action [derived]. Feeds Role 1 sensitivity. |
| CC-A3-11 | F7 | R313, R325, R252, R254, R241, R228, R229, R231, R223, R224, R071 | L469; L605; L622; L432-433; L372-375; L296-299 | "that is a very speculative question" / "The only thing we are not willing to speculate is if the raw milk prices will come down in the flush" / "it is possible that we might see you know inflation, continued inflation" / "we are hoping that post Diwali there is a little bit of a cooling effect" / "slight increase of procurement prices in October compared to September" | FORWARD-SIGNAL | Management declined to call the cycle three times. The relief case rests on "hoping" and a weather conditional ("might be stable if the good monsoon states perform well", L298-299). The only hard October data point is a cost increase (L375). Southern drought is in management's own description (L283-285). Lean bear on Q3 procurement cost. |
| CC-A3-12 | F7 | R319, R093, R320, R135-R138, R332, R333 | L508-509; L520-521; L527; L715-719 | "I don't think that you should deep dive too much into you know each at a product level" / "between ghee, paneer and curd is about 90% of everything they sell or 95% at 90%" / "please don't use that graph to calibrate" / "at a very high level I can say" | AMBIGUOUS | Management steered analysts away from the slide price/volume data. The 90% cannot be a revenue share: curd Rs 320 Cr + paneer Rs 200-230 Cr + ghee Rs 350 Cr annualised (L716-719) = Rs 870-900 Cr, about 40-42% of annualised broader VAP Rs 2,163 Cr (Rs 5,408 m x 4, L211) [derived]. Paneer "1200" (L717) is likely ASR. Ask: what the 90% measures, and Q2 revenue by curd, paneer, ghee, ice cream. |
| CC-A3-13 | F7 | R316, R188, R192, R193 | L492-497; L393-395 | "it is very unfair to ask us a question on cooperators because we have, we do not know the inner workings of cooperators" | AMBIGUOUS | Management cited Aavin and KMF price moves to argue pricing headroom (L393-403), then declined to discuss cooperative behaviour. Aavin's farm-price rise of about Rs 6/L, "unprecedented at the farm level" (L395), is in cow-milk belts that include Southern Andhra (L682-683). Ask: Heritage farm-gate price vs Aavin in overlapping catchments, Q2 and October. |
| CC-A3-14 | F6 | R272, R273, R162, R214, R225 | L306-309; L441-443; L816-817; L822-823 | "even tying up with the funds for overcoming their requirements of working capital" / "we supply subsidized cattle feed very conveniently to them" / "We also facilitate a lot of third-party lending to ... meet with their working capital requirements and also for them to increase their herd" | AMBIGUOUS | Procurement security leans on feed subsidy and facilitated farmer credit. Who bears the subsidy cost (Heritage or NutriVate), and whether Heritage gives any guarantee or first-loss cover on third-party loans, are not stated. Ask both; check FY27 AR contingent liabilities (M10). |
| CC-A3-15 | F15 | R050, R176, R177, R336 | L229-230; L232-233; L774-775 | "Getaway, in which we now hold 71 percent stake" / "Heritage Novandee Foods now a wholly owned subsidiary" / "this is the excluding getaway, because that's a subsidiary company" | AMBIGUOUS | "now" signals a holding change on both entities. No prior-quarter list (ND) to diff against. A4 cross-checks against the results Annexure 1 entity list and the Rs 4.04 Cr NCI (review Q15, Q32). |
| CC-A3-16 | F17 | R091, R197, R317, R318, R130-R132 | L500-502; L651-654; L686-688 | "Kaunulk accounts for 80 percent of procurement, do you mean price or volume?" / "Volume. Volume. Volume dependent." / "the significant inflationary trend we have seen also is in the hardcore cow milk" | FORWARD-SIGNAL | Partly answers A4 Q29. "Kaunulk" read as "cow milk" [INFERENCE: ASR; A4 Q29 states cow is about 80% of procurement]. Cow milk is about 80% of procurement by volume and is the more inflationary species ("cow meat is becoming dearer now", L677). This leans to the bear reading of slide 9 (cow = the higher-inflation series). Per-litre cost by species still not given. |
| CC-A3-17 | F17 | R051, R084, R336, R149-R153 | L229-232; L427; L774-775 | "Heritage manufacturing and supplying 3,272 liters of ice cream per day to support its growth" / "ice cream's has got more than 200 rupees per liter of revenue" | AMBIGUOUS | Intra-group ice cream supply is about Rs 24 Cr a year at Rs 200/L [derived: 3,272 x 365 x Rs 200 = Rs 23.9 Cr; transfer price NOT FOUND]. If it sits inside own ice cream revenue of Rs 170-180 Cr, about 13-14% eliminates on consolidation [derived]. Bears on the VAP basis question (A4 Q19, Q31). |
| CC-A3-18 | F17 | R009, R010, R015, R016, R087, R088, R314 | L179; L191; L471; L529-532 | "milk procurement volumes increased 7% year-on-year to 17.28 lakh liters per day" / "Milk sales volumes increased 2% year on year to 12.35 lakh liters per day" / "we have been able to take up consumer prices and sustain volumes" | AMBIGUOUS | Procured milk not sold as liquid milk rose from about 4.04 to 4.93 LLPD YoY (+22%) [derived]. The call says ghee is "100 percent" consumer packs (L531), so bulk ghee is ruled out; SMP and bulk use are not addressed (A4 Q10 partly). The "sustain volumes" claim holds for liquid milk only at 2% (1% in H1, L193). |
| CC-A3-19 | F17 | R145, R272 | L741-743; L805-807 | "you've shown a 6% CAGR on milk procurement ... do you believe that that's adequate" / "we are at a good speed to secure our procurement volumes" | AMBIGUOUS | The analyst repeated the slide 17 6% CAGR. Management did not correct it and gave no number. A4 Q30 (6% vs 1.6% CAGR; FY26 procurement fall) stays open. Management also said it is "not expanding geographically" (L777), so procurement growth must come from existing catchments. |
| CC-A3-20 | F17 | R295, R312 | L845 | "due to time constraint that was the last question for today" | NEUTRAL-FACT | 26 of 34 A4 questions got no answer. No analyst asked about CWIP, subsidiary P&L, tax, cash flow, impairment or the balance sheet. All 24 analyst questions were about pricing, procurement, mix, competition or ice cream. This silence is not evasion, but the open items still need the IR email. |
| CC-A3-21 | F17 | R166, R310 | L147; L371-372 | "I now invite Dr. Rao to present the company's business outlook and performance" | NEUTRAL-FACT | The Whole-Time Director (R166) gave the opening remarks on the call. This is a third presenter beside the deck (independent Chairperson) and release (Executive Director) in A4 Q22. A4 Q22 stays open. |

Counts: 21 findings. FORWARD-SIGNAL 9 (CC-A3-01, 02, 03, 04, 05, 06, 07, 11, 16). AMBIGUOUS 9 (CC-A3-08, 09, 12, 13, 14, 15, 17, 18, 19). NEUTRAL-FACT 3 (CC-A3-10, 20, 21). CONFIRMATORY-NEGATIVE 0 (no prior quarter, so no sustained silence can be shown).

---

## 2. CHECKLIST SCORECARD

| Check | Status | Basis |
|---|---|---|
| F1 Zero-value standing items | N.A. | Concall; no ZERO_STANDING rows in ledger; no financial-statement template. |
| F2 Standalone vs consolidated | N.A. | Concall gives consolidated headline only (R299, L159); no S-vs-C tables. Intra-group supply fact routed to CC-A3-17 (F17). |
| F3 Shell-entity detection | N.A. | No cost lines by entity on the call. |
| F4 Unaudited contribution ratio | N.A. | No auditor Other Matters paragraph on a call. Open as A4 Q8 (silent, see F17). |
| F5 Going concern / EoM scope | N.A. | No EoM language on a call; prior fulltext ND. |
| F6 Forward-commitment mining | FINDING | 24 commitments registered (Section 3); CC-A3-01 to 10 and 14. |
| F7 Hedge mining | FINDING | CC-A3-11, 12, 13: three refusals to speculate, granularity deflection, cooperative decline. |
| F8 Tax forensics | N.A. | No tax figures on the call. A4 Q11 (ETR) silent. |
| F9 OCI forensics | N.A. | No OCI on the call. |
| F10 Share count and dilution | N.A. | No share capital, EPS or ESOP mention. |
| F11 Reserves and net worth | N.A. | No net worth figure on the call. |
| F12 Segment forensics | N.A. | No segment assets or liabilities. Feed segment P&L comment routed to CC-A3-07. |
| F13 Board outcome | N.A. | No board, AGM, dividend or director item on the call. |
| F14 Note drafting inconsistencies | N.A. | No notes or auditor letter. ASR name misspellings are engine artefacts (A1 header L21-29), not drafting. In-call number conflicts handled in CC-A3-08, 12. |
| F15 Entity list diffs | FINDING | CC-A3-15: "now hold 71 percent" (L229) and "now a wholly owned subsidiary" (L232-233). Prior list ND, so change is flagged, not confirmed. |
| F16 Presentation dropped/reframed | N.A. | Not a presentation. Deck slides referred to on the call (slides 9, 17) are handled under F7/F17. |
| F17 Silence audit | FINDING | 34 questions: 1 answered, 7 partly, 26 silent. 14 monitorables: 2 answered, 5 partly, 7 silent. CC-A3-16 to 21. |

Blank checks: none. GATE A3: pass.

---

## 3. COMMITMENT REGISTER (F6)

| # | Commitment | Implied date | Turn / line / row | Status word |
|---|---|---|---|---|
| K1 | Staggered Q2 consumer price hikes; benefit accrues in Q3 | Q3 FY27 (Oct-Dec 2026) | T014, L364-366, R226 | underway |
| K2 | October opened at much higher consumer price levels than Q2 | Oct 2026 | T014, L367, R227 | completed |
| K3 | Q3 price hike decision: "we will take a call" | Q3 FY27 | T056, L638-639, R256 | initiated (decision pending) |
| K4 | Q3 procurement inflation: "11% kind of thing might continue" | Q3 FY27 | T016, L381, R230 | expectation |
| K5 | Procurement will not go from Rs 47 to Rs 50 in a quarter | Q3 FY27 | T051, L618, R253 | expectation (conflicts with K4, CC-A3-01) |
| K6 | EBITDA "is not going to come down" | Q3 FY27 onward | T049, L603-604, R251 | expectation (strong) |
| K7 | Operating leverage in Q3 better than Q2 | Q3 FY27 | T032, L485-486, R246/R247 | expectation (strong) |
| K8 | VAP contribution continues to expand in Q3 ("15 days into the quarter") | Q3 FY27 | T032, L476-478, R243 | underway |
| K9 | Ghee "bumper growth coming into Q3", already seen in first 15 days | Q3 FY27 | T041, L525-527, R248 | underway |
| K10 | Depreciation from large projects capitalised early FY27 keeps weighing in subsequent quarters | FY27 | T032, L479-483, R244 | completed (capitalised); impact ongoing |
| K11 | New ice cream facility commissioned; capacity absorption | done by Q2 FY27 | T003, L227-229, R218 | completed |
| K12 | Karnataka consumer milk +Rs 8/L effective 1 Nov; Heritage to pass on in Bangalore after KMF moves | 1 Nov 2026 | T022, L396-403, R232-R234, R285 | initiated (third-party trigger) |
| K13 | Will raise consumer prices again if procurement rises | conditional | T032, L475, R242 | standing |
| K14 | No consumer price pass-back when milk prices fall | conditional | T026, L411-418, R237/R238 | standing |
| K15 | Margins back to steady state if raw material falls | conditional | T073, L738-739, R264 | expectation |
| K16 | NutriVate passes input inflation on in Q3 and Q4; strengthens PBT in H2 | H2 FY27 | T067, L706-709, R257/R258 | initiated (September hike) |
| K17 | Own ice cream revenue Rs 500 Cr (excl Get-A-Way) in 5-7 years; FY27 Rs 170-200 Cr | FY32-FY34 [derived from FY27 + 5-7 yrs] | T076, L770-775, R265-R268 | underway |
| K18 | Exports (12 countries, 0.5% of revenue) to grow | undated | T076, L778-781, R270 | underway |
| K19 | No geographic expansion; "going deeper" | standing | T076, L777-778, R269 | standing |
| K20 | Milk availability may improve after Diwali; stable if good-monsoon states compensate | Nov 2026 | T006, L296-299, R223/R224 | expectation |
| K21 | Buffalo flush and post-Diwali cooling of procurement prices | Nov-Dec 2026 | T014/T016, L372-374, L383, R228/R229/R231 | expectation (hope) |
| K22 | Farmer engagement to improve milk availability; double farmer income "every few years" | undated | T006/T078, L310, L809-810, R225, R273 | underway |
| K23 | Q2 launches: Nourish+ high protein curd, Greek yogurt packs, organic curd, Alpenvie range | Q2 FY27 | T003, L219-222, R172-R174 | completed |
| K24 | Get-A-Way 71% held; Heritage Novandie wholly owned | as at call | T003, L229-233, R050, R176, R177 | completed (state; see CC-A3-15) |

Role 5 tracker priority (Q3 FY27 results, by 14 Feb 2027 [INFERENCE: Reg 33]): K4 vs K5 (landed cost per litre), K6 (EBITDA margin vs 5.6% and absolute vs Rs 74.0 Cr), K7, K9 (ghee volume), K16 (NutriVate PBT margin vs 4.3%).

---

## 4. F17 SILENCE AUDIT

### 4A. A4 Questions for Management (34) vs the call

Status: ANSWERED / PARTLY / SILENT. Silent items carry "quarters silent: 1 (prior ND)".

| Q | Topic (short) | Status | Concall line(s) | Note |
|---|---|---|---|---|
| 1 | Liquid-milk price increase since 30 Sep (% and date) | PARTLY | L364-367; L402-403; L638-639 | Sept hikes "much higher than 8%"; October "much higher price levels"; no liquid-milk % or date; Q3 hike undecided. |
| 2 | CWIP Rs 127.58 Cr: project, cost, COD | SILENT | (L479-481 adjacent) | Only "capitalized some large projects" at start of year. No project in progress named. 1 (prior ND). |
| 3 | Novandie and Get-A-Way Q2 revenue and PBT | SILENT | (L229-235 qualitative) | "robust revenue growth", "top five brands"; no numbers. 1 (prior ND). |
| 4 | Quarter when YoY margin turns positive | PARTLY | L603-604; L736-739 | EBITDA floor and "steady-state" if milk falls; no quarter named (A4 bear answer). |
| 5 | VAP categories above 85% utilisation | SILENT | (L228-229 "capacity absorption") | No utilisation figure. 1 (prior ND). |
| 6 | Feed sales to group companies | SILENT | (L704, L816 adjacent) | "integration" vertical and "subsidized cattle feed" named; no split. 1 (prior ND). |
| 7 | Rs 7.20 Cr invested in subsidiaries: which line | SILENT | none | 1 (prior ND). |
| 8 | Subsidiary not reviewed by auditor | SILENT | none | 1 (prior ND). |
| 9 | Feed margin fall: cost or price | ANSWERED | L700-705 | Ingredient cost; price hike in September in all verticals (A4 bull answer). |
| 10 | LLPD into SMP or bulk fat | PARTLY | L529-532 | Ghee "100 percent" consumer packs; SMP and LLPD not given. |
| 11 | Standalone ETR 26.39% | SILENT | none | 1 (prior ND). |
| 12 | GST flavoured-milk order final or appealed | SILENT | none | 1 (prior ND). |
| 13 | HNFL public conversion: stake sale or raise | SILENT | none | 1 (prior ND). |
| 14 | HNFL carrying value; impairment headroom | SILENT | none | 1 (prior ND). |
| 15 | Entity carrying Rs 4.04 Cr NCI | PARTLY | L229-230; L774-775 | Get-A-Way "now" 71% held and "a subsidiary company"; NCI entity not named; buy-out terms not stated. |
| 16 | FY28E VAP share and gross margin targets | SILENT | none | Only the ice cream Rs 500 Cr vision given (L770). 1 (prior ND). |
| 17 | Products that lost volume in Q2 | PARTLY | L522-524 | "except in the case of ghee" volume sustained; ghee flat; no full list. |
| 18 | Other financial liabilities, Rs 19.63 Cr | SILENT | none | 1 (prior ND). |
| 19 | VAP Rs 451.0 Cr: standalone or consolidated | SILENT | (L476-477; L774-775 adjacent) | Management repeats "+4.1 percent" (same as printed); basis not stated. Own ice cream stated excl Get-A-Way. 1 (prior ND). |
| 20 | Net debt definition | SILENT | none | 1 (prior ND). |
| 21 | Milk revenue growth outside Telangana | SILENT | (L510-511 illustrative only) | "I'm just making it up" example. 1 (prior ND). |
| 22 | Author of results commentary | SILENT | (L147) | WTD Dr. Rao presented on the call (CC-A3-21). 1 (prior ND). |
| 23 | FY25 exceptional Rs 8.7 Cr; JV status | SILENT | none | 1 (prior ND). |
| 24 | Missing highlight item 04 | SILENT | none | 1 (prior ND). |
| 25 | Negative consolidated interest income | SILENT | none | 1 (prior ND). |
| 26 | +Rs 8.50 Cr investing cash flow H1 FY26 | SILENT | none | 1 (prior ND). |
| 27 | Slide 8 EPS basis | SILENT | none | 1 (prior ND). |
| 28 | Rs 3.4 Cr FY26 schedule gap | SILENT | none | 1 (prior ND). |
| 29 | Slide 9 species mapping; cost by species | PARTLY | L500-502; L651-654; L677; L686-688 | Cow about 80% of procurement by volume; cow the more inflationary species (CC-A3-16); no Rs/L by species; no October easing. |
| 30 | 6% vs 1.6% procurement CAGR; FY26 fall | SILENT | (L741-743, L805-807 adjacent) | Analyst repeated 6%; management did not correct or reconcile (CC-A3-19). 1 (prior ND). |
| 31 | Price increase by product; subsidiary share of VAP | PARTLY | L357-358; L790-795; L774-775 | Overall about 8%, milk 6%, others 9-10%; curd about 10%, premium curd above 15%; subsidiary share not given. |
| 32 | Consideration for Novandie and Get-A-Way | SILENT | none | 1 (prior ND). |
| 33 | +Rs 10.98 Cr other financial liabilities in H1 OCF | SILENT | none | 1 (prior ND). |
| 34 | Cost per litre of the Rs 48.32 Cr FG/WIP drawdown | SILENT | none | 1 (prior ND). |

Tally: ANSWERED 1 (Q9) | PARTLY 7 (Q1, Q4, Q10, Q15, Q17, Q29, Q31) | SILENT 26. Total 34.
Top 3 A4 questions (Q1, Q2, Q3): Q1 partly, Q2 silent, Q3 silent.

### 4B. A4 Monitorables (M1-M14) vs the call

| M | Item | Status | Concall line(s) | Note |
|---|---|---|---|---|
| M1 | Q2 concall transcript | PARTLY | L115-127 | Call held 16 Oct 2026. Only the ASR transcript is in the corpus; a company-filed transcript is still pending. |
| M2 | Q3 FY27 gross-margin YoY gap, S-vs-C, CWIP | PARTLY | L381; L485-486; L603-604 | Qualitative Q3 statements only (K4-K7). No gross margin, S-vs-C or CWIP number. |
| M3 | VAP capacity expansion: CWIP capitalisation and COD | SILENT | (L227; L479-480) | Commissioned facility and capitalised projects only. 1 (prior ND). |
| M4 | Margin improvement via premiumisation, cost, leverage | ANSWERED | L727-739 | Cost ratios and operating leverage (period ambiguous, CC-A3-09). |
| M5 | Village-level procurement outreach | ANSWERED | L181-182; L437-451; L805-844 | Farmer adds, activation, volume per farmer, AI programmes, about 400 field staff (R162). |
| M6 | Strategic investments behind growth | PARTLY | L227-236 | Ice cream facility, Get-A-Way, Novandie named; no amounts. |
| M7 | Livo yogurt flavours ("Flavours next") | SILENT | (L234 Livo named) | No flavours timeline. 1 (prior ND). |
| M8 | FY27 impairment test (Rs 20.63 Cr) | SILENT | none | 1 (prior ND). |
| M9 | FY27 cash conversion; L592 inflow reversal | SILENT | none | 1 (prior ND). |
| M10 | FY27 AR items | SILENT | none | 1 (prior ND). |
| M11 | FY28E VAP share and gross margin values | SILENT | none | 1 (prior ND). |
| M12 | Unreviewed subsidiary status | SILENT | none | 1 (prior ND). |
| M13 | Q1 FY28 flush-season procurement cost | PARTLY | L372-374; L605 | Flush "expected"/"hoping"; management will not speculate. |
| M14 | Slide 9 species mapping | PARTLY | L686-688 | Cow is the more inflationary species; no Rs/L (CC-A3-16). |

Tally: ANSWERED 2 | PARTLY 5 | SILENT 7. Total 14.

### 4C. What Was NOT Discussed

| Item | Source | Consecutive quarters silent | Deteriorating metric? | Note |
|---|---|---|---|---|
| CWIP Rs 127.58 Cr project, cost, COD | A4 Q2, M3 | 1 (prior ND) | Yes (D&A +36.61%, interest +89.12% YoY per review Q2) | Top-3 question. Management named past capitalisation only. |
| Novandie and Get-A-Way P&L | A4 Q3, Q32 | 1 (prior ND) | Yes (acquired dairy businesses loss-making, review Q32) | Top-3 question. Promoted on the call without numbers (L229-235). |
| Unreviewed subsidiary | A4 Q8, M12 | 1 (prior ND) | Yes (loss rose QoQ, review Q8) | |
| Impairment headroom HNFL / goodwill | A4 Q14, M8 | 1 (prior ND) | Yes | |
| ETR above statutory | A4 Q11 | 1 (prior ND) | Yes (24.59% to 26.39%) | |
| Cash-flow tie-outs (Rs 7.20 Cr, Rs 10.98 Cr, Rs 27.01 Cr, Rs 8.50 Cr) | A4 Q7, Q18, Q26, Q33, M9 | 1 (prior ND) | Unknown | |
| GST order status | A4 Q12 | 1 (prior ND) | No | |
| HNFL public conversion | A4 Q13 | 1 (prior ND) | No | |
| FY28E targets | A4 Q16, M11 | 1 (prior ND) | No | |
| VAP basis (standalone vs consolidated) | A4 Q19 | 1 (prior ND) | No | Separating observation for L2-F1 not obtained. |
| Net debt definition; EPS basis; schedule gap; item 04; interest income; FY25 exceptional | A4 Q20, Q23-Q25, Q27, Q28 | 1 (prior ND) | No | Disclosure-care items. |
| Milk growth outside Telangana | A4 Q21 | 1 (prior ND) | Unknown | |
| Procurement CAGR conflict | A4 Q30 | 1 (prior ND) | Yes (FY26 procurement down 2.9%, review Q30) | Analyst raised 6%; not reconciled (CC-A3-19). |
| Inventory drawdown cost | A4 Q34 | 1 (prior ND) | Unknown | Bears on Q3 gross margin. |
| Livo flavours | M7 | 1 (prior ND) | No | |

Silence classification: no CONFIRMATORY-NEGATIVE. The run has one quarter only (prior ND), and no analyst asked these questions (CC-A3-20). Route all silent items to the IR email (Go India Advisors, per review L736) before /fttcp. Re-test at the Q3 FY27 call. A second quarter of silence on the CWIP and subsidiary P&L rows, both deteriorating, would meet the Role 5 confirmatory-negative test.

---

## 5. IN-CALL CONFLICTS (ledger Section 9) reviewed

| Ledger | Lines | A3 reading |
|---|---|---|
| C1 ice cream FY27 200 vs 170-180 Cr | L771-772 | Restated in the same breath; CC-A3-08. Use 170-180 (the correction) with 200 as upper bound. |
| C2 horizon 6-7 vs 5-6 yrs | L770, L774 | CC-A3-08. |
| C3 paneer 1200 vs 200-230 Cr | L717-718 | "1200" likely ASR; 200-230 Cr annualised used. |
| C4 90% vs 95% | L520-521 | CC-A3-12: neither fits a revenue share. |
| C5 1.8m vs 17.28 lakh L/day | L631 vs L179 | Within rounding of H1 17.69 lakh (L180); "very high level calculation" (L631). Not a finding. |
| C6 4.1% "in Q3" | L476-477 | ASR run-on: 4.1 pp = 35.4% - 31.3% (L201) [derived], the Q2 figure; "15 days into the quarter" refers to Q3 trend. Not a finding. |
| C7 4.6 to 5.6 vs 98 bps | L727 vs L167 | Consistent within rounding. |
| C8 "$13,196 million" | L159 | ASR dollar sign; Rs million; ties to press release per A1 header L124-125. |
| (new) procurement 11% vs "not 50" | L381 vs L618 | CC-A3-01. Not in the ledger conflict list; A3 adds it. |

---

## 6. HAND-OFF TO A4 (FORWARD-SIGNAL and AMBIGUOUS findings to convert into questions)

FORWARD-SIGNAL: CC-A3-01, 02, 03, 04, 05, 06, 07, 11, 16.
AMBIGUOUS: CC-A3-08, 09, 12, 13, 14, 15, 17, 18, 19.
New questions suggested (not in A4's 34):
1. Q3 FY26 base Rs 45.55/L and "11% might continue" imply Rs 50.56/L. Which is the Q3 guide: 11% YoY or below Rs 50? (CC-A3-01)
2. Is "EBITDA is not going to come down" a margin floor (5.6%) or an absolute floor (Rs 74.0 Cr)? (CC-A3-02)
3. Are the 1%, 0.6% and 0.1% cost-ratio declines YoY or QoQ? (CC-A3-09)
4. What does "90% of everything they sell" measure? (CC-A3-12)
5. Is the Rs 500 Cr ice cream vision based on FY25 or FY26, and is supply to Get-A-Way (3,272 L/day) inside own ice cream revenue? At what transfer price? (CC-A3-08, 17)
6. Heritage farm-gate price vs Aavin in overlapping cow-milk catchments, Q2 and October. (CC-A3-13)
7. Who bears the cattle-feed subsidy cost, and does Heritage guarantee any third-party farmer loans? (CC-A3-14)
8. What changed in the Get-A-Way and Novandie holdings ("now hold", "now wholly owned"), and when? (CC-A3-15)

---

## 7. YAML BLOCK

Identical copy written to `runs/heritgfood-q2fy27/work/blocks/a3-concall.yaml`.

```yaml
stage: A3-forensics
company: "HERITGFOOD"
quarter: "q2fy27"
doctype: "concall"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/heritgfood-q2fy27/work/forensics_concall_heritgfood_q2fy27.md"
ledger_reconciled_pct: 100
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
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: N.A.
  F15: FINDING
  F16: N.A.
  F17: FINDING
findings:
  - {id: "CC-A3-01", check: "F6", line: "L381; L618; L620-621", classification: "FORWARD-SIGNAL", implication: "11% YoY on Q3 FY26 base Rs 45.55 = Rs 50.56/L vs 'not 47 to 50'; Q3 landed cost separates readings"}
  - {id: "CC-A3-02", check: "F6", line: "L602-604", classification: "FORWARD-SIGNAL", implication: "EBITDA floor promise for Q3 vs Q2 Rs 74.0 Cr / 5.6%; basis unstated; hedged at L622"}
  - {id: "CC-A3-03", check: "F6", line: "L479-486; L227-229", classification: "FORWARD-SIGNAL", implication: "D&A drag continues in subsequent quarters; PBT/PAT lag EBITDA; CWIP project unnamed"}
  - {id: "CC-A3-04", check: "F6", line: "L364-367; L638-639", classification: "FORWARD-SIGNAL", implication: "Q3 margin rests on September hike carry-in; liquid-milk % not given; Q3 hike undecided"}
  - {id: "CC-A3-05", check: "F6", line: "L396-403", classification: "FORWARD-SIGNAL", implication: "Karnataka +Rs 8/L from 1 Nov 2026; Bangalore sales-side pass-through catalyst"}
  - {id: "CC-A3-06", check: "F6", line: "L523-527; L428", classification: "FORWARD-SIGNAL", implication: "Q2 ghee price-led (+20% revenue, flat volume); Q3 bumper volume promised"}
  - {id: "CC-A3-07", check: "F6", line: "L700-709", classification: "FORWARD-SIGNAL", implication: "NutriVate PBT margin Q1 2.6% to Q2 4.3%; H2 PBT improvement promised; intra-group channel exists"}
  - {id: "CC-A3-08", check: "F6", line: "L770-774", classification: "AMBIGUOUS", implication: "Ice cream Rs 500 Cr target implies 14-24% CAGR vs 55-82% current growth; two bases, two horizons"}
  - {id: "CC-A3-09", check: "F6", line: "L727-733", classification: "AMBIGUOUS", implication: "Cost-ratio declines period unstated; QoQ reading conflicts with +63 bps QoQ gross margin"}
  - {id: "CC-A3-10", check: "F6", line: "L411-418; L475; L631-633", classification: "NEUTRAL-FACT", implication: "One-way price ratchet; Rs 1/L procurement = about 1.2 pp of revenue per quarter"}
  - {id: "CC-A3-11", check: "F7", line: "L469; L605; L622; L372-375; L296-299", classification: "FORWARD-SIGNAL", implication: "Three refusals to call the cycle; relief rests on hope; October cost up vs September"}
  - {id: "CC-A3-12", check: "F7", line: "L508-509; L520-521; L527; L715-719", classification: "AMBIGUOUS", implication: "Granularity deflection; '90%' cannot be revenue share (curd+paneer+ghee about 40-42% of VAP)"}
  - {id: "CC-A3-13", check: "F7", line: "L492-497; L393-395", classification: "AMBIGUOUS", implication: "Declined cooperative comment after citing Aavin/KMF; Aavin +Rs 6/L in cow belts"}
  - {id: "CC-A3-14", check: "F6", line: "L306-309; L441-443; L816-817; L822-823", classification: "AMBIGUOUS", implication: "Feed subsidy cost bearer and any farmer-loan guarantee unstated"}
  - {id: "CC-A3-15", check: "F15", line: "L229-230; L232-233", classification: "AMBIGUOUS", implication: "'now hold 71 percent' / 'now a wholly owned subsidiary' signal holding changes; prior list ND"}
  - {id: "CC-A3-16", check: "F17", line: "L500-502; L686-688", classification: "FORWARD-SIGNAL", implication: "Cow about 80% of procurement and the more inflationary species; leans bear on A4 Q29"}
  - {id: "CC-A3-17", check: "F17", line: "L229-232; L427; L774-775", classification: "AMBIGUOUS", implication: "Get-A-Way supply about Rs 24 Cr/yr; may be 13-14% of own ice cream revenue, eliminates on consolidation"}
  - {id: "CC-A3-18", check: "F17", line: "L179; L191; L471; L529-532", classification: "AMBIGUOUS", implication: "Procured milk not sold as liquid milk +22% YoY; SMP/bulk use unaddressed"}
  - {id: "CC-A3-19", check: "F17", line: "L741-743; L805-807", classification: "AMBIGUOUS", implication: "6% procurement CAGR repeated, not reconciled with 1.6%; A4 Q30 open"}
  - {id: "CC-A3-20", check: "F17", line: "L845", classification: "NEUTRAL-FACT", implication: "26 of 34 A4 questions silent; none asked; route to IR email"}
  - {id: "CC-A3-21", check: "F17", line: "L147", classification: "NEUTRAL-FACT", implication: "WTD presented on call; third presenter vs deck and release; A4 Q22 open"}
forward_signals: ["CC-A3-01", "CC-A3-02", "CC-A3-03", "CC-A3-04", "CC-A3-05", "CC-A3-06", "CC-A3-07", "CC-A3-11", "CC-A3-16"]
ambiguous: ["CC-A3-08", "CC-A3-09", "CC-A3-12", "CC-A3-13", "CC-A3-14", "CC-A3-15", "CC-A3-17", "CC-A3-18", "CC-A3-19"]
commitments:
  - {commitment: "Staggered Q2 price hikes; benefit accrues in Q3", implied_date: "Q3 FY27", ref: "T014 L364-366 R226", status_word: "underway"}
  - {commitment: "October opened at much higher consumer price levels than Q2", implied_date: "Oct 2026", ref: "T014 L367 R227", status_word: "completed"}
  - {commitment: "Q3 price hike decision pending ('we will take a call')", implied_date: "Q3 FY27", ref: "T056 L638-639 R256", status_word: "initiated"}
  - {commitment: "Q3 procurement inflation ~11% YoY might continue", implied_date: "Q3 FY27", ref: "T016 L381 R230", status_word: "expectation"}
  - {commitment: "Procurement will not go from Rs 47 to Rs 50 in a quarter", implied_date: "Q3 FY27", ref: "T051 L618 R253", status_word: "expectation"}
  - {commitment: "EBITDA not going to come down", implied_date: "Q3 FY27 onward", ref: "T049 L603-604 R251", status_word: "expectation"}
  - {commitment: "Operating leverage Q3 better than Q2", implied_date: "Q3 FY27", ref: "T032 L485-486 R246/R247", status_word: "expectation"}
  - {commitment: "VAP contribution continues to expand in Q3", implied_date: "Q3 FY27", ref: "T032 L476-478 R243", status_word: "underway"}
  - {commitment: "Ghee bumper volume growth in Q3", implied_date: "Q3 FY27", ref: "T041 L525-527 R248", status_word: "underway"}
  - {commitment: "Depreciation from capitalised projects weighs in subsequent quarters", implied_date: "FY27", ref: "T032 L479-483 R244", status_word: "completed"}
  - {commitment: "New ice cream facility commissioned; capacity absorption", implied_date: "by Q2 FY27", ref: "T003 L227-229 R218", status_word: "completed"}
  - {commitment: "Karnataka +Rs 8/L from 1 Nov; Bangalore pass-through after KMF", implied_date: "1 Nov 2026", ref: "T022 L396-403 R232-R234 R285", status_word: "initiated"}
  - {commitment: "Raise consumer prices again if procurement rises", implied_date: "conditional", ref: "T032 L475 R242", status_word: "standing"}
  - {commitment: "No consumer price pass-back when milk falls", implied_date: "conditional", ref: "T026 L411-418 R237/R238", status_word: "standing"}
  - {commitment: "Margins to steady state if raw material falls", implied_date: "conditional", ref: "T073 L738-739 R264", status_word: "expectation"}
  - {commitment: "NutriVate pass-through Q3/Q4; stronger H2 PBT", implied_date: "H2 FY27", ref: "T067 L706-709 R257/R258", status_word: "initiated"}
  - {commitment: "Own ice cream Rs 500 Cr excl Get-A-Way in 5-7 years; FY27 Rs 170-200 Cr", implied_date: "FY32-FY34", ref: "T076 L770-775 R265-R268", status_word: "underway"}
  - {commitment: "Exports (12 countries, 0.5% of revenue) to grow", implied_date: "undated", ref: "T076 L778-781 R270", status_word: "underway"}
  - {commitment: "No geographic expansion; going deeper", implied_date: "standing", ref: "T076 L777-778 R269", status_word: "standing"}
  - {commitment: "Milk availability may improve after Diwali", implied_date: "Nov 2026", ref: "T006 L296-299 R223/R224", status_word: "expectation"}
  - {commitment: "Buffalo flush and post-Diwali procurement cooling", implied_date: "Nov-Dec 2026", ref: "T014/T016 L372-374 L383 R228/R229/R231", status_word: "expectation"}
  - {commitment: "Farmer engagement improves availability; double farmer income every few years", implied_date: "undated", ref: "T006/T078 L310 L809-810 R225 R273", status_word: "underway"}
  - {commitment: "Q2 launches: Nourish+ curd, Greek yogurt, organic curd, Alpenvie range", implied_date: "Q2 FY27", ref: "T003 L219-222 R172-R174", status_word: "completed"}
  - {commitment: "Get-A-Way 71% held; Heritage Novandie wholly owned", implied_date: "as at call", ref: "T003 L229-233 R050 R176 R177", status_word: "completed"}
gate_a3: pass
blank_checks: []
f17_tally: {questions_total: 34, answered: 1, partly: 7, silent: 26, monitorables_total: 14, mon_answered: 2, mon_partly: 5, mon_silent: 7}
analyst_note: "Procurement cost is the load-bearing signal. Two management answers conflict: '11% kind of thing might continue' (L381) and 'we don't think it will go from 47 to 50 rupees in a quarter' (L618). On the stated Q3 FY26 base of Rs 45.55 (L621), 11% YoY is Rs 50.56/L, so the Q3 landed cost separates the readings. Management's own sensitivity (L631-633) puts Rs 1/L at about 1.2 pp of revenue, so the gap is worth about 3 pp of margin before price action. The EBITDA floor (L603) is the trackable promise. Cow milk is about 80% of procurement by volume (L501-502; 'Kaunulk' read as cow milk [INFERENCE]) and the more inflationary species (L686). That leans to the bear reading of A4 Q29. The silence is mostly not evasion. Analysts asked only about pricing, procurement, mix and ice cream, and nobody asked about CWIP, subsidiaries, tax or cash flow (26 of 34 silent). Send those to the IR email. ASR caveat: 90%, 1200, 405% and 70% are likely engine artefacts. Findings use only numbers that context confirms."
```
