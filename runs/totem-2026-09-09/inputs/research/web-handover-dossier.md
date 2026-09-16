# WEB HANDOVER DOSSIER — TOTEM (Forbes Precision Tools & Machine Parts Ltd)

Run: `runs/totem-2026-09-09` | Halt 1 cycle date 16-Sep-2026 | Phase 2 input

## PROVENANCE

This is the claude.ai live-verification layer for the TOTEM run. The operator
ran it in Claude web after Halt 1 and saved it to the COMPANIES MASTER page
`3d6bb2b9-d3ab-81c9-956f-cf3a79435cdf` (Halt 1 cycle log, 16-Sep-2026).

Claude Code fetched that page on 16-Sep-2026 through the Notion connector and
wrote this repo copy so `/fttcp` can consume it. The content below is the
web-side record. Claude Code did not re-derive it and does not re-read the
corpus to confirm it; each document is paid for once.

Sources the web session names for its own work: the Halt 1 pack from
`run/totem-2026-09-09`; the Kennametal India institutional investors meeting
transcript of 07-Sep-2026; the Infomerics press release of 19-Feb-2026; the
FY26 annual report; the Q1 FY27 results filing of 12-Aug-2026; screener
quarterly and segment data; and live web on tungsten, cobalt, ACMA, defence,
railways, engineering exports, SP Group refinancing and price.

Evidence tiers appear as the web session wrote them: [FILED], [MGMT],
[AGENCY], [SECONDARY], [INFERENCE].

## SECTION 1 — ENTITY COUNT

**ENTITY COUNT: 1.**

Forbes Precision Tools and Machine Parts Ltd is a single reporting entity. One
operating segment, "Precision cutting tools and related components" [FILED, AR
FY26 Note 38; Q1 FY27 results filing note 3]. No subsidiaries and no joint
ventures. No demerger, spin-off or subsidiary listing is disclosed inside the
projection window.

Recorded by Claude Code from the filed facts the web session states, because
the Halt 1 cycle log does not carry a numbered entity-count declaration. The
entity-count gate therefore runs a single pass.

## SECTION 2 — PRIMARY CHECKS (web session, live)

- CMP Rs 161.20, BSE close 11-Sep-2026, down 2.39% on the day.
- Market cap Rs 832 cr. P/E 24.5. Dividend yield 3.10%.
- 52-week range Rs 103.05 to Rs 203.00.
- Pledge confirmed live at 94.4% of promoter holding.
- Run `runs/totem-2026-09-09`, branch `run/totem-2026-09-09`. Phase 1 gate
  recommendation REWORK on a confidence delta of 32 against a threshold of 60.
- **Operator ruling: PROCEED.**

## SECTION 3 — BUSINESS UNDERSTANDING NARRATIVE (web session)

A CNC machine is like an expensive printer. It cannot make a metal part on its
own. It needs a cutting tool to drill, thread or shape the metal. That tool is
the printer cartridge. It costs little next to the machine and the part. It
wears out. The customer buys it again.

The tool is cheap but the mistake is expensive. A bad tool stops a costly
machine or ruins a costly part. Kennametal's management puts the customer's
tool cost at never more than about 2% of total product cost, often 1% [MGMT].
So the buyer does not shop on price. He buys the tool that is reliable and
available.

Demand repeats because tools wear out. It rises and falls with how hard
factories run, not with how many machines they buy. Ninety percent of
Kennametal's revenue is consumables [MGMT], so the category is far less
capex-cyclical than it looks.

TOTEM sells two kinds of tools. Premium tools carry real skill: carbide taps,
thread mills, tools shaped for titanium and aerospace metals. Commodity tools
do not: standard drills, spring washers. The profit anchor is the dull,
dominant half, HSS threading taps, where TOTEM is number one in India.

## SECTION 4 — SIGNED MENTAL MODEL (operator signed 16-Sep-2026)

**Archetype: branded industrial consumable with a distribution moat.** Not a
technology company. Not an aerospace supplier. Not a carbide play.

The proof is the channel. TOTEM has the largest distribution network in the
country, 300+ dealers [SECONDARY, trade listings; corroborated AGENCY,
Infomerics "It has the large distribution network in the country"]. Those
dealers are multi-brand. Devi Steel (Bengaluru) carries TOTEM alongside JK
Files, Addison, YG and BPT-ITM. S.S. Sales (Faridabad) carries TOTEM alongside
Ceratizit [SECONDARY]. They choose what to push. TOTEM still holds close to 30%
of the Indian tap market on that shelf. That is a behavioural test, not a
company claim.

This explains the margin puzzle. TOTEM earns about 23% in tooling. Birla
Precision, same size and same products, earns about 5% at segment level [FILED,
screener segment data]. Both make HSS taps and drills. The difference is that
TOTEM's tools sit on more shelves in more towns. For a job shop needing an M8
tap today, availability beats a slightly better tool three days away. Birla has
product but not reach, so it competes on price.

**Dominant variables, four:**
1. Indian manufacturing and capital-goods utilisation, which sets machining hours.
2. Carbide versus HSS mix.
3. Share in taps against Birla, Kennametal and imports.
4. Working capital and cash conversion.

The promoter pledge sits over all four as a structural overhang rather than a
driver.

**The model's own falsifier:** if growth comes mainly from low-moat drills and
spring washers while the premium mix stays flat, this is a cyclical industrial
wearing inflection clothing. The company discloses one segment only [FILED, AR
FY26 Note 38], so this is checkable only indirectly.

**Where the advantages sit versus where the growth is.** The moat is strongest
in general engineering and standard tooling, thousands of small job shops
buying through dealers, the segment Kennametal deliberately stepped back from
during the tungsten shortage because gross margins were poor [MGMT]. The moat
is weakest in carbide and aerospace, where Sandvik and Kennametal compete,
product development matters more than dealer reach, and Kennametal has a
four-year head start with a dedicated team [MGMT]. The durable asset and the
growth ambition point in different directions.

**Development capability, corrected.** Reported R&D is nil, but the company
developed proprietary carbide thread-mill software, deployed Simufact
simulation for forming taps with CAE benchmarking, and built tooling for
titanium, superalloys and high-strength aluminium [FILED, AR FY26]. That is
applied engineering, geometry, software, simulation, not materials science.
TOTEM can develop a better flute geometry for titanium. It cannot develop a
better carbide grade. Kennametal India also spends under 0.5% of revenue on
R&D, but draws on the parent's Latrobe centre [MGMT]. TOTEM has no parent and
no lab.

**People risk on the moat.** FY26 permanent headcount fell 481 to 420.
Attrition about 25% in the lower executive cadre [FILED, ops summary] against
17.24% stated in the board report [FILED, AR FY26]. Conflict unresolved. The
application-engineering layer is people-embedded. A cheaper workforce achieved
through churn in the cadre that carries the moat is not operating leverage. It
is the moat depreciating while the P&L improves.

### PROOF GATE — note for the FTTCP reader

The Halt 1 cycle log does not restate a numeric proof gate. The proof gate the
signed model inherits is the one drafted at 09b Section 2 Part B3 in
`outputs/reports/09b-understanding-dossier.md`:

> Operating margin sustaining above 20% for two consecutive quarters beyond
> Q1 FY27.

The signed model adds its own falsifier, quoted above (growth from low-moat
lines with premium mix flat). FTTCP tests the 09b gate and carries the signed
falsifier beside it.

## SECTION 5 — VERTICAL VERDICTS (nine, web session)

**V1 — Tungsten carbide input [AGENCY/SECONDARY].** Western APT ran about
$390-410/mtu in late Jun-2025, peaked about $3,300/mtu (about $330/kg) and sits
about $3,000-3,075/mtu ($300/kg) since late Jul-2026. Chinese domestic APT
peaked 11-Mar-2026 and corrected 24.6% by 3-Aug-2026. The Western export
benchmark did NOT follow. The market has fragmented, and the 15-firm Chinese
export whitelist through 2026-27 enforces the gap. Structural deficit to 2030.
S&P estimates US$36-48/kg WO3 would support over 85% of accessible supply
against US$340/kg actual, so today's price is a scarcity-and-control premium,
not cost-driven. VERDICT: input cost plateaus high. No material relief inside
FY27. The pre-2025 base does not return within a 3-year projection.

**V2 — HSS steel [SECONDARY]. Correction to an earlier reading.** HSS is not
insulated. It contains 6-18% tungsten. M2 carries about 6.4%, against over 90%
for solid carbide. The exposure is a gradient, not a wall: carbide heavily
exposed, premium cobalt grades (M35/M42) moderately, standard M2 lightly,
carbon steel taps and spring washers not at all. India is volumetrically
self-sufficient in HSS bar but import-dependent for premium grades, with China
the leading supplier by value. OFFSET: every domestic competitor faces the
identical HSS structure, and Birla at 5% margin has no room to absorb, so on
the HSS side the shock should widen TOTEM's advantage over the weak domestic
peer.

**V3 — Cobalt and coatings [SECONDARY].** A second, independent policy squeeze
on the same premium lines. DRC export ban Feb-2025, replaced by a 96,600t
annual quota for 2026-27, roughly half 2024 volumes. Prices about $56,000/t,
more than tripled from lows. Cobalt is the carbide binder and the 5-8% alloying
element in M35/M42. Indian scrap pricing shows the differential: M2 Rs 180-220/kg
against M42 Rs 300-320/kg. Coatings (TiN/TiAlN) are titanium-based, microns
thick, capital-cost dominated, NOT an issue. VERDICT: input inflation is
concentrated exactly in the premium products the strategy wants to grow. The
economics push the portfolio opposite to the strategy. Cobalt has a
demand-destruction release valve via battery chemistry substitution. Tungsten
does not.

**V4 — Auto and auto-components [SECONDARY].** ACMA guides +8-10% for FY27,
down from +12.7% in FY26 (turnover Rs 7.60 lakh crore). Capacity utilisation
74.8% Dec-2025. Car production 2.86mn units Feb-2026, off a Sep-2025 peak of
3.07mn. At Kennametal's stated 1.3-1.4x market-growth algorithm, that implies
about 11-14% tool-demand volume growth. Headwind: the component trade balance
reversed, imports up 13% against exports 5%, China 36% of component imports. A
part imported is a part not machined on an Indian CNC. VERDICT: steady,
decelerating. The sober anchor for the whole forecast.

**V5 — Defence and aerospace [SECONDARY].** Demand is not in doubt: Rs 1.39
lakh crore, 75% of FY27 capital acquisition, earmarked domestic. Defence
production Rs 1.78 lakh crore with private share at a record 24%. 5,500+ items
across five indigenisation lists. Exports past USD 2.5bn growing about 30%. The
Tier-2/Tier-3 machining ecosystem (Aequs, Dynamatic, Azad, Godrej Aerospace) is
adopting 3/4/5-axis and turn-mill. BUT: Kennametal ranks A&D its fastest-growing
market and still imports rather than makes these tools in India. High value,
low volume, one plant serving Germany, France, US and Japan. It explicitly
deprioritised localising where margin expansion would not follow [MGMT].
CORRECTION LOGGED: that is a network-sourcing choice inside an existing global
footprint, NOT a verdict that Indian aerospace tooling is unprofitable. TOTEM
has no alternative plant and serves a domestic market machining more titanium
each year. The real constraint is capability (materials science) and per-SKU
development scale, not geography. No AS9100D evidence found. VERDICT: real
optionality with a long fuse. Do NOT credit material FY27 or FY28 revenue.

**V6 — Railways [SECONDARY].** Capex Rs 2,93,030 cr for FY27, up from
Rs 2,65,200 cr, budgetary-grant funded. Coach production 7,133 in FY25 (+11.2%).
318,196 freight wagons and 84,863 coaches installed. Products are steel,
high-volume, threaded, which is HSS tap and drill territory, and BBBB spring
washers fit the rolling-stock fitting ecosystem. Maintenance demand behaves
like an annuity tied to fleet size, not to new orders. LIMIT: Kennametal's
end-market ranking omits railways entirely, and the vendor base is MSME and
price-sensitive, which constrains pass-through. VERDICT: quality supporting
leg, about 10% growth, more durable than auto. Not a driver.

**V7 — General engineering and the long tail [SECONDARY].** Engineering
exports hit an all-time high USD 122.43bn in FY26, +4.86% (against +6.74%
FY25), decelerating, and Mar-2026 managed just +1.13% amid the Hormuz closure
while overall merchandise exports fell 7.44%. One outlier: engineering exports
+21% YoY in Jun-2026 to USD 11.48bn, uncorroborated but consistent with
Kennametal's mid-teens volume growth and TOTEM's Q1. STRUCTURAL POINT:
Kennametal operates at the top of the pyramid and turned down general-purpose
sales during the shortage because gross margins were poor [MGMT]. The leader is
vacating the volume end where TOTEM lives. CAVEAT: the export basket is
dominated by autos, iron and steel, and non-ferrous (copper), which is smelting
and rolling, not machining, so headline growth overstates machining intensity.
VERDICT: TOTEM's natural home, uncontested by the leader, growing
mid-single-digit structurally.

**V8 — Distribution channel [SECONDARY, strongest evidence in the file].** See
the signed model above. Two qualifications: MachiningCloud and CAM-embedded
tool specification move the spec upstream and weaken the dealer's gatekeeping
role at the top end; and the channel moat matters least in aerospace, where
Kennametal's own engineers work direct and the channel is pure logistics.

**V9 — SP Group and the cap table [SECONDARY].** Goswami Infratech's
Rs 14,300 cr June-2023 zero-coupon at about 18.75% was due Apr-2026. PFC
declined a roughly Rs 20,251 cr loan. A Tata Sons stake sale stayed
early-stage. Maturity slipped twice, with consent sought in late Jun-2026 to
push Rs 143bn past 30 June. Cleared Jul-2026: Rs 25,500 cr local-currency raise
with Farallon, Davidson Kempner and Cerberus, a $1.6bn three-year tranche
through Eqyizen at about 18.95%, secured on Afcons and Tata Sons shares.
VERDICT: refinancing, not deleveraging. Cost rose from 18.75% to 18.95% after
months of difficulty. About Rs 13,500 cr is repayable within 24 months, which
puts the next wall about mid-2028, inside a 3-year hold. The acute window has
passed. The structure has not changed. Corollary: a group paying about 19%
needs subsidiary cash, so the roughly 90% payout will not fall while that debt
stands, which caps how much of the carbide transition TOTEM can self-fund. The
financing structure and the growth constraint are the same fact.

## SECTION 6 — SUPERSESSIONS LOGGED (seven)

1. **Kennametal's margin mechanism.** Originally read as structural integration
   (owned mines and recycling) insulating cost. The 7-Sep-2026 institutional
   investors meeting states it came from a 5-6 month raw-material inventory lag
   plus pricing ahead of cost, with one-time scrap realisations. The CFO warned
   it reverses when tungsten falls and refused medium-term margin guidance.
   Kennametal India's tungsten is 100% imported with no domestic mines. PARTIAL
   RE-CORRECTION: the parent does negotiate tungsten pricing globally for the
   group and recycled feed is used, so a sourcing advantage exists, via
   purchasing scale, not asset ownership. TOTEM, standalone, has neither.
2. **HSS insulation.** Claimed insulated. HSS contains 6-18% tungsten. Revised
   to a gradient (V2).
3. **Aerospace localisation.** Kennametal's import choice was read as a verdict
   on Indian aerospace-tooling economics. It is a network-sourcing decision.
   Corrected (V5).
4. **Non-Chinese provenance upside.** Argued the tungsten controls could hand
   TOTEM a defence-vendor advantage if sourcing were non-Chinese. Infomerics
   confirms carbide AND M35 are imported from China and Germany. Branch closed.
5. **"Nil R&D".** Overstated. Applied engineering exists and is capitalised
   within operations. Materials science does not (see the signed model).
6. **"The market did nothing with Q1."** Superseded. +9.01% to Rs 155.40 on
   8-Sep-2026 on about 7x normal volume, the day after Kennametal's 7-Sep
   institutional meeting. Rs 161.20 by 11-Sep.
7. **August sector rally attribution.** Kennametal India +51% and Birla +37% in
   the month from 2-Aug. Tungsten was flat-to-weak across that window on the
   Western benchmark (European APT $3,000-3,279 on 5-Aug, $2,900-3,275 on
   17-Aug; Chinese market in consolidation since the second half of July). The
   only dated event in that window is the SMM Chinese domestic APT print of
   $79,731.63/t on 3-Aug, down 24.6% from July. Birla rallying 37% on +1%
   revenue fits a commodity-input re-rating better than an earnings one.
   Kennametal's June-quarter result, filed in the same window, fits too.
   TRIGGER NOT ESTABLISHED. Recorded as unresolved rather than assigned.

## SECTION 7 — PROMISE VERSUS DELIVERY

| Management claim | Source | Status |
|---|---|---|
| Drill capacity additions "paid off, seeing substantial growth" | AR FY26 [MGMT] | HIT. Q1 revenue +28.9% |
| Passing on carbide input cost "wherever feasible" | AR FY26 [MGMT] | PARTIAL. Materials 31.8% to 36.1% in Q1 |
| "Stable trend in the export business" | AR FY26 [MGMT] | MISS. FOB exports fell 15.9% to Rs 3,189.46 lakh; the same MD&A concedes US and Mexico tariffs cut sales. Graded the run's one CRITICAL verifier finding; the direction was described wrongly two years running |
| Expanded penetration into aerospace, defence, railways, valves and pumps, die and mould | AR FY26 [MGMT] | PENDING. No product-level or segment disclosure exists to test it |
| High-performance tooling strategy | Stated since FY17 in the former parent's reports | PENDING nine years. The strategy is not the inflection |

## SECTION 8 — FY27 PROJECTION (operator-set)

Revenue about **Rs 300 cr** (+ about 20% on FY26's Rs 251 cr). PAT about
**Rs 40 cr**. EPS about Rs 7.75 on 5.16 cr shares, which is about **20.8x at
Rs 161.20**.

Basis and the caution that goes with it. Against reported FY26 PAT of
Rs 28.8 cr this is +39%, but FY26 carried the Rs 5.9 cr pre-tax Labour Codes
charge. Adjusted FY26 PAT is about Rs 33 cr, so like-for-like growth is about
**21%**. Roughly half the apparent growth is the absence of a one-off, not
operating improvement.

Bear about Rs 33 cr (flat on adjusted FY26) if carbide pass-through fails
against hedged competitors. Bull about Rs 44 cr if materials return toward
32-33%, which now requires TWO policy regimes to loosen, Chinese tungsten
licensing and DRC cobalt quotas, neither forecast before 2027.

The current price already discounts the base case landing.

Input regime note carried from the Key Notes entry: blended pass-through
estimated 70-80%, lagged 2-3 quarters. Materials should drift from 36.1% toward
33-35%.

## SECTION 9 — GATE PRE-RULINGS (Section 1B pillar inputs)

**NO DOSSIER PRE-RULING.** The Halt 1 cycle log carries no per-pillar gate
pre-ruling: no P/E base per pillar, no cash multiplier band, no growth premium
or Amendment 16 call, no earnings basis, no sector cap row, no option inputs,
and no Amendment 17, 18 or 19 treatment.

The P/E BASE CARD must therefore print "no dossier pre-ruling" against every
pillar input and show the Claude Code draft alone, with the operator ruling on
one column instead of two.

## SECTION 10 — TRACKER PROOF (Role 5.5)

Six rows written to DOWNSTREAM SIGNAL TRACKER on 16-Sep-2026, all linked to
COMPANIES MASTER page `3d6bb2b9-d3ab-81c9-956f-cf3a79435cdf`.

| Row ID | Signal | Tier | Next check |
|---|---|---|---|
| 3ddbb2b9-d3ab-8199-ada3-c273eebc660b | materials ratio vs APT | T1 | 15-Nov-2026 |
| 3ddbb2b9-d3ab-8191-a258-d87b6cc5f04d | inventory conversion H1 FY27 | T1 | 15-Nov-2026 |
| 3ddbb2b9-d3ab-810d-9340-e71162bd61c7 | promoter pledge % | T1 | 21-Oct-2026 |
| 3ddbb2b9-d3ab-8197-9a10-ea2dcd786a81 | SP Group 2028 maturity wall | T1 | 31-Mar-2027 |
| 3ddbb2b9-d3ab-81a1-89c8-e31a19147b04 | attrition / app-eng headcount | T2 | 15-Jul-2027 |
| 3ddbb2b9-d3ab-819c-b454-cb35484e0dc0 | premium-mix / AS9100D | T2 | 15-Jul-2027 |

**Tracker gate: SATISFIED.**

## SECTION 11 — CONFLICTS THE WEB SESSION LEFT UNRESOLVED

- Promoter holding 72.56% (COMPANIES MASTER page) against 73.85% (shareholding
  filing and screener).
- FY26 attrition 17.24% (board report) against about 25% in the lower executive
  cadre (ops summary).
- Birla FY26 annual report missing from the corpus (collector-deleted), worked
  around with screener segment data.
- Promoter SAST direction unknown: five Regulation 29(2) filings plus one
  29(1) across two years. The Key Notes entry of 16-Sep-2026 records the five
  Reg 29(2) filings as pledge creations.
- About Rs 16 cr of Rs 46.7 cr two-year capex does not tie to the asset base.

## SECTION 12 — PRICE AND DECISION STATUS

- Price Rs 161.20, BSE close 11-Sep-2026. Market cap Rs 832 cr.
- COMPANIES MASTER Current Market Price updated 144 to 161.2. Analysis Date
  Sep-26.
- **Decision Status: blank. The operator ruling is pending.** The web session
  records that the framework's rules point at WATCHLIST with two re-engage
  triggers now sitting as tracker rows, and that the call is the operator's.
