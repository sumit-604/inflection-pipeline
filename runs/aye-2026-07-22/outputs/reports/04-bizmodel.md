# STAGE 4: BUSINESS MODEL DECODER — Aye Finance Limited (AYE)
Run date: 2026-07-22 | Model: Sonnet 5 | Pipeline mode, `full` run

LENDER ADAPTATION NOTE: AYE is a balance-sheet NBFC-ML lender, not a manufacturer or
services company. This report substitutes lender-appropriate frameworks throughout:
funding/ALM intensity instead of working-capital intensity, yield/NIM/spread instead
of gross margin, and P/B-led valuation instead of EV/EBITDA. Every substitution is
named at point of use.

Sources used: IPO Prospectus (AR, 614 pages, page numbers below refer to the printed
page number shown in the extract, e.g. "AR p.218" = prospectus page 218), Q1FY27
Investor Presentation (slide numbers as printed), FY26 audited results filing (Reg 33/52,
"Results FY26"), and the operator digest (NON-ANCHORED, labelled digest-only wherever used).

---

## SECTION 1: THE BUSINESS MODEL IN PLAIN ENGLISH

### 1A. One-line description
Aye Finance lends small amounts of money to India's smallest businesses (shopkeepers,
tailors, workshop owners) who banks won't touch because they have no paperwork, using
a proprietary "know-the-trade" credit system instead of financial statements, and it
makes its profit on the spread between what it pays to borrow and what it charges
these borrowers (AR p.218-219, "OUR BUSINESS — Overview").

### 1B. Money flow chain for each revenue stream

**Stream 1 — Interest income on loans held on book (the core engine)**
[Aye raises money from banks/DFIs/bond investors] → [Aye lends it in small chunks,
avg ticket ~Rs1.5-4.9 lakh, to micro-enterprises for working capital/asset purchase,
underwritten via 70+ "business cluster" models] → [Aye disburses cash and collects
monthly EMIs via NACH/digital + field officers] → [the micro-enterprise borrower
pays] → [borrower pays via NACH auto-debit, 85.97% of collections through digital
modes (Inv. Pres. slide 27)]. FY26: interest income Rs1,557.43cr, 83.6% of total
income (Results FY26 p.6, computed: 1,557.43/1,863.24).

**Stream 2 — Fees and commission income**
[Same loan] → [Aye charges servicing fee, application fee, delay payment/registration
charges at origination and during the loan's life] → [borrower pays as part of/on top
of EMI] (AR p.427, "Fees and commission income: comprises servicing fee, application
fee, delay payment charges, registration charges"). FY26: Rs73.54cr, 3.95% of total
income (Results FY26 p.6).

**Stream 3 — Net gain on derecognition of financial instruments (securitisation /
direct assignment — the "sell-down" engine)**
[Aye originates and seasons a pool of loans on its own book] → [Aye sells a pool to a
bank/DFI via direct assignment or securitisation, meeting Ind AS 109 derecognition
criteria] → [Aye records the present value of the future excess interest spread on
that pool as an upfront gain, and retains a servicing/collection role] → [buyer pays
Aye a purchase consideration; Aye retains a small MRR (minimum retention
requirement)] (AR p.428, "Net gain / (loss) on derecognition... generated through
direct assignment transactions... Income from assignment transactions, i.e. present
value of excess interest spread is recognized"). FY26: Rs67.97cr, 3.65% of total
income, UP from 2.50% in FY25 (Rs37.59cr/Rs1,504.99cr) and 1.94% in FY23 — a rising
share of profit, consistent with B02/B03's finding that this line is growing
(Results FY26 p.6; AR p.240, "Net gain on derecognition... increased by 98.40%... in
Fiscal 2025... primarily because of a higher volume of direct assignment
transactions"). This is a NON-cash, one-time-per-pool gain booked upfront — a flag
for earnings quality (see 4A).

**Stream 4 — Net gain on fair value changes (treasury / hedging, non-core)**
[Aye holds mutual funds for liquidity and cross-currency swaps to hedge ECB
borrowings] → [MTM movements and gains on sale generate P&L gains] → [booked as
revenue] (AR p.428). FY26: Rs105.79cr, 5.68% of total income (Results FY26 p.6) — this
is the largest non-interest line and is market-driven, not operating income; treat as
low-quality/volatile.

**Stream 5 — Other income (non-operating)**
Profit on sale of assets, early lease termination, misc/tax-refund interest (AR
p.430-431). FY26: Rs48.51cr, 2.60% of total income (Results FY26 p.6).

### 1C. Revenue model classification table

| Stream | Type | % of FY26 total income (anchored) | Predictability |
|---|---|---|---|
| Interest income on loans | Recurring, spread-based (yield less cost of funds) | 83.6% (Rs1,557.43cr / Rs1,863.24cr, Results FY26 p.6) | High (H) — contractual EMIs, but subject to credit losses |
| Fees and commission income | Recurring, transaction-linked | 3.95% (Rs73.54cr, Results FY26 p.6) | High (H) |
| Net gain on derecognition (securitisation/DA) | Episodic, deal-driven, upfront non-cash gain | 3.65% (Rs67.97cr, Results FY26 p.6), up from 1.94% in FY23 | Low (L) — depends on buyer appetite and deal timing, not repeatable without fresh pool sales |
| Net gain on fair value changes | Market/treasury-driven | 5.68% (Rs105.79cr, Results FY26 p.6) | Low (L) — FX/MTM swings |
| Other income | Non-operating, incidental | 2.60% (Rs48.51cr, Results FY26 p.6) | Low (L) |

### 1D. Simplified business model canvas

| Element | Answer for AYE |
|---|---|
| What they sell | Small business loans (secured hypothecation, unsecured hypothecation, mortgage/LAP, Saral property loans) (AR p.222, product table) |
| Who buys | Micro-scale MSMEs, turnover Rs20 lakh-1 crore, no formal financial documentation, Tier 2/3 towns (AR p.221-222; Inv. Pres. slide 12) |
| Why them (not a bank) | Bank/DFI-grade cost of funds (~10.2-10.8% incremental, Inv. Pres. slide 18) combined with a proprietary 70+ cluster underwriting model that substitutes for financial statements banks require (AR p.223, 228-229) |
| How delivered | 571-branch "phygital" network: branch-based sourcing + AI/ML underwriting/collections (Inv. Pres. slide 10-11; AR p.223-224) |
| Cost structure dominance | Finance cost (interest paid to lenders) + credit cost (provisions) + employee cost dominate; FY26 finance cost Rs534cr (28.6% of total income), impairment Rs336cr (18.0%), employee cost Rs494cr (26.5%) (Results FY26 p.6) |
| Scarce resource | Underwriting IP (70+ business-cluster cash-flow models) and 12+ years of granular repayment-behaviour data — not easily replicated (AR p.229-230, "considerable investment of time and resources... competitive edge") |
| Pricing power source | Weak/moderate — average yield 21.95% FY26 on ATA (Inv. Pres. slide 8, 37), set by risk-based pricing within an RBI-monitored ceiling (up to 26-32% PA by product, AR p.222) and competitive pressure from Five-Star, SBFC, Veritas etc.; NOT gross margin — see 1A/2A framing |
| Asset intensity | Financial-asset heavy (loan book is the asset), not fixed-asset heavy — Loans Rs6,266cr of Rs7,773cr total assets, 80.6% (Results FY26 p.5) |
| WC intensity | NOT APPLICABLE — a lender has no inventory/receivables/payables cycle in the manufacturing sense. Substitute metric: funding/ALM intensity — see 3A/3B. As of Jun-26 cumulative ALM is positive in every bucket out to 5 years (Inv. Pres. slide 20) |
| Regulatory moat or burden | Both — RBI NBFC-ML registration (certificate of registration, AR p.223,17371) is a genuine entry barrier (capital, compliance, RBI inspection) but also imposes CRAR, exposure and provisioning constraints that cap leverage and growth speed (AR p.3621, "subject to periodic inspections by the Reserve Bank of India") |

### 1E. The chai-stall-uncle version
Imagine the uncle who runs the tea stall near your house wants Rs2 lakh to buy a
bigger stove and fridge, so he can serve more customers. He has no salary slip, no
GST filing, nothing a bank wants to see. Aye Finance looks at his stall instead of his
paperwork — how busy it looks, what other tea-stall owners in his town typically earn,
how long he's been at that spot — and lends him the money anyway, at a higher
interest rate than a bank would charge (because the risk is higher and Aye has to
chase the money down in person if he's late). Aye borrows the money it lends from
banks and bond investors at around 10-11% a year, and lends it out at 21-22%
(Inv. Pres. slide 8) — the difference, minus what it loses when some borrowers can't
pay back, is the profit. Sometimes Aye also "sells" a bundle of these loans to a
bigger bank once they've proven reliable, and books an upfront profit on that sale —
that's the "gain on derecognition" line, and it's growing as a share of profit, which
means part of AYE's earnings now comes from packaging and selling loans, not just
collecting interest on them.

### Section 1 summary table

| Field | Answer |
|---|---|
| Business type | Balance-sheet NBFC lender (financial services, not manufacturing/trading/platform) |
| Revenue nature | Spread income (interest less cost of funds) as core, with a growing episodic securitisation-gain overlay |
| Asset intensity | Heavy (financial-asset heavy — loan book is 80.6% of total assets, Results FY26 p.5) |
| WC intensity | Not applicable (lender); substitute = funding/ALM intensity, currently comfortable (positive cumulative gaps to 5 years, Inv. Pres. slide 20) |
| Pricing power | Weak-to-moderate; yield set by risk-based ceiling and peer competition, not brand power |

---

## SECTION 2: INDUSTRY DYNAMICS & COMPETITIVE POSITION

### 2A. Five forces, plainly

| Force | Answer | Helps/Hurts/Neutral |
|---|---|---|
| Competition count | At least 6 named MSME-focused NBFC peers tracked by CRISIL: Five-Star Business Finance, SBFC Finance, Veritas Finance, Vistaar Financial Services, Finova Capital, plus Aye itself (AR p.202, "Peer Benchmarking") | Hurts — crowded, well-funded peer set, several bigger by AUM (Five-Star Rs1,28,471mn 1HFY26 vs Aye Rs60,276mn, AR p.203) |
| Entry barriers | High operational cost of servicing small-ticket loans, no credit history on target borrowers, years needed to build cluster-level underwriting knowledge, RBI NBFC registration and capital requirements (AR p.220, "Barriers to entry... include high operational costs... nuanced underwriting... stringent regulatory requirements") | Helps — genuine moat against new entrants, though not against well-capitalised existing peers |
| Supplier power (lenders to Aye) | Aye borrows from 82 lenders/counterparties as of Sep-2025 (banks 32.0%, DFIs 19.1%, other FIs 49.0% incl. retail, Inv. Pres. slide 18); cost of borrowing has been falling (11.80% FY23 → 10.78% Q1FY27, Inv. Pres. slide 18) | Neutral-to-helps — diversified base limits any single lender's pricing power, and rating upgrades (India Ratings A→A+, Jun-2026, digest-only) are cutting the marginal cost |
| Customer power/concentration | Individually powerless (micro-borrowers, avg ticket Rs1.5-4.9 lakh); portfolio concentration is geographic not customer — top state Bihar 15.77% AUM as of Sep-2025, top-5 states 57.0% (AR p.224-225) | Helps on customer side, Neutral/mild hurt on geographic concentration (Bihar/UP/Rajasthan-heavy) |
| Substitutes | Informal lenders/money-lenders/chit funds charging 36-60% p.a. (AR p.222, CRISIL); MFIs for the very smallest ticket sizes; banks only for the "organised" micro-MSME segment with GST filings (Inv. Pres. slide 13) | Helps — Aye is cheaper than the informal alternative and serves a segment banks structurally can't underwrite |

### 2B. Competitive positioning map (named competitors, from CRISIL/prospectus data)

| Player | AUM 1HFY26 (Rs mn) | 2.5Y AUM CAGR (FY23-1HFY26) | Branches 1HFY26 | AUM mix (secured:unsecured:other) | ATS (Rs mn) |
|---|---|---|---|---|---|
| Aye Finance | 60,276 | 37.4% (highest among peers) | 568 | 62% secured : 38% unsecured : 0% | 0.10-0.18 |
| Five-Star Business Finance | 128,471 | 28.1% | 800 | 100% secured : 0% : 0% | 0.3-0.5 |
| SBFC Finance | 99,380 | 32.2% | 220 | 83% secured : 0% : 17% other | 0.95 |
| Veritas Finance | 77,460 | 36.9% | NA (438 FY25) | 56% secured : 7% unsecured : 37% other | 0.2-5 |
| Vistaar Financial Services | 50,470 | 21.0% | NA (265 FY25) | 76.7% secured : 23.3% unsecured : 0% | 2-10 |
| Finova Capital | 35,535 | 36.6% | NA (393 FY25) | 79% secured : 13% unsecured : 8% other | 0.4 |

(All figures AR p.202-203, CRISIL peer benchmarking table.) Aye Finance is the
fastest-growing of the peer set on AUM CAGR, has the smallest average ticket size and
the most geographic diversification (no state >15.8% of AUM, AR p.203) but is also the
only peer among the largest names running a meaningfully unsecured book (38% of AUM)
— the flip side of "most diversified customer base" is "most exposed to unsecured
credit losses in a downturn."

### 2C. Moat assessment (eight standard moat types)

| Moat type | Present? | Evidence | Durability |
|---|---|---|---|
| Brand | Weak/absent | No brand-pricing evidence found; borrowers choose on access/speed, not brand (NOT FOUND: any brand premium data) | Low |
| Network effects | Absent | Lending is not a two-sided network business | N/A |
| Switching costs | Moderate | Repeat-loan retention rate 41.16-49.59% across FY23-1HFY26 (AR p.224, footnote 2); repeat loans 52.0% of HL AUM in Q1FY27 (Inv. Pres. slide 30) — borrowers who get one loan tend to come back, but this reflects access, not lock-in | Moderate, contingent on continued good service |
| Cost advantages | Moderate | Highest reduction in cost-to-income ratio among peers, FY23-FY25, "16%, the highest reduction among Peer MSME Focused NBFCs" (AR p.229); disbursement productivity/loans-per-employee highest among peers in FY25 (AR p.229, "29.3 loans per employee... highest among the Peer MSME Focused NBFCs") | Moderate — scale-and-maturity driven, erodes if branch/employee growth outpaces AUM maturation |
| Regulatory license/moat | Present, real | RBI NBFC-ML certificate of registration is a hard entry requirement; capital-heavy and compliance-heavy for new entrants (AR p.220, p.223) | Durable, but does not exclude the 5-6 named peers who already hold equivalent licenses |
| Proprietary data/IP | Present, strongest identified moat | 70+ business-cluster underwriting models built over 12 years, "considerable investment of time and resources and presents a notable challenge for new entrants to replicate" (AR p.230-231, CRISIL-sourced) | Durable and compounding (each new cluster adds to the knowledge bank), but only a moat against literal new entrants, not against the 5-6 established peers with their own data assets |
| Scale/distribution | Moderate | 571 branches, 18 states + 3 UTs, most geographically diversified among peers (AR p.203); but Five-Star has 800 branches and larger AUM | Moderate — Aye is mid-pack, not dominant, on distribution scale |
| Customer captivity/relationships | Moderate | 100% in-house origination (no DSA reliance), branch-local staff, high stated NPS "89.65% in Fiscal 2025" (AR p.230, self-reported, unaudited metric) | Moderate; self-reported NPS should be treated cautiously |

### 2D. Industry lifecycle stage and AYE's position
The formal MSME-lending-to-micro-enterprises segment is in an early-growth phase of
penetration, not a mature stage: only 27-28% of the estimated Rs159 trillion FY25
MSME credit demand is met by formal financing, leaving an estimated Rs117-trillion
credit gap (AR p.226, CRISIL). NBFC credit overall is forecast to grow 18-20% p.a.
Mar-25 to Mar-27, versus bank credit at 11-13% (AR p.11790-11791). Within this,
AYE sits as a fast-growing, mid-scale specialist (2.5Y CAGR 37.4%, highest among the
six-name peer set, AR p.202) still in a branch-maturation phase — 45.3-54.3% of
recent AUM growth has come from deepening existing branches rather than new branch
openings, and the company explicitly says it intends to slow new-branch openings
(AR p.236-237; Inv. Pres. slide 31 shows 0 new branches in Q1FY27).

### 2E. Key industry drivers

| Driver | Direction | Impact on AYE |
|---|---|---|
| Formalisation of MSMEs (Udyam registration ~50% of MSMEs as of Sep-2025) | Positive, structural | Expands the addressable, more-creditworthy customer pool over time (AR p.12236-12237) |
| NBFC credit growth outpacing bank credit (18-20% vs 11-13% NBFC vs bank, Mar25-Mar27E) | Positive | Favours NBFC-model lenders like AYE relative to bank-channel competition (AR p.11790-11791) |
| Rising NBFC share of MSME bank+NBFC lending (9.2% FY19 → 16.6% FY25) | Positive | Structural tailwind for the NBFC channel AYE operates in (AR p.15566) |
| Rate-cut cycle / cost of borrowing trend | Positive for AYE currently | CoB has fallen from 11.80% (FY23) to 10.78% incremental (Q1FY27), aided by rating upgrades (Inv. Pres. slide 18-19) |
| Regional/state-level micro-lending stress episodes (e.g. Bihar/local MFI over-lending, referenced digest-only) | Risk/negative if it recurs | Company states "minimal impact" and that 92% of the current portfolio was originated post the Jun-24 "over-lending" period (Inv. Pres. slide 23) — monitor, not yet a confirmed drag |

---

## SECTION 3: FINANCIAL METRICS THAT MATTER FOR THIS BUSINESS MODEL

### 3A. Ignore-these-track-these table

| Commonly tracked ratio | Verdict for AYE | Why |
|---|---|---|
| EV/EBITDA | IRRELEVANT | AYE has no "EBITDA" concept that is meaningful — finance cost (its main input cost) sits above the line that EBITDA would normally exclude, and equity/debt structure IS the business (leverage funds the loan book). EV/EBITDA double-counts or misprices funding cost. |
| EBITDA margin | IRRELEVANT | Same reasoning — a lender's "margin" is NIM/spread, not an EBITDA concept |
| Inventory days | IRRELEVANT | No inventory; a lender has none |
| Receivable days / DSO | IRRELEVANT | The loan book itself is the "receivable" and is measured via AUM, yield and NPA/PAR ageing buckets, not DSO |
| Asset turnover (Revenue/Assets) | MISLEADING | For a lender, "assets" (the loan book) generate revenue by design at a known yield; asset turnover conflates with yield and obscures leverage, which is the real variable that matters |
| Gross margin | MISLEADING | No cost-of-goods-sold; the analogous metric is NIM/spread (yield on advances minus cost of borrowing), reported directly by the company |
| P/E on unadjusted reported EPS | USE WITH CAUTION | Reported PAT includes the securitisation gain-on-derecognition line (3.65% of FY26 total income and rising, Results FY26 p.6) which is non-cash/episodic — normalise before applying P/E |

### 3B. Must-track metrics

**Growth**

| Metric | What it tells you | Healthy range (this industry) | Where to find it | Red flag threshold |
|---|---|---|---|---|
| AUM growth (YoY) | Core franchise momentum | 25-30% FY27 guidance (Inv. Pres. slide 32); peer range 21-37% 2.5Y CAGR (AR p.202-203) | Investor presentation / results filing | <15% YoY, or growth achieved only via lower-quality (unsecured) mix shift |
| Disbursement growth | Forward-looking pipeline signal, leads AUM | Q1FY27 +22% YoY (Inv. Pres. slide 7) | Investor presentation | Disbursement growth persistently below AUM growth (signals slowing new business, AUM sustained by back-book only) |
| AUM per branch / branch maturation | Efficiency of existing footprint vs new-branch-led growth | Branches >3yr vintage AUM Rs135.47mn vs <3yr Rs61.83mn (AR p.236-237) | Prospectus/MD&A | Falling AUM/branch despite branch vintage improving |

**Profitability and efficiency**

| Metric | What it tells you | Healthy range (this industry) | Where to find it | Red flag threshold |
|---|---|---|---|---|
| NIM / spread (on ATA) | Core unit economics — the lending spread | FY27 guidance 14.25-14.75% (Inv. Pres. slide 32); FY26 actual 14.38% (Inv. Pres. slide 37) | Results filing / investor presentation | Sustained compression not offset by cost-of-borrowing decline |
| Cost of borrowing (CoB), incremental | Funding cost trend, directly hits spread | Incremental CoB 10.20% Q1FY27, down from 11.80% FY23 (Inv. Pres. slide 18-19) | Investor presentation | Incremental CoB rising while yield is capped/falling |
| Cost-to-income ratio | Operating efficiency | 50.1% Q1FY27 (Inv. Pres. slide 8); FY27 opex/ATA guidance 8.25-8.75% (Inv. Pres. slide 32) | Investor presentation / MD&A | Rising cost-to-income alongside slowing AUM growth (loss of operating leverage) |
| RoA (on total assets) | Bottom-line efficiency per rupee of balance sheet | FY27 guidance 4.0-4.5% (Inv. Pres. slide 32); FY26 actual 3.08% on AUM basis / Q1FY27 3.71% on assets (Inv. Pres. slide 8, 37) | Investor presentation | RoA persistently below 2.5-3% for a lender at this risk profile |
| RoE | Return generated on shareholder capital | 3-year vision 17.0-20.0% (Inv. Pres. slide 33); FY26 actual 9.26% (post dilution from Feb-26 IPO equity infusion, Inv. Pres. slide 37) | Investor presentation | RoE stuck below 12% for multiple quarters post the equity infusion dilution washes through |

**Balance sheet and risk**

| Metric | What it tells you | Healthy range (this industry) | Where to find it | Red flag threshold |
|---|---|---|---|---|
| GNPA / NNPA / PAR X / PAR30 | Underlying asset quality across delinquency buckets | GNPA FY26 4.77%, NNPA 1.79-1.80% (Results FY26 p.11); PAR X 6.88-7.01% (Inv. Pres. slide 21-22) | Results filing / investor presentation | GNPA >6% or a reversal of the "6 consecutive quarters improving" trend (Inv. Pres. slide 6) |
| Credit cost (annualised, % of ATA) | Provisioning burn, directly hits RoA | FY27 guidance 3.5-4.0%, 3-year normalised target 3.25-3.75% (Inv. Pres. slide 32-33); Q1FY27 actual 4.01% (Inv. Pres. slide 8) | Investor presentation | Credit cost re-accelerating above 5% (FY25 level was 5.15%, AR p.225) |
| PCR (Provision Coverage Ratio) | Cushion held against recognised bad loans | 63.66% FY26, 63.80% Jun-26 (Results FY26 p.11; Inv. Pres. slide 25) | Results filing / investor presentation | PCR falling below ~55-60% while GNPA is rising (under-provisioning) |
| CRAR / Tier I | Capital cushion, growth headroom | 42.24% FY26 (Results FY26 p.11), well above RBI's ~15% NBFC-ML minimum; boosted by Feb-26 IPO Rs710cr primary infusion | Results filing | CRAR falling toward regulatory minimum without a fresh capital plan |
| ALM gaps (cumulative, by bucket) | Liquidity/refinancing risk | Positive cumulative mismatch in every bucket to 5 years as of Jun-26 (Inv. Pres. slide 20) | Investor presentation | Any negative cumulative gap in the <1 year buckets |
| Debt-to-equity / leverage | Balance-sheet risk multiplier on RoE | Closing D/E 2.06x FY26 (Results FY26 p.11); leverage (avg assets/avg net worth) 3.15x-3.46x Q1FY27/Q4FY26 (Inv. Pres. slide 37) | Results filing / investor presentation | D/E persistently rising without commensurate CRAR headroom |

### 3C. Industry-specific non-financial KPIs

| KPI | Why it matters for AYE | Where to find it |
|---|---|---|
| Number of active customers / accounts | Franchise breadth, portfolio granularity | ~6.7 lakh (Inv. Pres. slide 10); prospectus 5,86,825 as of Sep-2025 (AR p.219) |
| Collection efficiency, Non-OD and Bucket-1 | Leading indicator of asset-quality direction, ahead of GNPA recognition | Inv. Pres. slide 22-23 (99.2% Non-OD, 54.5% Bucket-1, Q1FY27) |
| Repeat retention rate / repeat loan % of disbursement | Customer stickiness, lower acquisition cost per rupee of AUM | AR p.224 (41.16-49.59% across years); repeat loans 45.3-54.3% contribution to AUM growth (Inv. Pres. slide 31) |
| % AI/ML-scored underwriting vs cluster-methodology | Tech-driven efficiency/scalability trajectory | 32% AI/ML : 68% cluster (Inv. Pres. slide 27; digest-only cross-check consistent) |
| % of collections via digital modes / NACH registration | Cost-to-collect efficiency and fraud/leakage control | 85.97% digital collection, 95.84% NACH-activated (Inv. Pres. slide 27) |
| Non-starter / early delinquency rate | Underwriting quality at first-payment stage, earliest possible red flag | 0.08-0.10% non-starter, 0.29-0.35% early delinquency, FY23-1HFY26 (AR p.230-231) |
| Number of business clusters covered | Proxy for underwriting-moat breadth | 70+ clusters as of Sep-2025 (AR p.221) |
| Branch vintage mix (<2Y / 2-4Y / 4+Y) | Signals how much AUM growth still has to come from maturation vs new sourcing | Inv. Pres. slide 30-31 |

### 3D. Unit economics — the physics of the business

**Define one unit:** one average outstanding loan (Rs 1.5-4.9 lakh depending on
product, AR p.213-214 / Inv. Pres. slide 15).

| Element | Value/driver |
|---|---|
| Revenue per unit | Interest income at yield ~21.95-22.95% on ATA (Inv. Pres. slide 8) applied to average outstanding, plus fees (servicing/application/delay charges) |
| Cost per unit | Cost of borrowing on the funded portion (~10.2-10.8% incremental, Inv. Pres. slide 18) + credit cost (provisions, 4.01% ATA Q1FY27, Inv. Pres. slide 22) + opex allocated per loan (branch, underwriting, collections staff) |
| Volume drivers | Branch count and branch maturation (AUM/branch rises with vintage, AR p.236), repeat-loan conversion, new customer sourcing via in-house branch teams (100% in-house origination, AR p.229) |
| Price drivers | Risk-based pricing by product (up to 26-32% PA ceiling by product, AR p.222); average yield is a portfolio-mix outcome (more mortgage/secured = lower yield but lower risk and longer tenor) |
| Cost drivers | Cost of borrowing (rating-linked), credit cost (macro/local stress-linked), employee cost (branch staffing ratio) |
| Incremental margin / operating leverage | As branches mature (3yr+ vintage AUM per branch more than double <3yr vintage, AR p.236-237) and mortgage share rises (longer tenor, "will reduce our cost to income ratio," AR p.238), incremental loans cost less to originate and service per rupee of AUM — this is the core operating-leverage story management is explicitly targeting (opex/ATA target 7.0-7.5% over 3 years vs 8.9% Q1FY27, Inv. Pres. slide 33 vs 32) |

---

## SECTION 4: RISKS, VALUATION APPROACH & MONITORING

### 4A. Business-model-specific risks

| Category | Risk | First financial line item that would deteriorate |
|---|---|---|
| Revenue model | Growing reliance on gain-on-derecognition (securitisation) income to support reported PAT — episodic, not repeatable without continuous fresh pool sales | "Net gain on derecognition of financial instruments" line in the P&L (currently 3.65% of FY26 total income, up from 1.94% FY23, Results FY26 p.6) |
| Margin | NIM compression if yield falls (mix shift to lower-yield mortgage/secured) faster than cost of borrowing falls | Average Yield (%) (Inv. Pres. slide 8) narrowing relative to Cost of Borrowing (%) (slide 18) |
| Balance sheet | Unsecured hypothecation book (37-38% of AUM, AR p.222) is the highest-loss-given-default segment; regional stress (e.g. Bihar concentration 15.77% AUM, AR p.224) could re-trigger the "over-lending" dynamics referenced for the pre-Jun-24 period | PAR X / PAR30 and Stage 2 assets ratio (Results FY26 disclosures; Inv. Pres. slide 22) |
| Execution | Reliance on branch maturation (not new branch openings) for growth — if maturing branches plateau below the 3yr+ vintage benchmark (Rs135.47mn AUM/branch, AR p.236), AUM growth guidance (25-30% FY27, Inv. Pres. slide 32) is at risk | AUM per branch (AR p.219) and disbursement growth vs AUM growth gap |
| Structural | No identifiable promoter; PE/VC-backed cap table with large single-investor stakes (Elevation Capital 12.6%, LGT 10.1%, Inv. Pres. slide 38) — future secondary block sales by financial sponsors post lock-up expiry are a supply overhang risk, not an operating risk but a market-structure one | Shareholding pattern disclosures (BSE/NSE filings) and promoter/AIF category ownership % |

### 4B. Valuation method applicability — formal handoff to Role 1 valuation stage

| Method | Applicable? | Notes |
|---|---|---|
| P/B (price to adjusted book value) | **PRIMARY** | Standard for lenders; book value directly reflects the capital base that generates the spread income. Must be adjusted for the quality of the FY26 book (gain-on-derecognition income embedded in retained earnings is lower-quality than pure NII-driven book growth). Net worth Rs2,464.69cr (Reg 52 basis, Results FY26 p.11) / Rs2,532.71cr (statutory total equity, Results FY26 p.5) as at Mar-26; BVPS Rs106 as of Jun-26 (Inv. Pres. slide 8) |
| P/E on normalised earnings | **SECONDARY** | Must strip the securitisation gain and FV-change gain (together 9.33% of FY26 total income, Results FY26 p.6) to get a normalised, repeatable earnings base before applying a multiple; reported diluted EPS FY26 Rs9.60 (Results FY26 p.6) is not directly comparable across periods given the mix shift in these two lines |
| Excess-return / Gordon-growth (RoE vs cost of equity, growth-adjusted) | **TERTIARY** | Useful cross-check given management's explicit 3-year RoE target band (17-20%, Inv. Pres. slide 33) and AUM CAGR target (28-33%, Inv. Pres. slide 33) — can triangulate a justified P/B from RoE-CoE-growth |
| EV/EBITDA | NOT APPLICABLE | Meaningless for a lender — finance cost is a core operating input, not a financing add-back (see 3A) |
| DCF on free cash flow | NOT APPLICABLE (in standard form) | A growing loan book consumes cash by design; standard FCF-to-firm framing misrepresents a lender. An excess-return/residual-income variant (tertiary above) is the appropriate substitute |
| Sum-of-the-parts | NOT APPLICABLE | Single reportable segment — "There is no separate reportable segment as per IndAS 108" (Results FY26 note 7, p.10) |

**Cycle stage that matters for valuation:** AYE is in a branch-maturation, credit-cost-normalisation
phase (credit cost declining for multiple consecutive quarters toward a 3.25-3.75%
normalised target, Inv. Pres. slide 33) within an early-penetration industry growth
phase (see 2D). Valuation should weight the trajectory of NIM, credit cost and RoE
toward the stated 3-year guidance band, not a single trailing quarter, given the
post-IPO (Feb-2026) capital infusion is still diluting recent RoE prints (Q1FY27 RoE
16.0%* on a post-infusion basis vs the unadjusted comparison, Inv. Pres. slide 8).

### 4C. Quarterly monitoring checklist (10-15 items)

1. AUM growth YoY and QoQ — vs 25-30% FY27 guidance (Inv. Pres. slide 32). Good: within/above band. Trouble: below 20% for two consecutive quarters.
2. Disbursement growth YoY — leading indicator. Good: tracking or exceeding AUM growth. Trouble: disbursement growth persistently lagging AUM growth.
3. NIM (on ATA) — Good: holding within 14.25-14.75% guidance. Trouble: sustained compression below 14%.
4. Cost of borrowing, incremental — Good: continued decline (rating-upgrade-linked). Trouble: incremental CoB rising QoQ.
5. GNPA / NNPA — Good: continuation of the multi-quarter improving trend. Trouble: any QoQ increase in GNPA.
6. PAR X / PAR30 — Good: stable-to-declining. Trouble: rising for two consecutive quarters.
7. Credit cost (annualised, % ATA) — Good: tracking toward 3.5-4.0% FY27 guidance. Trouble: re-acceleration above 4.5%.
8. PCR — Good: maintained above ~63%. Trouble: falling below 55% while GNPA is flat/rising.
9. Collection efficiency, Non-OD and Bucket-1 — Good: Non-OD sustained >99%. Trouble: Non-OD dropping below 98.5%.
10. Cost-to-income ratio — Good: declining toward the 7.0-7.5% opex/ATA 3-year target. Trouble: rising QoQ without a branch-expansion explanation.
11. Mortgage/LAP share of AUM — Good: rising toward the stated 30-35% target (digest-only cross-check, Q4FY26 deck). Trouble: stalling, undermining the stated portfolio-stability strategy.
12. Gain on derecognition as % of total income — Good: stable or declining as a share (signals earnings quality improving). Trouble: rising further as a share of PAT (signals reliance on episodic gains).
13. CRAR / Tier I — Good: comfortably above regulatory minimum with growth headroom. Trouble: rapid decline without a capital-raise plan.
14. RoA / RoE — Good: tracking toward 4.0-4.5% RoA / 17-20% RoE 3-year targets. Trouble: stalled well below band for 2+ quarters post-IPO-dilution washout.
15. ALM cumulative gap position — Good: positive in all buckets. Trouble: any negative gap in <1yr buckets.

### 4D. Highest-value questions for management

1. **Q: What share of FY26/FY27 PAT would remain if gain-on-derecognition and net FV
gain were excluded?**
   Reassuring: a small, stable, or shrinking share (below ~5-6% combined).
   Worrying: a rising share approaching double digits, indicating core spread income
   is not carrying reported profit growth on its own.

2. **Q: What is the credit-cost and yield profile specifically on the unsecured
hypothecation book (37-38% of AUM) versus the secured/mortgage book?**
   Reassuring: unsecured-book credit cost trending toward the 3.25-3.75% company-wide
   normalised target with a clear risk-adjusted spread.
   Worrying: unsecured credit cost meaningfully above company average with no
   convergence trend, implying mix-driven risk understatement.

3. **Q: How much of the FY27 25-30% AUM growth guidance depends on new-branch
openings versus deepening of the existing 571-branch network?**
   Reassuring: growth continues to be branch-maturation-led (consistent with the
   stated strategy of slowing new-branch openings, AR p.236-237).
   Worrying: a pivot back to branch-count-led growth, which historically brings lower
   AUM/branch and higher opex ratios in year 1-2 (AR p.236).

4. **Q: What is the concentration and renewal risk on the securitisation/direct-
assignment buyer base — how many counterparties, and is pricing/appetite improving
or tightening?**
   Reassuring: a diversified, growing buyer base at stable or improving pricing.
   Worrying: a small number of buyers, or gain-on-derecognition margins compressing,
   which would directly hit the growing income line identified in 1B/4A.

5. **Q: Post the Feb-2026 IPO capital infusion (Rs710cr primary), what is the
capital-deployment glidepath to bring CRAR (42.24% FY26, well above the regulatory
minimum) back toward an efficient operating range, and over what timeframe?**
   Reassuring: a clear multi-year AUM-growth plan that deploys the excess capital
   without diluting further or taking on disproportionate risk.
   Worrying: no clear plan, raising the risk of either value-destructive M&A/dilutive
   growth or persistently depressed RoE from carrying excess capital.

6. **Q: How exposed is the Bihar/UP/Rajasthan-heavy portfolio (top-5 states 57% of
AUM, AR p.224) to state-specific micro-lending stress episodes similar to those
referenced around Jun-2024?**
   Reassuring: management can show granular, cluster-level early-warning data and a
   track record of containing such episodes (as claimed for the post-Jun-24 book,
   Inv. Pres. slide 23).
   Worrying: limited visibility or a repeat pattern of regional flare-ups recurring
   across cycles.

7. **Q: What is management's target mix of mortgage/LAP vs hypothecation over the
next 3 years, and what NIM/credit-cost trade-off does that imply?**
   Reassuring: a coherent, quantified glidepath consistent with the stated 3-year
   RoA/RoE/credit-cost guidance band (Inv. Pres. slide 33).
   Worrying: vague or shifting targets that don't reconcile with the guidance band.

---

## SECTION 5: ONE-PAGE BUSINESS MODEL SUMMARY CARD

```
┌─────────────────────────────────────────────────────────────────────────┐
│ AYE FINANCE LIMITED (AYE) — BUSINESS MODEL SUMMARY CARD                  │
├─────────────────────────────────────────────────────────────────────────┤
│ BUSINESS TYPE: Balance-sheet NBFC-ML lender (micro-enterprise finance)   │
│ ONE-LINE: Lends small, high-margin business loans to India's smallest    │
│   MSMEs using proprietary cluster-based underwriting instead of formal   │
│   financial documents, funded by bank/bond borrowing at a lower rate.    │
├─────────────────────────────────────────────────────────────────────────┤
│ REVENUE MIX (FY26, anchored, Results FY26 p.6):                          │
│   Interest income          83.6%   High predictability                  │
│   Fees & commission         4.0%   High predictability                  │
│   Gain on derecognition     3.7%   Low predictability, RISING share     │
│   Net gain on FV changes    5.7%   Low predictability, market-driven    │
│   Other income               2.6%   Low predictability                  │
├─────────────────────────────────────────────────────────────────────────┤
│ ASSET INTENSITY: Heavy (financial) — loans 80.6% of total assets         │
│ WC INTENSITY: N/A (lender) — substitute = ALM/funding intensity: SOUND   │
│   (positive cumulative ALM gaps to 5 years, Jun-26, Inv. Pres. slide 20) │
│ PRICING POWER: Weak-moderate — yield 21.95-22.95% ATA (risk-based,       │
│   RBI-monitored ceiling, peer-competed), not brand-driven                │
│ CYCLICALITY: Cyclical (credit cost/PAR track SME/rural credit cycle)     │
├─────────────────────────────────────────────────────────────────────────┤
│ MOATS PRESENT:                                                           │
│   Proprietary cluster underwriting IP — DURABLE, compounding             │
│   RBI NBFC-ML license — DURABLE but shared with named peers              │
│   Cost/productivity edge (highest cost-to-income improvement, most       │
│     loans/employee among peers, FY23-25) — MODERATE, scale-dependent     │
│   Repeat-customer retention (41-50% retention rate) — MODERATE           │
├─────────────────────────────────────────────────────────────────────────┤
│ VALUATION: PRIMARY = P/B (adjusted book) | SECONDARY = P/E on            │
│   normalised earnings (strip securitisation + FV gains) | TERTIARY =     │
│   Excess-return/Gordon-growth on RoE vs CoE | EV/EBITDA IRRELEVANT       │
├─────────────────────────────────────────────────────────────────────────┤
│ MUST-TRACK (top 5): AUM growth, NIM/spread, credit cost, GNPA/PAR X,     │
│   CRAR/leverage headroom                                                  │
├─────────────────────────────────────────────────────────────────────────┤
│ ONE-LINE VERDICT: A genuinely differentiated, fast-growing micro-MSME    │
│   lender with a real underwriting moat, whose reported profit growth     │
│   increasingly leans on an episodic securitisation-gain line that must   │
│   be stripped out before valuing the core spread business.               │
└─────────────────────────────────────────────────────────────────────────┘
```

---

```yaml
stage: B04-bizmodel
company: "AYE"
run_date: "2026-07-22"
model: claude-sonnet-5
status: complete
input_gaps: []                # AR + investor presentation + FY26 results all available
flags:
  - "Gain-on-derecognition (securitisation) income is a rising share of total income (1.94% FY23 -> 2.50% FY25 -> 3.65% FY26, Results FY26 p.6) and is episodic/non-cash-upfront in nature; must be stripped for normalised P/E."
  - "Net gain on fair value changes (FX/MTM/treasury) was the single largest non-interest income line in FY26 (5.68% of total income, Results FY26 p.6) and is market-driven, not operating."
  - "No identifiable promoter; PE/VC-backed cap table with concentrated single-sponsor stakes (Elevation Capital 12.6%, LGT 10.1%, Inv. Pres. slide 38) is a structural overhang to monitor, not an operating flag."
business_type: "lending"      # balance-sheet NBFC lender
revenue_streams:
  - {name: "Interest income on loans", type: "recurring spread income", pct_of_revenue: 83.6, predictability: "H"}
  - {name: "Fees and commission income", type: "recurring transaction fee", pct_of_revenue: 4.0, predictability: "H"}
  - {name: "Net gain on derecognition (securitisation/direct assignment)", type: "episodic non-cash gain", pct_of_revenue: 3.7, predictability: "L"}
  - {name: "Net gain on fair value changes", type: "market/treasury gain", pct_of_revenue: 5.7, predictability: "L"}
  - {name: "Other income", type: "non-operating", pct_of_revenue: 2.6, predictability: "L"}
asset_intensity: "heavy"       # financial-asset heavy: loans 80.6% of total assets (Results FY26 p.5)
wc_intensity: "NOT APPLICABLE" # lender; substitute metric is funding/ALM intensity, currently sound
pricing_power: "moderate"      # expressed as yield/spread/NIM per lender adaptation, not gross margin
cyclicality: "cyclical"        # credit cost / PAR track the SME and rural credit cycle
moats_present:
  - {moat: "Proprietary 70+ business-cluster underwriting IP (12+ years built)", durability: "durable, compounding"}
  - {moat: "RBI NBFC-ML regulatory license", durability: "durable, but shared with 5-6 named peers"}
  - {moat: "Cost/productivity edge (highest cost-to-income improvement and loans/employee among peers, FY23-25)", durability: "moderate, scale-dependent"}
  - {moat: "Repeat-customer retention (41-50% retention rate)", durability: "moderate"}
valuation_methods:
  primary: {method: "P/B (price to adjusted book value)", why: "Standard for a balance-sheet lender; book value is the capital base generating spread income"}
  secondary: {method: "P/E on normalised earnings (ex securitisation gain, ex FV-change gain)", why: "Reported EPS is inflated by episodic, non-repeatable gain-on-derecognition and treasury/FX gains (9.3% of FY26 total income combined)"}
  tertiary: {method: "Excess-return / Gordon-growth on RoE vs cost of equity", why: "Cross-checks against management's own explicit 3-year RoA/RoE/AUM-growth guidance band"}
  not_applicable: ["EV/EBITDA", "Standard FCF-to-firm DCF", "Sum-of-the-parts (single reportable segment, Results FY26 note 7)"]
irrelevant_ratios:
  - {ratio: "EV/EBITDA", why: "Finance cost is a core operating input for a lender, not a financing add-back"}
  - {ratio: "EBITDA margin", why: "No EBITDA concept meaningfully applies; NIM/spread is the analogous metric"}
  - {ratio: "Inventory days", why: "A lender carries no inventory"}
  - {ratio: "Receivable days / DSO", why: "The loan book is measured via AUM, yield and NPA/PAR ageing, not DSO"}
  - {ratio: "Asset turnover", why: "Conflates with yield and obscures leverage, the variable that actually matters for a lender"}
must_track_metrics:
  - {metric: "AUM growth (YoY)", healthy: "25-30% (FY27 guidance)", red_flag: "below 20% for two consecutive quarters"}
  - {metric: "NIM / spread (on ATA)", healthy: "14.25-14.75% (FY27 guidance)", red_flag: "sustained compression below 14%"}
  - {metric: "Credit cost (annualised, % ATA)", healthy: "3.5-4.0% (FY27 guidance), 3.25-3.75% (3yr normalised target)", red_flag: "re-acceleration above 4.5%"}
  - {metric: "GNPA / PAR X", healthy: "continuation of multi-quarter improving trend (GNPA 4.77% FY26)", red_flag: "any QoQ increase for two consecutive quarters"}
  - {metric: "CRAR / leverage headroom", healthy: "comfortably above regulatory minimum (42.24% FY26) with a deployment plan", red_flag: "rapid decline without a capital-raise plan"}
unit_economics:
  unit: "One average outstanding loan (Rs 1.5-4.9 lakh depending on product)"
  revenue_per_unit: "Interest at ~21.95-22.95% yield on ATA plus servicing/application/delay fees (Inv. Pres. slide 8, AR p.427)"
  margin_per_unit: "Yield less cost of borrowing (~10.2-10.8% incremental) less allocated credit cost (~4.0% ATA) less allocated opex"
  key_lever: "Branch maturation (AUM/branch more than doubles from <3yr to 3yr+ vintage) and rising mortgage/secured mix driving operating leverage toward the 7.0-7.5% opex/ATA 3-year target"
first_deterioration_signals:
  - {risk: "Rising reliance on gain-on-derecognition for reported PAT", first_signal: "Net gain on derecognition of financial instruments (% of total income) line rising further, Results filing"}
  - {risk: "NIM compression", first_signal: "Average Yield (%) narrowing relative to Cost of Borrowing (%), investor presentation"}
  - {risk: "Unsecured-book / regional concentration stress", first_signal: "PAR X / PAR30 and Stage 2 assets ratio rising, results filing / investor presentation"}
  - {risk: "Growth reliance shifting back to new-branch openings", first_signal: "AUM per branch declining despite rising branch vintage, MD&A"}
  - {risk: "Sponsor/AIF ownership overhang", first_signal: "Bulk-deal / block-sale disclosures in shareholding pattern filings"}
mgmt_questions:
  - "What share of FY26/FY27 PAT would remain if gain-on-derecognition and net FV gain were excluded?"
  - "What is the credit-cost and yield profile specifically on the unsecured hypothecation book (37-38% of AUM) versus secured/mortgage?"
  - "How much of the FY27 25-30% AUM growth guidance depends on new-branch openings versus deepening the existing 571-branch network?"
  - "What is the concentration and renewal risk on the securitisation/direct-assignment buyer base?"
  - "Post the Feb-2026 IPO capital infusion, what is the capital-deployment glidepath to bring CRAR back toward an efficient range?"
  - "How exposed is the Bihar/UP/Rajasthan-heavy portfolio (top-5 states 57% of AUM) to state-specific micro-lending stress episodes?"
  - "What is management's target mix of mortgage/LAP vs hypothecation over the next 3 years, and what NIM/credit-cost trade-off does that imply?"
one_line_verdict: "A differentiated, fast-growing micro-MSME lender with a real underwriting moat, whose reported profit growth increasingly leans on an episodic securitisation-gain line that must be stripped out before valuing the core spread business."
```
