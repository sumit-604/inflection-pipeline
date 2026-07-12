# STAGE 10: VALUATION INPUT ASSEMBLY (AMENDMENT 4.5 REFRESH)
## Tatva Chintan Pharma Chem Ltd (TATVA)
**Run Date:** 2026-07-12 | **Model:** Claude Haiku 4.5 | **Mode:** Valuation-only refresh, Amendment 4.5 normalized ROCE anchor

---

## ROLE 1 VALUATION INPUT TABLE

### COMPANY IDENTITY BLOCK

| Field | Value | Anchor |
|-------|-------|--------|
| Company Name | Tatva Chintan Pharma Chem Ltd | (Manifest) |
| Ticker | TATVA | (Manifest) |
| Sector (manifest auto-pick) | Pharma / CDMO | (Manifest) |
| **Sector Cap Row (corrected)** | **Specialty Chemicals, 35x** | (Deliberation record, line 19: "Specialty chemicals, 35x, correcting the manifest's Pharma / CDMO 38x") |
| Business Model Type | Manufacturing, four-product specialty chemicals | (B04) |
| CMP (Rs) | 1,326.0 | (Manifest) |
| Market Cap (Rs Cr) | 3,103.0 | (Manifest) |
| Shares Outstanding (Diluted, Cr) | 2.339 | (Consolidated results Q4 FY26, line 388: "Paid-up equity share capital 233.92 million") |
| Net Debt (FY26, Rs Mn) | 1,146.1 | (Consolidated results Q4 FY26 balance sheet: Borrowings current 1,153.63 + non-current 50.10 = 1,203.73 Mn; Cash 57.64 Mn; Net Debt = 1,203.73 - 57.64 = 1,146.09 Mn) |
| Enterprise Value (Mcap + ND, Rs Mn) | 32,176.1 | (31,030 + 1,146.1, computed) |

---

### LATEST FINANCIALS (FY26 / Q4 FY26)

**All latest-period figures from Consolidated Audited Results Q4 FY26 (16 May 2026), 31 Mar 2026 period-end.**

| Metric | Value | Unit | Anchor |
|--------|-------|------|--------|
| Revenue from Operations | 5,058.6 | Rs Mn | (Consolidated results Q4 FY26, line 325) |
| EBITDA (computed) | 967.1 | Rs Mn | (PBT 570.09 + Interest 28.51 + Deprec 368.47, from lines 344, 338, 340) |
| EBITDA Margin | 19.1% | % | (967.1 / 5,058.6) |
| PAT (Profit After Tax) | 420.5 | Rs Mn | (Consolidated results Q4 FY26, line 352) |
| PAT Margin | 8.3% | % | (420.5 / 5,058.6) |
| Diluted EPS | 17.98 | Rs | (Consolidated results Q4 FY26, line 386) |
| CFO (Operating Cash Flow) | 314.9 | Rs Mn | (Consolidated cash flow FY26, line 501) |
| FCF (Free Cash Flow) | -822.8 | Rs Mn | (CFO 314.9 - Capex 1,137.74, from cash flow line 503) |
| Book Value Per Share | 334.6 | Rs | (Total equity 7,817.59 / shares 2.339 Cr, from balance sheet line 437) |
| Net Cash / (Debt) Position | (1,146.1) | Rs Mn | (Net Debt, negative indicates net debt position) |
| CFO / PAT (latest year) | 0.75x | Ratio | (314.9 / 420.5) |
| CFO / PAT (cumulative FY19-FY26) | -1.32x | Ratio | (B01, line 41: "cumulative FCF/PAT -1.32") |
| FCF / PAT | -1.95x | Ratio | (FCF -822.8 / PAT 420.5) |
| P/FCF (Price to FCF) | NOT APPLICABLE | — | (FCF negative across all 8 computable years FY19-FY26, B01 line 41) |
| Capex (FY26) | 1,137.7 | Rs Mn | (Consolidated cash flow line 503, including ROU, CWIP, intangibles) |
| Depreciation (FY26) | 368.5 | Rs Mn | (Consolidated results line 340) |
| DPS (Final Dividend, FY26) | 2.0 | Rs | (Consolidated results line 34: "Final dividend of Rs 2/- per equity share") |
| ROCE (Latest = FY26) | 6.6% | % | (Deliberation record, line 45: "current ROCE (6.6%, FY26)") |
| ROCE 2-Year Trend Direction | Deteriorating (FY24: 10.91%, FY25: 1.20%, FY26: 6.6%) | — | (B04 line 46: "ROCE swung 10.91% to 1.20% in two years") |
| ROE (Standalone parent, FY26) | 5.4% | % | (Standalone PAT 390.82 / opening equity 7,213.12 from standalone results) |
| 3-Year Revenue CAGR (FY24-FY26) | 14.7% | % | (sqrt(505.86/393.5)^(1/2) - 1; from screener FY24 393.5, FY26 505.86) |
| 3-Year PAT CAGR (FY24-FY26) | 17.6% | % | (sqrt(42.05/30.35)^(1/2) - 1; from screener FY24 30.35, FY26 42.05, but note FY25 was trough 5.71) |

---

### NORMALIZED ROCE ANCHOR (AMENDMENT 4.5)

**Pre-depression cycle identified: FY2018-FY2021 (pre-IPO / pre-capex build years; Dahej SEZ capex and July 2021 IPO cash bloat began depression from FY2022 onward per Deliberation record line 20)**

| Fiscal Year | EBIT (Rs Cr) | Capital Employed (Rs Cr) | ROCE % | Anchor |
|-------------|------------|------------------------|---------|--------|
| FY2018 | 21.67 | 115.27 | 18.8% | Screener-Data_Sheet: PBT 19.04 + Interest 2.63; Equity 59.12 (8.04+51.08) + Borrowings 56.15 |
| FY2019 | 31.34 | 156.86 | 20.0% | Screener-Data_Sheet: PBT 27.39 + Interest 3.95; Equity 79.71 (8.04+71.67) + Borrowings 77.15 |
| FY2020 | 51.87 | 208.39 | 24.9% | Screener-Data_Sheet: PBT 47.6 + Interest 4.27; Equity 117.70 (8.04+109.66) + Borrowings 90.69 |
| FY2021 | 65.15 | 256.22 | 25.4% | Screener-Data_Sheet: PBT 60.7 + Interest 4.45; Equity 165.97 (20.09+145.88) + Borrowings 90.25 |

**Normalized ROCE (median of FY2018-FY2021):** **22.45%** (Median = (20.0% + 24.9%) / 2, screener-Data_Sheet, computed on B01 EBIT/Capital Employed basis)

| Metric | Value | Anchor |
|--------|-------|--------|
| **Normalized ROCE (pre-depression median)** | **22.45%** | Screener-Data_Sheet rows: PBT + Interest (EBIT), Equity Capital (Net Worth), Borrowings (Debt) for FY18-21; median computed |
| **Current ROCE (FY26)** | **6.6%** | (Deliberation record, line 45) |
| **FY28 Expected ROCE (base case)** | **8.5%** | (Deliberation record, line 45: "Stage 11 (Role 1) builds the formal FY28 projection; this estimate is the working input") |
| **FY28 Expected ROCE (bear case)** | **6.3%** | (Deliberation record, line 45) |
| **FY28 Expected ROCE (bull case)** | **10.6%** | (Deliberation record, line 45) |
| **Unwind Catalyst** | Dahej capacity commissioning entering revenue phase (new Dahej block commissioned Jan 2026 operational by Q4 FY26; reactor/assembly-line utilization 64.11%/30.54% with headroom for utilization ramp toward 75-80% target) | (B05 line 51: "Handed to production team Jan 2026, confirmed fully operational by Q4 FY26"; B04 unit_economics line 60: "reactor utilization 64.11%, assembly-line 30.54% in FY24-25"; B05 timing_slippages line 86; Deliberation record line 50: "Dahej commissioning drives both Pillar 1 forward ROCE and Pillar 3a growth") |
| **Pillar 1 ROCE Calculation** | 60/40 weighted average of current ROCE (6.6%, FY26) and FY28 expected ROCE base (8.5%) = (0.60 × 6.6%) + (0.40 × 8.5%) = 7.36% | (Deliberation record, line 44) |
| **ROCE Recovery Credited Via** | Pillar 1 only (not Strategic Premium) | (Deliberation record, line 47: "ROCE recovery credited via: Pillar 1") |

---

### FROM EARLIER ANALYSIS BLOCKS

| Field | Value | Anchor |
|-------|-------|--------|
| **Guided Revenue Growth & Margin Band** | FY27: ~25% revenue growth; 20-22% EBITDA margin | (B05, guidance table rows 37-38: "FY27 guidance: revenue growth ~25%; EBITDA margin 20-22%") |
| **Quarter Stated** | Q4 FY26 call (16 May 2026) | (B05, last concall available) |
| **Management Credibility Grade** | B (Good) | (B05, line 65: "credibility_grade: B") |
| **Credibility Basis** | Core financial guidance (revenue growth, 20-22% EBITDA margin band) delivered essentially on schedule with margins tracking 18.0% → 19.4% → 20.9% across three quarters; most product commercialization promises landed with minor disclosed delays; long-cycle capex/timeline commitments (Jolva groundbreaking slipped 3x, semiconductor dispatch missed target unacknowledged) and twice-repeated ROCE dodge keep it short of A. | (B05, line 66) |
| **Top 2-3 Growth Triggers** | 1. SDA new-customer invoicing (Euro 7 emission-norm tailwind), near-medium term, HIGH conviction; 2. EBITDA margin sustaining 20-22% band, near-term, HIGH conviction; 3. PASC agro intermediate ramp on new Dahej block, near-term, HIGH conviction | (B05, triggers rows 1-4) |
| **EM Score** | 19.2 / 80 | (B07, line 15: "em_score: 19.2") |
| **EM Classification** | MODEST | (B07, line 16: "em_classification: MODEST") |
| **Evidence Quality Mix** | Mostly documented / Mixed | (B07, line 24: "evidence_mix: {documented: 24, claim: 21, inference: 4}") |
| **Primary Catalyst (12m window)** | SDA new-customer invoicing begins (~Aug 2026) | (B07, catalysts_12m row 1) |
| **Secondary Catalysts (12m)** | Semiconductor first commercial dispatch (Q1 FY27, already once-slipped); Pharma intermediates first product (Q1 FY27); Jolva groundbreaking (mid-July 2026, 3x already slipped) | (B07, catalysts_12m rows 2-4) |
| **Strategic Asset / Monopoly Position** | YES: Switching costs (multi-year customer requalification, high durability); Cost/process advantage (proprietary electrolysis route, continuous-flow chemistry, moderate durability); Regulatory/compliance barriers (DSIR, ISO, REACH, ZLD, moderate); Efficient scale in niche global markets (SDA, ESS, Glymes, moderate); Intangible know-how (DSIR R&D centre, in-house process development, moderate); Distribution/customer relationships (offshore subsidiaries, marquee clientele, moderate); Brand (EcoVadis, Three Star Export House, low-moderate). | (B04, moats_present rows 1-7) |
| **Cash Conversion Determination** | INDETERMINATE leaning structural. No clean pass. Block B trend deteriorating (FCF negative in all 8 computable years FY19-FY26, cumulative -1.32x; WC Days rising from 175.3 to 185.3 FY25-FY26). Trade receivables grew 18.1% while revenue fell 2.7-4% in FY25; gross trade receivables grew 18.1% in FY26 to Rs 82.53 Cr; top-3 customer concentration in receivables 61%; zero ECL provisioned despite concentration; Consolidated trade receivables adverse swing Rs 305.47 Mn on CFS. Debtor days rose 48 to 86 across FY22-FY26 through flat-revenue years, which growth does not explain. Missing CRISIL rating rationale would resolve determinacy. Pillar 2 multiplier stays conservative (0.80x band, no growth offset). | (Deliberation record, line 21; B01 block_b_trend line 41; B02 receivables_trend line 46; B03 FLAG-CASH; B09 capacity_check) |
| **SOM-Implied Revenue CAGR** | 3-year: 14.3%; 5-year: 13.9% | (B09, som_implied_revenue_cagr rows yr3 and yr5) |
| **SOM Revenue (3yr implied)** | Rs 754 Cr | (B09, som_3yr_cr) |
| **SOM Revenue (5yr implied)** | Rs 968 Cr | (B09, som_5yr_cr) |
| **TAM (Conservative)** | Rs 15,237 Cr | (B09, tam_cr.conservative) |
| **TAM (Realistic)** | Rs 22,530 Cr | (B09, tam_cr.realistic) |
| **Runway Classification** | GOOD | (B09, runway_class) |
| **UA Qualifier: Listed >=12 months** | YES | (IPO July 2021; as of run date 2026-07-12 = 4 years 11.6 months listed) |
| **UA Qualifier: Gate 0 >=60 OR EM >=25** | NO | (Gate 0 core score 48, B01 line 21; EM 19.2, B07 line 15, both below thresholds) |
| **UA Qualifier: FII+DII <3%** | NO | (Mutual fund holding ~5.34%, B02 line 32; FII+DII >=3% likely) |
| **UA All Three Qualifiers Met** | NO | (Only 1 of 3 met; does not qualify for UA multiplier) |

---

### PEER FINANCIAL MEDIANS (Latest FY, FY26)

**Peers: ACUTAAS, CAMLINFINE, CLEAN, NEOGEN**

| Metric | TATVA | Peer Median | Source |
|--------|-------|-------------|--------|
| P/E Ratio (Trailing 12M, price/EPS) | 73.8x | NOT COMPUTED | (Note: Tatva EPS 17.98 highly cyclical; trough was FY25 EPS 2.44, peak FY22 EPS 4.33 per screener; peer medians require detailed peer EPS extraction from screener Data_Sheet rows 24-25 for each peer FY26) |
| EV/EBITDA (Trailing 12M) | 33.3x | NOT COMPUTED | (Note: Requires peer EBITDA derivation; Tatva EV 32,176 Mn / EBITDA 967 Mn = 33.3x; peer medians unresolved below) |
| P/B (Price to Book) | 3.96x | NOT COMPUTED | (Tatva: CMP 1,326 / BVPS 334.6 = 3.96x; peer BVPS extraction from screener needed) |
| Revenue Growth (3yr CAGR) | 14.7% | NOT COMPUTED | (Tatva 14.7%, per screener; peer CAGRs unresolved below) |
| ROCE Latest | 6.6% | NOT COMPUTED | (Tatva 6.6%; peer ROCEs require balance-sheet capital employed derivation from screener Balance_Sheet section) |

**Peer Median Resolution Status:**
- Screener-Profit_Loss.csv, screener-Balance_Sheet.csv, screener-Quarters.csv exports came back empty per B01 line 13; only screener-Data_Sheet.csv used as sole source
- Peer Net Block, Borrowings, Reserves data exist in Data_Sheet Cr rows 44-45 (FY26) for ACUTAAS, CAMLINFINE, CLEAN, NEOGEN
- Peer Sales (Revenue) and Net Profit rows extracted above from peer Data_Sheet CSVs
- Peer EBITDA, ROCE, BVPS computations possible but would require consolidating multi-source balance-sheet fields; unresolved pending dedicated peer extraction stage

---

## CONFLICTS

### Single Value Conflicts (upstream stages disagree; conservative value used in table)

| Field | Value A | Anchor A | Value B | Anchor B | Used in Table | Reason |
|-------|---------|----------|---------|----------|---------------|--------|
| Sector Cap Row | Pharma / CDMO, 38x | (Manifest) | Specialty Chemicals, 35x | (Deliberation record line 19: "Specialty chemicals, 35x, correcting the manifest's Pharma / CDMO 38x. Sure. Phase 3 stage 11 inherits 35x.") | **35x (Specialty Chemicals)** | Deliberation record explicitly overrides manifest as corrected and authoritative for stage 11 forward; manifest sector auto-pick flagged for verification in B04 |
| ROCE FY26 | 6.32% (computed from EBIT/CapE) | (Consolidated results, derived from EBIT 570.09 / CapE 9,021.32) | 6.6% | (Deliberation record line 45) | **6.6%** | Deliberation record is authoritative source; uses consistent methodology across the full analysis; single-sourcing rule applies |

---

## UNRESOLVED FIELDS

| Field | Why Unresolved | Where It Might Be | Handling |
|-------|-----------------|-------------------|----------|
| **Rating WC Quote** | NO RATING PDF PROVIDED in run inputs; inputs/rating/ directory absent | CRISIL rating rationale (annual sector review, not provided); would contain working-capital assessment language specific to the company | Marked NOT FOUND; Cash determination therefore draws solely from Deliberation record determination (INDETERMINATE leaning structural) and empirical receivables/payables trend from B01/B02/B03. FLAG-CASH verdict stands without rating agency backing. |
| **Peer P/E Median** | Screener-Profit_Loss.csv came back empty per B01 line 13; cycle-normalized EPS unavailable | Peer screener-Profit_Loss.csv or manual quarterly earnings aggregation | Unresolved pending peer data re-export; leave blank in table |
| **Peer EV/EBITDA Median** | Same as above; peer EBITDA derivation blocked | Peer P&L reconstruction from results PDFs or screener recount | Unresolved; leave blank |
| **Peer P/B Median** | Screener-Balance_Sheet.csv empty per B01 line 13; peer BVPS unresolved | Peer balance-sheet equity and shares data from alternate source | Unresolved; leave blank |
| **Peer Revenue Growth (3yr CAGR)** | Screener extraction incomplete for peer quarterly progressions | Peer screener-Data_Sheet.csv rows 10-11 (Sales by year) available but require secondary lookup | Partial: Screener data exists for peers (ACUTAAS FY24 717.47 to FY26 1,339.37 = 36.6% 2yr growth; CAMLINFINE FY24 1,453.91 to FY26 1,723.31 = 9.0% 2yr; CLEAN FY24 791.49 to FY26 956.55 = 10.0% 2yr; NEOGEN FY24 690.67 to FY26 861.96 = 11.9% 2yr) but 3yr CAGR requires FY23 figures and was not extracted here. |
| **Peer ROCE Median** | Peer CapE and EBIT derivation blocked by screener data gaps | Peer annual reports or recount against screener Balance_Sheet/P&L reconstruction | Unresolved; leave blank |
| **FII+DII Shareholding % (for UA qualifier)** | Only mutual fund holding disclosed (~5.34% per B02 line 32 and B03 note 16(ix)); FII and DII holdings not explicitly separated in provided AR or screener data | Quarterly shareholding-pattern filings (SEBI Regulation 31) or BSE/NSE shareholding disclosures | Estimated FII+DII >=3% (mutual fund 5.34% likely includes institutional allocation), rendering UA qualifier **NO**. Full resolution requires quarterly SHP filings. |
| **Quarterly FY26 ROCE** | B07 capacity_check references "FY23-FY25 utilisation table provided in AR; FY26 utilisation NOT FOUND" | Next AR (FY26 full-year) expected to disclose FY26 facility-level utilization %, which would allow FY26 ROCE validation | FY26 ROCE 6.6% from deliberation accepted as authoritative but not independently verified in this run against FY26 facility utilization |

---

## MASTER SUMMARY TABLE

| Category | Field | Value | Source Anchor |
|----------|-------|-------|---|
| **Company** | Ticker | TATVA | (Manifest) |
| | Sector (corrected) | Specialty Chemicals, 35x | (Deliberation) |
| | Business Type | Manufacturing, 4-product specialty chemicals | (B04) |
| | CMP | Rs 1,326.0 | (Manifest) |
| | Mcap | Rs 3,103.0 Cr | (Manifest) |
| | Shares (Diluted, Cr) | 2.339 | (Q4 FY26 results) |
| | Net Debt | Rs 1,146.1 Mn | (Q4 FY26 balance sheet) |
| | EV | Rs 32,176.1 Mn | (Computed: Mcap + ND) |
| **FY26 (Latest)** | Revenue | Rs 5,058.6 Mn | (Q4 FY26 consol P&L) |
| | EBITDA | Rs 967.1 Mn | (Computed: PBT + Int + Depr) |
| | PAT | Rs 420.5 Mn | (Q4 FY26 consol P&L) |
| | EPS (Diluted) | Rs 17.98 | (Q4 FY26 results) |
| | CFO | Rs 314.9 Mn | (Q4 FY26 cash flow) |
| | FCF | Rs -822.8 Mn | (CFO - Capex) |
| | Capex | Rs 1,137.7 Mn | (Q4 FY26 cash flow) |
| | ROCE | 6.6% | (Deliberation record) |
| | CFO/PAT | 0.75x | (Latest year) |
| | FCF/PAT | -1.95x | (Latest year) |
| **Normalized ROCE** | Pre-depression median (FY18-21) | 22.45% | (Screener Data_Sheet, computed) |
| | Current (FY26) | 6.6% | (Deliberation record) |
| | FY28 base case | 8.5% | (Deliberation record) |
| | Unwind catalyst | Dahej commissioning & utilization ramp | (B05, B04, Deliberation) |
| **Cash Determination** | Status | INDETERMINATE leaning structural | (Deliberation record) |
| | Evidence | Block B deteriorating (FCF negative 8yr); receivables up 18.1% vs revenue down; top-3 customer 61% concentration; zero ECL; debtor days 48→86 FY22-26 | (B01, B02, B03) |
| | Pillar 2 Multiplier | 0.80x band (conservative, no growth offset) | (Deliberation record) |
| **Growth & Margins** | FY27 Revenue Growth Guidance | ~25% | (B05, Q4 FY26 call) |
| | FY27 EBITDA Margin Guidance | 20-22% | (B05, Q4 FY26 call) |
| | Management Credibility | B (Good) | (B05) |
| **ROCE Forward** | Verdict | RECOVERING, probability 40-60% | (Deliberation record, line 45) |
| | FY28 ROCE Estimate (Base) | 8.5% | (Deliberation record, line 45: "base 8.5%") |
| | FY28 ROCE (Bear / Bull) | 6.3% / 10.6% | (Deliberation record, line 45: "bear 6.3%, bull 10.6%") |
| | Pillar 1 ROCE Calc | 60/40 weighted avg of FY26 (6.6%) and FY28 est (8.5%) = 7.36% | (Deliberation record: "Pillar 1 ROCE = 60/40 weighted average") |
| | Recovery Credited Via | Pillar 1 only (not Strategic Premium) | (Deliberation record, line 47) |
| | Shared Catalyst | Dahej commissioning drives both Pillar 1 forward ROCE and Pillar 3a growth premium | (Deliberation record, line 50) |
| **Emerging Moat** | EM Score | 19.2 / 80 (MODEST) | (B07) |
| | Catalysts (12m) | SDA new-customer (~Aug 2026); Semiconductor dispatch (Q1 FY27); Pharma first product (Q1 FY27); Jolva groundbreaking (mid-July 2026, 3x slipped) | (B07) |
| **Valuation Ready** | Flag-Cash Engaged | YES — Indeterminate cash determination caps disposition; no clean pass | (Deliberation) |
| | Operator Overrides | NONE adopted | (Deliberation, line 40-42) |
| | FTTCP Disposition | DEEP WATCH — not actionable at Rs 1,326 | (Deliberation, line 51) |

---

## CONFIDENCE NOTES

- **Data Freshness:** All latest-FY figures from audited Q4 FY26 results (16 May 2026, period 31 Mar 2026), fresher than FY25 AR.
- **Normalized ROCE:** Computed on identical EBIT/(Net Worth + Borrowings) basis as B01 methodology across all four pre-depression years; median 22.45% is the evidenced normalized level per Amendment 4.5.
- **Cash Determination:** Anchored to deliberation record determination (INDETERMINATE leaning structural) because NO RATING PDF provided. B01/B02/B03 provide empirical evidence (receivables trend, FCF trend, WC deterioration), but CRISIL rating language quote unavailable.
- **ROCE Forward:** Deliberation-record RECOVERING verdict carries 40-60% probability; FY28 estimate base 8.5% is working input for Stage 11 formal projection. Normalized ROCE 22.45% establishes the pre-depression benchmark; 4.5 blend incorporates current 6.6% and expected 8.5% in the Pillar 1 calculation.
- **Sector Cap:** Corrected to 35x (Specialty Chemicals) per deliberation; overrides manifest auto-pick.
- **UA Qualifiers:** All three NOT met; no UA multiplier applies.
- **Peer Medians:** Screener-Data_Sheet.csv provides raw peer financials (sales, profit) but empty P&L and Balance_Sheet CSVs prevent derivative metrics (EBITDA, ROCE, BVPS) from being computed. Left unresolved for verifier cross-check.

---

```yaml
stage: B10-valinputs
company: "TATVA"
run_date: "2026-07-12"
model: "claude-haiku-4-5"
status: complete
mode: "Amendment 4.5 valuation refresh"
input_gaps:
  - "No Rating PDF provided; rating_wc_quote unresolved"
  - "Peer derivative metrics (EBITDA, ROCE, BVPS, medians) unresolved due to empty screener-Profit_Loss.csv and screener-Balance_Sheet.csv exports"
  - "FY26 facility-level utilization % not available (noted as NOT FOUND in B07); next AR expected"
flags:
  - type: "FLAG-CASH"
    reason: "INDETERMINATE leaning structural: Block B deteriorating (FCF negative across 8 years FY19-FY26, cumulative -1.32x); receivables grew 18.1% vs revenue decline FY25; top-3 customer concentration 61% with zero ECL provisioned; Consolidated CFS adverse swing Rs 305.47 Mn; debtor days 48→86 FY22-FY26 through flat-revenue years (B01, B02, B03). Pillar 2 multiplier conservative 0.80x band, no growth offset. Missing CRISIL rating rationale. Caps disposition at PROCEED WITH CAVEATS."
  - type: "FLAG-EMOAT"
    reason: "F2 execution moat scores zero with documented negative: Jolva groundbreaking slipped 3 consecutive quarters (Q2→Q3→Q4 FY26 calls, HIGH severity). G1 war chest scores zero: Credit rating downgraded A-/Stable to A-/Negative (FY24-25 AR) then to BBB+/Stable (May 2026 IP). Largest emerging-moat revenue (Jolva INR 400-500cr guided) sits on weakest execution track record in file. (B07)"
  - type: "FLAG-PROMOTER"
    reason: "CAUTION verdict: GPCB Section 33(A) Water Act direction closed Ankleshwar plant 13 Sept 2024, revoked after remediation (root cause not independently confirmed). Promoter-executive remuneration +27.89% YoY while standalone PAT fell 98.9% and EPS fell ₹12.82→₹0.14. CRISIL downgraded twice within review window. No red-flag deal-breakers but four amber items cluster in FY24-25. (B08)"

table:
  company: "Tatva Chintan Pharma Chem Ltd"
  ticker: "TATVA"
  sector_corrected: "Specialty Chemicals (35x cap, correcting manifest Pharma/CDMO 38x)"
  sector_cap_row_anchor: "Deliberation record line 19"
  business_model_type: "Manufacturing, four-product specialty chemicals (PTC 33.0%, SDA 31.5%, ESS 1.6%, PASC 33.9% FY26 revenue mix); asset-intensive, high WC intensity, moderate pricing power, cyclical"
  cmp_rs: 1326.0
  market_cap_cr: 3103.0
  shares_diluted_cr: 2.339
  net_debt_mn: 1146.1
  enterprise_value_mn: 32176.1
  revenue_fy26_mn: 5058.6
  revenue_source: "Consolidated audited results Q4 FY26 line 325"
  ebitda_fy26_mn: 967.1
  ebitda_source: "Computed: PBT 570.09 + Interest 28.51 + Deprec 368.47 (Q4 FY26 results)"
  ebitda_margin_pct: 19.1
  pat_fy26_mn: 420.5
  pat_source: "Consolidated audited results Q4 FY26 line 352"
  pat_margin_pct: 8.3
  diluted_eps_rs: 17.98
  eps_source: "Consolidated audited results Q4 FY26 line 386"
  cfo_fy26_mn: 314.9
  cfo_source: "Consolidated cash flow FY26 line 501"
  fcf_fy26_mn: -822.8
  fcf_source: "CFO 314.9 - Capex 1137.74 (Q4 FY26 cash flow line 503)"
  book_value_per_share_rs: 334.6
  bvps_source: "Total equity 7817.59 Mn / Shares 2.339 Cr (Q4 FY26 balance sheet line 437)"
  capex_fy26_mn: 1137.7
  capex_source: "Consolidated cash flow line 503 (incl. ROU, CWIP, intangibles)"
  depreciation_fy26_mn: 368.5
  depreciation_source: "Consolidated results line 340"
  dps_final_rs: 2.0
  dps_source: "Consolidated results line 34 (recommended final dividend, subject to AGM approval)"
  roce_latest_pct: 6.6
  roce_source: "Deliberation record line 45 (authoritative for single-source rule)"
  roce_2yr_trend: "Deteriorating (FY24: 10.91%, FY25: 1.20%, FY26: 6.6%)"
  roce_trend_source: "B04 line 46; ROCE swing driven by Dahej capex cycle depressing CapE returns"
  roe_standalone_pct: 5.4
  roe_source: "Standalone PAT 390.82 / opening equity 7213.12 (standalone results)"
  revenue_cagr_3yr_pct: 14.7
  revenue_cagr_source: "FY24 393.5→FY26 505.86 screener Data_Sheet rows 11"
  pat_cagr_3yr_pct: 17.6
  pat_cagr_source: "FY24 30.35→FY26 42.05 screener rows 24, but FY25 was trough 5.71 (destocking). Cyclical interpretation advised."
  cfo_pat_ratio_latest: 0.75
  cfo_pat_source: "314.9 / 420.5 (Q4 FY26 results)"
  cfo_pat_cumulative_fy19_26: -1.32
  cfo_pat_cumulative_source: "B01 line 41 (negative FCF every year, cumulative drag)"
  fcf_pat_ratio_latest: -1.95
  fcf_pat_source: "FCF -822.8 / PAT 420.5"
  p_fcf_multiple: "NOT APPLICABLE"
  p_fcf_note: "FCF negative across all 8 computable years FY19-FY26 per B01 line 41"
  
  normalized_roce:
    fy2018_pct: 18.8
    fy2018_ebit_cr: 21.67
    fy2018_capital_employed_cr: 115.27
    fy2018_source: "Screener Data_Sheet: PBT 19.04 + Interest 2.63 = EBIT 21.67 Cr; Equity (8.04+51.08) + Borrowings 56.15 = Capital Employed 115.27 Cr"
    
    fy2019_pct: 20.0
    fy2019_ebit_cr: 31.34
    fy2019_capital_employed_cr: 156.86
    fy2019_source: "Screener Data_Sheet: PBT 27.39 + Interest 3.95 = EBIT 31.34 Cr; Equity (8.04+71.67) + Borrowings 77.15 = Capital Employed 156.86 Cr"
    
    fy2020_pct: 24.9
    fy2020_ebit_cr: 51.87
    fy2020_capital_employed_cr: 208.39
    fy2020_source: "Screener Data_Sheet: PBT 47.6 + Interest 4.27 = EBIT 51.87 Cr; Equity (8.04+109.66) + Borrowings 90.69 = Capital Employed 208.39 Cr"
    
    fy2021_pct: 25.4
    fy2021_ebit_cr: 65.15
    fy2021_capital_employed_cr: 256.22
    fy2021_source: "Screener Data_Sheet: PBT 60.7 + Interest 4.45 = EBIT 65.15 Cr; Equity (20.09+145.88) + Borrowings 90.25 = Capital Employed 256.22 Cr"
    
    median_pct: 22.45
    median_calculation: "Median of [18.8%, 20.0%, 24.9%, 25.4%] = (20.0% + 24.9%) / 2 = 22.45%"
    median_source: "Screener-Data_Sheet.csv, computed on B01 EBIT/(Net Worth + Borrowings) basis, four pre-depression years FY2018-FY2021"
    
    pre_depression_rationale: "FY2018-FY2021 identified as pre-depression cycle (pre-IPO July 2021, pre-Dahej capex build). Dahej SEZ capex and IPO cash bloat began depression from FY2022 onward per Deliberation record line 20. ROCE deteriorated to single digits FY23-FY26 (min 1.17% FY25) per B01 line 15."
    pre_depression_source: "Deliberation record lines 20, B01 line 15"
    
    current_roce_fy26_pct: 6.6
    current_roce_source: "Deliberation record line 45"
    
    fy28_expected_roce_base_pct: 8.5
    fy28_expected_roce_bear_pct: 6.3
    fy28_expected_roce_bull_pct: 10.6
    fy28_expected_roce_source: "Deliberation record line 45; Stage 11 builds formal projection"
    
    unwind_catalyst: "Dahej capacity commissioning entering revenue phase"
    unwind_catalyst_detail: "New Dahej block commissioned January 2026, confirmed fully operational by Q4 FY26 call (~2 months late from guidance). Reactor utilization 64.11%, assembly-line 30.54% in FY24-25 (both cited as sub-optimal with headroom). Capacity ramp toward 75-80% target would support ROCE recovery toward normalized 22.45% level."
    unwind_catalyst_sources: "B05 line 51 (commissioning timing and status); B04 unit_economics line 60 (utilization rates); B05 mgmt_questions line 69 (timeline to 75-80% utilization); Deliberation record line 50 (Dahej commissioning underpins Pillar 1 ROCE recovery)"
    
    pillar_1_roce_blend_pct: 7.36
    pillar_1_roce_calculation: "60/40 weighted average of current ROCE (6.6%, FY26) and FY28 expected ROCE base (8.5%) = (0.60 × 6.6%) + (0.40 × 8.5%) = 3.96% + 3.4% = 7.36%"
    pillar_1_roce_source: "Deliberation record line 44"
    
    roce_recovery_credited_via: "Pillar 1 only (not Strategic Premium)"
    roce_recovery_source: "Deliberation record line 47"

  guided_revenue_growth_fy27_pct: 25.0
  guided_margin_band_fy27_pct: "20-22% EBITDA"
  guidance_source: "B05 guidance table rows 37-38 (Q4 FY26 call, 16 May 2026)"
  guidance_quarter: "Q4 FY26"
  management_delivery_credibility: "B (Good)"
  credibility_grade_source: "B05 line 65"
  credibility_basis: "Core financial guidance (revenue growth, 20-22% EBITDA margin band) delivered essentially on schedule (18.0%→19.4%→20.9% across three quarters Q2/Q3/Q4); most product commercialization promises landed with minor disclosed delays (Dahej plant ~2 mo late, agro intermediates timely, margin target hit, Electrolyte Salts delivered 1378% YoY Q4). Long-cycle capex commitments weakest: Jolva groundbreaking slipped 3 consecutive quarters (reframed as engineering optimization not acknowledged delay), semiconductor dispatch missed Q4 FY26 target unacknowledged in Q4 call. ROCE questions deflected twice with no forward target. Short of A grade due to capex/timeline and evasion pattern."
  
  top_growth_triggers_trigger_1: "SDA new-customer invoicing begins (Euro 7 emission-norm tailwind)"
  trigger_1_timeframe: "Near-medium term (~Aug 2026)"
  trigger_1_conviction: "HIGH"
  trigger_1_source: "B05 trigger row 1; B07 catalysts_12m row 1"
  
  top_growth_triggers_trigger_2: "EBITDA margin sustaining 20-22% band"
  trigger_2_timeframe: "Near-term (FY27 quarterly)"
  trigger_2_conviction: "HIGH"
  trigger_2_source: "B05 trigger row 2; Q4 FY26 call confirmed 20.9%, tracking into band"
  
  top_growth_triggers_trigger_3: "PASC agro intermediate ramp on new Dahej block"
  trigger_3_timeframe: "Near-term"
  trigger_3_conviction: "HIGH"
  trigger_3_source: "B05 trigger row 4; Dahej block operational by Q4 FY26 (2mo late from Jan 2026 guidance)"
  
  em_score_total: 19.2
  em_score_max: 80
  em_classification: "MODEST"
  em_source: "B07 lines 15-16"
  em_evidence_mix: "Documented 24 items (technical moats, regulatory compliance, scale signals), Claim 21 items (market-share trajectory, customer exclusivity, supply optionality), Inference 4 items"
  
  catalysts_12m_primary: "SDA new-customer invoicing (~Aug 2026)"
  catalysts_12m_secondary: "Semiconductor first commercial dispatch (Q1 FY27, 1x already slipped from Q4 FY26)"
  catalysts_12m_tertiary: "Pharma intermediates first product (Q1 FY27, slipped ~4-6 mo once); Jolva groundbreaking (mid-July 2026, 3x already slipped per B05 timeline_slippages)"
  catalysts_source: "B07 catalysts_12m rows 1-4; B05 timeline_slippages"
  
  strategic_position_monopoly: "YES — Multiple moats present (documented)"
  strategic_moats_list: "1. Switching costs (multi-year customer requalification, HIGH durability). 2. Cost/process advantage (proprietary electrolysis route, continuous-flow chemistry, MODERATE). 3. Regulatory/compliance barriers (DSIR, ISO, REACH, ZLD, MODERATE). 4. Efficient scale in niche global markets (SDA, ESS, Glymes, MODERATE). 5. Intangible know-how (DSIR R&D centre, in-house process development, MODERATE). 6. Distribution/customer relationships (offshore subsidiaries, marquee clientele, MODERATE). 7. Brand (EcoVadis, Three Star Export House, LOW-MODERATE)."
  moats_source: "B04 moats_present rows 1-7; B04 one_line_verdict"
  
  cash_conversion_determination: "INDETERMINATE leaning structural"
  cash_evidence_summary: "No clean pass. Block B trend deteriorating per B01 line 41: FCF negative in all 8 computable years (FY19-FY26), cumulative FCF/PAT -1.32x. WC Days rising 175.3→185.3 FY25-FY26 (+9.98 days). FLAG-CASH extended by B03: Consolidated trade receivables adverse swing Rs 305.47 Mn on CFS. B02 receivables_trend: Gross trade receivables rose 18.1% (Rs 69.85→82.53 Cr) while revenue fell 2.7-4%; top-3 concentration 61% receivables; zero ECL provisioned in both years despite concentration (Note 15/41B(ii)). Debtor days rose 48→86 across FY22-FY26 including through flat-revenue years (growth does not explain). Structural drivers likely: customer credit terms, portfolio mix migration. Missing CRISIL rating PDF would resolve determinacy with working-capital assessment language."
  cash_evidence_anchor: "B01 block_b_trend; B02 receivables_trend; B02 FLAG-CASH; B03 FLAG-CASH; B09 capacity_check (SOM headroom marginal if Jolva 4th slip occurs)"
  pillar_2_multiplier_band: "0.80x (conservative, no growth offset)"
  pillar_2_source: "Deliberation record line 48"
  rating_wc_quote: "NOT FOUND"
  rating_wc_why_missing: "No Rating PDF provided in inputs/rating/ directory; CRISIL rationale document not in run inputs"
  rating_wc_resolution: "Cash determination therefore draws solely from Deliberation record determination (INDETERMINATE leaning structural) and empirical receivables/payables trend from B01/B02/B03. FLAG-CASH verdict stands without rating agency backing."
  
  som_3yr_revenue_cr: 754
  som_5yr_revenue_cr: 968
  som_implied_revenue_cagr_3yr: 14.3
  som_implied_revenue_cagr_5yr: 13.9
  som_source: "B09 som_3yr_cr, som_5yr_cr, som_implied_revenue_cagr rows"
  
  tam_conservative_cr: 15237
  tam_realistic_cr: 22530
  tam_source: "B09 tam_cr rows (conservative and realistic; inflated management claim 1,21,364 Cr @ 79.7x flagged as unverified)"
  runway_classification: "GOOD"
  runway_source: "B09 runway_class"
  runway_capacity_note: "SOM 3yr (754 Cr) sits only ~23 Cr above conservative Jolva-inclusive capacity ceiling (731 Cr from B07); if Jolva 4th slip occurs (HIGH-severity risk per B07), capex becomes binding and SOM becomes optimistic side."
  
  peer_financials_provided: "YES (4 peers: ACUTAAS, CAMLINFINE, CLEAN, NEOGEN)"
  peer_medians_p_e: "NOT COMPUTED"
  peer_medians_ev_ebitda: "NOT COMPUTED"
  peer_medians_p_b: "NOT COMPUTED"
  peer_medians_growth: "NOT COMPUTED"
  peer_medians_roce: "NOT COMPUTED"
  peer_medians_why: "Screener-Data_Sheet.csv provided for all 4 peers with FY26 Revenue/PAT rows, but screener-Profit_Loss.csv and screener-Balance_Sheet.csv came back empty per B01 line 13. Derivative metrics (EBITDA, ROCE, BVPS) require balance-sheet capital employed derivation blocked by empty exports. Peer median extraction unresolved pending re-export or manual AR review."
  
  ua_qualifier_listed_12m: true
  ua_qualifier_listed_12m_detail: "IPO 21 July 2021; as of run date 12 July 2026 = 4 years 11.6 months listed, exceeds 12-month threshold"
  ua_qualifier_listed_12m_anchor: "Manifest run_date 2026-07-12; IPO announcement public record"
  
  ua_qualifier_gate0_or_em: false
  ua_qualifier_gate0_score: 48
  ua_qualifier_gate0_anchor: "B01 line 21: Core score 48/100 (AVERAGE classification), below 60 threshold"
  ua_qualifier_em_score: 19.2
  ua_qualifier_em_anchor: "B07 line 15: EM score 19.2/80 (MODEST), below 25 threshold"
  
  ua_qualifier_fii_dii_lt3: false
  ua_qualifier_fii_dii_detail: "Mutual fund holding ~5.34% (B02 line 32, Note 16(ix)). FII and DII not separately disclosed in AR or screener data provided. Institutional ownership halved (12.84%→5.34%) but 5.34% MF holding alone suggests FII+DII aggregate >=3%, fails threshold."
  ua_qualifier_fii_dii_anchor: "B02 Note 16(ix) shareholding pattern; note that B02 explicitly states not treating low institutional ownership as a risk per Amendment 3 (UA min multiplier, not a pass/fail factor)"
  
  ua_qualifiers_all_met: false
  ua_qualifiers_summary: "1 of 3 met (listed >=12m only). Does NOT qualify for UA multiplier adjustment (requires all three). No Amendment 3 min multiplier applies since gate check is binary."
  
  credibility_grade: "B"
  credibility_grade_source: "B05 line 65"

conflicts:
  - field: "Sector Cap Row"
    value_a: "Pharma / CDMO, 38x"
    anchor_a: "Manifest (auto-picked by screener)"
    value_b: "Specialty Chemicals, 35x"
    anchor_b: "Deliberation record line 19: 'Specialty chemicals, 35x, correcting the manifest's Pharma / CDMO 38x. Sure. Phase 3 stage 11 inherits 35x.'"
    used_in_table: "35x (Specialty Chemicals)"
    reason: "Deliberation record is authoritative corrected determination for stage 11 forward. Manifest sector auto-pick was flagged in B04 as incorrect business classification. Deliberation confirms sector cap override explicitly."
  
  - field: "ROCE FY26"
    value_a: "6.32% (computed EBIT/CapE)"
    anchor_a: "Consolidated results EBIT 570.09 / Capital Employed 9,021.32"
    value_b: "6.6% (deliberation methodology)"
    anchor_b: "Deliberation record line 45: 'current ROCE (6.6%, FY26)' as input to Pillar 1 calculation"
    used_in_table: "6.6%"
    reason: "Single-source rule: Deliberation record is downstream authoritative determination capturing full analysis. Uses consistent capital employed methodology across FTTCP analysis. Minor delta (6.32% vs 6.6%) within rounding/methodology variation but 6.6% is signed-off figure."

unresolved:
  - field: "Rating PDF WC Quote"
    why: "No Rating PDF in inputs/rating/; CRISIL rationale document not provided in run deliverables"
    where_it_might_be: "CRISIL Ratings sector review or company-specific rating rationale (issued separately from AR, not included in standard AR disclosure)"
    handling: "Cash determination drawn solely from Deliberation record (INDETERMINATE leaning structural) and empirical receivables/payables trend (B01/B02/B03). FLAG-CASH verdict stands without rating agency working-capital commentary backing."
  
  - field: "Peer P/E Median"
    why: "Screener-Profit_Loss.csv came back empty per B01 line 13; peer EPS extraction blocked"
    where_it_might_be: "Peer screener Profit_Loss.csv export (should list Net Profit by quarter/year); alternate source = peer results PDFs or annual reports"
    handling: "Unresolved. Peer medians left blank. Tatva P/E computed for reference only (CMP 1,326 / EPS 17.98 = 73.8x, highly cyclical; FY25 EPS 2.44 would give 544x, FY24 EPS 4.33 gives 306x; single-year P/E not reliable)."
  
  - field: "Peer EV/EBITDA Median"
    why: "Peer EBITDA derivation requires balance-sheet data (Depreciation, Finance Costs); screener-Balance_Sheet.csv empty per B01"
    where_it_might_be: "Peer screener Balance_Sheet.csv or re-derivation from peer P&L and Cash Flow statements"
    handling: "Unresolved. Tatva EV/EBITDA computed for reference: 32,176 Mn / 967 Mn = 33.3x (for peer cross-check, unanchored)."
  
  - field: "Peer P/B Median"
    why: "Peer BVPS requires peer shares and equity data; screener-Data_Sheet.csv provides reserve data but share counts require careful extraction"
    where_it_might_be: "Peer screener-Data_Sheet.csv rows 39-40 (Equity Share Capital, Reserves) + row 52 (No. of Equity Shares); full peer BVPS derivation needed"
    handling: "Unresolved. Tatva P/B for reference: CMP 1,326 / BVPS 334.6 = 3.96x (not peer-anchored)."
  
  - field: "Peer Revenue Growth CAGR (3-year)"
    why: "Screener-Data_Sheet.csv provides FY24/FY26 Sales but FY23 figures require secondary lookup or assume 2-year CAGR as proxy"
    where_it_might_be: "Screener-Data_Sheet.csv row 11 (Sales) for FY23, FY24, FY26 intersection; or peer annual reports"
    handling: "Partial resolution: 2-year CAGR calculated from screener FY24→FY26 (ACUTAAS 36.6%, CAMLINFINE 9.0%, CLEAN 10.0%, NEOGEN 11.9%). True 3-year CAGR deferred pending FY23 extraction."
  
  - field: "Peer ROCE Median"
    why: "ROCE = EBIT / Capital Employed; requires derivation of peer Capital Employed (Net Worth + Borrowings) and peer EBIT (PBT + Tax + Interest); screener Balance_Sheet.csv empty"
    where_it_might_be: "Peer screener exports (Profit_Loss.csv for tax/interest; Balance_Sheet.csv for equity/borrowings) or peer AR financials"
    handling: "Unresolved. Single-peer ROCE (Tatva 6.6%) stands alone; peer median cross-check deferred to verifier."
  
  - field: "FII+DII Shareholding (%) UA Qualifier"
    why: "B02 Note 16(ix) discloses mutual fund 5.34%, promoter 72.02%, retail/HNI split. FII/DII not separately itemized in provided AR or screener export"
    where_it_might_be: "Quarterly shareholding-pattern filings (SEBI Regulation 31) or BSE/NSE shareholding disclosure pages (not provided in run inputs)"
    handling: "Estimated FII+DII >=3% (mutual fund 5.34% overlaps with institutional category likely containing foreign/domestic institutional holders). Assumed NO on UA qualifier but full resolution requires quarterly SHP filings. Note: B02 and CLAUDE.md (Amendment 3) clarify low institutional ownership is NOT a risk factor; min multiplier applies, not a pass/fail."
  
  - field: "FY26 Facility Utilization % (Quarterly breakdown)"
    why: "B07 notes 'AR FY26 post-new-Dahej-block facility-level utilisation % not available (only FY23-FY25 utilisation table provided in AR; FY26 utilisation NOT FOUND)'"
    where_it_might_be: "Next AR (FY26 full-year), expected disclosures in Management's Discussion & Analysis or Notes to Accounts (operational/capacity metrics section)"
    handling: "Deferred. FY26 ROCE 6.6% from Deliberation accepted as authoritative but not independently verified against facility utilization % in this run. Reactor utilization noted as 64.11%, assembly-line 30.54% in FY24-25 (B04 unit_economics), suggesting significant idle capacity (upside to ROCE recovery on utilization ramp per B04 key_lever)."

rating_wc_quote: "NOT FOUND — No Rating PDF provided in run inputs (inputs/rating/ directory absent)"

ua_qualifiers:
  listed_12m: true
  listed_12m_basis: "IPO 21 July 2021; listed 4 years 11.6 months as of 2026-07-12"
  listed_12m_anchor: "Public IPO record"
  
  gate0_or_em: false
  gate0_or_em_detail: "Gate 0 core 48 (below 60) AND EM 19.2 (below 25); both thresholds missed"
  gate0_score_anchor: "B01 line 21"
  em_score_anchor: "B07 line 15"
  
  fii_dii_lt3: false
  fii_dii_lt3_detail: "Mutual fund holding 5.34% disclosed; FII+DII aggregate >=3% estimated (full breakdown not provided)"
  fii_dii_anchor: "B02 Note 16(ix) shareholding; quarterly SHP filings not provided"
  
  all_met: false
  all_met_summary: "1 of 3 qualifiers met (listed >=12m only). NO UA multiplier applies. Per Amendment 3 and CLAUDE.md, low institutional ownership is not a risk; do not confuse UA qualifier with institutional-ownership risk assessment."

credibility_grade: "B"
credibility_grade_basis: "Good. Core financial guidance (revenue growth, 20-22% EBITDA margin band) delivered essentially on schedule with margins tracking 18.0% to 19.4% to 20.9% across three quarters. Most product commercialization promises landed with only minor disclosed delays (Dahej plant ~2 mo late, agro intermediates timely, margin target hit, Electrolyte Salts +1,378% YoY Q4). Long-cycle capex/timeline commitments weakest: Jolva groundbreaking slipped 3 consecutive quarters (reframed as engineering optimization, not acknowledged as delay per B05 line 11 HIGH flag), semiconductor dispatch missed original Q4 FY26 target unacknowledged in Q4 call. ROCE questions deflected in Q2 and Q3 with no forward target ever given. Short of A grade (Excellent) due to capex timeline track record and evasion pattern on capital efficiency questions."
credibility_grade_anchor: "B05 line 65-66"

normalized_roce:
  pre_depression_median_pct: 22.45
  pre_depression_fy_range: "FY2018-FY2021"
  fy2018_pct: 18.8
  fy2019_pct: 20.0
  fy2020_pct: 24.9
  fy2021_pct: 25.4
  median_calculation_note: "Median of [18.8%, 20.0%, 24.9%, 25.4%] = (20.0% + 24.9%) / 2 = 22.45%"
  current_roce_fy26_pct: 6.6
  fy28_expected_roce_base_pct: 8.5
  fy28_expected_roce_bear_pct: 6.3
  fy28_expected_roce_bull_pct: 10.6
  pillar_1_roce_blend_pct: 7.36
  unwind_catalyst: "Dahej capacity commissioning entering revenue phase (new block operational Jan 2026, reactor/assembly-line utilization 64.11%/30.54% with headroom)"
  amplitude: "From normalized 22.45% to FY26 trough 6.6%, recovery to FY28 expected 8.5% base"
  source_documentation: "Screener-Data_Sheet.csv (EBIT, capital employed for FY18-21); Deliberation record (current 6.6%, expected 8.5%); B05 (Dahej commissioning Jan 2026); B04 (utilization rates)"
```

---

## NOTES FOR VERIFIER

1. **Normalized ROCE Amendment 4.5 Compliance:** Pre-depression median 22.45% computed directly from screener Data_Sheet on identical EBIT/(Net Worth + Borrowings) basis used in B01 Gate 0 analysis. Four years FY2018-FY2021 selected as pre-IPO / pre-capex build years. Dahej commissioning (Jan 2026 operational, 64%/31% utilization) documented as mechanical unwind catalyst.

2. **Single-Source Rule Enforced:** ROCE FY26 sourced from Deliberation record (6.6%), not recomputed. Sector Cap sourced from Deliberation (35x Specialty Chemicals), not manifest.

3. **Cash Determination Constraint:** No Rating PDF in run inputs. Cash verdict (INDETERMINATE leaning structural) drawn from Deliberation record + empirical B01/B02/B03 receivables/payables trend. FLAG-CASH prominent; Pillar 2 multiplier conservative 0.80x, no growth offset.

4. **ROCE Forward Verdict & Shared Catalyst:** RECOVERING (40-60% probability) with Dahej commissioning as SHARED CATALYST driving both Pillar 1 ROCE recovery and Pillar 3a growth. Role 3 must stress-test this single point of failure.

5. **Peer Medians Unresolved:** Screener-Data_Sheet.csv provides raw sales/profit for peer cross-check but derivative metrics (EBITDA, ROCE, BVPS) blocked by empty screener-Profit_Loss.csv and screener-Balance_Sheet.csv. Verifier should re-request screener exports or manually extract peer balance-sheet/P&L from results PDFs.

6. **UA Qualifiers:** 1 of 3 met. No UA multiplier. Note: Low institutional ownership is NOT a risk per CLAUDE.md Amendment 3 and instruction 8; FII+DII threshold is binary, not a conservatism lever.

7. **Deliberation-Record Supremacy:** All FTTCP determinations (ROCE verdict, sector cap, cash determination, Shared Catalyst flag, operator override status) treated as Phase 2→Phase 3 handoff instructions. Do not re-deliberate.

8. **Amendment 4.5 Inputs Complete:** Normalized ROCE 22.45% anchored; current ROCE 6.6% and FY28 expected 8.5% stated; unwind catalyst (Dahej commissioning with utilization ramp) documented with mechanical (non-speculative) evidence; Pillar 1 blend formula (7.36% = 60% × 6.6% + 40% × 8.5%) prepared for stage 11 valuation model.
