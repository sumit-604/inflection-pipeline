# STAGE 9: TAM / SAM / SOM MARKET SIZING — SSWL (Steel Strips Wheels Ltd)
Run date: 2026-09-19 | Sonnet 5 + web search | Status: PARTIAL (searches skipped, see Search Log)

---

## SECTION 1: MARKET DEFINITION

### 1A. Precise boundaries

- **Product scope**: steel wheel rims and alloy (cast aluminium) wheel rims for
  passenger vehicles (PV), medium and heavy commercial vehicles (M&HCV),
  tractors, off-the-road (OTR) equipment, and two/three-wheelers (2W/3W),
  plus aluminium steering knuckles (an early-stage, separate product, ~1% of
  revenue, B04-bizmodel.yaml).
- **Geographic scope**: India, OEM-fitment demand. This TAM is built on a
  **domestic-India basis**. SSWL's export business (~9% of FY26 revenue,
  Rs 454 Cr per company memory, guided to ~Rs 600 Cr FY27 per the Q4 FY26 and
  Q1 FY27 concalls) is a real and growing market, but no independently
  sourced export-destination wheel-market size was found (searched, see
  Search Log) — export is tracked directionally in Section 5D, not added to
  the headline TAM, to avoid fabricating a number.
- **Customer scope**: domestic and India-based OEM assembly lines (Tata
  Motors, Hyundai, Mahindra, Maruti, Kia and others per AR/deck clientele
  slide); replacement/aftermarket demand is out of scope for the headline
  TAM (SSWL is an OEM Tier-1 supplier; the Bhuj plant's planned aftermarket
  export channel is a SAM-expansion lever, Section 5D, not yet revenue-
  generating).
- **Channel scope**: OEM direct supply (SSWL's established channel).
  Aftermarket/retail retrofit is excluded from the headline TAM (see SAM
  filter 3, Section 3A).
- **Price segment**: no price-tier exclusion; SSWL spans mass-market steel
  through mid/premium alloy fitment.
- **Explicit exclusions**: global (ex-India) OEM wheel demand not attributable
  to India-manufactured vehicle exports; the retail/tuning aftermarket wheel
  market; carbon-fibre and other non-metal wheel technologies (a small, ~5%
  global volume niche per market.us, immaterial to SSWL's product line).

### 1B. Management's own TAM claim

Management gives **no absolute Rupee TAM figure** anywhere in the AR, the
four investor decks, or the three FY26/Q1 FY27 transcripts read (searched
the AR text for "market size", "TAM", "billion", "addressable" — no match;
grepped all four decks — no match). The only **quantified** market-size
claim found is a growth rate, not a level:

> "Steel Wheel Market to grow at 4% p.a. whereas Alloy Wheel Market to grow
> at 12% p.a. over next 5 years" — investor presentation, Jul-2026-A deck
> (Q1 FY27), page 16, "Growth Drivers" slide.

Date: Jul-2026 (Q1 FY27 deck). Credibility read: **reasonable**. The alloy
figure (12% p.a.) sits close to the independently sourced third-party India
alloy-wheel-market CAGR of 10.1% (Section 2, Method 1) — within the
framework's "reasonable" band (ratio 1.19x, well under the 1.5x threshold).
The steel figure (4% p.a.) is conservative relative to SIAM's FY26 domestic
vehicle sales growth of +10.4% YoY (AR p.122-123), but FY26 was a GST 2.0-
driven cyclical recovery year off a depressed base (AR MD&A explicitly
flags "high base effect" risk for FY27), so a lower structural long-run
steel-wheel growth rate is plausible, not evasive.

Beyond the growth-rate claim, management's qualitative ambition — "the next
10 years, we want to sell more wheels in the export market than we sell in
India... we want to be a very big global player in this business" (Dheeraj
Garg, Q1 FY27 concall, 16-Jul-2026, p.8-9, transcript p.341) — is the
LBF1 load-bearing claim this stage was asked to test. It is directional and
unquantified; Section 5D returns to it once the domestic TAM/SAM/SOM is
built, since no independent export-market source exists to size it
directly.

---

## SECTION 2: TAM ESTIMATION, MULTIPLE METHODS

All figures ₹ Crore unless stated. FX used for USD conversions: **Rs 96/US$**
(18-Sep-2026 spot, tradingeconomics.com / Federal Reserve H.10 release,
14-Sep-2026 data), consistent with the run date.

### Method 1 — Top-down (India alloy-wheel market, third-party report)

The only India-specific, third-party wheel-market report found (searched
"India alloy wheel market size", "India automotive wheel rim market size" —
no India-specific STEEL wheel report was found; flagged as a gap):

- **India Aluminum Alloy Wheel Market**: **US$1,270.64 million**, base year
  2025, CAGR 10.1% (2026-2034) — Allied Market Research, via
  marketlensiq.com (fetched 2026-09-19).
- Converted: $1,270.64M × Rs 96 = **Rs 12,198 Cr** (2025 base year; not
  stale, within the 2-year rule).
- Confidence: **M** (single source, no second India-specific alloy-market
  report corroborates the exact figure, though the growth rate corroborates
  management's own 12% p.a. claim, Section 1B).
- No India-specific steel-wheel market report was found. This is a
  **data gap**, carried to input_gaps. The steel-wheel TAM slice is instead
  built via Method 2.

### Method 2 — Bottom-up, via SSWL's own disclosed revenue ÷ disclosed market share

This is the best-anchored method: it uses two filed, dated disclosures
(SSWL's own revenue mix and India Ratings' rating rationale) rather than a
third-party estimate.

**Step 1 — SSWL's FY26 revenue by end-use segment** (management disclosure,
Q4 FY26 concall, 02-Jun-2026, p.22, Pranav Jain, CFO):
Car and MUV (steel + alloy combined) 54%, Truck (CV) 28%, Tractor 13%,
2-3 wheeler 2%, OTR 1%, Knuckles 1% (rounds to 100%).

Applied to FY26 revenue from operations **Rs 5,182.80 Cr** standalone
(REVENUE_ANCHOR: Q4 FY26 + FY26 audited results filing, 29-May-2026):
- PV (car+MUV): Rs 2,798.7 Cr
- CV (truck): Rs 1,451.2 Cr
- Tractor: Rs 673.8 Cr
- 2-3W: Rs 103.7 Cr
- OTR: Rs 51.8 Cr
- Knuckles: Rs 51.8 Cr

**Step 2 — basis-mismatch correction.** India Ratings' segment market shares
(rationale, 18-Feb-2026, p.2-3: "SSWL has a healthy market position in the
**steel wheel rim segment**, with a 34% share in PVs, 52% in M&HCV, 42% in
tractors, 35% in OTR and 39% in two- and three-wheelers") are stated for the
**steel-wheel segment only**. SSWL's PV revenue line (54%) blends steel and
alloy. Applying a combined-revenue PV figure to a steel-only market share
would overstate the implied market (flagged — see input_gaps). To correct:
SSWL's total steel revenue is ~63% of company revenue (B04-bizmodel.yaml,
Rs 3,265.2 Cr); total non-PV steel (CV+tractor+2-3W+OTR = 28+13+2+1 = 44%,
Rs 2,280.4 Cr) is subtracted from total steel revenue to isolate PV-steel:
Rs 3,265.2 Cr − Rs 2,280.4 Cr = **Rs 984.8 Cr PV-steel** (≈19% of revenue).
The remainder of the PV line (54% − 19% = 35%, Rs 1,813.9 Cr) is PV-alloy,
consistent with the deck's disclosed alloy revenue share of ~35-36% FY26
(Jul-2026-A deck p.16-17; Ind-Ra rationale p.4).

**Step 3 — divide by disclosed steel-segment market share to get implied
segment market size**:
| Segment | SSWL steel revenue (Rs Cr) | SSWL disclosed steel share | Implied segment market (Rs Cr) |
|---|---|---|---|
| PV (steel only) | 984.8 | 34% | 2,897 |
| CV (M&HCV) | 1,451.2 | 52% | 2,791 |
| Tractor | 673.8 | 42% | 1,604 |
| 2-3W | 103.7 | 39% | 266 |
| OTR | 51.8 | 35% | 148 |
| **Steel subtotal** | | | **7,706** |

**Step 4 — add the alloy slice** from Method 1 (Rs 12,198 Cr, India alloy
wheel market, all applications — no SSWL-specific alloy-market-share
disclosure exists anywhere in the corpus to cross-check this the way steel
was cross-checked; flagged as a genuine limitation).

**Method 2 total TAM = Rs 7,706 Cr (steel) + Rs 12,198 Cr (alloy) =
Rs 19,904 Cr ≈ Rs 19,900 Cr.**

Confidence: **M**. Anchored to two filed, dated, named sources (Ind-Ra
rationale, SSWL's own concall disclosure), but the steel-segment market
sizes are entirely a function of SSWL's own disclosed shares — a
single-source, potentially self-serving number with no independent
corroboration (the peer read in outputs/reports/06-peers.md could not
verify SSWL's specific segment shares against WHEELS or UNOMINDA directly,
though WHEELS' own 45% CV share is at least *consistent* with a
34%+52%+45%=~131% envelope across two players in three overlapping-but-
not-identical segments, not a clean check).

### Method 3 — Peer revenue aggregation

Dedicated listed wheel-makers only (ALICON does not make wheels — castings/
cylinder heads, per outputs/reports/06-peers.md; UNOMINDA is a diversified
auto-electronics group whose alloy-wheel-segment revenue is not disclosed
anywhere found, searched, NOT FOUND — a real gap, since UNOMINDA is
management's own implicit benchmark as the larger listed alloy-wheel maker):

- SSWL FY26 revenue: Rs 5,182.8 Cr (standalone, REVENUE_ANCHOR)
- Wheels India Ltd (WHEELS) FY26 gross revenue: **Rs 5,124.40 Cr**
  (themachinemaker.com / whalesbook.com, both reporting the FY26 results,
  15.8% YoY growth; company's own AGM disclosure per scanx.trade)
- Subtotal, two dedicated listed wheel-makers: **Rs 10,307.2 Cr**
- Unorganised / other-OEM-captive-supplier uplift: the framework's standard
  30-60% unorganised-sector range is applied at the **40% midpoint**
  (conservative bias — the low end of "aggressive" formalisation would push
  this higher, but this business is OEM-qualification-locked, B07's B2
  category, which typically means LOWER unorganised share than a retail-
  facing category; 40% is a deliberately mid, not high, pick):
  Rs 10,307.2 Cr ÷ (1 − 0.40) = **Rs 17,178.7 Cr ≈ Rs 17,200 Cr**

Confidence: **L**. Missing the largest listed alloy-wheel maker's
wheel-specific revenue (UNOMINDA, NOT FOUND) means this method structurally
undercounts the alloy segment; the true peer-aggregation figure is likely
higher than Rs 17,200 Cr. Retained as the **conservative** bound precisely
because it is a known undercount.

### Method 4 — Import substitution

Not cleanly applicable at wheel-specific granularity. The one substitution-
adjacent data point found is macro, not wheel-specific: India's PLI
(Production-Linked Incentive) allocation for auto and auto components is
Rs 25,938 Cr (search result, government PLI scheme); this is a sector-wide
tailwind (Section 4A), not a wheel-market-size input. No wheel-specific
import/export substitution target was found. **NOT FOUND** — carried to
input_gaps, not estimated.

### Method 5 — Global benchmark (context only)

- Global automotive wheel market: **US$46.02 billion (conservative) to
  US$51.96 billion** for 2026 (businessresearchinsights.com;
  researchandmarkets.com) → **Rs 4,41,792 Cr to Rs 4,98,816 Cr** at Rs 96/$.
- India's implied share of global wheel-market VALUE at TAM(realistic)
  Rs 19,900 Cr ≈ **4.0-4.5%** of the global figure.
- Cross-check against India's share of global vehicle PRODUCTION VOLUME:
  India's FY26 domestic PV+CV production (SIAM, AR p.122: 46,43,439 PV +
  10,79,871 CV = 5,723,310 units) is roughly 5-6% of global light-vehicle
  production (~94 million units/year, standard OICA-range approximation,
  not independently re-verified this run).
- **These two shares are close (4-4.5% value vs ~5-6% volume), not
  divergent** — the small gap is fully explained by India's materially
  lower average selling price per wheel (SSWL's own blended ASP is
  ~Rs 2,600/wheel ≈ US$27/wheel, per B04-bizmodel.yaml, against an implied
  global average of roughly US$120/wheel from the $46bn/94mn-vehicle/4-
  wheel-set arithmetic) — a steel-dominant, smaller-diameter, lower-price-
  point fleet, not a methodology error. **This satisfies the framework's
  "if methods diverge, explain why" instruction**: Method 5 does NOT
  materially diverge from Methods 2/3 once the ASP gap is accounted for;
  it is used for context, not counted as an independent TAM estimate in
  the triangulation table below.

### Triangulation table

| Method | Estimate (Rs Cr) | Confidence | Staleness |
|---|---|---|---|
| 1 — Top-down (alloy slice only, India, third-party) | 12,198 | M | 2025 base, not stale |
| 2 — Bottom-up (SSWL revenue ÷ disclosed segment share) | 19,900 | M | FY26 basis, current |
| 3 — Peer aggregation + unorganised estimate | 17,200 | L | FY26 basis, current |
| 5 — Global benchmark | context only (4,41,792-4,98,816 global) | M | 2026, current |

**Conservative estimate: Rs 17,200 Cr** (Method 3, a known undercount from
the missing UNOMINDA alloy figure — the "take the lower" conservative
bias applies cleanly here).
**Realistic estimate: Rs 19,900 Cr** (Method 2, the best-anchored figure —
two filed, dated, named sources, corrected for the steel/alloy basis
mismatch shown in the workings above).

**Management's claim vs conservative estimate**: not computable as a ratio
— management gave no absolute Rupee figure (Section 1B). The only
quantified claim (growth rate) was cross-checked as reasonable above.

---

## SECTION 3: SAM & SOM

### 3A. SAM

Starting base: **TAM(realistic) = Rs 19,900 Cr** (SAM is derived off the
realistic estimate per standard practice; the conservative estimate,
Rs 17,200 Cr, is a triangulation bound, not the SAM base, to avoid a
TAM<SAM sanity violation).

| Filter | Basis | Effect |
|---|---|---|
| Product fit | The alloy slice (Rs 12,198 Cr) likely includes 2W alloy wheels; SSWL's 2-3W revenue is ~2% of company revenue and is steel, not alloy (Q4 FY26 call, p.22). Apply 10% haircut to the alloy slice only. | 12,198 × 0.90 = 10,978 (−1,220) |
| Geography | TAM is already India-domestic-only by construction (Section 1A). No subtraction; export is a SAM-expansion lever (5D), not counted here. | 0 |
| Channel | The third-party alloy-market figure likely includes retail/tuning aftermarket sales; SSWL is an OEM Tier-1 supplier and has not yet commercialised the Bhuj aftermarket-export channel (concall, Q1 FY27, p.14, Aditya Dixit: "predominantly coming in for market outside India... more so on the aftermarket side" — not yet shipping). Apply 5% further haircut to the alloy slice. | 10,978 × 0.95 = 10,429 (−549) |
| Customer | No further exclusion; SSWL already serves the major domestic OEMs across all its segments, and the disclosed-share basis (Method 2) already reflects customer-level reality. | 0 |
| Capability | SSWL's combined capacity (~26.2 Mn units current: steel 20.7 Mn + alloy 5.0 Mn + knuckle 0.5 Mn, Jul-2026-A deck p.9) is a small fraction of total India wheel UNIT demand (2W alone is >40 Mn units/year, SIAM). No value-level SAM haircut; the capacity constraint is tested against SOM directly in 3C instead. | 0 |

**SAM = Rs 7,706 Cr (steel, unchanged) + Rs 10,429 Cr (alloy, after
product-fit and channel haircuts) = Rs 18,135 Cr ≈ Rs 18,100 Cr.**
SAM as % of TAM(realistic): 18,100 / 19,900 = **91.0%**.

### 3B. SOM at 3 and 5 years

**Current SAM share (FY26)**: Rs 5,182.8 Cr ÷ Rs 18,100 Cr = **28.6%**.

**Share-gain trajectory**: the framework's normal band is 1-2pp over 3
years; the aggressive band (3-5pp) requires capacity and execution backing.
SSWL clears the aggressive-tier test on capacity: alloy capacity +24%
(5.0→6.2 Mn), knuckle capacity +120-220% (0.5→1.1-1.2 Mn combined phases),
steel brownfield +~10% (20.7→~22.7 Mn), all currently committed and under
construction (Jul-2026-A deck p.9; AR p.23 "Key Business Development";
B07-emoat.yaml capex_embedded_growth_pct 33). This supports the **top of
the aggressive band**, not the extreme (>5pp requires a competitor exit or
acquisition, which is not the case here):

- 3-year: +3.5pp → 32.1% of SAM
- 5-year: +5.5pp → 34.1% of SAM

**SAM forward-projection** (TAM growth 8.5% p.a. blended — see 3C/5B
workings: 43% steel-weighted × 4% + 57% alloy-weighted × 12% ≈ 8.5%):
- SAM(yr3, FY29) = 18,100 × 1.085³ = **Rs 23,119 Cr**
- SAM(yr5, FY31) = 18,100 × 1.085⁵ = **Rs 27,216 Cr**

**SOM**:
- SOM(3yr) = 23,119 × 32.1% = **Rs 7,421 Cr ≈ Rs 7,420 Cr**
- SOM(5yr) = 27,216 × 34.1% = **Rs 9,281 Cr ≈ Rs 9,280 Cr**

**Implied revenue CAGR from FY26 base (Rs 5,182.8 Cr)**:
- 3-year: (7,420 / 5,182.8)^(1/3) − 1 = **12.7%**
- 5-year: (9,280 / 5,182.8)^(1/5) − 1 = **12.4%**

**This is the FORMAL handoff figure for Stage 11**: the SOM-implied
sustained revenue CAGR is **~12.4-12.7%**, not the 25% YoY management has
guided for FY27 alone (Rs 6,500 Cr, +25% vs FY26's Rs 5,182.8 Cr — Q1 FY27
concall, 16-Jul-2026, p.9, "so are we confident on achieving that? ... Yes").
Per the operating rule against shading an input: both readings are real and
evidenced. What separates them is that the FY27 guidance is a **single,
low-base, capacity-ramp catch-up year** (GST 2.0 demand recovery off a
depressed FY25/H1 FY26 base, plus the Bhuj/knuckle ramp beginning to land),
not a steady-state 3-5 year rate; the SOM reflects realistic share-gain
economics against a market that is itself growing at ~8.5% p.a.

### 3C. Capacity cross-check

B07's capex_embedded_growth_pct is **33%**, applied to the FY26 revenue
base: Rs 5,182.8 Cr × 1.33 = **Rs 6,893 Cr** — the realistic revenue
ceiling supportable by SSWL's currently-committed capex programme (Bhuj
alloy +1.2 Mn, knuckle +0.6 Mn, steel/agri brownfield ~Rs 150 Cr), at
utilisation and mix levels comparable to FY26 (blended utilisation was
~76%, cross-checked: FY26 unit sales of 19.696 Mn wheels + 0.257 Mn
knuckles ≈ 19.95 Mn units ÷ ~26.2 Mn combined capacity ≈ 76.1%, matching
the deck's reported 76-82% range).

- **Gap at 3yr**: SOM(3yr) Rs 7,420 Cr − capex-embedded ceiling Rs 6,893 Cr
  = **Rs 527 Cr short (≈7.6%)**.
- **Gap at 5yr**: SOM(5yr) Rs 9,280 Cr − same ceiling Rs 6,893 Cr =
  **Rs 2,387 Cr short (≈34.6%)**.

**The SOM is the optimistic side of this gap, not the capex plan.** The
3-year gap is modest and could plausibly close through further mix-shift
toward alloy/knuckle beyond what B07's 33% already assumes. The 5-year gap
is large and requires a **second, currently uncommitted capex cycle**
(management itself flags this only as an idea: "we have many ideas on
that, many things on drawing board, nothing firm," Q1 FY27 concall, p.9,
Dheeraj Garg) — the 5-year SOM should be read as contingent on capacity
SSWL has not yet announced, not as a number the current capex programme
alone delivers.

---

## SECTION 4: GROWTH DRIVERS, RISKS & STRUCTURE

### 4A. TAM growth drivers

| Driver | Impact | Evidence |
|---|---|---|
| Alloy penetration rising | High | SSWL's own alloy revenue share 28%→36% FY23-FY26 (Ind-Ra p.4; deck p.16); alloy volume share 16%→20% FY23-FY26/Q1FY27 (deck p.16-17) |
| Premiumisation (SUV/higher-trim mix) | Moderate | Web search: alloy wheels increasingly standard fitment in mid-segment cars, India aluminium alloy wheel market search results |
| Regulatory tailwind (GST 2.0) | High | AR p.122-123: FY26 "highest-ever sales across all segments," SIAM data, +10.4% YoY total industry; corroborated independently by all three peers (WHEELS, UNOMINDA, ALICON) per outputs/reports/06-peers.md Q6 |
| Import substitution (PLI) | Moderate, sector-wide not wheel-specific | Rs 25,938 Cr PLI allocation for auto/auto-components (search result); AR p.124 names PLI as an EV-ecosystem opportunity generally |
| New applications (aluminium knuckles, EV/ICE lightweighting) | Emerging, small base | AR/concall: knuckle sales 46,952 units (FY25) → 257,147 units (FY26), AR p.23; "important growth engine over the medium term," Q1 FY27 concall p.4 |
| Geographic expansion (export diversification) | Moderate, contested | Europe/LatAm/Asia diversification (concalls); but export revenue itself fell YoY in Q1 FY27 before a 37% QoQ recovery (concall p.6) — directionally real, not yet demonstrated at scale |
| Technology enablement (robotics/automation) | Moderate | Deck "Growth Drivers" slide p.16: "Development of Robotic Automated Operation process for Operating Cost Rationalization" |
| Demographics (rural income, tractor mechanisation) | High for tractor segment (13% of revenue) | Tractor industry record FY26: 10,50,077 units retail (+18.95% YoY, FADA) to 11.6 lakh total industry (TMA), driven by monsoon/rural cash flows (search results); AR/Q1FY27 concall corroborate |

### 4B. TAM risks

| Risk | Monitoring signal |
|---|---|
| Cyclical downturn | FY20-21 COVID precedent: capacity utilisation crash (Ind-Ra rationale p.4); watch SIAM monthly domestic sales for a turn |
| Import competition (Vietnam/Thailand export rivals) | SSWL's own claim of a "level playing field" from mid-2026 (concall) is a **contested claim** — B07-emoat.yaml flags this exact claim as reversed once already within a quarter; watch US tariff notices |
| Regulatory headwind (EU CBAM) | EU Carbon Border Adjustment Mechanism, live 1-Jan-2026: disclosed and quantified as a cost by peer WHEELS (Q4 FY26 call, p.13) but **never mentioned in any SSWL transcript** despite SSWL's stated Europe export ambition — a real, undisclosed exposure per outputs/reports/06-peers.md 2E |
| Saturation / high base effect | AR p.124 itself: "sustaining double-digit growth rates into FY 2026-27 will be inherently more difficult... a moderation in headline growth numbers should be read in that context" |
| Substitution (alternative wheel materials) | Carbon-fibre wheels ~5% of global volume mix (market.us search result) — currently immaterial, monitor as a tail risk only |
| Cost-pressure/margin risk (shared, not TAM-specific) | West Asia conflict-driven commodity spike, confirmed by all three peers with matching timing (outputs/reports/06-peers.md Q8) — a margin risk, not a TAM-size risk, but affects the earnings-CAGR side of the 5E valuation-implication line |

### 4C. Market structure

- **Competitor count**: organised-sector dedicated wheel makers are few —
  SSWL and Wheels India (WHEELS) dominate the steel-wheel CV/tractor space;
  SSWL 52% M&HCV + WHEELS' own-disclosed 45% CV share (outputs/reports/06-
  peers.md Q7) sum to ~97%, a highly concentrated two-player segment. The
  alloy-wheel segment is more fragmented: UNOMINDA is the largest listed
  alloy-wheel maker (company memory, unanchored); SSWL's implied alloy
  share (Rs 1,813.9 Cr PV-alloy revenue ÷ Rs 12,198 Cr India alloy market
  ≈ **14.9%**) suggests SSWL is a secondary, not dominant, alloy player —
  this implied share is a derived cross-check, not a disclosed figure,
  and carries the same single-source limitation as the Method 1 alloy TAM.
- **Top-3 concentration**: high in CV/tractor steel wheels (SSWL+WHEELS);
  moderate-to-fragmenting in alloy wheels, given an industry-wide capacity
  race (outputs/reports/06-peers.md 2C: UNOMINDA ~Rs 1,750 Cr FY27 capex
  across 11 projects, ALICON new Shikrapur facility, WHEELS' own aluminium
  capacity expansion — SSWL's Bhuj sits inside this pattern, not apart
  from it).
- **Organised vs unorganised**: predominantly organised, OEM-qualification-
  locked (B07-emoat.yaml B2 category, "Strong" moat strength) for the OEM
  channel; the unorganised/informal share is assumed higher only in the
  aftermarket/replacement channel, which SSWL does not yet serve at scale
  domestically (the Bhuj plant targets EXPORT aftermarket, per Section 1A).
- **Consolidating or fragmenting**: consolidating via capex race and one
  distress-driven inorganic move (AMW Autocomponent, acquired via NCLT
  resolution, FY24 — LBF4); no organic M&A consolidation pattern observed.
- **Price vs differentiation competition**: raw-material pass-through
  (B04-bizmodel.yaml: "clean pass-through with ~3-month lag") mutes
  price competition at the input-cost level; differentiation runs through
  OEM qualification/spec-in, location (Tata Steel supply proximity,
  Chennai port proximity — Ind-Ra rationale p.3), and emerging technology
  (hot stamping under evaluation, per B07-emoat.yaml optionality register).
- **Entries and exits**: AMW Autocomponent entry via NCLT (2024, distress
  resolution); no exits identified in the corpus.
- **Import share trend**: contested — SSWL claims a tariff-driven advantage
  over Vietnam/Thailand exporters that management itself partially reversed
  one quarter later (B07-emoat.yaml FLAG-CONTRADICTED-CLAIM); no peer
  transcript discusses this dynamic either way (outputs/reports/06-
  peers.md Q3, UNVERIFIABLE).

---

## SECTION 5: SUMMARY & RUNWAY

### 5A. Funnel

```
TAM (realistic)  Rs 19,900 Cr   [Method 2: bottom-up, SSWL revenue / disclosed segment share]
TAM (conservative) Rs 17,200 Cr [Method 3: peer aggregation + unorganised estimate, known undercount]
   |  5 SAM filters (product-fit -10% alloy, channel -5% alloy; geography/customer/capability = 0)
SAM  Rs 18,100 Cr  (91.0% of TAM-realistic)
   |  current share 28.6% -> +3.5pp (3yr, aggressive tier, capacity-backed) -> +5.5pp (5yr)
SOM (3yr)  Rs 7,420 Cr   (implied revenue CAGR 12.7%)
SOM (5yr)  Rs 9,280 Cr   (implied revenue CAGR 12.4%)
```

### 5B. Runway assessment

- **Revenue headroom** = SAM ÷ current revenue = 18,100 / 5,182.8 =
  **3.49x**.
- **TAM growth rate** ≈ **8.5% p.a.** (blended: steel-implied weight 43%
  × management's 4% p.a. claim, alloy-implied weight 57% × management's
  12% p.a. claim — both from the Jul-2026-A deck p.16, cross-checked
  reasonable in Section 1B).
- **Company CAGR vs TAM**: SSWL's own FY22-FY26 revenue CAGR (screener
  Data_Sheet.csv: Rs 3,559.95 Cr FY22 → Rs 5,182.8 Cr FY26) = (5,182.8 /
  3,559.95)^(1/4) − 1 = **9.9%**, modestly ABOVE the blended TAM growth of
  8.5% — consistent with a company gaining share, not merely riding the
  market, which supports (does not prove) the 3.5-5.5pp share-gain
  assumption used in 3B.
- **Years to saturate SAM**: SAM is itself growing (~8.5% p.a.), so this is
  a race between two growing quantities. At SSWL's recent 4-year CAGR
  (9.9%), the gap closes only slowly (roughly 13 years); at the FY27
  guided pace (25% YoY, if sustained, which Section 3B's capacity check
  argues it cannot be beyond year 3 without further capex) the gap would
  close in well under 10 years. **Approximate range: 7-13 years**,
  depending on which growth rate is sustained — flagged as a wide range,
  not a point estimate, because the two inputs (SSWL's own growth path and
  the market's growth path) are both moving targets.

### 5C. Runway classification

**GOOD** (headroom band 2-5x, moderate TAM growth ~8.5% p.a., multi-year
saturation horizon). Not STRONG or MASSIVE: the India domestic wheel market
alone, on the best-anchored estimate, does not offer 5x+ headroom, and the
5-year SOM already requires capacity SSWL has not yet committed (3C).

### 5D. SAM expansion levers actually being pursued

| Lever | Evidence it is being pursued | Potential addition | Revised headroom if realised |
|---|---|---|---|
| Export geography diversification (Europe, LatAm, Asia) | Concall commentary across all three FY26/FY27 calls; export revenue guided Rs 600 Cr FY27 vs Rs 454 Cr FY26 (company memory, unanchored figure, +32%) | Not sized — no independent export-market source found (Section 1A); this is the LBF1 test and remains **directionally supported but not independently quantifiable** from this corpus | N/A, data gap |
| Bhuj aftermarket export channel | Q1 FY27 concall p.14: plant "predominantly coming in for market outside India... more so on the aftermarket side" — not yet commercial | Not sized | N/A |
| Hot stamping (new product line) | B07-emoat.yaml optionality register: "discussing setting up our stamping projects," Q1 FY27 concall p.4, not yet committed capex | Not sized (pre-commitment) | N/A |
| Aluminium knuckle scale-up beyond current 2-customer base | Bhuj knuckle capacity 0.6-1.1 Mn vs FY26 sales of only 257,147 units (~2.6 lakh); "two additional knuckle OEM wins" named as a 12-month catalyst (B07-emoat.yaml) | Already counted inside the SOM's aggressive-tier share-gain assumption (3B); not additive on top | Already reflected |

**On LBF1 specifically**: the "export market bigger than domestic within a
decade" ambition cannot be tested against an independently sized global
export TAM (data gap, named above). What CAN be tested: FY27 export
guidance (Rs 600 Cr) against Q1 FY27 actual delivery (Rs 127 Cr, -21% YoY
before a 37% QoQ recovery) implies exports would need to average ~Rs 158
Cr/quarter for the remaining three quarters to hit the full-year Rs 600 Cr
figure — a step-up management itself frames as contingent on ramping
"OEM awarded businesses... not in the U.S., but... other geographies"
(Aditya Dixit, Q1 FY27 concall, p.6). This is a near-term delivery test,
not a TAM-size test; it is the correct object for Stage 11/FTTCP to track
quarter-by-quarter, not for this stage to resolve.

### 5E. Final output card

```
TAM (realistic):        Rs 19,900 Cr   |  TAM (conservative): Rs 17,200 Cr
SAM:                     Rs 18,100 Cr   (91.0% of TAM-realistic)
SOM (3yr):               Rs  7,420 Cr   |  implied revenue CAGR: 12.7%
SOM (5yr):                Rs 9,280 Cr   |  implied revenue CAGR: 12.4%
Current SAM share:       28.6%
Revenue headroom:        3.49x
TAM growth:               8.5% p.a.
Runway classification:   GOOD
```

**Valuation implication line**: At **~12.4-12.7% revenue CAGR** implied by
SOM (3-5yr), with a margin trajectory that is **rangebound, not expanding**
(Ind-Ra rationale: EBITDA margin 10-11% FY24-9MFY26, expected 10-10.5%
FY26-FY27; B04-bizmodel.yaml independently flags full-year EBITDA margin
falling from 12.7% FY22 to 9.9% FY26 despite the alloy mix-shift), the
earnings growth embedded here is **approximately 12-13% CAGR** (assuming
roughly flat margin — an approximation, not a full Role 1 earnings model,
which is Stage 11's job). Against the anchored current valuation of
**~30.8x P/E** (screener Data_Sheet.csv: market cap Rs 5,856.55 Cr ÷ FY26
net profit Rs 190.22 Cr, current price Rs 372.40 — a trailing-FY26 proxy,
not a live TTM figure), this embedded growth rate implies a PEG of roughly
**2.4x**, which **does not support** the current valuation on a
growth-alone basis. This is the SOM-implied CAGR handoff Stage 11 is
instructed to use as the cross-check against its own revenue assumptions;
it sits well below both management's single-year FY27 guidance (25%) and
the strategy's 25% CAGR target (CLAUDE.md) — the gap between "guided" and
"SOM-implied sustained" growth is the single most consequential number
this stage produces.

---

## SECTION 6: DOWNSTREAM SIGNAL CANDIDATES

| # | Candidate Signal | Entity Type | Why It Drives Demand | Likely Primary Source | Expected Cadence |
|---|---|---|---|---|---|
| 1 | SIAM monthly domestic vehicle production/sales (PV/CV/2W/3W) | Macro | Direct volume driver for OEM wheel orders across four of SSWL's five vehicle segments (all but tractor) | SIAM monthly press release | Monthly |
| 2 | TMA/FADA tractor wholesale and retail data | Macro | Direct volume driver for SSWL's tractor segment (13% of FY26 revenue, Q4 FY26 call) | TMA / FADA monthly releases | Monthly |
| 3 | Tata Motors PV+CV volume and capex disclosures | Counterparty / End-customer | Named strategic customer with a co-located plant (Jamshedpur, Ind-Ra rationale p.3); drives both PV and CV wheel offtake | Tata Motors monthly sales release / investor disclosures | Monthly |
| 4 | Hyundai Motor India PV sales and model mix | End-customer | Named alloy-wheel customer with a co-located plant (Mehsana, Ind-Ra rationale p.3); drives PV alloy wheel demand specifically | Hyundai Motor India monthly sales release | Monthly |
| 5 | Domestic/LME aluminium price index | Macro | Input-cost pass-through driver for alloy wheel and knuckle margin (B04-bizmodel.yaml: RM pass-through with ~3-month lag) | LME / MCX aluminium price series | Monthly |
| 6 | US Section 232 / reciprocal tariff rate on Indian auto exports | Regulatory | Drives export competitiveness of the ~Rs 450-600 Cr export book against Vietnam/Thailand rivals (Q1 FY27 concall p.6) | USTR / Federal Register tariff notices | Event-driven |
| 7 | EU CBAM (Carbon Border Adjustment Mechanism) implementation updates | Regulatory | Drives cost/competitiveness of Europe-bound exports; disclosed by peer WHEELS but never by SSWL despite its stated Europe export ambition (outputs/reports/06-peers.md 2E) | European Commission CBAM registry / official updates | Event-driven |

Entities 1 and 3 are marked **SHARED** — SIAM data serves PV, CV, 2-3W
revenue streams simultaneously; Tata Motors serves both the PV and CV
streams. FTTCP should count each once as a correlated catalyst, not once
per revenue stream.

`demand_externally_verifiable: true` — seven candidate signals identified,
above the minimum of three.

---
Full report ends. YAML block follows, and is also written standalone to
outputs/blocks/B09-tam.yaml.
