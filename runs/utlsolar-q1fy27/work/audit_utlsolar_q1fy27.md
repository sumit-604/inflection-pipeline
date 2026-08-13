# A5 ADVERSARY / COMPLETENESS AUDIT — Fujiyama Power Systems Ltd (UTLSOLAR / BSE 544613)
Quarter: Q1 FY27 (quarter ended 30 June 2026) | Model: claude-opus-4-8
Inputs seen: A4 review, A1 extract, A2 ledger (only). Re-derived independently; A4/A3 cites not trusted.
Units: source Rs million, converted x0.1 to Rs Crores (EPS / face value per-share, not converted).

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

The A4 PLAIN-LANGUAGE BRIEF (review lines 614-702) carries all four labelled parts, each non-empty with real content:

| Part | Heading present | Lines | Content check | Status |
|---|---|---|---|---|
| 1. Summary narrative | yes | 616-651 | ~30 lines; revenue/margin/fire/position walk, real prose | PRESENT |
| 2. Sector intelligence | yes | 653-666 | PM Surya Ghar + DCR + Mono-PERC/TOPCon, gross-margin slip, source-labelled | PRESENT |
| 3. Business-model intelligence | yes | 668-683 | single-segment, operating-leverage read, D&A/inventory, disclosed-metric gaps | PRESENT |
| 4. Competition intelligence | yes | 685-702 | BIS standards risk, Zayo upstream, peer/share/util gaps | PRESENT |

Gate 0 result: PASS. All four parts present and substantive.

---

## AUDIT 1 — COVERAGE (fresh independent enumeration vs A2 ledger, then vs A4)

I re-ran the enumeration off the A1 extract with my own sweep. Caption-by-caption count of the page-7 verified transcription and the page-1/3-6/8-11 blocks:

| Category | A2 count | My fresh count | Basis | Orphan rows (in ledger, absent from A4) | Status |
|---|---|---|---|---|---|
| P&L line items | 29 | 29 | Captions Revenue..EPS-Diluted in transcription lines 450-522, incl. 4 subtotals + OCI + Reserves + EPS | none | PASS |
| Numbered notes | 8 | 8 | Notes block lines 541-601; markers 1,3,4,7,8 legible + 2,5,6 OCR-glyphed ("ns","a","a") + 8 ("&") | none | PASS |
| Board-outcome agenda items | 4 | 4 | Page 1 lines 70,73,78,84 | none | PASS |
| Auditor paragraphs | 13 | 13 | Standalone 6 (lines 159-213) + consolidated 7 (243-323, 7a/7b) | none | PASS |
| Annexure rows | 12 | 12 | Annex B/C/D x 4 rows each (pages 9-11) | none | PASS |
| Consolidation entities | 3 | 3 | Consol para 4 lines 270-272 (Holding + Zayo Cables + Zayo Energy) | none | PASS |
| Signature/signoff blocks | 8 | 8 | Cover, std auditor, consol auditor, page-7 results, notes footer, Annex B/C/D | none | PASS |
| Zero-value / ZERO_STANDING lines | 4 | 4 | Exceptional item; Share in loss of associates; Income-tax-earlier-period; Reserves | none (see note) | PASS |

Every ledger row is either individually cited in A4 or covered by A4's explicit blanket marker (preamble lines 15-20: "29 P&L line-item rows, 4 board-outcome agenda items, 13 auditor paragraphs (6 standalone + 7 consolidated), 12 annexure rows, 3 consolidation entities, 8 signoff blocks — all reviewed. No ledger row is unreviewed.").

Zero-value line tracing:
- Exceptional item (fire, 143.581 Cr) — cited extensively (Step 1.5, Step 2, Step 4, verdict).
- Share in loss of associates (consol (0.001) Cr) — cited (Step 1 consol diffs, Step 1.5, S-vs-C gap).
- Income tax relating to earlier period (1.04m, FY26 col only) — cited (Step 4: "Rs 1.04m prior-period tax adjustment sits in the FY26 column only (A3-06), immaterial").
- Reserves (FY26 year-end Rs 1,242.714 Cr, dash in all quarterly columns) — NOT individually discussed in A4, covered only by the blanket "all reviewed" marker. This is acceptable coverage (standard interim convention, year-end-only figure, no Q1 actual, immaterial to a quarterly flow review). Noted as reviewed-no-finding, not an orphan. MINOR OBSERVATION only.

Rows my fresh pass found that the ledger lacks: NONE. My counts match A2 exactly (29/8/4/13/12/3/8). No return-to-A2 condition.

Coverage result: PASS. No orphan row; no missing-from-ledger row.

---

## AUDIT 2 — ARITHMETIC (every derived figure recomputed from A1 raw, in Rs Cr)

Raw subtotals independently re-summed first (all tie exactly):
- Total Expenses Q1FY27: 1,063.978 − 100.895 + 35.401 + 38.937 + 10.901 + 25.017 + 53.462 = 1,126.801 ✓
- PBEIT = 1,348.043 − 1,126.801 = 221.242 ✓; PBT = 221.242 − 143.581 = 77.661 ✓; PAT = 77.661 − 19.866 = 57.795 ✓
- Total tax rows: Q1FY27 198.04+0+0.62=198.66 ✓; FY26 885.52+1.04+152.48=1,039.04 ✓

| Metric | A4 value | My recompute | Source lines | Status |
|---|---|---|---|---|
| Op EBITDA Q1FY27 (PBEIT+D+Fin−OI) | 254.810 | 221.242+25.017+10.901−2.350 = 254.810 | 465/460/459/451 | MATCH |
| Op EBITDA Q1FY26 | 105.893 | 89.934+7.011+9.385−0.437 = 105.893 | ext | MATCH |
| Op EBITDA margin Q1FY27 | 18.94% | 254.810/1,345.693 = 18.936% | 450 | MATCH |
| Op EBITDA margin Q1FY26 | 17.73% | 105.893/597.349 = 17.727% | 450 | MATCH |
| Op EBITDA margin FY26 | 18.47% | 490.300/2,654.506 = 18.470% | 450 | MATCH |
| Reported EBITDA Q1FY27 | 257.160 | 221.242+25.017+10.901 = 257.160 | 465/460/459 | MATCH |
| Reported EBITDA margin Q1FY27 vs 26 | 19.11% / 17.80% | 257.160/1,345.693=19.11%; 106.330/597.349=17.80% | 450 | MATCH |
| Gross Profit Q1FY26 | 177.348 | 597.349−(413.242+6.759) = 177.348 | 450/455/456 | MATCH |
| Gross margin Q1FY27 / QoQ | 28.43% / −232 bps | 382.610/1,345.693=28.43%; 28.43−30.75 | 450/455/456 | MATCH |
| Gross margin YoY | −126 bps | 28.43−29.69 | — | MATCH |
| Core PBT ex-OI Q1FY27 | 218.892 | 221.242−2.350 = 218.892 | 465/451 | MATCH |
| ETR reported Q1FY27 | 25.58% | 19.866/77.661 = 25.581% | 495/476 | MATCH |
| ETR pre-exceptional Q1FY27 | 8.98% | 19.866/221.242 = 8.980% | 495/465 | MATCH |
| PAT margin reported Q1FY27 | 4.29% | 57.795/1,345.693 = 4.295% | 497/450 | MATCH |
| Revenue YoY | +125.3% | 748.344/597.349 = +125.28% | 450 | MATCH |
| Op EBITDA YoY | +140.6% | 148.917/105.893 = +140.63% | — | MATCH |
| Depreciation YoY | +256.8% | 18.006/7.011 = +256.82% | 460 | MATCH |
| Finance cost YoY | +16.2% | 1.516/9.385 = +16.15% | 459 | MATCH |
| Other income YoY | +437.8% | 1.913/0.437 = +437.76% | 451 | MATCH |
| Core Op PBT YoY | +144.6% | 129.395/89.497 = +144.58% | — | MATCH |
| Reported PBT YoY | −13.6% | −12.273/89.934 = −13.65% | 476 | MATCH |
| Reported PAT YoY | −14.5% | −9.792/67.587 = −14.49% | 497 | MATCH |
| EPS reported YoY | −22.0% | (1.88−2.41)/2.41 = −21.99% | 520 | MATCH |
| Revenue QoQ | +49.4% | 444.920/900.773 = +49.39% | 450 | MATCH |
| Op EBITDA QoQ | +48.6% | 83.346/171.464 = +48.61% | — | MATCH |
| PAT before exceptional QoQ | +55.0% | 58.502/106.323 = +55.02% | — | MATCH |
| Reported PAT QoQ | −45.6% | −48.528/106.323 = −45.64% | 497 | MATCH |
| Reported EPS QoQ | −47.5% | −1.70/3.58 = −47.49% | 520 | MATCH |
| Notional tax @25.5% on PBEIT | 56.417 | 221.242×0.255 = 56.417 | 465 | MATCH |
| PAT before exceptional (normalised) | 164.825 | 221.242−56.417 = 164.825 | — | MATCH |
| After-tax exceptional / tax shield | 107.030 / 36.551 | 143.581−(56.417−19.866)=107.030; shield 36.551 | 468/495 | MATCH |
| PAT-before-excep reconciliation | 164.825 | 57.795+107.030 = 164.825 | — | MATCH (ties) |
| Implied EPS ex-exceptional | Rs 5.37 | 164.825/30.69 = 5.371 | 514 | MATCH |
| PAT-before-excep margin | 12.25% | 164.825/1,345.693 = 12.248% | 450 | MATCH |
| PAT bridge close | −9.792 | +205.262−16.662−15.537−24.146−18.006−1.516+1.913−143.581+2.481 = −9.792 | Step 4 | MATCH (ties) |
| S-vs-C PAT gap Q1FY27 | 0.001 Cr / Rs ~10,000 | 57.795−57.794 = 0.001 Cr = Rs 10,000 | 497 | MATCH |
| FY26 current-tax reconciliation | 885.52+1.04+152.48=1,039.04 | 885.52+1.04+152.48 = 1,039.04 | 479/492/494/495 | MATCH |
| HR at CMP 265 | 1.52 (FAILS) | 2.00×(19.7/25.88)=1.522 <1.953 | Step 7 | MATCH |
| HR at Rs 200 | 2.02 (PASSES) | 2.00×(19.7/19.53)=2.017 >1.953 | Step 7 | MATCH |
| Q1 % of Rs 4,000 Cr guide | 33.6% | 1,345.693/4,000 = 33.64% | 450 | MATCH |

Arithmetic mismatches above rounding: NONE.

One within-rounding imprecision (NOT a FAIL, no verdict impact): A4's EPS-CAGR chain rounds 19.90/9.91 = 2.008 down to 2.00 and states 26.0% CAGR; my figure is 26.2% (2.008^(1/3)=1.2617). Re-running the Hurdle Ratio with the un-rounded 2.008 factor gives 1.528 at CMP (still <1.953 = FAILS) and 2.025 at the entry midpoint (still >1.953 = PASSES). Both pass/fail conclusions are unchanged. Noted, not failed.

Arithmetic result: PASS.

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims; strongest bear counter from the SAME extract)

Claim 1 (review lines 199-200, 595-596): "On operations the quarter was strong; revenue +125.3% YoY, the underlying operating quarter is the strongest on record."
- Strongest bear counter from the extract: Changes in inventories line (extract 456) is Rs (100.895) Cr — a single-quarter inventory BUILD larger than the entire FY26 build of Rs (185.580) Cr spread over four quarters. With no cash flow statement or balance sheet at Q1 (Reg 33 half-yearly), the "strong quarter" is entirely unconverted-to-cash; a build this size against a thesis whose central risk is a structural working-capital drain could be unsold stock, not demand.
- Survives? YES as a bear point, but ALREADY GRAFTED into A4 (Step 5 cash-conversion INDETERMINATE, verdict caveats 1-2, Q3, Step 8C focal metric). No new incorporation needed.

Claim 2 (review lines 212, 231, 597): "Operating EBITDA margin expanded +121 bps YoY; PAT-before-exceptional margin 12.25% inside the guided band."
- Strongest bear counter from the extract: Gross margin compressed −126 bps YoY and −232 bps QoQ (382.610/1,345.693 = 28.43% vs FY26 30.60% and Q4 30.75%). The EBITDA expansion is pure operating-leverage on fixed cost lines, not core unit economics; if revenue decelerates to the guided Q2 ~Rs 800 Cr (a sequential decline off Q1), the operating leverage reverses and the gross-margin erosion is exposed.
- Survives? YES, but ALREADY GRAFTED (Step 2 closing caution, C2 AMBER, growth trigger "margin holding" WEAKENED, Q5). No new incorporation needed.

Claim 3 (review lines 90-95, 598, 632-633): "Both audit conclusions unmodified; auditor signed clean; no thesis-broken condition fired; entry zone confirmed."
- Strongest bear counter from the extract: Both reports carry an Emphasis-of-Matter on the fire (standalone para 5 / consolidated para 6) — an AMBER flag, and "clean" overstates the disclosure quality. The same filing shows an undisclosed Rs 0.48m paid-up-capital rise with the diluted-EPS spread collapsing to nil (A3-08, extract 514-522), undisclosed Zayo acquisition consideration and related-party status (note 5), BIS goods-seizure disputes (note 4), and a fire-date drafting inconsistency ("06 May 2025" in note 3 vs "06 May 2026" in both EoMs). A cluster of governance/disclosure data points undercuts "clean."
- Survives? YES, but ALREADY GRAFTED (Step 0D EoM as AMBER, verdict caveats 3-6, flags list, Q4/Q7/Q12/Q14). No new incorporation needed.

Surviving-and-unincorporated bear counters: NONE. All three strongest counters are already carried in A4's caveats/flags/questions.

---

## TARGETED CHECKS DEMANDED BY THE TASK

- Operating vs below-the-line separation: CORRECT. A4 Step 1.5 isolates the Rs 143.581 Cr fire between PBEIT (221.242) and PBT (77.661), reads operations above the line, labels the normalisation an assumption (25.5% ETR), does not use it to fill any extraction cell. PASS.
- Cash conversion INDETERMINATE, never silently PROCEED: CORRECT. Step 5 declares INDETERMINATE, caps verdict at PROCEED WITH CAVEATS, names the missing evidence (no Q1 CFO / balance sheet). Verdict is PROCEED WITH CAVEATS, not PROCEED. PASS.
- Every A3 AMBIGUOUS / FORWARD-SIGNAL finding -> a Questions row: PASS. A3-01=Q2, A3-02=Q5, A3-04=Q11, A3-05=Q1, A3-07=Q13, A3-08=Q7, A3-09=Q12, A3-10=Q14, A3-11=Q4. All nine present.
- Standalone AND consolidated both carried: PASS (Step 1 + consol diffs + Step 1.5 dual columns + yaml sc_gap).
- S-vs-C gap first-class though small: PASS (dedicated yaml block, Step 1 diffs, narrative "loss share of Rs 10,000"; gap 0.001 Cr independently confirmed).
- Fire-date discrepancy surfaced: PASS (note 3 row, A3-10, Q14: note "06 May 2025" vs auditor EoM "06 May 2026").
- Undisclosed Zayo consideration surfaced as a question: PASS (Q4, flags list, narrative).
- Decision Status flag-not-decide, changed only by a fired trigger: PASS (Step 6C no condition fired; Step 8 status stays WATCHLIST; "I flag, the human decides").
- Data-quality limitation + arithmetic-resolved tax cell carried as limitation not clean fact: PASS (preamble DATA-QUALITY LIMITATION on the 885.52m consolidated FY26 cell "reconciled-but-not-visually-confirmed"; degraded Online2PDF text layer stated; caveat 6 + flag).

---

## VERDICT

**COMPLETE.**

- Deliverable gate: PASS (all four brief parts present).
- Coverage: PASS (29 / 8 / 4 / 13 / 12 / 3 / 8 independently reconfirmed; zero orphan rows; zero missing-from-ledger rows).
- Arithmetic: PASS (every derived figure reproduced to the paisa; the two reconciliations — normalised-PAT bridge to 164.825 and FY26 current-tax 885.52+1.04+152.48=1,039.04 — tie exactly; only a within-rounding CAGR imprecision that does not move any pass/fail).
- Adversarial: PASS (all three strongest bear counters already grafted into A4; nothing survives un-incorporated).

Count-reconciliation independently confirmed: P&L line items 29, notes 8, agenda items 4, auditor paragraphs 13 (6 standalone + 7 consolidated), annexure rows 12, entities 3, signoff blocks 8, ZERO_STANDING lines 4.

Arithmetic discrepancy found: NONE above rounding.

No loop-back required. Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "UTLSOLAR"
quarter: "Q1 FY27"
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
