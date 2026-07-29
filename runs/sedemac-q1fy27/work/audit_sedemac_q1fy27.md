# A5 ADVERSARY / COMPLETENESS AUDIT — SEDEMAC Mechatronics Ltd — Q1 FY27

Auditor: A5 (fresh context; sees only A4 review + A1 extracts + A2 ledgers).
Verdict re-derived independently; A4/A3 cites checked, not trusted.
Inputs audited:
- Review: review_sedemac_q1fy27.md
- Extracts: extract_results (312 file-lines), extract_presentation (256 file-lines)
- Ledgers: ledger_results, ledger_presentation

---

## 1. COVERAGE AUDIT (fresh grep pass diffed against A2 ledgers)

### 1A. Results filing — fresh enumeration vs A2 count

| Category | A2 count | My fresh count | Basis (extract lines) | Orphan rows | Status |
|---|---|---|---|---|---|
| Agenda items | 1 | 1 | L42 (results approval only) | none | PASS |
| Auditor paras | 5 | 5 | L95, L98, L105, L113, L117 | none | PASS |
| Numbered notes | 6 | 6 | L263, L271, L285, L288, L291, L293 | none | PASS |
| P&L data rows | 23 | 23 | L174-219 (recounted row-by-row, see below) | none | PASS |
| Segment data rows | 17 | 17 | L237-259 (3 rev + 6 result + 4 asset + 4 liab) | none | PASS |
| Signatures | 3 | 3 | L56, L143, L304 | none | PASS |
| Consolidation entities | 0 | 0 | Note 5 L291 (no sub/assoc/JV) | none | PASS |

P&L 23 recount: Rev, OtherInc, TotInc, CoM, ChgInv, EmpBen, FinCost, D&A, OtherExp, TotExp, PBT, CurTax, DefTax, TotTax, PAT, DBO-remeas, tax-on-OCI, OCI-net, TCI, Paid-up, OtherEquity, EPS-Basic, EPS-Diluted = 23. Matches.
Segment 17 recount: rev(237,238,239)=3; result(242,243,244,245,246,247)=6; assets(250,251,252,253)=4; liab(256,257,258,259)=4 = 17. Matches.

### 1B. Presentation — fresh enumeration vs A2 count

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Slides | 8 | 8 | none | PASS |
| Numeric disclosures | 65 | 65 (accepted; slide-6 44-token reconciliation checks out) | none | PASS |
| Footnotes | 4 | 4 (F1,F2,F3,F4) | none | PASS |
| Outlook/forward claims | 15 | 15 (O1-O10a) | none | PASS |
| Cover-letter items | 12 | 12 (C1-C12) | none | PASS |

### 1C. Ledger-row → review coverage (every material row cited or blanket-reviewed)

- All 23 P&L rows appear in Step 1 data table (line-anchored). COVERED.
- Segment material rows: Mobility/Industrial revenue (Step 2/6, F12c), Mobility/Industrial results (F12c, Q4), all 4 asset rows + 3 of 4 liability rows (Step 5 table, line-anchored). COVERED.
- Segment RECONCILING rows (Total result 43.05 L244; Unallocable expenses -2.31 L245; Unallocable income 0.60 L246) are not individually cited but tie PBT (43.05-2.31+0.60=41.34) and are carried by the preamble blanket "all 40 line items reviewed." I independently confirmed the tie. ACCEPTABLE (immaterial reconciling lines, arithmetically closed).
- All 6 notes individually extracted in Step 0D. Note 5 (no subsidiary) → standalone-only correct; consolidated check satisfied-by-absence, NOT skipped. Verified against L291. No consolidated statement exists to have been dropped.
- A3 findings F8-F12c and A3-01..A3-10 all appear in the merged register (lines 371-389). COVERED.
- Forward claims O9/O10/O10a (El Nino / US-hurricane macro risk; "no adverse effect seen so far", L217-225): NOT elevated to any A3 finding, monitorable, or question. They are carried only by the numeric blanket "15 outlook claims reviewed." I judge this ACCEPTABLE: generic external-macro hedges with self-stated null impact legitimately produce no forensic finding, and the blanket is an explicit reviewed-no-finding marker permitted by the coverage rule. Recorded as an observation, not an orphan.
- A2 slide-6 ANOMALOUS_VALUE "1,008" (L182) and UNRESOLVED tokens: review claims "zero residual UNRESOLVED (A3 recovered visually)." I cannot see A3, so I reconciled it myself from the extract: 1,008 (Mobility) + 142 (Industrial, L172) = 1,150 ≈ TTM Q1FY27 revenue 1,151. The anomaly resolves to Mobility TTM Q1FY27 revenue. Not a material gap; none of the review's findings depend on it. ACCEPTABLE.

COVERAGE VERDICT: no orphan rows; no rows in my fresh pass absent from the ledger. PASS.

---

## 2. ARITHMETIC AUDIT (every derived metric recomputed from raw extract lines)

Source lines cited are A1 results-extract embedded line numbers.

| Metric | A4 value | My recompute | Source lines | Status |
|---|---|---|---|---|
| Revenue YoY | +42.51% | 309.77/217.36−1 = +42.51% | L174 | MATCH |
| Op EBITDA Q1FY26 | 43.09 | 30.17+13.09+2.43−2.60 = 43.09 | L189/185/184/175 | MATCH |
| Op EBITDA Q1FY27 | 59.17 | 41.34+16.37+2.32−0.86 = 59.17 | same | MATCH |
| Op EBITDA Q4FY26 | 60.49 | 41.92+17.89+1.31−0.63 = 60.49 | same | MATCH |
| Op EBITDA FY26 | 216.93 | 150.19+63.48+8.53−5.27 = 216.93 | same | MATCH |
| Op EBITDA margin Q1FY26/Q1FY27 | 19.82% / 19.10% | 43.09/217.36=19.82%; 59.17/309.77=19.10% | L174 | MATCH |
| Op margin bridge | −72 bps | 19.82−19.10 = 0.72pp | — | MATCH |
| Reported EBITDA margin Q1FY26/Q1FY27 | 21.02% / 19.38% | 45.69/217.36=21.02%; 60.03/309.77=19.38% | L174/189/185/184 | MATCH |
| Reported margin bridge | −164 bps | 21.02−19.38 = 1.64pp | — | MATCH |
| ETR Q1FY26 | 43.42% | 13.10/30.17 = 43.42% | L194/189 | MATCH |
| ETR Q1FY27 reported | 19.42% | 8.03/41.34 = 19.42% | L194/189 | MATCH |
| ETR Q1FY27 ex-reversal | ~26.6% | (8.03+2.98)/41.34 = 26.63% | L194/189/285 | MATCH |
| Core PBT ex-OI YoY | +46.83% | 40.48/27.57−1 = +46.83% | L189/175 | MATCH |
| Reported PBT YoY | +37.03% | 41.34/30.17−1 = +37.03% | L189 | MATCH |
| PAT YoY (reported) | +95.14% | 33.31/17.07−1 = +95.14% | L196 | MATCH |
| Tax swing YoY | +5.07 (13.10→8.03) | 13.10−8.03 = 5.07 | L194 | MATCH |
| Of which base-ETR normalization | +2.09 | 5.07−2.98 = 2.09 | L194/285 | MATCH |
| Clean PAT Step A (strip one-off) | 30.33 → +77.7% | 33.31−2.98=30.33; 30.33/17.07−1=+77.68% | L196/285 | MATCH |
| Clean PAT Step B (tax-normalized) | +37.0% | 30.33/22.14−1=+37.0% (=PBT growth) | derived | MATCH |
| Normalized PAT Q1FY26 | 22.14 | 30.17×(1−0.2663) = 22.14 | L189 | MATCH |
| Clean EPS ex-reversal | ~6.87 | 30.33/4.417 = 6.87 (4.417cr sh = 44.17/10) | L210 | MATCH |
| Total segment assets QoQ | +129.36 / +15.90% | 943.06−813.70=129.36; /813.70=15.90% | L253 | MATCH |
| Mobility assets QoQ | +181.51 / +27.75% | 835.56−654.05=181.51; /654.05=27.75% | L250 | MATCH |
| Mobility revenue QoQ | +8.77% | 281.04/258.39−1 = +8.77% | L237 | MATCH |
| Unallocable (cash) assets QoQ | −56.85 / −66.6% | 28.55−85.40=−56.85; /85.40=−66.6% | L252 | MATCH |
| Total liabilities QoQ | +85.26 / +23.39% | 449.76−364.50=85.26; /364.50=23.39% | L259 | MATCH |
| Unallocable liab QoQ | +53.75 / +78.2% | 122.49−68.74=53.75; /68.74=78.2% | L258 | MATCH |
| TCI Q1FY27 (comparator) | 32.13 | L206 direct | L206 | MATCH |
| Net-worth proxy Q4/Q1 | 449.20 / 493.30 | 813.70−364.50; 943.06−449.76 | L253/259 | MATCH |
| F11 equity gap | ~11.96 | 493.30 − (449.20+32.13+0.01=481.34) = 11.96 | L214/206/210/253/259 | MATCH |
| Industrial rev YoY | −15.7% | 28.73/34.10−1 = −15.75% | L238 | MATCH |
| Industrial result YoY | −18.2% | 3.96/4.84−1 = −18.18% | L243 | MATCH |
| TTM units YoY | +52.9% | 4,201,939/2,747,383−1 = +52.94% | deck L107/L112 | MATCH |
| Deck EBITDA ≈ Reported EBITDA | 46/60 ≈ 45.69/60.03 | confirms deck path = reported EBITDA | deck L142 | MATCH |
| CMP multiple | ~84x | 1971/23.52(dil) = 83.8x | Notion/L219 | MATCH (rounding) |

ARITHMETIC VERDICT: every stated computation reproduced from raw extract lines. Zero mismatches above rounding. PASS.

Specifically confirmed the four items the task flagged: +42.51% revenue, the dual margin bridge (19.82→19.10 op / 21.02→19.38 rep), clean PAT +37% vs reported +95.14% with the +77.7% intermediate, clean EPS 6.87, and the ETR set (19.4% reported / 26.6% ex-reversal / 43.4% Q1FY26). All reproduce.

---

## 3. ADVERSARIAL READ (three most-positive A4 claims; strongest bear from the SAME extract)

**Positive claim A — "Revenue +42.51% YoY STRONG; positive mix, no ASP erosion" (Step 2 diag 1; Gate #2 revenue PASS).**
Bear counter (same extract): Industrial revenue −15.7% YoY (28.73 vs 34.10, L238) and result −18.2% (L243); growth is single-leg Mobility (~91%); sequential deceleration is stark — total revenue only +7.67% QoQ and Mobility only +8.77% QoQ vs the +42.5% YoY optic off a soft Q1FY26 base.
Survives? NO. Already incorporated: F12c, watchlist item 7 (AMBER→RED), Q4, and Step 3 QoQ deceleration / A3-03. No graft required.

**Positive claim B — "Core operating PBT +46.83% YoY is the single cleanest operational-health test, genuinely strong" (Step 2 diag 3).**
Bear counter (same extract): On a sequential basis core PBT ex-OI FELL 41.29 (Q4FY26) → 40.48 (Q1FY27), −2.0% QoQ, and operating EBITDA margin −192bps QoQ / −72bps YoY — the engine is flat-to-down sequentially; the +46.83% is amplified by the low year-ago base.
Survives? NO. Step 3 already shows the 41.29→40.48 QoQ decline and −192bps QoQ; Step 8C names margin-vs-19.1% as the secondary Q2 metric. No graft required.

**Positive claim C — "Other Income concentration fell (OI/PBT 8.62%→2.08%); operating line HIGH QUALITY, not propped by treasury" (Step 2 diag 6).**
Bear counter (same extract): Earnings quality did not improve, it MOVED — from other-income dependence to tax dependence (Rs2.98cr reversal, Note 3, L285) plus a Rs1.58cr DBO remeasurement charge below the line (L200, larger than all of FY26's 0.39). Reported PAT +95% is ~+37% clean; "high quality" holds only for the narrow operating line, not reported earnings.
Survives? NO. Review explicitly states "the earnings-quality problem is tax, not Other Income," quantifies clean PAT +37% once (F8↔A3-04, no double count), and F9 flags the DBO. No graft required.

Additional adversarial checks demanded by the task:
- **Double-count of F8 vs A3-04?** NO. Step 4 and the register reconcile them as "one tax story, counted once"; the clean-PAT +37% is derived a single time. Flags list them separately as flags but the quantification is not additive. Correct.
- **Is "DETERIORATING" cash-conversion overstated given no Q1 CFO?** The call rests on a balance-sheet asset build that mixes capex/RoU (an investing use, supported by D&A +25%) with working capital, compared against a single quarter's TCI — an inherently imperfect proxy. BUT the review already carries this exact hedge ("leaning growth-induced rather than structural distress," CFO/PAT INDETERMINATE, thesis-broken NOT fired), and caps the verdict per house rule. The negative is calibrated, not overstated. No graft required.
- **"Clean PAT +37%" sound, or conflates tax-normalization with growth?** Sound. Step B equalizes ETR across BOTH periods and the result equals underlying PBT growth (+37.03%) by construction — it isolates growth from the tax tailwind rather than conflating them. Verified arithmetically.
- **Every FORWARD-SIGNAL/AMBIGUOUS finding produced a management question; count = 12?** Verified. 9 FORWARD-SIGNAL (F8,F10,F12a,F12b,F12c,A3-01,A3-05,A3-08,A3-09) + 5 AMBIGUOUS (F9,F11,A3-03,A3-04,A3-07) = 14 findings, each mapped to ≥1 of the 12 questions (Q1 covers F12a/F12b/A3-06; Q3 covers A3-01/A3-08; Q4 covers F12c/A3-05; Q8 covers A3-02/A3-03). Count of 12 is correct.

ADVERSARIAL VERDICT: three positive claims tested; every bear counter is already incorporated in the review. ZERO surviving counters requiring graft. The review is symmetric and self-adversarial. PASS.

---

## VERDICT

**COMPLETE.**

- Coverage: no orphan ledger rows; no fresh-pass rows missing from the ledgers; standalone-only correct (Note 5) and consolidated check satisfied-by-absence, not skipped.
- Arithmetic: all ~35 derived metrics reproduced from raw extract lines; zero mismatches above rounding.
- Adversarial: no surviving bear counter; no tax double-count; clean-PAT derivation sound; 12-question count verified.

Loop-back: none. Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "SEDEMAC"
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
