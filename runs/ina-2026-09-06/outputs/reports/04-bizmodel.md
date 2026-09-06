# Stage 4: Business Model Decoder — Insolation Energy Ltd (INA)

Run date: 2026-09-06 | Model: Sonnet 5 | Stage: B04-bizmodel

Primary source: FY2026 Annual Report (page-marked extraction). Secondary
source: Investor Presentation, August 2026 (Q1 FY27 results, unaudited),
32 pages, page-marked.

---

## SECTION 1: THE BUSINESS MODEL IN PLAIN ENGLISH

### 1A. One-line description

INA makes and sells solar panels (modules), and it is racing to also make
the ingredients that go into those panels (cells, aluminium frames, and
eventually wafers and ingots), while a family of ~76 subsidiary companies
builds power plants that use those panels and sells the electricity.
Nearly all of the money today, though, still comes from selling panels
(AR p.130, Note 25; AR p.144-145, Note 46 "Manufacturing & Trading of
Solar Photovoltaic Modules").

### 1B. The money flow chain, for EACH revenue stream

The accounts split "Sale of Products" into three lines plus a small
"Other Operational Revenue" bucket (AR p.130, Note 25, consolidated; AR
p.172, Note 24, standalone). That split is the real revenue-stream map,
because the AR does not give a narrative revenue split anywhere else.

| Stream | Money flow chain |
|---|---|
| Module manufacturing (own factories) | [Bought-in solar cells, glass, EVA, aluminium, junction boxes] → [assembled into finished PV modules at INA-1/2/3, Jaipur] → [sold as "Finished Goods"] → [EPC contractors, developers, government tenders, channel partners] → [advance + credit terms, per PO] |
| Trading (bought-and-resold goods) | [Modules/cells bought from other manufacturers] → [re-badged/re-sold, little to no processing] → [delivered as "Trading Sales"] → [same customer base as above, used to fill orders beyond own capacity] → [credit terms] |
| Sale of Electricity (IPP) | [Capital deployed into ~76 step-down SPVs building solar power parks] → [electricity generated once commissioned] → [sold under PPA] → [state discoms / commercial & industrial offtakers] → [monthly power-sale billing] |
| Other Operational Revenue (installation/job work/scrap) | [Installation labour, contract job-work on customer-owned material, scrap material] → [service or ancillary product delivered] → [EPC/rooftop customers, job-work counterparties] → [billed alongside or separate from module sale] |

Two structural facts sit under this table and change how you should read
it:
- The single Ind AS 108 segment note says the whole group "operates only
  in one Business Segment i.e. 'Manufacturing & Trading of Solar
  Photovoltaic Modules'" (AR p.144-145, Note 46, and AR p.185, Note 45
  standalone equivalent). The company's own auditors do not yet see EPC,
  IPP, O&M or BESS as big enough, or separately managed enough, to be a
  reportable segment.
- EPC execution itself sits in a THIRD entity, Insolation Green Infra
  Private Limited, distinct from the manufacturing subsidiary Insolation
  Green Energy Private Limited (AR p.49-50, MD&A: "The Company's
  subsidiary, Insolation Green Infra Private Limited, focuses on the
  execution of solar EPC projects including KUSUM Components A and C,
  solar parks, O&M services, and rooftop installations"). So this is not
  two entities, it is at least three, plus roughly 76 project SPVs below
  them (prior-stage finding).

### 1C. Revenue model classification table

| Stream | Type | Description | % of FY26 consol. revenue (anchored) | Predictability |
|---|---|---|---|---|
| Sale of Products — Finished Goods (own-manufactured modules) | Manufacturing, point-in-time goods sale | Modules made in-house sold to EPCs, developers, government tenders, channel partners | 81.9% (Rs 1,757.22cr / Rs 2,146.02cr; AR p.130, Note 25) | Medium — order-book driven, but ASP is commodity-linked |
| Sale of Products — Trading Sales (bought-and-resold) | Trading, point-in-time goods sale | Third-party modules/cells bought and resold, thinner margin | 17.0% (Rs 364.91cr / Rs 2,146.02cr; AR p.130, Note 25) | Low — fills capacity gaps opportunistically |
| Sale of Electricity (IPP) | Asset-owner, over-time power sale | Electricity sold from commissioned solar parks held in step-down SPVs | 0.2% (Rs 4.22cr / Rs 2,146.02cr; AR p.130, Note 25) | High once commissioned (PPA-backed), but currently near-zero base |
| Other Operational Revenue (installation, job work, scrap, freight recovery) | Services + ancillary | Installation & commissioning (Rs 1.00cr), Job Work Income (Rs 8.79cr), Scrap Sales (Rs 1.02cr), Freight on Sales (Rs 0.47cr) | 0.5% combined (AR p.130, Note 25) | Low, small and lumpy |
| Explicit "EPC revenue" line | NOT FOUND | No revenue line named "EPC" or "O&M" exists anywhere in the Ind AS 115 disaggregation (AR p.149-150, Note 51 consol; AR p.187, Note 49 standalone) | NOT FOUND, check investor presentation or concall | NOT FOUND |

Cross-check: the group-wide Ind AS 115 disclosure shows "Goods
transferred at a point in time" = Rs 2,153.74cr and "Services transferred
at a point in time" = Rs 9.79cr, i.e. 99.55% goods vs 0.45% services (AR
p.149-150, Note 51). That is the accounting-standard confirmation of the
same point: whatever the presentation calls "EPC" and "O&M" today, it is
not yet showing up as a distinguishable service-revenue line. It is
either bundled inside "goods" (equipment-heavy EPC billed as a goods
sale) or genuinely tiny in FY26.

### 1D. Simplified business model canvas

| Element | INA today |
|---|---|
| What they sell | Solar PV modules (own-made and bought-in), a sliver of power (IPP), a sliver of EPC/installation services |
| Who buys | EPC contractors, project developers, government tenders/PSUs (NTPC, SECI, SJVN — AR p.16 Inv. Pres.), 1000+ channel partners, one large new customer (Solarworld Energy Solutions Ltd, Rs 265.19cr, 12.4% of FY26 consol revenue — AR p.144-145, Note 46(ii)), 40,000+ retail/rooftop customers |
| Why them | ALMM-listed and BIS/IEC/UL/TÜV/CE certified (AR p.49, MD&A; Inv. Pres. p.17), 5.5 GW installed capacity (top-10 claim, Inv. Pres. p.15), pan-India distribution reach |
| How delivered | Factory dispatch to EPC/developer site or channel partner, rooftop dealer network for retail |
| Cost structure dominance | Materials. Consolidated Cost of Raw Material Consumed Rs 1,662.13cr + Purchase of Stock-in-Trade Rs 272.06cr = Rs 1,934.19cr against Rs 2,146.02cr revenue, roughly 90% of revenue (AR p.131, Note 27/28). Employee cost is only Rs 38.91cr, under 2% of revenue (AR p.131-132, Note 30) |
| Scarce resource | ALMM listing and DCR/NDCR-classified product lines (Inv. Pres. p.19, AR p.43); NOT a scarce input position on cells, wafers, polysilicon — those are still bought in, per the raw-material-risk note (AR p.66-67: "Solar manufacturing is dependent on critical inputs such as solar cells, wafers, aluminium frames and other components") |
| Pricing power source or absence | Weak-to-moderate. Module ASPs are globally commodity-linked; INA's only genuine differentiators today are ALMM/BIS compliance (a gate, not a premium) and DCR/NDCR classification for government-scheme eligibility. Cell backward integration (the thing that could add real pricing power) is not yet commissioned (target COD Q4 FY27 / Dec 2026 — AR p.21-24; Inv. Pres. p.13, p.26) |
| Asset intensity | Rising fast. Consolidated capex Rs 448.05cr vs standalone Rs 28.43cr in FY26 (prior-stage finding); PPE + CWIP rose from Rs 123cr to Rs 547cr in the group in one year (Inv. Pres. p.31) |
| WC intensity | High and getting worse. Inventory 4.9x, finished goods ~14.7x, trade receivables 2.55x (Rs110cr to Rs281cr, Inv. Pres. p.31) against 60.9% revenue growth |
| Regulatory moat or burden | Both. ALMM (moat: keeps non-listed importers out of government/PSU tenders) and PLI-scheme eligibility (burden and opportunity: capital-intensive to qualify, no evidence yet that INA itself, as opposed to the industry generally, has been allocated a PLI tranche — NOT FOUND, check investor presentation or concall) |

### 1E. The chai-stall-uncle version

Think of INA like a tea-stall owner who started by just brewing and
selling chai (making and selling solar panels). Business boomed, so the
owner is now also buying tea leaves in bulk to resell to other stalls
(trading), building a sugar factory next door so he does not have to buy
sugar from anyone (the cell plant), and opening three new tea stalls of
his own down the road that he also owns (the IPP power plants). The
sugar factory is not running yet. The new stalls are still under
construction. So today, more than 98 rupees of every 100 the group earns
still comes from the original chai-brewing-and-selling business (AR
p.130, Note 25), even though the annual report and investor slides talk
mostly about the sugar factory and the new stalls.

### Section 1 summary table

| Business type | Revenue nature | Asset intensity | WC intensity | Pricing power |
|---|---|---|---|---|
| Manufacturing + trading (hybrid, transitioning toward integrated + IPP) | Point-in-time goods sale, 99.6% (AR p.149-150) | Medium today, rising to heavy (capex quadrupled group PPE+CWIP in one year) | High, worsening (inventory +4.9x, receivables +2.55x vs revenue +60.9%) | Weak-to-moderate; commodity module economics with a regulatory (ALMM) gate, not yet a cost or technology edge |

---

## SECTION 2: INDUSTRY DYNAMICS & COMPETITIVE POSITION

### 2A. Five forces, plainly

| Force | Reading | Direction |
|---|---|---|
| Competition count | India's solar module manufacturing capacity grew from 2.3 GW (2014) to about 172 GW (March 2026) (AR p.51-52, MD&A). That is a huge, fast build-out of rival capacity nationally. Named listed peers not identified anywhere in the AR or presentation — no competitor is named by name anywhere in either document | Hurts |
| Entry barriers | Capital cost is real (Rs 650-700cr per GW for wafer/ingot lines alone, per Inv. Pres. p.26) but capacity has grown roughly 75x nationally in a decade, so the barrier has not been high enough to stop a supply build-out | Hurts, mildly |
| Supplier power | Cells, wafers and aluminium frames are still bought-in inputs, not made in-house (AR p.66-67, raw-material risk note; product-line table AR p.43 shows cells/frames listed "Upcoming FY27"). Raw material cost is ~78% of revenue (AR p.131, Note 27) | Hurts |
| Customer power / concentration | One new customer, Solarworld Energy Solutions Ltd, is already 12.4% of consolidated revenue with nil prior-year base (AR p.144-145, Note 46(ii)). Recently announced single orders are large and lumpy: NTPC Rs 558cr, MEIL/L&T combined Rs 362cr, RREC Rs 340cr, AP IPP+KUSUM Rs 516cr (Inv. Pres. p.25) | Hurts |
| Substitutes | Solar itself is the substitute displacing thermal power, a secular tailwind (AI/data-centre power demand, PM Surya Ghar, Green Open Access, RPO+BESS, PM-KUSUM — all cited Inv. Pres. p.23). Technology substitution risk within solar (perovskite, other next-gen cell tech eventually displacing TOPCon) is a longer-dated risk, not currently a threat | Helps (macro demand); neutral-to-watch (technology risk) |

### 2B. Competitive positioning map vs named competitors

No competitor is named anywhere in the AR or the investor presentation.
The presentation cites third-party rankings (No.1 in SINOVOLTAICS
Financial Stability Ranking for listed solar manufacturers, four
consecutive times; Top-10 Solar Panel Manufacturer per Industry Outlook
2024; Forbes India "Best Under a Billion" 2024 — Inv. Pres. p.28) but
gives no named head-to-head comparison on capacity, cost, or margin.
Positioning vs peers on any quantified axis: NOT FOUND, check investor
presentation or concall.

### 2C. Moat assessment table (eight standard moat types)

| Moat type | Evidence | Durability |
|---|---|---|
| Brand | Sponsorship of Lucknow Super Giants IPL team as "official solar partner" (AR p.49); "40,000+ happy customers", "1000+ channel partners" (Inv. Pres. p.15) | Low-medium. Consumer brand recall in a project-driven B2B-heavy business has limited pricing translation |
| Switching costs | None identified. Modules are broadly interchangeable across ALMM-listed suppliers for a given spec | None found |
| Network effects | None identified — not a platform business | None found |
| Cost advantage | Not yet. Backward integration into cells (the source of a genuine cost edge) is still under construction, COD Q4 FY27 (AR p.21-24) | Not yet earned |
| Scale | 5.5 GW installed module capacity, described as "among India's leading PV manufacturers" (Inv. Pres. p.10) | Medium — real but matched by an industry that scaled 75x in a decade |
| Regulatory / licence | ALMM listing and BIS/IEC/UL/TÜV/CE certification (AR p.49; Inv. Pres. p.17) gate access to government and PSU tenders (NTPC, SECI, SJVN, PM-KUSUM) | Medium — a real gate, but one shared with every other ALMM-listed manufacturer, so it protects against imports more than against domestic rivals |
| Distribution | Pan-India footprint, 1000+ channel partners, dealer network for PM Surya Ghar rooftop (Inv. Pres. p.16, p.19) | Medium |
| Patents / IP | None disclosed | None found |

### 2D. Industry lifecycle stage and INA's position

Indian solar module manufacturing is in a capacity-scaling, margin-reset
phase: the presentation's own investment thesis slide describes "TODAY:
Industry Margin Reset... Pricing pressure, Margin contraction" as the
current phase, with the thesis that "TOMORROW: Structural Value Creation"
comes once players integrate backward into cells (Inv. Pres. p.22). INA
is mid-transition inside that phase: manufacturing capacity is built out
(5.5 GW), but the backward-integration step that the industry's own
narrative says creates the value (cells, frames, eventually wafers/
ingots) is not yet commissioned. This matches the CLAUDE.md Quality
Ladder framing: INA sits between R1 (commodity price-taker) and R2
(cost-advantaged converter), having built the capacity for R2 but not yet
proven the cost or margin outcome from it.

### 2E. Key industry drivers, direction and impact

| Driver | Direction | Impact on INA |
|---|---|---|
| ALMM-II cell mandate and ALMM-III wafer mandate (2028) | Structural tailwind for domestic, backward-integrated manufacturers | Positive if INA's cell/wafer plans land on schedule; a risk if they slip past when mandates bite |
| PM-KUSUM (34.8 GW target), PM Surya Ghar (1 crore rooftops), Green Open Access threshold cut to 100kW, RPO+BESS demand (all Inv. Pres. p.23) | Demand-side tailwind | Positive — broad, policy-backed demand across utility, rooftop and C&I |
| National module capacity growth 2.3 GW to ~172 GW in a decade (AR p.51-52) | Oversupply / margin-reset risk | Negative — the same policy push that creates demand has also created a lot of new supply |
| Global cell/wafer/polysilicon price and China import dependence (AR p.66-67, raw material risk note) | Input cost volatility | Negative until backward integration is commissioned |

---

## SECTION 3: FINANCIAL METRICS THAT MATTER FOR THIS BUSINESS MODEL

### 3A. Ignore-these-track-these table

| Ratio commonly tracked | Why it MISLEADS here |
|---|---|
| Standalone-only revenue growth or P/E | Standalone revenue FELL 13.3% (Rs113.02cr to Rs98.03cr) in FY26 while consolidated revenue grew 60.9% (prior-stage finding, cross-checked at AR p.185/p.172). A reader looking only at the listed entity's own P&L would conclude the business is shrinking when the group is not |
| Blended (consolidated) ROCE / ROE | Blends a mature, thin-margin trading stream, a growing but still-commodity manufacturing stream, and a pre-revenue IPP asset base that is almost pure capital with almost no return yet (Sale of Electricity is 0.2% of revenue against Rs 448.05cr of group capex) |
| Blended cash conversion (OCF/EBITDA) | FY26 consolidated OCF is minus Rs 73.13cr against PAT of roughly Rs 200cr (prior-stage finding). Part of that gap is genuine receivable-quality risk (39.5% of receivables aged beyond 6 months, all at the subsidiary — prior-stage finding) and part is normal IPP/EPC working-capital build. The blended ratio cannot tell you which |
| Blended inventory turnover / receivable days | Mixes fast-moving trading inventory, slower manufacturing WIP, and long-cycle EPC/IPP project inventory. Inventory grew 4.9x and finished goods ~14.7x against 60.9% revenue growth — a single turnover ratio hides which piece is actually the problem |
| Blended fixed-asset turnover | Mixes IPP assets (capital-heavy, long-gestation, revenue-light until commissioned) with manufacturing assets (revenue-heavy). A single ratio will look artificially weak as IPP capex lands ahead of IPP revenue, even if manufacturing asset efficiency is fine |
| Any implied "segment margin" comparison | There is no reportable segment. The Ind AS 108 note explicitly states one Business Segment, "Manufacturing & Trading of Solar Photovoltaic Modules" (AR p.144-145, p.185). Nothing published lets you compute a genuine EPC, IPP, or O&M margin |
| Parent standalone corporate-guarantee coverage taken in isolation | The parent guarantees Rs 1,654.01cr of subsidiary debt against its own Rs 544.04cr total assets (3.0x, prior-stage finding, anchored at AR p.137, Note 42), including a reverse guarantee where the subsidiary guarantees a parent AU Bank facility (AR p.137, Note 42: "Corporate Guarantee given by Insolation Green Energy Private Limited in favour of AU Bank Limited... availed by Insolation Energy Limited"). Reading either entity's balance sheet alone hides this circular exposure |

### 3B. Must-track metrics

**Growth**

| Metric | What it tells you | Healthy range | Where to find it | Red flag threshold |
|---|---|---|---|---|
| Consolidated revenue growth vs standalone revenue growth | Whether the group and the listed entity are moving in the same direction | Should not structurally diverge for long | AR Note 46(iii)/Note 25 (consol), Note 45(iii)/Note 24 (standalone) | Standalone declining while consol grows, sustained beyond one year |
| Order book conversion | 2.1 GW+ order book (Inv. Pres. p.10) turning into billed revenue | Order book should shrink as revenue books, refilled by new wins | Investor presentation quarterly updates | Order book flat or growing while revenue growth stalls (unexecuted backlog) |
| Sale of Electricity (IPP revenue) growth | The real signal of whether the ~400MW+ IPP pipeline is commissioning and monetizing, off a Rs 4.22cr FY26 base | Should scale toward a run-rate consistent with commissioned MW x plant load factor x tariff | AR Note 25 (consol), line item "Sale of Electricity" | Stays near-zero for multiple quarters after stated COD dates |

**Profitability and efficiency**

| Metric | What it tells you | Healthy range | Where to find it | Red flag threshold |
|---|---|---|---|---|
| Trading Sales as % of total revenue | Margin-dilutive stream tracking (bought-resold goods typically carry thinner margin than own-manufactured) | Should not rise as a share of the mix if the growth thesis is manufacturing-led | AR Note 25/24, "Sale of Products (Trading Sales)" | Rising share of trading sales alongside falling group EBITDA margin |
| Group EBITDA margin | Whether backward integration (cells, frames) is actually lifting margin as the presentation's thesis claims | Presentation shows FY22 6.3% to FY26 14.0% (Inv. Pres. p.30) — trend should continue, not reverse | Presentation results table / AR P&L | Margin flat or falling once the cell plant is live (would falsify the integration thesis) |
| Operating cash flow vs PAT | Real cash generation vs accounting profit | OCF should track toward PAT as the business matures | AR consolidated cash flow statement | OCF materially negative for more than one more year running |

**Balance sheet and risk**

| Metric | What it tells you | Healthy range | Where to find it | Red flag threshold |
|---|---|---|---|---|
| Trade receivables aged beyond 6 months, and where they sit | Collection quality; currently 39.5% of the book, all at the subsidiary (prior-stage finding) | Should fall as a share of the book as new sales books at normal terms | AR trade receivables ageing note | Rising share, or spreading to the parent |
| Parent guarantee-to-parent-assets ratio | Whether the risk transmission from subsidiary debt back to the listed shell is growing | Should not exceed 1x for a going-concern-safe parent | AR Note 42 (consol), Note 41 (standalone) | Above 3x (already the case at FY26 — Rs 1,654.01cr against Rs 544.04cr) |
| Capital commitments vs cash and undrawn facilities | Funding risk on the announced pipeline (cell, frame, wafer/ingot, IPP) | Committed capex should be covered by cash + sanctioned-but-undrawn debt | AR Note 42(b), capital commitments Rs 901.43cr; IREDA Rs 1,134cr sanctioned, Rs 468.89cr drawn (both prior-stage findings) | Commitments exceeding cash + undrawn sanctioned facilities |

### 3C. Industry-specific non-financial KPIs

| KPI | Where to find it |
|---|---|
| Module manufacturing capacity (GW) and utilisation % | AR p.21-24 (capacity), utilisation NOT FOUND, check investor presentation or concall |
| Cell/frame/wafer/ingot facility commissioning milestones (COD dates) | AR p.21-24; Inv. Pres. p.13 (cell facility progress roadmap) |
| Order book size (GW/Rs cr) | Inv. Pres. p.10, p.25 |
| IPP portfolio under execution (MW) | Inv. Pres. p.10, p.15, p.16 (400MW+ target FY27) |
| Channel partner count | Inv. Pres. p.15, p.19 (1000+) |
| Retail/rooftop customer count | Inv. Pres. p.15 (40,000+) |
| ALMM listing status, BIS/IEC/UL/TÜV/CE certification status | AR p.49; Inv. Pres. p.17 |
| Employee headcount, parent vs group | Prior-stage finding (42 parent, 394 group) |

### 3D. Unit economics — the physics of the business

| Element | Value |
|---|---|
| Unit | 1 Watt (Wp) of module capacity/output is the natural unit, but no per-watt figures are disclosed anywhere in either document |
| Revenue per unit (Rs/Watt or ASP) | NOT FOUND, check investor presentation or concall |
| Cost per unit (Rs/Watt) | NOT FOUND, check investor presentation or concall |
| Volume driver | Installed capacity utilisation against 5.5 GW nameplate (AR p.21-24); order-book conversion (2.1 GW+, Inv. Pres. p.10) |
| Price driver | Global cell/wafer/polysilicon spot prices pass through to module ASP; ALMM/DCR-NDCR classification affects which tenders a given product can bid into (AR p.43, product portfolio) |
| Cost driver | Bought-in raw materials — cells, wafers, aluminium frames, glass, EVA, junction boxes — 77.5% of consolidated revenue via Cost of Raw Material Consumed (Rs 1,662.13cr / Rs 2,146.02cr; AR p.131, Note 27), plus Purchase of Stock-in-Trade Rs 272.06cr for the trading stream |
| Incremental margin / operating leverage | Modest and improving. Employee cost is under 2% of revenue (Rs 38.91cr; AR p.131-132, Note 30), so fixed-cost operating leverage exists, but materials dominate the cost structure (~90% of revenue combined), which caps how much incremental margin any single volume increase can generate until backward integration changes the input-cost base. EBITDA margin has moved from 6.3% (FY22) to 14.0% (FY26) per the presentation's 5-year summary (Inv. Pres. p.30), consistent with gradual, not yet structural, margin gain |

---

## SECTION 4: RISKS, VALUATION APPROACH & MONITORING

### 4A. Business-model-specific risks

| Category | Risk | First financial line item that would deteriorate |
|---|---|---|
| Revenue model | EPC/IPP narrative is not yet monetized; growth could stall if IPP commissioning slips | "Sale of Electricity" line staying flat near Rs 4.22cr (AR p.130, Note 25) for multiple quarters after stated COD |
| Margin | Trading Sales (thinner margin, 17.0% of revenue) growing faster than manufactured Finished Goods sales | Gross margin compression alongside a rising Trading Sales share in Note 25/24 |
| Margin | Raw material cost pass-through failure if cell/wafer prices spike before backward integration is live | Cost of Raw Material Consumed rising faster than revenue in the quarterly P&L |
| Balance sheet | Receivable quality: 39.5% aged beyond 6 months, concentrated at the subsidiary (prior-stage finding) | Trade receivables ageing schedule; provisioning for doubtful debts |
| Balance sheet | Parent guarantee exposure to subsidiary debt (Rs 1,654.01cr vs Rs 544.04cr parent assets, 3.0x, AR p.137, Note 42) | Any subsidiary debt covenant breach or restructuring disclosure |
| Execution | Cell facility (Narmadapuram, 4.5 GW) delay past Q4 FY27/Dec 2026 target | Capital work-in-progress balance stalling without commissioning; capitalised interest continuing without a corresponding revenue line |
| Structural | Three-plus legal entities (listed parent, Insolation Green Energy Pvt Ltd for manufacturing, Insolation Green Infra Pvt Ltd for EPC) plus ~76 project SPVs mean no single P&L tells the whole story | Any future segment reporting change, or a widening gap between standalone and consolidated results |

### 4B. Valuation method applicability

| Method | Applicable? | Note |
|---|---|---|
| Sum-of-the-parts (manufacturing/trading engine + IPP SPV portfolio) | YES — PRIMARY | A single consolidated multiple cannot work here. The manufacturing-and-trading engine (98.9% of FY26 revenue) behaves like a capital-goods/commodity manufacturer and should be valued on an earnings or EBITDA multiple against module-manufacturing peers. The IPP portfolio (~76 SPVs, Rs 1,654.01cr of guaranteed debt, targeting 400MW+ by FY27, but only Rs 4.22cr of FY26 power revenue) is a long-dated, contracted-cashflow asset that should be valued separately, once PPAs and commissioning dates are known, on a per-MW or DCF/NAV basis, heavily risk-adjusted for construction-stage assets. Adding the two gives the fairer picture than any single blended multiple |
| EV/EBITDA on consolidated basis | YES — SECONDARY | A useful sanity cross-check against listed module-manufacturing peers, but only as a cross-check, because it currently blends a near-zero-revenue IPP capital base into the denominator's asset side without a matching earnings contribution, understating true engine profitability |
| EV / installed capacity (Rs cr per GW module, Rs cr per MW IPP) | YES — TERTIARY | Useful during this capex-heavy build-out phase precisely because near-term earnings are not yet stabilised (cell plant not commissioned, IPP not generating). An asset/capacity-based sanity check catches whether the market is paying for capacity that does not yet produce cash |
| Discounted cash flow (DCF) | NOT APPLICABLE (for now) | FY26 consolidated operating cash flow is negative (minus Rs 73.13cr, prior-stage finding) against positive PAT; a near-term FCF projection would be unreliable until the receivable-quality question and the IPP capex-to-revenue lag both resolve |
| Standalone P/E or P/B (listed entity alone) | NOT APPLICABLE | The parent's own consolidation-adjusted share of group profit was NEGATIVE in both FY25 and FY26 (Rs -49.92cr in FY26, -24.88% of consolidated PAT; AR p.152, Note 58). Valuing the listed shell's standalone earnings in isolation misprices the actual economic engine, which sits below it |
| Dividend discount model | NOT APPLICABLE | No dividend disclosed in either document; the company is in a heavy capex/growth phase |
| Cycle stage relevant to valuation | Early-to-mid capex cycle. The presentation's own framing ("TODAY: Industry Margin Reset... TOMORROW: Structural Value Creation", Inv. Pres. p.22) says the re-rating case depends on backward integration landing on schedule. Valuation today should price the manufacturing/trading engine on current fundamentals and treat the IPP and cell/wafer/ingot buildout as embedded, largely unproven optionality, not yet as delivered earnings power |

### 4C. Quarterly monitoring checklist

1. Consolidated revenue growth vs standalone revenue growth (should not structurally diverge)
2. Sale of Electricity (IPP revenue) — trending up from the Rs 4.22cr FY26 base, or still flat
3. Trading Sales as % of total revenue (mix quality)
4. Group EBITDA margin trend (thesis requires it to keep rising, not just hold)
5. Trade receivables aged beyond 6 months, as % of book, and which entity holds them
6. Order book size (GW/Rs cr) and its conversion rate into billed revenue
7. Cell facility (Narmadapuram) commissioning milestones vs the Q4 FY27/Dec 2026 target
8. Aluminium frame facility commissioning vs the Q3 FY27 target
9. Capital work-in-progress balance and whether it is converting to revenue-generating PPE on schedule
10. Parent guarantee balance vs parent standalone total assets (currently 3.0x)
11. IREDA facility drawdown pace (Rs 468.89cr drawn of Rs 1,134cr sanctioned, prior-stage finding)
12. Customer concentration — Solarworld Energy Solutions Ltd's share of revenue, rising or normalising
13. Operating cash flow vs PAT (cash conversion)
14. Any change to the single-segment Ind AS 108 classification (a change would itself be informative)
15. Capital commitments (Rs 901.43cr) vs cash and undrawn sanctioned facilities

### 4D. Highest-value questions for management

1. What is the actual revenue and margin split between the manufacturing subsidiary (Insolation Green Energy Pvt Ltd), the EPC subsidiary (Insolation Green Infra Pvt Ltd), and the ~76 IPP SPVs?
   - Reassuring answer: a clear, consistent split showing each stream's margin and growth trajectory.
   - Worrying answer: "we manage it as one business" with no ability to disaggregate.
2. Why is 39.5% of consolidated trade receivables aged beyond 6 months, and why does it sit entirely at the subsidiary?
   - Reassuring: named large government/PSU counterparties with known, if slow, payment cycles, and a falling trend.
   - Worrying: private-party receivables with no visible collection plan, or a rising trend.
3. What is the actual per-watt module ASP and per-watt cash cost today, and how is that expected to move once the cell plant commissions?
   - Reassuring: a specific number with a credible bridge to post-cell-integration economics.
   - Worrying: no per-unit data offered, or a bridge that assumes global cell prices stay favourable.
4. Why did standalone (parent) revenue fall 13.3% while consolidated revenue grew 60.9%, and is more of the group's real activity migrating away from the listed entity over time?
   - Reassuring: a temporary allocation/timing reason, with parent revenue understood to normalise.
   - Worrying: a structural, continuing shift of the operating business away from the listed shell.
5. What is the plan if the Narmadapuram cell facility COD slips past Q4 FY27/Dec 2026, given the scale of capital committed (Rs 901.43cr) and guaranteed (Rs 1,654.01cr)?
   - Reassuring: a specific contingency and clear lender covenant headroom.
   - Worrying: no contingency, or covenant risk tied to the commissioning date.
6. Has INA itself, as opposed to the industry generally, been allocated capacity under the PLI scheme, and if so how much and on what terms?
   - Reassuring: a specific, named allocation with disclosed terms.
   - Worrying: the PLI references in the AR/MD&A turn out to be generic industry narrative, not an INA-specific benefit (as already seen with the verbatim textile-industry boilerplate flagged by Stage 3 in the same MD&A "Challenges" section).
7. What tariff and offtake terms (PPA counterparties, tenor, tariff) apply to the ~400MW+ IPP pipeline, and when does each project reach COD?
   - Reassuring: named counterparties, signed PPAs, and a credible COD schedule.
   - Worrying: "under discussion" terms with no signed PPAs disclosed.

---

## SECTION 5: ONE-PAGE BUSINESS MODEL SUMMARY CARD

```
=================================================================
BUSINESS MODEL SUMMARY CARD — INSOLATION ENERGY LTD (INA)
=================================================================
BUSINESS TYPE:        Hybrid — manufacturing + trading (98.9% of FY26
                       revenue), with an early-stage, capital-heavy IPP
                       build-out and a distinct EPC subsidiary that has
                       not yet produced a disclosed revenue line.
                       Single Ind AS 108 segment: "Manufacturing &
                       Trading of Solar Photovoltaic Modules"
                       (AR p.144-145, p.185).

REVENUE STREAMS (FY26, consolidated, AR p.130, Note 25):
  - Finished Goods (own-made modules):    81.9%  (Rs 1,757.22cr)
  - Trading Sales (bought-resold):        17.0%  (Rs   364.91cr)
  - Sale of Electricity (IPP):             0.2%  (Rs     4.22cr)
  - Other operational (install/job work):  0.5%  (Rs    10.28cr)

ASSET INTENSITY:      Medium, rising to heavy (group capex Rs 448.05cr
                       FY26 vs Rs 28.43cr standalone; prior-stage
                       finding)
WC INTENSITY:         High and worsening (inventory +4.9x, finished
                       goods ~+14.7x vs revenue +60.9%)
PRICING POWER:        Weak-to-moderate; ALMM/DCR-NDCR gate, not yet a
                       cost or technology edge (cell plant not
                       commissioned)
CYCLICALITY:          Secular-growth demand (policy-driven) riding on
                       top of a cyclical, oversupplied manufacturing
                       segment (national capacity 2.3GW to ~172GW in a
                       decade — AR p.51-52)

TOP RISK:              Structural — three-plus legal entities and ~76
                       project SPVs mean no single financial statement
                       tells the whole story; parent guarantees 3.0x
                       its own assets (AR p.137, Note 42)

VALUATION APPROACH:    Sum-of-the-parts is REQUIRED, not optional.
                       Manufacturing/trading engine on EV/EBITDA vs
                       peers (secondary cross-check); IPP SPV portfolio
                       on per-MW/DCF once PPAs and COD dates are known
                       (part of primary SOTP); EV/capacity as a
                       build-out-phase sanity check (tertiary).
=================================================================
```

---

## Input gaps carried forward

- prospectus (HIGH)
- results (HIGH)
- annual-report-notes-1-3-absent (HIGH)
- rating (MEDIUM)
- shareholding (MEDIUM)
- screening-csv-shells (MEDIUM)
- sector_cap_row-mismatch (MEDIUM)
- announcements-thin (MEDIUM)
- research (LOW)
- peer-concalls-partial (LOW)
- share-count-blank-FY26 (LOW)

Additional gap surfaced this stage: no per-watt ASP, per-watt cost, or
utilisation % disclosed anywhere in the AR or the investor presentation
— unit economics are directionally described but not quantified in the
provided documents (LOW-MEDIUM, check investor presentation earnings
call transcript or concall if available).

---

```yaml
stage: B04-bizmodel
company: "INA"
run_date: "2026-09-06"
model: claude-sonnet-5
status: complete
input_gaps:
  - prospectus (HIGH)
  - results (HIGH)
  - annual-report-notes-1-3-absent (HIGH)
  - rating (MEDIUM)
  - shareholding (MEDIUM)
  - screening-csv-shells (MEDIUM)
  - sector_cap_row-mismatch (MEDIUM)
  - announcements-thin (MEDIUM)
  - research (LOW)
  - peer-concalls-partial (LOW)
  - share-count-blank-FY26 (LOW)
  - no-per-watt-ASP-or-utilisation-disclosed (LOW-MEDIUM)
flags:
  - "Single Ind AS 108 segment ('Manufacturing & Trading of Solar Photovoltaic Modules') means no company-disclosed EPC, IPP, or O&M margin exists; all stream-level economics in this report are derived from the Ind AS 115 revenue disaggregation, not from segment reporting (AR p.144-145, p.149-150)."
  - "Sale of Electricity (IPP revenue) is only Rs 4.22cr, 0.2% of FY26 consolidated revenue, despite the narrative emphasis on a 400MW+ IPP pipeline and large associated capex and guarantees (AR p.130, Note 25)."
  - "Parent guarantees Rs 1,654.01cr of subsidiary debt against its own Rs 544.04cr assets (3.0x), including a reverse guarantee where the subsidiary guarantees a parent AU Bank facility (AR p.137, Note 42)."
  - "MD&A PLI/PM MITRA references repeat the same generic, possibly copy-pasted industry narrative flagged by Stage 3 (textile-scheme boilerplate); no INA-specific PLI allocation is disclosed (AR p.55-56)."
business_type: "hybrid"
revenue_streams:
  - {name: "Finished Goods (own-manufactured modules)", type: "manufacturing, point-in-time goods", pct_of_revenue: 81.9, predictability: "M"}
  - {name: "Trading Sales (bought-and-resold goods)", type: "trading, point-in-time goods", pct_of_revenue: 17.0, predictability: "L"}
  - {name: "Sale of Electricity (IPP)", type: "asset-owner power sale", pct_of_revenue: 0.2, predictability: "H"}
  - {name: "Other operational revenue (installation, job work, scrap, freight)", type: "services/ancillary", pct_of_revenue: 0.5, predictability: "L"}
asset_intensity: "medium"
wc_intensity: "high"
pricing_power: "weak"
cyclicality: "cyclical"
moats_present:
  - {moat: "Regulatory/licence (ALMM listing, BIS/IEC/UL/TUV/CE certification)", durability: "medium"}
  - {moat: "Scale (5.5 GW installed capacity)", durability: "medium"}
  - {moat: "Distribution (1000+ channel partners, pan-India dealer network)", durability: "medium"}
  - {moat: "Brand (IPL sponsorship, retail recall)", durability: "low-medium"}
valuation_methods:
  primary: {method: "Sum-of-the-parts: manufacturing/trading engine (EV/EBITDA-style) + IPP SPV portfolio (per-MW/DCF/NAV)", why: "A single consolidated multiple cannot represent a 99%-revenue commodity manufacturing/trading engine bolted to a ~76-SPV, near-zero-revenue but capital- and guarantee-heavy IPP build-out; the parts have structurally different risk, cash-cycle, and earnings-timing profiles"}
  secondary: {method: "EV/EBITDA on consolidated basis vs listed module-manufacturing peers", why: "Useful sanity cross-check on the dominant manufacturing/trading engine, but must be read knowing it understates true engine profitability by blending in near-zero-earning IPP capital"}
  tertiary: {method: "EV / installed capacity (Rs cr per GW module, Rs cr per MW IPP)", why: "Appropriate during this capex-heavy build-out phase when near-term earnings are not yet stabilised (cell plant not commissioned, IPP not generating); flags if the market is pricing capacity that has not yet produced cash"}
  not_applicable:
    - "DCF (near-term FCF unreliable; FY26 consolidated OCF is negative against positive PAT)"
    - "Standalone P/E or P/B (parent's consolidation-adjusted profit share was negative in both FY25 and FY26, per AR p.152 Note 58)"
    - "Dividend discount model (no dividend disclosed; heavy capex/growth phase)"
irrelevant_ratios:
  - {ratio: "Standalone-only revenue growth or P/E", why: "Standalone revenue fell 13.3% in FY26 while consolidated revenue grew 60.9%; reading the listed entity alone inverts the real trend"}
  - {ratio: "Blended consolidated ROCE/ROE", why: "Mixes a mature trading stream, a growing manufacturing stream, and a pre-revenue, capital-heavy IPP base with almost no return yet"}
  - {ratio: "Blended cash conversion (OCF/EBITDA)", why: "FY26 OCF is negative against ~Rs 200cr PAT; the blended ratio cannot separate genuine receivable-quality risk from normal IPP/EPC working-capital build"}
  - {ratio: "Blended inventory turnover / receivable days", why: "Mixes fast-moving trading inventory, manufacturing WIP, and long-cycle EPC/IPP project inventory; hides which piece is deteriorating"}
  - {ratio: "Blended fixed-asset turnover", why: "IPP capex lands ahead of IPP revenue by design; a single ratio looks artificially weak even if manufacturing asset efficiency is fine"}
  - {ratio: "Any implied segment-margin comparison", why: "No reportable segment exists; Ind AS 108 discloses one segment, 'Manufacturing & Trading of Solar Photovoltaic Modules'"}
  - {ratio: "Parent guarantee coverage read from either entity's balance sheet alone", why: "The Rs 1,654.01cr guarantee (3.0x parent assets) includes a reverse guarantee from the subsidiary back to the parent; reading one entity in isolation hides the circular exposure"}
must_track_metrics:
  - {metric: "Sale of Electricity (IPP revenue)", healthy: "Scaling toward a run-rate consistent with commissioned MW x load factor x tariff", red_flag: "Stays near Rs 4-5cr for multiple quarters after stated COD dates"}
  - {metric: "Trade receivables aged beyond 6 months, % of book", healthy: "Falling share as new sales book at normal terms", red_flag: "Rising share, or spreading from subsidiary to parent"}
  - {metric: "Group EBITDA margin", healthy: "Continuing the FY22 6.3% to FY26 14.0% rise", red_flag: "Flat or falling once the cell plant commissions"}
  - {metric: "Consolidated vs standalone revenue growth", healthy: "Directionally aligned over time", red_flag: "Sustained divergence beyond one year"}
  - {metric: "Parent guarantee-to-parent-assets ratio", healthy: "Below 1x", red_flag: "Above 3x, already the case at FY26 (Rs1,654.01cr / Rs544.04cr)"}
unit_economics:
  unit: "1 Watt (Wp) of module capacity/output (natural unit; no per-watt figures disclosed)"
  revenue_per_unit: "NOT FOUND, check investor presentation or concall"
  margin_per_unit: "NOT FOUND, check investor presentation or concall"
  key_lever: "Bought-in raw material cost (cells, wafers, aluminium frames) at ~78% of revenue; backward integration into cells/frames/wafers is the stated lever to change this, not yet commissioned"
first_deterioration_signals:
  - {risk: "EPC/IPP narrative not yet monetized", first_signal: "Sale of Electricity line stays flat near Rs 4.22cr for multiple quarters after stated COD"}
  - {risk: "Trading Sales displacing manufactured sales (margin dilution)", first_signal: "Trading Sales share of Note 25/24 revenue rises alongside gross margin compression"}
  - {risk: "Raw material pass-through failure", first_signal: "Cost of Raw Material Consumed rising faster than revenue in the quarterly P&L"}
  - {risk: "Receivable quality deterioration", first_signal: "Trade receivables aged beyond 6 months rises further or spreads to the parent entity"}
  - {risk: "Parent guarantee exposure crystallising", first_signal: "Any subsidiary debt covenant breach or restructuring disclosure"}
  - {risk: "Cell facility execution delay", first_signal: "Capital work-in-progress balance stalls without commissioning past Q4 FY27/Dec 2026"}
  - {risk: "Structural opacity across entities", first_signal: "Widening gap between standalone and consolidated results, or a segment-reporting change"}
mgmt_questions:
  - "What is the actual revenue and margin split between the manufacturing subsidiary, the EPC subsidiary, and the ~76 IPP SPVs?"
  - "Why is 39.5% of consolidated trade receivables aged beyond 6 months, and why does it sit entirely at the subsidiary?"
  - "What is the actual per-watt module ASP and per-watt cash cost today, and how does that change once the cell plant commissions?"
  - "Why did standalone revenue fall 13.3% while consolidated revenue grew 60.9%, and is real activity migrating away from the listed entity?"
  - "What is the contingency plan if the Narmadapuram cell facility COD slips past Q4 FY27/Dec 2026?"
  - "Has INA itself been allocated capacity under the PLI scheme, and on what terms?"
  - "What tariff and offtake terms (PPA counterparties, tenor, tariff) apply to the ~400MW+ IPP pipeline, and when does each project reach COD?"
one_line_verdict: "Commodity module manufacturer/trader today; the EPC-IPP-cell integration story is capital-heavy but revenue-unproven."
analyst_note: "The single most load-bearing finding this stage: Ind AS 115 disaggregation (AR p.130, p.149-150) shows FY26 consolidated revenue is 81.9% own-manufactured Finished Goods, 17.0% Trading Sales, and only 0.2% Sale of Electricity. The AR and investor presentation both foreground EPC, IPP, BESS and cell/wafer/ingot integration, but the accounts show none of that has yet become a material, disclosed revenue line, and the group's own Ind AS 108 note still classifies itself as one segment. This is not evidence the transition thesis is false; it is evidence the transition has not yet shown up in reported revenue, so Stage 11/FTTCP should not treat EPC/IPP as an earnings stream to multiply, only as unresolved optionality plus committed capital and guarantee risk. The parent-vs-subsidiary structure (three-plus entities, ~76 SPVs) is real and load-bearing for both the WC and the valuation-method questions; treat every future ratio or multiple as needing the same SOTP lens applied here."
```
