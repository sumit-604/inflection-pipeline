# STAGE 12c — VERIFIER C: FRAMEWORK ADHERENCE AUDIT (PHASE 1 SCOPE)
Company: N R Agarwal Industries Ltd (NRAIL) | Run date: 2026-07-22 | Model: claude-opus-4-8

**Scope this run:** Gate 0 (B01) compliance + Emerging Moat (B07) compliance ONLY.
Valuation-adherence audit (B10 assembly / B11 valuation) is DEFERRED to Phase 3 — those
artifacts do not exist yet. The B12c `valuation` section is emitted as `pending-phase-3`.
`framework_adherence` (acceptance_rate) is computed from the Gate 0 + EM portion only.

I audit rule APPLICATION, not company quality and not raw source-number fidelity (Verifier A
owns whether a number exists at its anchor). Where I say a score is "correct," I mean the
stated inputs were placed in the correct rubric band, not that the input number was verified
against the PDF.

Run context noted and weighed throughout: this was a **NO-CONCALL** run with **no NRAIL
screener extract** (Gate 0 built directly from the FY2024-25 Annual Report + the Q4/FY26
audited results filing; peer JKPAPER CSVs explicitly excluded). The framework-appropriateness
of that degraded handling is assessed in each section.

---

## PART 1 — GATE 0 (B01) COMPLIANCE

Authority: `prompts/01-gate-0-pipeline.md` (160-point scorecard: Blocks A-E = 100 core,
Block F = 60 moat; formula definitions; CAGR edge rules; classification matrix; 9
deal-breakers). Every band re-derived from the report's own stated inputs.

### Block A — Return on Capital (rubric lines 55-60)

| Rule | Stated input | Band applied | Recheck | Verdict |
|---|---|---|---|---|
| A1 Median ROCE | 11.06% (median of 5.55/8.04/11.06/17.83/18.13) | 10-14.9 = 1 | median of 5 = 11.06 → band 1 | PASS |
| A2 Min ROCE | 5.55% | <8 = 0 | correct | PASS |
| A3 Median ROE | 10.56% (median of 15.62/17.98/2.30/5.50) | <12 = 0 | median of 4 = (5.50+15.62)/2 = 10.56 → 0 | PASS |
| A4 ROCE trend | FY26 8.04 vs FY22 17.83 = -9.79pp | >5pp decline = 0 | correct | PASS |

Block A = 1/20. **Correct.** A3 was computed independently (PAT ÷ avg net worth) rather than
using the company's disclosed "Return on Equity" — the report correctly identified that the
disclosed figure is PAT ÷ paid-up share capital (AR Note 57), not the rubric's ROE definition
(line 34). Using the rubric formula over a mislabeled disclosure is framework-correct.

### Block B — Cash Generation Quality (rubric lines 62-69)

3-year full-statement window (FY24-26) used because full cash-flow detail exists only for
those years. Rubric line 24 ("use whatever history is available; minimum 3 years") sanctions
this.

| Rule | Stated input | Band applied | Recheck | Verdict |
|---|---|---|---|---|
| B1 ΣCFO/ΣPAT | 406.20/186.81 = 2.174 | ≥1.00 = 5 | correct | PASS |
| B2 FCF-positive proportion | 1 of 3 = 33% | <50 = 0 | correct | PASS |
| B3 ΣFCF/ΣPAT | -541.42/186.81 = -2.898 | negative = 0 | correct | PASS |
| B4 ΔWC days | FY26 43.11 vs FY24 54.62 = -11.51d | decreased >5d = 5 | correct; revenue-basis WC days stated per formula rule (line 35-39) | PASS |

Block B = 10/20. **Correct.**

### Block C — Growth (rubric lines 71-75)

| Rule | Stated input | Band applied | Recheck | Verdict |
|---|---|---|---|---|
| C1 Revenue CAGR | 7.34% (2145.45/1616.51)^0.25-1 | 5-9.9 = 1 | 7.34% → 1 | PASS |
| C2 PAT CAGR | -8.00% (both endpoints positive) | negative = 0 | endpoints positive → compute, not N/M; -8.0% → 0 | PASS |
| C3 Positive YoY | 3 of 4 = 75% | 75-99 = 3 | correct | PASS |
| C4 PAT CAGR − Rev CAGR | -8.00-7.34 = -15.34pp | <-8pp = 0 | correct | PASS |

Block C = 4/20. **Correct.** CAGR edge rules (lines 44-52) honored: both C2 endpoints are
positive so a real CAGR is computed (not N/M); no loss-to-profit swing exists, and none was
falsely asserted; C4 used the arithmetic difference (PAT CAGR is negative, not N/M, so the
"score 0 on N/M" special case does not apply — the report reached 0 via the band, correctly).

### Block D — Balance Sheet Strength (rubric lines 77-87)

| Rule | Stated input | Band applied | Recheck | Verdict |
|---|---|---|---|---|
| D1 ND/EBITDA (FY26) | 3.96x | >3x = 0 | correct; not a bank/NBFC, standard formula right | PASS |
| D2 IC EBIT/Interest (FY26) | 1.93x (pipeline formula) | 1.5-2.9 = 1 | correct | PASS |
| D3 D/E (FY26) | 0.97x (total borrowings/equity) | 0.5-1.0 = 3 | correct | PASS |
| D4 Current Ratio (FY26) | 1.155x | 1.0-1.19 = 1 | correct | PASS |

Block D = 5/20. **Correct.** D2 and D3 correctly applied the pipeline's FIXED formula
definitions (rubric line 28: "do not substitute alternatives") over the company's differently
based disclosures (D/E on long-term debt only; ICR on an unreconcilable denominator). The
report flagged both deviations transparently. **This is framework-correct, exactly as the
rubric demands** — the task's specific question ("did it use the pipeline's own formula
definitions where the company's disclosed ratios differed, and is that framework-correct?")
is answered YES for D2/D3 and for A3 (ROE). Note the one asymmetry, which is also correct:
ROCE (A1/A4) USED the company-disclosed figures for FY22-25 and computed only FY26, because
rubric line 29 uniquely instructs "use the source's own ROCE ... compute only when absent."
So ROCE-use-disclosed and ROE/D-E/ICR-use-pipeline-formula are BOTH rubric-mandated, not an
inconsistency. (Minor caveat below on the resulting basis-mix.)

### Block E — Shareholder Alignment (rubric lines 89-96)

| Rule | Stated input | Band applied | Recheck | Verdict |
|---|---|---|---|---|
| E1 Promoter holding | 73.96% (FY25 snapshot, latest available) | ≥60 = 5 | correct | PASS |
| E2 3yr change | NOT FOUND | missing → 0 | rubric line 22-23 (missing → 0) honored | PASS |
| E3 Pledge | NOT FOUND (qualitative AR Note 18 language only) | missing → 0 | correct — did NOT numerically score the qualitative pledge; flagged instead | PASS |
| E4 ContLiab/NW | 49.81/774.59 = 6.43% (FY25) | 5-15 = 3 | correct | PASS |

Block E = 8/20 as computed in the body of the report. **Line-item scoring correct.** BUT see
Finding GATE0-1: this 8 is then dropped from the Core Score and the Grand Total, and from the
YAML `blocks` map.

### Block F — Quantitative Moat (rubric lines 98-139)

| Rule | Stated input | Band applied | Verdict |
|---|---|---|---|
| M1 Pricing Power | margin -0.31pp (stable), rev CAGR 7.34% <10% | neither growth tier met → 0 | PASS |
| M2 Cost Advantage | PEER DATA NEEDED | 0 (peer excluded) | PASS |
| M3 Capital Efficiency | FAT 1.81x, ROCE 8.04% <12% | fails ROCE>12% floor → 0 | PASS |
| M4 Customer Stickiness | 1 decline yr, fully recovered | "max 1 decline, recovered" = 3 | PASS |
| M5 Scale & Dominance | PEER DATA NEEDED | 0 (peer excluded) | PASS |
| M6 Technology/R&D | R&D nil | 0 | PASS |
| M7 Regulatory/License | unregulated segment | 0 | PASS |
| M8 Distribution | mentioned unquantified | 1 | PASS |
| M9 Brand | PEER DATA NEEDED | 0 (peer excluded) | PASS |
| M10 Switching Costs | growth all-but-1yr but receivables not stable; only 1 decline yr | both qualifying tiers fail → 0 | PASS |
| M11 Network Effects | <6yr, selling exp % rising | conservative → 0 | PASS |
| M12 Negative WC/Float | WC days latest 43.11 | 15-45 = 1 | PASS |

Moat total = 5/60. Moats present (≥3) = 1 (M4). Classification 1 = **THIN** (rubric line 139).
**Correct.** M4 at score 3 is right: the "max 1 decline year, fully recovered" tier (line 111)
does not require receivable stability — that condition sits only on the =5 tier. M2/M5/M9 were
correctly scored 0 / PEER DATA NEEDED with no guessed peer figures (line 100-101).

### Classification, deal-breakers, confidence

- **Classification matrix (lines 147-150):** Core <40 → AVOID. **Correct outcome.** (Robust to
  Finding GATE0-1: whether core = 20 or 28, both are <40 → AVOID.)
- **Deal-breakers (lines 152-160):** DB1 (Block A 1<8) correctly triggered→max GOOD, superseded
  by AVOID. DB6 (ND/EBITDA >3x AND IC <3x: FY26 3.96x/1.93x) correctly triggered→AVOID, with
  the driving years stated (FY25 also breaches), as line 155 requires. DB3 (median ROCE 11.06%
  ≥10, not triggered), DB4, DB7, DB8, DB9 correctly NOT triggered. DB5 (pledge >15%) correctly
  left UNRESOLVED / not scored as a numeric trigger because the % is NOT FOUND — this is the
  right call: the AR Note 18 qualitative language is flagged, not force-converted into a band.
  **PASS.**
- **Data confidence (line 145):** 5-year headline series → "5-6 lower" tier, cycle flag applied.
  **PASS** (see MINOR on history_downgrade).
- **No qualitative judgment, flags propagate, no halt:** the AVOID is a mechanical classification,
  not a STOP; consistent with CLAUDE.md ("no STOP verdict"). **PASS.**

### Gate 0 findings

**GATE0-1 (MAJOR) — Block E excluded from Core Score, Grand Total, and the YAML `blocks` map.**
- Location: `01-gate0.md` line 214 (`CORE SCORE = A+B+C+D = 20/80`), line 324
  (`GRAND TOTAL = Core(20)+Moat(5) = 25`), YAML `blocks: {A:1,B:10,C:4,D:5}` (line 433 / block
  file line 11). Block E (8/20) is computed in the body but then omitted from every aggregate.
- Rule basis: the emitted-schema template (rubric line 181) is `blocks: {A:0,B:0,C:0,D:0,E:0}`
  — E is an enumerated block. The scorecard is 160 points = A-E (100 core) + F (60 moat), so
  Core = A+B+C+D+E = 100 and Grand Total = 160-max. The matrix bands (≥80 / 60-79 / 40-59 /
  <40) are coherent only on a 100-point core; on an 80-point core the "≥80" band would require
  a perfect score, which is not a plausible rubric design. On the strongest reading, E belongs
  in core.
- Recompute (E in core): **Core = 28** (1+10+4+5+8), **Grand Total = 33** (28+5). The report
  states core 20 / grand 25 — an understatement of the grand total by 8 points (~32%).
- **Decision impact: NONE.** Core 28 is still <40 → AVOID; deal-breaker 6 independently mandates
  AVOID. Because the classification is unchanged either way, this is MAJOR (wrong computation,
  decision survives), not CRITICAL. The YAML `blocks` map dropping the `E` key is an
  unambiguous schema deviation regardless of the core-arithmetic reading.
- Caveat acknowledged: the rubric never states the Core Score arithmetic in prose, so a
  minority reading (core = A-D, E as a non-summed overlay feeding only deal-breaker 5) is not
  strictly impossible. I flag rather than fail-hard on that ambiguity, but the missing `E` key
  in the emitted `blocks{}` is a clear template departure and the grand_total is at minimum
  materially understated on the more defensible reading.

**GATE0-2 (MINOR) — `history_downgrade: true` set for a 5-year history.**
- Location: `01-gate0.md` line 356 / YAML line 441.
- Rubric line 145: 5-6 years = "lower, flag 'may not have seen full cycle'" (flag only, no tier
  downgrade); the one-tier downgrade attaches to the 3-4 year "LIMITED" tier. The report named
  the "5-6 lower" tier yet set `history_downgrade: true`. It is defensible (full balance-sheet /
  cash-flow detail is only 3 years — effectively the LIMITED tier — and the deal-breaker blocks
  B and D rest on that narrower window), so this is a mild internal tension, not a clear error.
  **Immaterial:** classification is already at the AVOID floor, so a downgrade changes nothing.

**MINOR (noted, not counted as a separate fail) — ROCE basis-mix.** A1/A4 blend company-disclosed
ROCE (FY22-25) with a pipeline-formula-computed FY26; the A4 trend and A1 median therefore span
two possibly different ROCE bases. This is rubric-sanctioned (line 29) and was not flagged the
way ROE/D-E/ICR were, but it does not move any band (A1 still 1, A4 still 0). Recorded for
transparency only.

### No-concall / no-screener handling (Gate 0)

Framework-appropriate. Gate 0 is a quantitative screen; it needs financial statements, which the
AR + Q4/FY26 results supply. Peer-dependent moat tests (M2/M5/M9) were correctly scored
0 / PEER DATA NEEDED rather than guessed (rubric line 100-101). The absence of a screener CSV
did not force any estimate — all inputs are AR/results-anchored, and gaps (E2, E3 %) resolved to
NOT FOUND → 0 per the missing-data rule, never filled. Degradation handled correctly.

---

## PART 2 — EMERGING MOAT (B07) COMPLIANCE

Authority: `prompts/07-emerging-moat-pipeline.md` (21-row scan A1-R1; evidence taxonomy;
likelihood×impact matrix; evidence-quality multipliers; completionist guard; optionality
discipline; combined Gate0+EM matrix; explicit NOT-FTTCP boundary).

### Category completeness and taxonomy

- **All 21 categories addressed** (A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3, R1),
  each with an evidence table or an explicit "NO EVIDENCE FOUND" (rubric line 5). **PASS.**
- **Evidence taxonomy tags (📄/🎙️/🔍)** applied to every evidence item, with source anchors
  (AR page/note, Inv. Pres. slide) (rubric lines 18-24). **PASS.**
- **Skepticism / no force-fit** (rubric lines 26-29): A1 explicitly refused to force-fit the
  company's scale/cost claim into "rare capability"; management claims consistently down-weighted.
  **PASS.**

### Scorecard arithmetic (rubric lines 126-132)

| ID | L×I | Raw | Type | Mult | Adj | Recheck |
|---|---|---|---|---|---|---|
| A3 | HM | 3 | 📄 | 1.0 | 3.0 | PASS |
| B1 | HM | 3 | 📄 | 1.0 | 3.0 | PASS |
| E1 | MM | 2 | 📄 | 1.0 | 2.0 | PASS |
| F2 | HH | 4 | 📄 | 1.0 | 4.0 | PASS |
| H1 | MH | 3 | 🎙️ | 0.7 | 2.1 | PASS |
| H3 | HL | 2 | 📄 | 1.0 | 2.0 | PASS |
| R1 | HM | 3 | 📄 | 1.0 | 3.0 | see EMOAT-1 |

- Raw scores match the matrix (HH=4, HM/MH=3, HL/MM/LH=2) exactly. **PASS.**
- Evidence multipliers (📄 1.0 / 🎙️ 0.7 / 🔍 0.5) applied correctly — notably H1 is 🎙️-only
  and was multiplied by 0.7, NOT scored as if 📄 (the exact trap Verifier C rubric line 158
  names). **PASS.**
- Total = 3+3+2+4+2.1+2+3 = 19.1 ≈ 19. **Arithmetic correct.**
- Classification: 19.1 → band 12-24 = **MODEST MOAT DEVELOPMENT** (rubric line 132). **PASS.**

### Completionist guard (rubric lines 30-35, 114)

- Recount line present: "9 documented items across 6 categories scored Moderate+ on 📄
  (A3, B1, E1, F2, H3, R1); one further (H1) on 🎙️ alone." **PASS.**
- 7 of 21 categories active — above the 3-6 base rate but below the 12-category "suspect"
  threshold; guard therefore not tripped, and the report proactively noted that most breadth
  traces to a single capital event (the 900 TPD plant + captive power), so it is not
  double-weighted. Correct, honest application. **PASS.**

### Section 2C embedded-growth arithmetic (rubric line 49-51)

₹150cr capex-under-execution × 1.459x historical FAT = ₹218.8cr = 13.2% of FY24-25 revenue
(₹1,659.03cr); `capex_embedded_growth_pct: 13`. Arithmetic shown and correct; tagged 🔍 with an
upper-bound caveat. **PASS.**

### Optionality register discipline (rubric lines 134-147)

Register holds only forward advantages that scored 0 or rest on 🎙️/🔍 (Dahej Unit VI, second
greenfield unit, FBB platform, CFTRI lock-in, customer-concentration trend, war-chest reversal,
WC normalization, H2 partnership), each with converting-📄 evidence, first-appearance venue, and
a conversion window. Critically, the operator-relayed Unit VI Dahej project (~₹1,500cr) was
**registered and NOT scored** — exactly the "watched, never scored" rule (line 145-147) and the
skepticism mandate. **PASS.**

### EM/FTTCP separation (rubric lines 3-6; CLAUDE.md NEVER-conflate)

The report is titled and framed throughout as the Emerging Moat 20-category scan; there is no
FTTCP language, no FTTCP scoring, no cross-contamination. **PASS.**

### Combined Gate0+EM assessment (rubric lines 152-161)

- 6C table built from the injected B01 block (core 20, moat 5, grand 25, THIN, AVOID) plus this
  stage's EM 19/MODEST. **PASS.**
- 6D combined classification: backward AVOID (below the GOOD/AVERAGE band the transition-alpha
  setup requires) + forward MODEST (below the STRENGTHENING/EXPANSION bands) → not HIGH POTENTIAL
  / not TURNAROUND → **AVOID**. Reasoning correctly maps to the standard matrix; both dimensions
  are genuinely weak, not merely under-covered, and the report says so. **PASS.**

### EM findings

**EMOAT-1 (MINOR) — R1 impact tier arguably generous.**
- Location: `07-emoat.md` line 204 (scorecard R1 = HM=3, 📄, 3.0) vs the report's own Section 4C
  (lines 170-174): the Aatmanirbhar Gujarat subsidy is **shared-eligibility** (not exclusive to
  NRAIL), ~₹9.1cr combined, and of **undisclosed duration** (recurrence unknown). On a ~₹1,659cr
  revenue base a Low-impact read (HL = 2) is at least as defensible as Moderate (HM = 3).
- Effect: an HL=2 read trims the EM total to ~18.1 — **still MODEST** (12-24), no classification
  change, no combined-verdict change. Likelihood×impact is inherently a judgment call within the
  analyst's latitude, so this is imprecision, not a rule violation. MINOR.
- (Related observation, not a separate fail: F2 carries the maximum HH=4 with full 📄 weight even
  though the report itself flags an unverified FY25-26 cash-conversion deterioration that it says
  "should reduce how much weight F2 carries." The underlying execution evidence — on-time
  commissioning, fast ramp, funding delivered to plan — is genuinely 📄, so HH is within latitude;
  the caveat was disclosed, not buried. No fail.)

### No-concall handling (Emerging Moat)

Framework-appropriate. F2 (execution moat) normally cross-references the injected concall
promise-delivery record (rubric line 96); with no concalls, the report substituted AR
capex-completion evidence across the Directors'-Report timeline, disclosed the substitution, and
attached a weight caveat. The FY25-26 CFO/FCF figures (which sit outside the AR's coverage
period) were pulled from the injected B01 block and explicitly marked unverified-in-this-stage —
used as a qualifier, never as silently-filled scored evidence. The stale (May-2022) investor
presentation was used only for pre-expansion baseline, weighted low. All three degradations were
surfaced in `input_gaps`. Handled correctly.

---

## SUMMARY

- **Gate 0:** 40 rules checked, 38 pass. Every block/moat band and the classification/
  deal-breaker/CAGR/formula logic re-derives correctly. One MAJOR (Block E dropped from Core /
  Grand Total / YAML `blocks{}` — grand total understated 25 vs 33, but AVOID unchanged) and one
  MINOR (history_downgrade tier tension, immaterial).
- **Emerging Moat:** 18 rules checked, 17 pass. Scan completeness, taxonomy, matrix arithmetic
  (19.1≈19 → MODEST), completionist recount, optionality discipline, EM/FTTCP separation, and
  the combined AVOID verdict are all correct. One MINOR (R1 impact tier generous, immaterial).
- **Decision concurrence:** Gate 0 AVOID and combined AVOID both stand. No CRITICAL. No
  decision-changing misapplication in scope.
- **Valuation (B10/B11):** DEFERRED to Phase 3 — not audited, artifacts do not exist.

framework_adherence (Gate0 + EM, rules passed ÷ rules checked) = 55 / 58 = **95%**.

```yaml
stage: B12c
company: "NRAIL"
run_date: "2026-07-22"
model: claude-opus-4-8
status: complete
phase_scope: "phase-1: gate0 + emoat only; valuation deferred to phase-3"
gate0:
  rules_checked: 40
  fails:
    - {id: "GATE0-1", severity: "MAJOR", rule: "Core Score / Grand Total must aggregate all core blocks A-E (160-pt scorecard: A-E=100 core, F=60 moat); YAML blocks{} template includes E", location: "01-gate0.md L214/L324; B01 YAML blocks{} L433 (E key omitted)", recompute: "Core 28 (not 20), Grand Total 33 (not 25) if E in core", decision_impact: "none — core still <40 and deal-breaker 6 both mandate AVOID"}
    - {id: "GATE0-2", severity: "MINOR", rule: "5-6yr history = lower-confidence flag only, not the 3-4yr one-tier downgrade", location: "01-gate0.md L356 / B01 YAML L441 history_downgrade:true", decision_impact: "none — already at AVOID floor; defensible given 3yr full-statement window"}
emoat:
  rules_checked: 18
  fails:
    - {id: "EMOAT-1", severity: "MINOR", rule: "likelihood x impact tier should match stated evidence; R1 impact scored Moderate (HM=3) though subsidy is shared-eligibility, ~Rs9.1cr, duration-undisclosed", location: "07-emoat.md L204 vs Section 4C L170-174", recompute: "HL=2 -> EM ~18.1, still MODEST (12-24); no classification change", decision_impact: "none"}
valuation: pending-phase-3
recomputed_destination_pe: ""
recomputed_decision: ""            # concur — Gate 0 AVOID and combined AVOID both stand
findings:
  - {severity: "MAJOR", location: "01-gate0.md L214/L324; B01 YAML blocks{} L433", note: "Block E (Shareholder Alignment, 8/20) computed in body but dropped from Core Score, Grand Total, and the emitted blocks{} map. Rubric template enumerates E as a block; 160-pt structure implies core=A+B+C+D+E=100. Recompute: core 28, grand total 33 (report says 20/25). Decision UNCHANGED — AVOID via core<40 and deal-breaker 6."}
  - {severity: "MINOR", location: "01-gate0.md L356 / B01 YAML L441", note: "history_downgrade:true set on a 5-year history that the report itself placed in the 5-6yr 'lower, flag-only' confidence tier (the one-tier downgrade attaches to 3-4yr LIMITED). Defensible (3yr full-statement window) and immaterial at the AVOID floor."}
  - {severity: "MINOR", location: "07-emoat.md L204 (scorecard R1) vs L170-174 (Section 4C)", note: "R1 regulatory-tailwind impact scored Moderate (HM=3, 3.0) despite the report's own finding that the Gujarat subsidy is shared-eligibility, ~Rs9.1cr, and of undisclosed duration; a Low impact (HL=2) is at least as defensible. EM total would fall to ~18, still MODEST. Judgment within latitude; no verdict change."}
  - {severity: "MINOR", location: "01-gate0.md Block A", note: "OBSERVATION (not counted): A1/A4 blend company-disclosed ROCE (FY22-25) with pipeline-computed FY26 per rubric L29; the resulting basis-mix was not flagged the way ROE/D-E/ICR were, but moves no band. Framework-sanctioned."}
critical_count: 0
major_count: 1
minor_count: 3
acceptance_rate: 95            # rules passed 55 / rules checked 58, Gate0 + EM only
```
