# Stage 9 — TAM / SAM / SOM Market Sizing: GSM Foils Ltd (GSMFOILS)

Run date: 2026-07-24 | Model: claude-sonnet-5 | Status: partial (see Section 2 gaps and Search Log)

---

## SECTION 1: MARKET DEFINITION

### 1A. Precise boundaries

- **Product scope:** aluminium-based primary pharmaceutical packaging materials converted by GSM —
  (i) blister lidding foils, 20/25 micron, nitrocellulose-coated/vinyl-solution laminated bare aluminium
  (source: Investor Presentation Q1 FY27, p.8-9); (ii) aluminium strip/pharma foils, 30/40 micron with
  150 GSM LDPE (source: Investor Presentation, p.10); (iii) aluminium ROPP caps for pharma syrup bottles
  and alcohol/beverage bottles, commercial since Jun-2026 (source: Investor Presentation, p.14).
  **Excluded:** cold-form/Alu-Alu (CFF) blister foil — not evidenced as a current GSM product in the AR
  or IP; plastic/PVC-PVDC forming films, glass vials/ampoules, prefilled syringes, cartons/labels/inserts,
  non-pharma aluminium foil (household, food & beverage, industrial/HVAC/cable — ~70% of the global
  aluminium foil end-use base per GSM's own IP, p.19).
- **Geographic scope:** India domestic. GSM discloses "14+ States" presence (Investor Presentation, p.6)
  and manufacturing in Vasai/Palghar (Maharashtra), Ahmedabad (Gujarat), and a Mumbai-region ROPP unit
  (Investor Presentation, p.11-14). Unit 4 (export-oriented, Vasai) is planned but uncorroborated —
  OPERATOR_CONTEXT flags the 23-Jul-2026 announcement as not yet in inputs. TAM here is scoped to India;
  export potential is treated as a SAM-expansion lever (Section 5D), not counted in the base TAM.
- **Customer scope:** Indian pharmaceutical formulators (branded generics, generics, OTC) — "110+"
  clients (Investor Presentation, p.6); secondary customer set for ROPP: alcohol/beverage bottlers
  (Investor Presentation, p.14).
- **Channel scope:** direct B2B supply to formulators, not through packaging distributors/traders.
  Pricing is a monthly cost-pass-through model off Hindalco letters (B04 business-model block,
  operator digest) — a commodity-converting model, not a branded/retail channel.
- **Price segment:** standard/commodity-grade blister and strip foil converting. GSM's disclosed
  certifications (ISO 9001:2015, CGMP declaration, Residual-Solvent, TSE/BSE, Food-Grade, BIS —
  Investor Presentation p.17) do **not** list USFDA or EU-GMP facility approval, which caps GSM's
  realistic customer base to domestically-regulated/generic-focused formulators rather than the
  most stringently-regulated export-grade segment (this is carried into the SAM customer filter,
  Section 3A).
- **Explicit exclusions:** cold-form/Alu-Alu (CFF) foil, plastic/PVC blister films, glass/plastic
  primary containers, cartons/secondary packaging, packaging equipment/machinery, non-pharma
  aluminium foil, non-India geography (ex-Unit 4 upside).

### 1B. Management's own TAM claim(s), held for comparison

From the **Q1 FY27 Investor Presentation** (dated Jul 2026, the most current document in inputs), p.19-20,
sourced by management to "IBEF, World Manufacturing Organization Reports":
- Global aluminium foil market: USD 32bn (2025) → USD 51bn (2035), 5.4% CAGR.
- Indian Packaging Industry: USD 84bn (2024) → USD 143bn (2029).
- Indian Pharmaceutical Market: USD 42bn (2021) → USD 55bn (2025) → USD 130bn (2030P).
- Pharmaceutical packaging is stated as ~30% of global aluminium foil end-use (indicative split, "based
  on industry averages").

From the **AR FY25 MD&A** (dated Sep-2025, AR filed for FY2024-25), p.49-51:
- Global aluminum foil market: USD 23.1bn (2020) → USD 30.4bn (2027), CAGR 3.8% — **STALE**, base year
  2020 is 6 years old at run date.
- India Aluminum Market (the whole metal market, not packaging-specific): USD 13.79bn (2023) →
  USD 21.46bn (2030), CAGR 6.70% — **STALE-BORDERLINE**, base year 2023 is 3 years old; also far too
  broad a scope (includes construction, automotive, electrical aluminium demand, not packaging).

From the **IPO Note** (X-B4 Advisory, non-anchored per injected inputs, undated within the extract):
Indian packaging industry "projected to reach $204.81 billion by 2025 (from $50.5 billion in [base
year not stated])." This is inconsistent with the Jul-2026 IP's own $84bn (2024) figure for the same
industry — a >2x internal contradiction across GSM's own document set. **Treated as unreliable; not
used as an anchor.**

From the **operator digest** (non-anchored, OPERATOR_CONTEXT.md): management guidance of FY27 topline
₹400-450cr (vs ₹258cr FY26) "on ramp alone, even a mediocre/average year," plus a claimed "market
doubling over five years." Neither figure is corroborated by a document in inputs; the doubling claim
is cross-checked against independent data in Section 2.

**Credibility read: BROAD.** Every headline figure management cites (global aluminium foil market,
India's total aluminium market, the entire Indian packaging industry, the entire Indian pharmaceutical
market) is the wrong denominator — one to two orders of magnitude larger than GSM's actual product/
customer/geography footprint (aluminium pharma foil + ROPP caps, India only). None of management's
cited figures is scoped to "aluminium-based pharmaceutical packaging in India," which is the actual
market GSM competes in. This is the TAM=SAM=growth-runway pattern the operating rules flag as dishonest;
it is not fraud, it is standard IR-deck practice, but it means none of management's cited numbers can be
used as the TAM anchor for this stage — Section 2 builds an independent figure instead.

---

## SECTION 2: TAM ESTIMATION, MULTIPLE METHODS

All conversions use USD/INR = 96.5 (X-Rates.com, average rate accessed 2026-07-24, spot 96.5-96.9 range
in the week of the run date — this is a materially weaker rupee than the ~83-88 range commonly used in
older analyses; flagged as a live, sourced figure, not an estimate). 1 USD bn ≈ ₹9,650cr.

### Method 1 — Top-down (India pharma packaging market, filtered)

- Base: **India Pharmaceutical Packaging Market = USD 5.14bn (2025)**, 8.72% CAGR to USD 7.81bn (2030)
  (Mordor Intelligence, accessed via web search 2026-07-24 — current, not stale). = ₹49,601cr (2025).
  This base is ALL materials (glass, plastic, paper, metal) and ALL pack formats (primary + secondary),
  so it must be filtered down.
- Filter 1, primary packaging only (excl. equipment, cartons, labels, secondary/tertiary): apply
  76.4% primary-packaging share (Grand View Research, global 2025 figure used as a proxy for India —
  **flagged, global proxy not India-specific, moderate confidence**). 49,601 × 0.764 = ₹37,905cr.
- Filter 2, aluminium-foil-based formats only (excl. glass vials/ampoules, plastic bottles, prefilled
  syringes, non-foil sachets): apply a conservative 30% aluminium-foil share of primary pharma
  packaging value (aluminium is one of several primary materials alongside glass, plastic, paper —
  **no disclosed India-specific split was found; this is an analyst estimate, flagged low-medium
  confidence**). 37,905 × 0.30 = **₹11,371cr ≈ ₹11,400cr** — Method 1 TAM (foil only, 2025).

### Method 2 — Bottom-up (blister/strip pack format, foil-cost-share filter)

- Addressable unit: revenue of the "India Healthcare Blister Packaging" segment, which is the closest
  disaggregated, India-specific, format-relevant figure available. Grand View Research (horizon
  report, accessed 2026-07-24): USD 1.916bn (2023) → USD 3.286bn (2030), implied 8% CAGR
  (internally consistent: 1.916 × 1.08^7 = 3.285, matches). This still blends plastic-film and
  aluminium-foil blister/strip formats.
- Project to 2025: 1.916 × 1.08² = USD 2.235bn = ₹21,567cr.
- Filter: aluminium foil's cost share of a blister/strip pack. Aluminium is stated as "the largest
  revenue-generating material" in this segment (2023, same source) but no exact % is disclosed.
  Conservative mid-point applied: **45%** (blister lidding foil typically runs 40-60% of a standard
  blister pack's material cost; strip packs, which GSM also makes, are ~100% foil — **NOT FOUND: exact
  disclosed split; this is an estimate, flagged**). 21,567 × 0.45 = **₹9,705cr ≈ ₹9,700cr** — Method 2
  TAM (foil only, 2025).

Methods 1 and 2 triangulate reasonably (₹9,700-11,400cr), from two independent, India-specific, current
(2025-based) reports. **Conservative TAM (foil) = ₹9,700cr; realistic TAM (foil) = ₹11,400cr.**

### Method 3 — Peer revenue aggregation (directional only, LOW confidence)

Organised, India-specific aluminium pharma-foil converters are almost entirely private/unlisted:
Positive Packaging Industries, Raviraj Foils, Singhvi Foils, SGM India, FlexiPack, NG Packaging, Rainbow
Plastic Industries — none disclose audited revenue in public search results (**NOT FOUND** for all).
Ess Dee Aluminium was historically the dominant listed player (first in India to make cold-form
blister/child-resistant blister packaging) but its post-2013 financial distress and de-scaling means its
current revenue contribution is not corroborable from search (**NOT FOUND, current status**). Mordor
Intelligence's own commentary on the broader India pharma packaging market states "no single company
exceeds a 15% revenue share" — this corroborates a fragmented structure but cannot independently size a
₹cr TAM. Method 3 is used only to confirm fragmentation (Section 4C), not as a sizing anchor.

### Method 4 — Import substitution (limited applicability)

India is the world's second-largest consumer of aluminium foil (915,000 tonnes demand) and
second-largest producer (750,000 tonnes output) — a net import gap of ~165,000 tonnes (~18% of
demand) (IndexBox, India Aluminium Foil Market Report 2026, accessed 2026-07-24). This gap sits mostly
at the raw-foil-stock/metal level (GSM buys converted coil from domestic suppliers like Hindalco per
the operator digest), not at the finished-blister-foil level where domestic converters appear to
dominate supply. **Not used as a TAM anchor** — flagged as directional context only: India's foil
converting base (including GSM) is not meaningfully import-substituting finished pharma foil, so this
method contributes limited signal here.

### Method 5 — Global benchmark (wide range, LOW confidence — flagged, not used as anchor)

Two global-benchmark constructions were tried and diverge sharply from each other and from Methods 1-2:
- (a) "Aluminium Blister Foil Market" = USD 1.5bn global (2024), CAGR 6.5% to USD 2.5bn (2033)
  (Verified Market Reports, accessed 2026-07-24 — vendor/scope unclear, no India split). Applying a
  15-20% India-share proxy (India's stated ~20% share of world generics by volume, GSM's own IP p.20,
  sourced IBEF) gives USD 225-300M ≈ **₹2,170-2,895cr** — roughly a quarter of Methods 1-2.
- (b) Global aluminium foil packaging market ≈ USD 30-32bn (2025/26, multiple sources incl. GSM's own
  IP) × 30% pharma end-use share (GSM's own IP, p.19) = USD 9-9.6bn global pharma aluminium foil
  packaging, × 20% India volume-share proxy = USD 1.8-1.92bn ≈ **₹17,370-18,530cr** — roughly 1.6-1.9x
  Methods 1-2.
Per the conservative-bias and divergence-flagging rules: these two global-benchmark variants bracket
Methods 1-2 from both sides by a wide margin, which signals the underlying vendor reports are
inconsistent with each other (a known feature of SEO-market-report aggregators) rather than that the
true TAM is materially different. **Method 5 is not used to set the headline TAM; Methods 1 and 2
(India-specific, most directly sourced, mutually consistent) remain the anchor.**

### ROPP caps — separate addressable segment (added to TAM, not folded into the foil methods above)

- Global Aluminium Caps and Closures Market: USD 6.82bn (2025) → USD 11.62bn (2035), 5.4% CAGR
  (Emergen Research, accessed 2026-07-24). ROPP caps are 41.1% of this market by product type (2023,
  same search). Global ROPP caps market ≈ USD 6.82bn × 0.411 = USD 2.80bn (2025).
- **NOT FOUND: an India-specific ROPP caps market size in USD or ₹.** Search confirms "India leading
  at 8.2% CAGR through 2035" for the aluminium ROPP closure market but gives no base-year ₹/USD figure
  (Future Market Insights, accessed 2026-07-24). A conservative 4-6% India-share-of-global proxy is
  applied (India's manufacturing share of global pharma + beverage bottling, judgment-based, **flagged
  low confidence, not sourced to a specific India ROPP report**): USD 2.80bn × 0.04-0.06 =
  USD 112-168M ≈ **₹1,080-1,620cr** (conservative-realistic range, 2025).

### Triangulation table

| Method | Estimate (₹Cr, 2025) | Confidence | Staleness |
|---|---|---|---|
| 1. Top-down (India pharma packaging → filtered) | 11,400 | Medium | Current (2025 base) |
| 2. Bottom-up (India blister packaging → foil filter) | 9,700 | Medium | Current (2025 base) |
| 3. Peer aggregation | Not sizeable (directional: confirms fragmentation) | Low | Current |
| 4. Import substitution | Not applicable as anchor | Low | Current |
| 5. Global benchmark | 2,170-18,530 (wide, inconsistent) | Low | Current but vendor-inconsistent |
| ROPP caps (adjunct) | 1,080-1,620 | Low | Current, India split unsourced |

**Conservative TAM = ₹9,700cr (foil) + ₹1,080cr (ROPP) = ₹10,780cr.**
**Realistic TAM = ₹11,400cr (foil) + ₹1,620cr (ROPP) = ₹13,020cr.**
(both 2025, India, aluminium-based pharma foil + ROPP caps only)

**Management's claim vs. conservative estimate:** management cites no figure scoped to this actual
market (Section 1B) — every cited figure is 30-100x larger because it is the wrong denominator (global
aluminium foil, whole Indian pharma industry, whole Indian packaging industry). Per the task's specific
instruction, the mgmt-claim ratio used for the formal handoff instead compares management's FY27/
medium-term revenue ambition (₹400-450cr) to the independently-sized SOM (Section 3B), not to TAM —
see below.

**Cross-check: the "market doubling over five years" claim (operator-relayed, non-anchored).** Neither
independent India-specific series supports a doubling in five years for the relevant packaging market:
India pharma packaging market (Mordor) grows 1.52x over 2025-2030 (8.72% CAGR); the India healthcare
blister packaging segment (Grand View) grows 1.47x over the same span (8% CAGR); the broader Indian
Packaging Industry (GSM's own IP) grows 1.70x, 2024-2029 (~11.2% CAGR). The only series in GSM's own
document set that DOES roughly double in five years is the **Indian Pharmaceutical Market** overall
(USD 55bn 2025 → USD 130bn 2030P, 2.36x, ~18.8% CAGR) — but that is the market for drugs, not for
packaging. If the "doubling" claim traces to this figure (plausible, given it sits on the same slide
as the packaging figures), it is the same wrong-denominator conflation flagged in Section 1B: the
end-market for medicines is not GSM's addressable market; the packaging market growth (8-11% CAGR) is.
**Read: the doubling claim is not corroborated for GSM's actual TAM and is treated as unreliable
management commentary, consistent with its non-anchored status.**

---

## SECTION 3: SAM & SOM

### 3A. SAM — five filters applied to conservative TAM

**Foil TAM (₹9,700cr) filters:**
| Filter | Multiplier | Basis |
|---|---|---|
| Product fit | 0.72 | excludes cold-form/Alu-Alu (CFF) foil, a growing premium sub-segment GSM does not evidence making; standard blister+strip assumed ~70-75% of the foil TAM |
| Geography | 0.95 | GSM covers 14+ states but is Maharashtra/Gujarat-centred; minor haircut for thin coverage elsewhere (Investor Presentation, p.23) |
| Channel | 1.00 | GSM's direct-B2B model matches how the TAM base is structured; no cut |
| Customer | 0.70 | no USFDA/EU-GMP facility approval disclosed (Investor Presentation, p.17 certifications list) — excludes the most stringently-regulated, export-grade formulator segment |
| Capability | 0.95 | near-term lead-time/onboarding haircut for un-penetrated accounts |

Foil SAM = 9,700 × 0.72 × 0.95 × 1.00 × 0.70 × 0.95 = **₹4,410cr**

**ROPP TAM (₹1,080cr) filters:**
| Filter | Multiplier | Basis |
|---|---|---|
| Product fit | 0.90 | already ROPP-specific; minor exclusion for non-pharma/non-beverage ROPP use |
| Geography | 0.95 | same as above |
| Channel | 1.00 | direct B2B, no cut |
| Customer | 0.85 | Unit 3 currently structured around a single MoU counterparty (AAPL Solutions) — limits immediate addressable customer breadth versus a mature multi-client ROPP supplier |
| Capability | 0.90 | single new unit (commercial since Jun-2026), still ramping |

ROPP SAM = 1,080 × 0.90 × 0.95 × 1.00 × 0.85 × 0.90 = **₹710cr**

**Total SAM = ₹4,410cr + ₹710cr = ₹5,120cr.**
**SAM as % of conservative TAM (₹10,780cr) = 47.5% ≈ 47%.**

### 3B. SOM at 3 and 5 years

Current SAM share: GSM FY26 revenue ₹258.15cr (screener Data_Sheet, y/e 31-Mar-2026) ÷ SAM ₹5,120cr =
**5.04% ≈ 5.0%.**

Share-gain trajectory: GSM's FY25 (+228%) and FY26 (+93%) growth has been capacity-ramp-driven
(Ahmedabad Unit 2 coming online, Vasai near-full utilisation) rather than organic share-taking in a
static market. Two new, capex-committed units are ramping within the 3-year window (Ahmedabad to 80%+
utilisation by Mar-2027; ROPP Unit 3 commercial since Jun-2026) — this fits the "aggressive" 3-5pp/3yr
share-gain band (capacity- and execution-backed, no competitor-exit or acquisition evidence, so the
>5pp band does not apply). Applied: **+4pp over 3 years, +7pp cumulative over 5 years.**

SAM itself grows at the blended TAM CAGR (~8%, averaging Mordor's 8.72%, the blister-segment's 8%, and
ROPP-India's stated 8.2% CAGR):
- SAM (Yr3) = 5,120 × 1.08³ = ₹6,449cr
- SAM (Yr5) = 5,120 × 1.08⁵ = ₹7,523cr

SOM (3yr) = 6,449 × (5.04% + 4pp = 9.04%) = **₹583cr**
SOM (5yr) = 7,523 × (5.04% + 7pp = 12.04%) = **₹906cr**

Implied revenue CAGR from FY26 base (₹258.15cr):
- 3yr: (583 / 258.15)^(1/3) − 1 = **31.2%**
- 5yr: (906 / 258.15)^(1/5) − 1 = **28.6%**

**This is the formal handoff to stage 11:** som_implied_revenue_cagr {yr3: 31.2%, yr5: 28.6%}.

### 3C. Capacity cross-check

Corroborated, in-inputs capacity (excludes the uncorroborated Unit 4 export line):
- Vasai Unit 1 (near-full) + Ahmedabad Unit 2 (ramping to 80%+ utilisation by Mar-2027): combined
  foil run-rate ~₹60-65cr/month at optimum (operator digest; directionally consistent with the AR/IP's
  disclosed 17,000+ MT/annum installed capacity and Ahmedabad's stated 10k+ MT/annum, Investor
  Presentation p.13) = **₹720-780cr/year**.
- Unit 3 ROPP: ~₹50cr/year at peak (Investor Presentation, p.14, directly anchored).
- Corroborated total = **₹770-830cr/year**, achievable within the 3-year SOM window (management's own
  Mar-2027 timeline sits inside Year 1-2 of it).

**This exceeds SOM (3yr) of ₹583cr by ₹187-247cr.** Capacity is not the binding constraint — GSM's own,
already-committed capacity plan already implies more revenue than the independent SAM/SOM math
supports without an unusually fast share gain. Cross-checking further: ₹770-830cr against the foil
TAM alone (₹9,700cr conservative) is a 7.9-8.5% TAM share within roughly 12-18 months of Mar-2027,
versus GSM's current ~2.7% share of that same TAM (258/9,700) — an implied +5pp move in about a year,
which sits outside the "aggressive" 3-5pp/**3-year** norm this framework applies, absent any
competitor-exit or acquisition evidence.

**Capacity check: gap of ~₹190-250cr by Year 3 — the capex/guidance side is the more optimistic one.**
Two readings are possible and neither can be resolved from inputs: (a) management's Mar-2027 utilisation
targets are optimistic and may undershoot, or (b) GSM's true served niche (specific micron
specifications, specific client relationships, specific regional clusters) is narrower than the
generically-defined "India blister+strip aluminium pharma foil market" used here, in which case GSM
could rationally hold a much higher share of its actual served niche while remaining small against the
broad category total. This tension should be stress-tested at stage 11 rather than resolved here.

---

## SECTION 4: GROWTH DRIVERS, RISKS & STRUCTURE

### 4A. TAM growth drivers

| Driver | Impact | Evidence |
|---|---|---|
| Unit-dose penetration (bottle → blister/strip shift) | Medium-High | "Global shift from bottle packaging to unit-dose formats... better compliance and hygiene" (Investor Presentation, p.20) |
| Per-capita consumption | Medium | "India's low per capita consumption is projected to drive demand growth of 6%-8% annually" (AR FY25 MD&A, p.51) |
| Premiumisation (CFF/Alu-Alu, biologics) | Medium (upside for GSM only if it enters CFF) | "Biosimilars market in India... USD 12bn by 2025 (CAGR 22%)... require advanced barrier packaging" (Investor Presentation, p.20) — GSM does not currently evidence CFF capability |
| Formalisation of unorganised converters | Medium, directional | Fragmented structure, "no single company exceeds 15% revenue share" (Mordor Intelligence, accessed 2026-07-24); GMP/traceability push favours organised players |
| Regulatory tailwind | High | "USFDA, WHO-GMP, and EU regulations mandate light/moisture/oxygen barrier packs" (Investor Presentation, p.20) |
| Import substitution | Low-Medium | Applies mainly to raw aluminium coil, not finished pharma foil (Section 2, Method 4) |
| New applications (ROPP into alcohol/beverage) | Medium-High, GSM-specific | Unit 3 diversification already executed (Investor Presentation, p.14) |
| Geographic expansion | Medium | GSM's own stated roadmap item; 14+ states currently vs full India coverage (Investor Presentation, p.6, p.22) |
| Technology enablement | Low-Medium | VMCH coating machine, spares upgrades (Investor Presentation, p.7) — mostly efficiency, not TAM expansion |
| Demographics | Medium, weakly sourced | General rising healthcare consumption; **not explicitly evidenced in the injected documents**, treated as low-confidence background factor |

### 4B. TAM risks

| Risk | Monitoring signal |
|---|---|
| Substitution by plastic-only films for less-sensitive drug categories (cost-driven) | Aluminium vs PVC/PVDC input-cost spread |
| Environmental/EPR restriction: recycled-content mandates (30% now, rising to 60% by 2027-28 per pharma-packaging market search) could favour mono-material recyclable formats over multi-layer foil laminates | EPR compliance-cost disclosures, substrate-mix shift in industry reports |
| Saturation: underlying TAM growth is single-digit (8-9% CAGR) | TAM growth deceleration below ~6% in future reports |
| Disruption from alternative unit-dose formats reducing foil intensity per pack | Material-mix data in future Mordor/Grand View updates |
| Import competition | Not directly evidenced at finished-foil level; mainly an upstream raw-aluminium-coil issue (India net importer, ~165,000-tonne gap, IndexBox 2026) |
| Cyclical downturn | Low — pharma demand is largely defensive/non-discretionary |

### 4C. Market structure

- **Competitor count / concentration:** fragmented; no single India pharma-packaging player exceeds a
  15% revenue share (Mordor Intelligence, accessed 2026-07-24). Precise top-3 concentration ratio:
  **NOT FOUND.**
- **Organised vs unorganised split:** not quantified specifically for aluminium pharma foil in any
  source found; the pipeline's standard India default range (30-60% unorganised) is noted as an
  unsourced assumption, not a hard figure — **flagged, not anchored.**
- **Consolidating or fragmenting:** directional evidence of past exits (Ess Dee Aluminium's post-2013
  distress/de-scaling from its former dominant position) alongside continued new entry (GSM itself,
  LLP-to-NSE-Emerge-listed since 2024) suggests an open, not tightly consolidating, market.
- **Price vs differentiation competition:** predominantly price/cost-pass-through (monthly Hindalco
  pricing letters, B04 business-model block); differentiation is limited to quality certification
  (ISO, CGMP, food-grade, BIS) and reliability rather than product uniqueness. The CFF/Alu-Alu premium
  segment (which GSM does not currently serve) offers more differentiation-based competition.
  Genuine unmet demand outside GSM's current segment is more of a margin/mix opportunity than a
  new-market opportunity — see Section 5D.
- **Entries and exits:** GSM's own ROPP entry (Jun-2026) is a recent diversification entry; Ess Dee's
  historical decline is the clearest exit precedent found. No further entry/exit data located —
  **NOT FOUND** beyond these two data points.
- **Import share trend:** India is a net importer of aluminium foil in aggregate (915,000 tonnes
  demand vs 750,000 tonnes domestic output, ~18% gap, IndexBox 2026) — this sits mostly at the
  raw-metal level, not the finished blister/strip foil level where converters like GSM operate.

---

## SECTION 5: SUMMARY & RUNWAY

### 5A. Funnel

```
TAM (conservative, India, alu pharma foil + ROPP, 2025)   ₹10,780cr
   -> SAM (5 filters applied)                              ₹5,120cr   (47% of TAM)
      -> SOM, 3yr                                          ₹583cr    (9.0% of Yr3 SAM)
      -> SOM, 5yr                                          ₹906cr    (12.0% of Yr5 SAM)
Current GSM revenue (FY26)                                 ₹258.15cr (5.04% of current SAM)
```

### 5B. Runway assessment

- Revenue headroom = SAM ÷ current revenue = 5,120 / 258.15 = **19.8x.**
- TAM growth rate (blended) ≈ **8.5%** CAGR (Mordor 8.72% India pharma packaging; Grand View 8% India
  healthcare blister packaging; ~8.2% India ROPP CAGR).
- Company CAGR vs TAM: GSM's realised growth (FY25 +228%, FY26 +93%) is 10-25x the underlying TAM's
  growth rate — GSM is overwhelmingly a **capacity-driven share-gainer**, not a market-rider. This is
  consistent with two new plants ramping rather than the market itself accelerating.
- Years to saturate current SAM: using the SOM-implied CAGR (28-31%) as a sustainable proxy,
  ln(5,120/258.15) / ln(1.30) ≈ **11-12 years** — well beyond the 3-5 year explicit window. Using the
  unsustainable FY25/26 hyper-growth rate instead would imply ~4-5 years, but that pace is capacity-
  ramp-driven and not a reasonable steady-state assumption once the two foil units and the ROPP unit
  reach full utilisation.

### 5C. Runway classification: **STRONG**

Headroom (19.8x) sits in the 10-50x band with a moderate, mid-single-to-high-single-digit-percent TAM
growth rate (8-9%). This falls short of MASSIVE (typically requires >15-20% underlying TAM growth or
>50x headroom, neither of which applies here — the underlying packaging market itself is not a
hyper-growth category) but comfortably clears GOOD/MODERATE.

### 5D. SAM expansion levers actually being pursued

| Lever | Status | Potential addition | Revised headroom impact |
|---|---|---|---|
| ROPP caps scale-up beyond Unit 3's ₹50cr peak | Committed, ramping | ₹50-150cr if capacity doubled/tripled (not yet committed beyond Unit 3) | Modest |
| Forward integration into specialised printing/conversion (8-10pp higher margin, per operator digest) | Guided, targeted end-FY27 | Margin/mix capture, not new TAM — excluded from SAM/SOM math above | Margin uplift only |
| Unit 4 export orientation | **Uncorroborated** — Reg 30 filing not in inputs | ₹60-180cr/year if realised; would also be genuine geography-based SAM expansion (new export markets, not counted in the India-only TAM above) | Material if realised, currently a flagged gap |
| Cold-form/Alu-Alu (CFF) entry | **Not evidenced** — no management commitment found | ~₹2,720cr of currently-filtered-out foil TAM (the 28% excluded by the product-fit filter in 3A) would become addressable; even a 5% share of that slice ≈ ₹136cr | Material but speculative — not built into base numbers |

### 5E. Final output card

At **28.6-31.2% revenue CAGR** implied by SOM (3yr: 31.2%, 5yr: 28.6%), with a margin trajectory of
**~11.5-12% EBITDA** (management's own stated stance is to "sustain," not expand, EBITDA margin in
FY27, per the operator digest — consistent with B04's flagged 10-14% must-track range), the earnings
growth embedded here is approximately **28-31% CAGR**, assuming broadly stable EBITDA margins and no
major additional operating-leverage step-up beyond already-committed capacity. This is a formal input
to stage 11; **current P/E is NOT FOUND in the inputs available to this stage** (B04 flags EV/EBITDA,
not P/E, as GSM's stated primary valuation approach), so the supports/does-not-support verdict against
a specific multiple is deferred to stage 11's valuation work rather than asserted here.

---

## SEARCH LOG

**Searches performed:**
1. India pharmaceutical packaging market size 2025-2030 (CRISIL/CARE/Mordor)
2. India aluminium foil pharma packaging blister foil market size/CAGR
3. Global pharmaceutical packaging market size 2025 CAGR (Grand View Research)
4. ROPP caps / aluminium closures market size, India
5. Blister packaging market India size 2025-2030
6. India pharma foil/blister packaging companies — peer aggregation attempt (CGRAPHICS, Ester)
7. GSM Foils "market doubling" claim — direct verification attempt
8. India aluminium foil converting industry, named peers (Ess Dee, Positive Packaging, Parksons), tonnes
9. CGRAPHICS ticker identification (aluminium pharma packaging)
10. India pharma packaging market — organised/unorganised fragmentation
11. USD/INR exchange rate, July 2026 (for ₹cr conversion basis)
12. Attempted direct fetch of GSM Foils Q3 FY26 concall transcript (NSE archives) to verify the
    "market doubling" quote directly — **blocked, HTTP 403 (NSE archive access restriction)**

**Searches skipped / not completed:**
- Proprietary CRISIL/ICRA/CARE rating-agency industry reports — paywalled, not accessible via public
  search; flagged as a data-quality gap for a more rigorous top-down anchor.
- India-specific cold-form/Alu-Alu (CFF) foil market segment sizing — searched via the general
  aluminium-foil-market queries above but no India-specific ₹/USD figure surfaced; treated as
  **NOT FOUND**, not pursued further given time constraints.
- Direct confirmation/refutation of the "market doubling in five years" quote at source (concall
  transcript) — blocked by NSE archive 403; cross-check instead performed against independent
  third-party market-size series (Section 2), which is a reasonable substitute but not a direct
  quote verification.

---

```yaml
stage: B09-tam
company: "GSMFOILS"
run_date: "2026-07-24"
model: claude-sonnet-5
status: partial
input_gaps:
  - "India-specific ROPP caps market size (₹/USD) — not found, India-share proxy applied (4-6% of global) with low confidence"
  - "Aluminium foil's exact cost-share of a blister/strip pack — not disclosed anywhere found; 45% mid-point estimate applied, flagged"
  - "India-specific cold-form/Alu-Alu (CFF) foil market size — not found"
  - "GSM's USFDA/EU-GMP facility approval status — not confirmed in extracts (certifications list omits it); customer-fit SAM filter assumes it is absent"
  - "Top-3 concentration ratio and organised/unorganised split for aluminium pharma foil specifically — not found; standard 30-60% unorganised range used as an unsourced default only where noted"
  - "Direct verification of management's 'market doubling in five years' claim at source (concall) — NSE archive fetch blocked (403); cross-checked indirectly against independent series instead"
flags:
  - "Management's own cited TAM figures (global aluminium foil market, India's total aluminium market, whole Indian packaging industry, whole Indian pharma market) are all the wrong denominator, 30-100x larger than GSM's actual addressable market — classic TAM=SAM conflation, not usable as an anchor"
  - "Operator-relayed 'market doubling over five years' claim is NOT corroborated by any independent India pharma-packaging or blister-packaging series (1.47-1.70x growth over the relevant 5yr spans, not 2x); only the whole Indian pharmaceutical (drugs) market roughly doubles, which is the wrong market"
  - "Capacity check shows a ₹190-250cr gap: GSM's own committed capacity (₹770-830cr/yr foil+ROPP run-rate by Mar-2027) exceeds the independently-modelled 3yr SOM (₹583cr) — the capex/guidance side is the more optimistic one; stage 11 should stress-test whether GSM's true served niche is narrower than the generic TAM used here"
  - "USD/INR conversion used 96.5 (spot, accessed 2026-07-24), materially weaker than rates commonly used in older comparisons — flagged as it materially affects all ₹cr figures in this report"
  - "IPO note's Indian packaging industry figure ($204.81bn by 2025 from $50.5bn) directly contradicts GSM's own Jul-2026 IP figure ($84bn 2024) — internal inconsistency in GSM's own document set, IPO note figure discarded"
market_definition: "India-only aluminium-based pharmaceutical blister/strip foil converting plus aluminium ROPP caps (pharma syrup + alcohol/beverage); excludes cold-form/Alu-Alu foil, plastics, glass, cartons, and non-pharma aluminium foil"
tam_cr: {conservative: 10780, realistic: 13020}
sam_cr: 5120
sam_pct_of_tam: 47
som_3yr_cr: 583
som_5yr_cr: 906
som_implied_revenue_cagr: {yr3: 31.2, yr5: 28.6}
current_sam_share_pct: 5.0
revenue_headroom_x: 19.8
tam_growth_pct: 8.5
runway_class: "STRONG"
mgmt_claim_cr: 425
mgmt_claim_ratio: 0.73
mgmt_claim_read: "reasonable"
capacity_check: "gap of ~₹190-250cr by Year 3; corroborated capacity (foil+ROPP run-rate ~₹770-830cr/yr by Mar-2027) exceeds the independently-sized SOM_3yr (₹583cr) — the capex/guidance side is the optimistic one, or GSM's true served niche is narrower than the generic TAM used here"
methods_used: ["top_down", "bottom_up", "peer_aggregation_directional", "import_substitution_limited", "global_benchmark_low_confidence"]
stale_data_flags:
  - {datapoint: "Global aluminum foil market USD23.1bn(2020)->USD30.4bn(2027), CAGR 3.8%", source: "GSM Foils AR FY25 MD&A, p.49-50", year: 2020}
  - {datapoint: "India Aluminum Market USD13.79bn(2023)->USD21.46bn(2030)", source: "GSM Foils AR FY25 MD&A, p.50, citing 'India Aluminum Market Industry Trends & Forecast Report 2030'", year: 2023}
  - {datapoint: "Indian packaging industry $204.81bn by 2025 from $50.5bn", source: "IPO Note (X-B4 Advisory, non-anchored, undated in extract)", year: "undated, internally inconsistent with GSM's own Jul-2026 IP figures"}
searches_performed:
  - "India pharmaceutical packaging market size 2025 2030 CRISIL CARE Mordor billion"
  - "India aluminium foil pharma packaging blister foil market size CAGR"
  - "global pharmaceutical packaging market size 2025 CAGR Grand View Research"
  - "ROPP caps aluminium closures market size India"
  - "blister packaging market India size 2025 2030 crore"
  - "India pharma foil aluminium blister packaging companies CGRAPHICS Ester revenue market share"
  - "GSM Foils market double pharma packaging management guidance"
  - "India aluminium foil converting industry pharma grade blister foil manufacturers Ess Dee Positive Packaging Parksons market size tonnes"
  - "CGRAPHICS NSE company aluminium pharma packaging Alu-Alu blister foil"
  - "India pharma packaging market unorganised organised share fragmentation converters"
  - "USD INR exchange rate July 2026"
searches_skipped:
  - "Proprietary CRISIL/ICRA/CARE rating-agency reports (paywalled)"
  - "India-specific cold-form/Alu-Alu (CFF) foil market sizing (searched broadly, not resolved, not pursued further)"
  - "Direct concall-transcript verification of 'market doubling' quote (NSE archive fetch returned HTTP 403)"
```
