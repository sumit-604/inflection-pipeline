# A5 ADVERSARY / COMPLETENESS AUDIT (RE-RUN) — SRM Contractors Limited (SRM), Q1 FY27

Second pass, against the A4-re-emitted review at the same path. Extract and ledger unchanged;
re-derived independently — no assumption about what A4 changed. Prior verdict was INCOMPLETE
(standalone PAT bridge did not foot). This pass verifies the re-emission.

Audited: A4 review (`review_srm_q1fy27.md`), A1 extract (`extract_results_srm_q1fy27.txt`, 438
lines), A2 ledger (`ledger_results_srm_q1fy27.md`).

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate)

PLAIN-LANGUAGE BRIEF (review 446-466), all four labelled parts present and substantive:
narrative (448-449), sector (451-455), business-model (457-461), competition (463-466).
**Gate 0: PASS** — unchanged from first pass.

---

## AUDIT 1 — COVERAGE (fresh enumeration vs A2 ledger)

Extract and ledger unchanged; my fresh counts reproduce the ledger (notes 11, line_items 48,
zero_standing 10, agenda_items 1, entities 8 [grep `[a-h]\)` returns 7; item c OCR-garbled "¢)"
@412; re-sweep 8], signature_blocks 7, reliance_table_items 3). Every ledger row cited in A4 or
shown ND/nil. No orphan rows, none missing from ledger. Two cosmetic A2 count-total notes carried
forward (auditor_paras total 12 vs 13 enumerated; ZERO_STANDING summary string omits std row 20) —
non-gating, no content lost. **Coverage: PASS.**

---

## AUDIT 2 — ARITHMETIC (full recompute; focus on the two items the coordinator named)

### 2a. Standalone PAT bridge (Step 4A) — now FOOTS. PASS.

| Bridge line | A4 value | My recompute (raw Lakhs) | Status |
|---|---|---|---|
| Gross profit change (Rev−COGS−Direct) | +14.22 | Q1FY27 45.07 − Q1FY26 30.85 | PASS (matches its own formula) |
| Employee cost increase | −2.11 | 1000.28 − 788.81 = 211.47 → 2.11 | PASS |
| Other expenses change (fell) | +0.14 | ~2.25 (balancing) vs 2.39 → +0.14 benefit | PASS |
| **subtotal → Op EBITDA** | **+12.25** | 14.22 − 2.11 + 0.14 = 12.25 | **PASS (foots)** |
| Depreciation increase | −7.63 | 1001.99 − 239.40 = 762.59 → 7.63 | PASS |
| Finance cost increase | −2.83 | 414.29 − 131.12 = 283.17 → 2.83 | PASS |
| Other Income change | −1.12 | 47.10 − 159.28 = −112.18 → −1.12 | PASS |
| Tax change (benefit) | +2.21 | see 2b | PASS |
| **Reported PAT YoY change** | **+2.88** | 12.25 − 7.63 − 2.83 − 1.12 + 2.21 = 2.88 | **PASS (foots to printed PAT Δ)** |

The prior FAIL (GP line +18.35 that contradicted its own formula; other-expense sign inverted;
column summing to 16.01 not 12.25) is **fully corrected**. Column foots end-to-end.

### 2b. Tax-line sign change — reconciles to the printed standalone PAT. PASS.

A4 now reads the standalone ₹162.67 lakh deferred-tax line as a **credit** (+₹2.21 Cr benefit).
Verified against the printed extract, and the sign is **determinate**, not a free choice:

| Test | Computation (extract 180-186) | Result |
|---|---|---|
| Foot with deferred as CREDIT | 1,912.46 − 481.33 **+** 162.67 | = **1,593.80** = printed PAT ✓ |
| Foot with deferred as CHARGE | 1,912.46 − 481.33 − 162.67 | = 1,268.46 ≠ printed PAT ✗ |
| Independent EPS cross-check | EPS 6.95 × ~229.45 lakh shares* | = 1,594.7 ≈ printed PAT 1,593.80 ✓ |
| (charge reading would imply EPS) | 1,268.46 / 229.45 | = 5.53 ≠ printed 6.95 ✗ |
| Net std tax Q1FY27 | 481.33 − 162.67 | = 318.66 lakh = ₹3.19 Cr |
| Net std tax Q1FY26 | 369.21 + 170.88 | = 540.09 lakh = ₹5.40 Cr |
| Tax change (benefit) | 540.09 − 318.66 | = 221.43 lakh = **+₹2.21 Cr** ✓ ties to bridge |

*Share count triangulated from every other printed period (1305.96/5.69, 3363.84/14.66,
8557.91/37.31, consol 1971.25/8.59) — all ≈ 229.4-229.5 lakh, corroborating the anchor.

**Both** the printed PAT (₹1,593.80 lakh) **and** the printed EPS (₹6.95) independently force the
credit reading; the extract's positive "16267" is an OCR-dropped minus (A2 recorded it positive
without flag). Near-identical magnitude to the consolidated credit −163.49 (FF7) confirms it is the
same deferred-tax event. A4's +2.21 tax benefit is correct and foots to the authoritative printed PAT.

### 2c. Consistency of the correction across the review — PASS.

The credit reading is now propagated everywhere it touches; no section contradicts the bridge:
- Step 1C ETR row (122) keeps 33.68% as the labelled face-value charge reading **with an explicit
  adjacent caveat (125)** that the printed PAT only foots as a credit → true ETR ~16.7%, sign to be
  confirmed with management. Transparent, not asserted as truth.
- Step 2 diagnostic 4 (185) rewritten: the +22% PAT is "a ~10.6% core story plus a deferred-tax
  credit," aligned with the bridge. The old contradicting "ETR ROSE to 33.68%, a further drag"
  language is gone.
- YoY table PAT verdict (158) now "Flattered by deferred-tax credit (see Step 4A)."
- Flags list (525) reframed to "Standalone deferred-tax sign ambiguity: printed PAT foots at ~16.7%
  ETR (credit) vs 33.68% charge reading — confirm with management (FF6)."
- Questions Q4 (413) and YAML (504) reframed to the deferred-tax **sign** confirmation.

The genuine ambiguity (OCR-dropped sign) is resolved to the authoritative printed figures for all
conclusions, and disclosed transparently. Not an unresolvable-arithmetic FAIL under discipline #4 —
it is resolved (PAT + EPS both force the credit), and the residual "confirm with management" is about
the underlying DTA cause, not the arithmetic value.

### 2d. All other derived metrics — re-verified PASS (unchanged).

Std/consol Op EBITDA, margins, Reported EBITDA, Core PBT ex-OI, OI/PBT, consol ETR 18.84%
[(619.63−163.49)/2421.39], PAT margins, all YoY %, S-vs-C PAT gaps (23.68 / 60.54 / −2.39 / 29.72),
MIPL residual ₹365.6 lakh and ~31.8% margin, reviewed-subs 0.34% margin and 17.6% of consol revenue,
consol bridge 4B footing to +6.96 within the acknowledged ~₹6 lakh OCR tax artefact — all reconcile.

---

## AUDIT 3 — ADVERSARIAL READ

The three strongest bear counters (margin +746 bps possibly revenue-recognition timing; no-NCI
overstating consol EPS 8.59 + DTA-credit flatter; "clean" audit resting on 17.6%-of-revenue
board-certified components + duplicate UDIN) all survive on the extract and all remain incorporated
in A4 (FF3/FF4/FF5/FF7/FF10, Step 2 diag 2, Q1/Q3/Q8/Q9, briefs). The re-emission additionally turns
the "+22% PAT" from a positive optic into a disclosed tax-aided figure, which strengthens the bear
symmetry rather than weakening it. **No new unincorporated surviving bear counter.**

---

## VERDICT

**COMPLETE.**

- Gate 0 (deliverable): PASS — all four brief parts present.
- Coverage: PASS — no orphan rows, no ledger-missing rows.
- Arithmetic: PASS — the standalone PAT bridge (Step 4A) now foots end-to-end; the deferred-tax
  sign change reconciles exactly to the printed standalone PAT (1,593.80) and is independently
  corroborated by the printed EPS (6.95); the correction is propagated consistently across Step 1C,
  Step 2, the flags, and the Questions table. All other derived metrics reconcile.
- Adversarial: PASS — three surviving bear counters, all incorporated; none new.

No loop-back. Cleared for Notion save.

```yaml
stage: A5-adversary
company: "SRM"
quarter: "q1fy27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
loop_back_to: ""
gap: ""
```
