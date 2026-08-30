# VERIFIER C — FRAMEWORK ADHERENCE AUDIT (PHASE 1)
Company: KRONOX (Kronox Lab Sciences Ltd) | Run date: 2026-08-30
Model: claude-opus-4-8 | Scope: PHASE-1 (Gate 0 B01 + Emerging Moat B07)
Valuation audit (B10/B11): NOT RUN — deferred to phase 3.

Rule sources read: prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md.
Artifacts audited: outputs/reports/01-gate0.md + outputs/blocks/B01-gate0.yaml;
outputs/reports/07-emoat.md + outputs/blocks/B07-emoat.yaml.

Degraded-condition context applied to every check: NO-CONCALL MODE, single
AR (FY26), HIGH prospectus gap. Adherence is judged against how each prompt
tells the stage to handle missing data (rule 5 grounded-claims, rule 6
whatever-history-available, F2 NO-CONCALL substitution), not against a
full-corpus ideal.

I audit rule application only. Numbers-in-source is Verifier A's non-
overridable gate; I re-derive scores FROM the stated inputs, I do not re-open
whether a stated input exists in the PDF.

═══════════════════════════════════════════════════════════════════
## PART 1 — GATE 0 (B01) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### Block A — Return on Capital (re-derived from stated inputs)
ROCE% stated: 49.46 / 43.15 / 38.03 / 32.22 (FY23-FY26).
ROE% stated (computed): 35.65 / 38.83 / 32.55 / 26.83.

| Item | Threshold applied | Re-derived | Stated | Verdict |
|---|---|---|---|---|
| A1 median ROCE | median=40.59 → ≥25 →5 | 5 | 5 | PASS |
| A2 min ROCE | 32.22 → ≥15 →5 | 5 | 5 | PASS |
| A3 median ROE | median=34.10 → ≥20 →5 | 5 | 5 | PASS |
| A4 ROCE trend | 32.22 vs 49.46 = -17.24pp → >5pp →0 | 0 | 0 | PASS |

ROE formula spot-check (PAT ÷ avg net worth): FY26 2766.0/((9010.50+11612.71)/2)
=26.83 PASS; FY25 32.55 PASS; FY24 38.82 PASS; FY23 closing-only 35.65 PASS
(opening-N/A rule honoured). **Block A = 15/20. PASS.**

### Block B — Cash Generation Quality
Cum CFO 9,166.90; cum PAT 9,062.90.

| Item | Threshold applied | Re-derived | Stated | Verdict |
|---|---|---|---|---|
| B1 cumCFO/cumPAT | 1.011 → ≥1.00 →5 | 5 | 5 | PASS |
| B2 FCF-pos years | 2/2 on FCF-computable window →100% →5 | 5 (window) | 5 | PASS-with-note (MINOR) |
| B3 cumFCF/cumPAT | 4817.79/5311.7 = 0.907 →≥0.60 →5 | 5 (window) | 5 | PASS-with-note (MINOR) |
| B4 ΔWC days | 83 vs 74 = +9 → 5-15 →1 | 1 | 1 | PASS |

**B2/B3 MINOR finding.** FY23/FY24 capex is absent, so the maker scored B2/B3
on the FY25-FY26 window and flagged it explicitly. This is defensible under
Gate-0 rule 6 (use whatever history is available; scoring adapted). A strict
rule-5 literal read (missing data point → N/A/0) would treat FY23/FY24 FCF as
untestable: B2 = 2 of 4 confirmed positive = 50% → band 50-74 → 2; B3 with a
2-year numerator over a 4-year PAT denominator = 4817.79/9062.90 = 0.531 →
band 0.40-0.59 → 3. Worst-case Block B = 13 (not 16), core = 72. Still core
60-79 → GOOD → AVERAGE after the history downgrade. **No decision change.**
The window-matched approach is the more apples-to-apples read and was
transparently flagged; logged MINOR, not a decision-relevant fail.

**Block B = 16/20. PASS (with MINOR window note).**

### Block C — Growth
Revenue 9557.7 / 8986.2 / 10018.4 / 10122.0; PAT 1595.5 / 2155.7 / 2545.7 / 2766.0.

| Item | Threshold applied | Re-derived | Stated | Verdict |
|---|---|---|---|---|
| C1 rev CAGR | (10122.0/9557.7)^(1/3)-1 = 1.93% → <5 →0 | 0 | 0 | PASS |
| C2 PAT CAGR | (2766.0/1595.5)^(1/3)-1 = 20.14% → ≥20 →5 | 5 | 5 | PASS |
| C3 pos YoY | 2/3 = 66.7% → 50-74 →1 | 1 | 1 | PASS |
| C4 PAT-Rev CAGR | 18.2pp → ≥+3 →5 | 5 | 5 | PASS |

CAGR edge rules: both endpoints positive, no loss-to-profit swing, C2 not N/M
→ edge rules correctly not triggered. PASS. **Block C = 11/20. PASS.**

### Block D — Balance Sheet
| Item | Threshold applied | Re-derived | Stated | Verdict |
|---|---|---|---|---|
| D1 ND/EBITDA | net cash →5 | 5 | 5 | PASS |
| D2 int coverage | 3741.7/11.4 = 328x → ≥10 →5 | 5 | 5 | PASS |
| D3 D/E | 160.7/11612.7 = 0.014 → <0.1 →5 | 5 | 5 | PASS |
| D4 current ratio | 7.60 → ≥2.0 →5 | 5 | 5 | PASS |

**Block D = 20/20. PASS.**

### Block E — Shareholder Alignment
| Item | Threshold applied | Re-derived | Stated | Verdict |
|---|---|---|---|---|
| E1 promoter % | 74.18 → ≥60 →5 | 5 | 5 | PASS |
| E2 3yr Δ | scored ±1% →3 on 1-yr window | see finding | 3 | MINOR FAIL |
| E3 pledge | NOT FOUND → rule-5 →0 | 0 | 0 | PASS |
| E4 contLiab/NW | 0% → <5 →5 | 5 | 5 | PASS |

**E2 MINOR finding.** The metric is a 3-year promoter-holding change. The 3-year
figure is not in the corpus and the window spans the Jun-2024 IPO OFS, which by
definition moved promoter %. The maker substituted the only available window
(FY25→FY26, unchanged) and scored ±1% → 3, flagged transparently. This is
internally inconsistent with the stricter rule-5 treatment given to E3 (pledge
NOT FOUND → 0). A strict rule-5 read of E2 gives N/A → 0 (or, on the known IPO
OFS direction, a decrease → 0-1). Worst-case Block E = 10 (not 13), core = 72.
Still core 60-79 → GOOD → AVERAGE. **No decision change.** Logged MINOR.

**Block E = 13/20 as scored. PASS-with-MINOR.**

### Block F — Quantitative Moat (re-derived, all 12 tests)
| Test | Rule check | Verdict |
|---|---|---|
| M1 pricing power | margin +11.14pp but rev CAGR 1.9% <10% → both top tiers need ≥10% → 0 | PASS |
| M2 cost adv | PEER DATA NEEDED → 0 | PASS |
| M3 cap efficiency | FAT 3.52x>3 AND ROCE 32.22>20 → 5 | PASS |
| M4 stickiness | 1 decline yr recovered → 3 | PASS |
| M5 scale | PEER DATA NEEDED → 0 | PASS |
| M6 tech/R&D | R&D% not quantified → 0 | PASS |
| M7 regulatory | unregulated → 0 | PASS |
| M8 distribution | none quantified, B2B → 0 | PASS |
| M9 brand | PEER DATA NEEDED → 0 | PASS |
| M10 switching | growth all-but-1yr, receiv days stable → 3 | PASS |
| M11 network | <6yr, weak CAGR, conservative → 0 | PASS |
| M12 negWC | CCC 74/96/77/83 all >45 → 0 | PASS |

Moat = 5+3+3 = 11. Moats present ≥3: M3, M4, M10 = 3. Class: 2-3 present →
MODERATE. **PASS.**

### Classification, downgrade, deal-breakers
- Core = 15+16+11+20+13 = **75**. Matches. PASS.
- Matrix: core 60-79 + MODERATE (not STRONG/FORTRESS) → GOOD. PASS.
- Confidence: 4 years → 3-4 LIMITED → downgrade one tier → GOOD → AVERAGE
  (ladder EXCELLENT>GOOD+>GOOD>AVERAGE>AVOID; one tier down = AVERAGE). PASS.
  history_downgrade=true. PASS.
- Grand total 75+11 = 86. PASS.
- Deal-breakers 1-9 each re-checked: none triggered. #5 pledge unknown
  (correctly not triggered on absence); #9 history 4yr (≥3, correctly the
  LIMITED downgrade path, not the <3 auto-AVERAGE path). deal_breakers=[]. PASS.
- FLAG-GATE0: classification AVERAGE with depressors identified → flag
  required and present. PASS.

**Gate 0 verdict: decision (AVERAGE, core 75, grand 86) fully re-derived and
concurred. Two MINOR degraded-condition scoring choices (E2, B2/B3), both
transparently flagged, neither changes the decision.**

═══════════════════════════════════════════════════════════════════
## PART 2 — EMERGING MOAT (B07) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### Category coverage (rule 3: all 23 addressed or explicit NO EVIDENCE)
Summary table and scorecard both carry all 23 rows: A1-A4, B1-B3, C1-C2,
D1-D2, E1-E2, F1-F2, G1-G2, H1-H3, I1-I2, R1. Every row is either scored or
marked NO EVIDENCE FOUND / NOT FOUND (data gap) / negative finding. **PASS.**

### Scored-row re-derivation (raw L×I map + evidence multiplier)
Map: HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1. Mult: 📄1.0 / 🎙️0.7 / 🔍0.5.

| Cat | Raw stated | Map check | Mult | Adjusted re-derived | Stated | Verdict |
|---|---|---|---|---|---|---|
| B1 | 1 (LM) | LM=1 ✓ | 🎙️0.7 | 0.7 | 0.7 | PASS |
| B2 | 3 (HM) | HM=3 ✓ | 📄1.0 | 3.0 | 3.0 | PASS |
| E2 | 3 (MH) | MH=3 ✓ | 🔍0.5 | 1.5 | 1.5 | PASS |
| G1 | 4 (HH) | HH=4 ✓ | 📄1.0 | 4.0 | 4.0 | PASS |
| R1 | 1 (LM) | LM=1 ✓ | 📄1.0 | 1.0 | 1.0 | PASS |

Total = 0.7+3.0+1.5+4.0+1.0 = **10.2**. Matches em_score. PASS.
Classification: 10.2 < 12 → NO MEANINGFUL EMERGING MOAT / "NONE". PASS.

### Evidence-tier consistency (rule 3: no 🎙️-only row scoring as 📄)
- B1 is 🎙️-only → correctly 0.7x. PASS.
- E2 has 📄 export-trend data but the category claim (China+1 causation) is
  🔍; the maker applied the conservative 0.5x, consistent with the skepticism
  rule. PASS.
- All 📄-multiplied rows (B2, G1, R1) rest on documented items (certificate
  stack; debt-equity/DSCR/FD growth; approvals obtained + export incentives).
  PASS. No tier inflation found.

### Completionist recount (rule 3)
Performed and stated: "9 documented items across 8 categories; only B2 and G1
clear the Moderate/Strong bar" — 2 active categories, inside the 3-6 base rate,
far below the 12-category over-crediting red flag. Guard correctly applied.
PASS.

### I1 / I2 (rule 8, Categories 21 and 22)
- I1 TALENT ASYMMETRY present, scored 0. Part (a) not established (no named
  inventor, no ex-major concentration, no above-norm technical-staff pay);
  the above-0 two-leg / 📄-(b) requirement is therefore not engaged. PASS.
- I2 CANNIBALIZATION BARRIER present, scored 0 by design ("nothing must be
  destroyed" across every candidate moat). Above-0 requires a specific named
  sacrifice, correctly absent. PASS.
- I1/I2 contribution stated separately (0), per the 20-Aug-2026 ruling. PASS.

### F2 NO-CONCALL substitution (degraded-condition handling)
Prompt 07 defines F2 on capex-on-time / ramp / guidance-delivery, cross-
referencing the concall promise-delivery record. In NO-CONCALL mode the maker
substituted the AR capex/CWIP timeline + B05 promise-delivery, returned a
documented NEGATIVE finding (Dahej clearances obtained, construction not
started; CWIP Rs 87.6 lakh; commitments NIL), and scored 0. This is the
prompt-sanctioned degraded path applied correctly. PASS.

### 2C capex-embedded growth arithmetic
FAT = 10122.0/2873.3 = 3.523x; CWIP 87.6 × 3.523 = 308.6 lakh; ÷ 10122.0 =
3.05%. capex_embedded_growth_pct = 3.05. Arithmetic re-derived, matches. PASS.

### Other block-field checks
- active_categories = only Strong/Moderate rows (G1 Strong, B2 Moderate);
  Weak rows (B1, E2) and negative findings (F2, G2) correctly excluded. PASS.
- catalysts_12m: 3 rows, each anchored. PASS.
- optionality_register: forward advantages that scored 0 or rest on 🎙️/🔍
  (incl. A3, E2, integration, customer data, talent). Consistent with the
  register rule. PASS.
- combined_assessment: AVERAGE backward + NONE forward → AVERAGE; matrix
  applied, transition-setup reasoning given for why nothing upgrades. PASS.

**Emerging Moat verdict: fully compliant. em_score 10.2 and classification
NONE re-derived exactly; no fails.**

═══════════════════════════════════════════════════════════════════
## SUMMARY
═══════════════════════════════════════════════════════════════════
- Gate 0: core 75, grand 86, AVERAGE — re-derived and concurred. Two MINOR
  degraded-condition scoring choices (E2 1-year-window; B2/B3 FCF window),
  both flagged, neither flips the decision.
- Emerging Moat: em_score 10.2, NONE — re-derived and concurred, no fails.
- No CRITICAL, no MAJOR. Two MINOR. Decision and destination classification
  unchanged; no recompute needed.
- Valuation audit (B10/B11): pending phase 3.

Acceptance rate (rules passed ÷ rules checked): 67/69 = 97%. Above the 60%
REWORK floor. No REWORK triggered.

```yaml
stage: B12c
company: "KRONOX"
run_date: "2026-08-30"
model: claude-opus-4-8
status: complete
gate0:
  rules_checked: 38
  fails:
    - {severity: MINOR, rule: "E2 promoter-holding 3yr change", finding: "3-year window not in corpus (spans Jun-2024 IPO OFS); scored on FY25->FY26 1-year window as +/-1% -> 3. Inconsistent with the strict rule-5 treatment given to E3 (NOT FOUND -> 0). Defensible under rule 6 and flagged. Strict read -> 0-1; worst-case core 72, still 60-79 GOOD -> AVERAGE.", decision_impact: none}
    - {severity: MINOR, rule: "B2/B3 FCF window", finding: "FY23/FY24 capex absent; B2/B3 scored on the FY25-FY26 window. Defensible under rule 6 and flagged. Strict literal read: B2 2 of 4 -> 2, B3 2yr-FCF/4yr-PAT 0.531 -> 3; worst-case Block B 13, core 72, still GOOD -> AVERAGE.", decision_impact: none}
emoat:
  rules_checked: 31
  fails: []
valuation:
  status: pending-phase-3
  rules_checked: 0
  fails: []
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: []}  # out of phase-1 scope (stage 13 not audited here)
recomputed_destination_pe: ""
recomputed_decision: ""
findings:
  - {severity: MINOR, location: "B01 Block E, E2", note: "1-year-window substitution for a 3-year metric; inconsistent with E3 rule-5 treatment; no decision change"}
  - {severity: MINOR, location: "B01 Block B, B2/B3", note: "2-year FCF window vs strict rule-5 read; defensible under rule 6, flagged; no decision change"}
critical_count: 0
major_count: 0
minor_count: 2
acceptance_rate: 97
```
