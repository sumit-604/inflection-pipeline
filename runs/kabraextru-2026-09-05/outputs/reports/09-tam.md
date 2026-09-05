# STAGE 9: TAM / SAM / SOM — Kabra Extrusiontechnik Ltd (KABRAEXTRU)
Run date: 2026-09-05 | Model: claude-sonnet-5

KABRA is a hybrid, two-segment company (B04). Because the two segments sit
on structurally unrelated demand curves (government infra capex cycle vs
EV/battery adoption), this report sizes TAM/SAM/SOM SEPARATELY per segment
and sums them for the combined, company-level figures the YAML schema
requires. Every combined number in Section 5 and the YAML block is the
arithmetic sum of the two segment tables built in Sections 2-3.

---

## SECTION 1: MARKET DEFINITION

### 1A — Precise boundaries

**Segment 1 — Extrusion Machinery**
- Product scope: capital-goods machinery that extrudes plastic pipe
  (PVC/HDPE/PPR), blown film, sheet, and compounding lines, plus spares
  and after-sales service. Excludes injection-molding and blow-molding
  machinery (a different process; Windsor Machines makes both, KABRA does
  not disclose making either).
- Geographic scope: primarily India. Consolidated geographic-segment note
  (AR26, Note on segment revenue, PDF p.~115 area, lines 6177-6179 /
  9393-9395 of the text twin) shows FY26 revenue India ₹391.92 Cr
  (39,191.86 + ... Lakh) vs Outside India ₹57.52 Cr — i.e. ~87% domestic,
  ~13% export, BLENDED across both segments (AR does not split
  geography by segment). Treated as primarily India; export shown as
  global context only (1A/Section 2 Method 5 not separately built; see
  Section 4).
- Customer scope: organized-sector plastic pipe and film/sheet
  processors, buying engineered capital equipment (multi-lakh to
  multi-crore ticket machines), not the end consumer of pipes or film.
- Channel scope: direct B2B machinery sale, export via distributors in
  100+ countries (AR26 p.34, "over 100 countries").
- Explicit exclusions: the downstream PIPE or FILM market itself (KABRA
  sells the machine, not the pipe); the informal/cottage single-screw
  extruder segment serving small-scale recyclers; raw-material (PVC
  resin) markets.

**Segment 2 — Battery Division (Geon, erstwhile Battrixx)**
- Product scope: lithium-ion battery PACKS and BMS, assembled from
  globally-sourced cells ("technology-agnostic... sourcing cells
  globally," AR26 p.34/36-37) — i.e. pack-assembly + integration value,
  explicitly EXCLUDING cell manufacturing, which GEON does not do.
- Geographic scope: India. No export battery revenue is disclosed
  anywhere in AR25 or AR26; treated as India-only (NOT FOUND: any
  battery export revenue split).
- Customer scope: EV OEMs (2W/3W/4W/E-CV), plus RESS/BESS, telecom,
  inverter, and a nascent D2C line. Mobility is ~70-80% of GEON's own
  revenue mix, energy-storage/other ~20-30% (AR26 p.34).
- Channel scope: direct OEM supply (B2B) + emerging D2C retail.
- Explicit exclusions: cell manufacturing (excluded by GEON's own
  stated model); grid-scale utility BESS (a different customer set —
  large system integrators — with no disclosed GEON presence at that
  scale); ICE 2W/3W battery replacement (lead-acid) markets.

A wrong-scope risk flagged up front: management's own cited "battery
pack market" figures span nearly two orders of magnitude between AR25
and AR26 (Section 1B, Section 2). Getting this boundary right is the
single highest-leverage judgment in this report.

### 1B — Management's own TAM claims (held for Section 2 comparison)

| Claim | Definition given | Date / source | Credibility read |
|---|---|---|---|
| Global plastic extrusion machinery market USD 7.74bn (2025) → USD 8.24bn (2026) → USD 12.22bn by 2032, CAGR 6.72% | Global, all extrusion machinery types (single/twin/multi-screw) | AR26 p.32, "Research and Markets" cited, text-twin line 1765 | Specific (named source, exact years/CAGR) but GLOBAL, not India, and not KABRA-specific |
| Blown film extrusion machine market USD 8.2bn (2025) → USD 12.7bn (2035), CAGR 4.5% | Global | AR26 p.33, "Future Market Insights Inc.", line 1809 | Specific, global, adjacent sub-segment only |
| India plastic pipes market USD 2.10bn (2025) → USD 3.65bn (2034), CAGR 6.30% | India, END-PRODUCT pipe market (not machinery) | AR26 p.33, "IMARC Group", line 1820 | Specific but wrong layer of the value chain (pipes, not the machines that make pipes) — a genuine demand driver for extrusion machinery, not itself the machinery TAM |
| "India's EV battery pack market...rising from USD 39.39 million in 2025 to USD 53.76 million in 2026...to USD 254.59 million by 2031, CAGR 36.5%" | India, battery PACKS specifically (matches GEON's product scope) | AR26 p.32, "Mordor Intelligence", lines 1888-1890, CURRENT-year AR | Specific-LOOKING (named source, exact years, precise CAGR) but INTERNALLY INCONSISTENT — see finding below |
| "Indian EV battery market...projected to grow from USD 2.22 billion in 2024 to USD 13.89 billion by 2033" | India, broader "EV battery market" (undefined whether cells+packs or packs only) | AR25 p.4-5/173, prior-year AR, ~1.3yr old at run date | Broad (definition of what's included is not stated) but directionally corroborated by independent data (Section 2) |
| "~40% market share in its product category as on FY25" | Extrusion, "product category" UNDEFINED | AR25 p.37 only; ABSENT from AR26 | Broad — undefined denominator, unsourced, and dropped by the company itself one year later |

**Load-bearing finding (flagged, carried to Section 2):** GEON's own FY26
Battery Division segment revenue is ₹136.11 Cr (Note 38). The AR26
Mordor citation puts the ENTIRE India EV battery pack market at USD
53.76 million in 2026 ≈ ₹507.5 Cr (at ₹94.4/USD, Trading Economics spot,
04-Sep-2026). That would put GEON — self-described as an "early mover,"
not the dominant player — at ~27% of the entire national market. No
other statement anywhere in AR25 or AR26 claims anything close to that
share. The AR26 citation is treated as a scope/definitional error (most
likely referencing a narrow report definition, not the market GEON
actually competes in), not as a usable TAM ceiling. This is exactly the
"~100x apart" discrepancy flagged at stage 5/company memory between the
AR25 and AR26 battery-market citations (AR25: ~USD 2.22bn 2024; AR26:
~USD 0.039bn 2025 — a ~57x gap for a comparable near-term year).

---

## SECTION 2: TAM ESTIMATION, MULTIPLE METHODS

FX used throughout: ₹94.4/USD (Trading Economics, spot 04-Sep-2026, via
WebSearch — searches_performed).

### 2.1 EXTRUSION MACHINERY SEGMENT

**Method 1 — Top-down (India-specific aggregator reports)**

Two independent aggregator citations found via WebSearch (WebFetch to
verify primary methodology was EGRESS_BLOCKED on both hosts —
grandviewresearch.com and 6wresearch.com; see searches_skipped):

(a) "India Plastic Extrusion Machinery Market": USD 571.2 million by
2030, CAGR 5.1% (2023-2030 stated). Back-solve 2023 base:
571.2 / 1.051^7 = 571.2 / 1.4170 = **USD 403.1M** (2023).
Project to 2026: 403.1 × 1.051^3 = 403.1 × 1.1609 = **USD 468.0M**.
× ₹94.4 = **₹4,418 Cr** (2026).

(b) "India Extrusion Machinery Market" (all materials, plastics being
"the largest revenue generating material segment"): USD 519.8M (2023) →
USD 734.6M by 2030, CAGR 5.1% (2024-2030). Project 2023→2026:
519.8 × 1.1609 = **USD 603.5M** (all materials) × ₹94.4 = **₹5,697 Cr**.
Applying a 70% plastics share (directional only, no sourced split found
— NOT FOUND exact %): ₹5,697 Cr × 0.70 = **₹3,988 Cr**.

Both routes converge to roughly **₹3,988 – ₹4,418 Cr**. Midpoint used:
**₹4,200 Cr** (2026, India, plastics extrusion machinery, top-down,
M confidence — base years 3 years old, forward-projected on a stated
CAGR; STALE base flagged).

**Method 3 — Peer revenue aggregation**

Known LISTED organized-sector peers, FY26 total revenue (screening data
sheets):
- KABRA Extrusion segment: ₹314.94 Cr (451.05 − 136.11, Note 38)
- Rajoo Engineers (pure extrusion-machinery player): ₹298.29 Cr
- Windsor Machines: ₹566.52 Cr (CAVEAT: diversified into blow-molding
  and rubber-processing machinery too — not pure extrusion; included at
  full value as an upper-bound, no sourced split available)

Known-listed total = 314.94 + 298.29 + 566.52 = **₹1,179.75 Cr**

Add explicit unorganised-sector estimate (framework-standard 30-60%
range for India, per the stage-9 method spec, not a company-specific
fabricated number):
- At 30% unorganised: 1,179.75 / (1-0.30) = **₹1,685 Cr**
- At 60% unorganised: 1,179.75 / (1-0.60) = **₹2,949 Cr**

This EXCLUDES known unlisted large players (e.g., Lohia Corp Ltd, a
material unlisted maker of tape/raffia extrusion machinery) — revenue
NOT FOUND (private company, no public filing accessed). Flag: peer
aggregation likely understates the true organized-sector total for this
reason, independent of the unorganised-sector add-on.

**Triangulation — Extrusion Machinery TAM**

| Method | Estimate (₹Cr, 2026) | Confidence | Staleness |
|---|---|---|---|
| Top-down (aggregator reports) | 3,988 – 4,418 (mid 4,200) | M | Base years 2023, STALE, projected forward |
| Peer aggregation (30-60% unorganised) | 1,685 – 2,949 | L-M | Current (FY26 peer data), but excludes unlisted majors |
| Management implied (back-calc from "~40% share") | 314.94 / 0.40 = **787.5** | L | Undefined denominator |

Methods diverge materially (peer-aggregation low end to top-down: ~2.5x).
Explanation: peer aggregation excludes unlisted majors (Lohia Corp and
smaller regional makers) and likely undercounts true organized-sector
depth; top-down aggregator figures are broader industry-report
extrapolations from 3-year-old base data. Per CONSERVATIVE BIAS:

- **Conservative estimate: ₹1,685 Cr** (peer aggregation, 30% unorganised)
- **Realistic estimate: ₹4,200 Cr** (top-down)

Management's implied TAM from its own "~40% market share" claim
(₹787.5 Cr) is BELOW both independent estimates (ratio 787.5/1,685 =
0.47x conservative, 787.5/4,200 = 0.19x realistic) — i.e., for the claim
to be true, "its product category" must be a narrow, undisclosed slice
of the market roughly one-fifth to one-half the size of the market this
report independently sizes. Since that slice is never defined, and the
claim itself vanished entirely from AR26, this reads as unverifiable
rather than as genuine conservatism — flagged, not scored as reliable.

### 2.2 BATTERY DIVISION (GEON) SEGMENT

**Method 1 — Top-down (independent India EV-battery data)**

Route (a) — IESA/Customized Energy Solutions, "India Electric Vehicle &
Components Market Overview Report" (India Energy Storage Week 2026,
via Autocar Professional / Openthemagazine / Tribune coverage, WebSearch
— WebFetch to primary articles EGRESS_BLOCKED on all three hosts tried):
India EV component market ₹41,000 Cr (2025); battery packs = 52% of
that = **₹21,320 Cr** (2025). Same report's own 2025→2032 endpoints
(₹41,000 Cr → ₹3,02,000 Cr) imply a CAGR of (302,000/41,000)^(1/7)-1 =
7.366^(0.1429)-1 = **33.0%** (computed here directly from the report's
own two stated endpoints; a WebSearch-synthesized summary stated "about
38%", which this report does not use).
Project to 2026: 21,320 × 1.330 = **₹28,356 Cr**.

Route (b) — AR25's own citation (Fortune Business Insights-style),
"Indian EV battery market" USD 2.22bn (2024) → USD 13.89bn (2033).
Implied CAGR: (13.89/2.22)^(1/9)-1 = 6.257^(0.1111)-1 = **22.6%**.
Project to 2026: 2.22 × 1.226^2 = 2.22 × 1.503 = USD 3.336bn × ₹94.4 =
**₹31,492 Cr**.

Routes (a) and (b) are independent (different named source, different
methodology) and converge within ~11% of each other (₹28,356 Cr vs
₹31,492 Cr, midpoint ₹29,924 Cr ≈ **₹29,900 Cr**). This is treated as
the credible size of the FULL India EV battery VALUE CHAIN (cells +
pack assembly + BMS) for 2026 — NOT GEON's addressable slice, because
GEON does not manufacture cells.

Scope-narrowing to GEON's actual addressable layer (pack assembly +
BMS only, excluding cells): BloombergNEF's 2025 Battery Price Survey
and US DOE 2025 modelled-cost data (both via WebSearch) put cell cost
at **78-80% of total pack price**, non-cell components (BMS, housing,
power electronics, wiring) at the remaining 20-22%. Applying 20-22% to
the ₹29,900 Cr full-value-chain figure:
₹29,900 Cr × 0.20 = ₹5,980 Cr; × 0.22 = ₹6,578 Cr.
**Pack-assembly-only top-down estimate ≈ ₹6,280 Cr** (midpoint, 2026).

**Method 2 — Bottom-up (unit × pack size × price)**

Units: AR26 p.35 (FADA-sourced) FY26 India EV retail sales by category.
Pack sizes: WRI India blog and e-vehicleinfo.com / evxpertz.com L5
model spec pages (WebSearch, 2025-2026 vintage). Price: ₹15,000-22,000
per kWh retail-pack level, mid ₹18,000/kWh (pv-magazine-india /
Mercom India, BNEF-sourced, 2026); e-buses at a lower bulk-fleet
₹15,000/kWh. E-bus units from KPMG/newkerala.com coverage (WebSearch).

| Category | FY26 units (AR26 p.35) | Pack size (kWh, sourced range, mid used) | ₹/kWh | Revenue (₹Cr) |
|---|---|---|---|---|
| E-2W | 14,01,818 | 2.5 (range 1.25-4, WRI India) | 18,000 | 630.8 |
| E-3W | 8,30,819 | 5 (range 5-12 for L5 models; blended down for mixed L3/L5 fleet, split NOT FOUND) | 18,000 | 747.7 |
| E-4W | 1,99,923 | 25 (typical Indian compact-to-mid EV, directional) | 18,000 | 899.7 |
| E-CV | 19,454 | 40 (directional, larger LCV packs) | 18,000 | 140.1 |
| E-Bus | 5,412 (KPMG/newkerala, FY25-26) | 250 (typical city-bus pack) | 15,000 | 2,029.5 |
| **Total** | | | | **₹4,447.8 Cr ≈ ₹4,450 Cr** |

This is mobility-only (2W/3W/4W/CV/bus new-vehicle OEM pack demand,
India, 2026). It EXCLUDES the stationary/telecom/inverter/D2C slice
that GEON also serves (~20-30% of GEON's own revenue mix, AR26 p.34) —
no independently sourced TAM figure was found for that narrower
sub-market (grid-scale BESS at USD 2.05bn/₹18,350 Cr in 2026, Mordor/
IESA-sourced, is the WRONG scope — that is utility-scale, a different
customer set GEON shows no evidence of serving). This is a conservative
omission (understates true TAM), left as NOT FOUND rather than
estimated.

**Method divergence, flagged and explained (not averaged silently):**
Bottom-up (₹4,450 Cr) vs cell-cost-adjusted top-down (₹6,280 Cr) diverge
by ~1.4x — reasonably close once the cell/pack scope correction is
applied. Before that correction the divergence was ~6.7x (₹4,450 Cr vs
₹29,900 Cr), which the cell-cost-share filter substantially explains.
Residual uncertainty remains because the IESA/Fortune-Business-Insights
report methodologies could not be independently verified (WebFetch
blocked on all attempted hosts) — it is possible the "EV component
market" figure double-counts exports, includes vehicle-level bill-of-
materials beyond the 5 named components, or uses a different unit-count
base than FADA's retail registrations used here.

**Triangulation — Battery Division TAM**

| Method | Estimate (₹Cr, 2026) | Confidence | Staleness |
|---|---|---|---|
| Top-down, full value chain (IESA + AR25-anchored) | 28,356 – 31,492 (mid 29,900) | M | Current (2026-dated reports) |
| Top-down, cell-cost-adjusted to pack-only | ~6,280 | L-M | Derived, one more inference step |
| Bottom-up, unit×price, mobility only | ~4,450 | M | Current (FY26 units), excludes stationary slice |
| Management claim (AR26, Mordor) | 507.5 | — | Internally inconsistent, rejected as unreliable (Section 1B) |

- **Conservative estimate: ₹4,450 Cr** (bottom-up)
- **Realistic estimate: ₹6,280 Cr** (cell-cost-adjusted top-down)

**mgmt_claim_ratio (formal handoff field):** using the AR26 Mordor claim
(₹507.5 Cr) against the conservative bottom-up estimate (₹4,450 Cr):
507.5 / 4,450 = **0.114x**. Per the standard read (>2x inflated, within
1.5x reasonable, below unusually conservative), 0.114x reads as
"unusually conservative" — but this is NOT genuine management
conservatism. It is the direct arithmetic consequence of the internal
inconsistency flagged in Section 1B (the cited market is smaller than
GEON's own segment revenue). Recorded in the YAML as the closest fit to
the fixed enum, with this caveat carried in flags/analyst_note so stage
11 does not read it as management under-promising.

---

## SECTION 3: SAM & SOM

### 3A — SAM

**Extrusion:** TAM was already scoped to India and to KABRA's product
category (pipe/film/sheet/compounding extrusion, excluding
injection/blow-molding) at the TAM-definition stage. Applying the five
filters finds no further quantifiable subtraction: product fit (already
excluded non-extrusion machinery), geography (already India-only),
channel (direct B2B, matches), customer (organized-sector processors,
matches — KABRA's actual addressable customer count within this is not
separately disclosed), capability (KABRA covers pipe, film, sheet,
compounding — full breadth of the defined category). **SAM = TAM
(conservative) = ₹1,685 Cr.**

**Battery:** Same logic — cells already excluded at the TAM-definition
stage, geography already India-only. One REAL but unquantifiable filter
noted: large 2W/3W OEMs (e.g., market leaders building in-house cell-
to-pack lines) increasingly vertically integrate, shrinking the
OUTSOURCED pool GEON can realistically win. No sourced percentage found
for how much of 2W/3W OEM pack demand is captive vs outsourced — this
is a qualitative SAM-shrinking risk, not a numeric filter (never
estimate a missing number). **SAM = TAM (conservative) = ₹4,450 Cr.**

**Combined SAM = 1,685 + 4,450 = ₹6,135 Cr.**
Expressed against the combined REALISTIC TAM (4,200 + 6,280 = ₹10,480
Cr): SAM/TAM(realistic) = 6,135 / 10,480 = **58.5%**. The gap between
SAM and the realistic TAM is upside not captured in the conservative
case (largely the battery segment's top-down-vs-bottom-up scope
uncertainty), not a filter-driven exclusion.

### 3B — SOM at 3 and 5 years

**Extrusion.** Current segment revenue ₹314.94 Cr. Current SAM share =
314.94 / 1,685 = **18.7%**. Trajectory basis: the FY26 revenue decline
(-13.2% YoY, per injected input) is attributed in the AR itself to
CYCLICAL JJM fund-disbursement timing (AR26 p.36), not to competitive
share loss, and the "~40% share" claim is unverifiable (Section 2). Per
the framework's share-gain rules, with no verified evidence of ongoing
share GAIN, the conservative assumption used is FLAT SHARE — revenue
grows with the market (5.1% CAGR, Method 1):

- 3yr SOM = 314.94 × 1.051^3 = 314.94 × 1.1609 = **₹365.6 Cr**
- 5yr SOM = 314.94 × 1.051^5 = 314.94 × 1.2820 = **₹403.7 Cr**
- Implied revenue CAGR: **5.1%** (3yr and 5yr, by construction — flat
  share)

**Battery.** Current segment revenue ₹136.11 Cr. Current SAM share =
136.11 / 4,450 = **3.06%**. FY26 evidence is mixed-to-negative for
aggressive share gain: segment revenue grew 7.2% but TRAILED the cited
EV industry unit growth of 24.6% (an implied relative share LOSS,
flagged in B04), and the segment loss ratio WIDENED (-20.1% to -31.9%
of segment revenue) even as revenue grew — the opposite of the "moving
toward profitability as volumes scale" narrative in the same MD&A
paragraph. Against this, the market itself is fragmented (many regional
2W/3W pack assemblers), which per the framework can support faster
formalisation-driven share gain. Given the negative execution signals,
this report uses the LOW end of the "normal" 1-2pp/3yr share-gain band
(1pp by yr3, 2pp cumulative by yr5), not the aggressive band, and a
SAM growth rate of 20%/yr (below the cited 24.6% actual unit growth and
well below the cited 33-36.5% pack-market CAGR, reflecting expected
deceleration off a larger base and continuing per-kWh price deflation
as PLI-driven localisation pulls costs toward ₹10,000-12,000/kWh):

- SAM_yr3 = 4,450 × 1.20^3 = 4,450 × 1.728 = ₹7,690 Cr
- SAM_yr5 = 4,450 × 1.20^5 = 4,450 × 2.488 = ₹11,072 Cr
- Share_yr3 = 3.06% + 1.00pp = 4.06% → SOM_yr3 = 7,690 × 0.0406 =
  **₹312.2 Cr**
- Share_yr5 = 3.06% + 2.00pp = 5.06% → SOM_yr5 = 11,072 × 0.0506 =
  **₹560.2 Cr**
- Implied revenue CAGR: yr3 = (312.2/136.11)^(1/3)-1 = 2.293^0.333-1 =
  **31.9%**; yr5 = (560.2/136.11)^(1/5)-1 = 4.116^0.2-1 = **32.7%**

Context only (not the reported figures): running the same share-gain
logic off the REALISTIC SAM basis (₹6,280 Cr, 30%/yr growth) produces
SOM_yr3 ≈ ₹575 Cr and SOM_yr5 ≈ ₹1,322 Cr, implying 57-62% CAGRs. These
are flagged as almost certainly unachievable given the segment's
current execution track record (widening losses, unnamed and
Reg-30-uncorroborated ₹150 Cr FY27 order) and are NOT used as the
primary reported figures.

**Combined (both segments, arithmetic sum):**
- SOM_3yr = 365.6 + 312.2 = **₹677.8 Cr**
- SOM_5yr = 403.7 + 560.2 = **₹963.9 Cr**
- Combined implied CAGR off current total revenue (₹451.05 Cr):
  yr3 = (677.8/451.05)^(1/3)-1 = 1.503^0.333-1 = **14.6%**
  yr5 = (963.9/451.05)^(1/5)-1 = 2.138^0.2-1 = **16.4%**

### 3C — Capacity cross-check

B07's capex-embedded-growth figure (16.6%) is a COMPANY-WIDE blend from
a single, un-split ₹31.77 Cr capital commitment (AR26 Note 41(b)) —
"neither AR splits capex by segment" (injected note). This limits the
cross-check to directional, not segment-precise.

**Battery, physical capacity:** claimed installed capacity ~7 GWh at
Chakan (AR26 p.34/37). At the blended bottom-up ASP used above (₹18,000/
kWh), theoretical maximum revenue at 100% utilisation = 7,000,000 kWh ×
₹18,000 = **₹12,600 Cr**. This is roughly 20x the modelled SOM_5yr of
₹560 Cr and comfortably above even the unused "realistic" context
scenario (₹1,322 Cr). FY26 implied utilisation, working backward from
₹136.11 Cr revenue at the same ₹18,000/kWh: 136.11 Cr ÷ ₹18,000/kWh =
75,617 kWh delivered ≈ **1.1% of nameplate** — a figure highly sensitive
to the unknown true realised ASP (NOT FOUND: GEON's actual per-kWh or
per-pack selling price; at a lower plausible wholesale ASP of ₹8,000-
10,000/kWh, implied utilisation would be ~1.9-2.4%, still low single
digits). Even management's own "at optimal levels, existing facility
can generate INR 1,500+ crore revenue" claim (AR26 p.34/37) implies only
~12% of the ₹12,600 Cr theoretical nameplate ceiling — suggesting the
7 GWh figure is a nameplate/theoretical number rather than a near-term
practical ceiling. **Conclusion: capacity is NOT the binding constraint
on any modelled SOM scenario. The binding constraint is demand
execution** (widening losses, growth trailing the cited market, the
uncorroborated ₹150 Cr FY27 order).

**Extrusion:** a mature, engineer-to-order business; the flat-share,
market-growth-only 5.1% CAGR used above requires no capacity expansion
signal beyond ordinary maintenance capex.

**Combined:** the combined SOM-implied CAGR (14.6% yr3, 16.4% yr5)
sits close to B07's blended capex-embedded ceiling of 16.6% — a
reasonable directional consistency check, though it masks that the
battery segment needs a much larger PERCENTAGE increase in utilisation
(off a ~1-2% base) than the extrusion segment needs in incremental
capacity (which is capacity-adequate already).

**capacity_check: sufficient** — physical capacity is not the
constraint in either segment; the gap, where one exists, is in
execution/demand, named above.

---

## SECTION 4: GROWTH DRIVERS, RISKS & STRUCTURE

### 4A — TAM growth drivers

| Driver | Segment | Impact | Evidence |
|---|---|---|---|
| Regulatory tailwind (JJM 2.0 outlay raised to ₹8.69 lakh Cr, PM E-DRIVE ₹10,900 Cr to Mar-2028, PLI-ACC) | Both | HIGH | AR26 p.34-35 |
| Penetration (EV: govt targets 30% private car / 70% commercial / 40% bus / 80% 2W-3W by 2030 vs FY26 actual far below) | Battery | HIGH if met | AR25 p.36; historical target-vs-actual gap noted below as a risk to this same driver |
| New applications (BESS/telecom/C&I diversification for GEON) | Battery | MEDIUM, unproven at scale | AR26 p.34 (only 20-30% of GEON revenue today) |
| Import substitution (PLI-ACC domestic cell/pack manufacturing) | Battery | MEDIUM, cost-side more than volume-side | AR25/AR26 |
| Formalisation (fragmented small-scale pack assembly consolidating toward certified suppliers post safety-norm tightening) | Battery | MEDIUM, plausible, not freshly sourced in AR26 | Stale deck only (Jan-2024) |
| Geographic expansion (100+ export countries) | Extrusion | LOW-MEDIUM | AR26 p.34; exports only ~13% of consol revenue |

### 4B — TAM risks

| Risk | Segment | Monitoring signal | Evidence |
|---|---|---|---|
| Cyclical downturn (JJM fund-disbursement delays) | Extrusion | Segment revenue vs JJM disbursement pace | AR26 p.36 — REALISED in FY26, not hypothetical |
| Regulatory target slippage (EV adoption has a history of large target misses — deck's own FAME II chart: e.g. e-2W actual 57,354 vs target 10,00,000) | Battery | EV registration data vs stated govt targets | Investor_Presentation_1 p.28 (STALE, Jan-2024, directional only) |
| Disruption (cell-to-pack, 800V architecture, OEM vertical integration) | Battery | GEON's OEM client list / order concentration | AR26 p.35 |
| Customer credit concentration (HEVPL/Hero Electric NCLT insolvency, ₹30.39 Cr receivable) | Battery | Trade receivables ageing, Note 9 | AR26 Note 9 p.87-88 — REALISED |
| Import competition | Extrusion | NOT FOUND — no import-share data in corpus | — |
| Substitution (alternative pipe materials: ductile iron, GI) | Extrusion | NOT FOUND — standard risk noted, no sourced evidence either way | — |

### 4C — Market structure

**Extrusion:** Known organized LISTED players — KABRA, Rajoo Engineers,
Windsor Machines. Known unlisted major — Lohia Corp (revenue NOT
FOUND). Top-3 concentration: NOT FOUND precisely; peer-aggregation data
implies known-listed-players combined (₹1,180 Cr) is 28-70% of the
total market depending which TAM basis is used (wide range, flagged).
Rajoo's own concalls (Nov-2025) describe segment-specific leadership
claims (33% share of India PVC/CPVC pipe-line INSTALLED CAPACITY,
55-60% share of domestic blown-film) that, if taken at face value
alongside KABRA's own "~40%" claim, would sum to over 100% across
overlapping product categories — consistent with these being
self-reported, non-independently-verified figures across the whole
peer set, not just KABRA. Differentiation-based competition (product
breadth/engineering), not pure price, per Rajoo concall commentary.
Import share trend: NOT FOUND.

**Battery:** Fragmented — many regional 2W/3W pack assemblers, a
handful of larger organized third-party players (Exicom, Log9, Lithium
Urban Technologies, Amara Raja/Exide EV arms — not independently sized
in this exercise, revenue NOT FOUND for a clean peer-aggregation
method), and large OEMs increasingly vertically integrating cell-to-
pack in-house (a structural consolidation-away-from-third-party-
assemblers risk). HBL Engineering (screened peer) explicitly avoids
lithium-ion cell manufacturing on margin grounds and is not a clean
GEON comparable (HBL Concall Sep-2025: defence/telecom niche focus,
avoids commodity lithium-ion competition) — informative on industry
economics, not usable for peer-aggregation TAM.

---

## SECTION 5: SUMMARY & RUNWAY

### 5A — Funnel

```
                    EXTRUSION                    BATTERY (GEON)              COMBINED
TAM (conservative)   ₹1,685 Cr                    ₹4,450 Cr                  ₹6,135 Cr
TAM (realistic)      ₹4,200 Cr                    ₹6,280 Cr                  ₹10,480 Cr
SAM                  ₹1,685 Cr                    ₹4,450 Cr                  ₹6,135 Cr
Current revenue      ₹314.94 Cr (18.7% of SAM)    ₹136.11 Cr (3.06% of SAM)  ₹451.05 Cr (7.35% of SAM)
SOM 3yr              ₹365.6 Cr                    ₹312.2 Cr                  ₹677.8 Cr
SOM 5yr              ₹403.7 Cr                    ₹560.2 Cr                  ₹963.9 Cr
Implied CAGR 3yr/5yr  5.1% / 5.1%                  31.9% / 32.7%              14.6% / 16.4%
```

### 5B — Runway assessment

- Revenue headroom = SAM ÷ current revenue = 6,135 / 451.05 = **13.6x**
- TAM growth (weighted by conservative-TAM share: extrusion 27.5% ×
  5.1% + battery 72.5% × 20% used-in-SOM) = **15.9%** blended
- Company CAGR vs TAM: company FY25→FY26 CONSOLIDATED revenue actually
  DECLINED -5.45% (AR26 p.37, ₹477 Cr → ₹451 Cr) while the underlying
  markets grew (extrusion's own decline is attributed to JJM timing,
  cyclical; battery grew 7.2% but trailed its own cited 24.6% market
  unit growth). **The company is currently RIDING NEITHER market well —
  it is losing relative ground in both segments in the most recent
  fiscal year**, even though the combined addressable opportunity is
  large and growing. This is the single most important qualifier on
  the runway numbers below.
- Years to saturate SAM at current growth: not meaningful while
  revenue is declining (division by a negative number); if the flat-
  share extrusion assumption and the modest 1pp/3yr battery share-gain
  assumption both hold, the company reaches ~11% of combined SAM by
  year 5 (963.9/10,480 realistic-TAM basis) — SAM is not remotely at
  risk of saturation within any relevant horizon.

### 5C — Runway classification

**STRONG** — not MASSIVE. Headroom (13.6x) and blended TAM growth
(~16%) alone would support MASSIVE, but that classification is reserved
here for cases where the company is demonstrably capturing the
opportunity. KABRA's most recent actual results (revenue decline,
share loss relative to cited market growth in both segments, widening
battery losses) show the OPPOSITE. STRONG reflects a large, genuinely
growing opportunity that the company has not yet shown it can execute
against — the gap between opportunity and execution is itself the
central finding of this report, to be weighed heavily at Halt 1.

### 5D — SAM expansion levers actually being pursued

- BESS/telecom/C&I/D2C diversification (GEON, AR26 p.34) — currently
  ~20-30% of GEON revenue (₹27-41 Cr). Potential addition: NOT FOUND
  (no sourced TAM for this specific narrow sub-market — see Section
  2.2). Revised headroom: cannot be computed without a sourced figure;
  flagged as a real but unquantified lever.
- Export growth (Extrusion, 100+ countries, ~13% of consol revenue
  today) — potential addition bounded by the much larger GLOBAL plastic
  extrusion machinery market (USD 8.24bn/₹778,000 Cr in 2026, AR26 p.32)
  but KABRA's actual export penetration and growth trajectory within
  that global figure is NOT FOUND (no export-specific growth data
  disclosed). Treated as directional upside only.

### 5E — Final output card

```
TAM (India, combined, conservative / realistic): ₹6,135 Cr / ₹10,480 Cr
SAM: ₹6,135 Cr (58.5% of realistic TAM)
Current revenue: ₹451.05 Cr (7.35% of SAM) — revenue headroom 13.6x
SOM 3yr / 5yr: ₹677.8 Cr / ₹963.9 Cr
SOM-implied revenue CAGR: 14.6% (3yr) / 16.4% (5yr)
Runway class: STRONG (opportunity strong; execution currently lagging it)
```

Valuation implication line: **P/E NOT COMPUTABLE.** FY26 consolidated
and standalone EPS are both negative (PAT ₹(2.44) Cr, EPS ₹(0.70), AR26
p.36; confirmed at B04 as "Trailing P/E not applicable"). The standard
"At __% revenue CAGR... supports/does not support the current
valuation of __x P/E" line cannot be completed on a P/E basis this
cycle. Substituting the available parts: at a 14.6-16.4% SOM-implied
combined revenue CAGR, with margin trajectory NOT FOUND at this stage
(margin modelling is Stage 11's remit, not Stage 9's; current state is
Extrusion segment margin 16.1% of segment revenue, down from 19.3%, and
Battery segment margin -31.9% of segment revenue, WIDENING from -20.1%
— B04), the earnings-growth read cannot yet be stated as a CAGR number.
B04 already names Sum-of-the-Parts as the correct valuation method for
this reason (not P/E, not PEG). Stage 11 should treat the 14.6-16.4%
combined SOM-implied revenue CAGR (and the 31.9-32.7% battery-only,
5.1% extrusion-only components) as its formal cross-check inputs.

---

## SECTION 6: DOWNSTREAM SIGNAL CANDIDATES

| # | Candidate Signal | Entity Type | Why It Drives Demand | Likely Primary Source | Expected Cadence |
|---|---|---|---|---|---|
| 1 | Jal Jeevan Mission 2.0 fund disbursement pace | Macro | JJM funding delays were the AR's own stated cause of FY26 extrusion segment decline; disbursement pace is the leading indicator for pipe-extrusion-line capex orders | JJM dashboard (jaljeevanmission.gov.in) + PIB releases (Ministry of Jal Shakti) + Parliament Q&A (sansad.in) | Monthly |
| 2 | India EV retail registrations by category (E-2W/3W/4W/CV) | Macro | Direct volume driver of GEON's addressable battery-pack demand; already the basis of the bottom-up TAM in this report | Vahan Dashboard (Ministry of Road Transport & Highways) / FADA monthly retail data | Monthly |
| 3 | Union Budget capital-expenditure allocation (infra/JJM AND PLI-ACC/PM E-DRIVE lines) | Macro | SHARED: a single annual event sets policy tailwind levels for BOTH segments simultaneously (JJM outlay for extrusion, PLI-ACC/PM E-DRIVE for battery) — correlated catalyst, count once | Union Budget documents (indiabudget.gov.in) + CGA monthly expenditure execution data | Event-driven (annual) |
| 4 | HEVPL (Hero Electric) NCLT insolvency resolution status | End-customer | GEON already carries a realised ₹30.39 Cr write-off exposure to this counterparty (AR26 Note 9); resolution outcome affects recovery and signals EV-OEM credit quality broadly | NCLT cause list / IBBI corporate insolvency resolution filings; MCA-21 filings | Event-driven |
| 5 | PLI-ACC / PM E-DRIVE scheme disbursement and battery-localisation milestones | Regulatory | Direct cost-curve and demand-incentive driver for GEON's battery segment | PIB releases (Ministry of Heavy Industries) / PLI scheme portal | Quarterly / event-driven |
| 6 | Lithium carbonate / cell price index | Macro | Input-cost driver for GEON's pack economics; falling cell prices (BNEF-tracked) are the main lever behind the ₹15,000-22,000/kWh pack-price range used in this report's bottom-up | Trading Economics / Benchmark Mineral Intelligence spot price; BloombergNEF annual Battery Price Survey | Monthly (spot); Annual (BNEF survey) |

demand_externally_verifiable: true (6 candidates identified, all
independently observable outside company disclosure).

---

```yaml
stage: B09-tam
company: "KABRAEXTRU"
run_date: "2026-09-05"
model: claude-sonnet-5
status: partial               # several WebFetch verification attempts EGRESS_BLOCKED; see searches_skipped
input_gaps: ["results", "rating-detail-beyond-AR-disclosure", "announcements", "shareholding", "research", "prospectus-not-expected", "investor-presentation-stale-2.5yr-Dec2023", "peer-concall-windsor", "peer-concall-mislabel-stale", "screener-csv-defect", "sector_cap_row-flagged-phase3"]
flags:
  - "AR26's own cited 'India EV battery pack market' (Mordor Intelligence, USD 53.76M / Rs 507.5 Cr, 2026) is SMALLER than GEON's own FY26 segment revenue (Rs 136.11 Cr = ~27% implied share) -- internally inconsistent, treated as a scope/citation error, not a usable TAM ceiling"
  - "AR25's '~40% market share in its product category' claim (undefined denominator) back-calculates to an implied machinery sub-market of only Rs 787.5 Cr, 0.19-0.47x this report's independent Extrusion TAM estimates (Rs 1,685-4,200 Cr); claim dropped entirely from AR26"
  - "Battery TAM: bottom-up (mobility-only, Rs 4,450 Cr) vs top-down full-value-chain (Rs 28,356-31,492 Cr) diverge ~6.7x before a cell-cost-share adjustment (cells ~78-80% of pack cost, BloombergNEF/DOE 2025) narrows it to Rs 4,450 Cr vs Rs 6,280 Cr (~1.4x); residual uncertainty remains, primary IESA/Fortune Business Insights report methodology could not be verified (WebFetch egress-blocked)"
  - "OEM vertical integration (large 2W/3W players building cell-to-pack in-house) is a real SAM-narrowing risk for GEON with no disclosed/sourced percentage to quantify; treated qualitatively only, not netted out of SAM"
  - "Segment-level capex split NOT FOUND (AR discloses only a single blended Rs 31.77 Cr capital commitment); the 3C capacity cross-check against B07 is directional, not segment-precise"
  - "Company is currently NOT capturing the sized opportunity: consolidated revenue declined -5.45% FY26 while both segments' cited underlying markets grew; battery segment revenue growth (7.2%) trailed cited EV industry unit growth (24.6%)"
market_definition: "India plastic extrusion machinery (pipe/film/sheet/compounding, excl. injection/blow-molding) plus India li-ion battery pack assembly and BMS for EV mobility and adjacent stationary storage (excl. cell manufacturing and grid-scale BESS), sized and summed as two segments per B04's sum-of-the-parts structure"
tam_cr: {conservative: 6135, realistic: 10480}
sam_cr: 6135
sam_pct_of_tam: 58.5
som_3yr_cr: 677.8
som_5yr_cr: 963.9
som_implied_revenue_cagr: {yr3: 14.6, yr5: 16.4}   # FORMAL handoff to stage 11
current_sam_share_pct: 7.35
revenue_headroom_x: 13.6
tam_growth_pct: 15.9
runway_class: "STRONG"
mgmt_claim_cr: 507.5
mgmt_claim_ratio: 0.114            # claim / conservative estimate (Battery segment, AR26 Mordor citation vs conservative bottom-up)
mgmt_claim_read: "conservative"    # literal ratio reading; SEE FLAGS -- this is an internal-inconsistency artefact, not genuine conservatism
capacity_check: "sufficient"       # 7GWh nameplate vastly exceeds modelled SOM in both segments; binding constraint is demand execution, not capacity
methods_used: ["top-down (India/global industry aggregator reports)", "bottom-up (unit x pack-size x price)", "peer revenue aggregation (Extrusion: KABRA+Rajoo+Windsor+unorganised estimate)", "cell-cost-share scope adjustment (Battery: full value chain to pack-assembly-only)", "management-claim back-calculation (Extrusion 40%-share implied TAM)"]
stale_data_flags:
  - {datapoint: "Investor Presentation 18% li-ion segment share and 40% extrusion market share claims", source: "Investor_Presentation_1.txt (Q3 FY24 deck)", year: "2024-01"}
  - {datapoint: "India Plastic/Extrusion Machinery Market base-year figures (USD 519.8M/571.2M-equivalent base)", source: "WebSearch snippet, Grand View Research / 6Wresearch-style India Extrusion Machinery Market reports", year: "2023"}
  - {datapoint: "AR25 'Indian EV battery market' USD 2.22bn (2024) to USD 13.89bn (2033) citation", source: "Annual_Report_2025.txt p.4-5/173", year: "2024"}
searches_performed:
  - "India plastic extrusion machinery market size 2025 crore CRISIL Plastindia"
  - "India EV battery pack market size 2026 crore IESA"
  - "India lithium ion battery pack cost per kWh 2025 2026 average price"
  - "average battery pack size kWh electric two wheeler three wheeler India"
  - "IESA India EV component market Rs 41000 crore 2025 battery pack 52% IESW 2026"
  - "average battery pack capacity kWh electric three wheeler India e-rickshaw L5"
  - "India battery energy storage system BESS market size 2026 GWh crore IESA"
  - "Kabra Extrusiontechnik market share plastic extrusion machinery India"
  - "India plastics processing machinery industry turnover crore Plastindia Foundation PMMAI"
  - "India pipe extrusion machinery market size crore 2025 report"
  - "EV battery pack cost breakdown cell cost percentage of total pack cost BMS 2025"
  - "India electric bus sales 2026 units FAME PM-eBus"
  - "USD INR exchange rate September 2026"
searches_skipped:
  - "WebFetch grandviewresearch.com/horizon/outlook/plastic-extrusion-machinery-market/india -- EGRESS_BLOCKED"
  - "WebFetch 6wresearch.com/industry-report/india-plastic-extrusion-machine-market -- EGRESS_BLOCKED"
  - "WebFetch autocarpro.in (IESA EV component market article) -- EGRESS_BLOCKED"
  - "WebFetch mordorintelligence.com/industry-reports/india-ev-battery-pack-market (scope verification) -- EGRESS_BLOCKED"
  - "WebFetch dailypioneer.com (IESA EV component market article) -- EGRESS_BLOCKED"
  - "WebFetch evinfrastructurenews.com (IESA FY25-26 EV sales article) -- EGRESS_BLOCKED"
downstream_candidates:
  - signal: "Jal Jeevan Mission 2.0 fund disbursement pace"
    entity_type: "macro"
    demand_link: "JJM funding delays cited by AR26 as the cause of FY26 extrusion segment decline"
    likely_source: "JJM dashboard (jaljeevanmission.gov.in) + PIB (Ministry of Jal Shakti) + sansad.in Q&A"
    cadence: "monthly"
    shared: false
  - signal: "India EV retail registrations by category (E-2W/3W/4W/CV)"
    entity_type: "macro"
    demand_link: "Direct unit-volume driver of GEON's addressable battery-pack demand"
    likely_source: "Vahan Dashboard (MoRTH) / FADA monthly retail data"
    cadence: "monthly"
    shared: false
  - signal: "Union Budget capex allocation (JJM AND PLI-ACC/PM E-DRIVE lines)"
    entity_type: "macro"
    demand_link: "One annual event sets policy tailwind for both segments at once"
    likely_source: "Union Budget documents (indiabudget.gov.in) + CGA monthly expenditure data"
    cadence: "event-driven"
    shared: true
  - signal: "HEVPL (Hero Electric) NCLT insolvency resolution status"
    entity_type: "end-customer"
    demand_link: "GEON carries a realised Rs 30.39 Cr write-off exposure to this counterparty"
    likely_source: "NCLT cause list / IBBI CIRP filings; MCA-21 filings"
    cadence: "event-driven"
    shared: false
  - signal: "PLI-ACC / PM E-DRIVE scheme disbursement and localisation milestones"
    entity_type: "regulatory"
    demand_link: "Direct cost-curve and demand-incentive driver for the Battery segment"
    likely_source: "PIB releases (Ministry of Heavy Industries) / PLI scheme portal"
    cadence: "quarterly"
    shared: false
  - signal: "Lithium carbonate / EV cell price index"
    entity_type: "macro"
    demand_link: "Input-cost driver behind the pack-price assumption used in the bottom-up TAM"
    likely_source: "Trading Economics / Benchmark Mineral Intelligence spot price; BloombergNEF annual Battery Price Survey"
    cadence: "monthly"
    shared: false
demand_externally_verifiable: true
analyst_note: "Two management TAM claims were tested, not one, because company memory flagged both. The Extrusion '40% share' claim back-calculates to an implied Rs 787.5 Cr market, below this report's independent estimates -- consistent with an undefined, possibly narrow denominator, and the claim vanished from AR26. The Battery AR26 Mordor citation (Rs 507.5 Cr) is smaller than GEON's own segment revenue -- an internal-consistency failure, not a genuine market read; mgmt_claim_cr/ratio in this YAML uses that figure only because it is the one explicit numeric 'market size' claim in the current-year AR, per the schema's single-field design. Battery TAM/SAM/SOM rest on a cell-cost-share bridge (cells ~78-80% of pack cost) between a well-converged top-down full-value-chain estimate and an independently-built bottom-up estimate; this bridge is the load-bearing, unverified assumption in the whole battery analysis and should be re-tested with primary IESA/Mordor source access at Halt 1 or in claude.ai verification."
```
