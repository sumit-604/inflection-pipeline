# A5 ADVERSARY / COMPLETENESS AUDIT, LOOP 1 RE-AUDIT - Gallantt Ispat Limited (GALLANTT) - Q2 FY27

Auditor: A5 (claude-opus-5-5), fresh context. Date: 2026-10-20.
Scope (orchestrator, loop 1): (1) confirm each prior item is closed; (2) re-run the deliverable-completeness gate; (3) check new or changed text for new FACTUAL / MISSING / CONTRADICTION errors, including arithmetic. No new full adversarial pass on unchanged text.
Inputs read: A4 review `runs/gallantt-q2fy27/work/review_gallantt_q2fy27.md` (689 lines, loop 1 revision, change log at A4 L673-L688); A1 fulltext `runs/gallantt-q2fy27/extracted/gallantt-results-q2fy27-fulltext.md` (statement transcription L1056-L1157); A1 structured `runs/gallantt-q2fy27/extracted/gallantt-results-q2fy27-structured.md`; A2 ledger `runs/gallantt-q2fy27/work/ledger_results_gallantt_q2fy27.md`; my prior audit `runs/gallantt-q2fy27/work/audit_gallantt_q2fy27.md`.
Not read: the source PDF, anything under `inputs/`, and A3 forensics.
Line references: "L" = fulltext line; "A4 L" = review line; "R" = structured row ID. Units are Rs lakhs unless marked Rs Cr (lakhs x 0.01).

---

## PRIOR-ITEM CLOSURE

| ID | Type | Prior gap | Where A4 fixed it (verified) | Status |
|---|---|---|---|---|
| F1 | FACTUAL | "Q2 weakest of its year / seasonal low" tagged as filed | A4 L200 (Step 3): states only Q2 < Q1 in both years and Q2 FY26 < H2 FY26 average; Q3/Q4 FY26 not split; seasonality INFERENCE only. A4 L370 (Step 6.5): "Seasonality is not shown by the filing". A4 L543-L544 (brief 2): FILED comparison plus "[FILED: absence]". A4 L546: "seasonal trough" survives only as an INFERENCE-tagged bull reading. Grep for "weakest" / "seasonal low" finds no residual filed claim. | CLOSED |
| M1 | MISSING | Traded-goods qualifier on the revenue growth | A4 L141 and L145 (proxy row, INFERENCE caveat); L155 (Step 2 row); L170-L173 (bear counter, bull reading, separating observation Q4); L201; L231; L397; L432-L433; L503; L523-L525; L555-L559; YAML L654 | CLOSED (wording note S9) |
| M2 | MISSING | FY26 loan origination; Rs 326.09 Cr L1098 pool; interest attribution re-tag | A4 L178 (attribution INFERENCE, L1098 named, accrued-interest tie); L272-L274 (loans origination, new L1098 row, pool row); L281, L284-L285; L295 (missing evidence d); L297; L410 (8B row 5); L430-L431 (Q1, new Q2); L506-L507 (flags 8, 9); L535; L562 ("[FILED balances; INFERENCE attribution]"); L563; L582; YAML L657-L658 | CLOSED (wording notes S11, S12) |
| M3 | MISSING | FY26 CFO/PAT 1.24x leans on the Rs 118.59 Cr L1132 release | A4 L250-L252, L254, L281, L286, L294, L379, L408 (8B row 3), L501 (flag 3), L531, L587 (forward-map bull fork), YAML L652 | CLOSED (wording notes S7, S8, S10, S13) |
| S1 | STYLE | -659 bps from rounded inputs | A4 L157, L174: -658 bps | Applied |
| S2 | STYLE | Bridge GM 20.9988% | A4 L212: 20.9990% (20.99895% rounds to 20.9990%) | Applied |
| S3 | STYLE | Q1 FY26 GM 31.54% | A4 L190: 31.55% (31.54504%) | Applied |
| S4 | STYLE | Fourth newly live line | A4 L61 and Q13 L442: fair value gain Rs 0.65 Cr (L1123) named | Applied |
| S5 | STYLE | Interest-adjusted CFO/PAT second view | A4 L253, L294, L379. Applied as I wrote it, but my S5 note was incomplete. See new finding M4. | Applied; defect in the note, see M4 |
| S6 | STYLE | A2 analyst-note miscount (6 vs 4) | Not an A4 item; A4 makes no change (A4 L686). Correct. | No action needed |

---

## AUDIT 0 - DELIVERABLE-COMPLETENESS (hard gate, re-run)

DELIVERABLE-COMPLETENESS AUDIT: narrative PRESENT | sector PRESENT | business-model PRESENT | competition PRESENT | forward map PRESENT. Gate PASS.

| Brief part | Location | Content check | Status |
|---|---|---|---|
| (1) Summary narrative | A4 L522-L538 | 16 lines (L523-L538, within 10-20); numbers, cause, traded-goods qualifier, CFO both bases, pool, decision line | present |
| (2) Sector intelligence | A4 L540-L548 | demand (INFERENCE), corrected seasonality (FILED comparison plus FILED absence), price-taker spread, bull/bear, separating observation | present |
| (3) Business-model intelligence | A4 L550-L566 | value chain (Note 4), two plants (L85, L90), trading drift with bull/bear and Q4, treasury drift with attribution re-tagged INFERENCE, loan origination, bull/bear, Q1/Q2 | present |
| (4) Competition intelligence | A4 L568-L576 | peers INFERENCE with no figures, win/weak points, bull/bear, separating observation | present (unchanged) |
| (5) Forward map | A4 L578-L589 | make-or-break line plus 10 catalysts; each carries a Bull and a Bear fork; L587 fork restated on both CFO bases | present |

---

## AUDIT 1 - COVERAGE (confirmatory re-run; A1 and A2 unchanged in this loop)

Loop 1 revised only the A4 review. I re-ran grep counts on the three inputs to confirm that nothing under A4 moved.

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Statement lines (P&L, BS, CF) | 96 | 96: grep `^[image transcription, page 7-10]` returns 101 lines = 96 statement lines + 4 section headers (L1056, L1083, L1119, L1148) + 1 notes line (L1156) | none | PASS |
| Structured row IDs | 449 | 449 (grep of row-ID lines in the structured file) | none | PASS |
| Ledger IDs referenced | 449 | 449; ledger L3 and L528-L530 "orphan_ids: []"; gate_a2 pass (L15, L532) | none | PASS |
| Notes rows / distinct notes | 15 / 7 | unchanged from prior audit (A4 L15-L17 still lists all 15 IDs) | none | PASS |
| Zero-standing cells; auditor rows R399-R449 | 27; 51 | ledger L9, L12 unchanged | none | PASS |
| Turns / questions / slides | 0 | 0 (results-only filing) | none | PASS |

Row-level coverage in A4: the blanket "all 449 reviewed" stands (A4 L16-L18). The six material rows my prior audit found uncited are now cited: R260/R261 (A4 L273), R330 (L250), R350 and R356 (L284), R354 (L272, L284). R311 is cited by line (L1123) at A4 L442. The structured cells match the fulltext: R260 32,609.37 and R261 30,694.99 (L1098); R330 11,858.60 (L1132); R350 11,030.49 (L1142); R354 (29,649.96) (L1144); R356 (14,868.43) (L1145).
Missing from ledger: none. Orphan rows: none.

---

## AUDIT 2 - ARITHMETIC (new and changed figures, recomputed from L1057-L1155)

Unchanged Step 1-4 arithmetic passed in the prior audit and was not re-run.

| Metric | A4 value (A4 line) | Recomputed (lakhs) | Source line | Status |
|---|---|---|---|---|
| Traded purchases YoY rise | Rs 93.76 Cr (L155, L170) | 9,886.58 - 510.26 = 9,376.32 | L1061 | PASS |
| Traded rise / revenue rise | 70.4% (L155, L170, L524, L556) | 9,376.32 / 13,314.13 = 70.424% | L1057, L1061 | PASS |
| Revenue less traded purchases, 6 cols | 1,007.65 / 1,136.88 / 1,047.03 / 2,118.02 / 2,183.91 / 4,379.14 Cr (L141) | 1,00,764.76 / 1,13,688.24 / 1,04,702.57 / 2,11,802.03 / 2,18,390.81 / 4,37,914.37 | L1057, L1061 | PASS |
| Proxy YoY / QoQ | +3.9% / -7.9% (L155, L170, L201, L525) | +3.908% / -7.904% | derived | PASS |
| Q2 FY26 vs derived Q1 FY26 | -10.2% (L170) | 1,01,275.02 / 1,12,777.84 - 1 = -10.200% | L1057 (H1 FY26 - Q2 FY26) | PASS |
| H1 FY27 revenue YoY; TTM vs FY26 | +7.06%; +3.42% (L170) | 15,103.00 / 2,14,052.86 = 7.056%; 15,103.00 / 4,41,892.19 = 3.418% | L1057 | PASS |
| Q1 FY26 gross margin | 31.55% (L190) | 1 - 77,202.02 / 1,12,777.84 = 31.545% | derived | PASS |
| Bridge current GM | 20.9990% (L212) | 24,062.52 / 1,14,589.15 = 20.99895% | derived | PASS |
| QoQ Op EBITDA margin | -658 bps (L157, L174) | 16.1559% - 9.5728% = -658.3 bps | derived | PASS |
| OCFA change | +19.14 Cr (L273) | 32,609.37 - 30,694.99 = 1,914.38 | L1098 | PASS |
| Accrued-interest tie | 608.01 + 1,306.38 = 1,914.39 vs 1,914.38 (L285) | 3,530.19 - 2,922.18 = 608.01; + 1,306.38 = 1,914.39 | L1122, L1146, L1132, L1098 | PASS (wording S11) |
| Loans + OCFA pool, 30-Sep | Rs 591.88 Cr; 17.0% of equity (L274, L281) | 26,578.46 + 32,609.37 = 59,187.83; / 3,48,654.13 = 16.976% | L1097, L1098, L1105 | PASS. My prior audit's 591.87 summed rounded crore values; A4's lakh-basis 591.88 is correct. |
| Pool, 31-Mar; change | Rs 603.45 Cr; 18.2%; -11.57 Cr (L274) | 29,649.96 + 30,694.99 = 60,344.95; / 3,31,623.48 = 18.197%; -1,157.12 | L1097, L1098, L1105 | PASS |
| Loan origination tie | 29,649.96 - 3,071.49 = 26,578.47 vs 26,578.46 (L284) | same | L1097, L1144 | PASS |
| FY26 borrowing / PPE sale / deposits | 170.02 / 110.30 / 148.68 Cr (L284) | 17,002.18 / 11,030.49 / 14,868.43 | L1149, L1142, L1145 | PASS |
| FY26 CFO ex L1132 release | 483.68 Cr (L250) | 60,226.48 - 11,858.60 = 48,367.88 | L1132, L1140 | PASS |
| H1 CFO ex L1132 line | 103.88 Cr (L250) | 9,082.36 + 1,306.38 = 10,388.74 = Rs 103.89 Cr | L1132, L1140 | PASS (0.01 rounding, S7) |
| CFO/PAT FY26 reported / ex release | 1.24x / 1.00x (L251-L252) | 60,226.48 / 48,426.70 = 1.2437; 48,367.88 / 48,426.70 = 0.9988 | L1140, L1076 | PASS |
| CFO/PAT H1 ex release; change | 0.56x; -0.44x (L252) | 10,388.74 / 18,417.78 = 0.5641; 0.5641 - 0.9988 = -0.4347 | L1140, L1132, L1076 | PASS (change -0.43x unrounded, S7) |
| CFO/Op EBITDA FY26 ex release | 67.5% (L254) | 48,367.88 / 71,644.38 = 67.511% | derived | PASS |
| CFO/PAT with interest received added | 0.65x / 1.33x; change -0.68x (L253) | (9,082.36 + 2,922.18) / 18,417.78 = 0.6518; (60,226.48 + 4,254.13) / 48,426.70 = 1.3315 | L1140, L1146, L1076 | PASS as labelled. View incomplete: see M4 |
| CFO/PAT, net-interest view (not in A4) | absent | H1: (9,082.36 + 2,922.18 - 1,711.35) / 18,417.78 = 10,293.19 / 18,417.78 = 0.5589x. FY26: (60,226.48 + 4,254.13 - 3,919.51) / 48,426.70 = 60,561.10 / 48,426.70 = 1.2506x | L1124, L1140, L1146, L1150, L1076 | MISSING (M4) |
| CFO/PAT, strict trade-only (reference) | "trade-only cash" label at L252 | PBWC + inventories + receivables + payables - tax: FY26 47,714.12 / 48,426.70 = 0.985x; H1 9,307.01 / 18,417.78 = 0.505x | L1127-L1129, L1134, L1139 | label imprecise (S8) |
| Borrowing tenor shift | +61.08 / -16.79 Cr (L267-L268, L297) | 6,108.03; -1,679.34 | L1111, L1106 | PASS |
| FY26 dividend outflow | Rs 9.40 Cr (L438, L507) | 940.46 | L1151 | PASS |
| Q13 new-line amounts | 7.58 / 2.80 / 0.36 / 0.65 Cr (L442) | 757.56 / 280.20 / 36.16 / 65.29 | L1112, L1116, L1125, L1123 | PASS |
| Question count | 17 rows; 20 YAML entries (L426) | 17 + 2 (Q10 split to 3) + 1 (Q11 split to 2) = 20; YAML L615-L634 = 20 | A4 L430-L446 | PASS |
| Renumbered cross-references | Q1, Q2, Q3, Q4, Q5, Q6, Q8 (L173, L452-L456, L559, L566) | each points to the matching row | A4 L430-L446 | PASS |

Arithmetic mismatches above rounding: none.

---

## AUDIT 3 - ADVERSARIAL READ (scoped to new and changed text)

The three prior counters are now grafted (M1, M2, M3 above). Loop 1 adds one new positive figure and two bull readings. I tested each against the extract.

### New positive figure - "CFO/PAT with interest received added back: 0.65x H1 FY27, 1.33x FY26, shown for symmetry" (A4 L253, L294, L379)
Bear counter:
- The cash-flow statement moves interest out of CFO on both sides, not one. Interest income is stripped (L1122) and interest received sits in investing (L1146). Interest expense is added back too (L1124: 1,711.35 H1; 3,919.51 FY26; R313, R314), and interest paid sits in financing (L1150: (1,711.35); (3,919.51); R368, R369).
- PAT (L1076) is after both interest income and finance cost. A view that matches PAT adds interest received and deducts interest paid. It gives 0.56x for H1 FY27 (10,293.19 / 18,417.78) and 1.25x for FY26 (60,561.10 / 48,426.70).
- The one-sided H1 figure, 0.65x, sits exactly on the "lowest Pillar 2 band (0.65x)" that A4 cites at L251. Step 7 (L379) flags it as the Pillar 2 second view for Role 1. On a consistent basis H1 is 0.56x, below that band.
- Survives? YES. Tag: MISSING (material qualifier absent from a pillar-input fact). Loop A4.
- Origin: my prior S5 note asked for interest received to be added back and left out interest paid. A4 built the view exactly as I wrote it. The defect is in my note, but the fix goes into A4's text.
- Suggested graft text (A4 L253, as a replacement row or a row beside it): "CFO / PAT, net-interest view (CFO + interest received L1146 - interest paid L1150) | 1.25x | 0.56x | -0.69x | CFO excludes interest income (L1122) and interest expense (L1124). Moving both back puts CFO on the PAT basis. The interest-received-only view (0.65x / 1.33x) is gross of interest paid and is not symmetric." Carry the same correction into A4 L294, L379 and the CF Note 2 cell at L60.

### New bull reading - traded goods bought to serve customers while own output was limited (A4 L171, L557)
Tagged INFERENCE, with the bear reading and the separating observation (own tonnage, Q4) beside it. The proxy caveat at A4 L145 states the assumption. No unanswered counter. No finding.

### New bull reading - treasury book is spare cash parked well, recoverable on demand (A4 L564)
Paired with the bear reading at L565 (lending while borrowing Rs 505.69 Cr short term, L1111) and questions Q1 and Q2. The FY26 origination facts sit in the same section at L563. No unanswered counter. No finding.

### Mandatory acquisition-economics probe
N/A, unchanged from the prior audit. The filing describes no acquisition, business purchase or stake buy. The year-ago associate (L1075) left the perimeter with no consideration disclosed.

---

## FINDINGS BY TYPE (this loop)

| ID | Type | Finding | Lines | Loop |
|---|---|---|---|---|
| M4 | MISSING | The interest add-back second view is one-sided. It adds interest received (L1146) but leaves out interest paid (L1150), which CFO also excludes (L1124 add-back). Net-interest CFO/PAT is 0.56x H1 FY27 and 1.25x FY26, not 0.65x and 1.33x. The one-sided 0.65x sits on the 0.65x Pillar 2 floor that A4 cites (L251) and feeds the Step 7 Pillar 2 row (L379). The defect starts in my prior S5 note. | A4 L60, L253, L294, L379; L1124, L1140, L1146, L1150, L1076 | A4 |
| S7 | STYLE | Rounding: the H1 ex-release CFO is 103.89 Cr on the lakh basis (10,388.74), not 103.88. The ex-release CFO/PAT change is -0.43x unrounded (0.5641 - 0.9988), not -0.44x. | A4 L250, L252 | none |
| S8 | STYLE | "Trade-only cash" (L252) overstates the ex-L1132 basis. It still includes other current assets (L1133), other current liabilities (L1136) and provisions (L1137). On a strict trade-only basis CFO/PAT is 0.99x FY26 and 0.51x H1. Say "ex the L1132 line". Also, H1 ex-release CFO/Op EBITDA (35.2%) is not shown, but FY26 (67.5%) is (L254). | A4 L252, L254 | none |
| S9 | STYLE (borderline) | Causal wording tagged FILED. L524 says "Most of that rise came from goods bought for resale"; L463 says "70% of revenue rise from traded goods"; L231 says "Traded purchases made up 70.4% of that rise". The filing shows only that traded-purchase cost rose by an amount equal to 70.4% of the revenue rise. Traded-goods revenue is not filed, and the stock-in-trade part of L1062 is not split (A4's own caveat, L145). Use "matched", as at L397 and L556. Logged as STYLE: the number, the bear reading and the verdict do not change, and L525 carries the INFERENCE tag. | A4 L231, L463, L524 | none |
| S10 | STYLE | "One-time release" (L531, tagged FILED). The filing does not say the FY26 L1132 inflow is one-time. Use "a non-trade release", the Step 5 wording at L286. | A4 L531 | none |
| S11 | STYLE | "Accrued interest explains it by tie" (L285). Accrued interest explains 608.01 of the 1,914.38 rise (31.8%). The other 1,306.38 is the L1132 operating increase, nature undisclosed. Suggested: "Accrued interest of 608.01 plus the L1132 increase of 1,306.38 ties to the rise." | A4 L285 | none |
| S12 | STYLE | "Sold plant for Rs 110.30 Cr" (L563). L1142 records the sale of property, plant and equipment. L552 mentions two plants, so "plant" reads as a whole plant. Use "sold fixed assets". | A4 L563 | none |
| S13 | STYLE | The 8B row 3 bases do not match. The green bar is on the ex-release basis (1.00x), while the red bar and the reading are on the reported basis (0.49x). Give one basis per row, or both thresholds on each basis. | A4 L408 | none |

---

## VERDICT

VERDICT: INCOMPLETE. Loop back to A4. Finding types this loop: 0 FACTUAL, 1 MISSING, 0 CONTRADICTION, 7 STYLE.
Prior items: F1, M1, M2 and M3 are closed. S1-S5 are applied. S6 needs no A4 action.
Gap (M4, MISSING): the interest add-back second view must also deduct interest paid (L1150), because CFO also excludes interest expense (L1124). Show the net-interest CFO/PAT: 0.56x H1 FY27, 1.25x FY26. State that the 0.65x / 1.33x interest-received-only figures are gross of interest paid, and that H1 does not reach the 0.65x Pillar 2 floor on a consistent basis. Apply at A4 L253 (Step 5 row), L294 (mandatory answer), L379 (Step 7 Pillar 2 row) and L60 (CF Note 2 cell).
No arithmetic mismatch above rounding. No coverage orphan. No missing ledger row. The A4 protocol verdict (PROCEED WITH FLAGS) and the INDETERMINATE-WITH-DIRECTION cash class are not challenged. The fix moves no headline number (reported CFO/PAT stays 0.49x).

## STYLE NOTES (logged, no re-run)
S7-S13 as tabled above. A4 may apply them in the same pass as M4 at no extra loop cost.

```yaml
stage: A5-adversary
company: "GALLANTT"
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
  - {claim: "CFO/PAT with interest received added back: 0.65x H1 FY27, 1.33x FY26, 'shown for symmetry' (A4 L253, L294, L379)", counter: "CFO also excludes interest expense (L1124 add-back; paid in financing L1150). A PAT-consistent view adds interest received and deducts interest paid: H1 10,293.19/18,417.78 = 0.56x; FY26 60,561.10/48,426.70 = 1.25x. The one-sided 0.65x sits on the 0.65x Pillar 2 floor A4 cites (L251); the consistent 0.56x sits below it.", source_line: "L1076, L1124, L1140, L1146, L1150 (R191, R313, R314, R345, R346, R357, R358, R368, R369)", type: MISSING}
findings_by_type:
  factual: []
  missing:
    - "M4 (A4): The interest add-back second view (A4 L253, L294, L379; L60) adds interest received (L1146) but not interest paid (L1150), though CFO excludes both (L1122, L1124). Net-interest CFO/PAT = 0.56x H1 FY27, 1.25x FY26 (vs 0.65x / 1.33x shown). The one-sided H1 0.65x sits on the Pillar 2 floor A4 cites (L251) and feeds the Step 7 Pillar 2 row. Defect originates in prior A5 note S5."
  contradiction: []
  style:
    - "S7: H1 ex-release CFO 103.89 Cr on lakh basis (A4 L250 shows 103.88); ex-release CFO/PAT change -0.43x unrounded (A4 L252 shows -0.44x)."
    - "S8: 'trade-only cash' (A4 L252) overstates the ex-L1132 basis; strict trade-only CFO/PAT 0.99x FY26, 0.51x H1. H1 ex-release CFO/Op EBITDA (35.2%) not shown beside FY26 67.5% (A4 L254)."
    - "S9 (borderline): A4 L524 'came from goods bought for resale', L463 'from traded goods', L231 'made up' state traded-goods revenue as filed; filing shows only traded-purchase cost rise = 70.4% of revenue rise. Use 'matched' (as A4 L397, L556)."
    - "S10: A4 L531 'one-time release' tagged FILED; filing does not say one-time; use 'non-trade release' (A4 L286)."
    - "S11: A4 L285 'Accrued interest explains it': accrued interest is 608.01 of the 1,914.38 rise; rest is the L1132 increase of 1,306.38."
    - "S12: A4 L563 'sold plant for Rs 110.30 Cr': L1142 is sale of PPE; use 'sold fixed assets'."
    - "S13: A4 L408 8B row 3 mixes bases: green 1.00x ex-release, red and reading 0.49x reported."
loop_back_to: "A4"
gap: "M4 (MISSING): add interest paid (L1150) to the interest add-back second view at A4 L253, L294, L379 and L60. Net-interest CFO/PAT = 0.56x H1 FY27 (10,293.19/18,417.78), 1.25x FY26 (60,561.10/48,426.70). State that 0.65x/1.33x are gross of interest paid and that H1 does not reach the 0.65x Pillar 2 floor on a consistent basis. Prior F1, M1, M2, M3 closed."
style_notes:
  - "S7: 103.89 not 103.88 (A4 L250); -0.43x not -0.44x (A4 L252)."
  - "S8: replace 'trade-only' with 'ex the L1132 line' (A4 L252); strict trade-only 0.99x FY26, 0.51x H1; add H1 ex-release CFO/Op EBITDA 35.2% (A4 L254)."
  - "S9: 'came from' / 'from' / 'made up' to 'matched' (A4 L231, L463, L524)."
  - "S10: 'one-time release' to 'non-trade release' (A4 L531)."
  - "S11: reword accrued-interest sentence (A4 L285)."
  - "S12: 'sold plant' to 'sold fixed assets' (A4 L563)."
  - "S13: one basis per 8B row 3 threshold (A4 L408)."
analyst_note: "Loop 1 closes F1, M1, M2 and M3. I checked each fix at the cited A4 lines. A1 and A2 are unchanged: 96 statement lines, 449 structured IDs, no ledger orphans. Every new figure recomputes from L1057-L1155: the 70.4% traded share, the Rs 591.88 Cr pool (lakh basis; my prior 591.87 summed rounded crore values), 17.0% and 18.2% of equity, 1.00x and 0.56x ex release, and 0.65x and 1.33x with interest received. The one new gap is mine. My prior S5 note asked for interest received to be added back but left out interest paid, which CFO also excludes (L1124 add-back, L1150 financing). A4 built the view as I wrote it. The consistent view is 0.56x H1 and 1.25x FY26. The one-sided 0.65x sits on the Pillar 2 floor that A4 cites and goes to Role 1, so I tag it MISSING, not STYLE. The fix is four cells. S9 is a borderline STYLE call: 'came from' should read 'matched'. PROCEED WITH FLAGS stands."
```
