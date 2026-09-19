# STAGE 4: BUSINESS MODEL DECODER — KISSHT (OnEMI Technology Solutions Ltd)

Run date: 2026-09-19. Archetype: Lender (CLAUDE.md archetype library). Sector
cap row: Banks / NBFCs / MFIs (P/B primary, PE cross-check), per B00.

Primary source: Annual Report FY2025-26 (AR), business/MD&A sections and
notes. Secondary: Q1 FY27 investor presentation (IP1, 29-Jul-2026) and Q4
FY26 deck (IP2, 28-May-2026). Cross-checked against the RHP (25-Apr-2026)
"Our Business" and "Industry Overview" sections, and the CRISIL rating
rationale on subsidiary Si Creva (13-Feb-2026). All figures ₹ Cr unless
stated; the AR statements are in ₹ million, its own MD&A narrative is in ₹
Cr — both cited as they appear on the source page.

LOAD-BEARING FACTS CHECKED (B00 LBF-1/2/3): LBF-1 (write-off trigger) —
confirmed NOT FOUND in the AR narrative sections read for this stage,
consistent with B02/B03; the AR gives only qualitative write-off language.
LBF-2 (FLDG) — the AR states the FLDG band is 0-5% of off-book AUM (AR
p.19-20), not a fixed 5%; company memory's "5% upfront FLDG" overstates the
disclosed range. LBF-3 (guidance) — the Q1 FY27 CEO letter (IP1 p.5) repeats
the FY27 AUM >40% and asset-quality-strengthening guidance; this stage found
no new business-model evidence changing the B03 verdict that GNPA is
tracking the wrong direction after one quarter.

---

## SECTION 1: THE BUSINESS MODEL IN PLAIN ENGLISH

### 1A. One-line description
Kissht is a technology-led digital lender that lends some money itself
through its own NBFC subsidiary and, for the rest, finds and services
borrowers on behalf of bank and NBFC partners for a fee (AR p.19-20, "Our
lending business comprising both on-book and off-book portfolios").

### 1B. Money flow chain, by revenue stream

The AR discloses five revenue lines (Note 23, consolidated, AR p.118-119)
and defines each precisely in the RHP (p.354-355). The parent, OnEMI
Technology Solutions Ltd (the listed entity), does not lend directly at
all: on-book lending happens entirely inside its wholly owned subsidiary,
Si Creva Capital Services Pvt Ltd, an RBI-registered NBFC-Middle Layer (AR
p.19). This is a structural fact that changes how every revenue line
should be read.

| # | Stream | Input | What Kissht does | What it delivers | Who pays | How they pay |
|---|---|---|---|---|---|---|
| 1 | Interest on loans (on-book) | Si Creva's own borrowed + equity capital | Underwrites and disburses PL/LAP loans from its own book (AI/ML decisioning, 400+ variables) | A funded loan, serviced end-to-end | The retail borrower | EMI over 6 months-5 years (PL) or up to 15 years (LAP, AR) / 10 years (LAP, IP1) — tenure figure conflicts across documents, see Section 4 |
| 2 | Sourcing and servicing fees (off-book) | Kissht's origination platform + partner bank/NBFC/fund-house capital | Originates, KYC's, underwrites and collects on loans that sit on a PARTNER's balance sheet (100-0, co-lending or direct assignment) | A sourced, serviced, collected loan account for the partner | The lending partner (bank/NBFC/fund house), not the borrower | Fee per loan sourced + fee for ongoing servicing/collections (RHP p.354-355) |
| 3 | Insurance commission and rewards | Third-party insurer's product (health/auto) | Cross-sells insurance at the point of loan disbursal via the app | A bundled insurance policy | The insurer, as commission | Commission on policies sold (RHP p.355) |
| 4 | Marketing and commission income | Other institutions' products/services | Promotes third-party offers (credit-improvement plans, wellness programs) on its app to its existing user base | Advertising placement / lead referral | The third-party institution | Marketing/referral fee (RHP p.355) |
| 5 | Other fees and charges | The borrower's own missed payment or early exit | Charges late-payment and foreclosure fees | Enforcement of loan terms | The retail borrower | Penal/foreclosure charge (RHP p.355) |

A sixth flow exists only in the STANDALONE (parent-only) accounts and
disappears on consolidation: corporate guarantee fees (₹217.15 mn FY26,
Note 21, AR p.83) that Si Creva pays OnEMI for OnEMI's guarantee backing
Si Creva's NCDs and term loans. This is an intercompany flow, not
consolidated revenue, but it is the parent's only "lending-adjacent"
income line besides sourcing/servicing fees — confirming the listed
entity itself carries a guarantee obligation, not a loan book (see B02/B03
FLAG-CAPITAL-STRUCTURE, 228% of parent net worth).

### 1C. Revenue model classification table (consolidated, FY26, Note 23, AR p.118-119; ₹ million)

| Stream | Type | Description | % of revenue FY26 | % of revenue FY25 | Predictability |
|---|---|---|---|---|---|
| Interest on loans | Interest income (on-book) | Interest + processing fees on Si Creva's own book | 58.4% (₹12,725.58 mn) | 74.3% (₹9,943.06 mn) | M — tied to on-book AUM growth and asset quality |
| Sourcing and servicing fees | Fee income (off-book origination + servicing) | Fees from 8+ partner banks/NBFCs/fund houses for sourced/serviced/collected loans on their books | 26.6% (₹5,793.65 mn) | 17.8% (₹2,381.90 mn) | M — depends on partner appetite continuing to fund off-book AUM |
| Other fees and charges | Penal/foreclosure fee income | Late-payment and foreclosure charges | 11.1% (₹2,421.86 mn) | 7.1% (₹944.44 mn) | L — rises when collections stress rises, not a "clean" growth line |
| Insurance commission and rewards | Cross-sell commission | Commission on third-party insurance sold at disbursal | 3.2% (₹693.95 mn) | 0.3% (₹34.42 mn) | L — discretionary attach-rate product |
| Marketing and commission income | Cross-sell/referral commission | Ad placement + referral fees for third-party products | 0.7% (₹157.42 mn) | 0.5% (₹70.83 mn) | L — small, discretionary |

Total consolidated revenue from operations: ₹21,792.46 mn (₹2,179.25 Cr)
FY26 vs ₹13,374.65 mn (₹1,337.47 Cr) FY25 (AR p.118-119, Note 23). Adding
other income (₹298.83 mn, Note 24) reconciles closely to the MD&A's
rounded "Total Income ₹2,209 Cr" FY26 figure (AR p.35).

Note the mix shift: interest income's share of revenue fell 16 points
(74.3% → 58.4%) as off-book fee income and penal/foreclosure charges grew
faster than the on-book book. This mechanically compresses the blended
revenue yield even before any change in underlying pricing — a fact any
yield trend must be read through (see Section 3D).

### 1D. Simplified business model canvas

| Dimension | This company |
|---|---|
| What they sell | Unsecured personal loans (up to ₹5 lakh, AR p.9 & IP1 p.11, consistent across sources) and secured loans against property (ticket size disclosed inconsistently, see Section 4); plus a loan-sourcing-and-servicing service sold to bank/NBFC/fund-house partners |
| Who buys | Retail borrowers: mass-market and mass-affluent, median CIBIL 746, 53% self-employed/47% salaried, 72% under 35, 78% from India's top 100 cities (IP1 p.12); AND, separately, 45+ lending/co-lending partners who buy the sourcing-and-servicing service (AR p.19) |
| Why them | Speed (TAT cut from weeks to minutes), zero-paperwork digital journey, proprietary AI/ML underwriting (400+ variables, 40 models, AUC improved 66%→74% 2023-2026, IP1 p.23), brand recall via Sachin Tendulkar endorsement (AR p.20, RHP p.179) |
| How delivered | 100% digital for PL; hybrid digital + 98-101 branch-assisted model for LAP (AR p.9, IP1 p.11) |
| Cost structure dominance | Operating expenses (₹1,091 Cr, 49% of FY26 total income) exceed both finance cost (₹282 Cr, 13%) and credit cost (₹459 Cr, 21%) — this is an opex-heavy, tech-and-collections-staff-driven cost base, not a pure balance-sheet lender (AR p.35) |
| Scarce resource | Proprietary underwriting/collections data and models (10 Mn+ historical credit decisions used to train models, IP1 p.22); the NBFC-ML registration held by Si Creva (AR p.19) |
| Pricing power source or absence | Absent on both sides. Cost of borrowing is set by the rating (A-/Stable, mid-investment-grade, AR p.20) and by lender appetite (14.16% AR FY26, 14.45% IP1 Jun-26); lending rates are constrained by intense competition from KreditBee, Navi, Fibe, Moneyview and bank-backed NBFCs (RHP p.178-180). No standalone yield or NIM % is disclosed anywhere in this container (NOT FOUND) |
| Asset intensity | Medium — 46.4% of AUM sits on Si Creva's own balance sheet (on-book), 53.6% is off-book/asset-light as of Jun-26 (IP1 p.38) |
| WC intensity | Not a trade-receivables business; the loan book itself is the "working capital," funded by ₹2,396 Cr of borrowings (AR p.20) at D/E 1.78x (subsidiary, FY26). Classified High in the YAML field for this reason, not in the manufacturer sense |
| Regulatory moat or burden | Both. RBI NBFC-ML registration and Digital Lending Guidelines are an entry barrier for unlicensed rivals (AR p.15, "DLG Discipline"), but the same guidelines cap FLDG/DLG at 0-5% of the off-book pool (AR p.20), structurally limiting how much off-book scale Kissht can support without absorbing more first-loss risk |

### 1E. The chai-stall-uncle version

Kissht is like the neighbourhood moneylender who also runs a matchmaking
service for a bigger financier down the road. Sometimes he lends his own
cash to a regular customer and pockets the interest when it comes back.
Other times, he does not have (or does not want to risk) enough of his own
money, so he introduces the same customer to a bank or a fund with deeper
pockets, vouches for them, chases the monthly instalment, and takes a
finder's-and-collector's fee instead of interest. He only promises to cover
a small slice (0-5%) of the loss if that introduced customer runs away, so
most of the risk on those introduced loans sits with the bigger financier,
not with him. About half his book today is his own money out on loan, and
half is introduced business (IP1 p.38). He is good at figuring out who is
likely to repay — he uses machines and years of data instead of gut feel —
but he is not the only moneylender in town doing this, and he does not set
the price the big financiers charge him for his own borrowing.

### Section 1 summary table

| Business type | Revenue nature | Asset intensity | WC intensity | Pricing power |
|---|---|---|---|---|
| Lending (digital NBFC, PL + LAP) | Interest + fee income, mixed on/off-book | Medium | High (funding/balance-sheet intensity, not trade WC) | Weak / price-taker on both funding cost and lending rate |

---

## SECTION 2: INDUSTRY DYNAMICS & COMPETITIVE POSITION

### 2A. Five forces

| Force | Reading | Helps / Hurts / Neutral |
|---|---|---|
| Competition | At least four named digital-first NBFC peers (KreditBee/Finnov, Navi Finserv, Fibe/Social Worth, Moneyview/Whizdm) plus branch-based giants (Bajaj Finance, Cholamandalam, HDB Financial, SBI Cards) all chase the same mass-market unsecured-credit customer (RHP p.178-180) | Hurts — fragmented, well-funded, low switching cost for the borrower |
| Entry barriers | RBI NBFC registration + Digital Lending Guidelines + years of underwriting data are real but not scarce; four to five credible digital-first entrants already exist at meaningfully larger AUM than Kissht (RHP p.179 table) | Neutral-to-hurts — barrier keeps out amateurs, not well-capitalised rivals |
| Supplier power (funders) | 45+ on-book lending partners, but on an A-/Stable rating (mid-investment-grade) paying 14.16-14.45% average cost of borrowing (AR p.19-20; IP1 p.33); 99.8% of the subsidiary's NCD book rests on one parent guarantee (B02/B03 FLAG-CAPITAL-STRUCTURE) | Hurts — funders hold real pricing and covenant power; concentration in the guarantee structure is a single point of failure |
| Customer power / concentration | Individually small retail borrowers with no negotiating power on price, but low switching cost and high price-sensitivity in aggregate; repeat-customer share of AUM fell from 73% (FY25) to 49% (FY26) (AR p.7) | Hurts — falling repeat share suggests weakening customer stickiness even as the book grows |
| Substitutes | Credit cards, BNPL, other lending apps, informal credit | Hurts — many close substitutes for a ₹5-lakh unsecured ticket |

### 2B. Competitive positioning map (RHP p.179-180, company-commissioned "1Lattice analysis" — flagged as issuer-sourced, not independently verified in this container)

New-age digital-first peers, FY25 (₹ Cr):

| Company | AUM FY25 | AUM CAGR FY23-25 | PAT FY25 | PAT CAGR FY23-25 | RoAA FY25 |
|---|---|---|---|---|---|
| Kissht (OnEMI) | 4,086.64 | 79.53% (best) | 160.62 | 140.95% (best) | 4.80% (2nd best) |
| KreditBee (Finnov) | 10,102.00 | 47.49% | 473.00 | 125.52% | 5.33% (best) |
| Navi Finserv | 11,694.90 | 31.23% | 221.96 | -8.34% | 2.20% |
| Fibe (Social Worth) | 5,287.00 | 64.11% | 116.00 | 360.13% | 2.48% |
| Moneyview (Whizdm) | 16,715.14 | 47.87% | 240.28 | 21.57% | 1.62% |

Kissht is the SMALLEST of the five named digital-first peers by AUM but
grew fastest and earned the second-best RoAA. Every one of the four named
peers is already larger than Kissht — this is a "fastest, not biggest"
position, not an efficient-scale moat.

Larger, branch-based/listed comparables (RHP p.180, ₹ Cr, converted from
the RHP's ₹ billion table): Bajaj Finance FY25 AUM ~₹4,16,661 Cr (29.78%
CAGR), Cholamandalam ~₹1,84,746 Cr (27.99%), HDB Financial ~₹1,07,262 Cr
(23.71%), SBI Cards ~₹55,840 Cr receivables (17.10%). Kissht's ₹7,066 Cr
FY26 AUM (AR p.7) is roughly 1.7% the size of Bajaj Finance's FY25 book —
scale is nowhere near comparable, though growth rate is.

### 2C. Moat assessment (eight standard types)

| Moat type | Present? | Evidence | Durability |
|---|---|---|---|
| Brand | Partial | Sachin Tendulkar brand ambassador since ~2025 (AR p.9); "Admired Brands & Leaders", Forbes Asia 100 to Watch 2025 (AR p.20) | Low-Moderate — marketing-driven, replicable by any well-funded rival |
| Network effects | Weak | More loans train better underwriting models (10 Mn+ decisions used, IP1 p.22) — a data-flywheel, not a classic two-sided network | Moderate, if sustained investment continues |
| Switching costs | Weak | Repeat-customer AUM share FELL from 73% to 49% in one year (AR p.7) — the opposite of rising switching cost | Low, and weakening |
| Cost advantages | Absent | Average cost of borrowing 14.16-14.45% (AR p.19-20; IP1 p.33) is a mid-investment-grade rate, not a low-cost-funder rate; no evidence of a cost edge vs peers | None evidenced |
| Intangible assets (proprietary data/IP) | Present | 400+ underwriting variables, 40 deployed models, AUC improved 66%→74% (2023-2026), 2.5x risk separation vs raw bureau score (IP1 p.22-24) | Moderate — currently ahead of the disclosed bureau baseline, but rivals invest in the same class of models |
| Efficient scale | Absent | Smallest of five named digital-first peers by AUM (RHP p.179); ~1.7% of Bajaj Finance's book | None — a scale disadvantage, not an advantage |
| Regulatory/license moat | Weak | NBFC-ML registration (AR p.19) is real but not scarce — at least four comparable licensed digital-first NBFCs already compete (RHP p.179) | Low as a moat; more a cost of entry than a barrier that excludes credible rivals |
| Distribution/embedded reach | Partial | 45+ lending partners, 8+ off-book partners, merchant "credit QR" O2O acquisition, e-commerce integrations (AR p.19; IP1 p.13) | Moderate — real but replicable distribution breadth |

Overall moat read: THIN, concentrated almost entirely in the underwriting-
data/model stack, consistent with B01's independently computed moat_class
"THIN" (moat_score 4, 1 of the tested moats confirmed).

### 2D. Industry lifecycle stage

Growth stage. India's PL + LAP addressable market is projected to grow
from ₹31.9 Tn (FY25) to ₹77.4 Tn by FY30 (RHP p.174, 1Lattice/industry
estimate), and Kissht's own AUM has compounded from ~₹10 Cr (FY17) to
₹8,001 Cr (Q1 FY27, IP1 p.10) — a company still in its own steep scaling
phase within a still-scaling market, not yet a mature, consolidated
industry.

### 2E. Key industry drivers

| Driver | Direction | Impact on Kissht |
|---|---|---|
| Retail credit penetration (mass-market/aspirational segment) | Rising — market growing at ~20-22% CAGR to FY30 (RHP p.174) | Tailwind — core addressable market expanding |
| NBFC digital lending guidelines / DLG cap | Tightening compliance regime, cap 0-5% on off-book FLDG | Constrains how far the capital-light off-book model can scale without more first-loss exposure |
| Cost of funds / rate cycle | A-/Stable rating, 14.16-14.45% average cost of borrowing (AR p.19-20; IP1 p.33) | A rate cut cycle helps margin; the company does not control its own funding cost, unlike a bank deposit franchise |
| Competitive intensity among digital-first NBFCs | Rising — at least 4 comparable, larger peers (RHP p.179) | Caps pricing power on both funding and lending sides |
| Underwriting/AI investment race | Continuing — AUC improved 4pp in the latest model version alone (IP1 p.23) | Where the company is currently ahead; also where it must keep spending to stay ahead |

---

## SECTION 3: FINANCIAL METRICS THAT MATTER FOR THIS BUSINESS MODEL

### 3A. Ignore-these, track-these

| Commonly tracked ratio | Verdict | Why |
|---|---|---|
| Trade receivable / payable days, inventory turnover | IRRELEVANT | No inventory or trade receivables cycle; the loan book is the asset, funded by borrowings, not by suppliers |
| Gross margin % (COGS-based) | IRRELEVANT | No cost-of-goods-sold concept; the analogous input cost is finance cost (cost of funds), already isolated in the P&L |
| Cash conversion / CFO-to-PAT ratio, read as a manufacturer would | MISLEADING | Per B01, cumulative CFO is deeply negative (-2.46x cumulative PAT, FY21-26) purely because loan disbursals are classified as an operating cash outflow under Ind AS 7 for a fast-growing lender — a growth signature, not evidence of earnings-quality failure on its own |
| ROCE, as literally computed with finance cost added back to EBIT | MISLEADING | Per B01's own analyst note, this measure is structurally inflated for a lender (finance cost is the core cost of funds, not overhead) and should not be compared across archetypes |
| Fixed-asset turnover / capex-to-sales | IRRELEVANT | Asset-light, opex-driven cost structure (people, tech, collections); PP&E is a trivial share of the balance sheet |
| Debt-to-Equity vs a manufacturer's "safe" threshold (e.g., <1x) | MISLEADING | Lenders run leveraged balance sheets by design; D/E must be read against CRAR, gearing covenants and the guarantee structure (228% of parent net worth, B02/B03), not a manufacturer's comfort band |

### 3B. Must-track metrics

**Growth**

| Metric | Tells you | Healthy range | Where to find | Red flag threshold |
|---|---|---|---|---|
| AUM growth % YoY | Scale/momentum of the core business | 30-50%+ for a growth-stage digital NBFC (Kissht: +73% FY26, +61% Q1 FY27 YoY, AR p.7; IP1 p.5) | AR MD&A, quarterly IP | Sustained deceleration below ~15-20%, or a sharp one-quarter drop |
| Off-book AUM % (funding mix) | Capital efficiency vs FLDG/first-loss exposure taken on | 40-60% (Kissht: 50% FY26, 53.6% Jun-26, AR p.7; IP1 p.38) | AR MD&A, IP | >65% (FLDG cost escalation risk, per B02 FLAG-OFF-BALANCE-SHEET) or <30% (loses capital efficiency) |

**Profitability and efficiency**

| Metric | Tells you | Healthy range | Where to find | Red flag threshold |
|---|---|---|---|---|
| RoAAUM (PAT / avg AUM) | Whether growth is actually profitable | 4-6% for this segment (Kissht: 5.05% FY26, 5.0% Q1 FY27, AR p.35; IP1 p.7) | AR MD&A, IP | Below ~3%, or falling for two consecutive quarters |
| Cost-to-Income ratio | Whether opex scale benefits are materialising | Improving toward <50% | AR KPI table | Worsening trend (Kissht: 45.54%→56.64% FY24-26, per B01 FLAG-QUALITY, an ALREADY-FIRED flag) |
| Credit cost as % of avg AUM | Underlying loss rate before write-offs distort GNPA | <7-8% (Kissht: ~8.2% FY26 computed from AR MD&A figures, 6.8% Q1 FY27 annualized, IP1 p.41) | AR MD&A, IP DuPont table | Credit cost growth outpacing AUM growth in any quarter |

**Balance sheet and risk**

| Metric | Tells you | Healthy range | Where to find | Red flag threshold |
|---|---|---|---|---|
| GNPA / Stage-3 % (sequential) | Underlying asset quality, net of the write-off mechanic | Improving or flat | AR, quarterly IP | Any further sequential rise past 2.25% (already occurred, Q1 FY27 vs FY26, per B03 FLAG-GUIDANCE-DIVERGENCE) |
| Write-off rate % of avg book | Whether GNPA "improvement" is real or write-off-assisted | Stable, not rising faster than book growth | AR notes (per B02, ~15.7% FY26) | Rising alongside rising new-Stage-3 inflow (already true per B02) |
| Guarantee-to-parent-net-worth ratio | Concentration/capacity risk in the funding structure | A stated, bounded ceiling | AR notes (228% FY26, per B02/B03 FLAG-CAPITAL-STRUCTURE) | Any further rise; no ceiling currently disclosed |
| CRAR (subsidiary) | Regulatory capital cushion | Comfortably above the NBFC-ML minimum | AR, IP (25.28% FY26; 40.2% Jun-26 post preferential allotment) | Approaching the regulatory floor (not imminent, but the post-IPO capital-raise pattern itself is separately flagged, LBF-4) |

### 3C. Industry-specific non-financial KPIs

| KPI | Where to find |
|---|---|
| Collection efficiency (DPD 30) — 97.01% FY26, 96.82% Q1 FY27 | AR p.7; IP1 p.7 |
| Repeat-customer AUM % — 49% FY26 (down from 73% FY25) | AR p.7 |
| Customers served (cumulative) / active customers — 11.76 Mn / 3.25 Mn FY26; 12.25 Mn / 3.49 Mn Q1 FY27 | AR p.7; IP1 p.7 |
| Registered users — 68.55 Mn FY26, 74.60 Mn Q1 FY27 | AR p.7; IP1 p.25 |
| Median CIBIL score of borrowers — 746 | IP1 p.12 |
| Model AUC (underwriting discrimination) — 74% latest vs 66% baseline (2023) | IP1 p.23 |
| Digital collection share — 99.2% | AR p.7 (implied); IP1 p.26 |
| Lending partner count / off-book partner count — 45+ / 8+ | AR p.19-20; IP1 p.9 |
| LAP branch count — 98 (AR, Mar-26) / 101 (IP1, Jun-26) | AR p.9; IP1 p.9 |

### 3D. Unit economics — the physics of the business

Define the unit as ₹100 of average AUM (the natural unit for a mixed
on/off-book lender; a per-loan unit would obscure the on-book/off-book
split). Built from the AR MD&A FY26 P&L (AR p.35) against average AUM of
₹5,576.5 Cr (average of ₹7,066 Cr FY26 and ₹4,087 Cr FY25 AUM, AR p.7):

| Line | ₹ per ₹100 avg AUM, FY26 (computed) | Q1 FY27 (disclosed, annualized, IP1 p.41) |
|---|---|---|
| Total income | 39.6 | 35.9 |
| Finance cost | 5.1 | 4.3 |
| Net total income | 34.6 | 31.6 |
| Operating expenses | 19.6 | 18.0 |
| Pre-provisioning operating profit | 15.0 | 13.6 |
| Credit cost | 8.2 | 6.8 |
| Profit before tax | 6.8 | 6.8 |
| Profit after tax | 5.0 (matches disclosed RoAAUM 5.05%, cross-check) | 5.0 |

Neither a standalone lending YIELD % nor a standalone COST OF FUNDS % (in
the classic NIM/spread sense) is disclosed anywhere in this container —
NOT FOUND. The "Total income / avg AUM" and "Finance cost / avg AUM" lines
above are the closest disclosed proxies, but Total income nets in fee
income (sourcing/servicing, insurance, penal charges) alongside interest,
so it is not a pure lending yield. The Q1 FY27 figure sitting below the
FY26 full-year figure (35.9% vs 39.6%) is directionally consistent with
the mix shift toward off-book (lower-yield-per-rupee-of-AUM) business
documented in Section 1C, and is separately consistent with the CEO
letter's own statement that yields/costs are expected to keep compressing
as AUM scales (IP1 p.5).

- Volume driver: disbursement growth, active-customer growth, repeat-loan frequency.
- Price driver: an algorithmic, risk-based APR set per customer/segment (no rate card disclosed); off-book fee-share is partner-negotiated.
- Cost drivers: cost of borrowing (14.16-14.45%, AR/IP1), credit cost (~8.2% FY26), and opex (19.6% of avg AUM — staff, collections infrastructure, technology).
- Incremental margin / operating leverage: management explicitly expects opex and cost of borrowing, as a % of average AUM, to fall as the book scales (IP1 p.5, "Disciplined Priorities"). The disclosed record so far runs the OPPOSITE way: Cost-to-Income ratio worsened from 45.54% to 56.64% between FY24 and FY26 even as PAT grew (per B01 FLAG-QUALITY). Operating leverage is a claimed, not yet evidenced, feature of this model.

---

## SECTION 4: RISKS, VALUATION APPROACH & MONITORING

### 4A. Business-model-specific risks

| Category | Risk | First line item to deteriorate |
|---|---|---|
| Revenue model | Off-book partner concentration — only 8+ partners carry 53.6% of AUM (IP1 p.38) | Sourcing-and-servicing fee growth decelerating faster than AUM growth |
| Margin | Cost of borrowing rises or the credit rating stalls short of an upgrade | Average cost of borrowings % (AR/IP1 disclosed line) ticking up quarter-on-quarter |
| Balance sheet | Parent corporate guarantee to Si Creva's lenders already at 228% of parent net worth, rising every year since FY24 (B02/B03 FLAG-CAPITAL-STRUCTURE) | Guarantee-to-net-worth ratio disclosed in the next AR's notes rising further, or a rating-agency query on the same |
| Execution | GNPA improvement substantially a write-off-rate artefact (B02/B03); Q1 FY27 GNPA already rose sequentially against "further strengthen asset quality" guidance | Any further sequential GNPA/Stage-3 rise in the next quarterly print |
| Structural | RBI tightens Digital Lending Guidelines / DLG caps or raises risk weights on unsecured retail credit (a precedent exists industry-wide) | A new RBI circular naming DLG/co-lending caps or unsecured-PL risk weights, or a sudden slowdown in off-book partner sanction |

### 4B. Valuation method applicability

| Method | Applicable? | Notes |
|---|---|---|
| P/B (Price-to-Book / P/ABV) | PRIMARY | Sector cap row for Banks/NBFCs/MFIs (B00) names P/B primary; ties the demonstrated RoAE (23.97% FY26, AR p.35) and near-4x net-worth growth since Mar-23 (IP1 p.36) to a sustainable book-value multiple |
| PE (cross-check) | SECONDARY | Two years of clean, restated profitability (FY25-FY26) allow a cross-check of the P/B-implied multiple against an earnings multiple and the disclosed AUM/PAT growth trajectory |
| Residual income / excess-return model (RoE vs cost of equity) | TERTIARY | Makes explicit whether the 23.97% RoAE durably clears the cost of equity — useful discipline given the P/B primary method, not a standalone driver |
| DCF | NOT APPLICABLE | Cash flow history is short (listed since May 2026), and CFO is structurally negative under Ind AS 7 loan-growth classification (B01), making multi-year FCF forecasting unreliable at this stage |
| EV/EBITDA | NOT APPLICABLE | EBITDA is not a meaningful metric for a financial firm whose core "input cost" is finance cost, not an operating cost line above the EBITDA line |
| SOTP / NAV | NOT APPLICABLE | Single core lending business; LAP is still nascent (7.3-7.7% of AUM) and not yet a separable segment |

Cycle stage that matters for valuation: an early-stage, still-scaling
NBFC inside a benign-but-turning credit cycle — collection efficiency is
still high (~97%, AR/IP1) but GNPA has already posted one sequential
increase (Q1 FY27 vs FY26, per B03), the first data point in what could
be either noise or an early cycle inflection.

### 4C. Quarterly monitoring checklist (10-15 items)

1. AUM growth % YoY and QoQ (good: sustained 40%+; trouble: sharp deceleration)
2. On-book vs off-book AUM mix % (good: stays in the 40-60% off-book band; trouble: off-book share keeps rising past 60% without a stated FLDG ceiling)
3. GNPA / Stage-3 % sequential move (good: resumes falling; trouble: further sequential rise after Q1 FY27's uptick)
4. NNPA % and Provision Coverage Ratio (good: PCR stable/rising; trouble: PCR falling while GNPA rises)
5. Write-off rate as % of average book (good: stable or falling alongside slowing new-Stage-3 inflow; trouble: still rising faster than AUM)
6. Credit cost as % of average AUM (good: falling or flat; trouble: growth outpacing AUM growth)
7. Cost-to-Income ratio (good: resumes improving; trouble: continues worsening past 56.64%)
8. Average cost of borrowings % (good: stable/falling with rating upside; trouble: rising)
9. RoAAUM and RoAE (good: sustained near current 5.0%/24% levels; trouble: falling for 2+ consecutive quarters)
10. Guarantee-to-parent-net-worth ratio, next disclosed (good: a stated ceiling near or below 228%; trouble: further rise with no ceiling)
11. Repeat-customer AUM % (good: stabilises or recovers from 49%; trouble: continues falling)
12. CRAR / Tier-1 ratio (good: comfortably above the regulatory floor; trouble: approaching it)
13. Off-book partner count and concentration (good: broadening beyond 8+; trouble: further concentration)
14. Management overlay ECL as % of total ECL (good: shrinking as models mature; trouble: stays large and static, per B02 rank-7 finding)
15. LAP ticket-size/tenure disclosure consistency across filings (good: a single reconciled figure appears; trouble: the AR/IP1/CRISIL discrepancy persists unexplained)

### 4D. Highest-value questions for management

1. What specific DPD threshold triggers a loan write-off, and why does no numeric trigger appear in the AR despite qualitative write-off language? — Reassures: a clear, disclosed, industry-standard trigger (e.g., 150 DPD as company memory suggests). Worries: no fixed policy, i.e., write-off timing is discretionary.
2. What ceiling, if any, governs the parent's corporate guarantee to Si Creva's lenders as a % of the parent's own net worth, now at 228% and rising every year since FY24? — Reassures: an explicit ceiling with a de-risking roadmap. Worries: "as needed," with no stated limit.
3. Why did the Cost-to-Income ratio worsen from 45.54% to 56.64% (FY24-26) even as AUM grew 73%, when the CEO letter states opex/AUM should fall with scale? — Reassures: identifiable one-off investment now amortizing. Worries: the claimed operating leverage is structurally not showing up.
4. What is the company's actual lending yield and cost-of-funds split (an explicit NIM), given neither is disclosed as a standalone percentage anywhere in this container? — Reassures: a disclosed NIM comparable to peers. Worries: continued non-disclosure, forcing reliance on blended proxies.
5. Why did repeat-customer AUM share fall from 73% (FY25) to 49% (FY26) in one year — a strategic shift toward new customers, or a retention weakness? — Reassures: a deliberate diversification strategy with stable renewal economics. Worries: existing customers churning to competitors.
6. Which loan-against-property ticket size and tenure is correct — the AR's "up to ₹30 lakh / 15 years" (AR p.9), the Q1 FY27 deck's "up to ₹15 lakh / 10 years" (IP1 p.11), or CRISIL's "up to ₹20 lakh / 10 years" (rating rationale)? — Reassures: a simple, explainable policy change over time. Worries: inconsistent internal risk-parameter disclosure across three filed documents.
7. What is the FY27 credit-cost/GNPA glide path, given Q1 FY27 GNPA already rose sequentially against the "further strengthen asset quality" guidance? — Reassures: a seasonal blip, full-year target still on track. Worries: guidance is already off-track one quarter in.

---

## SECTION 5: ONE-PAGE BUSINESS MODEL SUMMARY CARD

```
COMPANY: OnEMI Technology Solutions Ltd (Kissht) | TICKER: KISSHT
ARCHETYPE: Lender (digital NBFC — unsecured PL + secured LAP)
BUSINESS TYPE: Lending (mixed on-book / off-book model)

REVENUE MIX (FY26, consolidated, Note 23, AR p.118-119):
  Interest on loans (on-book) ................. 58.4%
  Sourcing and servicing fees (off-book) ....... 26.6%
  Other fees and charges (penal/foreclosure) ... 11.1%
  Insurance commission and rewards ............. 3.2%
  Marketing and commission income .............. 0.7%

SCALE: AUM ₹8,001 Cr (Jun-26, IP1) | On-book 46.4% / Off-book 53.6%
       PL 92.3% of AUM / LAP 7.7% of AUM (IP1 p.39)

PROFITABILITY: RoAAUM 5.0% | RoAE 21.2-24.0% | Cost-to-Income worsening
               (45.54% -> 56.64%, FY24-26, B01 FLAG-QUALITY)

ASSET QUALITY: GNPA 2.25% (Q1 FY27, up 13bps sequentially) | NNPA 0.36%
               Write-off rate ~15.7% of avg book (B02) — GNPA improvement
               is substantially a write-off-rate artefact, not a clean
               underwriting signal (B02/B03)

CAPITAL: CRAR 40.2% (post preferential allotment, Jun-26) | D/E 0.91x
         (on-book, post-capital-raise) | Guarantee-to-parent-net-worth
         228% (FY26), a single-point-of-failure funding concentration
         (B02/B03 FLAG-CAPITAL-STRUCTURE)

MOAT: THIN (B01 moat_class). Strongest evidenced element is the
      underwriting-data/model stack; brand, switching cost, cost
      advantage and scale are absent or weak.

PRICING POWER: Weak / price-taker on both funding cost and lending rate.

VALUATION: PRIMARY P/B | SECONDARY PE cross-check | TERTIARY residual
           income (RoE vs cost of equity) | DCF/EV-EBITDA/SOTP N/A

ONE-LINE VERDICT: Fast-growing digital lender priced on AUM momentum;
earnings quality still turns on an undisclosed write-off trigger and an
over-stretched parent guarantee, not on a durable competitive moat.
```
