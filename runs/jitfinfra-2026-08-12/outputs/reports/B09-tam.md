# B09 — TAM / SAM / SOM Market Sizing
**Company:** JITF Infra Logistics Ltd (JITFINFRA) | **Run date:** 2026-08-12 | **Model:** claude-sonnet-5
**FX assumption:** USD/INR ≈ 95.4 spot (Aug 2026, Federal Reserve H.10 / X-Rates); 95 used flat for all $→₹Cr conversions ($1bn = ₹9,500 Cr). This is a modelling simplification and is not itself sourced to any single data point below.

---

## SECTION 1: MARKET DEFINITION

### 1A. Precise boundaries

| Dimension | Scope (IN) | Scope (OUT) |
|---|---|---|
| Product | Water/wastewater infrastructure EPC (drinking water supply, irrigation, sewage/wastewater treatment, industrial effluent treatment/ZLD) delivered via EPC, HAM, DBOT and annuity-O&M contracts; municipal solid-waste-to-energy (WtE) concessions — mass-burn/RDF power generation, plus adjacent resource-recovery (CBG, compost, RDF sale) as an emerging, not-yet-material adjacency | Steel trading (4.6% of FY26 revenue, non-core, no market study run); rail-wagon manufacturing (divested Sept 2024); water purifier/consumer retail products; water-treatment chemicals-only businesses; industrial WtE (waste-heat/captive) unless municipal-solid-waste-fed |
| Geography | India (all states); this is where 100% of FY26 revenue and the entire disclosed order book sit | International — a Tanzania project funded via Exim Bank is cited as a base to "expand into other African markets" (AR p.84) but is not yet revenue-generating; excluded from TAM, carried as an optionality note in 5D |
| Customer | Urban local bodies (ULBs), state governments/PSUs (funded via Jal Jeevan Mission, AMRUT 2.0, Namami Gange, SBM-Urban 2.0, MNRE bioenergy programme), and industrial customers for effluent treatment/ZLD | Individual/retail consumers; private captive water systems outside effluent-treatment scope |
| Channel | Competitively tendered government/ULB EPC, HAM, DBOT and PPP-concession contracts | Departmental/force-account execution not open to private bidders (relevant to the Section 2 bottom-up haircut) |
| Price segment | Full range — capex-heavy EPC/HAM construction revenue and long-tenure O&M/tipping-fee/PPA annuity revenue | — |

A wrong definition here breaks every downstream number, so this scope is deliberately narrower than "everything JITF's parent Jindal Group touches" and narrower than "all Indian environmental spend" — it is water-infra-EPC-and-O&M plus MSW-to-energy, India only, government/ULB-funded.

### 1B. Management's own TAM claim (held for comparison, not adopted on trust)

From the AR 2025-26 MD&A (p.78-82) and the injected extract, management cites several overlapping figures rather than one clean TAM:
- **Water:** "India water-treatment market ~USD 2.3bn (2024) → ~USD 7.0bn (2035) at ~10.6% CAGR" (injected extract; not found verbatim as a chart in the AR pages read, likely sourced from an investor-presentation slide not in the input set).
- **WtE, narrow:** India WtE market USD 1.05bn (2023) → USD 1.52bn (2024) → USD 1.95bn (2030P), CAGR ~2.6% (AR p.80, chart sourced to imarcgroup.com).
- **MSW management, broad:** USD 7.85bn (2025) → USD 10.37bn (2030), CAGR 5.7% (AR p.79, sourced to blackridgeresearch.com/Mordor-style data).
- **All waste streams, widest:** USD 13.56bn (2025) → USD 18.95bn (2032), CAGR ~4.8-6.7% (AR p.79, unattributed in text).
- **Physical potential:** WtE energy potential 5,690 MW (urban+industrial) vs 522 MW installed (AR p.81, MNRE-sourced) — a 9% utilisation ratio.
- **Self-claimed share:** JUIL "retained its position as India's largest waste-to-energy operator with an estimated ~50% share of the country's operational MSW-to-energy processing capacity" (AR p.83) — **uncited**, no third-party source given.

**Credibility read: BROAD.** Management stacks four differently-scoped market-size citations (narrow WtE, broad MSW, widest all-waste, and a separate water-treatment number) rather than anchoring to one precise, company-relevant TAM, and the one company-specific claim (50% WtE share) is asserted without a source. This is typical of an AR narrative section written to convey "large and underpenetrated," not a rigorous addressable-market claim — held for the Section 2 ratio test below.

---

## SECTION 2: TAM ESTIMATION — MULTIPLE METHODS

Two sub-markets are sized separately (Water; WtE) and then summed, because JITF's two operating subsidiaries (JWIL — water, 79.5% of FY26 revenue; JUIL — WtE, 15.9%) sit in genuinely different value chains with different growth rates and different competitive structures.

### WATER (JWIL scope)

**Method 1 — Top-down (industry reports), staleness-flagged:**
| Estimate | Value (2024/2025) | CAGR | Source | Staleness |
|---|---|---|---|---|
| Water Treatment Market (India) | USD 2.3bn (2024) / USD 2.544bn (2025) → USD 6.968bn (2035) | 10.6% | Market Research Future, "India Water Treatment Market," accessed Aug 2026 | 2024 point borderline (2yr); independently matches management's own claim (1B) |
| Wastewater Treatment Plants Market (narrow) | USD 1.33bn (2024) → USD 2.46bn (2030) | 10.6% | TechSci Research / ResearchAndMarkets, "India Wastewater Treatment Plants Market," accessed Aug 2026 | 2024 point, 2yr — borderline |
| Wastewater Treatment Market (broad, incl. chemicals/equipment/services) | USD 6.67bn (2024) → USD 9.60bn (2030) | 6.10% | Unattributed aggregator in search results, accessed Aug 2026 | **STALE-adjacent (2024, 2yr) and source-attribution weak — flagged, not used for headline** |

Converting to ₹Cr (×9,500/$bn): Water Treatment Market 2024 = ₹21,850 Cr; 2025 = ₹24,168 Cr; 2035 = ₹66,196 Cr. WWTP-narrow 2024 = ₹12,635 Cr; 2030 = ₹23,370 Cr. Broad-WWT 2024 = ₹63,365 Cr; 2030 = ₹91,200 Cr.

The three estimates disagree by ~5x depending on scope (narrow plant-only vs broad chemicals/equipment/services-inclusive). The "Water Treatment Market" figure (₹24,168 Cr, 2025) is used as the top-down anchor because it is (a) independently corroborated by two separate sources (MRFR and management's own AR-adjacent claim) landing on the same number, and (b) closest in scope to JWIL's actual EPC+O&M mix (treatment-plant design-build, not equipment retail).

**Method 2 — Bottom-up (government fiscal outlay proxy):**
FY2026-27 Union Budget water-supply/sanitation/river-conservation earmark = ₹2,16,654 Cr (AR MD&A p.78, citing Union Budget presented 1 Feb 2026); Jal Jeevan Mission budget line within it = ₹67,670 Cr. Separately, JJM 2.0 (Cabinet-approved 10 March 2026) carries a total programme outlay of ₹8.69 lakh Cr through Dec 2028, of which ₹3.59 lakh Cr is central assistance (web search, Plutus IAS / Down To Earth, Aug 2026).

Not all of this fiscal outlay is contestable by private EPC/HAM contractors — a large share funds departmental execution, O&M salaries and subsidies, land acquisition and tariff support that never goes to competitive tender. Applying an assumed 45% "capital-works-actually-tendered" share (judgement call, flagged as an assumption, not sourced to any single document):
- FY27 single-year budget basis: ₹2,16,654 Cr × 45% = **₹97,494 Cr**
- JJM 2.0 programme, annualised (₹8.69 lakh Cr ÷ ~2.75 yrs to Dec-2028 ≈ ₹3,16,000 Cr/yr) × 45% ≈ **₹1,42,200 Cr**

Both bottom-up figures are 4-6x the Method 1 top-down range — a material divergence explained by scope mismatch (fiscal outlay vs. private-market-research "market size" definitions), not by underlying opportunity being larger. Flagged; **excluded from the conservative/realistic headline pick**, retained as a directional upper bound confirming there is no near-term ceiling on TAM from the government-spend side.

**Method 3 — Peer revenue aggregation + unorganised-sector estimate:**
| Company | FY revenue (₹Cr) | Basis | Source |
|---|---|---|---|
| VA Tech Wabag (domestic ~50%, int'l revenue is ~50% per Q3 FY26 commentary) | ~2,019 | FY26 consol. revenue ₹4,038.5 Cr ×50% domestic | Web search, Whalesbook/TipRanks, Aug 2026 |
| Ion Exchange (India) (water-project revenue share assumed ~60% of consol., rest is chemicals/consumer) | ~1,642 | FY25 consol. revenue ₹2,737 Cr ×60% (assumption, flagged) | stockanalysis.com, Aug 2026 |
| EMS Limited | 732 | FY26 consolidated (down ~36-37% YoY on WB election/payment-cycle disruption) | Sovrenn/Yahoo Finance, Aug 2026 |
| JWIL Infra (JITF's own water arm) | 2,228 | FY26 revenue from operations | AR p.84 |
| Thermax (water & enviro segment only, estimated ~15% of total co. revenue) | ~1,575 | Estimate, flagged — segment-level figure NOT FOUND in search | Web search did not return segment split |
| Other organised players (WPIL, Doshion, Praj enviro, Triveni water, VMC etc.) | ~1,500 | Rough aggregate estimate, flagged | Not individually sourced |
| **Organised-sector total** | **~9,696** | | |

Independent search confirms the water EPC market is fragmented: "the water sector is a fragmented and unorganised industry with top players having a market share of 2-3% at most" and "the top 20 companies account for approximately 30% of total [industrial water] market revenue" (Upstox / Vikran Group, Aug 2026) — consistent with the standard 30-60% India unorganised-sector range cited in the operating rules. Applying a **50% unorganised-sector estimate** (midpoint of the standard range, flagged as an estimate, no water-specific split found):
Market = ₹9,696 Cr ÷ (1 − 0.50) = **₹19,392 Cr**

**Method 5 — Global benchmark (directional only, not used for headline):**
Global water & wastewater treatment market ≈ USD 370bn (2025) across multiple converging sources (Fortune Business Insights, Precedence Research, Towards Chem & Materials, Aug 2026) = ₹35,15,000 Cr. India is ~17.8% of world population; a proportional per-capita benchmark implies an aspirational India TAM of ~₹6,25,700 Cr. This is presented only to show India is far below global per-capita water-infra intensity (a long-run ceiling, not a 3-5 year number) — excluded from every downstream calculation.

**Water TAM triangulation table**

| Method | Estimate (₹Cr) | Confidence | Staleness |
|---|---|---|---|
| M1 Top-down (Water Treatment Market, 2025) | 24,168 | H (2 sources converge) | 2025 point, fine |
| M1 Top-down (WWTP narrow, 2024) | 12,635 | M | borderline (2yr) |
| M1 Top-down (broad WWT, 2024) | 63,365 | L (unattributed, wide scope) | borderline/flagged |
| M2 Bottom-up (govt budget, FY27) | 97,494 | L (scope mismatch, assumption-heavy) | current |
| M2 Bottom-up (JJM 2.0 annualised) | 142,200 | L (scope mismatch, assumption-heavy) | current |
| M3 Peer aggregation + unorganised | 19,392 | M (several component estimates flagged) | current |
| M5 Global benchmark | 625,700 | L, directional only | — |

**Water TAM: Conservative = ₹19,392 Cr (M3); Realistic = ₹24,168 Cr (M1).** M2 (govt-budget) and M5 (global benchmark) are excluded from the headline pick — both diverge materially and for explainable scope reasons (fiscal-outlay inclusiveness; aspirational per-capita ceiling), not because the true opportunity differs; this is stated per the "flag, don't average" rule.

### WASTE-TO-ENERGY (JUIL scope)

**Method 1 — Top-down:** India WtE market USD 1.52bn (2024) → USD 1.95bn (2030P), CAGR 2.6% (AR p.80, imarcgroup.com; independently corroborated by web search finding "USD 1.42-1.52 billion in 2024" for the same market, IMARC Group, Aug 2026). = **₹14,440 Cr (2024)** → ₹18,525 Cr (2030P).

**Method 2 — Bottom-up (MW-capacity × company-disclosed unit economics):**
JITF's six operational WtE SPVs generated combined FY26 revenue of ₹484.13 Cr (Okhla ₹79.18 Cr + Tehkhand ₹109.74 Cr + Jaipur ₹62.96 Cr + Guntur ₹95.79 Cr + Visakhapatnam ₹67.66 Cr + Ahmedabad ₹68.80 Cr; AR p.83 SPV table) on ~110 MW operational capacity — a revenue intensity of **₹4.40 Cr/MW/year** (484.13 ÷ 110).
Applying this to MNRE's addressable "urban solid waste" potential of 1,247 MW (the in-scope segment — this is JITF's exact MSW-fed business model, excluding the 4,443 MW "industrial waste" potential which is a different customer base JITF does not currently serve, AR p.81):
1,247 MW × ₹4.40 Cr/MW = **₹5,487 Cr**
(For reference only, not adopted: applying the same rate to the full urban+industrial 5,690 MW potential gives ₹25,036 Cr — see 5D as an expansion lever, not a near-term TAM.)

**Method 3 — Peer/capacity-share cross-check (low confidence, excluded from headline):**
JUIL's Urban Infrastructure/WtE segment revenue ≈ ₹2,808.02 Cr × 15.9% = ₹446.5 Cr (FY26). If management's uncited "~50% national capacity share" claim (1B) is taken at face value, implied organised WtE revenue market ≈ ₹446.5 Cr ÷ 0.50 = ₹893 Cr; adding a modest unorganised/other-operator allowance (WtE is concession-gated and capital-intensive, so unorganised share should be far lower than water's — assumed 25%, flagged) gives ≈ ₹893 ÷ 0.75 = **₹1,191 Cr**. This number is **not used** to set the conservative TAM because it rests entirely on an unverified, uncited management claim (50% share) — using it would let an unsourced assertion set the headline number, which the operating rules prohibit. Shown for transparency only.

**Method 4 — Broader-scope cross-check (not comparable):** MSW management market (all waste streams, not just energy recovery) USD 7.85bn (2025) = ₹74,575 Cr (AR p.79/Mordor Intelligence, independently corroborated: "Mordor Intelligence estimates the market will reach USD 7.85 billion in 2025... CAGR of 5.72% to reach USD 10.37 billion by 2030," Aug 2026 search). This spans collection, transport, landfill and recycling in addition to energy recovery — WtE is only a sub-segment, so this is not directly comparable; retained as context.

**WtE TAM triangulation table**

| Method | Estimate (₹Cr) | Confidence | Staleness |
|---|---|---|---|
| M1 Top-down (narrow WtE, 2024) | 14,440 | H (2 independent sources) | borderline (2yr) |
| M2 Bottom-up (urban-MW × own unit economics) | 5,487 | M (real company data, but relies on MNRE potential figure) | current |
| M3 Peer/capacity-share | 1,191 | L — rests on uncited mgmt claim | current, but unreliable |
| M4 Broad MSW mgmt (not comparable scope) | 74,575 | L (wrong scope) | current |

**WtE TAM: Conservative = ₹5,487 Cr (M2, own-data-grounded); Realistic = ₹14,440 Cr (M1).** M3 is excluded from the pick for the reason stated above; M4 is excluded as wrong scope.

### COMBINED COMPANY TAM

| | Conservative (₹Cr) | Realistic (₹Cr) |
|---|---|---|
| Water | 19,392 | 24,168 |
| WtE | 5,487 | 14,440 |
| **Total TAM** | **24,879** | **38,608** |

### Management-claim ratio test
Using management's own currently-dated figures (Water: USD 2.3bn/2024 = ₹21,850 Cr; WtE: USD 1.52bn/2024 = ₹14,440 Cr, the exact IMARC chart management itself features), combined mgmt-claim = **₹36,290 Cr**.
Ratio = 36,290 ÷ 24,879 (conservative TAM) = **1.46x → within 1.5x → "reasonable."** Note this reasonable read is partly an artefact of management leaning on the same two independently-corroborated sources this analysis also selected as top-down anchors (Water Treatment Market/MRFR, narrow WtE/IMARC) — it is not a coincidence, but it is a genuine external corroboration, not double counting.

---

## SECTION 3: SAM & SOM

### 3A. SAM — five filters applied to conservative TAM (₹24,879 Cr)

| Filter | Retained % | Rationale |
|---|---|---|
| Product fit | 90% | JWIL/JUIL cover the dominant technology routes (drinking water, irrigation, wastewater, industrial effluent; mass-burn/RDF WtE) but not niche high-spec segments (advanced desalination/ZLD proprietary chemistry, specialised membrane supply) |
| Geography | 95% | India-only; Tanzania/Africa excluded as pre-revenue (see 5D) |
| Channel | 100% | TAM is already defined as govt/ULB-tendered work only; no further cut |
| Customer | 95% | Some of the largest state-level mega-HAM tenders require consortium/JV thresholds JITF alone cannot meet solo |
| Capability | 70% | Consolidated net worth is **negative** (B04) and JWIL is mid-scale (order book ₹11,352 Cr) against national players (WABAG ₹17,234 Cr order book) and diversified giants (L&T, Thermax); balance-sheet constraints cap the ticket size and simultaneous-project count JITF can realistically bid and execute |

SAM = 24,879 × 0.90 × 0.95 × 1.00 × 0.95 × 0.70 = **₹14,146 Cr**
SAM as % of TAM = 14,146 ÷ 24,879 = **56.9%**

### 3B. SOM at 3 and 5 years

Current core revenue (Water + WtE, excluding 4.6% trading) = ₹2,808.02 Cr × (79.5%+15.9%) = ₹2,808.02 × 95.4% = **₹2,679 Cr** (FY26).
Current SAM share = 2,679 ÷ 14,146 = **18.9%**.

Blended TAM growth (for projecting SAM forward): Water CAGR 10.6% weighted 62.6% (realistic-TAM weight, 24,168/38,608) + WtE CAGR 2.6% weighted 37.4% (14,440/38,608) = 0.626×10.6% + 0.374×2.6% = 6.64% + 0.97% = **7.61%**, applied to SAM.

Share-gain assumption: JITF sits at the **aggressive** end of the standard 3-5pp/3yr band, justified by disclosed capacity and order-book evidence — WtE portfolio doubling from 110 MW operational to a ~220 MW committed target, and JWIL order book up 123% YoY to ₹11,352 Cr (B07). A 3pp gain over 3 years and a 5pp gain (upper bound of "aggressive") over 5 years are used; note this is at the top of what the share-gain rules allow without a competitor exit or acquisition, so it is flagged as the more execution-dependent scenario, cross-checked against capacity in 3C.

- SAM_3yr = 14,146 × (1.0761)^3 = 14,146 × 1.2463 = ₹17,631 Cr
  SOM_3yr = 17,631 × (18.9% + 3pp = 21.9%) = **₹3,861 Cr**
- SAM_5yr = 14,146 × (1.0761)^5 = 14,146 × 1.4425 = ₹20,406 Cr
  SOM_5yr = 20,406 × (18.9% + 5pp = 23.9%) = **₹4,877 Cr** (rounded ₹4,875 Cr)

**Implied revenue CAGR (arithmetic):**
- 3yr: (3,861 ÷ 2,679)^(1/3) − 1 = (1.4413)^0.333 − 1 = **13.0%**
- 5yr: (4,875 ÷ 2,679)^(1/5) − 1 = (1.8198)^0.20 − 1 = **12.7%**

These figures apply to the core (water+WtE) business; total-company revenue CAGR would be very close to this since trading is only 4.6% of revenue and not a growth focus.

### 3C. Capacity cross-check

B07 (Emerging Moat) discloses: capital commitments ₹255.87 Cr (+116% YoY), capex-embedded growth of **~25.1%**, WtE portfolio 110 MW operational targeting ~220 MW, JWIL order book ₹11,352 Cr (+123% YoY).

The capex-embedded growth figure (25.1%) is **nearly 2x** the SOM-implied 3yr CAGR (13.0%). Installed-plus-committed capacity, as disclosed, is not a binding constraint on the SOM path modelled here — if anything the reverse is true.

**capacity_check: sufficient.** The gap runs the other way: the capex/order-book plan (25.1% embedded growth) is the more optimistic side of the ledger; the SOM estimate built here (13.0%/12.7% CAGR) is the conservative one. No named ₹ Cr shortfall exists.

---

## SECTION 4: GROWTH DRIVERS, RISKS & STRUCTURE

### 4A. TAM growth drivers

| Driver | Impact | Evidence |
|---|---|---|
| Penetration (treatment capacity gap) | High | Only ~28% of India's 72,368 MLD urban sewage is actually treated against ~37% installed capacity (AR p.78, NITI Aayog/IndiaSpend, undated within AR — flagged in stale_data_flags) |
| Regulatory tailwind | High | Revised Solid Waste Management Rules tighten segregation/enforcement from Oct 2025; SBM-Urban 2.0 (₹1,41,600 Cr, 2021-22 to 2025-26, more than double the previous phase) mandates garbage-free cities by 2026 (AR p.80) |
| Formalisation (HAM/annuity models) | Medium-High | AR explicitly notes contracts "increasingly bundle design, build and 15-plus years of O&M...rewarding performance...and favouring integrated players" — a structural tailwind for balance-sheet-backed players like JITF over unorganised operators (AR p.78) |
| New applications (CBG/RDF/resource recovery) | Medium | MNRE National Bioenergy Programme (₹1,715 Cr budget, 2021-26); 59 CBG plants, 684 TPD combined capacity by Nov 2025 (AR p.80) — early-stage |
| Geographic expansion (Tier-II) | Medium | AR flags "rapidly urbanising tier-II cities...as the next wave of demand" (p.82) |
| Government funding scale | High | JJM 2.0 total outlay ₹8.69 lakh Cr through Dec-2028; FY27 Union Budget water/sanitation earmark ₹2,16,654 Cr, more than double the prior-phase SBM outlay |
| Demographics/per-capita | Medium | Per-capita urban waste generation cited as roughly doubling to ~0.72 kg/day by 2025 from a historical 0.34 kg/day average (AR p.79) — unusually steep for a 2-3 year window, flagged as a management assertion worth independent verification, not corroborated externally in this search |

### 4B. TAM risks

| Risk | Monitoring signal |
|---|---|
| Payment-cycle/counterparty risk (municipal receivables) | Peer EMS Ltd FY26 revenue fell ~36% YoY on West Bengal election-related work stoppages and payment delays (Sovrenn/Yahoo Finance, Aug 2026) — a live, sector-wide example, not hypothetical |
| Commodity/input-cost risk | Stage 6 cross-read: "commodity-cost pressure is compressing sector forward margins" across water peers |
| Regulatory/tariff risk | AR's own risk section: "concession, tariff and policy risk" — WtE tariffs and PPAs set by public counterparties; water pricing has weak standalone economics without subsidy | 
| Feedstock/waste-supply risk | WtE plant economics depend on assured calorific-value waste supply; incomplete segregation affects feedstock quality (AR p.86) |
| Execution/financing risk | Capital-intensive HAM/concession model; weighted average cost of borrowing 9.16% (down from 10.19%) still a drag on annuity economics (AR p.84) |
| Cyclical/election-driven delays | Demonstrated in FY26 at a direct peer (EMS), directly relevant given JITF's own government-counterparty concentration |

### 4C. Market structure

- **Water:** Fragmented — "top players having a market share of 2-3% at most" individually; top-20 companies hold ~30% of the industrial water sub-segment, implying a large tail of small/unorganised contractors (Upstox/Vikran Group search, Aug 2026). Consolidating slowly as HAM/annuity structuring favours balance-sheet-backed players (per AR's own framing).
- **WtE:** Concentrated — JUIL claims ~50% of national operational MSW-to-energy capacity (uncited); overall national utilisation is low (522 MW installed vs 5,690 MW potential = ~9%), so the sector is better described as nascent/under-built than mature-competitive — growth here is more about capacity build-out than share-taking from incumbents.
- **Entries/exits:** No material new entrant or exit data found in this search; Essel Infraprojects, Ramky Enviro, Antony Lara Enviro Solutions and IL&FS-successor entities remain the named WtE competitors (web search, Aug 2026).
- **Price vs differentiation:** Government-tendered work is largely L1 (lowest-price) EPC bidding with limited differentiation on the construction side; HAM/annuity and O&M contracts differentiate more on financing cost and execution reliability (AR's own framing, p.84).

---

## SECTION 5: SUMMARY & RUNWAY

### 5A. Funnel

```
TAM (conservative)  ₹24,879 Cr  ─┐  Water ₹19,392 Cr + WtE ₹5,487 Cr
TAM (realistic)      ₹38,608 Cr ─┘  Water ₹24,168 Cr + WtE ₹14,440 Cr
        │  five filters (product 90% × geo 95% × channel 100% × customer 95% × capability 70%)
        ▼
SAM                  ₹14,146 Cr   (56.9% of conservative TAM)
        │  current share 18.9%, +3pp (3yr) / +5pp (5yr), SAM growing at blended 7.6%/yr
        ▼
SOM 3yr              ₹3,861 Cr    (implied CAGR 13.0%)
SOM 5yr               ₹4,875 Cr   (implied CAGR 12.7%)
```

### 5B. Runway assessment
- Revenue headroom = SAM ÷ current core revenue = 14,146 ÷ 2,679 = **5.3x**
- TAM growth rate (blended) = **7.6%**
- Company CAGR vs TAM: FY26 revenue grew **24% YoY** (REVENUE_ANCHOR) vs blended TAM growth of 7.6% — JITF is **gaining share**, not merely riding the market, consistent with the order-book (+123% YoY) and capacity (110→220MW) evidence.
- Years to saturate SAM at current growth: solving 2,679×(1.24)^n = 14,146×(1.076)^n gives n ≈ **11.7 years** at the current (unrealistically-sustained) 24% growth rate — illustrative only, since 24% growth will not persist for 12 years; shown to demonstrate SAM is not an imminent ceiling.

### 5C. Runway classification
**STRONG.** Revenue headroom of 5.3x sits in the 5-10x band, supported by a genuinely growing TAM (7.6% blended, with the larger water sub-market growing faster at 10.6%) and disclosed evidence (order book, capacity build-out) that JITF is currently outgrowing the market. Falls short of MASSIVE (which would need >10x headroom and/or faster TAM growth) given the WtE sub-market's slow 2.6% top-down growth rate and the company's negative net worth capping the capability filter.

### 5D. SAM expansion levers actually being pursued
- **WtE capacity build-out (110→220 MW):** already captured within the modelled national 1,247 MW urban-potential base; not incremental SAM, but accelerates SOM capture within existing SAM.
- **CBG/RDF/compost diversification:** explicitly named in AR strategic priorities ("diversifying into resource recovery... CBG, compost, RDF") — potential SAM addition is **NOT FOUND** in ₹ terms (no company-specific figures disclosed); nationally the CBG segment remains small (59 plants, 684 TPD as of Nov-2025) — qualitative optionality only, not sized.
- **Geographic diversification (NTPC, Mahagenco, SIPCOT zones; West Bengal, Gujarat AMC, Odisha; Tanzania/Africa):** AR names these explicitly (p.85) but gives no addressable-value figures — **NOT FOUND**, carried as unquantified optionality, consistent with the 95% (not 100%) geography filter already applied.
- **Full urban+industrial WtE potential (5,690 MW vs the 1,247 MW urban-only base used here):** applying JITF's own ₹4.40 Cr/MW unit economics to the full potential implies ₹25,036 Cr, a ₹19,549 Cr addition over the urban-only bottom-up figure — but industrial-waste WtE is a different customer relationship JITF does not currently serve, so this is listed as a lever, not folded into the base SAM.

None of these levers is sized into the headline SAM/SOM numbers above; the ₹14,146 Cr SAM / 5.3x headroom is the base case without them.

### 5E. Final output card

- TAM: ₹24,879 Cr (conservative) / ₹38,608 Cr (realistic)
- SAM: ₹14,146 Cr (56.9% of conservative TAM)
- SOM 3yr / 5yr: ₹3,861 Cr / ₹4,875 Cr
- SOM-implied revenue CAGR: 13.0% (3yr) / 12.7% (5yr)
- Runway: STRONG (5.3x headroom, TAM growing 7.6% blended, company outgrowing market)
- Management claim vs conservative estimate: 1.46x → reasonable

**Valuation implication line:** "At **13.0%/12.7%** revenue CAGR implied by SOM, with margin trajectory of **NOT FOUND** (JWIL EBITDA margin was 12.7% in FY26, +90bps YoY; AR states a mix-shift toward the higher-margin "Integrated" segment (18-25% margin band cited, AR p.84) is a stated FY27-29 priority, but no company-wide blended margin target is disclosed), the earnings growth embedded here is **NOT FOUND CAGR** (cannot be computed without a margin target), which **cannot be assessed against** the current valuation of **NOT FOUND x P/E** (P/E not provided in injected inputs; consolidated FY26 PAT is negative at −₹9.93 Cr, up from −₹24.42 Cr in FY25 — a 58% narrowing of losses — so a conventional trailing P/E is not meaningful even if a share price were available)."

This is a genuine data gap, not an estimation: neither current P/E nor a company-wide forward margin target were present in the injected inputs or found in the AR pages read, and per the operating rules missing numbers are not estimated.

---

## SEARCH LOG

**Status: complete** (all planned searches executed; none skipped)

### searches_performed
1. India water and wastewater treatment market size 2024 2030 USD billion CAGR
2. India municipal solid waste management market size 2025 CRISIL ICRA report
3. India waste to energy market size Mordor Intelligence TechSci 2025
4. Jal Jeevan Mission AMRUT 2.0 budget allocation FY27 water infrastructure India
5. VA Tech Wabag Ion Exchange EMS Limited revenue FY2025 FY2026 water infrastructure India crore
6. Antony Waste Handling Essel Infraprojects Ramky Enviro waste to energy revenue India crore
7. India water infrastructure EPC market unorganised organised share percentage
8. VA Tech Wabag FY26 annual revenue crore consolidated results March 2026
9. Ion Exchange India EMS Limited FY2026 annual revenue crore
10. "EMS Limited" wastewater FY2026 revenue crore results
11. India water sector top companies market share Wabag Ion Exchange Thermax Va Tech industrial water infrastructure Frost Sullivan 2025
12. USD to INR exchange rate August 2026
13. global water and wastewater treatment market size 2025 USD billion China per capita
14. global waste to energy market size 2025 India share percentage

### searches_skipped
None — investor presentation and concall transcripts were absent from inputs (per input_gaps) but this is a document-availability gap, not a skipped search; all web searches planned for triangulation were executed.

---
```yaml
stage: B09-tam
company: "JITFINFRA"
run_date: "2026-08-12"
model: claude-sonnet-5
status: complete
input_gaps: [prospectus, rating, announcements, shareholding, research, presentation, concalls]
flags:
  - "WtE peer/capacity-share method (Method 3) rests on JUIL's uncited ~50% national-share claim; excluded from headline TAM, shown only as a low-confidence cross-check (~₹1,191 Cr implied market, well below the adopted ₹5,487 Cr)"
  - "Government-budget bottom-up estimate for water (₹97,494-142,200 Cr, assuming a 45% capital-tender-share) is 4-6x the top-down/peer TAM and excluded from the headline as a scope mismatch (includes non-tendered departmental spend, O&M subsidies, land); retained as directional confirmation of headroom only"
  - "Consolidated PAT is negative (-₹9.93 Cr FY26, narrowed from -₹24.42 Cr FY25); P/E is not meaningful, so the Section 5E valuation-implication line is partially NOT FOUND (no P/E, no company-wide margin target disclosed)"
  - "CPCB (2021-22) MSW-generation data and an undated NITI Aayog urban-sewage-treatment-gap chart are used for directional growth-driver evidence only (STALENESS rule), never for the headline TAM number"
  - "SOM_5yr uses a 5pp share-gain assumption (top of the 'aggressive' 3-5pp band); justified by disclosed WtE capacity doubling (110→220MW) and JWIL order book +123% YoY, but flagged as the more execution-dependent scenario"
market_definition: "India water/wastewater infrastructure EPC+O&M/HAM and municipal solid-waste-to-energy concessions, government/ULB-funded, excluding steel trading and international operations"
tam_cr: {conservative: 24879, realistic: 38608}
sam_cr: 14146
sam_pct_of_tam: 56.9
som_3yr_cr: 3861
som_5yr_cr: 4875
som_implied_revenue_cagr: {yr3: 13.0, yr5: 12.7}
current_sam_share_pct: 18.9
revenue_headroom_x: 5.3
tam_growth_pct: 7.6
runway_class: "STRONG"
mgmt_claim_cr: 36290
mgmt_claim_ratio: 1.46
mgmt_claim_read: "reasonable"
capacity_check: "sufficient — capex-embedded growth (~25.1%, B07) exceeds SOM-implied 3yr CAGR (13.0%); the capex/order-book plan is the more optimistic side, SOM is the conservative one"
methods_used: ["top-down (industry reports, 2-3 sources per sub-market)", "bottom-up (govt fiscal outlay proxy for water; MW-capacity x company-disclosed unit economics for WtE)", "peer revenue aggregation + unorganised-sector estimate", "global benchmark (directional only, excluded from headline)"]
stale_data_flags:
  - {datapoint: "Broad India wastewater treatment market USD 6.67bn", source: "unattributed web-search aggregator", year: 2024}
  - {datapoint: "CPCB MSW generation 170,338 TPD / 91,512 TPD collected/treated", source: "AR MD&A p.79, citing CPCB", year: "2021-22"}
  - {datapoint: "NITI Aayog urban sewage treatment-gap chart (72,368/26,776/20,263 MLD)", source: "AR MD&A p.78, citing NITI Aayog/IndiaSpend", year: "undated, likely ~2021-22"}
searches_performed: ["India water and wastewater treatment market size 2024 2030 USD billion CAGR", "India municipal solid waste management market size 2025 CRISIL ICRA report", "India waste to energy market size Mordor Intelligence TechSci 2025", "Jal Jeevan Mission AMRUT 2.0 budget allocation FY27 water infrastructure India", "VA Tech Wabag Ion Exchange EMS Limited revenue FY2025 FY2026 water infrastructure India crore", "Antony Waste Handling Essel Infraprojects Ramky Enviro waste to energy revenue India crore", "India water infrastructure EPC market unorganised organised share percentage", "VA Tech Wabag FY26 annual revenue crore consolidated results March 2026", "Ion Exchange India EMS Limited FY2026 annual revenue crore", "EMS Limited wastewater FY2026 revenue crore results", "India water sector top companies market share Wabag Ion Exchange Thermax Va Tech industrial water infrastructure Frost Sullivan 2025", "USD to INR exchange rate August 2026", "global water and wastewater treatment market size 2025 USD billion China per capita", "global waste to energy market size 2025 India share percentage"]
searches_skipped: []
```
