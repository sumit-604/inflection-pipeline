# Chunk 16. FTTCP v2.3 verdict logic and the Part B handoff

Loaded by: FTTCP Part A (transition proof) and Part B (normalization); Role 1 inputs. Pipeline: /fttcp command; the claude.ai FTTCP run; stage 11 reads the ROCE forward verdict, the composite, the C.2 table and the Part B Output Sheet.
Sources in force: FTTCP_v2_1_Consolidated.md (content v2.3); Master v3.7 pipeline position and consumption clause.

## Position and gates

- FTTCP is a pre-valuation discipline gate. Sequence: Gate 0 + Emerging Moat → Role 4 → Role 5 → Role 5.5 → Debt Capacity → FTTCP (Part A then Part B) → Market-Implied → Role 1 → Role 2 → Role 3 → Notion save.
- Role 1 Pillar 1 cannot be computed without the FTTCP ROCE forward verdict.
- **Signal Gate.** Role 5.5's Step 4 HARD GATE must have passed: signals physically written to the Downstream Signal Tracker with row URLs as proof. A catalyst with no Downstream Signal anchor is evidence-thin and its magnitude caps at MODERATE. Zero identifiable signals caps the composite at DEEP WATCH.
- **Concall Gate.** Role 5 on the latest actual transcript precedes FTTCP. Without one, FTTCP runs with the limitation flagged and confidence materially reduced; catalysts are never built from MD&A or presentation narrative.
- **Survivorship guard.** Scorn, cheapness and long incubation argue that the PRICE is wrong only AFTER the fundamentals gate (the FTTCP verdict, the hard binary gate, the fired downstream signal) has passed. Never a substitute for it.

## Step 0: pre-flight

- 0A: first workup (Role 1 fields N/A) or quarterly refresh (fetch Decision Status, baseline, thesis, DA findings, promoter verdict, Role 5 grade, prior Role 1, last four quarterly entries, last Role 5 output, prior FTTCP triggers).
- 0B: verify Decision Status before any position-action language; state the forward intent tested.
- 0C: source check (latest actual transcript; latest results filing with full notes; last three results; latest presentation; last 90 days of exchange announcements; latest credit rating report; at least one true peer). Three or more missing → declare FTTCP inconclusive, or proceed with a declared low-confidence verdict.
- 0D windows: primary 3 months; secondary 6 months; extended 12 months, which is the PRIMARY window for ROCE.
- 0E: standard operating business or lender (lender transition set below).

## Step 1: backward baseline

| Transition | Verdict definitions |
|---|---|
| Revenue | FIRING: 3-yr CAGR ≥20% AND last 4 quarters positive YoY. STAGNANT: 3-yr CAGR 0-10% OR last 4 quarters mixed. DECLINING: 3-yr CAGR negative OR last 2 quarters negative YoY. VOLATILE: variance too high to read |
| Margin | FIRING: expansion >300 bps over 2 years AND below peer ceiling. SUSTAINED: within ±150 bps over 2 years at ≥ peer median. COMPRESSING: contraction >150 bps over 2 years. VOLATILE |
| Cash conversion | FIRING: CFO/PAT >0.70x AND debtor days stable or compressing. IMPROVING: CFO/PAT moving from <0.50x toward >0.50x over 2 years with debtor days compressing. STAGNANT: CFO/PAT 0.40-0.60x, no trend. DETERIORATING: CFO/PAT declining OR debtor days expanding meaningfully |
| ROCE | FIRING: >25% AND expanding ≥200 bps a year for 2+ years. SUSTAINED: within ±200 bps over 2 years at >20% asset-light / >18% asset-heavy. TEMPORARILY DEPRESSED: collapsed >500 bps in 12 months with identifiable temporary causes. DECLINING: contracting >300 bps over 2 years with no temporary catalyst. STRUCTURALLY LOW: below 15% for 3+ years (asset-heavy) or <18% (asset-light) |

- ROCE judgment test: "If the company stopped growing tomorrow, would ROCE recover to historical levels within 18-24 months?" YES → TEMPORARILY DEPRESSED. NO → DECLINING or STRUCTURALLY LOW. When in doubt, DECLINING.
- Positive backward verdicts: FIRING, SUSTAINED, IMPROVING. All others are not positive.
- Backward status: 4 positive → BACKWARD PASS; 3 → PARTIAL; 2 → WEAK; 0-1 → FAIL (default toward AVOID).
- Converters: cash trends on volume-denominated WC only (chunk 11).

## Step 2: forward catalyst analysis, per transition, Sections A → D

- A: current trajectory, latest data point, peer leader and median, sector direction.
- B: 3-5 specific catalysts with evidence type, what confirms firing, what kills it. "NONE FOUND" is valid and significant. Evidence weights: 📄 full confidence; 🎙️ discount 30-50% by track record; 🔍 discount 50-70%. A past promise missed on the same item adds a further 20% discount. Sector tailwind alone does not count.
- C: probability bands HIGH >60% | MODERATE 30-60% | LOW 10-30% | VERY LOW <10%. Magnitude HIGH (shifts a verdict band) / MODERATE / LOW. **Composite P = P(best single Moderate+ catalyst) + 10% per additional independent Moderate+ catalyst, maximum +20%, hard cap 90%.** Independent means no shared failure mode. Low-magnitude catalysts never add.
- C.2: the valuation-facing probability table, downside row mandatory (chunk 09).
- D forward verdict mapping (hybrid labels banned; round down when between states):
  - probability >60% AND catalyst strength ≥ Moderate AND backward verdict positive → FIRING
  - probability >40% with at least one Moderate catalyst, not yet confirmed in reported numbers → STARTING (ROCE: RECOVERING)
  - probability 20-40% → STAGNANT
  - probability <20% or going the wrong way → DECLINING
  - A TEMPORARILY DEPRESSED ROCE yields RECOVERING, not FIRING, until the recovery prints.

## Step 2E: Management Intent-and-Action Ledger

Runs after 2A-2D and before the scorecard. It checks whether documented action argues a verdict is too harsh.

- VISION = words (🎙️, discounted 30-50%). Vision alone never moves a verdict.
- ACTION = documented moves (📄): closed acquisition, commissioned line, sanctioned and operational factoring facility with amount and date, a debtor-day target actually hit, capex deployed, divestment closed, rating action. Full weight, less the promise-vs-delivery discount (a further 20% where this management missed on this dimension).
- Only net-📄 action loosens a verdict, by ONE state, via a return to Step 2B for re-scoring. Never leapfrog.
- Vision without action CONFIRMS the Step 2 verdict, including a conservative one.
- 2E does not tighten a verdict below Step 2 and does not manufacture optimism.
- The Kernex cap lifts only if 2E surfaces real 📄 action on that transition (the catalyst was NONE-in-error and is re-scored).
- 📄 feed: `inputs/announcements/`, `inputs/prospectus/`, results filings, the Role 5 tracker. Without announcements, 2E runs on concall/AR evidence, says so, and lowers confidence.

Ledger columns: Transition | Stated vision (🎙️) | Documented action (📄, source) | Promise-vs-delivery discount | Argues verdict too harsh? | Verdict adjustment (none / +1 state via re-score).

## Steps 3 and 4: scorecard and scored verdict

| Forward verdict | Score |
|---|---|
| FIRING | +2 |
| STARTING / RECOVERING | +1 |
| STAGNANT | 0 |
| DECLINING | −1 |

Composite = sum across four transitions, range −4 to +8.

| Composite | Position decision |
|---|---|
| 7-8 | STRONG BUY-candidate; MEDIUM-LARGE sizing if other gates clear |
| 5-6 | BUY-candidate; SMALL-MEDIUM sizing |
| 4 | DEEP WATCH leaning BUY-ON-DIPS; small starter defensible with strict entry zone |
| 3 | DEEP WATCH; wait for confirmation |
| 1-2 | DEEP WATCH leaning AVOID; extreme margin of safety required |
| ≤0 | AVOID / Hard AVOID |

- **Kernex cap:** any transition with forward DECLINING AND catalyst strength NONE caps the composite verdict at DEEP WATCH regardless of score.
- **TRIM/REDUCE:** all four FIRING backward + 2 or more with declining forward catalyst strength → TRIM/REDUCE, independent of score.
- **Override:** only for an override-worthy specific catalyst (binding acquisition announcement, regulatory monopoly award), documented in Notion with reasoning, and re-validated next quarter. "Strong management" and "great sector" are not override conditions.

## Lender transition set (banks, NBFCs, MFIs, HFCs)

| # | Lender transition | FIRING threshold (indicative) | Replaces |
|---|---|---|---|
| 1 | AUM / disbursement growth | AUM CAGR ≥20% with disbursements accelerating | Revenue |
| 2 | NIM / spread | NIM stable or expanding at ≥ peer median; cost of funds favourable | Margin |
| 3 | Asset quality (the critical one) | Credit costs within guided band 4+ quarters; GNPA stable/declining; collection efficiency ≥98% | Cash conversion |
| 4 | RoA / RoE trajectory | RoA ≥ archetype benchmark (MFI ~3%, NBFC ~2.5%, bank ~1.2%), rising or sustained | ROCE |

Transition 3 inherits every cash-conversion rule, including the silence diagnostic and the Kernex cap. Pillar 2L must be consistent with it (chunk 02).

## Step 4.5: Second-Order Section (Rule F) and Step 5: monitoring triggers

- Minimum five chains, each from a Step 2 forward catalyst or a firing Step 1 transition, at least two links out, a labelled [INFERENCE] in every chain, four questions (who pays and why now / what binds / what moves if it works / what was not said). "What binds" draws on Step 2E and the Part B sheet. Live-web links are PENDING LIVE VERIFICATION, never fabricated. Every confirm-by line feeds the Expectation Ledger and becomes a candidate Step 5 trigger.
- Step 5: minimum 5, ideally 8-10 specific, measurable triggers with horizon and explicit change condition, covering all four transitions, including one catalyst-absence trigger.
- Re-engagement: 3+ triggers fire favourably AND the missing transition improves → full re-run. A missing transition's forward probability moving from <30% to >50% may upgrade the position decision by one band.

## Pillar 1 handoff line

"ROCE verdict: ___ → Pillar 1 ROCE: ___%; recovery credited via: ___" (selection table and single-credit rule in chunks 01 and 04).

## Part B handoff: the Normalization Output Sheet (Role 1 consumes, never recomputes)

| Module | Output | Where it lands |
|---|---|---|
| Cyclical flag | YES/NO; cycle years; base = full-cycle average, bear = trough, bull = peak margins | chunk 07 margin rules |
| B1 Reinvestment funding | funding channel per year, pass/fail | chunk 07 projections; chunk 13 debt verdict cross-check |
| B2 ROCE crossover | ROCE path Y1/Y2/Y3; minimum ROCE and source; "growth premium eligible: YES from FY__ / NO" | chunk 12 (A16 gate) |
| B3 Base-year EPS | reported, normalized, basis (or "not applicable") | chunk 01 / 04 single credit with Route B |
| B4 Operating EPS | operating EPS; stripped items with ₹ Cr | chunk 08 earnings base; chunk 14 |
| B5 Incentives | incentive expiries; post-expiry margin and EPS for Year 3 | chunk 07 |
| B6 Restated efficiency | statutory vs restated ROCE; restated EPS; amortizable life (default 5 years); route declaration | chunk 01 / 04 single credit with Routes A/B |
| B7 Deleveraging | net debt Y0-Y3; post-delever EPS; Year 3 net debt for the EV bridge | chunk 13; chunk 15 EV/EBITDA |
| B8 Re-rating potential | HIGH / MODERATE / NONE; convergence target; binary gate | chunk 15 relative PE; chunk 06 range placement |

Every module that meets a NOT FOUND number says so and hands NOT FOUND forward. No module estimates.

## Methodological discipline (never violated)

1. No catalyst counts as a catalyst; write NONE FOUND when accurate.
2. Sector tailwinds are not company catalysts.
3. Management narratives take a 30-50% discount without operational evidence.
4. Past delivery discounts current promises.
5. Two missing transitions almost never fix together; sequence revenue → margins → cash → ROCE.
6. Two consecutive silent concalls on a missing transition is decisive.
7. Confirmation-bias check: would the same forward conclusion follow with no prior position?
8. Concall Gate mandatory.
9. Bands, not false precision; composite cap 90%.
10. The output is the work product; a verdict without populated tables is invalid.
11. ROCE is a 12-month transition.
12. TEMPORARILY DEPRESSED vs DECLINING is the critical ROCE judgment; bias toward DECLINING when in doubt.
13. The re-rating premium is archetype-dependent.
14. Hybrid labels are banned; round down; ambiguity resolves conservatively; scores are never promoted.
15. Single credit for ROCE recovery, stated in writing.
16. Intent-and-action is a cross-check, not a licence.
