# STAGE 4 — BUSINESS MODEL DECODER
Company: Millworks Technologies Limited (MILLWORKS) | Run date: 2026-08-22 | Model: claude-sonnet-5

## SOURCE NOTE AND SECTOR CORRECTION

The manifest tagged this company "Pharma / CDMO." That tag is wrong. The RHP
states plainly: "We are a precision engineering company engaged in the
manufacture of machined components, sheet metal parts, and integrated
assemblies used in mission-critical applications across the railways,
aerospace, defence, and semiconductor sectors" (RHP p.120). This is a
**Build-to-Print (BTP) / Build-to-Spec (BTS) precision-engineering component
maker** (RHP p.120), AS9100D-certified (RHP p.151), operating four Bengaluru
units. Peers named in the RHP itself are Unimech Aerospace and Manufacturing
Ltd and Azad Engineering Ltd (RHP p.94, p.96-98); the operator brief adds
Airfloa Rail and Apsis Aero. Archetype: **Build-to-spec component maker**
(customer capex cycle, design-win pipeline, content per unit, input-cost
pass-through).

No investor presentation was provided. The one presentation-folder document
is a SEBI Reg 30 order-book intimation and press release, used here only for
the Quik Pay/drone context it adds (already covered in the RHP itself, so no
material new fact was added beyond what RHP discloses).

**The single most important business-model fact in this file**: the
company's largest customer, contributing 47.02% of FY26 revenue (₹6,992.76
Lakh) under the "Defence" sector line, is **Quick Pay Private Limited**
(RHP p.28, Risk Factor 3, naming "Customer 1" explicitly as Quick Pay). The
same Quick Pay is also (a) a strategic equity investee — Millworks holds
5,332 shares, ₹575.06 Lakh, no ownership % disclosed (RHP Annexure XV,
p.F20/p.130); (b) the counterparty whose own delayed cash receipts are
explicitly blamed for part of the FY26 receivables blow-up (RHP p.90); and
(c) the destination of a "bill-to-ship-to" drone-component supply chain
that also runs through a second dependency, Big Bang Boom Solutions Private
Limited, for assembly/integration (RHP p.130, Risk Factor 4). Three separate
risks (customer concentration, related-party receivables, execution
dependency) trace back to one counterparty. Every section below treats this
as the central fact, not a footnote.

---

## SECTION 1: THE BUSINESS MODEL IN PLAIN ENGLISH

### 1A. One-line description
Millworks machines precision metal parts to a customer's exact drawing or
spec, for people who cannot afford the part to be wrong: aircraft engines,
missiles and drones, trains, and chip-making machines.

### 1B. Money flow chain, by revenue stream

**Aerospace** (0.99% of FY26 revenue, RHP p.124): [customer sends drawing
for an aero-engine turbocharger bracket or turbine blade component] →
[Millworks machines it on CNC/EDM equipment to the drawing, inspects it,
documents traceability] → [delivers Ex-Factory] → [aero-engine OEM/Tier-1
pays] → [payment on purchase-order terms, no long-term contract, RHP
p.28].

**Defence** (69.43% of FY26 revenue, RHP p.124, dominated by Quick Pay at
47.02% of total company revenue, RHP p.28): [customer specifies missile
airframe components, drone structural frames, BLDC motor housings] →
[Millworks machines and, for the Quick Pay drone programme, also designs/
engineers under a new "Sale of Services" line (₹2,300 Lakh FY26, first
year, RHP Annexure XXIV/p.130)] → [sub-assembled drone components are
carried to Big Bang Boom Solutions' Chennai facility for assembly/
integration, then delivered to Quick Pay under a bill-to-ship-to model,
RHP p.130] → [Quick Pay integrates into finished drones and pays Millworks]
→ [payment timing partly depends on Quick Pay's own cash receipt from its
downstream sale, RHP p.90 — an unusual double dependency: Millworks is
paid only after its customer, which it also part-owns, is paid].

**Railways** (23.65% of FY26 revenue, RHP p.124, the largest sector before
FY26): [customer specifies brake, door, coupler, or pantograph components
for passenger trains/metro] → [machined and delivered Ex-Factory] →
[railway OEM/Tier-1 pays on PO terms].

**Semiconductor** (5.94% of FY26 revenue, RHP p.124): [customer specifies
machine base frames, chip-handling fixtures, load-testing fixtures] →
[machined to tight tolerance, inspected with CMMs] → [delivered, customer
pays].

**Exports** (27.47% of FY26 revenue, cutting across all four sectors, to 9
countries: Canada, USA, Israel, Germany, France, Macedonia, Italy, UK,
Czech Republic — RHP p.126-127): revenue is recognised Ex-Factory even for
export shipments (RHP Annexure IV §2.13, p.F12) — i.e. the company books
the sale the moment goods leave its Bengaluru gate, before the customer
takes delivery abroad.

### 1C. Revenue model classification table

| Stream | Type | % of FY26 revenue (anchor) | Predictability |
|---|---|---|---|
| Defence (dominated by Quick Pay) | Manufacturing, BTP/BTS, job-order + new design/engineering service line | 69.43% (RHP p.124) | Low — single-customer 47% of total revenue, no long-term contract (RHP p.28) |
| Railways | Manufacturing, BTP/BTS, job-order | 23.65% (RHP p.124) | Medium — most repeat-customer history (largest FY24 segment) |
| Semiconductor | Manufacturing, BTP/BTS, job-order | 5.94% (RHP p.124) | Low-Medium — smallest customer count, tied to chip-equipment capex cycles |
| Aerospace | Manufacturing, BTP/BTS, job-order | 0.99% (RHP p.124) | Low — smallest and shrinking share (8.91% FY24 → 0.99% FY26) |
| Export overlay (cross-sector) | Manufacturing, job-order, FOB-adjacent geography, Ex-Factory recognition | 27.47% (RHP p.127) | Medium — stable ~30% share three years running, but revenue point is aggressive (Ex-Factory, not on acceptance) |

### 1D. Simplified business model canvas

| Element | Answer |
|---|---|
| What they sell | Machined metal components/sub-assemblies to a customer's own drawing (BTP) or spec (BTS) — not a Millworks-branded product (RHP p.120) |
| Who buys | OEMs, Tier-1 and Tier-2 suppliers in aerospace, defence, railways, semiconductor (RHP p.127); 74 customers FY26, but 92.06% of revenue from the top 10 (RHP p.140) |
| Why them | AS9100D/ISO9001:2015 multi-site quality certification (RHP p.151), 4-year track record of on-time delivery for approved programmes; NOT cost leadership — EBITDA margin (36.71%) trails both named peers (Unimech 42.47%, Azad 41.78%, RHP p.96-98) |
| How delivered | Ex-Works from four Bengaluru units; customer arranges transport (RHP p.147) |
| Cost structure dominance | Raw material (steel, aluminium, titanium, brass) = 51.05% of FY26 revenue (Cost of Material Consumed ₹7,595.53L / Revenue ₹14,876.70L, RHP Annexure XXVI/XXIV); direct/subcontract expenses 6.7%; employee cost 5.97% |
| Scarce resource | AS9100D-qualified capacity and customer-approved-vendor status, not raw material or capital |
| Pricing power source or absence | Absent-to-weak: PO-by-PO negotiated pricing (RHP risk factor 6, p.28), no long-term contracts, margin below both named listed peers |
| Asset intensity | Medium: leased land/buildings (not owned — see 1D Immovable Property, RHP p.150-151), but CNC/EDM/laser capex programme of ₹61.03 Cr proposed from this very IPO (RHP p.84-86) |
| WC intensity | High: WC days rose from 136 (FY24) to 191 (FY26); receivable days rose from 73 to 340 on a year-end basis (Gate0 scorecard, B01-gate0.yaml) |
| Regulatory moat or burden | Mild moat (AS9100D/ISO certification is a real qualification barrier, RHP p.151) but no licence-scarcity dynamic; export control (SCOMET) compliance is a burden, not an advantage (RHP p.127) |

### 1E. The chai-stall-uncle version

Imagine a tailor who does not sell his own clothes. Instead, big companies
that make planes, missiles, trains, and chip machines hand him a precise
paper pattern and say "stitch exactly this, in steel or titanium, to the
millimetre." He has four small workshops in Bangalore with fancy cutting
machines. Almost half his work last year came from one customer who also
happens to own a small piece of his workshop — and that customer pays him
only after IT gets paid by whoever buys the finished drone. His order book
right now covers only about five months of work, not years, so he has to
keep winning the next order. He grew nine-fold in one year, which sounds
great, but he is owed nearly a full year's sales by customers who have not
paid yet, so the growth has not turned into cash in his pocket.

### Section 1 summary table

| Field | Value |
|---|---|
| Business type | Manufacturing (job-order, BTP/BTS precision engineering), with a small (15.5% FY26) new design/engineering services sliver (RHP Annexure XXIV, p.F25) |
| Revenue nature | Purchase-order based, non-contractual, high single-customer dependency |
| Asset intensity | Medium (leased facilities, owned machinery, active capex programme) |
| WC intensity | High (WC days 136→164→191 over FY24-26; Gate0 B01) |
| Pricing power | Weak (below-peer EBITDA margin, no long-term contracts, extreme customer concentration) |

---

## SECTION 2: INDUSTRY DYNAMICS & COMPETITIVE POSITION

### 2A. Five forces, plainly

| Force | Reading | Helps / Hurts / Neutral |
|---|---|---|
| Competition intensity | RHP's own Competition section: "We face competition from both large organized manufacturers and mid-sized enterprises catering to similar customer segments... based on quality, technical capability, delivery performance, pricing, and compliance" (RHP p.152) — a thin, generic disclosure with no competitor count given | Hurts (crowded, price/quality contested; disclosure itself is thin — verification gap) |
| Entry barriers | AS9100D/ISO9001 certification, customer qualification cycles, and capex for CNC/wire-EDM/laser equipment are real (RHP p.124, p.151); but Millworks itself went from ₹9.4 Cr revenue (FY24) to ₹148.8 Cr (FY26) in two years, proving the barrier is surmountable quickly given capital and relationships | Neutral-to-hurts (barriers exist but are not high enough to have kept out this very entrant) |
| Supplier power | Supplier-1 concentration jumped from 22.01% (FY24) to 12.77% (FY25) to **44.05%** (FY26) of total purchases (RHP p.141); raw material price fluctuation named as a threat in the company's own SWOT (RHP p.131) | Hurts (single-supplier dependency worsening sharply) |
| Customer power / concentration | Top 5 customers = 81.07% of FY26 revenue; top 10 = 92.06% (RHP p.121, p.140); single customer (Quick Pay) = 47.02% (RHP p.28); no long-term contracts, PO-basis only (RHP risk factor 6, p.28) | Hurts, materially — this is the dominant force in the whole file |
| Substitutes | Once a component is qualified into a customer's approved-vendor programme, substitution has friction; but the company's own risk factor 3 explicitly names "increased in-house execution of services" by its top customer as a live risk (RHP p.28) | Mixed — friction exists but the top customer is disclosed as a potential substitute-in-house risk |

### 2B. Competitive positioning vs named peers (RHP's own comparison table, p.96-98)

| Company | FY26 Revenue (₹ Lakh) | FY26 EBITDA margin | FY26 RoCE | FY26 D/E | P/E (as of RHP date) |
|---|---|---|---|---|---|
| **Millworks** | 14,876.70 | 36.71% | 56.44% | 0.21 | Not yet priced (IPO) |
| Unimech Aerospace & Mfg Ltd | 24,049.04 | 42.47% | 11.11% | 0.17 | 87.87x |
| Azad Engineering Ltd | 60,297.50 | 41.78% | 10.63% | 0.31 | 96.45x |

Millworks is the smallest of the three by revenue (roughly 1/4 of Unimech,
1/24 of Azad in scale), and runs the lowest EBITDA margin of the three
(RHP p.96-98). Its ROCE looks far stronger, but that is a base-effect
artefact of a 2-year-old restated revenue window opening near-nil, not
evidence of superior capital efficiency at maturity (Gate0 analyst note,
B01-gate0.yaml). Peer market multiples (88-96x P/E) show the segment
trades on a growth/story basis, not earnings quality — relevant context
for Section 4B below. Airfloa Rail and Apsis Aero (operator-flagged peers)
were not covered in this RHP's own comparison table; not anchored here.

### 2C. Moat assessment (eight standard types)

| Moat type | Present? | Evidence | Durability |
|---|---|---|---|
| Cost advantage | No | EBITDA margin (36.71%) below both named peers (42.47%, 41.78%, RHP p.96-98); Gate0 quant test M2 scored 0/5 | N/A |
| Switching costs | Weak-moderate | AS9100D qualification and customer-approved-drawing status create some program-specific stickiness, but "we generally do not enter into long-term arrangements with our customers" (RHP risk factor 6, p.28) undermines it | Program-specific, not company-wide; low durability |
| Network effects | Absent | B2B point-to-point component supply; no platform dynamic | N/A |
| Intangible assets / certification | Weak-moderate | AS9100D + ISO9001:2015 multi-site certification (RHP p.151) is a real qualification barrier, but shared broadly across the peer set; one trademark application only, "Formalities Check Pass" status, not yet granted (RHP p.150) | Moderate — real but not unique |
| Efficient scale | Absent | Smallest of the three named comparable listed peers by revenue (RHP p.96-98); capacity utilization only 72-77% across units (RHP p.131), meaning there is room for more entrants at this scale | N/A |
| Regulatory / licence scarcity | Weak | Certification is a qualification hurdle, not a licence/quota; India's "Make in India" defence-indigenisation push (RHP p.113-115) is a sector tailwind available to all qualified players, not a Millworks-specific moat | Low |
| Distribution | Absent | Direct OEM/Tier-1/Tier-2 supply; no channel network disclosed | N/A |
| Customer captivity / repeat business | Weak-moderate | Repeat-customer share 44.59% (FY26), 50.00% (FY25), 20.00% (FY24) of customer count (RHP p.140) — a real and rising trend, but sits on top of extreme concentration (top-10 = 92.06%) and zero long-term contracts, so it is fragile, not durable | Fragile |

**Overall moat classification: MODERATE**, consistent with Gate0's
independent quantitative scoring (13/60, 3 of 12 tests confirmed: pricing
power, capital efficiency, customer stickiness — B01-gate0.yaml). No moat
here is structurally durable; the strongest is the certification/
qualification barrier, and even that is shared with the peer set.

### 2D. Industry lifecycle stage

**Growth stage.** India's defence production target of ₹3 lakh crore by
2029 (RHP p.114), defence exports up 12% YoY to ₹23,622 Cr in FY25 (RHP
p.113), India's semiconductor end-demand forecast to grow at 15% CAGR
2025-2030 (RHP p.116), and Indian Railways' record ₹2.93 lakh crore FY26-27
capex allocation with Vande Bharat rollout (RHP p.118-119) are all
structural tailwinds. Millworks itself is a sub-scale, early-stage
participant within that growing addressable market — proving out execution
and cash discipline, not yet an established leader.

### 2E. Key industry drivers

| Driver | Direction | Impact on Millworks |
|---|---|---|
| Defence indigenisation / Make in India (RHP p.113-115) | Up | Helps — structural demand tailwind for a qualified domestic BTP/BTS supplier |
| Semiconductor equipment localisation, 15% CAGR to 2030 (RHP p.116) | Up | Helps — smallest of the four sectors today (5.94%), room to grow |
| Railways capex / Vande Bharat expansion (RHP p.118-119) | Up | Helps — historically the company's largest segment |
| Raw material price volatility (steel, aluminium, titanium, brass) | Volatile | Hurts/mixed — named as a threat in the company's own SWOT (RHP p.131); no hedging programme disclosed anywhere in the notes |
| Customer capex/order cycle timing (aero-engine, chip-equipment cycles) | Cyclical | Mixed — adds cyclicality; order book covers only ~5-6 months of FY26 revenue run-rate (₹67.14 Cr order book, RHP p.129, vs ₹148.77 Cr FY26 revenue) |

---

## SECTION 3: FINANCIAL METRICS THAT MATTER FOR THIS BUSINESS MODEL

### 3A. Ignore-these / track-these

| Commonly tracked ratio | Why it misleads here |
|---|---|
| Same-period revenue growth in isolation | 573% FY26 growth (RHP p.121) is a near-nil-base artefact (FY24 revenue was only ₹9.4 Cr) plus a single-customer step-change (Quick Pay), not organic broad-based demand growth |
| PAT / EPS trend as a standalone quality signal | The restated accounts carry a 14-category restatement cluster including management's own admission that sales were recognised in the wrong (early) period in both FY24 and FY25 (Notes-pass1 §12, Annexure IV §3, RHP p.F15); FY26 PBT also includes an ₹441.00 Lakh (8.8% of PBT) non-operating FX translation gain (Notes-pass1 §12) |
| Debt/Equity ratio (0.21) in isolation | Understates true leverage risk: nearly all secured facilities carry personal guarantees from all four promoters (₹13.80 Cr guaranteed FY26, up 2.5x YoY) plus promoter real estate cross-collateralised for the entire Axis Bank exposure (Notes-pass1 §7) |
| Standard DSO benchmark vs industry norm | The FY26 spike (73→340 days) is substantially one counterparty (Quick Pay) whose own payment timing gates Millworks' collection (RHP p.90); blending this into a single "industry DSO" comparison hides the concentration story |
| Segment/geography diversification read from the 4-sector revenue table | The company self-asserts single-segment/single-geography reporting under AS-17 with thin supporting evidence (Notes-pass1 §11); the "4 sectors" framing understates that 69% of revenue sits in one customer relationship (Quick Pay, defence-tagged) |
| COGS-to-revenue ratio, single-year read | FY26 includes a brand-new, zero-COGS-attributed "Sale of Services" line (₹23 Cr, 15.5% of revenue, first year ever, RHP Annexure XXIV) that mechanically improves the blended ratio without a like-for-like product-margin comparison |

### 3B. Must-track metrics

**Growth**

| Metric | Tells you | Healthy range (this industry) | Where to find | Red flag |
|---|---|---|---|---|
| Order book value and book-to-bill | Forward revenue visibility | Order book ≥ 9-12 months of trailing revenue | RHP p.129 (₹67.14 Cr as of 05-Jun-2026, updated quarterly per Reg 30 filings) | Order book < 6 months trailing revenue (currently ~5.4 months: 67.14/148.77×12) |
| Top-customer / Quick Pay revenue % | Concentration risk | Single customer < 30% | RHP p.28/p.140 top-10 table (currently 47.02%) | Rising further, or any drop signalling non-renewal |
| Repeat-customer % (by customer count) | Relationship durability | ≥ 50%, rising | RHP p.140 (44.59% FY26, 50.00% FY25) | Falling YoY |

**Profitability & efficiency**

| Metric | Tells you | Healthy range | Where to find | Red flag |
|---|---|---|---|---|
| EBITDA margin vs peer median | Pricing/cost position | ≥ peer median (~42%, RHP p.96-98) | RHP KPI table / quarterly filings | Sustained gap below peer median, or declining trend |
| Capacity utilization % by unit | Whether new capex is needed / justified | 75-85% (efficient, room to grow) | RHP p.131 (currently 72-77% across units) | Utilization plateaus below 70% even after new capex lands |
| Revenue per employee | Labour productivity/scale | Rising YoY | RHP p.146 (₹92.4 Lakh/employee FY26 computed: 14,876.70L/161) | Flat or falling as headcount grows faster than revenue |

**Balance sheet & risk**

| Metric | Tells you | Healthy range | Where to find | Red flag |
|---|---|---|---|---|
| Operating cash flow / PAT (cash conversion) | Earnings quality | ≥ 0.8x | RHP restated cash flow (Notes-pass1; currently −0.29x cumulative FY24-26) | Below 0.5x, or negative |
| MSME payable balance and unpaid interest | Supplier-funded working capital, compliance risk | MSME payable stable, interest fully paid | Notes-pass1 §8, Annexure XLVII | MSME payable and unpaid interest both growing YoY (currently 10x and 9x growth respectively in FY26) |
| Guaranteed debt / promoter personal exposure | True leverage and promoter over-extension risk | Guaranteed debt growth ≤ overall debt growth | Notes-pass1 §3 (Annexure XXXIV, p.F31) | Guaranteed debt growing faster than total debt (currently 2.5x in FY26 alone) |

### 3C. Industry-specific non-financial KPIs

| KPI | Where to find |
|---|---|
| Order book value and composition by sector | RHP p.129 (updated via Reg 30 filings post-listing) |
| Top-5 / top-10 customer revenue concentration | RHP p.121, p.140 |
| Repeat-customer count and % | RHP p.140 |
| Capacity utilization % by unit (installed vs actual hours) | RHP p.131 |
| Supplier concentration % (top supplier, top 10) | RHP p.141 |
| Certification status per unit (AS9100D, ISO9001:2015) | RHP p.151 |
| Export revenue % and country count | RHP p.126-127 |
| Headcount by function, contractual worker % | RHP p.146 |

### 3D. Unit economics — the physics of the business

There is no single standardised "unit" in a BTP/BTS job-shop: the order
book itself ranges from ₹0.02 Lakh to ₹2,577.37 Lakh per customer order
(RHP p.129). Two better proxy units:

| Proxy unit | FY26 value | Computation |
|---|---|---|
| Revenue per installed machine-hour | ≈ ₹3,884/hour | ₹14,876.70 Lakh ÷ 383,019 total installed hours (RHP p.131) |
| Revenue per employee | ≈ ₹92.4 Lakh | ₹14,876.70 Lakh ÷ 161 employees (RHP p.146) |

- **Volume driver**: new design-win/qualification wins across the four
  sectors, plus headroom in existing capacity (72-77% utilization, RHP
  p.131) before the new ₹61.03 Cr capex programme is even needed.
- **Price driver**: negotiated per-purchase-order, no long-term fixed
  contracts (RHP risk factor 6, p.28); competition on quality, delivery,
  price, and certification compliance (RHP p.152).
- **Cost driver**: raw material dominates at 51.05% of revenue (Cost of
  Material Consumed ₹7,595.53L / Revenue ₹14,876.70L, RHP Annexure XXVI);
  direct/subcontract (incl. Big Bang Boom assembly fees) 6.7%; employee
  cost only 5.97% — this is a materials-pass-through business, not a
  labour-cost story.
- **Incremental margin / operating leverage**: EBITDA margin expanded
  29.55% (FY24) → 35.18% (FY25) → 36.71% (FY26) as revenue scaled 429%/
  135%/573% (RHP p.121) — real evidence of fixed-cost absorption as volume
  grew. But this margin expansion did not convert to cash: operating cash
  flow went from +₹65.28L (FY24) to −₹1,076.29L (FY26) over the same
  window (Gate0 B01-gate0.yaml, Block B = 0/20). Operating leverage on the
  P&L, without operating leverage in cash, is the single biggest tension
  in this business model.

---

## SECTION 4: RISKS, VALUATION APPROACH & MONITORING

### 4A. Business-model-specific risks

| Category | Risk | First financial line item that would deteriorate |
|---|---|---|
| Revenue model | Quick Pay (47% of revenue) reduces or cancels orders, or in-sources the work — RHP names this explicitly as a top risk factor (p.28) | Order book "Pending Amount" for the Defence-sector customers (RHP p.129 table); quarterly revenue by sector |
| Revenue model | No long-term contracts anywhere; any customer can walk at PO renewal (RHP p.28) | Repeat-customer % (RHP p.140) falling YoY |
| Margin | Raw material price pass-through fails (steel/aluminium/titanium volatility, no hedging disclosed, RHP p.131 SWOT) | Cost of Material Consumed as % of revenue widening past 51% |
| Margin | Supplier-1 now 44.05% of purchases (RHP p.141), up from 12.77% a year earlier — pricing leverage shifting to the supplier | Gross margin / EBITDA margin compression in the following quarter |
| Balance sheet | Working-capital-funded-by-suppliers via unpaid MSME dues (10x growth FY26, Notes-pass1 §8) is not sustainable and carries legal/compliance exposure | MSME payable balance and unpaid MSMED-Act interest (Notes-pass1 §8, Annexure XLVII) |
| Balance sheet | Receivables collection depends partly on Quick Pay's own cash receipt (RHP p.90) — a circular, related-party-adjacent liquidity risk | Trade receivable days / ageing >6 months bucket (Notes-pass1 §4) |
| Execution | ₹61.03 Cr new capex not yet ordered — only vendor quotations obtained, no purchase orders placed (RHP p.86) | Capacity utilization % by unit staying flat despite the capex objective |
| Execution | Dependency on Big Bang Boom Solutions' Chennai facility for drone assembly/integration (RHP risk factor 4, p.25) | Pending Amount on Defence-sector orders routed through the BBB execution flow |
| Structural | Section 185 breach (loans to related-party directors, cured only by FY26 repayment) and a 14-category restatement cluster including twice-repeated premature revenue recognition (Notes-pass1 §2, §12) signal thin financial controls maturity for a newly-listed entity | Any recurrence of restatement items in the first post-listing annual results |

### 4B. Valuation method applicability

| Method | Applicability | Reasoning |
|---|---|---|
| **EV/EBITDA — PRIMARY** | High | Cleanest cross-sectional comparison for a capex-cycle manufacturer; strips out the 115BAB→115BAA tax-regime distortion (Notes-pass1 §1), the ₹613.14 Lakh goodwill amortisation drag (Notes-pass1 §1/§12), and the ₹441.00 Lakh non-operating FX gain sitting in PBT (Notes-pass1 §12). Peer EBITDA margins (Unimech 42.47%, Azad 41.78%, RHP p.96-98) give a real, comparable anchor. |
| **P/E vs peer group — SECONDARY** | Medium | The RHP's own Basis for Issue Price uses this (weighted 3-yr EPS ₹17.34, peer P/E 87.87x-96.45x, RHP p.93-94), so it is the market convention for this segment; but earnings quality here is compromised by the restatement cluster and the FX gain, so this must be read only alongside the EV/EBITDA primary, never alone. |
| **Order-book coverage / revenue-visibility check — TERTIARY** | Supplementary only | Order book (₹67.14 Cr, RHP p.129) covers only ~5.4 months of FY26 revenue run-rate — not a stand-alone valuation method, but an essential sanity check on any forward-revenue assumption feeding the primary/secondary methods above. |
| DCF | Not applicable now | Only 3 restated years exist, all 3 FCF-negative (Gate0 Block B = 0/20); no reliable multi-year cash-flow forecast base exists yet. Revisit once cash conversion (currently −0.29x cumulative CFO/PAT) turns positive for 2+ consecutive years. |
| Asset-based / NAV / replacement cost | Not applicable | All four manufacturing units are leased, not owned (RHP p.150-151); this is not an asset-value story. |
| Dividend discount | Not applicable | No dividend history or stated policy; a growth-stage SME reinvesting fully. |
| Sum-of-parts | Not applicable | Single reporting segment, self-asserted under AS-17 (Notes-pass1 §11); no distinct business units to separately value. |

**Cycle stage that matters for valuation**: mid-growth, pre-consolidation.
The addressable market (defence indigenisation, semiconductor
localisation, rail capex) is early-growth-stage (Section 2D), but
Millworks' own P&L (2 restated years off a near-nil base) has not yet
proven it can hold margin and convert profit to cash through a full
customer-order cycle. Any EV/EBITDA or P/E multiple applied should be
cross-checked against the Section 1B destination-PE authority per pipeline
rules; this stage does not set that multiple.

### 4C. Quarterly monitoring checklist

1. Quick Pay / Customer-1 revenue as % of quarterly sales (RHP p.28)
2. Quick Pay receivables ageing and collection status (RHP p.90)
3. Trade receivable days, company-wide (Notes-pass1 §4)
4. Order book value and sector mix, book-to-bill ratio (RHP p.129)
5. Repeat-customer % of total customer count (RHP p.140)
6. Capacity utilization % by unit (RHP p.131)
7. EBITDA margin vs the FY26 base of 36.71% and vs peer median (RHP p.96-98)
8. Operating cash flow vs PAT (cash conversion ratio)
9. MSME payable balance and unpaid MSMED-Act interest accrual (Notes-pass1 §8)
10. Supplier-1 concentration % of purchases (RHP p.141)
11. Related-party transaction volume with V3 Technologies — rent, materials, PP&E (Notes-pass1 §2)
12. New ₹61.03 Cr capex deployment progress — orders placed vs quotations only (RHP p.86)
13. AS9100D / ISO9001:2015 certification renewal status, per unit (RHP p.151)
14. Section 185 / compounding-application remediation outcome (RHP p.26-27)
15. Effective tax rate (watch for further regime shifts beyond the 115BAA move, Notes-pass1 §1)

### 4D. Highest-value questions for management

1. What share of the Quick Pay relationship (47% of FY26 revenue) is the
   drone-component supply arrangement, and what happens to that stream —
   and to receivables timing — if Quick Pay's own funding or collections
   falter? *Reassuring*: diversification beyond the single bill-to-ship
   arrangement, collections now running under 90 days. *Worrying*:
   dependency deepening, or the equity stake creating pressure to keep
   booking revenue regardless of Quick Pay's own cash position.
2. Given the auditor-named Section 185 breach (FY24/FY25) and the
   14-category restatement cluster including twice-repeated premature
   revenue recognition, what specific control changes are in place ahead
   of the first post-listing results? *Reassuring*: named control owner,
   documented process, audit committee sign-off. *Worrying*: no named
   owner or timeline.
3. What is the commercial rationale and any promoter relationship for the
   ₹9 Cr slump-sale acquisition of Hindustan Springs Manufacturing Co and
   Universal Automobile and Dairy Products, and why does ₹6.94 Cr of the
   ₹9 Cr consideration remain unpaid? *Reassuring*: independent valuation,
   arm's-length sellers, integration on track. *Worrying*: undisclosed
   related-party link or financing strain.
4. With the order book (₹67.14 Cr) covering roughly 5-6 months of FY26
   revenue run-rate, what is the realistic path to sustaining ₹148.77 Cr
   of FY26 revenue into FY27? *Reassuring*: repeat-customer % rising past
   44.6%, multiple new large orders signed. *Worrying*: order book
   shrinking or repeat rate falling.
5. Rent, materials purchases, PP&E sales, and a >5% post-bonus
   shareholding all run through V3 Technologies, a promoter-controlled
   partnership firm; what independent valuation supports the ₹7.08 Cr
   FY25 PP&E purchase from V3? *Reassuring*: independent valuer report,
   competitive quotes. *Worrying*: no valuation basis exists.
6. Export revenue is recognised Ex-Factory even where risk typically
   transfers later (FOB/on acceptance) for aerospace/defence exports —
   has this created disputes or post-recognition reversals with export
   customers? *Reassuring*: no disputes, contracts confirm Ex-Factory risk
   transfer. *Worrying*: acceptance-based rejections after revenue is
   booked.
7. Annexure XLIX asserts the company "has investments in its subsidiary
   company," but only one minority-stake investment (Quick Pay, no % of
   ownership disclosed) appears in the financial statements — does
   Millworks control Quick Pay, and if so, why is it not consolidated?
   *Reassuring*: confirmed minority stake, no control. *Worrying*:
   undisclosed control relationship implying consolidation should have
   occurred.

---

## SECTION 5: ONE-PAGE BUSINESS MODEL SUMMARY CARD

| | |
|---|---|
| **Company** | Millworks Technologies Limited (MILLWORKS) |
| **Business type** | Manufacturing — Build-to-Print/Build-to-Spec precision engineering, job-order basis |
| **Archetype** | Build-to-spec component maker (customer capex cycle, design-win pipeline, content per unit, input-cost pass-through) |
| **One-line description** | Machines precision metal parts to customer drawings/specs for aerospace, defence, railways, and semiconductor OEMs |
| **Revenue streams** | Defence 69.43% (dominated by one customer, Quick Pay, at 47.02%), Railways 23.65%, Semiconductor 5.94%, Aerospace 0.99% (all RHP p.124); exports 27.47% cross-sector (RHP p.127) |
| **Revenue predictability** | Low — no long-term contracts, PO-basis only (RHP p.28), order book covers ~5-6 months of run-rate |
| **Asset intensity** | Medium — leased facilities, active ₹61 Cr capex programme not yet ordered |
| **WC intensity** | High — WC days 136→191 over FY24-26; receivable days 73→340 (year-end basis) |
| **Pricing power** | Weak — below-peer EBITDA margin, PO-negotiated, extreme customer concentration |
| **Cyclicality** | Cyclical, riding a secular growth tailwind (defence indigenisation, semiconductor localisation, rail capex) |
| **Moat strength** | Moderate (Gate0 quant score 13/60) — certification/qualification barrier is real but shared broadly; no cost, scale, network, or distribution moat |
| **Key concentration risk** | Quick Pay: top customer (47.02% revenue) + receivables counterparty whose own collections gate Millworks' cash + equity investee (₹575.06 Lakh, % undisclosed) — three risks, one name |
| **Cash conversion** | Failing: cumulative CFO/PAT = −0.29x over FY24-26 (Gate0 Block B = 0/20) |
| **Valuation approach** | Primary EV/EBITDA vs Unimech/Azad; secondary peer P/E (earnings-quality caveated); tertiary order-book coverage as a sanity check; DCF not yet usable (3-yr history, FCF negative all years) |

---

## ONE-LINE VERDICT

A fast-growing, sub-scale precision-engineering job shop whose headline
growth and margin expansion sit on top of one customer relationship that
is simultaneously its biggest revenue source, its worst receivables
problem, and a related equity investment.

```yaml
stage: B04-bizmodel
company: "MILLWORKS"
run_date: "2026-08-22"
model: claude-sonnet-5
status: complete
input_gaps:
  - no_results_pdf
  - no_rating
  - no_standalone_annual_report
  - no_shareholding_pattern
  - no_dedicated_prospectus_folder_rhp_routed
  - no_investor_presentation_reg30_only
  - no_research_notes
  - announcements_folder_empty_reg30_is_sole_action_record
  - sector_mismatch_manifest_pharma_cdmo_actual_aero_defence_precision
flags:
  - type: FLAG-CUSTOMER-CONCENTRATION
    detail: "Quick Pay Private Limited is simultaneously: top customer at 47.02% of FY26 revenue under the Defence sector line (RHP p.28, Risk Factor 3, naming 'Customer 1' as Quick Pay); the receivables counterparty whose own delayed cash receipt is explicitly blamed for part of the FY26 receivables blow-up (RHP p.90); and a strategic equity investee (5,332 shares, INR 575.06 Lakh, ownership % not disclosed, RHP Annexure XV/p.F20). A second dependency (Big Bang Boom Solutions Pvt Ltd, Chennai) sits inside the same drone-component execution chain (RHP p.130, Risk Factor 4). This single relationship threads through revenue, cash conversion, and related-party risk simultaneously."
business_type: "manufacturing"
revenue_streams:
  - {name: "Defence (dominated by single customer Quick Pay Pvt Ltd, 47.02% of total FY26 revenue)", type: "manufacturing - BTP/BTS precision components + new design/engineering services line", pct_of_revenue: 69.43, predictability: "low"}
  - {name: "Railways", type: "manufacturing - BTP/BTS precision components (brake, door, coupler, pantograph parts)", pct_of_revenue: 23.65, predictability: "medium"}
  - {name: "Semiconductor", type: "manufacturing - BTP/BTS precision fixtures and frames", pct_of_revenue: 5.94, predictability: "low"}
  - {name: "Aerospace", type: "manufacturing - BTP/BTS aero-engine components", pct_of_revenue: 0.99, predictability: "low"}
asset_intensity: "medium"
wc_intensity: "high"
pricing_power: "weak"
cyclicality: "cyclical"
moats_present:
  - {moat: "AS9100D/ISO9001:2015 multi-site quality certification (qualification barrier)", durability: "moderate - real but shared broadly across peer set (RHP p.151)"}
  - {moat: "Customer approved-vendor / switching-cost stickiness", durability: "low-moderate - program-specific, undermined by absence of long-term contracts (RHP p.28)"}
  - {moat: "Repeat-customer relationships (44.59% of customer count, FY26)", durability: "fragile - sits on top of extreme concentration, top-10 = 92.06% of revenue (RHP p.140)"}
valuation_methods:
  primary: {method: "EV/EBITDA vs named peers (Unimech Aerospace, Azad Engineering)", why: "Strips out 115BAB->115BAA tax-regime distortion, goodwill amortisation, and non-operating FX gain sitting in PBT; peer EBITDA margins (42.47%, 41.78%, RHP p.96-98) are a real comparable anchor for a capex-cycle manufacturer"}
  secondary: {method: "P/E vs peer group", why: "Market convention for this SME segment, used in the RHP's own Basis for Issue Price (peer P/E 87.87x-96.45x, RHP p.93-94); must be read only alongside EV/EBITDA given earnings-quality caveats (restatement cluster, FX gain)"}
  tertiary: {method: "Order-book coverage / revenue-visibility check", why: "Order book (INR 67.14 Cr, RHP p.129) covers only ~5.4 months of FY26 revenue run-rate; supplementary sanity check on forward-revenue assumptions feeding the primary/secondary methods, not a stand-alone valuation method"}
  not_applicable:
    - "DCF - only 3 restated years, all FCF-negative (Gate0 Block B = 0/20); no reliable multi-year forecast base yet"
    - "Asset-based/NAV/replacement cost - all 4 manufacturing units leased, not owned (RHP p.150-151)"
    - "Dividend discount - no dividend history or stated policy"
    - "Sum-of-parts - single reporting segment, self-asserted under AS-17 (Notes-pass1 section 11)"
irrelevant_ratios:
  - {ratio: "Same-period revenue growth in isolation", why: "573% FY26 growth is a near-nil-base artefact (FY24 revenue only INR 9.4 Cr) plus a single-customer step-change, not broad organic demand"}
  - {ratio: "PAT/EPS trend as standalone quality signal", why: "14-category restatement cluster includes twice-repeated premature revenue recognition (FY24 and FY25); FY26 PBT includes an INR 441.00 Lakh (8.8% of PBT) non-operating FX translation gain"}
  - {ratio: "Debt/Equity (0.21) in isolation", why: "Understates true leverage: promoter personal guarantees on secured debt grew 2.5x in FY26 alone, plus promoter real estate cross-collateralised for the entire Axis Bank exposure"}
  - {ratio: "Standard DSO benchmark vs industry norm", why: "FY26 receivables spike is substantially one counterparty (Quick Pay) whose own payment timing gates collection; blending into an industry-DSO comparison hides the concentration story"}
  - {ratio: "COGS-to-revenue ratio, single-year read", why: "FY26 includes a brand-new, zero-COGS-attributed Sale of Services line (15.5% of revenue, first year ever) that mechanically improves the blended ratio"}
must_track_metrics:
  - {metric: "Quick Pay / top-customer revenue % of quarterly sales", healthy: "single customer under 30%", red_flag: "currently 47.02%, or rising further"}
  - {metric: "Order book coverage vs trailing revenue run-rate", healthy: "9-12 months of trailing revenue", red_flag: "under 6 months (currently ~5.4 months)"}
  - {metric: "Operating cash flow / PAT (cash conversion)", healthy: "0.8x or higher", red_flag: "under 0.5x or negative (currently -0.29x cumulative FY24-26)"}
  - {metric: "EBITDA margin vs peer median", healthy: "at or above ~42% peer median", red_flag: "sustained gap below peer median or declining trend (currently 36.71%)"}
  - {metric: "MSME payable balance and unpaid MSMED-Act interest", healthy: "stable balance, interest paid current", red_flag: "both growing YoY (10x and 9x growth respectively in FY26)"}
unit_economics:
  unit: "No standardised unit in this BTP/BTS job-shop model; best proxies are revenue per installed machine-hour and revenue per employee"
  revenue_per_unit: "~INR 3,884 per installed machine-hour (14,876.70 Lakh / 383,019 hours, RHP p.131); ~INR 92.4 Lakh per employee (14,876.70 Lakh / 161 employees, RHP p.146)"
  margin_per_unit: "EBITDA margin expanded 29.55% (FY24) to 35.18% (FY25) to 36.71% (FY26) as revenue scaled, evidence of fixed-cost absorption, but this expansion has not converted to operating cash (Gate0 Block B = 0/20)"
  key_lever: "Raw material cost pass-through (steel/aluminium/titanium/brass, 51.05% of FY26 revenue) and order-book/design-win volume; labour cost is a minor lever at 5.97% of revenue"
first_deterioration_signals:
  - {risk: "Quick Pay reduces, cancels, or in-sources orders (RHP p.28 names this explicitly)", first_signal: "Order book 'Pending Amount' for Defence-sector customers (RHP p.129) or quarterly Defence-sector revenue"}
  - {risk: "No long-term contracts anywhere; any customer can walk at PO renewal", first_signal: "Repeat-customer % (RHP p.140) falling YoY"}
  - {risk: "Raw material pass-through fails amid single-supplier dependency (44.05% of purchases)", first_signal: "Cost of Material Consumed as % of revenue widening past 51%, or gross margin compression"}
  - {risk: "Working-capital-funded-by-suppliers via unpaid MSME dues is not sustainable", first_signal: "MSME payable balance and unpaid MSMED-Act interest accrual continuing to grow"}
  - {risk: "Circular receivables dependency: collection gated by Quick Pay's own cash receipt (RHP p.90)", first_signal: "Trade receivable days or the >6-month ageing bucket continuing to widen"}
  - {risk: "New INR 61.03 Cr capex not yet ordered, only quotations obtained (RHP p.86)", first_signal: "Capacity utilization % staying flat despite the stated capex objective"}
  - {risk: "Thin financial-controls maturity (Section 185 breach, 14-category restatement cluster)", first_signal: "Any recurrence of restatement items in the first post-listing annual results"}
mgmt_questions:
  - "What share of the Quick Pay relationship (47% of FY26 revenue) is the drone-component supply arrangement, and what happens to that stream and to receivables timing if Quick Pay's own funding or collections falter?"
  - "Given the auditor-named Section 185 breach and the 14-category restatement cluster including twice-repeated premature revenue recognition, what specific control changes are in place ahead of the first post-listing results?"
  - "What is the commercial rationale and any promoter relationship for the INR 9 Cr slump-sale acquisition of Hindustan Springs Manufacturing Co and Universal Automobile and Dairy Products, and why does INR 6.94 Cr of the consideration remain unpaid?"
  - "With the order book covering roughly 5-6 months of FY26 revenue run-rate, what is the realistic path to sustaining INR 148.77 Cr of FY26 revenue into FY27?"
  - "What independent valuation supports the INR 7.08 Cr FY25 PP&E purchase from V3 Technologies, a promoter-controlled partnership firm that is simultaneously landlord, supplier, lender/borrower, and >5% shareholder?"
  - "Export revenue is recognised Ex-Factory even where risk typically transfers later for aerospace/defence exports; has this created disputes or post-recognition reversals with export customers?"
  - "Annexure XLIX asserts the company has investments in a subsidiary, but only one minority-stake investment (Quick Pay, ownership % undisclosed) appears in the financials; does Millworks control Quick Pay, and if so, why is it not consolidated?"
one_line_verdict: "A fast-growing, sub-scale precision-engineering job shop whose headline growth and margin expansion sit on top of one customer relationship that is simultaneously its biggest revenue source, its worst receivables problem, and a related equity investment."
analyst_note: "The dominant fact for every downstream stage is that Quick Pay Private Limited is not just a receivables/investment overlap (as B01-gate0 flagged) but the company's largest customer outright, at 47.02% of FY26 revenue, named explicitly in RHP Risk Factor 3 (p.28) as 'Customer 1.' Combined with the Big Bang Boom Solutions execution dependency (RHP p.130), the entire Defence-sector revenue line (69.43% of FY26 total) is substantially one counterparty relationship dressed as a four-sector diversified business. Moat scoring, pricing power, and valuation method selection above all assume this concentration persists; any FTTCP or Role 1 valuation work must treat Quick Pay diversification (or its absence) as the single highest-priority verification item, ahead of the cash-conversion failure B01-gate0 already flagged."
```
