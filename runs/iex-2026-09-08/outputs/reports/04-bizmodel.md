# STAGE 4 — BUSINESS MODEL DECODER
Indian Energy Exchange Ltd (IEX) | Run date 2026-09-08 | Model: Sonnet 5

Primary source: Annual Report 2025-26 (AR p.__). Secondary: Investor
Presentation, Analyst Meet 24-Jul-2026 (Inv. Pres. slide __) and Q4FY26
presentation. Concall transcripts cited as (Concall Month Year, p.__).
Screener Data_Sheet cited as (Data_Sheet).

---

## SECTION 1: THE BUSINESS MODEL IN PLAIN ENGLISH

### 1A. One-line description
IEX is a licensed marketplace that matches buyers and sellers of Indian
electricity and green certificates, and charges a small fee per unit
traded. It never buys, sells, stores, or takes price risk on power itself.

### 1B. The money flow chain, one per revenue stream

**Transaction fees on electricity (DAM, RTM, TAM, Green segments) — 91.7%
of total revenue** (Rs558.51cr of Rs608.39cr standalone FY26 total revenue
incl. treasury; 95.6% of the Rs583.97cr transaction-fee line, AR p.207,
note 28):
[Generator or DISCOM places a buy/sell bid on the IEX screen] → [IEX's
matching engine runs a double-sided closed-bid auction and finds one
clearing price for the time block; National/Regional Load Despatch
Centre confirms the schedule] → [IEX delivers a matched, confirmed,
financially-settled trade and margining/collateral management] →
[the member who traded pays] → [a fee charged per unit (MWh) traded,
invoiced from the trade date, revenue accrued only once NLDC/RLDC
confirms the schedule] (AR p.186, note 3.7.1; AR p.207, note 28).

**Transaction fees on certificates (REC, ESCerts) — 4.2% of total
revenue** (Rs25.45cr of Rs608.39cr standalone FY26 total revenue, AR
p.207, note 28):
[Distribution licensee, RE generator or obligated entity registers a
REC/ESCert bid] → [IEX runs a periodic auction session, typically twice
a month] → [IEX delivers a matched certificate trade] → [the member
pays] → [a fee per certificate traded] (AR p.7; AR p.207, note 28).

**Annual subscription and membership/processing/transfer fees — 3.9% of
total revenue** (Rs23.98cr of Rs608.39cr, AR p.207, note 28):
[A member registers or re-registers annually to keep trading access]
→ [IEX keeps the member's account, KYC, and connectivity live] →
[IEX delivers continued market access] → [the member pays] → [a flat
annual fee, recognised pro-rata over 12 months from re-registration]
(AR p.186, note 3.7.1).

**Treasury income (interest, dividends, gains on the investment book) —
explicitly labelled "Treasury Income" by the company, NOT an operating
revenue stream — 20.4% of standalone total revenue, 17.6% of
consolidated total revenue** (Rs131.30cr consolidated of Rs746.95cr
consolidated total revenue; AR p.64, MD&A Key Performance Metrics table,
row "Treasury Income"):
[IEX invests its own net-cash surplus, mostly in debt mutual funds and
market-linked debentures] → [IEX earns interest, dividend, and
mark-to-market gains] → [no customer, no service delivered] → [the
capital market pays] → [return on Rs1,993.10cr of investments, FY26,
Data_Sheet]. This is balance-sheet income, not a second product line.

### 1C. Revenue model classification table

| Stream | Type | Description | % of standalone total revenue (FY26) | Predictability |
|---|---|---|---|---|
| Electricity transaction fees (DAM+RTM+TAM+Green) | Volume-based take rate | Fee per MWh matched and confirmed | 91.7% (95.6% of the transaction-fee sub-line) (AR p.207) | M — volume grows with power demand and market share, but per-unit fee and product mix (DAM vs RTM) are regulator-influenced |
| Certificate transaction fees (REC+ESCerts) | Volume-based take rate | Fee per certificate matched | 4.2% (AR p.207) | L — REC volumes collapsed 81.4% YoY in Q1FY27 and stayed down 56.3%-92.3% YoY every disclosed FY27 month (announcements__Power_Market_Update, Jun/Jul/Aug 2026) |
| Annual subscription + membership/processing/transfer fees | Subscription/recurring | Flat annual access fee per registered member/client | 3.9% (AR p.207) | H — sticky, tied to a growing and rarely-churning member base (9,000+ registered participants, AR p.5) |
| Treasury income | Non-operating, investment return | Interest/dividend/MTM gain on the cash-and-investment book | 20.4% standalone / 17.6% consolidated, explicitly labelled "Treasury Income" (AR p.64) | M — driven by rate cycle and average investment balance, not by the exchange business; do not extrapolate as if it were operating growth |

Note: revenue is disaggregated in the audited notes ONLY into the
two-way split above (Electricity bundle vs Certificates bundle). There
is NO revenue split by DAM / RTM / TAM / Green anywhere in the audited
statements. Only VOLUME splits by product exist, and only in the MD&A,
concalls, and investor presentation (AR p.61-62; Inv. Pres. slide 12).
Any DAM-specific or RTM-specific revenue number in this report is
therefore inferred from volume share and the blended fee rate, never
a disclosed figure — flagged wherever used.

### 1D. Simplified business model canvas

| Dimension | This company |
|---|---|
| What they sell | Access to a price-discovery and trade-matching venue for physical electricity and certificates. The product is the match, not the electron. |
| Who buys | DISCOMs (state and private distribution utilities), power generators (conventional and renewable), traders, and Commercial & Industrial (C&I) open-access consumers (AR p.4, Message to Shareholders) |
| Why them | 18 years of operating history, 80-85% market share of India's exchange-based electricity trade held consistently (Concall Jul-2026, p.4-5), 9,000+ registered participants, and API-based deep integration into customer back-offices (72% of I-DAM cleared volume via bidding APIs, AR p.58) |
| How delivered | A fully electronic, cloud/data-centre-hosted matching engine with hot-standby and DR failover, ISO-certified since Aug-2016 (AR p.2, p.58) |
| Cost structure dominance | Employee cost (Rs48.14cr) and technology expense (Rs13.65cr) dominate a tiny standalone operating-cost base of Rs85.11cr against Rs608.39cr total revenue — an 87% operating margin business (AR p.65; Data_Sheet FY26 OPM implied) |
| Scarce resource | The CERC trading licence (regulated since 27-Jun-2008) plus the accumulated liquidity pool itself — buyers go where sellers already are (AR p.2) |
| Pricing power source or absence | Historically strong (near-monopoly liquidity network effect); now under direct regulatory attack via market coupling, which would force a single clearing price across exchanges and remove IEX's ability to compete on liquidity/price discovery in DAM (AR p.57-58, MARKET COUPLING section) |
| Asset intensity | Very light. Net block Rs96.68cr against total assets Rs2,435.74cr, 4.0% (Data_Sheet FY26) |
| WC intensity | Structurally negative/low for the OPERATING business — trade receivables just Rs1.98cr (Data_Sheet FY26) because settlement runs through pre-funded member margin, not company receivables. Separately, IEX holds Rs974.69cr of "other current financial liabilities" (standalone, note 24, AR p.179) which is predominantly member settlement guarantee fund and trading margin money (AR p.287, notes 50-51) — NOT the company's working capital, member money passing through. |
| Regulatory moat or burden | Both. CERC licence and price-cap regime created and protects the exchange model; the same regulator can now redesign the market (coupling) and directly compress the moat that regulation itself built (AR p.57-58) |

### 1E. The chai-stall-uncle version
Think of IEX as the mandi (wholesale market) for electricity, not a
company that sells power. Every day, sellers of electricity (a solar
farm, a coal plant, a state that has surplus power) and buyers (a
DISCOM short of supply, a factory wanting cheap afternoon power) come to
IEX's screen instead of finding each other one by one. IEX runs the
auction, finds one fair price for everyone at that moment, and takes a
small fee, a few paise per unit, from whoever trades. It never owns the
electricity and never loses money if the price of power crashes or
spikes — it only cares how MUCH electricity crosses its counter, not
what price it crosses at. The catch: the government regulator that gave
IEX this mandi licence is now proposing to link IEX's price-setting
computer to a shared, government-run one (Grid India), the way UPI
linked every bank's payment system into one rail. IEX would still collect
its members' bids and still take its fee, but it would no longer be the
only place setting the price.

### Section 1 summary table

| | |
|---|---|
| Business type | Platform / marketplace (financial market infrastructure) |
| Revenue nature | Volume-based transaction fee (take rate) plus a smaller recurring subscription fee; treasury income is non-operating |
| Asset intensity | Light |
| WC intensity | Low/negative on the operating business; large member-money float sits on the balance sheet but is not company capital |
| Pricing power | Currently moderate-to-strong via liquidity network effect, but under active regulatory attack (market coupling) in its largest single segment, DAM |

---

## SECTION 2: INDUSTRY DYNAMICS & COMPETITIVE POSITION

### 2A. Five forces, plainly

| Force | Answer | Helps/Hurts/Neutral |
|---|---|---|
| Competition (how many, how fierce) | IEX has held 80-85% market share of India's power-exchange volume for years against other licensed power exchanges (unnamed in this corpus; Term-Ahead Market alone shows three exchanges splitting roughly 40/30/20-50% among themselves, Concall Apr-2026 p.14) | Helps today; TAM shows what a multi-exchange market looks like and it is not fee-destructive per management (see 2C) |
| Entry barriers | High. Requires CERC registration/approval as a power exchange, a proven clearing/settlement engine audited annually, and — critically — an existing liquidity pool that a new entrant cannot buy (AR p.2, p.58) | Helps |
| Supplier power (who "supplies" IEX) | IEX's inputs are its own technology team and its exchange licence, not a physical raw material. Regulatory dependency substitutes for supplier power: CERC alone approves new products and can redesign market structure (AR p.57-63, STRATEGIC RISK) | Neutral-to-Hurts (the "supplier" is also the regulator that can hurt the model) |
| Customer power and concentration | 9,000+ registered participants (AR p.5) spreads customer power thin, BUT one single unnamed customer is 16.2% of FY26 revenue (Rs9,862.24 lakh of Rs60,838.57 lakh standalone operating revenue, AR p.211, note 28) | Mixed — broad base helps, single-customer concentration at 16.2% is a named risk |
| Substitutes | Long-term bilateral PPAs (power purchase agreements) are the substitute channel; management states the market is structurally shifting AWAY from long-term PPAs toward exchange-based short-term procurement, with un-requisitioned PPA surplus increasingly routed to the exchange (Concall Jul-2026, p.4) | Helps (secular tailwind) |

### 2B. Competitive positioning map
Named competitors are NOT identified anywhere in this corpus (no PXIL,
HPX, or similar name appears in the AR, MD&A, presentations, or
concalls read). What IS disclosed:
- IEX market share: 80-85% of exchange-traded volume, held consistently
  ("we have always been maintaining 80-85% market share", Concall
  Jul-2026, p.4).
- In the one segment where liquidity is already spread roughly evenly
  across three exchanges (Term-Ahead Market, running four years),
  shares sit near 40%/30%/20-50% and the blended fee/margin has stayed
  intact at roughly Rs0.04 gross / Rs0.036-0.037 net per unit
  (Concall Apr-2026, p.14-15). Management uses this as the working
  precedent for what a coupled/fragmented DAM might look like.
- NOT FOUND, check investor presentation or concall: named competitor
  identities, their individual market shares, or their fee schedules.

### 2C. Moat assessment (eight standard moat types)

| Moat type | Present? | Evidence | Durability |
|---|---|---|---|
| Network effect | YES, but narrowing in DAM | Liquidity begets liquidity: buyers/sellers go where the deepest order book already is; 80-85% market share sustained for years (Concall Jul-2026 p.4) | MODERATE — market coupling is a direct regulatory attack on this exact moat in DAM (see Section 4 risk discussion below) |
| Switching costs | YES | API integration into customer SAP/back-office systems (72% of I-DAM cleared volume via bidding APIs, 56% via trade-report APIs, AR p.58); 18 years of workflow embedding | HIGH for existing large members, LOW barrier for a new member to add a second exchange connection |
| Cost advantage | YES | Near-zero marginal cost per additional trade on an already-built platform; 87% implied operating margin (AR p.64-65) | HIGH — structural to the asset-light model, not replicable cheaply by a new entrant without matching volume |
| Brand | MODERATE | "IEX" is the default reference price for Indian power ("DAM price" is widely quoted by media and utilities); 18-year incumbency (AR p.2) | MODERATE — brand recognition does not by itself stop a regulator-mandated price-coupling |
| Regulatory / licence | YES, but double-edged | CERC approval since 27-Jun-2008 created the moat; the same CERC is the entity proposing to erode it via market coupling (AR p.2, p.57-58) | LOW-MODERATE — this is the single most consequential line in the whole moat picture; a regulatory moat that the regulator itself is actively redesigning is not a durable moat in the conventional sense |
| Efficient scale | YES | The exchange only needs to exist once per liquidity pool; a second full-scale competitor gains little by fragmenting the same order flow (implicit in the TAM precedent, Concall Apr-2026 p.14) | MODERATE |
| Data / process advantage | YES | Two decades of bidding data, audited clearing algorithm, data analytics tools offered to customers (AR p.58) | MODERATE |
| Counter-positioning / first-mover | YES | First mover in DAM (2008), RTM (2020), REC (2011); the incumbent that new entrants must dislodge from an installed base | MODERATE, weakens as products commoditise (TAM precedent) |

### 2D. Industry lifecycle stage
The Indian power-exchange industry itself is in GROWTH — exchange-based
volume is 8% of India's total power consumption today, up from "4%, 5%,
6%" a few years ago, per management (Concall Jul-2026, p.4-5), against a
government policy push away from long-term PPAs toward market-based
procurement. IEX, as the dominant incumbent, sits at MATURE-LEADER
position within a still-growing category — the company's own growth
is now a product-mix story (RTM/TAM/Green taking share from DAM) more
than a market-share story.

### 2E. Key industry drivers

| Driver | Direction | Impact on IEX |
|---|---|---|
| India power demand growth (245 GW peak FY26, 1,707 BU consumption) | Up, ~1% YoY in FY26 but long-run structural growers (urbanisation, EVs, manufacturing) intact (AR p.44) | Positive, more electrons to trade |
| Renewable capacity addition (55 GW non-fossil added in FY26, highest ever) | Up sharply | Positive — intermittent renewable output needs short-term markets (RTM, Green DAM) to balance, a direct tailwind to IEX's fastest-growing segments |
| Shift from long-term PPAs to exchange-based procurement | Structural, ongoing | Positive |
| Market coupling regulation | Active regulatory process, draft regulations issued 17-Apr-2026, hearings concluded 10-Jun-2026, Supreme Court appeal pending | Negative for the DAM liquidity moat specifically; see Section 4 |
| REC volume collapse (down 56.3%-92.3% YoY every month disclosed in FY27) | Sharply down | Negative for the smaller certificates revenue line |

---

## SECTION 3: FINANCIAL METRICS THAT MATTER FOR THIS BUSINESS MODEL

### 3A. Ignore-these-track-these table

| Commonly tracked ratio | Verdict | Why it is misleading/irrelevant here |
|---|---|---|
| Inventory turnover | IRRELEVANT | IEX carries no inventory (Data_Sheet: inventory line blank every year); it trades nothing on its own book |
| Gross margin (COGS-based) | IRRELEVANT | There is no cost of goods sold; the "product" is a matched trade, not a manufactured or sourced good |
| Raw material cost | IRRELEVANT | No raw material line exists in the P&L (Data_Sheet, Power and Fuel is a de minimis Rs0.18cr facility cost, not a production input) |
| Capacity utilisation (plant-style) | IRRELEVANT | There is no physical production capacity to utilise; the constraint (if any) is software/engine throughput, not floor space or machine-hours |
| Fixed asset turnover | MISLEADING | Net block is only Rs96.68cr against Rs608.39cr standalone revenue (Data_Sheet); a headline ratio would look implausibly high and tells you nothing about the real driver, which is member liquidity, not fixed assets |
| Debt-to-equity / interest coverage | LOW SIGNAL VALUE | Borrowings are Rs11.16cr, entirely Ind AS 116 lease liability (per task brief and Data_Sheet); IEX is not credit-risk-relevant, and carries no rated debt (companies with no listed debt do not get rated, per B00 gap note) |
| P/E on reported (unadjusted) EPS | MISLEADING without adjustment | 20.4% of standalone / 17.6% of consolidated total revenue is Treasury Income, non-operating (AR p.64); an unadjusted P/E blends a market-infrastructure multiple with a bond-fund return |

### 3B. Must-track metrics

**Growth**

| Metric | What it tells you | Healthy range for this business | Where to find it | Red flag threshold |
|---|---|---|---|---|
| Electricity traded volume (BU), YoY | The core demand driver — fee revenue is roughly volume x blended rate | Double-digit YoY growth historically normal; FY26 was +16.9% (141 BU vs 121 BU FY25, AR p.4) | AR Key Highlights; monthly Power Market Update releases | Any month of flat or negative YoY volume growth, unexplained by demand |
| Product mix shift (DAM % of volume) | Directly measures exposure to the coupling risk | DAM fell from 95% (FY16) to 39% (FY26); RTM at 34% and closing the gap fast (Inv. Pres. slide 12; AR p.58) | Investor presentation, MD&A regulatory-risk section | DAM share stabilising or reversing its decline (would concentrate coupling risk instead of diluting it) |
| REC/ESCert volume, YoY | Smaller but currently the weakest line | REC volumes were DOWN 92.3% (Jun-26), 56.3% (Jul-26), 86.6% (Aug-26), 81.4% (Q1FY27) YoY (Power Market Update announcements) | Monthly Power Market Update releases | Continued double-digit-percent-of-prior-year collapse without a stated cause (sell-bid withdrawal) |

**Profitability and efficiency**

| Metric | What it tells you | Healthy range | Where to find it | Red flag threshold |
|---|---|---|---|---|
| Operating revenue growth EX treasury income | The real business growth rate, stripped of investment returns | Standalone operating revenue grew 13.64% FY26 (AR p.64) | MD&A KPI table, "Revenue from operation" row | Operating revenue growth materially below total revenue growth (treasury income doing the heavy lifting) |
| Treasury Income as % of total revenue/PBT | Flags how much of reported profit is non-operating | FY26: 20.4% of standalone total revenue; other income + IGX equity pickup = Rs151.10cr, 23.4% of consolidated PBT (AR p.64; Data_Sheet) | MD&A KPI table row "Treasury Income"; other income note | Rising share of PBT from treasury versus operations, especially if operating EPS is flat while reported EPS rises |
| Standalone operating margin (op. revenue less op. cost, ex D&A) | The economics of the core matching business | FY26 implied ~86% (Rs60,838.57 lakh op. revenue less Rs8,511.46 lakh op. cost, AR p.65) | MD&A expense table | A sustained fall below ~75-80% would signal the model is losing its structural cost advantage |

**Balance sheet and risk**

| Metric | What it tells you | Healthy range | Where to find it | Red flag threshold |
|---|---|---|---|---|
| Net cash / investments ex member float | True excess capital available to the equity holder | Investments Rs1,993.10cr + cash Rs105.18cr against borrowings Rs11.16cr (Data_Sheet FY26); ~20% of market cap per company memory | Balance sheet, MD&A | A large unexplained draw-down of the investment book without a stated capital-return or M&A use |
| Member settlement/margin liability vs company net worth | Confirms this money is NOT company capital | Rs974.69cr other current financial liabilities (standalone, note 24, AR p.179), predominantly SGF and trading margin deposits (notes 50-51, AR p.287) is LARGER than the operating business needs to run itself | Balance sheet notes 24, 50, 51 | Any commingling signal, or a liability growing materially faster than trading volume |
| Single-customer revenue concentration | Concentration/counterparty risk | 16.2% FY26 (Rs98.62cr of Rs608.39cr standalone revenue, AR p.211, note 28) | Revenue note, "more than 10% of total revenue" disclosure | Concentration rising further, or the same disclosure recurring with a growing rupee amount |

### 3C. Industry-specific non-financial KPIs

| KPI | Where to find it |
|---|---|
| Electricity traded volume, BU, monthly/quarterly/annual, by product (DAM, RTM, TAM, Green) | Monthly Power Market Update announcements; investor presentation slide 12; AR p.4 |
| REC volume traded, lakh certificates, and clearing price per REC | Monthly Power Market Update announcements |
| Number of registered participants/members | AR p.5, p.58 ("9,000+ registered participants") |
| % of cleared I-DAM volume via bidding API vs trade-report API | AR p.58 |
| DAM Market Clearing Price (Rs/unit) and RTM average price (Rs/unit) | Monthly Power Market Update announcements; presentation |
| Country peak power demand (GW) and total consumption (BU) | AR p.44, MD&A INDIA'S POWER SECTOR section |
| DAM % share of total volume (the single most important coupling-exposure KPI) | Investor presentation slide 12; AR p.58 MD&A regulatory-risk section |
| CERC/APTEL/Supreme Court docket status on market coupling | Company's own Regulation 30 filings; AR p.57-63, note 53 (AR p.291) |
| IGX volume (million MMBtu) and PAT | Concall commentary (Concall Jul-2026, p.4-5); IGX DRHP once available |

### 3D. Unit economics — the physics of the business

**Define one unit.** For the electricity business, one unit = 1 MWh
(one "unit" in Indian power-market convention = 1 kWh; traded volumes
are quoted in Billion Units, BU = billion kWh). For the certificates
business, one unit = 1 REC (1 MWh-equivalent renewable attribute) or
1 ESCert (1 Mtoe).

**Revenue per unit (electricity, blended, FY26, derived).** Rs558.51cr
electricity transaction-fee revenue (AR p.211) divided by 141 BU
electricity volume (AR p.4) implies a blended realisation of
approximately Rs0.0396/kWh, i.e. roughly 3.96 paise per unit traded.
This is a DERIVED figure, not a disclosed one, since revenue is not
split by product (flagged per 1C above). Management independently
quoted a comparable reference point for the Term-Ahead Market
specifically: gross fee around Rs0.04 (four paise) per unit, net
margin around Rs0.036-0.037 (3.6-3.7 paise) per unit, a rate that has
held steady for four years even with three exchanges sharing that
segment's liquidity (Concall Apr-2026, p.14-15). The two figures are
consistent, which supports using ~3.5-4.0 paise/unit as the working
blended fee range across products, while noting products differ (DAM,
RTM, and Green likely each price differently; the number above is a
company-wide average, not a per-product rate).

**Revenue per unit (certificates, derived).** Rs25.45cr certificates
revenue (AR p.211) against 187 lakh (18.7 million) RECs traded (AR
p.4) implies roughly Rs13.6 per REC on average — an approximation
because the revenue line also bundles ESCerts, whose volume is not
separately disclosed in this corpus (NOT FOUND, check investor
presentation or concall for a standalone ESCert volume figure).

**Cost per unit.** Effectively near-zero and falling as volume rises —
the platform is built once; an incremental matched trade consumes
negligible additional compute. Standalone operating cost of Rs85.11cr
(AR p.65) against 141 BU of electricity + 187 lakh certificates implies
a marginal cost structure that does not scale with volume in any
material way; almost all operating cost (employee cost, technology
spend, legal/professional) is FIXED relative to trade count.

**Volume drivers.** (1) India's overall power demand and generation
growth; (2) the secular shift of procurement from long-term bilateral
PPAs to exchange-based short-term trading (AR p.44; Concall Jul-2026
p.4); (3) renewable capacity growth, which creates intermittent supply
that needs a short-term market to balance (RTM, Green DAM) (AR p.44-45);
(4) new product launches (Green RTM, Peak Contracts, extended TAM
duration, all in pipeline per AR p.42, p.63).

**Price drivers.** The per-unit transaction fee itself is effectively
set by IEX within CERC's regulatory envelope, product by product; it
has historically NOT needed to be cut even under multi-exchange
competition in TAM (Concall Apr-2026, p.14-15). Market coupling is the
one live threat to this pricing discretion in DAM specifically (see
Section 4).

**Cost drivers.** Employee cost (Rs48.14cr, +7.05% YoY, AR p.65) and
technology expense (Rs13.65cr, +28.59% YoY, largely software licences,
AMCs, security tools, data-centre operations, AR p.65) are the two
lines that actually move with the business; both are headcount/
capability decisions, not volume-linked.

**Incremental margin and operating leverage.** Very high. Because cost
is near-fixed and revenue is volume-linked, each incremental unit of
electricity traded drops through to profit at close to the blended
fee rate, minus negligible marginal cost. This is the single most
important physics fact about IEX: revenue growth from volume comes
almost entirely as profit growth, which is why standalone operating
margin sits near 86-87% (AR p.64-65). The flip side: any structural
compression of the per-unit fee (via fee competition after coupling)
would also drop through to profit nearly 1:1, since there is little
variable cost to cut in offset.

---

## SECTION 4: RISKS, VALUATION APPROACH & MONITORING

### 4A. Business-model-specific risks

| Category | Risk | First financial line item that would deteriorate |
|---|---|---|
| Revenue model | Market coupling removes IEX's ability to differentiate on price discovery in DAM (39% of FY26 volume, AR p.58), turning IEX into a bid-collection venue for that segment and opening the door to fee competition | Electricity transaction-fee revenue growth decelerating below electricity volume growth (a widening gap between volume growth and fee revenue growth is the tell, since the two are currently disclosed only in combination) |
| Revenue model | REC certificate revenue continuing its collapse (down 56.3%-92.3% YoY every FY27 month disclosed) on falling sell-bid participation | Certificates revenue line in the annual revenue note (currently 4.2% of total, could shrink toward negligible or even threaten the annual subscription base of REC-only members) |
| Margin | Treasury income becoming a growing share of reported PBT while operating revenue growth slows, flattering headline EPS | Operating revenue growth rate falling below total/consolidated revenue growth rate; Treasury Income % of PBT rising past the current 20-23% |
| Balance sheet | Member settlement/margin money (Rs974.69cr, AR p.179) is contractually the members', not IEX's; any operational, cyber, or settlement failure exposes IEX's platform trust, not its own capital, but a failure event would be catastrophic to volume | A spike in "Other financial liabilities" without a matching spike in trading volume, or any disclosed settlement/cyber incident |
| Execution | Legal/professional expense already up 92.4% YoY (Rs628.88 lakh to Rs1,210.26 lakh, AR p.65) reflecting the coupling litigation load; continued litigation cost escalation without resolution | "Other operating expenses" line in the MD&A expense table |
| Structural | The CERC that created IEX's regulatory moat is the same body redesigning the market via coupling; a body that is simultaneously regulator and market-architect is a structural feature of this business, not a one-off event | Final CERC market coupling regulations, once notified (currently at draft stage; public hearings concluded 10-Jun-2026, AR p.58) |
| Structural | Zero promoter holding (0.00%, per B00 manifest) means no controlling shareholder anchors strategy; strategic decisions (product launches, IGX/coal/carbon exchange bets) rest entirely with a professional board and management team | Any governance or related-party disclosure change; the ongoing whistle-blower investigation on alleged conflict of interest (AR p.287, note 49) is the first visible marker to track |

### 4B. Valuation method applicability

| Method | Applicable? | Notes |
|---|---|---|
| P/E (on OPERATING EPS, treasury income stripped) | PRIMARY | Standard for an asset-light, high-margin, cash-generative platform; must strip Treasury Income (20.4% standalone / 17.6% consolidated of total revenue, AR p.64) to avoid crediting a bond-fund return inside an equity multiple. This is also the valuation basis flagged in company memory and the sector-cap gap (companies/IEX.md); Stage 11 must resolve the Section 1B sector-cap row before this method finalises a multiple. |
| EV/EBITDA | SECONDARY cross-check | Useful because it neutralises the large net-cash position and lets a reader compare the operating engine alone against peers (MCX, BSE, CDSL) without the cash pile distorting the multiple |
| DCF | TERTIARY | Workable given predictable cash conversion (CFO/PAT 0.88, Data_Sheet) but highly sensitive to a terminal assumption on DAM fee durability post-coupling; treat any DCF here as a scenario tool, not a point estimate, until the coupling regulations are finalised |
| SOTP (sum-of-the-parts) | NOT APPLICABLE as primary, but a live consideration | IEX carries a Rs90.25cr equity-method stake in IGX (47.28%, AR p.291) that is about to partially monetise via the IGX IPO OFS (1.671cr shares, cutting the stake to the PNGRB 25% ceiling); once IGX lists, a SOTP overlay (operating IEX + market value of residual IGX stake + Indian Coal Exchange/Indian Carbon Exchange optionality) becomes directly relevant and should be layered onto the primary P/E, not substituted for it |
| Asset-based / book value | NOT APPLICABLE | Net block is Rs96.68cr against a market cap of Rs10,396.21cr (B00 manifest); book value bears no relationship to the earnings power of a licence-and-liquidity business |
| Replacement cost | NOT APPLICABLE | The moat is the liquidity pool and the customer base, not the technology, which management itself says it can re-engineer in-house at no additional cost for coupling compliance (Concall Apr-2026, p.15) |

Cycle stage that matters for valuation: this is NOT a commodity cycle
business; the relevant "cycle" is the REGULATORY cycle on market
coupling (draft regulations issued, hearings concluded, Supreme Court
appeal pending) layered on a secular volume-growth trend. Valuation
should be built around a base case that assumes coupling proceeds in
some form, sized against DAM's already-shrinking 39% volume share, not
around a binary coupling/no-coupling switch.

### 4C. Quarterly monitoring checklist

1. Electricity traded volume (BU), YoY and QoQ — good: double-digit
   YoY; trouble: flat/negative without a clear demand-side cause.
2. DAM % of total volume — good: continuing to shrink or stabilise
   near current level; trouble: DAM share growing again (concentrates
   coupling exposure).
3. RTM % of total volume — good: continuing to grow toward/past DAM;
   trouble: growth stalling.
4. REC volume traded, lakh certificates, YoY — good: stabilising;
   trouble: continued 50%+ YoY declines.
5. Blended electricity transaction-fee realisation (revenue/volume,
   derived) — good: stable near 3.5-4.0 paise/unit; trouble: visible
   compression.
6. Operating revenue growth vs total revenue growth (the treasury-income
   gap) — good: near-equal or operating growing faster; trouble: a
   widening gap.
7. Treasury Income as % of total revenue and of PBT — good: broadly
   stable proportion; trouble: rising share while operating growth
   slows.
8. Single-customer revenue concentration (annual disclosure) — good:
   stable or falling; trouble: rising percentage or naming a new
   >10% customer.
9. Legal & professional expense (coupling litigation proxy) — good:
   stabilising; trouble: continued sharp YoY escalation.
10. CERC/APTEL/Supreme Court docket status on market coupling — good:
    prolonged delay or a favourable outcome for IEX; trouble: final
    regulations notified with an implementation date.
11. Member settlement/margin liability vs trading volume — good:
    growing roughly in line with volume; trouble: any disclosed
    settlement or cyber incident.
12. IGX carrying value and OFS progress (offer for sale of 1.671cr
    shares toward the 25% PNGRB ceiling) — good: IPO proceeding on
    schedule; trouble: delay or a materially lower-than-book valuation.
13. Whistle-blower investigation (AR p.287, note 49) — good: closed
    with no material finding; trouble: escalation or disclosure of a
    material finding.
14. New product approvals in the CERC pipeline (Green RTM, Peak DAM/
    RTM, extended TAM duration) — good: approvals proceeding; trouble:
    stalled approvals (could also signal regulator friction post the
    coupling litigation).
15. Dividend payout consistency (IEX has historically paid 50-65%+ of
    PAT as dividend per management, Concall Jul-2026 p.11) — good:
    maintained; trouble: a cut without a stated capital-allocation
    reason.

### 4D. Highest-value questions for management

1. "What share of FY26 and Q1FY27 transaction-fee revenue, not just
   volume, came from DAM specifically?" Reassuring answer: a number
   the company is willing to disclose and it roughly tracks the 39%
   volume share. Worrying answer: refusal to disclose, or a number
   showing DAM still carries a disproportionately higher fee rate than
   its volume share implies (meaning coupling risk to REVENUE is larger
   than the volume-share numbers suggest).
2. "If coupling proceeds, does IEX expect to compete on fee rate for
   DAM order flow, the way rates have held steady in TAM?" Reassuring:
   a specific, evidenced answer pointing to the TAM precedent (Concall
   Apr-2026 p.14-15) with a stated floor. Worrying: vague reassurance
   with no fee-floor commitment or precedent cited.
3. "What is driving the 56%-92% YoY collapse in REC volumes every month
   this fiscal year, and is it structural or temporary?" Reassuring:
   a specific, verifiable cause (e.g., a policy change on obligated
   entity compliance windows) with an expected recovery date. Worrying:
   "market dynamics" with no specificity.
4. "Who is the single customer that is 16.2% of FY26 revenue, and what
   is the retention risk if that customer's procurement strategy
   changes?" Reassuring: a category answer (e.g., "a large state
   DISCOM under a multi-year cost-optimisation programme") showing
   the concentration is structural, not fragile. Worrying: refusal to
   characterise the customer at all.
5. "What is the current book carrying value of the IGX stake and how
   will IEX deploy the OFS proceeds?" Reassuring: a clear capital
   allocation plan (dividend, buyback, new-exchange investment).
   Worrying: no stated plan, raising the risk of unproductive cash
   accumulation on top of the already Rs1,993cr investment book.
6. "Does IEX expect the whistle-blower investigation (note 49) to
   produce any disclosure beyond the current 'no material impact'
   statement?" Reassuring: investigation closed, findings immaterial
   and disclosed. Worrying: continued "ongoing" status across multiple
   quarters with no closure timeline.
7. "What operating cost, if any, will IEX bear once bids must be
   forwarded to Grid India as Market Coupling Operator?" Reassuring:
   "no additional cost, our own software team handles it" (as already
   stated, Concall Apr-2026 p.15) reconfirmed with specifics. Worrying:
   a new cost line appearing in a future MD&A expense table without
   prior guidance.

---

## SECTION 5: ONE-PAGE BUSINESS MODEL SUMMARY CARD

```
+-----------------------------------------------------------------+
| INDIAN ENERGY EXCHANGE LTD (IEX)                    FY26 (AR)   |
+-----------------------------------------------------------------+
| ONE-LINE: A licensed marketplace that matches electricity/      |
| certificate buyers and sellers and takes a fee per unit traded. |
| Never owns the electron, never takes price risk.                |
+-----------------------------------------------------------------+
| BUSINESS TYPE       | Platform / market infrastructure          |
| REVENUE NATURE       | Volume-based take rate + subscription    |
| PRIMARY REVENUE       | Electricity transaction fees, 91.7% of  |
|                       | standalone total revenue (AR p.207/64)  |
| ASSET INTENSITY       | Light. Net block Rs96.68cr / Rs2,435.74cr|
|                       | total assets (Data_Sheet)                |
| WC INTENSITY          | Low/negative on the operating business;  |
|                       | Rs974.69cr member float sits separately  |
|                       | on balance sheet (AR p.179)               |
| PRICING POWER         | Moderate-strong today via liquidity      |
|                       | network effect; under direct regulatory  |
|                       | attack in DAM (39% of volume, shrinking) |
| GROSS/OPERATING MARGIN| ~86-87% standalone operating margin      |
|                       | (AR p.64-65)                              |
| TREASURY INCOME SHARE | 20.4% of standalone total revenue, 17.6% |
|                       | consolidated (AR p.64)                    |
| KEY GROWTH DRIVER     | Electricity traded volume (+16.9% FY26,  |
|                       | 141 BU, AR p.4); mix shift RTM>DAM       |
| KEY RISK              | Market coupling (CERC-ordered DAM        |
|                       | coupling; draft regs issued Apr-2026,    |
|                       | Supreme Court appeal pending)             |
| SINGLE-CUSTOMER RISK  | 16.2% of FY26 revenue (AR p.211)         |
| MOAT COUNT (8-type)   | 6 of 8 present (network effect, switching|
|                       | costs, cost advantage, brand, efficient  |
|                       | scale, data/process); regulatory moat is |
|                       | double-edged, weakening in DAM           |
| PRIMARY VALUATION     | P/E on operating EPS (treasury stripped) |
| MUST-WATCH METRIC     | DAM % of volume; blended fee realisation |
+-----------------------------------------------------------------+
```
