# Stage 4: Business Model Decoder — Jubilant Agri & Consumer Products Ltd (JUBLCPL)
Run date: 2026-08-18 | Model: claude-sonnet-5

Primary source: FY2025-26 Annual Report (AR), pages as printed in the PDF footer (not raw
PDF page index — there is a +3 offset between raw PDF page and printed page number in this
file; all citations below use the PRINTED page number, e.g. "AR p.19").
Secondary source: Q1 FY27 Earnings/Investor Presentation dated 11-Aug-2026 ("Inv. Pres.",
slide numbers as printed) — this is the company's most recent investor deck, but it is a
quarterly earnings deck, not a full-year investor presentation; it is used here mainly for
its historical financial and segment tables (FY24–FY26 and Q1FY27).
Tertiary, NON-ANCHORED leads only (broker notes, explicitly flagged wherever used): MNCL
Initiating Coverage report (Jan-2026) and MNCL 4QFY26 update; JUBLCPL.NS PeTechKnowledge
report. These are never used as the basis for a number in the YAML block; they only supply
named-competitor context flagged as non-anchored.

**Critical structural fact governing this entire decode**: on 04-Nov-2025 the Board approved
a Scheme of Arrangement (NCLT Allahabad Bench order dated 08-Aug-2026; shareholder/creditor
meetings scheduled 05-Sep-2026, scheme not yet effective as of this run date) to demerge the
Agri Division (P&K Fertilizers + Agri Nutrients) into a new company, Jubilant Agri Solutions
Ltd (JASL), on a 1:1 share-entitlement basis (AR p.5; Inv. Pres. slide 26). Post-demerger,
JUBLCPL retains only Performance Polymers & Chemicals (PP&C) and is expected to be renamed
Jubilant Industries Ltd. Every section below calls out RETAINED vs DEMERGING explicitly.

---

## SECTION 1: THE BUSINESS MODEL IN PLAIN ENGLISH

### 1A. One-line description

JUBLCPL today is two businesses bolted together under one listing: (1) a specialty
industrial-polymers and branded-adhesives maker that glues furniture together and helps
tyres stick to their reinforcing fabric (RETAINED, will become "Jubilant Industries Ltd"),
and (2) a commodity phosphate-fertilizer and crop-nutrient maker that sells subsidised SSP
to Indian farmers (DEMERGING into Jubilant Agri Solutions Ltd).

### 1B. Money flow chain for each revenue stream

**1. Consumer Products — Adhesives & Wood Finishes (RETAINED, brands Jivanjor, Charmwood,
Ultra Italia, Vamicol)**
[Resins, VAM and solvents, partly backward-integrated via the Jubilant Group (AR p.16)] →
[JACPL blends/formulates branded water-based adhesives and wood-finish coatings at Gajraula
and Sahibabad plants, a new adhesives line commissioned at Samlaya, Gujarat in Q1 FY27 (AR
p.25; Inv. Pres. slide 12)] → [ships to ~1,450 distributors and ~31,000 retailers/dealers
pan-India (Inv. Pres. slide 3)] → [carpenters, contractors and furniture makers buy at
retail] → [distributors pay JACPL on trade credit; end-buyers pay cash/short credit at the
point of retail sale].

**2. Latex — VP/SBR/NBR (RETAINED, brand Encord / Enbuild)**
[Butadiene, styrene, vinyl-pyridine monomer inputs] → [JACPL polymerises into synthetic
latex at the Savli (Vadodara), Gujarat plant] → [supplied in bulk to global and domestic
tyre manufacturers, tyre-cord-fabric dippers, and (new, FY26) construction-chemical/
waterproofing formulators via the new SBR line (AR p.26–27; Inv. Pres. slide 5)] → [large
industrial B2B buyers, largely under standing commercial relationships] → [invoiced on
payment terms; raw-material cost pass-through via calibrated pricing (AR p.26)].

**3. Food Polymers — Solid PVAc / SPVA gum base (RETAINED, brand Vamipol; Ester Gum under
Jubigum)**
[Vinyl acetate monomer (VAM) and ethanol, largely group-sourced] → [processed into solid
PVAc gum-base resin] → [sold in bulk, mostly export, to global chewing-gum/confectionery
majors — JACPL is India's largest and among the world's top three PVAc suppliers (AR p.3,
p.26)] → [large FMCG confectionery companies buy under long-standing contracts] → [invoiced
on trade terms].

**4. P&K Fertilizers — SSP + bulk NPK (DEMERGING, brand Ramban)**
[Rock phosphate + captive sulphuric acid + boron/zinc/magnesium micronutrients (AR p.18,
27)] → [manufactured as powdered/granulated SSP at Gajraula and Kapasan plants; company also
now trades imported bulk NPK 20:20:0:13 (AR p.20)] → [sold through a dealer/retailer network
across Uttar Pradesh, Uttarakhand, Bihar, Rajasthan and Madhya Pradesh, with new-state entry
in Gujarat, Maharashtra, Chhattisgarh, West Bengal (AR p.28)] → [farmers buy, price partly
government-subsidised under the Nutrient Based Subsidy (NBS) scheme (AR p.36)] → [farmer
pays the subsidised retail price; government pays the subsidy to the company, typically with
a collection lag that drives working capital].

**5. Agri Nutrients — biostimulants/micronutrients (DEMERGING, Bio-Poshan, Shakti Zyme,
Jubigold)**
[In-house formulation of granular/liquid biostimulants] → [sold through the same Ramban
dealer network as a complement to SSP] → [farmers buy for crop nutrition, no direct
subsidy] → [dealer credit terms; FY26 revenue and margin hit by regulatory changes to
Fertiliser Control Order (FCO) norms governing biostimulants (AR p.20)].

### 1C. Revenue model classification table (FY2025-26, consolidated, AR p.19 segment note)

| Stream | Type | Description | % of revenue (anchored) | Predictability |
|---|---|---|---|---|
| Performance Polymers & Chemicals (PP&C) — total, RETAINED | Manufacturing, hybrid B2B/B2B2C, unit sale | Adhesives/wood finishes (branded, distributor-led) + Latex + Food Polymers (industrial B2B, contract-based) | 65.5% (₹12,386mn / ₹18,911mn total segment sales before elimination; AR p.19) — note corporate-overview page rounds this to "63%" (AR p.2); a minor internal inconsistency, not resolved here | Medium |
| — of which Adhesives sub-segment (RETAINED) | Manufacturing, branded B2B2C | Distributor/dealer-led branded consumer adhesives & wood finishes | ~26.5% of consolidated revenue on Inv. Pres. figures (₹5,015mn FY26; Inv. Pres. slide 10–11) — this sub-segment split does NOT reconcile exactly to the AR's PP&C total (see flags) | Medium |
| P&K Fertilizers (SSP + bulk NPK) — DEMERGING | Manufacturing, commodity, subsidy-linked | SSP/NPK sold to farmers via dealer network, price partly subsidised by GoI | 36.0% (₹6,812mn / ₹18,911mn; AR p.19) | Low |
| Agri Nutrients — DEMERGING | Manufacturing, branded agri-input | Biostimulants/micronutrients sold via Ramban dealer network | 0.6% (₹111mn / ₹18,911mn; AR p.19) | Low |

### 1D. Simplified business model canvas

| Dimension | RETAINED (PP&C, post-demerger) | DEMERGING (Agri: P&K Fertilizers + Agri Nutrients) |
|---|---|---|
| What they sell | Branded wood adhesives/wood finishes; industrial synthetic latex; PVAc gum-base resin | Single Super Phosphate (SSP), bulk NPK, biostimulants |
| Who buys | Carpenters/contractors/furniture-makers (via distributors); tyre & tyre-cord manufacturers; global confectionery majors | Farmers (via dealer network), largely in UP, Uttarakhand, Bihar, Rajasthan, MP |
| Why them | Brand + distribution reach (Jivanjor); niche global leadership (VP Latex #1 India/#2 global ex-China; PVAc #1 India/top-3 global) (AR p.3) | #1 SSP position in Uttar Pradesh (AR p.3); Ramban brand equity; established dealer network |
| How delivered | Distributor → retailer → contractor/end-user network (~31,000 retailers); direct bulk shipment to industrial customers | Dealer network direct to farmer, seasonal around cropping cycles |
| Cost structure dominance | Raw materials (VAM, monomers, resins) — largest single cost line consolidated (Cost of Materials Consumed ₹9,164mn of ₹16,951mn total expenses, FY26; AR p.19) | Rock phosphate, sulphuric acid, imported inputs; subject to global commodity price swings (AR p.18) |
| Scarce resource | Formulation/process know-how (R&D centres, Six Sigma/Green Belt programmes; AR p.29); brand trust with contractors | Distribution reach in core agri states; SSP granulation/fortification capability |
| Pricing power source or absence | Moderate: niche global scale in Latex/PVAc allows raw-material pass-through (AR p.26); Adhesives is a "distant #2" behind a dominant branded leader in a fragmented market (AR p.16) — non-anchored broker context below | Weak/price-taker: SSP price and demand are shaped by government NBS policy and by substitute-product (DAP/NPK) pricing, not by JACPL (AR p.36) |
| Asset intensity | Medium: 4 plants, PP&E ₹1,984mn on total assets ₹9,354mn (~21%, FY26; AR p.24/Inv. Pres. slide 24); disclosed capacity 80,000 MTPA polymers & chemicals (Inv. Pres. slide 4) | Medium-heavy for SSP: disclosed capacity 400,000 MTPA (Inv. Pres. slide 4), plus captive sulphuric acid |
| WC intensity | Medium on a standalone view (industrial B2B receivables + branded-consumer dealer credit) — precise standalone WC split NOT FOUND in provided documents | High: "working capital deployment remained high" and expected to stay high in Q1 FY27 for Agri Products, driven by subsidy-receivable lags and seasonal SSP inventory build (Inv. Pres. slide 17) |
| Regulatory moat or burden | Burden-light: environmental/safety compliance (ISO 45001, EHS policy) is a cost of doing business, not a moat (AR p.29–30) | Burden-heavy: NBS subsidy scheme and Fertiliser Control Order (FCO) norms directly set economics; FY26 Agri Nutrients revenue/margin was hit by an FCO norm change on biostimulants (AR p.20) |

### 1E. The chai-stall-uncle version

Imagine a chaiwala who also sells kites in mango season. The tea stall (adhesives, latex,
gum-base) is the steady business — people always need wood glue for furniture and tyre
factories always need latex, so that side runs every day, rain or shine, and the chaiwala
has built a bit of a name for his chai (the Jivanjor brand). The kite stand (SSP fertilizer)
only really moves when the monsoon behaves and the government's kite-subsidy scheme pays out
on time — some years it's a windfall, some years the kites just sit there. The family has now
decided to split the two stalls into separate shops so customers (and investors) can judge
each on its own terms, instead of one messy combined till. The tea stall is being kept and
renamed; the kite stand is being spun out to a cousin's shop next door.

### Section 1 summary table

| Attribute | Consolidated (current) | RETAINED (PP&C, post-demerger) |
|---|---|---|
| Business type | Manufacturing, hybrid (specialty B2B + branded B2B2C + agri-commodity) | Manufacturing, hybrid (specialty B2B + branded B2B2C) |
| Revenue nature | Mixed: contract-based industrial + distributor-led branded + subsidy-linked commodity | Contract-based industrial + distributor-led branded consumer |
| Asset intensity | Medium (PP&E/total assets ~21%, FY26) | Medium (component-level PP&E split by segment NOT FOUND) |
| WC intensity | High, pulled up by Agri (subsidy receivables + seasonal inventory) | Medium (standalone figure NOT FOUND; industrial + distributor-credit model typically lighter than subsidised-commodity agri) |
| Pricing power | Blended: moderate in polymers/adhesives, weak/price-taker in SSP | Moderate (niche global leadership in Latex/PVAc; distant #2 challenger in Adhesives) |

---

## SECTION 2: INDUSTRY DYNAMICS & COMPETITIVE POSITION

### 2A. Five forces, plainly

| Force | Assessment | Helps / Hurts / Neutral |
|---|---|---|
| Competition (rivalry) | Adhesives: AR itself says "local competition remains fragmented, but branded regional players like JACPL benefit particularly from quality perception and strong distribution networks" (AR p.16). Non-anchored broker context (MNCL, flagged NOT primary evidence): JACPL is described as the "2nd branded wood adhesives company in India by revenue," with a dominant market leader (~70% share per broker estimate) well ahead of it, and other named challengers Astral and Jyoti Resins. Latex/Food Polymers: AR states JACPL is India's #1 (VP Latex) and #1/top-3 globally (PVAc), with "intense competition from cost-competitive manufacturers in China and Europe" in Food Polymers/Latex (AR p.35). | Hurts in Adhesives (challenger position vs an entrenched leader); Helps in Latex/PVAc (scale leadership, though against low-cost Asian/European rivals) |
| Entry barriers | Formulation/process know-how carried from the group's chemicals heritage (AR/broker note both cite decades of in-house R&D); distribution network build-out (~31,000 retailers) takes years to replicate; SSP requires licensed fertiliser manufacturing capacity and NBS registration | Helps (moderate barriers in adhesives/latex; regulatory barrier in fertiliser) |
| Supplier power | Key inputs (VAM, monomers, resins, rock phosphate, sulphuric acid) are internationally-linked commodities; AR explicitly notes "JACPL's backward integration in raw materials (through the Jubilant Group) provides a cost advantage against global price swings" (AR p.16), and captive sulphuric acid supports SSP integration (AR p.18) | Helps (partial captive/group backward integration blunts supplier power) |
| Customer power / concentration | Adhesives: power is diffuse (thousands of dealers/contractors) but AR flags "a handful of customers account for a majority share of the market" for Food Polymers/Latex customer base (AR p.37) — concentrated global confectionery/tyre customers | Neutral in Adhesives; Hurts in Food Polymers/Latex (customer concentration risk named explicitly in AR risk section) |
| Substitutes | SSP faces "intense competition from substitute products such as DAP and NPK complexes" (AR p.36); Adhesives faces no named direct substitute threat in the provided documents (NOT FOUND) | Hurts (SSP only) |

### 2B. Competitive positioning map vs named competitors

AR text does not name specific competitor companies (it only describes competitive dynamics
qualitatively). The following named competitors are NON-ANCHORED broker-report leads (MNCL
Initiating Coverage, Jan-2026) — provided for context only, not to be treated as evidence:

| Business | Named comps (non-anchored, broker only) | Broker-cited positioning |
|---|---|---|
| Adhesives | Pidilite Industries (Fevicol) — market leader, ~70% share per broker estimate; Astral Ltd; Jyoti Resins | JACPL/Jivanjor positioned as fastest-growing challenger, far smaller scale (broker-estimated ~80,000 MTPA adhesive capacity vs Pidilite's 600,000+ MTPA) |
| Food Polymers | Mangalam Organics | Not detailed in provided docs |
| Latex | Apcotex India, BSF India | Not detailed in provided docs |
| Agri (SSP/fertiliser) | Coromandel International, Chambal Fertilizers, Khaitan | Not detailed in provided docs |

### 2C. Moat assessment (eight standard types)

| Moat type | Present? | Evidence | Durability |
|---|---|---|---|
| Brand | Yes, partial | Jivanjor/Charmwood/Ultra Italia named as "top-tier consumer brands" in adhesives/wood finishes (AR p.3); Ramban "well-regarded" in core agri states (AR p.3) | Medium — regional/challenger brand strength, not category-defining like the (non-anchored) named leader |
| Switching costs | Yes, partial | Latex/PVAc: "entrenched customer relationships," "long-standing contracts with leading confectionery companies" (AR p.16, p.26) | Medium — industrial B2B relationships are sticky but not contractually locked (no long-term take-or-pay disclosed) |
| Network effects | No | Not applicable to this business type | n/a |
| Cost advantage / scale | Yes, partial | Backward integration in raw materials via Jubilant Group (AR p.16); captive sulphuric acid integration benefit for SSP (AR p.18) | Medium — group-dependent, not a standalone structural cost edge |
| Intangible assets (IP/formulation) | Yes, partial | In-house R&D/Technology Centres, "specialised PVAc grades," continuous formulation innovation (AR p.16, p.29) | Medium — no patents or exclusive IP disclosed in provided pages (NOT FOUND) |
| Efficient scale | Yes, in niche global segments | #1 India / #2 global-ex-China in VP Latex; #1 India / top-3 global in PVAc solid form (AR p.3) — niche markets too small to attract many large-scale entrants | Medium-High in Latex/PVAc; Low in Adhesives (large addressable market with a dominant incumbent) |
| Regulatory / license moat | No (SSP is a burden, not a moat) | SSP economics are subsidy-and-FCO-norm dependent (AR p.20, p.36) — this is a regulatory *exposure*, not a moat | n/a (demerging anyway) |
| Distribution moat | Yes, partial | ~1,450 distributors / ~31,000 retailers pan-India (Inv. Pres. slide 3); dealer loyalty programmes, DMS Tool, Dealer App, Influencer Loyalty Apps (AR p.37) | Medium — built over "2 decades" (Inv. Pres. slide 2) but replicable with capital and time |

### 2D. Industry lifecycle stage and JACPL's position

- Indian wood adhesives/wood-finishes market: growing steadily, adhesives market projected
  to grow from USD 3.07bn (2025) to USD 4.58bn by 2031 (6.9% CAGR, AR p.15) — **growth
  stage**; JACPL is a scaling challenger gaining share off a small base.
- Global VP/synthetic latex market: growing ~3.0-4.0% CAGR to 2031 (AR p.16) — **mature,
  low-growth stage**; JACPL is an established #1/#2 leader defending share.
- Global chewing-gum/PVAc market: "mature market in many countries," 3-4% CAGR forecast (AR
  p.17) — **mature stage**; JACPL is an established top-3 global supplier.
- Indian SSP/fertiliser market: policy-driven, subsidy-dependent, structurally volatile
  (broker note, non-anchored, describes the Agri business as "cyclical" and "structurally
  volatile") — **mature, policy-cyclical stage**; JACPL is a regional (UP-centric) #1 player
  now being carved out.

### 2E. Key industry drivers

| Driver | Direction | Impact on JACPL |
|---|---|---|
| Indian housing/construction and furniture demand (PMAY, urbanisation) | Positive | Adhesives/wood-finishes volume growth (AR p.16) |
| Automotive/tyre replacement-market growth | Positive (OEM demand "may remain muted" FY26-27, but replacement/export tyre demand "expected to continue growth trajectory," AR p.26) | Mixed — supports Latex demand on replacement side, softens on OEM side |
| Global chewing-gum market shift to sugar-free/functional gums | Positive (albeit off a smaller base) | Supports Food Polymers demand mix (AR p.17) |
| Government fertiliser subsidy (NBS) policy and FCO regulatory norms | Uncertain/negative in FY26 (FCO norm change hit Agri Nutrients, AR p.20) | Direct hit to the demerging Agri segment; a key reason for the demerger itself |
| Raw-material/input-cost volatility (VAM, butadiene, rock phosphate, freight) tied to global geopolitics (Red Sea, Middle East conflict) | Negative | Margin pressure across all segments; company cites "proactive pricing actions" as the main mitigant (Inv. Pres. slide 9, 12) |

---

## SECTION 3: FINANCIAL METRICS THAT MATTER FOR THIS BUSINESS MODEL

### 3A. Ignore-these-track-these

| Commonly tracked ratio | Misleading/Irrelevant here? | Why |
|---|---|---|
| Consolidated gross margin (single blended number) | Misleading | Blends a subsidy-linked commodity business (SSP) with a branded/industrial polymer business; margins move for entirely different reasons in each — track segment-level EBIT margin instead (AR p.19 gives this split) |
| Consolidated ROCE (until demerger completes) | Misleading, temporarily | Includes capital tied up in the Agri business, which is about to leave the balance sheet; post-demerger ROCE will reset on a smaller, different capital base |
| Same-store/like-for-like sales | Irrelevant | Not a retail business; JACPL sells through distributors/dealers, not owned stores |
| Days-of-inventory as a single blended figure | Misleading | SSP inventory is seasonal/monsoon-driven (built ahead of Kharif/Rabi cycles) while adhesives/latex inventory reflects normal industrial turnover; blending hides the seasonality (Inv. Pres. slide 17 explicitly flags "working capital deployment remained high" for Agri alone) |
| Consolidated EPS trend as a valuation anchor | Misleading, temporarily | EPS FY26 ₹84.49 (AR p.7) mixes the two businesses; the demerger will mechanically split this EPS base — pre/post-demerger EPS is not comparable |

### 3B. Must-track metrics

**Growth**

| Metric | What it tells you | Healthy range | Where to find it | Red flag threshold |
|---|---|---|---|---|
| Segment-wise revenue growth (PP&C vs P&K Fertilizers vs Agri Nutrients) | Which engine is actually driving the consolidated 21% FY26 growth (AR p.19) | Adhesives double-digit (AR describes "strong double-digit revenue growth," p.25); Latex/Food Polymers low-single-digit given "softer demand" (AR p.20) | AR segment note (p.19); Inv. Pres. segment slides | PP&C revenue growth turning negative, or Adhesives growth decelerating into single digits |
| Adhesives sub-segment revenue growth | Read-through on the company's own stated core growth engine | Broker (non-anchored) cites a historical ~35% 5-yr CAGR; company itself does not disclose a target rate (NOT FOUND) | Inv. Pres. slide 10 | Growth falling meaningfully below reported historical run-rate |

**Profitability and efficiency**

| Metric | What it tells you | Healthy range | Where to find it | Red flag threshold |
|---|---|---|---|---|
| Segment EBIT margin, PP&C | Core retained-business profitability trend | FY26: 1,663/12,386 = 13.4% (AR p.19) | AR segment note | Sustained decline below FY25 level (1,650/9,704 = 17.0%, AR p.19) — note FY26 margin is already lower than FY25 on these AR figures, worth monitoring closely |
| Segment EBIT margin, P&K Fertilizers (until demerger) | Whether the "improved realisations" story (AR p.20) is holding | FY26: 462/6,812 = 6.8% vs FY25: (110)/4,415 = negative (AR p.19) — a genuine swing to profitability | AR segment note | Reversion to negative segment EBIT, as seen in FY25 |
| Consolidated EBITDA margin | Overall operating efficiency | FY26: 10.36% per Financial Highlights chart (AR p.6), vs 9.33% FY25 — improving trend | AR p.6 chart; note AR's own Key Financial Ratios table (p.20) shows "Operating Profit Margin 0.09" for FY26, an apparent internal rounding/labeling inconsistency versus the 10.36% chart — flagged, not resolved | Margin decline of >150bps YoY |
| Interest coverage ratio | Balance-sheet cushion | FY26: 23.91x (AR p.7), sharply up from 8.93x FY25 and 3.55x FY24 | AR p.7 chart | Below 5x |

**Balance sheet and risk**

| Metric | What it tells you | Healthy range | Where to find it | Red flag threshold |
|---|---|---|---| ---|
| Net debt/equity | Leverage, especially important pre/post demerger capital split | FY26: 0.06 (AR p.7), down from 0.17 FY25 and 0.61 FY24 — a genuinely deleveraging balance sheet | AR p.7 chart; Inv. Pres. slide 25 | Above 0.5x |
| Net working capital / revenue | Cash tied up in the business, esp. Agri subsidy receivables | Calculated: (Trade receivables 4,088 + Inventories 2,147 − Trade payables 2,117) / Revenue 18,911 = ~21.8% FY26 (AR p.24/Inv. Pres. slide 24; author calculation, not company-disclosed) | AR balance sheet (p.24-equivalent in Inv. Pres. slide 24) | NWC/revenue rising materially post-demerger despite Agri (the higher-WC business) leaving — would suggest WC discipline is deteriorating in the retained business |
| Trade receivable days (Debtors turnover) | Collection discipline, esp. government subsidy timing risk | FY26: 5.28x turnover ≈ 69 days (AR p.20) | AR Key Financial Ratios table | Turnover falling below ~4.5x (>80 days) |

### 3C. Industry-specific non-financial KPIs

| KPI | Relevance | Where to find it |
|---|---|---|
| Distributor/dealer/retailer count | Distribution moat proxy for Adhesives | Inv. Pres. slide 3 (~1,450 distributors, ~31,000 retailers, FY26) |
| Manufacturing capacity utilisation (Polymers 80,000 MTPA; SSP 400,000 MTPA) | Operating leverage headroom | Inv. Pres. slide 4 — utilisation % itself NOT FOUND in provided documents |
| Export revenue % of total | Currency/geopolitical exposure (Red Sea, Middle East disruptions cited, AR p.31) | Inv. Pres. slide 3 (15% export / 85% domestic, FY26); AR p.2 (15% of revenue from exports, ~consistent) |
| EcoVadis sustainability scores (Gajraula 64/100, Savli 60/100) | ESG/vendor-qualification signal, relevant to global tyre/confectionery customers | AR p.9 |
| New states entered (Agri) | Distribution expansion for the demerging business | AR p.15/28 ("entered 8 new states in last 2 years," Inv. Pres. slide 15) |

### 3D. Unit economics — the physics of the business

Given business-line diversity, the company does not disclose a single consistent "unit"
(volumes in MT/kg are NOT FOUND in any of the provided documents — only value (₹mn) and
installed capacity (MTPA) are disclosed). The physics can only be described qualitatively
here; precise revenue/cost-per-unit figures are NOT FOUND.

| Element | RETAINED (PP&C) | DEMERGING (Agri) |
|---|---|---|
| Natural unit | 1 kg of adhesive/latex/PVAc sold (volume NOT FOUND — only ₹mn revenue disclosed) | 1 tonne of SSP (volume NOT FOUND — only ₹mn revenue and MTPA capacity disclosed) |
| Revenue per unit | NOT FOUND (no per-kg realisation disclosed) | NOT FOUND (no per-tonne realisation disclosed) |
| Volume drivers | Housing/construction cycle (adhesives); tyre replacement/OEM cycle (latex); global gum-base demand (Food Polymers) | Monsoon quality, cropping intensity, farmer subsidy awareness, new-state dealer expansion |
| Price drivers | Raw-material pass-through via "proactive pricing actions" (Inv. Pres. slide 9, 12); brand premium in Adhesives | NBS subsidy rate set by government; DAP/NPK substitute pricing |
| Cost drivers | VAM, monomers, resins, freight/logistics (Red Sea disruption cited, AR p.31) | Rock phosphate, sulphuric acid, freight, railway-wagon availability (AR p.36) |
| Incremental margin / operating leverage | Adhesives EBIT grew 40% YoY on 19% revenue growth in Q1 FY27 (Inv. Pres. slide 11) — a favourable, above-1x incremental margin signal for one quarter | P&K Fertilizers swung from segment loss (FY25: -₹110mn EBIT) to profit (FY26: ₹462mn EBIT) on a 54% revenue jump (AR p.20) — high operating leverage, but off a low/negative base, so durability is unproven |

---

## SECTION 4: RISKS, VALUATION APPROACH & MONITORING

### 4A. Business-model-specific risks

| Category | Risk | First financial line item that would deteriorate |
|---|---|---|
| Revenue model | Adhesives growth deceleration as it scales against an entrenched leader (non-anchored broker framing; company itself cites "increasingly competitive market environment," AR p.25) | Adhesives sub-segment revenue growth rate (Inv. Pres. segment slide) |
| Revenue model | SSP demand/subsidy-timing volatility (monsoon, NBS scheme) — mechanically leaving the listed entity via demerger, but a real risk until the scheme is effective | P&K Fertilizers segment revenue (AR p.19) |
| Margin | Raw-material inflation (VAM, butadiene, rock phosphate, freight) outpacing pricing action | Segment EBIT margin, PP&C and P&K Fertilizers (AR p.19) |
| Margin | Regulatory/FCO norm changes hitting Agri Nutrients margins again (already happened FY26, AR p.20) | Agri Nutrients segment EBIT (AR p.19) — again, demerging away |
| Balance sheet | Working capital deployment in Agri staying "high" per company's own Q1 FY27 outlook, straining group cash before demerger completes (Inv. Pres. slide 17) | Trade receivables / net working capital (AR balance sheet) |
| Execution | Demerger execution risk — scheme not yet effective as of this run date (NCLT order 08-Aug-2026, shareholder/creditor meetings scheduled 05-Sep-2026); any delay or objection prolongs the "combined entity" valuation overhang | Timeline disclosures in subsequent stock-exchange filings (not a P&L line item) |
| Execution | New capacity (SBR Latex, Phase-2, targeted end-Q3 FY27) ramp-up risk (Inv. Pres. slide 5) | Latex segment revenue/utilisation post-commissioning |
| Structural | Customer concentration in Food Polymers/Latex — "a handful of customers account for a majority share of the market" (AR p.37) | Segment revenue volatility if any single large customer is lost (not separately disclosed) |
| Structural | No FX hedging despite import exposure — "does not use derivative financial instruments" (AR p.36) | Other expenses / forex loss line in P&L (not separately broken out in provided pages, NOT FOUND) |

### 4B. Valuation method applicability (handoff to Role 1 valuation stage)

| Method | Applicable? | Notes |
|---|---|---|
| DCF | Applicable, secondary use | Workable once segment cash flows can be modelled separately post-demerger; pre-demerger DCF must model the demerger cash/share adjustment explicitly |
| P/E | Applicable, tertiary | Only cleanly applicable post-demerger, once the retained PP&C entity has a standalone, comparable earnings base; pre-demerger consolidated P/E (EPS ₹84.49 FY26, AR p.7) is not comparable to a post-demerger peer set |
| EV/EBITDA | **Applicable, PRIMARY (segment-level cross-check)** | Segment EBIT/EBITDA is disclosed (AR p.19), enabling a sum-of-the-parts EV/EBITDA build using appropriate peer multiples for (a) branded adhesives, (b) industrial latex/food polymers, (c) commodity SSP/fertiliser — each segment has a structurally different appropriate multiple |
| SOTP (Sum-of-the-Parts) | **PRIMARY overall method while the demerger is pending** | The company is explicitly and imminently splitting into two listed entities with very different economics (branded/industrial polymers vs subsidy-linked commodity fertiliser); valuing the combined entity as one blended multiple would misprice both halves. Note: exit multiple selection must follow Section 1B v3.3 exclusively per pipeline rules — no multiple is proposed here |
| EV/Sales | Applicable, secondary for the Agri/SSP piece specifically | Useful cross-check for a low/volatile-margin commodity business where EBIT swings between profit and loss (FY25 P&K Fertilizers EBIT was negative, AR p.19) |
| P/B or NAV/Replacement cost | Not applicable | No replacement-cost or asset-revaluation data disclosed in provided documents (NOT FOUND); not a holding company |
| Dividend Discount Model | Not applicable | Dividend policy/history NOT FOUND in provided documents |

**PRIMARY**: SOTP (sum-of-the-parts), cross-checked segment-by-segment with EV/EBITDA.
**SECONDARY**: EV/EBITDA (segment-level).
**TERTIARY**: P/E, applicable only post-demerger completion on the standalone retained
(PP&C) entity.
**Cycle stage that matters for valuation**: mid-cycle for Adhesives (growth-stage,
challenger gaining share); mature/steady-state for Latex and Food Polymers; policy-cycle
trough-to-recovery for P&K Fertilizers (FY25 segment loss to FY26 segment profit, AR p.19) —
this last point matters less going forward since the segment is demerging out.

### 4C. Quarterly monitoring checklist (10-15 items)

1. PP&C segment revenue growth (AR/quarterly results segment note) — good: sustained
   double-digit; trouble: deceleration into single digits.
2. Adhesives sub-segment revenue and EBIT margin (Inv. Pres. segment slides) — good: margin
   expansion continuing (FY26: 459/5,015 = 9.2% vs implied prior years lower, Inv. Pres.
   slide 10); trouble: margin compression despite revenue growth.
3. Latex + Food Polymers combined EBIT margin — good: stable/improving pass-through; trouble:
   margin erosion from raw-material inflation outpacing price hikes.
4. P&K Fertilizers segment EBIT (while still consolidated) — good: sustained positive
   territory; trouble: reversion to loss as seen FY25 (AR p.19).
5. Demerger scheme milestones (NCLT approval status, shareholder/creditor meeting outcome
   scheduled 05-Sep-2026, effective/record date) — good: on-track/no objections; trouble:
   delays, litigation, or creditor objections.
6. Net working capital / revenue, consolidated and (once disclosed) segment-level — good:
   stable or declining; trouble: rising materially.
7. Net debt/equity — good: staying near FY26's 0.06 (AR p.7); trouble: re-leveraging above
   ~0.3-0.5x.
8. Interest coverage ratio — good: staying well above 10x (FY26: 23.91x, AR p.7); trouble:
   falling below 5x.
9. New SBR Latex capacity commissioning (targeted end-Q3 FY27, Inv. Pres. slide 5) — good:
   on schedule and ramping utilisation; trouble: delay or weak initial uptake.
10. Export revenue % and geopolitical/logistics commentary (Red Sea, Middle East) — good:
    stable ~15% (AR p.2); trouble: further logistics disruption compressing export
    profitability.
11. Distributor/retailer count growth (Inv. Pres. slide 3) — good: continued expansion;
    trouble: stagnation, signalling distribution-moat erosion.
12. Regulatory/FCO norm changes affecting Agri Nutrients (relevant until demerger effective)
    — good: no further adverse changes; trouble: repeat of FY26's negative impact (AR p.20).
13. Raw-material price trend commentary in quarterly outlook sections (VAM, butadiene, rock
    phosphate) — good: management confirms successful pass-through; trouble: management
    flags margin pressure it cannot offset.
14. EBITDA margin, consolidated — good: continuing the FY24→FY26 uptrend (8.55% → 9.33% →
    10.36%, AR p.6); trouble: reversal.

### 4D. Highest-value questions for management

1. **The AR's segment note (p.19) implies PP&C revenue grew ~27.6% YoY in FY26 (₹12,386mn
   vs ₹9,704mn), but the MD&A narrative text on the very next page states the segment grew
   "10%" YoY (AR p.20) — which figure is correct, and why do the Investor Presentation's own
   historical charts (₹11,988mn FY26 vs ₹11,042mn FY25) show yet a third set of numbers for
   the same "PP&C segment revenue" line?**
   Reassuring answer: a clear, specific reconciliation (e.g., gross-vs-net-of-inter-segment,
   or a reclassification between periods) that ties all three disclosures together.
   Worrying answer: vague/no reconciliation, or an admission that the two internal reporting
   systems (statutory segment note vs investor-facing MIS) are not kept consistent.
2. **What is the expected effective/listing date for Jubilant Agri Solutions Ltd, and what
   happens to consolidated FY26/Q1 FY27 comparatives once the scheme is effective?**
   Reassuring: a firm date within the disclosed NCLT process timeline with no pending
   objections. Worrying: open-ended timeline or unresolved creditor/shareholder objections.
3. **What was actual SSP/NPK sales volume (tonnes) in FY26, and what is capacity
   utilisation across the 400,000 MTPA SSP and 80,000 MTPA polymers capacity?**
   Reassuring: utilisation trending up with clear volume disclosure. Worrying: refusal to
   disclose volumes, or utilisation revealed to be structurally low.
4. **Beyond the group's broad backward-integration claim (AR p.16), what specific share of
   PP&C raw material is actually sourced captively from the Jubilant Group, and on what
   pricing terms (arm's length vs related-party pricing)?**
   Reassuring: clear, arm's-length-priced, meaningful captive share. Worrying: opaque
   related-party pricing that could mask true segment profitability.
5. **What is management's target margin/growth trajectory for Adhesives specifically, now
   that it is being called out as the "core long-term growth engine"?**
   Reassuring: a specific, credible multi-year target consistent with the brownfield capacity
   being added. Worrying: no target, or a target inconsistent with the scale of capex
   sanctioned (₹50 Cr brownfield, Inv. Pres. slide 5).
6. **Why did Agri Nutrients revenue and margin fall so much more than P&K Fertilizers
   recovered on a net basis in FY26, given both are attributed to the same regulatory/agri
   environment (AR p.20)?**
   Reassuring: a specific, product-level explanation (e.g., biostimulant SKUs pulled from
   sale pending re-registration). Worrying: an inability to explain the FCO impact
   concretely.
7. **Does the company hedge any of its import/export currency exposure given it explicitly
   states it uses no derivative instruments (AR p.36), and how large is the net unhedged
   exposure?**
   Reassuring: exposure quantified and shown to be genuinely small. Worrying: unwillingness
   to quantify, given rupee volatility risk flagged in the AR itself.

---

## SECTION 5: ONE-PAGE BUSINESS MODEL SUMMARY CARD

```
┌─────────────────────────────────────────────────────────────────────────┐
│ COMPANY: Jubilant Agri and Consumer Products Ltd (JUBLCPL)               │
│ ONE-LINE: Specialty adhesives/latex/gum-base polymer maker (retained,    │
│  soon "Jubilant Industries Ltd") currently bolted to a commodity SSP     │
│  fertiliser business (demerging into Jubilant Agri Solutions Ltd)        │
├─────────────────────────────────────────────────────────────────────────┤
│ BUSINESS TYPE: Manufacturing, hybrid (specialty industrial B2B + branded │
│  B2B2C consumer adhesives + subsidy-linked agri-commodity, the last of   │
│  which is demerging out)                                                 │
│ REVENUE STREAMS: PP&C 65.5% (AR p.19) [Adhesives sub-segment ~26.5% of   │
│  consol per Inv. Pres., not fully reconciled to AR total — flagged];    │
│  P&K Fertilizers 36.0%; Agri Nutrients 0.6% (AR p.19)                   │
│ ASSET INTENSITY: Medium (PP&E/total assets ~21%, FY26; AR)              │
│ WC INTENSITY: High consolidated (Agri-driven); Medium expected for      │
│  retained PP&C entity (qualitative, standalone figure NOT FOUND)        │
│ PRICING POWER: Moderate — niche global leadership in Latex/PVAc allows  │
│  raw-material pass-through; challenger position in Adhesives; price-    │
│  taker in SSP (demerging)                                               │
│ CYCLICALITY: Cyclical — tied to auto/tyre cycle, housing/construction   │
│  cycle, and (until demerger) the monsoon/subsidy cycle                  │
│ MOATS: Distribution (medium), Brand (medium, challenger-tier),          │
│  Switching costs/customer relationships (medium), Cost advantage via    │
│  group backward integration (medium), Efficient scale in Latex/PVAc     │
│  niches (medium-high) — no network-effect or true regulatory moat       │
│ PRIMARY VALUATION METHOD: SOTP, given the imminent demerger; segment-   │
│  level EV/EBITDA as the core cross-check                                │
│ #1 RISK TO WATCH: Demerger execution timing risk + the unreconciled     │
│  PP&C segment-revenue growth figures across AR text/AR table/Inv. Pres. │
│  (10% vs 27.6% vs a third IP-based growth rate — flagged, not resolved) │
│ ONE-LINE VERDICT: A genuinely differentiated niche-polymer/branded-     │
│  adhesives business is currently obscured inside a subsidy-exposed      │
│  fertiliser business; the demerger, once effective, should make the     │
│  retained entity's economics legible for the first time                 │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Input gaps and data-quality flags

- Investor presentation provided is a **Q1 FY27 earnings deck** (dated 11-Aug-2026), not a
  standalone FY26 annual investor presentation; used here for historical FY24-FY26 and
  Q1FY27 tables, which it does provide.
- **Material internal inconsistency**: PP&C segment revenue growth for FY26 is stated as
  "10%" in AR MD&A narrative text (p.20), while the AR's own segment note table (p.19)
  implies ~27.6% YoY growth (₹12,386mn vs ₹9,704mn), and the Investor Presentation's own
  historical chart shows a third, different set of PP&C segment revenue figures (₹11,988mn
  FY26 vs ₹11,042mn FY25, Inv. Pres. slide 7) that also do not tie to either AR figure. This
  is flagged for downstream numeric-verification stages; not resolved in this report.
- Corporate Overview page (AR p.2) rounds PP&C/Agri revenue split to "63%/37%," a minor
  rounding difference vs the segment note's precise 65.5%/34.5% (AR p.19).
- Sales volumes (MT/kg/tonnes) for any product line are NOT FOUND in the provided documents
  — only value (₹mn) and installed capacity (MTPA) are disclosed, so true unit economics
  (revenue/cost per unit) could not be computed and are marked NOT FOUND throughout.
- Dividend policy/history: NOT FOUND in the provided pages.
- Named competitors and market-share estimates (Pidilite ~70% share, Astral, Jyoti Resins,
  Mangalam Organics, Apcotex India, BSF India, Coromandel International, Chambal
  Fertilizers, Khaitan) are NON-ANCHORED broker-report leads (MNCL Initiating Coverage,
  Jan-2026) and are explicitly excluded from the YAML block's anchored fields.
- Demerger scheme is **not yet effective** as of this run date (2026-08-18): NCLT order
  dated 08-Aug-2026; shareholder/creditor meetings scheduled 05-Sep-2026. All "RETAINED vs
  DEMERGING" framing in this report describes the intended post-scheme structure, not the
  current legal structure.
```

