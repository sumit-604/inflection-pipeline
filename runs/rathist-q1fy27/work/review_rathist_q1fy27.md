# Q1 FY27 — COMPLETE QUARTERLY REVIEW (MERGED) — Rathi Steel and Power Ltd (RATHIST, BSE 504903)

Agent: A4 ANALYST | Model: claude-opus-4-8 | Review date: 2026-08-13
Protocols executed: Role 4 (Quarterly Results Review Protocol v1.2) in full step sequence; Role 5 (Quarterly Concall Analysis Protocol v1.1) = NOT APPLICABLE THIS RUN (no concall transcript filed/supplied).
Documents merged: `results` (Reg 30/33 Board Outcome + Limited Review Report + Unaudited Standalone Financial Results + Notes) and `presentation` (Reg 30 press release / media release). No concall.
Unit convention: statutory filing in Rs. Lakhs (l.183); press release in Rs. Cr (PR L87). Conversion factor Lakhs -> Cr is x0.01. All analysis presented in Rs. Cr per protocol Step 0B; every cell anchored to its extract line (results extract line = "l.NNN"; press-release extract line = "PR L.NNN"), or the literal ND.

---

## LEDGER-RECONCILIATION PREAMBLE (contractual, before Step 1)

Results ledger (`ledger_results_rathist_q1fy27.txt`) contains 5 notes / 35 financial line items / 10 zero-standing rows / 5 board-outcome agenda items / 11 auditor paragraphs / 1 entity row. All reviewed. GATE A2 = pass (grep vs sweep matched on every category).

Press-release ledger (`ledger_presentation_rathist_q1fy27.txt`) contains 4 slides (physical pages) / 13 disclosure blocks / 18 table cells / 2 footnotes / 6 section headers / 23 non-table numeric claims / 6 forward-hedge phrases / 14 identifier items / 63 total line_items. All reviewed. GATE A2 = pass.

Concall ledger: NONE. Role 5 turns reviewed = 0 because Role 5 = NOT APPLICABLE THIS RUN (no transcript filed/supplied). No concall content is fabricated anywhere in this review.

A3 findings incorporated (all): from results forensics — A3-01, A3-02, A3-03, A3-04, A3-05, A3-06, A3-07, A3-08. From press-release forensics — F1-EXC, F6-FWD, F7-RM, F7-HDG, F10-DIL, F14-TYPO, F16-MARGIN, F16-MIX, F16-ASYM, F16-PROMO. Every FORWARD-SIGNAL and AMBIGUOUS finding is carried to the Questions-for-Management table and/or the Monitorables list below; no finding is left unprocessed.

No ledger row is unreviewed. Proceeding.

### OCR-reconciliation binding (applied before any cell was used)
- PBT/PAT Q1FY27 = **347.99 Lakhs (Rs 3.48 Cr)**, NOT the "341.99" printed at l.204 (OCR-reconciled). Confirmed three ways: (i) l.209 and l.213 both read 347.99; (ii) arithmetic Total Revenue 19,367.25 (l.190) − Total Expenses 19,019.26 (l.199) = 347.99; (iii) press-release PAT Rs 3.48 Cr (PR L91). Used as 347.99.
- Line 216 (OCI sub-line) is unrecoverable from the extract ("2 | n| | nw | i"). Marked **ND (reason: OCR-garbled beyond parsing; magnitude bounded by arithmetic — see Step 1 OCI note)**. Not estimated.
- Other cells reconstructed from garbled cells where the ledger flagged missing separators/decimals are marked "(OCR-reconciled)" at first use and are bound to the AUTHORITATIVE FIGURES supplied and cross-checked against the press release / arithmetic.

---

# SECTION A — RESULTS REVIEW (Role 4, v1.2)

## STEP 0 — PRE-FLIGHT

### 0A. Notion page / thesis baseline
**Decision Status = NONE ON FILE.** There is no Notion page, no `companies/RATHIST.md`, no prior thesis, no Gate-0 score, no Role 1 valuation, no four-pillar destination PE, no Bear/Base/Bull projections, no thesis-broken conditions, no monitoring checklist, and no promoter verdict for this name in the repository. Per the task framing this is a **FRESH MONITORING-INITIATION review**, not a held or watchlisted position. Consequently: Step 6 (variance vs projections, watchlist status, thesis-broken triggers, growth triggers) has no baseline to reconcile against and is reported as "no baseline on file" rather than left blank; Step 7 (four-pillar re-validation) cannot be run because no pillar values exist; Step 8 uses the **8A-W (non-held) branch** as an initiation view only. No HOLD/ADD/TRIM/EXIT language is used, because there is no position.

### 0B. Unit convention
Statutory filing: Rs. Lakhs (l.183, "(Rs. in Lacs)"). Press release: Rs. Cr (PR L87). Conversion Lakhs -> Cr = x0.01. Analysis in Rs. Cr.

### 0C. Share-count changes
Paid-up equity share capital 8,636.30 Lakhs unchanged across all four periods (l.218, OCR-reconciled from "863630/B,63630", face value Rs 5). Redeemable Preference Shares 889.40 Lakhs unchanged all four periods (l.219, face value Rs 10). Basic EPS = Diluted EPS in every period (0.40 / 0.86 / 0.22 / 1.49, l.222-223) — zero dilution spread in the statutory filing, no split/bonus/rights/QIP/buyback disclosed. NOTE the cross-document tension: press-release **Diluted EPS +81.82% (PR L93) lags PAT +84.56% (PR L91)**, which A3 (F10-DIL) reads as an implied ~1.5% share-count rise; the statutory filing shows Basic=Diluted and unchanged capital, so the lag is most likely EPS rounding to Rs 0.01 rather than real dilution, but it is carried as a Question for Management because no basic-EPS or share-count line appears in the press release to confirm.

### 0D. Notes extraction (mandatory, all 5 notes)

| Note # | Line(s) | Subject | What it says (1 sentence) | Rs Cr impact | Period | Comparability impact |
|---|---|---|---|---|---|---|
| 1 | l.237 | Single segment | Operations fall under a single segment, "Steel". | None | All | No segment reclassification; Step-12/segment forensics N.A. |
| 2 | l.238-240 | Approval + audit conclusion | Results reviewed by Audit Committee and approved by Board 13-Aug-2026; statutory auditors expressed an **unmodified conclusion**. | None | Q1FY27 | Clean limited-review conclusion (see auditor check below). |
| 3 | l.241 (marker displaced to "w" l.242) | No subsidiary/JV | Company has **no subsidiary, associate or joint venture** for the period. | None | All | **Standalone-only entity; NO consolidated statement exists in this filing** (see Standalone-vs-Consolidated treatment). GARBLE_SUSPECT on the note marker only, not the text. |
| 4 | l.247 (marker displaced to "»" l.248) | Regrouping | Prior-period figures re-grouped to be comparable where necessary. | None quantified | Comparatives | Generic regrouping note; no specific restatement quantified — monitor at FY26 AR. |
| 5 | l.253-257 (leading numeral absent) | Basis of preparation | Prepared per Ind AS (Sec 133, Companies Act 2013) and Reg 33 presentation/disclosure requirements. | None | All | Standard basis-of-preparation note. |

**Auditor opinion check:** Limited Review (SRE 2410), **UNMODIFIED conclusion** (l.144-156, l.240). One **Emphasis-of-Matter-class paragraph** at l.137-143: the Q4 FY26 (31-Mar-2026) column figures are the **balancing figures** between FY26 audited annuals and the 9M-FY26 reviewed YTD, i.e. the Q4 FY26 column is **derived, not independently reviewed** (A3-03). This is the standard Reg-33 balancing-figure disclosure — not a going-concern or adverse flag — but it means every QoQ comparison against Q4 FY26 rests on a lower-confidence, plug-prone column (directly relevant to the Q4 depreciation anomaly, A3-04). Governance data gaps noted at extraction: auditor **Firm Registration Number not legible** (l.160), **UDIN unparseable** (l.166), and the results-page **signatory name is absent** — only "Managing Director, DIN 00174146" appears (l.262-263), with no digital-signature timestamp (A3-08).

### 0E. Business type
**Standard operating business** (steel manufacturer). Steps 1 and 5 apply; the lender variant (1L/5L) does not.

STOP-gate cleared: Notion status verified (NONE ON FILE), units identified, share-count changes noted, all 5 notes extracted, auditor opinion verified (unmodified + EoM-class balancing-figure paragraph), business type stated.

---

## STEP 1 — DATA EXTRACTION TABLE (Rs Cr; line anchors to the Lakhs extract)

| Line Item | Q1 FY26 | Q4 FY26 | Q1 FY27 | FY26 | Source lines |
|---|---|---|---|---|---|
| Revenue from Operations | 155.29 | 244.44 | 193.41 | 716.05 | l.188 (Q4 & Q1FY26 OCR-reconciled sep.) |
| Other Income | 0.11 | 0.12 | 0.26 | 0.44 | l.189 (OCR-reconciled decimals) |
| Total Income | 155.40 | 244.57 | 193.67 | 716.49 | l.190 (clean values) |
| Cost of Materials Consumed | 128.80 | 210.82 | 160.75 | 584.24 | l.192 (Q4 & FY26 OCR-reconciled) |
| Purchase of stock-in-trade | 0.00 (nil) | 0.00 (nil) | 0.00 (nil) | 0.00 (nil) | l.193 (ZERO_STANDING) |
| Change in Inventories | (3.96) | (1.98) | 1.67 | (11.75) | l.194 (positive = drawdown/cost) |
| Employee Benefits Expense | 3.71 | 4.64 | 4.31 | 16.27 | l.195 (Q1FY26 OCR-reconciled) |
| Finance Costs | 1.75 | 1.67 | 2.09 | 7.42 | l.196 (clean) |
| Depreciation & Amortisation | 2.59 | 0.71 | 2.21 | 8.61 | l.197 (FY26 OCR-reconciled) |
| Other Expenses | 20.62 | 27.19 | 19.17 | 98.83 | l.198 (Q1FY27 OCR-reconciled) |
| Total Expenses | 153.52 | 237.12 | 190.19 | 703.63 | l.199 (Q1FY26 OCR-reconciled) |
| Profit Before Tax | 1.89 | 7.45 | **3.48** | 12.86 | l.204 = 347.99 (OCR-reconciled from "341.99"); confirmed l.209/l.213 |
| Tax Expense | 0.00 (nil) | 0.00 (nil) | 0.00 (nil) | 0.00 (nil) | l.205-208 (all NIL) |
| PAT | 1.89 | 7.45 | 3.48 | 12.86 | l.209, l.213 |
| Other Comprehensive Income | +0.13 | +0.10 | +0.13 | (0.80) | derived: TCI(l.217) − PAT(l.213); sub-line l.216 = **ND** |
| Total Comprehensive Income | 2.01 | 7.54 | 3.61 | 12.06 | l.217 (Q1FY26 & FY26 OCR-reconciled) |
| EPS (reported, Basic) | 0.22 | 0.86 | 0.40 | 1.49 | l.222 (OCR-reconciled) |
| EPS (reported, Diluted) | 0.22 | 0.86 | 0.40 | 1.49 | l.223 (Basic=Diluted) |
| EPS (share-adjusted) | 0.22 | 0.86 | 0.40 | 1.49 | no corporate action -> reported = adjusted |

OCI note: the single OCI sub-line at l.216 is unrecoverable (ND). Period OCI is derived by arithmetic from TCI − PAT: Q1FY27 360.78 − 347.99 = **+12.79 L (+0.13 Cr)**; Q4FY26 754.29 − 744.57 = +9.72 L; Q1FY26 201.39 − 188.55 = +12.84 L; FY26 1,206.21 − 1,286.49 = **−80.28 L (−0.80 Cr)**. The full-year OCI is negative while every shown quarter is positive — implied unshown Q2+Q3 FY26 OCI ≈ −102.8 L (A3-06); flagged for the FY26 AR.

Equity/capital (memo, from l.218-220): Paid-up equity capital 8,636.30 L (face Rs 5); Redeemable Preference Shares 889.40 L (face Rs 10); Reserves & Surplus 5,273.00 L (FY26 column only, l.220 — disclosed by convention only in the annual column). Implied net worth (equity + reserves) ≈ 13,909.30 L = Rs 139.09 Cr; the Rs 889.40 L redeemable prefs sit as a debt-like redemption claim on top.

### Derived metrics

| Derived Metric | Formula | Q1 FY26 | Q4 FY26 | Q1 FY27 | FY26 |
|---|---|---|---|---|---|
| Operating EBITDA (Rs Cr) | PBT + D + Finance − OI | 6.12 | 9.71 | **7.51** | 28.46 |
| Operating EBITDA Margin | Op EBITDA / Rev from Ops | 3.94% | 3.97% | **3.88%** | 3.97% |
| Reported EBITDA (Rs Cr) | PBT + D + Finance | 6.23 | 9.83 | **7.77** | 28.90 |
| Reported EBITDA Margin (on Total Income) | Rep EBITDA / Total Income | 4.01% | 4.02% | **4.01%** | 4.03% |
| Core PBT ex-Other Income (Rs Cr) | PBT − OI | 1.78 | 7.32 | 3.22 | 12.42 |
| Other Income / PBT | OI / PBT | 5.68% | 1.67% | 7.53% | 3.44% |
| Effective Tax Rate | Tax / PBT | 0.0% | 0.0% | 0.0% | 0.0% |
| PAT Margin (on Rev from Ops) | PAT / Rev from Ops | 1.21% | 3.05% | 1.80% | 1.80% |

Reconciliation checks: Reported EBITDA Q1FY27 = 347.99 + 220.70 + 208.70 = 777.39 L = **Rs 7.77 Cr** — matches the press-release EBITDA (PR L89) exactly, confirming the company's EBITDA definition **includes Other Income** (footnote PR L95, "EBIDTA includes other income"). Operating EBITDA (ex-OI) = 751.18 L = **Rs 7.51 Cr**. Both are presented per the non-negotiable operating-vs-reported rule. The company's stated 4.01% EBITDA margin is the reported (ex-OI-inclusive) figure on Total Income; operating EBITDA margin on revenue-from-operations is 3.88%.

STOP-gate cleared: every cell filled or ND.

---

## STEP 2 — Q1 YoY COMPARISON (Q1 FY27 vs Q1 FY26) — the most important step

| Metric | Q1 FY26 | Q1 FY27 | YoY % Change | Verdict |
|---|---|---|---|---|
| Revenue from Operations (Rs Cr) | 155.29 | 193.41 | **+24.55%** | Strong top-line growth |
| Operating EBITDA (Rs Cr) | 6.12 | 7.51 | +22.73% | Grew, but slightly below revenue |
| Operating EBITDA Margin | 3.94% | 3.88% | **−6 bps** | Essentially FLAT (small contraction) |
| Depreciation (Rs Cr) | 2.59 | 2.21 | −14.86% | Falling — flatters PBT |
| Finance Costs (Rs Cr) | 1.75 | 2.09 | +19.30% | Rising faster than revenue |
| EBIT (operating, = Op EBITDA − D) | 3.53 | 5.30 | +50.4% | Boosted by depreciation step-down |
| Other Income (Rs Cr) | 0.11 | 0.26 | +144.7% | Up sharply but tiny in absolute terms |
| **Core Operating PBT (PBT − OI)** | 1.78 | 3.22 | **+80.9%** | Real, but see decomposition |
| Reported PBT | 1.89 | 3.48 | +84.56% | Matches press release |
| PAT | 1.89 | 3.48 | +84.56% | Zero tax both periods |
| EPS (share-adjusted) | 0.22 | 0.40 | +81.82% | Rounding lag vs PAT (see 0C) |

**Six mandatory diagnostics:**
1. **Did revenue grow YoY?** Yes, +24.55% (Rs 155.29 Cr -> Rs 193.41 Cr). The press release attributes this to volume: total sales volume +29.76% YoY (21,864 -> 28,372 MT, PR L102). Revenue grew *slower* than volume, which arithmetically means **blended realisation fell ~4%** (Rs 71,076/MT -> Rs 68,260/MT). No company guidance exists to compare against (no Notion base case on file).
2. **Did operating EBITDA margin expand, contract or stay flat YoY?** Q1 FY27 operating margin of 3.88% vs Q1 FY26 of 3.94% = **−6 bps, effectively flat**. On the company's own reported (OI-inclusive) basis it is **exactly flat at 4.01%** (PR L90). Despite ~30% volume growth there was **no margin expansion** (A3 F16-MARGIN). Operating leverage did not convert to profitability.
3. **Did core operating PBT (ex-OI) grow YoY?** Yes, +80.9% (Rs 1.78 -> 3.22 Cr). Growth is largely real, but two non-volume tailwinds inflate it: the depreciation step-down (−Rs 0.39 Cr, +Rs 0.39 to PBT) and near-zero variable-margin headwind offset by a fall in other expenses. The headline +84.56% PAT growth is **not purely operating quality** — see Step 4.
4. **What drove the gap between core-operating-PBT growth (+80.9%) and reported PAT growth (+84.56%)?** Other Income change (+Rs 0.16 Cr) is the entire difference. Finance cost rose (+Rs 0.34 Cr, a drag), depreciation fell (+Rs 0.39 Cr, a boost), tax rate was 0% in both periods (no delta), no exceptional items (l.201, nil). The gap is small because Other Income is tiny; the more important point is that **below-EBITDA line items (lower depreciation, near-nil tax) magnified PAT growth relative to EBITDA growth** (EBITDA +24.83% vs PAT +84.56%, A3 F16-ASYM).
5. **Are D&A and finance costs scaling faster than revenue?** Depreciation is *falling* (−14.86% YoY) while revenue grew +24.55% — the opposite of a capex-absorption gap, but consistent with a maturing/near-fully-depreciated asset base or a useful-life revision (A3-04); this flatters current PAT and is not a durable earnings driver. Finance cost is rising +19.30% YoY, close to revenue growth, but rising against a static equity base and a standing Rs 889.40 L redeemable-preference claim (A3-07).
6. **Is Other Income concentration changing?** Other Income is immaterial (Rs 0.26 Cr, 7.5% of PBT) and not masking trajectory; no treasury-timing distortion. Stripping it leaves core PBT of Rs 3.22 Cr, still +80.9% YoY.

---

## STEP 3 — SEQUENTIAL QoQ TRAJECTORY

| Quarter | Revenue (Rs Cr) | Op EBITDA Margin | Core PBT ex-OI (Rs Cr) | PAT (Rs Cr) | One-offs flagged | QoQ run-rate |
|---|---|---|---|---|---|---|
| Q1 FY26 | 155.29 | 3.94% | 1.78 | 1.89 | none | base |
| Q4 FY26 | 244.44 | 3.97% | 7.32 | 7.45 | **Q4 depreciation plug 0.71 Cr vs ~2.65/qtr run-rate (A3-04); Q4 is a balancing-figure column (A3-03)** | peak |
| Q1 FY27 | 193.41 | 3.88% | 3.22 | 3.48 | none flagged | step-down from Q4 |

Only three quarters are available (no Q2/Q3 FY26 columns are disclosed in this filing; they exist only inside the FY26 annual aggregate). The 4-6 quarter sequence the protocol prefers cannot be built — flagged as a data limitation, not estimated.

**Diagnostics:**
- **Run-rate trajectory:** Q1 FY27 revenue (Rs 193.41 Cr) is **down 20.9% QoQ** from Q4 FY26 (Rs 244.44 Cr) but **up 24.6% YoY**. Steel is seasonal and Q4 is typically the strongest Indian construction-demand quarter, so a Q4 -> Q1 sequential dip is expected; the YoY comparison is the cleaner read.
- **One-off distortion:** Q4 FY26 is distorted two ways — it is the auditor-flagged **balancing-figure** column (A3-03, l.137-143), and its depreciation of Rs 0.71 Cr is a **year-end truing-up plug** roughly 73% below the ~Rs 2.65/qtr FY26 run-rate (implied Q2+Q3 FY26 depreciation = 8.61 − 2.59 − 0.71 = 5.31 Cr, ~2.65 each). Q4 FY26 PAT of Rs 7.45 Cr is therefore *flattered* by the depreciation reversal and should not be treated as a clean run-rate base.
- **Implied Q2 FY27 base rate to hold trajectory:** to sustain ~24% YoY, Q2 FY27 revenue must exceed the Q2 FY26 base (not separately disclosed here — a monitorable). On margin, the cleanest hold test is operating EBITDA margin at or above ~3.9% while realisation stabilises.

---

## STEP 4 — OPERATIONAL DECOMPOSITION (PAT bridge, Q1 FY26 -> Q1 FY27)

Reported PBT/PAT change = +Rs 159.44 L (+1.59 Cr), +84.56%. Zero tax both periods, so PBT change = PAT change. Line-item bridge (each expense increase reduces PBT):

| Component | YoY change (Rs L) | YoY change (Rs Cr) | Contribution to +159.44 L | Recurring? |
|---|---|---|---|---|
| Revenue from Operations | +3,811.61 | +38.12 | volume + price | Recurring |
| Cost of Materials Consumed | −3,194.66 (cost up) | −31.95 | consumed the revenue gain | Recurring |
| Change in Inventories | −562.75 (cost up: +167.02 vs −395.73) | −5.63 | inventory drawdown added cost | Recurring (WC swing) |
| Employee Benefits | −59.98 (cost up) | −0.60 | wage inflation/volume | Recurring |
| Other Expenses | +144.93 (cost down) | +1.45 | conversion/power efficiency | Recurring |
| Operating subtotal (EBIT ex-OI drivers) | +139.15 | +1.39 | — | Recurring |
| Other Income | +15.50 | +0.16 | treasury/misc | Non-recurring typically |
| Depreciation | +38.56 (fell) | +0.39 | **asset-base step-down** | Recurring post-capex, but declining (A3-04) |
| Finance Costs | −33.77 (rose) | −0.34 | rising leverage/interest | Recurring post-debt |
| Effective tax rate change | 0.00 | 0.00 | 0% both periods | — |
| Exceptional items | 0.00 | 0.00 | none (l.201) | Non-recurring — none |
| **Reported PAT YoY change** | **+159.44** | **+1.59** | 100% | — |

**Mandatory questions:**
- **% of YoY PAT change from recurring core operations vs non-recurring:** Operating drivers (revenue less variable/other costs) contributed +Rs 1.39 Cr (~87%); the depreciation step-down +Rs 0.39 Cr (~24%) and Other Income +Rs 0.16 Cr (~10%) are lower-quality/less-durable, partly offset by rising finance cost −Rs 0.34 Cr (−21%). Net: the operating core is genuine, but roughly a quarter of the PAT uplift rests on a **falling depreciation charge that will not repeat indefinitely**.
- **If Other Income reverts to prior-year level:** run-rate PAT falls by only ~Rs 0.16 Cr — immaterial. Other Income is not the story here.
- **D&A / finance-cost steady state:** Depreciation is *declining* (contrary to the usual post-capex ramp), so the steady state is lower, not higher — but that is a headwind masked as a tailwind: once the asset base is fully depreciated the flattering effect stops. Finance cost is rising and, with a Rs 889.40 L redeemable-preference redemption pending, likely steps up further.
- **Tax adjustments inflating/deflating PAT:** The single largest latent distortion. **ETR = 0% against a 25.17% statutory rate**, all four periods (A3-05). If normal tax applied to Q1 FY27 PBT of Rs 3.48 Cr, PAT would be ~Rs 2.60 Cr (a ~Rs 0.88 Cr / ~25% haircut). Normalising BOTH the tax (25.17%) and depreciation (back to the ~Rs 2.59 Cr Q1 run-rate) yields an indicative normalised PAT of ~Rs 2.32 Cr vs the reported Rs 3.48 Cr — i.e. roughly a third of headline PAT is tax-shield-plus-depreciation-driven, not durable.

---

## STEP 5 — CASH QUALITY & BALANCE SHEET

| Metric | Prior period | Current period | Change | Verdict |
|---|---|---|---|---|
| CFO | ND | ND | ND | Not in a Q1 filing |
| CFO/PAT ratio | ND | ND | ND | **INDETERMINATE** |
| Capex (PPE + CWIP) | ND | ND | ND | Not disclosed |
| FCF (CFO − Capex) | ND | ND | ND | Not computable |
| Working-capital change | ND | inventory drawdown +Rs 1.67 Cr (l.194) | partial | Only the P&L inventory line is visible |
| Receivable days | ND | ND | ND | No balance-sheet detail |
| Inventory days | ND | ND | ND | No balance-sheet detail |
| Payable days | ND | ND | ND | No balance-sheet detail |
| Cash Conversion Cycle | ND | ND | ND | Not computable |
| PPE | ND | ND | ND | Not disclosed (falling depreciation is the only proxy signal) |
| CWIP | ND | ND | ND | Not disclosed |
| Net Debt / (Net Cash) | ND | ND | ND | Rising finance cost implies non-trivial debt (A3-07), but no figure disclosed |
| Promoter Pledge | ND | ND | ND | Not disclosed in this filing |

**Cash-conversion verdict: INDETERMINATE.** Per Reg 33, cash flow statements and balance sheets are mandated **half-yearly** (at Q2 and Q4), not at Q1. This is a Q1 filing; **no cash flow statement and no balance-sheet detail beyond equity capital, redeemable prefs and (annual-only) reserves are disclosed**. CFO/PAT cannot be computed, so the Pillar-2 cash multiplier cannot be validated. **Per house rule, this INDETERMINATE cash conversion caps the verdict at PROCEED WITH CAVEATS and does NOT silently resolve to PROCEED.** Missing evidence named explicitly: (a) cash flow from operations for H1 FY27 (available at Q2 FY27, ~Nov 2026); (b) full balance sheet — receivables, inventory, payables, PPE, CWIP, gross/net debt; (c) promoter pledge disclosure; (d) FY26 audited cash flow statement in the annual report (~Sept 2026). The rising finance cost (+19.3% YoY) and the standing Rs 889.40 L redeemable-preference redemption claim make the cash/leverage picture a first-order monitorable, not a footnote.

---

## STANDALONE-vs-CONSOLIDATED GAP (first-class metric, from A3 F2)

**Finding, not a blank:** There is **no consolidated statement filed; the company declares no subsidiary/associate/JV (Note 3, l.241).** The mandatory standalone-vs-consolidated PAT-gap metric is therefore reported as: standalone PAT Q1FY27 Rs 3.48 Cr / Q4FY26 Rs 7.45 Cr / Q1FY26 Rs 1.89 Cr / FY26 Rs 12.86 Cr, with **consolidated = not applicable (no consolidated entity exists)**; SC-gap = N/A by structure, 0% by definition.

**Carry-forward caveat (A3-02):** the press release references a group-level narrative ("India's only stainless-steel wire rod manufacturer using direct billet charging technology", PR L160-162; promotional "leading player" framing) and there is a known group-level WOS/PLI-linked route in the operator's context that does NOT appear inside this listed standalone entity. **Any PLI-linked capex or revenue may sit off these standalone statements in a group WOS.** This is flagged as a live monitorable and converted to a Question for Management: whether PLI-linked capacity and its economics accrue to this listed entity or to an off-statement group subsidiary. Until answered, the standalone accounts may not capture the full group economics that a promotional narrative implies.

---

## STEP 6 — RECONCILIATION vs THESIS

**No baseline on file.** There is no Notion page, no Bear/Base/Bull projection set, no watchlist checklist, no thesis-broken conditions, and no growth-trigger register for RATHIST. Steps 6A-6D cannot be executed against a prior thesis and are reported as "no baseline; this review initiates the baseline." Consequences:
- **6A Variance vs projections:** no projections exist -> cannot classify Bear/Base/Bull. This quarter's actuals (Rev Rs 193.41 Cr, Op EBITDA margin 3.88%, PAT Rs 3.48 Cr, EPS Rs 0.40) become the first data point of a future baseline.
- **6B Watchlist status:** no checklist on file -> all rows UNKNOWN by absence; the Monitorables list below seeds a fresh checklist.
- **6C Thesis-broken triggers:** none defined -> none can fire. No exit logic applies.
- **6D Growth triggers:** none defined -> the press-release forward statements (scaling volumes, product-mix optimisation, cost discipline; RM-cost moderation outlook) are logged as candidate triggers to be formalised only after a Gate-0 / Role 1-2 workup.
- **Probability re-weighting rule:** not applicable (requires two consecutive quarters of below-bear misses against an existing scenario set; none exists).

---

## STEP 7 — FOUR-PILLAR DESTINATION PE RE-VALIDATION

**Cannot be run.** No four-pillar destination PE, no ROCE base, no cash/asset-quality multiplier, no growth-visibility or strategic premium, no UA multiplier, no sector cap, and no hurdle ratio exist in the repository for RATHIST (Section 1B v3.3 inputs were never set for this name). Re-validation presupposes an original set of pillar values from a Role 1 valuation, which has not been performed. **This is a prerequisite gap, not a re-validation:** before any position view, the enforced chain (Gate 0 -> Role 1 valuation -> Role 2 thesis -> Role 3 devil's advocate) must establish the pillars. Two forward inputs are logged for that future workup: (i) ROCE cannot be computed here because capital employed (net debt, PPE) is undisclosed; (ii) the exit multiple, if ever set, must come solely from Section 1B v3.3 per the NEVER rule — no round-number default.

---

## STEP 8 — POSITION DECISION (8A-W branch, non-held / initiation view)

**Decision Status verified: NONE ON FILE.** RATHIST is not held and not on a formal watchlist; the **8A-W (non-held) branch** applies. No trim/exit mechanics are relevant. The output of this branch is an **initiation view**, explicitly caveated.

**Initiation view:** The quarter is a clean, arithmetically reconciling set of numbers showing genuine volume-led top-line growth (+24.55% YoY) but **no margin expansion** (operating EBITDA margin flat/−6 bps; reported flat 4.01%), a **realisation decline of ~4%** driven by a **mix shift down** toward lower-value MS TMT rebar, and a PAT line **flattered by a falling depreciation charge and a 0% effective tax rate** that will not persist. This is a low-margin (~4% EBITDA), commodity-exposed secondary steel producer at a ~Rs 194 Cr quarterly-revenue / ~Rs 3.5 Cr quarterly-PAT scale. **No buy/entry recommendation is made**, because the prerequisites do not exist in the repository: **no Gate-0 score, no Role 1 valuation, no destination PE, no promoter/governance check, and no prior thesis.** Those must be completed before any entry-zone or position sizing is defined. The appropriate next step is to route RATHIST through Gate 0 -> Role 1/2/3, using this review as the numerical baseline.

### 8B. Add-back / trim trigger refinement
Not applicable — no position, no existing triggers. For the future baseline, the two cleanest disqualifiers to pre-commit are: (i) operating EBITDA margin falling below ~3.5% (mix-down becoming structural margin erosion); (ii) evidence that PLI-linked economics accrue off-statement to a group WOS rather than to this listed entity.

### 8C. Single cleanest metric for next quarter (Q2 FY27)
**Blended realisation per tonne (revenue-from-operations ÷ total volume), read jointly with the stainless/high-value volume share.** This is the cleanest test of whether the Q1 mix-down is structural. **Bull threshold:** blended realisation stabilises or recovers toward ~Rs 71,000/MT AND stainless/non-TMT volume stops falling (holds above ~9,700 MT), i.e. the TMT surge is additive, not cannibalising. **Bear threshold:** realisation falls further below ~Rs 68,000/MT with stainless volume continuing to decline — confirming capacity has been re-allocated to low-margin TMT and future margin mix compresses.

---

## STEP 8.5 — QUESTIONS FOR MANAGEMENT

Every A3 FORWARD-SIGNAL and AMBIGUOUS finding generates at least one question (channel: IR email / AGM — this is a BSE-listed secondary producer with no concall this quarter).

| # | Question | Why it matters | Bull answer | Bear answer | From finding |
|---|---|---|---|---|---|
| 1 | Total volume rose ~30% YoY but revenue only +24.6%, implying blended realisation fell ~4% (Rs 71,076 -> Rs 68,260/MT); stainless/non-TMT volume fell ~28.5% (13,569 -> 9,695 MT) while TMT rebar doubled to 65.8% of mix. Is the stainless-volume decline a deliberate capacity re-allocation to TMT, and what is the resulting blended-realisation and gross-margin trajectory for FY27? | Tests whether the "strengthened product mix" claim is real or a mix-DOWN that structurally compresses margin | Stainless is capacity-constrained/temporary; realisation recovers as mix rebalances; TMT is incremental | Stainless capacity permanently re-allocated to commodity TMT; realisation and margin structurally lower | F16-MIX |
| 2 | EBITDA margin was flat at 4.01% YoY despite ~30% volume growth and a stated raw-material-price moderation. Can you bridge, in bps, why operating leverage and lower input costs did not lift EBITDA margin? | Isolates whether flat margin is realisation pressure fully offsetting cost relief, or cost pass-through failure | RM relief is a Q2 tailwind not yet in Q1; margin expands next quarter | Realisation pressure structurally offsets any cost relief; margin stuck ~4% | F16-MARGIN, F7-RM, F7-HDG |
| 3 | Depreciation fell to Rs 0.71 Cr in Q4 FY26 (vs ~Rs 2.65 Cr/qtr run-rate) and to Rs 2.21 Cr in Q1 FY27 (−14.9% YoY). Was there a useful-life revision or asset-base maturation, and what is the expected quarterly depreciation run-rate for FY27? | The falling charge flatters PAT; a Q4 plug in a balancing-figure quarter needs explanation | Genuine asset maturation; low depreciation is durable and cash-accretive | Year-end truing-up plug distorting comparability; run-rate normalises up, cutting PAT | A3-04, A3-03, F16-ASYM |
| 4 | The effective tax rate has been 0% across all four periods (nil current, deferred and MAT) against a 25.17% statutory rate. What is the remaining quantum of brought-forward losses / unabsorbed depreciation / MAT credit, and in which year do you expect normal cash tax to begin? | Quantifies the latent ~25% PAT haircut and its timing — first-order to any forward earnings estimate | Large carryforward pool shields profits for several years; visibility is high | Carryforwards near exhaustion; ETR steps toward 25% within 1-2 years, cutting PAT ~25% | A3-05, F16-ASYM |
| 5 | Finance cost rose +19.3% YoY (Rs 1.75 -> 2.09 Cr) while the equity base was static, and Rs 8.89 Cr of Redeemable Preference Shares (face Rs 10) remain outstanding. What is the gross/net debt position, and what is the redemption schedule and funding plan for the preference shares? | Rising interest plus a standing redemption claim is a cash-call risk against a ~Rs 139 Cr net worth | Debt modest, prefs redeemable from internal accruals on a comfortable timeline | Leverage building; near-term pref redemption forces a refinancing or cash drain | A3-07 |
| 6 | FY26 full-year OCI was −Rs 0.80 Cr even though every disclosed quarter posted positive OCI, implying a ~−Rs 1.03 Cr swing in H1 FY26. What actuarial/remeasurement assumption change drove this, and is a recurring negative OCI drag expected? | Signals a mid-year assumption change (discount rate / plan-asset) that could recur | One-off remeasurement; assumptions now stable | Recurring actuarial drag understating comprehensive earnings | A3-06 |
| 7 | The company reports no subsidiary/associate/JV (Note 3), yet group narrative references a PLI/wholly-owned-subsidiary route. Will PLI-linked capacity, capex and revenue sit inside this listed standalone entity, or in a separate group entity outside these statements? | Determines whether the listed shareholder captures PLI economics or they accrue off-statement | PLI capex/revenue accrues to the listed entity; shareholders participate | PLI economics sit in an off-statement group WOS; listed entity is hollowed of the growth optionality | A3-02 |
| 8 | Press-release Diluted EPS grew 81.82% while PAT grew 84.56%, yet the statutory filing shows Basic = Diluted EPS and unchanged paid-up capital. Please confirm the exact share count and whether any ESOP, warrant or convertible instrument is outstanding. | Reconciles the implied ~1.5% share-count lag; tests for hidden dilution | Pure rounding artifact; no dilutive instrument; share count static | Undisclosed dilutive instrument or issuance not visible in the filing | F10-DIL |
| 9 | The Limited Review Report omits a legible Firm Registration Number (l.160) and a parseable UDIN (l.166), the results page carries no signatory name (only DIN 00174146), and the Q1 FY26 PBT cell shows an undefined asterisk with no footnote. Please provide the auditor FRN and UDIN and confirm the results-page signatory. | Governance/disclosure-rigour signal on a promotional release | Clean administrative gaps attributable to OCR/scan; full particulars provided on request | Pattern of low-rigour disclosure; particulars not readily furnished | A3-08 |

**Top 3 by likelihood of producing thesis-changing information:**
1. **Q4 (0% ETR / carryforward quantum and tax-normalisation year)** — the single largest swing factor for forward PAT; a near-exhausted pool would cut normalised earnings ~25% (confirms bear).
2. **Q1 (stainless mix-down structural or temporary)** — resolves whether the growth story is quality (mix up) or commodity volume at falling realisation (bull vs bear on margin durability).
3. **Q7 (PLI/WOS on- or off-statement)** — tests where the forward growth optionality actually accrues; an off-statement answer materially changes what a listed shareholder is buying (transparency test).

**Channel recommendation:** IR email / AGM letter. No concall was hosted this quarter; RATHIST is a small secondary producer that does not appear to run analyst calls. Submit all nine questions verbatim by IR email now, and raise the top three at the next AGM Q&A if unanswered. Pre-commit these as watchpoints for the Q2 FY27 review.

---

# SECTION B — CONCALL ANALYSIS (Role 5, v1.1)

**ROLE 5 = NOT APPLICABLE THIS RUN.** No concall transcript was filed or supplied for Q1 FY27. Per source discipline (Role 5 Step 0 and the non-negotiable that the actual transcript is the sole primary source), Role 5 does not run and no concall content is fabricated. Steps 1-9 of the concall protocol are marked N/A (no transcript). The second document merged into this review is the **Reg-30 press release (presentation-class)**, whose findings feed the Role 4 results review above (F1-EXC, F6-FWD, F7-RM, F7-HDG, F10-DIL, F14-TYPO, F16-MARGIN, F16-MIX, F16-ASYM, F16-PROMO). When a Q1 FY27 (or any) concall is later supplied, Role 5 should be run and appended here, and the promise-vs-delivery log begun from the press-release forward commitments logged in the Monitorables list below.

---

# SECTION C — COMBINED VERDICT

- **Filing-derived signals:** Revenue +24.55% YoY, clean numbers that reconcile in every direction (PBT bridge closes to +Rs 159.44 L; EBITDA bridge ties to the press release at Rs 7.77 Cr). But margin flat (operating 3.88%, reported 4.01%), realisation down ~4%, PAT flattered by falling depreciation and 0% tax. Auditor conclusion unmodified with a standard balancing-figure EoM on the Q4 FY26 column. Governance data gaps (FRN/UDIN/signatory).
- **Press-release-derived signals:** Promotional framing ("Strong Performance", "strengthened product mix") masks a **mix-DOWN** to lower-value TMT and a realisation decline management itself concedes ("softer steel realisations"). Forward commitments are all undated and unquantified. RM-cost moderation flagged as a Q2 tailwind.
- **Reconciliation:** Filing numbers and the press release are arithmetically consistent (EBITDA bridge, PAT, EPS all reconcile); the divergence is narrative, not numerical — the press release's positive spin overstates the *quality* of a quarter the filing shows to be volume-led, low-margin, and tax/depreciation-flattered. Filing wins on substance.
- **Net thesis impact:** No thesis exists to impact; this review **initiates the baseline**.
- **Position decision:** No position (Decision Status NONE ON FILE); initiation view only, no entry recommended pending Gate 0 -> Role 1/2/3.
- **Verdict: PROCEED WITH CAVEATS.** The numbers pass mechanically and reconcile, so nothing halts (no REWORK, no INSUFFICIENT EVIDENCE). But the verdict is **capped at PROCEED WITH CAVEATS by the INDETERMINATE cash conversion** (no CFO, no balance sheet in a Q1 filing) — it does not resolve to a clean PROCEED — with these caveats/flags named: (1) cash conversion INDETERMINATE, missing evidence listed in Step 5; (2) latent ~25% PAT haircut when the 0% ETR normalises; (3) PAT flattered by a falling/plugged depreciation charge; (4) ~4% realisation decline and a margin-dilutive mix-down sold as a mix-up; (5) rising finance cost plus a Rs 8.89 Cr redeemable-preference redemption cash-call; (6) governance/disclosure gaps (FRN/UDIN/signatory); (7) possible off-statement PLI/WOS economics; (8) full prerequisite chain (Gate 0, valuation, promoter check, thesis) absent from the repository.

---

## MONITORABLES / CATALYST LIST (with implied dates)

| # | Item | Implied date | Source ref |
|---|---|---|---|
| 1 | Raw-material cost path into Q2 FY27 — did the flagged moderation actually lower COGS and lift margin? | Q2 FY27 results, ~Nov 2026 | F7-RM (PR L140-141); l.192 |
| 2 | Blended realisation per tonne + stainless/high-value volume share (the single cleanest metric, Step 8C) | Q2 FY27 results, ~Nov 2026 | F16-MIX (PR L102-108) |
| 3 | Operating EBITDA margin — expansion vs stuck ~3.9% under volume growth | Q2 FY27 results, ~Nov 2026 | F16-MARGIN; derived Step 1 |
| 4 | Depreciation quarterly run-rate — normalisation up vs durable low charge | Q2 FY27 results, ~Nov 2026 | A3-04 (l.197) |
| 5 | Tax normalisation — remaining carryforward quantum and first year of cash tax | FY26 AR tax note ~Sept 2026; each quarter thereafter | A3-05 (l.205-208) |
| 6 | Preference-share redemption schedule + gross/net debt + rising finance cost | FY26 AR ~Sept 2026; H1 FY27 balance sheet at Q2 | A3-07 (l.196, l.219) |
| 7 | H1 FY27 cash flow statement + full balance sheet (resolves the INDETERMINATE cash conversion) | Q2 FY27 (Reg 33 half-yearly), ~Nov 2026 | Step 5 (Reg 33) |
| 8 | PLI/WOS structure — on-statement or off-statement capex/revenue | FY26 AR ~Sept 2026; IR response | A3-02 (l.241; PR L160-162) |
| 9 | FY26 Annual Report — OCI/actuarial assumption note, tax note, cash flow, promoter pledge, auditor FRN/UDIN | ~Sept 2026 | A3-06, A3-08 |
| 10 | Press-release forward commitments (scaling volumes, mix optimisation, cost discipline) — begin promise-vs-delivery log | tracked from Q2 FY27 | F6-FWD (PR L143-146) |

---

# PLAIN-LANGUAGE BRIEF (mandatory final section)

## 1. Summary narrative
Rathi Steel and Power grew revenue about 25% year on year in the June 2026 quarter, to roughly Rs 194 Cr, and reported profit after tax of Rs 3.48 Cr, up about 85% (this quarter's filing/press release). On the surface that looks strong. Underneath, the growth is almost entirely about selling more tonnes, not selling them better. Volume rose about 30% (to 28,372 MT) while revenue rose only about 25%, which means the average price per tonne actually fell around 4% (this quarter's press release). The reason is a shift in what they sold: cheaper MS TMT rebar more than doubled and now makes up about two-thirds of volume, while higher-value stainless products fell roughly 28% in tonnes. The press release calls this a "strengthened product mix"; the numbers show it is a mix-down. Profitability did not improve at all — EBITDA margin was flat at 4.01% both years (this quarter's press release), a thin margin typical of a commodity steel re-roller. The large jump in profit is partly real operating gain, but a meaningful chunk comes from two things that will not last: the depreciation charge fell about 15% year on year, and the company paid zero tax against a 25% statutory rate because of accumulated past losses (this quarter's filing). Strip those out and normalised profit is closer to Rs 2.3 Cr than Rs 3.5 Cr. Finance costs are rising, and there is Rs 8.89 Cr of redeemable preference shares that will eventually need cash to redeem (this quarter's filing). Critically, a June-quarter filing carries no cash flow statement and no balance sheet, so we cannot judge cash quality at all — that check is indeterminate and caps the verdict. There is no prior thesis, no valuation, and no Notion page for this company, so this is a fresh monitoring-initiation, not a buy call. Verdict: PROCEED WITH CAVEATS. Before any position, the company needs to go through Gate 0, valuation, and a promoter/governance check.

## 2. Sector intelligence
Rathi is a small secondary (non-integrated) steel producer in the Ghaziabad NCR cluster: about 85,000 tpa of melting and 200,000 tpa of rolling capacity, making stainless long products (billets, wire rods) and MS TMT rebar (this quarter's press release, PR L158-160). At roughly Rs 194 Cr of quarterly revenue it is a micro-cap in an industry dominated by integrated majors. The Indian long-steel/TMT market is intensely price-competitive and cyclical: realisations track the steel cycle and input costs (scrap, sponge iron, ferro-alloys, power), and secondary producers like this are price-takers with thin, volatile spreads — the flat ~4% EBITDA margin here is characteristic (sector knowledge, not in these docs). TMT rebar demand is driven by construction/infrastructure and is highly seasonal, with the March quarter usually strongest and the June quarter softer, which explains the ~21% sequential revenue dip from Q4 (this quarter's filing, trajectory). Management itself flags "softer steel realisations" and volatile energy/input costs, while pointing to recent raw-material-price moderation as a possible tailwind into Q2 (this quarter's press release, PR L137-141). The stainless wire-rod niche is described as differentiated ("direct billet charging technology") but that superlative is unverified from these documents (this quarter's press release, flagged unverifiable). There is a group-level PLI/subsidiary angle referenced outside these standalone accounts that could matter for future capacity but is not visible here (A3-02; operator context).

## 3. Business-model intelligence
The company makes money by converting steel inputs into long products and selling on tonnage at a thin conversion spread. Unit economics: at ~Rs 68,000/MT realisation and ~4% EBITDA margin, it earns roughly Rs 2,700 of EBITDA per tonne before interest, depreciation and tax (derived from this quarter's filing/press release). Cost of materials is ~83% of revenue (Rs 160.75 Cr on Rs 193.41 Cr), so the entire model lives or dies on the spread between input cost and realisation, and on keeping fixed costs (power, labour, interest) covered by volume (this quarter's filing). This quarter's model drift is the mix shift toward commodity TMT and away from higher-value stainless, which lifts tonnage but dilutes price and keeps margin flat — the opposite of moving up the value chain. Two accounting features currently flatter the reported model and will not persist: a declining depreciation charge (suggesting a maturing, largely-depreciated asset base) and a 0% effective tax rate from carried-forward losses (this quarter's filing; A3-04, A3-05). When either normalises, reported earnings quality steps down. The balance sheet is only partly visible (net worth ~Rs 139 Cr; Rs 8.89 Cr redeemable prefs; rising finance cost), and cash conversion is unmeasurable this quarter (this quarter's filing) — a real gap for a working-capital-heavy steel business.

## 4. Competition intelligence
This is thin and I will say so honestly: there is **no peer work, no Notion sector page, and no named-peer comparison set** in the repository for RATHIST (repository state). The press release names no competitors and offers only unverifiable self-description ("one of the leading players", "India's only stainless-steel wire rod manufacturer using direct billet charging technology") which I do not carry into analysis as fact (this quarter's press release, flagged unverifiable). From general sector structure: Rathi is a small NCR-regional secondary producer competing in TMT against far larger integrated and branded rebar players (Tata Tiscon, JSW, SAIL, and numerous regional secondary re-rollers) on price and local logistics, where it is structurally weaker on scale, cost, and brand; its potential edge is the specialised stainless-steel long-product/wire-rod niche where it claims a proprietary charging process (sector knowledge, not in these docs; company claim unverified). The competitive risk to watch is precisely this quarter's signal — if it is re-allocating capacity from its differentiated stainless niche into commodity TMT to chase volume, it is competing where it is weakest and diluting where it is strongest. Building an actual peer benchmark (realisation/MT, EBITDA/tonne, leverage vs comparable secondary producers) is a prerequisite for any thesis and does not yet exist.

---

```yaml
stage: A4-analyst
company: "RATHIST"
quarter: "Q1FY27"
model: claude-opus-4-8
status: complete
docs_merged: [results, presentation]
ledger_reconciliation:
  notes: 5
  turns: 0
  slides: 4
  all_reviewed: true
  a3_findings_incorporated: ["A3-01","A3-02","A3-03","A3-04","A3-05","A3-06","A3-07","A3-08","F1-EXC","F6-FWD","F7-RM","F7-HDG","F10-DIL","F14-TYPO","F16-MARGIN","F16-MIX","F16-ASYM","F16-PROMO"]
protocol_verdict: "PROCEED WITH CAVEATS"
cash_conversion: "INDETERMINATE"
decision_status_verified: "NONE ON FILE (fresh monitoring-initiation; not held, not watchlisted)"
position_branch: "8A-W"
sc_gap_pat_pct: ["Q1FY27: N/A (no consolidated entity; company declares no subsidiary/associate/JV, Note 3 l.241) = 0% by structure","Q4FY26: N/A","Q1FY26: N/A","FY26: N/A"]
questions_for_management:
  - {q: "Stainless volume fell ~28.5% while TMT doubled to 65.8% of mix and realisation fell ~4%; is the stainless decline structural capacity re-allocation and what is the FY27 margin path?", from_finding_id: "F16-MIX"}
  - {q: "EBITDA margin flat 4.01% YoY despite ~30% volume growth and RM moderation; bridge in bps why leverage and cost relief did not expand margin.", from_finding_id: "F16-MARGIN / F7-RM / F7-HDG"}
  - {q: "Depreciation fell to 0.71 Cr in Q4FY26 (vs ~2.65/qtr) and -14.9% YoY in Q1FY27; useful-life revision or maturation, and the FY27 run-rate?", from_finding_id: "A3-04 / A3-03 / F16-ASYM"}
  - {q: "0% ETR all four periods vs 25.17% statutory; remaining carryforward/MAT quantum and the year normal cash tax begins?", from_finding_id: "A3-05 / F16-ASYM"}
  - {q: "Finance cost +19.3% YoY with static equity and Rs 8.89 Cr redeemable prefs outstanding; gross/net debt and pref redemption schedule/funding?", from_finding_id: "A3-07"}
  - {q: "FY26 OCI -0.80 Cr despite positive quarters (~-1.03 Cr H1 swing); which actuarial/remeasurement assumption changed and is a recurring drag expected?", from_finding_id: "A3-06"}
  - {q: "No subsidiary/JV per Note 3 yet a group PLI/WOS route is referenced; will PLI capex/revenue sit in this listed entity or an off-statement group WOS?", from_finding_id: "A3-02"}
  - {q: "Diluted EPS +81.82% lags PAT +84.56% yet filing shows Basic=Diluted and unchanged capital; confirm share count and any ESOP/warrant/convertible.", from_finding_id: "F10-DIL"}
  - {q: "Auditor FRN illegible, UDIN unparseable, results-page signatory name absent, and an undefined asterisk on Q1FY26 PBT; provide FRN/UDIN and confirm signatory.", from_finding_id: "A3-08"}
monitorables:
  - {item: "Raw-material cost path into Q2FY27 (did moderation lower COGS/lift margin)", implied_date: "2026-11 (Q2FY27 results)", source_ref: "F7-RM PR L140-141; l.192"}
  - {item: "Blended realisation per tonne + stainless/high-value volume share (cleanest metric)", implied_date: "2026-11 (Q2FY27 results)", source_ref: "F16-MIX PR L102-108"}
  - {item: "Operating EBITDA margin expansion vs stuck ~3.9%", implied_date: "2026-11 (Q2FY27 results)", source_ref: "Step1 derived; F16-MARGIN"}
  - {item: "Depreciation quarterly run-rate normalisation", implied_date: "2026-11 (Q2FY27 results)", source_ref: "A3-04 l.197"}
  - {item: "Tax normalisation: carryforward quantum and first cash-tax year", implied_date: "2026-09 (FY26 AR) then quarterly", source_ref: "A3-05 l.205-208"}
  - {item: "Preference-share redemption schedule + gross/net debt", implied_date: "2026-09 (FY26 AR) / 2026-11 (H1 BS)", source_ref: "A3-07 l.196,l.219"}
  - {item: "H1FY27 cash flow + full balance sheet (resolves INDETERMINATE cash conversion)", implied_date: "2026-11 (Q2FY27, Reg 33 half-yearly)", source_ref: "Step5 Reg33"}
  - {item: "PLI/WOS on- vs off-statement capex/revenue", implied_date: "2026-09 (FY26 AR)/IR", source_ref: "A3-02 l.241; PR L160-162"}
  - {item: "FY26 AR: OCI/actuarial note, tax note, cash flow, promoter pledge, auditor FRN/UDIN", implied_date: "2026-09", source_ref: "A3-06; A3-08"}
  - {item: "Press-release forward commitments: begin promise-vs-delivery log", implied_date: "from 2026-11 (Q2FY27)", source_ref: "F6-FWD PR L143-146"}
flags:
  - "Cash conversion INDETERMINATE (no CFO/balance sheet in Q1 filing) — caps verdict at PROCEED WITH CAVEATS"
  - "Latent ~25% PAT haircut when 0% ETR normalises (A3-05)"
  - "PAT flattered by falling/plugged depreciation charge (A3-04, A3-03)"
  - "~4% realisation decline + margin-dilutive mix-down sold as mix-up (F16-MIX, F16-MARGIN)"
  - "Rising finance cost + Rs 8.89 Cr redeemable-preference redemption cash-call (A3-07)"
  - "Governance/disclosure gaps: auditor FRN/UDIN illegible, results-page signatory name absent (A3-08)"
  - "Possible off-statement PLI/WOS economics vs standalone-only entity (A3-02)"
  - "Prerequisites absent: no Gate-0, no valuation, no destination PE, no promoter check, no prior thesis"
  - "Role 5 NOT APPLICABLE — no concall filed/supplied"
plain_language_brief_included: true
review_path: "/home/user/inflection-pipeline/runs/rathist-q1fy27/work/review_rathist_q1fy27.md"
```
