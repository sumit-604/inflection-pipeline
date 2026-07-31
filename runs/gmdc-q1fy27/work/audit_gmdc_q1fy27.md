# A5 ADVERSARY / COMPLETENESS AUDIT — GMDCLTD Q1 FY27 (LOOP 2, RE-AUDIT)

Scope: full re-run of coverage + arithmetic + adversarial audits on the REVISED A4 review, plus verification that the loop-1 finding (consolidated 1C carrying standalone values) is now closed and that the fix broke nothing downstream. Fresh context: I re-derived every figure below from the A1 extract myself; I did not defer to A4's or A3's cites.

---

## 1. COVERAGE AUDIT (fresh grep pass vs A2 ledger)

| Category | A2 count | My fresh count | Method | Orphan rows | Status |
|---|---|---|---|---|---|
| Numbered notes (std 4 + cons 5) | 9 | 9 | sweep L256-279 (4) + L379-406 (5) | none | PASS |
| Unnumbered footnote | 1 | 1 | L155-159 | none | PASS |
| Agenda items | 3 | 3 | grep `^\s*\([0-9]+\)\s` -> L31, L48, L68 | none | PASS |
| Detailed P&L lines (std 28 + cons 29) | 57 | 57 | row sweep pages 4 & 6 | none | PASS |
| Summary-table lines (9 + 9) | 18 | 18 | row sweep page 3 | none | PASS |
| Segment rows (22 + 22) | 44 | 44 | row sweep pages 5 & 7 | none | PASS |
| Auditor paragraphs (cons 6 + std 4) | 10 | 10 | pages 8-10 | none | PASS |
| Consolidation entities | 5 | 5 | grep JV/Associate -> L385-389 (=L454-458) | none | PASS |
| Signature blocks | 6 | 6 | CS L82 + MD x3 + auditor x2 (UDIN x2 distinct, L497/L547) | none | PASS |

Diff vs A4 review: A4's LEDGER-RECONCILIATION PREAMBLE (L12) declares exactly this row set (9 notes / 1 footnote / 3 agenda / 57 P&L / 18 summary / 44 segment / 5 entities / 10 auditor / 6 signature / 0 turns / 0 slides) and states all rows reviewed. Every ledger table (TABLE 1-14) surfaces in A4: notes in Step 0D, P&L in Step 1A/1B, summary in Step 1 cross-checks, segment in SEGMENT ANALYSIS, entities in Con N2 / auditor read, auditor paras in AUDITOR REPORT READ, PAT-gap in the S-vs-C section, MoUs in Board Outcome. The two OCR_SUSPECT rows (L212 "2.13", L151 "2.14") are handled by the EPS correction memo (5.13/5.14), per task instruction not an error. Zero orphan rows; zero rows my fresh pass found that the ledger lacks.

COVERAGE: PASS.

---

## 2. ARITHMETIC AUDIT — independent recompute from raw extract lines

### 2A. PRIOR FINDING (loop-1) — consolidated 1C, recomputed from scratch

Consolidated inputs: PBT-before-exceptional L312, Dep L307, Finance L306, Other Income L299 (Q1FY26 OI = Total 810.30 − Rev 732.60 = 77.70; printed cell garbled). Formula per A4 L134: Op EBITDA = PBT(pre-exc) + Dep + Finance − OI; Core PBT ex-OI = PBT(pre-exc) − OI.

| Metric (cons) | Period | Raw inputs | My recompute | A4 value | Ties to L361 | Status |
|---|---|---|---|---|---|---|
| Operating EBITDA | Q1FY26 | 224.43+22.00+0.51−77.70 | **169.24** | 169.24 | — | PASS |
| Operating EBITDA | Q4FY26 | 204.96+48.76+5.37−154.89 | **104.20** | 104.20 | — | PASS |
| Operating EBITDA | FY26 | 745.80+114.71+7.14−423.88 | **443.77** | 443.77 | — | PASS |
| Operating EBITDA | Q1FY27 | 227.25+33.33+6.61−76.15 | 191.04 | 191.04 | — | PASS |
| Core PBT ex-OI | Q1FY26 | 224.43−77.70 | 146.73 | 146.73 | L361 146.74 | PASS |
| Core PBT ex-OI | Q4FY26 | 204.96−154.89 | 50.07 | 50.07 | L361 50.07 | PASS |
| Core PBT ex-OI | FY26 | 745.80−423.88 | 321.92 | 321.92 | L361 321.93 | PASS |
| Core PBT ex-OI | Q1FY27 | 227.25−76.15 | 151.10 | 151.10 | L361 151.13 | PASS |

The two headline consolidated Op EBITDA figures I was asked to recompute independently: **Q4FY26 = 104.20** and **FY26 = 443.77**. Both tie exactly to A4's revised 1C and to the consolidated segment Total Results at L361 (via Core PBT). The loop-1 standalone-contamination (previously 130.44 / 477.20 carried into the cons rows) is CORRECTED. PRIOR FINDING CLOSED.

### 2B. Standalone 1C (confirm the edit did not disturb the standalone rows)

Std inputs: PBT-pre-exc L191, Dep L187, Finance L186, OI L179.

| Metric (std) | Q1FY26 | Q4FY26 | Q1FY27 | FY26 | A4 | Status |
|---|---|---|---|---|---|---|
| Op EBITDA | 169.90 | 130.44 | 191.04 | 477.20 | match | PASS |
| Op EBITDA margin | 23.19% | 16.02% | 21.07% | 17.98% | match | PASS |
| Reported EBITDA (incl OI) | 247.19 | 285.85 | 267.19 | 901.08 | match | PASS |
| Core PBT ex-OI | 147.40 | 76.31 | 151.10 | 355.35 | match | PASS |
| Total tax (derived) | 60.56 | 40.56 | 64.24 | 311.07 | match | PASS |
| ETR (/reported PBT) | 26.95% | 15.50% | 28.27% | 23.89% | match | PASS |
| PAT margin | 22.40% | 27.17% | 17.98% | 37.34% | match | PASS |

Std cross-checks: Core PBT ex-OI Q1FY27 151.10 vs segment L238 151.13; Q1FY26 147.40 vs L238 147.41 — both tie (rounding). PASS.

### 2C. Consolidated ETR / PAT-margin rows

| Metric (cons) | Q1FY26 | Q4FY26 | Q1FY27 | FY26 | A4 | Status |
|---|---|---|---|---|---|---|
| PAT margin | 22.35% | 23.84% | 18.03% | 36.05% | match | PASS |
| ETR (/PBT incl JV share) | 27.00% | 17.29% | 28.22% | 24.54% | A4: 26.96 / 17.26 / 28.22 / 24.53 | PASS (rounding) |

Cons ETR: my recompute uses PBT after JV-share (L314+L316). A4's Q1FY26/Q4FY26/FY26 differ from mine by 0.01-0.04 pp (largest 0.04pp on Q1FY26), consistent with A4 using PBT-before-JV-share as denominator. Sub-rounding, non-headline cross-check row; not a gate failure.

### 2D. Step 2 YoY deltas (the critical downstream repoint check)

Standalone: Rev +23.76%, Op EBITDA +12.44% (169.90->191.04), margin −212bps, Dep +51.50%, Finance +1,222%, EBIT(op) +6.63% (147.90->157.71), OI −1.47%, Core PBT +2.51%, Reported PBT +1.14%, PAT −0.68%, EPS −0.58% — ALL recompute-tie.

Consolidated: Op EBITDA **+12.88%** off base **169.24** (not the old 169.90); Core Op PBT **+2.98%** off base **146.73** (not the old 147.40); Reported PBT (pre-JV) +1.26%; JV swing +0.52; PAT −0.21%; EPS −0.19% — ALL tie. The Step 2 consolidated growth rates are correctly repointed to the corrected Q1FY26 cons base. This was the primary downstream risk from the edit; it is clean.

### 2E. QoQ (Step 3), PAT bridge (Step 4), segment, S-vs-C gap

- QoQ: Rev +11.37%, Op EBITDA +46.46% (130.44->191.04), margin +505bps, PAT −26.30% — tie.
- PAT bridge: +174.04 rev, −152.90 op cost (loading +145.88, other +47.21, royalty +27.17, employee +5.70, inventory +5.97, less cess −79.03), = Op EBITDA +21.14, −11.33 Dep, −6.11 finance, −1.14 OI, +2.56 PBT, −3.68 tax, = PAT −1.12 (164.13->163.01) — closes exactly.
- Segment: Mining rev +22.73%, result +20.55%, margin −45bps; Power rev +134.90%, swung to (6.00); Mining assets +39.77% (+1,165.45); Power assets +5.12% — tie.
- S-vs-C PAT gap: Q1FY26 −0.36 (resid −0.26), Q4FY26 −27.09 (resid −26.76), FY26 −34.14 (resid −33.43), Q1FY27 +0.42 (zero resid) — tie. Other-Expense divergence +30.34 Q4 (212.81 vs 182.47), +33.43 FY26 (564.18 vs 530.75) — tie.

ARITHMETIC: PASS. No new arithmetic error was introduced by the edit.

### Minor annotation note (not a FAIL)
Row "Other Income / PBT (std)" FY26 cell shows 32.56% labeled "(of PBT-before-exceptional)"; the value 32.56% = 423.88/1301.88 is actually computed on PBT AFTER exceptional (the Q4 cell 59.37% = 155.41/261.74 likewise uses after-exceptional PBT). The number is arithmetically correct from stated raw lines; only the parenthetical basis label is imprecise. Non-headline, below materiality — logged for A4's awareness, not a gate failure.

---

## 3. VERIFICATION OF THE SPECIFIC FIX CLAIMS

- SEGMENT ANALYSIS "identical operating figures" claim: CORRECTED. The revised note (L268) now states the equality holds ONLY in Q1FY27 (Mining 208.07, Power (6.00), Total 151.13 tie on both pages) and explicitly diverges in Q4FY26/FY26, with cons Op EBITDA 104.20 vs std 130.44 and FY26 443.77 vs 477.20, cons Un-allocable (80.46) L360 vs std (54.22) L237 — all values verified against the extract. Confirmed.
- A3-02 STRENGTHENED not weakened: the divergence is now shown on the operating lines (Op EBITDA, Core PBT) and not only at PAT; Question 1 (L383), flag #4 (L475), monitorable #11 (L470), and the Top-3 ranking (L393) all carry the operating-line reinforcement. It is named as an open item routed to management Q1, not asserted. Confirmed strengthened.
- Downstream preserved: Step 2 YoY (repointed, verified 2D), PAT-gap section, EPS 5.13/5.14 baseline (L351), PROCEED WITH CAVEATS verdict, and all 8 management questions (Q1-Q8 mapped A3-01..A3-08) are intact. Confirmed.

---

## 4. ADVERSARIAL READ — three most positive claims, strongest bear counter each

1. CLAIM: "Revenue +23.76% YoY — strong top-line growth" (L162).
   BEAR (from same text): the growth did not reach the bottom line — PAT −0.68%, Core PBT ex-OI only +2.51%, Op margin −212bps, and Power revenue +134.9% was booked at an operating LOSS. SURVIVES? No — already fully incorporated (Step 2 diagnostics 3-4, verdict flag 1). Not a new graft.

2. CLAIM: "Sequentially, operations improved sharply — Op EBITDA +46.46% QoQ, margin +505bps" (L210).
   BEAR: the QoQ step is distorted by Q4FY26 base weakness (Power (40.98), tax credit 47.02, exceptional 30.02) and by Q1 pre-monsoon seasonality; not a clean trajectory. SURVIVES? No — already stated at L211. Not new.

3. CLAIM: "GST cess Rs 79.03 cr -> nil is a structural margin lift" (implied bull, Q2 / monitorable 8).
   BEAR: margin STILL contracted −212bps YoY despite the cess disappearing, i.e. the benefit was fully absorbed by loading/overburden inflation and may be temporary or price-offset. SURVIVES? No — already the core of diagnostic 2 and Question 2 (bear column). Not new.

No surviving uncaptured bear counter. Nothing to graft into A4.

---

## VERDICT

**COMPLETE.**

- Prior loop-1 finding CLOSED: consolidated 1C Op EBITDA and Core PBT ex-OI now carry the correct consolidated values, independently recomputed (Q4FY26 Op EBITDA 104.20; FY26 Op EBITDA 443.77; both tie to L361 via Core PBT). Standalone-value contamination removed.
- Coverage: all 9 ledger categories reconcile on a fresh grep pass; zero orphan rows, zero missing-from-ledger rows.
- Arithmetic: every derived metric recomputes within rounding, including the repointed Step 2 consolidated growth rates. No new error introduced by the edit. One sub-rounding cons-ETR difference (<=0.04pp) and one imprecise ratio-basis label logged as non-material, not gate failures.
- Adversarial: three strongest bear counters already present in the review; none survive as new.

No loop-back required.

```yaml
stage: A5-adversary
company: "GMDCLTD"
quarter: "Q1FY27"
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
