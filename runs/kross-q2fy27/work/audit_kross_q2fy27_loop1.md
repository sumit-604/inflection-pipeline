# A5 AUDIT, LOOP 1 RE-AUDIT: Kross Limited (KROSS), Q2 FY27

Agent: A5 adversary / completeness auditor | model claude-opus-5-5 | date 2026-10-20
Instruction file: prompts/quarterly-a5-adversary.md
Prior audit: runs/kross-q2fy27/work/audit_kross_q2fy27.md (INCOMPLETE; F7 FACTUAL, F1-F6 MISSING)

Scope (from the task message): (1) confirm each prior FACTUAL / MISSING finding is closed; (2) re-run the deliverable-completeness gate and the coverage audit (M001 added to the PPT ledger; PPT-FN-18 added by A3); (3) check new or changed text for new FACTUAL / MISSING / CONTRADICTION errors, arithmetic included. No new full adversarial pass on unchanged text. Concall sections read "pending Role 5 addendum" by design (REV L4, L437-L440, L574-L580); not failed.

Inputs read (and only these):
- A4 review: runs/kross-q2fy27/work/review_kross_q2fy27.md (L1-L817; part 1 and part 2 concatenated; Loop 1 change log L794-L816)
- A1 fulltexts: extracted/kross-results-q2fy27-fulltext.md (RES), extracted/kross-pressrelease-q2fy27-fulltext.md (PR), extracted/kross-presentation-q2fy27-fulltext.md (PPT)
- A1 structured: the three *-structured.md files (RES R001-R372, PR R001-R135, PPT R001-R665)
- A2 ledgers: work/ledger_results_kross_q2fy27.md, work/ledger_pressrelease_kross_q2fy27.md, work/ledger_presentation_kross_q2fy27.md

Not read: the source PDFs, anything under inputs/, A3 forensic notes (PPT-FN-18 is checked only as A4 cites it), orchestrator commentary. No source access was needed; no pipeline error to report.

Anchor key: RES / PR / PPT Lnnn = fulltext line. REV Lnnn = line in the concatenated A4 review under audit. R### = A1 structured row. M001 = A2 ledger-only row. Units: RES and PR in Rs Mn (Rs Cr = Mn x 0.1); PPT in Rs Cr.

---

## A. PRIOR FINDINGS: CLOSURE CHECK

| Prior ID | Type | Required fix | Evidence in the revised review / ledger | Status |
|---|---|---|---|---|
| F1 | MISSING (A2, A3, A4) | Ledger unit for PPT p15 L341-L346; forensic line; 6D and Q13 | A2: PPT ledger L11 (missing_from_structured 1), L15, L17-L20 (M001, verbatim text, CONFLICT flag, cross-refs to R390-R392, R049/R057, R063). A4: preamble REV L31; 6B #5 REV L392; 6D REV L427 (both readings, separating observation); 6E REV L439; Q13 REV L526; M7 REV L557; M19 REV L569; disposition REV L592. PPT-FN-18 cited REV L33, L713. Text checked against PPT L341-L346 and L511-L515. | CLOSED |
| F2 | MISSING (A4) | Bear counter A (trough base; half-on-half plateau) | Step 2 diag 1 REV L171-L173; diag 3 REV L176-L178; Step 3 trajectory REV L217-L219; 6D REV L431; brief REV L639-L640, L652; flag 11 REV L627; YAML flag REV L776. Numbers recomputed (Section D). | CLOSED |
| F3 | MISSING (A4) | Bear counter B (about 81% of QoQ step from trailer half and top 5) | Step 4 note B REV L249-L251; 5.5C REV L343; Q3 REV L511; flag 5 REV L627; brief REV L643; YAML REV L775. Numbers recomputed. | CLOSED |
| F4 | MISSING (A4) | Bear counter C (PAT and EPS at Base only with unexplained OI) | 6A reading 2 REV L374-L380; 6B note REV L400; 8A-W REV L470-L474; Q4 REV L512; flag 10 REV L627; YAML REV L777. Numbers recomputed. | CLOSED |
| F5 | MISSING (A4) | Cite other non-current assets; capex and FCF on both bases; Q11/Q22 | Step 5 REV L264, L277-L282, L303; 6C REV L413; pillar table REV L455; Q22 REV L535; M12 REV L562; flags REV L627, L771-L772. Row IDs R225, R226, R333, R334 confirmed at RES structured lines 242-243, 350-351. | CLOSED |
| F6 | MISSING (A4) | Cite FY22-FY26 revenue and gross margin; re-read 8C | Step 1 cross-check REV L145; Step 3 history table REV L201-L213; 6D REV L430; pillar REV L457; 8C REV L489-L494; brief REV L660, L670, L688. Values tie to PPT L617, L620 and R416-R435. | CLOSED |
| F7 | FACTUAL (A4) | Fix "Forward EPS dilution up to 4.65%" | Every copy corrected: REV L68, L78, L453, L781, L788. Share count +4.65%, EPS -4.44% (equity leg -2.27%). | CLOSED |
| S1-S10 | STYLE | Logged only | S2-S8 and S10 applied (change log REV L805-L814, checked at REV L216, L285, L254, L179/L243, L248, L288, L370/L397, L522). S9 needed no change. S1 residual noted at S-L7 below. | logged |

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

DELIVERABLE-COMPLETENESS AUDIT: narrative PRESENT | sector PRESENT | business_model PRESENT | competition PRESENT | forward_map PRESENT. Gate PASSES.

| Part | Heading in review | Content check | Status |
|---|---|---|---|
| 1. Summary narrative | "### 1. Summary narrative" REV L635 | 17 lines (REV L636-L652), inside the 10-20 line band. Carries the new base-effect and concentration lines (REV L639-L640, L643), both readings and two separating observations (REV L650-L652). | present |
| 2. Sector intelligence | "### 2. Sector intelligence" REV L654 | 7 lines (REV L655-L661); adds FY24-FY25 flat revenue (REV L660). | present |
| 3. Business-model intelligence | "### 3. Business-model intelligence" REV L663 | 13 lines (REV L664-L676); adds FY22-FY26 gross-margin band (REV L670). | present |
| 4. Competition intelligence | "### 4. Competition intelligence" REV L678 | 7 lines (REV L679-L685). | present |
| 5. Forward map | "### 5. Forward map" REV L687 | Make-or-break line (REV L688) plus 8 catalysts, each with a bull and a bear fork (REV L692-L699). Present and non-empty. One row carries an internal contradiction (finding C1, Section E); that is a content error, not an empty part. | present |

---

## 1. COVERAGE AUDIT (re-run)

Method. (a) Fresh grep over the three A1 fulltexts for page markers, statement lines in the image transcriptions and ZERO_STANDING dashes. (b) Fresh grep count of structured row IDs per document. (c) PPT ledger row count, including the new M001 section. (d) Targeted re-sweep of PPT p15 (the slide of the prior gap) against its structured rows R313-R333. (e) Ledger rows checked against A4: cited, or covered by A4's explicit all-reviewed statement (REV L22, L28, L38), with the two previously uncited material groups re-checked.

| Document | Category | A2 count | Fresh count (A5) | Orphan rows | Status |
|---|---|---|---|---|---|
| RES | pages | 7 | 7 ([page N] markers) | none | PASS |
| RES | numbered notes | 7 (+2 footnotes R059, R060) | 7 (unchanged A1 text; RES L224-L249) | none | PASS |
| RES | line items | 304 | 304 = 24 P&L lines x 6 (RES L412-L435) + 35 BS x 2 (RES L438-L472) + 45 CF x 2 (RES L475-L519) | none | PASS |
| RES | ZERO_STANDING | 18 | 18 (RES L424 x3, L435 x5, L478 x2, L481, L482, L499, L503 x2, L507, L509 x2) | none | PASS |
| RES | agenda / auditor paras / entities / superseded | 2 / 4 / 0 / 21 | 2 / 4 / 0 / 21 (ledger header unchanged, RES ledger L4-L13) | none | PASS |
| RES | all structured IDs | 372 | 372 (grep of ^R### rows) | none | PASS |
| PR | pages / table cells / active numbers / superseded | 2 / 42 / 57 / 42 | 2 / 42 / 57 / 42 (ledger header unchanged, PR ledger L5-L16) | none | PASS |
| PR | all structured IDs | 135 | 135 | none | PASS |
| PPT | slides | 38 | 38 | none | PASS |
| PPT | all structured IDs | 665 | 665; PPT ledger lists 686 R-rows = 665 IDs + 21 superseded-ID accounting rows | none | PASS |
| PPT | missing_from_structured | 1 (M001) | 1: p15 L341-L346 "Established foundry Unit-V, a high-pressure mould line along with its machine shop" | none | PASS (prior F1 closed) |
| PPT | p15 re-sweep | n/a | Remaining p15 events are historical (incorporation, first supplies, early customers) or carried elsewhere with rows (tipping jack p10, extrusion p9, Leax AB entity R331). No further material unit. | n/a | PASS |
| All | ledger rows cited in A4 or marked reviewed | 1,173 (1,172 + M001) | 372 + 135 + 665 + 1 = 1,173, matching REV L22. RES R225/R226/R333/R334 now cited (REV L264, L278-L279). PPT R416-R435 now cited (REV L145, L201). PPT R436-R438 (deck CAGR headlines) sit under the all-reviewed statement only (STYLE S-L3). | none | PASS |

Coverage result: no orphan row, nothing missing from the ledger.

---

## 2. ARITHMETIC AUDIT (new and changed figures)

Method: each figure added or changed in loop 1 recomputed in Rs Mn from RES L412-L519 (image transcriptions govern) or from PPT L395-L397, L617-L620, L785-L788, then converted. Tolerance: last displayed digit. Unchanged Step 1-6.5 figures passed in the prior audit and were not re-run.

| Metric (review line) | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Share count on full conversion; equity leg (REV L68, L78, L453) | +4.65%; +2.33% | 3.0 / 64.51 = 4.650%; 1.5 / 64.51 = 2.325% | RES L238, L434 | PASS |
| EPS dilution full; equity leg (REV L68, L78, L453, L781) | -4.44%; -2.27% | 1 - 64.51/67.51 = 4.444%; 1 - 64.51/66.01 = 2.272% | RES L238, L434 | PASS |
| FY26 COGS and GM tie to deck (REV L145) | 365.48 Cr; 45.71% | 3,644.74 + 10.02 = 3,654.76 Mn; 1 - 3,654.76/6,732.01 = 45.711% | RES L415-L416; PPT L618, L620 | PASS |
| Q2 FY26 vs Q1 FY26; vs H2 FY26 avg qtr (REV L171) | -6.1%; 35.0% below | 1,309.20 / 1,393.55 = 0.9395; 1,309.20 / 2,014.63 = 0.6499 | RES L412 | PASS |
| FY26 revenue growth (REV L171) | +8.5% | 673.2 / 620.4 = 1.0851 | PPT L617 | PASS |
| H2 FY26 / H1 FY26 (REV L171, L222, L452) | 1.49x | 4,029.26 / 2,702.75 = 1.4908 | RES L412 | PASS |
| H1 FY27 vs H2 FY26 revenue (REV L171, L217, L640) | +4.1% | 4,194.31 / 4,029.26 = 1.0410 | RES L412 | PASS |
| Bull reading: de-seasonalised H2 FY26; H1 FY27 above it (REV L172) | 350-366 Cr; about 15-20% | 4,029.26/1.15 = 3,503.7, /1.10 = 3,663.0 Mn; 4,194.31 / 3,663.0 = +14.5%, / 3,503.7 = +19.7% | RES L412; PPT L102 | PASS ("about") |
| Separating test H1 x 1.10-1.15 (REV L173, L219, L475, L652, L699) | 461-482 Cr | 4,613.7 to 4,823.5 Mn | RES L412 | PASS |
| H1 FY27 vs H2 FY26 core PBT ex-OI (REV L176, L640) | -12.1% (42.38 vs 48.23) | 423.81 / 482.32 = 0.8787 | RES L413, L422 | PASS |
| Q2 FY27 core PBT vs H2 FY26 avg qtr (REV L176) | +2.8% | 247.81 / 241.16 = 1.0276 | RES L413, L422 | PASS |
| H2 FY26 operating margin (REV L176, L216) | 14.15% | (879.47 - 309.21) / 4,029.26 = 14.153% | RES L412-L422 | PASS |
| ETR split (REV L179, L243) | 4.68 pp fall; 0.98 pp earlier-years; deferred 9.77% to 4.88%; current 20.88% to 22.09% | 31.648 - 26.964 = 4.684; 1.16/118.27 = 0.981%; 11.56/118.27 = 9.774%, 13.15/269.54 = 4.879%; 24.70/118.27 = 20.884%, 59.53/269.54 = 22.086% | RES L422-L426 | PASS |
| Q2 FY27 vs H2 FY26 avg qtr (REV L199) | +16.7% | 2,350.92 / 2,014.63 = 1.1669 | RES L412 | PASS |
| Q2 margin vs FY26 margin (REV L216) | 4.8 bps | 13.064 - 13.016 = 4.8 bps | RES L412-L422 | PASS |
| FY22-FY26 revenue and GM (REV L205-L209) | 297.5 / 488.6 / 620.3 / 620.4 / 673.2; 46.1 / 40.7 / 42.6 / 43.0 / 45.7% | as deck | PPT L617, L620; R416-R420, R431-R435 | PASS |
| Recurring share, prior-ETR basis (REV L248) | 82.5% | (116.02 - 11.26 x 0.68352 - 12.62) / 116.02 = 82.49% | RES L413, L422, L426 | PASS |
| Trailer half QoQ (REV L249) | 74.95 to 115.92 Cr; +40.97; 80.7% of 50.75 | 0.4066 x 1,843.39 = 749.52; 0.4931 x 2,350.92 = 1,159.24; 409.72 / 507.53 = 80.73% | PPT L395-L397; RES L412 | PASS |
| Component half QoQ (REV L249) | 109.39 to 119.17; +8.9% | 1,093.87 to 1,191.68 Mn; x1.0894 | PPT L395; RES L412 | PASS |
| Top-5 QoQ; others (REV L249) | 109.63 to 150.95; +41.32 Cr; 81.4%; others +12.6% | 1,096.26 to 1,509.53 Mn; +413.27 Mn (41.33 Cr on the Mn basis, 41.32 on rounded Cr); 81.43%; 747.13 to 841.39 = x1.1262 | PPT L788; RES L412 | PASS (rounding) |
| YoY trailer; components (REV L250) | +103.2% (57.05 to 115.92); +61.3% (73.87 to 119.17) | 570.55 to 1,159.24 = x2.0318; 738.65 to 1,191.68 = x1.6133 | PPT L395-L397; RES L412 | PASS |
| ETR vs statutory (REV L254) | about 180 bps | 26.964 - 25.168 = 179.6 bps | RES L426 | PASS |
| Other NCA balance (REV L278) | 46.66 to 50.35 Cr; +3.68 | 466.64 to 503.45 Mn; +36.81 | RES L444 | PASS |
| Other NCA investing line (REV L279) | +2.49 / -3.68; swing -6.17 | +24.90 / -36.81 Mn; -61.71 | RES L500 | PASS |
| Capex basis 2 (REV L280, L303) | 59.12 / 63.26 Cr; +7.0% | 609.88 + 6.20 - 24.90 = 591.18; 591.60 + 4.16 + 36.81 = 632.57; x1.0700 | RES L497-L498, L500 | PASS |
| FCF basis 1 change (REV L281) | +1.67 | -548.48 - (-565.16) = +16.68 Mn | RES L496-L498 | PASS |
| FCF basis 2 (REV L282, L413, L455, L627, L771) | -54.03 / -58.53; -4.50 | 50.92 - 591.18 = -540.26; 47.28 - 632.57 = -585.29; -45.03 Mn | RES L496-L500 | PASS |
| Inventory days (REV L285) | 105.42 / 87.41 to 85.95; -1.46 | 1,055.54 / 3,654.76 x 365 = 105.42; 1,055.54 / 2,197.84 x 182 = 87.41; 1,096.56 / 2,334.84 x 183 = 85.95 | RES L446, L415-L416 | PASS |
| Capitalised, PPE-only basis (REV L288, L303) | about 20.2 Cr | 143.07 + (62.34 - 2.99 RoU/intangible amortisation) = 202.42 Mn | RES L438, L440-L441, L419, L498 | PASS |
| Closing-CE ROCE (REV L368, L370, L397, L412, L454) | 15.48% vs 15.29% | 992.98 / 6,416.35 = 15.476%; 831.12 / 5,434.87 = 15.292% | RES L418, L422, L455-L464 | PASS |
| Reading 2: OI after tax; H1 PAT ex-OI; Q1+Q2 basis (REV L374-L375) | 10.65 Mn; 32.10 Cr; 31.93 Cr | 14.43 x (1 - 0.26216) = 10.65; 331.63 - 10.65 = 320.98; 329.98 - 10.65 = 319.33 | RES L413, L426-L427, L480, L483, L565 | PASS |
| Reading 2 EPS (REV L376) | 4.98 / 4.86 | 320.98 / 64.51 = 4.976; / 66.01 = 4.863 | as above | PASS |
| Reading 2 count (REV L377, L472) | 2+2 current; 1+3 post-allotment | revenue 419.43 > 415; margin between; PAT 32.10 in 28.0-32.5; EPS 4.98 >= 4.95, 4.86 < 4.95 | REV L363-L366 | PASS |
| H2 share of FY26; H1 shortfall (REV L379) | 59.9%; 0.4 Cr | 4,029.26 / 6,732.01 = 59.85%; 32.5 - 32.10 | RES L412 | PASS |
| EPS implied by deck QoQ (REV L522) | about Rs 3.05 | 2.06 x 1.479 = 3.047 | PPT L785; RES L432 | PASS |

Arithmetic result: no mismatch above rounding.

---

## 3. ADVERSARIAL READ (loop scope: new and changed text only)

The prior audit's three surviving counters (A: base effect; B: QoQ concentration; C: PAT at Base only with unexplained OI) are now in A4, each beside A4's view with a bull reading and a separating observation (Section A). Re-checked from the extract:
- Counter A graft: numbers tie (Section 2). The new bull reading at REV L172 rests on MGMT's "H2 is always 10-15% up than H1" (PPT L102). Its strongest counter, that FY26 H2 ran 1.49x H1, is already stated by A4 (REV L171, L222, Q18 REV L531). No new survivor.
- Counter B graft: numbers tie. The legend-reading caveat on PPT L788 is carried (REV L249, PPT-FN-04). No new survivor.
- Counter C graft: numbers tie. A4 applies the ex-OI basis consistently between trigger 1 and PAT (REV L400). No new survivor.
- New positive text: none beyond the bull readings above. The 8C level reading (REV L493) is framed as "kills the margin-recovery lever but is not a break", which is not a positive claim.

Mandatory acquisition-economics probe: DOES NOT FIRE. The A1 inputs are unchanged since the prior audit. "Investment in shares" is nil in both halves (RES L503), Note 5 records no subsidiary, associate or JV (RES L243-L244), and the non-current investment of 49.62 Mn is unchanged (RES L442). The nearest analogue, the ~Rs 167 Cr seamless tube plant, stays at 6B #8 (REV L395).

---

## E. NEW FINDINGS ON CHANGED TEXT

### C1 (CONTRADICTION, loop A4). Forward-map row "By 30-May-2027" contradicts 6A and 6B

Text (REV L699), a row changed in loop 1 (the Rs 461 Cr test was added from counter A):
- Bull fork: "Operating margin ex-other income at or above 14%, like-for-like debtor days lower, H2 revenue at or above Rs 461 Cr: trigger 1 fires"
- Bear fork: "Margin under 14%, days flat or higher, H2 revenue under Rs 461 Cr: the bear case becomes the working case"

What it contradicts:
1. Revenue. 6A (REV L363) puts the H2 FY27 revenue needed at 370.57 Cr for Bear, 410.57 Cr for Base and 460.57 Cr for Bull (FY27 790 / 830 / 880 Cr less H1 419.43 Cr, RES L412). The Rs 461 Cr line is the Bull H2 figure. An H2 of Rs 411-460 Cr gives FY27 revenue of Rs 830-880 Cr, which is Base to Bull. The fork calls that outcome "the bear case becomes the working case".
2. Margin. 6B #1 (REV L388) sets the red line, where the bear becomes the working case, at operating margin "at or below ~12.5%". A margin from 12.5% to 14% is AMBER there. The fork moves that line to 14%.
3. Trigger definition. Trigger 1 has two legs, margin above ~14% AND debtor days falling (REV L56, L400, L480). The bull fork adds H2 revenue as a condition of "trigger 1 fires".
4. The 461-482 Cr test's own purpose (REV L173, L219). It separates the seasonal reading of claim A (H1 is the weak half) from the plateau reading. It is not a Bear-case threshold.

Why it is not STYLE: the forward map is a hard-gate deliverable, and the operator reads the brief first. The fork tells the operator to adopt the Bear case on an outcome that the review's own 6A grades Base to Bull on revenue and 6B grades AMBER on margin. That changes a conclusion.

Fix (one row, A4): keep the three tests apart.
- Trigger 1 fires on its two legs only.
- H2 revenue against 461-482 Cr separates the seasonal reading from the plateau reading (Step 2).
- H2 at or above 410.57 Cr keeps FY27 revenue at Base or better (6A).
- The Bear case becomes the working case only at operating margin at or below ~12.5% (6B #1), or at H2 revenue below 370.57 Cr (below Bear, 6A).

The margin element may predate loop 1. The prior text is not available to this audit, and the prior audit did not flag it. It sits in a changed row, so it is in scope.

No new FACTUAL or MISSING finding.

---

## FINDINGS REGISTER (tagged)

| ID | Type | Finding | Line evidence | Loop |
|---|---|---|---|---|
| C1 | CONTRADICTION | Forward-map Q4 FY27 row: bear fork adopts the Bear case on margin under 14% and H2 revenue under Rs 461 Cr. 6B #1 puts the bear line at ~12.5%, and 6A shows H2 of Rs 410.57-460.57 Cr is Base to Bull. The bull fork also adds H2 revenue to trigger 1's two legs. | REV L699 vs REV L363, L388, L400, L480, L173 | A4 |
| S-L1 to S-L7 | STYLE | See STYLE NOTES | as listed | none |

Prior F1-F7: all CLOSED (Section A).

---

## VERDICT

VERDICT: INCOMPLETE.
- Failing agent: A4. One CONTRADICTION (C1): a single forward-map row (REV L699) conflicts with the review's own 6A H2 thresholds and the 6B #1 red line.
- loop_back_to: A4. No A2 or A3 work is needed. The ledgers reconcile (1,173 rows, no orphans, nothing missing), and all seven prior findings are closed.
- Not failing: the plain-language brief gate (all five parts present), the coverage audit, and the arithmetic (every new or changed figure ties within rounding).

---

## STYLE NOTES (logged; no re-run)

- S-L1. REV L31, L427, L594 say the p15 year cannot be resolved. That is a defensible reading of the text layer. Two points narrow it. The p15 timeline runs left to right, so Unit-V sits before "Publicly listed ... 16th September 2024" (PPT L341-L346). The 12 years and 12 events alternate between two rows (PPT L339-L355), and strict alternation gives 2022 (R321). Either reading puts an HPML in the past, which is consistent with p24's 2023. No reading changes.
- S-L2. p24 itself says the 2023 HPML foundry "will double casting capacity" (PPT L513-L515). That is the same doubling language as p5/p6 (PPT L116, L134-L135), and it leans toward A4's Reading A (same line). Optional cite in 6D (REV L427) and Q13 (REV L526). The separating observation is unchanged.
- S-L3. REV L30 says PPT R416-R438 are "now cited". The body cites R416-R435 (REV L145, L201). R436-R438 are the deck's FY22-FY26 CAGR headlines: revenue 23%, EBITDA 31%, PAT 46% (PPT L616, L622, L628). They sit only under the all-reviewed statement. Optional context: the 23% revenue CAGR is front-loaded (FY23 +64.2%; FY23-FY26 CAGR 11.3%, PPT L617).
- S-L4. The Key Notes payload (REV L617) reads "rev +79.6% YoY (+4.1% vs H2 FY26)". The 4.1% is H1 FY27 vs H2 FY26. Q2 vs the H2 FY26 average quarter is +16.7% (REV L199). Label it "H1 rev +4.1% vs H2 FY26" before the Notion save.
- S-L5. The forward-map Q3 bear fork (REV L697) reads "trailer and top-5 shares fall back". That outcome reads bear only with revenue below Q2. A fall-back with revenue held means diversification. Add the revenue condition.
- S-L6. The brief at REV L671 reads "Debtors, stock and other current assets take about 124 days of cash cycle". The 124.4-day CCC is receivable plus inventory less payable days (REV L283-L287). Other current assets are not in it. The number is right; the description is off.
- S-L7. Residual of prior S1: the concatenated file's header still says "this file is part 1" (REV L8). Cosmetic.

---

```yaml
stage: A5-adversary
company: "KROSS"
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
surviving_bear_counters: []
findings_by_type:
  factual: []
  missing: []
  contradiction:
    - "C1: Forward-map row 'By 30-May-2027' (review L699). Bear fork: 'Margin under 14%, days flat or higher, H2 revenue under Rs 461 Cr: the bear case becomes the working case'. This contradicts 6B #1 (review L388), where the bear becomes the working case at margin at or below ~12.5% and 12.5-14% is AMBER. It also contradicts 6A (review L363): H2 needed is 370.57 Bear, 410.57 Base and 460.57 Bull, so an H2 of Rs 411-460 Cr is FY27 revenue of Rs 830-880 Cr, Base to Bull. The bull fork adds H2 revenue to trigger 1, which has two legs, margin and debtor days (review L56, L400, L480). The 461-482 Cr test separates the seasonal and plateau readings (review L173); it is not a Bear threshold. Loop A4."
  style:
    - "S-L1: p15 Unit-V sits before the 16-Sep-2024 listing; strict two-row alternation gives 2022 (R321); 'year not resolvable' is defensible; either reading is past, consistent with p24 (PPT L339-L355)."
    - "S-L2: p24 says the 2023 HPML 'will double casting capacity' (PPT L513-L515), the same doubling language as p5/p6; leans to Reading A; optional cite at review L427, L526."
    - "S-L3: review L30 says R416-R438 cited; body cites R416-R435; R436-R438 (deck CAGRs 23/31/46%) only under the all-reviewed statement; revenue CAGR is front-loaded (FY23-FY26 CAGR 11.3%)."
    - "S-L4: Key Notes payload (review L617) '+4.1% vs H2 FY26' needs the 'H1' label; Q2 vs H2 FY26 avg qtr is +16.7% (review L199)."
    - "S-L5: Q3 bear fork (review L697) 'trailer and top-5 shares fall back' is bear only with revenue below Q2; add the revenue condition."
    - "S-L6: brief review L671 says other current assets are in the 124-day cash cycle; the CCC is receivable + inventory - payable days (review L283-L287)."
    - "S-L7: concatenated header (review L8) still says 'this file is part 1'."
loop_back_to: "A4"
gap: "A4: rewrite the forward-map row 'By 30-May-2027' (review L699) so it agrees with 6A and 6B. (a) Trigger 1 fires or stays unfired on its two legs only: operating margin ex-OI at or above ~14% AND like-for-like debtor days lower. (b) H2 FY27 revenue against Rs 461-482 Cr separates the seasonal reading from the plateau reading (Step 2 diag 1). It is not a Bear threshold, and H2 at or above Rs 410.57 Cr keeps FY27 revenue at Base or better (6A). (c) The Bear case becomes the working case only at operating margin at or below ~12.5% (6B #1) or H2 revenue below Rs 370.57 Cr (below Bear, 6A). No other change is required. Prior F1-F7 are closed, coverage reconciles at 1,173 rows, and every new figure ties."
style_notes:
  - "S-L1: p15 order places Unit-V before the Sep-2024 listing; alternation gives 2022; no reading changes."
  - "S-L2: cite p24 'will double casting capacity' (PPT L513-L515) as leaning to Reading A."
  - "S-L3: R436-R438 CAGR rows under blanket coverage only; align review L30 wording."
  - "S-L4: label the Key Notes '+4.1%' as H1 vs H2 FY26 before the Notion save."
  - "S-L5: add 'with revenue below Q2' to the Q3 share fall-back bear fork."
  - "S-L6: describe the 124-day CCC as receivable plus inventory less payable days."
  - "S-L7: header part-1 wording in the concatenated file."
analyst_note: "Loop 1 closes all seven prior findings. M001 is in the PPT ledger and the review cites it with both HPML readings. The three bear counters are grafted beside A4's view, with bull readings and separating observations. The other non-current assets line and the FY22-FY26 gross-margin history are cited. The dilution label is fixed in every copy. Coverage reconciles: 372 + 135 + 665 + M001 = 1,173 rows, no orphans, and the p15 re-sweep finds nothing else. Every new or changed figure recomputes within rounding. The one failure is a single forward-map row that mapped the new Rs 461 Cr seasonality test to 'the bear case becomes the working case'. Rs 461 Cr is roughly the Bull H2 figure in 6A, and 6B puts the bear line at ~12.5% margin, not 14%. A Base-to-Bull outcome would be labelled Bear in the deliverable the operator reads first, so this is a CONTRADICTION, not STYLE. The fix is one row with no A2 or A3 work. A re-check can be limited to that row."
```
