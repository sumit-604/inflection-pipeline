# Q1 FY27 COMPLETE QUARTERLY REVIEW (v2 — CONCALL MERGED) — C.E. Info Systems Ltd / MapmyIndia (MAPMYINDIA)

Agent: A4 ANALYST | Protocols: Role 4 (Quarterly Results Review v1.2) FULL + **Role 5 (Concall Analysis v1.1) NOW RUN IN FULL**
Quarter: Q1 FY27 (quarter ended 30 June 2026) | Results filing date: 4 August 2026 | Concall: Q1 FY27 earnings call, host Arhant Capital Markets
Model: claude-opus-4-8 | Framing Decision Status (verified from passed Notion): **WATCHLIST / AVOID** (operator-confirmed 2026-07-19)
Unit rule: results filing in Rupees Lakhs (x0.01 = Rs Cr); presentation, press release and concall already in Rs Cr (one exception — the "80 lakhs" net write-off figure, Lakhs x0.01 = Rs0.80 Cr). All figures in Rs Cr unless stated. Anchors: "line" = A1 extract line; "T##/L##" = concall turn / source transcript line.

---

## v2 CHANGE LOG — WHAT THIS VERSION ADDS OVER v1

v1 (`review_mapmyindia_q1fy27.md`) marked **Role 5 N.A.** because no concall transcript had been supplied. A verified Q1 FY27 concall transcript is now available (86 turns / 33 questions / 46 management numbers). **v2 supersedes Section B of v1 in full** and revises the cash/falsifier disposition, the Questions-for-Management table, the combined verdict and the plain-language brief. The Section A results tables (Steps 0–3, 5-SC, 6, 7) are carried forward from v1 unchanged; where the concall forces an analytical revision, it is stated explicitly and flagged **[v2 CORRECTION]**.

**The single most important change:** the concall discloses the *geometry* of the Rs4 Cr government write-off. Roughly **half** of the 574 bps YoY operating-margin compression, and the entire reported **−2.9%** decline in core operating PBT, are driven by this **one-time** item. On an ex-one-time (underlying) basis, operating EBITDA is **+7.6% YoY** (margin ~43%, management's "43 plus"), and core operating PBT is **+5.4% YoY, not −2.9%**. v1's headline "core operating PBT declined / PAT is treasury-financed" is therefore **corrected on the underlying basis** while the *reported* numbers (which still show the compression, and which include a realized collection failure) are retained as the conservative anchor.

**What did NOT change:** the binding FLAG-CASH falsifier is still unresolved (management confirmed "Q1 we've not given the balance sheet", T33/L78) → cash conversion **INDETERMINATE**, verdict capped at **PROCEED WITH CAVEATS**; the full-year margin guide is **35% plus** (below the 40.2% reported and ~43% underlying); the FY28 Rs1,000 Cr target went **silent**. Decision Status unchanged: **WATCHLIST / AVOID**, entry zone unchanged, master gate remains the Q2 FY27 half-year balance sheet. Net thesis: **MAINTAINED — slightly better on operations, unchanged on the two overhangs (cash quality and promoter/family control).**

Newly reframed: the receivables root cause moves **from Gtropy (v1/Notion assumption) to GOVERNMENT receivables** (T33-34/L78-80, T29/L70) — a mild-adverse confirmation of the collection concern.

---

## LEDGER-RECONCILIATION PREAMBLE (contractual, stated before Step 1)

Four documents are merged this run. Every ledger row was reviewed before interpretation.

- **Results ledger** (`ledger_results_...`): 12 notes, 77 line_items, 0 zero_standing, 2 agenda_items, 11 auditor_paras, 6 entities, 7 signature_blocks, 5 annexure_rows, 0 turns, 0 slides. **All reviewed.**
- **Presentation ledger** (`ledger_presentation_...`): 4 notes, 30 line_items, 3 zero_standing, 17 slides, 60 chart_data_labels, 32 narrative_numbers, 7 toc_items, 4 governance_items, 0 turns. **All reviewed.**
- **Press-release ledger** (`ledger_pressrelease_...`): 7 line_items, 29 operational_metrics, 5 quote_paragraphs, 21 structural_units, 0 turns, 0 slides. **All reviewed.**
- **Concall ledger** (`ledger_concall_...`): **86 turns / 33 questions / 46 management numbers**, plus 13 participants and 11 forward/hedge phrase rows. GATE A2 = pass (grep=sweep on all three gated categories). **All 86 turns / 33 questions / 46 numbers reviewed** verbatim at their source line before judging.

**Findings incorporated (all A3 finding IDs, four files):**
Results — F2-1, F2-2, F3-1, F8-1, F8-2, F12-1, F13-1, F14-1, F15-1, BF.
Presentation — MMI-01…MMI-12.
Press release — F16-1, F16-2, F16-3, F6-1(PR), F13-1(PR), F14-1(PR).
**Concall — A3-01, A3-02, A3-03, A3-04, A3-05, A3-06, A3-07, A3-08, A3-09, A3-10, A3-11, A3-12, A3-13, A3-14, A3-15, A3-16, A3-17, A3-18, A3-19, A3-20, A3-21, A3-22.**

No ledger row is unreviewed. Proceeding.

---

# SECTION A — RESULTS REVIEW (Role 4) — carried from v1, with [v2 CORRECTION] inserts

## STEP 0 — PRE-FLIGHT

**0A. Notion baseline (memory to weigh, not filing evidence).** Decision Status **WATCHLIST / AVOID**, verified before any framing → non-held name → **Step 8A-W branch**. CMP ~Rs1,185; Entry Price Max Rs700 (base Rs690–700); MoS Rs555; destination PE 32x (operator ruling); current trailing PE ~47x; sector cap 45x; prob-weighted 3yr CAGR ~4–5% at CMP; Hurdle Ratio STOP. Gate 0 94/160; EM 30/100. FLAG-PROMOTER CONCERN (Rohan Verma Joint MD from 2026-07-01) and FLAG-CASH INDETERMINATE are live.

**0B. Unit convention.** Results filing "Rupees in lakhs" (lines 220, 425); x0.01 = Rs Cr. Deck (line 271) and press release (line 102) in Rs Cr; reconcile at x1. Concall figures spoken in crores (x1); sole exception "80 lakhs" (x0.01 = Rs0.80 Cr).

**0C. Share-count changes.** Paid-up equity flat QoQ at 1,095 lakhs (5.475 Cr shares), +7 lakhs YoY via ESOP (A3 F10). No split/bonus/rights/QIP/buyback. **EPS share-adjusted = EPS reported.**

**0D. Numbered-notes extraction** (unchanged from v1):

| Note # | Doc/loc | Subject | What it says | Rs Cr impact | Period | Comparability impact |
|---|---|---|---|---|---|---|
| Consol N1 | line 291-306 | Revenue & material breakup | Device vs Map-data split (only quasi-segment data) | Device 23.11 / Map-data 116.61 (Q1FY27) | All | HIGH — device +204% YoY vs Map-data +2.3% |
| Consol N2 | line 307-311 | Basis / approval | Ind AS; Board approved 3–4 Aug 2026; LRR unmodified | — | — | None |
| Consol N3 | line 312-313 | Q4 balancing figure | Q4FY26 is a balancing figure | — | Q4FY26 | Q4FY26 numbers derived, not independently reported |
| Consol N4 | line 314-315 | Availability | On website/BSE/NSE | — | — | None |
| Consol N5 | line 316-318 | Segment | Single business segment → Ind AS 108 not applicable | — | All | HIGH — suppresses Map-vs-IoT & segment asset/liab data (F12-1) |
| Consol N6 | line 319 | Regrouping | Prior periods regrouped "wherever necessary" | ND | Prior | Unquantified regrouping; silent comparability break |
| Standalone N1–N6 | line 486-514 | Mirror of consol | Standalone device 19.83 / Map-data 104.65 | — | All | Same |

Auditor **Other-Matter** paras (consol LRR 6–7, lines 159-181): Group share of net loss Rs0.37 Cr from 2 associates not reviewed by MSKA; 1 subsidiary (revenue Nil, net loss Rs0.11 Cr) and the JV (share of loss Rs0.27 Cr) management-furnished/unreviewed, "not material." **Auditor opinion: UNMODIFIED (clean)** both standalone and consolidated (lines 153-158, 385-389). No EoM, no going-concern.

**0E. Business type:** **Standard operating business** (deep-tech map data / geospatial software / IoT). Steps 1 & 5 apply.

🛑 Pre-flight complete.

---

## STEP 1 — DATA EXTRACTION TABLE (standard business)

### 1A. CONSOLIDATED (Rs Cr)

| Line Item | Q1 FY26 | Q4 FY26 | Q1 FY27 | FY26 | Anchor (Q1FY27) |
|---|---|---|---|---|---|
| Revenue from Operations | 121.61 | 145.04 | 139.72 | 474.10 | line 226 |
| Other Income | 13.67 | 17.75 | 19.65 | 52.40 | line 227 |
| Total Income | 135.28 | 162.79 | 159.37 | 526.50 | line 228 |
| Cost of Materials Consumed | 4.74 | 13.09 | 14.83 | 32.95 | line 230 |
| Purchase of Stock-in-Trade | 6.46 | 8.85 | 7.04 | 28.28 | line 231 |
| Change in Inventories | (0.31) | (2.52) | (0.20) | (0.90) | line 232 |
| Employee Benefits Expense | 26.09 | 21.77 | 25.56 | 90.79 | line 233 |
| Technical Services Outsource & Project Software | 11.32 | 19.36 | 13.25 | 75.41 | line 234 |
| Finance Costs | 0.82 | 0.15 | 0.18 | 1.78 | line 235 |
| Depreciation & Amortisation | 6.88 | 7.91 | 9.15 | 30.42 | line 236 |
| Other Expenses | 17.44 | 19.73 | 23.12 | 72.06 | line 237 |
| Total Expenses | 73.44 | 88.34 | 92.93 | 330.79 | line 238 |
| Profit Before Tax | 61.84 | 74.45 | 66.44 | 195.71 | line 239 |
| Current Tax | 16.29 | 35.61 | 16.99 | 67.74 | line 241 |
| Deferred Tax charge/(benefit) | (1.83) | (16.96) | (0.93) | (16.53) | line 242 |
| Tax — earlier years | ND | 3.64 | ND | 3.74 | line 243 |
| Total Tax Expense | 14.46 | 22.29 | 16.06 | 54.95 | line 244 |
| NPAT (before assoc/JV) | 47.38 | 52.16 | 50.38 | 140.76 | line 245 |
| Share of Associates | (0.20) | (0.31) | (0.37) | (0.19) | line 248 |
| Share of JV | (1.37) | (0.92) | (0.27) | (6.55) | line 249 |
| **NPAT incl. assoc/JV** | **45.81** | **50.93** | **49.74** | **134.02** | line 251 |
| — attributable to owners | 46.11 | 50.77 | 49.77 | 134.16 | line 260 |
| — non-controlling interest | (0.30) | 0.16 | (0.01) | (0.14) | line 261 |
| EPS Basic (Rs) | 8.48 | 9.28 | 9.09 | 24.56 | line 274 |
| EPS Diluted (Rs) | 8.39 | 9.24 | 9.05 | 24.46 | line 275 |
| EPS share-adjusted (Basic) | 8.48 | 9.28 | 9.09 | 24.56 | = reported |

### 1B. STANDALONE (Rs Cr)

| Line Item | Q1 FY26 | Q4 FY26 | Q1 FY27 | FY26 | Anchor (Q1FY27) |
|---|---|---|---|---|---|
| Revenue from Operations | 102.65 | 127.58 | 124.48 | 400.74 | line 431 |
| Other Income | 14.28 | 18.76 | 18.38 | 57.08 | line 432 |
| Total Income | 116.93 | 146.34 | 142.86 | 457.82 | line 433 |
| Cost of Materials Consumed | ND | 0.07 | ND | 0.07 | line 435 |
| Purchase of Stock-in-Trade | 4.62 | 15.57 | 21.18 | 38.92 | line 436 |
| Change in Inventories | 0.15 | (0.03) | (1.18) | (0.09) | line 437 |
| Employee Benefits Expense | 15.61 | 10.25 | 13.53 | 46.19 | line 438 |
| Technical Services Outsource & Project Software | 15.57 | 38.14 | 19.81 | 120.48 | line 439 |
| Finance Costs | 0.23 | 0.23 | 0.17 | 1.04 | line 440 |
| Depreciation & Amortisation | 4.29 | 4.35 | 5.44 | 17.37 | line 441 |
| Other Expenses | 10.68 | 10.79 | 10.84 | 42.52 | line 442 |
| Total Expenses | 51.15 | 79.37 | 69.79 | 266.50 | line 443 |
| Profit Before Tax | 65.78 | 66.97 | 73.07 | 191.32 | line 444 |
| Current Tax | 16.09 | 29.22 | 16.92 | 61.10 | line 446 |
| Deferred Tax charge/(benefit) | (0.66) | (12.48) | 0.73 | (11.34) | line 447 |
| Tax — earlier years | ND | 3.63 | ND | 3.63 | line 448 |
| Total Tax Expense | 15.43 | 20.37 | 17.65 | 53.39 | line 449 |
| **Net Profit After Tax** | **50.35** | **46.60** | **55.42** | **137.93** | line 450 |
| EPS Basic (Rs) | 9.25 | 8.51 | 10.12 | 25.25 | line 460 |
| EPS Diluted (Rs) | 9.16 | 8.48 | 10.08 | 25.15 | line 461 |

### 1C. DERIVED METRICS (as reported)

| Derived Metric | Formula | Q1 FY26 | Q4 FY26 | Q1 FY27 | FY26 |
|---|---|---|---|---|---|
| **CONSOL** Operating EBITDA | PBT + D + FC − OI | 55.87 | 64.76 | 56.12 | 175.51 |
| **CONSOL** Operating EBITDA Margin | Op EBITDA / Rev | 45.9% | 44.7% | **40.2%** | 37.0% |
| **CONSOL** Reported EBITDA | PBT + D + FC | 69.54 | 82.51 | 75.77 | 227.91 |
| **CONSOL** Core PBT (ex-OI) | PBT − OI | 48.17 | 56.70 | **46.79** | 143.31 |
| **CONSOL** Other Income / PBT | OI / PBT | 22.1% | 23.8% | **29.6%** | 26.8% |
| **CONSOL** Effective Tax Rate | Tax / PBT | 23.4% | 29.9% | 24.2% | 28.1% |
| **CONSOL** PAT Margin (on Rev) | PAT incl assoc / Rev | 37.7% | 35.1% | 35.6% | 28.3% |
| **STANDALONE** Operating EBITDA | PBT + D + FC − OI | 56.02 | 52.79 | 60.30 | 152.65 |
| **STANDALONE** Op EBITDA Margin | Op EBITDA / Rev | 54.6% | 41.4% | 48.4% | 38.1% |
| **STANDALONE** Core PBT (ex-OI) | PBT − OI | 51.50 | 48.21 | 54.69 | 134.24 |
| **STANDALONE** ETR | Tax / PBT | 23.5% | 30.4% | 24.2% | 27.9% |

Cross-check: deck EBITDA (Rs56.1 Cr) = consolidated operating EBITDA (deck "EBITDA" excludes other income); deck margin 40.2% confirmed on the call by Rakesh Verma (T3/L12). Deck "PAT margin 31.2%" = PAT / Total Income, also repeated verbatim on the call (T3/L12) — a different denominator from PAT/Revenue (35.6%).

🛑 Every cell filled or ND.

---

## STEP 2 — Q1 FY27 YoY COMPARISON

### 2A. CONSOLIDATED — Q1 FY27 vs Q1 FY26 (as reported)

| Metric | Q1 FY26 | Q1 FY27 | YoY % | Verdict |
|---|---|---|---|---|
| Revenue from Operations | 121.61 | 139.72 | **+14.9%** | Positive (well above FY26's +2.3%) — confirmed on call (T3/L12) |
| Operating EBITDA | 55.87 | 56.12 | **+0.4%** | Flat as reported (see [v2 CORRECTION] below: +7.6% ex-one-time) |
| Operating EBITDA Margin | 45.9% | 40.2% | **−574 bps** | Reported compression (~287 bps one-time, ~287 bps mix) |
| Depreciation | 6.88 | 9.15 | +33.0% | Scaling ~2.2x revenue — absorption drag |
| Finance Costs | 0.82 | 0.18 | −78.0% | Benefit (deleveraged) |
| EBIT (operating) | 48.99 | 46.97 | −4.1% | As reported |
| Other Income | 13.67 | 19.65 | **+43.7%** | Reported (see [v2 CORRECTION]: ~+20% ex write-back) |
| **Core Operating PBT (PBT − OI)** | 48.17 | 46.79 | **−2.9%** | As reported (see [v2 CORRECTION]: **+5.4% ex-one-time**) |
| Reported PBT | 61.84 | 66.44 | +7.4% | — |
| PAT (incl assoc/JV) | 45.81 | 49.74 | +8.6% | Confirmed on call (T3/L12) |
| EPS share-adjusted (Basic) | 8.48 | 9.09 | +7.2% | — |

### 2B. STANDALONE — Q1 FY27 vs Q1 FY26

| Metric | Q1 FY26 | Q1 FY27 | YoY % | Verdict |
|---|---|---|---|---|
| Revenue from Operations | 102.65 | 124.48 | +21.3% | Strong (parent) |
| Operating EBITDA | 56.02 | 60.30 | +7.6% | Positive |
| Operating EBITDA Margin | 54.6% | 48.4% | −614 bps | Compression at parent too |
| Core Operating PBT (ex-OI) | 51.50 | 54.69 | **+6.2%** | Positive — parent core grew |
| Reported PBT | 65.78 | 73.07 | +11.1% | — |
| PAT | 50.35 | 55.42 | +10.1% | — |
| EPS Basic | 9.25 | 10.12 | +9.4% | — |

**Mandatory diagnostic answers (consolidated):**

1. **Revenue?** +14.9% (Rs121.61 → Rs139.72 Cr), a genuine improvement on FY26's +2.3% pace. Below the ~45% CAGR the FY28 Rs1,000 Cr target implies (a target now silent on the call, A3-16).
2. **Operating margin?** Reported −574 bps (45.9% → 40.2%). **[v2 CORRECTION]:** the concall shows ~287 bps of this is the one-time write-off (A3-04); underlying compression is ~287 bps (genuine IoT-mix dilution).
3. **Core operating PBT?** Reported **−2.9%** (Rs48.17 → Rs46.79 Cr). **[v2 CORRECTION]:** ex the Rs4 Cr write-off (booked in other expenses, inside the operating block), underlying core operating PBT ≈ Rs50.79 Cr = **+5.4% YoY**. The reported decline is entirely the one-time item; the underlying core is positive. See Step 4B for the full walk.
4. **Gap between core PBT and reported PAT?** As reported, Other Income +Rs5.98 Cr more than explains the +Rs4.60 Cr PBT rise. **[v2 CORRECTION]:** ~Rs3.2 Cr of that OI jump is the one-time payable-write-back (A3-05), not recurring treasury; recurring OI grew ~+20% (Rs13.67 → ~Rs16.45 Cr), still ahead of the operating line but far less than the reported +43.7%.
5. **D&A / finance costs vs revenue?** D&A +33.0% vs revenue +14.9% — ~2.2x, a mild capex-absorption drag. Finance costs fell (deleveraged).
6. **Other Income concentration?** Reported OI is 29.6% of PBT (from 22.1%). **[v2 CORRECTION]:** on the underlying (ex-write-back) basis OI is ~Rs16.45 Cr ≈ 25% of an underlying PBT of ~Rs67.24 Cr — still elevated and rising, but not the 29.6% the face of the P&L shows.

🛑 YoY table and six diagnostics shown.

---

## STEP 3 — SEQUENTIAL QoQ TRAJECTORY (consolidated)

| Quarter | Revenue (Rs Cr) | Op EBITDA Margin | Core PBT ex-OI (Rs Cr) | One-offs flagged | QoQ run-rate |
|---|---|---|---|---|---|
| Q1 FY26 | 121.61 | 45.9% | 48.17 | — | base |
| Q2 FY26 | 113.80 | ND | ND | — | dipping |
| Q3 FY26 | 94.30 | ND | ND | — | trough |
| Q4 FY26 | 144.40 | 44.7% | 56.70 | Q4 = balancing figure (N3); earlier-yr tax +3.64 | recovery peak |
| Q1 FY27 | 139.72 | 40.2% (underlying ~43.0%) | 46.79 (underlying ~50.79) | **Rs4 Cr govt write-off (T12/L34); geometry now known** | −3.7% QoQ; margin down reported, roughly flat underlying |

Diagnostics:
- **Run-rate:** revenue −3.7% QoQ vs Q4FY26 but Q1 is seasonally the weakest Government quarter — now confirmed verbatim on the call: "government is a slow starter... Q1 is generally the weakest in government" (T17/L45, A3-21). YoY the run-rate is up +14.9%.
- **One-off:** the Rs4 Cr government write-off is booked in **Other Expenses** (inside operating EBITDA) with an offsetting ~Rs3.2 Cr payable-write-back in **Other Income** (below EBITDA); net P&L hit ~Rs0.80 Cr (T12/L34, T37/L87, T41/L95). Management: "instead of 40.2 it would have been 43 plus" (T12/L34).
- **Margin story [v2 CORRECTION]:** the reported sequential fall (44.7% → 40.2%) and the −574 bps YoY are ~half one-time. Underlying ~43.0% is closer to the Q4FY26 44.7% level, so the *genuine* mix-driven erosion is real but roughly half what the face of the P&L implies. The write-off itself remains a realized collection failure — the underlying number does not erase it, it re-classifies it as non-recurring.
- **Implied Q2 base:** Q2 FY27 revenue must exceed Q2 FY26's Rs113.8 Cr for positive YoY; margin must hold ≥40% (reported) without a fresh write-off; full-year guide is 35%+ (T14/L38), implying H2 dilution.

🛑 QoQ table and diagnostics shown.

---

## STEP 4 — OPERATIONAL DECOMPOSITION (PAT bridge, consolidated YoY)

### 4A. Reported PAT bridge (Rs45.81 → Rs49.74 Cr; +Rs3.93 Cr / +8.6%)

| Component | YoY change (Rs Cr) | YoY change (%) | Recurring? |
|---|---|---|---|
| Operating EBITDA (volume + margin, net, reported) | +0.25 | +0.4% | Recurring |
| — of which revenue growth at prior margin | +8.31 | — | Recurring |
| — of which margin compression (−574 bps, reported) | −8.06 | — | Recurring (~half one-time, see 4B) |
| D&A change | −2.27 | +33.0% | Recurring (post-capex) |
| Finance cost change | +0.64 | −78.0% | Recurring (post-debt) |
| **= Core operating PBT change (reported)** | **−1.38** | **−2.9%** | Recurring — negative as reported |
| Other Income change (reported) | +5.98 | +43.7% | Partly one-time (Rs3.2 Cr write-back) |
| = Reported PBT change | +4.60 | +7.4% | Mixed |
| Tax change (absolute) | −1.60 | — | Mixed (ETR 23.4% → 24.2%) |
| = NPAT before assoc/JV change | +3.00 | +6.3% | Mixed |
| Associate/JV share (loss narrowed) | +0.93 | — | Mostly recurring |
| NCI | +0.29 | — | Mixed |
| **Reported PAT change** | **+3.93** | **+8.6%** | — |

### 4B. [v2 CORRECTION] — UNDERLYING (EX-ONE-TIME) WALK, anchored to concall turns

Write-off geometry (management verbatim):
- Gross write-off booked in **Other Expenses** (inside operating EBITDA): **~Rs4.0 Cr** (T12/L34: "the impact has been almost like a 4 crores"; T37/L87).
- Offsetting payable-no-longer-owed booked in **Other Income** (below EBITDA): **~Rs3.2 Cr** (T37/L87: "back to back there was a payment for 3.2 cr... I don't have to make that payment"; T41/L95: "that payback... has gone as an other income").
- Net P&L hit: **~Rs0.80 Cr** (T12/L34: "the net effect of that is only 80 lakhs"; re-confirmed T39/L91).

| Metric | Reported Q1FY27 | One-time adj | Underlying Q1FY27 | Q1FY26 | Underlying YoY |
|---|---|---|---|---|---|
| Operating EBITDA | 56.12 | +4.0 (write-off in opex) | **60.12** | 55.87 | **+7.6%** |
| Operating EBITDA margin | 40.2% | +~287 bps | **~43.0%** ("43 plus", T12/L34) | 45.9% | **−287 bps** (not −574) |
| Other Income | 19.65 | −3.2 (write-back) | **16.45** | 13.67 | **+20.3%** (not +43.7%) |
| Core Operating PBT (ex-OI) | 46.79 | +4.0 (write-off in opex) | **50.79** | 48.17 | **+5.4%** (FLIPS reported −2.9%) |
| Reported PBT | 66.44 | +0.80 (net hit) | **67.24** | 61.84 | +8.7% |

**Margin-compression decomposition:** of the 574 bps reported YoY fall, **~287 bps is the one-time government write-off** (Rs4.0 Cr / Rs139.72 Cr) and **~287 bps is genuine IoT-mix-driven compression** (IoT share rose 19.2% → 29.4% at ~13% margin vs Map ~51%). The conservative read is retained alongside: the underlying number does not delete the write-off (it is a realized collection failure on a government receivable, A3-04), and the *reported* P&L — the number that flows to valuation and to the CFO/PAT test — still shows the full compression.

**Mandatory answers:**
- **% of PAT growth from recurring core vs non-recurring:** As reported, core is −Rs1.38 Cr and the +Rs3.93 Cr is treasury/one-off carried. **On the underlying basis, core operating PBT contributed +Rs2.62 Cr (+5.4%)** and the business, not treasury, carried a majority of the growth. Both framings are stated; the reported framing is the conservative anchor for valuation, the underlying framing is the truer read of operating health.
- **If OI reverts to prior-year level:** on reported OI, PAT would sit below Q1 FY26. On underlying OI (~Rs16.45 Cr), reverting to Rs13.67 Cr still leaves PBT roughly flat-to-up — the underlying operating business is not going backwards.
- **D&A steady-state:** still ramping (+33% YoY); mild ROCE drag until volume absorbs.
- **Tax:** deferred-tax credit Rs0.93 Cr (consol) shields ETR to 24.2%, ~140 bps below the 25.17% statutory (F8-2) — future ETR step-up risk. No earlier-years tax this quarter.

🛑 Bridge, the ex-one-time walk, and answers presented.

---

## STEP 5 — CASH QUALITY & BALANCE SHEET

**Data-availability rule (v1.2):** Q1 review. Reg 33 mandates half-yearly cash flow / balance sheet at Q2 and Q4 only. The filing is P&L-only; the concall **confirmed** this: "Q1 we've not given the balance sheet, but just like a quarter ago we had given it" (T33/L78, A3-01). Therefore Step 5 is largely ND and **cash conversion is INDETERMINATE** — unchanged from v1, now management-confirmed.

| Metric | Prior (FY26 / Q1FY26) | Current (Q1 FY27) | Change | Verdict |
|---|---|---|---|---|
| CFO | ND | ND | ND | Not disclosed at Q1 — escalate to Q2 H1 |
| CFO/PAT ratio | ND | ND | ND | INDETERMINATE — caps Pillar 2 |
| Capex (PPE + CWIP) | ND | ND | ND | D&A +33% YoY only proxy |
| FCF | ND | ND | ND | ND |
| Working-capital change | ND | ND | ND | ND |
| Receivable days | ND | ND | ND | **Falsifier input — not disclosed (confirmed T33/L78)** |
| Inventory days | ND | ND | ND | ND |
| Payable days | ND | ND | ND | ND |
| Cash Conversion Cycle | ND | ND | ND | ND |
| Total trade receivables | 176 (FY26 close, T34/L80) | **ND at 30-Jun-2026** | ND | Only FY26-end Rs176 Cr confirmed; Q1 number withheld |
| Cash & equivalents (incl financial instruments) | 685.0 (FY26 close, deck 289) | **745.3** (deck 289) | **+60.3 QoQ** | Treasury accreting; no allocation plan (MMI-12; call SILENT, A3-17) |
| Net Debt / (Net Cash) | Net cash | Net cash, larger | ND precise | Deleveraged (finance cost Rs0.18 Cr) |
| Promoter Pledge | 0% (Notion) | ND in filing | ND | No pledge disclosed |

**Mandatory answers:**
- **CFO/PAT vs Pillar 2 band:** not testable at Q1; remains capped by INDETERMINATE cash (Notion: consol CFO/PAT 69.6% at FY26, down from 79.3%). Update only at Q2 H1 cash flow.
- **WC drag structural or growth-induced:** untestable from the filing. **[v2 reframe]** the concall re-points the driver: management confirms "as government has grown it has reflected in the receivables... it is a longer cycle on government" (T29/L70, A3-02) and "the majority of the receivable will be from government — not like a large majority, but a majority" (T34/L80). This is *government-receivable* lengthening, not the Gtropy overdraft the Notion checklist assumed (A3-18; Gtropy not spoken once).
- **CWIP capitalisation:** not disclosed; D&A +33% consistent with recent capitalisation, unverifiable.
- **Net debt vs projection:** net-cash, de-leveraging; cash +Rs60.3 Cr QoQ to Rs745.3 Cr.

### BINDING FALSIFIER — explicit assessment (FLAG-CASH) [v2 UPDATE]

Pre-committed falsifier: *Q1 FY27 consolidated receivables ABOVE the Rs176.4 Cr FY26 close, on flat-to-up revenue, with the 6-month-plus bucket widening → confirms FLAG-CASH as STRUCTURAL.*

**Resolution: STILL UNRESOLVABLE (A3-01).** The concall explicitly confirmed no Q1 balance sheet was filed (T33/L78). Per the NEVER-estimate rule, no 30-Jun-2026 receivables number is inferred. The falsifier escalates to the **Q2 FY27 half-year balance sheet (~Nov 2026)**.

**However — the concall makes the falsifier MILDLY ADVERSE, not neutral. [v2]**
1. **Root cause reframed Gtropy → GOVERNMENT (A3-02).** Management attributes the receivables build to government's "longer cycle" and confirms receivables "grow as government grows." Total was Rs176 Cr at FY26 end, "a majority" (not a large majority) government.
2. **The Rs4 Cr write-off is a realized government-receivable failure (A3-04):** "when we were 100% sure that we will never be able to get that revenue, we decided that it's better to do the write off" (T29/L70). This is a confirmed collection loss on the very segment the falsifier tracks.
3. **Management self-identifies receivables as a growth constraint (A3-13):** on digital-twin / Naksha pursuit it will be "calibrated... what will lead to good receivables versus bad receivables. We've seen that issue play out in the peer companies" (T82/L180).
4. **Unverifiable reassurance (A3-03):** "our receivables are far better than peer companies when it comes to government" — no peer, no metric, no number; offered in the same breath as "we also have to be careful."

**Disposition: MILD ADVERSE CONFIRMATION of the collection concern.** Not benign; not yet structural-confirmed (no ageing, no Q1 number). It removes any benign read of the write-off and re-anchors the concern to government receivables.

**Cash conversion: INDETERMINATE → caps the protocol verdict at PROCEED WITH CAVEATS.** Missing evidence named: (1) consolidated trade receivables at 30-Jun-2026 vs Rs176 Cr FY26 close; (2) the 6-month-plus government ageing bucket; (3) H1 FY27 consolidated CFO and CFO/PAT; (4) whether the Rs4 Cr government write-off is genuinely isolated or the leading edge of a wider government-receivable problem.

🛑 Cash-quality table and answers; falsifier assessed, not resolved.

---

## STEP 5-SC — STANDALONE vs CONSOLIDATED GAP (first-class metric, F2-1)

| Period | Consol PAT (incl assoc/JV) | Standalone PAT | Gap (Rs Cr) | Gap as % of standalone PAT |
|---|---|---|---|---|
| Q1 FY26 | 45.81 | 50.35 | −4.54 | −9.0% |
| Q4 FY26 | 50.93 | 46.60 | +4.33 | +9.3% |
| Q1 FY27 | 49.74 | 55.42 | **−5.68** | **−10.2%** |
| FY26 (full) | 134.02 | 137.93 | −3.91 | −2.8% |

QoQ swing Q4FY26 → Q1FY27 = **19.5 pp** of standalone PAT, far beyond the 5 pp trigger. Subsidiary/JV/associate block is loss-making this quarter: subsidiaries take consol NPAT-before-associates (50.38) below standalone (55.42) = −Rs5.04 Cr; assoc/JV −Rs0.64 Cr; NCI ~+Rs0.03 Cr. Corroborated by standalone net worth (Rs920.3 Cr) exceeding consolidated (Rs894.0 Cr) at FY26 close (~Rs26 Cr of cumulative subsidiary/JV/associate erosion).

**[v2 concall note]:** management explicitly *deprecated* standalone analysis — "there is not much value in analyzing standalone... you should look at the consolidated" (T17/L45) — arguing government/IoT work is won at the parent and subcontracted to subsidiaries. This is a plausible structural explanation for the parent-vs-consol split, but it does not resolve the finding: the consolidated is where the drag lands, and management steered analysts away from the one cut (standalone vs subsidiary) that would isolate it. Signal retained: parent healthy (core PBT +6.2%, PAT +10.1%); consolidation dragged by the subsidiary block; gap at −10.2% is a first-class negative.

---

## STEP 6 — RECONCILIATION vs THESIS

### 6A. Variance vs Notion projections

Numeric Bear/Base/Bull ladders were not passed inline; cells needing them are ND (no estimation).

| Metric | Bear | Base | Bull | Actual Q1 FY27 | Lands In |
|---|---|---|---|---|---|
| Revenue | ND | ND | ND | 139.72 (+14.9%; ~Rs560 Cr annualised) | Above FY26 pace; behind FY28 Rs1,000 Cr |
| EBITDA Margin (operating) | ND | ND | ND | 40.2% reported / ~43.0% underlying | Reported below trajectory; underlying near it |
| PAT | ND | ND | ND | 49.74 (+8.6%; underlying core +5.4%) | Headline OK; underlying core positive |
| EPS (Basic) | ND | ND | ND | 9.09 | — |
| Net Debt | ND | ND | ND | Net cash Rs745.3 Cr | Better than any drawdown |
| ROCE | ND | ND | ND | ND (no interim BS) | Untrackable at Q1 |

**Probability re-weighting (v1.2):** requires actuals BELOW BEAR on 2+ metrics for 2 consecutive quarters. Bear thresholds not passed numerically; and the concall's ex-one-time correction shows underlying operating metrics are *positive*, not below bear. **No re-weight fires.** Logged: if Q2 FY27 shows underlying core operating PBT declining YoY with margin below trajectory, reconsider at the next valuation refresh.

### 6B. Watchlist-item status (10 Notion items) [v2 updated with concall]

| # | Watchlist item | Green | Red | This quarter reading | Status |
|---|---|---|---|---|---|
| 1 | Govt revenue growth back to 15–20% YoY | ≥15% | <10% | Not quantified on call ("slow starter... Q1 weakest", A3-21); deck implied ~9.2%/claimed 11% (MMI-03) | **RED / SILENT on number** |
| 2 | Consol receivables below Rs176 Cr on flat/up rev | <176.4 | >176.4 & 6m+ widening | **Not disclosed** (T33/L78 confirmed); root cause reframed to government; Rs4 Cr govt write-off adverse | **UNKNOWN / AMBER-adverse** |
| 3 | Gtropy overdraft & 6m+ ageing | falling | rising | **Gtropy never mentioned** (A3-18); subsidiary block loss-making | **UNKNOWN / SILENT** |
| 4 | Blended EBITDA margin >38% two consecutive quarters | >38% x2 | <38% | Q4FY26 44.7% & Q1FY27 40.2% both >38%; BUT full-year guide reaffirmed **"35% plus"** (T14/L38) | **GREEN on level / RED on full-year guide** (mgmt guides below 38% for FY27) |
| 5 | Map/data core returning to positive YoY | >0% | <0% | Map-led Rs98.2 → Rs98.7 Cr = +0.5% (T17/L45); analyst called it "very very flat" (T20/L51) | **GREEN (marginal) — materially stalled** |
| 6 | ClarityX/Zenithra RPT ceiling | low | near cap | **No RPT discussion of any kind** (A3-19) | **UNKNOWN / SILENT** |
| 7 | ROE/ROCE / net-profit trend | rising | falling | Net-profit ratio 35.6% (vs 37.7% Q1FY26); ROE/ROCE ND; not discussed on call | **AMBER / SILENT on ratios** |
| 8 | FY28 Rs1,000 Cr target pacing (~45% CAGR) | on pace | off pace | **Target not mentioned despite direct forward-growth question** (A3-16); order book Rs1,750 Cr reaffirmed instead | **RED / SILENT (soft-dropped across deck, PR and call)** |
| 9 | MD succession disclosure | disclosed | opaque | Rohan Verma JMD announced 30-Jun-2026 confirmed (T3/L12); focus areas discussed (T6/L22); ratification not separately confirmed | **ADDRESSED (executing)** |
| 10 | Capital-allocation plan for idle treasury | plan given | none | Cash Rs745.3 Cr (+60 QoQ); **no plan; OI discussed only as write-back mechanism** (A3-17) | **RED / worsening** |

### 6C. Thesis-Broken trigger check

| Thesis-Broken condition | Threshold | Current reading | FIRED? |
|---|---|---|---|
| FLAG-CASH structural (binding falsifier) | Receivables >Rs176.4 Cr on flat/up rev + 6m+ widening | Unresolvable (no Q1 BS, T33/L78); Rs4 Cr govt write-off + government root cause = mild adverse | **NO (unresolvable; escalated to Q2 H1 BS)** |
| Map/data core sustained negative YoY | <0% multi-quarter | +0.5% YoY this quarter (marginally positive) | NO |
| Governance / promoter overhang worsens materially | new adverse RPT / control event | Rohan Verma elevated to Joint MD; no new adverse RPT surfaced on call | NO (watch; not a defined breach) |
| Blended margin sustained <38% | <38% multi-quarter | 40.2% reported this quarter (>38%); full-year guide 35%+ is a forward amber | NO (but FY27 guide below 38%) |

**No thesis-broken condition has formally FIRED.** The binding falsifier is unresolvable, not cleared.

### 6D. Growth-trigger status [v2 updated with concall]

| Trigger | Original confidence | Confirming evidence | Killing evidence | Updated status |
|---|---|---|---|---|
| Map/data core recovery | Low | Map-led +0.5% YoY (T17/L45) | QoQ −8.3%; "very very flat" (T20/L51); single-segment reporting | **WEAKENED → marginal ON TRACK** |
| IoT scaling at improving margin | Medium | IoT +75% to Rs41.1 Cr; hardware Rs7 → Rs23 Cr (T45/L103) | Hardware-first, SaaS "kicks in later", billing-cycle dependent (A3-12); dilutive to blend | **ON TRACK (margin-dilutive; SaaS uplift un-dated)** |
| Government re-acceleration | Medium | Defense/oil-and-gas "green shoots" (T6/L22, A3-10) | +~9.2% (deck), not quantified on call; Rs4 Cr write-off; longer cash cycle | **DELAYED / WEAKENED** |
| Order-book-led FY28 Rs1,000 Cr | Medium | Order book **Rs1,750 Cr reaffirmed** (T19/L49), up from Rs1,500 / Rs1,350 Cr | FY28 Rs1,000 Cr target itself gone silent (A3-16); intake/mix withheld (A3-14) | **DELAYED (order book up, target silent)** |
| Treasury deployment / capital allocation | Low | — | Cash Rs745.3 Cr, no plan; SILENT on call (A3-17) | **DEAD / STALLED** |

🛑 6A–6D presented.

---

## STEP 7 — FOUR-PILLAR DESTINATION PE RE-VALIDATION

No pillar can be hard-updated on a P&L-only filing (no balance sheet → no ROCE, no CFO/PAT). The concall adds forward *colour* (35%+ margin guide, order book Rs1,750 Cr, government cash-cycle lengthening) but no hard balance-sheet input.

| Pillar / Input | Original assumption | Current reading (Q1 FY27) | Action |
|---|---|---|---|
| ROCE Base (0.5×ROCE + 7.5, floor 9x, cap 24x) | Per destination PE 32x build | ROCE **ND** (no interim BS); D&A +33% = mild ROCE pressure | **Hold** — no FTTCP ROCE re-run possible; re-run at Q2 H1 BS |
| Cash Multiplier | Capped by INDETERMINATE cash | CFO/PAT ND; govt-receivable cycle lengthening (A3-02); Rs4 Cr write-off adverse | **Hold, capped** — cannot lift above INDETERMINATE cap |
| Growth Visibility Premium | Per EM 30/100 | Order book Rs1,750 Cr now disclosed on call (was absent from deck, MMI-07) — a small positive; FY28 target silent | **Hold** (order book fills a disclosure gap; target silence offsets) |
| Strategic Premium | Moat / single-credit state | Map-led core marginally positive; "no other company like us... deep tech" (T4/L15) is narrative, not new evidence; single-credit intact | **Hold** |
| UA Multiplier | Per Amendment 3 | Shareholding unchanged (promoter 51.4%) | **Hold** |
| Sector Cap | 45x | No reclassification (single segment; AEG is market-facing only) | **Hold** |
| **Hurdle Ratio recheck** | HR = (1+EPS CAGR)³ × (Dest PE mid ÷ Current PE) ≥ 1.953 | TTM EPS 25.17; CMP ~Rs1,185 → trailing PE ≈ 47.1x; dest 32x → dest/current ≈ 0.68; at ~4–5% CAGR HR ≈ (1.045)³ × 0.68 ≈ **0.78 «< 1.953** | **STOP** (unchanged) |

**Destination PE: no recompute** — no pillar input changed with hard evidence. TTM EPS = 24.56 − 8.48 + 9.09 = **Rs25.17**; trailing PE ≈ **47.1x** vs 32x destination and 45x cap. Hurdle Ratio **STOP**. Fair values unchanged.

🛑 Pillar re-validation shown; no revised fair values.

---

## STEP 8 — POSITION DECISION (Role 4 view; Role 5 8E override applied in Section B)

**Decision Status verified: WATCHLIST / AVOID → Step 8A-W branch. No trim/exit mechanics.**

- **Any thesis-broken condition FIRED?** No (6C).
- **Actual below bear on 2+ metrics?** Not determinable (thresholds not passed); the ex-one-time correction shows underlying operating metrics positive.
- **Where do results land?** **MIXED-to-slightly-better than v1 read.** Positive: revenue +14.9%; **underlying operating EBITDA +7.6% and underlying core operating PBT +5.4%** (the write-off drove the reported softness); Map-led core marginally positive; IoT +75%; order book Rs1,750 Cr reaffirmed and disclosed; net cash growing; auditor unmodified. Negative: reported margin −574 bps; government segment soft and unquantified with a realized Rs4 Cr write-off; receivables root cause now government (longer cycle); consol-vs-standalone gap −10.2%; FY28 target and treasury plan silent; full-year margin guide 35%+.

**Decision (8A-W):**
- **Decision Status: HOLD at WATCHLIST / AVOID.** No trigger fired; the operating-quality read improves on the ex-one-time correction, but nothing clears the two overhangs and nothing justifies entry at CMP.
- **Position:** nil at CMP (Rs1,185, ~47x trailing, Hurdle STOP). Small 2–3% only in the Rs690–700 zone with the cash falsifier resolved benign.
- **Entry zone: unchanged** — Max Rs700, base Rs690–700, MoS Rs555. No pillar moved.
- **Master decision gate: Q2 FY27** (mandatory H1 balance sheet + cash flow). Gate question: *does H1 FY27 consolidated receivables sit below Rs176 Cr on flat/up revenue with the government 6-month-plus bucket not widening, and is the Rs4 Cr government write-off non-recurring?*

### 8B. Add-back / trim trigger refinement
- Original: enter only Rs690–700, small 2–3%, contingent on cash falsifier resolving benign.
- **Revised add-back gate:** require BOTH (a) H1 FY27 receivables below Rs176 Cr with stable/narrowing government 6m+ ageing, AND (b) two consecutive quarters of **underlying** operating EBITDA margin ≥38% with underlying core operating PBT positive YoY. **[v2 note]** the ex-one-time correction means condition (b) is *closer to met* than v1 implied (underlying core +5.4% this quarter), but it is a single quarter and the write-off itself is a collection event — do not relax the receivables leg.
- Trim ladder: N/A (not held).

### 8C. Single cleanest metric for Q2 FY27
**Consolidated trade receivables and the government 6-month-plus ageing bucket at 30 September 2026 (H1 FY27 balance sheet).** The one number that resolves the binding falsifier.
- **Bull:** receivables **below Rs176 Cr** on flat/up H1 revenue, 6m+ bucket not widening, Rs4 Cr write-off not repeated → FLAG-CASH toward growth-induced.
- **Bear:** receivables **above Rs176 Cr** with 6m+ widening → FLAG-CASH STRUCTURAL → thesis-broken fires → hard AVOID.
- Secondary: **underlying core operating PBT ex-Other Income ex-one-time YoY** — cleanest test that the business, not treasury or one-offs, is growing.

🛑 Step 8 (Role 4 view) presented.

---

# SECTION B — CONCALL ANALYSIS (Role 5 v1.1) — RUN IN FULL [supersedes v1 Section B]

## STEP 0 — PRE-FLIGHT

**0A. Notion (as Section A 0A).** Thesis: WATCHLIST/AVOID; growth triggers = Map-core recovery, IoT margin scaling, government re-acceleration, order-book-led FY28 Rs1,000 Cr, treasury deployment; thesis-broken = FLAG-CASH structural, Map-core sustained negative, promoter overhang worsening, blended margin <38%. DA said management would evade the receivables number and the treasury plan — both proved correct on this call.

**0B. Participants** (ledger §1):

| Role | Name | Notes |
|---|---|---|
| Hosting broker / IR | Ms. Natasha Singh, Arhant Capital Markets | Non-house independent broker host |
| Chairman & MD | Mr. Rakesh Verma | **Promoter present** and extensively speaking |
| Joint MD | Mr. Rohan Verma | Promoter's son; JMD from 2026-07-01; answered most operational Q&A |
| CFO | Mr. Anuj Jain | **`SILENT_PARTICIPANT`** — named present, zero individually-attributed turns; all financial/reconciliation answers went to Rakesh/Rohan Verma or generic "[Management]" |
| Company Secretary | Mr. Saurabh Somani | `SILENT_PARTICIPANT` |

**Yellow flags from participant list:** (1) **CFO silent throughout** — the Rs4 Cr write-off reconciliation, the receivables total, and the "80 lakhs net" geometry were all handled by the Chairman/Joint MD, not the CFO; for a call whose single most technical exchange was an accounting-geometry reconciliation, the CFO's silence is a genuine yellow flag. (2) Both promoters on the line is, per Role 5, a candour *positive* — Indian small/mid-cap calls with the CMD present are typically more candid; borne out by Rakesh Verma volunteering the "80 lakhs net" figure. No promoter-absence flag.

**0C. Call structure:** Q1 FY27 (quarter ended 30-Jun-2026); held same-day-ish with the 4-Aug filing (canned-to-managed window). 7 numbered analyst questioners, 33 distinct question turns, 86 total turns. Duration not stated in transcript; Q&A is the overwhelming majority of the call (opening remarks are two short statements, T3–T4). Engaged buy-side audience (Lucky Investment, CWC, Banyan Tree, Chris PMS are AIF/PMS buy-side; HDFC Securities sell-side).

**0D. Safe-harbour caveats:** none read into the transcript beyond the standard moderator preamble; no new caveat categories added.

**0E. Business type:** **Standard operating business** (not a lender) → Step 2 guidance set.

🛑 Pre-flight complete.

## STEP 1 — OPENING REMARKS — CLAIMS INVENTORY

| # | Claim | Type | Quantified? | Source |
|---|---|---|---|---|
| 1 | Q1 FY27 revenue up 14.9% YoY to Rs139.7 Cr | Backward | YES | T3/L12 |
| 2 | EBITDA Rs56.1 Cr, margin 40.2% | Backward | YES | T3/L12 |
| 3 | PAT up 8.6% to Rs49.7 Cr, PAT margin 31.2% | Backward | YES | T3/L12 |
| 4 | Segment framework changed A&M/C&E → Automotive / Enterprise / Government | Strategic | NO (no mapping bridge) | T3/L12 |
| 5 | Rohan Verma appointed Joint MD (announced 30-Jun), "stronger leadership... show up in times to come" | Strategic/Governance | Partial (date only) | T3/L12 |
| 6 | "AI is not new to us... leaning heavily into AI, AI-native product development... golden era" | Strategic / Macro | NO | T4/L15 |
| 7 | "multi-product, multi-industry, multi-use-case"; 30-year legacy; "moat... flywheel" | Strategic | Partial (30 yrs) | T4/L15 |
| 8 | "There is no other company like us... deep tech products in India or around the world" | Strategic | NO | T4/L15 |

**Diagnostics:** (i) ~3 of 8 opening claims quantified (all three are backward results restated verbatim from the filing); forward opening content is entirely qualitative ("golden era", "right to win"). (ii) New vs reaffirmation: the AEG segment reframe and the JMD appointment are new; the AI push and moat narrative are reaffirmations. (iii) **Quietly dropped:** the FY28 Rs1,000 Cr revenue target — expected in a forward-looking opening — does not appear (A3-16). (iv) Internal contradictions: none in the opening itself, but the "40.2% margin" headline is later shown to embed a one-time write-off that management only reconciles under Q&A pressure.

🛑 Claims inventory and four diagnostics shown.

## STEP 2 — FORWARD GUIDANCE EXTRACTION

| Metric | This Quarter's Guidance | Last Quarter's | Two Quarters Ago | Trajectory | Confidence |
|---|---|---|---|---|---|
| Revenue growth (FY27) | None given (order book cited instead) | ND | ND | Withdrawn/absent | LOW |
| Revenue target (FY28 Rs1,000 Cr) | **Not mentioned** (A3-16) | (prior-doc target) | (prior-doc target) | **Dropped (silent)** | — |
| EBITDA margin band | **"35% plus for the whole year"** FY27 (T14/L38) | ND (prior verbal per mgmt "we have always been saying") | ND | Maintained (per mgmt) | MEDIUM (hedged "quarter by quarter you'll have to see") |
| Order book / pipeline | **Rs1,750 Cr open order book** (T19/L49) | Rs1,500 Cr (prior year-end) | Rs1,350 Cr | Tightened/growing | HIGH (specific, with 2-yr trend) |
| Order-book segment mix | Withheld "for competitive reasons" (T27/L66) | ND | ND | Withdrawn | LOW |
| Automotive growth target FY27 | Refused ("not going to talk about quantitative target", T68/L150) | ND | ND | Refused | LOW |
| Working capital / receivables | Refused Q1 number (T33/L78); FY26-end Rs176 Cr confirmed | Rs176 Cr (FY26 BS) | ND | Withdrawn (Q1) | LOW |
| International / JV | "share-of-loss reduced, I'm guessing"; "not material" (T53/L119) | ND | ND | Soft-maintained | LOW |
| IoT SaaS uplift | "SaaS will kick in... in time to come", billing-cycle dependent (T47-51) | ND | ND | New (un-dated) | LOW |
| Digital-twin / Naksha | "looking aggressively... calibrated" on receivable quality (T82/L180) | ND | ND | New (gated) | LOW |
| Dividend / payout | Not discussed | ND | ND | — | — |
| Capex envelope | Not discussed | ND | ND | — | — |

**Diagnostics:**
- **Widen or tighten?** The one hard forward number (35%+ FY27 margin) is *maintained* but guides **below** both the 40.2% reported and the ~43% underlying — i.e. management is signalling H2 blended-margin dilution as IoT scales. The order book *tightened* (Rs1,350 → Rs1,500 → Rs1,750 Cr).
- **Dropped without acknowledgment?** Yes — the **FY28 Rs1,000 Cr target** (A3-16), a major credibility flag given a direct forward-growth question (T18/L47, T20/L51) was answered with the order book, never the target.
- **Internally consistent?** 35%+ full-year vs 40.2% Q1 vs Rs1,750 Cr order book is consistent with a front-loaded-margin, IoT-diluting-H2 picture; the arithmetic does not conflict.
- **vs Four-Pillar?** 35%+ margin sits below the FY26 blended level embedded in the destination-PE build; a forward amber, not a break.
- **Refused what analysts pressed for?** Q1 receivables number, order-book segment mix, automotive growth target, per-vehicle pricing — all refused. The receivables refusal is the thesis-critical one.

🛑 Guidance table and diagnostics shown.

## STEP 3 — PROMISE vs DELIVERY AUDIT

**This is the FIRST concall analysed under Role 5 for MAPMYINDIA** (v1 marked Role 5 N.A.; no prior concall log exists). Per Step 3, the historical trailing-4 audit is not yet computable — the log begins this quarter. What *can* be audited: (3A) the two written claims v1 logged as the promise-vs-delivery seed, and prior-document commitments; (3E) the v1 Role 4 "Questions for Management" table, which this concall partially answered.

### 3A. Prior written commitments (seed) — status this call

| Commitment (source) | This call's actual | Status | Points |
|---|---|---|---|
| "Rs4 Cr write-off is one-time" (v1 seed; deck MMI-06) | Reasserted "one-time write off of a government client" (T12/L34, T29/L70), but self-qualified by admitting government is "a longer cycle" and "we also have to be careful" | UNCLEAR (recurrence testable only at Q2) | excluded |
| Government softness "seasonal" (v1 seed; deck MMI-11) | Reaffirmed "Q1 is generally the weakest in government" (T17/L45) — but the YoY number was not quantified | UNCLEAR (seasonality vs demand testable at Q2/H1) | excluded |
| FY28 Rs1,000 Cr revenue target (prior-doc; MMI-10, F16-3) | **Not mentioned** despite direct forward-growth question | DROPPED (silent) — governance flag | 0 + flag |
| Order book disclosure (prior-doc; absent from deck, MMI-07) | **Disclosed on call: Rs1,750 Cr**, up from Rs1,500 / Rs1,350 Cr | DELIVERED | 1.0 |

### 3B. Cumulative track record (trailing 4 concalls)

| Concall Date | Total Commitments | Delivered | Partially | Missed | Delayed | Dropped | Unclear | Points |
|---|---|---|---|---|---|---|---|---|
| Q1 FY27 (2026-08, this call — FIRST under protocol) | 4 (scoreable) | 1 | 0 | 0 | 0 | 1 | 2 | 1.0 |

**Credibility Ratio (v1.1 formula) = Total Points ÷ (Total Commitments − UNCLEAR) = 1.0 ÷ (4 − 2) = 1.0 ÷ 2 = 50%.**
**PROVISIONAL — single data point, first concall under the protocol.** A 50% single-quarter ratio maps to **Grade C (Mixed)** on the raw table, but with only 2 scoreable items (one DELIVERED, one DROPPED) the sample is too small to set the trailing-4 grade. **Treat as Grade B/C borderline this quarter, provisional**, pending the next three concalls. The one DROPPED (FY28 target) is logged; the two-DROPPED automatic-downgrade rule has NOT fired (only one this window).

### 3C. Pattern recognition (nascent)
- The single most-repeated topic was the **write-off**, asked independently by **three** analysts (Anmol/DA Capital T11, HDFC Securities T28, Gautam Rathi/CWC T36) — a `REPEAT_QUESTION` signal that the market did not trust the first (headline "4% margin impact") answer until Gautam forced the geometry out. To management's credit, once pushed they reconciled it honestly.
- Consistent refusal to give forward *numbers* (automotive target, receivables, order-book mix) alongside willingness to give *backward* numbers — an early "conservative-on-guidance, candid-on-history" pattern. One quarter is not a pattern; logged.

### 3D. Promoter Verdict / Management Grade
No material shift warranted from a single call. FLAG-PROMOTER CONCERN (family succession, Rohan Verma JMD) persists. The FY28-target silence is a watch item, not yet a grade-changer. **Management Grade held; provisional this-quarter grade B/C borderline.**

### 3E. Last review's Questions for Management — answer status [cross-protocol, Role 4 Step 8.5]

Pulling v1's 10-question table and marking each against this call:

| v1 Q# | Question topic | Answer Status | What was said |
|---|---|---|---|
| 1 | Q1 consolidated receivables / 6m+ ageing / Gtropy overdraft / write-off containment | **PARTIALLY / EVADED** | Q1 receivables refused ("Q1 we've not given the balance sheet", T33/L78); FY26-end Rs176 Cr confirmed, "majority government"; Gtropy not addressed; write-off called one-time (T29/L70) |
| 2 | Margin bridge ex-write-off; blended-margin guide as IoT scales | **ANSWERED SPECIFICALLY** | Ex-write-off margin "43 plus" (T12/L34); full-year guide "35% plus" (T14/L38) |
| 3 | Treasury capital-allocation plan; PAT sustainability if rates fall | **NOT ADDRESSED** | No allocation plan given; OI discussed only as write-back mechanism (A3-17) |
| 4 | Government +9.2% vs stated 11%; seasonality vs demand | **PARTIALLY** | "slow starter, Q1 weakest" (T17/L45); number not reconciled/quantified |
| 5 | Consol-below-standalone; Gtropy standalone P&L; Nil-revenue subsidiary | **EVADED** | "not much value in analyzing standalone" (T17/L45); no Gtropy P&L; subsidiary not identified |
| 6 | Rohan Verma JMD scope/timing; Mappls DT WTD departure | **PARTIALLY** | JMD focus areas discussed (T6/L22); WTD departure not mentioned |
| 7 | Order book & intake; FY28 Rs1,000 Cr target | **PARTIALLY** | Order book Rs1,750 Cr given (T19/L49); intake/mix withheld; FY28 target silent |
| 8 | ETR / DTA shield exhaustion | **NOT ADDRESSED** | No tax discussion |
| 9 | A&M/C&E → AEG mapping bridge; no reclass confirmation | **NOT ADDRESSED** | AEG history shown, no bridge (A3-20) |
| 10 | Consolidation roster / Gtropy stake / entity name | **NOT ADDRESSED** | No consolidation-roster discussion |

**Answered-status tally:** 1 specific, 4 partial, 3 not-addressed, 2 evaded. The two EVADED (receivables number; standalone/Gtropy) are the thesis-critical ones and are carried forward. Repeated evasion of the receivables number is logged as an emerging governance signal (first instance under the protocol).

🛑 3A–3E shown. Credibility ratio provisional 50% (Grade B/C borderline, first data point); one DROPPED logged.

## STEP 4 — Q&A DECOMPOSITION (60%+ of effort)

### 4A. Q&A inventory (33 question turns condensed to the 7 questioners; response quality per exchange)

| # | Analyst & Firm | Question (1-line) | Category | Response Quality | Substance |
|---|---|---|---|---|---|
| Q1 | Anmol G, DA Capital | JMD focus; auto-OEM contract time-shift; write-off detail & recoverability; can margin run 43–44% | Strategic / Operational / Financial | B / B / **A** (write-off) / B | Write-off geometry surfaced here; auto time-shift dated to H2 |
| Q2 | Amar Maurya, Lucky Investment | Why is core (map-led) not growing; forward growth given govt backlog | Financial / Strategic | B / C | Steered to consolidated; order book Rs1,750 Cr; deflected quarter-on-quarter |
| Q3 | (Ahmed?), HDFC Securities | Order-book AEG mix; e-commerce deal; govt receivables mix & further write-off risk; Q1 receivables number | Customer / Financial | C / **D on receivables number** | Amazon Now name-drop; order-book mix refused; receivables number refused |
| Q4 | Gautam Rathi, CWC | Reconcile 80 lakh net vs 4% margin impact; international; IoT services seasonality | Financial / Clarification | **A** (reconciliation) / B / C | Forced the write-off geometry into the open; IoT seasonality unresolved ("I'll take it offline") |
| Q5 | Abhishek Jain, Chris PMS | Automotive 2W/PV/CV mix; revenue per vehicle; share at Maruti/Hyundai/Mahindra; FY27 auto target | Operational / Forward | C / D / **E on target** | Repeated non-disclosure; "we are the supplier there"; refused quantitative target |
| Q6 | Pranay Jain, Banyan Tree | Contract tenure/pricing structure; wallet-share expansion | Strategic | B / B | Pointed to deck; "no typical" tenure (5yr–1yr); wallet-share qualitative |
| Q7 | (Jamoshi/Jayesh), Chris PMS | Lower gross margin cause (mix); digital-twin / Naksha role | Financial / Strategic | B / B | Confirmed mix-driven; digital-twin "calibrated" on receivable quality |

### 4B. Question-pattern analysis
- **Most-repeated question:** the **write-off**, asked by three different analysts (Q1, Q3, Q4). Repeated asking = the market distrusted the headline "4% margin impact" until the geometry (Rs4 Cr opex / Rs3.2 Cr other income / Rs0.80 Cr net) was extracted by Gautam Rathi. This is the single most thesis-relevant exchange.
- **Consistently graded C/D/E:** anything requiring a **forward number or a receivables number** — automotive target (E), per-vehicle pricing (D), Q1 receivables (D), order-book mix (C). The topic management does not want quantified is *forward guidance and receivables*.
- **Buy-side vs sell-side:** strong buy-side presence (Lucky, CWC, Banyan Tree, Chris PMS = AIF/PMS), which asked the sharpest questions (Gautam's reconciliation; Amar's core-growth challenge). HDFC Securities (sell-side) asked the receivables-mix question. Healthy engagement; not an orchestrated call.
- **Hosting-broker softball?** Arhant (host) did not lead Q&A with softballs; the first questioner was a buy-side analyst (DA Capital) who went straight at the write-off. Not orchestrated.
- **Pushback?** Yes — Gautam Rathi explicitly pushed back on the "4% margin impact" framing ("there is some disconnect right"), and Amar Maurya pushed back on core-growth ("the map-led growth... is basically very very flat"). Both are genuinely contested topics.

### 4C. The three most important Q&A exchanges

**Exchange 1 — the write-off geometry (Gautam Rathi, CWC; T36–T43 / L85–L99).**
- Q (verbatim, condensed): "the press release / presentation says EBITDA margin was impacted by 4% due to this 4 crore one-time write off... there is some disconnect right."
- A (verbatim, condensed): "Approximately 4 crores was the receivable... back to back there was a payment for 3.2 cr... I don't have to make that payment... the accounting treatment of that has been net 80 lakhs... that write off has gone into the other expense, and that payback... has gone as an other income."
- **Said specifically:** Rs4 Cr write-off in other expenses (inside EBITDA); Rs3.2 Cr write-back in other income (below EBITDA); net Rs0.80 Cr.
- **NOT said:** the identity of the government customer; whether the Rs3.2 Cr payable was to a *related* party; why a Rs4 Cr receivable had a near-matching Rs3.2 Cr payable "back to back" (an unusual pairing that itself invites a question).
- **Implies for thesis:** the reported 40.2% margin and +43.7% other income are both distorted by one-time items in opposite directions — the **[v2 CORRECTION]** underlying walk (Step 4B) is entirely built on this exchange. Underlying operating EBITDA +7.6%, core PBT +5.4%. The genuine mix compression is ~287 bps, half the headline.
- **Follow-up we would ask:** "Was the Rs3.2 Cr offsetting payable owed to the same government counterparty or a subcontractor, and is any part of it also at risk?"

**Exchange 2 — receivables: the binding falsifier (HDFC Securities; T30–T34 / L72–L80).**
- Q: "what part of the overall receivables would be from government contracts as of the end of this quarter?"
- A: "Q1 we've not given the balance sheet... the majority of the receivable will be from government — not like a large majority, but a majority... 176 crores was the total at the end of FY26."
- **Said specifically:** FY26-end total Rs176 Cr; majority government (not large majority).
- **NOT said:** the 30-Jun-2026 receivables number (the binding falsifier), the ageing, the government sub-total in rupees.
- **Implies for thesis:** the falsifier stays unresolvable, but the root cause is now government (not Gtropy) — a structural cash-cycle lengthening as government scales (A3-02). **Mild adverse.**
- **Follow-up:** "In rupee terms, what was the government receivable at FY26-end, and what is your internal DSO target for government contracts?"

**Exchange 3 — full-year margin guide vs the ex-write-off number (Anmol, DA Capital; T13–T14 / L36–L38).**
- Q: "can we expect that our EBITDA over the next couple of quarters could be in this 43–44% kind of range?"
- A: "we have always been saying that we have kept the target for us to do a 35% plus for the whole year. So quarter by quarter you'll have to see."
- **Said specifically:** full-year FY27 EBITDA margin target 35%+.
- **NOT said:** any confirmation that 43% is sustainable; any half-year split.
- **Implies for thesis:** management guides **below** both reported (40.2%) and underlying (~43%), signalling H2 blended dilution as low-margin IoT hardware scales. Confirms the mix-drift read; watchlist item 4 goes red on the full-year guide.
- **Follow-up:** "If Q1 underlying was 43% and the full year is 35%+, what H2 blended margin are you implicitly guiding to, and what IoT hardware revenue share drives it?"

🛑 4A, 4B, 4C shown.

## STEP 5 — NEW INFORMATION AUDIT

### 5A. New disclosures

| Disclosure | Type | Material? | Thesis impact |
|---|---|---|---|
| Write-off geometry: Rs4 Cr opex / Rs3.2 Cr other-income / Rs0.80 Cr net (T37/L87) | Negative surprise clarified | **YES** | Enables the underlying-vs-reported correction; the single most important new datum |
| Open order book **Rs1,750 Cr** (from Rs1,500 / Rs1,350 Cr) (T19/L49) | Customer/Order | **YES** | Fills the deck's missing order-book (MMI-07); a visibility positive |
| Receivables root cause = **government** ("majority", "longer cycle") (T29/L70, T34/L80) | Financial | **YES** | Reframes FLAG-CASH from Gtropy to government; mild adverse |
| IoT hardware Rs7 → Rs23 Cr; services Rs16.3 → Rs18 Cr (T45/L103, T51/L115) | Operational | YES | Confirms hardware-first, SaaS-later margin drift |
| Amazon Now powered by MapmyIndia (T24/L60) | Customer win | Moderate | Names a live quick-commerce deployment |
| Auto OEM volume "time-shift" dated to **H2** (T10/L30) | Operational | Moderate | Weaker H2 FY26 auto base → possible H2 FY27 YoY tailwind (two-sided) |
| Automotive AEG history: Q1 Rs26→46→59 Cr; FY Rs182→190 Cr (T10/L30) | Backward | Moderate | Confirms auto +29% YoY; modest FY25→FY26 auto growth |
| Defense & oil-and-gas "green shoots" in government (T6/L22) | Forward catalyst | Moderate | Named government growth vectors (unquantified) |
| International/SE-Asia JV loss "reduced" but "not material" (T53/L119) | Segment | Low | International remains immaterial, self-uncertain |

### 5B. What Was NOT Discussed (F17 silence audit — mandatory)

| Expected topic | Why it should have been discussed | Significance of silence |
|---|---|---|
| **FY28 Rs1,000 Cr revenue target** | Growth trigger of the thesis; a direct forward-growth question was asked (T18/L47, T20/L51) | **AMBER→RED** — silent across deck, PR **and** call; a soft-dropped prior target (A3-16) |
| **Idle-treasury / capital-allocation plan** | Rs745 Cr cash, +Rs60 Cr QoQ; monitoring item 10; PAT increasingly treasury-linked | **RED** — no plan; OI mentioned only as the write-back mechanism (A3-17) |
| **Gtropy** (overdraft / 6m+ ageing) | The entity the Notion checklist tied receivables risk to; monitoring item 3 | **AMBER** — never spoken once; receivables narrative re-pointed to government (A3-18) |
| **ClarityX / Zenithra RPT ceiling** | Monitoring item 6; related-party governance | **AMBER** — no RPT discussion of any kind (A3-19) |
| **Government YoY growth number** | Monitoring item 1 (15–20% target); segment now identified as receivables driver | **AMBER** — only "slow starter / Q1 weakest" seasonality; number withheld (A3-21) |
| **A&M/C&E → AEG restatement bridge** | Segment basis changed this quarter; old/new not reconcilable without it | **AMBER** — AEG history shown, mapping bridge not provided (A3-20) |
| **Mappls DT WTD (Nikhil Kumar) departure** | A board-outcome governance item in the filing (F13-1) | AMBER — not raised by management or analysts |

**Silence interpretation:** the cluster of silences on the exact thesis-critical items (FY28 target, treasury plan, government number, receivables) is a **confirmatory negative** — sustained silence on a deteriorating cash-conversion metric is, per Role 5, a governance signal. It does not fire a trigger, but it removes any benefit-of-the-doubt.

🛑 5A and 5B shown.

## STEP 6 — TONE & SPECIFICITY ANALYSIS

### 6A. Tone comparison (vs prior written commentary — no prior concall exists)

| Topic | Prior (deck/PR) phrase | This call phrase | Direction |
|---|---|---|---|
| Government | "seasonally soft" (deck MMI-11) | "slow starter... Q1 generally the weakest" + "we also have to be careful" on receivables | DOWNGRADED (added caution) |
| Margin | "EBITDA remained strong" (deck MMI-05) | "35% plus for the whole year" (guides below reported) | DOWNGRADED (forward guide below current) |
| Order book | absent from deck (MMI-07) | "Rs1,750 Cr... grown healthily... strong visibility" | UPGRADED (now disclosed, growing) |
| Receivables | not framed | "far better than peer companies" + "longer cycle" + "good vs bad receivables" | MIXED (reassurance + admitted constraint) |
| FY28 target | in prior Notion thesis | (silent) | DROPPED |

### 6B. Specificity score
- Quantified forward statements: ~1 hard (35%+ FY27 margin) [order book Rs1,750 Cr is a disclosed stock, borderline].
- Unquantified/refused forward statements: ~7 (automotive target refused, digital-twin "calibrated", IoT SaaS "in time to come", green shoots, international "be patient", wallet-share qualitative, "keep winning orders").
- **Specificity ratio ≈ 1 / 8 ≈ 0.13 → <0.3 = HEAVY HEDGE / low-specificity call.**

### 6C. Defensive-language count (≥5 = hedge-heavy)
"I don't have it... I don't remember" (T31/L74); "I'm trying to remember" (T33/L78); "I'm guessing" (T53/L119); "for competitive reasons... not disclosing" (T27/L66); "it's all competitive information" (T62/L138); "there's no typical" (T73/L161); "not going to talk about quantitative target" (T68/L150); "quarter by quarter you'll have to see" (T14/L38); "I'll take it offline" (Gautam, but management effectively closed the IoT-seasonality thread). **Count ≈ 8–9 → hedge-heavy call.**

### 6D. Confidence indicators
- Promoter (Rakesh Verma) on the call answering the technical accounting reconciliation directly and volunteering the "80 lakhs net" figure — a genuine candour positive.
- Order book given with a 2-year trend (Rs1,350 → Rs1,500 → Rs1,750 Cr) — specific, testable.
- Named customer deployments (Tata Sierra EV, Suzuki, Vespa, Ultraviolette, Ampere, VinFast, Amazon Now).
- Honest acknowledgment of the government receivables constraint rather than denial.

### 6E. Management archetype — Specificity × Credibility 2×2
- Specificity ratio 0.13 (≤0.5).
- Trailing credibility: provisional (first concall); this-quarter grade B/C borderline (~50% raw on a 2-item sample) — treated as ≥ the C boundary given the write-off candour and order-book delivery.
- **Archetype: MEASURED (low-specificity) with candour-under-pressure — provisionally MEASURED & CREDIBLE, NOT Overpromiser.** The call is hedge-heavy but NOT hyper-specific-with-poor-delivery; the one hard commitment (35%+) is conservative and the promoter reconciled the write-off honestly. **Flag:** the FY28-target silence is the blemish that could tip the archetype toward EVASIVE if repeated. Not the danger quadrant this quarter.

🛑 6A–6E shown.

## STEP 7 — CROSS-REFERENCE vs FILING AND PEER CONCALLS

### 7A. Concall narrative vs filing numbers

| Concall claim | Filing evidence | Reconciliation |
|---|---|---|
| "Revenue up 14.9% to Rs139.7 Cr" (T3) | Rev 121.61 → 139.72 (line 226) | **CONFIRMED** |
| "EBITDA 56.1 Cr, margin 40.2%" (T3) | Operating EBITDA 56.12, 40.2% (derived) | **CONFIRMED** (deck EBITDA = operating EBITDA) |
| "PAT up 8.6% to 49.7 Cr, PAT margin 31.2%" (T3) | PAT 49.74 (line 251); 31.2% = PAT/Total Income | **CONFIRMED** (note non-standard margin denominator) |
| "would have been 43 plus" ex-write-off (T12) | 56.12 + 4.0 = 60.12 → 43.0% (Step 4B) | **CONFIRMED** (arithmetic ties) |
| "net effect only 80 lakhs" (T12) | 4.0 opex − 3.2 other income = 0.80 (Step 4B) | **CONFIRMED** (ties to the +43.7% OI line) |
| "map-led 98.2 → 98.7 Cr" (T17) | Deck line 399/408 Map-led | **CONFIRMED** (~+0.5%) |
| "IoT-led 23.4 → 41 Cr" (T17) | Deck IoT-led Rs41.1 Cr (MMI-04) | **CONFIRMED** |
| "order book 1,750 Cr" (T19) | Absent from filing/deck (MMI-07) | **UNVERIFIABLE** (not in any filed document; concall-only) |
| "receivables far better than peers" (T29) | No receivables in filing | **UNVERIFIABLE** (no peer, no metric) |
| "176 Cr total at FY26-end, majority government" (T34) | FY26 close; no split filed | **PARTIALLY CONFIRMED** (Rs176 Cr consistent with Notion Rs176.4 Cr; government split unfiled) |

**Key reconciliation:** the concall narrative *confirms* the filing numbers and, crucially, *explains* the distortion in them. The "strong EBITDA" narrative is technically true and was materially incomplete until the write-off geometry was forced out — the classic Role 5 case where a claim is true and misleading at once, resolved here by analyst pushback.

### 7B. Peer concall cross-check
**No peer concall was supplied for this run, and MapmyIndia has no close listed pure-play peer in the analysed universe** (Indian deep-tech mapping / geospatial is effectively single-name). Stated explicitly per protocol: peer cross-check N/A this quarter. The one indirect peer signal is management's own unverifiable "receivables far better than peer companies" and "we've seen that issue [bad receivables] play out in the peer companies" (T29/L70, T82/L180) — an admission that government-receivable stress is a known sector pattern, not company-specific.

### 7C. Concall vs industry channel checks
No third-party channel data (rating-agency, industry-body) was supplied this run. N/A.

🛑 7A, 7B, 7C shown.

## STEP 8 — UPDATE THESIS & POSITION DECISION (concall overrides)

### 8A. Growth-trigger status (post-concall) — see Section A 6D for the full table
Net: Map-core marginal ON TRACK; IoT ON TRACK but margin-dilutive; government DELAYED/WEAKENED (green shoots vs longer cash cycle); order-book-led FY28 target DELAYED (order book up, target silent); treasury deployment DEAD/STALLED.

### 8B. Watchlist items — concall-specific updates
- Item 4 (blended margin): full-year guide **35%+** pushes this RED on the forward view despite Q1 at 40.2%.
- Item 8 (FY28 target): **silent** → RED.
- Item 10 (treasury): **silent** → RED/worsening.
- Item 9 (succession): JMD executing → ADDRESSED.
- Item 2 (receivables): reframed to government, still UNKNOWN/AMBER-adverse.

### 8C. Thesis-broken trigger check (post-concall)
No condition FIRED (Section A 6C). The concall did **not** fire any trigger; it improved the underlying operating read and mildly worsened the receivables read.

### 8D. Four-Pillar inputs — concall adjustments
No pillar hard-updates (no balance sheet). Forward colour: (Pillar 1 ROCE) D&A +33% mild pressure, hold; (Pillar 2 cash) government cash-cycle lengthening + Rs4 Cr write-off, hold capped INDETERMINATE; (Pillar 3 EM) order book Rs1,750 Cr a small positive vs the deck's silence; (Strategic Premium) hold. **No destination-PE recompute; Hurdle Ratio STOP unchanged.**

### 8E. Position decision (Role 5 overrides applied)
- Credibility ratio **provisional 50%** (first concall, 2-item sample) — below the 60% line on the raw number → per the override, treat management commentary cautiously and anchor to filing numbers. This is *already* the posture (WATCHLIST/AVOID, filing-anchored). No incremental action.
- **One DROPPED** (FY28 target) this window — the two-DROPPED automatic-downgrade rule has NOT fired.
- **No undisclosed material risk** revealed (the write-off was already in the deck; the concall clarified it favourably on the underlying basis).
- **No undisclosed material positive** large enough to add on (order book Rs1,750 Cr is confirmatory, not thesis-changing at a ~47x price).
- **Narrative did not contradict the filing** — it confirmed and explained it.

**Position decision: HOLD at WATCHLIST / AVOID. Net concall impact on thesis: MAINTAINED — slightly better on operating quality (the ex-one-time correction), unchanged on the two overhangs (cash INDETERMINATE; promoter/family control). Entry zone unchanged (Rs690–700). Master gate: Q2 FY27 H1 balance sheet.**

### 8F. Updated Questions for Management (forward) — see the consolidated table below (Section: Updated Questions for Management)

🛑 8A–8F shown.

---

# SECTION C — COMBINED VERDICT (Role 4 + Role 5)

- **Filing-derived signals:** Revenue +14.9% YoY (real top-line beat). *Reported* operating EBITDA flat (+0.4%), margin −574 bps, core operating PBT −2.9%, other income +43.7% (29.6% of PBT). Standalone-vs-consolidated PAT gap −10.2% (subsidiary block loss-making). Auditor unmodified. No balance sheet → **cash INDETERMINATE**; falsifier unresolvable; Rs4 Cr government write-off.
- **Concall-derived signals [v2, NEW]:** the write-off geometry (Rs4 Cr opex / Rs3.2 Cr other income / Rs0.80 Cr net) shows **~half the margin compression and the entire reported core-PBT decline are one-time**. On the underlying basis, **operating EBITDA +7.6%, core operating PBT +5.4%, recurring other income +~20%.** Order book **Rs1,750 Cr** reaffirmed (up from Rs1,500 / Rs1,350 Cr). Full-year margin guide **35%+** (below reported and underlying → H2 dilution). Receivables root cause **reframed Gtropy → government** ("majority", "longer cycle"), a mild-adverse cash confirmation. FY28 Rs1,000 Cr target, treasury plan, Gtropy, RPT ceiling all **silent**.
- **Reconciliation between the two:** the concall **confirms and explains** the filing. The reported compression is real for valuation purposes, but the concall shows roughly half of it is non-recurring — so v1's "PAT is treasury-financed / core declined" is **corrected on the underlying basis to core +5.4%**, while the reported anchor (and the fact that the write-off is a realized collection failure) is retained conservatively. No narrative-vs-filing contradiction; the earlier "narrative flattering the numbers" gap (deck "strong EBITDA") was resolved by analyst pushback on the call.
- **Net thesis impact: MAINTAINED** — slightly better on operating quality, unchanged on the two overhangs. Nothing fired a thesis-broken trigger; nothing cleared cash or governance.
- **Position decision: HOLD at WATCHLIST / AVOID**, nil at CMP (~Rs1,185, ~47x trailing, Hurdle STOP), entry unchanged Rs690–700, master gate Q2 FY27 H1 balance sheet.
- **Protocol verdict: PROCEED WITH CAVEATS** — capped by INDETERMINATE cash conversion (house rule). Caveats named: unresolved receivables/ageing; government-receivable cash-cycle lengthening + Rs4 Cr realized write-off; subsidiary drag (−10.2% gap); full-year margin guide 35%+ (H2 dilution); FY28 target / treasury plan silent; order-book mix and receivables number withheld.

---

# UPDATED QUESTIONS FOR MANAGEMENT [v2 — concall-refreshed]

Every A3 FORWARD-SIGNAL and AMBIGUOUS finding (results, deck, press AND concall) generates at least one question. Concall-answered items are dropped or marked-answered; unresolved items are kept; the call raised new ones. Channel: the next concall / IR email / AGM (Rohan Verma ratification forum). Ordered by thesis materiality.

| # | Question | Why it matters (finding IDs) | Bull answer | Bear answer | Status vs v1 |
|---|---|---|---|---|---|
| 1 | At 30-Sep-2026 (H1 balance sheet), what are **consolidated trade receivables**, the **government sub-total in rupees**, and the **6-month-plus ageing**? Is the Rs4 Cr write-off contained? | BF, A3-01, A3-02, MMI-06 | Receivables <Rs176 Cr, govt ageing stable, write-off isolated | Receivables >Rs176 Cr, govt 6m+ widening, more govt impaired | **KEPT & sharpened** (receivables root cause now government) |
| 2 | The Rs4 Cr receivable had a "back-to-back" Rs3.2 Cr payable. Was that payable owed to the **same government counterparty or a subcontractor/related party**, and is any of it also at risk? | A3-04, A3-05, A3-06 | Unrelated arm's-length subcontractor; fully settled | Related/circular exposure; further risk | **NEW** (raised by the call's geometry) |
| 3 | You guide FY27 EBITDA margin to **35%+** while Q1 underlying was ~43%. What **H2 blended margin** does that imply, and what **IoT hardware revenue share** drives the dilution? | A3-07, A3-12, F12-1, MMI-04 | H2 blend ≥38%; IoT SaaS uplift offsets hardware | H2 blend <35%; structural dilution as IoT scales | **KEPT & sharpened** (now anchored to the 35%+ guide) |
| 4 | Cash is **Rs745 Cr (+Rs60 QoQ)** with no allocation plan, and FY28 Rs1,000 Cr was not mentioned. What is the **capital-allocation plan**, and is the **FY28 Rs1,000 Cr target still in place**? | A3-16, A3-17, MMI-10, MMI-12, F2-2 | Concrete buyback/dividend/M&A; target reaffirmed with pacing | No plan; target quietly abandoned | **KEPT** (both still silent after the call) |
| 5 | Government is now a "**majority**" of receivables on a "**longer cycle**". What is your internal **DSO target for government**, and how do you gate digital-twin / Naksha pursuit on "good vs bad receivables"? | A3-02, A3-03, A3-13 | Defined DSO discipline; selective, cash-positive pursuit | No DSO target; growth chased into weak collections | **NEW** (call reframed receivables to government) |
| 6 | Consolidated PAT (Rs49.74 Cr) is **below** standalone (Rs55.42 Cr), a 19.5 pp QoQ swing. Provide **Gtropy's standalone P&L** and identify the **Nil-revenue, Rs0.11 Cr-loss unreviewed subsidiary** (line 169). ("Look at consolidated" does not resolve which subsidiary drags.) | F2-1, F3-1, A3-18 | Gtropy turning; shell dormant wind-down | Gtropy losses widening; unexplained loss vehicle | **KEPT** (evaded on call — mgmt deprecated standalone analysis) |
| 7 | Provide the **A&M/C&E → AEG mapping bridge** and confirm **no revenue was reclassified** between segments in the restatement. | A3-20, MMI-01, F16-1 | Clean bridge; no reclass | No bridge; reclass flattered a weak segment | **KEPT** (not addressed on call) |
| 8 | Order book is **Rs1,750 Cr** (up from Rs1,500 / Rs1,350 Cr). Provide the **AEG segment mix** and **new-order intake value** (withheld "for competitive reasons"). | A3-14, MMI-07 | Government/enterprise mix healthy; intake growing | Mix concentrated / intake flat | **KEPT & downgraded** (aggregate given; mix still withheld) |
| 9 | Confirm the **ClarityX / Zenithra RPT ceiling** (Rs24 Cr) utilisation and any FY27 RPT — no RPT was discussed on the call. | A3-19, Notion item 6 | Low utilisation, arm's-length | Near cap / opaque | **KEPT** (silent on call) |
| 10 | ETR was **24.2%**, below the 25.17% statutory rate on deferred-tax credits. When does the **DTA shield exhaust** and ETR normalise? | F8-2 | Shield persists; ETR stable | ETR steps to 25%+, cutting PAT | **KEPT** (not addressed on call) |
| 11 | The auto-OEM volume "time-shift" is dated to **H2 FY26**. Will the weaker H2 base lift H2 FY27 auto YoY, or does the reduction "continue this year"? | A3-08, A3-09 | Weaker base + OEM re-adds vehicles → H2 tailwind | Reduction continues; no re-add contract | **NEW** (call dated the time-shift) |
| 12 | Why did **Mappls DT WTD (Nikhil Kumar)** step down with reason "NA", who succeeds him, and when is the **Rohan Verma JMD shareholder ratification**? | F13-1, MMI-08, A3-22 | Orderly succession; ratification scheduled | Leadership gap; concentration of family control | **KEPT** (JMD partial; WTD not raised) |

*(Neutral-fact / already-answered: v1 Q4 government 11%-vs-9.2% reconciliation is partially answered ("Q1 weakest", still unquantified — folded into Q5/Q1). v1 Q2 margin-bridge ex-write-off is ANSWERED ("43 plus", 35%+ guide) — dropped as a standalone question, its forward leg becomes Q3.)*

**Top 3 by likelihood of producing thesis-changing information:**
1. **Q1 (H1 receivables / government sub-total / ageing)** — resolves the binding FLAG-CASH falsifier; a bear answer fires the thesis-broken condition.
2. **Q3 (H2 blended margin implied by 35%+ guide)** — confirms whether the mix compression is structural; sets Pillar-1/2 direction.
3. **Q4 (treasury plan + FY28 target status)** — tests capital-allocation transparency and whether a prior growth target has been abandoned; a vague answer is itself diagnostic.

**Channel recommendation:** next concall (highest priority for Q1/Q3/Q4 in live Q&A) + IR email with all 12 verbatim; prioritise governance items (Q9, Q12) for the AGM/EGM where the Rohan Verma ratification is tabled.

---

# MONITORABLES / CATALYST LIST (seeded by A3 F6 commitment registers + F13 board items) [v2 — concall-updated]

| Item | Implied date | Source ref | Type / watch |
|---|---|---|---|
| **Q2 FY27 results with mandatory H1 balance sheet + cash flow** (resolves FLAG-CASH falsifier) | ~Nov 2026 | Reg 33; Step 5 / BF | **CATALYST — highest priority.** Receivables vs Rs176 Cr, government 6m+ ageing, CFO/PAT |
| **Full-year FY27 EBITDA margin "35% plus"** — test vs H2 print | FY27 year-end | Concall T14/L38 (A3-07) | CATALYST — confirms/denies H2 blended dilution |
| **Rs4 Cr government write-off — test recurrence** | Q2 FY27 | Concall T12/L34, T29/L70 (A3-04) | Watch — collection-quality confirm/deny |
| **Order book Rs1,750 Cr → revenue conversion**; annual fixed/volume split | Next annual disclosure | Concall T19/L49, T27/L66 (F6) | Watch — visibility-to-revenue conversion track record |
| **FY28 Rs1,000 Cr target** — reaffirm or confirm dropped | Next concall | Concall silence (A3-16); MMI-10 | Watch — soft-dropped; re-ask |
| **Idle-treasury / capital-allocation plan** | Undated (overdue) | Concall silence (A3-17); MMI-12 | Watch — Rs745 Cr, no plan |
| **Rohan Verma Joint MD — shareholder ratification** | Next AGM/EGM, FY27 | Concall T3/L12 (A3-22); deck s4; press L136 | CATALYST — governance; scope vs Rakesh Verma |
| **Nikhil Kumar cessation as WTD, Mappls DT (Material WOS)** — successor | Effective 2026-08-03; successor TBD | Results line 53; Annexure-B (F13-1) | Watch — leadership gap at the "DT" WOS |
| **AEG segmental reporting live; A&M/C&E → AEG bridge owed** | Commenced Q1 FY27 | Concall T3/L12, T10/L30 (A3-20); MMI-01 | Watch — request restatement mapping |
| **Auto-OEM volume time-shift (H2-dated) — H2 FY27 base effect** | H2 FY27 | Concall T10/L30 (A3-08) | Watch — potential auto YoY tailwind or continued reduction |
| **Defense / oil-and-gas government "green shoots"** | Near-term, undated | Concall T6/L22 (A3-10) | Watch — government growth vectors (same pipeline as receivables risk) |
| **IoT hardware→SaaS margin uplift** | Billing-cycle dependent | Concall T47-51 (A3-12) | Watch — SaaS margin kick-in |
| **FY26 AR / AGM** — RPT ceiling, receivables ageing, Gtropy stake, entity roster | FY27 AGM | Notion items 3/6/10; F15-1; A3-19 | Watch — resolves items 3, 6, 10 |

---

# MANDATORY PLAIN-LANGUAGE BRIEF (four labelled parts) [v2 — refreshed for the concall]

## Part 1 — SUMMARY NARRATIVE

MapmyIndia's June-2026 quarter looked weak on the surface and is better once you understand one accounting item. Consolidated revenue rose 14.9% to Rs139.7 Cr [this quarter's filing, line 226; confirmed on the concall, T3/L12], a real improvement on last year's 2.3% pace. The reported operating margin fell hard, from 45.9% to 40.2% [derived], and reported core operating profit fell 2.9%. But on the call management explained the geometry of a Rs4 Cr write-off on a government customer: the Rs4 Cr charge sits in operating expenses (inside EBITDA), while an offsetting Rs3.2 Cr payment the company no longer owes was booked in other income (below EBITDA), so the *net* hit to profit was only about Rs0.80 Cr [T12/L34, T37/L87, T39/L91]. Strip that one-time item out and the picture flips: underlying operating EBITDA was up about 7.6%, the underlying margin was about 43% (management's "43 plus"), and underlying core operating profit was up about 5.4%, not down 2.9% [Step 4B walk]. This is the single most important correction versus our first read: the business itself grew; the reported softness was mostly a one-off. Two cautions stay firmly in place. First, that write-off is still a real, realized collection failure on a government customer, and management confirmed government is now the "majority" of receivables and runs "a longer cycle" [T29/L70, T34/L80] — so the cash-quality worry moves from the Gtropy subsidiary (our earlier assumption) to government receivables. Second, and decisively, this was a P&L-only filing with no balance sheet; management confirmed on the call "Q1 we've not given the balance sheet" [T33/L78], so the one number that would settle our thesis — are receivables above Rs176 Cr and is old debt piling up — still cannot be answered and moves to the Q2 results (~Nov 2026), which must by law carry a half-year balance sheet. Elsewhere: the order book was disclosed on the call at Rs1,750 Cr, up from Rs1,500 Cr and Rs1,350 Cr [T19/L49], a genuine visibility positive; but the full-year margin guide is only "35% plus" [T14/L38], below both the reported and underlying Q1 numbers, which signals margin dilution in H2 as low-margin IoT hardware scales; the FY28 Rs1,000 Cr revenue target was not mentioned at all despite a direct question about future growth; and there is still no plan for the Rs745 Cr cash pile. For the decision: the stock stays WATCHLIST / AVOID, nil at ~Rs1,185 (about 47x trailing earnings, well above the 32x we would pay), entry only near Rs690–700, and only once Q2 shows receivables under control. Nothing this quarter fired a sell trigger; the operating read improved on the one-time correction; the two overhangs (cash quality and promoter/family control) are unchanged. Cash conversion stays INDETERMINATE, so the verdict is capped at PROCEED WITH CAVEATS. Provenance: financial figures and the write-off geometry from this quarter's filing/deck/concall; valuation anchors from prior Notion work.

## Part 2 — SECTOR INTELLIGENCE

MapmyIndia sells digital maps, geospatial software, location APIs, and IoT/telematics hardware into three end-markets it now labels Automotive, Enterprise, and Government (a reporting change made this quarter, replacing the old A&M/C&E split [deck slide 10; concall T3/L12]). The demand read is uneven: Automotive grew ~29% YoY [Rs45.7 → 58.98 Cr, T17/L45], driven by connected-mobility and EV wins (Tata Sierra EV, Suzuki, Vespa, Ultraviolette, Ampere, VinFast named on the call, T57/L130); Enterprise grew ~6% [Rs60.6 → 64 Cr]; Government — a structurally lumpy, tender-driven, slow-paying customer base — was described as "a slow starter... Q1 generally the weakest" [T17/L45] and its YoY number was not quantified on the call. The sector's classic risk showed through plainly: management admitted government is now the majority of receivables on "a longer cycle", took a Rs4 Cr write-off on a government customer, and said it will be "calibrated... good receivables versus bad receivables" on new government digital-twin/Naksha work because "we've seen that issue play out in the peer companies" [T82/L180] — an explicit acknowledgment that government-receivable stress is a sector-wide pattern, not company-specific. The structural tailwind is AI plus India's digital-mapping sovereignty (indigenous maps, defence, oil-and-gas, PSU digital-twin/Naksha projects); management framed a heavy "AI-native" push [T4/L15], a genuine multi-year demand driver but also an opex commitment that pressures margin. Payer mix is the swing factor: the more the mix tilts to government and to low-margin IoT hardware, the more the sector's cash-conversion and margin profile deteriorates. Provenance: segment growth, customer names and the government-receivable characterisation from this quarter's concall/deck; the AI/sovereignty tailwind framing from prior Notion sector work; no third-party channel data or peer concall was supplied this run.

## Part 3 — BUSINESS-MODEL INTELLIGENCE

The company makes money two ways with very different economics. The **Map-led** business (maps, navigation, analytics, GIS/digital-twins, sold as licences and subscriptions — MaaS/SaaS/PaaS) is the profit engine: Rs98.7 Cr revenue this quarter at ~51% EBITDA margin [deck; concall T17/L45], but it grew only ~0.5% YoY and an analyst on the call called it "very very flat" [T20/L51]. The **IoT-led** business (GPS telematics, dash-cams, trackers, plus mobility/logistics SaaS) is the growth engine but structurally lower-margin: Rs41 Cr revenue, up ~75% YoY, at ~13% EBITDA margin. Management confirmed the model mechanic on the call: IoT is "hardware first" (hardware jumped Rs7 → Rs23 Cr) and the higher-margin SaaS "kicks in later" on billing cycles that "might be yearly... two-yearly... monthly" [T45-51/L103-115]. So the model trades margin for growth now, with a margin recovery that is real but un-dated. This quarter shows the drift: IoT's revenue share rose from ~19% to ~29%, and because it earns roughly a quarter of the Map-led margin, the blended margin fell — about half of the 574 bps reported fall is this genuine mix drift, the other half is the one-time write-off. Two more model facts: first, reported profit leans on treasury (other income was 29.6% of pre-tax profit as reported, though about a fifth of the jump was the one-time write-back, so recurring treasury dependence is nearer 25%), and the Rs745 Cr cash pile has no allocation plan; second, value creation is concentrated in the standalone parent — the consolidated subsidiaries (notably Gtropy, the ~96%-owned IoT arm, though it was never named on the call) were a net drag this quarter, pulling consolidated PAT below standalone. Unit-economics summary: a high-margin, high-retention but barely-growing software core, wrapped around a fast-growing thin-margin hardware/telematics business whose SaaS tail is the future margin story, funded by a large idle cash balance. Provenance: product-segment margins and the hardware-to-SaaS mechanic from this quarter's concall/deck; Gtropy stake and treasury history from prior Notion work (Gtropy not re-disclosed this quarter).

## Part 4 — COMPETITION INTELLIGENCE

MapmyIndia's structural moat is its proprietary, continuously updated India map database (building/address level, 30+ years of accumulation), an indigenous-data and defence/PSU trust position that global players (Google Maps, HERE, TomTom) cannot easily replicate for sovereign and regulated Indian use-cases, and named OEM design-wins that create switching costs. On the call management leaned on this as "no other company like us... deep tech products in India or even around the world" and a "flywheel" of products x industries [T4/L15] — narrative, not new evidence, and worth reading adversarially. Where it **wins**: high-margin map/API licensing to automotive OEMs and government/defence, where indigenous sourcing and integration depth are decisive — Automotive +29% and named wins (Tata Sierra EV, Suzuki, Vespa, VinFast; Amazon Now for quick commerce, T24/L60) evidence continued OEM/enterprise traction. Where it is **structurally weaker**: the IoT/telematics hardware business competes in a crowded, commoditised, low-margin GPS-device market against many fleet-telematics vendors, which is why that segment runs at ~13% margin and drags the consolidation, and why management is candid that hardware leads and margin only recovers as SaaS builds. Zenrin (3.4% holder) and PhonePe (largest non-promoter holder) are on the register as strategic/financial holders, not head-to-head competitors. The competitive risk to watch: as global map providers push AI-native mapping and low-cost telematics competition intensifies, MapmyIndia must defend Map-led pricing (its whole margin structure depends on it — and Map-led revenue is already flat) while scaling IoT without letting the blend fall below the 38% tripwire, which its own 35%+ full-year guide now sits under. The near-term competitive tells are the government write-off (pricing/collection pressure), the flat Map-led line, and the still-withheld order-book segment mix — the concall confirmed the aggregate order book (Rs1,750 Cr) but declined the mix "for competitive reasons" [T27/L66], so win-rate-by-segment remains unverifiable. Provenance: moat, OEM/enterprise wins and holder identities from this quarter's concall/deck; competitive positioning vs Google/HERE/TomTom and the IoT-commoditisation read from prior Notion competition work; order-book mix and win-rate data were not disclosed.

---

```yaml
stage: A4-analyst
company: "MAPMYINDIA"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
docs_merged: [results, presentation, concall]   # press release also merged (presentation-class); concall NOW present
ledger_reconciliation:
  notes: 16                # results 12 + presentation 4
  turns: 86                # concall
  slides: 17
  questions: 33            # concall
  mgmt_numbers: 46         # concall
  all_reviewed: true
  a3_findings_incorporated: ["F2-1","F2-2","F3-1","F8-1","F8-2","F12-1","F13-1","F14-1","F15-1","BF","MMI-01","MMI-02","MMI-03","MMI-04","MMI-05","MMI-06","MMI-07","MMI-08","MMI-09","MMI-10","MMI-11","MMI-12","F16-1","F16-2","F16-3","F6-1(PR)","F13-1(PR)","F14-1(PR)","A3-01","A3-02","A3-03","A3-04","A3-05","A3-06","A3-07","A3-08","A3-09","A3-10","A3-11","A3-12","A3-13","A3-14","A3-15","A3-16","A3-17","A3-18","A3-19","A3-20","A3-21","A3-22"]
protocol_verdict: "PROCEED WITH CAVEATS"
protocol_verdict_cap_reason: "INDETERMINATE cash conversion caps at PROCEED WITH CAVEATS per house rules; concall confirmed no Q1 balance sheet filed (T33/L78)"
cash_conversion: "INDETERMINATE"
decision_status_verified: "WATCHLIST / AVOID"
position_branch: "8A-W"
net_thesis_impact: "MAINTAINED (slightly better on operating quality via ex-one-time correction; unchanged on cash INDETERMINATE and promoter/family control)"
management_credibility_ratio_provisional: "50% (1.0 / 2 scoreable; first concall under protocol, single data point)"
management_grade_provisional: "B/C borderline"
management_archetype: "MEASURED & CREDIBLE (provisional; low specificity 0.13, candour under pressure; NOT Overpromiser)"
dropped_commitments_this_window: ["FY28 Rs1,000 Cr revenue target (silent despite direct forward-growth question, A3-16)"]
sc_gap_pat_pct: ["Q1FY26: -9.0%","Q4FY26: +9.3%","Q1FY27: -10.2%","FY26: -2.8%"]
underlying_vs_reported_correction:
  reported: {op_ebitda_yoy: "+0.4%", op_margin_yoy_bps: -574, core_op_pbt_yoy: "-2.9%", other_income_yoy: "+43.7%"}
  underlying_ex_one_time: {op_ebitda_yoy: "+7.6%", op_margin: "~43.0% (-287bps)", core_op_pbt_yoy: "+5.4%", other_income_yoy: "~+20.3%"}
  write_off_geometry: "Rs4.0Cr write-off in Other Expenses (in EBITDA) + Rs3.2Cr payable-write-back in Other Income (below EBITDA) = Rs0.80Cr net P&L hit; ~287bps of 574bps compression one-time, ~287bps genuine IoT-mix"
  anchors: ["T12/L34","T37/L87","T39/L91","T41/L95"]
questions_for_management:
  - {q: "At 30-Sep-2026 H1 BS: consolidated receivables, government sub-total (Rs), 6m+ ageing; is the Rs4Cr write-off contained?", from_finding_id: "BF/A3-01/A3-02/MMI-06"}
  - {q: "Was the back-to-back Rs3.2Cr payable owed to the same govt counterparty/related party, and is any of it at risk?", from_finding_id: "A3-04/A3-05/A3-06"}
  - {q: "35%+ FY27 guide vs ~43% Q1 underlying: what H2 blended margin, and what IoT hardware revenue share drives the dilution?", from_finding_id: "A3-07/A3-12/F12-1/MMI-04"}
  - {q: "Rs745Cr cash (+60 QoQ), no plan, FY28 Rs1,000Cr unmentioned: capital-allocation plan and is the FY28 target still in place?", from_finding_id: "A3-16/A3-17/MMI-10/MMI-12/F2-2"}
  - {q: "Government now majority of receivables on longer cycle: internal DSO target for government; how gate digital-twin/Naksha on good vs bad receivables?", from_finding_id: "A3-02/A3-03/A3-13"}
  - {q: "Consol PAT below standalone (19.5pp swing): provide Gtropy standalone P&L; identify the Nil-revenue Rs0.11Cr-loss unreviewed subsidiary.", from_finding_id: "F2-1/F3-1/A3-18"}
  - {q: "Provide A&M/C&E->AEG mapping bridge; confirm no revenue reclassified between segments.", from_finding_id: "A3-20/MMI-01/F16-1"}
  - {q: "Order book Rs1,750Cr: provide AEG segment mix and new-order intake value (withheld for competitive reasons).", from_finding_id: "A3-14/MMI-07"}
  - {q: "Confirm ClarityX/Zenithra RPT ceiling (Rs24Cr) utilisation and any FY27 RPT (no RPT discussed on call).", from_finding_id: "A3-19"}
  - {q: "ETR 24.2% below 25.17% statutory on deferred-tax credits: when does the DTA shield exhaust and ETR normalise?", from_finding_id: "F8-2"}
  - {q: "Auto-OEM volume time-shift dated to H2 FY26: will the weaker base lift H2 FY27 auto YoY, or does the reduction continue?", from_finding_id: "A3-08/A3-09"}
  - {q: "Why did Mappls DT WTD (Nikhil Kumar) step down with reason NA, who succeeds, and when is Rohan Verma JMD ratification?", from_finding_id: "F13-1/MMI-08/A3-22"}
answered_or_dropped_from_v1:
  - {q: "Margin bridge ex-write-off / Map-core margin", status: "ANSWERED (43 plus ex-write-off; 35%+ FY27 guide) - forward leg folded into new Q3", ref: "A3-07"}
  - {q: "Government 11% vs 9.2% reconcile + seasonality", status: "PARTIAL (Q1 weakest seasonality; number still unquantified) - folded into new Q1/Q5", ref: "A3-21"}
monitorables:
  - {item: "Q2 FY27 results with mandatory H1 balance sheet + cash flow (resolves FLAG-CASH falsifier)", implied_date: "2026-11", source_ref: "Reg33 / BF"}
  - {item: "Full-year FY27 EBITDA margin 35%+ guide vs H2 print", implied_date: "FY27 year-end", source_ref: "concall T14/L38 (A3-07)"}
  - {item: "Rs4Cr govt write-off recurrence test", implied_date: "2026-11", source_ref: "concall T12/L34, T29/L70 (A3-04)"}
  - {item: "Order book Rs1,750Cr -> revenue conversion; annual fixed/volume split", implied_date: "next annual disclosure", source_ref: "concall T19/L49, T27/L66"}
  - {item: "FY28 Rs1,000Cr target reaffirm-or-confirm-dropped", implied_date: "next concall", source_ref: "concall silence (A3-16) / MMI-10"}
  - {item: "Idle-treasury capital-allocation plan", implied_date: "overdue/undated", source_ref: "concall silence (A3-17) / MMI-12"}
  - {item: "Rohan Verma Joint MD shareholder ratification", implied_date: "FY27 AGM/EGM", source_ref: "concall T3/L12 (A3-22) / deck s4 / press l136"}
  - {item: "Nikhil Kumar WTD Mappls DT cessation; successor", implied_date: "2026-08-03 (successor TBD)", source_ref: "results l53 / Annexure-B (F13-1)"}
  - {item: "AEG reporting live; A&M/C&E->AEG restatement bridge owed", implied_date: "Q1FY27 onward", source_ref: "concall T3/L12, T10/L30 (A3-20) / MMI-01"}
  - {item: "Auto-OEM volume time-shift (H2-dated) H2 FY27 base effect", implied_date: "H2 FY27", source_ref: "concall T10/L30 (A3-08)"}
  - {item: "IoT hardware->SaaS margin uplift", implied_date: "billing-cycle dependent", source_ref: "concall T47-51 (A3-12)"}
  - {item: "FY26 AR / AGM: RPT ceiling, receivables ageing, Gtropy stake, entity roster", implied_date: "FY27 AGM", source_ref: "Notion items 3/6/10 / F15-1"}
flags: ["FLAG-CASH-INDETERMINATE (falsifier unresolvable, no Q1 BS confirmed T33/L78; root cause reframed Gtropy->GOVERNMENT; Rs4Cr realized govt write-off)","FLAG-PROMOTER-CONCERN (Rohan Verma Joint MD, family succession; ratification pending)","UNDERLYING-VS-REPORTED-CORRECTION (v1 reported core-PBT -2.9% corrected to underlying +5.4% ex one-time; ~half of 574bps margin fall is one-time; reported anchor retained for valuation)","MARGIN-GUIDE-SUB-40 (FY27 guide 35%+, below reported 40.2% and underlying ~43% -> H2 dilution)","FY28-TARGET-SILENT (Rs1,000Cr not mentioned despite direct question; 1 DROPPED this window)","CFO-SILENT-ON-CALL (accounting reconciliation handled by promoters, not CFO)","SC-GAP-SWING (-10.2%; subsidiary block loss-making; mgmt deprecated standalone analysis)","ORDER-BOOK-DISCLOSED (Rs1,750Cr on call; segment mix still withheld)","TREASURY-PLAN-SILENT (Rs745Cr, no allocation plan)"]
plain_language_brief_included: true
review_path: "/home/user/inflection-pipeline/runs/mapmyindia-q1fy27/work/review_mapmyindia_q1fy27_v2.md"
supersedes: "/home/user/inflection-pipeline/runs/mapmyindia-q1fy27/work/review_mapmyindia_q1fy27.md (v1 Section B 'Role 5 N.A.')"
```
