# FTTCP handoff dossier — MENON BEARINGS (MENONBE)

Archive record for manual FTTCP v1.2 deliberation in a separate Opus session without source PDFs. Every figure carries its source anchor. Block references are intentional. First workup for this ticker; no WHAT CHANGED section.

CMP Rs 190 (deliberation; screener 190.17). Market cap Rs 1,073 Cr (5.604 Cr shares × 190). Run date 2026-07-16. Deliberation 2026-07-17. Operator Keerti Kaushik.

## 0. Machine index, deliberation inputs, overrides, Role outputs

### Block reference index

- B00 inputs: full run, concalls available, long listed. Provenance defects: sector cap row manifest wrong ("Agri processing", corrected phase 3); AR filename mislabel (Annual_Report_2023.pdf is FY2021-22).
- B01 Gate 0: core 54, moat 16, grand 70/160, MODERATE moat (3), classification AVOID (limited-history one-tier downgrade + Block B<8). FLAG-GATE0, FLAG-CASH, FLAG-DATA-BASIS (screener is CONSOLIDATED).
- B02 notes/accounting: accounting_quality 5/10, 6 red flags, going concern NONE, no restatements. FLAG-CASH.
- B03 AR deep read: overall quality 5/10, best fit Capex-Led Growth PASS / GARP WATCHLIST. FLAG-CASH, FLAG-PROMOTER-PRELIM.
- B04 business model: manufacturing, WC intensity high, cyclical, primary method EV/EBITDA, secondary normalised P/E. FLAG-DISCLOSURE (no audited segment P&L), FLAG-DATA (Alkop per-unit realisation conflict).
- B05 concall: credibility C, promise delivery 1/5/6, 4 repeated evasions. Flags: dynamometer 4x slippage, Alkop target inconsistent same period, silence on Alkop negative reserves, dropped growth initiatives.
- B06 peers: 3 peers, 2 verified, 1 contradicted (sweat-the-assets), 3 unverifiable; net narrative effect "complicates".
- B07 emerging moat: em_score 11, NONE band, combined AVOID. FLAG-EMOAT-WEAK, FLAG-GUIDANCE-SLIPPAGE, FLAG-DATA-INCONSISTENCY.
- B08 promoter: verdict CAUTION (6 clean / 3 caution / 1 red), status partial (BSE/Trendlyne HTTP 403). Pledge NOT FOUND. FLAG-PROMOTER not triggered.
- B09 TAM: TAM Rs 10,100 Cr realistic, SAM Rs 1,858 Cr, SOM 3yr Rs 240.8 Cr, runway STRONG, SOM-implied domestic CAGR 7.5%, mgmt claim ratio 1.06. FLAG-SCOPE (domestic-only), FLAG-VALUATION-GAP.
- B10 valuation inputs: full authoritative input table; CMP 190, EV 1,107 Cr, TTM PE 24.3x. FLAG-CASH, SHARED CATALYST, CREDIBILITY C.
- B11 valuation (Role 1): destination 25x additive / 22.4x RRM, Hurdle CONDITIONAL, entry 132-148, MoS 118, decision WATCHLIST.
- B12a verifier A (numerical): 47 checked, 91.5%, 0 CRIT / 0 MAJ / 4 MIN.
- B12b verifier B (red flag, binding): 16 independent flags, 12 caught, 75%, 0 CRIT / 1 MAJ / 4 MIN.
- B12c verifier C (framework): phase-1 Gate0+Emoat 99% (48+26 rules, 0 fails of consequence); phase-3 valuation+Role2 94% (52 rules, 1 MAJ / 5 MIN). Combined 126 rules, 96%.
- B12d verifier D (peer): 11 audited, 100%, 0 CRIT / 0 MAJ / 5 MIN.
- confidence: numerical 91.5, redflag 75 (binding), framework 94, peer 100, overall 75, band 75-89 normal, rework false.
- B14 thesis (Role 2): WATCHLIST, entry 132-148, Small, Tier A, 10 monitorables, 7 thesis-broken conditions.
- B15 devil (Role 3): WEAKENED BUT ALIVE (growth/moat/mgmt weakened, valuation destroyed).

### Deliberation-confirmed inputs (fttcp-deliberation.md, authoritative for phase 3)

- Forward window: 3m primary, 6m secondary, 12m for ROCE.
- Sector cap row: Manufacturing / Industrial products, 25x (corrected from manifest "Agri processing" 20x).
- Revenue: backward STAGNANT, forward STARTING (+1).
- Margin: backward SUSTAINED, forward STAGNANT (0).
- Cash conversion: backward DETERIORATING, forward STAGNANT (0), determination GROWTH-INDUCED; INDETERMINATE not invoked (CRISIL rationale available).
- ROCE: backward SUSTAINED at premium (~29.8% FY26 AR Note 33), forward STAGNANT (0); not depressed, Amendment 4.5 N/A; recovery not credited; Strategic Premium ROCE route barred.
- Composite: +1 out of 8, DEEP WATCH leaning AVOID.
- UA multiplier: applies, 1.25x (listed >12m; Gate0 grand 70>60; FII+DII ~0.24%<3%).
- Hurdle tier: Tier A, 25%.
- Credibility grade C: bull EPS CAGR capped at base + 5.

### Operator overrides (both valuation-side, not transition-verdict)

- Override 1, Pillar 3 growth premium: draft +0x (EM 11 NONE band, 3a/3b/3c all zero); operator set +1x. Reasoning verbatim: "India is a growing economy, and this is an old company, so obviously growth is there. Give it at least an additional one point."
- Override 2, destination PE: draft ~19x-24x; operator set 25x = sector cap. Reasoning verbatim: "take the destination valuation multiple to 25." Reconciles: 22.4×0.85=19.0, +1.0=20.0, ×1.25=25.0=cap.

### Role 1 output (B11 valuation)

destination_pe: Track 1 RRM {low 20.5, mid 22.4, high 24.0, r 14, rrm 0.94}; Track 2 additive {low 23.0, mid 25.0, high 25.0}; divergence 11.6% (under 15%, Track 2 governs, RRM conservative cross-check STOPs). hurdle_ratio {base 1.73, bull 1.96 used, verdict CONDITIONAL}. fair_values Track 1 {bear 137, base 260, bull 523}; Track 2 {bear 153, base 290, bull 584}. expected_cagr_prob_weighted 13.4%. entry_range {132, 148}. mos_price 118. upside_downside 2.7x. decision "WATCHLIST (BUY-ON-DIPS Rs 132-148; AVOID-on-valuation at CMP 190; growth-dependent with de-rating headwind)". one_line_thesis: "Premium-ROCE manufacturer priced for its own returns; the 25 percent case rests entirely on the export ramp firing while cash converts, so wait for Rs 132 to 148."

### Role 2 output (B14 thesis)

verdict WATCHLIST; entry 132-148; position_size Small (override empty); tier A (Tier B barred by FII+DII<3% default plus live FLAG-CASH + promoter CAUTION + credibility C); hurdle_band CONDITIONAL; operator overrides honored (Pillar 3 +1x, destination 25x); verdict_consistency: consistent with Role 1. thesis_broken_if: standalone DSO exceeds 114 days OR standalone receivables again grow faster than revenue in the next print (cash flips STRUCTURAL, Pillar 2 to 0.65x).

### Role 3 output (B15 devil)

overall WEAKENED BUT ALIVE. dimensions: growth_triggers weakened, moat_durability weakened, management_trust weakened, valuation_safety destroyed. Top counters: (a) CONDITIONAL hinges on one override; mechanical +0x with 29.8% ROCE gives destination 23.75x, Hurdle base 1.65 / bull 1.86, STOP; (b) shared-catalyst third path observed, exports +~50% while receivables grew 2.4x faster than revenue and ECL frozen; (c) on 24% closing ROCE + mechanical Pillar 3, destination 20.7x below trailing 24.3x, Hurdle base 1.44 / bull 1.62, STOP; RRM 22.4x already STOPs; (d) falsification metric already on the line (DSO 114 exactly, static ECL, ex-works stalled 80% two quarters); (e) governance weakest where it matters (CFO from Mani Auto RPT counterparty, new 70yo MD, pledge NOT FOUND, Rs 29 Cr Alkop guarantee off table, Alkop negative reserves); (f) zone likely reached only on thesis break.

---

## 1. Transition data series

### Topline (consolidated, screener Data_Sheet.csv, FY23-FY26)

| Year | Revenue Rs Cr | Growth % |
|---|---|---|
| FY23 | 219.36 (screener) | NOT FOUND (FY22 not in continuous set) |
| FY24 | 212.62 (screener) | -3.1% (computed) |
| FY25 | 242.52 (screener; FY26-AR comparative restates to 239.28, B01 note) | +14.1% (computed) |
| FY26 | 293.81 (screener; B01 validated to results PDF consol) | +21.2% (computed); +22.8% on the 239.28 restated base (B03) |

3yr revenue CAGR FY23-FY26 10.22% (B10). Q1 FY27 revenue 91.79 Cr, annualises to 367.2 Cr (B10).

### Margin (consolidated)

| Year | Gross margin | EBITDA margin | Net margin |
|---|---|---|---|
| FY23 | NOT FOUND (cost lines incomplete, single-segment) | 24.31% (PBT 42.5 + Int 2.91 + Dep 7.92 = 53.33 / 219.36, computed from screener) | 14.86% (32.6 / 219.36) |
| FY24 | NOT FOUND | 21.22% (45.12 / 212.62, computed) | 11.46% (24.36 / 212.62) |
| FY25 | NOT FOUND | 19.14% (46.41 / 242.52, computed) | 10.28% (24.93 / 242.52) |
| FY26 | NOT FOUND | 22.19% (65.21 / 293.81; B10, B01 EBITDA validated to results PDF p.12) | 13.02% (38.25 / 293.81) |

EBITDA convention here is PBT + Interest + Depreciation (includes other income, matches B10/B01 FY26 65.21). CRISIL operating margin band 18.65-20.39% over the two years through FY25 (B10; CRISIL p.1). Gross margin NOT FOUND per year: FY26 power/fuel, other mfr expense and selling lines are blank in screener and no audited segment/cost breakout exists (B01, B04 FLAG-DISCLOSURE).

### Cash conversion (consolidated unless marked standalone)

| Year | OCF Rs Cr | OCF/EBITDA | CFO/PAT | Debtor days | WC % of sales |
|---|---|---|---|---|---|
| FY23 | 50.09 (screener) | 93.9% (computed) | 1.54 (computed) | ~82.7 consol (49.71/219.36×365, computed) | NOT FOUND (payables aggregate, B01) |
| FY24 | 28.33 (screener) | 62.8% (computed) | 1.16 (computed) | ~94.3 consol (computed) | NOT FOUND |
| FY25 | 27.05 (screener) | 58.3% (computed) | 1.09 (computed) | ~91.2 consol (computed); standalone 85 (B02 Note 31) | ~25% (B04; WC days 108.99, B01) |
| FY26 | 23.32 (screener) | 35.8% (computed) | 0.609 (23.32/38.25, B10) | ~112.8 consol (computed); standalone 114 (B02 Note 31) | ~34.7% (B04; WC days 126.56, B01) |

Standalone deterioration (the flag core, B02): receivables +72.1% YoY vs revenue +28.5%; >6-month ageing bucket 6.8% (FY25) to 22.2% (FY26); standalone DSO 85 to 114 days; standalone operating cash conversion 35.3% (Cash from Ops Rs 1,448.22L / Operating Profit before WC changes Rs 4,097.81L, Standalone Cash Flow Statement AR pp.98-99); standalone cash down 69.7% (Rs 1,341.82L to Rs 406.40L); ECL allowance static Rs 19.57L both years (Note 6). Consolidated ageing broadly stable ~11% (B02, Note 6 consol AR pp.150-151).

CRISIL working capital commentary, verbatim (B10 rating_wc_quote; CRISIL Rating Rationale, 23-Apr-2026, pages 1-2, WEAKNESSES and RATING SENSITIVITY sections):

"Customer agreements include PRICE ESCALATION CLAUSES to periodically adjust selling prices for RM price movements; however there is a LAG in implementing price changes. Opmargin was 18.65-20.39% in the two years through March 2025; sustenance at healthy level remains monitorable. [DOWNWARD FACTOR:] SIZEABLE STRETCH IN THE WORKING CAPITAL CYCLE, or larger-than-expected debt-funded capex or acquisition or sizeable dividend payout [would trigger downgrade]."

CRISIL liquidity ADEQUATE; current ratio 2.45x as on 31-Mar-2025; interest coverage 12.34x FY25; export share 30-35% (B10; CRISIL pp.1-2).

### ROCE and ROE (consolidated, AR Note 33 basis)

| Year | ROCE | ROE | Capital-employed basis |
|---|---|---|---|
| FY23 | NOT FOUND (Note 33 basis) | NOT FOUND | — |
| FY24 | NOT FOUND | NOT FOUND | — |
| FY25 | 23.72% (AR Note 33, B01 p.166); independent EBIT/(TA-CL) 20.31% closing basis | 16.43% (AR Note 33, B01) | AR uses average capital employed; independent cross-check uses closing (TA-CL) |
| FY26 | 29.80% (AR Note 33, B01/B10); independent EBIT/(TA-CL) 26.08% closing; ~24% closing operating (deliberation alt) | 22.25% (AR Note 33, B01) | as above; ~3.5-4pp divergence from average-vs-closing and EBIT convention (B01) |

---

## 2. Catalyst inventory

From B05.triggers (7) and B07.catalysts_12m (3).

B05-T1 US export ramp (Allison, Federal-Mogul DRiV, tariff-exempt HCV/LCV). Tier: claim (documented capex, claim on ramp). Window near. Conviction HIGH. Confirm: continued QoQ export revenue growth against filed results. Kill: US tariff escalation with no customer burden-sharing, or reversal of HCV/LCV exemption.

B05-T2 Ex-works export-term conversion. Tier: claim. Window near-medium. Conviction M-H. Confirm: ex-works % rising past 80% toward 90%, receivables days falling. Kill: stalling at 80% with elevated receivables (FY26 receivables Rs 90.77 Cr from Rs 60.63 Cr FY25).

B05-T3 Alkop revenue ramp (John Deere/Eaton/TACO Prestolite pipeline). Tier: claim. Window medium. Conviction M. Confirm: a quarter meeting/exceeding 25-29% guided growth with one reconciled FY27 number. Kill: continued shortfall vs any stated target, or a fourth unreconciled restatement.

B05-T4 Menon Brakes railway/OEM approval (dynamometer-gated). Tier: claim (documented capex). Window near (guided Aug-2026). Conviction LOW. Confirm: actual dynamometer installation and first railway/OEM dispatch in a filing. Kill: fifth slippage past Aug-2026, or another unexplained vendor change.

B05-T5 RM cost pass-through / margin sustainability 20-22%. Tier: claim. Window ongoing. Conviction M. Confirm: FY27 quarterly margins holding 20-22% (Q1 FY27 ~21.9%). Kill: a quarter below 18% with RM blamed again.

B05-T6 PTFE bushes for EV (7-part European qualification). Tier: claim. Window medium-long. Conviction LOW. Confirm: approval of 3-4 more parts and a first PO. Kill: continued single-part-only progress with no new timeline.

B05-T7 Aerospace/industrial diversification (Honeywell, Mahindra, Mayekawa). Tier: inference/claim. Window long. Conviction LOW. Confirm: a named, quantified order in a subsequent call. Kill: these names disappearing from commentary.

B07-C1 Menon Brakes dynamometer commissioning + first railway/OEM order. Tier: documented capex, claim on timing. Window retargeted end-Aug-2026 (3rd/4th deadline). Anchor Q1 FY26 call (orig), Q4/FY26 call (retarget).

B07-C2 First firm PTFE bush order (1 of 7 parts orally approved). Tier: claim. Window 1-2 months from Q4/FY26 call. Anchor Q4/FY26 call (May-2026).

B07-C3 Q1 FY27 results, first read on FY27 division-level guidance (Alkop Rs 120 Cr, Brakes Rs 100 Cr). Tier: claim. Window Q1 FY27 (Aug-2026 reporting). Anchor Q1 FY26 orig guidance, Q4/FY26 reaffirmation.

capex_embedded_growth 28.9% (B07).

---

## 3. Flags with complete underlying findings

### FLAG-CASH — active — GROWTH-INDUCED

Cash multiplier 0.85x (base 0.80x + 0.05 growth offset; offset permitted, determination is growth-induced not structural). Falsification metric: standalone receivables again outrun revenue OR DSO above 114 days in the next print flips to STRUCTURAL 0.65x (destination drops to ~19.5x).

Cited items behind the determination:
- CRISIL BBB+/Stable/A2 reaffirmed 23-Apr-2026 (post year end), liquidity ADEQUATE, current ratio 2.45x, cash accrual >Rs 31 Cr vs term debt ~Rs 9 Cr (B10; CRISIL pp.1-2).
- CRISIL WC verbatim quote (reproduced in full in Section 1 above): stretch is a downward sensitivity, not realised weakness; balance-sheet pressure attributed to debt-funded capex.
- Consolidated ageing stable ~11% both years vs standalone spike (B02, Note 6 consol AR pp.150-151); deterioration standalone-entity-specific.
- Menon Alkop hived to wholly owned subsidiary 23-Jan-2024, re-routing intercompany receivables (B03).
- Standalone receivables +72.1% vs revenue +28.5%; >6mo ageing 6.8% to 22.2%; DSO 85 to 114; standalone cash conversion 35.3%; standalone cash down 69.7%; ECL static Rs 19.57L (B02, Note 6/31 AR pp.114,126-127; Standalone Cash Flow Statement AR pp.98-99).
- Q3 FY26 "180 to 30 day" ex-works pledge contradicted by Q4 FY26 (debtors still >180d, interest re-labelled one-off, DDP customers refusing conversion) (B12b MAJOR; Q3 FY26 call p.18; Q4 FY26 call pp.6-7, p.16).

Capex commissioning timeline: CWIP converted to operating assets Rs 9.10 Cr to Rs 0.09 Cr FY26 (B04); capex Rs 26.94 Cr FY26, Rs 31.02 Cr FY25 (B01); guided Rs 35 Cr next 2 years (Bi-Metal Rs 25 Cr, Alkop Rs 7 Cr, Brakes Rs 3 Cr, Q4/FY26 call, B05).

Receivables composition: consolidated receivables Rs 90.77 Cr FY26 vs Rs 60.63 Cr FY25 (screener); standalone Note 31 ageing >6mo 22.2%; Note 6 vs Note 31 internal contradiction (Note 6 own >6mo Rs 588.77L FY26 vs Note 31 schedule total, 2.5x-16x gap, B02 finding 5).

### FLAG-GATE0 — active — backward artifact, does not cap the gate

Core 54, moat 16, grand 70/160. Blocks A 19/20, B 5/20, C 6/20, D 18/20, E 6/20 (B01). Depressors: (1) mandatory one-tier LIMITED-history downgrade of AVERAGE core to AVOID because only 4 continuous years exist (FY23-FY26) after a 15-year filing gap disconnects FY06-FY08; (2) non-binding Block B<8 deal-breaker (5/20: negative FCF both measurable years FY25 -3.97 Cr, FY26 -3.62 Cr; WC days +17.6). Block A (19/20) and D (18/20) strong; moat MODERATE (3 confirmed). Historical depressors are a filing-continuity gap and a capex-heavy expansion phase (Net Block +56%, borrowings +218% FY23-FY26), not distress (B01).

### FLAG-PROMOTER — not triggered (verdict CAUTION)

Scorecard 6 clean / 3 caution / 1 red (B08). Promoter holding 68.44%, stable vs FY25 (Note 9 AR p.115). No deal-breaker confirmed; pledge >40% check UNRESOLVED not cleared.

Adverse findings (all carry forward):
- New CFO Chandrakant Ghatge's only disclosed prior employer is Mani Auto Components, Kolhapur, the Executive Chairman's own RPT sales counterparty, not an external professional hire; effective 4-Mar-2026 (VERIFIED, AR p.42).
- Simultaneous MD (R.D. Dixit, ~82-83, resigned; Arun Aradhye in) and CFO change, both 4-Mar-2026, ~4 weeks pre year-end (VERIFIED, AR pp.4-5).
- New MD Arun Aradhye 70 at start of a fresh 5-year term (VERIFIED, AR pp.65-66).
- Pledge status UNRESOLVED: AR silent; web conflicts (8.3% to Bajaj Finance vs nil as of Mar-2025); BSE Reg 31 fetch HTTP 403 (UNVERIFIED).
- Promoter holding step-down 70.18% to 68.44% (~1.74pp) at Sep-2024, no disclosed reason; an unverified web claim of a ~9.73 lakh share sale by Nitin Ram Menon does not cleanly reconcile (UNVERIFIED).
- 2018 NCLT (Mumbai): MENONBE bank accounts frozen during the Gitanjali Gems investigation over a reportedly shared independent director; no subsequent SEBI/SFIO/ED action found (MEDIA REPORTED).
- RPT sales to Mani Auto Components ~Rs 19.47 Cr (6.6% of group revenue) at consolidated level vs Rs 4.37 Cr standalone; interest-free unsecured advance to Menon Brakes +44.9% to Rs 457.22L, no disclosed terms (VERIFIED, Note 16 AR pp.107-109).

Transition evidence: Nandan Borgalkar appointed Independent Director effective 1-Oct-2025, 40 years sector-relevant leadership at named checkable employers (VERIFIED, AR pp.65-66).

---

## 4. Credibility grade

Grade C (Mixed). promise_delivery: 1 delivered, 5 partial, 6 missed (B05). excuse_pattern balanced-with-one-notable-deflection.

Repeated evasions:
- Dynamometer / railway approval timing: asked Q1-Q4 FY26; answer changed every quarter, ETA moved 4 times (Sep-2025 to Q3/Q4 FY26 to ~May-2026 to Aug-2026), never delivered, explanation degraded to explicit refusal to explain.
- Alkop real forward revenue target/timeline: asked Q1/Q3/Q4 FY26; changed between quarters, contradicted by a same-period investor presentation, never reconciled.

Guidance versus delivery (B05.promise_delivery rows):
- FY26 revenue ~Rs 300 Cr (Q1 FY26 call) -> delivered (FY26 Rs 293.81 Cr; audited total income >Rs 300 Cr incl other income).
- FY26 EBITDA margin 22% (Q1 FY26) -> partial (revised to 19-20% across Q2/Q3; FY26 actual ~20.0%, met revised guide only).
- Alkop FY26 revenue Rs 85-90 Cr (Q1 FY26) -> missed (actual ~Rs 60-65 Cr; management admits "slower").
- Alkop FY27 revenue Rs 120 Cr (Q1 FY26) -> partial/inconsistent (re-timed to "next 2 years" Q4; same-period presentation says Rs 95 Cr by FY27 from Rs 40 Cr, never reconciled).
- Brakes dynamometer by end-Sept-2025 enabling railway approval and Rs 100 Cr FY27 target (Q1 FY26) -> missed (4 slips; zero railway revenue; explanation degraded to refusal by Q4).
- Brakes FY26 revenue Rs 13-14 Cr (Q2 FY26) -> partial (H1 actual ~Rs 4 Cr; no explicit FY26 segment actual).
- PTFE bushes 7 parts ~Rs 1.25 Cr/month (Q3 FY26) -> partial (1 of 7 orally approved by Q4).
- Ex-works conversion ~90% (Q3 FY26) -> partial (80% by Q4, up from 60-70%).
- Canada OEM deal ~Rs 50-60 Cr/yr, meeting Apr-2026 (Q2 FY26) -> missed (no mention Q3/Q4; planned visit referenced Q4 p.16, no closure).
- Distributor network 35 to 150 (Q1 FY26) -> missed (never mentioned again).
- Menon Ventures EV-charging (Q1 FY26) -> missed (never mentioned again).
- FY27 company revenue Rs 350 Cr (Q1/Q3 FY26) -> partial (raised to >Rs 360 Cr Q4; Q1 FY27 Rs 91.79 Cr annualises ~Rs 367 Cr, one quarter of evidence).

Concall mode used (four FY26 calls: Q1 Aug-2025, Q2 Nov-2025, Q3 Jan-2026, Q4/FY26 May-2026). B07 F2 flagged the B05 promise-delivery record as unavailable to B07 at the time; self-service concall substitute used there (MINOR, no scoring impact).

---

## 5. Scorecards and market sizing

### Gate 0 (B01)

Grand 70/160. core_score 54/100, moat_score 16/60. Blocks: A 19/20, B 5/20, C 6/20, D 18/20, E 6/20. moats_confirmed 3/12, moat_class MODERATE. classification AVOID. history_downgrade true. Deal-breakers: Block B<8 (5/20) -> max GOOD (non-binding, actual already below cap). data_years 4, FY23-FY26.

### Emerging Moat (B07)

em_score 11, em_classification NONE. active_categories: E2 China+1/export growth (Strong, documented+claim, 0-24m partly realised); C1 customer ecosystem EV via Tier-1s (Moderate, documented, 12-24m); A1 rare capability PTFE bushes (Moderate, claim/partial documented, 12-24m). evidence_mix documented 12, claim 14, inference 2. combined_assessment AVOID.

### Accounting quality (B02)

accounting_quality 5/10. going_concern NONE. restatements none. Top findings with note_ref and rating:
1. Standalone receivables +72.1% vs revenue +28.5%; >6mo ageing 6.8% to 22.2%; DSO 85 to 114; consolidated ageing stable ~11%; ECL static (Note 6, 31 standalone AR pp.114/126-127; Note 6 consol pp.150-151) — red_flag.
2. Standalone cash conversion 35.3% (Rs 1,448.22L / Rs 4,097.81L); standalone cash down 69.7% in a year PAT grew 64.4% (Standalone Cash Flow Statement AR pp.98-99) — red_flag. [Note: 64.4% is a basis error; correct standalone PAT growth 61.9%, B03/B12a.]
3. Rs 29 Cr corporate guarantee to Menon Alkop (18.9% of standalone net worth) + disputed TDS Rs 12.78L, neither in any Contingent Liabilities table (CARO Annexure A AR pp.92-93; Note 1 para 11(ii)) — red_flag.
4. AOC-1 shows Menon Alkop (SEBI material subsidiary) negative Reserves Rs (206.98)L vs parent unimpaired carrying cost Rs 2,823.50L (~4.6x gap), no impairment (AOC-1 AR pp.41-42; Note 3) — red_flag.
5. Note 6 own >6mo sub-figure (Rs 588.77L FY26 / Rs 16.13L FY25) is 2.5x-16x smaller than Note 31 total for same date (AR p.114/116 vs pp.126-127) — red_flag.
6. Board's Report ratio table (undisclosed consolidated basis) shows Debtors Turnover -6.27% vs standalone Note 33 +12.6% same year (Board's Report Item 13 AR p.60) — red_flag.
7. CRISIL reaffirmation (23-Apr-2026) predates board adoption (14-May-2026) by ~3 weeks; KFI table has no FY26 full-year actuals — watch.
8. Interest-free unsecured advance to Menon Brakes +44.9% to Rs 457.22L, no terms; interest income fell 50.9% (Note 8, 16, CARO AR pp.92-93/108-109) — watch.
9. Trade payables +71.5% tracking receivables, both outpacing revenue +28.5%; payable days up ~51 to ~65 (Note 14, 30 AR pp.119,125-126) — watch.
10. Simultaneous MD and CFO change 4-Mar-2026, ~4 weeks pre year-end; an independent director also resigned during the year (Board's Report AR pp.4-5; Note 16) — watch.
11. RPT sales to Mani Auto Components (Chairman a partner) ~3x larger at consolidated (Rs 19.47 Cr, 6.6%) than standalone (Rs 4.37 Cr, 2.1%) (Note 16 AR pp.108-109/145-146) — watch.
12. No audited export/domestic split or customer concentration disclosure despite ~35% export share cited; no Ind AS 115 contract asset/liability (Note 17 AR pp.119-120) — watch.
13. Disclosure regression vs FY22 AR: 33 notes vs 36; no Ind AS 10 subsequent-events note despite 45-day gap to adoption — watch.
14. No Ind AS 19 numeric actuarial assumptions for gratuity/leave (Note 26, 27 AR pp.123-124) — watch.
15. Other operating revenue +170.9% and Other Income nearly tripled to 7.7% of PBT, both less-recurring (Note 18, 19 AR p.120) — watch.

### Market (B09)

tam_cr {conservative 8500, realistic 10100}. sam_cr 1858 (21.9% of TAM). som_3yr_cr 240.8. som_5yr_cr 269.4. runway_class STRONG. som_implied_revenue_cagr yr3 7.5%, yr5 6.8% (domestic-only, FLAG-SCOPE; excludes exports ~34%). current_sam_share 10.4%, revenue_headroom 9.6x. mgmt_claim_cr 9000, mgmt_claim_ratio 1.06 ("reasonable"). Management 25% CAGR aspiration (FY27 Rs 350-360 Cr, FY28 Rs 500 Cr) is ~3.3x the domestic-SOM 7.5%; the reconciling factor is the export leg outside domestic TAM (FLAG-VALUATION-GAP).

### Peer triangulation (B06)

Verified: China+1/Europe+1 sourcing shift into India auto-component chains (HARSHA, NRBBEARING, PRECAM, 3 anchors); copper/aluminium RM inflation with escalation-clause lag industry-wide (HARSHA, PRECAM, 4 anchors).
Partially verified: competitor margin claims (BIMETAL screening cross-check, PRECAM); customer concentration "no customer above 15%" (NRBBEARING).
Contradicted: "major capex behind us, sweating assets toward 2-2.5x turns" — NRBBEARING Q3 FY26 call (13-Feb-2026), Harshbeena Zaveri, p.11 of 17: "NRB is not a company that operates like a multinational, which goes and puts in like a huge plant and massive capacities and then tries to sweat them and look for business. That's not how we operate." All three peers mid-expansion in the same period.
Unverifiable: US tariff treatment (HCV/LCV exemption, ~25% duty with burden-sharing); DDP to ex-works shift; scarce/delayed dynamometer supply chain. net_narrative_effect: complicates. Peers describe export/Europe demand as slow and fragile (PRECAM subsidiary MFT GmbH insolvent).

---

## 6. Valuation pillar detail (Role 1, B11)

Four-pillar build (Section 1B v3.3, verifier C re-derived exactly, B12c phase 3):
- Pillar 1 (ROCE premium, Amendment 5: 0.5×ROCE+7.5, floor 9, cap 24): 0.5×29.8+7.5 = 22.4x (under cap). Alt on 24% closing ROCE: 19.5x. FTTCP SUSTAINED verdict is sole Pillar 1 authority (current ROCE, no trajectory blend; Amendment 4.5 N/A). ROCE recovery NOT CREDITED (no depression); Strategic re-rating route BARRED. Source: deliberation, AR Note 33.
- Pillar 2 (cash multiplier): GROWTH-INDUCED -> 0.80 base + 0.05 growth offset = 0.85x. Quality-adjusted base 22.4×0.85 = 19.0x.
- Pillar 3 (growth premium): draft +0x (EM 11 NONE); Operator Override 1 = +1x.
- Strategic premium: +0x (single-credit, ROCE re-rating barred).
- Raw destination PE (Row F): 19.0 + 1.0 + 0.0 = 20.0x.
- UA (Amendment 3, min(F×1.25, cap)): 20.0×1.25 = 25.0x; min(25.0, 25) = 25.0x. Three qualifiers evidenced: listed >30yr; Gate0 grand 70>60; FII+DII 0.24%<3%.
- Sector cap 25x (Manufacturing/Industrial), absolute. UA-adjusted raw lands exactly on the cap. Quality-uplift-on-cap NOT applied (requires durability >= Moderate-Strong; EM NONE; moot, raw = cap).

destination_pe_track2_additive: mid 25.0x, range 23.0-25.0 (Amendment 6 proportional ±7.5% capped). destination_pe_track1_rrm: RRM = 1 + (13.5-14)×0.12 = 0.94; 19.0×0.94 = 17.9, ×1.25 UA = 22.4, min(22.4,25) = 22.4x; r 14% (small/micro, bounded [9,18]). divergence 11.6% (<15%, no forced switch; Track 2 governs, RRM conservative x-check STOPs).

hurdle_ratio: formula (1+g)³ × (Dest mid / Current PE), PE ratio 25.0/24.3 = 1.0288. base (1.19)³×1.0288 = 1.73 FAIL; bull (1.24)³×1.0288 = 1.96 PASS; grade-C bull cap = base+5 = 24%. Verdict CONDITIONAL (Amendment 2), caps WATCHLIST/BUY-ON-DIPS. EPS-basis consistency: numerator (FY26 to FY29 reported EPS) and denominator (TTM reported EPS 7.83) both reported basis; SFL spurious-pass trap avoided. hurdle_verdict CONDITIONAL.

fair_values: Track 2 {bear 153, base 290, bull 584}; Track 1 {bear 137, base 260, bull 523}. 4D prob weights Mixed(C) = 35/45/20; 0.35(-6.9)+0.45(15.1)+0.20(45.3) = 13.4% prob-weighted CAGR. U/D 52.6%/19.5% = 2.7x.

entry_range 132-148 (base FV 290 / 1.953 Tier A = 148; 30% entry 290/2.197 = 132). mos_price 118 (25%-entry 148.5 × 0.80). decision WATCHLIST (BUY-ON-DIPS 132-148; AVOID-on-valuation at CMP 190). cash_multiplier_used 0.85. structural_or_growth growth-induced. ua_applied true (1.25). sector_cap_used 25.

SOM cross-check: base FY29 domestic ~Rs 241 Cr approx B09 SOM Rs 240.8 Cr; total growth export-led beyond domestic SOM scope. Shared-catalyst flag (Amendment 4): export ramp is Pillar 3 driver AND Pillar 2 receivables cause, flagged for Role 3. Unresolved inputs used: promoter pledge NOT FOUND (no valuation use); consolidated segment P&L NOT FOUND (SOTP not applied quantitatively; relied on P/E and EV/EBITDA) — both conservative.

Devil counter-build (Role 3, B15): mechanical Pillar 3 +0x with 29.8% ROCE -> 22.4×0.85=19.0, +0=19.0, ×1.25=23.75x; Hurdle base 1.65 / bull 1.86 STOP. On 24% closing ROCE + mechanical -> 19.5×0.85=16.575, ×1.25=20.7x, below trailing 24.3x; Hurdle base 1.44 / bull 1.62 STOP. RRM 22.4x already STOPs.

---

## 7. Gaps ledger

| Item | Stage/block needing it | Where to obtain |
|---|---|---|
| Promoter pledge % (AR silent; web conflicts 8.3% Bajaj Finance vs nil; BSE Reg 31 HTTP 403) | B08, B10, governance monitorable | BSE Regulation 31 consolidated pledge disclosure; FY27 AR shareholding note |
| Consolidated segment P&L (Bimetal/Alkop/Brakes split) | B04, B11 (SOTP not applied) | Future audited Ind AS 108 segment note; investor presentation updates |
| Alkop per-unit realisation (Rs 7.5 lakh/MT slide 33 vs Rs 2.0-2.2 lakh/MT concall) | B04 FLAG-DATA | Management Q&A or AR disclosure |
| Standalone Note 6 vs Note 31 ageing contradiction (2.5x-16x) | B02 | Management question for next AR/concall |
| CRISIL post-audited FY26 surveillance review (reaffirmation predates board adoption) | B02, B05 | CRISIL website / next rating action (Q2 FY27 surveillance expected) |
| Menon Alkop reserves trajectory + impairment test (Ind AS 36) | B02 finding 4, monitorable | FY27 AOC-1 (Board's Report Annexure I) |
| Formal Contingent Liabilities table covering Rs 29 Cr Alkop guarantee | B02 finding 3, monitorable | FY27 AR Notes (standalone and consolidated) |
| Menon Brakes advance terms (Rs 457.22L, +44.9%, interest-free) | B02, B03 | FY27 AR Note 8/16 |
| MD/CFO/CS continuity (post 4-Mar-2026 transition) | B08, B03 | Exchange filings; FY27 Board's Report |
| Audited export/domestic revenue split and customer concentration | B02 finding 12, B05 | FY27 AR if disclosed; management Q&A |
| Announcements folder (Reg 30 cross-check) | B00, B05 | BSE/NSE announcements for MENONBE |
| Research folder | B00 | Brokerage/independent research if available |
| FY23-FY24 capex, trade payables, cash-flow breakdown | B01 (B2/B3/B4 2-year subsample only) | Older annual reports FY23, FY24 |
| India export-specific market size for bi-metal bearings / Alkop EV parts | B09 FLAG-SCOPE | Industry reports decomposable by segment; ACMA export data |
| Braking friction (ex-Railways) domestic TAM corroboration | B09 FLAG-DATA-GAP | Independent brake-friction market report |
