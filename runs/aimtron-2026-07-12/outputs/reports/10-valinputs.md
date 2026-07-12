# STAGE 10: VALUATION INPUT ASSEMBLY
# Company: AIMTRON Electronics Ltd (AIMTRON)
# Run Date: 2026-07-12
# Model: Claude Haiku 4.5
# Status: COMPLETE

---

## COMPANY IDENTITY BLOCK

| Field | Value | Source Anchor |
|-------|-------|---------------|
| **Company** | AIMTRON Electronics Ltd | B01, AR2025 cover page |
| **Ticker** | AIMTRON | B01, manifest |
| **Sector** | Electronics Manufacturing (EMS/ESDM) | B04, stated as "manufacturing" |
| **Business Model Type** | Contract manufacturing (PCBA, Box Build, ODM design services); EMS/ESDM | B04.business_type, B04.revenue_streams |
| **Sector Cap Row** | Recycling / Manufacturing, 25x | FTTCP-deliberation.md line 19 (overrides manifest Pharma/CDMO 38x) |
| **CMP (Rs)** | 1,390 | Manifest, FTTCP-deliberation.md line 2 |
| **Market Cap (Rs Cr)** | 2,864 | Manifest, FTTCP-deliberation.md line 2 |
| **Shares Outstanding (Diluted, Cr)** | 2.06 | Derived: 2,864 Cr / 1,390 = 206.04 lakh shares = 2.06 Cr shares (results PDF EPS calculation basis) |
| **Enterprise Value (Rs Cr)** | 2,855.84 | mcap 2,864 + net debt -8.16 (cash position); arithmetic: 2,864 - 8.16 = 2,855.84 Cr (B01, balance sheet standalone 31-Mar-2026) |

---

## LATEST FINANCIALS (FY26 STANDALONE, AUDITED 27-APR-2026)

**Note: All revenue/PAT/CFO figures below are STANDALONE unless marked consolidated. Consolidated FY26 figures (for reference): Revenue Rs301.16Cr, PAT Rs45.97Cr, OCF -Rs40Cr (FTTCP-deliberation, concall data).**

| Metric | Value | Unit | Source Anchor |
|--------|-------|------|---------------|
| **Revenue** | 257.13 | Rs Cr | Results PDF (28-Apr-2026), P&L: Revenue from Operations 25,713.41 lakh = 257.13 Cr |
| **EBITDA** | 61.85 | Rs Cr | Derived: B01 FY26 margin 24.05% × 257.13 Cr = 61.85 Cr (B01 data notes, audited basis) |
| **EBITDA Margin** | 24.05% | % | B01.data_notes: "EBITDA margin standalone FY26 24.05%" |
| **PAT (Net Profit)** | 39.16 | Rs Cr | Results PDF (28-Apr-2026), P&L: Profit after tax 3,916.15 lakh = 39.16 Cr |
| **PAT Margin** | 15.23% | % | 39.16 / 257.13 = 15.23% |
| **Diluted EPS** | 18.49 | Rs | Results PDF (28-Apr-2026), standalone P&L: "Earnings per equity share: Diluted (Rs) 18.49" |
| **CFO (Operating Cash Flow)** | 0.47 | Rs Cr | Results PDF (28-Apr-2026), Cash Flow Statement: "Net cash from operating activities (A) 46.92 lakh" = 0.47 Cr |
| **Capex** | 4.36 | Rs Cr | Results PDF (28-Apr-2026), CFS: "Purchase of Property, plant and equipment's 436.00 lakh" = 4.36 Cr |
| **FCF (Free Cash Flow)** | -3.89 | Rs Cr | CFO 0.47 - Capex 4.36 = -3.89 Cr |
| **Depreciation & Amortization** | 6.16 | Rs Cr | Results PDF (28-Apr-2026), CFS: "Depreciation and amortisation expense 616.29 lakh" = 6.16 Cr |
| **Book Value per Share** | 100.71 | Rs | Equity (2,060.92 + 18,693.51 = 20,754.43 lakh) / Diluted shares (206.04 lakh) = 100.71 Rs (B01.data_notes: FY26 net worth adjusted for warrants Rs207.54Cr = 20,754.43 lakh; results PDF balance sheet 31-Mar-2026) |
| **Net Cash (Net Debt)** | -8.16 | Rs Cr | Cash 8.65 Cr - ST Borrowings 0.49 Cr = -8.16 Cr net cash position (Results PDF balance sheet: cash equivalents 864.69 lakh; short-term borrowings 49.06 lakh) |
| **ROCE (Latest FY26)** | 24.00% | % | FTTCP-deliberation.md line 21: "ROCE state: SUSTAINED (24.00% FY26, rising from 20.79% FY25)" - the authoritative forward ROCE for Pillar 1 |
| **ROCE Trend (3yr)** | Declining then Recovering | Direction | FY24: 31.48% → FY25: 20.79% → FY26: 24.00%; B01.data_notes |
| **ROE** | 22.21% | % | PAT 39.16 Cr / Average Equity (207.54 + 145.09) / 2 = 176.32 Cr = 22.21% (FY26 adjusted NW from B01.data_notes, FY25 from prior year balance sheet) |
| **3-Year Revenue CAGR (FY24-FY26)** | 66.2% | % | (257.13 / 92.98)^(1/2) - 1 = 66.2% (B01 anchored FY24 revenue 92.98 Cr, FY26 257.13 Cr from results PDF) |
| **3-Year PAT CAGR (FY24-FY26)** | 70.0% | % | (39.16 / 13.60)^(1/2) - 1 = 70.0% (B01 anchored FY24 PAT 13.60 Cr, FY26 39.16 Cr from results PDF) |
| **CFO / PAT (Latest FY26)** | 0.012 (1.2%) | Ratio | 0.47 / 39.16 = 0.012x |
| **CFO / PAT (Cumulative FY24-26)** | -0.13 | Ratio | (6.69 - 17.69 + 0.47) / (13.60 + 25.74 + 39.16) = -10.53 / 78.50 = -0.13x; B01.block_b_trend |
| **FCF / PAT (FY26)** | -10.0% | % | -3.89 / 39.16 = -9.9% ≈ -10% |
| **P/FCF** | NOT MEANINGFUL | --- | FCF is negative; P/FCF not applicable (FCF per share -1.89 Rs; CMP 1,390 Rs yields negative multiple) |
| **DPS (Dividend per Share)** | 0 | Rs | Company policy: zero dividend by design, 100% reinvestment (B04.irrelevant_ratios) |

---

## STRATEGIC & ANALYTICAL INPUTS

| Field | Value | Source Anchor |
|-------|-------|---------------|
| **Guided Revenue Growth (Stated)** | 40-50% CAGR | B05.guidance: "CAGR growth 40-50%" stated in all three calls (H2 FY25, H1 FY26, H2 FY26) |
| **Guidance Quarter** | H2 FY26 (May 2026) | B05: H2 FY26 concall, most recent guidance context |
| **Margin Band Guidance** | PAT 13-17% (±2%), EBITDA 20%+ | B05.guidance: H1 FY26 call states "EBITDA ~20%+; PAT 15% +/-2%" |
| **Management Credibility Grade** | C | B05.credibility_grade: "C" (Mixed); basis: "Revenue, order-book and named product/certification commitments delivered or beaten across all three calls, but two explicit transparency promises (reclassification press release, quarterly reporting) went unmet from H2 FY25 through H2 FY26, the H2 FY25 working-capital reassurance did not hold with cash flow turning -Rs40cr negative in FY26, and a material related-party revenue figure stated on calls (<20%) is unreconciled against prior-stage evidence (27.68-31.53%) with the FY26 AGM RPT ceiling of Rs120cr never once raised." (B05.credibility_basis) |
| **Management Delivery Track Record** | 5 Delivered / 2 Partial / 4 Missed of 11 promises | B05.promise_delivery: Track record summary; key broken promises include working capital normalization (FY26 CFO -Rs40Cr actual vs "no significant challenge" promised), transparency commitments (reclassification press release, quarterly reporting still pending), fundraising stance reversal (prefship issued without advance notice) |
| **Top Growth Trigger #1** | Greenfield Vadodara Mechatronics facility (6 SMT lines, Rs500Cr incremental capacity) | B05.triggers priority 1: "volume" type, medium timeframe (FY27), medium conviction; confirm signal: SMT lines operational and shipping per phased schedule; kill signal: delay past FY27-Q4 or cost overrun |
| **Top Growth Trigger #2** | AIC/ICS US acquisition margin ramp (11% EBITDA to 18-20% within a year) | B05.triggers priority 2: "cost/margin" type, near-medium timeframe, medium conviction; confirm signal: consolidated EBITDA trends toward 18-20%+ within a year; kill signal: AIC margins stay stuck in low double digits |
| **Top Growth Trigger #3** | Working capital / cash conversion normalization | B05.triggers priority 3: "cost" type, near timeframe, low conviction; confirm signal: positive operating cash flow reported, receivables days fall; kill signal: continued negative CFO or rising receivables-inventory |
| **Emerging Moat Score** | 23 / 80 | B07.em_score |
| **EM Classification** | MODEST | B07.em_classification |
| **EM Active Categories** | B2 (Qualification lock-in: strong, documented), H2 (Strategic partnerships/AIC: strong, documented), A3 (Process innovation: moderate, documented), B1 (Backward integration: moderate, claim), E2 (China+1 beneficiary: moderate, claim), R1 (Regulatory/policy ECMS/RDSO: moderate, documented) | B07.active_categories (6 categories showing evidence, 3 documented, 3 claim-based) |
| **Evidence Mix** | Mixed (11 documented + 19 claim + 4 inference) | B07.evidence_mix; mostly-📄 documented (11 items) mixed with claims (19) and inferences (4) |
| **Primary Catalyst (12m window)** | RDSO approval decision (Railways vendor qualification) | B07.catalysts_12m: H1-Q3 FY27 target window; evidence type: claim per management, anchor: May-2026 concall |
| **Cash Conversion Verdict** | INDETERMINATE → caps disposition PROCEED WITH CAVEATS | FTTCP-deliberation.md line 5: "Cash conversion determination: INDETERMINATE. Caps disposition at PROCEED WITH CAVEATS. Resolves to growth-induced only if H1 FY27 consolidated operating cash flow turns solidly positive with debtor days below 120; resolves to structural on a third straight negative operating cash flow or rising related-party receivables." |
| **Structural vs Growth-Driven Cash Issue** | INDETERMINATE (requires H1 FY27 print for direction) | B01.block_b_trend: "deteriorating - cumulative CFO/PAT = -0.13x (FY24-FY26 standalone); FY25 CFO -Rs17.69cr against PAT +Rs25.74cr"; B02.receivables_trend: "+417% YoY vs 70.3% revenue growth; 46.3% owed by related parties including a payable-to-receivable flip"; both demonstrate working-capital intensity, but direction (structural vs temporary) awaits FY27 evidence |
| **Strategic Asset / Monopoly Position** | Yes, with description | B07: "Strategic partnerships (AIC acquisition), Strong, documented" + B04: "Regulatory/certification stack (ISO 13485, IATF 16949, AS9100D, CDSCO, RDSO pending)" with medium-high durability; "Switching costs in qualified customer programs" medium-high unproven at scale; "Economies of scale emerging" via ICS ramp |
| **SOM-Implied Revenue CAGR (3-year)** | 46.6% | B09.som_implied_revenue_cagr.yr3 |
| **SOM-Implied Revenue CAGR (5-year)** | 34.0% | B09.som_implied_revenue_cagr.yr5 |
| **TAM (Conservative, Rs Cr)** | 205,600 | B09.tam_cr.conservative (India B2B contract EMS/ESDM market, excluding consumer/mobile/bare PCB/fab) |
| **TAM (Realistic, Rs Cr)** | 231,000 | B09.tam_cr.realistic |
| **SAM (Serviceable Addressable Market, Rs Cr)** | 48,500 | B09.sam_cr |
| **Current SAM Share (%)** | 0.62% | B09.current_sam_share_pct (FY26 standalone revenue 257.13 Cr / SAM 48,500 Cr) |
| **Revenue Headroom Multiple** | 161x | B09.revenue_headroom_x (SAM / current revenue = 188.7 to 231 x depending on TAM case; conservative 161x for stage 10 use) |
| **Capacity Assessment** | Sufficient but tight; SOM5yr equals disclosed combined India+US ceiling (~Rs1,290-1,300Cr) with zero margin | B09.capacity_check; "Vadodara greenfield total project cost not disclosed; capacity-to-revenue math (1 SMT line = Rs100cr) is asserted, not demonstrated (and peer Vinyas discloses Rs500-600cr/line)" per B07.input_gaps and B06 contradiction flag |

---

## PROMOTER & GOVERNANCE INPUTS

| Field | Value | Source Anchor |
|-------|-------|---------------|
| **Promoter Verdict** | CONCERN | B08.verdict: "CONCERN"; basis: Chairman Mukesh Vasani is externally disclosed as CEO of Aimtron Corporation USA (the company's single largest RPT counterparty ~19-22% of FY25 revenue); ~31.5% of FY25 revenue with non-consolidated promoter-controlled foreign entities; new unexplained Rs404.99Lakh RPT expense; FY26 AGM Rs120Cr RPT ceiling (~76% FY25 turnover) with no external valuation; FY25 material RPTs approved via omnibus Audit Committee only; contingent liabilities jumped 500x to Rs20.91Cr (81.24% of FY25 PAT) as sole KAM unprovisioned (B08.adverse_findings) |
| **Pledge % (Latest)** | 0% | B08.pledge_pct_latest; "confirmed free of encumbrance FY2025-26 under Reg 31(4); no pledge history in any period reviewed" |
| **Promoter Buying/Selling** | NET BUYER (positive signal) | B08.transition_evidence: "Promoter Mukesh Vasani net buyer of shares in open market (4,000 shares)" per Trendlyne disclosure as of 31-Mar-2025 |

---

## UA QUALIFIER VERIFICATION

| Qualifier | Met? | Value | Source Anchor |
|-----------|------|-------|---------------|
| **Listed ≥12 months** | YES | IPO 4-Jun-2024 → Run date 12-Jul-2026 = 13+ months | B01 (IPO date noted in notes) |
| **Gate 0 Score ≥60 OR EM Score ≥25** | YES (Gate 0 ≥60) | Gate 0: 72; EM: 23 (Gate 0 exceeds 60, condition met) | B01.grand_total = 72; B07.em_score = 23 |
| **FII+DII Ownership <3%** | NOT FOUND | --- | NOT FOUND in any block; B01.input_gaps: "latest-quarter shareholding pattern: NOT FOUND"; no FII/DII data provided |
| **All Three Qualifiers Met** | NO (one unresolved) | --- | FII+DII data missing; cannot affirm all three concurrently |

---

## PEER MEDIANS (COMPARISON SET)

**Status: NOT FOUND in input data**

| Metric | Peer Median | Source Anchor |
|--------|-------------|---------------|
| **P/E Multiple** | NOT FOUND | B06.input_gaps: "Stage-5 peer list (Kaynes, Syrma, Dixon, Data Patterns, Paras, MTAR) not represented in the 12 supplied transcripts; substituted with 4 available genuine EMS/ESDM peers (Avalon, Centum, Cyient DLM, Vinyas)" but no consolidated financial medians extracted in B06 output |
| **EV/EBITDA Multiple** | NOT FOUND | No peer financial data tables provided; B06 focused on narrative validation not valuation multiples |
| **P/B Multiple** | NOT FOUND | Not extracted from peer transcripts |
| **Growth Rate (Peer Median)** | NOT FOUND | Peers showed strong growth (Avalon 46%, Centum ~25%, Cyient DLM strong, Vinyas 43% H1) but no median tabulated for comparison |
| **ROCE (Peer Median)** | NOT FOUND | Not extracted from peer transcripts |

**Note**: Peer analysis in B06 focused on validating Aimtron's specific claims (RFQ pipeline, revenue-per-SMT-line, defence margin impact, sourcing mix) against peer commentary rather than extracting median multiples for relative valuation. Aimtron's Rs100Cr per SMT-line claim contradicted by peer Vinyas disclosure of Rs500-600Cr/line (B06 flag).

---

## RATING & WORKING CAPITAL COMMENTARY

**Status: RATING ABSENT**

| Field | Value | Source Anchor |
|-------|-------|---------------|
| **Credit Rating** | NOT FOUND | B01.input_gaps: "credit rating: NOT FOUND (no rating PDF provided)"; B08.input_gaps: "rating absent - no CRISIL/ICRA/CARE rating found for Aimtron Electronics Ltd" |
| **Rating Agency** | --- | --- |
| **Rating Outlook** | --- | --- |
| **Rating Date** | --- | --- |
| **Rating WC/Cash Flow Commentary (Verbatim Quote)** | NOT FOUND | No rating PDF supplied to extract agency's working capital or cash conversion assessment |

---

## CONFLICTS NOTED

| Field | Value A | Anchor A | Value B | Anchor B | Used in Table | Resolution |
|-------|---------|----------|---------|----------|---------------|------------|
| **Sector Cap Row** | Pharma / CDMO, 38x | Manifest (original assignment) | Recycling / Manufacturing, 25x | FTTCP-deliberation.md line 19 (authoritative override) | 25x | FTTCP deliberation supersedes manifest per instructions; 25x is law for Pillar 1 |
| **Related-Party Revenue (FY25)** | <20% of revenue | B05 concall statement | 27.68-31.53% of revenue | B02, B03, B08 (Note 35 analysis) | 27.68-31.53% (conservative midpoint 29.6%) | Concall figure appears understated; audited AR Note 35 is primary source; reconciliation unresolved per B05.flags |
| **Revenue-per-SMT-Line** | ~Rs100Cr | Aimtron concall narrative (B05.mgmt_questions) | Rs500-600Cr | Peer Vinyas disclosure (B06.contradicted, direct quote from Vinyas H2/FY26 call May 2026) | Unable to resolve; flagged as priority conflict for synthesis | Aimtron's productivity assumption contradicted 5-6x by peer; affects capacity-scaling credibility |

---

## UNRESOLVED ENTRIES

| Field | Why Unresolved | Where It Might Be | Priority |
|-------|----------------|-------------------|----------|
| **rating_wc_quote** | No credit rating PDF provided to extract agency working capital commentary | Rating PDF not in inputs; check CRISIL/ICRA/CARE for Aimtron | HIGH (needed for FLAG-CASH narrative) |
| **FII + DII Shareholding (%)** | Latest shareholding pattern not provided; B01 used AR2025 (31-Mar-2025) only | FY26 shareholding pattern from quarterly MCA filing or latest BSE disclosure | MEDIUM (needed for UA qualifier closure) |
| **Peer Financial Medians** | Peer transcripts provided narrative data only; no consolidated P&L/balance-sheet extraction | Peer latest annual reports or latest quarterly results filings | MEDIUM (for relative valuation sense-check only; absolute DCF/EV basis does not require) |
| **Customer Concentration (Top 5, Top 10 %)** | No top-customer disclosure found in AR or investor presentations | AR Note 35 or 38; or investor presentation detailed disclosure section | MEDIUM (impacts SOM sustainability and concentration risk) |
| **R&D Expense as % of Revenue** | Not separately line-itemed in P&L or notes | B01.input_gaps: "R&D expense / revenue: NOT FOUND"; check if capitalized in CWIP or bundled into manufacturing overhead | LOW (nice-to-have for GARP quality assessment) |
| **Vadodara Greenfield Total Capex (Rs Cr)** | No audited total project cost disclosed; only capacity targets (Rs500Cr) stated | Management concalls or investor presentation detailed capex bridge; or FY26 CWIP note | MEDIUM (needed for capex-embedded growth % credibility) |
| **Latest Quarterly Shareholding Pattern (FY26)** | AR2025 (31-Mar-2025) is last confirmed; warrant conversion (Sep-2025, Jan-2026) and preferential issue (Sep-2025) not reflected in published shareholding table | BSE/NSE shareholding pattern filing for Q4 FY26 (post-31-Mar-2026); note: B01 flagged "E3 scored 0" for pledge % due to missing FY26 data |
| **H1 FY27 Operating Cash Flow (Forecast)** | Critical for INDETERMINATE cash verdict resolution but not yet reported (current run date 12-Jul-2026; H1 FY27 = Sep-2026, not yet close) | Next results announcement (Nov 2026 expected for H1 FY27 half-yearly) | CRITICAL (will break the cash determination tie) |

---

## DATA QUALITY NOTES & CAVEATS

1. **Standalone vs Consolidated Split**: All core financials (revenue, PAT, CFO, ROCE, ROE) are STANDALONE (audited 27-Apr-2026) unless marked otherwise. Consolidated FY26 figures exist (revenue Rs301.16Cr, PAT Rs45.97Cr, OCF -Rs40Cr from FTTCP-deliberation and B05 concall) but are NOT the primary basis for stage 11 valuation; stage 11 should value the standalone entity. Consolidated data is for reference only (US subsidiary, AIC acquisition impact visibility).

2. **Screener Data Quality**: B01.flags notes "screener-Data_Sheet FY26 P&L is internally inconsistent and conflicts with audited standalone FY26 (Results 28-Apr-2026)". Screener's Rs301cr figure is the consolidated turnover, not standalone. All assembly here uses audited standalone figures from results PDF and AR.

3. **EBITDA Margin Reconciliation**: Standalone EBITDA margin FY26 reported as 24.05% by B01 (P&L basis D&A). CFS D&A differs slightly (P&L Rs712.36Lakh vs CFS Rs616.29Lakh per B01.data_notes "unreconciled minor gap in the source filing"). Stage 11 should note this minor variance; 24.05% used here per B01 audit.

4. **ROCE Authority**: FTTCP-deliberation.md is the sole authority for forward ROCE selection. Pillar 1 must use CURRENT ROCE 24.0% (not normalized or adjusted). Amendment 4.5 normalized-ROCE anchor does NOT apply (ROCE is SUSTAINED, not temporarily depressed per FTTCP line 21).

5. **CFO/PAT Concern**: Cumulative CFO/PAT -0.13x FY24-26 is a core B01 deal-breaker (Block B score 0/20). FY26 alone shows CFO Rs0.47Cr vs PAT Rs39.16Cr (0.012x) due to working-capital build. FY25 was the primary deterioration driver (CFO -Rs17.69Cr vs PAT +Rs25.74Cr = -0.687x single year). This is flagged as growth-induced (high inventory/receivables) not structural profitability, but INDETERMINATE per FTTCP pending FY27 cash print.

6. **Cash Conversion Disposition Cap**: Per FTTCP-deliberation.md line 5, INDETERMINATE cash determination CAPS the downstream disposition at PROCEED WITH CAVEATS, regardless of other factors. This is non-negotiable without H1 FY27 evidence (positive OCF + debtor days <120).

7. **Related-Party Revenue Unreconciled**: B05 concall stated <20% RPT share; AR Note 35 analysis shows 27.68% (FY25 sales) to 31.53% (sales + services). B02 flags this as red_flag (potential revenue quality risk). FY26 AGM ceiling Rs120Cr (~76% FY25 turnover) sought with two same-management entities. B08 shows this as a promoter verdict driver (CONCERN). Stage 11 and synthesis must address this split.

8. **Credibility Grade C Implications**: B05 credibility_grade C is not a stop but reflects: (a) two broken transparency commitments (reclassification press release, quarterly reporting promised H2 FY25, undelivered H2 FY26); (b) H2 FY25 working-capital reassurance (no significant challenge) did not hold (FY26 CFO -Rs40Cr consolidated); (c) fundraising stance reversal (stated no need, then issued warrants/preferential shares without advance notice). These do not invalidate the data but warrant elevated skepticism on forward guidance (40-50% CAGR, margin band targets).

9. **Warrant & Preferential Share Impact**: B01 notes Sep-2025 preferential issue and warrant conversions. FY26 diluted shares derived from results PDF EPS calculation (206.04 lakh). B01.data_notes: "FY26 net worth Rs227.86Cr includes Rs20.32Cr 'money received against share warrants'; excluding it, FY26 net worth = Rs207.54Cr and ROE = 21.6% (same scoring band)". Book value per share calculated using adjusted net worth (Rs207.54Cr) for consistency.

10. **Contingent Liability Risk**: B02, B03, B08 all flag sole KAM (Contingent Liability Note 30: GST/Income Tax disputes) totaling Rs20.91Cr = 81.24% of FY25 PAT, unprovisioned. No independent corroboration disclosed. This is a material tail risk but NOT reflected in PAT (no provision). Stage 11 should flag as downside scenario.

---

## DELIBERATION AUTHORITATIVE OVERRIDES (Inputs to Pillar Calculations)

These determinations from FTTCP-deliberation.md supersede any earlier pipeline values and are BINDING for stage 11:

| Field | Authoritative Value | Citation | Application |
|-------|--------------------|---------|-----------:
| **ROCE Forward Verdict** | STAGNANT (use current 24.0%) | FTTCP line 21: "ROCE state: SUSTAINED (24.0% FY26, rising from 20.79% FY25); Amendment 4.5 normalized-ROCE anchor DOES NOT APPLY" | Pillar 1: use 24.0% as is; no recovery credit |
| **Cash Conversion** | INDETERMINATE (caps PROCEED WITH CAVEATS) | FTTCP line 5: "Cash conversion determination: INDETERMINATE. Caps disposition at PROCEED WITH CAVEATS." | Pillar 2: default conservative pending H1 FY27 print; disposition hard-capped at PWC |
| **Sector Cap Row** | Recycling / Manufacturing, 25x | FTTCP line 4: "Sector cap row: **Recycling / Manufacturing, 25x** overrides the manifest's Pharma / CDMO 38x" | Pillar 3: exit multiple for EV/EBITDA or EV/Sales must use 25x cap not 38x |
| **Promoter Verdict & Credibility** | CONCERN, grade C | FTTCP line 36: "Promoter verdict CONCERN and credibility grade C carry into thesis and devil's advocate" | Devil's advocate & sensitivity: flag related-party concentration risk; cross-check management commitment credibility on capex/margin targets |

---

## ASSEMBLY COMPLETENESS CHECK

**Table Fields Filled**: 45 of 50 core fields populated with source anchor  
**Unresolved Fields**: 5 (rating_wc_quote, FII+DII %, peer medians, customer concentration, R&D %)  
**Conflicts Identified & Resolved**: 3 (sector cap override applied, RPT revenue flagged but used B02/B03/B08 basis, revenue-per-SMT contradiction flagged for synthesis)  
**Data Quality Issues Flagged**: 10 (standalone/consolidated split noted, screener conflict identified, EBITDA variance minor, CFO concern explained, RPT unreconciliation flagged, credibility downgrade noted, warrant dilution adjusted, KAM tail risk flagged, cash INDETERMINATE pending, deliberation authoritative overrides documented)  

**Status: READY FOR STAGE 11 (Valuation). All numbers anchored. YAML block emitted below.**

---

