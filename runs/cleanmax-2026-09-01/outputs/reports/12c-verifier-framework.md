# VERIFIER C — FRAMEWORK ADHERENCE (PHASE 1 SCOPE)
Company: CLEANMAX | Run date: 2026-09-01 | Model: claude-opus-4-8
Scope: Gate 0 (B01) + Emerging Moat (B07) only. Valuation audit (B10/B11) DEFERRED to phase 3.
Method: rule application re-derived from the stated inputs and thresholds. Raw-number
existence is Verifier A's authority, not audited here. Judgment on company quality is out
of scope; only "was the framework applied as written."

Inputs read:
- prompts/01-gate-0-pipeline.md (rule source)
- prompts/07-emerging-moat-pipeline.md (rule source)
- outputs/reports/01-gate0.md (B01, audited)
- outputs/reports/07-emoat.md (B07, audited)

---

## PART 1 — GATE 0 (B01) COMPLIANCE TABLE

### Block A — Return on Capital (threshold re-derivation)
| Rule | Stated input | Threshold band | Report score | Re-derived | Verdict |
|---|---|---|---|---|---|
| A1 Median ROCE | 5.83% (median of 3.71/6.54/6.60/5.13) | <10% = 0 | 0 | median = 5.835% <10 → 0 | PASS |
| A2 Min single-yr ROCE | 3.71% (FY23) | <8% = 0 | 0 | 3.71 <8 → 0 | PASS |
| A3 Median ROE | 1.94% (median of 6-yr series) | <12% = 0 | 0 | median(-5.28,-2.04,1.27,2.61,4.63,50.28)=1.94 → 0 | PASS |
| A4 ROCE trend | FY26 5.13% vs earliest-available FY23 3.71% | latest ≥ earliest = 5 | 5 | 5.13 ≥ 3.71 → 5 | PASS |
| Block A total | | | 5 | 0+0+0+5 = 5 | PASS |

### Block B — Cash Generation Quality
| Rule | Stated input | Band | Report | Re-derived | Verdict |
|---|---|---|---|---|---|
| B1 ΣCFO/ΣPAT | 4,149.37 / 25.71 = 161.4x | ≥1.00 = 5 | 5 | ≥1.00 → 5 (mechanical; distortion flagged, score still per rule) | PASS |
| B2 FCF-positive yrs | 0 of 4 | <50% = 0 | 0 | 0% → 0 | PASS |
| B3 ΣFCF/ΣPAT | -9,227.30 / 25.71 negative | <0.20/neg = 0 | 0 | negative → 0 | PASS |
| B4 ΔWC days | FY26 -273.35 vs FY23 -342.89 = +69.5 increase | increase >15 = 0 | 0 | +69.5 >15 → 0 | PASS |
| Block B total | | | 5 | 5+0+0+0 = 5 | PASS |

### Block C — Growth
| Rule | Stated input | Band | Report | Re-derived | Verdict |
|---|---|---|---|---|---|
| C1 Revenue CAGR | (1912.87/621.27)^(1/5)-1 = 25.2% | ≥20% = 5 | 5 | 25.22% → 5 | PASS |
| C2 PAT CAGR | endpoints FY21 25.32 / FY26 94.13 (both +); in-window loss yrs FY23/FY24 | see note | 0 (N/M) | see INTERPRETATION note below | PASS (with note) |
| C3 Positive YoY rev yrs | 5 of 5 | 100% = 5 | 5 | 100% → 5 | PASS |
| C4 PAT CAGR − Rev CAGR | PAT CAGR N/M | C4=0 when PAT CAGR N/M | 0 | consistent with report's C2 treatment | PASS (with note) |
| Block C total | | | 10 | 5+0+5+0 = 10 | PASS |

INTERPRETATION NOTE (C2/C4): The CAGR edge rule fires N/M when "either endpoint is
negative or zero." Both C2 endpoints are positive (25.32 → 94.13), so a strict reading of
the first bullet would COMPUTE the CAGR (~30.0%, ≥20% → C2=5), and C4 = 30.0 − 25.2 =
+4.8pp ≥+3pp → C4=5. The report instead invoked the second bullet ("if PAT swung from loss
to profit across the window ... do not attempt a synthetic CAGR"), because the series
crossed into losses twice inside the window (FY22→FY23 profit-to-loss, FY24→FY25
loss-to-profit). That reading is defensible on the rule's intent and honored the C4=0
dependency correctly. IMPACT IF SCORED THE OTHER WAY: Block C 10 → 20, Core 24 → 34, still
<40 → AVOID on the matrix, and deal-breaker #6 fires independently. Decision unchanged.
Logged MINOR, decision-neutral.

### Block D — Balance Sheet Strength (latest FY26)
| Rule | Stated input | Band | Report | Re-derived | Verdict |
|---|---|---|---|---|---|
| D1 ND/EBITDA | 10,396.36 / 1,294.56 = 8.03x | >3x = 0 | 0 | 8.03 >3 → 0 | PASS |
| D2 Interest Coverage | 920.90 / 785.92 = 1.17x | <1.5x = 0 | 0 | 1.17 <1.5 → 0 | PASS |
| D3 Debt/Equity | 12,684.32 / 4,638.27 = 2.73x | >1.5 = 0 | 0 | 2.73 >1.5 → 0 | PASS |
| D4 Current ratio | 3,405.12 / 5,129.21 = 0.66x | <1.0 = 0 | 0 | 0.66 <1.0 → 0 | PASS |
| Block D total | | | 0 | 0 | PASS |

### Block E — Shareholder Alignment
| Rule | Stated input | Band | Report | Re-derived | Verdict |
|---|---|---|---|---|---|
| E1 Promoter holding | 49.48% | 40-49.9 = 3 | 3 | 49.48 → 3 | PASS |
| E2 3-yr holding change | NOT FOUND (IPO dilution not a like-for-like) | n/a | 0 | scored 0, not estimated → correct per never-estimate | PASS |
| E3 Promoter pledge | 20.02% of promoter holding | >15% = 0 | 0 | 20.02 >15 → 0 | PASS |
| E4 Contingent liab/NW | 1,232.86 / 4,638.27 = 26.58% | 15-30 = 1 | 1 | 26.58 → 1 | PASS |
| Block E total | | | 4 | 3+0+0+1 = 4 | PASS |

### Block F — Quantitative Moat Scoring (M1-M12)
| Rule | Stated input | Report | Re-derived | Verdict |
|---|---|---|---|---|
| M1 Pricing power | OPM +20.6pp AND rev CAGR 25.2% ≥10 | 5 | expand ≥2pp AND CAGR ≥10 → 5 | PASS |
| M2 Cost advantage | no peer margin data | 0 (PEER DATA NEEDED) | correct per rule | PASS |
| M3 Capital efficiency | FAT 0.16x, ROCE 5.13% | 0 | FAT<1x & ROCE<12 → else 0 | PASS |
| M4 Customer stickiness | 0 decline yrs, rec days not stable ±10 | 3 | 0 declines ≤ "max 1 decline" tier (no stability rider on tier 3) → 3 | PASS |
| M5 Scale/dominance | no peer mcap data | 0 (PEER DATA NEEDED) | correct | PASS |
| M6 Technology/R&D | no R&D line disclosed | 0 | correct (0); "PEER DATA NEEDED" label imprecise (own-data), score right | PASS |
| M7 Regulatory/license | no player count | 0 (PEER DATA NEEDED) | correct | PASS |
| M8 Distribution | no quantified reach | 0 | correct | PASS |
| M9 Brand | no peer GM benchmark | 0 (PEER DATA NEEDED) | correct | PASS |
| M10 Switching costs | rev grew all yrs, rec days rose 24.96 (>10); 0 declines | 0 | fails tier5 (>10d), fails tier3 (not stable), fails tier1 (needs 2+ declines) → else 0 | PASS |
| M11 Network effects | latest 3yr 27.2% NOT > prior 30.8%; sell% rising | 1 | ≥20% but selling% rising → 1 | PASS |
| M12 Negative WC/float | WC days negative all 4 yrs | 5 | majority negative → 5 | PASS |
| Block F total | | 14 | 5+0+0+3+0+0+0+0+0+0+1+5 = 14 | PASS |
| Moat class | M1,M4,M12 ≥3 = 3 present | MODERATE | 2-3 present → MODERATE | PASS |

### Structural / classification rules
| Rule | Check | Report | Re-derived | Verdict |
|---|---|---|---|---|
| Core total | A-E sum | 24 | 5+5+10+0+4 = 24 | PASS |
| Grand total | Core + Moat | 38 | 24+14 = 38 | PASS |
| Classification matrix | Core 24 <40 | AVOID | Core <40 → AVOID | PASS |
| Deal-breaker application | #1,#2,#3,#5,#6,#8 | fired; #6 dominant | #6 (ND/EBITDA 8.03>3 AND IC 1.17<3) → AVOID confirmed | PASS |
| Data confidence / history downgrade | 6 yr overall vs 4 yr BS metrics | "5-6 lower", no downgrade | see note | PASS (with note) |
| Output — mandated closing YAML block | prompt 01 requires fenced YAML at end | ABSENT (file ends at decision line 367) | FAIL | **FAIL (MAJOR)** |

NOTE (data confidence): report characterizes depth as "5-6 lower, flag may not have seen
full cycle" using the 6-year overall span, while Blocks A/B/D rest on only 4 years of
balance-sheet detail. Under the 3-4-year "LIMITED, downgrade one tier" rule, an analyst
keying on the constrained BS span could argue for a downgrade. The report keyed on the
overall span. Decision-neutral (AVOID either way). Logged MINOR.

**GATE 0 VERDICT: every scored line item and the AVOID classification re-derive cleanly and
CONCUR. One MAJOR structural fail — the mandated machine-readable YAML payload is missing
from the report file. Two MINOR interpretation notes (C2/C4 CAGR treatment; data-confidence
basis). recomputed_decision = AVOID (concurs).**

---

## PART 2 — EMERGING MOAT (B07) COMPLIANCE TABLE

| Rule | Check | Report | Verdict |
|---|---|---|---|
| All 23 categories addressed | A1-A4,B1-B3,C1-C2,D1-D2,E1-E2,F1-F2,G1-G2,H1-H3,I1-I2,R1 | all 23 present in Section 3 + summary table | PASS |
| NO EVIDENCE handling | zeros stated explicitly, not force-fit | 12 of 22 scored 0, 3 flagged adverse | PASS |
| Evidence multipliers (📄 1.0 / 🎙️ 0.7 / 🔍 0.5) | scoring table | B1-4.0, B2-3.0, C1-4.0, E1-3.0, F1 1×0.7=0.7, F2-4.0, G2-3.0, H2-3.0, H3-2.0, R1-2.0 | PASS |
| Adjusted total arithmetic | sum of adjusted rows | 4+3+4+3+0.7+4+3+3+2+2 = 28.7 ≈ 29 = em_score | PASS |
| Classification band | 25-39 = STRENGTHENING (absolute, no rescale) | 29 → STRENGTHENING | PASS |
| Completionist recount performed | recount line required when active > base rate | "📄 recount performed: ~20 items across 9 categories" stated | PASS |
| Evidence-tier consistency (no 🎙️-only scored as 📄) | F1 🎙️ → 0.7 applied; H1 🎙️ → 0; H2 mixed treated 📄 | F1/H1 correct; H2 rests on documented equity contributions → defensible 1.0 | PASS (with note) |
| Scoring table all 23 rows | Section 5 table | all 23 rows present | PASS |
| Category 21 (I1 Talent asymmetry) present + gated | scored >0 only if both legs, (b) ≥1 📄 | scored 0 (part (a) absent) — correctly gated | PASS |
| Category 22 (I2 Cannibalization barrier) present + gated | scored >0 only if named specific sacrifice | scored 0 (execution lead, no sacrifice named) — correctly gated | PASS |
| I1/I2 contribution stated separately | operator ruling requirement | "I1/I2 contribution: 0 of 29 (0%)" stated | PASS |
| capex_embedded_growth (Section 2C method) | capex under execution × FAT ÷ current rev | 14,720.7 × 0.16 ÷ 1,913 = 123% | PASS |
| Optionality register present | table of 0-scored / 🎙️-🔍 forward items | 6 rows present with converting evidence + window | PASS |
| Output — mandated closing YAML block | prompt 07 requires fenced YAML at end | present and complete | PASS |

NOTE (H2 mixed evidence): H2 raw 3 is labeled "📄/🎙️ mixed, treated 📄" and multiplied
1.0x. The scored core (Osaka Gas Rs176 Cr equity received; Apple JV Rs100+ Cr) is
documented; the 🎙️ 400+MW/3-yr target is separately parked in the optionality register.
Treating the documented core at 1.0x is consistent with the taxonomy. Logged MINOR, no
score impact.

**EMERGING MOAT VERDICT: all rules PASS. 23 categories addressed, multipliers correct,
completionist recount performed, I1/I2 present and correctly gated to 0, band applied as
absolute. em_score 29 (STRENGTHENING) re-derives cleanly. No fails.**

---

## PART 3 — VALUATION (B10/B11)

DEFERRED to phase 3. B10/B11 do not exist yet and the valuation framework docs (Master
Prompt v3.6, Section 1B layers, FTTCP v2.1) were not loaded in this phase-1 pass by design.
Valuation section marked pending.

---

## SUMMARY

- Gate 0: 38 rule checks, 37 pass, 1 fail (missing mandated YAML block — MAJOR).
- Emerging Moat: 12 rule checks, 12 pass, 0 fail.
- No CRITICAL findings. No re-derived score or classification flips a decision.
- recomputed_decision: AVOID (concurs with B01).
- Business Understanding Narrative (rule 9) and Halt-1 dossier (rule 10): not in phase-1
  inputs; not assessed.

Findings:
- MAJOR — B01 report file omits the mandated closing fenced YAML block (prompt 01 OUTPUT).
  Scores and classification are fully present in prose and B07 consumed them, so the AVOID
  decision survives; but the machine-readable stage payload is missing from the artifact.
- MINOR — B01 C2/C4 scored 0 via the loss-to-profit-swing clause though both CAGR endpoints
  are positive; strict first-bullet reading would compute ~30% PAT CAGR (C2=5, C4=5, Block C
  → 20, Core → 34). Decision-neutral: still <40 and deal-breaker #6 fires. AVOID unchanged.
- MINOR — B01 data-confidence keyed to the 6-year overall span; core Blocks A/B/D rest on
  4-year balance-sheet detail. No tier downgrade applied. Decision-neutral.
- MINOR — B07 H2 mixed 📄/🎙️ evidence treated at 1.0x. Defensible (documented core;
  🎙️ target parked in optionality register). No score impact.
