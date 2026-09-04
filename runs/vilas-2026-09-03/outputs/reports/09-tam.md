# STAGE 9 — TAM / SAM / SOM MARKET SIZING
**Company:** Vilas Transcore Limited (VILAS) | **Run date:** 2026-09-03 | **Model:** claude-sonnet-5

---

## SECTION 1: MARKET DEFINITION

### 1A. Precise boundaries

**Core market (the pool VILAS actually fishes in, ~98% of FY26 revenue):**
India CRGO (Cold Rolled Grain Oriented electrical steel) **lamination and core processing market** — the
revenue earned by domestic processors who buy imported (and the small domestic-produced) CRGO coil,
slit/shear/stack it into transformer laminations, cores, coil-core assemblies and shielding, and sell to
transformer OEMs.

- **Product scope:** CRGO slit coils, laminations, stacked/wound cores, core-coil assemblies, magnetic
  shielding — the magnetic-core value-add step of transformer manufacturing. Excludes the transformer
  itself (windings, tank, oil, bushings, switchgear) except where VILAS itself is entering those lines
  (sized separately below).
- **Geographic scope:** India-consumed CRGO tonnage. VILAS's direct exports (Gulf, Europe, Canada) were
  ~₹6.0 Cr in FY25 (AR Note 34, FOB) and ~1.3% of FY25 revenue — immaterial to the core TAM today, treated
  as an SAM-expansion lever in 5D, not baked into the headline India TAM.
- **Customer scope:** Transformer OEMs (power, distribution, EPC-supplied) and, on a much smaller scale,
  renewable-evacuation and railway-electrification equipment makers.
- **Channel scope:** Direct B2B supply to OEMs; no retail/distributor layer.
- **Price segment:** Spans standard distribution-transformer-grade laminations through higher-kV,
  precision-cut laminations for power transformers; excludes HVDC-grade converter-transformer cores,
  which sit with a small number of globally qualified suppliers VILAS is not yet approved for
  (PGCIL approval pending — B01 anchor, B07 flags).
- **Explicit exclusions:** Copper/aluminium windings, transformer tanks, insulating oil, switchgear,
  and (for the core TAM only) nanocrystalline cores, radiators, copper conductors and HV bushings —
  these four adjacencies are sized as separate, non-blended pools in the section below per the run
  instructions, because each carries a different proof status (Amendment 18: no blending unresolved
  optionality into one number).

### 1B. Management's own TAM claim, tested

Management does **not** state a rupee CRGO/lamination-market TAM anywhere in the FY26 Investor
Presentation. The presentation's "Industry Overview" section (slides 24-25, sourced "CEA, Public
Reports") gives macro backdrop only: ~₹9+ lakh crore T&D capex through 2032, transmission capacity
~1,451 GVA (FY26) → ~2,412 GVA (FY32E), industry transformer capacity ~375 GVA (FY25) → ~650 GVA (FY27E),
~32 GW HVDC pipeline. None of these numbers is VILAS's addressable pool; they are demand-driver context
(used in Section 4A below).

The closest thing to an explicit market-opportunity claim sits in the **FY24-25 Annual Report**, MD's
Message (p.2) and MD&A Annexure IV (p.34, sourced there to "IMF, PIB" for the macro paragraph and
separately "IMARC, World Bank, KNN" for the industry paragraph, with no single footnote tied to this
specific figure): *"India's transformer market, estimated at USD 5.1 billion in 2024, is projected to
grow at a CAGR of 7.9% to reach USD 7.44 billion by 2029."*

**Credibility read: BROAD.** This is the *entire Indian transformer market* (windings, tanks, oil,
bushings, cores, assembly — everything), not the CRGO-lamination-processing slice VILAS actually
monetises. Citing the whole transformer industry as "the opportunity" while VILAS sells one input
component into it is the exact TAM-inflation pattern the framework asks this stage to test, not accept.
Tested against Section 2's independent triangulation below (mgmt_claim_ratio ≈ 4.7x conservative TAM,
read: inflated by definition-mismatch, not necessarily by number).

---

## SECTION 2: TAM ESTIMATION — CORE (India CRGO lamination/core processing)

**Method 1 — Top-down (transformer market minus non-core cost share).**
Independent web-search cross-checks on "India transformer market 2024" return a **wide, genuinely
divergent** range depending on scope: IMARC's *power-transformer-only* estimate is USD 2.3 Bn (2024);
a broader "India transformers market" (power + distribution + current + instrument) estimate from
Market Data Forecast-type aggregators runs USD 2.6-2.78 Bn (2024/FY24) to USD 5.34-5.6 Bn by 2032-34
at 7.6-8.5% CAGR (WebSearch, 2026-09-03, multiple aggregator sites — MODERATE confidence, wide
dispersion across vendors is itself a data-quality signal, not a single clean number).
Taking VILAS's own AR-cited USD 5.1 Bn (2024) as the top of a reasonable transformer-market range and
converting at ~₹83.5/USD (2024 average) gives **≈₹42,600 Cr** total transformer-market value (2024).
Core-steel material cost is documented industry-wide at **20-25% of a transformer's total manufacturing
cost** (WebSearch, taishantransformer.com cost-breakdown analyses, generic/global source, MODERATE
confidence — flagged as a directional industry rule of thumb, not India-audited data): a 33kV/10MVA
unit runs ~20% core-steel, a 220kV/100MVA unit ~25%.
Applying 20-25% to ₹42,600 Cr: **₹8,520 Cr – ₹10,650 Cr** implied core/lamination value embedded in the
Indian transformer market (2024).

**Method 2 — Bottom-up (national CRGO tonnage × realised processing price).**
India's annual CRGO consumption is independently sized at **~400,000-450,000 MT**, against domestic
production of only ~40,000-50,000 MT from the sole domestic mill (JSW JFE Electrical Steel, Nashik) —
i.e. **~90% import dependence** (WebSearch, 2026-09-03: GTRI commentary reported by Deccan Chronicle
and KNN India on the DGTR anti-dumping investigation into CRGO imports from China/Japan/South
Korea/Russia, initiated 22-Jun-2026, injury period FY22-23 to FY24-25 — HIGH-confidence *filing*, but
the specific tonnage figure is anchored to an **FY23-24 baseline**, now >2 years old vs. this run's
date — **STALE** flag per the staleness rule; direction only, not the exact current-year number).
VILAS's own realised processed-lamination price is derivable from its financials: FY25 CRGO revenue
₹301.7 Cr / 12,069 MT ≈ ₹2,50,000/MT; FY26 (Ind AS, price trough) CRGO revenue ≈₹457 Cr / ~19,826 MT
≈₹2,30,600/MT (both anchored to AR Note 23 p.66 and FY26 Investor Presentation slides 6/7/20 —
DOCUMENTED). Applying a ₹2.3-2.5 lakh/MT blended national realisation to 400,000-450,000 MT:
**₹9,200 Cr – ₹11,250 Cr**. This converges well with Method 1's ₹8,520-10,650 Cr range — good
triangulation on the *full* national CRGO-processing value (both in-house and third-party).

**Method 3 — Peer revenue aggregation (organised segment only, LOW confidence — data too thin
for a headline number, used as a floor sanity-check).**
Named organised CRGO-lamination players and FY25 revenue: VILAS ₹460.7 Cr (FY26; total company);
Jay Bee Laminations Ltd ₹367.5 Cr (FY25, +21% YoY; H1 FY26 ₹218.7 Cr, +43% YoY — WebSearch,
marketscreener.com/multibagg.ai, 2026-09-03); Kryfs Power Components Ltd (unlisted) ₹1,445 Cr (FY25,
+28% YoY — WebSearch, thecompanycheck.com/acuite.in, 2026-09-03, **blended** CRGO-lamination +
transformer-manufacturing + EPC, CRGO-only portion not disclosed, apply a heavy haircut); Pitti
Engineering Ltd ₹1,743 Cr (FY25 — WebSearch, 2026-09-03, **blended** with motor laminations, castings,
machining; CRGO-transformer-lamination share likely a minority, heavy haircut). Even after generous
haircuts on Kryfs and Pitti's non-CRGO revenue, the four named organised players sum to roughly
₹1,800-2,500 Cr — well short of Methods 1-2's ₹8,500-11,250 Cr. The gap is explained, not contradicted:
independent search confirms the India CRGO-processing industry is "**highly fragmented**...various
organised and unorganised players" (VILAS AR MD&A p.35, echoed independently by generic industry
directories naming a dozen-plus small unlisted processors — Mehta Steels, Universal Transcore,
Banmore Core, Premier Core, Kunal Stamping, Balajee Impex, Jayant Impex, Lee Vedla, Raj Metals, none
independently sized). Per the standard India unorganised-sector uplift (30-60%), an organised base of
~₹2,000-2,500 Cr plus a large unsized long tail is directionally consistent with, but cannot
independently confirm, the ₹8,500-11,250 Cr Method 1/2 range. **This method is a floor check only,
not a headline input.**

**Method 4 — Import substitution.** Not separately modelled: Method 2 already IS an import-substitution
framing (90% import-dependent CRGO steel input; VILAS processes, does not smelt, so this method
collapses into Method 2 for a converter). A genuine import-substitution TAM would apply if a domestic
CRGO-steel mill scaled meaningfully (JSW JFE's ~40-50k MT today is 10-12% of demand); no disclosed
near-term capacity-add changes this materially in-corpus.

**Method 5 — Global benchmark.** Not decision-useful for the core India market (China dominates global
CRGO production/consumption at a scale and cost structure not comparable to India's near-total-import
model); reserved below for the thinly-documented adjacencies where India-specific data is absent.

### Triangulation table — CORE (CRGO lamination/core processing, India, ~2024/25 vintage)

| Method | Estimate (₹ Cr) | Confidence | Staleness |
|---|---|---|---|
| 1. Top-down (transformer market × core-cost share) | 8,520 – 10,650 | Moderate | 2024 data, borderline 2yr |
| 2. Bottom-up (CRGO tonnage × realisation) | 9,200 – 11,250 | Moderate-High | Tonnage anchor FY23-24, STALE |
| 3. Peer aggregation (organised only) | ~2,000 – 2,500 (floor, incomplete) | Low | Mixed FY25 filings |
| 4. Import substitution | Collapses into Method 2 | — | — |
| 5. Global benchmark | Not applicable to core | — | — |

**Conservative estimate: ₹9,000 Cr. Realistic estimate: ₹10,500 Cr** (both current-year, ~2024/25
vintage; conservative bias applied per rule — took the lower end of the Method 1/2 overlap rather
than averaging).

**Management's claim vs. conservative estimate:** ₹42,600 Cr ÷ ₹9,000 Cr = **4.7x — read: INFLATED**
by scope mismatch (whole transformer industry cited as backdrop, not the CRGO-processing slice VILAS
serves). This is not an accusation that the USD 5.1 Bn number itself is wrong — independent transformer
market estimates span USD 2.3-5.6 Bn depending on definition, so it sits within a plausible range for
*some* definition of "the transformer market." The problem is definitional: management never narrows
it to the ~20-25% core-steel slice that is VILAS's actual addressable pool.

---

## SECTION 3: SAM & SOM — CORE

### 3A. SAM — five filters applied to conservative TAM (₹9,000 Cr)

| Filter | Subtraction | Rationale | Running TAM (₹ Cr) |
|---|---|---|---|
| Start | — | Conservative TAM | 9,000 |
| 1. Product fit | −15% | Excludes HVDC-converter-transformer and very-large power-transformer core segments where global majors (Hitachi Energy, Siemens Energy-type suppliers) hold in-house/qualified-only supply; VILAS is not yet in this tier | 7,650 |
| 2. Geography | 0% | TAM already India-only; exports are additive upside (5D), not subtracted here | 7,650 |
| 3. Channel | 0% | Both VILAS and the market at large sell direct B2B to OEMs; no material channel exclusion | 7,650 |
| 4. Customer | −15% | Excludes the PGCIL-approval-gated slice (larger, high-value government/institutional and global-MNC-eligible orders) VILAS cannot yet serve (B01 anchor: PGCIL approval "in process," >12 months, unfired per B07) | 6,500 |
| 5. Capability | −20% | Excludes captive in-house CRGO processing at fully vertically integrated large OEMs (BHEL-scale, and select in-house lines at top-tier private OEMs) who do not buy third-party lamination services | 5,200 |

**SAM = ₹5,200 Cr (58% of conservative TAM).**

### 3B. SOM at 3 and 5 years — arithmetic shown

**Current SAM share:** VILAS FY26 CRGO-only revenue ≈₹457 Cr (₹460.7 Cr total FY26 revenue B00 anchor,
less ₹3.48 Cr nanocrystalline, less ~₹0.2 Cr job work — AR Note 23, Inv. Pres. slide 6).
Current share = 457 / 5,200 = **8.8%**.

**Share-gain trajectory applied:** VILAS just tripled installed CRGO capacity (12,000 → 36,000 MTPA,
Unit 3 commissioned 25-Jul-2025 — AR p.18, Inv. Pres. slides 6/12/20, DOCUMENTED-physical-build per
B07). Tripled, already-built capacity plus management's own guided 45-50% FY27 volume growth qualifies
for the "**aggressive**" 3-5pp/3-year share-gain band (not the normal 1-2pp band), per the run's
share-gain rules. Applying +4.0pp over 3 years, and an incremental +2.5pp by year 5 (the fragmented,
unorganised-tail structure documented in Method 3 gives some room for faster formalisation-driven
gain beyond year 3, though this is the weaker leg of the argument given no clean unorganised-share
percentage is independently disclosed):

- 3-year share: 8.8% + 4.0pp = **12.8%**
- 5-year share: 12.8% + 2.5pp = **15.3%**

SAM itself grows with the 8% TAM growth rate (Section 4A): SAM₃ = ₹5,200 Cr × 1.08³ = ₹6,550 Cr;
SAM₅ = ₹5,200 Cr × 1.08⁵ = ₹7,640 Cr.

- **SOM (3yr) = 12.8% × ₹6,550 Cr = ₹840 Cr**
- **SOM (5yr) = 15.3% × ₹7,640 Cr = ₹1,170 Cr**

**Implied revenue CAGR (CRGO-only, arithmetic from base ₹457 Cr):**
- 3yr: (840/457)^(1/3) − 1 = **~23%**
- 5yr: (1,170/457)^(1/5) − 1 = **~21%**

Both sit **just under** the strategy's 25% CAGR hurdle on the core CRGO business alone. This is the
central finding of this stage for CRGO: the core business, even under an aggressive capacity-justified
share-gain assumption, gets VILAS close to but not comfortably above the return hurdle — the
optionality lines (nano/radiator/copper) are not just upside, they are load-bearing for a 25%+ CAGR
case (see the blended company-level cross-check in 5E).

### 3C. Capacity cross-check

Using B07's capex_embedded_growth_pct = 46% (the growth rate stage-7 judged the installed-plus-committed
capacity base can physically support) against the SOM path:

- **3-year SOM (₹840 Cr) vs. nameplate ceiling:** 36,000 MTPA × ₹2.3-2.5 lakh/MT current realisation =
  **₹828-900 Cr** revenue ceiling at 100% utilisation. SOM₃ (₹840 Cr) sits *inside* this ceiling
  (implies ~93-99% utilisation by year 3, up from the current ~55% — B00 anchor). **Capacity is
  sufficient for the 3-year SOM; it is essentially a utilisation-fill story, not a market-share-capture
  story, which is the more conservative and more defensible read.**
- **5-year SOM (₹1,170 Cr) vs. nameplate ceiling:** exceeds the ₹828-900 Cr ceiling by an estimated
  **~₹250-300 Cr**. Closing this gap requires either (a) a CRGO price recovery materially above the
  FY26 trough (₹180-185/kg input cost, per Chairman's Message — plausible given FY26 sits at a
  cyclical low, but not evidenced in corpus as already happening), or (b) further capacity expansion
  beyond the disclosed 36,000 MTPA (no such expansion is named in corpus). **At the 5-year horizon,
  the SOM path — not the capex plan — is the optimistic side.** This is the opposite of the more
  typical finding in this framework (usually the capex plan is more optimistic than SOM); flagged
  explicitly because it cuts against the usual pattern.

---

## SECTION 4: GROWTH DRIVERS, RISKS & STRUCTURE

### 4A. TAM growth drivers

| Driver | Impact | Evidence |
|---|---|---|
| Regulatory tailwind (BIS/BEE efficiency norms tightening) | Medium-High | AR MD&A p.34-35: "Further tightening of these norms is expected in FY26," pushes demand toward high-grade, laser-processed, thin-gauge laminations — VILAS's stated strength |
| Import substitution / anti-dumping | Medium | DGTR launched anti-dumping investigation into CRGO imports (China/Japan/S.Korea/Russia), 22-Jun-2026, injury period FY22-23 to FY24-25 (WebSearch) — if duties land, raises landed CRGO cost for ALL processors (double-edged: raises VILAS's input cost too, Amendment-17-relevant) |
| New applications / geographic expansion of demand | Medium | Renewable-evacuation transformers (~280 GW renewable capacity FY26 → 500 GW target 2030, Inv. Pres. slide 24), EV charging infra, data-centre power demand, rail/metro electrification — all named end-use drivers in AR MD&A p.34-37 |
| Regulatory/policy tailwind (capex programmes) | High | PLI scheme for electrical equipment, RDSS, Gati Shakti (AR MD&A p.37); National Electricity Plan (Transmission) ~₹9.15 lakh crore capex to 2032 (WebSearch, PIB/openthemagazine.com, 2026-09-03) |
| Technology enablement | Low-Medium | Shift to compact, low-loss transformer designs increases lamination precision requirements, a moat-adjacent tailwind more than a volume driver |
| Penetration / demographics | Low direct link | Power-demand CAGR ~6-7% (Inv. Pres. slide 24, CEA) is the demand backdrop, several steps removed from CRGO tonnage |

**tam_growth_pct applied: 8%** (midpoint of the 6.9-8.5% independent transformer-market CAGR range
found in Section 2's Method 1 web search; used as a proxy for CRGO-market growth on the assumption
the ~20-25% core-cost-share stays roughly stable — a simplification, flagged).

### 4B. TAM risks

| Risk | Monitoring signal |
|---|---|
| Import competition / anti-dumping duty imposition raising ALL processors' input cost (not just VILAS's) | DGTR final finding on the 2026-launched investigation; gazette notification of any duty |
| Cyclical downturn in CRGO steel pricing (currently at a trough, ₹180-185/kg) | Sequential CRGO price and gross-margin trend (B04 must-track metric) |
| Substitution (amorphous-core transformers in distribution segment) | AR product portfolio already lists "Amorphous Core" as an existing VILAS product — a partial hedge, but amorphous adoption could shrink CRGO's addressable share of the transformer core mix over time |
| Regulatory headwind: tighter efficiency norms could also favour amorphous/nanocrystalline over CRGO in the distribution segment | BEE/BIS notification tracking |
| Saturation: transformer-market growth (~7-8.5%) is moderate, not explosive; most of VILAS's own growth must come from share gain, not market expansion | Company revenue CAGR vs. independent transformer-market CAGR, tracked yearly |

### 4C. Market structure

- **Competitor count / concentration:** Highly fragmented. Organised, independently identified peers:
  VILAS, Jay Bee Laminations (listed, IPO Sep-2024), Kryfs Power Components (unlisted, part of a larger
  transformer group), Pitti Engineering (listed, broader lamination/casting business). No single
  named competitor with a directly comparable, pure-CRGO-lamination revenue base was found
  independently disclosing a top-3 concentration figure — **DATA THIN**, treated as a gap, not
  papered over.
- **Organised vs. unorganised split:** Described independently and in the AR as "highly fragmented...
  organised and unorganised players" with a long tail of small named processors (Mehta Steels,
  Universal Transcore, Banmore Core, Kunal Stamping, Balajee Impex, Jayant Impex, Lee Vedla, Raj
  Metals — WebSearch, 2026-09-03). No independently sourced organised/unorganised revenue-split
  percentage was found; the standard 30-60% unorganised-uplift convention was applied *qualitatively*
  in Method 3, not as a precise split.
- **Consolidating or fragmenting:** Directionally consolidating at the top (VILAS tripling capacity,
  Jay Bee and VILAS both recently IPO'd, suggesting organised-tier capital access is widening the gap
  with unorganised small processors) — inference, not independently confirmed.
- **Price vs. differentiation competition:** Commodity-price-taker dynamic on the CRGO input side
  (Amendment 17 converter classification, carried from B00/B04); differentiation is on precision,
  turnaround time, and OEM-qualification history (AR MD&A p.35: "capability to deliver
  transformer-grade, high-precision output at scale remains limited to a few specialised players").
- **Import share trend:** ~90% import-dependent on CRGO steel input (structural, not a trend expected
  to reverse materially near-term given domestic capacity is only 40,000-50,000 MT against
  400,000-450,000 MT demand).

---

## SECTION 5: SUMMARY & RUNWAY — CORE

### 5A. Funnel

```
TAM (conservative, India CRGO lamination/core processing, ~2024/25):     ₹9,000 Cr
  → SAM (product/geo/channel/customer/capability filters, 58% of TAM):   ₹5,200 Cr
    → Current VILAS share of SAM (FY26 CRGO revenue ₹457 Cr):            8.8%
    → SOM 3yr (aggressive capacity-justified share gain to 12.8%):       ₹840 Cr  (~23% CAGR)
    → SOM 5yr (share gain to 15.3%):                                     ₹1,170 Cr (~21% CAGR)
```

### 5B. Runway assessment

- **Revenue headroom (SAM ÷ current CRGO revenue):** 5,200 / 457 = **11.4x**.
- **TAM growth rate:** ~8%/year (moderate, industrial-capex-driven, not hypergrowth).
- **Company CAGR vs. TAM CAGR:** VILAS's guided/modelled growth (23-24% SOM-implied, management's own
  FY27 guide of 40-50% volume growth) vastly outpaces the ~8% market growth — **VILAS is gaining share,
  not merely riding the market**, consistent with the tripled-capacity build.
- **Years to saturate SAM at current growth:** At a 25% sustained CAGR, ~11 years to reach today's
  ₹5,200 Cr SAM from a ₹457 Cr base; at a 40% CAGR (management's near-term guide), ~7.5 years. Either
  way, headroom is not the near-term constraint — execution and proof-status of the newer lines are.

### 5C. Runway classification

**STRONG.** (Canonical enum per this stage's output contract: MASSIVE / STRONG / GOOD / MODERATE /
LIMITED. Note: the task brief for this run separately referenced an ABUNDANT/ADEQUATE/CONSTRAINED
scale; STRONG is the closest honest mapping — >10x revenue headroom and clear share-gain capability
via already-built capacity argue against a lower tier, but the market itself growing at only ~8%/year,
plus the demonstrated capacity ceiling binding by year 5, argue against the top MASSIVE tier.)

### 5D. SAM expansion levers actually being pursued

| Lever | Evidence | Potential addition | Revised headroom |
|---|---|---|---|
| Export growth (Gulf, Europe, Canada) | Inv. Pres. slide 12: "Growing export footprints"; FY25 exports only ₹6.0 Cr / 1.3% of revenue today | Small near-term (~₹20-40 Cr over 3-5yr if exports scale to 5-8% of revenue) | Marginal |
| PGCIL approval (removes the Customer filter's −15% SAM subtraction) | B01/B07: "in process," >12 months, unfired proof gate | Could restore up to ~₹1,300 Cr of SAM (the −15% customer-filter slice) if/when approval lands | Material, but proof-gate-dependent — do not credit until fired |
| New Unit-3 nanocrystalline machine (+4-5 MT/month, per B07 optionality register) | Management-claimed, unconfirmed installed | See adjacency sizing below | Small in absolute ₹ terms |

### 5E. Final output card

```
CORE (CRGO lamination/core processing) funnel:
  TAM (conservative):  ₹9,000 Cr        TAM (realistic): ₹10,500 Cr
  SAM:                 ₹5,200 Cr (58% of TAM)
  SOM 3yr:              ₹840 Cr  (~23% CAGR from ₹457 Cr base)
  SOM 5yr:            ₹1,170 Cr  (~21% CAGR)
  Runway class:        STRONG (11.4x headroom, ~8%/yr TAM growth, capacity-backed share-gain capability)
```

**Valuation implication line (qualitative — stage 11 owns the actual margin model):**
At the **~23-24% blended (CRGO + haircut-adjusted optionality, see analyst note) revenue CAGR** implied
by SOM over 3 years, with a margin trajectory that recovers from FY26's cyclical trough (11.2% EBITDA
margin) toward the pre-ramp 17-20% band as Unit-3 utilisation climbs (B04 must-track metric), earnings
growth would run **materially faster than revenue growth** near-term (margin recovery adds flow-through
on top of volume growth) before decelerating as normalisation completes and the capacity ceiling binds
by year 5. This **conditionally supports** the current trailing P/E of 21.8x (B00 anchor) — but only if
the margin recovery and the newer-line ramps (nano/radiator/copper) materialise close to schedule. If
margin stays at trough level and the optionality lines continue slipping (B07: PGCIL, radiator and
copper timelines have each slipped once already), earnings growth tracks the CRGO-only ~23% path alone,
which sits below the 25% hurdle — in which case the valuation is **not** supported by this stage's
market-sizing evidence alone.

---

## SECTION 6: DOWNSTREAM SIGNAL CANDIDATES

| # | Candidate Signal | Entity Type | Why It Drives Demand | Likely Primary Source | Expected Cadence |
|---|---|---|---|---|---|
| 1 | PGCIL vendor-approval status | Regulatory | Gates VILAS's access to larger institutional/high-kV orders and global-MNC eligibility; currently "in process" >12 months (B01/B07) | Power Grid Corporation of India vendor-empanelment notices / VILAS exchange filings | Event-driven |
| 2 | CEA National Electricity Plan (Transmission) capacity-addition data (GVA, ckm) | Macro | Direct demand driver for transformer-core (CRGO) volumes across the whole industry, not just VILAS | Central Electricity Authority (CEA) publications | Quarterly/Annual |
| 3 | DGTR CRGO anti-dumping investigation outcome | Regulatory | Any duty raises landed CRGO cost for all processors (double-edged for VILAS: margin risk on input, but also a moat vs. pure-import-arbitrage competitors) | Directorate General of Trade Remedies (DGTR) notifications / Gazette of India | Event-driven |
| 4 | Atlas Transformers India Ltd (promoter-related counterparty) | Counterparty | ~12.5% of FY25 revenue on a combined sales+purchase basis, trades on both sides of VILAS's book (B04 flag); a governance-adjacent demand signal, not a clean external one | Related-party-transaction disclosures / AGM resolutions (exchange filings) | Quarterly |
| 5 | Marquee OEM customer order books (Voltamp, Electrotherm, ECE Industries, Shilchar, Kirloskar Electric) | End-customer | Their capex/order-book cycles directly set VILAS's CRGO lamination offtake | Individual company exchange filings / investor presentations (order-book disclosures) | Quarterly |
| 6 | JSW JFE Electrical Steel Nashik (sole domestic CRGO mill) capacity status | Counterparty/Macro | Any domestic CRGO capacity add changes the ~90% import-dependence structure and input-pricing dynamics industry-wide | JSW Group exchange filings / DGTR petitioner disclosures | Event-driven |
| 7 | Renewable capacity addition (MNRE/CEA bulletins) | Macro | Every incremental GW of solar/wind requires step-up/evacuation transformers — a named structural driver (Inv. Pres. slide 24) | Ministry of New and Renewable Energy (MNRE) / CEA monthly renewable bulletins | Monthly/Quarterly |

Rows 1 and 4 are marked **SHARED**: PGCIL approval status is a correlated catalyst across both the core
CRGO institutional-order slice and the optionality lines (bushings/copper eligibility for larger
orders); Atlas Transformers appears on both the sales and purchase side of VILAS's book, so it is a
single correlated counterparty risk, not two independent ones. FTTCP should count each once.

**demand_externally_verifiable: TRUE** (7 rows, well above the minimum of 3).

---

## ADJACENCY SIZING (sized separately per run instructions — different proof status, not blended)

### Nanocrystalline cores (installed capacity 240 MTPA)

FY26 actuals: 30,250 kg sold H2 FY26, revenue ₹3.48 Cr (Inv. Pres. slide 6) → realisation
~₹1,150/kg, far above CRGO's ~₹230/kg (consistent with nanocrystalline's premium-material status).
Management's own FY27 target: ~15 MT/month (~180 MTPA) utilisation, guided ~₹18-20 Cr revenue
(B07 catalysts_12m). **Independent India-specific market size: NOT FOUND.** Global nanocrystalline
toroidal-core market (a broader category than transformer cores alone — includes current-transformer
and inductor applications) is sized at USD 1.31 Bn (2024) → USD 3.52 Bn (2035E), 9.4% CAGR
(WebSearch, sphericalinsights.com, 2026-09-03, MODERATE confidence, global only). No credible
India-allocation percentage could be sourced independently; any India-specific rupee figure derived
from this global number would be an unsupported guess and is deliberately not produced here (per the
"never estimate a missing number" rule). **Directional SOM only, anchored to management's own
disclosed capacity and near-term target, carried at a discount for slippage risk consistent with
B07's credibility-split rule:** SOM 3yr ≈ ₹20-25 Cr; SOM 5yr ≈ ₹35-45 Cr (assuming the "new China
machine, +4-5 MT/month" optionality in B07's register converts). **Confidence: LOW.**

### Transformer radiators (installed capacity 7,200 MTPA per most slides; 7,600 MTPA on one slide,
unreconciled per B04 flag)

**No independent third-party market-size report for "transformer radiators" as a standalone segment
was found** — radiators are typically a sub-component of a transformer OEM's own bill of materials or
a vendor-supplied fabrication item, not a market independently tracked by research firms. This is a
genuine data gap, stated rather than papered over. The only defensible number available is a
**capacity-implied revenue ceiling on VILAS's own plant**, not a market size: 7,200,000 kg × a generic
steel-fabrication realisation of ~₹150-200/kg (unsourced industry rule of thumb, not independently
verified — flagged) ≈ **₹108-144 Cr at 100% utilisation**. This ceiling should not be read as a
national TAM. Given the radiator line's commercial launch already slipped ~9 months (Jul-2025 guided
→ Apr-2026 actual, per B07 flag), SOM is carried conservatively: SOM 3yr ≈ ₹20-30 Cr; SOM 5yr ≈
₹50-60 Cr (partial utilisation of the plant's own ceiling). **Confidence: LOW.**

### Copper conductors / PICC-CTC (Phase 1 capacity 1,500-1,800 MTPA per Investor Presentation vs.
3,600 MTPA per May-2026 concall — unresolved conflict, both anchored, per B07 flag)

Global CTC-for-transformer market: ~USD 235 Mn (2024) → USD 366 Mn (2031E), ~6.5% CAGR (WebSearch,
Nexdigm market report, 2026-09-03, MODERATE confidence). India's specialty PICC/CTC capacity is
concentrated in four established players — KSH International, Precision Wires, Apar, and Asta
India — with combined specialty capacity expanding from ~45,000 MT to ~77,000 MT by FY28 (WebSearch,
SOIC Finance / Investorstack Substack research notes on KSH International, 2026-09-03, MODERATE
confidence, cross-referenced across two independent write-ups). VILAS's disclosed Phase-1 capacity
(1,500-3,600 MTPA) is **~2-8% of established India specialty-conductor capacity** — a useful scale
check showing this is a small, unproven entrant into a market with qualified, five-to-seven-year
end-utility qualification cycles already held by incumbents (a real barrier, not a formality).
A rough India CTC/PICC market estimate, allowing India a proportionate share of global demand given
its transformer-manufacturing scale, sits in the **₹300-500 Cr** range (LOW-MODERATE confidence,
built from the global figure with no independently sourced India split — flagged as a rough estimate,
not a sourced number). **Red flag:** management's own FY27 copper-conductor revenue guidance of
₹100-120 Cr (B07 optionality register) would imply VILAS capturing **20-40% of even this generously
sized rough India TAM in its first commercial year**, from a brand-new, currently pre-commercial line
with an unresolved capacity-spec conflict and a customer-qualification process that has not yet
started. This reinforces B07's existing credibility discount on copper timeline guidance rather than
resolving it. SOM carried at a steep haircut: SOM 3yr ≈ ₹35-45 Cr; SOM 5yr ≈ ₹75-85 Cr.
**Confidence: LOW.**

### HV Bushings (12kV-400kV, VILAS holds 25% equity in a newly incorporated R&D-stage entity)

Global electrical/HV bushings market: USD 3.1-3.67 Bn (2024) → USD 4.05-4.77 Bn (2029/2033E),
~4-5.4% CAGR across four independent research-firm estimates (WebSearch, 2026-09-03 — MODERATE
confidence backdrop, global only; the ~15-18% spread across vendors on both the base year and the
CAGR is itself a signal of measurement softness in this category). **No India-specific bushings
market size was found.** More importantly, this line has **no disclosed revenue, no signed
tech-transfer agreement, and VILAS holds only a 25% economic stake** in an entity still in "R&D and
product development" (Chairman's Message, Inv. Pres. p.5; B07 optionality register: "currently
unsigned"). Computing a SOM for a pre-revenue, 25%-owned, unsigned-technology entity would produce a
number with no evidentiary basis. Per the "never estimate a missing number" rule: **SOM for HV
bushings = NOT FOUND.** This is a proof-status gap (Proof NOT FIRED, per the Transition Decision
Matrix), not a sizing exercise that can currently be completed.

---

## SEARCH LOG

**Searches performed (15):**
1. India transformer market size 2024 2029 CAGR billion
2. India CRGO electrical steel market size lamination import volume
3. DGTR CRGO anti-dumping investigation India demand consumption metric tonnes 2024 2025
4. India power transmission distribution capex Rs lakh crore 2032 CEA National Electricity Plan transformer demand
5. nanocrystalline core market India size transformer
6. transformer radiator market size India manufacturers capacity
7. India copper CTC conductor PICC market size transformer winding conductors
8. HV bushings market India 12kV 400kV transformer bushing manufacturers import
9. Pitti Engineering revenue FY25 CRGO lamination laser cutting
10. Jaybee Laminations revenue CRGO transformer core India
11. global electrical steel bushing market size transformer bushings USD million 2024
12. BSE 544310 company CRGO laminations transformer
13. India CRGO lamination processors market unorganised fragmented players list
14. Kryfs Power Components revenue FY25 CRGO laminations BSE
15. transformer manufacturing cost breakdown core steel percentage copper winding tank

**Searches skipped:** none (no quota errors encountered; status is COMPLETE, not partial). Several
searches (nanocrystalline India-specific, radiator market, HV bushings India-specific, exact identity
of BSE code "544310") returned thin or no usable India-specific data — this is stated as a finding
(DATA THIN / NOT FOUND) within the relevant sections above, not treated as a skipped search.

---
