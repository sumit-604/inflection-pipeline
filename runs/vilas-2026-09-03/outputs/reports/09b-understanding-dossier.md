# STAGE 09b: HALT 1 UNDERSTANDING DOSSIER
Vilas Transcore Limited (VILAS) | Run: vilas-2026-09-03 | Model: claude-sonnet-5

Assembly only. Every claim below traces to a committed block or an anchored
quote in a stage report. No web search, no re-analysis, no valuation or
price vocabulary anywhere in this file except the one scoped exception
named in Section 2, Part B4.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

**1. Concalls.** Three transcripts held and used: May-2025 (FY25 full-year
results call), Nov-2025 (H1 FY26 results call), May-2026 (FY26 full-year
results call). (B00, B05) A fourth, Nov-2024 (H1 FY25), is listed as
available but was not supplied to this run (B00
`concalls_available_unused`). The most recent quarter covered is FY26
full year (year ended 31-Mar-2026, call held 12-May-2026). Given the run
date of 2026-09-03, Q1 FY27 (Apr-Jun 2026) results and its concall would
plausibly already exist under SME-platform filing timelines (45 days from
quarter end, so by roughly mid-August 2026) and are absent from this
corpus. This is a plausible gap, not a confirmed one; it is not one of
the four defined freshness pairs.

**2. Annual reports.** Two years held: FY24 (Annual_Report_2024.pdf,
filed 04-Sep-2024) and FY25 (SME_AR_28556_VILAS..., filed 05-Sep-2025).
(B00) The latest completed FY is FY26 (year ended 31-Mar-2026); its
Annual Report is NOT present in the corpus. At least 3 years of AR are
NOT held (only 2). FY23 figures are available only as FY24 AR
comparatives, not as a primary FY23 AR.

**3. Results filings.** Latest quarterly/annual filing: FY26 audited
annual results, filed 2026-05-11. (B00) A prior H1 FY26 results filing
(13-Nov-2025) is also held, though its PDF is image-only with no text
layer (B01). The quarter-gap: the latest results filing (FY26, May-2026)
sits a full financial year ahead of the latest Annual Report on file
(FY25, Sep-2025) - the FY26 AR itself is the missing document.

**4. Investor presentations.** Latest held: FY26 Investor Presentation,
dated 2026-05-11, aligned to the FY26 results filing date. (B00, B04)

**5. Research / rating.** One rating rationale held: ICRA full
rationale dated 2025-07-14 (rating action [ICRA]A-, outlook revised
Positive to Stable). (B00, B08) No rating action or broker note more
recent than 2025-07-14 is in corpus; over a year has elapsed to the run
date, which is a plausible (not confirmed) staleness point but is not
one of the four defined freshness pairs.

**6. Corporate actions.** One announcement held: GPCB Consolidated
Consent and Authorization (CCA) for the Unit-3 plant, dated 2026-05-01,
operator-ferried as a text summary (primary PDF absent). (B00, and
inputs/announcements/gpcb-cca-2026-05-01-operator-ferried.md) No AGM
outcome filings, no capital-raise filings, and no other primary
announcement PDFs are in corpus for the period Sep-2025 to Sep-2026.

**7. Freshness pair check.** Per B00 `freshness_pairs`: results-to-concall
PASSES (FY26 results 2026-05-11 paired with the FY26 concall
2026-05-12); rating-bulletin-to-rationale PASSES (ICRA 2025-07-14 paired
with the full rationale); referenced-SEBI-order-to-text PASSES (none
referenced). The fourth pair, AR-not-older-than-latest-audited-annual-
results, FAILS: the trigger document is the FY26 audited annual results
(filed 2026-05-11); the missing mate is the FY26 Annual Report, which is
not yet published. (B00 `freshness_verdict: CORPUS GAPPED-FRESHNESS`)

**8. Verdict line.**

**CORPUS GAPPED-FRESHNESS**

Missing mate: FY26 Annual Report (FY26 audited annual results filed
2026-05-11; the FY26 AR has not yet been published). This is a
findable-but-missing document; it will exist once the company files it,
expected source: BSE/NSE exchange filing or the company IR page.

Additional gaps carried under this umbrella (B00, B01):
- Prospectus/DRHP (IPO, May-2024): severity HIGH. Findable-but-missing,
  expected source: NSE Emerge SME platform archive or the company IR
  page. The FY24 AR confirms a DRHP was filed 31-Jan-2024 (FY24 AR Note
  1, p.46), so the document exists; it is simply not in this run's
  corpus. Its absence means FY20-FY22 restated financials and the
  pre-listing group/related-party map are not independently verifiable
  from a primary source.
- Announcements primary PDFs: severity MEDIUM. Findable-but-missing
  (BSE/NSE); only one operator-ferried text summary (GPCB CCA) is held.
- Shareholding pattern primary exchange filing: severity LOW.
  Findable-but-missing (BSE/NSE); only an aggregator (screener) table is
  held, with no pledge column.
- Contingent-liabilities note for FY26 and a peer set for several
  emerging-moat tests (M2, M5, M7, M9): both are data gaps rather than
  missing documents, carried forward from B01.

This verdict caps the phase-1 gate recommendation at PROCEED WITH
CAVEATS and is not softened to plain CORPUS GAPPED, per B00
`gate_cap: PROCEED WITH CAVEATS`.

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT - PENDING OPERATOR SIGN-OFF**

### PART A: THE FROM STATE

**A1. Archetype.** Commodity converter (CLAUDE.md Archetype Library;
Section 1B v3.7 Amendment 17 binds). One business line at the FROM
anchor: CRGO electrical-steel lamination/core processing, ~98% of FY25
revenue. (B04) The manifest sector tag "Pharma / CDMO" is a collector
error and is disregarded throughout (B00, B04).

**A2. The simple analogy.** Vilas Transcore buys imported CRGO
(cold-rolled grain-oriented) electrical steel, a specialised sheet steel
that carries current efficiently, and cuts, stacks and winds it into the
cores that sit inside power and distribution transformers. (B04) It does
not make transformers; it makes the metal heart that goes inside one.
Its customers are transformer manufacturers (named relationships include
Voltamp Transformers, Electrotherm India, Atlas Transformers, Shilchar
Technologies). (B04, FY24 AR Chairman's Message) The company buys a
commodity input at a world price it does not set, and sells a processed
component at a price its customers, not it, largely control. (B04
`pricing_power: price-taker`) It has just tripled its physical capacity
(12,000 to 36,000 MTPA) and is trying four new product lines on top of
that base: nanocrystalline cores, copper conductors, radiators, and a
minority stake in an HV bushings venture. (B04, B05, B07)

### PART B: THE TRANSITION

**B1. From tier to to tier.** One line, one transition. FROM: R2
COST-ADVANTAGED CONVERTER (mid-teens-to-20s ROCE, cost position from
processing scale among the few qualified Indian CRGO processors, and
OEM-qualification switching costs, per B04 `moats_present`; historical
ROCE 22.68% FY23, 22.03% FY24, 17.66% FY25, declining as new capital sits
idle pre-ramp, per B02/B03 Note 51). TO (claimed, not yet proven): R3
VALUE-ADDED / SPEC'D SUPPLIER, via diversification into nanocrystalline
cores, copper conductors (PICC/CTC), HV bushings, and radiators, each of
which carries its own customer-qualification cycle and, if it converts,
a different margin and stickiness profile than bulk CRGO lamination.
(B04, B05, B07) Per Amendment 17 and Amendment 18, the CRGO core sits in
the converter neighbourhood on its own; the new lines are separate,
unresolved optionality slices, not yet blended into a single proven
destination.

**B2. The engine.** Two things must physically change. First, Unit-3
must absorb its new fixed-cost base by running CRGO+nanocrystalline
volume up toward a level comparable to the ~90% utilisation the old
12,000 MTPA base achieved (B04 `must_track_metrics`; FY24 AR MD&A,
"operating at approximately 90% utilization"); it currently runs at
roughly 55% (B00). Second, the new product mix (nanocrystalline,
copper conductors, radiators, HV bushings) must convert from
management-narrated targets into invoiced, qualified, repeat revenue
that a customer cannot easily source elsewhere, which is what would
move the blended business off a pure-CRGO cost-position moat and onto a
spec'd-component moat. (B04, B07)

**B3. The proof gate.** The hard binary Stage 11 FTTCP tests: Unit-3
utilisation sustaining at or above a level comparable to the old base's
~90% for two consecutive quarters, cross-checked against gross margin
recovering to at least the ~20% band seen pre-ramp (FY26 sat at 17.82%,
B04 `first_deterioration_signals`), AND at least one new line (nano,
copper, or radiator) posting revenue at or above its own most recently
guided run-rate for two consecutive quarters. Until both legs fire
together, the transition is narrative, not confirmed. As of the FY26
concall, neither leg has fired: utilisation sits near 55% (B00) and
every rupee-denominated new-line target given since May-2025 has been
cut (nanocrystalline Rs 50 Cr to Rs 18-20 Cr; FY27 revenue Rs 1,000 Cr
to Rs 750-780 Cr base case). (B05)

**B4. The recognition gap (OPEN QUESTION, resolved at Stage 11).**
Whether the market has already priced in the TO-state climb to a
higher-quality, more diversified component supplier, before that climb
is proven, is an open question this dossier does not answer. Stage 11
resolves it via the destination-PE gap under Section 1B. If the TO state
already appears reflected, the re-rating engine this transition would
otherwise supply is already spent and only the underlying earnings
growth path remains available. No number, no fair-value conclusion, and
no entry-price judgment is stated here.

**B5. The ugliness test.** Today's dominant ugly optic is FY25's
negative operating cash flow (-Rs 35.46 Cr, against PAT growth of +48%)
and the accompanying working-capital build (inventory +283.7% in raw
materials, receivables +54.8%) and ROCE decline (22.03% to 17.66%).
Classification: **ARTIFACT-OF-CLIMB**, with evidence. B03's Phase 3 read
shows Operating Profit before Working Capital Changes actually rose
56.2% (Rs 33.92 Cr to Rs 52.97 Cr) in the same year; the negative OCF
traces to a 100%-raw-material-concentrated inventory build staged ahead
of Unit-3's commissioning, and to a receivables build that is 90%
non-related-party and 99.5% current by ageing, not to margin decay. (B03
Phase 3, 2E) The ROCE decline is consistent with a capital base (IPO
cash, CWIP) that has expanded ahead of the earnings it is meant to
generate during a pre-commissioning phase. (B03 3B) Separate from this
optic, a distinct pattern of governance and disclosure ugliness exists
(the Atlas Transformers related-party concentration, the SMT Packaging
advance disclosed at far lower depth, an unexplained ~110,000-share
reduction in the promoter's absolute holding despite a 100% fresh-issue
IPO, at least four arithmetic tie-failures across the FY25 AR, and a
CFO transition landing on the audit-report signing date). (B02, B03,
B08) This governance pattern sits outside the climb/decay binary the
ugliness test is built to classify; it is a live, unresolved risk
carried forward to the business falsifier (C3) below, not resolved by
calling the cash optic an artifact of the climb.

**B6. The transition falsifier.** Evidence that would kill the
transition thesis, kept separate from what would kill the business:
Unit-3 utilisation stalls materially below the old base's ~90% norm for
several quarters running (B04's own red-flag threshold), AND two or
more of the four new lines (nanocrystalline, copper, radiator, HV
bushings) fail to reach even their already-once-cut FY27 targets. That
combination would confirm the capacity add was simply "more of the same
commodity conversion at a bigger scale," with the value-mix shift never
actually arriving; the CRGO converter would stay at R2 rather than climb
toward R3.

### PART C: WHAT THE MODEL WATCHES

**C1. Dominant variables** (derived from B2/B3, become the Role 5.5
tracker signals):
1. Unit-3 utilisation and CRGO volume, tracking toward the FY27 guide of
   ~30,000 MT (B05 `triggers`). Current state: FY26 actual volume 19,500
   to 19,856 MT (B05 vs B00, discrepancy unresolved), against a 24,000 MT
   FY26 target that was missed. (B05)
2. Spread per kg (realised selling price minus landed CRGO/copper input
   cost), the converter's core lever under Amendment 17. Current state:
   FY26 sat at a cyclical trough, CRGO around Rs 195-210/kg versus
   Rs 270-290/kg in FY25/early FY26. (B04, B05, B06)
3. New-line revenue delivery against guidance (nanocrystalline, copper
   conductors, radiators, HV bushings). Current state: every rupee target
   given since May-2025 has been cut at least once; radiator commercial
   sales began ~9 months late (April 2026 vs guided July 2025). (B05)
4. Working-capital intensity (receivable, inventory and payable days)
   normalising as capex deploys. Current state: deteriorating through
   FY25 into FY26 (B01: WC days rose from roughly 41 in FY24 toward
   96.5 in FY26 on the corpus's own computed basis), the self-correcting
   (growth-induced) versus structural question B03 leaves open.

**C2. What the model rejects.** Aggregate India or global CRGO/transformer
TAM-size debates, and the "India as a global transformer export hub"
secular narrative, are declared noise for THIS model: B09's own funnel
shows demand headroom of roughly 11.4x the current SAM share and a
STRONG runway class, so market size is not the binding constraint. The
binding constraint is execution: whether Unit-3's utilisation ramps and
whether the new lines actually convert management narrative into
qualified, repeat revenue. (B09) Similarly, unresolved single-customer
concentration speculation (the ICRA-cited 40-55% figure, unconfirmed
anywhere in the AR) is not itself a transition-model variable; it
belongs to the business falsifier below, not to the climb-or-not
question this model tracks.

**C3. The business falsifier** (distinct from B6; kills the FROM
business itself, not just the climb): Either of two evidenced paths
would force a re-declaration. First, a sustained (multi-quarter) CRGO
price collapse below the cost curve that even Unit-3's added scale
cannot offset, given 100% import dependence for CRGO steel and zero
forward-contract hedging in place despite a written hedging policy
(B02, B03 Notes 35-36) - this would mean the FROM-state cost-position
moat itself is not durable. Second, the governance/disclosure pattern
named in B5 (unexplained promoter shareholding reduction, the Atlas
Transformers bidirectional related-party concentration at 12.5% of
FY25 revenue with its Rs 65 Cr ceiling already 34% consumed within 5
months of FY26, the undisclosed-terms SMT Packaging land advance, and
the AR's recurring arithmetic tie-failures) escalating into a confirmed
finding of related-party value extraction, which would mean the
operating shell is not run primarily for minority shareholders. (B02,
B03, B08) Either path re-opens the question of what business is
actually being valued, separate from whether its transition succeeds.

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

Vilas Transcore processes cold-rolled grain-oriented (CRGO) electrical
steel into laminations, cores, coils and toroidal cores, the components
that sit inside power, distribution and current transformers across all
voltage classes; a transformer cannot be built without a core, and CRGO's
grain orientation is what keeps energy losses in that core low, so the
product is not substitutable with ordinary steel. (B04) This CRGO line
is roughly 98% of FY25 revenue; four smaller, newer lines sit alongside
it: nanocrystalline cores (0.8% of revenue, a higher-value-add
conversion product still ramping), radiators (just commenced, 0%),
copper conductors (pre-commercial, 0%), and a shrinking legacy job-work
line (0.2%). (B04) The customers are transformer and power-equipment
manufacturers, named relationships including Voltamp Transformers,
Electrotherm India, Atlas Transformers India, and Shilchar Technologies
Limited; these are qualification-driven buyers, meaning a supplier must
pass a technical approval process before a manufacturer will source from
it, which creates switching costs once a supplier is qualified. (B04)
One of these named customers, Atlas Transformers, is majority-owned by
VILAS's own Managing Director and trades on both the sales and purchase
side of VILAS's book, a governance detail material to understanding who
the company's largest counterparty actually is. (B02, B03, B08) Demand
exists today because India's power transmission and distribution
network is expanding: renewable capacity additions (solar and wind) each
require step-up and evacuation transformers, and India's national CRGO
lamination processing market is sized in the corpus at roughly Rs 9,000
to 10,500 Cr, of which VILAS holds an estimated 8.8% current share.
(B09) The B09 Section 6 downstream candidates most tied to this present
demand are PGCIL vendor-approval status (institutional/higher-kV order
access), CEA National Electricity Plan transmission capacity-addition
data, and renewable capacity-addition bulletins from MNRE. (B09) Demand
should grow because B09's bottom-up funnel implies a company-level
blended revenue CAGR of roughly 26% (3-year) and 24% (5-year) once the
haircut-adjusted new-line contributions are added to the CRGO-only base,
though the CRGO-only implied CAGR alone (23% 3-year, 21% 5-year) sits
just under a 25% threshold, meaning the new-line optionality is
load-bearing to the growth case rather than pure upside. (B09) A second
named forward driver is a possible government anti-dumping or safeguard
duty on imported CRGO, which VILAS's own management cites but which the
supplied peer, Jay Bee Laminations, explicitly denies exists ("So there
is no safeguard duty on CRGO", JAYBEE May-2025 call); this driver is
contested, not confirmed, in the corpus. (B05, B06) On competitive
advantage: the CRGO line carries a moderate, evidenced moat from
processing scale among the few qualified Indian CRGO processors and
from OEM switching costs built on customer qualification history (B04,
B07 category C1); the Emerging Moat scan overall returned a score of 11
against a 25-point qualifier threshold, classification NONE, because
almost every forward claim supporting the newer lines is
concall-narrated guidance with a demonstrated 2-to-9-month slippage
pattern, not yet documented, audited fact. (B07) The four newer lines
(nanocrystalline, copper conductors, radiators, HV bushings) carry no
established moat in this corpus; each remains a management claim about
a future customer relationship, not a demonstrated one, and this is
said plainly rather than assumed.

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. Verticals framed (one per dominant variable, from Section 2 C1)

**Vertical 1: Unit-3 utilisation / CRGO volume ramp.** The corpus
establishes the capacity add is physically real and commissioned
on-schedule (Unit-3 commissioned 25-Jul-2025, per Board's Report; old
Units 1+2 ran above nameplate in FY25, 12,069 MT vs 12,000 MTPA). (B03,
B04) It cannot establish current-quarter utilisation independently of
management's own stated figures, since no FY26 AR or independent
production audit exists in corpus. Questions that decide it: (1) is the
19,500 MT (concall) vs 19,856 MT (operator anchor) FY26 volume
discrepancy resolved, and by what source; (2) does quarterly utilisation
data (if disclosed) show a monotonic climb toward the ~90% norm or a
plateau; (3) does the FY27 30,000 MT guide survive a further quarter
without another cut.

**Vertical 2: Spread per kg (CRGO/copper input cost vs realised
price).** The corpus establishes a directional price collapse (CRGO
roughly Rs 270-290/kg to Rs 195-210/kg through FY26, partial recovery in
April-2026) corroborated independently by peer Jay Bee Laminations. (B04,
B05, B06) It cannot establish an audited, company-disclosed per-kg
realisation series (no product-level segment note exists; AS-17 reports
a single business segment). Questions that decide it: (1) does the
company or a filed disclosure ever publish a per-kg realisation figure;
(2) does the disputed anti-dumping-duty and NLMK-price-holding claim get
independently confirmed or stays contradicted by peers; (3) does the
gross margin recover toward the pre-ramp ~20% band as CRGO stabilises.

**Vertical 3: New-line revenue delivery (nanocrystalline, copper,
radiator, HV bushings).** The corpus establishes a clear, repeated
pattern of guidance cuts and timeline slips across all four lines within
a single year of concalls (B05 `promise_delivery`: 9 missed, 2 partial,
3 delivered). It cannot establish independent verification of any new
line's customer base, margin, or true install capacity (the copper
Phase-1 capacity figure is internally inconsistent within a single
call, 1,500-1,800 MTPA vs 3,600 MT). (B04, B05) Questions that decide
it: (1) does any new line post two consecutive quarters at or above its
most recent guide; (2) is the HV Bushings JV's related-party structure
(25% VILAS / 75% promoter, using VILAS's own customer base and a rented
group building, per B12b) resolved or does it deepen as a governance
concern; (3) does PGCIL approval, silent since Nov-2025, ever resurface.

**Vertical 4: Working-capital intensity normalisation.** The corpus
establishes FY23-FY25 point-in-time deterioration on a consistent basis
(receivable days 54.7 to 45.9 to 62.3; inventory days derivable at 86.7
to 40.6 to 91.8; see Section 6 Q4 for the full computation and its
divergence from the operator's spear-held FY20-FY23 series). It cannot
establish the FY26 closing position independently of the audited results
sidecar and screener data (no FY26 AR notes exist to cross-check).
Questions that decide it: (1) does the corpus FY23 baseline (computed at
roughly 85 combined days) reconcile with the operator's separately-held
spear figures for the same period; (2) does OCF turn positive in FY26 or
FY27 as Unit-3 stabilises; (3) does short-term borrowing growth
(Rs 11.4 Cr FY25 to Rs 39.0 Cr FY26, per B04) outpace or track revenue
growth going forward.

### 4b. Candidate signal table (from B09 Section 6, expanded; UNVERIFIED,
verification happens at Role 5.5 in claude.ai)

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| PGCIL vendor-approval status | Approval remains "in process" past another 2 quarters with zero update | Event-driven | Power Grid Corporation of India vendor-empanelment notices; VILAS exchange filings |
| CEA National Electricity Plan (transmission) capacity-addition data | Transmission capacity-addition pace decelerates below the FY24 base rate (14,203 Ckms added) | Quarterly | Central Electricity Authority publications |
| DGTR CRGO anti-dumping investigation outcome | Investigation closes with no duty imposed, or is withdrawn | Event-driven | Directorate General of Trade Remedies notifications; Gazette of India |
| Atlas Transformers India Ltd related-party transaction volume | FY26 combined Atlas RPT run-rate breaches the Rs 65 Cr AGM ceiling before FY26 AGM | Quarterly | RPT disclosures; AGM resolutions (exchange filings) |
| Marquee OEM customer order books (Voltamp, Electrotherm, ECE Industries, Shilchar, Kirloskar Electric) | Two or more named customers report declining order books for two consecutive quarters | Quarterly | Individual company exchange filings / investor presentations |
| JSW JFE Electrical Steel Nashik domestic CRGO mill capacity status | Domestic CRGO mill capacity comes online at scale, ending VILAS's 100%-import dependence narrative | Event-driven | JSW Group exchange filings; DGTR petitioner disclosures |
| Renewable capacity addition bulletins (solar/wind GW added) | Monthly renewable capacity additions fall below trailing-12-month average for two consecutive months | Monthly | Ministry of New and Renewable Energy / CEA monthly bulletins |

### 4c. Fragility read

- **variable_count:** 7 (Unit-3 utilisation ramp; CRGO/copper spread and
  price recovery; new-line revenue delivery across four lines; PGCIL
  approval; anti-dumping/import-duty outcome; working-capital
  normalisation; RPT/governance containment.)
- **verifiability_ratio:** 5 of 7 externally observable (CRGO/copper
  market price, PGCIL approval status via a government notification,
  the anti-dumping duty outcome via DGTR/Gazette, working-capital
  metrics via audited filings, and RPT/AGM filings); 2 of 7
  company-narrated only (Unit-3 utilisation rate specifically, and
  new-line revenue run-rates specifically, both currently sourced only
  to concall and investor-presentation claims).
- **single_point_failure:** A sustained, multi-quarter CRGO price and
  spread collapse, given 100% import dependence for CRGO steel and zero
  forward-contract hedging despite a written hedging policy (B02, B03
  Notes 35-36), is the one variable most capable of doing outsized
  damage alone, since it hits the core CRGO business regardless of
  new-line progress. On a strict reading the framework still requires
  conjunction with continued capacity underuse to fully break the
  thesis, so the formal answer is: none - failure requires conjunction,
  with the CRGO price/spread variable flagged as the dominant single
  risk within that conjunction.
- **fragility_verdict:** FRAGILE. Seven variables must move together for
  the transition case to hold, two of the most execution-critical
  (utilisation, new-line delivery) are company-narrated only, and the
  concall record shows a demonstrated pattern of guidance cuts and
  slippage across nearly every rupee-denominated forward claim made
  since May-2025. (B05 credibility grade C)

### 4d. Research brief (live-web work the corpus cannot do; the claude.ai
work order)

1. Verify the FY26 CRGO volume discrepancy (19,500 MT per concall vs
   19,856 MT per operator anchor) against any exchange filing or
   investor-relations clarification.
2. Pull the ICRA rating rationale's underlying basis for the cited
   40-55% single-customer concentration figure; it is not sourced in
   the corpus (B02, B03).
3. Independently verify or refute the anti-dumping-duty and
   NLMK-price-holding claims against additional CRGO-tier peers beyond
   Jay Bee Laminations (Kryfs Power Components, Amod Stampings,
   Vardhaman Stampings), since the current contradiction rests on a
   single peer source. (B06)
4. Check PGCIL's own vendor-empanelment or approval-cycle disclosures
   for any CRGO/lamination peer, to benchmark VILAS's now-silent
   approval timeline against an industry norm. (B05, B06)
5. Pull primary BSE/NSE shareholding-pattern (SHP) and SAST filings for
   Nilesh Patel, to resolve the ~78,000-share unexplained reduction in
   his absolute holding despite a 100% fresh-issue IPO. (B03, B08)
6. Pull MCA/Zaubacorp director-history records for Tushar Somabhai
   Patel and Tushar Transequipment Pvt Ltd to confirm or refute the
   suspected link to the new 0.13% promoter-group shareholder "Tushar
   Patel". (B02, B03, B08)
7. Check DGTR's June-2026 anti-dumping filing (referenced in B09's
   stale-data flag) for its current procedural status and expected
   ruling date.
8. Verify whether a FY26 AR filing date has been announced by the
   company or exchange, to close the corpus's freshness gap.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. Vilas Transcore makes CRGO electrical-steel cores, the metal heart
   inside power and distribution transformers. (B04)
2. It does not make transformers. It supplies the component that goes
   inside one, to transformer manufacturers. (B04)
3. It has just tripled its main plant's capacity, from 12,000 to 36,000
   tonnes a year, and started four new, smaller product lines on top of
   that. (B04, B07)
4. Its customers are transformer makers such as Voltamp, Electrotherm
   and Shilchar, plus Atlas Transformers, a company owned by VILAS's own
   Managing Director. (B04, B02)
5. Buyers must qualify a supplier technically before they will buy from
   it, which makes it hard for a qualified supplier to be dropped
   quickly, but also hard for a new line to be added quickly. (B04)
6. Demand exists today because India keeps building and upgrading its
   power grid, and every new transformer needs a core. (B09)
7. A large and growing share of that demand comes from renewable power
   projects (solar and wind), which each need step-up transformers. (B09)
8. The market VILAS sells into is large enough for it to keep growing
   for years without running out of room; market size is not the
   company's binding limit right now. (B09)
9. Its main product line has a moderate, real advantage: few Indian
   processors are qualified to do this work, and switching suppliers is
   costly for a customer. (B04, B07)
10. Its four newer product lines have no proven advantage yet. Every
    one of them is still a company claim, not a demonstrated customer
    relationship. (B07)
11. The mental model here is a climb: from a plain commodity-steel
    processor toward a maker of higher-value, harder-to-copy components,
    but that climb is not yet proven in the numbers. (Section 2)
12. This company's forward story depends on several things going right
    at once, not just one, and two of the most important ones (how full
    the new plant is running, and whether the new product lines actually
    sell) can only be checked by trusting what management says, not by
    an independent filing. That combination is fragile. (Section 4c)
13. The corpus could not establish a per-product price the company
    charges (no segment breakdown exists), so any per-kilogram figure
    used elsewhere is a blend across all products, not a clean number
    for CRGO alone. (Section 6)
14. The corpus also could not establish who VILAS's single biggest
    customer is or how much of its revenue that customer represents; a
    rating agency has cited a 40-55% concentration figure that nowhere
    appears in the audited filings. (B02, B03)
15. The two biggest open questions are: why did the sole promoter's
    share count fall by roughly 78,000 shares with no explanation given
    a 100%-fresh-issue IPO, and will the company's new-plant volume and
    new product lines actually deliver on guidance that has already been
    cut once, or repeatedly, across every quarter checked. (B03, B08, B05)

---

## SECTION 6: STANDING EXTRACTION ANNEX

The ten Standing Extraction Annex questions were answered off-session on
2026-09-03 per operator ruling and are not re-run this pass. The ten
topics, for traceability: (1) units/per-unit realisation, (2) segment
capital and debt, (3) guidance versus aspiration, (4) concentration, (5)
promise ledger, (6) restated bases, (7) corporate-action clauses, (8)
related-party perimeter, (9) pledge and shareholding, (10) verification/
commit hash. Flagging for re-verification, from this run's own evidence:
B06 shows the supplied peer (Jay Bee Laminations) directly CONTRADICTS
VILAS's anti-dumping-duty claim and its NLMK-held-firm claim; and B04/B05
show the copper-conductor Phase-1 capacity figure conflicts within a
single concall, 1,500-1,800 MTPA (opening remarks) versus 3,600 MTPA
(Q&A). Both are named as re-verify candidates in the operator's hands,
not re-run here.

In place of the ten, the operator's five priority extractions are
answered below in full, corpus only, quote-then-comment, filename and
page anchor on every number.

### Priority 1: FY24/FY25 segment/product revenue and CRGO tonnage, to
build a per-kg realisation series FY23-FY25

Quote (FY25 AR, Note 40, cited at B02/B03 triple-pass item 6): the
company "discloses one business segment only; no customer-level revenue
breakdown anywhere in Notes 1-53." Quote (FY24 AR, Note 45, p.65,
"Segment Reporting"): "the business of production of Lamination and its
related products belong to one business segment only" (AS-17 basis).

Comment: a product-level revenue split is NOT DISCLOSED in the FY25 AR;
both years report a single AS-17 segment. The FY24 AR does carry one
product-level split, under "Sales (Finished Goods) Principal Items"
(FY24 AR, Notes forming part of the Financial Statements, p.60): "CRGO
Laminations 26,234.11 [lakh] / Others 4,739.95 [lakh] / Total 30,974.06
[lakh]" for FY24, against "23,345.35 / 4,915.16 / 28,260.51" for FY23.
It is unconfirmed whether the FY25 AR carries an equivalent note; B02/B03
did not extract one, and it is not cited anywhere in either report.

What tonnage and revenue the corpus does carry, quote-then-comment:

- FY24 AR, Annexure-IV MD&A, "Discussion on Financial Performance" (p.33
  of the AR): "Revenue for FY24 stands at Rs 313 Crore with a robust
  growth of 10% Y-o-Y. Total volume stood at 10,927 MT, grew by 16%
  Y-o-Y." Comment: this gives FY24 total production volume, 10,927 MT,
  directly printed. FY23 volume is not printed directly; it is
  derivable from the stated 16% growth rate as approximately 9,420 MT
  (10,927 / 1.16), a derived figure, not a printed one.
- FY24 AR, Statement of Profit and Loss (p.44): Revenue from Operations
  FY24 Rs 30,974.06 lakh (Rs 309.74 Cr); FY23 Rs 28,260.51 lakh (Rs
  282.61 Cr).
- FY25 AR, per B05 (Board's Report cited via 05-concall.md): FY25
  production 12,069 MT against a 12,000 MTPA nameplate ("Old-plant FY25
  actual production vs nameplate: 12,069 MT vs 12,000 MTPA"). FY25
  revenue from operations Rs 353.05 Cr (Note 23, per B02/B03).
- FY26 per the operator's anchors (B00): 19,856 MT / Rs 460.67 Cr
  revenue. B05 (concall) states management's own figure as 19,500 MT for
  the same year, an unresolved discrepancy already flagged (input_gaps,
  B05).

Derived (not printed), blended revenue-per-kg across all product lines,
using total revenue / total production volume: FY23 approximately Rs
300/kg (28,260.51 lakh / 9,420,700 kg, using the derived FY23 volume);
FY24 approximately Rs 283.5/kg (30,974.06 lakh / 10,927,000 kg); FY25
approximately Rs 292.5/kg (35,305.12 lakh / 12,069,000 kg, using the FY25
revenue figure per B02/B03 Note 23); FY26 approximately Rs 232/kg
(46,067 lakh / 19,856,000 kg, matching B04's own derived figure). This
series blends CRGO with the small non-CRGO lines each year and is not a
clean CRGO-only per-kg price; no cleaner figure exists in the corpus.

### Priority 2: Single-customer concentration (ICRA cites one customer
40-55% for four years)

Quote (FY25 AR Note 40, p.73, per B02 top_findings rank 7 and B03
triple-pass item 6): confirmed as NOT FOUND. No filing in the corpus
names or quantifies a single-customer share. Quote (FY24 AR, Annexure-IV
MD&A "Opportunities and Challenges" and Chairman's Message, p.30-32):
customer names are given qualitatively (Voltamp, Electrotherm, Shilchar,
Atlas) with no percentage attached to any one of them.

Comment: NOT DISCLOSED, confirmed across both Annual Reports in corpus.
The ICRA-cited 40-55% figure over four years cannot be verified or
sourced from any filing held in this corpus; the ICRA rating rationale
itself (B00, dated 2025-07-14, held in corpus) is the presumed origin of
this figure per the operator brief, but this dossier did not re-open
that rationale document during this pass since B02/B03 already confirm
the AR side is silent.

### Priority 3: Atlas Transformers full transaction history FY23-FY25,
both directions, plus the FY25 AGM resolution text on the Rs 65 Cr RPT
limit

Quote (FY24 AR, Annexure-II, Form AOC-2, p.26): "Atlas Transformers
India Ltd | Enterprise over which Key Managerial Person have significant
Influence | Sales Rs 22,56,38,800/- | Purchase Rs 8,66,50,856/-" (this
AOC-2 covers the FY2023-24 year, i.e. FY24 figures: sales Rs 22.56 Cr,
purchase Rs 8.665 Cr, matching the operator's stated FY24 figures).

Quote (FY25 AR, Note 41/AOC-2, per B03 section 2B): "Atlas Transformers
India Ltd (98.70% Nilesh Patel-owned) | Sales 1,916.55 [lakh] + Purchase
2,505.14 [lakh]" for FY25 (Rs 19.17 Cr sales / Rs 25.05 Cr purchase,
matching the operator's stated FY25 figures).

FY23 (Atlas-specific): NOT DISCLOSED as an itemised figure anywhere in
the corpus. Quote (FY24 AR, Notes Forming Part of the Financial
Statements, Note 46 "Related Party Transactions", p.66): "Enterprises
over which Key Managerial Person have significant Influence | Sales &
Job Work | 2,334.64 [FY24] | 1,581.97 [FY23] ... Raw Material Purchases |
880.43 [FY24] | 1,213.67 [FY23]". Comment: this is an AGGREGATE across
six related enterprises (Atlas Transformers, Tashu Impex, Pelton Power,
Nanocryst Transformer, SMT Packaging, Atlas Composites), not broken out
per entity for FY23; only the FY24 year gets a per-entity AOC-2 split.
Atlas Transformers' own FY23 sales and purchase figures are therefore
NOT DISCLOSED in this corpus; only the FY23 combined RPT total (Rs 15.82
Cr sales, Rs 12.14 Cr purchases across all six enterprises) is printed.

Quote, the FY25 AGM Notice's Rs 65 Cr resolution text (FY25 AR, Notice
Item 5 explanatory statement, p.13-15, as extracted at B02
pass1 line 37-39): "...shall not exceed Rs 65 crores for a period
commencing from the 19th Annual General Meeting up to the date of the
20th Annual General Meeting...(12 months)." with the split disclosed as
"Sale up to Rs 25 Cr, Purchase up to Rs 40 Cr" (p.13). Comment: this
ceiling governs FY26 (post-19th-AGM), not the FY25 actuals reported
above; year-to-date consumption at the point the FY25 AR was filed (28-
Aug-2025) already stood at Rs 22.35 Cr, roughly 34% of the ceiling
consumed in the first five months of FY26 (Notice p.13).

### Priority 4: WC / inventory / receivable days FY23-FY25 from corpus;
confirm or overturn the spear STRUCTURAL ruling

FY20-FY22 figures are NOT IN CORPUS; the operator holds separate spear-
tier figures for FY20-FY23 (116/108/78/70 days, per the operator's own
memory, not independently verified here). Only the FY23-FY25 leg is
built from corpus documents here.

Quote/derive (FY24 AR, Balance Sheet p.43 and Statement of Profit and
Loss p.44, figures in Rs lakh): FY23 closing Trade Receivables 4,238.54;
Inventories 5,329.12 (Raw Materials 1,502.05 + WIP 3,552.10 + Finished
Goods 274.97, Note 18 equivalent p.54); Trade Payables 3,447.44; Revenue
from Operations 28,260.51; Cost of Materials Consumed 22,426.21.

Derived (point-in-time, same method B02/B03 already use for FY24/FY25:
receivable days on revenue, inventory and payable days on cost of
materials consumed, x365): FY23 receivable days = 4,238.54 / 28,260.51 x
365 = 54.7 days; FY23 inventory days = 5,329.12 / 22,426.21 x 365 = 86.7
days; FY23 payable days = 3,447.44 / 22,426.21 x 365 = 56.1 days;
combined (receivable + inventory - payable) = 85.3 days.

Quote (B02, `receivables_trend`, and B03 2D/2E, both anchored to FY25 AR
Notes 18/19, p.64-65): FY24 receivable days 45.9, inventory days 40.6;
FY25 receivable days 62.3, inventory days 91.8-91.9. Quote (B01
`block_b_trend`): "WC days rose 41.4 to 96.5 FY24-FY26 (computed)" using
the 3-component formula on the audited FY24-FY26 balance-sheet basis.

Comment on the STRUCTURAL question: the corpus's own FY23 combined WC
figure (approximately 85 days, computed above) does not obviously
match the operator's separately-held spear FY23 figure of 70 days; the
two use different components or a different basis that is not
reconcilable from what is in this corpus alone (the spear figures
predate this corpus's earliest primary document, the FY24 AR, and their
exact formula is not stated in this run's inputs). What the corpus
CAN confirm: WC intensity did NOT sit at a structurally low, stable
level immediately before the Unit-3 ramp; FY23's own combined-days
figure (~85, computed) is closer to the elevated end of the FY23-FY26
range than to a clean low base. This complicates, rather than cleanly
confirms or overturns, a STRUCTURAL ruling: the ramp-period
deterioration (FY24's ~41 days to FY26's ~96.5 days, per B01) is real
and sits on top of an already-not-low FY23 starting point, so the
"growth-induced from a clean base" reading in B03 needs the FY23
baseline reconciled with the operator's spear-tier figures before Stage
11 treats this as a settled artifact-of-climb read. This reconciliation
is named as a re-verify candidate for the operator, not resolved here.

### Priority 5: Capex schedule, what was spent, on what, and CWIP
remaining

Quote (FY25 AR, Note 13, p.60-62, per B02 pass1 line 201-204): "Capital
work-in-progress: Rs 37.67 Cr (3,766.55L) FY25, from Nil FY24 - entirely
Unit-3 (all 'less than 1 [year]' ageing)." Quote (FY25 AR, Note 31, p.70,
per B02/B03): "Commitments: Rs 2,894.78 lakh (Rs 28.95 Cr) capital
commitments FY25 vs zero FY24," a first-appearance item entirely
attributable to Unit-3.

Quote (Concall_May_2026_Transcript, per 05-concall.md line 57): "FY26
total capex: Rs 60 crore; FY27 planned capex: Rs 30-40 crore (May-2026
call)." Quote (05-concall.md line 56, cross-calls): "Total capex on new
plant: Rs 90 crore planned (May-2025 call); Rs 80 crore invested + Rs
12-13 crore pending (Nov-2025 call) - broadly consistent, small
overrun."

Comment: the corpus shows a consistent, growing capex commitment across
three concalls (Rs 90 Cr planned, tracking to roughly Rs 92-93 Cr
actual for the Unit-3/radiator build through FY25-FY26) plus a
separately-guided FY26 total capex of Rs 60 Cr and an FY27 plan of Rs
30-40 Cr, which appears to extend beyond the original Unit-3 scope into
the copper-conductor Phase-1 build (Rs 25-30 Cr per the Nov-2025 call).
CWIP of Rs 37.67 Cr sat on the FY25-end balance sheet, entirely
attributable to Unit-3 and aged under one year, consistent with an
in-progress, not abandoned, capex programme. No FY26 AR exists in
corpus to confirm the FY26-end CWIP balance or actual-vs-guided FY26
capex spend; this is a genuine forward gap, not a resolved figure.

### Verification

Documents quoted in this annex: FY24 AR (Annual_Report_2024.pdf, filed
04-Sep-2024); FY25 AR (SME_AR_28556_VILAS_2024_2025_A_4244305_
05092025152635.pdf, filed 05-Sep-2025); Concall_May_2026_Transcript.pdf
(cited via 05-concall.md); B00-inputs.yaml, B01-gate0.yaml, B02-notes
reports (02-notes.md, 02-notes-pass1.md), B03-ardeep.md, B04-bizmodel.yaml,
B05-concall.md, B06-peers.yaml, B08-promoter.yaml, B09-tam.yaml.

Corpus commit hash: 280e2d81a2c8668f6707b6d2b04a3353dc87ef3d
