# FTTCP HANDOFF DOSSIER - Fedbank Financial Services (FEDFINA)

Purpose: self-sufficient input package for manual FTTCP v1.2 deliberation in a separate session with no source PDFs. Every figure carries its source anchor. Assembled from blocks B00 to B15 (both B12c halves) and the stage reports; no re-analysis, no new figures.

Company: Fedbank Financial Services Ltd. Ticker: FEDFINA. Business type: lender (NBFC-ND-SI, gold loans plus LAP), Lender Transition Set. CMP Rs 164, market cap Rs 6,132 Cr, BVPS Rs 78.2, market P/B 2.09x, P/E 16.0x, ROE 12.6% (screener.in, 15 Jul 2026 close; manifest.yaml, fttcp-deliberation.md). Run date 2026-07-15. Finalize date 2026-07-16. Framework: Master v3.3 / Section 1B v3.3 / FTTCP v1.2.

Block reference index: B00 inputs, B01 Gate 0, B02 notes/accounting, B03 AR deep, B04 business model, B05 concall, B06 peers, B07 emerging moat, B08 promoter, B09 TAM, B10 valuation inputs, B11 valuation (Role 1), B12a numerical audit, B12b red-flag audit, B12c-framework (phase-1 Gate0+EM), B12c-valuation (phase-3 valuation/Role2), B12d peer audit, B14 thesis (Role 2), B15 devil (Role 3), confidence.yaml.

Authoritative overlay: fttcp-deliberation.md supersedes phase-1 determinations where they differ. Composite FTTCP 4 of 8, DEEP WATCH leaning BUY ON DIPS. Operator overrides: (1) CMP/sector cap recorded (Rs 164, Rs 6,132 Cr, Banks/NBFCs/MFIs 18x); (2) Pillar 2L asset-quality band flipped 0.80x to 1.00x, self-withdraws to 0.80x if Q4 FY26 credit cost breaks 1.1% or PCR thins further.

---

## 1. TRANSITION DATA SERIES

### 1a. Topline (Total Income, growth)

| FY | Total Income (Rs Cr) | YoY growth | Anchor |
|---|---|---|---|
| FY21 | 697.57 | NOT FOUND (no FY20 base) | RHP-prospectus p.113 KPI table |
| FY22 | 883.64 | +26.7% | RHP-prospectus p.113 |
| FY23 | 1,214.68 | +37.5% | RHP-prospectus p.113 |
| FY24 | 1,623.00 | +33.6% | annual-report.txt p.64 Financial Highlights |
| FY25 | 2,079.82 | +28.1% | annual-report.txt p.64 (ties to results-B.txt p.6 FY25 comparative) |
| FY26 | 2,226.61 | +7.1% | results-B.txt p.6 Total Income (II+III) |

Revenue CAGR FY21 to FY26 (5yr): 26.1% (computed, B01 / 01-gate0.md L114). 3yr CAGR FY24 to FY26: 17.3% (B10, rating.txt).

### 1b. Margin (gross, EBITDA, net)

| FY | Gross margin | EBITDA margin | Net (PAT) margin | Anchor |
|---|---|---|---|---|
| FY21 | NOT APPLICABLE (NBFC, no COGS) | NOT FOUND | 8.8% | PAT 61.68 / income 697.57 (01-gate0.md L105) |
| FY22 | NOT APPLICABLE | NOT FOUND | 11.7% | PAT 103.46 / 883.64 (L106) |
| FY23 | NOT APPLICABLE | NOT FOUND | 14.8% | PAT 180.13 / 1,214.68 (L107) |
| FY24 | NOT APPLICABLE | NOT FOUND | 15.1% | PAT 244.70 / 1,623.00 (L108) |
| FY25 | NOT APPLICABLE | NOT FOUND | 10.8% | PAT 225.18 / 2,079.82 (01-gate0.md L64-65, p.64) |
| FY26 | NOT APPLICABLE | 60.3% proxy | 15.4% | EBITDA proxy PBT 461.01 + finance cost 879.32 = 1,340.33 / 2,223.60 (10-assembly.md L104-106); PAT margin 15.43% results-B.txt p.7 |

Note: for an NBFC there is no gross margin or COGS line; interest expense is core operating cost, not a financing add-back (B04). Replace with net interest margin / spread: blended spread 8.6% at Q1 FY27 (B04 unit_economics); Gold yield ~17.8%, MT LAP ~12.0%, ST LAP/HL ~15.1%, cost of borrowings ~7.7 to 7.8% (B04). EBITDA proxy is only computable for FY26 in the run inputs; prior-year finance-cost splits NOT FOUND.

### 1c. Cash conversion

| FY | CFO (Rs Cr) | OCF/EBITDA | CFO/PAT | Debtor days | WC % of sales | Anchor |
|---|---|---|---|---|---|---|
| FY21 | (371.23) | NOT FOUND | (6.02)x | N/A (lender) | N/A (lender) | RHP-prospectus p.~394 restated CF |
| FY22 | (577.89) | NOT FOUND | (5.59)x | N/A | N/A | RHP-prospectus p.~394 |
| FY23 | (1,474.00) | NOT FOUND | (8.18)x | N/A | N/A | RHP-prospectus p.~394 |
| FY24 | (775.52) | NOT FOUND | (3.17)x | N/A | N/A | annual-report.txt p.170 FY24 comparative |
| FY25 | (977.52) | NOT FOUND | (4.34)x | N/A | N/A | annual-report.txt p.170 FY25 |
| FY26 | (1,664.16) | (1.24)x | (4.84)x | N/A | N/A | results-B.txt p.8; 10-assembly.md L88, L108 |

Cumulative CFO/PAT FY21 to FY26: (5.04)x; cumulative FCF/PAT (5.14)x; all six years FCF-negative (B01). Determination: STRUCTURAL and mechanical for a growing lender under Ind AS 7, not an earnings-quality failure (fttcp-deliberation.md item 9). Debtor days and working capital as a share of sales do not map to an NBFC; the loan book is the balance-sheet asset. Minor non-loan trade receivables: net fell 44.1% YoY (Rs 34.52 Cr to Rs 19.31 Cr) but the >6-month ageing bucket rose to 23.5% of gross from ~16.0% (B02 Note 7 p.189-190, Note 45 p.231).

Rating agency working-capital / liquidity commentary, reproduced VERBATIM (CARE Ratings, April 10, 2026, rating.txt p.3): "Liquidity: Strong - Per asset liability management (ALM) dated December 31, 2025, there are no negative cumulative mismatches across all time buckets. As on December 31, 2025, the company maintained total liquidity of ~Rs 8,379 crore comprising cash and bank balances of Rs 404 crore and liquid investments of Rs 386 crore. It also has undrawn sanctioned credit lines of Rs 1,352 crore and expected inflows from advances of Rs 7,589 crore in the next one year against scheduled repayments of Rs 4,519 crore. Liquidity is further supported by the gold loan portfolio, which forms ~45% of AUM and has a short behavioural tenor of 3-4 months, enabling quick churn. Overall, the company's liquidity profile appears adequate to meet debt obligations in the next one year."

### 1d. ROCE and ROE

| FY | ROCE | ROE | Basis / Anchor |
|---|---|---|---|
| FY21 | NOT FOUND | 8.08% | RHP-prospectus p.113 "Return on Average Equity" |
| FY22 | NOT FOUND | 10.41% | RHP-prospectus p.113 |
| FY23 | NOT FOUND | 14.36% | RHP-prospectus p.113 |
| FY24 | NOT FOUND | 13.54% | annual-report.txt p.64 |
| FY25 | NOT FOUND | 9.37% | annual-report.txt p.64 |
| FY26 | NOT FOUND | 12.6% | investor-presentation.txt p.31 "Return on Average Total Equity"; screener.in |

ROCE NOT FOUND every year: NBFC Ind AS balance sheet carries no current-liabilities line, so capital-employed ROCE is non-computable and structural (B01, B10). Capital-employed basis therefore not applicable. ROA: FY26 computed 2.28% (PAT 343.60 / avg assets 15,062.24, 10-assembly.md L100); rating.txt 9M FY26 annualised ROA 2.50%; other years NOT FOUND. Median ROE across the six years 11.5% (01-gate0.md L44).

---

## 2. CATALYST INVENTORY

### From B05.triggers (concall)

- Gold branch rollout to 150 branches FY26, AUM/branch maturation. Tier: documented (VOLUME). Window: near-medium. Conviction H. Confirm: Q4 FY26 branch count >=140-150 and AUM/branch rising past Rs 13.3 Cr. Kill: branch count stalls below ~130 or AUM/branch flatlines into FY27. (B05 triggers p1)
- Credit cost held inside 1% +/-10bps through FY26 exit, FY27 guidance given. Tier: documented (MARGIN). Window: near. Conviction H. Confirm: Q4 FY26 credit cost <=1.1% and an actual FY27 number given. Kill: credit cost breaches 1.1% or FY27 guidance deferred again. (B05 triggers p2)
- ST LAP collection in-housing completes and disbursement growth resumes. Tier: documented (VOLUME/COST). Window: near. Conviction M. Confirm: Q4 FY26 confirms in-house transition done and ST LAP disbursals rise meaningfully above Rs 208 Cr. Kill: completion date pushed again or disbursals stay flat. (B05 triggers p3)
- Cost-to-income inflects down in FY27 as branch/co-location investment matures. Tier: documented/claim (COST). Window: medium. Conviction M. Confirm: FY27 opening quarters cost-to-income materially below ~57%. Kill: cost-to-income stays flat or worsens into FY27. (B05 triggers p4)
- CRAR/Tier 2 capital raise executed as promised in H2 FY26. Tier: claim (COST). Window: near. Conviction L. Confirm: Q4 FY26 discloses a CRAR figure and confirms a Tier 2 raise. Kill: CRAR remains undisclosed or falls further with no raise. (B05 triggers p5)

### From B07.catalysts_12m (emerging moat)

- FY27 cost-to-income and credit-cost guidance. Tier: claim. Window: Q4 FY26 earnings call (~Apr-May 2026). Anchor: Q3 FY26 call p.16. (B07)
- Maturation of the FY26 150-gold-branch cohort. Tier: documented. Window: 9-12 months per branch through FY27. Anchor: Q2 FY26 call p.5; Inv. Pres. p.20-21. (B07)
- BRE credit-scorecard go-live confirmation (ST LAP). Tier: claim. Window: targeted Q3 FY26, unconfirmed. Anchor: Q1 FY26 call p.3. (B07)
- Tier-2 capital supplementation. Tier: claim. Window: H2 FY26. Anchor: Q2 FY26 call p.5. (B07)
- Stree Sakthi scheme scale beyond Rs 100 Cr. Tier: documented. Window: 12 months. Anchor: Inv. Pres. p.39. (B07)

Shared-catalyst note: credit-cost normalisation drives both the asset-quality transition (Pillar 2L) and the return transition (Pillar 1 ROE); a single Q4 FY26 print governs both (fttcp-deliberation.md ruling 12; B11 shared_catalyst_flag true).

---

## 3. FLAGS WITH COMPLETE UNDERLYING FINDINGS

### Promoter (verdict CAUTION; formal FLAG-PROMOTER not escalated, B08 flags empty)

Verdict: CAUTION. Scorecard clean 5 / caution 4 / red 1 (B08). Deal-breaker (borderline/qualified, recorded not enforced): near-total executive-layer turnover in ~18 months (MD&CEO, CRO x2, COO vacant, 2 CBOs, CS) reads in spirit like the multiple mid-term independent-director-exit trigger, though the two actual independent-director exits (Krishnamurthy, Shah) were scheduled 5-year statutory term completions.

Adverse findings (B08): (1) near-total senior executive turnover FY25-FY26 [VERIFIED, annual-report.txt L6647-6661, L7019-7044 + exchange filings, 2024-08 to 2025-08]; (2) Anil Kothuri MD&CEO exit reason stated inconsistently, "personal reasons" vs "pursuing other opportunities" [UNVERIFIED inconsistency, annual-report.txt L5223-5225, 2024]; (3) reported frauds totalling Rs 509.47 lakh to RBI/Board in FY25 [VERIFIED, annual-report.txt L5516-5526]; (4) heavy and growing RPT dependency on Federal Bank, FY26-27 approved RPT ceiling Rs 4,459 Cr vs FY25-26 turnover Rs 2,227 Cr (~2x), includes Brand Usage Charges Rs 244 lakh [VERIFIED, annual-report.txt L6215-6299 + postal ballot]; (5) Federal Bank high volume of minor RBI penalties/caution letters over 5 years plus one PMLA warning and one FEMA penalty, all resolved [VERIFIED, RHP-prospectus.txt L3787-3839]; (6) two immaterial paid exchange fines, NSE Rs 10,620 on Federal Bank, BSE Rs 10,000 on FEDFINA [VERIFIED, RHP L32785-32791; AR L5493-5508].

Transition evidence (B08): new external MD&CEO Parvez Mulla, 29-year BFSI career, hired via NRC (annual-report.txt L5231-5234, 2024-11); Nomura India Equity Fund bought True North's entire 6.8644% via block deal Rs 385.4 Cr, muted reaction (2026-05-12); promoter pledge confirmed nil across FY26 via exchange encumbrance filing (2026-04-08); three new independent directors with verifiable credentials (Sonal Dave, Mona Bhide, Muralidharan Rajamani, FY25); 99.97% minority approval of the FY26-27 material RPT resolution (2026-06). Pledge latest: 0%; trend nil since IPO Nov-2023. Verdict basis: no SEBI ban, criminal conviction, SFIO, PMLA-with-assets, pledge, auditor resignation or restatement; decisive adverse finding is concentrated executive-layer turnover, offset by credible replacements and governance-renewal momentum.

### FLAG-CASH (STRUCTURAL, active)

Determination: STRUCTURAL and mechanical, not a cash-quality failure (fttcp-deliberation.md item 9; B10). Cited items: cumulative CFO/PAT (5.04)x and FCF/PAT (5.14)x across FY21-FY26, all six years FCF-negative (B01); loan disbursement is an Ind AS 7 operating outflow financed by financing inflows, cash pile grew (B03). Operating profit before working-capital changes grew 25.5% YoY (B03). Genuine non-structural earnings-quality item: direct-assignment gain-on-sale income rose to ~50% of PBT in FY25 from ~28% in FY24 (rating.txt p.2), now wound down (9M FY26 DA income Rs 1 Cr vs Rs 62 Cr in 9M FY25, B05). Receivables composition: net non-loan trade receivables Rs 19.31 Cr (fell 44.1% YoY), >6-month bucket 23.5% of gross (B02 Note 7 p.189-190). Capex commissioning timeline: NBFC has no plant capex; branch leasehold buildout is the analogue, FY26 tangible capex Rs 27.61 Cr (results-B.txt p.8). Rating agency verbatim liquidity quote reproduced in Section 1c above (CARE, rating.txt p.3). Valuation treatment: no cash multiplier penalty; Pillar 2L used (B11 cash_multiplier 1.00).

### FLAG-GATE0 (active)

Grand total 48/160, core 38/100, moat 10/60, classification AVOID (B01). Blocks: A 0/20, B 0/20, C 20/20, D 8, E 10. Moats confirmed 2, moat class MODERATE. Depressor detail: Block A ROCE not computable (no current-liabilities line in NBFC Ind AS balance sheet) and median ROE 11.5% below the 12% threshold; Block B CFO/FCF negative every year FY21-FY26 (Ind AS 7 structural); both apply across the full window, not a single year. Block C revenue CAGR 26.1%, PAT CAGR 41.0%. Block D CRAR 20.71% latest. Genuine non-structural depressors: PCR 40.0% (FY25) to 32.29% (FY26); credit cost 1.8% of avg assets FY25 (from 0.7% FY24); PAT dipped FY24 to FY25. Deal-breakers triggered: DB1 (Block A <8), DB2 (Block B <8), DB4 (cumulative CFO/PAT (5.04)x <0.50). Phase-1 verifier note (B12c-framework): strict M1 handling would move moats confirmed 2 to 1, class MODERATE to THIN, grand total 48 to 43; classification AVOID unchanged.

### FLAG-ASSETQUALITY plus FLAG-ASSET-QUALITY-OVERRIDE (active)

PCR thinned 40.0% (FY25) to 32.29% (FY26) to 38.36% (Q1 FY27); FY25 credit cost 1.8% of avg assets; mortgage-segment GNPA ~3.4-3.8% vs gold 0.1-0.3% (B01, rating.txt p.3). Impairment +228.6% YoY, Rs 65.85 Cr to Rs 216.36 Cr (B02 Note 32 p.208). Stage 3 gross-loan figure unreconciled across three notes: Rs 19,042L vs Rs 23,888L vs Rs 26,602L (B02 Notes 48.09/48.30(A)/8.3(a)/8(d)). Override: Pillar 2L lifted 0.80x to 1.00x (Sound band) by operator during deliberation; the 1.00x band nominally wants PCR 60-70%, FEDFINA is 32-38%; override rests on the 99% secured mix and three in-band credit cost quarters, not coverage depth. Self-withdraws to 0.80x if Q4 FY26 credit cost breaks 1.1% or PCR thins further (fttcp-deliberation.md override 2; B11).

### FLAG-Q4-FY26-DATA-GAP (active)

Q4 FY26 result filing (out 29 Apr 2026 per ICICI note) not in run inputs; full-year FY26 IS anchored, the Q4 quarter breakout is not. Non-anchored ICICI claims: credit cost 0.6%, RoA 2.6%, RoE 14% (B10, fttcp-deliberation.md). Must be verified against the actual filing before the 1.00x band or the RoA recovery can be confirmed.

### Other B11 flags

FLAG-EMOAT-BORDERLINE (EM 25.3 bottom edge of STRENGTHENING; Pillar 3 +1x). FLAG-GUIDANCE-SLIPPAGE (ST-LAP in-housing slipped Q2 to Q3 to Q4; CRAR/Tier 2 disclosure dropped Q3; ST-LAP scorecards and MT-LAP BRE pilot silently dropped). SHARED-CATALYST (credit-cost normalisation drives Pillar 1 and Pillar 2L; Role 3 stress-tested).

---

## 4. CREDIBILITY GRADE

B05 credibility_grade: B (full concall mode, three actual transcripts: Q1, Q2, Q3 FY26). Basis: headline turnaround metrics delivered cleanly (credit cost inside 1% +/-10bps every quarter, full secured-mix transition, DA reduction) with honest unprompted self-blame, offset by two dated technical commitments silently dropped, collections in-housing slipped two quarters, and CRAR/Tier 2 disclosure disappearing when leverage rose most. Promise delivery: delivered 6, partial 3, missed 5. Excuse pattern: balanced.

Repeated evasions (B05): (1) "When will ST LAP/collections rebuild become predictable?" asked Q1/Q2/Q3, deflected every time, timeline slipping Q3 to 6-months-out to Q4/FY27; (2) "Given the fully secured book, will you raise credit-cost guidance?" asked Q2/Q3, deflected every time; (3) "What geographies/segments show elevated stress?" asked Q1/Q3, answered eventually.

Guidance versus delivery (B05 promise_delivery rows):
- Q1 FY26: 100% assignment of Rs 770 Cr BL portfolio this quarter -> DELIVERED (executed and derecognized same quarter).
- Q1 FY26: credit cost 1% +/-10bps FY26 -> DELIVERED (0.8% Q1, 0.9% Q2, 0.9% Q3).
- Q1 FY26: collections leadership/field hiring complete by early Q2 -> MISSED (still building Q2, 200 to 400 headcount; Q3 still targets Q4).
- Q1 FY26: ST LAP credit scorecards/BRE by Q3 FY26 -> MISSED (never mentioned again).
- Q1 FY26: 100-150 new gold branches FY26 -> DELIVERED (113 cumulative through Q3).
- Q1 FY26: reduce DA income reliance -> DELIVERED (9M FY26 DA Rs 1 Cr vs Rs 62 Cr 9M FY25).
- Q1 FY26: gold mix settles 45-49% -> DELIVERED (Q3 ~45.2%).
- Q2 FY26: supplement Tier 2 capital H2 FY26 -> MISSED (Q3 no CRAR, no Tier 2 update).
- Q1 FY26: steady rise in ST LAP activity -> PARTIAL (disbursals nearly flat Q2 to Q3, Rs 206 Cr to Rs 208 Cr).
- Q2/Q3 FY26: cost-to-income flat FY26, improving FY27 -> PARTIAL (Q2 improved 136bps to 56.9%, Q3 worsened ~10bps, net flat).
- Q1/Q2 FY26: GNPA moves up and down, credit cost managed -> DELIVERED (Gross Stage 3 rose to 2.1% Q3 from 1.9%, credit cost 0.9%).
- Q1 FY26: follow up on geographic branch-mix disclosure error -> MISSED (never revisited).
- Q2 FY26: co-locate 75-80 branches -> PARTIAL (63 cumulative by Q3).
- Q1 FY26: MT LAP BRE/scorecard pilot planned -> MISSED (no follow-up).

Verifier B (B12b) concurs B is fair but at the low end; promise-delivery spot-checks 5 of 5 confirmed; four MAJOR concall misses surfaced (asset-quality disclosure opacity, ~30% cure rate, gold-mix ceiling walkback, gold growth ~90% price not tonnage).

---

## 5. SCORECARDS AND MARKET SIZING

### Gate 0 (B01)

Grand total 48/160; core_score 38/100; moat_score 10/60. Blocks: A 0/20, B 0/20, C 20/20, D 8, E 10. moats_confirmed 2/12. Classification AVOID. Deal-breakers: DB1 Block A <8 (structural NBFC ROCE N/A full window); DB2 Block B <8 (structural NBFC CFO classification full window); DB4 cumulative CFO/PAT (5.04)x <0.50. Data years 6 (FY21-FY26). History downgrade false.

### Emerging Moat (B07)

em_score 25.3 (B10) / 25 (B07 rounded); em_classification STRENGTHENING (bottom edge). Active categories with evidence_mix (documented 19, claim 12, inference 7): C2 customer concentration improving (Moderate, documented); D2 digital platform (Moderate, documented); F2 execution moat (Strong, documented, 3 quarters, FY27 test pending); G1 war chest / funding cost (Moderate, documented); H2 strategic partnerships Federal Bank / co-lending (Moderate, documented); R1 regulatory/policy tailwind RBI gold-loan framework (Moderate, documented, industry-wide). capex_embedded_growth 12.6%. Combined assessment TURNAROUND. Verifier C (B12c-framework) MAJOR notes: E1 multiplier 1x0.5 recorded as 1.0 (em 24.8 to 25.3, boundary); F2 graded 4.0 on self-derived record with B05 feed absent, a 0.7x haircut flips to MODEST.

### Accounting quality (B02)

accounting_quality 7/10. Top findings with note_ref and rating: (1) impairment/credit-cost +228.6% YoY Rs 65.85 Cr to Rs 216.36 Cr, primary PAT-decline driver [Note 32 p.208, Red Flag]; (2) NPA vintage Doubtful 1-3yr +292.6% Rs 8.83 Cr to Rs 34.67 Cr, Doubtful >3yr newly Rs 0.45 Cr [Note 48.30(A) p.248-249, Red Flag]; (3) FVOCI-book Stage 3 loans +2,027.5% Rs 3.35 Cr to Rs 71.27 Cr [Note 8(d)/(f), 44.1.2(b) p.192-193,227, Red Flag]; (4) customer complaints +897.3% (37 to 369), foreclosure-letter complaints +1,508% [Note 48.17 p.242-243, Red Flag]; (5) Standard-asset (Stage 1&2) provisioning +792.7% Rs 8.26 Cr to Rs 73.73 Cr, Ind AS-over-IRACP buffer 7.1x [Note 48.15/48.30(A) p.243,249-250, Red Flag]; (6) funding mix shift to short-tenor on-demand +331.6%, CRAR -23.46% to 21.92%, ALM >1yr swung to -Rs 529.27 Cr [Note 17/42/48.29-31, Watch]; (7) Federal Bank RPT intensified (term loans +39.9%, interest paid +71.8%), new Brand Usage Charges Rs 2.44 Cr [Note 39.2/39.3 p.216-217, Watch]; (8) DA income +66.9% Rs 91.24 Cr to Rs 152.31 Cr, upfront, retained interest 5%/10% [Note 26/48.04, Watch]; (9) real estate exposure Rs 5,616.05 Cr, 47.4% of gross book [Note 48.08 p.238, Watch]; (10) restructured book 89.9% resolved via write-off not cure [Note 49 p.252, Watch]; (11) mid-year statutory auditor transition disclosed only via remuneration footnote [Note 34.1 p.209, Watch]; (12) interest-rate sensitivity worsened 24.5%, +25bps cuts PAT Rs 11.19 Cr [Note 44.3.2 p.229, Watch]; (13) Stage 3 gross-loan figure unreconciled across three notes Rs 19,042L/23,888L/26,602L [Notes 48.09/48.30(A)/8.3(a)/8(d), Watch]; (14) gold-loan 90-day rebuttal kept Rs 77.56 Cr of 90+DPD out of Stage 3 [Note 48.28/48.30(B), Watch]; (15) gross write-offs -14.0% YoY even as provisioning surged [Note 50 p.252, Clean/Positive]. Going concern: NONE. Restatements: Note 59 p.258 vague boilerplate regrouping, not quantified.

### Market (B09)

tam_cr conservative Rs 23,10,000 Cr / realistic Rs 29,00,000 Cr; sam_cr Rs 12,48,000 Cr (54% of TAM); som_3yr_cr Rs 39,900 Cr; som_5yr_cr Rs 68,600 Cr; runway_class MASSIVE; som_implied_revenue_cagr yr3 23.6% / yr5 26.6%; current_sam_share 1.7%; revenue_headroom 59.1x; mgmt_claim_cr Rs 92,00,000 Cr; mgmt_claim_ratio 4.0x; mgmt_claim_read inflated (FY23-vintage all-India MSME credit gap, far broader than the gold+LAP niche). Capacity check: SOM 5yr implied 26.6% AUM CAGR exceeds B07 12.6% branch-capex-embedded growth by ~Rs 9,730 Cr (yr3) / ~Rs 30,340 Cr (yr5); achievable only via per-branch productivity and Federal Bank co-lending/DA funding, flagged as a funding-capital dependency for stage 11. Status: B09 partial (CRISIL/ICRA PDFs 403-blocked; secondary sourcing).

### Peer triangulation (B06)

Peers provided 4 (Manappuram, MAS Financial, SBFC, Five-Star), 15 peer-quarter files. Verified: sub-Rs5L/Rs5-7L ticket LAP stress consistent with MFI-sector spillover [Five-Star, SBFC, MAS, 4 anchors]; Fedfina cost-to-income ~56-57% materially above peers [SBFC, Five-Star, MAS, 3 anchors]. Partially verified: Muthoot/Manappuram ~20% gold-AUM benchmark vs Fedfina 25% guidance/52% Q3 [Manappuram]; conservative-LTV/mix-driven yield logic [Manappuram]; MT-LAP yield compression industry-wide [SBFC]; comparable FY26 branch-capex cycle [SBFC, Five-Star, MAS]; DA-to-co-lending accounting shift effective Jan 1 2026 [MAS, SBFC]. Contradicted: peers report elevated Maharashtra/Tamil Nadu MSME-LAP stress matching Fedfina [contradicted by Five-Star "TN NPA sub-1.5%, performing very well", SBFC "TN not very large, stress is Karnataka", MAS "CV stress Rajasthan/MP"]; industry gold tonnage 10-15% comparable to Manappuram [contradicted, Manappuram Feb 2026 "tonnage 58.9 up 3.2% QoQ, 2.8% YoY"]. Unverifiable: none. Net narrative effect: complicates. Verifier D (B12d): 15/15 peers substantive, 100% utilisation, 2 MINOR presentational notes.

---

## 6. VALUATION PILLAR DETAIL (Stage 11 ran; B11)

Both tracks. Destination PE Track 1 (RRM): low 13.0x, mid 14.3x, high 15.5x; r_used 13.5, rrm 1.00. Track 2 (additive): low 14.0x, mid 15.3x, high 16.5x. Divergence 7.0%. Governing track: Track 1 RRM (more conservative); both mid points below current ~16-18x (de-rating headwind).

Pillar build (B11 pillar_detail): roce_used 13.56 (roce_base 12.6, recovery route pillar1-midpoint; Pillar 1 on ROE per Section 1B Amendment 7, 0.5 x ROE + 7.5, floor 9x cap 24x, RECOVERING 40-60% uses 60/40 blend of current 12.6% and FY[Y+2] expected ROE). cash_multiplier 1.00 (structural lender, FLAG-CASH structural per Ind AS 7, no penalty, Pillar 2L applied). growth_offset 0. growth_premium +1. strategic_premium +0 (optional +1x Federal Bank backing left open). shared_catalyst_flag true. ua_applied false (UA fails: FII 0.66% + DII 18.82% = ~19.5% >> 3%, B10). sector_cap_used 18 (Banks/NBFCs/MFIs).

Pillar 2L asset-quality band 1.00x (Sound, operator override; self-withdraws to 0.80x if Q4 FY26 credit cost >1.1% or PCR thins). structural_or_growth: structural.

Hurdle: base ratio 1.21, bull_used true, verdict STOP (against required 1.953, Tier A 25% hurdle).

Fair values: Track 1 bear Rs 117 / base Rs 150 / bull Rs 186; Track 2 bear Rs 122 / base Rs 156 / bull Rs 193. expected_cagr_prob_weighted -3.1%. upside_downside_ratio 0.47. entry_range Rs 68 to 77. mos_price Rs 61. decision AVOID (on valuation).

Unresolved inputs used (B11): FY[Y+2] expected ROE 15.0% (ROA ~2.55% x leverage ~6.0x; rating ROA 2.50%; capped below peer best, conservative); cost of equity 13.5% (small/mid NBFC base 13-14%, AA+ parentage offset by governance CAUTION and asset-quality flags); Pillar 2L 1.00x carried from override with self-withdraw. SOM cross-check: consistent, base EPS CAGR 15% and implied revenue CAGR ~15-17% sit below B09 SOM-implied 23.6% (3yr), no cut needed. Verifier C phase-3 (B12c-valuation): 56 rules, recomputed destination PE and decision concur exactly, 0 CRITICAL/MAJOR, 1 MINOR (Amendment 4.3 first-line Tier/Hurdle label absent), acceptance 98%.

One-line Role 1 thesis (B11): AVOID FEDFINA at Rs 164: a 12.6% ROE (approx CoE 13.5%, near-zero economic spread) recovering NBFC already priced at 2.09x book / ~18x earnings, whose earned four-pillar destination PE of 14-16x sits BELOW the current multiple, so the Hurdle Ratio is STOP and probability-weighted 3-yr CAGR is -3.1%; entry only at Rs 68-77 (MoS Rs 61).

Role 2 (B14): verdict AVOID; entry Rs 68 to 77; position size Small; thesis_broken_if Q4 FY26 credit cost >1.1% OR ROE fails to cross 14% by FY28 OR PCR thins below 32%.

Role 3 (B15): overall SURVIVES. Dimensions: growth_triggers weakened, moat_durability weakened, management_trust weakened, valuation_safety survives. Top counter: ROE ~12.6% approx CoE 13.5% (negative economic spread); justified P/B 0.9-1.2x vs market 2.09x, so even the bull's most optimistic non-anchored ROE 14-16% implies ~1.0-1.2x book, stock ~1.8-2x its own justified value; AVOID survives the symmetric Type II test.

---

## 7. GAPS LEDGER

| Item | Stage/block needing it | Where to obtain |
|---|---|---|
| Q4 FY26 standalone quarter filing (credit cost, RoA, RoE) | B10, B11 Pillar 2L self-withdraw; falsification | BSE/NSE exchange filing 29 Apr 2026; company results |
| FY-wise ROE/ROA series FY21-FY26 | B11 Amendment 9 Route B (pre-cycle normalized ROE) | Annual Reports FY21-FY26; investor presentations |
| FY[Y+2] expected ROE (Pillar 1 60/40 blend input) | B10, B11 | Analyst consensus; management FY27/FY28 guidance |
| Cost of equity | B11 (P/B = ROE/CoE) | 10Y GSec, market risk premium, NBFC beta regression/proxy |
| FII + DII shareholding split | B10 UA qualifier | NSE/BSE Reg 31 LODR shareholding pattern (latest quarter) |
| Reg 30 / exchange announcements feed | B05, B07, B08, FTTCP Step 0C | BSE/NSE announcements; company disclosures |
| FEDFINA screening CSV / price history | zone reachability; 52-week range | screener.in export; exchange historical price data |
| Segment-level (Gold vs Mortgage) RoA/RoE/cost-to-income | B04, SOTP tertiary method | Company segment disclosures; future AR/investor deck |
| Stage 3 gross-loan reconciliation bridge | B02, B03 | FY26 AR notes succeeding 48.09/48.30(A)/8.3(a)/8(d) |
| Muthoot transcript (Q1 check-peer) | B06 (Q1 capped PARTIALLY VERIFIED) | Muthoot Finance concall transcript, matching quarter |
| Fedfina disclosed portfolio LTV | B06 (Q2 LTV-conservatism test) | Company investor presentation; concall |
| ST LAP old vs new book split, Stage 2 balances, collection efficiency | B05, B12b (withheld twice) | Q4 FY26 concall; company asset-quality disclosure |
| Promoter COO successor name (seat vacant) | B08 | Exchange filing on KMP appointment |
| CRAR / Tier 2 raise disclosure (dropped Q3) | B05, B01 | Q4 FY26 results; capital adequacy disclosure |
| Direct CRISIL MI&A / ICRA market-size PDFs (403-blocked) | B09 | CRISIL/ICRA subscription reports |
| FY26 AR Note 53 contingent liabilities (not yet published at run) | B01 E4 | FY26 Annual Report when filed |

Non-anchored leads (weigh, never anchor): ICICI Securities notes 29 Jul 2025 + 29 Apr 2026 (credit cost 0.6%, RoA 2.6%, RoE 14% Q4 FY26; 52-week range low Rs 84); operator 6-month operational briefing (B00 operator_context_note).
