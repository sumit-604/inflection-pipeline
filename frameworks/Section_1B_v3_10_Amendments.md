# SECTION 1B v3.10 AMENDMENTS — GROWTH SYMMETRY IN PROJECTIONS AND WEIGHTING

*Version 3.10 | issued 08 September 2026. Operator ruling 08-Sep-2026, Keerti Kaushik. Carries one amendment, Amendment 26. Layers on top of Section 1B v3.3 + v3.3 Amendments + v3.5.1 + v3.6 + v3.7 + v3.8 + v3.9 (Amendments 20-25). This file does not modify any prior file in place. Where they overlap on items named here, v3.10 governs, then v3.9, then v3.8, then v3.7, then v3.6, then v3.5.1, then v3.3. Stage 11 reads this alongside the earlier Section 1B files. Amendment numbering continues from v3.9, whose last amendment is 25.*

*Origin: cross-run review of the September 2026 AR batch. Finding: the projection rules in Section 2 of the Master Prompt anchor the base case to audited history, so a transition setup, the operation's own strategy, cannot earn a base case that credits the transition. Amendments 21 to 25 moved the exit multiple and the verdict toward the probability-weighted future. Amendment 26 moves the projections that feed them the same way. Without it, A21 to A25 reprice a base case that was never allowed to grow.*

---

## AMENDMENT 26 — GROWTH SYMMETRY IN PROJECTIONS AND WEIGHTING

`[v3.10: replaces the Master Prompt Section 2A base-case revenue rule, the Section 2B base-case margin rule, the "Conservative bias" Operating Rule, and the whole-history keying of the 4D probability weights; adds a standing check to 2D and a worksheet line to Section 2 — operator ruling 08-Sep-2026, arising from the September 2026 AR batch review]`

**The distortion.** Four rules compound in one direction:

1. Base revenue = lower of (discounted guidance) or (historical CAGR). Historical CAGR becomes a ceiling.
2. Base margin = trailing 3-year average. Destination mix and operating leverage cannot appear.
3. "Conservative bias, when in doubt use the conservative assumption." Applied per input, five inputs shaded 10% each produce a bear case labelled base.
4. Probability weights keyed to whole-history track record. A transition name has a thin record for the reason it is interesting, and is penalised for it.

The result is a base case that prices the audited past. The Hurdle Ratio then fails, the verdict lands WATCHLIST, and the operation screens out its own setups. This is the same failure class Amendment 9 addressed in Pillar 1 (trough-anchored ROCE), now corrected in Section 2.

**The principle.** Conservatism lives in position size (Amendment 25), not in the projection. The projection states the most evidenced path. Doubt is expressed as a starter size and a confirm-by date (Amendment 23), never by lowering the number.

### 26.1 BASE-CASE REVENUE BASIS (replaces the 2A base-case rule)

Base-case revenue uses whichever of the following rests on harder evidence, and the worksheet declares the basis:

| Basis | Definition | Evidence tier required |
|---|---|---|
| RUN-RATE | Exit-quarter revenue annualised, adjusted for stated seasonality | filed quarterly results |
| ORDER-BOOK | Executable order book at disclosed execution cycle, plus disclosed pipeline at historical conversion | filing, or concall with Role 5 grade A/B |
| CAPACITY | Commissioned or dated capacity at guided utilisation ramp and realisation | capex commissioning filing plus utilisation guidance on the concall |
| GUIDANCE-DISCOUNTED | Management guidance discounted by the trailing-4-quarter Role 5 credibility ratio | concall with Role 5 history |
| HISTORICAL | Historical CAGR | fallback only when none of the above exists |

Historical CAGR is always computed as a cross-check and shown beside the chosen basis. It governs only when no forward evidence exists. If the chosen basis diverges from historical CAGR by more than 10 percentage points, the worksheet names the observation that will confirm or refute the divergence and its confirm-by date (feeds the Amendment 23 Expectation Ledger).

### 26.2 BASE-CASE MARGIN BRIDGE (replaces the 2B base-case rule)

Base margin = margin implied by destination mix and operating leverage, shown as a bridge:

| Lever | bps contribution | Evidence | Confirm-by |
|---|---|---|---|
| Current margin | ___% | latest FY filing | n/a |
| Mix shift (name the product/segment) | +/- ___ bps | ... | ... |
| Operating leverage on fixed cost base | +/- ___ bps | ... | ... |
| Input cost / pricing pass-through | +/- ___ bps | ... | ... |
| Base-case margin Year 3 | ___% | | |

Rules:
- Trailing 3-year average margin is the BEAR case, not the base.
- Bull = guided margin at face value where Role 5 grade is A or B.
- A lever with no evidence line is not a lever. Drop it.
- If the bridge lifts margin more than 400 bps in three years, the Second-Order Section (Master Prompt Amendment, Rule F) must show the customer-side or cost-side mechanism that pays for it. **OPEN ITEM (08-Sep-2026):** the Second-Order Section / Rule F is not in the repo copy of the Master Prompt, and no session may reconstruct it. Until the operator lands it, the mechanism is named inline in 2B with its evidence line, flagged "Second-Order Section absent, mechanism stated inline".

The v3.5 cyclical override is unchanged and still supersedes this bridge for any sector flagged cyclical: base = full-cycle average margin, bear = cycle trough, bull = cycle peak.

### 26.3 NO PER-INPUT CONSERVATISM (replaces the Operating Rule "Conservative bias")

The Operating Rule reads instead: "State the most evidenced path. Where evidence is thin, present both readings and the single observation that separates them. Size the position for the doubt (Amendment 25). Do not shade individual inputs."

Bear and bull cases remain as defined. The change is that the base case is no longer built by stacking conservative choices.

This replaces the per-input conservatism rule in Role 1 projections only. It does not touch the interpretation rules in the document-reading protocols (Annual Report Analysis Protocol, Quarterly Results Review Protocol, quarterly forensic agents) or the TAM estimate-selection rule, which choose between competing readings of filed evidence rather than shade a projection input.

### 26.4 RELEVANT-PERIOD TRACK RECORD (clarifies 4D and the Rule B discount)

Probability weights in 4D and the guidance discount in 26.1 are keyed to the trailing four quarters of delivery (the Role 5 credibility ratio), not whole-company history. Mixed history plus four quarters of delivery = Good weighting. Where Role 5 history is shorter than four quarters, use what exists and state the period. The existing re-weighting rule (two quarters below bear on 2+ metrics shifts one notch toward Poor) is unchanged and cuts the other way.

### 26.5 EXIT-MULTIPLE CEILING LANGUAGE

Any surviving text in project instructions, prompts, or CLAUDE.md that says "never assume exit P/E above 20x" is void. Section 1B governs the destination PE through the four pillars, sector cap, UA uplift, and Category-Break Override. On adoption, Claude Code greps the repo for "above 20x" and "exit P/E of 15x, 20x" and removes any instance that operates as a ceiling. Text that forbids a round-number DEFAULT (an exit PE asserted without running the pillar calculation) is not a ceiling and is retained.

---

## INTERACTION WITH THE REST OF THE FRAMEWORK

- **Amendment 21 (forward run-rate earnings base).** A21 supplies the earnings base for the exit multiple. 26.1 supplies the revenue path to Year 3. They use the same run-rate definition.
- **Amendment 22 (probabilistic catalyst credit).** A22 prices catalysts into the exit multiple. 26.1 CAPACITY and ORDER-BOOK bases price them into revenue. The single-credit rule (Amendment 4) applies: a catalyst credited in revenue at its probability is not credited again in Pillar 3 at full weight. State the split in the worksheet.
- **Amendment 23 (Expectation Ledger).** Receives every confirm-by date generated by 26.1 and 26.2.
- **Amendment 24 (three-tier price decomposition).** Unchanged. The confirmed tier still rests on filed run-rate; the high-probability tier now has a base case that can carry it.
- **Amendment 25 (margin of safety as position size).** The sole home of conservatism after this amendment.
- **Amendment 20 (relative valuation cross-check, step 1C).** Untouched. Step 1C still runs on the A21 forward base; 26.1 and 26.2 change the projection that feeds the Hurdle Ratio, not the peer placement.
- **Amendment 9 (Pillar 1 normalisation) and Amendment 4 (single credit).** Unchanged.
- **Amendment 14 (growth fade horizon) and the v3.5 Year-5 projection rule.** Unchanged. The fade horizon still steps the chosen base-case growth down year by year; 26.1 sets the level the fade starts from, not the fade.
- **Sector cap.** Unchanged and still absolute. Amendment 26 touches the projection, never the destination PE ceiling.

## STANDING CHECK (added to 2D Projection Sanity Checks)

"Did the base case credit the transition, or price the audited past? If base revenue equals historical CAGR at trailing-average margins for a name with run-rate, order-book, or capacity evidence, the projection is wrong. Rebuild."

## WORKSHEET LINE (added to the Section 2 worksheet)

"Base-case basis: [RUN-RATE / ORDER-BOOK / CAPACITY / GUIDANCE-DISCOUNTED / HISTORICAL]. Evidence: [filing, section, date]. Historical CAGR cross-check: ___% (divergence ___ pp, confirm-by observation: ___, date: ___). Margin bridge: current ___% -> Year 3 ___% via [lever: bps, evidence] x N. Track-record period for weighting: trailing ___ quarters, Role 5 grade ___. Catalyst credit split: revenue ___% / Pillar 3 ___%."

## VERSION HISTORY

| Version | Date | Changes |
|---|---|---|
| 3.8 | 23-Aug-2026 | (prior) Amendments 18-19, exit-basis symmetry, option resolution, and FV-CAGR classification. See `Section_1B_v3_8_Amendments.md`. |
| 3.9 | 26-Aug-2026 | (prior) Amendment 20, relative valuation cross-check (new step 1C). See `Section_1B_v3_9_Amendments.md`. |
| 3.9 (reissue) | 07-Sep-2026 | (prior) Amendments 21-25, forward-expectation exit framework. See `Section_1B_v3_9_Amendments.md`. |
| 3.10 | 08-Sep-2026 | Amendment 26 (Growth Symmetry). Base-case revenue basis hierarchy replaces "lower of guidance or historical CAGR"; historical CAGR demoted to cross-check and fallback. Base-case margin defined as destination-mix bridge; trailing average reassigned to bear. Per-input "conservative bias" operating rule replaced with most-evidenced-path plus A25 sizing. Probability weights and guidance discount keyed to trailing four quarters. "Never above 20x" language voided wherever it survives. Standing check added to 2D. Single-credit split between 26.1 catalyst revenue and A22 Pillar 3 credit stated in worksheet. |
