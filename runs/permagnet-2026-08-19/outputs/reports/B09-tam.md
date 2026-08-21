# B09 — TAM / SAM / SOM Market Sizing: Permanent Magnets Ltd (PERMAGNET)
Run date: 2026-08-19 | Model: claude-sonnet-5 | Stage: B09-tam

FX convention used throughout: USD/INR = 95.70 (Federal Reserve H.10, 18-Aug-2026;
tradingeconomics.com, 18-Aug-2026 spot ~95.74). $1 bn = ₹9,570 Cr; $1 mn = ₹9.57 Cr.
All figures ₹ Crore unless marked USD.

---

## SECTION 1: MARKET DEFINITION

### 1A Precise boundaries

PML is not a single-market company; it is a components/assemblies supplier that
rides three distinct end-markets plus two pre-commercial growth lines. Getting
scope right here determines every number below.

**Product scope (revenue-generating today, FY26 standalone ₹225.46 Cr basis,
AR-FY26 p.4/p.19):**
- Segment A — Metering & current-measurement components: shunts, shunt
  assemblies, current transformers (CT), flux concentrators, brass terminals,
  gas-meter mechanical parts. = electricity-meter components (40%) + CT (9%)
  + gas meters (2%) = 51% of FY26 revenue ≈ ₹115.0 Cr.
- Segment B — Automotive magnetic/current/torque sensing components (Hall
  sensor + flux-concentrator + shield assemblies sold into BMS, MCU, EV and
  ICE platforms) = 23% of FY26 revenue ≈ ₹51.9 Cr.
- Segment C — Specialty alloys (AS9100D aerospace-grade, oil & gas, general
  industrial casting/heat-treatment/vacuum-induction melting) = 10% of FY26
  revenue ≈ ₹22.5 Cr.
- Excluded from headline sizing: "Others" (renewables/electrical/medical/
  aerospace-adjacent/F&B, 16% ≈ ₹36.1 Cr) — too diffuse across unrelated
  end-markets to size with sourced data at the right granularity; excluded
  conservatively (this understates true company TAM, which is the safe
  direction per the conservative-bias rule).

**Explicitly NOT sized into the headline TAM/SAM/SOM (per pipeline
instruction and company-quality discipline):**
- NdFeB rare-earth magnets (Quantum Magnetics subsidiary) — pre-revenue,
  5,000-tonne integrated capacity target by FY31, ₹47.81 Cr ECB drawn,
  generated **zero** revenue in FY26 because Chinese rare-earth export
  restrictions blocked the existing assemblies business (AR-FY26 p.4/p.19).
  Sized separately in Section 5D as far-dated optionality, not summed into
  TAM.
- Latching relays for smart meters — licensed from REL Developments (UK),
  guided commercial ramp H2FY27, management states this is already **behind
  original timelines** (AR-FY26 p.4). Pre-commercial today; treated as a SAM
  expansion lever (5D), not counted in headline TAM/SOM.

**Geographic scope:** Global. PML is a qualified supplier to "the top 3
global electricity meter manufacturers" and "~50% of tier-1 automotive
manufacturers worldwide" (AR-FY26 p.10/p.19). FOB export value ₹106.05 Cr
of ₹225.46 Cr standalone revenue = 47% export / 53% domestic (AR-FY26
financial statements, FOB Value of Exports note). No segment-level export
split disclosed — flagged input gap; company-wide ratio used as proxy where
needed.

**Customer scope:** Tier-1 global auto OEMs/component integrators; top-3
+ domestic electricity-meter manufacturers; AMISPs and DISCOMs indirectly
via meter OEMs; aerospace/oil & gas/industrial alloy buyers (new,
AS9100D-qualified).

**Channel scope:** Direct B2B supply as a qualified component vendor —
PML states it is "often one of only two or three suppliers" for specialised
products (AR-FY26 p.19). Not a retail/aftermarket business.

**Price segment / inclusions & exclusions:** PML sells the current-sensing
and magnetic-assembly *component/module* layer, not the finished meter,
not the sensor semiconductor IC (Allegro/Melexis/Infineon-type players own
that layer), and not the finished automotive module. This is the single
most important scoping decision in this report and is applied as a hard
product-fit filter in Section 3A.

### 1B Management's own TAM claim, and credibility read

Management does not state a company-specific TAM figure. It cites
industry-level context repeatedly to justify strategy:
- "Global Smart Meters market was valued at USD 35.13 billion in 2025... to
  grow from USD 39.58 billion in 2026 to USD 105.43 billion by 2034, at a
  CAGR of over ~13%" (AR-FY26 p.16, source cited: Straits Research,
  Fortune Business Insights, Brightly, Electronics Media, Energy Networks,
  RDSS). Date: 2025 base.
- "Global smart electricity meters segment... USD 29.51 billion in 2026 to
  USD 48.04 billion by 2034... ~6% CAGR" (AR-FY26 p.16-17). Date: 2026.
- NdFeB: "approximately 119,000 tonnes in 2020... projected to rise to
  nearly 387,000 tonnes by 2030" (AR-FY26 p.19; base year 2020 is >4 years
  stale relative to the 19-Aug-2026 run date — used for direction only per
  the staleness rule, never as a headline number here).
- RDSS: "250-million-meter target," "65 million... installed as of April
  2026" (AR-FY26 p.4/p.18).
- Relays: management states relay value is "~5x" PML's existing metering
  component basket and "significantly increases the addressable market"
  (AR-FY26 p.11) — a per-unit value ratio management uses internally, not
  an independent market-size figure.

**Credibility read: BROAD.** Every cited number is total industry/device
market value, not PML's own product-level addressable slice (PML doesn't
sell finished meters, comms modules, or sensor ICs). Management is not
explicitly claiming "this $35bn is our TAM" — it is citing macro context —
but no document translates the industry figure down to PML's actual
component/assembly opportunity. Held for the Section 2 ratio comparison
below with that caveat attached, so the ratio is read as a scope mismatch
first, "inflation" second.

---

## SECTION 2: TAM ESTIMATION, MULTIPLE METHODS

### Segment A — Metering & current-measurement components

**Method 1, top-down.** Global smart electricity meters device market:
USD 29.51 bn (2026) → USD 48.04 bn (2034), >6% CAGR (AR-FY26 p.16-17,
Straits Research/Fortune Business Insights et al., current data, not
stale). Converted: USD 29.51 bn × ₹9,570 Cr/$bn = **₹282,431 Cr** (2026,
global, total finished-device value — includes comms module, metrology IC,
enclosure, install/O&M pass-through cost that PML does not supply).

No industry report was found that sizes the shunt/CT/flux-concentrator
component slice specifically (searched: BOM cost breakdown, current-sensing
resistor market). General component literature indicates current-sensing
hardware adds roughly $3-9 to a meter BOM against typical landed device
costs; this is not precise enough to anchor a % on its own, so it is used
only to bound a plausibility range. **Analyst-derived component-content
ratio applied: 2% (conservative) / 4% (realistic)** — explicitly flagged
LOW confidence, not directly sourced at PML's exact product granularity.
- Conservative: ₹282,431 Cr × 2% = **₹5,649 Cr**
- Realistic: ₹282,431 Cr × 4% = **₹11,297 Cr**
Plausibility check: PML's Segment A revenue (₹115.0 Cr) ÷ ₹5,649 Cr = 2.0%
implied global share — reasonable for a qualified-but-not-exclusive
component vendor to "top 3" meter makers, not absurd.

**Method 2, bottom-up (India, peer-cross-checked).** Genus Power
Infrastructures — India's largest listed smart-meter AMISP — reported FY26
revenue of ₹4,821 Cr on a self-disclosed "~30% of India smart-meter market
share" (SolarQuarter/SmeStreet, FY26 results, current). Implied India
smart-metering **industry** annual revenue (TOTEX-inclusive, all AMISPs,
FY26 run-rate) ≈ ₹4,821 Cr ÷ 0.30 = **₹16,070 Cr**. This is device + 10-year
O&M value, not component value; applying the same 2-4% component ratio:
₹321 Cr (conservative) to ₹643 Cr (realistic), **India-only, current-year
run-rate** — shown as context for the RDSS growth driver, not summed on
top of the global Method-1 figure (would double-count).

**Method 3, peer revenue aggregation.** No listed pure-play component
peer was found (searches for shunt/CT/component-only competitors returned
only system-level names — BHEL, ABB India, Siemens, CG Power, Waaree,
Suzlon, Thermax — none of which compete in PML's actual product layer;
flagged as a false-peer result, not usable). Unorganised-sector estimate:
NOT FOUND at the component-supplier level. Method 3 is data-constrained
for Segment A; not used to anchor the range, only cross-checked via
Method 2's peer input (Genus).

**Method 4, import substitution.** India smart-meter manufacturing
capacity ≈100 million meters/year, judged sufficient for the RDSS
timeline (Power Line Magazine/PFI reporting, ~2025). Remaining rollout:
250 mn target − 65 mn installed (Apr-2026) = **185 mn meters still to be
installed** by the extended March-2028 completion date — this is the
concrete unit-volume runway behind Segment A's growth, used in Section 4A/
5B rather than as a separate TAM figure (would double count Method 2).

**Method 5, global benchmark.** Smart-meter penetration: USA ~94%,
Canada ~96%, EU ~63%, Australia ~57%, India ~26% (65mn/250mn RDSS target;
AR-FY26 p.16). India sits well below every developed-market benchmark —
supports a multi-year penetration runway, feeding Section 4A, not a
standalone TAM number.

**Segment A triangulation table**

| Method | Estimate (₹ Cr) | Confidence | Staleness |
|---|---|---|---|
| 1 Top-down (global, 2% ratio) | 5,649 | L (ratio unsourced at product level) | Not stale (2026 base) |
| 1 Top-down (global, 4% ratio) | 11,297 | L | Not stale |
| 2 Bottom-up (India, peer cross-check) | 321-643 | M (peer-sourced base, ratio unsourced) | Not stale |
| 3 Peer aggregation | NOT FOUND | — | — |
| 4 Import substitution | context only (185mn units) | H (unit volumes directly sourced) | Not stale |
| 5 Global benchmark | context only | H | Not stale |

**Segment A TAM: conservative ₹5,649 Cr / realistic ₹11,297 Cr** (global
basis; India Method-2 figure is a subset, shown for driver context).

### Segment B — Automotive magnetic/current/torque sensing

**Method 1, top-down.** Estimates diverge materially (>1.5x):
- "Automotive current sensor market projected at USD 2.34 billion in 2026...
  USD 5.28 billion in 2032" (14.2% CAGR) — one aggregator.
- "Automobile Current Sensor Market... USD 3.2 billion in 2024... USD 5.8
  billion by 2033" (6.5% CAGR 2026-2033) — a second aggregator; 2026
  implied value ≈ USD 3.63 bn.
Per the conservative-bias rule, the lower figure anchors the conservative
case: USD 2.34 bn × ₹9,570 Cr/$bn = **₹22,394 Cr** (conservative); USD 3.63
bn × ₹9,570 = **₹34,739 Cr** (realistic, higher-CAGR source). Flagged:
methods diverge >1.5x, not averaged — divergence explained by differing
market definitions (sensor-IC-inclusive vs module-only scope, neither
report specifies precisely).

**Method 2, bottom-up.** Not usable independently: no sourced global
automotive-electrification unit count × PML-specific content-per-vehicle
figure exists in the material gathered. NOT FOUND at the required
precision; not fabricated.

**Method 3, peer aggregation.** No listed Indian peer found supplying the
same magnetic-assembly/current-sensing-module layer to global Tier-1 autos.
NOT FOUND.

**Method 4, import substitution.** Not directly applicable — this is an
export-facing, developed-market-customer business (Western EV OEMs per
AR-FY26 p.4), not an India-import-substitution play.

**Method 5, global benchmark.** China's EV makers are gaining share from
Western incumbents PML supplies (AR-FY26 p.4-5: "Chinese manufacturers
continue to gain share globally... we are widening our customer base").
This is a **risk to Segment B's realistically-capturable share**, not a
TAM expander — carried into Section 4B, not Section 2.

**Segment B TAM: conservative ₹22,394 Cr / realistic ₹34,739 Cr** (global,
full current-sensor market value — note this includes semiconductor IC
content PML does not supply; the product-fit filter in Section 3A does the
real narrowing work for this segment).

### Segment C — Specialty alloys

**Method 1, top-down (mismatched, rejected as headline).** Global specialty
alloys market: USD 52,957 mn (2021) → USD 62,680 mn (2026E) (Cognitive
Market Research). Converted: USD 62,680 mn × ₹9.57 Cr/$mn = **₹599,844 Cr**.
This is a mature, majors-dominated global market (steel/superalloy
producers); using it as PML's TAM would be nonsensical for a single-new-
furnace niche entrant (implied 0.004% share) — **explicitly excluded as
scope-mismatched**, shown only to demonstrate why it was rejected. 2021
base year is 5 years stale — directional only even if it had been used.

**Method 1b, narrower proxy.** India investment-casting market (turbine
blades, valve bodies, impellers — aerospace/defence/pump end-uses, closest
scope match to PML's AS9100D + oil & gas + industrial alloy casting):
USD 313.51 mn (2024) → USD 498.16 mn (2033), 5.28% CAGR (IMARC Group).
2026 estimate: 313.51 × 1.0528² ≈ USD 347.5 mn × ₹9.57 Cr/$mn = **₹3,325
Cr**. A broader "India metal forging market" figure was also found (USD
5.08 bn in 2023 → USD 9.75 bn by 2030, 9.8% CAGR; 2022 base is 4 years
stale) — this is 17x larger and captures automotive/general steel forging
far outside PML's niche; per conservative bias, the lower/narrower
investment-casting figure is used. Plausibility check: PML Segment C
revenue ₹22.5 Cr ÷ ₹3,325 Cr = 0.68% implied share — reasonable for a
recently-commercialised single-furnace entrant.

**Method 2, bottom-up.** NOT FOUND at PML's exact niche granularity
(aerospace-grade + oil & gas alloy casting specifically, as opposed to
general investment casting). Flagged input gap.

**Method 3, peer aggregation.** NOT FOUND — no comparable listed Indian
specialty-alloy-casting peer identified in this search set.

**Method 4/5.** Not applicable / no additional sourced data found.

**Segment C TAM: single-method estimate ₹3,325 Cr** (India only; global
opportunity beyond India flagged as directionally real — AS9100D
certification, growing oil & gas/aerospace/industrial enquiries per
AR-FY26 p.11 — but not sized, LOW confidence, single method only).

### Headline TAM (sum of Segments A + B + C; NdFeB and relays excluded)

| Segment | Conservative (₹ Cr) | Realistic (₹ Cr) | Confidence |
|---|---|---|---|
| A — Metering/current-measurement components | 5,649 | 11,297 | L-M |
| B — Automotive sensing | 22,394 | 34,739 | L (methods diverge >1.5x) |
| C — Specialty alloys | 3,325 | 3,325 (single method) | L |
| **TAM total** | **31,368** | **49,361** | — |

**Management claim vs conservative estimate:** Management's cited context
figure (global smart meters market, USD 35.13 bn, 2025) = ₹336,194 Cr.
Ratio = 336,194 ÷ 31,368 = **10.7x**. Standard read: >2x = likely
inflated. **Read here: inflated relative to PML's actual product-level
TAM, but the gap is a scope mismatch (total finished-device/global-market
context vs PML's component/assembly slice), not a direct company-specific
claim by management** — see Section 1B credibility note. Recorded as
`inflated` per the formal rule, with the mismatch explanation carried
forward so it is not mistaken for dishonesty about PML's own opportunity.

---

## SECTION 3: SAM & SOM

### 3A SAM — five filters applied to TAM

**Segment A (metering/current-measurement).** Product fit is already
embedded in the 2-4% component-content ratio used in Section 2 (retain
100%, no further product discount to avoid double-counting). Geography:
PML is qualified with "top 3" global meter makers but not the whole
market (e.g., China's largely closed domestic supply chain) → retain 70%.
Channel: established relationships with existing customers → retain 90%.
Capability: 6 facilities being consolidated into one site, capacity
build-out in progress (B07 capex-embedded growth signal) → retain 85%.
Combined factor = 0.70 × 0.90 × 0.85 = 0.5355.
- SAM(A) conservative = ₹5,649 Cr × 0.5355 = **₹3,025 Cr**

**Segment B (automotive sensing).** This is where the real narrowing
happens: PML supplies magnetic-assembly/module content around
semiconductor current-sensor ICs, not the ICs themselves. Product fit:
retain 15% (assembly/passive-component value share of a sensor-IC-
inclusive TAM — analyst estimate, LOW confidence, no sourced BOM split
found). Geography: "~50% of tier-1 automotive manufacturers worldwide"
already served → retain 60% (Chinese-OEM share gains and non-tier-1
players outside reach). Channel: established Tier-1 relationships →
retain 90%. Capability: retain 85% (same capacity caveat as Segment A).
Combined factor = 0.15 × 0.60 × 0.90 × 0.85 = 0.0689.
- SAM(B) conservative = ₹22,394 Cr × 0.0689 = **₹1,543 Cr**

**Segment C (specialty alloys).** Product fit: PML's AS9100D/oil & gas/
industrial casting is a premium sub-slice of the broader investment-
casting market → retain 60%. Geography: India-focused currently →
retain 80% (most of the India market theoretically reachable given
"growing enquiries" across oil & gas, aerospace, industrial — AR-FY26
p.16). Channel: new customer relationships still converting → retain 70%.
Capability: new furnace operating "at close to optimum capacity" through
Q4FY26 (AR-FY26 p.4) → retain 90%.
Combined factor = 0.60 × 0.80 × 0.70 × 0.90 = 0.3024.
- SAM(C) conservative = ₹3,325 Cr × 0.3024 = **₹1,006 Cr**

**Total SAM (conservative) = 3,025 + 1,543 + 1,006 = ₹5,574 Cr**
**SAM as % of TAM (conservative) = 5,574 ÷ 31,368 = 17.8%**

### 3B SOM at 3 and 5 years

Current segment-matched revenue base (Segments A+B+C, FY26 standalone,
84% of total company revenue): ₹115.0 + ₹51.9 + ₹22.5 = **₹189.4 Cr**.
Current share of SAM = 189.4 ÷ 5,574 = **3.4%**.

**Share-gain trajectory chosen: NORMAL-to-moderately-aggressive, not full
aggressive.** Evidence for aggressive (3-5pp): real capacity build in
progress (B07 capex-embedded growth ~32.7%, new alloys furnace
commissioned Q4FY26, ECB drawn for Quantum Magnetics, land acquired for a
consolidated facility). Evidence against full aggressive: management
explicitly states relays are "behind our original timelines"; Quantum
Magnetics generated zero revenue in FY26 from an existing line due to an
external shock (China export restrictions); FY25 was a "consolidation"
(flat) year before FY26's 13% recovery. Net: **+1.5pp by year 3, +3.0pp
cumulative by year 5** — inside but toward the low end of the "aggressive"
band, justified by capacity evidence but discounted for the demonstrated
execution-timing risk.

- SOM share, yr3 = 3.4% + 1.5pp = 4.9%
- SOM share, yr5 = 3.4% + 3.0pp = 6.4%

SAM is grown at the blended TAM CAGR (see Section 4/5B: ≈6.3%, weighted by
conservative TAM shares: A 18.0% weight × 6% + B 71.4% weight × 6.5% + C
10.6% weight × 5.28% ≈ 6.3%):
- SAM, yr3 = ₹5,574 Cr × 1.063³ = **₹6,696 Cr**
- SAM, yr5 = ₹5,574 Cr × 1.063⁵ = **₹7,569 Cr**

**SOM, yr3 = ₹6,696 Cr × 4.9% = ₹328 Cr**
**SOM, yr5 = ₹7,569 Cr × 6.4% = ₹484 Cr**

Implied revenue CAGR from current segment-matched base (₹189.4 Cr):
- yr3: (328 ÷ 189.4)^(1/3) − 1 = **20.1%**
- yr5: (484 ÷ 189.4)^(1/5) − 1 = **20.6%**

This covers the 84% of FY26 revenue inside Segments A+B+C. The excluded
16% ("Others") is not modelled — stage 11 should treat this CAGR as
applying to ~84% of the current revenue base, with the remainder assumed
flat/NOT FOUND, which is the conservative direction.

**FORMAL HANDOFF to stage 11 (revenue growth cross-check):
SOM-implied revenue CAGR ≈ 20.1% (yr3) / 20.6% (yr5).**

### 3C Capacity cross-check

B07 capex-embedded growth (indicative, balance-sheet-residual method):
**~32.7%**. SOM-implied revenue CAGR: **~20.1-20.6%**. Capex-embedded
growth **exceeds** the demand-side SOM CAGR by roughly 12pp.

**Read: capacity is sufficient — not the binding constraint.** The gap
runs the other way: the capex plan implies *more* growth than the
conservative, demand-anchored SOM. The most consistent explanation is that
the excess capacity signal is aimed at the two lines explicitly excluded
from this SOM (latching relays, Quantum Magnetics NdFeB) rather than at
Segments A/B/C's baseline demand. **The capex plan is the more optimistic
side of this comparison**, and given relays are already running behind
schedule and Quantum Magnetics booked zero revenue in FY26, that
optimism carries real execution risk — flagged, not resolved.

---

## SECTION 4: GROWTH DRIVERS, RISKS & STRUCTURE

### 4A TAM growth drivers

| Driver | Impact | Evidence |
|---|---|---|
| Regulatory tailwind (RDSS) | HIGH | 250mn target, only 65mn installed (26%) as of Apr-2026; scheme extended to Mar-2028; ~185mn units still to install (AR-FY26 p.18) |
| Penetration gap | HIGH | India ~26% smart-meter penetration vs USA ~94%, Canada ~96%, EU ~63%, Australia ~57% (AR-FY26 p.16) |
| Import substitution (rare earth) | MEDIUM (mixed — also a risk, see 4B) | China ~92% of global NdFeB capacity; export restrictions creating a case for Indian supply chain (DAE/AMD backing cited); but same restrictions zeroed Quantum Magnetics' FY26 revenue |
| New applications / tech enablement | MEDIUM | EV current/torque sensing demand; AS9100D certification opening aerospace/defence (Tejas Mk1A programme context) |
| Formalisation / import substitution (relays) | MEDIUM, pre-commercial | Licensing agreement with REL Developments (UK); management's internal "~5x value" framing (AR-FY26 p.11) |
| Geographic/customer expansion | MEDIUM, early | Alloys division targeting oil & gas, aerospace, industrial customers with "growing enquiries" (AR-FY26 p.4) |

### 4B TAM risks

| Risk | Monitoring signal |
|---|---|
| Rare-earth supply-chain volatility (China ~92% share) | Already caused zero FY26 revenue in the Quantum Magnetics assemblies line; monitor Chinese export-licence announcements and DAE/AMD-backed domestic feedstock progress |
| Execution/timeline slippage | Relays explicitly "behind our original timelines" (AR-FY26 p.4); monitor H2FY27 commercial-ramp guidance for further slips |
| Import competition / vertical integration by IC majors | Allegro/Melexis/Infineon/TI-type players could integrate the magnetic-assembly layer PML occupies; monitor Segment B customer concentration |
| Customer-base cyclicality | Western EV OEM demand "broadly stable" but Chinese OEMs "continue to gain share globally," pressuring PML's core Western Tier-1 customer base (AR-FY26 p.4) |
| RDSS programme/funding risk | Scheme already extended once (2028 vs original target); dependent on DISCOM financial health and state participation; AT&C losses still 15.04% (FY25) vs 12-15% target band (AR-FY26 p.17) |

### 4C Market structure

- **Metering components:** Oligopolistic on the supply side — PML is "often
  one of only two or three suppliers" to specialised customers and holds
  relationships with the "top 3 global electricity meter manufacturers"
  (AR-FY26 p.10/p.19). On the demand side, India's smart-meter rollout is
  consolidating around large AMISPs (Genus Power alone holds ~30% share,
  order book ₹25,173 Cr) — fewer, larger customers for PML's components.
- **Automotive sensing:** Fragmented among specialised assembly/component
  players; PML sits below the semiconductor-IC layer occupied by larger,
  better-capitalised global names.
- **Specialty alloys:** Fragmented in India; PML is a small, newly-
  commercialised entrant (single new furnace, Q4FY26) against established
  diversified foundries and imports.
- **NdFeB (not in headline TAM but structurally relevant):** Globally
  concentrated — China ~92% of production capacity (AR-FY26 p.19). India
  has near-zero domestic capacity today; large white space, very high
  capital/technology/feedstock barriers.

---

## SECTION 5: SUMMARY & RUNWAY

### 5A Funnel

```
TAM (conservative)  ₹31,368 Cr   [A ₹5,649 + B ₹22,394 + C ₹3,325]
   ↓ (17.8%)
SAM (conservative)  ₹5,574 Cr    [A ₹3,025 + B ₹1,543 + C ₹1,006]
   ↓ (current share 3.4%)
Current captured    ₹189.4 Cr    [FY26 standalone, Segments A+B+C only]
   ↓ (share gain +1.5pp / +3.0pp)
SOM yr3             ₹328 Cr      (4.9% of SAM yr3 ₹6,696 Cr)
SOM yr5             ₹484 Cr      (6.4% of SAM yr5 ₹7,569 Cr)
```
Excluded from this funnel, sized separately below: latching relays
(pre-commercial), NdFeB/Quantum Magnetics (far-dated).

### 5B Runway assessment

- Revenue headroom = SAM ÷ current segment revenue = ₹5,574 Cr ÷ ₹189.4 Cr
  = **29.4x**.
- TAM growth rate (blended, conservative-share-weighted) ≈ **6.3%**.
- Company CAGR vs TAM: FY26 standalone revenue grew 13% YoY (AR-FY26 p.4)
  vs TAM growth ~6.3% → **PML is gaining share**, roughly 2x the market's
  growth rate, consistent with the positive SOM share-gain trajectory
  assumed above.
- Years to saturate SAM at current growth: at 13% company growth,
  ln(29.4)/ln(1.13) ≈ **28 years**; at the higher SOM-implied ~20% CAGR,
  ln(29.4)/ln(1.20) ≈ **18-19 years**. Either way, a multi-decade runway —
  the constraint is execution and share-capture speed, not market size.

### 5C Runway classification: **STRONG**

Mechanically, 29.4x headroom and an 18-28 year saturation horizon would
map to MASSIVE on a headroom-only reading. Held at **STRONG** instead,
for three documented reasons: (1) Segment B — the largest TAM
contributor at 71% of the conservative total — already carries the
heaviest SAM discount in this report (0.0689x) because PML occupies the
assembly layer, not the IC layer, of that market; the "headroom" there is
mostly value PML structurally cannot capture. (2) Two of the company's
most capacity-intensive growth bets (relays, NdFeB) are excluded from this
SOM entirely and carry demonstrated execution slippage. (3) PML is a
sub-₹1,000 Cr revenue micro-cap; converting even a few percentage points
of SAM share requires customer-qualification cycles measured in years, as
the relay delay itself illustrates.

### 5D SAM expansion levers actually being pursued

- **Latching relays** (H2FY27 guided, already delayed once): management's
  own framing is that relay value is "~5x" the current metering-component
  basket per unit (AR-FY26 p.11). Not quantified into SAM here (pre-
  commercial, no market-size figure independent of this internal ratio was
  found) — flagged as the single largest near-term SAM-expansion lever if
  commercialisation holds to the H2FY27 guide, and as an execution risk if
  it slips again.
- **NdFeB / Quantum Magnetics** (far-dated, FY31 target): 5,000-tonne
  integrated capacity target. Illustrative back-of-envelope only (NOT a
  forecast): at a rough blended NdFeB price of ~$50,000-70,000/tonne,
  5,000t × ~$60,000/t ≈ USD 300 mn ≈ **₹2,870 Cr** of potential *annual*
  revenue *at full FY31 capacity utilisation* — an order of magnitude
  above PML's current total revenue. This is a call option, not a
  probability-weighted addition to TAM/SAM/SOM: FY26 revenue from the
  predecessor assemblies line was zero due to Chinese export restrictions,
  Phase 2 (block cutting/machining/surface treatment) is not commercial
  until Q3FY27, and the FY31 date is 5 years out. Explicitly excluded from
  every headline number above.
- **Alloys export/aerospace expansion:** AS9100D certification and
  "growing enquiries" across oil & gas/aerospace/industrial (AR-FY26 p.4)
  — modest, already partially reflected in Segment C's SAM.

### 5E Final output card

- TAM (conservative / realistic): **₹31,368 Cr / ₹49,361 Cr**
- SAM: **₹5,574 Cr** (17.8% of conservative TAM)
- Current SAM share: **3.4%** | Revenue headroom: **29.4x**
- SOM yr3 / yr5: **₹328 Cr / ₹484 Cr**
- SOM-implied revenue CAGR: **20.1% (yr3) / 20.6% (yr5)**
- Runway class: **STRONG**
- Capacity check: **sufficient** — capex-embedded growth (~32.7%) exceeds
  the SOM-implied CAGR (~20%); the capex plan is the optimistic side of
  this comparison, likely aimed at the excluded relay/NdFeB optionality.

**Valuation implication line:** Margin trajectory — FY26 standalone EBITDA
margin was 17%, up from 14% in FY25 (AR-FY26 p.4). No forward margin
guidance was found (NOT FOUND), so margin is held flat at 17% here as the
conservative convention (no further expansion assumed) rather than
estimating a number. On that convention, earnings growth tracks revenue
growth.

*"At ~20% revenue CAGR implied by SOM, with margin trajectory held flat at
17% (no forward guidance found), the earnings growth embedded here is
~20% CAGR, which does not clearly support the current valuation of ~36x
P/E (most recent found: 36.33x, 21-Jul-2026; PE has ranged 31x-50x through
2026 — flagged as volatile/dated relative to the 19-Aug-2026 run date).
PEG ≈ 1.8x on this reading — rich for the demand-anchored, conservative
SOM. The gap is only closed if the excluded, execution-dependent
optionality (relays, NdFeB) converts — which is precisely the part of the
story this report has deliberately kept out of the headline numbers."*

---

## SEARCH LOG

**Searches performed (12):**
1. global current sensor market size 2026 forecast shunt resistor Hall sensor
2. automotive current sensing market size 2026 2030 CAGR
3. NdFeB permanent magnet market size 2026 India forecast tonnes value
4. India specialty alloys market size aerospace oil gas industrial 2026
5. "Permanent Magnets Limited" competitors peers shunt current transformer manufacturer India
6. smart meter relay market size latching relay electricity meter
7. India RDSS smart meter cumulative investment USD 30 billion component supply chain localisation
8. smart electricity meter BOM cost breakdown shunt current sensor component cost per unit
9. Genus Power Infrastructures revenue FY26 smart meter India market share
10. India investment casting precision forging market size aerospace defence oil gas 2026 crore
11. Permanent Magnets Ltd PERMAGNET share price PE ratio 2026 NSE BSE
12. USD INR exchange rate August 2026

**Searches skipped:** none forced by quota/tool errors — status is
`complete`. Data gaps that remained after searching are recorded as
`input_gaps`/`flags` below rather than fabricated.

---

## INPUT GAPS

- Segment-level export/domestic revenue split not disclosed by PML; used
  company-wide FOB export ratio (47%) as a proxy where needed.
- No industry-sourced BOM component-cost % for shunts/CT within a smart
  meter's total device value; used an analyst-derived 2-4% range, flagged
  LOW confidence, cross-checked for plausibility against PML's implied
  market share.
- No sourced automotive assembly-vs-IC value split for current-sensing
  modules; used an analyst-derived 15% product-fit retention, flagged LOW
  confidence.
- No sourced India-specific specialty-alloys market at PML's exact niche
  (aerospace + oil & gas alloy casting specifically); used the India
  investment-casting market as the nearest scope proxy.
- No listed pure-play component peer found for Method 3 (peer aggregation)
  in Segments A, B, or C — flagged NOT FOUND rather than estimated.
- PE ratio found is volatile across 2026 (31x-50x range across different
  dates); most recent found (36.33x, 21-Jul-2026) used, may not equal the
  19-Aug-2026 run-date price exactly.
