# STAGE 11: ROLE 1 MULTI-METHOD VALUATION (B11-valuation)
## OBSC Perfection Ltd (OBSCP)
**Run Date:** 2026-07-12 | **Model:** claude-opus-4-8 | **Status:** COMPLETE
**Framework authority:** Master v3.3 / Section 1B v3.3 (Amendments 1-8 + v3.4 4.1-4.4) / FTTCP v1.2
**Input source:** B10-valinputs (sole input table) + fttcp-deliberation (authoritative pillar rulings, consumed not re-derived)

> Pipeline mode: all sections executed in one pass; framework STOP checkpoints written as interim state lines then continued. Every input carries its B10 anchor on first use. No number is estimated; NOT FOUND is the only fill.

---

## SECTION 1A: METHOD SELECTION & JUSTIFICATION

**Business model (B10 company_identity):** asset-heavy precision-engineering contract manufacturer, B2B auto/defence/EV components. NSE Emerge (SME) listed Oct 2024. Sector corrected to **Manufacturing** (fttcp-deliberation, supersedes manifest EPC/Civil).

| Method | Suitable here? | Weight | Justification |
|---|---|---|---|
| **P/E (exit multiple from Section 1B)** | YES — PRIMARY | 70% | Profitable (FY26 PAT Rs 27.01 Cr, B10), clean-ish earnings, exit PE is EARNED via the four pillars. This is the framework's designated exit-PE authority. |
| **EV/EBITDA** | YES — SECONDARY | 20% | Capital-intensive; net debt Rs 67.33 Cr (B10); leverage rising with capex. Cross-checks the PE destination (rule of thumb EV/EBITDA ~0.6-0.7x of PE destination). |
| **P/B** | Tertiary | 10% | Asset-heavy; BVPS Rs 66.67 (B10). Floor/sanity only — book understates a growth franchise. Not primary (not a lender). |
| DCF | NO | 0% | FCF strongly negative (FY26 FCF Rs -78.0 Cr, B10); high-growth + capex phase makes terminal value dominate. Excluded per Master v3.3 (DCF fails for negative-FCF high-growth). |
| EV/Sales, EV/capacity, NAV, SOTP, sector-specific | NO | 0% | Company is profitable (EV/Sales not needed); no annuity/BOO split (SOTP N/A); not real estate/holdco (NAV N/A). |

**Peer relative cross-check:** peer median P/E, EV/EBITDA, P/B, ROCE = **NOT FOUND** (B10 input_gaps; B06 did not extract peer financial medians). No relative valuation cross-check possible; multiples assessed on absolute basis only. Flagged as an unresolved input used.

---

## SECTION 1B: FOUR-PILLAR EXIT MULTIPLE FRAMEWORK v3.3 (CRITICAL)

**Formula:** Raw Destination PE = (ROCE Base x Cash Multiplier) + Growth Premium + Strategic Premium; Final = min(Raw x UA if qualified, Sector Cap).

### Pillar 1 — ROCE Base Multiple (continuous formula)

**FTTCP ROCE forward verdict = STAGNANT** (fttcp-deliberation, authoritative; changed from RECOVERING on CRISIL-anchored FY26 data — recovery not visible, year-end ROCE fell again from FY25's 19%). Per the sole-authority table, **STAGNANT -> Pillar 1 uses CURRENT ROCE** (no midpoint smoothing).

**ROCE convention decision.** FY26 ROCE computes two ways from anchored EBIT Rs 36.26 Cr (= PBT 31.77 + interest 4.49, B10):
- Year-end capital employed ~Rs 240.5 Cr (networth 171.97 + bank borrowings 68.54) -> **15.1%** (36.26/240.5).
- Average capital employed ~Rs 185.7 Cr -> **19.5%** (36.26/185.7).

I use the **year-end convention (15.1%)** as primary because (a) the anchored comparatives FY24 33.38% and FY25 19.01% are on a year-end basis (B10: "year-end basis assumed consistent"; verified — FY25 year-end reconstruct ~18% is far closer to 19.01% than the ~23% average basis), so consistency demands year-end; and (b) it is the conservative reading (framework conservative-bias rule). The average basis (19.5%) is carried as an explicit upper sensitivity. I do NOT estimate a new ROCE.

- ROCE used for base (primary, year-end): **15.1%**
- Pillar 1 Base PE = 0.5 x 15.1 + 7.5 = 15.05 -> **15.1x** (floor 9x, cap 24x; not binding)
- Sensitivity (average basis 19.5%): 0.5 x 19.5 + 7.5 = 17.25 -> **17.3x**
- **ROCE recovery credited via: NOT CREDITED (STAGNANT).** Strategic Premium remains +0x (single-credit rule; ROCE not double-credited).

### Pillar 2 — Cash Conversion Multiplier

- Cumulative CFO/PAT (FY22-26): **0.31x** (B10); latest FY26 CFO/PAT **-0.07x** (CFO Rs -1.95 Cr, B10); FCF **negative** (Rs -78.0 Cr).
- Raw band: CFO/PAT below 30% / CFO negative -> base multiplier **0.80x**.
- **Structural or growth-induced? GROWTH-INDUCED** (fttcp-deliberation Override 1, operator-decided, CRISIL-validated: "working capital intensive operations," "long credit periods to export customers," no bad-debt/delinquency flag; receivables +62% and inventory +79% vs 24% revenue print = scale-up build). Not re-litigated per pipeline rule.
- Growth offset: PAT/revenue CAGR >40% (FY26 revenue growth ~54%; PAT CAGR 48.7%, B10) + growth-induced -> **+0.20**.
- **Effective Cash Multiplier = 0.80 + 0.20 = 1.00x.**
- **Quality-Adjusted Base = 15.1x x 1.00 = 15.1x** (average-basis sensitivity: 17.3x x 1.00 = 17.3x).
- **FLAG-CASH carried forward; multiplier actually applied = 1.00x.** Falsifier live: over-12-month receivables bucket >~15% or rising ECL -> reverts to STRUCTURAL (0.65x) and re-engages the cap.

### Pillar 3 — Growth Visibility Premium (decoupled 3a/3b/3c, combined cap +6x)

- **3a Growth Visibility = +3x.** Capex-embedded growth 18% (>=15% threshold, B07); order book Rs 1,200 Cr = 5.5x revenue (>=1.0x); SOM-implied 3yr CAGR 39.1% (>=20%); delivery grade B. Four documented qualifiers -> "+3x if three or more qualify AND delivery grade A/B" (grade B) = **+3x**.
- **3b Moat Formation = +0x.** EM score 23 < 25 (B07) -> +0x per the EM-gated table.
- **3c Duration Premium = +2x.** Order book Rs 1,200 Cr "to be executed over the next 5-6 fiscals" (CRISIL-filed, p.2) = 5.5x revenue, tenor past the 4-year line -> **+2x** (fttcp-deliberation Override 2, operator override: order book genuine).
- **Pillar 3 combined = +5x** (within +6x cap).
- **SHARED CATALYST — FLAGGED.** The capex commissioning / order book drives Pillar 1 context, Pillar 3a AND Pillar 3c and underpins revenue and any ROCE recovery. Role 3 must stress-test the single point of failure (order-book firmness, Rs 100-200 Cr/yr conversion pace).

### Pillar 4 — Strategic Asset Premium

- **+0x.** No rare licence/regulatory monopoly. ROCE re-rating optionality NOT credited here (single-credit; ROCE not entered in Pillar 1 either, verdict STAGNANT). Qualification lock-in is real but already priced in Pillar 3a. **Strategic Premium = +0x** (fttcp-deliberation).

### Undiscovered Alpha (UA) Multiplier — NOT APPLIED

| Qualifier | Status |
|---|---|
| Listed >=12 months | MET (listed Oct 2024, ~21 months to run date) |
| Gate 0 >=60 OR EM >=25 | **NOT MET** (Gate 0 core 52 < 60 AND EM 23 < 25) |
| FII+DII < 3% | MET (2.94%) |
| **All three met?** | **NO -> UA multiplier NOT applied** (Amendment 3) |

### Sector Reality Cap

**Manufacturing = 25x** (fttcp-deliberation, corrected from manifest EPC 20x; the only ceiling, absolute). No quality uplift (UA not triggered).

### Four-Pillar Summary (Track 2 Additive)

| Step | Calculation | Primary (year-end 15.1%) | Sensitivity (avg 19.5%) |
|---|---|---|---|
| A. ROCE Base | 0.5 x ROCE + 7.5 | 15.1x | 17.3x |
| B. Cash Multiplier (effective) | 0.80 + 0.20 offset | 1.00x | 1.00x |
| C. Quality-Adjusted Base | A x B | 15.1x | 17.3x |
| D. Growth Visibility Premium (3a+3b+3c) | +3 +0 +2 | +5.0x | +5.0x |
| E. Strategic Premium | single-credit, not credited | +0.0x | +0.0x |
| **F. Raw Destination PE** | C + D + E | **20.1x** | **22.3x** |
| F2. UA-Adjusted Raw PE | UA not applied -> F | 20.1x | 22.3x |
| G. Sector Cap | Manufacturing | 25.0x | 25.0x |
| **H. Final Destination PE** | min(F2, G) | **20.1x** | **22.3x** |

**Sector cap comparison:** F2 (20.1x, or 22.3x on average basis) < 25x cap -> **cap NOT binding.**

**Destination PE Range (Track 2, primary):** H 20.1x +/-7.5% = 18.59-21.61 -> **18.5x to 21.5x** (midpoint 20.1x). Average-basis convention lifts H to 22.3x (range 20.5x-24.0x), still below the 25x cap — the verdict is robust to the convention choice.

### RRM Dual-Track Derivation (Track 1)

- Base r (small/micro-cap): 14.0%. Adjust: durability MODERATE (qualification lock-in strong, execution moat moderate, customer concentration top-5 50-55%, cash weak) -> +0.5%; governance CAUTION (Omega Bright Steel RPT no non-compete, accounting-quality flags, broken disclosure cadence) -> +0.5%. **r = 15.0%** (in [9%, 18%]).
- **RRM = 1 + (13.5 - 15.0) x 0.12 = 1 - 0.18 = 0.82** (percentage-point reading per Amendment 4.4; within [0.70, 1.60]).
- Fundamental Base PE = the four-pillar raw destination PE (20.1x) — Track 1 overlays the required-return/governance discount that the additive track omits.
- **Track 1 RRM Destination PE = 20.1x x 0.82 = 16.5x** (capped at 25x, not binding). Range +/-7.5% = **15.5x to 17.5x** (midpoint 16.5x).

**Track reconciliation:** Track 1 mid 16.5x vs Track 2 mid 20.1x. Divergence = 3.6/18.3 = **19.7% (>15%)**. Track 1 (RRM) explicitly prices the elevated required return of a governance-flagged inflection micro-cap; Track 2 (additive) is the framework's exit-PE authority but carries no governance discount. **The more conservative track (Track 1 RRM, 16.5x) sets the entry zone.** Both tracks STOP the hurdle, so the choice does not change the decision.

### Hurdle Ratio (Amendment 2 / 4.3)

Current trailing PE = **63.7x** (market cap 1,720.15 / PAT 27.01; = CMP 666 / EPS 10.47 = 63.6x, B10). Return hurdle **Tier A (25%)** — FII+DII 2.94% < 3% (B10). Pass line **1.953**. Grade B (Good) -> **bull EPS CAGR permitted** in the check. Forward EPS built from B05/B09 guidance below (illustrative/EXPECTED).

HR = (1 + EPS CAGR)^3 x (Destination PE mid / Current PE).

| Track / basis | Dest PE mid | HR(base, EPS CAGR 33%) | HR(bull, EPS CAGR 43.4%) | Band |
|---|---|---|---|---|
| **Track 2 additive (year-end, primary)** | 20.1x | **0.74** | **0.93** | STOP |
| Track 2 (average-basis sensitivity) | 22.3x | 0.82 | 1.03 | STOP (reconciles to deliberation's 0.85/1.03) |
| Track 1 RRM (governing) | 16.5x | 0.61 | 0.76 | STOP |

**Hurdle verdict = STOP.** HR(bull) 0.93 << 1.953: 25% CAGR is infeasible from Rs 666 even on bull earnings, because de-rating from ~64x to ~20x swamps earnings growth.

> INTERIM STATE (Section 1 checkpoint): Four-pillar destination PE 18.5x-21.5x (Track 2, year-end primary; midpoint 20.1x); RRM track 15.5x-17.5x. Current PE 63.7x. Hurdle Ratio 0.74 base / 0.93 bull -> STOP. Continuing to Section 2.

---

## SECTION 2: EARNINGS & CASH FLOW PROJECTIONS (illustrative / EXPECTED — NOT anchored)

Base year FY26 (anchored, B10): Revenue Rs 219.54 Cr, EBITDA Rs 43.64 Cr (19.8%), PAT Rs 27.01 Cr (12.24%), EPS Rs 10.47, shares 2.58 Cr. 3-year target = **FY29** (Year 0 = FY26).

### 2A/2B. Assumptions (from B05/B09 guidance, clearly labelled EXPECTED)

| Assumption | Bear | Base | Bull | Rule / source |
|---|---|---|---|---|
| Revenue CAGR (FY26-29) | 18-20% | **33%** | 39% | Base = guidance 40-45% (B05) discounted grade B, below historical 38.5% and SOM 39.1%; Bull = guidance face value (grade B allows), capped at SOM-implied 39.1% (B09); Bear = triggers slip / concentration hit |
| PAT margin FY29 | 11.5% | 12.24% | 13.5% | Base = FY26 level held; Bull = ~1pp EBITDA guidance flow-through (B05); Bear = WC/interest drag |
| Share dilution | some | ~0% | ~0% | Base holds 2.58 Cr (preferential issue Feb 2026 already in count); further dilution risk flagged (bear) |

### 2C. Projection Table (EXPECTED)

| Line (Base case) | FY26 (Y0) | FY29 (Y3) |
|---|---|---|
| Revenue | Rs 219.54 Cr | Rs 516.5 Cr (x1.33^3) |
| PAT | Rs 27.01 Cr | Rs 63.2 Cr |
| **EPS** | Rs 10.47 | **Rs 24.5** |
| Implied EPS CAGR | — | 32.9% |

| Scenario | Rev CAGR | FY29 Revenue | FY29 PAT | FY29 EPS | EPS CAGR |
|---|---|---|---|---|---|
| Bear | 20% | Rs 379.4 Cr | Rs 43.6 Cr | Rs 16.9 | 17.4% |
| Base | 33% | Rs 516.5 Cr | Rs 63.2 Cr | Rs 24.5 | 32.9% |
| Bull | 39% | Rs 589.6 Cr | Rs 79.6 Cr | Rs 30.9 | 43.4% |

### 2D. Sanity checks

| Check | Result | Pass? |
|---|---|---|
| Revenue growth faster than capacity allows? | Base 33% < SOM 39.1%; capex-embedded 18% + order book 5.5x revenue | Pass |
| Margins require something unprecedented? | Base holds FY26 12.24%; bull +1pp per guidance | Pass |
| ROCE stays above 15%? | Base Year-3 ROCE ~mid-teens to ~20% (STAGNANT, no recovery assumed) | Marginal — consistent with STAGNANT |
| FCF funds growth without excessive new debt? | NO — FCF negative, capex debt/equity-funded (net debt rising) | FAIL — flagged (FLAG-CASH) |
| EPS growth operational not financial? | Operational (revenue-led) | Pass |
| Implied market share gain realistic? | SOM runway MASSIVE (B09); base within SOM | Pass |
| CFO/PAT trajectory consistent with Pillar 2 (1.00x, growth-induced)? | Assumes no deterioration; falsifier = over-12m ageing | Conditional |
| **Year-3 ROCE consistent with FTTCP STAGNANT used in Pillar 1?** | YES — base assumes no ROCE recovery; ~15-20% band, consistent with STAGNANT/current | Pass |

**SOM cross-check (Section 1B rule):** base revenue CAGR 33% < B09 SOM-implied 3yr 39.1% -> **CONSISTENT** (no cut needed). Bull 39% sits at the SOM ceiling, justified by filed order book, not exceeded.

> INTERIM STATE (Section 2 checkpoint): projections built; FY29 EPS bear/base/bull Rs 16.9 / 24.5 / 30.9. Continuing to Section 3.

---

## SECTION 3: APPLY EACH VALUATION METHOD

### PRIMARY — P/E (exit multiple from Section 1B; no other exit PE used)

| Source | Exit PE range |
|---|---|
| Four-Pillar Destination PE (Track 2, year-end primary) | 18.5x - 21.5x (mid 20.1x) |
| RRM-track Destination PE (Track 1) | 15.5x - 17.5x (mid 16.5x) |
| Sector Cap (Manufacturing) | 25x (not binding) |

**Target price matrix (FY29, exit PE = destination mid; CAGR from CMP 666):**

| EPS \ Track 2 mid 20.1x | Price | 3yr price CAGR | Track 1 mid 16.5x | Price | CAGR |
|---|---|---|---|---|---|
| Bear Rs 16.9 | Rs 340 | -20.1% (red) | | Rs 279 | -25.2% (red) |
| Base Rs 24.5 | Rs 492 | -9.5% (red) | | Rs 404 | -15.4% (red) |
| Bull Rs 30.9 | Rs 621 | -2.3% (red) | | Rs 510 | -8.5% (red) |

All nine cells < 15% CAGR (red). **Zero cells meet the 25% hurdle.**

**Reverse-engineered entry (25% CAGR, base EPS, destination mid):** Track 2 base target Rs 492 / 1.953 = **Rs 252**; Track 1 (governing) Rs 404 / 1.953 = **Rs 207**.

**P/E fair value range (FY29): Rs 279 (Track 1 bear) to Rs 621 (Track 2 bull).**

### SECONDARY — EV/EBITDA (cross-check)

Exit EV/EBITDA ~0.65x of PE destination -> ~13x (on 20.1x PE). FY29 base EBITDA ~ Rs 516.5 x 20.8% = Rs 107 Cr. EV = 107 x 13 = Rs 1,391 Cr; less est. FY29 net debt ~Rs 100 Cr (capex-heavy, rising) = equity Rs 1,291 Cr / 2.58 = **~Rs 500** base. Consistent with P/E base Rs 492 (triangulation holds).

### TERTIARY — P/B (floor / sanity)

Theoretical P/B = ROE / CoE = 20.5% / 14% = 1.46x. FY29 BVPS ~Rs 125 (retained base PAT). FV ~Rs 183. Low — book understates the growth franchise; **10% weight, treated as floor.** Confirms downside protection is thin at CMP.

### Method-wise fair value summary (base case, Track 2)

| Method | Weight | Base FV |
|---|---|---|
| P/E (Section 1B) | 70% | Rs 492 |
| EV/EBITDA | 20% | Rs 500 |
| P/B | 10% | Rs 183 |
| **Weighted** | 100% | **~Rs 463** |

> INTERIM STATE (Section 3 checkpoint): methods triangulate to a base FV of ~Rs 463-500 (Track 2); all point below CMP 666. Continuing to Section 4.

---

## SECTION 4: TRIANGULATION, ENTRY PRICE & FINAL VERDICT

### 4A. Triangulated fair value (FY29) — BOTH TRACKS

| | Bear | Base | Bull |
|---|---|---|---|
| **Track 2 (additive, 20.1x)** | Rs 340 | Rs 492 | Rs 620 |
| **Track 1 (RRM, 16.5x)** | Rs 279 | Rs 404 | Rs 509 |

More conservative track (Track 1 RRM) governs the entry zone.

### 4B. Methods agreement

P/E and EV/EBITDA agree (base ~Rs 492-500); P/B is the low outlier (Rs 183, book understates growth). All methods point the SAME direction: fair value well below CMP 666. Most-trusted method for OBSCP: **P/E via Section 1B** (exit-PE authority).

### 4C. Return expectation at CMP 666 (Track 2, FY29)

| Scenario | FV | Total return | 3yr CAGR | Meets 25%? |
|---|---|---|---|---|
| Bear | Rs 340 | -49.0% | -20.1% | No (red) |
| Base | Rs 492 | -26.1% | -9.5% | No (red) |
| Bull | Rs 620 | -6.9% | -2.3% | No (red) |

Even the bull FY29 target (~Rs 620) is below today's Rs 666.

### 4D. Probability-weighted expected return

Weights from grade B (Good): **Bear 25% / Base 50% / Bull 25%** (Master v3.3 4D; sole source = Role 5 credibility grade).

| Scenario | Prob | 3yr CAGR (Track 2) | Weighted |
|---|---|---|---|
| Bear | 25% | -20.1% | -5.03% |
| Base | 50% | -9.5% | -4.77% |
| Bull | 25% | -2.3% | -0.59% |
| **Expected CAGR** | 100% | | **-10.4%** |

(Track 1 RRM expected CAGR = -16.1%.) Both far below the +25% Tier A hurdle.

### 4E. Entry price (Tier A divisor 1.953)

| Calculation | Track 2 (additive) | Track 1 (RRM, governing) |
|---|---|---|
| Base FV (FY29) | Rs 492 | Rs 404 |
| Entry = FV / 1.953 | **Rs 252** | **Rs 207** |
| MoS = 20% below entry | Rs 202 | **Rs 166** |

**Entry range Rs 207 (governing RRM) to Rs 252 (additive). MoS price Rs 166** (20% below governing entry). Average-basis convention would lift entry to ~Rs 280, reconciling to the deliberation's Rs 280-320 zone. All entry/MoS levels sit roughly a half to a third of CMP 666 — MARKET-UNLIKELY ZONE (price history not in run inputs).

### 4F. Risk-reward asymmetry (from CMP)

| | Value |
|---|---|
| Bull target Rs 620 | Upside -6.9% (no upside) |
| Base target Rs 492 | -26.1% |
| Bear floor Rs 340 | Downside -49.0% |
| Upside(base)/Downside(bear) magnitude | **0.5x** (should be >=2x -> FAILS) |

No positive upside exists at CMP; all scenarios sit below the current price.

### 4G. Four-Pillar validation

| Check | Result | Pass? |
|---|---|---|
| Year-3 ROCE justifies ROCE base + matches FTTCP? | Base ~15-20%, STAGNANT, no recovery credited | Pass |
| Year-3 CFO/PAT justifies 1.00x cash multiplier? | Assumes no deterioration; falsifier live | Conditional |
| Primary catalyst fired by Year 3 (base)? | Sanand line + order-book conversion within window | Pass |
| Strategic premium justified (single-credit)? | +0x, ROCE not double-credited | Pass |
| UA ordering correct — min(F x 1.25, cap)? | UA not applied (fails 2/3 qualifiers) | Pass |
| Would you buy another stock at 20x with these Y3 metrics? | Yes at ~20x — but not at 63.7x entry | Pass (on exit PE) / FAIL (on entry price) |

### 4H. FINAL VALUATION VERDICT CARD

**Tier: A | Hurdle: 25%**

- **CMP Rs 666 | Market cap Rs 1,720.15 Cr | 2.58 Cr shares | trailing PE 63.7x**
- **FOUR-PILLAR EXIT PE:** ROCE Base 15.1x (FTTCP STAGNANT, current ROCE 15.1% year-end; recovery credited via: NOT CREDITED) x Cash 1.00x (growth-induced, 0.80+0.20 offset) = Quality Base 15.1x; +Growth 3a+3b+3c = +5x (SHARED CATALYST); +Strategic +0x; **Raw = 20.1x**; UA applied N; Sector cap 25x (not binding); **DESTINATION PE 18.5x-21.5x (mid 20.1x)**. Average-basis sensitivity 22.3x.
- **RRM TRACK:** r 15.0%, RRM 0.82, **destination 15.5x-17.5x (mid 16.5x)**; base/base/bull FV Rs 279 / 404 / 509. Divergence 19.7% — RRM governs entry.
- **HURDLE RATIO:** base 0.74 / bull 0.93 -> **STOP.**
- **METHODS:** P/E (70%) Rs 492 base; EV/EBITDA (20%) ~Rs 500; P/B (10%) Rs 183.
- **WEIGHTED FAIR VALUE (FY29):** Track 2 bear/base/bull Rs 340 / 492 / 620; Track 1 Rs 279 / 404 / 509.
- **EXPECTED CAGR (prob-weighted, grade B 25/50/25):** -10.4% (Track 2); -16.1% (Track 1).
- **UPSIDE/DOWNSIDE:** 0.5x (fails >=2x).
- **ENTRY Rs 207-252 | MoS Rs 166.**
- **DECISION: WATCHLIST (deep) — AVOID on valuation at CMP Rs 666.** Business is not an AVOID on quality (FTTCP +2 DEEP WATCH, real order book, capex commissioning); the stock is an AVOID-on-valuation because it fails the 25% hurdle decisively (STOP). Re-engage near Rs 207-280.
- **KEY ASSUMPTIONS THAT COULD MOVE IT:** (down-arrow) over-12m receivables bucket >15% or rising ECL -> cash reverts to STRUCTURAL 0.65x, Pillar 2 cuts base ~35%, destination falls to ~14x. (up-arrow) FY26 ROCE re-rates on average-basis + a confirmed FY27 recovery -> RECOVERING lifts Pillar 1 to midpoint, destination toward 22-24x (still STOPs at CMP). (up-arrow) order-book conversion accelerating >Rs 200 Cr/yr firms 3a/3c.
- **EXIT FRAMEWORK:** target exit destination ~20x; thesis-broken if a second negative CFO year or rising overdue bucket; time stop 3-5 yrs; PE compression floor ~15x (RRM low).
- **ONE-LINE THESIS:** Buying OBSCP only near Rs 207-252 because FY29 base EPS grows to ~Rs 24.5 (33% CAGR) on the Rs 1,200 Cr order book and Sanand ramp, at a four-pillar destination PE of 20.1x (ROCE 15.1%, cash 1.00x growth-induced, EM 23, Manufacturing cap 25x) = ~Rs 492 target; at CMP Rs 666 the de-rating from 63.7x to 20x makes 25% CAGR infeasible (Hurdle STOP). Key risk: cash conversion reverting to structural. Cash quality: growth-induced.

> FINAL: Valuation complete. Four-pillar exit PE 18.5x-21.5x (RRM 15.5x-17.5x). Hurdle Ratio STOP. Entry Rs 207-252. Decision: WATCHLIST (deep) / AVOID-on-valuation at Rs 666.

---

```yaml
stage: B11-valuation
company: "OBSCP"
run_date: "2026-07-12"
model: claude-opus-4-8
status: complete
input_gaps:
  - "Peer median P/E, EV/EBITDA, P/B, ROCE NOT FOUND (B10) — no relative valuation cross-check; absolute multiples only"
  - "FY26 over-12-month receivables ageing bucket unanchored (AR truncated) — falsifier for growth-induced cash verdict"
  - "Supa mega-factory capex quantum/timeline undisclosed — long-term SOM/Pillar 3 not separately modeled"
  - "FY27+ quarterly guidance unavailable (only 2 concalls) — forward EPS built on full-year guidance, labelled EXPECTED"
flags:
  - "FLAG-CASH: growth-induced (CRISIL-validated); cash multiplier ACTUALLY APPLIED = 1.00x (0.80 base + 0.20 growth offset); falsifier over-12m receivables >15% or rising ECL reverts to STRUCTURAL 0.65x"
  - "SHARED CATALYST: order book / capex commissioning drives Pillar 1 context, Pillar 3a and Pillar 3c plus revenue and any ROCE recovery — single point of failure for Role 3"
  - "FLAG-CUSTOMER-CONCENTRATION: top 5 = 50-55%, largest 15-20% (CRISIL) — priced via r=15% in RRM track"
  - "FLAG-RELATED-PARTY / FLAG-ACCOUNTING-QUALITY / FLAG-QUARTERLY-DISCLOSURE carried from B10 into governance leg of RRM r"
framework_versions: "Master v3.3 / Section 1B v3.3 / FTTCP v1.2"
destination_pe:
  track1_rrm: {low: 15.5, mid: 16.5, high: 17.5, r_used: 15.0, rrm: 0.82}
  track2_additive: {low: 18.5, mid: 20.1, high: 21.5}
  divergence_pct: 19.7
  governing_track: "Track 1 RRM (16.5x) — more conservative, prices governance/durability via r=15%; sets entry zone. Both tracks STOP the hurdle."
pillar_detail:
  roce_used: 15.1
  roce_base: 15.1
  roce_recovery_route: "not-credited"
  cash_multiplier: 1.00
  structural_or_growth: "growth-induced"
  growth_offset: 0.20
  growth_premium: 5
  strategic_premium: 0
  shared_catalyst_flag: true
  ua_applied: false
  sector_cap_used: 25
hurdle_ratio: {base: 0.74, bull_used: true, verdict: "STOP"}
fair_values:
  track1: {bear: 279, base: 404, bull: 509}
  track2: {bear: 340, base: 492, bull: 620}
expected_cagr_prob_weighted: -10.4
entry_range: {low: 207, high: 252}
mos_price: 166
upside_downside_ratio: 0.5
decision: "WATCHLIST (deep) — AVOID on valuation at CMP Rs 666; Hurdle STOP"
unresolved_inputs_used:
  - "Peer financial medians NOT FOUND -> no relative cross-check taken; absolute multiples only (conservative: no peer premium credited)"
  - "Over-12m receivables ageing bucket NOT FOUND -> cash multiplier held at 1.00x per operator-decided growth-induced ruling; falsifier flagged, not estimated"
  - "Post-FY26 share dilution NOT FOUND -> base holds 2.58 Cr shares flat (dilution risk flagged in bear); no dilution estimated"
  - "ROCE convention: year-end 15.1% chosen for consistency with FY24/FY25 year-end basis and conservative bias; average 19.5% carried as sensitivity"
som_cagr_crosscheck: "consistent"
one_line_thesis: "OBSCP is a real growth franchise (Rs 1,200 Cr order book, Sanand ramp) but at Rs 666 / 63.7x trailing it is priced ~2.6x above a four-pillar base fair value of ~Rs 492 (destination PE 20.1x, ROCE 15.1% STAGNANT, cash 1.00x growth-induced); Hurdle STOP, WATCHLIST deep, re-engage Rs 207-252."
```
