# A5 ADVERSARY / COMPLETENESS AUDIT, LOOP 2 FINAL RE-AUDIT - Gallantt Ispat Limited (GALLANTT) - Q2 FY27

Auditor: A5 (claude-opus-5-5), fresh context. Date: 2026-10-20.
Scope (orchestrator, loop 2, closure only): (1) confirm M4 is closed everywhere it appeared; (2) re-run the deliverable-completeness gate; (3) check only loop-2 changed text for new FACTUAL / MISSING / CONTRADICTION errors and arithmetic. No new adversarial pass on unchanged text.
Inputs read: A4 review `runs/gallantt-q2fy27/work/review_gallantt_q2fy27.md` (702 lines, loop 2 revision, change log at A4 L688-L701); A1 fulltext `runs/gallantt-q2fy27/extracted/gallantt-results-q2fy27-fulltext.md` (statement block L1056-L1157); A1 structured `runs/gallantt-q2fy27/extracted/gallantt-results-q2fy27-structured.md` (row IDs and interest/CFO cells); A2 ledger `runs/gallantt-q2fy27/work/ledger_results_gallantt_q2fy27.md` (gate lines); my loop-1 audit `runs/gallantt-q2fy27/work/audit_gallantt_q2fy27_loop1.md`.
Not read: the source PDF, anything under `inputs/`, A3 forensics.
Line references: "L" = fulltext line; "A4 L" = review line; "R" = structured row ID. Units Rs lakhs unless marked Rs Cr (lakhs x 0.01).

---

## PRIOR-ITEM CLOSURE (loop-1 findings)

| ID | Type | Gap (loop 1) | Where A4 fixed it (verified against the text) | Status |
|---|---|---|---|---|
| M4 | MISSING | Interest add-back view was one-sided (interest received L1146 added, interest paid L1150 not deducted) | A4 L60 (CF Note 2 cell): CFO excludes interest income L1122 and interest expense L1124; received in investing L1146, paid in financing L1150; points to the Step 5 net-interest view. A4 L253 (Step 5 row): net-interest view 1.25x FY26 / 0.56x H1 / -0.69x; 0.65x / 1.33x named as gross of interest paid and not symmetric. A4 L281 (computation notes): H1 10,293.19 / 18,417.78 = 0.56x; FY26 60,561.10 / 48,426.70 = 1.25x. A4 L294 (mandatory answer): 0.56x / 1.25x; "H1 does not reach the 0.65x floor on any consistent basis"; received-only view "not used". A4 L379 (Step 7 Pillar 2 row): 0.56x net-interest H1, 1.25x FY26; below floor on every consistent basis. A4 L652 (YAML flag 3) and L667 (analyst_note) carry the same figures. Grep for "0.65x", "1.33x", "symmetr", "interest received added" finds no residual one-sided figure presented as a live view: L251 is the band, L253 and L294 label the received-only numbers as gross and unused, L685 is the loop-1 change log marked "Superseded in loop 2 (M4)". | CLOSED |
| S7 | STYLE | 103.88 vs 103.89; -0.44x vs -0.43x | A4 L250: 103.89 (10,388.74 lakhs). A4 L252 and L281: -0.43x | Applied |
| S8 | STYLE | "Trade-only" label; H1 CFO/Op EBITDA ex L1132 absent | A4 L252: "ex the L1132 line"; strict trade-only 0.99x FY26, 0.51x H1 with lines L1127-L1129, L1134, L1139. A4 L254: 35.2% H1 ex L1132 | Applied |
| S9 | STYLE | Causal "came from / made up" | A4 L155, L231, L432, L463, L524, L556 now read "matched". Residual "came from" at A4 L445 and L633 concerns top-10 customers, not traded goods | Applied |
| S10 | STYLE | "One-time release" | A4 L531: "non-trade release" | Applied |
| S11 | STYLE | Accrued-interest sentence | A4 L285: accrued interest 608.01 plus the L1132 increase 1,306.38 ties to 1,914.39 | Applied |
| S12 | STYLE | "Sold plant" | A4 L563: "sold fixed assets". A4 L284, L430 and L506 say "PPE", the filed term (L1142). | Applied |
| S13 | STYLE | 8B row 3 mixed bases | A4 L408: green, red and reading each on both bases (reported 1.24x / 0.49x; ex L1132 1.00x / 0.56x) | Applied |

Prior loops: F1, M1, M2, M3 closed at loop 1. A4 states they are unchanged in loop 2 (A4 L701). Spot checks show the loop-1 fix text still in place at A4 L155, L170-L173, L200, L272-L274, L284-L286.

---

## AUDIT 0 - DELIVERABLE-COMPLETENESS (hard gate, re-run)

DELIVERABLE-COMPLETENESS AUDIT: narrative PRESENT | sector PRESENT | business-model PRESENT | competition PRESENT | forward map PRESENT. Gate PASS.

| Brief part | Location | Content check | Status |
|---|---|---|---|
| (1) Summary narrative | A4 L522-L538 | 16 lines (L523-L538, within 10-20); revenue, traded-goods "matched" qualifier, profit, cause, tax, CFO on both FY26 bases with "non-trade release" (L531), inventory, CWIP, liquidity, Rs 591.88 Cr pool, auditor, decision line | present |
| (2) Sector intelligence | A4 L540-L548 | demand (INFERENCE), FILED Q2-vs-Q1 comparison with FILED absence, price-taker spread, bull/bear, separating observation | present |
| (3) Business-model intelligence | A4 L550-L566 | value chain, two plants, trading drift ("matched", L556) with bull/bear and Q4, treasury drift with INFERENCE attribution, FY26 loan origination ("sold fixed assets", L563), bull/bear, Q1/Q2 | present |
| (4) Competition intelligence | A4 L568-L576 | peers tagged INFERENCE with no figures, win and weak points, bull/bear, separating observation | present |
| (5) Forward map | A4 L578-L589 | make-or-break line plus 10 dated or dated-ND catalysts (L580-L589); each carries a Bull and a Bear fork | present |

---

## AUDIT 1 - COVERAGE (confirmatory; A1 and A2 unchanged in loop 2)

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Statement lines (P&L, BS, CF) | 96 | 96: grep `^[image transcription, page 7-10]` returns 101 = 96 statement lines + 4 section headers (L1056, L1083, L1119, L1148) + 1 notes line (L1156) | none | PASS |
| Structured row IDs | 449 | 449 (grep of row-ID lines in the structured file) | none | PASS |
| Ledger IDs referenced | 449 | ledger L3 "ids_referenced_in_ledger: 449 / orphan_ids: [] / match: yes"; L530 orphan_ids []; gate_a2 pass (L15, L532) | none | PASS |
| Notes rows / distinct notes | 15 / 7 | unchanged; A4 L15-L17 lists all 15 IDs | none | PASS |
| Turns / questions / slides | 0 | 0 (results-only filing) | none | PASS |

Loop-2 cells cross-checked structured vs fulltext: R313/R314 1,711.35 / 3,919.51 (L1124); R329/R330 (1,306.38) / 11,858.60 (L1132); R345/R346 9,082.36 / 60,226.48 (L1140); R357/R358 2,922.18 / 4,254.13 (L1146); R368/R369 (1,711.35) / (3,919.51) (L1150). All match.
Row-level coverage in A4: the blanket "all 449 reviewed" stands (A4 L16-L18). Loop 2 removed no row citation.
Missing from ledger: none. Orphan rows: none.

---

## AUDIT 2 - ARITHMETIC (loop-2 changed figures, recomputed from L1057-L1155)

Unchanged Step 1-4 arithmetic and loop-1 figures passed in earlier audits and were not re-run.

| Metric | A4 value (A4 line) | Recomputed (lakhs) | Source line | Status |
|---|---|---|---|---|
| Net-interest CFO, H1 FY27 | 10,293.19 (L281) | 9,082.36 + 2,922.18 - 1,711.35 = 10,293.19 | L1140, L1146, L1150 | PASS |
| Net-interest CFO/PAT, H1 FY27 | 0.56x (L253, L281, L294, L379, L652, L667) | 10,293.19 / 18,417.78 = 0.5589 | L1076 | PASS |
| Net-interest CFO, FY26 | 60,561.10 (L281) | 60,226.48 + 4,254.13 - 3,919.51 = 60,561.10 | L1140, L1146, L1150 | PASS |
| Net-interest CFO/PAT, FY26 | 1.25x (L253, L281, L294, L379, L652, L667) | 60,561.10 / 48,426.70 = 1.2506 | L1076 | PASS |
| Net-interest change | -0.69x (L253, L692) | 0.5589 - 1.2506 = -0.6917 | derived | PASS |
| Interest-received-only (now labelled gross, unused) | 0.65x H1; 1.33x FY26 (L253, L294) | 12,004.54 / 18,417.78 = 0.6518; 64,480.61 / 48,426.70 = 1.3315 | L1140, L1146, L1076 | PASS |
| "Below 0.65x on every consistent basis" (L294, L379) | claim | reported 0.4931; ex L1132 0.5641; net-interest 0.5589; strict trade-only 0.5053; net-interest and ex L1132 combined (10,293.19 + 1,306.38) / 18,417.78 = 11,599.57 / 18,417.78 = 0.6298. All below 0.65 | L1076, L1132, L1140, L1146, L1150 | PASS |
| H1 CFO ex L1132 | Rs 103.89 Cr; 10,388.74 (L250, L281) | 9,082.36 + 1,306.38 = 10,388.74 | L1132, L1140 | PASS |
| CFO/PAT ex L1132 change | -0.43x (L252, L281) | 0.5641 - 0.9988 = -0.4347 | L1076, L1132, L1140 | PASS |
| Strict trade-only CFO/PAT | 0.99x FY26; 0.51x H1 (L252) | FY26 72,519.72 - 11,448.93 - 8,740.46 + 8,035.34 - 12,651.55 = 47,714.12; / 48,426.70 = 0.9853. H1 29,512.93 - 11,788.93 - 805.65 + 318.33 - 7,929.67 = 9,307.01; / 18,417.78 = 0.5053 | L1127-L1129, L1134, L1139, L1076 | PASS |
| CFO / Op EBITDA | 84.1% / 67.5% FY26; 30.8% / 35.2% H1; -53.3 pp (L254) | 60,226.48 / 71,644.38 = 84.06%; 48,367.88 / 71,644.38 = 67.51%; 9,082.36 / 29,478.68 = 30.81%; 10,388.74 / 29,478.68 = 35.24%; 30.81 - 84.06 = -53.25 pp | L1140, L1132; Op EBITDA from L1058, L1064, L1065, L1070 | PASS |
| Op EBITDA bases | 29,478.68 H1; 71,644.38 FY26 (L281) | 24,798.81 + 6,562.09 + 1,764.01 - 3,646.23 = 29,478.68; 60,403.48 + 13,031.72 + 4,168.59 - 5,959.41 = 71,644.38 | L1058, L1064, L1065, L1070 | PASS |
| Accrued-interest tie | 608.01 + 1,306.38 = 1,914.39 vs 1,914.38 (L285) | 3,530.19 - 2,922.18 = 608.01; + 1,306.38 = 1,914.39; 32,609.37 - 30,694.99 = 1,914.38 | L1098, L1122, L1132, L1146 | PASS (0.01 rounding) |
| 8B row 3 thresholds | 1.24x / 0.49x; 1.00x / 0.56x (L408) | 60,226.48 / 48,426.70 = 1.2437; 9,082.36 / 18,417.78 = 0.4931; 0.9988; 0.5641 | L1076, L1132, L1140 | PASS |

Arithmetic mismatches above rounding: none.

---

## AUDIT 3 - ADVERSARIAL READ (scoped to loop-2 changed text)

No new adversarial pass on unchanged text, per the loop-2 scope. Loop 2 adds one figure that reads positive: FY26 net-interest CFO/PAT 1.25x.
- Bear counter tested: the 1.25x still contains the Rs 118.59 Cr L1132 release. Net of both adjustments, FY26 is (60,561.10 - 11,858.60) / 48,426.70 = 48,702.50 / 48,426.70 = 1.01x.
- Survives? NO. The same table puts the 1.00x ex-L1132 row beside it (A4 L252). The Pillar 2 row names the release (A4 L379). The combined 1.01x differs from the shown 1.00x by 0.01x and does not change any reading. No finding.
- The H1 side of the loop-2 text is bearish (0.56x). Its "every consistent basis" claim survives my combined-basis test (0.63x, still below 0.65x).
Mandatory acquisition-economics probe: N/A. The filing describes no acquisition, business purchase or stake buy. The year-ago associate (L1075) left the perimeter with no consideration disclosed.

---

## FINDINGS BY TYPE (this loop)

| ID | Type | Finding | Lines | Loop |
|---|---|---|---|---|
| S14 | STYLE | Flag 3 in the verdict list (A4 L501) gives H1 0.49x and FY26 1.24x / 1.00x. The loop-2 YAML flag 3 (A4 L652) adds the net-interest readings (0.56x H1, 1.25x FY26). The two do not disagree, but they now carry different detail. Harmonise L501 to L652 if convenient. | A4 L501, L652 | none |

FACTUAL: none. MISSING: none. CONTRADICTION: none.

---

## VERDICT

VERDICT: COMPLETE. Finding types this loop: 0 FACTUAL, 0 MISSING, 0 CONTRADICTION, 1 STYLE.
M4 is closed at every place it appeared (A4 L60, L253, L281, L294, L379; also YAML flag 3 L652 and analyst_note L667). S7-S13 are applied. The deliverable gate passes with all five brief parts present. Coverage holds: 96 statement lines, 449 structured IDs, no ledger orphans, no row missing from the ledger. Every loop-2 figure recomputes from the fulltext with no mismatch above rounding. The A4 protocol verdict (PROCEED WITH FLAGS) and the INDETERMINATE-WITH-DIRECTION cash class are not challenged. The review may proceed to the Notion save gate.

## STYLE NOTES (logged, no re-run)
- S14: align the verdict-list flag 3 (A4 L501) with the YAML flag 3 (A4 L652) on the net-interest readings. Optional; no loop.

```yaml
stage: A5-adversary
company: "GALLANTT"
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
    - "S14: verdict-list flag 3 (A4 L501) omits the net-interest readings (0.56x H1, 1.25x FY26) that the loop-2 YAML flag 3 (A4 L652) carries; no disagreement, detail differs."
loop_back_to: ""
gap: ""
style_notes:
  - "S14: harmonise A4 L501 flag 3 with A4 L652 flag 3 (net-interest readings). Optional, no re-run."
analyst_note: "Loop 2 closure audit. M4 is closed at A4 L60, L253, L281, L294 and L379, and in YAML flag 3 and the analyst_note. The net-interest view recomputes from L1140, L1146, L1150 and L1076: H1 10,293.19 / 18,417.78 = 0.56x, FY26 60,561.10 / 48,426.70 = 1.25x, change -0.69x. The received-only 0.65x and 1.33x remain only as labelled gross figures marked not used. I tested A4's claim that H1 sits below the 0.65x floor on every consistent basis against the strongest combination, net-interest plus ex-L1132. It gives 0.63x, so the claim holds. The FY26 1.25x still contains the L1132 release. Net of both adjustments FY26 is 1.01x. That is 0.01x from the 1.00x row shown beside it, so no counter survives. S7-S13 are applied with correct arithmetic. A1 and A2 are unchanged: 101 page 7-10 lines (96 statement), 449 IDs, no orphans. One STYLE note only. PROCEED WITH FLAGS stands."
```
