# STAGE 9: TAM / SAM / SOM MARKET SIZING
## India Nippon Electricals Ltd (INDNIPPON) — run 2026-09-10

STATUS NOTE, read first: the WebSearch tool was unavailable for this entire
session (approximately 14 attempts across the run, every one returning
"web search tool is currently unavailable"). WebFetch against named URLs
worked and supplied the external data used below. Where a number could
not be reached by WebFetch either, it is marked NOT FOUND. This makes the
run **status: partial**; every skipped search is logged in the YAML.

---

## SECTION 1: MARKET DEFINITION

### 1A. Precise boundaries

**Product scope.** OEM-fit automotive electricals and electronics for
two-wheelers (2W) and three-wheelers (3W): flywheel magnetos (FWM),
regulator-rectifiers, ignition coils, CDI/TCI units, electronic ignition
systems, ECUs (ISG controller, EGR controller, EFI ECU), sensors, and the
nascent EV stack (DC-DC converters, motor controllers, traction motors,
side-stand sensors, TPMS, instrument clusters). General-purpose-engine
(GPE) electricals and the aftermarket channel are named separately below
as distinct pools (per the injected task instruction), not folded into
the core TAM.

**Geographic scope.** India-built vehicles, both sold domestically (92%
of FY26 revenue) and exported as finished 2W/3W units (a different pool
from INEL's own direct export sales, which sit at 8.2% of revenue / Rs
87.27 cr, to USA, Italy, China, Slovenia, Turkey, Vietnam, Thailand,
Japan, Nepal, Sri Lanka, Bangladesh, Africa — Investor Presentation
2026-08-21, p.5).

**Customer scope.** 2W/3W OEMs. Only three are named anywhere in the
corpus: TVS Motor, Hero MotoCorp, Bajaj Auto (BRSR Q19(c), AR2026); two
of them are 70.66% of revenue (Note 28, AR2026, per stage 0/7 carry).
Honda Motorcycle & Scooter India — a top-3 Indian 2W OEM by volume on
general market knowledge — is named nowhere as an INEL customer. This
absence is material and is treated as a real constraint on SAM below, not
proof of no relationship.

**Channel scope.** Direct OEM (Tier-1 mechatronics) supply plus a
dealer/distributor aftermarket channel (10.86% of sales; Aftermarket
overall ~11% of revenue per injected facts, targeted to reach "15%
levels" — Investor Presentation 2026-03-17, p.21).

**Price/spec segment.** INEL has explicitly aligned toward the
150cc-plus premium motorcycle segment, where content per vehicle is
higher (AR2026 MD&A p.124-125, "the Company has aligned itself with
faster-growing pockets, particularly the premium motorcycle segment").

**Explicit exclusions.** Passenger-vehicle and commercial-vehicle
electronics (ADAS, infotainment, BMS at scale), body electronics/wiring
harness (Minda Corporation's core turf, not INEL's), four-wheeler
electronics (an unconverted optionality item per B07, not a revenue line
yet), and any market outside the twelve named export destinations at
meaningful scale.

### 1B. Management's own TAM claim, held for comparison

Every investor deck examined (Institutional Meet 2026-03-17 p.27-28;
Investor Presentation 2025-09-22 p.27-28) and the AR2026 MD&A cite the
identical set of **global, all-vehicle-class** category market sizes,
sourced to Mordor Intelligence and 6Wresearch:

- Global Automotive Ignition System Market: USD 15.2 Bn by 2033, 6.2%
  CAGR (source cited by company: mordorintelligence.com; base year not
  stated).
- Global Automotive Sensors Market: USD 37.11 Bn (2024) to USD 75.40 Bn
  (2030), 12.54% CAGR.
- Global General Purpose Engines Market: USD 10.86 Bn (2024) to USD
  14.54 Bn (2032).
- Indian auto-component export potential: USD 30 Bn by 2026 (IBEF, cited
  AR2026 p.121).
- India's EV market: USD 110.7 Bn by 2029 (AR2026 MD&A p.120, sourced to
  evfy.in).

**Credibility read: BROAD.** None of these figures is India-specific,
2W/3W-specific, or scoped to INEL's own product range. Management never
states what fraction of any of these global category totals it can
plausibly reach, nor gives a single consolidated Rs Cr TAM figure for its
own business anywhere in the corpus searched. This is a textbook case of
citing an enormous adjacent category as implicit growth-runway evidence
without doing the work of scoping it — precisely the failure mode this
stage exists to correct (see mgmt_claim fields, Section 2).

---

## SECTION 2: TAM ESTIMATION — MULTIPLE METHODS

The relevant market, defined tightly per 1A, is: **OEM-channel
electricals/electronics/mechatronics content sold into India-built 2W
and 3W vehicles.** GPE and aftermarket are sized as separate pools
(item 4-5 of the task brief) and excluded from the headline TAM so the
funnel is not double-counted.

### Method 1 — Top-down (LOW confidence; stated as such)

Top-down decomposition needs a category split of the Indian auto
component industry (engine parts / drive-transmission / electricals /
body, etc.). That split was **not found** this session — WebSearch, the
tool that would normally surface an ACMA category table, was down for
the entire run (see status note). What WebFetch could confirm
independently:

- India auto component industry, H1 FY26 turnover: Rs 3.56 lakh crore
  (USD 41.2 Bn), OEM supply Rs 3.04 lakh crore, aftermarket Rs 53,160 cr,
  EV share of OEM supply 4.6% (motorindiaonline.in/ACMA, fetched
  2026-09-10). Annualising the OEM figure (~Rs 6.08 lakh crore/year)
  cross-checks against AR2026's own cited USD 85.8 Bn full-industry FY26
  figure (AR2026 MD&A p.122) — the two sources agree, which is a genuine
  corroboration, but neither gives the electricals-category slice.
- India automotive electronics market specifically (closer to but still
  broader than INEL's scope, since it includes PV/CV electronics):
  USD 11.8 Bn (2025) to USD 19.2 Bn (2034), 5.34% CAGR (IMARC Group,
  fetched 2026-09-10).

Without a sourced category split, Method 1 cannot be pushed to a
defensible India-2W-specific number. It is retained only as a sanity
ceiling: the electronics-only India market (USD 11.8 Bn ≈ Rs 9.8 lakh
crore at ~₹83/USD) is roughly 300x the bottom-up estimate below — plausible
given it spans every vehicle class, not just 2W/3W. **Confidence: LOW.
Used for directional sanity only, not the headline number.**

### Method 2 — Bottom-up (PRIMARY method; built transparently from
INEL's own numbers per the task instruction, since no third-party
content-per-vehicle report could be sourced)

**Step 1 — total addressable unit population, FY26.**
- 2W domestic sales: 2,66,91,916 units (SIAM data, AR2026 MD&A p.118-119
  table). This includes a 36.1% YoY jump versus FY24-25's 1,96,07,332
  units — the AR itself attributes this to the GST 2.0 rollout of
  September 2025, a policy-driven demand pull-forward, **flagged as a
  non-repeatable base-year effect** (see Section 4B and the Section 5
  runway discussion).
- 2W exports: 5.1 million units (AR2026 MD&A p.121, "Two-wheeler exports
  led the way, reaching an impressive 5.1 Million units").
- 3W domestic sales: 13,00,805 units (same SIAM table). 3W exports: NOT
  FOUND this session.
- **Total 2W+3W population, INEL's addressable universe = 26.69 mn +
  5.10 mn + 1.30 mn ≈ 33.09 million vehicles (FY26).**

**Step 2 — content per vehicle, built from INEL's own numbers (real
public per-vehicle content data for Indian 2W electricals could not be
sourced this session; this is an ESTIMATE, arithmetic shown in full).**

- INEL FY26 2W+3W revenue = 85% + 6% = 91% x Rs 1,068.48 cr = **Rs
  972.32 cr** (FY26 AR standalone Note 28, injected mix facts).
- Strip the aftermarket channel (11% of total revenue, cuts across
  segments, not tied 1:1 to new-vehicle units): Rs 972.32 cr x 89% =
  **Rs 865.36 cr** OEM-channel 2W+3W revenue.
- Served-vehicle population, two independent proxies:
  (a) FWM national market share, 28%, "No.1 position in India for FWM"
  (Institutional Meet 2026-03-17, p.24) x 33.09 mn total population =
  **9.27 million vehicles**.
  (b) FWM production run-rate, ~2 million units in Q1FY27 (Investor
  Presentation 2026-08-21, p.14), annualised x4 (single-quarter
  run-rate, seasonality unverified — flagged) = **8.0 million vehicles**.
  Average of the two: **~8.6 million vehicles**, used below.
- **Content per served vehicle = Rs 865.36 cr / 8.6 mn units ≈ Rs
  1,006/vehicle** (ESTIMATE; range Rs 930-1,092/vehicle depending on
  which served-population proxy is used).

**Step 3 — full-penetration TAM.**
- Realistic: Rs 1,000/vehicle (rounded midpoint) x 33.09 million total
  2W+3W population = **Rs 3,309 cr ≈ Rs 3,300 cr**.
- Conservative: lower end of the content range (~Rs 930/vehicle) x the
  domestic-only, more conservative population (26.69 mn 2W + 1.30 mn 3W
  = 27.99 mn, excluding exports) = **Rs 2,603 cr ≈ Rs 2,600 cr**.

**A genuine internal cross-check.** INEL's FY26 2W+3W revenue (Rs 972.32
cr) is 29.5% of the Rs 3,300 cr realistic TAM. Its disclosed national FWM
market share is 28%. These two independently-sourced numbers (a revenue
ratio and a unit-share disclosure) land within 1.5 points of each other —
a reasonable internal consistency signal that the TAM construction is
calibrated to something real, though not proof of accuracy.

### Method 3 — Peer revenue aggregation (data-poor; LOW-MODERATE
confidence)

Public, listed peers with a 2W/3W electricals footprint that could be
sourced this session:
- UCAL Ltd: FY26 revenue Rs 647 cr (screener.in, fetched 2026-09-10);
  carburettors, fuel management, emission control, automotive electronics
  and mechatronic components — overlapping but not identical scope.
- Minda Corporation: FY26 revenue Rs 5,017 cr (screener.in, fetched
  2026-09-10); primarily wiring harness/connectors/switches, a 2-3W
  revenue segment exists but its % of total was not disclosed on the
  page fetched — NOT FOUND.
- Bosch, Denso, Delphi-TVS, Varroc Engineering: no 2W-specific segment
  revenue sourced this session (private-JV or diversified-segment
  disclosure; WebSearch down).

**Floor only:** two named public pure/near-pure plays alone total Rs
1,715 cr before adding Bosch/Denso/Varroc and the OEM-captive slice. This
is *consistent with, not contradicting* the Rs 2,600-3,300 cr bottom-up
range — it shows the real market is at minimum comparable in scale, but
cannot independently triangulate a tighter number. **Unlike most Indian
component categories, this niche (precision OEM-qualified Tier-1 supply)
is not meaningfully unorganised** — the standard India unorganised-sector
uplift (30-60%) is not applied here; that dynamic belongs to the
aftermarket pool (Section 3-adjacent), not OEM supply.

### Method 4 — Import substitution: not applicable in the standard
direction

INEL is not an import-substitution beneficiary in its own product
category (it already holds a 28% domestic FWM share against no evidenced
import competition). The live import-substitution dynamic here runs the
other way — INEL substituting *imported Chinese rare-earth permanent
magnets* with domestic ferrite alternatives inside its own bill of
materials. That is an input-cost/supply-risk item, covered in Section 4B,
not a TAM-expansion method.

### Method 5 — Global benchmark (sanity check only, LOW confidence)

Applying management's own cited global Automotive Sensors figure (USD
37.11 Bn in 2024, interpolated at 12.54% CAGR to ~USD 47.0 Bn in 2026 —
calculation shown, not a sourced 2026 figure) against even a low
single-digit India-2W assumed share would still land far above the
bottom-up range, because the global figure spans every vehicle class and
every sensor type on earth. This method is retained to show the scale
mismatch explicitly, not as a usable India-2W estimate: **no sourced
India-share percentage exists to make Method 5 more than illustrative.**

### Triangulation table

| Method | Estimate (Rs Cr) | Confidence | Staleness | Notes |
|---|---|---|---|---|
| 1. Top-down | Not computable to India-2W scope | LOW | Current (2026 fetches) | No sourced ACMA category split |
| 2. Bottom-up (conservative) | 2,600 | MODERATE | Current | INEL's own FY26 numbers, arithmetic shown |
| 2. Bottom-up (realistic) | 3,300 | MODERATE | Current | as above |
| 3. Peer aggregation | >1,715 (floor only) | LOW-MODERATE | Current | 2 named peers only; Bosch/Denso/Varroc NOT FOUND |
| 4. Import substitution | N/A (wrong direction for this business) | N/A | N/A | Covered as input risk, Section 4B |
| 5. Global benchmark | Not usable (scale mismatch) | LOW | Current | No sourced India-share % |

**Conservative TAM = Rs 2,600 cr. Realistic TAM = Rs 3,300 cr.**

**Management's claim vs the conservative estimate.** Management gives no
single India-specific or INEL-specific TAM figure to divide by anything.
A literal ratio using the cited *global* sensors/ignition/GPE figures
against the Rs 2,600 cr conservative estimate would read in the
hundreds-of-times range — but that reflects scope mismatch (global,
all-vehicle-class vs India-2W/3W-specific), not a genuine claim-vs-reality
gap. **mgmt_claim_cr is reported as 0/NOT FOUND rather than fabricating a
false-precision ratio.** mgmt_claim_read: **not comparable — BROAD by
construction.** This is exactly the "TAM = SAM = growth runway" dishonesty
pattern this stage is built to catch: the figures are real, sourced, and
irrelevant to INEL's actual served market.

---

## SECTION 3: SAM & SOM

### 3A. SAM — five filters applied to the Rs 3,300 cr realistic TAM

1. **Product fit ≈ 100% (no further discount).** The TAM base was
   already built from INEL's own product mix (ignition + controllers +
   sensors, partial EV), not a broader "everything electronic on a 2W"
   figure, so product scope is already embedded, not a separate cut.
2. **Geography ≈ 100% (no further discount).** TAM already counts
   domestic + export-bound India-built units; INEL sells into both
   channels today (92% domestic / 8% export by revenue).
3. **Channel — already stripped.** Aftermarket was removed at the TAM
   build stage (Step 2 above) and is handled as its own pool (Section 4
   item 5), so no further channel cut applies inside this OEM-scoped SAM.
4. **Customer fit — the binding constraint, 40% (ESTIMATE).** Real,
   evidenced anchor: 28% national FWM market share (Institutional Meet
   2026-03-17, p.24). SAM applies 40%, a deliberate uplift above the raw
   28%, because (a) INEL sells more than FWM into its existing accounts
   (controllers, sensors, aftermarket), so effective wallet share x
   account coverage plausibly exceeds the single-product share, and (b) a
   realistic 3-5 year SAM should include modest new-OEM-win optionality.
   **This 40% is an analyst judgement, not a sourced figure — flagged
   explicitly.** Honda Motorcycle & Scooter India and most pure-EV OEMs
   (Ola Electric, Ather) are excluded from this SAM: no customer
   relationship is evidenced anywhere in the corpus.
5. **Capability — 85% (ESTIMATE).** Most of SAM sits in the mature ICE
   ignition stack (mass production today). The EV product line is mixed
   maturity: motor controller and traction motor are tagged "In Mass
   Production," the instrument cluster is explicitly "in proto stage" /
   "in development stage" (Investor Presentation 2026-08-21, p.8); DC-DC
   converter, side-stand sensor and TPMS maturity could not be cleanly
   read from the extracted deck layout — NOT FULLY DETERMINABLE. 85%
   reflects a modest discount for this EV-capability uncertainty.

**SAM = Rs 3,300 cr x 0.40 x 0.85 = Rs 1,122 cr.**
**SAM as % of TAM = 34.0%.**

**Current SAM share.** INEL's FY26 2W+3W OEM revenue proxy (Rs 865.36 cr,
per Step 2 above) / SAM (Rs 1,122 cr) = **77.1%** of this narrowly-defined
SAM already captured (on a full-revenue-including-aftermarket basis, Rs
972.32/1,122 = **86.7%** — this higher figure is used in the YAML as the
more conservative, revenue-inclusive read). **Either way the finding is
the same: INEL is already close to saturating the SAM as constructed from
its current, evidenced customer relationships.** This is an important,
uncomfortable result and is carried through to Section 5.

### 3B. SOM at 3 and 5 years

**Forward TAM/SAM growth rate.** Two candidates: SIAM's implied 5-year
2W unit CAGR of ~12.0% (FY20-21 to FY25-26; calculation: (2,66,91,916 /
1,51,20,783)^(1/5)-1) is doubly distorted — a COVID-trough starting year
and a GST-2.0-spike ending year — and is rejected as the forward
assumption per the stage's conservative-bias rule. Mordor Intelligence's
India 2W market value CAGR of 5.02% (2026-2031, same source AR2026
cites) is used instead as the **conservative, external, cross-checked**
forward growth rate for SAM.

- SAM (Y3, FY29) = Rs 1,122 cr x (1.05)^3 = **Rs 1,299 cr**.
- SAM (Y5, FY31) = Rs 1,122 cr x (1.05)^5 = **Rs 1,432 cr**.

**Share-gain assumption.** Current SAM share ~86.7% is already high (near
a mature-franchise ceiling for the ICE stack it already sells). Applying
the "normal" 1-2pp/3yr share-gain rule: +1.5pp by Y3, and a proportionally
extended +2.5pp by Y5 (between "normal" extended and "aggressive," given
B07's FY26 capex acceleration (+81.3% YoY) supports upside but the
Emerging Moat score of 24/100 MODEST argues against the full aggressive
3-5pp band).

- SOM (Y3, core 2W+3W) = 88.2% x Rs 1,299 cr = **Rs 1,145.6 cr**.
- SOM (Y5, core 2W+3W) = 89.2% x Rs 1,432 cr = **Rs 1,277.4 cr**.

**Grossed up to total-company basis for the stage-11 handoff.** Per the
task instruction, GPE is a separate pool; it is added here (not into
TAM/SAM above) purely so the SOM figure is comparable to total reported
revenue. GPE FY26 = 9% x Rs 1,068.48 cr = Rs 96.16 cr; grown at the
global GPE CAGR management itself cites (2.09%, Institutional Meet
p.27-28 — a conservative proxy since no India-specific GPE figure exists):
- GPE (Y3) = Rs 102.3 cr; GPE (Y5) = Rs 106.7 cr.

**SOM (Y3, total company) = Rs 1,145.6 + 102.3 = Rs 1,248 cr.**
**SOM (Y5, total company) = Rs 1,277.4 + 106.7 = Rs 1,384 cr.**

**Implied revenue CAGR (from FY26 base Rs 1,068.48 cr):**
- Y3: (1,248 / 1,068.48)^(1/3) - 1 = **5.3%**
- Y5: (1,384 / 1,068.48)^(1/5) - 1 = **5.3%**

**THE HEADLINE FINDING — flagged for operator ruling, Amendment 14
fade-guard trigger.** This bottom-up SOM implies ~5.3% forward revenue
CAGR. INEL just delivered 26.5% YoY revenue growth in FY26 and 35.5% YoY
in Q1FY27 (against 20% 2W industry growth — Investor Presentation
2026-08-21, p.14). The gap is not the classic Amendment 14 pattern (SOM
above a faded number); it runs the **opposite direction** — SOM
materially *below* recently delivered growth. Two honest readings, named
per the "state both readings, name the observation that separates them"
discipline (v3.9 Amendment 25):

- **Reading A — the SAM is too narrow.** The bottom-up construction
  anchors SAM to *today's* customer relationships and *today's* product
  mix. It structurally excludes new-OEM wins, the still-developing EV
  stack becoming a real revenue line, and any acceleration in export
  growth (which ran at 162% YoY in FY26, a pool this SAM treats only as
  embedded in the existing population, not separately grown). If any of
  these convert, the true SOM is understated here.
- **Reading B — FY26/Q1FY27 growth is a non-repeatable base effect.**
  FY26's 26.5% growth and the underlying 36.1% YoY jump in industry 2W
  volume both coincide exactly with the AR's own account of the GST 2.0
  rollout (September 2025) and its "record ~2.97 crore units" industry
  outcome (AR2026 MD&A p.118). A one-time tax-driven demand pull-forward
  does not repeat annually; a reversion toward mid-single-digit growth
  once the GST 2.0 base effect laps is a real risk this report's SOM may
  be closer to capturing than the recent print suggests.

**The observation that would separate the two readings:** whether Q2-Q4
FY27 growth (ex the GST-2.0 base quarter) holds materially above ~10%,
or reverts toward mid-single digits once the September-2025 comparison
period is lapped. **This is named explicitly for operator ruling, not
resolved here** (per CLAUDE.md: never shade an input to be safe; state
both readings and put the conservatism in position size, not in the
number).

### 3C. Capacity cross-check

B07's capex-embedded-growth figure is **4.2%** (B07-emoat.yaml,
capex_embedded_growth_pct). This is close to, but modestly below, the
5.3% SOM-implied CAGR computed above.

- Capacity-supportable revenue (Y3) = Rs 1,068.48 cr x (1.042)^3 = **Rs
  1,208.7 cr**. SOM (Y3, total company) = Rs 1,248 cr. **Gap = Rs 39.2
  cr (3.2% of SOM).**
- Capacity-supportable revenue (Y5) = Rs 1,068.48 cr x (1.042)^5 = **Rs
  1,312.6 cr**. SOM (Y5) = Rs 1,384 cr. **Gap = Rs 71.5 cr (5.2% of
  SOM).**

**Read: SOM is modestly the optimistic side, not the capex plan** — a
manageable, not alarming, gap of Rs 40-70 cr. Two caveats carried from
B07: the underlying FY26 capex of Rs 42.15 cr (up 81.3% YoY) is not tied
to any named capacity, facility, or commissioning detail anywhere in the
AR (B07 gap, confirmed independently here), so the 4.2% embedded-growth
figure's own derivation basis is opaque; and B07 separately flagged FY26
free cash flow turning roughly negative Rs 1.7 cr, which strains the
"debt-free, internally funded" capacity story precisely when capex
accelerated.

---

## SECTION 4: GROWTH DRIVERS, RISKS & STRUCTURE

### 4A. TAM growth drivers

| Driver | Impact | Evidence |
|---|---|---|
| Premiumisation (150cc+ segment) | Positive, content/vehicle up | AR2026 MD&A p.124: "aligned itself with faster-growing pockets, particularly the premium motorcycle segment... higher value-added offerings" |
| System-level solutions shift | Positive, content/vehicle up | AR2026 MD&A p.124: "transition from a traditional component supplier to an integrated, system-level solutions provider... raises the value per vehicle" |
| Export expansion | Positive, new geography | Export revenue Rs 33.25cr (FY25) to Rs 87.27cr (FY26), +162% |
| GST 2.0 tax simplification | Positive, one-time base effect | AR2026 MD&A p.117-118; flagged as non-repeating (Section 3B) |
| India-EU FTA (Jan 2026) | Positive, tariff removal on 99.5% of traded goods incl. components | AR2026 MD&A p.118 |
| Technology enablement (EFI ECU/BorgWarner licence) | Positive, new product segment | Investor Presentation 2026-08-21 p.11 (deck-tier claim only, no AR corroboration — B07 flag carried) |
| Formalisation of aftermarket | Positive, small base scaling | Aftermarket grew 20% FY26 (AR2026 MD&A p.121); target 15% of sales vs ~11-12% today |

### 4B. TAM risks

| Risk | Monitoring signal |
|---|---|
| **NdFeB/rare-earth magnet supply constraint** — named in 5 consecutive quarterly decks (Q1FY26-Q1FY27) and AR2026's own risk table (p.125-126): "Tensions between the US and China have heightened rare earth supply chain risks... increased adoption of ferrite magnets as an alternative." China restricted exports of six heavy rare-earths and rare-earth magnets in April 2025 amid US tariff escalation (Wikipedia, "China-United States trade war," fetched 2026-09-10); China holds ~90% of global rare-earth processing capacity (Wikipedia, "Rare-earth element," fetched 2026-09-10). This threatens BOTH the core flywheel-magneto franchise (permanent-magnet rotor) AND the EV motor-controller/ISG stack simultaneously — it is not a diversifiable risk within the product range. Ferrite substitution is real but explicitly partial and unquantified (AR2026; B07 confirms). | China MOFCOM export-licence announcements; INEL's own AR technology-absorption note on % ferrite-substituted |
| EV transition — content destruction on the flagship product | The flywheel magneto, INEL's No.1 franchise (28% share), generates zero revenue on a pure EV, which has no engine to synchronise ignition timing for. Whether INEL's EV stack (motor controller, DC-DC converter, traction motor) earns MORE or LESS Rs/vehicle than the ICE stack it displaces **could not be determined this session** — no INEL EV product pricing is disclosed, and WebSearch (the tool needed to source external EV motor-controller ASP benchmarks) was unavailable all session. **This is flagged as the single most important unresolved question in this report**, exactly as the task brief anticipated. | Track E2W penetration (11.85% of Indian 2W market in 2025, Mordor Intelligence, cited AR2026 p.119-120) and any disclosed INEL EV-product revenue line |
| GST 2.0 base-effect reversion | Q2-Q4 FY27 growth once the September 2025 comparison quarter is lapped (Section 3B) |
| Customer concentration | 70.66% of revenue from 2 customers (Note 28, AR2026); B07 already flags this against moat credit |
| Import competition / global players | Bosch, Denso and well-capitalised global players named as a structural threat in AR2026's own SWOT (p.124) |
| Regulatory/subsidy volatility | PM E-DRIVE (Rs 1,500 cr FY27 outlay) succeeding FAME, PLI auto-components Rs 5,939.87 cr — both AR2026 p.120 |

### 4C. Market structure

Organised, OEM-qualified Tier-1 supply, not a fragmented/unorganised
category (see Method 3 note). Competitor count in the specific
ignition/electricals niche is small and largely private or
diversified-segment (Bosch, Denso, Delphi-TVS are not standalone-listed
in this segment; UCAL and Minda are the two public comparables found).
Top-3 concentration: NOT FOUND with a sourced % this session, but
INEL's own 28% single-product national share suggests a moderately
consolidated structure. Price vs differentiation: AR2026's own SWOT
frames competition as shifting toward technology-led differentiation
(ADAS, connected mobility, software-defined vehicles) rather than pure
price (AR2026 MD&A p.124). Import share trend: NOT FOUND with a sourced
%; auto-component trade position overall flipped to a small deficit in
H1 FY26 (USD 180 mn, from a USD 150 mn surplus in H1 FY25 —
motorindiaonline.in/ACMA, fetched 2026-09-10), a directional signal
worth monitoring, though not 2W-electricals-specific.

---

## SECTION 5: SUMMARY & RUNWAY

### 5A. Funnel

```
TAM (core 2W+3W OEM content, realistic)     Rs 3,300 cr
  -> customer-fit filter (40%, ESTIMATE)
  -> capability filter (85%, ESTIMATE)
SAM                                         Rs 1,122 cr   (34.0% of TAM)
  -> current capture (FY26 2W+3W revenue Rs 972.32 cr = 86.7% of SAM)
SOM Year 3 (total company, incl. GPE)       Rs 1,248 cr   (5.3% implied CAGR)
SOM Year 5 (total company, incl. GPE)       Rs 1,384 cr   (5.3% implied CAGR)
```
GPE and aftermarket are separate pools (Section 4-adjacent), not folded
into TAM/SAM; they enter only at the SOM stage for the total-company
handoff figure (see 3B).

### 5B. Runway assessment

- **Revenue headroom = SAM ÷ current revenue.** Using the SAM (Rs 1,122
  cr, core) plus a no-growth-assumed GPE ceiling (Rs 96.16 cr) against
  total FY26 revenue (Rs 1,068.48 cr): (1,122 + 96.16) / 1,068.48 =
  **1.14x.**
- **TAM growth rate:** 5.0% (Mordor Intelligence India 2W value CAGR,
  conservatively chosen over the GST-2.0-distorted 12.0% SIAM unit CAGR;
  see Section 3B).
- **Company CAGR vs TAM:** INEL's FY26 revenue grew 26.5% against a TAM
  growing an estimated 5.0% — INEL is gaining share sharply, not riding
  the market, which is fully consistent with the ~86.7% current-SAM-share
  finding (Section 3A) and the growth-gap flag in Section 3B.
- **Years to saturate SAM at current growth:** at FY26's actual 26.5%
  growth rate, remaining SAM headroom (Rs 1,122 - 972.32 = Rs 149.68 cr,
  core-basis) would be exhausted in **under 6 months** of continued
  growth at that rate — mechanically impossible to sustain, which is
  itself evidence that either FY26's growth rate cannot repeat at this
  pace within the current SAM definition, or the SAM definition itself
  needs to expand (new OEMs, EV stack, faster export growth) for the
  growth to continue. This computation is a further, independent
  confirmation of the Section 3B flag.

### 5C. Runway classification

**LIMITED.** (Convention used, since the stage instructions reference "the
standard matrix" without stating cutoffs in the text supplied to this
run: MASSIVE >10x, STRONG 5-10x, GOOD 2-5x, MODERATE 1.5-2x, LIMITED
<1.5x headroom — stated explicitly as an assumed convention, not a
sourced threshold.) At 1.14x headroom, the currently-evidenced SAM is
nearly saturated by current revenue. The classification would move to
MODERATE or GOOD only if one or more of the SAM-expansion levers below
converts to disclosed revenue.

### 5D. SAM expansion levers actually being pursued

1. **EV product-stack maturation** (the single largest, and least
   quantifiable, lever). E2W penetration was 11.85% of the Indian 2W
   market in 2025 (Mordor Intelligence, cited AR2026 p.119-120), growing
   at a 7.02% CAGR through 2031 versus 5.02% for the overall market —
   i.e., the EV slice is growing faster than the ICE base INEL's
   existing SAM is built on. Applying 11.85% to the FY26 2W volume gives
   an approximate **3.16 million E2W units** as the physical scale of
   this pool (26,691,916 x 11.85% ≈ 3,163,192, ESTIMATE — a 2025
   penetration rate applied to a FY26 volume base). **Potential Rs Cr
   addition: NOT FOUND** — no sourced Rs/vehicle rate exists for INEL's
   motor-controller/DC-DC-converter/traction-motor stack (crux gap,
   Section 4B). This lever is real and scoped in units; it cannot
   responsibly be converted to a Rs Cr addition with data available this
   session.
2. **Export growth**, quantifiable: FY26 export revenue Rs 87.27 cr grew
   162% YoY. Even a conservative 20% forward CAGR (well below the 162%
   just delivered) would add: Rs 87.27 cr x (1.20)^3 = Rs 150.8 cr by
   Y3, an incremental **+Rs 63.5 cr** versus a flat base.
3. **Aftermarket scale-up to the company's own stated 15% target** (from
   ~11-12% today): 15% x Rs 1,068.48 cr = Rs 160.3 cr vs current ~11% =
   Rs 117.5 cr, an incremental **+Rs 42.8 cr** if the stated target is
   reached, company's own target (Institutional Meet 2026-03-17, p.21).
4. **New-OEM wins** outside the three named customers (Honda and others)
   — no evidence of progress found in the corpus; optionality only.

Revised headroom including only the two quantifiable levers (export +
aftermarket, excluding the unquantifiable EV lever): (1,122 + 96.16 +
63.5 + 42.8) / 1,068.48 = **1.24x** — still within the LIMITED band under
the stated convention, underscoring that the EV lever is doing the real
work if this thesis is to clear MODERATE/GOOD, and it is precisely the
lever this report cannot quantify with current tools.

### 5E. Final output card

**Market definition (one line):** OEM-channel electricals, electronics
and mechatronics content sold into India-built two- and three-wheelers,
where INEL holds a 28% national share of its flagship flywheel-magneto
product.

**TAM:** Rs 2,600 cr (conservative) / Rs 3,300 cr (realistic).
**SAM:** Rs 1,122 cr (34.0% of realistic TAM).
**SOM Year 3:** Rs 1,248 cr (5.3% implied revenue CAGR).
**SOM Year 5:** Rs 1,384 cr (5.3% implied revenue CAGR).
**Current SAM share:** 86.7% — near-saturated within the currently
evidenced customer and product base.
**Runway class: LIMITED** (1.14x headroom on current SAM; 1.24x with the
two quantifiable expansion levers added; the EV lever remains
unquantified).

**Valuation implication line.** CMP Rs 1,005.20/share (as of 30 Jun 2026,
Investor Presentation 2026-08-21, p.18-19); FY26 diluted EPS Rs 49.14
(consolidated income statement, same deck, p.16); implied current P/E ≈
**20.5x**. FY24-FY26 PAT margin trend: 8.19% to 10.41% (expansion, not a
forward model — margin trajectory modelling is Role 1/stage 11's task,
not this stage's).

> "At **5.3%** revenue CAGR implied by SOM, with an FY24-26 PAT margin
> trend of 8.2% to 10.4% (not a forward projection), the earnings growth
> embedded in this report's conservatively-scoped SAM/SOM **does not
> support** the current valuation of **20.5x** P/E against the strategy's
> 25% CAGR hurdle. Any valuation case that does support 25% CAGR must
> rest on the EV-content-per-vehicle question resolving favourably, new
> OEM wins, or a genuinely faster industry cycle than the conservative
> 5.02% TAM-growth assumption used here — none of which is quantified in
> this report, and the FY26/Q1FY27 delivered growth of 26.5%/35.5% may or
> may not be repeatable (Section 3B, flagged for operator ruling)."

---

## SECTION 6: DOWNSTREAM SIGNAL CANDIDATES

| # | Candidate Signal | Entity Type | Why It Drives Demand | Likely Primary Source | Expected Cadence |
|---|---|---|---|---|---|
| 1 | TVS Motor Company 2W/3W volumes and model mix | End-customer | One of INEL's 2 largest named customers (70.66% combined revenue); TVS's own volume and premium/EV mix directly drives INEL's core revenue stream | BSE/NSE corporate announcements + TVS Motor concall transcripts + AR segment note (Downstream Protocol Type 1) | Quarterly |
| 2 | Bajaj Auto 2W/3W volumes and model mix | End-customer | Same concentration logic as #1 | BSE/NSE corporate announcements + Bajaj Auto concall transcripts (Downstream Protocol Type 1) | Quarterly |
| 3 | Hero MotoCorp 2W volumes and model mix | End-customer | Named customer (BRSR Q19c); volume trend a direct demand signal for INEL's ICE ignition stack | BSE/NSE corporate announcements + Hero MotoCorp concall transcripts (Downstream Protocol Type 1) | Quarterly |
| 4 | SIAM monthly 2W/3W wholesale production and sales data | Macro | Industry volume base for the entire TAM; the GST-2.0 base-effect question (Section 3B) is resolved or confirmed here first | SIAM website monthly statistics release (Downstream Protocol Type 7) | Monthly |
| 5 | China MOFCOM rare-earth/NdFeB magnet export licensing status | Macro | Threatens both the ICE flywheel-magneto franchise and the EV motor/ISG stack simultaneously (Section 4B); a single point of failure across two of INEL's revenue streams | MOFCOM export-control announcements; cross-checked against DGCI&S India import data (Downstream Protocol Type 6/7) | Event-driven |
| 6 | Vahan/FADA electric two-wheeler registration data | Macro | Direct tracker for the E2W penetration rate (11.85% in 2025) this report used to scope the unquantified EV-content lever | Vahan Parivahan dashboard / FADA monthly release (Downstream Protocol Type 7) | Monthly |
| 7 | BorgWarner EFI ECU technical licensing partnership status | Counterparty | Named new-product-segment entry (Investor Presentation 2026-08-21, p.11); currently a deck-only claim with zero AR corroboration (B07 flag) | BorgWarner SEC EDGAR filings / investor relations (Downstream Protocol Type 3) | Event-driven |
| 8 | GST Council / CBIC GST 2.0 rate-slab stability | Regulatory | The policy event behind the FY26 volume spike this report treats as a possible one-off base effect (Section 3B); any further slab change would re-shape the industry volume base | PIB / CBIC notifications | Event-driven |

Entity #4 (SIAM data) and #5 (China rare-earth policy) are flagged
**SHARED** — SIAM data feeds both the 2W and 3W demand streams as a
single macro input, and the rare-earth constraint sits under both the
ICE and EV product lines simultaneously. FTTCP should count each once as
a correlated catalyst, not twice.

`demand_externally_verifiable: true` — 8 candidates found, well above the
minimum of 3.

---
END OF REPORT BODY

```yaml
stage: B09-tam
company: "INDNIPPON"
run_date: "2026-09-10"
model: claude-sonnet-5
status: partial
input_gaps:
  - "B04 business model decoder not available at run time (stage 4 running in parallel per orchestrator dependency table); used injected product/mix facts instead"
  - "INEL product-line revenue split (FWM vs CDI vs ECU vs sensors vs EV items) not disclosed anywhere in corpus; true SKU-level content-per-vehicle not computable, only a blended full-stack proxy built from company totals"
  - "EV motor controller / DC-DC converter / traction motor Rs-per-vehicle content NOT FOUND; WebSearch tool unavailable for the entire session (14+ failed attempts), could not source external EV powertrain-electronics ASP benchmarks -- this is the single most important unresolved number in the report"
  - "TVS Motor and Bajaj Auto individual 2W production volumes not sourced this session (WebSearch down); precluded computing INEL's exact customer-relationship coverage % of the Indian 2W population independent of the FWM national-share proxy"
  - "India-specific (vs global) market size for automotive sensors, ignition systems, and general purpose engines NOT FOUND; management cites only global, all-vehicle-class figures"
  - "Electric three-wheeler penetration percentage specifically (distinct from overall/2W EV penetration) NOT FOUND this session"
  - "ACMA product-category (electricals/electronics vs engine parts vs drive-transmission etc.) revenue split for the Indian auto component industry NOT FOUND this session, precluding a cleaner top-down Method 1 decomposition"
  - "3-wheeler export unit volume NOT FOUND; TAM population understates true 3W addressable base by this amount"
flags:
  - {type: "FLAG-SOM-BELOW-DELIVERED-GROWTH", reason: "SOM-implied CAGR (5.3%) is far below FY26 actual growth (26.5%) and Q1FY27 actual growth (35.5%). Two honest readings named in Section 3B (SAM too narrow vs FY26/Q1FY27 a GST-2.0 base-effect spike); flagged for operator ruling per the Amendment 14 fade-guard discipline, run in the opposite direction from its usual trigger."}
  - {type: "FLAG-EV-CONTENT-UNQUANTIFIED", reason: "Whether INEL's EV product stack earns more or less Rs/vehicle than the ICE stack it would displace could not be determined this session (no INEL EV pricing disclosed, WebSearch down for external benchmarks). This is the single most important open question named in the task brief and remains open."}
  - {type: "FLAG-RARE-EARTH-SUPPLY-RISK", reason: "NdFeB/rare-earth magnet supply constraint (China export restrictions, April 2025, ~90% global processing share) threatens both the core flywheel-magneto franchise and the EV motor/ISG stack simultaneously -- a single point of failure across two revenue lines, not a diversifiable risk. Ferrite substitution real but partial/unquantified."}
  - {type: "FLAG-MGMT-TAM-BROAD", reason: "Every management-cited market figure across all decks and the AR is global and all-vehicle-class; none is India-specific or INEL-scoped. mgmt_claim_cr reported as 0/not-comparable rather than a fabricated ratio."}
  - {type: "FLAG-GST-ONEOFF-BASE-YEAR", reason: "FY26's 36.1% YoY jump in industry 2W volume and INEL's own 26.5% revenue growth both coincide with the September 2025 GST 2.0 rollout, per the AR's own narrative. Forward growth built off this base risks being optimistic if the effect does not repeat."}
  - {type: "FLAG-WEBSEARCH-TOOL-OUTAGE", reason: "WebSearch tool returned 'unavailable' on every one of ~14 attempts across this session. All external data below was sourced via WebFetch against named URLs instead; several planned searches (peer competitor detail, India-specific category splits, EV component pricing) could not be substituted this way and are logged as input_gaps/searches_skipped."}
market_definition: "OEM-channel electricals, electronics and mechatronics content sold into India-built two- and three-wheelers"
tam_cr: {conservative: 2600, realistic: 3300}
sam_cr: 1122
sam_pct_of_tam: 34.0
som_3yr_cr: 1248
som_5yr_cr: 1384
som_implied_revenue_cagr: {yr3: 5.3, yr5: 5.3}
current_sam_share_pct: 86.7
revenue_headroom_x: 1.14
tam_growth_pct: 5.0
runway_class: "LIMITED"
mgmt_claim_cr: 0
mgmt_claim_ratio: 0
mgmt_claim_read: "not comparable -- management cites only global, all-vehicle-class category markets (ignition, sensors, GPE); no India-specific or 2W/3W-specific TAM figure exists anywhere in the corpus to ratio against"
capacity_check: "gap of ~Rs 40-70 Cr by Year 3-5 (SOM 3.2%-5.2% above the B07 capex-embedded growth rate of 4.2%); SOM is mildly the optimistic side, not the capex plan"
methods_used: ["bottom-up (primary)", "peer revenue aggregation (floor only)", "top-down (sanity ceiling only, not usable to scope)", "global benchmark (sanity check only, not usable to scope)", "import substitution (not applicable in standard direction)"]
stale_data_flags: []
searches_performed:
  - "WebFetch: SIAM statistics page (stale 2008-2014 data returned, superseded by AR2026's own SIAM table)"
  - "WebFetch: mordorintelligence.com/industry-reports/india-two-wheeler-market (confirmed E2W 11.85%/88.15% ICE split, 2025; 5.02% overall / 7.02% EV CAGR through 2031)"
  - "WebFetch: motorindiaonline.in ACMA H1FY26 auto component industry article (turnover, OEM/aftermarket split, export/import figures, EV share of OEM supply)"
  - "WebFetch: en.wikipedia.org/wiki/China-United_States_trade_war (April 2025 rare-earth/magnet export restrictions)"
  - "WebFetch: en.wikipedia.org/wiki/Rare-earth_element (China ~90% global processing share, 2025 restriction context)"
  - "WebFetch: screener.in/company/UCAL (peer revenue FY23-26)"
  - "WebFetch: screener.in/company/MINDACORP (peer revenue FY23-26)"
  - "WebFetch: imarcgroup.com/india-automotive-electronics-market (India automotive electronics market size/CAGR)"
searches_skipped:
  - "WebSearch: India two-wheeler EV penetration 2026 forecast -- tool unavailable"
  - "WebSearch: India two wheeler production volume forecast 2027-2030 SIAM -- tool unavailable"
  - "WebSearch: NdFeB rare earth magnet supply shortage 2026 China export restrictions automotive -- tool unavailable"
  - "WebSearch: India two wheeler ignition system market size crore India Nippon UCAL Minda -- tool unavailable"
  - "WebSearch: China rare earth magnet export licensing automotive impact 2025-2026 -- tool unavailable"
  - "WebSearch: rare earth magnets India -- tool unavailable"
  - "WebSearch: India electric three wheeler penetration percentage 2026 -- tool unavailable"
  - "WebSearch: UCAL Fuel Systems revenue FY26 -- tool unavailable (substituted via WebFetch)"
  - "WebSearch: electric two wheeler motor controller cost BLDC India price -- tool unavailable, no substitute found (crux EV-content gap)"
  - "WebFetch: siamindia.com/statistics.aspx -- connection refused"
  - "WebFetch: grandviewresearch.com automotive-ignition-system-market -- 403 Forbidden"
  - "WebFetch: evreporter.com category ev-sales -- 404 Not Found"
downstream_candidates:
  - signal: "TVS Motor Company 2W/3W volumes and model mix"
    entity_type: "end-customer"
    demand_link: "One of INEL's 2 largest named customers (70.66% combined revenue); directly drives INEL's core revenue"
    likely_source: "BSE/NSE corporate announcements + concall transcripts + AR segment note"
    cadence: "quarterly"
    shared: false
  - signal: "Bajaj Auto 2W/3W volumes and model mix"
    entity_type: "end-customer"
    demand_link: "Same top-2-customer concentration logic as TVS Motor"
    likely_source: "BSE/NSE corporate announcements + concall transcripts"
    cadence: "quarterly"
    shared: false
  - signal: "Hero MotoCorp 2W volumes and model mix"
    entity_type: "end-customer"
    demand_link: "Named customer (BRSR Q19c); volume trend is a direct demand signal for the ICE ignition stack"
    likely_source: "BSE/NSE corporate announcements + concall transcripts"
    cadence: "quarterly"
    shared: false
  - signal: "SIAM monthly 2W/3W wholesale production and sales data"
    entity_type: "macro"
    demand_link: "Industry volume base for the entire TAM; resolves the GST-2.0 base-effect question first"
    likely_source: "SIAM website monthly statistics release"
    cadence: "monthly"
    shared: true
  - signal: "China MOFCOM rare-earth/NdFeB magnet export licensing status"
    entity_type: "macro"
    demand_link: "Threatens both the ICE flywheel-magneto franchise and the EV motor/ISG stack simultaneously"
    likely_source: "MOFCOM export-control announcements, cross-checked against DGCI&S India import data"
    cadence: "event-driven"
    shared: true
  - signal: "Vahan/FADA electric two-wheeler registration data"
    entity_type: "macro"
    demand_link: "Direct tracker for E2W penetration, which scopes the unquantified EV-content SAM lever"
    likely_source: "Vahan Parivahan dashboard / FADA monthly release"
    cadence: "monthly"
    shared: false
  - signal: "BorgWarner EFI ECU technical licensing partnership status"
    entity_type: "counterparty"
    demand_link: "Named new-product-segment entry, currently a deck-only claim with no AR corroboration"
    likely_source: "BorgWarner SEC EDGAR filings / investor relations"
    cadence: "event-driven"
    shared: false
  - signal: "GST Council / CBIC GST 2.0 rate-slab stability"
    entity_type: "regulatory"
    demand_link: "The policy event behind the FY26 volume spike this report treats as a possible base-effect risk"
    likely_source: "PIB / CBIC notifications"
    cadence: "event-driven"
    shared: true
demand_externally_verifiable: true
analyst_note: "The bottom-up TAM/SAM/SOM here is deliberately built from INEL's own disclosed numbers because no third-party India-2W content-per-vehicle report could be sourced (WebSearch down all session). The two most important findings are linked: current SAM share is already ~87% (near-saturated within today's customer/product base), and SOM-implied CAGR (5.3%) sits far below FY26/Q1FY27 delivered growth (26.5%/35.5%). Both point the same way -- either the SAM definition is too narrow (new OEMs, EV stack, faster exports would widen it) or FY26's growth is a GST-2.0 base effect that will not repeat. The EV content-per-vehicle question (does the EV stack earn more or less than the flywheel magneto it displaces) could not be resolved with tools available this session and is the single highest-priority live-web verification item for Halt 1."
```
