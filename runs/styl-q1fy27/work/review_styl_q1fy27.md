# Q1 FY27 COMPLETE QUARTERLY REVIEW — Seshaasai Technologies Ltd (STYL)

Role 4 (Quarterly Results Review Protocol v1.2) merged over the Reg 33 results
filing and the Q1 FY27 investor presentation, **now UPGRADED with Role 5
(Quarterly Concall Analysis Protocol v1.1) over the Q1 FY27 earnings-call
transcript**. Role 4 numbers, tables and the three A5 fixes below are PRESERVED
verbatim; Role 5 (concall) analysis is ADDED; the monitoring-trigger scorecard,
the decision-gate scoring and the Questions-for-Management are RE-SCORED with the
concall; the verdict is RE-STATED.

Reviewer: A4 ANALYST | Model: claude-opus-4-8 | Upgrade date: 2026-07-25
(base Role 4 dated 2026-07-24). Unit convention: filing is INR Million; x0.1 =
Rs Cr. Concall is already in Rs Cr (x1). All figures below in Rs Cr unless
stated. C = Consolidated, S = Standalone.

*Revision note (A5 gate, preserved): three bounded fixes applied — ARI-1 (Q4FY26
gross profit digit slip 190.66 → 189.65), BEAR-1 (PAT margin 16.0% vs FY26 16.7%
benchmark added), COV-1 (net cash ~Rs 369 Cr disclosed, unaudited; cash
CONVERSION still INDETERMINATE). Verdict, cash-conversion cap and Decision
Status unchanged by those fixes.*

*Upgrade note (Role 5 activation): concall transcript arrived after the A5-verified
Role 4 pass. This document adds Section 5 (Role 5 concall analysis) and the
concall forensic findings A3-01..A3-15, and re-runs Sections 6 (triggers), 7
(questions), 8 (monitorables) and 9 (verdict). Role 4 Sections 1–4 are unchanged.*

---

## 0. LEDGER-RECONCILIATION PREAMBLE (enumeration before interpretation) — UPDATED FOR CONCALL

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

**Concall ledger** (`ledger_concall_styl_q1fy27.md`, gate_a2 pass): **58 speaker
turns / 19 questions / 7 analyst firms / 59 management numbers** (plus 13
participants, 18 forward/hedge phrases) — **all reviewed.** Line coverage 100%
(89 source lines, ASR-normalised transcript; numbers preserved verbatim). A2
flags MGMT_ABSENCE (Gautam Jain, WTD, silent) and REPEAT_QUESTION (margin ask
pressed by three analysts) both carried and resolved below. **Role 5 is now
ACTIVE.**

**A3 findings incorporated** — results: F1-01, F2-01, F6-01, F7-01, F8-01,
F9-01, F12-01, F14-01, X1, X2, X3, X4. Presentation: F1, F6, F8, F14, F16a,
F16b, F16c, F16d. **Concall: A3-01, A3-02, A3-03, A3-04, A3-05, A3-06, A3-07,
A3-08, A3-09, A3-10, A3-11, A3-12, A3-13, A3-14, A3-15.** All A3 forensic
findings from all THREE files are carried into Sections 4–7 below; every
AMBIGUOUS / FORWARD-SIGNAL finding produces at least one Questions-for-Management
row (Section 7).

No ledger row is unreviewed across any of the three documents. Proceeding to
analysis.

**Pre-flight (Step 0):** Units INR Mn → Rs Cr (x0.1); concall already Rs Cr.
Share count: fresh IPO issue Sep-2025 lifted implied shares ~147.4M → ~161.8M;
Basic = Diluted every period (3.73/3.73 C; 3.82/3.82 S, lines 485/500, 902/905) —
no dilutive spread, but Q1FY26 EPS (2.50) sits on the pre-IPO share base, so **EPS
YoY is not share-clean** and is read as a secondary metric. Auditor opinion:
**unmodified / unqualified Limited Review**, both C and S; no Emphasis of Matter,
no Going Concern (A3 §3, lines 322-328 / 766-774). Both UDINs NOT FOUND
(OCR-illegible, lines 361/787). Business type: **standard operating business**
(Security & variable-data printing; single statutory segment) — standard Steps
1/5 apply, not lender variant; Role 5 uses the Step 2 (not Step 2L) guidance set.
Decision Status verified from Notion: **HELD, 4% at Rs 287** (page ts
2026-06-16) → Step 8A branch.

---

## 1. HEADLINE SCORECARD (Consolidated, Rs Cr; YoY and QoQ)  [ROLE 4 — unchanged]

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
F16a) and is not used. **Concall cross-check (Role 5):** CFO restated all
headline figures verbatim on the call — Rs 377 Cr revenue, +21.1% YoY, -6.9%
QoQ, gross profit Rs 157 Cr, GM 41.7% vs 44.5%, EBITDA Rs 94 Cr / 25.1% (+135
bps), PBT Rs 82 Cr (+48.8%), PAT Rs 60 Cr / 16% (+418 bps) (concall L26). The
concall numbers CONFIRM the filing; no narrative-vs-filing numeric conflict.

---

## 2. DATA EXTRACTION TABLE (Step 1, full)  [ROLE 4 — unchanged]

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
| Gross profit (Rev − net materials) | 138.40 | 189.65 | 156.83 | ND** |
| Gross margin | 44.5% | 46.9% | 41.7% | ND** |
| Core PBT ex-Other Income | 52.63 | 105.79 | 74.69 | 314.16 |
| Other Income / PBT | 4.26% | 5.43% | 8.68% | 4.43% |
| Effective Tax Rate | 33.0% | 26.81% | 26.29% | 27.05% |
| PAT margin on Revenue | 11.85% | 20.24% | 16.03% | 16.65% |

**FY26 gross margin is ND: the FY26 net-materials split is not required for the
quarterly walk and is not independently footable without the annual note;
per-quarter gross margins (deck S6-02/08) are used and are internally consistent
(Q1FY27 156.83 / 376.47 = 41.66% ≈ 41.7%). Concall corroborates: CFO cited gross
profit Rs 157 Cr and GM 41.7% (L26), and gave COMC 58.34% vs FY26 average 54.23%
(+411 bps, L26) — a fresh disclosure consistent with the derived gross-margin
decline.

*(ARI-1 corrected) Q4FY26 gross profit = Revenue 404.18 − net materials 214.53 =
**189.65 Cr** (prior draft printed 190.66, a digit slip); the deck independently
prints 1,897 Mn = 189.7 Cr (presentation extract L445). Derived Q4FY26 gross
margin 46.9% is unchanged and correct.*

---

## 3. QUALITY-OF-EARNINGS — operating vs non-operating (Step 4 PAT bridge)  [ROLE 4 — unchanged, concall corroboration noted]

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
  a clean read** — inflated by the finance-cost collapse (IPO debt fully repaid,
  Rs 300 Cr, line 606; tailwind now EXHAUSTED, A3 pres-F1; concall confirms IPO
  proceeds deployment L26) and by tax normalising 33.0% → 26.3% off an abnormally
  high Q1FY26 tax base (A3 F8-01 / pres-F8; current ETR ~110 bps above statutory
  25.17%). **Concall corroboration:** CFO attributes the PBT jump to "operating
  growth and a substantial reduction in the finance cost" (L26) — management's
  own words confirm the finance-cost flatterer.
- **Surviving bear counter — margin against management's own benchmark (BEAR-1).**
  Despite the +63.8% PAT headline, **Q1FY27 PAT margin of 16.0% is BELOW the FY26
  full-year 16.7%** management cites (presentation extract L529-532; matches
  derived FY26 PAT margin 16.65% Section 2c; concall CFO cited "16%," L26). On
  management's own yardstick, per-rupee profitability went backwards YoY-into-FY27.
- **Margin expansion is other-income-driven.** Reported EBITDA margin +136 bps
  YoY; operating EBITDA margin +22 bps. Other Income (+203% YoY) supplies almost
  the entire "expansion" (A3 X2 / pres-F16b). Gross margin fell 286 bps (44.5% →
  41.7%) on raw-material / West Asia conflict / FX / logistics cost, flagged as
  ongoing (A3 F7-01, deck 511-512). **Concall deepens this:** CMD attributes
  "40% to 45% of the [gross-margin] impact directly to currency," the remainder
  to war-driven commodity/freight (L37), and confirms the pressure is live
  (A3-15, chip prices flat YoY but "more than offset by the dollar impact," L80).
- **Cash position disclosed (unaudited); cash CONVERSION INDETERMINATE (COV-1) —
  and now AGGRAVATED by a confirmed inventory build (A3-13).** No Balance Sheet
  and no Cash Flow Statement in this Q1 filing (A2-confirmed absence), so **CFO,
  CFO/PAT, receivable days, inventory days, payable days and the cash-conversion
  cycle are all ND** this quarter. Net cash is **NOT ND**: deck and concall both
  disclose cash & equivalents of **~Rs 369 Cr at 30-Jun-2026** (deck L950-951,
  incl ~Rs 170 Cr unutilised IPO; concall CFO Rs 369 Cr, L26). With the Rs 300 Cr
  IPO debt tranche fully repaid (line 606), gross cash ≈ net cash, broadly
  consistent with — and slightly above — the Notion FY26 base of Rs 339 Cr net
  cash. The cash-CONVERSION quality (CFO/PAT vs the Pillar 2 band) legitimately
  remains **INDETERMINATE** — a disclosed cash balance is not a cash-conversion
  reading. **The concall makes the INDETERMINATE cap MORE binding, not less:**
  management CONFIRMS a **deliberate chip-inventory build** "over the last couple
  of quarters ... to increase our inventory holding of chips for both the IoT ...
  and payment solutions business" (L82, A3-13), explicitly "reflected by our
  working capital days," with supplier lead times up. This is a deliberate WC /
  inventory expansion that CONSUMES cash — adverse to conversion — and cannot be
  netted against the Rs 369 Cr balance without the Cash Flow Statement. Resolves
  at the Q2FY27 half-yearly filing (Reg 33 mandates H1 Balance Sheet + Cash Flow).

---

## 4. FORENSIC FINDINGS — RESULTS + PRESENTATION (A3, each with implication + cite)  [ROLE 4 — unchanged]

Concall forensic findings (A3-01..A3-15) are tabulated separately in Section 5.10.

| A3 id (file) | Classification | Finding & implication | Line/slide cite |
|---|---|---|---|
| F1-01 (results) | AMBIGUOUS | Standalone Exceptional nil all 4 periods, but Consolidated carries a subsidiary-origin exceptional (Q4FY26 +0.02, FY26 -0.25 Cr); standing FVTOCI equity-instrument line = equity investment held/anticipated at fair value; restructuring/impairment template stands ready. | 421-422/847/453-454 |
| F2-01 (results) | AMBIGUOUS | **C PAT 60.34 sits Rs 1.41 Cr BELOW S PAT 61.75.** Two subsidiaries net only −0.14 Cr (loss 0.22 + profit 0.08), so ~Rs 1.3 Cr of consolidation eliminations are unexplained; gap **sign-flipped** from +0.16 (Q1FY26 C>S) to −1.41 (Q1FY27 C<S). Consolidated rests on unaudited components. | 443-444/865 |
| F6-01 (results) | FORWARD-SIGNAL | IPO proceeds **Rs 170.1 Cr still unutilised**, incl **Rs 136.1 Cr manufacturing-capex earmark**, only Rs 6.77 Cr deployed this quarter — dateless committed capex / future commissioning window. | 603/998/609 |
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
| pres-F14 | NEUTRAL-FACT | Operating EBITDA printed as Rs 873.1 mn (YoY block) vs Rs 873.13 mn (QoQ block); "OPERTATING" typo; "51.17" precision outlier — governance hygiene, immaterial; reconciles to filing derivation (87.3 Cr). | lines 163/185/555 |
| pres-F16a | AMBIGUOUS | Slide-10 FY revenue chart ASCENDS to FY26 peak 15,583, but slide-16 stack + Notion FY26 base (Rs 1,441 Cr) DESCEND — reversed year labels or column-alignment artifact. Slide-16/Notion base is the one confirmed by the filing. | slide 10 vs 16, 299-308/466-478 |
| pres-F16b | FORWARD-SIGNAL | Headline EBITDA margin +135 bps is other-income driven (OI +203%); clean operating margin +22 bps to 23.2%; numerator mixes other income against a revenue-from-ops denominator. | 154/164/509 |
| pres-F16c | AMBIGUOUS | Under a "Gross Margin (%)" header the deck prints "YOY +13.3%", which is gross-PROFIT rupee growth; actual gross MARGIN FELL 286 bps YoY / 527 bps QoQ. | slide 15, 435-438 vs 154 |
| pres-F16d | FORWARD-SIGNAL | The −6.9% QoQ revenue / −573 bps QoQ margin drop is pre-framed as Q4 seasonality ("Q4 historically strongest"); implies structurally soft H1FY27 and a low internal bar. | slide 18, line 550 |

---

## 5. ROLE 5 — CONCALL ANALYSIS (Protocol v1.1)

### 5.0 Pre-flight (Step 0)

- **Call:** Seshaasai Technologies Q1 FY27 earnings conference call, quarter ended
  30-Jun-2026 (L26). ASR-normalised transcript, 89 lines, 58 turns; Q&A = 47 of
  58 turns (81%) — high Q&A share for an Indian small-cap. 8 primary questions
  from 7 analyst firms + 11 follow-ups.
- **Participants (Step 0B):** Pratik Jakab (IR, E&Y) host; **Pragnyat Lalwani
  (CMD / promoter) — present and answers the substance** (positive: promoter on a
  substantive call); Pawan Kumar (CFO) — financial highlights + 3 Q&A answers;
  **Gautam Jain (Whole-time Director) — introduced (L12) but ZERO speaking turns
  (MGMT_ABSENCE, A3-09)** — yellow flag. Analyst firms: Safaya Capital, II
  Capital, Nasir Investment, Lucky Investments, FMY 325 Investment Advisors, SN
  Daga & Company, Dalmus Capital Management (all buy-side / AIF-type; sharp,
  specific questions — a positive quality signal for the Q&A).
- **CFO-answers-operational yellow flag (Step 0/6):** Pawan (CFO) fielded the
  insurance client-churn question (L64) and restated IoT segment growth (L56) —
  operational/customer topics normally the CMD's domain. Mild flag; CMD did
  answer most operational questions, so limited concern.
- **Caveats (Step 0D):** standard forward-looking disclaimer referencing SEBI
  prospectus + annual reports (L12); no new caveat category added vs a normal
  call, though management leans heavily on "geopolitical uncertainties, currency
  fluctuations, cost pressures" (L23) as the margin hedge.
- **Business type (Step 0E):** standard operating business → Step 2 guidance set.
- **Promise-vs-delivery history (Step 0A):** this is the **first concall analysed
  under Role 5 for STYL** — no prior Role 5 log exists, so the trailing-4-quarter
  credibility ratio cannot be computed this quarter. The commitment register
  below begins the log; delivery scoring starts next quarter. A limited
  promise-vs-delivery against the Notion pre-committed gate is in Section 5.6.

### 5.1 Opening-remarks claims inventory (Step 1)

| # | Claim | Type | Quantified? | Line |
|---|---|---|---|---|
| 1 | Revenue +21.1% YoY, "strong start to FY27" | Backward | YES | 15 |
| 2 | Nagpur & Bengaluru facilities still under construction; Bengaluru operational by end CY2026 post regulatory approval | Operational / Forward | YES (date) | 15 |
| 3 | Won 2 multi-year PSU-bank tenders ≈ Rs 73 Cr over the tender period | Customer/Order | YES | 15 |
| 4 | Payment solutions 42% of revenue, +5% YoY | Backward/Segment | YES | 17 |
| 5 | Premium metal-card business gaining traction; Bengaluru capacity to serve domestic + international | Strategic/Operational | NO | 17 |
| 6 | Europe & Africa card export traction "additional avenue" | Strategic/Forward Soft | NO | 17 |
| 7 | CFS 40% of revenue, +13% YoY | Backward/Segment | YES | 19 |
| 8 | IoT 18% of revenue, +145% YoY | Backward/Segment | YES | 21 |
| 9 | RFID "still in the early stage of adoption"; pharma traceability pilots | Strategic/Forward Soft | NO | 21 |
| 10 | SIM commercial rollout done; eSIM "well positioned"; no date/first revenue | Operational/Forward Soft | NO | 21 |
| 11 | Working on price revisions to protect margins; strategic inventory management | Forward Soft | NO | 23 |
| 12 | H2 FY27 expected STRONGER (seasonal BFSI + CFS + IoT) | Forward Soft | NO | 23 |
| 13 | Medium-term revenue growth target 8-12% | Forward Guidance | YES | 23 |

**Four diagnostics:** (i) Quantified opening claims ≈ 6 of 13 (~46%) — the
forward-looking ones (metal card, exports, RFID, eSIM, price revisions, H2
strength) are almost all UNQUANTIFIED; the one hard forward number is the 8-12%
revenue guide. (ii) All-new vs reaffirmation: this is the first Role 5, so all
are baseline; the 8-12% is framed as a reaffirmation of a "medium-term target."
(iii) Quietly dropped: N/A (no prior log). (iv) **Internal contradiction in the
opening:** revenue printed +21.1% (L15) while the full-year guide is 8-12% (L23),
and margins are simultaneously "pressured" (L15) yet "healthy" — the guide-vs-
run-rate gap is the seed of A3-01 (Section 5.3).

### 5.2 Forward-guidance register (Step 2) — THE centrepiece

| Metric | This Q (Q1FY27) guidance | Prior guidance | Trajectory | Confidence | Ref |
|---|---|---|---|---|---|
| Revenue growth FY27 (also "medium-term") | **8-12%** | none logged | New | MEDIUM | L23/L31 |
| EBITDA / PAT margin | **WITHHELD** ("false precision"; drivers-not-outcomes); asserts H2>H1 op-leverage, margin "positive bias," "no dramatic change" | none | New/Refused | LOW | L31/L39/L45/L58 |
| IoT segment growth | **~45% FY27**; **35-40% FY28** | none | New | MEDIUM | L53 |
| IoT revenue mix | **15-18% by FY27 year-end** (vs 18% already in Q1) | none | New | MEDIUM | L68 |
| Payment solutions growth | **10-12% FY27** | none | New | MEDIUM | L55 |
| CFS growth | **"flattish"** ("more or less flat"; grew ~30% FY26) | none | New | LOW | L55/L56 |
| Capex envelope | **Rs 140-160 Cr/year, reaffirmed** | (prior "range we spoke about") | Maintained | HIGH | L37 |
| Capacity utilization | 65-70% typical, 85-90% peak | none | New | MEDIUM | L37 |
| SIM (share of 3rd-largest operator req.) | 20-25% currently | none | New | MEDIUM | L33 |
| SIM-card capacity utilization | ~40% | none | New | MEDIUM | L62 |
| Bengaluru metal-card facility | operational end-CY2026; certification by Q4FY27; meaningful revenue FY28 (token FY27) | none | New | MEDIUM (date) / LOW (revenue) | L15/L37/L72/L74 |
| Internal CAGR plan | ~12% | none | New | LOW | L56 |
| Africa/Europe card exports | "nascent stages," no size/timeline | none | New | LOW | L47 |
| Working capital / CCC | no band; deliberate chip-inventory BUILD raising WC days | none | New (adverse) | — | L82 |
| Net debt trajectory | net cash Rs 369 Cr; no forward band | none | — | — | L26 |
| Dividend / payout | not discussed | none | — | — | — |

**Guidance diagnostics:**
- **Widen/tighten:** N/A vs history; but management explicitly REFUSED to narrow
  margin to a number under three-analyst pressure — a widening of uncertainty on
  the single most thesis-relevant profitability metric.
- **Internal consistency (arithmetic):** the 8-12% revenue guide does NOT
  reconcile cleanly with the Q1 +21.1% print (see Section 5.3). Segment guides
  are directionally consistent with a mix moving toward IoT but the blended math
  is soft: Payments +10-12% (42% of mix) + CFS ~flat (40%) + IoT +45% (18%)
  blends to roughly +5% to +10% weighted — i.e. **the segment guides themselves
  imply ~8-12%, internally consistent with the headline guide but BELOW the Q1
  +21.1% run-rate.**
- **Vs our projections:** the Notion base assumes a ~34% probability-weighted
  CAGR path to FY29 with FY29 EPS Rs 21-22. An FY27 revenue guide of 8-12% sits
  BELOW the Notion trajectory's implied near-term growth and, if delivered as
  stated, pressures the base-case EPS bridge — flagged for Role 1 re-weighting,
  though A4 does not re-run valuation.
- **Refused guidance:** the FY27 EBITDA/PAT-margin number, refused three times
  (A3-02) — refusal on a metric that is squarely addressable at a self-declared
  decision quarter is itself information.

### 5.3 LEAD ROLE 5 FINDING — the 8-12% guide vs +21.1% actual deceleration (A3-01, AMBIGUOUS, HEADLINE)

**The math (all Rs Cr):** FY26 base Rs 1,441 Cr. Guide +8-12% → FY27 Rs 1,556-1,614
Cr. Less Q1FY27 actual Rs 377 Cr → **remaining 9M implied Rs 1,179-1,237 Cr**
against FY26 9M of Rs 1,130 Cr (1,441 − Q1FY26 310.87) = **only +4.3% to +9.5%
YoY for the remaining nine months, versus the Q1 print of +21.1%.** The full-year
guide therefore implies a **sharp YoY deceleration** across Q2-Q4.

**The apparent tension and its partial resolution:** management simultaneously
frames **H2 FY27 as "stronger"** (seasonal BFSI pickup, steady CFS, continued IoT
— L23) and pegs the year at 8-12%. These are not strictly contradictory: "H2
stronger" is a **sequential** (H2 > H1) claim, while 8-12% is a **YoY** figure,
and FY26's own H2 base was seasonally strong (Q4FY26 Rs 404 Cr). So a
sequentially stronger H2 can still print low-single to high-single-digit YoY if
it is only matching a tough H2FY26 comp. **But the residual signal stands:** the
full-year YoY lands far below the Q1 run-rate, which means EITHER (a) management
genuinely expects Q2-Q4 comps to be much harder / order timing to normalise, OR
(b) management is guiding conservatively below run-rate (sandbagging). This is
the OPPOSITE of the Overpromiser pattern — a guide set well below the reported
run-rate — which is a relatively benign credibility posture, but it also means
**the 8-12% number is "soft" and low-information as a gate criterion**: it is
satisfied trivially by the Q1 print alone. A4 converts this to the lead
management question (Section 7B, Q18).

### 5.4 Margin-guidance refusal (A3-02, AMBIGUOUS)

The FY27 EBITDA/PAT-margin number was **refused three times** across three
consecutive analyst slots (Dia Jen L30→L31; Mohit Sukani L38→L39; Zakir Nasir
L44→L45) — a REPEAT_QUESTION pattern (three analysts do not trust the first
non-answer). Management's line: "Any precise number we give you today probably
would be false precision" (L31); "as a matter of practice we don't put out
specific margin figures" (L39); "we don't see any dramatic change in the margin
... positive bias as we go along" (L45); and it declines segment-level margins
too ("we've not separately given our margins across the three verticals," L58).
**Reading (adversarial, per Role 5):** management offers "drivers not outcomes"
and asserts H2>H1 operating leverage plus a margin "positive bias." This is
principled refusal, NOT evasive redirection (no "take it offline" / "get back to
you" defensive tells — see 5.8) — it reads as *evidenced discipline* rather than
*evidenced opacity*, but at the **pre-committed decision quarter** where the
Notion gate explicitly required "specific revenue/margin guidance," the margin
half of that criterion is UNMET. Trigger 7 is therefore PARTIAL (revenue given,
margin withheld). A4 converts to a direct FY27 EBITDA-margin question (Section
7B, Q19).

### 5.5 Q&A decomposition + management absence (Step 4)

**5.5A Q&A inventory (response-quality graded A best → E refusal):**

| # | Analyst / firm | Question (1-line) | Category | Resp. quality | Line |
|---|---|---|---|---|---|
| 1 | Dia Jen / Safaya | FY revenue + margin outlook | Fwd Guidance | B (rev) / E (margin) | 30-31 |
| 1f | Dia Jen / Safaya | SIMs rolled out so far | Operational | B (20-25% of 3rd-largest operator) | 32-33 |
| 2 | Mohit Sukani / II Capital | GM drivers (op-lev vs FX), capacity, capex | Financial/Op | B (40-45% FX; 65-70% util; 140-160 Cr) | 36-37 |
| 2f | Mohit Sukani | Full-year gross-margin % | Fwd Guidance | E (refused) | 38-39 |
| 2f2 | Mohit Sukani | Order-book growth rate | Customer/Order | C (no number; "steady pipeline") | 40-41 |
| 3 | Zakir Nasir / Nasir | Is Q1 the margin base for the year | Financial | C ("no dramatic change," positive bias) | 44-45 |
| 3f | Zakir Nasir | UPI vs cards impact on payments | Strategic | B (detailed, MDR thesis) | 46-47 |
| 3f2 | Zakir Nasir | Payment-gateway entry | Strategic | B (declines the adjacency clearly) | 48-49 |
| 4 | British / Lucky | Segment growth 2-3 yr (RFID/eSIM/SIM/cards) | Fwd Guidance | B (IoT 45%→35-40%) | 52-53 |
| 4f | British | Cards growth | Fwd Guidance | B (payments 10-12%; CFS flat) | 54-56 |
| 4f2 | British | Margin chronology by vertical | Financial | C (blended 25%; declines split) | 57-58 |
| 5 | Pratik Bantia / FMY 325 | SIM-card capacity utilization | Operational | A (~40%) | 61-62 |
| 5f | Pratik Bantia | Insurance client count 13→10 / 9→10 | Customer | B (churn "almost zero" business) [CFO] | 63-64 |
| 6 | Sedart Daga / SN Daga | IoT >100% Q1 vs 45% guide — slowdown? | Fwd Guidance | B (weak base, "no slowdown," 15-18% mix) | 67-68 |
| 7 | DRJ / Safaya | Bengaluru meaningful FY28 revenue? | Operational/Fwd | B ("Definitely") | 71-72 |
| 7f | DRJ | Quantify Bengaluru revenue | Fwd Guidance | E ("too early") | 73-74 |
| 8 | Pulkit Singhal / Dalmus | Chip price YoY, inventory pricing | Financial | B (flat, FX-offset) | 77-78 |
| 8f | Pulkit Singhal | Confirm chip flat YoY | Financial | B (marginal improvement, FX-offset) | 79-80 |
| 8f2 | Pulkit Singhal | Forward chip-price risk given inventory | Financial | B (WC build; "no clear indications") | 81-82 |

**5.5B pattern analysis:** the most-repeated ask is the **full-year margin
number** (three analysts, graded C/E each time) — the topic management least
wants pinned. Second cluster: **segment growth trajectory** (IoT deceleration
45% vs +145% print). Buy-side dominated, sharp questions (positive). No house-
broker softball opener. One analyst mildly pushed back (Sedart Daga's "are we
signaling a slowdown," L67) — management defended with the weak-base explanation.

**5.5C three most thesis-relevant exchanges:** (i) **margin refusal** (L38-39) —
management will not give a full-year margin at the decision quarter; implies the
27% gate stays unconfirmed and unforecastable from the call. (ii) **IoT
deceleration** (L67-68) — the +145% print is a weak-base artifact; true guided
trajectory is +45%, mix flat at 15-18%; the IoT catalyst is real but decelerating.
(iii) **WC / inventory build** (L81-82) — management confirms a deliberate
cash-consuming inventory strategy, directly relevant to the INDETERMINATE
cash-conversion cap.

**5.5D management absence (A3-09, CONFIRMATORY-NEGATIVE):** Gautam Jain, WTD, is
introduced (L12) as one of three management representatives but has **zero
speaking turns** across 89 lines — monitoring **trigger 13 NOT fired** (confirmed
negative, not merely N.A. as in the base). A named WTD silent on a substantive
guidance/margin/capex call is a governance data point, carried to A5 and to
Section 6.

### 5.6 Promise-vs-delivery — limited audit vs the Notion pre-committed gate (Step 3)

No prior Role 5 log exists, so the trailing-4-quarter credibility ratio is **not
computable this quarter**; the register in 5.2 begins the log. Where inferable,
delivery is assessed against the Notion pre-committed monitorables:

| Pre-committed monitorable (Notion) | Concall delivery | Status |
|---|---|---|
| FY27 guidance "provided" | Revenue 8-12% given (L23/31); margin refused (L31/39/45) | PARTIALLY DELIVERED |
| SIM utilization disclosure >40% (vs 30%) | "close to around 40%" (L62) | PARTIALLY DELIVERED (borderline) |
| eSIM first revenue / specific date | none — vague platform readiness (L21) | NOT DELIVERED (~9-mo slip) |
| RFID (Reliance/largest-retailer) volume | "early stage," pilots, no name/volume (L21) | NOT DELIVERED |
| WC / cash-transition initiative addressed | addressed, but a deliberate cash-CONSUMING inventory build (L82) | DELIVERED-ADVERSE |
| Gautam Jain substantive participation | silent (L12) | NOT DELIVERED |

Credibility grade this quarter: **N/A (first Role 5 — insufficient history);
provisional posture below-run-rate/conservative on revenue, refusing on margin.**

### 5.7 New-information audit + what was NOT discussed (Step 5)

**5.7A new disclosures:**

| Disclosure | Type | Material? | Thesis impact |
|---|---|---|---|
| 2 PSU-bank multi-year tenders ≈ Rs 73 Cr over tender period (L15) | Customer/Order | Modest — <5% of one year's revenue, spread over years | Minor positive; A3-08, reconcile vs deck |
| Bengaluru metal-card greenfield operational end-CY2026; certification by Q4FY27; meaningful revenue FY28 (L15/37/72/74) | Capex/Capacity | YES — datable commissioning catalyst | A3-14; FY28 revenue unquantified |
| Capex Rs 140-160 Cr/yr reaffirmed (L37) | Capex | YES | Confirms sustained investment; feeds Pillar/FCF |
| COMC 58.34% vs FY26 avg 54.23% (+411 bps) (L26) | Financial | YES — sizes the gross-margin driver | Confirms input-cost squeeze |
| Top-10 customers 56%; >95% from existing clients (L26) | Customer conc. | YES — conflicts with deck ~73% | A3-06; reconcile basis |
| Deliberate chip-inventory build raising WC days (L82) | Operational/WC | YES — adverse to cash conversion | A3-13; caps cash-conversion |
| SIM = 20-25% of 3rd-largest operator's requirement (L33); SIM util ~40% (L62) | Operational | YES — capacity-absorption evidence | Trigger 4 borderline |
| UPI-vs-cards / MDR thesis (L47) | Strategic | Medium — defends payments durability | Qualitative reassurance |

**5.7B what was NOT discussed (silence is signal):**

| Expected topic | Why it should have been discussed | Significance |
|---|---|---|
| FY27 EBITDA/PAT margin number | Decision quarter; Notion gate demanded it | AMBER→RED (refused 3x) |
| eSIM commercial date / first revenue | Named thesis catalyst; already slipped ~9 months | AMBER→RED |
| RFID named anchor customer + volume | Reliance-candidate; trigger 9 | AMBER |
| Receivable days / inventory days (numeric) | Cash-conversion is INDETERMINATE; WC build confirmed qualitatively only | AMBER |
| Promoter lock-in expiry / OFS intent (30-Sep-2026) | Supply overhang; trigger 10 | AMBER |
| Promoter pledge status | Hard-kill trigger 11 | Neutral (no event ⇒ not fired) |
| Receivables factoring | Rules out disguised WC financing; trigger 12 | Neutral-AMBER |
| Payments segment QoQ trajectory | Trigger 14 (deck shows 2 consecutive declines) | AMBER — YoY +5% given, QoQ not |
| C-minus-S consolidation / subsidiary detail | F2-01 sign-flip | Neutral (concall carries no C/S split) |

### 5.8 Tone, specificity & archetype (Step 6)

- **Specificity score (6B):** quantified forward statements ≈ 8 (8-12% rev; IoT
  45%/35-40%; IoT 15-18% mix; payments 10-12%; capex 140-160; SIM 20-25%; SIM
  util ~40%; capacity 65-70%) vs unquantified/directional forward ≈ 8 (margin
  refused; CFS "flattish"; eSIM date; RFID volume; Bengaluru revenue; Africa/
  Europe exports; H2 "stronger"; internal 12% CAGR). **Specificity ratio ≈ 0.5 —
  moderate.**
- **Hedge / defensive language (6C):** margin refusal x3, "false precision," "no
  dramatic change," "too early," "no forward bias / no very clear indications,"
  "as things crystallize," "share from time to time" — **≥8 hedge instances ⇒
  hedge-heavy call**, concentrated on (a) margin and (b) forward input-cost. Note
  these are **principled refusals, not evasive redirections** — no "take it
  offline"/"get back to you" tells — which reads more as discipline than
  concealment, but the count is logged for trajectory.
- **Confidence indicators (6D):** promoter (CMD) on the line answering
  operational questions directly (positive); specific capex band reaffirmed;
  specific SIM operator-share and utilization; datable Bengaluru commissioning.
- **Archetype (6E):** specificity ~0.5 with **credibility ratio not yet
  computable** (first Role 5). **Provisional classification: MEASURED-leaning** —
  a conservative guider (revenue guided BELOW the run-rate, margin withheld
  rather than over-committed). This is NOT the Overpromiser quadrant (that
  requires hyper-specific guidance + poor delivery). **The archetype is
  provisional until a delivery record exists**; the 8-12% guide is the first
  testable commitment. Watch for a shift toward Overpromiser only if future
  specific guides (IoT 45%, capex 140-160, Bengaluru FY28) are missed.

### 5.9 Cross-reference vs filing and peers (Step 7)

**7A concall narrative vs filing:**

| Concall claim | Filing evidence | Reconciliation |
|---|---|---|
| Revenue Rs 377 Cr, +21.1% YoY, -6.9% QoQ (L26) | 376.47 Cr; +21.1%; -6.9% (l.387/511) | CONFIRMED |
| Gross profit Rs 157 Cr, GM 41.7% vs 44.5% (L26) | 156.83 Cr; 41.7% derived | CONFIRMED |
| EBITDA Rs 94 Cr, 25.1%, +135 bps (L26) | 94.41 Cr; 25.08% derived | CONFIRMED |
| PBT Rs 82 Cr +48.8%; PAT Rs 60 Cr / 16% +418 bps (L26) | 81.79 / 60.34 / 16.03% | CONFIRMED |
| "substantial reduction in finance cost" drove PBT (L26) | Finance cost 7.76→1.84 (-76%) l.407-408 | CONFIRMED (management concedes the flatterer) |
| Net cash Rs 369 Cr at 30-Jun-2026 (L26) | deck ~Rs 369 Cr (L950-951); no BS in filing | PARTIALLY CONFIRMED (deck-only, unaudited) |
| IoT 18% of revenue, +145% (L21/26) | PR 18% ≈ Rs 67.4 Cr; NOT a statutory segment | PARTIALLY CONFIRMED (unaudited segment) |
| Top-10 customers 56% (L26) | deck ~73%; filing single-segment, no conc. data | CONTRADICTED / UNVERIFIABLE (basis differs) |
| "healthy margins maintained" (L15) | operating EBITDA margin +22 bps; GM -286 bps | PARTIALLY CONFIRMED / narrative-flattering |

The one material narrative-vs-source conflict is **top-10 concentration 56%
(concall) vs ~73% (deck)** — likely different bases (top-10 customers vs a
top-customer grouping), handed to Section 7B, Q23. No concall claim contradicts a
FILING number; all headline figures tie out.

**7B peer cross-check:** no company in the analysed universe reported a concall
within ±4 weeks of this call that shares STYL's security-printing / payment-card
end-market in this pass — **peer cross-check N/A this quarter** (stated
explicitly per protocol). Input-cost (chip/FX) commentary would be the natural
peer check if one becomes available.

### 5.10 CONCALL FORENSIC FINDINGS (A3-01..A3-15, each with cite)

| A3 id | Classification | Finding & implication | Line |
|---|---|---|---|
| A3-01 | AMBIGUOUS (HEADLINE) | 8-12% FY guide vs Q1 +21.1% ⇒ implied 9M remaining +4-10% YoY = sharp YoY deceleration; H2-"stronger" is sequential not YoY; guide soft/below run-rate | 23/31 |
| A3-02 | AMBIGUOUS | FY margin refused 3x under 3-analyst pressure ("false precision"); drivers-not-outcomes; trigger 7 PARTIAL | 31/39/45 |
| A3-03 | AMBIGUOUS / FWD | IoT +145% Q1 vs +45% FY27 / 35-40% FY28 ⇒ sharp H2 IoT deceleration; +145% a weak-base artifact; mix guided 15-18% | 21/53/68 |
| A3-04 | AMBIGUOUS | CFS growth framing inconsistent: +13% this Q vs ~30% FY26 vs "flattish" ahead — three rates, two speakers | 19/55/56 |
| A3-05 | AMBIGUOUS | Payments +5% Q1 vs 10-12% full-year guide ⇒ needs strong H2 payments ramp | 17/55 |
| A3-06 | AMBIGUOUS | Top-10 concentration 56% (concall) vs deck ~73%; >95% existing-client dependence; reconcile basis | 26 |
| A3-07 | AMBIGUOUS | Insurance client count 13→10 life / 9→10 general (analyst slide) reframed by CFO as "almost zero" business, not lost | 63/64 |
| A3-08 | NEUTRAL-FACT / AMBIGUOUS | 2 PSU tenders Rs 73 Cr over tender period = modest (<5% of one year); reconcile vs deck; size annualised | 15 |
| A3-09 | CONFIRMATORY-NEG | Gautam Jain WTD introduced but SILENT; trigger 13 NOT fired (MGMT_ABSENCE) | 12 |
| A3-10 | FWD / CONF-NEG | eSIM commercial date/first revenue still SILENT; ~9-mo slip; trigger 8 unanswered at decision quarter | 21 |
| A3-11 | CONFIRMATORY-NEG | RFID no named anchor customer, no volume; trigger 9 unquantified | 21 |
| A3-12 | CONFIRMATORY-NEG | Inventory days, receivable days, lock-in/OFS, pledge, factoring all SILENT (triggers 5,6,10,11,12) | 0 |
| A3-13 | FORWARD-SIGNAL | Deliberate chip-inventory BUILD raises WC days / consumes cash; supports INDETERMINATE cash-conversion cap; trigger 15 addressed but ADVERSE | 82 |
| A3-14 | FORWARD-SIGNAL | Bengaluru greenfield operational end-CY2026; meaningful FY28 revenue (unquantified); capex 140-160 Cr/yr; track slippage | 15/37/72/74 |
| A3-15 | FORWARD-SIGNAL | Chip prices flat YoY (rupee-offset); forward price-rise risk acknowledged; direct FY27 margin risk on the metric management refuses to guide | 78/80/82 |

---

## 6. FTTCP MONITORING-TRIGGER SCORECARD (all 15) — RE-SCORED WITH CONCALL — FLAG only, operator decides

Status set: **FIRED FAVOURABLY / BREACHED / CONFIRMED-NEGATIVE / BORDERLINE-MET /
PARTIAL / SILENT / N.A.** Each with the reconciled number and cite. STYL is a HELD
position; these are the pre-committed Q1 FY27 decision-gate triggers. **Δ = change
vs the pre-concall (Role-4-only) reading.**

| # | Trigger | Reconciled reading (incl. concall) | Status | Δ vs base | Cite |
|---|---|---|---|---|---|
| 1 | Revenue YoY > +10% | +21.1% (376.47 vs 310.87); concall confirms | **FIRED FAVOURABLY** | = | 387/511; concall L15/26 |
| 2 | EBITDA margin sustain > 27% | Reported 25.1% / Operating 23.2% — both <27%; concall confirms 25.1% (L26) | **BREACHED** | = | 418/407-410/389; L26 |
| 3 | IoT revenue > Rs 55 Cr | Rs 67.4 Cr (+145% YoY) deck/PR; concall 18% x Rs 377 Cr ≈ Rs 67.9 Cr — **unaudited, NOT a statutory segment** | **FIRED FAVOURABLY (unaudited)** | = | slide 14; L21/26; caveat l.611 |
| 4 | SIM utilization disclosure > 40% (vs 30%) | Concall: SIM-card capacity util "close to around 40%" (L62); SIM = 20-25% of 3rd-largest operator req. (L33) | **BORDERLINE-MET** | ▲ was SILENT | L62/L33 |
| 5 | Inventory days < 80 | No numeric days; concall CONFIRMS a deliberate chip-inventory BUILD raising WC days (L82) | **PARTIAL / ADVERSE** | ▲ was SILENT (now adverse-informed) | L82 |
| 6 | Receivable days stable or < 80 | No Balance Sheet; not addressed on concall | **SILENT** | = | A2 absence |
| 7 | FY27 guidance provided (specific rev + margin) | Revenue 8-12% GIVEN (L23/31); margin explicitly WITHHELD 3x (L31/39/45) | **PARTIAL** | ▲ was SILENT/ABSENT | L23/31/39/45 |
| 8 | eSIM commercial launch (first rev or Q2FY27 date) | Concall: vague platform readiness only; no date, no revenue (L21) | **SILENT** | = (re-confirmed on call) | L21 |
| 9 | Reliance/largest-retailer RFID volume disclosed | Concall: "early stage," pilots; no name, no volume (L21) | **PARTIAL / SILENT** | = (re-confirmed on call) | L21 |
| 10 | Promoter lock-in — no OFS within 60 days of 30-Sep-2026 | Not addressed on concall; lock-in expiry still pending | **SILENT** | = | — |
| 11 | Promoter pledge stays 0% | No pledge event disclosed anywhere | **SILENT (no event ⇒ hard-kill NOT triggered)** | = | — |
| 12 | Receivables factoring facility announced | Not mentioned; finance-cost fall attributed to debt reduction | **SILENT** | = | 181 |
| 13 | Gautam Jain substantive concall participation | Introduced (L12) but ZERO speaking turns across 89 lines | **CONFIRMED-NEGATIVE (NOT fired)** | ▲ was N.A. | L12 |
| 14 | Payments QoQ — no 2 consecutive declines | Deck: 1,984→1,919→1,582 Mn = TWO consecutive QoQ declines; concall gives +5% YoY (L17) but no segment QoQ | **BREACHED** (ORDER_INFERRED caveat) | = (concall adds +5% YoY, 10-12% guide) | slide 12 l.325; L17/55 |
| 15 | Cash-transition WC initiative addressed | Concall CONFIRMS a deliberate chip-inventory build to lock pricing — addressed, but CASH-CONSUMING | **ADDRESSED-ADVERSE** | ▲ was PARTIAL/SILENT | L82 |

**Updated tally (15):** FIRED FAVOURABLY **2** (#1, #3 — #3 unaudited) ·
BORDERLINE-MET **1** (#4) · PARTIAL **2** (#7, #9) · BREACHED **2** (#2, #14) ·
CONFIRMED-NEGATIVE **1** (#13) · PARTIAL/ADVERSE or ADDRESSED-ADVERSE **2** (#5,
#15) · SILENT **5** (#6, #8, #10, #11, #12). *(Base tally was: FAVOURABLE 2 ·
BREACHED 2 · PARTIAL 2 · SILENT 8 · N.A. 1. The concall MOVED #4 SILENT→
BORDERLINE-MET, #7 SILENT→PARTIAL, #13 N.A.→CONFIRMED-NEGATIVE, and re-cast #5/#15
as adverse-informed — net: SILENT drops from 8 to 5; no previously-favourable
trigger newly fired.)*

**Re-engagement rule FLAG (5+ favourable ⇒ upgrade to BUY 4-5% Medium, Tranche
2):** clearly-favourable firings remain **2** (#1, #3, one unaudited). #4 is
BORDERLINE (threshold is ">40%"; management said "close to around 40%," i.e. at
but not clearly above), #7 is PARTIAL (margin withheld). Even crediting #4 and #7
as half-fires the count does not reach 5 clean favourable. **Rule NOT met — no
upgrade signal.**

**Hard-kill rule FLAG (trim 50% if (a) trigger 11 pledge fires OR (b) 3+ of
triggers 8/14 fire negatively):** (a) **Pledge did NOT fire** — no pledge event.
(b) Among the negative-signal set, **#14 is an unambiguous negative** and #8 is a
gate-relevant silence re-confirmed on the call; #2 is a clear margin breach and
#13 is now a CONFIRMED governance negative — but the strict "3+ of triggers 8/14"
pair is **NOT mechanically met** (only two triggers named in that clause, and only
#14 clearly "fires negatively"). **Hard-kill NOT mechanically met.** However the
adverse cluster has WIDENED with the concall: 2 hard breaches (#2, #14) + 1
confirmed governance negative (#13) + 2 adverse-informed WC/inventory items (#5,
#15) + 3 re-confirmed thesis-critical silences (#8 eSIM, #9 RFID, #10 lock-in) at
the pre-committed gate. **Flagged for operator attention. A4 does not change
Decision Status.**

**Pre-committed "next decision gate" (Notion) — 4 criteria, RE-SCORED with
concall:**
- **IoT > Rs 55 Cr: MET** (Rs 67.4 Cr / ~67.9 Cr derived, unaudited; concall
  L21/26). *(unchanged)*
- **EBITDA > 26%: NOT MET** (25.1% reported / 23.2% operating; concall confirms
  25.1%, L26). *(unchanged)*
- **Payments YoY stable: MARGINAL** — concall gives +5% YoY (L17) and a 10-12%
  full-year guide (L55), positive on YoY but two consecutive QoQ declines in the
  deck and mix share ~48%→42%; hitting 10-12% needs a strong H2 ramp (A3-05).
  *(unchanged status, better sourced)*
- **FY27 guidance provided: NOW PARTIAL / soft-MET** — revenue 8-12% GIVEN
  (L23/31); margin WITHHELD (L31/39/45). *(▲ upgraded from NOT MET in the base.)*

→ **New count: 1 clearly MET (IoT) + 1 soft/PARTIAL MET (guidance — revenue only)
+ 1 MARGINAL (Payments) + 1 NOT MET (EBITDA), i.e. ~1.5-2 of 4, versus the prior
1 of 4.** The concall's provision of a REVENUE guide is the sole mover of the gate
tally; **the margin half remains unprovided and the 8-12% figure is SOFT** (it is
below the Q1 +21.1% run-rate and is satisfied by the Q1 print alone — Section
5.3). Flagged for the operator's gate decision.

**Thesis-broken conditions (any 2 of 5) — status:** PAT margin < 14% for two
quarters → NOT breached (16.0% this quarter). Promoter pledge initiated → NOT
fired. CFO/PAT < 0.5x for 2 years → **INDETERMINATE** (no cash flow; concall
confirms a cash-consuming inventory build, adverse but not measurable). eSIM
slips beyond Q2 FY28 → NOT yet, but the concall gave NO date at the decision
quarter (~9-month slip stands; AT RISK). Receivable days > 110 → **INDETERMINATE**
(no Balance Sheet). **No thesis-broken condition has FIRED.**

---

## 7. QUESTIONS FOR MANAGEMENT — UPDATED (concall answers marked; new concall questions added)

Every AMBIGUOUS / FORWARD-SIGNAL finding from all THREE forensics files maps to at
least one row. **7A** = the base Role 4 questions with concall answer-status
(protocol Step 3E / cross-reference to Role 4 Step 8.5). **7B** = new questions
raised by the concall (protocol Step 8F).

### 7A. Role 4 questions — concall answer status

| # | Question (abridged) | From finding | Answer status on concall | Disposition |
|---|---|---|---|---|
| 1 | Path/timeline back to >27% EBITDA / GM recovery from 41.7% | F7-01, X2, pres-F16b/c | PARTIALLY — H2>H1 op-leverage asserted, no timeline, no number (L37/39/45) | KEEP, sharpen (7B-Q19) |
| 2 | Specific FY27 revenue AND EBITDA-margin guidance | trigger7, pres-F16a | PARTIALLY — revenue 8-12% given; margin REFUSED (L23/31/39/45) | RETIRE revenue half; KEEP margin (7B-Q19) |
| 3 | Payments 2 consecutive QoQ declines — timing vs structural; Q2 run-rate | trigger14, pres-F6 | PARTIALLY — +5% YoY + 10-12% guide (L17/55); QoQ NOT addressed | KEEP, sharpen (7B-Q20) |
| 4 | Repeatable PAT growth ex finance-cost + ETR tailwinds | F8-01, pres-F8/F1, X3 | NOT ADDRESSED (management concedes finance-cost driver but not repeatability) | KEEP |
| 5 | Other Income +203% source and recurrence | X2, pres-F16b | NOT ADDRESSED | KEEP |
| 6 | C-minus-S PAT sign-flip; ~Rs 1.3 Cr unexplained eliminations | F2-01 | NOT ADDRESSED (no C/S split on call) | KEEP |
| 7 | Rs 136.1 Cr manufacturing-capex deployment schedule / commissioning | F6-01 | PARTIALLY — capex 140-160 Cr/yr reaffirmed; Bengaluru end-CY2026 (L37) | KEEP, sharpen (7B-Q26) |
| 8 | eSIM commercial launch date / first revenue | trigger8, A3-10 | EVADED — vague readiness only, no date (L21) | KEEP, escalate (7B-Q24) |
| 9 | SIM utilization vs prior ~30% | trigger4, A3 | ANSWERED — "close to around 40%" (L62); 20-25% of operator req. (L33) | ANSWERED — retire; monitor trajectory |
| 10 | Largest-retailer RFID volume — name and size | trigger9, pres-F6, A3-11 | EVADED — "early stage," pilots, no name/volume (L21) | KEEP, escalate (7B-Q25) |
| 11 | Receivable/inventory days and CFO/PAT; WC initiative effect | triggers5/6/15, COV-1 | PARTIALLY — inventory BUILD confirmed (L82), but no numeric days/CFO | KEEP, sharpen (7B-Q27) |
| 12 | FY27 revenue contribution/timing of 3 tenders + Europe/Africa exports | pres-F6 | PARTIALLY — Rs 73 Cr over tender period (L15); exports "nascent" (L47) | KEEP, sharpen (7B-Q22) |
| 13 | Actuarial OCI gain > full prior year — assumption change? | F9-01 | NOT ADDRESSED (no OCI on call) | KEEP |
| 14 | Slide-10 FY26 15,583 vs filing 14,411 — 3-yr revenue flat/declining? | pres-F16a, X1 | NOT ADDRESSED | KEEP |
| 15 | Any receivables-factoring facility this year? | trigger12 | NOT ADDRESSED | KEEP |
| 16 | Lock-in expiry 30-Sep-2026 — OFS within 60 days; pledge 0%? | triggers10/11 | NOT ADDRESSED | KEEP |
| 17 | FY27 PAT margin > FY26 16.7%? (Q1 16.0% regressed) | BEAR-1, pres-F8 | EVADED — margin refused (L39/45) | KEEP, fold into 7B-Q19 |

### 7B. New questions raised by the concall

| # | Question (references a concall number/line) | From finding | Why it matters | Bull answer | Bear answer |
|---|---|---|---|---|---|
| 18 | You printed +21.1% revenue in Q1 yet guide the full year to 8-12% (L23/31). Backing out Q1, that implies only ~+4-10% YoY for the remaining nine months. Is that a genuine expectation of tougher Q2-Q4 comps, an order-timing normalisation, or a conservative guide below run-rate? | A3-01 | The lead concall finding; sizes the H2 deceleration and tests whether the guide is sandbagged | Conservative guide; H2 comps tough but real momentum intact | Genuine sharp slowdown ahead |
| 19 | You declined a FY27 EBITDA/PAT-margin number three times (L31/39/45). At a self-declared decision quarter, what full-year EBITDA-margin range do you expect, and do you expect FY27 PAT margin to exceed FY26's 16.7% (Q1 was 16.0%)? | A3-02, BEAR-1, F7-01, X2 | The failed/withheld gate criterion; the single most thesis-relevant metric | Numeric band ≥27% EBITDA / >16.7% PAT with driver | Continued refusal; margin ≤ FY26 |
| 20 | Payments grew only +5% YoY in Q1 (L17) but you guide 10-12% for the year (L55). What H2 payments ramp gets you there, and did Payments decline QoQ in Q1 (the deck shows two consecutive sequential declines)? | A3-05, trigger14 | Payments is ~42% of revenue and the laggard; H2 ramp is load-bearing for the full-year guide | Named order backlog; H2 seasonal ramp confirmed | Structural share erosion |
| 21 | IoT grew +145% in Q1 (L21) but you guide ~45% FY27 and 35-40% FY28 (L53) and call the print "exaggerated" by a weak base (L68). What is the absolute IoT revenue run-rate you are underwriting for H2, and does mix stay at 15-18% (L68) despite 18% already in Q1? | A3-03 | Sizes the IoT catalyst and its H2 deceleration; IoT is the transition-alpha pillar | Absolute run-rate rising; mix expands past 18% | Sharp H2 IoT fade; mix flat/down |
| 22 | The two PSU-bank tenders are Rs 73 Cr "over the tender period" (L15). What is the annualised revenue and start timing, and how does this reconcile with the three multi-year tenders in the deck? | A3-08, pres-F6 | Sizes forward backlog; <5% of one year spread over years is modest | Annualised figure + start date | Vague, immaterial |
| 23 | The CFO cited top-10 customer concentration of 56% (L26), but the deck shows ~73%. Which basis is correct (top-10 vs top-customer grouping), and with >95% of revenue from existing clients, what is the new-logo pipeline? | A3-06 | Concentration is a core risk; a 56%-vs-73% gap needs a basis reconciliation | Clear basis; growing new-logo pipeline | Opaque; thin new-client funnel |
| 24 | eSIM: you cite only "platform readiness" (L21) with no commercial date or first revenue, at a quarter where the thesis flagged eSIM. When does eSIM commercially launch (first revenue or a specific date)? It has already slipped ~9 months. | A3-10, trigger8 | Named thesis catalyst; slippage past Q2 FY28 is a thesis-broken condition | Committed date / first revenue | Further slippage |
| 25 | RFID remains "early stage," pilots only (L21), with no named anchor customer or volume. Can you name a reference customer and quantify RFID volume/revenue? | A3-11, trigger9, pres-F6 | Anchor-customer / concentration thesis; repeated qualitative optionality without a number | Named + sized customer | Unnamed, unquantified again |
| 26 | Bengaluru metal-card greenfield is "operational by end CY2026" with "meaningful revenue FY28" but you declined to quantify (L72/74). What FY27 token and FY28 revenue do you underwrite, and what is the capex tied to it within the 140-160 Cr/yr envelope (L37)? | A3-14 | Datable commissioning catalyst + capex absorption; FY28 revenue unquantified | Sized FY28 revenue + capex schedule | Indefinite; capital idle |
| 27 | You confirmed a deliberate chip-inventory build "reflected by our working capital days" (L82). By how many days did inventory/WC rise, how much cash is tied up, and what were receivable/inventory days and CFO/PAT this quarter? (No Balance Sheet/Cash Flow was filed.) | A3-13, triggers5/6/15, COV-1 | Cash CONVERSION is INDETERMINATE and the build is adverse; the binding Pillar 2 gap | Quantified, temporary, funded by cash | Refusal; WC deteriorating structurally |
| 28 | The insurance client count fell 13→10 life / 9→10 general per your own slide (L63), reframed as "almost zero" business churned (L64). Please quantify the revenue of the churned accounts and confirm no retender losses. | A3-07 | Selective-framing check on a disclosed client-count decline | Sized as immaterial, no retender | Material churn understated |
| 29 | Gautam Jain (WTD) was introduced (L12) but did not speak on a substantive guidance/margin/capex call. What is his operating remit, and will he participate in future calls? | A3-09, trigger13 | Governance signal; a named exec silent on the record | Clear remit; will engage | Figurehead / undisclosed transition |
| 30 | Chip prices are "flattish" YoY, "more than offset by the dollar impact" (L80), with forward price-rise risk and rising supplier lead times (L82). What rupee/chip assumption underlies the 8-12% guide, and what margin sensitivity to a chip/FX up-move? | A3-15 | Input cost is the stated GM culprit and directly hits the margin you refuse to guide | Hedged/contracted; low sensitivity | Unhedged; high FY27 margin risk |

**Coverage check:** every AMBIGUOUS/FORWARD-SIGNAL finding across results
(F1-01, F2-01, F6-01, F7-01, F8-01, F9-01, F12-01, X2, X4), presentation (pres-F6,
pres-F8, pres-F16a/b/c/d) and concall (A3-01..A3-15) maps to at least one 7A or 7B
row. Concall CONFIRMATORY-NEGATIVES A3-09/10/11/12 map to Q29/Q24/Q25/Q27 & Q16.

**Top 3 by likelihood of thesis-changing information:** (1) Q19 (FY27 margin
number / refusal) — the failed gate criterion; a refusal repeated next quarter is
itself a downgrade signal. (2) Q18 (8-12%-vs-21% deceleration) — determines
whether the guide is conservative or a genuine slowdown; the base thesis growth
path depends on it. (3) Q27 (inventory-build cash impact) — resolves whether the
INDETERMINATE cash-conversion cap tightens or clears at Q2.

---

## 8. MONITORABLES & CATALYSTS — UPDATED with concall (A3 commitment register F6 + concall register)

| Item | Implied date | Source ref | Status word |
|---|---|---|---|
| FY27 revenue guide 8-12% — track full-year YoY vs the +21.1% Q1 run-rate (deceleration test) | FY27 | concall L23/31 | guided (soft/below run-rate) |
| FY27 EBITDA/PAT margin — WITHHELD; watch for a number next quarter | FY27 | concall L31/39/45 | refused (watch) |
| IoT growth ~45% FY27 / 35-40% FY28; mix 15-18% | FY27-FY28 | concall L53/68 | guided (decelerating from +145% Q1) |
| Payments growth 10-12% (needs H2 ramp; +5% Q1) | FY27 | concall L17/55 | guided (H2-loaded) |
| Bengaluru metal-card greenfield operational; certification by Q4FY27 | end-CY2026 | concall L15/37 | under construction |
| Bengaluru meaningful revenue (token FY27) | FY28 | concall L72/74 | committed (unquantified) |
| Capex Rs 140-160 Cr/yr reaffirmed | FY27 (per year) | concall L37 | reaffirmed |
| Chip-inventory BUILD / WC-days increase — quantify cash tied up | ongoing | concall L82 | confirmed (adverse to cash conversion) |
| Chip/FX forward price-rise risk; supplier lead times up | ~next year (uncertain) | concall L78/80/82 | watch |
| SIM: 20-25% of 3rd-largest operator req.; SIM util ~40% | current | concall L33/62 | building (trigger 4 borderline) |
| Deploy Rs 136.1 Cr IPO manufacturing-capex earmark; watch PPE/commissioning | none stated | Note 2 l.603/998; concall L26 | underway (Rs 6.7-6.77 Cr this qtr) |
| Deploy Rs 32.1 Cr IPO general-corporate earmark | none stated | Note 2 l.608/1002; concall L26 (13.7 Cr) | underway |
| Rs 300 Cr IPO debt repayment | delivered | Note 2 l.606/1000 | completed (tailwind exhausted) |
| Net cash ~Rs 369 Cr at 30-Jun-2026 (deck + concall, unaudited) vs Notion Rs 339 Cr base | 30-Jun-2026 | deck l.950-951; concall L26 | disclosed (verify at Q2 BS) |
| Europe/Africa payment-card exports — revenue contribution | "nascent" | deck slide 12 l.332; concall L47 | commenced (unsized) |
| 3 multi-year tenders (1 Payments, 2 CFS PSU banks); PSU value Rs 73 Cr over tender period | won Q1FY27 | deck l.330/367; concall L15 | won (annualise) |
| Largest-retailer RFID volume — quantification / named anchor | pending | deck slide 14 l.397; concall L21 | early stage (unquantified) |
| eSIM commercial launch date / first revenue | slipped; watch vs Q2FY28 tripwire | deck l.421; concall L21 | pending (no date) |
| Gautam Jain (WTD) future participation | next call | concall L12 | silent this call |
| Promoter lock-in expiry — OFS watch (60-day window) | 30-Sep-2026 | Notion thesis | pending |
| Annual Report — verify actuarial assumption change (F9) & FVTOCI equity line (F1) | FY27 AR | l.450/453-454 | to verify |
| Q2FY27 half-yearly filing — Balance Sheet + Cash Flow mandatory (resolves cash-conversion INDETERMINATE, receivable/inventory days; tests the WC build) | Q2FY27 (Reg 33 H1) | protocol Step 5; concall L82 | awaited |

---

## 9. PROTOCOL VERDICT (v1.2 verdict set) — RE-STATED WITH CONCALL

**VERDICT: PROCEED WITH FLAGS.** *(unchanged from the A5-verified Role 4 pass; the
concall adds flags and information but does not fire any pre-committed trigger that
would change the Decision Status.)*

Reasons:
- **Numbers are reliable to rely on:** unmodified/unqualified Limited Review
  opinion both C and S; no Emphasis of Matter, no Going Concern; A2 ledger
  reconciled 100% across results, presentation AND concall (gate_a2/gate_a3 pass
  on all three). **The concall CONFIRMS every filing headline number** (Section
  5.9 7A) — no narrative-vs-filing numeric conflict. Company quality never halts a
  run — flags propagate, the operator decides.
- **FLAGS surfaced (filing + concall):** (1) **EBITDA margin breach** — 25.1%
  reported / 23.2% operating, both < 27% (#2), confirmed on the call; (2)
  **Payments two consecutive QoQ declines** (#14), +5% YoY, 10-12% guide needs an
  H2 ramp; (3) **earnings quality** — PAT +63.8% flattered by finance-cost
  collapse (management concedes, L26), ETR normalisation and +203% Other Income;
  core PBT ex-OI up only +41.9%; **PAT margin 16.0% below management's own FY26
  16.7%** (BEAR-1); (4) **gross margin −286 bps**, sized on the call (COMC +411
  bps, 40-45% FX-driven, L26/37); (5) **segment data unaudited** — single
  statutory segment; (6) **C-minus-S PAT sign-flip** to −Rs 1.41 Cr with ~Rs 1.3
  Cr unexplained eliminations; (7) **CONCALL-ADDED flags:** the **8-12% FY guide
  implies a sharp YoY deceleration** (only +4-10% YoY over the remaining 9M vs
  +21.1% Q1) and is SOFT/below run-rate (A3-01); the **FY27 margin number was
  refused three times** at the decision quarter (A3-02); **IoT decelerates**
  sharply from +145% to a +45% guide (A3-03); a **deliberate chip-inventory build
  consumes cash** (A3-13, adverse to conversion); **Gautam Jain (WTD) silent** —
  governance negative (A3-09); and **eSIM/RFID remain undated/unquantified** at
  the gate (A3-10/11).
- **Cash conversion is INDETERMINATE — and the concall makes the cap MORE
  binding.** No Cash Flow Statement this quarter; CFO, CFO/PAT, receivable days,
  inventory days, payable days, cash-conversion cycle all ND. Net cash IS
  disclosed (unaudited) at ~Rs 369 Cr (deck + concall, incl ~Rs 170 Cr unutilised
  IPO), broadly consistent with the Notion Rs 339 Cr base — but a disclosed
  balance is not a conversion reading, and the concall CONFIRMS a **deliberate WC
  / inventory build** (L82) that consumes cash. Per house rule the INDETERMINATE
  reading independently caps at PROCEED WITH CAVEATS with the evidence named; that
  cap is **subsumed by the more severe PROCEED WITH FLAGS**, and the concall's
  confirmation of an adverse WC direction reinforces (does not relieve) it.
  Resolves at the Q2FY27 half-yearly filing (Reg 33 H1 Balance Sheet + Cash Flow).
- **Decision Status is UNCHANGED — HELD, 4% at Rs 287.** No thesis-broken
  condition has fired. The re-engagement rule (5+ favourable) is NOT met (2 clean
  favourable, one unaudited; #4 borderline, #7 partial). The hard-kill rule is NOT
  mechanically met (no pledge; only #14 an unambiguous negative under the strict
  8/14 clause), though the adverse cluster WIDENED with the concall (2 breaches +
  1 confirmed governance negative + 2 adverse-informed WC items + 3 re-confirmed
  gate silences). **The concall DID materially change one gate input:** the FY27
  gate tally moved from **1 of 4** clearly met to **~1.5-2 of 4** because a
  REVENUE guide (8-12%) is now provided (criterion 4 upgraded NOT-MET → soft/
  PARTIAL MET); the EBITDA criterion still fails, Payments is marginal, and **the
  8-12% figure is soft vs the Q1 +21.1% run-rate** (satisfied by the Q1 print
  alone), so the improvement is thin. **A4 flags; the operator decides** on the
  gate and on any trim/hold/upgrade. No pre-committed trigger formally fired, so
  A4 does not alter the Decision Status.

**Position branch:** 8A (HELD). **Decision Status verified:** HELD (Notion page ts
2026-06-16). **Cash conversion:** INDETERMINATE (concall-adverse). **Management
credibility (Role 5):** grade not yet computable (first Role 5; provisional
MEASURED-leaning archetype — conservative revenue guide, margin withheld; begin
tracking). **Net concall impact on thesis: MAINTAINED-to-slightly-WEAKENED** —
confirmed all filing numbers and a datable Bengaluru catalyst, but added a
deceleration guide, a margin refusal, an IoT fade and a confirmed cash-consuming
WC build. **Single cleanest metric for Q2FY27:** *Core operating PBT ex-Other
Income* (bull: > Rs 80 Cr with gross margin recovering toward 44%; bear: < Rs 70
Cr with gross margin still < 42%), read alongside the **first CFO/PAT reading**
from the mandatory H1 Cash Flow, which resolves the INDETERMINATE cap and tests
the confirmed inventory build.

---

*Reviewed 2026-07-25 (Role 5 upgrade) | base Role 4 2026-07-24 | Sources:
results_styl_q1fy27.pdf (Reg 33, 12 pp) + Investor Presentation Q1FY27 (32
slides) + Q1FY27 concall transcript (ASR-normalised, 89 lines / 58 turns). Role 4
+ Role 5 complete merged review.*

```yaml
stage: A4-analyst
company: "STYL"
quarter: "q1fy27"
model: claude-opus-4-8
status: complete
docs_merged: [results, concall, presentation]
role5_active: true
ledger_reconciliation:
  notes: 12
  turns: 58
  slides: 32
  questions: 19
  analyst_firms: 7
  mgmt_numbers: 59
  all_reviewed: true
  a3_findings_incorporated: [F1-01, F2-01, F6-01, F7-01, F8-01, F9-01, F12-01, F14-01, X1, X2, X3, X4, pres-F1, pres-F6, pres-F8, pres-F14, pres-F16a, pres-F16b, pres-F16c, pres-F16d, A3-01, A3-02, A3-03, A3-04, A3-05, A3-06, A3-07, A3-08, A3-09, A3-10, A3-11, A3-12, A3-13, A3-14, A3-15]
protocol_verdict: "PROCEED WITH FLAGS"
cash_conversion: "INDETERMINATE"
decision_status_verified: "HELD 4% at Rs 287 (Notion page ts 2026-06-16)"
position_branch: "8A"
a5_fixes_applied:
  - "ARI-1: Q4FY26 gross profit 190.66 -> 189.65 Cr (Rev 404.18 - net materials 214.53; deck 1,897 Mn = 189.7 Cr, pres L445); Q4FY26 GM 46.9% unchanged"
  - "BEAR-1: added Q1FY27 PAT margin 16.0% BELOW FY26 16.7% (pres L529-532) to Section 3 + QfM"
  - "COV-1: net cash ~Rs 369 Cr disclosed unaudited (deck L950-951 / concall L26); cash CONVERSION still INDETERMINATE (no BS/CF)"
role5_summary:
  lead_finding: "A3-01: FY27 revenue guide 8-12% (concall L23/31) vs Q1 +21.1% => implied 9M remaining +4-10% YoY = sharp YoY deceleration; guide soft/below run-rate"
  margin_guidance: "WITHHELD 3x under 3-analyst pressure (A3-02, L31/39/45); trigger 7 PARTIAL"
  credibility_ratio: "not computable (first Role 5; no prior log)"
  management_archetype: "provisional MEASURED-leaning (conservative revenue guide, margin refused)"
  mgmt_absence: "Gautam Jain WTD introduced (L12) but silent; trigger 13 CONFIRMED-NEGATIVE"
  peer_cross_check: "N/A - no peer concall in the analysed universe within +/-4 weeks this pass"
  net_thesis_impact: "MAINTAINED to slightly WEAKENED"
trigger_scorecard_tally:
  fired_favourably: ["#1", "#3(unaudited)"]
  borderline_met: ["#4"]
  partial: ["#7", "#9"]
  breached: ["#2", "#14"]
  confirmed_negative: ["#13"]
  addressed_adverse: ["#5", "#15"]
  silent: ["#6", "#8", "#10", "#11", "#12"]
  re_engagement_5plus: "NOT met (2 clean favourable)"
  hard_kill: "NOT mechanically met (no pledge; only #14 clear negative); adverse cluster widened"
decision_gate_score:
  iot_gt_55cr: "MET (unaudited ~Rs 67.4 Cr)"
  ebitda_gt_26pct: "NOT MET (25.1% reported / 23.2% operating)"
  payments_yoy_stable: "MARGINAL (+5% YoY, 10-12% guide, 2 QoQ declines)"
  fy27_guidance_provided: "PARTIAL / soft-MET (revenue 8-12% given; margin withheld)"
  count: "~1.5-2 of 4 (was 1 of 4 pre-concall); mover = revenue guide, which is soft vs +21.1% Q1"
sc_gap_pat_pct:
  - {period: "Q1FY27", c_pat_cr: 60.34, s_pat_cr: 61.75, gap_cr: -1.41, gap_pct_of_standalone: -2.28}
  - {period: "Q1FY26", c_pat_cr: 36.84, s_pat_cr: 36.68, gap_cr: 0.16, gap_pct_of_standalone: 0.44}
  - {period: "FY26", c_pat_cr: 240.01, s_pat_cr: 243.74, gap_cr: -3.73, gap_pct_of_standalone: -1.53}
questions_for_management:
  - {q: "8-12% FY guide vs +21.1% Q1 => implied +4-10% YoY 9M: genuine slowdown, order timing, or conservative guide?", from_finding_id: "A3-01"}
  - {q: "FY27 EBITDA/PAT margin range and whether PAT margin exceeds FY26 16.7% (refused 3x)", from_finding_id: "A3-02/BEAR-1/F7-01/X2"}
  - {q: "Payments +5% Q1 vs 10-12% guide: H2 ramp and did Payments decline QoQ?", from_finding_id: "A3-05/trigger14"}
  - {q: "IoT absolute H2 run-rate underwriting +145% Q1 vs +45% guide; mix past 18%?", from_finding_id: "A3-03"}
  - {q: "Annualised revenue/timing of Rs 73 Cr PSU tenders; reconcile vs deck 3 tenders", from_finding_id: "A3-08/pres-F6"}
  - {q: "Top-10 concentration 56% (concall) vs 73% (deck) basis; new-logo pipeline given >95% existing", from_finding_id: "A3-06"}
  - {q: "eSIM commercial date / first revenue (no date given; ~9-mo slip)", from_finding_id: "A3-10/trigger8"}
  - {q: "RFID named anchor customer and volume (still early stage/pilots)", from_finding_id: "A3-11/trigger9/pres-F6"}
  - {q: "Bengaluru FY27 token + FY28 revenue quantification and tied capex within 140-160 Cr/yr", from_finding_id: "A3-14"}
  - {q: "Chip-inventory build WC-days increase, cash tied up, receivable/inventory days, CFO/PAT this quarter", from_finding_id: "A3-13/triggers5/6/15/COV-1"}
  - {q: "Insurance client count 13->10 churn: quantify churned-account revenue, confirm no retender loss", from_finding_id: "A3-07"}
  - {q: "Gautam Jain (WTD) operating remit and future-call participation", from_finding_id: "A3-09/trigger13"}
  - {q: "Rupee/chip assumption underlying 8-12% guide; margin sensitivity to chip/FX up-move", from_finding_id: "A3-15"}
  - {q: "Repeatable PAT growth ex finance-cost and ETR tailwinds", from_finding_id: "F8-01/pres-F8/pres-F1/X3"}
  - {q: "Other Income +203% source and recurrence", from_finding_id: "X2/pres-F16b"}
  - {q: "C-minus-S PAT sign-flip; ~Rs 1.3 Cr unexplained eliminations", from_finding_id: "F2-01"}
  - {q: "Rs 136.1 Cr manufacturing-capex deployment schedule and commissioning", from_finding_id: "F6-01"}
  - {q: "Actuarial OCI gain exceeding full prior year — assumption change?", from_finding_id: "F9-01"}
  - {q: "Slide-10 FY26 15,583 vs filing 14,411 — 3-yr revenue flat/declining?", from_finding_id: "pres-F16a/X1"}
  - {q: "Any receivables-factoring facility this year?", from_finding_id: "trigger12"}
  - {q: "Lock-in expiry 30-Sep-2026 — OFS within 60 days; pledge 0%?", from_finding_id: "triggers10/11"}
  - {q: "FY27 revenue contribution/timing of Europe/Africa card exports", from_finding_id: "pres-F6"}
answered_on_concall:
  - {q: "SIM utilization vs prior ~30%", status: "ANSWERED ~40% (L62); retire, monitor trajectory", from_finding_id: "trigger4"}
  - {q: "FY27 revenue guidance", status: "ANSWERED 8-12% (L23/31); soft vs +21.1% run-rate", from_finding_id: "trigger7"}
monitorables:
  - {item: "FY27 revenue 8-12% guide vs +21.1% Q1 run-rate (deceleration test)", implied_date: "FY27", source_ref: "concall L23/31"}
  - {item: "FY27 EBITDA/PAT margin number (withheld; watch)", implied_date: "FY27", source_ref: "concall L31/39/45"}
  - {item: "IoT ~45% FY27 / 35-40% FY28, mix 15-18% (decelerating from +145% Q1)", implied_date: "FY27-FY28", source_ref: "concall L53/68"}
  - {item: "Payments 10-12% (needs H2 ramp; +5% Q1)", implied_date: "FY27", source_ref: "concall L17/55"}
  - {item: "Bengaluru metal-card greenfield operational; certification Q4FY27", implied_date: "end-CY2026", source_ref: "concall L15/37"}
  - {item: "Bengaluru meaningful revenue (token FY27)", implied_date: "FY28", source_ref: "concall L72/74"}
  - {item: "Capex Rs 140-160 Cr/yr reaffirmed", implied_date: "FY27", source_ref: "concall L37"}
  - {item: "Chip-inventory build / WC-days increase (adverse to cash conversion) — quantify", implied_date: "ongoing", source_ref: "concall L82"}
  - {item: "SIM 20-25% of 3rd-largest operator req.; SIM util ~40%", implied_date: "current", source_ref: "concall L33/62"}
  - {item: "Net cash ~Rs 369 Cr at 30-Jun-2026 (deck+concall, unaudited) vs Notion Rs 339 Cr — verify at Q2 BS", implied_date: "2026-06-30", source_ref: "deck l.950-951 / concall L26"}
  - {item: "eSIM commercial launch date vs Q2FY28 tripwire", implied_date: "pending", source_ref: "deck l.421 / concall L21"}
  - {item: "Largest-retailer RFID volume / named anchor", implied_date: "pending", source_ref: "deck l.397 / concall L21"}
  - {item: "Gautam Jain (WTD) future participation", implied_date: "next call", source_ref: "concall L12"}
  - {item: "Promoter lock-in expiry OFS watch (60-day window)", implied_date: "2026-09-30", source_ref: "Notion thesis"}
  - {item: "Q2FY27 half-yearly Balance Sheet + Cash Flow (resolves cash-conversion INDETERMINATE; tests WC build)", implied_date: "Q2FY27", source_ref: "Reg 33 H1 / protocol Step 5"}
  - {item: "Annual Report — verify actuarial assumption change and FVTOCI equity line", implied_date: "FY27 AR", source_ref: "l.450/453-454"}
flags:
  - "EBITDA margin BREACH: 25.1% reported / 23.2% operating, both < 27% trigger (#2); concall confirms 25.1% (L26)"
  - "Payments two consecutive QoQ declines (#14); concall +5% YoY, 10-12% guide needs H2 ramp"
  - "CONCALL LEAD: FY27 revenue guide 8-12% (L23/31) implies sharp YoY deceleration (+4-10% 9M vs +21.1% Q1); guide soft/below run-rate (A3-01)"
  - "FY27 margin number REFUSED 3x at the decision quarter (A3-02, L31/39/45); trigger 7 PARTIAL"
  - "IoT decelerates: +145% Q1 vs +45% FY27 guide / 35-40% FY28; mix flat 15-18% (A3-03)"
  - "Deliberate chip-inventory BUILD consumes cash (A3-13, L82); reinforces INDETERMINATE cash-conversion cap"
  - "Gautam Jain (WTD) introduced but SILENT; trigger 13 CONFIRMED-NEGATIVE (A3-09)"
  - "eSIM undated / RFID unquantified at the pre-committed gate (A3-10/11)"
  - "PAT +63.8% flattered by finance-cost collapse (mgmt concedes L26) + ETR + Other Income +203%; core PBT ex-OI +41.9%"
  - "PAT margin 16.0% BELOW management's own FY26 16.7% (BEAR-1)"
  - "Top-10 concentration 56% (concall L26) vs deck ~73% — basis reconciliation needed (A3-06)"
  - "Segment data unaudited: single statutory segment; C-minus-S PAT sign-flip -Rs 1.41 Cr; ~Rs 1.3 Cr unexplained eliminations"
  - "Cash CONVERSION INDETERMINATE: no Cash Flow (net cash ~Rs 369 Cr disclosed unaudited); WC build adverse"
  - "Re-engagement rule NOT met (2 clean favourable); hard-kill NOT mechanically met (no pledge); gate ~1.5-2 of 4 (was 1 of 4), mover = soft revenue guide"
  - "Decision Status UNCHANGED (HELD); no pre-committed trigger formally fired; operator decides"
review_path: "/home/user/inflection-pipeline/runs/styl-q1fy27/work/review_styl_q1fy27.md"
```
