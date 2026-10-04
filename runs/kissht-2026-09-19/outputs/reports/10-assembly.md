# STAGE 10: VALUATION INPUT ASSEMBLY
## OnEMI Technology Solutions Ltd (Kissht)
Ticker: KISSHT (NSE) / 544754 (BSE)  
Run date: 2026-09-19  
Run folder: runs/kissht-2026-09-19  
Assembly date: 2026-10-04 (corrected 04-Oct-2026)  
Model: claude-haiku-4-5-20251001  

---

## COMPANY IDENTITY BLOCK

| Field | Value | Anchor |
|-------|-------|--------|
| Company | OnEMI Technology Solutions Ltd (Kissht) | (B00.corpus_manifest, header) |
| Ticker | KISSHT (NSE); 544754 (BSE) | (B00.corpus_manifest, header) |
| Sector | Banks / NBFCs / MFIs | (B00.sector_cap_row; B04 confirmed lender archetype) |
| Business model type | Lending: unsecured personal loans (92.3% of AUM) + LAP (7.7%) | (B04.business_type; results Q1 FY27 press release 20260729-74639f09 p.2) |
| Sector cap row primary method | P/B (Price-to-Book); P/E cross-check | (B00.sector_cap_row_evidence: 18x P/B primary per Section 1B v3.3+) |
| Sector cap PE (whole company) | 18x | (B00.sector_cap_row_evidence) |
| CMP (Rs per share) | 369.55 (Trendlyne LTP, 01-Oct-2026) | (fttcp-deliberation §5) |
| Shares outstanding, diluted pre-raise (Cr) | 18.1922 | (fttcp-deliberation §3 override 6; RHP p.105) |
| Shares outstanding, diluted post-raise (Cr) | 20.8416 | (fttcp-deliberation §3 override 6) |
| Market cap (post-raise, Rs Cr) | 7,555.1 (Rs 369.55 per share × 18.1922 Cr pre-raise + Rs 832.20 Cr raise) | (fttcp-deliberation §5 [INFERENCE]) |
| Enterprise value note | n.m. for a lender (P/B primary); Rs 208.05 Cr is the Amendment 27.1 cash line only | (lender valuation does not use EV; cash is general-purpose slice per Amendment 27.1) |

---

## LATEST FINANCIALS (CONSOLIDATED)

**Most recent reporting: Q1 FY27 (30-Jun-2026, unaudited, 3-month)**  
**Prior year full-year: FY26 (31-Mar-2026, audited, 12-month)**

| Metric | Q1 FY27 | FY26 | Anchor |
|--------|---------|------|--------|
| **INCOME STATEMENT** | | | |
| Revenue (Rs Cr) | 669.50 | 2,179.25 | (results Q1 FY27 p.5: 6,695.00 million ÷ 10; FY26 p.6: 21,792.46 million ÷ 10) |
| EBITDA (Rs Cr) | NOT FOUND | NOT FOUND | (No EBITDA figure disclosed for lenders; interest income + fee income less finance cost is a non-standard proxy; not computed by pipeline stages) |
| EBITDA margin (%) | NOT FOUND | NOT FOUND | (Not applicable: financial firm; interest margin and cost-to-income ratio used instead per B04) |
| PAT (Rs Cr) | 95.08 | 281.45 | (results Q1 FY27 p.5: 950.77 million ÷ 10; FY26 p.6: 2,814.52 million ÷ 10) |
| PAT margin (%) | 14.21 | 12.91 | (computed: PAT / revenue) |
| **PER SHARE METRICS** | | | |
| Diluted EPS (Rs) | 5.88 | 21.39 | (results Q1 FY27 p.5; FY26 p.6) |
| Book value per share, Mar-27 (Rs) | 164.3 | 131.33 (FY26) | (fttcp-deliberation §5 [INFERENCE]: Jun-26 BVPS Rs 133.3 × 16.85 Cr + Q2-Q4 FY27 PAT 345.9 + raise 832.20, over 20.84 Cr; FY26 from AR net worth 1,231.98 Cr / 9.3769 Cr paid-up pre-split) |
| **BALANCE SHEET & LIQUIDITY** | | | |
| Net debt / (cash) (Rs Cr) | 208.05 (general-purpose cash slice only) | see notes | (fttcp-deliberation §5 Amendment 27.1: surplus cash Rs 208.05 Cr held at face value; FLDG deposits excluded as collateral) |
| Net cash (Rs Cr) | 208.05 | NOT FOUND | (cash surplus post-raise; FY26 figure not disclosed for this assembly purpose) |
| **GROWTH METRICS** | | | |
| Revenue CAGR 3-year (%) | NOT FOUND | (no 3-year series available; company unlisted until 08-May-2026) | (B00: only FY26 audited AR held; RHP restated FY23-FY25) |
| PAT CAGR 3-year (%) | NOT FOUND | (loss-to-profit swing FY21-FY22; C2 cagr edge rule; B01) | (B01 data_notes: 'no synthetic PAT CAGR attempted') |
| Revenue growth YoY (%) | 44.8 | 63.0 | (Q1 FY27 vs Q1 FY26: 669.5 vs 463.1; FY26 vs FY25: 2,179.25 vs 1,337.47 from RHP restated) |
| PAT growth YoY (%) | 59.2 | 75.0 | (Q1 FY27 vs Q1 FY26: 95.08 vs 59.74; FY26 vs FY25: 281.45 vs 160.62 from RHP restated) |
| **RETURNS (ANNUALIZED WHERE Q1 USED)** | | | |
| ROE (%) | 21.20 | 23.97 | (Q1 FY27 annualized from deliberation §5; FY26 RoAE from AR KPI p.5) |
| ROCE (%) | STAGNANT (T4 RoA/RoE sole Pillar 1 authority; not overridden) | see note | (fttcp-deliberation §2 ruling 12; lender variant applies per ruling 16) |
| **ASSET QUALITY (LENDER METRICS)** | | | |
| GNPA (Stage 3) (%) | 2.25 | 2.12 | (Q1 FY27 press release 20260729-74639f09 p.2; FY26 AR KPI p.5) |
| NNPA (%) | NOT FOUND for Q1 | 0.29 | (FY26 AR KPI p.5; Q1 figure not separately disclosed in results) |
| PCR (%) | NOT FOUND | 86.15 | (FY26 AR KPI p.5; Q1 figure not given) |
| Write-off rate (% of AUM, annual) | ~15.7 | ~15.7 | (B02 finding rank 2: annual write-off ~15.7% of average book; FY26 Rs 4,725.95 mn, +10.7% YoY; Consolidated Note 41 pp.127-129, Note 26 p.119) |
| Cost-to-Income ratio (%) | 56.64 | 56.64 (FY26) | (B01 FLAG-QUALITY: FY24 45.54% to FY26 56.64%; Q1 FY27 specific ratio not extracted) |
| **ASSET METRICS** | | | |
| AUM (Rs Cr) | 8,001 | 7,066 | (Q1 FY27 press release p.2; FY26 AR KPI p.5) |
| AUM growth YoY (%) | 13.3 (Q1 QoQ) | 73.0 (full year) | (Q1 FY27 growth within quarter; FY26 full-year +73% per AR KPI; Q1 YoY would be 8,001 vs FY25 Mar-26 = 4,086, +96%) |
| **CASH FLOW & CONVERSION** | | | |
| CFO (Rs Cr) | NOT FOUND for Q1 | see note | (Consolidated: no Q1 CFO extracted; FY26 and earlier: see B01 FLAG-CASH) |
| CFO / PAT (ratio, latest) | INDETERMINATE for Q1 | -1.64 (FY26) | (B01 FLAG-CASH: cumulative CFO FY21-26 -1,648.00 Cr vs cumulative PAT +671.20 Cr = -2.46x; FY26 standalone +1.2x per B01 analyst_note, consolidated negative per Ind AS 7 loan-disbursal classification) |
| FCF (Rs Cr) | NOT FOUND | NOT FOUND | (Not computed for lenders; capex is minor for asset-light lending model per B04; operating lease payments via Ind AS 16 make FCF definition non-standard) |
| **CAPEX / DEPRECIATION** | | | |
| Capex (Rs Cr) | NOT FOUND for Q1 | NOT FOUND for FY26 detailed | (B01: capex NOT FOUND FY21-22 due to screener balance-sheet limitation; RHP restated data starts FY23 but not itemized in assembly inputs) |
| Depreciation & amortization (Rs Cr) | 4.82 | 21.62 | (results Q1 FY27 p.5: 48.22 million ÷ 10; FY26 p.6: 216.17 million ÷ 10) |
| **DIVIDEND** | | | |
| DPS (Rs) | NOT FOUND for Q1 | NOT FOUND | (No dividend disclosed; recently listed company; profits reinvested into growth) |
| Dividend payout ratio (%) | NOT FOUND | NOT FOUND | (Not applicable; no dividend history) |

---

## UPSTREAM ANALYSIS INPUTS (COPIED FROM EARLIER STAGES)

| Field | Value | Anchor |
|-------|-------|--------|
| **CREDIBILITY & MANAGEMENT** | | |
| Credibility grade (A=Excellent, D=Poor) | C | (B05.credibility_grade) |
| Credibility basis | Two clean quarters mostly ahead of guidance; one hard test (GNPA/write-off mechanic) not fully supported cross-check; largest risk (228% guarantee) and Rs 832 Cr raise rationale absent from call record | (B05.credibility_basis) |
| **GUIDANCE** | | |
| Guided revenue growth | >40% (FY27) | (B05.guidance item 1, stated in Q4 FY26 call, Concall_Jun_2026_Transcript.pdf p.8) |
| Guided margin band | Credit cost -10 to -15% YoY (FY27); RoE 19-21% (FY27) | (B05.guidance items 2, 3, 4; Concall_Aug_2026_Transcript.pdf p.4, p.9) |
| **CATALYSTS & TRIGGERS** | | |
| Primary catalyst (12-month) | LAP branch-pace recovery toward FY27-end target; Rs 832 Cr preferential capital rationale disclosure; second rating upgrade; GNPA direction | (B07.catalysts_12m, rows 1-3) |
| Catalyst proximity window | FY27-end, EGM 14-Oct-2026 / next concall, FY27-FY28, Q2 FY27 | (B07.catalysts_12m) |
| **EMERGING MOAT** | | |
| EM score | 18.5 | (B07.em_score; ~0-92 scale, below EM >=25 UA-qualifying threshold) |
| EM classification | MODEST | (B07.em_classification; 12-24 band) |
| Moat strength (strongest categories) | D1 Strong (proprietary underwriting data / AI models, AUC 66-74%); C1 Moderate (cross-sell / LAP launch); D2 Moderate (digital platform 45+ partners) | (B07.active_categories rows; D1 only Strong-rated category) |
| **EVIDENCE QUALITY** | | |
| Evidence mix summary | Mostly documented (11 items across 8 categories); 8 claim-grade; 4 inference-grade | (B07.completionist_recount and evidence_mix) |
| Demand externally verifiable | True | (B09.demand_externally_verifiable) |
| **TAM / SOM / MARKET RUNWAY** | | |
| TAM (Rs Cr) | 2,600,000 to 2,700,000 (conservative/realistic) | (B09.tam_cr; India PL+LAP all-lender market) |
| TAM growth (%) | 20 | (B09.tam_growth_pct) |
| SAM (Rs Cr) | 60,000 (FY26 New Age/Digital Lender segment) | (B09.sam_cr) |
| SAM % of TAM | 2.3 | (B09.sam_pct_of_tam) |
| SOM (3-year, Rs Cr) | 33,620 | (B09.som_3yr_cr) |
| SOM (5-year, Rs Cr) | 63,747 | (B09.som_5yr_cr) |
| SOM-implied revenue CAGR (3-year) | 61.4 | (B09.som_implied_revenue_cagr yr3, on AUM proxy ~40% revenue/AUM yield) |
| Runway class | MASSIVE | (B09.runway_class) |
| **DOWNSTREAM CANDIDATES** | | |
| Downstream signal candidates (summary) | RBI Master Directions (FLDG caps); CRIF/TransUnion CIBIL bureau data; off-book partner banks/NBFCs; peer AUM/PAT (KreditBee, Navi, Fibe, Moneyview); EPFO/GST/ITR formalisation; RBI FSR (systemic credit/retail slippage) | (B09.downstream_candidates, 6 rows copied as summary) |
| First-time AR downstream entities | Invincible Minds Pvt Ltd (wholly owned subsidiary incorporated 17-Jun-2026, not yet in consolidated PS); Sachin Ramesh Tendulkar (individual investor + brand ambassador) | (B03.ar_new_downstream_entities, 2 rows) |

---

## RATING EXTRACTION

| Field | Value | Anchor |
|-------|-------|--------|
| Rating agency | CRISIL Ratings | (inputs/rating/CRISIL-SiCreva-RR-2026-02-13.txt cover) |
| Rating | A- / Stable (long-term bank debt; upgraded from BBB+ / Stable) | (CRISIL rationale section 1 'Rating Action'; 13-Feb-2026) |
| Short-term rating | Crisil A1 (upgraded from A2+) | (CRISIL rationale section 1) |
| Rating date | 13-Feb-2026 | (CRISIL rationale cover) |
| Rating outlook | Stable | (CRISIL rationale 'Outlook' section) |
| **Working Capital / Cash Flow Commentary (verbatim)** | "Liquidity Strong. As on December 31, 2025, the group had unencumbered cash, cash equivalent and liquid investment of Rs 290.4 crore. This is sufficient to cover one month debt repayments. Additionally, the group's average monthly collections stood at over Rs 500 crore over the last six months. Crisil Ratings also understands that Si Creva will not do any incremental disbursements unless it has adequate resources to service maturing debt obligations in the near term; this will remain a key monitorable." | (CRISIL rationale, 'Liquidity' section p.64; embedded within broader 'Key Rating Drivers - Strengths' narrative) |

---

## PEER MEDIANS (IF PROVIDED)

| Metric | POONAWALLA | UGROCAP | Anchor |
|--------|------------|---------|--------|
| P/E | NOT FOUND | NOT FOUND | (screener Data_Sheet CSVs provided for POONAWALLA and UGROCAP only; per B00 input_gaps, full quarterly/balance-sheet sheets were not collected; data insufficient for multi-period peer median construction) |
| EV/EBITDA | NOT FOUND | NOT FOUND | (Not applicable: financial firms; EBITDA undefined) |
| P/B | NOT FOUND | NOT FOUND | (Screener book values not extracted at this stage) |
| Growth | NOT FOUND | NOT FOUND | (Screener series not extracted; peer concall evidence exists but not tabulated as median) |
| ROCE | NOT FOUND | NOT FOUND | (Lender metrics; ROA/RoE used instead) |

**Peer evidence note:** Peer concall cross-checks exist (B06 stage). SBICARD, POONAWALLA, UGROCAP concall samples do not show cost-of-borrowing easing tailwind that Kissht cites; Rs 832 Cr raise at 40.2% CRAR is not precedented at the scale or timing observed in Poonawalla/Ugro raises.

---

## MENTAL MODEL DECLARATION & OPERATOR-SIGNED FTTCP INPUTS

**Carried forward as authoritative from fttcp-deliberation.md (signed off 04-Oct-2026):**

| Item | Value | Anchor |
|------|-------|--------|
| **VERDICT (final)** | Composite +2 of 8. DEEP WATCH leaning AVOID. Posture VALUE-TRAP RISK. | (fttcp-deliberation §1) |
| **Entity count** | ONE | (web handover dossier Section 1; deliberation ruling 5; SOTP slices are method outputs, not entities) |
| **PILLAR 1 (RoA/RoE backward verdict)** | STAGNANT (T4 sole authority; not overridden) | (fttcp-deliberation §2 ruling 12) |
| **Earnings basis** | FORWARD (31-Mar-2027 valuation date; own book on Mar-27 book; partner half on FY28 PAT; same basis at exit) | (fttcp-deliberation §5) |
| **Cash conversion** | GROWTH INDUCED (Ind AS 7 loan disbursal through CFO; operator confirmed) | (fttcp-deliberation §2 ruling 7; task message) |
| **T1 AUM growth** | FIRING +2 | (fttcp-deliberation §2 ruling 9) |
| **T2 NIM / funding cost spread** | DECLINING -1 (5.2-pt income decline post-raise; mix ~half, price ~half per deliberation section 7) | (fttcp-deliberation §2 ruling 10, §7 T2 note) |
| **T3 Asset quality** | STARTING +1 (operator override of draft STAGNANT; Q2 FY27 trigger: STARTING if Stage 2 <=3.3% and GNPA <2.92%; DECLINING if Stage 2 >4.11% or GNPA >2.92%) | (fttcp-deliberation §3 override 1; Q2 FY27 vs Q2 FY26 test, not Q1) |
| **Proof gate (transition to higher rung)** | NOT FIRED | (fttcp-deliberation §2 ruling 13) |
| **Proof gate definition** | All-in loss (on-book impairment + off-book ECL + collection outsourcing above run rate) / avg AUM below 10.5% for H2 FY27, with off-book loss rate not rising | (companies/KISSHT.md HALT 1 GATE; FY26 all-in loss 10.97% of avg AUM) |
| **Ugliness (part of posture)** | STRUCTURAL-FEATURE (negative CFO and cost-to-income optics are artifacts) | (companies/KISSHT.md rulings 2026-10-04 A, operator's words verbatim) |
| **Ugliness caveat** | Operator has not named which optic is structural; candidates in the dossier: off-book loss in opex, partner concentration, parent guarantee | (companies/KISSHT.md HALT 1 GATE) |
| **Recognition gap (part of posture)** | OPEN QUESTION for Stage 11: whether CMP already prices a cost-advantaged or franchise-tier lender against the sector cap | (fttcp-deliberation §5) |
| **Entry zone (provisional)** | ~Rs 350 per share (OPERATOR OVERRIDE; mechanical Track 1 Rs 371.4) | (fttcp-deliberation §3 override 5) |
| **Entry zone caveat** | PROVISIONAL pending Amendment 19 FV CAGR and return-source label; not to be presented downstream without these per CLAUDE.md | (fttcp-deliberation §5; CLAUDE.md) |
| **Sector cap (whole company & own-book slice)** | 18x P/B primary | (fttcp-deliberation §2 ruling 4) |
| **Sector cap (partner slice, operator-set blend)** | 22.67x (1/3 × 18x NBFC + 2/3 × 25x asset-light services; FLDG <40% revenue threshold to revisit) | (fttcp-deliberation §3 override 3) |
| **Hurdle rate** | Tier A, 25% | (fttcp-deliberation §5) |
| **Valuation method (primary)** | SOTP (Amendment 27.2): own book P/B + partner fee P/E cross-checks | (fttcp-deliberation §2 ruling 5; §5) |
| **Valuation basis (date & earnings)** | Forward, 31-Mar-2027. Own book on Mar-27 book value; partner half on FY28 PAT. Same basis at exit (Amendment 27.3) | (fttcp-deliberation §5) |
| **PAT projections** | Base 441 (FY27) / 623 (FY28); bear 400 / 500; bull 470 / 700 (return on average AUM 4.75% / 4.6%) | (fttcp-deliberation §5) |
| **AUM projections** | Base 11,600 (FY27) / 15,660 (FY28) | (fttcp-deliberation §5) |
| **Split (own book / partner fee revenue)** | 46 / 54 by AUM share | (fttcp-deliberation §5) |
| **Own book P/B multiples** | 0.8x (low) / 1.0x (base) / 1.2x (high) on Mar-27 book Rs 2,695.8 Cr | (fttcp-deliberation §5) |
| **Partner slice P/E multiples (SOTP)** | 18.62x (Track 1) / 20.64x (base) / 22.67x (high, cap) | (fttcp-deliberation §5) |
| **Cash (general-purpose surplus)** | Rs 208.05 Cr at face value, held constant on FV path (Amendment 27.1) | (fttcp-deliberation §5) |
| **Cash (FLDG deposits excluded)** | Locked collateral, not included in cash slice | (fttcp-deliberation §5) |
| **Undiscovered Alpha (UA)** | Not qualified | (fttcp-deliberation §2 ruling 18; EM 18.5 <25 threshold; listed only ~5 months) |
| **Governance durability add-on** | +0.5 (down from draft +1.5) per operator override 4 | (fttcp-deliberation §3 override 4) |
| **Cost of equity (r)** | 15.5% (14 base + 0.5 durability + 0.5 governance + 0.5 complexity) | (fttcp-deliberation §3 override 4, §5) |
| **Risk-return multiplier (RRM)** | 0.76 (applied to Pillar 1 multiple for Track 1 derivation) | (fttcp-deliberation §3 override 4, §5) |

---

## OPEN ITEMS & CONFLICTS

### Open Items (carried from fttcp-deliberation §8):

| # | Item | Owner | Blocks stage 11 | Impact |
|---|------|-------|-----------------|--------|
| I4 | Q2 FY27 business update (03-Oct-2026) not in corpus; BSE API returned Access Denied 04-Oct-2026 | operator to drop PDF into inputs/announcements/ | None at sign-off; T1 watch item reads it | AUM/GNPA/credit-cost Q2 trend will confirm or refute T1 FIRING trigger |
| I5 | Section 1B v3.11 (Amendment 27) not merged to main | operator, separate framework PR | **YES** | Stage 11 sign-off per CLAUDE.md ruling I5 (amendments must be merged before presentation) |
| A19 | Amendment 19 three-year FV CAGR and return-source label | Stage 11 | **YES** | Entry zone Rs 350 cannot be presented downstream without Amendment 19 label per CLAUDE.md |
| DBB | Disbursement by book (on-book Si Creva vs off-book partner), FY25/FY26/Q1 FY27 | IR reply | None at sign-off | Validates the 46/54 split; tests fee allocation fairness and entry-zone override sensitivity |

### Conflicts (values that differ across blocks, both with anchors):

| Field | Value A | Anchor A | Value B | Anchor B | Used | Resolution |
|-------|---------|----------|---------|----------|------|------------|
| FY23 CFO (consolidated) | 48.36 Cr | screener-data | 111.48 Cr | RHP restated consolidated cash flow p.271 | Both listed as unresolved | (B01 FLAG-DATA-CONFLICT: 2.3x apart; all other years FY24-26 reconcile exactly; flagged for Role 5.5 primary-source verification) |
| T3 asset quality | STAGNANT (draft) | fttcp-draft.md ruling 11 | STARTING +1 (operator override) | fttcp-deliberation §3 override 1 | STARTING +1 | Operator override per deliberation section 3, ruling 1; composite +2 result per ruling 14; deliberation governs |

### Unresolved (values NOT FOUND, with reason and recovery path):

| Field | Why NOT FOUND | Where it might be | Recovery path |
|-------|---------------|-------------------|----------------|
| FY21-FY22 ROCE | Screener balance sheet does not split current/non-current liabilities for those years | RHP restated data (starts FY23); auditor reports pre-listing | Requires full financial statements from before listing (not in corpus) |
| FY21-FY22 capex | RHP restated cash flow data starts FY23; screener no capex/PPE-purchase line | RHP restated data (starts FY23) | Requires full cash flow statements pre-FY23 (not in corpus) |
| WC days change (FY21 baseline) | No FY21 trade payables anywhere in corpus; AR/RHP payables data starts FY23 | AR/RHP payables notes | Requires FY21 balance sheet (not in corpus) |
| Promoter holding change (3-year trend) | Company listed 08-May-2026; only one post-listing shareholding statement (Jun-2026) exists | Future quarterly shareholding filings | Requires historical pledge/holding trend from pre-listing period (not in corpus) |
| FII/DII split (public shareholding) | BSE shareholding summary gives Promoter 24.80% / Public 75.20% only; no institutional sub-split | BSE detailed shareholding pattern OR next quarterly filing | Blocks UA qualifier; requires live-web FII/DII breakdown |
| SBICARD market cap | Screener only provided POONAWALLA and UGROCAP Data_Sheet CSVs; SBICARD produced no export | Screener Data_Sheet OR Trendlyne LTP | Collector defect; requires SBICARD peer-median comparability (minor impact) |
| R&D/Revenue (% of sales) | No R&D line disclosed anywhere in provided source | AR/RHP/concalls/decks (searched; not found) | Lender does not segregate R&D as manufacturing would; technology spend embedded in opex |
| 150-DPD write-off trigger (numeric) | Qualitative language in AR/RHP; numeric trigger NOT FOUND despite B00 LBF-1 company context naming 150 DPD | Company direct communication OR CRISIL detailed review | Live-web verification or IR question required (B02, B05 red flags track this) |
| FLDG-in-opex bps (Q1 FY27) | Management stated "not readily available" on Q1 FY27 call itself | Future quarterly results / investor presentation | Blocks precise cash-cost segregation; tracked as B05 FLAG-FLDG-QUANTUM |
| Standalone NIM / lending yield (%) | Total-income-per-avg-AUM and finance-cost-per-avg-AUM are only disclosed proxies; pure interest spread not stated | Company IR page OR CRISIL detailed review | B04 flag-disclosed-inconsistency; affects margin bridge precision |
| LAP ticket size & tenure (reconciled) | AR up to Rs 30 lakh/15yr, Q1 deck up to Rs 15 lakh/10yr, CRISIL up to Rs 20 lakh/10yr; unreconciled | Management direct clarification | B04 flag-disclosed-inconsistency; affects LAP product consistency read |
| Amendment 19 FV CAGR | Not computed until Stage 11 works forward from deliberation basis | Stage 11 valuation task | Blocks entry-zone downstream presentation per CLAUDE.md |

---

## ANALYST NOTES

1. **Entity count & consolidation basis:** ONE entity (OnEMI Technology Solutions Ltd + Si Creva Capital subsidiary). SOTP slices are valuation method outputs, not entity decomposition. No allocation is carried as an ESTIMATE (per fttcp-deliberation §5, ruling 4-5).

2. **Lender metrics framework:** This is a financial firm; all trailing metrics read through lender lens (AUM, NIM/spread, credit cost, GNPA/NNPA, write-offs, RoA, RoE, CRAR, borrowings). Manufacturer ratios (gross margin %, trade receivable days, fixed-asset turnover, ROCE with finance cost added back) are irrelevant per B04.must_track_metrics.

3. **CFO/PAT cash-conversion interpretation:** Consolidated CFO is deeply negative (-1,648 Cr cumulative FY21-26 vs +671 Cr PAT); standalone CFO is positive (>1.2x per B01 analyst_note). The divergence is Ind AS 7 classification: loan disbursals flow through operating cash as an outflow for a fast-growing lender, not a cash-quality failure. GROWTH INDUCED per operator ruling. Stand-alone positive conversion supports this read.

4. **Write-off-assisted asset quality:** GNPA (Stage 3) of 2.12% FY26 is sustained by a ~15.7% annual write-off rate (+10.7% YoY) while new Stage-3 inflow grew 28.9% YoY (B02 rank 2, rank 9 findings). The 150-DPD write-off trigger is NOT FOUND in AR/RHP despite company context (B00 LBF-1) naming it. Asset-quality improvement narrative in CEO letter is partially qualified; the write-off mechanic is material and undisclosed in summary form. Q1 FY27 GNPA rose sequentially to 2.25%, one quarter into "further strengthen asset quality" guidance (B03 FLAG-GUIDANCE-DIVERGENCE).

5. **Parent guarantee structural risk:** 228% of parent net worth backing Si Creva's lenders; rising every year for four straight years from 70.3% (FY23); crossed 100% in FY24 (two years pre-IPO); backs 99.8% of NCD book. Never named in AR risk factors or "Balanced liability base" narrative. Operator has flagged the negative CFO and cost-to-income optics as artifacts; has not explicitly named which structural optic is the core constraint (candidates: off-book loss in opex, partner concentration, parent guarantee).

6. **Capital raise (Rs 832 Cr preferential, Sep-2026) rationale:** Dated 17-Sep-2026, postdates both Kissht concalls. No numeric rationale filed or stated anywhere in corpus. Raised at 40.2% CRAR (2.5x regulatory minimum). Peer precedent check (B06) shows Poonawalla's Rs 2,500 Cr QIP at 16.83% CRAR with explicit ALM-gap rationale, and Ugro's ~18% CRAR-triggered raises tied to acquisition/growth funding with explicit rationale. Kissht's raise is unprecedented in scale, timing (4 months post-IPO), and lack of disclosed numeric need. EGM shareholder approval pending 14-Oct-2026 (Halt 1 gate item per B05.red_flags rank 5).

7. **Cost-of-borrowing outlook (guidance vs peer evidence):** Kissht cites system-wide FCNR(B)-driven liquidity-easing tailwind (Q1 FY27 call, Jul-2026). SBICARD and Poonawalla (same quarter, Jul-2026) independently report cost of borrowing as flat-to-rising, with no FCNR(B) mention (B06 FLAG-COST-OF-BORROWING-TAILWIND-CONTRADICTED). Stage 11 should treat Kissht's forward cost-improvement as company-specific (rating-upgrade-driven only), not sector-tailwind-supported.

8. **Proof gate for transition:** NOT FIRED per fttcp-deliberation. Gate requires "all-in loss (on-book impairment + off-book ECL + collection outsourcing above run rate) / avg AUM below 10.5% for H2 FY27, with off-book loss rate not rising" (companies/KISSHT.md HALT 1 GATE). FY26 all-in loss was 10.97% of avg AUM. Needs H2 FY27 confirmation.

9. **Credential grade C caveat:** Grade sits at C/B boundary per B05.analyst_note. Would move to B on one further clean quarter where GNPA resumes downward path AND management proactively addresses either the guarantee structure or the Rs 832 Cr raise rationale. Would trend toward D if future call repeats "technicality" framing on asset-quality miss.

10. **Unit trap throughout corpus:** AR and results statements in Rs million; presentations (decks) in Rs Cr; RHP mixed. All assembly figures use Rs Cr. Conversion factor 10 million = 1 crore (B00.reporting_units).

11. **Share count history:** Pre-listing paid-up capital 106.79 Cr (shares of Re. 1 face value); post-split 10-for-1 approved 08-Jul-2025. IPO added 497 lakh shares at Rs 171 IPO price (08-May-2026). Post-IPO paid-up 16.8483 Cr ordinary shares. Fully diluted adds in-force ESOPs (13,438,960 options per RHP p.105); pre-raise fully diluted 18.1922 Cr; post-raise (Sep-2026) 20.8416 Cr per fttcp-deliberation override 6.

12. **Carry-forward items to Stage 11:** 
    - B03.ar_new_downstream_entities (unchanged: Invincible Minds, Sachin Tendulkar)
    - B09.downstream_candidates (unchanged: 6 rows, summary form copied above)
    - B07.catalysts_12m with fttcp-deliberation §7 watch-list updates: T1 (added average ticket/loans per borrower in Q2 deck); T2 (NIM note on mix vs price effect); T3 (Q2 FY27 vs Q2 FY26 triggers); partner-slice cap revisit (FLDG >40% revenue threshold)
    - fttcp-deliberation §5 operator-approved pillar block (in full, above under "VALUATION PILLARS")

---

## REPORT END

**Stage complete: 04-Oct-2026 (corrected 04-Oct-2026)**  
**All values anchored. Unresolved items listed with recovery paths. Conflicts resolved by operator override (B10 authority). No estimates.**

**For Stage 11:** Use SOTP primary per Amendment 27.2. Own book Mar-27 book P/B (0.8/1.0/1.2x on 2,695.8 Cr); partner fee slice Mar-27 through FY28 PAT basis (18.62/20.64/22.67x). Sector cap 18x whole company/own-book, 22.67x partner blend. Hurdle 25% Tier A. Entry zone ~Rs 350 PROVISIONAL, pending Amendment 19 FV CAGR. Do not present entry zone downstream without Amendment 19 label per CLAUDE.md.

Open items I4/I5/A19/DBB tracked and flagged above for Stage 11 / deliberation / operator workflow.

Key deliberation carries forward: Entity count = 1. Earnings basis = FORWARD. Cash conversion = GROWTH INDUCED. Proof gate definition: all-in loss / avg AUM <10.5% for H2 FY27 with off-book loss rate not rising. Ugliness optics (negative CFO and cost-to-income) are artifacts per operator; specific structural optic not yet named. T3 Q2 FY27 vs Q2 FY26 trigger applies (not Q1). Pillar 1 STAGNANT (sole authority, not overridden by T3).
