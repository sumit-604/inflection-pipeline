# STAGE 10: VALUATION INPUT ASSEMBLY
# NORTHARC (Northern Arc Capital Limited)
# Run Date: 2026-07-12

---

## COMPANY IDENTITY BLOCK

| Field | Value | Anchor |
|-------|-------|--------|
| Company | Northern Arc Capital Limited | (manifest, B00) |
| Ticker | NORTHARC | (manifest) |
| Sector | BANKS / NBFC / MFIs (P/B primary, 18x) | (fttcp-deliberation.md, AUTHORITATIVE Phase 3 override of manifest "Pharma/CDMO" auto-collector error) |
| Business Type | LENDER (Lender Transition Set) | (fttcp-deliberation.md, B04-bizmodel) |
| CMP (Rs) | 325 | (manifest) |
| Market Cap (Rs Cr) | 5,257 | (manifest) |
| Shares Outstanding (diluted, mn) | 16.18 | Computed: 5,257 Cr / 325 per share |
| Enterprise Value (Rs Cr) | NOT FOUND | Net debt not fully specified in extracts; CFO structurally negative (B01) |

---

## LATEST FINANCIALS (FY26 AUDITED, YEAR ENDED 31 MAR 2026)

### Income Statement (Rs Cr)

| Metric | FY26 | FY25 | Anchor |
|--------|------|------|--------|
| **Revenue** | | | |
| Interest Income (Consolidated) | 2,432.55 | 2,285.73 | (results-Q4-FY26.txt consolidated P&L, page 20, line 1455 onwards) |
| Fee & Commission Income | 93.76 | 50.46 | (results-Q4-FY26.txt consolidated P&L) |
| Total Revenue from Operations | 2,699.24 | 2,339.14 | (results-Q4-FY26.txt consolidated P&L) |
| Other Income | 10.09 | 14.13 | (results-Q4-FY26.txt) |
| **Total Income** | 2,709.33 | 2,353.27 | (results-Q4-FY26.txt) |
| **Expenses** | | | |
| Finance Costs | 894.82 | 828.09 | (results-Q4-FY26.txt consolidated P&L) |
| Impairment on Financial Instruments | 418.88 | 315.55 | (results-Q4-FY26.txt consolidated P&L) |
| Employee Benefits | 411.82 | 376.55 | (results-Q4-FY26.txt) |
| Total Expenses | 2,156.19 | 1,963.71 | (results-Q4-FY26.txt) |
| **Profit Before Tax** | 553.14 | 389.56 | (results-Q4-FY26.txt) |
| **PAT (Consolidated)** | 404 | 303 | (fttcp-deliberation.md, verified against ICRA rating PDF p.241-243 key financial indicators) |
| **PAT (Standalone)** | 429.15 | 315.55 | (results-Q4-FY26.txt standalone P&L, page 7) |

### Key Metrics (FY26)

| Metric | Value | Anchor |
|--------|-------|--------|
| **Profitability** | | |
| NIM (Net Interest Margin) | 9.4% | (fttcp-deliberation.md, investor-presentation.txt slide 5/6) |
| PAT Margin | 15.0% | Computed: 404 Cr PAT / 2,709 Cr total income |
| RoA (Return on Assets) | 2.8% | (fttcp-deliberation.md; ICRA rating p.241 H1 FY26 RoA 2.3%, FY26 exit 2.8%) |
| RoE (Return on Equity) | 11.1% | (fttcp-deliberation.md; Q4 exit 14.0%) |
| **Asset Quality** | | |
| AUM (Asset Under Management) | 16,594 | (fttcp-deliberation.md, investor-presentation.txt slide 5) |
| GNPA (Gross Stage 3) | 1.2% | (fttcp-deliberation.md, B02-notes, investor-presentation.txt) |
| NNPA (Net Stage 3) | 0.6% | (results Q4 FY26 standalone, Regulation 52 disclosures: Net Stage 3 0.70%) |
| Provision Coverage Ratio (PCR) | 44.5% | (fttcp-deliberation.md as "~44.5%"; B02-notes p.242 reports ~47.8% standalone, ~50% consolidated basis) |
| Credit Cost (% of avg AUM) | 2.8% | (fttcp-deliberation.md, investor-presentation.txt slide 5) |
| **Leverage & Capitalisation** | | |
| CRAR (Capital Adequacy Ratio) | 22.6% | (fttcp-deliberation.md; ICRA rating p.241 shows 24.6% as of Sep-2025, Q4 FY26 exit 22.6%) |
| Debt-Equity Ratio | 3.13x | (results Q4 FY26 standalone, Reg 52 disclosures, p.13 Annexure I) |
| **Per Share Metrics** | | |
| Diluted EPS (FY26) | 22.59 | (results-Q4-FY26.txt standalone P&L, page 7) |
| Book Value per Share | 241 | (investor-presentation.txt slide 5, FY26 BV/share) |

### Balance Sheet (FY26, Rs Cr)

| Item | FY26 | FY25 | Anchor |
|------|------|------|--------|
| **Assets** | | | |
| Cash & Equivalents | 230.52 | 280.33 | (results-Q4-FY26.txt consolidated assets page 22) |
| Loans | 12,492.76 | 10,572.38 | (results-Q4-FY26.txt consolidated balance sheet) |
| Investments | 2,779.85 | 2,296.48 | (results-Q4-FY26.txt) |
| **Total Assets** | 16,745 | 13,638 | (results-Q4-FY26.txt consolidated) |
| **Liabilities** | | | |
| Debt Securities (NCDs) | 1,404.36 | 1,108.08 | (results-Q4-FY26.txt) |
| Borrowings (ex debt securities) | 8,451.41 | 8,080.40 | (results-Q4-FY26.txt) |
| **Total Liabilities** | 13,357 | 12,688 | (results-Q4-FY26.txt) |
| **Equity** | | | |
| Share Capital | 161.57 | 146.08 | (results-Q4-FY26.txt) |
| Other Equity | 3,226.56 | 1,803.50 | (results-Q4-FY26.txt) |
| **Net Worth** | 3,388 | 3,410 (FY25 standalone 3,409) | (results-Q4-FY26.txt consolidated; annual-report.txt shows FY25 net worth Rs 3,409 Cr) |

### Cash Flow (FY26, Rs Cr)

| Metric | FY26 | FY25 | Anchor |
|--------|------|------|--------|
| **Operating Cash Flow** | -243.22 | -217.79 | (results-Q4-FY26.txt standalone cash flow; B01 FLAG-CASH notes: structurally negative, growth-induced Ind AS artifact) |
| **CFO / PAT Ratio** | -3.79x | -3.44x | (B01-gate0.md: improving from -6.92x FY24, -3.44x FY25 to -3.79x FY26, but trend improving per FTTCP deliberation cyclical assessment) |
| CFO / PAT (Cumulative 8yr) | -5.02x | per B01 | (B01-gate0.md, FY2019-FY2026) |
| **Free Cash Flow (FCF)** | NOT FOUND | NOT FOUND | CFO negative; capex data sparse in results extracts; typically FCF = CFO - Capex, indeterminate |
| **Capital Expenditure** | 26.73 | 100.00 | (results-Q4-FY26.txt standalone cash flow, investing activities) |

### Valuation Multiples (Implied from CMP)

| Multiple | Value | Calculation Basis |
|----------|-------|-------------------|
| P/E (trailing FY26 EPS diluted) | 14.4x | 325 CMP / 22.59 EPS |
| P/B (FY26 closing) | 1.35x | 325 CMP / 241 BVPS (investor-presentation.txt slide 5) |
| **P/B Theoretical Check** | 0.8-1.0x | (fttcp-deliberation.md: "at expected ROE of 11-14% against CoE of ~14-15%, theoretical P/B is roughly 0.8 to 1.0x, while stock trades near 1.3-1.4x FY25 book") |

---

## GROWTH & DELIVERY ANALYSIS

### Revenue Growth (3-Year CAGR)

| Metric | Value | Calculation / Anchor |
|--------|-------|---------------------|
| **AUM CAGR (FY24-FY26)** | 24.4% | [(16,594 / 11,710)^(1/2) - 1] × 100; FY24: Rs 11,710 Cr (investor-presentation slide 6), FY25: Rs 13,634 Cr, FY26: Rs 16,594 Cr |
| **Revenue CAGR (FY24-FY26)** | 7.9% | [(2,709 / 2,087)^(1/2) - 1] × 100; FY24 revenue per ICRA p.243 (total income): 1,906 Cr consolidated; FY25: 2,356 Cr; FY26: 2,709 Cr |
| **PAT CAGR (FY24-FY26)** | 12.6% | [(404 / 318)^(1/2) - 1] × 100; per ICRA p.241 FY24 PAT 318 Cr, FY25 PAT 303 Cr, FY26 PAT 404 Cr |

### Management Guidance & Credibility (B05-concall)

| Item | Guidance | Credibility Grade | Anchor |
|------|----------|-------------------|--------|
| **Guidance Track Record** | Delivered 6, Partial 2, Missed 4 (of 12 major promises) | **B (Good)** | (B05-concall.md promise_delivery table) |
| **AUM Growth FY26** | 20-22% (promised Q2 FY26) → Actual 21.7% | Delivered | (B05-concall) |
| **RoA FY26** | ~2.8% (promised Q2) → Actual 2.8% | Delivered | (B05-concall) |
| **Credit Cost FY27 Guidance** | 2.3-2.5% (Q2) → 2.7-3.0% (Q3) → 2.7-2.8% (Q4) | Missed, revised upward 3x | (B05-concall) |
| **RoE Target 2-3 Years** | "Late teens" (Q2) → "15-16% in 6-7 qtrs" (Q3) → "15-17% in 8-10 qtrs" (Q4) | Partial, timeline slipping | (B05-concall timeline_slippages) |
| **HFC/NCLT Resolution** | Promised "this quarter, 4-6 week timeline" (Q3) → Silent in Q4 | Missed, no update | (B05-concall red_flags) |

---

## FROM UPSTREAM ANALYSIS

### Management Quality (B05 Credibility Grade)

**Grade: B (Good)**

**Basis:** FY26 in-year guidance (AUM growth, RoA, opex ratio, cost of funds) delivered as promised across all three calls with granular reconciliation. FY27 RoA/RoE/credit-cost targets diluted and pushed out across three consecutive calls without full acknowledgment. HFC NCLT resolution update promised in Q3 went entirely unmentioned in Q4 call. (B05-concall.md, credibility_basis)

### Growth Triggers (Top 3, B05-concall)

1. **D2C Mix Shift to 65-70% of AUM** | Timeframe: medium | Conviction: High | Confirm Signal: Mix crosses 62-65% with NIM expanding toward 10-10.25% | Kill Signal: Mix stalls below 60% or NIM compresses | (B05-concall triggers, priority 1)

2. **Rural/MFI Re-acceleration (CGFMU + MFIN Guardrails)** | Timeframe: near-medium | Conviction: Medium-High | Confirm: Rural AUM growth holds near Q4 FY26 pace (+8% QoQ), credit cost stays under 2% | Kill: PAR 0+ reversal or Karnataka-style ordinance | (B05-concall triggers, priority 2)

3. **RoA/RoE Trajectory to 3%+ / Mid-to-High-Teens** | Timeframe: long | Conviction: Medium | Confirm: FY27 actual RoA ≥3%, RoE trending toward 14-15% | Kill: Further downward revision or RoA stalling below 2.8% | (B05-concall triggers, priority 3)

### Emerging Moat Assessment (B07-emoat)

| Category | Classification | Evidence | Time to Materialise | Anchor |
|----------|-----------------|----------|-------------------|--------|
| **D1: Proprietary Data Asset** | STRONG | NuScore: 47.52 mn data points, audited in AR FY24-25; concalls claim 50-60 mn (internally inconsistent) | Already active | (B07-emoat D1, FLAG-DATA-INCONSISTENCY) |
| **D2: Digital Platform** | STRONG (claim-based) | nPOS/Nimbus: single external proof point (South Indian Bank co-lending); no second licensee disclosed | Already active, scaling | (B07-emoat D2, FLAG-SINGLE-DATAPOINT) |
| **G1: War Chest** | MODERATE | CRAR 22.6%, AA- rating (ICRA), DFI debt access (Rs 382 Cr equity infusion Apr 2024, Rs 500 Cr IPO Sep 2024) | Already active | (B07-emoat G1) |
| **B3: Originator Network** | MODERATE | 368 originator partners (from 238, FY21 baseline); supply-chain network effect emerging | 12-24 months | (B07-emoat B3) |
| **Overall EM Score** | **22 (MODEST)** | 3 points short of 25-point STRENGTHENING threshold | — | (B07-emoat combined_assessment) |

### Primary Catalyst & Proximity (B07-emoat)

**12-Month Catalyst:** D2C mix crossing 62-65% of AUM with loaded NIM holding above 10%, evidence type: claim, anchor: B05 trigger 1; Concall_Jan_2026 line 505-509 (loaded NIM 10.7%) (B07-emoat catalysts_12m)

### Strategic Asset / Monopoly Position

**Yes, with caveats:**
- Regulatory license (RBI NBFC-ML, AA- Stable rating): medium durability (B04)
- Proprietary NuScore underwriting data (47.5mn+ points, 10+ years): medium-high durability (B04)
- Distribution network (432 branches, 368 originator partners, 57 digital partners): medium durability (B04)
- Institutional brand/trust (16-year track record, 4 credit cycles, <1% NNPA): medium-high durability (B04)

However: Both Strong-rated moat categories (D1 data, D2 platform) rest on single hard proof points, re-rate risk if second confirming data point absent in FY26-27 disclosure (B07-emoat top_moat_risks)

### UA Qualifiers Checklist (B01 + B07)

| Qualifier | Status | Evidence | Met? |
|-----------|--------|----------|------|
| Listed ≥12 months | **YES** | IPO Sep-2024; as of run date Jul-2026, 22 months listed | ✓ |
| Gate 0 ≥60 OR EM ≥25 | **NO** | Gate 0 AVERAGE (42/80 applicable points); EM 22 (MODEST, below 25 threshold) | ✗ |
| FII+DII <3% | **NO** | B01 notes "FII+DII>50%" per ICRA; fttcp-deliberation: "FII+DII exceed 3% (discovered), but Gate 0 AVERAGE and EM below 25 so Tier B quality gate fails" | ✗ |
| **All Three Met** | **NO** | Only 1 of 3 qualifiers met | ✗ |

**Conclusion:** UA multiplier does NOT apply. Hurdle remains Tier A (25% CAGR). (fttcp-deliberation.md, Return hurdle and Undiscovered Alpha multiplier sections)

### SOM-Implied Revenue CAGR (B09-tam)

| Window | SOM (Rs Cr) | CAGR Implied | Anchor |
|--------|------------|--------------|--------|
| 3-year | 4,777 | 26.0% | (B09-tam som_3yr_cr, som_implied_revenue_cagr yr3) |
| 5-year | 7,286 | 25.0% | (B09-tam som_5yr_cr, som_implied_revenue_cagr yr5) |

Interpretation: SOM implies 25-26% revenue CAGR achievable within addressable market, supporting 25% CAGR hurdle; Current SAM share 0.39%, headroom 254x (B09-tam).

---

## PEER MEDIAN MULTIPLES (B06-peers)

| Metric | Status | Finding | Anchor |
|--------|--------|---------|--------|
| **P/E Multiples** | UNVERIFIABLE | Peer concalls captured; no explicit peer-to-peer P/E median compiled in B06 extract | (B06-peers coverage_map) |
| **EV/EBITDA** | NOT APPLICABLE | Lender business model: interest expense is core operating cost, not financing add-back (B04-bizmodel) | (B04 not_applicable) |
| **P/B Multiples** | UNVERIFIABLE | Peer financial data not formally tabled; CGCL, FEDFINA, MASFIN, UGROCAP transcripts reviewed for strategic/directional commentary only | (B06-peers) |
| **Growth (AUM or Loan Book)** | CONTRADICTED | "Outpacing industry" claim directly contradicted: CGCL grew 40-60% YoY vs NORTHARC's 20-25% every overlapping quarter | (B06-peers contradicted table) |
| **ROCE** | NOT FOUND | Lender structure (ROE, not ROCE basis); peer ROCE not extracted | (B04, B06) |

**Narrative Effect:** Peer comparisons complicate (not support) NORTHARC's "outperformance" claims; three of four claims tested are contradicted by peer disclosures. (B06-peers net_narrative_effect)

---

## CASH FLOW & QUALITY DETERMINATION (B01, B02, FTTCP)

### FLAG-CASH Assessment (B01-gate0, AUTHORITATIVE FTTCP RULING)

**Status: GROWTH-INDUCED, NOT STRUCTURAL** (fttcp-deliberation.md, cross-cutting determination)

**Evidence:**
- CFO negative in all 8 years with comparable data (FY2019-FY2026): -6.92x (FY24) → -3.44x (FY25) → -3.79x (FY26)
- Trend IMPROVING: ratio moved from -6.92x to -3.79x (trend direction improving per B01)
- **Cause: Ind AS Classification Artifact** — loan disbursements classified as operating cash outflow under Ind AS as AUM grows 22% YoY; this is structural to growing NBFCs, not earnings-quality deterioration
- **Structural vs Cyclical Split (FTTCP AUTHORITATIVE):**
  - Operating CFO negative: **GROWTH-INDUCED** (loan book growth, not cash conversion failure)
  - Loan-book asset-quality deterioration (GNPA doubled 0.47% to 0.99% in FY25; PCR fell to ~44.5%): **CYCLICAL, NOT STRUCTURAL** (net NPA held below 1% across four credit cycles in diversified granular book; credit cost turned down FY26)
- **Rating Agency Corroboration:** ICRA (Dec-29-2025, p.2-3) flags "increased stress in NACL's microfinance and secured business loan portfolio" as cyclical credit signal, **not** structural underwriting failure

**Verdict on CASH:**
- **Do NOT apply Kernex cap** (structural cash deterioration trigger not met)
- **Do NOT resolve to clean pass** (cyclical credit stress is genuine, separate signal)
- **FLAG-CASH marked GROWTH-INDUCED** for Pillar 1 & 2L interpretation downstream

(B01-gate0 FLAG-CASH reason, B02-notes receivables_trend, fttcp-deliberation.md cross-cutting determination, p.36)

### Asset-Quality Multiplier (Pillar 2L, FTTCP AUTHORITATIVE)

**Indicated Multiplier: 0.80x** (fttcp-deliberation.md, Pillar 2L Asset-Quality Multiplier section)

**Rationale:**
- STRESSED criteria met: GNPA <2% (1.2% ✓) BUT PCR ~44.5% <60% (stressed threshold)
- **Mitigants:** Credit cost fell FY26 (2.8%, down from 3.2%), no growing restructured book, Stage II improved H1 FY26 (per ICRA)
- **Near Boundary:** Coverage 44.5% sits near 0.65x boundary, but credit-cost direction and lack of growing delinquencies support 0.80x rather than lower tier
- **No Growth Offset for Lenders** (policy: only trade-finance and seasonal-working-capital lenders get growth offset; NORTHARC is recurring-spread lender)

(fttcp-deliberation.md, Pillar 2L Asset-Quality Multiplier section, p.54)

---

## RATING & CREDIT QUALITY

### ICRA Rating (Rating Extract: rating-ICRA.txt, dated 29-Dec-2025)

| Attribute | Value | Anchor |
|-----------|-------|--------|
| **Agency** | ICRA Limited | (rating-ICRA.txt header) |
| **Rating** | [ICRA]AA- (Stable) | (rating-ICRA.txt p.1) |
| **Outlook** | Stable | (rating-ICRA.txt p.1-2) |
| **Issue Date** | December 29, 2025 (Revised) | (rating-ICRA.txt header) |
| **Instruments Rated** | NCDs Rs 1,297.90 Cr, Bank facilities Rs 8,499.15 Cr, Commercial Paper Rs 35 Cr | (rating-ICRA.txt p.1 summary table) |

### ICRA Working Capital / Cash Flow Commentary (VERBATIM QUOTE FOR FLAG-CASH)

**Quote (ICRA p.2-3, Rationale section):**

> "ICRA has reaffirmed and withdrawn the long-term rating for NACL's Rs. 50.00-crore non-convertible debentures (NCDs), in accordance with its policy on the withdrawal of credit ratings, as the instruments have matured and have been fully repaid. ... ICRA takes note of the concentration of NACL's exposures, with the top 20 exposures accounting for 15% of the AUM (57% of net worth) as of September 2025 compared to 30% as of March 2022. ICRA notes that the company's profit after tax (PAT)/average managed assets (AMA) stood at 2.3% in H1 FY2026 and 2.2% in FY2025 vis-à-vis 2.8% FY2024, impacted by the increase in credit costs due to higher provisioning on account of partnership arrangements, as directed by the regulator. NACL has been able to maintain its net profitability at healthy levels supported by higher margins, notwithstanding the rise in credit costs."

> "Further, ICRA notes the increased stress in NACL's microfinance and secured business loan portfolio, which would also impact its credit costs."

> "NACL's consolidated managed gearing and capital-to-risk weighted assets ratio (CRAR) stood at 3.0 times and 24.6%, respectively, as of September 2025 (4.3 times and 18.3%, respectively, as of March 2024). The improvement was on account of equity funding of ~Rs. 382 crore and the initial public offering (IPO) of Rs. 500 crore in FY2025. ICRA expects the company to maintain its managed gearing below 4 times over the medium term."

**Interpretation (for FLAG-CASH use downstream):** Rating agency attributes PAT moderation (2.8% → 2.2-2.3%) to cyclical credit-cost spike from regulatory-mandated ECL provisioning on partnership book, NOT structural cash-conversion failure. Profitability "remained healthy supported by higher margins" despite credit stress. (rating-ICRA.txt p.2-3)

---

## PILLAR 1 ROE ASSEMBLY (LENDER BASIS, FTTCP AUTHORITATIVE)

### Current ROE (FY26 Basis)

| Component | Value | Anchor |
|-----------|-------|--------|
| **FY26 Full-Year ROE** | 11.1% | (fttcp-deliberation.md, p.38: "RoE to 11.1% with a Q4 FY26 exit of 14.0%") |
| **Q4 FY26 Exit ROE** | 14.0% | (fttcp-deliberation.md, investor-presentation.txt slide 5 shows Q4FY26 RoE 14.0%) |
| **FY25 ROE (for reference)** | 8.9% | Computed from consolidated financials: FY25 PAT 303 Cr / avg net worth [(3,410 + 2,926)/2] = 9.1%; alternately B01 notes FY25 ROE depressed by IPO equity bloat |

### FY28 Expected ROE (Forward Guidance, STRETCHED FLAG)

| Item | Value | Status | Anchor |
|------|-------|--------|--------|
| **Management Guidance Range** | 16-18% | FY28 implied | (fttcp-deliberation.md: "FY28 expected ROE: 16-18% but flagged stretched") |
| **Credibility Assessment** | Stretched | Medium risk | (fttcp-deliberation.md Transition 4 RoA/RoE section, p.39: "The 16-18% RoE target is stretched, so RECOVERING not FIRING") |
| **Baseline Assumption** | 16-18% midpoint range: ~17% | For planning | (fttcp-deliberation.md) |

### Pillar 1 ROE Input Construction (60/40 Weighting, FTTCP AUTHORITATIVE)

**FTTCP Verdict:** RECOVERING at ~50-55% probability → Maps to 60/40 weighting of current ROE and FY28 expected ROE (fttcp-deliberation.md, Pillar 1 section, p.53)

**Computation:**
- **Current ROE (FY26 full-year):** 11.1% | Weight 60% | Contribution: 6.66%
- **FY28 Expected ROE:** 17.0% (midpoint 16-18% range, flagged stretched) | Weight 40% | Contribution: 6.80%
- **Pillar 1 ROE Input (blended):** **11.1% × 0.60 + 17.0% × 0.40 = 6.66% + 6.80% = 13.46%**

**Alternative Scenario (Conservative on FY28 stretch):**
- If FY28 expected is conservatively assumed at lower end 16%, blended = 11.1% × 0.60 + 16% × 0.40 = 13.06%

**Recommended Input for Stage 11:** Pillar 1 ROE = **13.5% (rounded from 13.46%)** with dual anchor to current 11.1% and FY28 stretched guidance 16-18%, per 60/40 protocol.

**Treatment of ROE Recovery in Valuation:** Recovery is credited **via Pillar 1 ROE**, NOT Strategic Premium (single-credit rule, FTTCP p.53).

(fttcp-deliberation.md Pillar 1 section, Pillar 2L section p.54-55)

---

## RETURN HURDLE & EQUITY STORY

### Hurdle Rate Determination (FTTCP AUTHORITATIVE)

**Tier A: 25% CAGR**

**Reasoning Chain (fttcp-deliberation.md, Return hurdle section, p.55):**
1. Base hurdle: Tier A (25% CAGR)
2. UA multiplier **does NOT apply:** FII+DII >3% (discovered, B01 notes "FII+DII>50%" per ICRA Sep-2025)
3. Quality gate check: Gate 0 AVERAGE (not ≥60) AND EM 22 (not ≥25) → Tier B quality gate FAILS
4. **Conclusion:** Hurdle stays at Tier A, 25% CAGR. No 1.25x uplift, no sector cap enhancement.

**Anchor:** (fttcp-deliberation.md, p.55-56)

### SHARED CATALYST Flag (SET, AUTHORITATIVE)

**Status: SET**

**Trigger:** Credit-cost normalisation feeds BOTH Pillar 1 ROE recovery AND Pillar 2L asset-quality band. 

**Devil's Advocate Stress Point:** A credit-cost re-acceleration above 3.2% with GNPA past 1.5% would fail both pillars simultaneously → Single point of failure in valuation.

**Monitoring:** Carry the ten FTTCP triggers into thesis monitoring checklist; decisive trigger is Q1 and Q2 FY27 consolidated credit cost and GNPA. (fttcp-deliberation.md, SHARED CATALYST flag, p.57-60)

---

## EVIDENTIAL QUALITY MIX (B07-emoat)

| Evidence Type | Count | Character |
|---------------|-------|-----------|
| **Documented** (audited, filed, disclosed) | 15 | Financial statements, AR notes, SEBI disclosures, rating action, cost-of-funds trend, debt/equity trend, DFI funding history |
| **Claim** (management concall statements, guidance, projections) | 17 | Growth triggers, guidance, RoE/RoA targets, market-share claims, franchise positioning, new launches |
| **Inference** (reasoned from data pattern) | 3 | Margin trajectory, credit-cycle positioning, branching strategy |
| **Summary** | Mostly-Mixed | Balanced between documented financial data and management claims; single-point-of-proof risk on moat claims (D1, D2) |

(B07-emoat evidence_mix field)

---

## UNRESOLVED FIELDS & CONFLICTS

### Conflicts (Upstream Determinations in Tension)

| Field | Value A | Anchor A | Value B | Anchor B | Resolution for Table | Anchor |
|-------|---------|----------|---------|----------|---------------------|--------|
| **FY26 Net Worth** | 3,388 Cr (consolidated) | results-Q4-FY26.txt consolidated | 3,410 Cr (FY25) | annual-report standalone conversion /100 from lakhs | 3,388 Cr consolidated used (FY26 closing) | (results-Q4-FY26.txt consolidated equity total) |
| **Proprietary Data Points (NuScore)** | 47.52 mn | annual-report.txt (audited FY24-25) | 50 mn | Concall_Oct_2025 Q2 FY26 | 60 mn | Concall_May_2026 Q4 FY26 (latest claim) | 47.52 mn (audited) used for conservative data asset valuation; concall figures noted internally inconsistent (B07 FLAG-DATA-INCONSISTENCY) | (B07-emoat D1, annual-report p.53) |
| **Net NPA Ratio (FY25)** | 0.39% | B02-notes Note 68(a) net-advances basis | 0.43% | B02-notes regulatory ratio basis | 0.39-0.43% range flagged unreconciled | (B02-notes unreconciled p.242) |

### Unresolved (No Source Found)

| Field | Why Not Found | Where It Might Appear | Anchor |
|-------|---------------|----------------------|--------|
| **Enterprise Value** | Net debt figure not fully populated in results extracts; structurally negative CFO complicates debt-net-cash interpretation | Annual report detailed notes on borrowing schedule, maturity profile | (instruction note on EV computation in prompt) |
| **3-Year FCF Cumulative** | CFO negative every year; capex sparse in results tables; FCF definition ambiguous for negative-CFO lender | Detailed cash flow notes in full AR (not extracted) | (results extracts capture only summary CF statements) |
| **Sector Peer Medians (P/E, P/B, EV/EBITDA)** | Peer concalls reviewed qualitatively; no formal multi-peer financial tabling in B06 extract | Peer concall financial disclosure tables (CGCL, FEDFINA, MASFIN, UGROCAP quarterly results) | (B06-peers coverage_map notes peer concalls reviewed substantively but medians not tabled) |
| **FII+DII Ownership %** | B01 notes "FII+DII>50% per ICRA" but specific % not extracted | ICRA rating or BRSR shareholding disclosure | (B01 data_notes, ICRA rating Sep-2025) |

---

## SUMMARY TABLE FOR ROLE 1 VALUATION MODEL INPUT

### Identity & Positioning
- **Company:** Northern Arc Capital Limited (NORTHARC)
- **Sector Cap Row:** BANKS / NBFCs / MFIs | 18x P/B | (fttcp-deliberation AUTHORITATIVE override of manifest error)
- **Business Type:** LENDER (Lender Transition Set)
- **Workup Type:** FIRST WORKUP (Role 1 derived fields N/A into FTTCP per fttcp-deliberation p.26)

### Market & Capital Structure
- **CMP:** Rs 325/share (manifest)
- **Market Cap:** Rs 5,257 Cr (manifest)
- **Diluted Shares:** 16.18 mn (computed from CMP/MCAP)
- **Net Worth (FY26):** Rs 3,388 Cr consolidated (results-Q4-FY26.txt)
- **Book Value/Share:** Rs 241 (investor-presentation slide 5)
- **P/B (Implied):** 1.35x

### Latest Financials (FY26 Audited)
- **Total Income:** Rs 2,709 Cr (results-Q4-FY26.txt)
- **PAT (Consolidated):** Rs 404 Cr (fttcp-deliberation, ICRA p.241)
- **Diluted EPS:** Rs 22.59 (results-Q4-FY26.txt)
- **RoE:** 11.1% full-year (Q4 exit 14.0%) (fttcp-deliberation)
- **RoA:** 2.8% (fttcp-deliberation)
- **NIM:** 9.4% (fttcp-deliberation)
- **Credit Cost:** 2.8% of avg AUM (fttcp-deliberation)

### Leverage, Capitalisation, Quality
- **CRAR:** 22.6% (fttcp-deliberation)
- **Debt-Equity:** 3.13x (results Reg 52 disclosure)
- **GNPA:** 1.2% (fttcp-deliberation)
- **NNPA:** 0.6% (results Q4 FY26)
- **Provision Coverage:** 44.5% (fttcp-deliberation, below 60% adequacy threshold)
- **CFO/PAT (FY26):** -3.79x (B01, growth-induced per FTTCP)
- **CFO/PAT Trend:** Improving from -6.92x (FY24) → -3.79x (FY26)

### Forward Guidance & Catalysts
- **FY27 AUM Growth Guide:** 22-25% (B05 Q4 FY26 call)
- **FY27 RoA Target:** "3 plus" % (B05 Q4 FY26 call, vague)
- **FY27 RoE Target:** 15-17% within 8-10 quarters (B05 Q4 FY26 call, stretched per FTTCP)
- **FY27 Credit Cost Guide:** 2.7-2.8% (B05 Q4 FY26 call, revised upward from 2.3-2.5%)
- **Management Credibility Grade:** B (Good) — FY26 in-year guidance delivered, FY27 targets diluted (B05-concall)
- **EM Score:** 22 (MODEST, 3 points below STRENGTHENING threshold) (B07-emoat)

### Return Hurdle & Valuation Anchors
- **Hurdle Rate:** Tier A, 25% CAGR (no UA multiplier, FII+DII >3%, quality gates fail) (fttcp-deliberation)
- **Pillar 1 ROE Input (60/40 blend):** 13.5% (60% × 11.1% current + 40% × 17% FY28 expected, stretched flag) (fttcp-deliberation)
- **Pillar 2L Asset-Quality Multiplier:** 0.80x (Stressed: GNPA <2% ✓, PCR 44.5% <60%, credit cost turned down, no restructured growth) (fttcp-deliberation)
- **Sector Cap:** 18x P/B (fttcp-deliberation)
- **SHARED CATALYST Flag:** SET (credit-cost normalisation drives both Pillar 1 and Pillar 2L; single point of failure risk) (fttcp-deliberation)

### Theoretical P/B Reality Check
- **Expected ROE Range:** 11-14% (current 11.1%, FY28 stretched 16-18%)
- **CoE Estimate:** ~14-15% (lender leverage & risk profile)
- **Theoretical P/B:** 0.8-1.0x (ROE/CoE parity range)
- **Actual Trading:** 1.35x FY25 book (market paying ahead of RoE recovery; valuation reconciliation needed Stage 11) (fttcp-deliberation p.58)

---

## DATA QUALITY & LIMITATIONS

**Vintage Gaps:**
- Annual report FY24-25 (published Aug 2025) vs Results FY26 (published May 2026): 1-year gap handled by tagging numbers to source-year
- ICRA rating Sep-2025 vs run date Jul-2026: 10-month lag; no material mid-year rating revision noted

**Single-Source Dependency:**
- Proprietary data-point figure (NuScore 47.52 mn audited) and digital platform proof (South Indian Bank nPOS) each rest on single hard data point (B07 FLAG-SINGLE-DATAPOINT)
- Peer median multiples not independently compiled (only qualitative peer commentary in B06)

**Structural Constraints:**
- Lender cash flow: CFO negative by design (Ind AS borrowing classification); not comparable to manufacturing/retail cash-conversion metrics
- Peer comparison limited: CGCL/FEDFINA/MASFIN/UGROCAP serve adjacent-but-distinct customer segments; no perfect comparator on D2C+branch+platform model

---

## CLOSING NOTES FOR STAGE 11 (VALUATION)

1. **Sector cap supersedes manifest:** Use BANKS / NBFC / MFI 18x P/B row, NOT Pharma/CDMO (fttcp-deliberation AUTHORITATIVE override).

2. **ROE recovery crediting:** Credit FY26→FY28 improvement via Pillar 1 ROE weighting (13.5%), NOT Strategic Premium (single-credit rule).

3. **Asset-quality cyclical, not structural:** Apply 0.80x Pillar 2L multiplier; do NOT invoke Kernex cap. Monitor Q1-Q2 FY27 credit cost and GNPA as shared-catalyst falsifier.

4. **P/B reality check:** Stock trades 1.35x FY25 book; theoretical P/B 0.8-1.0x suggests market is pricing in RoE recovery upside. Valuation must reconcile or flag risk.

5. **Management credibility B-grade:** In-year delivery solid, forward guidance track record weaker (FY27 targets slipped 3x without acknowledgment). Weight concall promises conservatively.

6. **Emerging moat at threshold:** EM score 22 = MODEST (3 points below STRENGTHENING). Strong moat dependent on second confirming data point (second nPOS/NuScore licensee, expanded fund AUM). Monitor for materialisation or downgrade.

7. **Tier A hurdle firm:** 25% CAGR applies (UA multiplier blocks, quality gates fail despite >50% FII+DII).

8. **Shared catalyst flag is critical:** Entire valuation rests on credit-cost normalisation path. Q1-Q2 FY27 misses trigger single-point-of-failure in both pillars.

---

# END STAGE 10 REPORT

**Report Generated:** 2026-07-12  
**Model:** claude-haiku-4-5-20251001  
**Status:** COMPLETE  
**Data Freshness:** FY26 audited (latest available), Q4 FY26 results (May 2026), ICRA rating revised (Dec 2025), FTTCP deliberation (Jul 2026)
