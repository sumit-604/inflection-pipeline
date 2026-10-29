# SYNGENE Q2 FY27: A5 ADVERSARY / COMPLETENESS RE-AUDIT (correction loop 1 of 1)

Company: Syngene International Ltd (SYNGENE) | Quarter: q2fy27 | Agent: A5 adversary | model: claude-opus-5-5 | re-audit date: 2026-10-28 | loop: 1
Under audit: runs/syngene-q2fy27/work/review_syngene_q2fy27.md (A4 loop 1, 714 lines)
Baseline: runs/syngene-q2fy27/work/review_syngene_q2fy27.loop0.md (686 lines) and the loop-0 audit runs/syngene-q2fy27/work/audit_syngene_q2fy27.loop0.md (verdict INCOMPLETE, nine looped items).
Inputs re-checked: A1 fulltexts and structured files for results, presentation, press release and disclosure, and the A2 ledgers. No source PDF and nothing under inputs/ was opened.

Anchor key: res / deck / PR / disc = A1 fulltext line; review l.N = line in the loop-1 review; loop0 l.N = line in the loop-0 review; R### = structured row ID.

---

## TASK 1: VERIFICATION OF THE NINE LOOPED ITEMS

| Item | Tag (loop 0) | Loop-1 text (review line) | Re-check against A1 | Status |
|---|---|---|---|---|
| F1 | FACTUAL | l.227: "Q1 normalised tax credit of 6.7 exceeded the Q1 pre-exceptional loss of 5.7 (PR L405-406; deck l.670-671) ... PAT before exceptional of +1.0 (PR L407). After exceptional items, the total Q1 credit of 10.2 is smaller than the 19.2 loss (res l.90, l.94)" | PR L405 Q1 FY27 PBT (57); PR L406 tax 67 (credit); PR L407 PAT pre-exc 10 Mn; deck l.670-672 PBT -6, Tax -7, PAT 1; res l.90 (192), res l.94 (102). Agrees with the Step 1 ETR cell (l.124). | RESOLVED |
| F2 | FACTUAL | l.65: "0.73 (729,727 x Rs 10 = Rs 7.30 Mn, res l.471; paid-up +Rs 0.8 Cr on rounded Mn, res l.103)" | res l.471: 729,727 shares at Rs 10 = Rs 7,297,270 = Rs 0.73 Cr. res l.103: 4,029 to 4,037 Mn. | RESOLVED |
| F3 | FACTUAL | l.195: "no new manufacturing capacity commissioned in H1. A Clinical Translational Sciences (CTS) laboratory ... was commissioned in Q2 (PR L175; deck l.130). Its capex and capacity are not stated." Plus Q32 (l.461). | PR L175 "Syngene commissioned a new Clinical Translational Sciences (CTS) Laboratory in Bengaluru" (R749). deck l.130 "Commissioned a Clinical Translational Sciences laboratory" sits on the "Q2 FY27 performance" slide (deck l.111; R022). No capex figure in any extract. | RESOLVED |
| M1 | MISSING | l.37: letter dated 23-Oct-2026 (disc l.64, l.144; R043, R054); filing dated 27-Oct-2026 (disc l.19; R039) citing Regulation 30(6) (disc l.60; R069); "As discussed" (disc l.155); receipt date NOT FOUND; no breach asserted; [INFERENCE] label. Plus Q33 (l.462) and YAML flag (l.700). | disc l.64 "dated October 23, 2026"; disc l.144 "October 23, 2026"; disc l.19 "Date: October 27, 2026"; disc l.60 "Regulation 30(6)"; disc l.155 "As discussed". All anchors exact. | RESOLVED |
| M2 | MISSING | l.173: "underlying" replaced by "ex-hedge"; "(349.7 - 66.1) / 1,568.7" = ~18.08%; upper bound; composition and Q2 share NOT FOUND; hedge recurs, net derivative liability 96.5. Plus Brief l.538 and YAML flag l.701. | 349.7 = 238.2 + 111.5 (res l.86-88 derived); 66.1 = 124.6 - 58.5 (res l.477); 283.6 / 1,568.7 = 18.079%. 96.5 = (196 + 1,043 - 248 - 26) Mn (res l.145, l.158, l.172, l.184). Grep finds no "underlying" left in the review body. | RESOLVED (wording note L1-S3, anchor note L1-S4) |
| M3 | MISSING | l.297-298 (6A Q2 and H1 rows) and l.324 (watchlist #5): "GREEN on reported rupee revenue. Cash has not confirmed it: other current liabilities fell Rs 313.4 Cr (-40%) in H1 and H1 CFO was (143.2) (res l.188, l.226). Q6 decides..." Plus YAML flag l.704. | res l.188 7,808 to 4,674 Mn = 313.4 Cr, 40.1%; res l.226 (1,432) Mn. | RESOLVED (payload alignment note L1-S5) |
| M4 | MISSING | l.75: asset acquisition under Ind AS 103; CWIP 298.1 + land 31.1 = ~329.2 at 31-Mar-2025 (PR L444-446); CWIP 298.1 to 487.6, +189.5, +63.6% (res l.476); all-in at least 518.7; no target PAT so no earnings multiple; no revenue until FY28 (PR L160); carry ~132/yr. Plus YAML flag l.705. | PR L445 Rs 2,981 Mn CWIP and Rs 311 Mn land; PR L444 "asset acquisition under Ind AS 103"; res l.476 Rs 4,876 Mn; 487.6 - 298.1 = 189.5; 189.5 / 298.1 = 63.57%; 487.6 + 31.1 = 518.7; 66.1 x 2 = 132.2; PR L160 "next financial year". | RESOLVED |
| C1 | CONTRADICTION | l.373: 6D "CDMO share > 22%" set to **UNKNOWN** (MGMT claim unquantified; filed mix evidence neutral; matches 6B row 2). | 6B row 2 (l.321) reads UNKNOWN. Grep finds no "ON TRACK" left in the review. PR L130 (claim), PR L391 (23.9% vs 23.6%). | RESOLVED (log-wording note L1-S7) |
| C2 | CONTRADICTION | l.381: TTM PAT 186.1 on the results basis (316.7 - 153.8 + 23.2; res l.95) is primary, beside fact-sheet 184.2 (PR L409); "FILED CONFLICT" on 314.8 vs 316.7; gap in H2 FY26 (161.0 vs 162.9), traced to net-of-tax exceptional items. Plus Q34 (l.463) and YAML flag l.706. | res l.95: 3,167 - 1,538 + 232 = 1,861 Mn. PR L409: 867 + 671 + 150 + 1,460 = 3,148 Mn; 150 + 1,460 = 1,610 vs 1,629. Grep: 184.2 appears only at l.381, l.610 and l.706. No downstream cell still treats 184.2 as primary. | RESOLVED |

All nine looped items are resolved and correctly anchored.

---

## TASK 2: DRIFT CHECK (loop-1 review vs loop-0 copy)

Method. I read both versions line by line. Two grep tests back the read.

1. **Line-count reconciliation.** The loop-0 review ends at l.686 and the loop-1 review at l.714, so the delta is +28. Expected additions: Q32-Q34 (+3), Brief §1 line l.538 (+1), the "Correction loop 1" section l.598-615 (+18), YAML `loop: 1` (+1), YAML questions Q32-Q34 (+3), YAML flags l.705-l.706 (+2). Total +28. Every section heading after each insertion moves by exactly the insertion count. Examples: Prior-quarter table 469 to 472, MONITORABLES 485 to 488, STEP 9 511 to 514, BRIEF 523 to 526, Brief §2 547 to 551. No other line was added or deleted.
2. **Basket A** (numbers and labels the patches touch: 832.7, 147.4, 143.2, 313.4, 66.1, 238.2, 61.4, 25.07, 17.70, -421, -725, 53.3, 48.0, 1,140.6, 487.6, 96.5, 166.7, T3, T4, FIRED, UNKNOWN, GREEN, RED, NOT FOUND, INFERENCE). Matching lines went from 118 to 131, +13. I traced all 13:
   - 8 come from added lines: Q33 l.462, Brief l.538, log rows M1/M2/M3/M4/C1, flag l.705.
   - 5 come from patched lines that newly carry a term: l.37, l.75, l.298, l.373, l.700.
   - None is unexplained.
3. **Basket B** (terms no patch should touch: 910.6, 199.5, 21.91, 69.8, 85.2, 67.1, 1,785.1, 3,738.7, Zoetis, BMS, Aragen, Bicara, BIOSECURE, SHALLOW WATCH, A3P-, A3R-, A3-NN, Notion §, bps, x0.1, "(computed)"). Matching lines are 193 in both versions. Delta 0, as predicted.

Changed in-place lines found: l.37, l.65, l.75, l.173, l.195, l.227, l.297, l.298, l.324, l.373, l.381 (body), and YAML flags l.700, l.701, l.704. Each maps to one of the nine items. The three YAML flag edits are dependency alignment for M1, M2 and M3. They are permitted, and each is accurate.

**Drift outside the nine items: none.** The Step 1, standalone, Step 2, Step 3, Step 4, Step 5, 6B (other rows), 6C, tripwire, 6D (other rows), Step 7, Step 8, Q1-Q31, monitorables, Notion payload, Brief §2-§5 and A4 analyst_note lines are identical to loop 0.

---

## TASK 3: NEW QUESTIONS Q32-Q34 AND ADDED NUMBERS

| Q | Text (review line) | Anchors checked | Status |
|---|---|---|---|
| Q32 | CTS laboratory capex and revenue line (l.461; YAML l.673) | PR L175 and R749 (PR structured row: page 3, line 175, ENTITY, "Clinical Translational Sciences (CTS) Laboratory, Bengaluru"). deck l.130 and R022 (deck structured row: page 6, line 130, ENTITY). | ANCHORED (fork note L1-S2) |
| Q33 | Receipt date of the 23-Oct-2026 letter (l.462; YAML l.674) | disc l.64, l.144 (letter date); disc l.19 (filing date); disc l.60 (Reg 30(6)); R043 (page 1, line 64), R054 (page 4, line 144), R039 (line 19), R069 (line 60). | ANCHORED (fork note L1-S1) |
| Q34 | Fact-sheet FY26 quarters 314.8 vs audited 316.7 (l.463; YAML l.675) | PR L408-409 (exceptional and PAT after exceptional rows); res l.95. 314.8 = 86.7 + 67.1 + 15.0 + 146.0. | ANCHORED |

Added numbers recomputed (Audit 2 extension):

| Metric | Loop-1 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Note 4 impact | 0.73 | 7,297,270 / 10^7 = 0.730 | res l.471 | PASS |
| Q1 pre-exc credit vs loss | 6.7 vs 5.7, PAT +1.0 | 67, (57), 10 Mn | PR L405-407 | PASS |
| H1 ex-FX margin, pre-op expensed | ~18.08% | 283.6 / 1,568.7 = 18.079% | res l.76, l.86, l.477 | PASS |
| Brief rounding | 22.3% to ~18.1% | 22.29% to 18.08% | as above | PASS |
| Bayview price | ~329.2 | 298.1 + 31.1 | PR L445 | PASS |
| Bayview cost growth | +189.5, +63.6% | 487.6 - 298.1; / 298.1 = 63.57% | res l.476; PR L445 | PASS |
| Bayview all-in | at least 518.7 | 487.6 + 31.1 (land at Mar-2025 value) | res l.476; PR L445 | PASS |
| Pre-op carry | ~132/yr | 66.1 x 2 | res l.477 | PASS |
| OCL fall | 313.4, -40% | 780.8 - 467.4; 40.1% | res l.188 | PASS |
| TTM PAT results basis | 186.1 | 316.7 - 153.8 + 23.2 | res l.95 | PASS |
| Fact-sheet FY26 sum; H2 split | 314.8; 161.0 vs 162.9 | 86.7 + 67.1 + 15.0 + 146.0; 15.0 + 146.0; 316.7 - 153.8 | PR L409; res l.95 | PASS |

Arithmetic mismatches remaining: none.

---

## AUDITS 0-3 STATUS AT LOOP 1

- **Audit 0, deliverable completeness.** narrative PRESENT (l.531-549, 19 lines, inside the 10-20 band after the M2 line was added) | sector PRESENT (l.552-558) | business_model PRESENT (l.561-569) | competition PRESENT (l.572-578) | forward_map PRESENT (l.581-594; 10 dated rows, each with a bull and a bear fork). **PASS.**
- **Audit 1, coverage.** The ledgers and structured files are unchanged since loop 0. The counts stand: results 828 / 9 / 227 / 15 / 1 / 12 / 5 / 4; deck 350 / 32 / 45 / 10 / 7 / 1; PR 879 / 13 / 15 / 139 / 12 / 18; disclosure 71. orphan_rows [] and missing_from_ledger []. Both loop-0 row-to-review failures are cleared. PR R749 and deck R022 are now cited (l.195, l.461). Disclosure R043, R054, R039 and R069 are now cited (l.37, l.462). **PASS.**
- **Audit 2, arithmetic.** Loop-0 rows 28, 29 and 57 now pass (F1, F2, C2). The 59 loop-0 passes stand, because the drift check shows those lines unchanged. The added numbers pass (table above). **PASS.**
- **Audit 3, adversarial.** The four surviving loop-0 counters are now in the review:
  - P1 (revenue beat; M3) at l.297-298, l.324 and l.704.
  - P2 (ex-FX margin; M2) at l.173, l.538 and l.701.
  - P3 (CDMO share; C1) at l.373.
  - The Bayview acquisition probe (M4) at l.75 and l.705.
  The patches add no new positive claim, because every change is bearish or neutral. The three most positive claims are unchanged and each now carries its counter. The acquisition probe stands: Bayview's ~Rs 329.2 Cr against a target PAT of nil gives no earnings multiple, and the cost to date is +63.6%. The Rs 2.5 Cr stake and Unit 3 need no graft (loop-0 reasoning holds). **PASS.**

---

## VERDICT

**COMPLETE.** No FACTUAL, MISSING or CONTRADICTION finding remains. All nine loop-0 items are resolved, nothing drifted outside them, and Q32-Q34 are anchored correctly. The remaining findings are STYLE only. They are logged below and loop nowhere. The review may proceed to the operator-approval Notion gate.

---

## STYLE NOTES

### New at loop 1 (logged; no re-run)
- **L1-S1.** Q33 forks (l.462): "on or after 26-Oct-2026" against "23-Oct-2026" leaves 24-25 Oct unassigned. Any timeliness test runs from the filing stamp, 27-Oct-2026 20:06:13 (disc l.85; R011), not from a calendar date. The 24-hour rule itself is not in the extract. Suggest "received within 24 hours of the 27-Oct 20:06 filing" against "received earlier".
- **L1-S2.** Q32 forks (l.461) test disclosure, not outcome. "Revenue line" is undefined under a single reported segment (res l.495). Suggest "research or CDMO revenue".
- **L1-S3.** "Upper bound" at l.173, l.606 and l.701 is ambiguous. The Rs 66.1 Cr adjustment is the upper bound, so ~18.08% is the floor of the H1 ex-FX margin, not a ceiling. The ambiguity started in my loop-0 graft text.
- **L1-S4.** At l.173 the 96.5 net derivative liability is anchored to A3-10 only. Add res l.145, l.158, l.172, l.184 so the number is anchored to filed lines. The same applies at l.333, unchanged from loop 0.
- **L1-S5.** Two summary lines were not aligned with M2 and M3:
  - The Notion Key Notes prefix (l.520) still reads "op margin 17.7% (ex-FX 25.1%)" and "above Rs 790 Cr base path".
  - Brief §1 l.534 still reads "Revenue beat the Notion base path".
  The numbers are correct, and the qualifiers sit in the body (l.173, l.297-298, l.324, l.538) and in YAML flags l.701 and l.704. At the payload-approval gate the operator may want "(ex-FX flattered; ~18.1% H1 with pre-op expensed)" and "(not cash-confirmed)" added to the Notion line. These are unchanged lines, not drift.
- **L1-S6.** The correction-log header (l.598) points to audit_syngene_q2fy27.md, which this re-audit overwrites. The loop-0 audit it answers now sits at audit_syngene_q2fy27.loop0.md.
- **L1-S7.** The log verdict line (l.612) says "None of the nine fixes moves a tripwire, trigger or the cash classification". That is true for R1-R3, T1-T10 and cash. But C1 moved a 6D growth-trigger status, CDMO share, from ON TRACK to UNKNOWN (l.373). Name it.

### Carried from loop 0 (S1-S8; status in the loop-1 review)
| ID | Note | Status |
|---|---|---|
| S1 | The seasonality sentence omits the FY26 Q1-to-Q2 step of +4.1% (PR L378). The conclusion holds on the 3-year average of 9.8%. | Open (l.193 unchanged) |
| S2 | Forward Map rows ~6-Nov and 5-Nov are out of date order. | Open (l.585-586 unchanged) |
| S3 | Brief "A forex hedge loss of Rs 61.4 Cr caused most of that fall [FILED]" should be tagged [FILED, computed]. | Open (l.536 unchanged) |
| S4 | Step 7 cites disc l.43-58 for "discovery heads leaving". The departure is in PR L153-154 only. | Open (l.393 unchanged) |
| S5 | T5 "flat H2" is undefined. It means H2 FY27 revenue equal to H2 FY26 (1,953.6). | Open (l.358 unchanged) |
| S6 | The PR headline "6 percentage points" is 5.4 pp on filed figures (PR L42, L74, L131). | Open (optional) |
| S7 | A1 disclosure structured anchors drift 1-8 lines on boilerplate rows. The material rows are correct. | Open (A1 maintenance, outside A4) |
| S8 | deck l.369 bullet has no structured row. A4 cites the fulltext correctly. Not an A2 category. | Logged; no action |

---

```yaml
stage: A5-adversary
company: "SYNGENE"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
loop: 1
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
loop0_items_resolved: [F1, F2, F3, M1, M2, M3, M4, C1, C2]
drift_outside_patches: none
findings_by_type:
  factual: []
  missing: []
  contradiction: []
  style:
    - "L1-S1: Q33 forks leave 24-25 Oct unassigned; any timeliness test runs from the 27-Oct-2026 20:06:13 filing stamp (disc l.85, R011)"
    - "L1-S2: Q32 forks test disclosure only; 'revenue line' undefined under one segment (res l.495)"
    - "L1-S3: 'upper bound' at l.173, l.606, l.701 is ambiguous; the 66.1 adjustment is the upper bound, so 18.08% is the floor of the H1 ex-FX margin"
    - "L1-S4: 96.5 net derivative liability at l.173 anchored to A3-10 only; add res l.145, l.158, l.172, l.184"
    - "L1-S5: Notion Key Notes prefix (l.520) and Brief l.534 not aligned with M2/M3 qualifiers; numbers correct; qualifiers sit in body and YAML flags l.701, l.704"
    - "L1-S6: correction-log header (l.598) points to the audit path this re-audit overwrites; loop-0 audit is audit_syngene_q2fy27.loop0.md"
    - "L1-S7: log line l.612 says no trigger moved; C1 moved the 6D CDMO share growth-trigger status from ON TRACK to UNKNOWN"
loop_back_to: ""
gap: ""
style_notes:
  - "L1-S1 (new): restate Q33 forks against the filing timestamp"
  - "L1-S2 (new): Q32 forks to name research or CDMO revenue"
  - "L1-S3 (new): call 18.08% the floor, the 66.1 adjustment the upper bound"
  - "L1-S4 (new): anchor 96.5 to res l.145, l.158, l.172, l.184"
  - "L1-S5 (new): add ex-FX and cash qualifiers to the Notion Key Notes line at the approval gate"
  - "L1-S6 (new): repoint the correction-log header to audit_syngene_q2fy27.loop0.md"
  - "L1-S7 (new): name the C1 6D status change in the log verdict line"
  - "S1 (carried, open): add FY26 Q1-to-Q2 step (+4.1%) to the seasonality sentence"
  - "S2 (carried, open): reorder Forward Map rows by date"
  - "S3 (carried, open): retag Brief l.536 as [FILED, computed]"
  - "S4 (carried, open): cite PR L153-154 for discovery heads leaving (l.393)"
  - "S5 (carried, open): define 'flat H2' in T5 (l.358)"
  - "S6 (carried, open): optional note that the '6 pp' headline is 5.4 pp"
  - "S7 (carried, open): A1 disclosure anchor drift on boilerplate rows"
  - "S8 (carried, logged): deck l.369 bullet has no structured row; no ledger gap"
analyst_note: "All nine loop-0 items are fixed and anchored to the right A1 lines. The drift test was a full line-by-line read plus two grep baskets. Line count rose by exactly the 28 added lines. Basket A rose by 13, all traced to patches. Basket B, which no patch touches, was unchanged at 193. So nothing moved outside the nine items. Q32-Q34 cite correct rows. What remains is style. The one item worth the operator's eye is L1-S5. The Notion Key Notes line still shows ex-FX 25.1% and the base-path beat without the qualifiers the body now carries. Fix it at the approval gate, not by another loop. The 'upper bound' wording in L1-S3 started in my own loop-0 graft text."
```
