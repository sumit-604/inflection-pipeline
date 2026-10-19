# A3 FORENSIC NOTES: FEDFINA q2fy27 (doctype: concall)

Company: Fedbank Financial Services Ltd (FEDFINA). Quarter: Q2 FY27. Doctype: concall (ASR machine transcript of call audio, 68m32s).
Inputs read: extracted/fedfina-concall-q2fy27-structured.md (R001-R267, all 267 rows read), extracted/fedfina-concall-q2fy27-fulltext.md (lines 1-952, read in full), work/ledger_concall_fedfina_q2fy27.md (A2, 267 IDs), work/notion-thesis.md (prior promise log, prior Questions-for-Management, monitoring checklist). Filed cross-checks only through extracted/fedfina-results-q2fy27-structured.md ("Res R###") and extracted/fedfina-presentation-q2fy27-structured.md ("Deck R###"). No source PDF, no inputs/ file opened.
Prior-quarter fulltext: none on this branch. EoM / entity verbatim diffs not possible; F6 status transitions and F17 silence counts run against the Notion prior promise log and prior Questions-for-Management.

ASR CAVEAT (binds every finding). The fulltext carries no speaker labels. 52 of 74 turns are SPEAKER_INFERRED. Every finding below states whether its quote sits in an inferred turn. Garbled passages A1 flagged: lines 132-135 (src 109-111, metric label of "205.1 crore" lost, "40. 7.5%" ambiguous), line 420 (src 395, auction-loss sentence, negation likely dropped), line 826 (src 798, "un-argrove"). A3 adds two: lines 152-153 ("mortgage delinquency numbers across stages than the previous quarter", comparative word missing) and line 736 ("touch an AT in ROE", number lost; "eighteen" is a guess, not a reading).

## LEDGER RECONCILIATION
- Structured rows in ledger: 267 (R001-R267). Rows read at cited fulltext line: 267. Reconciled: 100%.
- Row-vs-fulltext mismatches found: none material. R203 cites line 424; the sentence starts at line 423. R111 ("about 75 | next quarter") is a parse A1 could not resolve; the line 539-541 sentence reads either "75 done this quarter, 100 in the next quarter" or "75 next quarter, 100 in Q4". A3 carries both readings (C06).
- ZERO_STANDING rows: 1 (R100). Handled under F1.
- DECLINED_GUIDANCE row R198 and qualifier rows R259 (Stage 2) used in FN-14.
- A2 flag NO_TURN_IDENTIFIED (R157-R159): three named senior managers never spoke. Note only.

## FINDINGS TABLE

| id | check | ledger row ref | line (turn) | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FN-01 | F1 | R100, R258, R203 | L420-424 (T19, CFO, SPEAKER_INFERRED, ASR_GARBLED at L420); L398-401 (T18) | L420 "We have had an auction loss on either principal or interest in the last six years, there is" / L421 "There's no intention to break that record." / L423 "we will not have any loss in terms of principle or interest" / L400-401 "get the recoverables through the auction process. We are fully geared for that." | AMBIGUOUS | The one nil standing claim on the call is a zero auction-shortfall record. The negation is lost in ASR. "Break that record" makes "have not had" the most likely reading, but this is not confirmed. The claim anticipates a transaction class: auction shortfall written off against principal or interest. Management also says it is "fully geared" for auctions while Stage 2 rises (FN-02) and incremental LTV runs above the book (FN-09). Auction volume is the forward variable. Ask for Q2 auction count and value, and any shortfall. The first shortfall breaks a six-year record the CEO and CFO stake credibility on. |
| FN-02 | F6 | R202, R265, R259, R201, R099, R079 | L387-392, L394, L414-415 (T18, CEO, SPEAKER_INFERRED); L160 (T05, CFO) | L387 "I don't think like that Renish" / L392 "there will be some numbers which will happen on the stage two side" / L414 "it may take one or two more quarters before customer behavior has changed" / L394 "I don't want to hold a number on the stage two side" | FORWARD-SIGNAL | The analyst asked whether Q2 Stage 2 / GNPA had peaked. The CEO did not confirm a peak. Stage 2 path is 2.2% (Q4 FY26, Notion) to 2.7% (Q1) to 3.6% (Q2) (L160; Deck R704-R706). The normalisation window now runs 1-2 more quarters (Q3-Q4 FY27), with no Stage 2 number guided. GNPA 1.8% (L91; Deck R709) leaves 20 bps to the CEO's own "below 2%" guide (L373) and sits inside checklist item 6 (1.9-2.1%). Expect a further Stage 2 rise in Q3. The test is Stage 2 to Stage 3 roll on the gold book. |
| FN-03 | F6 | R081, R038, R256, R267 | L167-171 (T05, CFO, explicit); L94 (T04, CEO, SPEAKER_INFERRED) | L167-168 "The decrease in PCR from 38.4% to 35.5% is due to a higher proportion of gold loans in stage three." / L169-170 "These gold loans carry a much lesser provisioning coverage per ECL." | FORWARD-SIGNAL | The Q1 promise "PCR optically reducing going forward" was delivered. Filed PCR fell 299 bps, 38.36% to 35.37% (Res R440-R441). This fails checklist item 2 (">= 38% and rising"). It also meets the Pillar 2L self-withdrawal wording "PCR thins further" on its face. The A4/operator ruling stays open. The mechanism persists: gold Stage 3 PCR is 10.5% vs mortgage 37.5% (Deck R726, R736), and gold Stage 3 went from 0.1% to 0.5% (Deck R720-R721). Each step up in gold Stage 3 pulls the blend toward the 32% tripwire. A3 arithmetic from the deck: segment GS3 Rs 234.4 + 47.6 = 282.0 Cr, provisions 88.0 + 5.0 = 93.0 Cr, so the blend is 33.0%. That is not the reported 35.4%. The 2.4 pp residual is unexplained (other segments or a different base). Ask for the bridge. |
| FN-04 | F6 | R125-R128, R242, R243, R216 | L727-733 (T51, CEO, SPEAKER_INFERRED); L888 (T66) | L727 "I have not revised the AUM guidance" / L728-729 "last year we had an ROA of about 2.4, we said we will improve that ROA by 30 to 40 basis points" / L729-730 "our AUM growth will be about 20 to 25 percent. This is what I had said in the month of March" / L888 "we will still give you a 20-25% growth on the AVM" | AMBIGUOUS | The CEO says the guidance is unchanged since March and July. The Q1 FY27 promise log records ROA +20-30 bps, entity AUM +20-22% and gold AUM +25-30%. On the call the ROA guide is restated 10 bps higher and the entity AUM top end 3 pts higher. The gold-specific 25-30% is never restated. L888 attaches "20-25%" to a tonnage-only (gold) context. Two readings: (a) the entity guide was quietly raised to 20-25% and the gold guide dropped from the call, or (b) the gold guide was quietly cut from 25-30% to 20-25%. The observation that separates them: a written FY27 guidance table split entity vs gold. Either way, a "not revised" claim that does not match the record is a CREDIBILITY data point. The turn is inferred, and ASR could have misheard "20 to 30" as "30 to 40". Ask for the guidance in writing. |
| FN-05 | F6 | R129, R149, R209, R217, R218, R231 | L734-736 (T51); L947-948 (T73) (both CEO, SPEAKER_INFERRED) | L734-735 "there might be an upside to the guidance that we have already given" / L735-736 "Our target ROA we are trying to reach is three and correspondingly try and touch an AT in ROE" / L947-948 "a ROA of three and we should see it sooner than we had promised you earlier" | FORWARD-SIGNAL | Q2 ROA 2.8% (Deck R088) already sits at the top of the restated +30-40 bps range (2.7-2.8%). The ROA 3 target is pulled forward, "sooner", with no date. The ROE target number is lost in ASR (L736). The bar moves up while NIM pressure is signalled (FN-06). That raises the miss risk at the next print. Ask for the dated ROA 3 quarter and the ROE target number. |
| FN-06 | F6 | R198, R199, R233, R215, R116-R118, R120 | L307-309 (T11, CEO, SPEAKER_INFERRED); L652, L659-662 (T42, CFO, SPEAKER_INFERRED); L681-683 (T47, CFO, SPEAKER_INFERRED); L632-633 (T40) | L307-308 "Q3 will be an intense market. It will be wrong of me to give you a guidance that we will play with a flattish yield." / L652 "No." / L661 "If there is a nim compression, we will handle it" / L681-682 "obviously there will be a limitation to how much we can pass it on" | FORWARD-SIGNAL | NIM compression is signalled for H2 FY27. Gold competition was "heightened" in Q2 (L238), with Q3 "intense". The rate cycle is turning up (analyst L583, L676; CFO "increasing interest rates" L147). Borrowings are 33% fixed and 24% MCLR, so the EBLR-linked residual is 43% (L630-633). That 43% transmits a hike fast. Deck by-position labels: yield 16.7% to 16.4% (Deck R560-R561), Ind-AS CoB 8.6% to 8.8% (Deck R580-R581), so the spread already narrowed about 50 bps QoQ. Management moves the defence to opex and credit cost levers. The FTTCP NIM/spread leg (STAGNANT) is at risk of turning negative. |
| FN-07 | F14 | R070, R071, R072, R252 | L138-143 (T05, CFO, explicit) | L139-140 "eels on the core loan book remained constant in quarter two compared to quarter one at 16.40 levels. The optical increase in eels by 29 bits" / L142-143 "weighted average cost of borrowing for quarter 2 flat at the same level as the previous three quarters at 7.80" | AMBIGUOUS | Yield: the CFO calls the 29 bp move an optical increase. The deck quarterly yield moves 16.7% to 16.4%, a 30 bp decrease (Deck R560-R561, by-position labels). Same magnitude, opposite sign. CoB: the CFO cites the i-GAAP daily average, 7.80%/7.79% (Deck R609-R610, footnote R624). The deck's other CoB series rose 8.6% to 8.8% (Deck R580-R581). The call picks the flattering basis on both legs of the spread. Ask for core yield and CoB on one stated basis for Q1 and Q2, and the DA-unwinding effect in bps each quarter. |
| FN-08 | F6 | R075, R253, R184, R076-R078 | L56 (T04, CEO, SPEAKER_INFERRED); L148-150 (T05, CFO, explicit) | L56 "even as we consciously reduce our reliance on direct assignment" / L148 "We did direct assignments of approximately 700 crores of the gold loan book to de-leverage." / L149 "aided by higher coal ending in the gold portfolio" | FORWARD-SIGNAL | The stated priority (reduce DA reliance) contradicts the quarter's action. Filed assignment is Rs 876.89 Cr (Res R472). The spoken "approximately 700" understates it by Rs 177 Cr (20% of filed). Deck incremental sell-down is Rs 1,085 Cr, the highest in the 15-quarter series; the prior high was 1,044 in Q1 FY26 (Deck R675, R680). Filed weighted residual maturity is 23 months (Res R473). That is long for a pool called "gold loan book", where the behavioural tenor is 2.5-3 months (L356). Either the pool is not all gold, or contractual tenor differs; ask. Debt-equity fell 4.89 to 4.61 (Res R388-R389). That only returns to the Mar-26 level of 4.61 (Res R390), and it came from asset sales, not capital. The AGM raised the securitisation/assignment limit to Rs 12,000 Cr. The forward read: de-leveraging and the GNPA denominator now lean on DA and co-lending (L92-93 "flattish AUF as we did our direct assignment"). DA income and excess-spread quality feed NII. |
| FN-09 | F6 | R015, R092, R093-R095, R106-R110 | L66, L259 (CEO, SPEAKER_INFERRED); L321-323 (T12, Jagdish Rao, SPEAKER_INFERRED); L484-485 (T25, SPEAKER_INFERRED); L498-501 (T27, CEO, SPEAKER_INFERRED) | L259 "we are still operating at 68%" / L500-501 "your portfolio is a mix of that seventy three percent, seventy two percent, seventy four percent" / L321 "there is a capping of 85%" / L484-485 "There is 20% of dispersal which is happening in income generating loan" | FORWARD-SIGNAL | The book LTV is stated at 68%. The working mix is described at 72-74%, and IGL (20% of disbursal) runs up to 85%. Incremental LTV sits above the book average, so the book drifts up. A3 arithmetic from the deck: gold AUM per tonne rose about 4.8% QoQ (11,191/12.7t = 881 Cr/t to 11,917/12.9t = 924 Cr/t; Deck R636-R637, R490-R491). The CFO called gold prices lacking momentum (L106). That gap fits a rising loan-to-gram, though a price rise inside the quarter is the other reading. Every speaker in these turns is inferred. Forward: a thinner collateral cushion, more auction exposure (FN-01), and no gold-price-down scenario on the call (FN-18). Ask for disbursal-weighted LTV for Q1 and Q2 and the share of the book above 75%. |
| FN-10 | F6 | R210-R213, R204-R206, R135-R137, R113 | L588-591, L611-613 (T36, CEO, SPEAKER_INFERRED); L464-465 (T21); L799-800 (T57) | L590-591 "it will be the best quarter compared to the last eight or nine quarters" / L612-613 "definitely it will be more than Q2 as well as the dispersals will be more" / L464 "the pedal will be pressed on Q3 and Q4" / L800 "now steadily they have moved up to the mid-40 or the early 40 levels" | FORWARD-SIGNAL | This is a dated and testable Q3 FY27 commitment. ST LAP disbursal must be the best of the last 8-9 quarters. That means above Rs 289 Cr (Q4 FY26, the highest quarter in Deck R475-R479); confirm the full 8-9 quarter series before scoring. Origination yield must be above 14.9% (Deck R326). Q2 delivered Rs 210 Cr, only +2% YoY on 206 (Deck R475, R479), just over the checklist bar of 208. Approval rates rose from about 30% to the early or mid 40s, while competitor appetite is "very, very aggressive" (L774). A growth push with rising approval rates in a crowded segment carries FY28 vintage risk. Track 1+ DPD on the H2 FY27 ST LAP vintage. |
| FN-11 | F6 | R014, R141, R142, R224, R214, R261-R263 | L885-886 (T66); L669-670 (T44); L757-759 (T51) (all CEO, SPEAKER_INFERRED) | L885-886 "We have given a tonnage growth of about 10-12% every year. We will continue that." / L670 "you will see a different trajectory in H2 for tonnage" / L757-759 "if the gold prices remain flat ... we will still give you a 20 to 25 percent. If the gold prices move up, then obviously we will do better" | FORWARD-SIGNAL | H2 carries the tonnage load. Deck tonnage: 12.6t (Q4 FY26) to 12.9t (Q2 FY27), +2.4% in H1 (Deck R489, R491). A 10-12% FY27 needs 13.9-14.1t, so +1.0-1.2t (+7.4-9.4%) in H2. Last year's H2 did +13.5% (11.1t to 12.6t, Deck R487, R489), so seasonality supports it. Entity AUM H1 +9.3% (20,153 to 22,035) needs +9.8-14.3% in H2 for 20-25%. The guidance is framed only on flat or rising gold prices. No downside case was offered. Test: Q3 tonnage at or above 13.4t keeps the path. |
| FN-12 | F7 | R189, R190, R082, R083, R208 | L188-192 (T05, CFO, explicit); L174-175; L542 (T31, CEO, SPEAKER_INFERRED) | L188 "we proposed to add at least another 150 branches" / L191-192 "we are hopeful of containing any material increases in cost to income over current levels" / L542 "it is not constrained by the cost to OPEX ratio" | FORWARD-SIGNAL | The cost-to-income downtrend stalls in H2. The CFO's best case is "containing" C/I at about 52.5% (L181), framed as "hopeful". Opex/ATA already rose from 4.8% to 4.9% (L174-175). Checklist item 4 ("falling into FY27") holds against FY26's 57.2% on the full year, but not quarter on quarter in H2. The CEO says branches are not constrained by the opex ratio. So the operating lever named in FN-06 as the NIM defence is partly spent on branches. |
| FN-13 | F7 | R232, R226, R147, R148 | L197-199 (T05, CFO, explicit); L905-907 (T68, CFO, SPEAKER_INFERRED) | L197-199 "shock buffers to potential headwinds on the interest rates or any insurance distribution related changes" / L906-907 "whenever that happens we are confident that we should be able to substitute to whatever is the reduction" / L905 "about a 0.1 in the ROA tree" | FORWARD-SIGNAL | The CFO raised an insurance-distribution change in prepared remarks, before any question. He then framed it as "whenever", not "if". About 0.1% of ROA (about 10 bps of 2.8%) is exposed. The substitute "other income tree" is not named. Ask what change is expected, its date, and the substitute line. |
| FN-14 | F7 | R198, R259, R233, R202 | L589 (T36, CEO); L307 (T11, CEO); L394 (T18, CEO); L646-647 (T40, CFO) (all SPEAKER_INFERRED) | L589 "I can't give you a definite guidance" / L307 "I don't want to specifically give you a guidance because it is a dynamic market" / L394 "I don't want to hold a number on the stage two side" / L646-647 "We have some levers. We will evaluate them" | AMBIGUOUS | Three numbers were declined on the call: gold yield, Stage 2, and ST LAP disbursal. One lexicon hedge ("evaluate") sits on the rate-hike defence. All three declined numbers are the variables that move in H2 (FN-02, FN-06, FN-10). Hard numbers were given only on lagging outcomes (credit cost, GNPA, ROA). A concall hedge is not legal cover, but this pattern tells us where management lacks visibility. |
| FN-15 | F14 | R017, R018, R038, R081, R267, R040 | L67-68 (T04, CEO, SPEAKER_INFERRED); L94 vs L167; L152-153 (T05) | L67-68 "taking our total gold branch count to 831. Total branch count to 831." / L94 "provision coverage ratio at 35.4%" vs L167 "38.4% to 35.5%" / L152-153 "mortgage delinquency numbers across stages than the previous quarter" | NEUTRAL-FACT | Spoken figures that differ from the filings: gold branches are 706, not 831 (Deck R496); 831 is the total (Deck R034). PCR is 35.4% in one turn and 35.5% in another; filed is 35.37% (Res R440). The mortgage delinquency sentence has lost its comparative word. Filed mortgage GS3 is flat at 3.4% (Deck R711-R712), against the CEO's "steady or in fact declining" (L349). Ties that hold: BVPS 84.4 (L96) = net worth Rs 3,164.96 Cr / 37.514 Cr shares = Rs 84.37 (Res R420, R169); D/E 4.6 (L150) = 4.61 (Res R388); credit cost Rs 27.1 Cr (L135) = impairment Rs 27.08 Cr (Res R043). Each gap is small on its own. Together with FN-04, FN-07 and FN-08, this call has four places where spoken numbers drift from the filings. That is a governance data point for CREDIBILITY-ND. |
| FN-16 | F17 | R081, R256 (nearest) | L167-171 (T05, CFO, explicit) | L171 "Our mortgage PCR continues at similar levels." | CONFIRMATORY-NEGATIVE | The PCR floor was not given. The gold-only vs mortgage-only PCR was not stated on the call (the deck shows 10.5% / 37.5%). This is the second consecutive quarter of silence: the Q1 call said "optically reducing" with no floor (Q1 QfM 5; AR top-3 #1). PCR is the most-at-risk tripwire and it fell 299 bps. Under Role 5, sustained silence on a deteriorating metric is a confirmatory negative. |
| FN-17 | F17 | R113, R137 (nearest) | L607-610 (T36, CEO, SPEAKER_INFERRED) | L607-609 "we were getting out of the woods in terms of the quality as well as we were putting guardrails and we were changing the manpower" | AMBIGUOUS | The checklist item 7 leg "ST LAP collections in-housing complete" was not confirmed. This is the second consecutive quarter (Q1 F17-3, QfM 10). The disbursal leg is met (Rs 210 Cr, L807; Deck R479), and management says ST LAP credit cost has normalised (L456-458, L463). The metric is not deteriorating, so this stays a question, not a negative. |
| FN-18 | F17 | R220, R261, R263 | L756-759 (T51, CEO, SPEAKER_INFERRED) | L756 "If the gold prices pick up in Q3 and Q4, you will definitely get a better performance." / L759 "If the gold prices move up, then obviously we will do better than that." | AMBIGUOUS | No gold-price-down scenario was discussed (AR top-3 #3, 15% correction impact). This is the first call since the AR review. With incremental LTV of 72-74% and IGL up to 85% (FN-09), a price fall moves directly into LTV breaches, auctions (FN-01) and Stage 3 (FN-03). Ask for the share of the book that crosses the regulatory LTV limit at a 10% and a 15% price fall. |
| FN-19 | F17 | R079, R080, R255 (nearest) | L160-161 (T05, CFO, explicit) | L160-161 "The increase in Stage 2 from 2.7% to 3.6% and in Stage 3 from 1.6% to 1.8% are entirely on account of this change constructed in goal loans." | CONFIRMATORY-NEGATIVE | Three things were not disclosed: gold 1+/30+/60+ DPD under bullet vs periodic structures (QfM 4), the Q1 GS3 provision bridge of about Rs 40 Cr (QfM 9; Q1 GNPA 1.87% ex write-off), and Q2 write-offs. This is the second consecutive quarter for each. Asset-quality ratios are rising, and the call offers attribution ("entirely") without the bucket data that would prove it. Confirmatory negative under Role 5. |
| FN-20 | F17 | R039, R077, R078 (nearest) | L129 (T05, CFO); L150 (T05, CFO) | L129 "Our growing ROE enhances our ability to fund the loan book expansion through internal approvals" / L150 "improved capital adequacy to 21% up from 20.7%" | AMBIGUOUS | Three items were not disclosed: the CRAR / Tier I floor that would trigger an equity raise (QfM 6, AR top-3 #2), the co-lending partner count, and the partner name (the Federal Bank parent co-lending trigger). Second consecutive quarter for CRAR floor and partner count. CRAR improved QoQ, but through DA (FN-08). "Internal approvals" is ASR, read as "internal accruals" (not confirmed). The implied no-equity stance is a commitment (C20). |
| FN-21 | F17 | R252, R184 (nearest) | L140-141 (T05, CFO, explicit) | L140-141 "the last quarter had a higher DA unwinding impact of around the same magnitude" | AMBIGUOUS | DA income and DA-unwinding drag were not quantified for the coming quarters, and no date was given for DA income turning neutral (QfM 7; Q1 promise "DA income negative going forward"). Second consecutive quarter, partial: the call gave about 29 bps on yield for Q1 only. With the Q2 assignment at a series high (FN-08), the excess-spread and unwinding schedule now matters more. |

## CHECKLIST SCORECARD

| check | status | one-line basis |
|---|---|---|
| F1 | FINDING | One ZERO_STANDING row (R100): nil auction loss over six years. The negation is ASR-garbled (L420), and the claim anticipates auction-shortfall losses (FN-01). |
| F2 | N.A. | Concall. No standalone vs consolidated statements on the call. |
| F3 | N.A. | Concall. No cost-line statements by entity. |
| F4 | N.A. | Concall. No auditor Other Matters paragraph. |
| F5 | N.A. | Concall. No Going Concern / EoM paragraph, and no prior-quarter fulltext on the branch. |
| F6 | FINDING | 49 FORWARD rows mined, 26 commitments registered. Status transitions vs Q1 log: de-leverage "we hope" went to completed via DA; PCR "optically reducing" was delivered; guidance was restated without matching the log (FN-02 to FN-11). |
| F7 | FINDING | Hedges: "hopeful" on C/I (L191), "whenever" on insurance (L906), "evaluate" on rate levers (L647), three declined numbers (FN-12 to FN-14). |
| F8 | N.A. | Concall. No tax lines discussed. |
| F9 | N.A. | Concall. No OCI discussed (FVOCI silence logged under F17). |
| F10 | N.A. | Concall. No share count or EPS discussed. The results A3 owns the paid-up 37,491 to 37,514 lakh move. |
| F11 | PASS | The spoken BVPS 84.4 ties to filed net worth Rs 3,164.96 Cr / 37.514 Cr shares = Rs 84.37 (Res R420, R169). D/E 4.6 ties to 4.61 (Res R388). CRAR 21% ties to the deck's 21.0% (Deck R070). |
| F12 | N.A. | Concall. No segment assets or liabilities discussed. |
| F13 | N.A. | Concall. No board outcome on the call (the AGM of 2026-09-29 sits in Notion, not this document). |
| F14 | FINDING | Spoken-vs-filed drift in four places: DA 700 vs 876.89, gold branches 831 vs 706, yield direction, PCR 35.4/35.5. CoB basis selection (FN-07, FN-15). |
| F15 | N.A. | Concall. No consolidation list, and no prior ledger (ENTITY_CHANGE untestable per A2). |
| F16 | N.A. | Presentation-specific check. The guidance-language changes are carried under F6 (FN-04). |
| F17 | FINDING | 8 checklist items and 10 prior QfM / AR / promise items audited. Ten rows silent or partial; six findings (FN-16 to FN-21); two are CONFIRMATORY-NEGATIVE. |

## COMMITMENT REGISTER (F6)

| # | commitment | implied date | note/turn ref | status word |
|---|---|---|---|---|
| C01 | Credit cost below 1% of average total assets, FY27 ("way below 1%") | Mar-27 | L89 (T04), L370 (T16), L943-945 (T73) | underway (Q1 0.78%, Q2 0.6%) |
| C02 | GNPA below 2% | Mar-27 | L372-373 (T16) | underway (1.8%, 20 bps headroom) |
| C03 | AUM growth about 20-25% FY27 on flat gold; better if gold rises | Mar-27 | L733, L757-759 (T51), L888 (T66) | underway (H1 +9.3%) |
| C04 | ROA +30-40 bps over FY26 ~2.4% (as restated; Q1 log says +20-30) | Mar-27 | L728-729 (T51) | underway (Q2 2.8%) |
| C05 | ROA 3 target "sooner than we had promised"; ROE target (number lost in ASR, L736) | undated | L735-736 (T51), L947-948 (T73), L564 (T31) | underway |
| C06 | At least 150 more branches in H2 FY27 (split read as 75 + 100 or 100 + more; ASR parse) | Mar-27 | L188-189 (T05), L68-69 (T04), L539-541 (T31) | initiated (H1: 74 total, gold 632 to 706) |
| C07 | Contain any material C/I increase over current ~52.5% despite H2 branches | H2 FY27 | L190-192 (T05) | initiated |
| C08 | Continue the opex-reduction trajectory; structural cost-intensity reduction "intact" | medium term | L179-180 (T05), L553, L562 (T31) | underway |
| C09 | Gold tonnage +10-12% a year; "different trajectory in H2" | Mar-27 | L885-886 (T66), L670 (T44) | underway (H1 +2.4%) |
| C10 | Gold growth per guidance in Q3-Q4; H2 beats H1 seasonally | Q3-Q4 FY27 | L248-249, L262-267 (T08), L290 (T09), L938 (T73) | underway |
| C11 | Gold customer-behaviour transition settles in "one or two more quarters" | Q3-Q4 FY27 | L414-415 (T18) | underway |
| C12 | No auction loss on principal or interest (six-year record, ASR-garbled at L420) | standing | L420-424 (T19) | underway |
| C13 | ST LAP Q3: best disbursal quarter of last 8-9; yield above Q2; disbursals higher | Q3 FY27 (Dec-26) | L588-591, L611-613 (T36) | initiated |
| C14 | ST LAP "pedal pressed" in Q3 and Q4; better yields, normalised ticket | H2 FY27 | L460-465 (T21), L941-942 (T73) | initiated |
| C15 | ST LAP ROA "different in Q3 and Q4"; later "touching the gold business ROA" | undated (cycle A/B) | L851-857 (T64) | initiated |
| C16 | ST LAP credit-cost stabilisation ("three four quarters") | done | L455-458 (T21), L463 | completed |
| C17 | IGL product ready in April and operating | Apr-26 | L268-271 (T08) | completed |
| C18 | DA of about Rs 700 Cr gold book to de-leverage; D/E 4.9 to 4.6; CRAR 21% (filed DA 876.89) | Q2 FY27 | L148-150 (T05) | completed |
| C19 | "Consciously reduce our reliance on direct assignment" | standing | L56 (T04) | underway (contradicted by Q2 record sell-down, FN-08) |
| C20 | Fund loan-book growth through internal accruals ("internal approvals", ASR) | standing | L129 (T05) | underway |
| C21 | Substitute insurance income through another income line "whenever" the distribution change comes | conditional | L906-907 (T68), L197-199 (T05) | initiated |
| C22 | Hold gold ROA flat at 20-25% AUM growth on flat price, via opex leverage (AUM per branch 8 to 16 Cr) | FY27 | L893-899 (T66) | underway |
| C23 | Gold branch expansion extends the ST LAP footprint | undated | L912-920 (T70) | underway |
| C24 | Absorb a rate shock and still deliver "superior ROA and ROE"; NIM compression handled by other levers | H2 FY27 | L686 (T47), L661-662 (T42) | initiated |
| C25 | Medium ticket LAP continues its trajectory (ASR_GARBLED L826) | undated | L825-826 (T61) | underway |
| C26 | Entry into eastern India | Q2 FY27 | L69 (T04) | completed |

Status transitions vs the Q1 FY27 promise log: "200 branches FY27" (0 in Q1) moved to 74 done plus at least 150 planned (stronger). "De-leverage, we hope" moved to completed, but through DA, not capital. "PCR optically reducing" was delivered (38.36% to 35.37%). "ROA +20-30 bps" was restated as +30-40 with a claim of no revision. "Entity AUM +20-22%" was restated as 20-25%. "Gold AUM +25-30%" was not restated (silent). "DA income negative going forward" got no update (silent).

## WHAT WAS NOT DISCUSSED (F17 silence audit)

Count = consecutive quarters of call silence on the specific item. Q1-originated items count 2 when the Q1 call also withheld the item. AR-originated items count from the first call after the AR (2026-09-09).

| # | item (source) | Q2 call status | nearest line | consecutive quarters silent |
|---|---|---|---|---|
| S01 | Checklist 2 / QfM 5 / AR #1: PCR floor; gold-only vs mortgage-only PCR | PCR fall explained; no floor, no segment PCR spoken | L167-171 | 2 |
| S02 | Checklist 7 / QfM 10: ST LAP collections in-housing complete | not confirmed (disbursal leg addressed) | L607-610 | 2 |
| S03 | Checklist 8 / QfM 2: absolute gold tonnage; split of AUM guide into tonnage / LTV / price | % growth spoken (16% YoY, L66); absolute tonnes and split not spoken | L66, L885-888 | 2 |
| S04 | QfM 4: gold 1+/30+/60+ DPD, bullet vs periodic | not discussed | L160-161 | 2 |
| S05 | QfM 9: GS3 provision bridge (~Rs 40 Cr); write-offs | not discussed | L160-161 | 2 |
| S06 | QfM 6 / AR #2: CRAR / Tier I floor that would trigger an equity raise; co-lending partner count | not discussed (CRAR level only) | L129, L150 | 2 |
| S07 | QfM 7 / promise log: DA-unwinding drag next 4 quarters; date DA income turns neutral | partial (Q1 ~29 bps on yield only) | L140-141 | 2 (partial) |
| S08 | QfM 8: FVOCI loss (~Rs 585 Cr) and ECL re-recognition | not discussed | none on call | 2 |
| S09 | AR #3: gold-price correction (15%) impact | not discussed; only flat or rising gold scenarios | L756-759 | 1 |
| S10 | Promise log: gold AUM +25-30% FY27 | not restated | L733, L888 | 1 |
| -- | Checklist 1 credit cost / FY27 guide | discussed (0.6%, sub-1%) | L87-89 | 0 |
| -- | Checklist 3 gold branches / AUM per branch | discussed (74 added; 16.9 Cr; count misspoken, FN-15) | L65-68 | 0 |
| -- | Checklist 4 C/I | discussed (52.5%) | L181-184 | 0 |
| -- | Checklist 5 ROE / ROA | discussed (17% / 2.8%) | L116-122 | 0 |
| -- | Checklist 6 GNPA / GS3 | discussed (1.8%) | L91 | 0 |
| -- | QfM 1 branches opened in Q2 | discussed (74) | L67, L187 | 0 |
| -- | QfM 3 FY27 stack firm | discussed ("committed to the guidances") | L943-945 | 0 |

Monitoring checklist outcome on this call (call figures, filed ties as cited): item 1 PASS (0.6%). Item 2 FAIL (35.4%, falling; above the 32% red line). Item 3 PASS on AUM per branch (16.9 Cr > 13.3); the "140-150" count criterion is ambiguous on the page (H1 gold +78, plan at least 150 in H2). Item 4 PASS on the level, at risk on trend (FN-12). Item 5 PASS (17% / 2.8%). Item 6 PASS (1.8%, 20 bps to the guide). Item 7 PARTIAL (210 Cr > 208; in-housing silent). Item 8 PASS on % growth, absolute tonnage not spoken. Tripwires: credit cost 0.6% (not fired); ROE 17% (not fired); PCR 35.37% (not fired, 337 bps above 32%). Pillar 2L "PCR thins further" wording: met on its face. Ruling left to A4 / the operator.

```yaml
stage: A3-forensics
company: "FEDFINA"
quarter: "q2fy27"
doctype: "concall"
model: "claude-opus-5-5"
status: complete
forensics_path: "work/forensics_concall_fedfina_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: N.A.
  F9: N.A.
  F10: N.A.
  F11: PASS
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: FINDING
findings:
  - {id: "FN-01", check: "F1", line: "L420-424, L400-401 (T18-T19, inferred, ASR_GARBLED L420)", classification: "AMBIGUOUS", implication: "Zero auction-loss record rests on a garbled negation; mgmt 'fully geared' for auctions as Stage 2 rises; ask Q2 auction count/value and any shortfall"}
  - {id: "FN-02", check: "F6", line: "L387-394, L414-415 (T18, inferred); L160", classification: "FORWARD-SIGNAL", implication: "Stage 2 2.2->2.7->3.6% not called peaked; 1-2 more quarters; GNPA 1.8% vs own <2% guide leaves 20 bps"}
  - {id: "FN-03", check: "F6", line: "L167-171 (T05); L94", classification: "FORWARD-SIGNAL", implication: "PCR 38.36->35.37% (-299 bps); checklist 2 fails; Pillar 2L 'thins further' wording met; gold PCR 10.5% keeps pulling blend toward 32%; deck segment blend 33.0% vs reported 35.4% unexplained"}
  - {id: "FN-04", check: "F6", line: "L727-733 (T51, inferred); L888", classification: "AMBIGUOUS", implication: "'Not revised' guidance restated as ROA +30-40bps / AUM 20-25% vs Q1 log +20-30bps / entity 20-22% / gold 25-30%; either entity guide raised or gold guide cut; credibility data point"}
  - {id: "FN-05", check: "F6", line: "L734-736 (T51), L947-948 (T73), inferred", classification: "FORWARD-SIGNAL", implication: "ROA 3 pulled forward undated while Q2 2.8% already tops restated range; bar rises into NIM pressure"}
  - {id: "FN-06", check: "F6", line: "L307-309, L652, L661, L681-682, L632-633 (inferred)", classification: "FORWARD-SIGNAL", implication: "NIM compression signalled for H2: yield guide declined, 43% EBLR borrowings transmit hikes, deck spread ~-50bps QoQ; FTTCP NIM leg at risk"}
  - {id: "FN-07", check: "F14", line: "L138-143 (T05, explicit)", classification: "AMBIGUOUS", implication: "CFO 'optical increase' 29bps in yield vs deck 16.7->16.4%; CoB 'flat 7.80' on i-GAAP basis vs deck CoB 8.6->8.8%; flattering basis on both spread legs"}
  - {id: "FN-08", check: "F6", line: "L56 (T04); L148-150 (T05, explicit)", classification: "FORWARD-SIGNAL", implication: "'Reduce reliance on DA' vs record Rs 1,085 Cr sell-down; spoken ~700 vs filed 876.89 Cr DA with 23-month residual maturity on a 'gold' pool; D/E back only to Mar-26 4.61 via asset sales"}
  - {id: "FN-09", check: "F6", line: "L259, L321, L484-485, L498-501 (all inferred)", classification: "FORWARD-SIGNAL", implication: "Book LTV 68% vs working mix 72-74% and IGL to 85% (20% of disbursal); AUM per tonne +4.8% QoQ on flat gold fits LTV creep; thinner collateral cushion"}
  - {id: "FN-10", check: "F6", line: "L588-591, L611-613, L464, L800 (inferred)", classification: "FORWARD-SIGNAL", implication: "Dated Q3 FY27 test: ST LAP disbursal best of 8-9 quarters (>Rs 289 Cr, confirm series), yield >14.9%; approval rates up to early/mid 40s in aggressive market = vintage risk"}
  - {id: "FN-11", check: "F6", line: "L885-886, L670, L757-759 (inferred)", classification: "FORWARD-SIGNAL", implication: "Tonnage H1 +2.4% (12.6->12.9t); 10-12% FY27 needs +7.4-9.4% in H2 (13.9-14.1t); AUM H2 needs +9.8-14.3%; guide framed only on flat/rising gold"}
  - {id: "FN-12", check: "F7", line: "L188-192 (T05, explicit); L174-175; L542", classification: "FORWARD-SIGNAL", implication: "C/I downtrend stalls in H2: CFO only 'hopeful' of containing at ~52.5% with >=150 branches; opex/ATA 4.8->4.9%"}
  - {id: "FN-13", check: "F7", line: "L197-199 (T05); L905-907 (T68, inferred)", classification: "FORWARD-SIGNAL", implication: "Insurance-distribution change pre-emptively raised, framed 'whenever'; ~10bps of ROA exposed; substitute unnamed"}
  - {id: "FN-14", check: "F7", line: "L307, L394, L589, L646-647 (inferred)", classification: "AMBIGUOUS", implication: "Three numbers declined (gold yield, Stage 2, ST LAP disbursal), exactly the H2 swing variables; hard numbers only on lagging outcomes"}
  - {id: "FN-15", check: "F14", line: "L67-68, L94 vs L167, L152-153", classification: "NEUTRAL-FACT", implication: "Gold branches spoken 831 vs filed 706; PCR 35.4/35.5 vs 35.37; mortgage sentence garbled; with FN-04/07/08 four spoken-vs-filed drifts on one call"}
  - {id: "FN-16", check: "F17", line: "L167-171 (nearest)", classification: "CONFIRMATORY-NEGATIVE", implication: "PCR floor and segment PCR silent 2 consecutive quarters on the most-at-risk, deteriorating tripwire"}
  - {id: "FN-17", check: "F17", line: "L607-610 (nearest, inferred)", classification: "AMBIGUOUS", implication: "ST LAP collections in-housing completion unconfirmed 2 quarters; disbursal leg met"}
  - {id: "FN-18", check: "F17", line: "L756-759 (nearest, inferred)", classification: "AMBIGUOUS", implication: "No gold-price-down scenario; with 72-74% incremental LTV a fall feeds LTV breaches, auctions, Stage 3"}
  - {id: "FN-19", check: "F17", line: "L160-161 (nearest)", classification: "CONFIRMATORY-NEGATIVE", implication: "Gold DPD buckets, GS3 provision bridge, write-offs silent 2 quarters while Stage 2/3 rise; 'entirely gold' attribution unproven"}
  - {id: "FN-20", check: "F17", line: "L129, L150 (nearest)", classification: "AMBIGUOUS", implication: "CRAR/Tier I equity-raise floor and co-lending partner count silent 2 quarters; CRAR uplift came via DA"}
  - {id: "FN-21", check: "F17", line: "L140-141 (nearest)", classification: "AMBIGUOUS", implication: "DA-unwinding drag and DA-income-neutral date unquantified 2 quarters (partial); matters more after record Q2 assignment"}
forward_signals: ["FN-02", "FN-03", "FN-05", "FN-06", "FN-08", "FN-09", "FN-10", "FN-11", "FN-12", "FN-13"]
ambiguous: ["FN-01", "FN-04", "FN-07", "FN-14", "FN-17", "FN-18", "FN-20", "FN-21"]
commitments:
  - {commitment: "Credit cost below 1% of avg total assets FY27", implied_date: "Mar-27", ref: "L89, L370, L943-945", status_word: "underway"}
  - {commitment: "GNPA below 2%", implied_date: "Mar-27", ref: "L372-373", status_word: "underway"}
  - {commitment: "AUM growth ~20-25% FY27 on flat gold", implied_date: "Mar-27", ref: "L733, L757-759, L888", status_word: "underway"}
  - {commitment: "ROA +30-40bps over FY26 ~2.4% (restated; log +20-30)", implied_date: "Mar-27", ref: "L728-729", status_word: "underway"}
  - {commitment: "ROA 3 sooner than promised; ROE target (number lost in ASR)", implied_date: "undated", ref: "L735-736, L947-948", status_word: "underway"}
  - {commitment: ">=150 branches in H2 FY27", implied_date: "Mar-27", ref: "L188-189, L539-541", status_word: "initiated"}
  - {commitment: "Contain C/I at ~52.5% despite H2 branches", implied_date: "H2 FY27", ref: "L190-192", status_word: "initiated"}
  - {commitment: "Continue opex-reduction trajectory", implied_date: "medium term", ref: "L179-180, L553, L562", status_word: "underway"}
  - {commitment: "Gold tonnage +10-12% a year; H2 trajectory change", implied_date: "Mar-27", ref: "L885-886, L670", status_word: "underway"}
  - {commitment: "Gold growth per guidance Q3-Q4; H2 beats H1", implied_date: "Q3-Q4 FY27", ref: "L248-249, L262-267, L938", status_word: "underway"}
  - {commitment: "Gold customer-behaviour transition in 1-2 more quarters", implied_date: "Q3-Q4 FY27", ref: "L414-415", status_word: "underway"}
  - {commitment: "No auction loss on principal or interest (ASR-garbled L420)", implied_date: "standing", ref: "L420-424", status_word: "underway"}
  - {commitment: "ST LAP Q3 best disbursal of 8-9 quarters, yield above Q2", implied_date: "Dec-26", ref: "L588-591, L611-613", status_word: "initiated"}
  - {commitment: "ST LAP pedal pressed Q3-Q4", implied_date: "H2 FY27", ref: "L460-465, L941-942", status_word: "initiated"}
  - {commitment: "ST LAP ROA rises toward gold ROA", implied_date: "undated", ref: "L851-857", status_word: "initiated"}
  - {commitment: "ST LAP credit-cost stabilisation", implied_date: "done", ref: "L455-458", status_word: "completed"}
  - {commitment: "IGL product live since April", implied_date: "Apr-26", ref: "L268-271", status_word: "completed"}
  - {commitment: "DA ~Rs 700 Cr gold book to de-leverage (filed 876.89); D/E 4.9->4.6", implied_date: "Q2 FY27", ref: "L148-150", status_word: "completed"}
  - {commitment: "Reduce reliance on direct assignment", implied_date: "standing", ref: "L56", status_word: "underway"}
  - {commitment: "Fund growth through internal accruals (ASR 'internal approvals')", implied_date: "standing", ref: "L129", status_word: "underway"}
  - {commitment: "Substitute insurance income when distribution change lands", implied_date: "conditional", ref: "L906-907, L197-199", status_word: "initiated"}
  - {commitment: "Hold gold ROA flat at 20-25% AUM growth via opex leverage", implied_date: "Mar-27", ref: "L893-899", status_word: "underway"}
  - {commitment: "Gold branches extend ST LAP footprint", implied_date: "undated", ref: "L912-920", status_word: "underway"}
  - {commitment: "Absorb rate shock, deliver superior ROA/ROE; handle NIM compression via other levers", implied_date: "H2 FY27", ref: "L686, L661-662", status_word: "initiated"}
  - {commitment: "Medium ticket LAP continues trajectory (ASR_GARBLED)", implied_date: "undated", ref: "L825-826", status_word: "underway"}
  - {commitment: "Entry into eastern India", implied_date: "Q2 FY27", ref: "L69", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "The call reads clean on lagging outcomes and soft on leading variables. Credit cost 0.6%, ROA 2.8%, ROE 17% all tie to filings. Every swing variable for H2 was declined or hedged: gold yield, Stage 2, ST LAP number, C/I 'hopeful', insurance 'whenever'. Three threads join. (1) Collateral: book LTV 68% but working mix 72-74%, IGL to 85%, AUM per tonne +4.8% QoQ on flat gold, no price-down case. (2) Coverage: PCR -299 bps on gold mix; gold PCR 10.5% means every gold Stage 3 step pulls toward 32%; the Pillar 2L 'thins further' wording is met and needs a ruling. (3) Funding: de-leveraging came from a record DA (filed 876.89 vs spoken ~700, 23-month residual on a 'gold' pool), against the stated priority to cut DA reliance. Four spoken-vs-filed drifts plus a 'not revised' guidance claim that differs from the Q1 log feed CREDIBILITY-ND. Most findings sit in SPEAKER_INFERRED turns; the CFO prepared remarks (T05, explicit) carry FN-03, FN-07, FN-08, FN-12."
```
