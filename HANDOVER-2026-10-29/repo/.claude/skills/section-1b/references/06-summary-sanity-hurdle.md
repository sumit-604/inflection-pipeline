# Chunk 06. Eight-row summary, sanity checks, Hurdle Ratio, standing check, entry and conclusion

Loaded by: Role 1 Section 1B Four-Pillar Summary and Hurdle Ratio; Section 2D; Section 4E to 4H. Pipeline: stage 11; stage 13 synthesis (Hurdle and verdict card); /finalize; Verifier C (12c).
Sources in force: Master v3.7 §1B summary, RRM dual track, Hurdle Ratio, §2D, §4E-4H, §4H-pre; Section 1B v3.3 Amendments 2, 3, 6, 4.3; v3.8 Amendment 18.5; v3.9 Amendments 20.5, 20.8, 24, 25; v3.10 Amendment 26 standing check.

## Four-Pillar Summary Calculation (rows A to H)

| Step | Calculation | Value |
|---|---|---|
| A. ROCE Base | ROCE ___% → formula (chunk 01) | ___x |
| B. Cash Multiplier (effective) | Base ___x + offset ___ (chunk 02) | ___x |
| C. Quality-Adjusted Base | A × B | ___x |
| D. Growth Visibility Premium | 3a + 3b + 3c, cap +6x (chunk 03) | +___x |
| E. Strategic Premium | chunk 04 | +___x |
| F. Raw Destination PE | C + D + E | ___x |
| F2. UA-Adjusted Raw PE | F × 1.25 if all three qualifiers hold; else F | ___x |
| G. Sector Cap (quality-uplifted if applicable) | chunk 05 | ___x |
| G2. Category-Break Override applied? | Y/N, conditions 1-4 status if Y | ___ |
| G3. Override-Adjusted Cap | min(G × 1.40, 45x) if G2 = Y; else G | ___x |
| **H. Final Destination PE** | **min(F2, G3)** | **___x** |

**Destination PE range = H ±7.5%, rounded to the nearest 0.5x.** The upper bound stays subject to the sector cap. Examples: 12x → 11-13x; 20x → 18.5-21.5x; 37x → 34-39.5x.

Where FTTCP Module B8 reads HIGH, the relative-PE convergence target supports H toward the upper end of the range; where B8 reads NONE, the relative expression checks that H assumes no unsupported re-rating (chunk 15).

## Dual track

Every Role 1 produces both tracks, carried through all fair values, entry prices and the verdict card.

- Track 1 (RRM): Destination PE = Fundamental Base PE × RRM, capped at the (quality-uplifted) sector cap. Formula and r table in chunk 15.
- Track 2 (Additive): the summary above, without RRM.
- Where they diverge by more than 15%, state which track fits this company and why; the more conservative track sets the entry zone. See open ruling OR-1 in SKILL.md.
- When Step 1C hands governance to the relative multiple (Amendment 20.5), that multiple, capped, becomes the governing destination and every downstream item recomputes on it (Amendment 20.8, chunk 15).

## Hurdle Ratio

**HR = (1 + EPS CAGR)³ × (Destination PE mid ÷ Current PE).**

- EPS CAGR = the probability-weighted EPS CAGR on the Amendment 21 run-rate base, built from the FTTCP C.2 credit net of the mandatory downside term (Amendment 24; chunks 08, 09).
- The destination-PE-times-EPS term is basis-consistent with the entry (Amendment 18.1).
- Amendment 24 governs: the Hurdle Ratio is a feasibility check, not a verdict cap (operator ruling 2026-09-15, OR-2). Compute the band and show it on the verdict card; it caps no verdict.

| Condition | Feasibility band |
|---|---|
| HR(Base) ≥ threshold | PASS: the tier hurdle is feasible on base-case earnings |
| HR(Base) < threshold but HR(Bull) ≥ threshold | CONDITIONAL: feasible only on bull-case earnings; flag "growth-dependent with de-rating headwind" |
| HR(Bull) < threshold | STOP band: the tier hurdle is infeasible even on bull-case earnings |

- Bull EPS CAGR may be used only if the Role 5 trailing-four-quarter credibility grade is A or B. If C or D, the Bull row uses Base EPS CAGR + 5 percentage points maximum (chunk 17).
- Final validation question: "Would you personally pay this destination PE for this quality of business?"

### Two-tier hurdle (Amendment 4.3)

- Tier A, Transition / Undiscovered: hurdle 25% CAGR, threshold 1.953 (1.25³). Default tier. Applies when FII+DII combined <3%, OR the combined Gate 0 + EM assessment is TURNAROUND or HIGH POTENTIAL.
- Tier B, Discovered Quality: hurdle 20% CAGR, threshold 1.728 (1.20³). Applies only when ALL hold: FII+DII ≥3%; Gate 0 GOOD or better OR EM ≥25; promoter verdict TRUSTWORTHY or better; no structural FLAG-CASH. A company failing Tier B's quality gates stays at 25%.
- Tier B positions default to a Medium (4-6%) ceiling unless the operator documents an override in the thesis.
- The verdict card's first line reads: "Tier: [A/B] | Hurdle: [25%/20%]".

## Section 2D projection sanity checks

| Check | Result | Pass? |
|---|---|---|
| Revenue growth faster than capacity allows? | | |
| Margins require something unprecedented? | | |
| ROCE stays above 15%? | | |
| FCF sufficient to fund growth without excessive new debt? | | |
| EPS growth driven by operations, not financial engineering? | | |
| Implied market share gain realistic? | | |
| Does CFO/PAT trajectory improve or stay consistent with the Pillar 2 assumption? | | |
| Is the Year 3 ROCE consistent with the FTTCP ROCE forward verdict used in Pillar 1? | | |
| **Did the base case credit the transition, or price the audited past?** | | |

**Standing check (Amendment 26).** "Did the base case credit the transition, or price the audited past? If base revenue equals historical CAGR at trailing-average margins for a name with run-rate, order-book, or capacity evidence, the projection is wrong. Rebuild."

## Entry price (Section 4E)

- Entry = exit-consistent fair value ÷ (1 + tier hurdle)^N, with 1.25 for Tier A and 1.20 for Tier B (Amendment 18.5 read with Amendment 4.3; operator ruling 2026-09-15, OR-8).

| Calculation | Value |
|---|---|
| Base Case Fair Value (Year 3) | ₹___ |
| Price for the tier hurdle = Fair Value ÷ (1 + hurdle)³ | ₹___ |
| Price for 30% CAGR = Fair Value ÷ (1.30)³ | ₹___ |
| Margin of Safety Price = hurdle entry × (1 − MoS), MoS per the evidence-scaled schedule | ₹___ |
| Ideal entry range | ₹___ to ₹___ |

Buy at the bottom of the revealed premium band, never the top. No entry zone is presented without the Amendment 19 FV CAGR and return-source label (chunk 12). Fast-growth names express margin of safety as position size instead (Amendment 25, chunk 08).

## Risk-reward and exit validation

- Section 4F: Upside (base) ÷ Downside (bear) ratio should be ≥ 2x.
- Section 4G checks: Year 3 ROCE justifies the ROCE base and matches the FTTCP verdict; Year 3 CFO/PAT justifies the cash multiplier or asset-quality band; the primary catalyst has fired by Year 3 in the base case; the strategic premium is still justified at Year 3 with single credit respected; UA ordering is min(F × 1.25, Cap); you would buy a different stock at this exit PE with similar Year 3 metrics. If any check fails, revise the exit PE and recalculate.

## Mandatory conclusion elements (Section 4H-pre)

1. **Value vs price (two lines).** Line one: what the business is worth and its single most important driver. Line two: what the price already assumes (Market-Implied flag OPPORTUNITY / FAIRLY PRICED / PRICED-WE-ARE-LATE, chunk 14), what closes the gap, and when.
2. **Evidence-scaled margin of safety** (price-based names):

| Evidence and catalyst | Margin of safety |
|---|---|
| Mostly 📄 documented evidence AND catalyst inside 12 months | 20% |
| Mixed evidence | 30% |
| Mostly 🎙️/🔍 evidence OR catalyst beyond 18 months | 40% |

3. **Dispersion-capped sizing.** Fair value range width = (Bull − Bear) ÷ Base. Under 40% → normal sizing; 40% to 80% → capped at Medium; above 80% → capped at Small regardless of conviction. It binds on top of the Role 2 position-size and Promoter caps, and on the Conviction Outlier tier; the tightest cap wins.
4. **Edge declaration.** "Edge claimed: [process / patience / information], because ___." Default PROCESS. INFORMATION only with the specific public-but-unread fact named.

## Verdict card additions carried by later layers

Tier line (A4.3); Hurdle band; both tracks; destination range ±7.5%; FV CAGR and return-source label (A19); price decomposition percentages and residual % (A24); Step 1C line: pillar destination, adjusted peer base or PENDING LIVE PEER TABLE, % gap, governing multiple (A20); value vs price, MoS row, dispersion cap, edge (4H-pre).
