# STAGE 12C — FRAMEWORK ADHERENCE AUDIT (VERIFIER C)
## Airfloa Rail Technology Ltd (544516) | Run date 2026-07-15 | Model claude-opus-4-8

**Scope this phase (PHASE 1 ONLY):** Gate 0 (B01) and Emerging Moat (B07) rule-application
audit. The valuation artifacts B11 and B10 do not exist yet (produced in Phase 3), so the
valuation-adherence audit is **DEFERRED TO PHASE 3**. The B12c `valuation` section below is
left at `{rules_checked: 0, fails: []}` and `recomputed_destination_pe` / `recomputed_decision`
are left blank, per task instruction. `acceptance_rate` is computed over the Gate 0 +
Emerging Moat rules checked this phase only.

**What this audit does and does not do:** I audit RULE APPLICATION — were the framework's own
thresholds, formulas, matrices, and edge rules applied as written to the report's *stated*
inputs. I do NOT re-verify the raw numbers against source PDFs (that is Verifier A's domain);
I take the report's stated inputs as given and check that the band/threshold mapping, the
matrix, the deal-breakers, the multipliers, and the completionist recount were executed
correctly.

---

## PART 1 — GATE 0 (B01) COMPLIANCE

### Block A — Return on Capital (formulas: ROCE = EBIT/(TA−CL); ROE = PAT/avg NW)

| Rule | Stated input | Band applied | Framework band | Verdict |
|---|---|---|---|---|
| A1 Median ROCE | (41.30+25.22)/2 = 33.26% | ≥25% → 5 | ≥25%=5 | PASS |
| A2 Min single-yr ROCE | min = 25.22% | ≥15% → 5 | ≥15%=5 | PASS |
| A3 Median ROE | (23.71+22.66)/2 = 23.19% | ≥20% → 5 | ≥20%=5 | PASS |
| A4 ROCE trend | 25.22 vs 41.30 = −16.08pp | decline >5pp → 0 | >5pp=0 | PASS |

- A3 opening-NW fallback correctly applied: FY25 opening net worth unavailable, closing NW
  used and stated — this is the exact fallback the formula prescribes ("if opening net worth
  unavailable for the earliest year, use closing and state so"). PASS.
- Block A = 5+5+5+0 = **15/20**. Matches report. PASS.

### Block B — Cash Generation Quality

| Rule | Stated input | Band applied | Framework band | Verdict |
|---|---|---|---|---|
| B1 Cum CFO/Cum PAT | −6,032.23/6,493.49 = −0.93x | <0.50 → 0 | <0.50=0 | PASS |
| B2 FCF-positive years | 0/2 = 0% | <50 → 0 | <50=0 | PASS |
| B3 Cum FCF/Cum PAT | −8,314.97/6,493.49 = −1.28x | negative → 0 | <0.20 or neg=0 | PASS |
| B4 Change in WC Days | +26.92d increase | increased >15 → 0 | >15=0 | PASS |

- **B4 basis rule audited closely.** Framework: Receivable Days always on Revenue; Inventory
  and Payable Days may use COGS basis "only if COGS is explicitly available; state which basis
  was used." Report used Receivable Days on revenue, Inventory/Payable on COGS (Cost of
  Material Consumed, explicitly disclosed), and stated the basis. This mixed construction is
  exactly what the framework's parenthetical permits. PASS.
- Block B = **0/20**. Matches report. PASS.

### Block C — Growth (CAGR edge rules audited)

| Rule | Stated input | Band applied | Framework band | Verdict |
|---|---|---|---|---|
| C1 Revenue CAGR | 66.12% | ≥20% → 5 | ≥20%=5 | PASS |
| C2 PAT CAGR | 51.85% | ≥20% → 5 | ≥20%=5 | PASS |
| C3 Positive YoY rev yrs | 1/1 = 100% | 100% → 5 | 100%=5 | PASS |
| C4 PAT−Rev CAGR | 51.85−66.12 = −14.27pp | <−8pp → 0 | <−8pp=0 | PASS |

- **CAGR edge rules honoured.** No endpoint is negative or zero (both revenue and PAT positive
  in both years), so no "N/M (negative endpoint)" trigger; no loss-to-profit swing, so no
  synthetic-CAGR suppression required; C4 computed normally because C2 is not N/M. The n=1
  reduction to one-year growth is disclosed as a limited-history caveat, not hidden. PASS.
- Block C = **15/20**. Matches report. PASS.

### Block D — Balance Sheet Strength

| Rule | Stated input | Band applied | Framework band | Verdict |
|---|---|---|---|---|
| D1 Net Debt/EBITDA | 0.85x (net debt, not net cash) | 0-1.0x → 4 | 0-1.0x=4 | PASS |
| D2 Interest Coverage | 7.14x | 5-9.9x → 4 | 5-9.9=4 | PASS |
| D3 Debt/Equity | 0.29x | 0.1-0.5 → 4 | 0.1-0.5=4 | PASS |
| D4 Current Ratio | 2.12x | ≥2.0 → 5 | ≥2.0=5 | PASS |

- Non-financial issuer, so no Bank/NBFC CAR/PCR substitution required. PASS.
- Block D = **17/20**. Matches report. PASS.

### Block E — Shareholder Alignment

| Rule | Stated input | Band applied | Framework band | Verdict |
|---|---|---|---|---|
| E1 Promoter holding | 54.20% | 50-59.9 → 4 | 50-59.9=4 | PASS |
| E2 Promoter change | −20.2pp | decreased >3% → 0 | >3%=0 | PASS |
| E3 Promoter pledge | 0% | 0% → 5 | 0%=5 | PASS |
| E4 Cont. Liab/NW | 0.36% | <5% → 5 | <5%=5 | PASS |

- E1 uses the post-IPO (18-Sep-2025) figure as best-available because no quarterly SHP closer
  to the run date was supplied; flagged as best-available, not silently treated as current. The
  framework asks for "latest quarter"; the report used the latest *available* and disclosed the
  staleness. Compliant handling of a data gap (no estimate inserted). PASS.
- E2: the framework metric is a 3-year change; the company is <12 months listed so a clean
  3-year quarter series is N/A, disclosed. Any decrease of the magnitude shown maps to the
  same band (>3% → 0), so the mechanical score is unambiguous and correctly applied. PASS.
- Block E = **14/20**. Matches report. PASS.

### Block F — Quantitative Moat (12 tests)

| Test | Stated input | Band applied | Framework band | Verdict |
|---|---|---|---|---|
| M1 Pricing Power | EBITDA margin −5.01pp despite growth | else → 0 | declined 2-5pp=1, else 0 | PASS |
| M2 Cost Advantage | PEER DATA NEEDED | 0 | peer-gated → 0 | PASS |
| M3 Capital Efficiency | FAT 6.34x, ROCE 25.22% | FAT>3x & ROCE>20% → 5 | =5 | PASS |
| M4 Customer Stickiness | 0 decline yrs, rec.days +2.29d | zero decline & ±10 → 5 | =5 | PASS |
| M5 Scale & Dominance | PEER DATA NEEDED | 0 | peer-gated → 0 | PASS |
| M6 Technology/R&D | no R&D line disclosed → N/A | 0 | N/A → 0 | PASS |
| M7 Regulatory/License | PEER DATA NEEDED (player count) | 0 | peer-gated → 0 | PASS |
| M8 Distribution | none (B2B direct) | 0 | none=0 | PASS |
| M9 Brand | PEER DATA NEEDED (peer GM) | 0 | peer-gated → 0 | PASS |
| M10 Switching Costs | grew every yr, rec.days +2.29d (≤10) | grew & rose ≤10d → 5 | =5 | PASS |
| M11 Network Effects | <6yr data, selling% unverifiable | conservative → 0 | fewer yrs → conservative, stated | PASS |
| M12 Negative WC/Float | WC days 238/265 (>45) | >45 → 0 | >45=0 | PASS |

- **M1 boundary audited.** Stated margin decline is −5.01pp. The "declined 2-5pp despite
  growth = 1" band requires the decline to be within 2-5pp; 5.01 falls just outside, dropping
  to "else = 0." Band application is correct on the stated input. (The raw margin figures
  25.26%/20.25% are Verifier A's to confirm; on the stated inputs the mapping is correct.)
- **M11 conservative-scoring rule honoured**: the two-window test needs ≥6 years; with 2 years
  the report scored conservatively (0) and stated the reason, exactly as the framework directs.
- **PEER-DATA-NEEDED rule honoured**: M2/M5/M7/M9 each scored 0 and flagged, never guessed —
  matches "score 0 and mark PEER DATA NEEDED (never guess peer figures)."
- Moats present (≥3): M3, M4, M10 = **3** → class MODERATE (2-3 band). PASS.
- Moat score = 5+5+5 = **15/60**. Matches report. PASS.

### Structural rules

| Rule | Report | Framework | Verdict |
|---|---|---|---|
| Core score composition (A+B+C+D) | 47 | 15+0+15+17=47 | PASS |
| Grand total (Core+E+Moat) | 76 | 47+14+15=76 | PASS |
| Moat classification band | MODERATE (3 present, 2-3 band) | 2-3=MODERATE | PASS |
| Data confidence (2 yrs) | <3 → auto AVERAGE | <3 auto AVERAGE | PASS |
| Classification matrix | Core 47 → 40-59 → AVERAGE | Core 40-59=AVERAGE | PASS |
| Deal-breaker #2 (Block B<8) | applied, max GOOD | Block B<8 → max GOOD | PASS |
| Deal-breaker #4 (CFO/PAT<0.50) | applied, max AVERAGE | max AVERAGE | PASS |
| Deal-breaker #9 (history<3yr) | applied, AVERAGE | history<3 → AVERAGE | PASS |
| Deal-breakers NOT triggered | A≥8, ROCE≥10, pledge≤15, ND/EBITDA-IC, rev not declining, no PAT loss | all correctly excluded | PASS |
| "State which years drive deal-breaker" | FY25-FY26 / IPO Sep-2025 named | required | PASS |

- Deal-breaker #1 (Block A<8) correctly assessed as NOT triggered (A=15). The report's
  "max GOOD" cap it lists is from #2 (Block B<8), correctly attributed. PASS.
- Final classification **AVERAGE** is reached by three independent mechanisms (Core band,
  Block B<8 cap, CFO/PAT cap, plus history<3) all landing on the same or lower tier — no
  conflict, and the binding floor (AVERAGE) is correctly selected. PASS.

**GATE 0 RESULT: 38 rules checked, 0 fails. Classification AVERAGE re-derived and CONCUR.**

Minor observation (non-fail, cosmetic): the report labels the <3-year outcome "data confidence
AVERAGE," whereas the framework phrases the <3yr row as "auto AVERAGE" (a classification
effect, not a confidence tier). Net effect is identical and the correct AVERAGE floor is
applied. No score or classification impact.

---

## PART 2 — EMERGING MOAT (B07) COMPLIANCE

### Coverage — all 21 categories addressed or explicitly NO EVIDENCE

Summary table (Section 3) and scorecard (Section 5) each carry all 21 rows: A1-A4, B1-B3,
C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3, R1. Every category is either scored with evidence or
explicitly marked NO EVIDENCE FOUND / negative. No category force-fit. **PASS.**

### Evidence-multiplier application (📄 1.0x / 🎙️ 0.7x / 🔍 0.5x) and raw likelihood×impact matrix

| ID | L×I label | Raw (matrix) | Ev. type | Multiplier | Adjusted | Recompute | Verdict |
|---|---|---|---|---|---|---|---|
| A1 | HM | 3 | 📄 | 1.0x | 3.0 | 3×1.0=3.0 | PASS |
| A4 | ML | 1 | 🎙️ | 0.7x | 0.7 | 1×0.7=0.7 | PASS |
| B2 | HM | 3 | 📄 | 1.0x | 3.0 | 3×1.0=3.0 | PASS* |
| B3 | LL | 1 | 🎙️ | 0.7x | 0.7 | 1×0.7=0.7 | PASS |
| C1 | LL | 1 | 📄 | 1.0x | 1.0 | 1×1.0=1.0 | PASS |
| F1 | LL | 1 | 📄 | 1.0x | 1.0 | 1×1.0=1.0 | PASS |
| H2 | MH | 3 | 📄 | 1.0x | 3.0 | 3×1.0=3.0 | PASS |
| R1 | HM | 3 | 🎙️ | 0.7x | 2.1 | 3×0.7=2.1 | PASS |
| all "none" rows (13) | none | 0 | — | — | 0.0 | 0 | PASS |

- Raw-score matrix mapping (HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, none=0) correctly
  applied on every active row. PASS.
- **Adjusted total = 3.0+0.7+3.0+0.7+1.0+1.0+3.0+2.1 = 14.5.** Matches report. PASS.
- **Evidence-tier consistency check (the "🎙️-only category scoring as if 📄" trap):** every
  🎙️/claim category (A4, B3, R1) received the 0.7x multiplier — none was credited at the 1.0x
  📄 rate. No inflation of claim-grade evidence to documented-grade. PASS.

\*B2 note (MINOR, advisory — not a rule fail): B2's documented evidence (Janatics sole-source
MOU) is sourced via the operator's *secondary* announcements summary, not the primary Reg 30
filing, and the report flags this provenance caveat explicitly. The taxonomy defines 📄 as
"contract signed," and a signed sole-source MOU qualifies, so the 1.0x multiplier is a
defensible application. Stress-test: even if B2 were discounted to 🎙️ 0.7x (2.1 instead of
3.0), the adjusted total falls to 13.6 — still inside the 12-24 MODEST band. **Classification
does not change.** Logged as MINOR for transparency; does not lower the pass count.

### Classification and completionist checks

| Rule | Report | Framework | Verdict |
|---|---|---|---|
| em_score → band | 14.5 → MODEST | 12-24 = MODEST MOAT DEVELOPMENT | PASS |
| Completionist recount performed | "📄 recount: 5 documented items across 5 categories" | recount required before finalising | PASS |
| Base-rate guard (3-6 active) | 4 Strong/Moderate (A1,B2,H2,R1) | realistic 3-6; not ≥12 | PASS |
| active_categories = only Strong/Moderate | A1,B2,H2,R1 (all Moderate) | only Strong/Moderate rows | PASS |
| Optionality register present, watched-not-scored | 10 rows, all 0/🎙️/🔍 items | required | PASS |
| Combined classification (6C/6D) | AVERAGE, using injected B01 block | matrix, HIGH POTENTIAL reasoning if applies | PASS |

- **Completionist guard fully honoured**: the report explicitly recounts 📄 items (5 across
  A1, B2, C1, F1, H2), and only A1/B2/H2 reach Moderate on documented evidence while C1/F1
  stay Weak because their documented data is noisy/offset — this is the exact discipline the
  guard demands, and the active count (4) sits inside the 3-6 base rate, well under the ≥12
  inflation trigger. PASS.
- **Combined 6D reasoning honoured**: the framework requires full reasoning on HIGH POTENTIAL /
  TURNAROUND rows *when they apply*. The report shows why they do NOT apply (forward MODEST is
  one tier below the STRENGTHENING/EXPANSION needed to lift an AVERAGE backward score, and F2
  execution scored a documented negative) and lands on AVERAGE. Correct use of the matrix. PASS.
- em_classification field value "MODEST" is within the allowed set (EXPANSION | STRENGTHENING |
  MODEST | NONE). PASS.

**EMERGING MOAT RESULT: 28 rules checked, 0 fails. em_score 14.5 / MODEST and combined
AVERAGE re-derived and CONCUR.**

---

## PART 3 — VALUATION (B11/B10): DEFERRED TO PHASE 3

B11 and B10 do not exist this phase. The continuous Pillar 1 formula, FTTCP ROCE authority,
single-credit rule, Pillar 2 multiplier/offset rules, Pillar 3 EM/catalyst inputs, UA
Amendment-3 ordering, sector cap, dual-track carry-through, Hurdle Ratio + credibility gate,
4D weights, SOM cross-check, and one-improvement-one-mechanism checks are **NOT audited this
phase** and are carried forward to the Phase 3 Verifier C pass. `valuation` is reported as
`{rules_checked: 0, fails: []}`; `recomputed_destination_pe` and `recomputed_decision` left
blank per instruction.

---

## SUMMARY

- Gate 0 (B01): 38 rules checked, 0 fails. Every block score (A 15, B 0, C 15, D 17, E 14),
  Core 47, moat 15/60, moat class MODERATE, data-confidence auto-AVERAGE, classification
  matrix, all three triggered deal-breakers and the six correctly-excluded ones, and the CAGR
  edge rules were applied as written. **Classification AVERAGE: CONCUR.**
- Emerging Moat (B07): 28 rules checked, 0 fails. All 21 categories addressed, every
  likelihood×impact and evidence-multiplier value recomputed and matches, no claim-grade
  evidence inflated to documented-grade, completionist recount performed and inside base rate,
  combined matrix reasoning correct. **em_score 14.5 / MODEST and combined AVERAGE: CONCUR.**
- One MINOR advisory (B2 secondary-provenance MOU credited at full 📄 1.0x) — defensible under
  the taxonomy, does not change em_score band or any classification.
- Total this phase: 66 rules checked, 0 fails, acceptance_rate 100%.

---

```yaml
stage: B12c
company: "544516"
run_date: "2026-07-15"
model: claude-opus-4-8
status: complete
gate0: {rules_checked: 38, fails: []}
emoat: {rules_checked: 28, fails: []}
valuation: {rules_checked: 0, fails: []}   # DEFERRED to Phase 3: B11/B10 not yet produced
recomputed_destination_pe: ""  # valuation audit deferred to Phase 3
recomputed_decision: ""        # valuation audit deferred to Phase 3
findings:
  - {severity: "MINOR", location: "B07 Section 5 scorecard, category B2", claim: "Janatics sole-source MOU credited at 📄 1.0x multiplier though sourced via operator secondary summary, not primary Reg 30 filing", note: "Defensible under taxonomy (signed MOU = 📄 'contract signed') and provenance flagged in-report; stress-test at 0.7x gives em_score 13.6, still MODEST — no classification change. Advisory, not a rule fail."}
  - {severity: "MINOR", location: "B01 Data Confidence section", claim: "'<3 years' outcome labelled 'data confidence AVERAGE' vs framework phrasing 'auto AVERAGE' (a classification effect)", note: "Cosmetic; identical net effect, correct AVERAGE floor applied via deal-breaker #9 and classification matrix. No score impact."}
critical_count: 0
major_count: 0
minor_count: 2
acceptance_rate: 100    # 66 Gate 0 + Emerging Moat rules checked, 0 fails; valuation deferred to Phase 3
```
