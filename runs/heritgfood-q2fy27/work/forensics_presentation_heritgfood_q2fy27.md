# A3 FORENSIC NOTES: HERITGFOOD | Q2 FY27 | doctype: presentation

Source chain: A1 structured `runs/heritgfood-q2fy27/extracted/heritgfood-presentation-q2fy27-structured.md` (R001-R651), A1 fulltext `runs/heritgfood-q2fy27/extracted/heritgfood-presentation-q2fy27-fulltext.md` (1,328 lines, 45 pages), A2 ledger `runs/heritgfood-q2fy27/work/ledger_presentation_heritgfood_q2fy27.md` (gate_a2 pass). Source PDF and inputs/ were not opened.
Prior-quarter fulltext: ND. Notion monitoring checklist: ND (pre-thesis read, no Notion page, no spear). So cross-deck diffs (F5, F15 list diff, F16 dropped metrics) cannot be tested. Every F16 item below is a within-deck finding.
Units: INR Mn as printed (x0.1 for Rs Cr). Derived numbers are marked [derived]. Values read from chart text positions are marked [positional inference] and are cross-checked by arithmetic where the deck allows.

## 0. LEDGER RECONCILIATION (100%)

- Rows in ledger: 45 slide rows + 651 structured rows (R001-R651). Rows read at cited line: 696 of 696. orphan_ids: none.
- 11 ZERO_STANDING rows read (R117, R118, R119, R121, R403, R439, R440, R486, R508, R509, R510). All go to F1.
- Line-cite drift (A1 hygiene, values correct): R030 "426" cites l143, the value sits at l150. R040 "1,358" cites l162, the value sits at l165.
- COLUMN_UNRESOLVED / FOOTNOTE_UNRESOLVED resolved by arithmetic on slide 8 (l228-251):
  - R120 / R648 "(13)" = H1FY26. H1FY26: 1,511 - 388 - 80 + 104 - 13 + 94 = 1,228 vs printed PBT 1,227.
  - R122 "94" = Q2FY26. Q2FY26: 772 - 201 - 38 + 52 + 94 = 679 vs printed 678. R123 "94" = H1FY26.
  - Both 94s are exceptional GAINS (added to reach PBT).
- R647 "10.353" (l230) = 10,353. Check: 11,125 - 772 = 10,353.
- CHART_PERIOD_ORDER_INFERRED rows on slide 7 (R052-R067) confirmed: segment sums tie to revenue. Q2FY27 6,857 + 4,510 + 918 + 912 = 13,197 vs 13,196. Q2FY26 11,126 vs 11,125. H1FY27 26,577 vs 26,577. H1FY26 22,493 vs 22,493.
- CHART_LABEL_UNMAPPED rows used below (slides 9, 11, 21, 29, 34, 44): mapped by column position to x-axis labels [positional inference]. Slide 44 mapping is confirmed by arithmetic for D/E (FY25 1,744/9,720 = 0.18; FY26 3,615/11,081 = 0.33), current ratio (FY25 6,851/3,766 = 1.82; FY26 6,936/4,938 = 1.40), ROCE FY26 (14.0 vs slide 16 "13.95% ROCE", l523) and receivables turnover FY26 (45,260 / avg(380, 712) = 82.9).
- MISSING_FROM_STRUCTURED: none found.

## 1. FINDINGS TABLE

| id | check | ledger row ref | line/slide | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | R117-R119, R121, R403, R486, R402, R404, R405 | l242, l245, l1221-1223, l1251 (slides 8, 42, 43) | "Share of Profit/(Loss) of an associate & Joint ... - - -"; "Investment in Associate & Joint Venture 177 96 -" | AMBIGUOUS | The associate/JV line is nil from Q2FY26 and the investment is nil at FY26, yet the line stays in the template. The "Exceptional Item" line is non-zero in FY25 (87), Q2FY26 (94) and FY26 (101): it is recurring, not exceptional. Ask: does any associate/JV remain, and what transaction class does the exceptional line carry (disposal, remeasurement, impairment)? |
| A3-02 | F1 | R122, R125, R127, R128-R130 | l245, l247 (slide 8) | "Exceptional Item - 94 - - 94"; "Profit Before Tax 426 678 335 (37) %" | NEUTRAL-FACT | The Q2FY26 base PBT 678 includes a +94 exceptional gain [derived]. Clean Q2FY26 PBT = 584; Q2FY27 PBT 426 is -27% YoY clean, not -37%. H1: 761 vs clean 1,133 = -33%, not -38%. Symmetric read: the headline overstates the YoY fall; the underlying fall is still large. |
| A3-03 | F2 | R203-R218, R543, R651, R058, R059, R066, R067 | l343, l351, l363-374 (slide 11); l187-214 (slide 7) | "Heritage Nutrivet Limited – Wholly owned subsidiary"; "Q2 FY27 Revenues up 47% YoY" | AMBIGUOUS | No standalone columns in the deck; Nutrivet is the only subsidiary decomposition. [positional inference] Nutrivet revenue FY23 1,069 / FY24 1,601 / FY25 1,849 / FY26 2,454 / H1FY27 1,581; PBT 24 / 84 / 169 / 206 / 56.2. PBT margin H1FY27 3.6% vs FY26 8.4% and FY25 9.1% [derived]. Nutrivet H1FY27 revenue 1,581 is close to consolidated "Others" 1,614 (l207) [inference: Others is mostly cattle feed]. Others grew 43% in Q2 and supplied 276 of the 2,071 Rs Mn revenue increase (13%). The slide headlines revenue only. Ask: Nutrivet Q2 PBT and margin, and whether H1 margin is seasonal or a feed-cost squeeze. |
| A3-04 | F6 | R586, R096-R109, R445-R447, R457-R459, R475-R477 | l122 (slide 5); l236, l238 (slide 8); l1248, l1253, l1258 (slide 43) | "expanding VAP capacity and accelerating innovation" | FORWARD-SIGNAL | The capacity commitment has no date, no capex number and no capacity figure. The cost of the build is already in the P&L: depreciation +37% YoY (275 vs 201), finance cost +89% (73 vs 38). FY26 PPE 11,395 vs 7,411 (+54%), gross debt 3,615 vs 1,744 (+107%) [derived]. Feeds Role 5 tracker as an open commitment. Ask: capex plan, commissioning dates, and the revenue capacity the new assets add. |
| A3-05 | F7 | R589, R591, R634, R003-R010, R173-R196, R606 | l127 (slide 5); l264-265, l270-293 (slide 9); l97-103 (slide 5) | "While near-term cost pressures persist"; "standard cost/litre rising steadily from April to September" | FORWARD-SIGNAL | [positional inference, direction confirmed by l265 text] Cow milk standard cost Apr 51.59 to Sep 54.65 Rs/L; YoY inflation rose every month: +4.8%, +5.1%, +5.7%, +6.4%, +7.2%, +8.3%. Buffalo YoY +9.1% to +15.5%. Q2 procurement price "+11% higher YoY" vs milk selling price "up 6%". Sept exit cost sits above the Q2 average, so Q3 starts on a higher cost base. Q2's 98 bps sequential margin gain is at risk unless prices rise again. Ask: price actions taken after September, and the Q3 procurement cost trend. |
| A3-06 | F7 | R197-R202 | l300, l304 (slide 10) | "Almost All Products Recorded Volume Growth Despite Price Increase"; "Price up, volume down" | AMBIGUOUS | "Almost all" admits at least one product with a volume decline after price increases. The deck does not name it. Products plotted at the highest realisation growth (Flavoured Milk, Milk Shakes, l334) are the candidates [positional inference]. Ask: which products lost volume and their revenue share. Elasticity evidence for the pricing-power claim. |
| A3-07 | F7 | R595-R599, R643 | l870-885 (slide 29); l1012-1033 (slide 36); l1056-1095 (slide 37) | "FY28E"; "CY32(E)"; "FY28(P)" | NEUTRAL-FACT | The F7 hedge lexicon has zero hits in 1,328 lines. The deck has no safe-harbour or cautionary statement, yet it carries company estimates (FY28E) and third-party projections. Prior deck ND, so "dropped" cannot be tested. Weight the FY28E chart as unhedged marketing, not guidance. |
| A3-08 | F8 | R131-R137, R124-R129, R409-R411, R406-R408, R448-R450 | l249 (slide 8); l1227 (slide 42); l1254 (slide 43) | "Tax 117 168 86 (30) % 203 312" | AMBIGUOUS | ETR [derived]: Q2FY27 27.5%, Q1FY27 25.7%, Q2FY26 24.8%, H1FY27 26.7%, H1FY26 25.4%, FY24 26.5%, FY25 27.1%, FY26 25.4%. Q2FY27 is 233 bps above the 25.17% statutory rate (about 10 Rs Mn of excess tax) and the highest in the series. No current/deferred split and no prior-year adjustment line in the deck. DTL rose 287 to 417 in FY26 (+45%), a deferred charge, not a shield. Candidate driver [inference]: a loss-making subsidiary with no DTA recognised (see A3-09, A3-14). Ask: Q2 ETR bridge and prior-year tax items. |
| A3-09 | F10 | R165-R171, R138-R143, R424-R426, R412-R414, R430-R432 | l259 (slide 8); l1237 (slide 42); l1247 (slide 43) | "EPS Diluted (INR) 3.4 5.5 2.7 (39) % 6.1 9.9" | AMBIGUOUS | Paid-up capital flat at 464 FY24-FY26. Implied share count from FY EPS = 92.8 Mn (1,883 / 20.29) [derived]. Q2FY27 PAT 309 / 92.8 = 3.33, printed 3.4. H1FY27 558 / 92.8 = 6.01, printed 6.1. Q2FY26, Q1FY27 and H1FY26 tie. Either attributable PAT exceeds consolidated PAT (non-controlling interest absorbs a loss of at least about 2 Rs Mn in Q2), or the share count fell, or the EPS is misprinted. Basic EPS is not shown, so the basic/diluted spread cannot be tested. Ask: Q2 profit attributable to owners, NCI share, weighted share count. |
| A3-10 | F11 | R244, R641, R445-R447, R457-R459, R505-R507, R499-R501, R442-R444, R520, R525 | l521 (slide 16); l1253, l1258, l1259, l1257 (slide 43); l1271-1286 (slide 44) | "0.33 Net Debt/Equity"; "*As of FY26" | AMBIGUOUS | FY26 gross debt 2,543 + 1,072 = 3,615; total equity 11,081. Gross D/E = 0.33. Net of cash 703: 0.26. Net of cash and current investments 1,855: 0.10 [derived]. The "Net Debt/Equity" label carries the GROSS ratio; slide 44 charts the same 0.3 as "Debt/Equity". Gap vs cash-net reading > 5%. Candidate reconciling items: label error, restricted cash, investments treated as non-liquid. The substance: gross debt doubled in FY26 and short-term borrowings rose 3.8x (283 to 1,072). Ask: net debt definition and FY27 debt trajectory. |
| A3-11 | F11 | R475-R495, R430-R444, R472-R474, R517-R519 | l1248-1254, l1263 (slide 43) | "Total non-current assets 7,561 8,732 12,562" | AMBIGUOUS | Net worth ties all three years (464 + 10,569 = 11,033; + MI 48 = 11,081). Liabilities and current assets tie. FY26 non-current asset lines sum to 12,528 (11,395 + 466 + 246 + 0 + 200 + 221) vs printed total 12,562: 34 Rs Mn unallocated [derived]. FY24 and FY25 tie. Candidates: goodwill on consolidation not shown, a deferred tax asset, or the associate line printed "-". Ask at AR: the FY26 non-current asset schedule. |
| A3-12 | F14 | R403-R405, R406-R408, R122, R123 | l1223, l1225 (slide 42); l245 (slide 8) | "Exceptional Item - 87 101" | AMBIGUOUS | Same line, same unbracketed print, opposite signs. FY25: 3,310 - 696 - 154 + 279 - 69 = 2,670; PBT 2,582, so the 87 is a CHARGE. FY26: 2,663 - 810 - 172 + 242 - 13 = 1,910; PBT 2,011, so the 101 is a GAIN [derived]. The associate line on the same slide uses brackets for losses. Clean PBT FY25 2,669 to FY26 1,910 = -28%, vs reported -22%. A reader who adds rows as printed misstates FY25 by 174. Ask: nature of the FY25 charge and the FY26/Q2FY26 gain. |
| A3-13 | F14 | R076, R647, R092, R095, R148, R151, R155, R268, R291 | l230, l234, l253, l255 (slide 8); l589 (slide 18); l687 (slide 22); l462 (slide 14); l630 (slide 20) | "10.353"; "(19) %" vs "(161) Bps"; "(112) %"; "188 ... Chilling Centres" vs "Chilling - 191 centres" | NEUTRAL-FACT | Cluster of drafting slips. Expenses typo 10.353. Q2 margin change shown as relative % ("(19) %", "(49) %") while H1 is shown in bps; Q2 in bps would read -133 bps EBITDA and -224 bps PAT [derived]. OCI "(112) %" labels an improvement (from -3 to +0.37) as a decline. Chilling centres 188 on slide 18 vs 191 on slide 22. Duplicate step "3" (l462) and duplicate "02" (l630). Individually immaterial; cumulatively a data-quality point for the deck. |
| A3-14 | F15 | R484-R486, R439-R441, R481-R483, R400-R402, R117-R120, R543 | l1250, l1251 (slide 43); l1221 (slide 42); l242 (slide 8); l343 (slide 11) | "Minority Interest 0 0 48"; "Investment in Associate & Joint Venture 177 96 -"; "Wholly owned subsidiary" | AMBIGUOUS | No consolidation list in the deck and no prior list, so this is an implied entity change, not a list diff. In FY26 the associate/JV investment fell from 96 to nil, associate share stopped after Q1FY26, a +94 exceptional gain landed in Q2FY26, minority interest appeared (48) and intangibles rose 65 to 246. The only named subsidiary (Nutrivet) is wholly owned, so a non-wholly-owned subsidiary exists that the deck does not name [inference: a JV/associate converted to a subsidiary, with a remeasurement gain, would produce this pattern]. Ask: entity list change in FY26, the entity carrying the MI, and whether the 94 gain is a remeasurement or disposal gain. |
| A3-15 | F16 | R011-R020, R629, R630 | l97, l102, l107, l112 (slide 5) | " 01 ... 02 ... 03 ... 05" | AMBIGUOUS | The Q2 overview numbers its bullets 01, 02, 03, 05. Item 04 is missing. Candidate for a removed highlight. Prior deck ND, so the dropped metric cannot be named. Ask: what item 04 carried in the draft or the prior deck. |
| A3-16 | F16 | R021-R023, R082-R095, R138-R151 | l118-119 (slide 5); l232-253 (slide 8) | "another quarter of strong execution ... a 98bps sequential recovery in EBITDA margin to 5.6%" | AMBIGUOUS | The headline uses the sequential basis. On the YoY basis the same quarter shows EBITDA -4%, margin -133 bps, PAT -39% (-27% PBT clean, A3-02). Derived margin path: Q1FY26 6.5%, Q2FY26 6.9%, H2FY26 5.1%, Q1FY27 4.6%, Q2FY27 5.6% [derived]. 98 bps sequential checks (5.61% vs 4.63%). Question for A4: is 5.6% a floor or a seasonal high, given A3-05? |
| A3-17 | F16 | R520-R535, R649, R246 | l1268, l1271-1306 (slide 44) | "Strengthening Financial Health : Key Balance Sheet Ratios" | CONFIRMATORY-NEGATIVE | [positional inference, arithmetic-confirmed where noted] FY25 to FY26: D/E 0.2 to 0.3 (confirmed), current ratio 1.8 to 1.4 (confirmed), ROCE 23.6 to 14.0 (confirmed via slide 16), FATR 5.7 to 4.8, inventory turnover 11.2 to 10.3, receivables turnover 155.2 to 82.9 (FY26 confirmed), payables turnover 30.4 to 18.7, net capital turnover 24.0 to 14.4. Every plotted ratio weakened under a title that says the reverse. Trade receivables +87% (380 to 712) vs revenue +9.5%. |
| A3-18 | F16 | R303-R306, R595, R596, R619, R643, R644 | l870-885 (slide 29) | "VAP portfolio to Improve Margins"; "FY20 FY26 FY28E" | FORWARD-SIGNAL | Two charts with six bars print four values. [positional inference] VAP (exc. bulk fats) share FY20 27%, FY26 32%; gross margin FY20 18%, FY26 23% (ties to slide 16 "23.4% Gross margin"). Both FY28E bars carry no number. A dated target with no value. Feeds FTTCP catalyst timeline as unquantified. Ask: FY28E VAP share and gross margin as numbers. |
| A3-19 | F16 | R011-R020, R054, R068, R016 | l106-113 (slide 5); l187 (slide 7); l228 (slide 8) | "Contribution of VAP to total revenue improved by 4.1% YoY to 35.4% from 31.3%" | AMBIGUOUS | Deck numbers give 4,510 / 13,196 = 34.2% and 3,418 / 11,125 = 30.7%; incl. packs 5,408 / 13,196 = 41.0% vs printed 42.5% [derived]. The printed shares imply a denominator about 12,730 (Q2FY27) and 10,900 (Q2FY26), below revenue from operations by about 465 and 225. "4.1%" is a percentage-point change. Ask: the VAP-share denominator. |
| A3-20 | F16 | R235, R600, R638, R549, R052, R053 | l473-490 (slide 14) | "9.4% (TG*)"; "*Executed in our core Telangana market"; "Boosted Profitability" | AMBIGUOUS | The campaign's growth metric covers one state. Company milk revenue grew 8.5% (6,857 vs 6,321) [derived], so milk outside Telangana grew less than 8.5%. "Boosted Profitability" has no number. Ask: milk revenue growth outside Telangana and the campaign's margin effect. |
| A3-21 | F16 | R054, R055, R062, R063, R052, R053, R060, R061 | l187-189, l206-208 (slide 7) | "4510 ... 3418"; "10,146 ... 7,451" | AMBIGUOUS | The deck shows Q2 and H1 but not Q1 by segment. Derived Q1 (H1 minus Q2): VAP Q1FY27 5,636 vs Q1FY26 4,033 = +39.7%; Q2 +32.0%. VAP growth slowed by 8 pp QoQ. Milk went the other way: Q1 +4.5%, Q2 +8.5% [derived]. Ask: whether the VAP slowdown reflects seasonality, base, or a capacity limit (link A3-04). |

## 2. CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 | FINDING | 11 ZERO_STANDING rows read. Associate line kept with nil investment; exceptional line recurring; Q2FY26 base holds a +94 gain (A3-01, A3-02). Loans nil all years (template schedule line, no lending). |
| F2 | FINDING | No standalone columns. Partial subsidiary decomposition via Nutrivet (slide 11): H1FY27 PBT margin 3.6% vs 8.4% FY26 (A3-03). |
| F3 | N.A. | Deck has no standalone cost lines; shell test not possible. |
| F4 | N.A. | No auditor report or Other Matters in a presentation. |
| F5 | N.A. | No Emphasis of Matter or going-concern text in a presentation; prior fulltext ND. |
| F6 | FINDING | Lexicon has zero hits. Soft commitments extracted: VAP capacity (undated, unquantified) against a visible D&A and debt step-up (A3-04). Register below. |
| F7 | FINDING | Lexicon has zero hits. Non-lexicon hedges: "near-term cost pressures persist" with accelerating monthly cost inflation (A3-05); "Almost All Products" (A3-06); no safe-harbour statement (A3-07). |
| F8 | FINDING | Q2FY27 ETR 27.5% vs 25.17%; DTL +45% FY26; no split or prior-year line (A3-08). |
| F9 | PASS | OCI Q2FY27 0.37, Q1FY27 0.48, FY26 +2, FY25 (13), FY24 (11). No single-quarter swing exceeds a prior full year. The sign flip in H2FY26 (+8 after H1 (6)) is under 1% of PAT; verify actuarial assumptions at AR. |
| F10 | FINDING | Capital flat at 464. Q2 and H1 EPS above PAT / 92.8 Mn shares; basic EPS not shown (A3-09). |
| F11 | FINDING | Net worth ties. "Net Debt/Equity 0.33" equals gross D/E (A3-10). FY26 non-current assets carry a 34 Rs Mn unallocated gap (A3-11). |
| F12 | N.A. | Deck gives product-line revenue only (ties to total), no segment assets or liabilities. |
| F13 | N.A. | No board-meeting outcome in a deck. Composition checked: 6 directors = 3 whole-time + 3 independent (l1139-1141) matches the 6 profiles on slide 40; no term dates given. |
| F14 | FINDING | Exceptional-item sign convention flips between years (A3-12); drafting cluster (A3-13). |
| F15 | FINDING | No entity list; balance sheet implies a FY26 entity change: associate gone, unnamed MI-bearing subsidiary (A3-14). |
| F16 | FINDING | Within-deck only (prior deck ND): skipped bullet 04, sequential framing, "Strengthening Financial Health" title vs weaker ratios, unquantified FY28E, VAP share denominator, Telangana-only metric, derived VAP slowdown (A3-15 to A3-21). |
| F17 | N.A. | Concall-specific; doctype is presentation; Notion checklist ND. |

## 3. COMMITMENT REGISTER (F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| Expand VAP capacity | none stated | slide 5, l122 | none stated (aspirational) |
| Strengthen procurement ecosystem; accelerate premium and nutrition-led innovation | none stated | slide 5, l122-123 | none stated |
| Sustainable margin improvement via premiumisation, cost control, operating leverage | none stated ("near-term cost pressures persist") | slide 5, l127-128 | none stated |
| Higher VAP (exc. bulk fats) share and higher gross margin by FY28E | FY28 (values not printed) | slide 29, l870-885 | none stated (unquantified target) |
| Livo yogurt flavours launch ("Plain now. Flavours next.") | next (undated) | slide 13, l450 | initiated (plain variant live) |
| Nourish+ curd added ("New Addition", 400g, 25g protein) | Q2 FY27 | slide 12, l409-414 | completed |
| Nourish+ volume "Crossed 4,633 LPD/KGPD in Q2" | Q2 FY27 | slide 12, l405-406 | completed (milestone) |
| Livo yogurt "Crossed 100 TONS in Q2" | Q2 FY27 | slide 13, l444-446 | completed (milestone) |
| Strategic priorities: geographical footprint, brand building, margin expansion, tech enablement | none stated | slide 27, l803-826 | none stated |

## 4. ITEMS FOR A4 (management questions, from FORWARD-SIGNAL and AMBIGUOUS findings)

Forward signals: A3-04, A3-05, A3-18. Ambiguous: A3-01, A3-03, A3-06, A3-08, A3-09, A3-10, A3-11, A3-12, A3-14, A3-15, A3-16, A3-19, A3-20, A3-21.
Suggested grouping: one question on the FY26 entity event (A3-01, A3-09, A3-12, A3-14, A3-08 candidate); one on cost exit rate and Q3 pricing (A3-05, A3-16, A3-06); one on capacity, capex and FY28E targets (A3-04, A3-18, A3-21); one on definitions (A3-10, A3-19, A3-11, A3-15); one on Nutrivet margin (A3-03).

```yaml
stage: A3-forensics
company: "HERITGFOOD"
quarter: "q2fy27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/heritgfood-q2fy27/work/forensics_presentation_heritgfood_q2fy27.md"
ledger_reconciled_pct: 100        # 696 of 696 (45 slide rows + R001-R651)
checklist:
  F1: FINDING
  F2: FINDING
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: PASS
  F10: FINDING
  F11: FINDING
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: FINDING
  F16: FINDING
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "l242, l245, l1221-1223, l1251", classification: "AMBIGUOUS", implication: "Associate line kept with nil investment; exceptional line non-zero FY25/Q2FY26/FY26, recurring. Ask transaction class."}
  - {id: "A3-02", check: "F1", line: "l245, l247", classification: "NEUTRAL-FACT", implication: "Q2FY26 PBT 678 includes +94 gain; clean Q2 PBT YoY -27% not -37%; H1 -33% not -38%."}
  - {id: "A3-03", check: "F2", line: "l351, l363-374, l207", classification: "AMBIGUOUS", implication: "Nutrivet H1FY27 PBT margin 3.6% vs FY26 8.4% (positional); Others (feed) 13% of Q2 revenue growth. Ask Q2 PBT."}
  - {id: "A3-04", check: "F6", line: "l122, l236, l238, l1248, l1253, l1258", classification: "FORWARD-SIGNAL", implication: "VAP capacity commitment undated/unquantified; D&A +37%, finance cost +89%, PPE +54%, gross debt +107%."}
  - {id: "A3-05", check: "F7", line: "l127, l265, l270-293, l97-103", classification: "FORWARD-SIGNAL", implication: "Cow cost YoY rose monthly +4.8% to +8.3% (Sep); procurement +11% vs selling price +6%; Q3 starts on higher cost base."}
  - {id: "A3-06", check: "F7", line: "l300, l304", classification: "AMBIGUOUS", implication: "'Almost All' admits unnamed volume decliners after price hikes. Ask which and their share."}
  - {id: "A3-07", check: "F7", line: "l885, l1033, l1075", classification: "NEUTRAL-FACT", implication: "No safe-harbour statement while carrying FY28E and third-party projections; weight as unhedged marketing."}
  - {id: "A3-08", check: "F8", line: "l249, l1227, l1254", classification: "AMBIGUOUS", implication: "Q2FY27 ETR 27.5% (+233 bps vs 25.17%), series high; DTL +45% FY26; no split. Ask ETR bridge."}
  - {id: "A3-09", check: "F10", line: "l259, l1237, l1247", classification: "AMBIGUOUS", implication: "Q2 EPS 3.4 vs 3.33 implied (309/92.8 Mn); H1 6.1 vs 6.01. NCI loss, share change or misprint. Basic EPS absent."}
  - {id: "A3-10", check: "F11", line: "l521, l1253, l1258, l1259", classification: "AMBIGUOUS", implication: "'Net Debt/Equity 0.33' equals gross D/E 3,615/11,081; cash-net 0.26. Ask definition; ST debt 3.8x."}
  - {id: "A3-11", check: "F11", line: "l1248-1254", classification: "AMBIGUOUS", implication: "FY26 non-current asset lines sum 12,528 vs total 12,562; 34 Rs Mn unallocated. Check at AR."}
  - {id: "A3-12", check: "F14", line: "l1223, l1225, l245", classification: "AMBIGUOUS", implication: "Exceptional 87 (FY25) is a charge, 101 (FY26) a gain, printed alike. Clean FY26 PBT -28% vs reported -22%."}
  - {id: "A3-13", check: "F14", line: "l230, l234, l253, l255, l589, l687", classification: "NEUTRAL-FACT", implication: "Typo 10.353; Q2 margin change in % vs H1 in bps; OCI (112)% on an improvement; chilling centres 188 vs 191."}
  - {id: "A3-14", check: "F15", line: "l1250, l1251, l1221, l242, l343", classification: "AMBIGUOUS", implication: "FY26: associate to nil, MI 0 to 48 though Nutrivet wholly owned, intangibles 65 to 246. Unnamed subsidiary; ask entity change."}
  - {id: "A3-15", check: "F16", line: "l97, l102, l107, l112", classification: "AMBIGUOUS", implication: "Overview bullets run 01, 02, 03, 05; item 04 missing. Ask what was removed."}
  - {id: "A3-16", check: "F16", line: "l118-119, l232-253", classification: "AMBIGUOUS", implication: "'Strong execution' on sequential +98 bps while YoY EBITDA -4%, margin -133 bps, PAT -39%. Is 5.6% a floor?"}
  - {id: "A3-17", check: "F16", line: "l1268-1306", classification: "CONFIRMATORY-NEGATIVE", implication: "'Strengthening Financial Health' while D/E, current ratio, ROCE (23.6 to 14.0), FATR and turnovers all weakened."}
  - {id: "A3-18", check: "F16", line: "l870-885", classification: "FORWARD-SIGNAL", implication: "FY28E VAP share and gross margin bars carry no values. Unquantified dated target; ask numbers."}
  - {id: "A3-19", check: "F16", line: "l106-113, l187, l228", classification: "AMBIGUOUS", implication: "VAP share 35.4% vs 34.2% from deck numbers; incl. packs 42.5% vs 41.0%. Denominator undisclosed."}
  - {id: "A3-20", check: "F16", line: "l473-490", classification: "AMBIGUOUS", implication: "Milk growth 9.4% is Telangana only; company milk +8.5%, so rest grew less. 'Boosted Profitability' unquantified."}
  - {id: "A3-21", check: "F16", line: "l187-189, l206-208", classification: "AMBIGUOUS", implication: "Derived VAP YoY Q1 +39.7% to Q2 +32.0%; milk Q1 +4.5% to Q2 +8.5%. Seasonality, base or capacity?"}
forward_signals: ["A3-04", "A3-05", "A3-18"]
ambiguous: ["A3-01", "A3-03", "A3-06", "A3-08", "A3-09", "A3-10", "A3-11", "A3-12", "A3-14", "A3-15", "A3-16", "A3-19", "A3-20", "A3-21"]
commitments:
  - {commitment: "Expand VAP capacity", implied_date: "none stated", ref: "slide 5 l122", status_word: "none stated"}
  - {commitment: "Sustainable margin improvement via premiumisation, cost control, operating leverage", implied_date: "none stated", ref: "slide 5 l127-128", status_word: "none stated"}
  - {commitment: "Higher VAP (exc. bulk fats) share and gross margin by FY28E (unquantified)", implied_date: "FY28", ref: "slide 29 l870-885", status_word: "none stated"}
  - {commitment: "Livo yogurt flavours ('Plain now. Flavours next.')", implied_date: "next (undated)", ref: "slide 13 l450", status_word: "initiated"}
  - {commitment: "Nourish+ curd added (New Addition)", implied_date: "Q2 FY27", ref: "slide 12 l409-414", status_word: "completed"}
  - {commitment: "Nourish+ crossed 4,633 LPD/KGPD", implied_date: "Q2 FY27", ref: "slide 12 l405-406", status_word: "completed"}
  - {commitment: "Livo yogurt crossed 100 tons", implied_date: "Q2 FY27", ref: "slide 13 l444-446", status_word: "completed"}
  - {commitment: "Strategic priorities: footprint, brand, margin expansion, tech", implied_date: "none stated", ref: "slide 27 l803-826", status_word: "none stated"}
gate_a3: pass
blank_checks: []
analyst_note: "Pre-thesis read. No prior deck, so cross-deck diffs are untestable and every F16 item is within-deck. Arithmetic resolved A1's unresolved columns: Q2FY26 PBT carries a +94 exceptional gain, FY25 an 87 charge, FY26 a 101 gain, all printed alike. Clean PBT fell 27% YoY in Q2, not 37%; FY26 clean PBT fell 28%, not 22%. The balance sheet shows a FY26 structural event the deck never names: associate investment to nil, minority interest appears though the one named subsidiary is wholly owned, intangibles near 4x, gross debt doubled, PPE +54%. That one event may explain the 94 gain, the EPS-above-PAT gap and the 27.5% ETR; A4 should ask it as one question. The heaviest forward signal is the cost exit rate: cow milk cost YoY inflation rose every month to +8.3% in September while milk realisation grew 6%. Q2's 98 bps sequential gain starts Q3 against a higher cost base. Chart values on slides 9, 11, 21, 29 and 44 rest on column-position mapping, arithmetic-checked where possible; treat them as inference."
```
