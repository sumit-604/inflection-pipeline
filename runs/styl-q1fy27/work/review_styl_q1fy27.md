# Q1 FY27 RESULTS REVIEW — Seshaasai Technologies Ltd (STYL)

Role 4 (Quarterly Results Review Protocol v1.2), merged over the Reg 33 results
filing and the Q1 FY27 investor presentation. **Role 5 (Concall Analysis) is
N.A. this run — no concall transcript was supplied.** The deck's forward claims
are folded into Role 4 as management-narrative signals, flagged deck-sourced
(unaudited).

Reviewer: A4 ANALYST | Model: claude-opus-4-8 | Date: 2026-07-24
Unit convention: filing is INR Million; x0.1 = Rs Cr. All figures below in Rs Cr
unless stated. C = Consolidated, S = Standalone.

---

## 0. LEDGER-RECONCILIATION PREAMBLE (enumeration before interpretation)

**Results filing ledger** (`ledger_results_styl_q1fy27.md`, gate_a2 pass):
12 numbered notes (6 Consolidated p8 + 6 Standalone p12) / 60 statement line
items (32 C + 28 S) / 10 auditor paragraphs (6 C + 4 S) / 5 board-agenda items /
2 consolidation entities / 3 zero-standing rows / 5 signature blocks — **all
reviewed.** No Balance Sheet and no Cash Flow Statement present (A2-confirmed
full-text absence; expected for a Q1 non-annual Reg 33 filing).

**Presentation ledger** (`ledger_presentation_styl_q1fy27.md`, gate_a2 pass):
32 slides (Table 1) + slide-6 granular claims (Table 2, S6-01..S6-12) +
slides 17/18 P&L (Table 3, L1..L11) + slide-31 IPO table (Table 4) — **all
reviewed.**

**Turns: 0.** Role 5 N.A. — no transcript in this run.

**A3 findings incorporated** — results: F1-01, F2-01, F6-01, F7-01, F8-01,
F9-01, F12-01, F14-01, X1, X2, X3, X4. Presentation: F1, F6, F8, F14, F16a,
F16b, F16c, F16d. All A3 forensic findings from both files are carried into
Sections 4–6 below; every AMBIGUOUS / FORWARD-SIGNAL finding produces at least
one Questions-for-Management row (Section 6).

No ledger row is unreviewed. Proceeding to analysis.

**Pre-flight (Step 0):** Units INR Mn → Rs Cr (x0.1). Share count: fresh IPO
issue Sep-2025 lifted implied shares ~147.4M → ~161.8M; Basic = Diluted every
period (3.73/3.73 C; 3.82/3.82 S, lines 485/500, 902/905) — no dilutive spread,
but Q1FY26 EPS (2.50) sits on the pre-IPO share base, so **EPS YoY is not
share-clean** and is read as a secondary metric. Auditor opinion: **unmodified /
unqualified Limited Review**, both C and S; no Emphasis of Matter, no Going
Concern (A3 §3, lines 322-328 / 766-774). Both UDINs NOT FOUND (OCR-illegible,
lines 361/787). Business type: **standard operating business** (Security &
variable-data printing; single statutory segment) — standard Steps 1/5 apply,
not lender variant. Decision Status verified from Notion: **HELD, 4% at Rs 287**
(page ts 2026-06-16) → Step 8A branch.

---

## 1. HEADLINE SCORECARD (Consolidated, Rs Cr; YoY and QoQ)

| Metric | Q1FY26 (C) | Q4FY26 (C) | Q1FY27 (C) | YoY % | QoQ % | Line(s) |
|---|---|---|---|---|---|---|
| Revenue from Operations | 310.87 | 404.18 | 376.47 | **+21.1%** | **-6.9%** | 387 / 511 |
| Gross margin % | 44.5% | 46.9% | 41.7% | **-286 bps** | -527 bps | S6-02/08 (deck 154/175) |
| Reported EBITDA (PBT+D+Fin) | 73.75 | 124.52 | 94.41 | **+28.0%** | -24.2% | 418/407-408/409-410 |
| Reported EBITDA margin % | 23.72% | 30.81% | 25.08% | **+136 bps** | -573 bps | derived |
| **Operating EBITDA (ex-Other Income)** | 71.41 | 118.45 | **87.31** | **+22.3%** | -26.3% | derived (–389) |
| **Operating EBITDA margin %** | 22.97% | 29.31% | **23.19%** | **+22 bps** | -611 bps | derived |
| Other Income | 2.34 | 6.07 | 7.10 | **+203.0%** | +17.0% | 389 / 513 |
| Core PBT ex-Other Income | 52.63 | 105.79 | 74.69 | **+41.9%** | -29.4% | derived |
| Reported PBT | 54.97 | 111.86 | 81.79 | **+48.8%** | -26.9% | 424 |
| PAT (C, post-NCI) | 36.84 | 81.79 | 60.34 | **+63.8%** | -26.2% | 443-444 |
| PAT margin % | 11.85% | 20.24% | 16.03% | +418 bps | -421 bps | derived |
| EPS Basic (not share-clean) | 2.50 | 5.06 | 3.73 | +49.2% | -26.3% | 485/499 |
| **Standalone PAT** | 36.68 | 82.56 | **61.75** | +68.4% | -25.2% | 865 |
| **C-minus-S PAT gap** | **+0.16** | -0.77 | **-1.41** | sign-flip | — | 443-444 / 865 |

**Headline reading (base named, operating vs reported distinguished):**
Revenue **+21.1% YoY** (Q1FY27 376.47 vs Q1FY26 310.87) but **-6.9% QoQ** vs a
seasonally strong Q4FY26. Headline EBITDA margin "expanded" to 25.1% (+136 bps
YoY) but the clean **operating EBITDA margin rose only +22 bps to 23.2%**; the
gap is Other Income (+203% YoY). PAT +63.8% YoY overstates operational
improvement (see Section 3). FY26 revenue base = **Rs 1,441 Cr** (14,411.35 Mn,
line 387/511); the deck slide-10 figure of 15,583 Mn is CONTRADICTED (A3 X1 /
F16a) and is not used.

---

## 2. DATA EXTRACTION TABLE (Step 1, full — every cell a line-anchored number or ND)

### 2a. Consolidated (Rs Cr)

| Line Item | Q1FY26 | Q4FY26 | Q1FY27 | FY26 | Line(s) |
|---|---|---|---|---|---|
| Revenue from Operations | 310.87 | 404.18 | 376.47 | 1,441.14 | 387/511 |
| Other Income | 2.34 | 6.07 | 7.10 | 14.58 | 389/513 |
| Total Income | 313.22 | 410.24 | 383.57 | 1,455.71 | 392 |
| Cost of Materials Consumed | 181.86 | 225.52 | 228.31 | 803.32 | 397-398 |
| Purchases of Stock-in-trade | 1.15 | 1.46 | 0.83 | 5.45 | 399-400 |
| Change in Inventories | -10.54 | -12.45 | -9.51 | -27.23 | 401-402 |
| Employee Benefits Expense | 14.98 | 19.34 | 17.54 | 69.58 | 405-406 |
| Finance Costs | 7.76 | 2.91 | 1.84 | 20.88 | 407-408 |
| Depreciation & Amortisation | 11.02 | 9.75 | 10.78 | 44.22 | 409-410 |
| Other Expenses | 52.01 | 51.88 | 51.98 | 210.50 | 411-412 |
| Total Expenses | 258.24 | 298.40 | 301.78 | 1,126.72 | 415 |
| Profit before exceptional & tax | 54.97 | 111.84 | 81.79 | 329.00 | 418-419 |
| Exceptional items | ND (nil) | 0.02 | ND (nil) | -0.25 | 421-422 |
| Profit Before Tax | 54.97 | 111.86 | 81.79 | 328.74 | 424-425 |
| Tax Expense (total) | 18.14 | 29.99 | 21.50 | 88.93 | 436 |
| PAT pre-NCI | 36.84 | 81.88 | 60.28 | 239.81 | 439-440 |
| NCI share | ND (nil) | -0.09 | 0.05 | 0.20 | 441-442 |
| PAT post-NCI (reported) | 36.84 | 81.79 | 60.34 | 240.01 | 443-444 |
| EPS reported Basic / Diluted (Rs) | 2.50 / 2.50 | 5.06 / 5.06 | 3.73 / 3.73 | 15.45 / 15.45 | 485/499-500 |
| EPS share-adjusted | ND* | ND* | ND* | ND* | — |

*EPS share-adjustment: Q1FY26 EPS rests on the pre-IPO share base; the filing
does not restate it for the fresh issue, so a clean share-adjusted YoY EPS is
**ND** (not estimated). PAT growth, not EPS, is the primary earnings metric.

### 2b. Standalone (Rs Cr)

| Line Item | Q1FY26 | Q4FY26 | Q1FY27 | FY26 | Line(s) |
|---|---|---|---|---|---|
| Revenue from Operations | 310.87 | 404.10 | 376.22 | 1,440.56 | 815 |
| Other Income | 2.30 | 6.03 | 7.09 | 14.46 | 817 |
| Finance Costs | 7.76 | 3.25 | 1.84 | 20.88 | 834 |
| Depreciation & Amortisation | 11.01 | 9.68 | 10.72 | 44.01 | 836 |
| Profit Before Tax | 54.77 | 112.94 | 83.29 | 332.98 | 850 |
| Tax Expense (total) | 18.09 | 30.38 | 21.54 | 89.24 | 861-862 |
| PAT (reported) | 36.68 | 82.56 | 61.75 | 243.74 | 865 |
| EPS Basic / Diluted (Rs) | 2.48 / 2.48 | 5.10 / 5.10 | 3.82 / 3.82 | 15.70 / 15.70 | 902/905 |

### 2c. Derived metrics (Consolidated)

| Derived Metric | Q1FY26 | Q4FY26 | Q1FY27 | FY26 |
|---|---|---|---|---|
| Operating EBITDA (PBT+D+Fin−OI) | 71.41 | 118.45 | 87.31 | 379.26 |
| Operating EBITDA margin | 22.97% | 29.31% | 23.19% | 26.32% |
| Reported EBITDA (PBT+D+Fin) | 73.75 | 124.52 | 94.41 | 393.84 |
| Reported EBITDA margin | 23.72% | 30.81% | 25.08% | 27.33% |
| Gross profit (Rev − net materials) | 138.40 | 190.66 | 156.83 | ND** |
| Gross margin | 44.5% | 46.9% | 41.7% | ND** |
| Core PBT ex-Other Income | 52.63 | 105.79 | 74.69 | 314.16 |
| Other Income / PBT | 4.26% | 5.43% | 8.68% | 4.43% |
| Effective Tax Rate | 33.0% | 26.81% | 26.29% | 27.05% |
| PAT margin on Revenue | 11.85% | 20.24% | 16.03% | 16.65% |

**FY26 gross margin is ND: the FY26 net-materials split is not required for the
quarterly walk and is not independently footable without the annual note;
per-quarter gross margins (deck S6-02/08) are used and are internally consistent
(Q1FY27 156.83 / 376.47 = 41.66% ≈ 41.7%).

---

## 3. QUALITY-OF-EARNINGS — operating vs non-operating (Step 4 PAT bridge)

**Bridge: Reported PAT YoY change +23.50 Cr (36.84 → 60.34), Consolidated:**

| Component | YoY change (Rs Cr) | Recurring? |
|---|---|---|
| Revenue → gross profit at prior GM (Δrev 65.60 × 44.52%) | +29.20 | Recurring |
| Gross-margin change contribution (−286 bps × 376.47) | **−10.77** | Recurring (adverse) |
| Employee cost increase | −2.56 | Recurring |
| Other expenses | +0.03 | Recurring |
| **= Operating EBITDA change** | **+15.90** | **Recurring core** |
| Depreciation change | +0.24 | Recurring |
| Finance cost change (7.76 → 1.84, −76%) | **+5.92** | **NON-repeatable (post debt repay)** |
| Other Income change (2.34 → 7.10, +203%) | **+4.76** | **NON-recurring typically** |
| = PBT change | +26.82 | |
| Tax change (net; embeds ~+5.5 ETR tailwind) | −3.36 | Mixed / non-repeatable tailwind |
| **= Reported PAT change** | **+23.50** | (rounding vs 23.46) |

**Clean vs headline growth — stated explicitly:**
- **Headline PAT +63.8% YoY.** Core operating contribution (Operating EBITDA
  +Dep) = **+16.14 Cr of the +23.50 Cr**, i.e. ~69% of the rupee gain is core;
  BUT the pre-tax picture is flattered further down: **finance cost +5.92 Cr and
  ETR normalisation (~+5.5 Cr embedded in the tax line)** together add roughly
  Rs 11 Cr of non-repeatable uplift, plus **Other Income +4.76 Cr**.
- **Cleanest test — Core operating PBT ex-Other Income grew +41.9%** (52.63 →
  74.69), well below reported PBT +48.8% and PAT +63.8%. The headline growth is
  partly real (operating EBITDA +22.3%) but the **PAT growth rate itself is not
  a clean read** — it is inflated by the finance-cost collapse (IPO debt fully
  repaid, Rs 300 Cr, line 606; tailwind now EXHAUSTED, A3 pres-F1) and by tax
  normalising 33.0% → 26.3% off an abnormally high Q1FY26 tax base (A3 F8-01 /
  pres-F8; current ETR ~110 bps above statutory 25.17%, so little tailwind
  remains).
- **Margin expansion is other-income-driven.** Reported EBITDA margin +136 bps
  YoY; operating EBITDA margin +22 bps. Other Income (+203% YoY) supplies almost
  the entire "expansion" (A3 X2 / pres-F16b). Simultaneously **gross margin fell
  286 bps** (44.5% → 41.7%) on raw-material / West Asia conflict / FX / logistics
  cost, which management flags as ongoing (A3 F7-01, deck lines 511-512).
- **Cash conversion: INDETERMINATE.** No Balance Sheet, no Cash Flow Statement
  in this Q1 filing (A2-confirmed absence). CFO, CFO/PAT, receivable/inventory
  days, net debt, working-capital cycle are all **ND** this quarter. This is a
  named data gap, not a pass — see verdict (Section 8).

---

## 4. FORENSIC FINDINGS CARRIED FROM BOTH A3 FILES (each with implication + cite)

| A3 id (file) | Classification | Finding & implication | Line/slide cite |
|---|---|---|---|
| F1-01 (results) | AMBIGUOUS | Standalone Exceptional nil all 4 periods, but Consolidated carries a subsidiary-origin exceptional (Q4FY26 +0.02, FY26 -0.25 Cr); standing FVTOCI equity-instrument line = equity investment held/anticipated at fair value; restructuring/impairment template stands ready. | 421-422/847/453-454 |
| F2-01 (results) | AMBIGUOUS | **C PAT 60.34 sits Rs 1.41 Cr BELOW S PAT 61.75.** Two subsidiaries net only −0.14 Cr (loss 0.22 + profit 0.08), so ~Rs 1.3 Cr of consolidation eliminations are unexplained; gap **sign-flipped** from +0.16 (Q1FY26 C>S) to −1.41 (Q1FY27 C<S). Consolidated rests on unaudited components. | 443-444/865 |
| F6-01 (results) | FORWARD-SIGNAL | IPO proceeds **Rs 170.1 Cr still unutilised**, incl **Rs 136.1 Cr manufacturing-capex earmark** ("expansion of existing manufacturing units"), only Rs 6.77 Cr deployed this quarter — dateless committed capex / future commissioning window. | 603/998/609 |
| F7-01 (results) | FORWARD-SIGNAL | Newly-added gross-margin hedge in commentary CONFIRMED by numbers: GM −286 bps YoY; management flags margin squeeze as ongoing (geopolitics/fuel/INR) → next-quarter margin risk. | 145-151/175 |
| F8-01 (results) | FORWARD-SIGNAL | PAT +63.8% flattered by ETR 33.0%→26.3% and finance cost −76% post debt repay; both largely non-repeatable; tax tailwind exhausted (ETR ~ statutory). | 424/436/407-408 |
| F9-01 (results) | AMBIGUOUS | Single-quarter actuarial OCI gain (Rs 0.78 Cr C / 0.78 Cr S) **exceeds the entire prior full year** (0.37 C / 0.38 S) → suspected discount-rate/plan-asset assumption change; verify at Annual Report. | 450/543/872 |
| F12-01 (results) | AMBIGUOUS | **Single reportable statutory segment** declared; NO segment assets/liabilities/results/capex disclosed; the 3-vertical split (Payments/CFS/IoT) exists ONLY in the unaudited press release + deck. All segment-level monitoring rests on marketing percentages, not audited data. | 611-612/115-119 |
| F14-01 (results) | NEUTRAL-FACT | Auditor Para 5 cross-refers to a "paragraph 7" that carries no numeral; two P&L rows both labelled "7."; single-segment note vs 3-vertical PR — cumulatively a drafting/governance data point. | 323/343-349/440-444 |
| X1 (results) | CONFIRMATORY-NEG | FY26 revenue base = Rs 1,441 Cr; deck slide-10 15,583 Mn CONTRADICTED, slide-16 / Notion base CONFIRMED. Q1 YoY +21.1% confirmed. | 387/511 |
| X2 (results) | FORWARD-SIGNAL | Headline EBITDA margin 25.1% is ~entirely Other-Income-driven (+203% YoY); operating EBITDA only 23.2% (+22 bps). EBITDA is a derived figure, not a disclosed line. | 389/418 |
| X3 (results) | CONFIRMATORY-NEG | PBT +48.8%, ETR 33.0%→26.3%, PAT +63.8% all confirmed both C and S; finance-cost deleveraging an added non-operating flatterer. | 418/424/436 |
| X4 (results) | AMBIGUOUS | Filing carries NO statutory segment data; IoT Rs 67.4 Cr reconcilable to PR 18% but unaudited; Payments "decline"/QoQ trajectory cannot be confirmed or refuted from the filing. | 611-612/119 |
| pres-F1 | NEUTRAL-FACT | IPO debt-repayment tranche (Rs 300 Cr) 100% deployed; finance-cost tailwind (−76% YoY) now **exhausted** — will not repeat in FY28 comparisons. | slide 31, line 935 |
| pres-F6 | FORWARD-SIGNAL | Europe/Africa payment-card exports **commenced** Q1FY27; **3 multi-year tenders won** (1 Payments, 2 CFS from PSU banks); largest-retailer RFID "ramped up and stabilized" → forward backlog. | slides 12-14, 330/332/367/397 |
| pres-F8 | AMBIGUOUS | Deck admits Q1FY26 low margin was "higher tax provisioning"; PAT +63.8% flattered by tax normalisation; underlying PBT +48.8%; ETR still ~110 bps above statutory. | slides 17/18, 529-532 |
| pres-F14 | NEUTRAL-FACT | Operating EBITDA printed as Rs 873.1 mn (YoY block) vs Rs 873.13 mn (QoQ block); "OPERTATING" typo; "51.17" precision outlier — governance hygiene, immaterial; exact Operating-EBITDA reconciles to filing derivation (87.3 Cr). | lines 163/185/555 |
| pres-F16a | AMBIGUOUS | Slide-10 FY revenue chart ASCENDS to FY26 peak 15,583, but slide-16 stack + Notion FY26 base (Rs 1,441 Cr) DESCEND — either reversed year labels dressing flat-to-declining 3-yr revenue as growth, or a column-alignment artifact. Slide-16/Notion base is the one confirmed by the filing. | slide 10 vs 16, 299-308/466-478 |
| pres-F16b | FORWARD-SIGNAL | Headline EBITDA margin +135 bps is other-income driven (OI +203%); clean operating margin +22 bps to 23.2%; numerator mixes other income against a revenue-from-ops denominator. Other-income sustainability is a live question. | 154/164/509 |
| pres-F16c | AMBIGUOUS | Under a "Gross Margin (%)" header the deck prints "YOY +13.3%", which is gross-PROFIT rupee growth; actual gross MARGIN FELL 286 bps YoY / 527 bps QoQ — label invites reading a deteriorating margin as improving. | slide 15, 435-438 vs 154 |
| pres-F16d | FORWARD-SIGNAL | The −6.9% QoQ revenue / −573 bps QoQ margin drop is pre-framed as Q4 seasonality ("Q4 historically strongest"); implies structurally soft H1FY27 and a low internal bar. Verify against the FY26 quarterly path. | slide 18, line 550 |

---

## 5. FTTCP MONITORING-TRIGGER SCORECARD (all 15) — FLAG only, operator decides

Status set: **FIRED FAVOURABLY / BREACHED / SILENT / PARTIAL / N.A.** Each with
the reconciled number and cite. STYL is a HELD position; these are the
pre-committed Q1 FY27 decision-gate triggers.

| # | Trigger | Reconciled reading | Status | Cite |
|---|---|---|---|---|
| 1 | Revenue YoY > +10% | +21.1% (376.47 vs 310.87) | **FIRED FAVOURABLY** | 387/511 |
| 2 | EBITDA margin sustain > 27% | Reported 25.1%, Operating 23.2% — both < 27% | **BREACHED** | derived 418/407-410/389 |
| 3 | IoT revenue > Rs 55 Cr | Rs 67.4 Cr (674 Mn, +144% YoY) — **deck/PR only, NOT a statutory segment** | **FIRED FAVOURABLY (unaudited)** | slide 14 l.395 / PR l.119; caveat Note 3 l.611 |
| 4 | SIM utilization disclosure > 40% | Not disclosed ("volumes continue to build up") | **SILENT** | 404-405 |
| 5 | Inventory days < 80 | No Balance Sheet in filing | **SILENT** | A2 absence / deck 516 |
| 6 | Receivable days stable or < 80 | No Balance Sheet in filing | **SILENT** | A2 absence |
| 7 | FY27 guidance provided (specific rev/margin) | No numeric guidance; only qualitative "sustaining growth momentum"; disclaimer disclaims obligation to update | **SILENT / ABSENT (gate criterion UNMET)** | 163 / deck 114 |
| 8 | eSIM commercial launch (first rev or Q2FY27 date) | Only "eSIM has cross-industry potential"; no date, no revenue | **SILENT** | deck 421 |
| 9 | Reliance Retail RFID volume disclosed | "one of the largest Indian retailer ramped up and stabilized" — unnamed, no volume/Rs | **PARTIAL** | deck 397 |
| 10 | Promoter lock-in — no OFS within 60 days of Sep 30 2026 | No shareholding pattern in filing/deck; lock-in expiry still pending | **SILENT** | — |
| 11 | Promoter pledge stays 0% | No pledge event disclosed anywhere; no shareholding pattern in filing | **SILENT (no pledge event → hard-kill NOT triggered)** | — |
| 12 | Receivables factoring facility announced | Not mentioned; finance-cost fall attributed to debt reduction, not factoring | **SILENT** | 181 |
| 13 | Gautam Jain substantive concall participation | No transcript this run (Role 5 N.A.); named Whole-time Director in deck | **N.A.** | deck slide 28 l.840 |
| 14 | Payments QoQ — no 2 consecutive declines | Payments 1,984 (Q3) → 1,919 (Q4) → 1,582 (Q1FY27) = **TWO consecutive QoQ declines**; Payments only +5.6% YoY, the laggard | **BREACHED** (ORDER_INFERRED caveat) | slide 12 l.325 |
| 15 | Cash-transition WC initiative addressed | Only generic "supply-chain agility / strategic inventory management / strengthen cash flows"; no named WC program or metric | **PARTIAL / SILENT** | 185-187 / deck 515-516 |

**Tally:** FIRED FAVOURABLY 2 (one, #3, is unaudited PR/deck-sourced) ·
BREACHED 2 (#2, #14) · PARTIAL 2 (#9, #15) · SILENT 8 (#4,5,6,7,8,10,11,12) ·
N.A. 1 (#13).

**Re-engagement rule FLAG:** 5+ triggers firing favourably → upgrade to BUY
4-5% Medium, Tranche 2. **Only 2 fired favourably (one unaudited). Rule NOT met
— no upgrade signal.**

**Hard-kill rule FLAG:** trim 50% if (a) Trigger 11 pledge fires, OR (b) 3+ of
triggers 8/14 fire negatively. (a) **Pledge did NOT fire** — no pledge event
disclosed. (b) Under the strict "fire negatively" reading only **#14 is an
unambiguous negative**; #2 is a clear margin breach and #8 is a gate-relevant
silence, but the remaining items are non-disclosures, not confirmed negatives —
so the **3+ threshold is NOT mechanically met.** However, the cluster (2 hard
breaches + 4 thesis-critical silences at the pre-committed gate) is flagged for
operator attention. **Decision left to operator; A4 does not change Decision
Status.**

**Pre-committed "next decision gate" (Notion) — 4 criteria:**
- IoT > Rs 55 Cr: **MET** (Rs 67.4 Cr, unaudited).
- EBITDA > 26%: **NOT MET** (25.1% reported / 23.2% operating).
- Payments YoY stable: **MARGINAL** (+5.6% YoY positive, but two consecutive
  QoQ declines and mix share falling ~48% → 42%).
- FY27 guidance provided: **NOT MET** (no numeric guidance).
→ **1 of 4 clearly met; 2 failed; 1 marginal.** Flagged for the operator's gate
decision.

**Thesis-broken conditions (any 2 of 5) — status:** PAT margin < 14% for two
quarters → NOT breached (16.0% this quarter). Promoter pledge initiated → NOT
fired. CFO/PAT < 0.5x for 2 years → **INDETERMINATE** (no cash flow this
quarter). eSIM slips beyond Q2 FY28 → NOT yet (no date given; at risk). Receivable
days > 110 → **INDETERMINATE** (no Balance Sheet). **No thesis-broken condition
has FIRED.**

---

## 6. QUESTIONS FOR MANAGEMENT (IR email — no concall transcript this run)

Every A3 FORWARD-SIGNAL / AMBIGUOUS finding from both files generates ≥1 row,
plus the deck's thesis-critical silences. Ordered by materiality to thesis.

| # | Question (references a Q1FY27 number/disclosure) | From finding | Why it matters | Bull answer | Bear answer |
|---|---|---|---|---|---|
| 1 | Reported EBITDA margin was 25.1% and operating EBITDA margin 23.2% — both below your >27% gate. What specific gross-margin recovery (vs the 286 bps YoY / 527 bps QoQ decline to 41.7%) do you expect in H2FY27, and by when do you regain 27% EBITDA? | F7-01, X2, pres-F16b/c | Margin is the failed gate criterion | Named input-cost pass-through / mix path back to 27% | "Cost pressure persists"; no timeline |
| 2 | Please provide specific FY27 revenue and EBITDA-margin guidance. The deck and filing give none at what you flagged as a decision quarter. | Trigger 7 silence, pres-F16a | A decision-gate criterion, unmet | Concrete numeric range | Refusal / "no guidance policy" |
| 3 | Payment Solutions revenue fell two consecutive quarters (1,984 → 1,919 → 1,582 Mn) and its mix share dropped ~48% → 42%. Is this order timing or structural share loss (top-10 concentration 81.4% → 73%)? What is the Q2FY27 Payments run-rate? | Trigger 14 breach, pres-F6 | Payments is ~42% of revenue and the laggard | Confirmed order-timing, backlog cover | Structural erosion, client losses |
| 4 | PAT grew 63.8% but finance cost fell 76% (IPO debt fully repaid) and ETR normalised 33.0% → 26.3%. With both tailwinds exhausted, what YoY PAT growth is repeatable on core operations? | F8-01, pres-F8, pres-F1, X3 | Tests durability of the earnings headline | Core-driven growth path | Growth was one-off-led |
| 5 | Other Income rose 203% YoY to Rs 7.1 Cr and supplied nearly all headline margin expansion. What is the source (treasury on IPO cash?) and is it recurring at this magnitude? | X2, pres-F16b | Distinguishes core vs treasury margin | Recurring, structural | One-off treasury timing |
| 6 | Consolidated PAT (Rs 60.34 Cr) is Rs 1.41 Cr BELOW standalone (Rs 61.75 Cr), a sign-flip from last year; the two subsidiaries net only −Rs 0.14 Cr, leaving ~Rs 1.3 Cr of unexplained eliminations. Please explain the consolidation adjustment. | F2-01 | Consolidated rests on unaudited components | Clear intragroup explanation | Evasive; opaque eliminations |
| 7 | Rs 136.1 Cr of the IPO manufacturing-capex earmark is unutilised (only Rs 6.77 Cr deployed this quarter) with no stated timeline. What is the deployment schedule and expected commissioning date for the capacity expansion? | F6-01 | Dateless committed capex = future absorption | Firm schedule + commissioning date | Indefinite; capital idle |
| 8 | When does eSIM commercially launch — first revenue or a specific Q2FY27 date? The deck cites only "cross-industry potential." (eSIM has already slipped ~9 months.) | Trigger 8 silence | Named thesis catalyst; slippage risk | Committed date / first revenue | Further slippage past Q2FY28 |
| 9 | SIM utilization: what is the current rate versus the ~30% prior reading? The deck says only "volumes continue to build up." | Trigger 4 silence | Capacity-absorption evidence for IoT | > 40% disclosed | No number given |
| 10 | Please quantify the "largest Indian retailer" RFID volume (the Reliance-Retail candidate) that "ramped up and stabilized" — retailer name and Rs / volume. | Trigger 9 partial, pres-F6 | Concentration / anchor-customer thesis | Named + sized | Unnamed, unquantified |
| 11 | No Balance Sheet or Cash Flow was filed this quarter. What were receivable days, inventory days and net cash at 30-Jun-2026, and did the "cash-transition" working-capital initiative move any metric? | Triggers 5/6/15 silence | Cash conversion is INDETERMINATE | Days improving; net cash held | Refusal; WC deteriorating |
| 12 | The three multi-year tenders won this quarter (1 Payments, 2 PSU-bank CFS) and the newly-commenced Europe/Africa card exports — what is the FY27 revenue contribution and start timing of each? | pres-F6 | Forward backlog quantification | Sized, dated | Vague, undated |
| 13 | The single-quarter actuarial OCI gain (Rs 0.78 Cr) exceeds the entire prior full year. Was there a change in the discount rate or plan-asset assumptions this quarter? | F9-01 | Assumption change flag | Routine re-measurement | Undisclosed assumption change |
| 14 | Slide 10 shows FY revenue rising to a FY26 peak of 15,583 Mn, but the filing and slide 16 put FY26 at 14,411 Mn (Rs 1,441 Cr). Which is correct, and is 3-year revenue actually flat-to-declining? | pres-F16a, X1 | Deck-vs-filing base contradiction | Labelling error, filing correct | Revenue flat/declining, dressed up |
| 15 | Was any receivables-factoring facility entered this year? The 76% finance-cost fall is attributed to debt repayment, not factoring — please confirm. | Trigger 12 silence | Rules out disguised WC financing | No factoring; clean deleverage | Undisclosed factoring |
| 16 | With promoter lock-in expiring 30-Sep-2026, is any OFS or promoter sale contemplated within 60 days, and does pledge remain 0%? | Triggers 10/11 silence | Hard-kill / supply-overhang watch | No OFS, 0% pledge affirmed | OFS planned / pledge |

**Top 3 by likelihood of thesis-changing information:**
1. Q3 (Payments trajectory) — a structural-erosion answer materially raises Bear
   probability; ~42% of revenue.
2. Q4 (repeatable PAT growth ex tailwinds) — confirms whether the 63.8% headline
   is durable; would confirm Bull if core-led.
3. Q2 (FY27 guidance) — refusal at a self-declared decision quarter is itself a
   transparency signal.

**Channel:** No concall transcript supplied to this run. Submit all 16 verbatim
via IR email; prioritise Q1-Q5 for any live Q&A if a call is scheduled within
two weeks (a call was flagged in the deck cover letter, lines 15-25).

---

## 7. MONITORABLES & CATALYSTS (seeded by A3 commitment registers F6)

| Item | Implied date | Source ref | Status word |
|---|---|---|---|
| Deploy Rs 136.1 Cr IPO manufacturing-capex earmark (expansion of existing units) — watch PPE jump / commissioning | none stated | Note 2 Table B, l.603/998 | underway (Rs 6.77 Cr deployed this qtr) |
| Deploy Rs 32.1 Cr IPO general-corporate earmark | none stated | Note 2 Table B, l.608/1002 | underway (Rs 13.73 Cr this qtr) |
| Rs 300 Cr IPO debt repayment | delivered | Note 2 Table B, l.606/1000 | completed (tailwind exhausted) |
| Europe/Africa payment-card exports — revenue contribution | commenced Q1FY27 | deck slide 12, l.332 | commenced |
| 3 multi-year tenders (1 Payments, 2 CFS PSU banks) — execution/revenue | won Q1FY27 | deck slides 12-13, l.330/367 | won |
| Largest-retailer (Reliance candidate) RFID volume — quantification | Q1FY27 | deck slide 14, l.397 | "stabilized" (unquantified) |
| SIM volume / utilization build | undated | deck slide 14, l.404-405 | building |
| eSIM commercial launch date / first revenue | slipped; watch vs Q2FY28 | deck l.421 | pending (no date) |
| Promoter lock-in expiry — OFS watch (60-day window) | 30-Sep-2026 | Notion thesis | pending |
| Annual Report — verify actuarial assumption change (F9) & FVTOCI equity line (F1) | FY27 AR | l.450/453-454 | to verify |
| Q2FY27 half-yearly filing — Balance Sheet + Cash Flow mandatory (resolves cash-conversion INDETERMINATE, receivable/inventory days) | Q2FY27 (Reg 33 H1) | protocol Step 5 | awaited |

---

## 8. PROTOCOL VERDICT (v1.2 verdict set)

**VERDICT: PROCEED WITH FLAGS.**

Reasons:
- The numbers are reliable to rely on: unmodified/unqualified Limited Review
  opinion both C and S; no Emphasis of Matter, no Going Concern; A2 ledger
  reconciled 100%; gate_a2 and gate_a3 both pass. Company quality never halts a
  run — flags propagate, the operator decides (per CLAUDE.md and protocol).
- FLAGS surfaced and carried to the operator: (1) **EBITDA margin breach** —
  25.1% reported / 23.2% operating, both below the 27% trigger (#2); (2)
  **Payments two consecutive QoQ declines** (#14); (3) **earnings quality** —
  PAT +63.8% is materially flattered by a non-repeatable finance-cost collapse,
  ETR normalisation, and +203% Other Income, with core operating PBT ex-OI up
  only +41.9% and operating margin up only +22 bps; (4) **gross margin −286 bps**
  flagged as ongoing pressure; (5) **segment data is unaudited** — single
  statutory segment; IoT/Payments splits exist only in the press release/deck;
  (6) **C-minus-S PAT gap sign-flipped** to −Rs 1.41 Cr with ~Rs 1.3 Cr
  unexplained eliminations, consolidated resting on unaudited components; (7)
  **four thesis-critical silences at a self-declared decision gate** — FY27
  guidance, eSIM date, SIM utilization, and both working-capital-days metrics.
- **Cash conversion is INDETERMINATE** — no Balance Sheet and no Cash Flow in
  this Q1 filing. Missing evidence named: CFO, CFO/PAT ratio, receivable days,
  inventory days, payable days, cash-conversion cycle, net debt/net cash. Per
  house rule this INDETERMINATE reading independently caps at PROCEED WITH
  CAVEATS with the evidence named; that cap is **subsumed by the more severe
  PROCEED WITH FLAGS** here (the binding constraint is the cluster of quality and
  monitoring flags, not the data gap alone). The gap resolves at the Q2FY27
  half-yearly filing (Reg 33 mandates H1 Balance Sheet + Cash Flow).
- **Decision Status is UNCHANGED — HELD, 4% at Rs 287.** No thesis-broken
  condition has fired; the re-engagement rule (5+ favourable) is not met; the
  hard-kill rule is not mechanically met (no pledge; only #14 an unambiguous
  negative). The pre-committed decision gate scored 1 of 4 criteria clearly met.
  A4 flags; the operator decides on the gate and on any trim/hold/upgrade.

**Position branch:** 8A (HELD). **Decision Status verified:** HELD (Notion page
ts 2026-06-16). **Cash conversion:** INDETERMINATE. **Single cleanest metric for
Q2FY27:** *Core operating PBT ex-Other Income* (bull: > Rs 80 Cr with gross
margin recovering toward 44%; bear: < Rs 70 Cr with gross margin still < 42%) —
it strips the treasury, tax and finance-cost noise that dominated this quarter's
headline.

---

*Reviewed 2026-07-24 | Sources: results_styl_q1fy27.pdf (Reg 33, 12 pp) +
Investor Presentation Q1FY27 (32 slides) | Role 5 N.A. (no concall transcript).*

```yaml
stage: A4-analyst
company: "STYL"
quarter: "q1fy27"
model: claude-opus-4-8
status: complete
docs_merged: [results, presentation]
ledger_reconciliation:
  notes: 12
  turns: 0
  slides: 32
  all_reviewed: true
  a3_findings_incorporated: [F1-01, F2-01, F6-01, F7-01, F8-01, F9-01, F12-01, F14-01, X1, X2, X3, X4, pres-F1, pres-F6, pres-F8, pres-F14, pres-F16a, pres-F16b, pres-F16c, pres-F16d]
protocol_verdict: "PROCEED WITH FLAGS"
cash_conversion: "INDETERMINATE"
decision_status_verified: "HELD 4% at Rs 287 (Notion page ts 2026-06-16)"
position_branch: "8A"
sc_gap_pat_pct:
  - {period: "Q1FY27", c_pat_cr: 60.34, s_pat_cr: 61.75, gap_cr: -1.41, gap_pct_of_standalone: -2.28}
  - {period: "Q1FY26", c_pat_cr: 36.84, s_pat_cr: 36.68, gap_cr: 0.16, gap_pct_of_standalone: 0.44}
  - {period: "FY26", c_pat_cr: 240.01, s_pat_cr: 243.74, gap_cr: -3.73, gap_pct_of_standalone: -1.53}
questions_for_management:
  - {q: "Path and timeline back to >27% EBITDA / gross-margin recovery from 41.7%", from_finding_id: "F7-01/X2/pres-F16b"}
  - {q: "Specific FY27 revenue and EBITDA-margin guidance", from_finding_id: "trigger7/pres-F16a"}
  - {q: "Payments two consecutive QoQ declines — order timing or structural share loss; Q2 run-rate", from_finding_id: "trigger14/pres-F6"}
  - {q: "Repeatable PAT growth ex finance-cost and ETR tailwinds", from_finding_id: "F8-01/pres-F8/pres-F1/X3"}
  - {q: "Other Income +203% source and recurrence", from_finding_id: "X2/pres-F16b"}
  - {q: "C-minus-S PAT sign-flip; ~Rs 1.3 Cr unexplained consolidation eliminations", from_finding_id: "F2-01"}
  - {q: "Rs 136.1 Cr manufacturing-capex deployment schedule and commissioning date", from_finding_id: "F6-01"}
  - {q: "eSIM commercial launch date / first revenue", from_finding_id: "trigger8"}
  - {q: "SIM utilization rate vs prior ~30%", from_finding_id: "trigger4"}
  - {q: "Largest-retailer RFID volume — name and size", from_finding_id: "trigger9/pres-F6"}
  - {q: "Receivable/inventory days and net cash at 30-Jun-2026; WC initiative effect", from_finding_id: "triggers5/6/15"}
  - {q: "FY27 revenue contribution and timing of 3 tenders + Europe/Africa exports", from_finding_id: "pres-F6"}
  - {q: "Actuarial OCI gain exceeding full prior year — assumption change?", from_finding_id: "F9-01"}
  - {q: "Slide-10 FY26 15,583 vs filing 14,411 — is 3-yr revenue flat/declining?", from_finding_id: "pres-F16a/X1"}
  - {q: "Any receivables-factoring facility this year?", from_finding_id: "trigger12"}
  - {q: "Lock-in expiry 30-Sep-2026 — OFS within 60 days; pledge 0%?", from_finding_id: "triggers10/11"}
monitorables:
  - {item: "Deploy Rs 136.1 Cr IPO manufacturing-capex earmark; watch PPE/commissioning", implied_date: "none stated", source_ref: "Note 2 l.603/998"}
  - {item: "Deploy Rs 32.1 Cr IPO general-corporate earmark", implied_date: "none stated", source_ref: "Note 2 l.608/1002"}
  - {item: "Europe/Africa card exports revenue contribution", implied_date: "commenced Q1FY27", source_ref: "deck slide 12 l.332"}
  - {item: "3 multi-year tenders execution (1 Payments, 2 CFS PSU banks)", implied_date: "won Q1FY27", source_ref: "deck l.330/367"}
  - {item: "Largest-retailer RFID volume quantification", implied_date: "Q1FY27", source_ref: "deck slide 14 l.397"}
  - {item: "eSIM commercial launch date vs Q2FY28 tripwire", implied_date: "pending", source_ref: "deck l.421"}
  - {item: "Promoter lock-in expiry OFS watch (60-day window)", implied_date: "2026-09-30", source_ref: "Notion thesis"}
  - {item: "Q2FY27 half-yearly Balance Sheet + Cash Flow (resolves cash-conversion INDETERMINATE)", implied_date: "Q2FY27", source_ref: "Reg 33 H1 / protocol Step 5"}
  - {item: "Annual Report — verify actuarial assumption change and FVTOCI equity line", implied_date: "FY27 AR", source_ref: "l.450/453-454"}
flags:
  - "EBITDA margin BREACH: 25.1% reported / 23.2% operating, both < 27% trigger (#2)"
  - "Payments two consecutive QoQ declines (#14): 1,984 -> 1,919 -> 1,582 Mn"
  - "PAT +63.8% flattered by non-repeatable finance-cost collapse + ETR normalisation + Other Income +203%; core PBT ex-OI only +41.9%"
  - "Gross margin -286 bps YoY (44.5% -> 41.7%), flagged ongoing"
  - "Segment data unaudited: single statutory segment; IoT/Payments only in press release/deck"
  - "C-minus-S PAT sign-flip to -Rs 1.41 Cr; ~Rs 1.3 Cr unexplained eliminations; consolidated on unaudited components"
  - "Decision-gate silences: FY27 guidance, eSIM date, SIM utilization, WC days all SILENT at self-declared gate"
  - "Cash conversion INDETERMINATE: no Balance Sheet / Cash Flow this quarter"
  - "Re-engagement rule NOT met (2 favourable, one unaudited); hard-kill NOT mechanically met (no pledge); pre-committed gate 1 of 4 met"
  - "Decision Status UNCHANGED (HELD); no thesis-broken condition fired; operator decides"
review_path: "/home/user/inflection-pipeline/runs/styl-q1fy27/work/review_styl_q1fy27.md"
```
