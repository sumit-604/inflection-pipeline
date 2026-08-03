# FTTCP handoff dossier: Indegene Limited (INDGN)

Machine-anchored archive for a separate FTTCP v1.2 deliberation session that will NOT have the source PDFs. Every figure carries a block or source anchor. Density over brevity. Frameworks: Master v3.3 / Section 1B v3.5.1 / FTTCP v1.2.

Run folder: runs/indgn-2026-08-03 | CMP Rs 545.25 | Market cap Rs 13,142 cr | Run date 2026-08-03 | Shares outstanding 24.09 cr (B10).
Business: asset-light life-sciences commercialization + medical/regulatory/digital operations services; NOT pharma manufacturer/CDMO/CRO (B04 flag; AR p.62 explicit management denial).
Evidence gate: PROCEED WITH FLAGS, confidence overall 79 (numerical 100, redflag 79, framework 93, peer 100). Valuation: BUY (on-dips). Devil's advocate: WEAKENED BUT ALIVE, valuation_safety DESTROYED.

Block map: B00 inputs, B01 gate0, B02 notes, B03 ARdeep, B04 bizmodel, B05 concall, B06 peers, B07 emoat, B08 promoter, B09 tam, B10 valinputs, B11 valuation, B12a Verifier A, B12b Verifier B, B12c Verifier C (gate0+EM), B12c-valuation Verifier C (phase 3), B12d Verifier D, B14 thesis, B15 devil, confidence.yaml delta, fttcp-deliberation.md authoritative.

---

## 1. Transition data series

### 1a. Topline

| Year | Revenue | Growth | Source |
|---|---|---|---|
| FY24 | Rs 2,589.6 cr | NOT FOUND (FY23 base not collected; pre-IPO restated) | B10 three_year_trend (screener Data_Sheet row 11) |
| FY25 | Rs 2,839.3 cr | +9.6% (2,839.3/2,589.6) | B12a B01 Revenue Growth check (screener; AR prior year) |
| FY26 | Rs 3,510.5 cr | +23.6% | B10 latest_financials (Consolidated P&L p.10); B12a ✓ CLEAN |
| Q1 FY27 | Rs 1,063.1 cr (quarter) | +39.7% YoY headline | B10 q1_fy27_interim (Q1 FY27 P&L p.4); B01 FLAG-GATE0 |

Organic constant-currency ex-M&A growth: Q3 FY26 18.3% -> Q4 FY26 12.0% (630 bps deceleration), headline Q4 32.8% inflated by BioPharm gross consolidation (B05 flags; B12a ✓ CLEAN). Revenue CAGR FY24-26 16.9% (B10); FY19-26 window 30.2% (B12a).

### 1b. Margin

| Year | Gross | EBITDA | Net | Source |
|---|---|---|---|---|
| FY25 | NOT FOUND | ~20% (FY25-era) | 14.3% | B11 forward path (FY25-era 20%); B04 PAT margin |
| FY26 | NOT FOUND | 19.1% (670.7/3,510.5) | 11.4% (401.1/3,510.5) | B10 latest_financials; B04 MD&A p.63 |
| Q1 FY27 | NOT FOUND | ~16.9% EBITDA / 16.4% operating | ~10.9% (116.2/1,063.1) | B07 F2 flag; fttcp-deliberation p.89; B10 q1_fy27 |

EBITDA basis note: B10 computes Rs 670.7 cr EBITDA (PAT 401.1 + tax 123.9 + interest 19.3 + D&A 126.4). B12a records a legitimate basis difference: Rs 619.0 cr computed excluding ESOP vs Rs 624.7 cr stated including ESOP (AR Note 38), 0.9% variance immaterial. FY26 net margin compressed from 14.3% (FY25) on litigation/other-income/D&A drag (B02; B04).

### 1c. Cash conversion

| Year | OCF | OCF/EBITDA | CFO/PAT | Debtor days (DSO) | WC % of sales | Source |
|---|---|---|---|---|---|---|
| FY25 | NOT FOUND | NOT FOUND | 1.09x | 72 days | NOT FOUND (WC days 84.6) | B02; B04 Inv.Pres slide 9; B01 |
| FY26 | Rs 650.8 cr | 0.97x (650.8/670.7) | 1.62x | 62-63 days | NOT FOUND (WC days 83.3) | B10; B02 p.173; B04; B01 block_b_trend |

Standalone CFO/PAT: FY25 0.71x -> FY26 1.63x (B02). FCF: FY25 Rs 411.9 cr -> FY26 Rs 606.5 cr (+47%) (B01; B10 fcf_cr). FCF/PAT FY26 1.51x (B10). Consolidated trade receivables +30.7% YoY (Rs 9,818 mn vs Rs 7,514 mn, Note 12 p.189-190); unbilled +77.5%; standalone receivables -31% (Rs 2,884 mn vs Rs 4,184 mn) (B02 receivables_trend). Capex FY26 Rs 44.3 cr (Consolidated Cash Flow p.12). WC days near-flat 84.6 -> 83.3, the only two comparable years (B01).

RATING AGENCY WORKING CAPITAL COMMENTARY (verbatim required): NOT FOUND. No credit rating PDF was collected this run (B00 rating gap MEDIUM; B10 unresolved credit_rating / rating_wc_cash_flow_commentary_verbatim). No agency working-capital or cash-flow verbatim quote exists in the input set; obtain the ICRA/CRISIL/India Ratings rationale from the agency or exchange filing to anchor FLAG-CASH downstream. Not estimated, not paraphrased.

### 1d. ROCE / ROE

| Year | ROCE | ROE | Capital-employed basis | Source |
|---|---|---|---|---|
| FY25 | NOT FOUND (M3 FAT 4.19x pre-BioPharm, would-be score 5) | NOT FOUND | Total Assets minus Current Liabilities (audited) | B01 M3; B01 data_notes |
| FY26 | 15.4% statutory / 25.8% operational | 12.8% | Total Assets minus Current Liabilities; operational strips 41.8% non-operating capital | B11 roce_base/roce_used; B10 roe_fye26; B01 |

FY26 statutory ROCE depressed by Rs 11.3 bn goodwill + Rs 4.8 bn intangibles from FY26 acquisitions (accounting/M&A effect, not model decline); underlying asset-light model intact (B01 M3; B10 roce_fye26_caveat). FY19-24 ROCE used proxy capital employed (Equity + Borrowings) as Data_Sheet lacks current/non-current split (B01 data_notes). FY20 ROE N/M (negative average net worth -15.49 cr, PAT loss); FY20 PAT -6.30 cr, positive from FY21 (B01). Pillar 1 verdict RECOVERING, probability 50-55%, catalyst Moderate (fttcp-deliberation; B10).

---

## 2. Catalyst inventory

From B05.triggers (8) and B07.catalysts_12m (6).

**T1 (B05 priority 1) Large outcome-based deal revenue realization** (top-10 pharma $10mn+ ACV, biotech $20mn TCV, Q3-won $10mn ACV omnichannel). Tier: documented. Window: near-medium (FY27, from Q2 FY27). Conviction H. Confirm: FY27 quarterly calls show revenue recognized on the stated go-live/lag schedule. Kill: further deferral, rescoping or non-mention in FY27 calls.

**T2 (B05 priority 2) EBITDA margin recovery toward ~20%.** Tier: claim. Window: medium (H2 FY27). Conviction M. Confirm: sequential adjusted EBITDA margin improvement confirmed Q1 FY27 with a restated explicit % target. Kill: Q1 FY27 margin flat/down again or target language dropped.

**T3 (B05 priority 3) Tectonic scale-up via largest-customer Germany beachhead.** Tier: documented. Window: medium (FY27). Conviction M. Confirm: additional Tectonic markets/customers named with revenue in FY27 calls. Kill: Germany stalls or no new markets by mid-FY27.

**T4 (B05 priority 4) Organic ex-M&A constant-currency growth reacceleration.** Tier: documented. Window: near (Q1 FY27). Conviction M. Confirm: organic growth returns above the Q3 FY26 ex-BioPharm 18.3% pace. Kill: organic stays near/below the Q4 FY26 12% print for two consecutive quarters (FTTCP falsification line).

**T5 (B05 priority 5) Beyond-top-20 client base compounding.** Tier: documented. Window: medium-long. Conviction M. Confirm: $1mn+ net adds reaccelerate from the Q4 FY26 +1 pace. Kill: net adds near zero for two more quarters.

**T6 (B05 priority 6) $10mn+ client cohort re-acceleration.** Tier: claim. Window: medium. Conviction L. Confirm: cohort count moves above 10. Kill: cohort flat through FY27.

**T7 (B05 priority 7) AI-as-TAM-expander (share gains from agencies/CROs).** Tier: inference. Window: long. Conviction M. Confirm: named competitive wins vs agencies/CROs, or peer-concall corroboration. Kill: peer concalls/industry data show AI compressing effort-based billing sector-wide including Indegene.

**T8 (B05 priority 8) Cake Kommunikations / European delivery build-out.** Tier: claim. Window: medium. Conviction L. Confirm: deal economics and integration milestones disclosed and met. Kill: continued non-disclosure alongside weak Europe/Tectonic traction.

B07 catalysts_12m (overlapping, with anchors): Tectonic beyond-Germany expansion (documented, Q4 FY26 call 30-Apr-2026); EBITDA margin recovery ~20% (claim, Q2/Q3/Q4 FY26 calls, H2 FY27); BioPharm synergy capture G&A/data/GTM (documented+claim, AR p.61, Q3 FY26 call, through FY27); TCPA settlement court approval (documented, Q4 FY26 call, near-term); $10mn+ ACV omnichannel deal revenue recognition begins (documented, Q4 FY26 call, H2 FY27); amortization step-down begins (documented, Q3 FY26 call, Q3 FY27 ~Rs 50mn/qtr).

---

## 3. Flags with complete underlying findings

### FLAG-PROMOTER: not active
B08 verdict TRUSTWORTHY (scorecard 6 clean, 4 caution, 0 red). No deal_breakers. No identified promoter; professionally + PE managed. transition_evidence: (1) FII+DII rose 7.63% (Jun 2024) -> peak 19.54% (Dec 2025) -> 18.66% (Jun 2026); (2) CA Dawn Investments (Carlyle/Brighton Park) fully exited 10.20% via three rising-price block trades (Rs 452 IPO May-2024, Rs 618 Dec-2024, ~Rs 591-592 Jun-2025) absorbed by Premji Invest affiliate, Capital Group, Societe Generale, Eastbridge, Abakkus; (3) two credentialed independent directors added Jan 2026 (Jill Mary De Simone, Neeraj Bharadwaj); (4) Audit Committee de-risked, ED Sanjay Parikh ceased AC membership 15-Jul-2026. Nadathur family office (Infosys-lineage) anchor since 2005. verdict_basis: no SEBI/criminal/SFIO/PMLA record found across 10 searches.

### FLAG-CASH: determination GROWTH-INDUCED, not structural (B02/B03/B10; FTTCP Pillar 2)
Cited items: consolidated OCF/PAT 1.62x (up from 1.09x, Cash Flow p.173); standalone OCF/PAT 1.63x (up from 0.71x); consolidated trade receivables +30.7% YoY (Rs 9,818 mn vs Rs 7,514 mn, Note 12 p.189-190); unbilled revenue +77.5%; standalone receivables -31% (Rs 2,884 mn vs Rs 4,184 mn) while standalone revenue +11.6%; billed DSO 72 -> 62 days (Inv. Pres. slide 9); ECL allowance reversal corroborated twice (Note 12, Note 21); WC days 84.6 -> 83.3. Determination growth-induced per FTTCP; Pillar 2 multiplier 1.30x, elite conversion, no growth offset in band. Capex commissioning timeline: NOT APPLICABLE, asset-light, capex Rs 44.3 cr / 1.3% of assets, no capacity build (B04; B09 capex_embedded 0). Receivables composition: build concentrated in BioPharm consolidation + large FY27-recognized deals (B05). RATING AGENCY VERBATIM QUOTE: NOT FOUND (no rating PDF; B00/B10). Falsifier: Q2 FY27 consolidated OCF/PAT below 1.0x with receivables ex-BioPharm outgrowing revenue ex-acquisition.

### FLAG-CONTINGENT-LIABILITY (B02/B03/B08)
Combined Rs 153 cr (Rs 1,531 mn): transfer-pricing proposed adjustment Rs 1,114 mn (AY2023-24, 21.2% of FY26 PBT, unprovided, contested via MAP, Note 33 p.204, Standalone Note 27 pp.162-165) + TCPA maximum settlement Rs 417 mn (provision recognized Rs 203 mn, Note 37 p.206). = 38.2% of FY26 consolidated PAT (4,011 mn), above the 25% threshold. TCPA: US District of New Jersey class-action, class certified 17 Jul 2025, tied to a discontinued FY19-20 fax-outreach practice; term sheet signed 25 May 2026, court approval pending as of Q1 FY27 note 6. CONTRADICTION: Board's Report Item 10 discloses a FINAL Section 144B tax demand of Rs 436.88 mn for AY2023-24 (income-tax demand u/s 156, Rs 43.69 cr incl interest) while Note 33 describes the identical AY as a pending DRAFT order with no final order received (B03; B08). Units note: earlier blocks wrote "Rs 1,531 cr"; corrected to Rs 153 cr = Rs 1,531 mn; B12a verified both components CLEAN; decision-neutral.

### FLAG-GOODWILL (B02/B03)
Goodwill + intangibles Rs 16,176 mn = 51.5% of consolidated net worth (Rs 31,387 mn); tripled +198% YoY. Same year, ECS CGU impairment-test discount rate fell 17.2% -> 12.5% and terminal growth rose from 2.4-4.9% to a uniform 5.0%, concurrent with Rs 6,429 mn new BioPharm goodwill landing in that CGU (Note 6 p.185, Note 7 pp.185-188). Contingent consideration liability grew Rs 152 mn -> Rs 2,914 mn (+1,817%), entirely Level 3 fair value, earnouts lapse FY27-28 (Note 16 p.192, Note 27a p.198). Carried, not valued into pillars.

### FLAG-GOVERNANCE (B03/B08)
ID K.V. Tenneti ~18-year tenure (appointed 22-Jul-2008), continuation approved by postal ballot under LODR 17(1A). Attendance gaps: Dzialga 60% board, Parikh 40% Audit Committee (seat ceased 15-Jul-2026), Bharadwaj 0% during FY26 tenure. Employee fraud (asset misappropriation) Rs 2.43 mn under CARO xi(a), fully recovered. Two self-reported MCA defects in remediation: ADT-1 filing chain defect (incoming auditor Deloitte, MCA GNL-1 pending, remediation filed 7-Jan-2026); RSU allotment timing deviation (exercise funds credited 11-Mar-2026 after allotment, USD 43.42, referred for adjudication/compounding, Board resolution 29-Apr-2026). All disclosed, bounded, non-integrity; verdict held TRUSTWORTHY.

### FLAG-GATE0 (B01/B10)
FY26 consolidated PAT -1.4% YoY (Rs 401.1 cr vs Rs 406.7 cr) despite +23.6% revenue and +11.1% EBITDA growth, continuing into Q1 FY27 (PAT -0.2% YoY on +39.7% revenue). Depressor detail: Rs 20.3 cr exceptional TCPA litigation provision; ~Rs 42 cr fall in other income; rising acquisition-related D&A (BioPharm/Warn/Cake). Standalone PAT +16.9% / EPS +15.6% (drag concentrated entirely in international/acquired subsidiaries). Mechanical FY19-26 CAGR scores (PAT CAGR 61.36%, +31.14pp vs revenue) do not reflect the single most-recent-year deceleration. Classification GOOD+ (not <=AVERAGE), so a carry-forward context flag, not a deal-breaker.

### SHARED-CATALYST (B10; B15)
Revenue growth on a fixed capital base drives BOTH Pillar 1 forward ROCE recovery AND the Pillar 3 +5x growth premium (3b moat +3x). Single point of failure; a stall trips both levers (destination toward 17-19x, real capital loss), a combined case neither B11 sensitivity 4E-a nor 4E-b models.

---

## 4. Credibility grade

B05 credibility_grade: B. Basis: delivery record genuinely evidenced (BioPharm integration completed ahead of schedule, DSO/cash conversion improving every quarter, no-guidance policy honored without exception) but capped below A by softening margin-recovery specificity (Q3 -> Q4 FY26), a never-addressed standalone-vs-consolidated PAT bridge despite FY26 PAT -1.4% on +23.6% revenue, and organic-growth deceleration (18.3% -> 12% YoY) not proactively flagged. B12b concurs "grade B at the low end". promise_delivery_score: 3 delivered / 5 partial / 0 missed. No-concall mode: false (Q2, Q3, Q4 FY26 earnings calls + Oct 2025 investor meet read directly).

repeated_evasions: (1) "What growth/revenue guidance can you give?" asked Q2/Q3/Q4 FY26, deflected every time but as an explicitly declared consistent policy, not concealment; (2) "When/how much will EBITDA margins recover?" asked Q2/Q3/Q4 FY26, answer changed between quarters, target/timeline specificity softened by Q4 FY26.

Guidance-versus-delivery (B05 promise_delivery.rows):
| Promised in | Promise | Outcome | Evidence |
|---|---|---|---|
| Q2 FY26 | 150bps EBITDA headwind, recovery to ~20%+ over 6-8 quarters | Partial | Margin +30bps QoQ Q3 FY26; Q4 reframes recovery to H2 FY27 without restating ~20% |
| Q2 FY26 / Oct 2025 meet | BioPharm support-function integration complete in 2 quarters (~Mar 2026) | Delivered (ahead) | Completed end-Feb 2026 per Q4 call |
| Q2 FY26 | Largest-customer pain behind us, bullish near-to-midterm | Partial | Still pipeline-stage Q3 FY26; Tectonic Germany landed at Q4 year-end, revenue to FY27 |
| Q3 FY26 | $10mn+ ACV omnichannel deal revenue starts Q2 FY27 (2.5-qtr go-live lag) | Partial (on track) | Q4 confirms deal live, revenue entirely in FY27 |
| Q2 FY26 | Tectonic 4 customers, $2mn H1 revenue, conversions by end-Dec | Partial | Q4 shows 5 customers, 2 scaled, Germany headline; slower net-add, higher quality |
| Q2 FY26 | Warn & Co not material to results | Delivered | Remained immaterial in later calls |
| Oct 2025 meet | BioPharm cost synergies ~$1mn p.a. | Partial | Reiterated Q3/Q4 as accruing FY27; not yet verifiable in numbers |
| All three calls | No formal revenue guidance (policy) | Delivered | Policy honored despite repeated analyst requests |

excuse_pattern: balanced, tilting honest-admission on hard/quantifiable misses (margin, PAT drivers, TCPA), mild deflection on softer optics (margin base-year math, organic deceleration, standalone-vs-consolidated bridge). B12b promise_delivery spot-checks: 5 checked, 5 confirmed, 0 wrong.

---

## 5. Scorecards and market sizing

### Gate 0 (B01)
Grand total 101/160; core_score 90/100; moat_score 11/60. Blocks: A 14, B 18, C 20, D 20, E 18. moats_confirmed 2/12. moat_class MODERATE. classification GOOD+. deal_breakers: none. history_downgrade false (data_years 8, FY2019-FY2026). E1 scored 3 on documented no-promoter interpretation (actual FII+DII 18.66%), per CLAUDE.md override on low institutional ownership. B12c note: M4 Customer Stickiness scored 3 vs M10 scored 1 on identical evidence (MAJOR); consistent conservative read moves moat_class MODERATE->THIN, classification GOOD+ -> GOOD; operator-resolvable, evidence-gate invariant.

### Emerging Moat (B07)
em_score 31 (B12c recomputed 30, classification unchanged). em_classification STRENGTHENING. active_categories: C1 Customer ecosystem/embedded (Strong, documented, active); C2 Customer concentration improving (Strong, documented, active); D1 Proprietary data asset (Strong, documented, active); D2 Digital platform (Moderate, documented+claim, 12-24m); F1 Talent density (Moderate, documented, active); G1 War chest (Moderate, documented, active); G2 WC improvement trajectory (Strong, documented, active); H1 Industry consolidation beneficiary (Moderate, documented+claim, 12-36m); A3 Process innovation (Moderate, documented+claim, ongoing). evidence_mix: documented 14, claim 12, inference 2 (9 active categories < 12 alarm threshold). combined_assessment EXCELLENT+ (GOOD+ backward + MOAT STRENGTHENING forward; tempered from EXCEPTIONAL by unproven margin-recovery F2). capex_embedded_growth_pct 0.

### Accounting quality (B02 = 7/10; B03 overall 6.5/10, components governance 6.5 / accounting 7.0 / balance_sheet 6.0 / earnings 7.0)
Top notes findings (rank, finding, note_ref, rating):
1. TCPA class-action provision Rs 203 mn, max exposure Rs 417 mn, not court-approved (Note 37 p.206, Note 17 p.193) red.
2. Transfer-pricing dispute Rs 1,114 mn AY2023-24, 21.2% of PBT, unprovided, pending MAP (Note 33 p.204, Standalone Note 27 pp.162-165) red.
3. Standalone PAT +16.9%/EPS +15.6% vs consolidated PAT -1.4%/EPS -2.5%; drag in international/acquired subs (P&L pp.172,137) red-yellow.
4. Goodwill+intangibles tripled to Rs 16,176 mn (+198%); terminal growth raised 2.4-4.9% -> uniform 5.0% same year (Note 6 p.185, Note 7 pp.185-188) yellow.
5. Contingent consideration Rs 152 mn -> Rs 2,914 mn (+1,817%), entirely Level 3 (Note 16 p.192, Note 27a p.198) yellow.
6. New cash-flow hedge program loss from inception (consol OCI -Rs 66 mn, standalone -Rs 79 mn); non-designated FX MTM balance-sheet position Rs 552 mn; actual FY26 P&L exchange loss Rs 79 mn (~1.5% of PBT) per B03 triple-pass correction (Note 27a pp.197-198) yellow.
7. Auditor change: Deloitte Haskins & Sells new FY26 statutory auditor, first-year in acquisition/litigation-heavy year (Auditor's Report p.169, Board's Report p.63, CARO p.135) yellow.
8. Standalone parent 86.8% dependent on Indegene Inc; Rs 3,993 mn intercompany loan to ILSL Holdings at SOFR+4% (Standalone Note 5 p.147, Note 9 pp.150-151, Note 27) yellow.
9. "Others" segment structurally loss-making two years; segment assets/liabilities not disclosed (Note 26 pp.195-196) yellow.
10. TriloDocs GmbH Rs 135 mn related-party convertible loan 100% written off within ~1 year; counterparty relationship NOT FOUND (Note 8 p.188) red.
11. CA Dawn Investments 10.2% shareholder fully exited; manner/timing NOT FOUND in notes (Note 15 pp.190-192, Note 13B p.284) yellow.
12. Two governance lapses: ADT-1 filing defect; RSU allotment before exercise funds (Board's Report/Secretarial Audit pp.69-70) yellow.
13. Cash conversion strong: consol OCF/PAT 1.62x (from 1.09x), standalone 1.63x (from 0.71x) (Cash Flow pp.173,138) green.
14. Cost structure grew faster than revenue: sub-contracting +78.7%, D&A +57.6%, other expenses +41.6%, trade payables +93.5%, unearned +98.6% vs 23.6% revenue; Basic EPS -2.5% (Notes 24,25,18,19,32 pp.194-196,204) yellow.
15. Dividend ~Rs 480 mn (~Rs 2.00/share) paid during FY26; FY26 proposed Rs 2.25/share is second consecutive annual payout (Cash Flow pp.173,138; Note 42 p.207) green.
going_concern_language: NONE (Nil borrowings, Nil gearing both years, Note 28). restatements: Brand Activation merged into ECS (FY25 restated, Note 20 p.194); Goodwill CGU relabel Omnichannel -> EMS (Note 6 p.185).

### Market (B09)
tam_cr conservative Rs 12,19,920 (USD 153 bn) / realistic Rs 15,11,640 (USD 189 bn). sam_cr Rs 8,53,325 (USD 107 bn, 56.4% of TAM). som_3yr_cr Rs 6,064 / som_5yr_cr Rs 8,301. runway_class MASSIVE (revenue headroom 243.1x). som_implied_revenue_cagr yr3 20.0% / yr5 18.8%. current_sam_share 0.41%. tam_growth 7.4%. mgmt_claim_cr Rs 11,93,400 (USD 135 bn), mgmt_claim_ratio 0.98 (CONSERVATIVE, not inflated). capacity_check sufficient (asset-light; required delivery headcount CAGR 13-21% within observed +13.4% YoY hiring; binding constraint domain-trained talent / 15.7% TTM attrition).

### Peer triangulation (B06)
verified: raw-material trend not applicable (15 anchors, all 4 peers); capex-cycle not applicable/NOT FOUND (15 anchors, all 4 peers).
partially_verified: GenAI as net TAM-expander vs compressor (IKS/eClerx/Sagility/Tata Elxsi); organic constant-currency decelerated sector-wide Jan-Mar 2026 (eClerx/IKS/Tata Elxsi, Sagility contradicts); $10mn+ conversion-cycle lengthening industry-wide (IKS/Sagility).
contradicted: Indegene's 6-8 quarter margin-recovery precedent ("we've done this before") vs peer cycles. Contradicting peers: IKS Health (AQuity beat timeline 3-4 quarters), Sagility (BroadPath drag absorbed within same fiscal year, beat guidance). Anchors: IKS Nov 2025 call, Sachin Gupta "we've probably arrived there perhaps three or four quarters ahead of when we had thought we would get there"; SAGILITY May 2026 call, Srinivas Mattapalli "performance came in ahead of the guidance we had shared during our last earnings call".
unverifiable: 5-8% pharma/life-sciences CAGR 2026-28 (no peer operates in pharma); RPE ~$75,000 leadership; EBITDA multiples paid by Sagility/eClerx for bolt-on M&A. net_narrative_effect: complicates.
B12b independent MAJOR (fully missed upstream): BioPharm consolidated at GROSS revenue (gross ~$38.1m vs net ~$29.2m) inflates INR headline growth, dilutes margin (Oct meet p.6, Q2 p.12, Q3 p.7, Q4 p.10).

---

## 6. Valuation pillar detail (B11; B10; fttcp-deliberation authoritative)

pe_basis: FORWARD (one-year forward P/E), operator ruling Decision 1. exit_pe_base_approved: 31.5x additive (RRM alternative 28.1x), operator-elected Decision 2.

### Pillar-by-pillar build
- Pillar 1 return: 25.8% operational (statutory alternative 15.4%); Route A operational governs, Route B suppressed per single-credit; non-operating capital 41.8% of capital employed stripped; base multiple 20.4x (0.5 x 25.8 + 7.5), within [9,24]. Return recovery credited via Pillar 1; strategic re-rating premium barred (verdict RECOVERING, probability 50-55%).
- Pillar 2 cash multiplier: 1.30x; structural_or_growth GROWTH INDUCED; elite conversion (CFO/PAT 1.62x, FCF positive); growth offset 0.
- Pillar 3 premium: +5x (3a +2x growth visibility [SOM 20% + grade B], 3b +3x moat formation [EM 31 STRENGTHENING], 3c +0x [no >=2.5yr order book]); within +6x cap.
- Strategic premium: +0x (no licence monopoly; pricing power moderate; re-rating barred).
- Undiscovered Alpha: NOT applied (institutions 18.66% vs <3% requirement; only 2 of 3 UA gates met).
- Sector cap row: Platform / SaaS / IT services, 45x (manifest Pharma/CDMO 38x is a collector defect; 31.5x < 45x, non-binding).

### Destination PE
- track1_rrm: low 26.0, mid 28.1, high 30.0; r_used 13.0, rrm 1.06 (build 26.5x x RRM; percentage-point reading 1+(13.5-13.0)x0.12=1.06).
- track2_additive: low 29.0, mid 31.5, high 34.0 (build C 26.5x + D 5x + E 0x).
- divergence 12.1% (< 15% materiality; both tracks carried; additive operator-elected governs). CMP inside BUY-on-dips band on both tracks so choice does not flip verdict.

### Hurdle and outputs
hurdle_ratio base 2.12, bull_used true, verdict PASS (Tier B threshold 1.728; also clears Tier A 1.953). SFL discipline: numerator FY27->FY30 EPS CAGR and denominator FY27 forward PE both on one FORWARD basis; forward-PE-at-exit convention (FY29 exit, destination on FY30 EPS).
Forward EPS ladder: FY26 actual 16.62 -> FY27 20.22 -> ... -> FY30 36.62 (B14).
DEVIL'S REBUILD (B15, carry prominently): on the no-margin-recovery bear FY27 EPS 17.51, forward PE 31.14x, EPS CAGR 15.5%, HR 1.56 < 1.728 = FAIL. PASS exists only because the assumed margin recovery is credited into both denominator and destination multiple.
fair_values track1 (RRM): bear 758, base 1029, bull 1243. track2 (additive): bear 850, base 1154, bull 1393.
expected_cagr_prob_weighted 27.4% (base case 28.4%). entry_range low 534, high 668. mos_price 534. upside_downside_ratio 10.0. cash_multiplier_used 1.30. structural_or_growth growth-induced. ua_applied false. sector_cap_used 45. decision BUY (on-dips), Tier B Medium 4-6% ceiling, staged Small->Medium, entry conjunction enforced.
Unresolved inputs used: forward_revenue_path base FY26->FY29 CAGR 17.1% (held below SOM 20.0%, conservative); forward_ebitda_margin base capped at FY25-era 20% (grade-B discount); tax_rate held at FY26 23.6% all years; forward_dna only documented amortization step-downs (Rs 50mn/qtr Q3 FY27, Rs 25mn/qtr Q3 FY28). som_cagr_crosscheck consistent.
Live sensitivities: SENSITIVITY-A treasury undeployable -> Pillar 1 20.4x->15.2x, destination ~19.8x, base FV ~Rs 725, combined-bear ~Rs 534 (CMP), caps verdict WATCHLIST/BUY-ON-DIPS. SENSITIVITY-B organic <=12% again -> revenue FIRING->STARTING, composite +5->+4, base drifts to bear ~Rs 850.

### FTTCP composite (fttcp-deliberation)
Composite +5 of 8, BUY-candidate band, standard conviction, Tier B Medium 4-6% ceiling. Transitions: revenue FIRING (backward+forward; 3-year-window uncertainty: backward 15% CAGR not positive would cap forward STARTING, composite +4), margin backward COMPRESSING / forward STAGNANT, cash backward+forward FIRING (growth-induced), capital efficiency backward TEMPORARILY DEPRESSED / forward RECOVERING (50-55%, Moderate). Operator overrides: Decision 1 FORWARD earnings basis; Decision 2 destination PE 31.5x additive over RRM 28.1x. Cross-family grade did NOT run (no GEMINI/GOOGLE key, exit 3 SKIPPED); FTTCP confidence held one notch below phase-1 79.

---

## 7. Gaps ledger

| Item | Stage/block needing it | Where to obtain |
|---|---|---|
| Credit rating agency + outlook | B10, FLAG-CASH anchor | ICRA/CRISIL/India Ratings press release or rating note (not in input set) |
| Rating agency working-capital/cash-flow verbatim quote | B10, Handoff 1c, FLAG-CASH/FLAG-CONTINGENT-LIABILITY | Working-capital section of the rating rationale |
| Standalone-vs-consolidated PAT bridge FY24-26 | B02/B05/B10 (FLAG-GATE0 explanation) | Next quarterly call detailed discussion or AR note reconciliation of subsidiary results |
| Tata Elxsi FY26 financials (screener CSV stale FY2015) | B06/B10 peer median (degraded to 3 peers) | MSEI/BSE latest quarterly results; Tata Elxsi IR website |
| IKS FY26 balance sheet (rows blank) | B10 peer EV/book-value (used FY25) | IKS IR FY26 annual results |
| Peer ROCE benchmarks (none disclose) | B10 peer relative-quality check | Peer annual reports / investor presentations (manual buildout) |
| Prospectus / DRHP restated pre-IPO financials (pre-May-2024) | B00/B01/B03 backward baseline (HIGH gap) | SEBI/exchange DRHP filing; FY19-24 currently screener RHP back-fill |
| Reg-30 announcements primary filings | B00 (LOW gap; operator digest non-anchored) | BSE/NSE announcement filings |
| TriloDocs GmbH counterparty relationship to Group | B02 (rank 10 red, 100% write-off) | Next AR related-party note / management Q&A |
| CA Dawn Investments exit manner/timing/price detail | B02/B03 | Block-deal disclosures / exchange bulk-deal data (partially in media) |
| Cake Kommunikations deal value / EBITDA multiple / integration timeline | B05 (least-disclosed acquisition) | Next AR business-combination note or concall |
| Whistleblower complaint count FY26 | B03 (only POSH count quantified) | Next AR / Board's Report |
| Consolidated/group auditor remuneration | B03 (only standalone disclosed) | Consolidated AR notes |
| Cross-family FTTCP grade | fttcp-deliberation (SKIPPED, no API key) | Re-run with GEMINI/GOOGLE key configured |
| Q2 FY27 margin print (the load-bearing catalyst) | B11/B14/B15 thesis resolution | Q2 FY27 quarterly results + concall (the falsifier) |

---

No publish drafting here. See fttcp-recommendation.md publish check for the flagged PUBLISH CANDIDATE (Hurdle double-credit teaching distinction; drafting deferred).
