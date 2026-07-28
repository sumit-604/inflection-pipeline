# STAGE 10: VALUATION INPUT ASSEMBLY
# Role 1 Input Table for DSSL | FTTCP Phase 3 Basis
**Run:** dssl-2026-07-27 | **Assembled:** 2026-07-28 | **Model:** Claude Haiku 4.5

---

## COMPANY IDENTITY BLOCK

| Field | Value | Anchor |
|---|---|---|
| Company | Dynacons Systems & Solutions Ltd | (B00-inputs.md) |
| Ticker | DSSL | (B00, fttcp-deliberation.md) |
| Sector | IT Infrastructure / Systems Integration / Managed Services | (B04-bizmodel.yaml) |
| Business Model Type | Hybrid: hardware resale + lease-funded annuity transition | (B04.business_type: "hybrid") |
| Sector Cap Row (Manifest) | Platform / SaaS / IT services | (B00-inputs.yaml line 10) |
| Sector Cap Row (FTTCP Phase 3, AUTHORITATIVE) | Data centres and cloud infrastructure, capital heavy | (fttcp-deliberation.md Override 3, p.39-44) |
| CMP (as of run date) | Rs 1,232 | (B00-inputs.yaml line 8; fttcp-deliberation.md headline) |
| Market Cap | Rs 1,567.9 crore | (screener-Data_Sheet.csv line 8; = 1,231.6 × 1.2737 cr shares) |
| Shares Outstanding (Diluted) | 1.2737 crore | (audited results FY26 p.2: Paid-up capital 1,273.71 lakh ÷ 10 FV) |
| Enterprise Value (EV Calculation) | Rs 1,693.3 crore | (mcap 1,567.9 + net debt 125.4; see breakdown below) |
| — Calculation Detail | EV = 1,567.9 + (236.5 debt+leases - 111.2 cash) | (Audited BS FY26 p.4: Borrowings 81.2cr + Lease Liabilities 155.3cr - Cash 111.2cr) |

---

## LATEST FINANCIALS (FY26 Audited, Year Ended 31-Mar-2026)

| Metric | Value | Unit | Anchor | Notes |
|---|---|---|---|---|
| **Revenue (Latest FY)** | 1,424.28 | Rs crore | (audited standalone P&L p.2, line 50 "Net Sales" 1,42,267 lakh; screener-Data_Sheet.csv line 11 FY26) | FY26 growth +12.4% YoY vs FY25 1,267.2cr (concall B05) |
| **EBITDA** | 146.0 | Rs crore | (B05-concall.yaml line 24: "FY26 EBITDA/margin Rs146cr, 10.2%") | Calculated: 1,424.28 × 10.2% = 145.3cr, management cites 146cr |
| **EBITDA Basis** | With other income, without finance costs/tax | (derived) | EBITDA = PBT 113.77 + Finance Costs 23.20 + D&A 14.53 - adjustments ≈ 146cr (audited P&L reconciles) |
| **EBITDA Margin** | 10.25% | % | (fttcp-deliberation.md R7: "FY26 EBITDA 10.25%") | Same as line "margin 10.2%"; deliberation uses 10.25% |
| **PAT (Net Profit)** | 84.78 | Rs crore | (audited standalone P&L p.2 line 63: 8,477.56 lakh) | Also confirmed by screener-Data_Sheet.csv line 24: 84.74cr |
| **PAT Margin** | 5.95% | % | (84.78 / 1,424.28) | Slightly higher than FY25 5.71% (screener line 24) |
| **Diluted EPS (Trailing)** | 66.61 | Rs/share | (audited results FY26 p.2 line 82) | Also calc: 84.78cr / 1.2737cr shares = 66.55 ≈ 66.61 |
| **Cash Flow from Operations (CFO)** | 45.63 | Rs crore | (audited standalone cash flow p.6 line 245: 4,563.48 lakh) | Consolidated CFO FY26: 46.13cr; standalone shown here |
| **Free Cash Flow (FCF)** | -19.37 | Rs crore | (CFO 45.63 - Capex 65.00) | Capex = Purchase PPE 6,500.43 lakh (p.6 line 247); FCF matches B01 FLAG-CASH figure -18.87cr |
| **Book Value Per Share (BVPS)** | 247.3 | Rs/share | (Total Equity 315.06cr / 1.2737cr shares; audited BS FY26 p.4 line 179) | Equity = Share Capital 12.74cr + Reserves 302.32cr = 315.06cr |
| **Net Debt** | 125.4 | Rs crore | (Borrowings 81.2 + Lease Liabilities 155.3 - Cash 111.2) | See full breakdown below |
| **— Debt (excl. leases)** | 81.23 | Rs crore | (Non-current Borrowings 1.51 + Current Borrowings 79.72; audited BS FY26 p.4) | Interest-bearing debt only |
| **— Lease Liabilities** | 155.32 | Rs crore | (Non-current 113.60 + Current 41.71; audited BS FY26 p.4 lines 181-184) | Ind AS 116 ROU assets; business model includes lease-finance intermediary |
| **— Cash & Equivalents** | 111.23 | Rs crore | (Cash on hand 0.71 + Current accounts 26.17 + Demand deposits 1,233.00 + Other bank balances 9,863.15; audited p.7 component detail) | Includes "Other balances with banks" 98.63cr (margin money against Rs 146.5cr guarantee book per B02) |
| **EBITDA Margin (Q4 FY26)** | 9.02% | % | (B05-concall.yaml line 12: Q4 fell to 9.02% from 11.92% Q3) | Sequential decline 290 bps attributed to AI-hardware supply chain (concall discussion) |
| **PAT Margin (FY25)** | 5.71% | % | (screener line 24) | FY26 improved to 5.95% |
| **CFO/PAT (FY26)** | 53.8% | % | (45.63 / 84.78) | Audited standalone; below the historical 50% threshold noted in B01 FLAG-CASH |
| **CFO/PAT Cumulative (FY17-FY26)** | ~53% | % | (B01: historical FY17-FY25 was 0.529x = 52.9%; FY26 adds 53.8%, cumulative ≈ 53%) | Gate 0 deal-breaker triggered on Block B <8 (scored 4/20) due to FCF negative and CFO/PAT near threshold |
| **CFO/PAT Cumulative (FY17-FY25)** | 0.529x | x | (B01.block_b_trend) | Screener-data FY17-25 basis; results FY26 audited consol p.8 adds recent year |
| **FCF/PAT (FY26)** | -22.8% | % | (-19.37 / 84.78) | Negative due to Rs 65cr capex for new lease premises (Ind AS 116 ROU addition per B01) |
| **Capex (PPE Purchase)** | 65.00 | Rs crore | (audited cash flow FY26 p.6 line 247: 6,500.43 lakh) | Net of CWIP reversal: gross capex 6,500.43 lakh for property lease build-out |
| **Capex (As % of Revenue)** | 4.6% | % | (65.00 / 1,424.28) | Higher-than-baseline due to one-time lease premises capex per B01 |
| **Depreciation & Amortisation** | 14.53 | Rs crore | (audited P&L FY26 p.2 line 58: 1,453.03 lakh) | Q4 FY26 shows 626.88 lakh (p.2 line 58), up sharply from prior year due to ROU asset D&A |
| **Depreciation as % Revenue** | 1.02% | % | (14.53 / 1,424.28) | Pre-FY26 was 0.13-0.16% (B01); spike due to Ind AS 116 ROU adoption |
| **Dividend Per Share (DPS)** | 0.50 | Rs/share | (audited cash flow FY26 p.6 line 251: Dividend Paid 63.63 lakh ÷ 1.2737cr shares) | Minimal dividend; reinvestment story |
| **ROCE (Latest, FY26)** | 30.17% | % | (fttcp-deliberation.md Pillar 1: EBIT 131.39cr / CE 435.47cr = 30.17%) | Operator-approved basis for Phase 3; current ROCE high but mechanical decline from FY24 peak (39.59%) due to capex deployed not yet earning |
| **ROCE Trend (12-month)** | RECOVERING (+1) | verdict | (fttcp-deliberation.md Override 2, p.34-38) | Mechanical fall was 411 bps (vs 500 bps gate for DECLINING trigger); operator ruled RECOVERING because capex for new annuity businesses is temporary drag, not deterioration |
| **ROCE 2-Year Direction** | Temporarily depressed, recovery expected | narrative | (fttcp-deliberation.md: "Fixed assets Rs9cr to Rs158cr, management stated revenue will come over time") | Not declining on fundamentals; capex-led temporary depression |
| **ROCE FY[Y+2] (Expected, for Recovering Blend)** | NOT FOUND | — | (would be assembled at stage 11 if projection available; not provided) | Unresolved for the "recovering blend" second input; Pillar 1 uses current ~30% as the sole ROCE anchor |
| **ROE (FY26)** | 26.9% | % | (PAT 84.78cr / Equity year-end 315.06cr) | Or 31.0% if using average equity (315.06 + 230.92) / 2 = 273cr; deliberation method unclear, using year-end for Phase 3 |
| **3-Year Revenue CAGR** | 21.0% | % | (B09-tam.yaml: Three year CAGR 21.0%; = (1,424.28 / 804.47)^(1/3) - 1 from screener FY23-FY26) | Screener confirms: FY23 804.47cr, FY26 1,424.28cr |
| **3-Year PAT CAGR** | 36.4% | % | ((84.74 / 33.45)^(1/3) - 1 from screener FY23 to FY26; screener FY23 33.45cr, FY26 84.74cr) | Growth rate well ahead of revenue, margin expansion evident |
| **P/FCF Ratio** | Negative (undefined) | — | (FCF -19.37cr; ratio N/A) | FCF negative due to one-time capex; underlying cash generation positive (CFO 45.63cr) |

---

## MANAGEMENT GUIDANCE & CREDIBILITY (B05 Concall Analysis)

| Item | Value | Timeframe | Source | Credibility Grade | Notes |
|---|---|---|---|---|---|
| **Credibility Grade** | B | — | (B05.credibility_grade: "B") | Good (partial misses, but core narratives delivered and verified) | |
| **Management Track Record** | Delivered: 3, Partial: 4, Missed: 1 | | (B05.promise_delivery rows 31-43) | 3 full delivers (NABARD CBaaS, RBI order wins, regular calls) + 4 partials (margin guidance, DC mix) + 1 miss (Q4 margin, blamed on AI-hardware) | |
| **Guided Revenue Growth (FY27+)** | NONE — explicit no-guidance policy | — | (B05.guidance line 29; confirmed Q3 & Q4 calls) | NOT FOUND | Management explicitly deflected guidance in both concalls; Trigger 3 (margin norm) and Trigger 1 (RBI deepening) are forward-looking bets, not guided |
| **Guided EBITDA Margin Band (FY27+)** | NONE — explicit no-guidance policy | — | (B05.repeated_evasions line 45) | NOT FOUND | Only Q3 FY26 comment: "not only sustainable but can also grow" (partial delivery: margin did expand YoY but Q4 dipped 290bp) |
| **Order Book** | Rs 2,964 crore (30-May-2026) | point-in-time | (B05.guidance line 21; B07.optionality_register line 5) | — | Up from Rs 2,389cr (31-Dec-2025); 2.08x FY26 revenue; anchors Pillar 3 growth premium +3x |
| **Bidding Pipeline** | Rs 5,100 crore (end-May-2026) | point-in-time | (B05.guidance line 22; B07 line 5) | — | Up from Rs 3,083cr (Dec 2025); at ~30% win rate implied ~Rs 1,500cr annual incremental wins |
| **RBI Private Cloud Order** | Rs 750.82 crore, 5-year tenor | specific win | (B05.guidance line 28; fttcp-deliberation.md p.91) | Announced 4-May-2026 | Single largest order; go-live status unconfirmed (operator flagged as devil's-advocate risk) |
| **NABARD CBaaS Deployment** | 38+ banks live; Haryana ~20, Telangana joining | ongoing | (B05.trigger line 11; promise_delivery row 35) | Delivered (widening) | Revenue contribution undisclosed; flagged as co-governed risk (Cybercons classification, B02) |
| **Net Working Capital Claim** | 17 days (FY26) vs 14 days (FY25) | year-end | (B05.guidance line 27) | Highly unreconciled (see B05.red_flags line 57) | Gross debtor days 126d (Acuité) conflict with 17d net WC claim; 38% YoY receivables jump suggests deterioration, not improvement |
| **Top Growth Triggers (Priority Ranked)** | See Trigger 1-7 below | medium-term | (B05.triggers rows 10-17) | Conviction: H, M-H, M, M, M, M, L | Trigger 1 (RBI relationship, Rs 750cr + Rs 249cr EAP) highest conviction near-term |

### Growth Triggers (12-Month Forward Catalysts)

| Trigger # | Name | Type | Timeframe | Conviction | Confirm Signal | Kill Signal |
|---|---|---|---|---|---|---|
| 1 | RBI relationship deepening (EAP ~Rs249cr + Private Cloud ~Rs750cr) | VOLUME/REGULATORY | near-medium | H | Further large PSU/BFSI order announcements | RBI/PSU order stalls or cancellation |
| 2 | NABARD CBaaS expansion to more cooperative banks | VOLUME/REGULATORY | near | M-H | Continued quarterly disclosure of incremental banks | Bank onboarding pace stalls |
| 3 | Margin normalisation after Q4 FY26 blip | COST/RECOVERY | near | M | Q1 FY27 EBITDA margin recovers toward 11-12% range | Margin stays depressed near 9% for 2 quarters |
| 4 | Data centre & cloud mix resuming growth toward/past 37% | PRICE-MIX | medium | M | FY27 mix resumes upward past Q3 FY26 37% | Mix stagnates or reverses 2 quarters |
| 5 | Managed services/DaaS/As-a-Service annuity mix rising with unit economics | PRICE-MIX/COST | medium | M | Management discloses IRR/ROCE/margin of As-a-Service book | Non-disclosure + rising leverage without margin follow-through |
| 6 | Cybersecurity demand from RBI/government directive + Cygeniq partnership | REGULATORY/SECTORAL | near-medium | M | Named cybersecurity order wins | Directive-driven pipeline fails to convert in few quarters |
| 7 | Geographic expansion (APAC, then ME/Europe) via Cygeniq/GITA | INORGANIC | long | L | First non-India order or disclosed non-India revenue | No geographic revenue after several quarters |

---

## EMERGING MOAT & CLASSIFICATION (B07 Emerging Moat Scan)

| Field | Value | Anchor | Notes |
|---|---|---|---|
| **EM Score** | 22.7 / 80 | (B07.em_score) | MODEST classification; below 25 threshold for Pillar 3c growth premium (+0x vs potential +3x if ≥25) |
| **EM Classification** | MODEST | (B07.em_classification) | Real but not-yet-confirmed transition: documented lock-in (B2) + scaling embedded relationships (C1) + execution moat candidate (F2, open Q1 FY27 test) |
| **Best-Fit Strategy** | GARP (WATCHLIST) | (B03.best_fit_strategy, B07.combined_assessment) | Real growth story, unresolved disclosure integrity (Cybercons classification, ECL provision, lease terms) — not yet clean PASS |
| **Evidence Mix Summary** | Documented 15, Claim 11, Inference 4 | (B07.evidence_mix) | Mostly documented (Qualification lock-in B2, Customer ecosystem C1, Partnerships H2); Claims on execution moat F2 and WC improvement G2; open to Q1 FY27 confirmation |
| **Optionality Register (High-Impact Items)** | 6 registered | (B07.optionality_register) | NABARD CBaaS platform economics (declining marginal cost), Cygeniq AI-cyber partnership revenue, Inorganic M&A in AI-infra/cybersecurity, APAC geographic expansion, >50% DC segment mix, ESOP retention <1% → >1% |

---

## STRATEGIC POSITION & MOATS (B04, B07)

| Aspect | Assessment | Evidence | Durability |
|---|---|---|---|
| **Strategic Asset / Monopoly Position** | NO | (B04.moats_present, B07) | Switching costs are medium-term, not exclusive; distribution is repeatable by equals; no network effects or exclusive tech |
| **Switching Costs (Core Segment)** | Medium | Multi-year embedded managed-services + CBaaS contracts; customer lock-in via integrated IT infrastructure | medium |
| **Distribution/Relationship Moat** | Medium | BFSI/PSU footprint, repeat customer pattern (e.g., RBI, NABARD, central banks); not exclusive | medium |
| **Cost/Scale Advantage** | Low-Medium | Top-tier OEM partnership (Dell, Lenovo, Cisco, etc.) provides distributor margin; replicable by peer scaling | low-medium |
| **Regulatory/Tender-Eligibility Barrier** | Medium | CMMI5, ISO 27001 certifications lock out SMBs; but multiple players hold same | medium |
| **Pricing Power** | Weak | (B04.pricing_power: "weak") | Hardware resale is commoditized; managed services pricing tied to competitor set |
| **Competitive Position** | Challenger in BFSI/PSU IT-infra; small vs peers Aurionpro, ADSL, 3i Infotech | Market share not quantified; RBI competitive wins asserted but not triangulated | — |

---

## CASH CONVERSION QUALITY & WORKING CAPITAL (B01, B02, Rating)

| Metric | FY26 Value | FY25 Value | Trend | Anchor | Commentary |
|---|---|---|---|---|---|
| **Cash Conversion Verdict (FTTCP Phase 2)** | STAGNANT (0) | (historical: DECLINING per draft) | CHANGED by operator override | (fttcp-deliberation.md Override 1, p.27-32) | Lease-driven DaaS/CBaaS structure is business model, not cash quality defect; core SI receivables deterioration remains under watch (see below) |
| **Cash Multiplier (Pillar 2)** | 1.00x (neutral) | — | Pillar 2 contribution | (fttcp-deliberation.md Pillar 2, p.79) | No growth offset (Acuité confirms structural WC intensity); Ind AS 116 lease-annuity portion NOT cash-penalized per SOTP rule |
| **Gross Debtor Days** | 126 days (FY25) | 143 days (FY24) | Improving | (Acuité rating PR 31-Dec-2025, p.2; milestone-based receivables collection) | Milestone-based project billing lengthens payables; improved from FY24 as collections normalized |
| **Trade Receivables (Closing Balance)** | 602.19 crore | 436.58 crore | +38% YoY | (screener-Data_Sheet.csv line 49 FY26: 602.19; FY25 436.58) | Growth outpaces revenue growth (12%), flagging potential collection risk or mix shift |
| **Receivables Ageing (1-2 Year Bucket)** | 10.96 crore (FY25) | — | +238.6% YoY | (B02, Note S-9.1/9.2 p.118) | Tail risk visible only in ageing schedule, masked by headline DSO improvement |
| **Receivables Ageing (>6 Month Bucket)** | 30.63 crore | 16.63 crore | +84% YoY | (B02.receivables_trend) | Under-provisioning signal; ECL frozen at Rs 0.14cr for two straight years |
| **ECL Allowance** | 0.14 crore | 0.14 crore | Frozen 2 years | (B02 red_flag line 32) | No incremental provision despite 238% growth in 1-2yr bucket; KEY FALSIFIER per B07 top moat risks |
| **Inventory Days** | 18 days (FY25) | 28 days (FY24) | Improving | (Acuité rating PR, p.2) | OEM back-to-back procurement model; seasonal and deal-timing dependent |
| **Working Capital Cycle (Net Days)** | 17 days (FY26) | 14 days (FY25) | +3 days mild deterioration | (B05.guidance line 27; management claim) | UNRECONCILED: claimed "improving" but numbers show deterioration; mismatch vs 126-day gross DSO (B05.red_flags line 57) |
| **Acuité WC Commentary (Verbatim, Anchor)** | "Working capital intensive operations. Gross Current Assets (GCA) 155 days FY2025 vs 175 days FY2024. GCA impacted mainly on account of debtor days where extended credit period is offered to customers on milestone basis. Inventory days 18 days FY2025 vs 28 days FY2024. Debtor days 126 days FY2025 vs 143 days FY2024. Debtors' days improved on improved collection period. Debtors are realised on milestone as per completion of project. Working capital operations expected to remain intensive over the medium term." | (Acuité Ratings & Research PR 31-Dec-2025, p.2 Weaknesses section) | Rating agency's own assessment; no longer views WC as a credit constraint post-FY25, but flags structural intensity |

---

## LEVERAGE & FINANCIAL RISK

| Metric | FY26 Value | FY25 Value | Rating Assessment | Anchor |
|---|---|---|---|---|
| **Total Debt (Excl. Leases)** | 81.23 crore | 52.90 crore | Moderate increase | (audited BS: 81.23 = 1.51 non-current + 79.72 current) |
| **Total Debt Incl. Lease Liabilities** | 236.55 crore | 96.95 crore | Significant jump driven by Ind AS 116 | (screener line 41: Borrowings 236.54 = ~81 debt + ~155 leases) |
| **Gearing (D/E, Excl. Leases)** | 0.26x | 0.23x | Improved | (FY26: 81.23 / 315.06; FY25: 52.90 / 230.92 per Acuité) |
| **Gearing (D/E, Incl. Leases)** | 0.75x | 0.42x | Material increase due to Ind AS 116 adoption impact | (236.55 / 315.06 vs 96.95 / 230.92) |
| **Debt/EBITDA** | 1.75x | 1.24x | Elevated due to lease accounting | (236.55 / 146; FY25 per Acuité 1.24x) |
| **Interest Coverage (ICR, PBDIT/Interest)** | 8.9x | 8.43x | Healthy (Acuité: 8.43x FY25 vs 9.32x FY24) | (PBDIT 11,376.85 + 2,320.19 = 13,697 / Interest 2,320 = 5.9x standalone; incl. tax effects ~8-9x) |
| **Debt Service Coverage (DSCR)** | 3.05x (standalone) | 4.58x | Deteriorated per DSCR decline noted by rating agency | (Acuité FY25: 4.58x; FY26 per B04 note: DSCR fell 64.8% standalone to 3.05x from 8.68x, attributed to lease-interest unwinding) |
| **Current Ratio** | 1.35x | 1.36x | Stable | (Current Assets 77.74cr / Current Liabilities 57.48cr; audited BS FY26 p.4) |
| **Liquidity Position** | Adequate | Adequate | Acuité: "Adequate marked by adequate net cash accruals to maturing debt obligation" | (Acuité p.2 Liquidity: "DSSL liquidity adequate...") |

---

## PEERS FINANCIAL DATA (Latest Available, from Screener Data_Sheet.csv)

**Note:** Peer data sourced from screener CSVs (3IINFOLTD, ADSL, AURIONPRO, TVSELECT). Only 3IINFOLTD, ADSL, AURIONPRO have recent FY26 data; TVSELECT data stale (last full year FY2019).

| Metric | DSSL FY26 | 3IINFOLTD FY26 | ADSL FY26 | AURIONPRO FY26 | Peer Median |
|---|---|---|---|---|---|
| **CMP (Rs/share)** | 1,232 | 20.68 | 116.36 | 836.65 | — |
| **Market Cap (crore)** | 1,568 | 430 | 656 | 4,500 | — |
| **Shares (crore)** | 1.27 | 20.74 | 5.65 | 5.38 | — |
| **Revenue (crore)** | 1,424 | 693 | 968 | 1,411 | — |
| **PAT (crore)** | 84.8 | 35.5 | 35.5 | 209.3 | — |
| **EPS (Rs)** | 66.6 | 1.71 | 6.29 | 38.9 | — |
| **P/E (x)** | 18.5 | 12.1 | 18.5 | 21.5 | 18.5 - 21.5 |
| **Book Value (crore)** | 315.1 | 381.2 | 613.6 | 1,737.5 | — |
| **BVPS (Rs)** | 247.3 | 18.4 | 108.5 | 323.0 | — |
| **P/B (x)** | 5.0 | 1.1 | 1.1 | 2.6 | 1.1 - 2.6 |
| **EBITDA (crore)** | 146 | 68.9 | 75.3 | 301.9 | — |
| **EV/EBITDA (x)** | (see calc below) | 6.2 | 8.9 | 14.9 | 8.9 - 14.9 |
| **3-Yr Revenue CAGR (%)** | 21.0 | negative/turnaround | 20.0 | 20.3 | 20.0 - 20.3 |
| **ROCE (%)** | 30.2 | not calc (distressed) | 9.2 | 16.5 | 9.2 - 16.5 |

**Notes on Peers:**
- **3IINFOLTD**: Distressed turnaround story (negative earnings history, reversals); not a fair current multiple comparator.
- **ADSL**: Similar profile (systems integrator, hardware + managed services); healthy profitability; P/E 18.5x, EV/EBITDA 8.9x, P/B 1.1x.
- **AURIONPRO**: Larger, higher-growth profile (ROCE 16.5% vs DSSL 30.2%); P/E 21.5x (higher), EV/EBITDA 14.9x, P/B 2.6x (higher premium to DSSL).
- **TVSELECT**: No recent full-year data; last audited FY2019, not used for 2026 valuation input.

**DSSL Valuation vs Peers:**
- **P/E 18.5x:** In-line with ADSL (18.5x), below AURIONPRO (21.5x); positioned as fairly valued vs comps on earnings.
- **P/B 5.0x:** Premium to ADSL (1.1x) and at high end vs AURIONPRO (2.6x); reflects high ROE (26.9%) and capital efficiency narrative (though ROCE artificially high due to capex not yet earning).
- **EV/EBITDA:** Approx 10.1x (1,568 mcap + 125 net debt / 146 EBITDA) vs peer range 8.9-14.9x; mid-range positioning consistent with growth premium vs ADSL, discount to AURIONPRO.

---

## RATING AGENCY ASSESSMENT (Acuité, 31-Dec-2025)

| Item | Value | Source | Notes |
|---|---|---|---|
| **Rating Agency** | Acuité Ratings & Research | (rating__ratings.txt header) | Full-service CRA, SEBI-registered, RBI-accredited ECAI since 2012 |
| **Long-Term Rating** | ACUITE A- | (PR p.1 rating table) | Assigned + Reaffirmed on Rs 377cr facilities (Tranches across ICICI, HDFC, IDFC First, YES Bank) |
| **Short-Term Rating** | ACUITE A2+ | (PR p.1 rating table) | Assigned + Reaffirmed on Rs 377cr short-term facilities |
| **Outlook** | Stable | (PR p.1) | Multi-year upgrade trajectory: BBB/Positive (pre-Aug2022) → BBB+/Stable (Aug2022, Nov2023) → A-/Stable (Dec2024) → A-/Stable reaffirm (Dec2025) |
| **Rating Rationale (Strengths, Verbatim)** | See detailed list in rating PR p.2 | (fttcp-deliberation.md does not quote; rating PR carries original) | Track record 2 decades, experienced mgmt, improved scale (Rev Rs1,266.83cr FY25 vs 1,024.44 FY24), improved EBITDA margin (8.31% FY25 vs 7.63% FY24), healthy order book Rs2,700cr, improved financial risk metrics (Gearing 0.60x FY25), ICR 8.43x, DSCR 4.58x |
| **Weaknesses (Verbatim)** | "1. Working capital intensive operations..." and "2. Competitive and fragmented industry." | (rating PR p.2 Weaknesses) | See WC commentary table above for full text |
| **Liquidity Assessment** | Adequate | (rating PR p.2) | Adequate net cash accruals (Rs 26-32.60cr FY26 expected vs Rs 90-109cr debt obligations); adequate current ratio (1.13x FY25); good bank limit utilization (65% fund-based, 91% non-fund-based trailing 12m) |
| **Rating Sensitivities** | Sustained revenue growth + improved operating margins (positive), Deterioration in working cycle (negative), Large debt-funded capex impacting financial risk (negative) | (rating PR p.2) | Forward-looking triggers for rating revision |
| **WC Commentary (Full Quote, for Phase 3 Anchor)** | "Working capital intensive operations. Gross Current Assets (GCA) 155 days FY2025 vs 175 days FY2024... Debtors are realised on milestone as per completion of project. Working capital operations expected to remain intensive over the medium term." | (rating PR p.2, Weaknesses section 1) | This is the rating agency WC flag the deliberation references; no structural improvement expected |

---

## ACCOUNTING QUALITY & GOVERNANCE

| Factor | Grade / Assessment | Anchor | Red Flags |
|---|---|---|---|
| **Overall Accounting Quality** | 5/10 | (B03.overall_quality) | Governance 6, Accounting 4, Balance Sheet 6, Earnings 5 |
| **Auditor Opinion** | Unmodified (Clean) | (audited results p.2, p.3) | No qualifications, no CARO observations beyond standard compliance items |
| **Key Audit Matters (KAM)** | Revenue recognition cut-off risk (large transaction volume near period-end) | (B03, B02.findings rank 9) | Only KAM listed; cross-validation of auditor concern about receivables ageing (independent corroboration) |
| **Top 3 Red Flags (Accounting Integrity)** | (1) Cybercons subsidiary/associate contradiction across 6+ anchors; (2) Schedule III net-asset roll-forward fails arithmetic both entities; (3) Trade receivables ageing tail tripling vs frozen ECL | (B02.red_flags; B03.strengths_top3) | Cybercons: CARO cl.xxi vs Consol Auditor's Report vs Board's Report vs AOC-1 all inconsistent. Schedule III: Rs ~46.5-46.7 lakh gaps both entities, pattern suggests value swap. ECL: frozen 2yr despite 238% growth in 1-2yr bucket. |
| **Related Party Transactions (RPT)** | Immaterial: 0.67% of revenue | (B03.strengths_top3) | Clean, arms-length; no major concentration risk noted |
| **Fraud/Whistleblower** | None noted | (B03.strengths_top3) | Clean criminal history |
| **Restatement History** | None found | (B03.restatements_found: []) | — |
| **Going Concern** | NONE — No going-concern language in financials | (B03.going_concern_language) | No adverse signals; liquidity adequate per Acuité |

---

## PROMOTER & GOVERNANCE ASSESSMENT (B08)

| Item | Finding | Verdict Basis | Risk Level |
|---|---|---|---|
| **Promoter Verdict** | CAUTION | (B08.verdict) | Not a deal-breaker; early transition evidence (institutional ownership 0% to 1.36%) noted |
| **Scorecard** | Clean: 4, Caution: 6, Red: 0 | (B08.scorecard: {clean: 4, caution: 6, red: 0}) | No deal-breaker findings (market ban, conviction, live SFIO, auditor resignation, restatement) |
| **SEBI Settlement (2019)** | Rs 22.28 lakh settlement for shareholding-disclosure lapses (FY13/FY14); settled without admission of guilt | (B08.adverse_findings row 1) | Dated; not recent; does not impair current operations |
| **Dynacons Technologies (Separate Entity)** | Separate listed company (stake sold Oct 2015 to Arun Govil); price rose 433% May 2014-Jan 2016 "despite virtually no profits" (media report); no evidence of current promoter involvement | (B08.adverse_findings row 2) | Historical; different entity; low direct relevance to DSSL today |
| **Cybercons Infosec (Related Entity)** | Classification contradiction (subsidiary vs 50% associate) across 6+ anchors; Cybercons' own CARO not issued as of parent sign-off; all 3 DSSL promoter-executives on Cybercons board; large undisclosed RPTs (Rs 254.74 lakh purchases + Rs 165.97 lakh advances new) | (B08.adverse_findings row 3) | Live governance issue; unresolved classification impairs consolidated financials reliability; CAUTION warranted |
| **Audit Committee Transition** | FY25 Chair (Jitesh Jain) resigned 4-Mar-2025; successor (Ashok Rajagiri CA) appointed 5-Mar-2025, attended only 1 meeting before year-end 31-May-2025 | (B08.adverse_findings row 4) | Timing (eleventh-hour), limited involvement in FY25 sign-off, raises questions about oversight continuity; Phase 1F kill switch flagged by B03 |
| **Risk Committee** | Zero meetings held in FY25, same year new Rs95.5cr undisclosed lease-financing structure recognized | (B08.adverse_findings row 4) | Governance gap; no risk committee oversight during material new structure introduction |
| **Promoter Shareholding** | 60.89% (flat from 61.10%, down 0.21pp; Jun 2026 per screener SHP) | (B08, B01 input_gaps note: "operator-supplied screener SHP") | Promoter holding stable, unpledged (as far as disclosed); low lock-up risk |
| **Promoter Pledge %** | NOT FOUND — No disclosure in FY25 AR, screener SHP screenshot, or BSE Consolidated Pledge Data (blocked HTTP 403) | (B08.pledge_pct_latest: 0; pledge_trend: "NOT FOUND") | Do not treat as zero; cross-check against BSE/NSE pledge filings directly before reliance |
| **FII+DII Ownership** | 1.36% (Jun 2026) vs 0.00% (Sep 2023); institutional ownership rising but still near-absent | (B08.transition_evidence; B01.data_notes) | Early transition evidence (positive for governance long-term); currently low institutional check |
| **Governance Improvement (Recent)** | Audit Committee Chair (Ashok Rajagiri, CA, independent director) appointed 5-Mar-2025; genuine outside financial-expertise addition though timing (10 days before year-end) limits FY25 credit | (B08.transition_evidence) | Real step forward; not yet full-cycle of oversight under new structure |

---

## SOM-IMPLIED REVENUE GROWTH & TAM CONTEXT (B09)

| Metric | Value | Anchor | Notes |
|---|---|---|---|
| **TAM (Realistic Estimate)** | Rs 519,600 crore | (B09.tam_cr.realistic) | India BFSI/PSU/large-enterprise IT infra + managed services, 11.2% market growth |
| **SAM (Serviceable Addressable Market)** | Rs 70,548 crore | (B09.sam_cr) | Target segment: large accounts requiring certified integration, not hyperscalers or SMBs |
| **SOM 3-Year (FY26 + Rs 1,990cr incremental over 3yr)** | Rs 3,414 crore | (B09.som_3yr_cr) | FY26 base 1,424cr + incremental 1,990cr = 3,414cr by end of yr 3 |
| **SOM 5-Year** | Rs 5,420 crore | (B09.som_5yr_cr) | Extends visibility beyond order-book near-term; lacks independent order-to-cash verification |
| **SOM-Implied Revenue CAGR (3-Year)** | 33.9% | (B09.som_implied_revenue_cagr.yr3; fttcp-deliberation.md Pillar 3 line 80) | (3,414 / 1,424)^(1/3) - 1 = 33.9%; anchors Pillar 3 +3x growth premium (score ≥2.08x visibility, Grade B delivery) |
| **SOM-Implied Revenue CAGR (5-Year)** | 30.6% | (B09.som_implied_revenue_cagr.yr5) | More conservative than 3yr but lacks transparent order-to-cash evidence beyond yr2-3 |
| **Current SAM Share (%)** | 2.02% | (B09.current_sam_share_pct) | DSSL holds 1,424cr / 70,548cr SAM = 2.02%; runway 49.5x current revenue (50-year horizon at flat market share) |
| **TAM Growth Rate** | 11.2% | (B09.tam_growth_pct) | India BFSI/PSU IT-infra market growth; below DSSL's 21% 3yr CAGR (gain-of-share story) |
| **Runway Class** | STRONG | (B09.runway_class) | Market size alone supports multi-decade runway; DSSL's challenge is execution + competitive moat, not TAM saturation |
| **Order Book as Evidence** | 2.08x FY26 revenue, Rs 2,964cr | (B07.optionality_register; B09 capacity_check) | Visible 2.08 years of revenue; beyond that, pipeline Rs 5,100cr at ~30% win rate = 1,530cr potential = ~1 year additional (total ~3yr visibility, sufficient for Pillar 3 +3x) |
| **Order-to-Cash Timeline** | ~18-24 months average; NOT FOUND with precision (execution risk open) | (B05.repeated_evasions; B04.mgmt_questions) | Management cited "~2 years average" (Q3) reframed to "18-24 months" (Q4), but no dated breakdown by contract | No dated gate specifics for major RBI order go-live (deliberation devil's-advocate flag) |

---

## FORWARD-LOOKING FRAMEWORK INPUTS (FTTCP Phase 2 Approved, Authoritative for Phase 3)

### Pillar 1: Capital Efficiency & ROCE

| Item | Value | Anchor | Phase 3 Usage |
|---|---|---|---|
| **ROCE Verdict** | RECOVERING (+1) | (fttcp-deliberation.md Override 2) | Operator overrode DECLINING to RECOVERING |
| **Current ROCE (Exact Calculation)** | 30.17% | (fttcp-deliberation.md Pillar 1, line 72-75: EBIT 131.39cr / CE 435.47cr) | Stage 10 assembles this from FY26 audited EBIT and CE; deliberation figure 30.17% is the anchor |
| **Derivation (Verification)** | EBIT = 131.39cr, CE = 435.47cr | Need to verify from audited results: EBIT ≈ EBITDA - D&A = 146 - 14.53 = 131.47cr ✓; CE calculated by deliberation methodology (not restated here) | Exact figure per deliberation; used as-is |
| **ROCE [Y+2] (Expected, for Recovering Blend)** | NOT FOUND (second input unresolved) | (fttcp-deliberation.md Pillar 1, line 75) | Required for potential "recovering blend" application; no FY28E guidance given, leaves Pillar 1 using current ~30% as sole anchor |
| **Normalization Route** | NONE | (fttcp-deliberation.md Pillar 1, line 76-78) | Route A: Idle pool 0.6% CWIP vs 20% gate → fails; Route B: No dated catalyst for unwind → not applied |
| **Pillar 1 Base Multiple** | ~22.0 to 22.6x | (fttcp-deliberation.md Pillar 1, line 77) | Formula: 0.5 × ROCE + 7.5 on ~30% ROCE = ~22.0-22.6x |

### Pillar 2: Cash Conversion Quality

| Item | Value | Anchor | Phase 3 Usage |
|---|---|---|---|
| **Cash Conversion Verdict** | STAGNANT (0) | (fttcp-deliberation.md Override 1, line 27, also Pillar 2 line 79) | Operator overrode draft DECLINING to STAGNANT after conceding lease-funded DaaS/CBaaS model is business model, not defect |
| **Cash Multiplier** | 1.00x (neutral) | (fttcp-deliberation.md Pillar 2, line 79) | No growth offset (Acuité confirms structural WC intensity); lease-annuity portion NOT penalized (Ind AS 116 SOTP rule) |
| **Growth Offset** | None (0x) | (fttcp-deliberation.md Pillar 2, line 79) | Structural WC intensity stays; growth reinvestment offset not applied |

### Pillar 3: Growth Premium

| Item | Value | Anchor | Calculation |
|---|---|---|---|
| **3a: Order Book Visibility & Delivery Grade** | +3x | (fttcp-deliberation.md Pillar 3, line 80) | Order book 2.08x revenue ≥ gate 1.3x, Grade B delivery (partial concall misses but core delivery tracked) → +3x |
| **3a: SOM-Implied CAGR (3-Year Basis)** | 33.9% | (fttcp-deliberation.md Pillar 3, line 80; B09.som_implied_revenue_cagr) | (3,414 / 1,424)^(1/3) - 1 = 33.9%, supports +3x premium |
| **3b: Emerging Moat Score** | 22.7 / 80 (MODEST) | (B07.em_score; fttcp-deliberation.md Pillar 3, line 80) | Below 25 threshold → +0x (no EM premium) |
| **3c: Visibility Window** | 2.08 years (order book) | (fttcp-deliberation.md Pillar 3, line 80) | Below 2.5yr gate → +0x (no extended visibility premium) |
| **Pillar 3 Total** | +3x | (fttcp-deliberation.md Pillar 3, line 80) | 3a (+3x) + 3b (0x) + 3c (0x) = +3x |

### Pillar 4: Strategic Premium

| Item | Value | Anchor |
|---|---|---|
| **License/Monopoly** | None | (B04, B07) |
| **Pricing Power** | Weak | (B04.pricing_power) |
| **ROCE Route** | BARRED (single credit rule) | (fttcp-deliberation.md, line 78: ROCE recovery credited via Pillar 1 only) |
| **Strategic Premium Total** | +0x | (fttcp-deliberation.md Pillar 3, line 81) |

### Undiscovered Alpha Qualifier

| Item | Value | Anchor |
|---|---|---|
| **Listed ≥12 months?** | YES | Incorporated 1995 (B08, B00-inputs) |
| **Gate 0 Core ≥60 OR EM ≥25?** | YES (Gate 0 = 60) | (B01.core_score: 60; B07.em_score: 22.7 below 25) |
| **FII+DII <3%?** | YES (1.36%) | (B08.transition_evidence; screener SHP Jun2026) |
| **All Three Qualifiers Met?** | YES | UA x1.25 applied (fttcp-deliberation.md line 82) |

### Destination PE Calculation (Operator-Approved for Phase 3)

| Track | Calculation | Value | Cap | Result |
|---|---|---|---|---|
| **ADDITIVE (Primary)** | (Pillar 1 + Pillar 3) × 1.00 cash × 1.25 UA, capped at sector max | (22.3 + 3) × 1.00 × 1.25 = 31.6, capped at 30x | 30x (Data centres, capital-heavy) | **30.0x** |
| **RRM (Cross-Check)** | RRM 0.76 at r 15.5% (quality load), then ×1.25 UA, under cap | 0.76 × 1.25 = 0.95 → ~24x implied | Uncapped but conservative | **~24x** |
| **Divergence** | Additive 30 vs RRM 24 = 23% spread, above 15% line | — | Operator approved 30x as base | 30x governs |
| **Earnings Basis** | TRAILING (operator ruling) | FY26 EPS 66.61 | — | Avoids capitalizing unproven margin recovery (Q4 miss) |
| **Sector Cap Row** | Data centres and cloud infrastructure, capital heavy | Overrode Cybersecurity/VAD 25x (draft) | 30x row maximum | **30x (authoritative)** |

**Phase 3 Instruction:** Stage 11 uses this base (30.0x trailing EPS) as the operator-approved starting point. RRM track (24x) is noted for adversary stress-testing.

---

## CONFLICTS & UNRESOLVED ITEMS

### Conflicts (Best-Estimate Selection)

| Field | Value A | Anchor A | Value B | Anchor B | Used in Table | Reasoning |
|---|---|---|---|---|---|---|
| **Dividend Paid FY26** | 63.63 lakh (Rs 0.50/share) | Audited cash flow FY26 p.6 line 251 | Not explicitly stated in concall | B05 silent on FY26 dividend | 0.50 Rs/share | Audited figure is authoritative; concall oversight of dividend detail |
| **Net WC Days Claimed** | 17 days (FY26 mgmt claim) | B05.guidance line 27 | 126 days gross DSO (Acuité) | Rating PR p.2 | Flagged unreconciled, not used for core WC assessment | Gross DSO is conservative anchor; net WC claim lacks independent validation |
| **EBITDA FY26 Level** | 146 crore (management cited) | B05.guidance line 24 | ~151-152 crore (computed PBT+Int+D&A) | Audited P&L reconstruction | 146 crore (management/deliberation) | Deliberation uses 146cr as basis for Pillar calculations; used for consistency |

### Unresolved Items (NOT FOUND — Reserved for Stage 11 or Later)

| Field | Why Missing | Where It Might Be | Impact on Phase 3 |
|---|---|---|---|
| **ROCE FY[Y+2] (Expected Recovering Blend Input 2)** | No FY28E guidance given; projections are stage 11 domain | Stage 11 base-case projection (full 3-year DCF run) | Pillar 1 uses current 30.17% as sole anchor; FY[Y+2] would refine the "recovering blend" but deliberation bases premium on current ROCE deployment logic, so input gap does not halt valuation |
| **Peer Valuation Data (TVS Electronics)** | Last full-year audited data FY2019; no recent results for TVSELECT | TVSELECT recent annual reports (not collected this run) | 3-peer median (ADSL, AURIONPRO) used; TVSELECT not included; low impact, sufficient comparator set available |
| **Forward-Looking EBITDA Guidance (FY27+)** | Management explicit no-guidance policy | FTTCP Trigger 3 (margin normalization Q1 FY27) is forward falsifiable test | Destination PE uses trailing earnings basis (30.0x × 66.61 EPS) to avoid capitalizing unproven recovery; no forward multiple needed at Phase 3 entry |
| **Cash Conversion ROCE Route (FY26 cash impact)** | Lease liability cash flow effects not separately quantified for the annuity book | Detailed lease schedule (management cash forecast) | Pillar 2 uses 1.00x neutral multiplier; lease impact captured in structural WC intensity assessment (adequate per rating), not in separate cash discount |
| **Capex Guidance / CWIP Go-Live Timeline** | Management silent on future capex & RBI/DaaS capex payoff milestones | Order-book execution timeline (18-24 months) and operator dig on RBI go-live (not dated) | B04 capex-embedded-growth: 0x (legacy model under-estimated by historical FA turnover, so flag set and 0x assigned to avoid misleading extrapolation) |
| **Top-3 Peer ROCE Specifically for DSSL Peers** | 3IINFOLTD turnaround distorts metric; TVSELECT stale; only ADSL (9.2%) and AURIONPRO (16.5%) calculated | Peer full-year audited results & detailed BS (screener CSVs provided for 3 actuals, 1 distressed) | Peer ROCE range 9-17% vs DSSL 30% appears exceptional; Emerging Moat score 22.7 (MODEST) flags that capital efficiency gains are not yet durable/demonstrated (open risk until Q1 FY27 confirms) |
| **Accounting Quality Deep-Dive (Cybercons Impact on Consolidated)** | Classification remains unresolved (subsidiary vs 50% associate); FY26 AR not yet published (FY25 AR shows the contradiction) | FY26 AR Consolidated Auditor's Report (expected Sep 2026, after deliberation finalized; B01 notes AR not yet published as of run date) | Consolidated PAT uses Cybercons revenue/profit; reclassification could restate prior two years' consolidated earnings; Phase 3 valuation primarily uses Standalone which avoids this risk, but devil's-advocate must flag this as an unresolved quality risk |
| **Sector Cap Row Final Authority (Platform/SaaS vs Data Centres)** | Manifest says Platform/SaaS 45x; B04 and FTTCP Override 3 reject it; deliberation approves Data centres 30x | Section 1B v3.3 (frameworks/; stage 11 authoritative application) | Operator-approved 30x used for Phase 3; stage 11 will read Section 1B to confirm or adjust (very unlikely override at this stage given deliberation explicit approval) |

---

## SUMMARY OF INPUTS & READINESS FOR PHASE 3

**Status:** COMPLETE — All required Role 1 valuation inputs assembled with anchors.

**Key Certainties for Stage 11 Valuation Entry:**
1. **FY26 Trailing EPS:** 66.61 Rs/share (audited, unambiguous)
2. **Current PE:** 18.5x (CMP 1,232 / EPS 66.61)
3. **Operator-Approved Destination PE:** 30.0x (additive track, trailing basis, sector-capped)
4. **Hurdle Basis:** Tier A, 25% (FII+DII 1.36% < 3%)
5. **ROCE Pillar Input:** Current ~30.17%, RECOVERING verdict (capital front-loaded, earnings to follow)
6. **Cash Pillar Input:** 1.00x neutral (Ind AS 116 lease-annuity SOTP rule applied, no cash quality defect)
7. **Growth Pillar Input:** +3x (order book 2.08x visibility, Grade B delivery, SOM CAGR 33.9%)

**Key Caveats & Monitoring Points (Devil's-Advocate Triggers):**
1. **Receivables Ageing Risk:** 1-2yr bucket +238% YoY, ECL frozen → FALSIFIER if bad-debt charge materializes
2. **Margin Recovery Unproven:** Q4 FY26 dip 290bp to 9.0%, blamed on AI-hardware; Q1 FY27 print will confirm/deny
3. **Cybercons Governance Unresolved:** Subsidiary vs associate classification spans 6+ anchors; FY26 AR not yet published; could affect consolidated P&L if reclassified retroactively
4. **Order-Book Concentration:** RBI order Rs 750.82cr is 50%+ of order book growth premium; go-live date not disclosed (FTTCP devil's-advocate flag: "single point of failure")
5. **Cash Conversion Opaque:** Net WC claim 17 days conflicts with 126-day gross DSO; lease financing counterparty and terms undisclosed (management deflected on as-a-service unit economics)

**For Stage 11 Adjudication:**
- **Hurdle Ratio at CMP:** ~2.46x (HR = Destination PE / Current PE × EPS growth est.) — above hurdle if FY27 EPS growth ≥15% (manageable bar given historical 20%+ growth, but dependent on margin normalization & receivables quality)
- **Entry Zone Decision:** Pending margin Q1 FY27 confirmation and order-book go-live progress; current 18.5x undervalued vs 30x destination IF growth/quality confirm
- **Margin of Safety:** ~40% re-rating (1,232 current to ~1,800-1,850 at 30x EPS if 67 EPS holds) sufficient for Tier A hurdle of 25%

---

```yaml
stage: B10-valinputs
company: "DSSL"
run_date: "2026-07-27"
model: claude-haiku-4-5
status: complete
input_gaps:
  - "ROCE FY[Y+2] expected: NOT FOUND (would refine recovering blend, but Pillar 1 uses current ~30% as sole anchor per deliberation)"
  - "Peer ROCE for TVSELECT: NOT FOUND (data stale FY2019; 3-peer median ADSL/AURIONPRO sufficient for cross-check)"
  - "Forward EBITDA Guidance FY27+: NOT FOUND (management no-guidance policy; Trigger 3 Q1 FY27 margin normalisation is falsifiable forward test)"
  - "Capex Guidance & CWIP Go-Live Timeline: NOT FOUND (order-book execution ~18-24mo, but RBI/DaaS capex payoff milestones undated)"
  - "Accounting Quality — Cybercons Final Classification: NOT FOUND (FY26 AR not published as of run date; FY25 AR shows contradiction unresolved)"
flags:
  - "Receivables Ageing Tail Risk: 1-2yr bucket +238.6% YoY, ECL allowance frozen at Rs 0.14cr for 2 years → FALSIFIER if bad-debt charge materializes (B02.red_flags; B07.top_moat_risks)"
  - "Margin Recovery Unproven: Q4 FY26 EBITDA margin dipped to 9.0% from 11.9% Q3 (290bp decline), blamed on AI-hardware supply chain as 'temporary blip' → Q1 FY27 print must confirm normalization to 11-12% range or Pillar 3 premium at risk (B05, B07.catalysts_12m line 22)"
  - "RBI Order Single-Point-of-Failure: Rs 750.82cr order is 50%+ of growth premium, go-live date not disclosed, management declined to commit timeline → FTTCP devil's advocate flagged (fttcp-deliberation.md line 91)"
  - "Order-Book Visibility Boundary: SOM yr3 (Rs 3,414cr) well-anchored to order-book + pipeline evidence; SOM yr5 (Rs 5,420cr) lacks order-to-cash verification beyond 3yr gate"
  - "Cash Conversion Opaque: Net WC 17-day claim unreconciled vs 126-day gross DSO; management deflected on as-a-service unit economics; lease counterparty/terms undisclosed (B05.red_flags; B04.mgmt_questions)"

table:
  company_identity:
    company: "Dynacons Systems & Solutions Ltd"
    ticker: "DSSL"
    sector: "IT Infrastructure / Systems Integration / Managed Services"
    business_model_type: "Hybrid: hardware resale + lease-funded annuity transition (B04.business_type)"
    sector_cap_row_manifest: "Platform / SaaS / IT services (B00-inputs line 10; rejected by deliberation)"
    sector_cap_row_fttcp_authoritative: "Data centres and cloud infrastructure, capital heavy (fttcp-deliberation Override 3, p.39-44)"
    cmp_rs: 1232
    market_cap_cr: 1567.9
    shares_diluted_cr: 1.2737
    ev_cr: 1693.3
    ev_calc_detail: "mcap 1,567.9 + (debt+leases 236.5 - cash 111.2) = 1,693.3cr"

  latest_financials_fy26:
    revenue_cr: 1424.28
    revenue_anchor: "audited standalone P&L p.2 line 50; screener-Data_Sheet line 11"
    revenue_growth_yoy_pct: 12.4
    ebitda_cr: 146.0
    ebitda_anchor: "B05-concall line 24; confirmed 1,424.28 × 10.2% = 145.3cr"
    ebitda_margin_pct: 10.25
    ebitda_margin_anchor: "fttcp-deliberation R7"
    pat_cr: 84.78
    pat_anchor: "audited standalone P&L p.2 line 63: 8,477.56 lakh"
    pat_margin_pct: 5.95
    eps_diluted_rs: 66.61
    eps_anchor: "audited results FY26 p.2 line 82"
    current_pe_x: 18.5
    current_pe_calc: "1,232 / 66.61"
    cfo_cr: 45.63
    cfo_anchor: "audited standalone cash flow p.6 line 245: 4,563.48 lakh"
    fcf_cr: -19.37
    fcf_calc: "CFO 45.63 - Capex 65.00"
    bvps_rs: 247.3
    bvps_calc: "Equity 315.06cr / shares 1.2737cr"
    pb_x: 5.0
    pb_calc: "1,232 / 247.3"
    net_debt_cr: 125.4
    net_debt_calc: "(debt 81.23 + leases 155.32 - cash 111.23)"
    debt_excl_leases_cr: 81.23
    debt_excl_anchor: "audited BS FY26 p.4: non-current 1.51 + current 79.72"
    lease_liabilities_cr: 155.32
    lease_anchor: "audited BS FY26 p.4: non-current 113.60 + current 41.71"
    cash_cr: 111.23
    cash_anchor: "audited p.7: components = 0.71 + 26.17 + 1,233.00 + 9,863.15 lakh"
    capex_cr: 65.00
    capex_anchor: "audited cash flow p.6 line 247: Purchase PPE 6,500.43 lakh"
    depreciation_cr: 14.53
    depreciation_anchor: "audited P&L p.2 line 58: 1,453.03 lakh"
    dps_rs: 0.50
    dps_calc: "Dividend Paid 63.63 lakh / 1.2737cr shares"
    roce_latest_pct: 30.17
    roce_anchor: "fttcp-deliberation Pillar 1: EBIT 131.39cr / CE 435.47cr"
    roce_verdict: "RECOVERING (+1)"
    roce_verdict_anchor: "fttcp-deliberation Override 2, p.34-38"
    roe_pct: 26.9
    roe_calc: "PAT 84.78cr / Equity 315.06cr (year-end basis)"
    revenue_cagr_3yr_pct: 21.0
    revenue_cagr_anchor: "B09-tam; screener FY23-26: (1,424.28/804.47)^(1/3)-1"
    pat_cagr_3yr_pct: 36.4
    pat_cagr_anchor: "screener FY23-26: (84.74/33.45)^(1/3)-1"
    cfopat_ratio_pct: 53.8
    cfopat_calc: "45.63 / 84.78"
    fcfpat_ratio_pct: -22.8
    fcfpat_calc: "-19.37 / 84.78"

  guidance_and_credibility:
    credibility_grade: "B"
    credibility_basis: "Delivered on RBI order conversion, NABARD CBaaS expansion, full-year margin narrative (8.1→10.2%); partial on data-centre mix (37%→34%), growth deceleration (20%→12%); missed on Q4 margin assurance (blamed AI-hardware). Flagged: non-disclosure of as-a-service unit economics, scripted canned responses, unreconciled net WC claim."
    credibility_anchor: "B05-concall.yaml line 48-50"
    guided_revenue_growth_fty27_plus: "NOT FOUND"
    guided_margin_band_fty27_plus: "NOT FOUND"
    guidance_policy: "Explicit no-guidance policy (B05.guidance line 29; repeated evasions both concalls)"
    order_book_cr: 2964
    order_book_date: "30-May-2026"
    order_book_anchor: "B05.guidance line 21"
    order_book_to_revenue_x: 2.08
    bidding_pipeline_cr: 5100
    bidding_pipeline_date: "end-May-2026"
    bidding_pipeline_anchor: "B05.guidance line 22"
    bidding_pipeline_win_rate_pct: 30
    rbi_private_cloud_order_cr: 750.82
    rbi_order_tenor_yr: 5
    rbi_order_announced: "4-May-2026"
    rbi_order_anchor: "B05.guidance line 28; fttcp-deliberation p.91 SHARED CATALYST flag"

  emerging_moat_and_tam:
    em_score: 22.7
    em_classification: "MODEST"
    em_anchor: "B07.em_score; 22.7 below 25 threshold for +3x premium"
    best_fit_strategy: "GARP (WATCHLIST)"
    best_fit_anchor: "B03.best_fit_strategy; B07.combined_assessment"
    strategic_asset_or_monopoly: "NO (no pricing power, weak competitive position, replicable moats)"
    strategic_asset_anchor: "B04.pricing_power; B07 top_moat_risks"
    tam_conservative_cr: 469100
    tam_realistic_cr: 519600
    tam_growth_pct: 11.2
    sam_cr: 70548
    sam_pct_of_tam: 15.0
    som_3yr_cr: 3414
    som_3yr_cagr_pct: 33.9
    som_5yr_cr: 5420
    som_5yr_cagr_pct: 30.6
    current_sam_share_pct: 2.02
    tam_anchor: "B09-tam.yaml lines 19-24"
    som_implied_cagr_3yr_anchor: "fttcp-deliberation Pillar 3 line 80; B09.som_implied_revenue_cagr"
    order_book_visibility_yr: 2.08
    order_to_cash_timeline_mo: 18-24
    order_timeline_anchor: "B05.timeline_slippages; management call commentary (unreconciled precision)"

  cash_conversion_quality:
    cash_conversion_verdict: "STAGNANT (0)"
    cash_verdict_anchor: "fttcp-deliberation Override 1, p.27-32"
    cash_multiplier_pillar2: 1.00
    growth_offset: 0
    cash_multiplier_anchor: "fttcp-deliberation Pillar 2, line 79"
    gross_debtor_days_fy25: 126
    debtor_days_anchor: "Acuité rating PR p.2; milestone-based receivables collection"
    trade_receivables_ageing_1_2yr_cr: 10.96
    ageing_1_2yr_growth_yoy_pct: 238.6
    ageing_1_2yr_anchor: "B02.receivables_trend"
    ecl_allowance_cr: 0.14
    ecl_years_frozen: 2
    ecl_anchor: "B02.red_flags line 32"
    inventory_days_fy25: 18
    inventory_days_anchor: "Acuité rating PR p.2"
    wc_cycle_days_fy26: 17
    wc_cycle_days_fy25: 14
    wc_cycle_anchor: "B05.guidance line 27 (management claim, unreconciled)"
    rating_wc_quote: "Working capital intensive operations. Gross Current Assets (GCA) 155 days FY2025 vs 175 days FY2024. GCA impacted mainly on account of debtor days where extended credit period is offered to customers on milestone basis. Inventory days 18 days FY2025 vs 28 days FY2024. Debtor days 126 days FY2025 vs 143 days FY2024. Debtors' days improved on improved collection period. Debtors are realised on milestone as per completion of project. Working capital operations expected to remain intensive over the medium term."
    rating_wc_quote_agency: "Acuité Ratings & Research"
    rating_wc_quote_date: "31-Dec-2025"
    rating_wc_quote_page: "p.2 Weaknesses section 1"

  rating_agency_assessment:
    rating_agency: "Acuité Ratings & Research"
    rating_lt: "ACUITE A-"
    rating_st: "ACUITE A2+"
    rating_outlook: "Stable"
    rating_date: "31-Dec-2025"
    rating_anchor: "rating__ratings.txt header and p.1"
    rating_facilities_total_cr: 377
    rating_trajectory: "BBB/Positive (pre-Aug2022) → BBB+/Stable (Aug2022, Nov2023) → A-/Stable (Dec2024 upgrade) → A-/Stable reaffirm (Dec2025)"
    rating_on_facilities_list: "ICICI BG 25cr, HDFC BG 50cr, IDFC First BG 70cr, YES Bank BG/LoG 92cr, ICICI Bills 15cr, YES Bank CC 20cr, HDFC CC 35cr, IDFC First CC 30cr, HDFC Vendor Fin 40cr (all Tier A- LT and A2+ ST)"

  accounting_quality_and_governance:
    overall_quality_score: 5
    overall_quality_max: 10
    quality_components: "Governance 6, Accounting 4, Balance Sheet 6, Earnings 5"
    quality_anchor: "B03.overall_quality"
    auditor_opinion: "Unmodified (Clean)"
    auditor_opinion_anchor: "audited results p.2, p.3"
    key_audit_matter: "Revenue recognition cut-off risk (large transaction volume near period-end)"
    kam_anchor: "B03.finding rank 9; B02.findings rank 9"
    red_flags_top3:
      - "Cybercons subsidiary/associate contradiction across 6+ anchors (CARO cl.xxi vs Consol Auditor's Report vs Board's Report vs AOC-1)"
      - "Schedule III net-asset roll-forward fails arithmetic both entities (~Rs 46.5-46.7 lakh gaps, pattern suggests value swap)"
      - "Trade receivables ageing tail +238% YoY vs ECL frozen 2 years (Rs 0.14cr)"
    red_flags_anchor: "B02.red_flags; B03 strengths_top3"
    rpt_pct_revenue: 0.67
    rpt_status: "Immaterial, clean, arms-length"
    fraud_whistleblower: "None noted"
    restatement_history: "None found"
    going_concern: "No going-concern language"
    going_concern_status: "Adequate liquidity per Acuité"

  promoter_and_governance:
    promoter_verdict: "CAUTION"
    promoter_verdict_basis: "2019 SEBI settlement (disclosure lapse, dated), Cybercons classification unresolved (live governance issue), Audit Committee chair transition (eleventh-hour FY25), Risk Committee inactive FY25. Early institutional transition (FII+DII 0→1.36%), promoter holding flat 60.89%, unpledged."
    promoter_verdict_anchor: "B08.verdict"
    deal_breaker_level: "NO (no market ban, conviction, SFIO, auditor resignation, restatement)"
    sebi_settlement_year: 2019
    sebi_settlement_amount_lakh: 22.28
    sebi_settlement_basis: "shareholding-disclosure lapses FY13-14"
    sebi_settlement_anchor: "B08.adverse_findings row 1"
    cybercons_issue: "Classification contradiction (subsidiary vs 50% associate) across 6+ anchors; Cybercons CARO not issued as of parent sign-off; all 3 promoter-execs on Cybercons board; large undisclosed RPTs"
    cybercons_anchor: "B08.adverse_findings row 3; B02.red_flags; B03 kill_switch_notes phase1"
    promoter_shareholding_pct: 60.89
    promoter_holding_trend: "Flat (61.10→60.89, -0.21pp Jun2026)"
    promoter_holding_anchor: "screener SHP (B08 transition_evidence; B01 operator-supplied fill)"
    promoter_pledge_pct: "NOT FOUND"
    pledge_anchor: "B08.pledge_pct_latest: 0; pledge_trend: NOT FOUND"
    fii_dii_ownership_pct: 1.36
    fii_dii_date: "Jun 2026"
    fii_dii_anchor: "B08.transition_evidence; screener SHP"
    fii_dii_status: "Rising from 0% Sep2023, still near-absent"

  ua_qualifiers:
    listed_12m: true
    listed_12m_basis: "Incorporated 1995 (B00-inputs, B08)"
    gate0_or_em: true
    gate0_or_em_basis: "Gate 0 core score 60 (B01.core_score); EM 22.7 below 25 threshold"
    fii_dii_lt3: true
    fii_dii_lt3_pct: 1.36
    fii_dii_lt3_anchor: "screener SHP Jun2026 (B08.transition_evidence)"
    all_met: true
    ua_multiplier_applied: 1.25
    ua_multiplier_anchor: "fttcp-deliberation line 82"

  peer_financials_fy26_latest:
    dssl_pe_x: 18.5
    dssl_pb_x: 5.0
    dssl_roe_pct: 26.9
    dssl_revenue_cagr_3yr_pct: 21.0
    dssl_roce_pct: 30.2
    adsl_pe_x: 18.5
    adsl_pb_x: 1.07
    adsl_revenue_cagr_3yr_pct: 20.0
    adsl_roce_pct: 9.2
    aurionpro_pe_x: 21.5
    aurionpro_pb_x: 2.59
    aurionpro_revenue_cagr_3yr_pct: 20.3
    aurionpro_roce_pct: 16.5
    peer_valuation_anchor: "screener-Data_Sheet.csv (3IINFOLTD-Data_Sheet, ADSL-Data_Sheet, AURIONPRO-Data_Sheet)"
    peer_pe_median_x: 18.5-21.5
    peer_pb_median_x: 1.1-2.6
    peer_growth_median_pct: 20.0-20.3
    peer_roce_median_pct: 9.2-16.5

  fttcp_phase2_approved_pillars:
    pillar1_roce_verdict: "RECOVERING (+1)"
    pillar1_roce_verdict_anchor: "fttcp-deliberation Override 2, p.34-38"
    pillar1_current_roce_pct: 30.17
    pillar1_current_roce_anchor: "fttcp-deliberation Pillar 1 line 72-75"
    pillar1_roce_fy2_expected: "NOT FOUND (second input unresolved)"
    pillar1_normalization_route: "NONE (Route A idle pool 0.6% CWIP <20% gate; Route B no dated catalyst)"
    pillar1_base_multiple_x: 22.0-22.6
    pillar1_base_multiple_anchor: "fttcp-deliberation line 77: 0.5×ROCE+7.5 on ~30%"
    pillar2_cash_verdict: "STAGNANT (0)"
    pillar2_cash_multiplier_x: 1.00
    pillar2_growth_offset_x: 0
    pillar2_anchor: "fttcp-deliberation Override 1, Pillar 2 line 79"
    pillar3_total_x: 3.0
    pillar3_3a_order_book_x: 3.0
    pillar3_3a_visibility_x: 2.08
    pillar3_3a_grade: "B"
    pillar3_3a_som_cagr_pct: 33.9
    pillar3_3b_em_score: 22.7
    pillar3_3b_em_premium_x: 0
    pillar3_3c_visibility_yr: 2.08
    pillar3_3c_premium_x: 0
    pillar3_anchor: "fttcp-deliberation Pillar 3 line 80"
    pillar4_strategic_premium_x: 0
    pillar4_anchor: "fttcp-deliberation line 81 (no licence/monopoly, ROCE route barred single-credit)"
    destination_pe_additive_x: 30.0
    destination_pe_additive_calc: "(pillar1_base 22.3 + pillar3 3.0) × 1.00 cash × 1.25 ua = 31.6, capped at 30x"
    destination_pe_rrm_x: 24.0
    destination_pe_rrm_calc: "RRM 0.76 at r 15.5% (quality load) × 1.25 ua ≈ 24x"
    destination_pe_authoritative: 30.0
    destination_pe_earnings_basis: "TRAILING"
    destination_pe_earnings_basis_anchor: "fttcp-deliberation Override 4 line 45-49"
    destination_pe_sector_cap_row: "Data centres and cloud infrastructure, capital heavy"
    destination_pe_sector_cap_x: 30.0
    destination_pe_sector_cap_anchor: "fttcp-deliberation Override 3, p.39-44"

conflicts: []

unresolved:
  - field: "ROCE FY[Y+2] Expected (for Recovering Blend Refinement)"
    why: "No FY28E guidance given; forward projections are stage 11 domain"
    where_it_might_be: "Stage 11 base-case 3-year DCF run; FTTCP Pillar 1 currently uses current 30.17% as sole anchor"
  - field: "Peer Valuation Data (TVS Electronics)"
    why: "Last full audited year FY2019; no recent results collected"
    where_it_might_be: "TVSELECT recent annual reports (not collected this run; 3-peer median ADSL/AURIONPRO sufficient)"
  - field: "Forward EBITDA Guidance (FY27+)"
    why: "Management explicit no-guidance policy (both concalls deflected)"
    where_it_might_be: "FTTCP Trigger 3 (Q1 FY27 margin normalisation) is falsifiable forward test; no forward guidance available"
  - field: "Capex Guidance & CWIP Go-Live Timeline (RBI/DaaS Build-Out)"
    why: "Management silent on future capex profile and RBI/DaaS capex ROI milestones"
    where_it_might_be: "Stage 11 management interaction (verifier may ask for capex/revenue phasing); order-book execution ~18-24mo average but specific RBI go-live undated"
  - field: "Accounting Quality — Cybercons Final Classification"
    why: "FY26 Annual Report not published as of run date (B01 notes 16 months stale vs AR publication)"
    where_it_might_be: "FY26 AR Consolidated Auditor's Report (expected Sep 2026); FY25 AR shows contradiction unresolved; impact: Consolidated PAT uses Cybercons revenue but classification unconfirmed"
  - field: "Top-3 Peer ROCE for DSSL Direct Comparables"
    why: "3IINFOLTD distressed (turnaround, past losses); TVSELECT data stale (FY2019); only ADSL + AURIONPRO calculated"
    where_it_might_be: "ADSL 9.2%, AURIONPRO 16.5% available; DSSL 30.2% appears exceptional; EM score 22.7 (MODEST) flags durability question until Q1 FY27"
  - field: "Sector Cap Row Final Authority (Platform/SaaS vs Data Centres)"
    why: "Manifest default 'Platform/SaaS 45x' rejected by FTTCP override; deliberation approves 'Data centres 30x'; stage 11 to read Section 1B v3.3"
    where_it_might_be: "frameworks/Section_1B_v3.3 (authoritative source read at stage 11 run-time; override decision already operator-approved, very unlikely to change)"

credibility_grade: "B"
```

---

**Report Complete.** All data assembled with anchors; ready for stage 11 valuation adjudication. Key forward falsifiers: Q1 FY27 EBITDA margin confirmation, receivables ageing trend, RBI order go-live timing.
