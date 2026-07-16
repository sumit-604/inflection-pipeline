# STAGE 10: VALUATION INPUT ASSEMBLY
## Fedbank Financial Services Ltd (FEDFINA)
**Run Date:** 2026-07-15  
**Report Date:** 2026-07-16  
**Model:** Claude Haiku 4.5  
**Status:** Complete  

---

## COMPANY IDENTITY BLOCK

| Field | Value | Anchor |
|---|---|---|
| Company | Fedbank Financial Services Ltd | manifest.yaml |
| Ticker | FEDFINA | manifest.yaml |
| Business Type | Lending (NBFC-ND-SI, primarily gold loans and LAP) | B04-bizmodel.yaml |
| Sector Cap Row | Banks / NBFCs / MFIs, 18x absolute | manifest.yaml (corrected 2026-07-16) |
| CMP (Rs) | 164.0 | manifest.yaml (screener.in, 15 Jul 2026 close) |
| Market Cap (Rs Cr) | 6,132 | manifest.yaml (screener.in, 15 Jul 2026 close) |
| Shares Outstanding (Diluted, Cr) | 3.742 (post-Q1 ESOP allotment June 2026) | results-A.txt Q1FY27 (37421L equity capital / 10 face value) |
| Book Value per Share (Rs) | 78.2 | fttcp-deliberation.md (screener.in) |
| Market P/B | 2.09x | fttcp-deliberation.md (screener.in) |
| Market P/E | 16.0x | fttcp-deliberation.md (screener.in, 15 Jul 2026 close) |

### Enterprise Value (Computed)
- Market Cap: Rs 6,132 Cr
- Total Debt (Mar 31, 2026): Debt Securities (Rs 1,730.31 Cr) + Borrowings excl. debt securities (Rs 10,837.47 Cr) + Subordinated Liabilities (Rs 916.35 Cr) = Rs 13,484.13 Cr (results-B.txt, Balance Sheet, pages 7-8)
- Cash & Equivalents (Mar 31, 2026): Rs 1,339.73 Cr (results-B.txt, Balance Sheet p.7)
- Net Debt: Rs 13,484.13 - Rs 1,339.73 = Rs 12,144.4 Cr
- **Enterprise Value: Rs 18,276.4 Cr** (arithmetic: 6,132 + 12,144.4)

---

## LATEST FINANCIALS (FY26 / YEAR ENDED MARCH 31, 2026)
**Source Priority:** Results PDFs (results-B.txt, audited as of April 28, 2026) supersede Annual Report for FY26.  
**Note:** Q4 FY26 results cover full-year FY26 ending March 31, 2026. Q4 FY26 (quarter-only) refers to the Jan 1 - Mar 31, 2026 quarter disclosed within the full-year results.

| Metric | FY26 Value (Rs Lakhs) | Anchor |
|---|---|---|
| **Revenue & Income** | | |
| Interest Income | 210,907 | results-B.txt p.6, Statement Line 1(a) |
| Fee & Commission Income | 9,669 | results-B.txt p.6, Statement Line 1(b) |
| Net Gain on Fair Value Changes | 1,784 | results-B.txt p.6, Statement Line 1(c) |
| Total Revenue from Operations | 222,360 | results-B.txt p.6, Statement Line I |
| Other Income | 301 | results-B.txt p.6, Statement Line II |
| **Total Income** | **222,661** | results-B.txt p.6, Statement Line III |
| **Expenses** | | |
| Finance Cost | 87,932 | results-B.txt p.6, Statement Line 1(a) under Expenses |
| Fees & Commission Expenses | (201) | results-B.txt p.6, Statement Line 1(b) under Expenses |
| Impairment on Financial Instruments | 11,527 | results-B.txt p.6, Statement Line 1(c) under Expenses |
| Employee Benefit Expense | 44,393 | results-B.txt p.6, Statement Line 1(d) under Expenses |
| Depreciation & Amortisation | 5,447 | results-B.txt p.6, Statement Line 1(e) under Expenses |
| Other Expenses | 27,281 | results-B.txt p.6, Statement Line 1(f) under Expenses |
| **Total Expenses** | **176,560** | results-B.txt p.6, Statement Line IV |
| **Profit Before Tax** | **46,101** | results-B.txt p.6, Statement Line V |
| Tax Expense | 11,741 | results-B.txt p.6, Statement Line VI |
| **Net Profit (PAT)** | **34,360** | results-B.txt p.6, Statement Line VII |
| **Diluted EPS (Rs, face value 10)** | **9.12** | results-B.txt p.6, Statement Line XII (Diluted) |

### Balance Sheet (as of March 31, 2026)

| Metric | Value (Rs Lakhs) | Anchor |
|---|---|---|
| **Assets** | | |
| Cash & Cash Equivalents | 133,973 | results-B.txt p.7, Balance Sheet Line 1(a) |
| Bank Balances (excl. cash) | 5,122 | results-B.txt p.7, Balance Sheet Line 1(b) |
| Loans | 1,431,885 | results-B.txt p.7, Balance Sheet Line 1(e) |
| Investments | 40,167 | results-B.txt p.7, Balance Sheet Line 1(f) |
| Other Financial Assets | 20,736 | results-B.txt p.7, Balance Sheet Line 1(g) |
| **Total Financial Assets** | **1,656,352** | results-B.txt p.7, Balance Sheet |
| PPE & Intangibles | 22,001 | results-B.txt p.7 (tangible + right-of-use + intangibles) |
| Other Non-Financial Assets | 9,125 | results-B.txt p.7 |
| **Total Assets** | **1,687,478** | results-B.txt p.7 |
| **Liabilities & Equity** | | |
| Debt Securities Outstanding | 173,031 | results-B.txt p.7, Balance Sheet Line 1(c) |
| Borrowings (excl. debt securities) | 1,083,747 | results-B.txt p.7, Balance Sheet Line 1(d) |
| Subordinated Liabilities | 91,635 | results-B.txt p.7, Balance Sheet Line 1(e) |
| Other Financial Liabilities | 21,638 | results-B.txt p.7 |
| **Total Financial Liabilities** | **1,390,035** | results-B.txt p.7 |
| Equity Share Capital | 37,421 | results-B.txt p.7, Balance Sheet Line 1(a) under Equity |
| Other Equity (Reserves) | 255,189 | results-B.txt p.7, Balance Sheet Line 1(b) under Equity |
| **Total Equity / Net Worth** | **292,610** | results-B.txt p.7 |

### Cash Flow (FY26 / Year Ended March 31, 2026)

| Metric | Value (Rs Lakhs) | Anchor |
|---|---|---|
| Operating Cash Flow (CFO) | (166,416) | results-B.txt p.8, Cash Flow Statement Line A (Net cash from operating activities) |
| Investing Cash Flow | (246,198) | results-B.txt p.8, Cash Flow Statement Line B (Net cash used in investing activities) |
| Capex (tangible assets) | 2,761 | results-B.txt p.8, Cash Flow Statement Line B (Purchase of tangible assets) |
| Depreciation | 5,447 | results-B.txt p.6, P&L Statement Line 1(e) |
| Free Cash Flow (CFO - Capex) | (169,177) | Computed: (166,416) - 2,761 |

### Key Financial Ratios (FY26)

| Ratio | Value | Anchor | Notes |
|---|---|---|---|
| **Return Metrics** | | | |
| ROE (Annual) | 12.6% | fttcp-deliberation.md; manifest.yaml (screener.in) | Current ROE as of 15 Jul 2026 close |
| ROA (Annual, computed) | 2.28% | Computed from results-B.txt: PAT 34,360 / Avg Assets 1,506,224 | FY26 computed; rating.txt shows 9MFY26 annualised ROA 2.50% |
| ROCE (Latest) | NOT FOUND | B01-gate0.yaml | NBFC balance sheet structure makes ROCE non-computable per regulatory Ind AS 7 |
| ROCE Trend (2-year) | NOT FOUND | B01-gate0.yaml | Not applicable to NBFC model |
| **Profitability Metrics** | | | |
| EBITDA (approx) | 134,033 | Computed: PBT 46,101 + Finance Cost 87,932 | Excludes adjustments for other income |
| EBITDA Margin | 60.3% | Computed: 134,033 / 222,360 | High due to finance cost treatment in NBFC model |
| PAT Margin | 15.43% | results-B.txt p.7, Disclosure section | Matches: 34,360 / 222,661 |
| **Cash Conversion Metrics** | | | |
| CFO / PAT (Latest Year) | (4.84)x | Computed: (166,416) / 34,360 | Negative; structural per NBFC Ind AS 7 treatment |
| CFO / PAT (Cumulative FY21-FY26) | (5.04)x | B01-gate0.yaml | 6-year cumulative negative (flag: structural for NBFC) |
| FCF / PAT (Latest Year) | (4.92)x | Computed: (169,177) / 34,360 | Negative; all 6 years FY21-FY26 FCF-negative |
| **Leverage & Capitalisation** | | | |
| Debt-to-Equity Ratio | 4.61x | results-B.txt p.10, Disclosure section (Debt Equity Ratio) | Per Ind AS: [Debt Securities + Borrowings + Subordinated] / [Equity] |
| Total Debt to Total Assets | 0.80 | results-B.txt p.10, Disclosure section | Structural to NBFC model |
| CRAR (Capital Adequacy Ratio) | 22.40% | results-B.txt p.7, Disclosure section (Sector specific ratios) | Comfortably above 18% regulatory minimum |
| **Asset Quality Metrics** | | | |
| GNPA (Gross Non-Performing Assets %) | 1.87% | results-B.txt p.7, Disclosure section (Sector specific ratios, Mar 31, 2026) | Improved from 2.02% (FY25) per rating.txt |
| NNPA (Net NPA %) | 1.28% | results-B.txt p.7, Disclosure section (Sector specific ratios, Mar 31, 2026) | Improved from 1.22% (FY25) |
| Provision Coverage Ratio (PCR) | 32.29% | results-B.txt p.7, Disclosure section (Sector specific ratios, Mar 31, 2026) | Thin vs normal 60-70%; thinned from 40.0% (FY25) |
| **Liquidity Metrics** | | | |
| Liquidity Coverage Ratio | 152.00% | results-B.txt p.7, Disclosure section (Sector specific ratios, Mar 31, 2026) | Strong, above 100% |

### 3-Year Growth CAGRs (FY24 to FY26)

| Metric | FY24 | FY26 | CAGR | Anchor |
|---|---|---|---|---|
| Total Income (Rs Cr) | 1,623 | 2,227 | 17.3% | Rating.txt p.5 (FY24), results-B.txt p.6 (FY26) |
| PAT (Rs Cr) | 244.7 | 343.6 | 18.5% | Rating.txt p.5 (FY24), results-B.txt p.6 (FY26) |
| AUM (Rs Cr) | 12,191.9 | ~17,500 (as of 9MFY26 per rating.txt) | ~19.8% (3-yr) | Rating.txt p.5 |

---

## GUIDANCE, CATALYSTS & EXECUTION (FROM B05)

| Item | Guidance | Timeframe | Status | Anchor |
|---|---|---|---|---|
| **Quantified Guidance (FY26)** | | | | |
| Credit Cost | 1.0% +/- 10bps | FY26 | Delivered: Q1=0.8%, Q2=0.9%, Q3=0.9% | B05-concall.yaml, promise_delivery rows |
| New Gold Branches | 100-150 branches | FY26 | Delivered: 113 through Q3 FY26 | B05-concall.yaml, promise_delivery |
| Branch Co-location | 75-80 branches | FY26 | Partial: 63 by Q3, remainder plausible in Q4 | B05-concall.yaml |
| Gold AUM Mix | 45-49% of book | FY26 | Delivered: ~45.2% at Q3 FY26 | B05-concall.yaml |
| Gold Tonnage Growth | 10-12% CAGR | Ongoing | Peer data contradicts: Manappuram shows 2.8% YoY vs Fedfina's 10-12% claim | B05-concall.yaml, B06-peers.yaml |
| Unsecured Business Loan Exit | 100% of Rs 770 Cr | Q1 FY26 | Delivered: Full de-recognition same quarter | B05-concall.yaml |
| **Unquantified Guidance** | | | | |
| FY27 Credit Cost Guidance | TBD | Q4 FY26 call | Deferred (as of Q3); not yet delivered | B05-concall.yaml, line 28 |
| FY27 Opex Guidance | TBD | Q4 FY26 call | Deferred (as of Q3) | B05-concall.yaml, line 28 |
| ST LAP Collections In-housing | Complete | Q4 FY26 | Slipped from Q2 to Q3 to Q4; still incomplete as of Q3 | B05-concall.yaml, timeline_slippages |

### Management Credibility Assessment
**Grade:** B (Good, with caveats) (B05-concall.yaml)

**Basis:** 
- Delivered cleanly on headline turnaround metrics (credit cost, secured-mix transition, DA reduction) with honest, unprompted self-blame framing
- BUT: Two dated technical commitments (ST LAP scorecards Q3 FY26, MT LAP BRE pilot) silently dropped
- Collections in-housing slipped two quarters; CRAR/Tier 2 disclosure disappeared during highest-leverage quarter
- (B05-concall.yaml, credibility_basis)

### Top 2-3 Growth Triggers (Next 12 Months)
1. **Gold branch rollout to 150 branches (FY26), AUM/branch maturation** – Confirmed Signal: Q4 FY26 branch count ≥140-150 and AUM/branch >Rs 13.3 Cr; Kill Signal: branch stalls <130 (B05-concall.yaml, triggers row 1)
2. **Credit cost held inside 1% +/- 10bps through FY26 exit, FY27 guidance given** – Confirmed Signal: Q4 FY26 credit cost ≤1.1% and actual FY27 number issued; Kill Signal: credit cost >1.1% or FY27 guidance deferred (B05-concall.yaml, triggers row 2)
3. **ST LAP collection in-housing completes, disbursement growth resumes** – Confirmed Signal: Q4 FY26 confirms transition done and ST LAP disbursals >Rs 208 Cr meaningfully; Kill Signal: completion date pushed again or disbursals flat (B05-concall.yaml, triggers row 3)

---

## EMERGING MOAT & CLASSIFICATION (FROM B07)

| Field | Value | Anchor |
|---|---|---|
| EM Score | 25.3 | B07-emoat.yaml |
| EM Classification | STRENGTHENING | B07-emoat.yaml (borderline, at bottom edge of band) |
| **Active Moat Categories** | | |
| C2 - Customer Concentration Improving | Moderate | B07-emoat.yaml |
| D2 - Digital Platform | Moderate | B07-emoat.yaml |
| F2 - Execution Moat | Strong | B07-emoat.yaml (3 quarters documented, FY27 test pending) |
| G1 - Funding Cost & Diversification | Moderate | B07-emoat.yaml |
| H2 - Strategic Partnerships (Federal Bank) | Moderate | B07-emoat.yaml (co-lending, brand access) |
| R1 - RBI Gold Loan Framework Tailwind | Moderate | B07-emoat.yaml (industry-wide, not proprietary) |
| **Combined Assessment** | TURNAROUND | B07-emoat.yaml (Gate 0 AVOID fixed by F2 execution, but EM at bottom of band and FY27 hardest promises unverified) |

### Primary Catalyst (Next 12 Months)
**Credit cost normalisation** – Drives both asset-quality transition (Transition 3) and return transition (Transition 8); shared catalyst flag raised. (fttcp-deliberation.md, ruling 12)

### Evidence Quality Mix
Mostly documentary (19 of 38 evidence points), with 12 management claims and 7 inferences. (B07-emoat.yaml, evidence_mix)

---

## STRATEGIC ASSET / MONOPOLY POSITION (FROM B04, B07)

| Assessment | Finding | Anchor |
|---|---|---|
| **Moats Present** | Yes, moderate durability | B04-bizmodel.yaml, moats_present |
| Federal Bank Parentage | Moderate – 60.80% ownership, liquidity/brand access, but creates dependency | B04-bizmodel.yaml; fttcp-deliberation.md (strategic premium ruled +0x base, institutional backing optional +1x) |
| Regulatory/Licensing (NBFC-ND-SI + CRAR) | Moderate – licensing barrier, but common to peer NBFCs | B04-bizmodel.yaml |
| Distribution (757 branches, doorstep gold, app) | Moderate – scale in branch network, but peers also expanding | B04-bizmodel.yaml |
| **Strategic Premium Rating** | +0x base | fttcp-deliberation.md (single-credit rule: ROE recovery credited in Pillar 1, re-rating route barred) |
| **Optional Strategic Premium** | +1x for Federal Bank institutional backing (for Phase 3/Role 3 to argue) | fttcp-deliberation.md, left to default |

---

## PEER COMPARISON (FROM B06)

**Peer Universe:** Manappuram, SBFC, Five-Star Business Finance, MAS Financial

### Key Findings

| Metric | FEDFINA | Peer Range | Finding | Anchor |
|---|---|---|---|---|
| **Cost-to-Income** | 56-57% | SBFC 35%, Five-Star 31-41%, MAS 36.6% | FEDFINA 15-25 points higher | B06-peers.yaml, verified claims |
| **Gold Tonnage Growth (YoY)** | Claims 10-12% CAGR | Manappuram 2.8% YoY | Gap contradicts claim; gold growth appears to be price/mix, not volume | B06-peers.yaml, contradicted claim |
| **Sub-Rs5L LAP Stress** | Claims MFI spillover | All 4 peers report similar patterns | Verified: stress is sector-wide spillover, not FEDFINA-specific | B06-peers.yaml, verified |
| **Maharashtra/Tamil Nadu LAP Stress** | Claims company-specific concentration | Five-Star (TN: <1.5%), SBFC (TN: not large), MAS (stress in MP/Raj) | Contradicted: states report different stress; FEDFINA narrative unsupported | B06-peers.yaml, contradicted |

---

## PROMOTER & GOVERNANCE (FROM B08)

| Field | Status | Anchor |
|---|---|---|
| Promoter | Federal Bank Limited (60.80% as of Mar 31, 2025) | B08-promoter.yaml, annual-report.txt |
| Promoter Pledge % | 0% (nil since IPO Nov 2023) | B08-promoter.yaml, pledge_pct_latest |
| Promoter Verdict | CAUTION | B08-promoter.yaml |
| **Adverse Finding:** Executive Turnover | Near-total senior layer turnover in ~18 months (MD&CEO, CRO x2, COO vacant, 2 CBOs, CS) | B08-promoter.yaml |
| **Transition Evidence:** New MD Hired | Parvez Mulla, 29-year BFSI career (ext'l NRC process, Nov 2024) | B08-promoter.yaml, transition_evidence |
| Institutional Investor Entry | Nomura India bought True North's 6.8644% stake, May 2026 | B08-promoter.yaml, transition_evidence |
| Independent Directors (New) | 3 new independent directors appointed FY25 with external credentials | B08-promoter.yaml, transition_evidence |
| Overall Governance Scorecard | 5 clean, 4 caution, 1 red | B08-promoter.yaml, verdict_basis |

---

## TAM / SOM / REVENUE HEADROOM (FROM B09)

| Field | Value | Anchor |
|---|---|---|
| **Market Definition** | Organized (bank+NBFC) secured lending to self-employed/MSME India via gold loans and property-backed LAP/home loans | B09-tam.yaml |
| **TAM (Conservative)** | Rs 23,10,000 Cr | B09-tam.yaml, tam_cr |
| **TAM (Realistic)** | Rs 29,00,000 Cr | B09-tam.yaml, tam_cr |
| **SAM** | Rs 12,48,000 Cr (54% of conservative TAM) | B09-tam.yaml, sam_cr |
| **Current SAM Share %** | 1.7% | B09-tam.yaml, current_sam_share_pct |
| **Revenue Headroom** | 59.1x | B09-tam.yaml, revenue_headroom_x |
| **SOM (3-year projection)** | Rs 39,900 Cr | B09-tam.yaml, som_3yr_cr |
| **SOM (5-year projection)** | Rs 68,600 Cr | B09-tam.yaml, som_5yr_cr |
| **SOM-Implied Revenue CAGR (3-yr)** | 23.6% | B09-tam.yaml, som_implied_revenue_cagr yr3 |
| **SOM-Implied Revenue CAGR (5-yr)** | 26.6% | B09-tam.yaml, som_implied_revenue_cagr yr5 |
| **Capacity Check** | Gap of Rs 9,730 Cr (yr3) / Rs 30,340 Cr (yr5) vs branch capex-embedded growth (12.6%); achievable via per-branch AUM productivity + co-lending funding with Federal Bank | B09-tam.yaml, capacity_check |
| **Runway Classification** | MASSIVE (59x headroom) | B09-tam.yaml, runway_class |

---

## CASH CONVERSION & WORKING CAPITAL (FROM B01, B02, B03, RATING)

### B01 Assessment
- **Block B (Cash Conversion):** 0/20 (score triggered deal-breaker: CFO/FCF negative all 6 years FY21-FY26, Ind AS 7 structural)
- **Block B Trend:** Deteriorating – Direct assignment (DA) gain-on-sale income rose to ~50% of PBT (FY25) from ~28% (FY24); cumulative CFO/PAT FY21-FY26 = -5.04x; PCR fell from 40.0% (FY25) to 32.29% (FY26) (B01-gate0.yaml)
- **Cash Determination (per deliberation):** STRUCTURAL and mechanical (not a quality failure); direct-assignment reliance being wound down. Ind AS 7 classification of loan disbursement as operating outflow is structural to NBFC lending model, NOT a cash-quality red flag. (fttcp-deliberation.md, item 9)

### B02 Working Capital Trend
- Trade receivables (non-loan): Fell 44.1% YoY (Rs 34.52 Cr to Rs 19.31 Cr), but >6-month ageing bucket worsened to 23.5% from ~16.0% (FY24). Assessed as deteriorating on ageing mix, improving on absolute balance. (B02-notes.yaml, receivables_trend)
- **Finding:** Core loan-book asset quality (Stage 3/NPA) is separate and more material concern, tracked in red flags. (B02-notes.yaml)

### Rating Agency Working Capital Commentary (CARE Ratings, April 10, 2026)
**Quote (Verbatim from rating.txt, p.3):**
> "Liquidity: Strong – Per asset liability management (ALM) dated December 31, 2025, there are no negative cumulative mismatches across all time buckets. As on December 31, 2025, the company maintained total liquidity of ~₹8,379 crore comprising cash and bank balances of ₹404 crore and liquid investments of ₹386 crore. It also has undrawn sanctioned credit lines of ₹1,352 crore and expected inflows from advances of ₹7,589 crore in the next one year against scheduled repayments of ₹4,519 crore. Liquidity is further supported by the gold loan portfolio, which forms ~45% of AUM and has a short behavioural tenor of 3-4 months, enabling quick churn. Overall, the company's liquidity profile appears adequate to meet debt obligations in the next one year."

**Agency:** CARE Ratings (CareEdge)  
**Rating:** CARE AA+; Stable  
**Date:** April 10, 2026 (Reaffirmation as of October 8, 2025)  
**Page:** Rating.txt p.3

---

## REGULATORY REQUIREMENTS & QUALIFICATIONS

### Unlisted to Listed (UA) Qualifier Check

| Qualifier | Status | Finding | Anchor |
|---|---|---|---|
| **Listed ≥12 months?** | YES | IPO Nov 30, 2023; as of July 16, 2026 = 31.5 months | B03-ardeep.yaml (IPO date), manifest (run date) |
| **Gate 0 ≥60 OR EM ≥25?** | PARTIAL | Gate 0 = 48/100 (AVOID), EM = 25.3/100 (STRENGTHENING at bottom edge). EM clears ≥25, Gate 0 fails. | B01-gate0.yaml (core_score 38, classification AVOID), B07-emoat.yaml (em_score 25) |
| **FII + DII < 3%?** | NOT FOUND | Shareholding breakdown in provided sources does not include FII/DII split. | Manifest, B08 do not provide this data |
| **All Three Met?** | **NO** | FII+DII data missing; Gate 0 failed (AVOID classification overrides EM pass). | Combined assessment |

**Conclusion:** Stock does **NOT** meet full UA qualifier criteria (missing FII/DII data, Gate 0 AVOID).

---

## RATING PDF EXTRACTION

**Agency:** CARE Ratings Limited (CareEdge Ratings)  
**Rating:** CARE AA+; Stable (on long-term facilities; A1+ on short-term)  
**Outlook:** Stable  
**Date:** April 10, 2026 (Press Release date, reaffirming Oct 8, 2025 rating)  

**Key Rating Strengths (verbatim excerpts):**
- Strong parentage and support from FBL (~₹471 Cr cumulative equity infusions; outstanding funding ~₹1,325.53 Cr as of Q1FY26)
- Adequate capitalisation (TNW ~₹2,776 Cr as of Dec 31, 2025; CAR 20.50% in 9MFY26, above 18% minimum)
- Significant scale-up (AUM 41% CAGR since FY18; ~₹17,500 Cr as of Dec 31, 2025)

**Key Rating Constraints:**
- Moderate asset quality (GNPA 2.10%, NNPA 1.40% as of Dec 31, 2025)
- Geographic concentration (~75.9% in top 5 states)
- High reliance on bank borrowings (87.5% of debt from term loans/ECB/STLs)
- Earnings sensitivity to direct assignment (DA) income (~50% of PBT in FY25 vs ~28% in FY24)

---

## CONFLICTS & CONTRADICTIONS

### Conflicts Identified

| Field | Value A | Anchor A | Value B | Anchor B | Resolution & Used Value |
|---|---|---|---|---|---|
| PCR (Latest Period) | 32.29% (Mar 31, 2026) | results-B.txt p.7 | 38.36% (June 30, 2026, Q1FY27) | results-A.txt p.7 | Q1FY27 more current; 38.36% reflects latest (post-run deliberation); used in table |
| Credit Cost (FY26 annualised) | 0.77% (implied from FY26 impairment 11,527 / avg assets) | Computed from results | ~1.0% guidance band (1% +/- 10bps delivered) | B05-concall.yaml | Rating.txt clarifies actual credit cost FY25 was 1.8%, FY26 normalised ~0.9%; full-year FY26 impairment includes reserve adjustments; rating more authoritative |
| Tonnage Growth (Gold) | 10-12% CAGR (management claim) | B05-concall.yaml | 2.8% YoY (Manappuram peer, Feb 2026) | B06-peers.yaml | Peer data contradicts claim; FEDFINA's high AUM growth is price/mix-driven, not tonnage-driven |
| No conflicts on core financial figures (P&L, B/S, CF) | FY26 audited | results-B.txt | No prior-period restatements noted | results-B.txt Note 12 | Aligned |

---

## UNRESOLVED ITEMS

| Field | Why Unresolved | Where It Might Be | Impact on Valuation |
|---|---|---|---|
| **FY-wise ROE/ROA Series (FY21-FY26)** | Only current ROE 12.6% and computed FY26 ROA 2.28% provided; historical annual series not in run inputs | Annual Reports FY21-FY26 (not in run folder) or investor presentations with multi-year summaries | Pillar 1 relies on 60/40 blend of current (12.6%) and FY[Y+2] expected ROE; historical trend informs confidence in recovery trajectory |
| **Q4 FY26 Actuals (Quarter-only)** | Results available only through full-year FY26 (ended Mar 31, 2026). Q4 FY26 result filing released April 29, 2026 per ICICI Securities note (B02 reference), but actual filing document NOT in run/derived/ folder. Task notes: Q4 FY26 credit cost, RoA, RoE claims in deliberation (0.6%, 2.6%, 14%) are non-anchored. | Actual NSE/BSE filing of Q4 FY26 results (expected ~Apr 29, 2026 per B02); FY26 AR Note 53 Contingent Liabilities | Q4 FY26 credit cost critical to validating Pillar 2L Asset-Quality Multiplier 1.00x self-withdraw condition (if >1.1% or PCR thins, reverts to 0.80x) |
| **FY[Y+2] Expected ROE** | Not computed; this is a stage-11 projection input requiring detailed forward earnings bridge | Stage 11 model (Opus), to be filled from forward guidance and management commentary | Pillar 1 base multiple = 0.5 x ROE + 7.5; for 40-60% RECOVERING read, uses 60/40 blend of current 12.6% and forward expected ROE. Without forward ROE, Pillar 1 multiple cannot be finalised. |
| **Cost of Equity** | Not computed; stage-11 task. Required for P/B theoretical = ROE / Cost of Equity, and WACC-based valuation if cross-check method used. | Stage 11 (Opus role); inputs: risk-free rate (10Y GSec current), market risk premium, FEDFINA beta (requires regression or peer proxy) | Primary method is P/B (ROE-adjusted); secondary cross-check P/E. Cost of equity drives P/B calibration and destination PE upper bound. |
| **FII + DII Shareholding %** | Shareholding pattern in manifest and B08 does not break out FII/DII separately. Exchange filings may carry this. | NSE/BSE shareholding pattern filing (Regulation 31 LODR) as of latest quarter (Q1FY27) | UA qualifier check (FII+DII <3%); does not affect valuation tables but gates UA-driven modifiers. |

### Data Gaps Noted in Source Blocks (Non-Critical to B10)
- Promoter pledge % not in AR initially, resolved via web search to nil (B08)
- Screening-FEDFINA peer-only CSV absent (B01)
- Prospectus folder absent, RHP used as backup for backward years (B01, B03)
- FY26 AR Note 53 Contingent Liabilities not yet published (B01)
- Current Liabilities line absent from NBFC Ind-AS balance sheet (B01, B04 per Reg 52(4) disclosure)
- IIFL Finance / HDB Financial Services AUM not retrieved for peer aggregation completeness (B09, time-boxed)
- Direct CRISIL MI&A / ICRA PDFs returned 403 (B09, relied on secondary sources)

---

## SUMMARY: DATA QUALITY & ASSEMBLY CONFIDENCE

**Financial Data Quality:** High (audited FY26 results with unmodified auditor opinion, results-B.txt p.3-5; Q1FY27 limited-reviewed Q1 results, results-A.txt p.3-5)

**Upstream Analysis Quality:** Comprehensive (all 9 blocks completed, peer data sourced, promoter background verified, TAM/SOM fully modelled)

**Anchor Completeness:** All core financial figures carry source anchors. Ratios and computed metrics clearly traced to source P&L/B/S lines.

**Valuation Input Readiness for Stage 11:**
- Pillar 1 (ROE-based): Current ROE anchored (12.6%), methodology set (0.5 x ROE + 7.5, floor 9x, cap 24x, 60/40 blend for RECOVERING). **Awaits:** FY[Y+2] expected ROE, cost of equity.
- Pillar 2L (Asset-Quality Multiplier): 1.00x (Sound) anchored to operator override, self-withdraw condition named (Q4 FY26 credit cost >1.1% or PCR thins). **Awaits:** Q4 FY26 actuals to confirm or revoke.
- Primary Method (P/B): ROE / CoE framework set. **Awaits:** Cost of equity.
- Secondary Method (P/E): Destination PE ~12-16x per deliberation; market P/E 16.0x at top of band. Cross-check ready once primary methodology yields target P/B.
- Sector Cap: 18x (absolute), primary method P/B, secondary P/E. **Confirmed.**

---

**Report Compiled by:** Stage 10 Assembly Engine (Claude Haiku 4.5)  
**Run Date:** 2026-07-15  
**Report Timestamp:** 2026-07-16  
**Status:** Complete, ready for handoff to Stage 11 (Role 1, Opus).


```yaml
stage: B10-valinputs
company: "FEDFINA"
run_date: "2026-07-15"
model: claude-haiku-4-5-20251001
status: complete

input_gaps:
  - "Q4 FY26 result filing (dated 2026-04-29 per B02, not in run/derived folder) — Q4 credit cost, ROA, ROE actuals non-anchored in deliberation"
  - "FY-wise historical ROE/ROA series (FY21-FY26) — only current 12.6% ROE and computed FY26 2.28% ROA available"
  - "FY[Y+2] expected ROE — projection input for stage 11, not backfilled from prior stages"
  - "Cost of equity — stage 11 task; required for P/B theoretical = ROE / CoE and destination PE calibration"
  - "FII + DII shareholding % — not in manifest or B08; UA qualifier cannot be fully verified"

flags:
  - "FLAG-CASH (B01): CFO/PAT -5.04x (6-year cumulative), all years negative. Structural per NBFC Ind AS 7, NOT a cash-quality failure. Asset quality recovery credited via Pillar 1, direct-assignment reliance being wound down. (fttcp-deliberation.md)"
  - "FLAG-ASSETQUALITY (B02): Impairment charge +228.6% YoY; PCR thinned 40.0% to 32.29%; NPA vintage aging in Doubtful 1-3yr bucket; Stage 3 reconciliation gap across notes. Real but recoverable per FTTCP STARTING (forward RECOVERING) verdict. (B02, B01)"
  - "FLAG-EMOAT-BORDERLINE (B07): EM score 25.3 at bottom edge of STRENGTHENING band. Half of active categories industry-shared tailwinds (R1, H2). Two hardest FY27 promises unverified. (B07)"
  - "FLAG-GUIDANCE-SLIPPAGE (B05): ST LAP in-housing slipped Q2->Q3->Q4 FY26; CRAR/Tier 2 disclosure dropped in Q3; ST LAP scorecards and MT LAP BRE pilot silently dropped. (B05)"
  - "FLAG-ASSET-QUALITY-OVERRIDE (fttcp-deliberation.md override 2): Pillar 2L lifted to 1.00x (Sound band nominally wants PCR 60-70%, FEDFINA 32-38%). Self-withdraws to 0.80x if Q4 FY26 credit cost breaks 1.1% or PCR thins further."
  - "FLAG-Q4-FY26-DATA-GAP: Q4 FY26 result filing (released 2026-04-29) not in run inputs. Non-anchored claims: credit cost 0.6%, RoA 2.6%, RoE 14%. Must be verified against actual filing."

market_inputs:
  cmp_rs: 164.0
  market_cap_rs_cr: 6132
  bvps_rs: 78.2
  market_pb: 2.09
  market_pe: 16.0
  shares_lakh: 3742.1
  anchor: "manifest.yaml / fttcp-deliberation.md (screener.in, 15 Jul 2026 close)"

latest_financials_fy26:
  total_income_rs_cr: 2226.61
  pat_rs_cr: 343.60
  diluted_eps_rs: 9.12
  net_worth_rs_cr: 2926.10
  finance_cost_rs_cr: 879.32
  impairment_charge_rs_cr: 115.27
  anchor: "results-B.txt (FY26 audited, Statement of P&L)"

key_ratios:
  roe_current_pct: 12.6
  roe_note: "current; Pillar 1 uses 60/40 blend of current and FY[Y+2] expected ROE per RECOVERING verdict"
  roa_fy26_pct: 2.28
  roce_latest: "NOT FOUND (NBFC Ind AS balance sheet; ROCE non-computable, structural)"
  crar_pct: 22.40
  gnpa_pct: 1.87
  nnpa_pct: 1.28
  pcr_pct_fy26: 32.29
  pcr_pct_q1fy27: 38.36
  pcr_note: "thin vs 60-70% norm; latest 38.36% (Q1FY27, results-A.txt); FY26 year-end 32.29% (results-B.txt)"
  lcr_pct: 152.0
  de_ratio_x: 4.61
  cfo_pat_cumulative_6yr_x: -5.04
  anchor: "results-A.txt (Q1FY27) / results-B.txt (FY26 audited) / B01"

growth_metrics:
  revenue_3yr_cagr_fy24_fy26_pct: 17.3
  pat_3yr_cagr_fy24_fy26_pct: 18.5
  aum_3yr_cagr_fy24_fy26_pct: 19.8
  anchor: "rating.txt / results-B.txt"

deliberation_overlay_authoritative:
  pillar1_basis: "ROE not ROCE (Section 1B Amendment 7). 0.5 x ROE + 7.5, floor 9x, cap 24x. RECOVERING 40-60% -> 60/40 blend of current 12.6% and FY[Y+2] expected ROE."
  primary_method: "P/B (theoretical P/B = ROE / cost of equity); destination PE secondary cross-check"
  pillar2L_asset_quality_multiplier: "1.00x (Sound), OPERATOR OVERRIDE (draft 0.80x). Self-withdraws to 0.80x if Q4 FY26 credit cost >1.1% or PCR thins further."
  sector_cap_row: "Banks / NBFCs / MFIs, 18x absolute"
  single_credit: "ROE recovery credited via Pillar 1; Strategic re-rating route barred"
  strategic_premium_base: "+0x (optional +1x Federal Bank institutional backing left for stage 11/Role 3 to argue)"
  shared_catalyst: "credit-cost normalisation drives both asset-quality and return transitions"
  cash_determination: "STRUCTURAL and mechanical (not a quality failure)"
  anchor: "fttcp-deliberation.md"

emerging_moat:
  em_score: 25.3
  em_classification: "STRENGTHENING (borderline, bottom edge)"
  combined_assessment: "TURNAROUND"
  anchor: "B07"

management:
  credibility_grade: "B"
  promoter: "Federal Bank Ltd, 60.80% stake, pledge nil"
  promoter_verdict: "CAUTION"
  new_md: "Parvez Mulla (Nov 2024)"
  rating: "CARE AA+; Stable (10 Apr 2026)"
  anchor: "B05 / B08 / rating.txt"

tam:
  runway_class: "MASSIVE"
  revenue_headroom_x: 59.1
  current_sam_share_pct: 1.7
  mgmt_claim_read: "inflated (4.0x conservative TAM)"
  anchor: "B09"

peer_benchmark:
  fedfina_cost_to_income_pct: "56-57"
  peer_cost_to_income: "SBFC 35, Five-Star 31-41, MAS 36.6"
  gold_growth_quality: "AUM growth price/mix-driven not volume; Manappuram tonnage 2.8% YoY vs FEDFINA claim 10-12%"
  anchor: "B06"

ua_qualifiers:
  listed_12m: "YES (IPO Nov 2023)"
  gate0_or_em: "PARTIAL (Gate0 48 AVOID fails; EM 25.3 clears)"
  fii_dii_lt3: "NOT MET (DII alone ~18.8% per shareholding; FII+DII well above 3%)"
  all_met: "NO -> UA does not apply"
  note: "B10 originally marked FII/DII NOT FOUND; shareholding-pattern-screener.txt shows FII 0.66% + DII 18.82% (Mar-2026) = ~19.5%, so UA clearly fails the <3% test"

unresolved:
  - "FY-wise ROE/ROA series FY21-FY26 (only current available)"
  - "Q4 FY26 standalone quarter filing and its credit cost / RoA / RoE (full-year FY26 IS anchored; Q4 breakout is not)"
  - "FY[Y+2] expected ROE (stage-11 projection input for the Pillar 1 60/40 blend)"
  - "Cost of equity (stage-11 task; drives P/B = ROE/CoE)"

handoff_status: "Complete and ready for Stage 11 (Role 1 valuation, Opus)"
```
