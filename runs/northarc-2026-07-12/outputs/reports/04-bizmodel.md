# STAGE 4 — BUSINESS MODEL DECODER
## Northern Arc Capital Limited (NORTHARC)
Run date: 2026-07-12 | Model: claude-sonnet-5

**Sources used:** Annual Report FY 2024-25 (AR, extracted/annual-report.txt, page markers refer to physical PDF page unless noted "printed p.__"), Investor Presentation Q4FY26/FY26 (Inv. Pres., extracted/investor-presentation.txt, physical PDF page = "slide __"), Q4FY26 audited results filing (extracted/results-Q4-FY26.txt).

**Important date-vintage note:** the AR is for FY 2024-25 (year ended 31 March 2025); the Investor Presentation is for FY 2025-26 (year ended 31 March 2026), one full year later. Both are used as instructed — AR as primary for business description/MD&A/segment notes, Inv. Pres. as the latest operating and financial data point. Every number below is tagged to its specific source and year so the two vintages are never blended silently.

The manifest's "Pharma / CDMO" sector label is a known collector error and is ignored; this is an NBFC-ML (lender).

---

# SECTION 1: THE BUSINESS MODEL IN PLAIN ENGLISH

## 1A. One-line description
Northern Arc is a diversified, technology-led NBFC that lends directly to underserved MSME, consumer and rural borrowers across India (D2C) while also acting as a wholesale credit pipe — lending to, investing alongside, and raising money for ~350+ smaller NBFC "originator partners" (Credit Solutions) — earning its money as the spread between what it charges borrowers and what it pays lenders, plus fees for moving other people's money through its funds, placements and technology platforms (AR printed p.6-7, Inv. Pres. slide 11).

## 1B. Money flow chains, one per revenue stream

| # | Stream | Flow |
|---|--------|------|
| 1 | **D2C interest income (MSME/Consumer/Rural)** | [Company borrows from banks/DFIs/bond markets at ~8.7%-9.0% cost of funds] → [Northern Arc originates and underwrites a loan directly via its own 432 branches or 57 digital partners] → [disburses to a small business, gig-economy/salaried consumer, or rural JLG borrower] → [borrower pays EMI/interest at 15%-24.9% depending on product] → [Northern Arc earns the D2C net yield of ~15%-19% before credit cost] (AR printed p.18-21; Inv. Pres. slides 13, 15, 17). |
| 2 | **Intermediate Retail (IR) / balance-sheet lending to originator partners** | [Northern Arc borrows on its own balance sheet] → [on-lends via term loans, NCDs, CPs, securitisation/PTC to ~350+ smaller NBFC "originator" partners, holding 110%-120% collateral cover of the originator's retail loan pool] → [originator on-lends to its own retail borrowers and services the pool] → [originator repays Northern Arc at an average yield of ~13.0%-13.5%] → [Northern Arc earns the spread over its own cost of funds] (AR printed p.24-25). |
| 3 | **Placement / structured debt distribution fees** | [Originator partner needs to raise debt] → [Northern Arc structures and places the debt (securitisation, PTC, NCD, syndication) with third-party investors — banks, offshore funds, DFIs — taking little/no balance-sheet risk itself] → [investor buys the paper] → [Northern Arc earns a placement/arranger fee, ~0.27% of placement volume in FY26, up from 0.21% in FY25] (Inv. Pres. slide 22). |
| 4 | **Fund management (Northern Arc Investment Managers — NAIM)** | [HNIs, family offices, DFIs, offshore investors commit capital] → [NAIM deploys it into performing-credit AIFs/PMS that invest in originator NCDs/pools] → [fund earns interest/returns for LPs] → [NAIM earns an annual management fee, ~1.17%-1.23% of Fund AUM (₹3,092-3,158 cr)] (AR printed p.42-43; Inv. Pres. slide 23). |
| 5 | **SaaS / technology monetisation (nPOS, NuScore, Altifi)** | [Third-party bank/NBFC/fintech wants co-lending or underwriting infrastructure without building it] → [Northern Arc licenses nPOS (co-lending tech), NuScore (ML credit-scorecard-as-a-service) or Altifi (retail bond distribution/OBPP)] → [partner processes loans/investments on the platform] → [Northern Arc earns a platform/transaction fee — e.g. South Indian Bank co-lending via nPOS generated ₹761 cr of volume in FY25] (AR printed p.24-25). |

## 1C. Revenue model classification table

| Stream | Type | Description | % of revenue (anchored) | Predictability |
|---|---|---|---|---|
| Net Interest Income — D2C + IR lending combined | Spread/interest income | Interest earned on loan book less interest paid on borrowings | NII was ₹1,377 cr of ₹1,484 cr Net Revenue in FY26 = **92.8%** (Inv. Pres. slide 36, consolidated income statement); FY25: NII ₹1,147 cr of ₹1,248 cr Net Revenue = **91.9%** (AR printed p.64 DuPont table) | Medium — recurring but credit-cost-sensitive |
| Fee & Other Income (placement fees + fund mgmt fees + SaaS + other) | Fee/transaction income | Non-fund-based, capital-light fee streams | FY26: ₹108 cr of ₹1,484 cr Net Revenue = **7.3%**; FY25: ₹102 cr of ₹1,248 cr = **8.2%** (Inv. Pres. slide 36; AR printed p.64) | Medium-High — sticky AUM-linked fee (funds) is high-predictability; placement fees are volume/market-cycle dependent, lower predictability |
| Statutory segment split (Note 46, consolidated, FY25) — "Financing activity" (interest income) | Interest income | Interest income on loans/investments across D2C+IR combined | ₹2,280.20 cr of ₹2,341.61 cr total external segment revenue = **97.4%** (AR printed p.375-376, Note 46) | Medium |
| Statutory segment — "Investment Management services" (NAIM/fund mgmt) | Fee income | AIF/PMS management fees | ₹50.46 cr = **2.2%** of total external segment revenue (AR printed p.375-376) | High — AUM-linked, contractual |
| Statutory segment — "Others/Unallocated" | Mixed | Includes Pragati and other minor lines | ₹10.89 cr = **0.5%** (AR printed p.375-376) | Low-Medium |
| Statutory segment — "Investment advisory services" | Fee income | Effectively nil in FY25 | ₹0.06 cr = **~0.0%** (AR printed p.375-376) | N/A — immaterial |

Note: two valid revenue lenses exist in the source documents — (i) the operating P&L view (NII vs Fee & Other Income, from the Inv. Pres./MD&A DuPont tables) and (ii) the statutory Ind AS segment note (Financing / Investment Advisory / Investment Management / Others, from AR Note 46). Both are anchored above and are not reconciled to a single number because the source documents themselves present them on different bases (segment revenue is gross external revenue before finance-cost netting; NII is post-finance-cost). A precise ₹-revenue split between D2C interest income and IR interest income specifically is **NOT FOUND** in either document — only AUM-mix and yield-range proxies are disclosed (see 3D).

## 1D. Simplified business model canvas

| Element | Description |
|---|---|
| What they sell | Credit (loans) directly to underserved households/MSMEs, and "credit infrastructure" (balance sheet, funds, placement access, technology, underwriting data) to smaller NBFC partners |
| Who buys | (a) MSME/consumer/rural retail borrowers directly; (b) ~350+ smaller NBFC "originator partners" who need balance-sheet capital, placement access or tech; (c) ~1,300+ institutional/HNI investors who buy into funds or placed paper (AR printed p.16-17, 24-25) |
| Why them | 16-year track record across four credit cycles (demonetisation, IL&FS, COVID, FY25 MFI stress) with NNPA sustained under 1% throughout (Inv. Pres. slide 9); AA-(Stable) rating gives relatively cheap, diversified access to 49 lenders/investors (AR printed p.66); proprietary 47.5 mn-plus data-point underwriting engine (NuScore) that smaller originators cannot replicate |
| How delivered | Own branch network (432 branches, Mar-26) + 57 digital lending partners for D2C; balance sheet + Nimbus platform + fund vehicles + Altifi distribution for Credit Solutions (Inv. Pres. slides 6, 11) |
| Cost structure dominance | Finance cost (interest paid on borrowings) is the single largest cost line — ₹902 cr of total costs in FY26 vs ₹331 cr employee cost and ₹198 cr other opex (Inv. Pres. slide 36) — i.e. this is a "cost of capital" business, not a "cost of goods" business |
| Scarce resource | Underwriting data/models (NuScore, 10+ years, 50 mn+ data points) and the AA- credit rating that unlocks diversified, lower-cost funding (AR printed p.67; AR printed p.66) |
| Pricing power source or absence | Partial and segment-specific: strong in niche underserved D2C pockets (secured LAP, rural JLG) where formal competition is thin; weak/price-taker in IR lending to originators, which is essentially a spread business competing against banks and other wholesale lenders on cost of funds |
| Asset intensity | Physical/fixed-asset intensity is **low** (leased branches, cloud tech stack); balance-sheet intensity is **high** — the loan book (₹12,493 cr of loans on balance sheet, Mar-26, Inv. Pres. slide 38) is funded by ₹12,258 cr of borrowings, i.e. leverage (D/E) of ~3.1x (Inv. Pres. slide 33) |
| WC intensity mapped for a lender | Not inventory/receivables — the analogue is **managed gearing and ALM (asset-liability mismatch)**. Northern Arc must continuously roll over/raise borrowings to fund AUM growth; company reports "no negative cumulative mismatch across all buckets" as of Mar-26 (Inv. Pres. slide 34) — the equivalent of "high working-capital intensity," permanently financed by debt, not equity |
| Regulatory moat or burden | Both. RBI NBFC-ML (middle layer) registration + AA- external rating is itself a barrier to new entrants (capital, compliance, governance requirements under RBI Scale Based Regulation, 2023); but it is also a burden — RBI risk-weight changes on unsecured credit and DLG/ECL rule changes directly hit FY25 P&L (₹68 cr one-time DLG provision) (AR printed p.62-64) |

## 1E. The chai-stall-uncle version

Imagine a very well-connected uncle at the chai stall who does two things. First, he lends his own savings directly to the vegetable seller, the auto driver and the small farmer nearby — charging them 15-24% interest because banks won't bother with such small loans, and because he actually knows their business (that's the D2C engine). Second, he's also the guy that smaller local moneylenders come to when they need capital to lend onward — he lends them money at a smaller spread, helps them find rich investors who want a piece of the action (funds and placements), and even rents them his notebook of "who pays back and who doesn't" (the NuScore data). He makes money in two ways: the difference between what he pays his own bank for money and what he charges borrowers (the spread), and a small fee for connecting other lenders to money and to his data. He's survived demonetisation, a funding crisis, COVID and a recent microfinance blow-up without ever losing more than 1% of what he lent out — that's the whole pitch.

## Section 1 summary table

| Field | Value |
|---|---|
| Business type | Lending (NBFC-ML) with an embedded asset-light fee/platform business |
| Revenue nature | Recurring spread income (~92-93% of net revenue) + AUM/volume-linked fee income (~7-8%) |
| Asset intensity | Physical: light. Balance sheet: heavy (leverage ~3.1x) |
| WC intensity | High (mapped as managed gearing/ALM, continuously debt-financed) |
| Pricing power | Moderate in niche D2C pockets; weak/price-taker in wholesale IR lending |

---

# SECTION 2: INDUSTRY DYNAMICS & COMPETITIVE POSITION

## 2A. The five forces, plainly

| Force | Assessment | Helps / Hurts / Neutral |
|---|---|---|
| Competition intensity | Retail credit market of ~₹82 trillion growing ~15% CAGR (FY18-FY25) but Northern Arc competes against banks (dominant in Tier-1, cheaper cost of funds), larger NBFCs, and a growing wave of fintech-NBFC co-lending partnerships; retail credit growth decelerated from 18.0% (FY24) to 13.9% (FY25) as lenders turned risk-averse (AR printed p.5, p.61). No specific named competitors are disclosed in either document — **NOT FOUND, check investor presentation or concall** for a named competitive set. | Hurts (crowded, capital-intensive segment; no moat of exclusivity) |
| Entry barriers | RBI NBFC-ML registration, minimum capital adequacy (15% CRAR minimum; Northern Arc runs 22.6%-24.7%), Scale Based Regulation governance requirements, and — critically — the need for an investment-grade external rating (AA- here) to access diversified, lower-cost funding are real barriers for new entrants (AR printed p.39-40, p.66) | Helps (raises the bar for new entrants, though does not block well-capitalised players) |
| Supplier power (cost of funds/capital providers) | Northern Arc has 49 lenders/investors, with borrowings split ~53% banks, ~30% offshore DFIs, ~17% capital markets (Mar-26, Inv. Pres. slide 33); no single lender concentration disclosed, but banks broadly reduced lending to NBFCs sector-wide in FY25 (AR printed p.62) | Neutral-to-Hurts (diversified but ultimately price-taker on cost of funds vs banks) |
| Customer power and concentration | On the D2C side, individual retail/MSME borrowers have essentially zero bargaining power (small ticket, fragmented). On the IR/Credit Solutions side, originator partners are more concentrated (350+ partners, but AUM-range data shows 40% of originators have AUM ₹2,000-10,000 cr, Inv. Pres. slide 20) and could shop for cheaper wholesale funding elsewhere in good times | Helps on D2C; Neutral-to-Hurts on IR |
| Substitutes | Digital lenders/fintechs with direct app-based disbursal, self-help-group/informal lending in rural areas, banks' own priority-sector lending push, and co-lending platforms that disintermediate Northern Arc's balance-sheet role | Hurts (structural, ongoing) |

## 2B. Competitive positioning map

Named, anchored competitors are **NOT FOUND** in the AR or Investor Presentation — neither document benchmarks Northern Arc against specific listed peers (no "Five-Star", "Aptus", "MAS Financial", "CreditAccess Grameen" or similar names appear). What can be anchored is Northern Arc's own positioning language: it describes itself as occupying a "dual-channel" niche — both a direct retail lender AND a wholesale credit-solutions provider to smaller NBFCs — which it presents as differentiated versus pure-play D2C NBFCs or pure-play wholesale/DCM arrangers (AR printed p.6-7, "differentiated and comprehensive play across India's retail credit ecosystem"). **Check investor presentation or concall for a named peer-comparison table.**

## 2C. Moat assessment (eight standard moat types)

| Moat type | Present? | Evidence | Durability |
|---|---|---|---|
| Regulatory/license | Yes | RBI NBFC-ML registration, AA-(Stable) rating from ICRA & India Ratings since inception of rating relationship, CRAR 22.6%-24.7% vs 15% regulatory minimum (AR printed p.40, Q4FY26 filing p.13) | Medium — rating can be downgraded; barrier is real but not exclusive |
| Data/informational advantage | Yes | Proprietary data repository of 47.52 mn+ data points built over 10+ years; NuScore ML underwriting engine processed 2.5 lakh+ loan assessments in FY25 (AR printed p.67) | Medium-High — compounds with scale, hard for new entrants to replicate quickly |
| Distribution network | Yes | 432 branches + 57 digital partners + 368 originator partners + 1,300+ investor partners across 28 states/7 UTs/680 districts (Inv. Pres. slides 6, 11; AR printed p.7) | Medium — capital and time-intensive to build, but replicable by well-funded competitors |
| Switching costs | Partial | nPOS/Nimbus API integrations embed Northern Arc into originator-partner workflows (e.g. South Indian Bank co-lending live on nPOS) creating some stickiness (AR printed p.25) | Low-Medium — technology stacks are increasingly commoditised/replaceable |
| Brand/trust (institutional) | Yes | 16-year track record across four credit cycles with NNPA <1% throughout; marquee institutional cap table (IFC, LeapFrog, Eight Roads, Sumitomo Mitsui, Accion) (Inv. Pres. slide 9; AR printed p.40) | Medium-High — reputational capital built over a long period, hard to fake |
| Network effects | Partial | The credit-solutions ecosystem (originators + investors + funds + data) becomes more valuable to each new originator/investor as it grows — a modest two-sided network effect | Low-Medium — nascent, not yet a dominant flywheel |
| Cost advantage/efficient scale | No/Weak | Cost-to-income ratio 35.6% FY26 (Inv. Pres. slide 37) is respectable but not clearly best-in-class; Northern Arc is a price-taker on cost of funds versus banks | Low |
| Counter-cyclical diversification | Yes | Explicit strategy to dial sector exposure (MSME/Consumer/Rural) and channel mix (D2C vs IR) up/down through cycles — demonstrated by cutting rural AUM 27.2% YoY in FY25 while growing MSME/Consumer (AR printed p.20-21) | Medium — a genuine structural feature, not easily replicated by mono-line lenders |

## 2D. Industry lifecycle stage

India's retail credit market (₹82 trillion, 15% CAGR FY18-FY25) and the specific sub-segments Northern Arc plays in (MSME credit gap ₹117 trillion; consumer finance market projected 20% CAGR to FY28; NBFC-MFI segment now in consolidation/de-risking post FY25 stress) are collectively in a **growth/early-maturity** stage — large unmet credit gap, double-digit structural growth, but with a currently ongoing **cyclical correction** in unsecured/MFI credit (AR printed p.61-63). Northern Arc itself is in an **early-scale-up phase as a listed entity** (IPO Sept-2024, first full listed year FY25), pivoting its own mix from wholesale/IR toward D2C (D2C mix rose from 18.9% Mar-21 to 59% Mar-26) (Inv. Pres. slide 9).

## 2E. Key industry drivers

| Driver | Direction | Impact on Northern Arc |
|---|---|---|
| NBFC credit growth (13.2% CAGR FY19-25, projected 15-17% to FY28) | Positive | Tailwind for AUM growth target of 20-25% (AR printed p.68) |
| RBI risk-weight/DLG regulatory changes | Negative (episodic) | Directly caused the FY25 one-time ₹68 cr DLG provision and the FY26 audit "Emphasis of Matter" on ECL/DLG treatment change (Q4FY26 filing p.4) |
| Repo rate cuts (6.5% Dec-24 → 5.5% Jun-25) | Positive | Lower cost of funds tailwind (cost of funds already down from 9.2% FY24 to 9.0% FY25 to 8.7% FY26 incremental, Inv. Pres. slide 33) |
| MFI sector overleveraging/stress (Karnataka ordinance, SRO guardrails) | Negative | Forced 27.2% YoY cut in rural AUM in FY25 and elevated rural credit cost (6.8% FY25, moderating to 4.8% FY26) (AR printed p.21; Inv. Pres. slide 27) |
| Rising retail credit penetration/formalisation (credit-to-GDP still ~25% vs developed markets) | Positive | Large multi-decade runway in underserved MSME/consumer/rural segments (AR printed p.62-63) |

---

# SECTION 3: FINANCIAL METRICS THAT MATTER FOR THIS BUSINESS MODEL

## 3A. Ignore-these-track-these table

| Commonly tracked ratio | Why MISLEADING or IRRELEVANT for an NBFC |
|---|---|
| Inventory days / inventory turnover | No inventory exists — the "product" is money, not goods |
| Gross block / fixed-asset turnover | Fixed assets (leased branches, IT hardware) are a trivial fraction of the balance sheet; irrelevant to earnings power |
| Working-capital days (receivable/payable days) | The loan book is not a trade receivable; it is a leveraged financial asset funded by borrowings, analysed via ALM buckets, not WC-days |
| Current ratio / quick ratio | Meaningless for a leveraged financial institution — liquidity is assessed via ALM cumulative mismatch, undrawn sanctions and liquidity coverage, not current assets/current liabilities |
| EV/EBITDA | "EBITDA" is not a meaningful concept here — interest expense is a genuine, core operating cost (cost of the raw material, money), not a financing add-back to be excluded |
| Gross margin % (as used in manufacturing/retail) | The equivalent concept is NIM/spread (yield minus cost of funds), not a cost-of-goods-sold margin |
| Revenue growth alone (without credit-cost context) | Revenue/AUM growth funded by loosening underwriting standards can mask a future credit-cost time bomb — must always be read together with GNPA/NNPA/credit cost trend |
| Debt/Equity as a "leverage red flag" in the conventional sense | For an NBFC, D/E of 2.5-4x is normal and necessary (the business model is to intermediate borrowed capital); D/E must be read against CRAR and ALM, not treated as a standalone solvency warning |

## 3B. Must-track metrics

**Growth**

| Metric | What it tells you | Healthy range (this industry) | Where to find it | Red flag threshold |
|---|---|---|---|---|
| AUM growth (total, and D2C vs IR split) | Core top-line growth engine | 15-25% YoY for a scaling retail NBFC | AR "Northern Arc's Performance" p.10-11; Inv. Pres. slide 8 | <10% YoY, or growth concentrated in one high-risk segment |
| D2C mix % | Shift toward higher-yield, more granular, stickier book | Rising trend (Northern Arc: 18.9%→59% Mar-21→Mar-26) | Inv. Pres. slide 9 | Mix stalling or reversing without stated strategic reason |
| Disbursement growth vs AUM growth | Confirms growth is organic, not just book revaluation | Roughly in line | AR printed p.63 (Gross Transaction Value) | Disbursements falling while AUM still rising (indicates slower churn/aging book) |

**Profitability and efficiency**

| Metric | What it tells you | Healthy range | Where to find it | Red flag threshold |
|---|---|---|---|---|
| NIM / Spread (yield − cost of funds) | Core unit economics of the lending engine | Spread 6-8%+ for a diversified retail NBFC; Northern Arc: 7.9% FY25, yield 16.9% - CoF 9.0% (AR printed p.64) | AR MD&A "Financial Overview"; Inv. Pres. DuPont slide | Spread compression >100 bps YoY without a stated strategic reason |
| Cost-to-income ratio | Operating efficiency | <40% is healthy for scale NBFCs; Northern Arc 35.6% FY26 | Inv. Pres. slide 37 | Rising trend above ~45% |
| RoA | Risk-adjusted profitability, the single best summary metric for a lender | 2.5-4%+ is strong for a diversified NBFC; Northern Arc 2.4% FY25 → 2.8% FY26, guided 3.7-4.0% | Inv. Pres. slide 7/37; AR printed p.65 | Sustained RoA <1.5% |
| RoE | Shareholder return, driven by RoA × leverage | 15-18%+ target; Northern Arc 10.0% FY25 (depressed by one-off provision) → 11.1% FY26, guided 16-18% | AR printed p.65; Inv. Pres. slide 37 | Sustained RoE <10% without a clear capital-deployment story |

**Balance sheet and risk**

| Metric | What it tells you | Healthy range | Where to find it | Red flag threshold |
|---|---|---|---|---|
| GNPA / NNPA (or Gross/Net Stage 3) | Asset quality | GNPA <2%, NNPA <1% is strong for this borrower mix; Northern Arc GNPA 1.2%, NNPA/net-stage-3 0.6-0.7% (Mar-26) | Inv. Pres. slide 27; Q4FY26 filing p.13 | GNPA >3% or a sharp QoQ jump in Stage II (early delinquency) |
| Credit cost (% of avg assets) | The true cost of the lending "raw material" — cyclical | 1.5-3% through-cycle normal; spikes to 5%+ in stress (Northern Arc: 3.2% FY25 incl. one-offs, 2.8% FY26) | AR printed p.64; Inv. Pres. slide 6-7 | Credit cost exceeding NIM for more than one quarter (structurally unprofitable lending) |
| CRAR (capital adequacy) | Capital cushion against regulatory minimum (15%) | 18%+ is comfortable; Northern Arc 22.6% (standalone, Mar-26) | AR printed p.40; Q4FY26 filing p.13 | Approaching 15% floor |
| Managed gearing / D/E | Leverage — the engine of RoE, but also the risk multiplier | 2.5-4x typical for retail NBFC; Northern Arc 3.1x (Mar-26) | Inv. Pres. slide 33 | >5x without a matching CRAR cushion |
| Borrowing mix / lender concentration | Funding diversification and refinancing risk | No single source >40-50% | AR printed p.66; Inv. Pres. slide 33 | Bank funding >70% (concentration risk in a bank-funding-averse cycle) |
| ALM cumulative mismatch | Liquidity/solvency early warning | No negative cumulative mismatch in any bucket, well within RBI's 15% limit | Inv. Pres. slide 34 | Any bucket breaching the 15% regulatory limit |

## 3C. Industry-specific non-financial KPIs

| KPI | Where to find it |
|---|---|
| Number of D2C customers (29.55 lakh, FY26) | Inv. Pres. slide 7 |
| Branch count and states/UTs/districts covered (432 branches, 28 states, 7 UTs, 680 districts) | Inv. Pres. slide 6; AR printed p.9 |
| Number of originator partners (368) and investor partners (1,500+) | Inv. Pres. slide 11 |
| Collection efficiency (X-bucket, by segment — e.g. Rural 99.6% Q4FY26) | Inv. Pres. slides 15, 17 |
| Repeat customer % (Consumer Finance ~70%) | Inv. Pres. slide 16 |
| Stage II asset trend (early delinquency, leading indicator) | Inv. Pres. slide 27-28 |
| Employee headcount and attrition/diversity (3,118 employees, 17% women, Mar-25) | AR printed p.67 |
| Digital/nPOS metrics (disbursals via nPOS, monthly transactions, cumulative disbursements) | AR printed p.25; Inv. Pres. slide 29 |

## 3D. Unit economics — the physics of the business

**Primary unit: ₹1 crore of average AUM outstanding for one year** (a lender's fundamental unit; there is no single "widget")

| Element | Value | Anchor |
|---|---|---|
| Revenue per unit | Yield of ~15.5%-16.9% (blended); D2C sub-segments run 15-24.9% depending on product; IR lending ~13.0%-13.5% (AR printed p.24, 64; Inv. Pres. slide 37) | Blended yield 15.9% Q4FY26 (Inv. Pres. slide 37) |
| Cost per unit | Cost of funds 8.7%-9.0% (FY26 incremental vs FY25 average) + credit cost 2.8% (FY26) + opex ~3.6% (% of avg assets) | Inv. Pres. slides 33, 37 |
| Margin per unit | Spread (yield − CoF) 7.9% FY25, plus further reduced by credit cost (net ~5.1% FY25 excl. opex) and opex (3.6%) to a RoA of 2.4-2.8% | AR printed p.64; Inv. Pres. slide 37 |
| Volume drivers | Branch/digital-partner additions (432 branches Mar-26 vs 360 Mar-25), new originator partner onboarding (368), D2C customer acquisition (29.6 lakh) | Inv. Pres. slides 6-7 |
| Price drivers | Product mix shift toward higher-yield D2C (59% mix Mar-26) vs lower-yield IR lending; risk-based pricing within each product (e.g. LAP 16-24%) | Inv. Pres. slides 9, 15; AR printed p.18-19 |
| Cost drivers | Cost of funds (rating-dependent, rate-cycle dependent), credit cost (underwriting quality and macro cycle — the single biggest swing factor, as FY25 showed), and opex (branch/employee scaling) | AR printed p.64 |
| Incremental margin / operating leverage | Positive and demonstrated: opex as % of avg assets fell from 4.0% (FY24) to 3.6% (FY25/FY26) even as AUM grew ~16-22% YoY, i.e. fixed-cost branch/tech infrastructure is scaling faster than the cost base — classic operating leverage for a branch-based lender once branches mature past break-even | AR printed p.64; Inv. Pres. slide 10 |
| Key lever | **Credit cost normalisation.** RoA moved from 3.0% (FY24) to 2.4% (FY25, depressed by one-off DLG provision + rural MFI stress) to 2.8% (FY26, partial recovery) purely on credit cost swings, while spread was stable/improving throughout — credit cost, not spread or opex, is the dominant swing factor in this business's earnings (AR printed p.64-65; Inv. Pres. slide 37) |

---

# SECTION 4: RISKS, VALUATION APPROACH & MONITORING

## 4A. Business-model-specific risks

| Category | Risk | First financial line item to deteriorate |
|---|---|---|
| Revenue model | Wholesale/IR lending spread compression if originator partners can access cheaper bank funding directly in a rate-cutting cycle | IR lending yield (~13.0-13.5%) and Net Revenue % of avg assets |
| Revenue model | Placement fee income is capital-markets-cycle dependent (foreign participation already "subdued" per Inv. Pres. slide 22) | Placement Fee income line (₹25.8 cr FY25 → ₹31.4 cr FY26) and placement volumes |
| Margin | Cost of funds rising faster than yield can be repriced (asset-liability rate mismatch) | Spread (yield − cost of funds), currently 7.9%/9.4% NIM |
| Margin | Credit cost spike from a single concentrated sector (as MFI/rural did in FY25, causing 6.0-6.8% segment credit cost) | Segment-wise credit cost %, specifically Consumer and Rural |
| Balance sheet | Regulatory ECL/DLG methodology changes (already happened twice — FY25 exclusion, FY26 re-inclusion per RBI Feb-2026 amendment) causing non-comparable provisioning and one-time hits | Credit cost line and the "Emphasis of Matter" audit note |
| Balance sheet | Funding concentration / bank-funding pullback (banks broadly cut NBFC lending in FY25) despite current 53% bank mix | Borrowing mix % from banks; cost of incremental borrowing |
| Execution | D2C branch expansion (432 branches, +64 added in Q4FY26 alone) outrunning underwriting/collections maturity in new geographies | New-branch vintage GNPA/collection efficiency vs mature-branch cohort (not separately disclosed — **NOT FOUND**, flag for concall) |
| Execution | Integration/scaling risk across five subsidiaries (NAIM, Pragati, Northern Arc Securities, Northern Arc CrediTech, Northern Arc Foundation) with different risk/return and regulatory profiles | Consolidated vs standalone PAT/RoA divergence |
| Structural | MFI/rural sector-wide overleveraging and socio-political disruption risk (Karnataka ordinance precedent) recurring | Rural segment GNPA, Stage II %, and collection efficiency |
| Structural | RBI risk-weight changes on unsecured consumer/NBFC exposures (already impacted FY24-25 capital availability) | CRAR trend and risk-weighted-asset growth vs AUM growth |

## 4B. Valuation method applicability (handoff to Role 1 valuation stage)

| Method | Applicable? | Notes |
|---|---|---|
| **P/ABV (Price to Adjusted Book Value)** | **PRIMARY** | Standard for lenders — book value adjusted for expected credit losses is the cleanest measure of intrinsic net-asset value; RoE (10.0% FY25 → 11.1% FY26, guided 16-18%) is the key driver of the justified P/ABV multiple. Book value/share ₹241 (Mar-26, Inv. Pres. slide 7). |
| **P/E on normalised-credit-cost earnings** | **SECONDARY** | Cross-check, but raw reported P/E is distorted by episodic one-offs (FY25 PAT depressed ₹51 cr by one-time DLG provision + overlay; normalised FY25 PAT was ₹356 cr vs reported ₹305 cr, AR printed p.65) — must normalise credit cost to a through-cycle average before applying P/E |
| **Sum-of-parts (lending book P/ABV + AMC/fund-management franchise)** | **TERTIARY** | NAIM (Northern Arc Investment Managers) is a capital-light, ~1.2% fee-on-AUM business (₹3,092 cr Fund AUM, Mar-26) that behaves more like an asset manager than a lender and could command a higher, AUM-multiple-based valuation distinct from the leveraged lending book — worth separating if the AMC business scales further |
| EV/EBITDA | **NOT APPLICABLE** | Interest expense is core operating cost for a lender, not a financing add-back; EBITDA is not a meaningful construct |
| DCF on FCFF | **NOT APPLICABLE** | Financial-firm cash flows are dominated by balance-sheet growth (loan disbursement/collection) rather than capex-driven free cash flow; equity-side DDM/residual-income approaches are the correct DCF analogue, not FCFF |
| EV/Sales or P/Sales | **NOT APPLICABLE** | Revenue is not comparable across differently-levered lenders; a high-leverage NBFC will always show inflated revenue relative to a conservatively-levered peer of similar economic size |
| Asset-based/replacement value | **NOT APPLICABLE** | Physical fixed assets are trivial; the "assets" that matter are financial (loan book), already captured in ABV |

**Cycle stage that matters for valuation:** Northern Arc is coming off a credit-cost trough-to-peak-to-partial-recovery cycle (FY24 credit cost 1.2% → FY25 3.2% including one-offs → FY26 2.8%). Valuation should explicitly test RoA/RoE at a **normalised through-cycle credit cost** (excluding the FY25 one-off DLG provision and overlay) rather than anchoring to either the depressed FY25 print or an unsustainably benign single quarter (Q4FY26 credit cost was 2.2%, RoA 3.3% — likely better than steady-state).

## 4C. Quarterly monitoring checklist (10-15 items)

| # | Item | Good looks like | Trouble looks like |
|---|---|---|---|
| 1 | AUM growth YoY | 15-25%, broadly in line with 20-25% guidance | <10% or a sudden deceleration without explanation |
| 2 | D2C mix % | Steady rise or stable at elevated level | Reversal/stalling |
| 3 | Spread (yield − cost of funds) | Stable or expanding | Compression >50 bps in a quarter |
| 4 | NIM | Stable/expanding, ~9%+ | Sustained decline |
| 5 | Credit cost (% of avg assets), and by segment | In line with guidance (~2.8% FY26) | Segment-level spike, especially Consumer/Rural |
| 6 | GNPA / NNPA (or Gross/Net Stage 3) | GNPA <1.5%, NNPA <1% | GNPA >2.5% or a sharp QoQ jump |
| 7 | Stage II assets (early delinquency) | Declining/stable trend | Rising QoQ — leading indicator of future Stage III |
| 8 | Collection efficiency (X-bucket) by segment | >98% | Declining trend, especially Rural/MFI |
| 9 | CRAR | Comfortably above 18% | Approaching 18% (getting close to 15% regulatory floor) |
| 10 | Debt/Equity (managed gearing) | 2.5-3.5x | Rising sharply without matching CRAR/equity raise |
| 11 | Borrowing mix (bank vs DFI vs DCM) | No source >55-60% | Bank concentration rising while banks broadly pull back from NBFC lending |
| 12 | Cost-to-income ratio | <38% | Rising trend above ~40% |
| 13 | RoA / RoE | RoA trending toward 3.7-4.0%, RoE toward 16-18% guidance | Flat or declining for 2+ consecutive quarters |
| 14 | Fund management AUM and management fee % | Growing AUM at stable/rising fee % | AUM shrinkage or fee-rate compression |
| 15 | One-time items / regulatory provisioning changes | None, or clearly flagged and quantified | Recurring "one-time" items (pattern risk) |

## 4D. Highest-value questions for management

| # | Question | Reassuring answer | Worrying answer |
|---|---|---|---|
| 1 | What is the credit cost run-rate you expect at steady state, excluding one-offs, and how confident are you in the 3.7-4.0% RoA / 16-18% RoE guidance? | Clear bridge from FY26's 2.8% credit cost to a stated normalised range with segment detail | Vague, or guidance repeatedly pushed out |
| 2 | How much of the D2C growth (branches +64 in Q4FY26 alone) is coming from geographies/cohorts less than 12 months old, and what is their vintage-adjusted delinquency versus mature branches? | Disclosed vintage curves showing new cohorts tracking or beating mature-branch performance | Refusal to disclose vintage data, or admission new cohorts are underperforming |
| 3 | Given the FY25 rural/MFI-driven credit-cost spike, what specific underwriting/exposure caps have changed for Consumer Finance and Rural, and are they now binding constraints on growth? | Concrete, quantified caps (e.g. max lenders per borrower, ticket-size limits) that management is holding to even when it caps growth | "We've learned our lesson" without specific new limits |
| 4 | How dependent is placement fee income on foreign/offshore investor participation, which you've flagged as "subdued" — what's the plan if that stays weak? | Diversified plan (domestic banks, DFIs, insurance) already showing traction | Continued reliance on a narrow, cyclical investor base |
| 5 | What is NAIM's (fund management) path to a materially larger, standalone-valuable AUM base, and would you ever consider carving it out? | Specific AUM/fee targets and a credible distribution plan (e.g. GIFT City, offshore) | No clear standalone strategy; treated as an afterthought |
| 6 | With two DLG/ECL regulatory methodology changes in two years, how much further regulatory/provisioning volatility should investors expect, and is this now fully resolved? | Clear statement that the Feb-2026 RBI amendment is the final word, with quantified one-time impact already taken | Hedging language suggesting further changes possible |
| 7 | What is the plan for bank-funding concentration given sector-wide bank pullback from NBFC lending — target mix for DCM/offshore over the next 2-3 years? | Specific diversification targets with progress already shown | Passive "we'll adapt as needed" |

---

# SECTION 5: ONE-PAGE BUSINESS MODEL SUMMARY CARD

```
┌─────────────────────────────────────────────────────────────────────────┐
│  NORTHERN ARC CAPITAL LIMITED (NORTHARC)                                │
│  Business type: Diversified NBFC-ML lender + asset-light credit         │
│  platform (fund management, placements, SaaS)                          │
├─────────────────────────────────────────────────────────────────────────┤
│  ONE-LINE: Lends directly to underserved MSME/consumer/rural            │
│  borrowers (D2C) and lends/arranges capital for smaller NBFC            │
│  "originator partners" (Credit Solutions), earning spread + fees.       │
├─────────────────────────────────────────────────────────────────────────┤
│  REVENUE MIX (FY26, Inv. Pres. slide 36):                               │
│    Net Interest Income .......... 92.8% of Net Revenue                  │
│    Fee & Other Income ............ 7.3% of Net Revenue                  │
│  AUM MIX (Mar-26, Inv. Pres. slide 11):                                 │
│    D2C (MSME+Consumer+Rural) ..... 59% (₹9,792 cr)                      │
│    Intermediate Retail lending ... 41% (₹6,802 cr)                      │
│    + Fund mgmt AUM ₹3,092 cr (off-balance-sheet, fee only)              │
├─────────────────────────────────────────────────────────────────────────┤
│  KEY METRICS (FY26 unless noted):                                       │
│    AUM: ₹16,594 cr (+21.7% YoY)          Yield: 15.9% (Q4FY26)          │
│    NIM: 9.4%                              Cost of funds: ~8.7% incr.    │
│    Spread: 7.9% (FY25)                    Credit cost: 2.8%             │
│    GNPA: 1.2% / NNPA: 0.6-0.7% (Mar-26)   CRAR: 22.6% (standalone)      │
│    Cost-to-income: 35.6%                  D/E: 3.1x                     │
│    RoA: 2.8% (mgmt guides 3.7-4.0%)       RoE: 11.1% (guides 16-18%)    │
├─────────────────────────────────────────────────────────────────────────┤
│  ASSET INTENSITY: Physical-light / Balance-sheet-heavy (leverage 3.1x)  │
│  WC INTENSITY (mapped): High — continuously debt-financed AUM growth    │
│  PRICING POWER: Moderate in niche D2C; price-taker in wholesale IR      │
│  CYCLICALITY: Cyclical (credit cost is the dominant earnings swing)     │
├─────────────────────────────────────────────────────────────────────────┤
│  MOATS: Regulatory/rating (AA-), proprietary underwriting data          │
│  (NuScore, 47.5mn+ data points), distribution network (432 branches,   │
│  368 originator partners), institutional brand/trust, counter-cyclical  │
│  sector-mix flexibility. Weak: cost advantage, network effects (nascent)│
├─────────────────────────────────────────────────────────────────────────┤
│  VALUATION: Primary P/ABV | Secondary P/E on normalised credit cost |   │
│  Tertiary sum-of-parts (lending book + AMC franchise)                   │
├─────────────────────────────────────────────────────────────────────────┤
│  #1 RISK TO WATCH: Credit cost re-spike in Consumer/Rural (segment      │
│  credit cost 4.8-4.9% FY26) — the single largest swing factor in RoA   │
├─────────────────────────────────────────────────────────────────────────┤
│  VERDICT: A recurring-spread lender with a genuine, data-backed         │
│  underwriting moat, whose earnings are entirely a function of how well  │
│  it controls credit cost through the cycle, not of revenue growth.      │
└─────────────────────────────────────────────────────────────────────────┘
```

---

```yaml
stage: B04-bizmodel
company: "NORTHARC"
run_date: "2026-07-12"
model: claude-sonnet-5
status: complete
input_gaps:
  - "AR is FY2024-25 (year ended Mar-2025); Investor Presentation is Q4FY26/FY26 (year ended Mar-2026) — a one-year vintage gap between the two primary sources, handled by tagging every number to its specific source-year rather than blending them"
  - "No named competitors (e.g. specific listed NBFC peers) disclosed in either AR or Investor Presentation; competitive positioning map is qualitative only"
  - "Vintage-cohort delinquency data for new vs mature branches not disclosed"
  - "Precise rupee-value revenue split between D2C interest income and IR interest income specifically (as opposed to AUM mix or blended yield) is not disclosed"
flags: []
business_type: "lending"
revenue_streams:
  - {name: "Net Interest Income (D2C + IR lending)", type: "spread/interest income", pct_of_revenue: 92.8, predictability: "M"}
  - {name: "Fee & Other Income (placement fees, fund mgmt fees, SaaS)", type: "fee/transaction income", pct_of_revenue: 7.3, predictability: "M"}
  - {name: "Statutory segment: Financing activity (interest income)", type: "spread/interest income", pct_of_revenue: 97.4, predictability: "M"}
  - {name: "Statutory segment: Investment Management services (NAIM)", type: "AUM-linked fee income", pct_of_revenue: 2.2, predictability: "H"}
  - {name: "Statutory segment: Others/Unallocated", type: "mixed", pct_of_revenue: 0.5, predictability: "L"}
asset_intensity: "medium"
wc_intensity: "high"
pricing_power: "moderate"
cyclicality: "cyclical"
moats_present:
  - {moat: "Regulatory license / credit rating (RBI NBFC-ML, AA- Stable)", durability: "medium"}
  - {moat: "Proprietary underwriting data (NuScore, 47.5mn+ data points, 10+ yrs)", durability: "medium-high"}
  - {moat: "Distribution network (432 branches, 368 originator partners, 57 digital partners)", durability: "medium"}
  - {moat: "Institutional brand/trust (16-yr, 4-cycle track record, NNPA <1%)", durability: "medium-high"}
  - {moat: "Counter-cyclical sector-mix flexibility (D2C/IR, MSME/Consumer/Rural)", durability: "medium"}
  - {moat: "Switching costs via nPOS/Nimbus API integration with originators", durability: "low-medium"}
valuation_methods:
  primary: {method: "P/ABV (Price to Adjusted Book Value)", why: "Standard lender valuation; book value adjusted for expected credit losses is the cleanest net-asset measure, driven by RoE"}
  secondary: {method: "P/E on normalised-credit-cost earnings", why: "Cross-check after normalising for episodic one-offs (FY25 DLG provision distorted reported PAT by ~₹51 cr)"}
  tertiary: {method: "Sum-of-parts (lending book P/ABV + AMC/fund-management franchise)", why: "NAIM is a capital-light, AUM-fee business (₹3,092 cr Fund AUM) that could warrant a separate, higher multiple than the leveraged lending book"}
  not_applicable: ["EV/EBITDA", "DCF on FCFF", "EV/Sales or P/Sales", "Asset-based/replacement value"]
irrelevant_ratios:
  - {ratio: "Inventory days/turnover", why: "No inventory exists in a lending business"}
  - {ratio: "Gross block / fixed-asset turnover", why: "Fixed assets are trivial relative to the financial (loan) balance sheet"}
  - {ratio: "Working-capital days", why: "Loan book is a leveraged financial asset funded by borrowings, analysed via ALM, not WC-days"}
  - {ratio: "Current ratio / quick ratio", why: "Meaningless for a leveraged financial institution; liquidity is assessed via ALM mismatch and undrawn sanctions"}
  - {ratio: "EV/EBITDA", why: "Interest expense is a core operating cost, not a financing add-back, for a lender"}
must_track_metrics:
  - {metric: "AUM growth (total, D2C vs IR split)", healthy: "15-25% YoY", red_flag: "<10% YoY or sudden deceleration"}
  - {metric: "NIM / Spread (yield minus cost of funds)", healthy: "Spread 6-8%+, e.g. 7.9% FY25", red_flag: "Compression >100 bps YoY"}
  - {metric: "GNPA / NNPA (Gross/Net Stage 3)", healthy: "GNPA <2%, NNPA <1%", red_flag: "GNPA >3% or sharp QoQ Stage II jump"}
  - {metric: "Credit cost (% of avg assets)", healthy: "1.5-3% through-cycle", red_flag: "Exceeds NIM for more than one quarter"}
  - {metric: "RoA / RoE", healthy: "RoA 2.5-4%+, RoE 15-18%+", red_flag: "Sustained RoA <1.5% or RoE <10%"}
unit_economics:
  unit: "₹1 crore of average AUM outstanding for one year"
  revenue_per_unit: "Blended yield ~15.5-16.9% (D2C 15-24.9%, IR ~13.0-13.5%)"
  margin_per_unit: "Spread 7.9% (FY25) minus credit cost (2.8-3.2%) minus opex (~3.6%) = RoA 2.4-2.8%"
  key_lever: "Credit cost normalisation — the dominant swing factor in RoA/RoE, far more than spread or opex, as demonstrated by the FY24-FY26 credit-cost cycle (1.2% to 3.2% to 2.8%)"
first_deterioration_signals:
  - {risk: "IR lending spread compression from originator disintermediation", first_signal: "IR lending yield and Net Revenue % of avg assets"}
  - {risk: "Placement fee income cyclicality (capital-markets/offshore dependence)", first_signal: "Placement Fee income line and placement volumes"}
  - {risk: "Asset-liability rate mismatch", first_signal: "Spread (yield minus cost of funds) and NIM"}
  - {risk: "Sector-concentrated credit cost spike (Consumer/Rural)", first_signal: "Segment-wise credit cost % and Stage II assets"}
  - {risk: "Regulatory ECL/DLG methodology volatility", first_signal: "Credit cost line and audit 'Emphasis of Matter' notes"}
  - {risk: "Bank-funding concentration/pullback", first_signal: "Borrowing mix % from banks and incremental cost of funds"}
  - {risk: "New-branch cohorts underperforming mature branches", first_signal: "Vintage-adjusted GNPA/collection efficiency by branch cohort (currently undisclosed)"}
  - {risk: "MFI/rural sector-wide overleveraging recurrence", first_signal: "Rural segment GNPA, Stage II %, collection efficiency"}
mgmt_questions:
  - "What is the steady-state credit cost run-rate, excluding one-offs, and how confident is management in the 3.7-4.0% RoA / 16-18% RoE guidance?"
  - "What is the vintage-adjusted delinquency of new branches/cohorts (64 added in Q4FY26 alone) versus mature branches?"
  - "What specific, binding underwriting caps have changed for Consumer Finance and Rural post the FY25 credit-cost spike?"
  - "How dependent is placement fee income on subdued offshore investor participation, and what is the diversification plan?"
  - "What is NAIM's path to a materially larger, potentially standalone-valuable AUM base?"
  - "Is the Feb-2026 RBI DLG/ECL methodology amendment the final word, or should investors expect further provisioning volatility?"
  - "What is the target funding mix (bank/DFI/DCM) over the next 2-3 years given sector-wide bank pullback from NBFC lending?"
one_line_verdict: "A recurring-spread lender with a genuine underwriting-data moat whose earnings live and die on credit-cost control, not revenue growth."
```
