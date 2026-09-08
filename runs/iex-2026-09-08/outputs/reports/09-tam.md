# Stage 9 — TAM / SAM / SOM: Indian Energy Exchange Ltd (IEX)

Run date 2026-09-08. Model claude-sonnet-5 + web search.

## SECTION 1: MARKET DEFINITION

### 1A Precise boundaries

IEX does not sell electricity. It sells a matching service and charges a
transaction fee per unit of electricity that clears on its platform. The
honest market for a fee-taking exchange is the FEE POOL available on the
volume it can plausibly move across its books, not the rupee value of the
power itself.

- **Product scope.** Exchange-based trading of physical short-term
  electricity in India: Day-Ahead Market (DAM), Real-Time Market (RTM),
  Term-Ahead Market/DEEP (TAM), Green DAM/TAM, plus Renewable Energy
  Certificates (REC) and Energy Saving Certificates (ESCerts). Excluded
  from the core figure: long-term PPA-based power (structurally
  non-exchange-tradable, two-part tariff), and treasury/investment income
  (non-operating, B04 flag).
- **Geographic scope.** India only. One national grid, CERC as sole
  regulator (One Nation One Grid, AR p.46).
- **Customer scope.** DISCOMs, conventional and renewable generators,
  open-access C&I consumers, and traders eligible under CERC power-market
  regulations. IEX already has 9,100+ registered participants across
  5,300+ C&I, 120+ Discoms, 1,100+ conventional generators, ~3,000 RE
  generators/obligated entities (Investor Presentation Jul-2026, p.10).
- **Channel scope.** The power-exchange channel specifically, as distinct
  from bilateral trades, energy-trader-intermediated trades, and the
  Deviation Settlement Mechanism (DSM) — all three sit inside the
  short-term market (STM) but outside any exchange today.
- **Price segment.** Not applicable; CERC sets a fee ceiling, not a price
  tier (see risk section).
- **Explicit exclusion.** Gas (IGX), coal (Indian Coal Exchange) and
  carbon (Indian Carbon Exchange) are sized SEPARATELY in this report as
  option pools. They are not folded into tam_cr/sam_cr/som because none
  is at run-rate revenue today, and one (coal) is not yet licensed to IEX
  specifically (B07 gap, coal_exchange_licence_status).

### 1B Management's own TAM claim

"We did some estimation on this and what we feel is that almost about 25
percent of the total generation... that is the market size, opportunity
size, maybe in the next five, six years, it can be that kind of
opportunity... the short-term market, which is almost about 14-15
percent [of total generation]... is on the exchange platform" — CMD Satya
Narayan Goel, IEX Analyst Meet, 24-Jul-2026 (Concall Jul-2026 transcript,
p.32).

Definition: exchange-traded electricity volume as a percentage of
India's TOTAL national generation, rising from ~14-15% today to ~25% in
5-6 years (roughly FY32).

Date: 24-Jul-2026, given once, verbally, in response to an analyst
question. Not repeated in the AR, not in a written filing, no bottom-up
build shown.

Credibility read: **BROAD**. It is a round number ("almost about 25
percent") without an underlying build, delivered in the same style as the
20-40% DAM-coupling-impact figure that B05 already scored against
management (grade C, given once, not defended under direct questioning).
Section 2 tests it against an independent build.

---

## SECTION 2: TAM ESTIMATION, MULTIPLE METHODS

All revenue figures use the identity verified against FY26 actuals:
**Revenue (Rs Cr) = Volume (Billion Units, BU) x Fee (paise/kWh)**.
Check: 141 BU x 3.96 paise = Rs558.4cr, against the actual disclosed
electricity transaction-fee revenue of Rs558.51cr (AR p.211, Note 28) —
the identity holds to within rounding.

### Method 1 — Top-down (subtract the non-tradable slice)

- Total electricity generation, FY26: **1,848 BU** (AR p.47, CERC/CEA
  data cited in the AR's own MD&A).
- Subtract long-term-PPA-locked, captive, and must-run generation —
  structurally NOT exchange-tradable because of two-part tariff PPA
  design (B04 archetype note; management confirms India will "have
  long-term contracts" as the dominant structure, Concall Jul-2026 p.32).
  What is left is CERC's own short-term-market (STM) figure.
- Short-term market, FY26: **302 BU**, up from 238 BU in FY25 (AR p.47,
  citing CERC). The AR states this is "13% of total generation of 1,848
  BU" — the arithmetic (302/1,848) actually computes to **16.3%**, an
  internal AR inconsistency flagged here and not resolved by this stage.
- Apply the fee. Conservative (management's own stated net rate, held
  steady 4 years, Concall Apr-2026 p.14-15): 3.6 paise/kWh. Realistic
  (FY26 actual blended, AR-derived): 3.96 paise/kWh.
- **TAM (Method 1) = 302 BU x fee = Rs1,087cr (conservative) to
  Rs1,196cr (realistic).**

### Method 2 — Bottom-up (unit economics)

- Addressable unit: 1 kWh of short-term electricity (separately, 1 REC /
  1 ESCert for certificates, not built here for lack of a per-unit fee
  disclosure — see input gaps).
- Total units in the relevant market: STM 302 BU FY26 (as above).
- Current penetration by ALL exchanges (IEX + PXIL + HPX): 60% of STM,
  with bilateral trades at 26% and DSM at 13% (AR p.47).
- IEX's own current volume: 141 BU (AR p.48), which is 46.7% of total
  STM and 78.1% of the exchange-traded slice of STM (141 / (0.60 x 302)
  = 141 / 181.2), consistent with the 80-85% aggregate IEX-of-exchanges
  share disclosed verbally (Concall Jul-2026 p.4, per B04 gap note).
- Current market (IEX actual) = 141 BU x 3.96p = Rs558.4cr — matches
  disclosed Rs558.51cr, cross-check passes.
- Full-penetration TAM (100% of STM through exchanges, at today's fee) =
  302 BU x fee = **Rs1,087cr (conservative) to Rs1,196cr (realistic)** —
  identical to Method 1, as expected since both use the same STM base.

### Method 3 — Peer / channel aggregation

Named peer volume and revenue disclosures for PXIL and HPX are NOT FOUND
in the corpus or via web search (searches_skipped). An implied estimate:
if IEX is 78-85% of exchange-traded STM (181.2 BU), PXIL+HPX together
trade roughly 27-40 BU. At a broadly similar regulated fee (~3.6-3.9p,
same CERC ceiling applies to all licensed exchanges), implied peer
revenue is roughly Rs100-155cr, and implied total exchange-sector revenue
(IEX + peers) is roughly Rs660-715cr — close to 181.2 BU x ~3.7-3.9p =
Rs670-706cr, an internal cross-check that holds.

The "unorganised" analogue here is the 39% of STM (bilateral 26% + DSM
13%, AR p.47) that sits OUTSIDE any exchange today — squarely inside the
30-60% band the prompt flags as typical for an Indian unorganised segment
still formalising, which is the structural basis for the 100%-penetration
TAM ceiling used in Methods 1-2.

### Method 4 — Import substitution

Not applicable. IEX is a domestic fee-taking service, not a good with an
import/domestic-production dynamic.

### Method 5 — Global benchmark

- Europe: EPEX day-ahead trading covered ~39% of German/Austrian load,
  and Nord Pool day-ahead covered >85% of Nordic load — both **2013 data,
  STALE (>4 years old), direction only** (Monopolkommission Germany
  competition report).
- China: market-based electricity transactions rose from 17% to 63% of
  consumption between 2016 and 2024 (RMI China Power Market Outlook
  2025/2026) — but "market-based" in China is dominated by bilateral
  medium/long-term (M2L) contracts, not spot-exchange trades, so this is
  a weak read-across to IEX's exchange-specific model. Recent (2024),
  usable for direction, not for a number.
- Read: both benchmarks show mature/reforming power markets can push
  well past 25% penetration over a decade-plus horizon, which makes
  management's 25%-of-generation aim directionally plausible over a long
  enough window, but neither benchmark validates a 5-6 year timeline, and
  neither is structured the way India's PPA-dominated market is.

### Triangulation table

| Method | Estimate (Rs Cr) | Confidence | Staleness |
|---|---|---|---|
| 1. Top-down (STM x fee) | 1,087 (cons.) – 1,196 (real.) | H | current (FY26) |
| 2. Bottom-up (unit econ.) | 1,087 – 1,196 (same base) | H | current (FY26) |
| 3. Peer aggregation | ~660-715 (current capture only, not a TAM) | M | current, peer figures estimated not disclosed |
| 4. Import substitution | N/A | — | — |
| 5. Global benchmark | directional only, no Rs Cr number | L | 2013 (stale) / 2024 |

**Conservative TAM: Rs1,087cr. Realistic TAM: Rs1,196cr.**

### Management claim vs conservative estimate

Management's claim is forward (FY32, ~6 years out), so it is tested
against an equally forward independent TAM, not today's snapshot:

- STM, grown at its own 15-year trend CAGR of 8.9% (AR p.47) to FY32:
  302 x 1.089^6 = **504 BU**.
- STM as % of FY32 total demand (2,700 BU, management's own figure,
  Concall Jul-2026 p.5, sourced to CEA's Long Term National Resource
  Adequacy Plan): 504/2,700 = **18.7%** — well short of the ~25-40%
  STM-of-generation ratio management's claim implicitly requires (25%
  exchange-of-generation, divided by a 60-100% STM-to-exchange
  penetration range, backs out an STM share of 25-42% of total
  generation).
- Independent forward TAM at FY32 (100% exchange capture of a
  trend-grown STM): 504 BU x 3.6p (conservative) = **Rs1,814cr**.
- Management's implied claim: 25% x 2,700 BU = 675 BU traded via
  exchange x 3.96p (today's fee, giving management the benefit of no fee
  compression) = **Rs2,673cr**.
- **mgmt_claim_ratio = 2,673 / 1,814 = 1.47x → "within 1.5x, reasonable"
  by the standard read — but only just, and only because the comparison
  already credits management with an STM that grows past its own
  15-year trend.** The claim is not inflated on its face, but it is not
  free money either: it requires the short-term market itself, not just
  exchange share within it, to outgrow its own history.

---

## SECTION 3: SAM & SOM

### 3A SAM

Applying the five filters to the conservative TAM (Rs1,087cr):

| Filter | Cut | Reasoning |
|---|---|---|
| Product fit | 0% | IEX already operates DAM, RTM, TAM, Green DAM/TAM — the segments that make up the STM base used in Section 2. Pending products (Green RTM, Peak DAM/RTM, 11-month TAM) are ADDITIVE, not already inside the 302 BU base, so no cut, no double count. |
| Geography | 0% | India-only is already the TAM's scope. |
| Channel | 0% | The exchange channel is already the TAM's 100%-capture definition. |
| Customer | 0% | 9,100+ participants already onboarded across every eligible counterparty class (p.10). |
| Capability | 15% | Even at full STM penetration, IEX is not a monopoly: PXIL and HPX hold licences to the same channel, and CERC's market-coupling design (Grid India as neutral Market Coupling Operator for DAM) is built to level, not concentrate, access. A realistic ceiling for ONE exchange, even the incumbent, is below 100% of a fully-penetrated STM. |

**SAM (conservative) = Rs1,087cr x 0.85 = Rs924cr. SAM (realistic) =
Rs1,196cr x 0.85 = Rs1,017cr. SAM as % of TAM = 85%.**

### 3B SOM at 3 and 5 years

STM volume projected forward at its own 8.9% trend CAGR (AR p.47),
conservative fee held flat at 3.6p, 85% capability ceiling applied
throughout:

- STM FY29 (3yr): 302 x 1.089^3 = 390 BU. SAM_FY29 = 390 x 3.6p x 0.85 =
  **Rs1,193cr**.
- STM FY31 (5yr): 302 x 1.089^5 = 463 BU. SAM_FY31 = 463 x 3.6p x 0.85 =
  **Rs1,415cr**.

**Share-of-SAM trajectory, given as a range because of the coupling
risk (per the task's explicit instruction):**

- Current share of SAM: Rs558.51cr / Rs924cr = **60.4%**.
- **Downside (coupling-stress) case.** DAM is 39% of IEX's FY26
  electricity VOLUME mix (Investor Presentation Jul-2026, p.12; no
  revenue-basis split exists, B04/B07 gap, so this is a volume-to-revenue
  proxy). Applying that share to FY26 electricity revenue: DAM ≈ 0.39 x
  Rs558.51cr = Rs217.8cr. Management's own worst-case coupling impact on
  DAM, given verbally and undefended (Concall Jul-2026 p.5): 40%. Impact
  = -0.40 x Rs217.8cr = -Rs87.1cr. Revenue falls to Rs471.4cr, which is
  471.4/924 = **51.0% of SAM**. Held flat (structural, not one-time) for
  both year 3 and year 5.
- **Base case.** Normal share-gain rule (1-2pp in 3 years) applied
  instead of the coupling stress, reflecting new-product volume (Green
  RTM, Peak DAM/RTM, 11-month TAM, once approved) offsetting DAM
  softness the way RTM already offset the DAM share fall from 95% (FY16)
  to 39% (FY26) without net revenue harm: 61% at year 3, 62% at year 5.

| | SAM (Rs Cr) | Share of SAM | SOM (Rs Cr) |
|---|---|---|---|
| Yr3 downside | 1,193 | 51% | **609** |
| Yr3 base | 1,193 | 61% | 728 |
| Yr5 downside | 1,415 | 51% | **722** |
| Yr5 base | 1,415 | 62% | 878 |

Per the CONSERVATIVE BIAS rule, **som_3yr_cr = Rs609cr, som_5yr_cr =
Rs722cr** are the reported point figures; the base case (Rs728cr /
Rs878cr) is carried as the upside scenario.

**Implied revenue CAGR (from current Rs558.51cr electricity segment
revenue):**
- Yr3: downside (609/558.51)^(1/3)-1 = **2.9%**; base (728/558.51)^(1/3)-1
  = 9.2%.
- Yr5: downside (722/558.51)^(1/5)-1 = **5.3%**; base (878/558.51)^(1/5)-1
  = 9.5%.

Reported (conservative): **som_implied_revenue_cagr yr3 = 2.9%, yr5 =
5.3%.**

### 3C Capacity cross-check

`capex_embedded_growth_pct = 0` (B07) is not an error; IEX grows by
adding traded volume on an existing software platform, not by
commissioning physical capacity, so there is no capex plan to
cross-check against. Reasoned in platform terms instead:

- **Throughput.** No disclosed system outage or capacity breach; the
  platform already clears record single-day volumes (e.g. 250 MU RTM in
  a single day, 30-Apr-2026, per web search) without incident. Not the
  constraint.
- **Regulatory approval.** The real gate on SOM delivery is CERC product
  approval, not engineering capacity: Green RTM, Peak DAM/RTM, and the
  11-month TAM contract are all "order reserved" with CERC, several 2+
  years overdue (B07 catalysts_12m). Until approved, the additive volume
  those products would unlock (management sizes the 11-month TAM alone
  at 15-20 BU; IEX's own DEEP platform already trades ~40 BU bilaterally
  that could shift to exchange under the 11-month contract, Investor
  Presentation Jul-2026, p.21) sits outside both TAM and SAM as
  constructed here.

**capacity_check: sufficient** — platform throughput is not the
constraint; the binding constraint is regulatory approval timing, which
this stage cannot forecast and which stage 11 should treat as a
timing risk on the upside case, not a capacity gap on the downside case.

---

## SECTION 4: GROWTH DRIVERS, RISKS & STRUCTURE

### 4A TAM growth drivers

| Driver | Impact | Evidence |
|---|---|---|
| Penetration (STM as % of generation, and exchange as % of STM) | Medium-High | STM grew 238→302 BU FY25→FY26 (+26.9%, above its own 8.9% trend, AR p.47); exchange share of STM at 60% (AR p.47), up from a much lower base historically. |
| Per-capita / demand growth | High | CEA target 2,000 kWh per capita by 2030, 4,000 kWh by 2047 (Investor Presentation p.5); total demand 1,708 BU FY26 → 2,700 BU FY32 (CEA LTNRAP, Concall Jul-2026 p.5) → 3,365 BU by FY35-36 (CEA LTNRAP, web search). |
| Regulatory tailwind | Medium, two-sided | New product approvals (Green RTM, Peak DAM/RTM, 11-month TAM) expand the addressable base; market coupling and the CERC fee review (Section 4B) work the other way. |
| Formalisation | Medium | Bilateral (26%) and DSM (13%) trades, 39% of STM, sit outside any exchange today and are the natural conversion pool behind the 100%-penetration TAM ceiling (AR p.47). |
| New applications | Medium | BESS/Peak contracts, VPPA, LPSC-driven URS supply (8.0 BU FY26 cleared, Investor Presentation p.21), carbon trading foundation (CCTS) — all additive to the core electricity base, not yet in the numbers above. |
| Technology enablement | Low-Medium | AI-enabled bidding/analytics tools deepen member stickiness but do not, on present disclosure, expand addressable volume. |
| Geographic expansion | Low | India-only market; Cross-Border Electricity Trading (CBET, 43+ portfolios) is a small extension, not a new geography for the fee-pool math. |

### 4B TAM risks

1. **Market coupling (DAM).** CERC ordered day-ahead coupling Jul-2025;
   APTEL declined to set it aside 13-Feb-2026; Supreme Court admitted the
   appeal but refused a stay 27-Jul-2026 (company memory, sourced
   business-standard.com and solarquarter.com). Management's own
   verbal impact range on DAM volume: 20-40% (Concall Jul-2026, p.5),
   never defended under direct questioning, never filed. Monitoring
   signal: final CERC coupling regulation text and its DAM fee-collection
   mechanics for non-MCO exchanges.
2. **CERC transaction-fee review — NOT in the corpus, found only by
   independent web search.** CERC finalised a staff paper, "Review of
   Transaction Fee charged by the Power Exchanges," in Dec-2025. Current
   ceiling: ~2 paise/kWh (per side). Under consideration: a fixed 1.5
   paise/unit for most segments, and 1.25 paise/unit specifically for TAM
   contracts (BusinessToday, 28-Dec-2025; Business Standard,
   28-Dec-2025). This is a SECOND, coupling-independent threat to the
   fee-per-unit assumption every number in this report depends on. As of
   this search (08-Sep-2026), it remains a staff paper / preliminary
   consultation, not a final order. Monitoring signal: any CERC draft or
   final regulation on transaction fee.
3. **Saturation of the STM's own historical growth path.** Section 2's
   management-claim test shows the 25%-of-generation aim needs STM
   growth well above trend; if STM reverts to its 8.9% trend rate, the
   upside case compresses toward the conservative case shown here.
4. **Substitution / disintermediation.** DEEP platform bilateral
   volume (~40 BU, Investor Presentation p.21) is a reminder that
   large counterparties can and do trade outside any exchange when it
   suits them; the 11-month TAM approval is designed to pull some of
   that back, but it is not guaranteed.
5. **Cyclical demand risk.** Peak demand and STM volume both track
   weather and hydro/thermal mix year to year (AR p.46-47 notes regional
   variation); a mild monsoon or a demand slowdown compresses STM
   directly.

### 4C Market structure

- Competitor count: 3 licensed power exchanges (IEX, PXIL, HPX).
- Top-1 concentration: IEX ~80-85% of exchange-traded volume (Concall
  Jul-2026, p.4, aggregate, no named-peer breakdown available —
  NOT FOUND for PXIL/HPX individually).
- Organised vs unorganised: within the STM, "organised" (exchange) is
  60%, "unorganised" (bilateral + DSM) is 39-40% (AR p.47).
- Consolidating or fragmenting: IEX's own share fell from ~95%+
  historically toward 80-85% as PXIL and (more recently) HPX have grown;
  market coupling is a regulatory design specifically intended to
  redistribute DAM share more evenly, i.e. fragmenting by design.
- Price vs differentiation competition: fee is regulator-capped for all
  three exchanges alike (Section 4B); competition today is on liquidity,
  product breadth, and member integration (API/back-office switching
  costs, B04), not price.
- Entries/exits: no new exchange licences reported since HPX; the
  binding new-entrant risk is regulatory redesign (coupling), not a
  fourth exchange.
- Import share trend: not applicable (domestic-only market).

---

## SECTION 5: SUMMARY & RUNWAY

### 5A Funnel

```
Total electricity generation, India, FY26:            1,848 BU
  less: long-term PPA / captive / must-run (structural, non-tradable)
Short-term market (STM), FY26:                           302 BU  (AR states 13%; computes to 16.3%)
  x fee (conservative 3.6p / realistic 3.96p)
TAM (100% exchange capture of STM):          Rs1,087cr — Rs1,196cr
  x 85% capability ceiling (competition + coupling design)
SAM:                                          Rs924cr — Rs1,017cr
  x IEX's achievable share of SAM (60% today; 51% downside / 61-62% base, yr3-5)
SOM 3yr:                                       Rs609cr (downside) — Rs728cr (base)
SOM 5yr:                                       Rs722cr (downside) — Rs878cr (base)
```

### 5B Runway assessment

- Revenue headroom = SAM (conservative) / current electricity revenue =
  Rs924cr / Rs558.51cr = **1.65x**.
- TAM growth rate (STM trend CAGR, AR p.47): **8.9%/yr**, well below the
  actual FY25→FY26 STM growth of +26.9% — the conservative figure is
  used deliberately as the headline per the pipeline's bias rule.
- Company CAGR vs TAM: IEX's own 8-year revenue CAGR is 13.5%
  (Data_Sheet, FY19-FY26), above the 8.9% STM trend — IEX has been
  GAINING SHARE of its addressable pool, not just riding it, consistent
  with the exchange-of-STM penetration rising from a lower historical
  base toward 60% today.
- Years to saturate the conservative SAM at IEX's own historical growth
  rate (13.5%): ln(924/558.51)/ln(1.135) ≈ **4.0 years** — a genuinely
  short runway on a STATIC SAM; the dynamic SAM_FY29/FY31 figures above
  (which grow with STM) are the more honest read, but even so the
  multi-year SOM CAGR implied (2.9-9.5%) sits far below IEX's own
  historical delivery.

### 5C Runway classification

**MODERATE-LIMITED. Reported: LIMITED.** Revenue headroom of 1.65x sits
at the low end of any reasonable band; TAM growth of ~9% is real but
modest; and the SOM-implied CAGR (2.9-5.3% conservative, up to 9.2-9.5%
base) is well short of both the pipeline's 25% CAGR hurdle and IEX's own
historical 13.5% revenue CAGR. This is the honest consequence of sizing
a FEE POOL rather than the value of electricity traded: IEX already
captures roughly 60% of its own conservative SAM, on a slow-growing
addressable pool, before layering coupling and fee-review risk.

### 5D SAM expansion levers actually being pursued

| Lever | Potential addition | Status |
|---|---|---|
| 11-month TAM contract approval | 15-20 BU (management claim) against a 40 BU DEEP bilateral base | CERC petition filed, order reserved 2+ years (B07) |
| Green RTM approval | Not sized (no volume figure disclosed) | CERC petition filed, order reserved |
| Peak DAM/RTM (BESS) approval | Not sized | CERC petition filed, order reserved |
| Gas (IGX) | Separate option pool, see below | Equity-accounted at 47.28%, falling to 25% post-OFS |
| Coal (Indian Coal Exchange) | Separate option pool, see below | Licence not yet awarded to IEX specifically (B07 gap) |
| Carbon (Indian Carbon Exchange) | Not sized (no fee-pool figure found) | Trading foundation laid, IEX venue designation not yet confirmed (B07 optionality register) |

None of these is inside SAM/SOM as computed; each is additive optionality
if and when it converts.

### 5E Final output card

At **2.9%-5.3%** revenue CAGR implied by the conservative SOM, with a
margin trajectory assumed broadly flat (standalone operating margin
~86-87%, B04, near its structural ceiling for an asset-light platform, so
no further operating leverage is modelled), the earnings growth embedded
here is also roughly **2.9%-5.3%** CAGR (in the base case, 9.2%-9.5%),
which **does not support** the current valuation of **~27.5x** operating
P/E (CMP Rs116.54, FY26 operating EPS ~Rs4.24 after stripping treasury
income of Rs151.10cr from consolidated PBT of Rs645.56cr at the blended
effective tax rate, B00 manifest + company memory figures) under the
conservative case, and remains stretched even under the base case. The
option pools (gas, coal, carbon) are the load-bearing source of any bull
case beyond the core electricity business; none of them is a certainty
today.

---

## SECTION 6: DOWNSTREAM SIGNAL CANDIDATES

| # | Candidate Signal | Entity Type | Why It Drives Demand | Likely Primary Source | Expected Cadence |
|---|---|---|---|---|---|
| 1 | CERC Short-Term Power Market report (monthly + annual) | Regulatory | Directly reports STM volume (302 BU FY26) and exchange-vs-bilateral-vs-DSM split, the single load-bearing input to this TAM's addressable pool | CERC Market Monitoring Division official reports | Monthly/Quarterly |
| 2 | CEA generation and demand-met data | Macro | Sets the total-generation denominator (1,848 BU FY26) and the FY32/FY35-36 growth trajectory (LTNRAP) that every forward SAM/SOM figure scales against | Central Electricity Authority (CEA) monthly/annual reports | Monthly |
| 3 | CERC market-coupling final regulation / Supreme Court case status | Regulatory | Resolves the 20-40% DAM volume-impact range that sets the SOM downside scenario | CERC official notifications; Supreme Court of India cause list | Event-driven |
| 4 | CERC transaction-fee review final order | Regulatory | Sets the per-unit fee (currently ~2p ceiling, proposed 1.5p/1.25p-TAM) that is multiplied into every Rs Cr figure in this report | CERC official notifications | Event-driven |
| 5 | Coal India Ltd monthly e-auction/SWMA allocation data | Counterparty | Anchors the Indian Coal Exchange option-pool volume base (management's ~100-120 MT year-one claim) | Coal India Ltd investor disclosures | Monthly |
| 6 | Ministry of Coal / Coal Controller Organization licence award | Regulatory | Converts the Coal Exchange optionality into an IEX-specific volume base; not yet awarded to IEX as of this corpus | Ministry of Coal / CCO official notification | Event-driven |

demand_externally_verifiable: true (6 rows, all corroborable against
regulator or peer-company public disclosure, independent of IEX's own
reporting).

---

## Search log

**Performed:**
1. CERC short term power market report FY26 India volume billion units 2026
2. India power exchange market share IEX PXIL HPX volume 2026
3. India electricity generation growth forecast CEA 2032 billion units National Resource Adequacy Plan
4. CERC power exchange transaction fee cap paise per unit regulation
5. CERC transaction fee power exchange draft regulation 2026 status IEX
6. India Coal Exchange market size e-auction coal volume 2026 million tonnes
7. Carbon Credit Trading Scheme India market size compliance mechanism 2026 CCTS volume
8. European power exchange EPEX Nordpool share of electricity generation traded percentage
9. China power spot market electricity trading share of generation percentage 2025 2026

**Skipped:**
- PXIL and HPX individual FY26 volume/revenue disclosures (exchange-specific filings, not pursued beyond the general market-share search)
- Indian Carbon Exchange / CCTS per-tonne trading fee schedule (only asset-value market-size figures found, USD-denominated, wrong basis for a fee pool per this stage's own rule; no fee-pool-appropriate figure exists as trading has not started)
- Coal Exchange per-tonne transaction fee schedule (not yet finalised/disclosed anywhere found)

---

## ADJACENT OPTION POOLS (NOT in tam_cr / sam_cr / som_*_cr)

### Gas — Indian Gas Exchange (IGX)

- Current: FY26 traded volume 1.94 BCM, 2.82% of India's gas consumption
  (IGX Draft Abridged Prospectus, Jul-2026, p.4, CRISIL Report cited).
  FY26 PAT Rs42cr (Concall Jul-2026, p.5).
- TAM (CRISIL, cited in the same prospectus): 16.40 BCM in FY26, 24.53%
  of gas consumption — implying **8.45x** headroom on current volume,
  growing at ~24.7% CAGR FY26-FY30 vs ~11.7% for overall gas consumption
  growth, driven by spot LNG availability and a possible removal of the
  current 10%-of-domestic-production exchange cap (same source, p.4).
- Caveat: IGX is equity-accounted, not consolidated (47.28% stake,
  falling to the PNGRB 25% ceiling via the OFS in the DRHP). Even full
  TAM capture flows to IEX only through its (shrinking) equity share and
  through the one-time OFS monetisation value, not through consolidated
  revenue.

### Coal — Indian Coal Exchange (ICX)

- Year-one opportunity: management states two figures — "at least 100
  million tonne" as an initial target (Concall Jul-2026, p.29) and "the
  market size as on date is 120 million tonnes" (same call, p.29),
  growing to "almost about 250-300 million tonnes by 2035" (same page).
  The Investor Presentation (p.34-35) shows 100 MT → 150 MT (FY30) → 250
  MT (FY35).
- Independent corroboration: Coal India's own e-auction allocation ran at
  roughly 110-150 MT/year annualised in FY27 YTD (Apr-Aug 2026, web
  search), broadly consistent with management's ~100-120 MT figure.
- Fee basis: NOT FOUND. No per-tonne coal-exchange transaction fee is
  disclosed anywhere in the corpus or located via web search, so no Rs Cr
  figure is built — per the pipeline's rule against estimating a missing
  number, this pool is reported in volume (MT) only.
- Caveat: the Coal Exchange licence has NOT yet been awarded to IEX
  specifically (B07 gap, coal_exchange_licence_status); the volume
  potential is real, IEX's capture of it is a management claim.

### Carbon — Indian Carbon Exchange / Carbon Credit Trading Scheme (CCTS)

- Compliance base: ~740 entities, >700 million tonnes CO2-equivalent
  across 9 sectors (aluminium, cement, chlor-alkali, fertiliser, iron &
  steel, pulp & paper, petrochemicals, petroleum refinery, textiles) —
  web search, ICAP/BeZero Carbon sourced. First compliance-based Carbon
  Credit Certificate trades expected around October 2026.
- The market-value figures found via search (USD 33.7bn in 2025, growing
  toward USD 66-405bn by 2033-34) are the VALUE OF CARBON CREDITS TRADED,
  the exact wrong basis this stage is instructed to avoid (the electricity
  TAM equivalent of that mistake would be sizing IEX off the rupee value
  of power traded, not the fee). No fee-pool figure exists because CCTS
  trading has not started. NOT sized.
- Caveat: IEX's own designation as a trading venue under CCTS is "laid
  the foundation... expectedly in FY'27" (Investor Presentation p.19) but
  not yet IEX-confirmed (B07 optionality register).
