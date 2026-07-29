# A5 ADVERSARY / COMPLETENESS AUDIT — PNGS Reva Diamond Jewellery Limited (PNGSREVA) — Q1 FY27

Artifacts audited (these only): A4 review `review_pngs_q1fy27.md`; A1 extract
`extract_results_pngs_q1fy27.txt`; A2 ledger `ledger_results_pngs_q1fy27.md`.
Standalone-only results filing, no concall/presentation this run. Units INR Million
(x0.1 = Rs Crore). All figures re-derived independently from the raw extract; A4/A3 cites
checked, not trusted.

---

## 1. COVERAGE AUDIT

Fresh grep passes: notes block (lines 238-282) `^\s*[0-9]+\s+[A-Za-z]` returns 7 numbered
notes (242, 246, 251, 257, 259, 261, 281); the other `^[0-9]` hits (177, 182, 194, 203,
205, 213, 218) are P&L section/Sr numbers and line 340 is a label wrap-fragment ("2 exclusive
brand stores"), not a note. Value-figure pattern returns 34 raw figure-occurrences across the
file (multi-column rows + IPO table + revenue sub-table); manual row sweep of the P&L
(lines 178-223) confirms 24 value-bearing rows, matching A2's refined count.

| Category | A2 count | My fresh count | Orphan rows (in ledger, absent from A4) | Status |
|---|---|---|---|---|
| Agenda items | 1 | 1 (l.15-46, single "approved" hit) | none | PASS |
| Auditor paragraphs | 4 | 4 (l.82, 88, 97, 125) | none | PASS |
| P&L value-bearing rows | 24 | 24 (l.178-223 manual sweep) | none | PASS |
| P&L structural/header rows | 6 | 6 (l.177,182,194,205,206-207,221) | none | PASS |
| Notes | 7 | 7 (l.242,246,251,257,259,261,281) | none | PASS |
| IPO utilisation rows (+1 footnote) | 4 (+1) | 4 rows (l.273,274-275,277,278) + footnote (l.279) | none | PASS |
| Management-comment items | 4 | 4 (l.309,333,338,342) | none | PASS |
| Revenue sub-table rows | 3 | 3 (l.318,319,320) | none | PASS |
| Signature blocks | 4 | 4 (l.36-44,135-153,288-292,350-355) | none | PASS |
| Entities in scope | 1 | 1 (standalone only) | none | PASS |

Every ledger row is either cited in A4's review or covered by the ledger-reconciliation
preamble (review line 13, which enumerates all categories and marks them reviewed, zero
unreviewed). A3 findings FN1-FN8 are all incorporated (review line 15). No orphan rows
(ledger row absent from A4). No row found by my fresh pass that the ledger lacks. Turns/slides
= 0 (results-only doctype) are correctly N.A., not unreviewed.

**Coverage verdict: PASS.** No loop-back to A2 or A3 on coverage.

---

## 2. ARITHMETIC AUDIT

Raw source (INR Million ÷ 10 = Rs Cr). Every derived metric in A4's Step 1, 2, 3, 4, 6, 7
tables recomputed from raw. Representative checks (all others also recomputed and tie):

| Metric | A4 value | My recomputed | Source line | Status |
|---|---|---|---|---|
| Cost of Materials Q1FY27 (Purch+ChgInv) | 76.141 | 106.619 + (-30.478) = 76.141 | l.183,184 | PASS |
| Operating EBITDA Q1FY27 (PBT+D+Fin-OI) | 33.927 | 36.398+0.357+2.748-5.576 = 33.927 | l.195,187,186,179 | PASS |
| Op EBITDA Margin Q1FY27 | 28.76% | 33.927/117.973 = 28.76% | derived | PASS |
| Reported EBITDA Margin Q1FY27 | 33.49% | 39.503/117.973 = 33.49% | derived | PASS |
| Gross Margin Q1FY27 | 35.46% | 41.832/117.973 = 35.46% | derived | PASS |
| Effective Tax Rate Q1FY27 | 25.24% | 9.188/36.398 = 25.24% | l.201,195 | PASS |
| Revenue YoY | +119.49% | (117.973-53.749)/53.749 = +119.49% | l.178 | PASS |
| Op EBITDA YoY | +192.90% | 22.344/11.583 = +192.90% | derived | PASS |
| Op EBITDA margin YoY | +721 bps | 28.76-21.55 = +7.21pp | derived | PASS |
| Other Income YoY | +1842.86% | 5.289/0.287 = +1842.86% | l.179 | PASS |
| Core Operating PBT YoY | +222.41% | 21.262/9.560 = +222.41% | derived | PASS |
| Reported PBT YoY | +269.64% | 26.551/9.847 = +269.64% | l.195 | PASS |
| PAT YoY | +265.33% | 19.762/7.448 = +265.33% | l.203 | PASS |
| EPS YoY | +151.61% | 5.17/3.41 = +151.61% | l.222 | PASS |
| PAT bridge reconciliation | ties to +19.762 | +24.914-0.821-0.319-0.763+5.289-1.749-6.789 = +19.762 | l.183-203 | PASS |
| Other Income after-tax share of PAT growth | 20.0% | 5.289×(1-0.2524)/19.762 = 3.954/19.762 = 20.0% | derived | PASS |
| Normalized PAT ex-OI YoY | +212% | 23.257/7.448 -1 = +212% | derived | PASS |
| Revenue QoQ | -14.59% | (117.973-138.126)/138.126 = -14.59% | l.178 | PASS |
| Core PBT ex-OI QoQ | +13.23% | 3.602/27.220 = +13.23% | derived | PASS |
| PAT QoQ | +27.10% | 5.801/21.409 = +27.10% | l.203 | PASS |
| 9M FY26 revenue (FY26 - Q4) | 300.902 | 439.028-138.126 = 300.902 | l.178 | PASS |
| Q1 rev as % of FY26 rev | 26.9% | 117.973/439.028 = 26.9% | l.178 | PASS |
| IPO total utilised % | 18.5% | 645.60/3491.23 = 18.5% | l.278 | PASS |
| 15-store object deployed % | 14.1% | 404.88/2865.64 = 14.1% | l.273 | PASS |
| Trailing PE | 13.19x | 374.8/28.41 = 13.19x | l.222 + brief | PASS |
| EPS Q1 as % of FY26 EPS (l.232) | 30.2% | 8.58/28.41 = 30.2% | l.222 | PASS |
| **PAT Q1 as % of full FY26 PAT (l.231)** | **26.9%** | **27.210/64.655 = 42.1%** | **l.203** | **FAIL** |

**FAIL detail (Step 6A, review line 231):** The variance table's PAT row states
"Q1 Rs27.210 Cr (26.9% of full FY26 PAT in one quarter)." Recomputed: 27.210 / 64.655
= 42.1%. The 26.9% figure is the REVENUE-to-revenue ratio (correctly used at review line 146:
"Q1 FY27 ... is 26.9% of the entire FY26 revenue") that was copy-pasted into the PAT row.
The parallel EPS row (line 232) correctly computes 30.2% (8.58/28.41), which isolates the PAT
row as the anomaly rather than a shared convention. Error magnitude 15.2pp, far above rounding.
Direction: the error UNDERSTATES the result (true 42.1% is even more supportive of "above base
trajectory"), so it does not flip the verdict, but it is a stated derived-metric mismatch and
per A5 discipline any mismatch above rounding = FAIL. **Loop back to A4** to correct
26.9% -> 42.1% in the Step 6A PAT row.

Secondary note (not scored as a separate arithmetic FAIL, narrative only): review line 110
verdict cell reads "core PBT grew faster than reported PBT ex-OI base." The recomputed rates
are core +222.41% vs reported PBT +269.64%, i.e. core grew SLOWER than reported PBT (the gap
is the Other Income spike, exactly as Step 2 diagnostic #4 correctly explains). The table
percentages themselves are correct; only the one-line characterization is muddled. A4 should
tidy the wording when fixing line 231.

All other derived metrics across Steps 1-7 tie to source within rounding.

---

## 3. ADVERSARIAL READ

The three most positive claims in A4, each with the strongest bear counter built from the
SAME extracted text, and whether the counter survives (i.e. is supported by the extract AND
not already incorporated by A4).

**Positive claim 1 — "~80% of the +265% PAT growth is recurring core, not treasury; headline
growth is largely real" (review l.121, l.171).**
Bear counter (from extract): reported gross profit / EBITDA of the quarter rests on a
Rs30.478 Cr finished-goods inventory build (l.184, "Changes in inventories (304.78)") that has
not converted to cash; growth is inventory-financed, not cash-generative.
Survives? NO — already fully incorporated. A4 flags the Rs30.478 Cr build as FN6 (Step 3
one-off, Step 5 directional cash read, Step 6D killing evidence), rules cash conversion
INDETERMINATE, and caps the verdict at PROCEED WITH CAVEATS explicitly for this reason.
Note: the sharper accounting form of the counter ("the inventory build inflates gross margin")
is invalid — the change-in-inventories line correctly matches unsold cost out of COGS, so the
35.46% margin is on goods sold; the legitimate cash concern is the one A4 already carries.

**Positive claim 2 — "Operating EBITDA margin 28.76% (+721 bps YoY), far above the 19-22%
modeled band; thesis CONFIRMED and STRENGTHENING" (review l.119, l.311).**
Bear counter (from extract): the margin is driven by diamond-studded mix (Rs115.987 Cr of
Rs117.973 Cr revenue, l.318) in a seasonally strong Akshaya-Tritiya quarter; Q4 FY26 GM was
only 27.73% and the filing gives no evidence the 35.46% GM is structural — it may normalize to
~22%.
Survives? NO — already incorporated. A4 marks the margin AMBIGUOUS per FN7, routes
sustainability to management (Step 8.5 Q2), and refuses to upgrade the entry zone on it.

**Positive claim 3 — "Revenue tracking at/above the bull FY27 path (Rs571 Cr), not base"
(review l.117, l.229).**
Bear counter (from extract): from the filing ALONE, Q1x4 = Rs471.9 Cr, which is ~17% BELOW
the Rs571 Cr bull anchor, and revenue actually FELL QoQ -14.59% (Rs138.126 -> Rs117.973). To
reach bull, the remaining 9M must average Rs151 Cr/qtr — a step-UP that the filing contains no
guidance to support (no concall, no order book this run). The "at/above bull" label leans on
the pre-results note (external to the filing) plus a seasonality assumption.
Survives? NO (marginally) — the load-bearing facts are present in A4: Step 2 diagnostic #1
shows the Q1x4 = Rs471.9 Cr figure and names the seasonality assumption; Step 3 shows the
-14.59% QoQ dip. The extract itself corroborates a seasonal step-up (FY26 shape: Q1 Rs53.749 Cr
vs Q2+Q3 avg Rs123.6 Cr vs Q4 Rs138.126 Cr), so the H2-heavier pattern is not unfounded. The
characterization is optimistic but the counter is disclosed, not suppressed; nothing new to
graft. Recommend A4 soften "tracking bull, not base" to "Q1 annualizes below bull; reaching
bull needs the FY26-shaped H2 step-up" when it corrects line 231 — improvement, not a required
graft.

No bear counter survives as an unincorporated finding requiring insertion. The single
completeness failure is arithmetic, not adversarial.

---

## VERDICT

**INCOMPLETE.** Loop back to **A4**. Gap: Step 6A variance table (review line 231) states Q1
FY27 PAT is "26.9% of full FY26 PAT"; the correct derived ratio is 27.210/64.655 = 42.1%.
The 26.9% is the revenue ratio copy-pasted from line 146 into the PAT row (the parallel EPS
row at line 232 is correctly computed at 30.2%). A 15.2pp derived-metric mismatch above
rounding = FAIL. Correct to 42.1% (and tidy the line 110 core-vs-reported-PBT wording). All
coverage checks pass; no surviving bear counter requires grafting. Only COMPLETE proceeds to
Notion save; this does not.

```yaml
stage: A5-adversary
company: "PNGSREVA"
quarter: "q1fy27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches:
  - metric: "Step 6A: Q1 FY27 PAT as % of full FY26 PAT"
    a4_value: "26.9%"
    recomputed: "42.1% (27.210 / 64.655)"
    source_line: "review l.231; raw PAT l.203 (272.10M / 646.55M)"
surviving_bear_counters: []
loop_back_to: "A4"
gap: "Step 6A variance table (review line 231) states Q1 PAT = 26.9% of full FY26 PAT; correct value is 42.1% (27.210/64.655). The 26.9% is the revenue ratio copy-pasted from line 146; the parallel EPS row (l.232, 30.2%) is correct. Fix 26.9% -> 42.1% and tidy the line 110 core-vs-reported-PBT wording."
```
