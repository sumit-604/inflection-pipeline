# A5 AUDIT: CYBERTECH Q2 FY27 (results, Reg 33 board outcome 22-Oct-2026)

ITERATION 1 (loop 1 re-audit). The loop 0 audit is preserved at runs/cybertech-q2fy27/work/audit_cybertech_q2fy27_loop0.md.

Stage: A5 adversary / completeness auditor. Model: claude-opus-5-5.
Inputs read: the revised A4 review (runs/cybertech-q2fy27/work/review_cybertech_q2fy27.md, 711 lines, YAML loop: 1); A1 fulltext (extracted/cybertech-results-q2fy27-fulltext.md, L1-L443); A1 structured (extracted/cybertech-results-q2fy27-structured.md, R001-R739); A2 ledger (work/ledger_results_cybertech_q2fy27.md). No source PDF and nothing under inputs/ was opened. A3 reasoning was not read.

Anchor convention: (Lnnn) = A1 fulltext line; (Rnnn) = A1 structured row; (A4 Lnnn) = line in the revised A4 review; "c:" = A5 arithmetic on anchored filed figures. All arithmetic is in Rs lakh as filed unless a cell says Cr. "Perimeter" = consolidated less standalone.

VERDICT: COMPLETE. All six loop 0 findings (F1, F2, F3, C1, M1, M2) are closed. The rewrite introduced no new FACTUAL, MISSING or CONTRADICTION finding. Five STYLE notes are logged (two carried from loop 0, three new). Proceeds to Notion save.

---

## LOOP 0 FINDING CLOSURE

| ID | Type | Status | Evidence in the revised review | A5 check |
|---|---|---|---|---|
| F1 | FACTUAL | CLOSED | A4 L204 (transfer-pricing scope stated), L248 ("transfer pricing cannot explain it"), L505 (8C: Q3 core PBT "cannot test transfer pricing"), L524 (QfM 1 "Why it matters" re-scoped), L546, L583 (brief), L631 (forward map), L663, L695, L707 (analyst note). | No remaining text says transfer pricing can explain the group gain, or that consolidated core PBT separates TP from real leverage. A4 L18 adds a tax-split caveat: perimeter ETR 25.24% vs parent 24.59%. Recomputed: (286.70 - 176.19) / (1,154.43 - 716.63) = 110.51 / 437.80 = 25.24% (L110-L114, L296-L299); parent 176.19 / 716.63 = 24.59%. Correct. |
| F2 | FACTUAL | CLOSED | A4 L87-L88 (Note 5 rows), L594-L595 (sector bullet split into FILED and INFERENCE), L535 (QfM 12), L563 (monitorable 6), L629 (forward map), L698 (flag). | Wording now matches L434-L435: no amount, no direction, no wage-base claim, no "expects a further charge". The "cost item for every Indian IT employer" line is labelled INFERENCE. |
| F3 | FACTUAL | CLOSED | A4 L334 and L347 (matched bases with formulas), L373 (5C facts for /fttcp), L378 (class), L433 (6B), L475 (Step 7 Cash Multiplier), L585 (brief), L630 and L684 (H2 bear fork), L696 (flag), L707. | 1.20x / 1.23x (H1 FY27) and 1.05x / 1.15x (H1 FY26) recompute (Audit 2). The unmatched 0.84x is kept only as an explained, rejected ratio (A4 L334). The class stays INDETERMINATE-WITH-DIRECTION on H2 reversal risk. |
| C1 | CONTRADICTION | CLOSED | A4 L567 (monitorable 10), L632 to L634 (forward map), L689 (YAML). | The bull fork (revenue at or above 73.30 Cr) and bear fork (back toward 58-60 Cr) no longer overlap. The bull fork is consistent with the Step 3 bar (A4 L275). The quarter is relabelled "fifth"; the residual "fourth" grep hits are none. |
| M1 | MISSING | CLOSED | A4 L247 (2C item 3 graft), L272 (Step 3), L288 (4A recurring column), L317, L458 (6.5A), L582 (brief), L694 (flag), L707. | Numbers recompute: Op EBITDA +236.98 QoQ = perimeter +266.59, parent -29.61; parent core PBT -6.9%; perimeter margin 2.4% / 2.5%; FCTR -24.96 to +217.88 (L121); H1 OI / PBT 53.47%; separator 11.04% / 8.36%. |
| M2 | MISSING | CLOSED | A4 L73-L77 (Step 0C buyback economics), L224 (2A EPS verdict), L538 (QfM 15), L697 (flag). | 18.0x (176.24 / 9.77, L127); Rs 54.48 cash a share (16,959.49 lakh / 3,11,30,600); 30.9%; ex-cash about 35x on core EPS Rs 3.49; about 18x on Q2 run-rate Rs 6.74. All match. A4 adds "arithmetic only, not an A21 base" (A4 L76). |

Loop 0 STYLE notes: S3 to S11 were applied (A4 L25 and the cited lines; checked). S2 is closed by the row-range "reviewed, no finding" marker at A4 L32. S1 and S12 concern A1/A2 capture and carry forward as logged notes.

---

## AUDIT 0. DELIVERABLE-COMPLETENESS (hard gate)

DELIVERABLE-COMPLETENESS AUDIT: narrative PRESENT | sector PRESENT | business_model PRESENT | competition PRESENT | forward_map PRESENT. Gate PASS.

| Part | A4 location | Content check | Status |
|---|---|---|---|
| 1. Summary narrative | A4 L574-L589 | 14 lines, inside the 10-20 line band. | PRESENT |
| 2. Sector intelligence | A4 L591-L599 | 7 bullets; FILED, INFERENCE and SECONDARY labelled. | PRESENT |
| 3. Business-model intelligence | A4 L601-L608 | 6 bullets. | PRESENT |
| 4. Competition intelligence | A4 L610-L616 | 5 bullets; peers labelled SECONDARY, PENDING LIVE VERIFICATION. | PRESENT |
| 5. Forward map | A4 L618-L634 | Make-or-break line plus 9 catalysts, each with separable bull and bear forks. | PRESENT |

---

## AUDIT 1. COVERAGE

The A1 fulltext, A1 structured file and A2 ledger are unchanged since loop 0, so the fresh enumeration stands.

| Category | A2 count | A5 fresh count | Orphan rows | Status |
|---|---|---|---|---|
| notes | 7 | 7 (L430-L436) | none | PASS |
| line_items | 191 | 191 | none | PASS |
| table NUMBER cells R001-R551 | 551 | 551 | none | PASS |
| zero_standing | 45 / 27 items | 45 / 27 | none | PASS |
| embedded_numbers | 42 | 60 (18 uncaptured boilerplate) | none | PASS; STYLE L1-S1 |
| agenda_items | 1 | 1 (L37) | none | PASS |
| auditor_paras | 7 | 7 by paragraph | none | PASS |
| entities | 46 | 55 (9 uncaptured boilerplate) | none | PASS; STYLE L1-S1 |
| forward | 3 | 3 (L434 x2, L435) | none | PASS |
| dates | 51 | 52 (L33 repeat) | none | PASS; STYLE L1-S1 |
| qualifiers | 46 | 51 (5 formula captions) | none | PASS; STYLE L1-S1 |
| signature_blocks | 10 | 10 | none | PASS |
| turns / questions / slides | 0 | 0 | n/a | PASS |

Ledger rows vs A4: A4 L32 now marks the uncited balance-sheet rows by range "reviewed, no finding": consolidated R138-R139, R146-R147, R150-R153, R156-R157, R162-R171, R182-R183, R186-R187, R202-R209; standalone R409-R416, R419-R426, R429-R446, R449-R480. It marks the identifier rows R552-R693 the same way. A4 L338, L362 and L364 now anchor L155, L336, L337, L338, L339 and L359. All A2 flags remain addressed. Orphan rows: none. missing_from_ledger: none (boilerplate units are STYLE).

Coverage verdict: PASS.

---

## AUDIT 2. ARITHMETIC

Loop 0 verified every unchanged cell (see the loop0 file). This pass recomputes every number that is new or changed in the rewrite.

| Metric | A4 value (A4 line) | Recomputed (c:) | Source line | Status |
|---|---|---|---|---|
| Perimeter vs parent ETR, Q2 FY27 | 25.24% vs 24.59% (L18) | 110.51 / 437.80 = 25.24%; 176.19 / 716.63 = 24.59% | L110-L114, L296-L299 | MATCH |
| Perimeter share of YoY Op EBITDA growth | 81.2% (L203, L245) | 281.56 / 346.95 = 81.15% | 1A less 1B | MATCH |
| M1 graft figures | 2.37 / 2.67 / 0.30 Cr; -6.9%; 2.4% / 2.5%; FCTR -0.25 / +2.18 Cr; 53.47% (L247, L272) | 236.98; 266.59; 29.61; 376.52 / 404.46 = 0.931; 45.05 / 1,892.26, 60.02 / 2,442.45; -24.96 / 217.88; 1,291.78 / 2,415.96 | L101-L121, L286-L296 | MATCH |
| Perimeter FV gain H1 FY27 vs H1 FY26 | nil vs 1.55 Cr (L252, L532) | 18.69 less 18.69 = 0; 264.50 less 109.27 = 155.23 | L212, L391 | MATCH |
| Perimeter OI and interest income H1 FY27 | 5.68 / 5.65 Cr (L532) | 1,291.78 less 723.59 = 568.19; 705.77 less 140.54 = 565.23 | L101, L287, L206, L387 | MATCH |
| Matched pre-WC conversion | H1 FY27 1.20x / 1.23x; H1 FY26 1.15x / 1.05x (L334) | 1,520.58 / (1,815.45 - 729.95 x 0.7514) = 1.200; (1,520.58 + 705.77) / 1,815.45 = 1.226; 1,079.89 / (1,682.88 - 977.74 x 0.7569) = 1.145; (1,079.89 + 692.82) / 1,682.88 = 1.053 | L204-L214, L221, L115 | MATCH |
| Removed-income totals | 729.95 / 977.74 lakh (L347) | 2.55 + 705.77 + 0.05 + 2.89 + 18.69; 3.43 + 692.82 + 8.88 + 8.11 + 264.50 | L204-L212 | MATCH |
| WC release split | liabilities 85.2%, assets 14.8% (L374) | 1,112.60 / 1,305.74 = 0.8521; (27.40 + 165.74) / 1,305.74 = 0.1479 | L216-L219 | MATCH |
| Perimeter other current liabilities | 22.04 Cr; parent -1.62, perimeter +4.99 Cr (L374, L529) | 2,594.32 less 390.09 = 2,204.23; 390.09 less 551.97 = -161.88; 2,204.23 less 1,704.99 = 499.24 | L184, L365 | MATCH |
| Perimeter share of group current investments | 95.1% Sep-26, 96.9% Mar-26 (L367) | 13,692.28 / 14,399.20 = 0.9509; 10,428.51 / 10,762.47 = 0.9690 | L154, L336 | MATCH |
| Intercompany OFA at March | 4.70 Cr (L369) | 1,769.30 less 1,299.22 = 470.08 | L341, L159 | MATCH |
| Standalone H1 FY26 buyback cell | nil (L35) | -402.20 - 42.72 - 13.11 = -458.03 = L418 | L413, L416, L417, L418 | MATCH |
| 12.15 Cr item = Rs 4.00 a share | exact (L94, L351, L514, L526) | 3,03,80,600 x 4.00 = 1,215.22 lakh = standalone gap | L124, L348, L301, L234, L235 | MATCH |
| Buyback economics | 18.0x; Rs 54.48; 30.9%; Rs 121.76; Rs 3.49; about 35x; Rs 6.74; about 18x (L74-L76) | 176.24 / 9.77 = 18.04; 16,959.49 lakh / 3,11,30,600 = 54.48; 54.48 / 176.24 = 0.309; 1,434.16 x 0.7566 / 3,11,30,600 = 3.485; 121.76 / 3.485 = 34.9; 681.20 x 4 x 0.7517 / 3,03,80,600 = 6.742; 121.76 / 6.742 = 18.1 | L124, L127, L101, L110, L147, L154, L156, L157, L178, L235 | MATCH |
| FY26 revenue average and core PBT range | Q1 58.19, Q2 58.79, H2 avg 60.09; core 3.46-3.78, H2 avg 3.55 (L271) | as loop 0 | L100, L101, L110 | MATCH |

Arithmetic result: no mismatch above rounding.

---

## AUDIT 3. ADVERSARIAL READ (revised review)

The rewrite changed which claims are most positive. The three most positive claims now are below, each attacked from the same extract.

### Claim 1. Core PBT ex-OI nearly doubled, 3.46 to 6.81 Cr (A4 L221, L246, L578).
The review now carries its own strongest counter (A4 L247: one quarter, all QoQ gain outside the parent, currency swing, H1 OI still 53.47% of PBT). The separator is stated (11.04% vs 8.36%). A fresh bear attempt finds nothing stronger in the extract. No graft needed.

### Claim 2. Matched pre-WC cash conversion is "above 1.0x on both matched bases, and improving YoY"; cash direction favourable (A4 L334, L378, L585). This claim is new in loop 1.
Strongest bear counter: the matched ratio follows Ind AS 7 conventions that flatter any CFO-to-PAT reading. Finance cost paid (L236, 87.79) and lease payments (L237, 46.36) sit in financing. Taxes paid (L221, 422.00) ran below the current tax charge (L112, 505.35) by 83.35. Charge all three and accrue current tax:
- H1 FY27, basis (b): (1,520.58 - 87.79 - 46.36 - 83.35) / 1,266.94 = 1,303.08 / 1,266.94 = 1.03x.
- H1 FY27, basis (a): (2,226.35 - 87.79 - 46.36 - 83.35) / 1,815.45 = 2,008.85 / 1,815.45 = 1.11x.
- H1 FY26 on the same strict basis: (1,079.89 - 47.15 - 38.51 - 115.93) / 942.81 = 0.93x; (1,772.71 - 47.15 - 38.51 - 115.93) / 1,682.88 = 0.93x (L236, L237, L112 533.22, L221 417.29).
Survives: NO. On the strict basis H1 FY27 is still above 1.0x (1.03x to 1.11x) and still improves on H1 FY26 (0.93x). A4's claim, its direction and its bases are correct as stated. The thin cushion on the strictest basis is logged for /fttcp as STYLE L1-S5, with no loop.

### Claim 3. "The revenue step looks real on the extract" (A4 L272), with the inorganic reading rejected (A4 L249).
Loop 0 tested this counter (inorganic or currency) and it failed. The consolidated investing sections (L223-L231) have no acquisition line. There is no goodwill line, intangibles are nil (L145), and the perimeter is unchanged (L73-L76, L431). Q1 FY27 stepped while FCTR was negative (L121). The revised text matches that test. Survives: NO.

### Mandatory purchase-economics probe
Buyback: the multiple is now stated in A4 Step 0C (A4 L73-L77) and recomputes. Investment in the WOS (L405): unchanged, and still not an acquisition at group level. A4 Q4, Q5 and forward map row 2 carry the bear reading. No graft needed.

---

## FINDINGS (tagged)

No FACTUAL, MISSING or CONTRADICTION finding in loop 1.

STYLE (logged, no loop):
- L1-S1 (carried from loop 0 S1). 33 boilerplate units are absent from A1's structured file and A2's ledger: 18 embedded numbers, 9 entities, 1 date, 5 formula captions. A1 should capture the page-3 and page-7 telephone and fax (L96, L282) next run, because they evidence A3-20.
- L1-S2 (carried from loop 0 S12). R121, R122, R394 and R395 are rows for blank Other-equity cells, against A1's own header rule. No value is lost.
- L1-S3 (new). A4 L25 says S2 "concern[s] A1/A2 capture and need[s] no A4 change". S2 concerned A4's blanket mark, and A4 closed it at L32. The changelog wording is wrong; the review itself is fine.
- L1-S4 (new). Brief A4 L582 opens with "The bear reading is strong." That is an unanchored judgement. Step 3 (A4 L272) finds the revenue step real and only the margin step unproven. Rule J asks for the same bar on both sides. Suggested: "The revenue step looks real. The margin step is one quarter old, and Q3 decides it."
- L1-S5 (new). The Pillar 2 fact (A4 L334, L373, L475) of 1.20x-1.23x follows Ind AS 7 conventions. On a strict basis that charges finance cost paid and lease payments and accrues current tax, it is 1.03x-1.11x (H1 FY27) vs 0.93x (H1 FY26). Still above 1.0x and improving. /fttcp should see the convention named next to the number.

---

## VERDICT

COMPLETE. Loop 0 findings F1, F2, F3, C1, M1 and M2 are closed. No new FACTUAL, MISSING or CONTRADICTION finding. loop_back_to "". Proceeds to Notion save with five STYLE notes recorded.
A4's protocol verdict (PROCEED WITH FLAGS) and cash class (INDETERMINATE-WITH-DIRECTION) stand.

---

```yaml
stage: A5-adversary
company: "CYBERTECH"
quarter: "q2fy27"
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
    - "L1-S1 (carried) 33 boilerplate units uncaptured by A1/A2 (18 embedded numbers, 9 entities, 1 date, 5 formula captions); capture L96/L282 telephone and fax next run (A3-20 evidence)"
    - "L1-S2 (carried) A1 rows R121, R122, R394, R395 for blank cells against A1's own rule; no value lost"
    - "L1-S3 A4 L25 changelog says S2 needed no A4 change; A4 closed S2 at L32"
    - "L1-S4 brief A4 L582 'The bear reading is strong' is an unanchored judgement; Step 3 L272 finds the revenue step real; suggest 'The revenue step looks real. The margin step is one quarter old, and Q3 decides it.'"
    - "L1-S5 Pillar 2 fact 1.20x-1.23x (A4 L334, L373, L475) follows Ind AS 7 conventions; strict basis (finance cost 87.79, lease 46.36, tax timing 83.35 charged) gives 1.03x-1.11x vs 0.93x H1 FY26; still above 1.0x and improving; name the convention for /fttcp"
loop_back_to: ""
gap: ""
style_notes:
  - "L1-S1 coverage boilerplate (33 units; capture L96/L282 next run)"
  - "L1-S2 A1 blank-cell rows"
  - "L1-S3 A4 L25 changelog mislabels S2"
  - "L1-S4 brief L582 'bear reading is strong' unanchored"
  - "L1-S5 name the Ind AS 7 convention on the 1.20x-1.23x Pillar 2 fact; strict basis 1.03x-1.11x"
analyst_note: "Iteration 1. All six loop 0 findings are closed, and every new number recomputes to the filed lines. Transfer pricing is now scoped to where profit sits, not the group gain. The perimeter ETR of 25.24% against the parent's 24.59% confirms that the tax-split effect is negligible. The new positive claim, matched pre-WC conversion above 1.0x and improving, survived a strict test. Charging finance cost paid, lease payments and the 0.83 Cr tax-payment lag still gives 1.03x-1.11x for H1 FY27 against 0.93x for H1 FY26. /fttcp should see that convention next to the Pillar 2 number. The brief's 'The bear reading is strong' is the one place the symmetric bar slips; it is STYLE. Coverage is unchanged and passes."
```
