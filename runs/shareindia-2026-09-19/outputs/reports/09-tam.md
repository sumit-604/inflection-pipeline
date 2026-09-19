# Stage 9 — TAM / SAM / SOM Market Sizing: Share India Securities Ltd (SHAREINDIA)

Run date: 2026-09-19. Model: claude-sonnet-5 + web search. Status: complete (all six sections executed; specific figures marked NOT FOUND where search did not return a usable primary number).

## SCOPE NOTE (read first)

Share India runs two structurally different income engines (B04-bizmodel):
1. **CLIENT POOL** — brokerage/fee income, MTF and NBFC lending interest, wealth/PMS/AIF fees, insurance broking commission, merchant banking fees, algo-platform (uTrade) subscriptions. This is a conventional demand-side market: it grows with client count, AUM, and penetration, and a competitor can take share from it.
2. **PROP POOL** — net gain on fair value changes (58.3% of FY26 consol income, Note 31, B04), trading-inventory turnover (9.2%) and portfolio dividend yield (1.1%). This is not a customer-demand market. It is Share India's slice of a zero-sum trading/arbitrage pool that scales with market volatility, exchange turnover and the firm's own risk capital, not with "market share" in the TAM/SAM/SOM sense. B04 flagged this line as having no volume x price unit economics (FLAG-NO-CLEAN-UNIT).

Per the injected instruction, the two pools are sized separately. **The formal TAM/SAM/SOM/YAML numbers in this report cover the CLIENT POOL only** (≈30.1% of FY26 consol revenue, Rs 442 Cr — see Section 1A). The PROP POOL is discussed narratively in Section 2B with sourced anchors but is NOT converted into a TAM/SAM/SOM figure; manufacturing a Rs Cr "market size" for a trading position would misstate what the number means. Stage 11 must not apply the SOM-implied CAGR in this report to Share India's total consolidated revenue (Rs 1,470 Cr, prop-inclusive) — it applies only to the client-annuity revenue base named above.

---

## SECTION 1: MARKET DEFINITION

### 1A. Precise boundaries — CLIENT POOL

- **Product scope**: retail/HNI/institutional broking (cash, F&O, currency, commodity execution fees); Margin Trading Facility (MTF) and NBFC-book lending interest; Portfolio Management Services (PMS) and Alternative Investment Fund (AIF) fees; wealth/debt distribution (Share India Wealth Multiplier, Share India Cred); insurance broking commission; mutual fund distribution commission; merchant banking (IPO/DRHP) fees; algo-trading platform (uTrade/Algowire) subscriptions.
- **Geographic scope**: India only (domestic capital markets and NBFC lending). No global segment claimed anywhere in the corpus.
- **Customer scope**: retail investors, HNI/UHNI, corporates, institutional clients — the full spectrum SEBI-registered intermediaries serve. Excludes clients Share India cannot legally or operationally reach (e.g., pure institutional prime-broking mandates it does not hold).
- **Channel scope**: branch network (95 own branches + franchises, 13 states, AR FY26 p.73) plus digital/app-based execution and uTrade algo delivery.
- **Price segment**: full-service-plus-algo positioning (AR: "leads in algo-trading solutions for domestic and international high-net-worth clients"), not the pure zero/near-zero-brokerage discount segment (Zerodha/Groww/Upstox model).
- **Explicit exclusions**: mutual fund AMC manufacturing economics (only distribution commission counted); insurance underwriting risk (only broking commission counted); the PROP POOL (Section 2B); any revenue Share India might earn outside India (none disclosed).

FY26 consol revenue split (Note 31/28/30/32/33/29, B04): net gain on fair value changes 58.3%, interest income 18.4%, fees and commission 11.1%, sale of products (trading inventory) 9.2%, dividend income 1.1%, sale of services 0.6%. **CLIENT POOL revenue = interest income + fees and commission + sale of services = 18.4% + 11.1% + 0.6% = 30.1% of Rs 1,470 Cr = Rs 442 Cr (FY26 consol)** (arithmetic shown; source AR FY26 P&L notes, B04-bizmodel.yaml). Interest income (18.4%) is not MTF-only — it also includes NBFC book and deposit interest (B04, "undifferentiated in this note") — treated here as client-pool because none of it is prop-trading income.

### 1B. Management's own TAM claim

No document in the corpus (AR MD&A Annexure-3, three investor presentations) states a numeric TAM for Share India's own addressable market. Management's claims are qualitative narrative:
- "financialization of savings, rising retail participation, digital adoption and continued growth in Indian capital markets to create significant long-term opportunities" (AR FY26 MD&A "Going Forward", p.75).
- Investor presentation (20-Mar-2026, p.17-19, sourced SEBI/Economic Times/Indiagraphs/Knightfrank/Deloitte/IRDAI/AMFI/CRISIL Intelligence/IBEF): India's IPO pipeline "249 filings for 2026, ~Rs 4 lakh crore proposed fundraising"; Indian wealth management market "USD 1,100 Bn (FY24) to USD 2,300 Bn (FY29P)"; mutual fund industry AUM projection; India to become world's 4th-largest private wealth market by 2028.

**Credibility read: BROAD.** These are sector-level backdrop statistics sourced to third-party research houses, not a company-specific TAM claim with a stated definition. There is no number to compare against a conservative estimate (mgmt_claim_cr = 0, ratio not computable — see YAML).

---

## SECTION 2: TAM ESTIMATION — CLIENT POOL

### Method 1 — Top-down (industry revenue, historical anchor)

ICRA reported the Indian securities broking industry on track for "a record Rs 28,000 crore revenue" in FY22 (Zeebiz, citing ICRA, 2022). **STALE — this is a FY22 figure, >4 years old at run date; per the staleness rule it informs direction only, never the headline number.** ICRA's subsequent notes ("Securities Broking Industry, May 2025 — Regulatory tightening reduces..."; "Securities Broking & Allied Industry, November 2025") were not machine-readable via web fetch (PDF binary/image content) — a corroborating current industry-revenue figure was **NOT FOUND**. A related, dated data point: ICRA's sample of nine listed securities-broking firms showed net revenue down 19% YoY and profitability at a 12-quarter low amid the FY25 F&O regulatory tightening (Business Standard, 17-Apr-2025 citing ICRA) — directionally useful (not stale, <2 yrs old) but not a Rs Cr total. Confidence: L (direction only).

### Method 2 — Bottom-up (Share India's own unit economics, scaled)

Addressable unit: one broking client. Share India standalone had 47,253 broking clients and 186 institutional clients as of Mar-2026 (AR FY26 p.73). Fees-and-commission revenue (the clean, prop-free fee line) was 11.1% of Rs 1,470 Cr consol = Rs 163 Cr FY26. Revenue per broking client ≈ Rs 163 Cr ÷ 47,253 ≈ **Rs 34,500/client/year** (arithmetic shown; ignores the institutional skew, so this is an upper-bound per-retail-client estimate).

Scaling this ARPU across NSE's unique registered investor base (>13 Cr, AR FY26 p.73) gives a mechanical TAM of ~Rs 4.5 lakh Cr. **This number is flagged as NOT REALISTIC and excluded from the triangulation table.** Share India's client mix skews HNI/UHNI/institutional/algo-trader (AR's own "Competitive Advantage" section); the ~13 Cr registered-investor population is overwhelmingly served by near-zero-brokerage discount platforms (Zerodha, Groww, Upstox) whose ARPU is an order of magnitude lower. Extrapolating a boutique full-service ARPU across the mass-market population would badly overstate the pool. Shown here for the "show every calculation" requirement, not used as an input.

### Method 3 — Peer revenue aggregation (primary method, current)

Sum of known organized players' FY26 total revenue (a reasonable CLIENT POOL proxy for five of the six names — only Share India itself runs a prop-trading-dominated mix; the other five are predominantly client-facing):

| Player | FY26 revenue (Rs Cr) | Source |
|---|---|---|
| Zerodha | ~8,500 | thehawk.in / Inc42, 2026 (FY26 revenue flat vs FY25's Rs 8,847 Cr per company filings reported in press) |
| Angel One | 5,138 | screener consol P&L CSV, Mar-2026 column |
| Groww | ~3,531 (extrapolated) | FY25 actual Rs 3,901 Cr (Inc42, 2026) less ~9.5% YoY per Q1/Q2 FY26 declines (Business Standard, Nov-2025) |
| SMC Global | 1,878 | screener consol P&L CSV, Mar-2026 column |
| Share India | 1,470 | screener consol P&L CSV, Mar-2026 column (matches AR Rs 1,470.26 Cr) |
| Choice International | 1,119 | screener consol P&L CSV, Mar-2026 column |
| **Sum (known 6 players)** | **≈ Rs 21,600 Cr** | — |

This is explicitly a **floor, not the full industry**: it excludes ICICI Securities, HDFC Securities, Kotak Securities, Motilal Oswal, 5paisa, Paytm Money, IIFL Securities and the long tail of ~300 other SEBI-registered brokers. No aggregated FY26 total for the full organized industry was found (input gap, named below). Confidence: M (current, directly sourced, but a known undercount).

### Method 4 — Import substitution

Not applicable. Domestic financial-services intermediation has no import/domestic-production/consumption structure.

### Method 5 — Global benchmark (light cross-check only)

India's total market capitalisation was USD 4.5 trillion in FY26 (AR MD&A p.73, sourced IMF/TOI/Moneycontrol). At the Method 3 floor of Rs 21,600 Cr (~USD 2.6 Bn at ~Rs83/USD), the implied brokerage-and-allied-revenue-to-market-cap ratio is ~0.07%, broadly the same order of magnitude as mature-market online-brokerage revenue-to-market-cap ratios (a rough sanity check, not a precision benchmark — confidence L). This does not contradict Method 3's floor being too low or too high; it only says the floor is not implausible at India's current market-cap scale.

### Triangulation table

| Method | Estimate (Rs Cr) | Confidence | Staleness |
|---|---|---|---|
| 1. Top-down (ICRA industry) | 28,000 (FY22 base) | L | **STALE** (>4 yrs; direction only) |
| 2. Bottom-up (company ARPU scaled) | ~4,48,500 | L, **excluded** | current but non-representative (see caveat) |
| 3. Peer aggregation (known 6) | 21,600 | M | current (FY26) |
| 4. Import substitution | N/A | — | — |
| 5. Global benchmark | order-of-magnitude consistent with 3 | L | current |

**Conservative estimate: Rs 21,600 Cr** (Method 3 floor, most current and directly sourced).
**Realistic estimate: Rs 30,000 Cr** (judgment band Rs 28,000–35,000 Cr, midpoint; brackets the Method 1 historical anchor — scaled up for the account-growth and revenue growth the industry has seen since FY22 — against the known Method 3 floor, with an allowance for the large unlisted/listed full-service houses not summed. **Flagged L confidence**; a full current industry total was not found.)

Management claim vs conservative estimate: **not computable** — management stated no number (mgmt_claim_cr = 0). Ratio and the standard >2x/within 1.5x/below read do not apply; recorded as "no explicit claim."

### SECTION 2B — PROP POOL (narrative, not TAM-sized)

The prop-trading line cannot be sized the way a demand market is sized because it is Share India's slice of a competitive, zero-sum trading pool bounded by capital and regulation, not by customer count. Sourced anchors, for context only:

- India's total options premium turnover was USD 1,909 Bn in CY2025, down 15% from USD 2,247 Bn in CY2024 (web search, FIA-linked data via businesstoday.in, 2026) — the scale of the pool prop/market-making desks compete over.
- Options premium average daily turnover initially fell 17.4% after the FY25 regulatory changes, then recovered 38% to ~Rs 81,696 Cr/day in H2 FY26 (web search, market-data aggregator citing NSE/SEBI figures, 2026 — **primary NSE/SEBI source PENDING LIVE VERIFICATION**, named not fabricated).
- Active derivatives traders fell 18% YoY to 87.5 lakh in FY26, from 106.2 lakh in FY25 — the first annual contraction in a decade (Business Standard, 20-Aug-2026, citing a SEBI study). Shrinking retail flow is a structural headwind to arbitrage/liquidity-provision revenue, since retail order flow is what liquidity providers trade against.
- Management's own estimate: "around INR 40,000 to INR 50,000 crores worth of capital will be taken out from the market" industry-wide because of the RBI intraday-funding curb effective ~1-Jul-2026 (Q4 FY26 concall, 23-May-2026, quote, B05). This is the single most concrete industry-scale figure for the capital base competing in this pool, though it is a management forecast, not a filed/regulator number.
- Share India's own segment assets (all segments combined) were Rs 4,589.86 Cr consol (Note 45, AR p.286, per B04) — a rough proxy for the capital base the company itself deploys across trading and lending books; the AR does not disaggregate a prop-trading-only capital figure.

No bps-level arbitrage/market-making margin-capture rate was found in any primary source, so no Rs Cr "prop TAM" is manufactured from the turnover figures above. **capacity_check and all downstream YAML fields (SAM/SOM/runway) in this report apply to the CLIENT POOL only.**

---

## SECTION 3: SAM & SOM (CLIENT POOL)

### 3A. SAM — five filters applied to the conservative TAM (Rs 21,600 Cr)

These are analyst-judgment cuts with the reasoning shown, not independently sourced per-filter percentages — flagged as such.

| Filter | Retained % | Reasoning |
|---|---|---|
| Product fit | 90% | Share India's product suite (broking, MTF, NBFC lending, PMS/AIF, insurance broking, merchant banking, algo platform) matches most of what the peer basket collectively covers; small cut for AMC-manufacturing-adjacent scope Share India does not hold. |
| Geography | 65% | Own-branch presence in 13 of ~28 states/UTs (AR p.73); digital reach is national but branch-led acquisition (the growth engine per B05) is not. |
| Channel | 75% | Hybrid full-service + digital model reaches fewer price-sensitive, app-only users than a pure-discount platform. |
| Customer segment | 55% | Own positioning skews HNI/UHNI/institutional/algo-trader (AR "Competitive Advantage" section); the mass discount-broker retail segment (Zerodha/Groww/Upstox users) is largely out of reach on cost structure. |
| Capability | 70% | NBFC book (Rs 265 Cr, AR p.74) is tiny against the Rs 1.49–1.54 lakh Cr industry MTF book (Business Standard/BusinessToday, Sep-2026); merchant banking is SME-weighted (22 SME IPOs to date, 1 mainboard DRHP filed, AR p.75) — capability constrains how much of the filtered pool is truly reachable near-term. |

Composite: 0.90 x 0.65 x 0.75 x 0.55 x 0.70 = **16.9%**.
**SAM = Rs 21,600 Cr x 16.9% ≈ Rs 3,650 Cr.**

### 3B. SOM at 3 and 5 years

Current SAM share = client-pool revenue (Rs 442 Cr) ÷ SAM (Rs 3,650 Cr) = **12.1%** (current_sam_share_pct = 12).

Share-gain assumption: B05's credibility grade is C (mixed promise-delivery: 5 delivered / 3 partial / 2 missed across three quarters) and B07 found NO MEANINGFUL EMERGING MOAT (em_score ~10). This does not support the "aggressive" 3-5pp band; the "normal" 1-2pp (3yr) band is used, with the low end of "aggressive" allowed at 5yr given the branch-rollout and MTF-doubling plans are real, sourced commitments (B05 guidance), not aspiration only.

- SAM at yr3 (TAM growth 15%/yr, see Section 4A): Rs 3,650 Cr x (1.15)^3 = **Rs 5,551 Cr**.
  SOM_3yr = Rs 5,551 Cr x 13.5% (12.1% current + 1.4pp gain) = **Rs 749 Cr**.
  Implied CAGR on the client-pool revenue base: (749/442)^(1/3) − 1 = **19.2%**.
- SAM at yr5: Rs 3,650 Cr x (1.15)^5 = **Rs 7,342 Cr**.
  SOM_5yr = Rs 7,342 Cr x 15.0% (12.1% current + 2.9pp gain) = **Rs 1,101 Cr**.
  Implied CAGR: (1,101/442)^(1/5) − 1 = **20.0%**.

**These CAGRs apply to the Rs 442 Cr client-pool revenue base only — not to Share India's Rs 1,470 Cr total consol revenue, 58.3% of which is the unforecastable prop line (Section 2B).** Coincidentally, management's own "~20% group revenue growth" guidance for FY27 (Q1 FY27 concall, B05) sits close to this range, but the two are not the same base — the convergence is noted, not treated as confirmation.

### 3C. Capacity cross-check

B07's capex_embedded_growth_pct = 0/NOT APPLICABLE — no capex programme exists to check the SOM against (B07-emoat.yaml, Section 2C). The only capacity proxies are qualitative and company-stated:
- Branch rollout: 25-30 branches over 2 years (B05, Q1 FY27 guidance), each targeted at Rs 15 Cr MTF in 8 months.
- MTF book target: Rs 900-1,000 Cr in 2 years from a base of ~Rs 470 Cr (Jun-2026) (B05) — an incremental Rs 430-530 Cr book. At the disclosed industry MTF rate range (9.5%-18% p.a., midpoint 13.5%; comparison-site data, 2026), this implies **~Rs 58-72 Cr of incremental annual interest revenue** from the branch/MTF plan alone, roughly consistent in direction with the SOM_3yr arithmetic above.

**capacity_check = "sufficient in principle, gap not in Rs Cr."** Share India's standalone net worth of Rs 2,187.26 Cr (AR p.74) gives balance-sheet headroom to fund the MTF/NBFC growth plan. The real constraint is **funding quality, not physical capacity**: CFO has been negative 3 of the last 4 years (B04/B07) and the MTF/NBFC book growth is debt-funded, not retained-earnings-funded. The Sep-2026 Infomerics downgrade to ISSUER NOT COOPERATING (B00 LBF4) and the adjourned NCD holders' meeting are live constraints on that debt-funded growth precisely when the SOM plan assumes uninterrupted access to it. **The SOM, not the branch/MTF plan, is the side more likely to prove optimistic if debt access tightens further.**

---

## SECTION 4: GROWTH DRIVERS, RISKS & STRUCTURE (CLIENT POOL)

### 4A. TAM growth drivers

| Driver | Impact | Evidence |
|---|---|---|
| Penetration / financialization of savings | High | Demat accounts 22.45 Cr Mar-2026 (AR p.73, NSDL/CDSL); still growing, though net additions fell ~21% YoY to 3.29 Cr in FY26 — deceleration, not reversal. |
| Formalization | Medium | AR MD&A names "Industry Consolidation Prospects" — stricter regulation and compliance cost is pushing smaller/unorganized players toward exit or merger. |
| Regulatory tailwind (algo) | Medium | SEBI's formal retail-algo-trading framework (broker oversight, unique algo ID) is cited by the AR as expected to widen adoption of regulated algo trading (AR p.72), a direct tailwind for uTrade. |
| Wealth/AUM growth | High | Mutual fund AUM crossed Rs 73 lakh Cr Mar-2026 (AMFI-CRISIL Factbook 2026, Aug-2026) and is projected at 16-18% CAGR (Share India investor presentation, Mar-2026, sourced CRISIL); Indian wealth-management market projected USD 1,100 Bn (FY24) to USD 2,300 Bn (FY29P), a 15.9% CAGR (same presentation) — independent triangulation converges near mid-teens %. |
| NBFC/lending growth | Medium-High | Retail NBFC AUM (ex-HFC) estimated to grow 16-18% in FY27 (AR MD&A p.72, sourced ICRA April 2026). |
| Geographic expansion | Medium | Tier-2/3 branch rollout (AR p.75; B05 guidance) targets underpenetrated cities specifically. |
| Technology enablement | Medium | uTrade crossed 71,062 total / 5,000+ paid subscriptions (AR p.76); financial materiality still unquantified (B07 gap). |
| Demographics | Medium | AR cites "expansion into non-metro cities... unlocking a large untapped pool of savings" (investor presentation, Mar-2026). |

Blended TAM growth estimate used in Section 3B: **15%** (rounding the 15.9% wealth-market CAGR and the 16-18% NBFC/MF AUM growth figures, all independently sourced and converging in the mid-teens).

### 4B. TAM risks

| Risk | Monitoring signal |
|---|---|
| Regulatory headwind (SEBI F&O curbs) | Active derivatives traders (SEBI monthly bulletin); index options volumes down 52% FY26 per SEBI annual report (web search, 2026) — a structural, not cyclical, ceiling on the F&O-linked slice of client revenue (brokerage on derivatives). |
| RBI intraday-funding curb | Bank-guarantee/limit utilisation disclosures; management's own Rs 40,000-50,000 Cr capital-exit estimate (B05). |
| Price competition (MTF rate wars) | MTF interest rates now advertised as low as 5.99%-6% p.a. by some discount brokers (web search, 2026) against Share India's presumed full-service pricing (rate itself NOT FOUND in AR/presentation, per B04 gap) — a live yield-compression risk on the largest CLIENT POOL growth lever. |
| Substitution (discount brokers) | Zerodha/Groww/Upstox continuing to take demat-account share at near-zero brokerage; AR MD&A names "changing client preferences towards passive strategies and online platforms" as a threat (p.73). |
| Cyclical downturn / FPI outflows | FPI cumulative equity outflows >Rs 2.2 lakh Cr CY2026-to-date (AR p.73) — a market-sentiment risk to both brokerage volumes and wealth-AUM flows. |
| Saturation in Tier-1 cities | Implicit in the AR's own Tier-2/3 branch strategy — Tier-1 broking penetration is already high. |

### 4C. Market structure

- Competitor count: ~300 SEBI-registered stockbrokers (industry knowledge; exact current count NOT FOUND in this corpus/search), heavily concentrated at the top.
- Top-3 concentration: not independently computed here (a full industry revenue total was not found — see Method 3 gap), but the known Zerodha + Groww + Angel One trio alone summed to ~Rs 17,169 Cr of the Rs 21,600 Cr known-6 floor (≈79% of that floor), indicating heavy concentration among the largest digital-first platforms.
- Organized vs unorganized: broking/DP activity is fully SEBI-licensed by definition (no meaningful "unorganized" broking segment in the informal sense used for goods industries); the more relevant split is digital-discount vs full-service, not organized vs unorganized.
- Consolidating: AR MD&A explicitly names "Industry Consolidation Prospects" amid stricter compliance demands (p.73).
- Price vs differentiation: brokerage and MTF pricing are racing toward zero/near-zero at the discount end; Share India competes on algo/tech and wealth-service differentiation rather than price (AR "Competitive Advantage" section).
- Entries/exits: no specific FY26 entry/exit data found; qualitative narrative only (industry consolidation).
- Import share trend: not applicable (domestic-only market).

---

## SECTION 5: SUMMARY & RUNWAY (CLIENT POOL)

### 5A. Funnel

```
TAM (conservative, Method 3 floor)      Rs 21,600 Cr
  -> SAM (16.9% of TAM, five filters)    Rs  3,650 Cr
      -> current share (12.1%)          Rs    442 Cr  (= FY26 client-pool revenue)
      -> SOM 3yr (13.5% of SAM_yr3)      Rs    749 Cr  (19.2% implied CAGR)
      -> SOM 5yr (15.0% of SAM_yr5)      Rs  1,101 Cr  (20.0% implied CAGR)
```

### 5B. Runway assessment

- Revenue headroom = SAM ÷ current client-pool revenue = Rs 3,650 Cr ÷ Rs 442 Cr = **8.3x**.
- TAM growth rate: **~15%/yr** (Section 4A).
- Company CAGR vs TAM: Share India's FY26 client-pool revenue (Rs 442 Cr) cannot be trended against a single prior-year client-pool figure in this corpus (the FY25 revenue-line split by prop/client is not separately available at this granularity — B04 gap). Directionally, fees and commission income *fell* 12.7%/18.6% (standalone/consol) in FY26 even as the AR claims a client-led shift (B04 FLAG-DISCLOSURE-CONTRADICTION) — i.e., on the one clean line available, the company is currently **losing ground within its own client pool**, not riding or beating market growth.
- Years to saturate SAM at the SOM_5yr trajectory: at ~20% CAGR the client-pool revenue base would need roughly 9-10 more years beyond yr5 to reach the (still-growing) SAM — saturation is not a near-term concern.

### 5C. Runway classification

Using the bands 8.3x headroom + ~15% TAM growth → **STRONG** (self-defined bands, stated for transparency since no fixed matrix was provided in this run's inputs: MASSIVE = headroom >15x and TAM growth >20%; STRONG = 7-15x and 12-20%; GOOD = 3-7x and 8-12%; MODERATE = 1.5-3x and 5-8%; LIMITED = below both). The classification applies to the CLIENT POOL only; it says nothing about the prop-trading 58.3% of today's actual revenue, which is capital- and volatility-bound, not runway-bound.

### 5D. SAM expansion levers actually being pursued

| Lever | Status | Potential addition |
|---|---|---|
| Silverleaf merger | NCLT-approved 20-Aug-2026 (B07) | ~Rs 50-60 Cr revenue (B05 trigger #5) |
| Branch/MTF rollout (25-30 branches) | Active, guided (B05) | ~Rs 58-72 Cr incremental annual interest revenue (Section 3C arithmetic) |
| Category III AIF launch | Slipped once, now guided Q3 FY27 (B05) | Unquantified — fee rate on AIF/PMS AUM NOT FOUND |
| uTrade algo monetization | 71,062 subscriptions, 5,000+ paid (AR p.76) | Unquantified — Rs-terms revenue for uTrade NOT FOUND anywhere in the AR (B07 gap) |
| GIFT City/IFSC | Currently loss-making (B04/B07) | Not yet a positive lever |

Revised run-rate if Silverleaf and the branch/MTF plan both land at their midpoints: Rs 442 Cr + Rs 55 Cr + Rs 65 Cr ≈ Rs 562 Cr, which would move current_sam_share_pct to ~15.4% and headroom to ~6.5x — still within the STRONG band, not a step-change.

### 5E. Final output card

- TAM (client pool): conservative Rs 21,600 Cr, realistic Rs 30,000 Cr.
- SAM: Rs 3,650 Cr (16.9% of conservative TAM).
- SOM: Rs 749 Cr (3yr) / Rs 1,101 Cr (5yr).
- Revenue headroom: 8.3x. TAM growth: ~15%/yr. Runway: STRONG (client pool only).
- **Valuation implication line**: "At 19-20% revenue CAGR implied by SOM for the client-annuity revenue lines only (fees, MTF/NBFC interest, wealth/insurance/merchant-banking; excludes the prop-trading book, which is 58.3% of FY26 income and not forecastable by this method, per B04/B07), and a stated PAT-margin guideline of ~22% (+/-2%, B05), this slice alone — roughly 30% of today's earnings base — could plausibly compound at that pace. It does **not**, by itself, support or refute Share India's current P/E of ~15.4x (CMP Rs 228.0, market cap Rs 4,992 Cr, screener 18-Sep-2026 close; FY26 consol PAT Rs 324.44 Cr, AR p.77), because the dominant swing factor for total-company EPS remains the prop-trading line this method cannot size."

---

## SECTION 6: DOWNSTREAM SIGNAL CANDIDATES

| # | Candidate Signal | Entity Type | Why It Drives Demand | Likely Primary Source | Expected Cadence |
|---|---|---|---|---|---|
| 1 | NSE/BSE monthly cash and F&O average daily turnover (ADTO) and options premium turnover | Macro | Drives prop-trading revenue, brokerage volumes and MTF utilisation simultaneously — the single most load-bearing external number for this name | NSE/BSE monthly business-growth bulletins | Monthly (SHARED) |
| 2 | SEBI active-derivatives-trader count and F&O regulatory circulars (contract size, expiry rationalisation) | Regulatory | Sets the structural ceiling on retail options volumes that both brokerage fees and the prop pool depend on | SEBI monthly bulletin / SEBI board circulars | Monthly / event-driven (SHARED) |
| 3 | RBI intraday-funding and bank-guarantee circular status/implementation | Regulatory | Directly caps the capital available to Share India's prop/liquidity-provision desk (management's own Rs 40,000-50,000 Cr industry estimate, B05) | RBI notifications/circulars | Event-driven |
| 4 | NSDL/CDSL total demat-account additions | End-customer | Direct proxy for the addressable client-pool population growth or deceleration | NSDL/CDSL monthly investor-data releases | Monthly (SHARED) |
| 5 | AMFI mutual-fund AUM and monthly SIP flow data | End-customer | Drives the wealth/PMS/AIF and mutual-fund-distribution segments' addressable pool | AMFI monthly data release | Monthly |
| 6 | Peer-disclosed MTF book size and MTF interest-rate changes | Counterparty | Signals industry-wide MTF yield compression risk, the largest quantified SAM-expansion lever for this name | NSE/BSE MTF disclosure data; peer investor presentations | Monthly |
| 7 | Infomerics/rating-agency cooperation status | Counterparty | Debt-funded growth capacity (Section 3C) depends on this; already a live stress event (Sep-2026 ISSUER NOT COOPERATING) | Infomerics rating rationale (Reg 30 filings) | Event-driven |
| 8 | SEBI DRHP filings / SME-platform IPO listing counts | End-customer | Drives merchant-banking fee revenue (22 SME IPOs to date, 1 mainboard DRHP filed, AR p.75) | SEBI DRHP filings; NSE/BSE SME platform listing data | Quarterly / event-driven |

demand_externally_verifiable: true (8 rows found, above the 3-row minimum).

---

## Search log

**Searches performed**: India stock broking industry revenue size 2026 (CRISIL/ICRA); India MTF industry book size 2026; SEBI F&O derivatives options premium turnover decline 2025-2026; India algo trading software market size 2026; ICRA securities broking industry revenue FY26/FY27 estimate; India wealth management AUM market size 2026 (CRISIL); NSE active derivatives traders 2026 / premium turnover; Zerodha revenue FY25/FY26; Groww revenue FY25/FY26; MTF interest rate range charged by Indian brokers 2026; ICRA "regulatory tightening" broking industry revenue FY26. Two WebFetch attempts on ICRA's May-2025 and November-2025 broking-industry PDF reports (both returned unparseable binary/image content, not usable text).

**Searches skipped**: none deliberately skipped; all planned search categories were executed. Some specific figures (full FY26 organized-industry revenue total; per-broker prop/arbitrage margin bps; exact SEBI-registered broker count) were searched for but **NOT FOUND** — named as input gaps, not as skips.

---

## Input gaps

- Exact FY26 total organized Indian broking-industry revenue (all ~300 SEBI-registered brokers) NOT FOUND; ICRA's proprietary reports were not machine-readable via web fetch. The Method 3 peer sum (Rs 21,600 Cr) is a known floor, not a verified total.
- Groww's FY26 full-year revenue was not yet reported at run date; extrapolated from FY25 actual and Q1/Q2 FY26 YoY declines (flagged as an extrapolation, not a filed figure).
- No bps-level bid-ask/arbitrage margin-capture rate for Indian equity-derivatives liquidity providers found in any primary source; this is why Section 2B (PROP POOL) stays narrative-only rather than producing a Rs Cr figure.
- MTF industry-wide average yield is not a single disclosed figure; the 9.5%-18% p.a. range used in Section 3C comes from broker-comparison websites (2026), not a regulator or primary filing.
- Share India's own per-trade brokerage rate and MTF interest rate remain NOT FOUND in the AR or presentations (confirms B04 gap), so Method 2's Rs 34,500/client ARPU is a fees-only proxy, not a full per-client revenue figure.

---

## Flags

- FLAG: the SOM-implied revenue CAGR (19.2% yr3 / 20.0% yr5) in this report applies **only** to the Rs 442 Cr client-annuity revenue base (fees, interest, services), not to Share India's Rs 1,470 Cr total consolidated revenue. Stage 11 must not apply this CAGR to total-company revenue without separately addressing the prop-trading line (58.3% of FY26 income), which this method does not and cannot forecast.
- FLAG: the "realistic" TAM estimate (Rs 30,000 Cr) carries low confidence — a full current organized-industry revenue total was not found despite multiple targeted searches; treat the Rs 21,600 Cr Method 3 floor as the more defensible number for any downstream arithmetic.
- FLAG: Section 3A's five SAM filter percentages are analyst-judgment calls with reasoning shown, not independently sourced per-filter data points; they are transparent, not precision-measured.
- FLAG: on the one clean, filed year-over-year signal available for the client pool (fees and commission income), the company is currently *losing* ground (-12.7%/-18.6% standalone/consol, FY26, B04) even as this report's SOM math assumes 1.4-2.9pp of share GAIN over the next 3-5 years. The SOM should be read as what the branch/MTF/AIF plan could deliver if it works, not as an extrapolation of the trend actually observed to date.
