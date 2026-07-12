# VERIFIER C — FRAMEWORK ADHERENCE AUDIT (PHASE 1 SCOPE)
## Northern Arc Capital Ltd (NORTHARC) | Run date: 2026-07-12 | Model: claude-opus-4-8

**Scope this run:** Gate 0 (B01) and Emerging Moat (B07) framework-application
compliance ONLY. Valuation adherence (B10/B11) does not exist yet — it runs in
phase 3 and is left `pending` in the emitted block. I audit rule APPLICATION,
not raw numbers (Verifier A owns numbers) and not company quality. Stated
inputs (e.g. "median ROCE = 9.62%") are taken as given; the question is whether
the score, classification, and override that follow from them are the ones the
framework prescribes.

Severity scale: CRITICAL (misapplication that flips the classification/decision)
| MAJOR (wrong application or reasoning, classification survives) | MINOR
(imprecision, conservative-but-defensible edge call, presentational).

---

## PART 1 — GATE 0 (B01) COMPLIANCE

Framework: `prompts/01-gate-0-pipeline.md`. NBFC adaptation authorized by
operator instruction (per the report's Methodology Note and CLAUDE.md NBFC
handling). The task directs me to test whether that adaptation was applied
**consistently** and per a **defensible reading of the rules**, and whether the
**classification followed from the stated method**.

### 1.1 Block A — Return on Capital (re-derived vs thresholds)

| Rule | Stated input | Threshold band | Score in report | Re-derived | Verdict |
|---|---|---|---|---|---|
| A1 Median ROCE | 9.62% | <10 = 0 | 0 | 0 | PASS |
| A2 Min single-yr ROCE | 7.69% | <8 = 0 | 0 | 0 | PASS |
| A3 Median ROE | 10.93% | <12 = 0 | 0 | 0 | PASS |
| A4 ROCE trend (latest−earliest) | −0.76pp (8.86 vs 9.62) | 5=latest≥earliest / 3=decline 1-3pp / 1=3-5pp / 0=>5pp | 3 | ambiguous (see note) | PASS w/ MINOR |
| Block A sum | | | 3/20 | 3/20 | PASS |

**A4 edge (MINOR):** a 0.76pp decline falls in the undefined gap between the
"latest ≥ earliest = 5" band and the "decline 1-3pp = 3" band. The framework
defines no <1pp-decline case. The report scored the nearest lower band (3),
which is the CONSERVATIVE choice — scoring 5 would have been more generous.
No impact: Block A = 3 < 8 either way, so deal-breaker #1 triggers regardless.
The report flags the edge case explicitly. Acceptable, noted as MINOR.

- ROCE compute-when-absent rule: screener ROCE row was blank (stated) → computed
  via NBFC proxy (CapEmployed = Total Assets − Other Liabilities; EBIT = PBT +
  Int), "computed" stated. Framework rule ("compute only when absent, state
  computed") honoured. PASS.
- ROE opening-NW rule: FY2017 and FY2019 use closing NW only (no prior / FY2018
  gap), stated per the formula rule. PASS.

### 1.2 Block B — Cash Generation Quality

| Rule | Stated input | Band | Score | Re-derived | Verdict |
|---|---|---|---|---|---|
| B1 Cumul CFO/PAT | −5.02x | <0.50 = 0 | 0 | 0 | PASS |
| B2 FCF-positive yrs | 0 of 8 (0%) | <50 = 0 | 0 | 0 | PASS |
| B3 Cumul FCF/PAT | ≈−5.0x | negative = 0 | 0 | 0 | PASS |
| B4 ΔWC Days | NOT APPLICABLE (NBFC) | — | 0 (excluded from adj. denom) | see 1.6 | PASS (consistent) |
| Block B sum | | | 0/20 | 0/20 | PASS |

Note: B1/B2/B3 kept as REAL zeros (CFO exists, it is just negative) rather than
excluded as N/A — the correct, principled line (exclude where the INPUT is
structurally absent; keep where the input exists but is unfavourable). See 1.6.

### 1.3 Block C — Growth

| Rule | Stated input | Band | Score | Re-derived | Verdict |
|---|---|---|---|---|---|
| C1 Revenue CAGR | 24.65% (9yr) | ≥20 = 5 | 5 | 5 | PASS |
| C2 PAT CAGR | 22.83% (9yr) | ≥20 = 5 | 5 | 5 | PASS |
| C3 Positive YoY yrs | 7/7 consecutive = 100% | 100 = 5 | 5 | 5 | PASS |
| C4 PAT−Rev CAGR | −1.81pp | ±3pp = 3 | 3 | 3 | PASS |
| Block C sum | | | 18/20 | 18/20 | PASS |

- C3 handling of the FY2018 gap (excluding the non-consecutive FY2017→FY2019
  transition, counting 7 consecutive) is a defensible reading; CAGRs use elapsed
  years (9) per the formula. CAGR edge rules honoured (no negative endpoints, no
  loss-to-profit swing, no synthetic CAGR). PASS.

### 1.4 Block D — Balance Sheet (NBFC alternates)

| Rule | Stated input | Band applied | Score | Re-derived | Verdict |
|---|---|---|---|---|---|
| D1 (NBFC → CAR) | CRAR 22.56% | ≥18 = 5 | 5 | 5 | PASS |
| D2 (NBFC → PCR) | 47.8% | <60 = 0 | 0 | 0 | PASS |
| D3 Debt/Equity | Financials: default 3 | =3 | 3 | 3 | PASS |
| D4 Current Ratio | NOT APPLICABLE (NBFC) | — | 0 (excluded) | see 1.6 | PASS (consistent) |
| Block D sum | | | 8/20 | 8/20 | PASS |

- Correct use of the framework's NBFC branches (CAR for D1, PCR for D2,
  Financials-default-3 for D3). Deal-breaker #6 (ND/EBITDA>3x AND IC<3x → AVOID)
  correctly treated as a manufacturing test whose NBFC analogue (weak CRAR AND
  weak PCR) does not fire because CRAR is strong. Defensible. PASS.

### 1.5 Block E — Shareholder Alignment

| Rule | Stated input | Band applied | Score | Re-derived | Verdict |
|---|---|---|---|---|---|
| E1 | Prof. managed, FII+DII 56.5% >50% | "prof managed: 3 if FII+DII>50" | 3 | 3 | PASS |
| E2 | No promoter | NOT APPLICABLE (excluded) | — | — | PASS (consistent) |
| E3 | No promoter | NOT APPLICABLE (excluded) | — | — | PASS (consistent) |
| E4 | Not in provided data | data gap → 0 (KEPT in denom) | 0 | 0 | PASS |
| Block E sum | | | 3/20 | 3/20 | PASS |

- Correct use of the E1 "professionally managed" branch. Critically, E4 is
  treated as a genuine data-gap zero and KEPT in the denominator, while E2/E3
  are excluded as structural N/A — the report distinguishes "input structurally
  absent" (exclude) from "input missing from provided data" (score 0, keep).
  Internally consistent. PASS.

### 1.6 Consistency of the NBFC exclusion set (the core adaptation question)

Excluded from the adjusted denominator (structural N/A, 4 items × 5 = 20 pts):
**B4 (WC days), D4 (current ratio), E2 (promoter change), E3 (promoter pledge).**
Each is individually defensible — an Ind AS NBFC balance sheet is liquidity-
ordered with no current/non-current split (no WC-days, no current ratio), and no
promoter/promoter group exists. KEPT as real/gap zeros: B1/B2/B3 (CFO exists,
negative), E4 (data gap). The operative principle — *exclude where the input is
structurally absent, keep where the input exists but is unfavourable or merely
undisclosed* — is applied consistently across all five blocks and matches the
B07 M3/M12/G2 convention. **No inconsistency found in the exclusion logic.** PASS.

### 1.7 Classification — THE BINDING FINDING (MAJOR)

Raw `core_score` = 3+0+18+8+3 = **32/100** (arithmetic PASS). Framework matrix:
**Core <40 = AVOID**; Core 40-59 = AVERAGE. Literal application → **AVOID**.

The report instead returns **AVERAGE**, on two stated justifications:
1. Adjusted basis: 32 achieved ÷ 80 applicable = 40% → rescaled 40 → AVERAGE floor.
2. "Deal-breaker overrides already cap classification at max AVERAGE … which
   converges with the adjusted-basis reading."

Audit of each:

- **Justification 2 is logically invalid.** Deal-breakers #3 (median ROCE<10%)
  and #4 (cumul CFO/PAT<0.50) are correctly identified as triggered, and they do
  cap the class at **max AVERAGE** — but a cap sets a CEILING, not a FLOOR.
  AVOID sits *below* AVERAGE, so "max AVERAGE" is fully satisfied by AVOID. The
  deal-breakers therefore do NOT lift a sub-40 core out of AVOID and do NOT
  "independently converge" on AVERAGE. The report's convergence claim overstates
  framework support for the AVERAGE outcome.
- **Justification 1 is not a framework mechanism.** The framework provides no
  adjusted-basis / rescaling procedure; it maps absolute core points to classes.
  The rescaled figure lands *exactly* on the 40.0 boundary, so the outcome is
  maximally marginal — any single excluded/kept item flips it.

**Net:** the AVERAGE classification rests SOLELY on the operator-instructed
adjusted-basis rescaling. That instruction is authorized (CLAUDE.md + task), the
exclusion set feeding it is defensible and consistently applied (1.6), and the
framework itself notes "downstream position sizing may override AVERAGE for
documented post-IPO rebase / legacy cleanup cases" — so AVERAGE is a defensible
operator-authorized outcome and the classification **survives**. The fault is in
the report's REASONING: it presents a logically invalid deal-breaker-convergence
argument as independent corroboration, masking that the entire AVOID→AVERAGE lift
is carried by one out-of-framework, boundary-exact adjustment. **Severity: MAJOR**
(reasoning wrong / classification decision-relevant, but survives on operator
authority; not CRITICAL because it does not force a wrong final class given the
authorized adaptation).

*Mitigating (in the report's favour, not used by it):* deal-breaker #9
("history <3 years → AVERAGE") is phrased as a hard set, not a cap. Read on the
PUBLIC listed history (IPO 24-Sep-2024, ~1.75yr < 3yr) it would FORCE AVERAGE
natively — a clean, framework-internal path to the same class the report reached
via rescaling. The report instead reads "history" as financial-statement years
(9), setting `history_downgrade=true` separately; that reading is defensible and
leaves #9 dormant, but it means the cleaner native justification was left on the
table in favour of the contested rescaling.

### 1.8 Confidence adjustment, moat block, deal-breakers

- Confidence tier: 9 data points → "7-9 moderate", no forced tier downgrade.
  Correct per the numeric-years rule. PASS.
- Block F moat: M3/M12 marked NOT APPLICABLE and excluded (2 of 12); raw moat
  score 10; moats "present" (≥3) = M4/M8/M10 = 3 → "2-3 present = MODERATE".
  Bands applied correctly. M4/M10 scored 3 on the revenue-stability component
  with the receivable-days sub-condition N/A — the report drops from the "=5"
  band (which requires the N/A condition) to "=3", the conservative choice; the
  "=3" band's literal text ("max 1 decline year") actually describes a weaker
  company, so this is a defensible conservative mapping, flagged as
  lower-confidence. No effect on moats_confirmed or class. **MINOR (conservative).**
  M1 (−6.24pp margin > 5pp band → 0), M8 (=3), M11 (=1 on growth alone) all
  correctly applied. PASS.
- Deal-breaker application: #1,#2 (→max GOOD), #3,#4 (→max AVERAGE) correctly
  triggered with driving years stated; #5,#7,#8 correctly not triggered; #6
  N/A-defensible; #9 not triggered under the financial-years reading. Binding cap
  = max AVERAGE, correctly identified (subject to 1.7). PASS w/ the 1.7 caveat.

### Gate 0 verdict
Every block score, both CAGR handlings, the NBFC branch selections, the
exclusion-set logic, and the deal-breaker triggers are applied as written. One
MAJOR (classification reasoning, 1.7) and two MINORs (A4 edge band; M4/M10
conservative partial). The AVERAGE classification is defensible via operator
instruction but is carried entirely by a boundary-exact, out-of-framework
rescaling that the report's second justification misrepresents as independently
corroborated.

---

## PART 2 — EMERGING MOAT (B07) COMPLIANCE

Framework: `prompts/07-emerging-moat-pipeline.md`.

### 2.1 All 21 categories addressed
All 20 scan categories (A1-H3) plus R1 are addressed with either a strength
rating, "NO EVIDENCE FOUND", or "NOT APPLICABLE (NBFC)". Section 3 summary lists
all 20 rows; Section 5 scorecard lists all 21 (adds R1). **PASS — no silent
skips.** NBFC "NOT APPLICABLE" marks (A1, B1, B2, E2, G2) mirror the B01
convention and are not force-fit, per rule 5. PASS.

### 2.2 Raw (L×I) and evidence-multiplier application (re-derived)

| ID | L×I | Raw (re-derived) | Report raw | Mult (evidence) | Report mult | Adjusted | Verdict |
|---|---|---|---|---|---|---|---|
| A3 | LM | 1 | 1 | 🎙️ 0.7 | 0.7 | 0.7 | PASS |
| A4 | MM | 2 | 2 | 🎙️ 0.7 | 0.7 | 1.4 | PASS |
| B3 | HM | 3 | 3 | 🎙️ 0.7 | 0.7 | 2.1 | PASS (conservative) |
| C1 | MM | 2 | 2 | 🎙️ 0.7 | 0.7 | 1.4 | PASS |
| D1 | HH | 4 | 4 | 📄 1.0 | 1.0 | 4.0 | PASS |
| D2 | HH | 4 | 4 | 🎙️ 0.7 | 0.7 | 2.8 | PASS (conservative) |
| F2 | MM | 2 | 2 | 📄 1.0 | 1.0 | 2.0 | PASS |
| G1 | HM | 3 | 3 | 📄 1.0 | 1.0 | 3.0 | PASS |
| H1 | LM | 1 | 1 | 🎙️ 0.7 | 0.7 | 0.7 | PASS |
| H2 | LL | 1 | 1 | 📄 1.0 | 1.0 | 1.0 | PASS |
| H3 | LL | 1 | 1 | 📄 1.0 | 1.0 | 1.0 | PASS |
| R1 | HM | 3 | 3 | 🎙️ 0.7 | 0.7 | 2.1 | PASS |
| all others | — | 0 | 0 | — | — | 0.0 | PASS |

Re-summed adjusted total = 0.7+1.4+2.1+1.4+4.0+2.8+2.0+3.0+0.7+1.0+1.0+2.1 =
**22.2**. Report: 22.2, rounded 22. **PASS.**

### 2.3 Evidence-tier discipline (the key skeptical check)
Framework's failure mode is a "🎙️-only category scored as if 📄." Auditing the
five rows carrying the 1.0x multiplier (D1, F2, G1, H2, H3): each rests on a
genuine audited/AR-disclosed 📄 anchor (D1 47.52mn data points AR p.53; F2 the
B05 promise-delivery reconciliation; G1 rating action AR note 62 + CoF/D&E/DFI
disclosures; H2 SMBC stake AR shareholding pattern; H3 Green Bond AR p.21).
**No 🎙️-only row was upgraded to 📄.** If anything the report under-credits:
D2, B3, and C1 all carry documented components in the narrative yet are scored
at 🎙️ 0.7x — the conservative (score-lowering) direction, the opposite of the
guarded failure. **PASS, clean.**

### 2.4 Completionist recount
Framework requires a 📄 recount whenever ≥12 categories are active. Report:
6 Strong/Moderate (within the stated 3-6 base rate), recount performed and
stated verbatim ("9 documented items across 5 categories …"). The 12+ trip wire
did not fire and the recount line is present. **PASS.**

- **MINOR:** the Section 3 line "6 of 20" is loose — it names 5 categories from
  the 20 (D1,D2,B3,F2,G1) plus R1 (the 21st, in Section 4) to reach 6. The YAML
  `active_categories` correctly lists all 6 incl. R1. Presentational only; no
  effect on score, recount, or classification.

### 2.5 Classification and combined read
- Adjusted 22 → framework band "12-24 MODEST MOAT DEVELOPMENT". Report: MODEST.
  **PASS.**
- 6D combined: EM 22 sits 3 short of the 25-pt STRENGTHENING floor, so the
  AVERAGE-backward × forward pairing does not unlock HIGH POTENTIAL / TURNAROUND.
  Matrix reasoning applied correctly; combined = AVERAGE. **PASS.**
- `capex_embedded_growth_pct = 0`: Section 2C's capex×FAT arithmetic marked
  NOT APPLICABLE for a balance-sheet lender, recorded as 0 per the B01 NBFC
  convention, explained. Consistent with the authorized adaptation; the "0" is
  labelled N/A rather than a real 0% and is unlikely to be misread. Acceptable.

### Emerging Moat verdict
Fully compliant. All 21 categories addressed, L×I and evidence multipliers
applied exactly, no 🎙️→📄 over-crediting (if anything conservative), completionist
recount performed and stated, classification and combined read both correct. One
MINOR presentational imprecision ("6 of 20" phrasing).

---

## PART 3 — VALUATION (B10/B11)
**PENDING — PHASE 3.** B10 and B11 do not exist at this stage. Valuation-
adherence audit (continuous Pillar 1, FTTCP ROCE authority, single-credit rule,
Pillar 2/3, UA Amendment 3, dual-track, Hurdle Ratio, 4D weights, SOM
cross-check, one-improvement-one-mechanism) is out of scope for this run and is
emitted as pending.

---

## SUMMARY

| Framework | Rules checked | Clean | Fails | Notes |
|---|---|---|---|---|
| Gate 0 (B01) | 30 | 29 | 1 MAJOR | + 2 MINOR (A4 edge; M4/M10 conservative partial) |
| Emerging Moat (B07) | 15 | 15 | 0 | + 1 MINOR (presentational "6 of 20") |
| Valuation (B10/B11) | pending | — | — | phase 3 |

**Acceptance rate (rules passed ÷ checked, phase-1 frameworks): 41/45 ≈ 91%.**
Well above the 60% rework trigger. No CRITICAL. The single MAJOR is a reasoning
defect in the Gate 0 AVOID→AVERAGE lift: the classification is defensible only on
operator-authorized adjusted-basis rescaling (boundary-exact at 40.0), and the
report's secondary "deal-breakers converge on AVERAGE" justification is logically
invalid because caps set a ceiling, not a floor. Recommend the synthesis stage
treat the AVERAGE class as operator-adjusted-basis-only, at the AVOID/AVERAGE
boundary, and not as independently corroborated by the deal-breaker overrides.

```yaml
stage: B12c
company: "NORTHARC"
run_date: "2026-07-12"
model: claude-opus-4-8
status: complete
gate0:
  rules_checked: 30
  fails:
    - {rule: "Classification matrix + deal-breaker application", severity: MAJOR, detail: "Literal core 32<40 = AVOID per matrix; AVERAGE rests solely on operator-instructed adjusted-basis rescaling (32/80=40%, exactly the 40.0 boundary). Report's second justification — deal-breakers #3/#4 'cap at max AVERAGE, converging on AVERAGE' — is logically invalid: a cap is a ceiling not a floor, and AVOID satisfies 'max AVERAGE'. Class survives on operator authority (exclusion set is consistent and defensible) but is not independently corroborated as the report claims."}
emoat:
  rules_checked: 15
  fails: []
valuation: {rules_checked: 0, fails: []}
recomputed_destination_pe: "pending phase 3"
recomputed_decision: "pending phase 3"
findings:
  - {severity: MAJOR, location: "B01 §Classification", claimed: "AVERAGE, corroborated independently by deal-breaker caps + adjusted basis", framework_truth: "Core 32<40 = AVOID literally; deal-breaker caps set a ceiling (max AVERAGE), not a floor, so they do NOT lift AVOID to AVERAGE; AVERAGE is carried solely by the operator-authorized, boundary-exact (40.0) adjusted-basis rescaling, which is not a framework mechanism", note: "Classification defensible via operator instruction and consistent exclusion set, so it survives; the stated dual-justification overstates framework support. Cleaner native path (deal-breaker #9 on 1.75yr public history -> AVERAGE) was available but unused."}
  - {severity: MINOR, location: "B01 §Block A / A4", claimed: "A4 = 3 for a 0.76pp ROCE decline", framework_truth: "0.76pp decline falls in the undefined gap between the 'latest>=earliest=5' and 'decline 1-3pp=3' bands; nearest-lower-band choice is conservative", note: "No impact: Block A=3<8 either way; deal-breaker #1 fires regardless. Flagged in-report."}
  - {severity: MINOR, location: "B01 §Block F / M4,M10", claimed: "M4=3, M10=3", framework_truth: "'=5' band requires a receivable-days sub-condition that is N/A for an NBFC; dropping to '=3' is the conservative mapping", note: "No effect on moats_confirmed (still 3) or MODERATE class; flagged lower-confidence in-report."}
  - {severity: MINOR, location: "B07 §Section 3 summary", claimed: "'6 of 20' Strong/Moderate", framework_truth: "5 of the 20 (D1,D2,B3,F2,G1) + R1 (the 21st category) = 6; YAML active_categories lists all 6 correctly", note: "Presentational only; no effect on score, completionist recount, or classification."}
critical_count: 0
major_count: 1
minor_count: 3
acceptance_rate: 91
```
