# STAGE 1 — GATE 0, BLOCK F (MOAT) RERUN
TAAL Tech Ltd (TAALTECH) | Original run: taaltech-2026-09-10 | Rerun date: 2026-09-21
Model: claude-sonnet-5 | Scope: BLOCK F ONLY. Blocks A-E and the core score
are NOT restated and NOT rescored in this document.

---

## 1. WHAT CHANGED AND WHY

The original Stage 1 run scored the moat block 11/60 with M2 (Cost
Advantage), M5 (Scale & Dominance) and M9 (Brand) all at zero, on the
stated basis "PEER DATA NEEDED — no peer financial statements in this
run's input set" (01-gate0.md, Block F table; B01-gate0.yaml
input_gaps). That basis was wrong. Three populated peer Data_Sheet CSVs
were already in the corpus at
runs/taaltech-2026-09-10/inputs/screening/ (TATAELXSI-, CYIENT-,
ONWARDTEC-Data_Sheet.csv) and were never passed to the stage. The
operator logged this as correction C8 in the Halt 1 ruling of 20-Sep-2026
and gated this rerun before /fttcp.

This rerun reads all four Data_Sheet.csv files (TAALTECH's own plus the
three peers), applies the M2/M5/M9 rules exactly as specified, and
re-scores only those three sub-tests. The other nine moat sub-tests
(M1, M3, M4, M6, M7, M8, M10, M11, M12) do not depend on peer data and
are carried forward unchanged from the original run, per scope.

One further, more precise finding falls out of doing the work rather
than just supplying "peer data exists now": the peer set is not uniform
quality. TATAELXSI-Data_Sheet.csv's P&L/Balance Sheet/Cash Flow sections
run FY2008-03-31 to FY2015-03-31 only (TATAELXSI-Data_Sheet.csv, line 10)
— an 11-to-19-year-old, non-contemporaneous export. Only its META block
(Current Price 3403.0, Market Capitalization 21202.62, TATAELXSI-Data_Sheet.csv
lines 7-8) is current. CYIENT- and ONWARDTEC-Data_Sheet.csv both carry a
full FY2017-FY2026 series matching TAALTECH's own window exactly. This
means M2 (a margin-level comparison, which needs a contemporaneous
figure) can only draw on 2 of 3 peers with confidence; M5 (an mcap
ranking, which needs only a current point figure) can draw on all 4.

A second finding, specific to M9, is that unblocking the PEER side of
the test does not unblock the test: the rule's Brand proxy needs a
gross-margin figure built from a Material Cost / COGS line, and that
line is genuinely not populated for TAALTECH itself (blank across
FY2019-FY2026 in screener-Data_Sheet.csv) or for Onward Technologies from
FY2023 onward (ONWARDTEC-Data_Sheet.csv). Treating a blank field as a
literal zero cost to force a 100% "gross margin" would be estimating a
missing number, which the pipeline rules and CLAUDE.md both forbid. M9
stays blocked, but the diagnosis changes from "peer data needed" to
"the subject's own Material Cost field is not disclosed, and the rule's
named proxy cannot be built without assuming a value for it."

Net effect: M2 and M5 unblock and score; M9 stays at zero on a corrected,
more specific basis. Moat score moves 11/60 to 19/60; moat classification
moves MODERATE to STRONG; the core score (70/100, unchanged) crosses into
the "Core 60-79 + STRONG/FORTRESS" row of the classification matrix, so
the Gate 0 classification moves GOOD to GOOD+.

---

## 2. PEER COMPARISON TABLE

All figures FY2026 (year ended 31-Mar-2026) unless marked otherwise.
Operating Profit / EBITDA computed on the same formula used for TAALTECH
in the original run's Load-Bearing Fact 1: Sales − Raw Material Cost −
Change in Inventory − Power & Fuel − Other Mfr. Exp − Employee Cost −
Selling & Admin − Other Expenses (excludes Other Income, Depreciation,
Interest). For TAALTECH and Onward, Raw Material Cost and Change in
Inventory are blank for FY2026 (treated as not present, contributing
nothing to the subtraction — not assumed zero-cost for any OTHER
purpose, see M9 below).

| Field | TAALTECH | Cyient | Onward Technologies | Tata Elxsi |
|---|---|---|---|---|
| Data period, P&L/BS/CF | FY2017-FY2026 | FY2017-FY2026 | FY2017-FY2026 | **FY2008-FY2015 only** |
| Latest year usable for margin compare | FY2026 | FY2026 | FY2026 | FY2015 (stale, 11yr old) |
| Revenue, latest usable yr (Rs cr) | 197.43 (screener-Data_Sheet.csv, L11) | 7268.2 (CYIENT-Data_Sheet.csv, L11) | 543.85 (ONWARDTEC-Data_Sheet.csv, L11) | 849.4 (TATAELXSI-Data_Sheet.csv, L11) |
| Employee Cost | 115.13 (L16) | 4040.8 (L16) | 395.96 (L16) | 462.14 (L16) |
| Selling & Admin | 17.59 (L17) | 385.4 (L17) | 21.33 (L17) | 116.06 (L17) |
| Other Mfr. Exp | 1.37 (L15) | 317.6 (L15) | 48.39 (L15) | 59.27 (L15) |
| Power & Fuel | 0.67 (L14) | 29.1 (L14) | 1.79 (L14) | 8.2 (L14) |
| Other Expenses | 3.17 (L18) | 810.0 (L18) | 4.53 (L18) | 1.37 (L18) |
| Raw Material Cost | blank/NOT FOUND (L12) | 812.8 (L12) | blank/NOT FOUND (L12) | 24.64 (L12) |
| Change in Inventory | blank/NOT FOUND (L13) | 26.6 (L13) | blank/NOT FOUND (L13) | 0.29 (L13) |
| Operating Profit / EBITDA (computed) | 59.50 | 845.9 | 71.85 | 177.43 |
| **EBITDA margin** | **30.14%** | **11.64%** | **13.21%** | 20.89% (FY2015, not contemporaneous) |
| Current Price (Rs) | 5163.7 (L7) | 1077.85 (L7) | 290.95 (L7) | 3403.0 (L7) |
| **Market Capitalization (Rs cr)** | **1609.15** (L8) | 11980.65 (L8) | 647.35 (L8) | 21202.62 (L8) |
| Mcap rank (of 4) | 3rd | 2nd | 4th (smallest) | 1st (largest) |
| Margin rank (of 4, TAALTECH FY26 vs peers' most recent available) | 1st | 3rd | 2nd | 4th (and stale) |

**M2 peer median (Cyient + Onward, the two contemporaneous peers)**:
(11.64% + 13.21%) ÷ 2 = **12.43%**. TAALTECH 30.14% − 12.43% = **+17.71pp**.
Robustness check: including Tata Elxsi's stale FY2015 figure as a third
peer (not used for scoring, shown for completeness) gives a 3-peer
median of 13.21% (middle of 11.64/13.21/20.89) — the gap would still be
+16.93pp, same qualifying band either way.

---

## 3. THE 12 MOAT SUB-TESTS — ORIGINAL, RERUN, REASON

| # | Test | Original | Rerun | Reason |
|---|---|---|---|---|
| M1 | Pricing Power | 0 | 0 (unchanged) | Not peer-data-dependent; out of rerun scope. Original basis stands: OPM expanded 11.4%→30.1% FY17→FY26 but revenue CAGR 8.85% is below the ≥10% qualifying floor for any non-zero band. |
| M2 | Cost Advantage vs peer median EBITDA margin | 0 (PEER DATA NEEDED) | **5** | Peer median (Cyient + Onward, FY2026, contemporaneous) = 12.43%. TAALTECH FY2026 EBITDA margin 30.14%. Gap +17.71pp ≥5pp above → band 5. Tata Elxsi's FY2015 figure (20.89%) is not used in the scored median because it is not contemporaneous with TAALTECH's FY2026 (TATAELXSI-Data_Sheet.csv carries no data past FY2015); shown only as a robustness check, which does not change the qualifying band. |
| M3 | Capital Efficiency | 5 | 5 (unchanged) | Not peer-data-dependent; out of rerun scope. Original flag stands: FAT is a formula artifact for this near-zero-fixed-asset services business, not a productive-asset moat signal. |
| M4 | Customer Stickiness | 0 | 0 (unchanged) | Not peer-data-dependent; out of rerun scope. 3 revenue-decline years (FY20, FY21, FY25) → "3+ decline years" band. |
| M5 | Scale & Dominance | 0 (PEER DATA NEEDED) | **3** | Mcap ranking (all 4 companies, current META figures): Tata Elxsi 21202.62 > Cyient 11980.65 > TAALTECH 1609.15 > Onward 647.35. TAALTECH is 3rd of 4 → within "top 3 mcap." Margin ranking: TAALTECH's 30.14% is the highest of the four figures shown (even counting Tata Elxsi's stale 20.89%) → within "margin top 2." "Top 3 mcap AND margin top 2" → band 3. Does NOT reach band 5 (TAALTECH is not the largest mcap; Tata Elxsi is ~13x larger). FLAG: the "segment" here is a 4-company total universe (TAALTECH + 3 selected peers), not an exhaustively counted listed segment; "top 3 of 4" is a low bar on this small a peer set. The margin-ranking leg also rests partly on Tata Elxsi's 11-year-stale figure for the 4th-place comparator, which does not affect TAALTECH's own rank but is named as a data-quality limitation. |
| M6 | Technology/R&D | 0 | 0 (unchanged) | Was never blocked by peer data — TAALTECH's own R&D/Revenue ratio (0.19%, AR p.49) already fails the ≥1% floor regardless of peer figures. No Data_Sheet in this run's set (subject or peer) carries an R&D expense row; the field structurally does not exist in this CSV template for any of the four companies. Out of rerun scope; unchanged. |
| M7 | Regulatory/License | 0 | 0 (unchanged) | Not peer-data-dependent; out of rerun scope. Unregulated ER&D services business. |
| M8 | Distribution | 0 | 0 (unchanged) | Not peer-data-dependent; out of rerun scope. No physical distribution network. |
| M9 | Brand | 0 (PEER DATA NEEDED) | **0 (confirmed, reason corrected)** | The rule's GM proxy is (Revenue − Material Cost) ÷ Revenue. Peer data no longer blocks this test — Cyient's Material Cost line is populated (FY2026: Rs812.8cr + Rs26.6cr change in inventory, CYIENT-Data_Sheet.csv L12-13). But TAALTECH's OWN Material Cost / Change in Inventory rows are blank/NOT FOUND for FY2026 (screener-Data_Sheet.csv, L12-13; blank since FY2019) and Onward's are blank since FY2023 (ONWARDTEC-Data_Sheet.csv, L12-13). Computing the GM proxy by treating a blank field as zero cost would produce TAALTECH ≈100% "gross margin," which is estimating a value for a missing number — forbidden by the pipeline's rule 5 and by CLAUDE.md's "never estimate a missing number." The blocking field moved from "peer data" to "the subject's own Material Cost / COGS line," which this corpus does not carry for TAALTECH at any post-FY2018 year. Kept at 0. |
| M10 | Switching Costs | 1 | 1 (unchanged) | Not peer-data-dependent; out of rerun scope. |
| M11 | Network Effects | 5 | 5 (unchanged) | Not peer-data-dependent; out of rerun scope. Original flag stands: borderline pass, 0.44pp CAGR gap. |
| M12 | Negative WC/Float | 0 | 0 (unchanged) | Not peer-data-dependent; out of rerun scope. |

**Where M9's still-blocking field would be found**: a cost-of-services /
cost-of-revenue note distinct from Employee Cost, in TAALTECH's audited
financial statements, broken out by materials or bought-out components,
if one exists. None is in this corpus (the FY2026 AR's P&L follows the
Schedule III nature-of-expense format used by screener, which is exactly
what Data_Sheet.csv already reflects — there is no deeper materials note
to find). More likely, per the Outsourcing partner (ER&D services)
archetype, the field is not merely undisclosed but structurally
inapplicable: a billable-engineer delivery model has no
materials/COGS component distinct from Employee Cost, so the rule's
named GM proxy may not be a constructible figure for this archetype at
all, independent of which company reports it.

---

## 4. REVISED MOAT TOTAL AND CLASSIFICATION

**Moats present (score ≥3), original**: 2 of 12 (M3, M11)
**Moats present (score ≥3), rerun**: 4 of 12 (M2, M3, M5, M11)

**MOAT SCORE, original: 11/60**
**MOAT SCORE, rerun: 19/60** (11 + M2's 5 + M5's 3; M9 unchanged at 0)

**MOAT CLASSIFICATION, original: MODERATE** (2 present → 2-3 band)
**MOAT CLASSIFICATION, rerun: STRONG** (4 present → 4-5 band)

Moat profile, rerun:
```
M1  [                    ] 0
M2  [########## ] 5  present  (was 0, PEER DATA NEEDED)
M3  [########## ] 5  present  (unchanged)
M4  [                    ] 0
M5  [######      ] 3  present  (was 0, PEER DATA NEEDED)
M6  [                    ] 0
M7  [                    ] 0
M8  [                    ] 0
M9  [                    ] 0  (was PEER DATA NEEDED; now confirmed blocked
                                on the subject's own Material Cost gap)
M10 [##                  ] 1
M11 [########## ] 5  present  (unchanged, borderline)
M12 [                    ] 0
```

---

## 5. EFFECT ON GRAND TOTAL AND GATE 0 CLASSIFICATION

Blocks A-E and the core score are UNCHANGED from the original run
(Block A 15, Block B 14, Block C 12, Block D 20, Block E 9 — see
01-gate0.md; not restated here per scope).

| | Original | Rerun |
|---|---|---|
| Core Score (A+B+C+D+E) | 70/100 | 70/100 (unchanged) |
| Moat Score (F) | 11/60 | 19/60 |
| Grand Total | 81/160 | 89/160 |
| Moat Classification | MODERATE | STRONG |
| Deal-breakers triggered | none | none (unchanged; Block F does not feed the deal-breaker list) |

Classification matrix (Master v3.7/pipeline rule): Core 70 sits in the
60-79 band. Original moat class MODERATE placed the run in "Core 60-79 +
else = GOOD." Rerun moat class STRONG moves the same core score into
"Core 60-79 + STRONG/FORTRESS = GOOD+."

**CLASSIFICATION, original: GOOD**
**CLASSIFICATION, rerun: GOOD+**

```
╔══════════════════════════════════════╗
║  CLASSIFICATION: GOOD+  (was GOOD)    ║
║  Core Score: 70/100 (unchanged)       ║
║  Moat: STRONG (19/60, 4 confirmed)    ║
║  Grand Total: 89/160 (was 81/160)     ║
║  Deal-breakers triggered: NONE        ║
║  History downgrade flag: TRUE (Block  ║
║  A-E finding, unchanged, unrelated    ║
║  to this rerun)                       ║
╚══════════════════════════════════════╝
```

This is a mechanical, data-driven upgrade from an orchestration
correction, not a reassessment of company quality. All three flags
carried by the original 01-gate0.md (FLAG-GATE0 on the FY2017-base
growth read, FLAG-CASH on deteriorating cash conversion, FLAG-RPT on the
Vishkul loan) are unaffected and continue to propagate downstream
unchanged. The two new M2/M5 passes rest on a genuinely large margin gap
(TAALTECH 30.1% EBITDA margin vs a peer median near 12-13%) and a
top-quartile-of-a-small-set mcap/margin position; both are named,
anchored findings, not judgment calls, and the small size of the peer
universe (n=4) is flagged for downstream weighing rather than folded
silently into the score.

---
