# A5 ADVERSARY / COMPLETENESS AUDIT — SPAPPAREL Q1 FY27

**Auditor:** A5 (Opus 4.8), fresh context. Inputs seen: A4 review, A1 extract, A2 ledger only.
**Re-derivation basis:** every number below recomputed from `extract_results_spapparel_q1fy27.txt` raw cells (Rs Millions x0.1 -> Cr). A4/A3 cites checked, not trusted.
**Verdict:** COMPLETE.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

PLAIN-LANGUAGE BRIEF located at Section 5 (review L432-448). All four labelled parts present, non-empty, real content (not placeholder):

| Part | Heading present | Location | Content check | Status |
|---|---|---|---|---|
| 1. Summary narrative | yes | L434-436 | Dense ~18-line paragraph; walks revenue decline, margin story, deleveraging split, S-vs-C gap, unreviewed loss, cash-conversion unknown, verdict PROCEED WITH FLAGS | PRESENT |
| 2. SECTOR intelligence | yes | L438-440 | Tirupur kidswear export context, China+1/UK-India FTA, FX + loss-making entity headwinds, provenance-flagged | PRESENT |
| 3. BUSINESS-MODEL intelligence | yes | L442-444 | Three revenue engines, parent-vs-subsidiary leverage split, ~8% payout reinvestment drift, export volumes | PRESENT |
| 4. COMPETITION intelligence | yes | L446-448 | Win/lose vs KPR/Gokaldas/Pearl, sub-scale UK front-end, subsidiary-drag risk, provenance-flagged | PRESENT |

Gate result: PASS. No missing or empty part.

---

## AUDIT 1 — COVERAGE (independent re-enumeration vs A2 ledger)

Fresh block-scoped sweep of the extract, diffed against the A2 count test:

| Category | A2 count | My fresh count | Basis | Orphan rows | Status |
|---|---|---|---|---|---|
| notes | 12 | 12 | SA notes L392/395/397/400/405 (5) + Consol L575/577/579/581/583/586/588 (7) | none | MATCH |
| line_items | 57 | 57 | SA 27 (P&L 18 + OCI 9) + Consol 30 (P&L 20 + OCI 10); zero-standing row L357 carried, TCI wrap L384/386 merged | none | MATCH |
| zero_standing | 1 | 1 | SA tax note (b) prior-year provision L357, all-dash 4 periods | none | MATCH |
| agenda_items | 7 | 7 | Board letter items 1-7, L33-86 | none | MATCH |
| auditor_paras | 11 | 11 | SA 4 (L272/277/282/292) + Consol 7 (L424/430/436/445/464/475/485) | none | MATCH |
| entities | 9 | 9 | Consol auditor list a-i, L447-455 | none | MATCH |
| annexure_items | 9 | 9 | Split-particular rows L128-158 | none | MATCH |
| signature_blocks | 4 | 4 | K.Vinodhini CS; Gururaj SA; Gururaj Consol; Sundararajan/Balaji | none | MATCH |

**No row my fresh pass found that the ledger lacks. No count divergence -> no A2 loop-back.**

**Orphan test (ledger row present but absent from A4).** Every material disclosure unit is cited or dispositioned in A4:
- Agenda items 2-7 -> Step 2.7 table (L326-332).
- Annexure split particulars incl. post-split count 12,56,94,415 -> Step 2.7 item 3 (verified 2,51,38,883 x 5 = 12,56,94,415).
- Consol auditor paras 5/6/7 -> Section 2.7 verbatim (L342-349).
- OCI / cash-flow-hedge lines (L561/565) -> Q5.
- Ritz acquisition Note C-4 (L581-582) -> Q3 / Step 0D C-4.
- Minority interest L566, deferred tax L358/L546, single-segment notes -> consol table / Step 4 / Section B.
- INTER_STATEMENT_MISMATCH (Q1FY26 consol paid-up 250.03 vs SA 260.93) -> Step 0C via A3-08 typo resolution.
- UNLABELED_SUBTOTAL / +10.0m standalone gap (L348/L353) -> Q7.
- Cosmetic-only flags not requiring a finding (ANNEXURE_LABEL_MISMATCH, LABEL_MISMATCH formula-vs-S.No, ARITHMETIC_CHECK_UNVERIFIABLE on garbled Q1FY26 TCI cell) are prior-period/OCR artefacts, correctly not elevated.

**Forward-signal / ambiguous -> question mapping (A3 findings via A4's classification):**
FORWARD-SIGNAL A3-02(Q2,Q9), A3-03(Q1,Q9), A3-04(Q6,Q8), A3-06(Q4), A3-07(Q5), A3-09(Q6), A3-12(Q3) — all 7 produced >=1 question. AMBIGUOUS A3-05(Q1), A3-11(Q7) — both produced a question. No orphan finding.

Coverage result: PASS. No orphan rows, no missing-from-ledger rows.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw extract cells)

All values Cr = filed Millions x0.1. Spot of the full recompute:

| Metric | A4 value | My recompute | Source lines | Status |
|---|---|---|---|---|
| SA Op EBITDA Q1FY27 | 46.77 | 350.13+106.02+24.21-12.59 = 467.75m = 46.77 | L354/351/350/341 | MATCH |
| SA Op EBITDA Q1FY26 | 44.56 | 290.98+95.28+72.12-12.83 = 445.55m = 44.56 | L354/351/350/341 | MATCH |
| SA Op EBITDA margin Q1FY27 | 17.0% | 46.77/275.12 = 17.00% | L340 | MATCH |
| SA margin YoY | +160 bps | 17.00 - 15.38 = +162 bp | — | MATCH |
| SA ETR Q1FY27 | 24.2% | 84.76/350.13 = 24.21% | L359/354 | MATCH |
| SA ETR Q1FY26 | 31.6% | 92.08/290.98 = 31.64% | L359/354 | MATCH |
| SA Revenue YoY | -5.0% | 275.12/289.68-1 = -5.03% | L340 | MATCH |
| SA Finance-cost YoY | -66.4% | 24.21/72.12-1 = -66.4% | L350 | MATCH |
| SA Core PBT YoY | +21.3% | 33.75/27.82-1 = +21.3% | L354/341 | MATCH |
| SA PAT YoY | +33.4% | 265.37/198.90-1 = +33.4% | L360 | MATCH |
| SA PAT bridge total | +6.65 | 265.37-198.90 = 66.47m = +6.65 | L360 | MATCH |
| SA bridge: EBITDA/dep/fin/OI/tax | +2.21/-1.07/+4.79/-0.02/+0.73 | +2.22/-1.07/+4.79/-0.02/+0.73 | — | MATCH (sums to +6.65) |
| Consol Op EBITDA Q1FY27 | 61.37 | 368.21+132.37+148.55-35.50 = 613.63m = 61.36 | L536/533/532/521 | MATCH (rnd) |
| Consol Op EBITDA Q1FY26 | 52.92 | 314.84+112.94+117.82-16.28 = 529.32m = 52.93 | L536/533/532/521 | within rounding (A4 52.92 vs 52.93) |
| Consol margin Q1FY27 | 15.3% | 61.36/401.08 = 15.30% | L520 | MATCH |
| Consol margin YoY | +220 bps | 15.30 - 13.12 = +218 bp | — | MATCH |
| Consol ETR Q1FY27 | 30.6% | 109.75/358.49 = 30.61% | L547/540 | MATCH |
| Consol Revenue YoY | -0.6% | 401.08/403.44-1 = -0.59% | L520 | MATCH |
| Consol Finance-cost YoY | +26.1% | 148.55/117.82-1 = +26.08% | L532 | MATCH |
| Consol PAT YoY | +20.4% | 248.74/206.55-1 = +20.43% | L548 | MATCH |
| Consol PAT bridge total | +4.21 | 248.74-206.55 = 42.19m = +4.22 | L548 | MATCH |
| Consol bridge EBITDA component | +8.45 | 61.36-52.93 = +8.43 | — | within rounding (see NOTE) |
| S-vs-C gap Q1FY26/Q4FY26/Q1FY27/FY26 | +0.77/-2.76/-1.66/+13.11 | +0.77/-2.76/-1.66/+13.10 | L360 vs L548 | MATCH (rnd) |
| S-vs-C gap %-of-SA | +3.8/-12.9/-6.3/+14.9 | +3.9/-12.9/-6.3/+14.9 | — | MATCH |
| Unreviewed rev share (paras 5+6) | ~16% | 654.39/4010.76 = 16.3% | L466/477/520 | MATCH |
| Para-6 loss as % consol PAT | ~30.1% | 74.84/248.74 = 30.09% | L478/548 | MATCH |
| Dividend payout on SA EPS 35.00 | ~8.6% | 3.00/35.00 = 8.57% | L388 | MATCH |
| Post-split paid-up count | 12,56,94,415 | 2,51,38,883 x 5 = 12,56,94,415 | L147 | MATCH |

**NOTE (documented, not a fail).** The consolidated PAT bridge (Step 4B) components as A4 lists them sum to +4.32 Cr against the correct stated total +4.21 Cr, a ~0.11 Cr residual. Root cause is fully traceable and not an A4 miscalculation of any metric: (i) the EBITDA component is double-rounded to +8.45 where raw is +8.43 (0.02), and (ii) the filing's own consolidated PBT carries a flagged 1.00m internal inconsistency (368.21 pre-assoc - 8.72 associate = 359.49, but printed PBT L540 = 358.49 — the A2 `ARITHMETIC_MISMATCH` on the consolidated PBT row). Every individual A4-derived metric reconciles to raw within rounding, and the "~50% below-EBITDA leakage" narrative is robust to the residual. This is a source-data artefact already enumerated by A2, not an A4 arithmetic error, so it does not fail the gate.

**Also observed (non-blocking):** A1 header states 565 lines / A2 repeats 565, while the extract runs to L601; A4's cited line numbers nonetheless resolve correctly against actual positions (all 35 table cites verified). No downstream impact.

Arithmetic result: PASS. No mismatch above rounding tolerance.

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims, strongest bear from same extract)

**Positive 1 — "Consolidated Op EBITDA margin +220 bps to 15.3%, the cleanest positive in the print" (L164, L177).**
Strongest bear from the extract: the step-up sits on flat/declining revenue (Consol -0.6%, SA -5.0%), the group added Ritz mid-quarter (C-4, L581-582) so scope is not like-for-like, prior periods were regrouped (C-7, L588), and part of the EBITDA base is the Rs 452.55m-revenue / Rs 74.84m-loss slice that no auditor reviewed (para 6, L475-483). **Counter does NOT survive as new material** — A4 already states margin is mix/cost-driven not volume-driven, flags the non-like-for-like scope, and sets a ">=15% must hold" structural test (Step 3, L213/L315).

**Positive 2 — "Standalone PAT +33.4% YoY, record PAT" (L155).**
Strongest bear: 72% of the gain is the finance-cost collapse (72.12 -> 24.21m, L350) plus a lower ETR (31.6% -> 24.2%), on a -5% revenue decline; normalise finance costs and ~4.8 Cr/qtr of PAT evaporates. **Does NOT survive as new** — this is A4's own Step 4A central read, verbatim.

**Positive 3 — "Subsidiaries added Rs 13.1 Cr to FY26 PAT; group out-earned parent ~15%" (Step 4C, L261).**
Strongest bear: the FY26 accretion is backward-looking and already reversed — both most-recent quarters (Q4FY26 -2.76, Q1FY27 -1.66) inverted to a drag, and much of the subsidiary layer's numbers carry other-auditor or no-auditor assurance (paras 5/6). **Does NOT survive as new** — A4 explicitly states the contribution "INVERTED to a drag... subsidiaries flipped from the group's engine to its brake within two quarters" and ties the drag to the Rs 74.84m unreviewed loss.

All three strongest bear counters are already grafted into A4's review. A4 is symmetric to the point of leading with the bear case. **No surviving un-incorporated counter -> no A4 loop-back required.**

---

## VERDICT

**COMPLETE.** Deliverable gate passes (all four brief parts present). Independent re-enumeration matches the A2 ledger with zero orphan and zero missing rows. Every derived metric recomputes to A4's value within rounding; the one bridge residual (~0.11 Cr) is traced to a source-filing inconsistency A2 already flagged, not an A4 error. All FORWARD-SIGNAL and AMBIGUOUS findings produced management questions. Standalone/consolidated table cites verified against extract line numbers. No adversarial bear counter survives that is not already in the review. This review may proceed to Notion save.

loop_back_to: none. gap: none.

```yaml
stage: A5-adversary
company: "SPAPPAREL"
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
