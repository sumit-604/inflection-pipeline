# HALT 1 UNDERSTANDING DOSSIER
Entero Healthcare Solutions Ltd (ENTERO) | Run date 2026-07-27
Corpus commit hash: 7043fdb9360cc115f1bf6125e5cd77301e26a467

This dossier assembles what the pipeline already found. It carries no
valuation, no price, and no verdict. It is the understanding package the
operator reads before signing the Mental Model and deciding KILL / SHALLOW
WATCH / PROCEED.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

**1. CONCALLS.** Five transcripts held: Q1 FY26 (Aug-2025), Q2 FY26
(Nov-2025), Q3 FY26 (12-Feb-2026), Q4 FY26 (Jun-2026), Q1 FY27
(17-Aug-2026) (B00). Stage 5 read the three newest: Q3 FY26, Q4 FY26, Q1
FY27 (B05). Most recent quarter covered: Q1 FY27. The run date on this
dossier (2026-07-27) predates the Q1 FY27 concall date printed on the
document itself (17-Aug-2026); the corpus already carries material dated
after the stated run date, so no newer quarter is plausibly missing on a
run-date test (B00).

**2. ANNUAL REPORTS.** One AR held: FY26 (year ended 31-Mar-2026), 276
pages, filed 2026-07-27 (B00). This is the latest completed FY. Only one
year of AR is held; fewer than 3 years. The company listed ~Feb-2024, so
a 3-year AR trail would in any case only reach into the pre-listing
period, which the missing prospectus (below) would normally cover (B00,
B03).

**3. RESULTS FILINGS.** Latest quarterly filing: Q1 FY27, dated 07-Aug-2026
(B00). No quarter-gap to the AR: the AR (FY26, filed 2026-07-27) and the
Q1 FY27 results (a later quarter) both sit in the corpus; the freshness
pair AR-to-latest-audited-results passes (B00).

**4. INVESTOR PRESENTATIONS.** Latest held: Q1 FY27 deck, dated
07-Aug-2026. FY26 deck, dated 25-May-2026, also held (B00).

**5. RESEARCH / RATING.** One rating document: India Ratings, IND
A-/Stable, dated 03-Dec-2025, image-only PDF, readable via poppler (B00).
No dedicated research-folder document. Two broker notes sit misfiled in
presentation/ (MNCL Q4 FY26 update; an unnamed third-party fundamental
report) and are treated as non-anchored leads only, not filed research
(B00).

**6. CORPORATE ACTIONS.** No filed Reg 30 announcement PDFs held (B00).
Some corporate-action-adjacent facts surface inside the AR notes
themselves: IPO proceeds utilisation (Note 53), a standalone-level
internal restructuring/amalgamation item, and Note 22(e) shareholder
movements (B02, B03). Director/KMP change announcements (CFO, Company
Secretary, board resignations, AGM voting) were sourced by Stage 8 via
live web, not from a held filing (B08).

**7. FRESHNESS PAIR CHECK.** B00 `freshness_verdict` = "FRESHNESS PAIRS
OK". All four defined pairs PASS: RESULTS->CONCALL (Q1 FY27 results has
its same-quarter concall); RATING BULLETIN->RATIONALE (the held rating
PDF carries the full Detailed Rationale, not a bulletin alone); SEBI
ORDER->ORDER TEXT (no SEBI order referenced in corpus, pair not
triggered); AR->LATEST AUDITED RESULTS (FY26 AR matches the latest
audited year). No failed pair (B00).

**8. VERDICT LINE.**

CORPUS GAPPED: prospectus (HIGH; findable-but-missing, expected source
BSE/SEBI SCORES/exchange archive of the Feb-2024 RHP/DRHP - the company is
listed and such a filing exists; its absence forces the entire backward
baseline and the promoter/group map onto the FY26 AR plus web-derived
material rather than filing-anchored pre-IPO data, B00/B03/B08);
announcements (MEDIUM; findable-missing, expected source BSE/NSE Reg 30
filings - no filed PDFs held, intent-and-action cross-checks run on
concall/AR evidence and operator-ferried leads instead, B00); shareholding
(MEDIUM; findable-missing, expected source BSE/NSE Reg 31(4) quarterly
pattern PDF - PARTIALLY narrowed by an AR note (Note 22(e), see Section 6
Q9) and by a non-anchored operator-ferried Screener series, but the filed
pattern PDF itself and any pledge percentage remain absent, B00/B02/B08);
research (LOW; ambiguous between findable-missing and plausibly-thin -
broker coverage evidently exists, given the two misfiled notes, but the
research/ folder itself is empty and no rating-agency or broker site
research was fetched into the corpus, B00). This verdict does not trigger
the CORPUS GAPPED-FRESHNESS cap, since no Freshness Pair Check pair
failed; the HIGH prospectus gap plus the MEDIUM announcements and
shareholding gaps still mean CORPUS CURRENT cannot be claimed.

---

## SECTION 2: MENTAL MODEL DECLARATION

### DRAFT - PENDING OPERATOR SIGN-OFF

This declaration is a transition thesis. It states where the business
starts and what it claims to become. It is not signed. It is not a
recommendation.

### PART A - THE FROM STATE (the anchor, not the model)

**A1. ARCHETYPE.** Entero's own revenue-stream mix is 99.22% "sale of
traded goods" (B04) - a trading/distribution business. It does not
cleanly match any single entry in the ARCHETYPE LIBRARY. B04 places it
closest to the Outsourcing-Partner archetype (client/principal
concentration, wallet share, capacity fill) adapted for distribution
logic, blended with roll-up/consolidator economics from the acquisition
programme (48 subsidiaries, 7 FY26 deals) (B04). B04 explicitly flags this
fit as imperfect and asks for an operator ruling before Mental Model
sign-off.

**A2. THE SIMPLE ANALOGY.** Entero buys medicines and medical devices in
bulk from manufacturers and moves them, through a network of warehouses,
to retail pharmacies and hospitals across India, earning a thin
percentage spread on each rupee of goods it moves (B04: business_type
"trading", pricing_power "price-taker", asset_intensity "light",
wc_intensity "high"). It grows mainly by buying up smaller regional
distributors and by adding a second product line, medical devices
(MedTech), that it hopes will carry a fatter spread than plain medicine
distribution (B04, B05). That is the business today: a low-margin,
high-working-capital, high-volume mover of other companies' products,
built by acquisition.

### PART B - THE TRANSITION (the model)

**B1. FROM to TO.** FROM: R1 COMMODITY PRICE-TAKER neighbourhood. Pricing
power is explicitly scored "price-taker" (B04); ROCE sits at 9.7-11.6%
across the two years it can be computed (FY25-FY26, B01), near the cost
of capital, sub-15%; the business ran cash-flow negative six years of
seven (FY20-FY25) before turning CFO-positive in FY26 (B01) - the volatile
cash description of R1, not the durable mid-teens ROCE of R2. TO (claimed):
R3 VALUE-ADDED / SPEC'D SUPPLIER neighbourhood. The claimed engine is a
mix shift toward MedTech distribution, where management describes
"commercial role" (demand-generation) contracts that earn better margin
terms than pure pharma fulfilment (B05), plus a stated organic
gross-margin/EBITDA-margin uplift from that mix (+70-90bps GM, +50-75bps
EBITDA, B05 guidance_note). Management's own longer-horizon claim (ROCE
25-30% within 3-4 years, B05) would actually land closer to R4; that gap
between the disclosed R3-level mechanism and an R4-level number claimed
in the same breath is itself a caution under the CLAUDE.md rung-jump base
rate (one rung per 2-3 years; a multi-rung leap needs extraordinary proof)
and is carried into B6 below.

**B2. THE ENGINE.** Two things must physically change. (1) Revenue mix:
MedTech must keep rising as a share of the whole, from ~15% toward a
management-guided ~20% over 2-3 years (B05), with FY27 MedTech
annualised revenue already stated to be tracking past Rs 1,000cr (B03
guidance table, "DELIVERED"). (2) Contract structure: a growing share of
volume must move from pure fulfilment (order-and-deliver) to a
"commercial role" where Entero also does demand generation for the
manufacturer, which B04/B05 describe as carrying a materially better
margin. Both are demand-side/mix-side changes; neither requires new
physical assets (B09: organic PP&E additions were only 2.4% of revenue in
FY26).

**B3. THE PROOF GATE.** The hard binary test Stage 11 FTTCP should apply:
consolidated EBITDA margin sustaining at or above 5.0% for at least two
consecutive quarters (FY27 guide 5.0%, already touched once in Q1 FY27 per
B05), WITH OCF-to-EBITDA conversion reaching the guided >=50% threshold in
the same window (B05 guidance). Both legs must hold together, because an
EBITDA-margin gain that does not convert to cash is consistent with the
receivables-outrunning-revenue pattern already flagged (B02), not with a
genuine margin-quality improvement. Until both fire together across two
quarters, the transition is guidance, not proof.

**B4. THE RECOGNITION GAP (open question, resolved at Stage 11).** Whether
the market has already priced the claimed MedTech-mix, commercial-role
transition into Entero's current multiple, or whether that re-rating has
not yet happened, is an open question this dossier does not answer. Stage
11's PE-gap read against the Section 1B destination multiple resolves it.
If the TO state is already reflected, the re-rating engine is spent and
only the underlying earnings growth remains as a return source; if it is
not yet reflected, the re-rating itself is still available. No number or
conclusion is stated here.

**B5. THE UGLINESS TEST.** Today's ugly optic is a cluster: goodwill at
~44% of consolidated net worth (B02), 40 of ~65 group subsidiaries
carrying an adverse or qualified CARO clause, overwhelmingly cash losses
(B02, B03), cumulative CFO of -Rs203cr against cumulative PAT of +Rs193cr
over FY20-FY26 (B01), and trade receivables growing 1.7x faster than
revenue (B02). Classification: provisionally ARTIFACT-OF-CLIMB, on the
reasoning that FY26 was explicitly the group's most acquisitive year (7
deals) inside a stated "land-grab" phase that management itself says is
now shifting to "integration and synergy realisation" for FY27 (B04), and
because FY26 was also the first CFO-positive year after six negative ones
(B01) - consistent with integration lag rather than a permanently broken
model. This classification is CONTESTED, not settled: the CARO-qualified
count (40 entities) is a single-year snapshot with no multi-year trend to
show it shrinking, and B03's own analyst note states plainly that whether
this population shrinks or stays static "determines the transition
posture more than any other number in this AR." Treat the classification
above as provisional pending at least one further AR cycle of the CARO
count.

**B6. THE TRANSITION FALSIFIER.** The transition thesis (not the whole
business) is falsified if: (a) the MedTech/commercial-role margin mix
fails to show up in the blended, audited gross margin over 2-3 sequential
quarters despite a rising claimed MedTech share (B04 first_deterioration
signal), or (b) the EBITDA margin regresses toward 4% on integration
costs or pricing pressure after having touched 5% (B05 kill_signal), or
(c) management's own guided ROCE 25-30% claim visibly requires skipping a
rung the quality ladder says takes 2-3 years per rung, without
extraordinary proof offered for the acceleration (CLAUDE.md rung-jump
rule). Any of these separately falsifies the climb, without necessarily
falsifying the underlying trading business.

### PART C - WHAT THE MODEL WATCHES (derived from the transition)

**C1. DOMINANT VARIABLES.**
1. MedTech revenue mix % and margin accretion - current state: guided
   ~15% rising to ~20% over 2-3 years, FY27 run-rate past Rs 1,000cr per
   management, unaudited (single Ind AS 108 segment, B04).
2. Consolidated EBITDA margin trajectory toward and past 5% - current
   state: 4.03% FY26 (delivered against guide), already 5.0% touched in Q1
   FY27 (B03, B05).
3. Network-reach reconciliation (retail pharmacies/hospitals/SKUs/
   districts) - current state: fell 28-36% Q4 FY26 -> Q1 FY27,
   unreconciled by management or any analyst (B05, B07).
4. CARO-qualified, cash-loss subsidiary count - current state: 40 of ~65
   group entities as of the FY26 CARO Annexure, no prior-year comparable
   count on the same basis (B02, B03).

**C2. WHAT THE MODEL REJECTS.** Precise TAM/SOM sizing debates are noise
here: B09 already finds the runway class STRONG (39.9x revenue headroom
against SAM, current SAM share only 2.5%) and finds the binding constraint
is working-capital financing (a ~Rs1,000-1,100cr incremental funding gap
by year 3), not market size (B09). The model also rejects chasing the
exact IPM (Indian Pharmaceutical Market) growth percentage debate in
isolation: peers cannot independently confirm or deny Entero's IPM
acceleration claim because none of the three available peers (MEDPLUS,
REDINGTON, RPTECH) operates in B2B pharma wholesale distribution (B06).
What matters is Entero's own outperformance multiple over whatever IPM
prints, not the absolute IPM number.

**C3. THE BUSINESS FALSIFIER.** Distinct from B6: the FROM business
itself (trading in manufacturer-authorised pharma and MedTech products)
is falsified if a material manufacturer principal withdraws or
renegotiates distribution authorisation, since 99.22% of revenue is
"sale of traded goods" contingent on that authorisation, with no
single-manufacturer concentration percentage disclosed to bound the risk
(B04 first_deterioration_signals, "Manufacturer principal loss/
de-authorisation"). The first observable signal would be organic
like-for-like revenue growth falling to at or below 1.0x IPM growth
(B04).

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

(Drafted per the shared five-question spec in prompts/13-synthesis-pipeline.md,
BUSINESS UNDERSTANDING NARRATIVE section. This is a Halt 1 draft; Stage 13
holds the final version.)

Entero moves medicines and medical devices from manufacturers to retail
pharmacies and hospitals across India (B04). Its main line, sale of
traded goods, is 99.22% of FY26 revenue; a smaller marketing-support fee
line, where manufacturers pay Entero to help generate demand, is 0.50%
(B04). Pharmacies and hospitals need this because no single pharmacy can
economically deal with hundreds of manufacturers directly; Entero holds
the inventory, credit relationships, and delivery network that make that
unnecessary (B04). Customers are retail pharmacies and hospitals, drawn
from a stated network of tens of thousands of pharmacy accounts and
thousands of hospital accounts across hundreds of districts, though the
exact current count is unreconciled (B05, B07; see Section 4 below).
Demand exists because India's pharmaceutical market grows on its own,
independent of Entero, tracked by IQVIA/AIOCD industry data that B09 names
as a downstream candidate (B09). Demand should grow because Entero
reports organic growth running above that industry rate, historically by
a multiple of around 1.4x to 1.9x, and because the industry itself is
shifting from unorganised to organised distribution, a formalisation
trend B09 proposes tracking through GST e-way-bill data (B09, B05).
Whether that outperformance multiple holds is itself a live question: it
has compressed from roughly 1.9x to roughly 1.4x for three straight
quarters, a trend management has not fully explained (B05). The
competitive advantage, where it exists, sits in scale and manufacturer
relationships plus an emerging data layer (Teqtic BI, Entero Direct) -
B07's Emerging Moat scan classifies this as MODEST overall (score 19),
with the network-reach moat itself under an unreconciled contraction the
same quarter warehouse count and margins both rose (B07). On the core
pharma distribution line, the run does not establish a durable pricing-
power moat; B04 scores pricing power "price-taker." On the MedTech line,
the claimed advantage (commercial-role, demand-generation contracts) is
management-narrated and not yet confirmed in an audited segment split, so
the run cannot yet say this line has a moat either, only that it claims
one (B04, B07).

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. VERTICALS FRAMED (one per dominant variable, Section 2 Part C1)

**Vertical 1 - MedTech mix and margin accretion.** The corpus establishes
that management guides MedTech toward ~20% of revenue over 2-3 years and
claims the FY27 >Rs1,000cr annualised run-rate is already reached, with a
promised gross-margin/EBITDA-margin uplift of 70-90bps/50-75bps (B05). It
cannot establish an audited Pharma-vs-MedTech split, because the FY26
financial statements report a single Ind AS 108 reportable segment (B04).
Deciding questions: (1) Does blended gross margin actually move as MedTech
mix rises, on a lag-adjusted basis? (2) Do the FY26 MedTech acquisitions
(Ace Cardiopathy, Bioaide, Anand Chemiceutics) show standalone
profitability, or do they still draw on goodwill headroom (B04)? (3) Will
a segment-level disclosure ever be given, or does management intend to
keep this single-segment indefinitely?

**Vertical 2 - EBITDA margin trajectory.** The corpus establishes FY26
EBITDA margin at 4.03% (delivered against a 4% guide) and FY27 guidance of
5.0%, already touched once in Q1 FY27 (B03, B05). It cannot establish
whether the touch is durable versus a one-quarter print, since only one
quarter of FY27 data exists in the corpus. Deciding questions: (1) Does
the margin hold at or above 5% for two or more consecutive quarters
(the B3 proof-gate test)? (2) Does OCF-to-EBITDA conversion reach the
guided >=50% in the same window, given a verifier-caught pattern of
management declining to disclose quarterly gross debt, net debt, and OCF
in Q1 FY27 (B12b)? (3) Is the margin gain price-mix (durable) or a
one-off cost item (not durable)?

**Vertical 3 - Network-reach reconciliation.** The corpus establishes a
28-36% fall across retail pharmacy, hospital, SKU, and district counts
between the Q4 FY26 and Q1 FY27 calls, in the same quarter warehouse
count rose (136->138) and margins hit records, with no management or
analyst reconciliation of scale (B05, B07). It cannot establish whether
this is deliberate low-margin-account pruning (management's only related
comment, a ~2.5% revenue-drag figure, does not obviously scale to match
the reach-count drop) or real customer/hospital attrition, nor whether it
is industry-wide, since the three available peers (MEDPLUS, RPTECH,
REDINGTON) operate in adjacent, not identical, industries and show no
comparable contraction over the same window (B06). Deciding questions:
(1) Does management give any reconciliation in the next concall? (2) Do
the metrics recover, stabilise, or keep falling in the next print? (3) Is
the metric-label shift ("retail pharmacies" to "retail customers")
noted by B12b itself informative of a reporting-basis change?

**Vertical 4 - CARO-qualified, cash-loss subsidiary population.** The
corpus establishes 40 of ~65 group subsidiaries carry an adverse or
qualified CARO clause in the FY26 Consolidated Auditor's Report, mostly
Clause xvii cash losses, a materially broader population than the 15
entities Note 54 shows with negative net worth or a loss (B02, B03). It
cannot establish a trend, since this is the first year this cross-check
has been run against the CARO Annexure in this corpus; there is no
prior-year comparable count. Deciding questions: (1) Does the count
shrink, stay static, or grow in the next AR's CARO Annexure? (2) Does
management ever address the population directly, beyond the single GS
Pharma example attributed to intercompany interest (B05)? (3) Is
distress concentrated in a specific acquisition vintage (older FY24/FY25
deals per B03) or spread evenly?

### 4b. CANDIDATE SIGNAL TABLE (from B09 Section 6, expanded; UNVERIFIED -
verification and tracker writes happen at Role 5.5 in claude.ai)

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| IQVIA/AIOCD Indian Pharmaceutical Market (IPM) MAT growth | Organic LFL growth converges to IPM (multiple falls to ~1.0x or below) despite a claimed IPM acceleration (B05 kill_signal) | Monthly | IQVIA India Pharmaceutical Market reports (B09) |
| NPPA/DPCO price notifications on NLEM SKUs | A new NLEM price cut lands on a high-volume Entero-carried SKU category and compresses blended gross margin sequentially | Event-driven | NPPA notifications (B09) |
| Apollo HealthCo / Keimed disclosures | Largest peer shows faster organised-sector consolidation pace than Entero's own SOM share-gain path, implying share loss rather than gain | Quarterly | Apollo Hospitals investor presentations/earnings calls (B09) |
| Hospital chain bed-count/capex expansion announcements | Hospital capex additions slow or reverse across Apollo/Max/Fortis/Manipal, undercutting the MedTech (cardiology/IVD/ortho) demand thesis | Quarterly | Apollo/Max/Fortis/Manipal investor releases (B09) |
| Domestic-formulation growth commentary from large manufacturers | Sun Pharma/Cipla/Alkem report domestic formulation deceleration that contradicts Entero's IPM-outperformance narrative | Quarterly | Sun Pharma/Cipla/Alkem quarterly earnings calls (B09; shared signal) |
| GST e-way bill/e-invoicing trade-volume data for pharma HSN codes | The unorganised-to-organised formalisation proxy stalls or reverses, undercutting the B09 SOM share-gain thesis | Monthly | GSTN/Ministry of Finance releases (B09) |

### 4c. FRAGILITY READ

- **variable_count:** 4 (the Section 2 Part C1 dominant variables: MedTech
  mix/margin, EBITDA margin trajectory, network-reach reconciliation,
  CARO-qualified subsidiary count).
- **verifiability_ratio:** 1 of 4 externally auditable in the strict sense
  (the CARO-qualified subsidiary count is an auditor-signed disclosure,
  B02/B03); the other 3 rest primarily on company disclosure or guidance
  (MedTech mix/margin is unaudited single-segment guidance, B04; EBITDA
  margin is audited at the whole-company level but not attributable to
  MedTech specifically; network-reach counts are concall/deck figures with
  no audit trail, B05/B07), each with a partial external-corroboration
  path through the Section 4b candidate signals.
- **single_point_failure:** Network-reach reconciliation. If the Q4->Q1
  contraction (28-36%) reflects real customer or hospital attrition
  rather than deliberate low-margin pruning, it undermines both the
  stated core network moat (B3 in the B07 scan) and the same distribution
  channel the MedTech mix-shift depends on to sell through, breaking two
  of the four dominant variables at once (B05, B07).
- **fragility_verdict:** FRAGILE. Three of four dominant variables are
  primarily company-narrated rather than independently auditable, one
  variable can break two others at once, and this sits alongside a
  separately weak read on both the backward Gate 0 scan, whose
  `classification` field reads "AVOID" (provisional, per B01's own analyst
  note), and the combined forward/backward Emerging Moat read, whose
  `combined_assessment` field independently also reads "AVOID" (B07), a
  credibility grade of B rather than A on management's own guidance
  record (B05), and a CONCERN promoter verdict carrying an unreconciled
  ~2x CEO-pay figure within the same audited AR (B08).

### 4d. RESEARCH BRIEF (live-web work the corpus cannot do; the claude.ai
work order)

1. Fetch the Entero Feb-2024 RHP/DRHP (BSE/SEBI SCORES/exchange archive) to
   close the HIGH prospectus gap and re-anchor the pre-IPO backward
   baseline (B00, B03).
2. Confirm the filed BSE/NSE quarterly shareholding pattern for the last
   twelve quarters, including the promoter pledge percentage, since the
   corpus carries only an AR note (Note 22(e)) and a non-anchored
   operator-ferried series (B00, B08).
3. Verify the CFO/Company Secretary/senior-executive/board-member
   resignation announcements (Sambit Mohanty, Kevin Daftary, Rajesh Dalal,
   CFO and CS changes) against filed BSE/NSE Reg 30 announcements, since
   Stage 8 sourced these via general web search, not a held filing (B08).
4. Verify the 19-Aug-2026 AGM voting results (the ~1/3 institutional
   opposition to both remuneration resolutions) against the filed
   scrutiniser's report, not the scanx.trade secondary source B08 used
   (B08).
5. Check counterparty/customer-health filings for organised retail pharmacy
   chains (referenced by name in concalls, e.g. MedPlus store counts) to
   test Entero's disintermediation-risk framing independently (B05, B06).
6. Pull the India Ratings full detailed rationale's historical FCF
   commentary against Entero's own FY26 OCF print to cross-check the
   "FCF positive from end-FY26" guidance referenced in B00's analyst note.
7. Search for any SEBI adjudication order, NCLT filing, or short-seller
   report naming Entero, Prabhat Agrawal, or Prem Sethi, to independently
   confirm B08's negative search result (no adverse legal/regulatory
   findings) (B08).
8. Obtain the third-party blog's Curever Pharma failed-venture narrative's
   primary source, or an alternative corroboration, since B08 flags this
   explanation as resting on a single unverified blog (B08).
9. Check IQVIA or AIOCD primary data directly for the claimed 7-9% to
   10-12% IPM growth acceleration, since none of the three available peers
   could independently confirm or deny it (B06, B09).
10. Confirm GLP-1 distribution share for any listed peer, to reconcile
    Entero's own internally inconsistent 10%-of-value versus 5%-of-value
    figures across calls (B05, B06).

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. Entero buys medicines and medical devices from manufacturers and sells
   them on to retail pharmacies and hospitals across India (B04).
2. Almost all its revenue, 99.22%, comes from this simple buy-and-resell
   line; a small slice comes from fees manufacturers pay it to help sell
   their products (B04).
3. It has grown fast partly by buying up smaller regional distributors,
   48 group subsidiaries and 7 deals in FY26 alone (B02, B04).
4. Its customers are retail pharmacies and hospitals; no single customer
   or manufacturer concentration figure is disclosed, so how spread out
   or concentrated that customer base really is cannot be confirmed from
   the corpus (B04).
5. Demand exists because India's medicine market grows on its own, and
   pharmacies need one partner instead of dealing with hundreds of
   manufacturers directly (B04, B09).
6. Demand should keep growing because the industry itself is shifting
   from small, unorganised distributors toward larger, organised ones,
   and Entero says it is growing faster than the industry average (B05,
   B09).
7. That "faster than industry" gap has been shrinking for three quarters
   in a row, and management has not fully explained why (B05).
8. Its moat, where it has one, is its size and its relationships with
   manufacturers, not pricing power; a scan built to find rising quality
   scored it MODEST, not strong (B04, B07).
9. Its newer medical-devices line is meant to carry better margins than
   plain medicine distribution, but no audited numbers separate the two
   lines yet (B04).
10. The corpus is a business built by acquisition, and roughly 40 of its
    roughly 65 subsidiaries carry an auditor-flagged caution, mostly for
    running at a cash loss (B02, B03).
11. The mental model here is a climb: from a low-margin, price-taking
    distributor toward a business with better-margin, higher-value
    medical-device distribution and demand-generation contracts, a climb
    that is claimed but not yet proven in audited numbers (Section 2).
12. Taken together, this is a fragile setup: most of the variables that
    would prove the climb rest on what management says rather than on
    audited or independently checkable numbers (Section 4c).
13. The corpus could not establish an audited split between the pharma
    and medical-devices businesses, and could not establish why the
    company's own reported customer, hospital, and SKU counts fell
    sharply in the latest quarter (B04, B05, B07).
14. The corpus could not establish a pre-listing (pre-2024) financial
    baseline, because no IPO prospectus document is held (B00, B03).
15. The two biggest open questions this dossier hands to Halt 1: is the
    latest quarter's network-reach drop a deliberate, healthy pruning of
    low-margin accounts, or a real loss of customers; and will the
    40-subsidiary cash-loss population shrink over the next annual
    report, or stay where it is (B05, B07, B03).

---

## SECTION 6: STANDING EXTRACTION ANNEX

### Q1. UNITS

No per-unit figure (realisation per tonne, revenue per case, price per
litre, ARPU) is printed anywhere in the corpus for Entero's distribution
business. This is a basket business: revenue is reported as a single
"sale of traded goods" line across an unspecified mix of pharma SKUs and
MedTech products, not per-unit (B04, AR Note 32, p.208). NOT DISCLOSED.
The nearest volume and revenue lines from which a rough throughput
measure could be derived: FY26 consolidated revenue Rs 6,591cr (B09), and
network-reach counts as management-narrated across the two most recent
concalls: "97,600 pharmacies / 3,000+ hospitals / 89,200 SKUs / 505
districts / 131 warehouses" as of the Q4 FY26 call, versus "72,000 retail
customers / 2,300 hospitals / 83,400 SKUs / 475 districts / 138
warehouses" as of the Q1 FY27 call (B05, Q4 FY26 call p.2 / Q1 FY27 call
p.3, per B05's red-flag anchor). Comment: dividing FY26 revenue by any of
these counts would give a crude "revenue per pharmacy account" style
figure, but no such figure is printed by the company itself, and the
denominator (the reach count) is itself unreconciled between quarters, so
any such derivation would compound two unresolved numbers. Better left
undone here; a question for management, not an extraction.

### Q2. SEGMENT CAPITAL AND DEBT

Quote (accounting policy/segment note): "Note 48 confirms single
reportable segment (trading of pharma/surgical products) so no
geographic or product disaggregation beyond 'Domestic'" (B02-notes-pass1,
paraphrasing Note 48, consolidated FS, near p.201; B04 separately cites
"single Ind AS 108 reportable segment (AR Note 3.19, p.195)"). Comment:
Entero reports one Ind AS 108 operating segment. There is no segment-level
assets, liabilities, capital employed, or borrowings breakdown by segment
(e.g. Pharma vs MedTech) in the corpus. Total (unallocated) borrowings:
Note 25 shows the group's leverage rising, with "adjusted net
debt-to-equity worsened 0.02x to 0.23x" per B02 Finding 6 (Note 25 p.205),
though B12a flags this "adjusted" basis as not independently traced to a
named methodology, and the AR's own Standalone Note 57 Ratio Analysis
(p.168, read directly this pass) prints Debt-Equity Ratio 0.06 (FY26) vs
"NA" (FY25) on a standalone short-term-plus-long-term-borrowings-over-
total-equity basis - a third, non-reconciled leverage figure alongside
the two B03 already named (gross D/E 0.17x->0.32x MD&A; net-of-cash D/E
-0.09x->0.15x Performance Highlights). NOT DISCLOSED: any borrowings
figure allocated specifically to a Pharma or MedTech segment; the total
consolidated borrowings figure is reported only at the whole-company
level.

### Q3. GUIDANCE VERSUS ASPIRATION

Every forward number named across the three concalls read at Stage 5,
classified:

(a) GUIDANCE WITH A PERIOD - "Revenue growth (like-for-like)... 30%...
FY26" (Q3 FY26 call, per B05 guidance table); "EBITDA margin... 4%...
FY26" (Q3 FY26 call); "Operating cash flow... ~Rs100cr... FY26" (Q3 FY26
call); "Revenue growth ex new M&A... 23% YoY... FY27" (Q4 FY26 call);
"EBITDA margin... 5%... FY27" (Q4 FY26 call); "EBITDA-to-OCF
conversion... >=50%... FY27" (Q4 FY26 call); "Tax rate... 22-23%...
FY27" (Q4 FY26 call); "Minority interest as % of PBT-minority... ~25-27%...
FY27" (Q4 FY26 call) (all per B05 guidance table, quarter and figure as
printed there).

(b) ASPIRATION WITHOUT A FIRM PERIOD - "MedTech share of revenue...
~15% rising to ~20%... 2-3 years" (Q4 FY26 call); "Organic growth ex
acquisitions... >20%... 3-4 years" (Q1 FY27 call); "ROCE... 25-30%...
3-4 years, ex further acquisitions" (Q1 FY27 call, "we should be able to
generate an ROCE of about 25% to 30%," B05). These carry a stated horizon
window (2-3 or 3-4 years) but not a specific fiscal-year figure, closer
to aspiration than firm guidance.

(c) CAPACITY/CAPABILITY ONLY - "Acquisition valuation multiple... 5-7x
EV/EBITDA... standing policy" (Q4 FY26 call, B05) - a stated internal
discipline, not a forward outcome commitment. MedTech annualised revenue
">Rs1,000cr" was originally forward guidance (Q3 FY26 call) but B05's
promise-delivery table marks it "delivered" by the Q4 FY26 call, so it
has moved from category (a) to a confirmed outcome, on management's own
(unaudited, single-segment) telling.

### Q4. CONCENTRATION

Product concentration: NOT DISCLOSED. "No single customer concentration
>10% disclosed (none required/given in Note 15 or Note 48 segment note)"
(B02-notes-pass1, p.201/consolidated segment note). Customer
concentration: NOT DISCLOSED, same source; B04 independently confirms
"no single customer concentration figure disclosed — NOT FOUND." Top
product share: NOT DISCLOSED - the single Ind AS 108 segment precludes any
product-line disaggregation. Geography concentration: DISCLOSED as fully
domestic - "caters mainly to the Indian market... not materially exposed
to Foreign Currency Risk" (Note 3.15/50(C)(i), per B02-notes-pass1) and
Note 48's segment disaggregation runs only to "Domestic," with no
international split given because there evidently is none. Top-3
industry concentration (a different, market-level figure, not
Entero-specific): "~8-10% combined (FY23, CRISIL), rising toward 20-30%
by FY28" (B09, TAM report, CRISIL-sourced).

### Q5. PROMISE LEDGER

| Promised in | Promise | Delivery status | Evidence anchor |
|---|---|---|---|
| Q3 FY26 call | FY26 revenue growth 30% like-for-like | Delivered (31.5% LFL) | Q4 FY26 call (B05) |
| Q3 FY26 call | FY26 EBITDA margin 4% | Delivered (4.0%, +67bps YoY) | AR p.31 (B05) |
| Q3 FY26 call | FY26 OCF ~Rs100cr | Partial (Rs96.2cr, ~96% of guide) | AR (B05) |
| Q3 FY26 call | MedTech annualised revenue >Rs1,000cr | Delivered (confirmed Q4 FY26 call, reaffirmed Q1 FY27) | Q4 FY26 call p.4; Q1 FY27 call p.3 (B05) |
| Q3 FY26 call | FY27 guidance to be given "in Q4 conference call" | Delivered | Q4 FY26 call p.4 (B05) |
| Q3 FY26 call | M&A pause for "next 2-3 quarters" | Partial (extended through all of FY27) | Q4 FY26 / Q1 FY27 calls (B05) |
| Q3 FY26 call | NWC days moving toward 60 | Delivered (59 days Q4 FY26) | FY26 Deck slide 11 (B05) |
| Q3 FY26 call | Tax losses fully utilised "maybe by next year," ~18% FY26 rate | Delivered (FY27 rate guided 22-23%) | Q4 FY26 call p.6 (B05) |
| Q4 FY26 call | FY27: 23% revenue ex-M&A, 5% EBITDA margin, >=50% OCF conversion | Partial (EBITDA margin already 5.0% in Q1 FY27; other two not yet full-year assessable) | Q1 FY27 call (B05) |
| Q4 FY26 call | Minority interest normalise to ~25-27% of PBT-minority | Delivered (~27% Q1 FY27) | Q1 FY27 call (B05) |
| Q4 FY26 call | Depreciation stays at Q4 FY26 level absent new capex | Delivered ("What you're seeing in Q1 is what you will see broadly going forward," Balakrishnan Kaushik, Q1 FY27 call) | Q1 FY27 call (B05) |
| Q4 FY26 call | Interest cost stable near-term then decline | Partial (stability confirmed, "broadly in the same range"; decline not yet visible) | Q1 FY27 call (B05) |

Overall: 8 delivered, 4 partial, 0 missed (B05). Credibility grade: B,
"held to B, not A, by a refusal to disclose receivables aging and an
unaddressed contraction in network-reach metrics" (B05).

### Q6. RESTATED BASES

"No restatement of prior-year figures for error correction found" (B02).
Note 23 (Statement of Changes in Equity) carries recurring "Impact due to
common control business combination" adjustments taken directly to
retained earnings under the Ind AS pooling-of-interest treatment for
common-control combinations: "+Rs19.75M FY25, -Rs297.32M FY26" (B02, Note
23, p.184/204). This is explicitly not an error restatement, but a
recurring policy-driven adjustment; comment: it means year-over-year
retained-earnings comparisons are not on a fully like-for-like basis
without adjusting for this line each year.

### Q7. CORPORATE-ACTION CLAUSES

The corpus's own Standalone Note 58 ("Other Statutory Information"), read
directly this pass at AR p.169, item (ix) "Compliance with approved
scheme(s) of arrangements," states verbatim: "The company has not entered
into any scheme of arrangement which has an accounting impact on current
or previous financial year." This appears to CONTRADICT the internal
restructuring/amalgamation item that stage report 02-notes-pass1 earlier
attributed to "STANDALONE Note 58" (transfer of two wholly-owned
subsidiaries, CPDPL and CPD Pharma, into a third wholly-owned subsidiary,
Rada Medisolutions, for Rs100,000, followed by an MCA-approved
amalgamation confirmed by a regional-director order dated 17-Apr-2026,
appointed date 15-Apr-2025). Flagging this discrepancy rather than
resolving it: either the item sits in a different note than B02 cited, or
its accounting impact was judged (by the company) to fall in FY27, not
FY26, which would make the FY26 Note 58(ix) statement technically
consistent. NOT independently re-located in this pass; a verification
item for the operator (or Role 5.5) to close by locating the exact note
and page. No merger, preferential issue, or buyback scheme with a
current-year accounting impact is otherwise disclosed in the corpus: "no
bonus issue, no buyback in the last 5 years" (Note 22g/h, B02-notes-pass1).

Related, and separately confirmed this pass by direct PDF read: Standalone
Note 55A (p.165) prints, for Curever Pharma Private Limited, a loan
"Balance as at 31 March 2025" of Rs364.69 lakh-equivalent (stated as
364.69 in the table's units) fully offset by a "Less: Impairment loss
accounted [Refer Note 9 and 39B]" line of (364.69), net balance nil -
independently confirming B02/B08's flagged Rs364.69M loan write-off with
no accompanying explanatory note printed alongside the table itself.

### Q8. RELATED-PARTY PERIMETER

The AR's Standalone Notes (p.165-166, read directly this pass) print two
related-party tables relevant here. Loans given to subsidiaries (Note
55A-adjacent table, "Purpose of Loans granted: The Loan has been provided
for general working capital and other long term purposes"): 32 named
subsidiary entities, "Total" balance as at 31-Mar-2025 of Rs8,925.86 (in
the table's stated units), less "Impairment loss accounted" of (364.69)
against Curever Pharma Private Limited specifically, net Rs8,561.17.
Corporate guarantees given by the Company: 26 named subsidiary entities,
"Total" Rs6,327.00 (31-Mar-2026) versus Rs4,657.00 (31-Mar-2025). Both
tables list entities including Atreja Healthcare Solutions, Avenir
Lifecare Pharma, Avenues Pharma Distributors, Curever Pharma, Dhanvanthri
Super Speciality, Novacare Healthcare Solutions, Sri Rama Pharmaceutical
Distributors, and Ace Cardiopathy Solutions, among others (full list as
printed, p.165-166). Beyond the subsidiary population, the AR's KMP/
promoter-adjacent RPT items already surfaced by earlier stages: CEO
(Prabhat Agrawal) remuneration disclosed as Rs47.27M (CG Report p.63) vs
Rs94.50M (Ind AS 24 KMP note, p.235-236), unreconciled (B08); the Rs
364.69M plus Rs95.82M interest Curever Pharma loan waiver (Note 55A,
p.164, B02); a new Rs1,160.84M Optionally Convertible Debenture
investment across 6 unnamed subsidiaries (Note 50B, B02). Comment: the
subsidiary population transacting with the parent is large (30+ named
entities across the two tables) and structurally central to the roll-up,
consistent with B02's RPT-fairness score of 5/10.

### Q9. PLEDGE AND SHAREHOLDING

Twelve-quarter filed shareholding pattern: ABSENT from the corpus (no
BSE/NSE Reg 31 quarterly PDF held, B00). What the corpus does carry, from
the AR's Note 22(e) (Consolidated FS, p.203, quoted per B02-notes-pass2):
"Prasid Uno Family Trust: 69,50,320 shares (15.97%) at 31-Mar-2025 ->
45,50,320 shares (10.46%) at 31-Mar-2026" - a non-promoter holder,
separately noted as having "declared the beneficial ownership in form no.
BEN-1"; "Invesco India Aggressive Hybrid Fund: 24,89,513 shares (5.72%)
at 31-Mar-2025 -> 0 shares / 0.00% at 31-Mar-2026"; "Smallcap World Fund,
Inc: 23,58,555 shares (5.42%) at 31-Mar-2025 -> 0 shares / 0.00% at
31-Mar-2026"; and the three named promoters "Prabhat Agrawal 9.26%, Prem
Sethi 5.15%, Orbimed Asia III Mauritius Ltd 38.01%... 0.00% change YoY."
Institutional holding latest: not given as a single filed aggregate in
the corpus; the AR note only shows named >5% holders as above. Promoter
pledge: NOT DISCLOSED IN CORPUS via any filed shareholding-pattern PDF.
B08 (stage 8, web-sourced, not corpus-anchored) reports zero promoter
pledge formally declared for FY26 under Reg 31(4) - this is explicitly a
non-anchored, declaration-based finding, not a filing held in this
corpus, and should be treated accordingly. A separate, non-anchored
operator-ferried Screener series (work/operator-ferried-2026-08-29.md)
narrates FII 23.3%->4.36% and DII 2.3%->15.48% (Mar-24 to Jun-26); this
is NOT filing-anchored and is cited here only as a leads pointer, not as
corpus evidence.

### Q10. VERIFICATION

Documents quoted in this annex, filename and date: FY26 Annual Report,
Entero Healthcare Solutions Limited (year ended 31-Mar-2026), filed
2026-07-27, 276 printed pages
(inputs/annual-report/1ee92e80-ec9c-45f5-ae7d-a2809837e81b.pdf), pages
165-170 read directly this pass for Notes 55A, 56, 57, 58; Q3 FY26 call
transcript, dated 12-Feb-2026 (inputs/concalls/Concall_Feb_2026_
Transcript.pdf); Q4 FY26 call transcript, dated Jun-2026
(inputs/concalls/Concall_Jun_2026_Transcript.pdf); Q1 FY27 call
transcript, dated 17-Aug-2026 (inputs/concalls/808d85fd-f6c7-4f4a-98d3-
f57a32a6e78f.pdf); plus stage reports 02-notes.md, 02-notes-pass1.md,
02-notes-pass2.md, 03-ardeep.md, 04-bizmodel.md, 05-concall.md,
08-promoter.md, 09-tam.md (runs/entero-2026-07-27/outputs/reports/), all
dated to this run, 2026-07-27.

CORPUS COMMIT HASH: 7043fdb9360cc115f1bf6125e5cd77301e26a467
