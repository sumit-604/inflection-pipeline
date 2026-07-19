# FTTCP HANDOFF DOSSIER — Shyam Metalics & Energy Ltd (SHYAMMETL)

Run: shyammetl-2026-07-19. Framework versions: Master v3.3 / Section 1B v3.5.1 / FTTCP v1.2.
CMP Rs 1,022, market cap Rs 28,541 cr (manifest). Self-sufficient input package for manual FTTCP v1.2 deliberation without the source PDFs. Every figure carries its anchor; nothing here is re-analysed.

## BLOCK REFERENCE INDEX

- B00 inputs/inventory; B01 Gate 0; B02 AR notes forensics; B03 AR deep-read (triple pass); B04 business model; B05 concall (Q2 to Q4 FY26); B06 peers; B07 Emerging Moat; B08 promoter; B09 TAM/SAM/SOM; B10 valuation inputs (assembly); B11 valuation (Role 1); B14 thesis (Role 2); B15 devil's advocate (Role 3); B12a Verifier A numerical; B12b Verifier B red flags; B12c-framework Verifier C phase-1 (Gate 0 + EM); B12c-valuation Verifier C phase-3; B12d Verifier D peers; confidence delta.

## DELIBERATION-CONFIRMED INPUTS AND OPERATOR OVERRIDES (authoritative)

From fttcp-deliberation.md (authoritative for phase 3):
- Forward window: 3 months primary, 6 secondary, 12 for ROCE. Business type: standard operating business (integrated metals). First workup, Role 1 derived fields N/A.
- Override 1 (destination PE base): operator set exit PE at 20x flat, "approve the PE base at 20x." Elects the sector-cap ceiling over the computed ~17.7x additive / ~15-16x RRM. +2.3x uplift from the computed 17.7x additive base; sits exactly on the cap, does not breach it.
- Override 2 (earnings basis): one-year-forward (FY27E) EPS. Operator: "use forward earnings" / "yes, forward earnings." Fits a cyclical business mid ramp.
- Cash conversion: GROWTH-INDUCED (fairly sure). Falsifier: consol FG inventory growth above 2x revenue growth for two straight quarters into FY27, OR standalone CFO/PAT below 0.7x after capex tapers.
- ROCE backward verdict: TEMPORARILY DEPRESSED held over DECLINING (genuinely uncertain). ROCE forward: RECOVERING at 40-60% over 12 months (+1). Revenue forward: FIRING (+2). Margin forward: STAGNANT (0). Cash forward: FIRING at consol level, flagged (+2).
- Composite transition score: 5 of 8, BUY-candidate band. Disposition: constructive transitions, cautious position, small sizing, strict entry. "The live promoter money laundering attachment is the single most likely veto at final disposition."
- Return hurdle tier: Tier A, 25% hurdle. FII+DII above 3% would allow Tier B, but the promoter CONCERN verdict fails the Tier B quality gate.
- UA: NOT applied. FII+DII ~16.7% (operator context, non-anchored) above the 3% institutional-absence ceiling.
- SHARED CATALYST flag: YES. Capex commissioning drives both Pillar 1 ROCE and Pillar 3a; Role 3 stress test required.
- Sector cap row: 20x operator confirmed. Manifest value "Pharma / CDMO" (38x) OVERRIDDEN. MANIFEST FILE STILL NEEDS THE FIX before any future run (manifest.yaml line 8 still reads "Pharma / CDMO").
- Cross-family grade: DID NOT RUN (no Gemini/GPT key). FTTCP confidence treated one notch lower for the absent out-of-family adherence check.

## ROLE OUTPUTS

- Role 1 (B11 valuation, opus): decision AVOID; applied 20x flat forward; fair values bear 867 / base 913 / bull 1,006; entry 416-468; MoS 374; Hurdle Ratio STOP (base 1.24, bull 1.66 vs 1.953); expected prob-weighted CAGR -3.3%; upside/downside 0.7.
- Role 2 (B14 thesis, opus): verdict AVOID; entry 416-468; position size Small; thesis_broken triggers listed in Section 2/monitorables.
- Role 3 (B15 devil's advocate, opus): overall SURVIVES. Dimensions: growth_triggers weakened, moat_durability weakened, management_trust weakened, valuation_safety survives. The AVOID survives; DA sharpens it by attacking the constructive transition read.

---

## 1. TRANSITION DATA SERIES

Source key: DS = screener-Data_Sheet.csv (9-yr series, B01); AUD = audited Q4 FY26 results (results 518b..., B01/B10); IP = Investor Presentation. All ROCE/ROE and revenue/PAT rows anchor to the B01 Block A/B/C tables (screener-Data_Sheet, FY26 cross-checked to AUD p.10).

### 1a. Topline (revenue and growth)

| Year | Revenue (Rs cr) | YoY growth | Anchor |
|---|---|---|---|
| FY18 | 3,747.16 | base year | DS (B01 Block C) |
| FY19 | 4,606.40 | +22.9% | DS (B01 M11) |
| FY20 | 4,376.35 | -5.0% | DS (B01 M11) |
| FY21 | 6,297.07 | +43.9% | DS (B01 M11) |
| FY22 | NOT FOUND | NOT FOUND | not extracted to blocks |
| FY23 | 12,658.07 | NOT FOUND (FY22 absent) | DS (B01 M11) |
| FY24 | NOT FOUND | NOT FOUND | not extracted to blocks |
| FY25 | 15,137.50 | NOT FOUND (FY24 absent) | AUD (B10 fy25_comparatives) |
| FY26 | 18,552.21 | +22.59% | AUD p.10 (B10) |

Anchored aggregate: 8-yr revenue CAGR FY18 to FY26 = 22.12% (B01 C1). FY26 YoY +22.59% (B10).

### 1b. Margin (gross, EBITDA, net)

| Year | Gross margin | EBITDA margin | Net margin | Anchor |
|---|---|---|---|---|
| FY18 | NOT FOUND | 20.85% | 11.32% | EBITDA/net: DS (B01 M1; PAT 424.37/rev 3,747.16) |
| FY19 | NOT FOUND | NOT FOUND | 13.11% | DS (604.13/4,606.40) |
| FY20 | NOT FOUND | NOT FOUND | 7.78% | DS (340.24/4,376.35) |
| FY21 | NOT FOUND | NOT FOUND | 13.39% | DS (843.34/6,297.07) |
| FY22 | NOT FOUND | NOT FOUND | NOT FOUND | revenue absent |
| FY23 | NOT FOUND | NOT FOUND | 6.74% | DS (852.68/12,658.07) |
| FY24 | NOT FOUND | NOT FOUND | NOT FOUND | revenue absent |
| FY25 | NOT FOUND | 13.85% | 6.00% | AUD (EBITDA 2,096.16/PAT 908.10, rev 15,137.50) |
| FY26 | ~26.32% implied | 13.67% | 5.77% | AUD p.10; gross implied from raw-material 73.68% (B12a corrected); net 1,070.24/18,552.21 |

Anchored: EBITDA margin compressed 20.85% (FY18) to 13.67% (FY26), -7.18pp, per B01 M1. FY26 cost-of-materials 73.68% audited (B12a Verifier-A corrected, was ~72% deck).

### 1c. Cash conversion

| Year | OCF (Rs cr) | OCF/EBITDA | CFO/PAT | Debtor days | WC | Anchor |
|---|---|---|---|---|---|---|
| FY18 | 246.95 | NOT FOUND | 0.58 | 35.91 | NOT FOUND | DS (B01 Block B, M10) |
| FY19 | 456.56 | NOT FOUND | 0.76 | NOT FOUND | NOT FOUND | DS |
| FY20 | -91.00 | NOT FOUND | -0.27 | NOT FOUND | NOT FOUND | DS |
| FY21 | 1,056.17 | NOT FOUND | 1.25 | NOT FOUND | NOT FOUND | DS |
| FY22 | 1,561.20 | NOT FOUND | 0.91 | NOT FOUND | NOT FOUND | DS |
| FY23 | 1,518.33 | NOT FOUND | 1.78 | NOT FOUND | NOT FOUND | DS |
| FY24 | 1,794.38 | NOT FOUND | 1.73 | NOT FOUND | NOT FOUND | DS |
| FY25 | 1,964.15 (DS) / 1,713.43 (AUD) | 0.82 (AUD) | 2.16 (DS) / 1.89 (AUD) | 19.11 | WC days 20.86 | DS + AUD p.12 (B01 M12) |
| FY26 | 2,023.56 | 0.80 | 1.89 | 17.80 | WC days 10.62 | AUD p.12 (B01 Block B, M10, M12) |

Anchored aggregates: cumulative CFO/PAT 9-yr = 1.35 (B01 B1, cum CFO 10,530.30 / cum PAT 7,802.43). FY25/FY26 FCF negative: -434.89 / -613.68 (B01 B2, AUD p.12). WC as a share of sales: NOT FOUND per year; net WC days 20.86 (FY25) to 10.62 (FY26) per B01 M12 (partial-data). Note the DS vs AUD FY25 CFO conflict (1,964.15 vs 1,713.43, regrouped per filing note (x)); B01 used DS for the 9-yr series, AUD for FCF.

Rating agency working capital commentary, reproduced verbatim (CRISIL Rating Rationale dated November 05, 2025, p.2, Key Rating Drivers Strengths, per B10 rating_wc_quote):
> "Working capital management has been prudent. The group sells mainly on advance/letter of credit basis, leading to low receivables of 15-30 days. Inventory, at 70-90 days, mainly comprises raw materials. While the group does not have captive iron ore mines, its proximity to raw material sources and setting up of railway siding gives it access to iron ore at competitive rates because of lower logistics cost, thereby supporting profitability."

### 1d. ROCE and ROE (capital-employed basis: proxy Equity+Reserves+Borrowings for FY18-24; audited TA minus CL cross-check FY25/FY26, variance 1.9 to 3.1%)

| Year | EBIT (Rs cr) | Capital Employed (Rs cr) | ROCE | PAT (Rs cr) | Avg Net Worth (Rs cr) | ROE | Anchor |
|---|---|---|---|---|---|---|---|
| FY18 | 566.24 | 2,421.51 | 23.38% | 424.37 | 1,853.99 | 22.89% | DS (B01 Block A) |
| FY19 | 828.32 | 3,218.30 | 25.74% | 604.13 | 2,171.83 | 27.82% | DS |
| FY20 | 381.26 | 3,940.79 | 9.67% | 340.24 | 2,658.06 | 12.80% | DS |
| FY21 | 1,117.40 | 4,430.01 | 25.22% | 843.34 | 3,230.24 | 26.11% | DS |
| FY22 | 2,387.49 | 6,377.71 | 37.44% | 1,724.54 | 4,734.35 | 36.43% | DS |
| FY23 | 1,130.08 | 8,447.66 | 13.38% | 852.68 | 6,555.32 | 13.01% | DS |
| FY24 | 1,073.08 | 10,243.58 | 10.48% | 1,034.79 | 8,461.32 | 12.23% | DS |
| FY25 | 1,385.11 | 11,342.76 | 12.21% | 908.10 | 10,100.00 | 8.99% | DS (CE cross-check AUD) |
| FY26 | 1,654.60 | 12,527.88 | 13.21% | 1,070.24 | 11,038.07 | 9.70% | DS + AUD p.10-11 |

Anchored: median ROCE 13.38%, minimum 9.67% (FY20), trend 23.38% to 13.21% (-10.17pp). Median ROE 13.01%. CWIP Rs 106.47 cr at Mar-26 (0.85% of CE), vs 71.62 Mar-25 (B10) — Route A denominator-fix test FAILS.

---

## 2. CATALYST INVENTORY

From B05.triggers (concall) and B07.catalysts_12m (Emerging Moat 12-month window). Tier: documented / claim / inference.

B05 triggers:
1. Aluminium FRP + foil ramp (Sambalpur/Pakuria). Tier: claim/VOLUME-PRICE-MIX. Window: near-medium. Conviction M-H. Confirm: FY27 aluminium EBITDA/tonne lands in guided INR 35,000-40,000 range; oversold demand persists. Kill: commissioning delays beyond FY27; EBITDA/tonne well below range.
2. CRM Phase II Jamuria ramp (color-coated/CR coil). Tier: documented/VOLUME. Window: near-term. Conviction H. Confirm: CR coil volume growth sustains into FY27. Kill: volume growth stalls; guided color-coated doubling not achieved.
3. Safeguard duty / pricing discipline. Tier: documented/REGULATORY-POLICY. Window: near-term. Conviction M. Confirm: price hikes stick, Q1 FY27 margin holds above 14%. Kill: duty diluted or reversed; hikes fail to hold.
4. Stainless flat product, Odisha/Sambalpur expansion. Tier: claim/VOLUME-PRICE-MIX. Window: long-term (Mar-2029). Conviction L-M. Confirm: filing confirms capacity figure; on-schedule progress. Kill: further slippage; capacity figure unreconciled/overstated.
5. FY27 growth guidance (~30%). Tier: claim/SECTORAL. Window: near-term. Conviction L-M. Confirm: Q1 FY27 results show growth above 25%. Kill: reverts to 15-20% band or below.
6. DRI 0.5 MTPA. Tier: claim/VOLUME. Window: medium-term (FY27). Conviction M. Confirm: commissioning confirmed within FY27. Kill: delay past FY27.
7. PLI scheme benefit, stainless/specialty. Tier: claim/REGULATORY-POLICY. Window: long-term. Conviction L. Confirm: re-emerges with quantification. Kill: continued silence / scheme lapses. NOTE: already dropped from Q4 FY26 call.
8. Wagon manufacturing plant, Kharagpur. Tier: claim/INORGANIC. Window: long-term. Conviction L. Confirm: Phase 1 commissioning by target date. Kill: shelved / no further disclosure.
9. 90 MW captive power plant. Tier: claim/COST. Window: near-term. Conviction M. Confirm: explicit commissioning confirmation in FY27 disclosures. Kill: continued silence or further delay. NOTE: guided Q4 FY26, never confirmed commissioned.
10. Hot-rolling mill, Bengal (1.6 MTPA). Tier: claim/VOLUME. Window: long-term. Conviction M. Confirm: on-schedule capex disclosure each quarter. Kill: delay or cost overrun vs stated ~INR 5,000 cr.

B07 catalysts_12m:
- Aluminium FRP plant (60,000 TPA) commercial launch. Tier: documented. Window: end-Sep-2026. Anchor: IP p.23 (17-Jun-2026 Investor Day).
- Wagon plant Phase-I (2,400 wagons/yr) commissioning, Kharagpur. Tier: documented. Window: Sep-2026. Anchor: IP p.26.
- DRI 0.5 MTPA commissioning. Tier: claim. Window: during FY27 (by Mar-2027). Anchor: operator context, cross-checked DRI table IP p.34-35.
- CPCB Rengali/Sambalpur compliance resolution. Tier: documented (regulatory action). Window: ~3 months from 13-Apr-2026 directive. Anchor: operator context 6-month operational log.
- Aluminium segment EBITDA/tonne mix-driven margin ramp. Tier: claim. Window: FY27. Anchor: operator context; per-tonne trend IP p.40.

Optionality register (B07): battery-grade aluminium foil qualification (2-3 customers under NDA), window 12-24m; GoI stainless-in-highway-bridges demand mandate, 12-24m; HSM/CSP thin-slab technology partner (named only as "world's #1 conglomerate supplying Nucor"), 6-18m; proprietary data/AI quality asset (SAP S/4HANA + IoT), 24-36m; ESG rating sustained improving trajectory (currently 50-63.7 across four agencies), 12-24m.

---

## 3. FLAGS WITH COMPLETE UNDERLYING FINDINGS

### FLAG-PROMOTER — CONCERN (B08)

Verdict: CONCERN. Scorecard: clean 5, caution 3, red 2.

Deal-breakers:
- PMLA with attached assets: TRIGGERED. Rs 159.51 cr provisional attachment, subsidiary SSPL, 15-Apr-2026, live/unresolved.
- Multiple mid-term independent exits within 3 years: TRIGGERED (borderline). Yudhvir Singh Jain (demise, Oct-2024) and Malay Kumar De (personal reasons, May-2025); both benign-cause on available evidence.

Adverse findings (full):
- ED provisional attachment Rs 159.51 cr on SSPL under PMLA, coal-mining investigation. Tier MEDIA REPORTED (corroborated by ED press release). Sources: scanx.trade / TipRanks / ED press release PDF / Daily Pioneer / Whalesbook. Date 2026-04-15.
- CPCB closure of 21 furnaces/production lines at Rengali for sustained pollution non-compliance (PM 268 mg/Nm3 vs 50 limit). Tier MEDIA REPORTED (multiple outlets). Sources: Business Standard / India CSR / Sambad English / Business Upturn. Date 2026-04-07 to 2026-04-13.
- Chairman and MD roles combined in Brij Bhushan Agarwal, departing from prior discretionary separate-post practice. Tier VERIFIED (AR FY2024-25 p.95, p.179). Date 2025-05-10.
- Long-running trademark/passing-off injunction against SSPL in favour of unrelated competitor Shyam Steel Industries Ltd. Tier VERIFIED (Calcutta HC / IndianKanoon). Date 2019-12-24 (ongoing at SC level).
- External CFO (Shree Kumar Dujari) replaced by internal long-tenured executive (Deepak Agarwal). Tier MEDIA REPORTED. Date 2022-11-08 / 2023-05-05.
- Two minor exchange non-compliance fines (Reg 29(1) timelines), Rs 11,800 each. Tier VERIFIED (AR p.176). Date 2023-08-23.

Transition evidence (full list):
- Chandra Shekhar Verma (ex-CMD SAIL, ex-CMD NMDC) appointed Independent Director, 5-yr term, 4-Jul-2024. AR p.95, VERIFIED.
- Rs 1,385.35 cr QIP to 38 QIBs, FY23-24; proceeds deleveraged parent and SSPL; explains promoter % drop as pure dilution, zero promoter share sale. AR Note 18, VERIFIED.
- DII holding risen 4.35% (Sep-23) to 13.75% (Jun-26) per operator-sourced screener trend. NON-ANCHORED, directionally consistent.
- Internal auditor upgraded KPMG to Ernst & Young LLP for FY25-26. AR Corporate Information, VERIFIED.
- Orderly founder-to-second-generation succession: Mahabir Prasad Agarwal to honorary non-executive Chairman Emeritus, 9/10-May-2025. AR p.95, VERIFIED.
- CPCB granted conditional relief with defined 3-month remediation window. MEDIA REPORTED.

Pledge: 0% throughout period checked; no pledge found in any quarter.

### FLAG-CASH — GROWTH-INDUCED (structural tail flagged) (B02, B03, B11)

Determination: GROWTH-INDUCED, not structural, not indeterminate (deliberation, fairly sure). Pillar 2 multiplier 1.0x provisional.

Cited items behind it:
- Consol working capital deterioration: inventory +37.7% (finished goods +53.7%) vs revenue +14.7% (B02, Note 11 consol p.291-292); NRV write-down expense jumped 9.4x (Rs 0.83 cr to Rs 7.77 cr); slow-moving inventory provision doubled (B02 rank 15).
- Standalone CFO/PAT collapsed to 0.57x (from 1.44x FY24), standalone FCF -223.49 cr in a 39.3% PAT-growth year; ~924 cr negative trade-payables swing plus inventory build (B03, CF Statement p.198, Note 26 p.305).
- Consol CFO/PAT ~1.9x (2,023.56/1,070.24) still strong; standalone drain is intra-group (B11, B10).
- Standalone trade payables fell 31.8% (days 92 to 67) while consol payables rose 23.2%; alongside Rs 597 cr loan recovery and Rs 800 cr OCD investment into SSPL (B02 rank 12, Note 26/42).
- Standalone related-party trade receivables Rs 726.53 cr = 77.77% of Rs 934.39 cr, unsecured interest-free, chiefly SSPL (B02 rank 6, Verifier-A corrected, AR Note 42).
- Capex commissioning timeline: 76% of consolidated capex (Rs 10,617 cr of Rs 13,902 cr) unexecuted, commissioning dates to Mar/Sep-2029 (B07). FY26 capex 2,637.24, FCF -613.68 (B10, AUD p.12).
- Rating agency verbatim quote: see Section 1c (CRISIL, Nov 05 2025, p.2).

Structural tail (B15): standalone drain read as structural, parent funding a subsidiary whose profit contribution halved (722.34 to 417.15 cr; 70.20% to 45.88%); consol 1.9x can launder this.

Falsifying quarterly metric with threshold: consol finished-goods inventory growth above 2x revenue growth for two consecutive quarters into FY27, OR standalone CFO/PAT below 0.7x after capex tapers.

### FLAG-GATE0 — AVOID (B01)

Classification AVOID; Core Score 34/100; grand total 41/160; moat score 7/60; moats_confirmed 2 (MODERATE).
Blocks: A 4/20, B 5/20, C 11/20, D 14/20, E 0/20.
Full depressor detail:
- Block A 4/20: median ROCE 13.38%, min 9.67% (FY20), trend 23.38% to 13.21% (-10.17pp). Deal-breaker #1 (A<8) caps max GOOD.
- Block B 5/20: cumulative CFO/PAT 1.35, but FCF negative both audited years (-434.89 FY25, -613.68 FY26), capex (+22.8%) outrunning CFO (+18.1%). Deal-breaker #2 (B<8) caps max GOOD.
- Block E 0/20: entirely a data gap (shareholding and contingent liabilities absent). Materially drives sub-40 Core; re-test once shareholding available.
- Genuine non-data-gap depressors: EBITDA margin 20.85% to 13.67%, current ratio 0.997x, FCF negative/worsening against active heavy capex (Rs 6,660 cr + Rs 2,700 cr newly approved).
Deal-breakers checked: #1 (A<8) YES; #2 (B<8) YES; #5 (pledge>15%) cannot evaluate (shareholding absent); all others No.

### FLAG-SHARED-CATALYST — ACTIVE (B10, B11)

Capex commissioning schedule drives BOTH Pillar 1 ROCE recovery and Pillar 3a growth premium; single point of failure, no diversifying second catalyst. Aluminium FRP 60 kTPA (Sep-2026), Wagon Phase-I (Sep-2026), DRI 0.5 MTPA (by Mar-2027). Role 3 stress test required and performed (B15): the first commissioned value-add line already prints realization down QoQ.

---

## 4. CREDIBILITY GRADE

B05 credibility_grade: B. Concall mode (3 transcripts, Q2 to Q4 FY26).
Basis: core capex milestones delivered on the exact quarter promised with disciplined capex-tracking every call; but PLI-stainless and flange-beam triggers went silent, the 90 MW captive power plant commissioning was never explicitly confirmed, and management deflected on the Q4 FY26 ED coal notice and the unreconciled FY27 growth-guidance escalation.
Promise-delivery score: delivered 3, partial 6, missed 2. Excuse pattern: balanced. Verifier B (B12b) concurs with grade B (promise-delivery spot-checks 5/5 confirmed).

Repeated evasions:
- "Why not take on more leverage to improve ROE given AA+ rating headroom?" asked Q3 and Q4 FY26; deflected every time.
- "Status/timeline of the parallel flange beam project?" asked Q2 and Q3 FY26; deflected every time, then dropped entirely by Q4.

Guidance-versus-delivery table (B05 promise_delivery rows):

| Promised in | Promise | Outcome | Delivery evidence |
|---|---|---|---|
| Q2 FY26 | Ramsarup 0.45 MTPA blast furnace, revenue from Dec 2025 | Delivered | Q3 FY26 confirms commissioning and commercial production |
| Q2/Q3 FY26 | 0.15 MTPA CRM Phase II (color-coated), Q4 FY26 | Delivered | Q4 FY26 confirms CRM Jamuria Phase 2 commissioned; CR coil +200% YoY |
| Q3 FY26 | Q4 FY26 margin improvement ~10-20% vs Q3 | Delivered | Q4 FY26 EBITDA margin 14.4% vs Q3 ~12.2% |
| Q2/Q3 FY26 | 90 MW captive power plant, Q4 FY26 | Partial/Unconfirmed | No explicit completion confirmation in Q4 FY26 |
| Q2 FY26 | Flat/stainless steel line "maybe year 26/27" | Partial/Slipped | Q4 FY26 sets formal target March 2029, unreconciled |
| Q2 FY26 | DI pipe capex redirected to a named replacement | Partial | No concrete replacement named across Q3/Q4 |
| Q2 FY26 | Mittal Corp FY26 revenue INR 1,500-2,000 cr | Unconfirmed | Q4 FY26 does not restate/confirm actual |
| Q2/Q3 FY26 | Revenue/EBITDA growth 15-20% CAGR | Partial/Escalated | Q4 FY26 raises FY27 to ~30% without reconciling |
| Q3 FY26 | Remaining capex ~INR 7,500-8,000 cr / 3 yrs | Partial/Inconsistent | Q4 FY26 restates ~INR 10,000 cr, no cumulative reconciliation |
| Q2/Q3 FY26 | PLI stainless/specialty INR 400-500 cr / 5 yrs | Dropped | Q3 pushes timeline; Q4 no mention |
| Q2/Q3 FY26 | Parallel flange beam line expansion | Dropped | Q3 hedges; Q4 zero mention |

---

## 5. SCORECARDS AND MARKET SIZING

### Gate 0 (B01)
Grand total 41/160; Core Score 34/100; moat score 7/60. Blocks: A 4, B 5, C 11, D 14, E 0. Moats_confirmed 2/12 (M4 Customer Stickiness 3, M10 Switching Costs 3). Classification AVOID. Deal-breakers triggered: A<8, B<8; pledge>15% cannot evaluate. Moat classification MODERATE. Data years 9 (FY18-FY26); history_downgrade false.

### Emerging Moat (B07)
em_score 30; em_classification STRENGTHENING; combined_assessment TURNAROUND. Evidence mix: documented 19, claim 10, inference 6. capex_embedded_growth 150%. Consolidated capex Rs 13,902 cr budgeted / Rs 3,285 cr incurred / Rs 10,617 cr pending (IP p.29-33).
Active categories: A3 Process innovation (Strong, documented); B1 Backward integration / RM security (Strong, documented); G1 War chest (Strong, documented); G2 WC improvement trajectory (Strong, documented); H2 Strategic partnerships (Strong, documented); A1 Rare manufacturing capability (Moderate, documented+claim); E2 China+1 beneficiary (Moderate, documented+claim); F2 Execution moat (Moderate, documented+claim); H1 Industry consolidation beneficiary (Moderate, documented); R1 Regulatory/policy tailwinds (Moderate, documented+claim).

### Accounting quality (B02): 5/10. Top notes findings (15):
1. Consol PAT (owners) fell 12.2% (1,034.79 to 908.10 cr) despite revenue +14.7% and standalone PAT +39.3%; consol EPS -17.3%. Note: P&L consol; Note 47 p.326-327. Red Flag.
2. SSPL profit contribution to consol P&L fell 42.2% (722.34 to 417.15 cr; 70.20% to 45.88%) even as net assets grew 27.4% and it received the bulk of FY25 capital injections. Note 47 consol p.326-327. Red Flag.
3. Unrecognised DTA on group tax losses rose 686.32 to 955.21 cr gross (tax effect 240.43 cr); FY24 PAT boosted by one-off (338.57) cr tax-recognition tailwind. Note 24(c) p.304; Note 37(c) p.309-310. Red Flag.
4. 10 of 13 group entities carry CARO clause 3(xvii) cash-losses qualification (77%); SSPL carries same title-deed/statutory-dues qualifications as parent. Consol Auditor's Report CARO table p.260 [Verifier-A corrected from 11 to 10]. Red Flag.
5. Rs 352.31 cr (consol) / 253.05 cr (standalone) equity in Dorite Tracon, Narantak Dealcomm, Subham Capital, entities that hold ~35.18% of SMEL; gains through OCI. Note 7(a) p.220/289; Note 18(e)/(f) p.296-297. Red Flag.
6. Standalone trade receivables 77.77% (726.53 cr of 934.39 cr) owed by related parties, chiefly SSPL, unsecured interest-free, vs 7.5% revenue-flow concentration. Note 12 p.221; Note 42 p.245 [Verifier-A corrected]. Red Flag.
7. Auditor server-backup finding: affirmative non-compliance ("backup... NOT kept in servers physically located in India") for some subsidiaries. Consol Auditor's Report p.258. Red Flag.
8. Statutory auditor unable to obtain some internal audit reports for Q4 FY25. Standalone CARO Annexure B (xiv)(b). Red Flag.
9. Audit trail not enabled at database level for Holding + 3 subsidiaries; one confirmed non-preservation instance. Standalone Note 50(j) p.252-253; Consol Note 51(j) p.329-330. Red Flag.
10. ~93% of standalone Other Income increase and ~23% of total PBT increase driven by treasury/FVTPL gains + interest income; Note 45(e) attributes ROI jump to "treasury related activities". Watch. [B03: correct anchor is Note 29 p.307, content verified at 23.8%.]
11. Shree Venkateshwara Electrocast (90% aluminium foil) lost 1.85 cr (FY25) / 9.32 cr (FY24); CARO clause 3(xix), only going-concern-adjacent language. Note 47 p.326-327; CARO table p.260. Red Flag.
12. Standalone trade payables fell 31.8% (days 92 to 67) while consol payables rose 23.2%; alongside 597 cr loan recovery and 800 cr OCD into SSPL. Note 26; Note 42 p.242-245. Watch.
13. Group gearing rose 14.80% to 21.08% (net debt 1,675 to 2,819 cr), 99.7% floating-rate, unhedged FX up 33% to 1,433.25 cr, no hedging policy. Note 44 consol p.323; Note 43(A) p.319-321. Watch.
14. "Single business segment" disclosure contradicted by Note 47 entity-level P&L/net-asset breakdown. Standalone Note 47 p.251; Consol Note 48 p.328. Red Flag.
15. Consol finished-goods inventory +53.7% vs revenue +14.7%; NRV write-down 9.4x; slow-moving provision doubled. Note 11 consol p.291-292. Watch.
Going concern: ISOLATED to one subsidiary (Shree Venkateshwara Electrocast, CARO 3(xix)); no going-concern qualification at Holding or Group level.

### Market (B09)
tam_cr conservative 424,060 / realistic 484,690; sam_cr 381,654 (90% of TAM); som_3yr_cr 28,090; som_5yr_cr 33,815; runway_class STRONG; som_implied_revenue_cagr yr3 14.8% / yr5 12.7%; current_sam_share 4.86%; revenue_headroom 20.6x; tam_growth 7%. mgmt_claim_cr 42,500 (FY31E, ~18% CAGR); mgmt_claim_ratio 0.10; mgmt_claim_read conservative. Capacity check: ~Rs 8,500 cr gap between bottom-up 5yr SOM (33,815) and mgmt FY31E (42,500), concentrated in stainless volume ramp (94,102t FY26 to 699,733t FY31E target vs 0.6 MTPA nameplate SS finishing).

### Peer triangulation (B06)
Verified: [] (none fully verified). Contradicted: [] (none contradicted).
Partially verified: (a) Indian steel demand ~11-12 MT/yr incremental (7-8% GDP-linked), India 300 MT target [GPIL, SARDAEN, GALLANTT]; (b) safeguard duty produced sustained sector-wide price/margin improvement from Q4 FY26 [GPIL, SARDAEN] (caveat: duty lapsed Oct-Nov 2025 before reimposition); (c) Shyam HR-mill capex efficiency ~INR 5,000 cr/1.6 MTPA internally consistent [GPIL, GALLANTT].
Unverifiable (no coverage in provided peer set): (a) ~20% nickel price rise since Dec 2025 and stainless pass-through; (b) cost competitiveness vs Jindal Stainless once Sambalpur flat stainless commissions (Mar 2029); (c) aluminium foil/FRP "oversold" demand industry-wide vs Shyam-specific; (d) ED coal notice status/substance. Peer coverage hole: no stainless/aluminium/nickel comparator (correct comparators Jindal Stainless, Hindalco, NMDC Steel not provided). net_narrative_effect: complicates.

---

## 6. VALUATION PILLAR DETAIL (B11, stage 11 ran)

pe_basis: forward (one-year-forward FY27E EPS). exit_pe_base_approved: 20x flat (operator sector-cap ceiling; manifest Pharma/CDMO 38x overridden).
FY27E EPS derivation: FY26 diluted EPS 38.70 x growth. Base 18% (historical PAT CAGR, per Section 2A lower-of rule) = ~45.67; bear 12% = ~43.34; bull 30% = ~50.31.

Destination PE, track 1 (RRM): low 14.5x, mid 15.7x, high 17.0x; r_used 14.75%, rrm 0.85. CoE/r build: mid-cap base 13% + governance 1.25% + durability 0.5%.
Destination PE, track 2 (additive pillar build): low 17.0x, mid 18.5x, high 20.0x. Divergence 15.1%. Governing track (self-derived): RRM (more conservative, fits governance-flagged commodity cyclical). BOTH superseded by operator 20x flat, which is applied to fair values.

Pillar build (B11 pillar_detail):
- Pillar 1 ROCE: roce_used 15.93, roce_base 15.5; route pillar1-midpoint; normalization Route B (pre-cycle), because Route A FAILS (CWIP 106.47 cr ~0.85% of CE, under 20%). Pre-cycle anchor ~20% capped below the single evidenced FY18 print 23.4%. RECOVERING 40-60%, 60/40 current/anchor blend. Route B self-withdrawal: if FY27 ROCE print does not turn up by Mar-2027 +1 quarter, anchor withdrawn, Pillar 1 reverts to statutory ROCE.
- Pillar 2 cash multiplier: 1.0x, growth-induced, growth_offset 0. (Verifier C flagged Pillar 3b under-credit; see below.)
- Pillar 3 growth+moat premium: +3x (3a +2x capex-embedded growth 150%, grade B; 3b +1x EM 30 STRENGTHENING; 3c +0x). Within +6x cap. Verifier C (B12c-valuation) MAJOR: 3b should be +3x EM-gated, correcting additive to 20.5x cap 20x; no decision impact (superseded by 20x flat).
- strategic_premium: 0x. ua_applied: false (FII+DII ~16.7% > 3% ceiling). sector_cap_used: 20.
- shared_catalyst_flag: true.

hurdle_ratio: base 1.24, bull_used true, verdict STOP (both < 1.953 pass mark; bull 1.66).
fair_values (applied 20x): bear 867, base 913, bull 1,006 (both track1 and track2 keys hold the applied-20x values; track-specific were RRM 680/717/790, additive 802/845/931 per B12c-valuation). expected_cagr_prob_weighted -3.3%. entry_range 416-468. mos_price 374. upside_downside_ratio 0.7.
decision: AVOID (CMP above bull fair value; Hurdle STOP; Gate 0 AVOID; Promoter CONCERN each independently force AVOID).
cash_multiplier_used 1.0; structural_or_growth growth-induced; ua_applied false; sector_cap_used 20.
one_line_thesis (B11): "Avoid SHYAMMETL at Rs 1,022: even at operator-approved 20x forward (above the 18.5x additive / 15.7x RRM pillar build), FY27E EPS ~45.67 gives fair value ~913 (bull ~1,006), all below CMP; expected CAGR -3.3%, Hurdle Ratio STOP; SHARED CATALYST commissioning drives both ROCE and growth; cash growth-induced (1.0x)."
SOM cross-check: base ~18% EPS maps to ~16-18% revenue vs SOM-implied 14.8% (3yr); justified excess by 22.12% historical revenue CAGR and near-term commissioning; base does not rely on aggressive stainless ramp.

Company identity / financials (B10): shares outstanding diluted 27.92 cr; EV 28,520.61 cr; net cash -20.39 cr; interest coverage 8.61x; current ratio 0.997x; CFO/PAT latest 1.89, cumulative 9-yr 1.35. CRISIL AA+/Stable (upgraded from AA/Positive), A1+, Nov 05 2025 (ratings.pdf p.1).

---

## 7. GAPS LEDGER

| Item | Stage/block needing it | Where to obtain |
|---|---|---|
| Shareholding pattern (promoter %, pledge, FII/DII) | B01 Block E (0/20), B08, UA qualifier | BSE/NSE shareholding filing (SHP) |
| Contingent liabilities note | B01 Block E, B10 | Annual Report notes (present in AR, not extracted to results) |
| Reg 30 announcements (capex commissioning, ED notice, CPCB) | B05, B07, B08 | BSE/NSE exchange filings |
| ED-PMLA attachment filing PDF (Rs 159.51 cr) | B08 (MEDIA-REPORTED only) | ED press release / exchange disclosure |
| CPCB Rengali order and remediation status | B08, B07 catalyst | CPCB order / exchange disclosure |
| SSPL Note 47 entity profit 722.34->417.15cr re-read | B02/B03, B12a (rendering-limited) | AR PDF p.298-302 at clean extraction |
| FY27E EPS (management-quantified) | B10, B11 (derived) | Management guidance / next quarterly |
| CWIP + idle capital % of CE (confirm Route A/B) | B10, B11 Pillar 1 | Balance sheet CWIP schedule (CWIP 106.47 cr Mar-26 anchored, Route A FAILS) |
| Peer comparables for stainless/aluminium/nickel | B06, B09, B10 | Jindal Stainless, Hindalco, NMDC Steel filings/screeners |
| Peer FY26 revenue for Method 3 TAM aggregation | B09 | Rashmi Metaliks, Sarda Energy, Jai Balaji, Godawari Power, Jindal Stainless |
| 3-year PAT CAGR (needs FY23 PAT) | B10, B11 base growth | screener 9-yr series (exists per B01, not extracted to B10) |
| FY22 and FY24 revenue, per-year gross margin | transition data series (Section 1) | screener full P&L / annual reports |
| Customer concentration (top 5/10 %) | B04, B07 (B2) | Annual Report / IR (NOT FOUND in AR or IP) |
| 90 MW captive power plant commissioning confirmation | B05 (unconfirmed) | FY27 disclosures / exchange filing |
| Mittal Corp FY26 actual revenue vs INR 1,500-2,000 cr guide | B05 (unconfirmed) | Next AR / segment disclosure |
| Contingent-liability reconciliation (subsidy +/-15.33cr; elec duty +/-5.00cr) | B02, B10 | AR notes cross-read (KAM vs Note 16; CARO vs Note 41(c)) |
| MCA status of Subham Capital, Kalpataru Housefin, Dorite Tracon, Top Light Mercantiles | B08 (skipped) | MCA portal |
| Proxy advisory (IiAS/SES/InGovern) coverage | B08 (not located) | proxy advisory reports |
| FTTCP cross-family adherence grade | deliberation (SKIPPED, no key) | configure Gemini/GPT key, re-run verifiers/fttcp_crossgrade.py |
| manifest.sector_cap_row correction | manifest.yaml (line 8 still "Pharma / CDMO") | edit manifest to the steel 20x row before any future run |

Gaps also feed the deliberation worklist: B10.unresolved (FY27E EPS, CWIP %, peer comparables, 3-yr PAT CAGR, contingent-liability reconciliation) and every block's input_gaps above.
