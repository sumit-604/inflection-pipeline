# Stage 9 — TAM / SAM / SOM Market Sizing
**Company:** Rappid Valves (India) Ltd (RAPPID) | **Run date:** 2026-09-19 | **Model:** claude-sonnet-5

Input gaps carried into this stage: rating/ folder empty (no credit rating exists); research/
folder empty; one earnings call only (NO-CONCALL MODE, 01-Jun-2026); peer transcripts 8 of
12; SME half-yearly filer (no quarterly-granularity disclosure). All figures ₹ Crore unless
marked USD. FX conversions in this report use ₹96/USD, the 18-Sep-2026 spot rate
(Trading Economics, WebSearch 2026-09-19) since no FX rate is specified anywhere in the
corpus — this is an ANALYST ASSUMPTION, flagged, and applied uniformly so relative
comparisons hold even if the absolute level moves with the rupee.

---

## SECTION 1: MARKET DEFINITION

### 1A. Precise boundaries

- **Product scope:** ball, gate, globe, butterfly, check, double-block and strainer valves,
  15mm-600mm, ferrous and non-ferrous metallurgy including nickel-aluminium bronze (NAB);
  integrated actuated-valve assemblies (Rappid integrates third-party electrical/hydraulic/
  electro-hydraulic actuators onto its own valve bodies, it does not manufacture actuators
  itself — Jun-2026 concall p.7-8, Gaurav Dalal). Excludes: plastic/PVC and residential
  plumbing valves, instrumentation-grade smart/control valves, safety/relief valves, and
  cryogenic/subsea ultra-high-pressure valve lines (none evidenced in the product range).
- **Geographic scope:** India domestic (>90% of revenue; the balance is opportunistic export
  to Dubai since 2012, with US/Japan certifications obtained but revenue not yet
  contributing — Jun-2026 concall p.6-7). SAM in Section 3 is built on the India-only TAM;
  export markets sit outside this SAM as pure optionality (B07-emoat.yaml optionality
  register: US data-centre customer, 16+ months at NDA/lab-test stage).
- **Customer scope:** PSU and private oil & gas, chemicals, ethanol/breweries, water/
  wastewater treatment, power, EPC/OEM, and marine/naval shipyards (Mazagon Dock
  Shipbuilders, Garden Reach Shipbuilders & Engineers, Cochin Shipyard, L&T Shipbuilding —
  Annual_Report_2026.txt p.23). FY26 actual revenue mix by named vertical (Annual_Report_
  2026.txt p.24): Ethanol/Breweries/Industrial Wastewater Treatment 30.81%, Shipbuilding &
  Repair 24.51%, Chemicals 15.43%, EPC & OEM 14.89%, Marine 8.34%, Steel 2.81%, Fire
  Safety 0.39%, Others 2.82%. Marine + Shipbuilding & Repair combine to 32.85%, matching
  B04-bizmodel.yaml's ~33% marine/naval stream.
- **Channel scope:** GeM-portal PSU tenders (MSME-status advantage), direct private-sector
  sales, EPC/OEM referral, and direct export. No material channel exclusion identified.
- **Price segment:** mid-value certified/engineered valves; not commodity low-end
  (unbranded/uncertified) nor the ultra-high-pressure nuclear/subsea niche.
- **Explicit exclusions:** valve MRO/aftermarket services (not evidenced as a revenue line),
  non-metallic valves, and any non-Indian manufacturing base.

### 1B. Management's own TAM claim

Annual_Report_2026.txt p.22-23 ("Industry Growth Indicators", source cited as "IMARC and
industry sources") and Investor_Presentation_1.txt p.25 (same figures, both dated with the
FY26 results cycle, presentation dated 01-Jun-2026) state:

| Market | Base year | Forecast year | CAGR |
|---|---|---|---|
| Global Valves Market | USD 82.9 Bn (2025) | USD 136.0 Bn (2034) | 5.70% |
| Indian Industrial Valves Market | USD 3.4 Bn (2025) | USD 6.3 Bn (2034) | 6.64% |

Date: filed with FY26 results (Jun-2026), base year 2025 — within the 2-year staleness
window, not flagged stale. **Credibility read: BROAD.** This is the entire India industrial
valves category (all valve types, all end-use verticals including oil & gas and power, which
Rappid barely serves — see Section 3A Filter 4), not a Rappid-specific addressable figure.
Management does not offer a narrower, product-or-vertical-specific TAM anywhere in the
corpus. A second management claim, on the import-substitution angle (Investor_Presentation_
1.txt p.25, source IMARC): "In 2024, India exported $2.66B of Valves (9th largest)... imported
$2.15B of Valves (15th largest). Thus there is huge opportunity of Import substitution." This
claim is internally weak: exports ($2.66Bn) exceed imports ($2.15Bn), meaning India is a **net
exporter** of valves at the aggregate category level — the "huge opportunity" framing does not
follow from the two numbers management itself cites. Flagged (FLAG-MGMT-CLAIM-
INCONSISTENCY below).

---

## SECTION 2: TAM ESTIMATION, MULTIPLE METHODS

### Method 1 — Top-down (India industrial valves market, multi-source triangulation)

Three research-house estimates were found, and they diverge sharply on *level* while
clustering tightly on *growth rate*:

| Source | Base year value | Forecast year value | CAGR | Evidence tier |
|---|---|---|---|---|
| Mordor Intelligence (current, WebFetch 2026-09-19) | USD 1.56 Bn (2025) | USD 2.34 Bn (2031) | 6.96% (2026-31) | Tier 2, live web, current |
| IMARC (= management's own cited figure) | USD 3.4 Bn (2025) | USD 6.3 Bn (2034) | 6.64% | Tier 1, filed in AR/IP |
| Verified Market Research (WebSearch 2026-09-19) | USD 3.73 Bn (2024) | USD 6.1 Bn (2032) | 7.74% | Tier 2, live web |
| Mordor Intelligence (as cited in RHP, Sep-2024) | USD 2.41 Bn (2024) | USD 3.38 Bn (2029) | >7% | Tier 1 filed, but STALE (Mordor has since revised its own number down to $1.56Bn/2025 — see flag) |

Converting at ₹96/USD:
- **Conservative (Mordor, current):** USD 1.56 Bn × 96 = **₹14,976 Cr** (2025)
- **Realistic (IMARC, = management's figure):** USD 3.4 Bn × 96 = **₹32,640 Cr** (2025)

Per CONSERVATIVE BIAS, the ₹14,976 Cr Mordor figure is carried as the TAM floor for all
downstream SAM/SOM math; the ₹32,640 Cr IMARC figure is carried as the realistic case.
**The growth-rate estimates (6.64%-7.74%) agree far better than the level estimates
(a >2x spread) — the trajectory is more reliable than the size.** Flagged
(FLAG-TAM-SOURCE-DIVERGENCE).

### Method 2 — Bottom-up: NOT COMPUTABLE

A bottom-up build requires an addressable-unit definition, total units, and revenue per unit.
B04-bizmodel.yaml already names this gap explicitly: "no average-selling-price or per-valve
cost disclosure; only company-wide % figures available" and "revenue_per_unit: NOT FOUND."
No peer transcript, the RHP, the AR, nor any web search surfaced a per-valve or per-vessel
rupee anchor. Rather than invent a valve-count or a valve-content-% of end-market capex
(neither of which is sourced anywhere in this run), Method 2 is marked **NOT COMPUTABLE**
and skipped. This is itself informative: it is the same evidentiary gap B06 flagged for the
naval pocket specifically (see the marine sub-section below).

### Method 3 — Peer revenue aggregation

Known listed/disclosed valve makers and their most recent disclosed revenue:

| Peer | Revenue | Period | Source |
|---|---|---|---|
| Rappid Valves | ₹53.23 Cr | FY26 | runs/rappid-2026-09-19/inputs/results (task anchor) |
| KSB Ltd — **valves segment only** | ₹125.2 Cr (+31.65% YoY) | FY25 | WebSearch 2026-09-19 (FY26 segment split not found) |
| Quest Flow Controls (Meson Valves India Ltd) | ₹62.36 Cr (down 7.21% YoY) | FY26 | WebSearch 2026-09-19 |
| Atam Valves Ltd | ₹47.30 Cr **or** ₹347.29 Cr (sources conflict) | FY26 | WebSearch 2026-09-19 — UNRESOLVED, carried as a data-quality flag, not averaged |
| L&T Valves (private, part of Larsen & Toubro) | ~USD 300 Mn ≈ **₹2,490 Cr** (at then-prevailing FX) | 2022 (latest found) | WebSearch 2026-09-19, no FY26 figure available |
| Kirloskar Brothers — valve segment | NOT FOUND (segment revenue not separately disclosed) | — | WebSearch 2026-09-19 |

Even taking the higher Atam Valves figure, the four SME/mid-cap listed pure-plays sum to
roughly ₹288-588 Cr — under 4% of the conservative ₹14,976 Cr TAM. L&T Valves alone, a
single private conglomerate subsidiary, is estimated at roughly ₹2,490 Cr (2022), i.e.
~15-17% of the conservative TAM on its own. Mordor Intelligence separately describes the
India industrial valves market as "highly fragmented, with around 600 companies" (WebSearch
2026-09-19). **Read: this is not a classic 30-60% "unorganised sector" market in the plumbing-
and-pipes sense; it is a market where the bulk of value sits with large private/conglomerate
players (L&T Valves, Kirloskar Brothers, MNC subsidiaries of Flowserve/Emerson) that do not
separately disclose valve-segment revenue, sitting above a long tail of ~600 small/SME makers
of which Rappid is one.** This corroborates, rather than resolves, the level uncertainty in
Method 1.

### Method 4 — Import substitution

India imported USD 2.15 Bn of valves in 2024 (15th largest importer globally — Investor_
Presentation_1.txt p.25, source IMARC). At ₹96/USD this is a theoretical **₹20,640 Cr**
import-substitution slice if 100% displaced by domestic manufacture. However, as noted in
Section 1B, India also exported USD 2.66 Bn of valves the same year (9th largest exporter) —
a net trade surplus at the category level. The import-substitution TAM slice is real at the
product-category level (China dumping in specific certified/high-spec segments is plausible and
is separately corroborated by the CMD's own comment that Indian exporters are "directly
challenged with China" — Jun-2026 concall p.7) but management's blanket "huge opportunity"
framing overstates what its own two cited numbers show. Confidence: L, direction only.

### Method 5 — Global benchmark (India vs China)

India's industrial valve market (IMARC, $3.4 Bn 2025) is 4.1% of the global valve market
(IMARC, $82.9 Bn 2025, both AR-cited). China's narrowly-scoped industrial valves market is
estimated at USD 4.1 Bn for 2025 (WebSearch 2026-09-19, mobilityforesights.com) — roughly
2.6x India's Mordor-conservative figure ($1.56 Bn) despite China's economy being ~4-5x
India's nominal GDP. This points toward mild India under-penetration relative to China on a
GDP-scaled basis, a modest tailwind, but the China figure itself ranges from $4.1 Bn to
$17.1 Bn across sources depending on scope (WebSearch 2026-09-19) — the same
methodology-divergence problem as Method 1. Confidence: L, directional only.

### Triangulation table

| Method | Estimate (₹ Cr, India, current) | Confidence | Staleness |
|---|---|---|---|
| 1 — Top-down (Mordor, conservative) | 14,976 | M | current (2025 base) |
| 1 — Top-down (IMARC, realistic = mgmt claim) | 32,640 | M | current (2025 base) |
| 2 — Bottom-up | NOT COMPUTABLE | — | — |
| 3 — Peer aggregation | Directional only (confirms fragmentation, not a TAM number) | L | current |
| 4 — Import substitution | 20,640 (theoretical, net-exporter caveat) | L | current (2024 base) |
| 5 — Global benchmark | Directional only (mild under-penetration vs China) | L | current |

**Conservative estimate: ₹14,976 Cr. Realistic estimate: ₹32,640 Cr.**
**Management's claim vs conservative estimate: 32,640 ÷ 14,976 = 2.18x → by the standard
read (>2x likely inflated), this sits right at the inflation threshold** — though as Method 1
shows, this reflects genuine divergence between two named research houses (Mordor vs
IMARC) more than a company-specific inflation of its own market. Management is simply citing
the higher of two third-party numbers; it did not construct a proprietary claim.

### The marine/naval pocket — sized separately, evidence tier stated

No document in this run's corpus, and no web search performed for this stage, produces a
rupee- or dollar-denominated size for the **Indian** naval/marine valve market specifically.
This echoes 06-peers.md's finding verbatim: "No peer gives a marine/naval-valve-specific TAM
or a per-vessel valve cost percentage... this silence is itself informative... the naval/marine
valve TAM appears to be a genuinely unquantified pocket across the whole listed peer set."
**Evidence tier for every marine TAM number below: Tier 2 (global, third-party, NOT
India-specific) or qualitative context only. No Tier 1 (filed, India-specific, rupee-denominated)
figure exists.**

- Global Marine Actuators & Valves market, as cited in this run's own corpus
  (Rappid_Valves_RHP_Sep2024.txt p.140-141, Investor_Presentation_1.txt p.26): USD 2.8 Bn
  (2022) → USD 3.6 Bn (2027), CAGR 4.5-5.3% depending on source. **STALE** (2022 base year,
  4 years old from run date; informs direction only, per the staleness rule).
- Cross-checked live (WebSearch 2026-09-19): current estimates cluster around USD 3.49-3.94
  Bn (2025) growing at 4.6-6.27% CAGR to roughly USD 5.34 Bn by 2032 (narrow scope,
  methodologically closest to the corpus figures); a broader-scope estimate puts the 2025
  base at USD 7.6-8.5 Bn. This is a **global**, not an India, figure.
- India-specific context that exists but is not a $-denominated TAM: Maritime India Vision
  targets ~₹697 Bn (₹69,700 Cr) of shipbuilding and maritime development package spend by
  2047 and top-5 global shipbuilding-nation status (Investor_Presentation_1.txt p.27, sourced
  "Tribune Dec'25"); the naval modernisation pipeline is described as exceeding ₹2.3 trillion
  (₹230,000 Cr), with over 60 naval vessels under construction and 70-80 more planned, and
  75% of defence procurement reserved for domestic suppliers (same source). Defence
  production reached ₹1.78 lakh Cr in FY2025-26 (+15.6% YoY), against a government target of
  ₹3 lakh Cr by 2029 (Annual_Report_2026.txt p.23, source Ministry of Defence).
- A bottom-up build from these pipeline figures would require a valve-content-% of total
  vessel/programme value. This search (queried explicitly this stage) returned no anchor
  ("valves percentage of shipbuilding cost" — no specific industry percentage surfaced,
  WebSearch 2026-09-19). **No such percentage is asserted here.** The marine SAM/SOM in
  Section 3 is therefore built off Rappid's own served-revenue and order-book trajectory, not
  off a derived marine TAM — this is a deliberate, evidence-driven choice, not an oversight.

---

## SECTION 3: SAM & SOM

### 3A. SAM — five filters applied to the conservative and realistic TAM

| Filter | Reasoning | Retained % | Conservative (₹Cr) | Realistic (₹Cr) |
|---|---|---|---|---|
| Start (TAM) | Method 1 triangulation | 100% | 14,976 | 32,640 |
| 1. Product fit | Rappid's range (ball/gate/globe/butterfly/check/double-block/strainer) covers the dominant mechanical valve-type categories (Mordor: ball valves alone 25.17% share in 2025) but excludes instrumentation/control valves, safety/relief valves, and cryogenic/subsea specialty lines. ANALYST JUDGMENT applied: 75% retained. | 75% | 11,232 | 24,480 |
| 2. Geography | Already India-only at the TAM stage; no further cut. Export markets (Dubai, pursued US/Japan) sit entirely outside this SAM as upside, not counted here. | 100% | 11,232 | 24,480 |
| 3. Channel | GeM/PSU, private direct, EPC/OEM, and export channels are all accessible to Rappid; no material channel exclusion identified. | 100% | 11,232 | 24,480 |
| 4. Customer / vertical fit | Rappid's FY26 revenue table shows 0% disclosed exposure to Oil & Gas (Mordor's single largest India segment at 35.20% share, 2025 — though one search snippet instead names water/wastewater as leading at ~29%, a source conflict noted and treated with low confidence) and no separately itemised Power vertical. ANALYST JUDGMENT: retain ~50% of the post-Filter-1 base, removing O&G's ~35% share plus a conservative ~15% allowance for Power. | 50% | 5,616 | 12,240 |
| 5. Capability | Rappid already holds the certifications (ClassNK, DNV/API607, IBR, UL) needed for every vertical it currently serves; no further vertical is being added that requires new capability, so no cut here. Physical *capacity* is a real constraint but binds SOM, not SAM (Section 3C). | 100% | 5,616 | 12,240 |
| **SAM** | | | **₹5,616 Cr** | **₹12,240 Cr** |

**SAM as % of TAM: 37.5%** (consistent on both the conservative and realistic basis, since the
same filter cascade was applied to each). Per CONSERVATIVE BIAS, **₹5,616 Cr** is carried
forward as the single SAM figure for the SOM math and the YAML handoff.

### 3B. SOM at 3 and 5 years

Current SAM share: FY26 revenue ₹53.23 Cr ÷ SAM ₹5,616 Cr = **0.95%**.

Share-gain rules (per stage instructions): 1-2pp in 3 years is "normal"; 3-5pp is "aggressive"
and requires capacity + execution evidence. B07-emoat.yaml's own execution-record flag
(FLAG-EMOAT-EXECUTION-RECORD) states the promise-delivery record is "1 delivered, 1
partial, 3 missed; credibility grade C" — this is evidence *against* assuming the aggressive
case. The base case below therefore uses the **low end of the normal range**; a 2pp upside
case is shown to make the capacity constraint (3C) visible.

| Scenario | SAM-share gain | Implied SAM share | Revenue (₹Cr) | Implied CAGR from FY26 base |
|---|---|---|---|---|
| **3yr base case** | +1.0pp | 1.95% | 5,616 × 1.95% = **₹110 Cr** | (110/53.23)^(1/3)-1 = **27.4%** |
| 3yr upside case | +2.0pp | 2.95% | 5,616 × 2.95% = ₹166 Cr | (166/53.23)^(1/3)-1 = 46.1% |
| **5yr base case** | +2.0pp | 2.95% | 5,616 × 2.95% = **₹166 Cr** | (166/53.23)^(1/5)-1 = **25.5%** |
| 5yr upside case | +3.5pp | 4.45% | 5,616 × 4.45% = ₹250 Cr | (250/53.23)^(1/5)-1 = 36.0% |

**SOM_3yr = ₹110 Cr, implied CAGR 27.4%. SOM_5yr = ₹166 Cr, implied CAGR 25.5%.**
These are the FORMAL handoff figures to Stage 11.

### 3C. Capacity cross-check

Management states, on the Jun-2026 concall (p.5-6, Gaurav Dalal): "we are well equipped up to
120 crores, so I don't see that we need to further expand our capacity, except for the fact
that we are continuously investing in expanding our automated machinery." A separate,
possibly inconsistent, statement in the same call describes "85% utilization" — but the CMD
clarifies this 85% figure refers to the *old* factory footprint before the recent 45,000+ sq ft
expansion (concall p.8, exchange with Chintan Parikh: "Absolutely, sir, with the existing [old
factory]... today we operate from 45,000 plus square feet"). The two statements are not
cleanly reconciled in the transcript; **₹120 Cr is used here as the best available, most specific,
revenue-denominated capacity ceiling.**

B07-emoat.yaml's capex_embedded_growth_pct is **12%** — read as the incremental capacity
uplift available from continuing automation investment alone, absent a new plant.
Effective ceiling with this uplift: ₹120 Cr × 1.12 ≈ **₹134 Cr**.

| Check | Result |
|---|---|
| SOM_3yr (₹110 Cr) vs ceiling (₹120 Cr) | **Sufficient.** Base case fits within disclosed capacity. |
| SOM_3yr upside (₹166 Cr) vs ceiling (₹120 Cr) | **Gap of ₹46 Cr.** The 2pp/3yr scenario cannot be physically produced without new capex. |
| SOM_5yr (₹166 Cr) vs automation-uplifted ceiling (₹134 Cr) | **Gap of ₹32 Cr.** Even the 5yr *base* case exceeds the disclosed capacity plan. |

**Which side is optimistic:** the capacity/capex plan is the more conservative, limiting side —
not the SOM. The SAM-derived demand opportunity can support faster growth than
management's disclosed capex plan currently allows for. If FY27 growth tracks management's
own guidance ("closing to 50% or more" — see 3B/5B below), two consecutive years of 50%
growth would take revenue from ₹53.23 Cr to ₹53.23 × 1.5 × 1.5 ≈ **₹119.8 Cr — within a
rounding error of the disclosed ₹120 Cr ceiling, in just two years, not three.** No new plant or
capacity announcement beyond continued automation investment exists anywhere in this
run's corpus. Flagged (FLAG-CAPACITY-CONSTRAINT).

### FY27 guidance cross-check (task-specified, against "closing to 50% or more")

Management's growth guidance for FY27 (Jun-2026 concall p.10, Gaurav Dalal, in response to
an order-book question: "we should at least have a minimum growth with the order book and
everything, closing to 50% or more") implies FY27 revenue of ₹53.23 × 1.50 = **₹79.85 Cr**.

Compared against the SOM_3yr-implied CAGR of 27.4% (a rolling 3-year average, not a
single-year figure): **50% ÷ 27.4% = 1.83x.** By the standard read (>2x inflated, within 1.5x
reasonable), 1.83x sits above the "reasonable" band but short of "inflated" — it is elevated,
which is structurally expected (a single strong guidance year will normally run hotter than a
smoothed 3-year average), but it is also the same management team B07 flags for a weak
promise-delivery record (1 delivered, 1 partial, 3 missed, credibility grade C). **Read: plausible
for FY27 alone given the disclosed order book (~80% of expected FY27 orders already booked
at ₹42 Cr per the Jun-2026 concall), but not free of the execution-credibility discount B07
already applies.** This guidance-vs-SOM ratio (1.83x) is the figure carried into the
`mgmt_claim_ratio` YAML field for this run, per the task's explicit instruction to compute it
against the FY27 guidance rather than the generic TAM claim (the TAM-claim ratio, 2.18x, is
reported separately in Section 2).

---

## SECTION 4: GROWTH DRIVERS, RISKS & STRUCTURE

### 4A. TAM growth drivers

| Driver | Impact | Evidence |
|---|---|---|
| Regulatory/defence tailwind | HIGH | Naval modernisation pipeline ₹2.3 trillion, 75% domestic-reserved, 60 vessels under construction + 70-80 planned (IP p.27); defence production ₹1.78 lakh Cr FY25-26 (+15.6% YoY), target ₹3 lakh Cr by 2029 (AR p.23, Ministry of Defence) — DOCUMENTED, and corroborated at the company level by four dated FSS shipset work orders (BHEL, Shree, Muller-BBM, L&T — B07-emoat.yaml catalysts_12m). |
| China+1 / import substitution | MODERATE | $2.15Bn import value theoretically substitutable (Method 4), though management's own framing is internally weak (net exporter). B07's E2 category scores this Moderate, 12-24m to materialise. |
| Ethanol/bioenergy blending target | MODERATE | Government's 20% ethanol-blending target (AR p.23) — directly matches Rappid's single largest FY26 vertical (Ethanol/Breweries/Wastewater, 30.81%). DOCUMENTED. |
| Natural gas infrastructure build-out | MODERATE | Gas pipeline network expanded to 16,800 km + 14,700 km under construction (AR p.23, Ministry of Petroleum) — relevant to City Gas Distribution, a vertical Rappid does not yet show material exposure to. |
| Export expansion / technology enablement | LOW-MODERATE | India engineering exports at a record US$122.43 Bn in FY25-26 (+4.86% YoY — AR p.23); Rappid holds UL and ClassNK export-relevant certifications, but the flagship US data-centre contract is 16+ months delayed and unconverted (B07 optionality register). |
| Industrial automation / actuated-valve adoption | LOW-MODERATE | India's industrial automation market cited at USD 19.3 Bn "by 2025" (RHP/IP) — this forecast horizon has now lapsed as of the run date; Rappid integrates but does not manufacture actuators. |
| Jal Jeevan Mission (piped water) | LOW (for Rappid specifically) | ₹8.69 lakh Cr programme target (IP p.6) is a large sector tailwind, but no order or revenue line in this corpus ties Rappid to JJM-specific work; more directly relevant to larger players (L&T Valves, Kirloskar Brothers). |

### 4B. TAM risks

| Risk | Monitoring signal |
|---|---|
| Import competition (China) | CMD's own words: "you are directly challenged with China... especially when China comes into play" (concall p.7) — monitor China-sourced valve import share trend (not disclosed anywhere in this corpus; NOT FOUND). |
| Regulatory/certification dependency | AR itself names this explicitly (p.24): "changes in applicable requirements or delays in certification renewals could affect its ability to serve certain markets." Monitor certification renewal dates (not itemised in this run). |
| Competitive intensity | AR names this explicitly (p.24): "pricing, certifications and technical capabilities influencing order wins." Monitor GeM/PSU tender win-rate and realised pricing. |
| Sector concentration | AR names this explicitly (p.24): "Marine and shipbuilding account for a significant share of the Company's revenue. A slowdown... could adversely affect overall business performance." Monitor Marine + Shipbuilding & Repair % of revenue (must-track metric, B04). |
| Cyclical / lumpy order timing | FY26 H1 +46.9% vs H2 -24.9% on a deliberate order-holding decision amid NAB/copper price escalation (B04-bizmodel.yaml) — monitor quarterly order-book-to-revenue conversion, not headline YoY growth. |
| Input-cost / margin (not TAM) | NAB price rose from ~₹1,250/kg to ~₹1,650/kg (concall p.8) — a margin risk that can defer TAM capture (₹10-12 Cr of orders held back in FY26) even where demand is present. |
| Substitution | LOW — no functional substitute for mechanical flow-control valves identified anywhere in the corpus. |

### 4C. Market structure

- **Global:** moderately competitive, dominated by Emerson Electric, Schlumberger, Alfa
  Laval, Flowserve, Crane Co. (Rappid_Valves_RHP_Sep2024.txt p.139, Mordor-sourced) — these
  players do not compete directly with Rappid's India-domestic SME niche.
- **India:** described by Mordor Intelligence as "highly fragmented, with around 600
  companies" (WebSearch 2026-09-19). Known listed pure-plays (Rappid ₹53.23 Cr, KSB valves
  segment ₹125.2 Cr FY25, Quest Flow Controls ₹62.36 Cr FY26, Atam Valves ₹47-347 Cr
  conflicting) sum to a small fraction of the TAM; large private/conglomerate players (L&T
  Valves ~₹2,490 Cr in 2022, Kirloskar Brothers segment revenue NOT FOUND) and MNC
  subsidiaries (Flowserve India, Emerson India, revenue NOT FOUND at valve-segment level in
  this corpus) hold the bulk of organised-sector share not visible in Rappid's peer set.
- **Marine/naval sub-segment:** structurally narrower. AR states explicitly (p.22): "Entry
  barriers are considerably higher than those for conventional industrial valve applications,
  requiring sustained engineering capabilities, manufacturing expertise and long-standing
  customer approvals." Rappid holds ClassNK, DNV/API607, IBR and UL certifications; peer
  evidence (06-peers.md) shows Quest Flow Controls is the only other named peer with
  defence/marine/offshore exposure, at materially higher margins (23-25% EBITDA vs Rappid's
  ~12% margin point management itself flags — 06-peers.md Claim 2).
- **Price vs differentiation:** PSU tenders run on L1 (lowest-price) reverse-auction logic for
  most peers (Atam Valves is the named exception, "No PSUs, no L1 bidding" — 06-peers.md);
  qualification/certification lock-in (B07 category B2) provides a partial differentiation moat
  once type-approved into a vessel programme, but does not eliminate price competition at the
  bid stage.
- **Consolidation/fragmentation trend:** NOT FOUND for the Indian domestic tier specifically;
  global players are described as pursuing "strategic collaborations" (RHP p.139), not
  acquisitions of Indian SME valve makers.
- **Import share trend (direction):** NOT FOUND. Only the single 2024 snapshot (imports
  $2.15Bn vs exports $2.66Bn) exists in this corpus; no time series.

---

## SECTION 5: SUMMARY & RUNWAY

### 5A. Funnel

```
TAM (India industrial valves, conservative)........... ₹14,976 Cr  (Mordor, 2025)
TAM (India industrial valves, realistic/mgmt-cited).... ₹32,640 Cr  (IMARC, 2025)
  -> Filter: product fit (75%)
  -> Filter: geography (100%, already India-only)
  -> Filter: channel (100%)
  -> Filter: customer/vertical fit (50%, ex-O&G/Power)
  -> Filter: capability (100%, certifications already held)
SAM (conservative basis carried forward)............... ₹5,616 Cr   (37.5% of TAM)
  Current revenue (FY26)................................ ₹53.23 Cr  (0.95% of SAM)
SOM 3yr (base case, +1.0pp SAM share)................... ₹110 Cr    (27.4% CAGR)
SOM 5yr (base case, +2.0pp SAM share)................... ₹166 Cr    (25.5% CAGR)
Capacity ceiling (disclosed, + automation uplift)....... ₹120-134 Cr  <- BINDS before SOM_5yr
```

### 5B. Runway assessment

- **Revenue headroom:** SAM ÷ current revenue = 5,616 ÷ 53.23 = **105.5x**.
- **TAM growth rate:** 6.64% (IMARC/management-cited), cross-checked at 6.96% (Mordor,
  current) — the two estimates agree closely on trajectory despite disagreeing on level.
- **Company CAGR vs TAM:** Rappid's own FY23-FY26 revenue CAGR is 48% (Investor_
  Presentation_1.txt p.7, "48% Revenue CAGR (FY23-FY26)") — roughly 7x the TAM's growth
  rate, meaning historical growth has come from share gain, not from riding the market. Note
  this 48% figure is front-loaded and lumpy (FY26 itself grew only 2.1%, per B04's order-timing-
  distortion flag), so it should not be read as a clean, repeatable trend.
- **Years to saturate SAM at current pace:** using the SOM_3yr-implied 27.4% CAGR,
  ln(105.5)/ln(1.274) ≈ **19 years** to fully saturate the SAM by extrapolation. **This is moot**
  — Section 3C shows capacity binds within 3-5 years, long before SAM saturation would ever
  become the limiting factor. The real runway question for this company is a capex question,
  not a market-size question.

### 5C. Runway classification

No explicit numeric thresholds for MASSIVE/STRONG/GOOD/MODERATE/LIMITED were found
in frameworks/ (only the five-label taxonomy exists, Master_Project_Prompt_v3_6.md:983);
the following bands are ANALYST-DEFINED and stated transparently: MASSIVE = headroom
>50x with TAM growth >5%; STRONG = 20-50x; GOOD = 8-20x; MODERATE = 3-8x; LIMITED =
<3x or TAM shrinking.

**Classification: MASSIVE** on headroom (105.5x) and TAM growth (6.6-7.0%) — but this
label describes the *market*, not the *company's near-term capacity to serve it*. The
operative constraint for the next 3-5 years is capital expenditure, not demand.

### 5D. SAM expansion levers actually being pursued

Only one lever shows evidence of active pursuit: **export certification** (UL and ClassNK
already obtained; US data-centre customer in qualification, 16+ months and counting — B07
optionality register). This would add a slice of the *global*, not the India-only, TAM used in
this SAM — the potential addition is **NOT QUANTIFIABLE from this corpus** given the
customer relationship is undisclosed (NDA) and unconverted. Two other named levers —
domestic data-centre cooling valves and Oil & Gas/Power vertical entry (the single largest
unaddressed slice of the India TAM per Filter 4) — are optionality only: the CMD states
explicitly "no scouting done" on the domestic data-centre opportunity (B07), and zero FY26
revenue is disclosed from Oil & Gas or Power. Neither is treated as a current lever.

### 5E. Final output card

```
TAM (conservative / realistic):  ₹14,976 Cr  /  ₹32,640 Cr   (India industrial valves, 2025)
SAM:                             ₹5,616 Cr   (37.5% of conservative TAM)
Current SAM share:                0.95%
Revenue headroom:                 105.5x
TAM growth:                       6.64-6.96% CAGR
Runway class:                     MASSIVE (market) / CAPACITY-GATED (company, next 3-5 yrs)
SOM 3yr / 5yr:                    ₹110 Cr (27.4% CAGR)  /  ₹166 Cr (25.5% CAGR)
Capacity check:                   insufficient beyond yr3-4; gap ~₹32 Cr by yr5
Mgmt FY27 guidance vs SOM_3yr:    50% vs 27.4% CAGR -> 1.83x (elevated, not clearly inflated)
```

**Valuation implication line:** At 27.4% revenue CAGR implied by SOM (3yr), with a margin
trajectory anchored to FY26's 19.36% EBITDA / 12.17% PAT margin (B07-emoat.yaml
catalysts_12m), the earnings growth embedded here is approximately 25-30% CAGR
(assuming stable-to-improving margin as the ~₹22 Cr low-margin carried book executes),
which **supports** the current valuation of ~24.75x P/E (CMP ₹308.9, 16-17 Sep-2026,
WebSearch 2026-09-19; rating/ and research/ folders both empty in this corpus, so this
external market-price cross-check is offered as context, not as a filed valuation figure) —
**provided** the ~₹120-134 Cr capacity ceiling identified in Section 3C is lifted by fresh capex
within the next 2-3 years. Absent a disclosed capacity expansion beyond continued
automation investment, growth mechanically decelerates once the ceiling is hit, which would
not support the current multiple on an unchanged earnings trajectory.

---

## SECTION 6: DOWNSTREAM SIGNAL CANDIDATES

| # | Candidate Signal | Entity Type | Why It Drives Demand | Likely Primary Source | Expected Cadence |
|---|---|---|---|---|---|
| 1 | Named naval shipyards (Mazagon Dock, Garden Reach Shipbuilders & Engineers, Cochin Shipyard, L&T Shipbuilding) | End-customer | Direct source of Rappid's Marine + Shipbuilding & Repair revenue (32.85% of FY26); order flow to these yards is the single biggest driver of the marine SOM. SHARED with catalyst tracking (B07 FSS shipset catalysts). | Individual shipyard investor disclosures / Ministry of Defence Press Information Bureau (PIB) naval procurement releases | Quarterly / event-driven |
| 2 | Ministry of Defence annual capital outlay and defence-production target (₹3 lakh Cr by 2029) | Macro / Regulatory | Sets the size and pace of the naval-modernisation pipeline Rappid's marine stream depends on. | Union Budget documents; PIB, Ministry of Defence | Annual (Budget day) / event-driven |
| 3 | GeM portal PSU industrial-valve tender awards | Counterparty / Regulatory | PSU tenders are the primary channel for Rappid's industrial-valve stream (fixed-price, no escalation clause per B04); award volume and pricing are directly observable. | Government e-Marketplace (GeM) public tender/award data | Event-driven |
| 4 | US data-centre customer (unnamed, NDA) contract conversion | End-customer | Named optionality item (B07); a signed contract would convert 16+ months of stalled pipeline into recognised export revenue. | Rappid's own Reg 30 / stock-exchange filings (counterparty itself undisclosed) | Event-driven |
| 5 | Praj Industries Ltd — ARC repricing (~₹10-12 Cr) | End-customer | Named, near-term catalyst (B07); Praj is a disclosed customer under active price renegotiation. | Praj Industries Ltd investor disclosures / concalls | Event-driven |
| 6 | Ethanol Blended Petrol (EBP) Programme blending target and OMC (IOCL/BPCL/HPCL) ethanol-infrastructure capex | Regulatory / Macro | Directly underpins Rappid's single largest FY26 vertical (Ethanol/Breweries/Wastewater, 30.81%). | Ministry of Petroleum & Natural Gas / PIB releases | Annual / event-driven |

`demand_externally_verifiable: true` — six externally observable rows are named above, all
above the 3-row minimum.

---

## SEARCH LOG

**Performed:**
1. USD/INR exchange rate, September 2026 (WebSearch)
2. India industrial valves market size 2025-2026, rating agencies (WebSearch — no CRISIL/
   ICRA/CARE valve-specific report surfaced; IMARC/Mordor/VMR/TechSci did)
3. Mordor Intelligence India Industrial Valves Market page (WebFetch, direct)
4. Global marine valves/actuators market size 2025-2026 (WebSearch)
5. Valve content as % of shipbuilding/vessel cost (WebSearch — no anchor found, used to
   confirm the naval-content-% gap rather than invent one)
6. China industrial valves market size 2025 (WebSearch)
7. KSB Limited India FY26 revenue, pumps/valves segment (WebSearch)
8. Atam Valves Ltd / Meson Valves India revenue FY26 (WebSearch — conflicting figures
   surfaced and flagged, not resolved)
9. Meson Valves India Limited (Quest Flow Controls) revenue FY25/FY26, BSE 543982 (WebSearch)
10. Rappid Valves India Ltd share price / P/E ratio, NSE RAPPID (WebSearch)
11. Kirloskar Brothers / L&T Valves revenue and India valve market competitor list (WebSearch)

**Skipped:**
- A dedicated, separate IBEF capital-goods sector report query (general market-size searches
  above already covered comparable ground; not independently queried).
- Any attempt to derive a rupee-denominated Indian naval/marine valve TAM via a valve-
  content-% assumption — deliberately not computed (Method 2/marine section), since no
  sourced percentage exists in the corpus or in search result #5 above; inventing one would
  violate the no-fabrication rule this pipeline runs under.

---

## FLAGS

- **FLAG-MGMT-CLAIM-INCONSISTENCY:** management's "huge opportunity of import
  substitution" claim (Investor_Presentation_1.txt p.25) is undercut by its own cited figures:
  India exported $2.66Bn of valves against $2.15Bn imported in 2024 — a net exporter position,
  not a case for import substitution as framed.
- **FLAG-TAM-SOURCE-DIVERGENCE:** India industrial valves market-size estimates diverge
  more than 2x across named research houses (Mordor $1.56Bn vs IMARC $3.4Bn vs VMR
  $3.73Bn, all ~2024-25 base years), while CAGR estimates cluster tightly at 6.6-7.7%. Treat
  the level as uncertain and the trajectory as the more reliable read.
- **FLAG-CAPACITY-CONSTRAINT:** the disclosed ₹120 Cr revenue capacity ceiling (Jun-2026
  concall) binds the SOM within 3-5 years under both the base and upside share-gain
  scenarios; two years of management's own "50% or more" FY27 guidance sustained would hit
  that ceiling almost exactly. No new capacity plan beyond continued automation investment
  (B07's 12% capex-embedded growth) exists in this corpus.
- **FLAG-NAVAL-TAM-NOT-SIZEABLE:** no company disclosure, peer disclosure, or web search
  performed for this stage produces a rupee- or dollar-denominated size for the Indian naval/
  marine valve market specifically. Carried forward from B06/06-peers.md. Marine SAM/SOM
  in this report is built off Rappid's own revenue and order-book trajectory, not off a derived
  market-size figure.

---

## INPUT GAPS CARRIED

- rating/ folder empty — no credit rating exists for this issuer.
- research/ folder empty — no third-party equity research on file.
- One earnings call only (NO-CONCALL MODE, 01-Jun-2026) — no guidance history to
  cross-check the FY27 "50% or more" claim against a prior-year equivalent statement.
- Peer transcripts 8 of 12 — Marine Electricals dropped (no transcripts filed); no listed
  pure-play marine valve maker exists in India.
- SME half-yearly filer — no quarterly-granularity disclosure to refine the H1/H2 order-timing
  distortion already flagged at B04.
- No per-valve ASP, volume, or valve-content-% of end-market capex anywhere in the corpus —
  Method 2 (bottom-up) marked NOT COMPUTABLE.
- Atam Valves FY26 revenue conflicts across web sources (₹47.30 Cr vs ₹347.29 Cr) — used
  directionally only in Method 3, not resolved.
- FX conversion (₹96/USD) is an analyst assumption (18-Sep-2026 spot rate); no FX rate is
  specified anywhere in the corpus for the USD-denominated market-size figures management
  itself cites.
