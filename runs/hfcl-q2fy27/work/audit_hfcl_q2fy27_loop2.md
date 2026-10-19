# HFCL LIMITED (HFCL): Q2 FY27 A5 ADVERSARY / COMPLETENESS AUDIT, LOOP 2 FINAL RE-AUDIT (CLOSURE)

Review under audit: runs/hfcl-q2fy27/work/review_hfcl_q2fy27.md (1,107 lines; Part 1 L1-537, Part 2 L542-1075, Loop 1 change log L1079-1094, Loop 2 change log L1096-1106).
Prior audit: runs/hfcl-q2fy27/work/audit_hfcl_q2fy27_loop1.md (INCOMPLETE: L1-F1 FACTUAL; L1-S1 to L1-S6 STYLE).
Inputs read: A1 results fulltext (R-L215-254, R-L800-839, R-L890-995), A2 ledgers (results, presentation; A2-added rows), A4 review. No source PDF was opened. Nothing under inputs/ was opened. A3 reasoning was not used.
Model: claude-opus-5-5. Run date: 2026-10-20.
Anchors: R-L = results fulltext line; P-L = presentation fulltext line; M-L = MA report fulltext line; rev L = review line.
Scope (loop 2, closure only): (1) confirm L1-F1 is closed at every location it appeared; (2) confirm the deliverable gate still passes; (3) check only the loop 2 changed text, including the new prior-period tax-accrual cells, for new FACTUAL / MISSING / CONTRADICTION errors and arithmetic. No new adversarial pass on unchanged text. Concall sections are "pending Role 5 addendum" by design. They are not failed.

---

## A. CLOSURE OF L1-F1 (FACTUAL, A4)

Loop 1 gap: restate the para 7 subsidiary-cash reading at seven locations to "cash balances fell 0.29 (R-L238); CFO NOT FOUND (Q36)"; drop the para 8 "turned 46.14 of NPAT into +36.24 of net cash" wording; add Reading C with the non-parent uses and attribution NOT FOUND.

| Loop 1 location | Now at (rev L) | Current text (abridged) | Status |
|---|---|---|---|
| Preamble M07 row | L53 | "Cash balances fell 0.29; operating cash flow NOT FOUND (Step 5C; RES-FN-28; Q36)" | CLOSED |
| Step 0D para 7 row (was L129) | L127 | "Its H1 cash balances fell 0.29; its operating cash flow is NOT FOUND (RES-FN-28)" | CLOSED |
| Step 0D para 8 row | L128 | "H1 net change in cash +36.24" | CLOSED |
| Step 5C (was L521) | L519-523 | Cash and cash equivalents fell 0.29 (R-L238); net change after investing and financing; CFO NOT FOUND; para 8 "cash rose 36.24"; non-parent uses 52.33 / 80.69 / 55.33, "not split among the para 6, 7 and 8 entities"; Readings A, B and C; Q36 separates them | CLOSED |
| Step 5D(g) (was L529) | L531 | "the para 7 subsidiaries' cash balances fell 0.29 and their operating cash flow is NOT FOUND (RES-FN-28)"; "para 7 subsidiary CFO" added to the missing-evidence list | CLOSED |
| Step 7 Strategic Premium (was L708) | L711 | "that pool's cash balances fell 0.29 and its CFO is NOT FOUND (RES-FN-28)" | CLOSED |
| Verdict flag 7 (was L893) | L896 | "That pool's cash balances fell 0.29 in H1 and its operating cash flow is NOT FOUND (RES-FN-28; Q36)" | CLOSED |
| Brief part 3 (was L934) | L937 | "their cash balances fell Rs0.29 Cr (FILED, Q2). Their operating cash flow is not disclosed, so how much of that profit turned into cash is unknown" | CLOSED |
| YAML flag (was L1061) | L1064 | "that pool's cash balances fell 0.29 and its CFO is NOT FOUND (RES-FN-28)" | CLOSED |
| Q36 and YAML Q36 | L799, L1023 | "while their cash balances fell Rs0.29 Cr. What was their H1 operating cash flow ..." | CLOSED |
| A4 analyst note | L1072 | "profit-to-cash for that pool is unknown, not zero; Q36 separates the three readings" | CLOSED |

Residual-phrase grep over the whole review (case-insensitive): "no cash", "no H1 cash", "produced no", "shown up as cash", "cash anywhere", "added no cash", "turned ... into", "into +36.24". The hits are L767 (warrant objects "have no cash until conversion", unrelated), L937 (the corrected "turned into cash is unknown") and the L1100 change log. No unsupported wording remains.

Fulltext check of the restated cells: para 7 "cash flows (net) ofRs. (0.29) Crores" (R-L238); para 8 "cash flows (net) of Rs. 36.24 Crores" (R-L248-249); para 6 "cash flows (net) of Rs. 0.14 Crores" (R-L223); para 7 H1 NPAT 186.19 (R-L236); "Dividends received" nil in both standalone and consolidated (R-L975). All match.

L1-F1: CLOSED.

### Style items from loop 1

| ID | Fix found | Evidence | Status |
|---|---|---|---|
| L1-S1 | The pointer to Part 2 as a separate location is gone. The header says Part 2 follows Part 1 directly; Part 2 header says Part 1 precedes it "in the same document" | rev L10, L544 | APPLIED (residual in review_path, see L2-S3) |
| L1-S2 | Prior-period tax-accrual cells filled and change columns filled | rev L444-451, L482-488, L529 | APPLIED (arithmetic below) |
| L1-S3 | "deferred tax payment" removed; rows read "current tax charged but unpaid" | rev L444, L531(f), L870, L894 | APPLIED |
| L1-S4 | "falls due under the remaining advance-tax instalments by year-end [INFERENCE]" | rev L475, L709, L838, L1036 | APPLIED |
| L1-S5 | 43.13 and 127.61 labelled "at cost" | rev L373-376, L395, L694, L774, L998 | APPLIED |
| L1-S6 | A2 ledger housekeeping. A2 was not re-run, so the ledgers are unchanged | ledger_results L30-33, L52-55; ledger_presentation L13-14, L480-486 | CARRIED (STYLE, no loop) |

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

| Brief part | Location (rev L) | Status |
|---|---|---|
| (1) Summary narrative | L909-921 (6 paragraphs, about 360 words; unchanged in loop 2) | present |
| (2) Sector intelligence | L923-931 | present |
| (3) Business-model intelligence | L933-941 (para 7 cash sentence revised; real content) | present |
| (4) Competition intelligence | L943-951 | present |
| (5) Forward map (dated catalysts, bull and bear fork each) | L953-964 (make-or-break reading plus 8 catalysts; each carries a Bull and a Bear) | present |

Gate result: PASS.

---

## 1. COVERAGE AUDIT (closure scope)

A1 and A2 were not re-run in loop 2. The ledgers carry the same A2-added rows at the same positions as in loop 1. The test here is whether the loop 2 edits dropped any citation, plus a spot re-run on the cells the edits touched.

| Category | A2 count | Fresh count | Orphan / missing rows | Status |
|---|---|---|---|---|
| Results ledger A2-added rows | 8 (M01-M08; ledger_results L30-33, L52-55) | 8 | none | PASS |
| Presentation ledger A2-added rows | 7 (PM01-PM07; ledger_presentation L480-486) | 7 | none | PASS |
| Auditor paras 6-8 value cells (the loop 2 edit zone) | 26 (R050-R074 plus M06, M07) | 26 (para 6: 10, R-L219-225; para 7: 8, R-L234-238; para 8: 8, R-L245-249) | none | PASS |
| A2-added rows cited in A4 after loop 2 | 15 | 15 (preamble table rev L47-61); M07 still cited in body at L127, L519, L531 | none | PASS |
| Ledger rows marked reviewed | 1,515 / 431 / 411 | 1,515 / 431 / 411 (rev L35-37, L981) | none | PASS |
| A3 FORWARD-SIGNAL / AMBIGUOUS coverage | 54 | 54 (rev L807-813; RES-FN-28 -> Q36 kept) | none | PASS |

Coverage result: PASS. No orphan rows. Nothing missing from the ledgers.

---

## 2. ARITHMETIC AUDIT (loop 2 changed cells)

All values recomputed from R-L804-994 (image transcription). Rounding tolerance is the last printed digit.

| Metric | A4 value (rev L) | Recomputed | Source line | Status |
|---|---|---|---|---|
| Cons tax paid less charged, H1 FY26 | 10.97 (L444) | 17.09 - 6.12 = 10.97 | R-L820, R-L966 | PASS |
| Cons CFO, tax counted when charged, H1 FY26 | (32.63) (L446) | -43.60 + 17.09 - 6.12 = -32.63 | R-L820, R-L966-967 | PASS |
| Cons CFO tax-accrual change | +364.50 (L446, L529) | 331.87 - (-32.63) | R-L966-967 | PASS |
| Cons reported CFO swing | +498.87 (L443, L529) | 455.27 - (-43.60) | R-L967 | PASS |
| Cons CFO/PAT tax-accrual, H1 FY26 | (0.77) (L448) | -32.63 / 42.62 = -0.7656 | R-L822 | PASS |
| Cons CFO/PAT tax-accrual change | +1.29 (L448) | 0.5187 + 0.7656 = 1.2843 (+1.28); +1.29 is the difference of the rounded cells, disclosed in change log L1102 | R-L822, R-L966-967 | PASS at rounding; STYLE L2-S2 |
| Cons FCF tax-accrual, H1 FY26; change | (229.83); +112.55 (L451) | -32.63 - (133.74 + 63.46); -117.28 + 229.83 | R-L970-971 | PASS |
| SA tax paid / charged, H1 FY26 | paid 16.50; charged nil (L482) | R-L966 (16.50); R-L820 "-" | R-L820, R-L966 | PASS |
| SA CFO tax-accrual, H1 FY26; change | (56.09); +191.82 (L483) | -72.59 + 16.50 - 0.00; 135.73 + 56.09 | R-L966-967 | PASS |
| SA CFO/PAT tax-accrual, H1 FY26; change | (2.94); +3.24 (L485) | -56.09 / 19.10 = -2.9366; 0.3035 + 2.9366 = 3.2401 | R-L822 | PASS |
| SA FCF tax-accrual, H1 FY26; change | (232.59); (25.50) (L488) | -56.09 - (113.05 + 63.45); -258.09 + 232.59 | R-L970-971 | PASS |
| "YoY swing flattered too" | qualitative (L444) | 498.87 - 364.50 = 134.37 = 123.40 + 10.97 | R-L820, R-L966-967 | PASS |
| Para 7 H1 NPAT; cash change | 186.19; (0.29) (L519, L799) | as filed | R-L236, R-L238 | PASS |
| Subsidiary cash sum vs group less parent | 36.09 vs 36.08 (L519) | 36.24 - 0.29 + 0.14; 147.30 - 111.22 | R-L223, R-L238, R-L248, R-L989 | PASS |
| Non-parent net bank deposits placed | 52.33 (L519) | (6.10) - 46.23 = (52.33); BS check (409.79 - 310.84) - (430.75 - 384.24) = +52.44 | R-L974, R-L911 | PASS |
| Non-parent net external borrowings repaid | 80.69 (L519) | (500.65 - 380.27) - (440.75 - 239.68) = 120.38 - 201.07 = (80.69); BS check 126.76 - 207.93 = (81.17) | R-L980-981, R-L923, R-L928 | PASS |
| Non-parent capex | 55.33 (L519) | (436.27 - 381.22) + (12.88 - 12.60) | R-L970-971 | PASS |
| Parent dividends received | nil (L519) | "-" in SA and CO | R-L975 | PASS |
| Inventory release at cost, Q2 | 43.13 (L376, L694) | 21.47 - (-21.66) | R-L809 | PASS |
| Inventory build at cost, Q1 | 127.61 (L373) | -168.54 - (-40.93) = -127.61 | R-L809 | PASS |
| Q11 rounded figures | about Rs43 / about Rs128 (L774) | 43.13; 127.61 | R-L809 | PASS |

Arithmetic result: no mismatch above rounding. One rounding presentation note (L2-S2).

---

## 3. ADVERSARIAL READ (loop 2 changed text only)

### Read L2-A. Reading C, the most favourable of the new readings, tested under Master Rule J

Claim (rev L519, L522): "At the non-parent level, H1 cash also went to visible uses [COMPUTED, consolidated less standalone]: net bank deposits placed 52.33; net external borrowings repaid 80.69; capex 55.33." Reading C: "the subsidiaries converted the profit to cash and then placed deposits, repaid debt or spent on capex."

Counter from the same extract: consolidated less standalone does not net out intra-group flows. Two lines show this.
- Loans line: standalone (16.70) paid out as loans to bodies corporate or subsidiaries; consolidated +6.60 (R-L972). The non-parent residual is a 23.30 inflow [COMPUTED: 6.60 - (-16.70)]. Part of the non-parent uses may have been funded by the parent, not by subsidiary profit.
- Interest received: standalone 6.91 vs consolidated 0.72 (R-L976). The non-parent residual (6.19) is an elimination effect, not a subsidiary outflow.
- The group-less-parent CFO gap of 217.20 (rev L515; 455.27 - 238.07, R-L967) is the same kind of proxy. It covers all nine subsidiaries and the eliminations. It does not give the para 7 CFO.

Does the counter survive as a fault? No. A4 does not claim that the listed uses were funded by para 7 profit. It says the uses are "not split among the para 6, 7 and 8 entities", presents C as one of three readings that "fit", and keeps the para 7 CFO and intra-group receivable (Q36) as the separating observation. No number, fact or conclusion changes. The intra-group caveat improves precision only: STYLE L2-S1.

### Read L2-B. New prior-period cells: does the tax-accrual basis change the YoY cash story?

Claim (rev L444, L446, L529): the reported YoY CFO swing (+498.87) is flattered; on the tax-accrual basis it is +364.50.
Counter tested: is the tax-accrual swing still overstated? Recomputed: the gap of 134.37 is exactly 123.40 (H1 FY27 unpaid) plus 10.97 (H1 FY26 overpaid). Both are filed cells (R-L820, R-L966). The standalone FCF change on the tax-accrual basis is negative, (25.50) (rev L488). A4 states this and does not soften it. The counter does not survive.

### Read L2-C. Para 8 "cash rose 36.24" (rev L128, L519)

Counter tested: is this still a conversion claim? No. The wording now matches the filed "cash flows (net) of Rs. 36.24 Crores" (R-L248-249) and makes no profit-to-cash claim. The counter does not survive.

### Mandatory acquisition-economics probe (unchanged inputs; restated)

Step 6E (rev L665-678) was not edited in loop 2. Purchase multiple: consideration NOT FOUND / target PAT NOT FOUND = NOT COMPUTABLE. The target's ~Rs1,600 Cr book is 86.5% of ~Rs1,850 Cr (P-L469-470). No accretion is credited. Q6, add-back tightener (e) and the 31-Dec bull fork each need a filed price and target profit (rev L740, L764, L958). Nothing to graft.

---

## FINDINGS (tagged)

| ID | Type | Agent | Finding | Anchor |
|---|---|---|---|---|
| L2-S1 | STYLE | none | Reading C evidence is consolidated less standalone and does not net intra-group flows: non-parent loans line +23.30 inflow [6.60 - (-16.70)], interest received residual (6.19). Add "intra-group flows not netted; part may be parent-funded" after the visible-uses list. Conclusion unchanged | rev L519, L522; R-L972, R-L976 |
| L2-S2 | STYLE | none | Cons CFO/PAT tax-accrual change shows +1.29, the difference of the rounded cells; unrounded it is +1.28. The other three change cells agree either way. Use +1.28 for one method across the table | rev L448, L1102; R-L822, R-L966-967 |
| L2-S3 | STYLE | none | review_path still names review_hfcl_q2fy27.part2.md in a parenthetical, and L10 narrates the part-file write method. Set review_path to the merged file path only | rev L10, L1073 |
| L1-S6 (carried) | STYLE | none | A2 ledger header and placement housekeeping from loop 1. A2 was not re-run | ledger_results L3, L13, L52-55; ledger_presentation L6, L9 |

FACTUAL: 0. MISSING: 0. CONTRADICTION: 0.

---

## VERDICT

COMPLETE.

- L1-F1 (FACTUAL) is CLOSED at all seven loop 1 locations and at M07, Q36 and the A4 analyst note. Reading C is added. Attribution by paragraph is stated as NOT FOUND.
- Deliverable gate: PASS (all five brief parts present with real content).
- Coverage: PASS (no orphan rows; no missing rows; all 15 A2-added rows still cited).
- Arithmetic: every loop 2 cell recomputes from the fulltext; no mismatch above rounding.
- Loop 2 changed text: no new FACTUAL, MISSING or CONTRADICTION finding.
- loop_back_to: none. The review may proceed to the Notion save gate.
- Finding counts: 0 FACTUAL, 0 MISSING, 0 CONTRADICTION, 4 STYLE (3 new, 1 carried).

## STYLE NOTES (logged, no loop)

- L2-S1: rev L519 add "intra-group flows not netted (parent loans out 16.70 vs consolidated +6.60, R-L972); part of the non-parent uses may be parent-funded" after the visible-uses list.
- L2-S2: rev L448 change cell +1.29 -> +1.28 (unrounded), to match the method used in the other change cells.
- L2-S3: rev L1073 review_path -> "runs/hfcl-q2fy27/work/review_hfcl_q2fy27.md" only.
- L1-S6 (carried): A2 ledger headers and M08 placement, as listed in the loop 1 audit.

---

```yaml
stage: A5-adversary
company: "HFCL"
quarter: "Q2 FY27"
model: "claude-opus-5-5"
status: complete
verdict: COMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
  forward_map: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
findings_by_type:
  factual: []
  missing: []
  contradiction: []
  style:
    - "L2-S1: Reading C visible-uses list (52.33 deposits, 80.69 debt, 55.33 capex) is consolidated less standalone and does not net intra-group flows; non-parent loans line +23.30 inflow [6.60 - (-16.70), R-L972], interest residual (6.19) (R-L976); add 'intra-group flows not netted; part may be parent-funded' (rev L519, L522); conclusion unchanged"
    - "L2-S2: cons CFO/PAT tax-accrual change +1.29 is the rounded-cell difference; unrounded +1.28 (0.5187 + 0.7656); other change cells agree either way (rev L448, L1102)"
    - "L2-S3: review_path still names review_hfcl_q2fy27.part2.md in a parenthetical; L10 narrates the part-file write method (rev L10, L1073)"
    - "L1-S6 (carried): A2 ledger header and placement housekeeping; A2 not re-run (ledger_results L3, L13, L52-55; ledger_presentation L6, L9)"
loop_back_to: ""
gap: ""
style_notes:
  - "L2-S1: rev L519 add intra-group caveat to the Reading C visible-uses list (R-L972, R-L976)"
  - "L2-S2: rev L448 +1.29 -> +1.28 (unrounded)"
  - "L2-S3: rev L1073 review_path -> merged file path only"
  - "L1-S6 (carried): A2 ledger header and M08 placement housekeeping"
analyst_note: "L1-F1 is closed. The para 7 figure now reads as a 0.29 fall in cash balances after investing and financing (R-L238), with CFO NOT FOUND. That wording appears at all seven loop 1 locations, at M07, Q36 and the A4 analyst note. A grep finds no residual 'no cash' or 'turned into' claim. Reading C is added, and attribution by paragraph is stated as NOT FOUND. Every loop 2 cell recomputes from R-L820, R-L966-967 and R-L970-981. The new prior-period tax-accrual cells are cons (32.63) / (0.77) / (229.83) and SA (56.09) / (2.94) / (232.59). The +364.50 vs +498.87 swing gap is exactly 123.40 + 10.97. One judgment is logged, not failed. Consolidated-less-standalone cash uses do not net intra-group flows (parent loans out 16.70 vs consolidated +6.60). So Reading C may be partly parent-funded. A4 already presents C as one of three readings, with Q36 as the separator, so no conclusion changes. The deliverable gate and coverage pass. Verdict COMPLETE; style notes only."
```
