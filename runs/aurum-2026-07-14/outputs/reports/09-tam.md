# Stage 9 — TAM / SAM / SOM Market Sizing: Aurum Proptech Ltd (AURUM)
Run date: 2026-07-14 | Model: claude-sonnet-5

FX assumption used throughout for USD-denominated figures: ₹95/USD (Federal
Reserve H.10, spot 13-Jul-2026 ≈95.8, July-2026 average ≈95.37; web search,
2026-07-14). Any USD figure converted at this rate is marked "(FX@95)".

Aurum operates three structurally distinct revenue engines addressing three
different markets (per B04-bizmodel: Rental 63.9% / Distribution 30.1% /
Capital 6.0% of FY25 ₹263.84 Cr revenue). Per task instruction, each is
sized separately below and then aggregated — no single blended TAM is used.

---

## SECTION 1: MARKET DEFINITION

### 1A. Precise boundaries

**Product scope (three engines, each with a different revenue-recognition model — B04-anchored):**
- **RENTAL** — HelloWorld (co-living operator; leases the asset, recognises
  full rent as revenue) + NestAway (managed-rental marketplace; recognises
  a % commission of rent, ~10% from landlord + ~5% from tenant blended,
  Investor Presentation Q2 FY26 slide 13, per B04 unit_economics).
- **DISTRIBUTION** — Aurum Analytica (AI/data lead-generation for
  developers) + Sell.do (real-estate CRM SaaS, license/annuity revenue) +
  PropTiger (primary residential sales brokerage, commission on
  transaction value).
- **CAPITAL** — AMSA SM-REIT (SEBI-registered, asset-management-fee model
  on AUM) + legacy Integrow/WiseX AIF vehicles (nascent, B04 flags as
  unmonetised/low-predictability).

**Geographic scope:** India only; no international operations found in any
injected document. Within India, Aurum's own footprint is ~15 cities (AR
FY24-25, p.49 text), concentrated in the metros that independent sources
say dominate demand (Colliers 2025: "bulk of [co-living] demand is from
Top-8 cities, ~70%+"; CBRE 2024/2025: SM-REIT-eligible office stock
concentrated in Mumbai/NCR/Bengaluru/Hyderabad).

**Customer scope:** Rental = individual renters/tenants + property owners
(C2C/B2C); Distribution = real-estate developers, RERA channel
partners/brokers, homebuyers (B2B + B2B2C); Capital = retail + HNI/family-
office/institutional investors in fractional commercial real estate
(B2C/B2B2C).

**Channel scope:** owned digital platforms/apps, not physical brokerage
network ownership (PropTiger retains an on-ground sales element).

**Price segment:** Rental = mass/mid-market urban (students, young
professionals, families); Distribution = spans developer tiers, revenue
likely skews to larger branded developers; Capital = SEBI SM-REIT minimum
ticket size ₹10 lakh (post the 2024 SEBI amendment; Dolat Capital note,
non-anchored, but consistent with the SEBI regulatory description in AR
p.30-31 text).

**Explicit exclusions:** new-construction/EPC; real-estate ownership as a
core business (Aurum is explicitly exiting non-core owned real estate —
the Q5/Q6 Navi Mumbai building sale, completed May-2026, OPERATOR_CONTEXT
item 3); pure content/listing aggregators like 99acres/Housing.com/NoBroker
(named only in the non-anchored Dolat broker note as competitors, not as
Aurum businesses); secondary/resale residential brokerage as a scaled,
sized business (NestAway "successfully entered the resale segment" per AR,
but this is not yet separately sized anywhere in the injected documents —
data gap, noted in Section 5D).

### 1B. Management's own TAM claims (held for Section 2 comparison)

| Segment | Management claim | Date/source | Credibility read |
|---|---|---|---|
| Distribution | "A ₹39,000 crore Opportunity" — annual spend on RE distribution: ₹1,000 Cr aggregator websites + ₹4,000 Cr social media + ₹34,000 Cr channel sales | AR FY24-25 MD&A, p.16-17 (published ~2025, <2yrs old at run date) | **Specific** — three named, summed line items |
| Capital | "₹50,000 crore+ Estimated SM-REITable commercial supply by FY 2026 across India" | AR FY24-25, p.19 | **Specific but narrow** — reads as near-term listing-ready supply, not full eligible stock (see Section 2 divergence vs CBRE) |
| Rental | No single ₹-crore TAM figure; structural stats only: "over 2 Crore rental consumers," "organized rental supply remains limited to just 8 lakh units," "25-fold mismatch" | AR FY24-25, p.49 | **Broad/directional** — unit counts, not a revenue TAM |
| Sector-level (context, not Aurum-specific) | "India's PropTech landscape... could scale into a USD 100 billion [market] by 2030" | AR FY24-25, p.47-48, citing an unnamed external report | **Broad** — round number, no methodology shown in the extracted text |
| Sector-level (context) | Global PropTech "USD 41.78 Bn (2024) → USD 140.67 Bn (2034), 11.8% CAGR" | AR FY24-25, p.46-47 | **Broad**, not India-specific, not usable for India TAM |

Management makes no single consolidated "Aurum TAM" claim — it gives
segment-specific opportunity figures for Distribution and Capital only,
consistent with the task's instruction to size each engine separately
rather than blend.

---

## SECTION 2: TAM ESTIMATION, MULTIPLE METHODS

### 2.1 RENTAL

**Method 1 — Top-down, subtractive.** India's total rental-housing market
is sized at USD 20.29–20.31 Bn (2024) by aggregator research houses
(TechSci Research / Grand View Research summaries via web search,
2026-07-14; specific primary report not independently retrievable, **M**
confidence) = ₹1,92,850 Cr (FX@95). This is the *gross* rental market
(overwhelmingly informal, individual-landlord). Aurum's product only
addresses the *organized/managed* slice. AR FY24-25 (p.49) discloses the
organized-penetration ratio directly: "over 2 Crore rental consumers"
against "organized rental supply... just 8 lakh units" → organized
penetration = 8,00,000 / 2,00,00,000 = **4.0%** (AR-anchored ratio, applied
to the gross market value as the subtraction basis — this likely
*understates* true organized GMV since managed stock typically commands a
rent premium over informal stock; no anchored premium % was found to
correct for this, so the resulting figure is treated as conservative).
Organized/managed rental GMV ≈ ₹1,92,850 Cr × 4.0% = **₹7,714 Cr**.

Splitting this GMV between the two revenue models in Rental:
- Co-living (HelloWorld, full-rent revenue recognition): Colliers India
  (May-2025 report, via web search) sizes the *organized* co-living market
  at **₹4,000 Cr** in 2025, "Top-30 cities," with stock of 0.3 Mn beds
  against demand of 6.6 Mn beds (5% penetration, 2025), and projects the
  market to reach ₹20,600 Cr by 2030 (implied CAGR: (20,600/4,000)^(1/5)−1
  ≈ **38.8%**). **H confidence, fresh (2025), specific methodology
  (bed-count based).**
- Remaining organized GMV (non-co-living, family/individual managed
  rental — NestAway's addressable pool) = ₹7,714 Cr − ₹4,000 Cr = ₹3,714
  Cr. NestAway earns commission only (~10% landlord + ~5% tenant blended =
  15%, B04-anchored), so its revenue-equivalent TAM = ₹3,714 Cr × 15% =
  **₹557 Cr**.

**Rental TAM (Method 1, bottom-up-blended revenue-equivalent) = ₹4,000 Cr
+ ₹557 Cr = ₹4,557 Cr** (2025 basis).

**Method 2 — Bottom-up unit economics, full-penetration sanity check.**
Using Colliers' own 2025 data pair (₹4,000 Cr market ÷ 0.3 Mn beds stock =
₹1,33,333 realization/bed/year) applied to the FULL stated co-living
*demand* of 6.6 Mn beds gives a full-penetration ceiling of ≈ **₹88,000
Cr**. This is not used as the headline TAM — it assumes 100% of latent
"demand" beds convert to paid co-living at today's realization, which
overstates near-term reality (much of that demand would default to
informal rental, not co-living, if not served) — shown only as the outer
bound / long-run direction, per the CONSERVATIVE BIAS rule.

**Method 3 — Peer aggregation (directional only, flagged unreliable).**
Dolat Capital's (non-anchored, dated May-2024, >2 yrs old = **STALE**)
capacity table shows Stanza Living 70,000 beds / ZoloStays 45,000 / Ishtara
24,000 vs HelloWorld 13,500 (Q4 FY24). Grossing these bed counts at
Dolat's own cited HelloWorld "realization per unit" (₹87,341/bed, FY24,
non-anchored) implies a peer-aggregate market of only ~₹260 Cr — an order
of magnitude below Colliers' ₹4,000 Cr, indicating the Dolat per-bed
metric and the Colliers market-value figure are not measuring the same
thing (likely different scope/definition). **Flagged as internally
inconsistent; not used to build the headline TAM, kept only as a
qualitative competitor-scale reference.**

**Divergence flag:** other secondary web sources cite wildly different
co-living market sizes for essentially the same year — JLL India "USD 6–7
Bn by 2025" (≈₹5.7–6.7 lakh Cr, FX@95) and Cushman & Wakefield "USD 40 Bn
by 2025" (≈₹38 lakh Cr) — both **14x to 90x larger** than Colliers' ₹4,000
Cr. None of these secondary citations could be traced to a retrievable
primary report in this run (only a secondary web summary), and they are
inconsistent with Aurum's own disclosed HelloWorld revenue scale (Q4 FY26
Rental total ~₹55 Cr/quarter across NestAway+HelloWorld combined — implying
Aurum, likely a top-3 organized co-living player, would hold an
implausibly small share of a ₹38–67 lakh Cr market). Colliers' figure
(specific bed-count methodology, freshest, most internally consistent with
Aurum's own scale) is used as the anchor; JLL/Cushman figures are recorded
in the stale/divergent flags below and excluded from the headline TAM.

### 2.2 DISTRIBUTION

**Method 1 — Management-disclosed, independently corroborated.**
AR FY24-25 states "A ₹39,000 crore Opportunity" (₹1,000 Cr aggregator
websites + ₹4,000 Cr social media + ₹34,000 Cr channel sales). Independent
web search corroboration: "Annual real estate marketing expenditures in
India have reached ₹38,000 crore" (Brainguru, 2026 blog summary — **weak
source quality, but close, independent, and directionally aligned within
2.6%**). Conservative figure taken: **₹38,000 Cr**.

**Method 2 — Bottom-up, primary-sales brokerage pool (PropTiger).**
AR FY24-25 discloses "₹4,00,000 crore+ Annual Value of Homes Purchased"
(p.16; scope — Top-8-cities-only vs pan-India is not explicitly stated in
the extracted text, treated as presented). Independent web search on
India primary-sales channel-partner commission rates: **1–3% of booking
value for residential** (up to 5% for commercial/luxury), multiple sources
via web search 2026-07-14. Conservative (1%) → ₹4,000 Cr; realistic
(2%, mid-range) → ₹8,000 Cr brokerage-commission-pool TAM.

**Distribution TAM = Marketing/lead-gen spend + brokerage-commission
pool:**
- **Conservative: ₹38,000 Cr + ₹4,000 Cr = ₹42,000 Cr**
- **Realistic: ₹39,000 Cr (AR) + ₹8,000 Cr = ₹47,000 Cr**

**Data gap:** an India-specific real-estate CRM/SaaS software market size
(distinct from marketing/media spend) was searched but **NOT FOUND** —
only global figures surfaced (Real Estate CRM software, global, USD 4.73
Bn 2025 → USD 14.97 Bn 2035, 12.2% CAGR; Business Research Insights, web
search). Sell.do's specific addressable pool is likely partially embedded
in / adjacent to the ₹38-39,000 Cr distribution-spend figure (CRM spend is
typically incremental to media spend) but this cannot be verified
independently — flagged as an input gap, not separately added to avoid
double-counting risk.

**Mgmt-claim-vs-conservative-estimate ratio (Section 2 formal check):**
₹39,000 Cr (AR) ÷ ₹42,000 Cr (conservative independent) = **0.93x** → read:
**reasonable** (within the 1.5x band). Management's Distribution TAM claim
is well corroborated, not inflated.

### 2.3 CAPITAL

**Method 1 — Management claim.** AR FY24-25 (p.19): "₹50,000 crore+
Estimated SM-REITable commercial supply by FY 2026 across India."

**Method 2 — Independent, asset-value basis.** CBRE South Asia ("Navigating
the SM REIT Landscape," report referenced via web search, 2024/2025 press
coverage): potential SM-REIT-eligible market **>USD 60 Bn by 2026**
(≈₹5,70,000 Cr, FX@95), covering >300 Mn sq ft of completed commercial
office stock concentrated in Mumbai (~75 Mn sq ft), NCR (~70 Mn), Bengaluru
(~50 Mn), Hyderabad (~30 Mn); a later update (secondary web summary, exact
report undated beyond "late 2025/2026") cites **>USD 75 Bn / 500 Mn sq
ft**. Conservative figure (lower of the two, per bias rule): USD 60 Bn =
**₹5,70,000 Cr**.

**Divergence flag — large:** AR's ₹50,000 Cr is only **~9%** of CBRE's
₹5,70,000 Cr independent estimate for what appears to be the same
underlying concept (SM-REIT-eligible commercial stock). Read: AR's figure
most likely describes near-term FY26 listing-ready supply (a
SAM/SOM-adjacent, narrower concept) rather than CBRE's full eligible
stock (a true TAM ceiling) — this is a plausible, not confirmed,
reconciliation; no single primary source in this run states both
figures side by side.

**Converting asset value to revenue TAM.** Aurum's Capital business earns
asset-management fees on AUM (Integrow AIF licenses, AMSA SM-REIT), not
asset sale proceeds. An India-SM-REIT-specific fee rate was searched but
**NOT FOUND**; a generic real-estate AIF/AMC fee benchmark of **0.5–2.0%
of AUM p.a.** was found (Dwellsy IQ / SyndicationPro, generic US/global
real-estate AM industry sources, web search 2026-07-14 — **flagged as an
approximation, not India-SM-REIT-specific**).
- Conservative: AR near-term supply (₹50,000 Cr) × 1.0% fee = **₹500 Cr**
- Realistic: CBRE eligible stock (₹5,70,000 Cr) × 0.5% fee (lower fee rate
  applied to the larger, longer-horizon base) = **₹2,850 Cr**

**Mgmt-claim-vs-independent ratio (asset-value, like-for-like):**
₹50,000 Cr ÷ ₹5,70,000 Cr = **0.088x** → read: **unusually conservative**
— management is describing a narrow near-term subset, not overclaiming
the category.

### 2.4 Triangulation table (all segments)

| Segment | Method | Estimate (₹ Cr) | Confidence | Staleness |
|---|---|---|---|---|
| Rental | M1 top-down (aggregator × AR ratio) + Colliers | 4,557 | M | Rental aggregator data 2024 (M); Colliers 2025 (H, fresh) |
| Rental | M2 bottom-up full-penetration ceiling (not used as headline) | ~88,000 | L | Colliers 2025 base, but 100%-conversion assumption is aggressive |
| Rental | M3 peer aggregation (Dolat bed-counts) | ~260 (internally inconsistent, not used) | L | **STALE** — Dolat note dated May-2024 |
| Rental | Divergent secondary (JLL, Cushman) | 5.7 lakh Cr – 38 lakh Cr (excluded) | L | JLL undated secondary citation; Cushman **STALE** (Jan-2020 base) |
| Distribution | M1 mgmt claim + independent corroboration | 38,000–39,000 | M-H | AR FY24-25 (fresh); Brainguru blog (weak but close) |
| Distribution | M2 bottom-up brokerage pool | 4,000–8,000 | M | AR homes-purchased figure fresh; commission-rate range from generic web sources |
| Capital | M1 mgmt claim (asset value) | 50,000 | M | AR FY24-25, fresh, narrow scope |
| Capital | M2 independent (asset value, CBRE) | 5,70,000–7,12,500 | M | CBRE report(s), 2024/2025 |
| Capital | Revenue-equivalent (fee-rate applied) | 500–2,850 | L | Fee rate is generic, non-India-SM-REIT-specific — **flagged approximation** |

**Consolidated TAM (sum of segment conservative / realistic figures):**

| | Rental | Distribution | Capital | **Total** |
|---|---|---|---|---|
| Conservative | 4,557 | 42,000 | 500 | **47,057** |
| Realistic | 4,557 | 47,000 | 2,850 | **54,407** |

---

## SECTION 3: SAM & SOM

### 3A. SAM (five filters applied to conservative TAM)

- **Product fit:** high — Aurum's products (co-living, managed-rental
  commission, lead-gen, CRM, brokerage, SM-REIT AMC) map directly onto
  each TAM component; no material product-fit discount applied.
- **Geography:** Aurum's ~15-city footprint (AR) overlaps heavily with
  where each TAM concentrates — co-living demand is "~70%+ Top-8 cities"
  (Colliers); SM-REIT-eligible stock is ~64% concentrated in
  Mumbai/NCR/Bengaluru/Hyderabad alone (CBRE city breakdown, computed:
  (75+70+50+30)/350 Mn sq ft ≈ 64%). Applied: **70%** filter to
  Rental and Distribution (both national-platform, top-city-concentrated
  businesses); **65%** filter to Capital (city-concentration basis, CBRE).
- **Channel/customer/capability:** not separately discounted beyond the
  geography filter above — Aurum's existing channel (840+ developer
  relations, 916 Sell.do accounts, national co-living/rental network) is
  treated as already reflected in the geography-weighted figure; no
  double-counting of filters.

| Segment | Conservative TAM (₹ Cr) | Filter | SAM (₹ Cr) |
|---|---|---|---|
| Rental | 4,557 | ×70% | 3,190 |
| Distribution | 42,000 | ×70% | 29,400 |
| Capital | 500 | ×65% | 325 |
| **Total** | **47,057** | | **32,915** |

**SAM % of TAM = 32,915 / 47,057 = 70.0%.** This is a higher-than-typical
SAM/TAM ratio, reflecting that Aurum is already a national, top-city-tier
platform in each segment rather than a niche/regional player — the
geography filter is the dominant (and only materially binding) constraint
identified.

### 3B. SOM at 3 and 5 years — arithmetic shown

**Current revenue base used: ₹424 Cr** (FY26 total income actual, +49%
YoY vs ₹285 Cr FY25; OPERATOR_CONTEXT.md item 4, Q4 FY26 results
Apr-23-2026 / concall Apr-27-2026 — full-year actual, AR/results-PDF-class
anchor). A faster Q4-FY26-exit annualized run-rate (Rental ₹55 Cr +
Distribution ₹66.9 Cr + Capital ~₹0.7 Cr, ×4 ≈ ₹490 Cr — OPERATOR_CONTEXT
item 4) is shown for context only; the lower, full-year FY26 actual
(₹424 Cr) is used for all formal calculations below as the more
conservative, cleanly-anchored base (higher CAGR hurdle = more scrutiny,
per CONSERVATIVE BIAS).

**Current SAM share, by segment** (using Q4-annualized segment run-rates
for segment-level share, since FY26 segment splits are not fully
disclosed — B04 input gap carried forward):
- Rental: ₹220 Cr / ₹3,190 Cr SAM = **6.90%**
- Distribution: ₹267.6 Cr / ₹29,400 Cr SAM = **0.91%**
- Capital: ~₹2.8 Cr / ₹325 Cr SAM = **0.86%**
- **Blended (using FY26 actual ₹424 Cr / total SAM ₹32,915 Cr) = 1.29%**

**Share-gain assumptions applied** (per the standard share-gain rules:
1-2pp/3yr normal, 3-5pp/3yr aggressive with capacity+execution evidence,
faster where unorganised share >40% is formalising):
- **Rental: +1pp (3yr) / +2pp (5yr) — "normal" tier.** Justification: Rental
  is mid-turnaround (only two consecutive profitable quarters, B04-flagged),
  not yet demonstrated aggressive-tier execution capacity, even though the
  underlying co-living market itself is formalising fast (organized
  penetration 5%→10% by 2030, Colliers).
- **Distribution: +1.5pp (3yr) / +3pp (5yr) — deliberately held at the low
  end of "normal-to-aggressive," not the full 3-5pp aggressive tier**,
  despite strong execution evidence (Sell.do+Analytica 90% YoY combined
  growth, AR; PropTiger record ₹42.8 Cr quarterly gross commission,
  OPERATOR_CONTEXT item 4) — because Distribution's *current* SAM share is
  so small (0.91%) that even a modest pp gain compounds into a very large
  % revenue increase; using the full aggressive tier here produced an
  implausible >80% CAGR for this segment alone in an earlier pass and was
  dialled back per CONSERVATIVE BIAS.
- **Capital: +0.3pp (3yr) / +1pp (5yr) — minimal.** AMSA's first SM-REIT
  scheme is not yet launched (OPERATOR_CONTEXT item 4: "to launch first
  product FY27"); no share-gain evidence exists yet.

**SAM growth rates applied (source-anchored):**
- Rental SAM: blended 38.8% (co-living portion, Colliers 2025-2030
  CAGR) + 13% (non-co-living portion, proxied to India RE market overall
  CAGR, AR: USD 482 Bn 2024 → USD 1 Tn 2030 implies (1000/482)^(1/6)−1 ≈
  13%), weighted by each portion's SAM share (2,800 co-living / 390
  NestAway).
- Distribution SAM: 13% (same AR-sourced RE market CAGR proxy — flagged
  as an approximation; the ₹38-39,000 Cr distribution-spend figure itself
  has no independently sourced forward growth rate).
- Capital SAM: 15% (assumption, no anchored SM-REIT-market forward growth
  rate found independently of the AR/CBRE stock figures already used;
  **flagged as an unanchored placeholder**, low materiality given
  Capital's ~1% weight in the total).

| Segment | Yr0 SAM | Yr0 share | Yr3 SAM (@growth) | Yr3 share | **SOM3yr** | Yr5 SAM | Yr5 share | **SOM5yr** |
|---|---|---|---|---|---|---|---|---|
| Rental | 3,190 | 6.90% | 8,051 | 7.90% | **636** | 15,148 | 8.90% | **1,348** |
| Distribution | 29,400 | 0.91% | 42,421 | 2.41% | **1,022** | 54,167 | 3.91% | **2,118** |
| Capital | 325 | 0.86% | 494 | 1.16% | **5.7** | 654 | 1.86% | **12.2** |
| **Total** | **32,915** | **1.29%** (blended) | | | **₹1,664 Cr** | | | **₹3,478 Cr** |

**Implied revenue CAGR (formal handoff to stage 11):**
- 3yr: (1,664 / 424)^(1/3) − 1 = **57.8%**
- 5yr: (3,478 / 424)^(1/5) − 1 = **52.3%**

**Cross-check against management and broker guidance:** management's own
₹1,000 Cr ARR-in-~3-years target (from a >₹500 Cr FY26 ARR base,
OPERATOR_CONTEXT) implies only a **~26% CAGR** ((1000/500)^(1/3)−1).
Dolat Capital's (non-anchored) broker model separately guides "45-50%
[consolidated revenue] CAGR hereon." My independent bottom-up SOM CAGR
(57.8%/52.3%) sits **above both** — see FLAG-SOM-CAGR-VS-MGMT in the YAML.
This is an unusual direction (management under-, not over-, claiming
relative to an independent bottom-up build) and should be read as a mild
positive credibility signal on management's target-setting, while also
flagging that my own share-gain/SAM-growth assumptions (particularly
Distribution's SAM growth proxy and Rental's co-living SAM CAGR) may
still be on the optimistic side and warrant pressure-testing at stage 11.

### 3C. Capacity cross-check

B07-emoat's `capex_embedded_growth_pct` field is **0 / NOT FOUND** — no
anchored physical-capacity ceiling exists to test the SOM against. This is
consistent with Aurum's asset-light business model (SaaS licensing,
lead-gen, commission-based brokerage, AMC fees) — physical capex is not
the natural binding constraint here, unlike a manufacturer. The relevant
capacity proxy is instead GTM/execution scale: current disclosed operating
capacity is 270 rental properties / 19,286-19,800 beds (Q3-Q4 FY26), 916
Sell.do accounts / 10,378 licenses, 840+ developer relationships, and a
single not-yet-launched SM-REIT scheme (all OPERATOR_CONTEXT/AR-anchored).
Reaching SOM3yr Rental (₹636 Cr, ~2.9x the current ₹220 Cr annualized run
rate) is broadly consistent with management's own guided bed-count
expansion (HelloWorld targeting 30,000 beds by FY27 vs ~19,800 today, Dolat
note, non-anchored) plus occupancy/pricing gains. Reaching SOM3yr
Distribution (₹1,022 Cr, ~3.8x the current ₹267.6 Cr run rate) is steep
but not physically capacity-constrained (no factory, no fixed unit
ceiling) — it is a sales/GTM execution question, not a capex one.
**capacity_check: no ₹ Cr gap is nameable because no capex ceiling
exists in the injected data; the real constraint to monitor is
GTM/execution pace, not physical capacity — flagged as a data gap, not a
"sufficient" clean pass.**

---

## SECTION 4: GROWTH DRIVERS, RISKS & STRUCTURE

### 4A. TAM growth drivers

| Driver | Impact | Evidence |
|---|---|---|
| Penetration/formalisation | High | Co-living organized penetration 5%→10% (Colliers, 2025→2030); overall organized rental penetration only 4% today (AR ratio) |
| Regulatory tailwind | High (Capital) | SEBI SM-REIT framework created 2024 (AR p.30-31, CBRE); direct enabler for the entire Capital TAM, which did not exist as a formal category before |
| Demographics | Medium-High | Urban population to 680 Mn by 2047, 230 Mn new housing units needed (AR p.48); 36.6 Mn student base cited for co-living (Dolat, non-anchored) |
| Technology enablement | Medium | 75% of homebuyers use digital platforms, 50% take virtual tours (AR p.48) — directly benefits Distribution |
| Formalisation of broker network | Medium | 90,000+ RERA channel partners, 43,000+ RERA developers (AR p.16) — large digitisable base vs Aurum's current 840+ developer relationships |
| Capital-markets deepening | Medium | ₹23,703 Cr raised by RE firms via QIP/IPO in 2024 (AR p.48) — signals institutional capital available to flow into SM-REIT-type vehicles |
| New applications (AI) | Low-Medium, weakly evidenced | Company's "Unified Brain"/AI-native narrative is the weakest-evidenced part of the B04/B07 analysis (both flag it Weak) — a real but currently unproven driver |

### 4B. TAM risks

| Risk | Monitoring signal |
|---|---|
| Disruption from horizontal SaaS entrants (Zoho, Salesforce, non-anchored/Dolat) into real-estate CRM | Sell.do pricing pressure, account-growth deceleration |
| Regulatory tightening on SM-REITs | SEBI already changed minimum ticket size once (₹25L→₹10L, Dolat, non-anchored); further AUM/leverage caps could compress Capital TAM |
| Governance-linked regulatory scrutiny | CARE Ratings flagged a rights-issue proceeds MF-parking deviation vs SEBI ICDR, since rectified (OPERATOR_CONTEXT item 2) — a live monitorable, not resolved-and-forgotten |
| Competitive saturation in co-living | Stanza Living (70,000 beds), ZoloStays (45,000) scaling faster than HelloWorld (Dolat, non-anchored, stale) — if 2-3 players consolidate the organized segment, Aurum's ceiling compresses |
| Cyclical downturn | Real estate is cyclical (B04: cyclicality "cyclical"); developer marketing spend (Distribution) and commercial asset values/investor appetite (Capital) are both pro-cyclical and cuttable in a downturn |
| Substitution / persistence of informal channels | 96% of the rental market remains informal by AR's own ratio; the 38.8% Colliers co-living CAGR assumption itself carries execution risk if formalisation is slower than projected |

### 4C. Market structure

- **Competitor count / concentration:** fragmented across all three
  segments. Co-living: Stanza Living, ZoloStays, Colive, Ishtara named
  (Dolat, non-anchored). CRM/lead-gen: Zoho, Salesforce (horizontal),
  99acres/Housing.com/NoBroker (aggregators) named (Dolat, non-anchored).
  SM-REIT: ~5 SEBI-registered sponsors as of the 2025-26 window (web
  search) — Strata, Property Share, hBits, and others alongside AMSA.
- **Organized vs unorganized:** overwhelmingly unorganized in all three —
  Rental 4% organized (AR ratio); co-living 5% penetration (Colliers); SM-REIT
  essentially 0% until the 2024 regulatory framework created the category.
- **Consolidating or fragmenting:** consolidating in co-living (organized
  stock projected 0.3 Mn→1 Mn beds by 2030, Colliers) and in SM-REITs
  (small number of licensed sponsors forming the category); Distribution/
  CRM remains fragmented with low switching costs (B04 rates Sell.do's
  moat "weak-to-moderate, unproven at scale").
- **Price vs differentiation competition:** Rental is margin-disciplined
  (HelloWorld requires ≥45% gross margin per property before expansion,
  Dolat, non-anchored); Distribution differentiates on data/AI claims
  (weakly evidenced per B07); Capital differentiates on regulatory
  licensing itself (SEBI registration is a genuine barrier to entry,
  B04-anchored).
- **Entries/exits:** SEBI's 2024 SM-REIT framework is actively drawing new
  entrants (Strata, Property Share, hBits, AMSA all recent registrants) —
  an active new-entry, not-yet-consolidated phase.
- **Import share trend:** not applicable — domestic services business.

---

## SECTION 5: SUMMARY & RUNWAY

### 5A. Funnel (₹ Cr, conservative basis)

```
TAM (conservative)         ₹47,057 Cr   [Rental 4,557 | Distribution 42,000 | Capital 500]
   ↓ (geography/channel filter, 65-70%)
SAM                        ₹32,915 Cr   (70.0% of TAM)
   ↓ (current capture: blended 1.29% of SAM)
Current revenue (FY26)     ₹424 Cr
   ↓ (share-gain trajectory, 3yr)
SOM 3yr                    ₹1,664 Cr    (57.8% implied revenue CAGR)
   ↓ (share-gain trajectory, 5yr)
SOM 5yr                    ₹3,478 Cr    (52.3% implied revenue CAGR)
```

### 5B. Runway assessment

- **Revenue headroom = SAM ÷ current revenue = 32,915 / 424 = 77.6x.**
- **TAM growth rate (blended, Rental+Distribution weighted, Capital
  excluded as non-comparable/nascent) ≈ 15%.**
- **Company CAGR vs TAM:** FY26 actual revenue growth was **+49% YoY**
  (₹424 Cr vs ₹285 Cr, OPERATOR_CONTEXT-anchored) — more than 3x the ~15%
  blended TAM growth rate, i.e. Aurum is clearly **gaining share**, not
  merely riding the market.
- **Years to saturate SAM at current relative growth:** illustrative only
  — at a 49% company growth rate vs ~15% TAM/SAM growth, the relative
  share-closing rate is ≈(1.49/1.15)−1 ≈ 29.6%/yr; from a 1.29% current
  blended SAM share, reaching 100% would take ≈ln(100/1.29)/ln(1.296) ≈
  **~17 years** if both growth rates held constant (they will not — shown
  for scale only, not a forecast).

### 5C. Runway classification

Using headroom (77.6x) and TAM growth (~15%) against a standard
MASSIVE(>100x & >20% growth) / STRONG(25-100x & 10-20%) / GOOD(10-25x &
5-10%) / MODERATE(3-10x & 0-5%) / LIMITED(<3x or shrinking) matrix (matrix
thresholds not given in the stage prompt; applied here transparently):

**Runway class: STRONG.** Very large revenue headroom (77.6x SAM/current
revenue) combined with double-digit blended TAM growth (~15%) and a
company growth rate (49% FY26 actual) that is running well ahead of the
market — but short of MASSIVE given Distribution (89% of TAM weight)
grows at a moderate ~13% and Capital's TAM remains genuinely nascent and
unmonetised.

### 5D. SAM expansion levers actually being pursued

| Lever | Evidence | Potential ₹ Cr addition |
|---|---|---|
| Geographic expansion (HelloWorld into Ahmedabad, Chennai, Goa) | AR p.49 | NOT FOUND — not independently sized |
| NestAway resale-segment entry | AR p.49 ("successfully entered the resale segment") | NOT FOUND — no secondary-brokerage market size located in this run |
| SM-REIT multi-scheme rollout beyond AMSA's first scheme | OPERATOR_CONTEXT item 4 ("first product FY27") | Already inside the Capital TAM sized above; this is SOM-execution, not TAM-expansion |
| Cross-sell/"Unified Brain" ecosystem monetisation | B04/B07 flag this as the weakest-evidenced narrative in the company (both rate it Weak) | NOT FOUND — no monetisation disclosed yet; treat as optionality, not a sizing input |

### 5E. Final output card

TAM (conservative / realistic): **₹47,057 Cr / ₹54,407 Cr**
SAM: **₹32,915 Cr** (70.0% of TAM)
SOM 3yr / 5yr: **₹1,664 Cr / ₹3,478 Cr**
SOM-implied revenue CAGR: **57.8% (3yr) / 52.3% (5yr)**
Current SAM share: **1.29%** | Revenue headroom: **77.6x** | Runway: **STRONG**
Management's ₹1,000 Cr-ARR-in-3-years claim ÷ my conservative SOM3yr =
1,000 / 1,664 = **0.60x → read: conservative** (management is *not*
overclaiming relative to an independent bottom-up build — an atypical and
mildly positive credibility signal, though it also means the SOM
assumptions above should be pressure-tested, not taken as ceiling-proof).

**Valuation implication line:** current P/E is **NOT MEANINGFUL / NOT
FOUND** for Aurum in this run — FY26 is only the first barely-profitable
year and Q4 FY26 profit included a ₹17.72 Cr one-time building-sale gain
(B04-anchored, FLAG-ONE-TIME-ITEM), and B04 explicitly places
"trailing/forward P/E on a single consolidated EPS" in its
`not_applicable` valuation-methods list. Margin trajectory beyond the
FY26 actual (Adjusted EBITDA margin 5.9%, OPERATOR_CONTEXT/B04) is not
forecast in any injected document (NOT FOUND). The template sentence is
therefore left for stage 11 to complete with its own margin/multiple
work: "At **57.8% (3yr) / 52.3% (5yr)**% revenue CAGR implied by SOM, with
margin trajectory of **NOT FOUND**%, the earnings growth embedded here is
**NOT FOUND**% CAGR, which [supports / does not support] the current
valuation of **NOT FOUND**x P/E (P/E not meaningful per B04)." This is a
formal handoff — stage 11 owns the multiple/margin work; this stage
supplies only the SOM-implied revenue CAGR.

---

```yaml
stage: B09-tam
company: "AURUM"
run_date: "2026-07-14"
model: claude-sonnet-5
status: complete
input_gaps:
  - "India-specific real-estate CRM/SaaS software market size NOT FOUND independently; only global figures located (Real Estate CRM software market, global, USD 4.73 Bn 2025). Sell.do's specific addressable pool is likely partially embedded in the ₹38-39,000 Cr Distribution marketing-spend figure but could not be verified separately."
  - "India-SM-REIT-specific asset-management fee rate NOT FOUND; used a generic real-estate AIF/AMC fee benchmark (0.5-2.0% of AUM p.a., non-India-specific) as a proxy to convert the SM-REIT asset-value TAM into a revenue-equivalent TAM. Flagged as an approximation."
  - "B07-emoat capex_embedded_growth_pct is 0/NOT FOUND; no anchored physical-capacity ceiling exists for the Section 3C cross-check. Aurum's model is asset-light so this is a lower-severity gap than for a capex-heavy business, but it means capacity_check below is qualitative only."
  - "FY26 segment-level revenue actuals are only partially disclosed in the injected documents (Q2-Q4 FY26 only, no Q1 FY26 figure, consistent with the same gap already flagged in B04); segment-level current-SAM-share figures use a Q4 FY26 annualized run-rate proxy, not a full FY26 actual segment split."
  - "No anchored average-rent premium for organized vs unorganized rental stock; the AR-derived 4% organized-penetration unit-count ratio was applied directly to blended rental-market value, which likely understates true organized GMV since managed stock typically commands a rent premium (no sourced premium % found to correct for this)."
  - "Co-living market-size estimates diverge sharply across sources (Colliers ₹4,000 Cr 2025 vs JLL ~USD 6-7 Bn vs Cushman & Wakefield USD 40 Bn); Colliers (freshest, most internally consistent with Aurum's own disclosed scale) used as the anchor, others excluded from the headline TAM and recorded only as divergence flags."
  - "SM-REIT TAM diverges ~11x between the AR management claim (₹50,000 Cr near-term supply) and the CBRE independent estimate (~₹5,70,000 Cr eligible stock); the two figures most likely describe different scopes (near-term listing pipeline vs full eligible stock) but this reconciliation is inferred, not confirmed against a primary source that states both together."
flags:
  - type: FLAG-DIVERGENT-ESTIMATES
    reason: "Co-living market-size estimates range from ₹4,000 Cr (Colliers 2025) to USD 6-7 Bn (JLL) to USD 40 Bn (Cushman & Wakefield) for essentially the same year/market — a 14x to 90x spread. Conservative, most-internally-consistent figure (Colliers) used as the TAM anchor; the divergence itself is a data-quality flag for any downstream stage citing India co-living TAM."
  - type: FLAG-DIVERGENT-ESTIMATES
    reason: "SM-REIT TAM diverges ~11x between AR management's ₹50,000 Cr near-term-supply claim and CBRE's independent ~₹5,70,000 Cr eligible-stock estimate. Likely different scope (near-term pipeline vs full eligible stock), not confirmed."
  - type: FLAG-SOM-CAGR-VS-MGMT
    reason: "Independent bottom-up SOM-implied revenue CAGR (57.8% yr3 / 52.3% yr5) is higher than both management's own implied ARR CAGR (~26%, from >₹500 Cr FY26 ARR to a ₹1,000 Cr 3-year target) and Dolat Capital's non-anchored broker guide (45-50%). Management is under-, not over-, claiming relative to this independent build (mgmt_claim_ratio 0.60x) — an atypical, mildly positive credibility signal, but it also means the SOM share-gain/SAM-growth assumptions used here should be pressure-tested at stage 11 rather than treated as a hard floor."
  - type: FLAG-CAPACITY-CROSS-CHECK-INCOMPLETE
    reason: "B07-emoat capex_embedded_growth_pct = 0/NOT FOUND; Section 3C capacity check is qualitative only (GTM/execution capacity, not physical capex, is the real constraint for this asset-light business model)."
market_definition: "India-only, three separately-sized engines: organized/managed rental (co-living + commission-based rental marketplace), real-estate developer distribution (lead-gen + CRM SaaS + primary brokerage commission), and SM-REIT/fractional commercial real-estate asset management — concentrated in Aurum's ~15-city, Top-8-metro-weighted footprint."
tam_cr: {conservative: 47057, realistic: 54407}
sam_cr: 32915
sam_pct_of_tam: 70.0
som_3yr_cr: 1664
som_5yr_cr: 3478
som_implied_revenue_cagr: {yr3: 57.8, yr5: 52.3}
current_sam_share_pct: 1.29
revenue_headroom_x: 77.6
tam_growth_pct: 15
runway_class: "STRONG"
mgmt_claim_cr: 1000
mgmt_claim_ratio: 0.60
mgmt_claim_read: "conservative"
capacity_check: "no capex ceiling nameable — B07 capex_embedded_growth_pct = NOT FOUND; qualitative check (asset-light model) points to GTM/execution pace, not physical capacity, as the binding constraint on SOM"
methods_used:
  - "Top-down aggregator market size narrowed by an AR-anchored organized-penetration unit-count ratio (Rental)"
  - "Bottom-up unit economics using Colliers 2025 co-living bed-count/realization data (Rental)"
  - "Management-disclosed segment opportunity figures independently corroborated via web search (Distribution, Capital)"
  - "Bottom-up commission-pool sizing using AR homes-purchased value x independently-sourced brokerage commission-rate range (Distribution)"
  - "Asset-value TAM (independent, CBRE) converted to revenue-equivalent TAM via a generic AIF/AMC fee-rate benchmark (Capital)"
  - "Share-gain-rule-based SOM build with segment-specific SAM growth rates, cross-checked against management's ARR target and a non-anchored broker CAGR guide"
stale_data_flags:
  - {datapoint: "Dolat Capital Initiating Coverage broker note (entire content, competitor bed-counts, per-bed realization)", source: "Dolat Capital, non-anchored", year: 2024}
  - {datapoint: "Cushman & Wakefield co-living USD 6.6-13.9 Bn 2019-2025 estimate", source: "Cushman & Wakefield Jan-2020 report, cited via Dolat Capital broker note", year: 2020}
  - {datapoint: "IMF India residential rental market USD 20 Bn valuation", source: "IMF 2012 study, cited via Dolat Capital broker note", year: 2012}
  - {datapoint: "JLL India co-living USD 6-7 Bn by 2025 estimate", source: "secondary web-search summary attributing to JLL India, primary report/date not independently retrieved", year: "undated"}
searches_performed:
  - "India co-living market size 2025 2026 report crore billion"
  - "India real estate CRM SaaS market size 2025"
  - "SM-REIT India market size AUM opportunity 2025 2026 SEBI"
  - "India real estate digital marketing lead generation proptech spend market size crore"
  - "Colliers India co-living market report 2025 crore size"
  - "India organized rental housing market size property management platform"
  - "aurumproptech.in FAQ page fetch (what is the size of the proptech market in India) - failed, HTTP 403"
  - "India real estate primary sales brokerage commission rate percentage developer channel partner"
  - "CBRE India SM REIT USD 60 billion report REITable stock definition office space"
  - "India REIT AIF real estate asset management fee percentage AUM typical rate 2025"
  - "USD to INR exchange rate July 2026"
searches_skipped: []
```
