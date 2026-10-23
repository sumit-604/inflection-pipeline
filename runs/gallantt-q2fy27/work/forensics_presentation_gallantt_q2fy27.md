# FORENSICS presentation GALLANTT q2fy27 (A3)

Document: Gallantt_Q2FY27_Investor_Presentation.pdf (38 pages, cover letter dated October 21, 2026, fulltext l20)
Inputs read: A1 structured (R001-R760), A1 fulltext (l1-l781), A2 ledger, same-quarter results structured extract (cross-check figures, Rs lakh converted x0.01 to Rs Cr), review_gallantt_q2fy27.md Step 8.5 (l424) and Monitorables (l473). No source PDF and nothing under inputs/ was opened.
Prior-quarter deck: none. DROPPED_SLIDE and chart-baseline diffs under F16 are not assessable.
Quote convention: "pN lL" = page N, fulltext line L. Quotes collapse layout whitespace; characters are otherwise verbatim.
Mapping convention: A1 does not assert cell mapping on pp16, 18, 19, 22, 23. Where this report maps a cell, the basis is stated as [INFERENCE: arithmetic tie] (row sums close exactly) or [INFERENCE: line order] (label/value offset pattern). A5 should test these.
Amendment 17 binds: spot-period ROCE (p10) and rupee working capital (p23) are flagged below and must not feed Section 1B or FTTCP.

## LEDGER RECONCILIATION
- Ledger IDs: 760 of 760 read in the structured file, each quote read at its cited fulltext line. Orphans: none. ledger_reconciled_pct = 100.
- ZERO_STANDING rows (8): R181, R232, R236, R237, R239, R242, R310, R311. All read at p18 l385/l399 and p19 l418 (F1).
- FORWARD rows (26): R664-R689. All in the commitment register or F7.
- A1/A2 flagged conflicts resolved: EBITDA/t QoQ (A3P-01), FY26 label (A3P-14), p17 asterisk (A3P-09), interleaved columns (mapping convention above).

A1 extraction notes. These are not deck findings. They are listed so that A4 and A5 do not inherit the labels.
- R024/R025 cite l128, which is blank. The values sit at l129 and l131.
- R031/R032 tag "YoY 12% / QoQ 22.4%" as the realisation block. In the text layer they sit in the Production/Sales column (l129) and the Capacity Utilization column (l131). The realisation figure has no growth rate (A3P-14).
- R096 tags "~35%" as the premium-grade share. At p12 l256-258 the value sits under "Brand awareness ... increase in core markets". The premium-grade share chart (l274-276) has no values in the text layer (A3P-24). A1 did not render page 12. Render request: page 12.
- R505/R506 tag -670 as Power & Fuel and -444 as Fixed cost. The bridge table at p24 l538-539 reads Power & Fuel 20.14, Fixed Cost -670.23, Others -444.30.
- R754 pairs the p22 asterisk with "Note line 475". The note is at l492.

## CROSS-CHECK: DECK vs FILED RESULTS (Rs Cr)
| Item | Deck | Filed (results extract) | Tie |
|---|---|---|---|
| Revenue Q2 FY27 | 1145.89 (p6 l121) | 1,145.89 (R072) | ties |
| Revenue QoQ / YoY | 0.02% / 13% (p6 l123) | +0.02% / +13.15% | ties |
| PBT / tax / PAT Q2 FY27 | 83 / 23 / 61 (p22 l486-490) | 83.17 / 22.66 / 60.51 | ties; ETR 27.25% |
| P&L lines Q2, Q1, Q2 FY26 (p22) | RM 794, SIT 99, inventory 12, employee 42, finance 9, D&A 36, other 89, total 1081 | 794.21, 98.87, 12.19, 41.71, 9.17, 35.51, 89.22, 1,080.87 | ties |
| Q2 FY26 PAT incl associate | 89 (p22 l492) | 88.93 (R187) | ties |
| EBITDA Q2 FY27 | 110.52 (p6 l121) | 109.69 operating (rev less RM, SIT, inventory, employee, other) | +0.83, basis not stated |
| EBITDA Q1 FY27 | 185 (p23 l505) | 185.10 operating; 203.41 incl other income | ties to operating |
| EBITDA Q2 FY26 | 135 (p23 l505) | 131.55 operating; 144.77 incl other income | ties to neither |
| EBITDA FY26 | 776 (p23 l499) | 716.44 operating; 776.03 incl other income | ties to incl OI |
| Capex spent | 652.54 (p6 l137) | tracker 438.60 + 213.94 = 652.54 (p16) | ties internally |
| Shares outstanding | 24,12,80,945 (p37 l760) | paid-up Rs 24,128.09 lakh at FV Rs 10 (R216) | ties |
| DSO | 15 days (p10 l222) | receivables 185.27 / (1,145.89/91) = 14.7 days | ties |
| Net debt | 190.58 (p6 l134) | borrowings 591.97 - other bank 401.66 - cash 1.12 = 189.19 | residual 1.39 |
| D/E | 0.289 (p10 l216) | borrowings/equity 0.170; total liabilities/equity 0.289 | ties to liabilities |
| ROCE | 7.09% (p10 l215) | H1 EBIT 265.63 / (TA - CL) 3,749.11 = 7.09% | six months, unannualised |

## FINDINGS TABLE
| id | check | ledger row ref | line / slide | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3P-01 | F16 | R018, R384, R472-R474 | p6 l123; p21 l457; p23 l511 | "7% YoY. 30% QoQ" vs "YoY (7) % \| QoQ (23) %"; "6617.75 \| 8010.40 \| 6148.56" | NEUTRAL-FACT | Resolved. 8,010.40 to 6,148.56 = -23.2%, so p21 is correct. The p6 "30%" is 8,010.40/6,148.56 - 1 = +30.3%, the change on an inverted base. Carry -23% QoQ downstream. |
| A3P-02 | F16 | R014, R015, R017, R021, R022, R024-R029, R372-R380 | p6 l123, l129-131; p21 l451 | "18% YoY. 45.7% QoQ"; "31% YoY. 51.1% QoQ" vs "YoY (18) % \| QoQ (45.7) %" | AMBIGUOUS | The headline slide prints every decline without a sign: EBITDA, PAT, EBITDA/t, production (-11.8% YoY, -22% QoQ), sales and utilisation. p21 brackets the same numbers. The text layer cannot show whether colour or arrows carry the sign. A reader of p6 alone sees growth. Ask A4 to confirm the p6 direction markers. |
| A3P-03 | F16 | R459, R466-R468, R476, R016, R373, R378 | p23 l499, l505, l511; p21 l451 | "776"; "135 185 111"; "8,785"; "QoQ (45.7) %" | AMBIGUOUS | The EBITDA basis changes by period. FY26 776 includes other income (716.44 + 59.59). Q1 FY27 185 excludes it. The (45.7)% QoQ implies a Q1 base of 203.4, which includes other income. Q2 FY26 135 matches neither basis. On one basis the QoQ fall is -40.3% (excluding OI) or -37.2% (including OI). FY26 EBITDA/t 8,785 = 776/883.4 KT carries about Rs 675/t of other income; on an operating basis it is about Rs 8,110/t. The FY26 benchmark against Q2's 6,149 is overstated. A4 question: define EBITDA and restate FY26 and Q2 FY26 on one basis. |
| A3P-04 | F16 | R500-R513, R016, R026 | p24 l539; p6 l121, l127 | "6,618 - 13,964 -13,339 20.14 -670.23 -444.30 6,149" | AMBIGUOUS | The EBITDA/t denominator is produced billet tonnes: 110.52/6,149 = 179.7 KT, 185/8,010 = 231 KT and 135/6,618 = 204 KT tie to the p18 l389 row "180 231 ... 204" [INFERENCE: arithmetic tie]. The NSR bar of +13,964/t matches revenue per produced tonne (1,145.89/180 less 1,012.75/204 = +14,015) [INFERENCE]. So the bar carries traded-goods revenue and DRI/pellet sales. Stock-in-trade purchases of Rs 98.87 Cr = Rs 5,493 per produced tonne sit inside the -13,339 RM bar. Leaning bear: the bridge cannot be read as price gain against cost inflation. Ask for the bridge on own-steel sales tonnes, excluding trading. |
| A3P-05 | F17 | R280-R290, R218-R230, R250-R263 | p18 l405, l402, l391, l401, l399 | "106 125 -16% 111 -5% 59 67 -12% 65 164 192"; "176 -7%" | CONFIRMATORY-NEGATIVE | This answers review Q4 with the bear reading. TMT sales were 164 KT against 192 KT QoQ (-14.6%) and 176 KT YoY (-6.8%). TMT production was 162 against 196 KT (l391, -17.3%) and billet output 180 against 231 KT (l389, -22%) [INFERENCE: line order]. Revenue was flat QoQ and +13% YoY on fewer own TMT tonnes. DRI sales (46 vs 12 KT, l401), pellet sales (21 KT vs nil, l399) and traded goods (Rs 98.87 Cr, filing) held revenue up. Q3 revenue depends on trading continuing. The margin reset is volume deleverage plus mix [INFERENCE]. |
| A3P-06 | F6 | R670, R738, R074, R075, R087 | p10 l206-208; p11 l231-233 | "652.54 cr of a 3000 cr programme spent to 30 Sept 2026, no incremental debt" | AMBIGUOUS | The filing contradicts the claim for H1 FY27. Borrowings went from 547.69 Cr (31-Mar-2026) to 591.97 Cr (30-Sep-2026), +44.28 Cr. H1 borrowing proceeds were Rs 44.29 Cr, FY26 proceeds were Rs 170.02 Cr, and cash fell from 101.65 to 1.12 Cr. Rs 2,347.46 Cr is still to spend by FY2029-30, about Rs 670 Cr a year, against H1 CFO at 0.49x PAT [INFERENCE]. External funding is likely unless CFO returns to FY26 levels. A4 question: over which window is "no incremental debt" measured, and what is the funding plan for the balance? |
| A3P-07 | F6 | R111-R141, R127-R130, R036, R037, R682 | p16 l336, l351, l332-338 | "860.00 438.60"; "213.94"; "13%" "19% 47%" "21% Mines" | FORWARD-SIGNAL | Every tracker row closes as plan - spent = balance [INFERENCE: arithmetic tie]. Gorakhpur: steelmaking 330.00/318.62/11.38, raw-material deepening 249.00/8.25/240.75, solar 175.00/3.74/171.26, thermal 106.00/107.99/(1.99). Kutch: steelmaking 236.00/127.00/109.00, raw-material deepening nil, solar 50.00/39.58/10.42, thermal 45.00/47.36/(2.36). The tracker plan totals Rs 1,191.00 Cr, 39.7% of the Rs 3,000 Cr programme. The split percentages are shares of 1,191 (steel 566 = 47.5%, RM 249 = 20.9%, solar 225 = 18.9%, thermal 151 = 12.7%), not of 3,000. Rs 1,809 Cr (60.3%) has no component, plant or date. |
| A3P-08 | F6 | R067, R614, R633, R146, R680, R702, R709, R119, R120 | p9 l195; p17 l360-362; p16 l329-331 | "Solar 60 MW, Prayagraj Q4 FY27 In progress"; "175.00 3.74" | FORWARD-SIGNAL | At 30-Sep-2026 the Gorakhpur (UP) solar line had spent Rs 3.74 Cr of Rs 175.00 Cr (2.1%), against Q4 FY27 commissioning [INFERENCE: arithmetic tie]. Rs 171.26 Cr must be deployed in two quarters or less. The Sidhpur benchmark is Rs 39.58 Cr of 50.00 spent for 18 MW commissioned in Jul 2026. Either the payment terms are back-ended or the date slips. Watch the Q3 FY27 tracker. |
| A3P-09 | F6 | R666, R681, R703, R157, R750 | p9 l196; p17 l371-372 | "Capacity to ~12.3 lakh MT Q3 FY27 About to start"; "enhancement* (debottlenecking)" | AMBIGUOUS | The steelmaking budget is 96.6% spent at Gorakhpur (318.62/330.00) and 53.8% at Kutch (127.00/236.00). "About to start" does not say whether construction or commercial operation starts in Q3 FY27. This partly answers review Q5: CWIP of Rs 598.37 Cr is most likely this debottleneck plus thermal (spent 445.62 + 155.35 = 600.97) [INFERENCE]. The asterisk has no footnote. Capacity would rise 23.7% (9,93,300 to 12,29,000 MT). Ask for the COD and the ramp. |
| A3P-10 | F6 | R143, R149, R154, R158, R102, R122, R123, R140 | p16 l334, l349; p17 l370-372; p3 l83 | "106.00 107.99"; "47.36"; "129 MW" ... "160 MW"; "time and cost overruns on projects" | AMBIGUOUS | Thermal has spent Rs 155.35 Cr against a Rs 151.00 Cr plan, an overrun of Rs 4.35 Cr (2.9%). The p9 commitment table has no thermal project or date. Post-enhancement power is 160 MW against 129 MW thermal, so +31 MW is undated. Ask what the thermal spend bought and when it commissions. |
| A3P-11 | F6 | R668, R671, R677, R739, R746, R156, R701 | p9 l194; p13 l290; p17 l371 | "Iron ore mines (operational) FY30 In progress"; "~2,000 per tonne of EBITDA from securing raw-material linkage (management" | FORWARD-SIGNAL | Raw-material deepening has spent Rs 8.25 Cr of Rs 249.00 Cr (3.3%), at Gorakhpur only. Todpura (Rajasthan) has no tracker line. Rs 2,000/t on about 1.23 MT is about Rs 246 Cr a year from FY30 [INFERENCE]. That lies outside the 12-month window. Post-enhancement mines of "70,00,000 MT" are several times own ore need [INFERENCE], so either merchant ore sales are planned or the unit is misprinted. Log as a Role 5 promise. |
| A3P-12 | F11 | R034, R035, R080, R081, R732, R740 | p10 l215-216; p6 l134-137 | "ROCE - 7.09% (Sept-26)"; "Debt/Equity - 0.289"; "190.58 Cr"; "0.64x" | NEUTRAL-FACT | Reverse-tied to the filing [INFERENCE]. D/E 0.289 = total liabilities 1,006.43 / equity 3,486.54; borrowings/equity is 0.170, and the p23 chart shows 0.1-0.2. ROCE 7.09% = H1 EBIT / (total assets - current liabilities), unannualised (about 14.2% annualised). Net debt nets the Rs 401.66 Cr other bank balances as cash but not the Rs 23.34 Cr current investments. Net debt/EBITDA 0.64x = 190.58 / H1 EBITDA of about 295.5 (about 0.32x annualised). The D/E figure sits 70% above the borrowings basis (0.289 vs 0.170), above the 5% F11 threshold. A17: spot-period ROCE, so do not feed it forward. |
| A3P-13 | F16 | R483-R487, R716 | p23 l515-519 | "Working Capital ( Cr) 1350 1274"; "1327"; "966"; "1106" | NEUTRAL-FACT | 1274 = current assets 2,018.03 - current liabilities 743.86 at 30-Sep-2026. 1327 = 2,007.43 - 680.17 at 31-Mar-2026 [INFERENCE: arithmetic tie]. The deck's "working capital" therefore includes bank balances (401.66), loans (265.78) and other current financial assets (326.09). Trade WC is 679.22 Cr. A17: this is a rupee WC trend; flag it and do not feed it forward. It embeds the Rs 591.88 Cr undisclosed pools (review Q1, Q2). |
| A3P-14 | F16 | R030, R729, R730, R031, R032 | p6 l125-127 | "Average Realization (FY26)"; "47,200 Rs./MT" | AMBIGUOUS | The only realisation figure on a Q2 FY27 slide carries an FY26 label. The deck gives no Q2 FY27 realisation and no growth rate for this one. 47,200 does not tie to FY26 revenue per TMT tonne (Rs 57,703) or per billet tonne (Rs 50,022) [INFERENCE]. Q2 FY27 realisation: NOT FOUND. Ask for Q2 FY27 TMT realisation and the basis of 47,200. |
| A3P-15 | F16 | R100-R102, R623, R745, R152, R155 | p13 l281; p17 l369-370 | "60 MW (per Q1 FY2 deck) WHRB Generation 78 MW development Solar under"; "Power 7 MW"; "129 MW 85 MW" | NEUTRAL-FACT | A drafting note pointing at the prior deck was left in print. "78 MW" of solar under development = 18 + 60, yet 18 MW Sidhpur was commissioned in Jul 2026 (p6 l137, p9 l193). p17 shows existing solar of 7 MW and post-enhancement solar of 85 MW (= 7 + 18 + 60) [INFERENCE: line order], which also leaves Sidhpur out of "existing". The slides were not refreshed. This is a governance data point. |
| A3P-16 | F16 | R069, R704, R736 | p9 l197-199 | "+ 1000 bps"; "EBITDA margin, Q3 FY23 to Q2 FY27" | AMBIGUOUS | Q2 FY27 margin is 9.64%, so +1000 bps implies a Q3 FY23 margin of about -0.4% [INFERENCE]. If the figure came over from the Q1 FY27 deck (Q1 margin about 16.2%), the base would be about 6.2%. Ask for the Q3 FY23 base margin. |
| A3P-17 | F14 | R159-R173 | p18 l383 | "58 73 -20% 63 -7% 32 43 -26 46 -31% 45 116 -61% 54 -17%" | NEUTRAL-FACT | Total power for Q2 FY27 is printed 45, but 58 + 32 = 90. Q2 FY26 is printed 54, but 63 + 46 = 109. Q1 (116 = 73 + 43) ties. The printed -61% QoQ follows from the wrong 45; the correct figure is -22.4%. The printed -17% YoY matches the correct sums (90/109). The "MWH" unit is implausible; the values fit average MW load (FY26 Gorakhpur 518.3 MU / 8,760 h = 59 MW) [INFERENCE]. |
| A3P-18 | F14 | R381, R382 | p21 l457 | "YoY (551) bps \| QoQ (333) bps" | NEUTRAL-FACT | The PAT margin changes are swapped. Q2 FY26 margin was 8.61% (87.23/1,012.75), so YoY is (333) bps. Q1 FY27 margin was 10.79% (123.67/1,145.67), so QoQ is (551) bps. |
| A3P-19 | F14 | R582-R592 | p37 l756-758, l759-762 | "70.98 70.03"; "0.09 0.10"; "29.02 29.87" | NEUTRAL-FACT | The 30-Sep-2026 categories sum to 100.09%; 30-Jun sums to 100.00% and the pie to 100.1%. One cell is off by 0.09 pp, so the promoter increase is 0.95 pp or 0.86 pp. |
| A3P-20 | F10 | R582, R583, R588, R589, R593-R596 | p37 l756, l760, l761 | "70.98 70.03"; "24,12,80,945 24,12,80,945"; "537.90 690.65" | FORWARD-SIGNAL | The share count is unchanged and ties to paid-up capital, so no issuance or dilution occurred. Promoters rose 0.86-0.95 pp QoQ, about 20.8-22.9 lakh shares, roughly Rs 112-158 Cr at Rs 538-691 [INFERENCE], in a quarter when the price fell 22.1%. Promoter buying into weakness is a bull datum. The deck names no acquirer or funding source, which matters given the undisclosed Rs 265.78 Cr loans (review Q1). Pledge: not disclosed. |
| A3P-21 | F14 | R176-R180, R103, R307-R309 | p18 l385; p13 l284; p19 l418 | "228 112 103% 185 23%"; "792 K MTPA"; "818.9 599.1 36.7%" | AMBIGUOUS | Q2 FY27 pellet output was 228 KT against a quarterly nameplate of 198 KT (792 K MTPA / 4), or 115%. FY26 output of 818.9 KT was 103% of nameplate, and Q1 was 112 KT (57%). Either stated capacity is understated, or an undisclosed debottleneck or a Q1 shutdown with Q2 catch-up explains it. Merchant pellet sales restarted (21 KT vs nil, l399). Ask for pellet capacity and the Q1 reason. |
| A3P-22 | F1 | R181, R232, R236, R237, R239, R242, R310, R311 | p18 l385, l399; p19 l418; p16 l341 | "21 - 0% 25 -16% - - 0% - 0%"; "818.9 599.1 36.7% 0 0"; "Raw-material deepening -" | NEUTRAL-FACT | The Kutch pellet rows are nil in every period because Kutch has no pellet plant (p9 l190 "Pellet plant, Gorakhpur"). The template row anticipates a Kutch pellet build, but the Kutch raw-material plan is nil, so none is planned [INFERENCE]. Gorakhpur pellet sales were nil in Q1 FY27 and 21 KT in Q2. The printed "0%" QoQ on a nil base is not meaningful. |
| A3P-23 | F7 | R664, R665, R727, R728, R746 | p3 l93, l83, l76-79; p13 l290 | "Certain figures and information in this presentation are indicative and provisional in nature and may be subject to" | NEUTRAL-FACT | The disclaimer covers every deck number and names "time and cost overruns on projects", which the tracker shows on thermal (A3P-10). The 2,000/t target is tagged "(management estimate)". With no prior deck, new hedges cannot be diffed. Deck-only numbers (EBITDA/t, realisation, ratios, volumes) rank below filed figures. |
| A3P-24 | F16 | R096, R743, R744 | p12 l274-276, l256-258 | "Share of premium grades In TMT sales, by quarter"; "~35%" ... "increase in core markets" | AMBIGUOUS | The quarterly premium-grade chart has no values in the text layer, and "~35%" belongs to brand awareness. Premium-grade share: NOT FOUND. The mix-shift claim (p12 l269-272 "Shift towards high-performance steel supporting higher realizations") has no number behind it. Ask for the Q2 FY27 premium share and its trend. Render request: page 12. |
| A3P-25 | F16 | R684, R686, R688, R721, R725, R758 | p34 l713-715, l707; p35 l743 | "India's safeguard duty (effective Apr'25, for 200 days) supports domestic producers"; "12.2 lakh cr FY26 Union Budget" | NEUTRAL-FACT | The industry slides carry stale policy items. On the slide's own terms, a 200-day duty from Apr-2025 lapsed around Nov-2025. The deck cites the FY26 budget, and it states the full-year 2026 China demand as a fact in October. Current safeguard status: PENDING LIVE VERIFICATION. Low weight. |
| A3P-26 | F17 | (checklist; see silence audit) | p22 l460, l492; p37 l755-762; p15 l307-314 | "Consolidated Profit And Loss Statement"; "Note : In Q2FY26 PAT including share of profit from associate ( 1.69 Cr) = 89 Cr" | AMBIGUOUS | Silence audit against the 17 review questions: the deck answers 1 (Q4, bear reading), partly answers 3 (Q5, Q14, Q16) and is silent on 13. Every governance and balance-sheet question is unanswered, including related-party loans, other financial assets, lien status, auditor change, equity roll-forward, dividend, associate identity, standalone filing and ETR. This is the first document tracked, so silence counts 1. Carry all open questions to the call. |

## CHECKLIST SCORECARD
| Check | Status | Basis |
|---|---|---|
| F1 | FINDING | 8 ZERO_STANDING pellet rows read. The Kutch nil is structural (no plant, no RM plan); Gorakhpur pellet sales restarted from nil (A3P-22). |
| F2 | N.A. | The deck carries only the consolidated P&L (p22 l460), with no standalone figures. The results A3 covers S-vs-C. |
| F3 | N.A. | No standalone cost lines in the deck. |
| F4 | N.A. | No auditor report or Other Matters in the deck. |
| F5 | N.A. | No EoM or going-concern paragraph in the deck. |
| F6 | FINDING | The deck carries 10 commitments (register below). Self-funding claim conflicts with filed borrowings; the tracker covers 39.7% of the plan; solar is 2.1% spent; capacity status is ambiguous; thermal is undated; mines target FY30 (A3P-06 to A3P-11). |
| F7 | FINDING | Hedge inventory: the "indicative and provisional" disclaimer covers all figures, overruns are a named risk, and 2,000/t is a management estimate. No prior deck to diff (A3P-23). |
| F8 | PASS | p22 PBT 83, tax 23, PAT 61 tie to the filing (ETR 27.25%). The deck adds no tax data. |
| F9 | N.A. | No OCI in the deck. |
| F10 | FINDING | Share count is unchanged and ties to paid-up capital (no dilution). Promoter stake rose 0.86-0.95 pp with no issuance (A3P-20). No EPS in the deck. |
| F11 | FINDING | D/E 0.289 is total liabilities to equity, 70% above the borrowings basis. ROCE and net debt/EBITDA are six-month figures (A3P-12). The deck shows no net worth figure. |
| F12 | N.A. | Single segment (filing Note 4). Plant-wise capex is covered under F6. |
| F13 | N.A. | No board outcome. The board roster (p31-32) carries no term dates. |
| F14 | FINDING | Internal drafting errors: power total, PAT margin bps swap, shareholding 100.09%, pellet output above nameplate (A3P-17 to A3P-19, A3P-21). The cover letter itself is clean (l20, l49). |
| F15 | N.A. | No consolidation list. The deck names no subsidiary or associate. |
| F16 | FINDING | Inverted EBITDA/t QoQ, unsigned declines, mixed EBITDA basis, production-tonne bridge, rupee WC definition, FY26 realisation label, stale carry-overs, unsupported +1000 bps, premium-grade chart with no data, stale industry items (A3P-01 to A3P-04, A3P-13 to A3P-16, A3P-24, A3P-25). Dropped-slide diff not assessable (no prior deck). |
| F17 | FINDING | Applied to the deck at the task message's direction (no transcript). 1 answered, 3 partly answered, 13 open; monitorables below (A3P-05, A3P-26). |

## COMMITMENT REGISTER (F6)
| # | Commitment | Implied date | Ref | Status word |
|---|---|---|---|---|
| C1 | Capacity to ~12.3 lakh MT (12,29,000 MT, debottlenecking) | Q3 FY27 | p9 l196; p17 l371-372 | "About to start" (budget 96.6% spent Gorakhpur, 53.8% Kutch) |
| C2 | Solar 60 MW, Prayagraj | Q4 FY27 | p9 l195; p17 l360-362; p16 l331 | "In progress" (Rs 3.74 Cr of 175.00 spent [INFERENCE: arithmetic tie]) |
| C3 | Iron ore mines operational (Todpura ~85 MT, Sonbhadra ~51 MT) | FY30 | p9 l194; p11 l246-247 | "In progress" (Rs 8.25 Cr of 249.00 spent) |
| C4 | Rs ~2,000 per tonne EBITDA from mines-to-mill linkage | FY30 (with C3) | p10 l212-214; p13 l290 | "targeted" (management estimate) |
| C5 | Total capex Rs 3,000 Cr | by FY2029-30 | p11 l231-233; p6 l137-141 | initiated (Rs 652.54 Cr spent to 30-Sep-2026) |
| C6 | Self-funded growth, no incremental debt | ongoing | p10 l204-208 | claimed; conflicts with filed borrowings +Rs 44.28 Cr in H1 (A3P-06) |
| C7 | Post-enhancement power 160 MW, mines 70,00,000 MT | NOT FOUND (asterisk, no footnote) | p17 l371-372 | not stated |
| C8 | Solar 18 MW, Sidhpur | Jul 2026 | p6 l137; p9 l193; p17 l367-369 | completed ("Commissioned", "Delivered") |
| C9 | Iron ore mines, preferred bidder | 2024-25 | p9 l192; p8 l150-152, l174-175 | completed ("Delivered") |
| C10 | Rs 3.50 crore annual cost savings (logistics/technology) | not stated | p11 l244 | not stated (claimed as running rate) |
Industry projections (p34 l711 "expected to grow 8-8.5%", p35 l743 "projected to grow 7.9%") are third-party, not company commitments.

## CHECKLIST SILENCE AUDIT (review Step 8.5 questions, l428-446)
| Q | Topic | Deck status | Cite | Note |
|---|---|---|---|---|
| Q1 | Related-party share of Rs 265.78 Cr loans | OPEN | none | Silent. The p23 WC series embeds the pool (A3P-13). |
| Q2 | Other current financial assets Rs 326.09 Cr | OPEN | none | Silent. |
| Q3 | Traded-goods revenue and margin | OPEN | p22 l472 "Purchases of stock in trade 99" | Restates the cost; no traded revenue. The bridge folds trading into NSR (A3P-04). |
| Q4 | Own TMT/billet sales tonnes QoQ | ANSWERED (bear) | p18 l405, l403 | TMT 164 vs 192 KT (A3P-05). |
| Q5 | CWIP project and commissioning date | PARTLY | p16 l336, l351; p9 l196; p17 l371 | Debottleneck to 12.29 lakh MT, Q3 FY27, "About to start" (A3P-09). |
| Q6 | Lien on Rs 401.66 Cr other bank balances | OPEN | p6 l134 "190.58 Cr" | Net debt treats them as cash; no lien statement. |
| Q7 | Predecessor auditor | OPEN | none | Silent. |
| Q8 | Rs 14.06 Cr equity roll-forward gap | OPEN | none | Silent. |
| Q9 | Dividend Rs 48.26 Cr payment date and funding | OPEN | none | Silent. |
| Q10 | Associate identity and exit | OPEN | p22 l492 | Restates the Rs 1.69 Cr; no name. |
| Q11 | Standalone statement filed | OPEN | p22 l460 "Consolidated Profit And Loss Statement" | Consolidated only. |
| Q12 | FY27 ETR guidance | OPEN | p22 l486-488 | Tax 23 on PBT 83; no guidance. |
| Q13 | Reclassification of four new lines | OPEN | none | Silent. |
| Q14 | D&A +17.90% QoQ driver | PARTLY | p6 l137 "Commissioned Jul 2026" | 18 MW solar (Rs 39.58 Cr) capitalised in Q2. At solar lives that adds well under the Rs 5.39 Cr QoQ rise [INFERENCE]. |
| Q15 | Suryalaxmi Technologies assets and wind-up | OPEN | none | The deck names no subsidiary. |
| Q16 | Top-10 customer share | PARTLY | p15 l307-314 "A fragmented dealer base limits individual customer concentration"; "80% Sales via" | 20% of sales are outside the dealer network; no top-10 figure. |
| Q17 | AGM approval of Singhi & Co. | OPEN | none | Silent. |
Silence count: 1 quarter for every OPEN row (first tracked document). The concall transcript is pending.

## MONITORABLES (review l475-489)
| # | Item | Deck status | Cite |
|---|---|---|---|
| 1 | Standalone Q2 FY27 on BSE/NSE | OPEN | p22 l460 (consolidated only) |
| 2 | Reg 47 newspaper extract | OPEN | not in deck |
| 3 | Shareholding pattern; promoter pledge | PARTLY | p37 l755-758 promoters 70.98%; pledge not shown (A3P-19, A3P-20) |
| 4 | Earnings call and answers | OPEN | no call date; IR contacts p38 l771-779 |
| 5 | FY26 dividend paid | OPEN | not in deck |
| 6 | AGM outcome, Singhi term | OPEN | not in deck |
| 7 | FY26 Annual Report for Role 6 | OPEN | not in deck; p29 l613 "during the year" ESG data suggests BRSR exists |
| 8 | Q3 FY27 results (gross margin, traded purchases, ETR, D&A) | OPEN | add: C1 capacity start (p9 l196) and C2 solar spend (p16 l331) as Q3 checks |
| 9 | CWIP commissioning | PARTLY | p9 l195-196; p16 (A3P-09) |
| 10 | FY27 audited results | OPEN | not in deck |
| 11 | Q1 FY28 results | OPEN | not in deck |
| 12 | FY27 Annual Report | OPEN | not in deck |
| 13 | Filing hygiene | PARTLY | cover letter clean ("October 21, 2026", l20; signature l49). Deck drafting errors add to the tally (A3P-01, A3P-15, A3P-17, A3P-18, A3P-19). Ligature drop-outs (l33 "presenta on") are text-layer artefacts. |

## A17 FLAGS (do not feed forward)
- p10 l215 ROCE 7.09% (Sept-26): a six-month spot-period ratio (A3P-12).
- p23 l519-521 ROCE chart 13-23% (Mar-21 to Mar-26), annual spot-year values; the period order is not asserted.
- p23 l515-519 rupee working capital series; the definition includes bank balances and loans (A3P-13).

## Reconciliation with rendered cell map
Date: 2026-10-23. Source: A1 "RENDERED CELL MAP (orchestrator check 2026-10-23)", with CELL rows R761-R1126, MAPS-TO rows R1127-R1484 and CORRECTION rows R1485-R1489, plus A2 addendum Tables 9-13. I read all 729 new rows. The ledger now reconciles at 1,489 of 1,489 IDs (100%). The original findings text above is unchanged. Where this section differs, this section governs.

Summary: 1 withdrawn (A3P-02), 4 amended (A3P-03, A3P-12, A3P-22, A3P-24), 1 new (A3P-27). Every finding that rested on an inferred cell mapping (pp16, 18, 19, 22, 23) is confirmed: each inferred cell matches the rendered cell.

| id | status | rendered cells | reconciliation |
|---|---|---|---|
| A3P-01 | CONFIRMED | R1096-R1098; R1485 | The render shows "30% QoQ" with a down arrow. -30% still conflicts with -23.2% from the deck's own captions (6,148.56 vs 8,010.40). The inverted-base reading stands. |
| A3P-02 | WITHDRAWN | R1485; R1101, R1102, R1108, R1109 | Every p6 delta (EBITDA, EBITDA/t, PAT, utilisation, production, sales) and every p23 delta carries a down arrow. The slide shows direction, so a p6 reader does not see growth. Removed from the A4 question list. |
| A3P-03 | AMENDED | R1091-R1095; R1103-R1107 | The chart cells confirm 135 / 185 / 111 / 710 / 776 by period. Addition: the FY margin bars read FY25 17.0 and FY26 18.0 (R1106, R1107). The deck's own EBITDA over revenue gives 16.5% (710/4,293) and 17.6% (776/4,419). The quarterly bars tie (13.3 = 135/1,013; 16.2; 9.6). So the FY benchmark margin is overstated twice: once by other income inside EBITDA, and again by about 0.4-0.5 pp on the bar itself. The classification stays AMBIGUOUS. |
| A3P-04 | CONFIRMED | R853, R854, R856; R1487 | The denominator is the "Billets - Steel Melt Shop" production total: 180 / 231 / 204 KT. The bridge labels in R1487 (NSR 13,964, RM -13,339, Power & Fuel 20, Fixed Cost -670, Others -444, Volume "-") match the l539 reading this finding used. |
| A3P-05 | CONFIRMED | R928-R932; R868-R869; R853-R854; R898-R902; R913-R914 | TMT sales 164 / 192 / 176 KT (QoQ -14%, YoY -7% printed). TMT production 162 vs 196 KT, billet production 180 vs 231 KT. Additions: DRI sales were 46 KT vs 34 KT YoY (+35%, R901-R902). Billet sales fell to 20 KT from 27 KT QoQ (R913-R914). Revenue support came from DRI, pellet and traded goods; billet sales did not add. |
| A3P-06 | UNCHANGED | n/a | Does not depend on the mapped pages. |
| A3P-07 | CONFIRMED | R764-R797 | All 30 tracker cells match the arithmetic-tie mapping. The donut labels (Steel Plant 47%, Mines 21%, Solar 19%, Thermal 13%; R794-R797) tie to shares of Rs 1,191 Cr. |
| A3P-08 | CONFIRMED | R770-R772; R785-R787 | Gorakhpur Solar 175.00 / 3.74 / 171.26; Kutch Solar 50.00 / 39.58 / 10.42. |
| A3P-09 | CONFIRMED | R764-R766; R779-R781; R774; R789 | Steelmaking and thermal cells match. The p17 asterisk is still unresolved; p17 was not rendered. |
| A3P-10 | CONFIRMED | R773-R775; R788-R790 | Thermal overruns of (1.99) and (2.36) confirmed. |
| A3P-11 | CONFIRMED | R767-R769; R782-R784 | Gorakhpur raw-material deepening 249.00 / 8.25 / 240.75; Kutch "-" in all three cells. |
| A3P-12 | AMENDED | R1115-R1126 | The ROCE chart order is now asserted: Mar-21 13%, Mar-22 15%, Mar-23 14%, Mar-24 16%, Mar-25 23%, Mar-26 23%. The method that reproduces the p10 7.09% (EBIT over total assets less current liabilities) gives FY26 ROCE of 645.72 / 3,589.45 = 18.0%, not 23%. The FY26 23% ties to EBITDA including other income over equity plus borrowings less cash and other bank balances: 776.03 / 3,360.78 = 23.1% [INFERENCE: arithmetic tie, one candidate]. So the deck uses two ROCE bases, and the chart's is EBITDA-based. The D/E chart cells of 0.1-0.2 are confirmed (R1121-R1126). The A17 flag stands; neither ROCE figure feeds forward. The classification stays NEUTRAL-FACT. |
| A3P-13 | CONFIRMED | R1110-R1114 | Period order: Q2 FY26 1106, Q1 FY27 1350, Q2 FY27 1274, FY25 966, FY26 1327. The ties (1274 = 30-Sep-2026, 1327 = 31-Mar-2026) match the rendered periods. The rupee series is +168 Cr YoY and -76 Cr QoQ. A17 applies; not fed forward. |
| A3P-14 | CONFIRMED | R1485 | Realisation of 47,200 carries no delta on the slide. R031/R032 are production deltas and R028/R029 are sales deltas. The FY26 label issue stands. |
| A3P-15 | UNCHANGED | p13 and p17 not rendered | The 7 MW / 85 MW mapping on p17 is still [INFERENCE: line order]. Render request: p17 (this also covers the A3P-09 asterisk). |
| A3P-16 | UNCHANGED | n/a | p9 was not rendered; no mapping reliance. |
| A3P-17 | CONFIRMED | R798-R812; R1489 | The rendered totals are 45 and 54, so the error stands. The Kutch QoQ cell prints "-26" without a % sign (R805). |
| A3P-18 | UNCHANGED | n/a | p21 was not rendered; no mapping reliance. |
| A3P-19 | UNCHANGED | n/a | p37 was not rendered; no mapping reliance. |
| A3P-20 | UNCHANGED | n/a | p37 was not rendered; no mapping reliance. |
| A3P-21 | CONFIRMED | R813-R817; R942 | Pellet output 228 / 112 / 185 KT; FY26 818.9 KT. |
| A3P-22 | AMENDED | R818-R822; R873-R887; R945-R947; R981-R983; R782-R784; R502 per R1487 | The standing nils are confirmed. Two additions. (1) The Kutch raw-material deepening plan, spent and balance cells are all "-" (R782-R784): the programme holds no mine or pellet build at Kutch. (2) The bridge "Volume" bar is a standing nil (R502 per R1487) while billet output fell 12% YoY (R857). A per-tonne bridge has no volume bar, so the volume deleverage sits inside Fixed Cost -670 and Others -444. The classification stays NEUTRAL-FACT. |
| A3P-23 | UNCHANGED | n/a | No mapping reliance. |
| A3P-24 | AMENDED | R761-R763; R1486 | The render confirms an icon only, with no chart values (R763). The page 12 render request is closed. ~35% = brand awareness (R761), and 2-3% = realisation premium versus unbranded peers (R762). Premium-grade share remains NOT FOUND. The classification stays AMBIGUOUS, so A4 still asks for the number. |
| A3P-25 | UNCHANGED | n/a | No mapping reliance. |
| A3P-26 | CONFIRMED | R928-R932 | The Q4 answer rests on rendered cells. The silence counts are unchanged. |
| A3P-27 | NEW (F14, NEUTRAL-FACT) | R1075, R1076; R1488 | p22 l479 prints "411" for Q1 FY27 tax expense. The filing shows Rs 41.15 Cr (results R170, 4,114.72 lakh). PBT 165 less PAT 124 is 41, and the printed QoQ of -45% matches 41 (23/41.15 = -44.9%). This is a drafting error. It joins the deck hygiene tally (monitorable 13). |

The A1 extraction notes above are all confirmed by R1485-R1488. The R754 asterisk sits on the Q2 FY26 net profit cell "87*" (R1082) and pairs to the l492 note. In the A17 flags, the p23 ROCE period order is now asserted (see A3P-12). Scorecard: no status changes. F14 adds A3P-27. F16 stays FINDING without A3P-02.

## Loop 1 addition (A5 M4, M9)
Date: 2026-10-23. Source: A5 loop 1 items M4 and M9; A1 rows R1490 and R1491 (p17 render); concall structured rows R029, R182, R226 and concall fulltext l152. This section governs over the sections above where they differ.

**M4. The R018 conflict is a deck error. A3P-01 is restated as one.**

| id | check | ledger row ref | line / cell | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3P-01 (restated) | F14 (deck error; also F16) | R018 (A2 CONFLICT), R384, R1096-R1098, R1485 | p6 l123; p21 l457; p23 l511 | "7% YoY. 30% QoQ" (p6) vs "YoY (7) % \| QoQ (23) %" (p21) | NEUTRAL-FACT (DECK ERROR) | The p6 EBITDA/t QoQ of "30%" with a down arrow (R1485) is wrong. The deck's own captions give 8,010.40 to 6,148.56 = -23.2% (R1097, R1098), so p21's (23)% is correct. 30% is the change computed on the wrong base (8,010.40/6,148.56 - 1 = +30.3%). Carry -23% downstream. A4 should list this under deck errors, not convert it into a question. The A2 CONFLICT on R018 is closed by this finding. |

The YAML block now carries a `deck_errors` list so A4 can list every deck error in one place: A3P-01, A3P-15, A3P-17, A3P-18, A3P-19, A3P-27.

**M9. The p17 render settles the solar mapping. A3P-15 is AMENDED and reclassified.**
- R1490 confirms the eight p17 capacity cells in row order. Existing capacity: Mines "Nil", Steel 9,93,300 MT, Thermal 129 MW, Solar 7 MW. Post-enhancement: Mines 70,00,000 MT, Steel 12,29,000 MT (debottlenecking), Power 160 MW, Solar 85 MW. The 7 MW / 85 MW mapping is no longer an inference.
- 85 MW = 7 + 18 + 60. The deck therefore counts Sidhpur's 18 MW as future capacity, not existing capacity.
- The call agrees. Concall fulltext l152: "Our 18 megawatt solar plant at Sidpur in Gujarat is completed and set to resume operations by November 26." (R029, R182; the date is flagged ASR_SUSPECT, R226.) On the call date the plant was not generating.
- The p6 and p9 status words conflict with this: p6 l137 "Commissioned Jul 2026" and p9 l193 "Delivered". p13 l281 also still lists "78 MW" under development (= 18 + 60). So two slides say the plant is done, and two slides plus the call say it is not yet in the operating base.
- Reading: p17 and the call support "Sidhpur 18 MW is not yet operating". "Resume" implies it ran for some period and then stopped. Leaning bear: treat Sidhpur as not contributing to Q2 FY27 power cost, and do not credit any Q2 power saving to it. This also weakens the Q14 partial answer: the D&A rise has a weaker link to an asset that is not generating [INFERENCE].
- R1491 confirms the "Post enhancement*" asterisk has no footnote on the rendered slide. C7 stays NOT FOUND, and the A3P-09 asterisk note stands.

| id | status | cells / lines | amendment |
|---|---|---|---|
| A3P-15 | AMENDED; reclassified NEUTRAL-FACT to AMBIGUOUS | R1490; p17 l369-372; p6 l137; p9 l193; p13 l281; concall l152 | The render settles the mapping: existing solar is 7 MW and post-enhancement solar is 85 MW. Sidhpur sits outside existing capacity. The call says it "is completed and set to resume operations by November 26". The deck's "Commissioned Jul 2026" and "Delivered" are contradicted by its own p17 and by the call. A4 question: when did Sidhpur first generate, why did it stop, what did it generate in Q2 FY27, and is it in the Q2 PPE/D&A base? The leftover drafting note "(per Q1 FY2 deck)" remains a deck error. |
| C8 (register) | AMENDED | p6 l137; p9 l193; p17 l369-372; concall l152 | Status word changes from "completed" to "disputed". The deck says "Commissioned"/"Delivered"; p17 and the call say it is not yet operating, with a restart by November 26 (ASR_SUSPECT). Role 5: log as promise-vs-delivery open. |
| A3P-08 | NOTE | p16 l343-349 | The Sidhpur benchmark (Rs 39.58 Cr spent for 18 MW) still holds as a cost benchmark, but not as a delivery benchmark. |

Scorecard: no status changes. F14 now includes A3P-01 as a deck error. The F16 basis stays as amended above.

```yaml
stage: A3-forensics
company: "GALLANTT"
quarter: "q2fy27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "C:/Users/SUMIT SHARMA/repos/inflection-pipeline/.claude/worktrees/quarterly-gallantt-call-q2fy27-7b3ed0/runs/gallantt-q2fy27/work/forensics_presentation_gallantt_q2fy27.md"
ledger_reconciled_pct: 100   # 1491 of 1491 IDs (rendered cell map addendum plus R1490-R1491)
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: PASS
  F9: N.A.
  F10: FINDING
  F11: FINDING
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "A3P-01", check: "F14", line: "p6 l123; p21 l457; p23 l511; R018, R1096-R1098, R1485", classification: "NEUTRAL-FACT", implication: "DECK ERROR (closes A2 CONFLICT R018): p6 prints EBITDA/t '30% QoQ' (down arrow); the deck's own captions give -23.2% (8,010.40 to 6,148.56), as p21 prints; 30% is the inverted base. Carry -23%."}
  - {id: "A3P-03", check: "F16", line: "p23 l499, l505, l511; p21 l451; R1091-R1095, R1103-R1107", classification: "AMBIGUOUS", implication: "EBITDA basis varies: FY26 776 includes other income, Q1 185 excludes it, the -45.7% QoQ implies an incl-OI base, Q2 FY26 135 ties to neither; FY26 8,785/t overstated by about Rs 675/t; FY margin bars 17.0/18.0 vs 16.5/17.6 on the deck's own EBITDA."}
  - {id: "A3P-04", check: "F16", line: "p24 l539; p6 l121, l127; R853-R856, R1487", classification: "AMBIGUOUS", implication: "EBITDA/t and the bridge divide all revenue, trading included, by billet production tonnes (180/231/204 KT); the +13,964/t NSR bar is not realisation."}
  - {id: "A3P-05", check: "F17", line: "p18 l405, l402, l391, l401, l399; R928-R932, R898-R902, R913-R914", classification: "CONFIRMATORY-NEGATIVE", implication: "Answers review Q4 bear: TMT sales 164 vs 192 KT QoQ (-14.6%), vs 176 KT YoY (-6.8%); revenue held up on DRI (46 vs 34 KT YoY), pellet and traded sales; billet sales fell 27 to 20 KT."}
  - {id: "A3P-06", check: "F6", line: "p10 l206-208; p11 l231-233", classification: "AMBIGUOUS", implication: "'No incremental debt' conflicts with filed borrowings +Rs 44.28 Cr in H1 and cash at Rs 1.12 Cr; Rs 2,347 Cr balance to FY30 implies external funding at the H1 CFO pace."}
  - {id: "A3P-07", check: "F6", line: "p16 l336, l351, l332-338; R764-R797", classification: "FORWARD-SIGNAL", implication: "Tracker itemises Rs 1,191 Cr (39.7%) of the Rs 3,000 Cr plan; the split % are of 1,191; Rs 1,809 Cr has no component or date."}
  - {id: "A3P-08", check: "F6", line: "p9 l195; p17 l360-362; p16 l331; R770-R772", classification: "FORWARD-SIGNAL", implication: "60 MW Prayagraj solar due Q4 FY27 with Rs 3.74 Cr of 175.00 spent (2.1%); slip risk; watch the Q3 tracker. Sidhpur is a cost benchmark only, not a delivery benchmark."}
  - {id: "A3P-09", check: "F6", line: "p9 l196; p17 l371-372; R764-R766, R779-R781, R1491", classification: "AMBIGUOUS", implication: "12.29 lakh MT debottleneck 'About to start' Q3 FY27 with budget 96.6%/53.8% spent; partly answers the CWIP question; COD unclear; asterisk has no footnote (render-confirmed)."}
  - {id: "A3P-10", check: "F6", line: "p16 l334, l349; p17 l370-372; p3 l83; R773-R775, R788-R790", classification: "AMBIGUOUS", implication: "Thermal spent 155.35 vs plan 151.00 (overrun 2.9%); +31 MW to 160 MW has no date in the commitment table."}
  - {id: "A3P-11", check: "F6", line: "p9 l194; p13 l290; p17 l371; R767-R769, R1490", classification: "FORWARD-SIGNAL", implication: "Mines operational FY30 (existing 'Nil') with 3.3% of the RM budget spent; Rs 2,000/t target is a management estimate; 70,00,000 MT post-enhancement mining exceeds own need."}
  - {id: "A3P-12", check: "F11", line: "p10 l215-216; p6 l134-137; R1115-R1126", classification: "NEUTRAL-FACT", implication: "D/E 0.289 = total liabilities/equity (borrowings basis 0.170); ROCE 7.09% and ND/EBITDA 0.64x are six-month figures; the p23 ROCE chart is EBITDA-based (FY26 23% vs 18.0% on the p10 method); A17, do not feed forward."}
  - {id: "A3P-13", check: "F16", line: "p23 l515-519; R1110-R1114", classification: "NEUTRAL-FACT", implication: "Deck WC = total current assets less current liabilities (Q2 FY27 1274, FY26 1327), including bank, loans and other financial assets; trade WC is 679 Cr; A17 rupee WC, do not feed forward."}
  - {id: "A3P-14", check: "F16", line: "p6 l125-127; R1485", classification: "AMBIGUOUS", implication: "Only realisation is labelled FY26 on a Q2 FY27 slide, carries no delta, and ties to no FY26 basis; Q2 FY27 realisation NOT FOUND."}
  - {id: "A3P-15", check: "F16", line: "p17 l369-372 (R1490); p6 l137; p9 l193; p13 l281; concall l152", classification: "AMBIGUOUS", implication: "Render settles p17: existing solar 7 MW, post-enhancement 85 MW = 7+18+60, so Sidhpur is outside existing capacity; the call says it 'is completed and set to resume operations by November 26'; the deck's 'Commissioned Jul 2026'/'Delivered' is contradicted; ask first generation date, stoppage cause, Q2 output, PPE/D&A treatment; '(per Q1 FY2 deck)' remains a drafting error."}
  - {id: "A3P-16", check: "F16", line: "p9 l197-199", classification: "AMBIGUOUS", implication: "+1000 bps to a 9.64% margin implies a Q3 FY23 base near -0.4%; likely a stale carry-over."}
  - {id: "A3P-17", check: "F14", line: "p18 l383; R798-R812", classification: "NEUTRAL-FACT", implication: "Power total printed 45/54 vs sums 90/109; the true QoQ is -22.4%, not -61%; 'MWH' unit implausible."}
  - {id: "A3P-18", check: "F14", line: "p21 l457", classification: "NEUTRAL-FACT", implication: "PAT margin YoY and QoQ bps are swapped: YoY is (333), QoQ is (551)."}
  - {id: "A3P-19", check: "F14", line: "p37 l756-758", classification: "NEUTRAL-FACT", implication: "30-Sep shareholding sums to 100.09%; the promoter increase is 0.86 or 0.95 pp."}
  - {id: "A3P-20", check: "F10", line: "p37 l756, l760, l761", classification: "FORWARD-SIGNAL", implication: "No dilution; promoter stake +0.86-0.95 pp (about 21-23 lakh shares, Rs 112-158 Cr) bought as the price fell 22.1%; acquirer, funding and pledge undisclosed."}
  - {id: "A3P-21", check: "F14", line: "p18 l385; p13 l284; p19 l418; R813-R817, R942", classification: "AMBIGUOUS", implication: "Q2 pellet output 228 KT = 115% of 198 KT quarterly nameplate; capacity understated or Q1 shutdown catch-up."}
  - {id: "A3P-22", check: "F1", line: "p18 l385, l399; p19 l418; p16 l341; R782-R784, R818-R822, R878-R884, R945-R947, R981-R983, R502, R1490", classification: "NEUTRAL-FACT", implication: "Kutch pellet and raw-material nils are structural (no plant, no RM build planned); existing mines 'Nil'; Gorakhpur pellet sales restarted from nil; bridge Volume bar nil while billet output fell 12% YoY, so deleverage sits in Fixed Cost -670 and Others -444."}
  - {id: "A3P-23", check: "F7", line: "p3 l93, l83; p13 l290", classification: "NEUTRAL-FACT", implication: "Disclaimer marks all deck figures 'indicative and provisional'; deck-only numbers rank below filed figures; no prior deck to diff."}
  - {id: "A3P-24", check: "F16", line: "p12 l274-276, l256-258; R761-R763, R1486", classification: "AMBIGUOUS", implication: "Premium-grade share is an icon with no values (render confirmed); ~35% is brand awareness, 2-3% is the premium vs unbranded peers; mix-shift claim unquantified."}
  - {id: "A3P-25", check: "F16", line: "p34 l707, l713-715; p35 l743", classification: "NEUTRAL-FACT", implication: "Stale policy items (200-day safeguard from Apr-25, FY26 budget); safeguard status PENDING LIVE VERIFICATION."}
  - {id: "A3P-26", check: "F17", line: "p22 l460, l492; p37 l755-762; p15 l307-314", classification: "AMBIGUOUS", implication: "Deck answers 1 of 17 review questions, partly answers 3, is silent on 13 (all governance and balance-sheet items); silence count 1; carry to the call."}
  - {id: "A3P-27", check: "F14", line: "p22 l479; R1075, R1076, R1488", classification: "NEUTRAL-FACT", implication: "DECK ERROR: Q1 FY27 tax printed 411 vs filed Rs 41.15 Cr; the printed -45% QoQ matches 41."}
deck_errors: ["A3P-01", "A3P-15", "A3P-17", "A3P-18", "A3P-19", "A3P-27"]
withdrawn: ["A3P-02"]          # 2026-10-23: render R1485 shows down arrows on every p6/p23 delta
amended: ["A3P-01", "A3P-03", "A3P-12", "A3P-15", "A3P-22", "A3P-24"]
added: ["A3P-27"]
forward_signals: ["A3P-07", "A3P-08", "A3P-11", "A3P-20"]
ambiguous: ["A3P-03", "A3P-04", "A3P-06", "A3P-09", "A3P-10", "A3P-14", "A3P-15", "A3P-16", "A3P-21", "A3P-24", "A3P-26"]
commitments:
  - {commitment: "Capacity to ~12.3 lakh MT (12,29,000 MT debottlenecking)", implied_date: "Q3 FY27", ref: "p9 l196; p17 l371-372", status_word: "About to start"}
  - {commitment: "Solar 60 MW Prayagraj", implied_date: "Q4 FY27", ref: "p9 l195; p17 l360-362; p16 l331", status_word: "In progress"}
  - {commitment: "Iron ore mines operational", implied_date: "FY30", ref: "p9 l194", status_word: "In progress"}
  - {commitment: "Rs ~2,000/t EBITDA gain from mines-to-mill linkage", implied_date: "FY30", ref: "p10 l212-214; p13 l290", status_word: "targeted (management estimate)"}
  - {commitment: "Total capex Rs 3,000 Cr", implied_date: "FY2029-30", ref: "p11 l231-233; p6 l137-141", status_word: "initiated (Rs 652.54 Cr spent)"}
  - {commitment: "Self-funded growth, no incremental debt", implied_date: "ongoing", ref: "p10 l204-208", status_word: "claimed (conflicts with filed borrowings)"}
  - {commitment: "Post-enhancement power 160 MW, mines 70,00,000 MT", implied_date: "NOT FOUND", ref: "p17 l371-372; R1491", status_word: "not stated"}
  - {commitment: "Solar 18 MW Sidhpur", implied_date: "deck Jul 2026; call restart by November 26 (ASR_SUSPECT)", ref: "p6 l137; p9 l193; p17 l369-372 (R1490); concall l152", status_word: "disputed (deck 'Commissioned'/'Delivered'; p17 and call: not yet operating)"}
  - {commitment: "Iron ore mines preferred bidder", implied_date: "2024-25", ref: "p9 l192", status_word: "completed"}
  - {commitment: "Rs 3.50 crore annual cost savings", implied_date: "not stated", ref: "p11 l244", status_word: "not stated"}
gate_a3: pass
blank_checks: []
analyst_note: "The deck's value is the volume data the filing lacked. TMT sales fell 14.6% QoQ and 6.8% YoY while revenue held flat QoQ and rose 13% YoY. Own steel did not carry revenue; DRI, pellet and traded sales did (A3P-05, render-confirmed). This confirms the review's bear reading of the traded-goods surge. The deck's own metrics hide it. EBITDA/t and the NSR bridge divide all revenue, trading included, by billet production tonnes (A3P-04). EBITDA mixes bases, and FY26 carries other income plus inflated margin bars (A3P-03). The p6/p10 ratios are six-month or non-standard (A3P-12); none feeds Section 1B. 'Self-funded, no incremental debt' conflicts with filed H1 borrowings (A3P-06). The tracker covers Rs 1,191 Cr of Rs 3,000 Cr, and the Q4 FY27 solar is 2.1% spent (A3P-07, A3P-08). Sidhpur is counted outside existing capacity on p17, and the call puts its restart in November, despite 'Commissioned Jul 2026' (A3P-15). Promoter buying of about 0.9 pp in a falling quarter is the one bull datum (A3P-20). Six deck errors are listed for A4."
```
