# MENTAL MODEL DECLARATION v2: SHHARICH (Shree Hari Chemicals Export Ltd, BSE 524336)

DRAFT - PENDING OPERATOR SIGN-OFF

Phase 2b rebuild, 2026-09-09. Run: runs/shharich-2026-09-05. Supersedes the Section 2
declaration in outputs/reports/09b-understanding-dossier.md.

Scope. Understanding layer only. No valuation, no entry range, no Decision Status, no
transition posture. Halt 1 still holds. Nothing here proceeds to /fttcp until this model
is signed and, separately, the stage 5 and stage 6 REWORK closes.

Framework basis. Section 1B v3.10 Amendment 26 (growth symmetry, the 2D standing check),
Master Prompt v3.7 Rule G (Entrepreneur Ledger), Rule H (steelman ordering: bull built to
depth first), Rule F (second-order chains), Amendment 17 (converter treatment). Merged to
this branch at commit f40268d before this rebuild ran.

Rules cited by the operator that this repository does not define: Investigation Stance,
unknowns ledger, Rule A, Part 2.6, the unasked block. The repo copy of the team workflow
manual is v2.2 and carries none of them. They are applied here exactly as the operator's
instruction describes them. The repo copy needs syncing with the claude.ai project text.

Evidence tiers used throughout. FILED = a filing in this run's corpus, page anchored.
PRESS = named press or trade report, dated. AGGREGATOR = market pricing or research
aggregator, weakest documentary tier. PEER CALL = peer transcript in corpus, call dated.
[INFERENCE] = reasoning by this session, labelled, never a substitute for a fact.
NOT DISCLOSED = the corpus does not carry it. NOT CONFIRMED = live web could not verify it.

---

## INVESTIGATION STANCE

### The decision this feeds

Two decisions, both the operator's, neither taken here.

1. The Mental Model Declaration for Halt 1 sign-off. Signing fixes the FROM state, the
   engine, the proof gate, and the two falsifiers that every later stage tests against.
2. The transition posture carried into Stage 11. The posture needs three state variables.
   Two are settled below (ugliness, and the proof gate's status). The third, the
   recognition gap, resolves only at Stage 11. Posture is therefore NOT assigned here.

What this rebuild changes. Phase 1 read FY26's 4.8% organic manufactured growth as the
verdict on the transition. FY26 is almost entirely pre-flip. Reading it as the verdict is
the failure Amendment 26 names, and the reason for this rework.

### Unknowns ledger, resolved before section 1

| # | Unknown | Status | Finding | Tier and date |
|---|---|---|---|---|
| 1 | H-Acid India-to-China trade direction | RESOLVED (direction) | China turns net importer of H-Acid in September 2026, reversing a multi-year net-export position. Chinese H-Acid moved from about 40,000 yuan/tonne at the start of 2026 to about 100,000 yuan/tonne by end-August 2026, roughly +150% in eight months. | PRESS, two independent sources, Sept-2026: a named industry commentator (Ajay Joshi Chemicals) and Indian trade press reporting a Chinese H-Acid shortage. Direct page fetch blocked by the container egress proxy; both read via search index. |
| 1b | India-to-China volume | UNRESOLVED | Best available: India exported over 18,000 MT of H-Acid and derivatives in calendar 2023, +12% YoY. A peer put the India-to-China flow at 7,000 to 8,000 tonnes beginning June or July 2025. No monthly DGCIS series obtained. | AGGREGATOR (2023 figure) and PEER CALL (SHREEPUSHK Q3 FY26, 12-Feb-2026, Punit Makharia). Trade-data sites blocked. |
| 2 | China VAT-refund withdrawal on H-Acid | NOT CONFIRMED, and demoted | China ended export VAT rebates across 249 categories effective 01-Apr-2026. Every category list obtained names solar PV, batteries, refined oil, non-metallic minerals, e-cigarettes and solar or battery linked chemicals such as methanol, ethylene glycol, PVC and BDO. No source places H-Acid or dye intermediates in the withdrawn list. | PRESS and official summaries, Jan to Apr 2026. The peer's Feb-2026 attribution of the flip to VAT withdrawal is not corroborated at product level. |
| 2b | The flip's actual mechanism | RESOLVED to a different cause | Chinese environmental regulation has cut domestic dye and dye-intermediate output by roughly 50% to 60%, and China now imports H-Acid and vinyl sulphone from India. Compounding causes named: naphthalene and sulphuric acid feedstock cost, tighter factory output, seasonal demand. | AGGREGATOR, 2026. Weakest tier of the three load-bearing findings, and the one most worth a primary check. This distinction decides the durability window in section 5. |
| 3 | Peer or trade-body confirmation of an Indian export step-change in the Jun/Sep 2026 quarters | PARTIAL | Bodal Chemicals Q1 FY27 (quarter to Jun-2026, results 05-Aug-2026): standalone revenue Rs 704 cr, highest ever, +57% YoY; EBITDA Rs 74 cr, +43%; PAT Rs 28.78 cr, +178%; management cites consistent volume, improved realisation, and full pass-through of rising raw-material cost. Confirms the price regime at a peer. Does not isolate exports. No CHEMEXCIL or DGCIS series obtained. | PRESS, 05-Aug-2026. Peer-level, not export-specific. |
| 4 | The 25-Aug-2026 board outcome | RESOLVED | Board 25-Aug-2026 approved 22,85,000 convertible warrants at Rs 176.10 each, aggregating Rs 40,23,88,500, convertible into one equity share of Rs 10 each at a premium of Rs 166.10, within 18 months of allotment. Also approved expansion and set-up in existing and new units for dye and dye intermediates and other organic and inorganic chemicals. No capacity figure disclosed in any source. | PRESS (EquityBulls, Aug-2026) agreeing line for line with FILED corpus text (AR FY26 AGM Notice Item 16, pp. 43 to 48). Two independent sources, exact match. The Reg 30 filing itself remains absent from the corpus. |
| 5 | The 270-tonne capacity unit of time | RESOLVED as PER MONTH, by arithmetic exclusion plus two convergent checks | See the box below. Reading it as per annum is arithmetically impossible. | [INFERENCE] from FILED revenue plus PRESS peer disclosures. Not a filed unit. |

**Unknown 5, worked.** The AR states "270 TONNES PRODUCTION CAPACITY AT OUR
STATE-OF-THE-ART MANUFACTURING FACILITY AT MAHAD, RAIGAD" with no unit of time (FILED, AR
FY26 p. 5), and a growth chart reading 30 tonnes at inception in 1989 to 270 tonnes current
(FILED, AR FY26 p. 8). The AR discloses no production volume, no utilisation and no
realisation anywhere in 181 pages, confirmed by direct search of the extracted text.

- Exclusion. Manufactured H-Acid revenue was Rs 14,476.45 lakh in FY26 (Note 35.2 H-Acid
  Rs 17,826.28 lakh less traded goods Rs 3,349.83 lakh; FILED, AR FY26 pp. 122 and 126).
  Read as 270 tonnes per annum, implied realisation is about Rs 53.6 lakh per tonne, near
  Rs 5,360 per kg. Observed world H-Acid prices in the same window run Rs 450 to Rs 680 per
  kg. The per-annum reading requires a realisation roughly ten times the world price. It is
  excluded.
- Convention check. Indian H-Acid peers denominate capacity per month. Bhageria Industries
  disclosed under Reg 30 on 08-Oct-2025 an increase from 400 MT/month to 500 MT/month at its
  Tarapur/Boisar plant, Rs 5 crore, six months, against utilisation then running near 95%
  (PRESS, 08-Oct-2025).
- Calibration check. That same disclosure prices 100 MT/month, 1,200 MT/year, at Rs 50 to
  55 crore of revenue, implying Rs 417 to 458 per kg as at Oct-2025. Applying that band to
  SHHARICH's FY26 manufactured H-Acid revenue implies 3,160 to 3,470 tonnes for the year,
  or 263 to 289 tonnes per month, against a stated 270. The two readings coincide.

Conclusion: capacity is about 270 tonnes per month, near 3,240 tonnes per year, and FY26
ran at high utilisation. This is an [INFERENCE] and is load bearing for everything below.

### Unresolved residue, stated as the uncertainty of this model

1. No filed unit of time for capacity, and no filed production volume in any period. Every
   volume and utilisation statement below is derived, not disclosed.
2. No monthly India-to-China H-Acid trade series. The direction is corroborated twice; the
   magnitude is not.
3. The flip's mechanism rests on aggregator-tier sourcing. If the cause is a permanent
   Chinese environmental curb the window is multi-year. If it is feedstock shortage and
   seasonal demand the window is a few quarters. The evidence does not yet separate them.
4. No primary results filing has ever entered this run. FY26 audited annual results and
   Q1 FY27 results are both absent; the Q1 FY27 figures used here come from the screener
   quarterly row and press reporting of the filing, not the filing.
5. SDPL discloses no capacity, no product mix and no commissioning date.

---

## 1. ARCHETYPE, PER LINE

The operator's two readings are (a) a sub-scale commodity intermediate maker with a thin
moat and a resale-flattered top line, and (b) a small maker positioned in a genuine H-Acid
regime flip, adding capacity into a market its low-cost competitor just left.

These are not two archetypes. Both are the same archetype from the CLAUDE.md library,
COMMODITY CONVERTER, and Amendment 17 binds under either. They differ on two things the
archetype does not carry: position in the cycle, and whether the competitor's exit is
durable. Resolving (a) against (b) by choosing an archetype would be resolution by fiat.
The archetype is settled; the rung and the durability are the live questions.

| Line | Share of FY26 revenue | Archetype | Where the model is soft |
|---|---|---|---|
| Manufactured H-Acid | Rs 14,476.45 lakh, 78.5% | COMMODITY CONVERTER. Margin is the spread of H-Acid realisation over the naphthalene and sulphur input basket. No patent, no brand, no customer-specific specification disclosed (FILED, AR FY26; B01 moat scan fails cost position, scale and brand). | The rung. Under (a) it sits at R1, a price taker whose ROCE cycles around the cost of capital. Under (b) the left side of the world cost curve has been removed by regulation, and a surviving compliant producer can hold R2 economics for as long as that removal lasts. Nothing in the corpus settles which. |
| Traded H-Acid resale | Rs 3,349.83 lakh, 18.2%, nil in FY25 | Fits no archetype in the library. A pass-through at about 1.03% gross margin with no processing step. | Its MEANING, not its economics, is what splits (a) from (b). See below. |
| By-products, gypsum, iron sludge, globular salt to the cement industry | Rs 225.82 lakh, 1.2% | Waste monetisation attached to the zero liquid discharge plant. | Small in revenue, large in what it implies about compliance. See section 5. |

**The resale line carries the whole disagreement.** Phase 1 read it one way only, as top-line
flattery that masks 4.8% organic growth. That reading is available. A second reading is
equally available on the same facts and Phase 1 never tested it. If the plant was full at
about 270 tonnes per month, a customer asking for more than the plant can make leaves two
choices: refuse the order, or buy finished H-Acid and pass it through at cost to hold the
customer. A 1.03% margin is what customer retention looks like, not what trading for profit
looks like. Under reading (a) the resale line is cosmetic. Under reading (b) it is a symptom
of a binding capacity constraint, and it is evidence FOR the capacity case, not against it.

**The single observation that separates (a) from (b).** Not organic growth, and not the
resale line's size. The separator is realisation per tonne against disclosed volume, or its
only available proxy: manufactured H-Acid revenue growth measured against the change in the
external H-Acid price index over the identical window.

- If manufactured revenue growth is at or below the price-index change, volume is flat or
  falling. The plant is full or under-loaded, and reading (a) governs on the resale point:
  there is no volume story until new capacity lands.
- If manufactured revenue growth materially exceeds the price-index change, tonnes rose.
  Since 270 tonnes per month caps the existing plant, tonnes can only rise if new capacity
  commissioned. That is reading (b) with the capacity leg proven.

One filed number closes it outright: any disclosure of tonnes produced or sold, or of
capacity utilisation, in any future filing. The company has never published one.

---

## 2. THE TRANSITION

### 2.1 The flip, as a dated and tiered sequence

Phase 1 built this sequence from peer transcripts alone and got three links wrong. The
corrected sequence follows. Withdrawn and re-dated items are marked.

| # | Event | Date | Source and tier |
|---|---|---|---|
| 1 | India net-exporting H-Acid to China begins | June or July 2025, stated retrospectively | PEER CALL. SHREEPUSHK Q3 FY26 call, 12-Feb-2026, Punit Makharia, 7,000 to 8,000 tonnes. Uncorroborated on magnitude. |
| 2 | Indian H-Acid producers running near full | 08-Oct-2025 | PRESS. Bhageria Reg 30 disclosure, utilisation near 95%, expanding 400 to 500 MT/month. |
| 3 | Chinese H-Acid price starts climbing | from January 2026, about 40,000 yuan/tonne | PRESS, Sept-2026, retrospective. |
| 4 | Feedstock shock reaches Indian converters | late February 2026 onward | PEER CALL. SHREEPUSHK Q4 FY26 call, 19-May-2026: sulphur and ammonia up two to four times. Verifier B re-dated this: the sulphur chain was FLAT through Q1 FY26 and turns sharp only from late Feb-2026. |
| 5 | H-Acid and related intermediate prices rise 40% to 45% | February to August 2026 | PEER CALL, corroborated by AGGREGATOR: India H-Acid USD 7,238/MT in June 2026, China USD 6,679/MT, Belgium USD 7,623/MT. |
| 6 | Peer regime turns explicitly price-led, volume given up | Q1 FY27, quarter to Jun-2026 | PEER CALL. SHREEPUSHK Q1 FY27 call, 13-Aug-2026: chemical volume down 38.6% YoY, revenue up 17.1% YoY. |
| 7 | Chinese price reaches about 100,000 yuan/tonne | end-August 2026, about +150% in eight months | PRESS, Sept-2026. |
| 8 | China turns net importer of H-Acid | September 2026 | PRESS, two independent sources, Sept-2026. This is the flip's clearest single marker and it post-dates the entire corpus. |

Withdrawn or corrected from Phase 1, not carried forward:

- WITHDRAWN. "Both peers describe a lag between input cost and price pass-through." Bodal
  states pass-through runs in tandem with sulphur, not lagged (PEER CALL, Bodal Q4 FY25
  call, 29-May-2025). Only Shree Pushkar described a lag, and only for its fertiliser leg.
- RE-DATED. The cost shock was dated to H2 FY26 generally. It is flat through Q1 FY26 and
  sharp only from late February 2026, which places most of it in Q4 FY26 and after.
- RE-DATED. The volume-led to price-led flip was dated to Q3 FY26. That quarter was
  volume-led at the peer: volume up 75.6% with realisations down 21% (PEER CALL, SHREEPUSHK
  Q3 FY26 call, 12-Feb-2026). The regime turn belongs in Q1 FY27, item 6 above.
- UPGRADED from UNVERIFIABLE. Phase 1 graded SHHARICH's export step-change unverifiable and
  called peer silence informative. Two things overturn that. The peer record carries the
  sector explanation (item 1). And the company's own audited accounts corroborate the
  exports directly: Export Benefit of Rs 161.99 lakh appears in FY26 revenue against nil in
  FY25 (FILED, AR FY26 Note 27, p. 122), alongside Export of Goods on FOB basis of
  Rs 8,554.32 lakh against nil (FILED, Note 35.9, p. 130). Export incentives do not accrue
  without exports. The step-change is FILED, not unverifiable.
- DEMOTED. The VAT-refund attribution. See unknowns ledger item 2.

### 2.2 The standing check, applied in writing

Section 1B v3.10 Amendment 26, 2D standing check: "Did the base case credit the transition,
or price the audited past? If base revenue equals historical CAGR at trailing-average
margins for a name with run-rate, order-book, or capacity evidence, the projection is wrong.
Rebuild."

Phase 1's answer priced the audited past, and here is the mechanism. FY26 runs from
01-Apr-2025 to 31-Mar-2026. On the sequence above, the Chinese price move starts in January
2026 and the trade reversal lands in September 2026. At most one quarter of FY26, Q4, holds
any part of the flip, and the feedstock shock that hit margin arrives in the same quarter.
FY26 is the PRE-FLIP BASELINE. Taking FY26's 4.8% organic manufactured growth as the verdict
on the transition tests the transition against a year that ended before the transition began.

There is a second, sharper form of the same error. On the capacity finding above, the plant
was substantially full through FY26. A full plant cannot grow volume. Its 4.8% revenue growth
is the ceiling of the pre-flip asset, not a statement about demand, management or the
transition. Phase 1 read a capacity ceiling as a demand verdict.

**The window the transition actually shows in.**

| Period | What it can show | Status |
|---|---|---|
| Q4 FY26, to 31-Mar-2026 | First contact with the flip, with the feedstock shock arriving at the same time. Margin, not volume. | Printed. Revenue Rs 41.22 cr, operating profit Rs 0.45 cr. Weak. |
| Q1 FY27, to 30-Jun-2026 | The price leg, on an unchanged plant. | PRINTED, and it is the first real evidence. Revenue Rs 54.91 cr, +125.78% YoY; operating profit Rs 8.48 cr, 15.4% margin against 5.31% for FY26; PAT Rs 5.92 cr against a loss of Rs 1.67 cr a year earlier. |
| Q2 FY27, to 30-Sep-2026, reporting around Nov-2026 | The first clean full quarter inside the flip, and the first quarter overlapping China turning importer. | NOT YET PRINTED. This is the load-bearing observation. |
| Q3 and Q4 FY27 | Whether the regime holds once Indian supply responds. | NOT YET PRINTED. |
| SDPL first turnover, undated | The volume leg. The only route to tonnes above 270 per month. | NOT DISCLOSED. No capacity, no commissioning date. |

### 2.3 The bull path, built first and to depth

Built under Rule H ordering and Amendment 26.3. Inputs are the most evidenced path. No input
is shaded downward. Conservatism belongs in position size at Stage 11 under Amendment 25, not
here. This is a model input, not a valuation, and it produces no fair value and no multiple.

**Revenue basis declaration, Amendment 26.1.**

| Basis | Available | Value | Evidence |
|---|---|---|---|
| RUN-RATE | YES, indicated basis | Q1 FY27 annualised, Rs 54.91 cr x 4 = Rs 219.6 cr | Screener quarterly row and press reporting of the 14-Aug-2026 filing. The filing itself is absent from corpus, so the basis is one tier below what 26.1 asks for. Named as a live-verify item. |
| CAPACITY | NO | Not computable | SDPL has environmental clearance but no disclosed capacity, product mix or commissioning date. This is the missing input that would let the bull path carry volume. |
| ORDER-BOOK | NO | Not applicable | Spot-priced commodity intermediate, no order book disclosed. |
| GUIDANCE-DISCOUNTED | NO | Not applicable | No earnings call, no guidance with a period. The only forward number is a Schedule V remuneration justification of "approximately Rs 10 crore" profit, which is not operating guidance. |
| HISTORICAL, cross-check only | Computed | FY24 Rs 138.33 cr to FY26 Rs 184.50 cr, 15.5% CAGR, giving Rs 213.1 cr | Screener annual columns. |

Divergence between the chosen basis and the historical cross-check is 3.0%, inside the 10
percentage point threshold, so no divergence flag is raised. The two bases nearly agreeing
is itself worth noting: the run-rate is not an aggressive number.

**Decomposing Q1 FY27, the only flip evidence in hand.** Capacity caps the quarter at about
810 tonnes. At Rs 54.91 crore of revenue that is about Rs 6.78 lakh per tonne, near Rs 678
per kg, against a quoted India H-Acid price of USD 7,238 per tonne in June 2026. The two sit
within roughly 10% of each other. Read plainly: Q1 FY27 is a full plant at flip prices.
Volume growth above 810 tonnes in the quarter is not possible without new capacity, and none
has commissioned. Modest volume growth within the cap cannot be excluded, and would show as
implied realisation falling below the world price. [INFERENCE], from FILED revenue and
AGGREGATOR price.

**The price leg, on an unchanged plant.** 3,240 tonnes a year is the whole of it.

| Realisation | Manufactured H-Acid revenue at full plant | Reference |
|---|---|---|
| Rs 447/kg, FY26 implied | Rs 144.8 cr | The pre-flip baseline, actual |
| Rs 530/kg, upper end of the FY26 peer band | Rs 171.7 cr | PEER CALL band |
| Rs 678/kg, Q1 FY27 implied | Rs 219.7 cr | Held for a full year |

The price leg alone is worth roughly Rs 75 crore of annual revenue on a plant that does not
change. That is the bull case's first and best-evidenced element, and Phase 1 never computed
it because it treated the flip as absent.

**The volume leg.** NOT QUANTIFIABLE. SDPL's capacity is not disclosed in the annual report,
the AGM notice, the environmental clearance reporting, or any press item obtained. The
warrant issue's own largest object is Rs 10.24 crore for expansion in existing and new units,
with a tentative utilisation timeline to March 2031, and it too carries no tonnage. Any
number placed here would be invented. State NOT DISCLOSED and name the document: the SEIAA
environmental clearance for Shakambhari Dyechem Private Limited, which by statute states
product-wise capacity.

**Margin.** The bridge in Amendment 26.2 does not govern this name. Amendment 26.2 preserves
the v3.5 cyclical override, which supersedes the bridge for any sector flagged cyclical:
base is the full-cycle average margin, bear is the cycle trough, bull is the cycle peak.
H-Acid is cyclical on every reading in this run. Stage 11 owns those three numbers. What the
model hands Stage 11 is the observed range and its composition:

| Point | Margin | Composition |
|---|---|---|
| FY26 blended, as reported | 5.31% EBITDA to turnover | Includes the 1.03%-margin resale line at 18.2% of revenue |
| FY26 manufactured only | about 6.3% | [INFERENCE], removing the resale line from the blend |
| FY26 strict operating, excluding other income | 3.57% | B01, and the reason other income at 57.7% of PBT matters |
| Q1 FY27 as printed | 15.4% operating | Full plant, flip prices, feedstock shock already inside it |

The FY26 to Q1 FY27 move of roughly 900 basis points is not a bridge built from assumptions.
It is a printed quarter. What is unknown is not whether the flip drops to margin, but for
how long, which is section 5.

### 2.4 This remains a hypothesis

The transition is stated, not established. Three things are true at once: the flip is real
and dated; the company's participation in it is evidenced for exactly one quarter; and the
volume leg has no disclosed capacity behind it at all.

**Must be live-verified before the transition is treated as real.**

1. The Q1 FY27 results filing itself, from BSE, 14-Aug-2026. The run has never read a
   primary results filing. Confirm revenue, the manufactured versus traded split if given,
   and any volume or utilisation disclosure.
2. The SEIAA environmental clearance for Shakambhari Dyechem Private Limited. It states
   product-wise capacity by statute. This single document converts the volume leg from
   NOT DISCLOSED to a number.
3. The 25-Aug-2026 Reg 30 board outcome from BSE, to confirm the warrant terms against the
   AGM notice text and capture any capacity or product detail the press summary dropped.
4. Whether H-Acid or dye intermediates appear in China's 01-Apr-2026 VAT-rebate withdrawal
   list, at HS-code level. This decides whether the peer's stated mechanism survives.
5. A monthly India-to-China H-Acid trade series from DGCIS, to size the flow the direction
   finding rests on.
6. Chinese H-Acid price now, against the roughly 100,000 yuan/tonne end-August level. The
   single best forward read on the durability window.
7. Whether the Chinese environmental curb on dye-intermediate output is a standing measure
   or a campaign, and its stated duration.

**The confirming and killing observation.** The operator named double-digit organic
manufactured growth with resale stripped as the confirmer, and about 5% organic under a
bigger headline as the killer. That gate does not work inside a price flip, and this is worth
stating plainly rather than adopting it. On a full plant, manufactured revenue growth goes
double-digit on price alone: H-Acid realisation rose about 40% to 45% between February and
August 2026, so the gate is passed by the spread cycle, which is the exact thing the run
exists to exclude. The gate as written would confirm the transition on evidence that proves
the opposite.

The gate that works, same observation, price-adjusted:

- CONFIRMS. Manufactured H-Acid revenue growth exceeding the H-Acid price-index change over
  the identical window, in the Q2 FY27 print (quarter to 30-Sep-2026, reporting around
  Nov-2026). Excess over the price change is tonnes, and tonnes above 810 per quarter can
  only come from new capacity.
- KILLS. Manufactured H-Acid revenue growth at or below the price-index change, with SDPL
  still at nil turnover. The company is then riding the spread on a full plant, which is a
  cyclical converter and not a transition.
- CLOSES IT OUTRIGHT, either way. Any filed disclosure of tonnes produced or sold, or of
  capacity utilisation.

Transition posture is NOT assigned here. It needs the recognition gap, which resolves only
at Stage 11.

### 2.5 Second-order chains (Rule F stub, three chains)

Rule F sets a floor of five chains for Role 2, Role 6 and FTTCP. Halt 1 sits earlier than
all three. Three chains are drafted here from corpus and live web; chains 4 and 5 are built
in claude.ai before Role 2.

```
CHAIN 1: China turns net importer of H-Acid in September 2026 [PRESS, Sept-2026, two sources]
Link 1 [AGGREGATOR]: Chinese environmental regulation has cut domestic dye and dye-intermediate output by about 50% to 60%, and China now imports H-Acid and vinyl sulphone from India.
Link 2 [PRESS]: Chinese H-Acid moved from about 40,000 yuan/tonne in January 2026 to about 100,000 yuan/tonne by end-August 2026.
Link 3 [INFERENCE]: A converter whose largest global competitor is removed from the supply side captures rent through realisation, not through share, because its own tonnes are capped. The rent accrues to every compliant Indian producer at once and is therefore a sector rent, not a company advantage.
Binding constraint: 270 tonnes per month of installed capacity [INFERENCE from FILED revenue], with no commissioned addition. SHHARICH cannot convert the rent into tonnes until SDPL runs.
Unsaid: the FY26 annual report never mentions the flip, never names an export destination, and never discloses a volume. Management wrote a 181-page report about a business whose price was about to double and said nothing about price.
Observation that confirms or breaks this chain, and confirm-by date: Chinese H-Acid price and China's monthly trade position. A return toward 40,000 yuan/tonne breaks it. Confirm-by: Q2 FY27 print, around Nov-2026.
```

```
CHAIN 2: A new resale line of Rs 3,349.83 lakh appears in FY26 at about 1.03% gross margin, nil in FY25 [FILED, AR FY26 Notes 27 and 30]
Link 1 [FILED]: Note 35.2 books it inside a table headed "Manufactured Goods", so the H-Acid line of Rs 17,826.28 lakh mixes 14,476.45 lakh made with 3,349.83 lakh bought.
Link 2 [INFERENCE]: A converter at high utilisation that buys finished product to resell at about 1% is not trading for profit. It is holding a customer it cannot supply from its own plant.
Link 3 [INFERENCE]: If that reading is right, the resale line is a capacity-shortage signal and should shrink when SDPL commissions, and reappear in any period demand exceeds 270 tonnes a month.
Binding constraint: working capital. The current ratio stayed below 1.0 in both years, 0.87 then 0.81 standalone, so buying product to resell consumes the scarcest thing the balance sheet has.
Unsaid: no customer is named anywhere, no concentration is disclosed, and the annual report never explains why the line exists at all.
Observation that confirms or breaks this chain, and confirm-by date: whether the traded-goods line persists, grows or disappears in FY27, read against SDPL's turnover. Confirm-by: FY27 annual report.
```

```
CHAIN 3: Export of goods on FOB basis of Rs 8,554.32 lakh in FY26 against nil in FY25, with Export Benefit of Rs 161.99 lakh appearing in revenue for the first time [FILED, AR FY26 Notes 27 and 35.9]
Link 1 [FILED]: Export incentive income does not accrue without exports. The incentive line is independent audited corroboration that the exports happened.
Link 2 [FILED, contradiction]: The same annual report's Note 35.13 states the company has no major foreign currency exposure and does no hedging, while other income carries a foreign exchange gain of Rs 169.32 lakh.
Link 3 [INFERENCE]: An unhedged export book at 46.4% of revenue makes reported margin partly a currency outcome. In a period when realisation is rising in dollars, currency and price are confounded in the same line, and neither the annual report nor any filing separates them.
Binding constraint: the absence of a hedging policy. There is no mechanism disclosed that would protect the flip's rupee value if the rupee strengthens.
Unsaid: the four export destination countries are counted on page 5 and never named. Tariff exposure cannot be assessed, and United States tariff action on Indian chemical exports is live.
Observation that confirms or breaks this chain, and confirm-by date: whether FY27 disclosure names export geographies or introduces a hedging policy, and whether other income normalises from 57.7% of profit before tax. Confirm-by: FY27 annual report.
```

Stub carries 3 of the Rule F floor of 5. Chains 4 and 5 are built in claude.ai with live web,
before Role 2. Every confirm-by line above feeds the Amendment 23 Expectation Ledger and the
Role 5.5 tracker.

---

## 3. THE MENTAL MODEL, FIVE PARTS

### 3.1 Archetype per line

- Manufactured H-Acid, 78.5% of FY26 revenue: COMMODITY CONVERTER. Amendment 17 binds.
  FROM rung R1, commodity price taker. Claimed TO rung R2, cost-advantaged converter. One
  rung, consistent with the one-rung-per-two-to-three-years base rate.
- Traded H-Acid resale, 18.2%: fits no archetype. Carried as a capacity-constraint indicator,
  not as a business line.
- By-products to the cement industry, 1.2%: waste monetisation attached to zero liquid
  discharge. Carried for what it says about compliance standing, not for its revenue.
- Shakambhari Dyechem Private Limited: a plant awaiting commissioning. **Flagged as a
  candidate CONVERTER slice under Amendment 17.** Where the classification is ambiguous it
  defaults to CONVERTER. Stage 11 values it as a converter slice, not at core PE. Nil
  turnover, a small loss, and construction in progress already aged into the one to two year
  bucket.

### 3.2 Dominant variables

1. **Realisation per tonne of manufactured H-Acid.** The flip's entire transmission into this
   company. Currently derived, never disclosed. Proxy: manufactured H-Acid revenue against
   the external H-Acid price index over the same window.
2. **SDPL commissioning date and its disclosed capacity.** The only route to tonnes above
   about 270 a month, and therefore the only route to a transition that is not the spread.
3. **Durability of China's supply withdrawal.** Decides whether the realisation gain is a
   regime or a spike, and it is the variable this model is least able to observe.
4. **Promoter capital follow-through.** The balance 75% of the warrant issue, roughly
   Rs 30.18 crore, inside 18 months of 25-Aug-2026. It is the family's own money voting on
   the two variables above.

### 3.3 The plain analogy

Shree Hari runs one chemical plant at Mahad that turns naphthalene-chain feedstock and acid
into H-Acid, the building block dye makers need to colour cotton, wool and nylon. It earns
the gap between what the feedstock costs and what H-Acid sells for, and it has almost no say
over either price. For years the world's cheapest supply came from China. During 2026 China's
own environmental rules shut a large part of that supply down, Chinese H-Acid prices roughly
doubled and a half, and by September China was buying H-Acid rather than selling it. That is
a windfall for every Indian maker with a compliant plant. Shree Hari's problem is that its
plant is already close to full, so it can take the higher price but it cannot sell more
tonnes. It is building a second plant through a subsidiary to fix exactly that, funded by the
family putting its own money in. The second plant has been under construction for over two
years and has produced nothing yet, and the company has never told anyone how big it will be.

### 3.4 What the model rejects as noise

- **The resale line as growth.** Rs 3,349.83 lakh at about 1.03% margin is not revenue in any
  sense that matters. It is read only as a capacity signal, and it is stripped from every
  growth measurement.
- **The foreign exchange gain of Rs 169.32 lakh** inside other income, and other income at
  57.7% of profit before tax more generally. FY26 profit is not an operating result and is
  not used as one.
- **Headline revenue growth of 30.7%.** Composed, not earned.
- **Market sizing.** The Phase 1 work found addressable-market headroom of about 8 times
  current revenue. Headroom is not the binding constraint and the model declares the question
  noise. The constraints are installed tonnes and cycle durability.
- **FY26 as a verdict on anything forward.** It is the pre-flip baseline. It sets the level
  the projection starts from and says nothing about the transition.

### 3.5 The model's own falsifier

Two falsifiers, kept separate.

**Transition falsifier.** Manufactured H-Acid revenue growth at or below the H-Acid
price-index change in the Q2 FY27 and Q3 FY27 prints, with SDPL still reporting nil turnover.
That is a full plant riding a spread, and the climb never started.

**Business falsifier**, which would force re-declaring the FROM business itself. Either of:
promoter-family cash extraction staying above 100% of standalone profit before tax for a
second consecutive year while the current ratio still does not recover above 1.0; or any
drawdown against the Rs 100 crore related-party ceiling toward Shubhlaxmi Dyetex Private
Limited, an entity with nil turnover and about Rs 1,163 crore of net worth and no disclosed
business connection to H-Acid. Either would say the listed company is a capital-allocation
vehicle for the family group rather than an H-Acid manufacturer, independent of whether the
flip is real.

---

## 4. ENTREPRENEUR LEDGER (Rule G)

Filled as forward-delivery evidence feeding the transition, per Rule G, and read separately
from the governance check that follows it.

| Item | Entry | Tier |
|---|---|---|
| What was built, from what base | Incorporated 1987, listed on BSE, 39th annual general meeting in September 2026. H-Acid capacity grown from 30 tonnes at inception in 1989 to 270 tonnes now, on the company's own growth chart, read as tonnes per month. One plant, Mahad, Raigad. Zero liquid discharge, 4-star air-pollution rating from the Maharashtra Pollution Control Board, ISO 9001:2015, a Dyestuffs Manufacturers Association merit certificate for export of dye intermediates by a large-scale unit. | FILED, AR FY26 pp. 5 to 8 |
| Built elsewhere by the same family | Shubhalakshmi Polyesters, sold to Reliance Industries for Rs 1,522 crore in March 2023, with affiliate Shubhlaxmi Polytex at Rs 70 crore. The family has built and exited a business roughly ten times the size of this listed company. | PRESS, March 2023, via B08 |
| Capital raised versus deployed | Zero-coupon compulsorily convertible debentures, 18,66,580 at Rs 79, Rs 14,74,59,820, entirely to promoter and promoter group, allotted 15-Mar-2025, 04-Dec-2025 and 03-Apr-2026. Stated objects and outcome at 31-Mar-2026: SDPL investment Rs 10.00 cr against Rs 9.99 cr utilised; working capital and debt repayment Rs 3.75 cr, utilisation disclosed a year after its own March 2025 timeline; general corporate Rs 1.00 cr against Rs 1.01 cr utilised. Warrants, 22,85,000 at Rs 176.10, Rs 40,23,88,500, approved 25-Aug-2026, 25% paid at subscription and about Rs 30.18 cr due within 18 months, across four objects to March 2031: Rs 10.24 cr expansion in existing and new units, Rs 10.00 cr SDPL, Rs 10.00 cr working capital and debt repayment, Rs 10.00 cr general corporate. A rights subscription of about Rs 5 crore into SDPL, 23-Mar-2026. A related-party loan of Rs 1,88,28,133 to SDPL during FY26, repaid before year end. | FILED, AR FY26 AGM Notice pp. 43 to 48, corporate governance report pp. 90 to 91, Notes 16 and 35.24; PRESS for the rights issue |
| What each rupee became | Consolidated capital work in progress of Rs 1,130.42 lakh at 31-Mar-2026, of which Rs 73.55 lakh already aged one to two years and none capitalised. About Rs 700 lakh of cash and deposits sitting undeployed at SDPL, which is what lifts the consolidated current ratio above the standalone. Solar, Rs 598 lakh of energy-conservation equipment. Working capital. | FILED, Notes 2(ii), 10, 11 |
| Contrarian decisions that worked | Zero liquid discharge with by-products sold to the cement industry, turning a disposal cost into Rs 225.82 lakh of revenue. Captive solar taken from 1.5 MW to 3.35 MW, decided and largely built before the 2026 energy and feedstock cost spike, in a business where power is roughly 11% of revenue. Environmental clearance for SDPL obtained during FY26, before the August 2026 price peak. | FILED, AR FY26 pp. 6 to 8, p. 63, Note 34 |
| Contrarian decisions, not found | No evidence of a deliberate export pivot. Exports went from nil to 46.4% of revenue in one year and management never explains it anywhere in 181 pages. NOT FOUND. | FILED, by absence |
| Skin in the game | Promoter holding 54.21% to 59.25% at 31-Mar-2026, 64.25% before the warrant issue, and a prospective 73.75% on full conversion. Zero pledge, independently corroborated. Both capital raises were promoter-family money going in, not out. | FILED, Note 35.1, corporate governance report p. 89 |
| Delivery under constraint | FY25 operating cash flow negative at Rs 147.99 lakh against profit after tax of Rs 512.40 lakh, with the current ratio below 1.0 in both years, and capex and the solar build still funded through it. | FILED, cash flow statement p. 107 |

**The ledger's weakest row, stated rather than smoothed.** The corporate governance report's
Regulation 32(7A) footnote says preferential-issue proceeds were used "towards other purposes
considered expedient", the adjacent line declares no deviation or variation, and Note 35.24
gives a third account. The single strongest row in this ledger, capital raised and deployed
to its stated objects, rests on a table the same report contradicts twice.

**Pillar 3 line, required by Rule G.** The Entrepreneur Ledger SUPPORTS a growth-visibility
premium on two rows only: the compliance and cost-position build, which is the one thing that
positions this company for a flip caused by a competitor's environmental failure; and the
scale of promoter capital committed at 25-Aug-2026, which is forward-delivery evidence rather
than history. It DOES NOT SUPPORT a premium on the delivery row: SDPL has produced nothing in
over two years, its construction in progress is ageing, and no capacity has ever been
disclosed. Stage 11 owns the Pillar 3 number. Two Rule G limits bind and are recorded here:
this ledger cannot lift any position cap the promoter verdict imposes, and single credit
means a ledger fact credited into Pillar 3 is not credited again in a strategic premium.

**Governance cluster, carried as named tripwires, not offset.** Part 2.6 as the operator
states it: the ledger and the concerns are both evidence and neither cancels the other
silently. Nothing above reduces anything below, and nothing below reduces anything above.

| Tripwire | Level now | Threshold that fires it |
|---|---|---|
| Promoter-family pay, relatives' salary and rent against standalone profit before tax | Rs 596.92 lakh, 112.7% of PBT, up from 84.9% in FY25 | A second consecutive year above 100% |
| Remuneration ceiling sought | Rs 6.60 crore a year, about 156% of FY26 profit, in the same report that skips the dividend to conserve cash | Any drawing against it while the current ratio stays below 1.0 |
| AOC-2 non-arm's-length contracts | 8 contracts, Rs 202.70 lakh, about 48% of profit, no section 188 general-meeting resolution | Any increase, or a repeat without the resolution |
| Related-party ceiling sought | Rs 100 crore combined against a market value of about Rs 156 crore, half of it for Shubhlaxmi Dyetex Private Limited: nil turnover, about Rs 1,163 crore net worth, no disclosed connection to H-Acid | Any actual drawdown. This is also the business falsifier |
| Family-only dilution | 54.21% to 59.25% to 64.25%, prospective 73.75%, at Rs 79 and Rs 176.10 against a market price of Rs 248 | Any further issuance to the family at a discount |
| Object-clause widening | Cranes, defence vehicles, infrastructure EPC and an investment business, in the same AGM notice that funds the H-Acid expansion | Any deployment of warrant proceeds outside dye intermediates |

The last tripwire is the one that touches the transition directly. The same meeting that
raises Rs 40.24 crore for chemical expansion also widens the objects far outside chemicals.
The capacity leg of the bull case is therefore not contractually protected.

---

## 5. COMPETITIVE ADVANTAGE, RE-READ IN THE FLIP

The Phase 1 moat read stands on trailing structure and remains correct as far as it goes:
17 of 60 on the moat scan, 5 of 12 tests confirmed, failing cost position, scale and brand
against Bodal Chemicals and Shree Pushkar Chemicals; the forward emerging-moat scan scored 8
of 92 with only captive solar reaching moderate strength; research and development spend
reported nil.

The forward question the flip raises is different, and it has two parts.

**Does China's exit change the demand position? Yes, and materially.** The largest global
supplier becoming a buyer converts the competitor into a customer. That is a genuine change
in the demand curve facing every Indian producer, and it is the single most consequential
fact found in this rebuild.

**Does it change SHHARICH's cost position against its Indian peers? No.** The rent falls on
every compliant Indian producer at once. Within India, SHHARICH remains the sub-scale one:
Bhageria alone runs 400 to 500 tonnes a month against SHHARICH's roughly 270, and Bodal is
larger again. Nothing in the flip gives SHHARICH an advantage over Bodal, Bhageria, Kiri or
Shree Pushkar. A sector rent is not a moat. Any moat claim must rest on something SHHARICH
holds that they do not, and the evidence does not show one.

**The one place a company-specific edge could sit.** If the flip's cause is Chinese
environmental enforcement, then compliance is the scarce asset, and a plant with zero liquid
discharge, a 4-star pollution rating and by-product recovery already built is holding the
thing that is scarce. That is a real argument. It is also an argument that applies to every
compliant Indian producer, and SHHARICH's compliance record is not shown to exceed theirs.
It protects participation in the rent. It does not create a share of it.

**Durability window, tiered.**

| Reading of the cause | Window | Tier |
|---|---|---|
| Permanent Chinese environmental curb, output down 50% to 60% | Multi-year, three years or more | AGGREGATOR. Weakest sourcing of the three, and the one that most needs a primary check |
| Feedstock shortage plus tighter output plus seasonal demand | Two to four quarters, unwinding as Chinese naphthalene and sulphuric acid supply normalises | PRESS and PEER CALL, Sept-2026 |
| VAT-rebate withdrawal on H-Acid | Would be structural, but NOT CONFIRMED at product level and demoted | Not established |

**The counter-force, already in flight and dated.** Indian supply is responding inside the
window. Bhageria added 100 tonnes a month, disclosed 08-Oct-2025 with a six-month build.
Shree Pushkar is commissioning 72,000 tonnes a year of chemical capacity and a 240,000 tonne
acid complex, stated on its Q1 FY27 call on 13-Aug-2026. SHHARICH's own SDPL is meant to add
more. Every tonne of Indian capacity that lands narrows the window from the India side even
if China never returns.

**Named window.** Two to six quarters at reasonable confidence, so through roughly FY28.
Beyond that the window depends entirely on whether the Chinese curb is permanent, which this
run cannot establish. **Confirm-by:** the Chinese H-Acid price against the roughly 100,000
yuan per tonne level of end-August 2026, read monthly. A sustained fall back toward 40,000
yuan per tonne closes the window, and it will show there before it shows in any Indian
company's results.

**The timing problem this creates, stated because it is the model's sharpest tension.** The
window is two to six quarters. SDPL has been building for over two years with no disclosed
commissioning date, and the warrant objects run to March 2031. The capacity that would let
this company convert the rent into tonnes may well arrive after the rent has gone. That is
not a reason to reject the transition. It is the specific thing the transition has to beat,
and no evidence in this run tells us whether it will.

---

## UNASKED

Three things not requested, ranked by how much they would change the transition read.

**1. The Halt 1 proof gate as currently written cannot falsify this model, and would confirm
it on the wrong evidence.** Highest impact, because it decides whether the signed model is
testable at all. Both the Phase 1 dossier and this rework brief name double-digit organic
manufactured revenue growth as the confirmer. On a plant already near full, in a window where
H-Acid realisation rose 40% to 45%, that threshold is cleared by price with zero volume. The
operator would sign a model whose confirming observation fires on the spread cycle it is
trying to exclude. Section 2.4 proposes the price-adjusted replacement. This should be
settled before signature, not after.

**2. The capacity finding inverts two Phase 1 conclusions and nobody asked it to.** Second,
because it changes what the evidence means rather than what we do next. If 270 tonnes is
monthly and the plant ran near full, then 4.8% organic growth is a ceiling and not a verdict,
and the resale line is a shortage symptom and not flattery. If instead the plant has real
idle capacity, the transition needs no capex at all, SDPL stops being load bearing, and the
whole model changes shape. One document settles it: the SEIAA environmental clearance, which
states product-wise capacity by statute. It is item 2 on the live-verify list and it is worth
more than the other six combined.

**3. The same meeting funds the expansion and unbinds it.** Third, because it is a
governance fact with a direct transition consequence that the governance section alone would
not surface. AGM Item 16 raises Rs 40.24 crore for dye intermediates. AGM Item 15, in the
same notice, widens the objects into cranes, defence vehicles, infrastructure EPC and an
investment business, and the family already runs private vehicles in infrastructure and
logistics. There is no disclosed restriction tying the warrant money to H-Acid. The bull case
assumes the capital builds chemical capacity; the constitutional documents, as amended, will
not require it to.

---

## SIGN-OFF BLOCK (operator completes)

- FROM rung to TO rung: R1 COMMODITY PRICE-TAKER to R2 COST-ADVANTAGED CONVERTER, manufactured H-Acid line.
- Engine: realisation captured from China's supply withdrawal, then tonnes from SDPL commissioning.
- Proof gate: manufactured H-Acid revenue growth against the H-Acid price-index change over the same window, first testable in the Q2 FY27 print around Nov-2026.
- Ugliness verdict: [operator]. This rebuild does not carry Phase 1's provisional STRUCTURAL-FEATURE forward unexamined. FY26's ugly optics are now substantially explained as a pre-flip baseline on a full plant, which argues ARTIFACT-OF-CLIMB. The ageing construction in progress at SDPL, with no capacity ever disclosed, argues STRUCTURAL-FEATURE. The evidence genuinely splits and the operator rules.
- Transition falsifier: section 3.5.
- Business falsifier: section 3.5.
- Transition posture: NOT ASSIGNED. Deferred to Stage 11, which resolves the recognition gap.
- Mental Model signed: NOT SIGNED.
