# STAGE 9: TAM / SAM / SOM MARKET SIZING — Insolation Energy Ltd (INA)
Run date: 2026-09-06 | Model: claude-sonnet-5

---

## SECTION 1: MARKET DEFINITION

### 1A. Precise boundaries

This is not one market. B04 (business model block) shows FY2026 consolidated
revenue is 81.9% own-manufactured modules, 17.0% traded modules, 0.2%
electricity sale, 0.5% other (B04-bizmodel.yaml). Three distinct markets are
therefore sized separately, then combined with an explicit no-double-count
rule.

**Market 1 — Indian solar module manufacturing (product scope: crystalline
silicon PV modules for utility, C&I, rooftop and government-scheme use;
geography: India only, domestic sale; customer scope: EPC contractors,
utilities/PSUs (NTPC, SECI), IPP developers, dealers/channel partners,
rooftop/retail; channel scope: direct institutional tender, dealer network,
EPC partnership; price segment: split DCR (ALMM-II cell-compliant,
scheme-mandated) and non-DCR (open market); explicit exclusion: exports —
US anti-dumping/countervailing duties closed that channel in 2026 and INA's
own corpus shows no material export revenue). This is ~99% of INA's FY2026
revenue (Finished Goods + Trading Sales + Other, per B04) and is the market
the SOM-implied CAGR handoff to Stage 11 is built on.

**Market 2 — Indian solar cell manufacturing** (the market the Rs1,500cr
committed Narmadapuram 4.5GW TOPCon facility enters; product scope: ALMM-II
listed solar cells; geography: India; customer scope currently captive —
INA's cell capacity (4.5GW) is smaller than its module capacity (5.5GW), so
this facility is sized to feed INA's own module lines, not to sell cells to
third parties at scale). **This market is sized for context and is NOT
added to headline TAM/SAM/SOM**: backward integration captures MARGIN on
revenue already counted in Market 1 (module ASP already embeds cell value);
counting a separate cell-market TAM on top would credit the same rupee of
revenue twice, which CLAUDE.md's "never credit one quality improvement
through two mechanisms" rule forbids. It is shown in Section 2 purely to
size the ALMM-II cell-capacity claim INA makes and to test it.

**Market 3 — PM-KUSUM-linked independent power production (IPP)**
(product scope: solar electricity sale under Component A/C of PM-KUSUM;
geography: India, state-specific PPAs; customer scope: state discoms/nodal
agencies). This IS additive to Market 1 — it is a different product
(electricity, not modules) sold through a different revenue mechanism
(long-term PPA, not one-time equipment sale). It is currently 0.2% of
INA revenue (Rs4.22cr, Sale of Electricity, AR p.130) against a stated
~400MW target of which ~38-40MW is commissioned (Concall Jun 2026, p.20).

### 1B. Management's own market claims

INA's corpus contains no explicit Rupee-denominated TAM figure. Management's
market-sizing argument is capacity-based: **"around 142 GW of total cell
manufacturing capacity registered in the ALMM... however that manufacturing
capacity less than 100, or you can say 100, nearly 100 GW of the capacity
registered, which is TOPCon or G12R"** (Concall Feb 2026 Transcript, p.485-487,
Manish Gupta), used to argue no industry overcapacity exists. Stage 6 (B06,
Q1) already found this figure implausible against every peer's own cell
capacity disclosure (Waaree ~30GW relevant, Premier ~27-30GW actual, Websol
24GW ALMM-approved) and matching almost exactly Websol's disclosed ALMM
MODULE capacity of 145GW (Websol, 30-Jan-2026 call, p.19). This stage treats
the 142GW claim as management's closest analogue to a market-size claim and
tests it quantitatively in Section 2.

Credibility read at this stage: **broad and likely mislabeled** — a capacity
figure presented as evidence of ample market headroom that in fact describes
a different, larger, adjacent market (modules, not cells).

---

## SECTION 2: TAM ESTIMATION, MULTIPLE METHODS (Market 1 — modules)

### Method 1 — Top-down (industry value)

India solar PV module market value: USD 10.9bn (2025) to USD 12.4bn (2026)
(Mordor Intelligence / Intellectual Market Insights industry reports, both
retrieved 2026-09-06). At ~Rs88/USD: **Rs95,920cr (2025) to Rs109,120cr
(2026)**. This is an India-market figure already (not global), so no
separate global/India split subtraction is needed; treated as-is.

### Method 2 — Bottom-up (units x realized price)

Addressable unit: 1 watt (Wp) of installed module capacity.
- Total annual India module DEMAND (not manufacturing capacity): ~60GW/year
  at current run-rate — cross-checked from AR's own "44.61 GW of solar
  capacity" added in FY2025-26 (AR p.48) plus Mercom's H1 2026 record 27GW
  (49% YoY, pv-tech.org, retrieved 2026-09-06, implying ~50-55GW annualized)
  and Premier's Aug-2026 call figure of "entire demand in India is about 60
  gigawatt" (B06, Q1). Conservative bottom-up uses 55GW; realistic uses 60GW.
- Demand split: ~30GW DCR (ALMM-II compliant, scheme-mandated) vs the
  remainder non-DCR (open market), per Premier Aug-2026 ("almost about 30
  gigawatt is DCR" out of 60GW total, B06 Q1).
- Realized price: DCR Rs21-22/watt (Waaree Q4 FY26, Premier Q3 FY26, cited
  in B06 Q2, cross-checked against INA's own stated Rs20-22/watt); non-DCR
  Rs13-16/watt (Waaree Rs15-16, Premier Rs14-15, INA Rs13-14, B06 Q2).
- Conservative: 30GW DCR x Rs21/watt + 25GW non-DCR x Rs13.5/watt = (30 x 21
  x 100) + (25 x 13.5 x 100) = Rs63,000cr + Rs33,750cr = **Rs96,750cr**
  (rounded to Rs96,000cr for the triangulation table below).
- Realistic: 30GW DCR x Rs21.5/watt + 30GW non-DCR x Rs14.5/watt = Rs64,500cr
  + Rs43,500cr = **Rs108,000cr**.
  (Formula: revenue Cr = GW x Rs/watt x 100, since 1GW = 1e9 watt and 1cr =
  1e7.)

Methods 1 and 2 triangulate tightly: Rs95,920-109,120cr (top-down) vs
Rs96,750-108,000cr (bottom-up). This is an unusually clean cross-check for
an Indian small-cap sizing exercise.

### Method 3 — Peer revenue aggregation

Known listed peers, FY2026 revenue: Waaree Energies Rs26,536.77cr (84% YoY
growth; scanx.trade, retrieved 2026-09-06), Premier Energies Rs7,824.30cr
(scanx.trade, retrieved 2026-09-06), Websol Energy Rs1,049cr (pv-magazine-
india.com, retrieved 2026-09-06), INA itself Rs2,146.02cr. Sum of these four
alone: **Rs37,556cr**. Adani Solar, Tata Power Solar, Vikram Solar, EMMVEE,
Goldi Solar, RenewSys and Saatvik Green Energy are all named top-10 players
(rayzonsolar.com / saurenergy.com, retrieved 2026-09-06) but do not disclose
comparable standalone revenue in the sources retrieved this run; their
combined scale is plausibly Rs50,000-70,000cr+ given Waaree's and Adani's
GW-scale capacity lead, which would bring aggregate organized-sector revenue
into the same Rs95,000-115,000cr band as Methods 1-2. **NOT FOUND: precise
FY26 standalone revenue for Adani Solar, Tata Power Solar, Vikram Solar,
EMMVEE, Goldi Solar, RenewSys, Saatvik** — flagged rather than estimated.
Unorganised-sector add-on: unlike most Indian industries, module
manufacturing for DCR/government-scheme demand is gated by ALMM listing and
BIS/IEC/UL certification (AR p.49, B04), which structurally excludes
informal/unorganised capacity from that share of demand. A residual
informal/grey-market segment plausibly exists only in uncertified retail/
rooftop modules; this stage does not attempt to size it and treats the
peer-aggregation method as directionally consistent with, not adding on top
of, Methods 1-2.

### Method 4 — Import substitution (applies most directly to Market 2, cells)

India is close to fully self-sufficient in MODULE capacity (172GW
manufacturing capacity vs ~162GW installed base, AR p.48-49) but remains
"100% import-dependent on China" for wafers today (Investor Presentation,
p.865-867) and has only ~24-30GW of ALMM-listed CELL capacity against
~172-210GW of module capacity (Websol 24GW; Mercom/PV Tech "India's
cumulative solar module capacity reaches 210GW, cell capacity hits 27GW,"
retrieved 2026-09-06). This 5:1+ module-to-cell capacity ratio is the
structural gap the Narmadapuram cell facility targets — sized separately in
the cell-market note below, not folded into Market 1's TAM.

### Method 5 — Global benchmark

Not run as a dedicated search this stage: India's own top-down (Method 1)
and bottom-up (Method 2) figures already triangulate tightly and India is
independently confirmed as the world's second-largest annual solar market
(AR p.48, 44.61GW added FY25-26), making a per-capita global benchmark a
lower-priority third check once two methods already agree within 12%. Not
listed under searches_skipped (no tool/quota failure occurred; this was a
prioritization choice, disclosed here for transparency).

### Triangulation table (Market 1 — modules)

| Method | Estimate (Rs Cr) | Confidence | Staleness |
|---|---|---|---|
| 1. Top-down (industry value) | 95,920 - 109,120 | M (third-party market-research sourcing, no single named primary report accessed in full) | Current (2025-2026 data) |
| 2. Bottom-up (units x price) | 96,750 - 108,000 | H (anchored to AR + 3 peer concalls + INA's own realized prices) | Current (FY2026/Q1 FY27 data) |
| 3. Peer aggregation (partial) | >=37,556 (4 disclosed peers only, directionally consistent with 95,000-115,000 once remaining top-10 peers are added) | L (incomplete peer set; NOT FOUND for 7 of ~11 named top-10 players) | Current |

**Conservative TAM (Market 1): Rs96,000cr. Realistic TAM (Market 1):
Rs108,000cr.**

**Management's implied market-size claim vs conservative estimate.** INA
gives no Rupee TAM. Its closest analogue is the 142GW ALMM cell-capacity
claim (Section 1B), tested against Market 2 below because it is a cell,
not module, claim. Applied there: **ratio 4.73x, read: inflated** (>2x
threshold). See Section 2's cell-market note for the calculation. This
stage does NOT compare INA's FY28 revenue *target* (Rs8,500cr, cut to
Rs5,000cr+, see Section 4B) to TAM, because a single company's revenue
target compared to total market size would trivially read as "conservative"
for any company and would not test market-size credibility, which is what
this ratio is for. The revenue-target cut is carried instead as a
credibility flag against SOM (Section 3B) and Stage 5's own guidance-miss
finding.

### Cell-market note (Market 2 — not additive to headline TAM)

Bottom-up: DCR-mandated demand (~30GW/year, Method 2 above) is the segment
ALMM-II legally requires to use domestic cells. At cell realization
~Rs12-14/watt (Websol 13-13.5 cents/watt ~ Rs11.5-12/watt, Concall/B06 Q2;
INA's own DCR module ASP of Rs20-22/watt implies a lower cell-only
component), conservative cell-linked revenue pool = 30GW x Rs12/watt x 100
= **Rs36,000cr/year**. If non-DCR module makers also backward-integrate
for margin capture (an industry-wide trend per B06 2C), a realistic ceiling
extends toward the full 60GW module-demand base = 60GW x Rs12/watt x 100 =
**Rs72,000cr/year** (upper bound, most of which INA cannot access given its
cell capacity, 4.5GW, is smaller than its own module capacity, 5.5GW, and
is designed to be captively consumed, not sold externally).

Testing management's 142GW claim: valuing 142GW at Rs12/watt implies a
headline cell-market claim of 142 x 12 x 100 = **Rs170,400cr**. Against the
conservative cell-market estimate of Rs36,000cr, **ratio = 4.73x — read:
inflated** (>2x threshold, per this stage's standard read). The claim is
also, per B06 Q1, very likely a module-capacity figure mislabeled as cell
capacity, which is a separate, corroborating credibility problem.

---

## SECTION 3: SAM & SOM

### 3A. SAM (Market 1 — modules)

Five filters applied to Module TAM:
1. **Product fit**: full fit — INA sells both DCR and non-DCR modules. No cut.
2. **Geography**: TAM is already domestic-only (exports excluded at
   definition stage, Section 1A). No further cut.
3. **Channel/customer fit**: exclude demand captured by vertically
   integrated groups supplying their own captive IPP arms (Adani, Tata
   Power) that INA structurally cannot bid for. Estimated cut: **15%**.
4. **Scale/track-record fit**: exclude ultra-large single-award tenders
   (500MW+) that typically screen for balance-sheet scale and track record
   INA has not yet demonstrated (INA's own order book mixes NTPC and L&T
   wins, AR p.810, but at sub-GW scale per award). Estimated cut: **10%**.
5. **Capability fit**: INA's DCR supply today depends on third-party
   cell tie-ups (Emvee, Premier, per Concall Jun 2026 p.594-596) rather than
   captive cells (COD guided Q3/Q4 FY27, B05 already flags this guidance as
   internally inconsistent). This is a temporary, not structural, capability
   gap. Estimated cut: **5%**.

Combined filter: 1 - (0.85 x 0.90 x 0.95) = 27.3% cut. **SAM (Module) =
72.7% of TAM: conservative Rs69,800cr, realistic Rs78,500cr.**

### KUSUM SAM (Market 3)

INA's own disclosed target is ~400MW (325MW AC / 400MW DC, Concall Jun 2026
p.776-778) against a national PM-KUSUM target of 34,800MW (MNRE, ibef.org,
retrieved 2026-09-06). Because INA's own capacity target already reflects
its capability ceiling in this vertical (a mid-size, single-state-heavy IPP
developer per the AR's own project list, e.g. "IPP + PM-KUSUM (AP) Awarded
Rs516 Cr", Investor Presentation p.781-782), SAM here is computed bottom-up
from that 400MW target rather than as a filtered percentage of the national
scheme (sizing the national scheme is reserved for TAM context only).

Per-MW annual revenue (independent cross-check, not management's figure):
capacity utilisation factor (CUF) 20% (conservative) / 22% (realistic),
feed-in tariff Rs2.44/unit (AR p.48, "solar tariffs... declined to Rs2.44
per unit") conservative / Rs3.00/unit realistic (typical KUSUM state SERC
order range, broad estimate, NOT a filed INA-specific tariff — flagged).
- Conservative: 1MW x 8,760h x 0.20 x Rs2.44 = Rs42.75 lakh = Rs0.4275cr/MW.
- Realistic: 1MW x 8,760h x 0.22 x Rs3.00 = Rs57.82 lakh = Rs0.5782cr/MW.

**KUSUM SAM (400MW ceiling): conservative Rs171cr/year, realistic
Rs231cr/year (steady state, once fully commissioned).**

National KUSUM TAM context (all developers, full 34,800MW build-out):
conservative 34,800 x 0.4275 = Rs14,880cr/year; realistic 34,800 x 0.5782 =
Rs20,120cr/year. INA's 400MW target is ~1.15% of the national headline
figure — a useful scale check, not a filter calculation.

### Combined TAM and SAM (headline, modules + KUSUM; cells excluded per
Section 1A no-double-count rule)

| | Conservative (Rs Cr) | Realistic (Rs Cr) |
|---|---|---|
| TAM | 96,000 + 14,880 = **110,880** | 108,000 + 20,120 = **128,120** |
| SAM | 69,800 + 171 = **69,970** | 78,500 + 231 = **78,730** |

sam_pct_of_tam (realistic) = 78,730 / 128,120 = **61.4%**.

### 3B. SOM at 3 and 5 years

Current SAM share: FY2026 total revenue Rs2,146.02cr / realistic SAM
Rs78,730cr = **2.7%**.

Share-gain assumption: INA's committed capex (cell + aluminium frame
facilities) argues for the "3-5pp aggressive" bracket, but Stage 5's
finding that FY26 guidance missed on every revenue line and Stage 6's
credibility grade D (B06 analyst_note) argue against assuming flawless
execution. Conservative-bias instruction applied: **+1.5pp by year 3
(to 4.2%), +2.5pp cumulative by year 5 (to 5.2%)** — inside "1-2pp normal"
for year 3, just into the low end of "3-5pp aggressive" by year 5, justified
by capacity (not yet by execution track record).

SAM is grown at tam_growth_pct = 16%/year (Section 4A) over the horizon:
- SAM_3yr (realistic) = 78,500 x 1.16^3 = Rs122,460cr (module portion only;
  KUSUM SAM held at its own ramp schedule, not compounded at 16%).
- SAM_5yr (realistic) = 78,500 x 1.16^5 = Rs164,850cr.

Module SOM:
- SOM_3yr = 122,460 x 4.2% = **Rs5,143cr**.
- SOM_5yr = 164,850 x 5.2% = **Rs8,572cr**.

KUSUM SOM: management states Rs135cr (FY27, partial-year, all currently
committed 400MW commissioning in progress) and Rs300cr (FY28, "50%" per
Ravi Dusad, Concall Jun 2026 p.784-790) for the SAME ~400MW target — an
internal 2.2x jump year-on-year for a project management itself frames as
still ramping, which is not a clean, reconcilable schedule (flagged, not
used uncritically). This stage instead phases the independently-computed
KUSUM SAM ceiling (Rs231cr at full run-rate): **KUSUM SOM_3yr = Rs115cr
(~50% of pipeline ramped), KUSUM SOM_5yr = Rs231cr (full 400MW online and
run-rate stabilised)**.

**Combined SOM_3yr = 5,143 + 115 = Rs5,258cr (rounded Rs5,260cr).**
**Combined SOM_5yr = 8,572 + 231 = Rs8,803cr (rounded Rs8,800cr).**

Arithmetic check: SOM < SAM < TAM holds at every horizon (SOM_3yr 5,260 <
SAM_3yr ~122,460+171 < TAM growth path; SOM_5yr 8,800 < SAM_5yr ~164,850+231
< TAM growth path).

**som_implied_revenue_cagr** (base: FY2026 consolidated revenue Rs2,146.02cr,
REVENUE_ANCHOR):
- yr3: (5,260 / 2,146.02)^(1/3) - 1 = (2.4514)^0.3333 - 1 = **34.8%**.
- yr5: (8,800 / 2,146.02)^(1/5) - 1 = (4.1006)^0.20 - 1 = **32.6%**.

Both figures sit far above management's own FY28 vision (Rs5,000cr+, itself
cut from Rs8,500cr+, Section 4B) restated as a CAGR: Rs2,146.02cr to
Rs5,000cr over 2 years (FY26 to FY28) implies ~52.7% CAGR — meaning even
management's own (already-cut) target implies FASTER growth than this
stage's SOM-implied CAGR over a shorter window, largely because the FY28
target is dominated by cell-integration margin/ASP uplift on the SAME
module volume rather than new addressable-market capture. Stage 11 should
treat the SOM-implied 32.6-34.8% CAGR as the market-capture-based ceiling
check on management's revenue target, not as an independent forecast of it.

### 3C. Capacity cross-check

Using B07's FY2026 capex figure (Rs430.63cr, gross-block additions, AR Note
4 p.119) and its capex_embedded_growth_pct of 428%: this figure describes
the SCALE of FY2026 capex relative to the prior asset base, not a revenue
CAGR, and should not be read as implying 428% revenue growth. It is
consistent with a company mid-way through a step-change capacity build
(5.5GW module base reached only within FY2026, AR p.229-230), which is why
FY2026 revenue (Rs2,146.02cr) reflects a PARTIAL-year run-rate on that
capacity, not a full-year one.

Physical check on Module SOM: at INA's own realized blended ASP
(predominantly non-DCR mix today, ~Rs14/watt blended estimate from B04's
revenue mix and Section 2's realized-price anchors), 5.5GW at 100%
utilisation = 5.5 x 14 x 100 = **Rs7,700cr/year maximum, on EXISTING
committed capacity, no further capex**.
- SOM_3yr (Rs5,260cr, of which Rs5,143cr is module) requires ~67% of that
  ceiling — comfortably inside existing capacity.
- SOM_5yr (Rs8,800cr, of which Rs8,572cr is module) EXCEEDS the Rs7,700cr
  ceiling by **~Rs1,100cr**. This gap can only be closed by (a) a shift in
  product mix toward higher-ASP DCR volume (worth ~Rs6-8/watt more per unit,
  achievable only once the captive cell facility feeds independent DCR
  supply) or (b) capacity beyond the currently committed 5.5GW+4.5GW
  cell/18,000MTA frame program — the announced-but-not-committed ingot/wafer
  facility is explicitly excluded from this capacity base because it is
  still at DPR stage (per injected PRODUCTS description), not committed
  capital.

**capacity_check: gap of ~Rs1,100cr at year 5; the SOM side is the
optimistic one, and its resolution rests entirely on the committed cell
facility (Rs1,500cr, Narmadapuram) commissioning on its guided schedule and
lifting DCR-compliant mix — a schedule Stage 6 (B06 Q3) and Stage 5 already
flag as internally inconsistent (Q3 vs Q4 FY27 COD guidance given in the
same call).** The capex plan itself is adequately scaled for SOM_3yr and
close to adequate for SOM_5yr; the gap is an execution/mix-timing risk, not
an under-investment problem.

KUSUM's own capacity check: SOM_5yr for KUSUM (Rs231cr) requires ALL 400MW
of the target to be commissioned and running at a full-year run-rate, versus
only ~38-40MW commissioned today (Concall Jun 2026 p.777-778) — a
~360MW-equivalent commissioning gap over 5 years. Separately, that same
~38-40MW already commissioned should, at this stage's own CUF/tariff
assumptions, generate roughly Rs17-22cr/year at a full-year run-rate; FY2026
actual Sale of Electricity revenue was only Rs4.22cr (AR p.130) — about
19-25% of that expected level. The most likely explanation is late-FY2026
commissioning (partial-year contribution only), but this cannot be
confirmed from the injected corpus and is flagged as a discrepancy for
Stage 11/FTTCP, not resolved here.

---

## SECTION 4: GROWTH DRIVERS, RISKS & STRUCTURE

### 4A. TAM growth drivers

| Driver | Impact | Evidence |
|---|---|---|
| Penetration (renewables share of grid) | High | India's non-fossil capacity 283.46GW incl. 274.68GW renewable, record 55.29GW annual addition (AR p.48); renewables met 51.5% of demand on one day in 2025 (AR p.48) |
| Regulatory tailwind (ALMM, PLI) | High | ALMM-II domestic-cell mandate (deferred to Dec-2026, B06 Q5); PLI scheme for high-efficiency modules (AR p.55, though INA's own PLI allocation is NOT FOUND, B04 flag) |
| New applications / scheme expansion | Medium-High | PM-KUSUM expanded from 35GW to ~50-55GW target with state co-participation (Investor Presentation p.414-415); new PM-Surya Sarovar Yojana (floating solar + BESS, Rs5,070cr outlay, approved Jul-2026, AR p.630-643) |
| Import substitution (cells/wafers) | High, but delayed | Cell capacity ~24-30GW vs ~172-210GW module capacity (Mercom, PV Tech, retrieved 2026-09-06); ALMM-III wafer mandate now June 2028 (Concall Jun 2026 p.750-751) |
| Technology enablement (TOPCon/G12R) | Medium | Sector-wide shift from Mono PERC to TOPCon (all 3 peers per B06 2C); INA's own 5.5GW is TOPCon-based (AR p.2519) |
| Geographic expansion | Low for INA | India-only; export channel effectively closed by US tariffs (WebSearch, pandwsolar.com context; not INA-specific but sector-wide) |

### 4B. TAM risks

| Risk | Monitoring signal |
|---|---|
| Non-DCR module oversupply / price competition | Premier's explicit Aug-2026 admission: non-DCR "not profitable," "250 odd gigawatt of module lines" vs 60GW total demand (B06 Q1) |
| Regulatory-date slippage | ALMM Part 2 deferred from 1-Jun-2026 to Dec-2026, disclosed in peer calls after INA's own corpus closes (B06 Q5, Websol 11-Aug-2026, Premier Aug-2026) |
| Guidance credibility / mgmt claim inflation | FY28 revenue vision cut from Rs8,500cr+ (Jun-2025 call, p.235) to Rs5,000cr+ (Jun-2026 call, p.618) without acknowledgement, per injected instruction; 142GW cell-capacity claim reads inflated at 4.73x the conservative cell-market estimate (Section 2) |
| Execution / commissioning risk | Cell facility COD internally inconsistent (Q3 vs Q4 FY27, per B05/B06); KUSUM 38-40MW commissioned generating far below this stage's modelled run-rate (Section 3C) |
| Cyclical / commodity input risk | Silver/polysilicon volatility real and sector-wide, actively hedged by all 3 peers via programs INA's own corpus never discusses (B06 2B) |

### 4C. Market structure

- Module manufacturing: highly fragmented at nameplate level — "45 to 50
  companies" with announced capacity adding to ~200GW (Premier, 23-Jan-2026
  call, cited in B06 Q1) against ~60GW annual demand, i.e. a 3x+
  nameplate-to-demand overhang. Top tier (Waaree ~18.7GW active, Adani,
  Tata Power Solar) is concentrated by capacity; INA self-describes as
  "top-10" (AR p.211/629). Organised-sector dominant; unorganised presence
  structurally limited by ALMM/BIS gating for DCR/scheme demand (Section 2,
  Method 3).
- Cell manufacturing: genuinely concentrated and capacity-constrained
  (~24-30GW ALMM-listed vs ~172-210GW module capacity) — the segment INA is
  entering, not the one it competes in today.
- Price vs differentiation: predominantly price/spec competition in
  non-DCR (commodity); a real but compressing DCR premium (8-15% in 2026,
  down from 20-30% in 2018, per SMM/metal.com data retrieved 2026-09-06).
- Entries/exits: capacity race is industry-wide, not a lone-expander
  situation (B06 2C) — all three read peers simultaneously build cell and
  ingot/wafer capacity.

---

## SECTION 5: SUMMARY & RUNWAY

### 5A. Funnel (Rs Cr, realistic case shown; conservative in parentheses)

```
TAM  (Module + KUSUM, cell excluded)      128,120   (110,880)
  -> SAM (5 filters on module + KUSUM ceiling)  78,730    (69,970)   [61.4% of TAM]
    -> SOM 3yr                              5,260              CAGR 34.8%
    -> SOM 5yr                              8,800              CAGR 32.6%
Current FY2026 revenue: 2,146.02 (2.7% of realistic SAM)
```

### 5B. Runway assessment

- Revenue headroom = SAM (realistic) / current revenue = 78,730 / 2,146.02
  = **36.7x**.
- TAM growth rate (module market): **~16%/year** estimated, driven by
  continued double-digit annual installation growth toward India's 2030
  non-fossil capacity target, partially offset by non-DCR price competition
  (Section 4).
- Company CAGR vs TAM: SOM-implied CAGR (32.6-34.8%) is roughly 2x the TAM
  growth rate (16%) — INA's plan, IF executed, is a share-gaining plan, not
  a market-riding one. Given the execution flags above (guidance misses,
  cash-conversion collapse, COD inconsistency), this is the single most
  important gap between the market opportunity and the company's proven
  ability to capture it.
- Years to saturate SAM at current growth: SOM_5yr (Rs8,800cr) is only
  ~11% of the realistic SAM at that horizon (~Rs165,080cr including KUSUM);
  saturation is not a near-term constraint (>>10 years at any realistic
  execution pace).

### 5C. Runway classification

**MASSIVE.** Headroom exceeds 20x, TAM growth is double-digit, and INA's
own installed capacity (5.5GW module) represents only ~2.6% of India's
national ~210GW module manufacturing capacity — the market-size ceiling is
not the binding constraint on this company's growth. (Execution capability
is a separate, and currently more binding, constraint — flagged, not
folded into this market-size classification.)

### 5D. SAM expansion levers actually being pursued

- Cell backward integration (4.5GW TOPCon, Rs1,500cr, committed, COD guided
  Q3/Q4 FY27): does not expand SAM directly (Section 1A) but is the lever
  that resolves the ~Rs1,100cr SOM_5yr capacity gap (Section 3C) via
  DCR-mix/ASP uplift.
- Aluminium frame integration (18,000MTA, committed): input-cost capture,
  margin lever, not a SAM expansion.
- KUSUM IPP scale-up (38-40MW to 400MW target): SAM expansion of ~Rs60-190cr
  as remaining ~360MW commissions (Section 3B/3C), small relative to the
  module business but a genuinely new (non-module) revenue stream.
- Announced-but-uncommitted ingot/wafer (4.5GW, DPR stage) and BESS
  assembly: NOT included in any SAM/SOM figure above because capital is not
  committed; if committed, ingot/wafer would extend Market 2 (cells)
  further upstream but, per the no-double-count rule, would still be a
  margin lever on Market 1 revenue, not a new TAM.

### 5E. Final output card

Runway: MASSIVE (headroom 36.7x, TAM growth ~16%/year).
At **32.6-34.8%** revenue CAGR implied by SOM, with a margin trajectory
guided by management toward **20%+ EBITDA** (Concall Jun 2026 p.652-655,
against a current 14% EBITDA margin, Ravi Dusad, same call), the earnings
growth embedded here is materially higher than 32.6-34.8% CAGR IF the
margin expansion is realised on top of the revenue path (operating
leverage compounds both), but this stage does not compute a PAT/EPS CAGR —
that is Stage 11's job, using the Section 1B destination PE. Whether this
supports the current valuation is explicitly deferred to Stage 11/FTTCP;
this stage's contribution is the market-capture ceiling the earnings case
must not exceed, and the ~Rs1,100cr SOM_5yr capacity gap that makes the
upper end of that ceiling execution-dependent, not market-size-dependent.

---

## SECTION 6: DOWNSTREAM SIGNAL CANDIDATES

| # | Candidate Signal | Entity Type | Why It Drives Demand | Likely Primary Source | Expected Cadence |
|---|---|---|---|---|---|
| 1 | SECI/NTPC solar tender awards and cancellations | Counterparty | Direct order-book driver for INA's institutional/DCR channel | SECI/NTPC e-tender portals, PIB press releases | Event-driven |
| 2 | MNRE ALMM List I/II updates and effective-date notifications | Regulatory | ALMM-II status is the single load-bearing regulatory trigger for the cell-integration margin thesis (already deferred once, B06 Q5) | MNRE circulars, mnre.gov.in ALMM portal | Event-driven, SHARED (module and cell segments both) |
| 3 | PM-KUSUM state nodal agency (e.g. state renewable energy development agencies) tender/PPA awards | Counterparty | Directly sizes INA's KUSUM IPP pipeline progress against its 400MW target | State nodal agency press releases / MNRE PM-KUSUM dashboard | Quarterly |
| 4 | Module/cell ASP benchmark trackers (DCR vs non-DCR, Rs/watt) | Macro | Cross-checks INA's stated realizations and margin trajectory independent of company disclosure | Mercom India / JMK Research monthly price bulletins | Monthly, SHARED (validates both Market 1 and Market 2 economics) |
| 5 | Silver and polysilicon commodity price indices | Macro | Primary input-cost driver across the sector (all 3 peers hedge actively; INA's own corpus does not disclose hedging, B06 2E) | LME/commodity exchange data, trade press (Mercom, PV Tech) | Monthly, SHARED |
| 6 | US anti-dumping/countervailing duty rulings on Indian solar imports | Regulatory | Governs whether the export channel reopens; also a competitive-supply signal (redirected export volume adds to domestic non-DCR oversupply) | US Department of Commerce / USITC filings | Event-driven, SHARED |
| 7 | Solarworld Energy Solutions Ltd (12.4% of INA FY26 revenue, per B04/B06) order flow and receivables signals | End-customer | Customer concentration risk is the leading hypothesis (per B06 Part 5) for INA's cash-conversion collapse; direct signal of collection risk | Solarworld's own filings/exchange disclosures if listed, else MCA filings | Quarterly |

demand_externally_verifiable: true (7 rows produced; module/cell ASPs,
tender awards, ALMM regulatory status and KUSUM nodal-agency data are all
independently observable outside INA's own disclosures).

---

```yaml
stage: B09-tam
company: "INA"
run_date: "2026-09-06"
model: claude-sonnet-5
status: complete
input_gaps:
  - prospectus (HIGH)
  - results (HIGH)
  - annual-report-notes-1-3-absent (HIGH)
  - rating (MEDIUM)
  - shareholding (MEDIUM)
  - screening-csv-shells (MEDIUM)
  - sector_cap_row-mismatch (MEDIUM)
  - announcements-thin (MEDIUM)
  - research (LOW)
  - peer-concalls-partial (LOW)
  - share-count-blank-FY26 (LOW)
flags:
  - "Management's headline no-overcapacity claim (142GW ALMM 'cell' capacity) implies a Rs170,400cr cell-market claim vs this stage's conservative Rs36,000cr cell-market estimate: ratio 4.73x, read inflated. Corroborates B06 Q1's independent finding that the figure is very likely mislabeled module capacity."
  - "SOM_5yr (Rs8,800cr) exceeds the physical revenue ceiling of INA's currently committed capacity (5.5GW module at 100% utilisation, ~Rs7,700cr at current blended ASP) by ~Rs1,100cr; closing this gap depends entirely on the committed cell facility commissioning on schedule and lifting DCR mix/ASP, a schedule Stage 5/6 already flag as internally inconsistent (Q3 vs Q4 FY27 COD guidance)."
  - "FY26 KUSUM electricity revenue (Rs4.22cr actual) is only 19-25% of this stage's modelled full-year run-rate for the ~38-40MW already commissioned (Rs17-22cr expected); most likely explained by late-FY26 commissioning but not confirmed in the injected corpus."
  - "Management's own FY28 revenue vision was cut from Rs8,500cr+ (Jun-2025 call) to Rs5,000cr+ (Jun-2026 call) without acknowledgement; even the CUT target implies ~52.7% 2-year CAGR, faster than this stage's SOM-implied 32.6-34.8% CAGR, meaning management's own target still runs ahead of an independent, capacity-triangulated market-capture estimate."
market_definition: "Indian solar PV module manufacturing (DCR + non-DCR, domestic-only), plus PM-KUSUM-linked IPP electricity sale as a separate additive market; solar cell manufacturing sized separately as a non-additive margin-capture note."
tam_cr: {conservative: 110880, realistic: 128120}
sam_cr: 78730
sam_pct_of_tam: 61.4
som_3yr_cr: 5260
som_5yr_cr: 8800
som_implied_revenue_cagr: {yr3: 34.8, yr5: 32.6}
current_sam_share_pct: 2.7
revenue_headroom_x: 36.7
tam_growth_pct: 16
runway_class: "MASSIVE"
mgmt_claim_cr: 170400
mgmt_claim_ratio: 4.73
mgmt_claim_read: "inflated"
capacity_check: "gap of ~Rs1,100cr at year 5 vs existing committed module capacity at 100% utilisation; the SOM side is the optimistic one, resolvable only if the committed cell facility commissions on guided schedule and lifts DCR-compliant mix/ASP."
methods_used:
  - "top-down (industry value benchmark, Mordor/IMI market reports)"
  - "bottom-up (units x realized price, AR + peer concalls)"
  - "peer revenue aggregation (partial, 4 of ~11 named top-10 peers disclosed)"
  - "capacity cross-check (installed + committed capacity vs SOM revenue)"
stale_data_flags: []
searches_performed:
  - "India solar PV module manufacturing market size 2026 crore Mercom Bridge to India"
  - "India solar cell manufacturing capacity GW 2026 ALMM list 2 demand"
  - "PM-KUSUM scheme total outlay crore component A B C target capacity 2026"
  - "India solar installations 2026 GW forecast annual capacity addition Mercom Q2"
  - "India DCR domestic content requirement module demand GW government tenders SECI NTPC 2026"
  - "India solar module price per watt non-DCR oversupply crash 2026"
  - "Waaree Energies Premier Energies Websol FY26 annual revenue crore full year results"
  - "India solar module manufacturers market share top players Adani Waaree Premier Vikram Solar 2026"
  - "Websol Energy System FY26 annual revenue crore full year"
searches_skipped: []
downstream_candidates:
  - signal: "SECI/NTPC solar tender awards and cancellations"
    entity_type: "counterparty"
    demand_link: "Direct order-book driver for INA's institutional/DCR channel"
    likely_source: "SECI/NTPC e-tender portals, PIB press releases"
    cadence: "event-driven"
    shared: false
  - signal: "MNRE ALMM List I/II updates and effective-date notifications"
    entity_type: "regulatory"
    demand_link: "ALMM-II status is the load-bearing trigger for the cell-integration margin thesis"
    likely_source: "MNRE circulars, mnre.gov.in ALMM portal"
    cadence: "event-driven"
    shared: true
  - signal: "PM-KUSUM state nodal agency tender/PPA awards"
    entity_type: "counterparty"
    demand_link: "Sizes INA's KUSUM IPP pipeline progress against its 400MW target"
    likely_source: "State nodal agency press releases / MNRE PM-KUSUM dashboard"
    cadence: "quarterly"
    shared: false
  - signal: "Module/cell ASP benchmark trackers (DCR vs non-DCR, Rs/watt)"
    entity_type: "macro"
    demand_link: "Cross-checks INA's realizations and margin trajectory independent of company disclosure"
    likely_source: "Mercom India / JMK Research monthly price bulletins"
    cadence: "monthly"
    shared: true
  - signal: "Silver and polysilicon commodity price indices"
    entity_type: "macro"
    demand_link: "Primary input-cost driver sector-wide; INA does not disclose hedging"
    likely_source: "LME/commodity exchange data, trade press"
    cadence: "monthly"
    shared: true
  - signal: "US anti-dumping/countervailing duty rulings on Indian solar imports"
    entity_type: "regulatory"
    demand_link: "Governs export channel reopening and redirected-volume pressure on domestic non-DCR pricing"
    likely_source: "US Department of Commerce / USITC filings"
    cadence: "event-driven"
    shared: true
  - signal: "Solarworld Energy Solutions Ltd order flow and receivables signals"
    entity_type: "end-customer"
    demand_link: "12.4% customer concentration is the leading hypothesis for INA's cash-conversion collapse"
    likely_source: "Solarworld's own exchange filings if listed, else MCA filings"
    cadence: "quarterly"
    shared: false
demand_externally_verifiable: true
analyst_note: "Three markets, not one: module manufacturing (~99% of current revenue), cell manufacturing (a margin-capture entry, explicitly NOT added to headline TAM to avoid double-crediting the same revenue), and KUSUM IPP (genuinely additive, currently 0.2% of revenue). The two strongest findings this stage: (1) management's own capacity-based no-overcapacity claim reads as inflated by 4.73x against an independently triangulated cell-market estimate, corroborating B06's cell/module conflation finding from a different angle; (2) the SOM_5yr figure this stage computes from bottom-up market-share mechanics slightly exceeds the physical revenue ceiling of INA's currently committed capacity, meaning Stage 11 should treat the upper end of the SOM-implied CAGR range as conditional on the cell facility's COD holding, not as a market-size-guaranteed outcome. Runway classification (MASSIVE) describes the size of the opportunity only; it does not offset the execution-credibility flags carried from Stages 5 and 6."
```
