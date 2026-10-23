# A3 FORENSIC NOTES: PAISALO Q2 FY27 (doctype: presentation)

Agent: A3-forensics | model: claude-opus-5-5 | run date: 2026-10-23
Inputs read: A1 structured `extracted/paisalo-presentation-q2fy27-structured.md` (R001-R1059, all rows); A1 fulltext `extracted/paisalo-presentation-q2fy27-fulltext.md` (lines 1-1270, body and resolved appendix); A2 ledger `work/ledger_presentation_paisalo_q2fy27.md`; Notion copy `work/notion_thesis_paisalo.md` (sections 3 and 4 used as the checklist; other sections used only for Notion-sourced prior-quarter facts, each one marked); results-filing cross-check `extracted/paisalo-results-q2fy27-structured.md` (rows cited by ID and results-fulltext line).
Not read: source PDF, anything under `inputs/`. Prior-quarter deck: none on record, so every prior-quarter diff below is Notion-sourced and marked [NOTION].
Conventions: "L" = presentation fulltext line. "RF L" = results fulltext line. "my arithmetic" = A3 computation on printed numbers. Rs Mn unless stated.

---

## 1. LEDGER RECONCILIATION

| Category | Ledger rows | Rows read at cited line | Status |
|---|---|---|---|
| NUMBER (R001-R909) | 909 | 909 | read |
| ENTITY (R910-R971) | 62 | 62 | read |
| FORWARD (R972-R994) | 23 | 23 | read |
| DATE (R995-R1029) | 35 | 35 | read |
| QUALIFIER (R1030-R1059) | 30 | 30 | read |
| Total | 1059 | 1059 | 100% |

A2 flags, how A3 handled them:
- SERIES_UNRESOLVED p8 (R065/R066). Resolved by arithmetic. R065 2,436 = Q3FY26 interest income (consolidated FY26 interest 9,047.2 [results R497, RF L1004] less H1FY26 4,086 [L927] less Q4 2,526 = 2,435). R066 2,401 = Q3FY26 total income (p30 FY26 9,437 [L989] less H1FY26 4,427 [L928] less Q4 2,609). So Q3FY26 total income sits about Rs 35 Mn below interest income. Used in FN04.
- SERIES_UNRESOLVED p13 1-decimal series (R181-R193). Resolves to Credit Cost (%) by arithmetic: p30 provisions over average AUM give FY22 2.2%, FY23 1.7%, FY24 0.3%, FY25 0.5%, FY26 0.7% against chart 2.0/1.6/0.3/0.5/0.7. Used in FN25.
- SERIES_UNRESOLVED p14 lender base (R224-R255). Q2FY27 bank/FI share 73% ties to p29: borrowings other than debt securities 39,684 / (39,684 + 15,114) = 72.4%. Used in FN27.
- SERIES_UNRESOLVED p21 business mix (R424-R433). Category labels assigned by column position on L486-500 (A3 reading, not mechanical). The ten values sum to 100%.
- FOOTNOTE_UNRESOLVED p19 '#' (R1048). Stays unresolved. In FN17.
- p29 header "31st September, 2025" (R1055). In FN17.
- p9 axis lacks Q1FY27 (R1004, R1038). The axis is mislabelled, not short. In FN13.

A1 row-label notes (no finding; A4 must not inherit the label):
- R285-R293 "row-1 holding" is Institutions & Others, not Promoter: 529.8 / 909.5 = 58.3% FY26. Row-3 (R303-R311) is Promoter: 379.7 / 909.5 = 41.7%, and H1FY27 46.5% ties to p34 46.50% (L781).
- R758-R767 "Normal-stage share" is very likely cashless/cash collection share. See FN18.
- R785-R802 (p36) pair by layout as (overall, years with Paisalo) per person, legend L831. A1 assigned the first six values as "overall" to six people. A3 pairing: Anurag Sinha 41/20, Gaurav Chaubey 22/16, Samresh Agarwal 29/27, Manendra Singh 19/9, BVSKT Bhaskar 41/5, Rajeev Seth 29/5, Nishtha Sharma 8/3, Sushant Sharma 16/5, Deep Chand 38/2, Rajeev Singhal 42/2.5, Arun Kumar Srivastav 40/2, Snigdha Agarwal 8.5/2 (L818, L826).

Deck vs filing tie-out (deck basis test):

| Item Q2FY27 | Deck | Results filing, consolidated | Results filing, standalone | Deck ties to |
|---|---|---|---|---|
| Interest income | 2,653 (L927) | 26,532.55 lakh = 2,653.3 (R492, RF L1004) | 2,603.9 (R014, RF L799) | consolidated |
| Total income | 2,773 (L928) | 2,773.1 (R558, RF L1015) | 2,723.4 (R080) | consolidated |
| Interest expense | 1,297 (L929) | 1,296.7 (R564, RF L1017) | 1,280.3 (R086) | consolidated |
| Provisions | (2) (L933) | (2.4) (R588, RF L1021) | (3.8) (R110) | consolidated |
| PBT | 874 (L934) | 874.3 (R648, RF L1031) | 866.5 (R170) | consolidated |
| PAT | 656 (L936) | 656.4 (R666, RF L1035) | 650.5 (R212, RF L834) | consolidated |
| Loan assets | 71,144 (L964) | 71,144.0 (R839, RF L1099) | 70,079.1 (R325) | consolidated |
| Debt securities + other borrowings | 54,798 (L973-974) | 54,798.3 (R875, R876) | 54,190.5 (R361, R362) | consolidated |
| Equity & reserves | 19,360 (L977) | 914.2 + 18,445.4 = 19,359.6 (R781, R895) | 19,147.5 | consolidated |
| GNPA / NNPA | 0.66% / 0.46% (L121-123) | 0.65% / 0.45% (R1103/R1105) | 0.66% / 0.46% (R1102/R1104) | standalone |
| D/E | 2.89x (L135) | 2.83x (R1078, RF L1214) | 2.83x | neither (FN16) |
| NIM | 5.7% (L131) | 6.46% (R1101, RF L1235) | 6.43% | neither (FN12) |

Every P&L and balance-sheet line ties to the consolidated statements. Asset-quality ratios tie to the standalone statements. The deck labels neither basis.

---

## 2. FINDINGS TABLE

| id | check | ledger row ref | line/slide | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FN01 | F1 | R639, R640, R641 | L967, p29 | "Current & Deferred Tax Assets (Net) - - 85" | NEUTRAL-FACT | The net DTA of 85 (Sep-25) is gone. The filed consolidated BS shows a net DTL of 170.6 (results R889, RF L1132). Q2 carried a deferred-tax charge of 48.9 (results R660). No DTA shield remains to unwind, so no ETR step-up risk from this line. The template line will stay nil while the DTL builds. |
| FN02 | F6 | R972, R974, R999 | L147-148, p7 | "Consumer-facing app scheduled ... to go live in Q3FY27" | FORWARD-SIGNAL | A dated, testable commitment. The date holds against the 15-May thesis trigger "Customer App + AI Lead Engine, Q3 FY27 Phase 1" [NOTION]. The Q3 deck must show the app live, or the trigger slips. |
| FN03 | F6 | R045, R046, R977, R259, R1011, R1036 | L141-143, p7; L339-340, p14 | "Approved and launched Tranche I"; "Raised ~294.9 Cr public NCD in Aug 26." | NEUTRAL-FACT | Milestone confirmed. "Launched" changed to "raised" inside one deck: Rs 294.9 Cr of the Rs 300 Cr tranche (98%, my arithmetic). About Rs 605 Cr of the Rs 900 Cr shelf is left (my arithmetic). More tranches are the likely funding route for 33% AUM growth. |
| FN04 | F7 | R984, R991, R992, R1050-R1052, R582-R584, R065-R072 | L595, p25; L398, p17; L943, p28 | "Co-lending Provides Optionality for Growth Acceleration"; "Non-Interest Income 0.6% 1.2% 0.6%" | CONFIRMATORY-NEGATIVE | The co-lending catalyst is now framed as "optionality" in writing. The Q1 call used the same word [NOTION, section 9]. The deck gives no co-lending AUM, fee or partner figure. Its own numbers show co-lending is immaterial. (a) Non-interest income fell from 1.2% to 0.6% of assets YoY. (b) Total income less interest income was 163, -35, 83, 98, 120 over Q2FY26-Q2FY27 (my arithmetic; Q3FY26 negative). (c) AUM less loan assets, the most room off-book or co-lent AUM can have, shrank from 2,001 to 1,765 to 1,515 (2.1% of AUM; my arithmetic, upper bound). Thesis trigger (b) and checklist item 12 get no support from the deck. The filed fee share is 3.65% (101.2 of 2,773; results R510). |
| FN05 | F10 | R769, R772, R776, R777, R571-R578 | L781, L788, p34; L937, p27 | "Promoter and Promoter Group, 46.50%"; "Promoter and Promoter Group, 42.90%" | FORWARD-SIGNAL | Fully diluted promoter 42.90% against basic 46.50%. That implies about 990.9 Mn fully diluted shares against 914.1 Mn outstanding, so about 76.8 Mn potential shares (+8.4%; my arithmetic, assuming promoters hold no convertibles). The deck prints basic EPS only. The filing prints basic = diluted (standalone 0.71 / 0.71, results R279/R285, RF L848-849; Reg 52 consolidated H1 "Basic and Diluted" 1.39, R1087). Either the instruments are anti-dilutive or diluted EPS ignores them. Notion records 940.1 Mn shares on 1-Oct after FCCB conversions [NOTION]. On that base, about 50.8 Mn potential shares remain (my arithmetic). Checklist item 20 (share count up more than 5% suddenly) would fire if the remainder converts in one window. |
| FN06 | F10 | R047, R283, R284, R310, R311, R1001, R1002 | L153-155, p7; L1163, p15 | "Promoter shareholding rose by ~4.8% in H1FY27, driven by earlier Q1FY27 acquisitions" | AMBIGUOUS | Promoter shares went from 379.7 to 425.1 Mn, +45.4 Mn. That is 4.99% of the FY26 base of 909.5 Mn (my arithmetic), at the SAST 5% creeping-acquisition limit. Notion carries this reading as an open ruling [NOTION]. "Earlier Q1FY27" means no Q2 buying. FY27 headroom for more promoter buying is close to nil unless FCCB dilution restores it. The "Deepening Promoter Ownership" story cannot extend in FY27 on market purchases. |
| FN07 | F12 | R404-R413, R424-R433, R938, R1018 | L482, p21; L463-464, p20 | "AUM Breakup (Rs. Mn)" axis "FY22 ... FY26"; "Mid- Corporate" / "Emerging Corporate" | AMBIGUOUS | Lending-variant segment check. The Micro/MSME AUM split ends at FY26 on a Q2 deck, so the Q2FY27 split is not given. MSME/SME share of AUM was 19.1/26.0/33.7/28.5/29.0% over FY22-FY26 (my arithmetic). Yield fell 100 bps in the same quarter (FN21). The product list includes an "Enterprise" line: Mid-Corporate, Emerging Corporate. The business mix shows Heavy Industries 10% and Technology 7% (column reading, A2 SERIES_UNRESOLVED). Reading A: timing (management's reading). Reading B: mix shift to larger, lower-yield enterprise loans. Separating observation: the Q2FY27 Micro/MSME split and the Q3 yield. |
| FN08 | F12 | R633-R635, R645-R647 | L965, L969, p29 | "Other Non-Financial Assets 551 344 147"; "Investments 1,755 1,008 905" | AMBIGUOUS | Other non-financial assets are up 3.7x YoY and 60% QoQ. Investments rose by 747 QoQ. The deck discloses the nature of neither. For a vehicle and equipment lender, repossessed assets often sit in other non-financial assets. If they do, the Q2 write-back (FN23) understates credit cost. Benign reading: prepaid or advance items. Ask for the break-up of both lines. |
| FN09 | F14 | R491-R578, R624-R671 | L936, p27 (vs RF L1035, RF L834) | "PAT (Rs Mn) 656 515 27% 613 7%" | NEUTRAL-FACT | The deck never states its basis. Every P&L and BS line ties to the consolidated Reg 33 statements (656.4 consolidated vs 650.5 standalone). Asset-quality ratios tie to standalone (see tie-out table). This settles Notion Q1 question 3, which went unanswered on the Q1 call, on a filed basis [NOTION, section 9]. The S-vs-C PAT gap is small: 0.9% of standalone PAT in Q2FY27 (my arithmetic, results R212/R666). |
| FN10 | F14 | R515-R522, R591-R596 | L930, p27; L946-947, p28 | "Net Interest Income (Rs Mn) 1,476 1,262 17% 1,447 2%"; "Net Interest Income 7.1% ... Net Total Income 7.7%" | AMBIGUOUS | One label, two meanings. The p27 "NII" of 1,476 is total income less interest expense (2,773 - 1,297), which p28 calls "Net Total Income". Interest-only NII is 1,356, +23% YoY and +0.5% QoQ (my arithmetic), against the deck's 17% YoY. Cost-to-income moves with the denominator: 41.0% on the deck NII, 44.6% on interest-only NII (my arithmetic). Notion's 41.0% uses the deck basis. Q2 is above 35% on both. |
| FN11 | F14 | R606-R614, R523-R554 | L951-953, p28; L931-933, p27 | "PPOP 4.8% 5.8% 5.7%"; "Credit Cost 0.4% 1.0% 0.9%"; "Loan Losses & Provisions (2) 119 (102%) 157" | AMBIGUOUS | The p28 Q2FY27 column does not tie to the p27 P&L. The Q1FY27 and Q2FY26 columns do (Q1: opex 462 vs 468, credit cost 154 vs 157, PPOP 976 vs 979, on a total-income base; my arithmetic). For Q2FY27, p28 shows credit cost of 0.4% of assets where the P&L shows a write-back of 2. It shows PPOP of 4.8% where the P&L implies about 4.4%. On a base derived from total income, about Rs 60-80 Mn sits in credit cost on p28 but in opex/PPOP on p27 (my arithmetic). p28 implies cost-to-income of 36.4% (2.8/7.7) against 41.0% on p27. Reading A: drafting error. Reading B: part of Q2 other expenses is credit loss (write-offs or settlement losses booked outside impairment), and p28 puts it back in credit cost. Standalone other expenses rose from 217.3 to 336.9 QoQ while impairment fell from 156.3 to (3.8) (results R146/R147, R110/R111). Separating observation: the Q2 other-expenses break-up or the write-off note. |
| FN12 | F14 | R022, R023, R102, R727-R731, R1035 | L129-131, p6; L1053, p9 | "NIM% Yield ... 5.7% 15.7%" | AMBIGUOUS | The value under "NIM%" (5.7%) equals the p9 Q2FY27 spread (yield 15.7% less CoB 10.0%). The filed NIM is 6.46% consolidated and 6.43% standalone (results R1101/R1100). The p30 FY26 "NIM" of 6.8% equals the p9 Q4FY26 spread of 6.8%. The deck may use spread as NIM throughout (unverified). This feeds the open Notion ruling on monitorable 6 [NOTION]. On the checklist bands neither reading is green: 6.46% is below the 6.5% green floor, and 5.7% is below the 6.0% red line. |
| FN13 | F14 | R123-R132, R1004, R1038, R469-R474 | L216 / L1072, p9; L1226, p24 | "Q1FY26@708 Q2FY26@818 Q3FY26@928 Q4FY26@1038 Q2FY27@1150" | NEUTRAL-FACT | The borrowings and D/E axis is mislabelled by one quarter. The bars are Q2FY26 to Q1FY27 plus Q2FY27. 48,467 ties to the 30-Jun-26 BS (12,916 + 35,541 = 48,457) and 37,688 to 30-Sep-25 (37,608) (my arithmetic). So p9 "Q4FY26 D/E 2.61" contradicts p24 "FY26 2.43". Borrowings grew 13% in one quarter, not two. One more slip: the Q1 D/E of 2.61 recomputes on p29 equity (48,467 / 18,519 = 2.62), not on the deck's own Q1 net worth (18,298, giving 2.65x; my arithmetic). |
| FN14 | F14 | R194-R213, R742-R751 | L1000-1001, p30; L1117-1129, p13 | "GNPA (%) 1.52% 0.25% 0.21% 0.99% 0.76%"; "1.38%@1036" | AMBIGUOUS | The deck prints GNPA/NNPA history two ways. p30 gives FY22-FY25 GNPA of 1.52/0.25/0.21/0.99% and NNPA of 1.26/0.02/0.02/0.76%. p13 gives 1.38/0.22/0.20/0.98% and 1.15/0.02/0.02/0.76%. p13 is lower in every year it differs. FY22 x-positions (1036, 1090) bracket the FY22 axis (1063), so the pairing is not the cause. The "best-in-class" and "sub-2% through cycles" history rests on a series the deck itself does not hold fixed. Ask which series is the audited one and what basis p13 uses. |
| FN15 | F14 | R316, R317, R434-R438, R439-R453 | L391, p17; L506-509, L533, p22; L559-560, L563-566, p23 | "500k GenAI calls daily"; "NVIDIA GenAI calling handles 350k calls daily"; "300K ... AI Driven Outbound Calls Daily"; "300k AI-driven outbound calls executed in Q2FY27" | AMBIGUOUS | The AI metrics do not agree across three slides. GenAI calls: 500k vs 350k daily. Outbound calls: 300K "daily" on p22 vs 300k "executed in Q2FY27" on p23, a unit gap of about 90x. Applications: 180k on p17 (the Q1 figure) vs 190k on p22-23. Bots: 25 live on p22 vs 7 text + 15 voice = 22 on p23. The AI operating-leverage trigger [NOTION, section 6] rests on these numbers. Ask for one audited KPI set. |
| FN16 | F14 | R011, R118-R122, R475-R480, R666-R668, R026, R132 | L209, p9; L977, p29 (vs RF L1220) | "16,799 17,404 17,930 18,298 18,981"; "Equity & Reserves 19,360 18,519 16,660" | AMBIGUOUS | Three net-worth figures for Q2FY27: deck 18,981, BS equity 19,360, Reg 52 consolidated net worth 18,779.7 (results R1083). The deck net worth sits above BS equity in Q2FY26 (+139) and below it in Q1FY27 (-221) and Q2FY27 (-379) (my arithmetic). The deduction is undefined and its sign changes. Deck D/E is 2.89x on 18,981. Filed D/E is 2.83x on 19,360. All gaps are under 5% (F11 PASS), but the definition is unstable. Ask what the deck deducts. |
| FN17 | F14 | R1055, R033, R034, R161, R258, R805, R1048, R396-R401 vs R897-R902 | L960, p29; L147-149, p7; L335-338, p14; L845-847, p38; L446, p19 | "As on 31st September, 2025"; "420 touchpoints added during the year"; "Public NCD Issuance of 900 Cr under the shelf programme"; "87%+ Customers Served" | NEUTRAL-FACT | Drafting slips, each immaterial and together a governance data point. (a) The date does not exist. (b) 420 is the QoQ addition (5,995 to 6,415, L1008). FY27 to date is +1,116 and YoY is +2,035 (my arithmetic). (c) Rs 900 Cr is the shelf, and Rs 294.9 Cr was raised. (d) 87% is the women-customer share (L1010) with the qualifier dropped. (e) The p19 '#' markers have no footnote text. (f) p19 and p40 differ by 1 on Q3/Q4FY26 transaction values (9,841 vs 9,840; 11,342 vs 11,341). |
| FN18 | F14 | R758-R767 (vs R855-R860) | L1255-1256, p33; L1012, p40 | "88%@1046 89%@1223 90%@1401 91%@1580 91%@1758"; "Cashless Collection (QR & NACH) 88% 88% 89% 90% 91% 91%" | AMBIGUOUS | The p33 bar series (88/89/90/91/91 and 12/11/10/9/9) equals the p40 cashless-collection series for Q2FY26-Q2FY27 exactly. It is most likely the cashless vs cash collection share, not a loan-stage split as A1 labels it. If it were a stage split, 9% of the book in early delinquency against 0.66% GNPA would be a bear signal. A4 must not use R758-R767 as delinquency data without confirmation. |
| FN19 | F14 | R919, R927, R928, R1042, R1043 | L240-242, p11; L253-254, p12; L329, L353, p14 | "AA/STABLE/A1+"; "*Rating assigned by Infomerics Ratings \| #Rating assigned by Brickwork Ratings" | AMBIGUOUS | p11 and p12 headline "AA/Stable/A1+" and name no agency. p14 credits the AA ratings to Infomerics and Brickwork, and names no agency for the A1+. Thesis trigger (f), a downgrade below AA/Stable, needs a named agency and instrument. Ask which agency rates the bank lines, NCDs and CP. |
| FN20 | F16 | R031, R053-R057, R973 | L146-147, p7; L163, p8 | "Record disbursements weighted toward end of the quarter"; "11,025 10,574 13,440 17,309 15,673" | CONFIRMATORY-NEGATIVE | Q2 disbursement of 15,673 is 9.5% below Q1's 17,309 on the deck's own chart (my arithmetic). "Record" is false on the deck's own chart. The yield explanation (FN21) rests on this premise. Communication-quality data point (the Promoter Verdict notes a B+ communication grade [NOTION]). |
| FN21 | F16 | R088-R112, R973, R1000 | L147-149, p7; L1045-1053, p9 | "temporarily diluted yields, to normalise from H2FY27" | FORWARD-SIGNAL | Yield fell from 16.7% to 15.7% (-100 bps), spread from 6.6% to 5.7%, and RoA from 3.6% to 3.3%. Management guides normalisation from H2FY27. The test is dated: the Q3FY27 yield should move back toward about 16.7%. If it stays near 15.7%, the cause is mix or pricing (FN07 reading B), not timing. |
| FN22 | F16 | R036, R976, R989, R523-R530, R885-R890 | L141-145, p7; L548-551, p23; L931, p27 | "Headcount reduced 11% YoY ... early operating leverage"; "Operating Expenses (Rs Mn) 605 453 33% 468 29%" | CONFIRMATORY-NEGATIVE | The deck claims operating leverage. Its own P&L shows opex +33% YoY and +29% QoQ against deck NII +17% and +2%. Cost-to-income is 41.0% in Q2 vs 32.3% in Q1 and 35.9% in Q2FY26 (my arithmetic). Headcount fell from 3,255 to 2,905 (-10.8%, L1018) while opex rose, so cost per employee rose. "Sustainable cost-to-income improvement" (R989) has no Q2 evidence. Q2 is above 35% on every deck basis (36.4% p28-implied, 41.0%, 44.6%), so it counts toward thesis trigger (d) whatever the Notion basis ruling is [NOTION]. |
| FN23 | F16 | R531-R570, R039 | L932-933, p27; L142-144, p7 | "PPOP (Rs Mn) 872 809 8% 979 (11%)"; "Loan Losses & Provisions (2) ... 157" | FORWARD-SIGNAL | PAT rose 7% QoQ only because provisions swung from 157 to (2). PPOP fell 11% QoQ. The p7 headline cites PAT +27% YoY and omits PPOP. If credit cost returns to the FY26 level of about 0.7% of AUM (p13), Q3 provisions run at about Rs 120 Mn a quarter. PAT would then fall QoQ unless PPOP recovers (my arithmetic, illustrative). |
| FN24 | F16 | R133-R147, R481-R484, R975, R990, R128-R132 | L148-151, p7; L1059-1071, p9; L586-589, p24 | "Recent capital raise expected to optimize leverage levels"; "Comfortably above the 15% regulatory minimum" | FORWARD-SIGNAL | Total CRAR fell from 38.2% to 30.7% (-7.5 pp in four quarters, -2.4 pp QoQ). Tier 1 fell from 30.3% to 25.2%. D/E rose from 2.24x to 2.89x. RoE held at 13.4% while RoA fell, so leverage now carries ROE. "Optimize leverage ... supporting ROE expansion" guides more of the same. At the Q2 pace, total CRAR reaches the checklist red line of 20% in about 4-5 quarters (my arithmetic, linear, before the post-Sep FCCB equity). An equity need, through FCCB conversion, warrants or an issue, sits inside the 12-month window. |
| FN25 | F16 | R181-R213 | L295, p13; L1104-1107, L1125-1127 | "GNPA (%) NNPA (%) Credit Cost (%)"; "3.1%@649"; "3.8%@781" | AMBIGUOUS | With the series resolved (Section 1), FY19-FY21 credit cost was 3.1/3.8/2.4% while GNPA was 0.26/0.39/0.66%. Credit cost ran 5-12x GNPA. Through the last stress period the company held GNPA low by writing loans off. GNPA understates stress, and thesis trigger (a) (GNPA above 1.5%) may never fire in a downturn. Credit cost and write-offs are the gauge (checklist 8). Ask for write-offs by year. |
| FN26 | F16 | R012, R058-R062, R150, R350-R354, R879-R884, R013 | L1023, p8; L1017, p40; L121, p6 | "Customer Franchise (Mn)" 13/14/16/18/20; "Lives Impacted 11 Mn 13 Mn 14 Mn 16 Mn 18 Mn 20 Mn" | AMBIGUOUS | "Customer franchise" (p8, p11, p18) and "Lives impacted" (p40) are the same series. AUM of 72,659 at an average ticket of Rs 6.16 lakh implies about 118k loans (my arithmetic, rough; ATS basis not stated). The 20 Mn figure is about 170x the borrower base and is mostly a BC-channel reach number. "Ability to capture future growth" (L151-153) needs a cross-sell-to-credit conversion number, which the deck does not give. |
| FN27 | F16 | R224-R255, R929, R985 | L323, p14; L1155-1157 | "Strategic Liability Diversification"; "69%@1376" ... "73%@1739" | NEUTRAL-FACT | The bank/FI share of borrowings rose from 69% (FY25) to 72% (FY26) to 73% (Q2FY27). The BS cross-check gives 72.4%. That runs opposite to the slide title and to "Funding base diversified" (R985). The NCD tranche (FN03) has not yet moved the mix. Watch whether the Q3 bank share falls below 70%. |
| FN28 | F16 | R018 | L123-125, p6 | "Liquidity Coverage ... 2.22X" | AMBIGUOUS | [NOTION] The thesis logged liquidity coverage of 8.3x (Notion, 1.3 3A). The deck prints 2.22X with no definition. Either the definition changed or liquidity fell about 73% while cash plus investments rose from 1,602 to 2,786 QoQ (p29; my arithmetic). Ask for the definition and the Q1 value. |
| FN29 | F16 | R324-R329, R933 | L407-412, p18 | "Delhi, 26.2% ... Others, 12.3%" | AMBIGUOUS | [NOTION] Top-5 states are 87.7% (my arithmetic) against 91.9% at FY26 (Notion). A 4.2 pp fall in two quarters is fast for a 72,659 book. Ask whether the five-state list and basis (AUM vs disbursement) are unchanged since the FY26 deck. Do not credit checklist 14 until that is confirmed. |
| FN30 | F16 | R810-R824, R873-R878, R867-R872 | L860, p39; L1014-1016, p40 | "+3.4% QoQ"; "Number of Electric Vehicles (EV) financed 678 934 2,141 1,478 1,736 1,257" | AMBIGUOUS | p39 frames the quarter as QoQ gains off a Q1 trough. p40 shows EVs financed down 28% QoQ (1,736 to 1,257) and 41% below the Q3FY26 peak. Small and medium businesses supported (2,287) are below Q3FY26 (2,433) and Q4FY26 (2,976). The new-product trigger (LAP, tractor, solar, medical, EV) [NOTION, section 6] gets weaker evidence than the framing suggests. |

---

## 3. CHECKLIST SCORECARD

| Check | Status | Basis |
|---|---|---|
| F1 | FINDING | 5 ZERO_STANDING rows read. R639/R640: tax-asset line nil after net DTA 85 flipped to filed net DTL (FN01). R301/R302: GDR row kept at 0.0% after Q2FY26 conversion (L374), benign. R251: lender-base 0% label at FY23 x-position, chart artefact, benign. |
| F2 | N.A. | Presentation carries one basis only. S-vs-C decomposition belongs to the results-filing A3. Deck basis identified as consolidated (FN09). |
| F3 | N.A. | No standalone vs consolidated cost lines in the deck. |
| F4 | N.A. | No auditor letter or Other Matters paragraph in a deck. Results-filing A3 scope. |
| F5 | N.A. | No EoM or going-concern paragraph in a deck. Results-filing A3 scope. |
| F6 | FINDING | Lexicon scan over L1-921: "expected to" (L148), "scheduled to go live" (L147), "to normalise from" (L149), "Approved and launched" (L141), "Initiated" (L900), "Established" (L911). Register in Section 4. Findings FN02, FN03. |
| F7 | FINDING | F7 lexicon: 0 hits ("subject to", "no assurance", "evaluating", "exploring", "in discussions", "endeavour", "may sometimes", "could have an effect" all absent from L1-921). Off-lexicon hedges: "optionality" (L398, L595), "temporarily" (L148), "early evidence" (L548), "early operating leverage" (L143). FN04. |
| F8 | PASS | Deck tax line only. ETR 24.9% Q2FY27 (218/874), 25.4% Q1 (209/822), 25.4% Q2FY26 (175/690), 25.1% H1 (my arithmetic) against 25.17% statutory. No prior-year tax line in the deck. Filed deferred-tax sign is a charge, not a credit (results R660), so no shield. |
| F9 | N.A. | No OCI in the deck. |
| F10 | FINDING | Paid-up shares 909.5 Mn (FY26) to 914.1 Mn (H1FY27), +0.5%, consistent with filed paid-up 9,095.84 to 9,142.11 lakh (results R781-R786). Fully diluted gap (FN05). Promoter creeping-acquisition headroom (FN06). |
| F11 | PASS | Deck p29 Equity & Reserves 19,360 equals filed consolidated paid-up + other equity (19,359.6). Deck net worth 18,981 differs by -2.0%, Reg 52 net worth 18,779.7 by -3.1%. All under 5%. Candidate reconciling items: Reg 52 deductions (revaluation reserve, deferred expenses), intangibles, unamortised issue costs. Definition instability is FN16. |
| F12 | FINDING | Lending variant: book-mix and asset-line trend. Q2FY27 Micro/MSME split withheld (FN07). Other non-financial assets and investments build with nature undisclosed (FN08). No segment liabilities in the deck. |
| F13 | N.A. | The deck has a board roster (p35) but no outcomes, term dates or resolutions. Observation only: by the A3 pairing of p36, control functions are recent hires: EVP Credit 2.5 years, EVP Audit 2 years, EVP HR 2 years, Head HR 2 years, CRO 5 years with Paisalo (L818, L826). |
| F14 | FINDING | FN09-FN19: basis unlabelled, NII double meaning, p28 vs p27 mismatch, NIM label, p9 axis, GNPA history, AI metrics, net-worth definition, drafting slips, p33 series identity, rating attribution. |
| F15 | N.A. | No consolidation list in the deck. The safe harbour names "subsidiaries or associate companies" (L89-90) and no entity is named anywhere. Results-filing A3 scope. |
| F16 | FINDING | No prior deck on record, so the dropped-slide diff is not testable (A2). F16 is run on the deck's internal framing against its own data, plus [NOTION] prior facts: FN20-FN30. |
| F17 | N.A. | Concall-only check. The checklist coverage table below is supplied for A4. |

Notion checklist coverage by this deck (data for A4, not an F17 score):

| Notion # | Item | Deck value | Deck cite | Read |
|---|---|---|---|---|
| 1 | AUM growth | +33% YoY | L142 | Green |
| 2/3 | GNPA / NNPA | 0.66% / 0.46% | L121-123 | Green; see FN14, FN25 |
| 4 | Collection efficiency | 98.3% (Q1 97.5%) | L1041 | Green |
| 5 | Cost of borrowing | 10.0% | L1048 | Green |
| 6 | NIM | 5.7% printed as NIM (spread) | L131 | Basis open (FN12) |
| 7 | Cost-to-income | 41.0% deck basis (my arithmetic) | L930-931 | Red on every basis (FN22) |
| 8 | Credit cost | Q2 write-back; p28 0.4% | L933, L952 | Basis open (FN11) |
| 9 | CAR | 30.7%, Tier 1 25.2% | L1063, L1071 | Green, falling fast (FN24) |
| 10 | ROA | 3.3% | L1050 | Amber |
| 11 | ROE | 13.4% flat | L1042 | Green, not rising |
| 12 | Co-lending fee share | NOT DISCLOSED in deck | p25 | Silent (FN04) |
| 13 | SBI MSME co-lending AUM | NOT DISCLOSED in deck | p25 | Silent (FN04) |
| 14 | Top-5 states | 87.7% (my arithmetic) | L407-412 | Basis check (FN29) |
| 15 | Pledge | NOT DISCLOSED in deck | p34 | Silent |
| 16 | Promoter holding | 46.50%, +4.8 pp H1 | L781, L153 | Green; FN06 |
| 17 | RPT borrowing | NOT DISCLOSED in deck | - | Silent |
| 18 | Rating | AA/Stable/A1+ (agency unnamed) | L240 | Unchanged; FN19 |
| 19 | AUM / net worth | 3.83x (my arithmetic) | L113, L117 | Green |
| 20 | Share count | 914 Mn; fully diluted +8.4% (my arithmetic) | L775, L788 | Watch (FN05) |

---

## 4. COMMITMENT REGISTER (F6)

| # | Commitment | Implied date | Ref (slide / line / row) | Status word |
|---|---|---|---|---|
| C1 | Consumer-facing app goes live | Q3FY27 | p7 L147-148; R974, R972, R999 | scheduled (date held vs 15-May thesis [NOTION]) |
| C2 | Yields normalise as the full interest impact comes through | from H2FY27 | p7 L146-149; R973, R1000 | guided, not started |
| C3 | Recent capital raise to optimise leverage and support ROE expansion | undated (H2FY27 implied) | p7 L148-151; R975 | raise completed; effect expected |
| C4 | Public NCD Tranche I up to Rs 300 Cr under the Rs 900 Cr shelf | Aug-26 | p7 L141-145; p14 L339-340; R977, R259, R1011 | completed (about Rs 294.9 Cr raised) |
| C5 | Asset quality held at sub-2% through credit cycles | ongoing | p13 L293; R980 | standing target |
| C6 | Continued reduction in cost of borrowing | ongoing | p17 L388-390; R981 | underway (10.1% to 10.0%) |
| C7 | Sustainable cost-to-income improvement from decoupling scale from headcount | undated | p23 L548-551; R989 | claimed "early evidence"; Q2 contradicts (FN22) |
| C8 | New categories: agri, industrial, alternative-fuel equipment | undated (Q1 call: Q3FY27-end [NOTION]) | p17 L396-397; R983 | underway (p20 product list) |
| C9 | Expansion in existing states and into new contiguous markets | undated | p11 L232-236; p18 L403; R978 | underway (23rd state added Q1FY27, L1007) |
| C10 | Co-lending 80:20 as optionality for future RoA and RoE | undated | p17 L397-399; p25 L595-614; R984, R991, R992 | no status word; reframed as optionality (FN04) |
| C11 | AI early-warning and AI-optimised collections | undated | p22 L513-520; R988 | in place (claimed) |
| C12 | Water stewardship measures | undated | p41 L900-903; R994 | initiated |
| C13 | ESG Steering Committee with board-level oversight | done | p41 L911-914; R970 | completed |
| C14 | Outstanding GDRs converted | Q2FY26 | p15 L374; R1045, R1014 | completed |

Status transition vs the Q1 call [NOTION, section 9]: NCD shelf "opens 7-Aug" changed to Tranche I "raised ~294.9 Cr" (completed). "Second raise Q2" is not evidenced in this deck. SBI co-lending "stalled, de-scoped to optionality" is unchanged.

---

## 5. ANALYST NOTE (copied in the YAML)

Three items matter most. (1) FN11: the p28 Q2FY27 column moves about Rs 60-80 Mn from opex/PPOP into credit cost compared with the p27 P&L, and the Q1 and Q2FY26 columns tie. Reading A: drafting error. Reading B: part of Q2 other expenses is credit loss booked outside impairment, so the Rs (2) Mn write-back understates credit cost. The separating observation is the Q2 other-expenses break-up or the write-off note. (2) The Q2 cost-to-income breach of 35% holds on every deck basis (36.4% to 44.6%). PAT +7% QoQ rests only on the provision swing, and PPOP fell 11%. (3) On the deck's own numbers co-lending is immaterial: AUM exceeds loan assets by at most 2.1%, non-interest income halved, and the slide now says "optionality". Capital is the forward constraint. CRAR fell 7.5 pp in four quarters, and management guides ROE expansion through leverage while RoA falls. FN25: past stress went through write-offs, not GNPA.

---

```yaml
stage: A3-forensics
company: "PAISALO"
quarter: "Q2 FY27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "C:\\Users\\SUMIT SHARMA\\repos\\inflection-pipeline\\.claude\\worktrees\\quarterly-paisalo-q2fy27-095262\\runs\\paisalo-q2fy27\\work\\forensics_paisalo_q2fy27_presentation.md"
ledger_reconciled_pct: 100
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
  F11: PASS
  F12: FINDING
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "FN01", check: "F1", line: "L967 p29 (R639-R641)", classification: "NEUTRAL-FACT", implication: "Net DTA 85 gone; filed net DTL 170.6 builds; Q2 deferred charge 48.9; no DTA shield, no ETR step-up risk"}
  - {id: "FN02", check: "F6", line: "L147-148 p7 (R974)", classification: "FORWARD-SIGNAL", implication: "Consumer app go-live Q3FY27, date held vs 15-May trigger [NOTION]; Q3 deck must show it live"}
  - {id: "FN03", check: "F6", line: "L141-143 p7; L339-340 p14 (R977, R259)", classification: "NEUTRAL-FACT", implication: "NCD Tranche I completed at Rs 294.9 Cr of 300 Cr; about Rs 605 Cr shelf left for further tranches"}
  - {id: "FN04", check: "F7", line: "L595 p25; L398 p17; L943 p28", classification: "CONFIRMATORY-NEGATIVE", implication: "Co-lending reframed as optionality; non-interest income 1.2% to 0.6% of assets YoY; AUM less loan assets at most 2.1% of AUM and shrinking; trigger (b) unsupported"}
  - {id: "FN05", check: "F10", line: "L781, L788 p34; L937 p27", classification: "FORWARD-SIGNAL", implication: "Fully diluted 42.90% vs basic 46.50% implies about 76.8 Mn potential shares (+8.4%); filing shows basic = diluted EPS; checklist 20 risk"}
  - {id: "FN06", check: "F10", line: "L153-155 p7; L1163 p15", classification: "AMBIGUOUS", implication: "Promoter +45.4 Mn shares = 4.99% of FY26 base, at SAST 5% creeping limit; FY27 buying headroom near nil"}
  - {id: "FN07", check: "F12", line: "L482 p21; L463-464 p20", classification: "AMBIGUOUS", implication: "Q2FY27 Micro/MSME split withheld while yield fell 100 bps; Mid-Corporate product line; timing vs mix shift"}
  - {id: "FN08", check: "F12", line: "L965, L969 p29", classification: "AMBIGUOUS", implication: "Other non-financial assets 147 to 551 and investments +747 QoQ, nature undisclosed; repossessed assets would understate credit cost"}
  - {id: "FN09", check: "F14", line: "L936 p27 (RF L1035, RF L834)", classification: "NEUTRAL-FACT", implication: "Deck P&L/BS tie to consolidated Reg 33, asset-quality ratios to standalone; basis never labelled; S-vs-C PAT gap 0.9%"}
  - {id: "FN10", check: "F14", line: "L930 p27; L946-947 p28", classification: "AMBIGUOUS", implication: "p27 NII = net total income 1,476; interest-only NII 1,356 (+23% YoY); C/I 41.0% vs 44.6% by denominator"}
  - {id: "FN11", check: "F14", line: "L951-953 p28; L931-933 p27", classification: "AMBIGUOUS", implication: "p28 Q2 column moves about Rs 60-80 Mn from opex/PPOP to credit cost vs P&L; implied C/I 36.4%; write-off may sit in other expenses"}
  - {id: "FN12", check: "F14", line: "L129-131 p6; L1053 p9", classification: "AMBIGUOUS", implication: "Deck NIM 5.7% equals spread; filed NIM 6.46%; neither green on checklist 6 bands"}
  - {id: "FN13", check: "F14", line: "L216/L1072 p9; L1226 p24", classification: "NEUTRAL-FACT", implication: "Borrowings/D-E axis mislabelled one quarter; p9 Q4FY26 2.61 contradicts p24 FY26 2.43; borrowings +13% in one quarter"}
  - {id: "FN14", check: "F14", line: "L1000-1001 p30; L1117-1129 p13", classification: "AMBIGUOUS", implication: "GNPA/NNPA history FY22-FY25 printed two ways (FY22 1.52% vs 1.38%); best-in-class history not fixed"}
  - {id: "FN15", check: "F14", line: "L391 p17; L506-509, L533 p22; L559-566 p23", classification: "AMBIGUOUS", implication: "AI KPIs conflict (500k vs 350k daily; 300K daily vs per quarter; 25 vs 22 bots); AI operating-leverage trigger rests on them"}
  - {id: "FN16", check: "F14", line: "L209 p9; L977 p29 (RF L1220)", classification: "AMBIGUOUS", implication: "Three net-worth figures; deck NW vs BS equity changes sign; deck D/E 2.89 vs filed 2.83"}
  - {id: "FN17", check: "F14", line: "L960 p29; L147-149 p7; L335-338 p14; L845-847 p38; L446 p19", classification: "NEUTRAL-FACT", implication: "Drafting slips (non-existent date, 420 QoQ called yearly, 900 Cr shelf called issuance, 87% women share unlabelled, unresolved '#'); governance data point"}
  - {id: "FN18", check: "F14", line: "L1255-1256 p33; L1012 p40", classification: "AMBIGUOUS", implication: "p33 series equals cashless-collection series; R758-R767 not to be used as delinquency data until confirmed"}
  - {id: "FN19", check: "F14", line: "L240-242 p11; L353 p14", classification: "AMBIGUOUS", implication: "AA/Stable/A1+ headline names no agency; AA from Infomerics/Brickwork; trigger (f) needs named agency and instrument"}
  - {id: "FN20", check: "F16", line: "L146-147 p7; L163 p8", classification: "CONFIRMATORY-NEGATIVE", implication: "'Record disbursements' false on own chart: Q2 15,673 is 9.5% below Q1 17,309"}
  - {id: "FN21", check: "F16", line: "L147-149 p7; L1045-1053 p9", classification: "FORWARD-SIGNAL", implication: "Yield -100 bps, spread 6.6% to 5.7%, RoA 3.3%; normalisation guided from H2FY27; Q3 yield is the test"}
  - {id: "FN22", check: "F16", line: "L141-145 p7; L548-551 p23; L931 p27", classification: "CONFIRMATORY-NEGATIVE", implication: "Operating-leverage claim vs opex +33% YoY / +29% QoQ; C/I 41.0% vs 32.3% Q1; above 35% on every deck basis, trigger (d)"}
  - {id: "FN23", check: "F16", line: "L932-933 p27; L142-144 p7", classification: "FORWARD-SIGNAL", implication: "PAT +7% QoQ only from provision swing 157 to (2); PPOP -11% QoQ; Q3 PAT at risk if credit cost normalises"}
  - {id: "FN24", check: "F16", line: "L148-151 p7; L1059-1071 p9; L586-589 p24", classification: "FORWARD-SIGNAL", implication: "CRAR -7.5 pp in 4 quarters; ROE guided via leverage while RoA falls; equity need inside 12 months at Q2 pace"}
  - {id: "FN25", check: "F16", line: "L295 p13; L1104-1107, L1125-1127", classification: "AMBIGUOUS", implication: "FY19-FY21 credit cost 3.1-3.8% vs GNPA under 0.7%; stress absorbed by write-offs; trigger (a) may not fire in a downturn"}
  - {id: "FN26", check: "F16", line: "L1023 p8; L1017 p40; L121 p6", classification: "AMBIGUOUS", implication: "Customer franchise 20 Mn = Lives impacted; about 118k loans implied; conversion to credit undisclosed"}
  - {id: "FN27", check: "F16", line: "L323 p14; L1155-1157", classification: "NEUTRAL-FACT", implication: "Bank/FI share 69% to 72% to 73% under a diversification title; NCDs not yet moving the mix"}
  - {id: "FN28", check: "F16", line: "L123-125 p6", classification: "AMBIGUOUS", implication: "[NOTION] liquidity coverage 2.22X vs thesis-logged 8.3x; definition change or 73% fall"}
  - {id: "FN29", check: "F16", line: "L407-412 p18", classification: "AMBIGUOUS", implication: "[NOTION] top-5 states 87.7% vs 91.9% FY26; confirm unchanged state list and basis before crediting checklist 14"}
  - {id: "FN30", check: "F16", line: "L860 p39; L1014-1016 p40", classification: "AMBIGUOUS", implication: "QoQ framing off Q1 trough; EVs financed -28% QoQ, SMBs below Q3/Q4FY26; new-product trigger weaker"}
forward_signals: ["FN02", "FN05", "FN21", "FN23", "FN24"]
ambiguous: ["FN06", "FN07", "FN08", "FN10", "FN11", "FN12", "FN14", "FN15", "FN16", "FN18", "FN19", "FN25", "FN26", "FN28", "FN29", "FN30"]
commitments:
  - {commitment: "Consumer-facing app goes live", implied_date: "Q3FY27", ref: "p7 L147-148; R974", status_word: "scheduled"}
  - {commitment: "Yields normalise as full interest impact comes through", implied_date: "from H2FY27", ref: "p7 L146-149; R973", status_word: "guided"}
  - {commitment: "Recent capital raise to optimise leverage and support ROE expansion", implied_date: "undated (H2FY27 implied)", ref: "p7 L148-151; R975", status_word: "completed (raise); effect expected"}
  - {commitment: "Public NCD Tranche I up to Rs 300 Cr under Rs 900 Cr shelf", implied_date: "Aug-26", ref: "p7 L141-145; p14 L339-340; R977, R259", status_word: "completed"}
  - {commitment: "Asset quality sub-2% through credit cycles", implied_date: "ongoing", ref: "p13 L293; R980", status_word: "standing target"}
  - {commitment: "Continued reduction in cost of borrowing", implied_date: "ongoing", ref: "p17 L388-390; R981", status_word: "underway"}
  - {commitment: "Sustainable cost-to-income improvement from decoupling scale from headcount", implied_date: "undated", ref: "p23 L548-551; R989", status_word: "claimed (contradicted Q2)"}
  - {commitment: "New categories agri, industrial, alternative-fuel equipment", implied_date: "undated (Q3FY27-end per Q1 call [NOTION])", ref: "p17 L396-397; R983", status_word: "underway"}
  - {commitment: "Expand in existing states and new contiguous markets", implied_date: "undated", ref: "p11 L232-236; p18 L403; R978", status_word: "underway"}
  - {commitment: "Co-lending 80:20 as optionality for future RoA/RoE", implied_date: "undated", ref: "p17 L397-399; p25 L595-614; R984, R991", status_word: "none (reframed as optionality)"}
  - {commitment: "AI early-warning and AI-optimised collections", implied_date: "undated", ref: "p22 L513-520; R988", status_word: "in place (claimed)"}
  - {commitment: "Water stewardship measures", implied_date: "undated", ref: "p41 L900-903; R994", status_word: "initiated"}
  - {commitment: "ESG Steering Committee with board-level oversight", implied_date: "done", ref: "p41 L911-914; R970", status_word: "completed"}
  - {commitment: "Outstanding GDRs converted", implied_date: "Q2FY26", ref: "p15 L374; R1045", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "Three items matter most. (1) FN11: the p28 Q2FY27 column moves about Rs 60-80 Mn from opex/PPOP into credit cost compared with the p27 P&L, and the Q1 and Q2FY26 columns tie. Reading A: drafting error. Reading B: part of Q2 other expenses is credit loss booked outside impairment, so the Rs (2) Mn write-back understates credit cost. The separating observation is the Q2 other-expenses break-up or the write-off note. (2) The Q2 cost-to-income breach of 35% holds on every deck basis (36.4% to 44.6%). PAT +7% QoQ rests only on the provision swing, and PPOP fell 11%. (3) On the deck's own numbers co-lending is immaterial: AUM exceeds loan assets by at most 2.1%, non-interest income halved, and the slide now says optionality. Capital is the forward constraint. CRAR fell 7.5 pp in four quarters, and management guides ROE expansion through leverage while RoA falls. FN25: past stress went through write-offs, not GNPA."
```
