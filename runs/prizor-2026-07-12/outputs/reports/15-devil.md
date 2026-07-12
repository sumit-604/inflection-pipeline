# STAGE 15 — ROLE 3 DEVIL'S ADVOCATE: PRIZOR VIZTECH LTD

**Run date:** 2026-07-12 | **Model:** claude-opus-4-8 | **Framework:** Master v3.3 Role 3 / Section 1B v3.3 / FTTCP v1.2
**Mode:** pipeline (interim states written, no stops). Exit-multiple authority: Section 1B v3.3 ONLY.
**Inputs attacked:** 14-thesis.md (B14, verdict AVOID), B01-B11 blocks, 11-valuation.yaml (Role 1 authoritative), fttcp-deliberation.md (authoritative).

```
═══════════════════════════════════════════════════════════
DEVIL'S ADVOCATE: PRIZOR VIZTECH LTD
"Every investment thesis is wrong. The question is how."
═══════════════════════════════════════════════════════════
```

## PIPELINE-MODE CHECKPOINT LINE

Interim (framework says report then continue): "The thesis under attack is an AVOID, so this role runs two-sided. I stress the AVOID first (is there a bull rescue the pipeline under-weighted), then stress the company's own bull narrative (which claims are most fragile). Headline finding: the AVOID DIRECTION survives even a maximally generous bull reconstruction, but its MAGNITUDE (base fair value Rs 154, expected CAGR -45.4%) is fragile because it is anchored to stale FY25 audited EPS Rs 9.495; on unaudited FY26 the same math gives ~29x, not 87x. Every bull rescue and every fragility resolve on the SAME single event: the FY26 audited cash-flow statement. Proceeding through all sections."

Note on dimension semantics: each dimension is rated for whether the AVOID thesis SURVIVES the strongest two-sided attack. SURVIVES = the AVOID stance holds on that axis. DESTROYED = a credible case overturns the AVOID on that axis. This is the correct reading of Role 3 when the thesis under test is AVOID.

---

## 1. THESIS DESTRUCTION — Point by Point (two-sided)

### 1A. Attacking the AVOID (strongest bull rescue against each AVOID leg)

| AVOID Argument (from B14) | Bull Counter-Argument (strongest rescue) | Strength |
| --- | --- | --- |
| "Trades at 87x FY25 audited EPS Rs 9.495 vs 15x destination" (B11, B14 §1) | The 87x uses year-old audited earnings for a company whose unaudited FY26 PAT tripled (fttcp ruling 7) and revenue rose +108% (B05). On the unaudited FY26 print (revenue ~Rs 148 Cr, PAT ~Rs 30 Cr, EPS ~Rs 28.5) the trailing multiple is ~29x, not 87x. The "5x overvalued" framing is an artefact of the audit lag. | **Strong** on magnitude, Weak on direction |
| "Cumulative CFO/PAT -1.02x; cash structurally broken" (B02, B10) | Cash multiplier 0.65x was a CONSERVATIVE DEFAULT because the rating WC quote is NOT FOUND and cash is INDETERMINATE, not confirmed structural (B11 input_gaps; fttcp ruling 5 "genuinely uncertain on structural vs growth"). If the drag is growth-induced, framework gives 0.80x + a +0.20 offset (>40% CAGR) = 1.00x, which lifts the quality-adjusted base from 15.0x to 23.1x and roughly doubles fair value (Section 1B Pillar 2). | **Moderate** (evidence leans structural; see 1B) |
| "Margins 21-23% exceed CP Plus 13.7%, so contradicted" (B06) | Prizor is a smaller, backward-integrated assembler (in-house SMT/PCB, 50 lakh PCB units p.a., B05 slide 13); a niche player can out-margin a scaled generalist on mix. CP Plus's own best quarter hit 18.0% EBITDA (B06). The gap is not physically impossible, only undisclosed. | **Weak-Moderate** |
| "Hurdle Ratio 0.23/0.27 STOP; 25% CAGR infeasible even on bull earnings" (B11) | HR uses the stale FY25-anchored current PE of 87x. Re-based to unaudited FY26 (~29x), and crediting ROCE recovery + growth-induced cash, the destination could reach the 25x sector cap; on that footing the overvaluation shrinks to ~14% today, not ~90%. | **Moderate** on magnitude |
| "Expected CAGR -45.4%; every one of 9 cells <15% CAGR" (B11, B14 §5) | Same objection: the 3x3 matrix is built off FY25 EPS Rs 9.495 as Year-0. Shift Year-0 to audited-if-confirmed FY26 EPS ~Rs 28.5 and the entire ladder moves up ~3x; base fair value ~Rs 460, not Rs 154. | **Strong** on magnitude, Weak on direction |

**Verdict on the AVOID after the bull rescue:** the DIRECTION survives (see the decisive table in Section 3), but the pipeline's stated MAGNITUDE (-45.4% CAGR, 72-91% below CMP) is the weakest, most attackable number in the whole workup because it uses FY25 earnings for an FY26-transformed (if unaudited) company. A devil must flag this: the honest AVOID is "~14% to ~50% overvalued depending on the FY26 audit," not "~90% overvalued." The pipeline is correct per framework to exclude unaudited numbers, but the resulting headline overstates the certainty of the downside.

### 1B. Attacking the COMPANY NARRATIVE (strongest bear counter against each bull claim)

| Bull / Company Claim | Bear Counter-Argument | Strength |
| --- | --- | --- |
| "FY26 PAT tripled, revenue +108%, EBITDA +121%" (B05, fttcp 7) | Unaudited investor-presentation figures, and the SAME Apr-2026 deck reports FY26 ROCE as both 47.4% (cover) and 37.2% (chart), 38.0% vs 35.5% ROE (B05, B10 FLAG-INTERNAL-ROCE-INCONSISTENCY). A company that cannot reconcile its own headline return within one document has not earned belief on its unaudited profit. | **Strong** |
| "21-23% EBITDA / 14% PAT margins" (B04, B05) | Contradicted in every quarter by the only scaled direct peer: CP Plus FY26 full-year EBITDA 13.7%, PAT 8.72%, FY27 guide 14-15% called "the new normal" (B06 contradicted). No disclosed unit-cost or mix advantage explains an ~800 bps EBITDA premium over the category leader. If margins revert to peer, FY26 PAT is far below the tripled claim. | **Strong** |
| "PAT tripled = the business is compounding" | PAT tripled but operating cash flow did NOT recover (fttcp ruling 5: "FY26 did not recover as PAT tripled"). FG inventory +281.7% vs revenue +99.4% under a delivery-triggered revenue policy (B02 rank 3), turnover 4.19x -> 3.32x. Tripled paper profit that produces no cash, alongside a ballooning finished-goods build, is the textbook sell-in / channel-loading signature. | **Strong** |
| "Backward integration is a durable cost moat" (B04, B07 B1) | Plant net block was Rs 0.69 lakh at FY25; capacity was built almost entirely in FY26 and is unproven at scale (B04). Peers confirm SMT/backward integration is an INDUSTRY-WIDE capex race (CP Plus, Sahasra, OSEL), not a Prizor edge (B06 verified, anchor_count 5-6). Installed capacity runs at ~5.5% utilisation vs SOM (B10 FLAG-FORWARD-ROCE-DILUTION). | **Strong** |
| "Regulatory STQC/BIS-ER tailwind" (B05 trigger 1, B07 R1) | Category-wide, not company-exclusive; CP Plus claims the same share gains (B06). When analysts asked CP Plus to name STQC-certified challengers gaining traction, they named Prama and Matrix; Prizor was NOT named (B06 peer_mentions_of_company: []). | **Strong** |
| "Clean promoter, no selling, 68.28% holding" (B08) | Absence of found adverse is not proof of clean. Pledge % is NOT FOUND, not confirmed zero (B08 pledge_pct_latest NOT FOUND). A Rs 3.00 Cr loan-to-equity conversion (4,00,000 shares at Rs 75, 07-May-2024) traces to no named lender across three cross-checks (B02 rank 2). Om Security related-party revenue was 9.95% of FY24 then zero in the IPO year, unexplained (B02 rank 4). Undisclosed post-balance-sheet promoter remuneration ~150% hike (B10 FLAG-DISCLOSURE-QUALITY). | **Strong** |
| "MASSIVE TAM, 24.2x headroom" (B09) | The realisable SOM path implies only 15.9-17.0% revenue CAGR (B10), one-sixth of the 108% print. A large TAM with 5.5% utilised capacity funded by short-term debt (Rs 2.76 Cr -> Rs 31.82 Cr, ~11.5x, B10) is a ROCE-dilution risk, not a growth guarantee. | **Moderate-Strong** |

**Verdict on the company narrative:** the three load-bearing bull claims (tripled FY26 profit, peer-beating margins, cost moat) are each individually fragile, and they are correlated. If margins revert to peer, the tripled profit shrinks and the ROCE collapses. The single most fragile claim is the peer-contradicted margin, because everything downstream (PAT, ROCE, the re-rating case) depends on it.

---

## 2. THREE WAYS MONEY IS LOST (and one way the AVOID is wrong)

There is no position (B14 verdict AVOID / DEEP WATCH). Loss here is (a) capital loss if a buyer overrode the AVOID, and (b) opportunity loss if the AVOID is a false negative. Both are shown, per the two-sided mandate.

### 2A. Three ways a buyer at CMP Rs 825 loses 30%+ (validating the AVOID)

| Scenario | What Triggers It | Timeline | Probability | How Much Lost |
| --- | --- | --- | --- | --- |
| Multiple compression to reality | FY26 audits and the market re-rates a ~29x-actual, cash-negative assembler toward the 15-25x destination band | 6-18 months (next audited AR) | High | -40% to -80% from Rs 825 (base fair value Rs 154, max-bull fair value ~Rs 713) |
| Margin reversion shock | Audited FY26 EBITDA prints near CP Plus 13.7% instead of claimed 21-23%; PAT far below the tripled claim; ROCE de-rates | 6-12 months | Medium-High | -50%+ (kills both the earnings base and the ROCE multiple simultaneously) |
| Governance / cash event | Rs 3.00 Cr counterparty still unnamed, or a third straight audited year of CFO <= 0 with PAT > Rs 20 Cr confirms structural cash leak (fttcp falsification print) | 6-18 months | Medium | -30% to -60% (de-rating plus discount for disclosure risk) |

### 2B. The one way the AVOID is wrong (opportunity loss / false negative)

| Scenario | What Triggers It | Timeline | Probability | Cost of the AVOID |
| --- | --- | --- | --- | --- |
| Clean FY26 audit rescues the case | Audited FY26 confirms revenue ~Rs 148 Cr, PAT ~Rs 30 Cr (EPS ~Rs 28.5), margins sustained, AND CFO turns positive (>=40% of PAT). Cash reclassifies to growth-induced (0.65x -> 1.00x), destination re-rates toward the 25x cap. | Next audited AR, ~12 months | Low-Medium | Even here the max-bull Year-3 target is ~Rs 1,055 (25x cap x EPS 42.2), a 3yr CAGR of ~8.6% from CMP, still below 25%. The AVOID is not "wrong" at CMP; it would move to a live WATCH, not a BUY. Opportunity cost of skipping is modest, not large. |

The asymmetry is decisive: the buyer's downside is -40% to -80% at high-to-medium probability; the AVOID's false-negative cost is a foregone ~9% CAGR at low-medium probability. Skipping is correct.

---

## 3. VALUE TRAP TEST — and its inverse (falling knife vs missed rocket)

**Is this a value trap?** No, because it is not cheap. A value trap is a low multiple hiding deterioration. Prizor is the opposite: a HIGH multiple (87x FY25, ~29x unaudited FY26) on top of unproven, cash-negative, peer-contradicted quality. The trap here is a growth trap, a story stock where reported ROCE 31.29% (B10) is accounting return, not cash return (cumulative CFO/PAT -1.02x, B02). Gate 0 Block B scored 0/20 (B14 §3A). The "melting ice cube" test does not apply; the correct label is "unproven scaling story priced for certainty it has not earned."

**The inverse test (is the AVOID missing a compounder?).** The decisive check: reconstruct valuation under the MAXIMALLY GENEROUS bull and see if any path clears 25% CAGR. If none does, the AVOID is robust regardless of the FY26 audit.

| Assumption | Pipeline (governing) | Maximally generous bull |
| --- | --- | --- |
| Year-0 EPS | Rs 9.495 (FY25 audited, B10) | Rs 28.5 (unaudited FY26 tripled, if audited) |
| ROCE for Pillar 1 | 31.29% STAGNANT (fttcp) | 37% (FY26 chart figure) -> base PE 25.2x |
| Cash multiplier | 0.65x (INDETERMINATE default) | 1.00x (growth-induced, +0.20 offset) |
| Destination PE | 15.0x (Track 2) | 25.2x raw, capped at sector 25x |
| Fair value TODAY | Rs 154 | ~Rs 713 (25x x 28.5) |
| Year-3 EPS (14% CAGR) | Rs 14.1 -> Rs 154 target | Rs 42.2 -> Rs 1,055 target |
| 3yr CAGR from CMP Rs 825 | -43% to -45% | +8.6% |
| Hurdle Ratio | 0.23 STOP | 1.28 STOP (needs >=31% EPS CAGR to pass; SOM ceiling is 16%) |

**Result:** even the maximally generous reconstruction (every swing assumption flipped bull, destination hitting the sector cap) lands a Year-3 target of ~Rs 1,055 = 8.6% CAGR, and the Hurdle Ratio remains STOP at 1.28 (pass needs 1.953). To clear 25% CAGR a buyer needs >=31% sustained EPS CAGR against a market growing 16.46% (B09) with capacity already 94.5% idle. That is infeasible. **The AVOID is not a missed rocket. Valuation safety survives the strongest bull reconstruction possible under the framework.**

---

## 4. VARIANT PERCEPTION CHECK

The pipeline's variant perception: the market pays Rs 825 (87x) for a business worth 15x, so the market is wrong by ~5x. **Argue the market is right:**

The market is not valuing FY25 audited EPS; it is discounting an FY26 that (unaudited) tripled profit on a real regulatory tailwind, in a MASSIVE TAM (B09), from a promoter holding 68.28% who has not sold a share (B08). SME micro-caps mid-transition from trading to manufacturing routinely trade at optically high trailing multiples that collapse as the manufacturing ramp lands; on forward FY26 the stock is ~29x, unremarkable for a doubling-revenue franchise with a policy moat. The market may simply be pricing the ramp the pipeline refuses to credit because it is unaudited.

**Now rebut (why the market is likely wrong here):** the market is extrapolating an unaudited print that the company cannot internally reconcile (ROCE 47.4% vs 37.2% in one deck, B05), whose margins exceed the only scaled peer by ~800 bps with no disclosed cause (B06), and whose tripled profit produced no cash (fttcp 5). The market is paying a certainty premium for numbers that carry three unresolved red flags and one unnamed Rs 3 Cr equity counterparty. Even granting the ramp in full (Section 3), the return does not clear the hurdle. The market is right that growth is real and wrong that it is worth Rs 825; both can be true. The variant perception survives, but its honest form is "the market has over-extrapolated an unaudited, cash-poor ramp," not "the market missed that the business is failing."

---

## 5. CATALYST DEPENDENCY

**SHARED CATALYST:** none flagged (fttcp AUTHORITATIVE CONCLUSIONS: "SHARED CATALYST flag: none"; B11 shared_catalyst_flag: false). Confirmed: Pillar 3 growth premium is +0x (EM 13.6 < 25, B11), so no forward capex catalyst is doing double duty in Pillar 1 and Pillar 3. There is no single point of failure of the shared-catalyst type to stress. This is itself informative: the valuation credits NO forward catalyst, so the AVOID does not depend on any catalyst failing. It depends only on the price being too high today, which is catalyst-independent.

**The one catalyst that matters (to the bull, not the bear):** the FY26 audited cash-flow statement (fttcp single falsification print). Both bull rescues in Section 1A require it to turn positive (>=40% of PAT). If that audit is delayed, or prints CFO <= 0 for a third straight year with PAT > Rs 20 Cr, the AVOID hardens to structural (B14 §7). While a buyer waits, the stock earns no support from fundamentals: the destination is 15-25x, the price is ~29x forward at best, so time works against the holder, not for them. The catalyst dependency runs entirely against the bull.

---

## 6. INFORMATION ASYMMETRY CHECK

Low FII+DII is NOT counted here (framework rule; SME mandate exclusion, not informed avoidance; B11 UA third qualifier NOT FOUND anyway).

The relevant asymmetry runs against an outside buyer on three counts, all insider-favouring:
1. **The Rs 3.00 Cr loan-to-equity conversion counterparty is known to the promoters and unknown to the market** (B02 rank 2, unreconciled across three cross-checks). Someone received 4,00,000 shares at Rs 75 in May 2024; the market cannot identify them. That is a concrete information gap held by insiders.
2. **Pledge status is NOT FOUND** (B08). The market cannot confirm whether promoter shares are encumbered; the promoters can.
3. **Segment, customer-concentration, and IPO-utilisation disclosures are absent or generic** (B02 rank 8, rank 15; B05 red_flags), and FY26 actuals exist only in an unaudited deck the company controls. Every material forward number is insider-timed.

No promoter selling is observed (float is 100% IPO + bonus, B03), which is mildly reassuring, but the promoter has no incentive to sell at Rs 825 with 68.28% locked. The asymmetry is real and adverse. It does not by itself force AVOID, but it caps trust at CAUTION (B08) and forbids paying a certainty premium.

---

## 7. PRE-MORTEM

It is July 2028. Two scenarios, because the thesis under test is an AVOID.

**Pre-mortem for a hypothetical buyer at Rs 825 (down 40%+, the likely path).** FY26 audited results, published late, confirmed what the peer cross-read predicted: EBITDA margin printed near 15-16%, not the 21-23% claimed, and PAT came in well below the tripled deck figure once the auditor normalised the FY26 inventory build. Operating cash flow stayed negative for a third year as finished-goods inventory (already +281.7% in FY25) was written down, and the market realised the "growth" had been sell-in to an 11,000-dealer channel rather than sell-through. Short-term borrowings, having gone from Rs 2.76 Cr to Rs 31.82 Cr to fund the idle capacity, forced either an equity raise at a depressed price or a further debt increase. The 87x trailing multiple compressed toward the mid-teens as the ROCE de-rated on 5.5% utilisation. The stock lost more than half its value, and the Rs 3.00 Cr counterparty question was never answered. The pipeline's AVOID was vindicated in direction and, once FY26 audited, roughly in magnitude.

**Pre-mortem for the AVOID as a false negative (the less likely path).** FY26 audited clean: revenue Rs 148 Cr, PAT Rs 30 Cr, margins sustained on genuine backward-integration savings, and, critically, CFO turned positive as the inventory build normalised, proving the drag had been growth-induced. The market re-rated toward the 25x cap, the stock reached ~Rs 1,000 by 2028, and the AVOID cost a foregone ~9% CAGR. Even in this best case the buyer did not earn 25%, so the AVOID was still defensible; the cost of caution was modest. This is the scenario a future refresh must watch for via the FY26 audited cash flow, but it does not retroactively make Rs 825 a buy.

The base-rate weighting (Grade C, B10; peer cohort Sahasra treating negative CFO as structural to FY2028, B06) puts the first pre-mortem well ahead of the second.

---

## 8. EARLY WARNING SIGNALS (next audited reporting cycle)

| Signal | What It Means | Threshold | Action |
| --- | --- | --- | --- |
| Audited FY26 operating CFO vs PAT | The single falsification print (fttcp) | Red: CFO <= 0 with PAT > Rs 20 Cr (third straight year, confirms structural, hardens AVOID). Green: CFO >= 40% of PAT (reopens to WATCH, not BUY) | If red, close the file structurally. If green, re-run Section 3 with growth-induced cash. |
| Audited FY26 EBITDA margin | Tests the peer-contradicted claim | Red: reverts toward CP Plus 13.7%. Green: sustains >= 18% AND reconciles to a disclosed cost advantage | If red, the tripled-PAT base is invalid; magnitude of downside widens. |
| Finished-goods inventory growth vs revenue growth | Sell-in vs sell-through / write-down risk | Red: FG growth > revenue growth again (was +281.7% vs +99.4%) | If red, treat reported growth as channel-loaded. |
| Rs 3.00 Cr conversion counterparty disclosure | Governance opacity | Red: still unnamed in RPT note / Q&A. Green: named and reconciled | Until named, Promoter CAUTION cap binds (B08). |
| Internal ROCE consistency in next deck/AR | Disclosure quality | Red: any repeat of the 47.4% vs 37.2% type inconsistency | If red, discount all company-sourced forward numbers. |
| Short-term borrowings / trailing EBITDA | Debt-funded idle capacity | Red: above 2x (was ~11.5x increase in absolute borrowings). Green: below 1.5x | If red, dilution or refinancing risk rising. |
| Price entering Rs 63-79 | Anti-value-trap conjunction (B14 §7) | Only actionable if NO thesis-broken trigger has fired; if the price falls BECAUSE a trigger fired, the zone is withdrawn | Do not buy a falling knife. |

Item 1 is the fulcrum. The entire two-sided call collapses to one line in the next audited cash-flow statement.

---

## 9. FINAL DEVIL'S VERDICT

Rated for whether the AVOID thesis survives the strongest two-sided attack. SURVIVES = the AVOID stance holds on this axis.

| Dimension | Deciding single fact | Verdict |
| --- | --- | --- |
| Growth triggers | Even the maximally generous bull (unaudited FY26 tripling, margins held) needs >=31% EPS CAGR for 3 years against a 16.46% market with 94.5% idle capacity to clear the hurdle; SOM-implied CAGR is 15.9-17.0% (B09, B10). Growth is real but structurally cannot rescue the price. | **SURVIVES** (AVOID holds; growth is the AVOID's most attackable axis on magnitude, not direction) |
| Moat durability | When analysts asked CP Plus to name STQC-certified challengers gaining traction, they named Prama and Matrix; Prizor was not named, and every moat leg (regulatory, backward integration, dealers) is industry-wide or self-reported (B06, B07, EM 13.6 MODEST). | **SURVIVES** (AVOID's no-durable-moat read holds; the bull moat is destroyed) |
| Management trust | A Rs 3.00 Cr equity block traces to no named lender across three cross-checks; pledge NOT FOUND; internal ROCE inconsistency in the company's own deck; undisclosed remuneration hike (B02, B05, B08, B10). | **SURVIVES** (CAUTION holds; cannot be lifted to TRUSTWORTHY) |
| Valuation safety | Every point of the reconstructed fair-value range, from Rs 154 (FY25 base) to ~Rs 713 (max-bull FY26 base at the 25x sector cap), sits below CMP Rs 825; Hurdle Ratio remains STOP (0.23 to 1.28) across the entire range. | **SURVIVES** (robustly; but the pipeline's -45.4% CAGR magnitude is overstated versus an honest -9% to -50% range) |
| **Overall thesis (AVOID)** | The AVOID direction survives even the maximally generous bull reconstruction the framework permits; no path clears 25% CAGR from CMP. | **SURVIVES** |

**Devil's closing judgment.** The AVOID is robust in direction and should stand. My genuine, brutal criticism of the pipeline is not that it reached the wrong verdict but that it reached it with an overstated magnitude: pinning "72-91% below CMP" and "-45.4% expected CAGR" to stale FY25 audited EPS, for a company whose unaudited FY26 tripled, produces a scarier number than the framework can actually defend. A hostile reader would attack that number and, on magnitude, win. The honest AVOID is "~15% to ~50% overvalued depending entirely on the FY26 audited cash flow, which resolves both the earnings-reality question and the cash-conversion question at once." My brutal criticism of the COMPANY is that its three load-bearing claims (tripled FY26 profit, ~800 bps peer-beating margins, a cost moat) are correlated and each unproven, its own deck cannot reconcile its headline ROCE, and its tripled profit produced no cash. The company narrative is the more destroyed of the two. Position implication: no position; DEEP WATCH; the file reopens only on the FY26 audited cash-flow print, and even a clean print moves this to WATCH, never to BUY at Rs 825.

---

```yaml
stage: B15-devil
company: "PRIZOR"
run_date: "2026-07-12"
model: claude-opus-4-8
status: complete
dimensions:
  growth_triggers: "survives"
  moat_durability: "survives"
  management_trust: "survives"
  valuation_safety: "survives"
overall: "SURVIVES"
top_counters:
  - "AGAINST THE AVOID (magnitude): the 87x / -45.4% CAGR / '90% overvalued' headline is anchored to stale FY25 audited EPS Rs 9.495; on unaudited FY26 (PAT tripled, EPS ~Rs 28.5) the trailing multiple is ~29x and base fair value ~Rs 460, so the honest overvaluation is ~15-50%, not ~90% (B05, B11)."
  - "AGAINST THE AVOID (cash): the 0.65x cash multiplier was a conservative INDETERMINATE default because the rating WC quote is NOT FOUND; if FY26 audited CFO turns positive (growth-induced), 0.65x->1.00x roughly doubles the destination toward the 25x cap (Section 1B Pillar 2, fttcp ruling 5)."
  - "DECISIVE FOR THE AVOID: even the maximally generous bull (FY26 tripling, margins held, ROCE 37%, cash 1.00x, destination at the 25x sector cap) gives a Year-3 target of ~Rs 1,055 = 8.6% CAGR and Hurdle Ratio 1.28 STOP; clearing 25% needs >=31% EPS CAGR against a 16% market with 94.5% idle capacity, which is infeasible."
  - "AGAINST THE COMPANY: tripled FY26 PAT produced no operating cash (fttcp 5) while FG inventory ran +281.7% vs revenue +99.4% under delivery-triggered revenue recognition; the sell-in / channel-loading signature undermines the profit's reality (B02)."
  - "AGAINST THE COMPANY: claimed 21-23% EBITDA exceeds the only scaled peer (CP Plus 13.7% FY26, 14-15% 'new normal') by ~800 bps with no disclosed cost advantage, and the company's own Apr-2026 deck reports FY26 ROCE as both 47.4% and 37.2% (B06, B05)."
  - "Both the bull rescue and the bear confirmation resolve on the SAME single event, the FY26 audited cash-flow statement (fttcp falsification print); the AVOID is robust today and reopens to WATCH, never BUY at Rs 825, only on that print."
```
