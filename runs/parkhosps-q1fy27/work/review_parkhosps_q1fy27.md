# Q1 FY27 COMPLETE QUARTERLY REVIEW — Park Medi World Limited (PARKHOSPS)

Agent: A4 ANALYST | Protocols: Role 4 (Quarterly Results Review v1.2) + Role 5 (Concall Analysis v1.1) | Model: claude-opus-4-8 | Date: 2026-08-04 (Role 5 merge)
Documents merged: results (Reg 33 filing), presentation (investor deck), release (Reg 30 earnings release), monitoring (CRISIL Reg 32(6) IPO monitoring report), **concall (Q1 FY27 earnings-call transcript, 87 turns)**.
Role 5 status: **EXECUTED IN FULL this merge** — the Q1 FY27 concall transcript is now available and analysed under Role 5 v1.1 (Steps 0–8). This replaces the prior "N.A. — no concall" stub. Section A (Role 4) is preserved verbatim; Sections B, C, the Questions-for-Management table, the Monitorables list, the Plain-Language Brief and the closing YAML are rewritten to incorporate the call.

Unit convention across the four filing documents: **Rs Millions; x0.1 to reach Rs Crores.** The concall transcript speaks predominantly in **Rs Crores (x1)** with occasional Lakhs and unresolved garble shorthand ("K"/"KES"/"kles") preserved verbatim. Filing column order: Q1 FY27 | Q4 FY26 | Q1 FY26 | FY26 (full year). Every number below carries a line/turn anchor or the literal ND. No number is estimated.

---

## LEDGER-RECONCILIATION PREAMBLE (contractual, stated before Step 1)

**Filing ledgers (Role 4, unchanged):** across the four A2 filing ledgers — **results 22 notes** (10 standalone + 12 consolidated) / **presentation 26 slides** / **release 4 pages** / **monitoring 15 notes** — plus 63 results line items, 341 presentation number rows, 55 release table cells, 21 monitoring line items, 12 auditor paragraphs (results) + 19 (monitoring), 23 consolidation entities, and 5 board/agenda items. **All rows reviewed at their cited line numbers.** GATE A2 = pass on all four. GATE A3 = pass on all four (17/17 checks each).

**Concall ledger (Role 5, this merge):** Ledger contains **87 turns / 29 questions / 199 management numbers / 34 forward phrases / 6 hedges / 16 participants.** **All 87 turns and every ledger row reviewed at the cited extract line before any judgement.** GATE A1 = pass (87/87 lines, 100% coverage). GATE A2 = pass (six count-tests all match). GATE A3 = pass (17/17; blank checks: none).

A3 findings incorporated (namespaced by doctype to avoid ID collisions):
- **RES-** (results): RES-A3-01 … RES-A3-10.
- **PRES-** (presentation): PRES-A1 … PRES-A9.
- **REL-** (release): REL-FND-01 … REL-FND-07.
- **MON-** (monitoring): MON-A3-F1-01, MON-A3-F1-02, MON-A3-F6-01, MON-A3-F6-02, MON-A3-F7-01, MON-A3-F14-01.
- **FN-** (concall, NEW this merge): FN-01 … FN-24 (scorecard FINDING on F6, F7, F8, F10, F14, F17). Forward-signals: FN-01, FN-03, FN-04, FN-06, FN-07, FN-08, FN-09, FN-10, FN-11, FN-13, FN-17, FN-23. Ambiguous: FN-02, FN-05, FN-12, FN-14, FN-15, FN-19, FN-21, FN-24. Confirmatory-negative: FN-16, FN-20, FN-22.

No ledger row (filing or concall) is unreviewed; proceeding.

---

# SECTION A — RESULTS REVIEW (ROLE 4)

## STEP 0 — PRE-FLIGHT

**0A. Notion Decision Status (verified BEFORE any framing):** **WATCHLIST (AVOID at CMP). Position Size: None.** Entry zone Rs 101–126; MoS Rs 101. Promoter Verdict MONITOR. CMP per deck slide 25 = **Rs 292.55** (mcap Rs 12,636.14 Cr, line 1040/1043), far above the Rs 126 AVOID line — AVOID stance confirmed on price. This review uses the **8A-W (non-held / watchlist)** decision branch. No HOLD/ADD/TRIM/EXIT framing applies; there is no position.

**0B. Unit convention:** Rs Millions in all four docs; conversion factor x0.1 to Rs Crores (results header line 7-8; release header; presentation header; monitoring header).

**0C. Share-count changes:** Paid-up equity rose 768.80mn → 863.86mn (FV Rs 2) between Q1 FY26 and Q1 FY27 (results line 192/457) = the Dec-2025 IPO. Shares outstanding 431,930,864 as on 30-Jun-26 (deck line 1046). EPS therefore not comparable on a raw basis without noting the IPO base change (see PRES-A5 / REL-FND-04). **Methodological observation (not a trigger):** reported basic EPS 2.05 = total PAT 885.93 ÷ ~432m shares; owners-of-parent PAT is 825.07mn (line 446), which on the same share count gives ~1.91. The filing's EPS appears struck on **total** PAT (incl NCI) rather than owners' PAT — a minor overstatement of per-share earnings vs the Ind AS 33 owners basis. Consistent across Q1 FY26 (655.06/384.4m = 1.70). Flagged, not a tripwire.

**0D. Numbered-notes extraction (all 22, mandatory):**

| Note # (stmt) | Line | Subject | What it says (1 sentence) | Rs Cr impact | Period | Comparability impact |
|---|---|---|---|---|---|---|
| S3 / C3 | 223 / 486 | Panchkula launch | 350-bed greenfield hospital launched 10-Apr-2026 | Capex/ramp; qty ND | Q1 FY27+ | New-bed ramp drag on occupancy/parent costs |
| S4 | 228 | Palam Vihar +100 (Umkal) | +100 beds "Park Platinum", ~Rs 250mn internal accruals, by Nov-2026 | ~25 (planned) | Fwd | Forward capex commitment |
| C4 | 490 | Mohali 350→500 (RGS) | +150 beds, ~Rs 400mn internal accruals | ~40 (planned) | Fwd | Forward capex commitment |
| S5 / C5 | 233 / 497 | Healplus incorporated | New WOS of Park Medicenters, 20-May-2026, no ops yet | 0 (no ops) | Q1 FY27 | Omitted from entity list — RES-A3-10 |
| C6 | 501 | Devina Derma divested | 55% sold for Rs 0.60mn, completed 5-Jun-2026 | ~0.06 | Q1 FY27 | Mid-quarter deconsolidation; no exceptional line — RES-A3-01 |
| C7 | 506 | Segment | Single segment "Healthcare Service", one geography | n/a | All | No segment disaggregation to test |
| S7 / C8 | 245 / 519 | IPO utilisation | Rs 648.32mn still pending; medical-equipment head Rs 36.08 of 274.59 utilised | 64.83 pending | Q1 FY27 | Ties to monitoring report; MON findings |
| S8 / C9 | 264 / 537 | V3/Rudrapur (subsequent) | 80% acquired 31-Jul-2026, 330 beds, ~Rs 1,770mn; launched 2-Aug | 177 (100% val) | Post-period | Not in Q1 numbers; Q2 consolidation |
| S9 / C11 | 270 / 546 | Regrouping | Prior periods regrouped; rounding ignored | n/a | All | Standard |
| Board item 2 | 62 | Mehar-Zirakpur | Acquisition Rs 107 Cr, 150+ beds, 100% cash, completion 3-Dec-2026 | 107 | Post-period | Not in Q1 numbers |
| Board item 3 | 68 | IPO object variation | Postal-ballot notice to vary IPO objects | n/a | Fwd | RES-A3-08 — capital-allocation signal |

**Auditor opinion check:** **UNMODIFIED / unqualified** on BOTH standalone (para 4, line 126) and consolidated (para 6, line 328). No Going Concern paragraph in either report (confirmed absent, NOT FOUND — RES-A3-04). Two emphasis-of-matter-type paragraphs (not formally headed EoM): (i) Q4 FY26 figures are balancing figures (line 133/320); (ii) Q1 FY26 comparatives were **never subjected to limited review** (line 137/325). Consolidated para 7 (line 342) is an **Other-Matter-type reliance paragraph**: 19 subsidiaries reviewed by other auditors + 2 by Company management only = the SOUTHWEST-style unaudited-contribution flag (RES-A3-03, quantified in Step 4/6).

**0E. Business type:** **Standard operating business** (hospital operator). Steps 1 and 5 (not the lender variants 1L/5L) apply.

STOP cleared: Notion fetched & Decision Status verified; units identified; IPO share-count change noted; all 22 notes extracted; auditor opinion unmodified with two EoM-type + one Other-Matter paragraph; business type = standard.

---

## STEP 1 — DATA EXTRACTION TABLE (both statements, every cell anchored or ND)

### 1A. CONSOLIDATED P&L (Rs Millions; anchor = results line #)

| Line Item | Q1 FY26 | Q4 FY26 | Q1 FY27 | FY26 | Anchor |
|---|---:|---:|---:|---:|---|
| Revenue from Operations | 3,988.45 | 4,604.13 | 4,757.09 | 16,793.56 | L418 |
| Other Income | 68.72 | 75.03 | 76.46 | 316.09 | L419 |
| Total Income | 4,057.17 | 4,679.16 | 4,833.55 | 17,109.65 | L420 |
| Cost of Material/Service | 699.39 | 784.34 | 771.24 | 2,950.61 | L422 |
| Changes in Inventories | 0.80 | 11.91 | (8.67) | 7.45 | L423 |
| Employee Benefits | 767.79 | 861.64 | 924.07 | 3,233.97 | L424 |
| Professional & Consultancy | 603.22 | 716.20 | 756.05 | 2,570.74 | L425 |
| Finance Costs | 151.33 | 139.75 | 98.10 | 588.85 | L426 |
| Depreciation & Amortisation | 147.71 | 175.06 | 188.40 | 624.62 | L427 |
| Other Expenses | 867.94 | 956.35 | 1,053.52 | 3,587.57 | L428 |
| Total Expenses | 3,238.18 | 3,645.26 | 3,782.71 | 13,563.81 | L429 |
| Profit Before Tax | 818.99 | 1,033.90 | 1,050.84 | 3,545.84 | L430/432 |
| Current Tax | 167.48 | 197.42 | 260.98 | 822.45 | L434 |
| Deferred Tax (benefit) | (3.55) | 68.25 | (93.40) | (14.51) | L435 |
| Income tax prior years | - | 0.45 | (2.67) | 2.33 | L436 |
| Total Tax Expense | 163.93 | 266.12 | 164.91 | 810.27 | L437 |
| PAT (total) | 655.06 | 767.78 | 885.93 | 2,735.57 | L438/448 |
| — Owners of parent | 579.83 | 708.64 | 825.07 | 2,581.20 | L446 |
| — Non-controlling interest | 75.23 | 59.14 | 60.86 | 154.37 | L447 |
| EPS reported (Basic=Diluted, Rs) | 1.70 | 1.78 | 2.05 | 6.87 | L460/461 |
| EPS share-adjusted (Rs) | 1.70 | 1.78 | 2.05 | 6.87 | L460 (IPO base change noted 0C) |

### 1B. STANDALONE P&L (Rs Millions; anchor = results line #)

| Line Item | Q1 FY26 | Q4 FY26 | Q1 FY27 | FY26 | Anchor |
|---|---:|---:|---:|---:|---|
| Revenue from Operations | 229.69 | 274.34 | 335.32 | 1,289.65 | L165 |
| Other Income | 2.01 | 82.69 | 46.68 | 103.35 | L166 |
| Total Income | 231.70 | 357.03 | 382.00 | 1,393.00 | L167 |
| Cost of Material/Service | 31.27 | 34.58 | 54.19 | 157.62 | L169 |
| Changes in Inventories | (0.02) | - | (0.71) | (3.97) | L170 |
| Employee Benefits | 36.04 | 43.17 | 87.54 | 187.46 | L171 |
| Professional & Consultancy | 16.23 | 15.72 | 51.77 | 101.57 | L172 |
| Finance Costs | 32.98 | 24.20 | 8.60 | 127.55 | L173 |
| Depreciation & Amortisation | 11.61 | 10.10 | 33.81 | 45.09 | L174 |
| Other Expenses | 42.66 | 133.13 | 129.69 | 323.27 | L175 |
| Total Expenses | 170.77 | 260.90 | 364.89 | 938.59 | L176 |
| Profit Before Tax | 60.93 | 96.13 | 17.11 | 454.41 | L177/179 |
| Current Tax | 12.09 | 22.96 | 3.44 | 112.75 | L181 |
| Deferred Tax (charge/(benefit)) | (0.13) | (12.89) | 2.83 | (24.50) | L182 |
| Total Tax Expense | 11.96 | 10.07 | 6.27 | 88.25 | L184 |
| PAT | 48.97 | 86.06 | 10.84 | 366.16 | L185 |
| EPS (Basic=Diluted, Rs) | 0.13 | 0.20 | 0.03 | 0.92 | L195/196 |

### 1C. DERIVED METRICS

**Consolidated (Rs Millions unless %):**

| Derived Metric | Formula | Q1 FY26 | Q4 FY26 | Q1 FY27 | FY26 |
|---|---|---:|---:|---:|---:|
| Operating EBITDA (ex-OI) | PBT+D+Fin−OI | 1,049.31 | 1,273.68 | 1,260.88 | 4,443.22 |
| Operating EBITDA Margin | ÷Rev | 26.31% | 27.66% | 26.51% | 26.46% |
| Reported EBITDA (incl-OI) | PBT+D+Fin | 1,118.03 | 1,348.71 | 1,337.34 | 4,759.31 |
| Reported EBITDA Margin | ÷Rev | 28.03% | 29.29% | 28.11% | 28.34% |
| Core PBT (ex-OI) | PBT−OI | 750.27 | 958.87 | 974.38 | 3,229.75 |
| Other Income / PBT | OI÷PBT | 8.39% | 7.26% | 7.28% | 8.91% |
| Effective Tax Rate | Tax÷PBT | 20.02% | 25.74% | 15.69% | 22.85% |
| PAT Margin (on Rev) | PAT÷Rev | 16.42% | 16.68% | 18.62% | 16.29% |

Cross-checks tie to release table (line 1015-1029): EBITDA 1,261 mn / 26.5% / +20% YoY / -1% QoQ; margin +20bps YoY / -116bps QoQ. Confirmed.

**Standalone (Rs Millions unless %):**

| Derived Metric | Q1 FY26 | Q4 FY26 | Q1 FY27 | FY26 |
|---|---:|---:|---:|---:|
| Operating EBITDA (ex-OI) | 103.51 | 47.74 | 12.84 | 523.70 |
| Operating EBITDA Margin | 45.06% | 17.40% | 3.83% | 40.61% |
| Core PBT (ex-OI) | 58.92 | 13.44 | **(29.57)** | 351.06 |
| Other Income / PBT | 3.30% | 86.02% | **272.82%** | 22.74% |
| Effective Tax Rate | 19.63% | 10.48% | 36.64% | 19.42% |

**Standalone read:** core operating PBT ex-OI turned **negative (−29.57mn)** in Q1 FY27 from +58.92mn a year ago; reported standalone PBT of 17.11mn is entirely rescued by Other Income 46.68mn, which alone exceeds PBT (OI/PBT = 273%). Standalone operating EBITDA margin collapsed 45.06% → 3.83% YoY. This is RES-A3-02, treated as a first-class metric in Step 4.

STOP cleared: every cell filled or ND. No estimation.

---

## STEP 2 — Q1 FY27 YoY COMPARISON (the most important step)

### 2A. CONSOLIDATED YoY (Q1 FY27 vs Q1 FY26), Rs Millions

| Metric | Q1 FY26 | Q1 FY27 | YoY % | Verdict |
|---|---:|---:|---:|---|
| Revenue from Operations | 3,988.45 | 4,757.09 | +19.27% | Growth, bed-led |
| Operating EBITDA | 1,049.31 | 1,260.88 | +20.16% | In line w/ revenue |
| Op EBITDA Margin (pp) | 26.31% | 26.51% | +20 bps | Broadly flat |
| Depreciation | 147.71 | 188.40 | +27.55% | Scaling faster than revenue |
| Finance Costs | 151.33 | 98.10 | −35.18% | Post-IPO deleveraging |
| EBIT (operating, EBITDA−D) | 901.60 | 1,072.48 | +18.95% | Solid |
| Other Income | 68.72 | 76.46 | +11.26% | Flat-ish |
| **Core Operating PBT (PBT−OI)** | 750.27 | 974.38 | **+29.87%** | **Genuinely strong** |
| Reported PBT | 818.99 | 1,050.84 | +28.31% | Strong |
| PAT (total) | 655.06 | 885.93 | +35.24% | Flattered (see below) |
| EPS (reported) | 1.70 | 2.05 | +20.59% | Real per-share growth ~20% |

**Mandatory diagnostics (consolidated):**
1. **Revenue grew?** Yes, +19.27% YoY (Rs 3,988.45→4,757.09mn). Broadly at the Notion base-case pace (+18.5% FY27E). But growth is **bed-led, not utilisation-led**: capacity +32% YoY (3,000→3,960, deck line 111) while occupancy fell to 55.6% from 67.8% (−1,224 bps, line 112). Revenue grew slower than beds — the new beds are sub-scale.
2. **Op EBITDA margin?** Q1 FY27 26.51% vs Q1 FY26 26.31% = **+20 bps YoY** — essentially flat. Margin held DESPITE a 1,224 bps occupancy fall. Credible read: revenue is IPD-heavy (94.4% IPD, deck line 628) and new beds carry lower fixed-cost absorption but the mix/ARPOB is holding the blended margin; but margin resilience is unverifiable without same-store occupancy and ARPOB (both undisclosed — PRES-A9). Conservative stance: margin resilience is real at the reported level but the QoQ direction is down (Step 3).
3. **Core operating PBT (ex-OI) grew?** Yes, **+29.87%** — faster than revenue. This is the cleanest test and it PASSES: the operational core is genuinely expanding, not a treasury illusion. Reported PAT growth (+35%) exceeds core PBT growth (+30%), so the gap is non-operating (tax + finance cost).
4. **What drove the gap between core PBT +30% and PAT +35%?** Walk: Other Income +7.74mn; Finance cost −53.23mn (a benefit); Depreciation +40.69mn (a drag); Tax essentially flat (+0.98mn) despite PBT +231.85mn, because **ETR fell to 15.69% from 20.02%** on a Rs 93.40mn **deferred-tax benefit** (line 435). Each delta quantified in Step 4. The tax tailwind and the finance-cost drop are the two items inflating the headline above the ~20% operating rate.
5. **D&A / finance costs vs revenue?** Depreciation +27.55% > revenue +19.27% = the capex-absorption gap is opening (new 350-bed Panchkula + others commissioned into a sub-scale occupancy base). Finance costs fell 35% (IPO paid down debt to a negligible Rs 256mn term debt, release line 75) — this benefit is largely spent (net cash already), so it does not recur at this magnitude.
6. **Other Income concentration changing?** OI/PBT stable at 7.28% (vs 8.39% YoY); FY26 OI/PBT 8.91%. Consolidated Other Income is NOT masking the quarter — it is small and stable. (The standalone story is the opposite — see 2B.)

### 2B. STANDALONE YoY (Q1 FY27 vs Q1 FY26), Rs Millions

| Metric | Q1 FY26 | Q1 FY27 | YoY % | Verdict |
|---|---:|---:|---:|---|
| Revenue from Operations | 229.69 | 335.32 | +45.99% | Grew (Panchkula parent revenue) |
| Operating EBITDA (ex-OI) | 103.51 | 12.84 | −87.60% | Collapse |
| Op EBITDA Margin | 45.06% | 3.83% | −4,123 bps | Collapse |
| Other Income | 2.01 | 46.68 | +2,222% | IPO-cash interest surge |
| **Core Operating PBT (PBT−OI)** | 58.92 | (29.57) | **turned negative** | Parent core loss-making |
| Reported PBT | 60.93 | 17.11 | −71.92% | Collapse |
| PAT | 48.97 | 10.84 | −77.86% | Collapse |

**Standalone diagnostics:** parent revenue +46% (Panchkula and flagship) but employee +142.9% (36.04→87.54), professional fees +219.0% (16.23→51.77), depreciation +191.2% (11.61→33.81), other expenses +204.0% (42.66→129.69) — a classic greenfield ramp where costs land ahead of revenue. Finance cost fell 32.98→8.60 (IPO deleveraging). The parent's reported profit survives only because Other Income (interest on unutilised IPO cash) jumped 2.01→46.68mn and **exceeds PBT**. As that IPO cash deploys into V3/Mehar, the Other-Income prop shrinks. This is RES-A3-02.

STOP cleared: YoY table + six diagnostics shown for both statements.

---

## STEP 3 — SEQUENTIAL QoQ TRAJECTORY (consolidated)

Only Q1 FY26, Q4 FY26, Q1 FY27 are disclosed as discrete quarters in the filing; Q2 FY26 and Q3 FY26 are **not separately disclosed** (FY26 full-year minus Q1+Q4 does not isolate them) — marked ND rather than estimated.

| Quarter | Revenue (Rs Cr) | Op EBITDA Margin | Core PBT ex-OI (Rs mn) | Occupancy | Beds | One-offs | QoQ run-rate |
|---|---:|---:|---:|---:|---:|---|---|
| Q1 FY26 | 398.85 | 26.31% | 750.27 | 67.8% | 3,000 | Comparatives unreviewed (L137) | base |
| Q2 FY26 | ND | ND | ND | ND | ND | ND | ND |
| Q3 FY26 | ND | ND | ND | ND | ND | ND | ND |
| Q4 FY26 | 460.41 | 27.66% | 958.87 | 62.5% | 3,610 | Balancing figures (L133) | step-up |
| Q1 FY27 | 475.71 | 26.51% | 974.38 | 55.6% | 3,960 | Deferred-tax benefit 93.40mn (L435) | mild step-up rev; margin & occupancy DOWN |

**QoQ diagnostics:**
- **Run-rate:** revenue stepped up +3.32% QoQ (460.41→475.71 Cr). Core PBT ex-OI +1.62% QoQ. **Plateau-to-modest-step-up on revenue, but deteriorating on quality:** Op EBITDA margin **−115 bps QoQ** (27.66%→26.51%; release states −116 bps, line 1021) and occupancy **−692 bps QoQ** (62.5%→55.6%, line 112). Reported EBITDA fell −1% QoQ in absolute terms (release line 1020).
- **One-off distortion:** Q1 FY27 PAT carries a Rs 93.40mn deferred-tax **benefit** (vs Rs 68.25mn deferred **charge** in Q4 FY26 — a Rs 161.65mn favourable QoQ tax swing). Q4 FY26 numbers are themselves balancing figures (audit caveat).
- **vs <22% EBITDA-margin tripwire:** margin at 26.51% is comfortably above the 22% floor; the QoQ −115 bps slide is a soft-trajectory warning, NOT a tripwire breach (Trigger #3 does not fire — Step 6C).
- **Implied Q2 FY27 base:** to hold the trajectory, Q2 revenue must exceed ~Rs 476 Cr, and — critically — occupancy must stop falling as Agra/Panchkula/Rudrapur ramp; Rudrapur adds its first P&L contribution and a minority-interest line in Q2 (PRES-A1). A new plant that does not lift the blended occupancy above the pre-commissioning level is the classic capex-absorption red flag; occupancy at 55.6% on 3,960 beds means ~1,758 beds are empty (PRES-A8).

STOP cleared.

---

## STEP 4 — OPERATIONAL DECOMPOSITION (PAT BRIDGE, consolidated YoY)

Reported PAT YoY change = 885.93 − 655.06 = **+230.87mn**.

| Component | YoY Change (Rs mn) | YoY Change (%) | Recurring? |
|---|---:|---:|---|
| Operating EBITDA growth | +211.57 | +20.16% | Recurring |
| Depreciation (higher) | −40.69 | +27.55% | Recurring (post-capex) |
| Finance cost (lower) | +53.23 | −35.18% | Recurring but largely spent (net cash) |
| Other Income change | +7.74 | +11.26% | Non-recurring typically |
| = Reported PBT change | **+231.85** | +28.31% | — |
| Tax change (net) | −0.98 | +0.60% | Mixed — see below |
| = Reported PAT change | **+230.87** | +35.24% | — |

**Tax tailwind quantified (RES-A3-06 / PRES-A4 / REL-FND-03):**
- ETR fell to **15.69%** (Q1 FY27) from **20.02%** (Q1 FY26) and 25.74% (Q4 FY26), vs ~25.17% statutory. The driver is a **Rs 93.40mn deferred-tax benefit** (line 435), a sign-flip from the Rs 68.25mn deferred charge in Q4 FY26, plus a Rs 2.67mn prior-year tax credit (line 436).
- **Tax tailwind vs holding prior-year ETR:** at 20.02% ETR, tax on Q1 FY27 PBT (1,050.84mn) would be ~210.4mn; actual tax 164.91mn → **~Rs 45.5mn (Rs 4.5 Cr) of PAT benefit** vs a flat-ETR world. Vs statutory 25.17%, the benefit is ~Rs 99.6mn.
- **Cleanest normalization:** stripping the deferred-tax benefit entirely (add back 93.40mn to tax): normalized PAT ≈ **792.5mn** vs a similarly-adjusted Q1 FY26 of ~651.5mn = **+21.6% growth** — i.e., in line with the +20% EBITDA growth. **The +35% headline PAT growth is flattered to roughly +21–22% real once the non-repeatable deferred-tax benefit is removed.**

**Mandatory questions answered:**
- **% of PAT growth from recurring core?** Operating EBITDA growth (+211.57mn) alone is 91.6% of the +230.87mn PAT change — the core is real. But the *headline optics* (35% vs the ~20% operating rate) rest on the finance-cost drop (largely non-repeating; company now net cash) and the deferred-tax benefit (non-repeating). 
- **If Other Income reverts to prior level?** Consolidated OI is small (7.28% of PBT); reversion is immaterial. (Standalone is the opposite — parent PBT would go negative without its Rs 46.68mn OI.)
- **D&A / finance at steady state?** Depreciation still ramping (+27.55% > revenue); finance cost near a floor (Rs 98mn on negligible debt) — the −35% YoY benefit will not recur. Steady-state PAT growth normalizes toward the ~20% operating rate.
- **Tax adjustments inflating PAT?** Yes — Rs 93.40mn deferred-tax benefit + Rs 2.67mn prior-year credit. Repeatability is the key open question (Q1 in the management-questions table). Conservative bias: treat go-forward ETR at ~23–25%, not 15.7%.

**Standalone-vs-consolidated PAT gap (first-class metric, RES-A3-02):**

| Period | Standalone PAT (mn) | Consolidated PAT (mn) | Standalone as % of Consol | Gap (mn) |
|---|---:|---:|---:|---:|
| Q1 FY26 | 48.97 | 655.06 | 7.48% | 606.09 |
| Q4 FY26 | 86.06 | 767.78 | 11.21% | 681.72 |
| Q1 FY27 | 10.84 | 885.93 | **1.22%** | 875.09 |
| FY26 | 366.16 | 2,735.57 | 13.39% | 2,369.41 |

The parent now contributes just **1.22%** of consolidated PAT (down from 7.48% YoY); **98.8% of group earnings are in subsidiaries**, of which 83.9% is not reviewed by the principal auditor (RES-A3-03, Step 6). The consolidated story is entirely a subsidiary story; the parent core is loss-making before Other Income.

STOP cleared.

---

## STEP 5 — CASH QUALITY & BALANCE SHEET

**Data-availability rule (v1.2):** this is a **Q1** limited review. Reg 33 mandates the cash-flow statement and balance sheet only **half-yearly (Q2/Q4)**. **No cash-flow statement and no balance sheet accompany this Q1 filing.** Therefore CFO, FCF, working-capital, receivable/inventory/payable days and CCC are **ND for the quarter — stated explicitly, not silently skipped.**

| Metric | Prior period | Current (Q1 FY27) | Change | Verdict |
|---|---|---|---|---|
| CFO | ND | ND | ND | No Q1 cash-flow statement (Reg 33 half-yearly) |
| CFO/PAT ratio | ND | ND | ND | Cannot test Pillar-2 cash multiplier this quarter |
| Capex (PPE+CWIP) | ND | ND | ND | Not in Q1 filing |
| FCF (CFO−Capex) | ND | ND | ND | **The FY27 FCF-inflection catalyst is UNTESTABLE in Q1** |
| Working-capital change | ND | ND | ND | No balance sheet |
| Receivable days | 129 (FY26, Notion) | ND | ND | Not disclosed in Q1 — Trigger #2 not testable |
| Inventory days | ND | ND | ND | No balance sheet |
| Payable days | ND | ND | ND | No balance sheet |
| Cash Conversion Cycle | ND | ND | ND | No balance sheet |
| PPE | ND | ND | ND | No balance sheet |
| CWIP | ND | ND | ND | No balance sheet |
| Net Debt / (Net Cash) | Net cash Rs 522 Cr (FY26, Notion) | **Net cash** | — | Term debt Rs 25.6 Cr (256mn, L75) vs FDs Rs 299.8 Cr (2,998mn, L76) + Rs 64.83 Cr idle IPO proceeds (monitoring L555) → net cash confirmed |
| Promoter Pledge | ND | ND | ND | Not disclosed in any of the four docs |

**Cash-quality assessment (do not let INDETERMINATE resolve silently to PROCEED):** cash conversion is **INDETERMINATE this quarter** — there is no Q1 cash-flow statement, so CFO/PAT cannot be measured and the Pillar-2 cash multiplier band cannot be confirmed. Per the house rule, this **caps the verdict at PROCEED WITH CAVEATS**, with the missing evidence named: **(1) no quarterly CFO/FCF (Reg 33 half-yearly — first read at H1 FY27/Q2); (2) receivable days undisclosed (Trigger #2 untestable); (3) capex undisclosed (FY27 FCF-inflection catalyst untestable).**

**Corroborating monitoring-report facts (MON findings):** Rs 648.32mn (Rs 64.83 Cr) of IPO proceeds sit idle in Axis (72.32mn) + ICICI (576.00mn) monitoring accounts at **zero disclosed yield** (monitoring L549-555; MON-A3-F1-01). Four of five IPO objects were dormant in Q1; only the Rohtak build (Park Medicity NCR) moved (Rs 28.66mn deployed, Rs 195.19mn of 605.00mn cumulative, Rs 409.81mn remaining; MON-A3-F6-02). The **medical-equipment object is ~84% behind its FY26 schedule** (Rs 36.08mn utilised vs Rs 229.59mn planned; MON-A3-F6-01) — a capital-deployment execution miss against the "G1 war-chest / capex discipline" thesis. The Rs 2,453.18mn "unidentified inorganic acquisitions & GCP" object is reported fully utilised by Mar-26 with **no named target** and GCP detail "Not applicable" (MON-A3-F1-02) — a capital-allocation transparency gap.

STOP cleared.

---

## STEP 6 — RECONCILIATION VS THESIS

### 6A. Variance vs Notion projections (FY27 base case; Q1 is one quarter, annualised where noted)

| Metric | Bear | Base | Bull | Q1 FY27 actual | Annualised run-rate | Lands in |
|---|---|---|---|---|---|---|
| Revenue (Rs Cr) | ND | 1,990 (base) | ND | 475.71 (L418) | ~1,903 (x4) | Below base run-rate (Q1 seasonally lowest; ramp ahead) |
| Op EBITDA Margin | ND | 26% | ND | 26.51% (derived) | — | At base |
| PAT total (Rs Cr) | ND | 318 (owners base) | ND | 88.59 total / 82.51 owners (L438/446) | ~330 owners (x4) | At/above base — but tax-flattered (~21% real) |
| EPS (Rs) | ND | 7.35 | ND | 2.05 (L460) | ~8.20 (x4) | Above base — but EPS struck on total PAT (0C) |
| Net Debt | ND | Net cash | ND | Net cash (L75/76) | — | At base |
| ROCE | ND | ~19–20% | ND | ND (no balance sheet) | ND | Untestable in Q1 |

**Read:** revenue is tracking slightly below the FY27 base quarterly average (Q1 is the seasonal low, and the c.46% bed build is still ramping), while PAT/EPS optically sit at or above base — but that beat is manufactured by the non-repeatable deferred-tax benefit; on a normalized-ETR basis PAT growth is ~21%, squarely at the +18.5% base pace. **No metric lands below bear. The probability-re-weighting rule (2+ metrics below bear for 2 consecutive quarters) does NOT trigger.**

### 6B. Watchlist / monitoring-checklist status

| # | Watchlist Item | Green | Red | Q1 FY27 reading | Status |
|---|---|---|---|---|---|
| 1 | FY27 FCF inflection (capex ~Rs 55 Cr vs CFO ~Rs 380 Cr) | +ve FCF | −ve FCF | **ND** — no Q1 cash-flow statement | UNKNOWN |
| 2 | FY26 promoter remuneration (AR) | <27% | ≥27% | ND — not in quarterly | UNKNOWN |
| 3 | Q2 Rudrapur standalone financials / EV/Sales test | ≤3.2x | >4x | ND — consolidates from Q2; nil Q1 (deck L506) | UNKNOWN (pending Q2) |
| 4 | Platinum ARPOB delta vs Rs 29,725 | ≥ blended | dilutive | ND — ARPOB never quantified (PRES-A9) | UNKNOWN |
| 5 | Bed roadmap delivery (3,960→~5,690 by Mar-28) | on schedule | slippage | 3,960 at Q1 (L111); Panchkula done, Rudrapur commissioned 2-Aug; dense dated pipeline | GREEN (on schedule so far) |
| 6 | Occupancy trajectory | rising | falling | 55.6%, −1,224 bps YoY / −692 bps QoQ (L112) | RED (falling; ramp-attributed) |
| 7 | EBITDA margin | ≥26% | <22% | 26.51% op (−115 bps QoQ) | GREEN (above floor; softening) |

### 6C. Thesis-broken trigger check (all four, explicit)

| Thesis-Broken Condition | Threshold | Q1 FY27 reading | FIRED? |
|---|---|---|---|
| 1. Promoter remuneration >30% of PAT, 2 consecutive years | >30% x2yr | **ND** — no remuneration line in a quarterly filing; FY25=27.5%, FY26 pending AR | **NO** (not testable this quarter) |
| 2. Debtor days >175, 2 consecutive quarters | >175 x2Q | **ND** — no balance sheet in Q1 limited review; FY26=129 | **NO** (not testable this quarter) |
| 3. EBITDA margin <22%, 2 consecutive quarters | <22% x2Q | Q1 FY27 op 26.51%; Q4 FY26 27.66% — both >22% (QoQ −115 bps) | **NO** |
| 4. Major acquisition >Rs 1.0 Cr/bed | >Rs 1.0 Cr/bed | V3/Rudrapur Rs 177 Cr ÷ 330 beds = **Rs 0.54 Cr/bed** (or Rs 141.6 Cr paid for 80% ÷ 330 = Rs 0.43 Cr/bed); Mehar Rs 107 Cr ÷ 150 beds = **Rs 0.71 Cr/bed** — both below Rs 1.0 Cr/bed | **NO** |

**All four triggers: NOT FIRED.** Decision Status stays **WATCHLIST**. 

*Note on a discrepancy for the record:* the presentation-forensics cross-check (PRES cross-check note, L85) stated Rudrapur/Zirakpur per-bed prices are "above the Rs 1.0 Cr/bed trigger," reading Rs-million-per-bed figures (4.3mn, 7.1mn) against the Rs-Crore threshold. Converted correctly, 7.1mn/bed = Rs 0.71 Cr/bed and 5.4mn/bed = Rs 0.54 Cr/bed — **both below Rs 1.0 Cr/bed.** The results-forensics (RES-A3-08) and the reconciled facts are correct; Trigger #4 does NOT fire. This is a unit-scaling slip in the presentation forensics, resolved here in favour of the correct (below-threshold) reading.

### 6D. Growth-trigger status

| Trigger | Original confidence | Confirming evidence | Killing evidence | Updated status |
|---|---|---|---|---|
| FY27 FCF inflection (re-rating lever) | Medium | Net cash; negligible debt; low finance cost | No Q1 CFO/capex to confirm; medical-equipment capex 84% behind schedule | **DELAYED / UNVERIFIED** (first read at Q2) |
| Bed roadmap 3,960→5,740 | Medium-High | Panchkula done; Rudrapur commissioned 2-Aug; dense dated pipeline (Step register) | None yet | **ON TRACK** |
| Margin defence ≥26% | Medium | 26.51% op margin held YoY despite occupancy fall | QoQ −115 bps; occupancy −692 bps QoQ | **ON TRACK (softening)** |
| Affordable-core / ARPOB | Medium | IPD-led 94.4% mix | ARPOB undisclosed; Platinum premium brand departs from affordable core | **WEAKENED (unverifiable)** |
| Capital-allocation discipline / war chest | Medium | Both acquisitions <Rs 1.0 Cr/bed; net cash | Rs 648mn idle zero-yield; IPO object variation via postal ballot; Rs 2,453mn "unidentified" fully spent with no named target | **AMBIGUOUS** |

STOP cleared: 6A–6D shown in full, including probability-re-weighting state (not triggered).

---

## STEP 7 — FOUR-PILLAR DESTINATION PE RE-VALIDATION

The destination PE (Notion: 23.2x, three-pillar) was set under Section 1B v3.3. **Q1 provides no balance sheet, so ROCE and CFO/PAT are ND — the two most valuation-load-bearing pillars cannot be revised on Q1 data.** No pillar is revised this quarter; the check is a hold-with-caveats.

| Pillar / Input | Original assumption | Q1 FY27 reading | Action |
|---|---|---|---|
| ROCE Base (0.5×ROCE+7.5, floor 9x, cap 24x) | ROCE 19.3% → ~17.2x mapped | **ND** — no balance sheet in Q1 | Hold; re-run FTTCP ROCE verdict at H1 FY27 |
| Cash Multiplier | ~1.15x (rising to 1.30x on FCF inflection) | **INDETERMINATE** — no Q1 CFO | Hold; band unconfirmable until Q2 |
| Growth Visibility Premium | + (EM 36.3, MOAT STRENGTHENING) | Dense dated bed roadmap on track | Hold |
| Strategic Premium | Conditional (drops to 0x if promoter remuneration ≥27%) | Remuneration ND this quarter | Hold; contingent on AR |
| UA Multiplier | Per Amendment 3 (min(Raw×1.25, Sector Cap)) | Institutions 9.8%, promoter 82.9% (deck L1043/1050) | Hold |
| Sector Cap | Hospital sector | No reclassification | Hold |
| **Hurdle Ratio recheck** | HR=(1+EPS CAGR)³×(Dest PE mid÷Current PE)≥1.953 | Current PE ~40x (CMP 292.55; deck L1040); dest 23.2x → dest/current ≈0.58; even at 25% EPS CAGR HR≈1.953×0.58≈1.13 <1.953 | **STOP-band on price** — overvalued at CMP; consistent with AVOID |

**Destination PE unchanged at 23.2x this quarter** (no pillar revised; ROCE/cash inputs ND). The Hurdle Ratio remains in the STOP band at the current Rs 292.55 price (dest 23.2x vs current ~40x PE) — mechanically confirming the AVOID-at-CMP stance. Fair-value / entry recompute is deferred to Q2 (H1) when ROCE and CFO become available.

STOP cleared.

---

## STEP 8 — POSITION DECISION (branch 8A-W, non-held / WATCHLIST)

Decision Status verified in Step 0A = **WATCHLIST (AVOID at CMP), Position None.** No thesis-broken trigger fired (Step 6C). Actuals land **between bear and base on revenue run-rate and at/above base on tax-flattered PAT/EPS** — no metric below bear. Applying the 8A-W branch:

- No thesis-broken condition FIRED → **do not reclassify to AVOID-permanent; retain WATCHLIST.**
- Actuals not below bear on 2+ metrics → no forced projection cut; but the **tax-flattered PAT and the QoQ occupancy/margin deterioration warrant explicitly re-anchoring the FY27 model to the ~21% normalized-PAT trajectory rather than the 35% headline.**
- **Entry zone: unchanged at Rs 101–126; MoS Rs 101.** No pre-committed BUY gate threshold was met (CMP Rs 292.55 is ~2.3x the AVOID line). **Recommended action: continue to AVOID at CMP; hold on WATCHLIST.**
- **Master decision gate: pushed to Q2 FY27 (H1)** — the first quarter carrying (a) a Reg 33 half-yearly cash-flow statement (FCF-inflection catalyst becomes testable), (b) Rudrapur consolidation with its minority line, and (c) a balance sheet to test ROCE and debtor days.

**8B. Add-back / trim trigger refinement:** no position, so no trim ladder. Pre-committed **BUY reconsideration** conditions to carry forward: (i) CMP into Rs 101–126 entry zone; (ii) Q2 H1 CFO/PAT ≥0.8x confirming the cash multiplier; (iii) occupancy stabilising ≥60% on the enlarged bed base; (iv) FY26 promoter remuneration <27% of PAT in the AR; (v) go-forward ETR normalising without a PAT cliff.

**8C. Single cleanest metric for Q2 FY27:** **Consolidated blended occupancy % on the enlarged bed base (Step 3 first-class metric).** It most cleanly resolves the bull/bear split — whether the 1,224 bps YoY / 692 bps QoQ occupancy fall is pure denominator dilution from new beds (bull: fills as they ramp) or emerging same-store demand weakness (bear). **Bull threshold: occupancy ≥60% and rising QoQ. Bear threshold: <55% and still falling.** Secondary focal metric (records the tax question): **consolidated ETR** — a return toward ~23–25% would confirm the Q1 PAT beat was a one-off deferred-tax benefit.

STOP cleared.

---

# SECTION B — CONCALL ANALYSIS (ROLE 5)

*Executed in full under Quarterly Concall Analysis Protocol v1.1 over the 87-turn Q1 FY27 transcript (extract 87/87 lines, GATE A1 pass; ledger GATE A2 pass; forensics FN-01..FN-24, GATE A3 pass). Citation convention: "turn N" = extract line N (A1/A2 verified 1:1). Adversarial reading throughout; garbles distinguished from genuine inconsistency and not over-weighted.*

## STEP 0 — PRE-FLIGHT

**0A. Notion / prior-call context.** Decision Status re-verified = **WATCHLIST (AVOID at CMP Rs 292.55), Position None, Promoter Verdict MONITOR** (same status framed in Section A Step 0A). Growth triggers, thesis-broken conditions and monitoring checklist are those carried in Section A. **This is the FIRST concall on record for PARKHOSPS** — there is no prior Role 5 log. Consequently the promise-vs-delivery scorecard and the trailing-4-quarter credibility ratio **cannot be computed this quarter**; the tracker BEGINS here (Step 3), and every commitment below is registered as a **baseline** to be scored from Q2 FY27 onward.

**0B. Call participants (turn 1 roster + operator sweep):**

| Role | Name (as heard) | Notes / flag |
|---|---|---|
| Hosting broker / IR | Ms. Saloni Nagar, Ad Factors PR | External IR firm moderates; no house-broker hosting the call (broker-neutral) |
| CMD / Chairman | **Dr. Ajit Gupta — ABSENT** | Zero occurrences across all 87 turns (grep = 0). **Yellow flag (FN-19):** promoter-Chairman absent on a two-acquisition, guidance-change quarter |
| Managing Director | Dr. Ankit Gupta ("Ankrit" garble) | Delivers opening remarks (turn 2) |
| CEO | Dr. Sanjay Sharma ("Chandi" garble), Full-time Director & CEO | Operating metrics (turn 3) |
| CFO | Mr. Rajesh Sharma ("Rajes"), Group CFO | Financials + FY27 guidance (turns 4, 7) — **answers the operational/guidance questions**, see yellow flag below |
| CSO / OSD Finance | Mr. Suresh/Sudesh Sharma | Closing remarks (turn 86) |

**Yellow flags from participant list:** (1) **Chairman absence** (FN-19) — the most senior promoter figure is neither introduced nor heard on a quarter with two acquisitions (Rudrapur ~Rs 177 Cr; Zirakpur/Mahair announced the day before) and a bed-guidance change (5,040→4,740). (2) **CFO fielding operational/forward guidance** — the FY27 P&L guide, greenfield-margin trajectory and ROCE all come from the CFO (turns 7, 8, 35), the MD/CEO answering less of the forward substance than typical; a mild depth flag, not disqualifying given the CEO handled operating metrics. Four management voices are present, so the call is not IR-dominated.

**0C. Call structure.** Q1 FY27 earnings call; the Board approved results "yesterday" and the call follows immediately (turn 2) — **same-day/next-day cadence = largely canned opening, signal is in Q&A.** ~29 discrete questions across **9 analysts** (one repeat caller, Akshay Thakur/Helios, in two rounds); operator closes "due to time constraints" (turn 86). Buy-side present (Helios, Asha Investment Managers, Alchemy Ventures, iThought PMS, Antique) — **not a softball-only call.** No house-broker lead-off. Q&A is the bulk of the transcript (turns 6–85 of 87).

**0D. Safe-harbour caveats.** Standard forward-looking disclaimer referenced to the earnings presentation (turn 1). No new or widened caveat category detected. First call, so no prior-caveat diff.

**0E. Business type.** **Standard operating business** (hospital operator) — Step 2 (not the lender Step 2L) guidance set applies.

STOP cleared: Notion status re-verified; participants listed with two yellow flags; structure noted (same-day, Q&A-heavy, buy-side present); caveats logged; business type standard.

---

## STEP 1 — OPENING REMARKS: CLAIMS INVENTORY

| # | Claim (trimmed) | Type | Quantified? | Turn |
|---|---|---|---|---|
| 1 | Rudrapur (Medicity) 100% acquired, all-cash ~Rs 177 Cr, entry into 6th state | Operational / Strategic | YES | 2 |
| 2 | Rudrapur is a "331 NH accredited" multi-super-speciality hospital, commissioned "22nd August 2026" | Operational | YES (but inconsistent w/ 330 beds / 2-Aug — FN-18) | 2 |
| 3 | 100-bed extension at Palam Vihar ("Park Platinum") → cluster to 750 beds | Operational | YES | 2 |
| 4 | Narela 200-bed (insolvency) on track; Mehar/Zirakpur 150-bed ~Rs 107 Cr announced "yesterday"; 450 beds total commission Nov–Dec 26 | Operational / Forward | YES | 2 |
| 5 | Bed capacity 3,960 as of 30-Jun, +32% YoY; CY26 addition 1,490 beds (+46% over CY25 3,250) | Backward / Operational | YES | 2 |
| 6 | **End FY27 at 4,740 beds; +1,000 in FY28 → 5,740 by FY28**, funded largely via internal accruals + IPO "without recourse to fresh debt" | Forward Guidance | YES (5,740 later restated 6,740 — FN-03/18) | 2 |
| 7 | Q1 revenue Rs 476 Cr (+19%); EBITDA ex-OI Rs 126 Cr (+20%, 26.5% margin); PAT Rs 89 Cr (+35%, 18.6% margin) | Backward | YES | 2 |
| 8 | IPD 26,341 (+16%); OPD 2,23,446 (+17%); ALOS 5.9d (−8%); high-end specialty 62% (+440bps) | Backward / Operational | YES | 3 |
| 9 | Network occupancy 56% vs 68% YoY — "reflects step-up in capacity" (960 beds added, ramping) | Backward | YES | 3 |
| 10 | FY27 full-year occupancy to **moderate below FY26's 64%** | Forward Soft/Guidance | YES (directional floor) | 3 |
| 11 | CGHS: guided 7–7.5% benefit into FY27; **full impact from Q2** | Forward Guidance | YES | 3 |
| 12 | Nine hospitals with NABH-accredited labs (up from 8); four more targeted this FY | Operational / Forward | YES | 3 |
| 13 | Term debt Rs 25.6 Cr (vs 28.2 Cr Mar-26); FDs Rs 300 Cr; net worth Rs 2,100 Cr | Backward | YES | 4 |
| 14 | **PAT-margin +220 bps expansion "largely on account of reduction in interest outgo"** | Backward / Causal | YES (causal claim — see FN-16) | 4 |
| 15 | Receivable days to trend to **125–130 (medium-term)** as govt-claim processing improves | Forward Guidance | YES | 4 |
| 16 | Payer mix 77% govt / 23% self+TPA; guided to 70:30 over 12–18 months | Backward / Forward | YES | 4 |
| 17 | Capex per bed "37 lakhs — lowest in listed peers"; "fully funded... without recourse to any material such debt" to 5,740 by Mar-2028 | Strategic / Forward | YES (37 later 34/36 — FN-18) | 4 |

**Four diagnostics:**
- **% quantified:** ~16 of 17 opening claims carry a number, date or binary → **specificity of the opening ~0.94** (very high). This is a numbers-forward opening.
- **New vs reaffirmation:** the entire call is NEW disclosure — first concall — but within it the load-bearing FIRST-ever hard FY27 P&L guide (Rs 2,080 / 530 / 360 Cr) is given in Q&A (turn 7), not the opening.
- **Quietly dropped:** none possible (no prior call). However the **bed guidance already moved** vs the last press communication (5,040→4,740 FY27, surfaced by an analyst at turn 41, not volunteered in the opening).
- **Internal contradictions in the opening:** yes — "331 NH accredited" beds (turn 2) vs "330 beds functional" (turn 10); "22nd August" commissioning (turn 2) vs "2nd of August" (turn 42); "37 lakhs per bed" (turn 4) vs "34 lakh" (turn 43) / "36 lakhs" (turn 46). Adjudicated as data-precision noise + garble (FN-18), not thesis-moving, but logged.

STOP cleared.

---

## STEP 2 — FORWARD GUIDANCE EXTRACTION (the centrepiece)

Every figure verbatim from the transcript; "Last Quarter / Two Quarters Ago" = **New** for all rows (first concall).

| Metric | This Quarter's Guidance | Last Qtr | 2 Qtrs Ago | Trajectory | Confidence |
|---|---|---|---|---|---|
| Revenue FY27 | **~Rs 2,080 Cr, +24%** (turn 7) | — | — | New | HIGH |
| EBITDA FY27 ("VA") | **~Rs 530 Cr, +25%** (turn 7) | — | — | New | HIGH (absolute; % inconsistent — see 2 diag) |
| PAT FY27 ("P"/"fat") | **~Rs 360 Cr, +32%** (turn 7) | — | — | New | MEDIUM (ETR-dependent — FN-02) |
| EBITDA margin band | **26.5–27% full FY27** (turns 8, 9, 30) | — | — | New | HIGH |
| Bed capacity FY27 | **4,740 by Mar-27** (turns 2, 42) | 5,040 (prior press) | — | Lowered (−300, Zirakpur timing; turn 41–42) | HIGH |
| Bed capacity FY28 | **5,740 [restated 6,740]** (turns 2, 42) | — | — | New (endpoint self-contradicts — FN-03/18) | MEDIUM |
| Capex envelope FY27+28 | **Rs 767 Cr → 2,130 beds at ~36 lakh/bed** (turns 46, 48) | — | — | New | HIGH |
| Rudrapur ramp | FY27 rev ~Rs 100 Cr / EBITDA ~20–22 Cr / PAT ~12–13 Cr; FY28 rev ~Rs 140 Cr / EBITDA ~35–36 Cr (turn 10) | — | — | New | MEDIUM (units garbled "K/KES" — FN-04) |
| Zirakpur (Mehar) | FY28 first-year rev [spoken "705 Cr" = garble vs ~Rs 70–75 Cr scale], EBITDA ~25–26% (turn 10) | — | — | New | LOW (number garble — FN-05, do NOT carry 705) |
| ARPOB growth | **10–12% p.a. for the next 2 years** (turns 9, 62, 63) | — | — | New | HIGH |
| Payer mix | to **70:30** in 12–18 [also 12–15] months (turns 4, 61) | — | — | New | MEDIUM (window self-varies) |
| Occupancy FY27 | to **moderate below FY26's 64%** (turn 3) | — | — | New | MEDIUM (directional) |
| CGHS benefit | **7–7.5%, full impact from Q2**; but **routed to equipment/capex, not directly to EBITDA** (turns 3, 26, 28) | — | — | New | MEDIUM (margin impact hedged down — FN-13) |
| ROCE | ~18% today → **+150–200 bps in 12–18 months** (turn 35) | — | — | New | MEDIUM |
| Receivable days | trend to **125–130 (medium-term)** (turn 4) | — | — | New | MEDIUM |
| Rudrapur incremental capex | **not more than Rs 10–12 Cr** FY27 (turn 18) | — | — | New | HIGH |
| Promoter dilution | to **75% (~8% divest) by Dec-2028** via acquisition-linked equity raise (turn 51) | — | — | New | LOW (triple-hedged — FN-12/17) |
| Dividend / payout | **NOT DISCUSSED** | — | — | — | ND |
| Net debt trajectory | net cash; "no material fresh debt" to 5,740 (turn 4) | — | — | New | MEDIUM (funding hedged — FN-22) |

**Diagnostic questions:**
- **Widened or tightened?** N/A (first call). The one movement vs prior communication — **bed guidance LOWERED 5,040→4,740 for FY27** — was surfaced by an analyst (turn 41), then explained as Zirakpur timing plus new Palam/Platinum adds, with the FY28 endpoint pushed to 5,740/6,740 (turn 42). Net: near-term bed count trimmed, out-year endpoint raised (and self-inconsistent).
- **Any guidance refused?** Management **declined to quantify a long-term case-mix target** (turn 55: "very difficult to actually project or predict any percentage") and **declined a firm dilution timeline** (turn 51: "too early to comment... I cannot specify exact timeline"). Both are addressable metrics; the refusals are logged (FN-15, FN-12).
- **Internally consistent arithmetic?** The revenue guide reconciles cleanly; the **PAT guide leans on a sub-statutory ETR** and the **EBITDA absolute vs its stated growth rate do not both tie to the FY26 base** — full bridge in Step 7A below.
- **Vs Four-Pillar projections?** Revenue guide (+24%) sits **above** the Notion +18.5% base; PAT guide (+32%) is **above base but ETR-flattered**; EBITDA margin guide (26.5–27%) is **at/above** the 26% base. Management is guiding to the bull edge on the top line while the quality of the PAT number is the open question.

STOP cleared — this is the most critical artifact.

---

## STEP 3 — PROMISE vs DELIVERY AUDIT

**3A/3B/3C/3D. Baseline established, no historical audit possible.** This is the FIRST concall under the protocol for PARKHOSPS. There is **no prior-quarter claims inventory to score**, so:
- Last-quarter delivery table: **N/A (no prior call).**
- Trailing-4-quarter credibility ratio: **UNSCORED this quarter** (denominator = 0). It is first computable at Q2 FY27, when this quarter's commitments are marked DELIVERED / PARTIAL / MISSED / DELAYED / DROPPED.
- Management credibility Grade and the Role 1 track-record input: **UNSCORED — not substitutable by session judgment** (protocol single-source rule). Provisional Promoter Verdict remains **MONITOR** (unchanged from Notion); no ratio exists to move it.

**Baseline commitment register registered for Q2+ scoring (from FN-01..FN-11, FN-13, FN-17; A3 commitment register):**

| # | Baseline commitment | Implied date | Turn | First scored |
|---|---|---|---|---|
| B1 | FY27 rev ~Rs 2,080 Cr / EBITDA ~Rs 530 Cr / PAT ~Rs 360 Cr (24/25/32%) | Mar-2027 (tracked Q2/Q3/Q4) | 7 | Q2 FY27 |
| B2 | Bed capacity 4,740 by end FY27 | Mar-2027 | 2, 42 | Q2/Q3 |
| B3 | Bed capacity 5,740 [/6,740] by end FY28 | Mar-2028 | 2, 42 | FY28 |
| B4 | 450 beds (Narela/Platinum/Zirakpur) commission Nov–Dec 26 | Q3 FY27 | 2, 42 | Q3 |
| B5 | Rudrapur FY27 rev ~Rs 100 Cr / EBITDA ~20–22 / PAT ~12–13 Cr | FY27 | 10 | Q2 onward |
| B6 | EBITDA margin held 26.5–27% | Full FY27 | 8, 9, 30 | Q2/Q3/Q4 |
| B7 | ARPOB growth 10–12% p.a. | Next 2 years | 9, 62 | Q2 onward |
| B8 | Payer mix to 70:30 | 12–18 months | 4, 61 | Q2 onward |
| B9 | CGHS 7–7.5% full impact from Q2 | Q2 FY27 | 3, 21, 26 | **Q2 FY27** |
| B10 | ROCE ~18% → +150–200 bps | 12–18 months | 35 | H1/H2 |
| B11 | Receivable days to 125–130 | Medium-term | 4 | Q2/Q4 (balance-sheet quarters) |
| B12 | Promoter stake to 75% (~8% divest) via equity raise | By Dec-2028 | 51 | Ongoing |

**3E. Prior Role 4 Questions-for-Management — answered by this call?** The Q1 FY27 Role 4 review posed 15 questions (Section A / Step 8.5, prior version). Answer-status against the concall:

| Prior Q | Topic | Answer status on call | What was said (turn) |
|---|---|---|---|
| Q1 | Deferred-tax / go-forward ETR | **NOT ADDRESSED — actively re-attributed** | Margin lift credited only to interest reduction (turn 4); no tax/ETR mention. **ESCALATE (FN-16/20).** |
| Q2 | Standalone parent core loss-making | **NOT ADDRESSED** | No standalone figure spoken (FN-24) |
| Q3 | 83.9% of PAT outside principal-auditor review | **NOT ADDRESSED** | Assurance scope never raised (FN-21) |
| Q4 | Rs 2,840mn M&A funding / IPO object variation / Rs 2,453mn "unidentified" | **PARTIALLY / masked** | "Fully funded... no material fresh debt" (turns 2, 4); object-variation ballot & idle proceeds not mentioned (FN-22) |
| Q5 | Medical-equipment object 84% behind | **NOT ADDRESSED** | Not raised |
| Q6 | Rohtak IPO deployment timeline | **NOT ADDRESSED** | Not raised |
| Q7 | Occupancy split + ARPOB | **PARTIALLY ANSWERED** | Network occupancy 56% vs 68% given (turn 3), ARPOB **growth** 10–12% given (turn 62); **absolute ARPOB and same-store vs new-bed split still NOT given** (FN-23) |
| Q8 | Equity raise / debt for +59% build | **PARTIALLY ANSWERED** | Equity raise now flagged — ~8% divest by Dec-2028, tied to an acquisition (turn 51, FN-17) |
| Q9 | Rudrapur 20% put/call terms & minority | **NOT ADDRESSED** | Rudrapur economics given (turn 10) but the 20%/FY30 terms not addressed |
| Q10 | Rudrapur Q2 first contribution | **PARTIALLY** | FY27 rev ~Rs 100 Cr / EBITDA 20–22 Cr guided (turn 10); no explicit Q2 split |
| Q11 | Share-count / raise into 75% floor | **PARTIALLY ANSWERED** | Confirms ~8% divest by Dec-2028 via raise (turn 51) |
| Q12 | Devina Derma disposal booking | **NOT ADDRESSED** | Not raised |
| Q13 | Actuarial remeasurement swing | **NOT ADDRESSED** | Not raised |
| Q14 | One reconciled bed roadmap | **PARTIALLY — and added new inconsistencies** | Roadmap detailed (turn 42) but 5,740 vs 6,740, 34/36/37 lakh, 2 vs 22 Aug, 330 vs 331 (FN-18) |
| Q15 | Healplus entity-list omission | **NOT ADDRESSED** | Not raised |

**Pattern (3C read):** the call answered the growth/roadmap questions in specific numbers but was **silent or evasive on every earnings-quality / governance / assurance question (Q1, Q2, Q3, Q5, Q12, Q13, Q15)** and actively supplied a competing story on the single most material one (Q1 deferred tax). This is a first-quarter observation, not yet a multi-quarter pattern, but it sets the escalation baseline: repeated silence on the tax/ETR and assurance items at Q2 becomes a governance signal.

STOP cleared: baseline registered; prior-question answer-status mapped; credibility ratio explicitly UNSCORED (first call).

---

## STEP 4 — Q&A DECOMPOSITION (60%+ of effort)

### 4A. Q&A inventory (9 analysts, ~29 threads)

| Analyst / Firm | Side | Key question(s) | Category | Resp. quality | Substance |
|---|---|---|---|---|---|
| Anul Agarwal, MK Global | Sell | FY27 revenue guide; greenfield EBITDA losses; ARPOB/occupancy split; Rudrapur ramp | Fwd Guidance / Operational | **B** | HIGH — surfaced the Rs 2,080/530/360 Cr guide (turn 7) |
| Akshay Thakur, Helios (R1) | Buy | Oncology surgical/medical split; incremental capex post-acquisition | Strategic / Financial | **B** | MED — capex 245 Cr Agra, 7.5 Cr equipment, Rudrapur 10–12 Cr (turn 18) |
| Kashish Thakur, Lara | — | CGHS flow-through timing; peer margin heat | Financial / Macro | **B** | MED — full impact Q2–Q4 (turn 21) |
| "Saga", Alchemy Ventures | Buy | Quantify CGHS EBITDA flow-through | Financial | **C** | MED — deflected: routed to capex, not EBITDA (turns 26–30, FN-13) |
| Nalisha, Asha Inv Mgrs | Buy | Diminishing returns as base expands; management bandwidth | Strategic | **B** | HIGH — densification/cluster logic + ROCE 18% +150–200bps (turn 35) |
| Shoubam Par, Chhattisgarh | — | Bed guidance 5,040→4,740; rising capex/bed; **promoter dilution timeline** | Fwd Guidance / Governance | **C on dilution / B on beds** | HIGH — bed reconciliation (turn 42); **dilution triple-hedged (turn 51, FN-12/17)** |
| Sumit Gupta, Antique | Buy | Case-mix target; acquired-facility payer mix; doctor retention/attrition | Strategic | **B/C** | MED — refused long-term case-mix % (turn 55, FN-15) |
| Ronak Agarwal, iThought | Buy | Payer-mix trajectory; ARPOB growth from mix shift | Financial | **B** | HIGH — 77% govt→70:30; ARPOB 10–12% for 2 yrs (turns 61–63) |
| Akshay Thakur, Helios (R2) | Buy | HIS/IT systems; OPD funnel; neurology mix | Operational | **B** | LOW-MED — qualitative |

### 4B. Question-pattern analysis
- **Most-repeated topics** (market doesn't trust the first answer): **CGHS impact** (3 analysts — Q8/Q10/Q11), **payer mix 70:30** (3 — Q5/Q20/Q23), **capex/bed** (3 — Q7/Q15/Q16), **occupancy/ARPOB** (Q3/Q24), **Rudrapur economics** (Q4/Q20/Q21), **bed roadmap** (Q14/Q21). CGHS being asked three times, and management routing it *away* from EBITDA each time (FN-13), is the clearest "contested topic" signal.
- **Buy-side vs sell-side:** strong buy-side participation (Helios, Asha, Alchemy, Antique, iThought) — **not an orchestrated softball call.** No house broker leading. Positive on call-quality.
- **Pushback:** analyst at turn 44 pushed on the capex/bed jump ("there's a significant increase") — management answered "no concern" (turn 45) then gave the blended Rs 36 lakh bridge (turn 46). Genuine pushback, adequately answered.
- **The obvious question that DID get asked but not answered:** promoter dilution timeline (turn 51) — triple-hedged. The obvious question that was NOT asked by anyone: the **deferred-tax benefit / ETR fall** — no analyst probed the tax composition of the +35% PAT, so management was never forced to address FN-16 (the most material earnings-quality item). Absence of that question + management's affirmative re-attribution to interest = the load-bearing disclosure-quality finding.

### 4C. Three most important exchanges

**Exchange 1 — the FY27 guide (turn 6→7).** *Analyst (Anul, MK Global):* asks for FY27 revenue-growth guidance given "not many beds added last year," on the back of ARPOB + occupancy. *Management (CFO Rajesh):* "we are expecting a top line of 2080 crores... a VA of 530 crores and a P of 360 crores... revenue growth is 24%... AITA growth 25%... fat growth staggering at 32%." **Said:** first hard FY27 P&L guide, the sole anchor for the 25%-CAGR thesis. **Not said:** the composition of the +32% PAT — no ETR assumption, no bridge from the tax-flattered Q1. **Implies:** the guide is credible on revenue, aggressive-and-tax-dependent on PAT (Step 7A). **Follow-up we would ask:** "what go-forward ETR is embedded in the Rs 360 Cr PAT, given Q1's 15.7%?"

**Exchange 2 — the PAT-margin bridge (turn 4, opening + confirmed in Q&A silence).** *Management (CFO):* "PAT margin expansion was largely on account of reduction in interest outgo following the substantial repayment of term debt." **Said:** a clean, plausible cause (finance cost −35% YoY). **Not said:** the Rs 93.40mn deferred-tax benefit and the ETR fall to 15.7% from 20.0% (line 435) that Section A quantifies as the larger flatterer of the +35% PAT. **Implies (FN-16/20):** this is not mere silence — management supplied a **competing causal story** for the same margin movement, and no analyst challenged it. **CONFIRMATORY-NEGATIVE on disclosure quality.** **Follow-up:** "quantify the interest-saving contribution vs the deferred-tax contribution to the +220 bps."

**Exchange 3 — promoter dilution (turn 51).** *Analyst (Shoubam):* "we are mandated to bring [promoter stake] down to 75%... any timeline and how?" *Management:* "too early to comment... 3-year regulatory timeline lapses December 2028... approximately 8% equity that we have to divest... we are evaluating now opportunities... if we should come close to acquiring an interesting asset... that would be the right time for us to raise this equity capital... I cannot specify exact timeline right now." **Said:** an explicit forward-dilution obligation — ~8% by Dec-2028, delivered via an **acquisition-linked equity raise** (FN-17). **Not said:** size, price, timing, or whether via OFS vs fresh issue. **Implies:** a defined future share-count expansion tied to M&A, directly relevant to per-share value and the entry zone. **Follow-up:** "fresh issue or OFS, and roughly what dilution % should we model against the Rs 101–126 entry zone?"

STOP cleared: 4A/4B/4C shown; Q&A carries the analytical weight.

---

## STEP 5 — NEW INFORMATION AUDIT

### 5A. New disclosures

| Disclosure | Type | Material? | Thesis impact |
|---|---|---|---|
| **FY27 P&L guide Rs 2,080/530/360 Cr (24/25/32%)** (turn 7) | Forward guidance | **YES** | The sole hard anchor for the 25%-CAGR thesis; PAT leg is ETR-dependent |
| **Rudrapur economics: FY27 rev ~Rs 100 Cr, EBITDA ~20–22% (~20–22 Cr), FY28 rev ~140 Cr** (turn 10) | New catalyst detail | YES | Sizes a Q2-consolidating asset; ~20–22% EBITDA below group 26.5% (dilutive year 1) |
| **CGHS 7–7.5% benefit routed to equipment/capex, NOT EBITDA** (turns 26–30, FN-13) | Negative surprise (soft) | YES | Removes a presumed FY27 margin tailwind; supports only "held" margin, not expansion |
| **Promoter to divest ~8% to 75% by Dec-2028 via acquisition-linked equity raise** (turn 51, FN-17) | Forward dilution | YES | Future share-count expansion; carry to monitorables + entry-zone math |
| Densification/cluster strategy articulated; Tricity to ~950 beds by Nov-26 (turns 10, 35, 57) | Strategic | YES (supportive) | Reinforces moat/durability narrative |
| ROCE ~18% today, +150–200 bps in 12–18 months (turn 35) | Forward pillar input | YES | Only ROCE anchor given; feeds FTTCP ROCE verdict at H1 |
| Receivable-days target **revised to a realistic 125–130** (turn 4) | Forward | YES (positive) | Aligns with structural peer evidence; drops the old sub-100 optimism |
| ARPOB growth re-rated 3–5% historic → **10–12% for 2 years** (turn 62) | Forward | YES | The price leg of the 24% revenue bridge |
| Case-mix to 62% high-end (+440 bps), targeting further shift (turns 3, 54) | Backward/Forward | Moderate | Supports ARPOB and margin resilience |
| Bed guidance FY27 lowered 5,040→4,740; FY28 to 5,740/6,740 (turns 41–42) | Forward (revised) | YES | Near-term trim, out-year raise (endpoint inconsistent) |
| Mohali proof-point: acquired May-2023 at Rs 52 lakh/23 Cr rev, now ~Rs 23 Cr run-rate, margin 12–13%→~26% (turn 8) | Backward (case study) | Moderate | A delivered ramp precedent supporting the greenfield-fill bull case |

### 5B. What was NOT discussed (silence is signal)

| Expected topic | Why it should have come up | Significance |
|---|---|---|
| **Deferred-tax benefit / ETR 15.7%** | It, not interest, is the larger flatterer of +35% PAT (line 435) | **RED — actively re-attributed to interest (FN-16/20); CONFIRMATORY-NEGATIVE** |
| **Idle Rs 648mn IPO proceeds at zero yield / equipment object 84% behind / object-variation ballot** | Directly contradicts "fully funded, no material fresh debt" | **RED — masked by "fully funded" framing (FN-22); CONFIRMATORY-NEGATIVE** |
| **Absolute ARPOB level + same-store vs new-bed occupancy split** | The cleanest bull/bear metric; growth given but level withheld | AMBER — partial disclosure (FN-23) |
| **83.9% of consolidated PAT outside principal-auditor review** | Assurance concentration on the earnings pool | AMBER — never raised (FN-21) |
| **Standalone parent core loss-making (1.22% of consol PAT)** | Parent PBT below Other Income | AMBER (expected silence; logged FN-24) |
| **FY27 FCF / cash-flow bridge** | The FY27 FCF-inflection is the re-rating catalyst | AMBER — debt/FD spoken, no CFO |
| **Promoter remuneration** | Thesis-broken trigger #1 | AMBER — no figure spoken |
| **Dividend / payout policy** | Standard | Neutral (routine) |
| **Chairman's view on the two acquisitions** | Promoter absent | AMBER (FN-19) |

**Silence interpretation:** two items are **RED CONFIRMATORY-NEGATIVE** (tax re-attribution; "fully funded" masking the deployment problem) because management supplied an affirmatively competing narrative rather than merely omitting. The rest are AMBER first-quarter silences; consecutive-quarter escalation begins at Q2.

STOP cleared: 5A and 5B populated; second table not skipped.

---

## STEP 6 — TONE & SPECIFICITY ANALYSIS

**6A. Tone comparison.** No prior concall exists, so adjective-diff vs a prior call is N/A. Intra-call tone is **promoter-confident to the point of overconfidence**: "we can't see any challenge in terms of achieving the numbers... we are expecting that we will overachieve" (turn 9, FN-14); "no concern" on the capex/bed jump (turn 45); "zero patient grievances" (turn 83); "we remain super confident in the growth roadmap" (turn 86). Conservative read: the downside was asserted away rather than stress-tested.

**6B. Specificity score.** Quantified forward statements dominate: of the 34 forward phrases, ~22 carry a hard number/date/binary (the FY27 guide, 4,740/5,740 beds, 26.5–27% margin, 10–12% ARPOB, 150–200 bps ROCE, Rs 767 Cr capex, Rs 10–12 Cr Rudrapur capex, 70:30 payer, Rs 100/140 Cr Rudrapur, 125–130 days) vs ~12 soft ("on track," "we are expecting," "continuous process," "super confident," "will continue," "will overachieve"). **Specificity ratio ≈ 0.65 → HIGHLY SPECIFIC concall (>0.5).**

**6C. Defensive-language count.** 6 lexicon hedges (ledger §6): "too early to comment" / "cannot specify exact timeline" / "we are evaluating now opportunities" (all turn 51, dilution); "very difficult to actually project or predict" / "very difficult to say" (turn 55, case-mix); "can't see any challenge" (turn 9). **Count = 6 (just over the 5 threshold = mildly hedge-heavy), but concentrated on exactly two topics** — promoter-dilution timing and long-term case-mix — not pervasive across the call. Elsewhere management was specific.

**6D. Confidence indicators.** Named proof-point (Mohali ramp with dated economics, turn 8); specific commissioning dates (Nov–Dec 26, turn 2); numerical margin/ROCE/ARPOB commitments; dense dated bed roadmap. These are genuine confidence signals — but they are exactly what makes the disclosure-quality omission (tax) more, not less, concerning: high specificity everywhere except the one earnings-quality item.

**6E. Management archetype (Specificity × Credibility 2×2).** Specificity ratio **0.65 (>0.5)**. Credibility ratio **UNSCORED** (first call — no trailing delivery record). Therefore the archetype **cannot be formally placed** this quarter; it is provisional. **Provisional read: high-specificity guider with UNPROVEN delivery — OVERPROMISER RISK on watch.** The two CONFIRMATORY-NEGATIVE disclosure findings (FN-16/20 tax re-attribution; FN-22 "fully funded" masking) mean that IF Q2–Q4 delivery undershoots the very specific guide, this management lands squarely in the OVERPROMISER quadrant (hyper-specific guidance + poor delivery = anchor to filing numbers only). The archetype is formally set at Q2 FY27 once one quarter of the baseline register can be scored.

STOP cleared: 6A–6E shown; archetype provisional-with-reason, not asserted.

---

## STEP 7 — CROSS-REFERENCE vs FILING AND PEERS

### 7A. Concall narrative vs filing numbers (the core Role 5 numerical check)

| Concall claim (turn) | Filing evidence | Reconciliation |
|---|---|---|
| Q1 revenue "476 Cr, +19%" (2, 4) | 4,757.09mn = Rs 475.71 Cr; +19.27% (L418) | **CONFIRMED** |
| Q1 EBITDA ex-OI "126 Cr, 26.5%, +20%" (2, 4) | 1,260.88mn = Rs 126.09 Cr; 26.51%; +20.16% (1C) | **CONFIRMED** |
| Q1 PAT "89 Cr, 18.6%, +35%" (2, 4) | 885.93mn = Rs 88.59 Cr; 18.62%; +35.24% (L438) | **CONFIRMED** (total PAT basis) |
| **"PAT-margin +220 bps largely on reduction in interest outgo"** (4) | Finance cost −53.23mn YoY is real, BUT the Rs 93.40mn deferred-tax benefit / ETR 15.69% (L435) is the larger flatterer; +35% PAT normalises to ~+21% ex-tax | **CONTRADICTED (by omission of the dominant cause) — the claim is technically true and materially incomplete (FN-16/20)** |
| Term debt "25.6 Cr vs 28.2 Cr"; FD "300 Cr"; net worth "2,100 Cr" (4) | Term debt Rs 256mn (L75); FD Rs 2,998mn (L76) | **CONFIRMED** (FD 299.8 Cr ≈ "300") |
| "Fully funded... without recourse to material fresh debt" (2, 4) | Rs 648.32mn IPO idle at zero yield; equipment object 84% behind; object-variation ballot pending (MON) | **CONTRADICTED in spirit — "fully funded" masks a deployment problem (FN-22)** |
| Occupancy "56% vs 68%" (3) | −1,224 bps YoY to 55.6% (deck L112) | **CONFIRMED** |
| Both acquisitions within cost/bed discipline: "~54 lakh... ~70 lakh" (42) | Rudrapur Rs 0.54 Cr/bed; Mehar Rs 0.71 Cr/bed (Step 6C) | **CONFIRMED — both <Rs 1.0 Cr/bed** |

**GUIDANCE-vs-FILING ARITHMETIC BRIDGE (FN-01/FN-02 — the load-bearing numerical check):**

*Base consistency (guide vs FY26 filing):*
- Revenue: Rs 2,080 Cr ÷ FY26 Rs 1,679.36 Cr (L418) = **+23.9% ≈ the spoken +24%.** ✔ Ties cleanly.
- EBITDA: Rs 530 Cr ÷ FY26 operating EBITDA ex-OI Rs 444.32 Cr (1C) = **+19.3%**, NOT the spoken +25%. A literal +25% off Rs 444 Cr would be Rs 555 Cr. **The Rs 530 absolute and the "+25%" label cannot both hold against the FY26 base** (a ~Rs 25 Cr inconsistency); the Rs 530 absolute is the more conservative anchor and implies EBITDA margin ~25.5% on Rs 2,080 Cr revenue, slightly BELOW the 26.5–27% margin guide (turn 8) — a second minor internal tension.
- PAT: Rs 360 Cr ÷ FY26 total PAT Rs 273.56 Cr (L438) = **+31.6% ≈ the spoken +32%.** ✔ Ties on the total-PAT basis (matching the "89 Cr" Q1 total-PAT anchor).

*Path (a) — Q1 annualised run-rate:*
| Metric | Q1 FY27 (Rs Cr) | ×4 run-rate | FY27 guide | Implied H2 ramp |
|---|---:|---:|---:|---|
| Revenue | 475.71 (L418) | ~1,902.8 | ~2,080 | **+~Rs 177 Cr (+9.3%)** above flat run-rate — needs CGHS full-impact (Q2+) + new-bed fill (Rudrapur/Panchkula/Agra + 450 Q3 beds) |
| Op EBITDA | 126.09 (1C) | ~504.4 | ~530 | +~Rs 26 Cr (+5%) — achievable if 26.5–27% margin holds |
| PAT (total) | 88.59 (L438) | ~354.4 | ~360 | +~Rs 6 Cr — **but Q1 PAT is ETR-flattered at 15.69%** |

*Path (b) — ETR-normalised PAT (the dependency):*
- Q1 PBT Rs 105.08 Cr (L430). Normalise tax to ~25% (statutory 25.17%): Q1 PAT ≈ Rs 78.8 Cr. **×4 ≈ Rs 315 Cr** vs the Rs 360 Cr guide = a **~Rs 45 Cr (12.5%) gap.**
- **Therefore the +32% PAT guide requires EITHER the ~15.7% Q1 ETR to persist (i.e., the non-repeatable deferred-tax benefit to recur), OR EBITDA/volume to over-deliver enough to bridge ~Rs 45 Cr of PAT against a normalising ETR toward ~25%.** At the Rs 530 Cr EBITDA guide, working down through ~Rs 80 Cr D&A (FY26 Rs 62.5 Cr growing +27%), ~Rs 40 Cr finance (Q1 Rs 9.81 Cr ×4), +~Rs 32 Cr other income → PBT ~Rs 442 Cr; to reach Rs 360 Cr PAT the **embedded ETR is ~18.5%** — well below the 25% statutory. **The PAT guide is arithmetically consistent only on a sub-statutory tax rate.** Conservative bias: model FY27 PAT at ~Rs 320–335 Cr on a ~25% ETR unless management evidences a structural (e.g., 80-IBA new-hospital) tax shelter. **This is the priority Question-for-Management (Q16 below).**

### 7B. Peer concall cross-check
No other analysed-universe hospital operator reported a concall within ±4 weeks of this call in the supplied materials, so a direct peer-narrative cross-check is **not available this quarter (stated explicitly).** One indirect check: management claimed no CGHS-revision margin heat in oncology while "a few peers" face it (turns 22–23) — an internal-consistency assertion, not independently verifiable here; logged for the Q2 peer window.

### 7C. Concall vs external channel checks
The receivable-days revision to 125–130 (turn 4) aligns with the **structural peer evidence** in the Notion thesis (hospital debtor days run 100–140 on government-scheme mix), correcting the earlier sub-100 optimism — a credibility-positive alignment with third-party sector data. No other external source in the supplied set to cross-check.

STOP cleared: 7A/7B/7C shown; peer window explicitly noted empty.

---

## STEP 8 — THESIS & POSITION UPDATE (concall overlay on Section A)

### 8A. Growth-trigger status (concall overlay)

| Trigger | Status pre-concall (Sec A) | Concall evidence | Status post-concall |
|---|---|---|---|
| FY27 FCF inflection | DELAYED / UNVERIFIED | No CFO on call; CGHS routed to capex (FN-13) raises FY27 capex intensity | **DELAYED / UNVERIFIED** (first read Q2) |
| Bed roadmap 3,960→5,740 | ON TRACK | Rudrapur commissioned; 450 beds Nov–Dec; dated pipeline; FY27 trimmed to 4,740, FY28 to 5,740/6,740 | **ON TRACK** (near-term count trimmed; endpoint inconsistent — FN-03) |
| Margin defence ≥26% | ON TRACK (softening) | 26.5–27% reaffirmed full FY27 (FN-08); CGHS not a margin tailwind (FN-13) | **ON TRACK (held, not expanding)** |
| Affordable-core / ARPOB | WEAKENED (unverifiable) | ARPOB growth 10–12% given; absolute ARPOB still withheld (FN-23); Platinum premium extension | **WEAKENED (partially addressed)** |
| Capital-allocation discipline / war chest | AMBIGUOUS | "Fully funded" framing masks idle proceeds + object variation (FN-22); dilution by Dec-2028 flagged (FN-17) | **AMBIGUOUS (disclosure-quality now a named caveat)** |

### 8B. Watchlist items — concall reading

| Item | This concall reading | Status |
|---|---|---|
| Occupancy trajectory | FY27 to "moderate below 64%" pre-warned (FN-11); Q1 network 56% | RED (falling; management-flagged) |
| EBITDA margin | 26.5–27% reaffirmed full FY27 | GREEN (held) |
| ARPOB | growth 10–12% given; level withheld | AMBER |
| Debtor days | guided 125–130 (realistic) | GREEN-ish (guidance credible; Q1 actual ND) |
| Promoter dilution | ~8% by Dec-2028 via equity raise now explicit | AMBER (new forward-dilution watch) |
| CGHS uplift | full impact from Q2, routed to capex not margin | AMBER (margin-neutral) |

### 8C. Thesis-broken trigger check (all four, citing the call)

| Condition | Threshold | Concall-relevant evidence | FIRED? |
|---|---|---|---|
| 1. Promoter remuneration >30% PAT, 2 yrs | >30% ×2yr | **Not discussed on call (ND)**; FY25=27.5%, FY26 pending AR | **NO** (not testable) |
| 2. Debtor days >175, 2 quarters | >175 ×2Q | Call **guides 125–130** (turn 4) — well below trigger; Q1 actual ND | **NO** |
| 3. EBITDA margin <22%, 2 quarters | <22% ×2Q | Call **reaffirms 26.5–27% full FY27** (turns 8/9/30); Q1 op 26.51% | **NO** |
| 4. Acquisition >Rs 1.0 Cr/bed | >Rs 1.0 Cr/bed | Call **reconfirms both** — Rudrapur ~54 lakh, Mehar ~70 lakh/bed (turn 42) | **NO** |

**All four triggers NOT FIRED on the call.** No undisclosed material RISK that fires a trigger; no undisclosed material POSITIVE warranting action on noise. Decision Status stays **WATCHLIST.**

### 8D. Four-Pillar inputs — concall adjustments

| Pillar | Pre-concall | Concall evidence | Post-concall |
|---|---|---|---|
| ROCE Base | ND (no BS) | ~18% today, +150–200 bps in 12–18 months (FN-09, turn 35) | **Hold** — forward commentary only; FTTCP ROCE verdict re-run at H1 when a balance sheet exists (no pillar revision on spoken ROCE) |
| Cash Multiplier | INDETERMINATE | No CFO on call; CGHS→capex raises intensity | **Hold — INDETERMINATE** |
| Growth Visibility Premium | + | Dense dated roadmap reaffirmed; densification logic | Hold (supportive) |
| Strategic Premium | Conditional | Remuneration ND; single-credit rule respected (ROCE recovery credited in Pillar 1, not double-counted here) | Hold |

No pillar is revised on concall commentary alone (spoken ROCE is not a balance-sheet-verified input). **Destination PE unchanged at 23.2x; Hurdle Ratio stays in the STOP band at CMP** (Section A Step 7). Fair value recompute deferred to H1.

### 8E. Position decision (8A-W).
Credibility ratio is **UNSCORED** (first call) — the "<60%" discount rule cannot mechanically fire, but the two CONFIRMATORY-NEGATIVE disclosure findings warrant a **precautionary discount on the PAT guide** (model ~Rs 320–335 Cr, not Rs 360 Cr). No DROPPED commitments (no prior call). No undisclosed trigger-firing risk. No position exists → no trim/add. **Action: continue to AVOID at CMP; retain WATCHLIST; entry zone unchanged Rs 101–126.** Master decision gate remains Q2 FY27 (H1: cash-flow statement, Rudrapur consolidation, balance sheet, first delivery-scoring of the guidance baseline).

### 8F. Updated questions for next quarter — folded into the Questions-for-Management table (Section C).

STOP cleared: 8A–8F complete.

---

## CONCALL VERDICT (Step 9 block; no Notion write performed by A4)

- **Management Credibility (this quarter):** **UNSCORED** — first concall; no trailing-4-quarter record. Baseline registered (Step 3).
- **Trailing-4-Quarter Credibility Ratio:** N/A (0 prior commitments scored). First computable Q2 FY27.
- **Management Archetype (6E):** provisional **HIGH-SPECIFICITY / DELIVERY-UNPROVEN — OVERPROMISER RISK on watch** (specificity 0.65; credibility unscored). Formally placed at Q2.
- **Role 1 Track-Record Input:** N/A this quarter (no ratio; not substitutable by session judgment).
- **Net concall impact on thesis:** **MAINTAINED.** No trigger fired; guidance supportive on revenue/beds/margin; PAT guide quality-caveated; disclosure-quality caveat added. Not strengthened (the PAT beat is tax-flattered and the tax silence is a governance negative), not broken.
- **Position decision:** **AVOID at CMP / WATCHLIST retained.** Entry zone unchanged.

*Concall reviewed 2026-08-04 | Source: extract_concall_parkhosps_q1fy27.txt (87 turns).*

---

# SECTION C — COMBINED VERDICT

**Filing-derived signals (Role 4, unchanged):** genuinely strong operating core (revenue +19.3% YoY, core PBT ex-OI +29.9% YoY, op EBITDA margin held at 26.5%), but the +35% PAT headline is **~21% real** once the non-repeatable Rs 93.40mn deferred-tax benefit is stripped; standalone parent is core loss-making (rescued by IPO-cash interest); 83.9% of consolidated PAT is not principal-auditor-reviewed (Rs 26mn reviewed by no auditor — the SOUTHWEST-style flag); occupancy fell 1,224 bps YoY on a bed-led (not utilisation-led) growth model; QoQ margin and occupancy both softened.

**Concall-derived signals (Role 5, this merge):** first hard FY27 guide Rs 2,080 / 530 / 360 Cr (24/25/32%) — revenue and PAT-growth-% reconcile to the FY26 base, but the **PAT guide is arithmetically consistent only on a sub-statutory (~18–19%) ETR persisting** (ETR-normalised annualised PAT ≈ Rs 315 Cr vs Rs 360 Cr guide, a ~Rs 45 Cr gap requiring the deferred-tax benefit to recur or a material H2 EBITDA over-delivery). Positives weighed symmetrically: EBITDA margin 26.5–27% reaffirmed; **debtor-days guidance revised to a realistic 125–130** (aligns with structural peer evidence, corrects the old sub-100 claim); Rudrapur economics disclosed (~Rs 100 Cr FY27 rev, ~20–22% EBITDA); densification/cluster logic articulated; ARPOB growth 10–12% for two years; ROCE ~18% guided +150–200 bps; case-mix to 62% high-end. Negatives: **disclosure quality** — management attributed the +220 bps PAT-margin lift solely to interest reduction and was **silent on the deferred-tax benefit** (FN-16/20, a competing causal story), and asserted "fully funded... without recourse to material debt" while Rs 648mn IPO cash sits idle, the equipment object is 84% behind and an object-variation ballot is pending (FN-22). Chairman absent (FN-19); CFO fielded the forward guidance; four internal inconsistencies (FN-18: 5,740 vs 6,740 beds, 34/36/37 lakh capex/bed, 2 vs 22 Aug, 330 vs 331) treated as data-precision + garble, not thesis-moving. Explicit **forward-dilution signal**: ~8% promoter divestment to 75% by Dec-2028 via an acquisition-linked equity raise (FN-17).

**Presentation/release + monitoring signals (unchanged):** the deck/release foreground the tax-and-finance-flattered +35% and background the occupancy/QoQ deterioration; M&A framing inconsistency (100% vs 80% Rudrapur); Rs 648mn idle at zero yield; equipment object 84% behind; Rs 2,453mn "unidentified" spent with no named target.

**Reconciliation between filing and call:** the numbers tie out (Step 7A CONFIRMED on every reported metric). The divergence is one of **emphasis and disclosure quality, now reinforced by the call**: management verbally re-attributed the PAT-margin expansion to interest and stayed silent on tax — a stronger negative than the deck's mere foregrounding, because it is an affirmatively competing narrative. Filing numbers govern for valuation and trajectory; the concall governs management-credibility read; the discrepancy is logged as the load-bearing disclosure-quality caveat.

**Four-trigger check (re-run citing the call): NONE fired.** (1) Promoter remuneration — ND, not discussed. (2) Debtor days — call **guides 125–130**, below the >175 trigger. (3) EBITDA margin — call **reaffirms 26.5–27%**, above the <22% trigger. (4) Acquisition cost/bed — call **reconfirms Rudrapur ~54 lakh / Mehar ~70 lakh**, both <Rs 1.0 Cr/bed. **Decision Status stays WATCHLIST (AVOID at CMP Rs 292.55).**

**Cash conversion: INDETERMINATE** (no Q1 cash-flow statement; the call added no CFO figure and, via CGHS→capex routing, points to higher FY27 capex intensity) → verdict capped at **PROCEED WITH CAVEATS**, missing evidence named (CFO/FCF, receivable days actual, capex — first read at H1 FY27/Q2).

**PROTOCOL VERDICT: PROCEED WITH CAVEATS.** The merged review is complete and internally consistent across both protocols. Caveats: (1) cash conversion INDETERMINATE this quarter (no Q1 cash-flow statement); (2) 83.9% of consolidated PAT outside principal-auditor review; (3) the +35% PAT headline flattered ~14 pp by a non-repeatable deferred-tax benefit, and the **FY27 PAT guide is consistent only on a sub-statutory ETR persisting** (Step 7A bridge); (4) **disclosure quality** — the call re-attributed the margin lift to interest and was silent on the deferred tax (FN-16/20), and framed the build as "fully funded" while masking idle IPO proceeds and the object-variation ballot (FN-22); (5) occupancy deterioration on a bed-led growth model with absolute ARPOB still undisclosed; (6) an explicit forward-dilution signal (~8% by Dec-2028). None is a mechanical failure and none fires a pre-committed trigger, so the verdict is not REWORK or INSUFFICIENT EVIDENCE; but the INDETERMINATE cash test, the unaudited-contribution flag and the tax-silence disclosure-quality finding preclude a clean PROCEED. **Decision Status: WATCHLIST. Net thesis impact of the call: MAINTAINED.**

**Watchpoints for next quarter:** (i) H1 cash-flow statement — FCF-inflection first read; (ii) consolidated ETR — a return to ~23–25% confirms the Q1 PAT beat was one-off; (iii) consolidated blended occupancy — bull ≥60% & rising, bear <55% & falling; (iv) CGHS full-impact realisation from Q2 and whether it reaches EBITDA or only capex; (v) score the FY27 guidance baseline (B1–B12) for the first credibility-ratio computation.

---

## STEP 8.5 — QUESTIONS FOR MANAGEMENT

Every A3 FORWARD-SIGNAL or AMBIGUOUS finding — filing and concall — generates ≥1 question. Concall additions Q16–Q22 map to FN- findings; the prior 15 (filing) are retained with their concall answer-status marked. Channel: next concall / IR email.

| # | Question | Why it matters | Answered by this call? | from_finding_id |
|---|---|---|---|---|
| 1 | The Rs 93.40mn deferred-tax benefit (line 435) cut ETR to 15.7% from 20.0% and lifted PAT ~Rs 45–90mn. Source, and normalized go-forward ETR? | Tests whether +35% PAT (and the Rs 360 Cr guide) is repeatable | **NOT ADDRESSED — re-attributed to interest; ESCALATE** | RES-A3-06; PRES-A4; REL-FND-03; FN-16; FN-20 |
| 2 | Standalone core PBT ex-OI is negative (−Rs 29.57mn); parent PBT (17.11mn) is below Other Income (46.68mn). Composition, and is the parent structurally loss-making as IPO cash deploys? | Parent earnings are IPO-cash interest, shrinking as cash is spent | **NOT ADDRESSED** | RES-A3-02; FN-24 |
| 3 | Rs 26.00mn PAT across 2 subs is management-reviewed only; 83.9% of consolidated PAT is other-auditor-reviewed (line 342). Which entities, what controls? | Assurance concentration on the earnings pool | **NOT ADDRESSED** | RES-A3-03; FN-21 |
| 4 | With Rs 648mn IPO proceeds idle at zero yield vs Rs 2,840mn announced M&A, what is the funding path, what does the object-variation ballot cover, and how was the Rs 2,453mn "unidentified acq/GCP" deployed (no target named)? | Capital-allocation credibility vs the "fully funded" claim | **PARTIAL / masked by "fully funded" framing** | RES-A3-08; MON-A3-F1-02; MON-A3-F1-01; FN-22 |
| 5 | Medical-equipment IPO object ~84% behind schedule (Rs 36.08 of 229.59mn): procurement timing or commissioning slippage at Panchkula/Ambala/Jaipur? | Benign lag vs roadmap slippage | **NOT ADDRESSED** | MON-A3-F6-01 |
| 6 | Rohtak (Park Medicity NCR): deployment timeline; Rs 409.81mn remaining; bed-commissioning date? | Only live IPO-funded bed project | **NOT ADDRESSED** | MON-A3-F6-02 |
| 7 | Occupancy 55.6% (−1,224 bps YoY): split same-store vs new-bed dilution; disclose **absolute** consolidated and same-store **ARPOB** (and the Platinum premium); expected occupancy trough/recovery quarter? | The cleanest bull/bear metric; ARPOB level still withheld | **PARTIAL — network occupancy & ARPOB growth given; absolute ARPOB + same-store split NOT given** | PRES-A8; PRES-A9; PRES-A7; REL-FND-06; REL-FND-07; REL-FND-02; FN-23 |
| 8 | The bed build is "fully funded... without material fresh debt" with an equity backstop. Will fresh equity be raised or debt drawn, how much and when? | Dilution/leverage risk | **PARTIAL — equity raise now flagged (see Q17)** | PRES-A3; FN-22 |
| 9 | Rudrapur is a "100% acquisition" but 80% now / 20% by FY30 — put/call terms, price of the 20%, interim minority drag? | Deferred outflow + minority deduction to FY30 | **NOT ADDRESSED** | PRES-A6 |
| 10 | Rudrapur (nil Q1) consolidates from Q2 — what first-quarter revenue/EBITDA and minority contribution to model? | Q2 mix + first minority line | **PARTIAL — FY27 rev ~Rs 100 Cr / EBITDA 20–22 Cr guided; no explicit Q2 split** | PRES-A1; FN-04 |
| 11 | PAT grew 35% but EPS 20% (~12% IPO dilution) — confirm weighted-avg basic vs diluted share count and any raise into the ~75% floor. | Per-share growth is the real 20%; dilution headroom | **PARTIAL — ~8% divest by Dec-2028 confirmed (see Q17)** | PRES-A5; REL-FND-04; FN-17 |
| 12 | Exceptional line is nil through the Devina Derma divestment and ahead of Rs 2,840mn M&A — where is the disposal result booked, and what acquisition-accounting effects to expect? | Divestment result location + goodwill/bargain-purchase/minority | **NOT ADDRESSED** | RES-A3-01 |
| 13 | Consolidated actuarial remeasurement swung to −Rs 7.76mn from +Rs 4.15mn (~92% of full-FY26 move in one quarter) — what assumption changed? | Assumption change affecting OCI | **NOT ADDRESSED** | RES-A3-07 |
| 14 | Provide one reconciled bed roadmap: CY26 adds 1,490 vs 1,450; as-on-date 4,290 vs 3,960 quarter-end; FY28 endpoint 5,740 vs 6,740; capex/bed 34/36/37 lakh; Rudrapur 2 vs 22 Aug, 330 vs 331 beds. Confirm dated milestones. | Persistent cross-document + intra-call inconsistencies on the core growth thesis | **PARTIAL — roadmap detailed but new inconsistencies added (FN-18)** | RES-A3-05; PRES-A2; REL-FND-01; REL-FND-05; FN-03; FN-18 |
| 15 | Healplus (incorporated 20-May, pre-period-end) is absent from the 23-entity consolidation list — why the omission? | Entity-list completeness under heavy M&A | **NOT ADDRESSED** | RES-A3-10 |
| **16** | **The FY27 PAT guide of Rs 360 Cr (+32%) implies a sub-statutory ETR (~18–19%) persisting — Q1's 15.7% annualised gets ~Rs 354 Cr, but ETR-normalised to 25% the run-rate is ~Rs 315 Cr, a ~Rs 45 Cr gap. What ETR is embedded, and is there a structural (80-IBA) shelter, or does the guide need H2 EBITDA over-delivery?** | The core guidance-vs-filing arithmetic; determines whether the PAT guide is real or tax-dependent | **NOT ADDRESSED (guide given, ETR basis not)** | FN-01; FN-02 |
| **17** | **Promoter divestment to 75% (~8%) by Dec-2028 via an "acquisition-linked equity raise" — fresh issue or OFS, expected size/timing, and what dilution % should we model against the Rs 101–126 entry zone?** | Explicit forward dilution; per-share value impact | **PARTIAL — obligation & Dec-2028 window given; mechanism/size/timing hedged (FN-12)** | FN-17; FN-12 |
| **18** | **CGHS 7–7.5% benefit is stated to route to equipment/capex rather than EBITDA — quantify the split between margin uplift and capex, and confirm what reaches FY27 EBITDA from Q2.** | Removes a presumed margin tailwind; feeds the 26.5–27% margin and Rs 530 Cr EBITDA guide | **PARTIAL — routing disclosed (FN-13); amounts not quantified** | FN-10; FN-13 |
| **19** | **Zirakpur (Mehar) FY28 first-year revenue was spoken as "705 Cr" against a ~Rs 70–75 Cr scale for a 150-bed first-year asset — please confirm the correct figure and the EBITDA-margin assumption.** | A garbled but material catalyst number; must not be carried forward unverified | **N/A — new garble to resolve** | FN-05 |
| **20** | **Why was the Chairman (Dr. Ajit Gupta) absent from a call covering two acquisitions and a bed-guidance change, and who owns capital-allocation sign-off?** | Governance / promoter engagement signal | **NOT ADDRESSED (absent)** | FN-19 |
| **21** | **Management said it "can't see any challenge... we will overachieve" against an occupancy-drag question — what is the downside case if same-store occupancy also softens, and what occupancy trough underpins the 26.5–27% margin guide?** | Overconfidence hedge; downside not stress-tested | **NOT ADDRESSED (asserted away)** | FN-14 |
| **22** | **Management declined any long-term case-mix target ("very difficult to predict") while committing specifically to 10–12% ARPOB for 2 years — reconcile the specificity gap; what high-end mix underpins ARPOB?** | Selective specificity; ARPOB bridge depends on mix | **PARTIAL — refused the target (FN-15)** | FN-15 |

**Top 3 by likelihood of thesis-changing information:**
1. **Q16 / Q1 (deferred-tax & the PAT guide's embedded ETR)** — resolves whether Rs 360 Cr FY27 PAT is real or tax-dependent; the single most material earnings-quality question, made sharper by the call's silence.
2. **Q7 (occupancy split + absolute ARPOB)** — same-store ≥66% with rising ARPOB confirms the bed-led model is scaling; same-store weakness breaks the affordable-core thesis.
3. **Q17 (dilution mechanism/size)** — sizes the future share-count expansion against the entry zone.

**Channel:** IR email now with all 22 verbatim; prioritise the top 3 for the next live call. These become the Role 5 promise-vs-delivery / answer-status baseline for Q2 FY27.

---

## MONITORABLES / CATALYST LIST (seeded by A3 commitment registers + board items + concall baseline)

| # | Item | Implied date | Source ref |
|---|---|---|---|
| 1 | H1 FY27 (Q2) cash-flow statement — first FCF-inflection read (capex vs CFO) | Q2 FY27 (Nov-2026) | Reg 33 half-yearly; Notion monitorable 1 |
| 2 | Rudrapur (V3) consolidation + first minority-interest line | Q2 FY27 | PRES-A1 (L506); FN-04 (turn 10) |
| 3 | Palam Vihar / Park Platinum +100 beds commissioned | Nov 2026 | RES note 4 (L228); PRES C4; turn 42 |
| 4 | Mehar-Zirakpur acquisition completion (Rs 107 Cr, 150 beds) | 3-Dec-2026 (commission Nov–Dec) | Board item 2 (L62/584); REL-FND-01; turn 2 |
| 5 | Narela/Febris Delhi 200-bed commissioning | Dec 2026 | PRES C5 (L811); turn 2 |
| 6 | IPO object-variation postal-ballot notice & outcome | "in due course" | Board item 3 (L68); RES-A3-08; FN-22 |
| 7 | Rohtak (Park Medicity NCR) IPO deployment — Rs 409.81mn remaining | ongoing FY27 | MON-A3-F6-02 (L400-406) |
| 8 | Medical-equipment IPO object catch-up — Rs 238.51mn unutilised | subsequent period / FY27 | MON-A3-F6-01 (L580-592) |
| 9 | Exit FY27 at 4,740 beds | Mar 2027 | PRES C11; turns 2, 42 |
| 10 | Gorakhpur O&M (400 beds) | Apr 2027 | PRES C10 (L810) |
| 11 | Mohali expansion +150 (350→500) | Sep 2027 | RES note 4/consol (L490); PRES C7 |
| 12 | Ambala expansion +200 (250→450) | Oct 2027 | PRES C8 (L794); turn 55 |
| 13 | Rohtak greenfield 250 beds | Jan 2028 | PRES C9 (L791) |
| 14 | Reach 5,740 beds [call restated 6,740 — reconcile] | Mar 2028 | PRES C12; turns 2, 42; FN-03 |
| 15 | Rudrapur remaining 20% ownership acquired | by 30-Apr-2030 (FY30) | RES note 8 (L266); PRES C3 (L533) |
| 16 | FY26 promoter-remuneration disclosure (AR) — Strategic Premium / trigger #1 | next AR/AGM | Notion monitorable 2; trigger #1; FN silence M6 |
| 17 | Panchkula NABH accreditation (+4 hospitals targeted FY27) | in process / FY27 | deck L446; PRES C15; FN (turn 3) |
| **18** | **FY27 GUIDANCE BASELINE — Rs 2,080 Cr rev / Rs 530 Cr EBITDA / Rs 360 Cr PAT (24/25/32%): score DELIVERED/PARTIAL/MISSED at each of Q2/Q3/Q4 (promise-vs-delivery tracker STARTS here)** | Q2 FY27, Q3 FY27, Q4/FY27 | FN-01 (turn 7); Step 3 baseline B1 |
| **19** | **CGHS full-impact realisation from Q2 — and whether it reaches EBITDA or only capex** | Q2 FY27 | FN-10 / FN-13 (turns 3, 21, 26) |
| **20** | **Consolidated ETR trajectory — return toward ~23–25% would confirm the Q1 PAT beat was a one-off deferred-tax benefit** | Q2 FY27 | FN-02 (turn 7 vs line 435) |
| **21** | **Equity raise into the ~75% promoter floor (~8% divest) by Dec-2028 — watch for the acquisition-linked issue/OFS and dilution size** | by Dec-2028 (event-driven) | FN-17 / FN-12 (turn 51) |
| **22** | **ARPOB growth 10–12% p.a. and absolute ARPOB disclosure; payer mix to 70:30 in 12–18 months; ROCE +150–200 bps in 12–18 months** | 12–18 months (score at Q2+) | FN-06 / FN-07 / FN-09 / FN-23 (turns 35, 61, 62) |

---

## PLAIN-LANGUAGE BRIEF (mandatory standing deliverable)

*Provenance labels: [Notion/peer] = prior thesis / peer work; [filing] = this quarter's four filing documents; [call] = this quarter's concall.*

### 1. Summary narrative

Park Medi World grew Q1 FY27 consolidated revenue 19% to Rs 476 crore and held its operating margin at 26.5% [filing], a solid operating quarter for a hospital chain that has just expanded its bed count 32% in a year to 3,960 beds [filing/call]. The reported profit jumped 35% to Rs 89 crore, but roughly two-thirds of the "extra" growth above the ~20% operating rate is not repeatable: a Rs 9.3 crore deferred-tax benefit dropped the tax rate to 15.7% from 20%, and a 35% fall in interest cost (the IPO paid off the debt) did the rest [filing]. Strip the tax benefit and profit grew about 21%, in line with the business [filing]. On the call — the company's first ever earnings call — management gave its first hard FY27 guidance: revenue about Rs 2,080 crore (+24%), EBITDA about Rs 530 crore (+25%), profit about Rs 360 crore (+32%) [call]. The revenue and profit-growth-% numbers tie cleanly to last year's base, but the profit guide only works if that low tax rate keeps recurring: annualise Q1 at a normal 25% tax and you get about Rs 315 crore, roughly Rs 45 crore short of the Rs 360 crore promise [filing/call]. The most important governance point is what management chose to say: they credited the whole margin improvement to lower interest and never mentioned the tax benefit that actually did more of the work [call]. They also called the growth plan "fully funded... without recourse to material fresh debt" while Rs 648 crore of IPO money sits idle earning nothing, the medical-equipment spending is 84% behind schedule, and a shareholder vote to re-purpose IPO objects is pending [filing/call]. Set against that, several things were genuinely reassuring: the debtor-days target was cut to a realistic 125–130 days (matching how the sector actually behaves) instead of the old sub-100 optimism [call/Notion]; margins were reaffirmed at 26.5–27% for the full year [call]; the Rudrapur acquisition economics were laid out (about Rs 100 crore revenue this year at 20–22% EBITDA) [call]; and ARPOB (revenue per bed) growth was guided at 10–12% for two years [call]. The occupancy story is the swing factor: network occupancy fell to 56% from 68% because 960 new beds entered the denominator before they filled up [filing/call]; management pre-warned that full-year occupancy will stay below last year's 64% [call]. Whether that is just new-bed dilution (fine) or same-store weakness (a problem) cannot be settled until they disclose the same-store split and the absolute ARPOB, both still withheld [call]. There is also a flagged future dilution: the promoter must cut its stake about 8 points to 75% by December 2028 and intends to do it through an acquisition-linked equity raise [call]. The stock at Rs 292.55 is roughly 2.3x our AVOID line of Rs 126 [Notion/filing], the hurdle-ratio check is firmly in the STOP band, and the verdict stays PROCEED WITH CAVEATS with the position on WATCHLIST — AVOID at this price. The next real test is the H1 results (Q2), which bring the first cash-flow statement, the Rudrapur consolidation, and the first chance to score this guidance.

### 2. Sector intelligence

Park operates in Indian multi-super-speciality hospitals with a government-scheme-heavy payer mix (77% government insurance, 23% cash/TPA) [call], graduating toward 70:30 over 12–18 months [call]. The dominant regulatory variable this year is the CGHS rate revision (12–15% hike effective October 2025) [call]; management expects a 7–7.5% blended benefit with full impact from Q2 [call], but crucially says it will spend that uplift on equipment and maintenance capex rather than let it drop to EBITDA [call] — so the payer tailwind supports "margins held," not "margins expanding." Sector demand is structurally supported by under-served tier-2/tier-3 and hill-state catchments (J&K, Himachal, upper UP funnelling toward the Chandigarh tri-city and Delhi) [call], which underpins Park's cluster/densification strategy. Debtor days of 100–140 are structural for government-scheme hospitals [Notion/peer], which is why the revised 125–130 guidance [call] reads as credible rather than a concession. Sector risk to watch: government-scheme reimbursement timing and any CGHS pushback on specific specialties (peers reportedly seeing oncology margin heat; Park claims none) [call].

### 3. Business-model intelligence

Park makes money by acquiring or building multi-super-speciality hospitals, filling them with high-end tertiary/quaternary work (62% high-end case mix, +440 bps YoY) [filing/call], and running them at a low capex-per-bed (~Rs 36 lakh blended, claimed lowest among listed peers) [call]. The model is IPD-heavy (94.4% of revenue) [filing]; OPD is deliberately run as a near-free funnel, not a profit centre [call]. Unit economics as disclosed for Rudrapur: acquired for ~Rs 177 crore (~Rs 54 lakh/bed), targeting ~Rs 100 crore revenue and 20–22% EBITDA in year 1, ramping to ~Rs 140 crore [call] — below the group's 26.5% margin initially, so new assets dilute margin before they lift it. The structural model-drift signal this quarter is that the consolidated result is now almost entirely a subsidiary story: the standalone parent contributes just 1.22% of group PAT and is loss-making before Other Income (which is just interest on idle IPO cash) [filing]. The re-rating catalyst the thesis leans on — the FY27 free-cash-flow inflection — is untestable this quarter (no Q1 cash-flow statement) [filing] and, given CGHS money routed to capex plus a 84%-behind equipment programme [filing/call], capex intensity may stay high. ROCE is guided at ~18% today improving 150–200 bps over 12–18 months [call], the only forward return anchor given.

### 4. Competition intelligence

Park's structural edge is cost: the lowest capex-per-bed among listed peers [call] and an affordable-tertiary positioning that pulls cash/TPA patients up from premium chains [call], plus a doctor model built on salaried full-time consultants with performance bonuses and ESOPs rather than celebrity visiting consultants — which management links to low consultant attrition and "zero patient grievances" [call]. Its densification/cluster play (Tricity to ~950 beds by Nov-2026, becoming the largest provider there) is a genuine local-scale moat in chosen catchments [call/Notion]. Where Park is structurally weaker or unproven versus larger listed hospital peers: (a) governance/disclosure maturity — the first-call tax silence, the Chairman's absence, and four internal number inconsistencies contrast with the cleaner IR of established peers [call]; (b) absolute ARPOB is undisclosed, so its revenue-per-bed cannot be benchmarked against peers who report it [call/filing]; (c) 83.9% of consolidated PAT sits outside the principal auditor's review, an assurance-scope gap larger peers do not carry [filing]. The competitive risk to watch is that Park is buying growth (two acquisitions this quarter, more signalled) into a still-diluting occupancy base while a peer with better disclosure and a proven fill curve could be valued more cheaply on comparable growth. No peer concall fell within the ±4-week window this quarter, so the direct narrative cross-check reruns at Q2 [call].

---

*Reviewed 2026-08-04 (Role 5 merge) | Sources: results.pdf (Reg 33), presentation.pdf (26-slide deck), earnings_release.pdf (Reg 30), monitoring_agency.pdf (CRISIL Reg 32(6)), concall transcript (87 turns). Role 5 executed in full. Verdict: PROCEED WITH CAVEATS. Decision Status: WATCHLIST (AVOID at CMP). No thesis-broken trigger fired. Management credibility UNSCORED (first concall); baseline registered. Net concall impact: MAINTAINED.*

```yaml
stage: A4-analyst
company: "PARKHOSPS"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
docs_merged: [results, presentation, release, monitoring, concall]
ledger_reconciliation:
  notes: 37                       # results 22 + monitoring 15
  turns: 87                       # concall transcript (Role 5)
  slides: 26                      # presentation deck (release = 4 pages, also reviewed)
  all_reviewed: true
  a3_findings_incorporated: ["RES-A3-01","RES-A3-02","RES-A3-03","RES-A3-04","RES-A3-05","RES-A3-06","RES-A3-07","RES-A3-08","RES-A3-09","RES-A3-10","PRES-A1","PRES-A2","PRES-A3","PRES-A4","PRES-A5","PRES-A6","PRES-A7","PRES-A8","PRES-A9","REL-FND-01","REL-FND-02","REL-FND-03","REL-FND-04","REL-FND-05","REL-FND-06","REL-FND-07","MON-A3-F1-01","MON-A3-F1-02","MON-A3-F6-01","MON-A3-F6-02","MON-A3-F7-01","MON-A3-F14-01","FN-01","FN-02","FN-03","FN-04","FN-05","FN-06","FN-07","FN-08","FN-09","FN-10","FN-11","FN-12","FN-13","FN-14","FN-15","FN-16","FN-17","FN-18","FN-19","FN-20","FN-21","FN-22","FN-23","FN-24"]
protocol_verdict: "PROCEED WITH CAVEATS"
cash_conversion: "INDETERMINATE"
decision_status_verified: "WATCHLIST (AVOID at CMP)"
position_branch: "8A-W"
sc_gap_pat_pct: [{period: "Q1FY26", standalone_pct_of_consol: 7.48}, {period: "Q4FY26", standalone_pct_of_consol: 11.21}, {period: "Q1FY27", standalone_pct_of_consol: 1.22}, {period: "FY26", standalone_pct_of_consol: 13.39}]
credibility_ratio: "UNSCORED — first concall on record; baseline registered, first computable Q2 FY27"
management_archetype: "provisional HIGH-SPECIFICITY / DELIVERY-UNPROVEN (specificity 0.65; credibility unscored) — OVERPROMISER RISK on watch"
guidance_fy27: {revenue_cr: 2080, revenue_growth_pct: 24, ebitda_cr: 530, ebitda_growth_pct: 25, pat_cr: 360, pat_growth_pct: 32, source: "turn 7 (L24)"}
guidance_arithmetic: "Rev 2080/FY26 1679.36 = +23.9% ties; PAT 360/FY26 273.56 = +31.6% ties; EBITDA 530/FY26 op-EBITDA 444.32 = +19.3% (NOT the spoken +25%). Q1 PAT 88.59x4=354.4 near guide ONLY on 15.7% ETR; ETR-normalised to 25% => ~315cr, ~45cr short => guide embeds ~18-19% ETR persisting or needs H2 EBITDA over-delivery. Conservative model ~320-335cr."
questions_for_management:
  - {q: "Source and go-forward normalized ETR of the Rs 93.40mn deferred-tax benefit (ETR 15.7%); NOT addressed on call - re-attributed to interest - ESCALATE", from_finding_id: ["RES-A3-06","PRES-A4","REL-FND-03","FN-16","FN-20"]}
  - {q: "Composition of Rs 46.68mn standalone Other Income; is the parent structurally loss-making as IPO cash deploys", from_finding_id: ["RES-A3-02","FN-24"]}
  - {q: "Identity/controls of the 2 management-only-reviewed subsidiaries; 83.9% of PAT outside principal-auditor review", from_finding_id: ["RES-A3-03","FN-21"]}
  - {q: "Funding path for Rs 2,840mn M&A vs Rs 648mn idle IPO; scope of object-variation ballot; deployment of Rs 2,453mn unidentified-acq/GCP", from_finding_id: ["RES-A3-08","MON-A3-F1-02","MON-A3-F1-01","FN-22"]}
  - {q: "Medical-equipment IPO object 84% behind: procurement timing or commissioning slippage", from_finding_id: ["MON-A3-F6-01"]}
  - {q: "Rohtak (Park Medicity NCR) deployment timeline; Rs 409.81mn remaining; bed-commissioning date", from_finding_id: ["MON-A3-F6-02"]}
  - {q: "Occupancy same-store vs new-bed split; disclose ABSOLUTE ARPOB + Platinum premium; occupancy trough - only growth given on call", from_finding_id: ["PRES-A8","PRES-A9","PRES-A7","REL-FND-06","REL-FND-07","REL-FND-02","FN-23"]}
  - {q: "Fresh equity vs debt to fund the +59% build; equity raise now flagged (see dilution Q)", from_finding_id: ["PRES-A3","FN-22"]}
  - {q: "Rudrapur put/call terms and price of remaining 20% (80%-now/20%-by-FY30); interim minority drag", from_finding_id: ["PRES-A6"]}
  - {q: "Rudrapur Q2 first revenue/EBITDA and minority contribution - FY27 ~100cr/20-22% guided, no Q2 split", from_finding_id: ["PRES-A1","FN-04"]}
  - {q: "Weighted-avg basic vs diluted share count (PAT +35% vs EPS +20%) and raise into ~75% floor", from_finding_id: ["PRES-A5","REL-FND-04","FN-17"]}
  - {q: "Where is the Devina Derma disposal result booked; expected acquisition-accounting effects", from_finding_id: ["RES-A3-01"]}
  - {q: "What assumption drove the actuarial remeasurement swing to -7.76mn (~92% of full FY26 move)", from_finding_id: ["RES-A3-07"]}
  - {q: "One reconciled bed roadmap (1,490 vs 1,450; 4,290 vs 3,960; 5,740 vs 6,740; 34/36/37 lakh; 2 vs 22 Aug; 330 vs 331)", from_finding_id: ["RES-A3-05","PRES-A2","REL-FND-01","REL-FND-05","FN-03","FN-18"]}
  - {q: "Why is Healplus (incorporated 20-May, pre-period-end) absent from the consolidation entity list", from_finding_id: ["RES-A3-10"]}
  - {q: "FY27 PAT guide Rs 360cr (+32%) implies sub-statutory ETR ~18-19% persisting - what ETR is embedded / structural 80-IBA shelter / needs H2 EBITDA over-delivery?", from_finding_id: ["FN-01","FN-02"]}
  - {q: "Promoter ~8% divest to 75% by Dec-2028 via acquisition-linked equity raise - fresh issue or OFS, size/timing, dilution % vs entry zone?", from_finding_id: ["FN-17","FN-12"]}
  - {q: "CGHS 7-7.5% routed to capex not EBITDA - quantify the margin-uplift vs capex split and what reaches FY27 EBITDA from Q2", from_finding_id: ["FN-10","FN-13"]}
  - {q: "Zirakpur FY28 first-year revenue spoken '705cr' vs ~70-75cr scale - confirm correct figure and EBITDA assumption", from_finding_id: ["FN-05"]}
  - {q: "Chairman (Dr. Ajit Gupta) absent across all 87 turns on a two-acquisition quarter - who owns capital-allocation sign-off?", from_finding_id: ["FN-19"]}
  - {q: "'We will overachieve / can't see any challenge' vs occupancy drag - downside case if same-store occupancy softens; occupancy trough under the margin guide", from_finding_id: ["FN-14"]}
  - {q: "Declined a long-term case-mix target while committing 10-12% ARPOB for 2 years - reconcile; what high-end mix underpins ARPOB", from_finding_id: ["FN-15"]}
monitorables:
  - {item: "H1 FY27 cash-flow statement - first FCF-inflection read", implied_date: "2026-11 (Q2 FY27)", source_ref: "Reg 33 half-yearly / Notion monitorable 1"}
  - {item: "Rudrapur (V3) consolidation + first minority line", implied_date: "Q2 FY27", source_ref: "PRES-A1 / RES note 8 L266 / FN-04 turn 10"}
  - {item: "Palam Vihar/Park Platinum +100 beds commissioned", implied_date: "2026-11", source_ref: "RES note 4 L228 / turn 42"}
  - {item: "Mehar-Zirakpur acquisition completion (Rs 107 Cr, 150 beds)", implied_date: "2026-12-03", source_ref: "Board item 2 L62/584 / turn 2"}
  - {item: "Narela/Febris Delhi 200-bed commissioning", implied_date: "2026-12", source_ref: "PRES C5 L811 / turn 2"}
  - {item: "IPO object-variation postal-ballot notice & outcome", implied_date: "in due course", source_ref: "Board item 3 L68 / RES-A3-08 / FN-22"}
  - {item: "Rohtak IPO deployment - Rs 409.81mn remaining", implied_date: "FY27 ongoing", source_ref: "MON-A3-F6-02 L400-406"}
  - {item: "Medical-equipment IPO object catch-up - Rs 238.51mn unutilised", implied_date: "FY27", source_ref: "MON-A3-F6-01 L580-592"}
  - {item: "Exit FY27 at 4,740 beds", implied_date: "2027-03", source_ref: "PRES C11 / turns 2,42"}
  - {item: "Gorakhpur O&M 400 beds", implied_date: "2027-04", source_ref: "PRES C10 L810"}
  - {item: "Mohali expansion +150 (350->500)", implied_date: "2027-09", source_ref: "RES consol note 4 L490 / PRES C7"}
  - {item: "Ambala expansion +200 (250->450)", implied_date: "2027-10", source_ref: "PRES C8 L794 / turn 55"}
  - {item: "Rohtak greenfield 250 beds", implied_date: "2028-01", source_ref: "PRES C9 L791"}
  - {item: "Reach 5,740 beds [call restated 6,740 - reconcile]", implied_date: "2028-03", source_ref: "PRES C12 / turns 2,42 / FN-03"}
  - {item: "Rudrapur remaining 20% ownership acquired", implied_date: "2030-04-30", source_ref: "RES note 8 L266 / PRES C3 L533"}
  - {item: "FY26 promoter-remuneration disclosure (AR) - Strategic Premium / trigger #1", implied_date: "next AR/AGM", source_ref: "Notion monitorable 2 / trigger #1 / FN silence M6"}
  - {item: "Panchkula NABH accreditation (+4 hospitals FY27)", implied_date: "in process / FY27", source_ref: "deck L446 / PRES C15 / turn 3"}
  - {item: "FY27 GUIDANCE BASELINE Rs 2,080/530/360 Cr (24/25/32%) - score DELIVERED/PARTIAL/MISSED at Q2/Q3/Q4 (promise-vs-delivery tracker STARTS)", implied_date: "Q2/Q3/Q4 FY27", source_ref: "FN-01 turn 7 / Step 3 baseline B1"}
  - {item: "CGHS full-impact from Q2 - and whether it reaches EBITDA or only capex", implied_date: "Q2 FY27", source_ref: "FN-10 / FN-13 turns 3,21,26"}
  - {item: "Consolidated ETR trajectory - return to ~23-25% confirms Q1 PAT beat was one-off deferred-tax", implied_date: "Q2 FY27", source_ref: "FN-02 turn 7 vs line 435"}
  - {item: "Equity raise into ~75% promoter floor (~8% divest) by Dec-2028 - acquisition-linked issue/OFS and dilution size", implied_date: "by 2028-12 (event-driven)", source_ref: "FN-17 / FN-12 turn 51"}
  - {item: "ARPOB 10-12% p.a. + absolute ARPOB disclosure; payer mix to 70:30 in 12-18mo; ROCE +150-200bps in 12-18mo", implied_date: "12-18 months (score Q2+)", source_ref: "FN-06 / FN-07 / FN-09 / FN-23 turns 35,61,62"}
triggers_check:
  - {trigger: "Promoter remuneration >30% of PAT x2yr", reading: "ND - not discussed on call; FY25=27.5%, FY26 pending AR", fired: false}
  - {trigger: "Debtor days >175 x2Q", reading: "Call guides 125-130 (turn 4), below trigger; Q1 actual ND", fired: false}
  - {trigger: "EBITDA margin <22% x2Q", reading: "Call reaffirms 26.5-27% full FY27 (turns 8/9/30); Q1 op 26.51%", fired: false}
  - {trigger: "Major acquisition >Rs 1.0 Cr/bed", reading: "Call reconfirms Rudrapur ~54 lakh, Mehar ~70 lakh/bed (turn 42) - both <1.0 Cr/bed", fired: false}
flags: ["cash_conversion_INDETERMINATE_no_Q1_cashflow", "disclosure_quality_deferred_tax_reattributed_to_interest_FN-16_FN-20", "fully_funded_framing_masks_idle_IPO_648mn_and_object_variation_FN-22", "FY27_PAT_guide_360cr_consistent_only_on_sub-statutory_ETR_FN-01_FN-02", "unaudited_contribution_83.9pct_of_PAT_RES-A3-03", "PAT_35pct_flattered_to_~21pct_by_deferred_tax_benefit_RES-A3-06", "standalone_core_loss_making_rescued_by_other_income_RES-A3-02", "occupancy_-1224bps_YoY_bed_led_growth_absolute_ARPOB_withheld_PRES-A8_FN-23", "forward_dilution_~8pct_to_75pct_by_Dec2028_acquisition_linked_equity_raise_FN-17", "chairman_absent_all_87_turns_FN-19", "CGHS_uplift_routed_to_capex_not_EBITDA_FN-13", "four_internal_inconsistencies_5740v6740_capex_bed_date_beds_FN-18_garble_not_overweighted", "credibility_ratio_UNSCORED_first_concall_baseline_registered", "idle_IPO_Rs648mn_zero_yield_and_84pct_behind_equipment_capex_MON", "EPS_struck_on_total_PAT_incl_NCI_minor_overstatement", "presentation_forensics_per_bed_unit_slip_corrected_trigger4_not_fired"]
plain_language_brief_included: true
review_path: "/home/user/inflection-pipeline/runs/parkhosps-q1fy27/work/review_parkhosps_q1fy27.md"
```
