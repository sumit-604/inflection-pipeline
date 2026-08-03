# QUARTERLY PIPELINE A5 — ADVERSARY / COMPLETENESS AUDIT
# SAMHI Hotels Limited (SAMHI) — Q1 FY27 (quarter ended 30 June 2026)
# Auditor: A5 (fresh context: A4 review + A1 extracts + A2 ledgers only). All figures re-derived.
# RE-AUDIT after narrow A4 correction loop (loop 1 of 2).

---

Scope of this loop: the three arithmetic-precision figures A4 was required to
change, applied consistently everywhere (no stale 5.8% / 4.9x / 16.9%), plus a
spot-confirmation that no OTHER derived metric regressed and no NEW arithmetic
inconsistency was introduced by the edits. Coverage and the structural items
(verdict / cash-conversion-cap reconciliation, the Q4FY26 column mis-read
correction, Questions-for-Management completeness) passed in the prior audit on
identical, unedited inputs and are re-affirmed below.

---

## 1. COVERAGE AUDIT (re-affirmation — inputs unchanged since prior PASS)

The three A1 extracts and three A2 ledgers are byte-identical to the prior loop
(only `review_samhi_q1fy27.md` was edited). I re-confirmed that every row touched
by the three corrections is still enumerated in the ledger and cited in A4, so
the edits did not orphan or drop any row.

| Category | A2 count | Fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Owners-of-Company PAT row (extract L758) | present | present | cited review L124/125, L163, L506 | PASS |
| Profit-for-period / total PAT row (extract L760) | present | present | cited review L124, L262, L504 | PASS |
| Consolidated deferred-tax row (extract L740) | present | present | cited review L122/123, L141, L222 | PASS |
| PBT-before-exceptional row (extract L735) | present | present | cited review L117, L262 | PASS |
| All other ledger rows | unchanged | unchanged | reviewed, no finding (prior loop) | PASS |

No orphan rows; no row my fresh pass found that the ledger lacks. Coverage: PASS.

---

## 2. ARITHMETIC AUDIT (core of this re-audit — full re-derivation)

Raw inputs verified directly against the A1 results extract:
- Owners' PAT: Q1 FY27 = 182.50, Q1 FY26 = 172.80 (extract L758; column order Q1FY27 | Q4FY26 | Q1FY26 | FY26).
- Total PAT FY26 = 5,665.45 (extract L760).
- Consolidated deferred tax Q1 FY26 = 38.67 (extract L740).
- Consolidated PBT-before-exceptional Q1 FY26 = 259.05; discontinued-ops loss = 28.22 → PBT reported = 230.83 (extract L735/L745).
- PBT-before-exceptional FY26 = 1,649.83 (extract L735).

### The three required corrections

| # | Metric | A4 value (corrected) | My re-derivation | Source | Status |
|---|---|---|---|---|---|
| 1 | Owners'/SAMHI-attributable PAT YoY | **+5.6%** | (182.50 − 172.80)/172.80 = 9.70/172.80 = 0.05613 = **+5.6%** | extract L758; review L163, L175, L216, YAML L464/470/506 | **PASS** (old +5.8% eliminated) |
| 2 | FY26 reported/normalised PAT distortion multiple | **~4.6x** | normalised = 1,649.83 × (1 − 0.25) = 1,237.37; 5,665.45 / 1,237.37 = **4.58x ≈ 4.6x** | extract L760/L735; review L262, L332, YAML L504 | **PASS** (old ~4.9x came from taxing at 30% → 1,154.9 → 4.9x; now correctly at ~25%) |
| 3 | Q1 FY26 effective tax rate | **~16.7%** | 38.67 / 230.83 = 0.16752 = **16.75% ≈ 16.7%** | extract L740; PBT 259.05 − 28.22 = 230.83; review L141, L222, L314 | **PASS** (marked "~"; on the rounding boundary, within tolerance, matches task-defined 38.67/230.83) |

### Consistency sweep for stale values
Grep over the full review for `5.8%` / `4.9x` / `16.9%` → **zero matches.** Every
downstream restatement of each figure uses the corrected value: owners-PAT +5.6%
at L163 / L175 / L216 / L302 (83% complement) / YAML L464 / L470 / L506; distortion
~4.6x at L262 / L332 / L504; ETR ~16.7% at L141 / L222 / L314. No stale instance
survives.

### Regression spot-check (no NEW inconsistency introduced by the edits)

| Metric | A4 value | My re-derivation | Source | Status |
|---|---|---|---|---|
| NCI share of YoY PAT increment | 83% | 47.41/57.11 = 83.0% (owners complement 9.70/57.11 = 17.0%) | review L302, L175, L216 | PASS |
| Total consolidated PAT YoY | +29.7% | (249.27 − 192.16)/192.16 = 57.11/192.16 = 29.72% | extract L760; review L162, L202 | PASS |
| Q1 FY27 ETR | 23.9% | 78.06/327.33 = 23.85% | extract L740/L737; review L141, L222 | PASS |
| PAT bridge total | +57.11 (+29.7%) | 77.30 − 120.09 − 18.17 + 129.27 + 28.22 − 39.39 = +57.14 (ties to +57.11 within component rounding) | review L204-214 | PASS |
| FY26 PAT DTA-inflation ("~2x", L388) | ~2x | 5,665.45 / PBT 2,671 = 2.12x | review L388 | PASS — DISTINCT metric (PAT-over-PBT = 2.12x) from the 4.6x reported/normalised distortion; pre-existing, correct, not conflated with the corrected 4.6x |

The "~2x" at L388 and the "~4.6x" distortion are two different ratios
(PAT-over-PBT = 2.12x vs reported-over-normalised = 4.58x); both are internally
correct and the edit did not blur them. No new inconsistency introduced.

Arithmetic: PASS.

---

## 3. ADVERSARIAL READ (spot-confirm the three most positive claims still carry their bear counter)

The corrections all sharpen bear-side precision, so no positive claim was
strengthened by the edits. Confirming the standing counters remain grafted:

1. **"Revenue from operations +12.1%, core operating PBT ex-OI +174%" (L159/169).**
   Bear counter: the +174% is finance-cost-led (−25.5%, +Rs 129 mn), not operating
   leverage; operating EBITDA alone +8.5% and margin −106 bps. **Already in A4**
   (L173, L219). Survives — already incorporated; no graft needed.

2. **"Consolidated PAT +29.7%" (L162).** Bear counter: owners' PAT only **+5.6%**
   (182.50 vs 172.80); minority took 83% of the increment; FY26 comparator is
   DTA-inflated. **Already in A4** (L163, L175, L377, flag L506). Survives — the
   corrected +5.6% makes the counter sharper and it is fully carried.

3. **"FY26 PAT Rs 5,665 mn / deleveraged, A+ rating" (L262/387).** Bear counter:
   FY26 PAT is ~**4.6x** the normalised ~Rs 1,238 mn (DTA credit ~Rs 3,000 mn), not
   a valuation anchor; ETR climbing ~16.7% → 23.9% → ~25%. **Already in A4** (L222,
   L262, L293, flag L504). Survives — already incorporated.

No surviving bear counter is absent from A4. Nothing to graft.

---

## VERDICT

**COMPLETE.** All three required corrections are arithmetically correct and applied
consistently across the prose tables, the Step-4 / Step-6 / Step-8.5 narratives,
the combined-verdict flags, and the closing YAML. No stale 5.8% / 4.9x / 16.9%
remains (grep-confirmed zero). No new arithmetic inconsistency was introduced; the
distinct PAT/PBT ~2x ratio was not conflated with the corrected reported/normalised
~4.6x distortion. Coverage and structural items re-affirmed on unchanged inputs.
This review may proceed to Notion save.

```yaml
stage: A5-adversary
company: "SAMHI"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
loop_back_to: ""
gap: ""
```
