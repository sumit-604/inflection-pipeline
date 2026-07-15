# FTTCP DRAFT — Fedbank Financial Services (FEDFINA)

Company: Fedbank Financial Services Ltd. Ticker: FEDFINA. CMP: not in manifest (manifest carries 0.0; a broker note shows about Rs 152 as of 29 Apr 2026, non anchored). Run date: 2026-07-15. Mode: first workup (no prior company memory, manifest run_type full), so all Role 1 derived fields are N/A because FTTCP runs before valuation. Concall status: FULL CONCALL MODE, three actual transcripts read in Phase 1 (Q1, Q2, Q3 FY26). This is a lender, so it runs the Lender Transition Set: AUM growth, NIM and spread, asset quality, and return on assets and equity.

---

## MY RULINGS

Every call below is made. Each carries a confidence tag and the single fact that would prove it wrong.

1. **Forward window: 3 months primary, 6 months secondary, 12 months for the return transition.** The company reports quarterly, so a 3 month print exists. `sure`. Wrong if the company stops quarterly reporting.

2. **Business type: LENDER. Run the Lender Transition Set.** B04 sets business_type to lending; the book is gold loans (about 53% of AUM) plus property backed LAP and small ticket home loans. `sure`. Wrong if B04 mislabelled a non lending business, which it did not.

3. **Workup intent: FIRST WORKUP.** No companies/FEDFINA.md exists and run_type is full. Destination PE, prior thesis, and prior devil's advocate findings are marked N/A because FTTCP precedes Role 1. `sure`. Wrong if a prior Notion or company memory turns up.

4. **Sector cap row: the manifest's "Pharma / CDMO" is WRONG. Corrected row for Phase 3: Banks / NBFCs / MFIs, 18x, with P/B as the primary method and destination PE as a cross check only** (Section 1B Amendment 8 cap table, and Amendment 7 lender carve out). Reasoning in one line: B04 is a lending business, so the pharma row cannot apply and the only lending row in the Section 1B table is the 18x banks and NBFCs row. Phase 3 stage 11 must inherit this row. `sure`. Wrong only if Section 1B adds a finer NBFC sub row before Phase 3.

5. **AUM growth (Transition 1): backward FIRING, forward FIRING (+2).** AUM growing about 35% year on year with disbursements accelerating and 113 of a planned 100 to 150 gold branches already opened. `fairly sure`. Wrong if headline AUM growth stripped of the gold price effect falls below 20%, since gold tonnage is flat and the rupee AUM is carrying a price tailwind.

6. **NIM and spread (Transition 2): backward SUSTAINED, forward STAGNANT (0).** Spread is healthy and stable near 8.6% and cost of funds is easing, but sector wide gold yield compression and the deliberate removal of high margin direct assignment fee income offset the funding tailwind, so the spread holds rather than expands. `fairly sure`. Wrong if blended spread expands above about 8.6% for two consecutive quarters, which would move it to FIRING.

7. **Asset quality (Transition 3, the critical one): backward IMPROVING, forward STARTING (+1).** Credit cost normalised from 1.8% of average assets in FY25 to about 0.8% held across three quarters of FY26, and the book is now 99% secured, but provision coverage thinned from 40% to 32%, Stage 2 and old versus new book data were refused on the calls, and the roughly 30% cure rate on secured paper is weak. `genuinely uncertain`. The two readings: STARTING if the fourth in band quarter prints and the ST LAP rebuild holds, or STAGNANT if the opacity is hiding a forming problem. The draft uses STARTING because the secured mix shift and three in band quarters are documented and real. Wrong if Q4 FY26 credit cost prints above 1.1% of average assets or GNPA breaks meaningfully higher.

8. **Return on assets and equity (Transition 4): backward SUSTAINED, forward STARTING (+1).** Return on assets sits near the 2.5% NBFC benchmark and is recovering, and cost to income has already fallen from about 57% to 52.8% as the branch cohort matures, but the cost to income gap to peers is still 15 to 25 points and the FY27 cost guidance was deferred. `fairly sure`. Wrong if cost to income fails to keep improving through FY27 or return on assets slips back below 2.5%.

9. **Cash conversion determination (read as asset quality for a lender): the negative operating cash flow is STRUCTURAL and mechanical, not an earnings quality failure; the asset quality recovery is real but NOT a clean pass because specific disclosure is missing.** Operating cash flow to profit ran negative about 5x across six years because a growing lender books loan disbursement as an operating outflow under Ind AS 7, funded by financing inflows, with the cash pile growing not shrinking. The genuine earnings quality item, direct assignment gain on sale at about 50% of pre tax profit in FY25, is being wound down (nine month FY26 direct assignment income Rs 1 Cr against Rs 62 Cr a year earlier). The missing evidence that keeps this from a clean pass is named: Stage 2 balances, the old versus new ST LAP book split, and collection efficiency were all withheld. `sure` on the mechanics, `genuinely uncertain` on whether the withheld data hides stress.

10. **The return transition is TEMPORARILY DEPRESSED and RECOVERING, not DECLINING.** Apply the test: if growth stopped tomorrow, would return on assets recover within 18 to 24 months. Yes, because the depressant was a one year credit cost spike that has already reversed in reported numbers. `fairly sure`. Wrong if the FY25 credit cost spike proves to be the first of a repeating pattern rather than a one off.

11. **Composite score 4 of 8: DEEP WATCH leaning BUY ON DIPS.** The Kernex cap does NOT engage, because no transition is DECLINING with catalyst NONE. The TRIM rule does not engage, because the four transitions were not all FIRING backward. `sure` on the arithmetic (2 + 0 + 1 + 1 = 4).

12. **SHARED CATALYST flag raised for the devil's advocate.** Credit cost normalisation drives both the asset quality transition and the return transition, so a single bad credit cost print weakens two of the four transitions at once. `sure`.

13. **Position posture: DEEP WATCH leaning BUY ON DIPS, a small starter defensible only with a strict entry zone and only after the Q4 FY26 confirmation.** The entry zone, margin of safety price, and destination PE are NOT set here; they are Phase 3 work. `sure` on the posture; the price is deliberately not stated.

Confidence reducers, stated plainly: the announcements folder is absent, so the Step 2E documented action feed is degraded and recent exchange filings could not be graded. Phase 1 red flag coverage was 63 (the concall read missed four major flags that a verifier caught). Asset quality disclosure was actively withheld by management on two of three calls. All three lower confidence and none halts the analysis.

---

## TRANSITION 1 — AUM AND DISBURSEMENT GROWTH

| Period | AUM (Rs Cr) | Gold mix % | Growth read | Actual or Expected |
|---|---|---|---|---|
| FY22 | NOT FOUND in blocks | NOT FOUND | pre stress base | ACTUAL |
| FY23 | NOT FOUND in blocks | NOT FOUND | RHP era | ACTUAL |
| FY24 | NOT FOUND in blocks | ~40% | growth intact | ACTUAL |
| FY25 | NOT FOUND (revenue CAGR FY21-26 26.1%, B01) | ~45% | growth intact through the credit stress | ACTUAL |
| Q3 FY26 | ~17,500 (investor presentation, via B09) | 45.2% (B04, B12b) | AUM up, gold accelerating | ACTUAL |
| Q1 FY27 | ~21,000 (investor presentation, via B04/B09) | 52.9% (B04) | AUM +34.7% YoY (B04) | ACTUAL |
| FY27-FY31 | illustrative only | gold above 50%, unconstrained | guidance about 25-30% AUM growth | EXPECTED (illustrative, from B05 guidance) |

Plain meaning: the book is compounding near 35% a year and gold is now more than half of it. That is the FIRING threshold on the number. The catch, and it is a real one, is that the 52% year on year gold AUM jump is mostly gold price, not volume. Gold tonnage was roughly flat at 11.2 tonnes across the fiscal (B12b, B06), and peer Manappuram disclosed only 2.8% year on year tonnage growth against its own 22 to 23% AUM print (B06). So the growth engine is running, but a chunk of it is the gold price doing the work. **Forward verdict: FIRING (+2).**

---

## TRANSITION 2 — NIM AND SPREAD

| Period | Blended spread % | Cost of funds % | Read | Actual or Expected |
|---|---|---|---|---|
| Q1 FY26 | NOT FOUND (yield/CoF split) | 7.87 (B05) | funding cost easing | ACTUAL |
| Q2 FY26 | NOT FOUND | 7.83 (B05) | easing | ACTUAL |
| Q3 FY26 | NOT FOUND | 7.80 (B05) | easing | ACTUAL |
| Q1 FY27 | 8.6 (B04) | ~7.7-7.8 (B04) | healthy, stable | ACTUAL |
| FY27-FY31 | illustrative | drifting lower on fixed rate mix | stable spread | EXPECTED (illustrative) |

Plain meaning: the spread is healthy at about 8.6% and the cost of borrowing is edging down as the company locks in more fixed rate liabilities and adds cheaper co-lending and ECB funding. That is the good side. The offsetting side is that gold loan yields are compressing across the whole sector (Manappuram walked its yield from about 22% to about 18% over the year, B06), and the company is deliberately giving up high margin direct assignment fee income. Net, the spread holds where it is rather than widening. A stable healthy spread is not a firing transition; it is a sustained one. **Forward verdict: STAGNANT (0).**

---

## TRANSITION 3 — ASSET QUALITY (THE CRITICAL ONE)

| Period | Credit cost % of avg assets | GNPA % | PCR % | Read | Actual or Expected |
|---|---|---|---|---|---|
| FY24 | 0.7 (B01, rating) | 1.66 (B03) | ~40 | clean, pre stress | ACTUAL |
| FY25 | 1.8 (B01, rating) | 2.02 (B03/B01) | 40.0 (B01) | the credit shock: impairment +229% to Rs 216 Cr (B02 Note 32) | ACTUAL |
| Q2 FY26 | 0.9 (B05) | Gross Stage 3 1.9 (B05) | NOT FOUND | normalising | ACTUAL |
| Q3 FY26 | 0.9 (B05) | Gross Stage 3 2.1 (B05) | 32.29 FY26 (B01) | credit cost held, GNPA ticked up, PCR thinned | ACTUAL |
| Q1 FY27 | ~0.8 (B04) | mortgage 3.4-3.8 vs gold 0.1-0.3 (B01, rating) | 38.36 (B01) | secured mix 99%+, mortgage the residual stress | ACTUAL |
| FY27-FY31 | illustrative | management wants it predictable | credit cost held near 0.8-1.0 | EXPECTED (illustrative, from B05; FY27 guidance deferred to Q4 FY26 call) |

Plain meaning: this is the whole story. FY25 was a genuine credit shock, the impairment charge jumped 229% to Rs 216 Cr and profit fell 8%, driven by small ticket LAP and the wind down of an unsecured book. The turnaround since is real on the headline: credit cost normalised to about 0.8% and held there for three quarters, the book is now 99% secured, and the entire unsecured business loan portfolio was exited and derecognised. Against that, three things keep this from a clean firing call. Provision coverage thinned from 40% to 32% even as GNPA stayed put, which means the buffer got thinner not thicker. Management refused to disclose Stage 2 balances and the old versus new ST LAP book split on two separate calls. And the cure rate on the secured book runs only about 30%, which is weak for collateralised paper. The recovery is underway and documented, but the fourth in band quarter and the withheld data are not yet in hand. **Forward verdict: STARTING (+1).** This transition cannot be called FIRING until Q4 FY26 prints a fourth in band credit cost and management reopens the asset quality disclosure.

---

## TRANSITION 4 — RETURN ON ASSETS AND EQUITY

| Period | RoA % | RoE % | Cost to income % | Read | Actual or Expected |
|---|---|---|---|---|---|
| FY24 | NOT FOUND | NOT FOUND | NOT FOUND | pre stress | ACTUAL |
| FY25 | dipped on the credit shock (PAT -8%, B04) | ~11.5 median (B01) | ~57 | trough year | ACTUAL |
| FY26 | ~2.4 (B04) | ~12.6 (B04) | ~57 (B04) | recovering | ACTUAL |
| Q3 FY26 | NOT FOUND | 12.7 (B12b) | NOT FOUND | recovering | ACTUAL |
| Q1 FY27 | ~2.5-2.6 (B04) | improving (B04) | 52.8 (B04) | operating leverage starting | ACTUAL |
| FY27-FY31 | illustrative | mid teens | RoA up 20-30 bps, opex falling | EXPECTED (illustrative, from B05; FY27 opex guidance deferred) |

Plain meaning: return on assets sits right around the 2.5% mark that a decent NBFC should clear, and it is rising off the FY25 trough. The lever from here is operating leverage. Cost to income has already dropped from about 57% to 52.8% in one year as the new gold branches season and carry more AUM each. Two things temper it. The cost to income ratio is still 15 to 25 points worse than peers who run at 35 to 41% (B06), so there is a structural opex gap that scaling has not yet closed. And management deferred the FY27 cost and credit guidance to the Q4 FY26 call, so the promise is still a promise. **Forward verdict: STARTING (+1).**

---

## THE CATALYST STORY IN PLAIN WORDS

What could make each transition fire or hold over the next 3 to 12 months, what the evidence is, and what would kill it.

**AUM growth (already firing).** The gold branch build out is the engine: 113 of a planned 100 to 150 new gold branches were open by Q3 FY26 (B05), each one maturing toward about Rs 20 Cr of AUM from about Rs 13 to 18 Cr now (B04). Co-lending with parent Federal Bank funds growth off balance sheet. What confirms it: branch count above 140 and AUM per gold branch still rising into FY27. What kills it: a gold price correction, because so much of the rupee growth is price not tonnage.

**NIM and spread (holding).** Cost of funds is easing as the company adds fixed rate liabilities, a Rs 450 Cr subordinated debt raise, and ECB money (B05). What confirms firing: spread widening above 8.6% for two quarters. What kills it: gold yield compression accelerating or funding costs turning back up.

**Asset quality (starting, the pivotal one).** The documented catalysts are the shift to a 99% secured book, the full exit of the unsecured portfolio, and a near doubling of collections headcount. The management claims that are not yet documented are the ST LAP credit scorecard rollout, which was promised for Q3 FY26 and then never mentioned again, and the FY27 credit cost guidance, deferred to the Q4 FY26 call. What confirms it: a fourth quarter of credit cost inside the roughly 1% band, plus reopened Stage 2 disclosure. What kills it: Q4 FY26 credit cost above 1.1%, or provision coverage thinning further while GNPA rises.

**Return on assets (starting).** The catalyst is operating leverage, and it is already showing: cost to income fell more than 400 bps in a year. What confirms it: cost to income continuing down through FY27 toward the low 50s and below. What kills it: the FY27 opex guidance being deferred again, or the branch cohort failing to season.

**One honest NONE FOUND.** There is no documented catalyst that closes the 15 to 25 point cost to income gap to peers on any near horizon. Scaling helps at the margin, but nothing in the filings or calls names a structural fix. That gap is the reason this is a mid teens return business, not a high teens one.

---

## STEP 2E — MANAGEMENT INTENT AND ACTION LEDGER

The announcements folder is absent, so the documented action feed is degraded and recent Reg 30 filings could not be graded. The ledger runs on concall, results, and annual report evidence only, and says so.

| Transition | Stated vision | Documented action | Promise vs delivery | Too conservative? | Adjustment |
|---|---|---|---|---|---|
| AUM growth | twin engine, gold unconstrained | 113 gold branches opened; Rs 770 Cr unsecured book derecognised; co-lending scaled | delivered on branch and exit promises | no, already FIRING (max) | none |
| NIM and spread | lock spreads, cut funding cost | Rs 450 Cr sub debt; ECB raised; fixed rate mix up | delivered on funding | no, action supports stability not expansion | none, STAGNANT holds |
| Asset quality | credit cost predictable, rebuild ST LAP | unsecured exit (strong); collections headcount ~2x; three in band credit cost quarters | mixed: ST LAP scorecard promised Q3 FY26, not delivered (discount) | no, action is real and already scored as STARTING | none, STARTING confirmed |
| Return on assets | improve RoA 20-30 bps, cut opex in FY27 | cost to income fell to 52.8% | FY27 opex guidance deferred (vision, not action) | no, already STARTING; guidance deferral blocks a leap to FIRING | none, STARTING confirmed |

Result: the ledger CONFIRMS the Step 2 grades. It does not loosen any verdict, because none was too conservative, and it does not tighten any, because the downside is already governed by the evidence. There is no Kernex cap to lift.

---

## STEP 3 — FORWARD SCORECARD

| Transition | Backward | Catalyst strength | Forward probability | Forward verdict | Score |
|---|---|---|---|---|---|
| AUM growth | FIRING | Strong | 3-6m: HIGH | FIRING | +2 |
| NIM and spread | SUSTAINED | Moderate | 3-6m: MODERATE for expansion | STAGNANT | 0 |
| Asset quality | IMPROVING | Moderate | 3-6m: MODERATE, above 40% | STARTING | +1 |
| Return on assets | SUSTAINED | Moderate | 12m: MODERATE, above 40% | STARTING | +1 |
| | | | | **COMPOSITE** | **+4 / 8** |

---

## THE VERDICT

The composite is **4 out of 8, which lands at DEEP WATCH leaning BUY ON DIPS**: a small starter is defensible, but only with a strict entry zone and only after confirmation. AUM growth is firing, the spread is holding, and both the asset quality and the return transitions are starting to recover off a real FY25 credit shock, but neither is confirmed. The Kernex cap does not engage because no transition is going backwards with no catalyst, and the TRIM rule does not engage because the book was not firing on all four backward. The whole call turns on one print: **Q4 FY26 credit cost.** If it holds at or below about 1.1% of average assets and management reopens the Stage 2 disclosure and finally issues FY27 guidance, the asset quality and return transitions can both move to firing and the score moves up a band. If it breaks the band, both transitions weaken together and the score falls.

---

## STEP 5 — MONITORING TRIGGERS (90 to 180 DAYS)

| # | Trigger | Threshold | Horizon | What it changes in FTTCP |
|---|---|---|---|---|
| 1 | Q4 FY26 credit cost | at or below 1.1% of average assets | 3m | fourth in band quarter moves asset quality toward FIRING; a breach moves it to STAGNANT or DECLINING and risks the Kernex cap |
| 2 | FY27 credit cost and cost to income guidance | actually issued at the Q4 FY26 call, not deferred again | 3m | issuance supports the return transition and management credibility; a third deferral is a negative signal |
| 3 | Gold tonnage versus gold AUM | tonnage growth disclosed and rising, not just rupee AUM | 3-6m | confirms whether AUM growth is volume or gold price; flat tonnage keeps the growth quality flag on |
| 4 | Provision coverage ratio | stops falling, holds above about 35% | 3-6m | a further slide while GNPA rises turns asset quality negative |
| 5 | Stage 2 and old versus new ST LAP book disclosure | reopened on the next call | 3-6m | continued refusal keeps the opacity discount and caps confidence |
| 6 | Cost to income | continues down toward the low 50s and below | 6-12m | sustained fall confirms the return transition FIRING; a stall confirms the structural opex gap |
| 7 | CRAR and Tier 2 capital | a CRAR figure is disclosed again and a Tier 2 raise lands | 3-6m | the dropped Q3 disclosure reopening restores confidence in capital adequacy against 35% AUM growth |
| 8 | Gold mix ceiling | gold stays inside about 45 to 53% rather than running unconstrained | 6-12m | unconstrained gold concentration raises price cyclicality and would reweight the AUM growth quality |
| 9 | Senior leadership stability | no further C suite exit within 12 months | 12m | another exit after the near total 18 month turnover reopens the execution risk |

---

## HANDOFF TO VALUATION (Phase 3, stage 11)

| Field | Value |
|---|---|
| Return forward verdict | STARTING, which is the RECOVERING state, probability in the 40 to 60% band |
| Pillar 1 basis (lender) | ROE, not ROCE (Section 1B Amendment 7). Formula 0.5 x ROE + 7.5, floor 9x, cap 24x. RECOVERING at 40-60% probability means a 60/40 weighted average of current and FY[Y+2] expected ROE. Current ROE about 12.7% (Q3 FY26, B12b) |
| Primary method | P/B, theoretical P/B = ROE / cost of equity (Section 1B Amendment 7); destination PE is the secondary cross check only |
| Pillar 2 (credit route) | Asset Quality Multiplier, NOT the cash multiplier (Amendment 7). Keep it conservative: provision coverage thinned to 32%, Stage 2 disclosure withheld, cure rate weak. Do not credit a full recovery until Q4 FY26 confirms |
| Sector cap row | Banks / NBFCs / MFIs, 18x absolute. The manifest's Pharma / CDMO row is wrong and must not be used |
| ROE recovery single credit | credit the recovery via Pillar 1 only, per the single credit rule; the strategic re-rating premium route stays barred while it is credited in Pillar 1 |
| SHARED CATALYST flag | credit cost normalisation drives BOTH the asset quality transition and the return transition. The devil's advocate must stress test this single point of failure: one bad Q4 FY26 credit cost print weakens two of the four transitions at once |
| Cash determination | negative operating cash flow is STRUCTURAL and mechanical for a growing lender, not a quality failure; the residual earnings quality item (direct assignment reliance) is being wound down; the missing asset quality disclosure is named and is why this is not a clean pass |

---

*Draft complete. Every call above is made, not asked. The operator may accept, question a figure, or override any call.*
