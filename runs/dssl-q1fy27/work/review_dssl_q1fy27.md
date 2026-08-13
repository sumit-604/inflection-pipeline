# A4 MERGED QUARTERLY REVIEW — Dynacons Systems & Solutions Ltd (DSSL)
## Q1 FY27 (quarter ended 30-Jun-2026) — Role 4 (Results Review Protocol v1.2)

Company: Dynacons Systems & Solutions Ltd (BSE 532365 / NSE DSSL)
Source filing: `results_dssl_q1fy27.pdf` (6 pages), IND-AS Standalone + Consolidated Un-Audited Financial Results with Limited Review Report, Board Meeting 13-Aug-2026.
Doc set in scope: **results only.** Role 5 (Concall Analysis) is **N.A. this run — no concall transcript, presentation deck, or investor call was filed or scheduled with this Board Outcome.** No Role 5 tables are produced; where the protocol references concall answers, this review substitutes the Questions-for-Management pre-commitment set (Step 8.5).

Numeric authority: ALL page-5 P&L values are taken from the A1 CORRECTED OCR-fallback block (extract lines 431-461 Rs lakh; 464-493 Rs crore), NOT the scrambled -layout portion (lines 237-312). Unit as filed = Rs lakh; converted to Rs crore at ÷100 (stated twice on page 5 header and page-6 segment table). EPS rows are per-share (not ÷100).

---

## LEDGER-RECONCILIATION PREAMBLE (contractual, before Step 1)

Ledger contains **5 notes / 0 concall turns / 0 slides**, plus the A2 completeness contract: **2 agenda items / 3 entities / 13 segment rows / 11 auditor paras / 36 line items / 5 signature blocks.** **All reviewed. No ledger row is unreviewed.**

A2 count-test result (all categories `match: yes`, `gate_a2: pass`):
- notes 5/5 (grep initially caught 4/5; note 2 rendered `2}` not `2)`, recovered on re-run)
- agenda_items 2/2
- auditor_paras 11/11 (3 standalone + 8 consolidated; one page-4 letterhead reprint excluded as a pagination artifact, not a paragraph)
- entities 3/3 (1 holding + 2 subsidiaries)
- line_items 36/36 (combined Standalone+Consolidated statement, page 5)
- segment_rows 13/13 (consolidated segment table, page 6)
- signature_blocks 5/5

Two carried extraction facts, both resolved:
1. **Page-5 OCR-fallback correction applied.** The raw pdftotext -layout render of the page-5 combined statement had visibly scrambled column-to-value mapping (year-to-date figures bleeding into quarterly cells). A1 re-derived every page-5 value from the source page image (pdftoppm 400 dpi + tesseract + cell-by-cell visual cross-check) and A3 confirmed the internal formula ties. This review uses ONLY those corrected values.
2. **One flagged casting cell carried, not corrected.** CON Q1FY26 "TCI attributable to Shareholders" is filed at 1,966.53 lakh and fails its own internal tie by exactly 9.58 lakh (PAT-Shareholders 1,961.74 + OCI-Shareholders −4.79 = 1,956.95; and 1,966.53 + NCI 2.77 = 1,969.30 vs the page's own Total comprehensive income 1,959.72). The error is isolated to that single cell on a **restated prior-year comparative**; the Total comprehensive income line itself ties. A1 flagged it as a likely source-filing typo and did NOT silently correct it. Routed to Question-for-Management (F14-01).

A3 findings incorporated: **F1-01, F2-01, F3-01, F6-01, F6-02, F10-01, F12-01, F12-02, F14-01**, plus the full F1-F17 checklist (F4/F5/F7/F8/F9/F13/F15 PASS; F11/F16/F17 N.A.). A3 ledger reconciliation 100%; `gate_a3: pass`.

---

## STEP 0 — PRE-FLIGHT

**0A. Notion thesis (passed inline, live-fetched by orchestrator 2026-08-13).** Decision Status **WATCHLIST / BUY ON DIPS** — verified before any position framing. This is a **non-held name → Step 8A-W branch**, not 8A. This Q1 FY27 print IS the thesis's pre-committed binary buy trigger (Q1 FY27 EBITDA margin + receivables print). CMP (thesis) Rs1,231.6; conservative entry zone Rs851-1,064 (MoS Rs851); CMP sits ~16% above zone top. Gate 0 GOOD 78/160; Emerging Moat 22.7/80 MODEST; evidence gate PROCEED WITH CAVEATS conf 84; FTTCP composite +3 DEEP WATCH. Active flags carried: FLAG-CASH (structural WC), promoter CAUTION, accounting quality 4/10. Sector cap 30x.

**0B. Unit convention.** Filed in Rs lakh (stated twice on page 5, once on page 6). Converted to Rs crore at ÷100. EPS left as Rs/share.

**0C. Share-count changes.** Paid-up equity capital moved from Rs1,272.53 lakh (Q1FY26) to Rs1,273.71 lakh (Q4FY26 and Q1FY27) — a rise of Rs1.18 lakh (~11,800 shares of Rs10) YoY, **unexplained by any note in this filing** (F10-01). Basic-vs-diluted EPS spread is now nil on both books (15.36/15.36 STD; 15.54/15.54 CON), so live dilution is negligible; the share-count change is immaterial to EPS comparability but the corporate action behind it is not disclosed. Share base ~1.2737 cr shares.

**0D. Notes extraction (all 5 read before any growth metric).**

| Note # | Line | Subject | What it says | Rs Cr impact | Period | Comparability impact |
|---|---|---|---|---|---|---|
| 1 | 315-316 | Audit Committee/Board review | Results reviewed by Audit Committee and approved by Board, 13-Aug-2026 | none | Q1FY27 | none |
| 2 | 318-319 | Limited review | Results subject to limited review by statutory auditors (SRE 2410) | none | Q1FY27 | none — moderate assurance, not an audit |
| 3 | 320 | Interim dividend | Rs0.50/share on Rs10 face (5%); cash outgo Rs0.6369 cr | (0.6369) cash | Aug-2026 | none to P&L; capital return |
| 4 | 321-322 | Regrouping | Prior-period figures regrouped/re-arranged "wherever necessary" | ND (not quantified) | comparatives | boilerplate; unquantified — watch alongside Note 5 |
| 5 | 322-331 | New segment | "Technology Workforce Augmentation Services" (TWAS) identified as a focus business segment carved from existing System Integration services; two operating segments now reported; **prior period restated** | ND (bridge not given) | Q1FY27 onward | **MATERIAL** — segment comparatives restated without a quantified bridge; breaks clean segment YoY continuity (F12-01) |

Auditor opinion: **unmodified/clean on both books.** Standalone LRR (3 paras) — no EoM, no going concern, UDIN 26008684GRIDZ7853. Consolidated LRR (8 paras) — unmodified, carries a standard **Other Matter** para (2 unaudited subsidiaries; aggregate revenue Rs2.4950 cr, aggregate PAT Rs0.2322 cr; foreign subsidiary management-furnished under foreign GAAP with only the Ind-AS conversion adjustments audited; domestic subsidiary Cybercons directly reviewed), UDIN 26008684WVDLLB7870. "Our opinion on the Statement is not modified in respect of the above matter." No modification, no qualification.

**0E. Business type.** Standard operating business (IT systems integration + services). Standard Steps 1 and 5 apply; lender variant (1L/5L) not used.

---

## STEP 1 — DATA EXTRACTION TABLE (Rs crore; every cell line-anchored or ND)

### 1A. CONSOLIDATED (source lines 465-493)

| Line Item | Q1 FY26 | Q4 FY26 | Q1 FY27 | FY26 | src line |
|---|---:|---:|---:|---:|---|
| Revenue from Operations (Net Sales) | 328.8517 | 402.4485 | 313.6883 | 1,424.2834 | 465 |
| Other Income | 0.9196 | 2.1301 | 1.5565 | 5.7251 | 466 |
| Total Income | 329.7712 | 404.5787 | 315.2448 | 1,430.0086 | 467 |
| Cost of Materials Consumed | 242.2511 | 325.8927 | 256.5202 | 1,162.3098 | 468 |
| Change in Inventories | 40.2435 | 19.7862 | (3.6118) | 42.0744 | 469 |
| Employee Benefits Expense | 10.8561 | 13.5643 | 13.5288 | 50.2957 | 470 |
| Finance Costs | 4.9415 | 6.7387 | 7.2040 | 23.2019 | 471 |
| Depreciation | 1.4767 | 6.2688 | 8.0892 | 14.5303 | 472 |
| Other Expenses | 3.7214 | 6.8973 | 7.0624 | 23.6753 | 473 |
| Total Expenses | 303.4903 | 379.1479 | 288.7928 | 1,316.0873 | 474 |
| Profit Before Tax | 26.2809 | 25.4308 | 26.4519 | 113.9213 | 475 |
| Tax Expense | 6.6358 | 6.4405 | 6.6564 | 29.1089 | 476 |
| PAT (Net Profit for period) | 19.6451 | 18.9903 | 19.7955 | 84.8124 | 477 |
| PAT attrib. to Shareholders | 19.6174 | 18.9198 | 19.7349 | 84.7352 | 485 |
| PAT attrib. to NCI | 0.0277 | 0.0705 | 0.0607 | 0.0772 | 486 |
| EPS Basic (Rs/sh, reported) | 15.44 | 14.92 | 15.54 | 66.64 | 492 |
| EPS Diluted (Rs/sh, reported) | 15.42 | 14.92 | 15.54 | 66.64 | 493 |
| EPS (share-adjusted) | 15.44 | 14.92 | 15.54 | 66.64 | see 0C — no split/bonus; reported = adjusted |
| Paid-up equity capital | 12.7253 | 12.7371 | 12.7371 | 12.7371 | 491 |

### 1B. STANDALONE (source lines 464-493)

| Line Item | Q1 FY26 | Q4 FY26 | Q1 FY27 | FY26 | src line |
|---|---:|---:|---:|---:|---|
| Revenue from Operations (Net Sales) | 328.6926 | 402.1238 | 311.1933 | 1,422.6729 | 465 |
| Other Income | 0.9196 | 2.1301 | 1.5565 | 5.7251 | 466 |
| Total Income | 329.6122 | 404.2540 | 312.7498 | 1,428.3981 | 467 |
| Cost of Materials Consumed | 242.2365 | 326.3199 | 254.7234 | 1,162.3384 | 468 |
| Change in Inventories | 40.2435 | 19.7862 | (3.6118) | 42.0744 | 469 |
| Employee Benefits Expense | 10.7995 | 12.8492 | 13.1058 | 48.9790 | 470 |
| Finance Costs | 4.9415 | 6.7387 | 7.2040 | 23.2019 | 471 |
| Depreciation | 1.4767 | 6.2688 | 8.0892 | 14.5303 | 472 |
| Other Expenses | 3.6765 | 6.7972 | 7.0502 | 23.5057 | 473 |
| Total Expenses | 303.3743 | 378.7599 | 286.5608 | 1,314.6296 | 474 |
| Profit Before Tax | 26.2379 | 25.4941 | 26.1889 | 113.7685 | 475 |
| Tax Expense | 6.6262 | 6.3650 | 6.6256 | 28.9929 | 476 |
| PAT (Net Profit for period) | 19.6117 | 19.1291 | 19.5634 | 84.7756 | 477 |
| EPS Basic (Rs/sh, reported) | 15.41 | 15.03 | 15.36 | 66.62 | 492 |
| EPS Diluted (Rs/sh, reported) | 15.40 | 15.03 | 15.36 | 66.61 | 493 |
| EPS (share-adjusted) | 15.41 | 15.03 | 15.36 | 66.62 | no split/bonus; reported = adjusted |
| Paid-up equity capital | 12.7253 | 12.7371 | 12.7371 | 12.7371 | 491 |

### 1C. Derived metrics

| Derived Metric | Formula | Basis | Q1 FY26 | Q4 FY26 | Q1 FY27 | FY26 |
|---|---|---|---:|---:|---:|---:|
| Operating EBITDA | PBT + Dep + Fin − OI | CON | 31.7795 | 36.3082 | 40.1886 | 145.9284 |
| Operating EBITDA margin | OpEBITDA / Revenue | CON | 9.66% | 9.02% | 12.81% | 10.25% |
| Operating EBITDA | PBT + Dep + Fin − OI | STD | 31.7365 | 36.3715 | 39.9256 | 145.7756 |
| Operating EBITDA margin | OpEBITDA / Revenue | STD | 9.66% | 9.04% | 12.83% | 10.25% |
| Reported EBITDA | PBT + Dep + Fin | CON | 32.6991 | 38.4383 | 41.7451 | 151.6535 |
| Reported EBITDA margin | RepEBITDA / Revenue | CON | 9.94% | 9.55% | 13.31% | 10.65% |
| Core PBT (ex-OI) | PBT − OI | CON | 25.3613 | 23.3007 | 24.8954 | 108.1962 |
| Other Income / PBT | OI / PBT | CON | 3.50% | 8.38% | 5.88% | 5.03% |
| Effective Tax Rate | Tax / PBT | CON | 25.25% | 25.33% | 25.16% | 25.55% |
| PAT margin (on Revenue) | PAT / Revenue | CON | 5.97% | 4.72% | 6.31% | 5.95% |
| Core PBT (ex-OI) | PBT − OI | STD | 25.3183 | 23.3640 | 24.6324 | 108.0434 |
| Effective Tax Rate | Tax / PBT | STD | 25.25% | 24.97% | 25.30% | 25.48% |

FY26 CON operating EBITDA margin 10.25% ties EXACTLY to the Notion baseline (10.25%) — method validated. Both books track within 2 bps, so subsidiaries barely move margin.

---

## STEP 2 — Q1 YoY COMPARISON (Q1 FY27 vs Q1 FY26) — the most important step

### 2A. CONSOLIDATED

| Metric | Q1 FY26 | Q1 FY27 | YoY % | Verdict |
|---|---:|---:|---:|---|
| Revenue from Operations | 328.8517 | 313.6883 | −4.61% | contracted |
| Operating EBITDA | 31.7795 | 40.1886 | +26.46% | expanded |
| Op EBITDA margin (pp) | 9.66% | 12.81% | +315 bps | expanded |
| Depreciation | 1.4767 | 8.0892 | +447.8% (×5.48) | step-up |
| Finance Costs | 4.9415 | 7.2040 | +45.8% | step-up |
| EBIT (operating) = OpEBITDA − Dep | 30.3028 | 32.0994 | +5.93% | modest |
| Other Income | 0.9196 | 1.5565 | +69.3% | up (small base) |
| **Core Operating PBT (PBT − OI)** | 25.3613 | 24.8954 | **−1.84%** | **contracted** |
| Reported PBT | 26.2809 | 26.4519 | +0.65% | flat |
| PAT | 19.6451 | 19.7955 | +0.77% | flat |
| EPS (share-adjusted) | 15.44 | 15.54 | +0.65% | flat |

### 2B. STANDALONE

| Metric | Q1 FY26 | Q1 FY27 | YoY % | Verdict |
|---|---:|---:|---:|---|
| Revenue from Operations | 328.6926 | 311.1933 | −5.32% | contracted |
| Operating EBITDA | 31.7365 | 39.9256 | +25.80% | expanded |
| Op EBITDA margin (pp) | 9.66% | 12.83% | +317 bps | expanded |
| Depreciation | 1.4767 | 8.0892 | +447.8% (×5.48) | step-up |
| Finance Costs | 4.9415 | 7.2040 | +45.8% | step-up |
| Other Income | 0.9196 | 1.5565 | +69.3% | up (small base) |
| **Core Operating PBT (PBT − OI)** | 25.3183 | 24.6324 | **−2.71%** | **contracted** |
| Reported PBT | 26.2379 | 26.1889 | −0.19% | flat/down |
| PAT | 19.6117 | 19.5634 | −0.25% | flat/down |
| EPS (share-adjusted) | 15.41 | 15.36 | −0.32% | flat/down |

### 2C. Six mandatory diagnostics

1. **Did revenue grow YoY?** No. Consolidated revenue fell 4.61% (313.6883 vs 328.8517); standalone fell 5.32%. Order-book context (Rs2,964cr book, 2.08x per Notion) is NOT disclosed in this filing, so the decline cannot be reconciled to backlog from the document alone. A revenue decline in a name whose thesis rests on a 2x-plus order book is a caution, not yet a break.
2. **Did operating EBITDA margin expand, contract, or stay flat YoY?** Expanded materially. CON Q1FY27 margin 12.81% vs Q1FY26 9.66% = +315 bps; STD 12.83% vs 9.66% = +317 bps. This is a genuine YoY expansion, not sequential noise (Q4FY26 was 9.02% CON, so the move is also sequential +379 bps).
3. **Did core operating PBT (ex-Other Income) grow YoY?** No. CON core operating PBT fell 1.84% (24.8954 vs 25.3613); STD fell 2.71%. **The headline "flat PAT" is worse than it looks: core operating profitability declined YoY on both books.** The margin expansion did not convert to core PBT because of the depreciation and finance-cost step-up below the EBITDA line.
4. **What drove the gap between core operating PBT decline and flat reported PAT?** The gap is small and closed by three offsets: Other Income +0.6369 cr (+69.3%, small base), a lower effective tax rate (CON 25.25% → 25.16%), and on the consolidated book a positive subsidiary swing (+0.2321 cr, see Step-4 gap analysis). None is large; the picture is a flat print resting on non-core help while core operations softened.
5. **Are D&A and finance costs scaling faster than revenue?** Yes, sharply, and this is the central signal. Depreciation rose ×5.48 (+447.8%) and finance costs +45.8% while revenue fell 4.61%. This is a textbook **capex-absorption deficit**: the gross-margin gain (materials + inventory cost fell from 85.90% of revenue to 80.62%, ~528 bps) was almost entirely consumed by depreciation +6.61 cr and finance +2.26 cr, leaving PBT flat. Per A3 F3-01, finance costs and depreciation are IDENTICAL standalone and consolidated in every period, so the entire step-up sits in the **parent book** — an as-a-service / Ind AS 116 lease-capex build that has not yet produced revenue. ROCE compresses mechanically until the leased/as-a-service assets earn.
6. **Is Other Income concentration changing?** Other Income is small throughout (0.92-2.13 cr per quarter; 3.5-8.4% of PBT). It rose 69.3% YoY off a tiny base and is not masking the trajectory. Stripping it does not change the read: core operations softened.

---

## STEP 3 — SEQUENTIAL QoQ TRAJECTORY (Consolidated)

Only three discrete quarters are in this filing (Q1FY26, Q4FY26, Q1FY27) plus the FY26 aggregate. Q2FY26 and Q3FY26 discrete quarters were not filed with this document → **ND** (would require prior filings).

| Quarter | Revenue (Rs cr) | Op EBITDA margin | Core PBT (ex-OI, Rs cr) | One-offs flagged | QoQ run-rate |
|---|---:|---:|---:|---|---|
| Q1 FY26 | 328.8517 | 9.66% | 25.3613 | none in this doc | base |
| Q2 FY26 | ND | ND | ND | ND | ND |
| Q3 FY26 | ND | ND | ND | ND | ND |
| Q4 FY26 | 402.4485 | 9.02% | 23.3007 | actuarial remeasurement 0.3828 cr in OCI (comparative only) | seasonal peak |
| Q1 FY27 | 313.6883 | 12.81% | 24.8954 | none | dip in revenue, jump in margin |

Diagnostics:
- **Run-rate trajectory:** revenue dipped from the Q4 seasonal peak (402.45) to 313.69, and is also below the Q1FY26 base (328.85). Margin stepped up hard (9.02% → 12.81%). So the quarter is a **low-revenue, high-margin** print — the mix that a rising fixed-asset/lease base produces when volume is soft.
- **One-off distortion:** the only sizeable OCI item (38.28 lakh actuarial remeasurement) sits in Q4FY26, a comparative column, not this quarter. Q1FY27 OCI is immaterial (CON total 0.0487 cr).
- **H1-vs-Q4 run-rate / capex-commissioning test:** the ×5.48 depreciation jump signals a fixed-asset (or lease) commissioning between Q1FY26 and Q1FY27, yet revenue did NOT lift above the pre-step base — it fell. Per the protocol's capex-commissioning rule, an asset base that commissions but does not lift run-rate above pre-commissioning levels is a red flag. Here it is directional, not yet confirmable, because the asset addition itself is not disclosed (no balance sheet, no segment assets).
- **Implied Q2FY27 base to hold trajectory:** to keep the trailing four-quarter revenue near the FY26 run-rate (~356 cr/qtr average), Q2FY27 needs to recover toward the 350-400 cr band. This is the single cleanest forward number (Step 8C).

---

## STEP 4 — OPERATIONAL DECOMPOSITION (PAT bridge, Consolidated, Q1FY26 → Q1FY27)

Reported PAT change: +0.1504 cr (19.6451 → 19.7955, +0.77%). Bridge below ties to the PBT change (+0.171) less tax change (+0.0206).

| Component | YoY change (Rs cr) | Recurring? |
|---|---:|---|
| Revenue (net sales) fall | −15.1634 | Recurring |
| Materials + inventory cost (combined) fall | +29.5862 | Recurring (mix/procurement) |
| Employee benefits expense rise | −2.6727 | Recurring |
| Other expenses rise | −3.3410 | Recurring |
| Finance cost rise | −2.2625 | Recurring (post-debt/lease) |
| Depreciation rise | −6.6125 | Recurring (post-capex) |
| Other Income rise | +0.6369 | Non-recurring typically |
| = PBT change | **+0.1710** | |
| Effective tax change | −0.0206 | Mixed |
| **= Reported PAT change** | **+0.1504** | |

Mandatory questions:
- **% of PAT change from recurring core vs non-recurring?** The +0.77% PAT rise is entirely a residual of large offsetting recurring moves. Core operating PBT actually FELL 1.84%; the flat headline is held up partly by Other Income (+0.6369) and a slightly lower tax rate. On a core basis this is a down quarter, not a flat one.
- **If Other Income reverts to prior-year level?** Removing the +0.6369 Other Income uplift pushes PAT below the prior year (run-rate PAT ~19.16 cr vs 19.6451 prior). The print does not stand on its own core legs.
- **Are D&A / finance costs at steady-state or still ramping?** Depreciation went from 1.4767 (Q1FY26) to 6.2688 (Q4FY26) to 8.0892 (Q1FY27) — still rising quarter on quarter, not yet steady-state. Finance costs likewise stepping up (4.9415 → 6.7387 → 7.2040). Steady-state depreciation is not yet visible; the absorption drag will persist into coming quarters until revenue catches the asset base.
- **Tax adjustments inflating/deflating PAT?** No. ETR is stable at 25.0-25.6% across all periods and both books (A3 F8 PASS); no deferred-tax or prior-year tax line. Clean.

---

## STEP 4B — STANDALONE-VS-CONSOLIDATED GAP (first-class metric, A3 F2-01)

| Period | STD PAT | CON PAT | Gap (CON − STD, Rs cr) | Gap % of STD PAT | Note |
|---|---:|---:|---:|---:|---|
| Q1 FY26 | 19.6117 | 19.6451 | +0.0334 | +0.17% | small positive sub contribution |
| Q4 FY26 | 19.1291 | 18.9903 | −0.1388 | −0.73% | subsidiaries a drag |
| Q1 FY27 | 19.5634 | 19.7955 | +0.2321 | +1.19% | subsidiaries additive, ×7 the Q1FY26 level |
| FY26 | 84.7756 | 84.8124 | +0.0368 | +0.04% | full-year sub contribution near-zero |

The gap flipped from a −0.1388 drag in Q4FY26 to +0.2321 in Q1FY27, and the Q1FY27 subsidiary contribution is ~7x the Q1FY26 level (0.0334 → 0.2321). It ties to the auditor's Other Matter disclosure of aggregate subsidiary PAT Rs0.2322 cr (line 189). The mechanical swing is 1.9pp of standalone PAT (below the 5pp materiality threshold), so it does not itself alter the read, but the sign flip and 7x jump on earnings that flow through the Cybercons name warrant a management question (F2-01). Note also: standalone PAT ALONE fell 0.25% YoY; the positive consolidated print (+0.77%) is partly the subsidiary swing dressing up a soft standalone quarter.

---

## STEP 5 — CASH QUALITY & BALANCE SHEET

**Data-availability rule (v1.2):** Reg 33 mandates the cash flow statement and balance sheet only at HALF-YEAR and full-year. This is a **Q1 limited-review filing** — no balance sheet, no cash flow statement, no receivables ageing, no ECL note. Every row below is therefore ND from this document. Next reading at Q2/H1 FY27.

| Metric | Prior period | Current period | Change | Verdict |
|---|---|---|---|---|
| CFO | ND | ND | ND | not filed (Q1) |
| CFO/PAT ratio | ND | ND | ND | not filed (Q1) |
| Capex (PPE + CWIP) | ND | ND | ND | not filed (Q1) |
| FCF (CFO − Capex) | ND | ND | ND | not filed (Q1) |
| Working capital change | ND | ND | ND | not filed (Q1) |
| Receivable days | ND | ND | ND | **cannot clear — key monitorable 2** |
| Inventory days | ND | ND | ND | not filed (Q1) |
| Payable days | ND | ND | ND | not filed (Q1) |
| Cash Conversion Cycle | ND | ND | ND | not filed (Q1) |
| PPE | ND | ND | ND | not filed (Q1) |
| CWIP | ND | ND | ND | not filed (Q1) |
| Net Debt / (Net Cash) | ND | ND | ND | not filed (Q1); finance +45.8% YoY directionally higher |
| Promoter Pledge | ND | ND | ND | NOT FOUND in filing; carried NOT FOUND from prior work |

Mandatory questions:
- **Is CFO/PAT meeting the Pillar 2 cash multiplier (1.00x) assumption?** Cannot be tested this quarter — no cash flow statement. **Cash conversion = INDETERMINATE.** Per house rule this may NOT resolve silently to PROCEED; it caps the verdict at PROCEED WITH CAVEATS with the missing evidence named (CFO, receivables ageing, ECL, WC).
- **Is the WC drag structural or growth-induced?** Cannot be re-tested from this filing. The carried FLAG-CASH (structural WC intensity, cash multiplier 1.00x, no growth offset) stands unchanged. The ×5.48 depreciation and +45.8% finance-cost step-up point directionally to a rising lease/debt load, consistent with the DaaS lease-annuity model, but the balance sheet needed to confirm is absent.
- **Did CWIP capitalize as expected?** The depreciation step-up implies an asset base came on line, but with no PPE/CWIP disclosure the amount capitalised is ND.
- **Did net debt move within range?** ND (no balance sheet). Finance costs +45.8% YoY is the only directional signal, and it points up.

---

## STEP 6 — RECONCILIATION VS THESIS

### 6A. Variance vs Notion projections

Explicit Bear/Base/Bull quarterly projections were not passed inline for this run; the actionable pre-committed reference is the FY26 baseline and the margin/receivables trigger thresholds. Framed against those:

| Metric | Reference | Actual Q1FY27 (CON) | Lands |
|---|---|---:|---|
| Revenue | FY26 run-rate ~356 cr/qtr | 313.6883 | below run-rate (−4.6% YoY) |
| Op EBITDA margin | green ≥11% / red <9% | 12.81% | above green threshold |
| PAT | FY26 84.81 cr (~21.2 cr/qtr) | 19.7955 | slightly below FY26 quarterly run-rate |
| EPS | FY26 66.64 (~16.66/qtr) | 15.54 | below FY26 quarterly run-rate |
| Net Debt | ND | ND | cannot assess |
| ROCE | recovering per FTTCP | ND (no balance sheet) | cannot assess; absorption deficit directionally negative |

Probability re-weighting rule: requires actuals BELOW BEAR on 2+ metrics for 2 CONSECUTIVE quarters. Bear case not passed inline and only one filing in view → **rule not triggered this run**; flagged for the next refresh to test against explicit Bear projections.

### 6B. Watchlist monitorable status (all 6)

| # | Monitorable | Green | Red | This-quarter reading | Status |
|---|---|---|---|---|---|
| 1 | EBITDA margin | ≥11% | <9% two qtrs | CON op EBITDA margin 12.81% (STD 12.83%) | **GREEN** |
| 2 | Trade receivables / ECL & debtor days | ≤154 days | >160, overdue widening, ECL frozen | not disclosed (no balance sheet/ageing/ECL in Q1) | **UNKNOWN — cannot clear** |
| 3 | RBI order dated go-live + revenue recognition | dated go-live | cancelled/slipped | not disclosed anywhere in filing | **UNKNOWN — cannot clear** |
| 4 | Order book / book-to-bill | >1.3x trailing | — | not disclosed; revenue −4.6% YoY (CON) | **UNKNOWN — cannot clear (revenue-decline caution)** |
| 5 | Annuity mix / leverage D/E | <0.3x | >0.4x, leases outgrowing annuity | D/E not computable (no balance sheet); finance +45.8%, dep ×5.48 | **UNKNOWN — directional caution, leverage rising** |
| 6 | Cybercons classification | stable | restatement or RPT balances re-accelerating | consolidated as "Subsidiary Company," no restatement/reclassification/EoM; RPT balances not disclosed | **GREEN on classification; RPT balances UNKNOWN** |

Named monitorables this limited-review filing **cannot clear**: 2 (receivables/ECL/debtor days), 3 (RBI go-live), 4 (order book/book-to-bill), and the leverage half of 5 — all because there is no balance sheet, no receivables ageing, no order-book disclosure, and no RBI-order note in a Q1 Reg-33 filing. The receivables leg is critical: it is one of the two legs of the pre-committed buy trigger (see Step 8).

### 6C. Thesis-broken trigger check (all 4)

| # | Thesis-broken condition | Threshold | Current reading | FIRED? |
|---|---|---|---|---|
| 1 | EBITDA margin near 9% (<11%) two consecutive quarters | green ≥11% / red <9% | Q1FY27 CON 12.81% (GREEN); Q4FY26 9.02% was a single sub-11% quarter, above the 9% red line, and now reversed | **NOT FIRED** — current quarter green; no two-consecutive sub-9% sequence |
| 2 | Debtor days >160 with 1-2yr overdue bucket widening on frozen Rs0.14cr ECL | green ≤154 | no balance sheet / ageing / ECL in filing | **CANNOT EVIDENCE / UNKNOWN** — not cleared, not fired |
| 3 | RBI Rs750.82cr order cancelled / materially slipped | — | no order disclosure, no cancellation language anywhere | **NOT FIRED** (no adverse evidence); go-live date UNKNOWN |
| 4 | HARD OVERRIDE: any Cybercons consolidated restatement → AVOID | — | Cybercons consolidated as "Subsidiary Company" (line 175, 543); no restatement, no reclassification, no EoM touching it | **NOT FIRED** |

**No pre-committed thesis-broken trigger has formally fired on this filing.** Decision Status is NOT re-rated. Two triggers (2 and, on go-live, 3) cannot be evidenced from a Q1 filing and remain open pending H1/Q2 data.

### 6D. Growth trigger status

| Trigger | Original confidence | Confirming evidence (this filing) | Killing evidence | Updated status |
|---|---|---|---|---|
| Margin recovery to ≥11% | thesis binary gate | CON 12.81%, STD 12.83% — cleared green | none | **FIRED (margin leg only)** |
| Order book conversion / revenue growth | GOOD | none in filing | revenue −4.6% YoY (CON), −5.3% (STD) | **DELAYED / not evidenced** |
| RBI Rs750.82cr private-cloud go-live | pending | none | none | **DELAYED — no dated go-live disclosed** |
| TWAS as a growth focus segment | new (Note 5) | flagged a "focus business segment" | TWAS revenue −20.7% YoY (307.77 vs 387.93 restated) | **WEAKENED — narrative vs number divergence** |
| ROCE recovery (as-a-service assets earning) | RECOVERING | margin up | dep ×5.48, finance +45.8%, revenue down → absorption deficit | **WEAKENED — absorption deficit until volume returns** |

---

## STEP 7 — FOUR-PILLAR DESTINATION PE RE-VALIDATION

The destination PE was set under Section 1B v3.3. This Q1 limited-review filing does not disclose the balance-sheet inputs (ROCE denominator, net worth, net debt) needed to re-run most pillars. Re-validation is therefore **directional only**; no pillar is re-set from this filing, and no destination-PE recompute is warranted on Q1 data alone.

| Pillar / Input | Original assumption | Current reading (this filing) | Action |
|---|---|---|---|
| ROCE Base (0.5×ROCE + 7.5, floor 9x, cap 24x) | FTTCP ROCE RECOVERING | ROCE not computable (no balance sheet); dep ×5.48 + finance +45.8% + revenue −4.6% = absorption deficit, directionally negative for ROCE near-term | **HOLD** — FTTCP verdict is sole Pillar-1 authority; no ad hoc revision on Q1; re-test at H1 |
| Cash Multiplier | 1.00x (FLAG-CASH, no growth offset) | CFO/PAT not testable (no cash flow statement); INDETERMINATE | **HOLD** — cannot revise up; FLAG-CASH stands |
| Growth Visibility Premium | per EM 22.7/80 MODEST | order book not disclosed; revenue −4.6% | **HOLD** — no evidence to lift |
| Strategic Premium | per moat MODEST; single-credit rule | margin up but via mix, not durable moat evidence | **HOLD** — do not credit margin gain as moat |
| UA Multiplier | excluded from conservative entry zone | unchanged | **HOLD** — N/A to conservative zone |
| Sector Cap | 30x (data centres & cloud) | no reclassification | **HOLD** |
| Hurdle Ratio recheck | HR ≥ 1.953 | EPS CAGR and ROCE inputs not refreshable on Q1; CMP ~16% above entry-zone top | **DEFER** to H1 refresh |

No pillar changes on this filing. Fair values and entry zone (Rs851-1,064) stand unchanged; no recompute triggered.

---

## STEP 8 — POSITION DECISION (Branch 8A-W — non-held / WATCHLIST name)

Decision Status verified at Step 0A = **WATCHLIST / BUY ON DIPS**. This is not a held position, so the 8A-W branch governs (no trim/exit mechanics).

Branch logic:
- Any thesis-broken condition FIRED? **No** (Step 6C: none fired; two cannot be evidenced). → not reclassified to AVOID.
- Actual below Bear on 2+ metrics? Bear projections not passed; not establishable this run. → no forced down-revision this run.
- The pre-committed BUY gate: **this Q1 FY27 print is the thesis's binary buy trigger, defined as Q1 FY27 EBITDA margin + receivables print.** Assessment of the two legs:
  - **Margin leg: GREEN.** CON op EBITDA margin 12.81% (STD 12.83%), above the ≥11% green threshold and well above the <9% red line.
  - **Receivables leg: UNKNOWN — CANNOT CLEAR.** A Q1 limited-review filing carries no balance sheet, no receivables ageing, no ECL. Debtor days and the 1-2yr overdue bucket cannot be read.

**Conclusion:** the pre-committed buy gate is **half-satisfied and therefore NOT met.** One of its two required legs (margin) reads green; the other (receivables/debtor days ≤154, overdue flat/shrinking, ECL topped up) cannot be evidenced from this document. A binary gate with one leg unverifiable does not fire. The buy gate is **pushed to the H1/Q2 FY27 filing**, when the balance sheet and receivables ageing publish. Additionally, CMP Rs1,231.6 sits ~16% above the entry-zone top (Rs1,064), so the name is not buyable at CMP even on the margin leg alone.

**Position read (flag, do not decide):** Decision Status stays **WATCHLIST / BUY ON DIPS**, unchanged. No trigger fired; no re-rate. The margin condition cleared green, which is thesis-supportive, but the buy action remains gated on (a) the receivables print at H1 and (b) price entering the Rs851-1,064 zone. New gate stated explicitly: **re-assess the buy trigger at the H1/Q2 FY27 results, requiring debtor days ≤154 with the overdue bucket flat/shrinking and ECL topped up, AND price at or below Rs1,064.**

### 8B. Add-back / trim trigger refinement
Not a held name — no trim ladder. Add/entry trigger unchanged: entry zone Rs851-1,064, MoS Rs851, plus the receivables leg of the buy gate now explicitly carried to H1. New caution to fold into the next refresh: revenue declined 4.6% YoY (CON) and the margin gain is mix-and-absorption-driven, not volume-driven — tighten the entry logic to require a revenue-run-rate recovery alongside the margin, so a low-revenue/high-margin quarter is not mistaken for the thesis firing.

### 8C. Single cleanest metric for next quarter
**Debtor days (with the 1-2yr overdue bucket and ECL top-up), read against the ≤154 green line, at the H1/Q2 FY27 filing.** It is the one number that resolves the buy gate's open leg and the FLAG-CASH structural-WC question in a single read. Bull threshold: debtor days ≤154, overdue bucket flat or shrinking, ECL topped up above Rs0.14cr. Bear threshold: debtor days >160 with the 1-2yr overdue bucket widening on a still-frozen Rs0.14cr ECL. Secondary clean metric: consolidated revenue recovery toward the 350-400 cr band, to confirm the absorption deficit is closing rather than widening.

---

## STEP 8.5 — QUESTIONS FOR MANAGEMENT (channel: IR email / next concall — no concall scheduled with this filing)

Contract: EVERY A3 finding tagged FORWARD-SIGNAL or AMBIGUOUS produces at least one row. Findings covered: F3-01 (FS), F6-01 (FS), F12-01 (FS/AMB), F1-01 (AMB), F2-01 (AMB), F10-01 (AMB), F14-01 (AMB). Two disclosure-gap questions added (receivables, order book/RBI) that the filing is silent on.

| # | Question | From finding | Why it matters | Bull answer | Bear answer |
|---|---|---|---|---|---|
| 1 | Depreciation rose ×5.48 (Rs1.48cr → Rs8.09cr) and finance costs +45.8% YoY while consolidated revenue fell 4.6%. What asset base (owned PPE vs Ind AS 116 lease-capex) commissioned between Q1FY26 and Q1FY27, what Rs-cr amount was capitalised, and what revenue is that base expected to earn, by when? | F3-01 | Tests whether the absorption deficit closes; ROCE compresses until these assets earn | A dated, quantified as-a-service/DaaS asset with a signed revenue schedule | Vague "growth capex," no dated revenue, deficit persists |
| 2 | Debtor days, the trade-receivables balance, the receivables ageing (esp. the 1-2yr overdue bucket) and the ECL provision were not in this Q1 filing. Can you provide the 30-Jun-2026 figures, and confirm whether the ECL was topped up above Rs0.14cr? | receivables gap (monitorable 2 / buy-gate leg) | This is the unverifiable leg of the pre-committed buy trigger and the FLAG-CASH structural-WC question | Debtor days ≤154, overdue flat/shrinking, ECL raised | Debtor days >160, overdue widening, ECL still frozen at Rs0.14cr |
| 3 | The Rs750.82cr RBI private-cloud order (7-year) and the Rs2,964cr order book were not referenced in this filing. What is the dated go-live for the RBI order, and how much of it (and the book) is recognised in Q1FY27 revenue? | order-book/RBI gap (monitorables 3,4) + F6-01 | Revenue fell 4.6% YoY; the order book is the thesis's growth engine and needs a conversion timeline | Dated go-live, quantified Q1 recognition, book-to-bill >1.3x confirmed | No date, no recognition, order slipping |
| 4 | Note 5 introduces "Technology Workforce Augmentation Services" as a focus growth segment, yet its segment revenue fell 20.7% YoY (Rs3.08cr vs Rs3.88cr restated). Can you reconcile the "focus growth" label with the decline, and give the quantified restatement bridge (how much revenue moved out of System Integration into TWAS)? | F12-01, F6-01 | The growth narrative and the number diverge; restated comparatives are un-bridged | A clear carve-out bridge plus a credible ramp plan for TWAS | Circular answer, no bridge, "focus" is aspirational only |
| 5 | The subsidiary net contribution swung from a Rs0.14cr drag in Q4FY26 to a Rs0.23cr add in Q1FY27, about 7x the Q1FY26 level, tying to the Rs0.2322cr subsidiary PAT in the Other Matter. Which subsidiary (Cybercons Infosec or Dynacons PTE) drove the swing, and is Cybercons' contribution recurring? | F2-01 | Lumpy earnings around the Cybercons name; classification is a hard-override monitorable | Cybercons contribution is small, recurring, arm's-length | Related-party-driven or one-off lump, opaque |
| 6 | Paid-up equity capital rose Rs1.18 lakh (~11,800 shares) between Q1FY26 and Q4FY26 with no explanatory note. What corporate action (ESOP exercise, warrant conversion, other) caused it, and is any further dilution pending? | F10-01 | Unexplained share-count change; basic-vs-diluted spread now nil | A closed, disclosed ESOP tranche, no pending dilution | Undisclosed instrument or an open warrant/ESOP overhang |
| 7 | The restated CON Q1FY26 "TCI attributable to Shareholders" is filed at Rs1,966.53 lakh but does not tie to its own components by exactly Rs9.58 lakh (PAT-Shareholders Rs1,961.74 + OCI-Shareholders −Rs4.79 = Rs1,956.95). Is Rs1,966.53 a filing typo, and will it be corrected in the H1 statement? | F14-01 | Casting error on a restated comparative; accounting-quality question (quality scored 4/10) | Acknowledged typo, corrected at H1 | Defended as correct, no reconciliation — governance flag |
| 8 | A Singapore subsidiary (Dynacons PTE) is consolidated, yet the reclassifiable-OCI / foreign-exchange-translation line is nil across all four periods on both books. Where is the foreign-currency-translation reserve on the PTE subsidiary carried, and is FX translation genuinely immaterial? | F1-01 | FCTR should appear where a foreign sub is consolidated; nil is unexplained | FX genuinely immaterial (tiny sub), reconciled | Translation netted or not surfaced, opacity |

**Top 3 by likelihood of thesis-changing information:**
1. Q2 — receivables/ECL disclosure. It resolves the open leg of the buy gate and the FLAG-CASH structural-WC question in one read; a clean answer moves the bull case, a widening overdue bucket confirms the bear.
2. Q1 — the depreciation/finance step-up and dated revenue on the new asset base. Confirms or kills the ROCE-recovery / absorption-deficit thesis.
3. Q7 — the Rs9.58 lakh casting error. A defensive or evasive answer is itself a governance signal for the accounting-quality flag.

**Channel:** No concall was scheduled with this Board Outcome. Recommend an IR email carrying all 8 questions verbatim, prioritising 1-3; if a concall is later scheduled for Q1FY27, submit 1-3 for live Q&A and the rest in writing.

---

## MONITORABLES / CATALYST LIST (into Q2 / H1 FY27)

Seeded from the A3 commitment register (F6) and the disclosure absences.

| Item | Implied date | Source ref | Watch for |
|---|---|---|---|
| Interim dividend Rs0.50/share paid (cash outgo Rs0.6369cr) | record 19-Aug-2026; pay 27-Aug-2026 | Board letter ln43-46; Note 3 ln320 | routine execution; confirms capital-return discipline |
| H1/Q2 FY27 results — balance sheet + cash flow (Reg 33 half-yearly) | ~Nov 2026 | protocol Step 5 data rule | receivables ageing, ECL, debtor days, CFO/PAT, net debt, PPE/CWIP — clears monitorables 2 and 5 and the buy-gate receivables leg |
| Debtor days vs ≤154 green line, 1-2yr overdue bucket, ECL top-up | H1/Q2 FY27 | monitorable 2; buy-gate leg | the single cleanest metric (Step 8C) |
| RBI Rs750.82cr private-cloud order — dated go-live + revenue recognition | date UNKNOWN | monitorable 3 (not in filing) | first dated go-live; any slippage/cancellation is trigger 3 |
| Order book / book-to-bill (Rs2,964cr + NPCI Rs267.58cr pro-forma ~Rs3,232cr per prior work) | H1/Q2 FY27 or concall | monitorable 4 (not in filing) | conversion vs the −4.6% YoY revenue print; >1.3x trailing is green |
| TWAS focus-segment ramp | Q2FY27 onward | Note 5 ln322-331; F6-01/F12-01 | does TWAS revenue reverse the −20.7% YoY; restatement bridge |
| Consolidated revenue run-rate recovery toward 350-400 cr | Q2FY27 | Step 3 | confirms absorption deficit closing, not widening |
| Cybercons Infosec classification + related-party balances | H1/Q2 FY27 balance sheet | monitorable 6; F2-01; hard-override trigger 4 | any restatement/reclassification = AVOID; RPT balances re-accelerating = red |
| Depreciation/finance-cost steady-state | Q2-Q3 FY27 | Step 4; F3-01 | when D&A and finance plateau, marking end of the capex ramp |

---

## PROTOCOL VERDICT

**PROCEED WITH CAVEATS.** The print is clean (unmodified auditor opinion on both books), the margin leg reads green (CON op EBITDA margin 12.81%), and no pre-committed thesis-broken trigger fired. The verdict is held at CAVEATS, not PROCEED, because **cash conversion is INDETERMINATE** — a Q1 limited-review filing carries no cash flow statement, no balance sheet, no receivables ageing and no ECL, so CFO/PAT cannot be tested and the FLAG-CASH structural-WC question cannot be cleared. Named missing evidence: CFO, receivables ageing / debtor days, ECL provision, net debt, PPE/CWIP. Carried flags propagate unchanged: FLAG-CASH (structural WC, cash multiplier 1.00x), promoter CAUTION (2019 SEBI settlement, Cybercons classification history, pledge NOT FOUND), accounting quality 4/10 — now with a new data point, the Rs9.58 lakh casting error on a restated comparative (F14-01). Two thesis-broken triggers (receivables; RBI go-live) cannot be evidenced and stay open to H1.

---

# PLAIN-LANGUAGE BRIEF (standing deliverable)

## Summary narrative

Dynacons reported its June 2026 quarter on 13 August 2026. Consolidated revenue was Rs313.7 crore, down 4.6 percent from Rs328.9 crore a year earlier. Standalone revenue fell 5.3 percent. Profit after tax was Rs19.8 crore on the consolidated book, up a thin 0.8 percent, and Rs19.6 crore standalone, actually down 0.3 percent. So the headline is a flat print on falling sales.

The one bright number is margin. Operating profit margin rose to 12.81 percent from 9.66 percent a year earlier, a gain of about 3.15 percentage points. That clears the green line the thesis set at 11 percent and sits well above the 9 percent red line. On the margin test alone, this quarter passed.

The catch is what happened below the margin line. Depreciation jumped more than five times, from Rs1.5 crore to Rs8.1 crore. Finance costs rose 46 percent. Those two together ate almost the entire margin gain, so profit before tax barely moved. The margin came from cheaper input costs and a bigger fixed-asset base, not from selling more. A company that builds assets faster than its sales grow runs what the protocol calls an absorption deficit. Returns fall until the sales catch up.

This June print was the pre-committed buy trigger for the stock. The trigger has two legs: the margin, and the trade receivables. The margin leg is green. The receivables leg cannot be read, because a first-quarter filing in India does not include a balance sheet. So the buy gate is half open, not fired. The next real test is the September-half results, likely around November 2026, when the balance sheet, the debtor days and the bad-debt provision finally publish.

No thesis-broken trigger fired. The Cybercons subsidiary is still consolidated as a normal subsidiary with no restatement, so the hard-override that would force an AVOID did not trigger. The stock stays WATCHLIST / BUY ON DIPS, unchanged. It is also not buyable at today's price of about Rs1,232, which sits roughly 16 percent above the top of the Rs851 to Rs1,064 entry zone.

Provenance: the revenue, margin, profit, depreciation and finance-cost figures are all from this quarter's filing. The order book, the RBI order, the entry zone, the flags and the buy-gate definition are from prior Notion work and were not disclosed in this filing.

## Sector intelligence

Dynacons sells IT systems integration and services, and its sector cap is set at 30 times for data centres and cloud (Notion/prior work). The demand story rests on India's public and private cloud build-out and on large multi-year contracts: an RBI private-cloud order of Rs750.82 crore over seven years, an NPCI order of Rs267.58 crore, and an order book of Rs2,964 crore, about 2.08 times sales (all Notion/prior work). None of these appeared in this quarter's filing, so their conversion into revenue cannot be checked from the document. What the filing does show is that consolidated revenue fell 4.6 percent year on year (this quarter's filing), which sits awkwardly against a 2x-plus order book. Either the book is back-ended, or conversion is slow. That gap is the sector question to resolve at the next filing.

## Business-model intelligence

The company makes money two ways: selling and integrating hardware and software systems, and providing services, increasingly on an as-a-service or device-as-a-service basis where it owns or leases the kit and bills over time (business model per Notion/prior work). This quarter's numbers show the model drifting toward that asset-heavy footing. Depreciation rose more than five times and finance costs rose 46 percent, and both are identical on the standalone and consolidated books, which means the whole asset build sits in the parent, not the subsidiaries (this quarter's filing, via A3 F3-01). Input costs fell as a share of sales, from about 85.9 percent to 80.6 percent, which lifted margin, but the asset cost absorbed the gain. A new reporting segment, Technology Workforce Augmentation Services, was introduced as a focus growth area, yet its own revenue fell 20.7 percent year on year (this quarter's filing). The model is shifting to annuity-style assets faster than those assets are earning. The cash-conversion evidence that would confirm or deny the strain, the cash flow statement and the receivables, was not in this filing.

## Competition intelligence

Dynacons competes in Indian IT systems integration against far larger integrators and against the services arms of hardware makers, so scale and balance-sheet depth are where it is structurally weaker (peer context per Notion/prior work; no peer figures were disclosed in this filing). Where it wins is niche, contract-led work: the RBI and NPCI mandates show it can land large regulated-sector deals (Notion/prior work). The competitive risk to watch is the same as the model risk. If Dynacons funds an as-a-service asset build with lease and debt while revenue is flat, a larger competitor with cheaper capital can underprice the same annuity contracts. The margin gain this quarter is real but it came from mix and cost, not from pricing power or share gains, and this filing gave no evidence of a widening moat. The Emerging Moat score of 22.7 out of 80 is MODEST (Notion/prior work), and nothing this quarter moved it.

```yaml
stage: A4-analyst
company: "DSSL"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
docs_merged: [results]
ledger_reconciliation:
  notes: 5
  turns: 0
  slides: 0
  all_reviewed: true
  a3_findings_incorporated: ["F1-01","F2-01","F3-01","F6-01","F6-02","F10-01","F12-01","F12-02","F14-01"]
protocol_verdict: "PROCEED WITH CAVEATS"
cash_conversion: "INDETERMINATE"
decision_status_verified: "WATCHLIST / BUY ON DIPS"
position_branch: "8A-W"
sc_gap_pat_pct: ["Q1FY27 +1.19%","Q4FY26 -0.73%","Q1FY26 +0.17%","FY26 +0.04%"]
questions_for_management:
  - {q: "What asset base commissioned Q1FY26->Q1FY27 (owned vs Ind AS 116 lease), Rs-cr capitalised, and expected revenue/date, given dep x5.48 and finance +45.8% vs revenue -4.6%?", from_finding_id: "F3-01"}
  - {q: "Provide 30-Jun-2026 debtor days, receivables balance, ageing (1-2yr overdue bucket) and ECL; was ECL topped up above Rs0.14cr?", from_finding_id: "receivables-gap/monitorable-2"}
  - {q: "Dated go-live for the RBI Rs750.82cr order and Q1FY27 revenue recognised from it and the Rs2,964cr book?", from_finding_id: "F6-01/order-book-gap"}
  - {q: "Reconcile TWAS as a focus growth segment with its -20.7% YoY revenue; give the quantified restatement bridge from System Integration.", from_finding_id: "F12-01"}
  - {q: "Which subsidiary drove the -0.14cr to +0.23cr Q4->Q1 PAT swing (7x Q1FY26), and is Cybercons' contribution recurring?", from_finding_id: "F2-01"}
  - {q: "What corporate action raised paid-up capital Rs1.18 lakh (~11,800 shares) with no note, and is further dilution pending?", from_finding_id: "F10-01"}
  - {q: "Is CON Q1FY26 TCI-to-Shareholders Rs1,966.53 lakh a filing typo (fails tie by Rs9.58 lakh), and will it be corrected at H1?", from_finding_id: "F14-01"}
  - {q: "Where is the foreign-currency-translation reserve on the Singapore subsidiary carried, given the reclassifiable-OCI/FX line is nil all periods both books?", from_finding_id: "F1-01"}
monitorables:
  - {item: "Interim dividend Rs0.50/share paid (cash outgo Rs0.6369cr)", implied_date: "2026-08-27 (record 2026-08-19)", source_ref: "Board letter ln43-46; Note 3 ln320"}
  - {item: "H1/Q2 FY27 balance sheet + cash flow (receivables/ECL/debtor days, CFO/PAT, net debt, PPE/CWIP)", implied_date: "~Nov 2026", source_ref: "protocol Step 5 data rule"}
  - {item: "Debtor days vs <=154 green line + 1-2yr overdue bucket + ECL top-up (cleanest metric)", implied_date: "H1/Q2 FY27", source_ref: "monitorable 2 / buy-gate leg"}
  - {item: "RBI Rs750.82cr order dated go-live + revenue recognition", implied_date: "UNKNOWN", source_ref: "monitorable 3 (not in filing)"}
  - {item: "Order book / book-to-bill (>1.3x trailing green) vs -4.6% YoY revenue", implied_date: "H1/Q2 FY27", source_ref: "monitorable 4 (not in filing)"}
  - {item: "TWAS focus-segment ramp + restatement bridge", implied_date: "Q2FY27 onward", source_ref: "Note 5 ln322-331; F6-01/F12-01"}
  - {item: "Consolidated revenue run-rate recovery toward 350-400 cr", implied_date: "Q2FY27", source_ref: "Step 3"}
  - {item: "Cybercons classification + related-party balances (hard-override trigger 4)", implied_date: "H1/Q2 FY27", source_ref: "monitorable 6; F2-01"}
  - {item: "Depreciation/finance-cost steady-state (end of capex ramp)", implied_date: "Q2-Q3 FY27", source_ref: "Step 4; F3-01"}
flags: ["FLAG-CASH structural WC / cash multiplier 1.00x (INDETERMINATE this quarter)","promoter CAUTION (2019 SEBI settlement; Cybercons classification history; pledge NOT FOUND)","accounting quality 4/10 (F14-01 Rs9.58 lakh casting error on restated comparative)","revenue -4.6% YoY CON despite 2x order book (unclearable from filing)","capex absorption deficit (dep x5.48, finance +45.8% vs revenue -4.6%)"]
plain_language_brief_included: true
review_path: "/home/user/inflection-pipeline/runs/dssl-q1fy27/work/review_dssl_q1fy27.md"
```
