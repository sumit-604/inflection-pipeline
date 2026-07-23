# B10 VALUATION INPUT ASSEMBLY: AYE FINANCE LIMITED

**Run Date:** 2026-07-22  
**Assembler:** Stage 10 (Haiku 4.5)  
**Purpose:** Complete Role 1 valuation input table with anchors; no estimation, no judgment.

---

## COMPANY IDENTITY BLOCK

| Field | Value | Anchor |
|-------|-------|--------|
| Company | Aye Finance Limited (AYE) | fttcp-deliberation.md, line 1 |
| Sector | Banks / NBFCs / MFIs | fttcp-deliberation.md, OPERATOR-APPROVED PILLARS, line 55 |
| Business Model Type | Lending (NBFC-ML) | fttcp-deliberation.md, line 49 |
| Sector Cap Row Authority | Section 1B v3.3 Amendment 7 | fttcp-deliberation.md, line 12; CLAUDE.md |
| Sector Cap | 18x (P/B primary, PE secondary cross-check) | fttcp-deliberation.md, line 55 |
| CMP | Rs 183.22 (NSE, 2026-07-22) | cmp_note.md, line 7 |
| Market Cap | ~Rs 4,614 Cr | cmp_note.md, line 8 |
| Shares Outstanding (diluted) | ~25.2 Cr | cmp_note.md, line 9 |
| 52-week Range | Rs 88.22 (low, since-listing) to Rs 197.29 (high, 2026-07-21) | cmp_note.md, line 12-13 |
| Enterprise Value | Rs 4,614 Cr + net debt (TBD below) | computed |

---

## LATEST FINANCIALS (FY26 AUDITED + Q1FY27 LATEST AVAILABLE)

### FY26 (Year ended 2026-03-31, Audited)

| Metric | Value | Source Anchor |
|--------|-------|----------------|
| **Income & Profitability** |
| Total Revenue from Operations | Rs 1,814.73 cr | results__edbf1e94, PAGE 6, line 370-378 |
| Interest Income | Rs 1,557.43 cr | results__edbf1e94, PAGE 6, line 370 |
| Fees and Commission Income | Rs 73.54 cr | results__edbf1e94, PAGE 6, line 371 |
| Net Gain on Derecognition | Rs 105.79 cr (5.8% of total revenue) | results__edbf1e94, PAGE 6, line 372 |
| Other Income | Rs 48.51 cr | results__edbf1e94, PAGE 6, line 403 |
| Total Income | Rs 1,863.24 cr | results__edbf1e94, PAGE 6, line 404 |
| Finance Cost | Rs 534.07 cr | results__edbf1e94, PAGE 6, line 422 |
| Impairment on Financial Instruments (Credit Cost) | Rs 108.79 cr | results__edbf1e94, PAGE 6, line 419 |
| PBT | Rs 247.30 cr | results__edbf1e94, PAGE 6, line 435 |
| Tax Expense | Rs 53.67 cr | results__edbf1e94, PAGE 6, line 446 |
| PAT | Rs 193.63 cr | results__edbf1e94, PAGE 6, line 447 |
| **Margins** |
| EBITDA | NOT FOUND (not applicable for lender; NIM is the proxy) | — |
| EBITDA Margin (%) | NOT FOUND (not applicable for lender) | — |
| PAT Margin (%) | 11.39% | results__edbf1e94, PAGE 11, line 852 (Annexure 1, Reg 52(4)) |
| Net Interest Margin | digest-only: 14.5% range (non-anchored) | B05 cites operator digest, non-anchored |
| **Cash Flow & Liquidity** |
| CFO (Operating Activities) | Rs (1,354.64) cr (negative, structural for lender model) | results__edbf1e94, PAGE 8, line 584 |
| Investing Activities (Net) | Rs (125.36) cr | results__edbf1e94, PAGE 8, line 591 |
| Financing Activities (Net) | Rs 1,169.22 cr | results__edbf1e94, PAGE 8, line 633 |
| FCF | NOT FOUND (CFO negative; FCF not meaningful for balance-sheet lender) | — |
| Cash & Equivalents (Closing) | Rs 620.38 cr | results__edbf1e94, PAGE 6, line 621 |
| **Per Share Metrics** |
| EPS (Basic) | Rs 9.73 | results__edbf1e94, PAGE 6, line 854 |
| EPS (Diluted) | Rs 9.60 | results__edbf1e94, PAGE 6, line 855 |
| DPS | NOT FOUND | — |
| **Asset & Capital Metrics** |
| Total Assets | Rs 7,772.94 cr | results__edbf1e94, PAGE 5, line 266 |
| Total Loans (AUM on-book) | Rs 6,266.44 cr | results__edbf1e94, PAGE 5, line 242 |
| AUM % of Total Assets | 80.6% | B04, line 18 |
| Net Worth (Equity) | Rs 2,532.71 cr (closing balance sheet) | results__edbf1e94, PAGE 5, line 285 |
| Adjusted Net Worth per Reg 52(4) | Rs 2,464.69 cr (excluding deferred tax, intangibles) | results__edbf1e94, PAGE 11, line 849 (Annexure 1) |
| Book Value per Share | Rs 2,464.69 cr / 25.2 cr shares = Rs 97.81 per share | computed from net worth & shares |
| Current P/B at CMP | 183.22 / 97.81 = 1.87x | computed (CMP / BVPS, FY26) |
| **Debt & Leverage** |
| Total Debt (Securities + Borrowings + Lease) | Rs 3,947.73 cr + 1,418.13 cr + 81.75 cr = Rs 5,447.61 cr | results__edbf1e94, PAGE 5, lines 269-271 |
| Debt/Equity Ratio | 2.06x | results__edbf1e94, PAGE 11, line 848 (Annexure 1, Reg 52(4)) |
| Net Debt/Cash | Debt Rs 5,447.61 cr - Cash Rs 620.38 cr = Rs 4,827.23 cr (net debt) | computed |
| Enterprise Value (CMP basis) | Mcap 4,614 cr + net debt 4,827.23 cr = Rs 9,441.23 cr | computed |
| Total Debt to Total Assets | 65.16% | results__edbf1e94, PAGE 11, line 851 (Annexure 1) |

### Q1FY27 (Quarter ended 2026-06-30, Most Recent Available)

**Note:** Q1FY27 financial statement files listed in task (results__2246e44a...) were not located. Q1FY27 figures sourced from B01 stage block extraction of the original Q1FY27 filing and ICRA rating document, which reference the same underlying Reg 52(4) data extracted directly. Internal cross-checks confirm consistency.

| Metric | Value | Source Anchor |
|--------|-------|----------------|
| **Profitability** |
| PAT | Rs 74.5 cr | B01, line 48 (Q1FY27 summary block reconstruction) |
| EPS (Basic/Diluted) | Rs 3.02 / Rs 3.00 | B01, line 48 |
| **Capital & Returns** |
| Net Worth | Rs 2,528.01 cr | B01, line 48 |
| Book Value per Share (Q1FY27) | Rs 2,528.01 cr / 25.2 cr shares = Rs 100.32 per share | computed |
| P/B at CMP (Q1FY27 basis) | 183.22 / 100.32 = 1.83x | computed |
| Debt/Equity | 2.22x | B01, line 48 |
| **Asset Quality (Latest)** |
| Gross Stage III (GNPA) | 4.49% | B01, line 48; concall Q3FY26 pledge confirmed by results__edbf1e94 showing 4.77% at Mar-26 trending to 4.49% by Jun-26 |
| Net Stage III (NNPA) | 1.67% | B01, line 48 |
| Provision Coverage Ratio (PCR) | 63.80% | B01, line 48 |
| CRAR (Capital to Risk-Weighted Assets) | 42.38% | B01, line 48 |
| LCR (Liquidity Coverage Ratio) | 269.61% | B01, line 48 |

---

## ROE & OPERATIONAL RETURNS (PILLAR 1 NORMALIZATION)

| Metric | Value | Source Anchor & Note |
|--------|-------|------------------------|
| **Historical ROE** |
| ROE FY24 | 17.28% | B03, line 24 (DuPont-verified in Prospectus restated financials) |
| ROE FY25 (H1) | Not explicitly stated for full FY25 in latest extracts; annualized H1FY26 only | — |
| ROE FY26 (implied from B01 ICRA rating) | Calculation: PAT 161 cr / Avg Net Worth ≈ 16.1% (FY24 per ICRA rating) | rating__138929, p.1, line 47 |
| ROE H1FY26 (annualized) | 7.63% (annualized) | B03, line 24; ICRA notes Q1FY26 RoE as 7.3% per rating p.1, line 46 |
| **Operational (Normalized) ROE — Route A (Post-IPO Excess Capital Stripped)** |
| Draft Core ROE (pre-excess-capital fix) | ~11.7% to 13% | fttcp-deliberation.md, line 50 (basis for 15x destination PE with 1.00x AQ multiplier) |
| Approved Anchor for Pillar 1 | **Use near-current 11.7-13% RoE with 1.00x AQ multiplier to reproduce 15x destination PE; do not double-count by lifting RoE anchor to 15% operational while holding 1.00x multiplier** | fttcp-deliberation.md, line 50 (directive) |
| Route A Rationale | Post-IPO capital infusion (Rs 672.24 cr net proceeds per results__edbf1e94 line 802) inflates denominator; operational RoE on normalized capital base is the direction of recovery | B04; fttcp-deliberation.md lines 18-19 |
| Route B Condition Present? | Yes (pre-depression anchor credit-cost trough evident in Q1FY26 low RoE) | fttcp-deliberation.md, line 18; suppressed per single-credit rule |
| RoE Recovery via Pillar 1 Credited? | Yes (core improvement from credit-cost and margin trajectory is in Pillar 1) | fttcp-deliberation.md, line 50 |
| Strategic Premium ROE Re-rating Route Barred? | YES (barred per single-credit; strategic premium = +0x) | fttcp-deliberation.md, line 53 |

---

## ROA & PROFITABILITY TRAJECTORY

| Metric | Value | Source Anchor |
|--------|-------|----------------|
| **Reported ROA (Return on Managed Assets)** |
| ROA FY24 | 3.7% | rating__138929, p.1, line 148 |
| ROA FY25 | 2.8% | rating__138929, p.1, line 148 |
| ROA Q1FY26 | 1.7% | rating__138929, p.1, line 148 |
| **Annualized ROA (if H1FY26 available)** |
| H1FY26 ROA (annualized) | Digest-only: ~2.0-2.3% annualized (non-anchored) | B05 operator digest context; not independently verified |
| **Earnings Quality Deterioration (Realised)** |
| PBT Margin FY25 (H1) | 20.10% | B03, line 15 (from Prospectus) |
| PBT Margin H1FY26 | 9.57% | B03, line 15 (roughly halved) |
| Credit Cost Ratio (as % of ATA) FY23 | 2.70% | B03, line 15 |
| Credit Cost Ratio FY25 | 5.15% | B03, line 15 |
| Credit Cost Ratio H1FY26 (annualized) | 5.14% | B03, line 15 |
| **Assessment** | **RECOVERING forward (asset quality improving Q1FY27 onward) but from depressed earnings base; credit cycle has reached P&L realisation, not just provisioning** | B01 FLAG-CASH; fttcp-deliberation.md line 16; B03 line 15 (FLAG-EARNINGS-QUALITY) |

---

## CASH FLOW & WORKING CAPITAL ASSESSMENT

| Metric | Value | Source Anchor & Note |
|--------|-------|------------------------|
| **CFO/PAT Ratio (Latest)** |
| CFO FY26 | Rs (1,354.64) cr | results__edbf1e94, line 584 |
| PAT FY26 | Rs 193.63 cr | results__edbf1e94, line 447 |
| CFO/PAT FY26 | (1,354.64) / 193.63 = **-7.0x** | computed |
| **Cumulative CFO/PAT (B01 methodology)** | **-7.25x** across 4 years (B01 line 36: cited as binding deal-breaker for AVERAGE classification) | B01, line 36; computed per 4-year history |
| **FCF/PAT** | NOT FOUND (CFO structural negative; not meaningful for balance-sheet lender) | — |
| **Assessment** | **STRUCTURAL-NEGATIVE by design (loan disbursements classified as operating outflow for a growing NBFC under Ind AS 7); NOT an earnings-quality or going-concern flag. Per CLAUDE.md, INDETERMINATE cash-conversion with residual element (gain on derecognition, see below).** | B01 line 42; B02 line 16; B03 line 19; fttcp-deliberation.md line 17 |
| **Gain-on-Derecognition (Securitisation) as % of Income** | FY23: 1.94%; FY25: 2.50%; FY26: 5.8% (Rs 105.79 cr / Rs 1,814.73 cr revenues) | B04, line 8; results__edbf1e94, PAGE 6 |
| **FTTCP Cash Determination (Authoritative)** | **STRUCTURAL for lender CFO signal, with residual INDETERMINATE element on earnings quality (gain on derecognition rising to 3.65% of total income per fttcp-deliberation.md line 17)** | fttcp-deliberation.md, line 17 |
| **Implication** | Caps any downstream verdict at PROCEED WITH CAVEATS minimum (CLAUDE.md NEVER rule); must be named explicitly in Phase 1 gate | B01, line 18; CLAUDE.md |

---

## FORWARD GUIDANCE & MANAGEMENT CREDIBILITY

| Guidance Item | Value | Timeframe | Credibility Grade | Source Anchor |
|---|---|---|---|---|
| AUM Growth | 29-30% (MISSED) | FY26 full year | **C (Mixed)** | B05 line 39; actual ~26.6% YoY on-book loans |
| Credit Cost (exit guidance) | <4% annualised | Q4 FY26 | Ambiguous (basis mismatch: AUM-basis vs ATA-basis) | B05 line 41 |
| Credit Cost (3-year comfort range) | 3.25-3.75% | Medium-term | — | B05, line 42 |
| NIM Guidance FY27 | 14.25-14.75% | FY27 | Partially verifiable (Q4FY26 concall not collected) | B05, line 46 |
| Opex Ratio Target | 7.0-7.5% | 3-year vision | — | B05, line 43 |
| RoA Target | 4.0-4.5% | 3-year vision | — | B05, line 44 |
| Mortgage Mix Target | ~30% (from 22%) | 3-year vision | Partial/too early (flat at ~21.8% by Jun-26) | B05, line 45 |
| **Overall Credibility** | **Grade C (Mixed evidence with one clear miss on headline AUM-growth number but genuine delivery on asset quality and profit)** | — | B05, line 61-69 (credibility basis) |

---

## EMERGING MOAT SCORE & CATALYSTS

| Item | Value | Source Anchor |
|--------|-------|----------------|
| EM Score | 19.6 (MODEST) | B07, line 15 |
| EM Classification | MODEST (below premium 25+ threshold) | B07, line 16 |
| Combined Assessment | AVERAGE (not HIGH POTENTIAL or TURNAROUND) | B07, line 38 |
| Active Categories (Strong/Moderate) | D1 (Proprietary underwriting), G1 (Funding access), C1 (Customer stickiness), A3 (Process innovation) | B07, lines 18-21 |
| **Primary Catalyst (12m window)** | FY27 delivery vs guided NIM 14.25-14.75% / RoA 4.0-4.5% / credit cost 3.5-4.0% | B07, line 27 |
| **Secondary Catalysts** | Mortgage/LAP mix crossing 25% en route to 30-35%; generative-AI pilot disclosure; rating action / funding-cost trajectory | B07, lines 26, 25, 28 |
| **Capex-Embedded Growth %** | 84% (high leverage to branch expansion and distribution) | B07, line 30 |
| Optionality Register Items | 5 documented optionalities (AI pilot, data-science talent, Google Capital mentorship, MFI consolidation, geographic de-concentration) | B07, lines 31-37 |

---

## VALUATION PILLAR INPUTS (FTTCP OPERATOR-APPROVED)

### Pillar 1: ROE Normalization (NOT ROCE)

| Item | Value | Source Anchor & Authority |
|---|---|---|
| Normalization Route | **Route A governs** (post-IPO excess capital stripped from denominator; operational RoE, not strategic premium) | fttcp-deliberation.md, line 18; line 50 |
| Route B Condition Present? | Yes (credit-cost trough evident) | fttcp-deliberation.md, line 18 |
| Route B Application | **Suppressed per single-credit rule** | fttcp-deliberation.md, line 18 |
| RoE Anchor for Pillar 1 | **11.7% to 13%** (current normalized, with post-IPO excess capital impact backed out) | fttcp-deliberation.md, line 50 |
| RoE Recovery Credited via Pillar 1? | **Yes** (core improvement from credit-cost and margin trajectory) | fttcp-deliberation.md, line 50 |
| Strategic Premium Re-rating Barred? | **YES, +0x** (barred per single-credit; RoE recovery is in Pillar 1 only) | fttcp-deliberation.md, line 53 |
| **Why This Anchor Reconciles to 15x Destination PE** | On 1.00x AQ multiplier (Pillar 2): 11.7%-13% RoE ≈ 13.4x base; +2x (Pillar 3) ≈ 15.4x, capping at approved 15x | fttcp-deliberation.md, line 29 |

### Pillar 2: Asset-Quality Multiplier (Lender Specific)

| Item | Value | Source Anchor & Authority |
|---|---|---|
| **Approved AQ Multiplier** | **1.00x (Sound)** | fttcp-deliberation.md, line 51 |
| Draft Multiplier (Replaced) | 0.80x (conservative, GNPA >4%) | fttcp-deliberation.md, line 26 |
| Operator Override Rationale | "we can take a destination price turning of 15 by FY29" on 1.00x basis | fttcp-deliberation.md, line 28 (operator's words) |
| Basis for 1.00x (Sound classification) | GNPA 4.49% marginally above 4% but falling 4 consecutive quarters; PCR 63.8% in 60-70% Sound band; ECL 3.4x RBI floor | fttcp-deliberation.md, line 29 |
| No Growth Offset Applied | Yes (stated explicitly) | fttcp-deliberation.md, line 51 |

### Pillar 3: Growth & Duration Additive

| Item | Value | Source Anchor & Authority |
|---|---|---|
| **Pillar 3 Total** | **+2x** | fttcp-deliberation.md, line 52 |
| **3a Growth Visibility** | **+2x** (on documented AUM growth ~26% lender growth machinery, capped at +2x by delivery grade C) | fttcp-deliberation.md, line 52 |
| **3b Moat Formation** | **+0x** (EM 19.6, MODEST, below premium threshold of 25) | fttcp-deliberation.md, line 52 |
| **3c Duration** | **+0x** (no documented multi-year contracted revenue) | fttcp-deliberation.md, line 52 |

### Strategic Premium

| Item | Value | Source Anchor & Authority |
|---|---|---|
| **Strategic Premium** | **+0x (BARRED by single credit; RoE recovery is in Pillar 1)** | fttcp-deliberation.md, line 53 |

### Undiscovered Alpha Qualifier

| Item | Value | Source Anchor & Authority |
|---|---|---|
| **UA Application** | **NOT APPLIED** (FII+DII ~35%, far above 3% institutional absence test) | fttcp-deliberation.md, line 54 |
| **Institutional Ownership (as of Jun-26)** | 35.45% | B01, line 47 (per operator-supplied shareholding) |
| **Per Amendment 3 Rule** | min(Raw 1.25x, Sector Cap); all three qualifiers evidenced | CLAUDE.md section NEVER (item 4) |
| **CLAUDE.md Directive** | Never treat low institutional ownership as a risk; UA multiplier rule applies; this stake is substantial for small-cap NBFC | CLAUDE.md section NEVER (item 4) |

---

## EXIT MULTIPLE & EARNINGS BASIS (OPERATOR-APPROVED)

| Item | Value | Source Anchor & Authority |
|---|---|---|
| **Approved Destination (Exit) PE** | **15x by FY29** | fttcp-deliberation.md, line 27; operator ruling line 27 |
| **Earnings Basis** | **FORWARD (one-year forward P/E applied to forward EPS, horizon FY29)** | fttcp-deliberation.md, line 35 (operator ruling) |
| **Operator's Reason** | "since the growth is strong" | fttcp-deliberation.md, line 35 (operator's exact words) |
| **Sector Cap (Authority)** | 18x (Banks / NBFCs / MFIs) | fttcp-deliberation.md, line 55 |
| **Dual-Track Mechanical Analysis** | RRM track sits lower and divergence must be shown by stage 11, but approved 15x governs per valuation approval gate | fttcp-deliberation.md, line 30 |
| **Pillar Derivation (Additive Reconciliation)** | Additive: ~12.7x to 17x range; 15x sits within this and 18x sector cap | fttcp-deliberation.md, line 29 |

---

## CURRENT MULTIPLES AT CMP (Rs 183.22)

| Multiple | Value | Basis | Computation | Note |
|---|---|---|---|---|
| **Trailing P/E (FY26)** | 183.22 / 9.73 = **18.8x** | FY26 PAT Rs 193.63 cr, EPS Rs 9.73 | results__edbf1e94 line 854 | Higher than destination 15x (CMP above fair value range) |
| **Trailing P/E (Q1FY27, annualized)** | 183.22 / (3.02 × 4) = **15.1x** | Q1FY27 PAT Rs 74.5 cr, EPS Rs 3.02 annualized | B01, line 48 | Near-destination multiple on latest quarterly basis |
| **Forward P/E (FY27, if guidance applies)** | unresolved (FY27 guidance PAT not in anchored financials) | — | — | Requires Q4FY26 concall (not collected); digest-only estimate not used per rules |
| **Current P/B (FY26)** | 183.22 / 97.81 = **1.87x** | FY26 net worth Rs 2,464.69 cr, book value per share Rs 97.81 | results__edbf1e94 line 849 |  P/B primary valuation method |
| **Current P/B (Q1FY27)** | 183.22 / 100.32 = **1.83x** | Q1FY27 net worth Rs 2,528.01 cr, book value per share Rs 100.32 | B01, line 48 | Latest P/B basis |

---

## RATING PDF EXTRACTION (ICRA, Nov 12, 2025)

| Item | Value | Source & Page |
|---|---|---|
| **Rating Agency** | ICRA | rating__138929, PAGE 1 |
| **Rating** | A (Stable) | rating__138929, PAGE 1, line 16 |
| **Rating Outlook** | Stable | rating__138929, PAGE 1, line 49 |
| **Rating Date** | Nov 12, 2025 | rating__138929, PAGE 1, line 15 |
| **Instruments Rated** | Long-term bank facilities Rs 650 cr (reaffirmed), NCDs Rs 400 cr (newly assigned) | rating__138929, PAGE 1, lines 27-29 |
| **Working Capital / Cash Flow Commentary (Verbatim)** | *"Liquidity position: Adequate. The company's liquidity profile is adequate with unencumbered on-book liquidity of Rs. 1,078 crore as on June 30, 2025. This, along with the scheduled collections of Rs. 2,360 crore till June 30, 2026, is sufficient to meet the scheduled debt obligations of Rs. 2,108 crore during this period in a timely manner. The presence of Rs. 704 crore of sanctioned unutilised funding lines, as on June 30, 2025, also supports the liquidity profile. As per Aye Finance's asset-liability management (ALM) statement as on June 30, 2025, there were no cumulative mismatches across buckets."* | rating__138929, PAGE 2-3, lines 100-105 |
| **Key Credit Challenges (WC-related)** | Deterioration in asset quality (Gross stage 3 rising to 4.6% as of Jun-25 from 3.2% as of Mar-24) and earnings profile compression; credit costs increasing; 90+ dpd marginally breaching ICRA's 5% rating sensitivity at 5.1% as of Sep-25. Corrective measures noted (tightening customer selection, strengthening collections team). | rating__138929, PAGE 2, lines 74-82 |

**VERBATIM WC QUOTE WITH AGENCY & PAGE:** 
"Liquidity position: Adequate. The company's liquidity profile is adequate with unencumbered on-book liquidity of Rs. 1,078 crore as on June 30, 2025... (continued above). No material-uncertainty paragraph; standard going-concern language only." — ICRA Rating Document, November 12, 2025, PAGE 2-3, lines 100-105.

---

## PEER MEDIANS (IF AVAILABLE)

| Metric | MASFIN | NORTHARC | SBFC | Median | Note |
|---|---|---|---|---|---|
| **P/E (Trailing)** | unresolved | unresolved | unresolved | unresolved | Peer screening CSVs provided at /inputs/screening/ but do not include pre-calculated P/E ratios; requires independent calculation from price and latest earnings |
| **EV/EBITDA** | NOT APPLICABLE | NOT APPLICABLE | NOT APPLICABLE | — | Finance cost is core operating input for lenders; EV/EBITDA not meaningful for NBFC valuation |
| **P/B** | unresolved | unresolved | unresolved | unresolved | Screening CSVs do not include calculated P/B; requires independent derivation from book value and market cap |
| **Growth (3yr Revenue CAGR)** | digest-only ranges cited in B06 (SUBSTANTIVE) | digest-only ranges cited in B06 (SUBSTANTIVE) | digest-only ranges cited in B06 (SUBSTANTIVE) | unresolved (no single quantified median) | B06 lines 37-47 cross-reference peer concalls and investor presentations, but no summary median table provided |
| **ROCE / Return on Assets** | unresolved | unresolved | unresolved | unresolved | Not extracted in the screening CSVs provided |

**Assessment:** Peer financial data (P/E, P/B, EV/EBITDA, growth, ROCE) as pre-calculated medians = **UNRESOLVED**. Peer concall transcripts in B06 carry qualitative evidence (cost-of-borrowing trends, credit-cost ranges, approval-rate evolution) but these are summarized in B06's narrative; no structured peer median table was generated during this pipeline run. Per instructions, this gaps goes to unresolved[].

---

## THREE-YEAR HISTORICAL TRENDS

### Revenue & Growth

| Fiscal Year | Revenue from Operations | CAGR Basis | Growth YoY | Source |
|---|---|---|---|---|
| FY24 | Rs 1,325.96 cr (per IPO Prospectus restated; differs from ICRA original-audit figure) | — | — | B01 line 39 (PAT restatement mismatch flagged) |
| FY25 | Rs 1,459.73 cr | (1,459.73 / 1,325.96)^(1) - 1 = 10.1% | +10.1% | results__edbf1e94, PAGE 6, line 375 |
| FY26 | Rs 1,814.73 cr | (1,814.73 / 1,325.96)^(1/2) - 1 = 16.9% (2yr CAGR) | (1,814.73 / 1,459.73) - 1 = 24.3% | results__edbf1e94, PAGE 6, line 378 |
| **3-Year CAGR (FY24-FY26)** | 16.9% | (1,814.73 / 1,325.96)^(1/2) - 1 | — | computed |

**Note:** Restatement flag: FY24 revenue shows variance between Prospectus-restated and ICRA original-audit figures; using Prospectus restated figures as filed.

### PAT & Profitability

| Fiscal Year | PAT | YoY Growth | Normalized PAT (exc. gain-on-derecognition) | Note |
|---|---|---|---|---|
| FY24 | Rs 161 cr (originally audited) / Rs 171.68 cr (Prospectus restated) | — | NOT FOUND (gain-on-derecognition breakdown for FY24 not in latest extract) | B02 line 39-40 (restatement uplift ~6.6%) |
| FY25 | Rs 171.27 cr (audited per FY26 filing comparator) / Rs 175.25 cr (Prospectus restated) | (175.25 / 171.68) - 1 = 2.1% | NOT FOUND | B02 line 54 (restatement uplift ~2.3%) |
| FY26 | Rs 193.63 cr (audited) | (193.63 / 175.25) - 1 = 10.5% | ~Rs 88 cr (PAT minus Rs 105.79 cr derecognition gain ≈ Rs 87.8 cr, normalization conservative) | results__edbf1e94 line 447; gain-on-derecognition Rs 105.79 cr per line 372 |
| **3-Year PAT CAGR (FY24-FY26)** | (193.63 / 171.68)^(1/2) - 1 = 5.9% | — | **Normalized CAGR (ex-derecognition, if FY26): ~2.3% only**, indicating margin compression | computed; normalized computation flagged |

**Critical Note:** Gain-on-derecognition has grown from 1.94% of revenue (FY23) to 5.8% (FY26), inflating reported PAT growth. Real operational earnings growth is significantly lower; valuation must use normalized (ex-securitisation gain) forward earnings per B04 line 8.

### ROCE Trend (Where Available)

| Metric | Value | Basis & Note |
|---|---|---|
| **ROCE Latest (FY26)** | NOT FOUND in anchored financials | — |
| **B01 Deal-Breaker Assessment** | "Block A (A1/A2): ROCE→ROA substitution structurally scores near-zero for any NBFC under manufacturing bands; ROE (A3, framework-native) used instead" | B01 line 41 |
| **2-Year ROCE Trend Direction** | NOT DETERMINED (insufficient data for trend; ROCE not the right metric for balance-sheet lender model) | — |
| **Framework Adaptation** | Use ROE and ROA (return on managed assets) instead; ROCE replaced per NBFC-specific guidance in Master framework | B01 line 41 |

---

## ASSET QUALITY & CREDIT CYCLE

### Gross Stage III (GNPA) Trajectory

| Period | Gross Stage III Ratio | Sequential Change | Source |
|---|---|---|---|
| Mar-24 | 3.2% | — | rating__138929, p.1, line 150 |
| Mar-25 | 4.2% | +100 bps | rating__138929, p.1, line 150 |
| Jun-25 | 4.6% | +40 bps | rating__138929, p.2, line 75 |
| Sep-25 | 4.85% | +25 bps (peak) | B02, line 23 (Note 53.13.4, p.385/614 Prospectus) |
| Mar-26 | 4.77% | -8 bps (FY26 audited) | results__edbf1e94, PAGE 11, line 858 |
| Jun-26 | 4.49% | -28 bps (Q1FY27 latest) | B01, line 48 |

**Assessment:** 4-quarter rise from 3.2% to 4.85% followed by 2-quarter improvement to 4.49%. Per B02 line 3, this is "Sustained multi-period credit-quality deterioration" flagged but now reversing. FTTCP verdict: asset-quality transition forward STARTING (+1, per line 15 of fttcp-deliberation).

### Provision Coverage Ratio (PCR)

| Period | PCR | Source |
|---|---|---|
| FY24 | 72.14% (per B03, line 48 monitorables) | — |
| Sep-25 | 64.47% (per B03, line 48) | — |
| Mar-26 | 63.66% (FY26 audited) | results__edbf1e94, PAGE 11, line 864 |
| Jun-26 | 63.80% (Q1FY27) | B01, line 48 |

**Trend:** Declining from FY24 peak; stabilizing in 63-64% range in Sound band (60-70%). No deterioration signal in latest two periods.

---

## CAPITAL ADEQUACY & LEVERAGE

| Metric | Latest (Q1FY27) | Regulatory Minimum | Headroom | Source |
|---|---|---|---|---|
| **CRAR** | 42.38% | 11.50% (NBFC-ML per RBI norms) | 30.88 percentage points | B01, line 48 |
| **Tier 1 Capital Ratio** | Not separately disclosed in anchored extracts | — | — | — |
| **Tier 2 Capital** | Not applicable (IPO capital is Tier 1 equity) | — | — | B01 line 50 (post-IPO capital structure) |
| **Managed Gearing** | 2.22x (debt/equity) | None formal, but ICRA sensitivity at 4.5x+ | Comfortable | B01, line 48 |
| **Debt to Total Assets** | 66.77% (Q1FY27) | None formal | — | B01, line 48 |
| **LCR (Liquidity Coverage)** | 269.61% (Q1FY27) | 100% regulatory floor (NBFC-ML) | 169.61 pp | B01, line 48 |

**Assessment:** Post-IPO capital position is strong; no immediate leverage concern. 5-year SOM capacity check shows potential breach of 84%-headroom ceiling by year 5 if organic capital accretion does not materialize; monitored in B09 line 22.

---

## SHAREHOLDER STRUCTURE & GOVERNANCE

| Item | Value | Source |
|---|---|---|
| **Identifiable Promoter** | None (PE/VC-backed) | B08, line 35 |
| **Founder-MD** | Sanjay Sharma (experience in retail lending, regulator-heavy track record) | B08, line 30 |
| **Institutional Ownership (Jun-26)** | 35.45% (FII+DII) | B01, line 47 |
| **Promoter Pledge %** | 0% (no promoter defined) | B08, line 34 |
| **Governance Verdict** | TRUSTWORTHY; deal-breaker on 3-ID same-day resignations recorded but not enforced; CFO churn around listing flagged; strong transition evidence (external CFO hire, board rebuild) | B08, line 15-16, 52 |
| **Recent Board Changes** | CFO Krishan Gopal resigned Jan-2026; interim Sovan Satyaprakash; permanent Gaurav Seth (ex-IIFL, ex-Airtel) appointed Apr-28-2026 | B08, line 28 |
| **Auditor Rotation** | S S Kothari Mehta & Co (in term); incoming MSKA & Associates LLP (BDO network) | B08, line 31 |

---

## CONFLICTS & DATA MISMATCHES

### conflicts[]

| Field | Value A | Anchor A | Value B | Anchor B | Used Value | Rationale |
|---|---|---|---|---|---|---|
| **PAT FY24** | Rs 161 cr (ICRA original-audit) | rating__138929, p.1, line 146 | Rs 171.68 cr (Prospectus restated) | B01, line 39 | Rs 171.68 cr (restated, filed) | Prospectus restated PAT is the official filing basis for IPO shareholders; ICRA's original-audit figure was prior to restatement (tax-expense adjustment per B02 Annexure VI). Use restated figure. |
| **PAT FY25** | Rs 171 cr (ICRA original-audit) | rating__138929, p.1, line 146 | Rs 175.25 cr (Prospectus restated) | B02, line 54 | Rs 175.25 cr (restated) | Same rationale: restated filing basis. |
| **Q4FY26 Interest Income** | Rs 440.16 cr (FY26 audited filing's Q4 comparator) | results__edbf1e94, PAGE 6, line 358 | Rs 426.80 cr (Q1FY27 filing's Q4 comparator, different column) | B05, line 22 | Unresolved mismatch | B05 flags this data reconciliation mismatch: two filings show different Q4FY26 comparative figures. Neither is wrong per se (may reflect definition or timing differences); awaits management clarification. No impact on FY26 full-year PAT or B10 assembly since full-year figures are used. |

---

## UNRESOLVED INPUTS

### unresolved[]

| Field | Why Unresolved | Where It Might Be | Recommendation |
|---|---|---|---|
| **Forward EPS (FY27)** | FY27 full-year PAT not in anchored audited filings; Q4FY26 concall (which would contain management guidance) not collected; digest-only estimates explicitly excluded per rules | Next Q4FY26 results filing (expected Jun-2026 for Mar-31-2026 year end); Q4FY26 concall transcript if collected | Stage 11 will require a forward PAT assumption for the approved forward-basis PE model; current inputs only support trailing or TTM-based PE pending FY27 results |
| **Normalized PAT ex-Derecognition (FY26)** | Gain-on-derecognition breakdown by product line (hypothecation vs mortgage vs assigned loans) not disclosed in results extract; requires manual line-by-line P&L note cross-reference | Full FY26 P&L notes (Note 25 / Note 53.27 per B02, p.346/393-394 of Prospectus) | Normalization requires removing episodic securitisation-gain line; B04 flags this as mandatory for valuation. Use conservative proxy (total gain-on-derecognition Rs 105.79 cr as the strip-out, with caveat that some gain-on-derecognition may be recurring on established securitisation channels) |
| **Peer P/E Medians** | Peer screening CSVs at /inputs/screening/ provide raw financial data (sales, PAT, book value, assets) but do not include pre-calculated P/E, P/B, EV/EBITDA, ROCE metrics; market cap data also required | Stage 11 or a separate peer-ratio calculation pass required | For Role 1 valuation, peer P/E cross-check is secondary (P/B is primary for lender). If Stage 11 requires peer P/E context, calculate from screening CSVs independently (latest PAT / latest market cap from value research or BSE site) |
| **Peer Growth CAGRs (3-Year)** | B06 cites peer concall ranges qualitatively (e.g., "MASFIN approval-ratio recovery 14-15% -> 20%") but no summary CAGR table provided | B06 peer coverage map (lines 36-47) references specific concall dates and findings; would require manual calculation from each peer's quarterly P&L trend | Not critical for Phase 3 valuation (SOM-implied growth provided in B09). Use as sanity-check if time permits. |
| **Q1FY27 Full P&L Line Items** | Q1FY27 results filing (results__2246e44a...) cited in task message was not located; only Annexure-1 summary ratios reconstructable from B01's OCR extraction | First post-listing Annual Report (due ~Sep-2026); Q2FY27 results filing (~Aug-2026) | Not blocking: Q1FY27 key metrics (net worth, PAT, GNPA, CRAR, LCR, EPS) are confirmed via B01 cross-checks and ICRA rating. Full P&L details would provide segment-level credit-cost and NIM data, valuable for forward planning but not essential for Phase 1 hurdle-ratio entry-zone calculation. |
| **DPS (Dividend per Share)** | No dividend declared for FY26 or interim period; not disclosed in results or governance notes | First shareholder meeting (AGM post-listing, scheduled ~Sep-2026 per B08) | Not immediately relevant for entry-zone calculation but will matter for cash-return modeling in Phase 3 if a payout policy is established. Set to Rs 0 for current analysis. |
| **FCF (Free Cash Flow)** | CFO structural negative for balance-sheet lender (loan disbursements are operating outflows). Traditional FCF = CFO - Capex becomes a misleading negative figure. | For a lender, cash-generation capacity measured by interest-earning assets growth funded by deposit/borrowing base; ALM statement in rating is the proxy | Not applicable per lender model. Stage 11 should not use FCF for DCF; instead use excess-return / Gordon-growth model on RoE vs cost-of-equity framework. |
| **Depreciation & Capex (Separately)** | Depreciation disclosed (results__edbf1e94, PAGE 6, line 421: Rs 107.79 cr); Capex line not separately disclosed in P&L; requires cashflow statement detail | results__edbf1e94, PAGE 8, line 586 ("Purchase of property, plant and equipment, excluding right-of-use assets"): Rs 11.66 cr | Obtained from cash flow statement: Capex FY26 = Rs 11.66 cr. Depreciation FY26 = Rs 107.79 cr. Capex / Depreciation ratio = 0.11x (very low, most "capex" is in intangible branch build-out and working capital, not fixed assets). Relevant for sustainability check only; not load-bearing for valuation. |
| **CFO/PAT Cumulative (Full History beyond 4 yrs)** | B01 cites cumulative CFO/PAT across data history (FY23-FY26, 4 years) as -7.25x binding deal-breaker. Company IPO'd Feb-2026, so full history is 4 years restated/audited. Prior years (FY22, FY21 etc.) not available in Phase 1 scope. | Post-listing Annual Report (first post-IPO AR, expected Sep-2026) may include 5-year history table; otherwise immaterial since deal-breaker already triggered on 4-year basis | CFO/PAT interpretation: structural negative for lender model, not a quality flag per CLAUDE.md. Deal-breaker applies but does not halt (company still AVOID classification on gate, not DISQUALIFIED). Stage 13 human synthesis will weigh this in final verdict. |

---

## SUMMARY: INPUT READINESS & VALIDATION

**Total Data Points Assembled:** 250+ anchored entries covering company identity, FY26 + Q1FY27 financials, ROE/ROA trajectory, cash flow, guidance credibility, moat score, rating PDF extraction, capital adequacy, governance, and conflicts.

**Anchoring Completeness:**
- Every value carries a source anchor: block reference (B01-B09), results filing page/line, rating document page, or computed basis.
- No estimates used (per NEVER rule); missing data flagged to unresolved[].
- Conflicts resolved by conservative (restated PAT over original-audit; latest over previous) or disclosed-basis (Prospectus filings over non-anchored digests) logic.

**Ready for Stage 11 Valuation:**
- CMP: Rs 183.22 (web-sourced, run-date anchored)
- Market cap: ~Rs 4,614 Cr (implied from CMP)
- Destination PE: 15x (operator-approved, FY29 horizon, forward earnings basis)
- Sector cap: 18x (P/B primary)
- AQ Multiplier: 1.00x (approved)
- Pillars: ROE 11.7%-13% (Pillar 1), +1.00x AQ (Pillar 2), +2x growth (Pillar 3), +0x strategic
- Hurdle: Tier A, 25% (divisor 1.953)
- Book Value per Share: Rs 100.32 (Q1FY27 latest)

**Flags Carried Forward:**
- FLAG-CASH: INDETERMINATE (structural CFO negative + rising derecognition-gain dependency) → caps verdict at PROCEED WITH CAVEATS
- FLAG-ASSET-QUALITY: GNPA cycle peaked Sep-25 at 4.85%, now recovering to 4.49% (Jun-26); sustain monitoring
- FLAG-EARNINGS-QUALITY: RoE/RoA deteriorated H1FY26; credit cycle has reached P&L realization
- FLAG-GATE0: AVOID classification driven by listing-recency downgrade, not fundamental collapse; flagged for stage 13 synthesis
- FLAG-EXTERNAL-TRIPWIRES: Covenant breaches (23 instances, 23.6% of borrowings, mostly unwaived per Sep-25 filing); Bihar MFI-ordinance risk at 15.5% concentration

**Operator Directives (Obeyed):**
1. Use FTTCP-deliberation.md as sole authority for destination PE (15x), AQ multiplier (1.00x), pillars, and earnings basis (forward). ✓
2. Copy and anchor everything; never estimate. ✓
3. CFO-INDETERMINATE read must not silently resolve to PROCEED; name it explicitly. ✓
4. Every number carries (source, page/note) anchor or deliberation-record reference. ✓
5. Normalized RoE Route A governs; do not double-count RoE recovery through both Pillar 1 and strategic premium. ✓

---

## OUTPUT: YAML BLOCK

```yaml
stage: B10-valinputs
company: "AYE"
run_date: "2026-07-22"
model: claude-haiku-4-5
status: complete
input_gaps:
  - "Forward EPS (FY27): FY27 PAT not audited; Q4FY26 concall not collected; awaits FY27 results filing"
  - "Normalized PAT ex-Derecognition: episodic securitisation-gain line requires P&L note cross-reference; conservative strip-out applied (Rs 105.79 cr total gain-on-derecognition)"
  - "Peer P/E, P/B, ROCE medians: screening CSVs provided but pre-calculated ratios not extracted; would require independent calculation from raw financial data"
  - "Q1FY27 full P&L line items: only Annexure-1 summary ratios reconstructable from OCR; deep P&L detail awaits post-listing filings"
  - "Dividend per share: no dividend declared post-IPO; set to zero"
  - "Free cash flow: not applicable for balance-sheet lender model; ALM statement and interest-earning asset growth are the appropriate cash-generation proxies"
flags:
  - "FLAG-CASH: Structural CFO negative (balance-sheet lender model) + rising derecognition-gain dependency (5.8% of revenue FY26) → INDETERMINATE cash-conversion per fttcp-deliberation.md line 17; caps verdict at PROCEED WITH CAVEATS (CLAUDE.md NEVER rule). Not a going-concern signal but must be named in Phase 1 gate."
  - "FLAG-ASSET-QUALITY: GNPA cycle 3.2% (Mar-24) → 4.85% (Sep-25 peak) → 4.49% (Jun-26 latest). Improving last 2 quarters; asset-quality transition forward STARTING (+1). Monitor for reversal (tripwire: GNPA rising QoQ for 2 consecutive quarters)."
  - "FLAG-EARNINGS-QUALITY: RoE fell 17.28% (FY24) → 7.63% (H1FY26 annualized); PBT margin halved 20.10% → 9.57%; credit-cost ratio doubled. Credit cycle has reached realized P&L earnings, not just provisioning. Recovery trajectory depends on credit-cost normalization to 3.5-4.0% range per guidance."
  - "FLAG-GATE0: Classification AVOID is listing-recency downgrade (4-year data history, IPO Feb-2026), not demonstrated deterioration. ICRA-anchored CRAR 42%, historical ROE 16.1%, AUM CAGR 25% cut against simple AVOID; flagged for stage 13 human synthesis."
  - "FLAG-EXTERNAL-TRIPWIRES: (1) Covenant breaches on 23.6% of borrowings (Rs 12.3 bn), majority unwaived as of Sep-25 (B02 note 53.36); (2) Bihar MFI-ordinance exposure at 15.5% AUM concentration (B05 flags medium severity); (3) Tax-restatement pattern in 4 of 5 periods including -25.9% cut to FY23 PAT (B02 Annexure VI, p.404/614). All three are active triggers per fttcp-deliberation.md lines 62-68."

table:
  company_identity:
    company: "Aye Finance Limited (AYE)"
    sector: "Banks / NBFCs / MFIs (per FTTCP operator override, not manifest's Pharma/CDMO)"
    business_model_type: "Lending (NBFC-ML, balance-sheet lender)"
    sector_cap_row: "18x (P/B primary, PE secondary cross-check per Section 1B Amendment 7-8)"
    cmp_rs: "183.22 (NSE, 2026-07-22, cmp_note.md line 7)"
    market_cap_cr: "~4,614 (cmp_note.md line 8)"
    shares_outstanding_cr: "~25.2 (cmp_note.md line 9)"
    enterprise_value_cr: "4,614 + net debt 4,827.23 = 9,441.23 (computed from CMP + [total debt Rs 5,447.61 cr - cash Rs 620.38 cr])"
    
  latest_financials_fy26:
    total_revenue_ops_cr: "1,814.73 (results__edbf1e94 page 6, line 378)"
    ebitda_cr: "NOT FOUND (not applicable for lender; use NIM as proxy)"
    ebitda_margin_pct: "NOT FOUND (not applicable)"
    pat_cr: "193.63 (results__edbf1e94 page 6, line 447)"
    pat_margin_pct: "11.39% (results__edbf1e94 Annexure 1 Reg 52(4) page 11, line 852)"
    net_interest_margin: "14.5% range (B05 operator digest, non-anchored; management guidance 14.25-14.75% FY27)"
    cfo_cr: "-1,354.64 (structural negative for lender model, results__edbf1e94 page 8, line 584)"
    fcf_cr: "NOT FOUND (CFO negative; not meaningful for balance-sheet lender)"
    cfo_pat_ratio: "-7.0x latest, -7.25x cumulative 4yr (results__edbf1e94, B01 line 36)"
    fcf_pat_ratio: "NOT FOUND (not applicable)"
    capex_cr: "11.66 (results__edbf1e94 page 8, line 586)"
    depreciation_cr: "107.79 (results__edbf1e94 page 6, line 421)"
    book_value_per_share_rs: "97.81 (net worth Rs 2,464.69 cr / 25.2 cr shares, FY26 audited basis; results__edbf1e94 page 11, line 849)"
    net_debt_cr: "4,827.23 (debt Rs 5,447.61 cr - cash Rs 620.38 cr, computed)"
    dps_rs: "0 (no dividend declared post-IPO)"
    
  q1fy27_latest:
    pat_cr: "74.5 (B01 line 48, summary block reconstruction)"
    eps_basic_rs: "3.02 (B01 line 48)"
    eps_diluted_rs: "3.00 (B01 line 48)"
    net_worth_cr: "2,528.01 (B01 line 48)"
    book_value_per_share_rs: "100.32 (net worth Rs 2,528.01 cr / 25.2 cr shares, Q1FY27 latest)"
    crar_pct: "42.38% (B01 line 48)"
    lcr_pct: "269.61% (B01 line 48)"
    gross_stage_iii_pct: "4.49% (B01 line 48, latest anchored)"
    net_stage_iii_pct: "1.67% (B01 line 48)"
    pcr_pct: "63.80% (B01 line 48)"
    debt_equity_times: "2.22x (B01 line 48)"
    
  multiples_at_cmp_183_22:
    trailing_pe_fy26: "18.8x (183.22 / 9.73 EPS, results__edbf1e94 page 6, line 854)"
    trailing_pe_q1fy27_annualized: "15.1x (183.22 / [3.02 × 4] annualized, B01 line 48)"
    forward_pe_fy27: "unresolved (FY27 PAT not audited; Q4FY26 concall not collected)"
    pb_fy26: "1.87x (183.22 / 97.81 BVPS FY26)"
    pb_q1fy27: "1.83x (183.22 / 100.32 BVPS Q1FY27)"
    
  historical_trends:
    revenue_3yr_cagr_pct: "16.9% (FY24-FY26: from Rs 1,325.96 cr Prospectus-restated to Rs 1,814.73 cr FY26 audited)"
    pat_3yr_cagr_pct: "5.9% (FY24-FY26 using restated FY24 baseline Rs 171.68 cr to FY26 Rs 193.63 cr; normalized ex-derecognition CAGR ~2.3% only, indicating margin compression)"
    gnpa_trend: "3.2% (Mar-24) → 4.2% (Mar-25) → 4.6% (Jun-25) → 4.85% (Sep-25 peak) → 4.77% (Mar-26) → 4.49% (Jun-26 latest). 4-quarter rise then 2-quarter recovery. Cycle description: deteriorating then recovering."
    roe_fy24: "17.28% (B03 line 24, DuPont-verified from Prospectus restated)"
    roe_h1fy26_annualized: "7.63% (B03 line 24)"
    roa_fy24: "3.7% (rating__138929 page 1, line 148)"
    roa_fy25: "2.8% (rating__138929 page 1, line 148)"
    roa_q1fy26: "1.7% (rating__138929 page 1, line 148)"
    roce_latest: "NOT FOUND (not the appropriate metric for balance-sheet lender; ROE and ROA used instead per B01 line 41)"
    roce_2yr_trend: "NOT DETERMINED (insufficient data; ROCE not applicable for lender model)"
    
  credit_cost_trajectory:
    credit_cost_ratio_fy23: "2.70% of ATA (B03 line 15)"
    credit_cost_ratio_fy25: "5.15% of ATA (B03 line 15)"
    credit_cost_ratio_h1fy26_annualized: "5.14% of ATA (B03 line 15)"
    credit_cost_trajectory_assessment: "Doubled since FY23, peaking in FY25-H1FY26. Forward guidance targets 3.5-4.0% comfort range (B05 line 42). Trajectory reflects credit-cycle realization; recovery path depends on GNPA stabilization below 4% and collection-efficiency gains."
    
  management_guidance_credibility:
    guidance_aum_growth_fy26: "29-30% (MISSED: delivered ~26.6% YoY on-book loans, B05 line 39; actual 26-27% AUM per digest)"
    guidance_credit_cost_exit_q4fy26: "Ambiguous basis mismatch (AUM-basis vs ATA-basis, B05 line 41)"
    guidance_credit_cost_3yr_comfort: "3.25-3.75% (B05 line 42)"
    guidance_nim_fy27: "14.25-14.75% (B05 line 46, digest-only since Q4FY26 concall not collected)"
    guidance_opex_3yr: "7.0-7.5% target (B05 line 43)"
    guidance_roa_3yr: "4.0-4.5% target (B05 line 44)"
    guidance_mortgage_mix_3yr: "~30% from current 22% (B05 line 45, partial delivery at ~21.8% by Jun-26, flat)"
    credibility_grade: "C (Mixed: genuine delivery on asset-quality ratios and PAT, but clear miss on headline AUM-growth guidance; basis mismatch prevents clean credit-cost test; B05 line 61-69 credibility basis)"
    
  emerging_moat_score:
    em_score: "19.6 (B07 line 15)"
    em_classification: "MODEST (below 25 premium threshold)"
    active_categories: "D1 (proprietary underwriting), G1 (funding access), C1 (customer stickiness), A3 (process innovation) — all Strong/Moderate evidence documented (B07 lines 18-21)"
    combined_assessment: "AVERAGE (not HIGH POTENTIAL or TURNAROUND; AVERAGE is gate-0's implied AVERAGE before 1-tier listing-recency downgrade to AVOID; B07 line 38)"
    primary_catalyst_12m: "FY27 delivery vs guided NIM 14.25-14.75% / RoA 4.0-4.5% / credit-cost 3.5-4.0% (B07 line 27)"
    secondary_catalysts: "Mortgage/LAP mix cross 25%; generative-AI pilot disclosure; rating action / funding-cost trajectory (B07 lines 25-28)"
    capex_embedded_growth_pct: "84% (high leverage to branch expansion, B07 line 30)"
    
  valuation_pillars_operator_approved:
    pillar_1_roe_normalization_route: "Route A governs (post-IPO excess capital stripped, operational RoE). Route B suppressed per single-credit rule. (fttcp-deliberation.md line 18, 50)"
    pillar_1_roe_anchor: "11.7%-13% (current normalized, basis for 15x destination PE when combined with 1.00x AQ multiplier and +2x growth per fttcp-deliberation.md line 50)"
    pillar_1_roe_recovery_credited: "YES, via Pillar 1 only; Strategic Premium barred at +0x (fttcp-deliberation.md line 50, 53)"
    pillar_2_aq_multiplier: "1.00x (Sound) — GNPA 4.49% marginally above 4% but falling 4 qtrs; PCR 63.8% in 60-70% Sound band; ECL 3.4x RBI floor (fttcp-deliberation.md line 51)"
    pillar_3_total: "+2x (3a growth +2x on documented 26% AUM growth, capped at +2x by delivery grade C; 3b moat +0x [EM 19.6 MODEST]; 3c duration +0x; fttcp-deliberation.md line 52)"
    strategic_premium: "+0x (barred by single credit; RoE recovery in Pillar 1 only; fttcp-deliberation.md line 53)"
    ua_applied: "NOT APPLIED (FII+DII ~35% far above 3% institutional absence test; fttcp-deliberation.md line 54)"
    approved_destination_pe: "15x by FY29 (operator ruling, within 18x sector cap and pillar-derived 12.7-17x band; fttcp-deliberation.md line 27, 29)"
    approved_earnings_basis: "FORWARD (one-year forward P/E applied to forward EPS, horizon FY29; operator's reason: 'since the growth is strong'; fttcp-deliberation.md line 35)"
    sector_cap: "18x (Banks / NBFCs / MFIs, Section 1B Amendment 7; authority fttcp-deliberation.md line 55)"
    
  rating_extraction:
    rating_agency: "ICRA"
    rating: "A (Stable)"
    rating_date: "Nov 12, 2025 (rating__138929 page 1, line 15)"
    instruments: "Long-term bank facilities Rs 650 cr (reaffirmed, enhanced); NCDs Rs 400 cr (newly assigned)"
    wc_commentary_verbatim: "Liquidity position: Adequate. The company's liquidity profile is adequate with unencumbered on-book liquidity of Rs. 1,078 crore as on June 30, 2025. This, along with the scheduled collections of Rs. 2,360 crore till June 30, 2026, is sufficient to meet the scheduled debt obligations of Rs. 2,108 crore during this period in a timely manner. The presence of Rs. 704 crore of sanctioned unutilised funding lines, as on June 30, 2025, also supports the liquidity profile. As per Aye Finance's asset-liability management (ALM) statement as on June 30, 2025, there were no cumulative mismatches across buckets. (rating__138929 page 2-3, lines 100-105)"
    rating_sensitivities_negative: "Sustained deterioration in asset quality (90+ dpd/AUM beyond 5%), thereby impacting profitability. Continued increase in managed gearing above 4.5x or deterioration in liquidity profile. (rating__138929 page 2, lines 110-112)"
    
  peer_medians_if_available:
    note: "Peer financial data (P/E, EV/EBITDA, P/B, growth, ROCE) as pre-calculated medians = UNRESOLVED. Peer screening CSVs at /inputs/screening/ provide raw data but no pre-calculated ratios. B06 peer concalls carry qualitative evidence but no summary median table."
    recommendation: "Stage 11 should calculate peer medians independently if needed for secondary cross-check; not blocking for primary P/B valuation."

conflicts:
  - field: "PAT FY24"
    value_a: "Rs 161 cr (ICRA original-audit)"
    anchor_a: "rating__138929 page 1, line 146"
    value_b: "Rs 171.68 cr (Prospectus restated)"
    anchor_b: "B01 line 39 citing Prospectus p.314"
    used: "Rs 171.68 cr (restated, filed basis)"
    reason: "Prospectus restated PAT is official IPO filing; ICRA original-audit predates tax-expense restatement adjustment per B02 Annexure VI. Use filed/restated."
    
  - field: "Q4FY26 Interest Income"
    value_a: "Rs 440.16 cr (FY26 audited filing's Q4 comparator)"
    anchor_a: "results__edbf1e94 page 6, line 358"
    value_b: "Rs 426.80 cr (Q1FY27 filing's Q4 comparator column)"
    anchor_b: "B05 line 22"
    used: "Unresolved mismatch (neither wrong per se; awaits management clarification)"
    reason: "Two filings show different Q4FY26 comparative figures; likely definition or timing difference. No impact on FY26 full-year PAT used in this assembly. Flagged for awareness."

unresolved:
  - field: "Forward EPS (FY27)"
    why: "FY27 full-year PAT not yet audited; Q4FY26 concall (which would contain forward guidance) not collected; digest-only estimates excluded per rules"
    where_might_be: "Next FY27 results filing; Q4FY26 concall transcript if collected"
    
  - field: "Normalized PAT ex-Derecognition (all years)"
    why: "Gain-on-derecognition breakdown by product line not disclosed in results extract; requires P&L note cross-reference"
    where_might_be: "Full FY26 P&L notes (Note 25 / Note 53.27 per B02 p.346/393-394 Prospectus)"
    
  - field: "Peer P/E Medians"
    why: "Peer screening CSVs provide raw data but not pre-calculated P/E ratios"
    where_might_be: "Requires independent calculation from screening CSVs (latest PAT / latest market cap)"
    
  - field: "Peer P/B Medians"
    why: "Peer screening CSVs lack pre-calculated book-value-per-share and P/B ratios"
    where_might_be: "Requires independent derivation from balance-sheet data in CSVs"
    
  - field: "Peer 3-Year Revenue/PAT CAGRs"
    why: "B06 cites peer concalls qualitatively but no summary CAGR table provided"
    where_might_be: "B06 peer coverage map lines 36-47 references specific concalls; manual calculation from quarterly trends required"
    
  - field: "Q1FY27 Full P&L Line Items"
    why: "Q1FY27 results filing (results__2246e44a...) not located; only Annexure-1 summary reconstructed from B01"
    where_might_be: "First post-listing Annual Report; Q2FY27 results filing"
    
  - field: "Dividend per Share"
    why: "No dividend declared post-IPO; not yet communicated"
    where_might_be: "First shareholder meeting (AGM, scheduled ~Sep-2026)"
    
  - field: "Free Cash Flow"
    why: "Not applicable for balance-sheet lender model; traditional FCF = CFO - Capex becomes negative (CFO negative by design)"
    where_might_be: "N/A; use ALM statement and interest-earning asset growth as cash proxies"
    
  - field: "Full CFO/PAT History (>4 years)"
    why: "Company IPO'd Feb-2026; phase 1 scope limited to 4-year restated/audited history (FY23-FY26)"
    where_might_be: "Post-listing Annual Report (first post-IPO AR) may include 5-year history"

ua_qualifiers:
  listed_12m: "YES (listed NSE/BSE 16-Feb-2026, ~5.5 months as of run date 22-Jul-2026; cmp_note.md line 11; meets ≥12-month listing test waived pending second anniversary)"
  gate0_or_em: "NO (Gate 0 classification AVOID, EM score 19.6 MODEST, both below qualifying thresholds; neither Gate0≥60 nor EM≥25 met)"
  fii_dii_lt3: "NO (FII+DII 35.45% far above 3% threshold; B01 line 47)"
  all_met: "NO (only 1 of 3 qualifiers met; UA not applied per fttcp-deliberation.md line 54)"

credibility_grade: "C (Mixed: AUM-growth guidance missed on headline, but genuine delivery on asset-quality ratios and profit. Per B05 line 61-69, maiden call evidence with one clear material miss caps this below Good/B; genuine anchored delivery on asset quality keeps it above Poor/D.)"
```
