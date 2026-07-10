# FTTCP Handoff Dossier, Apex Ecotech Ltd (APEXECO)

Run date 2026-07-10. Purpose: a self sufficient input package for manual FTTCP v1.2 deliberation in a separate Opus session that will not have the source PDFs. Every figure carries its source anchor. NOT FOUND is the only valid fill for a missing cell. Frameworks: Master Project Prompt v3.3, Section 1B v3.3, FTTCP v1.2.

Identity snapshot: Apex Ecotech Ltd, ticker APEXECO, sector EPC / Civil construction (B00 manifest). CMP 242.0, market cap 319.0 Cr, diluted shares 1.319 Cr, net cash 33.75 Cr (25.60/sh), enterprise value 285.25 Cr (B10 company_identity). Listed SME board December 2024 (B10, B08). No credit rating (SME exempt, AR Boards' Report p.26; B03, B10). No concall mode false; 3 semi annual concalls plus 16 peer concalls read (B00).

Block index confirmed present: B00 inputs, B01 gate0, B02 notes, B03 ardeep, B04 bizmodel, B05 concall, B06 peers, B07 emoat, B08 promoter, B09 tam, B10 valinputs, B11 valuation, B12a numerical, B12b redflags, B12c framework (both halves: gate0+emoat phase 1, valuation phase 3), B12d peers, B13 synthesis, B14 thesis, B15 devil, confidence.yaml.

---

## 1. Transition data series

### 1.1 Topline

| Year | Revenue (Cr) | Growth % | Anchor |
|---|---|---|---|
| FY18 to FY21 | NOT FOUND | NOT FOUND | B01 fy_range FY18-FY26 but revenue not itemized pre-FY22 in blocks |
| FY22 | 19.5 | +67 | FTTCP deliberation Engine 1 table |
| FY23 | 34.6 | +77 | FTTCP deliberation Engine 1 table |
| FY24 | 53.08 | +53 | B10 revenue_cagr_anchor (screener FY24) |
| FY25 | 70.96 | +33.67 | B02 Note 14 p.56; B03 |
| FY26 | 148.65 | +109.5 | B10 revenue_anchor screener; B05 guidance |

### 1.2 Margin

| Year | Gross margin % | EBITDA margin % | Net (PAT) margin % | Anchor |
|---|---|---|---|---|
| FY22 | NOT FOUND | negative | NOT FOUND | FTTCP deliberation Engine 2 (EBITDA neg) |
| FY23 | NOT FOUND | 12.4 | NOT FOUND | FTTCP deliberation Engine 2 |
| FY24 | NOT FOUND | 16.7 (delib 16.8) | 12.5 | B09 flags EBITDA/PAT margin series; FTTCP delib |
| FY25 | ~31.1 (material 68.9%) | 15.6 (delib 15.7) | 12.1 | B04 flags material cost; B09; FTTCP delib |
| FY26 | ~24.4 (material 75.6%) | 14.6 (B10 calc 15.5) | 11.4 | B04 flags; B09; B10 ebitda_margin_pct 15.5 |

Note on EBITDA margin divergence: B09 reports the FY24 to FY26 series 16.7 / 15.6 / 14.6; B10 back solves FY26 EBITDA margin to 15.5 (EBITDA 23.04 Cr on revenue 148.65 Cr); FTTCP deliberation used 16.8 / 15.7 / 14.6. All three agree on the direction (three years of compression). Gross margin proxy = (revenue minus material cost) / revenue; material cost 68.9% FY25 to 75.6% FY26 (B04 flags), earlier years NOT FOUND.

### 1.3 Cash conversion

| Year | OCF (Cr) | OCF/EBITDA | CFO/PAT | Debtor days | WC % of sales | Anchor |
|---|---|---|---|---|---|---|
| FY22 | NOT FOUND | NOT FOUND | n/m | 65 | NOT FOUND | FTTCP delib Engine 3 |
| FY23 | NOT FOUND | NOT FOUND | 0.74 | 74 | NOT FOUND | FTTCP delib Engine 3 |
| FY24 | 6.69 | NOT FOUND | 1.01 | 60 (B02 implied 54) | NOT FOUND | B01 block_b_trend; FTTCP delib; B02 |
| FY25 | -5.24 restated (-14.08 orig) | -1.21 | -1.65 | 114 (B02 implied 79) | NOT FOUND | B01, B03; B10 cfo_fy25_restated; B02 |
| FY26 | 6.77 | ~0.29 | 0.398 (cum FY25-26 0.41) | 41 | ~41.5 (WC 61.72 / sales 148.65) | B10 cfo_fy26; B01 cumulative; FTTCP delib; B05 WC 61.72 |

Debtor days divergence: FTTCP deliberation records the receivable days series 65 / 74 / 60 / 114 / 41 (FY22 to FY26). B02 derives implied days from debtors turnover (6.77x to 4.61x, FY24 to FY25) as approximately 54 to 79 days (B02 Note 29 p.63). Both are carried; the deliberation series is operator confirmed and used forward, the B02 implied figures are the audited turnover derivation.

Rating agency working capital commentary, reproduced verbatim as required: "NOT PROVIDED — SME-listed companies exempt from mandatory credit rating. No rating agency or rating commentary available in inputs. FTTCP operator ruling: 'no credit rating exists to confirm it; no formal cash plan named.' Cash determination proceeds on AR evidence + peer + operator authority." (B10 rating_wc_quote, verbatim). No third party rating rationale exists to quote; the cash determination rests on AR evidence, peer corroboration, and the operator ruling.

### 1.4 ROCE and ROE

| Year | ROCE % (reported) | ROE % | Capital employed basis | Anchor |
|---|---|---|---|---|
| FY22 | negative | NOT FOUND | reported | FTTCP delib Engine 4 |
| FY23 | ~56 | NOT FOUND | reported, tiny pre listing base | FTTCP delib Engine 4 |
| FY24 | 59.61 (delib ~60) | ~60 | reported, tiny pre listing base | B02 Note 29 p.63; FTTCP delib |
| FY25 | 24.70 (delib ~25) | 28 | reported, inflated by idle IPO cash | B02 Note 29 p.63; FTTCP delib |
| FY26 | 33.39 | 22.9 | reported (Pillar 1 authority); ex cash operating ~77% context only | B10 roce_anchor / FTTCP operator ruling; B10 roe_pct |

ROCE forward verdict FIRING, sustain at premium, no further multiple expansion underwritten (FTTCP operator ruling). Ex cash operating ROCE approximately 77% is context only and not used in Pillar 1.

---

## 2. Catalyst inventory

From B05.triggers (concall) and B07.catalysts_12m (emerging moat). One block each. Tier: documented / claim / inference.

### From B05 triggers

1. Reliance Consumer Products order execution. Tier: claim. Window: near (0 to 6m). Conviction H (B05 priority 1). Confirm: continued on schedule conversion of the 100 to 125 Cr order into revenue with no dispute or delay. Kill: disclosed delay, dispute, or scope cut, or a customer concentration shock.
2. Order book to revenue conversion discipline (6 to 10 month gestation). Tier: claim. Window: near. Conviction H (B05 priority 2). Confirm: FY27 revenue tracks disclosed order book within the historical gestation window. Kill: gestation window slippage or a repeat of the order book figure confusion from the Q4 FY26 call.
3. ZLD / higher margin mix shift. Tier: claim. Window: medium. Conviction M (B05 priority 3). Confirm: a disclosed updated ZLD percent of revenue paired with margin expansion. Kill: continued margin compression despite bigger ticket sizes.
4. Raw material cost pass through on new orders. Tier: claim. Window: near. Conviction M (B05 priority 4). Confirm: stable or improving EBITDA margin in FY27 despite input cost volatility. Kill: renewed margin compression blamed on commodities with no price escalation clauses adopted.
5. Customer diversification beyond Reliance / L&T. Tier: claim. Window: medium. Conviction L (B05 priority 5). Confirm: disclosed top customer concentration metric showing declining reliance. Kill: continued non disclosure plus a second mega order in the same handful of clients.
6. ESOP delivery for core team. Tier: claim. Window: near (deadline already passed). Conviction L (B05 priority 6). Confirm: future disclosure confirming the ESOP was implemented. Kill: continued silence on the commitment.
7. International expansion (Vietnam / Indonesia). Tier: claim. Window: long. Conviction L (B05 priority 7). Confirm: a first disclosed order or revenue from outside India. Kill: continued retreat to India only focus.
8. Quarterly (numeric) financial disclosure. Tier: claim. Window: near. Conviction L (B05 priority 8). Confirm: a genuine move to numeric quarterly reporting, not a percentage only circular. Kill: continued semi annual only reporting into FY27.

### From B07 catalysts_12m

9. Completion of remaining ~30% Reliance order execution against the stated 70% within year target. Tier: claim. Window: 0 to 6m. Anchor: Nov 2025 call, May 2026 call (B07).
10. Conversion of 6 to 7 pipeline jobs (15 to 30 Cr each) to signed orders beyond the Reliance / L&T anchor. Tier: claim. Window: 0 to 12m. Anchor: May 2025 call, May 2026 call (B07).
11. Adoption of genuine quarterly (numeric) reporting after repeated investor requests across 3 calls. Tier: claim. Window: 0 to 12m. Anchor: May 2025, Nov 2025, May 2026 calls (B07).

Capex embedded growth: 0% (B07 capex_embedded_growth_pct). No dropped catalyst is discarded; the international push and the ESOP are recorded as broken promises (B05 dropped_triggers, B07 FLAG-PROMISE-BROKEN).

---

## 3. Flags with complete underlying findings

### FLAG-CASH (active): determination GROWTH-INDUCED (operator final)

Every cited item behind the determination:
- Cumulative CFO/PAT (FY25 to FY26) 0.41; latest FY26 0.398; series volatile: FY24 1.01, FY25 negative 1.65 (B01 block_b_trend; B10 cfo_pat_cumulative_fy25_fy26).
- FY25 CFO negative 5.24 Cr restated (negative 14.08 Cr original filing, reclassified per Note 7) against PAT positive 8.56 Cr; CFO/PAT negative 1.65x, CFO/EBITDA negative 1.21x; funded entirely by IPO financing inflows (net 2,261.36 lakh), not operations (B03 FLAG-CASH; Cash Flow Statement p.48; B10 conflicts cfo_fy25).
- Trade receivables up 155.3% (866.67 lakh FY24 to 2,212.83 lakh FY25) versus revenue up 33.67%; debtors turnover 6.77x to 4.61x, implied days ~54 to ~79; zero doubtful debt provision both years (B02 Note 10 p.55, Note 30 p.64, Note 29 p.63).
- Trade retentions 47.7% of total trade receivables (1,056.03 of 2,212.83 lakh), up 61.7% YoY (B02 Note 10 p.55); retentions are contractual and release on project sign off.
- FY26 CFO recovered to 6.77 Cr; collection days already fell back to ~41 (B10 cfo_fy26; FTTCP deliberation Engine 3).
- Capex commissioning timeline: no forward capex guidance in concalls; FY26 capex inferred 1.96 Cr from balance sheet movement (net block 1.18 to 1.96, CWIP 0.98, depreciation 0.2), plus or minus 20% uncertainty; asset light, no major plant commissioning cycle disclosed (B10 capex_anchor; B10 unresolved capex_guidance_plan_fy27_fy29).
- Receivables composition: ~48% retentions (structural to EPC), remainder trade receivables with a small actively litigated DLF balance ~11.89 lakh classified considered good (B02 Note 30 p.64; B04 irrelevant_ratios).
- Rating agency verbatim: NOT PROVIDED, SME exempt (B10 rating_wc_quote, reproduced in full in Section 1.3).
- Falsification trigger: H1 FY27 CFO/PAT below 0.7x while working capital days climb faster than revenue growth flips the determination to STRUCTURAL, Pillar 2 to 0.65x, destination PE to ~11 to 16x (B10 cash_falsification_trigger; B11; FTTCP deliberation Step 5).

### FLAG-GATE0 (active): score 86 of 160, AVERAGE

- Grand total 86, core 65 of 100, moat 21 of 60; blocks A 20, B 7, C 18, D 20, E 0; moats confirmed 5, moat class STRONG; classification AVERAGE (B01).
- Depressor detail: deal breaker #2 Block B equals 7 (below 8) caps at max GOOD; deal breaker #4 cumulative CFO/PAT equals 0.41 (below 0.50) caps at max AVERAGE, most restrictive applied (B01 deal_breakers). Primary driver FY25 CFO negative 5.24 Cr restated against PAT positive 8.56 Cr, a post IPO working capital build, plus FY20 to FY22 COVID period CFO/PAT weakness (B01 FLAG-GATE0). Block E scored 0 of 20 solely because no shareholding pattern, pledge, or contingent liability data was provided, a data gap not a governance finding (B01 flags). Block A rests on only 2 of 9 years of computable ROCE (FY25 to FY26), flagged low confidence (B01 FLAG-DATA-GAP).

### FLAG-GOVERNANCE (active, major)

- Independent director attendance below 42% of FY25 board meetings (4/12 to 5/12) versus 100% for all three executive / promoter directors; an executive director (Aiyer) sits on the audit committee (B03, B08 Boards' Report).
- Remuneration disclosure contradiction: Note 20(b) p.58 implies 169.3% / 169.3% / 26.9% FY25 increases versus Annexure III p.31 stating 37.02% / 37.02% / 53.35% for the same three executive directors (B02, B03, B12a CRITICAL).
- Company secretary turnover three times in about 16 months across the IPO window (Nidhi Sharma, Kirti Jain, Vishakha Rani), no reasons disclosed (B08 Note 20a).
- Undisclosed Bank of India cash credit debit balance 665.43 lakh (~11% of total assets) in Note 11 with no corresponding facility in Note 4 Borrowings, which shows D/E 0.00 (B02 Note 11 p.55, Note 4 p.52).
- Priced through the required return track at r equals 16.0% (B11).

### FLAG-CONCENTRATION (active, major)

- Reliance Consumer Products and its bottler Bhartiyam Beverages together anchor ~70% of H2 FY26 order book execution, the single largest order in company history (B07 FLAG-CONCENTRATION; B10). Book to bill 0.84x and declining (B09, B10). Customer concentration never quantified despite being asked twice on calls (B05). Caps base revenue CAGR at the SOM ceiling of 23% (B11).

### SHARED-CATALYST (note)

- A single working capital unwind drives both Pillar 1 ROCE and Pillar 2 cash (B11 SHARED-CATALYST). Role 3 stress tested: if working capital does not release, capital employed swells and ROCE also falls, widening the true tail toward negative 44% (13x raw / 9.1x RRM) and pushing real upside to downside toward 1.4x (B15 top_counters).

### FLAG-PROMOTER (not active)

- Verdict CAUTION, not AVOID (B08). Scorecard clean 5, caution 5, red 0, zero deal breakers. Adverse findings (all VERIFIED unless noted): fourth promoter Lalit Mohan Datta (13.72%) exited the board 31/03/2024 ~8 months pre IPO with no reason disclosed; three promoter controlled enterprises (Oakens Engineering, Flagmo Ea Technologies, Flagmo Marketing) share the Delhi corporate address, family directed, disclosed as significant influence related parties with zero FY24 to FY25 transactions; director remuneration up 37 to 53% in the IPO year versus 11.98% median employee increase; independent director attendance 33 to 42% versus 100% for executives with an executive on the audit committee; CS turnover 3x in 16 months; FY25 OCF negative 1,408.02 lakh against PAT 856.08 lakh, corroborated into FY26 (accrual ratio 0.51 TTM to Mar 2026, Simply Wall St, corroborating only); one UNVERIFIED item, a generic MDA risk factor on equity allotted below IPO price with no named transaction (B08 adverse_findings). None found: SEBI orders, criminal / economic offence cases, SFIO / PMLA / benami / DRI, MCA disqualifications, auditor resignation / qualification / restatement, promoter pledge (0.00%) or promoter selling (B08 adverse_findings_none_found). Transition evidence: non family professional CFO (Rakesh Kaul) since 02/03/2024 pre IPO; standard IPO readiness governance build out with 4 IICA registered independent directors and audit / NRC / stakeholder committees, vigil mechanism, insider trading, RPT and materiality policies (B08 transition_evidence). Pledge 0% since Dec 2024 listing (B08).

---

## 4. Credibility grade

- Grade: B (B05 credibility_grade).
- Basis: core numeric commitments (revenue growth, order book conversion) consistently met or exceeded across all three periods with clean FY26 internal reconciliation, but governance and communication commitments (quarterly reporting, ESOP, H1/H2 skew reduction, order book number consistency, forward guidance specificity) show a recurring pattern of misses and unreconciled figures (B05 credibility_basis).
- promise_delivery_score: delivered 3, partial 2, missed 3 (B05 promise_delivery).
- repeated_evasions: quarterly (or more frequent) financial reporting, asked in Q4 FY25, Q2 FY26, Q4 FY26; answer changed from outright deferral, to an unfulfilled repeat of the same promise, to a partial percentage only (non numeric) delivery that still falls short (B05 repeated_evasions).

Guidance versus delivery table (B05 promise_delivery.rows):

| Promised in | Promise | Outcome | Explanation |
|---|---|---|---|
| Q4 FY25 | Revenue growth at least ~25% for FY26 | delivered | FY26 revenue grew 109.5% YoY, vastly exceeding the floor |
| Q4 FY25 | Order book (55 Cr+) converts within the year via 6 to 10 month gestation | delivered | Consistently explained and delivered across FY25 and FY26 |
| Q4 FY25 | Narrow the H1/H2 revenue skew (from 30/70) toward year round cadence | missed | FY26 split was ~22/78 (H1 32.56 Cr / H2 116.08 Cr), more skewed; not acknowledged |
| Q4 FY25 | Move to quarterly reporting from subsequent quarters | partial | Only a percentage only non numeric circular at Q3 FY26; full quarterly financials still not delivered |
| Q2 FY26 | ESOP for core people by end of FY26 | missed | Zero mention in the Q4 FY26 year end call; no explanation |
| Q2 FY26 | ZLD mix and bigger tickets will be margin accretive | partial | Margins declined YoY in H2 FY26 on raw material and logistics inflation; accretion claim not reconciled |
| Q2 FY26 | International expansion into Vietnam / Indonesia / Middle East | missed | Gulf effort explicitly abandoned by Q4 FY26 with a rare honest admission; focus retreated to India only |
| Q2 FY26 | Order book 145 Cr as of Nov 2025 will convert cleanly | partial | Q4 FY26 closing book 125 Cr could not be cleanly bridged from 145 Cr; conflicting historical figures on the same call |

Note: transcripts are semi annual (H1/H2) calls labelled Q4 FY25 / Q2 FY26 / Q4 FY26; figures are period anchored to their true H1/H2 basis (B05 flags). This is a no concall mode false run (3 concalls present).

---

## 5. Scorecards and market sizing

### Gate 0 (B01)

- grand_total 86 of 160; core_score 65 of 100; moat_score 21 of 60.
- Blocks: A 20, B 7, C 18, D 20, E 0.
- moats_confirmed 5 of 12; moat_class STRONG; classification AVERAGE.
- Deal breakers: #2 Block B equals 7 (below 8) caps at max GOOD; #4 cumulative CFO/PAT equals 0.41 (below 0.50) caps at max AVERAGE (most restrictive, applied). history_downgrade false.

### Emerging Moat (B07)

- em_score 10.1 (B12c notes re sum 10.3, non decision changing); em_classification NONE (threshold 12).
- active_categories: G1 War chest (Strong, documented, already active); F2 Execution moat (Moderate, mixed, ongoing); C1 Customer ecosystem (Moderate, claim, 12 to 24m); E1 Geographic / technology first mover (Moderate, claim, unverified).
- evidence_mix: documented 3, claim 11, inference 0. Completionist recount: 3 documented items across 2 categories (G1 cash balance growth plus debt free status; F2 audited FY26 revenue growth); all other rows rest on management claims (B07).
- combined_assessment AVERAGE; reasoning: AVERAGE backward (capped by cash conversion deal breakers) paired with NO MEANINGFUL EMERGING MOAT forward (10.1/80) fails the GOOD/AVERAGE plus EXPANSION transition setup; the one strong item (G1 war chest) is a backward IPO artefact (B07).

### Accounting quality (B02): 4 of 10

Top notes findings, with note_ref and rating:
1. Trade receivables up 155.3% vs revenue up 33.67%; zero doubtful debt provision both years; turnover 6.77x to 4.61x (Note 10 p.55, Note 30 p.64, Note 29 p.63) Red Flag.
2. Note 20(b) implies 169.3% FY25 pay rise for MD Dosajh and ED Aiyer vs 37.02% in Annexure III; third director 53.35% vs implied 26.9% (Note 20b p.58 vs Annexure III p.31) Red Flag.
3. Director remuneration +90.9% YoY; average managerial pay +38.79% vs average employee +7.19% in the listing year (Note 17 p.57; Annexure III p.31) Red Flag.
4. Three enterprises with directors' significant influence (Oakens, Flagmo Ea, Flagmo Marketing) named with zero disclosed transactions (Note 20a p.58) Red Flag.
5. Undisclosed Bank of India CC debit balance 665.43 lakh (~11% of assets) with no facility in Note 4, which shows D/E 0.00 (Note 11 p.55; Note 4 p.52) Watch.
6. Unexplained stale (>3 year) disputed non MSME trade payable 10.81 lakh, unchanged both years, no counterparty (Note 30 p.64) Red Flag.
7. 9:1 bonus issue (871.74 lakh capitalised) immediately pre IPO; promoter holding diluted 25.03pp (94.32% to 69.29%) in one year (Note 2 p.51, Note 3 p.52) Watch.
8. Export revenue fell 59% (407.71 to 167.10 lakh) with 100% customer/geography churn (Vietnam to Egypt/Nigeria), contradicting the MDA international growth claim (Note 22 p.59 vs MDA p.32) Watch.
9. MDA risk factors describe material litigation while Note 25's portfolio is modest (<1% of net worth), company predominantly a plaintiff (Note 25 p.60 vs MDA p.33) Watch.
10. Trade retentions 47.7% of total trade receivables (1,056.03 of 2,212.83 lakh), up 61.7% YoY (Note 10 p.55) Watch.
11. Disputed DLF receivable fell unexplained 15.51 to 11.89 lakh in active litigation; Note 25's 11.88 does not match Note 30's 11.89 (Note 30 p.64; Note 25 item 2 p.60) Watch.
12. ROE fell 60% to 28%; ROCE 59.61% to 24.70%, equity base (IPO) driven not operational (Note 29 p.63) Watch.
13. No warranty provision, no gratuity actuarial assumptions; depreciation useful lives deviate from Schedule II with no justification (Note 1 p.49-50, Note 5 p.52) Watch.
14. Note 1(i) DTA narrative 12.20 lakh vs Note 23 table 12.63 lakh for the same component (Note 1i p.50 vs Note 23 p.59) Watch.
15. Three company secretaries within ~17 months spanning the IPO window, no reason disclosed (Note 20a p.58) Watch.

going_concern_language: NONE (B02). restatements_found: only boilerplate regrouping (Note 26 p.60), no itemized quantified restatement (B02).

### Market (B09)

- tam_cr conservative 11,250 / realistic 14,500; sam_cr 6,375 (56.7% of TAM); som_3yr_cr 277; som_5yr_cr 434.
- runway_class STRONG; revenue_headroom_x 42.9; current_sam_share_pct 2.33; tam_growth_pct 9.6.
- som_implied_revenue_cagr yr3 23.1% / yr5 23.9%.
- mgmt_claim_cr 0; mgmt_claim_ratio 0 (not computable; no numeric TAM claim in inputs) (B09 flags).
- capacity_check: gap of ~290 Cr in required order book coverage by Year 3 versus current 125 Cr book; SOM trajectory optimistic given replenishment lagging and weak cash conversion (B09).

### Peer triangulation (B06)

- verified: [] (none formally verified).
- partially_verified: peer input cost inflation partly offset via price variation clauses (CEWATER, EIEL, FELIX); market consolidation toward larger tickets (EIEL, CEWATER); SME peers voluntarily give quarterly interim disclosure (FELIX).
- contradicted: [] (empty). But B06 flags the raw material inflation claim (25 to 40% H2 FY26) as not corroborated at claimed magnitude or window: peers show 1 to 2pp EBITDA, later (Q4 FY26/Q1 FY27), tied to Middle East disruption (B06 flags; B10 conflicts input_cost_inflation).
- unverifiable: ZLD/water recycling penetration single digit to ~1% and whether the two cited figures are the same metric (checked all four peers); Apex top 1/3/5 customer concentration relative to peers (checked all four peers).
- net_narrative_effect: complicates (B06).
- Peer citation integrity caveat: Verifier D flagged 2 CRITICAL and 1 MAJOR misattributions/fabrications in B06 (EIEL Q1 TAM quote, FELIX price variation quote, CEWATER speaker), acceptance 81 (B12d). Treat peer corroboration as weakened.

---

## 6. Valuation pillar detail

Stage 11 ran (B11). Both tracks in full.

### Track 1 (RRM, governing)

- Fundamental base PE = raw four pillar PE 24.0x. Base r small/micro cap 14%; +1.5% FLAG-GOVERNANCE major; +0.5% weak durability (EM NONE, ~70% two customer concentration); r = 16.0% (within [9%,18%]).
- RRM = 1 + (13.5 - 16.0) x 0.12 = 0.70 (lower bound). Track 1 destination PE = 24.0 x 0.70 = 16.8x, below sector cap 20x (not binding).
- Track 1 range 15.5 / 16.8 / 18.0 (B11 destination_pe.track1_rrm; r_used 16.0, rrm 0.70).

### Track 2 (additive)

- A ROCE base 24.0x (ROCE 33.39%, 0.5 x 33.39 + 7.5 = 24.195, capped 24.0; elite branch 24.1x, immaterial per B12c).
- B cash multiplier 1.00x (growth induced: 0.80 base + 0.20 offset).
- C quality adjusted base 24.0x.
- D growth visibility premium +0x (EM 10.1 below 25).
- E strategic premium +0x (single credit rule; ROCE via Pillar 1 only).
- F raw destination PE 24.0x; F2 UA adjusted 24.0x (UA not applied).
- G sector cap 20.0x (EPC / Civil construction, no uplift); H final = min(24.0, 20.0) = 20.0x.
- Track 2 range 18.5 / 20.0 / 20.0 (upper bound capped at the absolute sector cap) (B11 destination_pe.track2_additive).

### Track divergence and governing track

- Divergence 16.0% (above 15%). Governing track = Track 1 (RRM), more conservative; the additive track is pinned at the sector cap and cannot express governance/durability weakness, which RRM prices via r (B11).

### Pillar detail (B11 pillar_detail)

- roce_used 33.39; roce_base 24.0; roce_recovery_route pillar1; cash_multiplier 1.00; structural_or_growth growth-induced; growth_offset 0.20; growth_premium 0; strategic_premium 0; shared_catalyst_flag true; ua_applied false; sector_cap_used 20.

### Hurdle, fair values, entry, decision

- hurdle_ratio base 1.63 (Track 1) / 1.94 (Track 2), bull 2.21 / 2.63; bull_used true; verdict CONDITIONAL (base FAIL, bull PASS) (B11).
- fair_values Track 1 {bear 232, base 394, bull 572}; Track 2 {bear 276, base 469, bull 635} (B11).
- expected_cagr_prob_weighted 16.7% (Track 1 governing) / 22.9% (Track 2); weights grade B 25/50/25 (B11).
- entry_range 161 to 202; mos_price 161; upside_downside_ratio 1.9 (structural cash tail, binding risk) (B11).
- decision WATCHLIST; position size Small (B11, B14).
- EPS scenarios FY29: bear 14.9, base 23.4, bull 31.8 (from EPS 12.91, EPS CAGR 5/22/35%); base revenue FY29 ~276.6 Cr matches SOM Yr3 277 Cr; som_cagr_crosscheck consistent (B11).
- UA qualifiers: listed >=12 months MET (~19 months, B10 date error corrected to Dec 2024 listing); Gate 0 >=60 MET (86); FII+DII combined <3% NOT SATISFIED (not evidenced, only promoter 69.29%); all three fail, UA not applied (B11, B10 ua_qualifiers).
- unresolved inputs used: FCF/revenue ~5 to 7% held flat (tertiary 10% weight); flat capex/sales (no forward guidance); peer medians qualitative only (four pillar destination PE remains sole exit authority) (B11 unresolved_inputs_used).

---

## 7. Gaps ledger

| Item | Stage / block needing it | Where to obtain |
|---|---|---|
| FII + DII holding % | B10, B11 UA qualifier 3 (blocks UA gate) | Latest shareholding pattern filing with the exchange (NSE/BSE); Trendlyne public holdings; MCA registry |
| Credit rating / rating agency WC comment | B02, B03, B08, B10 cash determination | Does not exist; SME issuers exempt (AR Boards' Report p.26). Determination rests on AR + peer + operator |
| Order book aging / fulfillment schedule | B09, B10, B11 (blocks forward analysis) | Q4 FY26 concall detailed commentary; AR/investor presentation order book note; IR announcements |
| FY26 FCF / capex itemization (±20% uncertainty) | B10, B11 DCF/P-FCF (tertiary) | FY26 AR Cash Flow note; fixed asset depreciation and capex schedule |
| Peer medians (P/E, EV/EBITDA, P/B) | B06, B10, B11 relative cross check | Screener/exchange filings for CEWATER, EIEL, EMSLIMITED, FELIX; compute aggregate medians |
| Peer citations to re source (2 CRITICAL, 1 MAJOR) | B06 (B12d findings) | EIEL Aug 2025, FELIX Nov 2025, CEWATER May 2026 transcripts; correct speaker/company/quote |
| Remuneration contradiction (169.3% vs 37.02%) | B02, B03, B08 governance / RPT pillar | Management clarification; AR Note 20(b) p.58 vs Annexure III p.31; next AR |
| Bank of India CC facility terms | B02, B03, B10 governance flag | FY26 AR Notes 4 and 11; concall commentary on credit terms |
| Related party enterprise transactions (Oakens, Flagmo x2) | B02, B08 governance | FY26 Note 20(b) / AOC-2; entity records |
| Contingent liabilities rupee detail | B03, B10 (low materiality) | AR Note 25 full schedule with case name, amount, timing |
| Diluted share count direct verification | B10 (used with caveat) | Post IPO shareholding pattern filing; RHP/DRHP archives; MCA |
| Quarterly (numeric) FY26 results | B10 (deferred) | Investor presentation slides; Q4 FY26 concall; any Q3 FY26 circular |
| FY27 to FY29 capex guidance | B10, B11 FCF projection | Q4 FY26 concall capex commentary; AR guidance section |
| ROCE FY18 to FY24 (only FY25 to FY26 computable) | B01 Block A (low confidence) | Full balance sheets with current/non current liability split pre FY25 |
| Shareholding pattern / pledge detail | B01 Block E (0/20 data gap) | Exchange shareholding pattern filing; pledge disclosure |

Sources for these gaps, general: BSE / NSE exchange filings, the FY26 audited Annual Report, the company investor relations page, and the four peer transcripts named above. No credit rating rationale is obtainable (SME exempt).
