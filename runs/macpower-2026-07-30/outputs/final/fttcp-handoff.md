# FTTCP HANDOFF DOSSIER, MACPOWER (Macpower CNC Machines Ltd)

Run folder: runs/macpower-2026-07-30. CMP Rs 1,481. Run date 2026-07-30. First workup, concalls available (not no-concall mode). Standard operating business, capital goods CNC machine tool maker. Four standard transitions. Drive folder link: NOT PROVIDED.

Machine anchored archive for a separate FTTCP v1.2 deliberation session that will not have the source PDFs. Block references (B04 etc.) are intended here. Every figure carries its anchor. NOT FOUND is the only fill for absent data.

Deliberation confirmed inputs and overrides (authoritative, from outputs/final/fttcp-deliberation.md):
- Sector cap corrected to Cables / Industrial products 25.0x, absolute, from the manifest's wrong Pharma / CDMO 38x (deliberation Sec 1, Override context; B10 flags).
- Override 1: trailing P/E corrected to 38.1x on TTM EPS about Rs 38.9 (includes strong Q1 FY27), not roughly 45x on FY26 only profit (deliberation Sec 2).
- Override 2: destination (exit) PE set to 25.0x, equal to the additive track after the UA multiplier is capped by the 25x sector cap; framework consistent, not a hand set round number (deliberation Sec 2).
- Override 3: earnings basis set to one year forward, exit multiple applied to FY27 forward EPS (deliberation Sec 2).
- Gate disposition PROCEED WITH CAVEATS, capped by INDETERMINATE cash (deliberation Sec 3).
- Valuation AVOID on valuation at CMP (deliberation Sec 3).
- Cross family FTTCP grade did not run (no Gemini/GPT key; verifiers/fttcp_crossgrade.py SKIPPED); FTTCP confidence treated one notch lower per flag rule; no third family divergence to resolve (deliberation Sec 4).

Role outputs:
- Role 1 (FTTCP transition): composite plus 2 of 8, DEEP WATCH leaning AVOID; only revenue firing forward (deliberation Sec 1, Sec 3).
- Role 2 (valuation and sizing, B11): AVOID on valuation, destination 25.0x additive governing / 16.5x RRM, base FV Rs 1,075 / Rs 710, Hurdle STOP, entry Rs 440 to 550, MoS Rs 440, prob weighted 3yr CAGR minus 10.4% (B11).
- Role 3 (thesis B14 and devil B15): thesis AVOID, entry Rs 440 to 550, MoS Rs 440, position Small (B14); devil overall SURVIVES, valuation_safety survives, growth/moat/management weakened, AVOID over determined (B15).

Block index carried: B00 inputs, B01 gate0, B02 notes, B03 ardeep, B04 bizmodel, B05 concall, B06 peers, B07 emoat, B08 promoter, B09 tam, B10 valinputs, B11 valuation, B12a source fidelity, B12b redflag, B12c framework, B12d peer, B13 synthesis, B14 thesis, B15 devil, confidence.yaml.

---

## 1. Transition data series

### 1.1 Topline

| Year | Revenue (Rs cr) | Growth YoY | Anchor |
|---|---|---|---|
| FY24 | NOT FOUND (absolute) | NOT FOUND | FY25 revenue +8.6% over FY24 (B02 Finding #1/#3) implies FY24 base, not separately anchored |
| FY25 | 261.82 | +8.6% | Rs 261.82 cr (B03 guidance_table); +8.6% YoY (B02) |
| FY26 | 333.18 | +27.3% | Rs 333.18 cr (B10 revenue_fy26_cr); +27.3% YoY (B03 guidance_table) |
| Q1 FY27 | NOT FOUND (absolute) | +56.1% | +56.1% YoY (deliberation Sec 1; B10 note) |

Three year revenue CAGR 17.5% (B10 revenue_cagr_3yr_pct); three year PAT CAGR 18.1% (B10 pat_cagr_3yr_pct). Order book Rs 456 cr, 1.37x FY26 revenue (B10; deliberation Sec 1); FY25 close order book Rs 330.95 cr vs FY25 start Rs 262.38 cr (B04 must_track); FY26 close Rs 406 cr actual (B05 promise_delivery).

### 1.2 Margin

| Year | Gross margin | EBITDA margin | Net (PAT) margin | Anchor |
|---|---|---|---|---|
| FY24 | NOT FOUND | 14.70% | 10.00% | EBITDA 14.70% (B04 must_track); PAT margin 10.00% front matter KPI (B03) |
| FY25 | NOT FOUND | 15.87% | 9.72% (direct P&L) / 12.00% (AR Note 38 conflicting) | EBITDA 15.87% (B04); PAT 9.72% direct P&L + KPI p.4 vs Note 38vi 12.00% (B03 discrepancy, ~2.3pp unreconciled) |
| FY26 | NOT FOUND | 16.2% | 9.72% | EBITDA margin 16.2% (B10 ebitda_margin_pct); PAT margin 9.72% (B10 pat_margin_pct) |
| Q1 FY27 | NOT FOUND | 16.2% | ~10.1% | EBITDA 16.2% (deliberation Sec 1); PAT ~10.1% (B11 report note) |

Gross margin not isolable by year: clean COGS (materials plus manufacturing overhead) not separately reported in P&L notes (B01 data_notes). FY26 EBITDA Rs 53.90 cr (B10 ebitda_fy26_cr); FY26 PAT Rs 33.87 cr, EPS Rs 33.86 (B10). Margin definition trap: AR discloses two inconsistent pairs, EBITDA 15.87% p.4 vs Operating Profit 13.44% p.85, PAT 9.72% p.4 vs Net Profit 12.00% p.85, unreconciled (B04 flags; B03 triple_pass discrepancy rank 3).

### 1.3 Cash conversion

| Year | OCF (Rs cr) | OCF/EBITDA | CFO/PAT | Debtor days | WC % of sales | Anchor |
|---|---|---|---|---|---|---|
| FY24 | NOT FOUND | NOT FOUND | 0.70x | ~26 | NOT FOUND | CFO/PAT 69.9% (B03); debtor days ~26 (B02 receivables_trend); FCF +Rs 629.71 lakh (B03) |
| FY25 | NOT FOUND | NOT FOUND | 0.27x | ~39 | NOT FOUND | CFO/PAT 27.4% (B03); debtor days ~39 (B02); FCF -Rs 899.87 lakh (B03) |
| FY26 | 14.03 | 0.26x | 0.41x | NOT FOUND | NOT FOUND | CFO Rs 14.03 cr (B10 cfo_fy26_cr); OCF/EBITDA = 14.03/53.90 derived (B10); CFO/PAT 0.41x (B01/B10); FCF Rs 3.06 cr (B10) |

Cumulative CFO/PAT FY24 to FY26 = 0.4538x, below 0.50 (B01 deal_breakers). Cumulative FCF/PAT 0.0043x across the window (B01 flags). FY26 WC deterioration: WC days plus 27.19 vs FY24 (B01 flags). Inventory days ~181 (FY24) to ~223 (FY25) (B02 Finding #8). Payable days ~70 to ~98 (B02 Finding #2).

Rating agency working capital commentary, VERBATIM: NOT PROVIDED. No credit rating PDF was in inputs; B10 rating_wc_quote records "NOT PROVIDED (no rating PDF in inputs)". This is the single missing item that keeps the cash determination INDETERMINATE rather than resolvable to STRUCTURAL or GROWTH-INDUCED (B10 unresolved; deliberation Sec 1). Management proxy on the same question, Q4 FY26 call: conversion "will not improve rapidly" (B12b, Q4 FY26 call p.21-22).

### 1.4 ROCE

| Year | ROCE | ROE | Capital employed basis | Anchor |
|---|---|---|---|---|
| FY24 | 26.70% | 20.15% | AR Note 38(vi) audited | B02 Finding #10 |
| FY25 | 23.75% | 17.65% | AR Note 38(vi) audited | B02 Finding #10; B10 roce_fy25_pct / roe_fy25_pct |
| FY26 | NOT FOUND (audited); screener 29.1% (basis unspecified) | NOT FOUND | conflict: AR Note 38 basis 23.75% used vs screener 29.1% different capital employed basis | B10 conflicts; B11 uses 23.75% |

Supporting: Net capital turnover 2.02x (FY24) to 1.83x (FY25); Return on Investment 51.34% to 45.92% (B02 Finding #10). ROCE forward verdict STAGNANT: fall ~295 bps short of the 500 bps TEMPORARILY DEPRESSED trigger, premium ~24%, not DECLINING (capex will earn) (deliberation Sec 1). Stage 11 used 23.75% (AR Note 38), normalization route NONE, recovery NOT credited (B11 pillar_detail).

---

## 2. Catalyst inventory

From B05.triggers (8) and B07.catalysts_12m (5).

B05 triggers:
1. Capacity utilisation ramp to ~90% on 2,500 machine base. Tier: claim. Window: near (FY27). Confirm: utilisation trending toward 90%. Kill: stalls below 85% or new bottleneck. Conviction H (B05 triggers p1).
2. NEXA / high end mix rising past ~40% of order book. Tier: claim. Window: near-medium. Confirm: NEXA share of executed order book keeps rising. Kill: NEXA share plateaus or reverses. Conviction H (B05 p2).
3. 13-acre Metoda land execution (de-bottleneck plus backward integration). Tier: claim. Window: medium (FY27). Confirm: lease signed, construction milestones within ~12 months. Kill: slippage beyond FY27. Conviction M (B05 p3).
4. 60-acre govt greenfield land / 10,000 machine plan. Tier: claim. Window: long. Confirm: binding signed land agreement. Kill: continued delay beyond FY27 or policy denial. Conviction L-M (B05 p4). SHARED CATALYST.
5. Defence / aerospace vertical scale-up. Tier: claim. Window: medium. Confirm: defence moves single digit to double digit % of revenue. Kill: bid conversion stuck ~10-12% with flat revenue share. Conviction M (B05 p5). CONTRADICTED by JYOTICNC (B06).
6. Backward integration toward 25% EBITDA margin. Tier: claim. Window: long, multi-year. Confirm: margin structurally clears 18-19% without one-offs. Kill: margin range-bound 16-18% for multiple years. Conviction M (B05 p6).
7. JV / technology transfer with foreign partner. Tier: claim. Window: long, gated on land. Confirm: signed agreement / named counterparty. Kill: land delay persists beyond FY27 or partner exits. Conviction L (B05 p7).
8. Export market development (Europe / Gulf). Tier: claim. Window: deprioritised. Confirm: management re-elevates export as priority. Kill: remains "not a focus". Conviction L (B05 p8).

B07 catalysts_12m:
- 13-acre plant construction / utilisation ramp toward ~90% FY27. Tier: claim. Window 12m. Anchor Q4 FY26 concall (Jun-2026).
- Defence / aero bid book (Rs 304-376 cr under evaluation) converting to firm orders. Tier: claim. Window 6-12m. Anchor Q3/Q4 FY26 concalls; Q1 FY27 Inv Pres.
- 60-acre land signing decision (or a 4th slip). Tier: claim. Window 12m, high uncertainty. Anchor B05 promise-delivery record; Q3/Q4 FY26 concalls.
- NEXA / high end mix progression in order book (~39-40%). Tier: claim. Window ongoing/12m. Anchor Q3/Q4 FY26 concalls; Q1 FY27 Inv Pres.
- JV / technology transfer NDA-to-agreement conversion. Tier: claim. Window 12m, unconfirmed. Anchor Q2 FY26 concall (Nov-2025).

Dropped triggers (B05): car-case business (2 OEM prospects, Q4 FY26 sampling promised Q2, never re-mentioned); export push (EMO Germany, explicitly deprioritised Q4 FY26). Timeline slippages (B05): 60-acre land Dec-2025 to Feb/Mar-2026 to undated "3-4 months" (Q4 FY26); original plan traced to March 2024; JV frozen 3 quarters; 25% margin timeline narrowed to the undated 60-acre land under analyst pressure.

---

## 3. Flags with complete underlying findings

### FLAG-PROMOTER: not active

B08 verdict TRUSTWORTHY. Scorecard clean 5 / caution 5 / red 0. Deal breakers: none. Promoters Rupesh J. Mehta, Nikesh J. Mehta, holding 73.2%, pledge 0% across 12 quarters (Sep-2023 to Jun-2026), corroborated by FY26 SEBI Reg 31(4) declaration (B08). Adverse findings (all minor/immaterial): NSE fine Rs 23,600 for 4-day RPT filing delay, half-year ended 31-Mar-2022 (VERIFIED, AR CGR p.101); legacy GST ITC demand notice IPO services 2018 (UNVERIFIED, DRHP web synthesis); legacy VAT dispute FY2011-12 ~Rs 16.08 lakh principal (UNVERIFIED); two family proprietorship RPTs combined ~Rs 45 lakh, ~0.017% of revenue, Audit Committee approved (VERIFIED, AOC-2 p.67); internal auditor role held by 3 people within ~6 weeks Jan-Feb 2025 (VERIFIED, p.60-61); CFO succession Jan-2025 from 21-year non-family CFO to same-surname Mehta-family CFO Vishal B. Mehta (VERIFIED). Transition evidence: FII 0.00% (Sep-2023) to peak ~1.32% (Mar-2025) to 0.57% (Jun-2026), DII 0.39% (Jun-2026); dedicated FII (10-Jul-2026) and DII (5-Jun-2026) one-on-ones; pledge 0% throughout (B08 transition_evidence).

### FLAG-CASH: active, determination INDETERMINATE

Every cited item behind it:
- CFO/PAT trend 0.70x (FY24) to 0.27x (FY25) to 0.41x (FY26); cumulative 0.4538x below 0.50 (B01 flags/deal_breakers; B10 cfo_pat_ratio 0.41).
- Trade receivables +57.5% YoY (Rs 3,432.40 lakh vs Rs 2,179.51 lakh) against revenue +8.6%; turnover down 33% (9.32x vs 13.97x); >6-month ageing 15.4% of gross from 12.2% (B02 Finding #1, Note 9 p.149/174, Note 38vi p.185).
- Trade payables +28.0% YoY, MSME dues +81.4% (Rs 2,553.13 lakh); payable days ~70 to ~98 (B02 Finding #2, Note 18 pp.155-156).
- Raw material inventory +50.9% YoY (Rs 10,096.04 lakh); inventory days ~181 to ~223 (B02 Finding #8, Note 7 p.148).
- Investment portfolio (Rs 516.16 lakh) fully liquidated to zero to fund working capital (B02 Finding #6, Note 8 p.148).
- FCF turned negative FY25: -Rs 899.87 lakh vs +Rs 629.71 lakh FY24 (B03 flags).
- Management admission: conversion "will not improve rapidly", Q4 FY26 call p.21-22 (Kanishk); rising inventory Rs 145 cr and receivables Rs 46 cr (B12b missed MAJOR).
- Capex commissioning timeline: FY26 capex Rs 10.97 cr per B10 (Rs 15.36 cr per Q4 FY26 concall); active CWIP Rs 485.84 lakh (B02 Finding #7); 13-acre Metoda capex Rs 30-35 cr immediate/FY27; FY27 total capex Rs 30-40 cr; phase-1 new plant Rs 125 cr over 15-16 months post land (B05 guidance).
- Receivables composition: net receivables +57.5%, >6-month bucket 15.4% of gross (B02 Finding #1).
- Rating agency verbatim quote: NOT PROVIDED (no rating PDF in inputs, B10 rating_wc_quote).

Determination INDETERMINATE because the trajectory 0.70 to 0.27 to 0.41 is non-monotonic and the rating rationale is absent (B11 report; deliberation Sec 1). Falsifier for STRUCTURAL: FY27 CFO/PAT below 0.5x with receivable AND inventory days still rising (deliberation Sec 1; B14 thesis_broken).

### FLAG-GATE0: active

Grand total 81 of 160 (B01 grand_total). Core score 67 of 100; moat score 14 of 60; moats_confirmed 4 of 12; moat class STRONG; classification AVOID (B01). Depressor detail:
- Block B scored 2 of 20, below 8, caps at max GOOD (B01 deal_breakers).
- Cumulative CFO/PAT 0.4538 below 0.50 caps at max AVERAGE, driven by FY25 capex spike (FCF -899.87 lakh) and FY26 inventory build (WC days +27.19 vs FY24) (B01 deal_breakers).
- Three year LIMITED history one tier downgrade applied (B01 history_downgrade true).
- Blocks: A 18, B 2, C 16, D 20, E 11 (B01 blocks). Growth capex pattern, not demand/margin/leverage weakness; weigh accordingly downstream (B01 flags).

---

## 4. Credibility grade

B05 credibility_grade: B (B05 credibility_grade).

Basis: FY26 revenue/EBITDA/PAT growth guidance and order book targets all met or exceeded, Q1 FY27 ran well ahead of guidance, but the flagship 60-acre land/JV/margin-expansion promise slipped three-plus quarters running and an unreconciled market-share figure surfaced under direct questioning (B05 credibility_basis).

promise_delivery_score: 5 delivered / 2 partial / 2 missed (9 tracked) (B05 promise_delivery).

Guidance versus delivery table (B05 promise_delivery.rows):
| Promised in | Promise | Outcome | Explanation |
|---|---|---|---|
| Q2 FY26 | FY26 revenue/EBITDA/PAT growth 25-30% | delivered | met |
| Q2 FY26 | FY26 EBITDA target Rs 50 cr | delivered | exceeded, Rs 53.90 cr actual |
| Q2 FY26 | Order book Rs 300-330 cr by FY26 close | delivered | exceeded, Rs 406 cr actual |
| Q2 FY26 | Margin improves QoQ into Q3 FY26 | delivered | EBITDA margin rose to 18.08% Q3 FY26 |
| Q2 FY26 | No equity dilution/QIP for phase-1 capex | delivered | reaffirmed each call |
| Q2 FY26 (restating Q1) | 60-acre land acquired by end Dec-2025 | missed | external-blame: govt approval/policy timing |
| Q3 FY26 | Land signing Feb end / Mar first-second week 2026 | missed | external-blame: Gujarat local elections delaying land policy |
| Q2/Q3 FY26 | JV/tech transfer finalized once land received | partial | still gated on land at Q4 FY26; consistently explained, no movement in 3 quarters |
| Q3 FY26 | 25% EBITDA margin in 2-3 years via new plant | partial | reframed Q4 FY26 as requiring the undated 60-acre land; goalpost narrowed under analyst pressure |

repeated_evasions (B05):
- "How many machines did you sell/manufacture this quarter?" asked Q2/Q3/Q4 FY26, deflected every time.
- "When will the 60-acre govt land be signed / when does the JV finalize?" asked Q2/Q3/Q4 FY26, answer changed between quarters.

excuse_pattern: external-blame-heavy on the one recurring miss (land), delivered with unusually detailed proactive disclosure; one unresolved data-consistency deflection (market share); one goalpost-narrowing surfaced only under analyst pressure (B05 excuse_pattern).

Concalls available (not no-concall mode); quarters analysed Q2 FY26, Q3 FY26, Q4 FY26 (B05 quarters_analysed).

---

## 5. Scorecards and market sizing

### Gate 0 (B01)
- Grand total 81 of 160; core_score 67 of 100; moat_score 14 of 60.
- Blocks: A 18, B 2, C 16, D 20, E 11.
- moats_confirmed 4 of 12; moat_class STRONG.
- Classification AVOID.
- data_years 3, fy_range FY24 to FY26.
- Deal breakers: Block B <8 (=2) -> max GOOD; cumulative CFO/PAT <0.50 (=0.4538) -> max AVERAGE (FY25 capex spike FCF -899.87, FY26 inventory build WC days +27.19 vs FY24).
- history_downgrade true.

### Emerging Moat (B07)
- em_score 15.0; em_classification MODEST.
- active_categories: A4 Product platform/modular architecture (Moderate, claim, 12-24m); F2 Execution moat (Moderate, claim, 12-36m); G1 War chest/low leverage self-funded capex (Moderate, claim, ongoing); R1 Regulatory/policy tailwind (Moderate, claim, 12-24m).
- evidence_mix: documented 6, claim 15, inference 4 (completionist recount: 4 documented items across 3 categories, different basis).
- combined_assessment AVOID (STRONG backward moat already gated to AVOID by mechanical deal-breakers; MODEST claims-heavy scan not strong enough to override).

### Accounting quality (B02): 6 of 10
Top findings (rank, finding, note_ref, rating):
1. Trade receivables +57.5% YoY vs revenue +8.6%, turnover down 33%, >6mo ageing 15.4% from 12.2% (Note 9 p.149/174; Note 38vi p.185) Red Flag.
2. Trade payables +28.0% YoY, MSME dues +81.4% (Rs 2,553.13 lakh), payable days ~70 to ~98 (Note 18 pp.155-156; Note 38vi p.185) Red Flag.
3. Net margin "improvement" 12.00% vs 11.71% substantially mechanical raw-material inventory build depressing COGS (-15.2%) while Employee +29.7% and Other +38.1% (Misc +97.0% unexplained) outpace revenue +8.6% (Note 24/25/26/28 p.159-160; Note 7 p.148) Red Flag.
4. Fire 2-Feb-2025 destroyed Rs 439.09 lakh finished goods; Rs 362.39 lakh insurance claim pending; net exceptional loss Rs 76.70 lakh (Note 29 p.160-161; Note 39 p.182) Red Flag.
5. Note 12 certifies Nil loans to KMPs, yet Note 35 discloses Rs 10.10 lakh loan to CFO Vishal Mehta (Note 12 p.151; Note 35 p.169) Red Flag.
6. Investment portfolio Rs 516.16 lakh fully liquidated to zero; Other Income -73.9% (Note 8 p.148; Note 23 p.159; Note 37 pp.178-180) Watch.
7. Capex +51.5% YoY (Rs 1,597.77 lakh vs Rs 1,054.70 lakh); CWIP Rs 485.84 lakh, no capital commitment disclosure (Cash Flow p.132; Note 3 p.158) Watch.
8. Raw material inventory +50.9% YoY (Rs 10,096.04 lakh) vs revenue +8.6%; days ~181 to ~223 (Note 7 p.148; Note 38vi p.185) Watch.
9. Net cash cushion shrank: Net Debt -Rs 284.17 lakh (FY25) vs -Rs 884.17 lakh (FY24); Gearing -2.03% vs -8.02% (Note 36(f) p.177) Watch.
10. Returns compressing: ROE 17.65% (from 20.15%), ROCE 23.75% (from 26.70%), ROI 45.92% (from 51.34%), Net Capital Turnover 1.83x (from 2.02x) (Note 38(vi) p.185) Watch.
11. Three boilerplate/template instances: gratuity 5%/10% vs actual 12.00%; FX Net Exposure table transposed; Market Risk text claims FX receivables the table shows Nil (Note 34 pp.162-166; Note 36 pp.170-171) Watch.
12. WTD/CEO Nikesh J. Mehta holding fell 13.41% to 8.61% (-480,006 shares); absorbed by MD's family branch (Reyna +200,000, new entrant Vincy +280,000); total promoter group unchanged 73.18% (Note 13(f) pp.152-153) Watch.
13. Lease liability rose Rs 47.55 lakh to Rs 288.08 lakh; no Ind AS 116 discount rate; Rs 117.95 lakh (41%) due beyond 5 years (Note 16 p.154; Note 33 p.162) Watch.
14. Employee Loans & Advances +54.3% (Rs 72.19 lakh vs Rs 46.78 lakh); notional interest up 5.4x (Note 12 p.151; Note 23 p.159) Watch.
15. Quarterly stock-statement vs bank-return gap: Jun-24 Rs 53.49 lakh, Sep-24 Rs 221.86 lakh (largest), Mar-25 Rs 57.06 lakh, explained as provisional-figures timing (Note 47 p.184) Watch.

going_concern_language: NONE, explicit affirmative going concern (Note 1 p.135). restatements_found: none. B03 overall_quality 5.8; best_fit_strategy GARP (WATCHLIST); triple_pass discrepancy: PAT margin direction conflict (Note 38 12.00% vs P&L/KPI 9.72%, ~2.3pp unreconciled).

### Market (B09)
- tam_cr conservative 20,000, realistic 24,000; sam_cr 14,900 (62% of TAM).
- som_3yr_cr 660; som_5yr_cr 989.
- runway_class MASSIVE.
- som_implied_revenue_cagr yr3 25.6%, yr5 24.3%.
- current_sam_share_pct 2.24; revenue_headroom_x 44.7; tam_growth_pct 11.
- mgmt_claim_cr 35,000; mgmt_claim_ratio 2.13; mgmt_claim_read inflated (IMTMA Rs 35,000 cr vs IBEF/IMARC Rs 16,470 cr).
- Status partial (searches skipped: named vendor sources, primary IMTMA publication). Capacity cross-check gap ~Rs 190-290 cr at flat realisation for SOM(5yr); closes only if 13-acre capacity and NEXA/defence ASP mix both deliver on schedule.

### Peer triangulation (B06), 12 peer concalls, 8+ used substantively
- verified: none (B06 verified empty).
- partially_verified: industry growing 15-30%, IMTMA Rs 35,000cr (2026) to Rs 54,000cr (2030) [JYOTICNC]; import-component lead-time/cost pressure driving inventory builds [JYOTICNC]; multi-quarter govt land/policy approval delays [KLBRENG]; multi-year high-teens to ~25% EBITDA via backward integration and mix [JYOTICNC, KLBRENG, ADOR].
- contradicted: ~10-13% tender-bid conversion and single-digit-of-revenue defence contribution is consistent with peers -> CONTRADICTED by JYOTICNC, which executed ">INR800 crores of aerospace and defense" in FY26 (~75% India), plus Rs 180 cr India ordnance orders in a single quarter, 27-46% of quarterly intake (JYOTICNC Q4 FY26 May-2026 and Q2 FY26 calls). Caveat: likely different sub-segments (PSU ordnance vs private/global aerospace primes), not clean like-for-like.
- unverifiable: Macpower market share (4.5% vs 1-2%) reconciles with peers' disclosed share estimates (checked ADOR, JYOTICNC, KLBRENG; none disclose a comparable figure).
- net_narrative_effect: complicates. Industry demand real (JYOTICNC >20% CNC consumption CAGR; KLBRENG inquiry pipeline doubled to Rs 4,000 cr; ADOR muted 3-5%). No peer shows genuine pricing power. Peer risk read-across: JYOTICNC French export-control probe (Huron, Rs 67 cr revenue deferred); KLBRENG Middle East shipping disruption.

---

## 6. Valuation pillar detail (B11)

Stage 11 ran. Framework versions Master v3.3 / Section 1B v3.5.1 / FTTCP v1.2. pe_basis forward; exit_pe_base_approved 25.0.

Destination PE, both tracks:
- track2_additive (GOVERNING per operator approval): low 23.0x, mid 25.0x, high 25.0x. Raw additive 26.75x (21.4x x 1.25 UA) capped to 25.0x sector cap.
- track1_rrm (more conservative, deepens AVOID): low 15.0x, mid 16.5x, high 17.5x; r_used 14.75, rrm 0.85.
- divergence_pct 34. governing_track: Track 2 additive 25.0x per operator approval at FTTCP gate; RRM 16.5x flagged more conservative.

Pillar-by-pillar build (B11 pillar_detail; deliberation Sec 5):
- Pillar 1 ROCE: roce_used 23.75% (AR Note 38 FY25 audited), roce_base 19.375x (≈19.4x), normalization route NONE (Route A fails 20% idle-capital test; Route B barred on STAGNANT), recovery not-credited. Screener 29.1% (different basis) noted, not used; even at 29.1% additive stays cap-bound at 25x.
- Pillar 2 cash multiplier: 1.00x provisional (INDETERMINATE, structural_or_growth INDETERMINATE); 0.80x downside -> destination 21.9x, base FV Rs 942; devil's 0.65x band -> destination 18.2x, FV ~Rs 784 (B15). growth_offset 0.
- Pillar 3 growth: +2x (3a +2x order book 1.37x revenue, capex-embedded growth ~70%, delivery grade B; 3b +0x EM 15 below 25; 3c +0x order book below 2.5x tenor). growth_premium 2.
- Strategic premium: +0x (no rare licence, no documented pricing power, ROCE re-rating barred as ROCE not recovering).
- Undiscovered Alpha: APPLIES, x1.25 on raw destination PE before cap. All three qualifiers hold: listed since 2018, Gate 0 core 67 >60, FII+DII 0.96% <3% (ua_applied true).
- Sector cap: 25.0x (Cables / Industrial products), absolute (sector_cap_used 25.0).
- Tier A, 25% hurdle (FII+DII <3%).

Forward EPS: base Rs 43.0 (band Rs 40.5 to Rs 44.0), derived revenue +28-30% x ~10% margin (full-year EPS not published). FY26 (Year 0) EPS Rs 33.86.

hurdle_ratio: base 1.19, bull_used true, verdict STOP (bull 1.38; both under pass line ~1.953 per B15).
fair_values: track1 (RRM) bear 668 / base 710 / bull 726; track2 (additive) bear 1013 / base 1075 / bull 1100.
expected_cagr_prob_weighted -10.4%.
entry_range Rs 440 to 550; mos_price Rs 440; upside_downside_ratio 0.0.
decision AVOID (on valuation); FTTCP PROCEED WITH CAVEATS on quality; price ~2.7x entry zone; Hurdle STOP on base and bull.
Cross-checks: EV/EBITDA implied 16.3x vs current 27.5x (richly priced); P/B 10.4x on BVPS FY25 Rs 142.77 vs theoretical 1.20x (tertiary floor). som_cagr_crosscheck consistent.

---

## 7. Gaps ledger

| Item | Stage / block needing it | Where to obtain |
|---|---|---|
| Credit rating rationale and working capital commentary (verbatim) | B10, B11 Pillar 2, FLAG-CASH; closes INDETERMINATE cash | Rating agency rationale PDF (CRISIL/ICRA/CARE), BSE/NSE disclosure or agency site |
| Forward FY27 full-year EPS (committed) | B10, B11 exit multiple | Next quarterly results / management guidance in exchange filing |
| FY26 ROCE audited and reconciliation of AR Note 38 23.75% vs screener 29.1% | B10, B11 Pillar 1 | FY26 annual report (Note 38 equivalent) on BSE filing |
| BVPS FY26 audited | B11 P/B floor | FY26 annual report balance sheet |
| Peer financial multiples (JYOTICNC, ADOR, KLBRENG P/E, EV/EBITDA, P/B) | B06, B11 cross-check | Peer results filings; screener; empty peer CSVs to be refilled |
| Receivables ageing schedule FY26 and debtor days FY26 | B02, FLAG-CASH | FY26 AR Note 9 equivalent; quarterly investor presentation |
| Machine unit volumes per quarter | B04, B05 | Company disclosure (withheld to date); direct management question |
| Market share reconciliation (4.5% vs 1-2%) | B05, B09 | Management clarification; IMTMA primary publication |
| Fire insurance claim Rs 362.39 lakh settlement | B02 Finding #4, B03 | Next AR Note 39 equivalent; exchange filing |
| Note 12 vs Note 35 CFO-loan contradiction resolution | B02 Finding #5 | Direct management question; next AR notes |
| 60-acre land binding agreement status | B05, B07 shared catalyst | Exchange filing / next AR capital-commitments note |
| 21-Jul-2026 13-acre lease registration announcement | B00, B07 (operator context, non-anchored) | NSE/BSE announcement filing |
| Q1 FY27 investor presentation, Q3/9M and Q4/FY26 presentations | B03, B07 (operator context, non-anchored) | Company IR / exchange filing |
| Screening financials (MACPOWER + peers) | B00, stage 10 peer financials | Re-collect populated CSVs (current inputs empty header-only) |
| Cross-family FTTCP grade | deliberation Sec 4 | Configure Gemini or GPT provider key; rerun verifiers/fttcp_crossgrade.py |
| Viksit Gujarat Industrial Policy 2026 subsidy percentages | B07 | Gujarat govt policy document |
| R&D spend quantification (Rs / % of revenue) | B01 M6, B07 | AR Technology Absorption annexure (currently Nil disclosed vs "doubled team" claim) |
