# A5 ADVERSARY / COMPLETENESS AUDIT — Finkurve Financial Services Ltd (Arvog) — Q1 FY27 (LOOP 2, FINAL)

Independent re-derivation. Inputs seen: A4 review + A1 extracts (results / presentation / reg32) + A2 ledgers only. Every number below re-footed from the cited raw line; A4's and A3's cites were checked, not trusted.

Line-anchor convention verified: results `L###` = extract cat-n file line (= extract embedded line + 84); deck `S##/L###` = extract embedded line; reg32 `R-L##` = extract embedded line. Cross-checked on Interest income (L288 → 7,478.68), fee expense (S30/L938 → 19.70), reg32 (R-L54 → 141.50). Consistent.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate) — PASS

| Brief part | Location | Status |
|---|---|---|
| (1) Summary narrative (10-20 lines) | review L315-317 (~15 lines) | present, real content |
| (2) SECTOR INTELLIGENCE | review L319-321 | present, real content |
| (3) BUSINESS-MODEL INTELLIGENCE | review L323-325 | present, real content |
| (4) COMPETITION INTELLIGENCE | review L327-329 | present, real content |

All four labelled headings exist and carry substantive, non-placeholder content. Gate PASSES.

---

## 1. LOOP-1 GAP CLOSURE — re-derived from raw lines (all four CLOSED)

**Gap 1 — Fee-and-commission expense / expense-stack footing / "ties exactly" retraction / Q21.**
Re-footed the Q1 FY27 expense stack from the filing's own raw Lakhs (L295-L301), using the deck's 19.70 (1,970 L) in place of the filing's printed 1,363.74 (13.64, L296):
2,672.31 + 1,970.00 + 20.38 + 1,347.08 + 113.18 + 338.98 = **6,461.93 L ≈ 6,461.66 L (Total Expenses, L302)** — foots (0.27 L = deck 2-dp rounding). Exact residual that makes the filing's own total foot = 6,461.66 − (2,672.31+20.38+1,347.08+113.18+338.98) = 1,969.73 L = **19.70 Cr**. PBT check: Total Income 7,582.18 (L293) − Total Expenses 6,461.66 (L302) = 1,120.52 L = **11.21 Cr (L303)** — ties. Footing the same stack with the printed 13.64 sums to 5,855.67 L = 58.56 Cr, a 6.06 Cr shortfall — confirming the localisation.
Corroboration that 19.70 (not 13.64) is correct: deck independently prints Total Expenses 64.62 AND PBT 11.21 AND fee expense 19.70 (S30/L938/L944/L945); and the OTHER three fee-expense periods tie filing-to-deck (Q1FY26 12.73, Q4FY26 22.78, FY26 69.73). The divergence is isolated to the single Q1FY27 cell. A4's "filing misprint" call is sound and is NOT an estimate (it is the exact residual + cross-document print), and it is not silently "fixed" — it is flagged to management. Preamble "ties exactly" claim is explicitly RETRACTED (review L27). Q21 exists (review L261; YAML questions_for_management #21). **CLOSED.**

**Gap 2 — RoALA Q1 FY27 = 2.9%.** Deck slide 29 RoALA series (S29/L915-917): 4.2% / 3.9% / 3.7% / 3.3% / **2.9%** (Q1FY26→Q1FY27, declining). Review cell = 2.9% (review L104); tripwire text "RoALA declining 4.2->2.9%" (review L273/L278). Value confirmed on the slide; A4's line cites match A2's line attribution. **CLOSED.**

**Gap 3 — Net-worth decomposition period-matched to Jun'26.** Net Worth (Jun'26) = 35,436.80 L = 354.37 Cr (L365). Paid-up equity (Jun'26) = 1,401.28 L = 14.01 Cr (L310). Implied Other Equity (Jun'26) = 354.37 − 14.01 = **340.36 Cr** (review L187, correctly labelled "implied"). The Mar'26 audited Other Equity 33,089.57 L = 330.90 Cr (L311 / deck S32/L1005) is explicitly kept as a Mar'26 component and is **NOT** added to the Jun'26 total. No period mismatch remains. **CLOSED.**

**Gap 4 — CRAR halved 57.3%→26.6%.** Deck slide 29 Capital Adequacy series (S29/L901-905): 57.3% / 47.1% / 39.1% / 31.0% / **26.6%** (Q1FY26→Q1FY27); filing CRAR 26.63% (L385). 57.3→26.6 is more than a halving; over-5-qtr drop = 3,070 bps; QoQ (31.0→26.63) = 437 bps — all re-verified. Present in Step 5L (review L175/L179), Capital & Leverage (L187), and bear framing (brief L317, competition L329, flags L387). **CLOSED.**

---

## 2. COVERAGE AUDIT (fresh enumeration vs A2 ledgers vs A4 review)

| Category | A2 count | My fresh count | Orphan rows (ledger not in A4) | Status |
|---|---|---|---|---|
| RESULTS — agenda items | 11 | 11 (L107-159) | none | ok |
| RESULTS — review-report paras | 5 | 5 (L203-256) | none | ok |
| RESULTS — security-cover paras | 9 | 9 (L420-515) | none | ok |
| RESULTS — notes | 8 | 8 (L316-387) | none | ok |
| RESULTS — P&L line items | 23 | 23 (L288-314) | none | ok |
| RESULTS — CLA sub-table rows | 10 | 10 (L331-340) | none | ok |
| RESULTS — ratios rows | 26 | 26 (L360-385) | none | ok |
| RESULTS — Appendix I rows | 30 | 30 (14 asset + 14 liab + 2 cover) | none (data-legibility NOT_FOUNDs disclosed) | ok |
| RESULTS — Appendix I footnotes | 9 | 9 | none | ok |
| RESULTS — Annexure 3 fields | 15 | 15 | none | ok |
| RESULTS — Annexure 4 fields | 15 | 15 | none | ok |
| RESULTS — signature blocks | 7 | 7 | none | ok |
| RESULTS — total disclosure units | 176 | 176 | none | ok |
| PRESENTATION — slides | 37 | 37 ([page 1]-[page 37]) | none | ok |
| PRESENTATION — mgmt numbers | 253 | 253 | none | ok |
| PRESENTATION — named entities | 78 | 78 | none | ok |
| PRESENTATION — zero-standing | 7 | 7 | none | ok |
| PRESENTATION — footnotes | 5 | 5 | none | ok |
| PRESENTATION — guidance statements | 1 | 1 (S21/L675) | none | ok |
| REG32 — disclosure units | 41 | 41 (16+14+7+4) | none | ok |

Review preamble counts (176 / 37 / 253 / 78 / 7 / 5 / 1 / 41) reconcile exactly to the three ledgers. All 29 A3 findings are individually listed as incorporated (review L21-23) — RESULTS ×13, PRESENTATION ×13, REG32 ×3 = 29 — and each maps to a Step, an earnings-quality item, a management question, a monitorable, or a flag. Every material ledger flag (STANDALONE_ONLY, AUDITOR_CHANGE, RELATED_PARTY/Augmont, DIRECTOR_AGE_75, EPS anomaly + cross-table mismatch, Annexure-4 199>135, monitoring-agency inconsistency, Stage-ECL NOT_FOUND, deferred-tax sign-flip, off-book AUM footnote, CRAR/RoALA/LTV trends) is addressed in A4.
My fresh grep pass surfaced **no row the ledger lacks** and **no ledger row absent from A4**.

**Coverage gaps: 0. Orphan rows: 0. Missing-from-ledger: 0.**

---

## 3. ARITHMETIC AUDIT (recomputed from raw extracted numbers)

| Metric | A4 value | My recompute | Source lines | Status |
|---|---|---|---|---|
| NII Q1FY27 | 48.07 | 74.79 − 26.72 = 48.07 | L288/L295 | ok |
| NII Q1FY26 / Q4FY26 / FY26 | 19.52 / 46.19 / 155.43 | 19.52 / 46.19 / 155.43 | L288/L295 | ok |
| Interest income YoY | +181.2% | (74.79−26.60)/26.60 = 181.2% | L288 | ok |
| NII YoY | +146.3% | 28.55/19.52 = 146.3% | calc | ok |
| Finance cost YoY | +277.4% | 19.64/7.08 = 277.4% | L295 | ok |
| Total rev-from-ops YoY | +88.3% | 35.22/39.88 = 88.3% (deck 88.32) | L291/S30 | ok |
| PBT YoY | +64.1% | 4.38/6.83 = 64.1% (deck 64.06) | L303/S30 | ok |
| PAT YoY | +65.8% | 3.35/5.09 = 65.8% (deck 65.78) | L305/S30 | ok |
| Fee-exp YoY (corrected) | +54.8% | (19.70−12.73)/12.73 = 54.7% | S30/L938 vs L296 | ok |
| PPOP Q1FY27 / FY26 / Q4 / Q1FY26 | 11.41 / 56.77 / 17.52 / 11.61 | 11.21+0.20 / 34.60+22.17 / 10.42+7.10 / 6.83+4.78 | L303/L298 | ok |
| PPOP YoY | −1.7% | −0.20/11.61 = −1.7% | calc | ok |
| Expense-stack foot (corrected) | 64.61≈64.62 | 6,461.93 L ≈ 6,461.66 L | L295-302 | ok |
| PBT foot | 11.21 | 7,582.18 − 6,461.66 = 1,120.52 L | L293/L302/L303 | ok |
| ETR Q1FY27 / Q1FY26 | 24.7% / 25.5% | 2.77/11.21 / 1.74/6.83 | L304/L303 | ok |
| PAT bridge (NII +28.55; oth/fee −12.41; opex −16.35; prov +4.58; tax −1.03) | PAT +3.35 | 28.55−12.41−16.35+4.58−1.03 = 3.34≈3.35 | Step 4 | ok |
| Opex Q1FY27 (corrected) | 37.69 | 19.70+13.47+1.13+3.39 = 37.69 | S30/L938,L299-301 | ok |
| Normalised PBT / haircut | ~5.87 / ~47.6% | 11.41−5.54 = 5.87; 5.34/11.21 = 47.6% | L298/L303 | ok |
| Credit cost Q1FY27 annualised | ~0.06% | 0.20×4/1,270.4 = 0.063% | L298/S7 | ok |
| Cost-to-income Q1FY27 / Q1FY26 | 76.8% / 64.8% | 37.69/49.11 = 76.7%; 21.34/32.97 = 64.7% | calc | ok (proxy) |
| AUM YoY / tonnage YoY | +134.5% / +46.6% | 728.6/541.8; 371.3/796.2 | S7/L176,178 | ok |
| Employee YoY / QoQ | +240% / +150.8% | 9.51/3.96; 8.10/5.37 | L299 | ok |
| CRAR halving / 5-qtr / QoQ bps | 57.3→26.6; −3,070; −437 | 30.7pt; 31.0−26.63=4.37pt | S29/L901-905, L385 | ok |
| RoALA Q1FY27 | 2.9% | slide 29 last point | S29/L917 | ok |
| LTV QoQ | +510 bps (72.2→77.3) | 5.1 pt | S28/L881-884 | ok |
| Net-worth decomposition | 14.01 + 340.36 = 354.37 | 14.01 + (354.37−14.01) | L310/L365 | ok |
| NCD excess / reg32 gap | 199−135 = 64; 141.50−30 = 111.50 | 64; 111.50 | L737/L758; R-L54/L77 | ok |
| GNPA / NNPA (Cr) | 6.66 / 5.96 | 665.65 L / 596.11 L ×0.01 | L380/L382 | ok |

Every derived metric ties to its cited raw line within rounding. **Arithmetic errors: 0.**

Non-material notes (not failures): deck chart-label line cites for RoALA/RoAE/CRAR are approximate (A2 itself flagged those charts `CHART_LABEL_AMBIGUOUS`), but the *values* A4 uses are correct and on-slide. A4's assignment of RoAE 9.4% to Q1FY27 sits on an A2-flagged ambiguous chart; the review's independent "annualised ~10%" (8.44×4 / 354.37 ≈ 9.5%) corroborates it, so it does not affect any conclusion.

---

## 4. ADVERSARIAL READ (strongest bear counter to A4's three most positive claims, from the same extract)

The review is already predominantly bearish; the test is whether any bear counter to its residual positives SURVIVES and is NOT yet incorporated (which would force a graft back to A4).

1. **Positive: "CRAR 26.63% — capital ample, above regulatory minimum" (L175/L187).**
   Bear counter (same extract): CRAR HALVED 57.3%→26.6% in a year (S29/L901-905) while D/E ran 0.73→2.88 (S7/L184; L360), the board enabled Rs 5,000 Cr borrowing power (L148) toward a 4-4.5x target, and PCR is only 10.45% on a rising GNPA. "Ample" describes the level, not the drawdown. **SURVIVES — already grafted** (Step 5L, Capital & Leverage, brief, competition, flags). No new graft required.

2. **Positive: "Cost of borrowing improved to 10.2%, −90 bps" (L174/L183).**
   Bear counter: the 10.2% is a single unbasised charted point (S24/L729); on the filing's own numbers finance cost rose +277% vs interest income +181%, so NII grew only +146% and the blended/weighted cost of the incremental leverage is RISING as the marginal-rate print falls. **SURVIVES — already incorporated** (Step 3.3, spread analysis, Q2). No new graft required.

3. **Positive: "Collection efficiency 98.0% holding / the only counter-signal" (L168/L179).**
   Bear counter: on a 96%-gold, bullet/renewal book, collection efficiency does not capture the price/LTV lever; GNPA still rose ~6x and LTV hit 77.3% (highest in series) despite 98% collection, so a stable collection print gives no comfort on the actual risk driver. **SURVIVES — substantially incorporated** (Step 5L(c)/(d) explicitly subordinates the 98% to the LTV/price risk). No new graft required.

Adversarial challenges constructed: 3. Surviving counters requiring NEW incorporation into A4: **0** (all three already present in the review).

---

## 5. VERDICT

**COMPLETE.**

- All four loop-1 gaps independently re-derived and confirmed CLOSED.
- Deliverable-completeness gate: PASS (all four plain-language-brief parts present and substantive).
- Coverage gaps: **0** (176 + 37/253/78/7/5/1 + 41 all reconcile; no orphan rows, none missing from ledger; all 29 A3 findings incorporated).
- Arithmetic errors: **0** (every derived metric re-footed to its cited raw line within rounding; the corrected expense stack foots to Total Expenses 64.62 and PBT 11.21).
- Adversarial challenges: **3 constructed, 0 surviving un-incorporated** (all three bear counters already in A4).
- No new error was introduced by the loop-2 edits, and no other material gap is uncovered.

Confirmation: every material unit across the three documents is covered, and every number in A4's tables ties to its cited line (the sole cross-document divergence — the filing's 13.64 fee-expense print — is correctly localised to that one cell, resolved to 19.70 by the filing's own foot and the deck, and put to management as Q21). This review may proceed to Notion save.

```yaml
stage: A5-adversary
company: "finkurve"
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
