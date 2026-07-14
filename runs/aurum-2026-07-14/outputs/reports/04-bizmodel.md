# STAGE 4: BUSINESS MODEL DECODER — Aurum Proptech Ltd (AURUM)
Run date: 2026-07-14 | Model: claude-sonnet-5

---

## SECTION 1: THE BUSINESS MODEL IN PLAIN ENGLISH

### 1A. One-line description

Aurum Proptech is a three-legged Indian real-estate technology holding company that rents out managed homes (Rental), sells data, leads and CRM software to real-estate developers and brokers (Distribution), and is starting to package real-estate as an investable financial product (Capital) — with Distribution now the profit engine and Rental the largest revenue line (AR FY25 p.51, segment table; results press release Apr-23-2026).

### 1B. Money-flow chain for each revenue stream

| # | Stream | [Input] | [What Aurum does] | [What it delivers] | [Who pays] | [How they pay] |
|---|--------|---------|--------------------|--------------------|------------|-----------------|
| 1 | NestAway (managed rentals) | Landlord's vacant flat | Sources, lists, furnishes/manages, finds tenant, collects rent | A rented, managed home | Landlord (commission) + Tenant (blended fee) | Landlord pays "10% Recurring commission"; Tenant pays "5% blended commission... through move in move out and cancellation" (Inv. Pres. Q2 FY26 slide 13/p.13, "NestAway" economics box) |
| 2 | HelloWorld (co-living) | Landlord's building, leased long-term | Takes 5-7 year property lock-in, converts to co-living inventory, operates community/services | A branded co-living bed | Tenant (rent + service fee) | Monthly rent paid by resident; property secured via "long term agreements (5-7 yrs)" (Inv. Pres. Q2 FY26 slide 14/p.14) |
| 3 | Aurum Analytica | Developer's need for buyers | Builds/targets lookalike audiences off a "150M+ social profile" data lake, runs digital campaigns | Qualified sales leads | Real-estate developer | Per-lead / campaign fee (Inv. Pres. Q2 FY26 slide 18/p.17-18) |
| 4 | Sell.do | Developer/broker's disorganized sales process | Provides cloud CRM (pre-sales, sales, post-sales modules) | Software licenses/seats, individual + enterprise deployment | Real-estate developer/broker | SaaS license fee per seat/account (Inv. Pres. Q2 FY26 slide 19) |
| 5 | PropTiger | Developer's unsold inventory | Digital lead-gen + on-ground relationship-manager sales force + buyer financing tie-ups | A closed home sale | Developer (on closed transactions) | Gross commission on transaction value ("Highest-ever gross commission since inception," Q4 FY26 results press release p.3) |
| 6 | Capital / SM-REIT (AMSA) | Retail/HNI investor capital + commercial real-estate SPVs | Pools investor money into SEBI-regulated SM-REIT schemes holding commercial assets | Rental yield + capital appreciation units listed on BSE/NSE | Investor (min ₹10L per Inv. Pres.) via investment management fee (5%/15% investment by IM disclosed; fee structure beyond that NOT FOUND) | SEBI registration obtained (AR FY25 p.50, "SEBI registration certificate for AMSA"); first scheme not yet launched as of Q4 FY26 (B07-emoat catalysts_12m) |

### 1C. Revenue model classification table

| Stream | Type | Description | % of revenue (anchored) | Predictability |
|--------|------|--------------|---------------------------|-----------------|
| Rental (NestAway + HelloWorld) | Operating-lease / marketplace commission hybrid | Company takes on the property (own lease liability for HelloWorld) or acts as managing agent (NestAway), monetising via rent spread + commissions | 63.9% of FY25 consolidated revenue: ₹168.62 Cr of ₹263.84 Cr (AR FY25 p.51, Segment wise performance table; Note 23 consolidated, p.267/154 in printed pagination) | Medium — recurring monthly cash flow but occupancy- and churn-sensitive; segment still loss-making in FY25 (segment result −₹14.54 Cr) |
| Distribution (Aurum Analytica + Sell.do + PropTiger) | Blended: SaaS recurring license (Sell.do) + pay-per-lead (Analytica) + transaction commission (PropTiger) | Sale of leads, software licenses and closed-deal commissions to developers/brokers | 30.1% of FY25 consolidated revenue: ₹79.28 Cr of ₹263.84 Cr (AR FY25 p.51); rose to "~60% of income" per operator narrative for FY26 post-PropTiger consolidation (OPERATOR_CONTEXT.md item 7, operator-supplied, NOT independently anchored to a primary FY26 segment table in the documents collected for this run — see input_gaps) | Medium-High for Sell.do (recurring license); Low-Medium for Analytica/PropTiger (lead volume and transaction-count driven, cyclical with housing sales) |
| Capital (SM-REIT/AMSA + legacy Integrow/YieldWiseX/SPVs) | Asset management fee (nascent) | Investment management of SM-REIT schemes and legacy SPV structuring | 6.0% of FY25 consolidated revenue: ₹15.94 Cr of ₹263.84 Cr, +137.12% YoY off a small base (AR FY25 p.51) | Low — pre-scale; still loss-making (segment result −₹7.39 Cr FY25); one Group entity (Integrow) carries a confirmed CARO loan/interest default (B02-notes.yaml, rank 1) |

Note on FY26: total consolidated income reached ₹424 Cr (+49% YoY) with ARR crossing ₹500 Cr (results press release Apr-23-2026, p.2), but no FY26 segment-level revenue/profit table was present in the results press releases collected for this run (only operational KPIs, not the Ind AS 108 segment note). FY26 segment revenue splits cited anywhere in this report are OPERATOR_CONTEXT.md figures, carried as directional/secondary, not primary-source anchored — see input_gaps.

### 1D. Simplified business model canvas

| Element | Rental | Distribution | Capital |
|---|---|---|---|
| What they sell | Managed rental housing | Leads, CRM software, brokerage | Investment products (SM-REIT units) |
| Who buys | Tenants (young professionals, students, families) + landlords | Real-estate developers, brokers | Retail/HNI investors, family offices |
| Why them | Aggregated inventory, standardized experience, tech-enabled discovery (AR FY25 p.51-59; Inv. Pres. Q2 FY26 slide 13-14) | Real-estate-specific CRM (vs. generic Salesforce), proprietary lookalike-audience data lake ("150M+ social profiles") (Inv. Pres. Q2 FY26 slide 18) | First-mover SEBI SM-REIT registration under the AMSA brand (AR FY25 p.50) |
| How delivered | App + on-ground property operations teams, hub-and-spoke service model (Inv. Pres. Q2 FY26 slide 13) | Cloud SaaS + campaign execution + relationship-manager sales force (PropTiger) | Regulated fund/scheme structure |
| Cost structure dominance | Property lease/rent payments (long-term lease liability, Ind AS 116 RoU), on-ground ops staff | Employee cost (engineering, sales, data), marketing spend for lead generation | Legal/compliance/SEBI registration cost, SPV structuring |
| Scarce resource | Exclusive property inventory in supply-constrained micro-markets, tenant/owner stickiness | Proprietary developer relationships (950+ per Inv. Pres.), the 150M+ social-profile data lake | SM-REIT license (SEBI-regulated, not open to all comers) |
| Pricing power source (or absence) | Weak-to-moderate: commission % benchmarked to market norms (10% landlord / 5% tenant blended, Inv. Pres. slide 13); competitive market with NoBroker, Housing.com, Stanza Living, ZoloStays (Dolat Capital note, non-anchored, p.2187-2188) | Moderate for Sell.do (real-estate-specific feature depth vs. generic CRM per broker note, non-anchored); weak for Analytica (lead pricing is volume/market-competitive) | Undetermined — pre-scale, no live AUM-based fee track record (NOT FOUND) |
| Asset intensity | Medium-heavy: HelloWorld carries long-term lease liabilities (Ind AS 116 RoU); consolidated lease liabilities ₹192.33 Cr vs. total borrowings ₹81.01 Cr, i.e., 2.4x (B02-notes.yaml, rank 10, Note 3.b p.135) | Light: software/data assets, minimal fixed capital | Light: fee-based, no balance-sheet real-estate exposure by design (SM-REIT holds assets in SPVs, not on Aurum's own book) |
| WC intensity | Medium: security-deposit/rent-collection timing mismatches; receivables ageing has deteriorated Group-wide (>1yr bucket +327% YoY per B02-notes.yaml) though this is not segment-isolated in the documents reviewed | Medium: B2B receivables from developers, no evidence of negative WC / upfront-cash SaaS model found in this run (contract-liability/unearned-revenue balances not separately sized — NOT FOUND) | Low volume currently; WC profile NOT FOUND at segment level |
| Regulatory moat or burden | Burden: RERA-adjacent tenancy/rent-control exposure across states (qualitative; no specific regulatory citation found in this run) | Neutral | Moat: SEBI SM-REIT registration is a regulated, licensed activity — genuine barrier to new entrants (AR FY25 p.50) |

### 1E. The chai-stall-uncle version

Think of Aurum like a landlord-turned-broker-turned-banker, all under one roof. First, they rent out furnished flats and co-living rooms to young people moving to the city — like a hostel warden who also collects the rent for the building owner and takes a cut from both sides. Second, they sell "customer leads" and computer software to the builders who build those flats, the way a matchmaker sells rishtas — except here the matches are between builders and buyers, and the software is the ledger book that keeps every conversation organized. Third, they have just gotten a government license (SM-REIT) to let ordinary people invest small amounts of money into commercial buildings the way you'd buy a mutual fund, instead of needing crores to buy a whole office. Right now, the matchmaking-and-software business (Distribution) is the one making money; the rental business is the biggest but is only just breaking even; and the investment-product business is the newest, smallest, and still finding its feet.

### Section 1 summary table

| Field | Value |
|---|---|
| Business type | Hybrid — platform/services conglomerate with three distinct sub-models (operating-lease rental marketplace, B2B SaaS/lead-gen/brokerage, nascent regulated asset management) |
| Revenue nature | Mixed recurring (SaaS license, managed-rental rent) + transactional (leads, brokerage commission) |
| Asset intensity | Medium — light on paper (goodwill/intangibles-heavy, not PP&E-heavy after May-2026 building sale) but heavy on lease liabilities (Ind AS 116 RoU dominates the true fixed-obligation load; see B02-notes.yaml rank 10) |
| WC intensity | Medium, with a deteriorating trend flag (Group receivables ageing worsening per B02-notes.yaml) |
| Pricing power | Weak-to-moderate and segment-dependent — moderate in Sell.do (real-estate-specific SaaS niche), weak-to-market-rate in Rental commissions and Analytica lead pricing |

---

## SECTION 2: INDUSTRY DYNAMICS & COMPETITIVE POSITION

### 2A. Five forces, plainly

| Force | Assessment | Helps / Hurts / Neutral |
|---|---|---|
| Competition count (Rental) | NoBroker, Housing.com, Stanza Living, ZoloStays named as direct competitors in Rental/Co-living (Dolat Capital note, non-anchored, p.2187-2188) | Hurts — crowded, well-funded field |
| Competition count (Distribution) | Sell.do competes against generalist CRMs (Salesforce, Zoho) and real-estate-specific players (99acres cited as "closest peer" for Analytica) per broker note (non-anchored) | Neutral-to-helps for Sell.do (real-estate-specific niche defensible per broker note); hurts for Analytica (broad lead-gen competition) |
| Entry barriers (Rental) | Low-to-medium: requires landlord relationships and working capital for lease commitments, not deep tech moat | Hurts |
| Entry barriers (Capital/SM-REIT) | High: SEBI registration required, AMSA already holds it (AR FY25 p.50) | Helps |
| Supplier power | Landlords/property owners hold pricing power over inventory access in Rental; real-estate developers hold power over data/lead-gen mandates in Distribution | Hurts (Rental); Neutral (Distribution — Aurum has "950+ Real Estate Developer Relations", Inv. Pres. Q2 FY26 p.8) |
| Customer power / concentration | Distribution customer base is diversified across developers (140-175+ active clients per quarter, various presentations); no single-customer concentration disclosed | Helps (diversification), but no formal concentration disclosure found — NOT FOUND |
| Substitutes | Direct landlord-tenant deals (no intermediary) for Rental; in-house developer sales/marketing teams for Distribution; direct property purchase (no REIT) for Capital | Hurts — all three verticals face a "do it yourself" substitute |

### 2B. Competitive positioning map (documents-identifiable competitors only; broker-note sourced, non-anchored)

| Segment | Named competitors | Aurum's stated differentiator |
|---|---|---|
| Rental / Co-living | NoBroker, Housing.com, Stanza Living, ZoloStays (Dolat Capital note, non-anchored) | Combined managed-rentals + co-living scale: "one of the largest Co-living player in India," 19,000+ rental units under management, 15+ cities (Inv. Pres. Q2 FY26 slide 13) |
| CRM / SaaS | Salesforce, Zoho (generalist); positioned as real-estate-specific vs. these (Dolat Capital note, non-anchored) | "no direct competition in terms of real-estate focused CRM" per broker note (non-anchored claim, not independently verified in this run) |
| Data/lead-gen | 99acres cited as closest peer (Dolat Capital note, non-anchored) | Proprietary "150M+ social profiles" lookalike-audience data lake (Inv. Pres. Q2 FY26 slide 18) |
| Capital / SM-REIT | Peer SM-REIT sponsors NOT FOUND in documents reviewed | First-mover SEBI SM-REIT registration under AMSA brand |

### 2C. Moat assessment (eight standard types)

| Moat type | Present? | Evidence | Durability |
|---|---|---|---|
| Network effects | Weak/emerging | Two-sided marketplace in NestAway (landlord + tenant), but no disclosed liquidity/density metric proving network effects vs. simple scale (NOT FOUND) | Low confidence |
| Switching costs | Moderate (Sell.do only) | Developer CRM embeds sales workflow/data; company flags "cross-sell" thesis but management itself says ecosystem revenue is "still in single digit" (Concall Apr-2026 Transcript, lines 623-626) | Weak-to-moderate, unproven at scale |
| Cost advantages / scale | Weak | No disclosed unit-cost advantage vs. peers; broker note claims lower CAC trend but non-anchored (Dolat Capital note p.169-170) | Low confidence |
| Brand | Weak-moderate | HelloWorld/NestAway are recognized co-living/rental brands (AR FY25 narrative), but no brand-premium pricing evidence | Weak |
| Regulatory / licensing | Moderate-Strong (Capital segment only) | SEBI SM-REIT registration (AR FY25 p.50) is a genuine licensed-activity barrier | Durable if scheme launches; currently unmonetized ("wait and watch" per B07-emoat catalysts) |
| Proprietary data/IP | Weak | Central management narrative ("Unified Brain," "data is the biggest moat" — Concall Apr-2026, line 159, 321-324) but B07-emoat scan independently rated this the weakest-evidenced category (D1, A2 both "Weak") — no disclosed model-performance metric, patent filing, or monetized AI product beyond calling bots/lead scoring |
| Ecosystem / cross-sell lock-in | Weak, quantified as immaterial | 22% multi-product customers / 27% developer multi-product billing cited in presentations, but founder confirms cross-sell revenue is "still in single digit" (Concall Apr-2026, lines 623-626) — real but currently P&L-immaterial |
| Execution / management track record | Moderate, improving | Two consecutive profitable quarters delivered against guidance (Q3+Q4 FY26); B07-emoat rates F2 (execution moat) "Moderate," "already emerging" | Improving but only two data points |

**Overall moat read:** thin and mostly regulatory (SM-REIT) or execution-based (recent delivery), not yet structural (data/network/brand). This matters directly for valuation — see Section 4B.

### 2D. Industry lifecycle stage

Indian PropTech distribution/SaaS: growth stage, riding formalization of a fragmented ₹39,000 Cr annual real-estate distribution spend (Inv. Pres. Q2 FY26 slide 17, "A ₹39,000 crore Opportunity"). Managed rental/co-living: early-growth, large demand-supply gap cited as "25x" (Inv. Pres. Q2 FY26 slide 12) but still sub-scale and loss-making at the segment level in FY25. SM-REIT/Capital: nascent/pre-commercialization — the regulatory framework itself is new (SEBI SM-REIT regulations), first scheme not yet launched.

Aurum's position: a consolidator within this fragmented landscape (multiple bolt-on acquisitions — NestAway, HelloWorld, Aurum Analytica, PropTiger — per AR subsidiary list), transitioning from cash-burning roll-up to (barely) profitable operator in FY26.

### 2E. Key industry drivers

| Driver | Direction | Impact on Aurum |
|---|---|---|
| Urbanization / rental housing demand-supply gap | Positive, structural | Tailwind for Rental (25x demand-supply gap cited, Inv. Pres. slide 12) |
| Real-estate distribution digitization (developer tech adoption) | Positive, structural | Tailwind for Sell.do/Analytica |
| SM-REIT regulatory framework maturation | Positive but early | Tailwind for Capital, contingent on scheme launches actually happening |
| Housing sales cyclicality (macro rate cycle, affordability) | Cyclical | Direct risk to PropTiger (transaction commission) and Analytica (lead volume tied to developer marketing budgets) |
| AI adoption in sales/ops (company's own stated strategy) | Company-narrative-positive, unproven | Central to FY27 "Unified Brain" pitch; currently thin evidence per B07-emoat |

---

## SECTION 3: FINANCIAL METRICS THAT MATTER FOR THIS BUSINESS MODEL

### 3A. Ignore-these / track-these table

| Commonly tracked ratio | Verdict | Why misleading/irrelevant here |
|---|---|---|
| Reported EBITDA margin (as per Ind AS, unadjusted) | MISLEADING | Company's own P&L build shows reported EBITDA/Total Income of 30.3% in Q3 FY26 vs. Adjusted EBITDA/Adjusted Income of only 6.5% — the gap is entirely Ind AS 116 lease accounting (RoU-related other income added back, then long-term lease payments of ₹24.01 Cr deducted as a real cash cost) (pres_40dceab1, Q3 FY26 pres p.25, "Profit & Loss Build-up" table). Reported EBITDA overstates cash profitability roughly 4-5x. Always use company-disclosed Adjusted EBITDA, and verify the reconciliation each quarter. |
| Standard P/E on trailing earnings | IRRELEVANT (for now) | FY26 is the first (barely) profitable year (PAT margin still near breakeven; Q3 FY26 PAT ₹2.71 Cr was the first-ever positive quarter per OPERATOR_CONTEXT item 1); trailing P/E is either meaningless (negative) or based on one-off-inflated earnings (Q4 FY26 included a ₹17.72 Cr one-time building-sale gain in other income, per OPERATOR_CONTEXT item 4) |
| Debt/Equity or interest coverage using reported borrowings only | MISLEADING | Consolidated lease liabilities (₹192.33 Cr) are 2.4x total borrowings (₹81.01 Cr); real fixed-obligation leverage is understated by conventional debt ratios (B02-notes.yaml rank 10) |
| Current ratio (standalone) | MISLEADING | Standalone current ratio jumped to 8.70x, but management itself attributes this to an intercompany-loan reclassification artifact, not real liquidity improvement (B03-ardeep.yaml, rank/monitorable on DSCR) |
| Single blended gross margin % | IRRELEVANT as a single number | Three segments have structurally different margins (SaaS-like Sell.do vs. commission-based PropTiger vs. lease-heavy Rental); a blended figure hides which engine is actually working |
| Inventory turnover / days inventory | NOT APPLICABLE | No physical inventory in this business model (software/leads/managed-rental services) |
| Fixed-asset turnover | LOW VALUE | Post May-2026 building sale the company is "debt-free" and asset-light on owned PP&E; the real capital intensity sits in operating leases (off the traditional fixed-asset base) |

### 3B. Must-track metrics

**Growth**

| Metric | What it tells you | Healthy range (this business) | Where to find it | Red flag threshold |
|---|---|---|---|---|
| ARR (Annualised Recurring Revenue) | Scale and recurring-revenue base, company's own headline KPI | Growing toward stated ₹1,000 Cr, 3-year target (OPERATOR_CONTEXT item 1) | Quarterly results press release / investor presentation | ARR growth decelerating below prior guidance cadence |
| Segment revenue growth (Rental / Distribution / Capital), split | Which engine is actually driving growth | Distribution sustaining 40%+ historical CAGR per management ("Five years of 40%+ CAGR," OPERATOR_CONTEXT item 4) | AR segment note (Note 23) / quarterly results (NOTE: FY26 quarterly segment table not found in documents collected this run — see input_gaps) | Any segment reverting to single-digit or negative growth without explanation |
| Number of active licenses (Sell.do) / active accounts | SaaS-style recurring-seat growth | Sequential accretion each quarter (9,559→10,378 licenses per OPERATOR_CONTEXT items 1 and 4) | Investor presentation KPI slide | Flat or declining license/account count |

**Profitability and efficiency**

| Metric | What it tells you | Healthy range | Where to find it | Red flag threshold |
|---|---|---|---|---|
| Adjusted EBITDA margin (company-defined, post-lease-payment) | True cash operating profitability, correcting for Ind AS 116 distortion | Trending toward the medium-term "8-10% PAT margin" target (OPERATOR_CONTEXT item 1); FY26 print 5.9%, Q4 FY26 12.2% (results press release Apr-23-2026) | Quarterly results, "Adjusted EBITDA" reconciliation slide | Adjusted EBITDA margin reversing quarter-on-quarter after the FY26 inflection |
| Segment profit/loss by SBU | Which of Rental/Distribution/Capital is actually earning its capital | Distribution profitable and expanding (FY26 segment profit ₹32.3 Cr per OPERATOR_CONTEXT); Rental targeting FY27 breakeven | AR Note 23 (annual); FY26 quarterly equivalent not found in this run's documents | Distribution segment profit growth stalling (it currently funds the other two segments) |
| Revenue per team member (company KPI) | Labour productivity / AI-driven efficiency claim, management's own "guiding metric" for the AI pivot (Concall Apr-2026, line 157-159) | Quarter-on-quarter improvement (₹21L→₹27L Net Revenue per Team Member, NestAway, Q2→Q3 FY26; Distribution revenue-per-team-member ₹26L→₹30L over same window) (Inv. Pres. Q2 FY26 p.5; Q3 FY26 pres p.5) | Investor presentation KPI table | Flat or declining revenue per team member despite AI-spend narrative |
| PBT margin | Bottom-line trajectory, cleanest single number now that PAT has turned positive | Sustained positive after two consecutive quarters (Q3 FY26 +1.6%, Q4 FY26 +2.5%) (pres_40dceab1 p.25; results press release Apr-2026 p.2) | Quarterly results | Reversion to negative PBT margin ex-one-offs |

**Balance sheet and risk**

| Metric | What it tells you | Healthy range | Where to find it | Red flag threshold |
|---|---|---|---|---|
| Lease liability vs. operating cash flow coverage | Real fixed-obligation burden the debt ratios hide | Lease cash outflow should fall below CFO, not exceed it | AR cash flow statement + lease note | FY25 print: lease cash outflow (₹70.50 Cr) exceeded CFO (₹27.68 Cr) by ~2.5x, funded through financing (B02-notes.yaml rank 10) — continuing breach is a red flag |
| Consolidated receivables ageing (>1yr buckets) | Collection-quality trend masked by headline growth | Aged buckets should not outgrow revenue growth | AR Note 4.c ageing table | 1-2yr bucket already +259.8% YoY, 2-3yr +1,233% YoY in FY25 (B02-notes.yaml) — any further acceleration is a hard red flag |
| Goodwill as % of net worth, and per-CGU (NestAway/HelloWorld) impairment test outcome | Impairment risk concentrated in two negative-net-worth subsidiaries | No impairment charge, or impairment tests independently verifiable | AR goodwill note (Note 25) | First impairment charge against the ₹174.25 Cr goodwill balance (61% of consolidated equity) (B02-notes.yaml rank 2) |
| CARO qualifications / subsidiary-level default status (Integrow) | Governance/credit-quality signal invisible in headline P&L | Zero unresolved CARO exceptions | Next AR's Auditor's Report Annexure | Integrow default remains uncured or a new subsidiary-level default appears (B02-notes.yaml rank 1) |

### 3C. Industry-specific non-financial KPIs

| KPI | Segment | Where to find it |
|---|---|---|
| Number of houses / signed units / beds under management / occupancy % | Rental | Quarterly investor presentation KPI table (e.g., 5,214 houses, 9,559 signed units, 19,286 beds, 76% occupancy, Q4 FY26, OPERATOR_CONTEXT item 4) |
| Number of properties (HelloWorld co-living spaces) | Rental | Same table (270+ properties, Q3 FY26, OPERATOR_CONTEXT item 1) |
| Leads sold (Aurum Analytica) | Distribution | Quarterly presentation (1,48,392 leads Q4 FY26, +93% YoY, OPERATOR_CONTEXT item 4) |
| Active licenses / accounts (Sell.do) | Distribution | Quarterly presentation (10,378 licenses, +32%; 916 accounts, +38%, Q4 FY26) |
| Active developer clients / mandates (PropTiger) | Distribution | Quarterly presentation (170+ active developer clients, 12 active mandates, Q4 FY26 results press release p.3) |
| SM-REIT scheme count / AUM launched | Capital | Future quarterly presentations — none launched as of Q4 FY26 (B07-emoat catalysts_12m) |
| Ecosystem/cross-sell revenue % (multi-product customers) | Group | Concall Q&A — management states "still in single digit," committed to disclose FY27 (Concall Apr-2026, lines 623-634) |
| Revenue per team member (three flavors: Group, Rental, Distribution) | Group | Quarterly investor presentation KPI table |

### 3D. Unit economics — the physics of the business

Given the multi-segment structure, unit economics differ materially; the single most decision-useful unit is the **NestAway/Rental managed unit** and the **Sell.do license/account**, shown separately.

| Element | Rental (NestAway managed unit) | Distribution (Sell.do license) |
|---|---|---|
| One unit | One rented/managed home or co-living bed | One active CRM license/seat |
| Revenue per unit | Landlord commission (10% recurring) + tenant blended commission (5%) on rent value (Inv. Pres. Q2 FY26 slide 13) | Not disclosed per-seat (license pricing tiers NOT FOUND in documents reviewed) |
| Volume drivers | Number of houses/beds signed, occupancy % (76% Q4 FY26) | New developer onboarding (40+ new developers, 600+ new licenses added Q4 FY26, results press release p.3) |
| Price drivers | Prevailing market rent levels (Aurum takes a % of rent, not a fixed fee) | Multi-product billing adoption (27% developer multi-product billing, per B07-emoat C1 evidence) |
| Cost drivers | Property lease/rent payments (long-term lock-in), on-ground property-management staff | Engineering/support headcount, AI-tooling capex (target -30-50% cost per lead per company's own stated AI targets, OPERATOR_CONTEXT item 5) |
| Incremental margin / operating leverage | Moderate: each incremental filled bed at an existing property is high-incremental-margin (fixed lease cost already committed), but each new property adds a new lease-liability step-cost | High: software has near-zero marginal cost per incremental license once built; this is the segment management is targeting for the AI-driven "revenue per team member" leverage story (Concall Apr-2026, lines 157-159, 794) |

---

## SECTION 4: RISKS, VALUATION APPROACH & MONITORING

### 4A. Business-model-specific risks

| Category | Risk | First financial line item to deteriorate (quarterly monitoring trigger) |
|---|---|---|
| Revenue model | Distribution concentration (~60% of income per operator narrative) decelerating as PropTiger integration "early days" synergies remain unquantified (B07-emoat top_moat_risks) | Distribution segment revenue growth rate (watch for reversion below historical 40%+ trend) |
| Revenue model | Ecosystem/cross-sell revenue thesis stays P&L-immaterial despite being the centerpiece of the AI/platform narrative (management: "still in single digit," Concall Apr-2026 lines 623-626) | Disclosed cross-sell/ecosystem revenue % (management committed to FY27 disclosure) |
| Margin | Reported EBITDA vs. Adjusted EBITDA reconciliation gap widens or the company stops disclosing the reconciliation | Adjusted EBITDA margin vs. reported EBITDA margin spread (Q3 FY26 gap was 30.3% vs. 6.5%) |
| Margin | Rental segment misses its FY27 profitability target (HelloWorld adj-EBITDA breakeven claimed "by Mar" per OPERATOR_CONTEXT item 4) | Rental segment result (currently −₹14.54 Cr FY25) |
| Balance sheet | Lease-liability cash service continues to exceed operating cash flow, funded through financing/equity rather than operations | CFO vs. total lease cash outflow (FY25: ₹27.68 Cr CFO vs. ₹70.50 Cr lease cash service) |
| Balance sheet | Goodwill impairment against NestAway/HelloWorld (both negative, worsening net worth) crystallizes | First impairment charge line in the P&L against the ₹174.25 Cr goodwill balance |
| Balance sheet | Receivables ageing deterioration continues, signaling real collection problems behind headline revenue growth | >1yr receivables ageing buckets (already +327% YoY in FY25) |
| Execution | Two-quarter profitability streak (Q3+Q4 FY26) proves fragile without the one-time ₹17.72 Cr building-sale gain propping up Q4 (B07-emoat top_moat_risks) | PBT/PAT margin ex-one-off other income, next 2 quarters |
| Execution | Governance: rights-issue proceeds parked in debt mutual funds contrary to SEBI ICDR norms (rectified Jan-23-2026) recurs in a different form | Any future CARO qualification or SEBI observation in subsequent filings |
| Structural | SM-REIT (Capital) stays in "wait and watch" for a fourth+ consecutive quarter with no scheme filed, so the regulatory-moat segment never monetizes (B07-emoat top_moat_risks) | Capital segment revenue (currently ₹15.94 Cr FY25, tiny base) and any scheme-launch announcement |
| Structural | Upcoming Jul-16-2026 board-approved equity/QIP fund-raise dilutes shareholders faster than ARR/earnings growth compensates | Shares outstanding / EPS dilution vs. ARR growth rate, next 1-2 quarters |

### 4B. Valuation method applicability table

| Method | Applicable? | Reasoning |
|---|---|---|
| Sum-of-the-parts (SOTP): segment EV/Revenue or EV/EBITDA per SBU | **YES — PRIMARY** | The three segments (Rental, Distribution, Capital) have structurally different economics, margins, and growth rates, and the company itself reports them as distinct SBUs with separate revenue and segment-result lines (AR FY25 Note 23). A single blended multiple would misprice the profitable, high-margin Distribution engine against the still-loss-making, lease-heavy Rental business and the pre-revenue Capital optionality. |
| EV/Revenue (blended or per segment) | **YES — SECONDARY cross-check** | Appropriate given FY26 is only the first (barely) profitable year at the consolidated level — earnings-based multiples are not yet stable enough to anchor on alone; EV/Revenue (per segment, using the FY25 AR anchored split as the base, updated for FY26 ARR growth) cross-checks the SOTP build. Broker precedent: Dolat Capital's own model uses EV/Sales (8.8x/6.3x/4.1x/2.7x across the forecast years) as a primary comp metric (Dolat Capital note, non-anchored, p.2978), which corroborates this being the market's chosen cross-check method for this name, though the broker figures themselves are not to be used as anchored numbers. |
| DCF (segment-level, cash-flow-adjusted for Ind AS 116 lease distortion) | **YES — TERTIARY** | Usable once Adjusted EBITDA/free-cash-flow trends stabilize past 2-3 more quarters; must use the company's Adjusted EBITDA (post-lease-payment) build, not reported EBITDA, given the ~4-5x distortion identified in 3A. Currently only two profitable quarters exist, so near-term DCF inputs carry high estimation risk — hence tertiary, not primary. |
| Trailing P/E or forward P/E on a single consolidated EPS number | **NOT APPLICABLE currently** | FY26 EPS is barely positive and Q4 FY26 profitability included a one-time ₹17.72 Cr building-sale gain; a single blended P/E would badly misprice a three-segment business with a formerly loss-making Rental segment and an unmonetized Capital segment. Revisit once 4-6 consecutive clean quarters of segment-level profitability exist. |
| Asset-based / book value (P/B) | **NOT APPLICABLE** | Goodwill is 61% of consolidated net worth (B02-notes.yaml rank 2) and carries real impairment risk against two negative-net-worth subsidiaries; book value is not a reliable value anchor here. |
| Dividend discount model | **NOT APPLICABLE** | Company pays no dividend; capital is being reinvested (and now raised via equity) into growth/AI capex. |
| **PRIMARY** | SOTP (segment EV/Revenue and EV/EBITDA blend, using company-disclosed segment splits and Adjusted EBITDA) | Best matches the disclosed three-SBU structure and the divergent economics/lifecycle stage of each segment. |
| **SECONDARY** | Consolidated EV/Revenue (or EV/ARR) cross-check | Anchors the SOTP build against the market's evident preference for a revenue multiple on a still-young-profitability platform story; also the metric the broker community (Dolat, non-anchored) already uses. |
| **TERTIARY** | Segment-level DCF using Adjusted EBITDA/FCF, once 4+ clean quarters exist | Becomes primary once profitability trend is established past the one-time-gain-affected Q4 FY26 print. |
| Cycle stage that matters for valuation | Early-profitability inflection, post-consolidation, pre-scale on the newest segment (Capital) — this is a transition/turnaround valuation setup (consistent with B07-emoat's "TURNAROUND" combined_assessment), not a steady-state mature-cash-flow valuation. |

### 4C. Quarterly monitoring checklist (10-15 items)

| # | Item | Good looks like | Trouble looks like |
|---|---|---|---|
| 1 | ARR trajectory | Sequential growth toward ₹1,000 Cr, 3-yr target | Deceleration or flat ARR |
| 2 | Segment revenue split (Rental/Distribution/Capital) | Distribution sustaining growth, Rental narrowing losses, Capital showing early scheme activity | Distribution deceleration with no offsetting Rental/Capital pickup |
| 3 | Adjusted EBITDA margin (company-defined) | Continued sequential improvement (5.9% FY26 → higher) | Reversal quarter-on-quarter |
| 4 | Reported vs. Adjusted EBITDA reconciliation | Disclosed each quarter, gap explainable by lease accounting | Reconciliation disclosure dropped or gap widens unexplained |
| 5 | PBT/PAT margin ex-one-offs | Sustained positive | Reversion to negative excluding one-time items |
| 6 | Rental segment result | Narrowing loss toward FY27 breakeven target | Loss widening or breakeven target pushed out again |
| 7 | Lease cash outflow vs. CFO | CFO catching up to/exceeding lease cash service | Gap persists or widens, continued financing-funded lease service |
| 8 | Receivables ageing (>1yr buckets) | Stabilizing or shrinking | Continued disproportionate growth vs. revenue growth |
| 9 | Goodwill impairment test outcome (NestAway/HelloWorld) | No impairment, or modest/well-flagged impairment | Impairment charge, especially unflagged in advance |
| 10 | Cross-sell/ecosystem revenue % disclosure | First formal disclosure delivered as management committed (FY27) | Promised disclosure slips again |
| 11 | SM-REIT scheme launch | First scheme filed/launched | Continued "wait and watch" with no scheme |
| 12 | Revenue per team member (Group, Rental, Distribution) | Continued sequential improvement | Flat/declining despite AI-spend narrative |
| 13 | Integrow CARO default cure status | Cured, quantified, and disclosed | Remains unresolved/unquantified |
| 14 | Fund-raise (Jul-16-2026 board meeting) outcome and use of proceeds | Growth capital at reasonable dilution, clearly earmarked (AI capex per company narrative) | Large dilution with vague use-of-proceeds language |
| 15 | Debt-free status maintained | Confirmed post building-sale completion, no new leverage build-up | Re-leveraging via new LRD/term debt |

### 4D. Highest-value questions for management

| # | Question | Answer that reassures | Answer that worries |
|---|---|---|---|
| 1 | What is the FY26 (and quarterly FY27) segment-level revenue and profit split under Ind AS 108, comparable to the FY25 AR Note 23 table? | Clean, comparable segment table showing Distribution sustaining growth and Rental narrowing losses | Segment disclosure discontinued, aggregated, or restated again without explanation |
| 2 | What specific, monetized product or signed contract backs the "Unified Brain"/AI-native narrative today, beyond calling bots and lead scoring? | A named monetized AI product with disclosed revenue or cost-saving impact | Continued narrative without a disclosed model-performance metric or monetized deliverable (per B07-emoat, this is currently the weakest-evidenced category) |
| 3 | What is the cure status, amount, and counterparty of the Integrow Asset Management CARO ix(a) loan/interest default? | Fully cured, quantified, no cross-default risk to Group facilities | Remains open, unquantified, or reveals cross-default exposure |
| 4 | What is the use-of-proceeds plan for the Jul-16-2026 board-approved equity/QIP fund-raise, and at what expected dilution? | Specific AI/growth capex plan with modest, well-telegraphed dilution | Vague "general corporate purposes" language with large potential dilution |
| 5 | When will the first SM-REIT (AMSA) scheme actually launch, and at what target AUM? | A near-term (within FY27) launch date with a credible AUM pipeline | Continued "wait and watch" indefinitely |
| 6 | What is the ecosystem/cross-sell revenue % today, and what is the credible path to double digits? | A disclosed, credible number and trajectory (management has committed to this for FY27) | Continued deferral of the disclosure management itself promised |
| 7 | Is the two-quarter profitability streak sustainable excluding the Q4 FY26 one-time ₹17.72 Cr building-sale gain? | Yes, with a clean quarterly PBT bridge excluding one-offs | Profitability was substantially dependent on the one-time gain |

---

## SECTION 5: ONE-PAGE BUSINESS MODEL SUMMARY CARD

```
┌─────────────────────────────────────────────────────────────────────┐
│ AURUM PROPTECH LTD (AURUM) — BUSINESS MODEL SUMMARY CARD             │
├─────────────────────────────────────────────────────────────────────┤
│ Business type:        Hybrid platform conglomerate (3 SBUs)          │
│ One-liner:            Rents managed homes (Rental), sells data/CRM/  │
│                        brokerage to developers (Distribution, the    │
│                        profit engine), and is building a SEBI-       │
│                        licensed real-estate investment product       │
│                        (Capital)                                     │
├─────────────────────────────────────────────────────────────────────┤
│ Revenue mix (FY25, AR-anchored): Rental 63.9% | Distribution 30.1% | │
│   Capital 6.0%  (AR FY25 p.51). FY26 operator narrative: Distribution│
│   ~60% of income post-PropTiger (secondary, not AR-anchored)         │
│ Asset intensity:      Medium (lease-liability heavy, not PP&E heavy) │
│ WC intensity:         Medium, deteriorating trend flagged (B02)      │
│ Pricing power:        Weak-to-moderate, segment-dependent            │
│ Cyclicality:          Secular-growth demand backdrop, cyclical       │
│                        transaction/lead-volume exposure (housing     │
│                        sales cycle) in Distribution's PropTiger/     │
│                        Analytica legs                                │
├─────────────────────────────────────────────────────────────────────┤
│ Strongest moat:       SEBI SM-REIT license (Capital) — regulatory,   │
│                        currently unmonetized                         │
│ Weakest claimed moat: "Unified Brain"/AI data moat — central to the  │
│                        company narrative, weakest-evidenced per      │
│                        B07-emoat scan                                │
├─────────────────────────────────────────────────────────────────────┤
│ Must-track top 5:     1. ARR trajectory toward ₹1,000 Cr             │
│                        2. Adjusted EBITDA margin (not reported EBITDA)│
│                        3. Segment-level revenue/profit split         │
│                        4. Lease cash outflow vs. CFO coverage        │
│                        5. Cross-sell/ecosystem revenue % disclosure  │
├─────────────────────────────────────────────────────────────────────┤
│ Primary valuation:    Sum-of-the-parts (segment EV/Revenue &         │
│                        EV/EBITDA), given divergent segment economics │
│ Secondary:            Consolidated EV/Revenue (EV/ARR) cross-check   │
│ Tertiary:             Segment-level DCF (Adjusted EBITDA/FCF basis), │
│                        once 4+ clean profitable quarters exist       │
│ Not applicable:       Trailing/forward P/E (single line), P/B,       │
│                        dividend discount model                       │
├─────────────────────────────────────────────────────────────────────┤
│ One-line verdict:     A three-segment turnaround story where the     │
│                        profitable engine (Distribution) is real but  │
│                        the loudest narrative (AI moat) is the        │
│                        thinnest-evidenced part of the story.         │
└─────────────────────────────────────────────────────────────────────┘
```

---

```yaml
stage: B04-bizmodel
company: "AURUM"
run_date: "2026-07-14"
model: claude-sonnet-5
status: complete
input_gaps:
  - "No standalone Q4/FY26 investor presentation text was available in this run (only Q2 FY26 and Q3 FY26 presentations, plus the Q4 FY26 results press release which lacks a segment financial table); FY26 segment-level revenue/profit split therefore relies on OPERATOR_CONTEXT.md secondary figures (Distribution ~60% of income, Distribution FY26 segment profit Rs32.3 Cr), not an AR- or results-PDF-anchored Ind AS 108 segment note."
  - "Sell.do per-license/per-seat pricing tiers not disclosed in any document reviewed; unit economics for Distribution stream could only be characterized qualitatively."
  - "Contract liability / unearned revenue (SaaS deferred-revenue) balance not separately sized in the AR notes reviewed, so no verification of negative-working-capital SaaS dynamics was possible for Sell.do specifically."
  - "SM-REIT/AMSA investment-management fee structure (beyond the disclosed 5%/15% investment-by-IM feature) not found in documents reviewed."
  - "Competitive positioning names (NoBroker, Housing.com, Stanza Living, ZoloStays, Salesforce, Zoho, 99acres) are sourced only from the Dolat Capital broker note, explicitly non-anchored per operator instruction; no AR or investor-presentation source independently names competitors."
flags:
  - type: FLAG-METRIC-DISTORTION
    reason: "Reported EBITDA margin (30.3% of Total Income, Q3 FY26) is not comparable to the company's own Adjusted EBITDA margin (6.5%) due to Ind AS 116 lease accounting; any downstream stage using 'EBITDA' without specifying which figure risks a ~4-5x overstatement of cash profitability."
  - type: FLAG-NARRATIVE-VS-EVIDENCE
    reason: "Central AI/'Unified Brain' narrative used to justify forward growth and margin expansion is the weakest-evidenced category in the parallel B07-emoat scan (D1, A2 both Weak); Section 4A and 4D carry this forward as the top monitorable and top management question."
  - type: FLAG-ONE-TIME-ITEM
    reason: "Q4 FY26 profitability (second consecutive profitable quarter) included a Rs17.72 Cr one-time building-sale gain in other income; the underlying two-quarter operating profitability trend should be assessed ex-this-item before it is treated as a clean base for any earnings-based valuation approach."
business_type: "hybrid"
revenue_streams:
  - {name: "Rental (NestAway managed rentals + HelloWorld co-living)", type: "operating-lease / marketplace commission hybrid", pct_of_revenue: 63.9, predictability: "M"}
  - {name: "Distribution (Aurum Analytica leads + Sell.do SaaS CRM + PropTiger brokerage)", type: "blended SaaS license + pay-per-lead + transaction commission", pct_of_revenue: 30.1, predictability: "M"}
  - {name: "Capital (SM-REIT/AMSA + legacy Integrow/YieldWiseX/SPVs)", type: "asset management fee (nascent)", pct_of_revenue: 6.0, predictability: "L"}
asset_intensity: "medium"
wc_intensity: "medium"
pricing_power: "moderate"
cyclicality: "cyclical"
moats_present:
  - {moat: "Regulatory/licensing (SEBI SM-REIT registration, AMSA)", durability: "durable if scheme launches; currently unmonetized"}
  - {moat: "Switching costs (Sell.do CRM embedding)", durability: "weak-to-moderate, unproven at scale"}
  - {moat: "Ecosystem/cross-sell lock-in", durability: "weak, quantified as P&L-immaterial by management ('still in single digit')"}
  - {moat: "Execution/management track record", durability: "improving but only two profitable quarters of evidence"}
  - {moat: "Proprietary data/IP ('Unified Brain')", durability: "weak, central narrative claim not yet backed by disclosed model-performance or IP filing"}
valuation_methods:
  primary: {method: "Sum-of-the-parts (segment EV/Revenue and EV/EBITDA per SBU)", why: "Three disclosed SBUs (Rental, Distribution, Capital) have structurally divergent economics, margins, and lifecycle stages; a single blended multiple would misprice the profitable Distribution engine against the still-loss-making Rental segment and pre-revenue Capital optionality"}
  secondary: {method: "Consolidated EV/Revenue (EV/ARR) cross-check", why: "FY26 is only the first barely-profitable year, so earnings multiples are not yet stable; EV/Revenue anchors against the market's evident preference (also used by Dolat Capital's broker model, non-anchored) for valuing this still-young-profitability platform story"}
  tertiary: {method: "Segment-level DCF using company Adjusted EBITDA/FCF basis", why: "Becomes usable once 4+ consecutive clean profitable quarters exist past the Q4 FY26 one-time-gain-affected print; must use Adjusted EBITDA (post-lease-payment), not reported EBITDA, given the Ind AS 116 distortion identified in Section 3A"}
  not_applicable: ["Trailing/forward P/E on single consolidated EPS (FY26 barely positive, Q4 inflated by one-time gain)", "Price-to-book (goodwill is 61% of consolidated net worth with real impairment risk)", "Dividend discount model (no dividend, capital being reinvested/raised)"]
irrelevant_ratios:
  - {ratio: "Reported (unadjusted) EBITDA margin", why: "Ind AS 116 lease accounting inflates it roughly 4-5x vs. the company's own Adjusted EBITDA (30.3% vs 6.5% of income, Q3 FY26)"}
  - {ratio: "Trailing/forward P/E on a single consolidated EPS", why: "FY26 is the first barely profitable year and Q4 FY26 profit included a one-time Rs17.72 Cr building-sale gain"}
  - {ratio: "Debt/Equity or interest coverage using reported borrowings only", why: "Consolidated lease liabilities (Rs192.33 Cr) are 2.4x reported borrowings (Rs81.01 Cr); real fixed-obligation leverage is understated"}
  - {ratio: "Standalone current ratio", why: "The 8.70x standalone print is an intercompany-loan reclassification artifact per management, not real liquidity improvement"}
  - {ratio: "Single blended gross margin %", why: "Masks which of three structurally different segments (SaaS-like, commission-based, lease-heavy) is actually driving profitability"}
  - {ratio: "Inventory turnover / days inventory", why: "No physical inventory in this leads/software/managed-rental services business model"}
must_track_metrics:
  - {metric: "ARR", healthy: "sequential growth toward the stated Rs1,000 Cr 3-year target", red_flag: "deceleration or flat ARR vs. prior-quarter guidance"}
  - {metric: "Adjusted EBITDA margin (company-defined, post-lease-payment)", healthy: "continued sequential improvement from FY26's 5.9%", red_flag: "quarter-on-quarter reversal"}
  - {metric: "Segment revenue/profit split (Rental/Distribution/Capital)", healthy: "Distribution sustaining growth, Rental narrowing losses toward FY27 breakeven, Capital showing scheme activity", red_flag: "Distribution deceleration with no offsetting pickup elsewhere"}
  - {metric: "Lease cash outflow vs. operating cash flow (CFO) coverage", healthy: "CFO catching up to/exceeding lease cash service", red_flag: "gap persists or widens, continued financing-funded lease service (FY25: Rs27.68 Cr CFO vs Rs70.50 Cr lease cash service)"}
  - {metric: "Cross-sell / ecosystem revenue % disclosure", healthy: "management delivers the FY27 disclosure it committed to, showing a credible path to double digits", red_flag: "promised disclosure slips again, stays 'single digit' with no trajectory"}
unit_economics:
  unit: "One NestAway managed rental unit (Rental) and one Sell.do active CRM license (Distribution) — the two clearest disclosed unit economics"
  revenue_per_unit: "NestAway: 10% recurring commission from landlord + ~5% blended commission from tenant on rent value (Inv. Pres. Q2 FY26 slide 13); Sell.do: per-seat/account SaaS license fee, exact pricing tiers NOT FOUND"
  margin_per_unit: "NestAway: property lease/rent payments and on-ground management cost dominate; Sell.do: near-zero marginal cost per incremental license once built, high incremental margin"
  key_lever: "Revenue per team member (Group, Rental, Distribution) is management's own stated guiding metric for the AI-driven operating-leverage thesis"
first_deterioration_signals:
  - {risk: "Distribution concentration decelerating as PropTiger synergies remain unquantified", first_signal: "Distribution segment revenue growth rate falling below the historical 40%+ trend"}
  - {risk: "Ecosystem/cross-sell revenue thesis stays P&L-immaterial", first_signal: "disclosed cross-sell/ecosystem revenue % (management committed to FY27 disclosure) not delivered or stays single-digit"}
  - {risk: "Reported vs Adjusted EBITDA reconciliation gap widens or disclosure stops", first_signal: "Adjusted EBITDA margin vs reported EBITDA margin spread widening beyond the Q3 FY26 baseline (30.3% vs 6.5%)"}
  - {risk: "Rental segment misses FY27 profitability target", first_signal: "Rental segment result (FY25 baseline -Rs14.54 Cr) not narrowing quarter over quarter"}
  - {risk: "Lease-liability cash service continues to exceed operating cash flow", first_signal: "CFO vs total lease cash outflow gap (FY25: Rs27.68 Cr CFO vs Rs70.50 Cr lease cash service)"}
  - {risk: "Goodwill impairment against NestAway/HelloWorld crystallizes", first_signal: "any impairment charge line item in the P&L against the Rs174.25 Cr goodwill balance"}
  - {risk: "Receivables ageing deterioration continues", first_signal: ">1yr receivables ageing buckets (already +327% YoY in FY25) growing further"}
  - {risk: "Two-quarter profitability streak proves fragile without the one-time building-sale gain", first_signal: "PBT/PAT margin ex-one-off other income reverting negative in the next 1-2 quarters"}
  - {risk: "SM-REIT (Capital) stays unmonetized indefinitely", first_signal: "a fourth+ consecutive quarter passing with no scheme filed/launched"}
  - {risk: "Jul-2026 equity/QIP fund-raise dilutes faster than growth compensates", first_signal: "shares outstanding / EPS dilution outpacing ARR growth rate"}
mgmt_questions:
  - "What is the FY26 (and quarterly FY27) segment-level revenue and profit split under Ind AS 108, comparable to the FY25 AR Note 23 table?"
  - "What specific, monetized product or signed contract backs the 'Unified Brain'/AI-native narrative today, beyond calling bots and lead scoring?"
  - "What is the cure status, amount, and counterparty of the Integrow Asset Management CARO ix(a) loan/interest default?"
  - "What is the use-of-proceeds plan for the Jul-16-2026 board-approved equity/QIP fund-raise, and at what expected dilution?"
  - "When will the first SM-REIT (AMSA) scheme actually launch, and at what target AUM?"
  - "What is the ecosystem/cross-sell revenue % today, and what is the credible path to double digits?"
  - "Is the two-quarter profitability streak sustainable excluding the Q4 FY26 one-time Rs17.72 Cr building-sale gain?"
one_line_verdict: "A three-segment turnaround where the profitable engine (Distribution) is real but the loudest narrative (AI moat) is the thinnest-evidenced part of the story."
```
