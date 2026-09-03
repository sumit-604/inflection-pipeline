# STAGE 12c — VERIFIER C: FRAMEWORK ADHERENCE (PHASE 1 SCOPE)
Company: MODISONLTD | Run date: 2026-09-03 | Model: claude-opus-4-8
Scope: PHASE 1 ONLY — Gate 0 (B01) + Emerging Moat (B07) compliance.
Valuation-adherence audit (B10/B11) DEFERRED to phase 3 (artifacts do not exist yet).

Rule sources used (the only two loaded, per task):
- prompts/01-gate-0-pipeline.md (Gate 0 scoring rules)
- prompts/07-emerging-moat-pipeline.md (22-category + R1 scan rules)

Artifacts audited:
- runs/modisonltd-2026-09-03/outputs/reports/01-gate0.md (and B01-gate0 YAML inside it)
- runs/modisonltd-2026-09-03/outputs/reports/07-emoat.md
- runs/modisonltd-2026-09-03/outputs/blocks/B07-emoat.yaml

Method: I re-derive every block score, moat score, multiplier, and cap from
the numbers each report STATES, using the thresholds in the two rule files.
I do NOT re-check whether those numbers exist in the source PDFs — source
fidelity is Verifier A's non-overridable gate. I audit rule application only.

====================================================================
## PART 1 — GATE 0 (B01) COMPLIANCE
====================================================================

### Block A — Return on Capital (rule: prompts/01 lines 56-60)

| Line | Stated input | Band applied | Rule band | Re-derived | Verdict |
|---|---|---|---|---|---|
| A1 median ROCE | median{15.35, 17.58, 37.51}=17.58% | 15-19.9=3 | line 56 | 3 | PASS |
| A2 min ROCE | 15.35% | ≥15=5 | line 57 | 5 | PASS |
| A3 median ROE | 11.40% (5th/6th of 10) | <12=0 | line 58 | 0 | PASS |
| A4 ROCE trend | FY26 37.51 ≥ FY24 15.35 | latest≥earliest=5 | line 59 | 5 | PASS |
| Block A sum | | 13 | | 13 | PASS |

A1/A2/A4 rest on a 3-year ROCE window (FY24-FY26); A3 uses 10 years. Rule 6
(line 25) permits "whatever history is available" per metric; ROCE was only
computable for 3 years and this is disclosed per-metric. No window-mismatch
deviation.

### Block B — Cash Generation Quality (rule: lines 63-69)

| Line | Stated input | Band applied | Rule band | Re-derived | Verdict |
|---|---|---|---|---|---|
| B1 cum CFO/PAT | 0.24x | <0.50=0 | line 63 | 0 | PASS |
| B2 FCF+ years | 0/3 = 0% | <50=0 | line 65 | 0 | PASS |
| B3 cum FCF/PAT | -1.10x | neg=0 | line 66 | 0 | PASS |
| B4 ΔWC days | +49.62 | increased>15=0 | line 69 | 0 | PASS |
| Block B sum | | 0 | | 0 | PASS |

### Block C — Growth (rule: lines 72-75)

| Line | Stated input | Band applied | Rule band | Re-derived | Verdict |
|---|---|---|---|---|---|
| C1 rev CAGR | 15.50% | 15-19.9=4 | line 72 | 4 | PASS |
| C2 PAT CAGR | 20.88% | ≥20=5 | line 73 | 5 | PASS |
| C3 +YoY rev prop | 7/8 = 87.5% | 75-99=3 | line 74 | 3 | PASS |
| C4 PAT−Rev CAGR | +5.38pp | ≥+3=5 | line 75 | 5 | PASS |
| Block C sum | | 17 | | 17 | PASS |

CAGR edge rules (lines 45-51): both C1/C2 endpoints positive, no loss year, no
N/M; the FY19 data gap is handled by spanning 10 elapsed fiscal years and by
excluding the FY18→FY20 comparison from C3's YoY count. Compliant.

### Block D — Balance Sheet Strength (rule: lines 78-87)

| Line | Stated input | Band applied | Rule band | Re-derived | Verdict |
|---|---|---|---|---|---|
| D1 ND/EBITDA | 1.46x | 1-2x=3 | line 78 | 3 | PASS |
| D2 interest cov | 11.59x | ≥10=5 | line 81 | 5 | PASS |
| D3 Debt/Equity | 0.64x | 0.5-1.0=3 | line 84 | 3 | PASS |
| D4 current ratio | 1.81 | 1.5-1.99=4 | line 86 | 4 | PASS |
| Block D sum | | 15 | | 15 | PASS |

Not a bank/NBFC; standard bands correctly used (no CAR/PCR substitution).

### Block E — Shareholder Alignment (rule: lines 90-96)

| Line | Stated input | Band applied | Rule band | Re-derived | Verdict |
|---|---|---|---|---|---|
| E1 promoter hold | N/A (not in provided data) | 0 (rule 5) | lines 20-23, 90 | 0 | PASS |
| E2 3yr change | N/A | 0 (rule 5) | line 92 | 0 | PASS |
| E3 pledge | N/A | 0 (rule 5) | line 94 | 0 | PASS |
| E4 contingent/NW | 2.30% | <5=5 | line 95 | 5 | PASS |
| Block E sum | | 5 | | 5 | PASS |

E1-E3 scored 0 under GROUNDED CLAIMS (rule 5, lines 20-23): missing data is
scored 0, never estimated. The "professionally managed = 3 if FII+DII>50%"
alternative (line 90) is correctly NOT invoked — no FII/DII data present.

### Block F — Quantitative Moat (rule: lines 98-139)

| Test | Stated basis | Band applied | Rule | Re-derived | Verdict |
|---|---|---|---|---|---|
| M1 pricing power | margin ±2pp stable + rev CAGR≥10 | 3 | line 103 | 3 | PASS |
| M2 cost adv | PEER DATA NEEDED | 0 | line 99, 106 | 0 | PASS |
| M3 cap efficiency | FAT 7.52x>3 + ROCE 37.51>20 | 5 | line 108 | 5 | PASS |
| M4 stickiness | 1 decline yr, recovered | 3 | line 110 | 3 | PASS |
| M5 scale | PEER DATA NEEDED | 0 | line 113 | 0 | PASS |
| M6 tech/R&D | R&D/rev 0.22% <1% floor | 0 | line 115 | 0 | PASS |
| M7 regulatory | unregulated | 0 | line 118 | 0 | PASS |
| M8 distribution | no quantified reach, B2B | 0 | line 121 | 0 | PASS |
| M9 brand | PEER DATA NEEDED | 0 | line 124 | 0 | PASS |
| M10 switching | 1 decline yr + recv days +19.6 (>10) → else | 0 | line 127 | 0 | PASS |
| M11 network | latest-3yr CAGR>prior + selling% declining | 5 | line 130 | 5 | PASS |
| M12 neg WC | WC days >45 all yrs | 0 | line 135 | 0 | PASS |
| Block F sum | | 16 | | 16 | PASS |

M10 verdict traced carefully: 1 decline year fails the "every year" (=5) and
"all but 1 year AND stable receivables" (=3, receivables rose 19.6 days so not
stable) bands, and does not meet the "2+ decline years" (=1) band, so it falls
to else=0. Correct band logic.

M11 = 5 is a MECHANICAL pass of the line-130 top band (accelerating 3yr CAGR +
declining selling ratio). The maker flagged it as an economic artifact but
scored it per the rule as written. Verifier C audits rule application, not the
economic judgment; the mechanical score is correct and the flag is
appropriate. PASS.

Moats confirmed (score ≥3, line 99): M1, M3, M4, M11 = 4. Classification
"4-5 present = STRONG" (line 138). PASS.

### Totals, confidence, classification, deal-breakers

| Item | Stated | Rule | Re-derived | Verdict |
|---|---|---|---|---|
| Core (A+B+C+D+E) | 50 | sum | 13+0+17+15+5=50 | PASS |
| Grand total | 66 | Core+Moat | 50+16=66 | PASS |
| Data confidence | full/moderate, history_downgrade=false | line 143 | 10 yrs → full tier; no downgrade | PASS |
| Classification matrix | AVERAGE | line 150 "Core 40-59 = AVERAGE" | 50 in 40-59 → AVERAGE | PASS |

Classification matrix note: moat_class STRONG does NOT lift a Core-50 name. The
STRONG/FORTRESS uplift (lines 148-149) only applies at Core ≥80 and Core 60-79;
Core 40-59 is flatly AVERAGE. Correctly applied.

Deal-breaker overrides (lines 154-160):

| # | Rule | Stated evaluation | Re-check | Verdict |
|---|---|---|---|---|
| 1 | Block A<8 → max GOOD | A=13, not fired | correct | PASS |
| 2 | Block B<8 → max GOOD | B=0, FIRED (max GOOD) | correct | PASS |
| 3 | median ROCE<10% → max AVG | 17.58%, not fired | correct | PASS |
| 4 | cum CFO/PAT<0.50 → max AVG | 0.24x, FIRED (max AVG) | correct | PASS |
| 5 | pledge>15% → max AVG | NOT FOUND, not fired | correct (no fire on missing data) | PASS |
| 6 | ND/EBITDA>3x AND IC<3x → AVOID | 1.46x / 11.59x, not fired | correct | PASS |
| 7 | rev decline majority → max AVG | 1/8, not fired | correct | PASS |
| 8 | PAT neg last 3 yrs → max AVG | all positive, not fired | correct | PASS |
| 9 | history<3yr → AVERAGE | 10 yrs, not fired | correct | PASS |

Most-restrictive cap: max AVERAGE (deal-breaker #4). Core-driven classification
(AVERAGE) already sits at that ceiling. FINAL = AVERAGE. Correctly derived.

FLAG-GATE0 entry present (classification ≤ AVERAGE with historical depressor
named) per line 176-178. Compliant.

**GATE 0 RESULT: 55 rules checked, 0 fails. Full compliance.**

====================================================================
## PART 2 — EMERGING MOAT (B07) COMPLIANCE
====================================================================

### Category coverage (rule: prompts/07 line 65, 155; verifier rule 3)

All 23 rows present and addressed (A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2,
G1-G2, H1-H3, I1-I2, R1). Every non-scored row carries "NO EVIDENCE FOUND" or a
documented negative. No force-fit. PASS.

Categories 21 (I1 talent asymmetry) and 22 (I2 cannibalization barrier) present
in both the scan and the scorecard (verifier rule 8, prompts/07 lines 122-153).
PASS.

### Scorecard multiplier arithmetic (rule: prompts/07 lines 171-174)

Formula: raw (HH=4/HM,MH=3/HL,MM,LH=2/ML,LM,LL=1/none=0) × evidence
(📄1.0 / 🎙️0.7 / 🔍0.5).

| Cat | Raw | Tier | Multiplier | Stated adj | Re-derived | Verdict |
|---|---|---|---|---|---|---|
| A1 | 1 (LL) | 🎙️ | 0.7 | 0.7 | 0.7 | PASS |
| A3 | 1 (LM) | 🎙️ | 0.7 | 0.7 | 0.7 | PASS |
| A4 | 1 (LM) | 🎙️ | 0.7 | 0.7 | 0.7 | PASS |
| E2 | 1 (LM) | 🎙️ | 0.7 | 0.7 | 0.7 | PASS |
| H1 | 1 (LM) | 🎙️ | 0.7 | 0.7 | 0.7 | PASS |
| H2 | 2 (MM) | 🎙️ | 0.7 | 1.4 | 1.4 | PASS |
| R1 | 3 (HM) | 📄 | 1.0 | 3.0 | 3.0 | PASS |
| all others | 0 | — | — | 0 | 0 | PASS |

Total = 5×0.7 + 1.4 + 3.0 = 7.9 ≈ 8. Stated em_score 8. PASS.

### Classification band (rule: prompts/07 lines 175-176)

em_score 8 < 12 → NO MEANINGFUL EMERGING MOAT. Stated "NONE". PASS.
(Operator ruling, lines 11-18/177-181: bands ABSOLUTE, no rescale; correctly
respected.)

### Evidence-tier discipline (verifier rule 3: "a 🎙️-only category scoring as if 📄")

Checked every scored row against its stated tier:
- H2 is stated "entirely 🎙️ (no press release, no filed announcement, no
  contract value)" and is scored with the 0.7 🎙️ multiplier, NOT 1.0. Correct —
  the prohibited case (🎙️-only scored as 📄) does NOT occur.
- R1 carries an AR Annexure F p.68 filed anchor (ISRO import-substitution
  recognition disclosed in the audited FY26 AR) and is scored at 1.0 📄. This is
  the report's single 📄 item per its own recount. The 📄 multiplier is
  defensible: the recognition is in a filed document. The raw-score side (HM=3)
  already discounts for the absence of a signed PO or disclosed revenue, so the
  uncertainty is carried in the raw cell, not the tier. No tier deviation.
- A1/A3/A4/E2/H1 all 🎙️ at 0.7. Consistent. PASS.

### Completionist guard (rule: prompts/07 lines 41-46, 155-159)

"📄 recount performed: 1 documented item across 1 category (R1)." Only 2 active
(Strong/Moderate) categories, far under the 12-category red-flag threshold. The
recount is present and honest. PASS.

### I1 / I2 two-leg discipline (verifier rule 8; prompts/07 lines 122-153)

- I1 = 0. Part (a) has no named inventor / ex-major staff concentration / above-
  norm remuneration disclosure; part (b) not addressed. Scored 0 correctly —
  the (b) leg lacks the required 📄 source, so any score >0 would be a fail;
  the report scored 0. PASS.
- I2 = 0. Honest answer "nothing must be destroyed" for the HV and MCPL claims →
  execution lead, not configuration. No named, specific, 📄-backed sacrifice, so
  0 is required. Scored 0. PASS.
- I1/I2 contribution stated separately ("0 of 8") per the operator ruling
  (lines 179-181). PASS.

### Combined assessment (rule: prompts/07 lines 201-210; verifier "combined-assessment rule")

6C combined table present; 6D combined classification AVERAGE with reasoning.
AVERAGE backward + NONE forward is not the AVERAGE-plus-EXPANSION/STRENGTHENING
transition setup, so no elevation above backward AVERAGE. Correctly applied. PASS.

**EMERGING MOAT RESULT: 17 rules checked, 0 fails. Full compliance.**

====================================================================
## PART 3 — VALUATION (B10/B11) — DEFERRED
====================================================================

Not run in phase 1. B10 and B11 do not exist yet. The valuation framework docs
(Master v3.6 Role 1, Section 1B layer set, FTTCP v2.1) were deliberately NOT
loaded this pass. Status: valuation audit deferred to phase 3.

====================================================================
## SUMMARY
====================================================================

Both in-scope artifacts apply their frameworks as written. Every Gate 0 block
score, moat score, classification cap, and deal-breaker re-derives exactly from
the stated inputs. Every Emerging Moat multiplier, the em_score total, the band,
the completionist recount, the I1/I2 two-leg discipline, and the combined
assessment are correct. No CRITICAL, MAJOR, or MINOR framework-adherence
deviation found. Recomputed destination PE and recomputed decision: not
applicable in phase-1 scope (no valuation audited).

```yaml
stage: B12c
company: "MODISONLTD"
run_date: "2026-09-03"
model: claude-opus-4-8
status: complete
scope: phase-1 (Gate 0 + Emerging Moat only)
gate0: {rules_checked: 55, fails: []}
emoat: {rules_checked: 17, fails: []}
valuation: {rules_checked: 0, fails: [], status: "valuation audit deferred to phase 3"}
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: [], status: "out of scope in phase 1 (stage 13 not audited)"}
recomputed_destination_pe: ""
recomputed_decision: ""
findings: []
critical_count: 0
major_count: 0
minor_count: 0
acceptance_rate: 100            # rules passed (72) / rules checked (72)
```
