# HALT 1 UNDERSTANDING DOSSIER

Company: Rappid Valves (India) Ltd (RAPPID) | Run date: 2026-09-19
Assembled from committed evidence blocks B00-B09, verifier blocks
B12a/B12b/B12c(phase-1)/B12d, confidence-delta, and B13 phase-1-lite
synthesis. No new research, no web claims, no re-analysis. Every claim
below traces to a block. This is an UNDERSTANDING document. It carries no
valuation, price, or verdict vocabulary except the one scoped exception
named in Section 2 Part B4.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

1. **CONCALLS.** One transcript held: `Concall_Jun_2026_Transcript.pdf`
   (01-Jun-2026, covers H2FY26/FY26 results) (B00 concall_quarter_map).
   NO-CONCALL MODE is ON; this is the only earnings call the company has
   ever filed (B00). Most recent quarter covered: H2 FY26 / FY26
   full-year. Given the run date (19-Sep-2026) and the company's
   half-yearly SME filing cadence, the H1 FY27 result (period to
   30-Sep-2026) is not yet due; no transcript is plausibly missing beyond
   what has been filed. A quarterly-business-update cadence was promised
   on the 01-Jun-2026 call and delivered once, for Q1 FY27 (09/10-Jul-2026)
   (B05 promise_delivery).

2. **ANNUAL REPORTS.** FY26 AR held (`Annual_Report_2026.pdf`, signed
   29-Aug-2026) and FY25 AR held in `inputs/other/` (INR Thousands basis)
   (B00 inventory, reporting_units). The latest completed FY (FY26, year
   ended 31-Mar-2026) is present. Only 2 annual reports are held; 3+ years
   is NOT met from AR PDFs alone, though the RHP (Sep-2024) carries
   restated financials back to FY22 (B00 prospectus_status; B01
   fy_range "FY22 to FY26").

3. **RESULTS FILINGS.** Latest: FY26 audited results, filed 27-May-2026
   (`27May2026_RAPPID_*_BM_Outcome.pdf`). Also held: H1FY26 (13-Nov-2025),
   FY25 refiled (14-May-2025), FY25 original (12-May-2025), H1FY25
   (14-Nov-2024) (B00 results_used). No quarter-gap: the FY26 AR (signed
   29-Aug-2026) postdates the FY26 audited results (27-May-2026), and no
   half-yearly result has since fallen due (B00 freshness_pairs, AR to
   LATEST AUDITED ANNUAL RESULTS: PASS).

4. **INVESTOR PRESENTATIONS.** One held: the FY26 investor presentation,
   filed 01-Jun-2026 alongside the results and concall (`Investor_
   Presentation_1.pdf`, moved from announcements/ per B00 inventory note
   "one Investor Presentation filing, 09-Mar-2026, moved to
   presentation/" -- two presentation-type filings exist in `presentation/`
   per B00 inventory count of 2).

5. **RESEARCH / RATING.** Both empty. `rating/`: zero files; B00 confirms
   "FY26 and FY25 ARs carry no credit-rating disclosure. rating/ is
   EMPTY." No credit rating of Rappid Valves exists (B00 input_gaps).
   `research/`: zero files, no broker notes (B00, B01 input_gaps). Both
   folders are plausibly-nonexistent for an NSE Emerge SME name this
   size, not merely uncollected (B00 collector_warning: "no rating PDF...
   no credit rating of Rappid Valves was found on the web or in NSE
   filings").

6. **CORPORATE ACTIONS.** 42 Reg 30 filings held, Oct-2024 to Sep-2026,
   from the NSE SME announcements API (B00 inventory, input_gaps: "BSE
   scrip code not found: RAPPID is listed on NSE Emerge only"). These
   include order-win disclosures (BHEL, Shree Refrigerations, Muller-BBM,
   L&T FSS orders), the 21-Mar-2026 Board Meeting Outcome on IPO-proceeds
   redirection, the 24-Mar-2026 Postal Ballot Notice and 30-Mar-2026
   Corrigendum, and the 30-Apr-2026 voting results (B08 adverse_findings).
   The 14-Nov-2024 statement of deviation (IPO proceeds) is image-only,
   rendered to `work/raster/deviation_14Nov2024_p1-3.png` (B00
   input_gaps).

7. **FRESHNESS PAIR CHECK.** B00 `freshness_verdict`: FRESHNESS PAIRS OK.
   All four pairs PASS: RESULTS to CONCALL (skip condition applies since
   `concalls_available: false`, and the one transcript held postdates the
   FY26 results by 5 days); RATING BULLETIN to RATIONALE (no rating
   bulletin exists, n/a); SEBI ORDER to ORDER TEXT (no SEBI order beyond
   director-eligibility boilerplate, n/a); AR to LATEST AUDITED ANNUAL
   RESULTS (FY26 AR postdates the FY26 audited results). No pair failed;
   no CORPUS GAPPED-FRESHNESS trigger fires (B00).

8. **VERDICT LINE: CORPUS GAPPED.**
   - Credit rating rationale -- plausibly-nonexistent (confirmed against
     both ARs; no rating found on the web per B00's own collector check).
   - Broker/research notes -- plausibly-nonexistent (no coverage exists
     for a company this size; expected source, if it ever appears: company
     IR page or a rating agency site).
   - ATAM Valves concall transcripts more recent than Jul-2024 (3
     transcripts held, all Nov-2023 to Jul-2024, "stale, 2+ years") --
     findable-but-missing; expected source: BSE (Atam Valves' own filing
     page).
   - Quest Flow Controls (Meson Valves India Ltd) transcripts after
     Jun-2024 -- plausibly-nonexistent; B00/B06 confirm "BSE feed shows no
     transcript filings Oct-2024 to Sep-2026" for this scrip.
   - Final Prospectus (post-RHP) -- findable-but-missing, low materiality;
     the RHP (Sep-2024, 335pp) carries the same restated financials and
     promoter/group history, so B00 rates this "not a gap in substance."
   - Naval-specific (vs. commercial-shipbuilding) revenue disaggregation
     within the combined 32.85% Marine + Shipbuilding & Repair vertical --
     not a missing document but a missing disclosure inside documents
     held; NOT FOUND in the FY26 AR, the RHP, or any peer transcript (B03
     monitorables, B04 input_gaps, B09 flags). Carried forward as the
     load-bearing gap behind the sector-cap operator ruling in Section 4
     and the Operator Rulings list below.

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT - PENDING OPERATOR SIGN-OFF.** Nothing in this section is signed.
Signing happens only in claude.ai after live-web stress-testing.

### PART A -- THE FROM STATE (the anchor, not the model)

**A1. Archetype (per line).**
- Industrial valves (67% of FY26 revenue): **Build-to-spec component
  maker** -- customer capex cycle, PSU tender terms, input-cost
  pass-through (B04 valuation_methods, archetype split note).
- Marine/naval valves (33% of FY26 revenue, up from 0.5% in FY23):
  **Order-book business (EPC/defence/capital-goods variant)** -- order
  inflow, book-to-bill, long-cycle fixed-price execution, working
  capital on backlog (B04 revenue_streams, analyst_note: "Two archetypes
  apply by revenue stream, not one for the whole company").

**A2. The simple analogy.** Rappid makes valves, the parts that open,
shut or throttle flow in a pipe, at one plant in Palghar, Maharashtra
(B04, B00). Two-thirds of what it makes goes to factories: chemical
plants, ethanol distilleries, oil and gas lines, water and power
projects, sold mostly through government tenders at a fixed price
(B04 revenue_streams, must_track_metrics). One-third goes to shipyards
and the navy, where each valve design must first earn a certificate from
a classification society before a shipyard will buy it (B04 moats_present,
B07 A1/B2). Today, industrial valves are the business the company has
always been: commodity-priced, thin-moat, metal-cost-exposed (B04
pricing_power: "weak"). The marine line is small in absolute terms but
has grown from almost nothing three years ago to a third of sales (B04
revenue_streams; AR FY26 p.23-24 vertical table).

### PART B -- THE TRANSITION (the model)

**B1. From to To** (Quality Ladder, CLAUDE.md).
- Industrial valves: no claimed transition. This line stays the FROM
  anchor -- R1 Commodity price-taker (PSU fixed-price tenders with no
  escalation clause, material cost 71% of FY26 revenue, weak pricing
  power) (B04 pricing_power, unit_economics key_lever). No forward
  evidence in the corpus claims this line is climbing the ladder on its
  own.
- Marine/naval valves: **FROM R1 (undifferentiated, 0.5% of revenue in
  FY23, no certified position) TO R3 Value-added/spec'd supplier**
  (type-approval and switching-cost lock-in once a vessel programme
  accepts the design, partial pricing power claimed but ROCE durability
  not yet evidenced at the 20-25% R3 band) (B04 moats_present; B07
  active_categories A1 "Strong", B2 "Strong"; company-wide ROCE fell to
  14% FY26 from 17% FY25 on the AR's own disclosed basis, B01 data_notes
  G3 -- the R3 return band is not yet reached at the company level).

**B2. The engine.** Two things physically changed: (1) the company
earned marine type-approval and classification-society certifications
(ClassNK, UL, API/DNV/IBR cluster) and approved-vendor status with named
shipyards (Mazagon Dock, GRSE, Cochin Shipyard, Udupi, L&T Shipbuilding)
(B07 A1, B2, completionist_recount); (2) those certifications converted
into dated, PO-backed Fleet Support Ship (FSS) work orders in Q1 FY27
(BHEL Rs18.05 Cr, Shree Refrigerations Rs8.55 Cr, Muller-BBM Rs3.25 Cr,
L&T Rs2.84 Cr) (B07 catalysts_12m, anchor: Reg 30 filings 29-May/08-Jun/
15-Jun/13-Aug-2026). The mix shift itself is the AR's own vertical table:
Shipbuilding & Repair + Marine rose to 32.85% of FY2026 revenue (B04
revenue_streams; AR FY26 p.23-24).

**B3. The proof gate.** The hard binary observation Stage 11 FTTCP must
test: **H1 FY27 (period to 30-Sep-2026) operating cash flow turns
positive, AND combined receivables plus inventory fall below the
31-Mar-2026 level of Rs 51.51 Cr (Rs 24.83 Cr + Rs 26.68 Cr), while
Marine + Shipbuilding & Repair revenue share holds at or above 30%** (B04
must_track_metrics "CFO/PAT... healthy trending toward >0.7x"; B13
falsification_metric; gate-recommendation.md separating observation).
Until this fires, the margin-and-cash payoff of the mix shift is
narrative, not proof; the mix shift itself (B2) is already documented,
but its economic payoff is not.

**B4. The recognition gap (resolved at Stage 11).** OPEN QUESTION, no
number stated here: does the market's current pricing of Rappid already
assume the marine mix-shift narrative keeps compounding -- given that the
mix has already moved from under 1% to 33% of revenue and generated
Rs 30 Cr of FSS order intake in a single quarter -- or does it still
price the company as a flat, commodity industrial valve maker? Stage 11
resolves this via the destination-PE gap; this dossier states no fair
value, no PE, and no conclusion.

**B5. The ugliness test (draft classification, for operator review).**
Today's ugly optic is four consecutive years of negative operating cash
flow (FY23-FY26, cumulative CFO -Rs 26.56 Cr against cumulative PAT
+Rs 17.11 Cr, B01/B03) alongside receivables +29.1% and inventory +65.0%
against +2.1% revenue growth in FY26 (B02 Notes 16/18).
  - Evidence for **ARTIFACT-OF-CLIMB**: the CMD's specific, dated account
    -- Rs 14-15 Cr of March-2026 dispatches and about Rs 10 Cr of
    material held back awaiting a private-customer price revision
    (Concall_Jun_2026 p.6, p.23, via B05/B12b); only 8.34% of receivables
    are aged over six months, consistent with recent billing rather than
    stuck money (B02 Note 18); the IPO's own capex/acquisition buffer was
    a one-time, dated redirection (B02 Note 32), not a recurring drain.
  - Evidence for **STRUCTURAL-FEATURE**: the negative-CFO run spans FY23
    (+35% revenue growth), FY24 (+123%), FY25 (+43%) and FY26 (+2%) alike
    (B01 analyst_note) -- it is not confined to the slow year; working-
    capital days rose monotonically from 150.3 to 334.2 across all five
    years, FY22 to FY26 (B01 flags FLAG-GATE0); PSU tenders carry no
    escalation clause, the company pays 50% supplier advances with no
    commodity hedge (B05 red_flags; Concall p.16, p.20-21); and the same
    PSU-shipyard relationship that produces the B2 qualification-lock-in
    moat is management's own named cause of the receivable delay (B07
    top_moat_risks, analyst_note: "one mechanism showing up as both an
    asset and a liability").
  - **Most evidenced reading on this record: leaning STRUCTURAL, given
    the four-year span crossing both high-growth and low-growth years
    and the absence of any escalation clause or hedge to reverse the
    pattern mechanically.** ARTIFACT-OF-CLIMB remains a live, specifically
    evidenced competing account for the FY26 increment alone. **Separating
    observation and confirm-by date: the H1 FY27 result (due on NSE
    Emerge by mid-November 2026)** -- receivables plus inventory falling
    below Rs 51.51 Cr with CFO turning positive supports ARTIFACT; both
    holding or rising with CFO still negative supports STRUCTURAL. This
    classification is a DRAFT input to the operator's Part B5 sign-off,
    not a verdict.

**B6. The transition falsifier** (kills the transition thesis, distinct
from Part C3). Marine + Shipbuilding & Repair revenue share reverting
toward the FY23 base of 0.5% for two consecutive periods, or the FSS/
naval order pipeline drying up (no further named work orders) while the
receivable/inventory pattern that the mix shift was meant to justify
persists unchanged (B04 must_track_metrics: "Marine + Shipbuilding &
Repair % of revenue... red_flag: reverting toward the FY23 base of
0.5%").

### PART C -- WHAT THE MODEL WATCHES

**C1. Dominant variables** (derived from B2 the engine and B3 the proof
gate):
1. CFO / PAT ratio -- current state: -1.67x FY26, -2.12x FY25 (B03).
2. Marine + Shipbuilding & Repair % of revenue -- current state: 32.85%
   FY26, up from 0.5% FY23 (AR p.23-24; B04).
3. Executable order book (Rs Cr), QoQ -- current state: ~Rs 40 Cr at
   Q1 FY27, +60% YoY, plus ~Rs 11 Cr pending confirmation (B05, B09
   downstream_candidates).
4. Trade receivables / inventory turnover -- current state: 2.14x /
   2.00x FY26, down from 2.71x / 3.22x FY24 (B02 Note 36).

**C2. What the model rejects.** How large the Indian naval/marine valve
market is, in rupees or dollars -- no company disclosure, peer
disclosure, or search in this run's corpus sizes it (B09
FLAG-NAVAL-TAM-NOT-SIZEABLE), and it is not the binding constraint: the
company's own disclosed Rs 120 Cr revenue-capacity ceiling binds within
3-5 years before the addressable market does (B09 FLAG-CAPACITY-
CONSTRAINT, capacity_check). The import-substitution framing management
uses is also rejected as a sizing argument: India was a net exporter of
valves in 2024 ($2.66 Bn exported vs $2.15 Bn imported) on the company's
own cited figures (B09 FLAG-MGMT-CLAIM-INCONSISTENCY). The binding
questions are execution (can the naval order book convert to cash) and
capacity (can Rs 120 Cr of plant support two more years of guided
growth), not market size.

**C3. The business falsifier** (kills the FROM business itself, distinct
from B6). A working-capital funding failure: the CMD's own stated need
for additional working-capital funding within 4-5 months of the
01-Jun-2026 call (that is, roughly October-November 2026) going unmet,
given the IPO's own capex-and-acquisition buffer (Rs 764.51 Lakh, 25.1%
of gross proceeds) has already been spent redirecting to working capital
(B02 Note 32; B08). An unmet funding need would force an order-execution
halt, a covenant issue, or a distressed capital raise across both
revenue lines at once, independent of whether the marine mix shift is
real (B05 guidance table: "Additional working-capital funding, Required
in 4-5 months").

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

Drafted per prompts/13-synthesis-pipeline.md's BUSINESS UNDERSTANDING
NARRATIVE spec (five questions, prose, from B01-B09). Stage 13's copy
(outputs/final/business-narrative.md) is the governing version; this is
the Halt 1 draft, reused verbatim from that phase-1-lite run since both
were built from the same blocks.

Rappid Valves makes ball, gate, globe, butterfly, check and strainer
valves from 15 mm to 600 mm, in steel, brass and bronze, at one plant in
Palghar, Maharashtra. A valve opens, shuts or throttles flow in a pipe,
and no process plant or ship can run its piping without one. Industrial
valves made 67% of FY26 revenue and go into ethanol, chemical, oil and
gas, water and power plants. Marine valves made 33% and go into navy and
commercial ships, where each valve design must first pass a
classification society approval, such as ClassNK or DNV, before a
shipyard will accept a quote.

The marine buyers are the shipyards, Mazagon Dock, GRSE, Cochin
Shipyard, Hindustan Shipyard, Udupi and L&T Shipbuilding, plus system
integrators such as BHEL, Shree Refrigerations and Muller-BBM on the
navy Fleet Support Ship programme. Government shipyards buy by tender at
a fixed price with no escalation clause, and once a valve is approved
into a vessel programme the yard rarely changes supplier. On the
industrial side one customer, Praj Industries, gave about a quarter of
FY26 revenue under a rate contract that is now being repriced. Repeat
business is 60% in the company deck and "almost 75%" on its call, and
the run could not reconcile the two.

Present demand comes from the named naval shipyards (Mazagon Dock, GRSE,
Cochin Shipyard, L&T Shipbuilding), which are building vessels now. The
Ethanol Blended Petrol Programme target and oil company ethanol capex
sit behind the ethanol, brewery and wastewater vertical, the largest
single vertical at 31% of FY26 revenue. GeM portal PSU industrial valve
tender awards feed the fixed price industrial book.

Ministry of Defence capital outlay and the Rs 3 lakh Cr defence
production target for 2029 set the pace of naval orders, and Rappid took
Rs 30 Cr of Fleet Support Ship orders in Q1 FY27 alone. The US data
centre customer contract conversion would open export demand, but that
customer has sat at the testing and NDA stage for more than 16 months.
The Praj Industries rate contract repricing, worth about Rs 10 to 12 Cr,
is the nearest industrial signal.

The marine line has a moat: its type approvals and approved vendor
status are documented, and they score high on rare manufacturing
capability and qualification lock in. It is not a sole source position,
because qualified rivals such as KSB can bid on the same reverse auction
tenders. The industrial line has no moat, since the company takes the
metal price and the PSU tender terms as given, and material cost is 71%
of revenue. The two structural asymmetry tests, talent and
cannibalisation barrier, both score zero. The same PSU shipyard link
that builds the lock in also slows collection of cash.

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. Verticals framed (one per dominant variable, Section 2 C1)

**Vertical 1 -- Cash conversion (CFO/PAT).** The corpus establishes: CFO
negative every year FY23-FY26 (B01, B03); receivables +29.1%, inventory
+65.0% against +2.1% revenue in FY26 (B02 Notes 16/18); zero provisioning
against either trend (B02); two conflicting management explanations for
the same balance-sheet movement (written results note: "higher order
volumes"; CMD on call: March dispatches and price-revision holdbacks)
(B12b). It cannot establish: receivables split by customer type (PSU vs
private vs export -- NOT FOUND, AR Note 18), or whether the FY26 pattern
reverses in H1 FY27. Deciding questions: (1) does H1 FY27 CFO turn
positive; (2) do receivables plus inventory fall below Rs 51.51 Cr; (3)
which of the two management accounts (order-volume growth vs. dispatch
timing) does the customer-type split, if ever disclosed, support.

**Vertical 2 -- Marine mix shift.** The corpus establishes: Marine +
Shipbuilding & Repair rose from 0.5% (FY23, company memory cross-check)
to 32.85% (FY26 AR p.23-24); Q1 FY27 FSS orders of Rs 29.85 Cr from named
counterparties (B07); type-approval and vendor-status moats scored
Strong (B07 A1, B2). It cannot establish: the naval-only share within
the combined 32.85% line (commercial shipbuilding is blended in, NOT
FOUND anywhere in the corpus); whether the FSS orders convert to revenue
without a March-2026-style holdback. Deciding questions: (1) does the
FY27 AR or a future deck ever split naval from commercial shipbuilding;
(2) does the mix share hold above 30% for two more periods; (3) do the
FSS counterparties (BHEL, Shree Refrigerations, Muller-BBM, L&T) pay on
PSU-shipyard-like terms or faster.

**Vertical 3 -- Executable order book.** The corpus establishes: ~Rs 40 Cr
executable book at Q1 FY27, +60% YoY, plus ~Rs 11 Cr of confirmations
pending PO (B05, 10-Jul-2026 GBU); order book fell sequentially from
Rs 24.64 Cr to Rs 20.19 Cr ahead of the H2 FY26 miss (B05 red_flags); a
Rs 119 Cr GeM tender-bid pipeline (Oct-2025) was never followed up in any
later filing (B05). It cannot establish: how much of the Rs 40 Cr sits on
fixed-price PSU terms with no escalation versus flexible private/export
terms (B04 mgmt_questions). Deciding questions: (1) does the order book
keep rising QoQ without another unexplained disappearance like the
Rs 119 Cr pipeline; (2) what fraction is PSU fixed-price; (3) does H1/H2
FY27 revenue recognition track the order book without a repeat holdback.

**Vertical 4 -- Receivables/inventory turnover.** The corpus establishes:
trade receivables turnover fell 2.71x to 2.14x, inventory turnover fell
3.22x to 2.00x, FY24 to FY26 (B02 Note 36); Note 36's own printed ratios
do not reconcile to its own base-value table, and the MD&A states a
third, different value again (B03 analyst_note -- treat Note 36 as
printed as unreliable, use recomputed figures). It cannot establish: an
industry-normal benchmark specific to PSU-shipyard-serving valve makers
(peer disclosure is partial -- Atam Valves states 90-120 days industry
credit period, KSB reports PSU/solar receivables beyond 120 days, both
short of Rappid's 170, B06). Deciding questions: (1) does turnover
recover toward FY24 levels in H1 FY27; (2) does a peer ever disclose a
PSU-shipyard-specific receivable cycle to benchmark against; (3) does the
naval mix (longer-cycle, B04) mechanically explain part of the gap once
disaggregated.

### 4b. Candidate signal table

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| Named naval shipyards (Mazagon Dock, GRSE, Cochin Shipyard, L&T Shipbuilding) | No new shipyard vendor-list addition or FSS-linked order for 2 consecutive quarters | Quarterly | Individual shipyard investor disclosures / Ministry of Defence PIB releases (B09) |
| Ministry of Defence capital outlay and Rs 3 lakh Cr defence-production target (2029) | Union Budget defence capital outlay flat or cut YoY | Event-driven (Union Budget) | Union Budget documents; PIB, Ministry of Defence (B09) |
| GeM portal PSU industrial-valve tender awards | Rappid's win rate on tracked GeM tenders falls, or a disclosed pipeline (like the Rs 119 Cr Oct-2025 figure) disappears again without explanation | Event-driven | Government e-Marketplace (GeM) public tender/award data (B09) |
| US data-centre customer (NDA) contract conversion | Two more quarters pass with the relationship still at lab-testing/NDA stage | Event-driven | Rappid's own Reg 30 / exchange filings (B09; B05 kill_signal) |
| Praj Industries Ltd ARC repricing (~Rs 10-12 Cr) | Renegotiation stalls, or Praj shifts volume to a competitor | Event-driven | Praj Industries Ltd investor disclosures/concalls (B09) |
| Ethanol Blended Petrol Programme target and OMC ethanol-infrastructure capex | Programme target or OMC capex plan is scaled back | Annual | Ministry of Petroleum & Natural Gas / PIB releases (B09) |

These six are UNVERIFIED; verification and tracker writes happen at Role
5.5 in claude.ai, per Downstream_Source_Discovery_Protocol_v1_0,
unchanged.

### 4c. Fragility read

- **variable_count: 5** -- the near-term triggers this bull case needs
  to go right: (1) FSS naval shipset execution without a holdback
  repeat; (2) FY27 growth guidance ("50% or more") delivery; (3) Praj
  ARC repricing (~Rs 10-12 Cr); (4) EBITDA margin recovery above 19.36%
  against ~Rs 22 Cr of low-margin carried orders; (5) working-capital
  funding secured without dilution or a covenant event (B05 triggers
  list; B07 catalysts_12m; B09 FLAG-CAPACITY-CONSTRAINT).
- **verifiability_ratio: 2 of 5 externally observable.** FSS execution
  (counterparty-named work orders, checkable against BHEL/Shree/
  Muller-BBM/L&T or PIB disclosures) and Praj ARC repricing (checkable
  against Praj's own investor disclosures) are externally observable.
  FY27 growth delivery, margin recovery, and the working-capital funding
  outcome rest on Rappid's own filings and the CMD's spoken account, not
  on an independent counterparty confirmation.
- **single_point_failure:** an additional working-capital funding
  shortfall. The CMD's own statement that fresh funding is needed within
  4-5 months (Concall p.16, p.20-21), combined with the IPO's
  capex/acquisition buffer already spent redirecting to working capital
  (B02 Note 32), means a funding failure would halt order execution
  across both revenue lines regardless of how the naval order book
  performs.
- **fragility_verdict: FRAGILE.** Five variables, only two externally
  verifiable, one named single point of failure, plus twelve active
  flags spanning cash (INDETERMINATE), promoter (CONCERN), guidance
  delivery, and disclosure quality (B13 flags_active; gate-
  recommendation.md flag table).

### 4d. Research brief (live-web work order for claude.ai)

1. Verify the naval-specific (vs. commercial-shipbuilding) revenue split
   within the 32.85% Marine + Shipbuilding & Repair line -- check the
   FY27 AR, investor decks, or a direct extraction request to management
   (NOT FOUND anywhere in this corpus; load-bearing for the sector-cap
   ruling).
2. Verify BHEL's, Shree Refrigerations', and Muller-BBM's own disclosures
   on Navy Fleet Support Ship programme payment/milestone terms (Chain 1,
   Section 4e -- PENDING LIVE VERIFICATION).
3. Check Rappid's Reg 30 filings after 19-Sep-2026 for any bank-facility
   enhancement, rights issue, or preferential allotment announcement, and
   cross-check timing against the CMD's own 4-5 month funding-need
   statement (Chain 2, Section 4e -- PENDING LIVE VERIFICATION).
4. Check Praj Industries Ltd's own investor disclosures/concalls for the
   status of the ARC repricing the CMD said would be signed "on
   Thursday" (Concall p.22) but which no later Rappid filing has
   reported (B12b MAJOR finding).
5. Check GeM portal public tender/award data for the outcome of the
   Rs 119 Cr tender-bid pipeline named 16-Oct-2025 and never mentioned
   again.
6. Check whether a rating agency has since rated Rappid Valves (none
   exists as of this run; re-check at the next extraction cycle).
7. Verify institutional (FII/DII) shareholding at 31-Mar-2026 from
   `inputs/shareholding/SHP_31-MAR-2026.xml` (XBRL; not parsed this
   pass -- see Section 6, Q9).
8. Check PIB/Ministry of Defence releases for the Rs 3 lakh Cr defence-
   production-by-2029 target's current status and any near-term capital
   outlay change.
9. Cross-check the US data-centre customer's NDA/lab-testing status,
   16+ months stalled as of the Jun-2026 call, against any subsequent
   Reg 30 disclosure.

### 4e. Second-order stub (Rule F, Master v3.7)

Stub carries the first TWO chains, drafted from corpus. Claude web
extends to the Rule F floor of 5 with live-web links before Role 2.

```
CHAIN 1: Rs 29.85 Cr of FSS naval shipset work orders received in Q1
FY27 from BHEL, Shree Refrigerations and Muller-BBM, plus Rs 2.84 Cr
from L&T in Aug-2026 (B07 catalysts_12m; B09 downstream_candidates)
Link 1 [documented]: These are PO-backed, dated work orders disclosed
via Reg 30 filings on 29-May, 08-Jun, 15-Jun and 13-Aug-2026 (B07).
Link 2 [documented]: Marine + Shipbuilding & Repair revenue share
already reached 32.85% of FY26 revenue, up from 0.5% in FY23, the
second-largest single vertical after Ethanol at 30.81% (AR FY26 p.23-24;
B04).
Link 3 [INFERENCE]: If these FSS orders convert to revenue in H1/H2
FY27 without the March-2026-style dispatch holdback the CMD described
for FY26 (Concall p.6, p.23), the marine share should rise further; the
receivable-day profile tied to how these system integrators pay (rather
than how direct PSU shipyards pay) becomes the swing factor for whether
cash conversion improves or worsens as naval share grows.
Binding constraint: a disclosed Rs 120 Cr revenue-capacity ceiling
(Concall p.5, p.11) with no new capacity plan beyond continued
automation investment (B07 capex_embedded_growth 12%); two years of the
company's own FY27 guidance sustained would hit this ceiling almost
exactly (B09 FLAG-CAPACITY-CONSTRAINT).
Unsaid: the FY26 AR names the FSS orders and the marine mix shift
specifically, but nowhere repeats the FY27 "50% or more" growth figure
tied to them (grep-verified absent from Annual_Report_2026.txt, B05) --
management discloses the naval wins but not the growth number built on
them.
Who pays, and why now [PENDING LIVE VERIFICATION]: whether BHEL, Shree
Refrigerations and Muller-BBM -- system integrators on the FSS
programme, not direct PSU shipyards -- pay on PSU-shipyard-like terms or
faster is not established anywhere in this corpus. Claude web should
open BHEL's own investor/tender disclosures and any Ministry of Defence
FSS-programme payment-milestone documentation.
Observation that confirms or breaks this chain, and confirm-by date: the
H1 FY27 half-yearly result (NSE Emerge filing, expected by mid-November
2026) showing FSS-linked revenue recognised without a repeat holdback,
and, if disclosed, marine-vertical receivable days trending below the
company-wide 170-day FY26 figure.

CHAIN 2: Operating cash flow negative every year FY23-FY26, cumulative
CFO -Rs 26.56 Cr against cumulative PAT +Rs 17.11 Cr over the same four
years (B01, B03)
Link 1 [documented]: Receivables rose 29.1% and inventory 65.0%
(finished goods +93.6%) against revenue growth of 2.1% in FY26 (B02
Notes 16/18; AR p.55).
Link 2 [documented]: Short-term borrowings more than doubled, Rs 8.41 Cr
to Rs 17.84 Cr, funding the gap, while cash fell from Rs 9.49 Cr to
Rs 2.51 Cr (B03; AR Balance Sheet p.55).
Link 3 [INFERENCE]: The CMD's own statement that "no working capital is
enough" and that additional funding will be needed in 4-5 months
(Concall p.16, p.20-21; B05) implies the company sits near the limit of
its short-term borrowing capacity; if H1 FY27 receivables and inventory
do not fall from the combined Rs 51.51 Cr FY26 year-end level, a fresh
capital raise or bank-limit increase becomes likely within FY27 H2 to
fund the naval order book and the industrial working-capital cycle at
once.
Binding constraint: the IPO's own capex and acquisition budgets
(Rs 764.51 Lakh, 25.1% of gross proceeds) are already spent -- redirected
to working capital via the 30-Apr-2026 postal ballot (B08; B02 Note 32)
-- so that buffer no longer exists; the only remaining flexibility is
fresh short-term borrowing or fresh equity.
Unsaid: the FY26 Directors' Report states "there have been no material
changes and commitments, affecting the financial position of the
Company" for the period covering the very same postal-ballot redirection
it describes two sentences later in the same report (AR p.35, lines
3395-3412), and the written FY26 results note attributes the working-
capital build to "higher order volumes" while the CMD separately cites
March-dispatch timing and price-revision holdbacks (B05; B12b) -- two
different causal accounts for the same cash shortfall sit inside the
same disclosure record.
Who pays, and why now [PENDING LIVE VERIFICATION]: whether Rappid's
bankers, or a prospective preferential-issue investor, would extend
fresh working-capital limits, and on what terms, is not established in
this corpus. Claude web should check Rappid's Reg 30 filings after
19-Sep-2026 for a bank-facility enhancement, rights issue, or
preferential allotment, and time it against the CMD's own roughly
October-November 2026 window.
Observation that confirms or breaks this chain, and confirm-by date: H1
FY27 (to 30-Sep-2026) operating cash flow, filed by mid-November 2026; a
positive figure with receivables plus inventory below Rs 51.51 Cr breaks
the chain toward the artifact reading (Section 2, Part B5); a further
negative print, with or without a new funding announcement, confirms it.
```

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in
claude.ai with live web, before Role 2.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. Rappid Valves makes ball, gate, globe, butterfly, check and strainer
   valves, 15mm to 600mm, at one plant in Palghar, Maharashtra.
2. A valve opens, shuts or throttles flow in a pipe. No factory or ship
   can run its piping without one.
3. The company sells two valve types: industrial valves for process
   plants, and marine valves for ships and the navy.
4. Factories in ethanol, chemicals, oil and gas, water and power buy
   industrial valves, often through PSU tenders at a fixed price.
5. Navy shipyards such as Mazagon Dock, GRSE and Cochin Shipyard, and
   system integrators like BHEL, buy marine valves once a design passes
   a classification-society type approval.
6. Marine and shipbuilding revenue rose from under 1% of sales in FY23
   to 33% in FY26, and Q1 FY27 brought Rs 30 Cr of new navy Fleet
   Support Ship orders.
7. Industrial valve demand depends on factory capex and government
   tenders, and grew only 2% in FY26 after several years of much faster
   growth.
8. The marine line has a real moat: type-approval certificates and
   approved-vendor status lock a valve into a ship design once it is
   chosen.
9. The industrial line has no moat. Material cost is 71% of revenue,
   and the company takes the market price for metal and for the tender.
10. The company's story is a mix shift: less commodity industrial work,
    more certified marine work, aimed at a higher margin and a steadier
    order book.
11. The plan is fragile: only 2 of 5 tracked variables can be checked
    from outside the company, and one funding shortfall could stop both
    lines at once.
12. The corpus could not find a rupee or dollar size for the Indian
    naval valve market, or a naval-only revenue split within the 33%
    marine-and-shipbuilding line.
13. No credit rating of Rappid Valves exists, and no broker research
    note exists, so the cash-flow read rests on the company's own
    filings alone.
14. Will the receivables and inventory that built up by March 2026 fall
    back by September 2026, or will they stay high for a fifth year
    running.
15. Will FY27 sales growth reach anywhere near the "50% or more" guided
    on the June 2026 call, a number the company's own annual report
    does not repeat three months later.

---

## SECTION 6: STANDING EXTRACTION ANNEX

### Q1. UNITS

Quote: "With an installed manufacturing capacity of 33,500 industrial
and marine valves and 85% capacity utilisation, the facility supports
both current production requirements and future growth."
(Annual_Report_2026.txt, p.4; repeated near-verbatim at p.23: "installed
annual manufacturing capacity of 33,500 industrial and marine valves...
operated at approximately 85% capacity utilisation during FY2026.")

Quote: "Revenue from Operations (Domestic) 4,261.1 / Revenue from
Operations (Export) 1,020.3" (FY26, Rs Lakh), total revenue from
operations "5,323.3" (Note 21, AR p.65-66).

Comment: No per-valve average selling price or per-unit cost is printed
anywhere in this corpus (B04 unit_economics: "revenue_per_unit: NOT
FOUND"). The basket covers many products (15-600mm, ferrous and
non-ferrous, multiple valve types) sold across two lines with very
different pricing power (industrial 67%, marine 33% of FY26 revenue by
the AR's own vertical table, p.23-24), so a single blended figure would
mask the mix. If a rough figure is wanted, the volume line is the
disclosed installed capacity of 33,500 units/year at 85% utilisation
(itself a capacity estimate, not an audited unit-production count)
against the revenue line of Rs 5,323.3 Lakh (Rs 53.23 Cr) FY26 revenue
from operations (Note 21). No audited count of units actually produced
or sold is printed.

### Q2. SEGMENT CAPITAL AND DEBT

Quote: "The Company identifies primary segments based on the dominant
source, nature of risks and returns and the internal organisation and
management structure... However the company is currently dealing in
only one primary segment." (Note 2.18, AR p.59).

Quote: "Based on exemptions/relaxations provided to SMEs disclosures
under AS 17 'Segment Reporting' are not applicable to the Company for
the financial year ended 31st March 26." (AR p.69).

Comment: Segment assets, liabilities, capital employed and borrowings
are NOT allocated by segment; the company discloses one reportable
segment ("manufacturing of valve solutions," per the 19-Jan-2026 NSE
clarification cited in B00) and claims the SME AS-17 exemption.
Borrowings are disclosed only at the company level: short-term
borrowings rose from Rs 8.41 Cr (FY25) to Rs 17.84 Cr (FY26) (B03; AR
Balance Sheet p.55). No segment-level capital-employed or borrowings
split exists anywhere in the corpus.

### Q3. GUIDANCE VERSUS ASPIRATION

| Statement (quoted) | Source, page | Classification |
|---|---|---|
| "Volume CAGR Target: 50% CAGR in FY 2026 and FY 2027" | 01-Feb-2025 Reg 30 update, p.2 | (a) Guidance, period FY26-FY27 |
| "closing to 50% or more" (re: FY27 growth) | Concall_Jun_2026_Transcript, p.10 | (a) Guidance, period FY27, spoken not filed in writing |
| "we are well equipped up to 120 crores, so I don't see that we need to further expand our capacity" | Concall_Jun_2026_Transcript, p.5 | (c) Capacity/capability only, no period |
| "Anticipates further growth acceleration in forthcoming quarters" | 03-Jul-2025 Reg 30 update (per B05 guidance table) | (b) Aspiration, no period or number |
| Capex completion "By June 2025" | 01-Feb-2025 Reg 30 update (per B05) | (a) Guidance with period; outcome PARTIAL (B05 promise_delivery) |
| Backward integration foundry acquisition, "advanced talks," Rs 400 Lakh budget | 01-Feb-2025 Reg 30 update (per B05) | (b) Aspiration, no firm period; outcome MISSED/ABANDONED (B02 Note 32) |
| "Sales: ₹14.87 Crore for Q1 FY27 (↑ ~28% YOY)" | 10-Jul-2026 GBU, p.3 | Actual reported figure, not forward guidance; shown for contrast against the FY27 target above |

Comment: The FY27 "50% or more" figure is guidance-with-period by form,
spoken on the one filed earnings call, but is absent from the FY26 AR
published three months later -- "50%" and "closing to" return zero
matches anywhere in Annual_Report_2026.txt (grep-verified, B05). The
company has not repeated its own headline growth number in a formal
shareholder document since making it.

### Q4. CONCENTRATION

Quote: "Ethanol, Breweries & Industrial Wastewater Treatment was the
largest industry contributor at 30.81%, followed by Shipbuilding &
Repair at 24.51%, Chemicals at 15.43% and EPC & OEM at 14.89%."
"Shipbuilding & Repair & Marine together contributed 32.85% of FY2026
revenue." (AR FY26, p.23-24).

Quote: "Revenue from Operations (Domestic) 4,261.1 / (Export) 1,020.3"
FY26, vs. "4,706.6 / 439.2" FY25 (Rs Lakh, Note 21, AR p.65-66).

Comment: Product/vertical concentration is disclosed (top vertical
30.81%, top two verticals 55.32% of FY26 revenue). Geography
concentration is disclosed only as a domestic/export split: export rose
from about 8.4% of revenue (FY25) to about 19.2% (FY26), no
country-level breakdown exists. Customer-level concentration is NOT
DISCLOSED anywhere in the AR or RHP; the only customer-level figure
(Praj Industries about 24-26% of FY26 revenue) comes solely from the
CMD's spoken remarks on the 01-Jun-2026 call, not from a filed
disclosure (B05).

### Q5. PROMISE LEDGER

| Promised in | Promise | Delivery status | Evidence anchor |
|---|---|---|---|
| 01-Feb-2025 Reg 30 update | 50% volume CAGR, FY26 | MISSED -- FY26 actual +2.1% (Rs 52.13 Cr to Rs 53.23 Cr); H1 FY26 +46.9%, H2 FY26 -24.9% | 27-May-2026 results PDF; B05 |
| 01-Feb-2025 Reg 30 update | Capex completion by June 2025 | PARTIAL -- new facility commissioned (03-Jul-2025 update), but Rs 364.5 Lakh of the object stayed unutilised through FY26 (audited FY26 capex Rs 179.4 Lakh) and was later redirected | 03-Jul-2025 update; Note 32 AR p.68-69; B05 |
| 01-Feb-2025 Reg 30 update | Backward integration, Pune foundry acquisition, Rs 400 Lakh | MISSED/ABANDONED -- entire budget redirected to working capital via postal ballot, results 30-Apr-2026 | Note 32, AR p.68-69; postal ballot notice 24-Mar-2026; B05 |
| 16-Oct-2025 GBU | Rs 119 Cr GeM tender bid pipeline, result awaited | UNRESOLVED/UNREPORTED -- no later filing states the outcome | 16-Oct-2025 GBU; B05 |
| 03-Jul-2025 Reg 30 update | "Anticipates further growth acceleration in forthcoming quarters" | PARTIAL/MIXED -- Q2 FY26 genuinely accelerated (~Rs 17.19 Cr) before H2 FY26 fell 24.9% YoY | B05 promise_delivery |
| 01-Jun-2026 concall | Quarterly business updates going forward | DELIVERED -- Q1 FY27 update issued 09-Jul-2026 (revised 10-Jul-2026), on schedule | B05 |
| 01-Jun-2026 concall | FY27 growth "closing to 50% or more" | IN PROGRESS, not gradable this run -- Q1 FY27 +28% YoY, below the run-rate a 50%+ full year needs | Concall p.10; 10-Jul-2026 GBU; B05 |

Tally (round 2, B05): 1 delivered, 2 partial, 2 missed of the five
gradable items. Credibility grade: C (B05 credibility_grade).

### Q6. RESTATED BASES

Quote: "2.23 Previous year figures have been regrouped/rearranged
wherever necessary" (Note 2.23, AR p.60).

Quote: "xxvi Previous year figures (comparatives) have been regrouped
and reclassified wherever necessary to correspond to figures of current
year" (Note 37(xxvi), AR p.70).

Quote (comparative mismatch, printed as filed): Note 29 (Deferred Tax
Liabilities/Assets) shows "Net deferred tax liabilities... 14.8 [FY26]...
0.1 [FY25 comparative]" (AR p.67), while the Balance Sheet's own Note 7
line for the same FY25 date reads "Deferred Tax Liabilities/(Assets)...
(14.8) [FY26]... (13.4) [FY25]" (AR p.61).

Comment: No quantified restatement table exists anywhere in the notes;
both restatement references are generic "regrouped/reclassified
wherever necessary" boilerplate carrying no rupee amount (B02
restatements_found). The one concrete cross-note number discrepancy
found -- Note 29's FY25 comparative (Rs 0.1 Lakh) against Note 7/Balance
Sheet's own FY25 figure (Rs 13.4 Lakh) in the same filing -- reads as a
drafting/transcription error, not a disclosed restatement (B02 Pass 1
Finding).

### Q7. CORPORATE-ACTION CLAUSES

No merger, demerger, scheme of arrangement, buyback or preferential
issue exists in this corpus. The one substantive corporate action found
is the variation in utilisation of unutilised IPO proceeds, disclosed
with a direct internal conflict on mechanism and date.

Quote (MD&A, AR p.27): "Following shareholder approval obtained at the
Extraordinary General Meeting held on 17 April 2026, the remaining
unutilised balance of ₹764.51 Lakhs was reallocated towards working
capital requirements."

Quote (Directors' Report, AR p.35, immediately after its own "no
material changes" line): "the Members of the Company, by way of a
Special Resolution passed through Postal Ballot on 29 April, 2026,
approved the variation in the utilisation of the unutilised proceeds of
the Initial Public Offer ('IPO'). The Company had raised Rs. 3,040.96
Lakhs through its IPO pursuant to the Prospectus dated September 25,
2024. As on the date of seeking members' approval, an amount of
₹764.51 Lakhs remained unutilised, comprising ₹364.51 Lakhs originally
earmarked for funding capital expenditure towards purchase of new plant
& machinery and software and ₹400.00 Lakhs allocated towards pursuing
inorganic growth initiatives through acquisitions."

Quote (Directors' Report, AR p.35, the "no material changes" line
itself): "There have been no material changes and commitments, affecting
the financial position of the Company which occurred during the period
between the close of the financial year 2025-26 and the date of this
report."

Comment: Two different mechanisms and two different dates describe the
same event across the same filing -- an Extraordinary General Meeting on
17-Apr-2026 (MD&A, Note 32) versus a Postal Ballot with results on
29/30-Apr-2026 (Directors' Report x2, Secretarial Audit Report) (B03
red_flags_top3; B08 adverse_findings). The ratio: Rs 764.51 Lakh
redirected = Rs 364.51 Lakh (unspent capex object) + Rs 400.00 Lakh
(acquisition object), against total IPO proceeds of Rs 3,040.96 Lakh --
25.1% of gross proceeds. The rupee amounts and the 25.1% ratio tie out
consistently everywhere they appear; only the approval mechanism and
date conflict. The Directors' Report's own "no material changes"
sentence sits two sentences before it discloses this same event within
the same reporting window, an internal materiality-judgment
inconsistency (B02 Pass 3 finding).

### Q8. RELATED-PARTY PERIMETER

Quote (Note 28, Related Party Disclosure, AR p.66-67): "Related parties:
Mansi Dalal, Manray Foundation, Vijay Dalal. Key management personnel:
Gaurav Dalal (Managing Director), Padma Madhusudan Lohiya (Director),
Dayaram Paliwal (Director), Dinesh Gopal Mundada (Director)."

Quote (same note, FY26/FY25 Rs Lakh): "Directors Remuneration to Mansi
Dalal 28.0 / -. Rent to Mansi Dalal 2.6 / 2.9. Salary to Gaurav Dalal
62.0 / 48.0. Loan Received from Gaurav Dalal 38.5 / 369.0. Loan repaid
to Gaurav Dalal 24.7 / 377.1. Salary to Vijay Dalal 12.0 / 12.0.
Director Remuneration to Padma Madhusudan Lohiya 1.8 / 2.0. ... Total
173.2 / 814.9."

Quote (Annexure D, Section 197 disclosure, AR p.48): "Managing
Director... Rs.48,00,000/- [FY25] ... Rs.62,00,000/- [FY26] ... 29%"
[Gaurav Dalal]; "[Mansi Gaurav Dalal] Non-Executive Director ... 00.00
... Rs.48,00,000/- ... 100%"; ratio to median employee remuneration for
Mansi Gaurav Dalal: "18.42".

Comment: Note 28's RPT figures (Rs 28.0 Lakh directors' remuneration +
Rs 2.6 Lakh rent = Rs 30.6 Lakh to Mansi Dalal, FY26) do not equal
Annexure D's Section 197 remuneration figure for the same person
(Rs 48.0 Lakh, FY26); the two notes use different disclosure bases and
the gap is not reconciled anywhere in the filing (a further instance of
the cross-note inconsistency pattern B02/B03 document elsewhere). The
promoter (Gaurav Dalal) is also a net lender to the company in FY26
(Rs 38.5 Lakh advanced against Rs 24.7 Lakh repaid, a shrinking residual
of a much larger Rs 369.0 Lakh FY25 bridge) (B08 transition_evidence).

### Q9. PLEDGE AND SHAREHOLDING

Quote (Reg 31(4) declaration, filed 25-May-2026, covering FY25-26): "I,
Gaurav Vijay Dalal, Promoter of Rappid Valves (India) Limited, hereby
declare that, I along with person acting in concert, have not made any
encumbrance, either directly or indirectly during the financial year
2025-26." (p.2 of the filing; B08 corroborates a parallel FY25
declaration dated 07-Apr-2025).

Quote (Note 3.7, Shares held by Promoters & Promoters Group, AR p.60):
"Gaurav Dalal 24,90,436, 47.97%, 0.00% [change]... Vijay Dalal 1,87,500,
3.61%, 0.00%... Total 26,77,936, 51.58%, 0.00%" -- identical at both
31-Mar-2026 and 31-Mar-2025.

Comment: Promoter pledge is zero and stable; only two Reg 31(4) annual
declarations exist in the corpus (FY25, FY26) because the company has
been listed under two years -- twelve quarters of pledge history do not
exist for a company listed 30-Sep-2024. Promoter holding was unchanged
at 51.58% across the one full post-listing year covered by the AR's own
Note 3.7 table; the earlier, larger pre-issue-to-listing drop (from
69.46% pre-issue per the RHP to 51.58% post-listing, an IPO-dilution
event, not a sale) sits outside this one-year AR table (B01 data_notes
G22). Institutional (FII/DII) holding at 31-Mar-2026 is carried in
`inputs/shareholding/SHP_31-MAR-2026.xml` (XBRL) and the four earlier
XBRL filings; this pass did not parse the XBRL payload for a percentage
figure, so it is recorded here as NOT EXTRACTED THIS PASS rather than
NOT DISCLOSED -- the filing exists and should be opened directly for
this figure at the next extraction cycle.

### Q10. VERIFICATION

Documents quoted in this annex, with filename and date:
- `Annual_Report_2026.pdf` (FY26 Annual Report, signed 29-Aug-2026)
- `01Feb2025_RAPPID_01022025120242_RappidQIA.pdf` (Reg 30 business
  update, 01-Feb-2025)
- `Concall_Jun_2026_Transcript.pdf` (earnings call, 01-Jun-2026)
- `10Jul2026_RAPPID_10072026150526_GBU_Rappid_Signed.pdf` (Q1 FY27
  business update, revised 10-Jul-2026)
- `25May2026_team_sandeshc_29042026124914_40.pdf` (Reg 31(4) pledge
  declaration, filed 25-May-2026, covering FY25-26)
- `27May2026_RAPPID_27052026180012_BM_Outcome.pdf` (FY26 audited
  results, 27-May-2026), cited via B03/B05 for cross-reference
- `Rappid_Valves_RHP_Sep2024.pdf` (Red Herring Prospectus, Sep-2024),
  cited via B01 for the pre-issue promoter-holding cross-check
- `inputs/shareholding/SHP_31-MAR-2026.xml` and four earlier XBRL
  filings (Sep-2024 x2, Mar-2025, Sep-2025), named but not parsed this
  pass (Q9)

CORPUS COMMIT HASH: 074a32392097043632952df0c555f89a332f9773
