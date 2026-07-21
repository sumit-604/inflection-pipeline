# A5 ADVERSARY / COMPLETENESS AUDIT — SOUTHWEST — Q1 FY27 (confirming re-audit)

Agent A5. Fresh context: A4 review + the two A1 extracts + the two A2 ledgers only. Every number
re-derived independently (Rs Mn x0.1 to Rs Cr per A1 headers, results L7 / pres L8). A4's and A3's
cites checked, not trusted. This pass confirms A4's operator-authorised graft of the previously-
surviving seasonality / exit-pace bear counter, then re-attacks the review fresh.

---

## GRAFT-CONFIRMATION CHECK (task-directed)

| Prior graft | Where it now lives in A4 | Re-check | Verdict |
|---|---|---|---|
| Seasonality / exit-pace counter | Step 2 diag-1 (L140), Step 3 (L167/L169), Step 6D+verdict (L304/L325), Step 7 (L343), Combined verdict (L424/L441), Q14 (L398), flag (L529), monitorable (L464) | "at/above FY26 exit pace" and "no seasonal air-pocket" WITHDRAWN; Q1FY27 61.7 placed BELOW FY26 non-Q1 run-rate 67.6; QoQ vs Q4FY26 marked ND; x4-annualisation flagged as overstating. Structurally incorporated — but see Arithmetic FAIL on the "66%" figure. | **INCORPORATED (defective on one number)** |
| OIL 2D/3D empanelment (F6.7) | 6B#12 (L282), 6D (L305), Q18 (L402), monitorable (L455), flag (L532); sourced results E8 L102-103 + pres sl.32 L1011-1012 (both confirmed in extracts) | Carried as forward enabler, not banked as a booked order | CLOSED |
| JV-recurrence counter (F8.1) | Step 4 flag (L195), First-Class Metric (L211), Q16 (L400), Caveat 7 (L439) | 13/93=14.0% ✓; normalise 3.5 Mn → 83.5 Mn=8.4 Cr (−10.2%) ✓; margin 13.5% ✓ | CLOSED |
| ROCE label inconsistency (F16.4) | Step 7 (L335), Q12 (L396), Caveat 8 (L440) | 0.5×16+7.5=15.5x ✓; 0.5×23+7.5=19x ✓ | CLOSED |
| Order-book double-count (F16.2/Step 6E) | 6E (L307-323), Caveat 4 (L436), Qs 2&8 | net add 180.1 < single 307 order; carried forward unchanged | CLOSED |

The seasonality graft is present in substance; the other four prior grafts are confirmed intact.

---

## AUDIT 1 — COVERAGE

Independent grep/manual re-enumeration of both extracts, diffed against the two A2 ledgers.

| Category | A2 count | My fresh count | Orphan / note | Status |
|---|---|---|---|---|
| Results: numbered notes | 0 | 0 (`^\s*\d+\.\s`=0; 4-pg release, not Reg 33) | — | PASS |
| Results: financial line items (L86-90) | 5 | 5 | — | PASS |
| Results: financial period cells (5×4) | 20 | 20 | — | PASS |
| Results: table footnote (L91) | 1 | 1 | — | PASS |
| Results: Q1 highlight bullets (L93-111) | 13 | 13 | E8 OIL empanelment cited (closed) | PASS |
| Results: CMD commentary claims (L115-148) | 9 | 9 | F3 input-cost admission -> Audit 3 | PASS |
| Results: JV/coal statements | 7 | 7 | — | PASS |
| Results: absent Reg-33 units (K1-K15) | 15 | 15 | carried as first-class ND in A4 0D | PASS |
| Results: letterhead/addressee/sig/about/contact | 11 | 11 | J2 phone-digit typo immaterial | PASS |
| Presentation: slides | 40 | 40 | — | PASS |
| Presentation: line items (16+16+42+6) | 80 | 80 | sl.36 42 = 22 asset + 20 eq/liab | PASS |
| Presentation: chart data points | 110 | 110 (8+8+6+11+25+6+12+32+2) | — | PASS |
| Presentation: footnotes | 7 | 7 | — | PASS |
| Presentation: ZERO_STANDING | 7 | 7 | OCI→F9.1, held-for-sale→F1.1, Curr-Tax-Liab→F1.2, CWIP→Step 5; NCI/Loans template-nil reviewed | PASS |
| Presentation: Ritolia DISCLOSURE_INCONSISTENCY | 1 | 1 | F14.1 / Q15 | PASS |

**No orphan ledger row absent from A4 (no FAIL to A3). No row my fresh pass found is missing from
either ledger (no FAIL to A2).** Counts reconcile exactly on every category.

**Ledger-flag → A4 disposition spot-check (all cited):** TITLE_LABEL_MISMATCH → F14-01/Q14 ✓;
F2 standalone "on similar lines" → First-Class Metric/Q4 ✓; slide-6 Rs 307 cr HZL vs slide-32
Rs 3,070 Mn Rajasthan → F16.2/Step 6E (A4 correctly overrides the ledger "do not conflate" note) ✓;
slide-37 DATA_GAP → F16.1/Q12 ✓; OCI/Current-Tax-Liab/held-for-sale → F9.1/F1.2/F1.1 ✓.

**One under-reviewed commentary row (routed to Audit 3, not a standalone coverage FAIL):** results
F3 / CMD commentary L122-123 admits "this performance is despite ... substantial increase in input
cost." The row is enumerated (ledger cat F) and the commentary category is reviewed, but A4 never
reconciles that admission against its headline +972 bps margin expansion. Handled as a surviving
counter below.

**Minor benign cross-check (reviewed, no finding):** pres slide-9 map shows ~14 state labels vs
"20 Operations across 8 States" (sl.32) — all-time footprint vs current operating-state count; no
forensic/financial content. Not an orphan.

**COVERAGE VERDICT: PASS.**

---

## AUDIT 2 — ARITHMETIC

Every derived cell recomputed from raw extract numbers. Load-bearing cells shown; all others
reconcile to rounding.

| Metric | A4 value | My recompute (raw source) | Source | Status |
|---|---|---|---|---|
| Total Income Q1FY27 | 62.1 | 61.7+0.4 | L1033/41 | OK |
| Op EBITDA Q1FY27 (Rev−TotExp) | 14.9 | 61.7−46.8 | L1033/35 | OK |
| Op EBITDA margin Q1FY27 / Q1FY26 | 24.15% / 14.43% | 149/617 ; 58/402 | L1037/33 | OK |
| Reported EBITDA Q1FY27 (PBT+D+Fin) | 16.6 | 11.9+3.0+1.7 | L1051/43/45 | OK |
| Core Op PBT ex-OI / ex-OI ex-JV Q1FY27 | 11.5 / 10.2 | 11.9−0.4 ; 10.6−0.4 | L1051/47/41 | OK |
| ETR Q1FY27 (Tax/PBT) | 21.8% | 26/119=21.85% | L1053/51 | OK |
| ETR pre-JV Q1FY27 (Tax/PBSJV) | 24.5% | 26/106=24.53% | L1053/47 | OK |
| Revenue YoY | +53.5% | (617−402)/402=53.48% | L1033 | OK |
| Op EBITDA YoY / margin bps | +156.9% / +972 | (149−58)/58 ; 2415−1443 | L1037/39 | OK |
| Depreciation / Finance YoY | +42.9% / −15.0% | (30−21)/21 ; (17−20)/20 | L1043/45 | OK |
| Core ex-OI / ex-OI ex-JV YoY | +475% / +500% | (11.5−2.0)/2.0 ; (10.2−1.7)/1.7 | der. | OK |
| Reported PBT / PAT / EPS YoY | +283.9% / +287.5% / +287.3% | (119−31)/31 ; (93−24)/24 ; (3.06−.79)/.79 | L1051/55/63 | OK |
| PAT bridge (Op EBITDA/PBSJV/JV/tax → PAT) | +9.1/+7.8/+1.0/−1.9 → +6.9 | 14.9−5.8; 10.6−2.8; 1.3−0.3; 2.6−0.7; ties 9.3−2.4 | L1037-55 | OK |
| JV share of consolidated PAT | 14.0% | 13/93=13.98% | L1049/55 | OK |
| JV normalise → PAT / margin | ~8.4 / ~13.6% | 93−9.5=83.5 Mn; 83.5/617=13.5% | L1092 | OK |
| Receivable days FY25 / FY26 | 154.5 / 175.0 | 763/1803×365 ; 1166/2430×365=175.1 | L1132/76 | OK |
| Inventory / Payable days FY26 | 100.6 / 45.9 | 509/1847×365 ; 232/1847×365 | L1129/33/78 | OK |
| Cash conversion cycle FY26 | ~230 | 175.0+100.6−45.9=229.7 | der. | OK |
| Cash & equiv FY25→26 | 19.4→1.3 (−93%) | 194→13 (−93.3%) | L1134 | OK |
| Gross borrowings / net debt FY26 | 78.6 / 77.3 | 160+626 ; 78.6−1.3 | L1120/31/34 | OK |
| Order book net QoQ add | +180.1 (+31.0%) | (7613−5812)/10=180.1 ; /581.2=31.0% | L546 | OK |
| Survey concentration / CBM share | 59% / 29% | 4506/7613 ; 2222/7613 | sl.17 | OK |
| FY26 non-Q1 run-rate | ~67.6 | (243.0−40.2)/3 = 67.6 | L1076/33 | OK |
| FY26 simple-avg quarter | 60.75 | 243.0/4 | L1076 | OK |
| Q1FY27 x4 annualised | 246.8 | 61.7×4 | L1033 | OK |
| ROCE base (0.5×ROCE+7.5) | 15.5x / 19x | 0.5×16+7.5 ; 0.5×23+7.5 | L1170/1165 | OK |
| **Q1FY26 as % of FY26 non-Q1 run-rate** | **~66%** | **40.2/67.6 = 59.5% (~60%)** | **A4 L140/167/169/424/529 vs pres L1033/L1076** | **FAIL → A4** |

**ARITHMETIC FAIL (loop A4).** In the grafted seasonality passage A4 states five times that
"Q1 FY26 (Rs 40.2 Cr) was only ~66% of the FY26 non-Q1 run-rate (~Rs 67.6 Cr)" — review L140, L167,
L169, L424, and YAML flag L529. Against the denominator A4 itself names (the non-Q1 run-rate of
Rs 67.6 Cr), the ratio is 40.2/67.6 = **59.5% (~60%), not ~66%.** The 66% figure is actually Q1FY26
divided by the FY26 **simple-average** quarter (40.2/60.75 = 66.2%) — the smaller denominator A4
explicitly distinguishes from the non-Q1 run-rate two sentences earlier (Step 3, L167). The two
denominators have been swapped. Discrepancy 6.5 pp, well above rounding.

Direction is benign for the conclusion (at the correct 59.5% Q1FY26 is an even deeper seasonal
trough, so "Q1 is the seasonally weakest quarter / withdraw at-or-above exit pace" still holds), but
the specific quoted percentage is wrong in all five places and must be corrected to ~60% (or the
label changed to "% of the FY26 simple-average quarter") before save. All other derived cells
reconcile within rounding; the PAT bridge closes exactly both ways (+6.9 Cr). Separately noted (not
a FAIL, not used by A4): the release's "PAT ... more than 3.90 fold" (results L97) mildly overstates
93/24=3.875x; A4 correctly used +287.5% and did not import it.

---

## AUDIT 3 — ADVERSARIAL READ

Three most-positive A4 claims, each attacked from the same extracted text.

**Positive claim 1 — "Operating income statement genuinely strong, NOT treasury-led; core ex-OI
+475%, ex-JV +500%; ~100%+ of PAT growth recurring/operating" (Step 2 verdict L147; Step 4 L190).**
Same-text counter: the +500% is off a Rs 1.7 Cr base and the JV +Rs 1.0 Cr (14% of PAT, Q1 ≈ full
FY26, audit ND) sits inside reported PAT.
**DOES NOT SURVIVE as new.** A4 already carves the JV out of the "recurring" claim (Step 4 flag
L195), notes OI was a drag, and caps the verdict. Fully incorporated.

**Positive claim 2 — "EBITDA margin +972 bps to 24.15%, holding the FY26 step-up" (Step 2 diag-2
L141).**
Same-text counter: the record 24.15% margin (> FY26 full-year 23.99%, L1039/L1082) is printed in
the quarter A4's own seasonality analysis calls the WEAKEST revenue quarter (Q1FY27 61.7 < non-Q1
run-rate 67.6), and it is posted while the CMD admits a "substantial increase in input cost"
(results L122-123) with the entire cost stack ND (only aggregate Total Expenses disclosed;
materials/employee/other = K9-K13, A4 L101). A record margin on admitted rising input costs, in the
seasonally weakest quarter, with cost composition ND, is not demonstrably a durable structural
step-up — it could be project-mix or cost-recognition timing as the Rs 307 Cr Rajasthan core-
drilling order commences.
**SURVIVES.** Extract-supported (L1039, L1082, L122-123, cost lines ND). A4 addresses the JV and the
cost-line ND generally but never reconciles the explicit input-cost admission against the +972 bps
expansion, and frames the margin only as "holding." **Must be grafted into A4 as a margin-durability
caution (route to a management question on cost mix / project margins). → completeness FAIL to A4.**
This is a caution, not a restatement; the ex-OI ex-JV operating-growth read is unaffected.

**Positive claim 3 — "Coal first-production target FY27-28 is EARLIER than the house FY29 tripwire
(favourable); no thesis-broken trigger fired" (Step 6C L288; Combined verdict L423).**
Same-text counter: FY27-28 is a management target asserted while the enabling GR is only "being
finalised for early submission" (sl.22 L682) and mine development "shall be undertaken now" (not yet
begun, L143-145) — a self-declared pull-forward on an unsubmitted filing is promise-not-delivery.
**DOES NOT SURVIVE as new.** A4 logs "binary GR-slip risk" (L300), routes it to Q6, and lists GR
submission and first production as dated monitorables. The promise is flagged, not banked.

---

## VERDICT

**INCOMPLETE.** Loop back to **A4** (two localised, pre-save-fixable edits).

- Coverage: PASS — 70 results rows / 40 slides / 80 line items / 110 data points / 7 footnotes
  reconcile exactly; no orphans; nothing found the ledgers lack; all five prior grafts confirmed
  present.
- Arithmetic: one FAIL — the seasonality "66% of the non-Q1 run-rate" figure is miscomputed
  (correct ~60%; 66% is vs the simple-average quarter). All other derived metrics reconcile.
- Adversarial: one surviving bear counter — the margin-durability counter (claim 2) — is extract-
  supported and unincorporated; must be grafted before save.

The seasonality/exit-pace graft this re-audit was convened to confirm IS substantively incorporated
(claims withdrawn, Q1FY27 61.7 below the non-Q1 run-rate 67.6, QoQ ND) and fails only on the one
propagated percentage. The PROCEED WITH CAVEATS verdict floor is unaffected by either gap. Not
REWORK — the docs are internally coherent; both gaps are targeted A4 corrections.

```yaml
stage: A5-adversary
company: "SOUTHWEST"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches:
  - metric: "Q1 FY26 as % of FY26 non-Q1 run-rate (seasonality graft)"
    a4_value: "~66%"
    recomputed: "59.5% (40.2/67.6); the 66% is Q1FY26/simple-avg-quarter (40.2/60.75), a swapped denominator"
    source_line: "review L140/L167/L169/L424/L529; raw pres L1033 (402) & L1076 (2430)"
surviving_bear_counters:
  - claim: "EBITDA margin +972 bps to 24.15% holding the FY26 step-up (Step 2 diag-2, L141)"
    counter: "Record 24.15% margin (> FY26 full-year 23.99%) is printed in the seasonally weakest revenue quarter (Q1FY27 61.7 < non-Q1 run-rate 67.6) while the CMD admits a substantial increase in input cost (results L122-123) and the entire cost stack is ND (only aggregate Total Expenses; materials/employee/other = K9-K13). Durability of the step-up is unproven; could be project-mix or cost-recognition timing. A4 frames the margin only as 'holding' and never reconciles the input-cost admission. Graft a margin-durability caution + management question on cost mix/project margins."
    source_line: "pres L1039/L1082; results L122-123; A4 L101/L141"
loop_back_to: "A4"
gap: "(1) ARITHMETIC: correct 'Q1 FY26 ~66% of the non-Q1 run-rate' to ~60% (40.2/67.6=59.5%; 66% is vs the simple-average quarter 40.2/60.75) in review L140/L167/L169/L424/L529. (2) SURVIVING COUNTER: graft the margin-durability bear counter -- reconcile the +972 bps expansion against the CMD 'substantial increase in input cost' admission (results L122-123), noting cost composition ND and the record 24.15% margin posted in the seasonally weakest quarter, and route to a cost-mix/project-margin management question. Seasonality/exit-pace graft, OIL empanelment, JV-recurrence, ROCE-label and order-book counters are all verified correctly incorporated; no action there."
```
