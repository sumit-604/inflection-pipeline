# Stage 9 — TAM / SAM / SOM Market Sizing
**Company:** GNG Electronics Ltd (EBGNG) | **Run date:** 2026-07-12 | **Model:** claude-sonnet-5

**CORRECTION TO MANIFEST:** The collector-assigned sector tag "Pharma / CDMO" is a defect. GNG
Electronics Ltd (Electronics Bazaar / EB) is a refurbished ICT-device company (laptops, desktops,
tablets, servers, premium smartphones, workstations, accessories, nascent leasing), operating in
India plus export markets (USA, UAE, Europe). This report sizes that market. No pharma market is
sized anywhere below.

FX convention: ₹87.00/US$1 used uniformly for all USD→INR conversions in this report (source: DRHP
footnote, 1 USD = ₹87.40 as of 28-Feb-2025, line 7332 of drhp_text.txt; rounded to ₹87 for
calculation simplicity). This introduces minor timing imprecision on CY18-vintage figures but is
standard practice for market-sizing normalization and is applied consistently so ratios/growth
rates are unaffected.

---

## SECTION 1: MARKET DEFINITION

### 1A. Precise boundaries

- **Product scope (in):** refurbished/used-and-certified ICT devices — laptops, desktops,
  workstations, tablets, servers, and premium smartphones — sold under warranty after
  inspection/repair/grading ("EB certified"), plus adjacent refurbishment services (data-wiping,
  grading) and a nascent device-leasing line.
- **Product scope (out):** new-device OEM retail; non-ICT consumer-electronics refurbishment
  (home/kitchen appliances, TVs, cameras, gaming consoles — all part of the broader "used and
  refurbished electronics" category the DRHP's headline figures include but GNG does not
  participate in); raw e-waste/scrap-metal recycling (a distinct business model, e.g. Attero); high
  -value spare-parts resale as a standalone market (GNG consumes spare parts as an input, is not a
  spare-parts market participant).
- **Geographic scope (in):** India (domestic) + USA, UAE and Europe (export, per B04: ~75% of
  revenue is export, ~25% India). These are GNG's four disclosed, revenue-generating geographies.
- **Geographic scope (out):** all other global geographies (China, APAC ex-India, LatAm, Africa)
  are product-relevant globally but NOT counted in GNG's SAM; a company marketing claim of
  "presence across 46 countries" / Africa exposure is noted but not evidenced with disclosed
  revenue and is therefore excluded from SAM (conservative bias).
- **Customer scope:** B2B/B2B2C bulk and institutional buyers (corporate device-refresh programs,
  leasing companies, distribution partners such as Redington) plus B2C via e-commerce/D2C
  ("Electronics Bazaar" storefront). Predominantly device-replacement demand, not first-time
  computer buyers.
- **Channel scope:** organized/certified refurbishment channel (OEM-authorised where applicable —
  GNG is India's largest Microsoft Authorised Refurbisher per DRHP) and organized wholesale/
  distribution/e-commerce. Unorganized/informal peer-to-peer resale (still ~89% of India's
  refurbished-PC market by value, FY24) is excluded from SAM as not realistically capturable by an
  organized player in a 3-5 year window, though its shrinkage is a growth driver (Section 4A).
- **Price segment:** mid-value refurbished devices; excludes ultra-budget scrap-grade devices and
  full-price new premium devices.
- **Explicit inclusions:** laptops (~68% of GNG revenue), desktops/tablets/servers/workstations/
  premium smartphones/accessories (~32%), nascent leasing.
- **Explicit exclusions:** pharma/CDMO (manifest tag is a collector defect — not sized), new-device
  manufacturing, non-ICT refurbishment, e-waste metal recycling.

### 1B. Management's own TAM claim

GNG's DRHP does not state a single labelled "our TAM is $X" figure. Instead, the Industry Overview
chapter (sourced throughout to the **1Lattice Report**, commissioned market study, data vintage
CY23/FY24) opens with the broadest number available and gives it primary billing:

> "Global used and refurbished electronics market grew from US$169.9B in CY18 to US$207.4B in
> CY23, at a CAGR of 4.1%. By CY28, the market is projected to reach US$334.8B, growing at a 10%
> CAGR." — DRHP, Industry Overview §3.1, PDF raw page 143 (printed p.139), source 1Lattice Report.

This is the most prominent, section-opening figure and is the number an investor reading the
document top-to-bottom encounters first as "the opportunity." It spans non-ICT categories (home
and kitchen appliances, televisions, cameras, gaming consoles) that GNG does not participate in at
all — the DRHP itself defines the category to include these (raw p.142/printed p.138).

**Date:** CY23 actual / CY28 projection, 1Lattice Report, undated within the extract but the DRHP
itself is a 2025-vintage filing — data is **STALE by the >2yr rule** relative to run date
2026-07-12.

**Credibility read:** BROAD. Management (via the underwriter-commissioned market study) leads with
the widest possible framing before narrowing to PC- and smartphone-specific cuts later in the same
chapter. See Section 2 for the quantified ratio against the conservative TAM estimate below.

**DRHP internal inconsistency flagged:** The Risk Factors chapter (raw p.37/printed p.33, line
2703-2709) states the global refurbished-PC market "is projected to reach US$28.3 billion by CY28"
and the Indian refurbished-PC market "is expected to reach US$4.6 billion by FY29." The Industry
Overview chapter (raw p.144/printed p.140) and the Our Business chapter (raw p.177/printed p.173)
both state **US$38.3 billion by CY28** (global) and **US$3.3 billion by FY29** (India) — three of
four occurrences agree on 38.3B/3.3B, and the FY29 India figure is internally consistent with the
27%→33% CAGR math shown ($0.8B × 1.33^5 = $3.35B ≈ $3.3B), while $4.6B is not ($0.8B × 1.33^5 ≠
$4.6B). This report treats $38.3B / $3.3B as correct and the Risk Factors figures as a drafting
error, and flags the inconsistency itself as a data-quality point.

---

## SECTION 2: TAM ESTIMATION, MULTIPLE METHODS

All figures below are sourced to the DRHP Industry Overview chapter (1Lattice Report), raw pages
142-161 / printed pages 138-157 of `drhp_text.txt`, unless a web source is cited. CAGR figures not
directly stated as a starting-year value are **derived** by reversing the stated CAGR from the
stated end-year value; each such derivation is shown.

### Method 1 — Top-down, global segment aggregation (primary method)

**Global refurbished + used PC (laptop+desktop) market:**
CY23 value not stated directly for the *used+refurb* aggregate (only the *refurbished-only*
sub-segment, $14.4B CY23, is given directly). Reversing the stated "$57.4B by CY28, 11% CAGR
CY23-28" (raw p.144/printed p.140): CY23 = $57.4B ÷ 1.11⁵ = $57.4B ÷ 1.6851 = **$34.06B**.

**Global used + refurbished premium-smartphone market:**
Reversing "$193.7B by CY28, 12% CAGR CY23-28" (raw p.144-145/printed p.140-141):
CY23 = $193.7B ÷ 1.12⁵ = $193.7B ÷ 1.7623 = **$109.90B**.

**Conservative TAM (CY23, PC + premium smartphone only, global):**
$34.06B + $109.90B = **$143.96B ≈ ₹12,52,452 Cr** (143.96 × ₹8,700 Cr/US$B).

**Realistic TAM (CY23, adds open-box PC + high-value spare parts, global):**
- Open-box PC, global, CY23: $4.2B (stated directly, raw p.144/printed p.140).
- High-value electronics spare parts, global: reversing "$5.6B by CY28, 9% CAGR CY23-28"
  (raw p.145/printed p.141): CY23 = $5.6B ÷ 1.09⁵ = $5.6B ÷ 1.5386 = $3.64B.
- Realistic TAM = $143.96B + $4.2B + $3.64B = **$151.80B ≈ ₹13,20,660 Cr**.

Tablets, servers and workstations are NOT separately sized anywhere in the DRHP or in web search
within this run's budget — this is a genuine data gap (carried to stale_data_flags/input_gaps as
`tablets_servers_submarket_not_sized`). Given GNG's own revenue mix (68% laptops / 32% other, where
"other" bundles desktops — already inside the PC figure above — plus tablets/servers/smartphones/
workstations/accessories), the true product-scope TAM likely sits marginally above the realistic
figure above; this is not quantified and the conservative/realistic figures above are used as-is,
consistent with the conservative-bias instruction.

**Staleness:** CY23-dated 1Lattice figures are ~2.6 years old at run date → **STALE** (>2yr rule).

### Method 2 — Bottom-up, unit economics (cross-check, not independent)

- Global new PC shipments, CY2024: **262.7 million units** (IDC, web search, "Global PC shipments
  totaled 262.7 million units in 2024," ~1.5yr old, not stale).
- India new PC shipments, CY2024: **14.4 million units**, +3.8% YoY (IDC, web search, ~1.5yr old).
- India used+refurb PC penetration of the *total* PC market: 20% (FY19) → 24% (FY29) per DRHP
  (raw p.159/printed p.155); interpolating linearly to ~FY24 gives ≈22%.
- Implied India total PC market (new+used+refurb) units ≈ 14.4M ÷ (1−0.22) = **18.46M units**;
  implied used+refurb units ≈ 18.46M × 22% = **4.06M units**.
- Cross-check against the $ figure: India used+refurb PC value FY24 = $2.1B (Method 1 geography
  component below) ÷ 4.06M units = **$517/unit** blended ASP (≈₹44,980 at ₹87/US$).
- GNG's own FY24 blended revenue/unit (source B04): **≈₹30,822/unit** (≈$354/unit at ₹87/US$).
  GNG's own ASP sits below the market-derived blended ASP — plausible, since GNG's own mix skews
  to higher-volume, more price-sensitive B2B/bulk and export deals rather than premium D2C
  refurb, and the two figures are within 1.5x of each other (**no material divergence** —
  triangulation holds).

This method is not a fully independent TAM estimate (it reuses the $2.1B India figure from Method
1) but it corroborates that the $ market-sizing figures and GNG's own disclosed unit economics are
internally consistent, which is the intended cross-check function.

### Method 3 — Peer revenue aggregation (India, organized-segment sanity check; LOW confidence)

Disclosed organized-player revenues, most recent fiscal year:
- GNG/Electronics Bazaar: ₹1,414 Cr (FY25 consolidated, CARE rating p.4) / ₹1,895 Cr (FY26, +34%
  YoY, Q4 FY26 concall, May-2026) — India + export combined.
- Cashify: ₹1,096 Cr (FY25, Entrackr, web search) — India-focused, broader consumer-electronics
  buyback/resale (smartphone-heavy), only partially overlapping GNG's PC-centric scope.
- NewJaisa Technologies (listed SME): ₹65.66 Cr (FY25) declining to ₹40.49 Cr (FY26, hit by
  Amazon India's March-2025 discontinuation of its refurbished marketplace, which had been ~60% of
  NewJaisa's revenue) (screener.in / scanx.trade, web search).
- Attero Recycling: ₹961 Cr (FY25, Entrackr) — **excluded** from the sum; this is e-waste
  metal-recovery/recycling, a structurally different business from device refurbishment, kept as
  an adjacent-market reference only.

Organized-player sum (GNG + Cashify + NewJaisa, mixed India/global scope) ≈ **₹2,576 Cr (FY25)**.
Grossing this up using the DRHP's stated 11% organized-share-of-refurbished-PC-market ratio (FY24,
raw p.157-158/printed p.153-154) implies a total India refurbished-PC-scope market of
2,576 ÷ 0.11 ≈ **₹23,420 Cr (~$2.7B)**.

**This diverges materially from Method 1 and is NOT averaged into the headline TAM.** The
divergence is explained, not smoothed over: Method 3 (a) is India-weighted even though GNG's own
revenue and Cashify's revenue include non-India activity, and (b) entirely excludes the large
organized US/Europe refurb markets (e.g. Back Market alone: $415M revenue / $2.8B GMV in 2024,
Sacra/Getlatka, web search) that Method 1 counts. Method 3 is retained only as a floor-level sanity
check confirming the India organized segment is a small, fast-formalizing slice of a much larger
global addressable market — it is not used as a TAM candidate.

### Method 4 — Import substitution: not meaningfully applicable

India restricts, rather than encourages, import of used/end-of-life electronics under the
Hazardous and Other Wastes (Management and Transboundary Movement) Rules and e-waste EPR
framework; GNG's India supply is predominantly domestically sourced corporate device refresh, not
an import-substitution dynamic. This method is not applied to build a TAM figure; the import
restriction itself is instead carried into Section 4B as a structural risk/monitoring item.

### Method 5 — Global benchmark / penetration comparison (directional only)

- India PC penetration: **75-95 per 1,000 population** vs USA **750-800/1,000** and China
  **300-350/1,000** (DRHP raw p.141/printed p.137, source 1Lattice). Even parity with China's
  *current* penetration (not USA's) implies a 3.2-4.7x expansion of India's underlying PC
  installed base over time, holding price constant — a structural tailwind for the *total* PC
  market (new+used+refurb), not specific to the refurb segment.
- Used+refurb *share* of the PC market: USA 20% (CY23)→24%(CY28); Europe 19%(CY23)→22%(CY28);
  India 20%(FY19)→24%(FY29, i.e. ~22% around FY24). India's projected penetration trajectory
  **converges to, and briefly exceeds, current developed-market levels within the DRHP's own
  forecast window** — a genuinely aggressive assumption worth flagging rather than taking at
  face value; it is used here only to corroborate the *direction* of Section 4A drivers, not to
  produce a standalone $ TAM figure.

### Triangulation table

| Method | Estimate | Confidence | Staleness | Scope |
|---|---|---|---|---|
| 1 — Top-down (conservative) | $143.96B ≈ ₹12,52,452 Cr | Medium | STALE (CY23, 1Lattice) | Global, PC+premium smartphone |
| 1 — Top-down (realistic) | $151.80B ≈ ₹13,20,660 Cr | Medium | STALE (CY23, 1Lattice) | Global, +open-box PC+spare parts |
| 2 — Bottom-up unit cross-check | Confirms Method 1's India $2.1B component; ASP within 1.5x of GNG's own | Medium | STALE (India penetration data FY24/29); shipment units ~1.5yr, not stale | India only |
| 3 — Peer aggregation | ≈₹23,420 Cr (~$2.7B) | Low | Peer revenue FY25 (not stale); 11% ratio FY24 (borderline stale) | India organized-refurb-PC scope only, NOT comparable to Method 1 |
| 5 — Global benchmark | Directional only, no $ output | Low | Mixed CY18-29 | Corroborates growth durability |

**Headline TAM used for this report:** conservative $143.96B ≈ **₹12,52,452 Cr**; realistic $151.80B
≈ **₹13,20,660 Cr**. Method 3's much smaller figure is explained above and excluded from the
headline (materially different scope, not a competing estimate of the same thing).

**Management claim vs conservative estimate:**
Mgmt claim (Section 1B) = $207.4B (CY23) ≈ **₹18,04,380 Cr**.
Ratio = 1,804,380 ÷ 1,252,452 = **1.44x** → per the standard read (within 1.5x = reasonable), this
lands as **REASONABLE**, but with an important caveat: management's figure includes non-ICT
categories (appliances, TVs, cameras, gaming consoles) entirely outside GNG's product scope, while
the conservative estimate here excludes those but includes the *full global* premium-smartphone
TAM (a category where GNG's actual capability is nascent, addressed via steep discounting in SAM,
Section 3A). The "reasonable" verdict is therefore partly a function of these two scope
mismatches roughly offsetting — not evidence that management scoped the claim precisely to GNG's
addressable market. Read as reasonable-but-fortuitous, not as evidence of disciplined TAM framing.

---

## SECTION 3: SAM & SOM

### 3A. SAM — five filters applied to the conservative TAM (₹12,52,452 Cr)

**Filter 1 — Geography** (GNG's four served markets only: India, USA, Europe, UAE):

PC component: USA $10.1B + Europe $9.1B + India $2.1B ($0.8B refurb+$1.3B used) + UAE $0.283B
(refurbished laptops only, CustomMarketInsights 2024, web search, secondary/lower confidence) =
**$21.58B**, i.e. 21.58/34.06 = 63.4% of the global PC component.

Smartphone component: USA $27.8B + Europe $34.4B + India $3.5B = **$65.7B** (UAE premium-
smartphone data NOT FOUND — excluded, conservative), i.e. 65.7/109.9 = 59.8% of the global
smartphone component.

Geography-filtered subtotal = $21.58B + $65.7B = **$87.28B ≈ ₹7,59,362 Cr**.

*Cross-check:* India PC ($2.1B) + India smartphone ($3.5B) = $5.6B ≈ 35% × India's total used and
refurbished electronics market ($16.7B FY24, raw p.157/printed p.153) = $5.85B. Within 4% —
internal DRHP consistency confirmed for the India component (contrast with the CY28 projection
inconsistency flagged in Section 1B).

**Filter 2 — Product/capability fit** (GNG's actual capability is overwhelmingly PC-centric;
premium smartphones are a minor, nascent slice of the 32% "other" revenue bucket, not a scaled
product line):
Retain 100% of the PC component ($21.58B). Discount the smartphone component to **10%** of its
geography-filtered value, reflecting genuinely early-stage capability rather than an assumption
that GNG competes for the full smartphone opportunity: $65.7B × 10% = $6.57B.
Subtotal = $21.58B + $6.57B = **$28.15B ≈ ₹2,44,931 Cr**.

**Filter 3 — Channel fit** (organized/certified channel only; unorganized/informal resale is not
realistically capturable in 3-5 years):
PC-specific organized shares (CY23, DRHP): USA 75%, Europe ~75% (interpolated from 60% CY18→90%
CY28, linear), India 11% (FY24), UAE 11% (proxy, India-like, NOT FOUND directly — flagged
assumption). Weighted by each geography's PC $ value: (10.1×0.75 + 9.1×0.75 + 2.1×0.11 +
0.283×0.11) ÷ 21.58 = (7.575+6.825+0.231+0.031)/21.58 = 14.662/21.58 = **67.9% ≈ 68%** blended
organized share. Applied uniformly to the Filter-2 subtotal (smartphone organized share not
separately disclosed — same 68% used as proxy, flagged assumption):
$28.15B × 68% = **$19.14B ≈ ₹1,66,553 Cr**.

**Filter 4 — Customer/capability fit** (modest discount for enterprise ITAD/data-destruction-
certification-heavy contracts and Apple-authorized-program-gated premium smartphone deals GNG may
not fully address today): retain 90%.
$19.14B × 90% = **$17.23B ≈ ₹1,49,901 Cr**.

**SAM ≈ ₹1,49,900 Cr** (rounded). **SAM as % of conservative TAM = 149,900 ÷ 1,252,452 = 12.0%.**

### 3B. SOM at 3 and 5 years

Current revenue (SOM base, per REVENUE_CR marker) = **₹1,895 Cr (FY26)**.
Current SAM share = 1,895 ÷ 149,900 = **1.26%**.

SAM forward growth uses the Method-1 blended CY23-28 CAGR: weighted by CY23 component size,
(34.06×11% + 109.90×12%) ÷ 143.96 = **11.76% ≈ 11.8%** p.a., applied uniformly to SAM as a
simplifying assumption (products/geographies inside SAM grow at roughly the blended TAM rate).

3yr forward SAM (1.118³ = 1.3974) = 149,900 × 1.3974 = **₹2,09,451 Cr**.
5yr forward SAM (1.118⁵ = 1.7467) = 149,900 × 1.7467 = **₹2,61,821 Cr**.

**Share-gain rule applied:** current share (1.26%) is tiny in absolute terms, but the market's
unorganized share is 89% in India specifically (>>40% formalization threshold) and GNG already
holds the "largest refurbisher" position with disclosed capacity headroom (Section 3C) and an
active distribution partnership (Redington) — this supports the **aggressive** end of the
share-gain band for the 5-year case, while the 3-year case uses the **normal** band:

- 3yr: normal case, +1.0pp → share = 2.26% of 3yr SAM.
  SOM_3yr = ₹2,09,451 Cr × 2.26% = **₹4,734 Cr**.
- 5yr: aggressive case (capacity + execution + formalization tailwind evidenced), +3.0pp →
  share = 4.26% of 5yr SAM.
  SOM_5yr = ₹2,61,821 Cr × 4.26% = **₹11,154 Cr**.

**Implied revenue CAGR (arithmetic):**
- 3yr: (4,734 ÷ 1,895)^(1/3) − 1 = (2.498)^0.333 − 1 = **35.7%**.
- 5yr: (11,154 ÷ 1,895)^(1/5) − 1 = (5.886)^0.20 − 1 = **42.5%**.

Both figures sit above GNG's own recent actual (34% YoY, FY26) and well above the fund's 25% CAGR
target — this is a genuinely useful, positive read for stage 11: on this analysis, **the market is
not the binding constraint on a 25% CAGR thesis**; execution, competition and margin trajectory are
the swing factors. **FLAG: this implied CAGR is a mechanical SAM-share extrapolation, not a
forecast — stage 11 should treat it as an upper-bound sanity check, not a base case.**

### 3C. Capacity cross-check (against B07 capex-embedded-growth figure)

Installed capacity (Q4 FY26, per B07): **150,000 units/month = 1,800,000 units/year**. B07 confirms
capex-embedded growth is 0% — asset-light, no committed capex pipeline; capacity scales via
facilities + labour, not fixed assets.

Capacity-implied max annual revenue at 100% utilization, using GNG's FY24 blended revenue/unit
(₹30,822/unit, source B04, ~2yr-stale figure, flagged): 1,800,000 × ₹30,822 = **₹5,548 Cr**.

- vs SOM_3yr (₹4,734 Cr): capacity is **sufficient**, with an 17.2% cushion (5,548 ÷ 4,734 = 1.17x).
- vs SOM_5yr (₹11,154 Cr): **gap of ₹5,606 Cr** (11,154 − 5,548) at current facility footprint.

Per B07, capacity is not capex-committed — it scales via facilities and labour additions, which
are disclosed as a stated growth lever (Q4 FY26 concall) but are not a firm, dated capacity-
expansion plan in the materials supplied to this stage. **Read: the SOM_5yr figure is the more
optimistic side of this comparison** — it requires the facility footprint to roughly double (from
150,000 to ~295,000+ units/month) over five years with no committed capex plan evidencing that
this will happen, only an asset-light operating model that makes it *achievable in principle*.
This is a genuine execution dependency to monitor, not a hard capex bottleneck.

---

## SECTION 4: GROWTH DRIVERS, RISKS & STRUCTURE

### 4A. TAM growth drivers

| Driver | Impact | Evidence |
|---|---|---|
| Formalisation (organized share gain) | High | India organized refurb-PC share 5%(FY19)→11%(FY24)→32%(FY29e), 33-42% CAGR (DRHP raw p.157-158/printed p.153-154, 1Lattice) |
| Penetration (PC/1,000 population) | High | India 75-95/1,000 vs China 300-350, USA 750-800 (DRHP raw p.141/printed p.137) |
| Sustainability/regulatory tailwind | Medium-High | France mandates 20%→40% refurbished IT procurement by 2040 (50% public sector by 2025); Ireland's "Buying Greener" targets 80% refurbished/green ICT procurement by 2025; EU circular-economy goals (DRHP raw p.152/printed p.148) |
| Premiumisation | Medium | Premium notebook (>US$1,000) shipments +13.8% YoY in India, 2024 (IDC, web search) |
| Technology enablement / refresh cycles | Medium | Windows 10 end-of-support (Oct-2025) driving enterprise hardware refresh, feeding used-device supply into the refurb channel (IDC, web search) |
| Geographic expansion | Medium | GNG markets itself as present across 46 countries / Africa exposure (company PR, web search) — **not evidenced in disclosed revenue**, treated as unconfirmed upside, not counted in SAM |
| Demographics | Low-Medium | Rising India disposable income, young population, Digital India push (DRHP raw p.137/printed p.133) |
| New applications | Low | Nascent leasing line (per PRODUCTS marker) — too early to size, optionality only |

### 4B. TAM risks

| Risk | Monitoring signal |
|---|---|
| OEM-direct refurbishment programs (Apple Certified Refurbished, Dell Outlet, HP Renew) disintermediating third-party refurbishers | OEM refurb-program volume/pricing announcements |
| Import restriction on used electronics/e-waste into India (Hazardous and Other Wastes Rules, EPR) constraining domestic device-refresh supply flow | Regulatory notifications, customs data on used-device imports |
| Data-security/compliance tightening raising the cost of certified refurbishment, favouring larger organized players (could help GNG relatively but raises industry cost base) | Data protection rule enforcement (DPDP Act rules) |
| Extended device lifecycles via cloud/thin-client computing reducing physical hardware refresh frequency | Enterprise IT capex cycle length trends |
| Amazon-India-style marketplace-channel discontinuation risk (already hit NewJaisa, -38% revenue FY26) | Marketplace partner policy changes |
| Saturation of the largest, easiest-to-convert corporate device-refresh accounts | Win-rate/renewal-rate trends on large B2B contracts |
| Fragmented-but-organizing competitive set inviting new entrants (66 active competitors per Tracxn) as organized share visibly expands | New entrant funding announcements |

### 4C. Market structure

- **Competitor count:** ~66 active competitors tracked for Electronics Bazaar (Tracxn, web
  search); GNG ranks among the top 3 by that count and is the disclosed largest India laptop/
  desktop refurbisher (DRHP, multiple pages).
- **Top-3 concentration:** fragmented — DRHP explicitly notes no single player captures >5% of the
  used+refurbished PC market in either the USA or Europe (raw p.149/printed p.145; raw
  p.153/printed p.149).
- **Organized vs unorganized:** India refurb-PC 11%/89% (FY24, formalizing toward 32%/68% by
  FY29e); USA refurb-PC ~75%/25% (CY23, moving to ~90%/10% by CY28); Europe similar trajectory
  (~75%/25% CY23 interpolated → ~90%/10% by CY28).
- **Consolidating or fragmenting:** consolidating toward organized players industry-wide, but the
  organized tier itself remains fragmented (no single player >5% share) — a "rising tide,
  fragmented boats" dynamic.
- **Price vs differentiation competition:** differentiation-led among organized players
  (certification, warranty, OEM-authorised status) with price competition concentrated in the
  still-large unorganized tier.
- **Entries and exits:** Amazon India exited the refurbished-electronics marketplace category
  (March 2025), removing a channel that had been ~60% of NewJaisa's revenue — a channel-
  concentration risk for smaller organized players, and a potential open lane for GNG's own D2C/
  distribution-partner channels (Redington).
- **Import share trend:** NOT FOUND — no disclosed trade-data split of GNG's or the industry's
  device sourcing between domestic corporate refresh and cross-border import; carried as a gap.

---

## SECTION 5: SUMMARY & RUNWAY

### 5A. Funnel

```
TAM (conservative, global, PC+premium smartphone, CY23) ........ ₹12,52,452 Cr
TAM (realistic, +open-box PC +spare parts, CY23) ................ ₹13,20,660 Cr
  └─ Geography filter (India+USA+Europe+UAE only) ............... ₹7,59,362 Cr
      └─ Product/capability filter (smartphone @10%) ............ ₹2,44,931 Cr
          └─ Channel filter (organized-only, 68% blend) ......... ₹1,66,553 Cr
              └─ Customer/capability filter (90% retain) ........ SAM ≈ ₹1,49,900 Cr (12.0% of conservative TAM)
                  └─ SOM 3yr (share 1.26%→2.26% of 3yr SAM) ..... ₹4,734 Cr
                  └─ SOM 5yr (share 1.26%→4.26% of 5yr SAM) ..... ₹11,154 Cr
Current revenue (FY26) ........................................... ₹1,895 Cr
```

### 5B. Runway assessment

- **Revenue headroom** = SAM ÷ current revenue = 149,900 ÷ 1,895 = **79.1x**.
- **TAM growth rate** ≈ **11.8%** p.a. (blended CY23-28 CAGR, Method 1).
- **Company CAGR vs TAM:** GNG's actual FY25→FY26 growth (34% YoY, Q4 FY26 concall) is ~2.9x the
  TAM growth rate (11.8%) — **GNG is gaining share**, not merely riding market growth, consistent
  with the formalization narrative (organized share taking share from unorganized).
- **Years to saturate SAM at current growth rates** (illustrative, mechanical, not a forecast):
  solving 1,895×(1.34)ⁿ = 149,900×(1.118)ⁿ → (1.34/1.118)ⁿ = 79.1 → n = ln(79.1)/ln(1.1986) ≈
  **~24 years**. This is a standard-methodology extrapolation assuming both growth rates hold
  constant indefinitely, which is unrealistic over multi-decade horizons — its function here is
  only to confirm SAM is not a near-term ceiling.

### 5C. Runway classification

**MASSIVE.** ~79x revenue headroom combined with double-digit (11.8%) underlying TAM growth and a
company growing several multiples faster than the market clears the top band of the standard
MASSIVE/STRONG/GOOD/MODERATE/LIMITED matrix (headroom well above the ~20x threshold typically
associated with MASSIVE, with durable double-digit market growth reinforcing rather than
contradicting the read).

### 5D. SAM expansion levers GNG is actually pursuing

- **Distribution partnership (Redington):** disclosed nationwide distribution partnership to
  expand reach for refurbished ICT solutions (company PR, web search) — expands GNG's addressable
  *reach* within the already-defined SAM rather than the SAM itself; potential revenue addition
  NOT FOUND (undisclosed).
- **Nascent leasing line:** per PRODUCTS marker — could open a device-as-a-service adjacent
  market not currently counted in SAM; too early to size, NOT FOUND.
- **Formalization capture beyond the organized-only SAM boundary:** as India's organized refurb-PC
  share moves from 11%→32% (FY24→FY29e per DRHP), a portion of the currently-excluded unorganized
  pool converts into SAM-eligible demand each year; this is already embedded in the SAM's forward
  growth rate (11.8%) rather than treated as a separate lever, to avoid double-counting.
- **Geographic depth (marketed 46-country/Africa presence):** unconfirmed by disclosed segment
  revenue; potential addition NOT FOUND; treated as unevidenced upside, excluded from SAM per the
  conservative-bias instruction.

### 5E. Final output card

- TAM (conservative / realistic): ₹12,52,452 Cr / ₹13,20,660 Cr (global, PC + premium smartphone
  used-and-refurbished market, CY23, STALE >2yr).
- SAM: ₹1,49,900 Cr (12.0% of conservative TAM) — India + USA + Europe + UAE, organized channel,
  GNG's actual product/capability scope.
- SOM 3yr / 5yr: ₹4,734 Cr / ₹11,154 Cr.
- SOM-implied revenue CAGR: 35.7% (3yr) / 42.5% (5yr) — FORMAL handoff to stage 11.
- Runway: MASSIVE (79.1x headroom, 11.8% TAM growth, company outgrowing TAM ~2.9x).
- Capacity: sufficient through 3yr SOM (17.2% cushion); ₹5,606 Cr gap at 5yr SOM against current
  disclosed facility capacity, bridgeable under the asset-light model but not evidenced by a
  committed capacity-expansion plan.

**Valuation implication line:** "At **35.7-42.5%** revenue CAGR implied by SOM, with margin
trajectory of **NOT FOUND** (EBITDA/PAT margin trajectory data was not injected into this stage;
see stage 11 valuation for margin work), the earnings growth embedded here is **NOT FOUND** CAGR,
which stage 11 should assess against the current valuation of **NOT FOUND** x P/E (P/E not
injected into this stage)." This stage supplies the top-line CAGR input only; margin and multiple
inputs must come from stage 11's own evidence base.

---

## SEARCH LOG

**Performed (11 web searches + full DRHP Industry Overview chapter read/grep):**
1. "India refurbished laptop market size 2025 2026 report crore" — secondary/aggregator hits
   (gminsights, expertmarketresearch), used for directional corroboration only, low confidence.
2. "global refurbished electronics market size 2026 IDC Mordor Intelligence" — Mordor/Coherent/
   Business Research Insights hits, low-tier aggregator confidence, used for directional context.
3. "India ITAD IT asset disposition e-waste market size CAGR" — Coherent/IMARC/Astute Analytica,
   used for adjacent-market context (ITAD ≠ refurbishment core scope).
4. "GNG Electronics Bazaar refurbished laptops market share competitors Cashify Yaantra revenue" —
   Tracxn competitor count, company positioning confirmation.
5. "Attero Recycling Cashify revenue crore FY25" — Entrackr, peer revenue for Method 3.
6. "India e-waste generated 2024 million tonnes government CPCB annual" — CPCB data, context only,
   not used in headline TAM (feedstock proxy, not a refurb-market sizing input).
7. "Back Market revenue 2024 2025 refurbished electronics France global" — Sacra/Getlatka, global
   peer reference for Method 3 divergence explanation.
8. "NewJaisa refurbished laptop revenue crore India" — screener.in/scanx.trade, peer revenue.
9. "UAE Middle East refurbished electronics market size 2024 billion" — CustomMarketInsights, UAE
   geography-filter input (secondary/lower confidence, only source found).
10. "IDC global PC shipments 2023 2024 million units annual total" — IDC-sourced press coverage,
    Method 2 bottom-up unit base.
11. "IDC India PC shipments 2024 million units annual" — IDC-sourced press coverage, Method 2.

DRHP `drhp_text.txt` searched via grep for: "Industry Overview", "refurbished", "market size",
"TAM", "CAGR", "IDC", "Frost", "RedSeer", "billion", "USD", "market leader", "we believe" — no
Frost & Sullivan or RedSeer citation found in the DRHP (1Lattice Report is the sole cited market
study).

**Skipped (making status = partial):**
- Dedicated RedSeer/Frost & Sullivan India-refurb-market report search (DRHP cites only 1Lattice;
  a competing named-firm report was not separately sourced to cross-check 1Lattice's numbers).
- Tablets/servers/workstations standalone submarket sizing (global or India) — not found in DRHP
  or in the searches run; carried as a gap, not estimated.
- UAE/Middle East organized-vs-unorganized refurb-channel split — not found; India's 11% ratio
  used as a flagged proxy in the SAM channel filter.
- Africa-specific refurb market sizing (relevant to GNG's marketed-but-unevidenced "46 countries"
  claim) — not searched; treated as unconfirmed upside only.
- A 2025/2026-vintage primary market report to refresh the CY23/FY24-dated 1Lattice figures — only
  lower-tier aggregator sites (IMARC, Coherent, Grand View Horizon, Custom Market Insights) were
  found for 2026-dated figures, and these were used only for directional corroboration, not as a
  primary TAM input, given their lower reliability relative to the DRHP-cited, underwriter-
  commissioned 1Lattice study.
- India-specific premium-smartphone organized/unorganized channel split — not found; proxy used
  (Section 3A, Filter 3).

---

## STALE DATA FLAGS

| Datapoint | Source | Year | Flag |
|---|---|---|---|
| Global refurb+used PC market ($34.06B/$57.4B) | 1Lattice/DRHP | CY23/28 | STALE (>2yr from run date) |
| Global premium smartphone refurb+used market ($109.9B/$193.7B) | 1Lattice/DRHP | CY23/28 | STALE |
| India refurb-PC market ($0.8B/$3.3B), organized share (11%/32%) | 1Lattice/DRHP | FY24/29 | STALE |
| USA, Europe used+refurb PC and smartphone markets | 1Lattice/DRHP | CY23/28 | STALE |
| India PC penetration (75-95/1,000) | 1Lattice/DRHP | undated within DRHP, filing-vintage | STALE |
| GNG FY24 units (369,320) and revenue/unit (₹30,822) | B04 marker | FY24 | STALE (~2yr) |
| UAE refurbished laptop market ($282.9M) | CustomMarketInsights, web | 2024 | STALE (borderline, ~2yr) |
| Global PC shipments (262.7M units) | IDC, web | 2024 | Not stale (~1.5yr) |
| India PC shipments (14.4M units) | IDC, web | 2024 | Not stale (~1.5yr) |
| Peer revenues (GNG, Cashify, NewJaisa, Attero) | Company disclosures/Entrackr, web | FY25/26 | Not stale |

---

## FLAGS CARRIED TO YAML

1. DRHP internal inconsistency: Risk Factors chapter states $28.3B/$4.6B (global refurb-PC
   CY28 / India refurb-PC FY29) while Industry Overview and Our Business chapters state
   $38.3B/$3.3B for the same two figures (3 of 4 occurrences agree; $3.3B is also the only figure
   consistent with the stated CAGR math). Treated as a drafting error, not a modelling choice.
2. Management's headline TAM claim (Section 1B) mixes non-ICT categories entirely outside GNG's
   product scope; its "reasonable" 1.44x ratio against the conservative estimate here is partly
   coincidental (offsetting scope mismatches), not evidence of disciplined TAM framing.
3. SOM-implied revenue CAGR (35.7%/42.5%) is a mechanical SAM-share extrapolation and should be
   treated by stage 11 as an upper-bound sanity check, not a base-case forecast.
4. 5-year SOM (₹11,154 Cr) exceeds current disclosed facility capacity ceiling (₹5,548 Cr) by
   ₹5,606 Cr; bridgeable under GNG's asset-light, capex-free scaling model but not evidenced by
   any committed, dated capacity-expansion plan in the materials supplied to this stage.
5. UAE and India-premium-smartphone organized-channel shares were not found and were proxied
   using India's PC-market 11% organized ratio — a flagged assumption in the SAM channel filter.
6. Tablets/servers/workstations have no standalone market-sizing data anywhere in the DRHP or in
   the searches performed; this stage's TAM is therefore very likely a modest underestimate of
   the true product-scope TAM, consistent with the conservative-bias instruction but worth noting.
