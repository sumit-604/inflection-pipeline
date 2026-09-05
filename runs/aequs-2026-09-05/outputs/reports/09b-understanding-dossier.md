# HALT 1 UNDERSTANDING DOSSIER — Aequs Ltd (AEQUS)

Run: runs/aequs-2026-09-05. Phase 1 (evidence). Assembled from committed
blocks B00-B09, verifier blocks B12a/B12b/B12c/B12d, the confidence delta,
and the phase-1 final files. No new research. No valuation, no price, no
verdict-set language. The Mental Model Declaration below is a DRAFT for
operator sign-off in claude.ai; nothing in this file marks it signed.

A note on this run's own reliability before the reading starts: the
phase-1 verifier layer found that the concall-analysis stage (Stage 5,
block B05) caught only 9 of 30 independently identified findings in the
same three transcripts it read, missing one finding graded at the header
severity scale's top tier and seventeen at the next tier down (B12b;
confidence.yaml). Every fact in this dossier that traces to B05 or to the
peer stage (B06) is presented with that context. Where a verifier
corrected, overstated-flagged, or added to a claim, this dossier carries
the correction alongside the original, not in place of it.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

**1. CONCALLS.** Three transcripts held: Concall_Feb_2026_Transcript.pdf
(Q3 FY26, filed 04-Feb-2026), Concall_Jun_2026_Transcript.pdf (Q4 FY26 /
FY26 annual, held 26-May-2026, filed 02-Jun-2026), Concall_Aug_2026_
Transcript.pdf (Q1 FY27, held 29-Jul-2026) (B00 concall_map). The most
recent quarter covered is Q1 FY27 (quarter ended 30-Jun-2026). Q2 FY27
(quarter ending 30-Sep-2026) has not yet closed as of the 2026-09-05 run
date, so no more recent transcript is plausibly missing.

**2. ANNUAL REPORTS.** One year held: Annual_Report_2026.pdf, FY2025-26
(year ended 31-Mar-2026), 361 pages, filed with the AGM notice dated 2026
(B00; B03). This is the latest completed FY (FY2026-27 will not close
until 31-Mar-2027). Fewer than 3 years are held: FY24 and FY25 Annual
Reports are ABSENT (B01 input_gaps "prior-year ARs"). This caps every
multi-year ratio series (ROCE, working-capital days, capex/FCF) to the two
years the single AR's own comparative balance sheet carries, FY25-FY26,
not the full FY23-FY26 window (B01 data_notes).

**3. RESULTS FILINGS.** ABSENT entirely. No quarterly or annual results
filing sits in the corpus for any period (B00 input_gaps "results"). Every
Q1 FY27 number in this dossier traces only to the investor presentation
or the Aug-2026 concall transcript, never to a filed results document
(B00 analyst_note; final/business-narrative.md). Quarter-gap: the Q1 FY27
results (period ended 30-Jun-2026, reported ~29-Jul-2026) are absent as a
filed document even though the concall and presentation covering the same
quarter are present.

**4. INVESTOR PRESENTATIONS.** One held: Investor_Presentation_1.pdf, Q1
FY27, 30 pages (task inputs; B00).

**5. RESEARCH / RATING.** No standalone research or broker note is held
(B00 input_gaps "research"; ".gitkeep planted"). No standalone rating
document is held either, but the fact of a rating is disclosed inside the
AR's Corporate Governance Report: "the credit ratings obtained by the
company during the financial year 2025-26 for Bank Facilities are as
follows... Aequs Limited Long-term Bank Facilities 25.00 CARE BBB-;Stable
Reaffirmed" (AR p.113; B03 input_gaps). No rating rationale text
accompanies this line.

**6. CORPORATE ACTIONS.** The announcements folder is EMPTY (B00 input_gaps
"announcements"). No Reg 30 filing exists in corpus for the Safran A320
wheel agreement, the CFO resignation, the Scheme of Amalgamation board
approval (23-Apr-2026, disclosed only as an AR subsequent event, Note 41
AR p.302), the FY27 capex reallocation, or any capital raise. No date
range applies; the folder carries zero documents.

**7. FRESHNESS PAIR CHECK.** B00's `freshness_verdict` reads FRESHNESS
PAIRS OK. All four pairs PASS (B00 freshness_pairs):
- results_to_concall: PASS. No results filing exists in corpus to trigger
  the pair (results absence is an input gap, not a failed pair).
- rating_bulletin_to_rationale: PASS. No rating bulletin document exists
  in corpus to trigger the pair.
- sebi_order_to_text: PASS. No SEBI order is referenced anywhere in the
  FY26 AR.
- ar_to_latest_audited_annual: PASS. Trigger document
  annual-report/Annual_Report_2026.pdf (FY2025-26) matches the latest
  audited annual year; no missing mate.

No freshness pair failed. This run's gaps are document-absence gaps, not
freshness-pair failures.

**8. VERDICT LINE.**

CORPUS GAPPED: prospectus / RHP (ABSENT; findable-missing, expected source
BSE/SEBI filing page or the company IR page; HIGH-severity gap per B00,
since the company listed 10-Dec-2025 inside the ~3-year window and the RHP
carries the promoter/group history and restated pre-IPO financials this
run could not otherwise construct); results filings for all periods
(ABSENT; findable-missing, BSE); rating rationale (ABSENT beyond the
single AR line quoted above; findable-missing, CARE Ratings site or BSE);
Reg 30 announcements (ABSENT; findable-missing, BSE); shareholding
pattern filings beyond the single FY26 year-end AR snapshot (ABSENT;
findable-missing, BSE/company IR page); FY24 and FY25 Annual Reports
(ABSENT; findable-missing, BSE/company IR page); screener companion CSVs
— Profit_Loss/Balance_Sheet/Cash_Flow/Quarters/Customization — populated
only as headers for AEQUS and all three peers, a collector defect, not a
company-side gap (findable-missing, screener.in); a more current
DYNAMATECH peer transcript beyond the single Feb-2024 investor-day
recording (findable-missing, company IR page or BSE). No item in this
list is judged plausibly-nonexistent: a company of this size and listing
recency would ordinarily generate all of the above, so their absence from
this corpus reads as a collection gap, not as evidence the company itself
publishes nothing here.

---

## SECTION 2: MENTAL MODEL DECLARATION

DRAFT - PENDING OPERATOR SIGN-OFF. This declaration is a transition
thesis, not a business description. It is signed only in claude.ai after
live-web stress-testing; nothing below changes that status.

### PART A — THE FROM STATE (the anchor, not the model)

**A1. ARCHETYPE.**
- **Aerospace line (85% of FY26 revenue, B04):** Build-to-spec component
  maker. Customer capex cycle = Airbus/Boeing single-aisle build-rate
  ramps; design-win pipeline = the qualification cycle and the new
  part-number count management itself tracks; content per unit = per-part,
  per-program supply under long-term OEM agreements (B04 revenue_streams
  "Contract manufacturing - build-to-print/spec long-term program
  supply"). Input-cost pass-through is contested, not confirmed: see B5
  below.
- **Consumer line (15% of FY26 revenue, B04):** Outsourcing partner
  (CDMO/EMS/IT services)-type archetype. Client concentration = Hasbro,
  Mattel, Spin Master and others named at AR p.121/p.20 (B04); capacity
  fill = the utilisation percentage management tracks quarterly; contract
  stickiness is LOW, not durable — Hasbro discontinued sourcing entirely
  in FY26 with no root cause given (B05 dropped_triggers).

**A2. THE SIMPLE ANALOGY.** Aequs runs factories inside a special economic
zone in Belagavi, plus smaller sites in France and the United States, that
make two very different kinds of things to other companies' exact
specifications. One factory line forges, machines, surface-treats and
assembles certified parts for aircraft, sold to Airbus, Boeing, Safran and
similar global names, where each part is approved for one specific
aircraft program and cannot easily be resourced elsewhere (B04). The other
line molds toys, cookware and plastic electronics housings for consumer
brands, where the same customer could, and in Hasbro's case did, take the
work elsewhere with little warning (B04; B05). The aircraft line is
profitable and growing. The consumer line is losing money and was built
out with a large amount of capital ahead of the volume needed to use it
(B04 flags "CAPITAL_ASSET_MISMATCH"). That is where the arrow begins.

### PART B — THE TRANSITION (the model)

**B1. FROM to TO.**
- **Aerospace:** FROM R2 COST-ADVANTAGED CONVERTER — margin sourced from
  India labour arbitrage and single-SEZ co-location logistics, not from
  priced differentiation (B04 moats_present "Cost advantage... moderate,
  replicable over time"). TO (claimed) R3 VALUE-ADDED / SPEC'D SUPPLIER —
  qualification lock-in, NADCAP/AS9100 certification and 15-year average
  top-3 customer tenure argue for partial pricing power and stickiness
  (B04 moats_present; B07 active_categories B2, A1). The Aerospace segment
  ROCE of 21.69% (Q1 FY27, Inv. Pres. slide 12) sits inside R3's 20-25%
  band. This TO claim is contested by the company's own words: management
  told analysts directly that "if we increase our margin, our win rate
  might come down" and that the company "don't own any IPs" (B12b MAJOR
  findings, Jun-2026 PDF p.18 and p.13) — a statement of price-taking, not
  of the partial pricing power R3 requires. Section 2 does not resolve
  this tension; it is carried forward into B5 and B6 below.
- **Consumer:** FROM at or below R1 COMMODITY PRICE-TAKER — no moat
  category scored Strong or Moderate anywhere in the emerging-moat scan
  (B07 active_categories), FY26 segment EBITDA margin -42.5% (B02 Note 36
  AR p.292). TO (claimed) something near R2 COST-ADVANTAGED CONVERTER —
  management's own long-term target states Consumer ROCE should reach
  "18-20%, same as aerospace" at steady state (B05 guidance list) — but no
  moat evidence in this corpus supports that destination; treat the claim
  as unevidenced aspiration, not a supported destination.

**B2. THE ENGINE.**
- Aerospace: (i) capacity-utilisation catch-up converts fixed costs
  already built into the SEZ into incremental margin as volume rises (B04
  unit_economics "most incremental revenue drops through to EBITDA once
  volumes rise against an already-built fixed cost base"); (ii) the
  disclosed order book (USD 889mn to USD 1,004mn in one quarter, B04)
  converting into revenue as the Safran A320-wheel programme and other
  qualified programs ramp.
- Consumer: capacity-utilisation alone. Utilisation must climb from 22%
  (Q1 FY27) toward the 40-50% FY27 exit target for the segment to move
  off its -42.5% margin base (B04 must_track_metrics; B12b).

**B3. THE PROOF GATE.**
- Aerospace: segment EBITDA margin, computed on a like-for-like basis that
  excludes other income and matches the guide's own cost-allocation
  definition, holds at or above 20% for two consecutive quarters. This
  matters because the reported Q4 FY26 headline EBITDA (Rs 32.1 cr)
  contained Rs 27.9 cr of other income, leaving an operational EBITDA of
  Rs 4.2 cr, disclosed only one quarter later (B12b CRITICAL finding,
  Jun-2026 PDF p.6 vs Aug-2026 PDF p.5); the Q1 FY27 23% segment margin
  itself is other-income-inclusive and unallocated-cost-exclusive against
  a guide defined on the exclusive basis (B12b MAJOR finding, Jun-2026 PDF
  p.9). Until a like-for-like reading clears 20% for two quarters running,
  the margin leg of the proof gate has not fired.
- Consumer: segment EBITDA loss narrows every quarter and utilisation
  climbs past 30%, on the way to the management-guided Q4 FY27 breakeven
  (B04 must_track_metrics; final/gate-recommendation.md monitorable 1).
  The stated kill condition, carried verbatim from this run's own
  falsification line, is a Q2 FY27 segment EBITDA loss at or wider than
  the Q1 FY27 figure of Rs 36.1 cr with utilisation still at or below 23%
  (final/gate-recommendation.md).

**B4. THE RECOGNITION GAP (open question, resolved at Stage 11).** Two
open questions, neither concluded here. For Aerospace: does the current
market price already reflect the segment's climb from a cost-advantaged
converter posture to a value-added, spec'd-supplier posture, such that any
further re-rating from a quality-tier migration is already spent and only
underlying earnings growth remains as a source of return; or does the
price still sit at the FROM-state converter posture, leaving the climb
itself unpriced? For Consumer: since no moat evidence supports the claimed
destination tier at all, is there any tier migration for the market to
price in the first place, or is Consumer's whole current value entirely a
function of whether it reaches basic operating breakeven? Stage 11's own
destination-multiple work under Section 1B settles both questions via the
multiple gap it computes; this dossier states no number, no conclusion,
and no verdict on either question.

**B5. THE UGLINESS TEST.**
- Aerospace: classified ARTIFACT-OF-CLIMB, provisionally. The segment's
  own reported numbers (26.9% FY26 margin, Rs 173.98 cr PBT +144.5%, PBT
  more than doubling) look clean on their face (B02 Note 36). But this
  classification is contingent, not settled: the verifier found that
  reported and segment EBITDA both embed other income in at least one
  quarter (B12b CRITICAL) and that the new-part-numbers-added metric, the
  company's own performance proxy for the qualification-lock-in engine,
  fell 80% quarter on quarter (433 to 86) with no explanation offered or
  asked for (B12b MAJOR). If either pattern recurs rather than reverses,
  this classification should move to STRUCTURAL-FEATURE.
- Consumer: classified STRUCTURAL-FEATURE. The ugly optic here (a -42.5%
  segment margin, segment assets nearly equal to Aerospace's for one-sixth
  the revenue, B04 flags "CAPITAL_ASSET_MISMATCH") is not yet showing the
  improving trend an "artifact of climb" reading would require: utilisation
  fell for three consecutive quarters (31% to 23% to 22%, B12b), the
  opposite of the direction the climb narrative needs, while the 40-50%
  FY27 exit target was held unchanged through that fall (B12b MAJOR).
  Management's own 75-80% utilisation precondition for the 18-20% steady-
  state ROCE guide sits far outside the near-term target (B12b MAJOR,
  Feb-2026 PDF p.22; Jun-2026 PDF p.10, p.15).

**B6. THE TRANSITION FALSIFIER (kept separate from Part C's business
falsifier).**
- Aerospace: the transition thesis is falsified if the like-for-like
  segment EBITDA margin (B3 basis) falls below 20% for two consecutive
  quarters, or if new part numbers added per quarter do not recover from
  the Q1 FY27 collapse without an explained cause — either would show the
  qualification-lock-in engine has stalled, not merely paused (B05
  triggers; B12b).
- Consumer: the transition thesis is falsified per this run's own stated
  falsification line: a Q2 FY27 segment EBITDA loss at or wider than Rs
  36.1 cr with utilisation still at or below 23% (final/gate-
  recommendation.md).

### PART C — WHAT THE MODEL WATCHES (derived from the transition)

**C1. DOMINANT VARIABLES.**
1. Aerospace segment EBITDA margin on a like-for-like, ex-other-income
   basis, quarter by quarter. Current state: FY26 reported 26.9% (audited
   segment note); Q1 FY27's reported 23% is not established on this basis
   (B12b MAJOR).
2. New aerospace part numbers added per quarter (management's own
   qualification-engine proxy). Current state: fell from 433 (Q4 FY26) to
   86 (Q1 FY27), an 80% drop, unexplained (B12b MAJOR).
3. Consumer segment utilisation percentage. Current state: fell three
   consecutive quarters, 31% to 23% to 22% (Q3 FY26 to Q1 FY27), against
   an unchanged 40-50% FY27 exit target (B12b MAJOR).
4. Consolidated operating cash flow against capex. Current state: FY26
   CFO -Rs 98.75 cr against capex Rs 342.6 cr; Q1 FY27 CFO -Rs 41.4 cr
   against Rs 83 cr capex (B03 FLAG-CASH; B04 must_track_metrics).

**C2. WHAT THE MODEL REJECTS.** Market-sizing questions are noise here,
not the binding constraint: the runway class is STRONG with roughly 9.5
times revenue headroom against the serviceable market (B09 runway_class,
revenue_headroom_x), so the execution variables in C1 bind long before any
market-size ceiling would. The model also rejects: management's own
"India's share of the global aerospace supply chain" framing (internally
inconsistent within a single sentence — both ~5% and ~2% are stated — and
unverifiable against any peer disclosure, B05/B06); the FY31 Vision targets
as a near-term signal (too distant to test against any current quarter,
B03 guidance_table); and consolidated ROCE, consolidated margin, or any
blended consolidated ratio as a read on Aerospace quality, since these
blend a 26.9%-margin segment with a -42.5%-margin one (B04
irrelevant_ratios).

**C3. THE BUSINESS FALSIFIER (distinct from the transition falsifier,
B6).** Two triggers, either sufficient alone. First: if the Aerospace
segment's own reported margin and ROCE are shown to be materially inflated
by non-operating items on a recurring basis across two or more further
quarters — not the single quarter's other-income spike already found
(B12b CRITICAL) — then the one segment currently described as a clean,
profitable precision-manufacturing franchise would have no verified
profitable core left anywhere in the Group, forcing a re-declaration of
the FROM business itself, not just of the transition. Second: if the Rule
11(g) audit-trail qualification and the seven-entity CARO adverse remarks
(B02; B03 FLAG-GOVERNANCE) recur in the FY27 Auditor's Report rather than
clearing as a first-year-listed transition matter, the reliability of
every company-narrated number this dossier assembles — not only the
transition-tracking variables — would need re-examination before any of
it could be relied on again.

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

(Drafted per the five-question spec at prompts/13-synthesis-pipeline.md,
BUSINESS UNDERSTANDING NARRATIVE section, from B03/B04/B06/B07/B09 only.
Stage 13's copy is the final version; this is the Halt 1 draft.)

Aerospace, 85 percent of FY26 revenue, makes certified precision parts and
assemblies built to a customer's own approved drawing under long-term OEM
programs: engine parts, structures, actuation, landing systems, turned
parts, interiors, cargo items and finished assemblies (B04
revenue_streams). Each aerospace part is qualified to one program on one
approved line, so a customer that wants to switch supplier must
re-qualify a new one from scratch, the switching-cost moat the emerging-
moat scan names Qualification lock-in (B04 moats_present; B07
active_categories, row B2). Consumer, 15 percent of revenue, makes toys,
cookware and durables, and consumer-electronics enclosures to a brand
owner's own specification, molded and machined at Koppal and Hubballi (B04
revenue_streams). Consumer work moves between contract manufacturers with
comparatively little friction, and this run did not establish a
comparable switching-cost moat on that line (B04 pricing_power "moderate";
no Consumer-specific entry in moats_present). Named aerospace customers
include Airbus, Boeing, Safran, Collins Aerospace, Honeywell, SAAB, GKN
Aerospace, Eaton, DTL and Bombardier (B03 ar_new_downstream_entities), and
four anonymised customers were 58.0 percent of FY26 revenue, all four in
Aerospace, with the top three relationships averaging 15 years' tenure
(B04; Note 36 AR p.294). Named Consumer customers include Hasbro, Mattel,
Spin Master, Tramontina, Wonderchef and Reliance Retail plus one unnamed
large consumer-electronics player (B04; AR p.121, p.20); Hasbro stopped
sourcing entirely during FY26 with no root cause disclosed on any of the
three calls read (B05 red_flags, dropped_triggers). The present demand
driver is the Airbus and Boeing single-aisle build-rate ramp, a read the
peer stage corroborates from two listed peers' own order books rather than
from Aequs alone (B06 verified list; industry_cross_read.demand). The
disclosed order book grew from USD 889 million at 31 March 2026 to USD
1,004 million at Q1 FY27, and the B09 downstream candidate set names the
external checks by name: the combined Airbus and Boeing single-aisle and
long-range delivery and backlog trend, the Safran Landing Systems A320
wheel programme ramp, the Collins Aerospace, Honeywell, GKN Aerospace and
Eaton programme awards, and the USD/INR exchange rate, since nearly all
Aerospace revenue is dollar-linked (B09 downstream_candidates; B06 red
flag on the 93-95 percent USD linkage). Forward growth on the Aerospace
side rests on two unbooked Farnborough Tier-1 agreements, the Hosur
aero-engine and landing-gear site, and the India ECMS/PLI 2.0 approval,
each carrying a named external check in the B09 candidate set: the state
MoU milestones to state-government releases, the ECMS approval to MeitY
and PIB releases (B09 downstream_candidates; B07 catalysts_12m). On the
Consumer side the equivalent forward driver is Mattel and Spin Master's
own global sourcing and production guidance, a signal B09 names as
externally checkable through their own quarterly disclosures (B09
downstream_candidates). Only the Aerospace line carries a scanned,
evidenced moat: the emerging-moat scan's three strongest forming
categories, all graded Strong, are Qualification lock-in, Geographic
first-mover position (the Belagavi SEZ and Hosur build-out) and Strategic
partnerships, and all three sit inside Aerospace (B07 active_categories).
Two of the capabilities behind that moat sit inside joint ventures Aequs
does not wholly own, surface treatment with Magellan Aerospace and forging
with Aubert & Duval (B04 moats_present). Consumer carries no scanned moat
category of its own, and the same scan finds the two purely financial
categories it tested, cash reserves and working-capital strength, argue
against the company rather than for it at the whole-company level (B07
flags FLAG-CASH). The run did not establish a per-unit price or margin
figure for either line; only segment-level revenue and EBITDA margin are
disclosed, not a rupee figure per aerospace part number across the roughly
5,654 SKUs in the portfolio, and not a per-unit figure for Consumer at all
(B04 unit_economics).

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. VERTICALS FRAMED

**Vertical 1 — Aerospace segment EBITDA margin, like-for-like.** The
corpus establishes the audited FY26 segment EBITDA margin (26.9%, Note 36
AR p.292) and the two quarterly headline figures management has since
quoted (20% guide "maintained at 20%" per the Q4 FY26 call, p.3; "above
20%" per the Q1 FY27 call, p.3 — a phrasing shift Verifier A flagged as a
non-overridable source-fidelity finding, B12a). It cannot establish a
clean quarterly like-for-like margin series, because the Q4 FY26 headline
EBITDA figure has already been shown to embed other income (B12b
CRITICAL) and the Q1 FY27 23% figure is on a different cost-allocation
basis than the guide it is measured against (B12b MAJOR). Questions this
run cannot close: (1) what is the operational, ex-other-income Aerospace
segment margin in Q1 and Q2 FY27, on the same basis as the 20% guide; (2)
has the phrasing shift from "maintained at" to "above" 20% actually
tightened the bar, or is it a clarification with no substance; (3) does
the new-parts-added collapse (433 to 86) reflect a genuine slowdown in the
qualification pipeline, or a reporting artifact.

**Vertical 2 — New aerospace part numbers added per quarter.** The corpus
establishes the two data points themselves: 433 in Q4 FY26, 86 in Q1 FY27
(B12b MAJOR, Jun-2026 PDF p.4 vs Aug-2026 PDF p.3), against a stated
"100-plus, 150 parts per month" claim from the intervening call (B12b,
Jun-2026 PDF p.10, p.15-16). It cannot establish why the collapse
happened: no analyst asked, and management did not address it
unprompted (B12b). Questions: (1) is the metric itself measured
consistently quarter to quarter (a single large program qualifying many
parts at once versus steady incremental additions); (2) does the metric
recover in Q2 FY27; (3) does a recovery or non-recovery correlate with
order-book growth in the same quarter.

**Vertical 3 — Consumer segment utilisation.** The corpus establishes the
three-quarter utilisation trend (31% to 23% to 22%, Q3 FY26 to Q1 FY27,
B12b MAJOR) against the unchanged 40-50% FY27 exit target (B04
must_track_metrics), and the segment margin trend that goes with it
(-24% H1FY26 company-memory figure superseded by the audited -42.5% FY26
full-year figure, B01 FLAG-GATE0 reason). It cannot establish the FY27
capex split behind this line with confidence: the Rs 500 cr of Rs 660 cr
consumer capex commitment named in the Q4 FY26 call became explicitly
conditional on utilisation materialising one quarter later (B05 flags),
and a verifier separately found the capex_embedded_growth figure Stage 7
carried (63%) rests on the claim-grade Rs 660 cr guide rather than on
capex under execution, which recomputes to 1.7% on the audited Rs 21.01 cr
commitment or 8.0% on Q1 FY27's actual Rs 83 cr spend (B12c MAJOR).
Questions: (1) does utilisation actually turn upward in Q2 FY27, reversing
three straight quarters of decline; (2) does the conditional Rs 500 cr
commitment get phased down, as management now says it would if utilisation
misses; (3) what specific evidence, beyond a stated date, supports the
Q4 FY27 breakeven milestone given the current trend runs the other way.

**Vertical 4 — Consolidated operating cash flow against capex.** The
corpus establishes the audited FY26 figures directly (CFO -Rs 98.75 cr
against Rs 342.6 cr capex, converting zero of Rs 154.45 cr EBITDA to
operating cash, B03 FLAG-CASH) and the Q1 FY27 figure from the concall
(CFO -Rs 41.4 cr against Rs 83 cr capex, B04). It cannot establish whether
this is growth-induced or structural: this run's own cash-conversion
determination is INDETERMINATE, capped at that reading because the
missing evidence (a rating agency's own working-capital commentary, a
receivables-ageing schedule beyond the AR's own note, and a management
reconciliation of operational EBITDA excluding other income) sits outside
this corpus by name (final/gate-recommendation.md FLAG-CASH section).
Questions: (1) does CFO turn positive in FY27 as revenue scales, or does
the working-capital build keep pace with revenue growth; (2) does the
Axis Bank stock-statement gap on trade receivables, which widened every
quarter of FY26 to Rs 59.01 cr, continue to widen in FY27; (3) is the
~USD 150mn raise management has flagged as possibly needed debt-weighted
or equity-heavy, and does it arrive before or after operating cash flow
turns.

### 4b. CANDIDATE SIGNAL TABLE

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| Airbus + Boeing combined single-aisle/long-range delivery and backlog trend | The combined build-rate/backlog trend flattens or declines for two consecutive quarters while Aequs's own order book keeps accelerating, decoupling the two | Monthly | Airbus/Boeing monthly delivery reports, annual order-and-delivery statements (B09) |
| Safran Landing Systems A320 wheel programme ramp (15-yr agreement) | No deliveries or revenue recognition begins on the guided schedule, or Safran's own disclosures make no mention of an India-sourced wheel programme | Event-driven | Safran investor disclosures; Aequs Reg-30 filings (B09) |
| Collins Aerospace / Honeywell / GKN Aerospace / Eaton programme awards | No new award is named or booked in the disclosed order book for two or more consecutive quarters despite continued "pipeline" commentary | Event-driven | Company investor-relations pages, aerospace trade press (B09) |
| India ECMS / PLI 2.0 scheme approvals and disbursement | No disbursement or eligible-income recognition occurs in FY27 despite the approval already being confirmed | Event-driven | MeitY / PIB press releases (B09) |
| Tamil Nadu (Hosur) and Karnataka state MoU execution milestones | Hosur Phase-1 commissioning slips past the guided Sep-2026 to Mar-2027 window, or either MoU is scaled back or unwound | Event-driven | State government press releases; Aequs Reg-30 filings (B09) |
| USD/INR exchange rate | A sharp rupee move compresses or inflates reported segment margin without management separately disclosing the FX effect | Monthly | RBI reference rate / FBIL (B09) |
| Mattel and Spin Master global sourcing/production guidance | Either customer's own guidance signals a sourcing pull-back from India or from Aequs specifically, echoing the undisclosed Hasbro exit | Quarterly | Mattel/Spin Master quarterly earnings calls (B09) |

These seven are UNVERIFIED. Verification and tracker writes happen at
Role 5.5 in claude.ai.

### 4c. FRAGILITY READ

- **variable_count: 7.** The bull case needs: (1) Aerospace like-for-like
  segment margin holding at or above 20%; (2) new-parts-added pace
  recovering; (3) Consumer utilisation climbing past 30%; (4) operating
  cash flow turning positive or the gap to capex narrowing; (5) the order
  book converting on schedule, backed by the Safran ramp and Airbus/Boeing
  build rates; (6) the audit-trail qualification and CARO adverse remarks
  clearing in FY27 rather than recurring; (7) the FY27-31 capex programme
  funding without an equity-heavy raise.
- **verifiability_ratio: 4 of 7 externally observable.** Variables 4
  (audited cash flow statement), 5 (Airbus/Boeing delivery reports, Safran
  investor disclosures), 6 (the next audited Auditor's Report and CARO
  Annexure), and 7 (Reg 30/exchange filings on any raise) are checkable
  outside company narration. Variables 1, 2 and 3 are company-narrated
  only in this corpus — no independent source discloses Aequs's own
  segment margin composition, its part-qualification pace, or its segment
  utilisation percentage.
- **single_point_failure:** governance and audit-trail control-environment
  reliability. If the Rule 11(g) qualification and the seven-entity CARO
  adverse remarks (B02; B03 FLAG-GOVERNANCE) persist into the FY27
  Auditor's Report rather than clearing as a first-year-listed transition
  matter, confidence in every other company-narrated variable in this list
  (1, 2, 3, and even the composition of 4) breaks at once, since all of
  them rest on the same set of company disclosures the auditor has already
  qualified for record-keeping reasons.
- **fragility_verdict: FRAGILE.** Seven variables, three of them
  company-narrated only, one named single point of failure that would
  undermine the credibility of the company-narrated set as a whole, and a
  bull case that needs several of the seven to move together (Aerospace
  margin holding AND Consumer utilisation turning AND cash conversion
  improving AND the order book converting on schedule).

### 4d. RESEARCH BRIEF (claude.ai work order)

1. Fetch the RHP/DRHP (SEBI, BSE, or company IR page) to confirm and
   quantify: the promoter litigation matter naming Jagadish Shivaputrappa
   Melligeri, the restated pre-IPO financials, the full promoter/group
   history, and the pre-IPO shareholding pattern (B08 searches_skipped,
   all egress-blocked this run).
2. Obtain the CARE Ratings press release or rationale for the Rs 25 cr
   long-term bank facility rating (CARE BBB-;Stable), from the CARE
   Ratings site or a BSE filing; not in this corpus.
3. Fetch Reg 30 filings for: the Safran A320-wheel agreement's actual
   terms and value, any separate Safran engine-parts agreement (not
   independently identifiable in any of the three transcripts read, B05
   analyst_note), the CFO resignation filing, the Scheme of Amalgamation
   filing status, the FY27 capex reallocation, and any capital raise
   (~USD 150mn) announcement.
4. Fetch the Q1 FY27 results filing directly from BSE/NSE; every Q1 FY27
   number in this dossier traces only to the investor presentation or the
   concall transcript, never to a filed results document.
5. Obtain the FY24 and FY25 Annual Reports (BSE or company site) to extend
   the ROCE, working-capital-days, and cash-conversion series beyond the
   two years this AR alone can compute.
6. Verify the identity behind the anonymised Customer 1-4 (58% of FY26
   revenue) and confirm or deny whether Safran sits among them (B02
   questions_for_mgmt).
7. Verify Airbus and Boeing's own monthly delivery and backlog data
   independently of management's framing, to corroborate the single-aisle
   demand driver.
8. Verify the state incentive packages reciprocal to the Tamil Nadu
   (Hosur, Rs 1,900 cr) and Karnataka (Rs 2,856 cr) MoUs, not disclosed in
   this corpus (B07 input_gaps), and verify whether the funded five-year
   USD 350-400mn plan covers both MoUs or displaces one against the other
   (B12b MAJOR finding on the unreconciled totals).
9. Verify management's claim on India's share of the global aerospace
   supply chain (stated as both ~5% and ~2% in the same sentence, B05/B06)
   against an independent industry source, since none of the three peers
   could corroborate it (B06 unverifiable list).
10. Verify Mattel, Spin Master and Hasbro's own sourcing guidance directly
    from their quarterly disclosures, to test the Consumer demand driver
    and the undisclosed root cause of the Hasbro exit.
11. Verify the PLI/ECMS scheme quantum and sunset date specific to Aequs
    (approval confirmed, value NOT FOUND in this corpus, B07 input_gaps)
    via MeitY/PIB releases.
12. Verify the shareholding-pattern trend (pledge, FII/DII holding,
    promoter selling pattern) at the next quarterly filing, since the AR
    gives only one first-year-listed snapshot with no year-on-year
    comparison (B03 5D).

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. Aequs makes certified parts for aircraft, and separately makes toys,
   cookware and electronics housings for consumer brands, in factories in
   Belagavi, Koppal and Hubballi plus smaller sites in France and the US.
2. Aircraft parts are 85 percent of sales. The consumer goods line is 15
   percent.
3. Each aircraft part is approved for one program on one production line.
   A customer cannot easily move that work to a rival supplier.
4. Airbus, Boeing, Safran and other global names buy the aircraft parts.
   Four unnamed customers make up 58 percent of last year's sales.
5. Hasbro, Mattel and Spin Master buy the consumer goods. Hasbro stopped
   buying entirely during the year. No one explained why on any of the
   three calls this run read.
6. Demand for the aircraft parts follows how fast Airbus and Boeing build
   single-aisle planes. Two other listed Indian suppliers confirm the
   same demand pattern from their own order books.
7. The disclosed order book for aircraft parts grew from about 890
   million dollars to just over 1,000 million dollars in one quarter. A
   new 15-year deal with Safran to supply aircraft wheels backs future
   growth.
8. The aircraft parts business already earns a 26.9 percent profit margin
   before interest, tax and depreciation, ahead of the company's own near-
   term target for that number.
9. The consumer goods business lost money at a rate of 42.5 percent of its
   sales last year. How much of the factory sits idle kept falling for
   three straight quarters even as the year-end target for that number
   stayed the same.
10. The pipeline's own early screen scores this company AVOID. That score
    comes from weak cash generation and weak returns across four years,
    not from the aircraft-parts story, which the same screen finds clean.
11. Cash from operations turned negative last year. A profit of about
    154 crore rupees on paper produced no actual operating cash. Almost
    all the cash sitting on the balance sheet came from the December 2025
    stock-market listing, not from running the business.
12. Both of the company's audit reports for the year carry a formal
    exception. Seven group companies carry adverse remarks from the
    auditor.
13. An independent check of the earnings calls found gaps the company's
    own reporting did not surface: a one-time non-operating gain sat
    inside a headline profit number without being called out, and the
    count of newly qualified aircraft parts fell by four-fifths in one
    quarter with no explanation offered.
14. This run had no prospectus, no filed quarterly results, no rating
    report and no shareholding filing to work from. Every recent number
    traces to an earnings call or a slide deck, never to a filed report.
15. The model behind this company is a bet that the aircraft business
    grows fast enough, and reports cleanly enough, to carry the consumer
    business and the cash gap until both turn a corner. That bet rests on
    several moving parts at once, most of them known only from the
    company's own account of itself, which makes the model fragile until
    more of those parts can be checked independently.

---

## SECTION 6: STANDING EXTRACTION ANNEX

Ten standing questions, answered from the corpus, quote-then-comment.

**1. UNITS.** No per-unit revenue, price, or margin figure is printed
anywhere in the corpus for either line. Aerospace: "our portfolio expanded
to 5,654 SKUs during the year" (AR p.11) and a separate chart states
"5,654 Aerospace Products" (AR p.18); both describe the same product-
portfolio count, a basket, not a single product. No revenue-per-SKU,
revenue-per-tonne, or price-per-part figure is printed. The lines from
which one could be derived: Aerospace net external revenue Rs 1,046.38 cr
FY26 (Note 36, "Net external revenue 10,463.75" [INR Mn], AR p.292) against
the 5,654-SKU portfolio count (AR p.11/p.18) — the AR itself never divides
one by the other. Consumer: net external revenue Rs 184.06 cr FY26 (Note
36, "Net external revenue... 1,840.61" [INR Mn], AR p.292); no unit count
(pieces, cases, or SKUs shipped) is printed anywhere in the corpus for
Consumer, so NOT DISCLOSED and no derivation is possible from this corpus
alone.

**2. SEGMENT CAPITAL AND DEBT.** Note 36 gives segment assets and
liabilities, two periods, in INR Millions: "Segment assets 13,783.42
12,868.60 26,652.02 (71.73) 26,580.29 10,148.71 8,701.64 18,850.35
(602.69) 18,247.66" and "Segment liabilities 4,741.99 7,202.93 11,944.92
(74.29) 11,870.63 6,893.90 5,147.00 12,040.90 (602.28) 11,438.62"
(Aerospace / Consumer / Total / Eliminations / Total, FY26 then FY25; AR
p.293). In Rs Crore: FY26 segment assets Aerospace 1,378.34, Consumer
1,286.86; FY26 segment liabilities Aerospace 474.20, Consumer 720.29.
FY25 segment assets Aerospace 1,014.87, Consumer 870.16; FY25 segment
liabilities Aerospace 689.39, Consumer 514.70. No "capital employed" line
is printed by segment anywhere in Note 36. Borrowings are NOT allocated by
segment: Note 36 carries no borrowings row, and the only borrowings
figures in the corpus sit at Group level — "Total borrowings" Rs 657.58 cr
FY26 against Rs 785.05 cr FY25 (Note 28(C)(ii), per B02's direct citation
of AR p.282). Comment: since borrowings are unallocated, any segment-level
leverage or interest-coverage read this run's own stages construct (for
example Aerospace vs Consumer finance costs, B02 top_findings rank 1,
which allocates finance costs of Rs 58.25 cr Aerospace and Rs 55.06 cr
Consumer through the segment result bridge in Note 36 itself, not through
a separate borrowings split) rests on the segment RESULT bridge, not on a
segment BALANCE SHEET debt allocation, which this AR does not provide.

**3. GUIDANCE VERSUS ASPIRATION.** Every forward number found in the
corpus, classified (source: B05 guidance list, cross-checked against B03
guidance_table for the AR-sourced items):

| Number | Timeframe stated | Class | Stated in |
|---|---|---|---|
| Aerospace revenue growth 25-30% YoY | FY27 | (a) guidance, period stated | Q4 FY26 call |
| Aerospace segment EBITDA margin "maintained at 20%" (Q4 FY26 call, p.3) / "above 20%" (Q1 FY27 call, p.3) — two framings, not one (B12a source-fidelity finding) | FY27 | (a) guidance, period stated, but the bar itself is inconsistently worded between calls | Q4 FY26 call, reaffirmed with different wording Q1 FY27 |
| Consumer revenue growth 125-150% YoY | FY27 | (a) guidance, period stated | Q4 FY26 call |
| Consumer EBITDA breakeven | Q4 FY27 | (a) guidance, period stated | Q4 FY26 call, reaffirmed Q1 FY27 |
| Consolidated revenue growth 45-50% | FY27 | (a) guidance, period stated | Q4 FY26 call, reaffirmed Q1 FY27 |
| Consolidated PAT breakeven | H1 FY28 | (a) guidance, period stated (slipped from an informal pre-IPO "end FY27" framing, B05 timeline_slippages) | Q4 FY26 call, reaffirmed Q1 FY27 |
| FY27 capex Rs 660 cr (Rs 500 cr consumer / Rs 160 cr aerospace) | FY27 | (a) guidance, period stated, but the consumer leg became explicitly conditional on utilisation one quarter later (B05 flags) | Q4 FY26 call; reallocation flagged Q1 FY27 |
| Consumer utilisation target ~40-50% | by FY27 year-end | (a) guidance, period stated | Q4 FY26 call, reaffirmed Q1 FY27 |
| Hosur (Tamil Nadu) investment Rs 1,900 cr | 10 years | (a) guidance, period stated | Q4 FY26 call, reaffirmed Q1 FY27 |
| Karnataka MoU investment Rs 2,856 cr | 5 years | (a) guidance, period stated | Q4 FY26 call, reaffirmed Q1 FY27 |
| Group 5-year capex plan USD 350-400mn | FY27-31 | (a) guidance, period stated; does not reconcile to the Rs 4,756 cr combined MoU total (B12b MAJOR) | Q1 FY27 call |
| Consumer PAT breakeven | FY30 | (a) guidance, period stated, 3+ years out, not independently testable this run | Q1 FY27 call |
| Group steady-state ROCE ~20% | FY31 | (a) guidance, period stated, but framed as "steady state" against a FY26 consolidated actual of 1.56% with no interim bridge (B03 4C) | Q1 FY27 call |
| Vision 2031 revenue 4-6x FY26 base | FY2030-31 | (a) guidance, period stated, though the AR itself frames it as "Vision," reading as aspirational in tone despite the stated period | CEO letter, AR p.10 |
| Vision 2031 EBITDA margin 18-22% | FY2030-31 | (a) guidance, period stated | CEO letter, AR p.10 |
| Consumer revenue mix 40-60% of total | "over 5 years" | (a) guidance, period stated, though the start point is not fixed | Q1 FY27 call |
| Possible capital raise ~USD 150mn | "not this year unless capex pull-in/inorganic" | (b) aspiration, no fixed period, explicitly conditional | Q1 FY27 call |
| Consumer asset turns (steady state) ~1.5x | "peak utilization" | (c) capacity/capability only, tied to a state not a date | Q4 FY26 call, reaffirmed Q1 FY27 |
| Consumer ROCE (steady state) 18-20% | "long-term" | (b) aspiration, no fixed period | Q4 FY26 call, reaffirmed Q1 FY27 |
| Aerospace utilisation target ~75% | "ongoing" | (c) capacity/capability only | Q3 FY26 call |
| PLI/ECMS approval received | not stated | (c) capacity/capability only; approval confirmed but scheme quantum and sunset date NOT FOUND (B07 input_gaps) | Q3 FY26 call |

**4. CONCENTRATION.** Product: top-product share is NOT DISCLOSED; the AR
discloses no per-part or per-program revenue percentage, only the four-
customer table below. Customer: "Customer 1 Aerospace 2,814.38 22.87%...
Customer 2 Aerospace 2,347.05 19.07%... Customer 3 Aerospace 723.88
5.88%... Customer 4 Aerospace 1,248.99 10.15%" (Note 36, AR p.294; INR
Mn), summing to 57.97%, all four in Aerospace and none named. Geography
(revenue): "India 1,459.97 11.87%... The United States of America
2,866.41 23.30%... France 2,547.15 20.70%... Hong Kong 1,070.45 8.70%...
Sweden 723.87 5.88%... United Kingdom 1,242.97 10.10%... Germany 1,469.39
11.94%... Others 924.15 7.51%" (Note 36, AR p.293; INR Mn, FY26). Comment:
customer concentration (58% in four names) and geographic concentration
(USA + France = 44% of revenue) sit together, but the AR names neither the
four customers nor states whether Safran is among them (B02 questions_for_
mgmt).

**5. PROMISE LEDGER.**

| Promised in | Promise | Outcome | Evidence anchor |
|---|---|---|---|
| Q3 FY26 | Hasbro "growing", will continue alongside Mattel | Missed | Hasbro discontinued sourcing entirely, disclosed Q4 FY26 as "unexpected", no root cause given (B05) |
| pre-IPO (cited by analyst, Q3 FY26) | Consolidated PAT positive by end of FY27 | Missed | Formal guide became H1 FY28 (Q4 FY26 call), attributed to customer capacity-expansion requests (B05) |
| Q4 FY26 | Aerospace FY27 revenue +25-30% at >20% segment EBITDA margin | Delivered per B05; OVERSTATED per verifier (B12b MAJOR) | Q1 FY27 delivered +40% YoY at a reported 23% segment margin, but that figure is other-income-inclusive and unallocated-cost-exclusive against a guide defined on the exclusive basis (Jun-2026 PDF p.9) — the revenue leg is clean, the margin leg is not established like-for-like |
| Q4 FY26 | Consumer FY27 revenue +125-150% | Delivered | Q1 FY27 delivered +190% YoY (B05) |
| Q4 FY26 | Consumer EBITDA loss path to Q4 FY27 breakeven | Partial | Q1 FY27 loss narrowed Rs 473mn to Rs 361mn, -24% QoQ, first quarterly proof point; full realisation still three quarters out (B05) |
| Q3 FY26 | Aerospace utilisation ~71%, targeting ~75% | Partial | Q1 FY27 cites ~70% unchallenged, "adding a machine a week"; not re-quantified consistently every quarter, and a second analyst figure of 80% was left uncorrected the same call (B05; B12b MINOR) |
| Q3 FY26 | MeitY/ECMS PLI approval received | Partial | Q4 FY26: no FY26 income booked, FY27 is first eligible year; a timing clarification, not a miss (B05) |
| Q4 FY26 | FY27 capex Rs 660 cr, split Rs 500 cr consumer/Rs 160 cr aerospace | Partial | Q1 FY27: total unchanged but the split reallocating toward aerospace, disclosed proactively (B05) |

Verifier B additionally found, outside this ledger's original eight rows,
that the Q4 FY26 headline EBITDA and reported PAT loss each concealed a
favourable item not disclosed until the following call (Rs 279mn of other
income inside a Rs 321mn headline EBITDA; a Rs 90mn exceptional gain
inside a Rs 541mn reported loss), and that the count of new aerospace
parts added fell 433 to 86 quarter on quarter against a moat claim made
one call earlier (B12b CRITICAL and MAJOR findings).

**6. RESTATED BASES.** No restated prior-period comparative was found in
the audited financial statements: "A full-document search for
'restat[ed/ement],' 'prior period error,' and 'regroup' returns only an
unrelated ESOP-plan reference" (B02 (j)). One business-transfer note
exists but is not a restatement: "one of the Group's subsidiary company -
Aequs Consumer Products Private Limited (ACPPL) has entered into an
agreement with Aequs Cookware Private Limited (ACPL) and transferred
certain assets and liabilities relating to its Consumer Durable Goods
business unit effective from October 1, 2024" (Note 33, AR p.283-284),
accounted for prospectively from the transfer date, not as a restatement
of prior-year figures (B02 2A). Outside the audited statements, two
concall-level metrics were restated between consecutive calls without
reconciliation: FY25 fixed-asset turnover, "1.3X" (Q3 FY26 call, Feb-2026
PDF p.8) versus "1.84x" (Q4 FY26 call, Jun-2026 PDF p.6), same base year
(B12b MAJOR); and FY26 net working-capital days, 151 per the Q4 FY26 call
versus 127 per the Q1 FY27 call for the same year-end close (B05 flags,
never reconciled).

**7. CORPORATE-ACTION CLAUSES.** One scheme is in the corpus: "The Parent
Company, vide its board resolution dated April 23, 2026, has approved the
Scheme of Amalgamation of certain wholly owned subsidiaries i.e.,
AeroStructures Manufacturing India Private Limited, Aequs Engineered
Plastics Private Limited and Aequs Force Consumer Products Private
Limited with itself. As of the date of adoption of these financial
statements, the Scheme and the related applications are yet to be filed
with requisite authorities, and necessary approvals are still pending...
this will be a transaction between entities under common control...
Following the merger, these wholly owned subsidiaries will be subsumed
into the Parent Company and will cease to exist as separate legal
entities. This merger will not have an impact on the consolidated
financial statements of the Group" (Note 41, AR p.302). Comment: no
exchange ratio is disclosed because all three entities are wholly owned
(no minority consideration to allocate); no appointed date or effective
date is stated, since approvals were pending as of the 26-May-2026
sign-off; the only liability-allocation language given is that the
subsidiaries "will be subsumed into the Parent Company." A second,
smaller corporate action is disclosed: "On July 11, 2024... Aequs
Consumer Products Private Limited (ACPPL) has entered into an agreement
with Aequs Cookware Private Limited (ACPL) and transferred certain assets
and liabilities relating to its Consumer Durable Goods business unit
effective from October 1, 2024. The consideration of [Rs 300.53 Mn] is
receivable after two years from the effective date of transfer and
interest of 12% p.a. on the outstanding consideration amount is receivable
quarterly" (Note 33, AR p.283-284), with Total Assets transferred Rs
619.46 Mn and Total Liabilities Rs 318.93 Mn against the table printed
there. The Dec-2025 IPO itself carries no scheme document in this corpus:
the prospectus/RHP is ABSENT (B00; B08 input_gaps); fetch the SEBI or BSE
RHP filing. No preferential issue or buyback is disclosed anywhere in the
corpus.

**8. RELATED-PARTY PERIMETER.** The AR's Note 34 names the promoter-linked
"Enterprises in which individuals owning interest in the Group, or their
relatives have control, joint control or significant influence": "Aequs
SEZ Private Limited ('ASEZ')... Automotive End Solution Private
Limited('AESPL')... Melligeri Investments LLC ('MILLC')... Industrial
Knowledge Centre Private Limited ('IKC')... MFRE Texas Holding LLC, USA...
MFRE Taris, LLC... MFRE Private Trust... MFRE Estate Private Limited
('MFREEPL')... Altum Trust ('Altum')... QuEST Global Engineering Services
Private Limited ('QGESPL')... Aequs Stock Option Plan Trust ('ESOP
Trust')... MFO IP Holdings Private Limited [formerly known as Aequs
Limited, Malta ('ALM')] ('MFO IP')... Hubballi Durable Goods Cluster
Private Limited ('HDGCPL')" (Note 34, AR p.285). Latest-year transaction
amounts, aggregated across the full purchase/services-received table:
API Rs 44.13 cr, ASEZ Rs 32.84 cr, HDGCPL Rs 17.67 cr, SQuAD purchases Rs
16.29 cr (+283% YoY), QGEPL Rs 2.76 cr, MFRE Taris Rs 1.54 cr, summing to
approximately Rs 115 cr, about 9.4% of consolidated revenue (Note 34, AR
p.284-289; B02 (g)). Individually quoted from the transaction table:
"ASEZ... Financial guarantee expense 58.49... Interest expense on lease
liability 211.90... Repayment of lease liability 307.22" (Note 34, AR
p.286, INR Mn). The holding company (up to 10-Dec-2025), AMIPL, carries
its own interest expense line: "Holding Company - AMIPL... Interest
expense -others 34.41 32.77" (Note 34, AR p.286, INR Mn, FY26 vs FY25).
Two related-party loans price at 13% p.a.: AMIPL Rs 28.43 cr and
Melligeri Investment LLC Rs 1.81 cr (Note 15, AR p.264-266; B03 2B). A
flat Rs 1 cr/year branding fee runs to MFO IP Holdings, unchanged FY25 to
FY26 (B02 (g)).

**9. PLEDGE AND SHAREHOLDING.** Pledge: 0%. The AR's shareholding-pattern
page carries no pledge line at all (AR p.111-112), and no twelve-quarter
series exists in this corpus or can exist: the company listed only
10-Dec-2025, so at most two quarter-end snapshots (Dec-2025, Mar-2026)
could plausibly exist before this run date, and the shareholding folder
in this corpus is empty — NOT DISCLOSED beyond the single FY26 year-end
snapshot the AR itself carries. That snapshot, quoted directly: "1.
Promoters and Promoters Group 396207820 59.08%... 3. Mutual Funds
37762324 5.63%... 4. Foreign Portfolio Investors (Corporate) 26149081
3.90%... 5. Insurance Companies 590772 0.09%... 6. NBFCs registered with
RBI 1000000 0.15%... 7. Alternate Investment Funds 36991974 5.52%... 10.
Foreign Companies 97068846 14.47%... 11. Foreign Nationals 15237915
2.27%... 12. Hindu Undivided Family 595380 0.09%... 13. Non-Resident
Indians 7105769 1.06%... 14. Trusts 3889552 0.58%... 15. Body Corporate -
LLP 5845234 0.87%... 16. Resident Individuals 25521392 3.81%... 17. Key
Managerial Personnel 180711 0.03%... 18. Directors and their relatives
(excluding independent directors and nominee directors) 707365 0.11%...
19. Aequs Stock Option Plan Trust 15811500 2.36%" (AR p.111-112, as at
31-Mar-2026). Institutional holding latest, combining the mutual fund,
FPI, AIF and insurance rows above: approximately 15.14% of shares held by
domestic and foreign institutional categories, plus a further 14.47% held
by "Foreign Companies," a category the AR does not further identify below
the promoter line.

**10. VERIFICATION.**

| Document | Filename | Date |
|---|---|---|
| Annual Report FY2025-26 | annual-report/Annual_Report_2026.pdf | Sign-off 26-May-2026; filed with AGM notice dated 2026 |
| Q3 FY26 concall | concalls/Concall_Feb_2026_Transcript.pdf | Filed 04-Feb-2026 |
| Q4 FY26 concall | concalls/Concall_Jun_2026_Transcript.pdf | Held 26-May-2026, filed 02-Jun-2026 |
| Q1 FY27 concall | concalls/Concall_Aug_2026_Transcript.pdf | Held 29-Jul-2026 |
| Q1 FY27 investor presentation | presentation/Investor_Presentation_1.pdf | Q1 FY27 (quarter ended 30-Jun-2026) |

CORPUS COMMIT HASH: 53a59aeecea0c852c3e6cac719d3fddb95915265


## HANDOFF BLOCK (B09b-dossier, as returned by the stage; Section 6 above ends with the corpus commit hash line)

```yaml
stage: B09b-dossier
company: "AEQUS"
run_date: "2026-09-05"
model: claude-sonnet-5
status: complete
corpus_verdict: "CORPUS GAPPED"
corpus_gaps:
  - document: "prospectus / RHP"
    expected_source: "BSE / SEBI filing page or company IR page"
    kind: "findable-missing"
  - document: "all quarterly and annual results filings"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "rating rationale (only a single CG-report rating line exists in corpus)"
    expected_source: "rating agency site (CARE Ratings) or BSE"
    kind: "findable-missing"
  - document: "Reg 30 / corporate announcements"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "shareholding pattern filings beyond the single FY26 year-end AR snapshot"
    expected_source: "BSE / company IR page"
    kind: "findable-missing"
  - document: "FY24 and FY25 Annual Reports"
    expected_source: "BSE / company IR page"
    kind: "findable-missing"
  - document: "screener companion CSVs (Profit_Loss/Balance_Sheet/Cash_Flow/Quarters/Customization), header-only for AEQUS and all peers"
    expected_source: "screener.in"
    kind: "findable-missing"
  - document: "current DYNAMATECH peer transcripts beyond the single Feb-2024 investor-day recording"
    expected_source: "company IR page or BSE"
    kind: "findable-missing"
  - document: "research / broker notes"
    expected_source: "n/a"
    kind: "plausibly-nonexistent"
archetypes:
  - line: "Aerospace (85% of FY26 revenue)"
    archetype: "Build-to-spec component maker"
  - line: "Consumer (15% of FY26 revenue)"
    archetype: "Outsourcing partner (CDMO/EMS/IT services)"
transition:
  - line: "Aerospace"
    from_tier: "R2 COST-ADVANTAGED CONVERTER"
    to_tier: "R3 VALUE-ADDED / SPEC'D SUPPLIER (claimed; contested by management's own no-pricing-power statements)"
    engine: "Capacity-utilisation catch-up converting already-built SEZ fixed cost into margin, plus the USD 889mn-to-1,004mn order book converting via qualified programs including the Safran A320-wheel agreement"
    proof_gate: "Aerospace segment EBITDA margin, computed like-for-like ex-other-income on the guide's own cost basis, at or above 20% for two consecutive quarters"
    recognition_gap: "Open question, resolved at Stage 11: does the market price already reflect Aerospace's climb from a cost-advantaged converter to a value-added spec'd-supplier posture, leaving only earnings growth as a return source, or does price still sit at the FROM-state converter tier"
    ugliness: "ARTIFACT-OF-CLIMB"
    transition_falsifier: "Like-for-like segment EBITDA margin falls below 20% for two consecutive quarters, or new aerospace parts added per quarter (433 to 86 QoQ, unexplained) do not recover, evidencing the qualification-lock-in engine has stalled"
  - line: "Consumer"
    from_tier: "at or below R1 COMMODITY PRICE-TAKER"
    to_tier: "R2 COST-ADVANTAGED CONVERTER (claimed via management's 18-20% long-term ROCE guide; unsupported by any moat evidence found in this corpus)"
    engine: "Capacity-utilisation climbing from 22% (Q1 FY27) toward the 40-50% FY27 exit target"
    proof_gate: "Segment EBITDA loss narrows every quarter with utilisation past 30%, en route to the guided Q4 FY27 breakeven"
    recognition_gap: "Open question, resolved at Stage 11: since no moat evidence supports the claimed destination tier at all, is there any tier migration for the market to price, or is Consumer's value entirely a function of reaching basic operating breakeven"
    ugliness: "STRUCTURAL-FEATURE"
    transition_falsifier: "Q2 FY27 segment EBITDA loss at or wider than the Q1 FY27 Rs 36.1 cr, with utilisation still at or below 23%"
dominant_variables:
  - "Aerospace segment EBITDA margin on a like-for-like, ex-other-income basis, quarter by quarter"
  - "New aerospace part numbers added per quarter (qualification-engine proxy; fell 433 to 86 QoQ)"
  - "Consumer segment utilisation percentage (fell 31% to 23% to 22% across three quarters)"
  - "Consolidated operating cash flow against capex (FY26 CFO -Rs 98.75 cr vs Rs 342.6 cr capex)"
business_falsifier: "Either (a) the Aerospace segment's reported margin and ROCE are shown materially inflated by non-operating items on a recurring basis across two or more further quarters, leaving no verified profitable core anywhere in the Group, or (b) the Rule 11(g) audit-trail qualification and seven-entity CARO adverse remarks recur in the FY27 Auditor's Report rather than clearing as a first-year-listed transition matter, undermining the reliability of every company-narrated number in this dossier, not only the transition variables"
mental_model_status: "DRAFT - PENDING OPERATOR SIGN-OFF"
fragility:
  variable_count: 7
  verifiability_ratio: "4 of 7 externally observable"
  single_point_failure: "governance and audit-trail control-environment reliability: if the Rule 11(g) qualification and 7-entity CARO adverse remarks persist into FY27, confidence in every other company-narrated tracking variable breaks at once"
  fragility_verdict: "FRAGILE"
candidate_count: 7
research_brief_items: 12
plain_summary_points: 15
annex:
  present: true
  questions_answered: 10
  corpus_commit_hash: "53a59aeecea0c852c3e6cac719d3fddb95915265"
```
