# STAGE 9 — TAM / SAM / SOM MARKET SIZING, Vinyas Innovative Technologies Ltd (VINYAS)
Run date: 2026-09-01 | Model: claude-sonnet-5 | Status: PARTIAL (two report-house full-PDF fetches blocked
by the egress proxy; equivalent data recovered via web search snippets, so triangulation is not degraded,
but direct primary-document verification of two sources — KPMG EMS opportunity report, IBEF defence
manufacturing page — was not possible this run).

CAUTION ON B04: no Business Model block (B04) exists in this run's `outputs/blocks/` folder (stage 4 was
not run, or its output was not persisted to this run folder). Scope definition below is built instead from
B03 (AR deep read), B07 (Emerging Moat scan) and this run's own read of the FY26 AR MD&A and Investor
Presentation. Flagged as `input_gaps`.

---

## SECTION 1: MARKET DEFINITION

### 1A Precise boundaries

- **Product scope (IN):** contract electronics manufacturing services — Printed Circuit Board Assembly
  (PCBA), cable harness assembly, electro-mechanical assembly, sub-system/system integration ("box-build"),
  test and after-market/lifecycle support — for defence, aerospace, medical-device, industrial and (nascent)
  transportation/rail customers (Investor Presentation, "Sectors Served" and "Program Capabilities" slides,
  pp.4, 7; AR MD&A "Business Model", p.39).
- **Product scope (OUT):** bare-board PCB fabrication (Vinyas assembles, does not fabricate raw boards);
  semiconductor/component design or fabrication; owned-IP product sales (management is explicit Vinyas
  does not own the IP on most programmes — "we don't have an engineering [development] side… we are
  predominantly a production engineering strength", cited in B07 Section 3, A2); consumer-electronics EMS
  (mobile phones, appliances) — different customer/price segment, not served by Vinyas.
- **Geographic scope:** India-manufactured, sold domestically and exported (management claims ~50% export
  mix at Jun-2026 concall, but this is **not corroborated** by AR Note 34, which states a single
  geographical segment with no export split disclosed — B07 flag, carried forward here as a scope caveat,
  not resolved).
- **Customer scope:** DPSUs, private defence primes, foreign OEM/Tier-1 defence and aerospace primes,
  medical-device OEMs (e.g. Fresenius Kabi), industrial OEMs. Excludes large DPSUs' own in-house electronics
  production (BEL, HAL etc. self-manufacture a large share of defence electronics; this capacity is not
  "addressable" by an outsourced EMS vendor and is netted out in Method 1 below).
- **Channel scope:** direct B2B manufacturing-services contracts (build-to-print / build-to-spec), no
  distributor or retail channel.
- **Price/quality segment:** high-mix, low-to-medium-volume, high-reliability/regulated manufacturing
  (NADCAP, AS9100D, ISO13485, IATF 16949 certified) — explicitly differentiated by management from
  "low-mix, high-volume" consumer EMS (Investor Presentation p.9; B07 I2).

### 1B Management's own opportunity claim

Source: **Investor Presentation, H2 FY26 (issued 29-May-2026), "Growth Momentum Factors" slide, p.8**
(runs/vinyas-2026-09-01/inputs/presentation/Investor_Presentation_1.pdf).

Management states **"Opportunity Worth ₹10K+ Cr"** over 5 years, decomposed into six pillars (each with
a stated current order-book base):

| Pillar | 5-yr opportunity (₹ Cr) | Current order book (₹ Cr) |
|---|---|---|
| Program Pipeline | 3,000 | 793 |
| Technology Transfer Enablement | 3,000 | 45 |
| System Integration | 2,000 | 324 |
| Vertical Segment Expansions | 800 | 35 |
| Global Expansion | 800 | not stated |
| License and Certifications | 600 | 112 |
| **Total** | **10,200** | **1,309** (matches disclosed FY26-close order book) |

**Credibility read: SPECIFIC in decomposition, but not independently anchored.** Each pillar is named and
sized, which is more rigorous than a single round number, and the total reconciles arithmetically with the
disclosed order book. But no pillar cites a third-party market study, a bottoms-up unit count, or a
customer-program list — every number traces back to management's own internal estimate (safe-harbour
disclaimer on p.2 explicitly disclaims accuracy). It is also **not a TAM** in the strict sense defined
above: it reads as management's own 5-year addressable **opportunity pipeline** (closer in concept to
SAM/SOM than to total market size), which matters for how the `mgmt_claim_ratio` below should be read.
The AR's own MD&A section (pp.37-41) contains extensive qualitative market commentary (see Section 4) but
**no equivalent headline ₹ figure** — the ₹10,200 Cr number exists only in the investor deck, not the AR.

---

## SECTION 2: TAM ESTIMATION, MULTIPLE METHODS

All conversions use an assumed FX rate of **₹87/USD** (approximate current rate, stated as an assumption,
not sourced to a specific date — flag as an estimation input, not a market fact).

### Method 1 — Top-down (defence electronics, outsourcing-addressable slice)

- India Defense Electronics market: **USD 7.46 billion (2025)** → USD 11.35 billion by 2032, CAGR 6.18%
  (Fortune Business Insights, accessed 01-Sep-2026, no report date beyond "2025" cited in snippet — CURRENT).
- Cross-check: India Defense Electronics and Avionics market USD 8.4 billion (2025) → USD 17.6 billion by
  2031, CAGR 13.3% (Mobility Foresights, accessed 01-Sep-2026 — CURRENT).
- USD 7.46bn × ₹87 = **₹64,902 Cr** (total India defence-electronics market, 2025) — this figure includes
  DPSU in-house production and component/IP value that is NOT addressable by an outsourced EMS vendor like
  Vinyas.
- Outsourcing-addressable filter: private-sector share of India's defence PRODUCTION (a proxy, not a
  perfect match) reached **23.6% in FY26** (search result, "India Defence Output Hits ₹1.78 Lakh Crore in
  FY26", accessed 01-Sep-2026 — CURRENT, dated this year). Applying a conservative 15-20% outsourcing/EMS-
  addressable band (private-share proxy, deliberately held below the 23.6% headline since not all private
  production is outsourced-EMS specifically; some is DPSU-affiliated private manufacture with in-house
  electronics):
  - ₹64,902 Cr × 15% = **₹9,735 Cr**
  - ₹64,902 Cr × 20% = **₹12,980 Cr**
- **Method 1 range: ₹9,700 – ₹13,000 Cr.** Confidence: **M**. Not stale (2025-sourced).

### Method 2 — Bottom-up (not independently constructible this run)

**NOT FOUND / INDETERMINATE.** A genuine bottoms-up build (addressable programme count × average
programme value) requires a programme-level dataset (number of qualified defence/aerospace electronics
assembly programmes in India, average contract value) that is not available in this run's corpus or via
web search at this depth. Vinyas's own order book (₹1,309 Cr, 5-6 year visibility, Investor Presentation
p.4, p.6) is a bottoms-up data point for the company's own SOM, not for total-market TAM, and is used
instead in Section 3. This method is marked skipped for TAM purposes; triangulation relies on Methods 1,
3, 4 and 5.

### Method 3 — Peer revenue aggregation + unorganised-sector estimate

FY26 (year ended Mar-2026) revenue of listed India EMS/electronics peers with material defence/aerospace
exposure, sourced from `runs/vinyas-2026-09-01/inputs/screening/*-Data_Sheet.csv` (screener.in export,
FY26 = period ending 2026-03-31):

| Company | FY26 revenue (₹ Cr) | Defence/aerospace weighting used |
|---|---|---|
| Vinyas | 514.32 | 100% (subject company) |
| Astra Microwave Products | 1,162.80 | 100% (RF/microwave defence electronics, pure-play) |
| Centum Electronics | 952.75 | 100% (defence/space-concentrated EMS) |
| Cyient DLM | 1,261.49 | 100% (aerospace/defence/medical/industrial EMS mix, materially defence-exposed) |
| Avalon Technologies | 1,603.21 | 20% weighted (₹320.6 Cr) — predominantly industrial/other EMS, minority defence exposure, no filed segment split found (NOT FOUND) |
| Kaynes Technology | 3,626.05 | Excluded from narrow sum — multi-vertical (auto, industrial, semiconductor, railways, defence/aerospace/space as one of several segments); no segment revenue split found in this corpus (NOT FOUND) — listed for context only, not summed |
| Syrma SGS | 4,819.06 | Excluded from narrow sum — predominantly consumer/auto/industrial EMS, minimal defence exposure per public positioning — listed for context only |

Narrow organized-peer sum (Vinyas + Astra + Centum + CyientDLM + 20%-weighted Avalon) =
514.32 + 1,162.80 + 952.75 + 1,261.49 + 320.64 = **₹4,212 Cr**.

Unorganised-sector addition (standard 30-60% band per methodology; no independent source for India
defence-EMS specifically, held conservative):
- At 30% unorganised share of total: Total = 4,212 / 0.70 = **₹6,017 Cr**
- At 45% unorganised share of total: Total = 4,212 / 0.55 = **₹7,658 Cr**

**Method 3 range: ₹6,000 – ₹7,700 Cr.** Confidence: **M**. This method likely **understates** the true
market because it cannot capture DPSU in-house electronics production (BEL, HAL, BDL etc. self-manufacture
a large share of defence electronics and are not "peers" in a revenue sense, yet compete for the same
underlying programme value) and because Kaynes/Data Patterns/Paras Defence/MTAR Technologies-type names
with partial defence exposure are excluded for lack of segment data in this corpus (NOT FOUND).

### Method 4 — Import substitution (directional cross-check only, not a standalone TAM)

- Sixth Positive Indigenisation List, notified **August 2026**: 405 items across air/land/naval/electronics
  domains, **₹3,070 Cr estimated business potential** (search result, "India indigenises 405 Defence items
  worth Rs 3,070 crore", organiser.org / tradebrains.in, accessed 01-Sep-2026 — CURRENT, this month).
  Electronics items named include radars, sonars, fire-control systems, satcom — directly in Vinyas's
  programme-capability list (Investor Presentation p.7) — but this figure covers ALL 405 items across ALL
  domains, not electronics alone, and is one indigenisation TRANCHE, not the full addressable market.
  **Directional use only — not summed into the TAM triangulation table.**
- Broader directional figure: domestic defence market projected to expand to **₹10,00,000 Cr (~USD 122
  billion) over the next 20 years** (search result citing IBEF, accessed 01-Sep-2026). This is a 20-year
  horizon figure with no interim milestone stated — **per the staleness/scope discipline, this informs
  DIRECTION ONLY** (long-run indigenisation tailwind is real and government-stated) and is explicitly
  excluded from the headline TAM number.

### Method 5 — Global benchmark

- Global Aerospace & Defense Electronic Manufacturing Services market: **USD 23.98 billion (2025)** →
  USD 33.47 billion by 2035, CAGR 3.44% (SNS Insider, accessed 01-Sep-2026 — CURRENT).
- India's overall EMS industry currently holds roughly **4-5% of global EMS market share** (search result
  context, accessed 01-Sep-2026). Applying this same overall-EMS penetration rate to the narrower global
  A&D EMS market (a benchmark, not a claim India has actually reached this share in A&D specifically — its
  actual current global A&D EMS share is almost certainly far lower, since Vinyas's own export base implies
  only tens of crores of actual global A&D revenue against a USD 24bn market):
  - USD 23.98bn × 4.5% = USD 1.079bn × ₹87 = **≈₹9,390 Cr**
- **Method 5: ≈₹9,400 Cr** if India's global A&D EMS penetration converges toward its broader EMS
  penetration rate. Confidence: **L** (convergence assumption is speculative, not evidenced; used only as
  a cross-check that Method 1's top-down range is directionally plausible, not as an independent anchor).

### Triangulation table

| Method | Estimate (₹ Cr) | Confidence | Staleness |
|---|---|---|---|
| 1 — Top-down (defence electronics, EMS-addressable) | 9,700 – 13,000 | M | Current (2025-sourced) |
| 2 — Bottom-up | NOT FOUND / skipped | — | — |
| 3 — Peer aggregation + unorganised | 6,000 – 7,700 | M | Current (FY26 filed peer data) |
| 4 — Import substitution | Directional only, not summed | L | Current but partial-scope |
| 5 — Global benchmark | ≈9,400 | L | Current (2025-sourced) |

**Conservative estimate: ₹6,000 Cr** (Method 3 lower bound — the most conservative anchored figure,
per the CONSERVATIVE BIAS instruction).
**Realistic estimate: ₹9,500 Cr** (Method 1 midpoint, corroborated by Method 5's independent convergence
check landing at almost the same number — two different methods arriving near ₹9,400-9,700 Cr is the
strongest cross-validation in this analysis).

**Management's claim vs conservative estimate:** ₹10,200 Cr ÷ ₹6,000 Cr = **1.70x**. Per the standard read
(>2x likely inflated, within 1.5x reasonable), 1.70x sits **between the two bands** — above "reasonable"
but below the "likely inflated" threshold. Read as **reasonable, at the high end, flagged**: management's
5-year "opportunity" figure is plausible in magnitude against an independently triangulated TAM, but it is
a company-specific pipeline estimate, not a market TAM, and rests entirely on unaudited internal sizing
(safe-harbour disclaimer). Notably, against the REALISTIC estimate (₹9,500 Cr) the ratio falls to 1.07x —
comfortably reasonable — so the classification is sensitive to which anchor is used; the ratio field below
uses the conservative anchor per the field's own definition.

---

## SECTION 3: SAM & SOM

### 3A SAM — five filters applied to TAM (conservative, ₹6,000 Cr)

| Filter | Retained % | Rationale |
|---|---|---|
| Product fit | 80% | Excludes bare-board fabrication, owned-IP systems and semiconductor-level work Vinyas does not perform (B07 A2: "we don't have an engineering [development] side"). |
| Geography | 90% | Vinyas's current qualified footprint is India-manufactured with limited direct Europe/US customer-site presence (US subsidiary incorporated Feb-2026, non-operating at FY26-close per B03); excludes the portion of the market requiring an established local qualification history in those geographies. |
| Channel | 95% | B2B direct-manufacturing-services model matches almost the entire TAM as defined; minimal channel-mismatch loss. |
| Customer | 100% | No further cut — the outsourcing-addressable filter in Method 1 and the peer-set definition in Method 3 already exclude DPSU in-house customers from the TAM base. |
| Capability | 70% | NADCAP + AS9100D + ISO13485 gate access to only a subset of programmes; current utilisation (~35-40%, per B07 2B) and unresolved cash-conversion (Gate 0 dominant flag) constrain how much of the certified-addressable space Vinyas can credibly serve near-term. |

SAM = 6,000 × 0.80 × 0.90 × 0.95 × 1.00 × 0.70 = **₹2,873 Cr**.
**SAM as % of TAM (conservative) = 2,873 / 6,000 = 47.9% ≈ 48%.**

### 3B SOM at 3 and 5 years

- Current share of SAM = 514.32 / 2,873 = **17.9%** (current_sam_share_pct). This is a high starting share
  for a "TAM/SAM" framing, but plausible given the SAM is itself a narrow, qualification-gated niche where
  management states Vinyas is one of only "2-3" NADCAP-electronics-accredited companies in India (B07 A1,
  concall-sourced, unverified against a filing).
- Share-gain trajectory: capacity is doubling (SMT expansion; capex-embedded growth +69% per B07/B00
  injected figure) and the NADCAP/AS9100D bundle is a real qualification barrier — this supports the
  **aggressive** band (3-5pp gain in 3 years) rather than the normal 1-2pp band, tempered downward from the
  top of that band by the unresolved Gate 0 cash-conversion flag (receivable days 33→161, negative
  cumulative CFO/PAT), which caps how much execution credit this run extends.
  - 3-year share gain: **+4.0pp** → 17.9% + 4.0pp = **21.9%**
  - 5-year share gain: **+7.0pp** cumulative (a further +3.0pp in years 4-5, decelerating as the SAM's
    qualification-gated ceiling is approached) → **24.9%**
- **SOM_3yr = 2,873 × 21.9% = ₹629 Cr.**
- **SOM_5yr = 2,873 × 24.9% = ₹716 Cr.**
- **Implied revenue CAGR, shown arithmetic:**
  - Yr3: (629 / 514.32)^(1/3) − 1 = (1.2231)^(0.333) − 1 = **6.95% CAGR**
  - Yr5: (716 / 514.32)^(1/5) − 1 = (1.3921)^(0.2) − 1 = **6.84% CAGR**

**This is the single most important finding in this stage.** The SOM-implied CAGR (≈7%) is dramatically
below the FY26 actual growth rate (29.67%, AR Financial Highlights p.42) and below management's own guided
30-35% growth band (Investor Presentation p.5). Three explanations, none of which this run's corpus can
resolve definitively:
1. The TAM/SAM constructed here is genuinely too narrow — most plausibly because it is anchored to
   **India-domestic** defence electronics data (Method 1), while Vinyas's own management claims ~50% export
   revenue (unverified per AR Note 34). If that export claim is real, Vinyas already operates partly inside
   the far larger **global** A&D EMS market (~USD 24bn / ≈₹2,08,800 Cr, Method 5's raw figure before the
   India-share discount), which would support materially higher achievable growth without breaking the
   standard share-gain rules. This cannot be incorporated into the anchored SOM number because the
   underlying export-mix claim is itself flagged unresolved (B07).
2. Management's growth guidance assumes share gains beyond the "aggressive" 3-5pp/3yr band used here —
   which the framework reserves for competitor exit or acquisition, neither of which is evidenced.
3. FY26's 29.67% growth may partly reflect one-off programme timing (defence order lumpiness, named by
   management itself as the primary risk) rather than a sustainable run-rate.

This divergence is carried forward explicitly as the FORMAL handoff to Stage 11 (below), which should treat
the SOM-implied CAGR (~7%) as the market-sizing-anchored floor and management's 30-35% guidance as the
claim to be tested, not assumed.

### 3C Capacity cross-check

Using the injected `capex_embedded_growth_pct = 69%` (B07-emoat, Method 1, fixed-asset-turnover-based,
the more conservative of B07's two methods):
- Capacity-supportable revenue ceiling = 514.32 × 1.69 = **≈₹869 Cr**.
- Management's own capacity-ceiling math (B07, cross-check only): **₹2,000-2,100 Cr** post-expansion
  ceiling.

Both figures **comfortably exceed** SOM_3yr (₹629 Cr) and SOM_5yr (₹716 Cr). **Capacity check: SUFFICIENT.**
The gap identified in 3B is not a capacity constraint — physical capacity is not the binding limit even
under the conservative +69% method, let alone management's ₹2,000-2,100 Cr ceiling. **The optimistic side
of the divergence is the demand/market-share assumption (SOM growth), not the capex plan.** If Vinyas
genuinely captures management's 30-35% growth guidance, capacity would not bind; the open question this
stage raises is whether the addressable market, as independently sized here, can support that share gain.

---

## SECTION 4: GROWTH DRIVERS, RISKS & STRUCTURE

### 4A TAM growth drivers

| Driver | Impact | Evidence |
|---|---|---|
| Regulatory tailwind (Make-in-India, offset obligations, Positive Indigenisation Lists) | Strong | 6th Positive Indigenisation List, Aug-2026, 405 items/₹3,070 Cr (search); AR MD&A "Government's continued emphasis on Make in India... has created significant opportunities" p.37 |
| Import substitution | Strong | Foreign defence procurement share reportedly fallen to ~12% (search, accessed 01-Sep-2026, directional); private-sector share of defence production 23.6% FY26 (search) |
| New applications (NADCAP-unlocked civil aerospace + export-controlled defence) | Moderate-Strong | NADCAP AC7120 achieved H1FY26 (B07 A1); 18-24 month qualification gestation per programme |
| Geographic/China+1 diversification | Strong | Medical-device order explicitly framed as China+1 by management (B07 E2); AR MD&A "China+1 sourcing strategy... continued to create opportunities for emerging manufacturing destinations, particularly India" p.37 |
| Formalisation (private-sector share of defence production rising) | Moderate | Private share 23.6% of FY26 defence output (search) — directional, not electronics-specific |
| Technology enablement (traceability/digitisation raising qualification bar and value capture) | Moderate | Manufacturing-floor digitisation 80-85%, targeting 95%+ (B07 A3) |
| Premiumisation (mix shift PCBA → box-build/system integration) | Moderate | Gross-margin expansion path tied to system-integration mix (B07 1A); AR "Objectives" p.5 names System Integration explicitly |
| Demographics / per-capita | N/A | Not a relevant driver for a B2B defence/aerospace EMS TAM |

### 4B TAM risks

| Risk | Monitoring signal |
|---|---|
| Regulatory/programme push-out | Any disclosed programme delay or defence budget-cycle slippage (management's own named top risk, B07 6B) |
| Cyclical/lumpy defence capex | Quarter-to-quarter order and revenue volatility; H1 vs H2 growth divergence already visible in FY26 |
| Import competition / vertical integration by primes | Global A&D primes reducing outsourced-EMS spend by insourcing |
| Capacity/qualification saturation at the top tier | A well-funded competitor completing the ~2-year NADCAP cycle (B07 6B) |
| Substitution (DPSU in-house re-insourcing) | Any BEL/HAL/BDL capacity-expansion announcement in SMT/PCBA assembly |
| Geopolitical/supply-chain concentration | Israel-linked supply exposure (10-15% of supplies per B07 E2) already caused one receivable spike; further disruption |

### 4C Market structure

- **Competitor count:** narrow at the NADCAP-accredited top tier — "hardly a little over 30 companies"
  globally, "2-3... on the electronic side" in India per management (B07 A1, concall-sourced, **not
  independently verified in this corpus** — flag). Broader listed peer set: Astra Microwave, Centum,
  CyientDLM, Avalon, Kaynes (diversified), plus unlisted names (Data Patterns, Paras Defence, MTAR
  Technologies) whose financials are **NOT FOUND** in this run's screening folder.
- **Top-3 concentration:** NOT FOUND — no independent revenue-share data for the India defence/aerospace-
  EMS sub-segment specifically.
- **Organised vs unorganised split:** 30-60% unorganised assumed per standard methodology (Method 3);
  **no independent source for this segment specifically** — estimate only.
- **Consolidating or fragmenting:** directionally consolidating at the qualification-gated top tier
  (NADCAP/AS9100D raise entry cost), fragmenting at the entry/lower-qualification tier — inference (🔍),
  not independently sourced.
- **Price vs differentiation competition:** differentiation-led — sole-vendor/single-tender status on
  select programmes (B07 B2), not price competition.
- **Entries/exits:** NOT FOUND — no named competitor entry or exit event in this run's corpus or search.
- **Import share trend:** declining (indigenisation/import-substitution tailwind), though the "foreign
  procurement fallen to ~12%" figure is a **total defence acquisition** statistic, not electronics-specific
  — flagged as a scope caveat.

---

## SECTION 5: SUMMARY & RUNWAY

### 5A Funnel

```
TAM (conservative)  ₹6,000 Cr   ─┐  (Method 3: peer aggregation + unorganised estimate)
TAM (realistic)      ₹9,500 Cr   │  (Method 1/5: top-down defence-electronics-EMS slice, cross-checked
                                  │   by global-benchmark convergence)
        ↓  five filters (80% × 90% × 95% × 100% × 70%)
SAM                  ₹2,873 Cr   (48% of TAM conservative)
        ↓  current share 17.9%
Current revenue       ₹514 Cr    (FY26 actual, AR Financial Highlights p.42)
        ↓  +4.0pp (3yr) / +7.0pp (5yr) share gain
SOM (3yr)             ₹629 Cr    (implied CAGR 6.95%)
SOM (5yr)             ₹716 Cr    (implied CAGR 6.84%)
```

### 5B Runway assessment

- **Revenue headroom** = SAM ÷ current revenue = 2,873 / 514.32 = **5.59x**.
- **TAM growth rate** ≈ 6.18-13.3% (Method 1 sources), blended midpoint used: **≈9.7%**.
- **Company CAGR vs TAM:** FY24→FY26 revenue CAGR = (514.32/317.20)^(1/2) − 1 = **27.3%**, roughly 2.8-4.4x
  the TAM's own growth rate. Vinyas is **gaining share**, not merely riding the market — consistent with
  the current 17.9% SAM share already computed above.
- **Years to saturate SAM at current growth:** at the 27.3% historical CAGR, ln(2,873/514.32)/ln(1.273) =
  **≈7.2 years**; at management's guided 30-35% growth, **≈5.5-6.5 years**. Either way, SAM saturation
  falls within or just beyond a 3-5 year hold horizon if growth continues anywhere near its recent pace —
  a meaningful constraint for a strategy built on sustained 25% CAGR.

### 5C Runway classification: **MODERATE**

Headroom (5.6x) looks respectable in isolation, but two factors pull the classification down from
GOOD/STRONG: (i) the underlying TAM itself grows slowly (high single digits), so nearly all of Vinyas's
historical outperformance has been share-gain-driven, which is inherently harder to sustain and more
competitively contested than market-growth-driven expansion; (ii) the SOM-implied CAGR under standard
share-gain rules (≈7%) sits far below both FY26 actual growth and management's guidance, and SAM
saturation is plausible within 5-7 years at anything like the company's recent growth rate. Capacity is not
the constraint (3C); the market-sizing discipline applied here is.

### 5D SAM expansion levers actually being pursued

| Lever | Evidence | Potential SAM addition | Status |
|---|---|---|---|
| Global expansion (US subsidiary, Europe) | US subsidiary incorporated Feb-2026, non-operating at FY26-close (B03); two shortlisted US opportunities, no order (B07 H2) | Could open access to the much larger global A&D EMS TAM (~₹2,08,800 Cr raw, Method 5) beyond the India-anchored SAM modelled here — unquantifiable without a revenue base; NOT FOUND for magnitude | Early-stage, unproven in revenue |
| Technology transfer / licensed manufacturing | Management pillar valued at ₹3,000 Cr/5yr (Investor Presentation p.8) | Structural move up the value chain (from build-to-print toward owned/licensed IP) — could re-rate margin/moat, not sized independently here | Concall/deck-level claim only |
| Vertical segment expansion (medical, rail) | Management pillar valued at ₹800 Cr/5yr | Likely already substantially captured inside the base TAM/SAM (medical and industrial customers are IN the market definition in 1A) — flagged as a probable **double-count risk** if added on top of the SAM above, not a clean addition | Partially captured already |

Revised headroom if global expansion executes even modestly (illustrative only, not anchored): SAM could
plausibly approach ₹5,700-6,000 Cr, lifting headroom toward ~11x — but this depends entirely on unproven,
concall-only claims (Israeli JV, US subsidiary) and is not carried into the anchored fields below.

### 5E Final output card

- TAM (conservative / realistic): **₹6,000 Cr / ₹9,500 Cr**
- SAM: **₹2,873 Cr** (48% of conservative TAM)
- SOM 3yr / 5yr: **₹629 Cr / ₹716 Cr**
- SOM-implied revenue CAGR: **6.95% (3yr) / 6.84% (5yr)**
- Revenue headroom: **5.6x**
- Runway class: **MODERATE**
- Management claim ₹10,200 Cr vs conservative TAM: **1.70x — reasonable, flagged at the high end**

**Valuation implication line:** At **6.9-7.0%** revenue CAGR implied by SOM, with a margin trajectory of
**~11-12.5%** EBITDA (FY26 actual 12.50%, FY27 guided 11-12% per B07 2B — i.e., flat-to-slightly-declining,
not expanding), the earnings growth embedded here is roughly **high-single-digit CAGR**, which **does not
support** the current valuation of **≈63x P/E** (CMP ₹1,546 ÷ FY26 diluted EPS ₹24.53, both from the
Investor Presentation Income Statement, p.11; market cap ₹1,945 Cr ÷ FY26 PAT ₹30.87 Cr gives the same
≈63.0x). A PEG built on the SOM-anchored earnings-growth path would sit at roughly 8-9x — far outside any
GARP discipline. The valuation is currently priced for something much closer to management's 30-35%
guidance sustaining for years, not for the market-sizing-anchored floor this stage computes. This is the
central tension Stage 11 must resolve: either the export/global-market thesis (unverified per AR Note 34)
is real and materially expands the addressable market beyond what this India-anchored analysis captures, or
the current multiple is pricing growth this stage's independent triangulation cannot support.

---

## SECTION 6: DOWNSTREAM SIGNAL CANDIDATES

| # | Candidate Signal | Entity Type | Why It Drives Demand | Likely Primary Source | Expected Cadence |
|---|---|---|---|---|---|
| 1 | Positive Indigenisation List updates (MoD/Dept. of Defence Production) | Regulatory | Each list directly enumerates electronics items (radars, sonars, fire-control, satcom) that must be indigenised, creating a defined, dated demand pool matching Vinyas's programme capabilities | Ministry of Defence / Department of Defence Production press releases, PIB | Event-driven |
| 2 | Union Budget defence capital outlay | Macro | Top-down funding envelope for the entire defence electronics TAM; year-on-year capital allocation directly sets programme demand | Union Budget documents (Ministry of Finance), Ministry of Defence Annual Report | Annual (February) |
| 3 | NADCAP/PRI accreditation status (own and competitor) | Regulatory | Gates access to the qualified-vendor pool for defence-grade and export-controlled electronics assembly across all four verticals (defence, aerospace, medical, industrial) | PRI eAuditNet / Nadcap accredited-supplier public database | Event-driven (audit cycle, ~annual/biennial) |
| 4 | Global A&D Tier-1 OEMs / defence primes (foreign OEM qualification, Israeli JV partner) | End-customer / Counterparty | Direct source of the "Program Pipeline" and "Global Expansion" opportunity pillars; qualification and first-order events are the single largest catalysts named in B07 | Company exchange filings (order announcements), OEM/prime investor disclosures | Event-driven |
| 5 | Medical-device OEM localisation announcements (e.g. Fresenius Kabi-type customers) | End-customer | Direct China+1/Make-in-India localisation demand driver for the medical vertical | Customer investor disclosures; DGCI&S import-export trade data | Quarterly |
| 6 | Independent EMS/A&D market trackers (Mordor Intelligence, Fortune Business Insights, SNS Insider et al.) | Macro | External, third-party confirmation or revision of the TAM growth-rate assumptions used throughout this stage | Named market-research publishers (per Downstream Source Discovery Protocol registry) | Event-driven (annual report refresh) |

Shared dependencies: Rows 1 and 2 (MoD indigenisation policy and Budget outlay) are correlated — both flow
from the same underlying government defence-spending decision and should be counted once by FTTCP. Row 3
(NADCAP) is SHARED across defence, aerospace and medical verticals, since it gates all three simultaneously.

`demand_externally_verifiable: true` (6 candidates, above the 3-row minimum).

---

## SEARCH LOG

**Searches performed:**
1. "India defence electronics manufacturing market size 2026 crore"
2. "India Electronics Manufacturing Services EMS market size CRISIL ICRA 2026"
3. "India defence indigenisation electronics offset market crore 2026 2030 target"
4. "global aerospace electronics manufacturing services market size 2026 billion"
5. "India defence PCB assembly outsourcing market NADCAP accredited companies"

**Searches/fetches skipped or blocked:**
- WebFetch of `assets.kpmg.com/.../indias-electronic-manufacturing-services-ems-opportunity.pdf` — blocked
  by the egress proxy (EGRESS_BLOCKED). Equivalent EMS market-size figures were recovered via the WebSearch
  snippet for the same report (India EMS market "may cross USD 150 billion by FY30" per KPMG, thestatesman.com
  summary), but the full report's segment breakdown (if any, by defence/aerospace vs consumer EMS) was not
  independently read.
- WebFetch of `www.ibef.org/industry/defence-manufacturing` — blocked by the egress proxy. The ₹10,00,000 Cr
  /20-year figure and other IBEF context were recovered only via WebSearch snippets, not the primary page;
  used for direction only, as noted in Method 4, per this stage's own staleness/scope discipline.

Per the stage's operating rule, these two blocked fetches are recorded as skips; `status: partial` is set
accordingly, though the triangulation itself rests on five independently sourced methods and is not judged
materially weakened by the two blocked full-document reads.

---

## ANALYST NOTE

The load-bearing finding of this stage is the divergence between the SOM-implied CAGR (~7%, standard
share-gain rules against an independently triangulated SAM) and both FY26 actual growth (29.67%) and
management's guidance (30-35%). This is not resolved here — it hinges on the unverified ~50% export-mix
claim (B07 flag, contradicted by AR Note 34's single-segment disclosure). If Stage 11/FTTCP obtains
independent evidence the export mix is real and growing, the true addressable market is closer to the
global A&D EMS TAM (~₹2,08,800 Cr raw), which would materially loosen this stage's MODERATE runway
classification. Absent that evidence, treat the SOM-anchored ~7% CAGR as the floor case and management's
30-35% as the claim under test, not the base case.
