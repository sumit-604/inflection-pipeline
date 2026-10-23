# A3 FORENSIC NOTES: PAISALO Q2 FY27, doctype CONCALL

- Agent: A3 forensic notes (claude-opus-5-5)
- Date: 2026-10-23
- Inputs read: A1 structured `extracted/paisalo-concall-q2fy27-structured.md` (R001-R288); A1 fulltext `extracted/paisalo-concall-q2fy27-fulltext.md` (lines 001-681); A2 ledger `work/ledger_concall_paisalo_q2fy27.md`. Same-quarter filed cross-checks: `extracted/paisalo-results-q2fy27-structured.md` (prefix `res:`) and `extracted/paisalo-presentation-q2fy27-structured.md` (prefix `deck:`). Prior-quarter evidence: Notion copy `work/notion_thesis_paisalo.md`, sections 3, 4, 8 and 9 (prefix `Notion §n`). No source PDF and nothing under `inputs/` was opened.
- Source caveat: the transcript is a machine ASR transcript (faster-whisper small.en), not a company-filed transcript (line 002). Every spoken number carries ASR risk. All management answers in Q&A are speaker UNRESOLVED (lines 356-676). They are written here as "management (unresolved)".
- Prior-quarter fulltext: none on record. Every Q1 FY27 diff below rests on the Notion promise log and question table. Those diffs are marked **[Notion-sourced]**.
- Row ID convention: bare `R###` = concall structured row. `res:R###` = results structured row. `deck:R###` = presentation structured row.

## 0. LEDGER RECONCILIATION

| Item | Count | Read at cited line | Notes |
|---|---|---|---|
| Structured rows R001-R288 | 288 | 288 | Every row was read at its fulltext line. |
| A2 ledger row IDs | 288 (orphan_ids: []) | 288 | 100% reconciled. MISSING_FROM_STRUCTURED: none. |
| A2 flag MGMT_ABSENCE | 1 | yes | Lines 005, 028-029. Finding C16. |
| A2 flag REPEAT_QUESTION | 9 rows (3 clusters) | yes | Yields/NIM asked 3 times (R041, R042, R045). Efficiency/cost asked 3 times (R043, R046, R047). Cost of funds asked twice (R049, R052). The efficiency cluster never received a ratio (C01). |
| A2 flag SPEAKER_UNRESOLVED | 15 turns | yes | Attribution "management (unresolved)" throughout. |
| A2 flag ASR_MISHEARD | 30 rows | yes | See section 4, spoken vs filed. |
| A2 flag FOOTNOTE_UNRESOLVED | R286 | yes | ROE/ROA history at line 503-505. Finding C10. |
| A2 flag ZERO_STANDING | R148, R150 | yes | F1. These are spoken bot-count baselines, not template lines. |
| A2 flag RESTATED | 30 rows | yes | Restatements are consistent except the app date (R227 vs R238, C08). |

ledger_reconciled_pct = 288 / 288 = 100.

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| C01 | F17 | R021, R022, R047, R232, R233, R265 | 448; 485; 487 | "when should investors expect a measurable impact on the cost to income ratio" (448) / "on a short term basis you will see that growth will outpace what we are doing here" (485) / "when we approach quarter 1 of next fiscal year" (487) | FORWARD-SIGNAL | Efficiency was asked 3 times (R043, R046, R047). No cost-to-income number was given. Q1 had an answer of "about 40%" [Notion-sourced, §9 row 1]. Filed opex is Rs605 Mn, up 33% YoY and 29% QoQ (deck:R523, R525, R527). Filed C/I is 41.0% (Notion §4, 23-Oct table). Management now dates the operating-leverage effect to about Q1 FY28. Read at face value, Q3 FY27 C/I stays above 35%. That is the second consecutive filed-basis breach and fires thesis-broken trigger (d) (Notion §2, 1.7). |
| C02 | F6 | R080, R133, R138, R159, R226, R278 | 136-137; 390-391; 474 | "our employees declined by 11% year-on-year ... We see this as an early evidence of increasing operating leverage" (136-137) / "towards the end of quarter 4 We are expecting it to normalize" (390-391) / "the cost of creating an AI framework on a short term basis remains high or elevated" (474) | FORWARD-SIGNAL | Filed cost lines do not show the leverage that the call claims. Employee benefits were Rs18.86 Cr vs Rs17.81 Cr, up 5.9% YoY with headcount down 11%, so cost per employee is up about 19% (res:R134, R139; my arithmetic). D&A was Rs5.49 Cr vs Rs2.18 Cr, up 152% (res:R137, R143). Other expenses were Rs33.69 Cr vs Rs24.16 Cr, up 39% YoY and 55% QoQ (res:R146, R152, R147). NII grew 17% (line 270). Management says the headcount trend will "normalize" (that is, hiring resumes) in Q3-Q4. AI build cost stays "elevated", and humans and AI run side by side (maker-checker, 481-484). H2 opex growth therefore has no visible brake. |
| C03 | F6 | R129, R130, R132, R225, R282, R042 | 377-379 | "net interest margins will be range bound within the expectation which was provided which was about 6% on an annualized basis ... We are currently at 5.7%" | FORWARD-SIGNAL | On the deck basis (yield less CoB), NIM was 6.8% for FY26 (deck:R731) and is 5.7% now (deck:R022). The guide of about 6% resets the anchor about 80 bps below FY26. Checklist #6 (Notion §4) has green at 6.5-7.0% and red below 6.0%. The guide sits on the red line. Basis conflict: Reg 52 NIM is 6.43% (results header line 8). An operator ruling is pending (Notion §3). The "expectation which was provided" does not appear in the Q1 forward-guidance log [Notion-sourced, §9]. |
| C04 | F6 | R125, R126, R127, R128, R131, R173, R174, R175, R222, R223, R224, R244 | 366-372; 646-654 | "about a 25 to 30 base point increase, which we have already priced in" (366-367) / "finishing our cost of funds at 10.5%" (370) / "we are currently sort of ahead of our guidance of 10.5, we are at 10% right now" (647-648) | FORWARD-SIGNAL | The guide implies a 50 bps rise from 10.0%. That reverses a five-year decline: 13.0% in FY21 (deck:R217), 10.5% in Q2 FY26, 10.0% in Q2 FY27 (deck:R093-R097). The guide lands exactly on early-warning #4, "CoB >10.5% -> pause; investigate rating" (Notion §3, 3.8). Checklist #5 green is "≤10.5%". Any overshoot trips the tripwire. The incremental cost is above the book average: unsecured NCD 12.00% on Rs124.47 Cr, filed (Notion Key Notes 23-Oct), the "unsecured 10-year paper" at line 540. Combined with the NIM guide in C03, yield must recover to about 16.5% from 15.7% (my arithmetic). Management frames the 10.5% ceiling as being "ahead". The macro premise is also unclear. The call says "RBI raising rates" (357) and also "not expecting any more rate cuts" (360). ASR may have garbled this. The prior 10.5% guide is absent from the Q1 log [Notion-sourced]. |
| C05 | F14 | R045, R230, R277, R283, R087, R088 | 76-77; 382-383; 419-428; 553-554 | "A significant portion of this funding was raised towards the end of the quarter, which temporarily impacted reported yields" (76-77) / "a majority of the disbursement ... happened towards the end of the quarter of the quarter 2 which created a denominator effect" (420-422) / "This is typical of our trend in a finance company in quarter one and quarter two for us" (553-554) | AMBIGUOUS | The call gives two different causes: late fundraising (76, 382) and late disbursement (420). The deck adds "Record disbursements temporarily diluted yields" (deck:R973). Filed disbursement was Rs15,673 Mn in Q2 vs Rs17,309 Mn in Q1, down 9.5% QoQ (deck:R056, R057; my arithmetic). That is not a record. Yield fell for a second straight quarter: 17.0, 16.9, 17.0, 16.7, then 15.7% (deck:R088-R092). The "typical Q1-Q2 trend" claim has no support in the deck series, where Q2 FY26 yield (17.0%) equals Q4 FY26. Spoken disbursement figures (1,573 / 3,292 Mn) are ASR or unit errors against filed 15,673 / 32,982 Mn. The Q3 yield print tests the transience claim. Lean bear. |
| C06 | F6 | R049, R166, R167, R168, R237, R287 | 520-524; 546-557 | "rate of change in the finance cost is about 33% ... revenue growth ... only at about 24%" (520-524) / "primarily on account of the late deployment of funds" (546-547) / "as the quarter three and quarter four comes, this automatically normalizes" (550-551) | FORWARD-SIGNAL | Standalone filed figures: finance cost Rs128.03 Cr vs Rs95.40 Cr, up 34.2% YoY. Total income Rs272.34 Cr vs Rs215.83 Cr, up 26.2% YoY (res:R086, R088, R080, R082; my arithmetic). QoQ: finance cost up 12.4%, total income up 7.0%. Borrowings are up 45% YoY against AUM up 33%. Investments rose from Rs19.8 Cr to Rs175.5 Cr, nature not disclosed (Notion §4, 23-Oct). The call alludes only to money parked "on the treasury side" (548-549). This is a dated commitment: the gap closes in Q3-Q4 FY27. If Q3 finance cost growth still exceeds income growth, the negative carry is structural (12% unsecured 10-year paper), not timing. |
| C07 | F7 | R081-R083, R192, R193, R194, R195, R215, R216, R217, R218, R114, R116, R117 | 181-207; 381 | "With Maharashtra, the most impacted states" (182) / "so it is still early to draw definitive conclusions on portfolio performance" (201-202) / "there have been certain issues that propped up on the portfolio" (381) | FORWARD-SIGNAL | Agri-equipment repayments are half-yearly and fall due after Kharif. Management says the outcome is clear "by end of October or early November" (212-213), so the test lands in Q3 FY27. Maharashtra is 20.1% of AUM (Notion §4, deck p.18), and agri and allied is about 15% (line 54). In the same quarter, the filed impairment line is a write-back of Rs0.38 Cr, against a Rs15.63 Cr charge in Q1 (res:R110, R111). Q2 PAT growth rests on that write-back. The spoken "credit cost declined to 0.4%" (296) matches the deck (deck:R609) but not the negative P&L line, so the basis is unclear. Q3 credit cost risk is skewed up. |
| C08 | F6 | R050, R207, R227, R231, R238, R239, R240, R241, R242, R264, R266, R267, R288 | 394; 580-595; 618-626 | "as guided in the last quarter, we are also releasing our app by the end of this Q3 to be targeting in Q4" (394) / "releasing it around Christmas or towards the New Year's" (585-586) / "if provided the app is stable" (623) | AMBIGUOUS | A2 marks R227 vs R238 as a timing mismatch. The Notion trigger reads "Customer App + AI Lead Engine \| Q3 FY27 Phase 1" (Notion growth triggers 3B). The call puts the release at end-Q3 or New Year. The app is visible "towards quarter four" (594), metrics come in Q1 FY28 (582-583), and the BC/OEM push starts in Q1 FY28 (618-619). FY27 acquisition is a "relatively small chunk" (626), conditional on stability (623). In effect, the catalyst has moved right by one quarter with no admitted slip. The status word is "underway". |
| C09 | F17 | R013, R014, R044, R187-R189, R202, R229 | 400-407 | "we have pretty much staked score [likely: status quo] on the co-lending side" (400) / "We are just waiting the go ahead from the respective banks" (403) / "it's staked score right now from both, from their side" (407) | CONFIRMATORY-NEGATIVE | SBI co-lending is stalled for a second straight quarter. Q1 status was "STALLED (bank-side compliance)" [Notion-sourced, §9]. Fee and commission income was not mentioned on the call. Filed fees were Rs10.09 Cr vs Rs16.69 Cr, down 39.6% YoY, at 3.7% of total income (res:R032, R034, R080; my arithmetic). Checklist #12 needs more than 5% by Q4 FY27. Thesis-broken condition (b) is below 5% by Q4 FY28. The deck still markets co-lending as "optionality for future RoA and RoE" (deck:R984). Sustained silence on a deteriorating thesis metric. |
| C10 | F14 | R048, R106-R108, R161-R165, R235, R236, R285, R286 | 499-505; 282 | "we will target somewhere around the 15 to 18%" (499) / "anywhere between 4, 4.5% is a good level" (502) / "we also doubled our ROE and ROE in the last 2 years fiscal year from about 1.5 and 7% to now 13.3 and 3.5%" (503-505) | AMBIGUOUS | FOOTNOTE_UNRESOLVED (R286), ASR-garbled. Filed ROE: 7.9% FY23, 13.4% FY24, 13.0% FY25, 13.2% FY26, 13.4% Q2 FY27 (deck:R738-R741, R107). ROE has been flat for about three years. The doubling happened in FY24, not recently. Filed ROA: 4.5% FY24, 3.9% FY25, 3.8% FY26, 3.6% Q1, 3.3% Q2 (deck:R734-R736, R111, R112). ROA is falling, and the spoken "3.5%" at line 505 conflicts with 3.3% at line 282. ROE holds only because D/E rose from 2.43x to 2.89x (Notion §4). The 4-4.5% ROA target is undated, and every guided input moves against it (C01, C03, C04). |
| C11 | F14 | R076, R077, R078, R142-R152, R148, R150 | 125; 451-461; 469-470 | "AI-driven outbound calling scaled to approximately 3,000,000 calls daily" (125) / "we did about 3 lakh outbound calls on a daily basis" (454) / "we had basically zero bots ... we had basically zero text bots then we had 7 and now we are at 15" (458-461) | AMBIGUOUS | The deck shows 300K calls daily (deck:R437, R449), so the scripted opening is 10x off, possibly an ASR error. Deck bot counts are 3 text bots in Q1, then 7 text bots and 15 voice bots in Q2 (deck:R451-R453). The spoken "zero" baselines conflict with this. Management credits AI with the Q1 3% headcount cut (469-470), yet Q1 had zero or 3 bots. Applications rose only 5.6% QoQ, 1.9 lakh vs 1.8 lakh (my arithmetic). The AI-efficiency case rests on activity counts, not cost. The headcount cut cannot yet be attributed to AI. |
| C12 | F17 | R119, R122, R123, R124, R281, R213 | 311-315; 323-325 | "Debt to equity stood at 2.89 times" (311) / "our alien [ALM] position remained comfortable with a positive gap across buckets" (314-315) | AMBIGUOUS | Leverage and liquidity moves were stated as levels only. D/E went from 2.43x in FY26 to 2.61x in Q1 to 2.89x (Notion §4). CAR fell from 33.1% to 30.7%. LCR is 2.22x vs the 8.3x logged in the thesis. Cash fell from Rs147 Cr to Rs99.6 Cr while investments rose from Rs19.8 Cr to Rs175.5 Cr (Notion §4). No analyst asked about any of these. Q1 guidance named an internal leverage cap of about 3.5x [Notion-sourced]. The call did not restate it. |
| C13 | F17 | R181, R185, R186, R213 | 005; 143-145; 661 | "The progress made through public and private NCD issuances, commercial paper, and proactive debt management" (143-144) / "that was the last question for today" (661) | CONFIRMATORY-NEGATIVE | Governance items were absent from the call. Promoter pledge: the DMD (call lead, line 005) topped up pledges on 29-Sep, and group pledge is 7.68% (Notion Key Notes 14-Oct). FCCB conversion: filed paid-up capital rose from Rs90.96 Cr to Rs91.42 Cr (res:R384, R379), consistent with 46,27,240 conversion shares (Notion). The Q1 commitment was "FCCB ~$44mn conversion pending" [Notion-sourced]. The call's liability pillar lists NCDs and CP but omits FCCBs, which the deck lists (deck:R985). The BSE Reg 60(2) fine was not mentioned. Analysts did not ask, and management did not volunteer. |
| C14 | F6 | R160, R169, R234 | 490-494; 576-579 | "we are doubling our AUM revenue impact by the end of next 3 years, next 3 fiscal years" (491-492) / "the entire framework for doubling of AUM revenue impact over the next three fiscal years" (578-579) | AMBIGUOUS | Q1 wording was "~double AUM/income/PAT in ~3 fiscal years (~FY30), base EXCLUDES co-lending" [Notion-sourced, §9]. Q2 does not restate PAT. ASR may have garbled "AUM revenue impact". Doubling in 3 years is about 26% CAGR (my arithmetic), against 33% AUM growth now. The plan implies deceleration. Line 494, "closer to the downward trajectory of our operating leverage" in the third year, pushes full cost normalisation to about FY30. |
| C15 | F17 | R212 | 116-118 | "We therefore intend to progressively broaden our product suite ... through an increasingly partnership-led and asset-like approach" | AMBIGUOUS | Q1 dated commitment: "3 new development products launch Q3 FY27-end" [Notion-sourced, §9]. Q2 restates product broadening with no names, count or date. The dated promise has been dropped to an undated intent. This is one quarter of silence on the dated version. |
| C16 | F17 | R181-R183, ledger MGMT_ABSENCE | 005; 028-029 | "Management named in the call intimation (BSE, 16-Oct-2026): Santanu Agarwal (Deputy MD), Harish Singh (ED and CFO), Gaurav Chaubey (Chief Business Officer)" | NEUTRAL-FACT | The promoter-CMD was not on the roster. The DMD led the call. The fact is confirmed by the filed intimation, so it is not an ASR artefact. Q1 roster not on record, so no trend. |
| C17 | F6 | R064, R065, R066, R067, R185, R186, R253, R254 | 071-075 | "We have successfully raised approximately 294.9 crores through our public entity issuance under the Rs. 900 crore shell program, followed by a 124.4 tonne crore listed dual-rated unsecured private placement of NCDs in September" | NEUTRAL-FACT | The Q1 commitment "NCD Rs300cr / Rs900cr shelf opens 7-Aug; second raise Q2" [Notion-sourced] is completed: Rs294.9 Cr public NCD (98% of the Rs300 Cr base), a Rs124.4 Cr unsecured private placement and Rs177 Cr of CP. This milestone confirms delivery. Cost is in C04. |
| C18 | F17 | R049, R166, R287, R041-R052 | 521; 661 | "is about 33% when we compare on a consolidated basis" (521) / "that was the last question for today" (661) | CONFIRMATORY-NEGATIVE | Five Q1 open questions went unaddressed for a second straight quarter [Notion-sourced, §8-9]: standalone vs consolidated basis (the analyst used "consolidated" and management did not engage), own-book vs off-book split, PCR and write-offs, DMD term forward-dating and NRC terms, and dividend quantum. Concall communication remains weak on the questions that matter to the thesis. |

## 2. CHECKLIST SCORECARD

| Check | Status | Basis |
|---|---|---|
| F1 Zero-value standing items | PASS | Two ZERO_STANDING rows (R148 line 458, R150 line 460) were read. Both are spoken Q1 bot-count baselines, not standing template lines, and anticipate no transaction class. Their conflict with the deck is logged at C11. |
| F2 Standalone vs consolidated | N.A. | Concall; no S/C statements are spoken. The basis silence is logged at C18. |
| F3 Shell-entity detection | N.A. | Concall; no entity-level cost lines. |
| F4 Unaudited contribution ratio | N.A. | Concall; no auditor Other Matters. |
| F5 Going concern / EoM scope | N.A. | Concall; no EoM paragraph. |
| F6 Forward-commitment mining | FINDING | 37 FORWARD rows mined (R209-R245). Findings C02, C03, C04, C06, C08, C14, C17. Register below. |
| F7 Hedge mining | FINDING | Safe harbour (lines 011-016, R274) is boilerplate. The material new hedge covers agri-equipment repayment and drought (line 201, R216), at C07. App stability hedge (line 623, R288) is folded into C08. |
| F8 Tax forensics | PASS | Spoken PAT 656 Mn / PBT 874 Mn gives ETR 24.9% for Q2. H1 1,270 / 1,696 gives 25.1% (my arithmetic). Both sit in line with the 25.17% statutory rate. Tax was not discussed. |
| F9 OCI forensics | N.A. | Concall; OCI not discussed. |
| F10 Share count and dilution | N.A. | Concall; no share count or EPS spoken. FCCB silence is logged at C13. |
| F11 Net worth tie-out | PASS | Spoken borrowings of 54,808 Mn at D/E 2.89x imply net worth of Rs1,896.5 Cr. Filed standalone net worth is Rs1,914.7 Cr (res:R379 + R381). The gap is 1.0%, inside 5% (my arithmetic). |
| F12 Segment forensics | N.A. | Single-segment lender; no segment data spoken. |
| F13 Board outcome | N.A. | Concall; no board outcomes discussed. |
| F14 Drafting inconsistencies (concall adaptation: spoken statement vs same-quarter filing) | FINDING | Findings C05, C10, C11. ASR-explainable mismatches are listed in section 4, not as findings. |
| F15 Entity list diffs | N.A. | Concall; no consolidation list. The entities named are partners, states and analysts. |
| F16 Presentation dropped/reframed | N.A. | Presentation-only check. The deck's "Record disbursements" line is cross-referenced at C05 for the presentation A3 run. |
| F17 Silence audit | FINDING | Findings C01, C09, C12, C13, C15, C16, C18. Table in section 3b. |

GATE A3: pass. No blank checks.

## 3a. COMMITMENT REGISTER (F6)

| # | commitment | implied date | turn / line ref | status word |
|---|---|---|---|---|
| 1 | Yields normalise; incremental interest income follows through | Q3-Q4 FY27 | R209 l.78; R230 l.423 | initiated |
| 2 | Finance cost vs income gap normalises | Q3-Q4 FY27 | R237 l.550-557 | initiated |
| 3 | NIM range-bound, closing at about 6% annualised | FY27 end (Mar-2027) | R225 l.377-379 | initiated (prior guide cited, absent from Q1 log [Notion-sourced]) |
| 4 | Cost of funds about 10.5% for the full year; 25-30 bps rise priced in | FY27 end (Mar-2027) | R223/R224 l.366-370; R244 l.646-654 | underway (cited as an existing guide) |
| 5 | Kharif outcome clear | end-Oct / early-Nov 2026 | R217/R257 l.212-213 | initiated |
| 6 | Rural cash flows improve after harvest; Bihar impact manageable | Q3 FY27 | R215 l.195; R218 l.214 | initiated |
| 7 | Headcount trend normalises (hiring resumes) | Q3 festive to end Q4 FY27 | R226/R263 l.390-391 | initiated |
| 8 | Consumer app release | end Q3 FY27, "Christmas or New Year", visible Q4 FY27 | R227/R264 l.394; R238/R266 l.580-586 | underway (guided in Q1 [Notion-sourced]) |
| 9 | Q4 used to stabilise app infrastructure across DP/BC/branches | Q4 FY27 | R240 l.589 | initiated |
| 10 | App metrics shared; QoQ comparisons begin | Q1 FY28 | R239/R267 l.582-583, 596-598 | initiated |
| 11 | BC, OEM and lender tie-ups push the app | Q1 FY28 | R241 l.618-619 | initiated |
| 12 | Small share of acquisition via app this year, if stable | FY27 | R242 l.626; R288 l.623 | initiated |
| 13 | 40-50% of acquisition via the consumer app | end of 3-year strategy (about FY30) | R243 l.629 | initiated |
| 14 | Operating leverage rises as the app and AI framework kick in | from Q3 FY27 end | R228 l.395; R231 l.438-440 | initiated |
| 15 | Short-term growth outpaces operating-leverage gains; frameworks align | Q1 FY28 | R232 l.485; R233/R265 l.487-489 | initiated |
| 16 | Doubling of "AUM revenue impact" | end of next 3 fiscal years (about FY30) | R234 l.490-494; R169 l.578-579 | underway (Q1 framework restated; PAT not restated) |
| 17 | Long-term ROE 15-18% sustained | undated | R235 l.499 | initiated |
| 18 | ROA 4-4.5% | undated | R236 l.502 | initiated |
| 19 | SBI and bank co-lending live once banks comply with the circular | undated | R229 l.403-406 | initiated (no change vs Q1, status quo) |
| 20 | Broaden the product suite, partnership-led, asset-light | undated (Q1 had "Q3 FY27-end") | R212 l.116-118 | initiated (date dropped) |
| 21 | H2 FY27 priorities: growth, funding efficiency, asset quality, returns | H2 FY27 | R221 l.316-322 | initiated |
| 22 | Public NCD Rs294.9 Cr under the Rs900 Cr shelf; Rs124.4 Cr unsecured PP; Rs177 Cr CP | H1 FY27 | R064-R067 l.071-075 | completed |

## 3b. WHAT WAS NOT DISCUSSED (F17 silence audit)

Consecutive-quarter count: Q2 FY27 = 1. Where the Notion Q1 log records the item as NOT ADDRESSED, the count is 2 [Notion-sourced]. Where Q1 status is not on record, the count shows "1 (Q1 not recorded)".

| Item | Source of the item | Q2 call status | Consecutive quarters silent | Metric direction | Finding |
|---|---|---|---|---|---|
| Fees and commission income, Rs Cr and share | Checklist #12; Q1 Q#2; thesis-broken (b) | Not mentioned | 2 | Deteriorating (down 39.6% YoY, 3.7% share) | C09 |
| Cost-to-income ratio | Checklist #7; Q1 Q#1; trigger (d) | Asked (l.448); no number given | 1 (Q1 answered about 40%) | Deteriorating (41.0% filed) | C01 |
| Standalone vs consolidated basis | Q1 Q#3 | Analyst used "consolidated" (l.521); not addressed | 2 | n/a | C18 |
| Own-book vs off-book disbursement split | Q1 Q#5 | Not addressed | 2 | n/a | C18 |
| SBI co-lending AUM and spread | Checklist #13; Q1 Q#6 | Qualitative "status quo" only (l.400-407) | 2 (quantified) | Stalled | C09 |
| PCR and write-offs | Early-warning #3; Q1 Q#7 (partial) | Not addressed | 2 | Unknown | C18 |
| DMD term forward-dating; NRC terms | Q1 Q#9 | Not addressed | 2 | n/a | C18 |
| Dividend quantum | Q1 Q#10 | Not addressed | 2 | n/a | C18 |
| Total Income QoQ dash | Q1 Q#11 | Not addressed | 2 (likely moot after the Reg 33 filing) | n/a | none |
| Reg 33 filing date | Q1 Q#8 | Resolved by the filing on 22-Oct (Notion Key Notes) | RESOLVED-BY-FILING | n/a | none |
| Promoter pledge; lender quality (Carwin/Bikewin) | Checklist #15; early-warning #7; 1-Jul and 4-Sep tripwires | Not mentioned | 1 (Q1 not recorded) | Rose to about 8.35% after 29-Sep top-ups; 7.68% post-conversion | C13 |
| Promoter holding or selling | Checklist #16 | Not mentioned | 1 (Q1 not recorded) | 46.50% Sep-end (Notion) | C13 |
| RPT borrowing usage | Checklist #17; early-warning #6 | Not mentioned | 1 (Q1 not recorded) | Unknown | C13 |
| FCCB conversion and share count | Checklist #20; Q1 guidance "conversion pending" | Not mentioned; FCCB omitted from the liability list (l.143-144) | 1 | Dilution occurred (res:R379 vs R384) | C13 |
| BSE Reg 60(2) fine | Notion Key Notes 23-Oct | Not mentioned | 1 | n/a | C13 |
| Rating action | Checklist #18 | Only "dual-rated" (l.072); no rating level | 1 (Q1 not recorded) | Stable (deck AA/Stable) | none |
| Leverage trend vs about 3.5x internal cap | Checklist #19; Q1 guidance | Level 2.89x only (l.311); cap not restated | 1 | Rising | C12 |
| LCR, cash, investments build | Notion §4 23-Oct | "positive gap across buckets" only (l.314-315) | 1 | LCR down to 2.22x; investments up about 9x | C12 |
| CAR decline (33.1% to 30.7%) | Checklist #9 | Level only (l.312) | 1 | Falling | C12 |
| Opex growth vs early-warning #5 (>35% YoY) | Early-warning #5 | Not quantified | 1 | 33% YoY, near the line | C02 |
| 3 new products by Q3 FY27-end | Q1 forward guidance | Undated restatement (l.116) | 1 (dated version) | n/a | C15 |
| Top-5 state concentration | Checklist #14 | State colour only (l.182-233) | 1 (Q1 not recorded) | Improving (87.7%) | none |

Addressed on the call: AUM (#1), GNPA (#2), NNPA (#3), collection efficiency (#4), cost of borrowing (#5), NIM (#6, basis caveat at C03), credit cost (#8, basis caveat at C07), CAR level (#9), ROA (#10), ROE (#11).

## 4. SPOKEN vs FILED (ASR reconciliation; not findings unless cited above)

| Spoken (line) | Filed | Read |
|---|---|---|
| AUM 72,659 Mn (257) | Rs7,265.9 Cr (Notion §4) | ties |
| Disbursement Q2 1,573 Mn, H1 3,292 Mn (261-262) | 15,673 Mn Q2; Q1 17,309 Mn; H1 32,982 Mn (deck:R005, R056, R057; my arithmetic) | ASR or unit error; the 42% YoY ties (11,025 to 15,673) |
| PBT 8,74 / PAT 6,56 Mn (276-277) | PAT Rs65.64 Cr (Notion Key Notes) | ties as 874 / 656 Mn |
| ROE 13.4%, ROA 3.3%, ROE Q2 FY26 11.8% (282-285) | deck:R107, R112, R622 | ties |
| Credit cost 0.4% Q2 FY27 vs 1.1% Q2 FY26 (296-298) | deck 0.4% / 1.0% (deck:R609, R610); P&L impairment write-back of Rs0.38 Cr (res:R110) | 10 bps prior-year gap may be ASR; P&L basis gap at C07 |
| H1 loan losses "1.55 / 2.95 million" (301-302) | standalone H1 Rs15.25 Cr / Rs24.11 Cr (res:R112, R117) | unit as spoken; the spoken -47% fits consolidated, not standalone (-36.7%, my arithmetic); unverified |
| CoB down "approximately 15 bps" YoY to 10% (307-308) | 10.5% to 10.0% = 50 bps (deck:R093, R097) | likely ASR (fifteen/fifty) |
| D/E 2.89x (311) | deck 2.89x; Reg 52 2.83x | basis gap belongs to results/deck A3 |
| NIM 5.7% (378) | deck 5.7% (yield less CoB); Reg 52 6.43% | basis conflict, C03 |
| Outbound calls 3,000,000 daily (125) vs 3 lakh (454) | 300K (deck:R437) | C11 |
| Q1 headcount down "about 3%" (387, 429) | Q1 log "headcount −2%" [Notion-sourced] | small gap; ASR possible |
| CoF 13% to 10% over five years (644) | 13.0% FY21 to 10.0% (deck:R217, R223) | ties |
| Quarter end "September 6" (034), "September 13" (293) | 30-Sep-2026 | ASR |

```yaml
stage: A3-forensics
company: "PAISALO"
quarter: "Q2 FY27"
doctype: "concall"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/paisalo-q2fy27/work/forensics_paisalo_q2fy27_concall.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: PASS
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
  - {id: "C01", check: "F17", line: "448; 485; 487", classification: "FORWARD-SIGNAL", implication: "C/I asked 3x, no ratio given; op-leverage dated to ~Q1 FY28; filed opex +33% YoY, C/I 41.0%; Q3 FY27 C/I >35% likely = second filed strike on trigger (d)"}
  - {id: "C02", check: "F6", line: "136-137; 390-391; 474", classification: "FORWARD-SIGNAL", implication: "Headcount -11% claimed as op leverage but employee cost +5.9% YoY, D&A +152%, other exp +39% (res:R134/R137/R146); hiring to resume Q3-Q4 while AI cost stays elevated; no brake on H2 opex"}
  - {id: "C03", check: "F6", line: "377-379", classification: "FORWARD-SIGNAL", implication: "NIM guide ~6% vs FY26 6.8% (deck basis) and current 5.7%; sits on checklist #6 red line; Reg 52 NIM 6.43% basis conflict pending ruling"}
  - {id: "C04", check: "F6", line: "366-372; 646-654", classification: "FORWARD-SIGNAL", implication: "CoF guided 10.0% -> 10.5%, reversing 5-yr decline, exactly at early-warning #4 (>10.5% pause); marginal paper 12% unsecured; with NIM 6% needs yield ~16.5% vs 15.7%"}
  - {id: "C05", check: "F14", line: "76-77; 420-422; 553-554", classification: "AMBIGUOUS", implication: "Two causes given for yield drop; deck 'record disbursements' vs filed Q2 disb -9.5% QoQ; yield down 2 straight quarters (16.7 -> 15.7); 'typical Q1-Q2' not in deck series; Q3 yield tests transience"}
  - {id: "C06", check: "F6", line: "520-524; 546-557", classification: "FORWARD-SIGNAL", implication: "Finance cost +34.2% vs total income +26.2% YoY standalone; promised to normalise Q3-Q4; investments 19.8 -> 175.5 Cr unexplained; persistence = structural negative carry"}
  - {id: "C07", check: "F7", line: "182; 201-202; 381", classification: "FORWARD-SIGNAL", implication: "Maharashtra (20.1% AUM) drought, half-yearly agri instalments due post-Kharif; Q2 impairment a Rs0.38 Cr write-back vs Rs15.63 Cr Q1 flattered PAT; Q3 credit cost skewed up"}
  - {id: "C08", check: "F6", line: "394; 580-595; 618-626", classification: "AMBIGUOUS", implication: "App: end-Q3 vs Christmas/New Year; visible Q4, metrics and channel push Q1 FY28, conditional on stability; catalyst moved right one quarter without admitted slip"}
  - {id: "C09", check: "F17", line: "400-407", classification: "CONFIRMATORY-NEGATIVE", implication: "SBI co-lending status quo 2nd straight quarter; fee income unmentioned 2 quarters while filed fees -39.6% YoY at 3.7% of income vs >5% by Q4 FY27 path"}
  - {id: "C10", check: "F14", line: "499-505; 282", classification: "AMBIGUOUS", implication: "ROE 15-18% / ROA 4-4.5% targets undated; filed ROE flat ~13% since FY24, ROA falling 4.5 -> 3.3; spoken history garbled (R286); ROE held by leverage"}
  - {id: "C11", check: "F14", line: "125; 454; 458-461; 469-470", classification: "AMBIGUOUS", implication: "AI metrics conflict with deck (3,000,000 vs 300K calls; zero vs 3 Q1 bots); AI credited for Q1 headcount cut with ~zero bots; efficiency evidence is activity, not cost"}
  - {id: "C12", check: "F17", line: "311-315; 323-325", classification: "AMBIGUOUS", implication: "D/E 2.43 -> 2.61 -> 2.89x, CAR 33.1 -> 30.7%, LCR 2.22x vs 8.3x, investments up ~9x stated as levels or not at all; internal cap ~3.5x not restated"}
  - {id: "C13", check: "F17", line: "005; 143-145; 661", classification: "CONFIRMATORY-NEGATIVE", implication: "Pledge top-ups by call-lead DMD, FCCB conversion (paid-up 9,095.84 -> 9,142.11 lakh), BSE fine all unmentioned; FCCB omitted from liability pillar"}
  - {id: "C14", check: "F6", line: "490-494; 576-579", classification: "AMBIGUOUS", implication: "Q1 'double AUM/income/PAT ~3 yrs' restated as 'AUM revenue impact', PAT dropped; implies ~26% CAGR vs 33% now; full op leverage pushed to ~FY30"}
  - {id: "C15", check: "F17", line: "116-118", classification: "AMBIGUOUS", implication: "Q1 dated '3 new products by Q3 FY27-end' now undated intent; dated promise dropped"}
  - {id: "C16", check: "F17", line: "005; 028-029", classification: "NEUTRAL-FACT", implication: "Promoter-CMD absent from roster per filed intimation; DMD led; no prior roster to trend"}
  - {id: "C17", check: "F6", line: "071-075", classification: "NEUTRAL-FACT", implication: "Q1 funding commitments completed: public NCD Rs294.9 Cr, unsecured PP Rs124.4 Cr, CP Rs177 Cr"}
  - {id: "C18", check: "F17", line: "521; 661", classification: "CONFIRMATORY-NEGATIVE", implication: "Five Q1 open questions unaddressed 2nd quarter: S vs C basis, own vs off-book, PCR/write-offs, DMD term/NRC, dividend"}
forward_signals: ["C01", "C02", "C03", "C04", "C06", "C07"]
ambiguous: ["C05", "C08", "C10", "C11", "C12", "C14", "C15"]
commitments:
  - {commitment: "Yields normalise; incremental interest income follows", implied_date: "Q3-Q4 FY27", ref: "R209 l.78; R230 l.423", status_word: "initiated"}
  - {commitment: "Finance cost vs income gap normalises", implied_date: "Q3-Q4 FY27", ref: "R237 l.550-557", status_word: "initiated"}
  - {commitment: "NIM about 6% annualised at close", implied_date: "FY27 end", ref: "R225 l.377-379", status_word: "initiated"}
  - {commitment: "Cost of funds about 10.5% full year", implied_date: "FY27 end", ref: "R224 l.370; R244 l.646-654", status_word: "underway"}
  - {commitment: "Kharif outcome clear", implied_date: "end-Oct / early-Nov 2026", ref: "R217 l.212-213", status_word: "initiated"}
  - {commitment: "Rural cash flows improve post harvest; Bihar manageable", implied_date: "Q3 FY27", ref: "R215 l.195; R218 l.214", status_word: "initiated"}
  - {commitment: "Headcount trend normalises (hiring resumes)", implied_date: "Q3-Q4 FY27", ref: "R226 l.390-391", status_word: "initiated"}
  - {commitment: "Consumer app release", implied_date: "end Q3 FY27 / New Year; visible Q4 FY27", ref: "R227 l.394; R238 l.580-586", status_word: "underway"}
  - {commitment: "Q4 used to stabilise app infrastructure", implied_date: "Q4 FY27", ref: "R240 l.589", status_word: "initiated"}
  - {commitment: "App metrics shared", implied_date: "Q1 FY28", ref: "R239 l.582-583", status_word: "initiated"}
  - {commitment: "BC/OEM/lender tie-ups push app", implied_date: "Q1 FY28", ref: "R241 l.618-619", status_word: "initiated"}
  - {commitment: "Small share of acquisition via app this year, if stable", implied_date: "FY27", ref: "R242 l.626", status_word: "initiated"}
  - {commitment: "40-50% of acquisition via consumer app", implied_date: "end of 3-yr strategy (~FY30)", ref: "R243 l.629", status_word: "initiated"}
  - {commitment: "Operating leverage rises as app and AI kick in", implied_date: "from Q3 FY27 end", ref: "R231 l.438-440", status_word: "initiated"}
  - {commitment: "Frameworks align; op-leverage impact visible", implied_date: "Q1 FY28", ref: "R233 l.487-489", status_word: "initiated"}
  - {commitment: "Doubling of AUM revenue impact", implied_date: "~FY30", ref: "R234 l.490-494", status_word: "underway"}
  - {commitment: "ROE 15-18% sustained", implied_date: "undated", ref: "R235 l.499", status_word: "initiated"}
  - {commitment: "ROA 4-4.5%", implied_date: "undated", ref: "R236 l.502", status_word: "initiated"}
  - {commitment: "Co-lending live once banks comply", implied_date: "undated", ref: "R229 l.403-406", status_word: "initiated"}
  - {commitment: "Broaden product suite (Q1 date dropped)", implied_date: "undated", ref: "R212 l.116-118", status_word: "initiated"}
  - {commitment: "H2 FY27 priorities: growth, funding efficiency, AQ, returns", implied_date: "H2 FY27", ref: "R221 l.316-322", status_word: "initiated"}
  - {commitment: "Public NCD Rs294.9 Cr, unsecured PP Rs124.4 Cr, CP Rs177 Cr", implied_date: "H1 FY27", ref: "R064-R067 l.071-075", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "The call guides every spread input against the thesis at once. CoF rises 50 bps to the 10.5% tripwire (C04), NIM is re-anchored near 6% versus 6.8% FY26 (C03), and the op-leverage payoff is dated to about Q1 FY28 (C01). Hiring resumes in Q3-Q4 (C02). Read together, Q3 FY27 cost-to-income very likely stays above 35%, the second filed-basis strike on trigger (d). The 4-4.5% ROA target has no bridge from these inputs (C10). Q2 PAT growth also leaned on a provision write-back in the quarter management named drought stress in Maharashtra, 20.1% of AUM (C07). Q3 therefore tests three management claims at once: yield transience (C05), carry normalisation (C06) and agri repayment (C07). F14 is used here as a concall adaptation, spoken statement versus same-quarter filing. ASR-explainable gaps stay in section 4 and are not findings. All Q1 diffs rest on Notion text, with no prior transcript."
```
