# STAGE 4: BUSINESS MODEL DECODER
## Zaggle Prepaid Ocean Services Limited (ZAGGLE) | Run date: 2026-07-27 | Model: claude-sonnet-5

**Primary source**: FY25 Annual Report (AR, year ended March 31, 2025, 158-PDF-page file, two printed pages per PDF page).
**Secondary source**: Investor Presentation, May 2026, covering Q4/FY26 and FY26 full-year actuals (39 slides). Note: the presentation covers FY26, a period beyond the AR's FY25 window; it is used here only as directional/confirmatory context, never as the anchor for the FY25 revenue-mix numbers that drive Section 1C and the YAML handoff. All revenue-stream percentages in this report are anchored to FY25 AR figures unless explicitly marked "Pres." with a later period.

Input gaps flagged up front: prospectus ABSENT (HIGH - IPO offer document would carry the fullest business-model and risk-factor detail; not provided), stock exchange announcements ABSENT, shareholding pattern ABSENT, sell-side/independent research ABSENT. Every "NOT FOUND" below traces to one of these gaps unless otherwise noted.

---

## SECTION 1: THE BUSINESS MODEL IN PLAIN ENGLISH

### 1A. One-line description
Zaggle is a SaaS-plus-fintech platform that lets Indian companies digitise and control every rupee an employee, vendor or channel partner spends on the company's behalf, and gets paid a slice of that spend three different ways (AR p.144, "About Zaggle").

### 1B. Money-flow chain for each revenue stream

**Stream 1 - Program Fees (interchange revenue share)**
[Corporate loads money for employee/vendor spend] → [Zaggle issues co-branded prepaid/corporate credit cards through bank partners (HDFC, ICICI, Axis, IndusInd, Kotak Mahindra, IDFC First, NSDL Payments Bank - AR p.144) and routes the spend through Visa/Mastercard/RuPay rails] → [Zaggle delivers the software dashboard, controls and the physical/virtual card programme] → [the bank pays Zaggle] → [the bank pays Zaggle a contracted share of the interchange fee it earns each time the card is swiped] (AR Note 42 revenue-recognition policy, p.294 standalone financials: recognised "at the point in time" based on information shared by banks post-settlement).

**Stream 2 - Propel platform revenue / gift cards**
[A corporate wants to reward employees, channel partners or dealers] → [Zaggle sources and issues prepaid cards / merchant gift vouchers, acting as principal - i.e. Zaggle buys and resells the instrument rather than merely arranging it] → [Zaggle delivers the reward/incentive platform plus the redeemable instrument] → [the corporate pays Zaggle the full face value of the cards/vouchers] → [Zaggle pays out ~94% of that as "cost of point redemption/gift cards" to the underlying merchants/card issuers and keeps a thin margin] (Significant Accounting Policies, AR standalone financial statements p.??? - "the Company acts as a principal and accordingly consideration... is recognised on gross basis"; cost of point redemption/gift cards Rs.6,781.00 Mn against Propel gross revenue of Rs.7,218.48 Mn in FY25, AR p.147).

**Stream 3 - Platform fee / SaaS fee / service fee**
[A corporate subscribes to Save (expense management), Zoyer (procure-to-pay), Zatix (spend analytics) or BROME] → [Zaggle provides the software as a recurring service] → [Zaggle delivers dashboards, workflow automation, reconciliation and reporting] → [the corporate pays a subscription/service fee] → [recognised over time as the service is rendered] (AR Note 42, "services transferred over time"; AR p.144-145 product list).

### 1C. Revenue model classification table (FY2024-25, consolidated, AR p.145 Business Performance table)

| Stream | Type | Description | % of revenue (FY25, anchored) | Predictability |
|---|---|---|---|---|
| Program fee | Transaction/usage-based, agency-like (bank pays a revenue share) | Interchange income share from prepaid/corporate-card spend via bank partners | Rs.5,456.41 Mn / Rs.13,037.57 Mn = 41.85% (AR p.145) | Medium - recurring but tied to card-spend GMV and bank-partner terms |
| Propel platform revenue / gift cards | Principal-basis resale (goods, point-in-time) | Corporate reward/incentive gift cards and points, reported gross per Ind AS principal accounting | Rs.7,218.48 Mn / Rs.13,037.57 Mn = 55.37% (AR p.145) | Low on a gross basis (pass-through, ~94% cost ratio, AR p.147); the ~6% net take is the real recurring piece |
| Platform fee / SaaS fee / service fee | Subscription/SaaS (services, over time) | Save, Zoyer, Zatix, BROME software subscriptions | Rs.362.68 Mn / Rs.13,037.57 Mn = 2.78% (AR p.145) | High - contractual subscription revenue, but smallest stream and growing slowest (+16.06% YoY vs total +68.10%, AR p.147) |

Total revenue from operations FY25: Rs.13,037.57 Mn (consolidated), +68.10% YoY from Rs.7,755.98 Mn (AR p.146, "Income"). 100% of revenue is domestic (AR p.145, geographical segment: "Within India").

**The gross-versus-net distinction is the single most important fact about this business model.** On a gross-accounting basis, Propel (the lowest-margin, most pass-through stream) looks like the majority of revenue (55%). On a net basis - after deducting the cost of point redemption/gift cards - Program Fees dominate net revenue. Net Revenue FY25 = Rs.6,245 Mn (Software Fees Rs.352 Mn + Program Fees Rs.5,456 Mn + Propel net Rs.437 Mn), and Adjusted EBITDA margin on that net base is 19.9%, versus just 9.6% on the reported gross-revenue base (Inv. Pres. slide 9, "Revenue mix - Net Reporting," which states: "We guide our investors to look at our revenue numbers on a Net basis after deducting cost of point redemption/gift cards on Propel... Note: Propel points are reported on a gross basis as per Ind AS").

### 1D. Simplified business model canvas

| Element | Detail |
|---|---|
| What they sell | Spend-management software (Save, Zoyer, Zatix, BROME) bundled with payment instruments (prepaid/corporate cards, gift cards, forex cards) issued via bank partners (AR p.144-145) |
| Who buys | Corporates (3,455 accounts with 250+ users, plus 635 SMB accounts up to 250 users, as of March 31, 2025 - AR p.144); end-users are employees, vendors, dealers and channel partners of those corporates (B2B2C model) |
| Why them | Deep multi-bank integration (7 named partners plus 19 total per Pres. slide 19), payment-rail integration (Visa/Mastercard/NPCI), and long-tenor contracts (3-10 years per recent wins, Inv. Pres. slide 13) create switching friction once embedded in a client's ERP/HRMS workflow |
| How delivered | Cloud dashboard + mobile app + API integrations with ERPs, HRMS, CRMs and government portals (Inv. Pres. slide 4/18) |
| Cost structure dominance | Cost of point redemption/gift cards (Rs.6,781.00 Mn, 55.9% of total expenses FY25, AR p.146-147) dwarfs every other cost line; employee benefits (Rs.667.41 Mn) and other expenses/incentives-cashback (Rs.4,432.06 Mn, of which cashback to customers Rs.3,598.72 Mn, AR p.147) are the next largest |
| Scarce resource | Bank-partner relationships and the accumulated integration/compliance stack needed to issue prepaid instruments under RBI PPI rules (AR p.144, p.150) |
| Pricing power source or absence | Asymmetric across streams: SaaS fee has genuine pricing power (multi-year subscription contracts); Program Fee economics are set largely by interchange rates negotiated with/by banks and card networks (partly outside Zaggle's control); Propel's ~6% net take rate on gift-card GMV is thin and competitive |
| Asset intensity | Light - no manufacturing plant, minimal PP&E; capitalised technology (intangible assets Rs.544.1 Mn plus Rs.220.2 Mn under development, standalone, March 2025, Inv. Pres. slide 11) is the main capitalised asset |
| WC intensity | Medium - trade receivables turnover of 6.69x (~55 days) versus trade payables turnover of 202.87x (~1.8 days) (AR p.148) means the company extends meaningful working capital to counterparties (interchange/settlement receivables from banks) while paying its own suppliers almost immediately |
| Regulatory moat or burden | Both - RBI PPI/interchange rules and multi-bank compliance create a real barrier to new entrants, but the same rulebook is a structural burden and a named risk (AR p.150, "Regulatory Risk": "Any changes in laws related to PPIs, interchange fees, or data governance could impact operations") |

### 1E. The chai-stall-uncle version
Think of Zaggle as the person who runs the "petty cash and expense counter" for hundreds of Indian companies, but does it digitally. When your company gives you a prepaid card for travel or a gift voucher for winning a sales contest, there is a good chance Zaggle built the software behind it and arranged the card or voucher through a bank. Zaggle earns money three ways: a small cut every time that card is swiped (like a toll booth taking a small fee on traffic that passes through - AR p.145, Program fee), a thin margin on gift cards and reward points it buys wholesale and resells to companies (like a sweet-shop owner who buys mithai boxes in bulk and sells them at a small markup - AR Note 42, Propel), and a subscription fee for the software dashboard itself, which is the smallest but stickiest slice of the pie (AR p.144-145, Platform/SaaS fee). The big number on the topline (Rs.13,037.57 Mn) looks dominated by the gift-card reselling business, but almost all of that money passes straight through to pay for the cards themselves - so what actually lands in Zaggle's pocket (Net Revenue of Rs.6,245 Mn, Inv. Pres. slide 9) is a very different, much smaller number, and that is the one that matters.

### Section 1 summary table

| Business type | Revenue nature | Asset intensity | WC intensity | Pricing power |
|---|---|---|---|---|
| Hybrid: B2B2C SaaS platform + payments-agency (Program fee) + principal-basis resale (Propel) | Mixed - subscription (high quality, small) + interchange revenue-share (recurring, medium quality) + pass-through resale (large gross, thin net) | Light | Medium | Moderate, asymmetric across streams |

---

## SECTION 2: INDUSTRY DYNAMICS & COMPETITIVE POSITION

### 2A. Five forces, plainly

| Force | Assessment | Helps/Hurts/Neutral |
|---|---|---|
| Competition intensity | No named competitor list or count is disclosed in the AR or presentation; management itself states: "The fintech and SaaS markets in India are highly competitive and rapidly evolving. There is a constant threat of new entrants and existing competitors launching similar or superior offerings" (AR p.150, Risk Mitigation Strategy, "Competitive Risk"). NOT FOUND: specific named competitors or market-share figures - check investor presentation or concall/research reports (ABSENT here) | Hurts |
| Entry barriers | Meaningful - requires bank-partner tie-ups (7 named + 19 total per Pres. slide 19), RBI PPI compliance, card-network integration (Visa/Mastercard/NPCI, Pres. slide 18), and multi-year enterprise sales cycles evidenced by 3,455 corporate accounts built over 14 years since 2011 incorporation (AR p.144) | Helps incumbent |
| Supplier power | "Suppliers" here are the banking partners who actually issue the underlying instruments and share interchange. AR p.150 explicitly names "Revenue Concentration Risk...High dependency on Program Fees derived from arrangements with banking partners, especially Preferred Banking Partners. Any disruption or termination of these relationships could significantly impact revenue and cash flows" | Hurts |
| Customer power / concentration | Customer base is broad and diversified across 3,455 corporate accounts (250+ users) and 635 SMB accounts, spanning BFSI, technology, healthcare, manufacturing, retail, FMCG, infrastructure, pharmaceuticals, automotive, oil & gas (AR p.144). No single-customer concentration percentage is disclosed. NOT FOUND: top-10-customer revenue concentration - check prospectus/concall | Neutral to Helps (diversification suggests low individual-customer power, but unquantified) |
| Substitutes | Manual/Excel-based expense processes, generic bank-issued corporate cards without the software layer, competing spend-management SaaS players, and the risk of banks or ERP/HRMS vendors building the same functionality in-house | Hurts |

### 2B. Competitive positioning map
NOT FOUND in the provided documents - no named direct competitors (e.g. other Indian spend-management/corporate-card SaaS players) appear in the AR or investor presentation. The presentation instead lists banking, network and VAS *partners* (HDFC, Kotak, BOI, SBI Card, Yes Bank, Axis, Mastercard, Visa, Strada, RuPay, keka, repute - Inv. Pres. slide 20) and marquee *customers* (White Oak, IIFL, Siemens, Tech Mahindra - Inv. Pres. slide 20; PNB MetLife, Indus Towers, PhysicsWallah, Wonder Home Finance, Mamaearth, Blinkit, Zepto and others - AR p.59). A true competitive map requires the prospectus, sell-side research or management commentary, none of which are provided (input gap, HIGH).

### 2C. Moat assessment table

| Moat type | Evidence | Durability |
|---|---|---|
| Switching costs | Multi-year enterprise contracts (recent wins carry 3-10 year terms, Inv. Pres. slide 13); churn "consistently under 2% in recent years" (AR p.144); deep integration with client ERP/HRMS/CRM systems (Inv. Pres. slide 4/18) | Medium-High |
| Network effects | Two-sided distribution via 19 banking partners who effectively co-sell/embed Zaggle programmes with their own corporate-card products (Inv. Pres. slide 19-20); 50 Mn+ cards issued, "#1 Prepaid Card issuer in country" (self-declared, Inv. Pres. slide 19, unverified by third-party source) | Medium - depends on continued bank cooperation; disintermediation risk is explicitly named as "Third-party Dependency Risk" (AR p.150) |
| Regulatory/licensing complexity | Multi-bank PPI compliance stack, RBI/NPCI rail integration, GDPR-aligned data practices (AR p.150, "Data Privacy & Cybersecurity Risk") | Medium |
| Brand | "#1 Spend Management company in India" and "#1 Prepaid Card issuer" are company self-declarations (Inv. Pres. slide 19); no independent brand-ranking or market-share source found | Low confidence - NOT FOUND (third-party verification) |
| Cost advantage / scale | Rs.13,037.57 Mn revenue scale and 50 Mn+ cards issued suggest some negotiating leverage with banks, but no quantified unit-cost advantage is disclosed | NOT FOUND (unquantified) |
| Data/analytics moat | Zatix (AI-driven spend analytics) and stated "AI Strategy" around zero-touch onboarding and agentic workflows (Inv. Pres. slide 15) | Low confidence - early-stage, no retention/accuracy metrics disclosed |
| Counter-positioning | NOT FOUND | - |
| Process power (integration stack) | Simultaneous integration with ERPs, HRMS, CRMs, government portals, and Visa/Mastercard/NPCI rails (Inv. Pres. slide 18) raises the bar for a new entrant to replicate the full stack | Medium |

### 2D. Industry lifecycle stage
The underlying Indian FinTech market is forecast to grow from ~Rs.9,248.91 Bn (CY2024E) to ~Rs.43,080.58 Bn (CY2030E), a 29.23% CAGR (AR p.134-135, sourced to EY/Frost & Sullivan), and India's B2B spend pool is projected to reach USD 15 trillion by 2030 (AR p.141, "Spend Management," sourced Frost & Sullivan Analysis). Within that pie, SaaS is a sliver today (~1% of FinTech revenue in 2023, projected ~2% by 2030 per the segment chart, AR p.135) - meaning Zaggle sits inside a fast-growing macro theme (digitisation of corporate spend) but its specific SaaS-fintech-hybrid niche is still emerging, not mature. Zaggle's own position: an early scaled leader by customer count and card issuance (3,455 corporates, 50 Mn+ cards) within a segment still being defined, evidenced by continuous new-product launches (Fleet Management, ZIP, BROME - all introduced or expanded "during the year under review," AR p.144-145) rather than steady-state product maturity.

### 2E. Key industry drivers

| Driver | Direction | Impact on Zaggle |
|---|---|---|
| India B2B spend growth to $15tn by 2030 (AR p.141) | Tailwind | Expands total addressable market for spend-management software |
| Indian SaaS market CAGR 27.3% to ~$70Bn industry by 2030 (AR p.141) | Tailwind | Supports the smallest but highest-quality (SaaS fee) revenue stream |
| Channel-rewards/loyalty market growing at 14% CAGR (AR p.143) | Tailwind | Supports Propel |
| Accounts-payable software market Rs.11.86 Bn (CY2024E) to Rs.21.76 Bn (CY2030E), 10.64% CAGR (AR p.143) | Tailwind | Supports Zoyer |
| Regulatory overhang - RBI/MCA/GDPR rule changes on PPIs and interchange (AR p.143, "Threats") | Headwind/risk | Could compress Program Fee economics directly |
| Entry of new global and local SaaS/fintech players (AR p.143, "Threats") | Headwind | Raises competitive intensity |
| Disruption or loss of critical third-party integrations - UPI, banks, processors (AR p.143, "Threats") | Headwind | Direct threat to the bank-partner-dependent Program Fee stream |

---

## SECTION 3: FINANCIAL METRICS THAT MATTER FOR THIS BUSINESS MODEL

### 3A. Ignore-these, track-these table

| Commonly tracked ratio | Why misleading/irrelevant here |
|---|---|
| Gross revenue growth (headline Rs.13,037.57 Mn, +68.10%, AR p.146) | ~55% of gross revenue is Propel pass-through gift-card/point revenue reported gross under Ind AS principal accounting (accounting policy note, standalone financial statements); the underlying cost of point redemption/gift cards is ~94% of that line (Rs.6,781.00 Mn against Rs.7,218.48 Mn gross Propel revenue, AR p.147). Net Revenue growth is the real growth metric to track (Inv. Pres. slide 9) |
| Gross profit margin off the P&L | Dominated by cost of point redemption/gift cards; masks true SaaS/Program-fee unit economics. Use Adjusted EBITDA margin on Net Revenue basis instead (19.9% FY25, Inv. Pres. slide 9, versus 9.6% on a gross basis) |
| Asset turnover / fixed-asset ratios | Asset-light platform business with immaterial PP&E relative to revenue; not discriminating |
| Inventory turnover | No meaningful inventory; the small "Inventories" line (Rs.3.3 Mn standalone, March 2025, Inv. Pres. slide 11) reflects prepaid-card physical stock and is immaterial to the economics of the business |
| Debt-to-equity as a standalone risk signal | Already near zero (0.01x FY25, down from 0.13x FY24, AR p.148) following QIP-funded deleveraging; not currently a discriminating risk metric, though watch for re-leveraging to fund M&A |
| Net profit margin on gross revenue (6.74%, AR p.148) taken at face value | Structurally depressed by the low-margin Propel gross-revenue drag; the same PAT of Rs.878.98 Mn measured against Net Revenue of Rs.6,245 Mn implies ~14.1% (derived), a truer profitability read |

### 3B. Must-track metrics

**Growth**

| Metric | What it tells you | Healthy range | Where to find it | Red flag threshold |
|---|---|---|---|---|
| Net Revenue growth (Program fee + SaaS fee + Propel net take) | Real top-line growth, stripped of Propel pass-through | >=25% YoY | Inv. Pres. slide 9 "Net Reporting" table; AR Note 42 | <15% YoY |
| Program fee growth | Card-spend/GMV-driven interchange growth, the largest quality-adjusted stream | >=40% YoY at this scale | AR p.145 Business Performance table | <20% YoY |
| Corporate customer count growth | New-logo momentum | >=20% YoY (25.4% CAGR FY22-FY25, AR p.144) | AR p.144 | <10% YoY |
| Users on platform (Mn) growth | End-user adoption depth per corporate | >=20% YoY | AR p.144 (3.28 Mn FY25) | Flat or declining |

**Profitability and efficiency**

| Metric | What it tells you | Healthy range | Where to find it | Red flag threshold |
|---|---|---|---|---|
| Adjusted EBITDA margin on Net Revenue basis | The true operating-leverage story | 18-25%, rising | Inv. Pres. slide 9 (19.9% FY25, 21.7% FY26) | <18% or a declining trend |
| Propel net take-rate (Net Propel / Gross Propel) | Margin quality of the pass-through stream | ~6-7%, stable/rising | Derived: Rs.437 Mn / Rs.7,218 Mn FY25 (Inv. Pres. slide 9) | <5% |
| Cost of point redemption/gift cards as % of Propel gross revenue | Structural cost ratio of the resale business | 90-95% | AR p.147 (93.94% FY25, derived from Rs.6,781.00/Rs.7,218.48) | >96% |
| Trade receivables turnover | Collection efficiency from banking-partner settlement | >=6x | AR p.148 (6.69x FY25) | <5x |
| Employee benefit expense growth vs. Net Revenue growth | Operating leverage evidence | Employee cost growth well below Net Revenue growth | AR p.147 (Employee costs +30.15% FY25 vs total revenue +68.10%) | Employee costs growing faster than Net Revenue |

**Balance sheet and risk**

| Metric | What it tells you | Healthy range | Where to find it | Red flag threshold |
|---|---|---|---|---|
| Current ratio | Liquidity (temporarily inflated by unutilised IPO/QIP proceeds) | Normalising toward 2-4x as capital deploys | AR p.148 (20.06x FY25, vs 6.18x FY24; variance flagged as "Unutilised IPO and QIP proceeds...deployed in temporary fixed deposits") | Not itself a red flag currently, but watch capital-deployment discipline |
| Debt-Equity ratio | Leverage | <0.3x | AR p.148 (0.01x FY25) | Material re-leveraging to fund M&A |
| RoCE | Capital efficiency, especially post fresh QIP capital | >=18-20% | AR p.148 (20.70% FY25, down from 22.87% FY24) | <12-15% |
| Allowance for credit losses (trade receivables) | Counterparty/settlement risk from banking partners | Declining or stable | Consolidated financial statement notes (Rs.7.88 Mn FY25 vs Rs.57.56 Mn FY24) | Rising trend |

### 3C. Industry-specific non-financial KPIs

| KPI | Value (FY25) | Where to find it |
|---|---|---|
| Corporate customer accounts | 3,455 (250+ users) + 635 SMB accounts (up to 250 users) | AR p.144 |
| Users on platform | 3.28 Mn | AR p.144 |
| Cards issued (cumulative) | 50 Mn+ | Inv. Pres. slide 19 |
| Banking/network partners | 19 (7 named: HDFC, ICICI, Axis, IndusInd, Kotak Mahindra, IDFC First, NSDL Payments Bank) | Inv. Pres. slide 19; AR p.144 |
| Customer churn | <2% "in recent years" | AR p.144 |
| Employee headcount | 425 (March 31, 2025), up from 303 (March 31, 2024) | AR p.151 |
| Credit rating | Upgraded ACUITE BBB (Stable) to BBB+ (Positive) | AR p.75 |

### 3D. Unit economics - the physics of the business

- **Unit**: one corporate customer account.
- **Revenue per unit (derived, not company-disclosed as an ARPU metric)**: ~Rs.1.81 Mn Net Revenue per corporate customer per year (Rs.6,245 Mn Net Revenue FY25, Inv. Pres. slide 9, divided by 3,455 corporate customers, AR p.144).
- **Margin per unit (derived)**: ~Rs.0.36 Mn Adjusted EBITDA per corporate customer per year (19.9% Adjusted EBITDA margin at Net basis applied to the derived revenue-per-unit figure).
- **Volume drivers**: number of corporate accounts onboarded (3,455, +14.6% YoY from 3,016, AR p.144), number of activated end-users (3.28 Mn, +20.10% YoY, AR p.147), card-spend/GMV growth per user.
- **Price drivers**: interchange rate negotiated with each banking partner (Program fee); Propel's net take-rate on gift-card/point GMV (~6%); SaaS subscription fee per module/seat (Save, Zoyer, Zatix, BROME).
- **Cost drivers**: cost of point redemption/gift cards (built structurally into the Propel take-rate, Rs.6,781.00 Mn FY25); employee/tech headcount costs (Rs.667.41 Mn, +30.15% YoY, AR p.147); customer incentives and cashback (Rs.3,598.72 Mn FY25 vs Rs.2,168.27 Mn FY24, within "Other expenses," AR p.147); capitalised technology D&A (Rs.147.94 Mn, +76.90% YoY, AR p.147, "primarily due to continuous investment in enhancement and launch of our new products").
- **Incremental margin and operating leverage**: Adjusted EBITDA margin on a Net Revenue basis rose from 19.9% (FY25) to 21.7% (FY26 per Inv. Pres. slide 9), while employee-cost growth (30.15% FY25) trailed total revenue growth (68.10%) - consistent with a scaling SaaS-plus-fintech cost base that is partly fixed (engineering, compliance, bank-integration overhead) being spread over a growing transaction/subscriber base. This is the core operating-leverage thesis to underwrite or falsify each quarter.

---

## SECTION 4: RISKS, VALUATION APPROACH & MONITORING

### 4A. Business-model-specific risks

| Category | Risk | First financial line item to deteriorate |
|---|---|---|
| Revenue model | High dependency on Program Fees derived from Preferred Banking Partner arrangements; any disruption or termination could significantly impact revenue and cash flows (AR p.150) | Program fee YoY growth deceleration, or a disclosed renegotiation/loss of a named banking partner |
| Margin | Rising cost of point redemption/gift cards ratio compresses Propel's already-thin net take (currently ~94% of Propel gross revenue, AR p.147) | Cost of point redemption/gift cards rising above ~96% of Propel gross revenue |
| Balance sheet | Receivables/settlement risk from banking-partner interchange flows and corporate customers | Trade receivables turnover falling below ~5x, or a rising trend in allowance for credit losses (currently Rs.7.88 Mn FY25 consolidated, down from Rs.57.56 Mn FY24) |
| Execution | Integration of recent acquisitions (Span Across/TaxSpanner - 98.32% subsidiary since Sept 2024, AR p.62-63; Mobileware - 38.91% associate since March 2025, AR p.63; and per the FY26 investor deck, GreenEdge and Rivpe Technology) | Continued losses at consolidated entities - Span Across already posted a loss share of Rs.(12.49) Mn in FY25 (AR Additional Disclosure, consolidated notes) |
| Structural | Disintermediation risk - banks or ERP/HRMS platforms building similar spend-management functionality in-house, or third-party (UPI/bank/processor) integration disruption (AR p.143, "Threats"; AR p.150, "Third-party Dependency Risk") | Corporate-client churn rising above the <2% baseline, or loss of a marquee client disclosed in a subsequent filing |

### 4B. Valuation method applicability table

| Method | Applicability |
|---|---|
| DCF | Applicable - a scaling platform with improving Net Revenue margin trajectory (19.9%→21.7%, Inv. Pres. slide 9) and rising Cash PAT conversion (Cash PAT > PAT in both FY25 and FY26, Inv. Pres. slides 6/10) supports explicit multi-year cash-flow modelling. **PRIMARY** |
| EV/EBITDA (Net Revenue basis) | Applicable as a cross-check, provided EBITDA is normalised to the Net Revenue base to correct for the Propel gross/net distortion. **SECONDARY** |
| EV/Sales (Net Revenue basis) | Usable only as a sanity check during periods of margin volatility (e.g., M&A integration noise); must use Net, not Gross, revenue or the multiple is structurally distorted downward. **TERTIARY** |
| P/E | Usable but distorted by ESOP costs and one-off items (e.g., a gain on re-measurement of an associate investment flagged in the FY25 MD&A, AR p.146, "Income"); better read on a Cash PAT basis |
| Sum-of-parts (SaaS vs. Program-fee/fintech-distribution vs. Propel vs. recently acquired TaxSpanner/Mobileware) | Conceptually the cleanest lens given three structurally different economics, but segment-level P&L by product is NOT FOUND in the provided documents beyond the three-line revenue table (AR p.145) |
| Dividend discount model | Not applicable - no dividend recommended for FY25; company stated it will "conserve funds to maximize the Shareholders wealth on the long run" (AR p.59) |
| Asset-based / replacement cost | Not applicable - asset-light business, book value not meaningful |
| Comparable transactions | Not applicable with confidence - insufficient disclosed detail on acquired-entity standalone financials (e.g. Span Across, Mobileware) to derive a clean transaction multiple from the company's own M&A (AR p.62-63) |

**Cycle stage for valuation**: early-to-mid growth/scaling stage of a secular, still-nascent Indian SaaS-fintech niche (revenue +68.10% FY25, +42.2% FY26 standalone, Inv. Pres. slide 6) - valuation should weight forward Net Revenue growth durability and margin trajectory over trailing gross-revenue multiples.

### 4C. Quarterly monitoring checklist

1. Net Revenue growth YoY (ex-Propel gross pass-through) - good: >=25%; trouble: <15%.
2. Adjusted EBITDA margin on Net Revenue basis - good: rising toward/above 20-22%; trouble: <18%.
3. Program fee revenue growth YoY - good: >=40%; trouble: <20%.
4. Propel net take-rate (Net/Gross Propel revenue) - good: stable/rising ~6-7%; trouble: <5%.
5. Corporate customer count and growth rate - good: >=20% YoY; trouble: <10%.
6. Aggregate users on platform (Mn) - good: >=20% YoY; trouble: flat/declining.
7. Customer churn rate - good: <2%; trouble: >3%.
8. Cost of point redemption/gift cards as % of Propel gross revenue - good: ~93-95%; trouble: >96%.
9. Employee benefit expense growth vs. Net Revenue growth - good: employee cost growth well below Net Revenue growth; trouble: employee costs outgrowing Net Revenue.
10. Trade receivables turnover - good: >=6x; trouble: <5x.
11. QIP capital deployment progress (Rs.5,948.41 Mn raised, AR p.60-61) - good: deployed per stated objects into accretive growth/M&A; trouble: idle cash dragging RoCE, or non-accretive M&A.
12. RoCE - good: sustained >=18-20%; trouble: <12-15%.
13. Associate/subsidiary performance (Span Across/TaxSpanner, Mobileware) - good: turning profitable; trouble: continuing losses.
14. Banking-partner count/concentration - good: stable/growing partner base with no single-bank dependency disclosed; trouble: loss of a Preferred Banking Partner.
15. Credit rating trajectory - good: continued upgrades (currently BBB+/Positive, AR p.75); trouble: outlook downgrade.

### 4D. Highest-value questions for management

1. What is the underlying Propel take-rate trend, and is it structurally improving or being competed away? *Reassures*: stable/improving take-rate. *Worries*: steady erosion toward the low single digits.
2. How concentrated is Program Fee revenue among the top 2-3 banking partners, and what termination/renewal protections exist? *Reassures*: diversified across the 19 partners with long-tenor agreements. *Worries*: a single bank representing a large share of Program Fees.
3. What is the path to breakeven for Span Across (TaxSpanner), which posted a loss share in FY25? *Reassures*: a clear breakeven timeline with visible cross-sell traction. *Worries*: continued drag with no measurable synergy.
4. How is the Rs.5,948.41 Mn QIP capital (with Rs.3,750 Mn allocated to strategic investments/M&A, AR p.61) being underwritten, and what return hurdle governs recent deals (Span Across, Mobileware, and per the FY26 deck, Rivpe, GreenEdge)? *Reassures*: disciplined, accretive multiples disclosed. *Worries*: opportunistic or dilutive diversification.
5. How sensitive is Program Fee revenue to regulatory changes in interchange/PPI rules (RBI/NPCI)? *Reassures*: contractually protected margins or a diversified fee structure. *Worries*: high direct pass-through exposure to a regulatory fee cap.
6. What is the SaaS-only (Platform/SaaS fee) growth rate and net revenue retention, isolated from Program Fee and Propel? *Reassures*: strong retention (>110%) and accelerating SaaS-only growth. *Worries*: the current 16.06% FY25 growth in this stream (AR p.147) versus 68.10% total revenue growth, suggesting SaaS is a small, slow-growing sliver of the model.
7. What is the deployment timeline for the idle cash driving the 20.06x current ratio, and how will it affect RoE (7.04% FY25, AR p.148-149)? *Reassures*: a committed near-term deployment plan with returns above cost of capital. *Worries*: prolonged idle cash suppressing return ratios.

---

## SECTION 5: ONE-PAGE BUSINESS MODEL SUMMARY CARD

| | |
|---|---|
| **Company** | Zaggle Prepaid Ocean Services Limited (ZAGGLE) |
| **Business type** | Hybrid: B2B2C SaaS platform + payments-agency (Program fee) + principal-basis resale (Propel) |
| **One-liner** | Digitises corporate spend and monetises it via a bank interchange share, principal-basis gift-card resale, and a small SaaS subscription layer |
| **Revenue streams (FY25, AR p.145)** | Propel platform revenue/gift cards 55.37% (gross); Program fee 41.85%; Platform/SaaS fee 2.78% |
| **Net Revenue (Inv. Pres. slide 9)** | Rs.6,245 Mn FY25 (vs Rs.13,037.57 Mn gross) |
| **Adjusted EBITDA margin** | 9.6% on gross revenue / 19.9% on Net Revenue basis (FY25, Inv. Pres. slide 9) |
| **PAT / margin** | Rs.878.98 Mn / 6.74% (gross basis, AR p.148) |
| **Asset intensity** | Light |
| **WC intensity** | Medium (receivables turnover 6.69x vs payables turnover 202.87x, AR p.148) |
| **Pricing power** | Moderate, asymmetric across streams |
| **Cyclicality** | Secular-growth (India digitisation of corporate spend), with macro/geopolitical sensitivity named as a risk (AR p.150) |
| **Key moats** | Switching costs (multi-year contracts, <2% churn) - Medium-High durability; bank-partner network/distribution - Medium durability; regulatory/integration complexity - Medium durability |
| **Top risk** | Revenue concentration in Program Fees tied to Preferred Banking Partners (AR p.150) |
| **Primary valuation method** | DCF on Net Revenue/normalised EBITDA |
| **Verdict** | Fast-scaling spend platform; net revenue quality, not gross revenue growth, is the number to underwrite |

---

```yaml
stage: B04-bizmodel
company: "ZAGGLE"
run_date: "2026-07-27"
model: claude-sonnet-5
status: complete
input_gaps:
  - "Prospectus/IPO offer document ABSENT (HIGH) - fullest business-model, risk-factor and peer detail typically lives here"
  - "Stock exchange announcements ABSENT"
  - "Shareholding pattern ABSENT"
  - "Independent/sell-side research ABSENT - no named competitor list or market-share benchmark found in AR or investor presentation"
  - "Investor presentation covers FY26 (May 2026 deck), a period beyond the FY25 AR window; used only as secondary/directional context, not as the anchor for FY25 revenue-mix figures"
flags:
  - "Gross revenue (Rs.13,037.57 Mn FY25) is structurally misleading as a growth/scale metric because ~55% is Propel pass-through gift-card revenue with a ~94% cost ratio; Net Revenue (Rs.6,245 Mn) and Net-basis Adjusted EBITDA margin (19.9%) are the metrics that matter"
  - "No named direct competitors identified in provided documents; competitive-positioning claims ('#1 Spend Management company', '#1 Prepaid Card issuer') are company self-declarations (Inv. Pres. slide 19), not third-party verified"
  - "Span Across (TaxSpanner) subsidiary posted a loss share of Rs.(12.49) Mn in FY25 (consolidated additional disclosure) - early M&A integration is a live drag, not yet a proven success"
  - "Program Fees, the largest quality-adjusted revenue stream, carry explicit management-acknowledged concentration risk on Preferred Banking Partners (AR p.150)"
business_type: "hybrid"
revenue_streams:
  - {name: "Program fee (interchange revenue share via bank partners)", type: "transaction/usage-based, agency-like", pct_of_revenue: 41.85, predictability: "M"}
  - {name: "Propel platform revenue / gift cards", type: "principal-basis resale (goods, point-in-time)", pct_of_revenue: 55.37, predictability: "L"}
  - {name: "Platform fee / SaaS fee / service fee", type: "subscription/SaaS (services, over time)", pct_of_revenue: 2.78, predictability: "H"}
asset_intensity: "light"
wc_intensity: "medium"
pricing_power: "moderate"
cyclicality: "secular-growth"
moats_present:
  - {moat: "Switching costs (multi-year contracts 3-10yr, <2% churn)", durability: "medium-high"}
  - {moat: "Bank-partner distribution network (19 partners)", durability: "medium"}
  - {moat: "Regulatory/integration complexity (RBI PPI, card-network rails)", durability: "medium"}
valuation_methods:
  primary: {method: "DCF (Net Revenue-driven, 3-5yr explicit forecast)", why: "Scaling SaaS-fintech platform with rising Adjusted EBITDA margin on Net Revenue basis (19.9% FY25 to 21.7% FY26, Inv. Pres. slide 9) and improving Cash PAT conversion; fits a 3-5yr GARP transition-alpha hold"}
  secondary: {method: "EV/EBITDA on Net Revenue basis", why: "Cross-check multiple normalised for the gross-vs-net revenue distortion created by Propel principal-basis pass-through accounting"}
  tertiary: {method: "EV/Sales on Net Revenue basis", why: "Sanity-check only during periods of M&A-driven margin volatility; must use Net, not Gross, revenue"}
  not_applicable:
    - "Dividend discount model (no dividend declared FY25, AR p.59)"
    - "Asset-based/replacement cost (asset-light business, book value not meaningful)"
    - "Comparable-transactions method (insufficient disclosed detail on acquired-entity standalone financials)"
irrelevant_ratios:
  - {ratio: "Gross revenue growth", why: "~55% of gross revenue is Propel pass-through gift-card revenue with a ~94% cost ratio; Net Revenue growth is the real metric"}
  - {ratio: "Gross profit margin off the P&L", why: "Dominated by cost of point redemption/gift cards; use Adjusted EBITDA margin on Net Revenue basis instead"}
  - {ratio: "Asset turnover / fixed-asset ratios", why: "Asset-light platform business, PP&E immaterial"}
  - {ratio: "Inventory turnover", why: "No meaningful inventory; the small Inventories line is immaterial prepaid-card stock"}
  - {ratio: "Debt-to-equity as a standalone risk signal", why: "Already near zero (0.01x FY25) post QIP-funded deleveraging; not currently discriminating"}
must_track_metrics:
  - {metric: "Net Revenue growth (ex-Propel gross pass-through)", healthy: ">=25% YoY", red_flag: "<15% YoY"}
  - {metric: "Adjusted EBITDA margin on Net Revenue basis", healthy: "18-25%, rising", red_flag: "<18% or declining"}
  - {metric: "Propel net take-rate (Net/Gross Propel revenue)", healthy: "6-7%, stable/rising", red_flag: "<5%"}
  - {metric: "Corporate customer count growth", healthy: ">=20% YoY", red_flag: "<10% YoY"}
  - {metric: "Customer churn rate", healthy: "<2%", red_flag: ">3%"}
unit_economics:
  unit: "one corporate customer account"
  revenue_per_unit: "~Rs.1.81 Mn Net Revenue/customer/year (derived: FY25 Net Revenue Rs.6,245 Mn / 3,455 corporate customers)"
  margin_per_unit: "~Rs.0.36 Mn Adjusted EBITDA/customer/year (derived: 19.9% Adj EBITDA margin at Net basis)"
  key_lever: "Cross-sell of additional modules (Save/Zoyer/Propel/Zatix/ZIP) into existing corporate accounts plus GMV/card-spend growth per user, more than new-logo addition alone"
first_deterioration_signals:
  - {risk: "Revenue model - Program Fee concentration on banking partners", first_signal: "Program fee YoY growth deceleration or a disclosed loss/renegotiation of a Preferred Banking Partner"}
  - {risk: "Margin - rising cost of point redemption on Propel", first_signal: "Cost of point redemption/gift cards rising above ~96% of Propel gross revenue"}
  - {risk: "Balance sheet - receivables/settlement lag from banking partners", first_signal: "Trade receivables turnover falling below ~5x, or rising allowance for credit losses"}
  - {risk: "Execution - M&A integration (Span Across/Mobileware and newer deals)", first_signal: "Continued losses at consolidated subsidiaries/associates (Span Across already loss-making in FY25)"}
  - {risk: "Structural - disintermediation by banks/ERP-HRMS platforms", first_signal: "Corporate-client churn rising above the <2% baseline"}
mgmt_questions:
  - "What is the underlying Propel take-rate trend, and is it structurally improving or being competed away?"
  - "How concentrated is Program Fee revenue among the top 2-3 banking partners, and what termination/renewal protections exist?"
  - "What is the path to breakeven for Span Across (TaxSpanner), which posted a loss share in FY25?"
  - "How is the Rs.5,948.41 Mn QIP capital being underwritten, and what return hurdle governs recent M&A?"
  - "How sensitive is Program Fee revenue to regulatory changes in interchange/PPI rules?"
  - "What is the SaaS-only (Platform/SaaS fee) growth rate and net revenue retention, isolated from Program Fee and Propel?"
  - "What is the deployment timeline for the idle cash driving the 20.06x current ratio, and how will it affect RoE?"
one_line_verdict: "Fast-scaling spend platform; net revenue quality, not gross revenue growth, is the number to underwrite."
```
