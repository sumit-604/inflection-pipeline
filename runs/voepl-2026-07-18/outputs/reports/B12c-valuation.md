# STAGE 12 — VERIFIER C: FRAMEWORK ADHERENCE (B12c) — PHASE 3 VALUATION HALF
## Virtuoso Optoelectronics Ltd (VOEPL) — Run 2026-07-18

**Model:** claude-opus-4-8
**Scope:** PHASE 3 VALUATION-ADHERENCE audit. Role 1 valuation (B11) + assembled inputs (B10) against Section 1B v3.3 four-pillar framework, RRM dual-track, Hurdle Ratio, sector cap, UA ordering, single-credit; EXTENDED to Role 2 (B14) decision rules + position sizing against Master v3.3 Role 2. Destination PE, Hurdle Ratio and decision recomputed independently.
**Out of scope (phase 1, not re-audited):** Gate 0 (B01) and Emerging Moat (B07). Restated pass status only: 99% adherence, 0 CRIT / 0 MAJ, 1 MINOR.

---

## SUMMARY

Fresh-context recomputation CONCURS with B11's destination PE (within tolerance), Hurdle Ratio STOP, and the AVOID-on-valuation decision, and with B14's Role 2 decision-rule and position-size logic. One MAJOR framework-adherence fail: the Pillar 1 ROCE blend was computed with the RETIRED Amendment 4.5 three-anchor formula (40% normalized + 30% FY[Y+2] + 30% current) after the worksheet had correctly selected Reconciliation v3.5.1 Route B as governing — and Route B specifies a 60/40 current/anchor two-anchor blend. The deviation overstates blended ROCE by ~1.1 pp and destination PE by ~0.5x in the LESS-conservative direction, but does not flip the Hurdle verdict or the decision (STOP holds by a wide margin under either blend). Two MINOR notes recorded. No CRITICAL.

---

## PART A — VALUATION (B11 + B10), the deep audit

### A1. Method selection (Master 1A) — PASS
- P/E primary (80% nominal, effectively governing); EV/EBITDA secondary marked INPUT UNRESOLVED → zero effective weight, no fabricated net-debt bridge; P/B and DCF excluded with business-appropriate reasons (asset base ramping; negative FCF/high terminal sensitivity). Compliant with Master method matrix and conservative-bias rule.
- Per-share work on the single stated share basis (3.18 Cr FY26, reconciles Mcap 1,621 ÷ 3.18 ≈ CMP 509). EPS/PE on REPORTED-EPS basis throughout — the LESSONS discipline (no cash-EPS PE mixed with reported-EPS growth) is explicitly honoured. PASS.

### A2. Pillar 1 — continuous formula, FTTCP authority, route selection

| Rule | Framework | B11 application | Verdict |
|---|---|---|---|
| Continuous formula, not old bands | Amendment 5 / Master 207-216 | 0.5×ROCE+7.5 used | PASS |
| FTTCP RECOVERING sole Pillar 1 authority, no ad hoc trajectory | FTTCP v1.2 lines 360-372; Master 218 | RECOVERING (operator-affirmed) applied; no ad hoc smoothing | PASS |
| Route A denominator test (CWIP+idle+advances >20% CE) | Recon 3.5.1 Route A | Capital employed / CWIP NOT FOUND (image-only BS) → Route A cannot be evidenced → does not apply | PASS (route selection correct) |
| Route B governs (denominator clean/untestable + TEMPORARILY DEPRESSED/RECOVERING + 📄 pre-depression print) | Recon 3.5.1 Route B | Route B selected as governing | PASS (selection) |
| **Route B blend weights** | **Recon 3.5.1 Route B: "RECOVERING (40-60%) blends 60/40 current/anchor"** | **Used RETIRED Amendment 4.5 three-anchor 40% norm + 30% FY[Y+2] + 30% current** | **FAIL — MAJOR** |
| Normalized anchor 📄-gated, capped at evidenced level, named/dated unwind catalyst | Amendment 4.5 / Recon 3.5.1 Route B | 25.66% (FY24) capped; catalyst = compressor commissioning ~Mar-2027 (named, dated, 📄) | PASS-with-caveat (see MINOR-1) |
| Single-credit route stated | Master 228 / FTTCP 374-376 | "ROCE recovery credited via: Pillar 1"; Strategic re-rating barred | PASS |

**MAJOR finding (Pillar 1 blend).** The worksheet states "Route B governs (operator-designated Amendment 4.5 anchor)" and then applies the three-anchor blend `0.40×25.66 + 0.30×21.0 + 0.30×17.19 = 21.72%`. But Reconciliation v3.5.1 explicitly "supersedes both texts," RETIRES Amendment 4.5 as a number, and defines Route B's blend as **60/40 current/anchor** for the RECOVERING 40-60% band — a two-anchor blend that does NOT use an FY[Y+2] leg (and therefore does not need the invented FY28 21.0% projection the worksheet itself flags as "not an external fact").

Recompute under governing Route B:
- Blended ROCE = 0.60 × 17.19 + 0.40 × 25.66 = **20.58%** (vs 21.72% used)
- Pillar 1 base = 0.5 × 20.58 + 7.5 = **17.8x** (vs 18.4x used)
- Quality-adjusted base = 17.8 × 0.85 = **15.1x** (vs 15.6x)
- Raw destination PE (Track 2) = 15.1 + 5.0 + 0 = **20.1x** (vs 20.6x)
- Track 1 (RRM) = 20.1 × 0.70 = **14.1x** (vs 14.4x)

Impact ~0.5x on destination PE, in the LESS-conservative direction (the maker's blend is higher, not lower, than the governing spec). Within the 1x tolerance and does not flip the Hurdle verdict or decision → MAJOR, non-outcome-determinative. STOP holds under either blend (see A9).

### A3. Pillar 2 — cash conversion multiplier — PASS

| Rule | Application | Verdict |
|---|---|---|
| Base band: CFO/PAT 0.22x (<30%) → 0.80x | 0.80x base assigned | PASS |
| Structural vs growth-induced test | GROWTH-INDUCED (operator-affirmed); no CARE structural assessment exists to override (ICRA notes "improvement from previous years") | PASS |
| No 0.65x structural multiplier misapplied | Correctly not structural | PASS |
| Growth offset applies to growth-induced only | +0.05 applied; ambiguous "PAT/Revenue CAGR" table resolved conservatively on revenue CAGR 22% (<25% → +0.05) rather than PAT CAGR ~35% (would give +0.10) | PASS (conservative, Master 73) |
| Effective multiplier matches determination | 0.80 + 0.05 = 0.85x | PASS |
| Residual gap named, not silently absorbed | Note 37 unconfirmed WC named as FLAG-CASH; falsifier H1 FY27 CFO/PAT <0.5x stated; multiplier unchanged (no CAVEATS cap since growth-induced, not indeterminate) | PASS |

### A4. Pillar 3 — decoupled 3a/3b/3c, +6x cap — PASS
- **3a** (Amendment 4.1): two qualify — capex-embedded growth 122% (📄) and management grade B; order book NOT FOUND; SOM-implied 25.2% but capacity cross-check fails (Rs705 Cr gap) → not qualifying. Two qualify → **+2x** (not +3x, which needs three-plus). PASS.
- **3b** (Master 297-305): EM 31 (band 30-39), catalyst 0-12m, evidence MIXED (Documented 17 / Claim 24 / Inference 6, claim-heavy → correctly "mixed," not "mostly documented") → **+3x**. PASS. (A 🎙️/claim-heavy set correctly did not score the "mostly 📄" +4x row.)
- **3c** (Amendment 4.2): executable order book ≥2.5x revenue NOT FOUND → **+0x**. PASS.
- Combined 3a+3b+3c = **+5.0x**, under the +6x cap. PASS.
- Shared-catalyst flag raised (compressor commissioning drives Pillar 1 ROCE AND Pillar 3) — permitted, flagged for Role 3. PASS (Master 307, Amendment 4).

### A5. Strategic Premium + single-credit — PASS
ROCE re-rating optionality BARRED (recovery credited in Pillar 1); FTTCP 376 permits the Strategic route only when the ROCE verdict is STAGNANT/FIRING — here RECOVERING, so barred correctly. QCO treated as category-wide tailwind not exclusive licence; institutional backing not Tata/GIC-tier. Strategic = +0x. One-improvement-one-mechanism honoured; no double-crediting of the ROCE recovery. PASS.

### A6. UA multiplier + ordering + sector cap — PASS

| Rule | Application | Verdict |
|---|---|---|
| Three qualifiers all required | Listed ≥12m YES; Gate0≥60 OR EM≥25 → EM 31 YES; FII+DII <3% → 12.1% **FAILS** | PASS (correctly not applied) |
| UA NOT applied when any qualifier fails | ua_applied = false | PASS |
| Ordering min(Raw×1.25, Cap), UA before cap | Not invoked (unqualified); F2 = F = 20.6x | PASS |
| Sector cap correct row for the business (NOT agri) | Cables / Industrial products 25x (Master 355; identical 25x on Recycling/Manufacturing 356). Manifest "Agri processing" 20x is a collector defect superseded by deliberation. Electronics/appliance contract manufacturer → 20x agri would be wrong | PASS |
| Sector cap absolute, applied as min ceiling | min(20.6, 25) = 20.6x; cap not binding | PASS |
| No quality uplift on cap absent UA | Cap not uplifted (uplift requires UA triggered) | PASS |

### A7. Tier / return hurdle — PASS
Amendment 4.3: Tier A default; applies via combined Gate0+EM = TURNAROUND (and independently, Tier B is barred because promoter is CONCERN not TRUSTWORTHY and FLAG-CASH is present). Hurdle 25%. Verdict card states "Tier: A | Hurdle: 25%" on its first line (Amendment 4.3 mandatory). PASS.

### A8. Both tracks + RRM + governing-track selection — PASS

| Rule | Application | Verdict |
|---|---|---|
| Both tracks present, carried through every fair value + verdict card | Track 1 and Track 2 in destination PE, FV matrices, 4C/4D, verdict card | PASS |
| RRM base r | small/micro-cap 14% base; +governance (CONCERN), B-grade, leverage → r=16%, bounded [9,18] | PASS |
| RRM percentage-point reading | 1+(13.5−16)×0.12 = 0.70, floored at 0.70 (Amendment 4.4) | PASS |
| Track 1 = base × RRM | 20.6 × 0.70 = 14.4x | PASS |
| >15% divergence → conservative track governs | (20.5−14.4)/20.5 = 30% → Track 1 governs, sets entry zone (Master 394) | PASS |

### A9. Hurdle Ratio — independent recompute — CONCUR (STOP)

- EPS basis consistency (the LESSONS trap): numerator EPS CAGR is reported-EPS FY26 4.73 → FY30 (base 14.60 / bull 20.76); denominator ratio uses reported-EPS current PE 107.9x and reported-EPS destination PE. CONSISTENT basis throughout. No cash-EPS/reported-EPS mixing. PASS (this is the critical check).
- Bull row credibility gate: grade B (Good) permits use of the bull EPS CAGR (Amendment 2 / Master 406). PASS.
- 4-year adaptation: maker uses HR₄ = (1+CAGR)⁴ × (DestPE/CurrentPE), threshold 1.25⁴ = 2.4414, for the operator-set FY30 horizon. Framework HR is written 3-year (threshold 1.953); the adaptation is operator-authorized (deliberation horizon FY30) and internally consistent (see MINOR-2).

Independent recompute (maker's DestPE mids):
- Track 1 ratio = 14.4/107.9 = 0.1334; Track 2 = 20.5/107.9 = 0.1900
- Base 32.6%: (1.326)⁴ = 3.082 → HR₄ T1 = 0.411, T2 = 0.586
- Bull 44.8%: (1.448)⁴ = 4.396 → HR₄ T1 = 0.587, T2 = 0.835
- All << 2.4414 → **STOP**. Robustness: even under the standard 3-year HR (threshold 1.953), base T1 = 0.31 and bull T2 = 0.58 — still STOP. Under my recomputed Route B DestPE (T1 14.1x / T2 20.1x): bull T2 HR₄ = 0.82 — STOP. Verdict is invariant to the A2 blend deviation and to the 3yr-vs-4yr construct.

**Hurdle Ratio verdict: STOP. CONCUR.**

### A10. Projections, SOM cross-check, unresolved handling — PASS
- SOM cross-check performed: base revenue CAGR 22% < SOM-implied 25.2% → CONSISTENT (conservative). PASS.
- 4D weights: grade B → Bear 25 / Base 50 / Bull 25 (Master 630). PASS.
- Every unresolved input handled by a stated conservative rule, no silent fills: FY26 ROCE → FY25 17.19% trough (basis-consistent) with Gate-0 ~10% downside sensitivity; EV/EBITDA → zero weight; FY30 shares 3.50 Cr flagged as modeling assumption; FY28 ROCE flagged as projected, not fact. All in input_gaps. PASS. (Note: the FY28 projected leg only exists because of the A2 blend choice; under governing Route B it is not needed.)
- Entry price / MoS (Tier A divisor 1.25⁴ = 2.4414 on the 4-year horizon): 210 ÷ 2.4414 = Rs86 (25% entry); 20% below = Rs69 MoS; 210 ÷ 1.30⁴ = Rs74 (30% entry). Arithmetic and rule consistent. PASS.

### Recomputed destination PE
- B11: Track 2 (additive) 20.6x / Track 1 (RRM) 14.4x.
- Verifier C (governing Recon 3.5.1 Route B 60/40 blend): Track 2 20.1x / Track 1 14.1x. Difference ~0.5x, within tolerance; decision unchanged.

---

## PART B — ROLE 2 EXTENSION (B14) vs Master v3.3 Role 2

| Rule | Framework | B14 application | Verdict |
|---|---|---|---|
| AVOID triggers (any one fires) | Master 809 | Gate0 AVOID + Promoter CONCERN + U/D 0.2x (<2x) + Hurdle STOP — all four fire; hardest verdict wins | PASS |
| Promoter CONCERN → AVOID regardless | Master 916 | Cited (line 916) and applied as hard rule | PASS |
| Gate0 <60 → default WATCHLIST unless harder verdict | Master 915 | Core 45 <60; harder AVOID triggers dominate | PASS |
| Position sizing ceilings | Master 813-818 | Large fails (not EXCELLENT/EXEMPLARY/EXPANSION/below-MoS); Medium fails (Gate0 AVOID, Promoter not TRUSTWORTHY); Small is the CAP only, promoter CONCERN cap binds and overrides | PASS |
| Position size is a ceiling for a hypothetical future entry, not a current buy | Master 817 ("Everything else that qualifies as BUY") | Correctly framed: not a buy at CMP; Small only if entry conjunction is one day satisfied at Rs74-86 | PASS |
| Entry conjunction stated in Section 7 verdict box | Master 811 | Stated explicitly (price in zone AND no thesis-broken trigger fired; zone withdrawn if entered because a trigger fired) | PASS |
| Valuation carried unchanged from Role 1 | — | Entry Rs74-86, MoS Rs69, FVs, HR STOP carried verbatim | PASS |
| Verdict card Tier/Hurdle first line | Amendment 4.3 | "Tier: A | Hurdle: 25% | Horizon FY30" present | PASS |

**Role 2 decision recompute:** four independent hard AVOID triggers → **AVOID (on valuation)**; position size Small as a forward ceiling only, promoter CONCERN binding. **CONCUR.**

---

## MINOR NOTES (non-fail, recorded)

- **MINOR-1 (normalized-anchor evidence thinness).** Amendment 4.5 / Recon Route B require the "median ROCE of the last complete pre-depression cycle" from a 📄 historical series. Only ONE pre-depression print exists (FY24 25.66%); FY22-FY23 NOT FOUND. A single year is the thinnest possible "cycle." Strictly, if the pre-depression ROCE series is NOT FOUND the amendment does not apply and the standard blend stands. The maker applied it because the operator explicitly designated the anchor LIVE (deliberation line 65) — an operator override that wins — and capped it conservatively at the single evidenced level while blending it down with the trough. Acceptable under operator authority, but the anchor rests on one data point; flagged for the operator's awareness.
- **MINOR-2 (Hurdle Ratio horizon adaptation).** The framework HR is written as a 3-year construct (threshold 1.953). B11 uses a 4-year variant (threshold 1.25⁴ = 2.4414) for the operator-set FY30 horizon. Operator-authorized and internally consistent; outcome-invariant (STOP under both). Presentational deviation from the written 3-year form.

---

## PHASE 1 STATUS (restated for completeness, not re-audited)
- Gate 0 (B01) and Emerging Moat (B07): 99% adherence, 0 CRITICAL / 0 MAJOR, 1 MINOR. No new phase-3 findings touch these.

## COVERAGE
~38 valuation + Role 2 rules checked across B10/B11/B14. Destination PE, Hurdle Ratio, and the Role 1 and Role 2 decisions were recomputed independently from the framework texts. Numbers-in-sources checks belong to Verifier A and were not duplicated here.

---

```yaml
stage: B12c
company: "VOEPL"
run_date: "2026-07-18"
model: claude-opus-4-8
status: complete
gate0: {rules_checked: 0, fails: []}   # phase-1, not re-audited; restated pass: 99% adherence, 0 CRIT/0 MAJ/1 MINOR
emoat: {rules_checked: 0, fails: []}   # phase-1, not re-audited; restated pass: 99% adherence, 0 CRIT/0 MAJ/1 MINOR
valuation:
  rules_checked: 38
  fails:
    - {severity: "MAJOR", rule: "Pillar 1 ROCE blend weights (Recon v3.5.1 Route B)", detail: "Worksheet selected Route B as governing but applied the RETIRED Amendment 4.5 three-anchor blend (40% norm + 30% FY[Y+2] + 30% current = 21.72%). Governing Route B specifies 60/40 current/anchor = 20.58%. Overstates ROCE ~1.1pp, base 18.4x vs 17.8x, dest PE ~0.5x higher, less-conservative direction. Does not flip Hurdle (STOP) or decision (AVOID)."}
    - {severity: "MINOR", rule: "Amendment 4.5 normalized-anchor evidence base", detail: "Normalized 'cycle median' rests on a single pre-depression year (FY24 25.66%); FY22-FY23 NOT FOUND. Applied under explicit operator LIVE designation and capped conservatively; acceptable but thin."}
    - {severity: "MINOR", rule: "Hurdle Ratio horizon form", detail: "4-year HR variant (threshold 1.25^4=2.4414) used vs written 3-year form (1.953). Operator FY30 horizon authorizes it; outcome-invariant (STOP under both)."}
recomputed_destination_pe: "B11: Track2 20.6x / Track1 14.4x. Verifier C (governing Recon v3.5.1 Route B 60/40 blend, ROCE 20.58%): Track2 20.1x / Track1 14.1x. Difference ~0.5x, within tolerance; decision unchanged."
recomputed_decision: "CONCUR — AVOID (on valuation); Hurdle Ratio STOP (base HR4 0.41, bull HR4 0.59 vs threshold 2.4414; STOP invariant to the blend deviation and to 3yr-vs-4yr construct). Role 2 four hard AVOID triggers concur (Gate0 AVOID, Promoter CONCERN, U/D 0.2x, Hurdle STOP); position size Small forward-ceiling only, promoter CONCERN cap binds."
findings:
  - {severity: "MAJOR", location: "B11 Pillar 1 (Section 1B, lines 53-70)", claimed: "three-anchor blend 40/30/30 = 21.72%, base 18.4x", framework: "Recon v3.5.1 Route B: RECOVERING 40-60% blends 60/40 current/anchor = 20.58%, base 17.8x", note: "Used retired Amendment 4.5 formula after selecting Route B as governing; less-conservative; non-outcome-determinative (STOP holds)"}
  - {severity: "MINOR", location: "B11 Pillar 1 normalized anchor (line 59)", claimed: "normalized 25.66% as pre-depression cycle median", framework: "Amendment 4.5 requires 📄 historical ROCE series; single year only", note: "Operator-designated LIVE; capped conservatively; thin evidence base"}
  - {severity: "MINOR", location: "B11 Hurdle Ratio (lines 141-154)", claimed: "HR4 with threshold 1.25^4=2.4414", framework: "Master 398 HR is 3-year, threshold 1.953", note: "Operator FY30 horizon authorizes; STOP invariant"}
critical_count: 0
major_count: 1
minor_count: 2
acceptance_rate: 95   # ~36 of 38 rules passed clean (1 MAJOR fail + 2 MINOR fails)
coverage_note: "Audited B11 four-pillar (Pillars 1-3, Strategic, UA, sector cap), RRM dual-track, Hurdle Ratio, Tier/hurdle, single-credit, unresolved-input handling; B10 assembled inputs; extended to B14 Role 2 decision rules + position sizing. Destination PE, Hurdle Ratio, Role 1 and Role 2 decisions recomputed independently from framework texts. Gate 0 / Emerging Moat not re-audited (phase 1). Raw numbers-in-sources are Verifier A scope."
```
