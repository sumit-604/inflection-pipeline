# STAGE 12 VERIFIER B: CONCALL RED FLAGS — SHAREINDIA (run 2026-09-19)

Model: claude-opus-5. Fresh context. Phase 1 scope.
Inputs read: 3 main-company transcripts (Q3 FY26 call 28-Jan-2026, Q4 FY26 call
20-May-2026, Q1 FY27 call 27-Jul-2026), 12 peer transcripts (SMCGLOBAL x4,
CHOICEIN x4, ANGELONE x4; SMC Q4 FY26 and Q1 FY27 read in full, others read at
the passages bearing on Share India's claims), then B05 (05-concall.md) and B06
(06-peers.md). The Q2 FY26 context file (inputs/other) was opened only to trace
one B05 quote.

Anchor convention: `[page N]` = the page marker in the pre-extracted .txt;
`L` = line number in that .txt. Q3 = SHAREINDIA-concall-Q3FY26-2026-01-30.txt,
Q4 = SHAREINDIA-concall-Q4FY26-2026-05-23.txt, Q1 = SHAREINDIA-concall-Q1FY27-2026-07-31.txt.
All rupee figures in Rs Cr as spoken on the call.

---

## 1. INDEPENDENT RED-FLAG LIST (from the raw transcripts, before reading B05/B06)

Severity is graded on the common scale. Material = CRITICAL + MAJOR.

| # | Sev | Item | Anchor (call, speaker, location) |
|---|---|---|---|
| I1 | CRITICAL | **Prop-vs-client split: shifting answers across two quarters, under repeated analyst insistence.** Q4: prop = "around 70% of the revenue", profit share 49% consol / 52% standalone; client turnover ">53%" vs prop 47%. Q4 (Urmesh Shah asks for a ballpark): "share broking business diversification is a number that we don't share". Q1: prop "around 52%" of profit (basis unstated), then "58% to 60%" of revenue, and Kamlesh says 60/40 client/prop by volume. Prop revenue share moves 70% -> 58-60% in 68 days with no explanation. Four analysts press the point (Abhijit Sakhare, Urmesh Shah in Q4; Rohan, Chirag Sehgal in Q1). | Q4 Abhinav Gupta [page 13] L453-459; Sachin Gupta [page 13] L465-468; Abhinav [page 16] L576-577; Abhinav [page 17] L605-607. Q1 Abhinav [page 10] L408-409; Kamlesh Shah [page 12] L469-470; Abhinav [page 12] L483-484 |
| I2 | MAJOR | **Prop profit share shows no progress against management's own FY27 target.** Q4 target: client profit "more than 50%, or 55% and 45% from the prop side" by end FY27; prop to ~30% of profit in 3 years. Q1: prop "around 52%" of profit, the same figure as Q4 standalone. On the one metric management set a dated target for, the needle has not moved. | Q4 Sachin [page 16] L589-593, Abhinav [page 17] L605-607; Q1 Abhinav [page 10] L408-409 |
| I3 | MAJOR | **MTF target goalpost moves every quarter; the book is not on the glide path.** Q3: double to Rs 900-1,000 Cr in "next two years" (from Jan-2026). Q4: Sachin says Rs 650 Cr by FY27, then Abhinav in the SAME call says Rs 650 Cr "by the Fiscal Year '28". Q1: Rs 1,000 Cr "in next two years" (now from Jul-2026, a 6-month slide). Actual: Rs 457 Cr (Dec-25) -> Rs 424 Cr (Mar-26) -> Rs 470 Cr / "465 odd" (Jun-26): +3% in six months against a doubling target. | Q3 Sachin [page 10] L455-469; Q4 Sachin [page 8] L270-272, Urmesh/Sachin [page 17] L608-611, Abhinav [page 12] L424-425, Abhinav [page 18] L636-637; Q1 Sachin [page 5] L193-198, Abhinav [page 10] L395 |
| I4 | MAJOR | **Every dated new-initiative milestone set in Q3 FY26 slipped.** Silverleaf NCLT (by end Q4 FY26, missed twice); uTrade multi-broker (FY27, dropped); PMS ("next 10 to 15 days" in Jan-26; Q4 says "started in this quarter", Q1 says "launched our PMS in Q1"); wealth distribution ("from the Q1 of next financial year" -> "first month of Q3" -> "by Q3"); AIF (approval end Q2 -> launch Q3). Each slip is explained by a regulator, a court or a circular; none is acknowledged as a slip. | Q3 Sachin [page 5] L237-245, [page 6] L272-276, [page 8] L366-369; Q4 Sachin [page 6-7] L222-238, [page 9] L312-313, [page 11] L389-401; Q1 Sachin [page 5] L202-208, [page 6-7] L255-260 |
| I5 | MAJOR | **uTrade revenue / monetization evaded in two consecutive calls; multi-broker plan walked back.** Q3 Rohan asks revenue and run rate: only "2x to 3x" aspiration. Q4 Murtaza asks the monetization model: Sachin answers the partnership half, then "And what was your second question?" and moves on; later "It is still not a big number in terms of revenue. Right now, revenue is not the focus." | Q3 Sachin [page 8] L361-369; Q4 Sachin [page 11] L389-401, [page 19-20] L701-705 |
| I6 | MAJOR | **Silverleaf merger: NCLT date missed twice, then status goes silent while the MD speaks of it as done.** Q3: NCLT approval "by end of this quarter". Q4: "still in NCLT... maximum quarter's time". Q1: no status; Abhinav gives history only; Kamlesh: "Even acquisition of Silverleaf... has added our strength in terms of technology and delivery" (present-perfect framing of a pending merger). | Q3 Sachin [page 6] L272-276; Q4 Sachin [page 9] L312-313; Q1 Abhinav [page 9] L366-374, Kamlesh [page 13] L513-514 |
| I7 | MAJOR | **Consolidated earnings swing on unquantified fair-value moves.** Q4: consolidated "relatively subdued... primarily due to weak market conditions and fair value adjustments relating to the investment held by group companies"; FY26 consol PAT Rs 324 Cr vs Rs 328 Cr. Q1: consol PAT Rs 124.41 Cr, "+114% sequential", "strongest quarterly financial performance to date"; Sachin concedes "definitely some impact of the valuation... some positive impact at least". The MTM share of the record quarter is never quantified. | Q4 Kamlesh [page 4] L152-154, [page 5] L161-165; Q1 Kamlesh [page 3] L104-117, Sachin [page 10-11] L417-422 |
| I8 | MAJOR | **Peer contradiction: "Tier-3 vacuum... no supply" for MTF.** Share India Q4: "Tier-3 cities there is still lot of demand and there is no supply... there is a vacuum"; Q1: "there is a vacuum on the ground". Choice (Feb-26): Tier-3-and-below "require a physical presence" and Choice has branches + AP network there; Choice (Aug-26): 210-220 branches, 300-350 by Mar-27, 800 in 3-4 yrs. Angel One (Jan-26): assisted channel gives "really good growth" in "Tier 2, Tier 3 and beyond"; present in "19,000 PIN codes". | Q4 Sachin [page 8] L287-290; Q1 Sachin [page 7] L287-289; CHOICEIN-2026-02-11 [page 6] L224-236; CHOICEIN-2026-08-17 L487-498; ANGELONE-2026-01-21 [page 12] L544-546, [page 17] L727 |
| I9 | MAJOR | **Peer contradiction: algo-trading "USP... Nobody is offering this product" / "unique advantage of algo trading".** SMC (Feb-26): "we are even going to integrate algo trading into our mobile trading". SMC (Jul-26): has "launched... AI-based Algo platform". The moat claim is repeated by Sachin (Q4) and Kamlesh (Q1, twice). | Q4 Sachin [page 7-8] L259-260; Q1 Kamlesh [page 9] L358, [page 13] L511; SMCGLOBAL-2026-02-09 [page 6] L218-222; SMCGLOBAL-2026-07-31 [page 10] L352-355 |
| I10 | MAJOR | **Peer MTF books grow faster than Share India's, undercutting the "network advantage" framing.** SMC Q1 FY27: MTF + T+5 book "from 760 crores to more than 900 crores" in one quarter (~+18%). Choice Feb-26: MTF average book Rs 370-400 Cr, "grow the MTF book very aggressively". Angel One Q3 FY26: book "+10% quarter-over-quarter". Share India: +3% over the same six months, called "mild growth". | SMCGLOBAL-2026-07-31 [page 7] L271-272; CHOICEIN-2026-02-11 [page 6] L233-236; ANGELONE-2026-01-21 [page 17] L707-708; Q1 Sachin [page 5] L195-198 |
| I11 | MINOR | Wealth distribution launch slid Q1 FY27 -> Q3 FY27 with no acknowledgement; Q3 FY26 had promised "good numbers" from third-party distribution in FY27. | Q3 Sachin [page 5] L237-242; Q4 Sachin [page 6] L222-228; Q1 Sachin [page 6-7] L255-260 |
| I12 | MINOR | AIF: approval "by end of Q2" (Q4) -> "still working with the regulatory things... launch in Q3" (Q1). | Q4 Sachin [page 7] L236-238; Q1 Sachin [page 5] L207-208, Abhinav [page 9] L339-341 |
| I13 | MINOR | RBI curb tone shift. Q4: "no materialistic impact on Share India's bottom line", "absolutely nothing to worry", minimum impact "up to March 2027". Q1: CP and NCD programmes launched "to counter the RBI measures which restricted [prop] desk funding". | Q4 Sachin [page 14] L519-521, Kamlesh [page 21-22] L771-779; Q1 Kamlesh [page 4] L147-149 |
| I14 | MINOR | Enshrine acquisition: "up to Rs 45 Cr" for a company with Rs 2-3.0 Cr turnover; rationale is an office property (~18,000 sq ft). Analyst had to ask why. Capital into own-use real estate. | Q1 Chirag Sehgal / Kamlesh [page 11] L438-458 |
| I15 | MINOR | Speakers contradict each other on insurance. Sachin: "Revenues have not shown any decline. Revenues are up." Abhinav, next: YoY "there might be a little drop". | Q3 [page 8] L398-399; [page 9] L402-409 |
| I16 | MINOR | Q4 opening numbers are internally impossible: standalone Q4 revenue "INR 383 crore" but FY revenue "INR 395 crore"; quarterly EPS "INR 17.6" (Q3 quarterly EPS was Rs 3.69 on Rs 81 Cr PAT). The MD's read-out cannot be relied on. | Q4 Kamlesh [page 4] L139-148; Q3 Kamlesh [page 3] L136-137 |
| I17 | MINOR | Volunteered negative: retail "number of clients is not increasing at all", clients closing accounts; active equity clients +1% QoQ. | Q3 Sachin [page 5] L213-221 |
| I18 | MINOR | NBFC: NIMs to fall "a few more hundred basis points"; NPA up Q3 vs Q2 on unsecured defaults; branch network downsized; Rs ~100 Cr of Rs ~250 Cr book still unsecured; Q4 NIM 17.64% "will go down". | Q3 Abhinav [page 7] L305-331; Q4 Abhinav [page 18] L655-665 |
| I19 | MINOR | Share India Cred run rate. Q4 (20-May): "already we have closed six issues till now", target Rs 500 Cr in FY27. Q1: six issues and Rs 74 Cr underwritten for the whole quarter, implying no issue from 20-May to 30-Jun; the rest of FY27 needs ~Rs 142 Cr per quarter. | Q4 Sachin [page 7] L246-248; Q1 Sachin [page 6] L221-226 |
| I20 | MINOR | PMS metric broadened: Q4 "PMS... more than INR 100 crore"; Q1 "PMS AUM and the direct PMS and advisory stands at Rs. 150 crores". Launch quarter stated as Q4 FY26 in one call and Q1 FY27 in the next. | Q4 Sachin [page 7] L229-235; Q1 Sachin [page 5] L202-204 |
| I21 | MINOR | Margin guidance restated. Q3: "operating profit margin 43%, net profit margin 24%". Q4: "EBITDA of around 38% (+/-2%) and PAT margin of around 22% (+/-2%)... the broader guideline from the very beginning". | Q3 Kamlesh [page 4] L152-153; Q4 Abhinav [page 10] L353-356 |
| I22 | MINOR | Branch disclosure. Revenue per branch declined ("not a metric that we look at"), promised for future presentations. Branch economics restated: Q4 "10 to 15 crore MTF in a year" per branch; Q1 "15 Cr MTF book in the first 8 months" to break even. | Q4 Sachin [page 19] L670-676, Abhinav [page 19] L691-692, Sachin [page 19-20] L697-713; Q1 Sachin [page 7] L282-285 |
| I23 | MINOR | MTF spread question deflected. Murtaza asks at what AUM the interest spread becomes meaningful; Abhinav opens "that would be a very kind of an unfair statement"; no spread or break-even AUM given. | Q4 [page 11-12] L402-425 |
| I24 | MINOR | Institutional metric switches base: Q3 "active clients... from 154 to 174"; Q4 "empanelment... from 137 to 186"; Q1 "active clients stand at 212 versus 186". | Q3 Sachin [page 5] L222-224; Q4 Sachin [page 8-9] L294-298; Q1 Sachin [page 5] L213 |
| I25 | MINOR | Defensive rebuttal of analyst data: "I'm sorry to cut you off on this. I'm not sure where you're getting your data from". | Q1 Abhinav [page 12] L490 |
| I26 | MINOR | Stock-price / low-PE question deflected as "hypothetical". | Q1 Sachin [page 8] L321-329 |
| I27 | MINOR | "We have performed far, far better [than peers]": no metric, no peer named. | Q1 Kamlesh [page 9] L352-353 |
| I28 | MINOR | Branch count flat: seven branches named in Q4 and the same seven in Q1 (Q4 also says "6 branches" then names 7). | Q4 Sachin [page 8] L277-281; Q1 Sachin [page 5] L186-191 |

Count: 28 items. Material: 10 (1 CRITICAL, 9 MAJOR). Minor: 18.

---

## 2. COMPARISON AGAINST THE PIPELINE (B05, B06)

### 2A. My items vs pipeline

| # | Sev | Status | Pipeline location / gap |
|---|---|---|---|
| I1 | CRITICAL | CAUGHT | B05 4D HIGH, 1C, 2C, 2D. Weight is right. Defect: B05 2C attributes "52% standalone / 49% consolidated" to Q1 FY27; the transcript has it in Q4 FY26 [page 17] L605-607. B05 never cites the Q4 "70% of revenue" figure, so the 70% -> 58-60% revenue jump inside 68 days is not on the record. |
| I2 | MAJOR | MISSED | B05 1B records the Q4 target as "Client 60% / prop 40%, profitability". The transcript sets 60/40 for TURNOVER and 55/45 for PROFIT ([page 16] L589-593). B05 2A then scores the volume claim as "Delivered". The flat profit share (52% -> ~52%) is not flagged anywhere. |
| I3 | MAJOR | MISSED | B05 1C: "No slippage"; 2A: "Delivered (on track)"; 4A ranks MTF trigger #1. Abhinav's "FY28" restatement and the Jul-2026 reset of the two-year clock are absent. +3% in six months is not on a doubling path. |
| I4 | MAJOR | PARTIALLY CAUGHT | B05 caught Silverleaf, uTrade, AIF individually and 2B classifies excuses as external-blame-heavy. It labels PMS "genuine, ahead-of-plan" and wealth "Planned" with no slip, so the five-for-five slip pattern is not stated. |
| I5 | MAJOR | CAUGHT | B05 2E ("Deflected every time"), 3C, 4D MEDIUM. |
| I6 | MAJOR | CAUGHT | B05 1C, 2A, 4D LOW-MEDIUM, 4A #5. Kamlesh's "done" framing in Q1 [page 13] L513-514 not noted; the flag survives without it. |
| I7 | MAJOR | MISSED | No mention of fair-value / valuation effects in B05 or B06. B05 cites "strongest quarterly performance to date" as over-promotion only. |
| I8 | MAJOR | PARTIALLY CAUGHT | B06 2C documents Choice's 800-branch plan and Angel's AP reach, but reads them as "directionally industry-validated". It does not test Share India's "no supply / vacuum" claim against them. They contradict it. |
| I9 | MAJOR | MISSED | B06 Q5 cites the SMC Feb-26 algo passage only for the circular question. It does not test the "nobody is offering this product" claim, and it does not cite SMC's Jul-26 AI-based algo platform launch. |
| I10 | MAJOR | MISSED | B06 Q3 "Peers silent": "Neither SMC Global nor Choice International discusses MTF pricing... (no MTF product line disclosed by either in the corpus)". False. SMC SMCGLOBAL-2026-07-31 [page 7] L271-272 and Choice CHOICEIN-2026-02-11 [page 6] L233-236 both disclose MTF books. |
| I11 | MINOR | MISSED | B05 1A: "Planned (team hired, ops by Q3 FY27)". No slip noted. |
| I12 | MINOR | CAUGHT | B05 1C, 2A. |
| I13 | MINOR | PARTIALLY CAUGHT | B05 1C: "consistent explanation across two quarters; no slippage". The Q1 CP/NCD "to counter" language is logged in 3B but the tone shift is not read. |
| I14 | MINOR | PARTIALLY CAUGHT | B05 1B, 2A log the price and close. The turnover-vs-price question and the real-estate use of capital are not flagged. |
| I15 | MINOR | MISSED | B05 2A tracks the insurance growth promise only. |
| I16 | MINOR | MISSED | — |
| I17 | MINOR | MISSED | — |
| I18 | MINOR | MISSED | B05 has no NBFC reading. B06 2E states Share India's lending is "never discussed in asset-quality terms". Q3 had a direct NPA Q&A (see 2B). |
| I19 | MINOR | MISSED | B05 1A: "Committed, delivering". |
| I20 | MINOR | MISSED | B05 1C: "Genuine, quantified, ahead-of-plan delivery". |
| I21 | MINOR | MISSED | B05 1B takes 38%/22% as "Standing (repeated as 'from the beginning')". It does not note that Q3 printed 43%/24%. |
| I22 | MINOR | MISSED | B05 1B calls Q1 branch economics "new, first time quantified". Q4 had already given 10-15 Cr MTF a year per branch. |
| I23 | MINOR | MISSED | — |
| I24 | MINOR | PARTIALLY CAUGHT | B05 3D merges active-client and empanelment counts into one series and calls it "the single cleanest delivering metric". |
| I25 | MINOR | CAUGHT | B05 2C Defensiveness. |
| I26 | MINOR | CAUGHT | B05 3C. |
| I27 | MINOR | CAUGHT | B05 3A, 4D LOW; B06 2A. |
| I28 | MINOR | CAUGHT | B05 1C, 2A, 4A. |

Totals: CAUGHT 8, PARTIALLY CAUGHT 5, MISSED 15.

### 2B. Pipeline red flags and claims I did not find, or that the transcript does not support

| Pipeline item | Verdict | Evidence |
|---|---|---|
| B05 4D MEDIUM: cash flow, contingent liabilities, pledge, NCD early redemption never raised on the calls | SUPPORTED (as a silence) | None of the three transcripts mentions pledge, operating cash flow, contingent liabilities or NCD early redemption. Q1 mentions only a new NCD issuance programme ([page 3] L129-131). The underlying numbers come from B01/B03, outside this verifier's scope. |
| B05 1C / 2C: no revenue number for uTrade or Algowire in three calls | SUPPORTED | Q3 [page 8] L340-379; Q4 [page 19-20] L701-705. |
| B05 3B: SEBI prop-cap answer framed by management as "more of a media hype than regulatory action" (attributed to Q4 FY26, Sanjeev Pandya) | NOT SUPPORTED as attributed | "Media hype" appears only in the Q2 FY26 context call, on weekly option expiries (inputs/other/SHAREINDIA-concall-Q2FY26-2025-11-04.txt [page 13] L526, L535). The Q4 answer is "there is nothing like that... there is no such cap" ([page 15] L539-545). Not a red flag in itself, so graded MINOR. |
| B05 1C: RBI curb "25-30% intraday-limit impact" | OVERSTATED | Q4 Abhinav corrects the analyst's "20%, 30%": "the number that has been stated in this call is around 20%" ([page 20] L722-723). B05 1B itself says 20%. |
| B06 Q3: "no MTF product line disclosed by either [SMC, Choice] in the corpus" | NOT SUPPORTED | SMCGLOBAL-2026-07-31 [page 7] L271-272 (MTF 760 -> 900+ Cr); CHOICEIN-2026-02-11 [page 6] L233-236 (MTF 370-400 Cr); CHOICEIN-2026-08-17 L176 (IPO funds to MTF). The false silence hides the contradiction in I10. |
| B06 2E: Share India lending "never discussed in asset-quality terms (GNPA/NNPA equivalent)" | OVERSTATED | True for MTF and Share India Cred. But Q3 has a direct NBFC NPA Q&A ([page 7] L322-331) and Q4 a NIM Q&A ([page 18] L655-665). |
| B06 Part 5: Angel One "content to let market share 'stagnate' (its own CFO's word, per Q4 FY26)" | NOT SUPPORTED | "Stagnated" is the analyst's word (Sanketh Godha, ANGELONE-2026-04-22 [page 12] L535-537). CEO Ambarish Kenghe rebuts it with share gains ([page 12-13] L545-572). The hypothesis leans on a misattributed quote. It is a peer characterisation, not a flag on Share India, so graded MINOR. |
| B06 2C: Choice 800 branches in 3-4 yrs, 210-220 now, 300-350 by Mar-27 | SUPPORTED | CHOICEIN-2026-08-17 L487-498. |
| B06 Q2: Angel One disclosed the RBI curb and bank-guarantee workaround before Share India's call | SUPPORTED | ANGELONE-2026-04-22 [page 6] L297-302. |

---

## 3. PROMISE-DELIVERY SPOT CHECKS (B05 2A)

| B05 row | B05 outcome | Earlier call has the promise? | Later call shows the outcome? | Verdict |
|---|---|---|---|---|
| Silverleaf NCLT by end Q4 FY26 | Missed | Yes: Q3 [page 6] L272-274 | Yes: Q4 [page 9] L312-313, still in NCLT | CONFIRMED |
| uTrade multi-broker, 2x-3x in 1-2 yrs | Missed | Yes: Q3 [page 8] L366-369 | Yes: Q4 [page 11] L389-401, "facing some challenges" | CONFIRMED |
| MTF Rs 900-1,000 Cr in two years | Delivered (on track) | Yes: Q3 [page 10] L455-457 | No. Book 457 -> 424 -> 470 (+3% in 6 months). Target restated to 650 by FY27/FY28 (Q4) and the two-year clock reset (Q1) | WRONG. Should read "Off track; target restated" |
| PMS FY27 AUM Rs 200 Cr | Delivered (exceeding) | Yes: Q4 [page 7] L230-235 | Yes, with a caveat: Q1 Rs 150 Cr includes "direct PMS and advisory" ([page 5] L202-204) | CONFIRMED (direction). Metric broadened |
| AIF approval end Q2, ops in FY27 | Partial (slipping) | Yes: Q4 [page 7] L236-238 | Yes: Q1 launch "in Q3" ([page 5] L207-208) | CONFIRMED |

Checked 5, confirmed 4, wrong 1. The wrong row is B05's number-one trigger.

---

## 4. CREDIBILITY GRADE

B05 overall grade C: **concur**. The C holds, but for partly different reasons. B05's "Good" sub-rating for operational guidance delivery is overstated. The MTF glide path is off track, and every dated new-initiative milestone from Q3 FY26 slipped. The fair-value swing (I7) also means the record Q1 FY27 print cannot yet be taken as clean operating delivery. Offsetting that, management volunteered real negatives: NBFC NPA and NIM, flat retail clients, GIFT City's past losses. That keeps the grade from falling to D.

---

## 5. CONSOLIDATED FINDINGS

| Sev | Location | Finding |
|---|---|---|
| MAJOR | B05 1C, 2A, 4A #1 | MTF trigger scored "No slippage" / "Delivered (on track)". The transcript shows the target restated each quarter (Abhinav: FY28) and the book up +3% in 6 months. (I3; spot check wrong) |
| MAJOR | B05 1B, 2A | Q4 profit-mix target misrecorded as 60/40 (it is 55/45 profit; 60/40 is turnover). The flat prop profit share (~52%) is not flagged. (I2) |
| MAJOR | B05 (absent) | Fair-value / valuation contribution to Q4 weakness and the record Q1 consolidated PAT is not identified. (I7) |
| MAJOR | B06 Q3 "Peers silent" | NOT SUPPORTED: SMC and Choice both disclose MTF books. Peer MTF outgrowth (SMC +~18% in Q1 FY27) is missed. (I10) |
| MAJOR | B06 Q5 | SMC's retail algo integration (Feb-26) and AI algo platform launch (Jul-26) contradict Share India's "nobody is offering this product" claim. Not tested. (I9) |
| MAJOR | B06 2C | Choice and Angel Tier-3 evidence is logged but not set against Share India's "no supply / vacuum" claim. PARTIALLY CAUGHT. (I8) |
| MAJOR | B05 1C, 2A, 2B | Five-for-five slip pattern on Q3 FY26 dated milestones is not stated. PMS called "ahead-of-plan", wealth not tracked. PARTIALLY CAUGHT. (I4) |
| MINOR | B05 1A | Wealth distribution Q1 -> Q3 FY27 slip not flagged. (I11) |
| MINOR | B05 1C | RBI curb read as "no slippage". Q1 CP/NCD "to counter" language is a tone shift. Also the "25-30%" misstatement (transcript: ~20%). (I13) |
| MINOR | B05 1B, 2A | Enshrine acquisition logged as "Delivered" without the turnover-vs-price or capital-use question. (I14) |
| MINOR | B05 (absent) | Q3 Sachin vs Abhinav contradiction on insurance revenue. (I15) |
| MINOR | B05 (absent) | Q4 opening-remark numbers internally impossible (quarter Rs 383 Cr vs FY Rs 395 Cr; EPS 17.6). (I16) |
| MINOR | B05 (absent) | Volunteered retail-client stagnation, Q3. (I17) |
| MINOR | B05 (absent); B06 2E | NBFC NIM/NPA negatives missed. B06 2E overstates "never discussed in asset-quality terms". (I18) |
| MINOR | B05 1A | Share India Cred "delivering": run rate vs Rs 500 Cr target and the six-issue overlap not checked. (I19) |
| MINOR | B05 1C | PMS "genuine" delivery: Q1 figure broadened to include advisory; launch quarter inconsistent. (I20) |
| MINOR | B05 1B | Margin guidance 43%/24% (Q3) vs 38%/22% "from the very beginning" (Q4) not noted. (I21) |
| MINOR | B05 1B | Branch economics called "first time quantified" in Q1; Q4 already gave 10-15 Cr MTF a year per branch. Branch revenue disclosure declined. (I22) |
| MINOR | B05 (absent) | MTF spread / break-even AUM question deflected ("unfair statement"). (I23) |
| MINOR | B05 3D | Active-client and empanelment counts merged into one series. (I24) |
| MINOR | B05 2C, 3B | Attribution errors: "52%/49%" placed in Q1 (it is Q4); "media hype" quote placed in Q4 on the prop cap (it is Q2 FY26 context, on weekly expiries). |
| MINOR | B06 Part 5, 2A | "Stagnate" attributed to Angel One's CFO. It is the analyst's word, and the CEO rebutted it. |

Counts: CRITICAL 0, MAJOR 7, MINOR 15.

No MISSED item is a repeated evasion, so no finding reaches CRITICAL under rule 5. The one repeated evasion (I1, prop split) and the one repeated deflection (I5, uTrade) were both caught.

---

## 6. SCORING

- Independent items: 28. Material (CRITICAL + MAJOR): 10.
- Material caught by the pipeline: I1, I5, I6 CAUGHT; I4, I8 PARTIALLY CAUGHT. Partial catches count as "already had", because the pipeline found the item and under-weighted it. Material caught = 5.
- acceptance_rate = 5 / 10 = 50%. On CAUGHT alone it is 3 / 10 = 30%.
- The denominator is 10, which is 4 or more, so the rate is valid under rule 7. It is below 60%.

```yaml
stage: B12b
company: "SHAREINDIA"
run_date: "2026-09-19"
model: "claude-opus-5"
status: complete
independent_flags_found: 28
caught: 8
partially_caught: 5
missed:
  - {severity: "MAJOR", item: "Prop profit share flat (~52%) vs Q4 FY27 target 55/45; B05 misrecords target as 60/40 profitability", anchor: "Q4 [page 16] L589-593, [page 17] L605-607; Q1 [page 10] L408-409"}
  - {severity: "MAJOR", item: "MTF target restated every quarter (Abhinav FY28 vs Sachin FY27; 2-yr clock reset Jul-26); book +3% in 6 months; B05 scores on track", anchor: "Q3 [page 10] L455-469; Q4 [page 8] L270-272, [page 12] L424-425; Q1 [page 5] L193-198"}
  - {severity: "MAJOR", item: "Fair-value swings drive Q4 consol weakness and part of record Q1 consol PAT (+114% QoQ), never quantified", anchor: "Q4 [page 4] L152-154; Q1 [page 3] L114-117, [page 10-11] L417-422"}
  - {severity: "MAJOR", item: "SMC retail algo integration and AI algo platform contradict 'nobody is offering this product' / 'unique advantage of algo trading'", anchor: "Q4 [page 7-8] L259-260; Q1 [page 13] L511; SMCGLOBAL-2026-02-09 [page 6] L218-222; SMCGLOBAL-2026-07-31 [page 10] L352-355"}
  - {severity: "MAJOR", item: "Peer MTF books outgrow Share India (SMC 760->900+ Cr in Q1 FY27; Choice 370-400 Cr aggressive; Angel +10% QoQ); B06 wrongly says SMC/Choice have no MTF line", anchor: "SMCGLOBAL-2026-07-31 [page 7] L271-272; CHOICEIN-2026-02-11 [page 6] L233-236; ANGELONE-2026-01-21 [page 17] L707-708"}
  - {severity: "MINOR", item: "Wealth distribution ops slid Q1 FY27 -> Q3 FY27 unacknowledged", anchor: "Q3 [page 5] L237-242; Q4 [page 6] L222-228; Q1 [page 6-7] L255-260"}
  - {severity: "MINOR", item: "Insurance: Sachin says no decline, Abhinav concedes YoY drop", anchor: "Q3 [page 8] L398-399; [page 9] L402-409"}
  - {severity: "MINOR", item: "Q4 opening numbers impossible (Q4 rev 383 vs FY 395; EPS 17.6)", anchor: "Q4 [page 4] L139-148"}
  - {severity: "MINOR", item: "Volunteered retail client stagnation", anchor: "Q3 [page 5] L213-221"}
  - {severity: "MINOR", item: "NBFC NIM compression, NPA rise, branch downsizing", anchor: "Q3 [page 7] L305-331; Q4 [page 18] L655-665"}
  - {severity: "MINOR", item: "Share India Cred run rate vs Rs 500 Cr target; six-issue overlap Q4/Q1", anchor: "Q4 [page 7] L246-248; Q1 [page 6] L221-226"}
  - {severity: "MINOR", item: "PMS metric broadened to include advisory; launch quarter inconsistent", anchor: "Q4 [page 7] L229-235; Q1 [page 5] L202-204"}
  - {severity: "MINOR", item: "Margin guidance 43/24 (Q3) restated as 38/22 'from the very beginning' (Q4)", anchor: "Q3 [page 4] L152-153; Q4 [page 10] L353-356"}
  - {severity: "MINOR", item: "Branch economics restated (10-15 Cr/yr vs 15 Cr in 8 months); branch revenue disclosure declined", anchor: "Q4 [page 19] L670-697; Q1 [page 7] L282-285"}
  - {severity: "MINOR", item: "MTF spread / break-even AUM question deflected as 'unfair statement'", anchor: "Q4 [page 11-12] L402-425"}
pipeline_flags_not_supported:
  - "B06 Q3: 'no MTF product line disclosed by either [SMC, Choice]' - false (SMCGLOBAL-2026-07-31 [page 7] L271-272; CHOICEIN-2026-02-11 [page 6] L233-236)"
  - "B06 Part 5: 'stagnate' attributed to Angel One CFO - analyst's word, rebutted by CEO (ANGELONE-2026-04-22 [page 12] L535-572)"
  - "B05 3B: 'media hype' quote attributed to Q4 FY26 SEBI prop-cap answer - it is Q2 FY26 context, on weekly expiries (inputs/other Q2FY26 [page 13] L526, L535)"
  - "OVERSTATED: B05 1C RBI impact '25-30%' - transcript ~20% (Q4 [page 20] L722-723)"
  - "OVERSTATED: B06 2E Share India lending 'never discussed in asset-quality terms' - Q3 NBFC NPA Q&A (Q3 [page 7] L322-331)"
promise_delivery_spot_checks: {checked: 5, confirmed: 4, wrong: 1}
credibility_grade_concur: "concur - C holds, but B05's 'Good' operational-delivery sub-rating is overstated: MTF is off its glide path and all five dated Q3 FY26 new-initiative milestones slipped"
findings:
  - {severity: "MAJOR", location: "B05 1C/2A/4A", finding: "MTF trigger scored on track / no slippage; target restated each quarter, book +3% in 6 months"}
  - {severity: "MAJOR", location: "B05 1B/2A", finding: "Q4 profit-mix target misrecorded (55/45 profit, not 60/40); flat ~52% prop profit share not flagged"}
  - {severity: "MAJOR", location: "B05 absent", finding: "Fair-value contribution to Q4 weakness and Q1 record consol PAT not identified"}
  - {severity: "MAJOR", location: "B06 Q3", finding: "False peer silence on MTF; peer MTF outgrowth missed"}
  - {severity: "MAJOR", location: "B06 Q5", finding: "SMC algo platform contradicts Share India algo-uniqueness claim; not tested"}
  - {severity: "MAJOR", location: "B06 2C", finding: "Tier-3 'no supply / vacuum' claim not set against Choice/Angel evidence (partially caught)"}
  - {severity: "MAJOR", location: "B05 1C/2A/2B", finding: "Five-for-five slip pattern on Q3 FY26 milestones not stated (partially caught)"}
  - {severity: "MINOR", location: "B05 1A", finding: "Wealth distribution slip not flagged"}
  - {severity: "MINOR", location: "B05 1C", finding: "RBI tone shift not read; 25-30% misstatement"}
  - {severity: "MINOR", location: "B05 1B/2A", finding: "Enshrine acquisition not flagged"}
  - {severity: "MINOR", location: "B05 absent", finding: "Insurance speaker contradiction missed"}
  - {severity: "MINOR", location: "B05 absent", finding: "Impossible Q4 opening numbers missed"}
  - {severity: "MINOR", location: "B05 absent", finding: "Retail client stagnation missed"}
  - {severity: "MINOR", location: "B05 absent / B06 2E", finding: "NBFC NIM/NPA missed; B06 2E overstated"}
  - {severity: "MINOR", location: "B05 1A", finding: "Share India Cred run rate not checked"}
  - {severity: "MINOR", location: "B05 1C", finding: "PMS metric broadening and launch-quarter inconsistency missed"}
  - {severity: "MINOR", location: "B05 1B", finding: "Margin guidance restatement missed"}
  - {severity: "MINOR", location: "B05 1B", finding: "Branch economics called first-time quantified; Q4 already quantified"}
  - {severity: "MINOR", location: "B05 absent", finding: "MTF spread question deflection missed"}
  - {severity: "MINOR", location: "B05 3D", finding: "Institutional active vs empanelment counts merged"}
  - {severity: "MINOR", location: "B05 2C/3B", finding: "Quarter/topic attribution errors (52%/49%; media hype)"}
  - {severity: "MINOR", location: "B06 Part 5/2A", finding: "'Stagnate' misattributed to Angel One CFO"}
critical_count: 0
major_count: 7
minor_count: 15
material_found: 10
material_caught: 5
acceptance_rate: 50
coverage_basis: "10 material of 28 listed (1 CRITICAL, 9 MAJOR); 3 caught + 2 partially caught = 5; 30% on full catches only; denominator >= 4 so rule 7 does not apply"
```
