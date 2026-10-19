# A3 FORENSIC NOTES: Kross Limited (KROSS), Q2 FY27, doctype CONCALL (Role 5 addendum)

CAVEAT (binds every finding below): MACHINE TRANSCRIPT (faster-whisper; medium.en to 20:00, small.en after; L19). Not official. Speakers are INFERRED, not labelled. Numbers and names may be mis-heard. On any number conflict the filed results win. All line numbers are lines in the A1 fulltext (runs/kross-q2fy27/extracted/kross-concall-q2fy27-fulltext.md).

Inputs read: A1 structured (R001-R334), A1 fulltext (L1-L509), A2 ledger (sections 1-11, including rows M1 and M2 added in Role 5 loops 1 and 2), Notion memory (runs/kross-q2fy27/work/notion-thesis.md), Role 4 review Step 8.5 (runs/kross-q2fy27/work/review_kross_q2fy27.md, Q1-Q22). Prior-quarter fulltext: none supplied. No source document and nothing under inputs/ was opened.

Revisions:
- ROLE 5 LOOP ITERATION 1: ledger row M1 read and reconciled (334 to 335 units). No finding added; CC-F6-02 refs extended. See section 1A.
- ROLE 5 LOOP ITERATION 2 (final): ledger row M2 read and reconciled (335 to 336 units). No finding added; folded into CC-F6-08. A2 corrected M1 to T35 as flagged. See section 1B.

---

## 1. LEDGER RECONCILIATION

- Units: 334 structured IDs (R001-R334) plus 2 ledger-only rows (M1, M2; ledger section 11) = 336. Ledger references: 336. Orphans: 0. Units read at cited line: 336 of 336 (100%).
- Every row's verbatim value was found in the fulltext at its cited line, or within two lines of it. Line drift (A1 cite vs where the value sits; quote confirmed, no content issue):

| Row | A1 line | Value found at | Note |
|---|---|---|---|
| R027 | 122 | L124 | "33.16 crores" carries over the page break |
| R051 | 234 | L235 | "50-55%" |
| R072 | 336 | L335 | "funded by 110 crores via term" |
| R083 | 365 | L366 | "This plan is $110.70" |
| R102 | 459 | L458 | "No, no, 30% of it, 30%." |
| R103 | 480 | L481 | "a guided 14-15% kind of a beta margin" |
| R104 | 492 | L493 | "55 on the roads" |
| R141 | 424 | L425 | "there is York" |

### 1A. Ledger row M1 (MISSING_FROM_STRUCTURED, added Role 5 loop 1)

- Verbatim at L324-L326: "Secondly, on the key space that we were doing on seamless view, if you could highlight what / is the amount that we are spent in now and what is the we are going to spend maybe 1 / 6 3 7 or 4 routes." L327: "So, how much of that is already been spent?"
- Speaker attribution: Shubham Batra's second question (T35, Q4 slot). Batra is introduced at L298-L299; Vignesh only at L341-L342. A2 has corrected the ledger row from T39 to T35 (loop 2).
- Figure: ASR garble of an analyst-stated total. Not estimated. Management did not confirm it. Management's own budget figure is "approximately 170 crores" (L334-L335, R071). "No, that's not to figure" (L334) answers the analyst's "120 odd" six-month spend (L333, R070), not M1.
- Effect on findings: none changes. M1 is added to the CC-F6-02 ledger refs and line cite as one more unconfirmed seamless budget reference. Classification and implication unchanged.

### 1B. Ledger row M2 (MISSING_FROM_STRUCTURED, added Role 5 loop 2)

- Verbatim at L453-L454: "And check this index tube is overall 1 leg capacity right. / So phase 1 would be 2 percent of that." The exchange continues: L455 "Absolutely." L456 "Sorry." L457 "Phase one would be 50% of that capacity." L458 "No, no, 30% of it, 30%." L459 "Phase one, yeah."
- Speaker: Dhvanil Shah follow-up (T58, Q7 slot), as the ledger states. Confirmed.
- Figure: the "2 percent" and the "1 leg" capacity base are both ASR garbles of analyst-stated figures. Neither is estimated.
- Disposition: folded into CC-F6-08 (seamless phase 1 share and margin basis). M2 adds one fact to that finding. The "Absolutely." at L455 confirms the garbled 2% before the speaker apologises, and the analyst then offers 50%. The only management figure, 30%, is a single correction (L458). It is not repeated in the prepared remarks and not tied to a tonnage. That makes the phase 1 share weaker evidence than the row count suggests. It does not change CC-F6-08's classification (AMBIGUOUS) or its question. No new finding.

### A2 flag dispositions

| A2 flag | Rows | Disposition |
|---|---|---|
| NUMBER_CONFLICT PAT | R005 vs R021 | Not a conflict. "196 million" (L38) = Rs 19.6 Cr; Rs 19.69 Cr (L118) = 196.9 million. Unit restatement only. Filings govern. |
| NUMBER_CONFLICT EBITDA | R003 vs R017 | "IPITA was 36 crores" (L37) implies 15.3% on Rs 235 Cr. That contradicts "13 percent" in the same sentence (L37-L38). "30.6 crores with a margin of 13%" (L116) gives 13.02%, which ties to the filed 13.02% ex-OI (review 6E). H1 53.32 less Q2 30.6 = Q1 22.72 Cr = 12.3% on Rs 184.3 Cr (ties to the Notion Q1 12.2%). Treat 36 as an ASR outlier and discard it. |
| NUMBER_CONFLICT seamless split / debt | R069-R090, R304, M1 | Real conflict across three answers. See CC-F6-02 and CC-F6-03. |
| DATE_CONFLICT | R238, R309 | "as on 3rd September" (L371). Read as 30 September: the Rs 115 Cr stated there ties to the filed Rs 117.14 Cr borrowings at 30-Sep-2026 (review Q8). |
| REPEAT_QUESTION seamless funding (x3) | R134, R136, R137 | Asked by Batra (L324-L327), Vignesh (L343-L344) and Rajat (L362-L364). The funding split changed in each answer. See CC-F6-02. |
| REPEAT_QUESTION axle volumes | R127, R140 | First answer "in excess of 10,500" (L223). Second answer "in excess of 10,000" (L412), with the exact figure deferred to a private follow-up. See CC-F6-09. |
| REPEAT_QUESTION receivables | R126, R127 | Receivables are asked once in the text (L179-L182). The Q2 slot (Chheda) covers utilisation and volumes (L204-L246). Repeat not confirmed. No finding. |
| MGMT_ABSENCE_QA | R109 | See CC-F17-09. |
| AUDIO_GAP | R333 | See CC-F17-07. |
| TIMELINE_WATCH | R161, R186, R187, R199 | See CC-F6-01. |
| MISSING_FROM_STRUCTURED; ANALYST_FIGURE; ASR_GARBLE | M1 | See section 1A. T35 (Batra), corrected by A2. Folded into CC-F6-02. |
| MISSING_FROM_STRUCTURED; ANALYST_FIGURE; ASR_GARBLE | M2 | See section 1B. T58 (Dhvanil Shah). Folded into CC-F6-08. |

---

## 2. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| CC-F6-01 | F6 | R161, R186, R187, R199, R200, R201, R301 | L99-L100; L331-L333; L440-L442 | "we plan to undertake production trials in February or March of 2027" / "Hopefully, by end of Q4, we will be able to have some production trials" / "It's not that we would be 100% productionizing it by quarter four itself... by end of H1, we should be able to be completely backward integrated" | FORWARD-SIGNAL | The Q1-call milestone "seamless commercial Q4 FY27" is now trials in Q4 FY27. Full captive use is at end H1 FY28. Equipment is still in transit for Nov-Dec (L331-L332). No external-sale or first-revenue date was given. Seamless benefit moves to H1-H2 FY28 at the earliest. Finance cost and depreciation arrive first. |
| CC-F6-02 | F6 | R069, R072, R073, R074, R075, R076, R078, R083, R084, R085, R304, M1 | L324-L326; L328; L335-L339; L366-L367 | "spent approximately 50 crores on our, from our terms on borrowing" / "funded by 110 crores via term loan, the rest is from internal accruals" / "Our own contribution is about 60 crores. 60 crores plus 70 crores we have taken as our the firm term loan 70 plus 50 120 crores out of the 170" / "This plan is $110.70 out of which 50 crores is being done from internal accruals" | AMBIGUOUS | Three answers give three splits. Internal accruals are 50 or 60. Term loan drawn is 50, 60 or 70. Term loan size is 110 or "110-120" (L367). The analyst's own budget figure (M1, L325-L326) is garbled and unconfirmed. Management's budget is about 170 (L335). The most consistent reading: debt rose 35 to 80 (L352-L353), so about 45-50 Cr of term loan is drawn; spend of 120 then implies about 70 Cr own money, above the 60 budgeted. "Most of the internal accruals have already been done because we are eligible to take the entire term loan" (L336-L337) says the own contribution was front-loaded. That explains part of the H1 cash drain. Ask for the sanction, the drawdown to date and the own money spent, in Rs Cr. |
| CC-F6-03 | F6 | R079, R080, R086, R087, R088, R089, R090, R193, R194, R308, R310 | L371-L376; L368-L370 | "the total debt comes to around 115 crores including working capital. If I were to add that 50 crores which we have not drawn till now, so it will be around 165, 170 crores." / "Yeah, correct" / "There are no further debt plans on any of our expansion plans" | FORWARD-SIGNAL | Management confirmed FY27-end gross debt of about Rs 165-170 Cr. Filed borrowings were Rs 52.37 Cr at FY26 end and Rs 117.14 Cr at H1 (review Q8, derived). So debt reaches about 3.2x the FY26-end level before seamless revenue. The "no further debt" claim is conditional on equipment timing (L368-L369). It also excludes working-capital borrowing: the CC limit is Rs 32 Cr (L376) against receivables of about Rs 206 Cr (review Q6). Finance cost steps up in H2 FY27 and FY28. |
| CC-F6-04 | F6 | R077, R081, R066, R166, R188, R189, R190, R191, R192 | L345-L351; L355-L359; L288-L289; L106 | "what we are basically raising, is close to 60 crores. We are planning on an immediate capex via warrants and pressures which we would be spending between the next two quarters" / "roughly 110 corrodes of KFX in H2" / "about 24, 25, 20-odd crores in this area, in this ah cold drawn tube" | FORWARD-SIGNAL | H2 FY27 capex is about Rs 110 Cr (analyst sum, not denied): about 60 Cr preferential-funded lines (shaft lines, robotic automation, L355) plus about 50 Cr seamless balance. Cold drawn tube adds Rs 20-25 Cr, undated and unfunded on the call. Funding gap: per Notion, the Aug-2026 raise brings Rs 31.8 Cr equity plus Rs 7.95 Cr warrant upfront (25%) = Rs 39.75 Cr. About Rs 23.85 Cr needs promoter warrant conversion, which has an 18-month window. Spending "between the next two quarters" needs early conversion, internal accruals, or debt. The last contradicts CC-F6-03. The issue is still "ongoing" (L106). |
| CC-F6-05 | F6 | R152, R203, R204, R205, R325, R326, R327, R328, R329, R330, R331 | L470-L477; L485-L489; L56-L57 | "only a part of the compensation on steel as a commodity which we have received in quarter 1" / "We have very recently settled with most of our OEMs and TAFE companies on a conversion front as well. that impact would be coming in our upcoming quarter, that is quarter 3, mostly in quarter 3 and quarter 4" / "We do believe all of it will be compensated obviously, you know, retrospective" / "settlements are underway" | FORWARD-SIGNAL | Q3 and Q4 gross margin is the test of the pass-through claim. Management claims retrospective compensation on steel, conversion and consumables. Notion memory says the trailer-axle half has "no retrospective mechanism". This conflicts with that memory. A retrospective credit booked in one quarter would inflate that quarter's margin and must be stripped out. Ask: Rs Cr of retrospective credit, which customers, which quarter it is booked, and whether trailer customers are included. |
| CC-F6-06 | F6 | R031, R033, R034, R035, R036, R037, R038, R174, R175, R176 | L188-L191; L193-L197 | "in H1 of last year, they were in excess of 110 days" / "for the quarter, it's almost come down back to around 81 days and overall for H1 period, it's at around 90 days" / "our receivable days will be at around 80 and our working capital cycle should be lesser than 90, 95 days" | FORWARD-SIGNAL | A testable commitment: receivable days about 80 and a WC cycle under 90-95 days. Notion CCC was 153 days in FY26. The 81-day Q2 figure sits on a quarter with revenue 27.5% above Q1, so growth lowers days mechanically. The review found like-for-like days flat (89.1 to 90.0). Test at the FY27 balance sheet (Q4 FY27 results). Export receivables stay above 120 days (L193-L194). |
| CC-F6-07 | F6 | R154, R155, R172, R173, R184, R185 | L63-L64; L318-L323 | "we expect Q3 and Q4 volumes to be stronger than Q2" / "Overall volumes and historically also H2 is always 20% up on H1" / "Q3 and Q4 we should see numbers in this range or higher." "Yes, sir." | FORWARD-SIGNAL | If applied to revenue, H2 at 1.2x H1 Rs 419.4 Cr = about Rs 503 Cr, so FY27 about Rs 923 Cr (arithmetic). That is above the Notion base of Rs 830 Cr and above the review's H2 need of Rs 461-482 Cr. The statement is framed on "volumes" and conflicts with the deck (see CC-F16-02). Test: Q3 FY27 revenue at or above Rs 235 Cr, and trailer revenue at or above about Rs 115 Cr. |
| CC-F6-08 | F6 | R099, R100, R101, R102, R198, R202, R323, R324, M2 | L438-L439; L443-L446; L449-L451; L453-L459 | "phase one will be on our backward integration or the active requirement" / "approximately 8 to 10% lesser than... existing buying prices" / "on our axles front we should be having on the overall business we should be having a margin of approximately 3 to 4 percent" / "So phase 1 would be 2 percent of that." "Absolutely." ... "No, no, 30% of it, 30%." | AMBIGUOUS | The margin benefit has no clear basis: 3-4 points on axles or on the whole company. Trailer is 49% of revenue, so 3-4 points on axles is about 1.5-2.0 points at company level (arithmetic). Phase 1 share rests on one corrected answer: management first said "Absolutely." to a garbled 2% (M2, L454-L455), then gave 30% after the analyst offered 50% (L457-L458). The capacity base ("1 leg", L453) is also garbled. Neither is estimated. Phase 1 is captive. The surplus is merchant tube, a commodity-converter slice (Amendment 17 question for /fttcp). The saving is also hedged on commodity prices (L446). Ask: phase 1 capacity in tonnes, the total capacity, and the margin basis. |
| CC-F6-09 | F6 | R095, R096, R097, R098, R195, R196, R316 | L408-L412; L417 | "I will have a look at the exact volumes and we will have it sent over to you for quarter two" / "in excess of 10,000, again on the exact numbers we will share that with you" / "So all put together, we will share these numbers with you." | AMBIGUOUS | Management promised to send Q2 axle and suspension volumes privately to one analyst. The stated figure also moved from 10,500 (L223) to 10,000 (L412). Fair-disclosure practice: ask whether the volumes will be published by exchange filing or in the next deck. A disclosure-quality data point. |
| CC-F7-01 | F7 | R103, R332, R327, R331 | L477-L482 | "still as a commodity we see increase going on in each and every quarter" / "OEMs are also talking about another increase in quarter 3 as well" / (analyst) "difficult to give a sense of when we can return to maybe like a guided 14-15% kind of a beta margin." (mgmt) "Yeah, it is difficult currently." | FORWARD-SIGNAL | Management did not reaffirm the Q1-call 14-15% EBITDA guide and gave no date. Pass-through chases a cost that rises every quarter. Under conservative bias the working case for H2 FY27 is about 13%, not 14-15%. Re-engage trigger 1 (margin above about 14%) is unlikely to fire at Q3. |
| CC-F7-02 | F7 | R186, R187, R193, R300, R301, R307 | L331-L333; L357-L359; L368-L369 | "We have a couple of more equipment which is in transit" / "hopefully we will be getting our all our equipment in time and if that is if that goes after the timeline then yes it should be done within H2" / "if all the equipment that we have to receive is stipulated time" | AMBIGUOUS | Three conditional hedges sit on the seamless schedule, the H2 capex timing and the "only debt" claim. Ask: which equipment is in transit, from which supplier, and the shipped and delivery dates. A slip moves trials past Q4 FY27 and pushes capex and drawdown into FY28. |
| CC-F7-03 | F7 | R172, R224, R225, R267, R135, R296, R185 | L148-L153; L313-L316; L322-L323 | "the monsoons ended in about, you could say, July. And then the demand started picking up in August." / "people were waiting for those monsoons to get over to buy the vehicles" / "certain markets has recently... got good demand after a really long time. One of these markets is Chhattisgarh." / "at least for this financial year we see that unless something." | FORWARD-SIGNAL | Part of the Q2 trailer jump is timing: monsoon pent-up buying and one region (Chhattisgarh). The sustainability answer is hedged and cut off ("unless something"). Q3 trailer revenue at or above Rs 115 Cr separates a new level from a timing spike. |
| CC-F7-04 | F7 | R285, R286, R287, R180 | L269-L274 | "post Diwali period, they do see a dip" / "it all depends how much of inventory all these tractor manufacturer companies are carrying" | NEUTRAL-FACT | Agri Q4 is unguided; Q3 "similar numbers as compared to quarter 2" (L274-L275). Tractor is 10-11% of revenue (L397). Low materiality. Monitor only. |
| CC-F7-05 | F7 | R141, R142, R143, R144, R319, R320, R321 | L425-L427; L432-L434 | "there is York, who are the market leaders in this segment and there's Tata Motors as well, who are in this business" / "it all depends on the product families actually." | AMBIGUOUS | Management names Tata Motors as a trailer-axle competitor. Notion memory lists Tata Motors as a customer. The largest customer is 15-16% of revenue (L398). Ask: is the largest customer Tata Motors, and does Tata Motors make trailer axles in-house that compete with Kross supply? Insourcing risk on a concentrated account. |
| CC-F16-01 | F16 | R012, R029, R030, R039, R040, R041, R042, R043, R044, R045, R046, R047, R119, R157, R177 | L69-L70; L208-L215; L223 | "the capacity utilization of this is approximately 80 percent of our current output" / "No, no sir, that is not the information that is there. Say we are making currently 4,000 trailer axles, 4,200 trailer axles per month. On that we are utilizing between 65 to 80% of our extruded beams" / "On that it is at 80% today." | AMBIGUOUS | The deck's and CMD's extrusion "utilization" is the share of axles made by extrusion, not plant fill. Management denied it applies to the 7,500/month expanded capacity (analyst figure). Run rate of 4,000-4,500/month (L209-L214) gives 12,000-13,500 per quarter. Q2 volume was "in excess of 10,500" (L223), about 3,500/month. Either September is an exit rate well above the quarter average, or the figures conflict. On 7,500/month capacity, 4,200/month is about 56% fill (arithmetic). The 100% switch is "by Q3 or Q4" (L73) and "next one or two quarters" (L211). Benefits come "over a longer time period" (L177), so the extrusion saving is not a near-term margin lever. |
| CC-F16-02 | F16 | R011, R155 | L64 | "Overall volumes and historically also H2 is always 20% up on H1." | AMBIGUOUS | The CMD says 20% on the call. The same-quarter deck says "always 10-15% up than H1" (PPT L102 per review Q18). FY26 revenue H2 was 1.49x H1 (review Q18). Three numbers describe one seasonal pattern. Guidance language moved up between deck and call. Ask for the metric (volume or revenue) and the history. |
| CC-F17-01 | F17 | R017, R018, R103, R332 | L116; L480-L482 | "EBITDA for this quarter was at 30.6 crores with a margin of 13%." / "Yeah, it is difficult currently." | CONFIRMATORY-NEGATIVE | Q1-call guide was 14-15%. Q1 printed 12.2% (Notion) and Q2 13.0% (L116; filed 13.02%). That is two straight quarters below guide, and the guide was not reaffirmed. Score: NOT DELIVERED, NOT REAFFIRMED. |
| CC-F17-02 | F17 | R061, R062, R063, R064, R129, R179 | L255-L258; L260-L261 | "In quarter 2, we have done similar volumes what we had done in quarter 1." / "we set the capacity of close to 800 numbers, we should be at a few 50, 60 percent of that capacity by quarter 4." / (asked for revenue) "The realization value of one tipping set is at approximately 1.4 lakh rupees." | FORWARD-SIGNAL | Q1-call promise: 500/month. Q2 was flat on Q1, about 75/month per Notion's 226 kits in Q1. New path: 50-60% of about 800 = about 400-480/month by Q4. So 500/month is not reached even at Q4 FY27. The analyst asked for revenue and got a per-unit price instead. At 480/month and Rs 1.4 lakh, the Q4 run rate is about Rs 20 Cr per quarter (arithmetic). Track the Q4 figure. Score: SLIPPED. |
| CC-F17-03 | F17 | none (silence) | no transcript line; search for mould, casting, HPML returns zero hits in L1-L509 | (no mention) | AMBIGUOUS | The HP moulding line was due Sept-2026 per the Q1 call. The date has passed and the call says nothing. The review records the PR as "progressing as planned", not commissioned, and line identity is unclear (review Q13). One quarter of silence on a missed dated milestone. Send review Q13 by IR email. |
| CC-F17-04 | F17 | R010, R113, R166, R077 | L49-L50; L106; L345-L347 | "a preferential issue to the tune of 63.6 crores" / "financed through the ongoing preferential issues" | AMBIGUOUS | The call is silent on in-principle approval, allotment date and the four non-promoter allottees (Notion checklist; review Q10). "Ongoing" says the issue is not complete. H2 capex plans depend on it (CC-F6-04). |
| CC-F17-05 | F17 | R076 | L339-L341 | "basically 120 crores of cash flow has happened in the books" | CONFIRMATORY-NEGATIVE | The only "cash flow" on the call is project spend. Nothing on H1 CFO or closing cash (Notion checklist). The filed H1 CFO/PAT is 0.14x and FCF is negative (review 6.5). Silence on a deteriorating metric is a confirmatory negative per Role 5. |
| CC-F17-06 | F17 | none (silence) | search for ROCE returns zero hits in L1-L509 | (no mention) | CONFIRMATORY-NEGATIVE | Re-engage trigger 2 (ROCE back toward 20%) and the Notion core tension (ROCE 34% to 16%) are not addressed. The review puts H1 ROCE flat at about 15.5% with CWIP of Rs 54.92 Cr not earning. Management did not volunteer it. Review Q21 (half-year ROCE in the deck) stays open. |
| CC-F17-07 | F17 | R104, R105, R146, R333 | L490-L495 | "CWIT stands at roughly 55 on the roads. And we mentioned that we have done a difference of around 120,000" [00:48:16] / [00:48:48] "over to the management for closing comments." | AMBIGUOUS | The only balance-sheet question on the call (CWIP about Rs 55 Cr, filed Rs 54.92 Cr) was lost in a 32-second gap. The moderator then says "As there are no further questions" (L494). No answer is on record. Route review Q11 and the balance-sheet questions (Q4, Q5, Q8, Q12, Q22) to IR email. |
| CC-F17-08 | F17 | R047, R052, R053, R054, R056, R058, R059, R060, R067, R097, R280, R317, R318 | L223-L224; L234-L244; L413-L416 | "we've done in excess of 10,500 trailer axles" / "quarter versus quarter we've done around 50% more. In quarter one we had done of this year around 75" / "115 or 115" / "Compared to 58 yeah" / "a lot on the suspension plus due to commodity increases there has been a surge in prices as well" | AMBIGUOUS | Trailer revenue: Rs 115 Cr vs Rs 58 Cr YoY (+98%) and vs Rs 75 Cr QoQ (+53%). Axle volume: +50-55% YoY (L234-L235) and about +10.5% QoQ on the analyst's Q1 recall of 9,500 (L413, not confirmed). So about 28-32% of YoY value growth per unit comes from suspension mix and commodity price pass-through (arithmetic). Pass-through revenue carries little margin, which fits gross margin falling 46.23% to 43.90% (review Q1). This partly answers review Q3. The one-time fleet order question remains open. |
| CC-F17-09 | F17 | R109, R248 | L30-L31; L89-L91 | "I'll now hand over the call to Kunal sir for his opening remarks" / "I'm Sudhir here." / "hand it over to Sumit Rai" | NEUTRAL-FACT | Sudhir Rai (CMD, about 38% holder per Notion) gave the opening remarks only. No Q&A answer is attributed to him; speakers are inferred, low confidence. Q&A ran through Sumit and Kunal Rai. Governance data point only; no inference on intent. |

---

## 3. CHECKLIST SCORECARD

| Check | Status | Basis |
|---|---|---|
| F1 | N.A. | Concall. No ZERO_STANDING rows in the ledger (ledger section 10). |
| F2 | N.A. | No standalone vs consolidated figures on the call. |
| F3 | N.A. | No cost-line tables on the call. |
| F4 | N.A. | No auditor Other Matters paragraph on the call. |
| F5 | N.A. | No Going Concern / EoM text on the call; no prior-quarter extract supplied. |
| F6 | FINDING | 9 findings (CC-F6-01 to CC-F6-09). 18 commitments in the register below. |
| F7 | FINDING | 5 findings (CC-F7-01 to CC-F7-05). Ledger HEDGE rows R155, R172, R185, R287, R307, R321, R322, R332 all read. |
| F8 | PASS | Checked. Implied Q2 ETR = 1 - 19.69/26.94 = 26.9% (L117-L118), 174 bps above 25.17%. Within normal range. No prior-year tax line on the call. The results-filing A3 owns the full tax read. |
| F9 | N.A. | No OCI on the call. |
| F10 | N.A. | No paid-up capital or EPS on the call. Preferential issue mentioned (L49-L50, L106); allotment silence is carried to CC-F17-04. |
| F11 | N.A. | No net worth or reserves on the call. |
| F12 | N.A. | Segment revenue shares only (L118-L120, L395-L398). No segment assets or liabilities on the call. |
| F13 | N.A. | No board outcome on the call. |
| F14 | N.A. | No notes or auditor letter on the call. Transcript-level inconsistencies (EBITDA 36 vs 30.6; host name; Sumit vs Sumeet) are handled in the A2 flag dispositions as ASR artifacts. |
| F15 | N.A. | No consolidation entity list on the call. |
| F16 | FINDING | Applied to call vs same-quarter deck where the call itself references the deck (L204, L276). 2 findings: CC-F16-01 (extrusion "utilization" redefined), CC-F16-02 (H2 seasonality 20% on call vs 10-15% in deck). |
| F17 | FINDING | 9 findings (CC-F17-01 to CC-F17-09). Silence audit tables in section 5. Review Q1-Q22: 0 ANSWERED, 11 PARTIAL, 1 DECLINED, 10 SILENT. |

---

## 4. COMMITMENT REGISTER (F6)

| # | Commitment | Implied date | Turn / line ref | Status word |
|---|---|---|---|---|
| C01 | Extruded axle beam commercial production | done | T4 L69 (R119) | completed ("has commenced") |
| C02 | Trailer axles 100% on extruded beam (80% today) | Q3 or Q4 FY27 | T4 L73-L74 (R157); T17 L211, L215 (R177) | underway |
| C03 | Seamless: sizing and straightening mills received and installed | done | T5 L99 (R124) | completed |
| C04 | Seamless: furnace mostly ready, piercing mill almost ready; remaining equipment received | end Nov or Dec 2026 | T36 L330-L332 (R300, R301, R186) | underway (equipment in transit) |
| C05 | Seamless production trials | Feb or Mar 2027; "end of Q4" FY27 | T5 L100 (R161); T36 L332-L333 (R187); T55 L440 (R199) | not started (hedged "hopefully") |
| C06 | Seamless phase 1 (about 30% of capacity per one corrected answer, captive); full backward integration | end H1 FY28 | T55 L438-L442; T58 L453-L459 (R198, R200, R201, R102, M2) | not started |
| C07 | Seamless cost 8-10% below buying price; axle margin +3-4% | after integration (H1 FY28 on) | T55 L443-L444 (R099); T57 L449-L451 (R100, R202) | not started; basis ambiguous |
| C08 | Seamless budget about Rs 170 Cr; balance about Rs 50 Cr spent entirely in H2 FY27 | H2 FY27, if equipment on time | T36 L335 (R071); T39 L350-L351, L356-L359 (R078, R190, R192, R307) | underway (Rs 120 Cr spent, L339-L340) |
| C09 | Only debt is the seamless term loan; no further debt plans; FY27-end debt about Rs 165-170 Cr | FY27 | T41 L364-L370 (R193, R194, R308); T42-T43 L371-L377 (R088, R310) | underway (conditional) |
| C10 | Immediate capex of about Rs 60 Cr via warrants and preferential (shaft lines, robotic automation) | next two quarters (H2 FY27) | T39 L345-L349, L355 (R077, R188, R189, R191) | initiated (issue "ongoing", L106) |
| C11 | Cold drawn tube line and metal treatment, about Rs 20-25 Cr; partly for merchant sale | not dated | T28 L280-L289, L292 (R066, R182, R291) | initiated (planned) |
| C12 | Receivable days about 80; WC cycle under 90-95 days | not dated (FY27 balance sheet is the test) | T14 L196-L197 (R175, R176) | not started (guidance) |
| C13 | Q3 and Q4 volumes stronger than Q2; H2 20% up on H1 | H2 FY27 | T4 L63-L64 (R154, R155) | guidance |
| C14 | Trailer revenue Q3 and Q4 at Q2 level or higher, "at least for this financial year" | Q3-Q4 FY27 | T33-T34 L318-L323 (R184, R185) | guidance (hedged) |
| C15 | Price revisions and conversion settlement impact; retrospective compensation | Q3 and Q4 FY27 | T4 L55-L57 (R152); T61 L474-L477, L485-L489 (R203, R204, R205) | underway ("settlements are underway") |
| C16 | Tipping jacks at 50-60% of about 800 capacity | by Q4 FY27 | T24 L257-L258 (R063, R179) | underway (Q2 flat on Q1) |
| C17 | Exports up 45% this year on last year | FY27 | T4 L87-L88 (R160) | guidance |
| C18 | Send exact Q2 axle and suspension volumes to the analyst | after the call | T51 L408-L412, L417 (R195, R196) | promised (private follow-up) |

Also on record (status only, no date): European customer for propeller shaft parts, "not in mass production... under a validation stage" (L384-L386, R139, R312). Agri Q3 "similar numbers as compared to quarter 2" (L274-L275, R180). Utilisation to improve "over the coming two quarters" (L125-L126, R169).

---

## 5. SILENCE AUDIT (F17)

### 5A. Q1 FY27 call guidance scored against this call

| Q1-call promise (memory) | This call | Line | Score |
|---|---|---|---|
| EBITDA margin 14-15% | Q2 13%; guide not reaffirmed, "Yeah, it is difficult currently." | L116; L480-L482 | NOT DELIVERED; NOT REAFFIRMED (CC-F17-01, CC-F7-01) |
| Tipping jacks to 500/month | Q2 "similar volumes" to Q1; 50-60% of about 800 by Q4 = about 400-480/month | L255-L258 | SLIPPED: below 500 even at Q4 (CC-F17-02) |
| HP moulding line Sept-2026 | Not mentioned | none (zero hits) | SILENT; date passed (CC-F17-03) |
| Seamless tube commercial Q4 FY27 | Trials Feb-Mar 2027 / end Q4; not 100% in Q4; full captive by end H1 FY28 | L100; L332-L333; L440-L442 | REFRAMED and SLIPPED about two quarters (CC-F6-01) |

### 5B. Notion monitoring checklist, re-engage triggers and growth levers

| Item (Notion) | Status on call | Line | Consecutive quarters silent |
|---|---|---|---|
| Re-engage 1: margin above about 14% AND debtor days falling | ADDRESSED. Margin 13% (fails). Days: H1 about 90 vs H1 FY26 above 110; Q2 about 81 | L116; L188-L191 | 0 |
| Re-engage 2: ROCE back toward 20% | SILENT | none | 1 (prior quarters NOT FOUND; no prior transcript supplied) |
| Re-engage 3: price into Rs 150-185 | N.A. (market item) | none | n/a |
| FY27 base needs about 13.2% margin over Q2-Q4 | PARTIAL. Q2 13%; H2 margin undated | L116; L482 | 0 |
| Separating observation: Q2 margin | ADDRESSED. 13%, between the 12.5% bear line and the 14% gate | L116 | 0 |
| HP moulding line commissioned? | SILENT | none | 1 |
| H1 CFO and cash | SILENT (only project spend) | L339-L341 | 1 |
| Preferential allotted? | SILENT on status; "ongoing" | L106 | 1 |
| Seamless funding (debt vs equity) | ADDRESSED, conflicting | L324-L326; L328; L335-L339; L366-L367; L371-L376 | 0 |
| FY26 AR cash flow, segment split, top-5 de-growth | PARTIAL. Segment shares and largest customer 15-16%; nothing on top-5 de-growth or cash flow | L395-L398 | 1 (top-5 de-growth) |
| Extruded-beam OEM adoption | PARTIAL. "feedback is positive"; no named OEM approvals | L170; L175-L178 | 0 |
| Identity of four non-promoter allottees | SILENT | none | 1 |
| Lever: extrusion axle beam | ADDRESSED | L69-L74; L171-L177; L209-L215; L306-L307 | 0 |
| Lever: seamless tube | ADDRESSED | L98-L102; L324-L340; L436-L459 | 0 |
| Lever: tipping jacks | ADDRESSED (no volume number) | L255-L261 | 0 |
| Lever: HP moulding line | SILENT | none | 1 |
| Lever: tractor share 9% to 15% | PARTIAL. 10-11% share; target not restated | L397 | 0 |
| Lever: exports 4% to 8% | ADDRESSED. 8% of component business (about 4.1% of revenue); 4-4.5% of business; +45% YoY; new European customer under validation | L82; L87; L163; L195; L384-L386 | 0 |
| Concall promise log (prior Q4M table) | ND on the Notion page | none | n/a |

### 5C. Role 4 review Questions-for-Management (Step 8.5, Q1-Q22)

Note: none of Q1-Q22 was put to management by the company's analysts. The status records what the call happened to cover.

| Q | Topic | Status | Transcript line | Note |
|---|---|---|---|---|
| Q1 | Steel settlement in Q2 COGS, Rs Cr | PARTIAL | L468-L477 | Gross margin fall explained as partial steel compensation and uncompensated consumables; conversion settled, impact Q3-Q4. No Rs Cr; no yes/no on a one-off in Q2 COGS. Leans to lagged pass-through, not a one-off. |
| Q2 | 14-15% guide still valid, which period | DECLINED | L480-L482 | "Yeah, it is difficult currently." No period, no reaffirmation. |
| Q3 | Top-5 rise, largest customer, one-time fleet order | PARTIAL | L398; L303-L305; L313-L316 | Largest customer 15-16%. Wallet-share gains plus Chhattisgarh orders. One-time order not addressed. See CC-F17-08. |
| Q4 | Other income Rs 1.44 Cr identity | SILENT | none | |
| Q5 | Other current assets: GST credit vs supplier advances | SILENT | none | |
| Q6 | Receivables overdue beyond 180 days; ECL allowance | PARTIAL | L188-L197 | Days given (81 Q2, 90 H1, export above 120). No ageing, no ECL. |
| Q7 | Seamless commercial date, first revenue quarter, 18-month basis | PARTIAL | L100; L331-L333; L440-L442 | Trials Q4 FY27; full captive by end H1 FY28. No commercial or revenue date. |
| Q8 | Term-loan moratorium, first repayment, capitalised interest | SILENT | (adjacent: L352-L353, L371-L376 debt levels only) | |
| Q9 | Q2 EPS column error, H1 PBT gap | SILENT | none | |
| Q10 | Preferential approval date, allotment, allottees | SILENT | (adjacent: L49-L50, L106 "ongoing") | |
| Q11 | CWIP split; capex for robotic shaft and cold drawn lines; debt share | PARTIAL | L288-L289; L345-L355; L490-L494 | Cold drawn Rs 20-25 Cr; about Rs 60 Cr preferential capex for shaft and robotics. The CWIP question was lost in the audio gap. |
| Q12 | Other liabilities unwind | SILENT | none | |
| Q13 | HPML: second line, capex, date, tonnes | SILENT | none (zero hits) | |
| Q14 | Extrusion OEM approvals, capacity, saving quarter | PARTIAL | L170-L177; L208-L215 | Share of output 65-80%; 100% in one or two quarters; benefits "over a longer time period". No OEM count or saving date. |
| Q15 | Tipping-jack kits in Q2; date for 500/month | PARTIAL | L255-L261 | "Similar volumes" to Q1; 50-60% of about 800 by Q4. No number; 500/month not dated. |
| Q16 | Order book, FY27 revenue guidance, projects nearing completion | PARTIAL | L63-L64; L318-L320; L87 | Qualitative H2 outlook only. No order book, no Rs guidance. |
| Q17 | Export revenue in Rs Cr | PARTIAL | L82; L163; L193-L195 | 8% of component business is about 4.1% of revenue (arithmetic), close to the 4-4.5% stated. No Rs Cr; deck 3.21% not reconciled. |
| Q18 | H2 seasonality basis | PARTIAL | L64 | Call says 20% ("Overall volumes"); conflicts with the deck's 10-15% (CC-F16-02). |
| Q19 | Tractor EBITDA margin vs company | SILENT | (adjacent: L397 share only) | |
| Q20 | European Tier-1 PO value, product, start date; beyond Leax? | PARTIAL | L384-L386 | Product named (propeller shaft parts), validation stage. No value or date. |
| Q21 | Half-year ROCE and receivable days in the deck | SILENT | none | |
| Q22 | Other non-current assets / capital advances | SILENT | none | |

Totals: ANSWERED 0; PARTIAL 11 (Q1, Q3, Q6, Q7, Q11, Q14, Q15, Q16, Q17, Q18, Q20); DECLINED 1 (Q2); SILENT 10 (Q4, Q5, Q8, Q9, Q10, Q12, Q13, Q19, Q21, Q22).

Questions for A4 to add (new from this call): CC-F6-02 (seamless sanction, drawdown, own money spent), CC-F6-04 (warrant conversion timing vs H2 capex), CC-F6-05 (Rs Cr retrospective credit, booking quarter, trailer customers included), CC-F6-08 (3-4% margin basis; phase 1 and total seamless capacity in tonnes), CC-F6-09 (public release of Q2 volumes), CC-F7-02 (equipment in transit, dates), CC-F7-05 (Tata Motors as customer and in-house axle maker), CC-F16-01 (Q2 volume vs monthly run rate), CC-F16-02 (seasonality metric).

---

```yaml
stage: A3-forensics
company: "KROSS"
quarter: "Q2 FY27"
doctype: "concall"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/kross-q2fy27/work/forensics_concall_kross_q2fy27.md"
ledger_reconciled_pct: 100        # 336 of 336 units read (R001-R334 + M1 + M2; Role 5 loops 1-2)
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: PASS
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: N.A.
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "CC-F6-01", check: "F6", line: "L99-L100; L331-L333; L440-L442", classification: "FORWARD-SIGNAL", implication: "Seamless 'commercial Q4 FY27' now trials in Q4 FY27, full captive use end H1 FY28; equipment in transit; no revenue date; cost before benefit"}
  - {id: "CC-F6-02", check: "F6", line: "L324-L326; L328; L335-L339; L366-L367", classification: "AMBIGUOUS", implication: "Three funding splits across three answers (accruals 50/60, term loan drawn 50/60/70, loan 110/110-120); analyst budget figure (M1) garbled, unconfirmed; own contribution front-loaded (L336-L337) explains part of H1 cash drain"}
  - {id: "CC-F6-03", check: "F6", line: "L368-L376", classification: "FORWARD-SIGNAL", implication: "FY27-end debt ~Rs 165-170 Cr confirmed, ~3.2x FY26-end; 'no further debt' conditional on equipment timing and excludes WC lines"}
  - {id: "CC-F6-04", check: "F6", line: "L345-L351; L355-L359; L288-L289; L106", classification: "FORWARD-SIGNAL", implication: "H2 capex ~Rs 110 Cr plus cold drawn Rs 20-25 Cr; ~Rs 23.85 Cr of the ~60 Cr needs promoter warrant conversion inside an 18-month window; gap means accruals or debt"}
  - {id: "CC-F6-05", check: "F6", line: "L470-L477; L485-L489", classification: "FORWARD-SIGNAL", implication: "Pass-through and retrospective compensation claimed for Q3-Q4; conflicts with Notion 'no retrospective mechanism' on trailer; a booked retrospective credit inflates its quarter"}
  - {id: "CC-F6-06", check: "F6", line: "L188-L197", classification: "FORWARD-SIGNAL", implication: "Commitment: receivable days ~80, WC cycle under 90-95 days; Q2 81 days is growth-flattered; test at FY27 balance sheet"}
  - {id: "CC-F6-07", check: "F6", line: "L63-L64; L318-L323", classification: "FORWARD-SIGNAL", implication: "H2 20% above H1 implies ~Rs 503 Cr H2 and ~Rs 923 Cr FY27 if revenue; trailer Q3-Q4 at or above Q2; test Q3 revenue >= Rs 235 Cr"}
  - {id: "CC-F6-08", check: "F6", line: "L438-L451; L453-L459", classification: "AMBIGUOUS", implication: "3-4% margin benefit basis unclear (axles vs company, ~1.5-2.0 pts at company level); phase 1 share rests on one corrected answer (30%, L458) after 'Absolutely.' to a garbled 2% (M2, L454-L455); capacity base garbled; captive phase 1, merchant surplus is an Amendment 17 question"}
  - {id: "CC-F6-09", check: "F6", line: "L408-L412; L417", classification: "AMBIGUOUS", implication: "Q2 volumes promised privately to one analyst; figure moved 10,500 to 10,000; fair-disclosure and data-quality question"}
  - {id: "CC-F7-01", check: "F7", line: "L477-L482", classification: "FORWARD-SIGNAL", implication: "14-15% guide not reaffirmed or dated; costs rising each quarter; working case ~13% for H2; re-engage trigger 1 unlikely at Q3"}
  - {id: "CC-F7-02", check: "F7", line: "L331-L333; L357-L359; L368-L369", classification: "AMBIGUOUS", implication: "Three conditional hedges on equipment timing gate seamless trials, H2 capex and the 'only debt' claim"}
  - {id: "CC-F7-03", check: "F7", line: "L148-L153; L313-L316; L322-L323", classification: "FORWARD-SIGNAL", implication: "Part of Q2 trailer jump is monsoon pent-up demand and one region; sustainability answer cut off 'unless something'"}
  - {id: "CC-F7-04", check: "F7", line: "L269-L274", classification: "NEUTRAL-FACT", implication: "Agri Q4 depends on OEM inventory; tractor 10-11% of revenue; monitor only"}
  - {id: "CC-F7-05", check: "F7", line: "L425-L427; L432-L434", classification: "AMBIGUOUS", implication: "Tata Motors named as trailer-axle competitor while a customer per Notion; largest customer 15-16%; insourcing risk"}
  - {id: "CC-F16-01", check: "F16", line: "L69-L70; L208-L215; L223", classification: "AMBIGUOUS", implication: "Extrusion 'utilization' is share of output, not plant fill (~56% of 7,500/month); 4,000-4,500/month run rate vs ~3,500/month Q2 average; saving is long-dated"}
  - {id: "CC-F16-02", check: "F16", line: "L64", classification: "AMBIGUOUS", implication: "H2 vs H1 uplift 20% on call vs 10-15% in deck vs 1.49x in FY26 revenue; metric undefined"}
  - {id: "CC-F17-01", check: "F17", line: "L116; L480-L482", classification: "CONFIRMATORY-NEGATIVE", implication: "Two straight quarters below the 14-15% guide (12.2%, 13.0%); guide not reaffirmed"}
  - {id: "CC-F17-02", check: "F17", line: "L255-L261", classification: "FORWARD-SIGNAL", implication: "Tipping jacks flat QoQ; new path 400-480/month by Q4, below the 500/month promise; revenue question answered with a unit price"}
  - {id: "CC-F17-03", check: "F17", line: "none (zero hits for mould/casting/HPML in L1-L509)", classification: "AMBIGUOUS", implication: "HP moulding line due Sept-2026 not mentioned; date passed; 1 quarter of silence; send review Q13 by IR email"}
  - {id: "CC-F17-04", check: "F17", line: "L49-L50; L106; L345-L347", classification: "AMBIGUOUS", implication: "Silent on preferential approval, allotment and allottees; issue 'ongoing'; H2 capex depends on it"}
  - {id: "CC-F17-05", check: "F17", line: "L339-L341", classification: "CONFIRMATORY-NEGATIVE", implication: "Silent on H1 CFO and cash while filed CFO/PAT is 0.14x; silence on a deteriorating metric"}
  - {id: "CC-F17-06", check: "F17", line: "none (zero hits for ROCE in L1-L509)", classification: "CONFIRMATORY-NEGATIVE", implication: "Re-engage trigger 2 and the ROCE core tension not addressed; ROCE flat ~15.5% per review"}
  - {id: "CC-F17-07", check: "F17", line: "L490-L495", classification: "AMBIGUOUS", implication: "Only balance-sheet question (CWIP ~Rs 55 Cr) lost in the 00:48:16-00:48:48 gap; route Q4, Q5, Q8, Q11, Q12, Q22 to IR email"}
  - {id: "CC-F17-08", check: "F17", line: "L223-L224; L234-L244; L413-L416", classification: "AMBIGUOUS", implication: "Trailer value +98% YoY / +53% QoQ vs axle volume +50-55% YoY / ~+10% QoQ; gap is suspension mix and commodity pass-through, low-margin revenue"}
  - {id: "CC-F17-09", check: "F17", line: "L30-L31; L89-L91", classification: "NEUTRAL-FACT", implication: "CMD spoke only in opening remarks; no Q&A answer attributed (speakers inferred)"}
forward_signals: ["CC-F6-01", "CC-F6-03", "CC-F6-04", "CC-F6-05", "CC-F6-06", "CC-F6-07", "CC-F7-01", "CC-F7-03", "CC-F17-02"]
ambiguous: ["CC-F6-02", "CC-F6-08", "CC-F6-09", "CC-F7-02", "CC-F7-05", "CC-F16-01", "CC-F16-02", "CC-F17-03", "CC-F17-04", "CC-F17-07", "CC-F17-08"]
commitments:
  - {commitment: "Extruded axle beam commercial production", implied_date: "done", ref: "T4 L69", status_word: "completed"}
  - {commitment: "Trailer axles 100% on extruded beam (80% today)", implied_date: "Q3 or Q4 FY27", ref: "T4 L73-L74; T17 L211, L215", status_word: "underway"}
  - {commitment: "Seamless sizing and straightening mills received and installed", implied_date: "done", ref: "T5 L99", status_word: "completed"}
  - {commitment: "Seamless remaining equipment received (furnace mostly ready, piercing mill almost ready)", implied_date: "end Nov or Dec 2026", ref: "T36 L330-L332", status_word: "underway"}
  - {commitment: "Seamless production trials", implied_date: "Feb-Mar 2027 / end Q4 FY27", ref: "T5 L100; T36 L332-L333; T55 L440", status_word: "not started"}
  - {commitment: "Seamless phase 1 (~30% capacity per one corrected answer, captive); full backward integration", implied_date: "end H1 FY28", ref: "T55 L438-L442; T58 L453-L459", status_word: "not started"}
  - {commitment: "Seamless cost 8-10% below buying price; axle margin +3-4%", implied_date: "H1 FY28 onward", ref: "T55 L443-L444; T57 L449-L451", status_word: "not started"}
  - {commitment: "Seamless balance capex ~Rs 50 Cr of ~Rs 170 Cr, all in H2", implied_date: "H2 FY27, if equipment on time", ref: "T36 L335; T39 L350-L351, L356-L359", status_word: "underway"}
  - {commitment: "Only debt is seamless term loan; no further debt; FY27-end debt ~Rs 165-170 Cr", implied_date: "FY27", ref: "T41 L364-L370; T42-T43 L371-L377", status_word: "underway"}
  - {commitment: "Capex ~Rs 60 Cr via warrants and preferential (shaft lines, robotic automation)", implied_date: "H2 FY27", ref: "T39 L345-L349, L355; T5 L106", status_word: "initiated"}
  - {commitment: "Cold drawn tube line and metal treatment ~Rs 20-25 Cr, partly merchant", implied_date: "not dated", ref: "T28 L280-L292", status_word: "initiated"}
  - {commitment: "Receivable days ~80; WC cycle under 90-95 days", implied_date: "not dated (FY27 balance sheet)", ref: "T14 L196-L197", status_word: "not started"}
  - {commitment: "Q3 and Q4 volumes above Q2; H2 20% up on H1", implied_date: "H2 FY27", ref: "T4 L63-L64", status_word: "guidance"}
  - {commitment: "Trailer revenue Q3-Q4 at Q2 level or higher", implied_date: "Q3-Q4 FY27", ref: "T33-T34 L318-L323", status_word: "guidance"}
  - {commitment: "Price revision and conversion settlement impact; retrospective compensation", implied_date: "Q3-Q4 FY27", ref: "T4 L55-L57; T61 L474-L477, L485-L489", status_word: "underway"}
  - {commitment: "Tipping jacks at 50-60% of ~800 capacity", implied_date: "Q4 FY27", ref: "T24 L257-L258", status_word: "underway"}
  - {commitment: "Exports +45% YoY", implied_date: "FY27", ref: "T4 L87-L88", status_word: "guidance"}
  - {commitment: "Send exact Q2 axle and suspension volumes to analyst", implied_date: "post call", ref: "T51 L408-L412, L417", status_word: "promised"}
gate_a3: pass
blank_checks: []
analyst_note: "Machine transcript; filings win. Three points the rows cannot rebuild. (1) The Q2 trailer jump is mostly price and mix, not axles. Trailer value is +98% YoY and +53% QoQ (L238-L244). Axle volume is +50-55% YoY and about +10% QoQ on an unconfirmed analyst Q1 figure (L223, L235, L413). Management credited suspension and commodity-driven prices (L415-L416). Pass-through revenue carries little margin, which fits the falling gross margin. (2) The seamless own contribution was paid first (L336-L337), which explains part of the H1 cash drain. FY27-end debt of about Rs 165-170 Cr was confirmed (L373-L375), about 3.2x FY26-end. 'No further debt' is conditional on equipment timing (L368-L369), and about Rs 24 Cr of the Rs 60 Cr H2 capex rests on promoter warrant conversion. (3) Every Q1-call promise slipped or went silent: margin guide not reaffirmed (L482), tipping jacks below 500/month even at Q4 (L257-L258), seamless now trials in Q4 with full captive use by end H1 FY28 (L440-L442), HP moulding line not mentioned. Review Q1-Q22: 0 answered, 11 partial, 1 declined, 10 silent. M1 and M2 change no finding."
```
