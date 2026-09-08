# STAGE 9 — TAM / SAM / SOM MARKET SIZING
## Borana Weaves Ltd (BORANA) | Run date 2026-09-07

---

## SECTION 1: MARKET DEFINITION

### 1A. Precise boundaries

Borana sells one thing at scale: unbleached, undyed, unprinted synthetic (predominantly polyester) woven fabric — "greige" or "grey" fabric — produced on water-jet looms and sold as an intermediate industrial input, not a finished good. 90.95% of FY26 revenue (Rs 353.41 cr of Rs 388.59 cr, AR FY2026 p.112 Note 21). This stage sizes the market at that step: WEAVING, not fibre production and not apparel/finished-fabric retail. Every number below is tagged with which value-chain step it belongs to, because the corpus (RHP, AR, investor decks) routinely blends "textile industry," "man-made fibre industry," "polyester yarn industry" and "weaving industry" numbers in the same paragraph.

- **Product scope**: unbleached, undyed synthetic (polyester-dominant) woven fabric, produced on shuttleless (principally water-jet) looms. Excludes: cotton-only woven fabric, knitted fabric, dyed/finished/printed fabric, garments, yarn sold as a standalone product (Borana's own PTY-yarn stream, 4.56% of FY26 revenue, is a by-product of spare texturising capacity and is explicitly excluded from this TAM — Concall Q3FY26 p.13: "it is not part and parcel of the business").
- **Geographic scope**: India, domestic sale only. Borana's FY26 revenue from outside Gujarat was 0.11% (RHP p.178); it has zero export revenue (AR FY2026 Note 21(2)). The TAM defined here is therefore India-wide (to size the addressable opportunity), with SAM narrowed to the geography Borana can actually reach (Section 3A).
- **Customer scope**: traders and dyeing/processing houses — B2B intermediate-goods buyers who finish the fabric further. Not apparel brands, not retail, not the export garment chain.
- **Channel scope**: direct ex-factory sale, buyer arranges transport (RHP p.185). No e-commerce, no direct-to-brand contracts disclosed.
- **Price segment**: commodity/mass-market grey fabric. Management claims 20-25% of production is "value-added" or technical-use, but this figure was extracted from management only after the analyst on the Q3FY26 call asked twice ("Sir, how much will be the value-added product?" — Concall Q3FY26, transcript pp.10-11, question restated because the first answer ducked the number), and carries no capex, no margin, and no customer detail. Treated here as unverified color, not a distinct addressable segment.
- **Inclusions**: polyester greige woven fabric from any loom technology in principle; water-jet is the technology Borana actually uses and the technology Indian industry commentary (AR MD&A, peer decks) treats as the modern/growing sub-segment.
- **Exclusions**: fibre/yarn production (POY, PFY, PTY as a standalone product), fabric processing/dyeing/printing, garmenting, and any technical-textile end-use that requires certification or capex Borana has not disclosed.

### 1B. Management's own TAM claim(s) — three distinct claims, none of them a clean Rs Cr figure for Borana's actual market

**Claim 1 (Concall Q3FY26, 27-Jan-2026, transcript p.3)**: "the outlook of India's man-made fiber sector remains structurally strong. Polyester filament yarn continuously dominates the segment, accounting to close to 80% of the total man-made fabric production in the country." No source cited (contrast with the AR/RHP, which tag D&B-sourced claims explicitly as "(Source: D&B Report)" — this one carries no tag). No growth number attached to "structurally strong." **Credibility read: BROAD** — an assertion of sector health with one unsourced share statistic, no Rs/USD figure, no date range.

**Claim 2 (Investor Presentation Q4FY26, 31-Mar-2026, "Industry Overview" slide, deck pp.19-21)**: gives two quantified figures — polyester filament YARN volume (~2.53 million tonnes 2024 to ~3.06 million tonnes 2030, ~3.2% CAGR) and Indian Home Textile industry EXPORTS (US$10.8bn 2023 to US$23.3bn 2032, 8.9% CAGR). Both are precisely numbered and sourced-looking, but neither is Borana's actual market: Borana does not sell yarn as a core product and has **zero export revenue** (AR FY2026 Note 21(2)). **Credibility read: BROAD** — specific-looking numbers, wrong scope.

**Claim 3 (AR FY2026 MD&A, "Indian Weaving Industry Structure," p.69)**: "The total fabric production from water jet looms in India is projected to grow from 12.1 billion meters in 2025 to over 18.5 billion meters by 2031." This is the only claim in the entire corpus that matches Borana's product (water-jet), geography (India) and step (fabric production, weaving) at once. It carries **no source, no citation, no methodology** — unlike the RHP's D&B-tagged figures, this AR paragraph cites nothing. **Credibility read: SPECIFIC in scope, unverifiable in reliability** — used in Section 2 as the primary top-down anchor precisely because no better-scoped alternative exists, with the caveat carried through every downstream calculation.

None of the three claims is denominated in Rupees. Management has never, across the RHP, the AR, four investor decks, and the one available concall transcript, stated a Rupee-crore addressable-market size for its own actual product. That absence is itself the Section 1B finding, carried into `mgmt_claim_cr`/`mgmt_claim_ratio` in Section 2.

---

## SECTION 2: TAM ESTIMATION, MULTIPLE METHODS

### Method 1 — Top-down (primary method used for the headline TAM)

Cascade, each subtraction shown, all figures cross-checked against at least one source outside the RHP/AR pair:

1. Global textile market: **USD 1,210bn (2026) → USD 1,610bn (2033), 4.2% CAGR** (AR FY2026 MD&A p.68, unsourced within the AR but directionally consistent with the RHP's separately-sourced IMF/CII macro section).
2. India textile & apparel industry: **USD 223bn (FY23) → USD 350bn (FY30F)** (SANGAMIND Investor Presentation Q4FY26, "Ministry of Textiles; Media sources; NSSO data; Press Information Bureau" — an independent peer deck, not Borana's own document, corroborating the RHP's separate "USD 190bn by 2025-26" CII figure and the AR's "USD 350bn by 2030" figure).
3. Narrow to the weaving step, water-jet technology, India: **12.1 billion metres (2025) → 18.5 billion metres (2031)** — AR FY2026 MD&A p.69, unsourced (Claim 3 above). This is the narrowest, best-scoped volume figure available and is used as the TAM base.
   - Implied CAGR: (18.5/12.1)^(1/6) − 1 = **7.3%** (calculated here; not stated in the source).
4. No further product-mix subtraction (e.g., isolating polyester specifically from other synthetic fibres run on water-jet looms) is applied. Water-jet looms require filament (synthetic) yarn by design, and Borana's own concall claims ~80% PFY dominance of MMF fabric production (Claim 1) — but that figure is itself unsourced, so using it to shrink an otherwise-independent TAM number would launder one unsourced claim through another. The 12.1-18.5bn metre band is treated as already polyester-heavy by construction of the technology, with no numeric haircut applied.

**Value conversion** (Rs Cr = metres × realisation per metre; realisation anchors carried from B04):
- Conservative: Rs 11.27/metre (FY24 clean grey-fabric realisation, RHP-anchored) × 12.1bn m = **Rs 13,637 cr** (2025 TAM, conservative)
- Realistic: Rs 16.5/metre (FY25-9MFY26 blended, midpoint of Rs 15.80-17.50 range, B04) × 12.1bn m = **Rs 19,965 cr** (2025 TAM, realistic)

Per rule 6 (conservative bias), Rs 13,637 cr is carried as the primary TAM anchor into Sections 3 and 5; Rs 19,965 cr is carried as the upside case.

### Method 2 — Bottom-up (loom count × capacity × utilisation × realisation)

Addressable unit: one water-jet loom in the Surat cluster.

- Installed base: **~95,000 water-jet looms in Surat** (2026 SITEX industry profile, cited via web search of trade/industry press — a single, unverified source, the same evidentiary tier as the RHP's uncorroborated D&B competitor list; the same profile cites 6 lakh total looms of all types, 40,000 rapier, 10,000 air-jet, 1,500 velvet in the same cluster).
- Nameplate capacity per loom: **~3.1-3.28 lakh metres/year** (Borana's own disclosed rate — RHP p.166: "Each machine is designed to deliver a capacity of 900 meters per day"; cross-checked in B04 against the RHP objects-of-issue capex arithmetic).
- Utilisation: **80-85%** (Borana's own three-year band, RHP pp.176, 179).
- Surat-only actual output ≈ 95,000 × ~3.2 lakh × 0.80-0.85 ≈ **23.6-25.8 billion metres/year**.

This **exceeds** Method 1's all-India figure (12.1-18.5bn m). That is not resolved by averaging; it is a genuine, unresolved data-quality problem in the corpus, and is named as such: either (a) the SITEX loom count materially overstates active/comparable water-jet capacity, (b) real utilisation across the cluster is well below Borana's own 80-85% (plausible — Borana explicitly claims scale/efficiency advantages over less-integrated peers), (c) the AR's 12.1bn figure is understated or wrongly scoped, or (d) some combination. A separate independent cross-check corroborates the higher end: Surat is independently reported to produce **~6 crore (60 million) metres of fabric per day, all loom types** (web search, multiple trade sources), which annualises to **~21.9 billion metres/year for Surat alone** — closer to the Method 2 bottom-up figure than to the AR's all-India figure. **Conclusion carried forward: the AR's 12.1bn-metre figure, used as the primary TAM anchor for conservative-bias reasons, is more likely a floor than a precise estimate; Method 2 suggests the true water-jet TAM could be ~1.5-2x higher.** Stage 11 should not lean on a single point estimate from this stage.

Grossing Surat to all-India (web search: Surat variously cited as "~65% of India's man-made fibre segment" and, in the same source, "~40% of all manmade fabrics produced in India" — two different metrics, not averaged) produces an even wider, lower-confidence range (36-66bn m all-India) that is not used quantitatively here; it is noted only to show the direction of the uncertainty.

### Method 3 — Peer revenue aggregation: ATTEMPTED, ABANDONED

The RHP states explicitly: **"The Company does not have any listed industry peers in India or abroad... it is not possible to provide an industry comparison in relation to the Company."** (RHP p.129, "Comparison of Accounting Ratios with Peer Group Companies"). The RHP's own "peer benchmarking" table (p.168, D&B-sourced) lists Jindal Worldwide, Vardhman Textiles, Arvind Ltd, KPR Mill, Gokaldas Exports and Shahlon Group — all diversified, multi-segment textile companies (denim, home textile, garmenting, cotton spinning), none a grey-fabric-only weaving comparable. A spot web-check of one entry (Jindal Worldwide, independently reported FY24 revenue ~Rs 1,814 cr) does not reconcile cleanly to the RHP table's printed figure (Rs 1,86,142 cr on a literal INR-million reading of the table header) — an internal unit/scaling inconsistency in the RHP's own table that further undermines using it for aggregation. **Method 3 is not used to build the TAM number.** This is itself a finding: there is no listed pure-play to triangulate against, and the RHP's own comparison table does not survive a basic sanity check.

### Method 4 — Import substitution: NOT MEANINGFULLY APPLICABLE

India is a large net producer/exporter of woven fabric, not an importer of finished grey fabric; the import exposure in this value chain sits one step upstream, at the yarn/feedstock (POY, PTA, MEG) level, not at the fabric-production step this TAM covers. **NOT FOUND** for a finished-fabric import-substitution number; the relevant import dynamic (China POY/PFY post-BIS-QCO) is carried in Section 4 as a cost/competitive driver, not a TAM-sizing method.

### Method 5 — Global benchmark (per-capita, directional only)

India's per-capita fibre consumption is **~5.5kg**, against a global average of **~13.5kg** and developed-market levels of **20-35kg** (FILATEX Investor Presentation Q4FY26, p.23, an independent upstream peer's deck, not Borana's own document). This implies substantial long-run headroom on pure consumption catch-up, but the horizon is unstated and the metric is fibre consumption (upstream of weaving), not fabric production — used here as a qualitative growth driver (Section 4A), not converted into a Rs Cr figure, since doing so would require assumptions (catch-up speed, target year) the sources do not supply.

### Triangulation table

| Method | Estimate (2025, Rs Cr) | Confidence | Staleness | Note |
|---|---|---|---|---|
| 1. Top-down (AR water-jet volume × realisation) | 13,637 (conservative) / 19,965 (realistic) | M | Fresh (AR FY2026, but unsourced within the AR) | Primary anchor |
| 2. Bottom-up (Surat loom count × capacity) | ~26,600-42,600 for Surat alone (exceeds all-India Method 1) | L | Mixed (SITEX profile undated precisely; web-sourced) | Flags Method 1 as a likely floor |
| 3. Peer revenue aggregation | NOT USED | — | — | RHP states no listed peer exists; own table fails a sanity check |
| 4. Import substitution | NOT APPLICABLE | — | — | India is a net fabric exporter; import exposure is upstream (yarn) |
| 5. Global per-capita benchmark | Directional only, no Rs Cr | L | Fresh | Long-run headroom signal, not a TAM number |

**Conservative estimate carried forward: Rs 13,637 cr (2025). Realistic estimate: Rs 19,965 cr (2025).**

**Management's claim vs conservative estimate**: `mgmt_claim_cr` = **NOT FOUND**. Management has never stated a Rupee-denominated TAM for its actual product. The closest analogue (Claim 3, the AR's water-jet volume figure) is the same source used to build Method 1 itself, so converting it into a Rupee figure and comparing it back to Method 1 would be circular, not independent triangulation. `mgmt_claim_ratio` = **NOT FOUND** as a clean number. The qualitative finding stands in its place: of the three management claims in Section 1B, two are broad/miscoped (Claims 1 and 2) and the third is correctly scoped but entirely unsourced (Claim 3). **`mgmt_claim_read`: INFLATED** — not because a specific number is provably too large, but because every claim management does quantify (PFY 80% dominance, polyester yarn volume growth, Home Textile export growth) either lacks a source or describes a market Borana does not actually sell into (yarn export, home textile export), while the one number that WOULD matter (a Rs Cr or even a sourced metre figure for grey-fabric weaving specifically) is never given.

---

## SECTION 3: SAM & SOM

### 3A. SAM — five filters applied to TAM

| Filter | Applied? | Basis |
|---|---|---|
| Product fit | Already baked into TAM base (water-jet, synthetic fabric) | Method 1 |
| Geography | **40% multiplier applied** | Surat's share of India's man-made fabric production, web-sourced (the more conservative of two cited figures, 40% vs. 65%, per rule 6) |
| Channel | Not separately quantified | Borana sells through the same trader/processor channel dominant in Surat; no numeric filter available |
| Customer | Not separately quantified | No data splitting "open-market" buyers from vertically-integrated captive consumption (e.g., SAAM Textiles' disclosed ~90% captive processing, RHP p.162) — this would reduce SAM further but no corpus source quantifies the captive share cluster-wide. **NOT FOUND**, named rather than estimated. |
| Capability | Not separately quantified (this becomes the SOM question, Section 3B) | — |

SAM (conservative) = Rs 13,637 cr × 40% = **Rs 5,455 cr**
SAM (realistic) = Rs 19,965 cr × 40% = **Rs 7,986 cr**

**SAM as % of TAM: 40%.** This is a geography/channel proxy, not a fully filtered number — the missing captive-consumption and customer-tier filters mean SAM as computed here is likely an overstatement of what Borana can realistically transact against, but no sourced percentage exists to correct it further.

### 3B. SOM — 3 and 5 years, share-gain arithmetic shown

Current SAM share (conservative basis) = Rs 388.59 cr ÷ Rs 5,455 cr = **7.1%**.

Share-gain trajectory: Borana already executed an aggressive capacity expansion (700 → 1,212 looms in ~20 months, B04) and has committed capital to Unit 4 (192 more looms, target Dec-2026) — real, executed evidence supporting the "aggressive" 3-5pp band rather than the "normal" 1-2pp band. But the further doubling to 2,000 looms by March 2028 (Rs 350-400 cr) is **not yet funded** (cash Rs 1.68 cr vs. gross debt Rs 69.51 cr at FY26 close, no equity dilution planned — B07). A mid-aggressive **+3pp over 3 years** and top-of-band **+5pp over 5 years** are used, with the funding gap carried as an explicit condition, not assumed away.

SAM is grown forward at the Method 1 TAM CAGR (7.3%), holding the 40% SAM/TAM ratio constant:
- SAM (3yr) = 5,455 × 1.073³ = **Rs 6,740 cr**
- SAM (5yr) = 5,455 × 1.073⁵ = **Rs 7,766 cr**

SOM:
- 3yr share = 7.1% + 3pp = 10.1% → SOM (3yr) = 10.1% × 6,740 = **Rs 681 cr**
- 5yr share = 7.1% + 5pp = 12.1% → SOM (5yr) = 12.1% × 7,766 = **Rs 940 cr**

**Implied revenue CAGR** (against FY26 actual Rs 388.59 cr):
- 3yr: (681 / 388.59)^(1/3) − 1 = **20.6%**
- 5yr: (940 / 388.59)^(1/5) − 1 = **19.3%**

**This is the single most decision-relevant number this stage produces.** On the conservative TAM/SAM chain, SOM-implied revenue growth runs **20.6% (3yr) / 19.3% (5yr) — below the strategy's 25% CAGR hurdle.** Running the identical share-gain arithmetic off the realistic TAM/SAM chain (Rs 7,986 cr SAM base, same +3pp/+5pp) gives SOM (3yr) ≈ Rs 780 cr, SOM (5yr) ≈ Rs 1,126 cr, and implied CAGR of **26.2% (3yr) / 23.7% (5yr) — which does clear the hurdle.** The market-size and share-gain uncertainty in this niche (Section 2) is wide enough that whether Borana's realistic growth path clears or misses the 25% target depends on which TAM scenario is used, not on execution alone. **Stage 11 should treat 20-26% as the SOM-implied growth band, not a single number, and should weight toward the lower end given the conservative-bias convention this stage otherwise follows.**

### 3C. Capacity cross-check

Using current blended realisation (Rs 16.65/metre midpoint, FY25-9MFY26, more representative of near-term pricing than the stale FY24 Rs 11.27/metre figure used for TAM prudence):

- **SOM (3yr), Rs 681 cr ÷ Rs 16.65/m = ~409 million metres/year needed.**
  Current capacity run-rate: 1,212 looms × ~3.2 lakh m/loom nameplate × 80% utilisation ≈ 310 million m/year. Unit 4 (192 looms, target Dec-2026) adds ≈ 49 million m/year → **≈ 359 million m/year post-Unit 4**, still short of 409 million by ~50 million m/year (≈193 looms). The announced doubling plan (to 2,000 looms by March 2028) supplies this with room to spare (2,000 looms ≈ 512 million m/year at 80% utilisation).
  **3yr verdict: capacity SUFFICIENT, with margin — but only if the Rs 350-400 cr doubling capex is funded.** Against Rs 1.68 cr cash and Rs 69.51 cr gross debt at FY26 close, with no equity dilution planned (B07), **the funding plan is the optimistic side of this equation, not the market absorption assumption.** Gap named: **Rs 350-400 cr of unfunded, announced-but-uncommitted capex.**
- **SOM (5yr), Rs 940 cr ÷ Rs 16.65/m = ~565 million metres/year needed.**
  Even the full 2,000-loom plan (≈512 million m/year at 80% utilisation) falls short by ≈53 million m/year (≈207 further looms) — a THIRD phase of expansion, beyond the currently announced ceiling, that is not disclosed anywhere in the corpus.
  **5yr verdict: capacity INSUFFICIENT against the SOM figure as calculated — here the SOM assumption (a further +2pp of aggressive share gain in years 4-5) is the optimistic side, requiring capacity commitments management has not yet announced.**

---

## SECTION 4: GROWTH DRIVERS, RISKS & STRUCTURE

### 4A. TAM growth drivers

| Driver | Impact | Evidence |
|---|---|---|
| Per-capita/penetration catch-up | HIGH, long-run | India ~5.5kg fibre/capita vs global 13.5kg, developed 20-35kg (FILATEX Q4FY26 deck p.23) |
| Regulatory tailwind — PLI Scheme Round 3 | MEDIUM-HIGH | Borana itself approved (Reg 30, 1-Jul-2026, MMF Fabrics segment); 96 companies, Rs 12,822.67 cr committed investment, Rs 58,294.18 cr projected cumulative turnover industry-wide (Ministry of Textiles approval, web-sourced, June 2026) |
| China Plus One / global buyer diversification | MEDIUM, but NOT captured by Borana today | AR FY2026 MD&A cites Bangladesh political crisis as an opportunity; but Borana has zero export revenue — this driver benefits export-oriented peers (FILATEX, SANATHAN), not directly Borana, unless it starts exporting |
| Formalisation / cheaper input via BIS-QCO removal | MEDIUM, cost-side tailwind, contested | BIS QCO on polyester yarn imports withdrawn 12-Nov-2025 (Ministry of Chemicals & Fertilisers, web-sourced) — corroborated independently by FILATEX and SANATHAN peer transcripts (not Borana's own claim), lowering input yarn cost. **Correction to the injected brief: the removal date is 12-Nov-2025, not December 2025 as commonly cited.** |
| New applications / technical textiles | LOW-MEDIUM, unverified for Borana specifically | NTTM targeted $40-50bn domestic technical-textile market by 2024 (target year already passed, stale); Borana's own 20-25% "value-added" claim carries no capex/margin/customer detail (Section 1A) |
| Geographic expansion within India | LOW-MEDIUM, incremental | RHP p.181: intent to tap Bharuch, Vapi, Valsad — still Gujarat-centric, not a genuine geographic diversification |

### 4B. TAM risks

| Risk | Monitoring signal |
|---|---|
| **Import competition reversal — BIS-QCO litigation**. The QCO withdrawal (12-Nov-2025) that cheapened Borana's input yarn was **stayed by a High Court**, which "directed that the QCOs shall continue to remain in force until further orders" (web-sourced, CRISIL/press coverage). If the stay holds, the input-cost tailwind partly underlying FY26's margin gain (B04) could reverse. | Court proceedings on the QCO stay; gross margin reversion toward the Q2FY25 trough (31.7%, B04) |
| **Cluster-wide capacity race**. FILATEX's own Nov-2025 concall describes downstream weaving/knitting capacity additions being **preponed cluster-wide** ahead of a rumoured BIS-on-machinery restriction ("a lot of machines are getting put... downstream is really booming" — FILATEX Concall Nov-2025, an independent peer's own words, not Borana's). Borana is doubling capacity into the same window every other Surat weaver is also expanding into. | Cluster-wide utilisation rates, realisation trend, any reports of price competition intensifying in Surat |
| **Subsidy runoff vs. renewable delay** (company-specific, carried from B04/B07) | Unit 1 power/interest subsidy window closing 2026 vs. hybrid renewable project now on its 4th slipped date (Sep/Oct 2026 target) |
| **Utilisation ceiling** | Management's own stated ~90% max; blended utilisation already 79.6-83.8% (RHP p.176) |
| **No listed peer, no external benchmark** | RHP p.129: "does not have any listed industry peers in India or abroad" — makes any TAM figure in this stage inherently harder to independently cross-check than for a company with comparable listed peers |

### 4C. Market structure

- **Competitor count / concentration**: the RHP's own D&B report names only four competitors (SAAM Textiles, Paramount Textile Mills, Madhav Fashion, JAINCOTEX MILLS — RHP p.162), and on inspection, none is a close like-for-like comparable: SAAM is ~90% vertically-integrated/captive (RHP p.162, "90% of its mill capacity is directed to its own factories"), Paramount is export/premium-certified (GOTS, Fair Trade) fine-fabric focused, and JAINCOTEX makes embroidery YARN, not grey fabric. Only Madhav Fashion (Surat-based, embroidery/printed/plain fabrics) is loosely adjacent, and it too is a customisation/embroidery specialist, not a plain commodity-grey producer. **The competitive set genuinely mapped to Borana's exact niche (plain, unbleached, commodity polyester grey fabric, sold merchant-channel) is effectively unnamed in the corpus.**
- **Organised vs. unorganised split**: Surat cluster reported at ~10,000 weavers ranging from a few power looms to dozens of modern shuttleless looms (web search, trade press) feeding ~400-600 processing houses. No sourced organised/unorganised revenue split specific to grey-fabric weaving. **NOT FOUND** as a clean percentage.
- **Consolidating or fragmenting**: directionally fragmenting/expanding at the cluster level (see 4B, FILATEX's "preponed" capacity commentary) even as Borana's own narrative claims consolidation of scale advantage ("unmatched among the companies with a similar product focus" — Concall Q3FY26 p.3, unverified against a named comparator set, same caveat as B04).
- **Price vs. differentiation competition**: weak pricing power confirmed independently across the RHP, the AR, and the concall (B04's classification stands); capacity, delivery reliability and execution are the stated differentiators, not price or brand.
- **Import share trend**: rising at the YARN/feedstock level post-BIS-QCO removal (subject to the litigation stay above); near-zero at the finished-fabric level — India is a large net producer/exporter of fabric, not an importer of it.

---

## SECTION 5: SUMMARY & RUNWAY

### 5A. Funnel

| Layer | Conservative (Rs Cr) | Realistic (Rs Cr) |
|---|---|---|
| TAM (2025, India water-jet greige fabric) | 13,637 | 19,965 |
| SAM (× 40% Surat/Gujarat-served) | 5,455 | 7,986 |
| SOM 3yr | 681 | ~780 |
| SOM 5yr | 940 | ~1,126 |
| Current revenue (FY26) | 388.59 | 388.59 |

### 5B. Runway assessment

- **Revenue headroom** (SAM ÷ current revenue, conservative basis): 5,455 ÷ 388.59 = **14.0x**
- **TAM growth rate**: **7.3%** CAGR (2025-2031, Method 1)
- **Company CAGR vs. TAM**: Borana's revenue growth has run far above TAM growth (219.84% FY23, 47.01% FY24, and continued rapid growth through FY26, RHP p.179) — this is unambiguously **share-gain, capacity-fuelled growth, not market-riding growth**. The market itself grows at a modest, commodity-typical single-digit rate; all of Borana's outsized growth to date has come from adding looms, not from the market expanding under it.
- **Years to saturate SAM at current growth**: at FY26's revenue run-rate and a continuation of anywhere near historical growth rates, SAM saturation is a distant, low-probability event — the binding constraint is capacity and funding (Section 3C), not market absorption.

### 5C. Runway classification: **STRONG**

Reasoning (no explicit numeric matrix was supplied with this stage's instructions, so the classification logic is made explicit here): revenue headroom of 14x (conservative) to ~20.5x (realistic) is large but not extreme (>50x would be MASSIVE); TAM growth of 7.3% is real but modest, not explosive (>15% would push toward MASSIVE); the market is a fragmented commodity segment with no listed comparable and weak pricing power, which caps how much of that headroom is genuinely capturable without price concessions. STRONG, not MASSIVE or GOOD, reflects: real headroom, real (if modest) market growth, but a market structure (fragmentation, no pricing power, unverified competitive intensity) that makes the SOM trajectory genuinely uncertain rather than a high-confidence glide path.

### 5D. SAM expansion levers actually being pursued

- **Unit 4 + capacity doubling** (192 looms Dec-2026; 2,000-loom target March 2028, Rs 350-400 cr) — the only lever with real capital committed to date, and only partly funded (Section 3C).
- **Value-added/technical fabric** (claimed 20-25% of production) — unquantified in Rs Cr or margin terms; not usable as a SAM-expansion number.
- **Geographic reach beyond Gujarat** (Bharuch, Vapi, Valsad named, RHP p.181) — still intra-Gujarat, does not expand SAM beyond the 40% Surat/Gujarat filter already applied.
- **Exports** — mentioned nowhere as an active pursuit; Borana's own investor deck TAM slide (Claim 2) touts export-market growth (Home Textile, polyester yarn) it does not itself participate in. **This is the single largest unpursued SAM-expansion lever visible in the corpus** — if exercised, it would access the China-Plus-One/FTA tailwinds peers (FILATEX, SANATHAN) are already citing, but there is zero evidence Borana has begun.

### 5E. Final output card

At **20.6-26.2%** revenue CAGR implied by SOM (conservative-to-realistic TAM/SAM band), with an FY26 EBITDA margin of 23.6% (AR FY2026) sitting on a base still partly explained by two now-lapsing subsidies (B04) rather than fully by durable pricing power, the earnings growth embedded here runs **roughly in line with, to modestly below, the strategy's 25% CAGR hurdle** — the range straddles the target rather than clearing it comfortably. Whether this **supports** the current entry economics depends on (a) which TAM scenario proves closer to reality (Section 2's Method 1/Method 2 divergence is unresolved), (b) whether the Rs 350-400 cr doubling capex gets funded without diluting equity, and (c) whether the BIS-QCO litigation resolves in a way that preserves or reverses the recent input-cost tailwind. None of these three swing factors is resolved by this stage; all three are named for Section 1B (Halt 1) and Stage 11 to carry forward. Valuation/exit-multiple judgment sits entirely with Section 1B (frameworks/), per the operating rules governing this pipeline — this stage supplies the growth input only.

---

## SECTION 6: DOWNSTREAM SIGNAL CANDIDATES

| # | Candidate Signal | Entity Type | Why It Drives Demand | Likely Primary Source | Expected Cadence |
|---|---|---|---|---|---|
| 1 | Borana Industries LLP grey-fabric offtake | Counterparty | Largest single customer of grey fabric in every disclosed period FY22-9MFY25 (5.54-8.34% of grey-fabric revenue, RHP p.175); a related party with no disclosed pricing basis — demand signal AND concentration risk in one entity. **SHARED** with the B04 related-party-pricing flag. | Company RPT disclosures (AR notes, RHP related-party section) | Quarterly/Annual |
| 2 | Ministry of Textiles PLI Scheme (MMF Fabrics segment) disbursement and participant progress | Regulatory | Borana is an approved Round-3 participant (Reg 30, 1-Jul-2026); scheme-wide investment/turnover trajectory signals whether the policy tailwind is materialising or stalling industry-wide | Ministry of Textiles / PIB releases | Event-driven |
| 3 | BIS QCO litigation status (polyester yarn import certification) | Regulatory / Macro | Directly determines whether the input-cost tailwind behind recent margin gains persists or reverses; currently under a High Court stay | Ministry of Chemicals & Fertilisers notifications; court filings; CRISIL/press coverage | Event-driven |
| 4 | China POY/PFY/PTA import volumes and pricing into India | Macro | Sets the input-cost floor/ceiling for all Surat weavers, Borana included; also a proxy for competitive intensity from cheaper Chinese finished fabric | DGCI&S trade data; Ministry of Textiles | Monthly |
| 5 | Gujarat Textile Policy 2024 subsidy notifications (power/interest, per-unit 5-year window) | Regulatory | Subsidy runoff timing directly affects the margin base this SOM/CAGR estimate assumes continues; Unit 1's window closes 2026 | Gujarat Industries Commissionerate / Government of Gujarat notifications | Event-driven |
| 6 | Surat cluster weaving-capacity additions (import data for weaving machinery, HS-code level) | Macro | Proxy for whether the whole cluster is racing to add capacity into the same demand window Borana is betting on (oversupply/price-competition risk, Section 4B) | DGFT import data (weaving-machinery HS codes) | Quarterly |

`demand_externally_verifiable: true` — six candidates named, none requiring Borana's own disclosures alone.

---

## Search log

**Performed**: water jet loom market India fabric production billion meters; India synthetic grey fabric weaving market size Surat cluster crore; Surat power loom water jet loom installed base number of looms India; Surat textile number of looms lakh looms weaving cluster; Jindal Worldwide Limited revenue FY2024 crore annual; PLI scheme textiles Round 3 MMF fabrics outlay crore approved companies 2026; National Technical Textiles Mission India budget outlay crore target market size; BIS quality control order polyester yarn China withdrawn November 2025 QCO textile import.

**Skipped / blocked**: texfash.com (On the Edge: Can India's Synthetic Hub Weave Scale with Sustainability) — WebFetch blocked by network egress proxy (`EGRESS_BLOCKED`, domain texfash.com); relied on the search-snippet tier of that same query's other results instead (fibre2fashion, clothtextiles.in, apparelresources.com), each marked as trade-press/secondary tier throughout this report.

## Input gaps carried from B00

inputs/research/ empty, so no independent broker market-sizing model is available for this niche; NO-CONCALL MODE for Borana (one Q3FY26 transcript only, used above); missing Brickwork rating rationale and SEBI Section 11C(9) order text (not TAM-relevant, carried for completeness); no standalone Q1FY27 results filing; four scanned PDFs OCR'd; screener CSV export defect (not used in this stage). Additional gap surfaced by this stage: no corpus or web source gives a clean organised/unorganised split, or a captive-vs-merchant-market split, for Surat's water-jet weaving output — both would materially sharpen the SAM filter in Section 3A and are marked NOT FOUND rather than estimated.

---

```yaml
stage: B09-tam
company: "BORANA"
run_date: "2026-09-07"
model: claude-sonnet-5
status: partial
input_gaps:
  - "inputs/research/ empty; no independent broker market-sizing model for this niche (carried from B00)"
  - "NO-CONCALL MODE for Borana; one Q3FY26 transcript only (carried from B00)"
  - "No corpus or web source gives a clean organised/unorganised or captive-vs-merchant split for Surat's water-jet weaving output; both would sharpen the Section 3A SAM filter and are NOT FOUND rather than estimated"
  - "Missing Brickwork rating rationale and SEBI Section 11C(9) order text (not TAM-relevant, carried for completeness)"
flags:
  - "TAM Method 1 (AR MD&A, unsourced: 12.1bn to 18.5bn water-jet metres, India) diverges ~2x from Method 2 bottom-up (Surat loom count x nameplate x utilisation, ~23.6-25.8bn metres for Surat ALONE) - unresolved corpus data-quality problem; AR figure treated as a likely floor, not a precise estimate"
  - "Management has never stated a Rupee-crore TAM for its actual product across the RHP, AR, four investor decks and the one concall; the two claims it does quantify (PFY ~80% of MMF fabric production, unsourced; polyester-yarn and Home-Textile-export volumes) are either unsourced or scoped to markets Borana does not sell into (zero export revenue)"
  - "SOM-implied revenue CAGR runs 20.6%-26.2% depending on conservative vs realistic TAM/SAM chain - straddles, does not clearly clear, the strategy's 25% CAGR hurdle"
  - "3yr SOM is capacity-sufficient only if the announced Rs350-400cr/2000-loom doubling capex (target Mar-2028) is funded; unfunded as of FY26 close (cash Rs1.68cr vs gross debt Rs69.51cr, no equity dilution planned per B07) - the capex plan, not market absorption, is the optimistic side of the 3yr figure"
  - "5yr SOM requires loom capacity beyond even the announced 2000-loom ceiling (~207 further looms, undisclosed) - here the SOM assumption is the optimistic side, not the capex plan"
  - "BIS QCO removal on polyester yarn imports (12-Nov-2025, not December 2025 as commonly cited) was subsequently stayed by a High Court, which ordered the QCO to remain in force until further orders - live reversal risk to the input-cost tailwind behind recent margin gains, corroborated independently via FILATEX/SANATHAN peer transcripts"
  - "RHP states explicitly it has no listed industry peer in India or abroad (RHP p.129); RHP's own peer-benchmarking table (p.168) fails an independent sanity check (Jindal Worldwide entry does not reconcile to independently web-sourced FY24 revenue) - Method 3 (peer aggregation) abandoned as unreliable"
  - "RHP's D&B-commissioned industry report carried an unchanged 2025 polyester-demand projection (4mt to 6.7mt) from its October-2024 DRHP base version into the April-2025 RHP refresh despite the target year having nearly arrived - sign of recycled, not re-verified, figures in a report the issuer paid for"
market_definition: "India, weaving step only: unbleached/undyed synthetic (polyester-dominant) woven fabric sold to traders and processing houses; excludes fibre/yarn, dyeing/finishing, and garmenting steps"
tam_cr: {conservative: 13637, realistic: 19965}
sam_cr: 5455
sam_pct_of_tam: 40
som_3yr_cr: 681
som_5yr_cr: 940
som_implied_revenue_cagr: {yr3: 20.6, yr5: 19.3}
current_sam_share_pct: 7.1
revenue_headroom_x: 14.0
tam_growth_pct: 7.3
runway_class: "STRONG"
mgmt_claim_cr: "NOT FOUND"
mgmt_claim_ratio: "NOT FOUND"
mgmt_claim_read: "inflated"
capacity_check: "3yr sufficient with margin IF the Rs350-400cr/2000-loom doubling capex (Mar-2028) is funded - currently unfunded; 5yr insufficient even at the full 2000-loom plan, needs ~207 further looms beyond the announced ceiling, a third undisclosed expansion phase"
methods_used:
  - "Method 1: top-down (AR FY2026 MD&A water-jet loom fabric-production volume x Borana's own realisation)"
  - "Method 2: bottom-up (Surat water-jet loom count x nameplate capacity x utilisation) - used as a cross-check, not the primary anchor"
  - "Method 3: peer revenue aggregation - attempted, abandoned (RHP states no listed peer exists; RHP's own comparison table fails a sanity check)"
  - "Method 4: import substitution - not applicable (India is a net fabric exporter; import exposure is upstream, at yarn/feedstock level)"
  - "Method 5: global per-capita fibre-consumption benchmark - directional growth-driver only, not converted to Rs Cr"
stale_data_flags:
  - {datapoint: "India polyester demand 4mt (current) to 6.7mt (2025 target)", source: "RHP/DRHP D&B Report", year: "base report Oct-2024, unchanged in Apr-2025 RHP refresh"}
  - {datapoint: "Production of Synthetic Fabric, '000 run mt chart (FY2023-24: 123,343)", source: "RHP p.157, CMIE", year: "FY2023-24, unit ambiguous - not used in TAM math"}
searches_performed:
  - "water jet loom market India fabric production billion meters 2025 2031"
  - "India synthetic grey fabric weaving market size Surat cluster crore"
  - "Surat power loom water jet loom installed base number of looms India"
  - "Surat textile number of looms lakh looms weaving cluster 2025 2026"
  - "Jindal Worldwide Limited revenue FY2024 crore annual"
  - "PLI scheme textiles Round 3 MMF fabrics outlay crore approved companies 2026"
  - "National Technical Textiles Mission India budget outlay crore target market size"
  - "BIS quality control order polyester yarn China withdrawn November 2025 QCO textile import"
searches_skipped:
  - "WebFetch of texfash.com (On the Edge: Can India's Synthetic Hub Weave Scale with Sustainability) - blocked by network egress proxy (EGRESS_BLOCKED); relied on search-snippet tier from the same query's other results instead (fibre2fashion, clothtextiles.in, apparelresources.com)"
downstream_candidates:
  - signal: "Borana Industries LLP grey-fabric offtake"
    entity_type: "counterparty"
    demand_link: "Largest customer of grey fabric every period FY22-9MFY25; related party, no disclosed pricing basis"
    likely_source: "Company RPT disclosures (AR notes, RHP related-party section)"
    cadence: "quarterly"
    shared: true
  - signal: "Ministry of Textiles PLI Scheme (MMF Fabrics segment) disbursement/progress"
    entity_type: "regulatory"
    demand_link: "Borana is an approved Round-3 participant; scheme trajectory signals policy tailwind materialising or stalling"
    likely_source: "Ministry of Textiles / PIB releases"
    cadence: "event-driven"
    shared: false
  - signal: "BIS QCO litigation status on polyester yarn imports"
    entity_type: "regulatory"
    demand_link: "Determines whether the input-cost tailwind behind recent margin gains persists or reverses"
    likely_source: "Ministry of Chemicals & Fertilisers notifications; court filings; CRISIL/press"
    cadence: "event-driven"
    shared: false
  - signal: "China POY/PFY/PTA import volumes and pricing into India"
    entity_type: "macro"
    demand_link: "Sets input-cost floor for all Surat weavers and proxies competitive intensity from cheaper Chinese fabric"
    likely_source: "DGCI&S trade data; Ministry of Textiles"
    cadence: "monthly"
    shared: false
  - signal: "Gujarat Textile Policy 2024 subsidy notifications (power/interest, 5yr window)"
    entity_type: "regulatory"
    demand_link: "Subsidy runoff timing affects the margin base this SOM/CAGR estimate assumes continues"
    likely_source: "Gujarat Industries Commissionerate / Govt of Gujarat notifications"
    cadence: "event-driven"
    shared: false
  - signal: "Surat cluster weaving-machinery import volumes (HS-code level)"
    entity_type: "macro"
    demand_link: "Proxy for whether the whole cluster is racing to add capacity into the same demand window Borana is betting on"
    likely_source: "DGFT import data (weaving-machinery HS codes)"
    cadence: "quarterly"
    shared: false
demand_externally_verifiable: true
analyst_note: "The single biggest judgment call in this stage: which TAM scenario to trust. Method 1 (AR, unsourced) and Method 2 (bottom-up loom count) disagree by roughly 2x, and the RHP admits no listed peer exists to triangulate against. Conservative-bias convention picks the lower (AR) figure throughout, which pushes SOM-implied CAGR to 20.6%/19.3% (3yr/5yr) - below the 25% hurdle - while the realistic chain clears it at 26.2%/23.7%. Stage 11 should treat 20-26% as a band, weighted low, not a point estimate. Capacity is not the binding constraint at 3 years (sufficient with margin if funded) but funding is unresolved, and at 5 years capacity itself falls short of even the announced plan. The BIS-QCO court stay is a live, undated risk to the cost tailwind this whole margin base assumes continues."
```
