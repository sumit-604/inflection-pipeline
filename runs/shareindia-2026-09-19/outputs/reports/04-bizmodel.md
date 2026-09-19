# STAGE 4 — BUSINESS MODEL DECODER
## Share India Securities Ltd (SHAREINDIA), Phase 1 run 2026-09-19

Sources used: SHAREINDIA-AR-FY26.txt (AR, MD&A Annexure-3, BRSR Annexure-7,
Note 45 segment reporting, Statement of P&L, Board's Report), investor
presentations Q1 FY27 (2026-07-27), Q4 FY26 (2026-05-20), Mar-2026 deck;
company memory (companies/SHAREINDIA.md, step1-business-brief.md, weighed
never anchored); prior blocks B00-B03 (weighed for consistency, not
re-anchored).

---

## SECTION 1: THE BUSINESS MODEL IN PLAIN ENGLISH

### 1A. One-line description

Share India is a Noida-based, technology-driven capital-markets group that
makes most of its money trading its own account in derivatives, and the
rest from broking, margin lending, and small fee businesses bolted on
around that core (AR p.71, Company Overview).

### 1B. Money flow chain, one chain per revenue stream

| # | Stream | Input | What the company does | What it delivers | Who pays | How they pay |
|---|---|---|---|---|---|---|
| 1 | Proprietary trading ("Net gain on fair value changes") | The company's own capital plus borrowed margin | Runs algorithmic strategies (Algowire, Silverleaf) across equity, F&O and commodity exchanges, holding "Securities held for trading" as its own book | Realised and mark-to-market trading gains | The market (counterparties on the other side of each trade); no external "customer" | Booked as fair-value gain/loss straight to the P&L (Note 31 consol; AR p.72, KAM disclosure) |
| 2 | Client broking (fees and commission income) | Client orders routed through the platform | Executes trades, provides research, IPO access, advisory | Trade execution and access | Retail, HNI, corporate and institutional clients | Per-trade brokerage and commission, deducted from settlement (Note 30 consol) |
| 3 | Margin Trading Facility / NBFC lending (interest income) | Company/NBFC own funds plus borrowings | Lends against securities (MTF) or personal/SME loans (Share India Fincap) | Leveraged buying power for clients | Borrowers (MTF clients, NBFC loan clients) | Interest on the outstanding book (Note 28 consol; MTF book Rs 402.61 Cr standalone, AR p.74) |
| 4 | Depository, distribution, merchant banking, insurance, PMS (fees and commission, sale of services) | Regulatory registrations (DP, merchant banker, AMFI, insurance broker) | Account maintenance, mutual fund and insurance distribution, IPO advisory, PMS | Access to products and advisory | Clients and, for merchant banking, issuer companies | Fixed/variable fees, trail commission (AR p.74-75) |
| 5 | Sale of products (stock-in-trade securities, gross) | Securities purchased as inventory | Buys and resells securities classified as stock-in-trade (distinct from the FV-through-P&L trading book) | Executed sale of securities | The market | Gross sale proceeds recognised as revenue, cost as "Purchases of stock-in-trade" (Note 32/38 consol) |

### 1C. Revenue model classification table (consolidated, FY26)

All figures anchored to the Consolidated Statement of Profit and Loss
(AR p.229/printed 226) and Note 45 Segment Reporting (AR pp.286-287,
printed 289-290). Amounts in Rs Lakh.

| Stream | Type | FY26 amount | % of total income (Rs 1,48,884.97 Lakh) | FY25 amount | Predictability |
|---|---|---|---|---|---|
| Net gain on fair value changes (proprietary trading) | Trading gain, mark-to-market and realised | 86,730.03 | 58.3% | 88,758.57 | LOW — swings with market direction and volatility, no client contract behind it |
| Interest income (MTF + NBFC + deposits, undifferentiated in this note) | Spread/interest income | 27,444.66 | 18.4% | 22,419.39 | MEDIUM — recurring while the book stays funded, but the note does not split MTF vs NBFC vs treasury interest |
| Fees and commission income | Fee/commission | 16,518.37 | 11.1% | 20,306.56 | MEDIUM, but FELL 12.7% standalone / 18.6% consol in FY26 (AR p.74 ratio table; B03 finding) — the "client-led" line moved the wrong way |
| Sale of products (stock-in-trade securities, gross) | Trading inventory turnover | 13,731.45 | 9.2% | 10,278.93 | LOW — same trading-book economics as the fair-value line, reported gross |
| Dividend income | Portfolio yield | 1,636.87 | 1.1% | 2,173.64 | LOW — depends on holdings and payout timing |
| Sale of services | Fee/service | 964.20 | 0.6% | 919.75 | MEDIUM |
| Other income | Non-operating | 1,859.39 | 1.2% | 2,093.25 | LOW |

Cross-check, BRSR Annexure 7 (standalone basis, p.84/printed 84-85, "90% of
turnover" test): Trading in Securities 73.47% of turnover, Stock Broking
Services (incl. depository and distribution) 15.19%. This is a TURNOVER
split, not a revenue-recognition split, and it is standalone-only; it is
wider than the 58.3% P&L figure because it likely includes the gross
"Sale of products" trading-inventory line inside "Trading in Securities."
Read together the two disclosures triangulate to the same conclusion:
LBF1 answer — the company is a proprietary trading business first. Both
the BRSR activity split and the P&L revenue split, taken from filed
primary statements, contradict the MD&A's own claim of "reducing
dependence on proprietary trading" in the same document (AR p.74 MD&A
Outlook vs AR p.84 BRSR; B03 red flag #2).

Segment-level cross-check (Note 45 consol, AR pp.286-287): "Share
broking/trading business" is reported as ONE segment and is 93.2% of
FY26 segment revenue (Rs 1,38,784.39 Lakh of Rs 1,48,884.97 Lakh) and
93.4% of profit before tax and finance charges (Rs 53,389.97 Lakh of Rs
57,171.86 Lakh). NBFC is 3.7% of revenue / 4.4% of segment profit,
merchant banking 1.6%/1.5%, insurance 0.6%/0.2%, technology services
0.9%/0.6%. The segment note is structurally unable to separate prop
trading from client brokerage inside that one line (confirms B02 finding
1); the P&L revenue-line breakdown above is the best available proxy,
and it still cannot separate PROFIT (only revenue) between prop and
client, because expenses are not allocated by revenue line.

Investor-presentation cross-check (Q1 FY27 deck, p.3/printed slide 5):
segmental revenue split (not product-level) shown as Broking & Trading
94.47%, NBFC 3.23%, Merchant Banking 1.11%, Insurance 0.37%, Technology
Services 0.82% — consistent with the AR segment note's concentration
finding but at the same coarse (segment, not product) resolution.

### 1D. Simplified business model canvas

| Dimension | Answer |
|---|---|
| What they sell | Trade execution, leveraged capital (MTF/NBFC), algorithmic trading software, and its own trading skill deployed with its own balance sheet |
| Who buys | Retail/HNI/institutional traders (broking, MTF), SME/retail borrowers (NBFC), issuers (merchant banking), no one — for the prop book, the "buyer" is the market itself |
| Why them | Technology stack (Algowire, Silverleaf, uTrade), 31 years of exchange membership and infrastructure, one of few Indian brokers running its own large prop book alongside client business (AR p.71) |
| How delivered | Digital trading platforms, 95 branches/franchises (standalone, AR p.74) plus API/algo access |
| Cost structure dominance | Employee benefits (Rs 35,967 Lakh, 34.3% of consol expenses) and finance costs (Rs 13,125 Lakh, 12.5%) dominate; the trading book itself carries no separate "cost of goods," its cost is capital and risk (Note 35, 39 consol) |
| Scarce resource | Exchange trading memberships/NBFC registration (regulatory scarcity) and the proprietary algo/tech stack, not a physical asset |
| Pricing power source or absence | NONE on the trading book (a price-taker against the market); WEAK on brokerage (commoditised, fee income fell YoY); the NBFC book prices on credit risk, not brand |
| Asset intensity | HEAVY — the trading book, MTF book and margin deposits pledged to exchanges are all balance-sheet assets; segment assets Rs 4,58,986 Lakh consol (Note 45) |
| WC intensity | HIGH and DETERIORATING — debtor turnover fell 29.8% standalone / 34.2% consol FY26 (AR p.74 ratio table), funded by new debt/NCDs rather than retained cash (B02/B03 FLAG-CASH) |
| Regulatory moat or burden | BOTH — SEBI broker/DP/merchant-banker registration and RBI NBFC registration are entry barriers, but the same regulator's F&O curbs and margin rules are a direct earnings threat to the largest revenue line |

### 1E. The chai-stall-uncle version

Imagine a chai stall that also runs a small side business betting on
cricket odds with its own savings. Most days the cricket bets make more
money than the tea. The stall tells customers it is "reducing its
dependence on cricket betting and growing the tea business," but this
year tea sales actually fell and the betting book stayed the biggest
earner. To place bigger bets, the stall owner also started borrowing
money, and pledged some of his own house papers as collateral. That, in
one sentence, is Share India: a broker whose biggest profit engine is its
own trading book, not its customers' trades, funded increasingly by debt
while its stated strategy of growing the "tea" (client, fee-based)
business has not yet shown up in the numbers.

### Section 1 summary table

| Business type | Revenue nature | Asset intensity | WC intensity | Pricing power |
|---|---|---|---|---|
| Hybrid: proprietary trader + broker-dealer + NBFC lender + fintech platform | Majority trading-gain/mark-to-market (58.3% of FY26 income), balance interest and fees | Heavy | High, deteriorating | Weak to none on the core trading/broking lines; NBFC prices on credit risk |

---

## SECTION 2: INDUSTRY DYNAMICS AND COMPETITIVE POSITION

### 2A. Five forces, plainly

| Force | Answer | Effect |
|---|---|---|
| Competition count | Large field: full-service and discount brokers (Angel One, Zerodha, Groww, ICICI Securities), other broker-cum-prop-trading houses named in company memory as structural peers (SMC Global, Choice International), plus fintech entrants (AR p.72-73, "Competition Risk") | HURTS — brokerage is commoditised and rivalry is named explicitly as a threat in the MD&A |
| Entry barriers | SEBI broker/DP/merchant-banker registration, exchange membership, RBI NBFC registration, capital adequacy/net worth requirements (AR p.74, "Company maintains modest debt... standalone net worth of Rs 2,187.26 Cr") | HELPS moderately — regulatory registration is not trivial, but many licensed players already compete |
| Supplier power | "Suppliers" are the exchanges (NSE/BSE/MCX) that set transaction and margin-guarantee terms, and capital markets that set the cost of the company's own borrowing (finance costs rose to Rs 131 Cr FY26 per company memory) | HURTS — the company does not control exchange fee or margin-guarantee terms, and rising contingent liabilities to exchanges (Rs 3,233 Cr FY26, +48% YoY, B02 finding 6) show this dependency growing faster than revenue |
| Customer power and concentration | Retail/HNI/institutional clients can move brokers with low switching cost; institutional client base is small in absolute terms (186 clients, AR p.74) though growing | HURTS — no disclosed single-client concentration, but the diffuse retail base has no lock-in and fee income already fell |
| Substitutes | Discount brokers, direct-to-exchange algo access, other NBFCs for MTF-like leverage, mutual funds/PMS from other providers | HURTS — the MD&A itself names "changing client preferences towards passive strategies and online platforms" as a threat (AR p.73) |

### 2B. Competitive positioning map

Documents in this run do not carry head-to-head market-share or pricing
data against named competitors. Per company memory (weighed, not
anchored), the closest structural peers are SMC Global Securities
(broking + prop trading + NBFC + insurance, similar diversified mix) and
Choice International (broking + NBFC + advisory, already re-rated as a
"fintech transition" story); Angel One is named as the F&O retail-volume
read-across for the SEBI derivative curbs. None of these comparisons are
anchored to this run's corpus; NOT FOUND IN AR/PRESENTATION, check
concalls or peer filings for a quantified positioning comparison.

### 2C. Moat assessment (eight standard types)

| Moat type | Evidence | Durability |
|---|---|---|
| Brand | Chairman's letter and MD&A cite "31+ years of trust" (AR p.71) but no disclosed brand-tracking or premium pricing evidence | WEAK / unproven |
| Network effects | uTrade platform subscriptions (72,507 total, 6,543 paid, Q1 FY27 deck p.3) show scale but not evidenced network effects (value to one user rising with more users) | WEAK, not demonstrated |
| Switching costs | None disclosed; brokerage/MTF/NBFC lending all face standard portability | ABSENT |
| Cost advantage | Not evidenced at the trading-book level; NBFC NIM 17.64% FY26 (AR p.74) is a margin figure, not a proven cost-curve advantage over peers | NOT FOUND / unproven |
| Regulatory / licence moat | SEBI broker-dealer, merchant-banker, DP and RBI NBFC registrations are real entry barriers | MODERATE — barrier is real but shared with all similarly licensed peers, not exclusive |
| IP / technology | Proprietary algo stack (Algowire low-latency execution, Silverleaf quant research, uTrade retail algo platform), "18 years of algorithmic trading expertise" claimed (AR p.72) | MODERATE, self-asserted; no independent verification of technology superiority in this corpus |
| Scale / distribution | 95 branches (standalone, AR p.74) / 225 branches and franchises (consol, Q1 FY27 deck), pan-India across 19 states | MODERATE, but B01 flags NBFC branch count fell (80 to 73, AR p.74) and the broking branch base is not YoY comparable (B01 M8) |
| Capital / balance-sheet strength | Standalone net worth Rs 2,187.26 Cr cited as a moat (AR p.74) | UNDERCUT by the same year's negative CFO and rising contingent liabilities (B02/B03 FLAG-CASH); a capital moat funded increasingly by debt is not the same as a capital moat funded by retained earnings |

No moat here is confirmed strong and durable on the evidence in this
corpus; the strongest candidate (regulatory/licence) is shared with
peers, and the self-cited capital-strength moat is contradicted by the
FY26 cash-flow and leverage trend documented in B02/B03. This is a
finding, not a gap to smooth over.

### 2D. Industry lifecycle stage and position

The Indian capital-markets and broking industry is in a GROWTH phase
(demat accounts ~22.45 crore, NSE trading accounts >26 crore, mutual fund
AUM crossing Rs 73 lakh crore, AR pp.72-73, Industry Overview), but
undergoing REGULATORY TIGHTENING specific to derivatives (SEBI F&O curbs,
per company memory, not directly named as a risk in the MD&A risk table —
B03 "missing risks" finding). Share India sits as a mid-sized, diversified
player within this growth industry, positioned as much on its own trading
book's fortunes as on industry-wide client growth.

### 2E. Key industry drivers

| Driver | Direction | Impact on Share India |
|---|---|---|
| Retail demat account growth | Positive but decelerating (net additions down ~21% YoY, AR p.73) | Slower tailwind for the client-facing broking/NBFC lines |
| Financialisation of savings, digital adoption | Positive, structural | Supports MD&A's stated growth verticals (PMS, wealth, AIF) |
| SEBI derivative-market regulation (F&O curbs, weekly-expiry rationalisation) | Negative for volume-linked and prop revenue | Directly threatens the 58.3%-of-income trading line; not named in the AR's own risk table (B03 missing-risk finding) |
| Interest rate environment (RBI repo 5.25%, neutral stance, AR p.72) | Neutral to mildly negative | Higher-for-longer rates raise the company's own finance costs (Rs 131 Cr FY26 per company memory) on a balance sheet already funding growth with debt |
| Market volatility / FPI flow direction | Ambivalent | Volatility can help or hurt a prop-trading book depending on positioning; FPI outflows (AR p.73) are a broader sentiment headwind |

---

## SECTION 3: FINANCIAL METRICS THAT MATTER FOR THIS BUSINESS MODEL

### 3A. Ignore-these-track-these

| Commonly tracked ratio | Verdict | Why |
|---|---|---|
| Gross margin / OPM as if it were a manufacturer's margin | MISLEADING | The largest "revenue" line (net fair-value gain) has no matching cost-of-goods; margin ratios conflate trading-book economics with fee-business economics |
| Inventory turnover | IRRELEVANT | Structurally NA in the AR's own ratio table (p.74: "Inventory Turnover (in days) NA NA") — there is no physical inventory |
| Current ratio, as a liquidity signal | MISLEADING for this business | Ind AS financial-services presentation is liquidity-ordered, not current/non-current split (B01 D4 finding); the disclosed 1.89x/2.04x figures (AR p.74) are the SEBI-mandated ratio format, not a working-capital signal in the manufacturing sense |
| Revenue growth alone, without a prop/client split | MISLEADING | Revenue can rise or fall purely on trading-book mark-to-market swings unrelated to franchise growth (FY26 consol revenue +1.5% while fee income fell double digits) |
| Standard D/E as the sole leverage read | INCOMPLETE | D/E of 0.25x looks low (AR p.74), but contingent liabilities (exchange guarantees) at Rs 3,233 Cr are 122.7% of net worth (B01 E4) and sit off this ratio entirely |

### 3B. Must-track metrics

**Growth**

| Metric | What it tells you | Healthy range | Where to find it | Red flag threshold |
|---|---|---|---|---|
| Fees and commission income growth | Whether the "client-led" strategy is actually working | Positive, ideally double-digit | Consol/standalone P&L (Note 30) | Negative for 2+ consecutive years (already -12.7%/-18.6% FY26, AR p.74) |
| MTF book growth and client count | Client-side leverage franchise health | Steady growth without asset-quality slippage | AR MD&A operational review; quarterly presentations | Growth funded entirely by new debt with no NII improvement |
| Institutional client count | Wallet-share/franchise depth | Consistent quarter-on-quarter additions | Investor presentation (212 clients Q1 FY27, up from 186 FY26) | Flat or declining for 2+ quarters |

**Profitability and efficiency**

| Metric | What it tells you | Healthy range | Where to find it | Red flag threshold |
|---|---|---|---|---|
| Prop trading gain as % of total income | How much of profit is market-direction dependent vs franchise-earned | Declining trend if the stated strategy is real | P&L revenue note (Note 31 consol); this run: 58.3% FY26 | Rising, or flat despite stated diversification strategy |
| NBFC NIM and GNPA/NNPA | Whether lending diversification is credit-sound | NIM sustaining ~17%+, GNPA/NNPA stable or improving | AR p.74; quarterly presentations (GNPA 4.05%, NNPA 2.26% Q1 FY27 deck) | GNPA rising alongside book growth |
| Segment profit concentration (parent vs subsidiaries) | Whether the diversification story shows up in earnings | Subsidiary/segment share rising | Note 62 consol (Additional Info per Schedule III) | Parent share of profit rising (92.03% FY26 vs 75.28% FY25, B02 finding 2) — ALREADY A RED FLAG |

**Balance sheet and risk**

| Metric | What it tells you | Healthy range | Where to find it | Red flag threshold |
|---|---|---|---|---|
| CFO / PAT | Whether reported profit converts to cash | Positive and >0.5x on a multi-year view | Cash flow statement (AR pp.134, 230-231) | Negative (already -0.55x standalone / -0.56x consol FY26; negative in 3 of last 4 years, B01/B02) |
| Contingent liabilities / net worth | Off-balance-sheet guarantee exposure to exchange margin calls | Stable, growing in line with revenue | Note 44 consol / Note 42 standalone | Rising faster than revenue (already 122.7% of net worth, +48% YoY, B01 E4) |
| Promoter pledge % of promoter holding | Solvency stress signal at the promoter level | Falling or near zero | BSE SHP summary (not the AR itself — AR's own shareholding table does not disclose pledge %, B03 gap) | Rising (52.16% Sep-25 to 57.80% Jun-26 per company memory/BSE data, LBF2) |
| Debt/working capital and debtor turnover days | Funding-structure and receivables efficiency | Stable | AR p.74 SEBI ratio table (Note 58a/63a) | Deteriorating >25% YoY (already flagged: long-term debt/WC up 4.7x standalone, debtor turnover down 29.8% standalone) |

### 3C. Industry-specific non-financial KPIs

| KPI | Where to find it |
|---|---|
| Average daily turnover (ADTO) | AR p.74 (Rs 9,293 Cr standalone FY26); investor presentation (Rs 90 Bn consol, Q1 FY27) |
| Broking client count and institutional client count | AR p.74; quarterly presentations |
| Algo platform subscriptions (total and paid) | AR p.74 (71,062 subscriptions, 5,000+ paid, FY26); Q1 FY27 deck (72,507 / 6,543) |
| MTF AUM | AR p.74 (Rs 402.61 Cr standalone FY26); presentation (INR 4,655 Mn consol Q1 FY27) |
| NBFC branch count, client count, GNPA/NNPA/NIM | AR p.74; quarterly presentations |
| Merchant banking IPO listings (SME and mainboard) | AR p.74-75 (22 SME IPOs cumulative, 1 mainboard DRHP filed) |
| Insurance lives covered, premium collected | AR p.74; presentation |
| PMS AUM | AR p.75 (>Rs 100 Cr, target Rs 200 Cr FY27) |

### 3D. Unit economics — the physics of the business

The business has no single clean "unit" because it runs at least three
different economic engines simultaneously.

| Engine | Unit | Revenue per unit | Cost per unit | Volume driver | Price driver | Incremental margin / operating leverage |
|---|---|---|---|---|---|---|
| Proprietary trading | One trade/position on the firm's own book | Realised + unrealised P&L on that position (no fixed "price") | Capital cost (funding), technology/data cost, exchange margin/guarantee cost | Market volatility and available capital | Market price movement, not set by the company | HIGH operating leverage on the tech platform, but P&L itself is NOT a function of volume discipline — it can go negative; this is the least controllable engine in the model |
| Client broking | One executed trade | Brokerage/commission per trade (rate not disclosed in this corpus; NOT FOUND, check tariff sheet or concall) | Exchange transaction charges, platform cost, client acquisition cost | Number of active clients x trading frequency | Competitive brokerage-rate pressure (industry-wide race to zero/discount pricing) | Moderate — fixed platform cost spread over more trades, but fee income already fell FY26 despite client-count growth |
| MTF / NBFC lending | Rs 1 of book outstanding | Interest income (NIM 17.64% NBFC FY26, AR p.74) | Cost of funds, credit losses (GNPA 4.30% FY26 AR p.74) | Client demand for leverage, disbursement pace | Spread over cost of funds, some competitive pressure from other MTF providers | Moderate — scales with book size but credit risk scales too; NBFC segment revenue and EBIT both fell FY26 despite book growth (Note 45; B02 finding 15) |

The single most important physics fact for this name: the model's
BIGGEST revenue line (proprietary trading, 58.3% of income) has no
"volume x price" unit economics at all in the normal sense — it is a
risk position, not a repeatable transaction. Any valuation or projection
that treats total revenue as if it behaves like a client-fee business
will misprice the volatility embedded in the majority of the income
statement.

---

## SECTION 4: RISKS, VALUATION APPROACH AND MONITORING

### 4A. Business-model-specific risks

| Category | Risk | First financial line item that would deteriorate |
|---|---|---|
| Revenue model | Regulatory curbs on F&O trading directly compress the volume/positions behind the "net gain on fair value changes" line | Net gain on fair value changes (Note 31 consol) turning down sharply quarter over quarter |
| Revenue model | Stated shift to client/fee business fails to materialise (already the case in FY26: fee income -12.7%/-18.6%) | Fees and commission income (Note 30 consol) |
| Margin | NBFC book growth outpaces underwriting discipline (impairment allowance rose 58.9% FY26 per B02, on a book that stayed "always Stage-1") | Impairment on financial instruments (Note 37 consol) and NBFC segment EBIT (Note 45) |
| Balance sheet | Contingent liability/exchange-guarantee growth continues to outpace revenue, straining pledged FD collateral | Contingent liabilities note (Note 44 consol) and pledged fixed deposits |
| Balance sheet | Cash conversion stays negative a fourth year, forcing further debt/NCD reliance | Cash flow from operations (Statement of Cash Flows) |
| Execution | NCD early-redemption and rating-cooperation stress (Sep-2026 Infomerics downgrade under ISSUER NOT COOPERATING) impairs future debt access or raises cost of funds | Finance costs (Note 35 consol) and debt-service coverage ratio |
| Structural | Parent profit concentration keeps rising (92.03% FY26) instead of the diversification thesis showing up, meaning the group IS effectively a single-line prop/broking bet dressed as a conglomerate | Segment profit mix (Note 45) and Note 62 profit-attribution table |

### 4B. Valuation method applicability (formal handoff to Role 1)

| Method | Applicable? | Why |
|---|---|---|
| DCF | LOW applicability as primary | The dominant cash flow (prop trading gains) is not a stable, forecastable operating cash flow; FY26 CFO is negative despite positive PAT |
| P/E | SECONDARY, with heavy caveats | Usable as a cross-check but earnings quality is impaired by the trading-gain concentration and 0% 3-year profit CAGR (company memory) |
| P/B | PRIMARY | This is the standard valuation lens for broker-dealers and NBFCs with large trading/lending books; book value is a cleaner anchor than an earnings multiple when >58% of income is mark-to-market; consistent with B00's sector-cap-row assignment ("Banks / NBFCs / MFIs," P/B primary, PE cross-check only) |
| EV/EBITDA | NOT APPLICABLE as primary | EBITDA is distorted by the same fair-value-gain concentration as P/E; finance costs (a real cash cost, given the funding mix) are excluded from EBITDA, understating the true cost of the growth strategy |
| Sum-of-the-parts (SOTP) | TERTIARY, worth building | The group genuinely runs distinct businesses (prop trading, broking, NBFC, merchant banking, insurance, tech/algo platforms) each of which might carry a different peer multiple; Note 45's segment split is the starting data, though it cannot separate prop from client within the largest segment |
| Replacement cost / asset-based | NOT APPLICABLE | No meaningful physical asset base (no plants, AR p.85 BRSR) |
| Dividend discount model | NOT APPLICABLE | Dividend policy not the return driver for this thesis; not evidenced as material in this corpus |

**PRIMARY: Price to Book.** **SECONDARY: P/E, heavily caveated for
earnings-quality concentration in mark-to-market trading gains.**
**TERTIARY: Sum-of-the-parts by segment**, useful for testing whether the
market is already pricing the non-trading businesses at zero.

Cycle stage that matters for valuation: the PROP-TRADING BOOK's cycle
(derivative market volatility and volumes, itself now shaped by SEBI's
F&O curbs) matters more than the broader capital-markets industry cycle,
because it is the line generating the majority of income.

### 4C. Quarterly monitoring checklist (10-15 items)

| # | Item | Good looks like | Trouble looks like |
|---|---|---|---|
| 1 | Fees and commission income YoY | Return to growth | Continued decline (already -12.7%/-18.6% FY26) |
| 2 | Net gain on fair value changes as % of total income | Declining share | Flat or rising share despite stated strategy |
| 3 | CFO (standalone and consol) | Positive | Negative for a 4th consecutive year |
| 4 | Contingent liabilities / net worth | Stabilising | Continuing to rise faster than revenue |
| 5 | Promoter pledge % of promoter holding | Falling | Rising (57.80% Jun-26 per BSE SHP, LBF2) |
| 6 | NCD early-redemption execution | Completed on disclosed terms | Further delay or a second adjourned meeting |
| 7 | Infomerics/Crisil rating cooperation status | Restored to "cooperating" / re-upgraded | Continued ISSUER NOT COOPERATING classification |
| 8 | NBFC GNPA/NNPA vs book growth | Stable or improving alongside growth | GNPA rising with book growth |
| 9 | Segment profit mix (parent vs subsidiaries; broking/trading vs others) | Non-trading segments' share rising | Broking/trading concentration deepens further |
| 10 | Institutional client count and MTF AUM | Steady growth | Flat or declining |
| 11 | Debtor turnover days | Improving toward historical levels | Continued deterioration |
| 12 | Enshrine Leasing acquisition completion and use | Closes at disclosed terms, clear rationale | Terms change or rationale remains unclear |
| 13 | Preferential equity/warrant raise (board item 21-Sep-2026) outcome | Raise on fair terms, dilution disclosed clearly | Raise priced to promoter/related parties on favourable terms |

### 4D. Highest-value questions for management

| # | Question | Answer that reassures | Answer that worries |
|---|---|---|---|
| 1 | What is the FY24-FY26 and Q1 FY27 split of REVENUE AND PROFIT between proprietary trading and client-driven business? | A specific, reconcilable number showing the client share of PROFIT rising | Continued reliance on the "60% client by volume" framing without a profit-basis answer |
| 2 | Why did fee and commission income fall 12.7%/18.6% in the same year the MD&A claims a shift toward client-led business? | A credible one-off explanation with a clear reversal plan | A structural explanation (pricing pressure, client attrition) with no reversal plan |
| 3 | What is the current status of the Rs 99.90 Cr NCD early redemption, and what is the pro-forma DSCR including it? | Redemption executed on schedule, pro-forma DSCR still comfortable | Further delay, or pro-forma DSCR materially weaker than reported |
| 4 | Why is the group cooperating basis for Infomerics restored or not, post the 16-Sep-2026 downgrade? | Cooperation restored, rating stabilised or improved | Continued non-cooperation, further downgrade risk |
| 5 | What drove Algoplus's 64.7% PAT decline and IFSC's swing to a loss in FY26? | Identifiable, temporary cause with a recovery plan | Structural weakening in the fintech/international subsidiaries central to the diversification story |
| 6 | Who are the beneficiaries of the 21-Sep-2026 preferential equity/warrant raise, and at what price versus CMP? | Raise priced at or above CMP to unrelated investors | Raise priced at a discount to promoters/related parties |
| 7 | Why does the MTF book carry NIL impairment allowance and remain always-Stage-1 despite the group's NBFC arm running a 4.30% GNPA? | A specific, evidenced reason the MTF book's risk profile differs from the NBFC book | No differentiated risk rationale, i.e., an aggressive provisioning assumption |

---

## SECTION 5: ONE-PAGE BUSINESS MODEL SUMMARY CARD

```
================================================================
 SHARE INDIA SECURITIES LTD (SHAREINDIA) — BUSINESS MODEL CARD
================================================================
 ONE-LINE:      Prop-trading-led capital markets group with
                broking, MTF/NBFC lending, and fee businesses
                bolted on around a volatile core.

 BUSINESS TYPE: Hybrid — proprietary trader + broker-dealer +
                NBFC lender + fintech/algo platform (fits no
                single CLAUDE.md archetype cleanly; see note
                below)

 REVENUE MIX (FY26 consol, Note 31 etc., AR p.229):
   Net gain on fair value changes (prop trading) ....... 58.3%
   Interest income (MTF/NBFC/deposits, undifferentiated)  18.4%
   Fees and commission income .......................... 11.1%
   Sale of products (stock-in-trade securities) .........  9.2%
   Dividend income .......................................1.1%
   Sale of services .......................................0.6%
   Other income ...........................................1.2%

 SEGMENT CONCENTRATION (Note 45): Share broking/trading is ONE
   segment = 93.2% of FY26 segment revenue, 93.4% of segment
   profit before tax/finance charges. Cannot be split further
   into prop vs client within this note.

 ASSET INTENSITY:   Heavy (trading book, MTF book, pledged FDs)
 WC INTENSITY:      High, deteriorating (debtor turnover -29.8%
                    standalone FY26)
 PRICING POWER:     Weak to none (price-taker on the trading
                    book; commoditised brokerage)
 CYCLICALITY:       Cyclical, tied to derivative-market
                    volatility/volume and SEBI's F&O regulation
 CASH CONVERSION:   Negative CFO 3 of last 4 years (FY23, FY24,
                    FY26); FY26 CFO/PAT -0.55x standalone /
                    -0.56x consol

 MOATS (2C):        Regulatory/licence — MODERATE (shared with
                    peers). Technology/IP — MODERATE, self-
                    asserted, unverified. All others WEAK or
                    ABSENT or UNDERCUT by cash-flow evidence.

 VALUATION HANDOFF: PRIMARY = P/B. SECONDARY = P/E (caveated).
                    TERTIARY = SOTP by segment. DCF and EV/EBITDA
                    NOT APPLICABLE given mark-to-market earnings
                    concentration.

 CENTRAL TENSION:   The AR's own MD&A claims a shift away from
                    proprietary trading; the AR's own BRSR
                    (73.47% trading turnover) and P&L (58.3% of
                    income from fair-value gains) contradict it,
                    in the same document, the same year fee
                    income fell double digits.
================================================================
```

**Archetype note (CLAUDE.md library):** the business fits NO single
archetype cleanly. It combines the "Lender" archetype (its NBFC
subsidiary: AUM growth, NIM, GNPA/NNPA, ROA/ROE all cleanly evidenced,
AR p.74) with the "Platform/network" archetype (uTrade algo subscriptions,
take-rate-like fee income) — but its dominant earnings engine, proprietary
derivatives trading on its own book, matches none of the eight library
archetypes. It is closest in spirit to a market-maker/prop-trading desk,
which the library does not name. This is a finding for the operator: a
"proprietary trading / market-maker" archetype may be needed for future
capital-markets names, alongside the flagged sector-cap-row gap (B00).

---

## Input gaps carried into this stage

- Investor presentation revenue mix is at the SEGMENT level (Broking &
  Trading / NBFC / Merchant Banking / Insurance / Technology), not at the
  product level (prop vs client); it cannot resolve LBF1 further than the
  AR already does.
- Per-trade brokerage rate/tariff: NOT FOUND IN AR OR PRESENTATION, check
  the company's tariff sheet or a concall for a per-unit rate.
- Head-to-head competitor market-share or pricing comparison: NOT FOUND
  IN PROVIDED DOCUMENTS; company memory names SMC Global, Choice
  International and Angel One as structural peers but this is web-sourced
  memory, not anchored evidence.
- Profit-level (not just revenue-level) split between proprietary trading
  and client business: NOT FOUND anywhere in the AR; the segment note
  reports broking/trading as one line and expenses are not allocated by
  revenue type within it. This is a structural, not a corpus, limitation
  (confirms B02 finding 1).
