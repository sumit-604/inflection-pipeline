# VERIFIER C — FRAMEWORK ADHERENCE AUDIT (B12c)
Company: INDIAGLYCO | Run date: 2026-08-24 | Model: claude-opus-4-8
Scope: PHASE 1 (Gate 0 + Emerging Moat only). Valuation audit (B10/B11)
deferred to phase 3; valuation framework docs not loaded this phase.

Rule sources: prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md
Audited artifacts: B01-gate0.yaml, 01-gate0.md, B07-emoat.yaml, 07-emoat.md

I audit rule application only. Raw source-number fidelity belongs to
Verifier A and is out of my scope.

---

## PART 1 — GATE 0 (B01) COMPLIANCE

### Block A — Return on Capital (re-derived)

| Item | Stated input | Framework band | Correct score | Reported | Verdict |
|---|---|---|---|---|---|
| A1 Median ROCE | 11.96% (median of FY25 11.85, FY26 12.08) | 10-14.9% = 1 | **1** | **3** | **FAIL** |
| A2 Min single-yr ROCE | 11.85% | 8-11.9% = 1 | 1 | 1 | PASS |
| A3 Median ROE | 11.39% | <12% = 0 | 0 | 0 | PASS |
| A4 ROCE trend | +0.23pp, latest >= earliest | latest>=earliest = 5 | 5 | 5 | PASS |

Block A as reported = 9. Re-derived = 1+1+0+5 = **7**.

**FINDING G-1 (MAJOR).** A1 mis-scored. Report line 55 states the correct
band ("10-14.9%") but assigns 3. Per rule file line 56, the 10-14.9% band
scores 1; the value 3 belongs to the 15-19.9% band. Correct A1 = 1.
Effect: Block A 9 -> 7; core_score 42 -> 40; grand_total 46 -> 44. The
40-59 band is still AVERAGE, so classification does not flip. Decision
survives -> MAJOR, not CRITICAL. Location: 01-gate0.md line 55;
B01-gate0.yaml line 13 (blocks.A: 9), line 14 (core_score: 42), line 16
(grand_total: 46).

### Block A deal-breaker consequence

Rule file lines 154-160, deal-breaker 1: "Block A <8 -> max GOOD."
With the corrected Block A = 7 (<8), deal-breaker 1 fires. The report
(line 95) checked "Block A = 9, not <8 -> not triggered" and lists
deal_breakers: [] (yaml line 20).

**FINDING G-2 (MAJOR).** Deal-breaker 1 not recorded. Direct consequence
of G-1: corrected Block A = 7 triggers DB1 (max GOOD). It does not change
the outcome, because AVERAGE already sits below the GOOD cap, but the
deal_breakers list should carry DB1 with the driving years (FY25-FY26
window). Rule 2 of my rubric requires deal-breaker application be
checked; the list is incomplete once G-1 is corrected. Location:
01-gate0.md line 95, 269-270; B01-gate0.yaml line 20.

### Blocks B, C, D, E — re-derived, all PASS

- **B1** CFO/PAT 2.06 -> >=1.00 = 5. PASS. **B2** FCF 0/2 yrs = 0% -> <50 = 0. PASS.
  **B3** cumFCF/PAT -0.86 -> negative = 0. PASS. **B4** WC days -14.56 ->
  decreased >5 = 5. PASS. Block B = 10, matches. (B2-B4 on a 2-yr window
  vs B1 on 10-yr is a source-coverage limitation, disclosed, permitted by
  rule file line 26 "use whatever history is available.")
- **C1** rev CAGR 5.97% -> 5-9.9 = 1. **C2** PAT CAGR 26.6% -> >=20 = 5
  (no loss-to-profit swing; edge rules honoured). **C3** 6/9 up = 66.7% ->
  50-74 = 1. **C4** +20.6pp -> >=+3 = 5. Block C = 12, matches. PASS.
- **D1** ND/EBITDA 2.51x -> 2-3x = 1. **D2** IC 3.26x -> 3-4.9 = 2.
  **D3** D/E 0.58 -> 0.5-1.0 = 3. **D4** CR 0.74x -> <1.0 = 0. Block D = 6,
  matches. PASS.
- **E1/E2/E3** NOT FOUND -> 0 each (rule file line 20-23 grounded-claims:
  N/A scored 0, no estimate). **E4** contingent/NW 1.33% -> <5 = 5.
  Block E = 5, matches. PASS.

### Block F — Moat (re-derived, all 12 PASS)

M1=0 (rev CAGR 5.97% <10% floor), M2=0/M5=0/M7=0/M9=0 (PEER DATA NEEDED,
correctly scored 0 not guessed), M3=0 (FAT 0.92x <1x), M4=0 (3 decline
yrs), M6=0 (R&D not in provided data), M8=1 (mentioned unquantified),
M10=1 (growth, 2+ decline yrs), M11=1 (growth>15% but selling% rising),
M12=1 (FY26 39.36 days band 15-45). Moat total = 4; moats_confirmed
(>=3) = 0; moat_class NONE (0 present, rule file line 138-139). PASS.

### Classification and confidence

- Core 42 (reported) -> AVERAGE (40-59). With G-1 correction core 40, still
  AVERAGE. Matrix applied correctly (rule file line 150).
- Data confidence: 10 yrs P&L/CF -> "full"; history_downgrade false is
  correct (rule file line 143; company traded 10+ yrs, the BS-split gap is
  source coverage not history depth). PASS.
- CAGR edge rules: no negative/zero endpoints; loss-to-profit correctly
  absent; C4 not N/M. PASS.

**Gate 0 result: 24 rule applications checked, 2 FAIL (G-1 A1 mis-score,
G-2 linked deal-breaker omission). Classification AVERAGE is robust to
the correction.**

---

## PART 2 — EMERGING MOAT (B07) COMPLIANCE

### Category completeness (rubric rule 3, rule file lines 65-153, 170-181)

All 23 rows present in the Section 3 summary table and Section 5
scorecard: A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G3(H1-H3), I1,
I2, R1. Categories with no evidence explicitly marked NO EVIDENCE FOUND
(B3, D1, D2, H1). PASS.

### Family I guardrails (rubric rule 8, rule file lines 122-153)

- **I1 (Talent asymmetry, Cat 21)** scored 0. Report finds leg (a)
  partially present (named hires) but leg (b) — competitor-economics
  arithmetic — absent, no 📄 source. Rule file lines 136-138 require the
  (b) leg with >=1 📄 for any top-band score; scoring 0 is compliant. PASS.
- **I2 (Cannibalization barrier, Cat 22)** scored 0. Report applies the
  test to every claimed moat and finds no named, specific sacrifice
  ("nothing must be destroyed... execution lead"). Rule file lines 148-153
  require a named specific sacrifice for >0; scoring 0 is compliant. PASS.
- I1/I2 contribution stated separately (Section 5 line 234; yaml
  completionist_recount). Feeds the operator review checkpoint per rule
  file lines 179-181. PASS.

### Multiplier and tier consistency (rubric rule 3, rule file line 205)

Re-derived every adjusted score = raw x multiplier (📄=1.0, 🎙️=0.7,
🔍=0.5):

A1 2x0.7=1.4, A2 1x0.5=0.5, A3 3x1.0=3.0, A4 3x1.0=3.0, B1 2x1.0=2.0,
B2 4x1.0=4.0, B3 0, C1 2x0.7=1.4, C2 1x0.7=0.7, D1 0, D2 0, E1 3x1.0=3.0,
E2 1x0.7=0.7, F1 1x1.0=1.0, F2 3x1.0=3.0, G1 3x1.0=3.0, G2 1x1.0=1.0,
H1 0, H2 2x1.0=2.0, H3 1x1.0=1.0, I1 0, I2 0, R1 2x1.0=2.0.
Sum = **32.7 ~= 33**, matches em_score. PASS.

Tier discipline check (rule 3 example: a 🎙️-only category must not score
as if 📄): A1 self-reported scarcity claims correctly held at 🎙️ 0.7x
(not upgraded to 📄 despite AR assertion); C1/C2 held at 0.7x; A4/H2
mixed with a genuine 📄 leg (L'Oreal delivery; Clariant stake-sale
disclosure) so 1.0x is defensible. No 🎙️-only category scored at 📄. PASS.

### Completionist guard (rule file lines 40-46, 159)

9 of 23 rows Strong/Moderate, below the 12-category red-flag threshold.
Explicit 📄 recount line present ("~17 distinct documented items across
9 categories... 33 documented total"). Guard performed as written. PASS.

### Classification band (rule file lines 175-181)

Adjusted 33 -> 25-39 band -> MOAT STRENGTHENING. Absolute bands honoured
(no rescale), ceiling 92 acknowledged, "EM >=25" UA qualifier cleared.
PASS.

### Two MINOR observations (within tolerance, not rule fails)

**FINDING E-1 (MINOR).** capex_embedded_growth_pct: yaml line 38 = 1;
Section 2C text computes ~1.2%. Integer truncation, immaterial.

**FINDING E-2 (MINOR).** Combined classification 6D = HIGH POTENTIAL
(yaml line 48). Rule file lines 202-207 key the transition setups to
"AVERAGE backward scores with EXPANSION forward scores"; here the forward
score is STRENGTHENING (33), one band below EXPANSION (>=40). The 6D
matrix carries no exact threshold cells, and the report gives full
reasoning and self-labels the signal "second-tier, not top-tier," so this
is a permissible judgment, not a violation. Flagged so the operator sees
HIGH POTENTIAL rests on a sub-EXPANSION forward score.

**Emerging Moat result: 26 rule applications checked, 0 FAIL, 2 MINOR
observations. Fully compliant on the load-bearing rules (23-category
coverage, multipliers, I1/I2 guardrails, completionist recount, band).**

---

## VALUATION (B11/B10) — PENDING PHASE 3

Not run. B10/B11 blocks do not exist this phase and the valuation
framework docs (Master v3.6 Role 1, Section 1B layer set, FTTCP v2.1) are
deliberately withheld as dead context. Rubric rules 4-7 and 11-12
deferred.

---

## SUMMARY

- Gate 0: 24 checks, 2 FAIL (both MAJOR, both flowing from a single A1
  band-mapping slip). Classification AVERAGE unaffected.
- Emerging Moat: 26 checks, 0 FAIL, 2 MINOR. Compliant.
- Framework adherence (Gate0 + EM portion): 48 of 50 rule applications
  clean = 96%.
- No CRITICAL. No decision flip. acceptance_rate 96% (> 60%), so no
  REWORK trigger from this verifier.
</content>
</invoke>
