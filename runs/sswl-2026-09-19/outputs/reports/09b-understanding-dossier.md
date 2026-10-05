# SSWL (Steel Strips Wheels Ltd) — HALT 1 UNDERSTANDING DOSSIER

Run: sswl-2026-09-19. Assembled from committed blocks B00-B09, B12a-d, confidence-delta
and B13-synthesis-lite. No new research, no web search, no re-analysis. Every claim
below traces to a block. No valuation, price, or verdict vocabulary appears except the
one scoped exception in Section 2 Part B4. The Mental Model Declaration in Section 2 is
a DRAFT. Nothing here is signed.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

**Empty-folder record (repeated per the run's injected instruction):** `research/` is
EMPTY (no broker notes held; B00 input_gaps: "research: EMPTY. No broker notes. No
effect on anchored evidence."). `prospectus/` is EMPTY and not expected (SSWL is a
long-listed company; B00 input_gaps: "prospectus: EMPTY. Long-listed company; not
expected; not a gap.").

1. **CONCALLS.** Three transcripts held inside the run's stated contract: Q3 FY26
   (23-Jan-2026), Q4 FY26 (02-Jun-2026), Q1 FY27 (16-Jul-2026). A fourth, Q2 FY26
   (13-Nov-2025), sits in `other/` as a backward check beyond the contract (B00). Most
   recent quarter covered: **Q1 FY27** (quarter ended 30-Jun-2026). Against the run
   date (2026-09-19), the next quarter (Q2 FY27, ended 30-Sep-2026) has not yet closed,
   so no plausibly-reported transcript is absent; the next one due is Q2 FY27, expected
   with results around Nov-2026 (B13-lite `cash_missing_evidence`).
2. **ANNUAL REPORTS.** Only the FY26 Annual Report is held (Reg 34 filing, 03-Sep-2026,
   245pp incl. the 40th AGM notice; B00). It carries FY25 comparatives inside it, but
   the FY25 Annual Report itself, and the FY24 Annual Report, are NOT in the corpus
   (B01, B02, B03, B04 all name this gap; it blocks the FY24 AMW NCLT gain breakup and
   the FY25 reserve-transfer comparative). The latest completed FY (FY26, year ended
   31-Mar-2026) IS present. Fewer than 3 years of AR are held — only one.
3. **RESULTS FILINGS.** Latest: Q1 FY27 (15-Jul-2026). Also held: Q4 FY26 / FY26
   audited (29-May-2026), Q3 FY26 (22-Jan-2026), and Q2 FY26 (12-Nov-2025, in `other/`)
   (B00). No quarter-gap exists between the latest results filing (Q1 FY27, quarter
   ended Jun-2026) and the latest AR (FY26, year ended Mar-2026); the AR sequentially
   follows the audited FY26 results.
4. **INVESTOR PRESENTATIONS.** Four decks held: Jan-2026 (Q3 FY26), May-2026 (Q4 FY26,
   filed 01-Jun-2026), Jul-2026-A (Q1 FY27, 15-Jul-2026), and Jul-2026-B (a second,
   distinct Jul-2026 deck BSE filed under "Earnings Call Transcript") (B00). Latest:
   Jul-2026-A, 15-Jul-2026.
5. **RESEARCH / RATING.** The India Ratings rationale of 18-Feb-2026 (Reg 30 filing,
   IND AA-/Stable affirmed) is held, full text readable (B00). No broker research note
   of any kind is held (`research/` EMPTY, see above).
6. **CORPORATE ACTIONS.** 45 Reg 30 filings, Oct-2025 to Sep-2026, held (B00),
   including CFO and Deputy MD changes, the Echanda Urja captive-power investment, two
   MoU disclosures, the Customs show-cause notice, and the Sep-2026 promoter SAST
   purchases.
7. **FRESHNESS PAIR CHECK.** All four pairs PASS (B00 `freshness_pairs`): RESULTS to
   CONCALL (Q1 FY27 results paired with the Q1 FY27 transcript); RATING BULLETIN to
   RATIONALE (same PDF carries both); SEBI ORDER to ORDER TEXT (no SEBI order exists in
   the corpus; the one show-cause notice found is a Customs matter, not SEBI); AR to
   LATEST AUDITED ANNUAL RESULTS (the FY26 AR postdates the FY26 audited results by
   little over 3 months). `freshness_verdict: FRESHNESS PAIRS OK` (B00). No pair failed;
   nothing to restate here.
8. **VERDICT LINE: CORPUS GAPPED.**
   - FY25 Annual Report — findable-but-missing (BSE, scrip 513262). Closes the AMW gain
     breakup and the FY25 reserve-transfer comparative (B02, B03, B04).
   - FY24 Annual Report — findable-but-missing (BSE, scrip 513262). The only route to
     LBF4's ~Rs 138 Cr AMW consideration figure and the exceptional-gain journal
     (B01, B03, B04).
   - Screener export sheets (P&L / Balance Sheet / Cash Flow / Quarters, for SSWL and
     all three peers) — findable-but-missing on the operator's own machine (Financials.xlsx
     needs to be opened and saved once, then `collect_to_repo.py --push-again`; B00, B01).
   - Debtor-factoring note / bill-discounting disclosure (Rs 400-500 Cr limit named on
     two concalls) — plausibly-nonexistent in the FY26 AR itself (a full-text search of
     the AR for "factor"/"bill discounting" found nothing; B04) but findable via a
     direct management question or the FY25 AR.
   - Broker / research coverage — findable-but-missing status unresolved; the corpus
     holds none and B00 records no independent confirmation that no broker covers the
     name, only that the run's `research/` folder came back empty.
   - The Freshness Pair Check itself is clean, so this verdict is `CORPUS GAPPED`, not
     `CORPUS GAPPED-FRESHNESS` (B00 `freshness_verdict: FRESHNESS PAIRS OK`).

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT - PENDING OPERATOR SIGN-OFF.** Nothing in this section is signed. Signing
happens only in claude.ai after live-web stress-testing.

### PART A — THE FROM STATE (the anchor, not the model)

**A1. ARCHETYPE.**
- Steel wheels (63% of FY26 revenue, B04): **Commodity converter** (CLAUDE.md
  archetype library). B04 describes this line as "manufactured, OEM-spec,
  cost-plus-conversion with raw-material pass-through"; pricing power is scored
  `weak` and cyclicality `cyclical` (B04).
- Alloy wheels + aluminium knuckles (36% + ~1% of FY26 revenue, B04): **Build-to-spec
  component maker** (CLAUDE.md archetype library). Same raw-material pass-through
  mechanics as steel (B04), but riding an OEM design-win/platform-qualification
  pipeline that B07 scores "Qualification lock-in" Strong (evidence type MANAGEMENT
  CLAIM, B07 active_categories).

**A2. THE SIMPLE ANALOGY.** SSWL is the workshop that makes the wheel a car rolls on,
but it never sells to the driver directly. It sells to Maruti Suzuki, Hyundai, Tata
Motors and the rest, who bolt the wheel onto the car before it reaches the showroom.
For most of its history SSWL made steel wheels: cheap, tough, and it simply passes the
price of steel through to the carmaker, the way a tailor charges for the cloth on top
of the stitching (B04). It is now also building aluminium alloy wheels and steering
knuckles, parts that cost more to make and sell for more, at a new plant in Bhuj,
Gujarat (B04, B07). Stopping the description here, at what the business is today,
misses the point of this section: the model is the arrow, not the anchor.

### PART B — THE TRANSITION (the model)

**B1. FROM to TO.**
- Steel wheels: FROM **R1 COMMODITY PRICE-TAKER** TO **R2 COST-ADVANTAGED CONVERTER**.
  The backward integration into hot rolling, the Tata Steel supply relationship, the
  captive renewable power investment, and the ~25.7 Mn combined capacity base (the
  broadest product span of any listed maker) already give this line a moderate
  cost-advantage and efficient-scale moat (B04 `moats_present`); the FROM anchor is a
  plain steel converter, the claimed present state already sits closer to R2.
- Alloy wheels + knuckles: FROM **R2 COST-ADVANTAGED CONVERTER** (same
  raw-material-pass-through starting mechanics as steel, just a higher ASP) TO **R3
  VALUE-ADDED / SPEC'D SUPPLIER** (spec-in and switching costs from OEM platform
  qualification, giving partial pricing power). This is the claimed destination, not a
  proven one; see B3 and B6.

**B2. THE ENGINE.** Two things physically change: (1) OEM platform-qualification wins
route incremental volume into higher-ASP alloy and knuckle capacity, concentrated at
the new Bhuj plant (1.2 Mn alloy wheels, up to 1.1 Mn knuckles, ~Rs 420 Cr capex, B05
guidance table; B07 catalysts); (2) the product mix inside total volume shifts from
steel toward alloy and knuckle, which management says lifts blended per-wheel
realisation and, it claims, blended EBITDA per wheel (B04 `unit_economics`).

**B3. THE PROOF GATE.** Management has stonewalled the one disclosure that would prove
this cleanly — a steel-versus-alloy EBITDA-per-wheel split — in every quarter it has
been asked (Q2 FY26, Q3 FY26, Q1 FY27; B05 `FLAG-STONEWALL`). Absent that split, the
proof gate Stage 11 FTTCP must test is a **joint** print: blended EBITDA/wheel holding
at or above **Rs 310/wheel** (B05 `confirm_signal`, priority-1 trigger) **in the same
quarter** that the alloy revenue share moves off its current **35-37% stall band**
observed across four consecutive quarters (B12b independent reread). A high EBITDA/wheel
number with alloy share still flat is a price effect, not the claimed mix engine; only
the joint print separates them.

**B4. THE RECOGNITION GAP (open question, to be resolved at Stage 11).** Whether the
market has already priced the claimed R2-to-R3 climb in alloy and knuckles is an open
question this dossier does not answer. Stage 11 resolves it via the destination-PE gap
under Section 1B. If the TO state is already reflected in current pricing, the
re-rating engine behind the transition is spent and only underlying earnings growth
would remain; this dossier states no number and no conclusion either way.

**B5. THE UGLINESS TEST.** Today's ugly optic is the FY26 cash-conversion collapse:
standalone CFO/EBITDA fell from 103.5% (FY25) to 63.3% (FY26), AR basis (B03), against
a backdrop of a Rs 676.50 Cr reverse-factoring Supplier Finance Arrangement covering
67.6% of trade payables (first-year disclosure, B02 Note 25) and a separate Rs 400-500
Cr debtor-factoring facility that surfaces only on two concalls, never in the AR (B05,
B13-lite). Two readings compete. GROWTH-INDUCED (ARTIFACT-OF-CLIMB): revenue grew 17%
in FY26 and 27% in Q1 FY27 (B05), inventory built ahead of exports, a capex cycle is
underway, and FY25 conversion was above 100% (B03) — a one-year effect of fast growth,
not a durable feature. STRUCTURAL (STRUCTURAL-FEATURE): payable days stretched
69.29→75.64 in a confirmed **two-year** accelerating trend (B02 Note 48e), not a
one-year event; MSME overdue-and-unpaid principal nearly doubled (B02); and two
separate off-balance-sheet financing lines already sit underneath the reported 63%
figure. **Classification: STRUCTURAL-FEATURE (provisional).** The two-year accelerating
trend and two independent financing supports outweigh the one-year growth story on the
evidence read so far, but the pipeline's own cash determination is explicitly
`INDETERMINATE` (B13-lite `cash_determination`), and this classification is contested,
not settled. The observation that separates the two readings: H1 FY27 CFO/EBITDA above
80% of AR-basis EBITDA supports GROWTH-INDUCED; below 65% supports STRUCTURAL (B03
monitorable; B13-lite `falsification_metric`), due with the Q2 FY27 results filing
expected around Nov-2026.

**B6. THE TRANSITION FALSIFIER.** Evidence that kills the TRANSITION thesis
specifically (not the business): a disclosed or credibly-inferable product-level split
showing alloy/knuckle EBITDA/wheel at or below steel's, sustained across quarters; or
blended EBITDA/wheel that keeps tracking input-price cycles (aluminium/LME moves) while
alloy revenue share stays pinned at 35-37% for a further two-plus quarters (B05, B12b).
Peer WHEELS already reports its own alloy-wheel business as its lowest-ROI segment
(B06) — a live analog of exactly this falsifier, not yet confirmed or denied for SSWL.

### PART C — WHAT THE MODEL WATCHES (derived from the transition)

**C1. DOMINANT VARIABLES.**
1. Blended EBITDA/wheel, and whether it moves with alloy share or with input-price
   cycles. Current state: Rs 314/wheel (Q1 FY27) vs Rs 262/wheel (Q1 FY26), alloy share
   stalled at 35-37% across the four quarters read (B05, B12b).
2. Alloy + knuckle revenue share of total revenue. Current state: ~36% FY26 (B04), a
   rise from ~28% FY24 that has since stalled (B12b).
3. Bhuj capacity commissioning and OEM approvals. Current state: capex committed
   (~Rs 420 Cr), trial-production guidance already slipped once, from an Oct-2026 read
   to Q4 FY27, roughly a 4-5 month delay against the MD's own internal plan (B07, B12b).
4. Cash conversion, CFO/EBITDA. Current state: 63.3% FY26 standalone AR basis, down
   from 103.5% FY25, INDETERMINATE classification (B03, B13-lite).

**C2. WHAT THE MODEL REJECTS.** Market-size adequacy is not the binding constraint.
B09's TAM/SAM/SOM work shows a GOOD runway class, headroom of 3.49x SSWL's current SAM
share, and a market growing ~8.5% p.a. (B09). The bull case's binding constraints are
execution and disclosure — the withheld product margin split, the Bhuj timeline, cash
conversion — not the size of the pond. Separately, the model rejects SSWL's own
decade-out ambition of exporting more than it sells domestically (company memory
LBF1's long horizon) as a near-term signal: B09 found no independently sized export TAM
to test it against, so it is noise for THIS transition read until the nearer-term H2
FY27 export run-rate (B09 §5D) delivers a testable data point.

**C3. THE BUSINESS FALSIFIER.** Distinct from B6, this is evidence that would force
re-declaring the FROM business itself, not just the climb. Candidates: loss of a
top-tier OEM platform (the AR itself names "top customer concentration is a risk," AR
p.124 per B04) that erodes the qualification-lock-in moat the whole ladder position
rests on; or a durable break in the Tata Steel raw-material/technology relationship
that underlies the cost-advantage moat (B04); or the AMW Autocomponent cluster (three
years of subsidiary losses, a Rs 59.31 Cr DTA with no forecast support, an adverse CARO
land-title finding, and two years of unexplained reserve transfers totalling over
Rs 1,000 Cr, all under zero Key Audit Matters from a regional auditor — B02, B03, B08)
crystallising into a material capital loss that forces a re-read of SSWL not as a
disciplined converter climbing the ladder, but as a group with weak capital-allocation
control at the parent level.

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

*(As specified in prompts/13-synthesis-pipeline.md, BUSINESS UNDERSTANDING NARRATIVE
section — the shared five-question spec. Drafted at Halt 1 from B01-B09; Stage 13's
copy is the final version, updated by later stages.)*

Steel Strips Wheels makes wheel rims for vehicle makers, and in small volume it makes
aluminium steering knuckles (B04). Steel wheels bring about 63% of revenue and go on
trucks, tractors, cars, off-road equipment and two- and three-wheelers; the rating
agency puts the company's share of each domestic steel-rim segment between 34% and 52%
(B04, Ind-Ra rationale via B04). Alloy wheels bring about 36% of revenue: cast aluminium
rims, mostly for higher-trim cars, selling for roughly Rs 4,730 a wheel against roughly
Rs 2,070 for a steel wheel (both derived, B04 `unit_economics`). Knuckles are about 1%
of revenue with two customers (B04). Every part is built to the vehicle maker's
specification and approved for one platform, so a buyer switching supplier must first
put a new part through approval — the switching-cost basis of the moat B07 scores
"Qualification lock-in" Strong (B04, B07).

The buyers are named OEMs: Maruti Suzuki, Hyundai, Mahindra, Honda, Kia, MG, Tata
Motors, Ashok Leyland, Honda's two-wheeler arm, Suzuki Scooters, and tractor/equipment
makers including Sonalika, Escorts, JCB and New Holland (B04). The investor deck claims
large shares of individual buyers' purchases — 96% at Suzuki Scooters, 64% at Ashok
Leyland, 58% at Tata Motors — but no audit or contract stands behind those percentages;
B07 separately flags this as the weakest-evidenced part of the moat claim (B04, B07
`FLAG-UNVERIFIABLE-LOCKIN`). Plants sit next to customer assembly lines: Jamshedpur
(Tata Motors), Mehsana (Hyundai) (B04). Exports run 7-9% of revenue depending on the
basis used (B04).

Demand today follows vehicle output. The signals are SIAM's monthly production and
sales release, TMA/FADA tractor data (tractors are 13% of FY26 revenue), and the
monthly sales of named customers Tata Motors and Hyundai Motor India — all named
downstream candidates in B09's Section 6. All three listed peers independently confirm
that the GST 2.0 cut of late September 2025 lifted demand for cars, trucks, tractors
and two-wheelers at the same time SSWL reports it (B06 `industry_cross_read`).

Demand should grow for two forward-looking reasons, each tied to an externally
verifiable signal. First, cars are moving from steel to alloy wheels; management
expects the alloy market to grow ~12% a year and steel ~4% a year for five years, a
claim a third-party report corroborates at ~10.1% for alloy (B09). Second, exports
should recover if US Section 232/reciprocal tariff treatment of India, relative to
Vietnam and Thailand, settles favourably, and if EU CBAM costs on Europe-bound wheels
stay small — both checkable against the Federal Register and EU CBAM registry updates
named in B09's downstream candidates. The LME aluminium price sets alloy-wheel and
knuckle input cost, passed through with a lag (B04); Bhuj is the capacity being built to
capture the shift (B07).

The competitive advantage sits differently by line. Steel wheels carry a moat of
moderate depth: segment shares of a third to a half, the widest product range of any
listed maker, and a long-standing steel supply tie to Tata Steel (B04, B07 categories
B1, F2, H2). Alloy wheels have no proven moat at the company-wide level: the claim that
buyers cannot leave rests only on management's own percentages (B07
`FLAG-UNVERIFIABLE-LOCKIN`), management told two different analysts on two different
calls that domestic alloy margins are "crashing" under competition and, separately,
expanding at every segment (B12b), and peer WHEELS calls its own alloy business its
lowest-return segment (B06). Knuckles are too new and too small to carry a moat yet.
The forward moat scan scores the business MODEST overall at 17 (B07); the run did not
establish separate scores for scan Categories 21 and 22 (B07 `active_categories`).

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. Verticals framed

**Vertical 1 — EBITDA/wheel and alloy share (price vs mix).** What the corpus
establishes: blended EBITDA/wheel rose Rs 262 (Q1 FY26) → Rs 314 (Q1 FY27) (B05);
alloy revenue share rose ~28% (FY24) → ~36% (FY26, B04) but has stalled at 35-37%
across the four most recent quarters read (B12b); the AR carries no product-level
split (single Ind AS 108 segment, Note 44, B02/B03); management stonewalled a direct
split request three times, once citing "trade secrets" (B05 `FLAG-STONEWALL`; the
concall itself records: "I cannot mention anything to you because I do not want to
reveal my trade secrets to you," Q3 FY26 transcript, in response to an analyst's floated
~Rs 450/wheel alloy-EBITDA figure that management never denied). What it cannot
establish: whether the Rs 314 print reflects genuine mix (more alloy volume) or price
(input-cost pass-through / negotiated increases) or both (B12b flags this exact
ambiguity unresolved). Questions: (1) does Q2 FY27 show EBITDA/wheel holding ≥Rs 310
together with alloy share breaking the 35-37% band? (2) will management ever disclose
the steel-vs-alloy split? (3) does the floated ~Rs 450/wheel alloy premium survive an
LME aluminium price move?

**Vertical 2 — Alloy + knuckle revenue share.** What the corpus establishes: alloy
~36% of FY26 revenue (B04); knuckles ~1%, two customers, FY27 knuckle revenue guided
Rs 110-130 Cr (B05); all three peers are simultaneously expanding alloy/aluminium
capacity (B06 `industry_cross_read`: "INDUSTRY-WIDE CAPACITY RACE"). What it cannot
establish: whether SSWL's alloy share resumes rising past the current stall or is
hitting a near-term ceiling from rising competitive supply. Questions: (1) does alloy
share move past 37% in the next two quarters? (2) does the knuckle customer count grow
beyond two, per B07's optionality register item "two additional knuckle OEM wins"? (3)
does rising peer alloy capacity compress SSWL's realised alloy ASP?

**Vertical 3 — Bhuj commissioning and OEM approvals.** What the corpus establishes:
~Rs 420 Cr capex for 1.2 Mn alloy wheels plus up to 1.1 Mn knuckles (B05); named
Chinese technology partners Liuzhou Arays Technology and Hainan Jihoo, first appearing
in this AR (B03 `ar_new_downstream_entities`); B12b's independent reread finds the
guided trial has moved to Q4 FY27, a 4-5 month slip against the MD's own internal
timeline (B12b). What it cannot establish: whether Bhuj's output will be OEM-qualified
supply or export-aftermarket-only; B12b flags a reframing on the Q1 FY27 call toward
"export aftermarket... with Arays technical support," against the earlier "sold
out"/OEM-approval framing (B12b). Questions: (1) does a Reg 30 filing or a call confirm
actual trial output and OEM sign-off by Q4 FY27? (2) does Bhuj's stated purpose settle
between calls? (3) does the second, currently uncommitted capex cycle B09's 5-year SOM
requires ever get named?

**Vertical 4 — Cash conversion (CFO/EBITDA).** What the corpus establishes: standalone
CFO/EBITDA fell 103.5% (FY25) → 63.3% (FY26), AR basis (B03); a Rs 676.50 Cr
reverse-factoring Supplier Finance Arrangement covers 67.6% of trade payables,
first-year disclosure (B02, Note 25); a separate Rs 400-500 Cr debtor-factoring
facility surfaces only on two concalls, never in the AR (B05, B13-lite); payable days
stretched 69.29→75.64, a confirmed two-year accelerating trend (B02, Note 48e); year-end
standalone cash was Rs 6.5 Cr (B03). What it cannot establish: whether the FY26
collapse is a one-year growth/capex effect or the start of a structural dependence on
the two financing lines (B13-lite `cash_determination: INDETERMINATE`). Questions: (1)
does H1 FY27 CFO/EBITDA print above 80% or below 65% of AR-basis EBITDA? (2) what are
the debtor-factoring and supplier-finance balances at 31-Mar-2025, both currently
missing (B13-lite `cash_missing_evidence`)? (3) does the Supplier Finance Arrangement
grow beyond Rs 676.50 Cr, or the debtor facility beyond the Rs 400-500 Cr limit (B03
monitorables)?

### 4b. Candidate signal table

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| SIAM monthly domestic vehicle production/sales (PV/CV/2W/3W) | Domestic volumes contract while SSWL's steel-wheel revenue keeps growing, implying share gain rather than sectoral demand, or both decline together, breaking the sectoral-tailwind read | Monthly | SIAM monthly press release (B09) |
| TMA/FADA tractor wholesale and retail data | Tractor wholesale falls while SSWL's tractor-segment revenue (13% of FY26 revenue) holds flat or rises, implying channel stuffing rather than end demand | Monthly | TMA / FADA monthly releases (B09) |
| Tata Motors PV+CV volume and capex disclosures | Tata Motors volume or capex guidance falls while the Jamshedpur-adjacent CV wheel relationship is assumed stable | Monthly | Tata Motors investor disclosures (B09) |
| Hyundai Motor India PV sales and model mix | Hyundai's alloy-trim mix share falls, undercutting the alloy-adoption assumption behind the mix-shift engine | Monthly | Hyundai Motor India sales release (B09) |
| Domestic/LME aluminium price index | A sustained LME spike coinciding with a still-rising blended EBITDA/wheel would support the price-not-mix reading Vertical 1 leaves open | Monthly | LME / MCX aluminium price series (B09) |
| US Section 232 / reciprocal tariff rate on Indian auto exports | A fresh tariff escalation in the Federal Register kills the export-recovery trigger | Event-driven | USTR / Federal Register tariff notices (B09; B05 trigger 3 kill_signal) |
| EU CBAM implementation updates | A CBAM cost disclosure, already quantified by peer WHEELS but never by SSWL, surfaces as a material cost on SSWL's own Europe-bound exports | Event-driven | European Commission CBAM registry (B09; B06 `risks_peers_raise`) |

These candidates are UNVERIFIED. Verification and tracker writes happen at Role 5.5 in
claude.ai, unchanged.

### 4c. Fragility read

- **variable_count: 7** — the seven forward triggers B05 names for the bull case:
  input-price pass-through lifting EBITDA/wheel; Bhuj capacity commissioning; export
  recovery; steel-wheel demand reflation; FY27 revenue growth of ~25%; EV-scooter wheel
  dominance; hot-stamping/new-product diversification (B05 `triggers`).
- **verifiability_ratio: 5 of 7 externally observable** — input-price pass-through (LME
  and steel indices, cross-checked against peer commentary, B06), Bhuj commissioning
  (Reg 30 filings, OEM approval announcements), export recovery (Federal Register
  tariff notices, India export data), steel-wheel reflation (SIAM/TMA data), and FY27
  revenue growth (quarterly exchange-filed results) are all externally checkable; EV-scooter
  wheel dominance (~80% share claimed) and hot-stamping diversification are
  company-narrated only, confirmed by no peer transcript (B06 `unverifiable`).
- **single_point_failure:** none for the whole bull case — failure requires
  conjunction across the demand, cost and execution variables. But the mix-shift ENGINE
  specifically (Part B2) has one live single point: a disclosed or credibly-inferable
  product-level split showing alloy/knuckle EBITDA/wheel at or below steel's would alone
  falsify the TRANSITION thesis (Part B6), even though it would not by itself falsify
  the underlying steel-wheel business (Part C3).
- **fragility_verdict: MODERATE.** The steel-wheel base has externally verifiable
  demand and cost drivers and real, if moderate, moat evidence (B04, B07). But the
  engine central to the claimed TO state rests on the one metric management withholds
  (B05 `FLAG-STONEWALL`), and cash conversion is INDETERMINATE with two off-balance
  financing lines already supporting the reported figure (B02, B13-lite). Not FRAGILE,
  because multiple confirm/kill signals are already tracked and peer data corroborates
  the demand and cost sides (B06); not ROBUST, because the one transition-specific
  metric is exactly the one thing withheld.

### 4d. Research brief

1. **[PENDING LIVE VERIFICATION, Chain 1 below]** OEM-side alloy-wheel trim-mix
   disclosures (Maruti Suzuki, Hyundai Motor India investor materials) to test whether
   rising alloy adoption at the customer level is independently confirmed, not just
   SSWL's own claim.
2. **[PENDING LIVE VERIFICATION, Chain 2 below]** USTR Federal Register tariff notices
   on Indian auto-component/wheel exports versus Vietnam/Thailand, to test the
   Southeast Asia tariff-edge claim management raised on one call and reversed the next
   (B07 `FLAG-CONTRADICTED-CLAIM`).
3. FY25 and FY24 Annual Reports (BSE, scrip 513262) — closes the AMW NCLT gain
   breakup, the ~Rs 138 Cr consideration, and the FY25 reserve-transfer comparative
   (B02, B03, B04).
4. Debtor-factoring balance at 31-Mar-2025 and 31-Mar-2026, and supplier-finance
   balance at 31-Mar-2025 — management question or the FY25 AR (B13-lite
   `cash_missing_evidence`).
5. AACL land-title registration status under the AMWL demerger scheme — direct
   management question or next AR update (B02 Finding 7; B03 `FLAG-AMW-ADVERSE-CARO`).
6. Customs show-cause notice (17-Jun-2026, Mundra) resolution/outcome — next Reg 30
   filing (B03 `FLAG-MISSING-DISCLOSURE`; B08).
7. Indian alloy-wheel market structure ("only 2 serious players" claim) — independent
   trade/industry source; no peer transcript confirms it (B06 `unverifiable`).
8. SSWL's claimed ~80% EV-scooter wheel share and ~30% ICE 2W/3W share — independent
   industry source; unconfirmed by any peer (B06 `unverifiable`; B07 optionality
   register).
9. Next India Ratings review, on adjusted net leverage (3.2x at 9MFY26 versus Ind-Ra's
   own 2.5x positive-trigger threshold, B04 `must_track_metrics`).
10. MCA/RoC direct DIN-disqualification lookup for directors (B08 `searches_skipped`
    relied only on the AR's own self-declaration).
11. Proxy advisory (IiAS/SES/InGovern) governance opinion, if one exists, given the
    Audit Committee Chairman's low FY26 attendance (B08 §3D; a direct fetch was not
    completed).
12. AmbitionBox employee-review cross-check for SSWL specifically (B08 `input_gaps`:
    the SSWL-specific page could not be retrieved; only Glassdoor was used).
13. Screener P&L / Balance Sheet / Cash Flow / Quarters export sheets — operator-side
    fix (open Financials.xlsx, save it, re-run `collect_to_repo.py --push-again`; B00,
    B01).
14. H1 FY27 cash flow statement, once filed with Q2 FY27 results (~Nov-2026) — the
    single sharpest test named across B03, B13-lite and this dossier's Vertical 4.

### 4e. Second-order stub (Master Prompt v3.7, Rule F)

Rule F sets a floor of FIVE chains for Role 2, Role 6 and FTTCP. Halt 1 is earlier than
all three and has no live web, so it carries a STUB: the first TWO chains, drafted from
corpus, for Claude web to extend to the Rule F floor with live-web links.

```
CHAIN 1: Alloy revenue share rose from ~28% (FY24) to ~36% (FY26) while blended
EBITDA/wheel rose from Rs 262 to Rs 314 in Q1 FY27, even as full-year EBITDA margin
fell from 12.7% (FY22) to 9.9% (FY26) (B04, B05).
Link 1 [CLAIM]: Management states alloy wheels carry a materially higher ASP (~Rs 4,730
per wheel derived, versus ~Rs 2,070 for steel, B04) and frames the OEM shift toward
alloy trim as an industry-wide styling and lightweighting trend (B04 unit_economics).
Link 2 [DOC]: The AR discloses no product-level segment split (single Ind AS 108
segment, Note 44, standalone AR p.173-174) and management has stonewalled the direct
steel-vs-alloy EBITDA/wheel split in every quarter asked, including a "trade secrets"
refusal on the Q3 FY26 call (B02 Finding 14; B05 FLAG-STONEWALL).
Link 3 [INFERENCE]: If the split were flattering to SSWL, disclosing it would
strengthen the investment case at low competitive cost, since peers already discuss
segment-level alloy economics in some form (B06). Three-plus quarters of repeated
refusal is more consistent with the split being unflattering, or genuinely commercially
sensitive in a way peers' disclosures are not, than with simple oversight.
Binding constraint: Working-capital intensity of the alloy/knuckle ramp is rising faster
than the steel-wheel base did: inventory +28.2% YoY, receivables +25.2% YoY against
11-17% revenue growth (B02), and FY26 standalone CFO/EBITDA fell to 63.3% (B03) — a real
cost of the climb the EBITDA/wheel number alone does not show.
Unsaid: Note 44's single-segment disclosure and the AR's MD&A narrative both frame SSWL
as one integrated wheel business; nowhere does the AR or the four decks discuss alloy
wheel profitability risk, even though peer WHEELS calls its own alloy business its
lowest-ROI segment (B06) — a comparison SSWL's own materials never raise.
Observation that confirms or breaks this chain, and confirm-by date: the Q2 FY27
deck/concall (expected on or after mid-Nov-2026, per B00's quarterly filing cadence).
If alloy revenue share moves off the 35-37% stall band in the same quarter that blended
EBITDA/wheel holds at or above Rs 310, the mix reading is confirmed. If EBITDA/wheel
holds only when input prices rise while alloy share stays flat, the chain breaks and
the engine is repriced RM pass-through, not mix.
Who pays, and why now: PENDING LIVE VERIFICATION. Claude web should open OEM-side
trim-mix disclosures (Maruti Suzuki, Hyundai Motor India investor materials on
alloy-wheel-equipped variant mix) to test whether the "why now" — rising alloy adoption
at the customer level — is independently confirmed, since B04/B05 give only SSWL's own
claim. Never fabricate a counterparty fact; if no such disclosure exists, record that
finding as NOT DISCLOSED.
```

```
CHAIN 2: SSWL guided FY27 exports of ~Rs 600 Cr against FY26 actual exports of Rs 454
Cr (down from Rs 561 Cr FY25) and Q1 FY27 actual exports of Rs 127 Cr (B05 guidance
table; B04 export figures).
Link 1 [CLAIM]: Management attributes the FY26 export fall to US tariff disruption and
guides recovery once "the level playing field" versus Vietnam/Thailand competitors is
reached — a specific tariff-edge claim raised on the Q4 FY26 call and reversed by
management itself one quarter later ("no differential advantage... level playing
field," Q1 FY27 call, per B07 FLAG-CONTRADICTED-CLAIM).
Link 2 [DOC]: Bhuj capacity (1.2 Mn alloy wheels + up to 1.1 Mn knuckles) is
capital-committed (~Rs 420 Cr, B05 guidance table), and the India Ratings rationale of
18-Feb-2026 records that Bhuj "would cater entirely to exports" (rating rationale p.3,
per gate-recommendation.md quoting B03/B08's source review).
Link 3 [INFERENCE]: Because Bhuj was built for exports with named Chinese
technology-partner support (Liuzhou Arays, Hainan Jihoo, first appearing in this AR,
B03 ar_new_downstream_entities), and because the plant's own framing shifted between
calls — from "OEM approval, sold out" toward "export aftermarket plant" on the Q1 FY27
call (B12b independent finding) — the export-recovery trigger depends on an unresolved
question (does Bhuj's output find OEM-qualified or aftermarket-only demand) that
management's guidance does not itself resolve.
Binding constraint: FY27 capex for Bhuj plus the agri/steel brownfield rose from Rs 460
Cr (Q3 FY26 guide) to Rs 550 Cr (Q4 FY26) to Rs 650 Cr (Q1 FY27) across three
consecutive calls (B12b), funded against a standalone cash balance of Rs 6.5 Cr and net
adjusted leverage already above the 2.5x threshold Ind-Ra itself names as its positive
trigger (B04 must_track_metrics).
Unsaid: No AR or deck narrative names a signed customer-side commitment (an OEM
development contract, an offtake agreement) for Bhuj's incremental export capacity; the
optionality register carries "Bhuj as a global aftermarket export hub" as an
unconverted item requiring a disclosed export-revenue split attributable to
Bhuj-sourced product before it counts as delivered (B07 optionality_register).
Observation that confirms or breaks this chain, and confirm-by date: the H2 FY27
quarterly export run-rate (results filings expected Nov-2026 and Feb-2027). A run-rate
implying a full-year figure of Rs 550-600 Cr confirms the chain; exports stuck below
~Rs 400 Cr annualised, or a fresh US Section 232/reciprocal tariff escalation in the
Federal Register, breaks it (B05 trigger 3 kill_signal; B09 downstream_candidates).
Who pays, and why now: PENDING LIVE VERIFICATION. Claude web should open the USTR
Federal Register tariff notices on Indian auto-component/wheel exports, naming the
comparator jurisdictions Vietnam and Thailand (per B05/B06/B07), to test whether India
in fact holds the tariff-cost advantage management first claimed and then reversed,
since this container cannot reach live tariff-notice text. Never fabricate a
counterparty fact; if the notices are silent on wheels specifically, record that as
NOT DISCLOSED.
```

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in claude.ai with live
web, before Role 2.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. Steel Strips Wheels makes wheel rims for vehicle makers, plus small volumes of
   aluminium steering knuckles (B04).
2. Steel wheels bring about 63% of FY26 revenue; alloy wheels about 36%; knuckles
   about 1% (B04).
3. Every wheel is built to the buyer's own design and approved for one vehicle
   platform, so a new supplier needs a fresh approval cycle before it can compete
   (B04, B07).
4. Buyers are named Indian and export vehicle makers: Maruti Suzuki, Hyundai,
   Mahindra, Tata Motors, Ashok Leyland, Honda's two-wheeler arm, and several tractor
   and equipment makers (B04).
5. Demand today follows vehicle output. SIAM, TMA/FADA, and the named customers' own
   sales data all track it directly (B09).
6. Demand should grow if cars keep shifting from steel to alloy wheels, and if exports
   recover as US tariff treatment of India, against Vietnam and Thailand, settles
   (B04, B05).
7. The company is building new alloy-wheel and knuckle capacity at Bhuj in Gujarat to
   meet that shift, though the trial-production date has already slipped once (B07,
   B12b).
8. Steel wheels carry a moderate moat: broad capacity, a long-standing steel supply tie
   to Tata Steel, and multi-decade OEM qualification (B04, B07).
9. Alloy wheels do not yet show a proven moat: management called the domestic alloy
   margin "crashing" under competition on one call and "expanding at every segment" on
   another, and one listed peer calls its own alloy business its lowest-return segment
   (B06, B12b).
10. The mental model is a transition bet: does the shift from steel to alloy and
    knuckles lift company-wide margin, and does cash follow that lift (Section 2)?
11. The bull case rests on a moderate number of variables, most checkable against
    outside data, but the one number that would prove the mix story, the steel-versus-
    alloy profit split, is the one thing management has declined to give in every
    quarter it was asked (Section 4c, B05).
12. The corpus could not establish the FY24 AMW insolvency gain's exact breakup,
    because the FY24 Annual Report is not in the corpus (B02, B03, B04).
13. The corpus could not establish a company-wide product margin split for steel
    versus alloy wheels anywhere in the Annual Report, the four decks, or four
    quarters of call transcripts (B02, B04, B05).
14. The biggest open question is whether the FY26 fall in cash conversion is a
    one-year effect of fast growth and capex, or the start of a lasting reliance on
    two financing lines that already support reported cash flow (B03, B13-lite).
15. A second open question sits around the AMW Autocomponent subsidiary: unexplained
    reserve transfers, a growing tax asset against a loss-making unit, and an
    unregistered land title, none of which the statutory auditor flagged as a key
    audit matter (B02, B03, B08).

---

## SECTION 6: STANDING EXTRACTION ANNEX

Answered from corpus. Quote-then-comment form; NOT DISCLOSED given with reason where
the corpus does not carry an item.

**1. UNITS.** No printed per-unit realisation figure (Rs per wheel, Rs per tonne)
exists anywhere in the FY26 AR; a full-text search for such a figure returned nothing
(B04 `input_gaps`, corroborated by B03). NOT DISCLOSED IN THE AR. The only per-unit
figures in the corpus are spoken on concalls and derived from decks: "Rs 314" EBITDA
per wheel for Q1 FY27 versus "Rs 262" for Q1 FY26 (Dheeraj Garg, Q1 FY27 concall,
16-Jul-2026, per B05 `guidance`) — a blended, all-product basket figure covering steel,
alloy and knuckle wheels together, not a single product. The volume and revenue lines
from which a basket average can independently be derived: Revenue from Operations
Rs 5,182.8 Cr (FY26) against total volume of ~199.52 lakh units (derived, B04
`unit_economics`), giving a blended ~Rs 2,600/wheel; steel ~Rs 2,070/unit versus alloy
~Rs 4,730/unit (both derived, not printed, B04). Comment: no document in this corpus
prints a per-product realisation or margin figure; every per-unit number here is either
spoken (concall) or derived (this run's own arithmetic on deck/AR totals).

**2. SEGMENT CAPITAL AND DEBT.** AR Note 44A: "The Company's Operation predominantly
comprise of only one segment i.e Manufacturing of Auto-Components" (AR p.174, per B04).
Comment: because SSWL discloses a single Ind AS 108 segment, no segment-wise capital
employed, segment assets, segment liabilities or segment-allocated borrowings figure
exists anywhere in the AR (B02 Finding 14; B03 `input_gaps`). Borrowings are wholly
unallocated by definition. Total borrowings, unallocated: "FY27 total borrowings
~Rs 826cr (flat vs FY26)" (Dheeraj Garg / Pranav Jain, Q1 FY27 concall, per B05
`guidance`). NOT DISCLOSED (no segment split exists to disclose; single-segment
company).

**3. GUIDANCE VERSUS ASPIRATION.**
- (a) Guidance with a period: "More or less, and the turnover will be close to INR
  6,500 crores versus INR 5,143 this year" (Dheeraj Garg, Q4 FY26 concall, 02-Jun-2026;
  timeframe FY27). Comment: an explicit revenue figure with an explicit forward period;
  the comparator base cited (INR 5,143 Cr) is a rounder number than the audited FY26
  figure used elsewhere in this run (Rs 5,182.8 Cr, B04) — a minor internal
  inconsistency in management's own spoken figures, not resolved in the transcript.
- (a) Guidance with a period: "Yes... you can see the current run rate also... we are
  at INR1,509 crores" confirming "in FY '27, we can do a top line of around INR6,500
  crores... that makes our top line growth at around 25%" (Nishita Shanklesha / Dheeraj
  Garg exchange, Q1 FY27 concall, 16-Jul-2026; timeframe FY27). Comment: reaffirms the
  FY27 revenue guide one quarter into the year, against a Q1 actual of Rs 1,509 Cr
  (B05).
- (a) Guidance with a period: "on the export side, you said INR600 crores this year"
  (Ankur Kumar, referencing management's own prior statement, Q1 FY27 concall,
  16-Jul-2026; timeframe FY27). Comment: the ~Rs 600 Cr FY27 export figure recurs across
  Q3 FY26, Q4 FY26 and Q1 FY27 calls (B05 `guidance`); Q1 FY27 actual exports were
  Rs 127 Cr (B05), one quarter into a four-quarter guide.
- (a) AR-native guidance with a period: FY27 renewable-energy capex "Rs 15.00 Cr (vs
  Rs 10.00 Cr spent FY26)" and FY27 renewable electricity sourcing "~650 lakh units"
  (Board's Report / BRSR, per B03 `guidance_table`; timeframe FY27). Comment: specific
  and capital-quantified; first-year delivery not yet testable.
- (c) Capacity/capability only, no explicit period or metric: Dappar plant
  "water-positive target" is named directionally with no metric given (B03
  `guidance_table`). Comment: qualitative aspiration, not gradeable guidance.
- (c) Capacity/capability only: "The next financial year would be where we end up
  utilizing all our assets. The expansion comes into play" (Dheeraj Garg, Q4 FY26
  concall, 02-Jun-2026). Comment: a capability statement about future capacity
  utilisation, not itself a numbered guide; the EBITDA figure that follows it in the
  same breath ("INR 700-750 crore... in the next financial year") is ambiguous on
  which fiscal year it targets — B12b independently corrects the pipeline's own earlier
  reading to ~Rs 650 Cr for FY27 and ~Rs 700-750 Cr for the year after (B12b).

**4. CONCENTRATION.** Product concentration: steel wheels ~63%, alloy wheels ~36%,
knuckles ~1% of FY26 revenue (B04). Customer concentration: the AR itself states, in
its own risk discussion, that "top customer concentration is a risk" (AR p.124, quoted
in B04); no percentage accompanies that AR sentence. Deck-only, unaudited figures name
individual OEM share-of-business percentages as high as "96% at Suzuki Scooters, 64% at
Ashok Leyland and 58% at Tata Motors" (Jul-2026 deck, per B04) — B07 separately flags
these percentages as management-claimed, not audited (B07 `FLAG-UNVERIFIABLE-LOCKIN`).
Geography concentration: AR Note 44B (standalone, gross sale revenue basis): domestic
Rs 5,641.3 Cr, exports Rs 453.5 Cr, FY26, i.e. exports 7.4% of the AR's "gross sale
revenue" base of Rs 6,094.8 Cr (B04). The AR's own MD&A text separately states "85% of
revenues come from domestic market customers" (AR p.124, per B04) — a rounder figure
that does not reconcile exactly with either the Note 44B split or the deck's export
line (8.8% of Revenue from Operations, May-2026 deck, per B04); this run used the more
precise Note 44B / deck figures, not the MD&A rounding, as its anchor (B04).

**5. PROMISE LEDGER.**

| Promised in | Promise | Outcome | Evidence anchor |
|---|---|---|---|
| Q2 FY26 | FY26 revenue ~Rs 4,800 Cr | Delivered (beat): Rs 5,183 Cr actual | B05 promise_delivery row 1 |
| Q2 FY26 | FY26 EBITDA Rs 470-480 Cr | Delivered (beat): Rs 523 Cr actual | B05 row 2 |
| Q2 FY26 | EBITDA/wheel first milestone Rs 260-265 | Delivered: Rs 260 in Q3 FY26 | B05 row 3 |
| Q3 FY26 | Q4 FY26 EBITDA/wheel target Rs 270 | Delivered (beat): Rs 282 actual | B05 row 4 |
| Q4 FY26 | FY27 EBITDA/wheel ~Rs 300 | Delivered ahead of schedule: Rs 314 in Q1 FY27 | B05 row 5 |
| Q2/Q3 FY26 | Knuckle capacity to 0.5mn then ~1.0-1.1mn via Bhuj | Delivered/on track: Bhuj knuckle 1.1mn confirmed | B05 row 6 |
| Q3 FY26 | Return next call with FY27 EBITDA/wheel and EBITDA figures | Delivered on the letter, Q4 FY26 call | B05 row 7 |
| Q1 FY26 deck (ref. Q3 FY26 call) | Steel wheel capacity 205 to 270 lakh | Missed/downsized to ~210 lakh, not proactively disclosed | B05 row 8 |
| Q3 FY26 | US export recovery in three to six months | Partial: unresolved through Apr-May 2026; ~one quarter of slippage | B05 row 9 |
| Q2/Q3/Q1 FY27 (repeated) | Steel-vs-alloy EBITDA/wheel split | Missed every quarter, "trade secrets" cited | B05 row 10; concall verbatim above |
| Q3 FY26 | MHCV share discrepancy (52% vs prior 61%), "will clarify" | Missed: no on-record follow-up found | B05 row 11 |
| Q3 FY26 (B12b reread) | Bhuj trial production on track for Oct-2026 | WRONG per B12b: transcript moves trial to Q4 FY27, a 4-5 month slip | B12b `promise_delivery_spot_checks` (1 of 6 spot-checks found wrong) |

Comment: B05's own tally (7 delivered, 1 partial, 3 missed) is corroborated by B12b's
independent spot-check on 6 rows (5 confirmed, 1 wrong: the Bhuj timeline row). Treat
the Bhuj row as corrected per B12b, not per B05's original reading.

**6. RESTATED BASES.** A full-text search of the AR for "restat" returns only
accounting-policy boilerplate: Ind AS 8 policy language, the Ind AS 109 reclassification
policy explicitly stating financial assets/liabilities do "not restate" prior periods
on reclassification, and the common-control business-combination policy's own
restatement clause (Note 2.04(C), covered under Q7 below) (B02 Pass 3, `analyst_note`
and pattern re-checks). Comment: no note in the AR discloses that an actual
prior-period restatement occurred; `restatements_found: []` stands across all three
reading passes (B02).

**7. CORPORATE-ACTION CLAUSES.** The AR's own Note 2.04(C) "Business Combinations" (AR
p.197-198, consolidated) states the Group's default policy is the acquisition method,
then separately sets out a pooling-of-interests method for common-control
combinations, with two clauses: Clause (d): "The balance of the retained earnings
appearing in the financial statements of the transferor is aggregated with the
corresponding balance appearing in the financial statements of the transferee or is
adjusted against revenue reserve." Clause (f): "The difference... between the amounts
recorded as share capital issued... and the amount of share capital of the transferor
is transferred to revenue reserves/capital reserves." (Note 2.04(C), consol AR
p.197-198, per B02 Pass 3.) Comment: this is the AR's own definitional language for a
common-control combination, and B02 finds it a near-exact mechanical match to the
FY25/FY26 unexplained reserve transfers — but no note in the AR confirms whether this
method, rather than the stated default acquisition method, was actually applied to the
AMW acquisition (B02 Pattern Finding 1). The underlying corporate-action documents
themselves — the AMW Autocomponent NCLT insolvency-resolution plan (FY24) and the
Asia Motor Works Limited (AMWL) demerger scheme that transferred AACL's land (B02
Finding 7) — are NOT IN THE CORPUS as scheme documents; name the filings to fetch: the
NCLT/IBBI resolution plan for AMW Autocomponent Ltd (Bhuj), and the AMWL demerger
scheme filing (MCA/BSE). The one corporate action with clause-level detail actually
found in this corpus is a routine ESOS exercise: "84,680 shares at Rs 20, 23-Jul-2026
allotment" under the ESOS 2021 scheme (B08 §3B).

**8. RELATED-PARTY PERIMETER.** The AR names 30 promoter-group entities (bodies
corporate, HUF, trust) as related parties in Note 41 (standalone AR p.170-172; B08
§1B), of which the June-2026 shareholding pattern shows only 9 hold any equity in
SSWL. FY26 standalone RPT total: Rs 54.96 Cr (FY25: Rs 58.86 Cr) (Note 41, standalone
AR p.170-172; Board's Report AR p.29; B08 §3A). Nature and amount, latest year (FY26):
rent paid to a promoter-group enterprise rose 3.5x YoY, Rs 42.15 lakh (FY25) to
Rs 147.44 lakh (FY26), the largest single-year jump in the table, recipient entity not
cleanly resolved by the AR's own column layout (B08); Rs 315.00 lakh of the Rs 634.95
lakh FY26 CSR spend routed through "Enterprises over which KMP are able to exercise
significant influence" (Note 41, per B08); MD remuneration Rs 1,329.47 lakh FY26, down
3.08% YoY (Board's Report Annexure VI, per B08); an unsecured, interest-bearing
Rs 133.15 Cr loan to wholly-owned subsidiary AMW Autocomponent, unchanged two years,
Rs 8.27 Cr interest accrued FY26 (Note 41, standalone AR p.171-172, per B02/B08);
dividend paid to promoter entities Rs 12.05 Cr FY26 versus Rs 9.60 Cr FY25 (Note 41,
per B08). Comment: the Board's Report affirms all RPTs were at arm's length, in the
ordinary course, and that none required Form AOC-2 (AR p.29, per B08); B08 nonetheless
rates this dimension a caution, concentrated on the AMW loan and the unresolved rent
jump.

**9. PLEDGE AND SHAREHOLDING.** The corpus holds ONE filed shareholding pattern: BSE
XBRL SHP, quarter ended 30-Jun-2026 (`inputs/shareholding/SSWL-SHP-Jun2026-BSE.txt`).
Declaration line 7, exactly as printed: "Whether any shares held by promoters are
encumbered under 'Pledge'? | No | No" (SSWL-SHP-Jun2026-BSE.txt, Declaration table,
Quarter Ended 30-06-2026). Promoter and promoter group holding: 61.14% (17 holders), no
pledge, no encumbrance; public 38.86% (B00). Comment: the corpus does NOT hold the last
twelve quarters of filed shareholding patterns — only this single quarter is present,
so the last-twelve-quarters ask in this question cannot be met from filed documents in
this corpus. A five-year pledge-reduction narrative (21.9% Jul-2021 → 0% by FY26,
stepping through 12.26%, 8.70%, 5.78%, 3.06%) exists in the run's evidence, but it is
explicitly MEDIA REPORTED (Business Standard / EquityBulls items), not a filed document
read in this corpus (B08 `transition_evidence`); only the single Jun-2026 zero-pledge
data point above is independently VERIFIED from a filed source. Institutional (FII+DII)
holding latest: NOT DISCLOSED IN THIS DOSSIER. B00 records that FII/FPI and mutual-fund
rows sit inside the same SHP file, but extraction of that split is deferred to Stage 10
and was not pulled into a Halt-1 block (B00).

**10. VERIFICATION.**
- `inputs/annual-report/SSWL-AR-FY26-Reg34-2026-09-03.pdf` (Reg 34 filing, 03-Sep-2026)
  — Notes 2.04(C), 19, 25, 35, 41, 44, 48; Board's Report; CARO Annexure; auditor's
  reports; AOC-1.
- `inputs/results/SSWL-results-Q1FY27-2026-07-15.pdf` (15-Jul-2026).
- `inputs/results/SSWL-results-Q4FY26-FY26-2026-05-29.pdf` (29-May-2026).
- `inputs/results/SSWL-results-Q3FY26-2026-01-22.pdf` (22-Jan-2026).
- `inputs/concalls/SSWL-concall-Q3FY26-2026-01-23.pdf` (23-Jan-2026).
- `inputs/concalls/SSWL-concall-Q4FY26-2026-06-02.pdf` (02-Jun-2026).
- `inputs/concalls/SSWL-concall-Q1FY27-2026-07-16.pdf` (16-Jul-2026).
- `inputs/rating/SSWL-IndRa-rationale-2026-02-18.pdf` (18-Feb-2026).
- `inputs/shareholding/SSWL-SHP-Jun2026-BSE.txt` (quarter ended 30-Jun-2026).
- `inputs/announcements/SSWL-showcause_2026-06-17.pdf` (Customs SCN, 16/17-Jun-2026).
- `inputs/presentation/SSWL-investor-presentation-Jul2026-A.pdf` (15-Jul-2026).

CORPUS COMMIT HASH: 0c6387f9
