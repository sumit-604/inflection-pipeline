# Chunk 01. Pillar 1: ROCE base multiple and trajectory smoothing

Loaded by: Role 1 Section 1B Pillar 1, row A of the summary. Pipeline: stage 11; Verifier C (12c); /fttcp pillar-approval gate.
Sources in force: Master v3.7 §1B Pillar 1; Section 1B v3.3 Amendments 4, 5, 7; v3.5.1 consolidated Amendment 9; v3.6 Amendment 11; v3.7 Amendment 17.1; FTTCP v2.3 Pillar 1 Integration.

## The formula

- ROCE ≤ 33%: **Base PE = 0.5 × ROCE(%) + 7.5, floored at 9x.**
- ROCE > 33%: **Base PE = 24 + 0.3 × (ROCE(%) − 33), capped at 30x.**

Reference points: 12% → 13.5x | 17% → 16x | 22% → 18.5x | 27% → 21x | 32% → 23.5x | 40% → 26x | 50% → 29x | 55%+ → 30x.

- Round the base to one decimal. Do not round intermediate ROCE.
- The band above 33% is for genuinely capital-light names that cross 33% ROCE. It does not relax any sector cap.
- Lenders (banks, NBFCs, MFIs, HFCs): ROE replaces ROCE in the same formula.

## ROCE selection: the FTTCP ROCE forward verdict is the sole authority

No standalone trajectory judgment exists. Pillar 1 cannot be computed without the FTTCP verdict.

| FTTCP ROCE forward verdict | Pillar 1 ROCE used |
|---|---|
| FIRING | Current ROCE |
| RECOVERING, probability >60% with Strong catalysts | Midpoint of current and FY[Y+2] expected ROCE |
| RECOVERING, probability 40-60% | 60/40 weighted average of current and FY[Y+2] |
| STAGNANT | Current ROCE |
| DECLINING | FY[Y+1] expected ROCE (lower bound) |

Hybrid verdict labels do not exist. A TEMPORARILY DEPRESSED backward verdict yields forward RECOVERING, even at >60% with Strong catalysts, until the recovery is confirmed in reported numbers; it then becomes FIRING.

## Normalization for capital-cycle names (consolidated Amendment 9)

Point-in-time ROCE misprices a capital-cycle business through two channels:

1. Denominator bloat: CWIP, idle raised capital and capex advances sit in capital employed but do not yet earn.
2. Numerator trough: current EBIT is cyclically depressed against evidenced pre-capex earning power.

A run normalizes through ONE route only. Two routes credit the same recovery twice. The worksheet declares the route.

### Route selection

| Condition | Route |
|---|---|
| (CWIP + idle raised capital + capex advances) > 20% of capital employed | Route A, Operational ROCE (denominator fix) |
| Denominator clean (test above fails) BUT FTTCP verdict TEMPORARILY DEPRESSED or RECOVERING with 📄-evidenced pre-depression ROCE history | Route B, Pre-Cycle Normalized ROCE (numerator fix) |
| Both conditions hold | Route A governs. Worksheet note: "Route B condition also present, suppressed per single-credit rule." |
| Neither holds | No normalization. Statutory ROCE feeds Pillar 1 directly. |

Neither route may be invoked on a STAGNANT or DECLINING ROCE verdict. FTTCP is the sole source of the recovery verdict and its probability.

### Route A: Operational ROCE

- Operational capital employed = capital employed − non-operating cash and investments − CWIP − capex advances. Adjust EBIT to exclude income the stripped assets generate (for example interest on idle cash), so numerator and denominator stay consistent.
- Mid-cycle ROCE = normalized EBIT on that operational base at target or steady-state utilization, taken from the FTTCP RECOVERING blend where a recovery verdict applies, else trailing operational ROCE.
- 9.1 Blend consistency: either both blend endpoints are computed on the same operational basis, or the blend is skipped and operational ROCE feeds the formula alone. Worksheet: "Blend basis: [operational-consistent / blend skipped]."
- 9.2 Staleness: capital qualifies for stripping only with 📄 evidence of a deployment plan and a commissioning timeline within 24 months. Idle capital beyond that stays in the denominator and is flagged to Role 3 as a capital-allocation concern.
- Mandatory disclosure line: statutory ROCE, each stripped item with its amount, resulting operational ROCE. Never management's "adjusted ROCE".
- EV/EBITDA cross-check where that is the primary method: a divergence above 25% requires a stated governing choice.

### Route B: Pre-Cycle Normalized ROCE

- Third ROCE anchor = median ROCE of the evidenced pre-depression cycle, 📄-gated (audited filings only), capped at the evidenced historical level, never extrapolated above what the company has printed.
- Named unwind catalyst required: a specific, dated, documented mechanism (capacity commissioning, contract restart, regulatory clearance). "Cycle will turn" is not a catalyst.
- Probability-weighted blend with current ROCE per the FTTCP recovery probability. RECOVERING (40-60%) blends 60/40 current/anchor. Higher-confidence verdicts may weight the anchor more, per the FTTCP verdict band.
- Self-withdrawal: if the recovery does not print by the named catalyst date plus one quarter of grace, the anchor is withdrawn at the next refresh, Pillar 1 reverts to statutory ROCE, and the withdrawal is logged in Key Notes.
- Route B lifts fair value toward evidenced reality. It does not manufacture an entry zone.

## Converters

Spot-year ROCE never feeds Pillar 1 for a CONVERTER, in either direction. The through-cycle input is computed after the declared route is applied, never as a second credit. See chunk 11.

## Single credit touching Pillar 1

- ROCE recovery credited here bars the Strategic Premium route (chunk 04).
- A capital-base distortion is fixed by Route A/B or by FTTCP Module B6, never both. Declare which governs.
- A depressed base year is normalized by FTTCP Module B3 or by Route B, never both. Declare which.
- Where Amendment 10's intrinsic cross-check triggers, the DCF uses the same route-declared ROCE basis. Amendment 10's own trigger and mechanics text is NOT FOUND in frameworks/.

## Worksheet lines

- "FTTCP ROCE forward verdict: ___ | ROCE (or ROE) used for base: ___% | ROCE Base Multiple: ___x | ROCE recovery credited via: [Pillar 1 / Strategic Premium / not credited]"
- "Pillar 1 normalization route: [NONE / A-Operational / B-Pre-Cycle / A-governs-B-suppressed]. If A: statutory ___%, stripped items [list+amounts], operational ___%, blend basis ___. If B: pre-cycle median ___% (source: [filing, years]), unwind catalyst [named, dated, 📄], blend weight ___/___, self-withdrawal date ___."
- CONVERTER only: "Spot ROCE ___% | through-cycle ROCE used ___% (basis: 5-7 year average / midpoint of current and cycle trough)"
