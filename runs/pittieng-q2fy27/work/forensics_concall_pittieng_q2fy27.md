# A3 FORENSIC NOTES: concall, PITTIENG Q2 FY27

Agent: A3 forensic notes (claude-opus-5-5). Run date: 2026-10-23.
Doctype: concall (machine ASR of a third-party YouTube upload; NOT company-filed).
Inputs read: A1 structured (runs/pittieng-q2fy27/extracted/pittieng-concall-q2fy27-structured.md, R001-R589, all rows), A1 fulltext (runs/pittieng-q2fy27/extracted/pittieng-concall-q2fy27-fulltext.md, L1-L769, all lines), A2 ledger (runs/pittieng-q2fy27/work/ledger_concall_pittieng_q2fy27.md), Notion context (runs/pittieng-q2fy27/work/notion-context.md, memory only), cross-document filed sources (results fulltext L170-L449; presentation fulltext L118-L277, L428-L467), review STEP 8.5 (Q1-Q32).
Nothing under inputs/ was opened. Prior-quarter concall fulltext: NOT PASSED. Status transitions against the Q1 call rest on analyst recall inside this call only.

Citation convention: bare "L###" = concall fulltext line. "results:L###" and "presentation:L###" = the filed sources. Filed sources win on numbers. Spoken numbers are never corrected; conflicts are recorded both ways. [derived] = arithmetic by this agent on cited inputs. [INFERENCE] = reasoning, not evidence.

## SOURCE CAVEATS CARRIED
- Coverage gap: the recording starts mid-Q&A (L30). Opening remarks are missing. Every silence finding is "silent in the recorded portion" and may be a coverage artifact.
- Speaker labels are INFERRED (A1). Analysts address management as "Akshay" (L173, L180). That matches the MD&CEO name Akshay S Pitti (results:L406) [INFERENCE]. MGMT_ABSENCE stays UNTESTABLE for other officers.
- ASR flags carried: 161700 tons (L413), 3,198 vs 3,086 (L543, L712), 2185 vs 2124 (L60-L61), capex 250 vs 450 (L344), 6 vs 2 hours per ton (L591, L601), "nine or percent" (L396), "850 or crores" (L288).

## LEDGER RECONCILIATION
- Ledger rows: 589 (R001-R589). Rows read in the structured file at their ID: 589. Fulltext lines read at cited line: all 769 lines. Reconciled: 589 / 589 = 100%.
- A2 count test (589 ids, 0 orphans) confirmed. Every turn, question, number, forward, entity, date and qualifier row was checked at its cited line.
- A1 data-quality notes (no effect on findings): R135 span "L706-L705" is reversed, and R135/R136 share L706. R134 (L705, MANAGEMENT) opens with analyst words "20612 or 21612?" and is not flagged MIXED. R099/R109 ("Yes, I am audible") are labelled MODERATOR, UNCERTAIN.
- zero_standing rows: 0 (F1 N.A.).

## FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3C-01 | F6 | R165, R236, R237, R440, R441 | L132-L136 | "Yeah, it is here to sustain." / "work more on the trade table side than leverage our cash positions to buy material going forward as we are going into a capex cycle over the next four years" | FORWARD-SIGNAL | Supplier credit is now a stated funding source for the 4-year capex cycle. Filed payables rose Rs 243.27 Cr to Rs 474.79 Cr (results:L273-L274) and carried the Rs 164.84 Cr H1 working-capital release (results:L304). If the Rs 231.52 Cr rise is LC acceptances, net debt is about Rs 770 Cr, not Rs 538.68 Cr [derived: results:L262, L270, L248, L249, L246]. The LC split was not asked (Q1 open). |
| A3C-02 | F14 | R376-R380, R588, R204 | L742-L748 | "We didn't do 250 crores in each one. We capitalized 100 crores in each one." / "So about 140 crores would have been the cash outflow on Kpex." | AMBIGUOUS | Filed H1 purchase of PPE incl. CWIP and capital advances is Rs 256.83 Cr (results:L310). The spoken figure is Rs 116.83 Cr lower [derived]. The analyst's "250" was close to the filing; management corrected it downward. Either management excludes capital advances (other non-current assets +Rs 70.22 Cr, results:L241) and CWIP (+Rs 70.51 Cr, results:L234) from "capex", or the spoken number is wrong. H1 FCF reads differ by about Rs 117 Cr. |
| A3C-03 | F6 | R161, R200-R202, R205, R210-R215, R367, R371, R381, R435, R543, R586 | L61; L726; L751 | "So your 17,000 number is after you add both of these, the target." / "17,000 tons will be the casting produced to make those sales." / "I need to pull that out. I don't like I said it's not there on this table here." | AMBIGUOUS | The FY27 castings guide changed basis three times in one call: sales (L57-L58), sales plus castings into lamination assemblies (L59-L61), then castings produced (L721-L728). No H1 number on the final basis was given. On the filed sales basis H1 is 6,054 MT (presentation:L195); H2 needs 10,946 MT, or 5,473 MT a quarter, +77% on Q2's 3,086 MT [derived]. On the L61 basis H1 is about 8,078-8,239 MT and H2 needs only +6-8% [derived; presentation:L190, positional]. Lean bear: the guide is not testable on any published series until the promised production numbers appear (A3C-04). Q2 status: EVADED. |
| A3C-04 | F16 | R489, R490, R568, R573, R585, R589 | L752; L558-L561; L423; L706-L710 | "I think for the next call we'll try to simplify this and give the production numbers." / "we need to probably work a little bit on that metric because we are taking the sales and defining the utilization" / "that's why we had stopped giving that metric" | FORWARD-SIGNAL | The call confirms four disclosure changes: EBITDA per tonne dropped (L423); a new "other machined components going into laminations" line added (L706-L710; presentation:L192); castings utilisation is sales-based and will be re-cut (L570-L572, L755-L757); production numbers promised for the Q3 call. The Q3 deck will likely break comparability with tracker row 2 (~4,600 MT/qtr on a sales basis). A4 should require a bridge from old to new basis. |
| A3C-05 | F14 | R191, R330-R333, R363, R576 | L543; L712 | "And out of this 3,198, you know, 1059 would have" / "you are not going to just the 3086 castings and machine components" | AMBIGUOUS | 24,600 MT x 52% / 4 = 3,198 MT [derived; presentation:L156, L163]. The ASR "3,198" matches the utilisation-implied quarterly figure exactly, while sales are 3,086 MT (presentation:L195). H1 53% x 24,600 / 2 = 6,519 MT vs 6,054 MT sold [derived; presentation:L169, L174]. Management says utilisation is "calculated on sale basis" (L570), yet it does not reproduce on sales tonnage. Ask what tonnage the 52% uses. Record both numbers; neither is corrected. |
| A3C-06 | F14 | R159, R206, R207, R536-R538, R581, R499 | L39; L42; L674-L675 | "X loss in the quarter. 4.61 crores." / "this is recorded in other expenses which is above EBITDA. Yes." / "your forex loss, which I mentioned, which is booked in the other expense" | AMBIGUOUS | The deck isolates FX only inside finance cost: Q2 FX gain Rs 1.8 Cr (presentation:L255). A Rs 4.61 Cr FX loss inside other expenses appears in neither the deck nor the filing. Net Q2 FX is about a Rs 2.8 Cr loss [derived]. The Rs 4.61 Cr is about 80 bps of Q2 revenue [derived; results:L187]; reported Q2 EBITDA margin 15.4% (presentation:L248) would be 16.2% ex-FX [derived]. Q1's other-expense FX was not given ("I don't have that number", L40; deferred to SGA, L41). The "one-off" label is the analyst's (L42-L43); management did not confirm it. |
| A3C-07 | F6 | R186, R310, R476 | L454-L455 | "Are we still on track to our previous quarter guidance of 370 crores for the full year?" / "if you look at the current quarter and simply extrapolate this you should be getting there." | AMBIGUOUS | The metric is not named on the call; memory has FY27 EBITDA ~Rs 370 Cr. Q2 x 4 gives Rs 355.6 Cr reported or Rs 365.2 Cr adjusted (presentation:L244, L247) [derived]. Neither reaches 370. On adjusted H1 of Rs 180 Cr (presentation:L209), H2 needs Rs 95 Cr a quarter (+4% on Q2), and management itself flags Q3 as weak (L406, L519). Only an ex-FX extrapolation clears 370 (Rs 383.6 Cr adjusted) [derived]. The guide holds only if the A3C-06 FX loss is one-off. Lean bear. |
| A3C-08 | F6 | R275, R432-R434, R461, R463, R475, R483, R539-R542, R559 | L316; L47; L50-L51; L440 | "your sustainable blended margins should be in the vicinity of 17% plus bit" / "the fuel and power cost is going to be passed on from January onwards" / "from quarter four you should see that margin for the gaining" | FORWARD-SIGNAL | Management says 17%+ is sustainable at Q2 price levels, but Q2 printed 15.8% adjusted / 15.4% reported (presentation:L245, L248). The levers it names are dated: fuel and power reset from January 2027 (annual), consumables (not normally passed through, L47-L48), employee cost absorption (Q2 Rs 49.66 Cr, +8.1% QoQ, +24.9% YoY, results:L194 [derived]). Q4 FY27 is the dated test. A Q4 margin below 16.5% falsifies "sustainable at Q2 prices". |
| A3C-09 | F6 | R162, R169, R216-R224, R255-R264, R436-R438, R452, R453, R544 | L254-L256; L235; L68-L70 | "So you won't be able to recover any in a 27th, but to recover the whole amount you have to defer it and then you'll start recovering again from a 28th? Yes." / "our sales support a recovery of roughly about 35 to 36 crores per annum" | FORWARD-SIGNAL | FY27 carries no Maharashtra incentive; recovery resumes in FY28 at about Rs 40 Cr a year (L248-L249). Filed other income: Q2 FY27 Rs 2.10 Cr vs Q2 FY26 Rs 21.32 Cr; FY26 Rs 40.11 Cr (results:L188). [INFERENCE] FY26 other income was mostly this incentive. That points to Reading B of Q8 (a recurring item paused) for FY27, with a non-operating step back up of about Rs 40 Cr pre-tax in FY28. Role 1 must keep the incentive on the same basis at entry and exit (v3.8 A18). |
| A3C-10 | F14 | R218, R219-R222, R256-R261, R437 | L66; L238; L244 | "we are eligible to receive up to 400 crores of the incentive" / "The investment that was eligible for incentive claim was 400 crores." / "the approval and sanction that we got was for seven years" | AMBIGUOUS | Rs 400 Cr is called the incentive cap at L66 and the eligible investment at L238. The 7-year sanction needs Rs 57.1 Cr a year; the 9-year request needs Rs 44.4 Cr [derived]. Sales support Rs 35-36 Cr (L235), "not more than 40" in the near term (L68-L69). [INFERENCE] Under the 7-year sanction, about Rs 400 Cr less 7 x ~Rs 40 Cr = ~Rs 120 Cr may lapse unless the 9-year extension is granted. Ask for the sanction letter terms. |
| A3C-11 | F6 | R196, R197, R353, R484, R485, R583, R584 | L679-L683; L685-L686 | "this round 70 crores of the approval for the Maharashtra incentive is already done, or it is still in the process?" / "No, it is in the process for disbursement." / "It will help in managing the overall debt level." | FORWARD-SIGNAL | About Rs 70 Cr (the analyst's figure; management repeats "So 70 crores?" at L681 and does not confirm it) of accrued incentive is not yet received in cash. If disbursed, net debt falls about 13% [derived: 70 / 538.68]. No date was given. Bear link [INFERENCE]: the incentive is state-tax-linked, and the 8-Oct-2026 SGST Section 67 search at the Maharashtra unit (Notion memory) was not discussed (A3C-27). Ask for the receivable amount on the balance sheet and the disbursement date. |
| A3C-12 | F14 | R166, R189, R444-R446, R459, R479, R553 | L159-L161; L162-L163; L167-L168; L302; L499-L500 | "we should be able to fund it entirely with the internal accruals" / "we have put a point out there that we are going to fund it through a mix of both" / "So, then we will have to depend to probably debt" | AMBIGUOUS | The funding statement flips within the call. The filing says "Internal accruals and Debt" (results:L447). In H1, pre-WC operating cash after tax was about Rs 158.2 Cr (results:L303, L306) [derived] against Rs 256.83 Cr capex (results:L310). Internal accruals did not cover H1 capex; payables did (A3C-01). "Internal accruals" depends on payables staying at the higher level. |
| A3C-13 | F6 | R166, R176-R178, R189, R238-R244, R283-R297, R313-R323, R441-R443, R455, R464-R466, R579 | L153-L156; L356; L361-L362; L483-L484; L490-L493 | "something like 150 crores in the first year which would be FY28 and then towards FY29, 30 and 31" / "the first year would be something like 300 or 250 to 300" / "if you take the start date as first of July, I would say that in 18 months you could see more than 90% of it being expended" / "the board has just approved 450 instead of 400" | FORWARD-SIGNAL | Analyst recall of the Q1 call: Rs 400 Cr Bangalore capex for FY28-FY29 (L483-L484). Now Rs 450 Cr, phased to FY31 (L493; results:L441, L445). The window grew by 2 years and the cost by 12.5% [derived]. Committed Rs 250-260 Cr land and building (L348, L496) should be over 90% spent by about Dec-2027 if the start is 1-Jul-2026 [INFERENCE: year not stated]. Split as heard: 125 + 325 (analyst, L140-L141) vs 125 capacity + 125 consolidation (L219). Rs 200 Cr is not explained. The "250" at L344 conflicts with 450 (ASR; filing wins). |
| A3C-14 | F6 | R182, R203, R305, R373-R375, R471-R474, R488, R525, R526, R587 | L734; L738; L404; L407-L408 | "You would be about 2350 to 2350 to 2400 crores." / "That would be closer to 23, not 2350 to 2400. That would be based on Q3 pricing." / "FY 27 I think we'll still hold on to the upgraded guidance given last quarter." | FORWARD-SIGNAL | The FY27 revenue implied is Rs 2,350-2,400 Cr at Q3 pricing, or about Rs 2,300 Cr at Q2 pricing. H1 was Rs 1,107.53 Cr (results:L187), so H2 must be Rs 1,242-1,292 Cr: +7.4% to +11.7% on Q2 x 2 [derived]. The rise over memory's ~Rs 2,300 Cr comes from price (steel pass-through), not volume. FY28 memory guide of Rs 2,500 Cr implies only +4-6% growth against "a stronger volume growth" (L408) [derived]. The FY28 number is stale or unrestated; no FY28 figure was given. |
| A3C-15 | F14 | R190, R324-R329, R356-R362, R480, R481, R572 | L515-L516; L705 | "H1 numbers is about 40,889 tons. So if I just double this, you're at 82,000 tons." / "It is against the 21671." | AMBIGUOUS | 40,889 MT is Total Laminations (presentation:L191). 21,671 MT is Total Lamination & Assemblies, which includes the 1,059 MT of machined components (presentation:L193). Management doubled the first basis and then named the second. On the 21,671 basis H1 is about 42,900-43,100 MT (presentation:L190, positional) [derived], which gives headroom; on the 40,889 basis the target has zero slack, and Q3 is flagged to dip (L519). The analyst's Q1 figure of 19,200 MT (L509) does not reproduce: restated Q1 laminations are 20,277 MT [derived: presentation:L191]. |
| A3C-16 | F14 | R184, R194, R308, R348, R568, R569 | L416; L629-L630; L423 | "thing that's seen a 10% decline over the Q1 quarter" / "it is one of the lowest in the last six to seven quarters, EBITDA per ton" | NEUTRAL-FACT | The analysts' premise does not reproduce on restated figures. Q1 reported EBITDA Rs 86.36 Cr over about 21,300 MT is about Rs 40.5k/t; Q2 Rs 88.87 Cr over 21,671 MT is about Rs 41.0k/t (results:L187-L197; presentation:L193) [derived]. It is flat to slightly up. The "decline" likely rests on pre-merger Q1 bases. Do not carry "10% decline" into the tracker. Management did not dispute it and explained it by mix, FX and employee cost (L673-L677). |
| A3C-17 | F6 | R193, R349-R352, R421, R482, R580 | L656-L659; L653-L655 | "Out of 580 crores of revenue, about 27% is about 156 crores for traction motor and railway-related components. If you see last year, it's about 32%." | AMBIGUOUS | This ties to the deck: Q2 FY26 32%, Q2 FY27 27%; H1 34% to 27% (presentation:L437, L447). Traction and railway revenue: Q2 about Rs 156 Cr vs Rs 152.9 Cr (+2%); H1 about Rs 299 Cr vs Rs 317.7 Cr (-6%) [derived, shares rounded]. The company grew 21% YoY. Export railway was not split, so tracker row 3 (Rs 135-139 Cr plateau vs Wabtec) cannot be read. Q12 open. |
| A3C-18 | F6 | R187, R188, R477, R570, R571 | L460; L471 | "overall exports will remain stable or slightly downward as a percentage of overall sales" / "We cannot actually quantify what are our deemed exports" | CONFIRMATORY-NEGATIVE | Management walks back the deck claim "Increasing share of exports" (presentation:L515; review M2). Filed outside-India revenue was 26.3% of H1 (results:L394-L396) [derived]. The export-share driver of the developed-market thesis is now guided flat-to-down by management itself. The case moves to "deemed exports", which cannot be quantified. |
| A3C-19 | F6 | R179, R298, R467, R513 | L372-L374 | "being half year end, we are not able to dispatch many of the products. So there is a little bit of an overhang from last quarter in terms of inventory of finished goods which will get liquidated in this quarter." | FORWARD-SIGNAL | Filed inventory change was -Rs 38.13 Cr in Q2 and -Rs 38.10 Cr in Q1 (results:L193). The build ran equally in both quarters, so it is not only a half-year-end effect. Inventory rose Rs 394.91 Cr to Rs 478.70 Cr (results:L244). The dated test: Q3 FY27 must show an inventory release (positive change line). |
| A3C-20 | F6 | R179, R195, R298, R416 | L374-L377 | "the high value added SMBs volume has significantly jumped in this quarter and that also yields into a lower utilization of the side splits. So if we are not able to use those side splits, we prefer to liquidate them." | AMBIGUOUS | This answers Q15 as a yield effect driven by mix plus higher production. By-products and scrap +68.7% to 21,081 MT (presentation:L197); high value-added assemblies 4,786 vs 3,168 MT, +51.1% (presentation:L184-L186, positional). If scrap scales with high value-added mix, part of the mix margin gain is lost as scrap realisation. That partly matches the bear reading of Q15. Ask for scrap realisation per tonne vs steel cost. |
| A3C-21 | F6 | R247-R249, R272, R273, R448, R449, R454, R460, R555 | L205-L207; L307; L263 | "we will actually have to go to a fifth and a sixth lease facility before we can move into our own facility" / "In Bangalore there won't be any incentive available." | FORWARD-SIGNAL | Bangalore goes from 3 leased premises to 5-6 before the owned site, which is due about Dec-2027 (A3C-13). Lease liabilities (debt-like) were Rs 113.92 Cr at Sep-26 (results:L263, L271) [derived]. They will rise before consolidation. No state incentive offsets the Bangalore build. |
| A3C-22 | F6 | R192, R339-R345, R575 | L596; L591; L601 | "And 172,000 hours were utilized to get that machining done." / "about 6 hours per ton of machine output" / "it's two hours per ton, roughly." | FORWARD-SIGNAL | 172,000 hours is 84.6% of quarterly machining capacity (8,13,600 / 4; presentation:L149), which ties to the deck's 85% (presentation:L157) [derived]. 172,000 / 3,000 MT = 57 hours per tonne [derived]; neither spoken figure (6 or 2) ties. [INFERENCE] At 85% machining use, about 15% headroom allows roughly 3,500 MT a quarter of machined output until hours rise to 10,80,000 by Q1 FY30 (results:L425). A sales-basis 5,473 MT quarter (A3C-03) would then need about 2,000 MT of raw castings a quarter, against about 1,000 MT today (L553). This supports the bear reading that the redefinition at L726 replaces a sales target the machining shop cannot carry. |
| A3C-23 | F7 | R181, R199, R304, R450, R451, R457, R464, R469, R487, R566, R567 | L392; L395-L396; L695-L697; L225; L293; L348 | "we are looking at it cautiously optimistic on data center" / "I would not look at it you know increasing more than probably nine or percent" / "Potentially it can grow very, very fast, even faster than the others" / "we are exploring to get it outsourced" / "we are not committing to expand anything today" | AMBIGUOUS | Optionality is hedged both ways. Data centres are capped at about 9% (ASR uncertain) and also called potentially the fastest. Copper winding is "exploring" outsourcing only. "Not committing" (L293) sits against "250 to 260 would be kind of a committed KPEX" (L348). The Caterpillar data-centre housing start (Q3 FY27 in memory) was not named. Treat the data-centre slice as unquantified. |
| A3C-24 | F7 | R472, R481, R557, R564, R572 | L406; L519; L357-L358; L287; L691 | "Execution will be a challenge for the three" / "Quarter three volumes might dip a little bit on lamination owing to the festivals." / "It's all going to depend on what demand comes in" / "Assuming that it's full utilization by FY 31" | FORWARD-SIGNAL | Q3 FY27 softness is pre-announced (Diwali and Christmas, L406). Combined with A3C-07 and A3C-15, a soft Q3 leaves the FY27 EBITDA and lamination guides with no slack into Q4. The Rs 3,800 Cr FY31 figure is conditional on full utilisation (L287). |
| A3C-25 | F14 | R267, R268, R279, R456, R462 | L287-L289; L323 | "revenue potential of approximately 3,800 crores as a company of which around 850 or crores would come from machine components" / "lamination would do closer to 2000 crores revenue on a standalone basis" | AMBIGUOUS | Rs 850 Cr + Rs 2,000 Cr = Rs 2,850 Cr, leaving about Rs 950 Cr of the Rs 3,800 Cr FY31 potential unallocated [derived]. "850 or" is ASR-uncertain. Machine components are said to earn about 25% EBITDA margin (L326, ASR term). Ask for the FY31 split by line. |
| A3C-26 | F14 | see register below | L127-L128; L413; L423; L60-L61; L344; L482 | "increase to 470 crores from 236" / "Machine components about 161700 tons" / "low value added assemblies are almost 15500 tons" | NEUTRAL-FACT | Minor spoken-vs-filed conflicts are logged in the SPOKEN VS FILED REGISTER below. The "236" is Mar-26 "dues to others" (Rs 236.09 Cr), not total payables (Rs 243.27 Cr) (results:L273-L274). Loose lamination 15,500 MT vs 14,476 MT filed (presentation:L190, positional). Individually immaterial; together they show that the call figures need a filed anchor before use. |
| A3C-27 | F17 | R533, R534 (coverage); R485 | L30; L686; L763 | "COVERAGE GAP: the upload begins mid-Q&A" / "It will help in managing the overall debt level." / "improving, working capital" | AMBIGUOUS | Twenty memory and checklist items were not discussed in the recorded portion (WHAT WAS NOT DISCUSSED table). The most material: the net-debt number, LC acceptances, lien-marked deposits, the SGST search, the tax rate, goodwill, export railway, Section 232, and numeric FY28 guidance. Coverage gap: the opening remarks may have covered some. Silence count is 1 quarter (prior transcripts ND). It is not yet a "sustained" confirmatory negative. |
| A3C-28 | F17 | R189, R317, R191, R330-R333, R363 | L488; L536-L540; L569 | "how will it be funded given the total borrowings currently stand at 640 crores?" / "that would be closer to 4,900 tons of casting produced" | AMBIGUOUS | Tier-1 tracker rows read against the call. Row 1: filed net debt Rs 538.68 Cr [derived: results:L262, L270, L248, L249, L246] is above the Rs 491 Cr Q1 mark (basis comparability not verified). Management gave no net-debt number; borrowings of Rs 640 Cr went unchallenged (ties Rs 640.43 Cr). Row 2: 3,086 MT sold (presentation:L195) is well under ~4,600 MT, so the falsifier fires on the sales basis. Management offered a production-equivalent ~4,900 MT (L569) on a basis with no history. Row 3: unreadable (A3C-17). Lean bear on rows 1 and 2. |

## CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 Zero-value standing items | N.A. | Concall has no financial tables; ledger zero_standing = 0. |
| F2 Standalone vs consolidated | N.A. | No S-vs-C data on a call; company has no subsidiaries post-merger (results:L353). |
| F3 Shell-entity detection | N.A. | No cost-line tables on a call. |
| F4 Unaudited contribution ratio | N.A. | No auditor Other Matters on a call. |
| F5 Going concern / EoM scope | N.A. | No EoM paragraph on a call. |
| F6 Forward-commitment mining | FINDING | 30 commitments registered; A3C-01, 03, 07-09, 11, 13, 14, 17-22. |
| F7 Hedge phrase mining | FINDING | Hedge clusters on optionality and on Q3 (A3C-23, A3C-24). |
| F8 Tax forensics | N.A. | Tax not discussed on the call; the silence is logged in F17 (Q14 unasked). |
| F9 OCI forensics | N.A. | No OCI data on a call. |
| F10 Share count / dilution | N.A. | No share-count data on the call; ESOP silence logged in F17. |
| F11 Reserves / net worth tie-out | N.A. | No equity figures on the call. |
| F12 Segment forensics | N.A. | Single reported segment; end-market shares only, handled in F6 (A3C-17). |
| F13 Board outcome | N.A. | Board outcomes sit in the results filing; the call's board reference (L490) is handled in F6 (A3C-13). |
| F14 Drafting inconsistencies (applied to spoken vs filed and intra-call conflicts) | FINDING | A3C-02, 05, 06, 10, 12, 15, 16, 25, 26. |
| F15 Entity list diffs | N.A. | No consolidation list on a call. |
| F16 Dropped and reframed disclosures | FINDING | The call confirms the dropped EBITDA/t metric, a new line item, and a coming castings-metric re-basis (A3C-04). |
| F17 Silence audit | FINDING | A3C-27, A3C-28; table below. |

Totals: PASS 0, FINDING 5, N.A. 12. Blank: none.

## COMMITMENT REGISTER (F6)

| # | commitment | implied date | ref | status word |
|---|---|---|---|---|
| C01 | Fuel and power cost passed on (annual reset) | from Jan-2027 | L47, L51 | initiated |
| C02 | Fuel/power margin pressure "coming back" | Q4 FY27 | L50-L51 | initiated |
| C03 | Steel inflation passed through quarterly per contract | ongoing | L51-L53 | underway |
| C04 | Employee-cost absorption; margin gain | from Q4 FY27 | L437-L440, L675-L677 | initiated |
| C05 | Sustainable blended margin 17%+ at Q2 prices; 17% comfortable, 18% potential | ongoing / FY31 | L316, L330-L331 | stated |
| C06 | Maharashtra incentive: nil FY27; recovery restarts FY28 at ~Rs 40 Cr/yr | FY28 | L248-L249, L254-L256 | deferred |
| C07 | Seek 9-year recovery period (sanction is 7) | not dated | L71-L72, L246-L247 | in process |
| C08 | Maharashtra receivable (~Rs 70 Cr, analyst figure) disbursement | not dated | L683 | in process |
| C09 | Trade payables level "here to sustain" through capex cycle | 4 years | L132-L136 | underway |
| C10 | Rs 450 Cr capex: ~Rs 150 Cr FY28, rest FY29-FY31 | FY28-FY31 | L153-L156 | board approved |
| C11 | Whole Rs 740 Cr programme done | by FY31 | L285, L493 | underway |
| C12 | Committed Rs 250-260 Cr land and building (Hyderabad, Bangalore) | >90% within 18 months of 1-Jul [year INFERRED 2026] | L348, L361-L362, L496 | underway |
| C13 | First-year capex Rs 250-300 Cr; then Rs 100/125/150 Cr a year | FY27-FY28 onward | L355-L357 | stated |
| C14 | Funding: internal accruals; debt if demand comes faster | FY27-FY31 | L159-L168, L499-L502 | stated (inconsistent) |
| C15 | Bangalore: 5th and 6th lease sites, then one owned site | before own site | L205-L207, L308 | stated |
| C16 | Aurangabad remains the largest lamination facility | post-capex | L189-L191 | stated |
| C17 | Copper winding: explore outsourcing first | not dated | L225-L230 | exploring |
| C18 | FY27 volume guidance held: 82,000 MT laminations | FY27 | L404, L515-L523 | reaffirmed |
| C19 | FY27 castings 17,000 MT (basis: castings produced) | FY27 | L61, L726 | reaffirmed (re-based) |
| C20 | Q3 lamination dip; Q4 similar to or slightly above Q2 | Q3-Q4 FY27 | L406, L517-L520 | guided |
| C21 | Strong FY28 volume growth; modular capacity adds from Q4 | FY28 | L407-L408 | guided (no number) |
| C22 | FY27 EBITDA ~Rs 370 Cr on track | FY27 | L455 | reaffirmed |
| C23 | FY27 revenue Rs 2,350-2,400 Cr at Q3 pricing if targets met | FY27 | L734-L739 | guided |
| C24 | Finished-goods overhang liquidated | Q3 FY27 | L373-L374 | promised |
| C25 | Production numbers and cleaned-up utilisation (incl. foundry) | next call (Q3 FY27) | L752-L757 | promised |
| C26 | Q1 FX number to be provided via IR (SGA) | post-call | L40-L41 | promised |
| C27 | FY31 revenue potential ~Rs 3,800 Cr at full utilisation | FY31 | L287-L288 | conditional |
| C28 | Exports grow but share stable to slightly down | 3-4 years | L460-L461 | guided |
| C29 | Top 5-7 customer groups remain the major revenue source | ongoing | L382-L383 | stated |
| C30 | Closing focus: working capital, completing ongoing capex, scaling machine components | FY27 | L763 | stated |

## SPOKEN VS FILED REGISTER (F14 support for A3C-26 and others)

| item | spoken (line) | filed / derived | status |
|---|---|---|---|
| Trade payables | "470 crores from 236" (L127-L128) | Rs 474.79 / 243.27 Cr total; Rs 466.91 / 236.09 Cr dues to others (results:L273-L274) | Basis mixed; 236 = Mar-26 dues to others |
| Borrowings | "640 crores" (L488, analyst) | Rs 640.43 Cr (results:L262, L270) | Ties |
| Q2 revenue | "580 crores" (L656) | Rs 578.44 Cr (results:L187) | Ties (rounded) |
| Gross margin move | "60 bits" (L85) | 39.4% to 38.8% YoY (presentation:L218); QoQ -57 bps [derived] | Ties |
| EBITDA margin move | "hundred bits" (L83) | Adjusted 16.8% to 15.8% YoY (presentation:L218); reported QoQ -96 bps [derived] | Ties |
| New capex | "250" (L344) vs "450" (L139, L153, L490) | Rs 450 Cr (results:L445) | ASR; filing wins |
| Hyderabad programme | "2.90 crore" (L482) | Rs 290 Cr (presentation:L126) | ASR |
| Other machined comps (H1) | "2185" then "2124" (L60-L61) | 2,185 and 2,024 appear at presentation:L190 (column position ambiguous) | 2,124 not in deck |
| Machine components Q2 | "161700 tons" (L413) | Total castings and machined 3,086 MT (presentation:L195) | Implausible; ASR |
| Raw castings Q2 | "1000 tons" (L413, L553, L715) | Not split in deck | Spoken only |
| Loose lamination Q2 | "almost 15500 tons" (L423) | 14,476 MT (presentation:L190, positional) | Conflict ~1,024 MT |
| Laminations H1 | "40,889 tons" (L515) | 40,889 MT (presentation:L191) | Ties |
| Q2 lamination lines | "20612", "1059", "21671" (L703-L705) | presentation:L191-L193 | Ties |
| Castings Q2 | "3,198" (L543) vs "3086" (L712) | 3,086 MT (presentation:L195); 3,198 = 24,600 x 52% / 4 [derived] | See A3C-05 |
| Sheet metal capacity | "108,000 to 160,000", "52,000" (L215-L216) | results:L422, L436; presentation:L130 | Ties |
| Castings capacity, utilisation | "24,600", "52%" (L539-L540, analyst) | presentation:L156, L163 | Ties |
| Machining hours used | "172,000 hours" (L596) | 84.6% of 8,13,600 / 4 vs deck 85% (presentation:L149, L157) [derived] | Ties |
| Hours per tonne | "6 hours" (L591) vs "two hours" (L601) | 57 h/t [derived] | Neither ties |
| Traction and railway share | "27%", "32%" (L656-L659) | presentation:L437 | Ties |
| Programme total | "740, 290 plus 450" (L495) | presentation:L125-L126 | Ties |
| Q1 lamination + assemblies | "19,200 tons" (L509, analyst) | Q1 laminations 20,277 MT restated [derived] | Not reproduced |
| FX in other expenses | "4.61 crores" (L39) | Not disclosed; deck FX in finance cost -1.8 (presentation:L255) | See A3C-06 |
| H1 capex cash | "about 140 crores" (L748) | Rs 256.83 Cr (results:L310) | See A3C-02 |
| High value-added assemblies | "significantly jumped" (L375) | 4,786 vs 3,168 MT, +51.1% (presentation:L184-L186, positional) | Ties |
| By-products and scrap | "more than 60%" (L368, analyst) | +68.7% (presentation:L197) | Ties |

## WHAT WAS NOT DISCUSSED (F17 silence audit)

Consecutive-quarter silence count: 1 (this call). Prior-quarter transcripts were not passed, so earlier counts are ND. All entries are "silent in the recorded portion"; the opening remarks are missing (L30).

| # | checklist / commitment item (source) | discussed? | consecutive quarters silent | note |
|---|---|---|---|---|
| S01 | Tracker row 1: net debt vs Rs 491 Cr (Notion) | No number given | 1 | Filed Rs 538.68 Cr [derived]; only "managing the overall debt level" (L686) |
| S02 | Rs 300 Cr net-debt target / Rs 125 Cr WC release (Spear facts) | No | 1 | "improving, working capital" in closing only (L763) |
| S03 | LC acceptances / buyer's credit inside payables (Q1; pending operator ruling) | No | 1 | Payables "here to sustain" (L132) |
| S04 | Lien-marked deposits, Rs 42.65 Cr other bank balances (Q32) | No | 1 | results:L249 |
| S05 | Tracker row 2: castings vs ~4,600 MT/qtr | Re-based, no comparable number | 1 | A3C-03, A3C-28 |
| S06 | Tracker row 3: export railway vs Wabtec plateau | No | 1 | Only total traction + railway (L656-L657) |
| S07 | SGST Section 67 search, 8-Oct-2026, Maharashtra unit (Notion) | No | 1 | Link to the Maharashtra incentive [INFERENCE] |
| S08 | Tax rate guide 33% to 25%; H1 ETR (Q14) | No | 1 | |
| S09 | Goodwill Rs 136.1 Cr gone in restatement (Q4) | No | 1 | |
| S10 | Ratio basis FY26 ROE/ROA/D-E (Q5) | No | 1 | |
| S11 | Section 232 US petition, HTS 8503.00.65 (Notion) | No | 1 | |
| S12 | Caterpillar data-centre housings, commercial start Q3 FY27 (Notion) | Not named | 1 | Data centre discussed only generically (L392-L398) |
| S13 | FY28 numeric guide: Rs 2,500 Cr, 90,000 MT, 17-17.2% (Spear) | No number | 1 | "stronger volume growth" only (L408) |
| S14 | Castings 36,000 MT by Q1 FY29 date (Spear; Q10) | Programme end FY31 only | 1 | L285, L493 |
| S15 | Rs 300 Cr inventory target (Notion) | No | 1 | FG overhang only (L372-L374) |
| S16 | ESOP grant 2, options outstanding, dilution (Q20-Q23) | No | 1 | |
| S17 | Amalgamation costs, post-merger line disclosure, restatement auditor (Q17, Q18, Q26) | No | 1 | Only "before the foundation was merged in" (L755) |
| S18 | Capitalised borrowing cost on CWIP (Q9) | No | 1 | |
| S19 | Deputy CEO and board composition (Q27, Q28) | No | 1 | |
| S20 | Interim dividend cash out (Notion) | No | 1 | results:L340 |

Items addressed (not silent): margins and pass-through (L33-L123), payables sustainability (L126-L136), capex size, phasing and funding (L138-L168, L339-L362, L481-L502), Maharashtra incentive (L62-L73, L232-L256, L678-L686), lamination and castings volume guides (L53-L62, L504-L526, L700-L757), scrap (L368-L377), customer concentration (L378-L388), data centres (L389-L398, L694-L697), exports (L456-L474), traction (L613-L662), EBITDA guide (L454-L455), FY27 revenue (L730-L739), H1 capex (L741-L748).

## STEP 8.5 QUESTIONS Q1-Q32: CALL OUTCOME

Status key: ANSWERED = answered with a usable figure or reason. PARTIAL = topic addressed, the asked figure not given. EVADED = asked on the call, not answered or deferred. UNASKED = not raised in the recorded portion.

| Q | topic | status | cite | note |
|---|---|---|---|---|
| Q1 | LC acceptances in Rs 474.8 Cr payables | PARTIAL | L126-L136 | Sustainability confirmed; LC split not asked or given |
| Q2 | Q3 FY27 castings tonnage | EVADED | L53-L62, L749-L751 | Re-based; "I need to pull that out" |
| Q3 | Q1 castings restated (2,968 vs 3,191) | UNASKED | - | ASR "3,198" (L543) is near 3,191; unresolved |
| Q4 | Goodwill reserve entry | UNASKED | - | |
| Q5 | FY26 ratio equity base | UNASKED | - | |
| Q6 | Peak net debt in Rs 740 Cr programme | PARTIAL | L488-L502 | Funding mix given; no peak figure |
| Q7 | Rs 290 Cr programme spent by 30-Sep | PARTIAL | L741-L748 | H1 ~Rs 140 Cr spoken vs Rs 256.83 Cr filed (A3C-02) |
| Q8 | Other income source by item | PARTIAL | L254-L256, L678-L683 | Maharashtra incentive named by analyst; deferral confirmed; amounts not given |
| Q9 | Capitalised borrowing cost | UNASKED | - | |
| Q10 | Castings 36,000 MT date | PARTIAL | L285, L493 | Programme end FY31; castings-specific date not given |
| Q11 | 10,80,000 machining hours: level or addition | UNASKED | - | 172,000 hours used in Q2 (L596) |
| Q12 | Export railway revenue Q2 | PARTIAL | L656-L657 | Total traction + railway only |
| Q13 | Export receivables factored | UNASKED | - | |
| Q14 | H2 FY27 ETR | UNASKED | - | |
| Q15 | Scrap +68.7% cause | ANSWERED | L371-L377 | Higher production plus side-split yield from high value-added mix (A3C-20) |
| Q16 | Lease principal sign in cash flow | UNASKED | - | |
| Q17 | Post-merger line disclosure (castings, Karnataka laminations) | UNASKED | - | |
| Q18 | Restatement auditor for PIPL/DFPL | UNASKED | - | |
| Q19 | Chaitra Sundaresh link / earn-out | UNASKED | - | |
| Q20 | ESOP grant-1 date | UNASKED | - | |
| Q21 | Options outstanding; grant-2 sourcing | UNASKED | - | |
| Q22 | Grant-1 market price | UNASKED | - | |
| Q23 | ESOP add-back gross or net | UNASKED | - | |
| Q24 | Reported PAT on FY charts | UNASKED | - | |
| Q25 | SGST search outcome | UNASKED | - | |
| Q26 | Amalgamation costs | UNASKED | - | |
| Q27 | Deputy CEO remit | UNASKED | - | |
| Q28 | Y B Sahgal executive history | UNASKED | - | |
| Q29 | Actuarial assumption change | UNASKED | - | |
| Q30 | FY23 regrouping | UNASKED | - | |
| Q31 | Share of 3,086 MT cast in-house | PARTIAL | L727, L569 | "some part ... produced in our own company"; no share |
| Q32 | Lien-marked deposits | UNASKED | - | |

Count: ANSWERED 1, PARTIAL 7, EVADED 1, UNASKED 23 (total 32). The top-3 live questions: Q1 PARTIAL, Q2 EVADED, Q4 UNASKED. All three stay open for the written IR route (Strategic Growth Advisors).

New questions this call raises for A4: the A3C-02 capex gap (Rs 140 Cr vs Rs 256.83 Cr); the Rs 4.61 Cr FX loss in other expenses and Q1's equivalent (A3C-06); which EBITDA definition the Rs 370 Cr is (A3C-07); the incentive sanction terms and the Rs 70 Cr receivable date (A3C-10, A3C-11); the 82,000 MT basis (A3C-15); the FY31 Rs 950 Cr gap (A3C-25); the tonnage behind the 52% utilisation (A3C-05); restated FY28 guidance (A3C-14).

```yaml
stage: A3-forensics
company: "PITTIENG"
quarter: "q2fy27"
doctype: "concall"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/pittieng-q2fy27/work/forensics_concall_pittieng_q2fy27.md"
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
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "A3C-01", check: "F6", line: "L132-L136", classification: "FORWARD-SIGNAL", implication: "Payables named as capex-cycle funding; filed payables 243.27 to 474.79 Cr (results:L273-L274); if LC-backed, net debt ~770 Cr not 538.68 Cr"}
  - {id: "A3C-02", check: "F14", line: "L742-L748", classification: "AMBIGUOUS", implication: "Spoken H1 capex cash ~140 Cr vs filed 256.83 Cr (results:L310); FCF read differs by ~117 Cr"}
  - {id: "A3C-03", check: "F6", line: "L61; L726; L751", classification: "AMBIGUOUS", implication: "17,000 MT castings guide re-based three times; sales basis needs 5,473 MT/qtr in H2 vs Q2 3,086 (presentation:L195); untestable until production data"}
  - {id: "A3C-04", check: "F16", line: "L752; L558-L561; L423; L706-L710", classification: "FORWARD-SIGNAL", implication: "EBITDA/t dropped, new line added, castings utilisation to be re-cut, production numbers promised next call; tracker row 2 comparability breaks"}
  - {id: "A3C-05", check: "F14", line: "L543; L712", classification: "AMBIGUOUS", implication: "3,198 = 24,600 x 52% / 4 [derived] vs 3,086 sold; utilisation does not reproduce on sales tonnage"}
  - {id: "A3C-06", check: "F14", line: "L39; L42; L674-L675", classification: "AMBIGUOUS", implication: "Rs 4.61 Cr FX loss in other expenses not in deck or filing (deck FX gain 1.8 in finance cost, presentation:L255); ~80 bps of Q2 margin; recurrence unconfirmed"}
  - {id: "A3C-07", check: "F6", line: "L454-L455", classification: "AMBIGUOUS", implication: "Rs 370 Cr EBITDA 'simply extrapolate' fails arithmetic: Q2x4 = 355.6 reported / 365.2 adjusted; clears only ex-FX"}
  - {id: "A3C-08", check: "F6", line: "L316; L47; L50-L51; L440", classification: "FORWARD-SIGNAL", implication: "17%+ called sustainable at Q2 prices vs 15.8% printed; dated levers Jan-2027 and Q4 FY27; Q4 is the test"}
  - {id: "A3C-09", check: "F6", line: "L254-L256; L235; L68-L70", classification: "FORWARD-SIGNAL", implication: "Maharashtra incentive nil in FY27, ~Rs 40 Cr/yr from FY28; explains other income collapse (results:L188) [INFERENCE]; non-operating FY28 step"}
  - {id: "A3C-10", check: "F14", line: "L66; L238; L244", classification: "AMBIGUOUS", implication: "Rs 400 Cr is both incentive cap and eligible investment; 7-year sanction needs 57.1 Cr/yr vs 35-40 supportable; ~120 Cr may lapse [INFERENCE]"}
  - {id: "A3C-11", check: "F6", line: "L679-L683; L685-L686", classification: "FORWARD-SIGNAL", implication: "~Rs 70 Cr incentive receivable in process, undated; ~13% net-debt cut if paid; SGST search undiscussed"}
  - {id: "A3C-12", check: "F14", line: "L159-L163; L167-L168; L302; L499-L500", classification: "AMBIGUOUS", implication: "Funding flips between internal accruals and mix with debt; H1 pre-WC cash ~158 Cr vs capex 256.83 Cr; payables filled the gap"}
  - {id: "A3C-13", check: "F6", line: "L153-L156; L356; L361-L362; L483-L484; L490-L493", classification: "FORWARD-SIGNAL", implication: "Bangalore capex 400 Cr FY28-29 became 450 Cr to FY31; committed 250-260 Cr L&B ~90% spent by ~Dec-2027; 125+325 vs 125+125 split unexplained"}
  - {id: "A3C-14", check: "F6", line: "L734; L738; L404; L407-L408", classification: "FORWARD-SIGNAL", implication: "FY27 revenue 2,350-2,400 Cr at Q3 pricing (price-led); FY28 2,500 Cr memory guide implies +4-6% only; FY28 not restated"}
  - {id: "A3C-15", check: "F14", line: "L515-L516; L705", classification: "AMBIGUOUS", implication: "82,000 MT doubled on 40,889 basis but named against 21,671 basis; zero slack on one basis with Q3 dip flagged"}
  - {id: "A3C-16", check: "F14", line: "L416; L629-L630; L423", classification: "NEUTRAL-FACT", implication: "Analyst EBITDA/t 10% decline does not reproduce on restated data (~40.5k to ~41.0k/t) [derived]; do not carry to tracker"}
  - {id: "A3C-17", check: "F6", line: "L656-L659", classification: "AMBIGUOUS", implication: "Traction+railway Q2 ~156 Cr (+2% YoY), H1 ~299 Cr (-6%) [derived]; export railway unsplit; tracker row 3 unreadable"}
  - {id: "A3C-18", check: "F6", line: "L460; L471", classification: "CONFIRMATORY-NEGATIVE", implication: "Management guides export share stable to down, contradicting deck 'Increasing share of exports' (presentation:L515)"}
  - {id: "A3C-19", check: "F6", line: "L372-L374", classification: "FORWARD-SIGNAL", implication: "FG overhang to liquidate in Q3; filed inventory build equal in Q1 and Q2 (-38.10, -38.13 Cr, results:L193); Q3 release is the test"}
  - {id: "A3C-20", check: "F6", line: "L374-L377", classification: "AMBIGUOUS", implication: "Scrap rise = side-split yield from high value-added mix plus production; part of mix gain may leak to scrap"}
  - {id: "A3C-21", check: "F6", line: "L205-L207; L307; L263", classification: "FORWARD-SIGNAL", implication: "Bangalore to 5-6 leased sites before own site; lease liabilities 113.92 Cr will rise; no state incentive"}
  - {id: "A3C-22", check: "F6", line: "L596; L591; L601", classification: "FORWARD-SIGNAL", implication: "172,000 hours = 84.6% machining use [derived] ties deck 85%; ~3,500 MT/qtr machined ceiling to FY30 constrains sales-basis castings target [INFERENCE]"}
  - {id: "A3C-23", check: "F7", line: "L392; L395-L396; L695-L697; L225; L293; L348", classification: "AMBIGUOUS", implication: "Data-centre, copper-winding and capex-commitment statements hedged both ways; Caterpillar DC housing start not named"}
  - {id: "A3C-24", check: "F7", line: "L406; L519; L357-L358; L287", classification: "FORWARD-SIGNAL", implication: "Q3 FY27 softness pre-announced; FY27 EBITDA and lamination guides have no Q4 slack"}
  - {id: "A3C-25", check: "F14", line: "L287-L289; L323", classification: "AMBIGUOUS", implication: "FY31 Rs 3,800 Cr = 850 MC + ~2,000 lamination leaves ~950 Cr unallocated"}
  - {id: "A3C-26", check: "F14", line: "L127-L128; L413; L423; L60-L61; L344; L482", classification: "NEUTRAL-FACT", implication: "Minor ASR and basis conflicts logged in the register; call figures need a filed anchor"}
  - {id: "A3C-27", check: "F17", line: "L30; L686; L763", classification: "AMBIGUOUS", implication: "20 checklist items silent in the recorded portion (net debt, LC, SGST search, tax, goodwill, export railway, FY28 numbers); coverage gap; 1 quarter"}
  - {id: "A3C-28", check: "F17", line: "L488; L536-L540; L569", classification: "AMBIGUOUS", implication: "Tracker row 1 filed 538.68 > 491 with no management number; row 2 falsifier fires on sales basis, management offers production-equivalent 4,900 MT"}
forward_signals: ["A3C-01", "A3C-04", "A3C-08", "A3C-09", "A3C-11", "A3C-13", "A3C-14", "A3C-19", "A3C-21", "A3C-22", "A3C-24"]
ambiguous: ["A3C-02", "A3C-03", "A3C-05", "A3C-06", "A3C-07", "A3C-10", "A3C-12", "A3C-15", "A3C-17", "A3C-20", "A3C-23", "A3C-25", "A3C-27", "A3C-28"]
commitments:
  - {commitment: "Fuel and power cost pass-through (annual reset)", implied_date: "from Jan-2027", ref: "L47, L51", status_word: "initiated"}
  - {commitment: "Fuel/power margin recovery", implied_date: "Q4 FY27", ref: "L50-L51", status_word: "initiated"}
  - {commitment: "Steel inflation passed through quarterly", implied_date: "ongoing", ref: "L51-L53", status_word: "underway"}
  - {commitment: "Employee-cost absorption, margin gain", implied_date: "from Q4 FY27", ref: "L437-L440, L675-L677", status_word: "initiated"}
  - {commitment: "Sustainable blended margin 17%+ at Q2 prices; 18% potential", implied_date: "ongoing / FY31", ref: "L316, L330-L331", status_word: "stated"}
  - {commitment: "Maharashtra incentive nil FY27; ~Rs 40 Cr/yr from FY28", implied_date: "FY28", ref: "L248-L249, L254-L256", status_word: "deferred"}
  - {commitment: "Seek 9-year incentive recovery period", implied_date: "not dated", ref: "L71-L72, L246-L247", status_word: "in process"}
  - {commitment: "Maharashtra receivable (~Rs 70 Cr, analyst figure) disbursement", implied_date: "not dated", ref: "L683", status_word: "in process"}
  - {commitment: "Trade payables level sustained through capex cycle", implied_date: "4 years", ref: "L132-L136", status_word: "underway"}
  - {commitment: "Rs 450 Cr capex ~150 Cr FY28, rest FY29-FY31", implied_date: "FY28-FY31", ref: "L153-L156", status_word: "board approved"}
  - {commitment: "Rs 740 Cr programme complete", implied_date: "FY31", ref: "L285, L493", status_word: "underway"}
  - {commitment: "Committed Rs 250-260 Cr land and building >90% spent in 18 months from 1-Jul", implied_date: "~Dec-2027 [INFERENCE]", ref: "L348, L361-L362, L496", status_word: "underway"}
  - {commitment: "First-year capex Rs 250-300 Cr, then 100/125/150", implied_date: "FY27 onward", ref: "L355-L357", status_word: "stated"}
  - {commitment: "Funding internal accruals; debt if demand faster", implied_date: "FY27-FY31", ref: "L159-L168, L499-L502", status_word: "stated"}
  - {commitment: "Bangalore 5th and 6th lease sites then one owned site", implied_date: "before own site", ref: "L205-L207, L308", status_word: "stated"}
  - {commitment: "Aurangabad remains largest lamination facility", implied_date: "post-capex", ref: "L189-L191", status_word: "stated"}
  - {commitment: "Copper winding via outsourcing first", implied_date: "not dated", ref: "L225-L230", status_word: "exploring"}
  - {commitment: "FY27 laminations 82,000 MT held", implied_date: "FY27", ref: "L404, L515-L523", status_word: "reaffirmed"}
  - {commitment: "FY27 castings 17,000 MT (castings produced basis)", implied_date: "FY27", ref: "L61, L726", status_word: "reaffirmed (re-based)"}
  - {commitment: "Q3 lamination dip; Q4 similar to or above Q2", implied_date: "Q3-Q4 FY27", ref: "L406, L517-L520", status_word: "guided"}
  - {commitment: "Strong FY28 volume growth; modular adds from Q4", implied_date: "FY28", ref: "L407-L408", status_word: "guided"}
  - {commitment: "FY27 EBITDA ~Rs 370 Cr on track", implied_date: "FY27", ref: "L455", status_word: "reaffirmed"}
  - {commitment: "FY27 revenue Rs 2,350-2,400 Cr at Q3 pricing", implied_date: "FY27", ref: "L734-L739", status_word: "guided"}
  - {commitment: "Finished-goods overhang liquidated", implied_date: "Q3 FY27", ref: "L373-L374", status_word: "promised"}
  - {commitment: "Production numbers and cleaned-up utilisation incl. foundry", implied_date: "Q3 FY27 call", ref: "L752-L757", status_word: "promised"}
  - {commitment: "Q1 FX figure via IR (SGA)", implied_date: "post-call", ref: "L40-L41", status_word: "promised"}
  - {commitment: "FY31 revenue potential ~Rs 3,800 Cr at full utilisation", implied_date: "FY31", ref: "L287-L288", status_word: "conditional"}
  - {commitment: "Exports grow; share stable to slightly down", implied_date: "3-4 years", ref: "L460-L461", status_word: "guided"}
  - {commitment: "Top 5-7 customer groups remain major source", implied_date: "ongoing", ref: "L382-L383", status_word: "stated"}
  - {commitment: "Closing focus: working capital, ongoing capex, machine components", implied_date: "FY27", ref: "L763", status_word: "stated"}
gate_a3: pass
blank_checks: []
analyst_note: "ASR transcript, opening remarks missing; silences are coverage-qualified, so none is classed confirmatory-negative yet. The call matters for three reasons. First, management named supplier credit as the funding source for the four-year capex cycle (A3C-01). With H1 pre-WC cash about Rs 158 Cr against Rs 257 Cr filed capex (A3C-12), the LC-acceptance question (Q1) now decides whether net debt is Rs 539 Cr or about Rs 770 Cr. Second, the castings guide was re-based to a production measure with no published series just as tracker row 2 fires on sales tonnage. Machining at 85% caps machined output (A3C-22), so the bear reading is a quiet walk-back, not definitions. Third, other income: the Maharashtra incentive is nil in FY27 and returns at about Rs 40 Cr in FY28. That is a non-operating EPS step Role 1 must keep on one basis. Spoken capex (Rs 140 Cr) and the Rs 4.61 Cr FX loss in other expenses do not appear in the filing; both need IR confirmation. Q1-Q32: 1 answered, 7 partial, 1 evaded, 23 unasked."
```
