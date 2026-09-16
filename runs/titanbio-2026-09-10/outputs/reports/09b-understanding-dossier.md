# HALT 1 UNDERSTANDING DOSSIER — TITANBIO (Titan Biotech Ltd)

Run: runs/titanbio-2026-09-10 | Phase 1 | 2026-09-16 | Stage: B09b-dossier
Assembled from committed blocks B00-B09, verifier blocks B12a-B12d, confidence.yaml,
and the phase-1 final files. No web search. No re-analysis. No valuation, price, or
verdict vocabulary except the one scoped exception at Part B4 below.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

1. **CONCALLS.** None held. B00 records `concalls_available: false`; Titan Biotech
   holds no earnings calls in the corpus or, per B00's declaration, in fact (B00
   input_gaps: "concalls: NONE. Titan Biotech holds no earnings calls"). Stage 5 ran
   in NO-CONCALL MODE against annual report prose instead (B05). Eleven peer
   transcripts are held (ADVENZYMES 4, FERMENTA 4, VIDHIING 3), the most recent being
   ADVENZYMES Q1 FY27, 12-Aug-2026. Given the run date of 2026-09-16 and that Titan
   itself never publishes a transcript, no "more recent quarter's transcript" is
   plausibly missing; the absence is declared, not accidental.
2. **ANNUAL REPORTS.** Three years held: AR_FY2026.pdf (FY2025-26, 201 pages),
   AR_FY2025.pdf (FY2024-25, 195 pages), AR_FY2024.pdf (FY2023-24, 200 pages). The
   latest completed FY (FY2025-26) is present. Three years clears the minimum.
3. **RESULTS FILINGS.** Latest is the Q1 FY27 unaudited filing, dated 2026-08-13
   (quarter ended 30-Jun-2026). The three most recent per B00 are Q1 FY27
   (13-Aug-2026), FY26 audited (30-May-2026) and Q3 FY26 (12-Feb-2026); Q2 FY26
   (11-Nov-2025) is held as a fourth, additional filing. No quarter-gap exists
   between the latest results filing (Q1 FY27) and the latest AR (FY2025-26): Q1
   FY27 is simply the newest data point beyond the AR's year-end.
4. **INVESTOR PRESENTATIONS.** ABSENT. B00 input_gaps: "presentation: NONE. The
   company publishes no investor presentation." Zero held, zero expected on this
   evidence; not a findable-but-missing gap.
5. **RESEARCH / RATING.** ABSENT, both. B00: "rating: NONE. No credit rating
   document exists on screener or in BSE announcements for scrip 524717." B00:
   "research: NONE. No broker notes." The company is near debt-free (borrowings
   Rs 5.71 cr including leases, B01/B03), which is itself relevant context for why
   no rating may exist, but its absence is still a gap for the record.
6. **CORPORATE ACTIONS.** Eight Reg 30 filings held, 13-Feb-2025 to 05-Sep-2026:
   integrated filing (13-Feb-2025), arbitration update (28-Feb-2025), arbitration
   notice received (24-Jul-2025), arbitration legal notice (25-Jul-2025), change in
   management (27-Sep-2025), share split board outcome (29-Nov-2025), bonus issue
   board outcome (03-Sep-2026), AR weblink intimation (05-Sep-2026). One filename
   flag: the document filed as "2025-02-28 arbitration update" is, on direct read,
   NOT an arbitration update; its content is an intimation that Titan's voting
   rights in Titan Media Limited rose to 48.44% from 32.29% on payment of a call on
   partly-paid shares (see Section 6, Q7). No genuine follow-up filing on the
   NGenious Solutions arbitration exists in the corpus after the 24/25-Jul-2025
   notices (confirmed independently at Section 6, Q7).
7. **FRESHNESS PAIR CHECK.** B00 `freshness_verdict`: FRESHNESS PAIRS OK. All four
   pairs PASS or correctly SKIP; none FAILED.
   - RESULTS to CONCALL: SKIPPED. `concalls_available` is false; the absence is
     declared, not accidental, so no mate is expected.
   - RATING BULLETIN to RATIONALE: PASS. No bulletin exists to trigger the pair.
   - SEBI ORDER to ORDER TEXT: PASS. No SEBI order is referenced in any collected
     filing.
   - AR to LATEST AUDITED ANNUAL RESULTS: PASS. The FY2025-26 AR is held against
     the 30-May-2026 FY26 audited results filing.
8. **VERDICT LINE: CORPUS GAPPED.**
   - No investor presentation — expected source: company IR page — kind:
     plausibly-nonexistent (B00 states the company publishes none).
   - No credit rating or rating rationale — expected source: rating agency site /
     BSE announcements — kind: plausibly-nonexistent (near debt-free company, no
     rating mandate evident; still a data point, not itself adverse).
   - No broker/research note — expected source: BSE / broker research site —
     kind: plausibly-nonexistent (a thinly-covered micro-cap).
   - No BSE shareholding-pattern (XBRL) filing in the corpus — expected source:
     BSE — kind: findable-but-missing (B00: "The BSE shareholding XBRL API did not
     serve"; the AR's own Corporate Governance Report carries a two-year
     shareholding table as a partial substitute, see Section 6 Q9).
   - No product-wise or plant-wise segment mix — expected source: company filing
     — kind: plausibly-nonexistent (one reportable segment under Ind AS 108 for
     three years running, AR FY26 Note 38A, p.142).
   - No capacity, utilisation or commissioning-date disclosure for any of the four
     plants — expected source: company filing / investor presentation — kind:
     plausibly-nonexistent (never disclosed in three annual reports; contrasts
     with every one of the three peers, which each disclose a utilisation
     percentage, per B06).
   - No concall transcripts — expected source: company IR page / BSE — kind:
     plausibly-nonexistent (declared absence, not a findable-but-missing gap).
   This is CORPUS GAPPED, not CORPUS GAPPED-FRESHNESS: no freshness pair failed, so
   the freshness cap on the gate recommendation does not apply from this dossier's
   side (the REWORK verdict already in force, see Section 2 headnote, is driven by
   confidence delta, not by this freshness check).

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT - PENDING OPERATOR SIGN-OFF.** Nothing below is signed. The operator signs
or rewrites this in claude.ai after live-web stress-testing; this dossier only
assembles the case from the committed evidence.

### PART A — THE FROM STATE

**A1. Archetype.** Single business line (one reportable segment, Ind AS 108, AR
FY26 Note 38A, p.142; B00, B04). Archetype: **Commodity converter** (Section 1B
v3.7 Amendment 17 binds), per Stage 4's own classification: business_type
"manufacturing", pricing_power "weak", cyclicality "cyclical", moats_present: []
(B04). Stage 4's one-line verdict names it directly: "Commodity converter with a
flat cost margin, a related-party-heavy supply chain, and a FY26/FY27 rebound not
yet proven to be a durable value-added climb" (B04).

**A2. The simple analogy.** Titan Biotech buys animal and plant protein, ferments
or extracts it, and sells the output as a raw material to other manufacturers: a
peptone that feeds a fermentation tank, a bottle of prepared culture media that
grows bacteria on a lab plate, a collagen peptide that goes into someone else's
supplement or cosmetic, an ox-bile extract that goes into someone else's
diagnostic kit. Titan does not sell a finished, branded product to a consumer. It
sells an input, priced mostly on cost of its own raw material (48.1% of revenue
in FY26, flat versus 48.3% in FY25, B04), to industrial buyers who are themselves
named only as classes (pharma, biotech, diagnostics, nutraceutical, food,
cosmetics, veterinary, agri-input) and never as companies (B04). Sixty-one
percent of FY26 revenue was domestic, thirty-nine percent export (AR FY26 Note
38, p.142). That is where the arrow starts.

### PART B — THE TRANSITION

**B1. FROM to TO.** One line (the single reportable segment).
- **FROM: R1 COMMODITY PRICE-TAKER.** Evidence: pricing power scored "weak" by
  Stage 4 (B04); zero moats present (B04 moats_present: []); gross margin 12.7
  percentage points below the peer median, one of only two clean adverse moat
  findings (B01 M9); a deceleration from a 21.92% three-year revenue CAGR to
  11.65% (B01 M11); raw-material price pass-through named as the company's own
  top risk in every one of three annual reports (B04). Note the ROCE headline
  (standalone 24.09%, consolidated 22.76%, B04 irrelevant_ratios) reads well above
  a classic R1 band; the run itself flags why that number should not be trusted
  at face value for a CONVERTER-classified name: capital employed includes a Rs
  49.66 cr FVTPL investment book earning only 3.64% return, inflating the
  apparent operating return (B04 irrelevant_ratios; per CLAUDE.md's own binding
  rule against feeding spot-year ROCE for a converter into destination-multiple
  work). Stripped of that distortion, the qualitative record (margin-taker, not
  margin-setter, per B01's own analyst note) is the more load-bearing signal, and
  it reads R1, not higher.
- **TO (CLAIMED, not delivered): R3 VALUE-ADDED / SPEC'D SUPPLIER.** The implicit
  claim embedded in the FY26/FY27 export acceleration (+49.0% to Rs 80.33 cr, 39%
  of revenue, versus +22.7% domestic; AR FY26 Note 38, p.141-142) and in
  management's own aspiration to diversify into health-supplement products (AR
  FY26 Directors' Report, Future Plans, p.71) is a climb toward regulated,
  qualified export customers whose switching costs would give Titan partial
  pricing power, the R3 signature. This is a CLAIM, not a finding: the Emerging
  Moat scan returns 2.0/92, classification NONE, with export growth (E2) as the
  only live category and the one the company's own filings never explain
  causally (B07).

**B2. The engine.** Two things would have to physically change to move FROM to
TO. First, the customer mix inside the export line would need to shift from
commodity-grade, price-driven buyers toward regulated, qualified buyers (pharma,
diagnostics) who pay for consistency and cannot easily re-qualify a new
supplier — the switching-cost mechanism the peer set describes (VIDHIING: a
four-to-ten-year customer approval cycle for a comparable regulated ingredient,
B06 verified claim). Second, that mix shift should show up mechanically as the
cost-of-materials-consumed ratio falling as a share of revenue, because
higher-value, qualified-customer volume should carry better realisation per unit
of input cost — this is the exact signature the peer set shows when margin
expands on better mix, and it is the signature Titan's FY26 numbers do NOT show
(B06 analyst_note: "Titan's flat 48% raw-material ratio alongside rising OPM does
not match the mix-driven margin signature... this peer set shows when margin
expands"). The engine, in other words, has not yet visibly turned.

**B3. The proof gate.** Cost of materials consumed as a percentage of revenue
must fall below the FY26 floor of 48.1% for two consecutive quarters while
like-for-like revenue growth (ex the freight gross-up, B01 FLAG-REVENUE-BASIS)
holds at or above high single digits. This is the hard binary this dossier can
state from corpus: B04's own must-track metric names the direction ("Cost of
materials consumed / revenue: healthy = flat or falling, red flag = rising
quarter over quarter"), and the gate-recommendation's own falsification line
inverts it into a kill test ("Q2 FY27 revenue growth below 8 percent year on
year... with cost of materials consumed holding at or above 48 percent of
revenue," gate-recommendation.md). Until the ratio moves, the climb is
narrative.

**B4. The recognition gap.** OPEN QUESTION, not resolved here. Whether the
market has already priced an assumed export-led, value-add climb into Titan's
current multiple is a question this dossier does not answer. Stage 11 resolves
it via the PE gap once a destination multiple is derived under Section 1B,
including the Amendment 17 converter cap that binds this archetype. If the TO
state (R3) is already priced, the re-rating component of any future return is
already spent and only the underlying earnings growth would remain; if it is
not priced, an unresolved climb still carries a re-rating component. This
dossier states no number and no conclusion on which is true.

**B5. The ugliness test.** Classification: **STRUCTURAL-FEATURE.** The ugly
optic is the working-capital level, not a single bad quarter. The evidence that
separates the two readings: corrected working-capital days ran 130.85 (FY23),
135.39 (FY24), 150.05 (FY25) and 127.67 (FY26), a net decrease of only 3.18 days
across four years, and the level PEAKED in FY25, the year revenue FELL 5.7%, not
in a growth year (B01, corrected this run; gate-recommendation.md FLAG-CASH).
Heavy working capital present when growth is absent is a feature of the
business, not a byproduct of the current growth spurt. Finished-goods inventory
rose 53.2% against 31.8% revenue growth, the company booked its first-ever
expected-credit-loss provision (Rs 36.26 lakh, nil in FY24/FY25), and
receivables aged past six months rose from 7.6% to 8.4% of the gross book (B02;
AR FY26 Notes 8/9, p.129-130). This sits alongside, and is a separate finding
from, genuinely sound profit-to-cash conversion (CFO/PAT above 1.0x in both FY26
and FY25, B01/B03).

**B6. The transition falsifier** (kills the climb, not the business). Any of:
(a) the cost-of-materials ratio holding flat or rising for two more quarters
while like-for-like growth reverts toward the FY25 flat/declining pattern once
the freight-driven base effect laps (gate-recommendation.md falsification
line); (b) the export growth (E2, the scan's only live category) proving to be
a single-customer restock rather than a broadening, qualified base, per the
optionality register's own stated convertor test ("growth sustains 2-4 quarters
ex freight gross-up," B07 optionality_register); or (c) Advanced Enzyme and
Vidhi's currently-contradicted, industry-wide demand deceleration (B06
"contradicted" findings) persisting through FY27, removing any industry
tailwind explanation for Titan's FY26 rebound.

### PART C — WHAT THE MODEL WATCHES

**C1. Dominant variables** (derived from the engine and the proof gate):
1. **Cost of materials consumed / revenue.** Current state: flat, 48.1% FY26 vs
   48.3% FY25 (B04). The single most direct mix-climb tell.
2. **Export revenue share and its cause.** Current state: 39% of FY26 revenue,
   +49.0% YoY, no customer, country, certification or product named in any
   filing (AR FY26 Note 38, p.141-142; B07 FLAG-NO-CAUSAL-EXPORT-STORY).
3. **Related-party share of raw-material cost.** Current state: 39.1% of cost of
   materials consumed, Rs 3,877.14 lakh, audited (AR FY26 Note 41(a); this
   figure replaces the Rs 3,683.61 lakh / 37.1% carried in B02/B03/B04, see
   Section 4a below); Phoenix Bio Sciences alone 26.0% of the bill, +73.6% YoY,
   with two serving Executive Directors on its board (B08).
4. **Net PPE additions versus net FVTPL/financial-asset additions.** Current
   state: gross PPE additions fell three years running (Rs 1,948.49 lakh FY24 to
   Rs 936.88 lakh FY25 to Rs 740.08 lakh FY26) while 77% of the FY26 investing
   outflow (Rs 25.16 cr of Rs 32.55 cr audited) went into a quoted-debt FVTPL
   portfolio whose own return fell from 7.04% to 3.64% (B07
   FLAG-CAPEX-CLAIM-CONTRADICTED).

**C2. What the model rejects.**
- The size of the addressable market. TAM/SAM sizing (Rs 5,040-6,660 cr,
  9% growth, 21.65x revenue headroom, runway class GOOD, B09) is not the
  binding constraint; execution and proof of the mix climb are.
- The health-supplement diversification claim as a near-term driver. Identical
  or near-identical language has run for three straight annual reports with no
  product named, no launch date, no revenue (B05, B07 FLAG-HEALTH-SUPPLEMENT-STALE).
  It is noise until a product is named.
- The headline 31.8% FY26 revenue growth figure as the test metric. It carries
  an unrestated freight gross-up; like-for-like growth is closer to 28% (B01
  FLAG-REVENUE-BASIS). The model watches the like-for-like number, not the
  reported one.

**C3. The business falsifier** (kills the FROM business itself, distinct from
B6). Cost of materials consumed rising past roughly 50% of revenue for two
consecutive years, combined with a disruption, renegotiation, or independently
evidenced above-market pricing at Phoenix Bio Sciences (26.0% of the FY26
raw-material bill, no arm's-length benchmark disclosed in three years of
filings, two serving Executive Directors on its board, B08) would force a
re-declaration of the FROM business itself. A converter that cannot pass
through input costs and depends on a single related-party supplier for over a
quarter of its raw material is not a stable, cash-generative converter; it is a
margin-and-supply-fragile one, a different and worse starting point than R1 as
declared above (B04 must_track_metrics; B08 adverse_findings).

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

*(Drafted per the shared spec at prompts/13-synthesis-pipeline.md, BUSINESS
UNDERSTANDING NARRATIVE section, answering the five questions in order, from
B03/B04/B06/B07/B09. Stage 13's copy is the final version.)*

Titan Biotech ferments and extracts animal and plant protein into biological
ingredients: peptones, biological extracts and yeast, prepared culture media
sold under the TM Media brand, collagen peptides, ox bile extract, animal
nutrition ingredients and plant growth promoters (B04). A peptone is the
digested protein that feeds a fermentation batch or a diagnostic culture
plate, and a customer who has qualified one supplier's grade carries the cost
of revalidating everything built on that grade if it changes, which is why
these are not easily substitutable inputs once a buyer has qualified one (B04,
B06). The company reports one segment and gives no product-wise revenue split
in three years of filings, so the only division the record carries is
geographic: 61% domestic, 39% export in FY26 (B04). Customers are named only
as classes, never as companies: pharma, biotech, nutraceutical, food and
beverage, diagnostics, cosmetics, veterinary and agriculture (B04); no top-five
or top-ten concentration figure exists anywhere, and the company names
customer concentration as a risk without a number attached to it (B04). On
switching costs the filings are silent, so the only evidence in the run comes
from peers: Vidhi Specialty describes a four-to-ten-year customer approval
cycle for a comparable regulated ingredient, and Advanced Enzyme ties its own
registration timelines to the same pattern (B06). Present demand sits with
those classes and is checkable only from outside the company, through the
downstream signals B09 names by name: HiMedia Laboratories' revenue
disclosures for the culture-media segment, peer quarterly results from
Advanced Enzyme, Fermenta, Vidhi and Nitta Gelatin, and DGCIS export
trade data by HS code for peptones, culture media and collagen (B09). The
forward drivers are a market sized at Rs 5,040-6,660 cr, growing about 9% a
year, of which Titan holds 4.62% of the addressable slice (B09); the
externally verifiable signals for those drivers are the DGCIS monthly export
series, US tariff and HS-code notifications from USTR and the Ministry of
Commerce, and Department of Biotechnology / BIRAC policy announcements that
test the company's own stated government-support claim (B09). Competitive
advantage cannot be located per line, because the company publishes no
line-level revenue at all (B04). On the whole-company view, the Emerging Moat
scan scored 2.0 out of 92 and classified the forward signal NONE, with one
live category, export growth, that the company's own filings never explain
causally (B07). Three categories carry documented ADVERSE evidence rather than
absent evidence: the contradicted capacity-building claim, the repeated
capex-framing sentence, and a working-capital series that does not genuinely
improve (B07). Categories 21 and 22 were scored and both returned zero (B07).
The backward moat block scored 14 out of 60, two moat tests confirmed of
twelve, and the two clean adverse findings are a gross margin 12.7 points below
the peer median and a deceleration from 21.92% to 11.65% three-year revenue
CAGR (B01). Stated plainly: no business line shows an evidenced moat in the
filed record, and the culture-media line competes with HiMedia Laboratories,
an unlisted peer roughly five times Titan's size on the available revenue
estimates (B09).

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. Verticals framed

**Vertical 1 — Cost of materials consumed / revenue.** What the corpus
establishes: the ratio was 48.1% in FY26 versus 48.3% in FY25, essentially flat
despite 31.8% reported revenue growth (B04). What it cannot establish: whether
the flatness reflects a genuinely stable input-cost environment, a
related-party pricing choice (Vertical 3), or simply insufficient time for a
mix shift to show up. Questions that decide it: (1) does the ratio move in
either direction over the next two-to-four quarters as exports keep growing;
(2) do peers report a comparable ratio direction for the same period (B06);
(3) is any part of the flatness attributable to related-party input pricing
rather than an open-market cost trend (see Vertical 3)?

**Vertical 2 — Export revenue share and cause.** What the corpus establishes:
exports rose 49.0% to Rs 80.33 cr, 39% of FY26 revenue, against 22.7% domestic
growth (AR FY26 Note 38, p.141-142). What it cannot establish: which country,
customer, product or certification drove the increase; no filing names any of
the four (B07 FLAG-NO-CAUSAL-EXPORT-STORY). Questions that decide it: (1) does
DGCIS HS-code trade data show a broadening country/customer base or a
concentrated single-buyer pattern; (2) does the growth sustain for 2-4 more
quarters once the freight-gross-up base effect laps (B07 optionality
register); (3) do peers' own demand commentary (currently contradicting an
industry-wide re-acceleration, B06) offer any explanation compatible with
Titan's idiosyncratic growth?

**Vertical 3 — Related-party share of raw-material cost.** What the corpus
establishes: 39.1% of cost of materials consumed, Rs 3,877.14 lakh, audited
(AR FY26 Note 41(a)), Phoenix Bio Sciences alone 26.0% and +73.6% YoY, with two
serving Executive Directors on Phoenix's board and no arm's-length pricing
benchmark disclosed in three years (B08). What it cannot establish: whether the
pricing is at, above, or below an arm's-length market rate; the corpus holds no
independent MCA/RoC record for Phoenix (B08 input_gaps). Questions that decide
it: (1) does Phoenix Bio Sciences' own MCA/RoC filing or a rating rationale, if
one exists, show a margin on sales to Titan consistent with market pricing; (2)
does the related-party share keep rising past 39.1% with no benchmark ever
printed (B03 monitorables); (3) does the FY27 AR add any disclosure at all on
the pricing mechanism (B02 questions_for_mgmt)?

**Vertical 4 — Net PPE additions versus net FVTPL/financial-asset additions.**
What the corpus establishes: gross PPE additions fell three years running (Rs
1,948.49 lakh to Rs 936.88 lakh to Rs 740.08 lakh) while 77% of the FY26
investing outflow went into a quoted-debt FVTPL portfolio whose own return fell
from 7.04% to 3.64% (B07). What it cannot establish: what specific capacity, if
any, the remaining PPE spend created, or the composition/related-party linkage
of the FVTPL portfolio (B07 input_gaps). Questions that decide it: (1) does the
FY27 AR disclose the FVTPL portfolio's composition and any related-party link
(B07 catalysts_12m); (2) does any capital-commitment note appear for the first
time (none exists in three years, Note 36(II) shows only "uncalled liability on
partly paid-up shares," not a capex commitment, AR FY26 p.140); (3) does net
PPE spend recover as a share of the investing outflow in FY27?

### 4b. Candidate signal table

*(Expanded from B09 SECTION 6 downstream candidates. UNVERIFIED; verification
and tracker writes happen at Role 5.5 in claude.ai.)*

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| HiMedia Laboratories revenue/growth disclosures | HiMedia revenue flat or declining while Titan's culture-media-adjacent lines claim growth, implying Titan's growth is not segment-wide | Event-driven | CRISIL/rating-agency rationale or BioSpectrum India trade press (Downstream Protocol Type 2: unlisted counterparty) |
| Precedence Research / Grand View Research culture-media market updates | A published update revises the TAM base materially versus the Rs 5,040-6,660 cr figure carried here | Event-driven | Published market-research reports (Type: macro data provider) |
| US tariff / HS-code notifications on biological ingredients | A tariff action lands on Titan's HS codes with no corresponding management disclosure, an unquantified exposure becoming quantifiable only from outside | Event-driven | USTR notifications; Indian Ministry of Commerce trade circulars (Type: government/regulatory) |
| Peer quarterly results (Advanced Enzyme, Fermenta, Vidhi, Nitta Gelatin) | Peer demand commentary flips from the current contradicted-deceleration read to a confirmed re-acceleration, or stays deteriorated through FY27 | Quarterly | BSE/NSE filings, investor communications (Type 1: Indian listed counterparty) |
| India export trade data (HS-code) for peptones, culture media, collagen | Titan's export growth does not show up as a broadening country/customer footprint in the DGCIS series | Monthly | DGCIS (Directorate General of Commercial Intelligence and Statistics) (Type: government trade data) |
| Nutraceutical/collagen ingredient demand trackers | Downstream nutraceutical/cosmetic formulator demand shows no correlation with Titan's collagen-peptide line growth | Quarterly | Trade publications (Nutraceuticals World); IMARC/GVR updates (Type: macro/trade press) |
| Department of Biotechnology / BIRAC BioEconomy policy announcements | No policy tailwind materialises to corroborate the company's implicit government-support framing | Event-driven | Department of Biotechnology (India), BIRAC publications (Type: government/regulatory) |

### 4c. Fragility read

- **variable_count:** 4 (the C1 dominant variables: cost-of-materials ratio,
  export share and cause, related-party raw-material share, net PPE versus
  FVTPL additions).
- **verifiability_ratio:** 4 of 4 externally observable as NUMBERS from audited
  filings (quarterly results, annual report notes); 0 of 4 have a company-stated
  CAUSAL explanation available in the corpus. The numbers are checkable without
  management; the "why" behind every one of them is company-silent, and the
  company has no earnings call through which a shareholder could ask (B05
  no_concall_mode).
- **single_point_failure:** the cost-of-materials-consumed / revenue ratio.
  Per the run's own falsification line, this single ratio failing to fall while
  growth continues (or growth reverting while the ratio holds at or above 48%)
  is sufficient on its own to break the transition case, independent of what
  the other three variables do (gate-recommendation.md Falsification Line; B04
  must_track_metrics).
- **fragility_verdict: FRAGILE.** Four variables must move together for the
  climb case to hold, none of them has a company-stated cause, the company
  holds no concalls through which to test any of them in real time, and a
  named single point of failure exists. Set against this: the numbers
  themselves are audited and externally computable every quarter, which is why
  the read is FRAGILE rather than the most severe available reading; the case
  is testable, just not yet supported.

### 4d. Research brief

Numbered live-web work for claude.ai. Items 1-2 are the PENDING LIVE
VERIFICATION links raised by the Section 4e chains below; items 3-11 are
additional live-web items the corpus cannot resolve.

1. **(Chain 1)** Open DGCIS (Directorate General of Commercial Intelligence and
   Statistics) HS-code export data for peptones, culture media and collagen
   peptides to test whether Titan's FY26 export growth maps to a broadening
   country/customer base or a concentrated single-buyer restock. Confirm by the
   Q2 FY27 results filing date (on or before 14-Nov-2026).
2. **(Chain 2)** Pull Phoenix Bio Sciences Private Ltd's MCA/RoC filings
   (AOC-4 financials) or a credit-rating rationale, if one exists, to test
   whether Phoenix's reported margin on sales to Titan is consistent with
   arm's-length input-cost pass-through. Confirm by the FY27 annual report's
   Note 41 refresh (expected ~Sep-2027) or sooner if an MCA filing surfaces.
3. HiMedia Laboratories revenue/growth disclosures (culture-media segment
   demand cross-check; B09 downstream candidate).
4. Peer quarterly results tracker: Advanced Enzyme, Fermenta, Vidhi, Nitta
   Gelatin (ongoing; B09 downstream candidate; B06 currently shows contradicted
   demand re-acceleration).
5. US tariff / HS-code notifications (USTR, Indian Ministry of Commerce) —
   Titan's export book carries an unquantified tariff exposure peers quantify
   for themselves (B06 risks_peers_raise).
6. Department of Biotechnology / BIRAC BioEconomy policy announcements (B09
   downstream candidate; tests the company's own implicit government-support
   framing).
7. MCA/RoC director and shareholder record for Phoenix Bio Sciences Private
   Ltd, independently of the Chain 2 financial-filing pull (B08 input_gaps:
   "full director/shareholder list not independently verified").
8. BSE ASM/GSM surveillance status for scrip 524717 (B08 input_gaps; not
   confirmed or ruled out this run).
9. Ravinder Gupta / HUF FY26 exit — the BSE SAST disclosure PDF, blocked at
   HTTP 403 this run, to reconcile per-transaction prices and quantities (B08
   input_gaps).
10. The full Dr Vijay Malik fundamental-analysis article on Titan Biotech,
    blocked at HTTP 403 this run; only a search-snippet was recovered (B08
    input_gaps).
11. Precedence Research / Grand View Research culture-media market updates
    (B09 downstream candidate; direct TAM input verification).

### 4e. Second-order stub (Rule F, Master Prompt v3.7)

Two chains, drafted from corpus, off the two dominant variables the evidence
base can carry furthest: export mix-cause (Vertical 2) and related-party
raw-material concentration (Vertical 3).

```
CHAIN 1: Export revenue grew 49.0% YoY to Rs 80.33 cr, 39% of FY26 revenue,
against 22.7% domestic growth (AR FY26 Note 38, p.141-142; B04).
Link 1 [DOCUMENTED]: Cost of materials consumed held flat at 48.1% of revenue
in FY26 versus 48.3% in FY25, showing no mix-driven margin lift despite the
export-share increase (B04; B01).
Link 2 [DOCUMENTED]: No filing names a customer, country, certification or
product behind the export increase in three years of annual reports; the only
industry-comparable evidence is a peer-disclosed 4-10 year customer
qualification cycle for a comparable regulated ingredient (VIDHIING Q4 FY24
call, Jun-2024; B06 verified claim; B07 FLAG-NO-CAUSAL-EXPORT-STORY).
Link 3 [INFERENCE]: If the export growth reflects newly qualified regulated
customers (pharma, diagnostics, nutraceutical) rather than a generic restock,
the cost-of-materials ratio should begin falling within 2-4 quarters as
higher-value mix takes share, matching the peer set's own margin-mix signature
(B06 analyst_note). A ratio that stays flat while export share keeps rising
instead points to a currency, pricing, or restocking explanation, not a
qualification-driven climb.
Binding constraint: customer qualification for a new regulated-ingredient
export buyer runs four to ten years on peer precedent (VIDHIING, Jun-2024), so
a genuine brand-new-customer explanation for a single-year 49% jump is
implausible on its face; the more likely explanations are an existing
qualified customer restocking, a currency effect, or the freight gross-up
distorting comparability (B01 FLAG-REVENUE-BASIS).
Unsaid: the AR's own Future Plans section proposes marketing and
trade-exhibition activity to "expand its customer base" (AR FY26 Directors'
Report, Future Plans, p.71) but never claims a new customer was actually won
in FY26. The silence on any specific qualification event, against the 4-10
year peer cycle, is the footnote implying the export jump is not a
new-customer story.
Observation that confirms or breaks this chain, and confirm-by date: PENDING
LIVE VERIFICATION — Claude web should open DGCIS HS-code export data for
peptones, culture media and collagen peptides to check whether Titan's FY26
export growth maps to a broadening country/customer base or a concentrated
single-buyer restock. Confirm by the Q2 FY27 results filing date (on or before
14-Nov-2026), cross-read against the DGCIS monthly series.

CHAIN 2: Related-party raw-material purchases were Rs 3,877.14 lakh in FY26,
39.1% of cost of materials consumed of Rs 9,916.35 lakh, with Phoenix Bio
Sciences Private Ltd alone at 26.0% of the bill and up 73.6% year on year (AR
FY26 Note 41(a); the audited figure that replaces the Rs 3,683.61 lakh / 37.1%
carried in B02/B03/B04).
Link 1 [DOCUMENTED]: Two serving Executive Directors, Raja Singla and Shivom
Singla, sit on the board of Phoenix Bio Sciences Private Ltd, the single
largest related-party raw-material counterparty (AR FY26 Corporate Governance
Report, p.43-44; B08).
Link 2 [DOCUMENTED]: No arm's-length pricing benchmark or cost-plus basis for
any related-party raw-material purchase is disclosed in three years of annual
reports (B02 input_gaps; B08 adverse_findings).
Link 3 [INFERENCE]: A related-party supplier that is both growing its share of
the group's raw-material bill and has two of the buyer's own Executive
Directors on its board carries a higher risk that FY26's flat cost-of-materials
ratio (48.1% versus 48.3% FY25) reflects negotiated related-party pricing
rather than an arm's-length input-cost trend. If so, the ratio's stability is
not informative about the transition's mix-climb question at all, because the
single largest cost line is not price-discovered externally.
Binding constraint: the company's Corporate Governance Report states all
related-party transactions during FY26 "were in the ordinary course of
business and on arm's length basis" (AR FY26, Other Disclosures, p.54), but no
disclosure exists anywhere in the corpus (a cost-plus formula, an independent
valuation, or a comparable third-party price) that would let a shareholder
test that statement.
Unsaid: no annual report footnote states whether Phoenix Bio Sciences' 73.6%
YoY growth in supply to Titan reflects a general input-cost rise, a volume
increase, or a price renegotiation; the AR is silent on which of the three it
is, despite Phoenix being nearly a fifth of total cost of materials consumed.
Observation that confirms or breaks this chain, and confirm-by date: PENDING
LIVE VERIFICATION — Claude web should pull Phoenix Bio Sciences Private Ltd's
MCA/RoC filings (AOC-4 financials) or a credit-rating rationale, if one
exists, to check whether Phoenix's reported margin on sales to Titan is
consistent with an arm's-length input-cost pass-through, or shows a pricing
pattern inconsistent with market rates. Confirm by the FY27 annual report's
Note 41 refresh (expected around Sep-2027), or sooner if an MCA filing becomes
available.
```

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in claude.ai
with live web, before Role 2.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. Titan Biotech ferments and extracts animal and plant protein into
   biological ingredients: peptones, culture media, collagen peptides, ox bile
   extract and animal-nutrition inputs.
2. It runs four plants in Rajasthan and reports as one business segment, so no
   filing splits revenue by product.
3. FY26 revenue was about Rs 206 crore, up 31.8 percent as reported, or about
   28 percent once an accounting freight add-back is stripped out.
4. Customers are named only as classes: pharma, biotech, diagnostics,
   nutraceutical, food, cosmetics, veterinary and farm-input buyers, never as
   named companies.
5. No filing gives a customer-concentration number, though the company names
   concentration as a risk without attaching a figure to it.
6. A buyer that has qualified one supplier's ingredient grade faces a costly
   re-validation to switch suppliers; peer companies in comparable regulated
   ingredients describe four to ten year approval cycles for a new buyer.
7. Exports grew 49 percent to about Rs 80 crore in FY26, faster than the 22.7
   percent domestic growth, but no filing names the country, customer or
   certification behind it.
8. The addressable market is large, roughly Rs 5,000 to 6,700 crore and
   growing about 9 percent a year, so market size does not look like the limit
   on growth here.
9. The cost of raw material stayed flat at about 48 percent of revenue even as
   sales grew 31.8 percent, which is not the pattern peers show when a richer
   product mix lifts margin.
10. No business line in the filed record carries a proven pricing or product
    moat; a forward-signal scan scored 2 out of 92 categories.
11. The one live forward signal, export growth, has no cause the company
    itself has ever stated in three years of filings.
12. The model here is a possible climb from a commodity raw-material seller
    toward a higher-value, qualified-export supplier, provable only if the
    raw-material cost ratio starts falling as exports keep rising.
13. The fragility read is FRAGILE: several things must move together, the
    company gives no voice of its own to explain any of them because it holds
    no earnings calls, and one ratio failing to move can break the case on its
    own.
14. The corpus could not establish plant capacity, the specific export
    customers or certifications behind the growth, or why a large FY26
    investment went into a bond-like financial portfolio instead of equipment.
15. The biggest open questions are whether the export growth is a genuine
    new-customer story or a one-year restock, and whether a related-party raw
    material supplier, partly overseen by the company's own directors, is
    priced at arm's length.

---

## SECTION 6: STANDING EXTRACTION ANNEX

*(Ten standing questions, answered from corpus, quote-then-comment. Opens the
named source PDFs directly per the Section 6 exception; reuses a stage-report
anchor where one already exists.)*

**1. UNITS.** No physical unit (kilogram, tonne, litre) is printed for any
product in any of the three annual reports or four results filings. Quote,
Directors' Report, State of Company Affairs: "The Company is engaged in
manufacture and export of Prepared Culture Media, Biological Goods, Plant
Growth Promoters etc. The Company is manufacturing Peptones, Biological
Extracts, Culture Media and Chemicals." (AR FY2026, Directors' Report, p.71).
Comment: this is a basket description covering the whole single reportable
segment, not one product. The only figures from which a reader could attempt a
derivation are the rupee revenue lines: "Domestic 12,585.83 / Overseas 8,033.20
/ Total 20,619.03" (Rs lakh, standalone, AR FY2026 Note 38B, p.142) — revenue
only, no volume denominator exists anywhere in the corpus, so no realisation
per unit can be derived (confirms B04 unit_economics: "NOT FOUND — no
kg/tonne/litre volume disclosed in any filing").

**2. SEGMENT CAPITAL AND DEBT.** Quote: "the Company's business activity falls
within a single primary business segment, the disclosure requirements of Ind
AS-108 in this regard are not applicable" (AR FY2026 Note 38A, Segment
Reporting, p.142). Comment: no segment assets, liabilities, capital employed or
borrowings allocation exists for either of the last two periods; there is only
one segment to allocate to. Borrowings are unallocated at the whole-company
level. Quote, Lease Liabilities note: "Lease Liabilities-non current 144.33
144.33 23.48 23.48 / Lease Liabilities-current 59.32 59.32 45.97 45.97" (Rs
lakh, AR FY2026 Note 17(b), p.134; FY26 columns first, FY25 second). Comment:
total lease liabilities were Rs 203.65 lakh FY26 versus Rs 69.45 lakh FY25, the
only debt-adjacent figure with a two-period comparative printed at this
granularity; total borrowings including non-lease debt sit at Rs 5.71 cr per
B01/B03's whole-company read, not separately re-derived here since no segment
split exists to test against.

**3. GUIDANCE VERSUS ASPIRATION.** Classified per B03/B05:
   (a) Guidance with a period: "Final dividend FY26, Rs 0.50/share (25%, face
   value Rs 2), payable after AGM 29-Sep-2026" (AR FY26 Directors' Report /
   board outcome 30-May-2026; B05). "Bonus issue 1:4 (1,03,29,625 shares),
   credited on/before 03-Nov-2026" — quote: "The Bonus shares will be
   credited/dispatched within 2 months from the date of Board's approval i.e.
   on or before November 03, 2026" (Reg 30 announcement, 03-Sep-2026,
   Annexure-A). "Share split 1:5, effective 20-Feb-2026" (Reg 30, 29-Nov-2025).
   (b) Aspiration without a period: quote, Directors' Report Future Plans: "In
   addition, the Company is developing products in the health supplement
   segment to diversify its product portfolio and address the growing demand
   for wellness and nutrition products." (AR FY2026, p.71). Comment: this exact
   or near-identical sentence recurs in AR FY2024 and AR FY2025 with no product
   name, launch date, or revenue evidence in any year (B05 timeline_slippages).
   (c) Capacity or capability only, contested by its own notes: MD&A frames the
   FY26 investing outflow as building "capacity and capabilities for future
   business growth" (B03/B07 paraphrase of MD&A framing, AR FY26 MD&A p.104),
   while the same annual report's Note 5/Note 2 show 77% of that outflow went
   into a quoted-debt FVTPL portfolio, not plant (B07 FLAG-CAPEX-CLAIM-CONTRADICTED).

**4. CONCENTRATION.** Product: NOT DISCLOSED. Single reportable segment (AR
FY2026 Note 38A, p.142); no product-wise revenue split in three years.
Customer: NOT DISCLOSED. No top-five or top-ten customer figure exists in any
filing; the company names customer concentration as a named risk factor
without a supporting number (B04 flags). Geography: DISCLOSED. Quote: "Revenue
from Operations / Domestic 12,585.83 10,254.80 / Overseas 8033.20 5390.28 /
Total 20,619.03 15,645.08" (Rs lakh, standalone, AR FY2026 Note 38B, p.142,
FY26 then FY25 columns). Comment: export share is therefore derivable and
audited (8,033.20 / 20,619.03 = 39.0% standalone FY26); this is the only
concentration axis the company discloses at all.

**5. PROMISE LEDGER.**

| Promised in | Promise | Status | Evidence anchor |
|---|---|---|---|
| AR FY24 | Dividend Rs 2.00/share FY24 | Delivered | Confirmed paid, AR FY25 |
| AR FY25 | Dividend Rs 2.00/share FY25 | Delivered | Confirmed paid, FY26 audited cash flow |
| AR FY24 & AR FY25 | Investing outflow "builds capacity... for future business growth" | Missed / contradicted in FY26 | 77% of FY26 outflow into FVTPL portfolio; sentence reused unchanged (AR FY26 Note 5, p.127) |
| AR FY24 | Developing product for health supplement | Missed | No product, launch, or revenue evidence after 3 ARs (AR FY24/25/26, Future Plans) |
| AR FY24 | Aggressive marketing/exhibitions grow domestic and export revenue | Partial | FY25 decline blamed on external slowdown; FY26 rebound unexplained (B05) |
| Reg 30, 29-Nov-2025 | Share split 1:5 "to enhance liquidity and retail participation" | Delivered | Completed 20-Feb-2026 |
| Reg 30, 24-Jul-2025 | "Will be informed in due course" on the NGenious arbitration | Missed | No follow-up filing found through 05-Sep-2026 (see Q7 below) |

Source: B05 promise_delivery, cross-checked against the announcement filenames
and dates in this run's corpus.

**6. RESTATED BASES.** Two undisclosed cross-AR changes to the identical FY25
year, neither flagged as a restatement in either document (B02). Quote, the
comparative as printed in the latest filing: "Trade Payables... 854.10 765.52"
(Rs lakh, FY26 then FY25 comparative, AR FY2026 Note 21, p.135). Comment: AR
FY2025's own original Note 20 (p.124) had printed the FY25 Trade Payables
figure as Rs 521.65 lakh, not the Rs 765.52 lakh now shown as the FY25
comparative in AR FY2026 — a Rs 243.87 lakh reclassification (Other Financial
Liabilities and a new Employee Payables line moved into Trade Payables),
disclosed as a reclassification in NEITHER annual report (B02
restatements_found). Separately, the FY25 ROE and ROCE figures differ across
the two ARs on identical FY25 PAT, equity and debt (AR FY2025 Note 44, p.146,
versus AR FY2026 Note 45, p.150 standalone / p.196 consolidated); the build-up
mechanism (Average Shareholder's Equity / Capital Employed) is not disclosed in
either document (B02).

**7. CORPORATE-ACTION CLAUSES.**
   - **Bonus issue (03-Sep-2026).** Quote: "Issue of bonus equity shares in the
   ratio of 1:4 i.e. 1 (one) new fully paid-up bonus equity shares of Rs. 2/-
   each for every 4 (Four) existing fully paid-up equity shares of Rs. 2/- each
   held by the members as on the record date, subject to the members approval
   in forthcoming Annual General Meeting." Bonus source: "Bonus shares will be
   issued out of Securities Premium account and/or retained earnings and/or
   free reserves... available as at March 31, 2026." Free reserves available
   for capitalisation: "Rs. 16,257.78 Lacs." (Reg 30, 03-Sep-2026, Annexure-A).
   Record date: not yet fixed at filing date ("will be informed in due
   course").
   - **Share split (29-Nov-2025).** Quote: "Sub-division/split of 1 (One)
   equity share having face value of Rs. 10/- each, fully paid-up, be
   sub-divided into 5 (Five) equity shares having face value of Rs. 2/- each,
   fully paid-up." Rationale, quote: "To enhance the liquidity of Company's
   equity shares and to encourage participation of retail investors by making
   equity shares of the Company more affordable." (Reg 30, 29-Nov-2025,
   Annexure-A). Effective 20-Feb-2026 per B05.
   - **Arbitration notice (24-Jul-2025).** Quote: "NGenious Solutions Private
   Limited has sent a notice invoking arbitration proceedings against Titan
   Biotech Limited, all directors and KMP's for the recovery of disputed
   outstanding dues," claim "Rs. 10,62,410/- plus GST" (Reg 30, 24-Jul-2025,
   Annexure-A). Commitment: "will be informed in due course" for status
   changes. Comment: no follow-up filing exists in the corpus. The document
   filed under the name "2025-02-28 arbitration update" is NOT a follow-up on
   this arbitration; on direct read its content is: "Investee Company has
   called the 1st call ('Tranches 2') on remaining capital. The Company has
   paid the 1st call money. Resulting, the Company's voting right in Investee
   Company [Titan Media Limited] stands increased to 48.44% (from 32.29% at
   the time of our investment in February 2024)." (Reg 30, 28-Feb-2025). This
   is a filename/content mismatch in the corpus, not an arbitration update;
   flagged here rather than silently corrected, consistent with Verifier D's
   finding pattern on other mislabelled items in this run (B12d).

**8. RELATED-PARTY PERIMETER.** Twenty-one named related entities (AR FY2026
Note 41A: 2 associates, 1 significant-influence entity, 18 other related
parties; standalone p.142-144). FY26 nature and amount, audited (Rs lakh,
Note 41B, standalone p.145): Cost of Materials Consumed — Peptech Biosciences
Ltd (Associate) 44.79; Phoenix Bio Sciences Private Ltd (Other related party)
2,574.32; Stalwart Nutritions Private Ltd (Other related party) 986.20; Titan
Animal Nutrition Private Ltd (Other related party) 78.30. Revenue from
Operations — Peptech Biosciences Ltd 389.38; Stalwart Nutritions Private Ltd
33.07; Titan Media Limited (Associate) 21.79; PG Micro Lab Solution LLP (Other
related party) 29.33; Phoenix Bio Sciences Private Ltd 3.47; Titan Animal
Nutrition Private Ltd 0.60. Loan given/received — Peptech Biosciences Ltd
420.00 / 420.00. Interest income — Peptech Biosciences Ltd 22.83. The audited
total that Verifier A's re-run pass anchors at Note 41(a) — Rs 3,877.14 lakh,
39.1% of cost of materials consumed of Rs 9,916.35 lakh — replaces the Rs
3,683.61 lakh / 37.1% figure carried in B02, B03 and B04; that figure is used
throughout this dossier with the Note 41(a) anchor, and the audited figure is
higher, so the underlying dependency finding strengthens rather than weakens
(B12a; confidence.yaml).

**9. PLEDGE AND SHAREHOLDING.** Pledge: NOT DISCLOSED as a percentage line
anywhere in three annual reports; no pledge column appears in the AR's own
shareholding tables, and no pledge event is named in any filing (B01 E3 scored
0 as an absent disclosure, not an adverse finding; B08 pledge_pct_latest: 0,
"no pledge disclosed at any point"). Shareholding, filing-anchored (two annual
points only, not twelve quarters — no BSE XBRL shareholding-pattern filing
exists in this corpus): quote, AR FY2026 Corporate Governance Report,
Shareholding Pattern: "A. Promoter's Holding / Indian Promoters 2,30,47,520
55.78 [FY26] ... 46,17,515 55.88 [FY25] ... B. Non-Promoters Holding / 1.
Institutional Investors / Mutual Funds - - / Banks, Fin Institutions, Ins Cos.
- - / FII - - / Alternate Investment Fund 11,950 0.03 1,088 0.01" (AR FY2026,
p.61). Comment: institutional ownership (mutual funds, banks, FII, QIB, FPI)
is nil to negligible across both years shown in the AR itself; IEPF holds
9.58% (unclaimed/transferred shares, not an investor position). For a
twelve-quarter series, this corpus holds none; the screener-derived figures
named in this run's task brief (promoters 55.78%, DII 0.01%, FII nil, public
44.21%, 18,671 shareholders, Jun-2026 quarter) are named here as
screener-derived, not filing-anchored, per the instruction carried from B00.

**10. VERIFICATION.**

| Document | Date | Quoted for |
|---|---|---|
| AR_FY2026.pdf (annual report FY2025-26) | FY year-end 31-Mar-2026, filed ~Aug/Sep-2026 | Q1, Q2, Q3, Q4, Q6, Q7, Q8, Q9 |
| AR_FY2025.pdf (annual report FY2024-25) | FY year-end 31-Mar-2025 | Q3, Q6 |
| AR_FY2024.pdf (annual report FY2023-24) | FY year-end 31-Mar-2024 | Q3 |
| 2026-05-30_FY26_audited_results.pdf | 30-May-2026 | Q3 (dividend recommendation) |
| Reg 30, bonus issue board outcome | 03-Sep-2026 | Q3, Q7 |
| Reg 30, share split board outcome | 29-Nov-2025 | Q3, Q7 |
| Reg 30, arbitration notice received | 24-Jul-2025 | Q5, Q7 |
| Reg 30, filed as "arbitration update" (content: Titan Media call-money/voting-right increase) | 28-Feb-2025 | Q7 |

CORPUS COMMIT HASH: c74cdb3befa949fbdccf2eed6c15dbebc08dc1a7

---

```yaml
stage: B09b-dossier
company: "TITANBIO"
run_date: "2026-09-16"
model: claude-sonnet-5
status: complete
corpus_verdict: "CORPUS GAPPED"
corpus_gaps:
  - document: "Investor presentation"
    expected_source: "company IR page"
    kind: "plausibly-nonexistent"
  - document: "Credit rating / rating rationale"
    expected_source: "rating agency site"
    kind: "plausibly-nonexistent"
  - document: "Broker / research note"
    expected_source: "BSE / broker research site"
    kind: "plausibly-nonexistent"
  - document: "BSE shareholding-pattern (XBRL) filing, 12-quarter series"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "Product-wise or plant-wise segment revenue split"
    expected_source: "company filing"
    kind: "plausibly-nonexistent"
  - document: "Capacity, utilisation, or commissioning-date disclosure, any of four plants"
    expected_source: "company filing / investor presentation"
    kind: "plausibly-nonexistent"
  - document: "Earnings call transcripts"
    expected_source: "company IR page / BSE"
    kind: "plausibly-nonexistent"
archetypes:
  - line: "Biological ingredients (single reportable segment)"
    archetype: "Commodity converter"
transition:
  - line: "Biological ingredients (single reportable segment)"
    from_tier: "R1 COMMODITY PRICE-TAKER"
    to_tier: "R3 VALUE-ADDED / SPEC'D SUPPLIER (claimed, not delivered)"
    engine: "Export customer mix shifting from commodity-grade to qualified regulated buyers, which should show up as cost of materials consumed falling as a share of revenue"
    proof_gate: "Cost of materials consumed / revenue falls below the FY26 floor of 48.1% for two consecutive quarters while like-for-like revenue growth (ex freight gross-up) holds at or above high single digits"
    recognition_gap: "OPEN: whether an assumed export-led value-add climb is already priced into Titan's current multiple is unresolved here; Stage 11 resolves it via the PE gap under the Amendment 17 converter cap"
    ugliness: "STRUCTURAL-FEATURE"
    transition_falsifier: "Cost-of-materials ratio holds flat or rises for two more quarters while like-for-like growth reverts to the FY25 flat/declining pattern, or the FY26 export growth proves to be a single-customer restock rather than a broadening qualified base"
dominant_variables:
  - "Cost of materials consumed / revenue (flat 48.1% FY26 vs 48.3% FY25)"
  - "Export revenue share and its cause (39% of revenue, +49.0% YoY, no customer/country/certification named)"
  - "Related-party share of raw-material cost (39.1% audited, Phoenix Bio Sciences 26.0%, +73.6% YoY)"
  - "Net PPE additions vs net FVTPL/financial-asset additions (PPE falling 3 years running, 77% of FY26 outflow into FVTPL)"
business_falsifier: "Cost of materials consumed rising past roughly 50% of revenue for two consecutive years, combined with a disruption or evidenced above-market pricing at Phoenix Bio Sciences (26.0% of the FY26 raw-material bill, no arm's-length benchmark disclosed, two serving Executive Directors on its board)"
mental_model_status: "DRAFT - PENDING OPERATOR SIGN-OFF"
fragility:
  variable_count: 4
  verifiability_ratio: "4 of 4 externally observable as audited numbers; 0 of 4 have a company-stated causal explanation"
  single_point_failure: "Cost of materials consumed / revenue ratio failing to fall while growth continues"
  fragility_verdict: "FRAGILE"
candidate_count: 7
second_order:
  chains_drafted: 2
  pending_live_links: 2
  confirm_by_observations: 2
research_brief_items: 11
plain_summary_points: 15
annex:
  present: true
  questions_answered: 10
  corpus_commit_hash: "c74cdb3befa949fbdccf2eed6c15dbebc08dc1a7"
```
