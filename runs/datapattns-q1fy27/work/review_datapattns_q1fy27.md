# Q1 FY27 COMPLETE QUARTERLY REVIEW — Data Patterns (India) Ltd (DATAPATTNS)

**Agent:** A4 ANALYST | **Model:** claude-opus-4-8 | **Date:** 2026-07-31
**Quarter:** Q1 FY27 (quarter ended 30 June 2026)
**Protocols executed:** Role 4 (Results Review v1.2) in full; **Role 5 (Concall Analysis v1.1) now COMPLETED against the actual 84-turn transcript** (call held 31-Jul-2026 12:30 IST). The prior version of this file ran Role 4 in full and Role 5 against the investor presentation as a surrogate with the live-call Q&A/credibility read flagged PENDING; **this run replaces Section B with the transcript-based analysis and grades the 18 pre-committed management questions.** Role 4 numbers are unchanged.
**Docs merged:** results, acquisition (Reg 30 / STAC), presentation, **concall**.

---

## LEDGER-RECONCILIATION PREAMBLE (contractual — stated before Step 1)

**Ledger contains 18 notes / 84 turns / 32 slides. All 18 notes, all 84 turns, and all 32 slides reviewed.** Full reconciliation contract discharged:

| Doc | A2 gate | Rows read verbatim at cited lines |
|---|---|---|
| results | pass | 8 notes + 27 line items + 1 agenda item + 4 auditor paras + 3 signature blocks + 0 entities + 0 annexures |
| acquisition | pass | 10 Annexure-A disclosure fields + 24 granular sub-items + 18 letter/header fields + 8 signature-block lines |
| presentation | pass | 32 slides; 918 gated financial values (340 P&L/margin + 98 order-book/inflow + 63 segment/customer + 296 balance-sheet/cash-flow + 121 headline stats) + 43 zero-standing cells + 9 footnotes |
| concall | pass | **84 turns** (39 question-turns + 28 answer-turns + 1 Moderator + 1 Closing + 15 unbracketed operator/mgmt), 39 questions, 66 management numbers, 29 forward-commitment phrases, 14 hedge phrases — A2 COUNT TEST all match (grep=sweep). |

Notes total for preamble = 8 (results) + 10 (acquisition disclosure fields) = **18**. Turns = **84** (concall). Slides = **32**. **No ledger row is unreviewed; proceeding.**

**A3 findings incorporated (all non-N.A. IDs across four docs):**
Results — DP-F1a, DP-F6a, DP-F14a.
Acquisition — F1, F6, F7, F11, F13, F14, F15, F17.
Presentation — A3-F1-01, A3-F6-01, A3-F6-02, A3-F6-03, A3-F6-04, A3-F6-05, A3-F6-06, A3-F6-07, A3-F6-08, A3-F7-01, A3-F9-01, A3-F13-01, A3-F14-01, A3-F15-01, A3-F16-01, A3-F16-02, A3-F16-03, A3-F16-04.
**Concall (new this run) — A3-01, A3-02, A3-03, A3-04, A3-05, A3-06, A3-07, A3-08, A3-09, A3-10, A3-11, A3-12, A3-13, A3-14, A3-15, A3-16, A3-17, A3-18.**

Every concall finding classified **FORWARD-SIGNAL** (A3-01..A3-07, A3-12, A3-15) or **AMBIGUOUS** (A3-11, A3-13, A3-14, A3-16, A3-17) is carried to the Updated-Questions-for-Management table (Section B Step 8F) with an explicit `from_finding_id`. The EVASION/CONFIRMATORY-NEGATIVE findings (A3-08, A3-09, A3-18) are also converted to questions per conservative bias (A3 rule 6).

**Decision Status verified BEFORE framing: WATCHLIST / AVOID** (Notion, analysis date 01-Jun-2026, CMP Rs 4,043.10). Non-held name → **Step 8A-W branch** applies. No HOLD/ADD/TRIM/EXIT mechanics.

---

# SECTION A — RESULTS REVIEW (Role 4) — NUMBERS UNCHANGED FROM PRIOR RUN

## STEP 0 — PRE-FLIGHT

**0A. Notion baseline (verified):** WATCHLIST / AVOID; entry zone Rs 770-867 (DA-tightened Rs 693-770); Base FY29 FV Rs 1,694; MoS Rs 694; P/B floor Rs 2,420; current ~83x P/E; prob-weighted 3-yr CAGR at CMP = −26.4%. FY26 base: Revenue Rs 924.77 Cr, EBITDA Rs 371 Cr/40.4%, PAT Rs 271 Cr/29.3%. DA central crack: CFO/PAT 0.234x cumulative, 0.30x FY26. Promoter pledge 0%; auditor Deloitte; EXEMPLARY promoter.

**0B. Unit convention:** results filing states "All figures are in INR Crores" (line 126); conversion factor x1. Presentation is in Rs Mn (x0.1 to Cr) with order-book/guidance items already in Cr; acquisition in mixed Cr/Lakhs (Lakhs x0.01). Concall figures quoted in Rs Crores throughout (x1). All analysis below in **₹ Crores**.

**0C. Share-count changes:** none since the 13-Mar-2023 QIP (Note 4, line 187-188). Paid-up Rs 11.20 Cr (Rs 2 face → 5.60 Cr shares) identical across all four periods (line 163). EPS "Basic and Diluted" single figure → **EPS reported = EPS share-adjusted**.

**0D. Numbered-notes extraction (mandatory):**

| Note # | Subject | What it says (1 sentence) | ₹ Cr impact | Period affected | Comparability impact |
|---|---|---|---|---|---|
| 1 (unnum., l.174-178) | Approval / auditor conclusion | Results reviewed by Audit Committee & Board 30-Jul-2026; Deloitte expressed **unmodified conclusion** | — | Q1FY27 | None; clean |
| 2 (l.180-181) | Single segment | Only one business segment (defence electronics); no reportable segment per Ind AS 108 | — | all | No segment split available |
| 3 (l.183-184) | Q4FY26 balancing figure | Q4FY26 column = FY26 audited minus 9M-Dec-2025 published (**derived, not independently reported**) | — | Q4FY26 | QoQ base is a balancing figure — treat with care |
| 4 (l.187-207) | QIP utilization | Rs 26.25 Cr of Rs 487.74 Cr QIP proceeds still **unutilised** as on 30-Jun-2026 (Rs 24.65 Cr product dev + Rs 1.60 Cr EMI-EMC) | 26.25 undeployed | since 13-Mar-2023 | Standing capex/deployment commitment (→ DP-F6a) |
| 5 (l.209) | Consolidation scope | **No subsidiary/associate/JV as on 30-Jun-2026** → no consolidated statement exists | — | Q1FY27 | S-vs-C gap structurally zero this quarter |
| 6 (l.211-212) | Labour Code exceptional | FY26 exceptional Rs 3.01 Cr = incremental impact of revised wage definition (Labour Codes notified 21-Nov-2025) | 3.01 (FY26 only) | FY26 | Recurring wage-base step-up flows through Employee benefits FY27+ (→ DP-F1a) |
| 7 (l.214) | Regrouping | Prior-period figures regrouped where necessary | — | prior | Boilerplate |
| 8 (footnote, l.168/170) | EPS basis | EPS **not annualised** for the quarters | — | quarters | Do not annualise Q1 EPS × 4 |

**Auditor opinion:** **Unmodified** limited-review conclusion (Deloitte Haskins & Sells, FRN 008072S; Ananthi Amarnath, Partner, M.No. 209252; UDIN 26209252LUDGSU3734; line 106-117). No EoM, no Other Matters, no Going Concern paragraph. **AMBER flag (governance, not opinion):** auditor's digital signature timestamped **16:34:57 IST**, ~1h56m BEFORE the Board's stated conclusion time of **18:30 IST** (line 41), while the report asserts the Statement was "approved by the Company's Board of Directors" (→ DP-F14a).

**0E. Business type:** **Standard operating business** (defence electronics manufacturer). Steps 1 and 5 (not 1L/5L).

🛑 Pre-flight complete: Notion fetched & Decision Status verified (WATCHLIST/AVOID); units ₹ Cr; no share-count change; 8 notes extracted; auditor unmodified; standard business.

---

## STEP 1 — DATA EXTRACTION TABLE (standalone; ₹ Cr; no consolidated statement exists)

| Line Item | Q1 FY26 | Q4 FY26 (bal. fig.) | Q1 FY27 | FY26 | FY25 |
|---|---|---|---|---|---|
| Revenue from Operations | 99.33 (l.132) | 344.85 (l.132) | 116.03 (l.132) | 924.77 (l.132) | 708.4 (deck l.454, 7,084 Mn) |
| Other Income | 10.55 (l.133) | 5.66 (l.133) | 7.31 (l.133) | 27.96 (l.133) | 46.3 (deck l.912, 463 Mn) |
| Total Income | 109.88 (l.134) | 350.51 (l.134) | 123.34 (l.134) | 952.73 (l.134) | 754.7 (deck l.913, 7,547 Mn) |
| Cost of Materials Consumed | 57.16 (l.137) | 88.06 (l.137) | 30.73 (l.137) | 306.06 (l.137) | 351.3 (deck l.915, 3,513 Mn) |
| Change in Inventories | (37.06) (l.139) | 3.65 (l.139) | (6.21) (l.139) | 33.84 (l.139) | (75.2) (deck l.916, -752 Mn) |
| Employee Benefits Expense | 36.38 (l.140) | 40.72 (l.140) | 42.53 (l.140) | 154.26 (l.140) | 114.1 (deck l.917, 1,141 Mn) |
| Finance Costs | 3.19 (l.141) | 4.65 (l.141) | 3.28 (l.141) | 12.45 (l.141) | 12.1 (deck l.918, 121 Mn) |
| Depreciation | 5.49 (l.142) | 5.89 (l.142) | 5.92 (l.142) | 22.95 (l.142) | 13.9 (deck l.919, 139 Mn) |
| Other Expenses | 10.77 (l.143) | 19.58 (l.143) | 17.61 (l.143) | 56.62 (l.143) | 43.2 (deck l.920, 432 Mn) |
| Total Expenses | 75.93 (l.144) | 162.55 (l.144) | 93.86 (l.144) | 586.18 (l.144) | 459.4 (deck l.921, 4,594 Mn) |
| Profit Before Exceptional & Tax | 33.95 (l.149) | 187.96 (l.149) | 29.48 (l.149) | 366.55 (l.149) | 295.3 (deck l.922, 2,953 Mn) |
| Exceptional (Labour Codes) | – (l.153) | – (l.153) | – (l.153) | 3.01 (l.153) | ND |
| Profit Before Tax | 33.95 (l.154) | 187.96 (l.154) | 29.48 (l.154) | 363.54 (l.154) | 295.3 (deck l.470, 2,953 Mn) |
| Tax Expense | 8.45 (l.155) | 49.58 (l.155) | 7.42 (l.155) | 92.17 (l.155) | 73.5 (deck l.924, 735 Mn) |
| PAT | 25.50 (l.156) | 138.38 (l.156) | 22.06 (l.156) | 271.37 (l.156) | 221.8 (deck l.925, 2,218 Mn) |
| EPS reported (₹) | 4.55 (l.168) | 24.71 (l.168) | 3.94 (l.168) | 48.47 (l.168) | 39.6 (deck l.473) |
| EPS share-adjusted (₹) | 4.55 | 24.71 | 3.94 | 48.47 | 39.6 |

**Derived metrics (₹ Cr; computed row-by-row):**

| Derived Metric | Formula | Q1 FY26 | Q4 FY26 | Q1 FY27 | FY26 |
|---|---|---|---|---|---|
| Operating EBITDA | PBT + D + FC − OI | 32.08 | 192.84 | 31.37 | 373.99¹ |
| Operating EBITDA Margin | Op EBITDA / Rev | 32.30% | 55.92% | **27.04%** | 40.44% |
| Reported EBITDA | PBT + D + FC | 42.63 | 198.50 | 38.68 | 401.95¹ |
| Core PBT (ex-OI) | PBT − OI | 23.40 | 182.30 | 22.17 | 338.59¹ |
| Other Income / PBT | OI / PBT | 31.08% | 3.01% | 24.80% | 7.63% |
| Effective Tax Rate | Tax / PBT | 24.89% | 26.38% | 25.17% | 25.35%² |
| PAT Margin (on Rev) | PAT / Rev | 25.67% | 40.13% | 19.01% | 29.34% |

¹ FY26 derived from PBT-before-exceptional (366.55) to keep the one-off Labour Code Rs 3.01 Cr out of operating EBITDA; deck reports FY26 EBITDA 371.0 Cr (l.462) by folding the Rs 3.01 Cr exceptional into Other Expenses (deck opex 597 Mn vs filing 566.2 Mn). Both reconcile; the Rs ~3 Cr difference is exactly the exceptional. ² FY26 ETR on reported PBT after exceptional (363.54).

**Deck cross-check:** filing-derived operating EBITDA (Q1FY27 31.37 Cr, Q1FY26 32.08 Cr, Q4FY26 192.84 Cr) ties 1:1 to deck EBITDA (314 / 321 / 1,928 Mn, l.462). **The deck's "EBITDA" IS operating EBITDA (ex-Other Income), not reported EBITDA** — important for honest margin reading.

**Concall tie-out (new — confirms Role 4 numbers, changes none):** the CFO's spoken P&L (turn 11) — Revenue Rs 116 Cr, GP Rs 91.5 Cr / 78.9%, EBITDA Rs 31.4 Cr / 27%, PAT Rs 22.1 Cr / 19% — reconciles to the filing at every line: spoken GP Rs 91.5 Cr = Revenue 116.03 − (RM consumed 30.73 − change in inv 6.21 = 24.52) = **91.51 Cr** (identical to the Step 4 gross-profit figure); EBITDA 31.37/27.04% and PAT 22.06/19.01% match. **Spoken P&L = filing = CONFIRMED.** The only concall figures that do NOT reconcile to the deck are the balance-sheet cash number (Rs 530 Cr spoken vs Rs 465.9 Cr deck) and the confirmed order book (Rs 920 Cr spoken vs Rs 927.7 Cr deck) — handled in Section B Step 7A, not here.

🛑 Every cell filled or ND. Consolidated columns absent by structure (Note 5) — not ND-by-omission but ND-by-nonexistence; **standalone = consolidated this quarter**.

---

## STEP 2 — Q1 FY27 YoY COMPARISON (Q1FY27 vs Q1FY26) — THE MOST IMPORTANT STEP

| Metric | Q1 FY26 | Q1 FY27 | YoY % Change | Verdict |
|---|---|---|---|---|
| Revenue from Operations | 99.33 | 116.03 | **+16.81%** | Grows, but below the low end of mgmt's own 20-25% FY27 guidance |
| Operating EBITDA | 32.08 | 31.37 | **−2.21%** | Contracts despite revenue growth — negative operating leverage |
| Op EBITDA Margin | 32.30% | 27.04% | **−526 bps** | Material compression |
| Depreciation | 5.49 | 5.92 | +7.83% | Scaling ~half of revenue growth |
| Finance Costs | 3.19 | 3.28 | +2.82% | Flat; net-cash balance sheet |
| EBIT (operating) | 26.59 | 25.45 | −4.29% | Declines |
| Other Income | 10.55 | 7.31 | −30.71% | Treasury timing lower YoY |
| **Core Operating PBT (PBT − OI)** | 23.40 | 22.17 | **−5.26%** | **Declines — headline growth is not real at the operating line** |
| Reported PBT | 33.95 | 29.48 | −13.17% | Falls (OI drop + margin) |
| PAT | 25.50 | 22.06 | −13.49% | Falls |
| EPS (share-adjusted) | 4.55 | 3.94 | −13.41% | Falls |

**Six mandatory diagnostics:**

1. **Did revenue grow YoY?** Yes, +16.81% (Q1FY27 116.03 vs Q1FY26 99.33). But management's FY27 guidance is 20-25% revenue growth (deck l.256/262; concall turn 9); Q1 came in **below the low end** of the company's own full-year target on the first quarter.
2. **Op EBITDA margin?** **Contracted 526 bps: 27.04% (Q1FY27) vs 32.30% (Q1FY26).** Named explicitly, comparison base is the year-ago quarter (not sequential). Driven by Employee benefits +16.9% (l.140) and Other expenses +63.5% (l.143) both outrunning revenue +16.8%.
3. **Did core operating PBT (ex-OI) grow YoY?** **No — it fell 5.26% (23.40 → 22.17).** This is the cleanest operational-health test and it is negative. Revenue grew 16.8% while core operating profit shrank: **the +16.8% revenue headline masks operating deterioration.** The gap is named.
4. **What drove the gap between core PBT and reported PAT decline?** Reported PBT fell 13.17% vs core PBT −5.26%; the extra −7.9pp is **Other Income −30.71%** (10.55 → 7.31, a −3.24 Cr swing). PAT fell 13.49%, slightly less severe than PBT because tax fell (8.45 → 7.42, −1.03 Cr) at a near-constant ETR (24.89% → 25.17%). Each delta quantified in the Step 4 bridge.
5. **D&A / finance costs scaling faster than revenue?** No absorption alarm: Dep +7.83% and Finance +2.82% both **below** revenue +16.81%. Capex-absorption gap is not the issue this quarter; margin mix and cost step-ups are.
6. **Other Income concentration changing?** OI/PBT fell to 24.80% (Q1FY27) from 31.08% (Q1FY26) — still a meaningful quarter (a quarter of PBT is treasury). Stripping OI, core operations declined YoY — the read does not improve when OI is removed; it confirms the operating softness.

🛑 YoY table + six diagnostics shown. Core signal: **revenue up, core operating profit down.**

---

## STEP 3 — SEQUENTIAL QoQ TRAJECTORY (last 5 quarters)

| Quarter | Revenue (₹ Cr) | Op EBITDA Margin | Core PBT ex-OI (₹ Cr) | One-offs flagged | QoQ run-rate |
|---|---|---|---|---|---|
| Q1 FY26 | 99.33 (l.132) | 32.30% | 23.40 | — | base |
| Q2 FY26 | 173.1 (deck l.384, 1,731 Mn) | ND (quarterly EBITDA not disclosed) | ND | — | Stepping up |
| Q3 FY26 | 307.5 (deck l.384, 3,075 Mn) | ND | ND | — | Stepping up |
| Q4 FY26 | 344.85 (l.132) | 55.92% | 182.30 | Balancing figure (Note 3) | Peak (year-end) |
| Q1 FY27 | 116.03 (l.132) | 27.04% | 22.17 | Labour Code base now in opex | **Reset to Q1 seasonal low** |

**Diagnostics:**
- **Run-rate trajectory:** Data Patterns has a **severe back-ended seasonal pattern** — Q1 is structurally the weakest quarter. Q1FY27 116.03 Cr is 33.6% of the Q4FY26 print and only marginally above Q1FY26. The −66.4% QoQ (deck l.454) is **seasonality, not deterioration** — but the YoY read (Step 2) is the honest comparison, and it is soft. **Concall corroboration (turns 21, 37):** the CMD explicitly frames the softness as a "yearly business," "not a quarter to quarter" or "month-to-month day on day production business" — i.e., management itself endorses the seasonality reading, which does not rescue the YoY core-PBT decline.
- **One-off distortion:** Q4FY26 is a **balancing figure** (Note 3, line 183) — derived, not independently reported; its 55.92% operating margin is a year-end catch-up artifact and must not be read as a run-rate. Q2/Q3 FY26 quarterly EBITDA margins are **not disclosed** in any of the four documents (ND).
- **Latest vs H1 run-rate / capex commissioning test:** N/A this quarter — no new-plant commissioning claimed; Q1 revenue below the trailing average is expected seasonally.
- **Implied Q2 base to hold guidance:** to reach even the 20% FY27 revenue floor (~Rs 1,109.7 Cr), Q2-Q4 must average ~Rs 331 Cr/qtr after a Rs 116 Cr Q1 — i.e. a **very steep H2 ramp**. This is the crux the concall was expected to address; it did not quantify the bridge (turn 37 was qualitative — "confident of full year," margins "very much in line with our internal targets" — no numbers).

🛑 QoQ table + diagnostics shown.

---

## STEP 4 — OPERATIONAL DECOMPOSITION (PAT bridge, Q1FY26 → Q1FY27)

Reported PAT change = 25.50 → 22.06 = **−3.44 Cr**.

| Component | YoY Change (₹ Cr) | YoY Change (%) | Recurring? |
|---|---|---|---|
| Gross profit (Rev − RM cost) | +12.28 (79.23 → 91.51) | +15.5% | Recurring |
| Employee benefits (cost ↑) | −6.15 (36.38 → 42.53) | +16.9% | Recurring (incl. Labour Code wage-base) |
| Other expenses (cost ↑) | −6.84 (10.77 → 17.61) | +63.5% | Recurring; **step-up now EXPLAINED by concall — see note** |
| = Operating EBITDA change | **−0.71** (32.08 → 31.37) | −2.2% | Recurring |
| Depreciation (↑) | −0.43 (5.49 → 5.92) | +7.8% | Recurring (post-capex) |
| Finance cost (↑) | −0.09 (3.19 → 3.28) | +2.8% | Recurring |
| Other Income (↓) | −3.24 (10.55 → 7.31) | −30.7% | **NON-RECURRING (treasury/FV)** |
| = Reported PBT change | −4.47 (33.95 → 29.48) | −13.2% | — |
| Tax (lower, ETR ~flat) | +1.03 (8.45 → 7.42) | −12.2% | Mixed |
| Exceptional | 0 | — | n/a (nil in quarters) |
| **Reported PAT change** | **−3.44** | **−13.5%** | — |

**Concall RESOLVES the prior open item on the +63.5% other-expenses step-up (turn 15/17, IIFL Capital):** the prior Role 4 flagged this jump as "unexplained by any note." The concall now attributes it to two items — (a) "additional repairs and maintenance cost … because the facility is now going through some revamping," and (b) **"close to 2 crore we have additionally provided for … against the long pending receivables as per our policy."** The **~Rs 2 Cr receivables provision is decision-relevant evidence on the cash-conversion / receivables crack** (the central DA thesis): the company is provisioning against long-pending receivables in a quarter it also declined to disclose CFO or DSO. This does NOT change any Role 4 number (the Rs 17.61 Cr Other Expenses already includes it) but it re-characterises part of the step-up as a **credit-quality charge on the receivable book**, not routine cost inflation. Surfaced as a flag and carried to Section B.

**Mandatory answers:**
- **% of PAT decline from recurring vs non-recurring:** the operating line (EBITDA + D + finance) fell **−1.23 Cr** (recurring), and Other Income fell **−3.24 Cr** (non-recurring); tax added back +1.03 Cr. So both buckets are negative — **there is no "one-off masking a good quarter" here; the quarter is soft on both core operations and treasury.**
- **If Other Income reverts to prior-year level (10.55):** PBT would be ~32.72 Cr and PAT ~24.5 Cr — still **below** Q1FY26's 25.50, confirming the decline is operational, not merely treasury timing.
- **D&A/finance steady-state?** Depreciation +7.8% is modest; against a capex plan **RAISED on the call to "Rs 200 Cr+ minimum" over two years** (turn 109; deck had said Rs 150 Cr) plus Rs 26.25 Cr QIP still undeployed, D&A will step up materially when that capex commissions — a forward margin headwind, now larger than the deck implied.
- **Tax adjustments?** None — ETR dead-on statutory (25.17%); no earlier-year tax line, no DTA/credit distortion.

🛑 Bridge + answers shown.

---

## STEP 5 — CASH QUALITY & BALANCE SHEET

**Data-availability rule (v1.2):** this is a **Q1 review**. Reg 33 mandates cash-flow and balance-sheet statements only **half-yearly (Q2/Q4)**. The Q1 results filing therefore carries **no cash flow, no balance sheet** — CFO, receivable days, CCC, PPE, CWIP rows are **ND by regulation, not by omission**. The presentation discloses **only annual** (FY21-FY26) cash flow (deck slide 30) and **only annual/H1-TTM** working-capital days (slide 24) — **no Q1FY27 point exists anywhere**, and the concall (turn 11) gave only a closing cash figure, no CFO and no DSO (A3-18).

| Metric | Prior period (FY26 annual) | Current period (Q1FY27) | Change | Verdict |
|---|---|---|---|---|
| CFO | 80.1 (deck l.998, 801 Mn) | **ND** (Q1, no Reg-33 statement; concall silent, turn 11) | ND | Indeterminate for quarter |
| CFO/PAT ratio | 0.295x (80.1/271.37) | **ND** | ND | FY26 confirms structural weakness (~0.30x, ICRA/Notion agree) |
| Capex (PPE+CWIP) | PPE 160.6 + CWIP 13.2 (deck l.943/945, Mar-26) | **ND** (Q1); plan RAISED to Rs 200 Cr+ / 2 yr (concall turn 109) | ND | Rs 200 Cr+ 2-yr plan (was Rs 150 Cr) + Rs 26.25 Cr QIP undeployed |
| FCF (CFO − Capex) | ND (annual capex split not clean) | **ND** | ND | — |
| Working capital change | −211.4 (deck l.994, -2,114 Mn FY26) | **ND** | ND | Chronic WC absorption |
| Receivable days | 307 (deck l.820, FY26, H1-TTM basis) | **ND** (no DSO; ~Rs 2 Cr fresh provision on long-pending receivables, concall turn 17) | ND | Structural (~280-308 for 4 yrs); provisioning a negative marker |
| Inventory days | 108 (deck l.837, FY26) | **ND** | ND | — |
| Payable days | 43 (deck l.820, FY26) | **ND** | ND | — |
| Cash Conversion Cycle | 428 (deck l.837, FY26) | **ND** | ND | ~427-432 for 3 yrs — structural |
| PPE | 160.6 (deck l.943, Mar-26, 1,606 Mn) | **ND** | ND | — |
| CWIP | 13.2 (deck l.945, Mar-26, 132 Mn) | **ND** | ND | — |
| Net Debt / (Net Cash) | (Net cash) — total debt 0.0 (deck l.932) | **(Net cash); deck Rs 465.9 Cr (l.326) vs concall spoken Rs 530 Cr (turn 11) — Rs 64 Cr UNRECONCILED GAP** | ↑ cash | Net-debt-free maintained; the two figures do not tie (A3-13) |
| Promoter Pledge | 0% (Notion) | **ND in filing** (no pledge disclosure; Notion 0%) | — | No pledge event disclosed |

**Mandatory answers:**
- **CFO/PAT vs Pillar 2 assumption:** cannot test for the quarter (Q1 CFO = ND, concall silent). FY26 annual CFO/PAT = **0.295x**, in the ~0.30x band the DA already flagged as the central crack — **well below the 0.65x-1.30x Pillar-2 valuation bands**. The quarter adds no CFO evidence to relieve this; the **half-yearly statement at Q2FY27 is the first and mandatory CFO reading** for FY27. The concall's ~Rs 2 Cr fresh provision against long-pending receivables (turn 17) is a **directionally negative** colour on the receivable book.
- **WC drag structural or growth-induced?** **Structural.** CCC has held ~427-432 days for FY23-FY25 and only eased to 428 (FY26); receivable days ~307. If growth stopped, the ~300-day receivables and ~430-day CCC would persist — passes the "stopped growing tomorrow" test as structural. Trade receivables grew 596.4 → 727.8 Cr (Mar-25 → Mar-26, deck l.964).
- **CWIP capitalisation:** ND (no Q1 balance sheet). Rs 26.25 Cr QIP earmarked for product development / EMI-EMC facility remains **undeployed 3.3 years post-allotment** (DP-F6a); on the call the CMD referenced "we took money … to fund such development programs" (turns 33, 117) generically but gave no deployment schedule.
- **Net debt vs projection:** net cash somewhere between the deck's Rs 465.9 Cr and the CFO's spoken Rs 530 Cr (30-Jun-2026) — either way far above the Rs 100 Cr "cash drain" tripwire. **The Rs 64 Cr gap between the two same-date figures is itself a flag** (A3-13); per protocol the filing/deck figure (Rs 465.9 Cr) is the anchor and the spoken figure is not credited without reconciliation. The Rs 10 Cr STAC outlay is immaterial to this cushion; the RAISED Rs 200 Cr+ capex is not.

**CASH-CONVERSION CLASSIFICATION: INDETERMINATE for the quarter.** Per house rule, INDETERMINATE cash conversion **may not resolve to PROCEED**; it caps the protocol verdict at **PROCEED WITH CAVEATS**, with the **missing evidence named: Q1FY27 CFO, receivable days, and capex-YTD are undisclosed** (Reg-33-permitted at Q1). The concall — for a company with a known 0.234x cumulative CFO/PAT problem — was **silent on CFO/OCF and DSO while volunteering a fresh receivables provision**; that combination is a decision-relevant CONFIRMATORY-NEGATIVE (A3-18).

🛑 Cash-quality table + answers shown.

---

## STEP 6 — RECONCILIATION VS THESIS

### 6A. Variance vs Notion projections

The inline Notion payload passed **FY26 base actuals and the destination-PE / entry-zone framework, but did NOT pass the granular FY27 Bear/Base/Bull revenue/margin/PAT cells.** Per the no-estimation rule those specific projection cells are **ND (not passed to this review)**; the quarter is instead scored against management's own FY27 guidance and the thesis-broken thresholds (which WERE passed). No estimation performed.

| Metric | Bear Proj | Base Proj | Bull Proj | Actual (Q1FY27 / annualised context) | Lands In |
|---|---|---|---|---|---|
| Revenue (FY27) | ND (not passed) | ND | ND | Q1 116.03; +16.8% YoY vs mgmt guide 20-25% | Below mgmt guide low-end on Q1 |
| EBITDA Margin (FY27) | ND | ND | ND | Q1 Op 27.04% vs mgmt guide 35-40% | 800-1300 bps below guidance (1 qtr) |
| PAT (FY27) | ND | ND | ND | Q1 22.06; −13.5% YoY | Declining YoY |
| EPS (FY27) | ND | ND | ND | Q1 3.94 | Declining YoY |
| Net Debt (FY27) | ND | Net cash | ND | Net cash Rs 465.9 Cr (deck) / Rs 530 Cr (call) | On track (net-debt-free held) |
| ROCE | ND | ND | ND | FY26 20.8% (deck l.323); Q1 ND | No new annual reading |

**Probability re-weighting rule:** requires actuals **below Bear on 2+ metrics for 2 consecutive quarters**. Bear cells were not passed and this is a **single seasonally-weak Q1** — the rule **does not fire this quarter**. Flagged for the Q2FY27 review: if H1 EBITDA margin stays sub-33% and CFO/PAT stays sub-0.30x, the second-consecutive-quarter test becomes live.

### 6B. Watchlist-item status (Notion 12-point monitoring checklist)

| # | Watchlist item | Green | Red | This-quarter reading | Status |
|---|---|---|---|---|---|
| 1 | Revenue/EBITDA%/PAT% vs Bear-Base-Bull | ≥Base | <Bear | Rev +16.8% YoY; Op EBITDA 27.04%; NPM 19.0% (l.462/487) | **AMBER** (margin soft, base cells ND) |
| 2 | Order book total + inflows | growing | shrinking | Confirmed book Rs 927.7 Cr deck (l.330) / Rs 920 Cr spoken (turn 11); Q1 inflow Rs 117.2 Cr (1,172 Mn, l.548); "incl. negotiated" Rs 2,654 Cr (l.286/turn 9) | **AMBER** (confirmed book flat QoQ 9,265→9,277) |
| 3 | Order-book composition (svc/exp/dev %) | balanced | export-thin | Services 30.0%, EW 31.9%, Radar 20.9% (l.538-543); production-vs-development split **REFUSED twice** (turns 85, 89); exports % of book not given | **AMBER→RED (opacity)** |
| 4 | CFO YTD + capex YTD | positive | negative/absent | **SILENT — no Q1 CFO/capex on filing, deck, or call** (A3-18) | **RED (silence)** |
| 5 | DSO / receivable days | falling | rising | Annual/H1-TTM 307 only; no Q1 DSO; fresh ~Rs 2 Cr provision on long-pending receivables (turn 17) | **AMBER/UNKNOWN (negative colour)** |
| 6 | Net cash | >Rs 100 Cr | <Rs 100 Cr | Rs 465.9 Cr (deck) / Rs 530 Cr (call) — both >>Rs 100 Cr | **GREEN (but Rs 64 Cr gap flagged)** |
| 7 | EW suite tender (L1) progress | L1 won | stalled | **L1 CONFIRMED on one large contract, value withheld, "undergoing negotiation"** (turn 45) | **AMBER (L1 acknowledged, unquantified)** |
| 8 | BrahMos seeker production order | order won | not converted | Seeker "successfully tested" (deck l.667); **order intake expected THIS FY, "product intake not the revenue," value withheld** (turn 73) | **AMBER (intake guided FY27, unconverted/unquantified)** |
| 9 | AMCA RFP / award | DP subsystem | total loss | **Not named on the call** (turn 61 vague "male program and bigger h programs"); silent in deck | **UNKNOWN (silence)** |
| 10 | Export order book value | rising | falling | International OB **Rs 39 Cr** (l.566/turn 9) vs export = 22.1% of Q1 revenue | **RED (confirms thin export book)** |
| 11 | Customer concentration | diversified | concentrated | Brahmos 26.7%, Export 22.1%, DRDO 16.3%, HAL 12.8%, MoD 12.7%, BEL 7.5% (l.444); not addressed on call | **AMBER** (BrahMos + export = ~49%) |
| 12 | Mgmt Q&A specificity/silence | specific | vague | **Transcript now available: dates specific, VALUES withheld on all four big catalysts; two outright refusals; quantum evaded** (see Section B) | **AMBER (OVERPROMISER-RISK pattern)** |

### 6C. Thesis-broken trigger check

| Thesis-broken condition | Threshold | Current reading | FIRED? |
|---|---|---|---|
| 1. Margin+export double-fail | FY27 EBITDA <33% **sustained 2Q** AND export OB <Rs 30 Cr | Q1 Op EBITDA 27.04% (1 qtr only); export OB **Rs 39 Cr** (>Rs 30 Cr) | **NO** — both legs must hold; margin only 1 qtr, export OB above threshold. **AMBER — half the margin leg tripped; export OB Rs 39 Cr sits just above the Rs 30 Cr line; concall guided employee-cost drag to persist (turn 9), so the margin leg risk is rising.** |
| 2. Cash conversion | cumulative FY27-28 CFO/PAT <0.30x | Q1 CFO = ND (no reading); fresh receivables provision a negative marker | **NO (unmeasurable yet)** — first reading at H1FY27 |
| 3. AMCA total loss | prime→BEL-L&T AND DP-Bharat Forge no material subsystem | AMCA **not named** on call; silent in docs | **NO (no adverse event disclosed)** |
| 4. Governance break | promoter pledge initiated (any %) | No pledge disclosure; Notion 0% | **NO** |
| 5. Audit red flag | Deloitte resigns OR qualified opinion | Deloitte signed **unmodified** conclusion (l.98-117) | **NO** |
| 6. Cash drain without trail | net cash <Rs 100 Cr without capex trail | Net cash Rs 465.9-530 Cr | **NO** |

**No thesis-broken trigger has FIRED.** Trigger 1 is the one to watch: a second sub-33% margin quarter at H1 combined with export OB slipping below Rs 30 Cr would fire it; the call's guidance that employee-cost drag persists (turn 9) raises the odds of the margin leg.

### 6D. Growth-trigger status (Notion Re-Evaluate triggers)

| Trigger | Original confidence | Confirming evidence | Killing evidence | Updated status |
|---|---|---|---|---|
| CMP < Rs 1,500 (re-evaluate) | n/a (price) | Not evaluable (no current price in scope) | — | **UNKNOWN (price not in scope)** |
| AMCA RFP outcome | catalyst | — | Not named on call (turn 61 vague) | **DELAYED / UNKNOWN** |
| BrahMos serial production order >Rs 500 Cr | catalyst | Seeker tested (l.667); **order INTAKE guided FY27** (turn 73) | Value withheld; "product intake not revenue"; not >Rs 500 Cr confirmed | **ON TRACK but UNCONVERTED / UNQUANTIFIED** |
| Two consecutive Q CFO/PAT >0.50x | catalyst | — | Q1 CFO not disclosed | **UNKNOWN (unmeasurable)** |
| Any thesis-broken fires | — | None fired | — | **NONE FIRED** |

🛑 6A-6D shown in full.

---

## STEP 7 — FOUR-PILLAR DESTINATION PE RE-VALIDATION

This is a **seasonally weak Q1 with no new annual data** (no Q1 balance sheet, no Q1 CFO, no fresh ROCE reading). Per protocol, do not re-anchor pillars on a single seasonal quarter. FY26 actuals (the pillar inputs) are unchanged.

| Pillar / Input | Original assumption | Current reading (Q1FY27) | Action |
|---|---|---|---|
| ROCE Base (0.5×ROCE+7.5, floor 9x, cap 24x) | FY26 ROCE 20.8% → ~17.9x | No Q1 ROCE (ND); FY26 20.8% unchanged (deck l.323) | **HOLD** — no FTTCP re-run trigger from a seasonal Q1 |
| Cash Multiplier | per DA (weak, ~0.30x band) | Q1 CFO ND; FY26 0.295x confirms weak band; fresh receivables provision | **HOLD (watch)** — first FY27 reading at H1 |
| Growth Visibility Premium | per EM score 45.9 | Confirmed book flat QoQ; "incl. negotiated" Rs 2,654 Cr ~65% soft; production/development split refused | **HOLD, lean cautious** |
| Strategic Premium | franchise-not-monopoly (DA) | STAC vertical-integration bolt-on (Rs 10 Cr); seeker tested; single-credit rule respected | **HOLD** (immaterial size) |
| UA Multiplier | per Notion | No change to the 3 qualifiers this quarter | **HOLD** |
| Sector Cap | defence-electronics | No reclassification | **HOLD** |
| **Hurdle Ratio recheck** | HR = (1+EPS CAGR)³ × (Dest PE mid ÷ Current PE) ≥ 1.953 | EPS CAGR inputs unchanged (Q1 seasonal); current PE ~83x (Notion); HR **fails on price**, unchanged | **STOP-on-price (unchanged)** — the entry-price gap governs |

**No pillar changed. Destination PE unchanged. No fair-value recompute triggered.** The valuation gate remains governed by the CMP being ~4.7-5.3x above the ideal entry zone (Notion), not by any Q1 pillar movement.

🛑 Pillar re-validation shown; no revised fair values (none required).

---

## STEP 8 — POSITION DECISION (Branch 8A-W — non-held / WATCHLIST-AVOID)

**Decision Status verified: WATCHLIST / AVOID → 8A-W applies (no trim/exit mechanics).**

Walking 8A-W:
- **Any thesis-broken condition FIRED?** No (Step 6C).
- **Below Bear on 2+ metrics?** Bear cells not passed; single seasonal Q1 → cannot assert "below bear," and the 2-consecutive-quarter rule is not met.
- **Between Bear and Base?** The honest read is **soft-but-inconclusive on a seasonal quarter**: revenue +16.8% (below mgmt's 20-25% guide), Op EBITDA margin 27.04% (below FY26 40.4% and far below the 35-40% FY27 guide), core operating PBT −5.3% YoY. On margin and core PBT the quarter reads soft; on net cash and order-book total it reads stable.

**8A-W output:**
- **Decision Status: REMAIN WATCHLIST / AVOID.** No change warranted from a single seasonally weak quarter with no fired trigger. The name was already AVOID on valuation (CMP ~4.7-5.3x above entry); nothing this quarter improves that, and the margin/cash softness (plus the fresh receivables provision and RAISED capex) marginally strengthens the AVOID.
- **Entry zone: UNCHANGED (Rs 770-867; DA-tightened Rs 693-770).** No new annual data on which to re-anchor fair value; re-anchoring on a seasonal Q1 would be an error. Fair values NOT recomputed.
- **Master decision gate: PUSH ONE QUARTER to H1FY27 / Q2FY27 results (~Oct 2026).** Q2 delivers the two data points that resolve the thesis's central cracks: (a) the mandatory Reg-33 half-yearly cash-flow statement → the first FY27 CFO/PAT reading, and (b) a second EBITDA-margin quarter → whether the 27% is seasonal or structural (thesis-broken trigger 1). STAC completion (~end Oct 2026) and first-ever consolidated accounts also land in that window.

### 8B. Add-back / trim trigger refinement
- Original (Notion): enter Small (2.0%) only if price reaches Rs 693-770 (DA-tightened) AND catalyst confirmation. **Unchanged.**
- **Refinement flagged (not a change to Notion):** add a pre-condition that any future entry consideration require **at least one H1FY27 CFO/PAT reading ≥0.50x**, given the quarter deepened rather than relieved the cash-conversion concern (fresh receivables provision; capex raised to Rs 200 Cr+ against 0.30x CFO). No trim ladder applies (not held).

### 8C. Single cleanest metric for next quarter
**H1FY27 CFO/PAT ratio** (disclosed in the mandatory Q2 half-yearly cash-flow statement). The single cleanest resolver of the bull/bear split because the entire DA thesis pivots on structural cash conversion, and Q2 is the first FY27 quarter where CFO is disclosed.
- **Bull threshold:** H1FY27 CFO/PAT > 0.50x (relieves the central crack; fires Notion re-evaluate trigger 4 if repeated).
- **Bear threshold:** H1FY27 CFO/PAT < 0.30x (confirms the structural crack; moves thesis-broken trigger 2 toward firing).
- **Secondary metric:** H1FY27 operating EBITDA margin vs the 33% thesis-broken line and the 35-40% guidance.

🛑 Position decision (8A-W), trigger refinement, and single cleanest metric shown.

---

## STEP 8.5 — QUESTIONS FOR MANAGEMENT (from the filing/deck, pre-committed before the call)

Every A3 FORWARD-SIGNAL and AMBIGUOUS finding maps to ≥1 row (`from_finding_id`); CONFIRMATORY-NEGATIVE silence items also converted per the A3 instruction. Ordered by materiality to thesis. **These 18 were the pre-committed questions submitted for / expected at the 31-Jul-2026 call; the ADDENDUM below grades how the call answered each.**

| # | Question | Why it matters | Bull answer | Bear answer | from_finding_id |
|---|---|---|---|---|---|
| 1 | What was Q1FY27 CFO and closing receivable days? Exact figures. | Q1 cash undisclosed for a 0.234x cumulative CFO/PAT company — central crack (Cat D) | Specific CFO with days falling below ~300 | "We report cash half-yearly" / no number | A3-F16-02 |
| 2 | Of the Rs 2,654 Cr order book, how much is signed vs "negotiated and pending receipt"? | Confirmed book only Rs 927.7 Cr; ~65% soft (Cat E) | Signed >Rs 1,500 Cr with named contracts | Refusal / "mostly negotiated" | A3-F16-01 |
| 3 | Q1 operating EBITDA margin 27.0% vs 35-40% FY27 guidance. Walk the H2 bridge. | Tests whether guidance is achievable or promotional (Cat C) | Named mix/volume drivers with cadence | "H2 is always stronger" without specifics | A3-F6-01, A3-F6-02 |
| 4 | Which customer approvals delayed, on which programmes, and what revenue quantum slipped? | "Temporary delays" is the unevidenced word for the soft print (Cat A) | Named programmes + rupee quantum + recovery quarter | Vague "across the board" / "confidential" | A3-F7-01 |
| 5 | Recurring annual Labour Code P&L impact; why does the standing exceptional line remain blank? | Recurring wage-base step-up feeds the sub-33% margin tripwire (Cat C/D) | Quantified, small, already-in-run-rate | "Still assessing" / no number | DP-F1a, A3-F1-01 |
| 6 | Deployment schedule for Rs 26.25 Cr undeployed QIP proceeds (3.3 yrs on)? | Money raised, not converted to productive capex; cash-trail thesis (Cat F) | Dated deployment plan | Open-ended / further delay | DP-F6a |
| 7 | STAC net worth; true Rs 10 Cr outlay; why did FY26 provisional turnover fall ~5.7%? | Rs 8.5 Cr to clear liabilities implies thin/negative net worth + goodwill drag (Cat F/E) | Positive net worth; turnover dip explained | Negative net worth / distressed | acq F11 |
| 8 | STAC Rs 1.5 Cr equity paid "to the Promoters" yet declared not-RPT — whose promoters, arm's-length basis, incorporation date, country? | Governance: promoter payment + four silent fields (Cat G) | Independent third party; valuation basis given | Related counterparty / evasion | acq F17 |
| 9 | Basis for STAC "1.3-2.0x addressable value per programme"? | Unquantified accretion claim, no basis (Cat A) | Programme examples + math | "Directional / illustrative" | acq F7 |
| 10 | Approvals "Not Applicable" vs "subject to approval, if any" — any defence/CCI/sectoral clearance? | Contradiction; approval surprise could slip the timeline (Cat G) | Clear "none required, here's why" | Contradiction persists | acq F1, acq F14 |
| 11 | Confirm STAC completion date and first-ever consolidated-accounts date. | First consolidation event in company history (Cat F/G) | Firm date + Q2/Q3 consolidation | Slippage / vague | acq F6, F13, F15, A3-F15-01 |
| 12 | BrahMos seeker — timeline and value for conversion to serial production order (>Rs 500 Cr trigger)? | Catalyst tested but unconverted (Cat B/E) | Named timeline + indicative value | "In discussions" | A3-F6-06 |
| 13 | International OB only Rs 39 Cr while exports 22.1% of Q1 revenue — forward export pipeline; is the book declining? | Confirms declining-export thesis; export OB near Rs 30 Cr tripwire (Cat E) | New export orders named | Book falling toward Rs 30 Cr | A3-F6-07 |
| 14 | Quarterly inflow cadence for Rs 2,000 Cr / Rs 20-40bn targets vs Rs 117 Cr Q1 inflow? | Q1 inflow far below the implied run-rate (Cat B) | Named large-order timing | Backloaded / vague | A3-F6-03, A3-F6-04 |
| 15 | Rs 150 cr 2-yr capex against ~0.30x CFO/PAT — funding; does it draw the net cash? | Capex vs weak cash generation (Cat F) | Internal accrual + clear envelope | Net-cash drawdown without trail | A3-F6-05 |
| 16 | Deloitte report signed 16:34:57 vs board concluded 18:30 while asserting board approval — explain sequencing. | Governance-hygiene / control signal (Cat G) | Audit Committee approved early | No coherent explanation | DP-F14a |
| 17 | FY26 OCI flipped to +Rs 0.6 Cr after a 5-yr actuarial-loss streak — assumption change? | Assumption-change candidate; verify at AR (Cat D) | Assumptions unchanged, explained | Opaque | A3-F9-01 |
| 18 | Current status of the EW-suite tender (L1) and the AMCA RFP/award — both absent from the deck? | Two thesis catalysts silent (Cat E) | Concrete status update | Continued silence | checklist items 7 & 9 |

### STEP 8.5 ADDENDUM — ANSWER-STATUS GRADE OF ALL 18 (post-concall, cross-protocol per Role 5 §3E / Role 4 non-negotiable "track answer status across quarters")

Grades: **ANSWERED-SPECIFICALLY / PARTIAL / EVADED / NOT-ADDRESSED**, each with a concall turn cite. This is the authoritative grading required this run; it reconciles A3's draft grid.

| # | Pre-committed question (abbrev.) | Grade | Concall cite | What was said / why the grade |
|---|---|---|---|---|
| 1 | Q1 CFO + closing receivable days | **NOT-ADDRESSED** | turn 11 (cash Rs 530 Cr only); turn 17 (~Rs 2 Cr provision, no DSO, no CFO) | No CFO/OCF figure, no DSO. Closing cash given but conflicts with deck. |
| 2 | Signed vs negotiated split of Rs 2,654 Cr | **PARTIAL** | turns 9/11 (Rs 920 Cr confirmed + Rs 1,726 Cr negotiated) | Two-bucket split given; but the finer production-vs-development cut REFUSED (see #—/A3-08). |
| 3 | H2 bridge from 27% to 35-40% EBITDA | **PARTIAL (qualitative)** | turns 35/37 ("didn't have lower margin … uneven revenue … confident of full year") | No quantified bridge; defensive framing that Q1 margin is a distribution artifact. |
| 4 | Which approvals delayed + revenue quantum slipped | **EVADED (quantum)** | turn 21 ("we can't be specific because it involves customers … can't talk about open channel") | Slippage direction admitted; magnitude withheld. |
| 5 | Recurring Labour Code P&L impact | **NOT-ADDRESSED** | (no utterance) | Employee-cost drag flagged generically (turn 9) but no Labour-Code quantum. |
| 6 | QIP Rs 26.25 Cr deployment schedule | **NOT-ADDRESSED** | turns 33/117 ("we took money" generic) | No schedule. |
| 7 | STAC net worth / outlay / turnover | **NOT-ADDRESSED** | turn 53 ("small company … yesterday only finalized … too early") | No financials of any kind. |
| 8 | STAC arm's-length + promoter payment + incorporation/country | **NOT-ADDRESSED** | turn 53 (refers to "the promoter of the company," no RPT/arm's-length/country) | Governance fields left blank. |
| 9 | Basis for STAC 1.3-2.0x accretion | **NOT-ADDRESSED** | (no utterance) | Not mentioned. |
| 10 | STAC approvals NA-vs-"if any" | **NOT-ADDRESSED** | (no utterance) | Not mentioned. |
| 11 | STAC completion + first-consolidation date | **PARTIAL** | turn 53 ("yesterday only finalized" ~30-Jul-2026) | Completion effectively dated; consolidation date not given. |
| 12 | BrahMos seeker conversion timeline/value | **PARTIAL** | turn 73 ("this financial year … product intake not the revenue"); turns 91-97 (inside Rs 20bn prospects) | Timeline (FY27 intake) specific; VALUE withheld. |
| 13 | Forward export pipeline vs Rs 39 Cr | **PARTIAL (qualitative)** | turn 49 (UK antenna 6-8m; US civil aviation; "multi-million dollar" — no forward value) | Directional colour; no forward order value. |
| 14 | Inflow cadence Rs 2,000 Cr / Rs 20-40bn vs Rs 117 Cr Q1 | **PARTIAL** | turn 153 ("9 months" self-imposed); turn 25 ("during this FY") | Self-imposed clock; no quarterly cadence. |
| 15 | Rs 150 Cr capex funding vs 0.30x CFO | **EVADED (funding)** | turn 109 (capex RAISED to "Rs 200 Cr+ minimum"; funding not addressed) | Capex quantum specifically raised; funding/net-cash-draw question not answered. |
| 16 | Auditor 16:34 vs board 18:30 sequencing | **NOT-ADDRESSED** | turn 117 (board meeting referenced; sequencing not) | Governance question not put/answered. |
| 17 | FY26 OCI actuarial swing | **NOT-ADDRESSED** | (no utterance) | Not mentioned. |
| 18 | EW-suite L1 tender + AMCA status | **PARTIAL** | turn 45 (L1 acknowledged on one large contract, value declined); AMCA not named (turn 61 vague) | L1 half acknowledged/unquantified; AMCA half NOT-ADDRESSED. |

**Tally: 0 ANSWERED-SPECIFICALLY | 7 PARTIAL (#2,3,11,12,13,14,18) | 2 EVADED (#4,15) | 9 NOT-ADDRESSED (#1,5,6,7,8,9,10,16,17).** The unanswered mass clusters on (a) **cash conversion / working capital** (#1,6,15,17) and (b) the **day-old STAC acquisition** (#7,8,9,10,11) — the two decision-critical areas for a WATCHLIST/AVOID name whose thesis crack is cash conversion. **Not one of the 18 pre-committed questions received a fully specific answer.** Per Role 4 non-negotiable, repeated evasion/non-address is a governance signal to carry into the Promoter Verdict at Q2 (this is the first tracked cycle — logged as the baseline).

**Top 3 by likelihood of thesis-changing information (as pre-committed):** (1) Q1 CFO + receivable days — NOT-ADDRESSED, so the crack is unresolved and the bear framing holds; (2) signed vs negotiated split — PARTIAL, finer split REFUSED; (3) auditor-vs-board sequencing (#16) + STAC arm's-length (#8) — both NOT-ADDRESSED, the two cleanest transparency tests, both failed.

**Channel recommendation:** The concall occurred (31-Jul-2026). The nine NOT-ADDRESSED and two EVADED items should now go out as a **verbatim IR email to Go India Advisors** (the CMD twice invited written follow-up — turns 25, 171: "we will write to the shareholder," "do write to Go India"). Log the email answer-status into the Q2FY27 review.

🛑 Questions table + answer-status addendum + Top 3 + channel shown.

---

# SECTION B — CONCALL ANALYSIS (Role 5) — RUN AGAINST THE ACTUAL 84-TURN TRANSCRIPT

**Source discipline:** primary source is the actual transcript (`extract_concall_datapattns_q1fy27.txt`, 175 native lines / 84 turns; A2 reconciled 100%). The transcript is auto-transcribed and uncorrected (ASR artifacts preserved: "audible"=order book, "EITA"=EBITDA, "Bramos"=BrahMos, "2025%"=20-25%, "Sranga Rajan"=Srinivasagopalan Rangarajan). Where an ASR number is garbled the figure is treated as directional and reconciled against the deck/filing, never anchored on the ASR alone.

## Step 0 — Pre-flight

**0A. Notion:** growth triggers, thesis-broken conditions, checklist as in Section A. **No prior Role-5 concall log on file → this is the BASELINE cycle**; the historical promise-vs-delivery audit is skipped and the commitment register (Step 2 / A3 F6) is baselined from this quarter forward.

**0B. Call participants (A2 ledger §1):**

| Role | Name | Notes |
|---|---|---|
| Hosting / IR (moderator) | Ms. Prayasi Patel, **Go India Advisors** | **House IR firm** (same as the presentation IR) — not an independent broker; opened and closed the call |
| CMD / Chairman (Promoter) | Mr. Srinivasagopalan Rangarajan | **Promoter PRESENT** — delivered opening remarks (turn 9) and, on the register/first-person voice, appears to have answered essentially all 28 Q&A turns |
| CFO | Mr. Venkata Subramanian Venkatachalam | Delivered the prepared financial remarks (turn 11) only; **AMBIGUOUS_SPEAKER flag — all 28 `[A — Mgmt]` Q&A answers are attributed to a generic "Mgmt" tag, so the CFO's individual answer share cannot be verified** |
| COO / other senior | — | Not on the call (deck lists WTD/COO Vijay Ananth K, CTO Desinguraja Parthasarathy — absent) |

**Yellow flags from the participant list:** (1) **Promoter-CMD present and dominant on Q&A → candour-positive** (the protocol's preferred pattern; the opposite of a CFO-only call). (2) But the **CFO appears absent from Q&A** (or indistinguishable) — the standard "CFO answering operational questions" flag is inverted here; the concern instead is that a single voice (the promoter) fielded every substantive question with no CFO cross-check on the financial answers. (3) **House IR (Go India) hosting** — not an independent broker; softball risk, though the buy-side (361 Capital, Bajaad Alternate AIF, Invest Capital) did ask pointed questions. (4) 10 analyst firms engaged — healthy participation.

**0C. Structure/date:** call **31-Jul-2026, 12:30 IST — one day after the 30-Jul-2026 filing** (managed, not same-day-canned). 84 turns; 39 question-turns (28 substantive, 11 session-closing courtesies per A2); 10 analyst firms + 1 individual investor. **Call duration and Q&A-as-%-of-total: ND** (not stated in the transcript). Operator twice invoked the "two questions per participant, rejoin the queue" rule (turns 81, 129) — a sign of an engaged/oversubscribed queue.

**0D. Safe-harbour caveats:** standard forward-looking disclaimer read by the moderator (turn 7: "the discussion … may include certain forward-looking statements and must be therefore viewed in conjunction with the risk that the company may face"). **No unusual new caveat** verbally introduced.

**0E. Business type:** **Standard** operating business → Step 2 guidance set (not the Step 2L lender set).

🛑 Pre-flight complete: promoter present (candour-positive) but CFO Q&A share unverifiable; house IR; managed call one day post-filing; standard business.

## Step 1 — Opening-remarks claims inventory (turns 9 & 11)

| # | Claim | Type | Quantified? | Source turn |
|---|---|---|---|---|
| 1 | Orders secured across avionics, radars, EW, ATE from MoD, VRO, BrahMos | Customer/Order | NO | 9 |
| 2 | Server products transitioned dev → complete system solutions ("expands addressable market") | Strategic | NO | 9 |
| 3 | Order book Rs 2,654 Cr "including negotiation" — "healthy revenue visibility over the coming years" | Customer/Order | YES (soft base) | 9 |
| 4 | International order book Rs 39 Cr | Customer/Order | YES | 9 |
| 5 | "~Rs 2,000 Cr of fresh order inflows during FY27 over and above orders already received and negotiated" | Forward Guidance | YES | 9 |
| 6 | Drone/counter-drone — "started receiving orders," "important growth driver" | Forward Soft | NO | 9 |
| 7 | "Higher employee cost base is expected to remain elevated over the coming quarters" | Forward Guidance (cost) | YES (directional-committed) | 9 |
| 8 | "Changes in the product [mix] also impacted margins" | Backward | NO | 9 |
| 9 | "We remain confident of achieving our full-year guidance … 20-25% revenue growth while maintaining … margins in 35 to 40% range" | Forward Guidance | YES | 9 |
| 10 | Revenue Q1FY27 Rs 116 Cr, +17% YoY | Backward | YES | 11 |
| 11 | Gross profit Rs 91.5 Cr, +16% YoY, GM 78.9% | Backward | YES | 11 |
| 12 | EBITDA Rs 31.4 Cr, margin 27% ("impacted by high employee cost … product mix") | Backward | YES | 11 |
| 13 | PAT Rs 22.1 Cr, margin 19% ("temporary impact due to uneven quarterly revenue") | Backward | YES | 11 |
| 14 | Net-debt-free; cash + bank + investments Rs 530 Cr as on 30-Jun-2026 | Financial | YES | 11 |
| 15 | Confirmed order book Rs 920 Cr as on 30-Jun-2026; with July + negotiated orders, Rs 2,654 Cr | Customer/Order | YES | 11 |

**Diagnostics:**
- **Quantified share of opening claims:** ~10/15 quantified (~0.67).
- **New vs reaffirmed:** the FY27 20-25% / 35-40% bands and the Rs 2,000 Cr inflow target are **reaffirmations** of the deck; the Q1 actuals are **new**; **new negative colour**: the explicit guide that employee-cost drag "is expected to remain elevated over the coming quarters" (turn 9, claim 7 = finding A3-01) — i.e. the 27% margin is **not framed as a one-quarter dip**.
- **Internal contradiction:** the opening pairs "net-debt-free … ample flexibility" and a "strong balance sheet" against **no CFO/OCF disclosure and a fresh Rs 2 Cr provision against long-pending receivables** — the balance-sheet-strength narrative is asserted without the one cash-flow datum that would test it (A3-18).
- **Two spoken figures that do not reconcile to the deck:** cash Rs 530 Cr (deck Rs 465.9 Cr) and confirmed order book Rs 920 Cr (deck Rs 927.7 Cr) — both surface in the opening (A3-13, A3-14), reconciled in Step 7A.

## Step 2 — Forward guidance extraction (Step 2, standard set)

| Metric | This quarter (call) | Last quarter | Two quarters ago | Trajectory | Confidence |
|---|---|---|---|---|---|
| Revenue growth FY27 | 20-25% (turn 9) | ND (no prior log) | ND | New (baseline) | MEDIUM |
| EBITDA margin FY27 | 35-40% (turn 9) | ND | ND | New | **LOW** (Q1 actual 27.0%, 800-1300 bps below; employee-cost drag guided to persist) |
| Order book / pipeline | Confirmed Rs 920 Cr; incl. negotiated Rs 2,654 Cr; single-vendor prospect Rs 20bn / "Rs 20-40bn" (turns 9,11,97) | ND | ND | New | MEDIUM (wide) |
| Order inflow FY27 | ~Rs 2,000 Cr ex-negotiated (turn 9); + "another Rs 2,000 Cr" simulator contracts "during this FY" (turn 25) | ND | ND | New | MEDIUM |
| Capex envelope | **Rs 200 Cr+ "minimum" over next 1-2 yrs (turn 109) — RAISED from deck Rs 150 Cr** | Rs 150 Cr (deck) | ND | **Widened/Raised** | MEDIUM (funding unaddressed) |
| Utilisation target / timeline | ND | ND | ND | — | — |
| Strategic order execution | Rs 1,726 Cr negotiated → confirmed "in ~3 months" (could be 2 wks; delayed from AGM) (turn 25); L1 on one large contract, value withheld (turn 45) | ND | ND | New | LOW (delayed) |
| Working capital / CCC | Not guided (turn 21 qualitative "yearly business") | ND | ND | Not guided | — |
| Net debt trajectory | Maintain net-debt-free (turn 11) | ND | ND | New | HIGH |
| Export / segment | Intl OB Rs 39 Cr; UK antenna delivery 6-8 mo; "multi-million dollar" export in "next few months," scale 2-3 yrs (turns 9, 49) | ND | ND | New | LOW (thin book) |
| New product / contract milestones | SPJ-230 trials before Dec-2026, contract ~2 yr (turn 33); BrahMos seeker intake FY27 (turn 73); hawk-radar breakthrough 2-3 mo, 2nd-gen 6 mo (turn 65) | ND | ND | New | MEDIUM (dates specific, values withheld) |
| Dividend / payout | ND | ND | ND | — | — |

**Diagnostics:**
- **Widen or tighten?** Guidance is **maintained on revenue/margin bands** but **capex RAISED ~33%+** (Rs 150 Cr → Rs 200 Cr+ minimum, turn 109 = A3-15). A capex raise without a funding statement, against ~0.30x CFO/PAT, WIDENS the funding-gap question rather than signalling confidence.
- **Any prior guidance dropped without acknowledgment?** No prior log to test (baseline). But **one commitment is explicitly a repeat carried forward and now delayed**: the Rs 1,726 Cr negotiated-to-confirmed conversion "was asked during our AGM" and has slipped ("additional 6 months … another two months," turn 25).
- **Internal arithmetic consistency:** 20-25% off FY26 Rs 924.77 Cr = Rs 1,109.7-1,155.96 Cr; at Q1 Rs 116.03 Cr, Q2-Q4 must average Rs 331-347 Cr — possible only with the same extreme back-ending as FY26. The **margin band is the weak leg** (Q1 27% vs 35-40%, with cost drag guided to persist). Order-book stack: Rs 920 confirmed + Rs 1,726 negotiated = Rs 2,646, an **Rs 8 Cr gap** vs the stated Rs 2,654 total; the deck's Rs 927.7 Cr closes it (927.7 + 1,726.3 = 2,654.0), so the **spoken Rs 920 Cr is the rounded/soft number** (A3-14).
- **What analysts pressed for that management refused:** the **production-vs-development split of the Rs 2,654 Cr order book — REFUSED twice** (turns 85, 89, A3-08); the **revenue-slippage quantum — EVADED** (turn 21, A3-09); the **Rs 40,000 Cr TAM realization horizon — REFUSED** (turn 165, A3-11); and **values** on SPJ-230, the L1 contract, the BrahMos seeker, and the HAL order — all withheld.

🛑 Guidance table + diagnostics shown — the most critical artifact; capex-raise and the withheld-values pattern are the load-bearing signals.

## Step 3 — Promise vs delivery audit

### 3A/3B. Historical audit — BASELINE (no prior Role-5 concall log)
**First cycle under the protocol.** The trailing-4-quarter historical delivery audit is **skipped**; the commitment register (below) is baselined for the Q2FY27 audit.

**Within-call delivery signals (seed the baseline register, not yet scored):**
- **Rs 1,726 Cr negotiated → confirmed order book:** promised previously (flagged by the CMD as "asked during our AGM"), now **DELAYED** ("taken additional 6 months … the whole program stretched to more than one and a half years … another two months," turn 25). First observed delay → would score 0.25 in a formal cycle; logged.
- **BrahMos seeker commercial order:** "we expect it earlier but there's some delays … anyway before end of this year" (turn 73) → **DELAYED** relative to an earlier expectation; intake (not revenue) guided FY27.
- **Revenue "on track as indicated earlier" (turn 9)** while Q1 came in below the 20-25% pace and core PBT fell — a soft-delivery marker against the company's own "on track" framing.

### 3B (formal). Cumulative track record
| Concall Date | Total Commitments | Delivered | Partially | Missed | Delayed | Dropped | Unclear | Points |
|---|---|---|---|---|---|---|---|---|
| 31-Jul-2026 (Q1FY27) | 19 (register below) | 0 | 0 | 0 | 2 (Rs 1,726 Cr conversion; BrahMos seeker) | 0 | 17 (future-dated, not yet measurable) | **baseline — ratio not computable** |

**Management credibility ratio (trailing 4 concalls):** **NOT COMPUTABLE this cycle.** The v1.1 formula requires a trailing register of scored commitments; with only this baseline cycle, 17 of 19 commitments are future-dated (UNCLEAR — excluded) and the 2 measurable ones are early DELAYs. **No trailing-4-quarter ratio exists → the Role 1 "management delivery track record" input is HELD at the Notion prior (EXEMPLARY promoter) pending the Q2FY27 second data point.** The archetype read below rests on the specificity ratio jointly with the visible delay/evasion pattern, not on a computed credibility number.

**Commitment register (baseline — from A3 F6, dated):**

| Commitment | Implied date | Turn | Status word |
|---|---|---|---|
| FY27 revenue 20-25%, EBITDA 35-40% | FY27 | 9 | committed/confident |
| ~Rs 2,000 Cr fresh order inflows FY27 (ex-negotiated) | FY27 | 9, 25 | confident |
| Rs 1,726 Cr negotiated → confirmed order book | ~3 months | 25 | expect (DELAYED from AGM) |
| Additional ~Rs 2,000 Cr simulator contracts | "during this FY" | 25 | expect |
| SPJ-230 qualification + flight trials | before Dec-2026 | 33 | should-happen |
| SPJ-230 commercial contract | ~2 years | 33 | expect |
| BrahMos seeker order intake (not revenue) | FY27 | 73 | expect (some delays) |
| Counter-drone contracts "fortified" | next 3-6 months | 49 | should-start |
| UK antenna-redesign export delivery | next 6-8 months | 49 | will-deliver |
| Export multi-million-dollar business | next few months → scale 2-3 yrs | 49, 171 | expect |
| Hawk-radar software breakthrough / porting | next 2-3 months | 65 | expect |
| Advanced 2nd-gen hawk-radar ready | next 6 months | 65 | available |
| Air-defence radar contract wins (few thousand Cr) | next 1.5-2 years | 105 | expect |
| Rs 20bn single-vendor prospect converts | 9 months (self-imposed) | 153 | should-happen |
| Space-business investment decision | 3-4 months (~Nov-2026) | 117 | will-decide |
| Capex Rs 200 Cr+ minimum | next 1-2 years | 109 | will-spend |
| EW business "matures to a large stage" | 6 months-1 year | 171 | expect |
| AI-driven products | 1-1.5 years | 171 | come-out-with |
| L1 large-contract announcement | on contract signing | 45 | undergoing negotiation |

### 3C. Pattern recognition (first-cycle read)
- Management gives **specific timelines but consistently withholds values** on the biggest catalysts (SPJ-230, L1, BrahMos seeker, HAL, air-defence radars) — a specificity-on-dates / opacity-on-money asymmetry.
- **Delays already visible** on the two carried-forward commitments (Rs 1,726 Cr; seeker) — the "delay by one quarter/timeline slip" pattern the protocol warns about is present from cycle one.
- Two **outright refusals** (order-book production/development split, TAM horizon) and one **quantum evasion** (revenue slippage) cluster on the questions that most cut the thesis.

### 3D. Promoter Verdict / Management Grade
**No change this cycle** (credibility ratio not computable). Notion "EXEMPLARY promoter" is HELD pending Q2. **Flag logged:** the OVERPROMISER-RISK archetype (Step 6E) plus the 0-of-18 specific-answer rate and two DROPPED-adjacent refusals should be re-tested at Q2; a second cycle of the same pattern would warrant a downgrade.

### 3E. Last quarter's questions — answered?
Handled authoritatively in **Section A Step 8.5 ADDENDUM** (the 18 pre-committed questions graded 0 ANSWERED-SPECIFICALLY / 7 PARTIAL / 2 EVADED / 9 NOT-ADDRESSED). Cross-protocol consistency discharged.

🛑 3A-3E shown. Credibility ratio = baseline/not computable; specificity + evasion pattern carry the read.

## Step 4 — Q&A decomposition (60%+ of effort)

### 4A. Q&A inventory (substantive turns; session-closing courtesies omitted per A2 NO_NEW_QUESTION)

| # | Analyst & firm | Question (1-line) | Category | Response quality | Substance |
|---|---|---|---|---|---|
| 15/17 | Har Kraat, IIFL Capital | Other expenses +64% vs +17% revenue — anything peculiar? | Financial | **A** | R&M for facility revamp + **~Rs 2 Cr provision on long-pending receivables**; "otherwise in line with budget" — specific and decision-relevant |
| 19/21 | IIFL Capital | Quantum of revenue slipped from customer-approval delays? | Financial | **D (evasion)** | "we can't be specific because it involves customers … can't talk about open channel" (A3-09) |
| 23/25 | IIFL Capital | Timeline for Rs 1,726 Cr negotiated to convert to order book? | Customer/Order | **B** | "~3 months … could be 2 weeks"; program delayed +6mo then +2mo; **flagged as an AGM repeat** |
| 31/33 | Rishika, Goldman Sachs | SPJ-230 testing update + medium-term revenue contribution | Forward Guidance | **B** | Trials before Dec-2026, contract ~2 yr; **value withheld** ("not appropriate to talk about a future order," "several thousand crores") (A3-02, A3-10) |
| 35/37 | Goldman Sachs | Why lower margins this quarter; FY27 outlook? | Financial | **C** | "actually we didn't have lower margin … uneven revenue" — defensive, **no quantified bridge** (A3-16) |
| 43/45 | Deepen Wakil, Philip Capital | HAL order (>Rs 10bn) conversion timeline & execution | Customer/Order | **B** | 18-24 mo project execution; confirms L1 on **one large contract, value withheld, "undergoing negotiation"** (A3-04) |
| 47/49 | Philip Capital | Counter-drone & export — platform vs subsystem, portfolio | Strategic/Operational | **B** | Active/passive detection + jamming; MoD "10-20 systems" pilots; timelines 3-6mo, 6-8mo — **no values** |
| 51/53 | Philip Capital | STAC (ST Advance) acquisition — rationale, applications | Strategic | **C** | Composites for EW/radar; "yesterday only finalized … too early" — **no financials** (A3-12) |
| 59/61 | Venit Prasad, Invest Capital | Larger platforms as subsystem dev (3-5 yr); Himshakti status | Strategic | **C** | Discursive; "male program and bigger h programs"; "can't comment exactly when the contract" (A3 hedge #6) |
| 63/65 | Invest Capital | Hawk radars — monetization; Su-30 fit | Operational | **B/C** | Software breakthrough 2-3 mo; 2nd-gen 6 mo; discussions with OEMs/Russian counterparts |
| 71/73 | Kavesh Parik, 361 Capital | BrahMos seeker — commercial order timeline | Customer/Order | **B** | "this financial year … product intake not the revenue"; some delays; **value withheld** (A3-03) |
| 75/77 | 361 Capital | New BrahMos subsystems — incremental wallet share; capacity | Customer/Order | **C** | Qualitative; no wallet-share number |
| 83/85 | Neil Obal Sahu, JM Financial | Order book Rs 2,600 Cr — production vs development split? | Customer/Order | **E (refusal)** | "I don't know. I'm not classified accordingly" (A3-08) |
| 87/89 | JM Financial | Will you provide a classification? | Customer/Order | **E (refusal)** | "I have not classified it … I don't have a needed answer" — **second consecutive refusal** (A3-08) |
| 91/93 | JM Financial | Does Rs 20-40bn prospect include HAL + BrahMos seeker? | Customer/Order | **B** | Yes — "everything is potential until the contract comes" |
| 99/101 | JM Financial | HAL order in same prospect bucket? | Customer/Order | **B** | Yes, inside the "additional 20 billion" prospect pool, not the negotiated bucket |
| 103/105 | JM Financial | Other prospects beyond BrahMos → production in 2-3 yrs | Strategic | **B** | Air-defence long-range radars, "few thousand crores," 1.5-2 yr; TAM ~Rs 40-50k Cr |
| 107/109 | JM Financial | Capex plan next two years? | Financial | **B** | **Rs 200 Cr+ "minimum"** — building, clean rooms, integration, AI/servers; **funding not addressed** (A3-15) |
| 115/117 | "Arab," individual investor | Space business — stance now (deferred ~1-2 yr ago)? | Strategic | **B** | Decision in 3-4 mo (~Nov-2026); contingent on govt funding; "still unsure" (A3-05) |
| 119/121 | Individual investor | Subsidiary (composites) — value-add plan? | Strategic | **B/C** | Adds markets/process/investment; qualitative |
| 131/133 | Krishnan Sha, DAM Capital | Astra Microwave as DCP partner for hawk radar? | Operational | **B** | "hawk radar is ours; no partner" |
| 135/137 | DAM Capital | Clarify DCP-partner role | Operational | **B** | AA is DCP for LCA variant; parallel development streams |
| 139/141 | DAM Capital | DRDO software / Astra hardware split; DRDO integration? | Operational | **B** | Parallel path; DP can source/develop software elsewhere; "both are possible" |
| 147/149 | Abijit Singh, Systematix | Naval program — plans to raise naval-platform share? | Strategic | **B/C** | Sonar subsystems via BEL; 2 naval radars won; jammer upgrades in flight-trial stage |
| 151/153 | Systematix | Risk of Rs 20bn inflow slipping to FY28? | Forward Guidance | **B** | Tenders "already on"; **self-imposed 9-month clock** (A3-06) |
| 159/161 | Bhavya Gandhi, Bajaad Alternate (AIF) | Addressable market for key products; counter-drone outlook | Strategic | **B/C** | TAM ~Rs 40,000 Cr (Rs 30,000 + Rs 10-12,000); counter-drone "beginning stages," can't size |
| 163/165 | Bajaad Alternate | Rs 40,000 Cr TAM over how many years? | Forward Guidance | **E (refusal)** | "I don't want to say this because I have no control over the market" (A3-11) |

**Grade distribution:** A: 1 (turn 17) | B: ~16 | C: ~6 | D: 1 (turn 21) | E: 3 (turns 85, 89, 165). No fully specific (A) answer on any of the four thesis-critical **value** questions.

### 4B. Question-pattern analysis
- **Most-repeated topic:** the **order-book / negotiated-pipeline conversion** cluster — 6 distinct turns across 4 firms (IIFL, Philip, JM Financial x-multiple, Systematix). Per the protocol, a question asked by multiple analysts = the market does not trust the first answer. Here the repeated pushback met a **double refusal** on the production/development split — the market is probing order **quality** and management will not disclose it.
- **Topics graded C/D/E (management does not want discussed):** order-book composition (E, E), revenue-slippage quantum (D), TAM horizon (E), margin bridge (C). These are precisely the thesis-critical cuts.
- **Buy-side vs sell-side split:** buy-side present and sharp — 361 Capital, Bajaad Alternate (AIF), Invest Capital asked the hardest catalyst/quality questions; sell-side (IIFL, Goldman, JM, DAM, Philip, Systematix) covered order book/margins. **Buy-side participation is healthy** (not a yellow flag).
- **House-broker softball?** Go India (house IR) only moderated; the first substantive question came from IIFL (independent) on the +64% other-expenses — **not** an orchestrated softball open.
- **Analyst pushback:** JM Financial pushed back after the first refusal (turn 87, "will you have a classification") and was refused again — a rare double-refusal, marking order-book quality as genuinely contested.

### 4C. Three most important Q&A exchanges

**Exchange 1 — Order-book production vs development split (turns 83-89, JM Financial).**
- Q: "Can you give us some colour of how much of these [Rs 2,600 Cr] are production and what level would be development orders?"
- A: "I don't know. I'm not classified accordingly." → follow-up → "I have not classified it … I don't have a needed answer."
- **Said specifically:** nothing — a clean double-refusal.
- **NOT said:** any split of the order book by revenue-recognition quality.
- **Thesis implication:** the single most decision-relevant cut of the Rs 2,654 Cr headline (which is already ~65% negotiated/soft per A3-F16-01). Development orders carry execution/qualification risk and lumpier, later cash; production orders convert faster. Refusing the split **sustains opacity on order quality** and, combined with the ~Rs 2 Cr receivables provision, is bearish for cash conversion.
- **Follow-up we would have asked:** "Then what share of Rs 116 Cr Q1 revenue came from development-stage contracts, and what is the trade-receivable balance against them?"

**Exchange 2 — Revenue-slippage quantum (turns 19-21, IIFL Capital).**
- Q: "Is there any quantum of revenue that basically slipped from recognition this quarter because of [customer-approval delays]?"
- A: "We can't be specific because it involves customers and I can't talk about open channel … products are ready but inspection doesn't come … we are not a quarter to quarter business, we are a yearly business."
- **Said specifically:** slippage direction confirmed (revenue was deferred, not lost) and framed as recurring/seasonal.
- **NOT said:** the rupee quantum.
- **Thesis implication:** "temporary delays in customer approvals" is management's unevidenced characterisation of the soft print; refusing the quantum means the −526 bps margin and −5.3% core-PBT cannot be attributed to timing with confidence. Lean bear until the H2 recovery is visible in the numbers.
- **Follow-up we would have asked:** "Roughly what revenue is inspection-ready but unbilled at 30-Jun, and how much has been recognised in July?"

**Exchange 3 — Other-expenses +64% explained (turns 15-17, IIFL Capital).**
- Q: "Other expenses have risen 64% despite only 17% revenue growth — anything peculiar?"
- A: "Increase … is due to some additional repairs and maintenance because the facility is going through revamping … and close to Rs 2 crore we have additionally provided for against the long-pending receivables as per our policy. Otherwise it's in line with our budget."
- **Said specifically:** the two drivers, one quantified (~Rs 2 Cr provision).
- **NOT said:** the R&M amount, and the age/size of the "long-pending receivables" being provided against.
- **Thesis implication:** this is the one Grade-A answer of the call — and its content is **bearish**. A fresh provision against long-pending receivables is direct evidence on the receivables/cash-conversion crack (the DA's central thesis), disclosed in the same call where CFO and DSO were withheld. It resolves the Role 4 "+64% unexplained" flag but replaces it with a credit-quality signal on the receivable book.
- **Follow-up we would have asked:** "What is the gross value and ageing of the receivables pool that required this provision, and is the provision expected to recur in H2?"

🛑 4A-4C shown — the heart of the analysis. Order quality is the contested topic; the one specific answer (other-expenses) is itself bearish on receivables.

## Step 5 — New information audit

### 5A. New disclosures
| Disclosure | Type | Material? | Thesis impact |
|---|---|---|---|
| **~Rs 2 Cr additional provision against long-pending receivables** (turn 17) | Negative surprise (credit quality) | **YES** | Direct evidence on the receivables/cash-conversion crack; disclosed alongside CFO/DSO silence |
| **Capex RAISED to "Rs 200 Cr+ minimum" over 1-2 yrs** (turn 109) | New capex | **YES** | +33%+ vs deck Rs 150 Cr; funding vs 0.30x CFO unaddressed — widens funding-gap watch (A3-15) |
| **L1 confirmed on one large contract, value withheld, under negotiation** (turn 45) | Customer/Order | **YES** | Near-term catalyst if it converts; value opacity (A3-04) |
| **BrahMos seeker — order INTAKE expected FY27 (not revenue), value withheld** (turn 73) | Customer/Order | **YES** | Catalyst advances to guided-intake; still unquantified/unconverted (A3-03) |
| **Rs 1,726 Cr negotiated conversion DELAYED from AGM (+6mo, +2mo)** (turn 25) | Order/timeline | **YES** | Delivery-slippage marker on a carried-forward promise |
| Cash Rs 530 Cr spoken vs Rs 465.9 Cr deck — **Rs 64 Cr unreconciled gap** (turn 11) | Financial/reconciliation | **YES** | Balance-sheet number does not tie across sources (A3-13) |
| SPJ-230 flight trials before Dec-2026; contract ~2 yr; "several thousand crores" (turn 33) | New product milestone | YES | Dated milestone; value unquantified (A3-02) |
| Space-business go/no-go decision in ~3-4 months (~Nov-2026), contingent on govt funding (turn 117) | Forward catalyst | YES | Dateable decision point; capital-allocation optionality (A3-05) |
| Rs 20bn single-vendor prospect — self-imposed 9-month clock (turn 153) | Order/pipeline | YES | Management-set deadline to hold them to (A3-06) |
| TAM ~Rs 40,000 Cr (Rs 30,000 + Rs 10-12,000) (turns 105, 161) | Strategic/scale | Modest | Directional scale claim, realization horizon refused (A3-11, A3-17) |
| Counter-drone orders "started"; MoD 10-20-system pilots per vendor (turn 49) | New product traction | Modest | Early-stage; cannot be sized |
| STAC = composites supplier to Bharat Electronics; deal "yesterday finalized" (turn 53) | M&A colour | Modest | First subsidiary; no financials (A3-12) |

### 5B. What was NOT discussed (silence audit — A3 F17)
| Expected topic | Why it should appear | Significance of silence |
|---|---|---|
| **Q1FY27 CFO / OCF and receivable days** | Central thesis crack (0.234x cumulative CFO/PAT); volunteered a receivables provision but not the metric | **RED** — the single most decision-relevant current datum, withheld (A3-18) |
| **AMCA RFP / award** | Notion catalyst + thesis-broken trigger 3 | **AMBER-to-RED** — not named; turn 61 "male program and bigger h programs" is not AMCA |
| **QIP Rs 26.25 Cr deployment schedule** | 3.3 yrs undeployed; cash-trail thesis | **AMBER** — "we took money" generic, no schedule (turns 33, 117) |
| **Recurring Labour Code P&L quantum** | Feeds the sub-33% margin tripwire | **AMBER** — employee-cost drag flagged generically, no Labour-Code number |
| **STAC financials (net worth/outlay/turnover/arm's-length/country/approvals/consolidation date)** | Day-old first-ever subsidiary; Rs 1.5 Cr paid to promoters, not-RPT | **AMBER-to-RED** — 8 pre-committed fields all NOT-ADDRESSED (A3-12) |
| **Auditor 16:34 vs board 18:30 sequencing** | Governance-hygiene signal | **AMBER** — board meeting referenced (turn 117), sequencing not |
| **FY26 OCI actuarial swing** | Assumption-change candidate | **AMBER** — not mentioned |
| **Customer concentration** | BrahMos + export ~49% | Neutral-to-AMBER — not addressed |

## Step 6 — Tone & specificity

### 6A. Tone comparison
No prior transcript on file → **baseline**. Register: the **promoter-CMD is candid and expansive on strategy/technology** (long, detailed answers on radars, EW, counter-drone) but **defensive-and-opaque on the two numbers that matter** — revenue slippage ("we can't be specific," "bear with me for some time," "you need to be patient") and order-book quality ("I have not classified it"). Margin framing is defensive ("actually we didn't have lower margin"). The tone pairs **strategic confidence with financial evasion**.

### 6B. Specificity score
- Quantified forward statements: ~18 (dated milestones/numbers in the commitment register).
- Unquantified/directional forward statements: ~11 (revenue "met QoQ as we go along," "grow very fast," "repeat contracts," counter-drone "growth driver," SPJ-230 "several thousand crores," L1 value withheld, TAM horizon refused, export "substantially," subsidiary value-add, "well positioned," "sky's the limit").
- **Specificity ratio ≈ 18 / 29 ≈ 0.62** → nominally "moderate-to-high" (>0.5).
- **Critical asymmetry:** specificity is on **dates/timelines**, not on **values**. The four biggest catalysts (SPJ-230, L1, BrahMos seeker, HAL order) each have a **date but no rupee value**; the order-book quality split and the TAM horizon are refused outright. **Specificity here does not equal substance** (v1.1 warning) — the most specific claim (35-40% FY27 margin) is contradicted by the 27% Q1 actual with an unquantified H2 bridge.

### 6C. Defensive-language count (A2 §6 lexicon)
**14 hedge instances across 12 management turns** (>5 = hedge-heavy call). The load-bearing ones: the **double refusal** on order-book classification (turns 85, 89), the **quantum refusal** on revenue slippage (turn 21), the **TAM-horizon refusal** (turn 165), and "too early … yesterday only finalized" on STAC (turn 53). No prior call to trend against; 14 is high in absolute terms.

### 6D. Confidence indicators
- **Promoter-CMD on the call answering essentially every operational/strategic question directly** (candour-positive).
- Named milestones with **specific dates** (Dec-2026 SPJ-230 trials; 3-4-month space decision; 9-month single-vendor clock; 2-3-month hawk breakthrough).
- Specific Q1 P&L that reconciles to the filing (turn 11).
- **Counterweight:** every confidence indicator is a date; the rupee values behind them are withheld, and the one hard balance-sheet number (cash) does not tie to the deck.

### 6E. Management archetype — Specificity × Credibility 2×2
- Specificity ratio ≈ 0.62 (**>0.5**).
- Credibility ratio: **not computable** (baseline cycle) — but the **within-call evidence is delay + refusal + value-opacity**, i.e. pointing below the 60% line rather than above it.
- **Archetype: OVERPROMISER-RISK (the danger quadrant) — CONFIRMED from the prior run's provisional call.** High specificity on timelines, poor/untracked delivery, hyper-specific guidance (35-40% margin) that Q1 already undershoots, and the softness pre-excused as "temporary delays." **Per the quadrant rule: treat ALL forward guidance as promotional; anchor exclusively to filing numbers; require pre-committed thresholds (not narrative) for any position action.** Re-classify formally at Q2FY27 once a delivery data point exists; a second cycle of the same pattern converts OVERPROMISER-RISK to OVERPROMISER and triggers a Promoter-Verdict downgrade.

🛑 6A-6E shown.

## Step 7 — Cross-reference vs filing and peers

### 7A. Concall narrative vs filing/deck numbers
| Concall claim | Filing/deck evidence | Reconciliation |
|---|---|---|
| Revenue Rs 116 Cr / GP Rs 91.5 Cr 78.9% / EBITDA 27% / PAT 19% (turn 11) | Rev 116.03; GP 91.51; Op EBITDA 31.37/27.04%; PAT 22.06/19.01% | **CONFIRMED** (spoken P&L ties to filing at every line) |
| Cash + bank + investments **Rs 530 Cr** (turn 11) | Deck cash/bank/invt **Rs 465.9 Cr** (l.326) | **CONTRADICTED — Rs 64 Cr unreconciled gap** on the same 30-Jun date; per protocol the deck figure is the anchor, spoken figure not credited (A3-13). Management question. |
| Confirmed order book **Rs 920 Cr** (turn 11) | Deck **Rs 927.7 Cr** (l.330) | **PARTIALLY CONFIRMED** — spoken figure rounded; deck value reconciles the Rs 2,654 total (927.7 + 1,726.3 = 2,654.0) (A3-14) |
| Order book Rs 2,654 Cr "healthy revenue visibility over the coming years" (turn 9) | Confirmed book only Rs 927.7 Cr | **PARTIALLY CONFIRMED** — ~65% is negotiated/pending; production/development split refused (A3-F16-01, A3-08) |
| Capex **Rs 200 Cr+ minimum** over 2 yrs (turn 109) | Deck **Rs 150 Cr** (l.182) | **CONTRADICTED (RAISED)** — spoken supersedes; funding vs 0.30x CFO unaddressed (A3-15) |
| "Strong balance sheet … ample flexibility"; "prudent capital allocation" (turn 11) | FY26 CFO/PAT 0.295x; Q1 CFO undisclosed; fresh receivables provision | **CONTRADICTED** by annual cash conversion; unverifiable for Q1 |
| 35-40% FY27 EBITDA (turn 9) | Q1 actual 27.0% | **CONTRADICTED for Q1** (forward; H2 bridge left qualitative) |
| "Revenue trajectory continues on track as indicated earlier" (turn 9) | +16.8% YoY (below 20-25%); core PBT −5.3% | **PARTIALLY CONTRADICTED** — below the guided pace on Q1 |

### 7B. Peer concall cross-check
**No peer transcript (BEL, Astra Microwave, Bharat Forge defence, HAL, Paras Defence) was passed to this review within the ±4-week window. Peer cross-check: NOT PERFORMED — stated explicitly.** One in-call cross-reference of note: the DAM Capital exchange (turns 131-141) touches **Astra Microwave** as a DCP partner on the LCA hawk-radar variant — DP claims an independent parallel development stream; this is a competitive-positioning claim, not a peer-narrative cross-check, and remains unverified against Astra's own call.

### 7C. Concall vs channel checks
ICRA/Notion structural WC assessment (CFO/PAT ~0.30x FY26) **aligns** with the deck's annual cash flow (CFO Rs 80.1 Cr / PAT Rs 271.4 Cr = 0.295x) and is **reinforced** by the call's fresh ~Rs 2 Cr receivables provision; both **contradict** the "strong balance sheet / prudent capital allocation" framing. External/filing source wins per protocol.

🛑 7A-7C shown.

## Step 8 — Thesis & position updates (concall-derived)

### 8A. Growth-trigger status
| Trigger | Pre-concall | Concall evidence | Post-concall |
|---|---|---|---|
| AMCA subsystem | catalyst | Not named (turn 61 vague) | **DELAYED / UNKNOWN** |
| BrahMos serial order >Rs 500 Cr | catalyst | Order intake guided FY27, value withheld (turn 73) | **ON TRACK, UNCONVERTED / UNQUANTIFIED** |
| Export traction | catalyst | PAR-SAT done; UK antenna 6-8mo; OB still Rs 39 Cr | **WEAKENED** (book thin, forward value unquantified) |
| Cash conversion >0.50x | catalyst | CFO silent; fresh receivables provision | **UNKNOWN → leaning WEAKENED** |
| L1 large tender | (new) | L1 confirmed on one large contract, value withheld (turn 45) | **NEW — ON TRACK, unquantified** |

### 8B. Watchlist items — concall-specific
Utilisation: not disclosed. Contract wins: modest/qualitative; **order-book quality split refused** (AMBER→RED). Customer concentration: not addressed (AMBER). Capex: RAISED (funding watch). Overall concall-specific reading: **AMBER, with order-book opacity and the receivables provision as the two negative deltas.**

### 8C. Thesis-broken trigger check (concall view)
**None fired.** Trigger 1 (margin+export) at **AMBER** — 27% margin (1 qtr) with cost drag guided to persist (turn 9) + export OB Rs 39 Cr (just above Rs 30 Cr). Trigger 2 (cash) unmeasurable but the receivables provision is a negative marker.

### 8D. Four-Pillar inputs — concall adjustments
| Pillar | Pre-concall | Concall evidence | Post-concall |
|---|---|---|---|
| Pillar 1 ROCE | FY26 20.8% → ~17.9x | No Q1 ROCE; capex raised (future D&A/asset-base up) | **HOLD** (no FTTCP re-run on a seasonal quarter) |
| Pillar 2 Cash / WC | weak ~0.30x band | CFO silent; fresh receivables provision; capex Rs 200 Cr+ | **HOLD, lean weaker** — no positive cash evidence, one negative marker |
| Pillar 3 EM / catalysts | per EM 45.9 | Seeker intake guided; L1 confirmed; SPJ-230 dated — all value-withheld | **HOLD** (dates without values do not move the score) |
| Strategic Premium | franchise-not-monopoly | STAC vertical integration (Rs 10 Cr); single-credit rule respected | **HOLD** (immaterial) |
**No pillar moves on concall evidence; no destination-PE recompute; Hurdle Ratio still fails on price.**

### 8E. Position decision (8A-W)
**REMAIN WATCHLIST / AVOID.** Decision Status verified WATCHLIST/AVOID → 8A-W (no trim/exit mechanics). The concall (a) **does not fire any thesis-broken trigger**, (b) **does not relieve the cash-conversion crack** (CFO/DSO withheld; fresh receivables provision; capex raised against 0.30x CFO), and (c) **confirms the OVERPROMISER-RISK archetype** (dates specific, values withheld, guidance undershot on margin, two refusals, one evasion). No undisclosed material positive verified (catalysts are dated but unquantified — do not act on concall narrative alone). Credibility ratio not computable → **no Promoter-Verdict change this cycle**; EXEMPLARY prior HELD pending Q2, with the archetype and 0-of-18 specific-answer rate logged for re-test. Master decision gate **PUSHED to H1FY27/Q2FY27 (~Oct 2026)**. Entry zone UNCHANGED; no fair-value recompute.

### 8F. Updated questions for the NEXT review (forward — feed Role 4 Step 8.5 next cycle)
| # | Question | Why it matters | What to watch next concall | from_finding_id |
|---|---|---|---|---|
| 1 | Reconcile cash Rs 530 Cr (call) vs Rs 465.9 Cr (deck) at 30-Jun-2026 — which is the audited figure and what are the Rs 64 Cr of items? | Balance-sheet number does not tie across sources | Q2 half-yearly BS | A3-13 |
| 2 | Production vs development split of the order book (re-ask; refused twice) | Order-book quality is the contested cut | Whether they classify it | A3-08 |
| 3 | Revenue quantum that slipped in Q1 and how much recognised in Q2 (re-ask; evaded) | Tests the "temporary delays" claim | Q2 revenue recovery vs the Rs 331 Cr/qtr H2 need | A3-09 |
| 4 | Capex RAISED to Rs 200 Cr+ — funding source; does it draw the net cash? Deployment schedule incl. the Rs 26.25 Cr QIP | Capex vs 0.30x CFO; cash-trail | Q2 capex-YTD, CWIP, net-cash move | A3-15, DP-F6a |
| 5 | L1 large-contract value and expected announcement date | Near-term catalyst | Contract signing / exchange filing | A3-04 |
| 6 | BrahMos seeker order value and intake timing within FY27 (>Rs 500 Cr re-evaluate trigger) | Catalyst, value withheld | Order filing this FY | A3-03 |
| 7 | Rs 1,726 Cr negotiated conversion — hard date (delayed from AGM, +6mo +2mo) | Delivery-slippage on a carried promise | Confirmed-book step-up at Q2 | commitment/turn 25 |
| 8 | STAC net worth, true outlay, arm's-length basis, country, first-consolidation date | Day-old first subsidiary; governance | First consolidated accounts (Q2/Q3) | A3-12, acq F11/F17 |
| 9 | SPJ-230 order value (several thousand Cr, withheld); Dec-2026 trial outcome | Dated milestone, value withheld | Trial completion by Dec-2026 | A3-02, A3-10 |
| 10 | Rs 20bn single-vendor prospect — which tenders, and the 9-month clock (self-imposed) | Management-set deadline | Conversion by ~Apr-2027 | A3-06 |
| 11 | Space-business go/no-go by ~Nov-2026 and the capital committed if go | Capital-allocation optionality | Board decision ~Nov-2026 | A3-05 |
| 12 | Rs 40,000 Cr TAM realization horizon (refused) | Scale claim without cadence | Any dating of the TAM | A3-11, A3-17 |
| 13 | Recurring Labour Code P&L quantum; FY26 OCI actuarial-swing assumptions (both not addressed) | Margin tripwire; assumption change | AR disclosure | DP-F1a, A3-F9-01 |
| 14 | AMCA RFP/award status (not named on call) | Notion catalyst + trigger 3 | Any AMCA subsystem award | checklist item 9 |
| 15 | Auditor 16:34 vs board 18:30 sequencing (not addressed) | Governance hygiene | IR email response | DP-F14a |

🛑 8A-8F shown.

## Concall Verdict (Step 9 block)
- **Management Credibility (this quarter):** NOT COMPUTABLE (baseline cycle — no prior Role-5 register). Provisional read from within-call evidence: **below the 60% line** (0-of-18 pre-committed questions answered specifically; 2 refusals; 1 quantum evasion; 2 carried-forward commitments already delayed).
- **Trailing 4-Quarter Credibility Ratio:** N/A (baseline; formula needs a prior register). Role 1 track-record input HELD at the Notion prior.
- **Specificity Ratio:** ≈ 0.62 (moderate-to-high) — but timelines-specific / values-withheld; specificity ≠ substance here.
- **Management Archetype (6E): OVERPROMISER-RISK (danger quadrant) — CONFIRMED.** Treat all guidance as promotional; anchor to filing numbers; require pre-committed thresholds for any action.
- **Net concall impact on thesis: WEAKENED (at the margin).** No trigger fired; cash crack unrelieved and mildly deepened (receivables provision, capex raise, cash-figure gap).
- **Position decision: REMAIN WATCHLIST / AVOID (8A-W); entry zone unchanged; master gate pushed to Q2FY27.**

---

# SECTION C — COMBINED VERDICT

**Standalone AND consolidated:** **standalone = consolidated this quarter** — Note 5 (l.209) confirms zero subsidiaries/associates/JVs as on 30-Jun-2026, so no consolidated statement exists and the **S-vs-C PAT gap is structurally 0.0% for all four periods** (A3 F2 = N.A. by nonexistence, not omission). **This changes next quarter:** STAC ("ST Advance," acquisition "yesterday only finalized," concall turn 53) becomes DP's **first-ever subsidiary** on completion (~end Oct 2026), so Q2/Q3 FY27 will carry the first consolidated P&L/BS with goodwill and a component-audit scope (acq F13/F15, A3-F15-01, A3-12) — a monitorable, not a current gap.

**Filing-derived signals:** revenue +16.8% YoY but **operating EBITDA −2.2%, core operating PBT −5.3%, PAT −13.5%**; margin compressed 526 bps to 27.0%; the growth headline **masks operating deterioration**. Net cash intact; auditor unmodified. Q1 cash conversion **INDETERMINATE** (Reg-33 permits omission at Q1). The +64% other-expenses jump is now **explained** (concall turn 17): facility-revamp R&M + **~Rs 2 Cr provision against long-pending receivables** — a credit-quality charge on the receivable book.

**Concall-derived signals:** spoken P&L ties to the filing (CONFIRMED); but **cash Rs 530 Cr vs deck Rs 465.9 Cr is a Rs 64 Cr unreconciled gap**, confirmed order book Rs 920 vs Rs 927.7 Cr, and **capex RAISED to Rs 200 Cr+ minimum vs deck Rs 150 Cr** with funding unaddressed. Guidance (20-25% rev / 35-40% EBITDA) undershot on Q1 margin with cost drag guided to persist; H2 bridge left qualitative. Order-book **production/development split REFUSED twice**; revenue-slippage quantum **EVADED**; L1 confirmed (value withheld); BrahMos seeker **intake** guided FY27 (value withheld). Archetype **OVERPROMISER-RISK — CONFIRMED**. **0 of 18 pre-committed questions answered specifically** (7 PARTIAL, 2 EVADED, 9 NOT-ADDRESSED).

**Reconciliation between the two:** the P&L reconciles across filing/deck/call; the divergences are (a) **narrative vs numbers** — "strong balance sheet / prudent capital allocation" vs 0.30x FY26 cash conversion, undisclosed Q1 CFO, and a fresh receivables provision; and (b) **spoken vs deck** on cash (Rs 64 Cr gap) and capex (raised). **Filing/deck wins for valuation and cash; the concall informs credibility (OVERPROMISER-RISK) and forward catalysts (dated but value-withheld).**

**Net thesis impact: MAINTAINED at WATCHLIST / AVOID (weakened at the margin).** No thesis-broken trigger fired; valuation gate unchanged (CMP ~4.7-5.3x above entry). The quarter and the call **marginally strengthen the AVOID** (margin + core-PBT softness, receivables provision, capex raise, cash-figure gap, order-book opacity) without firing any exit condition.

**Position decision (8A-W):** **REMAIN WATCHLIST / AVOID; entry zone UNCHANGED (Rs 770-867; DA Rs 693-770); master decision gate PUSHED to H1FY27/Q2FY27 (~Oct 2026)** — the window that delivers the mandatory CFO/PAT reading, a second margin quarter, and the first consolidated accounts. No fair-value recompute (no new annual data).

**PROTOCOL VERDICT: PROCEED WITH CAVEATS.** Cash conversion is **INDETERMINATE** for the quarter → per house rule this caps the verdict at PROCEED WITH CAVEATS and may **not** resolve to PROCEED. **Missing evidence named:** Q1FY27 CFO, receivable days, capex-YTD, the signed-vs-negotiated (and production-vs-development) split of the Rs 2,654 Cr order book, and the reconciliation of the Rs 64 Cr cash gap. **Flags propagate (surfaced prominently, human decides):** (1) governance sequencing — auditor signed 16:34 vs board concluded 18:30 (DP-F14a; NOT-ADDRESSED on call); (2) STAC arm's-length silence on a Rs 1.5 Cr promoter payment declared not-RPT (acq F17; NOT-ADDRESSED); (3) STAC approval contradiction "Not Applicable" vs "if any" (acq F1/F14); (4) dual order-book basis / ~65% soft, production/development split REFUSED twice (A3-F16-01, A3-08); (5) cash Rs 530 vs Rs 465.9 Cr Rs 64 Cr gap (A3-13); (6) capex RAISED to Rs 200 Cr+ against 0.30x CFO, funding unaddressed (A3-15); (7) fresh ~Rs 2 Cr receivables provision alongside CFO/DSO silence (turn 17, A3-18); (8) OVERPROMISER-RISK archetype confirmed; 0-of-18 pre-committed questions answered specifically; (9) catalyst silence on AMCA and quantum on EW-L1 (checklist items 7, 9). **No mechanical failure (no halt); no thesis-broken trigger fired.**

---

## MONITORABLES / CATALYST LIST (seeded by A3 commitment registers F6 + board-outcome F13)

| Item | Implied date | Source ref |
|---|---|---|
| STAC acquisition completion (3-mo indicative; "yesterday only finalized" 30-Jul) | ~end Oct 2026 | acq Field 6 l.106-107 (F6); concall turn 53 (A3-12) |
| First-ever consolidated accounts (DP's first subsidiary) | Q2/Q3 FY27 | acq Field 4 l.80-84 (F13/F15) |
| H1FY27 half-yearly CFO/PAT (first FY27 cash reading — SINGLE CLEANEST METRIC) | Q2FY27 results, ~Oct 2026 | Reg-33 half-yearly; Step 5/8C |
| Reconciliation of cash Rs 530 Cr (call) vs Rs 465.9 Cr (deck), Rs 64 Cr gap | Q2 half-yearly BS | concall turn 11 (A3-13) |
| Rs 1,726 Cr negotiated → confirmed order book (delayed from AGM) | ~3 months (~Oct-Nov 2026) | concall turn 25 |
| FY27 revenue growth 20-25% | FY27 | deck l.262 / turn 9 (A3-F6-01, A3-16) |
| FY27 EBITDA margin 35-40% (vs 27.0% Q1; cost drag guided to persist) | FY27 | deck l.262 / turns 9, 37 (A3-F6-02, A3-01) |
| Rs 2,000 Cr FY27 order inflow (ex-negotiated) + "another Rs 2,000 Cr" simulator contracts | FY27 | deck l.526 / turns 9, 25 (A3-F6-03) |
| Rs 20-40bn / Rs 20bn single-vendor prospect — self-imposed 9-month clock | ~Apr 2027 | deck l.254 / turns 97, 153 (A3-F6-04, A3-06) |
| Capex Rs 200 Cr+ minimum (RAISED from Rs 150 Cr; funding unaddressed) | next 1-2 years (~FY28) | concall turn 109 (A3-15) |
| BrahMos seeker order INTAKE (>Rs 500 Cr re-evaluate trigger; value withheld) | this FY (FY27) | concall turn 73 (A3-03) |
| L1 large-contract announcement (value withheld, under negotiation) | on contract signing | concall turn 45 (A3-04) |
| SPJ-230 qualification + flight trials (contract ~2 yr; "several thousand crores") | before Dec-2026 | concall turn 33 (A3-02) |
| Space-business go/no-go decision (contingent on govt funding) | ~Nov 2026 (3-4 mo) | concall turn 117 (A3-05) |
| QIP Rs 26.25 Cr deployment (Rs 24.65 Cr product dev + Rs 1.60 Cr EMI-EMC) | ongoing since 13-Mar-2023 | Note 4 l.200/202-204 (DP-F6a) |
| Labour Code recurring wage-cost quantum | FY27 run-rate | Note 6 l.211-212 (DP-F1a) |
| Export order book vs Rs 30 Cr tripwire (currently Rs 39 Cr; UK antenna delivery 6-8 mo) | each quarter | deck l.566 / turns 9, 49 (A3-F16-04) |
| AMCA RFP/award status (not named on call) | next disclosure | checklist item 9 |
| Order-book production vs development split (refused twice — IR email re-ask) | next disclosure | concall turns 85, 89 (A3-08) |

*Reviewed 2026-07-31 | Sources: BSE filings 30-Jul-2026 (results SEC/SE/048; acquisition SEC/SE/050; presentation SEC/SE/051); Q1 FY27 earnings concall transcript 31-Jul-2026 12:30 IST (84 turns, Go India Advisors). Role 4 numbers unchanged from the prior run; Role 5 completed against the transcript this run.*

---

```yaml
stage: A4-analyst
company: "DATAPATTNS"
quarter: "q1fy27"
model: claude-opus-4-8
status: complete
docs_merged: [results, presentation, acquisition, concall]
ledger_reconciliation:
  notes: 18
  turns: 84
  slides: 32
  all_reviewed: true
  a3_findings_incorporated: [DP-F1a, DP-F6a, DP-F14a, acq-F1, acq-F6, acq-F7, acq-F11, acq-F13, acq-F14, acq-F15, acq-F17, A3-F1-01, A3-F6-01, A3-F6-02, A3-F6-03, A3-F6-04, A3-F6-05, A3-F6-06, A3-F6-07, A3-F6-08, A3-F7-01, A3-F9-01, A3-F13-01, A3-F14-01, A3-F15-01, A3-F16-01, A3-F16-02, A3-F16-03, A3-F16-04, concall-A3-01, concall-A3-02, concall-A3-03, concall-A3-04, concall-A3-05, concall-A3-06, concall-A3-07, concall-A3-08, concall-A3-09, concall-A3-10, concall-A3-11, concall-A3-12, concall-A3-13, concall-A3-14, concall-A3-15, concall-A3-16, concall-A3-17, concall-A3-18]
protocol_verdict: "PROCEED WITH CAVEATS"
cash_conversion: "INDETERMINATE"
decision_status_verified: "WATCHLIST / AVOID"
position_branch: "8A-W"
sc_gap_pat_pct: [0.0, 0.0, 0.0, 0.0]   # Q1FY26, Q4FY26, Q1FY27, FY26 — no consolidated entity exists (Note 5); STAC is first subsidiary from Q2/Q3 FY27
questions_for_management:
  - {q: "Reconcile cash Rs 530 Cr (call turn 11) vs Rs 465.9 Cr (deck) at 30-Jun-2026 — Rs 64 Cr gap; which is audited and what are the items?", from_finding_id: "concall-A3-13"}
  - {q: "Production vs development split of the Rs 2,654 Cr order book (refused twice, turns 85/89)", from_finding_id: "concall-A3-08"}
  - {q: "Revenue quantum slipped in Q1 and how much recognised in Q2 (evaded, turn 21)", from_finding_id: "concall-A3-09"}
  - {q: "Capex RAISED to Rs 200 Cr+ minimum (turn 109) vs deck Rs 150 Cr — funding vs 0.30x CFO; does it draw net cash; QIP Rs 26.25 Cr deployment", from_finding_id: "concall-A3-15, DP-F6a"}
  - {q: "L1 large-contract value and expected announcement date (value withheld, turn 45)", from_finding_id: "concall-A3-04"}
  - {q: "BrahMos seeker order value and intake timing within FY27 (>Rs 500 Cr trigger; value withheld, turn 73)", from_finding_id: "concall-A3-03"}
  - {q: "Rs 1,726 Cr negotiated conversion — hard date (delayed from AGM +6mo +2mo, turn 25)", from_finding_id: "concall-commitment-turn25"}
  - {q: "STAC net worth, true outlay, arm's-length basis, country, first-consolidation date (all NOT-ADDRESSED, turn 53)", from_finding_id: "concall-A3-12, acq-F11, acq-F17"}
  - {q: "SPJ-230 order value (several thousand Cr, withheld) and Dec-2026 trial outcome (turn 33)", from_finding_id: "concall-A3-02, concall-A3-10"}
  - {q: "Rs 20bn single-vendor prospect — which tenders and the self-imposed 9-month clock (turn 153)", from_finding_id: "concall-A3-06"}
  - {q: "Space-business go/no-go by ~Nov-2026 and capital committed if go (turn 117)", from_finding_id: "concall-A3-05"}
  - {q: "Rs 40,000 Cr TAM realization horizon (refused, turn 165)", from_finding_id: "concall-A3-11, concall-A3-17"}
  - {q: "H2 bridge from 27.0% to 35-40% FY27 EBITDA (qualitative only, turn 37); recurring Labour Code P&L quantum; FY26 OCI assumptions", from_finding_id: "concall-A3-16, DP-F1a, A3-F9-01"}
  - {q: "AMCA RFP/award status (not named on call, turn 61 vague)", from_finding_id: "checklist-item-9-silence"}
  - {q: "Auditor review report signed 16:34 vs board concluded 18:30 — sequencing (NOT-ADDRESSED)", from_finding_id: "DP-F14a"}
monitorables:
  - {item: "STAC acquisition completion (3-mo indicative; finalized 30-Jul)", implied_date: "~2026-10-31", source_ref: "acq Field 6 l.106-107; concall turn 53 (A3-12)"}
  - {item: "First-ever consolidated accounts (first subsidiary)", implied_date: "Q2/Q3 FY27", source_ref: "acq Field 4 l.80-84 (F13/F15)"}
  - {item: "H1FY27 half-yearly CFO/PAT (single cleanest metric)", implied_date: "Q2FY27 ~2026-10", source_ref: "Reg-33 half-yearly; Step 8C"}
  - {item: "Reconcile cash Rs 530 Cr (call) vs Rs 465.9 Cr (deck) — Rs 64 Cr gap", implied_date: "Q2 half-yearly BS ~2026-10", source_ref: "concall turn 11 (A3-13)"}
  - {item: "Rs 1,726 Cr negotiated -> confirmed order book (delayed from AGM)", implied_date: "~2026-10/11 (3 mo)", source_ref: "concall turn 25"}
  - {item: "FY27 revenue growth 20-25%", implied_date: "FY27", source_ref: "deck l.262 / turn 9 (A3-F6-01)"}
  - {item: "FY27 EBITDA margin 35-40% vs 27.0% Q1 (cost drag guided to persist)", implied_date: "FY27", source_ref: "deck l.262 / turns 9,37 (A3-F6-02, A3-01)"}
  - {item: "Rs 2,000 Cr FY27 order inflow ex-negotiated + Rs 2,000 Cr simulator contracts", implied_date: "FY27", source_ref: "deck l.526 / turns 9,25 (A3-F6-03)"}
  - {item: "Rs 20bn single-vendor prospect - self-imposed 9-month clock", implied_date: "~2027-04", source_ref: "concall turns 97,153 (A3-F6-04, A3-06)"}
  - {item: "Capex Rs 200 Cr+ minimum (RAISED from Rs 150 Cr; funding unaddressed)", implied_date: "~FY28 (1-2 yrs)", source_ref: "concall turn 109 (A3-15)"}
  - {item: "BrahMos seeker order intake (>Rs 500 Cr trigger; value withheld)", implied_date: "FY27", source_ref: "concall turn 73 (A3-03)"}
  - {item: "L1 large-contract announcement (value withheld)", implied_date: "on contract signing", source_ref: "concall turn 45 (A3-04)"}
  - {item: "SPJ-230 qualification + flight trials (contract ~2 yr)", implied_date: "before 2026-12", source_ref: "concall turn 33 (A3-02)"}
  - {item: "Space-business go/no-go decision", implied_date: "~2026-11 (3-4 mo)", source_ref: "concall turn 117 (A3-05)"}
  - {item: "QIP Rs 26.25 Cr deployment", implied_date: "ongoing since 2023-03-13", source_ref: "Note 4 l.200/202-204 (DP-F6a)"}
  - {item: "Labour Code recurring wage-cost quantum", implied_date: "FY27 run-rate", source_ref: "Note 6 l.211-212 (DP-F1a)"}
  - {item: "Export order book vs Rs 30 Cr tripwire (now Rs 39 Cr; UK antenna 6-8mo)", implied_date: "each quarter", source_ref: "deck l.566 / turns 9,49 (A3-F16-04)"}
  - {item: "AMCA RFP/award status (not named on call)", implied_date: "next disclosure", source_ref: "checklist item 9; concall turn 61"}
  - {item: "Order-book production vs development split (refused twice — IR email re-ask)", implied_date: "next disclosure", source_ref: "concall turns 85,89 (A3-08)"}
flags:
  - "INDETERMINATE Q1 cash conversion - CFO/DSO/capex-YTD undisclosed on filing, deck, AND call (Reg-33 permits at Q1) - verdict capped at PROCEED WITH CAVEATS (A3-18)"
  - "Cash figure gap: CFO said Rs 530 Cr (call turn 11) vs deck Rs 465.9 Cr at 30-Jun-2026 - Rs 64 Cr unreconciled; deck is the anchor, spoken not credited (A3-13)"
  - "Capex RAISED to Rs 200 Cr+ minimum (call turn 109) vs deck Rs 150 Cr over 2 yr; funding vs ~0.30x CFO/PAT not addressed (A3-15)"
  - "Fresh ~Rs 2 Cr provision against long-pending receivables (call turn 17) disclosed alongside CFO/DSO silence - direct negative evidence on the receivables/cash-conversion crack; explains the +64% other-expenses jump"
  - "Order-book production-vs-development split REFUSED TWICE consecutively (turns 85, 89) - sustained opacity on order quality (A3-08)"
  - "Revenue-slippage quantum EVADED ('can't be specific ... involves customers', turn 21) - the soft print magnitude withheld (A3-09)"
  - "OVERPROMISER-RISK archetype CONFIRMED: specificity ~0.62 but timelines-specific/values-withheld; 35-40% margin guidance undershot at 27% Q1 with qualitative H2 bridge; treat guidance as promotional, anchor to filing"
  - "0 of 18 pre-committed management questions ANSWERED-SPECIFICALLY (7 PARTIAL, 2 EVADED, 9 NOT-ADDRESSED); unanswered mass clusters on cash conversion and the day-old STAC acquisition"
  - "Credibility ratio NOT COMPUTABLE (baseline cycle, no prior Role-5 register); Role 1 track-record input HELD at Notion prior; two carried-forward commitments (Rs 1,726 Cr conversion, BrahMos seeker) already DELAYED"
  - "Governance sequencing: auditor review report signed 16:34:57 vs board concluded 18:30 while asserting board approval (DP-F14a; NOT-ADDRESSED on call)"
  - "STAC arm's-length silence: Rs 1.5 Cr paid to promoters, declared not-RPT; net worth/outlay/country/consolidation-date all NOT-ADDRESSED (acq-F17, A3-12)"
  - "STAC approval contradiction: 'Not Applicable' vs 'subject to approval if any' (acq-F1/F14)"
  - "Dual order-book basis: Rs 2,654 Cr headline vs Rs 927.7 Cr confirmed (~65% negotiated/soft); spoken Rs 920 Cr rounds off the confirmed book (A3-F16-01, A3-14)"
  - "Margin: Q1 operating EBITDA 27.0% vs 35-40% FY27 guidance; core operating PBT -5.3% YoY despite revenue +16.8%; employee-cost drag guided to persist (A3-01, A3-F6-02)"
  - "Catalyst status: L1 confirmed but value withheld (turn 45); BrahMos seeker INTAKE guided FY27, value withheld (turn 73); AMCA not named (turn 61)"
  - "Export order book Rs 39 Cr, near the Rs 30 Cr thesis-broken tripwire; thesis-broken trigger 1 at AMBER (A3-F16-04)"
  - "First-ever subsidiary (STAC) creates consolidation/goodwill scope from Q2/Q3 FY27 (acq-F15, A3-F15-01, A3-12)"
  - "Promoter-CMD present and dominant on Q&A (candour-positive); CFO Q&A share unverifiable (AMBIGUOUS_SPEAKER); house IR (Go India) hosting"
  - "No thesis-broken trigger fired; no mechanical failure; Decision Status remains WATCHLIST/AVOID (8A-W); master gate pushed to H1FY27/Q2FY27"
review_path: "/home/user/inflection-pipeline/runs/datapattns-q1fy27/work/review_datapattns_q1fy27.md"
```
