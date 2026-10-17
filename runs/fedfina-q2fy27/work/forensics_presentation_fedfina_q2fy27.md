# A3 FORENSIC NOTES: FEDFINA Q2 FY27 (doctype: presentation)

Company: Fedbank Financial Services Ltd (FEDFINA) | Quarter: q2fy27 | Doctype: presentation (42 slides, investor deck under LODR 46(2), letter dated October 15, 2026)
Inputs read: A1 structured extraction (R001-R1102, all 1102 rows), A1 fulltext (lines 1-1248, all 42 pages), A2 ledger (1102 IDs, 42 slides, gate_a2 pass). Prior-quarter extract: ND. Source PDF and inputs/ not opened.
Lender reading applied throughout (NBFC: gold loan + mortgage). Product lines are treated as segments for F12.
Line cites refer to extracted/fedfina-presentation-q2fy27-fulltext.md.

## 0. LEDGER RECONCILIATION

- Rows in ledger: 1102. Rows read in structured file: 1102. Fulltext lines read: 1-1248 (every [page N] block, incl. the 5 no-row divider slides p4, p9, p20, p32, p37). Reconciled: 100%.
- ZERO_STANDING rows: 1 (R1024), handled in F1.
- RESTATED pairs (R024/R049, R025/R048, R026/R052, R027/R051, R041/R054, R042/R193, R043/R186): all tie, value for value.
- Arithmetic tie-outs run (all pass within rounding): P&L cascade slide 35 for all four columns (e.g. Q2 FY27 693.2 - 288.3 = 404.9 ~ 404.8; 431.5 - 226.4 = 205.1; 205.1 - 27.1 = 178.0; 178.0 - 47.3 = 130.7 ~ 130.8); balance sheet slide 34 four columns (Q2 FY27 assets 827+16,020+799+527+368 = 18,541 ~ 18,540; liabilities 3,165+14,602+773 = 18,540); RoA tree slide 36 (15.1 - 6.3 = 8.8; 8.8 + 0.0 + 0.6 = 9.4; 9.4 - 4.9 = 4.5; 4.5 - 0.6 = 3.9; less 1.0 tax = 2.8 rounded); RoE 130.8 x 4 / avg SF 3,084 = 16.96%; RoA 523.2 / avg TA 18,393.5 = 2.84%; credit cost 27.1 x 4 / 18,393.5 = 0.59%; PCR 104.7 / 296 = 35.37%; off-book % per product (gold (11,917 - 9,421) / 11,917 = 20.9%); AUF 16,264 - ECL 243.5 = 16,020.5 = Loans R898; product AUM 11,917 + 6,059 + 3,922 + BL 135 = 22,033 ~ 22,035; disbursal splits per quarter (Q2 FY27 5,822 + 645 + 210 = 6,677 ~ 6,676; non-gold 645 + 210 = 855 = R401); CAGR labels (43.2%, 34.3%); sell-down headline groups (see section 1).

## 1. SERIES ATTRIBUTION CROSS-CHECKS (A1 by-position rows; caller instruction)

| slide | rows | A1 attribution | cross-check | result |
|---|---|---|---|---|
| 8 | R180-R193 | RoE / RoA by position | Q2 FY26, Q1 FY27, Q2 FY27 equal slide 33 R867-R869 / R861-R863; Q1-Q4 FY26 RoA mean 2.45% ~ FY26 2.4% (R866); RoE mean 12.6% = FY26 R872 | RECONCILES. Usable. Axis floors 2.0% (RoA) and 7.5% (RoE), lines 215, 212. |
| 16 | R289-R300 | market chart by position | third-party (BIS, RBI, Crisil, RHP, line 452); no company identity available | NOT TESTABLE. Do not rely for thesis numbers. |
| 19 | R340-R347 | branch / AUM mix not resolvable | AUM mix computed from slide 24 shares x slide 27 AUM: South 0.35 x 11,917 + 0.45 x 9,982 = 8,663 (39%); West 7,539 (34%); North 5,578 (25%) | AUM mix RESOLVED: South 40% (R345), West 35% (R346), North 25% (R344), East <1% (R347). Branch mix (R340-R343) stays unresolved. |
| 19 | R374-R380 | branch expansion segments not resolvable | tie to slide 23 gold branches: FY26 558 + 70 = 628 (R494); Q2 FY27 634 + 72 = 706 (R496) | RESOLVED: Gold-only 558 -> 634, Co-located 70 -> 72, MSME Hubs 129 -> 125. 706 = gold + co-located; 197 = co-located + hubs. |
| 22 | R455-R464 | MTL / STL annual by "left-to-right position" (ascending) | x-axis line 636 column offsets: MTL FY25 col 88, FY26 col 98; STL FY22-FY26 cols 108/118/128/138/148. Grep offsets: 2,303 at 80-95, 2,180 at 96-110, 1,475 at 120-137, 1,102 at 110-125, 1,004 at 130-145, 904 at 140-160. Identity: quarterly non-gold = MTL + STL exactly (Q2 FY26 554 + 206 = 760; Q3 545 + 208 = 753; Q4 632 + 289 = 921), so FY26 MTL + STL must be <= 3,084 (R406). A1 gives 2,303 + 1,475 = 3,778 (fails). Offset reading gives 2,180 + 904 = 3,084 (exact). | A1 WRONG. Corrected: MTL FY22 518, FY23 1,091, FY24 1,359, FY25 2,303, FY26 2,180. STL FY22 765, FY23 1,102, FY24 1,475, FY25 1,004, FY26 904. See FN13. |
| 23 | R487-R491 | gold tonnage by position | 12.9 / 11.1 = 1.162 = "YoY Growth: 16%" (R481, line 660) | RECONCILES. |
| 24 | R507-R548 | stack position | every column sums to 99-101% | PLAUSIBLE. Usable. |
| 25 | R552-R581 | yields / spreads / CoB by position | annual: yield - CoB = spread in all 5 years (FY22 16.0 - 8.2 = 7.8 ... FY26 16.7 - 8.6 = 8.1). Quarterly under A1: Q1 FY27 16.7 - 8.6 = 8.1 vs 7.7 stated; Q2 FY27 16.4 - 8.8 = 7.6 vs 7.9 stated (both FAIL). Grep offsets: 16.4% (line 744) sits at col 190-198 = Q1 FY27 column (line 762); last 16.7% (line 743) at col 208-216 = Q2 FY27 column. Spread 7.7/7.9 and CoB 8.6/8.8 confirmed at the same two columns. | A1 SWAPPED R560/R561. Corrected: Q1 FY27 yield 16.4%, Q2 FY27 yield 16.7%. Then Q1 16.4 - 8.6 = 7.8 ~ 7.7; Q2 16.7 - 8.8 = 7.9 = 7.9. Slide reconciles internally. It does NOT reconcile to the P&L (FN25). |
| 26 | R587-R593 | funding pie not resolvable | labels sum to 100%; no identity | UNRESOLVED. Do not use. |
| 27 | R663-R666 | sell-down headline groups unassigned | 193 + 527 + 457 + 284 = 1,461 (FY24); 577 + 536 + 486 + 531 = 2,130 ~ 2,129 (FY25); 1,044 + 578 + 313 + 645 = 2,580 (FY26); 530 + 1,085 = 1,615 (H1 FY27) | RESOLVED: FY24 1,461; FY25 2,129; FY26 2,580 (incl. Rs 886 Cr one-off BL assignment, R681); H1 FY27 1,615. |
| 28 | R687-R690 | STL CIBIL mix not resolvable | ~78% mortgage >700 (R682): 0.83 x 6,059 + x x 3,922 = 0.78 x 9,981 gives x = 70% | PARTLY RESOLVED: STL >700 = 70% (R687). Other three slices unresolved. |

Pipeline flag for the orchestrator: A1 rows R455-R464 and R560-R561 carry wrong period attribution. A2 section 2 did not list slide 22 among SERIES_BY_POSITION rows. Downstream stages must use the corrected values above.

## 2. FINDINGS TABLE

| id | check | ledger row ref | line / slide | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FN01 | F1 | R1024 (also R960-R963) | line 1088, slide 36 | "Net Gain on DA / Average total Assets 0.2% -0.3% 0.0% 0.1%" | NEUTRAL-FACT | Not a dormant line. The 0.0% is a rounded -Rs 1.2 Cr (line 1057, "Net Gain on Direct Assignment 6.6 -12.9 -1.2"). The line exists because the company assigns loans every quarter; it anticipates DA gain or loss. Live input to FN08. |
| FN02 | F6 | R021 | line 86, slide 3 | "The Company does not undertake to make any announcement ... or update any forward looking statements" | AMBIGUOUS | Deck carries no numeric FY27 guidance (no AUM, credit cost, RoA or branch targets). Checklist item 1 asks for "FY27 guidance issued". A4: confirm from the concall whether guidance was given, and on what metric. |
| FN03 | F7 | R722 | line 921, slide 29 | "Asset Quality reflecting gold loan industry changes" | AMBIGUOUS | Management pre-attributes the Stage 3 rise to an unnamed industry change (the deck does not say which; NOT FOUND). Pre-emptive framing suggests gold Stage 3 stays elevated next quarter. A4: which change, how much of Rs 47.6 Cr gold GS3 is technical (renewal / bullet timing) vs true default, and auction loss to date. |
| FN04 | F8 | R996-R1003 | line 1073, slide 35 | "Tax Expense 27.3 39.1 47.3 117.4" | AMBIGUOUS | ETR Q2 FY27 = 47.3 / 178.0 = 26.6% vs Q1 FY27 25.5%, Q2 FY26 25.4%, FY26 25.5%, statutory 25.17%. Excess ~Rs 2.5 Cr. Deck has no current / deferred split. Candidates: prior-year tax adjustment, non-deductible items, DTA reversal on ECL movement. Verify at the results filing. |
| FN05 | F9 | R798, R800, R922-R925, R1004-R1006 | lines 980, 982, 1036 | "ECL provision % of assets are net of amounts transferred to OCI on Fair valuation of eligible loans" | AMBIGUOUS | Part of the book is fair-valued through OCI (loans held to collect and sell via DA). Part of impairment goes to OCI, not to P&L credit cost, so the 0.6% credit cost may not be total impairment. Reserves roll-forward: Q2 +162 (2,628 -> 2,790) vs PAT 130.8 = +31.2 Cr non-PAT; Q1 +76 (2,552 -> 2,628) vs PAT 114.4 = -38.4 Cr non-PAT. Candidates: OCI fair-value reserve, FY26 dividend (NOT FOUND in deck), ESOP reserve. Verify OCI line at results filing / AR. |
| FN06 | F10 | R918-R921 | line 1035, slide 34 | "Share Capital 374 375 375 374" | NEUTRAL-FACT | Paid-up capital moved Rs 374 Cr (FY26) -> 375 Cr (Q1 FY27), flat in Q2. Deck names no corporate action; ESOP allotment is the likely source. Rounded to Rs 1 Cr, so the move may be smaller. No basic / diluted EPS in the deck; spread not assessable. A4 cross-checks against known ESOPs. |
| FN07 | F12 | R639, R640, R642, R643, R656-R658, R030, R680, R069 | lines 119, 826, 832, 846, 150 | "Net growth in Gold AUM of ₹726 Cr in this quarter" vs "Gold Loan ... 9,473 9,421" (AUF) | FORWARD-SIGNAL | All of the Q2 gold growth was off-book. Gold AUM +726 Cr but on-book gold AUF fell Rs 52 Cr (9,473 -> 9,421); gold off-book share 15.3% -> 20.9%. Total AUM +899 Cr, total AUF +27 Cr. Borrowings -0.6% QoQ. Sell-down 530 -> 1,085 Cr QoQ; H1 FY27 sell-down 1,615 Cr vs FY26 ex-BL one-off 1,694 Cr. Growth now depends on the appetite of assignment / co-lending buyers. The buyer identity is not in the deck (a related-party buyer would matter, since Federal Bank owns 60.6%). CRAR +25bps QoQ also rests on this. |
| FN08 | F12 | R961, R962, R679, R680 | lines 1057, 846 | "Net Gain on Direct Assignment 6.6 -12.9 -1.2" | AMBIGUOUS | DA gain was negative two quarters running while sell-down volume doubled. Reading A: excess-spread unwind on short-tenor gold pools that prepaid (accounting timing). Reading B: pools sold at thin or negative excess spread, so off-book growth is being bought. Separating observation: gross DA gain on new pools vs reversal on old pools, and the retained-interest asset trend. |
| FN09 | F12 | R761-R796, R993, R994, R085 | lines 961-974, 1069 | "ECL provision % of assets 15.41% 16.53% 12.61%" (Stage 2) | FORWARD-SIGNAL | Stage 2 assets +35% QoQ (436 -> 587) while Stage 2 coverage fell 16.53% -> 12.61%; Stage 3 coverage fell 38.36% -> 35.37%; Stage 1 rose 0.34% -> 0.42%. At Q1 FY27 stage-wise coverage, the Q2 ECL stock would be ~Rs 262.9 Cr vs 243.5 actual, a shortfall of ~Rs 19.4 Cr. Credit cost would be ~Rs 46.5 Cr = ~1.0% of average total assets, vs 0.6% reported and the 1.1% tripwire. Post-tax ~Rs 14.5 Cr = ~11% of Q2 PAT and ~88% of the Rs 16.4 Cr QoQ PAT gain. Reading A: mix shift into gold Stage 2 / 3 with low LGD (68% LTV collateral). Reading B: provision release flattering PAT. Separating observation: product-wise Stage 2 split and coverage. |
| FN10 | F12 | R713-R715, R788-R790 | lines 909-911, slide 29 | "PCR ... 38.4% 35.4%" | CONFIRMATORY-NEGATIVE | Checklist item 2 (PCR >= 38% and rising) MISSED: 35.4%, down 300bps QoQ. Red line (< 32%) not hit. The Pillar 2L override text ("self-withdraws to 0.80x if ... PCR thins further") reads as met on a QoQ basis. FLAG for operator; the decision stays human. Cause is largely gold mix (gold PCR 10.5%, line 942). |
| FN11 | F12 | R719-R721, R734-R739, R497-R501, R481, R487-R491 | lines 914, 942, 678-679, 665 | "Gold Loan 9,421 47.6 42.6 10.5% 0.4% 0.1% 0.5%" | FORWARD-SIGNAL | Gold GS3 rose from ~0.1% to 0.5% QoQ (about Rs 5-14 Cr on the rounded 0.1% to Rs 47.6 Cr). This drives most of the +44 Cr total Stage 3 rise (252 -> 296). Portfolio LTV 59.3% (Q3 FY26) -> 68.0% (+870bps); origination LTV 72.1% (R327). Tonnage +1.6% QoQ (12.7 -> 12.9 t) vs gold AUM +6.5%; AUM per tonne ~Rs 606 Cr -> ~Rs 924 Cr YoY. Growth is gold price and LTV, not grams. A gold-price fall now hits a thinner collateral cushion. Checklist item 8 is met on disclosure. |
| FN12 | F12 | R542-R548, R710-R712, R727-R732 | lines 698-702, 911, 939 | Mortgage North share "6% 9% 14% 19% 24% 30% 32%" | AMBIGUOUS | North mortgage share rose from 6% (FY21) to 32% (Q2 FY27), so the fastest-growing region is the least seasoned. Mortgage GS3 3.2% -> 3.4% -> 3.4%; NS3 2.0% -> 2.2%. A4: vintage-wise GS3 for North-originated mortgage. |
| FN13 | F12 | R455-R464 (corrected), R406, R470-R479 | lines 623-636, 641 | "28,326 2,303 1,475" (line 623; offsets place 2,303 at MTL FY25 and 1,475 at STL FY24) | CONFIRMATORY-NEGATIVE | Corrected series (section 1): STL disbursals 1,475 (FY24) -> 1,004 (FY25) -> 904 (FY26), down 39% in two years. MTL 2,303 (FY25) -> 2,180 (FY26), down 5%. H1 FY27 STL 144 + 210 = 354 (annualised ~708) is still below FY26. MTL H1 FY27 529 + 645 = 1,174 (annualised ~2,348) is recovering. Checklist item 7 (STL disbursals > Rs 208 Cr) cleared by Rs 2 Cr (210, R479). The deck says nothing on STL collections in-housing. A1's ascending attribution showed the reverse trend; downstream must not use it. |
| FN14 | F12 | R376-R380, R492-R496 | lines 541-548, 677 | "558+129+70" (FY26) / "634+72+125" (Q2 FY27) | NEUTRAL-FACT | Resolved by tie to slide 23 (section 1). Gold-only branches 558 -> 634, co-located 70 -> 72, MSME hubs 129 -> 125. All net branch additions since FY26 are gold. Mortgage hub count shrank by 4. Mortgage distribution is not expanding, consistent with FN13. |
| FN15 | F12 | R033, R075, R078, R980-R984, R855-R858, R485, R486, R503 | lines 123, 691, 1065, 1011 | "*Reduction due to opening 74 new branches" | FORWARD-SIGNAL | Q2 added 74 branches (+9.8%) and 544 employees (+10.1%); opex +7.8% QoQ; gold AUM per branch 17.7 -> 16.9 Cr. C/I fell only 36bps QoQ (52.8% -> 52.5%). New-branch cost runs ahead of AUM. H2 C/I depends on the ramp of 74 new branches. Checklist item 4 met (52.5% < ~57%). |
| FN16 | F12 | R1062-R1069, R885-R890, R058, R068 | line 1098, slide 36; line 1016 | "Average total assets / Average Shareholders' Fund (x) 5.0 5.9 6.0 5.2" | FORWARD-SIGNAL | RoE 12.0% -> 17.0% YoY. RoA factor x1.17 (2.4 -> 2.8) and leverage factor x1.20 (5.0 -> 6.0): about half of the RoE gain is leverage. SF +16.8% YoY vs borrowings +42.7% and AUM +36.6%. CRAR 21.0%, -68bps YoY. If assignment slows (FN07), on-book growth consumes capital: either an equity raise or RoE gives back part of the gain. Checklist item 5 met on the number; the durability is the question. |
| FN17 | F12 | R594, R600, R611, R602 | lines 779-781, slide 26 | "< 3 months ... 186" | AMBIGUOUS | ALM < 3-month cumulative surplus is Rs 186 Cr on Rs 3,291 Cr outflows (5.7%). The gold-heavy book gives a large < 1-year surplus (Rs 7,506 Cr), so the thin bucket is the near one. A4: liquidity buffer composition and undrawn sanctioned lines. |
| FN18 | F14 | R586, R599, R605, R616 | lines 776, 805-807 | "(Cumulative) ₹ Cr" with "> 5 year ... 2,024 ... 3,781 ... (1,757)" | NEUTRAL-FACT | Header says cumulative, but the > 5-year row is a standalone bucket (3,781 < 14,996 cumulative at < 5 years). Drafting inconsistency. Read the > 5-year row as a bucket. |
| FN19 | F14 | R791-R793, R656-R658, R914 | line 973, slide 31 | "Total assets 11,743 16,237 16,264" | NEUTRAL-FACT | Labelled "Total assets" on the ECL slide but equals total loan assets / AUF (slide 27), not balance-sheet total assets (18,540, line 1033). Label error; the numbers tie to AUF. |
| FN20 | F14 | R797-R800 | lines 957, 979-982 | "Q2 FY26*^" with "* Debited to P&L" and "^ ECL provision" | AMBIGUOUS | Only the Q2 FY26 column carries the * and ^ markers, and each symbol carries two meanings. The Q2 FY26 column may sit on a different basis from Q1 / Q2 FY27, so the YoY coverage move (PCR 32.0% -> 35.4%) may not be like-for-like. A4: confirm basis per column. |
| FN21 | F14 | R095, R1098-R1100 | lines 159, 1231-1233 | "3. Employees excludes apprentices" / "This program is designed to equip apprentices" | AMBIGUOUS | Headcount (5,920) excludes apprentices while a CSR apprentice programme runs. Per-employee productivity is overstated by an unknown amount. A4: apprentice count and whether their cost sits in opex or CSR. Low weight. |
| FN22 | F14 | R324, R332, R606-R610, R624 | lines 469, 485, 815 | "(17.7^%)" and "^ Portfolio yield : On i-GAAP basis" | NEUTRAL-FACT | Gold origination yield is footnoted as "Portfolio yield" on an I-GAAP basis; MTL / STL yields carry no marker. Slide 26 CoB is also I-GAAP while slides 25 / 35 are Ind-AS. Mixed accounting bases sit side by side; cross-slide comparison needs care. |
| FN23 | F16 | R560, R561 (corrected), R557-R581 | lines 743-744, 751, 756, 762 | "16.8% 16.7%" (line 743, last value at Q2 FY27 col) / "16.4%" (line 744, Q1 FY27 col) | NEUTRAL-FACT | A1 swapped Q1 / Q2 FY27 yields. Corrected: Q1 FY27 16.4%, Q2 FY27 16.7%. Yield rose 30bps QoQ, not fell. With the correction, yield - CoB = spread within 0.1pp in all ten periods. Spreads Q2 FY26 8.4% -> Q2 FY27 7.9% (-50bps YoY), deck tagline "Rangebound Spreads" (line 767). |
| FN24 | F16 | R583, R584, R552-R556, R567-R576 | line 768, slide 25 | "Yearly Yields, CoB, and Spreads restated from two-point average to quarterly average; quarterly metrics remain on two-point average" | AMBIGUOUS | Methodology restatement of the annual series. Annual FY22-FY26 figures in this deck are not comparable with earlier decks, and annual and quarterly series on one slide use different averaging. A4: old vs restated FY26 yield / CoB / spread, and why restate now. |
| FN25 | F16 | R577-R581, R606-R610, R624, R946-R953, R932-R935, R656-R658 | lines 756, 781, 815, 1051-1053, 1038 | "Daily Average Cost of Borrowing* 8.19% 7.87% 7.83% 7.80% 7.79%" | AMBIGUOUS | Two CoB measures move apart. Slide 25 CoB went 8.6% -> 8.8% QoQ while slide 26 daily I-GAAP CoB went 7.80% -> 7.79%; the gap widened from 51bps (Q2 FY26) to 101bps (Q2 FY27). P&L interest expense / two-point average borrowings gives 7.87% (Q2 FY27: 288.3 x 4 / 14,649) and 7.74% (Q1 FY27: 272.7 x 4 / 14,090). That is close to the I-GAAP series, not to the 8.8% on slide 25. Interest income / average AUF = 17.1% vs 16.7% presented. P&L-implied spread is ~9.2% vs 7.9% presented. The slide 25 basis is undefined. A4: the slide 25 CoB numerator / denominator, and which series management steers on. |

Counts: 25 findings. FORWARD-SIGNAL 5 (FN07, FN09, FN11, FN15, FN16). AMBIGUOUS 11 (FN02, FN03, FN04, FN05, FN08, FN12, FN17, FN20, FN21, FN24, FN25). CONFIRMATORY-NEGATIVE 2 (FN10, FN13). NEUTRAL-FACT 7 (FN01, FN06, FN14, FN18, FN19, FN22, FN23).

## 3. CHECKLIST SCORECARD

| check | status | one-line basis |
|---|---|---|
| F1 | FINDING | One ZERO_STANDING row (R1024); it is a rounded -Rs 1.2 Cr, live DA line (FN01). |
| F2 | N.A. | Presentation carries a single reporting set; no standalone vs consolidated split. No subsidiaries or JVs named in the deck. |
| F3 | N.A. | No standalone vs consolidated cost lines in a deck; shell test needs the results filing. |
| F4 | N.A. | No auditor report or Other Matters paragraph in the deck. Lender note: no JV / associate named, so no unaudited contribution is visible. |
| F5 | N.A. | No EoM / going-concern text in the deck; prior-quarter extract ND, so no verbatim diff possible. |
| F6 | FINDING | Lexicon sweep (grep, case-insensitive): only boilerplate hits ("will be", line 74; "shall be", line 78; "subject to", line 82) plus "being developed" (line 1198), "launched" (line 1211), "launch" (line 1231), "aim to" (line 1235). No dated financial commitment and no FY27 guidance (FN02). Register in section 4. |
| F7 | FINDING | Lexicon hedge only in safe harbor (line 82, boilerplate). Non-lexicon hedge on slide 29 tagline attributes asset quality to "gold loan industry changes" (FN03). |
| F8 | FINDING | Deck carries PBT and tax: ETR 26.6% in Q2 FY27 vs 25.4-25.5% in the other three periods and 25.17% statutory (FN04). No deferred-tax split in deck. |
| F9 | FINDING | No actuarial OCI line in deck. ECL footnotes show transfers to OCI on fair-valued loans; reserves move by +31.2 / -38.4 Cr beyond PAT in Q2 / Q1 (FN05). |
| F10 | FINDING | Paid-up capital 374 -> 375 Rs Cr with no stated corporate action; no EPS shown (FN06). |
| F11 | PASS | Share capital + R&S = SF in all four columns (374 + 2,336 = 2,710; 375 + 2,628 = 3,003; 375 + 2,790 = 3,165; 374 + 2,552 = 2,926). SF ties across slides 6, 7, 33, 34. BVPS 3,165 / 37.5 Cr shares = 84.4. No third-party net worth figure in deck. Reserve roll-forward gap is carried in F9. |
| F12 | FINDING | Product-segment reading (gold, mortgage, business loan run-off) plus funding, ALM and leverage: FN07-FN17. |
| F13 | N.A. | No board outcome in the deck. Board roster as on September 30, 2026 (line 266, 8 directors incl. 5 independent, 2 Federal Bank nominees) recorded for next-quarter diff; no term dates. |
| F14 | FINDING | Label and basis inconsistencies: ALM "cumulative" header (FN18), ECL "Total assets" (FN19), Q2 FY26 column markers (FN20), apprentice exclusion (FN21), I-GAAP / Ind-AS mix (FN22). |
| F15 | N.A. | No consolidation entity list in the deck; prior extract ND. |
| F16 | FINDING | Prior deck ND, so dropped-metric diff is not assessable. Within-deck reframing found: annual yield / CoB / spread restated to a new averaging basis (FN24); two CoB series moving apart and not reconciling to P&L (FN25); slide 25 attribution corrected (FN23). Axis floors on slide 8 (2.0% / 7.5%) noted; no prior to compare. |
| F17 | N.A. | Concall-specific silence audit; this doctype is a presentation. Deck coverage of the Notion checklist is recorded in section 5 for A4. |

## 4. COMMITMENT REGISTER (F6)

| commitment | implied date | note / slide ref | status word |
|---|---|---|---|
| 74 new branches commissioned, total 831 across 18 states and UTs | Q2 FY27 (done) | slide 5, line 123 (R033, R034) | completed |
| Stree Sakthi Gold Loan Schemes launched; portfolio crossed Rs 100 Cr | launched 07 January 2026; milestone by Q2 FY27 | slide 40, line 1211 (R1095, R1096) | completed |
| ESG KPI list in place; "metrics for evaluation are being developed" | undated | slide 40, lines 1194-1198 (R1091) | underway |
| Nation Skill Building CSR programme for apprentices ("proud to launch") | undated; first appears in this deck | slide 41, line 1231 (R1099) | initiated |
| "Building a modern, innovative and future-ready digital ecosystem" | undated aspiration | slide 38, line 1135 (R1081) | underway |

Excluded: "Retail credit growth to continue" FY28P Rs 125 tn (R288, line 417) is a third-party projection (RBI, Crisil), not a company commitment. Slide taglines (R195, R307, R449, R480, R502, R549, R582, R623, R697, R753, R1084, R1089, R1097) are descriptive and carry no date. No numeric FY27 guidance exists in the deck (FN02).

## 5. NOTION MONITORING CHECKLIST: DECK COVERAGE (supplementary to F17 N.A.; for A4)

| # | checklist item | deck evidence (row, line) | reading |
|---|---|---|---|
| 1 | Credit cost <= 1.1% of avg assets; FY27 guidance issued | 0.6% (R085, line 155-157; R1048 line 1094); no guidance in deck | Met as reported. At constant Q1 coverage ~1.0% (FN09). Guidance: check concall (FN02). |
| 2 | PCR >= 38% and rising toward 50%+ (red < 32%) | 35.4% vs 38.4% Q1 (R714-R715, line 909-911) | MISSED. Not red. Override clause "PCR thins further" reads as met (FN10). |
| 3 | Gold branch count 140-150; AUM per branch > Rs 13.3 Cr | gold branches 706 (R496, line 677); AUM per branch 16.9 Cr (R486, line 663) | Per-branch MET. The "140-150" band does not match any deck count (706 gold branches; +78 gold branches in H1 FY27, 628 -> 706). The checklist definition needs operator clarification. |
| 4 | Cost-to-income below ~57% and falling | 52.5% vs 52.8% Q1, 56.9% Q2 FY26 (R855-R857, line 1011) | MET; QoQ fall only 36bps (FN15). |
| 5 | ROE toward 14-15%; ROA >= 2.5% | RoE 17.0%, RoA 2.8% (R869, R863, lines 1012-1013) | MET; about half of the RoE gain is leverage (FN16). |
| 6 | GNPA / GS3 at or below ~1.9-2.1% | 1.8%, +27bps QoQ (R875-R876, line 1014) | MET; rising QoQ, gold-driven (FN11). |
| 7 | ST LAP collections in-housing complete; disbursals > Rs 208 Cr | STL Q2 FY27 210 Cr (R479, line 641-644); in-housing not mentioned | Disbursals MET by Rs 2 Cr; annual STL trend down 39% FY24-FY26 (FN13). In-housing: NOT FOUND in deck. |
| 8 | Gold tonnage disclosed and rising | 12.9 t, +16% YoY (R481, R491, lines 660-665) | MET; QoQ +1.6% vs gold AUM +6.5% (FN11). |

Tripwires: credit cost > 1.1%: not triggered as reported (0.6%). ROE < 14% by FY28: not triggered (17.0%). PCR < 32%: not triggered (35.4%). Pillar 2L override self-withdraw clause: the PCR limb reads as met (38.4% -> 35.4%). FLAG for operator; the decision stays human.

## 6. ITEMS FLAGGED FOR A4 (FORWARD-SIGNAL and AMBIGUOUS)

FORWARD-SIGNAL: FN07 (off-book-funded growth), FN09 (coverage-driven credit cost and PAT), FN11 (gold GS3 and LTV), FN15 (branch cost ahead of AUM), FN16 (leverage-led RoE).
AMBIGUOUS: FN02 (guidance), FN03 (industry-change framing), FN04 (ETR), FN05 (OCI / reserves), FN08 (negative DA gain), FN12 (North mortgage seasoning), FN17 (ALM near bucket), FN20 (column basis), FN21 (apprentices), FN24 (annual restatement), FN25 (CoB basis).
Highest priority for questions: FN09 together with FN10 (one question set: product-wise Stage 2 / 3 coverage), then FN07 with FN08 (one set: assignment economics and buyer identity), then FN25.

```yaml
stage: A3-forensics
company: "FEDFINA"
quarter: "q2fy27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "C:/Users/SUMIT SHARMA/repos/inflection-pipeline/.claude/worktrees/q2fy27/runs/fedfina-q2fy27/work/forensics_presentation_fedfina_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: FINDING
  F10: FINDING
  F11: PASS
  F12: FINDING
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "FN01", check: "F1", line: "1088 (R1024); 1057", classification: "NEUTRAL-FACT", implication: "0.0% DA/assets is a rounded -Rs 1.2 Cr; live DA line, feeds FN08"}
  - {id: "FN02", check: "F6", line: "86 (R021)", classification: "AMBIGUOUS", implication: "No numeric FY27 guidance in deck; checklist item 1 needs the concall"}
  - {id: "FN03", check: "F7", line: "921 (R722)", classification: "AMBIGUOUS", implication: "Stage 3 rise pre-attributed to unnamed gold industry changes; gold GS3 may stay elevated"}
  - {id: "FN04", check: "F8", line: "1071-1073 (R996-R1003)", classification: "AMBIGUOUS", implication: "ETR 26.6% vs 25.17% statutory, ~Rs 2.5 Cr excess; cause not in deck"}
  - {id: "FN05", check: "F9", line: "980, 982, 1036", classification: "AMBIGUOUS", implication: "ECL partly routed via OCI on fair-valued loans; reserves +31.2 Cr / -38.4 Cr beyond PAT in Q2 / Q1"}
  - {id: "FN06", check: "F10", line: "1035 (R918-R921)", classification: "NEUTRAL-FACT", implication: "Share capital 374 -> 375 Rs Cr, no stated corporate action; no EPS in deck"}
  - {id: "FN07", check: "F12", line: "119, 826, 832, 846", classification: "FORWARD-SIGNAL", implication: "Gold AUM +726 Cr but on-book gold AUF -52 Cr; total AUF +27 vs AUM +899; growth rides assignment buyers"}
  - {id: "FN08", check: "F12", line: "1057, 846", classification: "AMBIGUOUS", implication: "DA gain -12.9 / -1.2 Cr while sell-down doubled to 1,085 Cr; EIS unwind vs thin-spread sales"}
  - {id: "FN09", check: "F12", line: "961-974, 1069", classification: "FORWARD-SIGNAL", implication: "At Q1 coverage ECL would be ~19.4 Cr higher; credit cost ~1.0% vs 0.6% reported and 1.1% tripwire; ~88% of QoQ PAT gain"}
  - {id: "FN10", check: "F12", line: "909-911 (R714-R715)", classification: "CONFIRMATORY-NEGATIVE", implication: "PCR 38.4% -> 35.4%; checklist item 2 missed; Pillar 2L override clause 'PCR thins further' reads as met; operator flag"}
  - {id: "FN11", check: "F12", line: "914, 942, 678-679, 665", classification: "FORWARD-SIGNAL", implication: "Gold GS3 0.1% -> 0.5% (Rs 47.6 Cr), LTV 59.3% -> 68.0%, tonnage +1.6% QoQ vs AUM +6.5%; price-driven growth, thinner collateral cushion"}
  - {id: "FN12", check: "F12", line: "698-702, 911, 939", classification: "AMBIGUOUS", implication: "Mortgage North share 6% -> 32%; unseasoned book; mortgage GS3 3.2% -> 3.4%"}
  - {id: "FN13", check: "F12", line: "623-636, 641", classification: "CONFIRMATORY-NEGATIVE", implication: "Corrected slide 22: STL disbursals 1,475 (FY24) -> 904 (FY26), MTL 2,303 -> 2,180; A1 R455-R464 misattributed"}
  - {id: "FN14", check: "F12", line: "541-548, 677", classification: "NEUTRAL-FACT", implication: "Branch split resolved: gold 558 -> 634, co-located 70 -> 72, MSME hubs 129 -> 125; all adds are gold"}
  - {id: "FN15", check: "F12", line: "123, 691, 1065, 1011", classification: "FORWARD-SIGNAL", implication: "+74 branches, +544 staff, opex +7.8% QoQ, AUM per branch 17.7 -> 16.9; H2 C/I depends on ramp"}
  - {id: "FN16", check: "F12", line: "1098, 1016", classification: "FORWARD-SIGNAL", implication: "About half the RoE gain (12.0% -> 17.0%) is leverage 5.0x -> 6.0x; SF +16.8% vs borrowings +42.7%; capital need if DA slows"}
  - {id: "FN17", check: "F12", line: "779-781", classification: "AMBIGUOUS", implication: "ALM <3m cumulative surplus Rs 186 Cr on 3,291 Cr outflows (5.7%)"}
  - {id: "FN18", check: "F14", line: "776, 805-807", classification: "NEUTRAL-FACT", implication: "ALM header says cumulative; >5 year row is a bucket"}
  - {id: "FN19", check: "F14", line: "973", classification: "NEUTRAL-FACT", implication: "ECL slide 'Total assets' 16,264 is AUF, not balance-sheet total assets 18,540"}
  - {id: "FN20", check: "F14", line: "957, 979-982", classification: "AMBIGUOUS", implication: "Only Q2 FY26 column carries */^ basis markers; YoY coverage may not be like-for-like"}
  - {id: "FN21", check: "F14", line: "159, 1231-1233", classification: "AMBIGUOUS", implication: "Headcount excludes apprentices while a CSR apprentice programme runs; productivity overstated by unknown amount"}
  - {id: "FN22", check: "F14", line: "469, 485, 815", classification: "NEUTRAL-FACT", implication: "I-GAAP and Ind-AS bases mixed across slides 17, 25, 26, 35"}
  - {id: "FN23", check: "F16", line: "743-744, 751, 756, 762", classification: "NEUTRAL-FACT", implication: "A1 swapped R560/R561; corrected Q1 FY27 yield 16.4%, Q2 FY27 16.7%; slide 25 then reconciles internally"}
  - {id: "FN24", check: "F16", line: "768 (R583)", classification: "AMBIGUOUS", implication: "Annual yield / CoB / spread restated to quarterly average; not comparable with prior decks"}
  - {id: "FN25", check: "F16", line: "756, 781, 815, 1051-1053, 1038", classification: "AMBIGUOUS", implication: "Slide 25 CoB 8.8% vs P&L-implied 7.87% and I-GAAP daily 7.79%; gap widened 51 -> 101 bps; slide 25 basis undefined"}
forward_signals: ["FN07", "FN09", "FN11", "FN15", "FN16"]
ambiguous: ["FN02", "FN03", "FN04", "FN05", "FN08", "FN12", "FN17", "FN20", "FN21", "FN24", "FN25"]
commitments:
  - {commitment: "74 new branches commissioned; total 831 across 18 states and UTs", implied_date: "Q2 FY27", ref: "slide 5 line 123 (R033, R034)", status_word: "completed"}
  - {commitment: "Stree Sakthi Gold Loan Schemes portfolio crossed Rs 100 Cr", implied_date: "launched 2026-01-07; milestone by Q2 FY27", ref: "slide 40 line 1211 (R1095, R1096)", status_word: "completed"}
  - {commitment: "ESG KPI evaluation metrics being developed", implied_date: "undated", ref: "slide 40 lines 1194-1198 (R1091)", status_word: "underway"}
  - {commitment: "Nation Skill Building CSR programme for apprentices", implied_date: "undated; first in Q2 FY27 deck", ref: "slide 41 line 1231 (R1099)", status_word: "initiated"}
  - {commitment: "Future-ready digital ecosystem build", implied_date: "undated", ref: "slide 38 line 1135 (R1081)", status_word: "underway"}
gate_a3: pass
blank_checks: []
analyst_note: "Two A1 attribution errors were corrected by column offset and identity. Slide 25 Q1/Q2 FY27 yields are 16.4%/16.7%; with that, yield minus CoB equals spread in every period. Slide 22 annual MTL/STL values were assigned in ascending order; offsets and the FY26 tie (2,180 + 904 = 3,084) show STL disbursals fell from 1,475 (FY24) to 904 (FY26). The quarter's strength rests on two levers the deck does not foreground. First, coverage: at Q1 stage-wise coverage the ECL stock would be about Rs 19 Cr higher, which puts credit cost near 1.0% of average assets against the 1.1% tripwire and absorbs most of the QoQ PAT gain. Second, off-book: on-book AUF grew Rs 27 Cr while AUM grew Rs 899 Cr, and on-book gold shrank. PCR fell from 38.4% to 35.4%, which meets the literal 'PCR thins further' clause of the Pillar 2L override; the decision stays with the operator. The benign reading for both levers is a mix shift into low-LGD gold. The separating observation is product-wise Stage 2/3 coverage and gold auction losses, from the concall or the results filing."
```
