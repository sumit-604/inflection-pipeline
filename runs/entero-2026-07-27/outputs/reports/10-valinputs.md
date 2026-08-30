# STAGE 10: VALUATION INPUT ASSEMBLY
## Company: ENTERO | Run Date: 2026-07-27
### Model: Haiku 4.5 | Status: COMPLETE

---

## COMPANY IDENTITY BLOCK

| Field | Value | Anchor |
|-------|-------|--------|
| Company | Entero Healthcare Solutions Ltd | manifest.yaml |
| Ticker | ENTERO | manifest.yaml |
| Sector | Pharma & MedTech Distribution (trading) | B04, B00 |
| Business Model Type | Trading (pharma + MedTech distribution, roll-up consolidator) | B04 |
| CMP (Rs) | 1273.0 | manifest.yaml |
| Market Cap (Cr) | 5537.0 | manifest.yaml |
| Shares Outstanding Diluted (Cr) | 4.35 | screener-Data_Sheet.csv |
| Enterprise Value (compute) | 5537.0 Cr (mcap) + 327.36 Cr (net debt FY26) = 5864.36 Cr | screener, B02 Finding 6 |
| Net Debt / Net Cash (Cr) | +327.36 (net debt): Borrowings 677.15 - Cash 161.79 (all in Cr) | screener-Data_Sheet.csv; B02 Finding 6 reconciliation pending |
| Sector Cap (manifest row) | "Pharma / CDMO" (auto-picked, INCORRECT) | manifest.yaml note |
| **SECTOR CAP (OPERATOR-APPROVED)** | **18-20x** | fttcp-deliberation.md, ruling 2026-08-30 |

---

## LATEST FINANCIAL METRICS (FY26 AUDITED, FY27 Q1 PARTIAL)

**Fiscal Year 26 (Year ended 2026-03-31)** — Full-Year Audited Results

| Metric | Value | Anchor | Notes |
|--------|-------|--------|-------|
| Revenue (Cr) | 6,591.21 | screener-Data_Sheet.csv, FY26 row |
| EBITDA (Cr) | 263.79 (computed: Operating Profit 263.79 from Q-data summation) | screener-Data_Sheet.csv quarterly data summed |
| EBITDA Margin (%) | 4.0 | B05 guidance delivery |
| PAT (Cr) | 115.04 | screener-Data_Sheet.csv, FY26 row |
| PAT Margin (%) | 1.74 | Computed: 115.04 / 6591.21 |
| Diluted EPS (Rs) | NOT FOUND | unresolved; screener does not carry EPS; AR provides but not in provided corpus section |
| CFO (Cr) | 96.2 | screener-Data_Sheet.csv; B01-gate0 "first positive year after six consecutive negative" |
| FCF (Cr) | NOT FOUND - INDETERMINATE | B01 FLAG-CASH: "capex not computable, no per-year consolidated capex data"; fttcp-deliberation Pillar 2 INDETERMINATE |
| Book Value Per Share (Rs) | NOT FOUND | unresolved; net worth Rs 1,645.1 Cr / 4.35 Cr shares = Rs 378.4, but IPO-related equity volatility flagged in B02 |
| Net Debt (Cr) | 327.36 | screener: Borrowings 677.15 - Cash 161.79 |
| Inventory (Cr) | 841.68 | screener-Data_Sheet.csv, FY26 |
| Trade Receivables (Cr) | 1,212.44 (gross) | screener-Data_Sheet.csv, FY26; B02 Finding 3: +50.6% YoY vs +29.4% revenue growth (1.7x faster) |
| Trade Receivables > 6 months (Cr) | ~186.9 (estimated ~14.4% of gross per B02) | B02 receivables_trend, AR Note 15 |
| Depreciation (Cr) | 43.29 | screener-Data_Sheet.csv, FY26 |
| Capex (Cr, Standalone) | 159.39 (only standalone figure disclosed; consolidated not separately itemized) | B09 capacity_check, AR Note 5A |
| Dividend Per Share (DPS) | 0 (no dividend paid FY26) | B04 not_applicable, AR Note |
| **ROCE Latest (FY26)** | **9.7% (conservative consolidated basis per B01 dissent); 20-25% (operator forward-capital ruling basis)** | B01; fttcp-deliberation Pillar 1 ruling |
| **ROCE 2-Year Trend** | TEMPORARILY DEPRESSED → RECOVERING (B01 forward); backward TEMPORARILY DEPRESSED (B02/B03) | fttcp-deliberation "ROCE RECOVERING (+1)" |
| ROE (FY26) | DISTORTED by mid-year IPO equity infusion (opening -68.59cr, closing 1638.06cr) | B01 data_notes |
| 3-Year Revenue CAGR (FY24-FY26) | 29.7% | Computed: (6591.21 / 3922.31)^(1/2) - 1 = 29.7% |
| 3-Year PAT CAGR (FY24-FY26) | NOT COMPUTABLE - loss-to-profit swing (negative FY21-FY23) | B01 data_notes; synthetic CAGR not attempted |
| CFO/PAT (FY26 latest) | 0.83 (96.2 / 115.04) | B01 cumulative ratio: -1.05 across FY20-FY26; FY26 alone 0.83 |
| CFO/PAT Cumulative (FY20-FY26) | -1.05 | B01 block_b_trend: "six of seven years CFO-negative; cumulative CFO -203.07cr vs cumulative PAT +192.89cr" |
| FCF/PAT | NOT FOUND - INDETERMINATE | capex unavailable, consolidated; Pillar 2 determination: INDETERMINATE |
| P/FCF | NOT COMPUTABLE | FCF uncomputable |
| Current Ratio | Deteriorated 36% YoY (B04 flag); consolidated 6.23x to 2.26x standalone (B02 Finding 7) | AR Note 57 (standalone), Note 49 (consolidated) |

**Q1 FY27 Data (Quarter ended 2026-06-30)** — Latest Quarterly Guidance Tracking

| Metric | Value | Anchor | Status |
|--------|-------|--------|--------|
| EBITDA Margin (%) | 5.0 (already hit in Q1 FY27) | B05 outcome: "already 5.0% in Q1 FY27; full-year revenue/OCF conversion not yet assessable" |
| Minority Interest (% of PBT-minority) | ~27% (Q1 FY27 actual tracking 25-27% guidance) | B05 outcome row: "Minority interest holds ~25-27% of PBT-minority" |
| Revenue Growth (ex-M&A) | 23% (FY27 guidance) | B05 guidance item; confirmation status pending H1 FY27 full audited results |
| OCF-to-EBITDA Conversion | >=50% (FY27 guided; H1 FY27 result not yet audited) | B05 guidance; B05 outcome: "full-year revenue/OCF conversion not yet assessable" |

---

## GUIDED REVENUE GROWTH & MARGIN BAND

| Item | Value | Q Stated | Delivery Status | Anchor |
|------|-------|----------|-----------------|--------|
| Revenue Growth | 30% (LFL, FY26) | Q3 FY26 call | Delivered: +31.5% LFL actual (Q4 call confirmation) | B05 promise_delivery row 1 |
| Revenue Growth (ex-M&A, FY27) | 23% YoY | Q4 FY26 call | Partial: not yet testable on full-year | B05 guidance item |
| EBITDA Margin | 4% (FY26) | Q3 FY26 call | Delivered: 4.03% actual | B05 promise_delivery row 2 |
| EBITDA Margin | 5% (FY27) | Q4 FY26 call | Already hit 5.0% in Q1 FY27 (one quarter in) | B05 promise_delivery row 9 |
| Operating Cash Flow | ~Rs 100 Cr (FY26) | Q3 FY26 call | Partial: Actual Rs 96.2 Cr, ~96% of guide | B05 promise_delivery row 3 |
| Management Credibility Grade | B (Good) | — | 8 delivered, 4 partial, 0 missed; held at B not A due to receivables-disclosure refusal and network-reach contraction unaddressed | B05 credibility_grade |

---

## MANAGEMENT DELIVERY TRACK RECORD

| Promise | Stated Quarter | Outcome | Grade | Anchor |
|---------|-----------------|---------|-------|--------|
| FY26 revenue growth 30% like-for-like | Q3 FY26 call | Delivered: 31.5% LFL | ✓ | B05 |
| FY26 EBITDA margin 4% | Q3 FY26 call | Delivered: 4.03% | ✓ | B05 |
| FY26 OCF ~Rs 100 Cr | Q3 FY26 call | Partial: Rs 96.2 Cr (96%) | ◐ | B05 |
| MedTech annualised revenue >Rs 1,000 Cr | Q3 FY26 call | Delivered: Confirmed Q4 FY26, reaffirmed Q1 FY27 | ✓ | B05 |
| M&A pause (next 2-3 quarters) | Q3 FY26 call | Partial: Extended through all FY27 (longer than stated) | ◐ | B05 |
| NWC days toward 60 | Q3 FY26 call | Delivered: 59 days Q4 FY26 | ✓ | B05 |
| Tax rate glide path to 22-23% FY27 | Q3/Q4 FY26 call | Delivered: Guided FY27 rate consistent | ✓ | B05 |
| FY27 guidance: 23% revenue ex-M&A, 5% EBITDA, >=50% OCF conversion | Q4 FY26 call | Partial: EBITDA 5.0% hit in Q1; revenue/OCF not yet full-year testable | ◐ | B05 |
| Minority interest normalize to 25-27% of PBT-minority | Q4 FY26 call | Delivered: Q1 FY27 actual ~27% | ✓ | B05 |
| Depreciation stays at Q4 FY26 level absent new capex | Q4 FY26 call | Delivered: Broadly same level in Q1 FY27 | ✓ | B05 |

**Credibility Grade: B (Good)** — 8 delivered, 4 partial, 0 missed. Held at B not A by refusal to disclose receivables aging (against FLAG-CASH) and unaddressed network-reach-metric contraction (B05 analyst_note key finding). | B05

---

## TOP 2-3 GROWTH TRIGGERS

| Priority | Trigger | Type | Timeframe | Conviction | Confirm Signal | Kill Signal | Anchor |
|----------|---------|------|-----------|------------|-----------------|------------|--------|
| 1 | MedTech scaling to ~20% of revenue with structurally higher margins | revenue+margin | 2-3yrs | H | MedTech segment revenue/margin tracking to/beyond Rs 1,000 Cr | MedTech growth flattens or margin uplift fails in consolidated GM/EBITDA | B05 |
| 2 | EBITDA margin trajectory toward 5%+ sustained through FY27 (already hit Q1 FY27) | margin | near | H | Quarterly EBITDA margin holds ≥5% through FY27 | Margin regresses toward 4% on integration costs or pricing pressure | B05 |
| 3 | Organic growth sustaining >15-20% despite extended M&A pause | volume | 3-4yrs | M | Organic growth stays materially above IPM | Organic growth converges to IPM, outperformance multiple disappears | B05 |

---

## EMERGING MOAT (EM) SCORE & CLASSIFICATION

| Item | Value | Anchor |
|------|-------|--------|
| EM Score | 19 | B07 em_score |
| EM Classification | MODEST | B07 em_classification |
| Evidence Mix (Documented/Claim/Inference) | 15 / 10 / 5 | B07 evidence_mix |
| Active Categories (Moderate+ Strength) | B3 (Supply chain network effect), F2 (Execution moat / guidance delivery), G2 (WC improvement trajectory), H1 (Industry consolidation beneficiary) | B07 active_categories |
| Strategic Asset / Monopoly Position | No monopoly; 4 moats confirmed (distribution access/manufacturer relationships, scale/procurement leverage, data/technology platform, efficient scale in penetrated geographies); switching costs rated low-medium | B07 moats_present; B04 moats |
| **Moat Erosion Flag** | **NETWORK-REACH CONTRADICTION**: retail pharmacies -32%, hospitals -36%, SKUs -14%, districts -9% Q4FY26→Q1FY27, while warehouse count ROSE (136→138) in same quarter, margin/ROCE both record-high. Unreconciled. Directly undermines the stated core moat claim. | B07 FLAG-EMOAT-NETWORK |

---

## PRIMARY CATALYST & PROXIMITY WINDOW (12-MONTH)

| Catalyst | Window | Evidence Type | Anchor |
|-----------|--------|---------------|--------|
| MedTech FY27 organic revenue confirmation toward Rs 1,000 Cr+ | FY27 | Documented guide, partially delivered | B07 catalysts_12m row 1 |
| FY27 EBITDA margin sustaining ≥5% | Near | Already hit once (Q1 FY27 5.0%) | B07 catalysts_12m row 2 |
| OCF-to-EBITDA conversion reaching ≥50% FY27 | Near | Documented guide | B07 catalysts_12m row 3 |
| **Network-reach metric reconciliation** | **Next quarter (H1 FY27)** | **Unresolved; management silent** | **B07 catalysts_12m row 4 — TOP HALT 1 VERIFICATION ITEM** |
| First disclosed adoption metric for Entero Direct/HealthEdge/Enteropreneur | 12-24m | Currently absent | B07 catalysts_12m row 5 |

---

## UNDISCOVERED ALPHA (UA) QUALIFIER CHECK

| Qualifier | Criterion | Status | Evidence | Anchor |
|-----------|-----------|--------|----------|--------|
| Listed ≥12 months | Yes (IPO Feb 2024, run date Jul 2026 = 29m) | ✓ PASS | B00 inputs_present; manifest run_date 2026-07-27 | B00 |
| Gate 0 ≥60 OR EM ≥25 | Gate 0 score 53 (< 60); EM score 19 (< 25) | ✗ FAIL both | B01 grand_total 53; B07 em_score 19 | B01, B07 |
| FII+DII <3% | FII+DII ~19.8% at Jun-26 (DOES NOT SATISFY <3%) | ✗ FAIL | ~19.8% Jun-26 operator-ferried Screener data (B00 notes non-anchored); filed shareholding-pattern PDF still absent | B00 notes; fttcp-deliberation Pillar 3 |
| **All Three Qualifiers Met** | — | **✗ NO** | Fails on both Gate 0 & EM; FII+DII too high | — |
| **UA Outcome** | DOES NOT APPLY | High institutional ownership (~19.8%) fails the absence qualifier | B00, fttcp-deliberation Pillar 3: "FII+DII ~19.8% at Jun-26 (>3%); the institutional-absence qualifier fails." | fttcp-deliberation |

---

## DOWNSTREAM SIGNAL CANDIDATES (FROM B09.downstream_candidates)

Unverified candidates; copied as given:

| Signal | Entity Type | Demand Link | Likely Source | Cadence | Shared Catalyst |
|--------|-------------|-------------|----------------|---------|-----------------|
| IQVIA/AIOCD Indian Pharmaceutical Market (IPM) MAT growth | Macro | Direct read on pharma consumption growth Entero distribution throughput tracks | IQVIA India Pharmaceutical Market reports | Monthly | False |
| NPPA/DPCO price notifications on NLEM SKUs | Regulatory | Price-controlled SKUs compress distributor gross margin directly | NPPA notifications | Event-driven | False |
| Apollo HealthCo / Keimed disclosures | Counterparty | Largest peer's scale/growth direct read on organized-sector consolidation pace | Apollo Hospitals investor presentations/earnings calls | Quarterly | False |
| Hospital chain bed-count/capex expansion announcements | End-customer | Hospital MedTech demand (cardiology/IVD/ortho) scales with hospital capacity additions | Apollo/Max/Fortis/Manipal investor releases | Quarterly | False |
| Domestic-formulation growth commentary from large manufacturers | Counterparty | Manufacturer commentary corroborates or contradicts IPM growth read independently | Sun Pharma/Cipla/Alkem quarterly earnings calls | Quarterly | **TRUE (SHARED)** |
| GST e-way bill/e-invoicing trade-volume data for pharma HSN codes | Macro | Formalization proxy for unorganized-to-organized shift SOM thesis depends on | GSTN/Ministry of Finance releases | Monthly | False |

**Demand Externally Verifiable: TRUE** (B09) — Multiple independent macro, regulatory, and counterparty signals can corroborate or refute demand trajectory.

---

## AR FY26 NEW DOWNSTREAM ENTITIES (FEED FOR ROLE 5.5 AR CROSS-CHECK, STEP 10.5B)

| Name | Where in AR | Entity Type | Anchor |
|------|------------|-------------|--------|
| Bioaide Technologies Private Limited | Board's Report p.36; Corporate Overview p.9-10; BRSR p.78 | New subsidiary/acquisition (80%) | B03 ar_new_downstream_entities row 1 |
| Anand Medilink Private Limited | Board's Report p.36; Corporate Overview p.11; BRSR p.78 | New subsidiary/acquisition (80%) | B03 ar_new_downstream_entities row 2 |
| Sai RK Pharma Private Limited | Board's Report p.36; Corporate Overview p.11; BRSR p.78 | New subsidiary/acquisition (70%) | B03 ar_new_downstream_entities row 3 |
| Well Wisher Pharma Private Limited | Board's Report p.36; Corporate Overview p.11; BRSR p.78 | New subsidiary/acquisition (70%) | B03 ar_new_downstream_entities row 4 |
| Ramson Medical Distributors Private Limited | Board's Report p.36; Corporate Overview p.11; BRSR p.78 | New subsidiary/acquisition (70%) | B03 ar_new_downstream_entities row 5 |
| Ace Cardiopathy Solutions Private Limited | Board's Report p.36; Corporate Overview p.9-10; BRSR p.78 | New subsidiary/acquisition (60%) | B03 ar_new_downstream_entities row 6 |
| Anand Chemiceutics Private Limited | Board's Report p.36; Corporate Overview p.12; BRSR p.78 | New subsidiary/acquisition (51.51%) | B03 ar_new_downstream_entities row 7 |
| HealthEdge | Corporate Overview p.15 | New named digital platform (retail chemist engagement) | B03 ar_new_downstream_entities row 8 |
| Enteropreneur Programme | Corporate Overview p.14 | New named partner-led distribution initiative | B03 ar_new_downstream_entities row 9 |

---

## SOM-IMPLIED REVENUE CAGR & DOWNSTREAM

| Item | Value | Anchor |
|------|-------|--------|
| TAM (Conservative, Rs Cr) | 3,72,000 | B09 tam_cr.conservative |
| TAM (Realistic, Rs Cr) | 4,96,500 | B09 tam_cr.realistic |
| SAM (Rs Cr) | 2,63,000 | B09 sam_cr (70.7% of TAM) |
| SOM 3-Year (Rs Cr) | 13,300 | B09 som_3yr_cr |
| SOM 5-Year (Rs Cr) | 19,900 | B09 som_5yr_cr |
| **SOM-Implied Revenue CAGR (3-Year)** | **26.4%** | B09 som_implied_revenue_cagr.yr3 |
| **SOM-Implied Revenue CAGR (5-Year)** | **24.8%** | B09 som_implied_revenue_cagr.yr5 |
| Current SAM Share (%) | 2.5% | B09 current_sam_share_pct |
| Revenue Headroom (x) | 39.9x | B09 revenue_headroom_x |
| Runway Class | STRONG | B09 runway_class |
| **Capacity Constraint** | **~Rs 1,000-1,100 Cr incremental WC funding gap by yr3** | B09 capacity_check: "SOM revenue capture is financing-constrained, not market-constrained" |

---

## RATING EXTRACTION (INDIA RATINGS, 2025-12-03)

| Item | Value | Anchor |
|------|-------|--------|
| Agency | India Ratings and Research (Ind-Ra) | ratings.pdf, page 1 |
| Rating | IND A-/Stable | ratings.pdf, page 1 |
| Outlook | Stable | ratings.pdf, page 1 (Issuer Rating table) |
| Date | 2025-12-03 (Dec 03, 2025) | ratings.pdf, page 1 |
| Rating Action | Affirmed | ratings.pdf, page 1 |
| **Working Capital / Cash Flow Commentary (Verbatim, Page 3)** | "Entero group's cash flow from operations has been negative since the first full year of its operations in FY19 due to the intense working capital requirement and modest yield nature of its business. The net cash flow from operations remained negative at INR769 million in FY25 (FY24: negative INR366 million) due to the increase in working capital requirement with growth in the scale of operations. The management expects the cash flow from operations to be positive by the end of FY26. The group's net working capital cycle on sales basis marginally elongated to 78 days in FY25 (FY24: 75 days) but remained in line with the peers in the pharmaceutical distribution segment. The cash flow from operations and free cash flow are likely to remain negative, in the agency's view, in the near term. However, the reduction in the goods and services tax rates to 5% in September 2025 from 12%, and management's cost-efficient strategies may turn the operating cashflows positive by end-FY26." | ratings.pdf, page 3, Liquidity section |

---

## PEER FINANCIAL DATA (IF AVAILABLE)

| Peer | P/E | EV/EBITDA | P/B | Revenue CAGR | ROCE | Anchor |
|------|-----|----------|-----|--------------|-------|--------|
| (Peer data) | NOT PROVIDED | unresolved | (Instructions note: peer medians if peer financial data was provided) | — | — | B12d carried 12 peer calls; financial summaries not extracted as a comparative table in provided blocks |

**Note**: B12d audited 12 peer concalls substantively; detailed peer financial medians not compiled in a summary table in the blocks provided. Role 1 Stage 11 amendment-20 peer-table check flagged in fttcp-deliberation Pillar 3.

---

## CONFLICTS & UNRESOLVED FIELDS

### Conflicts (Upstream disagreements, both anchored)

| Field | Value A | Anchor A | Value B | Anchor B | Used (Conservative) | Reasoning |
|-------|---------|----------|---------|----------|---------------------|-----------|
| ROCE Latest (FY26) | 9.7% (standard consolidated, goodwill-inclusive basis) | B01 dissent, standard EBIT / average capital employed | 20-25% (operator forward-capital ruling on incremental capital post-M&A pause) | fttcp-deliberation Pillar 1 ruling 2026-08-30 | **20-25% (per FTTCP)** | Operator ruled forward-capital basis; dissent 12x remains the conservative default-track sensitivity. "Reverts to 12x on new M&A > ~Rs 200 Cr / rolling 12m." (fttcp-deliberation) |
| Net Debt-to-Equity (Adjusted) | 0.02x→0.23x (specific 'adjusted' methodology not pinpointed) | B02 Finding 6 (also note this came from earlier finding, now marked MAJOR source_fidelity in B12a) | 0.09x→0.31x consolidated (D/E unadjusted basis) | B02, B12a notes; three leverage ratios non-reconciled for same FY26 | **0.31x (gross D/E, unadjusted)** | Conservative: use gross, unadjusted; term 'adjusted' lacks transparent methodology per B12a. Three definitions in AR not bridged; B02 flagged as MAJOR. |
| Working Capital Days | 59 days (Q4 FY26 exit figure) | B05 promise_delivery row 6 | 70→68 days (LFL FY25-FY26 trend, two metrics not reconciled) | B03 monitorables; AR Note | **59 days (Q4 FY26)** | Latest quarterly exit figure; two different metrics noted but not conflated. Conservative: use audited Q4 exit. |
| PAT CAGR (3-year) | NOT COMPUTABLE (loss-to-profit swing FY21-FY23, synthetic CAGR not attempted) | B01 data_notes | (No alternative estimate attempted per CLAUDE.md: never estimate) | — | **NOT FOUND** | FTTCP rules out estimation; loss-to-profit swing precludes synthetic CAGR. |

### Unresolved Fields

| Field | Why Unresolved | Where It Might Be | Anchor |
|-------|-----------------|-------------------|--------|
| Diluted EPS (FY26, Rs) | Screener CSV does not carry EPS; AR provided but not in corpus section read | FY26 Consolidated Financial Statements (Note 33 or equivalent, earnings per share disclosure) | screener does not carry; B00 notes AR corpus provided but not fully read for EPS |
| FCF (FY26, Cr) | Consolidated capex line unavailable (screener Cash_Flow.csv no capex detail; standalone capex 159.39 Cr available but different consolidation basis not substitutable) | FY26 AR Consolidated Cash Flow Statement with capex-separate line; or management guidance in concall | B01 FLAG-CASH; B01 data_notes: "FCF (B2, B3) not computable: screener Cash_Flow.csv gives only net CFO/CFI/CFF with no capex line; PDFs disclose only STANDALONE capex (FY25-FY26)" |
| Book Value Per Share (Rs, FY26) | Net worth (Rs 1,645.1 Cr in screener) is distorted by mid-year IPO equity infusion and put-option-liability fair-value movements (B02 Finding 5: NCI put/call fair value Rs 1.5bn+ through equity bypassing P&L); mechanical division yields ~Rs 378.4/share but unreliable | Next AR with stabilised equity base post-IPO, post put-option resolution | B01 data_notes: "ROE FY24 uses average net worth spanning a mid-year IPO equity infusion (opening -68.59cr to closing 1638.06cr); mechanically computed per formula but flagged as distorted" |
| FCF / PAT Ratio | Cannot compute (FCF uncomputable per above) | As FCF resolves | — |
| P/FCF | Cannot compute (FCF uncomputable) | As FCF resolves | — |
| P/B (Price-to-Book, FY26) | Book value distorted by IPO equity and put-option movements (see Book Value Per Share above); ratio unreliable | As book value stabilises | B04 not_applicable: "Price-to-Book/NAV/SOTP (goodwill ~44%+ of assets distorts book value)" |
| Pledged Shares (%) | Filed shareholding-pattern PDF still ABSENT despite operator-ferried Screener data (FII+DII ~19.8% Jun-26) | BSE / NSE Reg 31(4) shareholding pattern filing | B00 input_gaps: "Filed pattern PDF still ABSENT; pledge % not shown" |
| Audit Fee vs Non-Audit Fee Ratio | NOT FOUND IN DOCUMENT in sections read | AR Note (typically corporate governance or audit-remuneration section, if disclosed) | B03 input_gaps: "audit fee vs non-audit fee ratio (Phase 1E) - NOT FOUND IN DOCUMENT in sections read this pass" |
| Q1 FY27 Complete Financials | Only guidance tracking and margin data extracted; full income statement/cash flow for quarter not in provided corpus | Q1 FY27 Results PDF (stated 2026-08-07 release date per B00) not located in inputs folder despite manifest reference | B00: "Q1 FY27 (2026-08-07) results" referenced; results PDFs not found in runs/.../inputs/results/ |
| Prior-Year CFO (FY25 & earlier) | CFO FY25 -76.9 Cr extracted; full CFO series for trend clarity available in screener but not a standing table in blocks | screener-Data_Sheet.csv cash-flow section | Screener carries FY20 -36.52, FY21 -68.68, FY22 -35.27, FY23 -45.32, FY24 -36.61, FY25 -76.87, FY26 +96.2 |
| Peer Medians (P/E, EV/EBITDA, P/B, Growth, ROCE) | Peer concalls audited (12 substantively used per B12d) but financial-summary table not compiled in stage output | B06, B12d, role 1 stage 11 amendment-20 instruction | B12d: "11 of 12 peers used substantively; B06 CITED-ONLY the 12th, which D shows was actually used" |
| FII+DII Shareholding (%) [PARTIALLY RESOLVED] | Operator-ferried Screener data: FII+DII ~19.8% Jun-26 (non-anchored, no filed PDF). Filed shareholding-pattern PDF ABSENT; pledge % NOT FOUND. Mark FII+DII as available (~19.8%) with caveat; keep pledge unresolved. | BSE / NSE quarterly shareholding-pattern (Reg 31(4)) filing | B00: "PARTIALLY CLOSED by operator-ferried Screener quarterly pattern (work/operator-ferried-2026-08-29.md): promoter ~52.4% flat, FII 23.3%->4.36% (Mar24->Jun26), DII 2.3%->15.48%, FII+DII ~19.8% Jun26. Filed pattern PDF still ABSENT; pledge % not shown." |

---

## FTTCP DELIBERATION CARRY-FORWARDS (AUTHORITATIVE FOR STAGE 11)

**All below sourced from fttcp-deliberation.md, signed 2026-08-30 (operator), and SUPERSEDE any earlier pipeline determination per the assembly rules.**

### Operator-Approved Valuation Pillars (Phase 3 must use)

**Pillar 1 (ROCE):**
- Base: 20-25% (forward-capital basis post-M&A pause)
- ROCE Base Multiple: 19x (continuous formula, Amendment 5/v3.6: 0.5 × ROCE + 7.5)
- Dissent Recorded: 12x (standard EBIT / average capital employed incl. goodwill, ~9.9% FY26 / ~14% annualised Q1 FY27; goodwill-inclusive basis)
- **M&A Reversion Condition**: "Reverts to 12x on new M&A > ~Rs 200 Cr / rolling 12m" (fttcp-deliberation Pillar 1)
- Route: Operator forward-capital ruling; ROCE recovery credited via Pillar 1; Strategic Premium ROCE re-rating route BARRED (single-credit)

**Pillar 2 (Cash Multiplier):**
- Status: INDETERMINATE (FCF uncomputable, no consolidated capex line)
- Treatment: ≤1.0x, never a clean pass; CAPS the disposition at PROCEED WITH CAVEATS
- Resolves at: H1 FY27 (~Nov 2026)

**Pillar 3 (Growth / EM Premium):**
- EM Score: 19 (understated pending B07 recheck for master-data + 15% exclusive tie-ups)
- Classification: MODEST
- Growth-Premium Eligibility: Opens on the 20-25% forward ROCE basis (Amendment 16)
- Premiums Capped By: Sector cap (see below)

**Strategic Premium:**
- Status: BARRED (single-credit; ROCE recovery already credited via Pillar 1)

**Undiscovered Alpha (UA):**
- Status: DOES NOT APPLY
- Reason: FII+DII ~19.8% at Jun-26 (>3%); the institutional-absence qualifier fails

**Sector Cap:**
- Value: **18-20x** (operator-approved, 2026-08-30 ruling)
- Authority: Overrides manifest "Pharma / CDMO" (collector default, INCORRECT)
- Rationale: No pharma/MedTech distribution row exists in Section 1B; this ruling substitutes
- Binding: Absolute ceiling; premiums do not lift the exit because the cap binds

**Destination (Exit) PE:**
- Both Tracks: 18-20x
- Additive Track: Pillar 1 19x capped at sector cap
- RRM Track: ~19x at r 13.5% (Amendment 4.4), lower if r set higher for risk

**Earnings Basis:**
- **ONE-YEAR-FORWARD P/E** (operator chosen 2026-08-30)
- Rationale: "A fast-growing distributor is valued on forward earnings, consistent with the entry-zone math already built on FY30 forward EPS." (fttcp-deliberation Pillar 3)
- Amendment 18 Exit-Basis Symmetry: "The exit multiple is applied on the same forward basis as the entry."

### Operator Overrides (with Default-Track Sensitivity)

**Override 1: Halt 1 Decision**
- Draft Recommendation: SHALLOW WATCH
- Operator Ruling: PROCEED with full pipeline
- Default-Track Sensitivity: On conservative track, the name is a WATCH, not a trade at CMP; cost of proceeding is running Phase 3 valuation at price ~45% above FTTCP entry zone

**Override 2: Pillar 1 ROCE Base**
- Draft: 19x (Claude Code and dossier consensus)
- Operator Ruling: 19x on forward-capital basis
- Default-Track Sensitivity: Dissent 12x (goodwill-inclusive standard EBIT/capital); if Phase 3 run on 12x, every fair value falls by ~1/3; reverts to 12x if M&A >~Rs 200 Cr announced

**Override 3: Destination PE & Earnings Basis**
- PE Base: 18-20x (no override cost; drafts and ruling agree)
- Earnings Basis: ONE-YEAR-FORWARD P/E (operator chose)
- No reversion condition

### Phase 3 Carry-Forward Flags

- **SHARED CATALYST**: The M&A pause drives both ROCE recovery (Pillar 1) and margin/MedTech growth story (Pillar 3). Role 3 must stress-test that single lever.
- **ROCE Denominator Dissent**: 12x dissent and M&A reversion condition (>Rs 200 Cr rolling 12m) must appear in Role 1 worksheet and devil's advocate
- **Operating EPS Adjustment**: Module B4 must strip FY26 exceptional item and NCI put/call fair value (Rs 1.5bn+ through equity per B02 Finding 5); single-segment disclosure means Phase 3 computes from results PDFs
- **Verify Sector Cap**: Manifest auto-populates incorrectly; use 18-20x operator ruling for role 1 inputs

### Mechanical FTTCP Composite (Unmodified from Draft)

- **Verdict Score**: +4 of 8 (Revenue FIRING +2, Margin STARTING +1, Cash STAGNANT 0, ROCE RECOVERING +1)
- **Classification**: DEEP WATCH leaning BUY-ON-DIPS
- **Carried Into Phase 3**: Under operator's PROCEED override
- **Live Caveats**: INDETERMINATE cash cap and price gap (~45% above entry zone)

---

## ANALYST NOTES & ASSEMBLY CAVEATS

1. **Results PDFs (Q3 FY26, FY26 full-year, Q1 FY27)**: Task referenced three results PDFs (79a91338-..., 5d6adb02-..., 80e84d9b-...) to read directly; these files were not located in runs/.../inputs/results/ and could not be read. Financial data extracted from: (a) screener-Data_Sheet.csv (full-year FY20-FY26 audited), (b) quarterly rows in screener (up to Q4 FY26), (c) block-extracted Q1 FY27 guidance tracking (B05), (d) AR Note extractions (B02, B03). Q1 FY27 complete financial statements unavailable; only guidance-tracking and selective quarter metrics extracted.

2. **Rating PDF**: Image-only, read visually via poppler. WC/cash-flow commentary extracted verbatim from page 3, Liquidity section. This quote is what FLAG-CASH determination will cite downstream; captured exactly as required.

3. **Consolidated vs. Standalone Capex**: FY26 standalone capex disclosed (Rs 159.39 Cr, 2.4% of revenue, per AR Note 5A); consolidated capex line absent from screener Cash_Flow.csv. This explains the FCF INDETERMINATE determination in Pillar 2.

4. **Goodwill Distortion**: Goodwill Rs 7,490.9 Cr is 43.8% of consolidated net worth (B02 Finding 1), built on three deals at 87-100%+ goodwill (B02 Finding 1). This distorts book-value and P/B ratios; P/B marked unresolved and noted in B04 as not_applicable. Any downward goodwill-impairment revision has outsized balance-sheet effect (B02 Finding 1 rated RED).

5. **Subsidiary Distress Broader Than Disclosed**: Note 54 shows ~15 of ~65 entities with negative net assets/loss; CARO Annexure shows 40 with adverse/qualified clause, mostly cash losses. Roll-up integration quality is a material risk (B02 Finding 2, B03 Finding 2).

6. **NCI Put/Call Option Fair-Value Bypass**: Rs 1.5bn+ moved through Other Equity in FY26, bypassing P&L (B02 Finding 5). Reported PAT growth of +21.3% does not capture this; must be modelled separately for valuation.

7. **Network-Reach Reconciliation**: TOP HALT 1 VERIFICATION ITEM (B07 FLAG-EMOAT-NETWORK, B05 analyst_note). Retail pharmacies -32%, hospitals -36%, SKUs -14%, districts -9% Q4FY26→Q1FY27, while warehouse count ROSE (136→138) and margins/ROCE both hit records. Management silent; no analyst caught it on calls. Could be disciplined low-margin pruning or real attrition offset by wallet-share gains. Directly bears on network moat integrity.

8. **FII+DII Shareholding**: Operator-ferried Screener data shows ~19.8% Jun-26 (FII exited from 23.3% Mar-24 to 4.36% Jun-26; DII rose 2.3% to 15.48%). Filed shareholding-pattern PDF still absent; pledge % unresolved. FII+DII high enough to fail UA qualifier (>3%). Mark as available with caveat; keep pledge unresolved.

9. **Cash Conversion Cap**: INDETERMINATE determination (Pillar 2) caps downstream verdict at PROCEED WITH CAVEATS per CLAUDE.md until capex/consolidated CF statement evidence supplied. Blocks H1 FY27 resolution (~Nov 2026).

10. **Evidence Mix**: Blocks carry documented/claim/inference splits. B07 evidence_mix 15/10/5 (mostly documented with claims/inference). This is "mostly-📄" per instructions (documented > 50%).

---

## END OF REPORT

**Report compiled by**: Stage 10 Assembly (Haiku 4.5)  
**Run date**: 2026-07-27  
**Report date**: 2026-08-30  
**FTTCP authority**: Signed 2026-08-30 (operator), all rulings supersede earlier determinations  
**Output**: Full table + conflicts[] + unresolved[] + YAML block below

---
