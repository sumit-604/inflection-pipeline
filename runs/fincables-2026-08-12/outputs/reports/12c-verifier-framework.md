# STAGE 12c — VERIFIER C: FRAMEWORK ADHERENCE AUDIT
# PHASE 1 SCOPE (Gate 0 B01 + Emerging Moat B07). Valuation (B11/B10) DEFERRED to Phase 3.
# RE-VERIFICATION of the revised v2 audited Gate 0 (AVOID→AVERAGE, core 37→42, moat THIN→NONE).

Company: Finolex Cables Ltd (FINCABLES) | Run date: 2026-08-12 | Model: claude-opus-4-8
Verifier scope: rule application only (numbers are Verifier A's domain). Fresh context.
Authorities used: prompts/01-gate-0-pipeline.md (Gate 0 rules), prompts/07-emerging-moat-pipeline.md
(20-category scan rules). Master v3.3 / Section 1B v3.3 / 1B v3.5.1 reconciliation are exit-PE /
valuation authorities and are OUT of Phase 1 scope; not exercised here.

Bottom line: the revised Gate 0 and the unchanged Emerging Moat scan are BOTH applied as written.
Every block score, the classification-matrix mapping, the moat cascade, the deal-breaker sweep, the
cash-flag treatment, and the emerging-moat multiplier discipline re-derive to the reported values.
No CRITICAL, no MAJOR. Three MINOR advisory observations, none of which flip any classification or
destination. recomputed_decision: concur (AVERAGE). recomputed_moat_class: concur (NONE).

═══════════════════════════════════════════════════════════════════
## PART 1 — GATE 0 (B01) RE-DERIVATION, RULE BY RULE
═══════════════════════════════════════════════════════════════════

### Block A — Return on Capital (framework prompt 01, lines 56-60)

| Rule | Stated input | Band applied | Re-derived | PASS/FAIL |
|---|---|---|---|---|
| A1 Median ROCE | median of 10 yrs = 17.95% | 15-19.9 → 3 | median{14.16,14.84,15.60,17.06,17.44,18.46,20.05,22.33,22.66,23.71}=(17.44+18.46)/2=17.95% → 3 | PASS |
| A2 Min single-yr ROCE | 14.16% (FY26) | 12-14.9 → 3 | 14.16% → band 12-14.9 → 3 | PASS |
| A3 Median ROE | 14.19% | 12-14.9 → 2 | median → 14.19% → 2 | PASS |
| A4 ROCE trend | 14.16 vs 23.71 = -9.55pp | >5pp decline → 0 | -9.55pp → 0 | PASS |
| Block A total | 8/20 | — | 3+3+2+0 = 8 | PASS |

Note: audited FY26/FY25 ROCE corrections (15.60%/14.16%) did not move any Block A band vs v1; A2 min
is now the FY26 audited 14.16% (same band as v1's FY23 proxy 14.84%). Consistent.

### Block B — Cash Generation Quality (lines 63-69)

| Rule | Stated input | Band applied | Re-derived | PASS/FAIL |
|---|---|---|---|---|
| B1 Cum CFO/PAT (10yr) | 2,688.26/5,159.88 = 0.521 | 0.50-0.69 → 1 | 0.521 → 1 | PASS |
| B2 FCF-positive years | 7/9 = 77.8% | 75-99 → 4 | 7 of 9 computable → 77.8% → 4 | PASS |
| B3 Cum FCF/PAT (FY18-26) | 1,606.92/4,759.64 = 0.338 | 0.20-0.39 → 1 | 0.338 → 1 | PASS |
| B4 ΔWC days (FY25→26) | +18.38 days | increased >15 → 0 | 67.64 − 49.26 = +18.38 → 0 | PASS |
| Block B total | 6/20 | — | 1+4+1+0 = 6 | PASS |

B4 window note: framework intends latest-vs-earliest full-history; report scores a 2-yr window because
Trade Payables are absent pre-FY25. This is disclosed as a limitation and scored on real audited
evidence rather than left blank — the score (0) is invariant to the window here (the FY25→FY26 increase
alone is >15 days). Handled per the missing-data rule; not a silent full-history substitution. PASS.

### Block C — Growth (lines 72-75) — unchanged from v1

| Rule | Input | Band | Re-derived | PASS/FAIL |
|---|---|---|---|---|
| C1 Revenue CAGR (9yr) | 11.13% | 10-14.9 → 3 | (6,321.01/2,444.84)^(1/9)-1 = 11.13% → 3 | PASS |
| C2 PAT CAGR (9yr) | 6.64% | 5-9.9 → 1 | (713.72/400.24)^(1/9)-1 = 6.64% → 1 | PASS |
| C3 Positive YoY yrs | 7/9 = 77.8% | 75-99 → 3 | 2 declines (FY20,FY21) of 9 → 77.8% → 3 | PASS |
| C4 PAT−Rev CAGR | -4.49pp | -3 to -8 → 1 | 6.64−11.13 = -4.49 → 1 | PASS |
| Block C total | 8/20 | — | 3+1+3+1 = 8 | PASS |

CAGR edge rules (lines 44-52): all endpoints positive, PAT positive all 10 yrs, no loss-to-profit
swing → no N/M, no synthetic CAGR; data_notes records the no-swing condition. Honoured. PASS.

### Block D — Balance Sheet Strength (lines 77-87) — the largest change this run

| Rule | Stated input | Band applied | Re-derived | PASS/FAIL |
|---|---|---|---|---|
| D1 Net Debt/EBITDA | ND = 0.86 − 163.13 = -162.27 (net cash) | net cash → 5 | net cash → 5 | PASS |
| D2 Interest coverage | 930.27/1.75 = 531.6x | ≥10x → 5 | 531.6x → 5 | PASS |
| D3 Debt/Equity | 0.86/6,085.88 = 0.0001x | <0.1 → 5 | 0.0001x → 5 | PASS |
| **D4 Current Ratio** | **3,531.97/419.61 = 8.42x** | **≥2.0 → 5** | **8.42x → band ≥2.0 → 5** | **PASS** |
| Block D total | 20/20 | — | 5+5+5+5 = 20 | PASS |

**CHECK 1 (Current Ratio) — CONFIRMED.** Framework D4 bands (line 86): ≥2.0=5 | 1.5-1.99=4 |
1.2-1.49=2 | 1.0-1.19=1 | <1.0=0. Audited consolidated current assets 3,531.97 ÷ current liabilities
419.61 = 8.42x, far above the 2.0 top band → 5/5. The v1→v2 move D 15→20 is driven solely by D4
going from a data-absence N/A (0) to a computed 5. This is a data-completeness fix, correctly NOT
characterised as a business-quality improvement. The framework requires "N/A (not in provided data)
→ score 0" when a split is unavailable (line 24-26); v1 obeyed that, and v2 correctly re-scores once
the audited split exists. Band application correct. PASS.

### Block E — Shareholder Alignment (lines 90-96) — 0/20

E1-E4 all N/A: no shareholding FILING supplied (only a non-anchored screener.in screenshot). Per the
missing-data rule (score 0, mark N/A) and per explicit operator instruction not to score on the
screenshot → 0/20. The report labels this a data-absence outcome, NOT a scored governance weakness.
Note on E1's "professionally managed: 3 if FII+DII >50%" carve-out: even if the screenshot were
scoreable, FII 9.65% + DII 16.71% = 26.36% (<50%), so the carve-out would not apply; the 0 stands on
both the operator instruction and the arithmetic. PASS (missing-data rule correctly applied).

### Block F — Quantitative Moat (lines 98-139)

| Test | Score | Re-derived band | PASS/FAIL |
|---|---|---|---|
| M1 Pricing Power | 0 | EBITDA margin fell 16.20→9.80% (>2pp decline despite growth) → "else 0" | PASS |
| M2 Cost Advantage | 0 | PEER DATA NEEDED → 0 (never guessed) | PASS |
| **M3 Capital Efficiency** | **1** | FAT 7.44x (>3x); ROCE 14.16% not >20, not >15, but >12 → "FAT>1x AND ROCE>12% = 1" | **PASS** |
| M4 Customer Stickiness | 1 | 2 decline yrs, CAGR positive → 1 | PASS |
| M5 Scale & Dominance | 0 | PEER DATA NEEDED → 0 | PASS |
| M6 Technology/R&D | 0 | no R&D line disclosed → 0 | PASS |
| M7 Regulatory/License | 0 | unregulated → 0 | PASS |
| M8 Distribution | 1 | mentioned unquantified (stale AR) → 1 | PASS |
| M9 Brand | 0 | PEER DATA NEEDED → 0 (GM proxy informational only) | PASS |
| M10 Switching Costs | 1 | overall growth, 2 decline yrs → 1 | PASS |
| M11 Network Effects | 0 | latest 3yr CAGR 12.14% < prior 15.93%, neither ≥20% → 0 | PASS |
| M12 Negative WC/Float | 0 | 2-yr window 49-68 days, well above 0-15 band → 0 | PASS |
| Moat total | 4/60 | — | 0+0+1+1+0+0+0+1+0+1+0+0 = 4 | PASS |

**CHECK 2 (M3 cascade) — CONFIRMED.** Framework M3 (line 108): "FAT>3x AND ROCE>20%=5 | FAT>2x AND
ROCE>15%=3 | FAT>1x AND ROCE>12%=1 | else 0." Inputs: FAT = 6,321.01/849.78 = 7.44x; ROCE (FY26
audited) = 14.16%. Walking the ladder: 14.16 is not >20 (skip 5); not >15 (skip 3); is >12 with FAT>1x
(land on 1). Score = 1. The v1 figure (proxy ROCE 15.24%) cleared the >15 gate and scored 3; the
audited 14.16% falls just under the strict >15% threshold, so 3→1 is a correct, evidenced cascade, not
a data artifact. ROCE computation method: framework line 29 defines ROCE = EBIT ÷ (Total Assets −
Current Liabilities); the report uses EBIT (=PBT+Interest, consolidated) ÷ (Total Assets − Total
Current Liabilities, consolidated) = identical formula, with numerator and denominator kept on the same
consolidated base (associate profit in PBT, associate investment in capital employed). Framework-
consistent. PASS.

MINOR observation (advisory, not a FAIL — see MINOR-1 below): the framework does not state whether M3's
ROCE input is the latest-year or the median ROCE. The report uses latest-year FY26 ROCE (14.16%),
which is the internally consistent choice because it is paired with a latest-year FAT (FY26 sales ÷
FY26 net block), and it is the same convention v1 used. If median ROCE (17.95%) were substituted, M3
would score 3 and moat_class would remain THIN — but this would NOT change the classification (AVERAGE
is fixed by core 40-59 irrespective of moat class) nor the B07 combined_assessment (both THIN and NONE
fail the GOOD bar). Flagged for operator awareness; no destination impact.

Moat classification (line 138): 0 tests ≥3 → NONE. Re-derived: highest moat test is 1 (M3/M4/M8/M10);
none reach the "present" threshold of 3 → 0 present → NONE. Correct. THIN→NONE is a genuine evidenced
move (M3 dropping out of "present"). PASS.

### Classification, confidence, deal-breakers (lines 141-160)

**CHECK 3 (Classification matrix) — CONFIRMED.** Core = 8+6+8+20+0 = 42. Matrix (line 150): "Core
40-59 = AVERAGE | Core <40 = AVOID." Core 42 → AVERAGE. Moat class does not enter the tiering at core
40-59 (only Core ≥60 and Core ≥80 rows are moat-sensitive), so moat NONE correctly does not alter the
AVERAGE tier. Prior v1 core 37 → <40 → AVOID is likewise correct; the boundary is exact — a single
point (37→42 crossing 40) is the pivot, and it is driven entirely by the D4 data-completeness fix. Both
the AVERAGE (v2) and the AVOID (v1) map correctly; the boundary is applied right. PASS.

Data confidence (line 146): 10 years → "10+ yrs full", no downgrade. Correct. PASS.

Deal-breaker sweep (lines 157-160), all 9 tested:
1. Block A <8 → A=8 (not <8) → not triggered. PASS.
2. Block B <8 → B=6 → TRIGGERED, cap max GOOD. Correctly recorded as non-binding (AVERAGE already
   below GOOD). PASS.
3. Median ROCE <10% → 17.95% → not triggered. PASS.
4. Cumul CFO/PAT <0.50 → 0.521 → not triggered. Correct: 0.521 > 0.50 (a near-miss the report
   discloses, but the rule as written keys on the cumulative figure, which is above 0.50). PASS.
5. Pledge >15% → data absent → cannot confirm, not triggered. PASS.
6. ND/EBITDA >3x AND IC <3x → net cash / IC 531.6x → not triggered. This is the only deal-breaker that
   forces AVOID; correctly not triggered, so AVERAGE stands. PASS.
7. Revenue declined majority of years → 2 of 9 → not majority → not triggered. PASS.
8. PAT negative in any of last 3 yrs → positive FY24-26 → not triggered. PASS.
9. History <3 yrs → 10 yrs → not triggered. PASS.

No deal-breaker floors below AVERAGE; caps are max-ceilings only and none bite. Classification AVERAGE
survives the full sweep. PASS.

### CHECK 4 — Cash-flag handling vs CLAUDE.md INDETERMINATE rule

CLAUDE.md: "Never let INDETERMINATE cash conversion silently resolve to PROCEED. It caps at PROCEED
WITH CAVEATS with the missing evidence named." The report classifies the FY26 CFO collapse (standalone
CFO/PAT 38.1%→7.9%) as a working-capital-timing event: "not INDETERMINATE (drivers are evidenced), not
a genuine leak (operating profit before WC improved 527.91→640.21), but an unconfirmed-reversal event."
Crucially, it does NOT resolve to clean: it (a) names the specific missing evidence (no FY27 cash flow
statement exists in the Q1 FY27 filing), and (b) explicitly caps downstream confidence at a "PROCEED
WITH CAVEATS-equivalent" read via FLAG-CASH. The letter of the CLAUDE.md rule governs INDETERMINATE
cases; here the maker argues the drivers are evidenced (inventory +306.14cr, receivables +127.61cr,
both traced in the audited standalone cash flow) so it is not INDETERMINATE — but it still applies the
conservative cap and names the missing evidence, which is exactly the treatment the rule demands. No
silent resolution to clean. COMPLIANT. PASS.

### CHECK 5 — Data-absence zeros not conflated with measured weakness

- Block E (0/20): labelled "data-absence outcome, not a scored weakness" (report §Block E, §Strongest/
  Weakest, YAML input_gaps). Correct per missing-data rule. PASS.
- M2/M5/M9 (0): marked "PEER DATA NEEDED", never guessed, consistent with line 101 ("never guess peer
  figures"). PASS.
- Full-history B4/M12: Trade Payables absent pre-FY25; scored on the disclosed 2-yr window with the
  limitation stated, not silently treated as a full-history trend. The report separates these from
  genuine measured depressors (A4 ROCE decline, M1 margin compression, C4 operating de-leverage, the
  FY26 cash air-pocket), which it lists explicitly in FLAG-GATE0. PASS.

FLAG-GATE0 presence: the prompt requires a FLAG-GATE0 when classification ≤ AVERAGE with historical
depressors identified (line 176-178). AVERAGE with depressors → flag present and correctly populated.
PASS.

═══════════════════════════════════════════════════════════════════
## PART 2 — EMERGING MOAT (B07) RE-CONFIRMATION
═══════════════════════════════════════════════════════════════════

The B07 report is UNCHANGED (ran against v1 Gate 0). Re-confirming its scoring is framework-correct and
that its combined_assessment survives the revised Gate 0.

### Scorecard re-derivation (prompt 07 lines 126-132)

Multipliers 📄 1.0 / 🎙️ 0.7 / 🔍 0.5; matrix HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, none=0.

| # | L×I | Raw | Factor | Adj | Re-derived | PASS/FAIL |
|---|---|---|---|---|---|---|
| A1 | MH | 3 | 📄 1.0 | 3.0 | 3×1.0 = 3.0 | PASS |
| A3 | HM | 3 | 📄 1.0 | 3.0 | 3.0 | PASS |
| A4 | LL→ML | 1 | 🎙️ 0.7 | 0.7 | 1×0.7 = 0.7 | PASS |
| B1 | HM | 3 | 📄 1.0 | 3.0 | 3.0 | PASS |
| B2 | MM | 2 | 🎙️ 0.7 | 1.4 | 2×0.7 = 1.4 | PASS |
| C1 | LL | 1 | 🔍 0.5 | 0.5 | 1×0.5 = 0.5 | PASS |
| E2 | ML | 1 | 📄 1.0 | 1.0 | 1.0 | PASS |
| F2 | MM | 2 | 📄 1.0 | 2.0 | 2.0 | PASS |
| G1 | HM | 3 | 📄 1.0 | 3.0 | 3.0 | PASS |
| H2 | HM | 3 | 📄 1.0 | 3.0 | 3.0 | PASS |
| R1 | MM | 2 | 🎙️ 0.7 | 1.4 | 1.4 | PASS |
| others (10) | none | 0 | — | 0 | 0 | PASS |

Adjusted total re-derived: 3.0+3.0+0.7+3.0+1.4+0.5+1.0+2.0+3.0+3.0+1.4 = **22.0**. Matches. Band
(line 131-132): 12-24 → MODEST MOAT DEVELOPMENT. Correct.

All 21 categories addressed (A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G3? no — G1/G2, H1-H3, R1 =
21). Each is either scored or explicitly NO EVIDENCE FOUND. PASS.

Evidence-multiplier discipline (verifier rubric item: no 🎙️-only category scored as if 📄): the 1.0-
factor rows (A1, A3, B1, E2, G1, H2) each rest on a genuinely documented anchor (preform commissioned;
e-beam facility in market; export actuals ₹30cr→₹52cr; near-zero-borrowings balance sheet; Sumitomo JV
FY26 revenue/PBT/order-book). The claim-laden rows (A4, B2, R1) correctly take 0.7; the stale-AR row
(C1) correctly takes 0.5. No 🎙️-only category is credited at 1.0. PASS.

Completionist guard (lines 30-36): base rate 3-6, hard re-examine trigger at 12+ active. Report has 7
Strong/Moderate rows and performs the required explicit 📄 recount (9 documented items across 6
categories). 7 < 12, so the hard trigger is not hit, and the recount is nonetheless performed as
instructed and justified (excess concentrated in documented capex/financial facts). PASS.

### CHECK 6 — combined_assessment AVERAGE under the revised Gate 0

B07's 6D combined-classification logic (prompt 07 lines 154-159): HIGH POTENTIAL / TURNAROUND require a
STRENGTHENING or EXPANSION forward score; GOOD / GOOD+ require a stronger existing-moat base. B07's
forward read is MODEST (unchanged, 22.0) and its backward read is AVERAGE-quality. Under the REVISED
Gate 0 the backward read is now FORMALLY AVERAGE (core 42, matrix-derived) rather than the "ex-Block E
rationalised AVERAGE" the B07 narrative had to construct from v1's headline AVOID, and the existing-moat
base is now 0/NONE (weaker than the 1/THIN B07 cites). Walking the matrix with the revised inputs:
forward still MODEST (not STRENGTHENING/EXPANSION) → not HIGH POTENTIAL, not TURNAROUND; existing moat
now 0/NONE → further from GOOD/GOOD+, not closer; core AVERAGE. Result: **combined_assessment = AVERAGE
still holds, and holds more robustly** than in the as-written report (the revised Gate 0 removes the
tension B07 flagged between the v1 headline AVOID and its ex-Block-E AVERAGE flag). 22.0/MODEST and
combined AVERAGE are framework-correct. PASS.

MINOR observation (MINOR-2 below): B07's §6C table and §6D narrative cite the SUPERSEDED v1 Gate 0
figures (core 37, moat 6, moat_class THIN, headline AVOID). Because B07 ran before the audited re-run,
this is expected staleness, not a scoring error; the combined output (AVERAGE) is unaffected and, as
shown, is if anything reinforced by the revised inputs. Synthesis should reconcile the stale internal
references, but no re-scoring of B07 is warranted.

═══════════════════════════════════════════════════════════════════
## PART 3 — VALUATION (B11 / B10) — DEFERRED
═══════════════════════════════════════════════════════════════════

Per task scope, the valuation-adherence audit (continuous Pillar 1 formula, FTTCP ROCE authority,
single-credit rule, Pillar 2/3, UA Amendment 3 order, sector cap, dual-track, Hurdle Ratio, 4D weights,
SOM cross-check, exit-PE authority per Section 1B v3.3 / v3.5.1) is DEFERRED to Phase 3 and was NOT run.
Master v3.3, Section 1B v3.3, and the 1B v3.5.1 reconciliation were not exercised. valuation: {status:
pending-phase-3}.

═══════════════════════════════════════════════════════════════════
## FINDINGS (all advisory MINOR; no CRITICAL, no MAJOR; no rule FAILs)
═══════════════════════════════════════════════════════════════════

- MINOR-1 (gate0, M3): framework does not specify latest-year vs median ROCE for the M3 Capital
  Efficiency test. Report uses latest-year FY26 ROCE (14.16%), internally consistent with the latest-
  year FAT it is paired with and with v1's convention. Under a median-ROCE reading (17.95%) M3 would
  score 3 and moat_class would stay THIN, but neither the AVERAGE classification (core 40-59, moat-
  insensitive) nor the B07 combined_assessment would change. No destination impact. Recommend the
  framework state the ROCE basis for M3 explicitly.
- MINOR-2 (emoat, §6C/§6D): B07 cites superseded v1 Gate 0 figures (core 37 / moat 6 / THIN / AVOID).
  Expected pre-revision staleness; combined_assessment AVERAGE is unaffected and reinforced by the
  revised inputs. Reconcile at synthesis.
- MINOR-3 (gate0, presentational): the cash-flag section asserts "not INDETERMINATE" while the
  CLAUDE.md rule is framed around INDETERMINATE cases; the treatment applied (name missing evidence,
  cap at caveated) is nonetheless exactly what the rule requires, so this is a labelling nuance, not a
  compliance gap. No action beyond noting the maker relies on evidenced drivers to step outside the
  INDETERMINATE branch.

## VERDICT

Gate 0 v2 (audited re-run): every block, the classification matrix, the moat cascade, the deal-breaker
sweep, and the cash-flag treatment are applied AS WRITTEN. The AVOID→AVERAGE move (core 37→42) is a
correct data-completeness re-score of D4, and the THIN→NONE move is a correct evidenced M3 cascade;
neither is a framework misapplication. Emerging Moat: 22.0/MODEST and combined AVERAGE re-derive exactly
and remain framework-correct under the revised Gate 0. recomputed_decision: concur (AVERAGE).
recomputed_moat_class: concur (NONE). All findings are MINOR/advisory with zero destination impact.
framework_adherence: 100% (0 rule FAILs across rules checked).

```yaml
stage: B12c
company: "FINCABLES"
run_date: "2026-08-12"
model: claude-opus-4-8
status: complete
phase: 1
scope: "gate0 (B01) + emerging moat (B07); valuation deferred to phase 3"
gate0:
  rules_checked: 51
  fails: []
  findings:
    - {severity: "MINOR", ref: "M3", note: "framework unspecified on latest-vs-median ROCE for M3; report uses latest-year FY26 ROCE (14.16%), internally consistent with latest-year FAT and v1 convention; median reading (17.95%) would give M3=3/THIN but would not change AVERAGE classification or B07 combined; no destination impact"}
    - {severity: "MINOR", ref: "cash-flag", note: "cash-flag labelled 'not INDETERMINATE' while CLAUDE.md rule is framed around INDETERMINATE; treatment applied (missing evidence named, capped at caveated read, no silent resolution to clean) is exactly rule-compliant; labelling nuance only"}
  check_results:
    current_ratio_D4: "CONFIRMED — 3,531.97/419.61 = 8.42x -> band >=2.0 -> 5/5; Block D 15->20 is a data-completeness fix, band applied correctly"
    m3_cascade: "CONFIRMED — FAT 7.44x, ROCE 14.16% audited: not >20, not >15, but >12 -> M3=1; ROCE = EBIT/(Total Assets - Current Liabilities) is framework-consistent; 3->1 cascade correct; moat 6->4, THIN->NONE correct"
    classification_matrix: "CONFIRMED — core 42 -> 40-59 -> AVERAGE (moat-insensitive tier); prior core 37 -> <40 -> AVOID; boundary exact and correctly applied"
    cash_flag_vs_claudemd: "COMPLIANT — does not silently resolve to clean; names missing FY27 cash flow evidence; caps at PROCEED WITH CAVEATS-equivalent"
    data_absence_zeros: "CORRECT — Block E, M2/M5/M9, full-history B4/M12 handled per missing-data rule, not conflated with measured weakness"
    deal_breakers: "all 9 tested; only B<8 (rule 2, non-binding cap) and none forcing AVOID; AVERAGE survives"
emoat:
  rules_checked: 28
  fails: []
  findings:
    - {severity: "MINOR", ref: "6C/6D", note: "B07 cites superseded v1 Gate 0 figures (core 37/moat 6/THIN/AVOID); expected pre-revision staleness; combined_assessment AVERAGE unaffected and reinforced by revised inputs; reconcile at synthesis"}
  check_results:
    score_recount: "CONFIRMED — adjusted total re-derives to 22.0; band 12-24 -> MODEST"
    multiplier_discipline: "CONFIRMED — no 🎙️-only category credited at 1.0x; claim/stale rows correctly 0.7/0.5"
    completionist_recount: "PERFORMED — 7 active rows < 12 hard trigger; 📄 recount (9 items/6 categories) present and justified"
    all_21_addressed: true
    combined_assessment: "CONFIRMED AVERAGE — holds under revised Gate 0 (core formally AVERAGE, moat NONE); forward MODEST fails STRENGTHENING/EXPANSION bar for HIGH POTENTIAL/TURNAROUND; existing moat 0/NONE fails GOOD/GOOD+ bar"
valuation: {status: pending-phase-3, rules_checked: 0, fails: []}
recomputed_destination_pe: ""        # deferred to phase 3
recomputed_decision: ""              # concur — AVERAGE (core 42), no re-derivation delta
recomputed_moat_class: ""            # concur — NONE (0 of 12 tests confirmed)
findings:
  - {severity: "MINOR", location: "B01 M3", note: "M3 ROCE basis (latest vs median) unspecified by framework; latest-year use is internally consistent and non-destination-changing"}
  - {severity: "MINOR", location: "B07 6C/6D", note: "stale v1 Gate 0 figures cited; combined_assessment AVERAGE unaffected"}
  - {severity: "MINOR", location: "B01 cash-flag", note: "'not INDETERMINATE' labelling nuance; treatment is rule-compliant (evidence named, capped, not resolved clean)"}
critical_count: 0
major_count: 0
minor_count: 3
framework_adherence: 100
acceptance_rate: 100
```
