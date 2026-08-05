# Q1 FY27 MERGED QUARTERLY REVIEW — Vaibhav Global Limited (VAIBHAVGBL)

Agent A4 (Analyst) | Role 4 (Results Review Protocol v1.2) in full; Role 5 (Concall) = N.A. (no transcript this run)
Sources: A1 extracts + A2 ledgers + A3 forensics for results / press release / investor presentation.
Anchoring convention: `R:Lxx` = results extract line; `PR:Lxx` = press-release extract line; `PP:Lxx` = presentation extract line; `s##` = slide.
Unit convention: results filing is in **₹ Lakhs** (R:L7, factor ×0.01 → ₹ Cr); press release and presentation are natively in **₹ Cr** (PR:L8, PP:L8). All analysis below is in **₹ Cr**. Every cell is a line-anchored number or the literal `ND`. No estimation.

---

## LEDGER-RECONCILIATION PREAMBLE (contractual, before Step 1)

- **Results ledger** (`ledger_results`): contains **15 notes** (9 consolidated R:L157-231 + 6 standalone R:L291-313), 81 line items, 14 entities, 13 auditor paragraphs, 4 board-agenda items, 7 signature blocks, 11 annexure rows. Gate A2 = pass. **All 15 notes reviewed.**
- **Press-release ledger** (`ledger_pressrelease`): NSE/BSE cover letter + management press release, 5 pages, **71 disclosure units** across 18 sections (no numbered notes / no slides — `DOCTYPE_LABEL_MISMATCH` recorded by A2). Gate A2 = pass. **All 71 units reviewed.**
- **Presentation ledger** (`ledger_presentation`): investor deck, **39 slides**, 432 disclosure units (39 slides + 9 chart blocks + 304 numeric lines + 15 footnotes + 39 entities + 11 guidance items + 10 leadership profiles + 6 OCR flags). Gate A2 = pass. **All 39 slides reviewed.**

**All ledger rows reviewed: YES.** No unreviewed row remains; the protocol proceeds.

**A3 findings incorporated (all 24):**
- Results: `A3-01, A3-02, A3-03, A3-04, A3-05, A3-06, A3-07, A3-08, A3-09`
- Press release: `F7-01, F8-01, F16-01, F6-01, F14-01`
- Presentation: `FND-01, FND-02, FND-03, FND-04, FND-05, FND-06, FND-07, FND-08, FND-09, FND-10`

Every FORWARD-SIGNAL and AMBIGUOUS finding (19 of the 24) generates at least one Questions-for-Management row in Step 8.5; the 5 NEUTRAL-FACT findings (A3-09, F14-01, FND-01, FND-05, FND-07) are logged in Monitorables. Cross-map is shown at the head of Step 8.5.

---

## STEP 0 — PRE-FLIGHT

### 0A. Notion / Decision Status
**Decision Status = NOT YET COVERED / NO POSITION.** Live Notion search returned no VGL page; no `companies/VAIBHAVGBL.md` memory exists. This is **FIRST-TIME coverage**. There is no prior thesis, no entry zone, no active tripwire, no prior monitoring checklist, no Devil's-Advocate probability split, and no prior Questions-for-Management to age. Consequently: Step 6 is framed as an **initiation reconciliation** (not a HOLD/ADD/TRIM/EXIT on a held book), Step 8 uses the **8A-W (non-held) branch**, and every figure in the Plain-Language Brief is provenance-labelled to **this quarter's filing** (no prior Notion/peer artifact exists to cite).

### 0B. Units
Results filing: ₹ Lakhs (R:L7), converted ×0.01 → ₹ Cr. Press release & deck: ₹ Cr native (PR:L8; PP:L8). No unit ambiguity.

### 0C. Share-count changes
Paid-up equity capital moved 3,340.48 → 3,346.01 (₹ Lakhs, FV ₹2) across FY26-end → Q1FY27 (R:L117), a rise of ₹5.53 L = **276,874 equity shares** allotted under ESOP/RSU/MSOP trusts (Note 4, R:L182-184). **No split, bonus, rights, QIP, FPO or buyback** in the period. Reported EPS is therefore directly comparable across periods; **share-adjusted EPS = reported EPS** (no adjustment factor required). Fresh grants approved this quarter — 93,170 MSOP + 11,858 RSU + 14,970 ESOP at ₹2 exercise (R:L556-560) — keep dilution live but immaterial in magnitude (≈0.07% of ~16.73 Cr shares).

### 0D. Notes extraction (all 15) — one-off / comparability screen

| Note # | Source | Subject | ₹ Cr impact | Period | Comparability impact |
|---|---|---|---|---|---|
| C1 | R:L157-159 | Board/Audit-Committee approval; statutory-auditor limited review | — | Q1FY27 | None |
| C2 | R:L161-163 | Ind AS / Reg 33 basis | — | — | None |
| C3 | R:L165-180 | 14-entity consolidation list (all wholly-owned + 1 controlled trust) | — | — | Baseline (no prior ledger to diff) |
| C4 | R:L182-184 | 276,874 ESOP shares allotted (exercise ₹2.00–188.95) | +0.06 (capital) | Q1FY27 | Trivial dilution; see 0C |
| C5 | R:L186-190 | Content & broadcasting expense (>10% of total expenditure): 196.55 (Q1FY27) vs 165.03 (Q1FY26) | 196.55 | all | Largest single opex; +19.1% YoY, scaling faster than revenue (+12.7%) |
| C6 | R:L194-196 | Interim dividend ₹1.50/sh, record date 12 Aug 2026 | ~25.1 outflow (≈16.73 Cr sh × ₹1.50) | Q2FY27 | Capital-return signal; cash out next quarter |
| C7 | R:L198-200 | Q4FY26 figures are BALANCING figures (not separately audited) | — | Q4FY26 | **QoQ base is derived, not independently reported — treat Q4FY26 QoQ reads with caution** |
| **C8** | R:L202-229 | **IEEPA / Section 122 US tariff saga** | **see below** | Q1FY27 + fwd | **MATERIAL — one-off revenue + unbooked contingency; drives Step 4** |
| C9 | R:L231 | Segment info per Ind AS 108 in Annexure I | — | — | None |
| S1 | R:L291-294 | Standalone approval / limited review | — | — | None |
| S2 | R:L296-298 | Ind AS / Reg 33 basis (standalone) | — | — | None |
| S3 | R:L300-302 | Same 276,874 ESOP allotment (standalone) | — | Q1FY27 | Ties to C4 |
| S4 | R:L304-306 | Interim dividend (standalone restatement of C6) | — | Q2FY27 | Ties to C6 |
| S5 | R:L308-310 | Q4FY26 balancing-figure caveat (standalone) | — | Q4FY26 | Ties to C7 |
| S6 | R:L312-313 | Standalone segment data intentionally absent (cross-refers to consol) | — | — | None |

**Note C8 decomposed (R:L202-229) — the quarter's defining one-off:**
- IEEPA tariffs of USD 4.59M (₹4,338.55 L) paid in FY26 had been carried as a *contingent asset* (R:L202-209).
- **This quarter** a refund of **₹3,839.90 L (USD 4.04M) + ₹148.04 L interest** was received (R:L211-217). Of it: **₹2,559.15 L (≈₹25.59 Cr) booked as OTHER OPERATING REVENUE** (inside Revenue from operations), **₹1,280.75 L (≈₹12.81 Cr) netted off the carrying value of inventory still in stock** (future-COGS benefit, not this quarter's P&L), and **₹148.04 L (≈₹1.48 Cr) interest booked in Other Income**.
- Separately, **₹1,425.73 L (≈₹14.26 Cr) of Section 122 tariffs paid** (24 Feb–24 Jul 2026) is **NOT recognised as a receivable** — CIT ruled it unlawful, Federal Circuit stayed the injunction, outcome "not considered probable at this stage… will be accounted for in future periods" (R:L219-229). **Unbooked binary catalyst** (A3-03, A3-04).

**Analytical consequence (my Step-2/Step-4 anchor):** ≈**₹25.59 Cr of the ₹917.07 Cr reported revenue is a non-recurring tariff refund** sitting inside "Revenue from operations." It is pure pre-tax profit. It must be stripped before judging operating trajectory. This is not separately flagged in A3 as a revenue distortion (A3 logged it in the commitment register as "completed"); I raise it here under the protocol's "every one-off must be named and quantified" rule.

### 0D (cont). Auditor opinion
**UNMODIFIED / clean** limited review on BOTH consolidated (R:L380-386, BSR & Co. LLP, "conclusion not modified" R:L419) and standalone (R:L508-514, "not modified" R:L532). No Going Concern, no qualification. Two "Other Matters / attention is drawn" paragraphs are the standard Q4-balancing-figure caveat (R:L374-378; R:L502-506), not an Emphasis-of-Matter on solvency. Statutory auditor **unchanged** (BSR & Co. LLP). Distinct UDIN per report (correct practice). **AMBER governance note (not an audit modification):** the Board this quarter appointed **Ernst & Young LLP as INTERNAL auditor for FY27-FY28** (R:L42-43, R:L607-619), and EY is simultaneously the company's **Investor-Relations advisor** (PR:L205-208; PP:L1159). Same firm on internal audit and IR advisory — an independence-optics data point (see A3-08 / Step 8.5 Q9).

### 0E. Business type
**Standard operating business** — vertically-integrated omnichannel e-tailer of fashion jewellery / lifestyle products via TV home-shopping + digital (PR:L64-66; PP:s6). NOT a lender. Steps 1 and 5 (standard) apply; Steps 1L/5L do not.

🛑 Pre-flight complete: Notion status = NOT YET COVERED (verified), units identified, share-count traced, all 15 notes extracted, auditor opinion clean, business type = standard. Proceeding.

---

## STEP 1 — DATA EXTRACTION (₹ Cr)

### 1A. CONSOLIDATED P&L (from R:L79-121)

| Line Item | Q1 FY26 (Jun-25) | Q4 FY26 (Mar-26)ᴮ | Q1 FY27 (Jun-26) | FY26 (audited) |
|---|---|---|---|---|
| Revenue from operations | 813.74 (R:L79) | 934.71 (R:L79) | 917.07 (R:L79) | 3,691.79 (R:L79) |
| Other income | 13.07 (R:L80) | 12.54 (R:L80) | 5.31 (R:L80) | 41.27 (R:L80) |
| Total income | 826.81 (R:L81) | 947.25 (R:L81) | 922.39 (R:L81) | 3,733.06 (R:L81) |
| Cost of materials consumed | 80.44 (R:L83) | 158.57 (R:L83) | 98.64 (R:L83) | 399.06 (R:L83) |
| Purchases of stock-in-trade | 218.65 (R:L84) | 141.38 (R:L84) | 216.93 (R:L84) | 879.21 (R:L84) |
| Change in inventories | (22.08) (R:L85) | 19.93 (R:L85) | (41.28) (R:L85) | (3.75) (R:L85) |
| Employee benefits | 149.01 (R:L86) | 155.12 (R:L86) | 152.88 (R:L86) | 616.82 (R:L86) |
| Finance costs | 3.50 (R:L87) | 4.31 (R:L87) | 4.54 (R:L87) | 14.94 (R:L87) |
| Depreciation & amortisation | 25.29 (R:L88) | 27.92 (R:L88) | 26.63 (R:L88) | 102.89 (R:L88) |
| Other expenses | 326.18 (R:L89) | 376.29 (R:L89) | 393.18 (R:L89) | 1,442.21 (R:L89) |
| Total expenses | 780.99 (R:L90) | 883.52 (R:L90) | 851.51 (R:L90) | 3,451.38 (R:L90) |
| PBT before exceptional | 45.82 (R:L91) | 63.74 (R:L91) | 70.87 (R:L91) | 281.68 (R:L91) |
| Exceptional items | ND (nil) (R:L92) | 0.18 (R:L92) | ND (nil) (R:L92) | 0.18 (R:L92) |
| PBT after exceptional | 45.82 (R:L93) | 63.91 (R:L93) | 70.87 (R:L93) | 281.85 (R:L93) |
| Current tax | 17.37 (R:L95) | 17.53 (R:L95) | 22.97 (R:L95) | 80.88 (R:L95) |
| Deferred tax credit | (9.19) (R:L96) | (44.76) (R:L96) | (8.48) (R:L96) | (65.16) (R:L96) |
| Total tax expense/(credit) | 8.19 (R:L97) | (27.23) (R:L97) | 14.49 (R:L97) | 15.72 (R:L97) |
| **PAT** | **37.63** (R:L98) | **91.14** (R:L98) | **56.38** (R:L98) | **266.13** (R:L98) |
| EPS basic (₹) | 2.26 (R:L120) | 5.47 (R:L120) | 3.37 (R:L120) | 15.97 (R:L120) |
| EPS diluted (₹) | 2.24 (R:L121) | 5.40 (R:L121) | 3.33 (R:L121) | 15.75 (R:L121) |
| EPS share-adjusted (₹) | 2.26 (= reported; no split/bonus, 0C) | 5.47 | 3.37 | 15.97 |

ᴮ Q4FY26 column is a BALANCING figure, not independently audited (Note C7, R:L198-200).

### 1B. CONSOLIDATED derived metrics

| Derived metric | Formula | Q1 FY26 | Q4 FY26 | Q1 FY27 | FY26 |
|---|---|---|---|---|---|
| Operating EBITDA | PBT + D + Fin − OI | 61.54 | 83.60 | 96.73 | 358.41 |
| Operating EBITDA margin | ÷ Rev | 7.6% | 8.9% | 10.5% | 9.7% |
| Reported EBITDA | PBT + D + Fin | 74.61 | 96.14 | 102.04 | 399.68 |
| Reported EBITDA margin | ÷ Rev | 9.2% | 10.3% | 11.1% | 10.8% |
| Core PBT (ex-OI) | PBT − OI | 32.75 | 51.37 | 65.56 | 240.58 |
| Other Income / PBT | OI ÷ PBT | 28.5% | 19.6% | 7.5% | 14.6% |
| Effective tax rate | Tax ÷ PBT | 17.9% | −42.6% | 20.4% | 5.6% |
| Current-tax-only ETR | Curr tax ÷ PBT | 37.9% | 27.4% | 32.4% | 28.7% |
| PAT margin | PAT ÷ Rev | 4.6% | 9.8% | 6.1% | 7.2% |

Reconciliation to management framing: press "EBITDA ₹102 Cr, +37%" (PR:L71) = **Reported** EBITDA (102.04), which includes ₹5.31 Cr other income; deck "EBITDA margin 11%" (PP:L234) = 102.04/917.07 = 11.1%. Anchor analysis to **Operating** EBITDA (10.5%), which strips other income.

### 1C. STANDALONE P&L (from R:L256-286)

| Line Item | Q1 FY26 | Q4 FY26ᴮ | Q1 FY27 | FY26 |
|---|---|---|---|---|
| Revenue from operations | 142.15 (R:L256) | 135.85 (R:L256) | 157.52 (R:L256) | 563.28 (R:L256) |
| Other income | 9.98 (R:L257) | 44.19 (R:L257) | 4.96 (R:L257) | 150.05 (R:L257) |
| Cost of materials consumed | 97.34 (R:L260) | 77.12 (R:L260) | 50.35 (R:L260) | 334.51 (R:L260) |
| Purchases of stock-in-trade | 19.85 (R:L261) | 8.98 (R:L261) | 39.29 (R:L261) | 45.53 (R:L261) |
| Change in inventories | (19.53) (R:L262) | 5.49 (R:L262) | 7.13 (R:L262) | (7.01) (R:L262) |
| Employee benefits | 15.82 (R:L263) | 15.21 (R:L263) | 17.69 (R:L263) | 60.89 (R:L263) |
| Finance costs | 2.45 (R:L264) | 2.16 (R:L264) | 1.69 (R:L264) | 9.69 (R:L264) |
| Depreciation & amortisation | 1.87 (R:L265) | 2.00 (R:L265) | 2.01 (R:L265) | 7.65 (R:L265) |
| Other expenses | 23.72 (R:L266) | 27.26 (R:L266) | 26.38 (R:L266) | 101.03 (R:L266) |
| PBT before exceptional | 10.62 (R:L268) | 41.82 (R:L268) | 17.96 (R:L268) | 161.03 (R:L268) |
| Exceptional items | ND (nil) (R:L269) | 58.43 (R:L269) | ND (nil) (R:L269) | 58.43 (R:L269) |
| PBT after exceptional | 10.62 (R:L270) | 100.25 (R:L270) | 17.96 (R:L270) | 219.45 (R:L270) |
| Current tax | 1.79 (R:L272) | 4.68 (R:L272) | 3.58 (R:L272) | 12.29 (R:L272) |
| Deferred tax | (0.19) (R:L273) | (47.53) (R:L273) | 1.10 (R:L273) | (49.39) (R:L273) |
| Total tax | 1.60 (R:L274) | (42.85) (R:L274) | 4.68 (R:L274) | (37.10) (R:L274) |
| **PAT** | **9.02** (R:L275) | **143.11** (R:L275) | **13.28** (R:L275) | **256.55** (R:L275) |
| EPS basic (₹) | 0.54 (R:L285) | 8.58 (R:L285) | 0.79 (R:L285) | 15.40 (R:L285) |

Standalone Q4FY26 PAT (143.11) is inflated by a ₹58.43 Cr exceptional gain (R:L269) **and** a ₹47.53 Cr deferred-tax credit (R:L273) — the "₹47.6 Cr MAT credit" management strips out in the press release (PR:L91) and deck (PP:L540). Neither one-off survives consolidation at scale (consol exceptional nets to just 0.18 Cr).

🛑 Every cell filled or ND. Proceeding to analysis.

---

## STEP 2 — Q1 FY27 YoY COMPARISON (Q1 FY27 vs Q1 FY26, CONSOLIDATED) — the most important step

| Metric | Q1 FY26 | Q1 FY27 | YoY % | Verdict |
|---|---|---|---|---|
| Revenue from operations | 813.74 | 917.07 | **+12.7%** | Grew — but see one-off + FX caveats |
| Revenue ex-IEEPA one-off (−25.59) | 813.74 | 891.48 | **+9.6%** | Underlying softer |
| Operating EBITDA | 61.54 | 96.73 | +57.2% | Strong headline |
| Operating EBITDA ex-IEEPA (−25.59) | 61.54 | 71.14 | **+15.6%** | Real underlying rate |
| Operating EBITDA margin | 7.6% | 10.5% | +297 bps | Expanded (deck cites 417 bps gross) |
| Depreciation | 25.29 | 26.63 | +5.3% | Below revenue growth — no absorption gap |
| Finance costs | 3.50 | 4.54 | +29.7% | Rising off a tiny base (net-cash co.) |
| EBIT (operating) = OpEBITDA − D | 36.25 | 70.10 | +93.4% | Flattered by one-off |
| Other income | 13.07 | 5.31 | −59.4% | Fell — NOT the growth driver (positive quality signal) |
| **Core operating PBT (PBT − OI)** | 32.75 | 65.56 | **+100.2%** | Doubled on reported basis… |
| **Core operating PBT ex-IEEPA (−25.59)** | 32.75 | 39.97 | **+22.1%** | …≈+22% once the tariff refund is removed |
| Reported PBT | 45.82 | 70.87 | +54.7% | — |
| **Reported PBT ex-IEEPA (−25.59)** | 45.82 | 45.28 | **−1.2% (FLAT)** | **Core pre-tax profit is essentially flat YoY once the one-off is stripped** |
| PAT | 37.63 | 56.38 | +49.8% | Matches PR "+50%" (PR:L72) |
| EPS basic (₹) | 2.26 | 3.37 | +49.1% | — |

**Six mandatory diagnostics:**

1. **Did revenue grow YoY?** Yes, +12.7% reported (917.07 vs 813.74). But management concedes constant-currency revenue "remained broadly flat" (PR:L127, F7-01) and ₹25.59 Cr of the reported figure is the non-recurring IEEPA refund (Note C8). Ex one-off, +9.6%; ex one-off AND ex-FX, roughly flat. **The headline overstates underlying demand.**
2. **Margin — expand/contract/flat?** Operating EBITDA margin **expanded** to 10.5% (Q1FY27) vs 7.6% (Q1FY26) = +297 bps. Genuine mix improvement (in-house brands 57% vs 36% of B2C, PR:L90) is real, but part of the gross-margin lift is the ₹25.59 Cr refund landing in revenue at ~zero cost. Deck's own EBITDA walk starts from a 4.2% base that contradicts the 9% reported Q1FY26 margin (FND-09) — unreconciled; see Q8.
3. **Did core operating PBT grow YoY?** Reported: +100.2% (32.75 → 65.56). **Ex-IEEPA: +22.1%.** And reported PBT ex-IEEPA is FLAT (−1.2%). So the "doubling" is half real mix/operating leverage, half a tariff refund. Name the gap: **≈₹25.59 Cr (the IEEPA revenue booking) accounts for roughly all of the reported-PBT growth.**
4. **What drove the gap between core-PBT growth and reported-PAT growth?** Reported PBT +25.05 Cr; PAT +18.75 Cr. Difference = tax rose +6.30 Cr (ETR 17.9% → 20.4%). Other income FELL 7.76 Cr (a drag, not a prop — the *good* kind of quality). Deferred-tax credit near-constant (−9.19 → −8.48). No exceptional either period. So the headline PAT growth is **not** treasury-driven — it is operating + one-off tariff, partially taxed.
5. **Are D&A / finance costs scaling faster than revenue?** No. D&A +5.3% vs revenue +12.7% — no capex-absorption deficit. Finance +29.7% but off ₹3.50 Cr (immaterial for a net-cash company).
6. **Is Other Income concentration changing?** Falling, both absolute (13.07 → 5.31) and as share of PBT (28.5% → 7.5%). Quarterly quality *improved* on this axis. (Contrast standalone, where OI is 45–150 Cr of intragroup dividend noise — see the S-vs-C section.)

🛑 YoY table + six diagnostics complete.

---

## STEP 3 — SEQUENTIAL QoQ TRAJECTORY (CONSOLIDATED, last available quarters)

Only three consecutive consolidated quarters are extractable from this filing (Q1FY26, Q4FY26, Q1FY27); Q2/Q3 FY26 are not in this artifact and are ND (no prior ledger). The deck supplies the same three-point series (PP:s17/s18, chart labels Revenue 814/935/917, EBITDA 75/96/102, PAT 38/44*/56).

| Quarter | Revenue | Op EBITDA margin | Core PBT (ex-OI) | One-offs flagged | QoQ run-rate |
|---|---|---|---|---|---|
| Q1 FY26 | 813.74 (R:L79) | 7.6% | 32.75 | none | base |
| Q2 FY26 | ND | ND | ND | ND | ND |
| Q3 FY26 | ND | ND | ND | ND | ND |
| Q4 FY26ᴮ | 934.71 (R:L79) | 8.9% | 51.37 | consol exceptional 0.18 (R:L92); big DTA credit 44.76 (R:L96); standalone MAT credit 47.53 / exceptional 58.43 | seasonal peak (Q4 is the festive/holiday high) |
| Q1 FY27 | 917.07 (R:L79) | 10.5% | 65.56 | **IEEPA refund +25.59 in revenue** (C8) | −1.9% rev QoQ; margin up |

**Diagnostics:**
- **Run-rate trajectory:** Revenue dipped −1.9% QoQ (917.07 vs 934.71) — expected, Q4 is the seasonal peak for a Western gifting-led retailer. Operating EBITDA margin *rose* sequentially (8.9% → 10.5%), helped by the one-off.
- **Reported PAT QoQ is the reframing trap:** reported basis 56.38 vs 91.14 = **−38.1% QoQ** (a decline). Management shows **+29%** by rebasing Q4 to ₹44 Cr ex-MAT-credit (PR:L84 footnote L91; PP:L540). Both numbers are tax-distorted. Cleanest QoQ read is **PBT: 70.87 vs 63.91 = +10.9%**, or current-tax-only PAT: 47.90 vs 46.38 = +3.3%. **Neither the +29% (management) nor the −38% (reported) is the true operating trend; PBT +10.9% is.** (F8-01, F16-01, FND-04.)
- **Q4 base is a balancing figure** (C7) — QoQ comparisons carry extra uncertainty.
- **Implied Q2 FY27 base to hold trajectory:** to keep operating EBITDA margin ≥10% *without* the IEEPA tail, Q2 needs ~₹71 Cr underlying operating EBITDA on a seasonally softer top line — a demanding bar given constant-currency-flat demand.

🛑 QoQ table + diagnostics complete.

---

## STEP 4 — OPERATIONAL DECOMPOSITION (PAT bridge, CONSOLIDATED, Q1 FY26 → Q1 FY27)

Reported PAT change +18.75 Cr (37.63 → 56.38). PBT walk first (+25.05 Cr), then tax:

| Component | YoY change (₹ Cr) | Recurring? |
|---|---|---|
| Gross profit: revenue +103.33 with COGS (materials+purchases+Δinv) DOWN 2.72 (274.29 vs 277.01) → GP +106.05 | +106.05 | Recurring mix — BUT includes ~25.59 IEEPA revenue + a slice of the 12.81 inventory write-down benefit |
| Employee benefits | −3.87 | Recurring |
| Other expenses (incl. content/broadcasting 196.55 vs 165.03, +31.52) | −67.00 | Recurring |
| Depreciation | −1.34 | Recurring |
| Finance costs | −1.04 | Recurring |
| Other income | −7.76 | Non-recurring by nature (fell) |
| Exceptional items | 0.00 | — |
| **= Reported PBT change** | **+25.05** | — |
| Tax (ETR 17.9% → 20.4%) | −6.30 | Mixed (deferred-tax-credit dependent) |
| **= Reported PAT change** | **+18.75** | — |

**Mandatory questions:**
- **% of PAT change from recurring core vs non-recurring?** Strip the ₹25.59 Cr IEEPA revenue (pre-tax) → residual reported PBT growth is **−0.5 Cr (flat)**. Post-tax, the IEEPA piece (~₹25.59 Cr less ~20% tax ≈ ₹20.4 Cr) **exceeds the entire ₹18.75 Cr reported PAT increase.** Conclusion: **on a clean, one-off-adjusted basis, core PAT did not grow YoY; the reported +50% is one-off + FX + genuine-but-smaller mix leverage.** This is the single most important line in the review.
- **If Other Income reverts to prior-year level (13.07):** PBT would be ~8 Cr higher, but that only masks the underlying flatness further — OI is not the prop this quarter.
- **D&A / finance at steady state?** D&A ~₹26–28 Cr/qtr is stable; no ramp. Finance immaterial.
- **Tax adjustments inflating/deflating PAT?** Persistent deferred-tax credits every period (−8.48 this quarter, R:L96) hold blended consol ETR (20.4%) ~12 pp below the current-tax-only ETR (32.4%) — **ETR step-up risk when carryforwards/DTA exhaust** (A3-05 / F8). FY26 blended ETR was just 5.6%.

🛑 Bridge complete.

---

## STEP 5 — CASH QUALITY & BALANCE SHEET

**Data-availability rule (v1.2):** this is a **Q1** Reg-33 filing — no balance sheet and no cash-flow statement are present (confirmed by full read, results ledger §"No Balance Sheet…", R:L175 note). Reg 33 mandates these only at H1/FY. Therefore the standard cash rows are **ND this quarter**.

| Metric | Prior period | Current period | Change | Verdict |
|---|---|---|---|---|
| CFO | ND | ND | ND | Not disclosed at Q1 |
| CFO/PAT ratio | ND | ND | ND | **Cannot be computed — see cap below** |
| Capex (PPE+CWIP) | ND | ND | ND | ND |
| FCF | ND (FY26 ₹272 Cr per deck PP:L737) | ND | ND | Deck FY26 annual only |
| Working-capital change | ND | ND | ND | ND |
| Receivable / Inventory / Payable days | ND | ND | ND | ND |
| Cash conversion cycle | ND | ND | ND | ND |
| PPE / CWIP | ND | ND | ND | ND |
| Net debt / (Net cash) | (Net cash) — FY26 ₹296 Cr (PR:L86) **OR ₹387 Cr (PP:L731)** — CONFLICT | Net cash ₹287 Cr (PR:L86) | −₹9 Cr QoQ (per PR) | **Net cash, but FY26 base disputed by ₹91 Cr (FND-06)** |
| Promoter pledge | ND | ND | ND | Not disclosed in this filing |

**Cash-conversion verdict = INDETERMINATE.** Per house rule, INDETERMINATE cash conversion may NOT resolve silently to PROCEED; it **caps the verdict at PROCEED WITH CAVEATS**, with the missing evidence named:
1. No Q1 cash-flow statement (structural to Reg-33 Q1) — CFO/PAT unverifiable until the H1 FY27 filing.
2. **Net-cash figure is internally inconsistent across management's own documents:** press release net cash Q4FY26 = ₹296 Cr and Q1FY27 = ₹287 Cr (PR:L86); deck slide 26 chart plots FY26 net cash = ₹387 Cr with ₹296 Cr as the FY25 bar (PP:L731/L739); deck slides 11 and 35 call ₹296 Cr "net cash… as on FY26" (PP:L275, L1052). **A ₹91 Cr (>30%) discrepancy in the headline balance-sheet metric, unreconciled (FND-06).** Until reconciled, net-cash quality is not established.
3. **Budget Pay = 38% of B2C revenue** is EMI/instalment financing (PP:L654, L1148) framed only as "affordability," never as a customer-receivable / credit-exposure line (FND-10). For a business selling on instalments to value-conscious Western consumers, this is a working-capital and credit-risk item the filing is silent on.

**What IS observable (management-sourced, annual, unaudited-in-deck):** FY26 FCF ₹272 Cr, net cash ₹296/387 Cr (disputed), ROCE 24%, ROE 18% (PP:s26/s29). These are FY26 annual figures, not Q1FY27 balance-sheet actuals, and cannot substitute for the Q1 cash statement.

🛑 Cash quality = INDETERMINATE → verdict capped at PROCEED WITH CAVEATS, evidence named.

---

## STEP 5S — STANDALONE-vs-CONSOLIDATED PAT GAP (first-class metric, from A3-01 / F2)

Definition: S-C gap % = (Consolidated PAT − Standalone PAT) ÷ Consolidated PAT.

| Period | Consol PAT (R:L98) | Standalone PAT (R:L275) | Subsidiary net contribution (₹ Cr) | **S-C gap %** |
|---|---|---|---|---|
| Q1 FY26 | 37.63 | 9.02 | +28.61 | **+76.0%** |
| Q4 FY26 | 91.14 | 143.11 | −51.97 | **−57.0%** |
| Q1 FY27 | 56.38 | 13.28 | +43.10 | **+76.4%** |
| FY26 | 266.13 | 256.55 | +9.58 | **+3.6%** |

**Reading:** In normal quarters (Q1FY26, Q1FY27) subsidiaries generate ~76% of consolidated PAT — consistent with the model (US/UK/Germany retail subsidiaries do the selling; the Indian parent manufactures/sources; subs = 82.8% of consolidated revenue, results forensics F2). The **−57% swing in Q4FY26 is an artefact**: standalone Q4 PAT (143.11) was inflated by a ₹58.43 Cr standalone exceptional gain + ₹47.53 Cr deferred-tax (MAT) credit — one-offs that net to ~zero on consolidation and are almost certainly intragroup (e.g., an intragroup dividend / restructuring eliminated in consol). **Never use standalone VGL numbers for trajectory** — they are polluted by intragroup dividends, exceptional items and MAT-credit timing. The consolidated statement is the only clean read. Bridge of the standalone one-offs to intragroup flows is a management question (Q1, from A3-01).

---

## STEP 6 — RECONCILIATION VS THESIS (initiation framing — no prior Notion thesis exists)

There is no Notion Bear/Base/Bull, no watchlist, no thesis-broken trigger, no growth-trigger register for VGL. 6A-6D are therefore populated as an **initiation baseline** using this quarter's filings plus management's own stated targets, so that Q2 FY27 has something to diff against. Nothing here is retrofitted to a prior view.

### 6A. Variance vs management's own guardposts (no analyst projections exist yet)
| Metric | Management reference | Q1 FY27 actual | Reading |
|---|---|---|---|
| Revenue | FY30 target ₹5,000–5,500 Cr (PP:L1004); FY26 ₹3,691.79 | ₹917.07 Cr (~₹3,668 annualised) | On the FY30 path only if growth re-accelerates; constant-currency flat this quarter is *behind* the implied ramp |
| Digital mix | FY27 target 50% of B2C (from 44%) (PP:L1008) | 45% (PR:L88) | On track, small gap |
| In-house brands | FY27 target 60%+ of B2C (from 48.8%) (PP:L1018) | 57.2% (PP:L410) | Ahead of pace |
| Germany | "contribute towards profitability from FY27" (PP:L1028) | Europe (incl. Germany) segment PBIT −2.89 Cr (R:L142) | Behind — Europe swung to a loss YoY (see 6D) |
| Net cash | net-cash, no debt (PP:L1052) | ₹287 Cr (PR:L86) | Confirmed net-cash; magnitude disputed (FND-06) |

### 6B. Initiation watch-list (seed for Q2 FY27)
| # | Item | Green | Red | Q1 FY27 reading | Status |
|---|---|---|---|---|---|
| 1 | Constant-currency revenue growth | >0% | <0% | "broadly flat" (PR:L127) | **AMBER** |
| 2 | Operating EBITDA margin ex one-offs | ≥9% | <7% | ~7.8% ex-IEEPA | AMBER |
| 3 | UK + Europe segment PBIT | positive | negative | UK −0.47, Europe −2.89 (R:L140,142) | **RED** |
| 4 | Net-cash reconciliation | figures agree | >10% gap | ₹91 Cr gap (FND-06) | **RED (disclosure)** |
| 5 | Blended ETR normalisation | stable | rising >25% | 20.4%, current-tax 32.4% (A3-05) | AMBER |
| 6 | Section 122 tariff outcome | refund booked | permanent cost | ₹14.26 Cr unbooked (C8) | UNKNOWN |

### 6C. Thesis-broken trigger check
No pre-committed thesis-broken conditions exist (first coverage). **None can FIRE.** Nothing forces an exit because there is no position. For the record, the two conditions a future thesis would most plausibly encode — (a) two consecutive quarters of negative constant-currency revenue, and (b) UK+Europe structurally loss-making — are both **AMBER/RED already this quarter** and should be written into the Notion thesis when opened.

### 6D. Growth-trigger status (initiation register)
| Trigger | Confidence | Confirming evidence (this qtr) | Killing evidence (this qtr) | Status |
|---|---|---|---|---|
| In-house-brand margin engine | High | 57.2% of B2C, +2,200 bps YoY (PR:L90); gross margin +417 bps (PR:L82) | Part of margin lift is IEEPA one-off | **ON TRACK** |
| Digital / Shopify-led shift to 50% | Medium | Digital 45%; all sites migrated to Shopify Enterprise in-quarter (PR:L145) | Digital ASP the only rising ASP but volume roughly flat | ON TRACK |
| Germany / Europe profit inflection | Medium | Germany "first full year of positive EBITDA" FY26 (PP:L700) | Europe PBIT −2.89 Cr Q1FY27 vs +12.88 Q1FY26 (R:L142) | **DELAYED / WEAKENED** |
| Ideal World + Mindful Souls scale-up | Medium | Ideal World £6mn, 143K customers; both "delivered profitably FY26" (PP:s32) | Mindful Souls "lower recurring subscription revenues… reduced acquisition" (PP:L944-946) | ON TRACK (Mindful Souls softening) |
| TV home-shopping base | Low | TV revenue +9% YoY in INR (PP:L225) | **TV volume −3.9% and USD ASP −4.4% YoY (FND-08); +9% is pure FX** | **WEAKENED** |
| Lab-grown diamonds / new categories | Low | 13% of jewellery mix; market $34bn→$92bn by 2034 (PP:s33) | Early, unquantified | ON TRACK (optionality) |

🛑 6A-6D complete (initiation baseline).

---

## STEP 7 — FOUR-PILLAR RE-VALIDATION (initiation inputs only — no prior destination PE to revalidate)

No Section 1B destination PE has ever been set for VGL, and **FTTCP has not been run** (Master v3.3 L77: Pillar 1 cannot be computed without the FTTCP ROCE forward verdict). I therefore do **not** compute a destination PE here (doing so would breach the framework). I record the pillar *inputs this quarter supplies*, for the pending FTTCP/Role 1 workup:

| Pillar / input | This quarter's reading | Note for FTTCP/Role 1 |
|---|---|---|
| ROCE base (0.5×ROCE+7.5, floor 9, cap 24) | Deck ROCE **24%** "as on FY26" (PP:L857) → formula gives 19.5x pre-cap | ROCE is a deck-stated FY26 annual figure, not a Q1 computation; **FTTCP must set the forward verdict** before Pillar 1 is fixed. 24% ROCE with a disputed net-cash base (FND-06) needs verification. |
| Cash multiplier (Pillar 2) | **INDETERMINATE** (Step 5) | Cannot band the 0.65/0.80/1.00/1.15/1.30 multiplier at Q1 (no CFO). FY26 FCF ₹272 Cr / PAT 266.13 ≈ 1.02x if the deck FCF is accepted — but that is annual and unaudited-in-deck. Resolve at H1 FY27. |
| Growth visibility premium (Pillar 3) | Mixed: brand-mix + digital on track; TV + Europe weakening; constant-currency flat | Catalyst proximity modest this quarter. |
| Strategic premium | Vertical integration, owned brands, 0% marketplace take-rate (PP:L472), 16 owned brands | Respect single-credit rule with Pillar 1. |
| UA multiplier (1.25×) | Not assessed (needs the 3 qualifiers evidenced) | First coverage — defer to Role 1. |
| Sector cap | Consumer/retail e-tail — cap per Section 1B table (not reproduced here) | Absolute ceiling; UA cannot breach. |
| Hurdle-ratio recheck | Not computable — no current PE / EPS-CAGR set for an uncovered name | Compute at Role 1. |

**Pillar action: NONE re-validated (nothing prior existed). Destination PE deferred to FTTCP→Role 1.** No stale fair value to update.

🛑 Pillar inputs recorded; no destination PE asserted.

---

## STEP 8 — POSITION DECISION (Branch 8A-W — NON-HELD / INITIATION)

Decision Status verified = **NOT YET COVERED / NO POSITION** (Step 0A). The 8A held-position branch does NOT apply. Applying 8A-W:

- No thesis-broken condition exists → cannot fire → **no AVOID reclassification forced.**
- Actuals vs "bear/base/bull": no analyst projections exist, so the below/between/above test is not literally runnable. Judged against management's own guardposts (6A), the quarter lands **mixed-to-soft**: reported growth is real but one-off/FX-flattered; two segments (UK, Europe) swung to losses; the balance-sheet headline is internally inconsistent.

**8A-W output — initiation view:**
- **Recommendation: WATCHLIST / INITIATE-DILIGENCE (fresh look), NOT a buy today.** The business is high-quality on structure (vertical integration, owned brands, net cash, 24% stated ROCE, clean audit) but this specific quarter's headline overstates momentum: strip the ₹25.59 Cr IEEPA refund and FX, and revenue/PBT are ~flat, with the UK and Europe legs loss-making.
- **No entry zone can be set here** — it requires FTTCP → Role 1 (destination PE) → MoS. Explicitly deferred, not invented.
- **Master decision gate:** open the Notion page with Decision Status = WATCHLIST; run FTTCP then Role 1/2/3 to set the entry zone; **re-gate at H1 FY27** when the first cash-flow statement and balance sheet arrive (resolves the INDETERMINATE cash conversion and the ₹91 Cr net-cash conflict).
- **Overall protocol verdict: PROCEED WITH CAVEATS** — capped there (not PROCEED) by INDETERMINATE cash conversion per house rule; caveats = the IEEPA one-off, constant-currency-flat demand, UK/Europe losses, ETR step-up risk, and the unreconciled net-cash figure.

### 8B. Add-back / trim triggers
Not applicable — no position, no ladder. To be authored at Role 2 when the thesis opens.

### 8C. Single cleanest metric for Q2 FY27
**Constant-currency revenue growth of the consolidated group, ex the IEEPA/Section-122 tariff items.** It is the cleanest resolver of the bull/bear split because this quarter proved the reported line is flattered by both FX and a one-off.
- **Bull threshold:** constant-currency revenue up >5% YoY with UK+Europe segment PBIT back to positive.
- **Bear threshold:** constant-currency revenue flat-to-negative for a second consecutive quarter (would satisfy condition (a) that a future thesis-broken trigger should encode).

🛑 Position decision (8A-W), trigger note, and single cleanest metric stated.

---

## STEP 8.5 — QUESTIONS FOR MANAGEMENT

**Coverage map (every FORWARD-SIGNAL / AMBIGUOUS A3 finding → ≥1 question):**
A3-01→Q1 · A3-02→Q11 · A3-03→Q5 · A3-04→Q5 · A3-05→Q6 · A3-06→Q7 · A3-07→Q4 · A3-08→Q9 · F7-01→Q2 · F6-01→Q10 · F8-01→Q3 · F16-01→Q3 · FND-02→Q4 · FND-03→Q4 · FND-08→Q2 · FND-04→Q3 · FND-06→Q8 · FND-09→Q8 · FND-10→Q12. (NEUTRAL-FACTs A3-09, F14-01, FND-01, FND-05, FND-07 → Monitorables, no question required.)

| # | Question | Why it matters | Bull answer | Bear answer |
|---|---|---|---|---|
| 1 | Standalone Q4FY26 PAT (₹143.11 Cr) exceeded consolidated (₹91.14 Cr) on a ₹58.43 Cr exceptional + ₹47.53 Cr deferred-tax credit that net to ~zero in consol. Please bridge the standalone exceptional and other income to the specific intragroup flows (dividends/restructuring). [A3-01] | Standalone is being cited (MAT credit) yet is polluted by intragroup one-offs | Clean, one-time intragroup dividend, fully eliminated | Recurring intragroup engineering that flatters standalone optics |
| 2 | Reported revenue rose 13% YoY but you state constant-currency was "broadly flat," and TV unit volume fell 3.9% with USD ASP down 4.4%. What was constant-currency revenue by segment, and what is your FX sensitivity (₹ per 1% USD/GBP move)? [F7-01, FND-08] | Tests whether growth is demand or FX | Specific CC growth positive in ≥2 regions | CC negative; growth entirely FX |
| 3 | Q1FY27 PAT of ₹56 Cr is +50% YoY but −38% QoQ on a reported basis (the +29% you show rebases Q4 ex-₹47.6 Cr MAT credit). Is Q1FY27 PAT free of comparable one-offs, and what is the normalised effective tax rate you expect for FY27? [F8-01, F16-01, FND-04] | Separates clean earnings from tax/one-off framing | Q1 clean; normalised ETR guided | Q1 also one-off-aided; ETR to step up |
| 4 | UK segment PBIT was −₹0.47 Cr and Europe(ex-UK) −₹2.89 Cr in Q1FY27 vs +₹9.78 Cr and +₹12.88 Cr a year ago, yet the deck promises Germany "profitability from FY27" and Europe margins to "strengthen meaningfully over the year." What quarterly EBITDA path gets Europe to positive, and by which quarter? [A3-07, FND-02, FND-03] | Two of five regions are loss-making; a core catalyst | Named quarter + margin bridge | Vague "over the year," no date |
| 5 | You have paid but NOT booked ₹14.26 Cr (USD 1.5M) of Section 122 tariffs pending the Federal Circuit merits appeal. What is the expected ruling timeline, and at what point do you recognise a receivable versus expense it permanently? [A3-03, A3-04] | Unbooked binary catalyst / cost | Dated calendar, high-probability refund | Open-ended, likely permanent cost |
| 6 | Blended consolidated ETR was 20.4% (current-tax-only 32.4%) this quarter and just 5.6% for FY26, held down by persistent deferred-tax credits. When do the carryforwards/DTA exhaust, and what steady-state ETR should we model? [A3-05] | ~12 pp of PBT is tax-shielded; step-up risk | DTA runway multi-year, low steady ETR | Near exhaustion; ETR jumps |
| 7 | FX-translation OCI reversed to −₹0.80 Cr this quarter from +₹49.31 Cr in Q4FY26 and +₹109.59 Cr for FY26. Given ~90% of revenue is USD/GBP/EUR, how much of reported profit and book-value growth is currency, and how do you hedge it? [A3-06] | Net-worth tailwind stalled | Modest, hedged FX exposure | Book value was FX-inflated, now reversing |
| 8 | Net cash is shown three ways: ₹287 Cr (Q1FY27, press release), ₹296 Cr ("as on FY26," slides 11/35), and ₹387 Cr (FY26 on the slide-26 chart). Which is the audited FY26 net-cash figure, and what is the exact Q1FY27 number? Separately, what is the ₹4.2% base of the EBITDA-margin walk versus the 9% reported Q1FY26 margin? [FND-06, FND-09] | ₹91 Cr headline inconsistency + unreconciled walk base | One clean reconciliation | Persistent inconsistency = disclosure-quality flag |
| 9 | EY has been appointed internal auditor for FY27-28 while also acting as your investor-relations advisor. Who was the outgoing internal auditor, why the change, and how is EY's independence maintained across the two mandates? [A3-08] | Governance / independence optics | Routine upgrade; ring-fenced teams | Remediation-driven; independence unclear |
| 10 | You migrated all retail sites to Shopify Enterprise in-quarter at ~one-third the prior re-platforming cost. What single ECom KPI (conversion, digital revenue growth, or CAC) will you hold yourself to next quarter to evidence the promised acceleration? [F6-01] | Converts a completed migration into a testable promise | A specific committed KPI | No KPI = unfalsifiable claim |
| 11 | Four subsidiaries (₹414.01 L PAT, ₹10,560.67 L revenue) were reviewed by other auditors, not BSR, and are unnamed. Which four, and what were their YoY growth and margins? [A3-02] | 7.3% of consol PAT / 11.5% of revenue on other-auditor numbers | Named, healthy, immaterial | Concentrated or deteriorating |
| 12 | Budget Pay (EMI/instalment sales) was 38% of B2C revenue. What is the associated customer receivable balance, its ageing, and the loss/charge-off rate? [FND-10] | An unaddressed credit/working-capital exposure | Small book, low losses | Large receivable, rising defaults |

**Top 3 by likelihood of thesis-changing information:**
1. **Q2 (constant-currency growth / FX sensitivity)** — would change the *bull* case: if CC growth is genuinely positive, the flat-demand read is wrong and the multiple story survives.
2. **Q4 (UK/Europe path to profit)** — would confirm the *bear* case: back-to-back regional losses with only "over the year" language would validate the weakening-geography risk.
3. **Q8 (net-cash reconciliation + EBITDA-walk base)** — tests *management transparency*: a business leaning on "Big Four audit / governance award" claims (PP:L1066) should reconcile its own headline balance-sheet number instantly.

**Channel recommendation:** No concall was held for this result (none in the document set). Recommend a **formal IR email** with all 12 questions verbatim to Vivek Jain (Head-IR, PR:L198) and the EY IR desk (PR:L205-208), prioritising the top 3; carry the remainder into the next scheduled concall. Log all 12 as pre-committed watchpoints for the Q2 FY27 review.

🛑 Questions table + top-3 + channel complete.

---

## ROLE 5 — CONCALL ANALYSIS: **N.A. THIS RUN**

**No concall transcript exists in this document set.** Role 5 is not fabricated. State explicitly:
- Steps 1-9 of the Concall Protocol are **N.A.** — no claims inventory, no forward-guidance-vs-prior table (no prior concall log; first coverage), no promise-vs-delivery credibility ratio, no Q&A decomposition, no tone/specificity 6E archetype.
- **Management-communication surrogate:** the press-release MD quote (PR:L118-175) and the investor deck (PP) are treated per Role 4 as *management-communication sources feeding the results review*, NOT as a concall. Their forward statements are captured in the Monitorables/Catalyst register below and cross-referenced to the A3 commitment registers.
- **Role 1 track-record input:** no credibility ratio can be produced (no Role 5 history). Role 1 must use its default track-record treatment until a concall is analysed. Note for the file: the press release/deck already show two **soft-framing tells** an eventual Role 5 should score — the ex-MAT-credit QoQ PAT rebase (F16-01/FND-04) and the reported-vs-constant-currency revenue gap (F7-01) — early evidence leaning toward an OVERPROMISER watch, to be confirmed once a live call is analysed.
- **Peer concall cross-check:** no peer in the analysed universe reported in the ±4-week window that is passed to this run; recorded as "none in window."

---

## MONITORABLES / CATALYST REGISTER (seeded by A3 commitment registers F6/F13 + neutral-facts)

| Item | Implied date | Source ref | Type |
|---|---|---|---|
| Interim dividend ₹1.50/sh paid | record 12 Aug 2026; pay by ~3 Sep 2026 | R:L33-37, R:L194-196 | Capital return (~₹25.1 Cr outflow, hits Q2 cash) |
| Section 122 tariff (₹14.26 Cr) ruling — Federal Circuit merits panel | undated (US court calendar) | R:L219-229 (A3-03/04) | Binary catalyst — unbooked gain or permanent cost |
| Germany segment to "contribute towards profitability" | FY27 | PP:L1028 (FND-02) | Delivery test; Europe PBIT currently negative |
| Europe margins to "strengthen meaningfully over the course of the year" | FY27 full year | PP:L387-388 (FND-03) | Delivery test — Q2 Europe margin is the tell |
| Shopify Enterprise migration → ECom acceleration | Q2-Q3 FY27 | PR:L145 (F6-01) | Promise-vs-delivery; demand a committed KPI (Q10) |
| Digital 50% of B2C (from 45%) | FY27 | PP:L1008 | Progress metric |
| In-house brands 60%+ of B2C (from 57.2%) | FY27 | PP:L1018 | Ahead of pace |
| Revenue ₹5,000–5,500 Cr | FY30 | PP:L1004 | Long-range anchor |
| First H1 FY27 cash-flow + balance sheet (resolves INDETERMINATE cash conversion & net-cash conflict) | ~Nov 2026 | Step 5 | Re-gate trigger |
| EY internal-audit appointment (independence watch) | effective 4 Aug 2026 | R:L42-43 (A3-08) | Governance monitorable |
| Fresh MSOP/RSU/ESOP grant (dilution watch) | vesting FY27-FY30 | R:L556-584 (FND-05) | Minor dilution |
| Net-cash figure reconciliation (₹287 / 296 / 387 Cr) | next filing | FND-06 | Disclosure-quality flag |
| Meals-donated drafting inconsistency (113mn vs 115mn) | — | PR:L110 vs L190 (F14-01) | Neutral drafting-control datapoint |
| Section-badge / dual-email-domain drafting defects | — | PP:s23/s30 (FND-07) | Neutral drafting-control datapoint |

---

## PLAIN-LANGUAGE BRIEF (mandatory, four parts)

### 1. SUMMARY NARRATIVE
Vaibhav Global reported Q1 FY27 (quarter ended 30 June 2026) consolidated revenue of ₹917 Cr, up 13% year on year, EBITDA of ₹102 Cr up 37%, and PAT of ₹56 Cr up 50% (all this quarter's filing; PR:L70-72). The headline looks strong, but three adjustments matter. First, about ₹25.6 Cr of that revenue is a one-off United States tariff (IEEPA) refund booked as operating revenue this quarter (this quarter's filing, R:L214-215); it is pure profit and does not repeat. Strip it, and reported pre-tax profit is essentially flat versus a year ago. Second, management itself concedes that on a constant-currency basis revenue "remained broadly flat" (this quarter's filing, PR:L127) — the 13% is largely a weaker rupee, not more selling. Third, the +50% PAT is a year-on-year figure; sequentially, reported PAT actually fell 38% from Q4's ₹91 Cr, and the +29% management shows uses a Q4 base stripped of a ₹47.6 Cr tax credit (this quarter's filing, PR:L91). The cleanest sequential read is pre-tax profit, up about 11%. Underneath, the genuine good news is real: in-house brands reached 57% of consumer revenue (from 36% a year ago) and gross margin rose ~417 bps (this quarter's filing, PR:L82,L90), lifting operating EBITDA margin to 10.5%. The genuine concern is also real: the UK and Europe segments swung from profit to loss year on year (this quarter's filing, R:L140,L142), and TV — still the largest channel — is shrinking on both volume (−3.9%) and US-dollar price (−4.4%), masked by currency (this quarter's filing, PP:L543). The audit is clean and unmodified. Because this is a Q1 filing there is no cash-flow statement or balance sheet, so cash conversion is INDETERMINATE and the net-cash figure is quoted three different ways (₹287 / ₹296 / ₹387 Cr) across the company's own documents (this quarter's filing, PR:L86 vs PP:L275/L731). This is first-time coverage: no position is held, no prior thesis exists. The verdict is PROCEED WITH CAVEATS — a high-quality, net-cash, vertically-integrated retailer worth a proper workup, but a quarter whose optics run ahead of its underlying trajectory. Next step is to open the name as WATCHLIST, run FTTCP then valuation, and re-gate at H1 FY27 when the cash statement arrives.

### 2. SECTOR INTELLIGENCE
VGL sells fashion jewellery and lifestyle products to value-conscious Western consumers (core age 40+, US/UK/Germany) through proprietary TV home-shopping channels and its own e-commerce sites, reaching ~127-129 million households (this quarter's filing, PP:L294; PR:L184). The sector's structural pull is the migration of TV-shopping audiences to digital and live/social commerce: management sizes an aggregate platform TAM of ~$20bn against ~$416mn FY26 revenue (this quarter's filing, PP:L919), and cites US video/live-commerce growing toward $68bn by 2026 and a ~41% industry livestream CAGR (this quarter's filing, PP:L873,L1010). The cyclical headwind this quarter is discretionary-spend caution across Western markets plus a Middle-East-conflict disruption early in the quarter (this quarter's filing, PR:L127-129), which is why constant-currency demand was flat. A regulatory wildcard specific to VGL is US import tariffs: the IEEPA leg was ruled unlawful and partly refunded this quarter, but a Section 122 tariff (₹14.26 Cr paid, unbooked) is still contested in US courts (this quarter's filing, R:L219-229) — a live policy risk that can swing either way. Currency is a first-order sector factor: ~90% of revenue is USD/GBP/EUR (this quarter's filing, PP:L769), so rupee moves flatter or flatten reported growth independent of demand. No prior Notion or peer sector work exists for VGL to reconcile against; the above is entirely this quarter's disclosure plus general sector knowledge.

### 3. BUSINESS-MODEL INTELLIGENCE
VGL is vertically integrated: it manufactures/sources jewellery in India, China and the US (5 units, a 1,69,000 sq ft Jaipur factory, ~5mn pieces/year capacity), owns 16 retail brands, and sells direct through owned TV channels and websites with a stated 0% marketplace take-rate on primary channels (this quarter's filing, PP:L315,L718,L472). The money is made by capturing the full margin stack — manufacturer + brand owner + retailer — instead of paying a licensor or a marketplace. Unit economics this quarter: gross margin ~68% (this quarter's filing, PR:L82), operating EBITDA margin 10.5%, PAT margin 6.1%. The margin engine is the in-house-brand mix (57% of B2C, +2,200 bps YoY) which the company says lifts per-unit margin, loyalty and pricing control (this quarter's filing, PR:L90,L139-143). The consolidated entity is where value shows: the Indian parent (standalone) mostly manufactures and earns intragroup income, so ~76% of group profit comes from the overseas retail subsidiaries (this quarter's filing, R:L98 vs L275) — standalone numbers are noisy with intragroup dividends and one-offs and should be ignored for trajectory. Model-drift signals this quarter: (a) the shift from TV toward digital continues (digital 45%, all sites moved to Shopify Enterprise) but TV, still 53% of format mix, is contracting in real terms; (b) Budget Pay — instalment/EMI financing — is now 38% of consumer revenue and is presented as "affordability" with no disclosure of the receivable or default rate (this quarter's filing, PP:L1148, FND-10), an emerging working-capital/credit exposure to watch. The balance sheet is net-cash with no debt and a stated 24% ROCE (this quarter's filing, PP:L1052), though both the net-cash figure and the ROCE base need reconciliation. No prior business-model baseline exists in Notion; all figures here are this quarter's filing.

### 4. COMPETITION INTELLIGENCE
VGL's structural win is being one of very few vertically-integrated, own-brand, own-channel electronic retailers at global scale — it controls manufacturing, brand and distribution, so it keeps margin that importer/marketplace-dependent rivals hand to licensors and platforms (management contrasts VGL ~60% gross margin vs a typical importer ~40%, this quarter's filing, PP:L330-334). Its owned-audience TV+digital reach (~127mn households, 677K active customers, 23 repeat pieces/customer/year, this quarter's filing, PP:L470,L482) is expensive to replicate and gives first-party data for AI-led merchandising. Where it is structurally weaker: it is sub-scale against the broad e-commerce and live-commerce field it points to as its TAM — Shop LC is "under 0.3%" of the US video-commerce market and TJC+Ideal World "a fraction" of the UK base (this quarter's filing, PP:L912) — so it competes on niche value positioning ($5–$1,000, ~35,000 SKUs), not breadth or logistics muscle, against Amazon-scale players and against TV-shopping incumbents (e.g., QVC/HSN-type operators) in the US/UK. The competitive risk to watch: its two European legs (UK, Germany/Europe) turned loss-making this quarter (this quarter's filing, R:L140,L142) while a rival like a scaled marketplace does not carry TV-channel fixed cost — if Western discretionary demand stays soft, VGL's owned-channel fixed-cost base is a disadvantage exactly when volumes fall, which is what the TV volume/ASP decline is already showing. No named-peer financials were passed to this run (first coverage), so peer comparisons here are qualitative and drawn from this quarter's filing plus general sector knowledge; a formal peer set should be built at the Role 2 stage.

---

```yaml
stage: A4-analyst
company: "VAIBHAVGBL"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
docs_merged: [results, presentation]   # results filing + press release + investor deck; NO concall (Role 5 N.A.)
ledger_reconciliation:
  notes: 15
  turns: 0
  slides: 39
  all_reviewed: true
  a3_findings_incorporated: ["A3-01","A3-02","A3-03","A3-04","A3-05","A3-06","A3-07","A3-08","A3-09","F7-01","F8-01","F16-01","F6-01","F14-01","FND-01","FND-02","FND-03","FND-04","FND-05","FND-06","FND-07","FND-08","FND-09","FND-10"]
protocol_verdict: "PROCEED WITH CAVEATS"
cash_conversion: "INDETERMINATE"
decision_status_verified: "NOT YET COVERED / NO POSITION (first-time coverage; framed as initiation, 8A-W)"
position_branch: "8A-W"
sc_gap_pat_pct:
  - {period: "Q1 FY26", value: "+76.0%"}
  - {period: "Q4 FY26", value: "-57.0%"}
  - {period: "Q1 FY27", value: "+76.4%"}
  - {period: "FY26", value: "+3.6%"}
questions_for_management:
  - {q: "Bridge standalone Q4FY26 exceptional + deferred-tax credit to intragroup flows", from_finding_id: "A3-01"}
  - {q: "Constant-currency revenue by segment + FX sensitivity; TV volume/ASP decline", from_finding_id: "F7-01/FND-08"}
  - {q: "Is Q1FY27 PAT one-off-free; normalised FY27 ETR; reconcile QoQ PAT framing", from_finding_id: "F8-01/F16-01/FND-04"}
  - {q: "Quarterly EBITDA path to positive UK/Europe; Germany FY27 profit date", from_finding_id: "A3-07/FND-02/FND-03"}
  - {q: "Section 122 tariff (Rs14.26 Cr) ruling timeline and recognition trigger", from_finding_id: "A3-03/A3-04"}
  - {q: "DTA/carryforward exhaustion timing and steady-state ETR", from_finding_id: "A3-05"}
  - {q: "FX-translation OCI reversal; how much of profit/book value is currency; hedging", from_finding_id: "A3-06"}
  - {q: "Reconcile net cash Rs287/296/387 Cr; explain 4.2% EBITDA-walk base vs 9% margin", from_finding_id: "FND-06/FND-09"}
  - {q: "EY internal-auditor appointment vs EY IR-advisor role; independence; outgoing auditor", from_finding_id: "A3-08"}
  - {q: "Committed ECom KPI to evidence Shopify-migration acceleration next quarter", from_finding_id: "F6-01"}
  - {q: "Name the 4 other-auditor subsidiaries and their growth/margins", from_finding_id: "A3-02"}
  - {q: "Budget Pay (38% of B2C) receivable balance, ageing, charge-off rate", from_finding_id: "FND-10"}
monitorables:
  - {item: "Interim dividend Rs1.50/sh paid (~Rs25 Cr outflow)", implied_date: "2026-09-03", source_ref: "R:L194-196"}
  - {item: "Section 122 tariff Rs14.26 Cr court ruling (unbooked)", implied_date: "US court calendar (undated)", source_ref: "R:L219-229"}
  - {item: "Germany segment profitability contribution", implied_date: "FY27", source_ref: "PP:L1028"}
  - {item: "Europe margins strengthen over the year", implied_date: "FY27", source_ref: "PP:L387-388"}
  - {item: "Shopify migration -> ECom acceleration KPI", implied_date: "Q2-Q3 FY27", source_ref: "PR:L145"}
  - {item: "Digital 50% of B2C (from 45%)", implied_date: "FY27", source_ref: "PP:L1008"}
  - {item: "In-house brands 60%+ of B2C (from 57.2%)", implied_date: "FY27", source_ref: "PP:L1018"}
  - {item: "Revenue Rs5000-5500 Cr", implied_date: "FY30", source_ref: "PP:L1004"}
  - {item: "H1 FY27 cash flow + balance sheet (resolves INDETERMINATE cash conversion)", implied_date: "2026-11 (approx)", source_ref: "Step 5"}
  - {item: "EY internal-audit independence watch", implied_date: "FY27-FY28", source_ref: "R:L42-43"}
  - {item: "Net-cash figure reconciliation (Rs287/296/387 Cr)", implied_date: "next filing", source_ref: "PR:L86 vs PP:L731"}
flags:
  - "ONE_OFF_IN_REVENUE: ~Rs25.59 Cr IEEPA tariff refund booked as operating revenue inflates Q1FY27 revenue/EBITDA/PBT; ex one-off, reported PBT is FLAT YoY (R:L214-215)"
  - "CONSTANT_CURRENCY_FLAT: management concedes CC revenue broadly flat; reported +13% is FX-led (PR:L127)"
  - "QoQ_PAT_REFRAME: reported PAT -38% QoQ; +29% shown uses ex-MAT-credit Q4 base; cleanest QoQ = PBT +10.9% (PR:L91)"
  - "NET_CASH_CONFLICT: Rs287 vs Rs296 vs Rs387 Cr across company's own documents, ~Rs91 Cr / >30% gap (FND-06)"
  - "SEGMENT_LOSSES: UK PBIT -0.47 and Europe(ex-UK) -2.89 swung negative YoY (R:L140,L142)"
  - "TV_STRUCTURAL_DECLINE: TV volume -3.9% and USD ASP -4.4% YoY, masked by +9% INR print (FND-08)"
  - "ETR_STEP_UP_RISK: blended ETR 20.4% vs current-tax 32.4%; FY26 blended 5.6%; deferred-tax-credit dependent (A3-05)"
  - "CASH_CONVERSION_INDETERMINATE: no Q1 cash flow/balance sheet; verdict capped at PROCEED WITH CAVEATS"
  - "GOVERNANCE_OPTICS: EY is both new internal auditor and IR advisor (A3-08); statutory auditor BSR unchanged/clean"
  - "STANDALONE_UNRELIABLE_FOR_TRAJECTORY: S-C PAT gap swings +76%/-57%/+76%/+4% on intragroup one-offs (A3-01)"
  - "BUDGET_PAY_DISCLOSURE_GAP: EMI sales 38% of B2C with no receivable/credit disclosure (FND-10)"
  - "SECTION_122_UNBOOKED: Rs14.26 Cr paid tariff not recognised; binary catalyst (A3-03/04)"
plain_language_brief_included: true
review_path: "/home/user/inflection-pipeline/runs/vaibhavgbl-q1fy27/work/review_vaibhavgbl_q1fy27.md"
```
