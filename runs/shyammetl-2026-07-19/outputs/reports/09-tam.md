# Stage 9 — TAM / SAM / SOM Market Sizing: Shyam Metalics & Energy Ltd (SHYAMMETL)

Run date: 2026-07-19 | Model: claude-sonnet-5 | Status: PARTIAL (see Section 2 triangulation and search log — Method 3 peer aggregation not independently pulled this run)

Current annual revenue used throughout this report: **₹18,552.21 Cr** (FY26 consolidated Revenue from Operations, source: Q4/FY26 audited consolidated results, `results/518b5092-c75c-47ee-8ec1-22e9bd3f787b.pdf`, "Statement of audited consolidated financial results for the quarter and year ended 31 March 2026", Year-ended 31-Mar-26 column, "Revenue from operations" row). This supersedes the injected FY25 placeholder of ~₹15,138 Cr per task instruction. FY25 comparative on the same statement: ₹15,158.63 Cr (a small ₹21 Cr variance vs the AR's own ₹15,137.50 Cr FY25 figure — immaterial, likely a reclassification, noted not resolved).

---

## SECTION 1: MARKET DEFINITION

### 1A — Precise boundaries

- **Product scope**: Carbon steel — long (TMT bars, wire rod, structural steel, SBQ/specialty wire-bar, railway wagons) and flat (HR coil, CR coil, colour-coated/galvalume roofing, pipe); ferro-alloys (ferro chrome, silico manganese, low-carbon ferro chrome); sponge iron/DRI and iron-ore pellets (intermediate/merchant inputs sold to other steelmakers); stainless steel — long (billets, bright bars, wire rod, rebar) and emerging flat (HR/CR, precision CR, bright-annealed); aluminium (foil, flat-rolled products/FRP, EV battery foil). **Excluded**: captive/merchant power (677 MW post-expansion — internal cost lever, not sold externally at scale, per B04 asset-intensity tag); mining (SMEL has no captive ore/coal mines; raw material sourced within 250km per IR Day pg8).
- **Geographic scope**: India-primary (90% of FY26 revenue is domestic per the 10% export-contribution disclosure, IR Day pg12), with material export exposure concentrated in two segments — ferro-alloys (52% export mix) and aluminium foil (23% of exports; >60% of foil production exported) — across 40+ countries. TAM below is built India-first; export exposure is treated as an SAM-expansion lever (Section 5D), not folded into the India TAM.
- **Customer scope**: Construction contractors/distributors (TMT, structural, roofing — retail-facing via the SEL Tiger brand); other steel mills and foundries (sponge iron, pellets, billets, ferro-alloys as merchant/intermediate inputs); OEMs in auto, white goods, kitchenware, defence, engineering (stainless steel); packaging, pharma, cable, and (from FY27) EV battery makers (aluminium foil/FRP); Indian Railways/rolling-stock OEMs (wagons — new from FY27).
- **Channel scope**: Direct B2B industrial contracts (majority of volume) plus a distributor network for retail-facing long products under the "SEL Tiger" brand (TMT, structural, roofing sheets, stainless wires — IR Day pg54).
- **Price segment**: Predominantly commodity/mid-market (carbon steel is a price-taker per B04); premium/value-added at the margin (stainless flat, SBQ auto-grade, EV battery foil, thin-gauge 0.125mm CRM) — company's explicit stated strategy is migration toward this higher end ("~80% of revenue mix from more value-added products," "profits grow faster than volumes," IR Day pg45).
- **Explicit exclusions**: Auto-grade/rail-grade high-end flat steel and heavy plate (JSW/Tata Steel/AM-NS/SAIL territory) — SMEL's own HR mill (1.58 MTPA) is not yet commissioned (₹5,304 Cr of ₹5,400 Cr budgeted capex still pending per IR Day pg30), so this is treated as SAM, not current-run TAM capture. Captive power and mining are excluded entirely (internal-use only, no external market).

### 1B — Management's own TAM claim

No AR (FY24-25 Integrated Annual Report) or Investor & Analyst Day deck (17-Jun-2026) slide states an explicit rupee-crore or tonnage "TAM" figure for Shyam's addressable market — a genuinely positive signal against the CLAUDE.md concern that "management claiming TAM=SAM=growth runway is being dishonest." What management instead discloses is a bottom-up, capex-tied **revenue and capacity roadmap**:

- FY31E consolidated revenue target: **~₹42,500+ Cr** (~18% CAGR off FY26's ₹18,552 Cr) [IR Day, "Vision 2031" slide, pg46, dated 17-Jun-2026]
- FY31E EBITDA target: **~₹6,200+ Cr** (~22% CAGR), EBITDA margin ~15% (up from FY26's 12.6% operating EBITDA margin) [same source]
- Metal capacity: 16.78 MTPA installed FY26 → ~27 MTPA by FY31E [IR Day pg15, pg46]
- Segment-level buildup (IR Day pg47, "Financial Roadmap to Vision 2031") sums exactly to the headline: Stainless ₹11,969 Cr + Aluminium ₹2,331 Cr + Carbon Steel ₹17,933 Cr + SBQ ₹4,704 Cr + Specialty Alloys ₹947 Cr + CRM ₹2,976 Cr + Wagon ₹1,788 Cr = **₹42,648 Cr**, ties to the "~42,500+" headline.

**Credibility read: SPECIFIC.** This is a bottom-up, segment-by-segment, capex-named (₹13,902 Cr budgeted / ₹3,285 Cr incurred / ₹10,617 Cr pending, per B07 injected figure and confirmed on IR Day pg33) revenue plan, not a broad market-opportunity claim. Because no independent TAM figure exists to test against, Section 2's "management claim vs. conservative estimate" test below uses this FY31E revenue target as the only available quantified forward claim (flagged explicitly, see YAML flags).

---

## SECTION 2: TAM ESTIMATION — MULTIPLE METHODS

All figures ₹ Crore unless stated. Realizations used are Shyam's own FY26 per-tonne blended realizations (IR Day pg40, "Per Tonne Realizations," ₹/tonne, FY26 audited): Carbon Steel (incl. billets + finished) ₹43,043/t; Stainless Steel ₹1,40,443/t; Speciality Alloys (ferro) ₹93,837/t; Aluminium Foil ₹3,79,805/t. Using the company's own realizations (rather than an assumed market-average price) directly ties the TAM to Shyam's product mix and pricing tier.

### Method 1 — Top-down (industry volume × realization, with subtractions)

1. **Carbon steel (long + intermediates)**: India finished steel consumption FY24-25 = **137.8 million tonnes** [Ministry of Steel, cited in AR FY24-25 pg64, "India's Finished Steel Consumption" chart]. 137.8 Mt × ₹43,043/t = **₹5,93,133 Cr** gross carbon-steel-equivalent market.
   *Subtraction*: this figure spans both long and flat steel; Shyam's current commercial footprint is long-product-and-intermediate-dominant (HR flat mill, 1.58 MTPA, is not yet commissioned — pg30). No AR-sourced precise long-vs-flat split was found this run (**NOT FOUND**); applying a directional 50–55% long/SBQ/intermediate-scope haircut (analyst estimate, flagged LOW-MEDIUM confidence) yields **₹2,96,566 Cr (conservative, 50%) to ₹3,26,223 Cr (realistic, 55%)**.
2. **Stainless steel**: India stainless steel consumption FY25 = **4.8 million tonnes**, +8% YoY [ISSDA, via IBEF news item, dated 2025]. 4.8 Mt × ₹1,40,443/t = **₹67,413 Cr**. No subtraction applied — Shyam already participates across the stainless value chain (long + emerging flat).
3. **Ferro alloys**: India domestic ferro-alloys demand cited as "over 4 million tonnes"; production ~6 Mt; capacity ~7.5 Mt; exports ~2 Mt [Business Standard/BigMint, Sep-2025]. Conservative (domestic demand only): 4 Mt × ₹93,837/t = **₹37,535 Cr**. Realistic (production basis, capturing Shyam's own 52% export mix in this segment): 6 Mt × ₹93,837/t = **₹56,302 Cr**.
4. **Aluminium foil**: India aluminium foil demand ≈ **915,000 tonnes** (India is the world's 2nd-largest consumer) [DataBridge Market Research, 2025]. Volume-based: 915,000 t × ₹3,79,805/t = **₹34,752 Cr**. Cross-check via value-based estimate: India aluminium-foil-packaging market revenue USD 2,338.4 million (2025) [Grand View Research Horizon, 2025] × ₹96.4/USD (18-Jul-2026 spot rate, x-rates.com) = **₹22,546 Cr**. The two estimates diverge by ~1.5x (volume-based uses Shyam's own realization, which may run above broad-market average packaging-grade foil pricing; value-based estimate may exclude industrial/pharma-grade foil). Per the conservative-bias rule, take the lower: **₹22,546 Cr**.

**Method 1 conservative TAM = ₹2,96,566 + ₹67,413 + ₹37,535 + ₹22,546 = ₹4,24,060 Cr**
**Method 1 realistic TAM = ₹3,26,223 + ₹67,413 + ₹56,302 + ₹34,752 = ₹4,84,690 Cr**

### Method 2 — Bottom-up (addressable unit × penetration)

Addressable unit = one tonne of finished/intermediate metal product within Shyam's four product families.
- **Full-penetration ceiling** (no product-fit haircut, i.e., "if Shyam served 100% of all India demand across all four categories at its own realizations"): 137.8 Mt (carbon, unhaircut) × ₹43,043 + 4.8 Mt × ₹1,40,443 + 6 Mt × ₹93,837 + 0.915 Mt × ₹3,79,805 = ₹5,93,133 + ₹67,413 + ₹56,302 + ₹34,752 = **₹7,51,600 Cr**. This is a directional upper anchor only — it does not apply the long-vs-flat product-fit cut, so it is not used as a headline TAM.
- **Disciplined bottom-up** (product-fit applied at the unit level, same logic as Method 1's conservative case): converges to the same **₹4,24,060 Cr** as Method 1 conservative — a useful internal consistency check between the two methods.

### Method 3 — Peer revenue aggregation (partial — data gap, flagged)

Shyam's closest competitive set is not the flat-dominant majors (JSW Steel, Tata Steel, SAIL, AM/NS India, JSPL — all far larger and flat/auto/rail-weighted) but mid-cap, sponge-iron-integrated players: Rashmi Metaliks/Group (2.18 MTPA DRI — India's #6 DRI producer, per web search aggregation), Sarda Energy & Minerals, Jai Balaji Industries, Godawari Power & Ispat, Kirloskar Ferrous, Tata Metaliks, MSP Steel, Electrosteel Castings (long/sponge-iron peers); IMFA (ferro alloys); Jindal Stainless (stainless steel). **Individual FY26 revenue figures for this peer basket were not pulled this run** (out of scope for a single-pass web search) — this is a genuine input gap. Directionally, trade commentary suggests this mid-cap peer basket plus an unorganised/induction-furnace long-steel and ferro-alloys tail (commonly cited 30–40% of volume in trade press, **NOT FOUND** a single AR-anchored precise %) collectively occupy the balance of the Method 1/2 TAM not held by the flat-dominant majors. **Method 3 is retained as a qualitative cross-check only this run (confidence LOW), not a standalone TAM line.**

### Method 4 — Import substitution (directional, non-additive)

FY24-25 recorded steel imports of **9.5 million tonnes — the highest in nearly a decade** [AR FY24-25 pg65, citing PIB], triggering a 12% provisional safeguard duty from April 2025. At Shyam's carbon-steel realization: 9.5 Mt × ₹43,043/t = **₹4,08,909 Cr** of import value now facing tariff protection. This volume is already embedded inside the 137.8 Mt consumption figure used in Method 1 — it is **not additive** to the TAM; it is presented here as a growth-driver signal (Section 4A) showing the scale of the domestic-substitution opportunity behind the new duty.

### Method 5 — Global per-capita benchmark (forward-looking, directional)

India per-capita finished steel consumption ≈ **103–108 kg** vs global average **~215 kg** vs China **~601 kg** [web search aggregation of Ministry of Steel/worldsteel-sourced commentary, 2025 vintage — consistent order of magnitude with the AR's own cited 2017 baseline of 61 kg and NSP 2030-31 target of 158–160 kg, AR pg65 / steel.gov.in]. National Steel Policy (NSP) 2017 targets 300 MT capacity / 255 MT production / 158–160 kg per-capita consumption by 2030-31, requiring ~₹10 lakh crore of incremental investment [IBEF, PIB]. Applying Method 1's realization and product-fit logic to the NSP's own 2030-31 production target: 255 Mt × 0.50–0.55 × ₹43,043/t = **₹5,48,798 – ₹6,03,678 Cr** — a forward-looking (2030-31), not current-year, carbon-steel-equivalent TAM, shown for context only and not blended into the triangulation table below (it is a different time horizon).

### Triangulation table

| Method | Estimate (₹ Cr) | Confidence | Staleness |
|---|---|---|---|
| 1. Top-down, conservative | 4,24,060 | M | Mixed: AR FY24-25 (<1yr as of run date), ISSDA/BigMint/DataBridge web data (2025, <1yr) |
| 1. Top-down, realistic | 4,84,690 | M | same |
| 2. Bottom-up, full-penetration ceiling | 7,51,600 | L | same — upper bound only, not headline |
| 2. Bottom-up, disciplined | 4,24,060 (= Method 1 conservative) | M | same |
| 3. Peer aggregation | Not computed — data gap | L | qualitative cross-check only |
| 4. Import substitution | Not additive; informs Section 4A only | M | AR FY24-25, <1yr |
| 5. Global benchmark (forward, FY30-31) | 5,48,798–6,03,678 (different horizon, not blended) | L | NSP 2017 target is **STALE** (>4yrs old as a policy document) but still the active operative government target, frequently reaffirmed in 2025 industry commentary — informs direction only per the staleness rule |

**Conservative TAM (current-year) = ₹4,24,060 Cr**
**Realistic TAM (current-year) = ₹4,84,690 Cr**

### Management's claim vs. conservative estimate

No independent TAM claim exists to test (per Section 1B). Using the only quantified forward claim available — FY31E revenue target ₹42,500 Cr — as a proxy: **ratio = 42,500 / 4,24,060 ≈ 0.10x (10%)**. This is structurally different from the standard "TAM inflation" test (which compares a stated TAM claim to an independent TAM estimate); here it is a revenue-target-to-TAM ratio, which is naturally well under 1x. Read: **management's implied 10% terminal share of the triangulated conservative TAM by FY31 is not aggressive** for a company that is already India's 6th-largest steel producer — this reads as **conservative**, not inflated, consistent with the absence of any TAM-inflation slide in the deck.

---

## SECTION 3: SAM & SOM

### 3A — SAM (five filters applied to conservative TAM, ₹4,24,060 Cr)

1. **Product fit**: Method 1's carbon-steel component already applies the long-vs-flat haircut, so no further cut is needed there. A further **10% haircut** is applied for portions still pre-commercial across all four segments — HR flat mill (₹5,304 Cr of ₹5,400 Cr budgeted capex still pending, IR Day pg30) and aluminium FRP/battery-foil scale-up (₹800 Cr total capex; foil facility commissioned only 16-Jul-2026, FRP due end-Sep-2026, per operator context) — since these are named, funded, but not yet revenue-generating at scale. 4,24,060 × 0.90 = **₹3,81,654 Cr**.
2. **Geography**: No subtraction. The underlying TAM lines (ferro-alloys, aluminium foil) were built on India-domestic demand/market-value bases; Shyam's export revenue (10% of FY26 total, 52% of ferro-alloys, >60% of aluminium-foil production) sits *outside* this India TAM and is additive, not subtractive — treated as an SAM-expansion lever in 5D, not a filter here.
3. **Channel**: No subtraction — direct industrial contracts plus the SEL Tiger distributor network already cover the relevant retail and B2B channels for the product categories defined in 1A.
4. **Customer**: No subtraction against the ₹3,81,654 Cr base — the wagon-manufacturing entry into Indian Railways as a wholly new customer segment (₹1,788 Cr FY31E target) is not counted in any TAM line above and is treated purely as an SAM-expansion lever (5D) to avoid double-counting.
5. **Capability**: No SAM cut — capacity is a SOM-stage constraint (3C below), not a market-definition filter.

**SAM = ₹3,81,654 Cr (90.0% of conservative TAM)**

### 3B — SOM at 3 and 5 years

**Current SAM share** = FY26 revenue ₹18,552 Cr ÷ SAM ₹3,81,654 Cr = **4.86%**.

**Share-gain trajectory**: Shyam's capacity is expanding 16.78 → ~27 MTPA (+61%) on ₹13,902 Cr of named, partly-incurred capex (₹3,285 Cr / 24% already spent), alongside an explicit mix-shift into higher-EBITDA/tonne segments (stainless 7%→28% of FY31E revenue share, SBQ 0%→11%, wagons 0%→4%, per IR Day pg47). This is capacity-and-execution-backed, qualifying for the stage's "3–5pp aggressive" share-gain band (not the 1–2pp normal band).

- **3-year SOM (≈FY29)**: +2.5pp share gain → 4.86% + 2.5% = 7.36% of SAM. **SOM_3yr = 0.0736 × 3,81,654 = ₹28,090 Cr.**
  Implied revenue CAGR: (28,090 / 18,552)^(1/3) − 1 = **~14.8%**.
- **5-year SOM (≈FY31, matching management's own Vision-2031 horizon)**: +4pp share gain → 4.86% + 4% = 8.86% of SAM. **SOM_5yr = 0.0886 × 3,81,654 = ₹33,815 Cr.**
  Implied revenue CAGR: (33,815 / 18,552)^(1/5) − 1 = **~12.7%**.

**Cross-check against management's own FY31E revenue target (₹42,500 Cr, ~18% CAGR)**: the bottom-up SOM-implied 5-year figure (₹33,815 Cr, 12.7% CAGR) is **~₹8,500–₈,700 Cr lower** than management's guided target. This is a genuine, material divergence. Drilling into the segment table (IR Day pg47) shows it is concentrated almost entirely in **stainless steel**: management targets sales volume of 6,99,733 tonnes by FY31E, up from 94,102 tonnes FY26 (+643%, ~49% volume CAGR per IR Day pg20) — against ISSDA's own **India-wide** industry capacity target of just 9.3–9.5 million tonnes by 2030. That would imply Shyam alone accounts for ~7.4% of *all of India's* stainless steel capacity by 2030 — a large but not impossible ask given the segment's real, largely-funded capex (₹2,940 Cr budgeted for stainless-flat capacity, 1.38 MTPA incremental, IR Day pg32) and Danieli-built rolling technology (IR Day pg11). **Read: management's plan is the more optimistic side of this divergence, concentrated in a single segment's aggressive volume ramp — flagged explicitly for stage 11's cross-check of revenue-growth assumptions.**

### 3C — Capacity cross-check

Installed metal capacity FY26 = 16.78 MTPA; Vision-2031 target = ~27 MTPA (+61%, IR Day pg15/pg46), implying a **~10% capacity-tonnage CAGR** over FY26–FY31. Against the bottom-up 5-year SOM's **12.7% revenue CAGR**, this is capacity-consistent — revenue can outgrow tonnage modestly given the stated mix-shift toward higher-EBITDA/tonne segments, so **no gap flagged on the SOM side**.

Against **management's own** FY31E revenue target (18% CAGR), the tension surfaces specifically in stainless steel: 6,99,733 tonnes of FY31E sales volume against only 0.6 MTPA (600,000 TPA) of installed stainless-steel *finishing* capacity by FY31E (IR Day pg36) — i.e., >100% of single-stage nameplate on an annualized run-rate basis, before accounting for multi-stage process yield (melt shop → HR → CR are separate capacity lines, so "sales tonnes" is not a direct 1:1 read against any single nameplate figure; this is a reconciliation gap in the two-page extract available this run, not a confirmed hard contradiction).

**capacity_check: gap of ~₹8,500 Cr between bottom-up SOM (₹33,815 Cr, 5yr) and management's FY31E revenue target (₹42,500 Cr); management's plan is the more optimistic side, concentrated in the stainless steel volume ramp (94,102t FY26 → 699,733t FY31E target against 0.6 MTPA nameplate SS finishing capacity) — flagged for stage 11.**

---

## SECTION 4: GROWTH DRIVERS, RISKS & STRUCTURE

### 4A — TAM growth drivers

| Driver | Impact | Evidence |
|---|---|---|
| Penetration / per-capita | HIGH | India steel consumption ~103–108 kg/capita vs global 215 kg vs China 601 kg; NSP 2017 targets 158–160 kg by 2030-31 vs 61 kg baseline [AR pg65, web search] |
| Premiumisation / mix-shift | MEDIUM | Company's own pivot: stainless 7%→28% of FY31E revenue share, SBQ 0%→11% [IR Day pg47] riding a broader India trend toward higher-spec steel demand (auto, white goods) |
| Formalisation | MEDIUM | QCO (Quality Control Order) to add 1,000 more mandatory-BIS-certified steel grades (from 1,376 items currently regulated), disfavouring unorganised producers [AR pg64, Steel Ministry/PIB] |
| Regulatory tailwind | HIGH | 12% provisional safeguard duty on steel imports (Apr-2025); PLI 2.0 for specialty steel, ₹6,322 Cr outlay targeting 42 MT by FY26-27; ₹10.2 lakh crore infra budget; GoI circular mandating stainless steel on national highway bridges in corrosive/marine settings [AR pg62/64/65, IR Day pg19] |
| Import substitution | MEDIUM-HIGH | Record 9.5 MT steel imports FY24-25 (highest in a decade) now facing tariff protection [AR pg65] |
| New applications | MEDIUM | EV battery-grade aluminium foil (5,000 TPA, ₹25 Cr capex), stainless in defence/railways/engineering per Vision-2031 focus, wholly-new wagon-manufacturing line [IR Day pg23/pg46, operator context] |
| Geographic expansion | MEDIUM | Export footprint 23→40+ countries in one year (FY25→FY26); 10% of FY26 revenue exported; ferro-alloys 52% export mix, aluminium foil >60% of production exported [IR Day pg12/pg15] |
| Technology enablement | MEDIUM | Danieli (Italy)-built stainless rolling mill; Achenbach (Germany)-installed foil line; 0.125mm-gauge CRM at Jamuria vs 0.22mm industry-typical, giving a captive Northeast-India position [IR Day pg11/pg19] |
| Demographics / urbanisation | HIGH | Construction is ~41.9% of India's domestic steel demand (web search); India real-estate market projected to reach $5.8 trillion by 2047 [AR pg65, NAREDCO/Knight Frank] |

### 4B — TAM risks

| Risk | Monitoring signal |
|---|---|
| Cyclical downturn | World steel consumption fell for a 3rd straight year in 2024 (−0.9%, AR pg63) even as India bucked the trend (+8%); a China-style slowdown is the primary macro risk. Watch: China steel demand, global HRC pricing, India capacity utilisation |
| Import competition | Despite the new 12% safeguard duty, FY24-25 saw the highest imports in nearly a decade (9.5 Mt, AR pg65). Watch: safeguard-duty renewal, Chinese/Korean/Japanese export pricing |
| Trade tensions | US 25% steel tariff risks redirecting global excess capacity toward Asia including India (AR pg66, "Threats" section). Watch: US/EU trade policy, ASEAN steel flows |
| Regulatory/environmental restriction | CPCB closure directions (Apr-2026) against one pellet plant, ferro-alloys plant, and power plant at Rengali/Sambalpur for pollution non-compliance, later granted conditional relief (operator context, NOT anchored to a filed PDF this run — company-specific execution risk, but signals sector-wide tightening). Watch: CPCB/state pollution board actions across ferro-alloys/steel peers |
| Saturation | ISSDA's own India stainless capacity target (9.3–9.5 Mt by 2030) is a near-doubling of *industry* capacity against 7–8% demand growth — risk of margin compression if multiple players (Jindal Stainless, Shyam, others) execute simultaneously. Watch: sector-wide capacity announcements vs. ISSDA demand print |
| Substitution | Aluminium/composite lightweighting is a slow-moving structural risk to select carbon-steel end-uses; largely internally hedged for Shyam given its own aluminium exposure. Impact: LOW for Shyam specifically |

### 4C — Market structure

- **Concentration**: Per IR Day's own competitor slide (pg55), the top-3 by capacity (JSW Steel 51.5 MTPA, Tata Steel 40.0 MTPA, SAIL 35.0 MTPA) alone dwarf India's ~200–235 MT installed base's mid-tier; Shyam appears on the same slide at 11.6 MTPA (2026 figure) which is **inconsistent with the 16.78 MTPA installed-capacity figure cited elsewhere in the same deck** (pg15) — flagged as a source-data-quality note within the IR Day materials, not resolved this run.
- **Organised vs. unorganised**: Meaningfully unorganised in secondary/induction-furnace long steel and ferro-alloys (commonly cited 30–40% in trade press; **NOT FOUND** a single AR-anchored precise %). QCO/BIS certification expansion (4A) is actively formalising this.
- **Consolidating or fragmenting**: Consolidating at the top (named large-player capacity expansion under NSP tracking, Shyam included); a long fragmented tail of small induction-furnace units persists beneath it.
- **Price vs. differentiation**: Predominantly price-competition in commodity carbon steel (price-taker, per B04); differentiation is emerging at Shyam's targeted higher end (stainless, SBQ auto-grade, EV battery foil, thin-gauge CRM) — an explicit, capex-backed company strategy to migrate up this axis.
- **Entries and exits**: New capacity entry dominates (Shyam's own ₹13,902 Cr programme is itself an entry into HR flat, SBQ, stainless-flat, and wagons); no major exits identified in the materials reviewed this run.
- **Import share trend**: Rising sharply into FY24-25 (9.5 Mt, highest in a decade) ahead of the April-2025 safeguard duty; post-duty trend is the key thing to watch going forward.

---

## SECTION 5: SUMMARY & RUNWAY

### 5A — Funnel

```
TAM (conservative)      ₹4,24,060 Cr
   ↓ (5 filters: −10% product-fit for pre-commercial HR-flat/aluminium-FRP scale)
SAM                      ₹3,81,654 Cr   (90.0% of TAM)
   ↓ (current share 4.86%)
Current revenue (FY26)   ₹18,552 Cr    (4.86% of SAM, 4.37% of conservative TAM)
   ↓ (+2.5pp aggressive share gain, 3yr)
SOM 3yr (≈FY29)          ₹28,090 Cr    (7.36% of SAM; implied 14.8% revenue CAGR)
   ↓ (+4pp aggressive share gain, 5yr)
SOM 5yr (≈FY31)          ₹33,815 Cr    (8.86% of SAM; implied 12.7% revenue CAGR)
```

### 5B — Runway assessment

- **Revenue headroom** = SAM ÷ current revenue = 3,81,654 / 18,552 = **~20.6x**.
- **TAM growth rate**: India steel-industry growth moderated to 6.8% in FY24-25 (from 16.9%/9.3%/12.5% in the three prior years, AR pg64, PIB); blended with stainless (7–8%, ISSDA), ferro-alloys (7–8%, BigMint), and aluminium foil (6.4% CAGR 2026-33, industry report) — a reasonable blended headline is **~7% CAGR**.
- **Company CAGR vs. TAM**: Shyam's own trailing 20-year revenue CAGR is 20% (IR Day pg5); its forward Vision-2031 guide is 18% (IR Day pg46) — both far exceed the ~7% blended TAM growth rate. Shyam is **gaining share, not merely riding the market**, consistent with its capacity-doubling capex programme.
- **Years to saturate SAM**: at management's own 18% company CAGR against a static ₹3,81,654 Cr SAM: ln(20.57)/ln(1.18) ≈ **18.3 years**. Adjusting for the SAM's own ~7% concurrent growth (net growth differential ~11pp): ln(20.57)/ln(1.11) ≈ **29 years**. Either way, SAM saturation is a distant, non-binding constraint over the 3–5 year investment horizon relevant to this pipeline.

### 5C — Runway classification

Revenue headroom (~20.6x) is large by any reasonable band, and the underlying multi-segment India metals TAM has genuine multi-decade structural tailwinds (per-capita steel consumption roughly half the global average, NSP 2030-31 targets not yet reached). However, the TAM/SAM derivation rests on a directional, non-AR-sourced 50–55% long-vs-flat product-scope haircut (Method 1) that could not be independently verified this run, and Method 3 (peer aggregation) is a genuine data gap. Per the pipeline's conservative-bias rule, this report classifies runway as:

**runway_class = STRONG** (not MASSIVE) — the headroom multiple alone would support MASSIVE, but estimation uncertainty in the underlying product-scope split argues for the more conservative call.

### 5D — SAM expansion levers actually being pursued

1. **HR flat steel mill** (1.58 MTPA, ₹5,400 Cr budgeted, ₹5,304 Cr pending) — would add back some/all of the ~₹2,96,000–3,26,000 Cr flat-steel TAM excluded by Method 1's product-fit haircut, as this ramps [IR Day pg30].
2. **Stainless steel flat** (CRM, precision CRM, HR annealing/pickling, bright annealing — ₹2,940 Cr budgeted, 0.5→0.6 MTPA plus new flat capability) — deepens penetration of the already-counted ₹67,413 Cr stainless SAM and opens flat-SS auto/white-goods/construction adjacencies [IR Day pg29/pg32/pg36].
3. **Aluminium FRP + EV battery foil** (₹800 Cr total capex: mill+caster ₹75 Cr, FRP ₹450 Cr, foil ₹250 Cr, battery foil ₹25 Cr) — adds a wholly new product line (EV battery materials) with no precedent revenue base [IR Day pg23, operator context].
4. **Railway wagon manufacturing** (4,800 wagons/yr, ₹200 Cr capex, Kharagpur; Phase-I targeted Sep-2026 per operator context) — an entirely new customer segment (Indian Railways/rolling-stock OEMs); FY31E revenue target ₹1,788 Cr [IR Day pg26/pg47].
5. **Geographic/export expansion** (23→40+ countries in one year) — extends the addressable market beyond the India-only TAM computed above; already monetised in ferro-alloys (52% export) and aluminium foil (>60% of production exported), with further scale-up a stated Vision-2031 pillar [IR Day pg12/pg46].

Summed, management's own segment table implies **~₹19,118 Cr** of incremental FY26→FY31E revenue across carbon steel (+₹5,173 Cr), stainless (+₹10,647 Cr), and aluminium (+₹1,510 Cr), plus wagons (+₹1,788 Cr) [arithmetic from IR Day pg47]. A fully illustrative revised SAM incorporating flat-steel add-back (+₹2,96,566 Cr low end) would be ≈₹6,93,220 Cr, lowering current SAM share to ~2.7% and raising headroom to ~37x — presented as **directional only**; the incremental wagon/EV-battery-foil TAM itself is **NOT FOUND** independently this run (India rolling-stock and EV-battery-foil market sizing were not pulled).

### 5E — Final output card

- TAM (conservative / realistic): **₹4,24,060 Cr / ₹4,84,690 Cr**
- SAM: **₹3,81,654 Cr** (90.0% of conservative TAM)
- SOM 3yr / 5yr: **₹28,090 Cr / ₹33,815 Cr**
- SOM-implied revenue CAGR 3yr / 5yr: **14.8% / 12.7%**
- Current SAM share: **4.86%**
- Revenue headroom: **~20.6x**
- Runway class: **STRONG**

> "At **12.7%** revenue CAGR implied by SOM (5-year, bottom-up), with margin trajectory of **~15%** EBITDA margin (FY26 operating EBITDA margin 12.6% → Vision-2031 target ~15%, IR Day pg46), the earnings growth embedded here is **~16.8%** CAGR (EBITDA growing faster than revenue on margin expansion), which [**NOT FOUND — current market P/E multiple was not supplied to stage 9; stage 11/13 to complete this comparison**] the current valuation of **__x P/E**. Note: management's own guide is more aggressive on both counts (18% revenue CAGR, ~22% EBITDA CAGR to FY31E) — see the Section 3B divergence flag on the stainless-steel volume ramp."

---

## Search log

**Searches performed** (11 web searches + 1 web-fetch attempt):
1. "India steel market size 2025 2026 Rs crore CRISIL IBEF industry report"
2. "India stainless steel market size 2025 IBEF ISSDA crore tonnes"
3. "India ferro alloys market size 2025 exports tonnes crore"
4. "India aluminium foil market size 2025 crore tonnes FRP"
5. "India per capita steel consumption 2025 kg vs China global average"
6. "India long steel products TMT wire rod market size crore 2025"
7. "USD INR exchange rate July 2026"
8. "India HRC hot rolled coil steel price per tonne 2026 domestic"
9. "India sponge iron DRI integrated steel producers market size mid-cap Rashmi Metaliks Jai Balaji Sarda Energy revenue 2025"
10. "National Steel Policy 2017 India 300 million tonnes 2030-31 target steel demand"
11. "'specialty alloys' OR 'ferro chrome' India market size India domestic consumption 2025 2026"
12. WebFetch of steel.gov.in Overview-of-Steel-Sector PDF — **failed, HTTP 403** (not retried; AR's own citations of the same underlying Ministry of Steel data were used instead)

**Searches skipped** (forced by scope/time — this is what makes status PARTIAL):
- Peer-by-peer FY26 revenue pull for Rashmi Metaliks, Sarda Energy & Minerals, Jai Balaji Industries, Godawari Power & Ispat, Jindal Stainless (Method 3 aggregation) — retained as qualitative-only cross-check, LOW confidence, flagged as an input gap.
- India rolling-stock/wagon-manufacturing market size and India EV-battery-foil market size (would refine Section 5D's illustrative SAM-expansion figure) — not pulled this run.
- Current market P/E multiple for SHYAMMETL (needed to complete the Section 5E valuation-implication sentence) — not supplied to stage 9 and not independently pulled (out of stage-9 scope per the stage's own definitional focus on TAM/SAM/SOM, not live market pricing).

---

```yaml
stage: B09-tam
company: "SHYAMMETL"
run_date: "2026-07-19"
model: claude-sonnet-5
status: partial
input_gaps:
  - "peer FY26 revenue figures for Method 3 aggregation (Rashmi Metaliks, Sarda Energy, Jai Balaji, Godawari Power, Jindal Stainless)"
  - "precise long-vs-flat steel product split for India finished steel consumption (used a directional 50-55% analyst estimate)"
  - "unorganised-sector % for India long steel / ferro alloys (commonly cited 30-40% in trade press, no single AR-anchored figure found)"
  - "current market P/E multiple for SHYAMMETL (needed for Section 5E valuation-implication sentence, not supplied to stage 9)"
  - "India rolling-stock and EV-battery-foil market sizing (would refine SAM-expansion illustrative figure in 5D)"
flags:
  - "No explicit management TAM claim found in AR/IR-Day extracts; used FY31E revenue roadmap (Rs42,500cr) as the only quantified forward claim for the mgmt_claim test - not a like-for-like TAM comparison"
  - "Long-vs-flat steel product-scope split (50-55% assumed) for Method 1 top-down TAM is a directional analyst estimate, not directly sourced - flagged LOW-MEDIUM confidence"
  - "Bottom-up 5yr SOM (Rs33,815cr, 12.7% CAGR) is below management's own FY31E revenue target (Rs42,500cr, 18% CAGR) by ~Rs8,500-8,700cr / ~5pp CAGR, concentrated almost entirely in the stainless steel segment's aggressive volume ramp (94,102t FY26 -> 699,733t FY31E target vs 0.6 MTPA nameplate SS finishing capacity) - flagged for stage 11 cross-check of revenue growth assumptions"
  - "Method 3 peer revenue aggregation not completed this run (no company-by-company FY26 financials pulled) - retained as qualitative cross-check only, LOW confidence"
  - "IR Day deck shows an internal capacity-figure inconsistency: 11.6 MTPA on the 'Rising Force' competitor-comparison slide (pg55) vs 16.78 MTPA cited elsewhere in the same deck as FY26 installed capacity (pg15) - not resolved this run"
  - "USD/INR rate used for third-party market-value conversions (aluminium foil, stainless steel) was ~96.4 (18-Jul-2026 spot); using the FY26 average of ~93.3 instead would lower converted figures by ~3%"
market_definition: "Indian carbon steel (long+flat), stainless steel, ferro alloys, and aluminium foil/FRP markets addressable by Shyam's current and committed product portfolio"
tam_cr: {conservative: 424060, realistic: 484690}
sam_cr: 381654
sam_pct_of_tam: 90.0
som_3yr_cr: 28090
som_5yr_cr: 33815
som_implied_revenue_cagr: {yr3: 14.8, yr5: 12.7}
current_sam_share_pct: 4.86
revenue_headroom_x: 20.6
tam_growth_pct: 7
runway_class: "STRONG"
mgmt_claim_cr: 42500
mgmt_claim_ratio: 0.10
mgmt_claim_read: "conservative"
capacity_check: "gap of ~Rs 8,500 Cr between bottom-up 5yr SOM (Rs33,815cr) and management's FY31E revenue target (Rs42,500cr); management's plan is the more optimistic side, concentrated in the stainless steel volume ramp (94,102t FY26 sales -> 699,733t FY31E target vs 0.6 MTPA nameplate SS finishing capacity) - flagged for stage 11"
methods_used:
  - "top-down (industry volume x Shyam's own realization, with product-fit subtractions)"
  - "bottom-up (addressable-unit x penetration, full-penetration ceiling and disciplined variants)"
  - "peer aggregation (qualitative cross-check only - data gap)"
  - "import substitution (directional growth-driver signal, non-additive to TAM)"
  - "global per-capita benchmark (forward-looking FY30-31 context, not blended into current-year TAM)"
stale_data_flags:
  - {datapoint: "National Steel Policy 2017 target (300MT capacity, 158-160kg per capita by 2030-31)", source: "steel.gov.in / PIB, cited via AR FY24-25 footnote", year: 2017}
  - {datapoint: "India DRI producer capacity ranking (Shyam #5 nationally at 2.71 MTPA)", source: "web search aggregation of industry trackers", year: 2024}
searches_performed:
  - "India steel market size 2025 2026 Rs crore CRISIL IBEF industry report"
  - "India stainless steel market size 2025 IBEF ISSDA crore tonnes"
  - "India ferro alloys market size 2025 exports tonnes crore"
  - "India aluminium foil market size 2025 crore tonnes FRP"
  - "India per capita steel consumption 2025 kg vs China global average"
  - "India long steel products TMT wire rod market size crore 2025"
  - "USD INR exchange rate July 2026"
  - "India HRC hot rolled coil steel price per tonne 2026 domestic"
  - "India sponge iron DRI integrated steel producers market size mid-cap Rashmi Metaliks Jai Balaji Sarda Energy revenue 2025"
  - "National Steel Policy 2017 India 300 million tonnes 2030-31 target steel demand"
  - "specialty alloys OR ferro chrome India market size India domestic consumption 2025 2026"
  - "WebFetch: steel.gov.in Overview of Steel Sector PDF (failed, HTTP 403)"
searches_skipped:
  - "peer-by-peer FY26 revenue pull for Rashmi Metaliks / Sarda Energy / Jai Balaji / Godawari Power / Jindal Stainless (Method 3 aggregation) - skipped due to scope of a single-pass web-search run"
  - "India rolling-stock / wagon-manufacturing market size and India EV-battery-foil market size - not pulled this run"
  - "current market P/E multiple for SHYAMMETL - not pulled, out of stage-9 TAM/SAM/SOM scope"
```
