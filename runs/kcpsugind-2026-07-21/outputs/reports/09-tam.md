# Stage 9 — TAM / SAM / SOM Market Sizing
## K.C.P. Sugar and Industries Corporation Ltd (KCPSUGIND) — run 2026-07-21

Status: **partial** (one primary-source fetch failed; substituted with secondary
sources — see Section 2 and search log). All other core estimates are
multi-sourced and triangulated.

---

## SECTION 1: MARKET DEFINITION

### 1A — Precise boundaries

KCP is not a single-market company; B04 (Sum-of-the-parts valuation_primary)
and the FY26 filed segment table confirm four economically distinct
addressable markets. Each is scoped separately below; TAM/SAM/SOM in
Sections 2-3 are built as a sum-of-parts, consistent with B04.

**Important correction to injected inputs:** B04's revenue-stream percentages
(Sugar 56.7%, Urad Dal 20.2%, Engineering 6.1%, ...) reconcile to the
**standalone** entity (FY25 CARE figures). The FY26 Audited Results cache
(consolidated segment note, `FY26_Audited_Results.txt` p.4) shows Engineering
— which consolidates **The EIMCO-K.C.P. Limited**, the wholly-owned
subsidiary — at **Rs 78.64 Cr, 26.3% of gross segment revenue** in FY26, not
6.1%. This stage uses the filing-anchored consolidated FY26 segment table as
the revenue-mix source of record (source: FY26_Audited_Results.txt, p.4,
"AUDITED STANDALONE AND CONSOLIDATED REPORTING OF SEGMENT WISE REVENUE"),
flagged for reconciliation against B04 at synthesis.

FY26 consolidated segment revenue (source: FY26_Audited_Results.txt p.4,
gross segment revenue before inter-segment elimination, year ended
31.03.2026): Sugar Rs 141.55 Cr, Engineering Rs 78.64 Cr, "Others" (Urad Dal,
by cross-check against CARE's 20.2%-of-TOI FY25 figure) Rs 44.95 Cr,
Power & Fuel Rs 19.70 Cr, Chemicals (calcium lactate, CO2, bio-fertiliser)
Rs 13.84 Cr. Gross segment total Rs 298.88 Cr; net of Rs 38.94 Cr
inter-segment revenue = Rs 259.95 Cr, matching the injected REVENUE_CR
anchor.

**Segment 1 — Sugar** (54.5% of FY26 net revenue)
- Product: raw/plantation white sugar, a nationally fungible commodity traded
  on uniform ex-mill/mandi pricing (not a differentiated or branded product).
- Geography: India domestic only (sugar exports are government-quota gated;
  no evidence of KCP export sugar volumes in the cache).
- Customer/channel: bulk wholesale and institutional trade, government PDS
  allocations where applicable; no retail-branded presence.
- Exclusions: khandsari/gur (unorganised cane-to-jaggery conversion,
  ~15-20% of national cane diversion by various trade estimates) is a
  different product and excluded from TAM.

**Segment 2 — Ethanol / industrial & anhydrous alcohol** (~4% of FY25
turnover per AR; FY26 not separately broken out in the segment table, folded
into Sugar/Power segments)
- Product: ethanol for the government's Ethanol Blending Programme (EBP,
  cane-juice/molasses-based only — KCP has no grain-based ethanol capacity).
- Geography: India, OMC (oil marketing company) procurement nationally.
- Exclusions: grain-based (maize/rice) ethanol, which is ~66% of India's
  EBP feedstock (ChiniMandi, Sep-2025 data) and structurally outside KCP's
  cane/molasses-only production capability.

**Segment 3 — Urad Dal (black gram) processing** (17.3% of FY26 gross
segment revenue)
- Product: processed black gram (Urad Dal), a differentiated pulse product,
  not a raw commodity in the same sense as sugar.
- Geography: sourced from the Krishna Delta (contributes ~30% of Andhra
  Pradesh's black gram production per CARE), sold via bulk/institutional
  trade channels, not organised branded retail.
- Capacity: 22,000 MTPA processing capacity, commissioned Feb 2023 (CARE,
  p.2).

**Segment 4 — Engineering (Eimco-KCP: clarifiers, thickeners, filtration
process equipment)** (26.3% of FY26 gross segment revenue)
- Product: liquid-solid separation process equipment (reactor clarifiers,
  thickeners, vacuum filters, dosing systems) for mineral processing,
  chemical processing, power/FGD, pulp & paper, and municipal/industrial
  water & wastewater treatment.
- Geography: India-primary with selective international EPC-subcontract
  wins (the operator-relayed Hyundai/Saudi order is one data point; company
  claims 25,000+ installations worldwide historically, per web search of
  Eimco-KCP's own marketing material — not filing-verified).
- Channel: sold as capital equipment to EPC contractors and industrial end
  users, not a consumer-facing business.

### 1B — Management's own TAM claim

**NOT FOUND — no quantified TAM figure anywhere in the AR MD&A or the CARE
rating.** The AR's "Industry Structure and Developments" and "Opportunities
and Threats" sections (Annual_Report.txt pp.35-36, MD&A dated 13/08/2025)
give only qualitative language: "The long term outlook for Sugar Industry
remains positive and promising," citing ethanol demand, cogeneration, and
bio-composting as opportunities, with no market-size number, no timeframe,
and no addressable-market definition. Credibility read: **vague** — not
assessable against a conservative estimate because there is nothing to
compare. `mgmt_claim_cr`, `mgmt_claim_ratio` are NOT FOUND, not zero.

---

## SECTION 2: TAM ESTIMATION, MULTIPLE METHODS

### Segment 1 — Sugar

**Method 1 — top-down (industry report), flagged as scope-mismatched:**
Mordor Intelligence cites the "India Cane Sugar Market" at **USD 55.40
billion (2025)**, growing to USD 70.13bn by 2031 (4.01% CAGR)
[Mordor Intelligence, accessed 2026-07-21]. Sanity check: USD 55.4bn ÷
30.95 MT (India's 2025-26 production, ISMA/Business Standard, 11-Nov-2025)
implies ~USD 1,790/tonne (~Rs 14,850/quintal) — **3.5x** the actual
ex-mill/mandi price band of Rs 4,170-4,270/quintal reported by CARE for
2025. This report figure is **not used** as the headline TAM; it likely
reflects a different scope (possibly a broader cane-value-chain or global
figure mislabeled "India"). Flagged as a materially diverging, low-quality
source — **not averaged in**, per the conservative-bias / triangulation
rule.

**Method 2 — bottom-up (primary, used as headline):** India's 2025-26
domestic sugar requirement is 28.5 million tonnes against 30.95 MT
production and 35.95 MT total availability (ISMA, via Business Standard,
11-Nov-2025, dated within the run's 2-year staleness window). Domestic
ex-mill/wholesale sugar prices in 2025 ran Rs 4,170-4,270/quintal (CARE
press release, 07-Oct-2025, p.2 — "In 2025, domestic sugar prices are in the
range of ₹4,170-₹4,270/quintal").
- Conservative: 28.5 MT = 285,000,000 quintals × Rs 4,170/quintal =
  **Rs 1,18,845 Cr**
- Realistic: 285,000,000 quintals × Rs 4,270/quintal = **Rs 1,21,695 Cr**
- Confidence: **M** (production/requirement figures are recent and
  authoritative; price band is a single CARE-cited range, not a full-year
  weighted average).

**Method 3 — peer revenue aggregation:** Sum of FY25 revenue for five listed
near-pure-play sugar millers: Triveni Engineering & Industries Rs 6,808 Cr,
Balrampur Chini Mills Rs 5,415 Cr, Bajaj Hindusthan Sugar Rs 5,590 Cr,
Dwarikesh Sugar Rs 1,359 Cr, Dalmia Bharat Sugar & Industries Rs 3,617 Cr
(various sources, WebSearch 2026-07-21; EID Parry excluded — its Rs
~38,534 Cr consolidated FY26 revenue is dominated by non-sugar nutraceutical
and fertiliser businesses and would overstate the sugar-specific slice).
Sum = **Rs 22,789 Cr**. India has 500+ operating sugar mills nationally,
overwhelmingly UP/Maharashtra cooperative and private mills that are
unlisted; the listed five above capture only a small, unquantified fraction
of national crushing capacity (their combined capacity as a % of national
30.95 MT NOT FOUND in this search pass). This method is **directional-only,
Confidence L**, and confirms Method 2's implicit point that peer-aggregation
severely undercounts a market this dominated by unlisted/cooperative
capacity — the "unorganised" adjustment here (30-60% India rule of thumb) is
if anything too small; the true unlisted share of Indian sugar-mill capacity
is almost certainly >70%.

**Method 5 — global per-capita benchmark:** India's per-capita sugar
consumption is ~20.2 kg/year vs a global average of 24.8 kg/year (World
Population Review / Statista, 2023 base, accessed 2026-07-21). Closing this
gap (+22.8%) at constant population would lift domestic consumption from
28.5 MT to ~35.0 MT, implying a global-average-benchmark TAM of:
- 350,000,000 quintals × Rs 4,170-4,270/quintal = **Rs 1,45,950 -
  Rs 1,49,450 Cr**
- This is an **upside case**, not the baseline; India is also seeing rising
  health-driven substitution away from sugar in urban/premium segments, a
  partial offset not separately quantified here (NOT FOUND).

**Sugar triangulation table**

| Method | Estimate (Rs Cr) | Confidence | Staleness |
|---|---|---|---|
| 1 — top-down industry report (Mordor) | ~4,59,800 (USD 55.4bn) | L — flagged, scope-mismatched, **excluded from headline** | Current (2025) |
| 2 — bottom-up (production × price) | 1,18,845 – 1,21,695 | **M — headline** | Current (2025) |
| 3 — peer aggregation (listed only) | 22,789 (floor, undercounts) | L | Current (FY25) |
| 5 — global per-capita benchmark | 1,45,950 – 1,49,450 (upside case) | M | 2023 base, within 4yr window |

Sugar TAM used: **conservative Rs 1,18,845 Cr / realistic Rs 1,21,695 Cr**
(Method 2).

### Segment 2 — Ethanol (cane/molasses feedstock, EBP)

OMC total ethanol procurement cost, ESY 2024-25 (Nov'24-Oct'25): ~Rs 62,566
Cr (infomerics/CEEW-linked industry note via WebSearch, 2026-07-21).
Feedstock split: grain-based ~66%, sugarcane-based (cane juice/B-heavy
molasses/C-heavy molasses) ~33-34% (ChiniMandi/RuralVoice, Sep-2025 and
ESY25-26 data, 2026-07-21) — this is KCP's addressable slice, since it has
no grain-based capacity.
- TAM (cane-feedstock ethanol, national): Rs 62,566 Cr × 34% =
  **Rs 21,272 Cr** (conservative)
- Realistic: OMCs allocated ~1,048 crore litres for ESY 2025-26 vs ~920
  crore litres implied for ESY 2024-25 (+14% volume); applying the same
  proportional growth to the cane-feedstock value: Rs 21,272 Cr × 1.14 =
  **Rs 24,250 Cr**
- Confidence: **M** — single-source procurement-cost figure, no independent
  cross-check found; flagged.
- Method used: import/policy-linked substitution method (Method 4 analogue —
  government procurement target and feedstock mix).

### Segment 3 — Urad Dal (black gram)

Bottom-up: India annual urad dal consumption 2.8-3.0 million tonnes
(exceeds domestic production of ~1.7-2.4 MMT most years, gap filled by
imports from Myanmar/Brazil — WebSearch, 2026-07-21). Current market
(mandi) price ~Rs 8,000-9,882/quintal (Agriwatch/Commodityonline,
dated to 02-May-2026, within staleness window).
- Conservative: 28,000,000 quintals (2.8 MMT) × Rs 8,000/quintal =
  **Rs 22,400 Cr**
- Realistic: 30,000,000 quintals (3.0 MMT) × Rs 9,882/quintal =
  **Rs 29,646 Cr**
- Confidence: **M** — consumption range is a search-aggregated estimate,
  not a single official source; official MSP for 2025-26 could not be
  retrieved (govt PDF fetch returned HTTP 403 — see search log) so the
  market-price band, not MSP, is used; this likely overstates the
  farm-gate/wholesale value slightly since retail includes processing
  margin. Flagged.
- Method: bottom-up (Method 2 analogue).

### Segment 4 — Engineering (Eimco-KCP process equipment)

India water treatment equipment market: USD 2.4bn in 2025 (Grand View
Research horizon outlook, "India Primary Water and Wastewater Treatment
Equipment Market," accessed 2026-07-21) ≈ **Rs 19,920 Cr** (at ~Rs
83/USD). Primary clarifiers were cited as the single largest
revenue-generating equipment category, "31.44% of revenue share in 2024"
(same source, scope of this % — global or India — not fully disentangled
from the search summary, flagged).
- Conservative: Rs 19,920 Cr × 31.44% = **Rs 6,263 Cr** (clarifier/thickener
  equipment slice only)
- Realistic: + 20% for adjacent segments Eimco also serves but not captured
  in the "water treatment" framing (mineral processing/thickeners, FGD,
  pulp & paper) = **Rs 7,516 Cr** — this uplift is an explicit, labelled
  assumption, not sourced to a specific report (NOT FOUND: dedicated
  India market-size report for industrial clarifiers/thickeners across all
  end-use industries).
- Confidence: **L** — narrowest, most assumption-stacked segment in this
  analysis; flagged prominently.
- Method: top-down with product-line subtraction (Method 1 analogue).

### Combined TAM (sum-of-parts, per B04 valuation_primary)

| Segment | Conservative (Rs Cr) | Realistic (Rs Cr) | Confidence |
|---|---|---|---|
| Sugar | 1,18,845 | 1,21,695 | M |
| Ethanol (cane feedstock) | 21,272 | 24,250 | M |
| Urad Dal | 22,400 | 29,646 | M |
| Engineering (clarifier/thickener) | 6,263 | 7,516 | L |
| **Total TAM** | **1,68,780** | **1,83,107** | — |

**mgmt claim vs conservative TAM:** NOT FOUND ÷ Rs 1,68,780 Cr = not
computable; mgmt_claim_ratio NOT FOUND.

---

## SECTION 3: SAM & SOM

### 3A — SAM

Filters applied per segment (product, geography, channel, customer,
capability):

- **Sugar — no discount (SAM = TAM).** Sugar is a nationally fungible
  commodity with uniform pan-India pricing; KCP faces no structural
  geography/channel/customer exclusion within India (it already sells via
  standard wholesale/trade channels). The realistic constraint is capacity,
  addressed in 3C, not market accessibility.
- **Ethanol — no discount (SAM = TAM), heavy capacity caveat carried to
  3C.** OMC procurement is a national tender/allocation system open to all
  registered distilleries; KCP's 50 KLPD distillery is eligible in
  principle for the full cane-feedstock pool.
- **Urad Dal — 60% of TAM.** Channel filter: KCP sells bulk/institutional,
  not organised branded retail (dominated by large FMCG players); geography
  filter: sourcing is regionally concentrated in the Krishna Delta, limiting
  reliable supply-side scale versus pan-India processors. SAM = 0.60 ×
  TAM = **Rs 13,440 Cr (conservative) / Rs 17,788 Cr (realistic)**.
- **Engineering — no further discount (SAM = TAM).** The TAM in Section 2
  is already narrowed to the specific clarifier/thickener/filtration
  equipment category Eimco makes; no further product-fit subtraction
  needed.

| Segment | TAM conservative (Rs Cr) | Filter | SAM conservative (Rs Cr) |
|---|---|---|---|
| Sugar | 1,18,845 | 100% | 1,18,845 |
| Ethanol | 21,272 | 100% | 21,272 |
| Urad Dal | 22,400 | 60% | 13,440 |
| Engineering | 6,263 | 100% | 6,263 |
| **Total SAM** | **1,68,780** | — | **1,59,820** |

SAM (realistic) = 1,21,695 + 24,250 + 17,788 + 7,516 = **Rs 1,71,249 Cr**

**sam_pct_of_tam** = 1,59,820 / 1,68,780 = **94.7%** (conservative basis) —
high, because the dominant segment (sugar) faces essentially no addressability
discount; this is a property of the commodity, not a sign of unusual
company reach.

### 3B — SOM at 3 and 5 years

The standard share-gain rules (1-2pp normal / 3-5pp aggressive / >5pp only
on competitor exit) are calibrated for companies with a meaningfully
measurable SAM share (low single digits or more). KCP's current blended SAM
share is **0.16%** (below) — percentage-point share-gain language is not
meaningful at this scale. SOM is instead built bottom-up per segment from
capacity, utilization, and evidenced trend, consistent with the run
context's instruction to compute SOM-implied CAGR "from evidence, not
aspiration."

**Current position (FY26, filing-anchored):**
Sugar Rs 141.55 Cr | Urad Dal Rs 44.95 Cr | Engineering Rs 78.64 Cr |
Ethanol/Alcohol ~Rs 10.20 Cr (FY25 sold value, AR p.37; FY26 not separately
disclosed in the segment table — carried flat as a placeholder, flagged) |
Chemicals + Power & Fuel Rs 33.54 Cr (held flat, immaterial, not separately
sized). Total FY26 = Rs 259.95 Cr, plus Rs 0.69 Cr unallocated — reconciles
to the injected REVENUE_CR anchor.

**Realistic scenario (used as the higher bound, shown for transparency but
not the formal handoff — see conservative bias note below):**

| Segment | Basis | 3yr Rs Cr | 5yr Rs Cr |
|---|---|---|---|
| Sugar | Flat-to-modest 3% nominal (price-led; cane-availability risk caps volume — CARE flags FY25 cane crushed fell to 2.6 lakh MT from 4.4 lakh MT on farmer crop-switching) | 154.7 | 164.1 |
| Urad Dal | Utilization ramp from ~24% of 22,000 MTPA (current) to 45% (3yr) / 65% (5yr) — capacity already installed since Feb-2023, no new capex required, execution/sourcing risk only | 84.3 | 121.8 |
| Engineering | 10% CAGR, in line with the India water-treatment-equipment market's cited 5.19-7% CAGR plus company execution; **excludes** the operator-relayed Rs 257 Cr Hyundai order | 104.7 | 126.6 |
| Ethanol/Alcohol | Flat (no visible recovery evidence; held at FY25 level) | 10.2 | 10.2 |
| Chemicals + Power (flat, immaterial) | — | 33.5 | 33.5 |
| **Total (realistic)** | — | **387.4** | **456.2** |

Realistic SOM-implied CAGR: 3yr = (387.4/259.95)^(1/3) − 1 = **14.2%**;
5yr = (456.2/259.95)^(1/5) − 1 = **11.9%**.

**Conservative scenario (used as the formal handoff, per the pipeline's
conservative-bias rule):**

| Segment | Basis | 3yr Rs Cr | 5yr Rs Cr |
|---|---|---|---|
| Sugar | Flat (0%) — cane-availability structural risk offsets FRP-linked price gains | 141.6 | 141.6 |
| Urad Dal | Slower utilization ramp: 24% → 35% (3yr) → 45% (5yr) | 65.5 | 84.3 |
| Engineering | 6% CAGR — below the equipment-market growth rate, reflecting Eimco's lumpy, order-book-driven revenue and execution risk; **excludes** the Hyundai order | 93.7 | 105.3 |
| Ethanol/Alcohol | −5%/yr — extending the FY24→FY25 output-collapse trend (11.61 vs 65.41 lakh litres, AR p.37) rather than assuming a reversal | 8.7 | 7.9 |
| Chemicals + Power (flat) | — | 33.5 | 33.5 |
| **Total (conservative)** | — | **343.0** | **372.6** |

Conservative SOM-implied CAGR: 3yr = (343.0/259.95)^(1/3) − 1 = **9.7%**;
5yr = (372.6/259.95)^(1/5) − 1 = **7.5%**.

**These conservative figures are the formal `som_3yr_cr` / `som_5yr_cr` /
`som_implied_revenue_cagr` handoff to Stage 11.** They sit well above a
naive "cyclical commodity should be flat" prior only because of one
specific, evidenced lever: Urad Dal is running at roughly a quarter of its
already-installed 22,000 MTPA capacity, so a utilization catch-up (not a
capacity expansion) does real arithmetic work. Strip Urad Dal out and the
blended CAGR falls close to mid-single digits, consistent with a low-growth
cyclical commodity core.

### 3C — Capacity cross-check

B07 capex-embedded growth is **0%** — CWIP ~Rs 25 lakh (~0.1% of revenue),
parent capex down 36% YoY and below depreciation. This would normally imply
the SOM figures above are the optimistic side. Segment-by-segment:

- **Sugar:** 7,500 TCD crushing capacity is unchanged and was itself
  under-utilised in FY25 (72-day season, 2.6 lakh MT cane crushed) versus
  FY24 (85-day season, 4.4 lakh MT). The conservative SOM (flat revenue) is
  well within physical capacity; the binding constraint is **cane
  availability** (farmers in the Krishna belt shifting to paddy/black
  gram/vegetables — CARE, p.2), not capacity or capex. **Sufficient.**
- **Urad Dal:** 22,000 MTPA capacity was built in Feb-2023 and is running at
  an estimated ~21-26% utilization today (Rs 44.95 Cr revenue ÷ Rs
  8,000-9,882/quintal price band ≈ 4,550-5,600 MT). Both the conservative
  (35%→45%) and realistic (45%→65%) utilization targets are physically
  achievable on **existing** capacity with **zero** further capex.
  **Sufficient — and the single largest source of capacity-supported,
  capex-free upside in this analysis.**
- **Engineering:** Eimco-KCP's own fabrication-capacity ceiling is NOT
  FOUND in the available cache; order-book-driven businesses of this kind
  typically scale with skilled labour and subcontracting more than fixed
  plant, so capacity is a softer constraint than for Sugar/Urad Dal.
  **Not independently verifiable — flagged as a data gap**, not assumed
  sufficient.
- **Ethanol:** 50 KLPD distillery capacity implies a theoretical full-capacity
  output roughly an order of magnitude above the FY25 actual of 11.61 lakh
  litres (a ~82% YoY output collapse from 65.41 lakh litres, AR p.37). The
  conservative SOM (flat-to-declining) is trivially within capacity.
  **Sufficient — capacity is not the constraint here; the FY25 collapse
  itself is unexplained in the available cache and is a genuine
  operational red flag**, not a capacity story.

**capacity_check: "sufficient — existing installed capacity across Sugar,
Urad Dal, and Ethanol comfortably covers the conservative SOM without new
capex (consistent with B07's zero capex-embedded growth); Urad Dal
utilization catch-up, not new capacity, is the SOM's main growth engine.
Engineering capacity ceiling NOT FOUND, flagged separately. Where a gap
exists, it runs the other way from usual: capacity is idle, not
constraining — the risk to the SOM is raw-material availability (cane,
black gram) and execution, not capital."**

---

## SECTION 4: GROWTH DRIVERS, RISKS & STRUCTURE

### 4A — TAM growth drivers

| Driver | Segment | Impact | Evidence |
|---|---|---|---|
| Regulatory tailwind (E20/EBP) | Ethanol | High | Nationwide E20 rollout from Apr-2025, five years ahead of the original 2030 target; ESY 2025-26 lifted restrictions on cane-juice/B-heavy-molasses diversion to ethanol (CARE, p.2) |
| Per-capita gap vs global average | Sugar | Medium | India ~20.2kg/capita vs global 24.8kg (Section 2, Method 5) |
| Formalisation / import substitution | Urad Dal | Medium | Consumption (2.8-3.0 MMT) structurally exceeds domestic production (1.7-2.4 MMT); government pulses self-sufficiency push is a stated national policy direction (general knowledge, not separately sourced here — flagged as directional) |
| Regulatory/industrial tailwind (water stress, effluent norms) | Engineering | Medium | India wastewater treatment market cited at USD 10.4bn (2025) → USD 19.4bn (2034), 7.00% CAGR (industry report, WebSearch 2026-07-21) |
| Government price support (FRP) | Sugar | Low-Medium | FRP raised 8% to Rs 340/quintal (2024-25) from Rs 315/quintal, and to Rs 355/quintal for 2025-26 (CARE, p.2) — supports price but raises input cost simultaneously, largely margin-neutral |

### 4B — TAM risks

| Risk | Segment | Monitoring signal |
|---|---|---|
| Cyclicality / weather | Sugar, Urad Dal | Cane crushed fell 39% YoY in FY25 on drought/crop-switching (CARE, p.2); a repeat would further compress the Sugar SOM below even the conservative case |
| Feedstock competition (grain vs cane ethanol) | Ethanol | Grain-based ethanol is ~66% of national EBP supply and structurally outside KCP's capability; maize's ethanol-feedstock share rose from 6.2% (ESY22-23) to ~50% (ESY24-25), squeezing the cane-based pool KCP can compete for |
| Import competition | Urad Dal | Consumption gap filled by Myanmar/Brazil imports; a sharp rupee move or trade-policy shift could reprice the domestic market either way |
| Saturation / health substitution | Sugar | Rising health-driven substitution in premium/urban segments globally and increasingly in India is a partial offset to per-capita-gap upside (Section 2, Method 5) — not separately quantified, NOT FOUND |
| Regulatory (sugar as essential commodity) | Sugar | Government retains SAP/FRP and export-quota control; policy reversal risk on either side (support or restriction) |
| Order-book lumpiness | Engineering | Eimco-KCP's own segment result swung from a loss in the FY26 Q4 quarter (-Rs 6.8 lakh) to a large full-year profit (Rs 24.6 Cr) — evidence of lumpy, quarter-to-quarter volatility (FY26_Audited_Results.txt p.4) |

### 4C — Market structure

- **Sugar:** highly fragmented, 500+ mills nationally, dominated by
  UP/Maharashtra cooperative and private mills; top-5 listed players
  (Section 2, Method 3) represent a small, unquantified fraction of
  national capacity. Competing on price, not differentiation (pure
  commodity). Southern-region mills, including KCP, have been structurally
  shrinking — CARE and the AR both note southern sugar production has
  "toppled down drastically" versus other regions and several southern
  private mills have closed (Annual_Report.txt p.35).
- **Ethanol:** consolidating toward grain-based (maize) feedstock; KCP is
  on the shrinking side of that mix shift.
- **Urad Dal:** import-dependent national market; KCP is a small regional
  processor (single 22,000 MTPA plant) in a market with structural
  production-consumption gap filled by Myanmar/Brazil imports.
- **Engineering:** specialised, technical, relationship/reference-driven
  equipment category (clarifiers/thickeners); competitors include global
  players (e.g., Metso, Veolia/Wabag-adjacent EPC contractors) and Indian
  peers; Eimco-KCP's positioning (50+ years, 25,000+ installations claimed)
  suggests an established niche rather than a price-competed commodity —
  but this is company marketing material, not independently verified.

---

## SECTION 5: SUMMARY & RUNWAY

### 5A — Funnel

```
TAM (conservative)  Rs 1,68,780 Cr   [Sugar 1,18,845 | Ethanol 21,272 | Urad 22,400 | Eng 6,263]
   -> SAM             Rs 1,59,820 Cr   (94.7% of TAM — sugar/ethanol/engineering undiscounted;
                                        Urad Dal discounted to 60% for channel/geography)
      -> current       Rs 259.95 Cr    (0.16% of SAM)
      -> SOM 3yr       Rs 343.0 Cr     (9.7% CAGR, conservative)
      -> SOM 5yr       Rs 372.6 Cr     (7.5% CAGR, conservative)
```

### 5B — Runway assessment

- **Revenue headroom** = SAM ÷ current revenue = 1,59,820 / 259.95 =
  **614.7x**. This number is mechanically large because sugar (70% of TAM)
  is a huge, undiscounted national commodity market — it is **not** a
  measure of executable opportunity for a single-plant miller with zero
  capex-embedded growth (B07).
- **TAM growth rate** (revenue-weighted blend across the four segments) ≈
  **3.7%** (Sugar 2.5% weight-adjusted, Urad Dal 3.5%, Engineering 6%,
  Ethanol 10% — see Section 4A sourcing; blend computed as
  Σ(segment TAM share × segment growth)).
- **Company CAGR vs TAM:** conservative SOM-implied CAGR (7.5-9.7%) is
  meaningfully **above** the blended TAM growth rate (3.7%) — the company is
  a **share-gainer within a slow-growing market**, not a market-rider, and
  the gain is concentrated almost entirely in one segment (Urad Dal
  utilization catch-up) that required no incremental capital.
- **Years to saturate SAM at current growth:** at even the realistic SOM
  trajectory, the company would still be at <0.3% of SAM in 5 years —
  saturation is not a relevant multi-decade concept here; the ceiling that
  matters is capacity (Section 3C), not market size.

### 5C — Runway classification

Mechanical headroom (614.7x) falls in the **MASSIVE** band (>50x) per the
standard bands used in prior runs of this pipeline (MASSIVE >50x / STRONG
20-50x / GOOD 10-20x / MODERATE 5-10x / LIMITED <5x, cross-read against TAM
growth — noted here as an explicit assumption since the exact Section 1B
v3.3 threshold text was not present in this stage's inputs).

**This stage overrides that mechanical read down to MODERATE.** Reasoning:
the 614.7x figure is an artifact of sugar being a vast, undifferentiated
national commodity market that a single 7,500-TCD plant with zero
capex-embedded growth cannot meaningfully approach — treating it as
executable "runway" would be the exact kind of aspirational sizing the
operating rules for this stage warn against. The blended TAM itself grows
slowly (3.7%). The genuine, capacity-supported growth story here is narrow
and specific (Urad Dal utilization catch-up), not broad market pull. A
MODERATE classification reflects real, evidenced upside (conservative SOM
CAGR of 7.5-9.7%, comfortably above the TAM growth rate) without pretending
the company is riding a large or fast-growing addressable market.

### 5D — SAM expansion levers actually being pursued

- **Urad Dal utilization ramp** — the only lever with hard evidence of
  being "pursued" in the sense of already-committed capacity (22,000 MTPA,
  built Feb-2023) sitting well below run-rate. Potential addition:
  Rs 40-77 Cr of incremental revenue by year 5 (conservative-to-realistic
  range) at zero further capex. Revised headroom impact: marginal — this
  lever operates entirely within the existing SAM discount already applied
  in 3A.
- **Engineering order intake** — the operator-relayed Rs 257 Cr Hyundai
  order (20-Jul-2026, EIMCO-K.C.P. / Hyundai Engineering & Construction,
  Common Seawater Supply Project) is, if confirmed, a genuine SAM-expansion
  event: it would represent roughly 3.3x FY26 Engineering segment revenue
  and would extend the segment's addressable reach into international EPC
  subcontracting. **This figure is operator-relayed, pending filing
  confirmation, and is explicitly excluded from every anchored TAM/SAM/SOM
  number in this report** per the run's non-anchored-context instruction.
  It is named here only as a lever to monitor, not counted.
- **No new sugar-crushing or distillery capacity, no new product line** —
  confirmed by the operator's own disclosure check (21-Jan-2026 to
  21-Jul-2026 window): "What did NOT happen" explicitly lists no new
  capacity, no new plant/line, no major capex decision, no new product
  line. There is no SAM-expansion lever being pursued in Sugar or Ethanol.

### 5E — Final output card

- **TAM:** conservative Rs 1,68,780 Cr / realistic Rs 1,83,107 Cr (sum of
  parts: Sugar, cane-feedstock Ethanol, Urad Dal, Engineering)
- **SAM:** Rs 1,59,820 Cr (94.7% of TAM)
- **SOM 3yr / 5yr (conservative, formal handoff):** Rs 343.0 Cr / Rs 372.6 Cr
- **SOM-implied revenue CAGR:** 9.7% (3yr) / 7.5% (5yr)
- **Current SAM share:** 0.16%
- **Revenue headroom:** 614.7x (mechanical, capacity-overridden — see 5C)
- **Runway class: MODERATE** (overridden down from mechanical MASSIVE)
- **Management TAM claim:** NOT FOUND (no quantified figure; qualitative
  outlook language only)

**Valuation implication line:** At **7.5-9.7%** revenue CAGR implied by
SOM, with a margin trajectory that starts from a **negative** consolidated
base (FY26 PAT loss; Sugar segment result −Rs 17.3 Cr, per
FY26_Audited_Results.txt p.4) and depends on the Engineering segment (the
only consistently profitable segment, +Rs 24.6 Cr FY26 segment result)
carrying a growing share of the mix, the earnings growth embedded here is
**not independently computable from this stage's inputs alone** (margin
trajectory is a Stage 11 input) — but a high-single-digit-to-low-double-digit
revenue CAGR on a currently loss-making commodity core is a **modest**
growth underpin, which [does not, on its own, support] an aggressive
multiple; it supports valuation being anchored to the Engineering
subsidiary's profitability and asset/investment backing (per B04's
sum-of-the-parts framing) rather than to a growth narrative on the sugar
core.

---

## SEARCH LOG

### Searches performed
1. "India sugar industry market size 2025 2026 crore CRISIL ISMA production"
2. "India ethanol blending program market size crore 2025 OMC ethanol procurement value"
3. "India urad dal black gram market size production consumption tonnes 2025"
4. "urad dal MSP 2025-26 price per quintal India black gram"
5. "India industrial water treatment effluent EPC market size crore 2025 clarifier filtration equipment"
6. "Eimco KCP annual report order book revenue clarifiers thickeners mining water treatment India"
7. "India sugar market size 2025 billion USD IMARC Mordor report"
8. "India ethanol supply year 2024-25 sugarcane based vs grain based ethanol share crore litres"
9. "India listed sugar companies revenue FY25 Balrampur Chini Triveni Dwarikesh EID Parry Bajaj Hindusthan Dalmia Bharat Sugar crore"
10. "India per capita sugar consumption kg per year global average comparison"
11. WebFetch: desagri.gov.in official MSP PDF (2024-25/2025-26 urad MSP)

### Searches skipped / failed
- **desagri.gov.in MSP PDF fetch returned HTTP 403** — official government
  MSP for urad 2025-26 could not be retrieved; substituted with current
  mandi/market-price data (Agriwatch/Commodityonline, dated 02-May-2026)
  for the Urad Dal TAM calc, flagged in Section 2.
- Did not separately size the khandsari/gur (unorganised cane-diversion)
  market — excluded as a different product, not a gap in the sugar TAM.
- Did not find a dedicated India market-size report specifically for
  industrial clarifiers/thickeners (Eimco's exact niche) — used the 31.44%
  "primary clarifier" revenue-share proxy from the broader water-treatment-
  equipment report instead, flagged Confidence L.
- Did not verify Eimco-KCP's own fabrication-capacity ceiling (relevant to
  3C) — NOT FOUND in the available cache or search results.
- Did not independently verify the top-5 listed sugar peers' combined share
  of national crushing capacity (Method 3 gross-up) — left as a directional,
  unquantified caveat.

---

```yaml
stage: B09-tam
company: "KCPSUGIND"
run_date: "2026-07-21"
model: claude-sonnet-5
status: partial
input_gaps:
  - "Management TAM claim: NOT FOUND (AR MD&A gives qualitative outlook only, no quantified market size)"
  - "Official government MSP for urad dal 2025-26: fetch failed (HTTP 403), substituted with current mandi price data"
  - "Eimco-KCP standalone fabrication-capacity ceiling: NOT FOUND (relevant to 3C capacity cross-check for Engineering segment)"
  - "Top-5 listed sugar peers' combined share of national crushing capacity: NOT FOUND (Method 3 gross-up left unquantified)"
  - "FY26 Ethanol/Alcohol segment revenue not separately disclosed in filed segment table; FY25 AR figure (Rs 10.20 Cr sold value) carried forward flat as a placeholder"
flags:
  - "Engineering segment is 26.3% of FY26 gross consolidated revenue (Rs 78.64 Cr, filing-anchored), materially larger than B04's injected 6.1% (which reflects standalone-parent-only figures) — flagged for reconciliation at synthesis"
  - "Ethanol/Alcohol output collapsed 82% YoY in FY25 (11.61 vs 65.41 lakh litres, AR p.37) even as the national E20/EBP TAM expands — company is not capturing the sector tailwind; unexplained operational red flag"
  - "revenue_headroom_x (614.7x) is a mechanical SAM/current-revenue artifact of sugar being a vast national commodity market; runway_class overridden down from mechanical MASSIVE to MODERATE given zero capex-embedded growth (B07) and slow blended TAM growth (3.7%)"
  - "Eimco-KCP Rs 257 Cr Hyundai order (20-Jul-2026) is operator-relayed, pending filing confirmation, and is EXCLUDED from all anchored TAM/SAM/SOM figures; if confirmed it is ~3.3x FY26 Engineering segment revenue"
  - "SOM conservative CAGR (7.5-9.7%) is driven almost entirely by one evidenced, capex-free lever: Urad Dal running at ~21-26% of its already-installed 22,000 MTPA capacity; strip this out and the blended CAGR falls to mid-single digits, consistent with a low-growth cyclical commodity core"
market_definition: "Sum-of-four-parts: India domestic sugar (national commodity), India cane/molasses-based ethanol (EBP-linked), India urad dal processing, and India industrial clarifier/thickener process-equipment (Eimco-KCP subsidiary)"
tam_cr: {conservative: 168780, realistic: 183107}
sam_cr: 159820
sam_pct_of_tam: 94.7
som_3yr_cr: 343.0
som_5yr_cr: 372.6
som_implied_revenue_cagr: {yr3: 9.7, yr5: 7.5}
current_sam_share_pct: 0.16
revenue_headroom_x: 614.7
tam_growth_pct: 3.7
runway_class: "MODERATE"
mgmt_claim_cr: 0
mgmt_claim_ratio: 0
mgmt_claim_read: "not applicable - no quantified management TAM claim found; qualitative outlook language only"
capacity_check: "sufficient - existing installed capacity (Sugar 7,500 TCD, Urad Dal 22,000 MTPA, Ethanol 50 KLPD) covers the conservative SOM without new capex, consistent with B07 capex_embedded_growth_pct=0; Urad Dal utilization catch-up (~21-26% to 35-65%) is the main growth engine; Engineering capacity ceiling NOT FOUND"
methods_used:
  - "top-down industry report (flagged divergent, excluded from headline - Sugar)"
  - "bottom-up production x price (Sugar, Urad Dal)"
  - "peer revenue aggregation (Sugar, directional only)"
  - "import/policy-linked substitution (Ethanol, OMC procurement x feedstock share)"
  - "global per-capita benchmark (Sugar, upside case)"
stale_data_flags: []
searches_performed:
  - "India sugar industry market size 2025 2026 crore CRISIL ISMA production"
  - "India ethanol blending program market size crore 2025 OMC ethanol procurement value"
  - "India urad dal black gram market size production consumption tonnes 2025"
  - "urad dal MSP 2025-26 price per quintal India black gram"
  - "India industrial water treatment effluent EPC market size crore 2025 clarifier filtration equipment"
  - "Eimco KCP annual report order book revenue clarifiers thickeners mining water treatment India"
  - "India sugar market size 2025 billion USD IMARC Mordor report"
  - "India ethanol supply year 2024-25 sugarcane based vs grain based ethanol share crore litres"
  - "India listed sugar companies revenue FY25 Balrampur Chini Triveni Dwarikesh EID Parry Bajaj Hindusthan Dalmia Bharat Sugar crore"
  - "India per capita sugar consumption kg per year global average comparison"
  - "WebFetch desagri.gov.in MSP PDF"
searches_skipped:
  - "Official desagri.gov.in MSP PDF - HTTP 403, substituted with mandi price data"
  - "Khandsari/gur unorganised market sizing - excluded as different product"
  - "Dedicated India clarifier/thickener market report - used 31.44% proxy from broader water-treatment report instead"
  - "Eimco-KCP standalone fabrication capacity - not found"
  - "Top-5 listed sugar peers' combined national crushing capacity share - not found"
```
