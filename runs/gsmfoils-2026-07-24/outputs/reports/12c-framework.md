# STAGE 12C — VERIFIER C: FRAMEWORK ADHERENCE (GSMFOILS)
Run date: 2026-07-24 | Model: claude-opus-4-8 | Pipeline mode
Scope: PHASE 1 — Gate 0 (B01) and Emerging Moat (B07) only. Valuation audit
(B10/B11) is a PHASE 3 deliverable and is NOT run here (valuation: pending-phase-3).

Method: I re-derived every block/category score from the inputs each report
states, using the thresholds written in prompts/01-gate-0-pipeline.md and
prompts/07-emerging-moat-pipeline.md. I audit rule application, not raw-number
existence (Verifier A owns whether a figure appears in a source PDF at its
anchor) and not company quality. A correct application is not a finding.

Framework docs read: prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md,
frameworks/Master_Project_Prompt_v3.3.md, frameworks/Section_1B_v3.3_Amendments.md,
frameworks/Section_1B_v3_5_1_Reconciliation.md, frameworks/FTTCP_v1.2_Consolidated.md.
For phase-1 scope the two stage rubrics are the binding authorities; the Section 1B
and FTTCP docs govern the phase-3 valuation audit and are noted but not scored here.

---

## PART 1 — GATE 0 (B01) COMPLIANCE

### Block A — Return on Capital (stated ROCE 21.77/47.77/bounded24.67-39.37; ROE 12.42/45.66/37.54)

| Rule | Stated input | Threshold | Maker score | Re-derived | Verdict |
|---|---|---|---|---|---|
| A1 Median ROCE | median(21.77,47.77)=34.77 (FY26 excluded) | ≥25=5 | 5 | 5 on 2-yr basis; 4 if FY26-low-bound included | PASS* (minor, see F-1) |
| A2 Min single-yr ROCE | 21.77 (FY24) | ≥15=5 | 5 | 5 | PASS |
| A3 Median ROE | median(12.42,45.66,37.54)=37.54 | ≥20=5 | 5 | 5 | PASS |
| A4 ROCE trend latest vs earliest | FY26≥24.67 vs FY24 21.77 | latest≥earliest=5 | 5 | 5 (robust across full bound) | PASS |
| Block A total | | | 20 | 20 | PASS |

### Block B — Cash Generation Quality (CFO FY24 −13.72, FY26 −36.79; FY25 N/A)

| Rule | Stated input | Threshold | Maker | Re-derived | Verdict |
|---|---|---|---|---|---|
| B1 ΣCFO/ΣPAT | −50.51/21.21=−2.38 | <0.50=0 | 0 | −2.38 → 0 | PASS |
| B2 FCF-positive proportion | 0 of 2 | <50%=0 | 0 | 0 | PASS |
| B3 ΣFCF/ΣPAT | −54.91/21.21=−2.59 | <0.20 or neg=0 | 0 | −2.59 → 0 | PASS |
| B4 ΔWC days | FY26 ≥161 vs FY24 146.15 | increased >15=0 | 0 | 0 (bounded, payables floor argued) | PASS |
| Block B total | | | 0 | 0 | PASS |

FY25 CFO gap handled correctly: marked N/A, computed B1/B3 on the 2 anchored years,
OCR cross-check explicitly quarantined from scoring (operating rule 5 honoured).

### Block C — Growth

| Rule | Stated input | Threshold | Maker | Re-derived | Verdict |
|---|---|---|---|---|---|
| C1 Rev CAGR 2yr | (258.15/40.83)^.5−1=151.5% | ≥20=5 | 5 | 5 | PASS |
| C2 PAT CAGR 2yr | (19.84/1.37)^.5−1=280.5% | ≥20=5 | 5 | 5 | PASS |
| C3 Positive YoY rev yrs | 2/2=100% | 100%=5 | 5 | 5 | PASS |
| C4 PAT−Rev CAGR | +129.09pp | ≥+3pp=5 | 5 | 5 | PASS |
| Block C total | | | 20 | 20 | PASS |

CAGR edge rules honoured: both PAT endpoints positive (1.37, 19.84) → no N/M, no
loss-to-profit swing, no synthetic CAGR. Correct.

### Block D — Balance Sheet Strength (all FY26; EBITDA 29.78)

| Rule | Stated input | Threshold | Maker | Re-derived | Verdict |
|---|---|---|---|---|---|
| D1 NetDebt/EBITDA | 43.89/29.78=1.47x | 1-2x=3 | 3 | 3 | PASS |
| D2 Interest coverage | 29.32/3.00=9.77x | 5-9.9x=4 | 4 | 4 | PASS |
| D3 Debt/Equity | 44.39/74.46=0.596 | 0.5-1.0=3 | 3 (self-corrected from 4) | 3 | PASS |
| D4 Current ratio | bounded 1.65-2.01, low bound taken | 1.5-1.99=4 | 4 | 4 | PASS |
| Block D total | | | 14 | 14 | PASS |

D3 shows a self-corrected transcription (line wrote 4, note corrects to 3); the final
score and YAML use 3. No error propagated — not a finding.

### Block E — Shareholder Alignment

| Rule | Stated input | Threshold | Maker | Re-derived | Verdict |
|---|---|---|---|---|---|
| E1 Promoter latest | 54.38% | 50-59.9=4 | 4 | 4 | PASS |
| E2 Promoter Δ | Sep24 73.14 → Jun26 54.38 = −18.76pp | decreased >3%=0 | 0 | 0 | PASS |
| E3 Pledge | N/A | N/A→0 (rule 5) | 0 | 0 | PASS |
| E4 ContLiab/NW | N/A | N/A→0 (rule 5) | 0 | 0 | PASS |
| Block E total | | | 4 | 4 | PASS |

E2 uses the full ~21-month available window rather than a strict 3-year window
(only post-IPO quarters exist). Consistent with operating rule 6 (use whatever
history exists). E3/E4 scored 0 not assumed-nil — correct application of rule 5.

### Block F — Quantitative Moat (12 tests)

| Test | Threshold path | Maker | Re-derived | Verdict |
|---|---|---|---|---|
| M1 Pricing power | margin +4.85pp (≥2) AND rev CAGR ≥10 → 5 | 5 | 5 | PASS |
| M2 Cost advantage | peer data absent → 0 | 0 | 0 | PASS |
| M3 Capital efficiency | FAT 50.7x (>3) AND ROCE >20 all scenarios → 5 | 5 | 5 | PASS |
| M4 Customer stickiness | 0 decline yrs but receivables unstable → 5-band fails → 3-band | 3 | 3 | PASS |
| M5 Scale & dominance | peer data absent → 0 | 0 | 0 | PASS |
| M6 Technology/R&D | no R&D line → 0 | 0 | 0 | PASS |
| M7 Regulatory/license | peer/player-count data absent → 0 | 0 | 0 | PASS |
| M8 Distribution | no quantified reach → 0 | 0 | 0 | PASS |
| M9 Brand | GM proxy computed, no peer median → 0 | 0 | 0 | PASS |
| M10 Switching costs | receivables rose 68.7d (>10), 0 decline yrs → else=0 | 0 | 0 | PASS |
| M11 Network effects | <6yr, scored conservatively per rubric → 0 | 0 | 0 | PASS |
| M12 Negative WC | WC >45 every year → 0 | 0 | 0 | PASS |
| Moat total | | 13 | 13 | PASS |

Moat count ≥3: M1,M3,M4 = 3 present → MODERATE (2-3=MODERATE). Correct.
M9 GM-proxy computed-but-not-scored (no peer median) and M11 conservative-0 both
match the rubric's explicit instructions for those tests.

### Aggregation, classification, overrides

| Rule | Maker | Re-derived | Verdict |
|---|---|---|---|
| Core score sum | 20+0+20+14+4=58 | 58 | PASS |
| Moat score | 13/60 | 13 | PASS |
| Grand total | 71/160 | 71 | PASS |
| Base matrix | Core 58 → AVERAGE (40-59) | AVERAGE | PASS |
| Deal-breakers fired | #2 Block B<8→max GOOD; #4 CFO/PAT<0.50→max AVERAGE | both correct; #4 binding | PASS |
| Deal-breakers not fired | #1,#3,#5,#6,#7,#8,#9 all correctly non-triggered | confirmed | PASS |
| History confidence tier | 3 full FY → "3-4 LIMITED, downgrade one tier" | correct band (not <3 auto-AVERAGE) | PASS |
| history_downgrade bool | true | consistent with narrative and with AVOID result | PASS |
| Final classification | AVERAGE −1 tier → AVOID | AVOID | PASS |

Deal-breaker #9 (history <3 → AVERAGE) correctly does NOT fire: exactly 3 full FYs
places the company in the "3-4 LIMITED" downgrade band, which is more punitive
(AVOID) than the <3 AVERAGE floor. Rule sequencing (matrix → deal-breaker cap →
LIMITED downgrade) is applied as written. `history_downgrade=true` is internally
consistent with its own narrative — no boolean/narrative contradiction.

**Gate 0 verdict: 38 of 39 rules PASS. One MINOR (F-1). Classification AVOID stands.**

---

## PART 2 — EMERGING MOAT (B07) COMPLIANCE

| Rule | Requirement | Finding | Verdict |
|---|---|---|---|
| Category coverage | all 21 (A1-H3 + R1) addressed or NO EVIDENCE | all 21 present in Section 3 + scorecard | PASS |
| Evidence taxonomy | 📄/🎙️/🔍 on every item | applied throughout | PASS |
| Completionist recount | explicit 📄 recount line | "3 documented items across 2 categories (H2,C2) of 21" | PASS |
| C2 raw score | Medium×Medium=MM=2 | 2 | PASS |
| E2 raw score | Low×Medium=LM=1 | 1 | PASS |
| F1 raw score | Low×Low=LL=1 | 1 | PASS |
| H2 raw score | Medium×Medium=MM=2 | 2 | PASS |
| C2 multiplier | 🎙️ 0.7 → 1.4 | 1.4 | PASS |
| E2 multiplier | 🎙️ 0.7 → 0.7 | 0.7 | PASS |
| F1 multiplier | 🎙️ 0.7 → 0.7 | 0.7 | PASS |
| H2 multiplier | 📄 1.0 → 2.0 | 2.0 | PASS |
| em_score arithmetic | 1.4+0.7+0.7+2.0 | 4.8 | PASS |
| em_classification | 4.8 <12 → NONE | NONE | PASS |
| No tier inflation | 🎙️-only categories not scored as 📄 | H2 (📄) is the only 1.0x; all thin items at 0.7x | PASS |
| active_categories | Strong/Moderate rows only | H2 only (C2/E2/F1 are Weak, excluded) | PASS |
| capex_embedded_growth 2C | 5.65×50.7/258.15≈111% | 111, flagged in-line as distorted for asset-light model | PASS |
| evidence_mix vs recount | documented:3 matches recount | consistent | PASS |
| Combined 6C uses injected B01 | core 58, moat 13, AVOID, grand 71 all carried | matches injected block | PASS |
| Combined 6D matrix | AVOID backward + NONE forward → AVOID | outcome correct | PASS* (minor, see F-2) |

Scorecard evidence tiers are internally consistent: H2 alone carries the 1.0x
�-documented multiplier (production commenced June 2026), and every thin category
(C2, E2, F1) is held at the 0.7x 🎙️ rate. No 🎙️-only category is credited as 📄.
The likelihood×impact → raw → multiplier chain reproduces 4.8 exactly.

**Emerging Moat verdict: 17 of 18 rules PASS. One MINOR (F-2). em_score 4.8 / NONE and combined AVOID stand.**

---

## PART 3 — VALUATION (B10/B11) COMPLIANCE

NOT RUN IN PHASE 1. B10/B11 do not exist yet; produced in phase 3. This section
is deferred (valuation: pending-phase-3). The Section 1B v3.3 / v3.5.1 and FTTCP
v1.2 rule set (continuous Pillar 1, FTTCP ROCE authority, single-credit route,
Pillar 2 offset rules, Amendment 3 UA order, dual-track carry, Hurdle Ratio,
4D weights, SOM cross-check) will be audited then.

---

## FINDINGS

- **F-1 (MINOR, B01 Block A / A1).** A1 median ROCE is computed on the two clean
  years only (median 34.77% → 5), excluding the bounded FY26 value. Because FY26
  is the middle of the three-year set, a strict 3-year median equals the FY26
  figure (bounded 24.67-39.37%); at its conservative low bound this scores 4, not 5.
  The exclusion is defensible (FY26 ROCE is genuinely only bounded, since the FY26
  current-liability split did not OCR), but it is inconsistent with the conservative
  low-bound treatment the same report applies at D4. No decision impact: A1=4 would
  make Block A 19/20 and Core 57, still AVERAGE band → AVOID after the LIMITED
  downgrade. Presentational/methodology inconsistency, within tolerance.

- **F-2 (MINOR, B07 combined_reasoning).** The 6D combined reasoning states the
  AVOID backward floor is "driven by hard mechanical failures (cash conversion,
  data gaps)." Strictly, Gate 0's substantive deal-breaker (#4) caps at AVERAGE;
  the step from AVERAGE to AVOID comes from the mechanical LIMITED-history downgrade
  that B01 explicitly instructs downstream stages NOT to treat as an independent
  quality signal. Leaning on "already AVOID" therefore borders on re-using that
  mechanical downgrade as a quality input. Outcome unaffected: the forward em_score
  is 4.8 (NONE), far below the EXPANSION threshold (40) and even the MODEST floor
  (12), so no HIGH POTENTIAL / TURNAROUND transition classification is reachable
  whether the backward floor is read as AVERAGE or AVOID; combined = negative /
  non-transition either way. The 6D rule (use the injected Gate 0 classification,
  which is AVOID) is itself followed. MINOR.

No CRITICAL and no MAJOR findings. No recomputation flips a block total, the Gate 0
classification (AVOID), the em_score (4.8 / NONE), or the combined assessment (AVOID).

---

```yaml
stage: B12c
company: "GSMFOILS"
run_date: "2026-07-24"
model: claude-opus-4-8
status: complete
gate0:
  rules_checked: 39
  fails:
    - {rule: "A1 median ROCE (2-yr median 34.77% vs 3-yr low-bound 24.67%)", severity: "minor", recomputed: "A1=4 not 5; Block A 19 not 20; Core 57; classification unchanged AVOID"}
emoat:
  rules_checked: 18
  fails:
    - {rule: "6D combined_reasoning attributes AVOID floor to mechanical cash/data failures", severity: "minor", recomputed: "outcome unchanged; forward em_score 4.8 (NONE) precludes any transition classification regardless of AVERAGE-vs-AVOID backward read"}
valuation: pending-phase-3
recomputed_destination_pe: ""
recomputed_decision: ""
findings:
  - {severity: "minor", location: "B01 Block A / A1", note: "median ROCE on 2 clean years excludes bounded FY26; conservative low-bound inclusion gives A1=4 not 5; inconsistent with D4 low-bound treatment; no decision impact (still AVERAGE->AVOID)"}
  - {severity: "minor", location: "B07 Section 6D combined_reasoning", note: "AVOID floor attributed to mechanical cash/data failures when substantive cap is AVERAGE and AVOID comes from the LIMITED-history downgrade B01 says not to re-use as a quality signal; outcome unaffected, forward em_score 4.8 (NONE) blocks any transition class"}
critical_count: 0
major_count: 0
minor_count: 2
acceptance_rate: 96             # 55 of 57 phase-1 rules passed (gate0 + emoat)
```
