# B09 — TAM / SAM / SOM Market Sizing
**Company:** Millworks Technologies Limited (MILLWORKS)
**Run date:** 2026-08-22
**Stage:** B09-tam | Model: claude-sonnet-5

---

## SECTION 1: MARKET DEFINITION

### 1A Precise boundaries

**Product scope:** Precision-machined components, sheet-metal parts, fabricated sub-assemblies and integrated sub-systems, made under Build-to-Print (BTP, customer drawing) and Build-to-Spec (BTS, customer functional requirement) contract-manufacturing models. Excludes: full weapon platforms, complete rolling stock, complete aircraft/engines, complete semiconductor tools, electronics/avionics assemblies, castings, large forgings — Millworks supplies INTO these, it does not build them (RHP p.120-124).

**Geographic scope:** India-domiciled demand (Defence, Railways, Semiconductor-equipment OEMs and DPSUs), plus an export channel already live — 27.47% of FY26 revenue went to customers in 9 countries (Canada, US, Israel, Germany, France, Macedonia, Italy, UK, Czech Republic), concentrated in Aerospace and Semiconductor-machinery segments (RHP p.121). Headline TAM/SAM below is sized on the **India domestic addressable pool only**; export upside is named as an unquantified SAM-expansion lever in 5D.

**Customer scope:** OEMs and Tier-1 integrators in Defence (DPSUs, private primes, drone platform companies), Indian Railways production units and rolling-stock OEMs, semiconductor manufacturing/testing-equipment OEMs, and aero-engine OEMs — companies that outsource machined-component and sub-assembly work rather than make it in-house.

**Channel scope:** Direct BTP/BTS contract-manufacturing relationships requiring AS9100D and ISO 9001:2015 certification (Millworks holds both, multi-site) (RHP p.120).

**Price segment:** Mission-critical, regulated, low-to-medium-volume, high-tolerance work — not commodity/high-volume machining.

**Explicit inclusions:** missile airframe/guidance-housing components, drone structural frames/BLDC motor parts, train braking/door/coupler/pantograph components, semiconductor equipment fixtures and base frames, aero-engine turbocharger/fuel-filter/turbine-blade components, spring and wire-form components (Unit IV, trial stage, not yet revenue-generating) (RHP p.122-124).

**Explicit exclusions:** full defence platforms, full rolling stock, chip fabrication/design, aircraft OEM assembly, civil works and land acquisition components of railway capex, non-precision commodity fasteners.

### 1B Management's own TAM claim

**NOT FOUND.** The RHP's "Industry Overview" chapter (p.102-127) reproduces third-party macro statistics — India's defence budget, railway capex, semiconductor end-market size — but at no point does management assert a company-specific addressable-market number, a served-market definition, or a "TAM" figure tied to Millworks' actual product scope (machined components/sub-assemblies). This is a genuine gap, not an oversight in this report: no market-research firm publishes a disaggregated "precision machined components for Indian defence/rail/semiconductor-equipment" market size (verified by search, Section 2).

Read as an **implicit** claim, the macro citations (full national defence budget ₹6,81,210cr, full India semiconductor end-market ₹4,64,940cr, full India railway gross revenue ₹2.79 lakh cr) would be **broad** — several orders of magnitude beyond a Tier-3 component supplier's addressable slice, and management does not narrow them. Per the injected run instructions, the operative "management claim" tested against a defensible ceiling in this report is instead the **FY27 working-capital-table implied revenue (~₹346cr)** — see Section 3C and the YAML `mgmt_claim_*` fields.

---

## SECTION 2: TAM ESTIMATION, MULTIPLE METHODS

### Method 1 — Top-down (segment procurement/equipment-market pools)

Segment addressable pools, each anchored to a disclosed current-year figure, weighted by Millworks' own FY26 revenue mix (Defence 69.43%, Railways 23.65%, Semiconductor 5.94%, Aerospace 0.99%; RHP p.123):

| Segment | Pool used | Value | Source | Confidence |
|---|---|---|---|---|
| Defence | Capital outlay earmarked for **domestic-industry** procurement, FY26 | ₹1,12,000 cr | RHP p.106, citing PIB press release, Feb 2026 defence budget | H, current |
| Railways | India Railway Equipment Market (rolling stock + infrastructure equipment), 2024 | US$12.31bn → ₹1,05,866 cr (@₹86/US$, RHP-implied FX) | TechSci Research, via web search, 2024 | M, ~2yr old, equipment-not-component level |
| Semiconductor equipment | India Semiconductor Manufacturing Equipment Market, 2024 | US$1,397.7mn → ₹12,020 cr | Grand View Research, via web search — **lowest of 3 divergent estimates found (GVR $1.4bn / PS Market Research $2.6bn / Straits Research $17.9bn for the same 2024 category — 12x spread, flagged, conservative pick used per pipeline rule)** | L-M, source divergence flagged |
| Aerospace | NOT FOUND at India-specific, aerospace-only split (India's disclosed $30.72bn "Aerospace **and** Defence" figure bundles Defence, and would double-count the row above) | excluded from pool | — | Aerospace is 0.99% of FY26 revenue — immaterial to the headline number |

**Segment pool total (platform/equipment-market level, "100% capture ceiling"):** ₹1,12,000 + ₹1,05,866 + ₹12,020 = **₹2,29,886 cr**. This is a ceiling, not Millworks' TAM — it is the value of the platforms/equipment these budgets fund, most of which is captured by OEMs, DPSUs and Tier-1 integrators, not by an outsourced Tier-2/3 machining vendor.

**Outsourcing/component discount.** The only sourced ratio found anywhere (RHP text, RHP-cited government sources, or web search) for "value of outsourcing as % of value of production" in this space is **37.4%, for Defence only, dated 2015-16** (source: India Briefing / defence-MSME commentary, via web search). This is **10 years old — STALE under the staleness rule (>4 years, direction only, never the headline number)**. No current equivalent exists for Railways or Semiconductor-equipment. Applied here, flagged, as the sole available cross-sector proxy — **not asserted as precise**:

₹2,29,886 cr × 37.4% ≈ **₹86,000 cr — TAM (conservative), Low-Medium confidence, order-of-magnitude only.**

TAM (realistic) is left at the undiscounted pool level, ₹2,29,900 cr, explicitly labelled a ceiling.

### Method 2 — Bottom-up (unit economics)

**NOT FOUND / skipped.** A bottom-up build requires an addressable unit count (e.g. number of qualified vendor slots, platforms in production, machine-hour demand per program) and a revenue-per-unit figure at industry level. Neither the RHP nor web search discloses this for the machined-component/sub-assembly layer specifically. Fabricating a unit count would be an estimate presented as fact — not done. Company-level machine-hour economics are used instead, bottom-up, for SOM only (Section 3B/3C), where they are directly sourced from Millworks' own Chartered Engineer capacity certificate (RHP p.87-88).

### Method 3 — Peer revenue aggregation

Direct listed comparables (RHP's own peer set, p.94-95, FY26 Total Income):
- Unimech Aerospace and Manufacturing Ltd: ₹287.46 cr (>90% export, precision tooling/components/EMS for aerospace, nuclear, semiconductor)
- Azad Engineering Ltd: ₹648.63 cr (precision-forged/machined components for aerospace, defence, energy, oil & gas)
- Millworks itself: ₹148.77 cr

Sum: **₹1,084.86 cr**. This set is **not exhaustive** — other listed and unlisted precision-component makers exist (e.g. Paras Defence, MTAR Technologies, Data Patterns are adjacent but electronics/systems-weighted, not pulled in this run for scope/effort reasons; ~430 licensed defence companies and ~16,000 defence-associated MSMEs exist nationally per RHP p.114, almost entirely unquantified). Three companies' revenue is too narrow a base to extrapolate a credible national TAM via the standard organised+unorganised-30-60% convention — doing so would be an unsupported multiplication, not an estimate. **Method 3 is therefore used for competitive/SAM benchmarking (Section 3), not as a headline TAM output.**

### Method 4 — Import substitution / government target (Defence, 69.4% of revenue)

- Government target: ₹3,00,000 cr (₹3 lakh crore) total defence production by FY29 (RHP p.113-114, source IBEF Feb-2026)
- Private sector currently contributes **21%** of total defence production (RHP p.114, source PIB Apr-2025)
- Holding that share flat (conservative — government policy via Make in India, Green Channel Status, iDEX explicitly pushes the private/MSME share **up**, so 21% understates the FY29 figure): 21% × ₹3,00,000 cr = **₹63,000 cr — private-sector defence-production value pool by FY29**
- Current-year cross-check: Defence production FY26 (Apr-Dec, annualised) ≈ ₹1,46,075 cr (RHP p.112, 9-month actual ₹1,09,556cr annualised); 21% private share → **₹30,676 cr current private defence-production run-rate**, H confidence, current-year data.

No sourced fraction exists for how much of that ₹30,676-63,000cr private-defence-production pool flows down to Tier-2/3 component/sub-assembly suppliers versus stays in-house at the prime level — flagged NOT FOUND. This method's value is as a **Defence-segment growth ceiling for the largest revenue line**, cross-checking Method 1's direction, not as a second independent TAM number.

### Method 5 — Global benchmark

Directional only. India's Aerospace & Defence market (US$30.72bn, 2025, Research and Markets) is ~3.4% of the global A&D market (US$899.65bn, 2026, RHP-cited source, thebusinessresearchcompany.com, p.109) against India's ~17-18% share of world population — India is structurally under-indexed on defence/aerospace manufacturing spend relative to population, consistent with the disclosed government push (Atmanirbhar Bharat, 70% self-reliance target by 2027, ₹50,000cr export target by 2029). This supports the **direction** of TAM growth (Section 4A) but produces no usable headline figure at the component-supplier layer.

### Triangulation table

| Method | Output | Confidence | Staleness |
|---|---|---|---|
| 1 — Top-down | Conservative ₹86,000 cr / Realistic (ceiling) ₹2,29,900 cr | L-M (stale multiplier) / H (pool sourcing) | 37.4% ratio is 2015-16 — STALE, direction only |
| 2 — Bottom-up | NOT FOUND | — | — |
| 3 — Peer aggregation | ₹1,084.86 cr (peer-set revenue, not TAM) | H (figures) / N/A (as TAM) | Current, FY26 |
| 4 — Import substitution | ₹30,676 cr (current) – ₹63,000 cr (FY29 target), Defence only | H (anchors) / M (share-forward assumption) | Current |
| 5 — Global benchmark | Directional only, no figure | — | Current |

**Conservative estimate used for downstream YAML: ₹86,000 cr.** **Realistic estimate: ₹2,29,900 cr** (explicitly a platform-level ceiling, not a component-supplier-realizable figure — carried forward with that caveat).

**Management claim vs conservative estimate:** no explicit TAM claim exists (1B) — this ratio is therefore not computable in the standard sense. The substitute comparison the run specifies — FY27 working-capital-implied revenue (₹346 cr, Section 3C) against the 3-year SOM (₹261 cr) — gives **1.33x**, discussed below.

---

## SECTION 3: SAM & SOM

### 3A SAM

Applying the five filters to TAM (conservative, ₹86,000 cr):

1. **Product fit** — already embedded in the Method-1 outsourcing discount (37.4%); no further cut here to avoid double-counting.
2. **Geography** — pass-through; the segment pools are already India-scoped and Millworks is India-domiciled with all four units in Bengaluru; exports are additive upside, not subtracted (kept as unquantified SAM-expansion lever, 5D).
3. **Channel fit** — pass-through; AS9100D/ISO 9001 certification requirement is already implicit in "outsourced-to-qualified-vendor" framing above, not double-discounted.
4. **Customer fit** — NOT FOUND as a sourced fraction (no data on what share of outsourced spend is accessible to Tier-3/MSME-scale vendors vs reserved for Tier-1 integrators). Not applied as a separate cut to avoid inventing a number; folded into the capability filter below with that caveat stated.
5. **Capability fit** — Millworks' actual process scope (CNC 3/4/5-axis machining, turn-mill, wire EDM, laser cutting, press-brake sheet metal, springs) addresses a **subset** of the outsourced-component universe, which also includes castings, forgings, large fabricated structures and electronics/avionics assembly that Millworks does not do. **No sourced fraction exists for this split.** Applied here as an explicit **analyst judgment of 50%** (not sourced — flagged as the report's single largest unsourced assumption) reflecting that Millworks addresses roughly half of the realistic outsourced-machining/sub-assembly scope within its three core sectors, based on its demonstrated product breadth (missile/drone components, rail braking/door/coupler/pantograph parts, semiconductor fixtures, aero-engine ancillary parts) against the fuller outsourced-component universe those sectors imply.

**SAM = ₹86,000 cr × 50% ≈ ₹43,000 cr.** SAM as % of TAM (conservative) = **50%** (a direct artefact of the single judgment cut above — flagged, not a triangulated result).

### 3B SOM at 3 and 5 years

**Current SAM share is ~0.35%** (₹148.77cr / ₹43,000cr). At this near-zero share, the standard "1-2pp normal / 3-5pp aggressive" share-gain convention **breaks down**: 1pp of a ₹43,000cr SAM alone would imply ₹430cr of incremental revenue in 3 years — a ~3.9x multiple of current revenue, which is not a "normal" trajectory by any definition and would misuse the convention. **SOM is instead built bottom-up from Millworks' own disclosed physical capacity**, the more defensible anchor given the data available:

- FY26 actual production hours across revenue-generating units (Unit 1: 90,231 + Unit 2: 74,466 + Unit 3: 3,632 + Unit 4-Machining: 73,066) = **241,395 hours**, against FY26 revenue ₹148.77cr → **realisation rate ≈ ₹6,163/hour** (RHP p.87-88, Chartered Engineer certificate; RHP p.24/56 revenue).
- FY26 blended utilisation on the then-installed 3,83,019 hours = 241,395/383,019 = **63.0%** (matches the injected B07 base figure).
- Proposed installed capacity post-IPO capex: **6,71,499 hours** (+75.3%; RHP p.88, funded by the ₹61.03cr machinery objects-of-issue tranche, no purchase orders placed as of RHP date).

**SOM 3yr** (holding utilisation flat at the FY26 blended 63.0% — conservative, no assumed improvement): 6,71,499 × 63.0% = 423,044 utilised hours × ₹6,163/hour ≈ **₹261 cr**.
Implied 3-year revenue CAGR: (261/148.77)^(1/3) − 1 ≈ **20.6%**.

**SOM 5yr** (utilisation ramping to 77.16% — the highest per-unit utilisation Millworks has actually demonstrated to date, Unit 4-Machining FY26, not an invented optimistic figure): 6,71,499 × 77.16% = 518,129 utilised hours × ₹6,163/hour ≈ **₹319 cr**.
Implied 5-year revenue CAGR: (319/148.77)^(1/5) − 1 ≈ **16.5%** (decelerating vs the 3-year figure — realistic, as utilisation approaches its own demonstrated ceiling with no further disclosed capex).

Caveat: this hours×realisation-rate model assumes the blended revenue-per-hour holds as product mix shifts; FY26 already included ~₹23cr of "non-inventory intensive service income" (RHP p.91) that may not fit the hours model cleanly — a modelling limitation, not a sourcing gap.

### 3C Capacity cross-check — the load-bearing finding of this report

Management's own **Fiscal 2027 working-capital table** (RHP p.91, certified by Vishnu Daya & Co. LLP, 29 June 2026) implies a revenue figure, cross-validated two independent ways:

- Via **trade receivables**: average FY27 receivables (₹13,868.68L opening + ₹14,015.00L closing)/2 = ₹13,941.84L, at a projected 147-day holding period → implied revenue = ₹13,941.84L × 365/147 = **₹34,617.67L ≈ ₹346.18 cr**
- Via **inventory**: average FY27 inventory (₹1,146.60L + ₹5,492.00L)/2 = ₹3,319.30L, at a projected 35-day holding period → implied revenue = **₹34,629.6L ≈ ₹346.30 cr**

Both methods converge tightly on **~₹346 cr implied FY27 revenue** — i.e., management's own certified working-capital plan implies **2.33x FY26 revenue in one year**.

Compare to the capacity-bound ceilings above:
- **3yr SOM: ₹261 cr** — mgmt's 1-year figure is already **32.6% above** this
- **5yr SOM: ₹319 cr** — mgmt's 1-year figure is still **8.5% above** this

**The gap is ₹85 cr against the 3-year SOM, and the mgmt figure clears even the 5-year ceiling.** Even at 100% utilisation of the full new 6,71,499-hour installed base (a ceiling no unit has ever hit; best actual is 77.16%), implied revenue would be 6,71,499 × ₹6,163 ≈ ₹414cr — so ₹346cr is not physically impossible in the extreme, but it requires ~83.6% utilisation of capacity that, per the RHP itself, had **no purchase orders placed as of the RHP date**, commissioned and ramped inside a single fiscal year, against a company whose own units have taken 1-2 years to reach 70-77% utilisation historically (Unit 3, started April 2024, still at 75.67% two years in).

**Named gap: ₹85 cr (FY27 mgmt-implied revenue vs 3yr capacity-bound SOM). The capex/management plan is the optimistic side of this gap, not the SOM.**

This sits on top of a separately-flagged cash problem: FY26 trade receivables were 178 days (93% of revenue) "primarily attributable to unforeseen geopolitical instability and war-like conditions" per the RHP's own words (p.91), and operating cash flow has been under pressure. Even if the physical capacity existed, funding a ₹346cr revenue run rate would require working capital well beyond the ₹81.5cr the IPO earmarks for FY27 (Total Working Capital per the same table rises to ₹16,427L ≈ ₹164.27cr from ₹5,428.91L ≈ ₹54.29cr in FY26 — a 3.03x jump funded only ₹81.5cr by the IPO, the rest by borrowings ₹14cr and internal accruals ₹68.77cr that don't yet exist at that scale).

---

## SECTION 4: GROWTH DRIVERS, RISKS & STRUCTURE

### 4A TAM growth drivers

| Driver | Impact | Evidence |
|---|---|---|
| Regulatory tailwind | High | Atmanirbhar Bharat; 70% self-reliance-in-weaponry target by 2027; 75% of MoD modernisation budget (₹1,11,544cr) earmarked for domestic procurement (RHP p.115) |
| Import substitution | High | 65% of defence equipment now domestically manufactured, up from ~30-35% self-sufficiency historically (RHP p.114) |
| Formalisation | Medium | DPSUs/OFB mandated to build outsourcing/vendor-development plans favouring MSME Tier-2/3 suppliers (web search, niir.org/electronicsforyou.biz) |
| New applications | Medium-High | Drone/UAV and anti-drone component demand (Quick Pay captive relationship); Micron ATMP facility commissioning, Sanand, Feb 2026 (RHP p.106) |
| Technology enablement | Medium | KAVACH signalling rollout (37,000km target); 7 new high-speed rail corridors, Union Budget 2026-27 (RHP p.117-118) |
| Geographic expansion | Medium | Exports already 27.47% of FY26 revenue to 9 countries; national target ₹50,000cr defence exports by 2029 (RHP p.113) |

### 4B TAM risks

| Risk | Monitoring signal |
|---|---|
| Import competition persists | India still imports ~35% of defence equipment; global A&D primes could dual-source or vertically integrate |
| Cyclical/geopolitical disruption — already realised once | FY26 receivables blew out to 178 days, explicitly attributed by the company to "geopolitical instability and war-like conditions" affecting export collections (RHP p.91) |
| Semiconductor-cycle exposure | Global chip-sales swings (SIA: +25% QoQ Q1-2026, historically volatile) flow through to equipment-maker capex, Millworks' Semiconductor segment (5.94% of revenue) |
| Single-site concentration | All four manufacturing units are in Bengaluru — one state/city event is a single point of failure for the whole outsourced-component book |
| Customer/qualification-cycle risk | Top-5 customers = 81.07% of FY26 revenue, Quick Pay alone 47.02% (RHP p.121-122, B04) — TAM growth does not automatically become Millworks' growth if qualification cycles or the Quick Pay relationship change |

### 4C Market structure

- **Fragmented, formalising Tier-2/3 base:** ~16,000 defence-associated MSMEs, 430+ licensed defence companies, 16 DPSUs nationally (RHP p.114); only 2 direct listed component-tier peers identified (Unimech Aerospace, Azad Engineering) — the organised/listed slice of this market is tiny relative to the fragmented private base.
- **Top-3 concentration:** not disclosed at the component-tier level; platform level is dominated by HAL/BEL/BEML (not directly comparable to Millworks' tier).
- **Consolidating:** Millworks itself is a consolidator, not just a target — it acquired Hindustan Spring Manufacturing Company and Universal Automobile and Dairy Products to build spring-component and expanded-capacity presence (RHP p.89).
- **Price vs differentiation:** mission-critical tolerances and dual AS9100D/ISO 9001:2015 certification favour differentiation over pure price competition, but this is in tension with the company's own "weak pricing power" characterisation (B04) — certification is a moat against new entrants, not against concentrated-customer bargaining power.
- **Entries/exits:** private-sector share of total defence production is only 21% today (RHP p.114) but trending up; CRISIL projects private defence firms' revenue growing 16-18% in FY26 after a ~20% CAGR FY22-FY25 (RHP p.113, via web search cross-reference) — the segment is growing and formalising, favourable for new entrants like Millworks with fresh capacity.

---

## SECTION 5: SUMMARY & RUNWAY

### 5A Funnel

```
TAM (realistic, platform/equipment-market ceiling)   ₹2,29,900 cr
   ↓ (37.4% stale outsourcing proxy, flagged)
TAM (conservative)                                    ₹86,000 cr
   ↓ (50% capability-fit, analyst judgment)
SAM                                                    ₹43,000 cr
   ↓ (current share ~0.35%; pp-gain convention invalid at this base —
      SOM built bottom-up from capacity instead)
SOM 3yr (capacity-bound, 63% utilisation)              ₹261 cr
SOM 5yr (capacity-bound, 77.16% utilisation)           ₹319 cr

Current FY26 revenue                                   ₹148.77 cr
Mgmt FY27 working-capital-implied revenue               ₹346 cr  ← EXCEEDS 5yr SOM
```

### 5B Runway assessment

- **Revenue headroom** (SAM ÷ current revenue) = ₹43,000cr / ₹148.77cr ≈ **289x**
- **TAM growth rate** (blended, revenue-mix-weighted): Defence budget +9.53% YoY (RHP p.106) × 69.43% + Railway capex +19.8% YoY (₹3.02L cr FY25-26 vs ₹2.52L cr FY24-25, RHP p.119) × 23.65% + Semiconductor end-market +15% CAGR 2025-30 (UBS/IBEF, RHP p.116) × 5.94% + India A&D +7.10% CAGR (Research and Markets, web search) × 0.99% ≈ **12.3%**
- **Company CAGR vs TAM:** FY24-FY26 company revenue CAGR is a distorted ~298% (₹938.6L → ₹14,876.7L over 2 years) off a near-zero base — not a meaningful "gaining share" signal, just base-effect hyper-growth from a startup-stage company. The company is not yet a steady-state operator whose share-gain trajectory can be read off historical CAGR.
- **Years to saturate SAM** at even the aggressive 3-year SOM-implied CAGR (20.6%): ln(289)/ln(1.206) ≈ **31 years**. The market is definitionally not the constraint for this company at any realistic growth rate — execution, capital and customer concentration are.

### 5C Runway classification: **MASSIVE**

By the objective SAM/revenue-headroom test (289x) and double-digit blended TAM growth (12.3%), this classifies MASSIVE on market-size grounds alone. **This classification describes market size only.** Per the run's own framing, the effective, fundable runway is narrower: gated by (a) the ₹85cr capacity gap named in 3C, (b) receivables at 178 days / 93% of revenue with a demonstrated geopolitical-shock vulnerability, and (c) 47.02% single-customer (Quick Pay) concentration. A MASSIVE TAM/SAM does not convert to MASSIVE realized growth without capital and diversified execution — this tension is carried forward as a flag, not resolved by downgrading the market-size classification itself.

### 5D SAM expansion levers actually being pursued

- **Export growth:** 27.47% of FY26 revenue already exports to 9 countries (RHP p.121), concentrated in Aerospace/Semiconductor-machinery. Potential addition: **NOT FOUND** — no global-market sizing was attempted for this run (India-only scope, Section 1A); flagged as unquantified upside rather than estimated.
- **Spring/wire-form diversification (Unit IV):** trial-stage as of RHP date, no FY26 revenue yet (RHP p.124). Potential addition: **NOT FOUND** — no market-size data for railway/industrial spring components located in RHP or web search within this run's scope.

Both levers are real and disclosed but cannot be sized without inventing a number — left as qualitative upside, not folded into the headline SAM.

### 5E Final output card

- TAM (conservative): **₹86,000 cr** | TAM (realistic ceiling): **₹2,29,900 cr**
- SAM: **₹43,000 cr** (50% of conservative TAM)
- SOM 3yr: **₹261 cr** (20.6% implied CAGR) | SOM 5yr: **₹319 cr** (16.5% implied CAGR)
- Runway: MASSIVE (market-size axis) / capacity-and-cash constrained (execution axis, flagged)

**Valuation implication line:** At **20.6%** revenue CAGR implied by the 3-year SOM, with margin trajectory of **~25%** PAT margin (FY26 actual 24.91%, RHP p.121, no forward guidance disclosed — flagged, latest actual used as proxy), the earnings growth embedded here is approximately **20-21%** CAGR (assuming flat margin), which **does not support** the current valuation reference of **~92x P/E** (RHP industry peer-group average, Unimech 87.87x / Azad 96.45x, RHP p.94, B04). Even the more aggressive management-implied FY27 growth (2.33x in one year) is a one-year spike that the capacity build cannot sustain into years 2-3 without further, currently-undisclosed capex — it does not change this read.

---

## SECTION 6: DOWNSTREAM SIGNAL CANDIDATES

| # | Candidate Signal | Entity Type | Why It Drives Demand | Likely Primary Source | Expected Cadence |
|---|---|---|---|---|---|
| 1 | Union Budget Defence capital outlay / domestic-procurement earmark | Macro | Sets the annual ceiling on domestic-industry defence spend Millworks' Defence segment (69.4% of revenue) draws from | Union Budget documents / PIB press releases (Ministry of Defence) | Event-driven (annual budget) / Quarterly (MoD contract announcements) |
| 2 | Quick Pay Private Limited order flow | Counterparty / End-customer | 47.02% of FY26 revenue; captive drone-component supply arrangement | Company RHP disclosures / related-party filings post-listing | Quarterly / event-driven |
| 3 | Indian Railways capex allocation & rolling-stock production units (ICF/RCF/MCF) | Counterparty / Macro | Funds the braking/door/coupler/pantograph component demand behind the Railways segment (23.65% of revenue) | Union Budget (Ministry of Railways) / Indian Railways press releases | Quarterly / event-driven |
| 4 | India Semiconductor Mission (ISM) equipment-OEM capex announcements | Macro / Regulatory | Drives semiconductor-equipment fixture/base-frame demand (5.94% of revenue) | MeitY / India Semiconductor Mission press releases | Event-driven |
| 5 | SRIJAN indigenisation portal / iDEX contract awards | Regulatory | Newly-indigenised item lists create fresh component-qualification opportunities across both Defence and Aerospace | Ministry of Defence SRIJAN portal / iDEX press releases | Quarterly — **SHARED** (feeds both Defence and Aerospace segments) |

**demand_externally_verifiable: true** (5 rows, above the 3-row minimum).

---
