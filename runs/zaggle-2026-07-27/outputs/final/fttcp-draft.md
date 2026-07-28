# FTTCP v1.2 DRAFT — ZAGGLE

Company: Zaggle Prepaid Ocean Services Ltd | Ticker: ZAGGLE | CMP Rs 203.00 | Market cap Rs 2,731 cr | Run date 2026-07-27

First workup. No prior companies/ZAGGLE.md exists and manifest run_type is full, so Role 1 derived fields (destination PE, prior thesis, prior devil's advocate) are N/A because FTTCP runs before Role 1. Concall Gate CLEARED: three actual transcripts read (Q2 FY26, Q3 FY26, Q4 FY26) plus one older Q2 FY25 call. This did NOT run in NO-CONCALL MODE.

Every actual number below carries its source. Where a number does not exist in this run's inputs it is written NOT FOUND. Nothing is estimated.

---

## 1. MY RULINGS

These are decisions, not questions. Each one is made. The operator can overturn any of them.

### The four setup calls

**Ruling 1. Forward window is 3 months primary, 6 months secondary, 12 months for ROCE.**
Zaggle reports quarterly and four consecutive quarterly prints exist in the data, so the default applies unchanged.
Confidence: `sure`.
What would prove it wrong: the company moving to semi annual reporting.

**Ruling 2. Zaggle is a standard operating business, so I ran the four standard transitions, not the Lender Transition Set.**
B04 records business_type hybrid and asset_intensity light, with revenue in three streams: program fee 41.85%, Propel gift card resale 55.37%, SaaS or platform fee 2.78% (B04-bizmodel). Hybrid describes the revenue mix, not lender status. Management states repeatedly that credit risk on the retail card book sits with the partner bank and not with Zaggle (Q4 FY26 concall). A company that carries no loan book is not a lender.
Confidence: `sure`.
What would prove it wrong: Zaggle taking credit risk onto its own balance sheet, which management has explicitly ruled out.

**Ruling 3. This is a first workup, not a refresh.**
No companies/ZAGGLE.md exists and no prior run folder for this ticker exists under runs/. Forward intent tested: does a new name earn a position at all, on forward evidence.
Confidence: `sure`.
What would prove it wrong: a prior ZAGGLE workup surfacing from outside this repository.

**Ruling 4. I corrected the sector cap row from Platform / SaaS / IT services at 45x to CPaaS / Communications platform at 28x.**
The manifest row was auto picked by the collector and the manifest itself says to verify it. Only 2.78% of gross revenue is true subscription SaaS (B04-bizmodel). The economics are per transaction interchange sharing with partner banks at 41.85% of revenue, plus principal basis gift card resale at 55.37% carrying roughly 94% cost. That is a transaction platform monetising volume through partners, not a software licence business. The run's own peer set includes Tanla, a CPaaS name, on exactly that logic. Phase 3 must inherit 28x.
Confidence: `fairly sure`.
Both readings: the 45x reading says the DICE acquisition brings AI SaaS with roughly 95% gross margin (Q4 FY26 concall, management claim) and that on a net revenue basis the SaaS and program fee streams dominate, so the business is genuinely a platform. The 28x reading says only 2.78% of gross revenue is SaaS today, DICE is unclosed and its margin claim is unaudited, and the cash economics look like a payments intermediary. The draft used 28x.
What would prove it wrong: DICE closing and lifting audited subscription revenue above roughly a quarter of net revenue, which would move the row back toward Platform / SaaS.
Note that this ruling does not change any number below. The pillars produce a destination PE near 11x, so the cap does not bind at either 28x or 45x. The correction matters only if the pillars later rise.

### The transition calls

**Ruling 5. Revenue growth is FIRING backward and FIRING forward.**
Three year revenue CAGR 51.08%, and all four quarters of FY26 grew year on year (screener-data, cross checked to results Q4 FY26 p.9).
Confidence: `sure`.
What would prove it wrong: a quarter printing negative year on year revenue.

**Ruling 6. Margin is SUSTAINED backward and STAGNANT forward.**
Gross operating margin moved 9.11% in FY24 to 9.70% in FY26, a rise of 59 basis points, which is inside the plus or minus 150 basis point stability band (computed from screener-data). Forward, management withheld FY27 EBITDA guidance pending DICE integration, the incentive and cashback ratio moved to roughly 68% of program fees against a stated path toward 50%, and Propel gross margin fell to 4%. Probability of a band change in 3 to 6 months sits near 35%, which lands in STAGNANT.
Confidence: `fairly sure`.
What would prove it wrong: FY27 EBITDA guidance reissued at or above 10% to 11% with the incentive ratio turning down.

**Ruling 7. Cash conversion is DETERIORATING backward and STAGNANT forward, and the structural versus growth induced question is INDETERMINATE.**
Cumulative CFO to PAT is negative 0.44 across four years, with operating cash flow negative in FY23, FY24 and FY26 (screener-data, cross checked to results Q4 FY26 p.11). Applying the test, if growth stopped tomorrow would working capital release: partly yes, because receivables and incentive funding scale with volume, and partly no, because the incentive and cashback ratio is a pricing choice that has been moving the wrong way and Propel take rate collapsed to 4%. The record does not settle it, so it stays INDETERMINATE, and INDETERMINATE caps the disposition at PROCEED WITH CAVEATS rather than resolving to a pass.
I chose STAGNANT over DECLINING because there is real executed action, not just words: management changed the Propel redemption model to cut cash intensity and you can see the cost of that decision in the take rate falling from 10% to 4%, and standalone quarterly operating cash flow improved from about negative Rs 33 cr to about negative Rs 6 cr across FY26 (Q4 FY26 concall). Catalyst strength is Weak, not NONE, so the Kernex cap does not engage.
Confidence: `genuinely uncertain`.
Both readings: the STAGNANT reading credits the executed redemption model change and the improving standalone quarterly trend. The DECLINING reading notes that consolidated operating cash flow actually went backwards in FY26, from positive Rs 19.70 cr to negative Rs 51.47 cr, and that management deflected the cash flow question in all three tracked quarters. The draft used STAGNANT, which scores 0 rather than negative 1. On the DECLINING reading the composite falls from 3 to 2 and the band moves from DEEP WATCH to DEEP WATCH leaning AVOID.
What would prove it wrong: FY27 first half consolidated operating cash flow printing worse than the FY26 run rate.

**Ruling 8. ROCE is TEMPORARILY DEPRESSED backward and RECOVERING forward at roughly 55% probability.**
ROCE ran 22.06% in FY23, then 9.41%, then 7.83%, then 10.16% in FY26 (computed from screener-data on an operating basis excluding treasury other income). The collapse has a documented and specific cause: the September 2023 IPO raised about Rs 590 cr net and the FY24 to FY25 QIP about Rs 574 cr net (AR FY25 p.232 Note 35, p.233 Note 36), so capital employed rose roughly sevenfold from FY23 to FY26 while operating profit rose about 3.5 times. That is capital base dilution, which the framework names as a temporary cause. FY26 already recovered 232 basis points off the FY25 low.
Confidence: `genuinely uncertain`.
Both readings: the TEMPORARILY DEPRESSED reading rests on the documented cash bloat and the FY26 upturn. The STRUCTURALLY LOW reading is the letter of the rule, because an asset light business below 18% for three consecutive years (FY24, FY25, FY26) meets that definition, and the whole four year history is short. I used TEMPORARILY DEPRESSED. Both readings are non positive backward, so the backward composite is the same either way; the difference matters only for whether Pillar 1 may normalize at all.
What would prove it wrong: FY27 ROCE printing flat or lower while the idle cash stays idle.

**Ruling 9. Pillar 1 normalization uses Route A, the operational ROCE denominator fix, and the blend is skipped.**
The route test: QIP proceeds unutilised were Rs 382.84 cr at 31 March 2026 (results Q4 FY26 p.3, Note 4) against capital employed of Rs 1,458.86 cr (computed from screener-data), which is 26.2% and above the 20% threshold, so Route A applies. Route B conditions are also present because the ROCE verdict is TEMPORARILY DEPRESSED, so per the single credit rule Route B is suppressed and noted. On blending, the FY28 endpoint does not exist on an operational basis anywhere in this run's inputs, so under rule 9.1 the blend is skipped and operational ROCE feeds the formula alone.
I stripped only capital that carries a documented and dated deployment, per the staleness rule 9.2: DICE at about Rs 67.9 cr with asset purchase agreements executed 13 May 2026 and closing inside 120 days, and the Rs 50.0 cr Rivpe rights issue completed 2 April 2026. That is Rs 117.90 cr. The remaining idle cash stays in the denominator and is flagged to Role 3 as a capital allocation concern, because the IPO technology budget was only 35.6% deployed after two and a half years and the QIP only 14.6% deployed inside three months (B02, AR FY25 Note 35 p.232 and Note 36 p.292).
Confidence: `genuinely uncertain`.
Both readings: the conservative strip gives operational ROCE 11.05% and a Pillar 1 base of 13.0x. Stripping all non operating cash and investments of Rs 577.95 cr instead gives operational ROCE 16.82% and a base of 15.9x. The draft used the conservative strip because the staleness rule says undeployed capital without a dated plan stays in the denominator.
What would prove it wrong: a documented deployment schedule for the remaining QIP balance with dates inside 24 months.

**Ruling 10. Composite score is 3 out of 8, which is DEEP WATCH.**
Revenue plus 2, margin 0, cash 0, ROCE plus 1.
Confidence: `fairly sure`.
What would prove it wrong: either the cash reading moving to DECLINING, which takes it to 2, or margin guidance returning and cash turning, which takes it to 5.

**Ruling 11. The Kernex cap does not engage and the TRIM rule does not engage.**
No transition is DECLINING with catalyst strength NONE, so there is nothing to cap. TRIM requires all four transitions FIRING backward, and only one is.
Confidence: `sure`.
What would prove it wrong: reclassifying cash to DECLINING with catalyst NONE, which would engage the cap, though the score already sits at DEEP WATCH.

**Ruling 12. Undiscovered Alpha does not apply, and the hurdle tier is Tier A at 25%.**
UA needs all three qualifiers. Listed at least 12 months holds since September 2023. Gate 0 at or above 60 fails at 58 core, but Emerging Moat 26 clears the alternative branch. The third qualifier fails: the best available evidence puts FII at 2.31% and DII at 5.44% for June 2026, a combined 7.75%, well above the 3% ceiling. That evidence is an operator supplied screenshot and is NOT anchored, and the shareholding filing is absent from the run, so UA is withheld both because the test fails on the evidence available and because no filing can affirm it. On tiering, Tier B would need no structural cash flag, and the cash flag is unresolved rather than cleared, so Tier A stands as the default.
Confidence: `sure` on UA withheld, `fairly sure` on Tier A.
What would prove it wrong: a quarterly shareholding filing showing FII plus DII below 3%.

**Ruling 13. Position: DEEP WATCH, no starter position.**
Composite 3 is the wait for confirmation band. The thing being waited for is named in the verdict.
Confidence: `fairly sure`.
What would prove it wrong: two consecutive quarters of positive consolidated operating cash flow.

### Deliberation cap

Closed inside the 8 iteration cap. Three calls are tagged `genuinely uncertain` and reported as such rather than iterated further: the cash forward state (Ruling 7), the backward ROCE state (Ruling 8), and the Route A strip size (Ruling 9). Each names the single missing fact.

### Source availability, Step 0C

| Required input | Available | Note |
|---|---|---|
| Latest concall transcript | Yes | Q4 FY26, actual transcript, 13 May 2026 |
| Latest quarterly result filing | Yes | Q4 and FY26 audited, 13 May 2026 |
| Last 3 quarterly results | Partial | Only Q3 FY26 and Q4 FY26 filings in the run |
| Latest investor presentation | Yes | May 2026 |
| Recent exchange announcements | **No** | inputs/announcements absent, which is the documented action feed Step 2E depends on |
| Latest credit rating report | Yes | CARE A minus Stable, reaffirmed 4 March 2026 |
| Peer comparable data | Yes | Capillary, RateGain, Tanla, seven transcripts |

Two inputs missing, which is below the three input inconclusive threshold, so the protocol proceeds with confidence reduced. The announcements gap is the one that bites, because Step 2E grades documented action and that feed is absent. Prospectus is also absent, which matters for a company listed in September 2023, so the backward baseline runs on post listing years only and says so.

---

## 2. THE FOUR TRANSITIONS

**Reading the tables.** FY23 to FY26 columns are ACTUAL and anchored. FY27 to FY31 columns are EXPECTED and illustrative. They are built from management guidance where guidance exists and from a stated taper where it does not. They are not forecasts I am anchoring and they are not facts. FY22 is NOT FOUND throughout, because Zaggle listed in September 2023, the prospectus is absent from this run, and the screener history begins FY23.

### 2.1 Revenue growth

| Rs cr | FY22 | FY23 | FY24 | FY25 | FY26 | FY27E | FY28E | FY29E | FY30E | FY31E |
|---|---|---|---|---|---|---|---|---|---|---|
| Revenue | NOT FOUND | 553.46 | 775.60 | 1,303.76 | 1,907.65 | 2,671 | 3,338 | 4,006 | 4,807 | 5,528 |
| Growth % | NOT FOUND | ACTUAL | 40.1 | 68.1 | 46.3 | 40 | 25 | 20 | 20 | 15 |
| Basis | | ACTUAL | ACTUAL | ACTUAL | ACTUAL | guided | illustrative | illustrative | illustrative | illustrative |

Actuals are screener-data, consolidated, tied to results Q4 FY26 p.9. FY27E uses management's stated consolidated growth of about 40% (Q4 FY26 concall); FY28E onward is an illustrative taper with no management guidance behind it.

Quarterly revenue grew every quarter of FY26 against the year before: Q1 up 31.6%, Q2 up 42.8%, Q3 up 56.0%, Q4 up 49.9% (computed from screener-data quarterly). Three year CAGR is 51.08%. One caution that does not change the verdict: about 55% of gross revenue is Propel gift card resale carrying roughly 94% cost, so the number that describes the business is net revenue, and standalone net revenue still grew about 35% in FY26. Either basis clears the 20% bar comfortably.

**Backward FIRING. Forward FIRING.**

### 2.2 Margin

| % | FY22 | FY23 | FY24 | FY25 | FY26 | FY27E | FY28E | FY29E | FY30E | FY31E |
|---|---|---|---|---|---|---|---|---|---|---|
| Gross operating margin | NOT FOUND | 8.70 | 9.11 | 8.75 | 9.70 | 9.7 | 10.0 | 10.5 | 11.0 | 11.5 |
| Basis | | ACTUAL | ACTUAL | ACTUAL | ACTUAL | not guided | illustrative | illustrative | illustrative | illustrative |

Actuals computed from screener-data. Adjusted EBITDA margin on the net revenue basis, which is the comparable one, was 19.9% in FY25 and 21.7% in FY26 (investor presentation May 2026 slide 9). Management's long run target is 14% to 15% adjusted EBITDA, stated variously as 4 to 5 years, 5 to 7 years, and next 5 years across three consecutive calls.

The two year move on the gross basis is plus 59 basis points, inside the stability band. On the net basis the level is healthy against the peer set. Against that, three things point the other way: FY27 EBITDA guidance was withheld pending DICE integration, which is a retreat from FY26's specificity; the incentive and cashback ratio moved to about 68% of program fees against a stated glide toward 50%; and Propel gross margin fell to 4% in Q4 FY26 versus the 7% to 9% recovery promised back in Q2 FY25, with the recovery target itself lowered to about 5.5%. Quarterly gross margin also slipped for two straight quarters, from 10.17% in Q2 FY26 to 9.93% then 9.44%.

**Backward SUSTAINED. Forward STAGNANT.**

### 2.3 Cash conversion

| Rs cr | FY22 | FY23 | FY24 | FY25 | FY26 | FY27E | FY28E | FY29E | FY30E | FY31E |
|---|---|---|---|---|---|---|---|---|---|---|
| PAT | NOT FOUND | 22.90 | 44.02 | 87.92 | 138.08 | 193 | 240 | 288 | 346 | 398 |
| CFO | NOT FOUND | -15.62 | -82.75 | 19.70 | -51.47 | 39 | 96 | 144 | 208 | 239 |
| CFO/PAT | NOT FOUND | -0.68 | -1.88 | 0.22 | -0.37 | 0.20 | 0.40 | 0.50 | 0.60 | 0.60 |
| Debtor days | NOT FOUND | 67.7 | 82.2 | 60.2 | 69.1 | 69 | 68 | 66 | 65 | 65 |
| Net debt | NOT FOUND | 118.75 | -192.68 | -633.46 | -491.13 | illustrative | illustrative | illustrative | illustrative | illustrative |
| Basis | | ACTUAL | ACTUAL | ACTUAL | ACTUAL | part guided | illustrative | illustrative | illustrative | illustrative |

Actuals from screener-data, cross checked to results Q4 FY26 p.11. Negative net debt is net cash. FY27E CFO reflects management's stated intent that operating cash flow turns positive in FY27; everything past FY27 is an illustrative path showing what a real cash transition would look like, not a prediction that it happens.

This is the transition the whole case turns on. Cumulative operating cash flow across four years is negative Rs 130.14 cr against cumulative PAT of Rs 292.92 cr, a ratio of negative 0.44. Free cash flow in FY26 was negative Rs 158.58 cr, the worst of the four years, against reported PAT of Rs 138.08 cr, with capex of about Rs 107 cr almost entirely capitalised development cost. Receivables grew from Rs 102.66 cr to Rs 361.18 cr over the window while debtor days stayed roughly flat at 67.7 to 69.1, so the receivables build is volume driven rather than a collection collapse. The balance sheet remains net cash at Rs 491.13 cr, so nothing here is a solvency question. It is an earnings quality question.

**Backward DETERIORATING. Forward STAGNANT. Determination INDETERMINATE.**

### 2.4 ROCE and capital efficiency

| | FY22 | FY23 | FY24 | FY25 | FY26 | FY27E | FY28E | FY29E | FY30E | FY31E |
|---|---|---|---|---|---|---|---|---|---|---|
| EBIT (Rs cr) | NOT FOUND | 41.93 | 62.29 | 99.27 | 148.16 | 207 | 273 | 350 | 448 | 542 |
| Capital employed (Rs cr) | NOT FOUND | 190.10 | 662.01 | 1,267.85 | 1,458.86 | 1,720 | 2,010 | 2,330 | 2,690 | 3,080 |
| ROCE % | NOT FOUND | 22.06 | 9.41 | 7.83 | 10.16 | 12.0 | 13.6 | 15.0 | 16.7 | 17.6 |
| Basis | | ACTUAL | ACTUAL | ACTUAL | ACTUAL | illustrative | illustrative | illustrative | illustrative | illustrative |

Actuals computed from screener-data. EBIT is operating profit less depreciation and excludes other income, which is largely treasury interest on IPO and QIP cash and would otherwise flatter the ratio. Capital employed is equity share capital plus reserves plus borrowings. No management ROCE guidance exists, so every forward column here is illustrative.

The shape is the story. ROCE was 22.06% in FY23 on a small pre listing capital base, collapsed to 7.83% by FY25 as roughly Rs 1,164 cr of IPO and QIP money landed on the balance sheet, and recovered 232 basis points to 10.16% in FY26. Rs 382.84 cr of QIP proceeds were still unutilised at 31 March 2026. Against the recovery sit real counter forces: the Span Across acquisition put Rs 36.35 cr of goodwill on the books for a target that was loss making with negative net assets in its post acquisition stub period, roughly Rs 107 cr a year of capitalised development cost keeps adding to the capital base, and both DICE and the Rivpe consumer business are loss making going in.

**Backward TEMPORARILY DEPRESSED. Forward RECOVERING at roughly 55%.**

---

## 3. THE CATALYST STORY IN PLAIN WORDS

**What could make revenue keep firing.** Two acquisitions are already documented rather than promised. Zaggle bought 100% of Rivpe, now Zagg.money, completing equity in March 2026 and the preference shares by 11 June 2026, and put Rs 50 cr of fresh capital into it in April 2026. It restructured the DICE deal from a Rs 123 cr share purchase into a roughly Rs 68 cr asset and intellectual property purchase, with the agreements executed on 13 May 2026 and closing inside 120 days. Both add revenue mechanically once consolidated. Management guides FY27 consolidated growth of about 40%. What confirms it: FY27 quarterly revenue holding above 25% year on year with DICE revenue disclosed separately. What kills it: the DICE closing conditions failing, or bank partners repricing the interchange share.

**What could make margin move.** The honest answer is that nothing documented is pushing margin up right now. The DICE platform is described as AI enabled SaaS at roughly 95% gross margin, but that is a management claim about an unclosed asset, and DICE is loss making enough that Zaggle lent it Rs 10 cr before closing. Management withheld FY27 EBITDA guidance entirely pending integration, which is the opposite of a catalyst. The incentive and cashback ratio is moving away from the target, not toward it. What confirms a turn: FY27 EBITDA guidance reissued at or above the old 10% to 11% band and the incentive ratio printing below 65%. What kills it: another quarter of Propel take rate below 4%.

**What could make cash convert.** One real thing has happened and it is not a promise. Management changed the Propel redemption model specifically to cut cash intensity, and they paid for it visibly: Propel gross margin fell from about 10% to 4%. Standalone quarterly operating cash flow improved from roughly negative Rs 33 cr to roughly negative Rs 6 cr across FY26. That is action, not vision, which is why this transition scores 0 rather than negative 1. What is missing is everything the framework normally wants: no factoring facility, no receivables discounting line, no debtor day target that has actually been hit, and no consolidated cash flow bridge. Management deflected the cash flow question in all three tracked quarters. What confirms it: consolidated operating cash flow crossing zero in FY27. What kills it: FY27 first half consolidated cash flow worse than FY26.

**What could make ROCE recover.** The mechanism is arithmetic, not operational. Rs 382.84 cr of raised money sits idle inside capital employed and earns treasury interest that the ROCE calculation deliberately excludes. Deploying it into operating assets lifts the ratio from both ends. DICE and Rivpe are exactly that deployment and both are documented and dated. What confirms it: FY27 ROCE printing above 12% with the unutilised QIP balance falling. What kills it: the balance still sitting idle at FY27 year end, or acquisitions adding goodwill faster than they add operating profit.

**One absence worth naming.** Zaggle had already advanced Rs 36.14 cr toward the Effiasoft acquisition with a further Rs 5.27 cr committed (AR FY25 Note 31(b) p.229-230). The board decided not to proceed on 3 April 2026. Whether that Rs 36.14 cr comes back, and on what terms, is NOT FOUND in this run's inputs. For a company whose entire open question is cash, an unexplained Rs 36 cr is worth tracking.

### Step 2E, management intent and action ledger

The documented action feed, inputs/announcements, is absent from this run. The ledger below therefore runs on results filings, the annual report, concall evidence, and the web confirmed items in B08, and it cannot fully grade recent exchange filed action. Confidence is lowered accordingly.

| Transition | Vision (spoken) | Documented action | Promise vs delivery discount | Too conservative? | Adjustment |
|---|---|---|---|---|---|
| Revenue | FY27 about 40% consolidated; $1bn in 5 to 7 years | Rivpe 100% closed; Rs 50 cr rights issue funded; DICE agreements executed 13 May 2026 | Applies, DICE slipped roughly 6 months and was repriced | Already at maximum | none, FIRING holds |
| Margin | DICE at roughly 95% gross margin; incentive ratio to 50% | NONE. FY27 EBITDA guidance withheld | Applies, Propel 7 to 9% recovery promised Q2 FY25 and missed | No, vision without action | none, STAGNANT holds |
| Cash | Operating cash flow positive in FY27 | Propel redemption model changed and paid for in margin; standalone quarterly cash flow improved to about negative Rs 6 cr | Applies, FY26 consolidated breakeven missed | Yes, enough to hold at STAGNANT rather than DECLINING | already reflected, no further move |
| ROCE | Capital will be put to work | Rs 117.90 cr deployed or committed with dates; Rs 382.84 cr still idle at 31 March 2026 | Applies, deployment has run chronically slow | Balanced, deployment is real and so is the idle balance | none, RECOVERING holds |

The ledger loosened nothing. On cash it supported holding at STAGNANT instead of dropping to DECLINING, which is the one place documented action changed a state, and that action is already inside the Step 2 scoring rather than patched on afterwards.

---

## 4. STEP 3 SCORECARD AND STEP 4 VERDICT

| Transition | Backward verdict | Catalyst strength | Forward probability | Forward verdict | Score |
|---|---|---|---|---|---|
| Revenue growth | FIRING | Strong | 80% (3 to 6m) | FIRING | +2 |
| Margin expansion | SUSTAINED | Weak | 35% (3 to 6m) | STAGNANT | 0 |
| Cash conversion | DETERIORATING | Weak | 30% (3 to 6m) | STAGNANT | 0 |
| ROCE / capital efficiency | TEMPORARILY DEPRESSED | Moderate | 55% (12m) | RECOVERING | +1 |
| | | | | **COMPOSITE** | **+3 / 8** |

Backward composite: 2 positive of 4, which is BACKWARD WEAK.
Kernex cap: not engaged, no transition is DECLINING with catalyst NONE.
TRIM rule: not engaged, only one transition is FIRING backward.

### THE VERDICT

Zaggle scores 3 out of 8, which is DEEP WATCH, wait for confirmation. Revenue is genuinely firing and the ROCE trough is a documented capital bloat that is starting to unwind, but margin has no catalyst and management pulled its own guidance, and cash conversion has produced negative Rs 130 cr of operating cash flow against Rs 293 cr of reported profit over four years. Neither the Kernex cap nor the TRIM rule engaged; the score got here on its own. The whole call turns on one print: consolidated operating cash flow in FY27, because a business that compounds revenue at 50% while consuming cash is an accounting transition until the cash arrives, and the moment it arrives this becomes a materially different name.

---

## 5. STEP 5 MONITORING TRIGGERS

| # | Trigger | Threshold | Horizon | What it changes |
|---|---|---|---|---|
| 1 | Consolidated operating cash flow | Crosses zero for a full half year | H1 FY27 | Cash to STARTING, composite to 4, disposition cap lifts |
| 2 | Consolidated CFO/PAT | Above 0.50x for two consecutive halves | 12 months | Cash to FIRING, composite to 5, BUY candidate band |
| 3 | Incentive and cashback ratio | Below 65% of program fees | 2 quarters | Margin catalyst becomes real, margin to STARTING |
| 4 | Propel gross margin | Above 5.5% for two quarters | 2 to 3 quarters | Confirms the redemption model change worked |
| 5 | FY27 EBITDA guidance | Reissued at or above 10% | Next 1 to 2 calls | Removes the guidance retreat, margin to STARTING |
| 6 | Unutilised QIP balance | Falls below Rs 150 cr with deployment disclosed | 12 months | Pillar 1 strip widens, ROCE base rises materially |
| 7 | Reported ROCE | Above 12% on the FY27 annual print | 12 months | ROCE recovery confirmed, moves toward FIRING |
| 8 | Net revenue growth excluding Propel pass through | At or above 25% year on year | Each quarter | Confirms revenue FIRING is real and not gross optics |
| 9 | Catalyst absence test: cash flow question in the next concall | Management again gives no dated consolidated cash flow bridge | Next call | Catalyst stays Weak, cash cannot rise above STAGNANT |
| 10 | Effiasoft advance | Rs 36.14 cr recovered, written off, or still unexplained | Next annual report | Unexplained or written off reinforces the cash and governance read |
| 11 | Trade receivables | Growing faster than net revenue for two quarters | 6 months | Moves cash determination from INDETERMINATE toward structural |

Re-engagement rule: if three or more of these fire favourably and cash shows directional improvement, re-run FTTCP in full and the band may upgrade one step.

---

## 6. HANDOFF TO VALUATION

| Field | Value |
|---|---|
| ROCE forward verdict | RECOVERING, probability roughly 55% (40 to 60% band) |
| Pillar 1 normalization route | A-Operational (Route B condition also present, suppressed per single credit rule) |
| Statutory ROCE FY26 | 10.16% |
| Stripped items | DICE Rs 67.90 cr (agreements 13 May 2026), Rivpe rights issue Rs 50.00 cr (2 April 2026). Total Rs 117.90 cr |
| Operational ROCE | 11.05% |
| Blend basis | Blend skipped, FY28 operational endpoint NOT FOUND (rule 9.1) |
| Pillar 1 ROCE for Role 1 | 11.05% |
| ROCE recovery credited via | Pillar 1. Strategic Premium ROCE re-rating route is BARRED |
| Cash multiplier band | 0.80x, no growth offset, because the determination is INDETERMINATE |
| Sector cap row Phase 3 must use | CPaaS / Communications platform, 28x (corrected from Platform / SaaS / IT services 45x) |
| Hurdle tier | Tier A, 25% |
| UA applied | No, FII plus DII roughly 7.75% fails the under 3% qualifier |
| SHARED CATALYST flag | Yes. DICE closing and integration drives both the revenue FIRING verdict and the ROCE RECOVERING verdict. Role 3 must stress test it as a single point of failure |
| Capital allocation flag to Role 3 | Rs 264.94 cr of raised capital remains idle with no dated deployment plan and fails the 24 month staleness test |

---

## 7. THE P/E BASE CARD, FOR OPERATOR APPROVAL

This is a preview of the exit multiple base computed from what is known now. It is not the valuation. Role 1 still runs the full dual track exercise in Phase 3.

| Step | Calculation | Value |
|---|---|---|
| A. Pillar 1 ROCE base | Operational ROCE 11.05%, formula 0.5 x 11.05 + 7.5 | 13.0x |
| B. Pillar 2 cash multiplier | Cumulative CFO/PAT -0.44, FY26 CFO negative, FCF negative. Band 0.80x. Determination INDETERMINATE so no growth offset | 0.80x |
| C. Quality adjusted base | A x B | 10.4x |
| D. Pillar 3 growth and moat premium | 3a growth visibility +0x (only 1 of 4 criteria qualifies, delivery grade C), 3b moat formation +1x (EM 26 in the 25 to 29 band), 3c duration +0x (no documented order book) | +1x |
| E. Strategic premium | No regulatory monopoly, pricing power moderate, ROCE route barred by single credit, institutions net selling | +0x |
| F. Raw destination PE | C + D + E | 11.4x |
| F2. UA adjusted | UA not qualified, F2 = F | 11.4x |
| G. Sector cap | CPaaS / Communications platform | 28x |
| **H. Final destination PE, Track 2 additive** | **min(F2, G)** | **11.4x** |

**Track 2 additive destination PE: 11.4x, range 10.5x to 12.5x** (plus or minus 7.5%, rounded to nearest 0.5x).

**Track 1 RRM destination PE.** Base r for a small cap is 14%, adjusted to 15% for governance (delayed statutory filings and an NSE warning in FY25, non audit fees above audit fees, CFO and CTO both departing in 2026, credibility grade C). RRM = 1 + (13.5 − 15.0) x 0.12 = 0.82, inside the 0.70 to 1.60 bounds. Applied to the quality adjusted base of 10.4x gives **8.5x, range 8.0x to 9.0x**.

The two tracks diverge by about 34%, which is well past the 15% materiality line. Under the framework the more conservative track sets the entry zone, which would be Track 1. Role 1 must state which track governs and why.

**The number that matters most.** Zaggle trades at Rs 203 on FY26 consolidated EPS of Rs 10.27, which is 19.8x trailing. Both tracks put the destination multiple below the current multiple. That means this analysis is pricing a de-rating, and any return has to come from earnings growth outrunning that de-rating. Role 1's Hurdle Ratio test is where that gets settled.

**Provisional on these inputs:** the cash multiplier is provisional on the structural versus growth induced determination. If the operator rules GROWTH-INDUCED, the offset for PAT CAGR above 40% is plus 0.20, the multiplier becomes 1.00x, and the raw destination PE moves from 11.4x to 14.0x. That single ruling is worth about 23% on the exit multiple, and it is the operator's call at this gate.

### THE EARNINGS BASIS QUESTION

This is the operator's decision and I am not making it.

**Option 1, one year forward P/E.** Apply the multiple to FY27 expected EPS. Fits a business consolidating two acquisitions that are not in trailing earnings at all, growing revenue about 40%, where trailing understates the earnings base by construction.

**Option 2, trailing P/E.** Apply the multiple to FY26 reported EPS of Rs 10.27. Fits a business where earnings quality is the open question: roughly Rs 107 cr a year of development cost is capitalised rather than expensed, other income was 22.6% of consolidated profit before tax and is treasury interest on idle cash, and Q4 FY26 standalone profit grew 18% against revenue growth of 44% as the depreciation from that capitalisation started biting. Forward earnings from a management graded C on delivery carry a discount that trailing does not.

Both are defensible here and the choice moves fair value materially. Operator decides.

---

*FTTCP v1.2 draft. Composite 3 of 8, DEEP WATCH. Cash determination INDETERMINATE, which caps disposition at PROCEED WITH CAVEATS. Awaiting operator review, destination PE approval, and the earnings basis choice.*
