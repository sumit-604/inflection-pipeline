# A3 FORENSIC NOTES: SKYGOLD q2fy27 (doctype: presentation)

Company: Sky Gold & Diamonds Ltd (SKYGOLD) | Quarter: Q2 FY27 | Model: claude-opus-5-5
Inputs read: A1 structured (R001-R915), A1 fulltext (851 lines), A2 ledger (915 IDs, 41 ZERO_STANDING, 4 MISSING_FROM_STRUCTURED units M001-M004).
Not read: source PDF, inputs/. Prior-quarter fulltext: none (first Sky Gold run). Notion page: none (PRE-THESIS READ; operator watch list used as checklist).
Ledger reconciliation: 915 of 915 structured rows read at their cited lines, plus M001-M004 = 100%.
Finding ID prefix: D- (deck).

## Reading caveats (carry to A4)
- Pages 9-12 and 36-40: -layout scrambled the tables. Values and period columns below come from A1's render-checked structured rows. Fulltext lines anchor to the label line, +/-2. Where a fulltext quote shows a scrambled label, the finding says so.
- Pages 17 and 27: column assignment was NOT render-checked (R499, R627). Findings D-A3-20, D-A3-23 and D-A3-27 rest on the p17 column reading. D-A3-18 uses a p27 milestone. Each flags this.
- No call transcript exists (call 31-Oct-2026). Every FORWARD-SIGNAL and AMBIGUOUS finding goes to A4.
- Derived numbers below are arithmetic on deck rows only. Each one shows its formula. Nothing is estimated.

## 1. FINDINGS TABLE

| id | check | ledger row ref | line / slide | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| D-A3-01 | F1 | R283, R284, R285, R286, R287 | fulltext 225-226 (p10; label scrambled, values per render) | "Exceptional income/(expense)" ... "-7.4      0.0               0.0             -7.4" | FORWARD-SIGNAL | A standing zero line came alive. Q2 FY27 carries a Rs 7.4 Cr exceptional charge. Q2 FY26, Q1 FY27 and H1 FY26 were 0.0. The deck never says what it is. It is the first quarter reviewed by the new statutory auditor (D-A3-28). Ask about its nature, whether it recurs, and whether it links to the land sale (R358), the Rs 44.0 Cr investment that went to zero (R328), or the investment property that went to zero (R322). |
| D-A3-02 | F1 | R322/R323, R328/R329 | fulltext 239-240, 243-244 (p11; scrambled) | "Financial Assets                                    0.0        44.0" | AMBIGUOUS | Two asset lines dropped to 0.0 in H1. Non-current investments fell from 44.0 to 0.0 and investment property from 2.4 to 0.0. That is Rs 46.4 Cr with no slide comment. The deck does not say whether these were sold, reclassified or written off. The exceptional charge (D-A3-01) is a candidate destination. Ask what the investments were, the sale price, and the gain or loss booked. |
| D-A3-03 | F1 / F15 | R429, R324/R325, R439, R440, R443 | fulltext 290 (p13); 241 (p11); 281 (p12) | "Acquired 100% stake in Purvi Gems for ₹9 crore" | AMBIGUOUS | p13 lists the Purvi Gems buy as a Q2 FY27 update. Goodwill is unchanged at 250.5 on 30-Sep-26 and 31-Mar-26. "Cash and cash equivalent on acquisition of subsidiaries" is 0.0 for H1 FY27. Either the deal closed after 30-Sep-26, or the price equalled net assets. Ask for the completion date, the consolidation date and the purchase-price allocation. |
| D-A3-04 | F2 | R537-R543, R544-R550, R523-R536, R552, R692 | fulltext 472-474, 477-480 (p20) | "Turnover :- ₹42 crore as on 31st March ... PAT :- ₹16.6 crore" | AMBIGUOUS | Speed Bangle earns a 39.5% PAT margin (16.6/42) on revenue "mainly on job work basis" (line 472). The group margin is 4.5%. Its turnover rose 48x from Rs 0.87 Cr within about a year. FY26 PAT of the four acquired entities sums to 80.6 Cr, which is 28.6% of consolidated PAT of 281.8 (before eliminations and NCI). Shri Rishab was acquired in Dec'25, yet its FY26 PAT of 18.8 is a full-year entity figure, not a post-acquisition contribution. Ask how much subsidiary job-work revenue is intra-group, and how much of the 80.6 Cr is post-acquisition and attributable to Sky Gold. |
| D-A3-05 | F6 | R582, R585, R587, R358/R359, R759 | fulltext 500-504 (p21) | "Completion extended beyond Aug 2026. Shifted from a proposed promoter purchase to an external sale" | FORWARD-SIGNAL | The land sale missed its Aug-2026 date and has no new date. Assets held for sale stay at 110.1 on both balance-sheet dates. The buyer changed from the promoter (a related party) to an unnamed outside party. Ask for the new date, the expected price against the 110.1 carrying value, and the buyer. A sale below book is an exceptional-loss risk. |
| D-A3-06 | F6 | R583, R584 (ZERO_STANDING), R586 | fulltext 504-505 (p21) | "100% conversion by Dec FY25 not achieved ... GML was nil as of Mar 2026." | AMBIGUOUS | The GML (gold metal loan) commitment was dropped, not delivered. The GML balance is given for Mar-26 only, not Sep-26. In the same half, trade payables rose 4.7x (D-A3-24). Gold sourcing may have moved from GML to supplier credit. Ask for the Sep-26 GML balance, how gold is now funded, and the cost of each route (operator watch item 5). |
| D-A3-07 | F13 | R518, R520 | fulltext 433, 453 (p19) | "Sky Gold had previously indicated that expansion would be supported through internal cash generation." / "Similar capital-raising initiatives undertaken in the past have coincided with periods of business expansion" | FORWARD-SIGNAL | p19 prepares readers for a capital raise without naming one. The deck is dated 28-Oct-2026. Per the operator's watch list, the board approved a QIP of up to Rs 1,800 Cr on 27-Oct-2026, with an EGM on 18-Nov-2026. The earlier internal-funding commitment is being walked back. Ask for the use of proceeds, why internal cash no longer suffices, and the pricing floor. |
| D-A3-08 | F6 | R458, R459, R456, R234/R235 | fulltext 327-329 (p15) | "promoters will not draw salaries from FY27, all promoter payouts will be solely through dividends generated from operating cash flows" | FORWARD-SIGNAL | This commitment ties promoter income to dividend payout. That gives promoters a reason to raise payout, which competes with the funding need in D-A3-07. Employee cost still rose 54% YoY in Q2 (13.1 to 20.2). Ask whether the ESOP grant on the watch list includes any promoter or promoter relative. Ask what FY27 dividend policy follows from this commitment. |
| D-A3-09 | F7 | R519, R582 | fulltext 450-451 (p19); 503 (p21) | "Management recognizes that working capital has historically been an area of investor focus; recent operating cash flow performance provides additional context" | AMBIGUOUS | The hedge reads like legal-vetted framing ahead of the raise. It speaks to the market's working-capital concern with one positive half (H1 FY27 CFO +136.7) after three negative years (R847-R849). The land-sale note "Transaction size is extending completion" (line 503) hedges the slip. Ask whether management will commit to positive full-year FY27 CFO. |
| D-A3-10 | F8 | R288-R300, R332/R333, R380/R381, R689-R691 | fulltext 227-228 (p10; scrambled, values per render) | Tax Expenses "36.7 / 20.9 / 29.9 / 66.6 / 36.2" against PBT "166.0 / 87.9 / 134.8 / 300.8 / 146.8" | AMBIGUOUS | ETR is 22.1% in Q2 FY27, 22.2% in Q1 FY27 and 22.1% in H1 FY27, against 23.8% in Q2 FY26, 24.7% in H1 FY26 and 25.6% in FY26. The statutory rate is 25.17%. The H1 shield is 303 bps, about Rs 9.1 Cr ((25.17% - 22.14%) x 300.8), or 3.9% of H1 PAT. Net deferred tax flipped from a 0.3 DTL to a 0.9 DTA. A partnership subsidiary (Shri Rishab) should lift ETR, not lower it. Ask what drives the lower rate and whether it lasts. |
| D-A3-11 | F8 | R417/R418, R299/R300, R400/R401, R844, R689 | fulltext 273 (p12; label line scrambled, values per render) | "Less: Direct Taxes paid  -25.9  -34.4" | FORWARD-SIGNAL | Cash tax paid in H1 FY27 was 25.9 against a P&L tax charge of 66.6, a 39% ratio. In H1 FY26 the ratio was 95% (34.4/36.2). Current tax liability rose from 5.6 to 51.1. H1 CFO of 136.7 therefore carries about 40 Cr of tax not yet paid. H2 cash tax will catch up and reduce H2 CFO. Ask about the advance-tax position. |
| D-A3-12 | F10 | R362/R363, R765-R767, R617, R623-R625 | fulltext 237 (p11); 717 (p37); 593-595 (p27) | "(a) Equity share capital                      154.9       154.9" | FORWARD-SIGNAL | Paid-up capital did not change in H1 FY27. It rose 8.2 Cr in FY26 (146.7 to 154.9), and the deck names no corporate action for that rise. The deck carries no EPS, so the basic-vs-diluted spread cannot be tested. A QIP of up to Rs 1,800 Cr (watch list) equals 1.27x Sep-26 total equity of 1,422.4. The ESOP grant is absent from the deck. A4 to cross-check face value, share count, the FY26 issuance and outstanding warrants (2023 promoter warrants, line 595). |
| D-A3-13 | F11 | R572, R900, R680, R762, R823, R777, R780, R798 | fulltext 494 (p21); 786 (p40) | "ROCE                 ~30–35%     36% in FY26                                                            Achieved early" | AMBIGUOUS | The deck's ROCE equals EBIT / (total assets - current liabilities): FY26 457.9/1,271.5 = 36.0%, FY25 30.3%, FY24 27.2%. All three match slide 40. That definition removes current borrowings of 799.8 Cr from capital employed, and those are 94% of FY26 debt. With all borrowings counted, FY26 ROCE is 22.3% (457.9 / (1,205.9 + 48.1 + 799.8)). The "Achieved early" claim and any quality-ladder rung placement depend on the definition. Ask management to confirm it. |
| D-A3-14 | F11 | R364/R365, R362/R363, R366, R306, R368/R369 | fulltext 237-239 (p11) | "(b) Other equity                             1,250.6     1,037.1" | NEUTRAL-FACT | Net worth ties: 154.9 + 1,250.6 = 1,405.5 against 1,405.4 shown (rounding). Mar-26, Mar-25 and Mar-24 also tie. The other-equity roll-forward leaves about 17.7 Cr unexplained (H1 PAT 234.3 - NCI rise 3.1 - other-equity rise 213.5). That is 1.3% of net worth, under the 5% threshold. Candidate items: FY26 dividend paid in H1, OCI, acquisition accounting. It links to D-A3-08. |
| D-A3-15 | F14 | R193, R589, R161, R129, R164, R132, R260, R262, R283 | fulltext 202 (p9); 507 (p21) | "Operational PAT / PBT is reported PBT / PAT less non operational income & exceptional items" | AMBIGUOUS | The calculation does not match the stated definition. Q2 operational PBT of 173.4 is reported PBT 166.0 plus the 7.4 exceptional charge. Other income of 14.4 (up from 8.0 in Q1) is not removed. In Q1, operational PBT equals reported PBT (134.8), and other income of 8.0 is kept. "Operational" therefore only adds back charges. This metric supports the p21 "5.6% ... Exceeded" PAT claim. Ask what other income contains (interest, hedging or gold fair-value gains) and why it was not removed. |
| D-A3-16 | F14 | R208-R212, R213-R217, R650-R652 | fulltext 212 (p10) | "Purchase of Stock in Trades              -43.6    16.6" | AMBIGUOUS | Q2 FY27 purchases of stock-in-trade are negative (-43.6) after +74.0 in Q1, netting to 30.4 for H1. A negative purchase line points to a Q2 reclassification of Q1 costs, in the first quarter under the new auditor. Q1 inventory change was -255.2 and Q2 +30.0. This trading line was zero in FY24 and FY25 (R651/R652) and first appeared in FY26 at 108.5. Ask whether Q1 FY27 was restated, and what the trading activity is. |
| D-A3-17 | F14 | R507, R515, R505 | fulltext 426 vs 413 (p18) | "currently generates a PAT margin of ~4.5%" | NEUTRAL-FACT | The same slide says H1 FY27 PAT margin is 5.3% (line 413). The ~4.5% text is FY26 language carried into this deck. Taken with the ₹5,000 crore market-cap text (line 609) and H1 revenue shown as 4,403.4 vs 4,403.5 (R578), it shows template reuse. Governance-data point only. |
| D-A3-18 | F15 | R434, R868, R626, R619, R628, R368/R369, R774-R776, R443, R537 | fulltext 283 and 760 (p12, p38; scrambled); 594-597 (p27, column not render-checked); 290 vs 588-589 | "Acquisition of 51% partnership interest in Shri Rishab Gold through Starmangalsutra" | AMBIGUOUS | Entity-list changes inside the deck periods: (a) an unnamed subsidiary was derecognised in FY26 (cash -2.9 in H1 FY26 and FY26); (b) Shri Rishab Gold is a 51% partnership interest held through Starmangalsutra, so a step-down partnership. NCI went from 0 to 13.9 to 17.0. (c) Purvi is called "Purvi Gems" (line 290) and "M/s. Purvi Gems & Jewellery" (line 588-589); "M/s." suggests a firm, not a company. (d) Speed Bangle was renamed from Ganna N Gold. The deck does not give stakes in Sparkling, Starmangalsutra or Speed Bangle. Ask for the full list of entities with stakes and legal form, and which entity was derecognised. |
| D-A3-19 | F16 | R599 | fulltext 538 (p23) | "*Revenue Projection on consolidated level" | FORWARD-SIGNAL | This footnote describes a revenue projection, but the chart shows actuals only (FY22-H1FY27). A1 found no asterisk marker on the slide in the text layer or the render. A forward projection was likely removed from the chart and its footnote left behind. With D-A3-22, the deck has stopped putting a forward revenue number in front of investors during a QIP window. Ask whether a FY27/FY28 revenue outlook exists. |
| D-A3-20 | F16 | R478, R611, R028, R047 | fulltext 383 (p17, column not render-checked); 564 (p26) | "Volumes at a run-rate of ~200 kgs per month" | FORWARD-SIGNAL | The only volume figure in the deck is the FY23 run-rate. The "What we have achieved" side gives no current kg. Capacity is 14.4 tonne/year, which is 1,200 kg/month. Revenue grew 61% YoY with no split between gold price and volume. Operator watch items 1 and 2 are not disclosed. Without volume, the deck does not show how much growth came from gold price. Ask for kg processed in Q2 FY27, Q1 FY27 and Q2 FY26. |
| D-A3-21 | F16 | R568-R570, R588, R589, R153, R185 | fulltext 493 (p21) | "PAT margin           4.5–4.75%   5.6% in Q2 FY27*" | AMBIGUOUS | The PAT guidance is scored on the operational margin (5.6%), not the reported margin (5.4%, R153). It is also scored on one quarter against a range that looks annual. The guidance period is not stated. Reported H1 is 5.3%, so the claim still holds on the reported basis. The yardstick switch matters because the operational definition only adds back charges (D-A3-15). Ask which period and basis the 4.5-4.75% guidance uses. |
| D-A3-22 | F16 | R565, R568, R571, R574, R580, R581 | fulltext 486-496 (p21) | "Original FY27 revenue target of ₹5,000 Cr surpassed a year early" | FORWARD-SIGNAL | The scorecard closes the old FY27 target and gives no new FY27 or FY28 revenue number. The margin and ROCE guidance (7.0-7.5%, 4.5-4.75%, ~30-35%) carry no period. Together with D-A3-19, forward revenue guidance has gone quiet just before a QIP. Ask for FY27 and FY28 revenue and margin guidance with periods. |
| D-A3-23 | F16 | R501-R503, R509, R510, R487, R488, R493, R580 | fulltext 412 (p18) vs 390-391 (p17, column not render-checked) and 486 (p21) | "we guided for ₹3,000 Cr revenue, ~3% PAT margin, and cash-flow neutrality by FY27–28" | AMBIGUOUS | The deck gives conflicting "original" targets. p18 says Rs 3,000 Cr by FY27-28, set after the FY24 allotment. p17 says FY23 guidance was ~Rs 5,000 Cr for FY27 at ~3.5% PAT margin, and p21 calls Rs 5,000 Cr the "Original FY27 revenue target". A FY23 target of 5,000 followed by a FY24 target of 3,000 would be a cut, then a later upgrade. The p17 column reading is not render-checked. Ask for the dated guidance history. |
| D-A3-24 | F16 | R080-R092, R101, R390-R393, R805, R808, R512, R602 | fulltext 157-162, 184 (p8); 427 (p18) | "Working capital days has improved, because of the scale benefits, higher export mix, increased spot payments and greater share of advance gold volumes." | FORWARD-SIGNAL | All of the improvement came from payables. Net WC days fell from 59 to 55, but receivable days rose from 26 to 33 and inventory days from 37 to 39. Payable days moved from -4 to -17. Trade payables rose from 92.2 to 437.5 (4.7x, +345.3 Cr), which exceeds H1 CFO of 136.7. MSME payables rose from 64.9 to 182.3. The days use "*Based on quarterly sales" (line 184), which flatters days while sales rise 18.8% QoQ. If payables return to normal, CFO reverses. Ask what the payables are (gold supplier credit?), their terms, and MSME 45-day payment compliance. |
| D-A3-25 | F16 | R372/R373, R384/R385, R344-R347, R912 | fulltext 153 (p8); 535 (p23) | "Improving Financial Position" / "Building Fortress Balance Sheet" | FORWARD-SIGNAL | Net debt rose 42.7% in H1. Borrowings went from 847.9 to 939.4 (48.1+799.8 to 117.9+821.5). Cash plus other bank balances fell from 235.4 to 65.2. Net debt went from 612.5 to 874.2 (+261.7 Cr), against positive CFO. The deck states no net-debt figure (operator watch item 7). Non-current borrowings rose 2.5x. Leases are excluded, and some bank balances may be lien-marked. Ask for net debt as management defines it, and whether QIP proceeds will retire debt. |
| D-A3-26 | F11 | R350/R351, R421/R422, R318/R319, R346/R347 | fulltext 257-259 (p11; scrambled); 275 (p12) | Other current financial assets "382.3 / 18.8"; investing "-127.5" | AMBIGUOUS | Other current financial assets rose 20x, from 18.8 to 382.3 (+363.5 Cr), and are now 13.2% of total assets. The deck gives no comment. Investing outflow was 127.5 while PPE rose only 12.8 and investments and bank balances fell. A large investing outflow with little capex points to deposits, advances or loans. Ask what the line contains: gold deposits, margin money, advances to acquirees, or related-party loans. |
| D-A3-27 | F16 | M004 (line 396, treated as ledger row), R496, R441, R453 | fulltext 396-398 (p17, column not render-checked); 288 (p13) | "Presence in light-weight jewellery, with dominance in 22kt and ... strategic shift toward lower-kt and studded jewellery mix" | AMBIGUOUS | The 22kt dominance and the move to lower-kt and studded jewellery read as an FY23 claim and plan. The current studded share is "~2.3%" (line 288), and the deck gives no current karat mix. Lower-kt products cut the gold content per piece, which matters when gold prices are high. Ask for the Q2 FY27 karat mix and the studded share trend (watch item 3, margin per gram). |
| D-A3-28 | F13 | R445, R452, R444, R492, R620 | fulltext 300-303 (p13) | "has been appointed as the Statutory Auditors. ... The current quarter's financials have been reviewed by them." | AMBIGUOUS | The statutory auditor changed to MSKA (a BDO member firm). The deck names neither the outgoing auditor nor the reason. Q2 FY27 is the first limited review by MSKA. Its first quarter shows a new exceptional charge (D-A3-01), Rs 46.4 Cr of zeroed asset lines (D-A3-02) and a negative purchase line (D-A3-16). A new Internal Auditor was also appointed (line 299-301). Ask who the outgoing auditor was, why it resigned or rotated, and whether the review raised any qualifications or reclassifications. |
| D-A3-29 | F17 | R478, R216/R226, R080-R092, R584, R466, R355, R520 | fulltext 383, 505, 355, 453 (deck-level audit; no transcript) | "GML was nil as of Mar 2026." | AMBIGUOUS | Silence audit run against the deck, since no transcript exists yet. Of 8 watch items: 4 are silent (volume, gold-price/volume split, customer concentration, equity raise by name), 3 are partial (margin as % only, GML only to Mar-26, net debt only derivable) and 1 is addressed (WC days). See Section 4. The call-level silence audit stays open for the 31-Oct transcript. |
| D-A3-30 | F16 | R513, R469, R601, R454, R226-R233 | fulltext 418 (p18); 362-363 (p16); 523 (p23) | "The company bills only for the making charges." | AMBIGUOUS | The deck gives two explanations for gross-margin expansion (8.2% to 9.6% YoY). p16 credits value-added mix (line 362). p23 also lists the advance-gold model as a margin lever (line 523). Under advance gold, revenue excludes the metal, so a rising advance-gold share lifts GP% through the denominator alone, with no pricing gain. The advance-gold share of volume is the figure that separates the two explanations, and the deck does not give it. Ask for advance-gold share of kg and of revenue, Q2 FY26 against Q2 FY27. |

Finding count: 30. FORWARD-SIGNAL 11 | AMBIGUOUS 17 | CONFIRMATORY-NEGATIVE 0 | NEUTRAL-FACT 2.

## 2. CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 | FINDING | All 41 ZERO_STANDING rows read. Most are template lines (current investments, current tax assets, NC other financial liabilities, trade-payables headings, historical CF lines). Three changed: the exceptional line went from zero to -7.4 (D-A3-01). Non-current investments (44.0) and investment property (2.4) went to 0.0 (D-A3-02). Cash on acquisition is 0.0 despite the Purvi buy (D-A3-03). R584 GML nil, see D-A3-06. Held for sale and NCI were zero before FY26 and are now live (D-A3-05, D-A3-18). |
| F2 | FINDING | The deck has no standalone column. The p20 subsidiary table allows a partial decomposition: acquired entities' FY26 PAT is 28.6% of consolidated PAT, and Speed Bangle earns a 39.5% margin (D-A3-04). The 5 pp gap trend cannot be tested without standalone figures. |
| F3 | N.A. | The deck has no standalone cost lines, so shell detection is not possible. |
| F4 | N.A. | The deck has no auditor review report or Other Matters paragraph. |
| F5 | N.A. | The deck has no Going Concern or EoM paragraph, and there is no prior-quarter text to diff. |
| F6 | FINDING | Lexicon hits: "will" (lines 310, 327, 421), "to be driven" (529), "previously indicated" (433), "extended" (502), "not achieved" (504), "plans to" (399). Status changes: land sale slipped (D-A3-05), GML dropped (D-A3-06), internal-funding stance reversed (D-A3-07), promoter dividend-only pay (D-A3-08). Register in Section 3. |
| F7 | FINDING | The strict lexicon hits only the safe-harbor "subject to" (line 78, boilerplate). The p19 framing and the land-sale hedge are non-lexicon pre-emptive cover (D-A3-09). |
| F8 | FINDING | ETR is 22.1% in H1 FY27 against 25.17% statutory (303 bps, about 9.1 Cr) and the DTL-to-DTA flip (D-A3-10). Cash tax is 39% of the P&L charge (D-A3-11). No "earlier years" tax line is shown in the deck. |
| F9 | N.A. | The deck shows no OCI or actuarial lines. |
| F10 | FINDING | Paid-up capital is flat in H1 at 154.9. The FY26 +8.2 Cr is unexplained. No EPS is shown. The QIP equals 1.27x equity (D-A3-12). |
| F11 | FINDING | Net worth ties for all four dates. The roll-forward gap of ~17.7 Cr is under 5% (D-A3-14). The ROCE definition excludes current borrowings: 36.0% shown against 22.3% with all debt (D-A3-13). Other current financial assets rose 20x (D-A3-26). D/E 0.7 ties ((48.1+799.8)/1,205.9). ROE 23% ties on closing equity (281.8/1,205.9). |
| F12 | N.A. | The deck carries no segment assets, liabilities or results. |
| F13 | FINDING | Statutory auditor change with no reason given; first review this quarter (D-A3-28). Capital-raise foreshadowed one day after the QIP approval (D-A3-07). No AGM, record date or director-term disclosure in the deck. |
| F14 | FINDING | Operational PAT definition does not match the calculation (D-A3-15). Negative purchases line (D-A3-16). Stale ~4.5% text (D-A3-17). Purvi entity name differs between slides (D-A3-18). Minor: QoQ PBT shows 23.1% on p9 and 23.2% on p10; PAT YoY 93.2% on p9 and 93.1% on p10; H1 revenue 4,403.4 on p21 and 4,403.5 on p6. All rounding, no finding. p1 "Unaudited" matches p13 "reviewed". |
| F15 | FINDING | Purvi Gems added, consolidation date open (D-A3-03). Unnamed subsidiary derecognised in FY26. Step-down partnership at 51%. Speed Bangle rename (D-A3-18). No prior-quarter list to diff. |
| F16 | FINDING | No prior deck, so only within-deck tests apply. Orphaned projection footnote (D-A3-19). Volume dropped after FY23 (D-A3-20). PAT guidance scored on operational basis (D-A3-21). No forward revenue guidance (D-A3-22). Conflicting original targets (D-A3-23). WC improvement comes from payables (D-A3-24). "Fortress" claim while net debt rose (D-A3-25). Karat-mix claim (D-A3-27). Margin denominator effect (D-A3-30). |
| F17 | FINDING | Run against the deck at the task message's direction; no transcript yet. 4 of 8 watch items silent and 3 partial (D-A3-29, Section 4). Transcript-level audit pending for 31-Oct-2026. |

## 3. COMMITMENT REGISTER (from F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| Promoters draw no salary; payouts only through dividends from operating cash flow | FY27 onward | p15 line 327-328 (R458) | initiated |
| Land sale (held for sale 110.1 Cr) to an outside buyer, not the promoter | beyond Aug 2026, no new date | p21 line 502-504 (R582) | underway (deadline missed, extended) |
| GML: 100% conversion | Dec FY25 | p21 line 504 (R583) | not achieved; plan revised (GML nil Mar-26) |
| Expansion funded through internal cash generation | standing | p19 line 433 (R518) | "previously indicated"; under review (QIP approved 27-Oct-2026 per watch list) |
| Cash-flow neutrality | FY27-28 | p18 line 412 (R510) | completed early (H1 FY27 CFO +136.7) |
| EBITDA margin 7.0-7.5% | period not stated | p21 line 492 (R565) | exceeded (7.9% Q2 FY27) |
| PAT margin 4.5-4.75% | period not stated | p21 line 493 (R568) | exceeded (5.6% operational Q2; 5.4% reported) |
| ROCE ~30-35% | period not stated | p21 line 494 (R571) | "achieved early" (36% FY26 on a definition without current debt) |
| Positive operating cash flow | not stated | p21 line 496 (R574) | achieved H1 FY27 |
| Reduce WC days through advance gold, ERP, export mix | undated | p23 line 529-533 (R602) | underway |
| Advance gold "will be transformative" for ROCE | undated | p18 line 421 (R511) | underway |
| Induct external leadership talent (SkyGold 3.0) | undated | p15 line 321-323 (R460) | initiated |
| Acquire 100% of Purvi Gems for Rs 9 Cr | Q2 FY27 | p13 line 290 (R439) | completed (as stated; consolidation date open) |
| Appoint MSKA (BDO) as statutory auditor; Q2 reviewed | Q2 FY27 | p13 line 300-303 (R445, R452) | completed |
| Appoint Doshi Jain & Co as internal auditor | Q2 FY27 | p13 line 299-301 (R444) | completed |
| Become a trusted global export partner | FY23 plan | p17 line 399-401 (R495) | underway (export share 8% FY25, 11% FY26, 18% H1 FY27) |
| Shift to lower-kt and studded mix | FY23 plan | p17 line 398 (R496) | underway (studded ~2.3%) |
| Open Dubai office; footprint 1,50,000 sq ft | done | p17 line 399-400 (R489, R491) | completed |
| Keep making substantial marketing and brand-building investments | undated | p30 line 659-661 (R640) | stated |

## 4. WHAT WAS NOT DISCUSSED (F17, deck-level; consecutive quarters of silence = 1, first read)

| watch item | deck status | ref |
|---|---|---|
| 1. Volume processed (kg / tonnes) | SILENT. Only FY23 ~200 kg/month and capacity 14.4 t/yr | lines 383, 564 |
| 2. Revenue growth split, gold price vs volume | SILENT | none |
| 3. Gross margin per gram or % | PARTIAL. % only (9.6% Q2 FY27); no per-gram figure; no karat mix | line 216 |
| 4. WC days, inventory, receivables | ADDRESSED. Days and balances given; composition worsened except payables (D-A3-24) | lines 157-162; 252-254 |
| 5. GML use and interest cost | PARTIAL. Nil at Mar-26; Sep-26 not given; finance cost 25.5 total only | lines 505, 225 |
| 6. Customer concentration | SILENT. One unnamed Middle East chain only | line 355 |
| 7. Net debt | PARTIAL. Not stated; derivable at 874.2 (D-A3-25) | p11 lines 244-257 |
| 8. Equity raise (QIP up to Rs 1,800 Cr; EGM 18-Nov-2026; ESOP) | SILENT by name. Indirect reference only | line 453 |

## 5. LEDGER RECONCILIATION NOTE
All 915 IDs were read in the structured file and checked at their fulltext lines. The scrambled tables on pages 7-12 and 36-40 were checked against A1's render-sourced values. M001-M003 (addresses, chart-axis ticks) were read; no forensic content. M004 (line 396) was treated as a ledger row (D-A3-27). No row was left unread.

```yaml
stage: A3-forensics
company: "SKYGOLD"
quarter: "q2fy27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/skygold-q2fy27/work/forensics_presentation_skygold_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: N.A.
  F10: FINDING
  F11: FINDING
  F12: N.A.
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: FINDING
  F17: FINDING
findings:
  - {id: "D-A3-01", check: "F1", line: "225-226 (p10)", classification: "FORWARD-SIGNAL", implication: "Exceptional line live for first time: -7.4 Cr Q2 FY27, nature undisclosed, first quarter under new auditor"}
  - {id: "D-A3-02", check: "F1", line: "239-240, 243-244 (p11)", classification: "AMBIGUOUS", implication: "NC investments 44.0 and investment property 2.4 went to 0.0 in H1 with no comment"}
  - {id: "D-A3-03", check: "F1", line: "290 (p13); 241 (p11); 281 (p12)", classification: "AMBIGUOUS", implication: "Purvi Gems buy (Rs 9 Cr) but goodwill flat at 250.5 and acquisition cash 0.0; completion and consolidation date open"}
  - {id: "D-A3-04", check: "F2", line: "472-474, 477-480 (p20)", classification: "AMBIGUOUS", implication: "Acquired entities 28.6% of FY26 PAT; Speed Bangle 39.5% PAT margin on job work; intra-group share and post-acquisition attribution unknown"}
  - {id: "D-A3-05", check: "F6", line: "500-504 (p21)", classification: "FORWARD-SIGNAL", implication: "Land sale missed Aug-2026, no new date; held for sale 110.1 Cr; buyer switched from promoter to unnamed outside party; loss-on-sale risk"}
  - {id: "D-A3-06", check: "F6", line: "504-505 (p21)", classification: "AMBIGUOUS", implication: "GML 100% conversion dropped; Sep-26 GML not given; gold funding may have moved to supplier credit"}
  - {id: "D-A3-07", check: "F13", line: "433, 453 (p19)", classification: "FORWARD-SIGNAL", implication: "Internal-cash funding stance walked back; capital raise foreshadowed one day after QIP approval of up to Rs 1,800 Cr"}
  - {id: "D-A3-08", check: "F6", line: "327-329 (p15)", classification: "FORWARD-SIGNAL", implication: "Dividend-only promoter pay ties promoter income to payout; check ESOP recipients; employee cost +54% YoY"}
  - {id: "D-A3-09", check: "F7", line: "450-451 (p19); 503 (p21)", classification: "AMBIGUOUS", implication: "Legal-style framing of one positive CFO half after three negative years; hedge on land-sale slip"}
  - {id: "D-A3-10", check: "F8", line: "227-228 (p10)", classification: "AMBIGUOUS", implication: "ETR 22.1% vs 25.17%; 303 bps shield about 9.1 Cr H1 (3.9% of PAT); DTL to DTA flip; step-up risk"}
  - {id: "D-A3-11", check: "F8", line: "273 (p12)", classification: "FORWARD-SIGNAL", implication: "Cash tax 39% of P&L tax vs 95% a year ago; current tax liability 5.6 to 51.1; about 40 Cr H2 CFO headwind"}
  - {id: "D-A3-12", check: "F10", line: "237 (p11); 717 (p37); 593-595 (p27)", classification: "FORWARD-SIGNAL", implication: "Capital flat H1; FY26 +8.2 Cr unexplained; no EPS; QIP up to 1.27x total equity; ESOP absent from deck"}
  - {id: "D-A3-13", check: "F11", line: "494 (p21); 786 (p40)", classification: "AMBIGUOUS", implication: "ROCE 36% = EBIT/(TA-CL), excludes 799.8 Cr current borrowings; with all debt 22.3%; affects ladder rung"}
  - {id: "D-A3-14", check: "F11", line: "237-239 (p11)", classification: "NEUTRAL-FACT", implication: "Net worth ties; other-equity roll-forward gap about 17.7 Cr (1.3%), candidate dividend or OCI"}
  - {id: "D-A3-15", check: "F14", line: "202 (p9); 507 (p21)", classification: "AMBIGUOUS", implication: "Operational PAT adds back exceptional but keeps other income 14.4 despite stated definition; metric supports guidance claim"}
  - {id: "D-A3-16", check: "F14", line: "212 (p10)", classification: "AMBIGUOUS", implication: "Negative Q2 stock-in-trade purchases -43.6 after +74.0 in Q1; possible Q1 reclass in first BDO-reviewed quarter"}
  - {id: "D-A3-17", check: "F14", line: "426 vs 413 (p18)", classification: "NEUTRAL-FACT", implication: "Stale ~4.5% PAT margin text beside 5.3%; template reuse"}
  - {id: "D-A3-18", check: "F15", line: "283, 760 (p12, p38); 594-597 (p27); 290 vs 588-589", classification: "AMBIGUOUS", implication: "Unnamed subsidiary derecognised FY26; 51% step-down partnership; Purvi entity form inconsistent; stakes undisclosed"}
  - {id: "D-A3-19", check: "F16", line: "538 (p23)", classification: "FORWARD-SIGNAL", implication: "Orphaned revenue-projection footnote with no projection on chart; forward number removed"}
  - {id: "D-A3-20", check: "F16", line: "383 (p17); 564 (p26)", classification: "FORWARD-SIGNAL", implication: "Volume shown only for FY23 (~200 kg/month); no current kg; 61% growth not split gold price vs volume"}
  - {id: "D-A3-21", check: "F16", line: "493 (p21)", classification: "AMBIGUOUS", implication: "PAT guidance scored on one-quarter operational 5.6% not reported 5.4%; guidance period unstated"}
  - {id: "D-A3-22", check: "F16", line: "486-496 (p21)", classification: "FORWARD-SIGNAL", implication: "Old FY27 target closed, no new FY27/FY28 revenue guidance; margin and ROCE guidance carry no period"}
  - {id: "D-A3-23", check: "F16", line: "412 (p18); 390-391 (p17); 486 (p21)", classification: "AMBIGUOUS", implication: "Conflicting original targets: 3,000 Cr by FY27-28 vs 5,000 Cr FY27; p17 column not render-checked"}
  - {id: "D-A3-24", check: "F16", line: "157-162, 184 (p8); 427 (p18)", classification: "FORWARD-SIGNAL", implication: "WC-days gain is all payables (92.2 to 437.5, 4.7x, above H1 CFO 136.7); receivable and inventory days worse; CFO reversal risk"}
  - {id: "D-A3-25", check: "F16", line: "153 (p8); 535 (p23)", classification: "FORWARD-SIGNAL", implication: "Net debt 612.5 to 874.2 (+42.7%) under 'Improving Financial Position' and 'Fortress' headlines; no net-debt figure given"}
  - {id: "D-A3-26", check: "F11", line: "257-259 (p11); 275 (p12)", classification: "AMBIGUOUS", implication: "Other current financial assets 18.8 to 382.3 (20x); investing outflow 127.5 vs PPE +12.8; contents unknown"}
  - {id: "D-A3-27", check: "F16", line: "396-398 (p17); 288 (p13)", classification: "AMBIGUOUS", implication: "M004 22kt dominance and lower-kt/studded shift (FY23 plan) vs studded ~2.3% now; no current karat mix"}
  - {id: "D-A3-28", check: "F13", line: "300-303 (p13)", classification: "AMBIGUOUS", implication: "Statutory auditor changed, outgoing auditor and reason not named; first review quarter carries exceptional, zeroed assets, negative purchases"}
  - {id: "D-A3-29", check: "F17", line: "383, 505, 355, 453", classification: "AMBIGUOUS", implication: "Deck silent on 4 of 8 watch items and partial on 3; transcript audit pending 31-Oct"}
  - {id: "D-A3-30", check: "F16", line: "418 (p18); 362-363 (p16); 523 (p23)", classification: "AMBIGUOUS", implication: "Margin gain is value-added mix or advance-gold denominator effect; advance-gold share is the separating figure, not disclosed"}
forward_signals: ["D-A3-01", "D-A3-05", "D-A3-07", "D-A3-08", "D-A3-11", "D-A3-12", "D-A3-19", "D-A3-20", "D-A3-22", "D-A3-24", "D-A3-25"]
ambiguous: ["D-A3-02", "D-A3-03", "D-A3-04", "D-A3-06", "D-A3-09", "D-A3-10", "D-A3-13", "D-A3-15", "D-A3-16", "D-A3-18", "D-A3-21", "D-A3-23", "D-A3-26", "D-A3-27", "D-A3-28", "D-A3-29", "D-A3-30"]
commitments:
  - {commitment: "Promoters draw no salary; payouts only via dividends from OCF", implied_date: "FY27 onward", ref: "p15 line 327-328 (R458)", status_word: "initiated"}
  - {commitment: "Land sale (held for sale 110.1 Cr) to outside buyer", implied_date: "beyond Aug 2026, no new date", ref: "p21 line 502-504 (R582)", status_word: "underway (extended)"}
  - {commitment: "GML 100% conversion", implied_date: "Dec FY25", ref: "p21 line 504 (R583)", status_word: "not achieved; plan revised"}
  - {commitment: "Expansion funded through internal cash generation", implied_date: "standing", ref: "p19 line 433 (R518)", status_word: "under review (QIP approved 27-Oct-2026)"}
  - {commitment: "Cash-flow neutrality", implied_date: "FY27-28", ref: "p18 line 412 (R510)", status_word: "completed"}
  - {commitment: "EBITDA margin 7.0-7.5%", implied_date: "not stated", ref: "p21 line 492 (R565)", status_word: "completed (exceeded Q2)"}
  - {commitment: "PAT margin 4.5-4.75%", implied_date: "not stated", ref: "p21 line 493 (R568)", status_word: "completed (exceeded, operational basis)"}
  - {commitment: "ROCE ~30-35%", implied_date: "not stated", ref: "p21 line 494 (R571)", status_word: "completed (definition flag)"}
  - {commitment: "Positive operating cash flow", implied_date: "not stated", ref: "p21 line 496 (R574)", status_word: "completed (H1 FY27)"}
  - {commitment: "Reduce WC days via advance gold, ERP, exports", implied_date: "undated", ref: "p23 line 529-533 (R602)", status_word: "underway"}
  - {commitment: "Advance gold transformative for ROCE", implied_date: "undated", ref: "p18 line 421 (R511)", status_word: "underway"}
  - {commitment: "Induct external leadership talent", implied_date: "undated", ref: "p15 line 321-323 (R460)", status_word: "initiated"}
  - {commitment: "Acquire 100% Purvi Gems for Rs 9 Cr", implied_date: "Q2 FY27", ref: "p13 line 290 (R439)", status_word: "completed (consolidation date open)"}
  - {commitment: "MSKA (BDO) statutory auditor; Q2 reviewed", implied_date: "Q2 FY27", ref: "p13 line 300-303 (R445)", status_word: "completed"}
  - {commitment: "Doshi Jain & Co internal auditor", implied_date: "Q2 FY27", ref: "p13 line 299-301 (R444)", status_word: "completed"}
  - {commitment: "Global export partner", implied_date: "FY23 plan", ref: "p17 line 399-401 (R495)", status_word: "underway"}
  - {commitment: "Shift to lower-kt and studded mix", implied_date: "FY23 plan", ref: "p17 line 398 (R496)", status_word: "underway"}
  - {commitment: "Dubai office; 1,50,000 sq ft footprint", implied_date: "done", ref: "p17 line 399-400 (R489, R491)", status_word: "completed"}
  - {commitment: "Substantial marketing and brand-building investment", implied_date: "undated", ref: "p30 line 659-661 (R640)", status_word: "stated"}
gate_a3: pass
blank_checks: []
analyst_note: "The deck's cash story rests on two things it does not explain. H1 CFO of +136.7 came while trade payables rose 345.3 Cr and cash tax ran at 39% of the P&L charge. Strip those and H1 operating cash is likely negative again. Net debt rose 261.7 Cr in the same half. That is why p19 walks back the internal-funding promise one day after the QIP approval. ROCE is the second load-bearing number. The 36% excludes current borrowings, which are 94% of debt. With all debt counted it is 22.3%, roughly one quality-ladder rung lower (R3, not R4). Q2 FY27 is the first quarter under the new auditor. That quarter alone shows a new exceptional charge, 46.4 Cr of zeroed assets and a negative purchase line. A4 should treat these as one cluster and ask about them together. Margin expansion has two readings: value-added mix, or the advance-gold denominator effect. The advance-gold share of volume decides between them, and it is not disclosed. p17 and p27 column readings are not render-checked (D-A3-20, D-A3-23, D-A3-27, D-A3-18)."
```
