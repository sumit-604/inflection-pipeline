# HFCL LIMITED (HFCL): Q2 FY27 A5 ADVERSARY / COMPLETENESS AUDIT, LOOP 1 RE-AUDIT

Review under audit: runs/hfcl-q2fy27/work/review_hfcl_q2fy27.md (1,092 lines; Part 1 L1-537, Part 2 appended L539-1072, Loop 1 change log L1076-1091).
Prior audit: runs/hfcl-q2fy27/work/audit_hfcl_q2fy27.md (INCOMPLETE: F1; M1-M5; C1, C2; S1-S3).
Inputs read: A1 fulltexts (results, presentation, MA report), A1 structured files (results, presentation), A2 ledgers (results, presentation), A4 review. No source PDF was opened. Nothing under inputs/ was opened. A3 reasoning was not used.
Model: claude-opus-5-5. Run date: 2026-10-20.
Anchors: R-L = results fulltext line; P-L = presentation fulltext line; M-L = MA report fulltext line; rev L = review line.
Scope (loop 1): (1) closure of every prior FACTUAL / MISSING / CONTRADICTION item; (2) deliverable gate and coverage re-run over the patched ledgers; (3) new or changed text checked for new FACTUAL / MISSING / CONTRADICTION errors, arithmetic included. No new full adversarial pass on unchanged text. The concall sections are pending the Role 5 addendum by design. They are not failed.

---

## A. CLOSURE OF PRIOR FINDINGS

| Prior ID | Type | Agent | Fix found | Evidence | Status |
|---|---|---|---|---|---|
| F1 | FACTUAL | A4 | Step 3A Q1 FY27 now reads +74.49 (items not reclassified) / +72.16 (OCI after tax). The standalone 74.24 moved to Step 3B with a standalone label. Q23 now reads 74.49 | rev L375, L389, L783; R-L823, R-L826 | CLOSED |
| M1 | MISSING | A2 | Rows M06 (para 6 TCI (0.17) Q2 and (0.18) H1), M07 (para 7 net cash flows (0.29) H1) and M08 (PR forward claim on the OFC portfolio and DC connectivity) were added. Each one matches the fulltext word for word | ledger_results L52-54; R-L221-222, R-L238, R-L749-750 | CLOSED |
| M2 | MISSING | A2 | Rows PM01-PM07 were added. Each one matches the fulltext word for word: "1.49"; secured raw materials; OF/OFC value realisation; PCS/DC adjacency; slide 19 priority lines; "#1 in OFC and strong market share in Wifi and UBR"; "Actively catering to Domestic telcos and Bharatnet" | ledger_presentation L479-486; P-L215, P-L119-120, P-L467-471, P-L503-518, P-L532-533, P-L537-538 | CLOSED |
| M3 | MISSING | A3 / A4 | M01-M08 and PM01-PM07 are each cited with a use in the review preamble table and in body steps. The reconciliation now counts 1,515 / 431 / 411 rows | rev L37-38, L45-63, L978 | CLOSED |
| M4 | MISSING | A4 | The tax-accrual cash reading now sits beside the reported one in Steps 5A, 5B and 5D, 6B G3 and AR-2, Step 7 Pillar 2, Step 6.5, add-back tightener (g), Q42, monitorables M6 and M14, the verdict card, flags and brief parts 1 and 5 | rev L446-453, L477, L484-490, L525-528, L611, L628, L692, L706, L737, L802, L835, L843, L880, L891, L912, L960 | CLOSED |
| M5 | MISSING | A4 | The new Step 6E probe gives target, price and target financials as NOT FOUND and the multiple as NOT COMPUTABLE; 86.5% of the book in the unowned entity; no accretion credited. Core Q6 asks the price and target financials. The 31-Dec bull fork now needs a filed price and target profit | rev L662-675, L761, L890, L955 | CLOSED |
| C1 | CONTRADICTION | A4 | Step 2D answer 1 now says H1 is AT the guide on run-rate, with H2 YoY +46.69% against H1 +132.81%. "Far above" now applies only to the old Notion base (rev L349). Step 6A reads "ABOVE BASE; AT GUIDE". A grep finds no other "far above" or "above the new guide" wording | rev L349, L594, L601, L722, L759, L894-895, L910 | CLOSED |
| C2 | CONTRADICTION | A2 | Ledger pointers now read R141 -> R1479 (corrected from R763) and R162 -> R1486 (corrected from R1485). The structured file confirms R1479 = Rs90 Cr FD, R-L869 and R1486 = statement date, R-L889 | ledger_results L371, L390; structured L1488, L1495 | CLOSED |
| S1-S3 | STYLE | none | +14.06% (rev L398); 5 no-row slides (rev L38); capital-advance label tiered INFERENCE (rev L353, L451, L464, L498, L934) | as cited | APPLIED |

All eight prior loop items are closed.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

| Brief part | Location (rev L) | Status |
|---|---|---|
| (1) Summary narrative | L906-918 (6 paragraphs, about 360 words; real content, cash paragraph revised) | present |
| (2) Sector intelligence | L920-928 | present |
| (3) Business-model intelligence | L930-938 | present |
| (4) Competition intelligence | L940-948 | present |
| (5) Forward map (dated catalysts, bull and bear fork each) | L950-961 (make-or-break reading plus 8 catalysts, each with Bull and Bear) | present |

Gate result: PASS.

---

## 1. COVERAGE AUDIT (re-run over the patched ledgers)

Method: a fresh grep pass over each A1 fulltext, diffed against the A1 structured file plus the A2-added rows. Then every A2-added row was checked for a citation in A4.

### 1A. Results (ledger_results_hfcl_q2fy27.md)

| Category | A2 count | Fresh count | Orphan / missing rows | Status |
|---|---|---|---|---|
| Notes | 10 | 10 (R-L866-887, R-L993-994) | none | PASS |
| FS line items | 153 | 153 (unchanged since the prior pass) | none | PASS |
| PR table line items | 14 | 14 (R-L715-730) | none | PASS |
| Consolidation entities | 15 | 15 (R-L871-885) | none | PASS |
| Auditor paragraphs | 11 | 11 | none | PASS |
| Agenda items | 1 | 1 (R-L44, "inter-alia") | none | PASS |
| Auditor paras 6-8 value cells | 23 values in R050-R074 (plus 2 count rows) + 3 cells in M06/M07 = 26 | 26 (para 6: 10, R-L219-225; para 7: 8, R-L234-238; para 8: 8, R-L245-248) | none | PASS |
| Forward claims | 21 structured + M08 = 22 | 22 (R-L681-683, L697, L700, L706-707, L709, L738-739, L742-743, L747-750, L752-762, L779-780, L869) | none | PASS |
| Board-letter units | M01-M04 | 4 (R-L42, L57-58, L60, L80-83) | none | PASS |
| Structured IDs in ledger | 1,507 | 1,507 | none | PASS |
| Superseded pointers | 124 | 124; R141 -> R1479 and R162 -> R1486 now correct | none | PASS |
| A2-added rows cited in A4 | 8 (M01-M08) | 8 cited at rev L49-56 and in the body | none | PASS |

Judgment logged, not a finding: R-L734-736 ("reinforce our confidence ... sustained growth") is generic sentiment with no named line, metric or date. It is not counted. The decision is the same as in the prior audit.

### 1B. Presentation (ledger_presentation_hfcl_q2fy27.md)

| Category | A2 count | Fresh count | Orphan / missing rows | Status |
|---|---|---|---|---|
| Slides | 25 | 25 | none | PASS |
| Slide 8 numeric tokens | 71 + PM01 = 72 | 72 (P-L189-215) | none | PASS |
| Forward claims | 33 + PM02-PM05 = 37 | 37 | none | PASS |
| Slide 20 claim units | PM06, PM07 + R298-R302, R374-R378, R416 | all tagged (P-L532-544) | none | PASS |
| Slides 13-14 claim units | R264, R324, R328, R331, R332 | tagged | see judgment below | PASS |
| Entities / dates / qualifiers | 30 / 21 / 23 | 30 / 21 / 23 | none | PASS |
| Structured IDs in ledger | 424 + 7 = 431 | 431 | none | PASS |
| A2-added rows cited in A4 | 7 (PM01-PM07) | 7 cited at rev L57-63 and in the body | none | PASS |

Judgment logged, not a finding: two claims have no A1 type (no entity, number, date, forward element or qualifier) and are generic. They are not counted. The claims are P-L394-399 "Supplied for nation-wide OFC connectivity projects in multiple countries" and P-L409-410 ("strengthened R&D capabilities ... technology-led enterprise"). PM06 and PM07 differ from these. Each of them carries a typed token that parallels a tagged row (#1 parallels R264; BharatNet parallels R328).

### 1C. MA report (ledger_mareport_hfcl_q2fy27.md)

Not patched in loop 1. The prior pass stands: 25 pages, 411 structured IDs, 6 QIP objects, 5 preferential objects, 10/10 superseded IDs. The Step 6E anchors were re-checked: M-L1107 (Rs90 Cr HASPL object), M-L1097-1146 (conditions-precedent reason), M-L1166-1167 (extension to 31-Dec-2026), M-L1282 ("Not Ascertain..."). PASS.

### 1D. Ledger rows vs A4 citation

A4 marks 1,515 / 431 / 411 rows reviewed and names every A2-added row with a use. A3 findings RES-FN-28, RES-FN-29 and PPT-FN-17 to PPT-FN-21 are incorporated (rev L521, L796-801, L808-809). The 8.5C coverage recounts as 23 + 19 + 12 = 54 FORWARD-SIGNAL or AMBIGUOUS findings, each mapped to a question.

Coverage result: PASS. No orphan rows. Nothing is missing from the ledgers.

---

## 2. ARITHMETIC AUDIT (new and changed text)

All values were recomputed from R-L804-994 (image transcription), P-L and M-L lines. Rounding tolerance is the last printed digit.

| Metric | A4 value (rev L) | Recomputed | Source line | Status |
|---|---|---|---|---|
| Unpaid current tax H1 FY27, cons | 123.40 (L446) | 243.29 - 119.89 = 123.40 | R-L820, R-L966 | PASS |
| BS tie, cons: tax liabilities / tax assets / net | +134.04 / +10.63 / +123.41 (L447) | 194.03 - 59.99; 23.38 - 12.75; 134.04 - 10.63 | R-L933, R-L914 | PASS |
| CFO, tax counted when charged, cons | 331.87 (L448) | 455.27 - 123.40 | R-L967 | PASS |
| CFO/PAT cons, reported / tax-accrual | 0.71 / 0.52 (L449-450) | 455.27 / 639.86 = 0.7115; 331.87 / 639.86 = 0.5187 | R-L822, R-L967 | PASS |
| CFO/PAT H1 FY26 cons; change | (1.02); +1.73 (L449) | -43.60 / 42.62 = -1.023; 0.71 + 1.02 | R-L822, R-L967 | PASS |
| Capex cons H1 FY27 / H1 FY26 | 449.15 / 197.20 (L451) | 436.27 + 12.88; 133.74 + 63.46 | R-L970-971 | PASS |
| FCF cons, reported / tax-accrual | 6.12 / (117.28) (L452-453) | 455.27 - 449.15; 331.87 - 449.15 | R-L967, R-L970-971 | PASS |
| WC share of PAT; drains / offsets | 79.6%; 848.90 / 426.71 (L454) | 509.11 / 639.86 = 0.7957; 403.61 + 127.99 + 317.30; 178.51 + 109.43 + 138.77 | R-L954-964 | PASS |
| Unpaid current tax H1 FY27, SA | 102.34 (L484) | 162.39 - 60.05 | R-L820, R-L966 | PASS |
| BS tie, SA | +106.98 / +4.63 / +102.35 (L484) | 154.03 - 47.05; 13.24 - 8.61 | R-L933, R-L914 | PASS |
| CFO tax-accrual SA; CFO/PAT SA reported / tax-accrual | 135.73; 0.53 / 0.30 (L485-487) | 238.07 - 102.34; 238.07 / 447.23 = 0.5323; 135.73 / 447.23 = 0.3035 | R-L822, R-L967 | PASS |
| CFO/PAT H1 FY26 SA; change | (3.80); +4.33 (L486) | -72.59 / 19.10 = -3.801 | R-L822, R-L967 | PASS |
| Capex SA; FCF SA reported / tax-accrual | 393.82 / 176.50; (155.75) / (258.09) (L488-490) | 381.22 + 12.60; 113.05 + 63.45; 238.07 - 393.82; 135.73 - 393.82 | R-L967, R-L970-971 | PASS |
| Prior-period tax-accrual cells | ND (L448, L450, L453, L485, L487, L490) | computable: cons CFO (32.63), CFO/PAT (0.77), FCF (229.83); SA CFO (56.09), CFO/PAT (2.94), FCF (232.59) | R-L820, R-L966-967, R-L970-971 | STYLE (S2): no stated value is wrong |
| Guide floor; H1 x 2 | 8,908.69; 8,913.54 (L349) | 4,949.27 x 1.8 = 8,908.686; 4,456.77 x 2 | R-L700, R-L804 | PASS |
| H2 need; per quarter; vs Q2 | 4,451.92; 2,225.96; -12.43% (L349, L399) | 8,908.69 - 4,456.77; / 2; 2,225.96 / 2,541.79 = 0.87574 | R-L804 | PASS |
| H2 FY26; implied H2 YoY; H1 YoY | 3,034.91; +46.69%; +132.81% (L349) | 4,949.27 - 1,914.36; 4,451.92 / 3,034.91 = 1.46690; 4,456.77 / 1,914.36 = 2.32810 | R-L804, R-L724 | PASS |
| SA guide pace | 2,182.01 (L399) | (4,527.54 x 1.8 - 3,785.56) / 2 = 2,182.006 | R-L804 | PASS |
| Old-base implied growth; H1 share of base | +25.3%; 71.9% (L349, L594) | 6,200 / 4,949.27 = 1.2527; 4,456.77 / 6,200 = 0.7188 | R-L804 | PASS |
| Defence book in unowned entity; own book | 86.5%; ~250 (L671, L660) | 1,600 / 1,850 = 0.8649; 1,850 - 1,600 | P-L469-470 | PASS |
| Defence H1 share of aspiration; H2 run-rate need | 15.7%; 3.83x (L660) | 78.68 / 500; (500 - 78.68) / 2 / 54.94 = 3.834 | R-L840, R-L709 | PASS |
| Q1 FY27 cons OCI (F1 fix) | +74.49 / +72.16 (L375) | R-L823 CO Q1; R-L826 CO Q1 | R-L823, R-L826 | PASS |
| Q2 vs H1 average (S1 fix) | +14.06% (L398) | 2,541.79 / 2,228.385 = 1.14064 | R-L804 | PASS |
| Para 6 PAT impact; share of PAT | (0.49); 0.12% (L128) | (0.17) + (0.32); 0.49 / 394.22 = 0.124% | R-L221, R-L224 | PASS |
| Para 7 / para 8 share of Q2 PAT | 31.30% / 6.26% (L129-130) | 123.40 / 394.22; 24.68 / 394.22 | R-L236, R-L246, R-L822 | PASS |
| Subsidiary net cash sum vs group less parent | 36.09 vs 36.08 (L521) | 36.24 - 0.29 + 0.14; 147.30 - 111.22 | R-L223, R-L238, R-L248, R-L989 | PASS (arithmetic only; reading fails, see L1-F1) |
| SA less CO trade payables | 74.55 (L521) | 1,260.50 - 1,185.95 | R-L931 | PASS |
| Turnkey net capital Q1 to Q2 | 2,477.30 to 2,545.16 (L619) | 3,565.77 - 1,088.47; 3,448.38 - 903.22 | R-L855, R-L861 | PASS |
| Non-parent OCA rise | +260.66 (L644) | 317.31 - (2,101.13 - 2,044.48) | R-L915 | PASS |
| 6B counts | GREEN 5 / AMBER 6 / RED 5 / UNKNOWN 10 (L635) | recounted row by row, 26 readings | rev L609-633 | PASS |
| Early-warning signals lit | 1 of 8 (L648) | recounted | rev L648 | PASS |
| Gross borrowings H1 rise | 126.76 (L531) | 1,840.13 - (389.88 + 1,323.49) | R-L923, R-L928 | PASS |

Arithmetic result: no mismatch above rounding. One presentation note (S2).

---

## 3. ADVERSARIAL READ (new and changed text only)

### Read L1-A. New bear claim, tested under Master Rule J (a bear claim carries the same bar as a bull claim)

Claim (new loop 1 text, RES-FN-28 as adopted by A4):
- rev L521: "The fastest-growing profit pool has not yet shown up as cash anywhere in the group."
- rev L529 (g): "para 7 subsidiary profit produced no cash".
- rev L129: "no cash in H1"; rev L708: "with no H1 cash"; rev L893 and L1061 (flag 7): "that pool showed no H1 cash".
- rev L934 (brief part 3, tier FILED): "earned Rs186.19 Cr in the half year but added no cash".
- rev L521 also says, in the bull direction, that the para 8 subsidiaries "turned 46.14 of H1 NPAT into +36.24 of net cash".

Counter from the same extract:
- The filed figure is "cash flows (net)" (R-L238). This is the change in cash and cash equivalents after investing and financing flows. It does not measure how much profit became cash. No subsidiary CFO is in the extract, and A4's own Q36 asks for it (rev L796).
- At group level, the non-parent entities used cash in ways the net figure hides. These are the visible uses [COMPUTED, consolidated less standalone]:
  - Net bank deposits placed: 52.33 = (6.10) - 46.23 (R-L974). Balance-sheet check: non-parent "bank balances other than cash" rose 52.44, from 46.51 to 98.95 (R-L911).
  - Net external borrowings repaid: 80.69 = (500.65 - 440.75) - (380.27 - 239.68) (R-L980-981). Balance-sheet check: consolidated less standalone borrowings fell 81.17, from 224.35 to 143.18 (R-L923, R-L928).
  - Capex: 55.33 = (436.27 - 381.22) + (12.88 - 12.60) (R-L970-971).
- With the 36.08 change in cash, these visible uses come to 224.43. All nine subsidiaries together earned an H1 NPAT of 232.15 [COMPUTED: 186.19 + 46.14 - 0.18; R-L221, R-L236, R-L246]. Intra-group flows are not netted out of either figure. The parent paid out 16.70 of loans to bodies corporate or subsidiaries (R-L972).
- The extract does not split these uses among the para 6, para 7 and para 8 entities. So the para 7 cash conversion is NOT FOUND. It is not zero.

The counter survives. Three statements are not supported: "has not yet shown up as cash anywhere in the group", "produced no cash", and "turned ... into net cash". The extract supports only this: the para 7 subsidiaries' cash and cash equivalents fell 0.29 in H1, and their CFO is NOT FOUND. A Reading C belongs beside A4's Readings A and B. Under Reading C, the subsidiaries converted the profit and spent it on deposits, debt repayment or capex. The observation that separates the three readings stays the same: the para 7 subsidiaries' own CFO and their intra-group receivable from HFCL (Q36).
Type: FACTUAL (a claim the extract does not support). Loop: A4. Finding L1-F1.

### Read L1-B. New positive claim: G3 and AR-2 "GREEN (positive on both readings)" (rev L611, L628)

Counter tested: does the tax-accrual reading turn CFO negative? No. 331.87 > 0 (R-L967 less 123.40). The threshold is "CFO positive", and the GREEN holds on both readings. A4 states the quality qualifier (below 0.65). The counter does not survive.

### Read L1-C. New positive claim: "reported CFO/PAT is the first reading above the 4-year 0.18 history" (rev L528)

Counter tested: does the tax-accrual reading erase the step-up? No. 0.52 is also above the 0.18 memory figure. A4 already says the tax-accrual reading does not clear 0.65 and that the evidence is one half-year only. The counter does not survive. The YoY swing is flattered on the tax-accrual basis: +364.50 against +498.87 reported [COMPUTED: 331.87 - (-32.63)]. A4 states this in words (rev L446). Putting the number in is STYLE (S2).

### Mandatory acquisition-economics probe, re-run on the patched inputs

The patched rows (M06-M08, PM01-PM07) add no consideration, target PAT, ROCE, debt, cash or customer tenure. Purchase multiple: consideration NOT FOUND / target PAT NOT FOUND = NOT COMPUTABLE. A4's Step 6E (rev L662-675) now states this. It credits no accretion, asks the price and target financials in core Q6, and puts a price condition on the 31-Dec bull fork (rev L955) and add-back tightener (e) (rev L737). Nothing further needs grafting.

---

## FINDINGS (tagged)

| ID | Type | Agent | Finding | Anchor |
|---|---|---|---|---|
| L1-F1 | FACTUAL | A4 | A4 reads the para 7 net cash flow of (0.29) as proof that H1 profit "has not yet shown up as cash anywhere in the group" and "produced no cash". It also reads the para 8 figure as profit "turned into" cash. The filed figure is the change in cash after investing and financing, and no subsidiary CFO is filed. At group level, non-parent entities placed 52.33 net in bank deposits, repaid 80.69 net of external borrowings and spent 55.33 on capex in H1 [COMPUTED]. The extract does not attribute these by paragraph. Restate rev L521, L529(g), L129, L708, L893, L934 and L1061 as "cash balances fell 0.29; CFO NOT FOUND", and add Reading C | rev L129, L521, L529, L708, L893, L934, L1061; R-L238, R-L911, R-L923, R-L928, R-L970-974, R-L980-981 |
| L1-S1 | STYLE | none | The review points to Part 2 at runs/hfcl-q2fy27/work/review_hfcl_q2fy27.part2.md. That file does not exist. Part 2 is appended in the same file at rev L539-1072. Point to one file | rev L10-12, L537, L541, L1070 |
| L1-S2 | STYLE | none | Prior-period tax-accrual cells say ND but can be computed: cons CFO (32.63), CFO/PAT (0.77), FCF (229.83); SA CFO (56.09), CFO/PAT (2.94), FCF (232.59). On this basis the YoY CFO swing is +364.50, against +498.87 reported | rev L448, L450, L453, L485, L487, L490; R-L820, R-L966-967 |
| L1-S3 | STYLE | none | 5D(f) calls the 123.40 a "deferred tax payment". It is current tax charged but not paid. "Deferred tax" names a different line (R-L821). Use "unpaid current tax" | rev L529 |
| L1-S4 | STYLE | none | Tax-timing INFERENCE "advance-tax instalments normally fall in the second half" is broader than needed. The extract shows only that 123.40 is unpaid at 30-Sep (R-L933). Suggest "falls due under the remaining advance-tax instalments by year-end". The conclusion does not change | rev L477 |
| L1-S5 | STYLE | none | Unchanged text: "subsidiary stock release about 43.13 revenue". 43.13 is an inventory change at cost (21.47 consolidated less (21.66) standalone), not revenue. Label it "at cost" | rev L691; R-L809 |
| L1-S6 | STYLE | none | Ledger housekeeping. Results header (L3, L13) ignores M01-M08: forward count 21 against 22 forward units with M08. M08 is filed under section 2 "Auditor report paragraphs" but is a press-release line. M05 cites L262; the membership number sits at R-L263. A1 structured R141/R162 still carry SUPERSEDED_BY R763/R1485, though the ledger documents the correction. Presentation header forward_rows 33 is not updated to 37, and line 9 still reads "7 no-data slides" | ledger_results L3, L13, L54-55; ledger_presentation L6, L9; structured L150, L171 |

---

## VERDICT

INCOMPLETE.

- Failing agent: A4 (L1-F1, FACTUAL).
- loop_back_to: A4. A2 and A3 need no re-run. The fix is review text only. No table number changes.
- Exact gap: restate the para 7 subsidiary-cash reading at rev L129, L521, L529(g), L708, L893, L934 and L1061. The supported claim is "para 7 subsidiaries' cash and cash equivalents fell 0.29 in H1 (R-L238); their CFO is NOT FOUND (Q36)". Replace "turned 46.14 of H1 NPAT into +36.24 of net cash" with "net cash flows +36.24 against H1 NPAT 46.14". Add Reading C beside Readings A and B: at group level, non-parent entities placed 52.33 net in bank deposits (R-L974), repaid 80.69 net of external borrowings (R-L980-981) and spent 55.33 on capex (R-L970-971); attribution by paragraph is NOT FOUND. A4 may record this as an A4 correction to RES-FN-28, as it did for MA-FN-13.
- Finding counts: 1 FACTUAL, 0 MISSING, 0 CONTRADICTION, 6 STYLE.
- All prior loop items (F1, M1-M5, C1, C2) are CLOSED. The deliverable gate passes. Coverage passes. Arithmetic shows no mismatch.

## STYLE NOTES (logged, no loop)

- L1-S1: point the review header, the Part 1 continuation line and review_path at the single merged file.
- L1-S2: fill the prior-period tax-accrual cells: cons (32.63) / (0.77) / (229.83); SA (56.09) / (2.94) / (232.59).
- L1-S3: rev L529 "deferred tax payment" -> "unpaid current tax".
- L1-S4: rev L477 tax-timing INFERENCE -> "falls due under the remaining advance-tax instalments by year-end".
- L1-S5: rev L691 "43.13 revenue" -> "43.13 at cost (inventory release)".
- L1-S6: A2 ledger headers and placement as listed. The A1 structured supersession tags are documented in the ledger and do not affect the review.

---

```yaml
stage: A5-adversary
company: "HFCL"
quarter: "Q2 FY27"
model: "claude-opus-5-5"
status: complete
verdict: INCOMPLETE
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
surviving_bear_counters:
  - {claim: "RES-FN-28 as adopted by A4: para 7 subsidiaries' H1 profit 'has not yet shown up as cash anywhere in the group' / 'produced no cash' / 'added no cash'; para 8 'turned 46.14 of NPAT into +36.24 of net cash' (rev L129, L521, L529, L708, L893, L934, L1061)", counter: "R-L238 (0.29) is net change in cash after investing and financing, not cash conversion; no subsidiary CFO filed (A4 Q36). Group-level non-parent uses in H1 [COMPUTED, consolidated less standalone]: net bank deposits placed 52.33 (R-L974; BS other bank balances +52.44, R-L911); net external borrowings repaid 80.69 (R-L980-981; BS -81.17, R-L923, R-L928); capex 55.33 (R-L970-971); with cash change 36.08 these total 224.43 vs subsidiaries' combined H1 NPAT 232.15, before intra-group flows. Attribution to para 7 NOT FOUND, so para 7 conversion is NOT FOUND, not zero", source_line: "R-L238, R-L911, R-L923, R-L928, R-L970-974, R-L980-981, R-L989", type: FACTUAL}
findings_by_type:
  factual:
    - "L1-F1 (A4): para 7 net cash flow (0.29) read as 'no cash anywhere in the group' / 'produced no cash', and para 8 net cash read as profit 'turned into' cash; the extract supports only 'cash balances fell 0.29; CFO NOT FOUND'; non-parent entities placed 52.33 in deposits, repaid 80.69 external debt and spent 55.33 on capex in H1, unattributed; Reading C missing (rev L129, L521, L529, L708, L893, L934, L1061)"
  missing: []
  contradiction: []
  style:
    - "L1-S1: review points to non-existent review_hfcl_q2fy27.part2.md; Part 2 is appended at rev L539-1072 (rev L10-12, L537, L541, L1070)"
    - "L1-S2: prior-period tax-accrual cells ND but computable: cons CFO (32.63), CFO/PAT (0.77), FCF (229.83); SA (56.09), (2.94), (232.59)"
    - "L1-S3: rev L529 'deferred tax payment' should read 'unpaid current tax'"
    - "L1-S4: rev L477 advance-tax INFERENCE broader than needed; conclusion unchanged"
    - "L1-S5: rev L691 '43.13 revenue' is an inventory release at cost (R-L809)"
    - "L1-S6: A2 ledger headers not updated for M01-M08 / PM02-PM05; M08 filed under auditor paragraphs; M05 pointer L262 vs R-L263; A1 R141/R162 tags still show old supersession targets (ledger documents the correction)"
loop_back_to: "A4"
gap: "A4: restate the para 7 subsidiary-cash reading at rev L129, L521, L529(g), L708, L893, L934, L1061 to 'para 7 cash and cash equivalents fell 0.29 in H1 (R-L238); CFO NOT FOUND (Q36)'; replace 'turned 46.14 of H1 NPAT into +36.24 of net cash' with 'net cash flows +36.24 against H1 NPAT 46.14'; add Reading C: non-parent entities placed 52.33 net in bank deposits (R-L974), repaid 80.69 net external borrowings (R-L980-981) and spent 55.33 on capex (R-L970-971) in H1, attribution by paragraph NOT FOUND. Text-only fix; no table number changes."
style_notes:
  - "L1-S1: point review header and review_path at the single merged file"
  - "L1-S2: fill prior-period tax-accrual cells (cons (32.63)/(0.77)/(229.83); SA (56.09)/(2.94)/(232.59)); tax-accrual YoY CFO swing +364.50 vs +498.87 reported"
  - "L1-S3: rev L529 'deferred tax payment' -> 'unpaid current tax'"
  - "L1-S4: rev L477 -> 'falls due under the remaining advance-tax instalments by year-end'"
  - "L1-S5: rev L691 '43.13 revenue' -> '43.13 at cost (inventory release)'"
  - "L1-S6: A2 ledger header and placement housekeeping (results L3, L13, L54-55; presentation L6, L9)"
analyst_note: "All eight prior items are closed. F1, M1-M5, C1 and C2 each tie to the fulltext. The patched rows match it word for word, and every new number recomputes: tax-accrual CFO/PAT 0.52 consolidated and 0.30 standalone, tax-accrual FCF (117.28) and (258.09), guide pace 2,225.96 with H2 YoY +46.69%, defence-book share 86.5%. Coverage is clean. One new fault sits in the loop 1 text. A4 took the para 7 net cash flow of (0.29) as proof that H1 profit never became cash anywhere in the group. That figure comes after capex, deposits and debt, and no subsidiary CFO is filed. At group level the non-parent entities placed 52 in deposits, repaid 81 of debt and spent 55 on capex in H1. Those uses cannot be split by paragraph. The bear claim fails the same evidence bar a bull claim must meet (Rule J). The fix is a text-only restatement plus a Reading C. No number in any table changes, so A4 alone re-runs."
```
