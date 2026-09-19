# Stage 12b: Verifier B, Concall Red Flags. eMudhra Ltd (EMUDHRA)

Run date: 2026-09-19. Model: claude-opus-5. Fresh context. Inputs read by this verifier:
- Main company, read in full: Q3 FY26 call 03-Feb-2026 (`inputs/concalls/Concall_Feb_2026_Q3FY26_Transcript.txt`), special 3i Infotech call 06-Feb-2026 (`inputs/announcements/20260209-3i-Infotech-Investor-Call-Transcript.txt`), Q4 FY26 call 07-May-2026 (`Concall_May_2026_Transcript.txt`), Q1 FY27 call 30-Jul-2026 (`Concall_Aug_2026_Transcript.txt`).
- Peers (12 files): targeted reads on the claim-relevant passages, not cover to cover. NEWGEN Jan-2026 p.14-15, Jul-2026 p.2-4 and margin lines, Nov-2025 and May-2026 margin and profit lines. PROTEAN Aug-2026 p.3-6, May-2026 p.3 and p.15. QUICKHEAL Aug-2025 p.4 and p.8-9, May-2026 p.3-4. The other peer passages were reached by keyword search (H-1B, EBITDA margin, PAT, eSign, DSC, token, DPDP, consent, war, conflict).
- Pipeline outputs compared: B05 (`outputs/reports/05-concall.md`) and B06 (`outputs/reports/06-peers.md`).

Anchor convention: transcript file (call date), speaker, [page N] marker in the .txt. "VS" is Venkatraman Srinivasan (Executive Chairman). "KS" is Kaushik Srinivasan. "AS" is Arvind Srinivasan.

---

## PART 1: INDEPENDENT RED-FLAG LIST (from raw transcripts, before reading B05/B06)

| # | Sev | Item | Anchor(s) |
|---|---|---|---|
| 1 | MAJOR | **FY27 PAT guidance softened and called "unchanged".** May: "bottom line may be around between 25% to 30%. Could be around 27%-28%". Jul: "guidance remains unchanged ... work towards achieving a PAT growth of 25%". VS repeats "Overall, we are expecting 25% growth on PAT" later in the Jul call. | May-2026, VS, [page 8]; Jul-2026, VS opening, [page 5]; Jul-2026, VS, [page 12] |
| 2 | MAJOR | **Organic growth runs below the 18% guide in the quarters the calls quantify.** Q3 FY26 organic was "11% to 12%" (3 months), even though VS called FY26 organic "18-19%". Q1 FY27 total growth is 28% and "approximately 13% was contributed by the Cryptas acquisition", so organic is about 15%. KS gives a different frame in the same Jul call ("25% was the organic growth in the product segment"). [INFERENCE] The 18% FY27 organic guide (May) has no quarter at or above 18% in the calls that disclose a split. A Q4 FY26 figure of about 13-14% follows from FY Cryptas Rs 85 Cr less Q2 Rs 24 Cr and Q3 Rs 34 Cr. That figure is my arithmetic, not a management statement. | Feb-2026, VS, [page 6] and [page 13]; May-2026, VS, [page 8] and [page 12]; Jul-2026, VS, [page 4]; Jul-2026, KS, [page 18] |
| 3 | MAJOR | **The Cryptas profitability story changes each quarter.** Feb: "now positive at INR 1 crore or INR 1.25 crores CRYPTAS PAT" ([page 6]). The same call later says "profit of about INR 1.4 crores or INR 1.5 crores" ([page 8]). May: "almost a break-even ... maybe totally 1 or 2 crores profit", and FY27 "almost over a million dollar of profit" ([page 12]). Jul: Cryptas is "roughly around INR 100 crore business, which was not profitable at all. Gradually, it is improving. This year, we expect profit" ([page 11]). Jul also shows a subsidiary net loss of about Rs 4 Cr "predominantly ... the European subsidiary, B.V." with legal expenses ([page 12]). Revenue also swings: Q3 Rs 34 Cr was lifted by the Cryptas "year-end" ([page 7]), and Q1 FY27 was Rs 20 Cr ([page 10]). [INFERENCE] Management's own account moved from "positive" to "not profitable at all" in two quarters. The acquired asset's earnings run-rate is not established. | Feb-2026, VS, [page 6-8]; May-2026, VS, [page 12]; Jul-2026, VS, [page 10-12] |
| 4 | MAJOR | **3i Infotech matter escalated while management said "no update".** May: "we have not got the complaint from the police or any inquiry from the police". Jul: "No. There is no update. The police to it, they have complied. They called me for a statement on Monday, and they have extensively taken our side of the story". A police statement from the Executive Chairman is a development, and management framed it as "no update". | May-2026, VS, [page 7-8]; Jul-2026, VS, [page 23] |
| 5 | MAJOR | **Promoter bought a personal stake in the complainant.** Analyst: "a group called Capital MXT has acquired 5% stake in [3i Infotech] ... Is that ... related to eMudhra?" VS: "Not related to eMudhra. That is related to my personal investment." [INFERENCE] The Executive Chairman holds about 5% of the company that filed a criminal complaint against him. That creates a governance conflict and possible leverage over the dispute. Nobody asked a follow-up question. | Jul-2026, analyst Sanjyot Khare and VS, [page 23-24] |
| 6 | MAJOR | **The 3i exposure is structurally open-ended and was never quantified.** The Rs 5 Cr preference tranche was "equated ... to 8% of equity", and one redemption trigger was "IPO valuation". 3i contests which trigger applied. The term sheet was "between me and the 3i Infotech", which names the promoter personally. No rupee exposure or provision is given on any call. | Special call 06-Feb-2026, VS, [page 5-6]; May-2026 [page 7-8]; Jul-2026 [page 23] |
| 7 | MAJOR | **R&D is capitalised, and the peer comparison mixes bases.** FY26 software capex is "INR 60 crores or INR 62 crores" (FY25: "INR 45 crores"), plus about Rs 15 Cr for the UAE data centre. VS benchmarks this as R&D: "US product companies are all they are incurring 20%. For us, it may be 10% to 12% only." [INFERENCE] Reported EBITDA and the "only company above 25% EBITDA" claim (item 19) sit on a capitalised-R&D base. The comparison with US peers who expense R&D is not like-for-like. | Feb-2026, VS, [page 11-12] |
| 8 | MAJOR | **Management says ROE of about 15% is the sustainable level.** "Around 14.5-15%. Ideally, that could be the ROE which we can maintain." The analyst had asked twice why the Enterprise mix shift has not lifted ROE/ROCE. [INFERENCE] This bears directly on any R3/R4 quality-ladder claim, where durable ROCE is 20-30%. | Jul-2026, VS, [page 25] |
| 9 | MINOR | Trust Services fell in Q1 FY27, and management expects Q2 to be weak too: "the top-line may continue to be less during the next quarter also". ProxKey tokens are "not getting re-certified". ePass recertification is "pending from the CCA side". The May guide was +20% Trust growth for FY27. | Jul-2026, VS, [page 4], [page 9-10]; May-2026, VS, [page 9] |
| 10 | MINOR | The FY26 Trust "beat" was partly low-margin tokens and channel stocking. May gives tokens sold separately as a growth driver. Jul says token gross margin is "10% or something" and "this time everybody was stocking". [INFERENCE] Part of the 32% FY26 Trust growth was hardware pass-through and partner inventory, not DSC/eSign franchise growth. | May-2026, VS, [page 11]; Jul-2026, VS, [page 10] |
| 11 | MINOR | The "stock issue" with former partners and distributors drags "INR 3 crore" per quarter through stock-in-trade purchases. It will "go another one or two quarters". The root cause is never explained or revisited. | Feb-2026, analyst Aashray Vasa and VS, [page 12-13] |
| 12 | MINOR | UAE timeline. Feb: audit "two months, three months ... Then we can commission". May prepared remarks: "we now have data centers operating in ... the UAE". Jul: QTSP licence at the "final step", with completion "towards the end of this quarter to beginning of next quarter". | Feb-2026 [page 10]; May-2026 [page 4]; Jul-2026, AS, [page 8] |
| 13 | MINOR | Order-book math. FY25 book was Rs 191 Cr and FY26 book is Rs 238 Cr (+24.6%). The conversion multiple was raised from "generally ... 2X" to "2.2X-2.3X" even as ME orders were "delayed". In Feb, the interim book figure was refused: "working in proportion to our growth numbers". | Feb-2026 [page 13]; May-2026, VS, [page 6] |
| 14 | MINOR | The eSign volume figure fell between calls: "now it is almost more than 4 lakh per day" (Feb) became "well over 3 lakh daily transactions" (May). This was not explained. | Feb-2026, VS, [page 10]; May-2026, VS, [page 4] |
| 15 | MINOR | International segment profitability outlook was declined: "Separately, we are not put what is the profitability for that". A qualitative bridge was given: services at 18-20% gross margin, Cryptas unprofitable, senior hires at USD 200-300k. | Jul-2026, VS, [page 11-12] |
| 16 | MINOR | The US cross-sell story is thin. May cites US services relationships as a cross-sell base. Yet "The identity access management, we have not taken to the US because that is still not part of the full plan". | May-2026, VS [page 3]; KS [page 11] |
| 17 | MINOR | PrivaTrust slipped. Feb: "Early deployment ... being tested in live environments". Jul: "pilots, proof of concepts, and very soon a few wins". A peer (QUICKHEAL) had a tier-1 BFSI DPDP win with consent management in Aug-2025 and "several large BFSI customers" by May-2026. eMudhra arrives late to that market. | Feb-2026 [page 5]; Jul-2026, KS, [page 6]; QUICKHEAL Aug-2025 [page 9]; QUICKHEAL May-2026 [page 3] |
| 18 | MINOR | A peer competes head-on in India BFSI eSign workflows. PROTEAN calls eSign Pro ("complete digital documentation workflow ... stamping to signing") "a unique moat ... massively scalable". PROTEAN reports Identity Services +16% on 20% volume growth and holds more than Rs 800 Cr of cash. This overlaps emSigner plus eSign/eStamp in BFSI. | PROTEAN Aug-2026 [page 5-6]; PROTEAN May-2026 [page 15] |
| 19 | MINOR | VS claims on peer margins: "nobody is achieving more than 25% EBITDA margin or more than 16% PAT margin". This is partly contradicted by NEWGEN (FY25 EBITDA 25.3%, Q2 FY26 net margin 20.4%, FY26 adjusted PAT Rs 334 Cr on Rs 1,574 Cr revenue). VS scoped the claim to cybersecurity, and NEWGEN is not a cybersecurity vendor. QUICKHEAL (negative EBITDA) supports VS. | Jul-2026, VS, [page 25]; NEWGEN Nov-2025 lines 160 and 426; NEWGEN May-2026 lines 109 and 199-200 |
| 20 | MINOR | The acquisition stance drifts. Feb: "Currently, we are not evaluating any acquisition ... six months to nine months". May: "open to selective bolt-on ... Maybe ... 3rd Quarter or 4th Quarter ... US only". Jul (KS): "nothing immediately". | Feb-2026 [page 11]; May-2026 [page 5], [page 7]; Jul-2026 [page 19] |
| 21 | MINOR | Adjusted-EBITDA framing. Q3 reported 23.1% is recast as "adjusted EBITDA margin is 25.8%" by excluding acquisition legal cost and the labour-code gratuity. The Q4 margin of 22.4% (EBITDA +25.5% vs income +31.7%) drew no question and no explanation. | Feb-2026, VS, [page 7]; May-2026, CFO, [page 5] |
| 22 | MINOR | Middle East war delayed March-quarter orders (volunteered). | May-2026, VS, [page 6] |
| 23 | MINOR | The year-end cash expectation was cut from Rs 140-150 Cr to Rs 125-140 Cr, with "we have to wait and see". | Feb-2026, VS, [page 14] |

Grading summary: 23 items listed, 8 MAJOR, 15 MINOR, 0 CRITICAL. I found no evasion repeated across 2+ quarters (see Part 2, the international-profitability row).

---

## PART 2: COMPARISON TABLE

### 2A. My items vs pipeline

| # | Sev | Status | Pipeline location / note |
|---|---|---|---|
| 1 | MAJOR | CAUGHT | B05 1B last guidance row, 2C Consistency, 4E Medium flag 3 |
| 2 | MAJOR | PARTIALLY CAUGHT | B05 2A row 7 catches Q1 organic of about 15%. It misses Q3 FY26 organic of "11% to 12%", which makes this a trend, not one quarter. B05 also writes "management attributes the shortfall to the temporary Trust Services decline". The transcripts contain no such attribution. |
| 3 | MAJOR | MISSED | B05 3C marks Cryptas disclosure "Yes / Low risk, high transparency mark". 1C calls the Cryptas trigger "strengthening". The Feb→May→Jul drift ("positive" → "break-even" → "not profitable at all") and the B.V. loss are not flagged. |
| 4 | MAJOR | PARTIALLY CAUGHT | B05 4E rates the 3i matter "Low". 4C grades governance handling "Good" with a "consistent factual account". The Jul "no update" framing around a fresh police statement is not flagged. |
| 5 | MAJOR | MISSED | No mention in B05, B06, or any other report (grep across outputs/: "personal investment", "Capital MXT", "5% stake": no hit). |
| 6 | MAJOR | CAUGHT | B05 2D bullet 1 (no provisioning or contingent-liability figure) |
| 7 | MAJOR | PARTIALLY CAUGHT | B05 1B lists the capex guide, and 3B treats the 10-12% vs 20% R&D line as an "unverified competitive cost-structure claim". The capitalisation angle is absent from B05. The pipeline does carry it elsewhere (B02 finding 7, useful-life extension; B04 asset-intensity row). |
| 8 | MAJOR | PARTIALLY CAUGHT | B05 4E lists it as "Low". Management calls ~15% ROE the level "we can maintain". That caps the quality-ladder thesis, so "Low" under-weights it. |
| 9 | MINOR | CAUGHT | B05 1C Trust row, 2B, 1B "mostly by September" |
| 10 | MINOR | MISSED | B05 2A row 2 records the 32% Trust beat as clean delivery. |
| 11 | MINOR | CAUGHT | B05 2A row 6, 4E Low-Medium |
| 12 | MINOR | PARTIALLY CAUGHT | Caught as a slip. B05 says Q4 was "silent" and "no update given at all", but the May prepared remarks say the UAE DC is "operating" ([page 4]). See spot check 3. |
| 13 | MINOR | CAUGHT | B05 2B (multiple raised despite delays), 1B |
| 14 | MINOR | MISSED | not in B05 |
| 15 | MINOR | CAUGHT | B05 2E, 3C, 4E. B05 over-grades it (see 2B). |
| 16 | MINOR | MISSED | not in B05 |
| 17 | MINOR | MISSED | B05 marks PrivaTrust "Aspirational" but has no peer comparison. B06 was not asked. |
| 18 | MINOR | MISSED | B06 2D and Q7 call PROTEAN "adjacent but structurally distinct" and find no competitive mention. eSign Pro competes directly with the emSigner/eSign BFSI workflow. |
| 19 | MINOR | MISSED | B06 Q5 uses NEWGEN margins as "held flat". It does not test VS's "nobody above 25%/16%" claim. |
| 20 | MINOR | CAUGHT | B05 1C acquisition row |
| 21 | MINOR | MISSED | B05 2A row 3 accepts adjusted EBITDA as delivered, with no flag on the adjusted framing or the Q4 dip. |
| 22 | MINOR | CAUGHT | B05 2B; B06 Q6 and 2A |
| 23 | MINOR | CAUGHT | B05 1B |

Totals: CAUGHT 9, PARTIALLY CAUGHT 5, MISSED 9 (of 23).

### 2B. Pipeline flags I did not independently raise

| Pipeline flag | Assessment | Evidence |
|---|---|---|
| B05 4E: "3i's threatened SEBI complaint status is never addressed on any earnings call" (also 2D bullet 5) | **NOT SUPPORTED** | May-2026, VS, [page 7]: "though they said they are going to file a complaint with SEBI, we have not got anything from them." The status was addressed in the Q4 call. |
| B06 Q8 verdict CONTRADICTED (H-1B), named "single most consequential contradiction" and "priority item for synthesis" | **NOT SUPPORTED** | eMudhra blames H-1B only for its US *services* line: "the US services business, there is no growth ... because of the AI and because of the H1 visa problem" (Feb-2026 [page 6]). It says product is unaffected. NEWGEN's statement is about *product* businesses: "for product-based businesses, H-1B is not a criteria" (NEWGEN Jan-2026 [page 16], lines 756-763). The two statements agree on the product/services split, so they do not contradict each other. The anchor is also wrong: B06 cites "NEWGEN Q4FY26, May-2026 call, p.10". The quote sits in the **Jan-2026 (Q3FY26)** transcript, and the May-2026 file has no H-1B mention. |
| B05 2E / 4E: international profitability "Deflected every time" (Q3 FY26 and Q1 FY27), a repeated evasion | **OVERSTATED** | Q3: VS said "I do not understand the question" and then gave Cryptas revenue and profit. That is a misunderstanding answered with data, not a deflection (Feb-2026 [page 7-8]). Only Q1 FY27 is a real decline to answer, and it came with a qualitative bridge. One evasion, not a repeated one. |
| B05 1C: bolt-on acquisition "not raised by management or any analyst" in Q1 FY27 | **OVERSTATED** (the fading read holds, the fact is wrong) | Jul-2026, KS, [page 19]: "some bolt-on capability ... may pursue sometime down the future, although nothing immediately" (in answer to Amit Chandra). |
| B06 2B: stock-in-trade drag may be industry hardware inflation | **OVERSTATED** (speculative) | The Jul call shows stock-in-trade is DSC tokens with ~10% gross margin, driven by partner stocking and a FIPS transition (Jul-2026 [page 10]). The Feb driver was a partner and distributor "stock issue". No transcript links it to price inflation. |
| B05 4C: "EOW outcome (civil, not criminal) favourable so far" | NOT ASSESSABLE from transcripts | The source is the 18-Aug-2026 Reg 30 letter, which is outside Verifier B's inputs. The last transcript touchpoint (30-Jul) shows an active police statement process. |
| B05 4E: no customer-concentration disclosure | SUPPORTED | No call discloses it. The Q3 India defence deal skews Q4 India (May-2026, KS, [page 10]). |
| B05 2D: FCF and working capital never discussed | SUPPORTED | Only the cash balance is discussed (Feb-2026 [page 14]). |
| B05 2B: India Q4 dip from a large Q3 defence deal | SUPPORTED | May-2026, KS, [page 10] |
| B06 Q4: organic guide "reads aggressive" vs NEWGEN 6%/11% | SUPPORTED as context | NEWGEN May-2026 line 109 (6%), Jul-2026 line 125 (11%) |
| B06 2E: CEO transitions at all three peers | SUPPORTED as peer fact | NEWGEN Jul-2026 line 102. The read-across to eMudhra is weak. Note that Jul-2026 is the first eMudhra call with three Srinivasan family members on the panel. |

---

## PART 3: PROMISE-DELIVERY SPOT CHECKS (B05 2A)

| B05 row | Promise in earlier call? | Outcome in later call? | Verdict |
|---|---|---|---|
| 1. FY26 revenue Rs 700 Cr → Rs 713.2 Cr | Yes. Feb-2026 [page 6]: "we will achieve that Rs.700 crores" | Yes. May-2026 [page 3]: "total income of INR7,132 million" | CONFIRMED |
| 2. FY26 Trust growth 22-25% → 32% | Yes. Feb-2026 [page 10]: "at least 22% to 25% increase" | Yes. May-2026 [page 3]: Trust "up 32%"; CFO Rs 1,400 Mn [page 5] | CONFIRMED (direction). Quality caveat in item 10. |
| 5. UAE DC commissioning slipped; "no update given at all" in Q4 | Yes. Feb-2026 [page 10]: audit "two months, three months ... Then we can commission" | Partly wrong. May-2026 [page 4] says the UAE data centre is "operating", so Q4 was not silent. What is still pending in Jul is the QTSP licence (Jul-2026 [page 8]), a later milestone. | WRONG (partial). The slip is real, but it sits on the licence and not the DC, and the "silent in Q4" claim is false. |
| 6. Stock-in-trade drag to normalise in 1-2 quarters; never revisited | Yes. Feb-2026 [page 12-13] | Correct. It is not revisited in May or Jul. | CONFIRMED |
| 7. FY27 organic 18% → Partial (~15%) | Yes. May-2026 [page 8]: "Most likely 18% organic growth" | Yes. Jul-2026 [page 4]: 28% total, ~13% Cryptas | CONFIRMED. The "management attributes shortfall to Trust decline" line is not in the transcript. |

Checked 5, confirmed 4, wrong 1.

---

## PART 4: CREDIBILITY GRADE

B05 grades management **B (Good)**. I would grade **lower (B-/C+)**. The B grade rests on a clean FY26 batting average and a "consistent" 3i account. The transcripts show four things that grade does not price in:
1. Cryptas economics restated in each call (item 3).
2. A police-statement development presented as "no update", beside an undisclosed-until-asked promoter stake in the complainant (items 4-5).
3. A PAT guide cut from "27-28%" to "25%" and labelled unchanged (item 1).
4. Organic growth below the 18% guide in every quarter where a split is given (item 2).

The FY26 quantified promises were met. That part of the B05 basis stands.

---

## PART 5: CONSOLIDATED FINDINGS

| Sev | Location | Finding |
|---|---|---|
| MAJOR | B05 3C/1C/4A row 2 | MISSED: the Cryptas profitability narrative drifts from "positive Rs 1-1.5 Cr" (Feb) to "break-even" (May) to "not profitable at all" (Jul), with a ~Rs 4 Cr B.V. loss. It is graded "high transparency" instead. |
| MAJOR | B05 (absent), all reports | MISSED: the Executive Chairman's personal ~5% stake in 3i Infotech, the complainant (Jul-2026 [page 23-24]). |
| MAJOR | B05 4E/4C | UNDER-WEIGHTED: the 3i matter is rated Low and handling "Good". The Jul call shows a police statement framed as "no update". |
| MAJOR | B05 4E | UNDER-WEIGHTED: management's "~15% ROE we can maintain" is rated Low. It caps the transition thesis. |
| MAJOR | B05 4E / 2D | NOT SUPPORTED: "3i SEBI complaint status never addressed". It was addressed in May-2026 [page 7]. |
| MAJOR | B06 Q8, Part 4, flags | NOT SUPPORTED: the H-1B CONTRADICTED verdict. NEWGEN's statement concerns product businesses and agrees with eMudhra's services-only attribution. The quote is misanchored (Jan-2026 p.15-16, not May-2026 p.10). |
| MINOR | B05 2A row 7 | PARTIAL: Q3 FY26 organic of 11-12% is omitted, and a Trust-decline attribution is written that the transcript does not contain. |
| MINOR | B05 3B | PARTIAL: R&D capitalisation (Rs 60-62 Cr) is not tied to the EBITDA and peer-R&D comparison in the concall read. It is carried elsewhere (B02/B04). |
| MINOR | B05 2A row 5, 1C | Spot check wrong in part: the Q4 call was not silent on the UAE DC ("operating", May [page 4]). The pending item is the QTSP licence. |
| MINOR | B05 2E | OVERSTATED: the "repeated deflection" rests on a Q3 misunderstanding, not an evasion. |
| MINOR | B05 1C | OVERSTATED detail: the bolt-on acquisition was raised in Q1 FY27 (KS [page 19]). |
| MINOR | B06 2B | OVERSTATED: the hardware-inflation hypothesis for stock-in-trade is contradicted by the Jul token explanation. |
| MINOR | B05 2A row 2 | MISSED: the FY26 Trust beat was partly 10%-margin tokens and partner stocking. |
| MINOR | B05 | MISSED: eSign daily volume went from ">4 lakh" (Feb) to "well over 3 lakh" (May). |
| MINOR | B05 | MISSED: IAM "not taken to the US", which weakens the US cross-sell narrative. |
| MINOR | B06 | MISSED: QUICKHEAL was a year ahead on DPDP consent-management wins, and PrivaTrust slipped. |
| MINOR | B06 2D/Q7 | MISSED: PROTEAN eSign Pro competes directly in BFSI eSign/eStamp workflows. |
| MINOR | B06 Q5 | MISSED: NEWGEN's ~20% PAT margin partly contradicts VS's "nobody above 16% PAT" claim (VS scoped it to cybersecurity). |
| MINOR | B05 2A row 3 | MISSED: the adjusted-EBITDA framing and the unprobed Q4 margin dip to 22.4%. |

Counts: CRITICAL 0, MAJOR 6, MINOR 13.

Acceptance basis. There are 8 material items (MAJOR) in my independent list. Of those, the pipeline had 6: CAUGHT 2 (items 1, 6) and PARTIALLY CAUGHT 4 (items 2, 4, 7, 8). It MISSED 2 (items 3, 5). Acceptance rate 6/8 = 75%. Under the strict CAUGHT-only reading it is 2/8 = 25%. The orchestrator should read the 75% together with the four under-weightings above.

stage: B12b
company: "EMUDHRA"
run_date: "2026-09-19"
model: "claude-opus-5"
status: complete
independent_flags_found: 23
caught: 9
partially_caught: 5
missed:
  - {severity: "MAJOR", item: "Cryptas profitability narrative drifts: 'positive Rs 1-1.5 Cr' (Q3) -> 'break-even' (Q4) -> 'not profitable at all' (Q1 FY27); ~Rs 4 Cr B.V. subsidiary loss; B05 grades Cryptas disclosure high-transparency", anchor: "Feb-2026 VS [page 6-8]; May-2026 VS [page 12]; Jul-2026 VS [page 11-12]"}
  - {severity: "MAJOR", item: "Executive Chairman holds a personal ~5% stake in 3i Infotech, the complainant against him ('That is related to my personal investment')", anchor: "Jul-2026 Sanjyot Khare / VS [page 23-24]"}
  - {severity: "MINOR", item: "FY26 Trust Services beat partly low-margin (~10% GM) token sales and partner stocking", anchor: "May-2026 VS [page 11]; Jul-2026 VS [page 10]"}
  - {severity: "MINOR", item: "eSign daily volume stated >4 lakh (Feb) then 'well over 3 lakh' (May), unexplained", anchor: "Feb-2026 VS [page 10]; May-2026 VS [page 4]"}
  - {severity: "MINOR", item: "IAM not taken to the US ('not part of the full plan'), thins the US cross-sell narrative", anchor: "May-2026 KS [page 11]"}
  - {severity: "MINOR", item: "PrivaTrust slipped from 'live environments' (Feb) to 'pilots, POCs' (Jul) while QUICKHEAL already had BFSI DPDP consent wins", anchor: "Feb-2026 [page 5]; Jul-2026 KS [page 6]; QUICKHEAL Aug-2025 [page 9]; QUICKHEAL May-2026 [page 3]"}
  - {severity: "MINOR", item: "PROTEAN eSign Pro competes directly in BFSI eSign/eStamp workflow; B06 called PROTEAN structurally distinct", anchor: "PROTEAN Aug-2026 [page 6]; PROTEAN May-2026 [page 15]"}
  - {severity: "MINOR", item: "Chairman's 'nobody above 25% EBITDA / 16% PAT' claim partly contradicted by NEWGEN (~20% PAT margin, 25.3% FY25 EBITDA)", anchor: "Jul-2026 VS [page 25]; NEWGEN Nov-2025 lines 160, 426; NEWGEN May-2026 lines 199-200"}
  - {severity: "MINOR", item: "Adjusted-EBITDA recasting (23.1% -> 25.8%) and unprobed Q4 FY26 margin dip to 22.4%", anchor: "Feb-2026 VS [page 7]; May-2026 CFO [page 5]"}
pipeline_flags_not_supported:
  - "B05 4E/2D: 3i Infotech SEBI complaint status 'never addressed on any earnings call' (addressed May-2026 VS [page 7])"
  - "B06 Q8 CONTRADICTED (H-1B): NEWGEN's statement is about product businesses and agrees with eMudhra's services-only attribution; quote misanchored (NEWGEN Jan-2026 [page 16], not May-2026 p.10)"
promise_delivery_spot_checks: {checked: 5, confirmed: 4, wrong: 1}
credibility_grade_concur: "lower: B is too generous given Cryptas economics restated each call, 3i police development framed as 'no update' plus undisclosed promoter stake in the complainant, PAT guide cut 27-28% to 25% called unchanged, organic below 18% guide in every disclosed quarter"
findings:
  - {severity: "MAJOR", location: "B05 3C/1C/4A", finding: "MISSED Cryptas profitability narrative drift and B.V. loss"}
  - {severity: "MAJOR", location: "B05 and all reports", finding: "MISSED promoter personal ~5% stake in 3i Infotech"}
  - {severity: "MAJOR", location: "B05 4E/4C", finding: "UNDER-WEIGHTED 3i matter (Low, handling Good) despite Jul police statement framed as 'no update'"}
  - {severity: "MAJOR", location: "B05 4E", finding: "UNDER-WEIGHTED management's ~15% ROE 'we can maintain' admission, thesis-capping"}
  - {severity: "MAJOR", location: "B05 4E/2D", finding: "NOT SUPPORTED: SEBI complaint status was addressed in Q4 call"}
  - {severity: "MAJOR", location: "B06 Q8 / Part 4 / flags", finding: "NOT SUPPORTED: H-1B CONTRADICTED verdict; misanchored quote"}
  - {severity: "MINOR", location: "B05 2A row 7", finding: "Q3 FY26 organic 11-12% omitted; Trust-decline attribution not in transcript"}
  - {severity: "MINOR", location: "B05 3B", finding: "R&D capitalisation not tied to EBITDA/peer R&D comparison in concall read (carried in B02/B04)"}
  - {severity: "MINOR", location: "B05 2A row 5 / 1C", finding: "Spot check partly wrong: Q4 not silent, UAE DC stated 'operating'; pending item is QTSP licence"}
  - {severity: "MINOR", location: "B05 2E", finding: "OVERSTATED repeated deflection; Q3 was a misunderstanding answered with data"}
  - {severity: "MINOR", location: "B05 1C", finding: "OVERSTATED detail: bolt-on acquisition was raised in Q1 FY27 (KS [page 19])"}
  - {severity: "MINOR", location: "B06 2B", finding: "OVERSTATED hardware-inflation hypothesis for stock-in-trade"}
  - {severity: "MINOR", location: "B05 2A row 2", finding: "MISSED Trust beat quality (tokens, partner stocking)"}
  - {severity: "MINOR", location: "B05", finding: "MISSED eSign volume drift 4 lakh to 3 lakh/day"}
  - {severity: "MINOR", location: "B05", finding: "MISSED IAM not taken to US"}
  - {severity: "MINOR", location: "B06", finding: "MISSED QUICKHEAL DPDP lead vs PrivaTrust slip"}
  - {severity: "MINOR", location: "B06 2D/Q7", finding: "MISSED PROTEAN eSign Pro direct competition"}
  - {severity: "MINOR", location: "B06 Q5", finding: "MISSED NEWGEN margin partial contradiction of chairman peer-margin claim"}
  - {severity: "MINOR", location: "B05 2A row 3", finding: "MISSED adjusted-EBITDA framing and Q4 margin dip"}
critical_count: 0
major_count: 6
minor_count: 13
material_found: 8
material_caught: 6
acceptance_rate: 75
coverage_basis: "23 independent items listed, 8 material (all MAJOR, 0 CRITICAL); pipeline had 6 of 8 (2 CAUGHT, 4 PARTIALLY CAUGHT), missed 2; CAUGHT-only rate would be 25%. Main transcripts read in full; peers read on claim-relevant passages plus keyword search"
