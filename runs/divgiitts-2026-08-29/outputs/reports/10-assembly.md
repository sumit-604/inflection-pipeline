# B10 VALUATION INPUTS ASSEMBLY — DIVGIITTS

**Run:** divgiitts-2026-08-29  
**Stage:** 10 (Haiku 4.5)  
**Date:** 2026-08-29  
**Assembled by:** Claude Code stage-10-assembly-pipeline  

---

## COMPANY IDENTITY BLOCK

| Field | Value | Anchor |
|---|---|---|
| Company | Divgi Torqransfer Systems Ltd | manifest.yaml |
| Ticker | DIVGIITTS | manifest.yaml |
| Sector / Category | Auto Components (driveline/transmission) | B04 (corrected from agri processing) |
| Business Model Type | Build-to-spec component maker (manufacturing) | B04 |
| Market Cap (Cr) | Rs 3,594 | manifest.yaml |
| CMP (Rs) | 1,175 | manifest.yaml |
| Shares Outstanding (Diluted, Cr) | 3.0582 | FY26 paid-up capital 152.91 Mn / face value 5; consistent with FY27 base, FTTCP deliberation |
| Enterprise Value (Cr) | 649.8 (computed: Mcap 3,594 + Net Debt -2,944) | Computation: Cash+Bank (315.20 + 2,630.03) - Borrowings (0.46 + 0.95) = 2,943.82 Cr net cash; EV = 3,594 - 2,943.82 (FY26 audited balance sheet, results PDF 0231a580) |

---

## LATEST FINANCIALS (FY26 AUDITED, ENDED 31-MAR-2026)

| Metric | FY26 Audited | Q1 FY27 Unaudited | Anchor / Note |
|---|---|---|---|
| **Income & Profitability** | | | |
| Revenue from operations (Cr) | 3,528.88 | 1,371.42 (Q1 quarterly) | FY26: Statement of Financial Results, results PDF 0231a580 p.4; Q1 FY27: results PDF ece436bc p.5 |
| EBITDA (Cr) | ~920 (estimated 627.49 PBT + 292.37 D&A) | 415.71 (Q1, estimated PBT 337.51 + D&A 78.20) | FY26 derived from PBT + D&A; Q1 FY27 from results PDF |
| EBITDA margin (%) | ~26.1% | 29.3% (Q1) | FY26: (920/3,528.88); Q1: (415.71/1,417.64) |
| PAT (Cr) | 469.26 | 252.40 (Q1) | FY26 audited Statement of Financial Results p.4; Q1 FY27 unaudited results PDF ece436bc p.5 |
| PAT margin (%) | 13.3% | 17.8% (Q1) | FY26: (469.26/3,528.88); Q1: (252.40/1,417.64) |
| Diluted EPS (Rs) | 15.34 | 8.25 (Q1) | FY26 audited results; Q1 FY27 unaudited results |
| Operating EPS FY27 (Rs) | 24 (forward base, FTTCP) | — | FTTCP deliberation Section 5 (operator verified): FY27 operating EPS Rs 24, treasury stripped |
| Treasury EPS FY27 (Rs) | 4 (forward, FTTCP) | — | FTTCP deliberation Section 5: Rs 4 per share from treasury income |
| **Cash Flow & FCF** | | | |
| CFO (Cr) | 410.83 | — | FY26 audited Cash Flow Statement, results PDF 0231a580 p.7 |
| FCF (Cr) | -32.33 | — | Computed: CFO 410.83 - Capex 443.16 (capex from investing activities in cash flow) |
| Capex (Cr) | 443.16 | — | FY26 audited Cash Flow Statement, results PDF 0231a580 p.7 (payments for PPE acquisition) |
| D&A (Cr) | 292.37 | 78.20 (Q1) | FY26 audited statement p.4; Q1 FY27 unaudited p.5 |
| CFO / PAT (latest) | 0.876 | — | FY26: 410.83 / 469.26 |
| CFO / PAT (cumulative FY20-26) | 0.969 | — | B01-gate0 (data_notes) |
| FCF / PAT | -0.069 (negative FCF) | — | FY26: -32.33 / 469.26 (negative due to capex cycle) |
| P/FCF | Not applicable (FCF negative) | — | Cannot compute meaningful metric on negative FCF |
| **Balance Sheet & Liquidity** | | | |
| Book Value (Cr) | 6,354.56 (total equity) | — | FY26 audited balance sheet, results PDF 0231a580 p.6 (equity share capital 152.91 + other equity 6,201.65) |
| Book Value per Share (Rs) | 207.72 | — | Equity 6,354.56 / Shares 30.582 |
| Net Cash (Cr) | 2,943.82 | — | Cash + Bank (315.20 + 2,630.03) - Borrowings (0.46 + 0.95) = 2,943.82 (FY26 audited balance sheet) |
| Net Cash per Share (Rs) | 96.19 | — | 2,943.82 / 30.582 shares (approx Rs 95/share per FTTCP deliberation, Section 5) |
| Trade Receivables (Cr) | 792.87 | — | FY26 audited balance sheet p.6 |
| Receivables Days (approx) | ~82 | — | (792.87 / 3,528.88) x 365 = ~82 days (normal for OEM Tier-1, per B04) |
| Inventory (Cr) | 587.83 | — | FY26 audited balance sheet |
| Total Debt (Cr) | 1.41 | — | Long-term borrowings 0.46 + short-term borrowings 0.95 (effectively debt-free) |
| **Valuation Ratios (snapshot at CMP)** | | | |
| P/E (on FY26 EPS) | 76.5x | — | CMP 1,175 / EPS 15.34 |
| P/E (on FY27 operating EPS, forward) | 48.9x | — | CMP 1,175 / Operating EPS 24 (FTTCP forward base) |
| EV/EBITDA | 0.7x | — | EV 649.8 / FY26 EBITDA ~920 (depressed by cash; not economically meaningful) |
| P/B | 5.65x | — | CMP 1,175 / BVPS 207.72 |

---

## RETURN METRICS & QUALITY

| Metric | FY26 | FY25 | Trend / Note |
|---|---|---|---|
| **ROCE (latest, treasury-stripped basis)** | 7.68% (median FY25-26) | — | B01: "median ROCE 7.68% (FY25-26, only computable years) driven by outsized post-IPO cash pile (~Rs 283-295 Cr) inflating capital employed relative to operating EBIT" |
| **ROCE forward (operator-ruled FY27)** | — | — | FTTCP deliberation: Pillar 1 ROCE 20% treasury-stripped both sides, fair-case (rests on 24% FY29 operating margin above 20-22% guide) |
| **ROE (reported, FY26)** | 7.38% | — | PAT 469.26 / Equity 6,354.56; depressed by treasury income |
| **ROCE 2-year trend direction** | Improving (trough FY25 ~4.2%, recovery FY26) | — | B04 and B01 analysis; FY26 capex cycle underway |

---

## HISTORICAL GROWTH & CAGR

| Metric | Value | Period / Basis | Anchor |
|---|---|---|---|
| **3-year Revenue CAGR** | — | NOT FOUND | B01 notes: "screener export lacks current/non-current liability split for FY2018-FY2024 — limits historical analysis" |
| **3-year PAT CAGR** | — | NOT FOUND | Same limitation |
| **1-year Revenue Growth (FY26 vs FY25)** | +61.2% | FY25 Rs 2,189.17 Cr to FY26 Rs 3,528.88 Cr | FY26 audited results PDF, statement p.4 |
| **1-year PAT Growth (FY26 vs FY25)** | +92.2% | FY25 Rs 243.92 Cr to FY26 Rs 469.26 Cr | FY26 audited results PDF |
| **Q1 FY27 Revenue Growth YoY** | +85% | Q1 FY26 Rs 716.76 Cr to Q1 FY27 Rs 1,371.42 Cr | Q1 FY27 results PDF ece436bc p.5 |

---

## FORWARD GUIDANCE & MANAGEMENT CREDIBILITY

| Metric | Value | Timeframe | Credibility | Anchor |
|---|---|---|---|---|
| **Guided Revenue Growth** | ~Rs 500 Cr (approx 41% on FY26 baseline) | FY27 | Directionally credible but requires further acceleration; MD letter uses "revenue" inconsistently | B05 (guidance_table) |
| **Guided EBITDA Margin Band** | 20-22% | FY27 implied | Mixed credibility; Q1 FY27 printed 27% but cycle-elevated per management framing | B05; FTTCP deliberation notes 24% as blend |
| **Long-term Revenue Aspiration** | ~Rs 1,000 Cr | FY29-30 | No interim milestones; contingent on non-contracted automatic-transmission opportunity; flagged as unassessable | B05 (guidance_table) |
| **Management Credibility Grade** | B (Good) | — | Financial guidance and flagship Indonesia program delivered; EV transmission slipped 3 consecutive quarters on identical excuse; auto-transmission contract milestone quietly dropped; cannot answer organic-vs-Indonesia growth split | B05 (credibility_grade) |

---

## EMERGING MOAT & CATALYSTS (FROM B07)

| Metric | Value | Anchor |
|---|---|---|---|
| **EM Classification** | STRENGTHENING (30/92) | B07 |
| **Evidence Quality Mix** | 38 documented + 18 claim + 6 inference = 62 items weighted; mostly documented (61%) | B07 (evidence_mix) |
| **Active Moat Categories** | B2 (OEM qualification PPAP), E2 (China+1 sourcing), G1 (balance-sheet war chest), G2 (working-capital improvement), A3 (process innovation), C1 (customer ecosystem), E1 (Indonesia first-mover), F1 (engineering talent), H2 (BorgWarner partnership) | B07 (active_categories) |
| **Primary Catalyst (12m)** | Sigma EV transmission SOP (slipped 3 quarters) | B07; window 0-6m; management claim, tracked failure to date |
| **Secondary Catalyst (12m)** | BorgWarner partnership renegotiation outcome | B07; window 6-12m |
| **Downstream Signal Candidates** | Mahindra/Tata 4x4 monthly sales; Indonesia Scorpio Pik Up CY2026 exports (35,000-unit program); India EV PV sales; BorgWarner tech-licensing updates; Named NA OEM automatic-transmission decision; Project Mayflower capex/hiring | B09 (downstream_candidates) — all externally verifiable, cadence monthly to event-driven |

---

## TAM / SAM / SOM (FROM B09)

| Metric | Value | Confidence | Anchor |
|---|---|---|---|
| **TAM (realistic)** | Rs 6,800 Cr | L (low) | B09: apportionment proxy; no India-specific transfer case market value located |
| **TAM (conservative)** | Rs 4,000 Cr | L | B09 |
| **SAM** | Rs 2,160 Cr (31.8% of realistic TAM) | L-M | B09 |
| **SOM (3-year)** | Rs 552 Cr | M | B09; implies FY27-29 revenue growth to ~Rs 640 Cr at 16.1% CAGR |
| **SOM (5-year)** | Rs 708 Cr | M | B09; implies 15.0% CAGR |
| **Management Claim (FY29-30)** | Rs 1,000 Cr (aspiration) | M-H (for SOM ratio) | B09: mgmt_claim_ratio 1.41x vs SOM; claim reads "reasonable" |
| **Implied Revenue CAGR (SOM, 3yr)** | 16.1% | — | B09 (som_implied_revenue_cagr) |
| **Demand Externally Verifiable** | True | — | B09: downstream candidates identified; SIAM data, government trade stats, OEM disclosures |

---

## SHAREHOLDER COMPOSITION & UA QUALIFIERS

| Qualifier | Value | Anchor |
|---|---|---|
| **Listed >= 12 months** | Yes (March 2023 IPO, 3.4 years as of 29-Aug-2026) | B00 |
| **Gate 0 Composite Score >= 60 OR EM >= 25** | EM 30 > 25 (PASSED) | B01: Gate 0 composite 46 (FAILED); B07: EM 30 >= 25 (PASSED) |
| **FII + DII < 3%** | No (FII 1.86% + DII 26.16% = 28.02%) | B00 (non_anchored_leads, screener.in secondary source from Jun-2026); B08 reports same institutional holding via Oman India Joint Investment Fund ~12.19% |
| **UA Qualifiers Summary (all-three-met)** | No (fails condition 3: FII+DII 28% >> 3% threshold) | Per CLAUDE.md: UA none (fails the <3% qualifier) |

---

## DOWNSTREAM ENTITIES (AR NEW, FEED FOR STEP 10.5B)

From B03 (ar_new_downstream_entities):

| Entity | Where in AR | Type | Note |
|---|---|---|---|
| Divgi-TTS US subsidiary (unnamed legal entity) | Chairman's/MD's Perspective pp.25-27, 32-33 vs Board's Report Item 13 p.75 | Claimed wholly-owned US subsidiary | **Contradiction flagged**: Narratives describe as "established, operating"; Board's Report states no subsidiary existed FY26. Board approval 25-May-2026, Delaware incorporation 4-Jun-2026, both AFTER FY26 year-end. FLAG-SUBSIDIARY-CONTRADICTION (B03). |
| Silao, Mexico warehouse (BorgWarner Irapuato-linked) | Business Driver - Global Outreach p.68 | Overseas warehouse/logistics facility | Confirmed in AR; verification pending |
| CREATE (Center for Research Excellence in Automotive Transmission Engineering) - BITS Pilani MoU | MD's Perspective p.33 | Academic research collaboration/MoU | New collaboration; exploratory stage |
| Planned Greenville, South Carolina USA presence (Clemson University/ICAR) | MD's Perspective p.34 | Planned new North American presence/facility | Not yet active; at planning stage |
| Divgi Holdings Pvt Ltd - Leave & License Agreement for office premises (Oct-2025) | AOC-2 p.84 | New related-party lease arrangement | Rent expense Rs 1.21 Lakh/month; new arrangement not explicitly called out in Note 34 related-party note (B02 finding) |

---

## RATING PDF EXTRACTION

| Field | Value | Anchor |
|---|---|---|
| **Agency** | NOT FOUND — No credit rating exists for this company | B00 and B08 input_gaps; confirmed finding, not a gap |
| **Rating** | NOT FOUND | — |
| **Outlook** | NOT FOUND | — |
| **Date** | NOT FOUND | — |
| **Working Capital / Cash Flow Commentary (verbatim quote)** | NOT FOUND (no rating PDF available) | — |

---

## PEER MEDIANS (IF PROVIDED)

Peers listed in manifest: ENDURANCE, HAPPYFORGE, SANSERA, SONACOMS

| Metric | Median / Note |
|---|---|
| **P/E** | Peer downside line 27x forward (Amendment 20 cross-check only, does not set multiple per FTTCP); no standalone peer median provided for assembly |
| **EV/EBITDA** | NOT FOUND — no peer financial data extracted by stage 6 |
| **P/B** | NOT FOUND |
| **Growth** | NOT FOUND |
| **ROCE** | NOT FOUND |

**Note:** B06 reports peer verification against claims (tariff, de-sourcing, EV market growth) but peer financial medians were not extracted as a data table for this assembly. Peer comps are a cross-check only; they do not set the exit multiple per FTTCP (Amendment 20 gates both fail). (B06 / FTTCP deliberation Section 2, Override 3)

---

## CONFLICTS & UNRESOLVED

### Conflicts[]

| Field | Value A (Source A) | Anchor A | Value B (Source B) | Anchor B | Used | Reasoning |
|---|---|---|---|---|---|---|
| Promoter Shareholding % | 56.47% (FY26 audited) | AR Note 13(f), 31-Mar-2026 | 60.56% ('latest quarter' secondary web source) | screener.in/trendlyne.com (2026-08-29 access, proxy-blocked) | 56.47% | Audited AR figure takes precedence; web figure undated, unable to reconcile without filed shareholding pattern |
| Net Cash / Cash Position Trend (Spear load-bearing fact) | Rose Rs 9.7 Cr (FY26 actual) | B01/B03: Note 10 cash rose from Rs 284.8 to Rs 294.5 Cr | ~Rs 275 Cr net cash DECLINE (Spear brief B00) | B00 spear_hit | Actual: +Rs 9.7 Cr (rise) | AR Note 10 directly contradicts Spear claim; verified finding (B01/B03) |
| R&D Expenditure | Rs 11.79 Cr (million-figure, corroborated two pages) | AR Value-Creation Report + Business Driver p.42 | Rs 117.94 Cr (BRSR Annexure D, unit 100x error?) | AR Annexure D Technology Absorption | Rs 11.79 Cr | BRSR appears to contain a unit typo (crore vs million); smaller figure corroborated in two independent AR pages |
| US Subsidiary Status (narrative vs statutory) | Described as "our subsidiary", "established, operating" during FY26 | Chairman's/MD's Letters, pp.25-27, 32-33 (narrative tense) | "No subsidiary existed during FY2025-26" | Board's Report Item 13 p.75 (statutory) | Board's Report statement (accurate) | Board approval 25-May-2026 and Delaware incorporation 4-Jun-2026, both AFTER 31-Mar-2026 year-end; Chairman/MD narrative uses misleading tense |

### Unresolved[]

| Field | Why Unresolved | Where It Might Be | Severity |
|---|---|---|---|
| **Peer Financial Medians** | Stage 6 extracted peer verification claims but not a comparable-company data table with P/E, EV/EBITDA, growth, ROCE across ENDURANCE, HAPPYFORGE, SANSERA, SONACOMS | Peer company transcripts / investor presentations / screener.in; requires live SIAM/industry-tracker cross-check for precise comps | Medium (peer cross-check is secondary to operator-overridden exit multiple 30x) |
| **Customer/OEM Revenue Concentration (%)** | Not disclosed by company; no top-customer % or top-3 breakdown found in AR or investor presentations | Management concall (direct question); B05 notes management "could not/did not disaggregate Indonesia-driven vs organic" when asked directly in Q1 FY27 call | Medium (material for Halt 1 corpus resolution) |
| **Promoter Pledge (%** | Undisclosed; zero sources (AR, regulatory filings, web aggregators) produced a verifiable figure | SEBI shareholding-pattern filing (Regulation 31); trendlyne.com/CapitalLine direct shareholding tracker | Medium (estate-planning and credit-risk input) |
| **FY25 Results Resubmission Specifics** | Spear brief claims "June 2026 FY25 results resubmission"; B08 found resubmission was 11-Jul-2025 (technical XBRL/PDF PAT mismatch fix, unmodified auditor opinion), not substantive restatement | Regulatory news archives (BSE/NSE); B08 cross-verified date correction | Low (confirmed real but misdated; technical fix) |
| **FY27 Forward Operating EPS build components** | Operator provided FY27 operating EPS Rs 24 (treasury stripped); components (revenue Rs 545 Cr, margin 24%, D&A Rs 33 Cr, tax 25.2%, shares 3.0582 Cr) stated but not reproduced independently line-by-line by Claude Code | FTTCP deliberation Section 5 (operator verified); full detailed P&L build not provided | Low (operator-verified; used as-is) |
| **FY29 Operating Capital Employed (Pillar 1 ROCE driver)** | Deliberation cites Rs 575 Cr FY29 figure as "reasonable" projection; FY26 operating CE computed as ~Rs 355 Cr; intermediate year build (FY27-28) not detailed | FTTCP deliberation Section 6.1 provides the logic and FY26 anchor (Rs 355 Cr); FY27-29 is forecast, not audited | Low (operator-verified as load-bearing caveat; acknowledged as fair-case dependent on capex deployment) |
| **Indonesia 70,000-unit Program Unit Price Realization** | Blended transfer-case ASP FY26 ~Rs 34,000, but Indonesia units are "value-engineered manual-shift" (lower margin) — specific per-unit price NOT FOUND | Management concall (direct question on ASP by program); likely in Q1 FY27 call Q&A or later calls | Medium (impacts revenue runway FY27-28; FTTCP deliberation Section 6.2 provides bounded estimate Rs 105-140 Cr total program) |
| **3-year Historical Revenue & PAT CAGR** | Data gaps (screener lacks current/non-current split for FY18-24) limit ROCE and FCF to FY25-26 only | Full-year audited financial statements FY18-25 (screener.in or company IR page) | Low (not material to valuation if sourced; recent 1-year growth +61% / +92% more relevant) |
| **Operating ROCE FY26 (audited)** | Calculated median FY25-26 = 7.68% (per B01); individual year breakout not provided in blocks, only the median | B01 sourced figures; can be reverse-engineered from median if both years available, but FY25 not explicitly stated | Low (marked as TEMPORARILY DEPRESSED by cash pile; forward 20% is operator-ruled Pillar 1) |
| **P/E Relative Valuation Comps** | FTTCP notes peer downside line 27x forward and Amendment 20 gates both fail; no detailed peer P/E table constructed | Peer company latest-quarter results (transcripts, investor presentations) | Low (peer cross-check does not set the multiple per FTTCP; operator used 30x override on sector cap rationale) |

---

## GOVERNANCE & INTERNAL CONTROL FLAGS

Carried from B02 (accounting quality) and B08 (promoter):

- **FLAG-CASH** (B03): Spear brief claim of ~Rs 275 Cr net cash decline contradicted by audited Note 10 (cash rose Rs 9.7 Cr FY26). Verification risk; not an accounting-quality defect per se, but blocks use of that claim as load-bearing fact without re-verification.
- **FLAG-RPT-COMPLETENESS** (B03): Tejal Transmission Pvt Ltd (equity investee with common directorship) omitted from Note 34 related-party list; Ind AS 24 completeness gap extending to sitting Executive Director (per B08).
- **FLAG-SUBSIDIARY-CONTRADICTION** (B03, B08 confirmed): Chairman/MD narratives describe US subsidiary as "established, operating during FY26"; Board's Report Item 13 states no subsidiary existed during the year. Board approval 25-May-2026 and Delaware incorporation 4-Jun-2026, both after 31-Mar-2026 year-end. Narrative tense is misleading (VERIFIED disclosure-integrity issue).

---

## ANALYST NOTE

**Data Quality & Prioritization:**

1. **Treasury Cash vs Operating Earnings**: B04 and FTTCP deliberation emphasize that Other Income (Rs 222.83 Cr, ~6% of total income) is treasury interest on ~Rs 2,944 Cr net cash, NOT operating income. All valuation forwards must use OPERATING EPS, never reported EPS. Reported EPS Rs 15.34 multiplied by CMP Rs 1,175 = 76.5x P/E, which misleadingly values the treasury cash at 30x its yield (Rs 381 Cr vs Rs 294 Cr actual cash). Operating EPS Rs 24 (FY27) yields 48.9x, a more defensible but still elevated multiple at CMP.

2. **Conflict Resolution & Hierarchy**: The Spear brief's net cash decline claim is directly contradicted by audited financials; used audited Note 10 figure (cash rose) as authoritative. US subsidiary narrative is contradiction-within-the-same-AR (tense misleading; statutory disclosure accurate). Promoter shareholding carries 56.47% (audited AR) over 60.56% (web secondary, undated), pending shareholding-pattern filing reconciliation.

3. **Forward Estimates as Anchor**: FY27 forward operating EPS (Rs 24) and net cash per share (Rs 95) are operator-verified in the FTTCP deliberation, Section 5, and are the sole authority for Stage 11. No alternative derivation is entertained.

4. **Peer Set & Relative Valuation**: Four named peers; no financial medians extracted. Relative valuation (peer downside 27x forward) is cross-check only per Amendment 20 and FTTCP ruleset. Operator override to 30x exit multiple is peer-supported but not derived from peer comps; it is set at the overridden sector cap.

5. **Governance & Disclosure Integrity**: Three red flags identified (cash, RPT completeness, subsidiary narrative) spanning B02-B03-B08. None is individually disqualifying, but the cluster pattern of internal same-document contradictions (Spear claim vs Note 10, current-ratio explanation vs balance sheet, R&D units, related-party omissions) is flagged as a compilation/review control gap affecting management credibility on unverified numbers. Operator ruled WATCHLIST default to AVOID until 18-Sep-2026 AGM and FY27 AR clear governance items.

---

## OPERATIVE SUMMARY FOR STAGE 11 VALUATION

**Authoritative Inputs (from FTTCP deliberation, Section 5, to be used without modification by Stage 11):**

- **Pillar 1 base PE:** 19x (ROCE 20% treasury-stripped, v3.5.1 Route B cash-strip)
- **Pillar 2 cash multiplier:** 1.0x INDETERMINATE (no growth offset; no rating exists)
- **Pillar 3 growth premium:** +1x
- **Sector cap:** 30x (operator override, DIVGIITTS this run only)
- **Exit multiple (destination):** 30x forward (peer-anchored, at cap)
- **Earnings basis:** FY27 forward operating EPS (Rs 24), treasury-stripped, PRIMARY; FY28 secondary; FY30 dropped
- **Valuation method:** Operating EPS x exit multiple PLUS net cash at FACE value (Rs 95/share FY27, tapered later)
- **FY27 Base (operator verified):** Revenue Rs 545 Cr; operating EBITDA margin 24.0%; D&A Rs 33 Cr; other income Rs 17 Cr; tax 25.2%; shares 3.0582 Cr
  - **Fair Value FY27 = Rs 24 x 30 + Rs 95 = Rs 815**
  - **Entry Zone = Rs 570 to Rs 650** (20-30% margin of safety)
  - CMP Rs 1,175 = 45x forward operating earnings, 44% above fair value

**Not used**: Reported EPS (multiplies treasury cash at 30x yield); relative valuation does not set multiple (Amendment 20 gates fail); peer medians (incomplete extraction).

**Flagged for Stage 11 & Halt 1 resolution:** Promoter governance (CONCERN, defaults to AVOID until 18-Sep AGM and FY27 AR); net cash deployment timeline (Rs 293 Cr deploying into Shirwal and Mayflower, affecting FY28-29 interest income and working capital); Indonesia program unit ASP and follow-on order confirmation; proof gate (Sigma EV SOP, three consecutive quarter slips).

---

**Report compiled:** 29-Aug-2026  
**Assembly model:** Claude Haiku 4.5  
**Status:** Complete, ready for Stage 11 (Role 1 Valuation)

---
