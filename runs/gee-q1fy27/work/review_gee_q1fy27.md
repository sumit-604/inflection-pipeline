# GEE Limited (GEE) — Q1 FY27 — MERGED QUARTERLY REVIEW (A4 ANALYST)

Role 4 (Quarterly Results Review Protocol v1.2) executed in full step sequence over the A1 extract, A2 ledger, and A3 forensics.
**Role 5 (Concall Analysis Protocol v1.1) is N.A. this run** — no concall transcript and no investor presentation were supplied for Q1 FY27. Every Role 5 artifact (claims inventory, forward-guidance table, promise-vs-delivery audit, Q&A decomposition, tone/specificity, archetype) is therefore not produced; its inputs do not exist in this cycle. This is logged, not skipped.

Source extract: `runs/gee-q1fy27/work/extract_results_gee_q1fy27.txt` (line anchors below are that file's `cat -n` numbers).
Unit convention: filing is in **Rs Lakhs** (line 69). Reported in **Rs Crores** = Lakhs x 0.01, per pipeline convention. Line-number anchors preserved to the Lakhs extract.

> **REV NOTE (A5 arithmetic loop-back):** Step-4 reported-PAT-YoY total corrected from +₹6.87 Cr to **+₹5.87 Cr** (line 99: 684.55 − 97.59 = 586.96 L = ₹5.87 Cr — a Crore-conversion slip; the Lakhs figure and all bridge components were already correct). Step-4 recurring/non-recurring split recomputed against the correct ₹5.87 Cr denominator. "Half one-off" framing corrected to **~63% one-off** (exceptional 369.55/586.96 = 63.0%). Cash-conversion INDETERMINATE cap and PROCEED WITH CAVEATS verdict unchanged — arithmetic correction, not a thesis change.

---

## LEDGER RECONCILIATION PREAMBLE (contractual, stated before Step 1)

Ledger contains **6 notes / 0 turns / 0 slides** (plus 28 line items, 5 agenda items, 5 auditor paragraphs, 3 signature blocks, 4 zero-standing rows, 0 consolidation entities). **All rows reviewed.** A2 gate: pass (`gate_a2: pass`). A3 gate: pass, 100% reconciled (`gate_a3: pass`, `ledger_reconciled_pct: 100`).

Findings incorporated (all seven A3 findings): **F1.1, F6.1, F8.1, F9.1, F10.1, F13.1, F14.1.**
- FORWARD-SIGNAL: F10.1 (warrant dilution overhang), F13.1 (FY26 AR imminent).
- AMBIGUOUS: F1.1 (property-sale exceptional / operational CFO undisclosed), F14.1 (director date inconsistency).
- NEUTRAL-FACT: F6.1 (dated commitments), F8.1 (tax forensics), F9.1 (OCI).

No ledger row is unreviewed. **Proceeding to Step 1.**

Structural N.A. declarations (stated, not left blank): this is a STANDALONE unaudited filing with a **single reportable segment** (Note 3, lines 119-120), **no consolidated statement and no subsidiaries**. Therefore A3 checks F2 (standalone-vs-consolidated decomposition), F3 (shell entity), F4 (unaudited contribution ratio), F12 (segment forensics) and F15 (entity diffs) fall N.A. this cycle. The standalone-vs-consolidated PAT gap, normally a first-class metric, is **N.A. — no consolidated statement exists this cycle** (recorded as such in the YAML `sc_gap_pat_pct`).

---

## STEP 0 — PRE-FLIGHT

**0A. Notion Decision Status (verified before any framing): WATCHLIST / AVOID.** Gate 0 33/160 AVOID (3 deal-breakers); EM 30 (Modest); Promoter CONCERN. Position rule: ZERO at any price until 3+ triggers fire, and specifically Trigger #1 (operational CFO positive ex-asset-sales) must fire. Entry zone ₹46-52 (DA ₹40-45); MoS ₹37-42 (DA ₹32-36). CMP at Notion analysis (13 Jun 2026) ₹83; current CMP ND (no live quote in this run). This Q1 FY27 filing is the **pre-committed re-examination point** named in the thesis. Not held → **Step 8A-W branch** applies (non-held name), NOT 8A.

**0B. Unit convention:** Rs Lakhs (line 69). Conversion to Rs Crores = x0.01. Stated.

**0C. Share-count changes:** Paid-up equity doubled YoY, ₹519.77 L (Q1 FY26, line 103) → ₹1,039.54 L (Q1 FY27), face value ₹2 unchanged. This is the **1:1 bonus of Oct 2025** (Notion). Reported EPS is retrospectively bonus-adjusted per Ind AS 33 (check: Q1 FY26 PAT 97.59 / 519.77 = ₹0.19 = reported EPS on line 109; on pre-bonus 259.885 L shares it would read ₹0.375). Therefore **reported EPS is already share-adjusted and directly comparable** across all four columns. Paid-up is UNCHANGED QoQ (Q4 FY26 = Q1 FY27 = ₹1,039.54 L) → the **51 lakh promoter warrants at ₹80 are NOT yet converted** at 30-Jun-26 (F10.1).

**0D. Notes extraction (mandatory, all 6 read before any growth metric):**

| Note # | Subject | What it says (1 sentence) | ₹ Cr impact | Period affected | Comparability impact |
|---|---|---|---|---|---|
| 1 (lines 112-114) | LRR authority | Results reviewed by Audit Committee and approved by Board 06-Aug-2026; Limited Review under Reg 33. | ND | Q1 FY27 | None (procedural). |
| 2 (lines 115-118) | Basis of prep | Prepared per Ind AS recognition/measurement, Sec 133, Reg 33. | ND | Q1 FY27 | None (procedural). |
| 3 (lines 119-120) | Single segment | Operates mainly in ONE segment: manufacturing/selling of welding consumables; Ind AS 108 segment disclosure N/A. | ND | All | Confirms single-segment; no segment YoY comparability issue; F12 N.A. |
| **4 (lines 122-123)** | **Exceptional gain** | **Sold two immovable properties; resultant profit ₹369.55 L booked as Exceptional item.** | **+₹3.70 Cr** | **Q1 FY27** | **CRITICAL — non-recurring gain = 40.4% of PBT-after-exceptional (914.79). MUST strip for trajectory. Ties to line 89.** |
| 5 (lines 124-125) | Restatement | Previous-period figures restated/regrouped/rearranged to be comparable. | ND | Comparatives | Prior-period figures declared comparable; but no restatement detail given — take at face, flag as unverifiable. |
| 6 (lines 126-127) | Website upload | Results to be uploaded to company website + BSE. | ND | Q1 FY27 | None (procedural). Numbering anomaly "6.The results" (F14.1 drafting-control data point). |

**Auditor opinion check:** **UNMODIFIED / UNQUALIFIED** review conclusion (line 188: "Our conclusion on the Statement is not modified"). No Emphasis of Matter, no Other Matters, no Going Concern paragraph (A2 §5; A3 F5 PASS). Auditor = **SAPD & Associates**, FRN 327271E, UDIN 26069240AKMFHN3898 present (lines 190-198). Matches Notion incumbent — **no auditor change; file-closure trigger #2 does NOT fire on this filing.** (Note: the FY26 statutory audit opinion is a separate event, resolving only in the FY26 AR — see F13.1 / trigger #7, pending.)

**0E. Business type:** **Standard operating business** (welding consumables manufacturer). NOT a lender. Steps 1 and 5 (not 1L/5L) apply.

Confirmed: Notion fetched (Decision Status WATCHLIST/AVOID), units Lakhs→Cr, 1:1 bonus + unconverted warrants noted, all 6 notes extracted, auditor opinion unmodified, business type standard. Proceeding.

---

## STEP 1 — DATA EXTRACTION TABLE (Rs Crores; anchors to Lakhs extract)

Columns: Q1 FY26 (30-Jun-25, Unaudited) | Q4 FY26 (31-Mar-26, Audited) | Q1 FY27 (30-Jun-26, Unaudited) | FY25 | FY26 (31-Mar-26, Audited). **FY25 is not present in this filing → ND for every FY25 cell.**

| Line Item | Q1 FY26 | Q4 FY26 | Q1 FY27 | FY25 | FY26 |
|---|---|---|---|---|---|
| Revenue from Operations (line 73) | 79.18 | 112.16 | 102.86 | ND | 369.14 |
| Other Income (line 74) | 0.02 | 1.12 | 0.31 | ND | 1.20 |
| Total Income (line 75) | 79.20 | 113.29 | 103.17 | ND | 370.34 |
| Cost of Raw Materials Consumed (line 78) | 65.36 | 69.63 | 66.50 | ND | 255.65 |
| Purchase of Stock-in-Trade (line 79) | 0.06 | 11.65 | 13.61 | ND | 17.14 |
| Changes in Inventories (line 80) | (4.05) | (1.81) | (0.77) | ND | (1.42) |
| Employee Benefits Expense (line 82) | 4.41 | 7.05 | 5.25 | ND | 20.79 |
| Finance Costs (line 83) | 2.24 | 1.82 | 1.85 | ND | 8.46 |
| Depreciation & Amortisation (line 84) | 1.02 | 0.77 | 1.01 | ND | 3.83 |
| Other Expenses (line 85) | 8.85 | 14.51 | 10.26 | ND | 43.58 |
| Total Expenses (line 86) | 77.90 | 103.62 | 97.71 | ND | 348.03 |
| PBT before Exceptional (line 88) | 1.30 | 9.66 | 5.45 | ND | 22.30 |
| Exceptional items — Less/(Add) (line 89) | — (nil) | 3.34 (charge) | (3.70) (gain) | ND | 3.34 (charge) |
| PBT after Exceptional (line 90) | 1.30 | 6.33 | 9.15 | ND | 18.97 |
| Tax Expense — total (line 97) | 0.33 | 2.79 | 2.30 | ND | 5.97 |
| PAT (line 99) | 0.98 | 3.54 | 6.85 | ND | 13.00 |
| Other Comprehensive Income (line 100) | 0.001 | (0.01) | 0.01 | ND | (0.01) |
| Total Comprehensive Income (line 101) | 0.98 | 3.53 | 6.85 | ND | 12.99 |
| Paid-up Equity Capital (line 103) | 5.20 | 10.40 | 10.40 | ND | 10.40 |
| Other Equity ex-Reval Reserve (line 106) | ND | ND | ND | ND | 134.76 |
| EPS Basic reported ₹ (line 109) | 0.19 | 0.68 | 1.32 | ND | 2.50 |
| EPS Diluted reported ₹ (line 110) | 0.19 | 0.67 | 1.30 | ND | 2.46 |
| EPS (share-adjusted, ₹) — bonus already retrospective | 0.19 | 0.68 | 1.32 | ND | 2.50 |

Notes on cells: Q4 FY26 and FY26 exceptional item of ₹3.34 Cr is a **CHARGE** (Less), not explained in this filing — its nature is **ND** (Note 4 covers only the Q1 FY27 property-sale gain). Flagged. Q1 FY26 exceptional is nil (dash, A2 ZERO_STANDING row 14). Other Equity is annual-only balance-sheet disclosure (blank at all interim columns; A2 ZERO_STANDING row 25) → ND for the three non-annual columns, not estimated.

Check (self-consistency of the PAT-YoY base used downstream): Step 1 PAT Q1 FY27 − Q1 FY26 = 6.85 − 0.98 = **+₹5.87 Cr**. This is the denominator Step 4 must use.

**Derived metrics (Operating EBITDA computed off PBT-before-exceptional to strip the non-operating exceptional; formula PBT + D + Finance Costs − Other Income):**

| Derived Metric | Formula | Q1 FY26 | Q4 FY26 | Q1 FY27 | FY25 | FY26 |
|---|---|---|---|---|---|---|
| Operating EBITDA (₹ Cr) | PBT(pre-exc) + D + FinCost − OI | 4.54 | 11.13 | 8.00 | ND | 33.40 |
| Operating EBITDA Margin | OpEBITDA / Revenue | 5.74% | 9.92% | 7.78% | ND | 9.05% |
| Reported EBITDA (₹ Cr, incl OI) | PBT(pre-exc) + D + FinCost | 4.56 | 12.25 | 8.31 | ND | 34.59 |
| Core PBT ex-OI (₹ Cr, pre-exc) | PBT(pre-exc) − OI | 1.28 | 8.54 | 5.14 | ND | 21.11 |
| Other Income / PBT | OI / PBT(after-exc) | 1.74% | 17.78% | 3.38% | ND | 6.31% |
| Effective Tax Rate | Tax / PBT(after-exc) | 25.17% | 44.03% | 25.17% | ND | 31.46% |
| PAT Margin (on Revenue) | PAT / Revenue | 1.23% | 3.16% | 6.66% | ND | 3.52% |

Anchor observations for the walks: Q1 FY27 and Q1 FY26 ETR are **identical at exactly 25.17%** (230.24/914.79 = 32.82/130.41) — confirming F8.1: a flat statutory estimate, not a full computation; the H2 deferred-tax true-up (₹104.47 L booked only at Q4 FY26, line 96) will step H2 ETR up. Q4 FY26 ETR 44.03% is inflated by that annual deferred-tax true-up on a lower (post-charge) PBT base.

Every cell above is a line-anchored number or the literal ND. No estimation.

---

## STEP 2 — Q1 FY27 YoY COMPARISON (Q1 FY27 vs Q1 FY26) — THE MOST IMPORTANT STEP

| Metric | Q1 FY26 | Q1 FY27 | YoY % Change | Verdict |
|---|---|---|---|---|
| Revenue from Operations (₹ Cr) | 79.18 | 102.86 | +29.9% | Strong topline growth |
| Operating EBITDA (₹ Cr) | 4.54 | 8.00 | +76.1% | Operating leverage positive |
| Operating EBITDA Margin | 5.74% | 7.78% | +204 bps | Genuine margin expansion |
| Depreciation (₹ Cr) | 1.02 | 1.01 | −0.8% | Flat; no capex absorption spike |
| Finance Costs (₹ Cr) | 2.24 | 1.85 | −17.7% | Lower interest burden |
| EBIT operating (₹ Cr) | 3.53 | 6.99 | +98.3% | Nearly doubled |
| Other Income (₹ Cr) | 0.02 | 0.31 | +1260.8% | Off a near-nil base; immaterial ₹0.31 Cr |
| **Core Operating PBT ex-OI (₹ Cr, pre-exc)** | 1.28 | 5.14 | **+301.4%** | **Core operations genuinely improved (4.0x)** |
| Reported PBT after exceptional (₹ Cr) | 1.30 | 9.15 | +601.5% | Inflated by ₹3.70 Cr property-sale gain |
| PAT (₹ Cr) | 0.98 | 6.85 | +601.5% | 40.4% of PBT-after-exc is non-recurring |
| EPS share-adjusted (₹) | 0.19 | 1.32 | +594.7% | Same distortion as PAT |

**Six mandatory diagnostics:**

1. **Did revenue grow YoY?** Yes, +29.9% (₹79.18 Cr → ₹102.86 Cr). This clears Notion monitoring trigger #2 (≥₹95 Cr) and sits far above closure trigger #5 (<₹70 Cr, does NOT fire). It also exceeds the Notion "STAGNANT ~₹369 Cr" FY baseline on an annualised basis (₹102.86 × 4 = ₹411 Cr), but this is one quarter and QoQ it declined (see Step 3) — do not annualise a single print into a trend.

2. **Did operating EBITDA margin expand, contract or stay flat YoY?** Expanded: **Q1 FY27 7.78% vs Q1 FY26 5.74% = +204 bps**. This is real YoY expansion (not sequential noise), though still below the FY26 full-year 9.05% and far below the Notion 13% FY29 target.

3. **Did core operating PBT ex-OI grow YoY?** Yes, and cleanly: **+301.4% (₹1.28 Cr → ₹5.14 Cr, 4.0x)**. Critically, core operating PBT rose independent of both Other Income (₹0.31 Cr, immaterial) and the exceptional gain. So unlike a treasury-driven print, the operational core is genuinely up. This is the single most important honest signal in the filing and is what makes F1.1 AMBIGUOUS rather than a clean "one-off" dismissal.

4. **What drove the gap between core operating PBT growth (+301%) and reported PAT growth (+601%)?** The gap is almost entirely the **₹3.70 Cr exceptional property-sale gain** (Note 4). Walk (₹ Cr): core operating PBT ex-OI +₹3.86 Cr; +Other Income change +₹0.29 Cr; +finance-cost saving +₹0.40 Cr; +depreciation change +₹0.01 Cr → PBT-before-exceptional +₹4.15 Cr; + exceptional gain +₹3.70 Cr; − higher tax −₹1.97 Cr = **+₹5.87 Cr PAT**. The exceptional gain is **63.0% of the reported PAT increase** (369.55/586.96 L) and 40.4% of reported PBT-after-exceptional. Nearly two-thirds of the headline PAT jump is a one-off asset sale; the operating core supplies the rest.

5. **Are D&A and finance costs scaling faster than revenue?** No — the opposite. Depreciation flat (−0.8%) and finance costs DOWN 17.7% against revenue +29.9%. No capex-absorption deficit signalled this quarter; the operating leverage is clean of a D&A ramp. (Caveat: no balance sheet, so PPE/CWIP movement is ND — a commissioning capex could still be pending and simply not yet capitalised.)

6. **Is Other Income concentration changing?** No. Other Income is ₹0.31 Cr (3.38% of PBT), immaterial and not masking trajectory. The distortion here is the EXCEPTIONAL line, not Other Income — strip the ₹3.70 Cr and re-read: normalised PBT ≈ ₹5.45 Cr, still +4.2x YoY.

---

## STEP 3 — SEQUENTIAL QoQ TRAJECTORY

Only three quarters are present in this filing (Q1 FY26, Q4 FY26, Q1 FY27). **Q2 FY26 and Q3 FY26 are not in this extract → ND** (not estimated). A full 4-6 quarter run-rate cannot be built from a first-pipeline-run filing; flagged as a data limitation.

| Quarter | Revenue (₹ Cr) | Op EBITDA Margin | Core PBT ex-OI (₹ Cr) | One-offs flagged | QoQ Run-Rate |
|---|---|---|---|---|---|
| Q1 FY26 (30-Jun-25) | 79.18 | 5.74% | 1.28 | None (exceptional nil) | Base |
| Q2 FY26 | ND | ND | ND | ND | ND |
| Q3 FY26 | ND | ND | ND | ND | ND |
| Q4 FY26 (31-Mar-26) | 112.16 | 9.92% | 8.54 | Exceptional CHARGE ₹3.34 Cr (nature ND) | Peak of the three |
| Q1 FY27 (30-Jun-26) | 102.86 | 7.78% | 5.14 | Exceptional GAIN ₹3.70 Cr (property sale, Note 4) | Down QoQ from Q4 |

**Diagnostics:**
- **Run-rate trajectory (of the three available prints):** Q1 FY27 revenue ₹102.86 Cr is DOWN 8.3% QoQ from Q4 FY26 ₹112.16 Cr, and operating margin compressed 214 bps QoQ (9.92% → 7.78%). Against Q1 FY26 it is sharply up. So the honest read is: **strong YoY, softer sequentially** — the Q4 peak was not sustained into Q1. Whether Q4 is seasonally strong (year-end push) is untestable without Q2/Q3 FY26.
- **One-off distortion:** Q4 FY26 carried a ₹3.34 Cr exceptional CHARGE (unexplained in this filing); Q1 FY27 carries a ₹3.70 Cr exceptional GAIN. Both quarters' reported PBT are distorted in OPPOSITE directions — comparing reported PBT QoQ is meaningless; the ex-exceptional PBT (Q4 ₹9.66 Cr → Q1 ₹5.45 Cr) is the comparable line and it fell 43.5% QoQ.
- **Implied Q2 FY27 base to hold trajectory:** to hold the YoY ~30% revenue growth, Q2 FY27 must print ≥ ~₹100-105 Cr (against an unknown Q2 FY26 base — ND). The cleaner watch is ex-exceptional operating PBT holding ≥ ₹5 Cr.

---

## STEP 4 — OPERATIONAL DECOMPOSITION (PAT bridge, Q1 FY26 → Q1 FY27)

Reported PAT change: ₹0.98 Cr → ₹6.85 Cr = **+₹5.87 Cr** (line 99: 684.55 − 97.59 = +586.96 L). Decomposed (Lakhs shown for precision; Op EBITDA change split into volume-at-prior-margin and margin effect):

| Component | YoY Change (₹ Cr) | YoY Change (₹ L) | Recurring? |
|---|---|---|---|
| Revenue/volume contribution (rev +₹23.68 Cr at prior 5.74% margin) | +1.36 | +135.83 | Recurring |
| Margin change contribution (+204 bps on Q1 FY27 revenue) | +2.10 | +209.91 | Recurring |
| Depreciation change | +0.01 | +0.81 | Recurring (post-capex) |
| Finance cost change | +0.40 | +39.67 | Recurring (post-debt) |
| Other Income change | +0.29 | +28.62 | NON-RECURRING typically (immaterial ₹0.31 Cr level) |
| Exceptional items (property sale, Note 4) | +3.70 | +369.55 | **NON-RECURRING** |
| Effective tax rate / tax change | (1.97) | (197.42) | Mixed (flat 25.17% ETR; higher absolute tax on higher PBT) |
| **Reported PAT YoY change** | **+5.87** | **+586.96** | — |

**Recurring / non-recurring split of the +₹5.87 Cr (+586.96 L) reported PAT increase (denominator = 586.96 L; components sum to ~100%):**

| Bucket | ₹ L | % of PAT increase |
|---|---|---|
| Core operating (volume +135.83 + margin +209.91 + D&A +0.81 + finance +39.67) | +386.22 | **65.8%** |
| Other Income | +28.62 | **4.9%** |
| Exceptional property-sale gain (NON-RECURRING) | +369.55 | **63.0%** |
| Tax drag | −197.42 | **−33.6%** |
| **Total** | **+586.96** | **≈100%** |

**Mandatory questions:**
- **% of YoY PAT change from recurring core vs non-recurring:** Against the correct ₹5.87 Cr (586.96 L) base, the exceptional property-sale gain is **63.0% of the reported PAT increase** — nearly two-thirds is a one-time asset sale. The recurring operating core contributes +65.8% (pre-tax), Other Income +4.9%, offset by a −33.6% tax drag. Read plainly: **~63% of the headline PAT jump is non-recurring property gain**, and the operating improvement, though genuine, is largely consumed by higher tax at the reported-PAT line.
- **If Other Income reverts to prior level:** negligible effect (−₹0.29 Cr). Other Income is not the distortion here.
- **If the exceptional gain is stripped:** normalised PAT ≈ ₹6.85 Cr − (₹3.70 Cr gain net of tax). The gain appears taxed within current tax (no separate LTCG line, F8.1); a conservative post-tax gain of ~₹2.8-3.7 Cr strips to a normalised PAT of roughly **₹3.1-4.1 Cr** (₹ range, because the tax split is undisclosed → the exact split is ND). Even at the low end, normalised PAT is ~3x Q1 FY26 — operationally real, just not ₹6.85 Cr of recurring earnings.
- **D&A / finance at steady state?** D&A flat and finance costs falling; no ramp evident. But no balance sheet → whether a commissioning-stage asset (the Notion FCAW line) is about to lift depreciation is ND.
- **Tax adjustments:** No deferred-tax entry this quarter (nil, line 96); interim tax is a flat statutory 25.17% estimate. The FY27 full-year deferred-tax true-up is deferred to a later quarter (F8.1) — H2 ETR will likely step up.

---

## STEP 5 — CASH QUALITY & BALANCE SHEET

**Data-availability rule (v1.2):** Reg 33 mandates the cash-flow statement and balance sheet only at HALF-YEAR and YEAR-END (Q2 and Q4). **This is a Q1 filing → no cash-flow statement and no interim balance sheet are present** (A3 confirms; only the annual Other Equity ₹134.76 Cr at 31-Mar-26 is disclosed, line 106). CFO, capex, working-capital, debtor/inventory/payable days, net debt and pledge are therefore **ND for the current period** and cannot be estimated.

| Metric | Prior period (FY26, where annual-only) | Current period (Q1 FY27) | Change | Verdict |
|---|---|---|---|---|
| CFO | −₹10.52 Cr (FY26, Notion MEMORY — not in this filing) | ND (no cash-flow stmt in Q1 filing) | ND | UNTESTABLE this filing |
| CFO/PAT ratio | −0.81x (FY26, Notion MEMORY) | ND | ND | UNTESTABLE — the single most informative data point, undisclosed |
| Capex (PPE + CWIP) | ND | ND | ND | No balance sheet |
| FCF (CFO − Capex) | ND | ND | ND | No balance sheet |
| Working capital change | ND | ND | ND | No balance sheet |
| Receivable days | 95 (FY26, Notion MEMORY) | ND | ND | Trigger #3 (<85) UNTESTABLE |
| Inventory days | ND | ND | ND | No balance sheet |
| Payable days | ND | ND | ND | No balance sheet |
| Cash Conversion Cycle | ND | ND | ND | No balance sheet |
| PPE | ND | ND | ND | No balance sheet |
| CWIP | ND | ND | ND | No balance sheet |
| Net Debt / (Net Cash) | ND | ND | ND | No balance sheet |
| Promoter Pledge | 43.36% (Mar-2026, Notion MEMORY) | ND | ND | Not disclosed in results filing; resolves only in FY26 AR (F13.1) |

**Mandatory questions:**
- **Is CFO/PAT meeting the Pillar 2 cash multiplier assumption?** UNTESTABLE. The FY26 baseline (CFO/PAT −0.81x, CFO −₹10.52 Cr) is DETERIORATING and asset-sale-driven per Notion. This quarter's operational CFO — the Notion CRITICAL Trigger #1 and "the single most informative data point for this filing" — **cannot be settled from this document.** The ₹3.70 Cr property-sale proceeds are exactly the kind of asset-sale cash that masks operational CFO, and there is no statement to strip them from.
- **WC drag structural or growth-induced?** Cannot re-test (no balance sheet). Notion carries debtor days 84→95 (deteriorating) and CARE's structural WC assessment; nothing this filing overturns it.
- **CWIP capitalisation:** ND. Depreciation flat suggests no major commissioning yet capitalised, but PPE/CWIP not disclosed.
- **Net debt movement:** ND. Finance costs fell 17.7% YoY (₹2.24 → ₹1.85 Cr), weakly consistent with lower average borrowings, but the balance-sheet net-debt figure is not disclosed.

**Cash-conversion classification: INDETERMINATE.** Per CLAUDE.md house rule, INDETERMINATE cash conversion must NOT silently resolve to PROCEED — it caps the protocol verdict at **PROCEED WITH CAVEATS with the missing evidence named**: the missing evidence is the **Q1 FY27 (and the mandatory Q2/H1) operational cash-flow statement excluding asset-sale proceeds**.

---

## STEP 6 — RECONCILIATION VS THESIS

### 6A. Variance vs Notion Projections

The Notion snapshot (13 Jun 2026) carries FY29 SOTP price targets (Bear ₹52-57 / Base ₹90-102 / Bull ₹162-191) and a qualitative "revenue STAGNANT ~₹369 Cr / margin ~9% vs 13% target" baseline, but **no quarterly numeric Bear/Base/Bull operating projections for FY27** → those projection cells are ND (not estimated), with the FY26 stagnation baseline used as the reference.

| Metric | Bear Proj | Base Proj | Bull Proj | Actual (Q1 FY27 / annualised) | Lands In |
|---|---|---|---|---|---|
| Revenue | ND | ~₹369 Cr FY (stagnant) | ND | ₹102.86 Cr Q1 (₹411 Cr annualised, +11.5% vs FY26) | Above the stagnation baseline on one print; unconfirmed as trend |
| EBITDA Margin | ND | ~9% | 13% (FY29 target) | 7.78% Q1 operating | Below FY26 9.05%; below base ~9% |
| PAT | ND | ND | ND | ₹6.85 Cr reported / ~₹3.1-4.1 Cr normalised | ND baseline; normalised ~3x YoY |
| EPS | ND | ND | ND | ₹1.32 reported / ~₹0.6-0.8 normalised | ND baseline |
| Net Debt | ND | ND | ND | ND (no balance sheet) | UNTESTABLE |
| ROCE | ND | ND | ND | ND (no capital-employed disclosure) | UNTESTABLE |

Probability re-weighting rule (v1.2): it requires actuals BELOW BEAR on 2+ metrics for 2 CONSECUTIVE quarters. This is the FIRST pipeline run (no prior quarter under protocol) and revenue is ABOVE the stagnation baseline, so **the re-weighting rule does not trigger.** State the state: not applicable this cycle.

### 6B. Watchlist Item Status (12-trigger monitoring checklist reconciled against THIS filing)

| # | Watchlist Item | Green Threshold | Red Threshold | This-Quarter Reading | Status |
|---|---|---|---|---|---|
| 1 | Q1 FY27 operational CFO ex-asset-sales (CRITICAL) | Positive | Negative/undisclosed | No cash-flow statement in Q1 filing (line 106 only annual) | **UNKNOWN — untestable; per re-engagement rule, undisclosed → AVOID extends** |
| 2 | Q1 FY27 revenue | ≥₹95 Cr | <₹70 Cr | ₹102.86 Cr (line 73) | **GREEN — fired favourably** |
| 3 | Q1 FY27 debtor days | <85 | ≥95 | ND (no balance sheet) | UNKNOWN |
| 4 | Mgmt WC plan in Q1 concall | Named initiative + timeline | Silence | No concall this cycle | UNKNOWN |
| 5 | FCAW line commissioning first revenue | ≥₹5 Cr in Q2 FY27 | No revenue | Q2 not yet reported; single segment, no line-level split (Note 3) | UNKNOWN (pending Q2) |
| 6 | FY26 AR pledge explanation | Specific reason + reduction timeline | Unexplained | FY26 Board's/Corp Gov Report approved 06-Aug (agenda 2), AR not yet published | PENDING (resolves in imminent AR — F13.1) |
| 7 | FY26 AR auditor opinion | Unmodified, no EoM | Modified/EoM | This Q1 LRR unmodified (line 188); FY26 statutory opinion is a separate AR event | PARTIAL GREEN on interim; FY26 AR PENDING |
| 8 | First Thane cash receipt + deployment | ≥₹40 Cr to debt reduction | None | ND (Q3 FY27 window; not in this filing) | UNKNOWN |
| 9 | NPCIL first order disclosure | Material order ≥₹5 Cr | None | ND (no order disclosure; single segment) | UNKNOWN |
| 10 | Receivables factoring facility | Sanctioned facility | None | ND | UNKNOWN |
| 11 | Fenkin9 (Fen-Kin Buildpro) RERA completion | >50% + improving sales | Stall | ND | UNKNOWN |
| 12 | Absence-of-catalyst test | WC discussed in Q2 concall | No WC discussion | Q2 concall not yet (Nov 2026) | UNKNOWN (pending) |

### 6C. Thesis-Broken / File-Closure Trigger Check

| File-Closure Condition | Threshold | Current Reading | FIRED? |
|---|---|---|---|
| #1 Pledge crosses 50% OR unexplained in FY26 AR | ≥50% or unexplained | Pledge not in this filing; FY26 AR imminent, unresolved | NOT FIRED (unresolved — pending AR) |
| #2 Another auditor change or modified opinion on FY26 AR | Change/modified | SAPD unchanged; Q1 LRR unmodified (line 188, 190) | **NOT FIRED** |
| #3 M&A announcement before Q1 FY28 validates ops | Any M&A | None in this filing | **NOT FIRED** |
| #4 Fen-Kin Infinity LLP defaults on JDA | Default | ND (not in filing) | NOT FIRED (no evidence) |
| #5 Q1 FY27 revenue below ₹70 Cr | <₹70 Cr | ₹102.86 Cr (line 73) | **NOT FIRED (clears comfortably)** |
| #6 FY27 H1 operational CFO (ex-asset-sales) still negative | Negative at H1 | UNTESTABLE at Q1; H1 cash-flow available only at Q2 | PENDING (Q2 FY27 decides) |

**No file-closure trigger has fired.** Two remain unresolved and PENDING (pledge/AR #1; H1 CFO #6), one is untestable this quarter (#1 monitoring CFO). Since the decisive Trigger #1 (operational CFO positive ex-asset-sales) is UNDISCLOSED, the re-engagement condition ("3+ triggers AND specifically #1 fires") **cannot be satisfied on this filing → AVOID extends.**

### 6D. Growth Trigger Status

| Trigger | Original Confidence | Confirming Evidence | Killing Evidence | Updated Status |
|---|---|---|---|---|
| Revenue recovery (≥₹95 Cr) | Watch | Q1 FY27 ₹102.86 Cr, +29.9% YoY (line 73) | QoQ down 8.3% from Q4 peak; single print | **ON TRACK (1 trigger fired favourably)** |
| Operational cash conversion turning positive | Absent (FTTCP AVOID) | None — no cash-flow statement | Undisclosed = AVOID extends | **UNRESOLVED (untestable)** |
| Margin toward 13% | Weak | Op margin +204 bps YoY to 7.78% | Still below FY26 9.05% and 13% target; QoQ compressed | WEAKENED-to-ON TRACK (partial) |
| Pledge reduction / governance clean-up | Concern | None in filing | Unresolved; resolves in FY26 AR | DELAYED (pending AR) |
| Warrant conversion / capital clarity | Concern | Warrants unconverted at 30-Jun-26 (F10.1) | ~9.8% dilution overhang still live | ON TRACK as overhang, not resolved |

**Net:** exactly ONE trigger (revenue) fired favourably; the decisive cash trigger is untestable; governance triggers pending the AR. **Fewer than 3 triggers fired, and Trigger #1 did not fire → the ZERO-position rule stands.**

---

## STEP 7 — FOUR-PILLAR DESTINATION PE RE-VALIDATION

No pillar input can be MECHANICALLY recomputed from a Q1 interim filing: ROCE requires capital employed (no balance sheet); the cash multiplier requires CFO (no cash-flow statement); the Strategic/EM premiums require the AR and concall (both absent). Therefore **all pillars are HELD at Notion values pending the FY26 AR and Q2 H1 cash flow.** No destination-PE recompute is triggered this cycle. Recorded, not skipped.

| Pillar / Input | Original Assumption | Current Reading (Q1 FY27) | Action |
|---|---|---|---|
| ROCE Base (0.5×ROCE+7.5, floor 9x cap 24x) | Notion RRM 7.3x / Additive 11.8x destination | ROCE ND (no capital-employed disclosure) | HOLD — FTTCP verdict remains AVOID; no re-run possible this filing |
| Cash Multiplier | Low (cash DETERIORATING, −0.81x FY26) | CFO ND (no statement) | HOLD — cannot revise up on undisclosed CFO; INDETERMINATE |
| Growth Visibility Premium | Modest (EM 30) | Revenue +29.9% is one favourable data point | HOLD pending trend confirmation |
| Strategic Premium | Low | No moat evidence in filing; single segment | HOLD |
| UA Multiplier | Per Notion (not evidenced as applied) | No change in qualifiers this filing | HOLD |
| Sector Cap | Per sector | No reclassification (welding consumables) | HOLD |
| Hurdle Ratio recheck | Expected CAGR ~3.4% at CMP ₹83 vs 25% hurdle → fails | Cannot recompute (no updated EPS CAGR basis; normalised EPS uncertain, CMP ND) | HOLD — remains a STOP on the ₹83 basis; not investable |

Destination PE UNCHANGED (7.3x RRM / 11.8x Additive). No revised fair values this cycle. Entry zone ₹46-52 (DA ₹40-45) and MoS ₹37-42 (DA ₹32-36) UNCHANGED — no numeric basis in a single distorted print to move them.

---

## STEP 8 — POSITION DECISION (branch 8A-W, non-held / WATCHLIST-AVOID)

**Decision Status verified: WATCHLIST / AVOID (Notion, 13 Jun 2026). Position not held → 8A-W branch (not 8A). No trim/exit mechanics apply.**

Walk the 8A-W logic:
- **Has any thesis-broken (file-closure) condition FIRED?** No (Step 6C). So no reclassification to permanent-AVOID-close on this filing.
- **Did actuals land BELOW BEAR on 2+ metrics?** No — revenue is above the stagnation baseline; margin expanded YoY. Not below bear.
- **Did actuals land BETWEEN BEAR and BASE?** Mixed: revenue above base baseline (one print), operating margin (7.78%) below base (~9%). The decisive cash metric is UNDISCLOSED.
- **Did actuals land AT or ABOVE BASE with a pre-committed BUY gate met?** The pre-committed BUY gate requires **3+ triggers AND Trigger #1 (operational CFO ex-asset-sales) positive.** Only 1 trigger (revenue) fired; Trigger #1 is untestable. **The BUY gate is NOT met.**

**8A-W output:**
- **Decision Status: UNCHANGED — WATCHLIST / AVOID.** Position: **ZERO at any price** (rule intact; <3 triggers, Trigger #1 unresolved).
- **Master decision gate pushed one quarter out, stated explicitly: Q2 FY27 results (Nov 2026)** — because Reg 33 mandates the H1 cash-flow statement at Q2, which is the ONLY venue that can settle the decisive Trigger #1 / closure #6 (operational CFO ex-asset-sales). This filing could not, by construction.
- **Entry zone / MoS: UNCHANGED** (₹46-52 / ₹37-42; DA ₹40-45 / ₹32-36). No numeric basis to revise on one distorted print.
- **Protocol verdict caps at PROCEED WITH CAVEATS** — cash conversion INDETERMINATE (no cash-flow statement); missing evidence named = operational CFO ex the ₹3.70 Cr property-sale proceeds. AVOID extends through the untested-CFO window.

**8B. Add-back / trim trigger refinement:** No held position → no trim ladder. Re-entry gate refined only in specificity: the prior "3+ triggers incl. #1" gate now explicitly reads "**H1 FY27 operational CFO (ex-asset-sales) positive at Q2**" as the concrete, near-term instance of Trigger #1, plus a clean, unmodified, pledge-explained FY26 AR (triggers #6/#7). Nothing on this filing loosens the gate.

**8C. Single cleanest metric for next quarter (Q2 FY27):** **H1 FY27 operational cash flow from operations, EXCLUDING asset-sale proceeds** (the Reg 33 half-yearly cash-flow statement, mandatory at Q2). 
- **Bull threshold:** H1 operational CFO positive after stripping the ₹3.70 Cr property proceeds (and any further asset sales) → cash catalyst forming → re-run FTTCP.
- **Bear threshold:** H1 operational CFO still negative → **file-closure Trigger #6 FIRES → AVOID confirmed for the full FY27 cycle.**

---

## STEP 8.5 — QUESTIONS FOR MANAGEMENT

Channel: GEE hosts no concall this cycle (none supplied; SME-style disclosure). **Channel recommendation: formal IR email now, and table these at the 65th AGM Q&A (07-Sep-2026).** Every A3 FORWARD-SIGNAL (F10.1, F13.1) and AMBIGUOUS (F1.1, F14.1) finding generates at least one question (mapping shown in the "From" column).

| # | Question | From finding | Why It Matters | Bull Answer | Bear Answer |
|---|---|---|---|---|---|
| 1 | For Q1 FY27, what was cash flow from operations EXCLUDING the ₹3.70 Cr proceeds from the two property sales — a specific rupee figure? | **F1.1 (AMBIGUOUS)** | The decisive Notion Trigger #1; the filing carries no cash-flow statement, so operational cash quality is entirely undisclosed. | A positive operational CFO figure with debtor-days evidence | Refusal, "we'll share at half-year", or a negative number |
| 2 | Which two immovable properties were sold in Q1 FY27, to whom, and is either connected to the Thane JDA with Fen-Kin Infinity LLP or to any related party? | **F1.1 (AMBIGUOUS)** | ₹3.70 Cr = 40.4% of PBT and 63.0% of the YoY PAT increase; RPT history (Sec 185/186 flagged) makes counterparty identity material. | Arm's-length third-party sale, unrelated to JDA | Related-party buyer or JDA-linked → governance red flag |
| 3 | The typed director-signature date on the results reads 06-Jul-2026, but the digital certificate and board meeting are 06-Aug-2026 — which is correct, and what is the sign-off control that let a July date onto an August filing? | **F14.1 (AMBIGUOUS)** | Backdating cannot be excluded on face; drafting-control quality is a governance tell for a CONCERN-rated promoter. | Clear copy-paste explanation + tightened control | Evasion or inability to explain → control weakness |
| 4 | The 51 lakh promoter warrants at ₹80 remain unconverted at 30-Jun-26. What is the exact conversion schedule, and will the ₹40.80 Cr proceeds go to debt reduction or working capital? | **F10.1 (FORWARD-SIGNAL)** | ~9.8% dilution overhang is live; use of proceeds bears on the cash thesis and on promoter alignment. | Committed date + debt-reduction use | Vague timeline, or WC top-up (masks operational cash gap) |
| 5 | When will the FY26 Annual Report and Corporate Governance Report (approved at this board meeting) be published, and will they carry a specific explanation and reduction timeline for the 43.36% promoter pledge? | **F13.1 (FORWARD-SIGNAL)** | The AR is where closure triggers #1 (pledge) and #2 (FY26 audit opinion) resolve; AR approval was booked at this meeting. | Firm publication date + pledge-reduction plan | Delay or "no change to disclose" → closure trigger #1 risk |
| 6 | The FY26/Q4 accounts carry a ₹3.34 Cr exceptional CHARGE that this filing does not explain. What was it, and is any part recurring? | F1.1 context (Step 1) | An unexplained prior charge sits opposite this quarter's gain; both distort the PBT trajectory. | One-time, non-recurring, fully explained | Recurring or unexplained → normalised-earnings doubt |
| 7 | Q1 FY27 revenue (₹102.86 Cr) is up 30% YoY but down 8.3% QoQ from Q4's ₹112.16 Cr. Is Q4 seasonally elevated, and what is the Q2 FY27 revenue run-rate you expect to hold? | Step 3 (QoQ) | Tests whether the YoY strength is a trend or a base effect; no Q2/Q3 FY26 data to judge seasonality. | Specific Q2 run-rate ≥ ₹100 Cr with order visibility | Refusal to guide, or admission Q4 was a one-off push |

**Top 3 ranked by likelihood of producing thesis-changing information:**
1. **Q1 (from F1.1)** — a positive operational CFO ex-asset-sales would begin forming the cash catalyst and could move the position off AVOID; a negative/withheld answer confirms the bear case and extends AVOID.
2. **Q5 (from F13.1)** — the FY26 AR pledge + opinion resolution directly governs two file-closure triggers; a clean AR is the largest single de-risking event available.
3. **Q3 (from F14.1)** — the date inconsistency is the cleanest live test of management transparency/governance controls; an evasive answer is itself diagnostic for a CONCERN-rated promoter.

---

## MONITORABLES / CATALYST LIST (seeded by A3 Commitment Register F6 + Board-Outcome forward items F13)

| Item | Implied Date | Source ref |
|---|---|---|
| 65th Annual General Meeting held (voteable resolutions; AGM Q&A channel for questions above) | 2026-09-07 | agenda 3, line 38 (F6.1) |
| Register of Members / Share Transfer books closed for AGM | 2026-09-01 to 2026-09-07 | agenda 4, lines 40-43 (F6.1) |
| FY26 full Annual Report + Corporate Governance Report published (resolves pledge trigger #6 and auditor-opinion trigger #7 → schedule Role 6 AR Deep Dive) | 2026-08-06 + weeks (pre-AGM) | agenda 2, lines 36-37 (F13.1) |
| Scrutinizer (Deep Shukla) oversees AGM e-voting | 2026-09-07 | agenda 5, lines 44-46 (F6.1) |
| Q1 results uploaded to company website + BSE | on/after 2026-08-06 | Note 6, line 126 (F6.1) |
| **Q2 FY27 results with mandatory Reg 33 H1 cash-flow statement — the decisive Trigger #1 / closure #6 venue** | Nov 2026 | v1.2 Step 5 rule + Notion trigger #1/#6 |
| FCAW line commissioning first revenue ≥₹5 Cr (monitoring #5) | Q2 FY27 (Sep-Oct 2026) | Notion checklist #5 |
| First Thane cash receipt ≥₹40 Cr to debt reduction (monitoring #8) | Q3 FY27 | Notion checklist #8 |
| 51 lakh promoter warrants (₹80) conversion window close | within 18-mo window from issue | F10.1; Notion governance flag |
| NPCIL first material order ≥₹5 Cr (monitoring #9) | Q2-Q3 FY27 | Notion checklist #9 |

---

## MANDATORY PLAIN-LANGUAGE BRIEF (four parts; final narrative section before the YAML)

Provenance key: **[FILING]** = this Q1 FY27 filing at a line anchor; **[NOTION]** = prior Notion/peer/DA work (memory to weigh); **[ND]** = not disclosed anywhere available this cycle.

### 1. SUMMARY NARRATIVE

GEE Limited reported Q1 FY27 revenue of ₹102.86 Cr **[FILING line 73]**, up 29.9% from ₹79.18 Cr a year earlier. Reported profit after tax jumped to ₹6.85 Cr **[FILING line 99]** from ₹0.98 Cr, and headline EPS rose to ₹1.32 **[FILING line 109]** from ₹0.19. That headline is mostly a one-off. The company sold two properties and booked a ₹3.70 Cr exceptional gain **[FILING Note 4, lines 122-123]**, and that gain alone is about 63% of the ₹5.87 Cr rise in profit and 40% of pre-tax profit. Strip it out and profit before tax is still about ₹5.45 Cr **[FILING line 88]**, roughly four times last year, so the underlying operations did genuinely improve: operating margin widened 204 basis points to 7.78% and finance costs fell 18%. But sequentially the quarter is softer than it looks, with revenue down 8.3% from the December-quarter peak of ₹112.16 Cr **[FILING line 73]** and operating margin down 214 basis points.

The one number that would have settled the investment question is missing. GEE's thesis is on AVOID because its cash generation has been deteriorating (FY26 operating cash flow was negative ₹10.52 Cr **[NOTION]**), and the single agreed test for this filing was Q1 operating cash flow excluding asset sales. A first-quarter Indian filing carries no cash-flow statement, and this one does not either **[FILING — only annual Other Equity at line 106]**. So the decisive test cannot be answered here. Governance items also stay open: the 43.36% promoter pledge **[NOTION]** is not addressed in a results filing and resolves only in the annual report, which the board just approved and which is due within weeks **[FILING agenda 2, lines 36-37]**. The 51 lakh promoter warrants at ₹80 remain unconverted **[FILING line 103 — paid-up flat QoQ]**, leaving a roughly 10% dilution overhang. One drafting oddity is worth an answer: the director's typed sign-off date reads 06-Jul-2026 while the certificate and board meeting are 06-Aug-2026 **[FILING line 140]**.

For the decision: the auditor's opinion is clean and unmodified **[FILING line 188]**, the auditor is unchanged, and revenue cleared the ₹95 Cr monitoring mark and is nowhere near the ₹70 Cr close-the-file mark. No file-closure trigger fired. But only one of the required triggers fired, the profit jump is nearly two-thirds a one-time property sale, and the decisive cash trigger could not be tested, so the re-entry gate is not met. Decision Status stays **WATCHLIST / AVOID**, position stays **ZERO**, and the real test moves to the Q2 FY27 results in November, when the half-yearly cash-flow statement is legally required.

### 2. SECTOR INTELLIGENCE

GEE is a welding-consumables manufacturer operating in a **single reportable segment** **[FILING Note 3, lines 119-120]** — a mature, cyclical Indian industrial-consumables niche geared to capex, infrastructure, fabrication and construction activity. The prior work frames the demand backdrop as one with **no evident pricing power and a 6-7% retail discount pressure**, with a structurally stagnant revenue base (~₹369 Cr across FY24-FY26) **[NOTION]**. This quarter's 30% YoY revenue lift **[FILING line 73]** is the first data point that pushes against the "stagnant" label, but it is one print against an unknown seasonal base — Q2 and Q3 FY26 are **[ND]** in this filing, so the sector-demand read cannot yet be called a cycle turn. Raw-material cost is the swing factor for this sector: cost of raw materials consumed is ₹66.50 Cr, still 64.7% of revenue **[FILING lines 78, 73]**, so input prices dominate margin, and the modest margin expansion this quarter came without any disclosed pricing action. Regulation/payer-mix is not a factor here (industrial B2B, not a regulated or payer-driven sector), so the sector risk to watch is straightforward demand cyclicality plus commodity input swings, neither disprovable from a one-quarter print.

### 3. BUSINESS-MODEL INTELLIGENCE

The model is a straightforward make-and-sell manufacturer with a growing trading overlay. Two structural signals stand out this quarter. First, **purchase of stock-in-trade jumped to ₹13.61 Cr from ₹0.06 Cr a year earlier** **[FILING line 79]** — GEE is now buying finished goods to resell alongside what it manufactures, a mix shift toward trading that typically carries thinner margins and can flatter revenue without adding much profit. That partly explains why revenue grew 30% while operating margin, though up YoY, remains modest at 7.78% and below the FY26 full-year 9.05% **[FILING derived]**. Second, and more important for the thesis, **the reported profit leans on a property sale, not on operations** **[FILING Note 4]** — roughly 63% of the profit increase is that one-time gain. This matters because the whole GEE question is whether the business converts profit into cash: FY26 converted profit into *negative* cash (CFO/PAT −0.81x) **[NOTION]**, and a company that plugs cash by selling real estate is exhibiting exactly the model weakness the thesis flags. Unit economics that would confirm or deny model drift — debtor days, inventory days, working-capital intensity — are **[ND]** this quarter (no balance sheet). Depreciation is flat and finance costs fell **[FILING lines 84, 83]**, so there is no sign yet of a heavy new-capex absorption drag, but no capacity or utilisation figure is disclosed **[ND]**. Net read: operations improved, but the model has drifted toward trading and continues to rely on asset sales for cash — unresolved until the H1 cash-flow statement.

### 4. COMPETITION INTELLIGENCE

No peer is named in this filing **[ND]**, and no concall or presentation was supplied, so competitive positioning rests on prior work **[NOTION]**: GEE scores EM 30 (Modest), Gate 0 33/160 (AVOID with three deal-breakers), promoter CONCERN, and is judged to have **no pricing power** in a segment where it faces retail discounting of 6-7%. Where GEE could "win" is the operating improvement visible this quarter — 30% revenue growth and +204 bps margin **[FILING]** — if it proves durable and if the pending FCAW-line and NPCIL-order catalysts **[NOTION checklist #5, #9]** convert; those would be genuine competitive gains rather than accounting ones. Where GEE is structurally weaker than better-run industrial-consumables peers is the combination that the numbers keep pointing to: reliance on asset sales for cash, a 43.36% promoter pledge, two auditor exits in 18 months **[NOTION]**, and a ~10% warrant dilution overhang **[FILING line 103; NOTION]** — a governance and balance-sheet profile that a cleaner competitor would not carry into a capex cycle. The competitive risk to watch is that the operating uptick is being partly manufactured by a trading-mix shift and monetised through property sales, so a peer with real pricing power and clean cash conversion would out-earn GEE through the same demand cycle. The FY26 Annual Report **[FILING agenda 2]** and the Q2 H1 cash flow are the two documents that will show whether the competitive gap is narrowing or just being papered over.

---

```yaml
stage: A4-analyst
company: "GEE"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
docs_merged: [results]
ledger_reconciliation:
  notes: 6
  turns: 0
  slides: 0
  all_reviewed: true
  a3_findings_incorporated: ["F1.1", "F6.1", "F8.1", "F9.1", "F10.1", "F13.1", "F14.1"]
protocol_verdict: "PROCEED WITH CAVEATS"
cash_conversion: "INDETERMINATE"
decision_status_verified: "WATCHLIST / AVOID"
position_branch: "8A-W"
sc_gap_pat_pct: ["N.A. — standalone-only filing, no consolidated statement exists this cycle (all periods)"]
pat_bridge_yoy_total_cr: 5.87            # 684.55 − 97.59 = 586.96 L = ₹5.87 Cr (corrected from 6.87; A5 arithmetic loop-back)
pat_bridge_split_pct:                    # against 586.96 L denominator, sums ≈100%
  core_operating: 65.8
  other_income: 4.9
  exceptional_property_sale: 63.0
  tax_drag: -33.6
questions_for_management:
  - {q: "Q1 FY27 operational CFO EXCLUDING the ₹3.70 Cr property-sale proceeds — specific figure?", from_finding_id: "F1.1"}
  - {q: "Which two immovable properties were sold, to whom, and any Thane-JDA / related-party connection?", from_finding_id: "F1.1"}
  - {q: "Director typed date 06-Jul-2026 vs cert/board 06-Aug-2026 — which is correct and what sign-off control failed?", from_finding_id: "F14.1"}
  - {q: "51 lakh promoter warrants at ₹80 unconverted — exact conversion schedule and use of ₹40.80 Cr proceeds?", from_finding_id: "F10.1"}
  - {q: "FY26 AR / Corp Gov Report publication date, and will it explain the 43.36% pledge with a reduction timeline?", from_finding_id: "F13.1"}
  - {q: "Unexplained ₹3.34 Cr FY26/Q4 exceptional CHARGE — what was it and is any part recurring?", from_finding_id: "F1.1"}
  - {q: "Revenue +30% YoY but −8.3% QoQ — is Q4 seasonally elevated and what Q2 FY27 run-rate holds?", from_finding_id: "Step3-QoQ"}
monitorables:
  - {item: "65th AGM held (AGM Q&A channel)", implied_date: "2026-09-07", source_ref: "agenda 3, line 38 (F6.1)"}
  - {item: "Book closure for AGM", implied_date: "2026-09-01/2026-09-07", source_ref: "agenda 4, lines 40-43 (F6.1)"}
  - {item: "FY26 Annual Report + Corp Gov Report published -> Role 6 AR Deep Dive (resolves pledge #6 + auditor #7)", implied_date: "2026-08-06+weeks", source_ref: "agenda 2, lines 36-37 (F13.1)"}
  - {item: "Scrutinizer oversees AGM e-voting", implied_date: "2026-09-07", source_ref: "agenda 5, lines 44-46 (F6.1)"}
  - {item: "Q1 results uploaded to website + BSE", implied_date: "2026-08-06", source_ref: "Note 6, line 126 (F6.1)"}
  - {item: "Q2 FY27 results with mandatory H1 cash-flow statement — decisive Trigger #1 / closure #6 venue", implied_date: "2026-11", source_ref: "v1.2 Step 5 + Notion trigger #1/#6"}
  - {item: "FCAW line first revenue >=₹5 Cr", implied_date: "2026-09/2026-10", source_ref: "Notion checklist #5"}
  - {item: "First Thane cash receipt >=₹40 Cr to debt", implied_date: "Q3 FY27", source_ref: "Notion checklist #8"}
  - {item: "51 lakh promoter warrants conversion window", implied_date: "within 18-mo window", source_ref: "F10.1; Notion"}
  - {item: "NPCIL first material order >=₹5 Cr", implied_date: "Q2-Q3 FY27", source_ref: "Notion checklist #9"}
flags:
  - "Cash conversion INDETERMINATE — no cash-flow statement in Q1 filing; the decisive Trigger #1 (operational CFO ex-asset-sales) CANNOT be settled from this document."
  - "~63% of the +₹5.87 Cr YoY PAT increase is a non-recurring ₹3.70 Cr property-sale gain (Note 4, lines 122-123); = 40.4% of PBT-after-exceptional."
  - "Unexplained ₹3.34 Cr FY26/Q4 exceptional CHARGE (opposite sign to Q1 gain) not described in this filing."
  - "51 lakh promoter warrants at ₹80 unconverted at 30-Jun-26 -> ~9.8% dilution overhang live (F10.1)."
  - "43.36% promoter pledge NOT addressed in results filing; resolves only in imminent FY26 AR (F13.1) — closure trigger #1 unresolved."
  - "DATE_INCONSISTENCY: director typed date 06-Jul-2026 vs cert/board 06-Aug-2026 (F14.1) — governance/drafting-control tell; backdating not excludable on face."
  - "Trading-mix drift: purchase of stock-in-trade ₹13.61 Cr vs ₹0.06 Cr YoY (line 79)."
  - "Role 5 N.A. — no concall/transcript supplied this cycle."
  - "SCOPE_LIMITATION: FY26 Board's/Corp Gov Report + director term-dates not captured upstream — UNREVIEWED, carry to Role 6 AR Deep Dive."
plain_language_brief_included: true
review_path: "/home/user/inflection-pipeline/runs/gee-q1fy27/work/review_gee_q1fy27.md"
```
