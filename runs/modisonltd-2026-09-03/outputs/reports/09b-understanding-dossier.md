# Halt 1 Understanding Dossier — Modison Ltd (MODISONLTD)

Run date: 2026-09-03. Corpus commit: fb2cc81c0c7ffd30bab69981c198a37c2c5ce975.
Assembled from committed blocks B00-B09, verifier blocks B12a-B12d, and the
confidence-delta block. No new research in Sections 1-5. No valuation, price,
or verdict vocabulary anywhere in this file except the one scoped Part B4
exception named in the stage instructions.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

1. CONCALLS. Two held: Concall_Oct_2022_Transcript.pdf (Investor Meet,
   Oct-2022) and AGM_43rd_Jul2026_webcast_operator_transcript.txt (43rd AGM
   webcast, Jul-2026, operator-supplied auto-transcript, non-filed) (B00).
   The most recent communication covered is the Jul-2026 AGM, discussing
   FY2025-26 results and some Q1 FY27 commentary. The manifest records
   concalls_available: false; the company holds no regular quarterly
   earnings calls, so no Q1 FY27 (quarter ended 30-Jun-2026) or later
   concall transcript is absent by omission, it is absent by company
   practice (B00 manifest_defects, freshness_pairs row 1). Given the
   run date of 2026-09-03, Q2 FY27 (quarter ended 30-Sep-2026) has not
   yet plausibly reported.

2. ANNUAL REPORTS. Two years held: FY2025-26 (primary, 43rd AGM, year
   ended 31-Mar-2026) and FY2024-25 (secondary, 42nd AGM, year ended
   31-Mar-2025) (B00). The latest completed FY (FY26) is present. Only 2
   AR PDFs are held, not the 3 years the audit would prefer as a PDF set;
   the screener CSV series extends the numeric history back to FY16
   (B01), but underlying AR text for years before FY25 is not in the
   corpus.

3. RESULTS FILINGS. Three held: Q1 FY27 unaudited (quarter ended
   30-Jun-2026, the NEWEST filing in the corpus), Q4 FY26 audited annual
   (quarter and year ended 31-Mar-2026), and Q3 FY26 (nine months ended
   31-Dec-2025) (B00). No quarter-gap: the newest results filing (Q1 FY27)
   post-dates the FY26 AR sign-off (22-May-2026 per B03), so nothing
   filed since is missing from this set.

4. INVESTOR PRESENTATIONS. One held: Investor_Presentation_1.pdf, dated
   4-Mar-2024 (Q3 FY24), two years before the FY2025-26 AR (B04
   input_gaps). It was used only for product/history/facility facts, not
   for FY26 figures. No FY26 or FY27 investor presentation is in the
   corpus.

5. RESEARCH / RATING. One rating document: CARE Ratings, Dec-2025 (CARE
   A;Stable / CARE A1), FULL rationale present in the same PDF (B00).
   Two broker notes held (research/rpt 1.pdf, rpt2.pdf) without a
   confirmed date in the blocks reviewed. Two operator-supplied leads:
   an FY26 operational summary and a shareholding-pattern screener image
   (both non-anchored, research tier).

6. CORPORATE ACTIONS. The announcements/ folder is ABSENT (count: 0)
   (B00). The operator states no material exchange announcement after
   31-Mar-2026 beyond the FY26 AR (B00 input_gaps). This statement sits
   in tension with B08's independently sourced finding (media/aggregator
   tier, primary BSE filing blocked by egress proxy) that Modison HV
   Private Limited, the company's sole subsidiary, was divested on
   13-Aug-2026 directly to the MD and JMD personally — an event dated
   after the operator's cut-off and not present in the corpus as a
   primary filing (B08).

7. FRESHNESS PAIR CHECK. B00's freshness_verdict reads "FRESHNESS PAIRS
   OK." All four pairs: results-to-same-quarter-concall is SKIPPED
   (declared absence — company holds no regular quarterly calls, AGM used
   per operator ruling, not a failure); rating-bulletin-to-full-rationale
   is PASS (detailed key rating drivers in the same PDF); SEBI-order-to
   -order-text is PASS (no SEBI order referenced anywhere in the
   corpus); AR-to-latest-audited-annual-results is PASS (FY26 AR present,
   same year as the audited FY26 results). No pair FAILED.

8. VERDICT LINE: **CORPUS GAPPED** — the announcements/ folder is absent
   (Reg 30 filings; expected source: BSE) and no filed shareholding-pattern
   PDF exists anywhere in the corpus (expected source: BSE / company IR
   page). Both are findable-but-missing, not plausibly-nonexistent: listed
   companies routinely file both. The prospectus is absent but is NOT a
   gap — Modison has been listed since 1983 (CIN L51900MH1983PLC029783,
   43rd AGM), so no prospectus is expected to exist in current form. The
   four Freshness Pair Check pairs are all OK (PASS or a declared,
   non-failing SKIP), so this is NOT CORPUS GAPPED-FRESHNESS. Two further
   findable-but-missing items, noted for the research brief in Section 4:
   an FY26/FY27-dated investor presentation (the one held is stale,
   Mar-2024) and the BSE primary filing for the 13-Aug-2026 Modison HV
   divestment, which postdates the operator's stated cut-off.

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT — PENDING OPERATOR SIGN-OFF**

### PART A — THE FROM STATE (the anchor, not the model)

**A1. ARCHETYPE.** One reported business line (single primary segment,
"Manufacturing of Electrical Contacts," AR Note 47, p.179). The archetype
is a HYBRID of two entries in the CLAUDE.md Archetype Library: the
Commodity converter (spread economics: silver, copper and tungsten are
87.1% of revenue gross, pass-through pricing under customer agreements,
utilisation and cycle position dominate) and the Build-to-spec component
maker (OEM design-in and type-approval switching costs, content-per-unit
economics with named anchor customers GE, Siemens, ABB, L&T, GM Modular
and BHEL) (B04 analyst_note). Section 1B Amendment 17 (converter multiple
treatment) likely binds on the pass-through slice; this is a Stage 11
question, not resolved here.

**A2. THE SIMPLE ANALOGY.** Modison buys silver, copper and tungsten and
turns them into small metal contacts, the part inside a switch that
touches to complete a circuit and separates to break it. Every low,
medium and high voltage switchgear unit, circuit breaker and vacuum
interrupter needs these parts; a switchgear maker cannot ship a breaker
without them. Modison sells to OEM switchgear makers business to
business, on contracts that pass most of the metal price through to the
buyer. About 88% of sales are domestic, about 12% export. Today the
company earns its margin mostly from the fabrication or conversion charge
on top of a pass-through metal cost, with only a modest, unproven layer
of design-in stickiness on top (B04, B01, business-narrative.md).

### PART B — THE TRANSITION (the model)

**B1. FROM to TO.** FROM: **R1 COMMODITY PRICE-TAKER** (~12x
neighbourhood on the CLAUDE.md Quality Ladder) — margin has moved with
metal-input price and pass-through timing across a 10-year band of
6.95% to 16.29% EBITDA margin (B01, B04), and the one claimed
cost-advantage moat (backward integration into a group refining
affiliate, MCPL) was independently denied: MCPL is an unconsolidated
related party depending on Modison for a large share of its own
turnover, not a captive plant on Modison's balance sheet (B07
FLAG-IR-AR-CONFLICT). TO (management's claim): **R3 VALUE-ADDED /
SPEC'D SUPPLIER** (~19x neighbourhood) — a niche HV "crown business"
position, OEM design-in and type-approval stickiness, and a claimed
migration toward sub-assemblies with named OEMs (B04, B05). The
emerging-moat scan found no confirmed moat yet forming toward this TO
state (em_score 8 of 92, threshold 12, B07), and R&D spend fell 24.4%
YoY in the same record year (B07). Both endpoints are named here as a
DRAFT for operator sign-off, not an assertion.

**B2. THE ENGINE.** Two things would have to physically change to move
FROM to TO: (i) a real product-mix shift toward the HV "crown business"
and toward sub-assembly / value-added products with named OEMs (claimed
in 2022, silent by the Jul-2026 AGM — B05 dropped_triggers), and (ii)
pass-through pricing mechanics capturing the full metal-cost move on a
shorter lag than peers, evidenced this cycle by a record 16.1% EBITDA
margin (B01, B04). B12b's review found the FY26 record margin is
substantially a Q4 timing catch-up from retroactive tungsten
price-approvals concluded that quarter, alongside a Rs 9.51 cr Q4 silver
hedging loss — a quality-of-earnings caveat on the engine, not yet a
structural cost or mix advantage (B12b, B05 AGM Speaker 7 answer).

**B3. THE PROOF GATE.** Two conditions, both required, quarter by
quarter: (a) EBITDA margin sustained at or above roughly 14% (above the
FY25 trough of 8.33% and the B04 red-flag floor of ~9%) through at least
two quarters in which silver, copper or tungsten prices are falling —
the tightened confirm signal B06 recommends, since silver had already
fallen from roughly Rs 400/g to Rs 250/g by Aug-2026 per Salzer's own
disclosure (B06); and (b) operating cash flow positive in at least one
of the next two quarters (Q1 or Q2 FY27), reversing the FY25-FY26
negative run (B02, B03). Until both fire, the climb up the quality
ladder is claimed at the accrual level only, not proven (gate-
recommendation.md PROOF GATE: NOT FIRED).

**B4. THE RECOGNITION GAP (to be resolved at Stage 11).** Open question,
not answered here: does the market already price Modison as if it has
reached, or is close to, the claimed value-added / HV-niche TO state, or
does it still price the pass-through commodity-converter FROM state? If
the TO state is already reflected in current pricing, the re-rating
engine is spent and only earnings growth would carry a return; if it is
not, the gap remains open. Stage 11 resolves this via the destination-PE
read against the Section 1B framework. No number, no fair value, no
conclusion is stated here.

**B5. THE UGLINESS TEST.** **INDETERMINATE — pending operator
classification**, carried forward from gate-recommendation.md's own
finding rather than forced into one of the two canonical labels here.
Evidence toward ARTIFACT-OF-CLIMB: growth is working-capital-led, not
capex-led (FY26 capex only Rs 15.10 cr, B04); payables discipline held
throughout (MSME payables fully current, trade payables turnover
improved, B02); receivables ageing stays 98.4% under six months (B02).
Evidence toward STRUCTURAL-FEATURE: receivables (+83.8%) and inventory
(+72.4%) both outran revenue (+44.9%) rather than tracking it (B02); the
deterioration accelerated roughly fourfold into FY26 (-16.10 cr to
-64.18 cr, B03); ECL coverage on receivables fell from 1.47% to 0.40% of
gross book as the book nearly doubled (B02); no post-year-end cash
confirmation exists in the corpus (B05 input_gaps). The classification
is left open for the operator; it cannot be cleanly resolved on the
evidence assembled here.

**B6. THE TRANSITION FALSIFIER.** Operating cash flow staying negative
through Q2 FY27 while revenue keeps growing would strike the core of the
transition thesis: it would show the margin recovery and the claimed
mix-shift toward value-added products are not converting to cash, and
that the "climb" so far is an accrual and Q4-timing artifact rather than
an economic one (gate-recommendation.md Falsification line; B02, B03).

### PART C — WHAT THE MODEL WATCHES (derived from the transition)

**C1. DOMINANT VARIABLES.**
1. EBITDA margin trajectory through the metal-price cycle — currently
   16.10% FY26 (10-year band 6.95%-16.29%), guided down to "at least
   10-12%" for FY27, a step down from the just-achieved 16.2% (B01, B04,
   B05).
2. Operating cash flow / cash conversion — currently negative two
   filed years running: +1.24 cr FY24, -16.10 cr FY25, -64.18 cr FY26
   (B02, B03).
3. MCPL related-party dependency and pricing — currently Rs 50.42 cr
   FY26 actual transaction (11.27% of Modison turnover), a Rs 80 cr FY27
   forward ceiling equal to 48.76% of MCPL's own FY26 turnover, and an
   unreconciled AGM claim that Modison is only ~25% of MCPL's sales
   (B02, B05, B08, and this dossier's Section 6 Q8).
4. HV / value-added product mix and segment disclosure — currently
   undisclosed at the segment level (single reported segment, AR Note
   47); R&D spend fell 24.4% YoY; the emerging-moat scan found nothing
   forming (B04, B07).

**C2. WHAT THE MODEL REJECTS.** Market-sizing precision is noise here.
B09 already reads the runway class GOOD with roughly 4.1x revenue
headroom against a conservative SAM, and same-year global TAM estimates
from tertiary report-mill vendors span 1.7x against each other on low-
quality data (B09) — the binding constraint on this thesis is proving
cash conversion and margin durability, not addressable market size.
Precise LV/HV self-reported market-share percentages (16-17% vs 30-35%
LV; 72-82% HV) are similarly rejected as decision-relevant: they are
unverifiable against any independent source and moved without
explanation across the two communication sources four years apart (B04,
B05, B06).

**C3. THE BUSINESS FALSIFIER.** A sustained EBITDA margin fall below the
10-year band floor (6.95%) combined with a third consecutive year of
sharply rising leverage (past the FY26 gearing of 38.83%, itself already
double FY25's 25.12%) would force a re-declaration of the FROM business
itself: it would mean even the commodity-converter economics that have
held for a decade, not just the claimed climb above them, have broken
down (B01, B02, B03).

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

*(Drafted per prompts/13-synthesis-pipeline.md's BUSINESS UNDERSTANDING
NARRATIVE spec, from B01-B09; already assembled to that spec in this
run's business-narrative.md, reused here verbatim per the shared-spec
rule.)*

Modison makes electrical contacts and contact materials from silver,
copper and tungsten. The contact is the small metal part inside a switch
that touches to complete a circuit and separates to break it. Every low,
medium and high voltage switchgear unit, circuit breaker and vacuum
interrupter needs these parts to switch power and to protect the line. A
switchgear maker cannot ship a breaker without them. Modison reports one
segment, split about 88% domestic and about 12% export. Both sell
business to business on contracts that pass metal prices through to the
buyer.

The customers are original equipment makers of switchgear. Named anchor
buyers are GE, Siemens, ABB, L&T, GM Modular and BHEL. A buyer designs a
contact into a product and type approves it, which raises the cost of
moving to another supplier once a part is qualified. The company names
customer concentration in a limited set of OEMs as a formal risk. It
does not disclose top five or top ten customer share.

Present demand comes from those OEMs buying to fill their own order
books, so their capex and order intake drive Modison's orders. Reported
revenue also moves with silver, copper and tungsten prices, since metal
is about 87% of the cost passed through. India transmission and
distribution capex under the CEA National Electricity Plan is the
largest structural pull for high and medium voltage switchgear parts.

Demand should grow with several external programmes. The CEA
transmission plan carries a Rs 7.93 lakh crore programme. The MNRE 500
GW renewable target needs grid switchgear for integration. India data
centre buildout, tracked by JLL and CBRE, pulls low voltage switchgear
and contacts. An ISRO import substitution recognition points at a
possible government and defence pipeline. Each links to a signal a
reader can check outside the company.

Competitive advantage is thin and unproven on filed evidence. The high
voltage niche carries a self claimed sole India manufacturer position,
but the company never discloses segment revenue, so the claim cannot be
checked. Switching costs from OEM design in are moderate and real. The
cost advantage claim from backward integration does not hold: the
refining affiliate MCPL is a related party, not a captive plant on
Modison's books, and it depends on Modison for about 49% of its own
sales. R&D spend fell about 24% in the record year. The emerging moat
scan scored 8 of 92 and found no forming moat. No business line shows a
proven moat on the filed record.

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. VERTICALS FRAMED

**Vertical 1 — EBITDA margin through the commodity cycle.**
Established: FY26 record margin 16.10%, top of a 10-year 6.95%-16.29%
band (B01, B04); the record is substantially a Q4 timing catch-up from
retroactive tungsten price-approvals plus a Rs 9.51 cr Q4 silver-hedging
loss (B12b); FY27 guidance is "at least 10-12%" (B05); peer SBCL, the
closer silver-contacts match, expanded margin ~250bps to 22.9% and calls
silver margin-neutral, while Salzer alone compressed 12% to 7.5-8% and
calls the pass-through lag "industry-wide" (B06, corrected by B12b).
Cannot establish: whether the FY26 margin holds through a full metal-
price DOWN-cycle, since silver had already fallen from ~Rs 400/g to
~Rs 250/g by Aug-2026 per Salzer (B06); the volume-versus-metal-price
split of FY26's 44.9% revenue growth (B04).
Questions: Does Q1/Q2 FY27 margin hold above the FY25 trough of 8.33% as
silver falls further? Does the Q4 catch-up repeat, or was it a one-off
timing event? Does Modison's pass-through genuinely differ structurally
from Salzer's (a weaker product match) or align with SBCL's (a closer
match, corroborating)?

**Vertical 2 — Operating cash flow / cash conversion.**
Established: OCF +1.24 cr FY24, -16.10 cr FY25, -64.18 cr FY26 on the
filed AR basis (B03); receivables +83.8%, inventory +72.4% against
revenue +44.9% (B02); borrowings +139.8% to Rs 174.47 cr including a new
Rs 99 cr WCDL (B02); a Rs 14.60 cr dividend was paid in the negative-OCF
year (B02); payables discipline held (B02, B03).
Cannot establish: Q1/Q2 FY27 operating cash flow, since the quarterly
cash flow statement did not file or extract cleanly in this corpus
(B05); whether the working-capital build is growth-induced-timing or
structural — Gate 0's own determination on this is INDETERMINATE
(gate-recommendation.md).
Questions: Does OCF turn positive in Q1 or Q2 FY27? Does receivable days
trend back toward the stated 75-day policy from 82.2? Does WIP, which
grew 76.3% against revenue's 44.9%, stabilise?

**Vertical 3 — MCPL related-party dependency and pricing.**
Established: Rs 50.42 cr FY26 actual RPT, 11.27% of Modison's
consolidated turnover (AR Explanatory Statement, p.29-30); the proposed
Rs 80 cr FY27 ceiling equals 48.76% of MCPL's own FY26 turnover of
Rs 16,406.88 lakh, provisional and unaudited at the time of filing (same
source); MCPL holds 1.26% of Modison's equity, Modison holds none of
MCPL's, and MCPL is controlled by promoters and relatives holding over
98% of its equity (AR p.28-29); the AGM states Modison is only ~25% of
MCPL's sales, unreconciled against the AR's 48.76% figure (B05, B08,
and Section 6 Q8 below).
Cannot establish: an independent arm's-length pricing benchmark for the
RPT (B08); which figure — the AGM's ~25% or the AR's 48.76% — answers
the same question, since the AR figure is stated against the *proposed*
ceiling and MCPL's own turnover, not against the actual FY26 transaction
value (this dossier's own read of the AR text, Section 6 Q8).
Questions: What is Modison's actual share of MCPL's FY27 sales once the
Rs 80 cr ceiling is drawn down? Does an independent valuer opinion exist
for the arm's-length pricing? Why did the AGM answer differ from the AR
by roughly half?

**Vertical 4 — HV / value-added product mix and segment disclosure.**
Established: single reported primary segment, "Manufacturing of
Electrical Contacts" (AR Note 47, p.179); only a geographic secondary
segment (India / Outside India revenue and assets) is disclosed (same
note); R&D spend fell 24.4% YoY to Rs 1.59 cr (0.22% of revenue) in the
same year the AR states no significant technology-absorption effort was
made (B07); the emerging-moat scan found no confirmed forming moat, 8 of
92 (B07); the claimed backward-integration moat via MCPL is denied — it
is an unconsolidated related party, not a captive plant (B07).
Cannot establish: LV/MV/HV revenue or margin split, never disclosed,
asked twice across sources four years apart, deflected both times (B04,
B05); the claimed HV "sole India manufacturer" position, unverified
against any independent source (B04).
Questions: Will the FY27 AR disclose any segment-level revenue split?
Does the LV Brownfield / HV Greenfield capex programme (targeted
Nov-2022/FY23, still unconfirmed 3-4 years later) ever complete and get
disclosed? Does the GE Best Supplier relationship or the GE/Siemens/ABB
joint-improvement projects convert into a quantified wallet-share
disclosure?

### 4b. CANDIDATE SIGNAL TABLE

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| GE / Siemens / ABB / L&T / BHEL capex and order-book disclosures | Named OEM customers' capex or order intake falling YoY for 2+ consecutive quarters while Modison claims continued growth | Quarterly | OEM investor-relations filings and capex announcements (B09) |
| CEA National Electricity Plan (Transmission) execution updates | Execution materially behind the Rs 7.93 lakh crore programme's stated pace for 2+ years | Event-driven | Central Electricity Authority published plans and progress reports (B09) |
| MNRE renewable capacity addition data | Monthly capacity-addition bulletins showing growth stalling well below the 500 GW 2030 pace | Monthly | Ministry of New and Renewable Energy monthly bulletins (B09) |
| India data-centre capacity buildout trackers | Tracked buildout flat or declining, undercutting the CEO-stated AI/data-centre demand driver | Quarterly | JLL India / CBRE India / Cushman & Wakefield India reports (B09) |
| Silver (LBMA), copper (LME), tungsten APT prices | Prices falling sharply (already observed, ~Rs 400/g to ~Rs 250/g silver by Aug-2026) without a matching EBITDA-margin compression at Modison | Monthly | LBMA silver, LME copper, Metal Bulletin/Argus tungsten APT (B09) |
| Shivalik Bimetal Controls (SBCL) quarterly results, Electrical Contacts division | SBCL's contacts-division margin or revenue moving opposite Modison's for 2+ consecutive quarters without an explained reason | Quarterly | SBCL BSE/NSE quarterly filings and investor presentations (B09) |

These are UNVERIFIED drafts; verification and tracker writes happen at
Role 5.5 in claude.ai.

### 4c. FRAGILITY READ

- variable_count: 4 (the C1 dominant variables: margin trajectory, cash
  conversion, MCPL dependency/pricing, HV/value-add mix and disclosure).
- verifiability_ratio: "2 of 4 externally observable" — margin (via
  quarterly filed results plus LBMA/LME/tungsten reference prices) and
  cash conversion (via the quarterly filed cash-flow statement) are
  externally observable once filed; MCPL dependency/pricing and the
  HV/value-add mix are company-narrated only, resting on AR/AGM
  disclosure with no independent benchmark or segment data (B08, B04).
- single_point_failure: Operating cash flow. A third consecutive
  negative period (Q1 or Q2 FY27) would on its own confirm the
  cash-conversion problem is structural, independent of how the margin
  or MCPL questions resolve (gate-recommendation.md Falsification line).
- fragility_verdict: **FRAGILE** — four variables in play, half of them
  company-narrated only, and one named single point of failure, against
  a management credibility grade of C (B05) that already includes an
  unreconciled related-party discrepancy and a downplayed fire loss.

### 4d. RESEARCH BRIEF

1. Fetch and verify the filed shareholding-pattern PDF (BSE/NSE) for
   promoter %, pledge/encumbrance field, and FII/DII holding for the
   last twelve quarters, replacing the non-anchored operator screener
   lead.
2. Fetch Reg 30 announcement filings (BSE/NSE) for the period since
   31-Mar-2026, including confirmation of the Modison HV Private Limited
   divestment (13-Aug-2026, sourced only from aggregator media in this
   run) and the Modison Solartech buyer identity and price.
3. Obtain an independent arm's-length pricing benchmark or valuer
   opinion for the Modison Copper Private Limited Rs 80 cr FY27 RPT
   ceiling.
4. Reconcile the AGM's ~25% MCPL-dependency claim against the AR's
   48.76% figure directly with management, or via a follow-up filing.
5. Verify the India electrical-contacts / switchgear-components TAM
   figures against primary sources (valuates.com QYRE-Auto-38C15590,
   IMARC), since same-year global estimates in this run span 1.7x across
   tertiary vendors.
6. Check for any IiAS/SES proxy-advisory report or minority-shareholder
   vote history on the MCPL resolution and other related-party items.
7. Confirm LV Brownfield / HV Greenfield factory (~Rs 25 cr, targeted
   Nov-2022/FY23) completion status via BSE filings or a direct company
   query, since no source in this corpus confirms this 3-4 years after
   target.
8. Pull direct MCA21 filings to confirm the Rs 105 cr of HDFC/Citi bank
   charges not yet registered on the MCA portal.
9. Verify Q1/Q2 FY27 operating cash flow directly from the filed
   cash-flow statement once available — the single most decisive test
   named in this dossier.
10. Check CARE Ratings for any update since Dec-2025 that covers the
    FY26 cash-flow deterioration, since the existing rationale covers
    FY25 only.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. Modison makes electrical contacts, small metal parts made from
   silver, copper and tungsten that let a switch complete or break an
   electric circuit.
2. Every low, medium and high voltage switchgear unit, circuit breaker
   and vacuum interrupter needs these parts.
3. The company reports one business segment. About 88% of sales are
   domestic and about 12% are export.
4. Customers are OEM switchgear makers such as GE, Siemens, ABB, L&T,
   GM Modular and BHEL, who design the part into their own product.
5. Once a part is designed in and type approved, moving to another
   supplier costs the buyer time and money. That gives Modison some
   stickiness with its customers.
6. Present demand tracks those OEMs' own order books and capex, plus
   the price of silver, copper and tungsten, which Modison mostly passes
   through to customers.
7. Demand should grow with India's transmission capex plan, the
   renewable energy target, data centre buildout and a possible
   government or defence pipeline from an ISRO recognition. Each links
   to a public source a reader can check.
8. Competitive advantage on the filed record is thin. Switching costs
   from design-in are real but only moderate.
9. A claimed backward-integration advantage into a group refining
   company, MCPL, does not hold: MCPL is a related party, not Modison's
   own plant, and Modison is close to half of MCPL's own sales. Research
   spend fell about 24% in the same record year, and a scan for new
   emerging strengths found almost nothing forming.
10. The mental model is a claimed climb from a plain metal converter
    toward a value-added, design-in supplier, still unproven in cash.
11. Judged for fragility, the story rests on four things that must move
    together (margin holding through a metal-price down-cycle, cash
    turning positive, the related-party dependency question resolving,
    and the value-added mix showing up in real segment numbers), half of
    them resting only on the company's own word. The read is fragile.
12. The corpus could not establish per-unit price or volume figures,
    top-customer or top-product concentration percentages, or a
    segment-level revenue split for low, medium and high voltage
    products.
13. The corpus also could not confirm whether a low voltage and high
    voltage factory expansion promised in 2022 was ever completed.
14. One open question: why did management tell the AGM that the
    related company depends on Modison for about a quarter of its sales,
    when the annual report's own explanatory statement reads close to
    half?
15. A second open question: does the record margin survive now that
    silver has fallen sharply from its 2026 peak, or was the FY26 record
    mostly a one-quarter pricing catch-up?

---

## SECTION 6: STANDING EXTRACTION ANNEX

### 1. UNITS

No per-unit price or volume figure (Rs per kg, Rs per tonne, price per
piece, ARPU or equivalent) is printed anywhere in the extracted FY26 AR
text or in the two results filings extracted for this run. A targeted
search across the full AR text for "per Kg," "per unit," "per piece,"
"realisation," "per tonne" and Schedule III-style quantitative details
(consumption in Kgs./M.T./quantity terms) returned no matching
disclosure (Annual_Report.txt, full-text search, this run). Comment: the
figure is not printed; it covers a basket, not one product, since
Modison also does not disclose LV/MV/HV volumes separately (B04). The
only derivable lines are aggregate Revenue from Operations (Rs 710.33 cr
FY26, Rs 490.24 cr FY25, per Note 31 as corrected for an internal
citation typo, B02) and the aggregate cost lines in the P&L; no volume
denominator (kg, tonnes, pieces) exists in this corpus from which a
per-unit figure could be derived. NOT DISCLOSED.

### 2. SEGMENT CAPITAL AND DEBT

Quote: "The Company's business activity falls within a single Primary
segment viz. : 'Manufacturing of Electrical Contacts'. Since the sales
outside India is more than 10% of the total sales, geographical segment
is reported as the secondary segment." (Annual_Report.txt, Note 47
Segment Reporting, p.179.)

Quote (figures, Rs in Lakhs): "Segment Revenue [With India / Outside
India]: 63,084.25 / 8,515.90 (2025-26); 41,549.81 / 7,799.73 (2024-25).
Segment Assets: 47,670.19 / 2,604.67 (2025-26); 29,088.84 / 2,835.63
(2024-25). Addition Fixed Assets: 1,366.17 / — (2025-26); 2,157.03 / —
(2024-25)." (same note, p.179.)

Comment: only geographic (India / Outside India) segment revenue and
segment assets are disclosed. No segment liabilities, no capital
employed by segment, and no borrowings allocated by segment appear
anywhere in the note. Borrowings are unallocated at the company level
only; total borrowings were Rs 174.47 cr FY26 (B02, citing Note 24,
p.161-162). No LV/MV/HV product-line segment exists in this AR at all —
there is a single primary segment.

### 3. GUIDANCE VERSUS ASPIRATION

(a) Guidance with a period:
- "Estimating next year revenue ~Rs 880 cr (moving in that direction)"
  and "~19-20% growth next year" (AGM Jul-2026 transcript, CEO answer to
  Speaker 6, line 118), for FY2026-27.
- "TARGET to maintain AT LEAST 10-12% profit next year (stated as the
  estimate)" (AGM Jul-2026 transcript, line 131-132), for FY2026-27; the
  metric is ambiguous between EBITDA margin and PAT margin (B05 flag).
- "Export ~Rs 85-90 cr FY26, target Rs 100 cr" (AGM transcript, line
  171), for FY2026-27.
- "New target Rs 1,360 cr by 2030" (AGM transcript, line 74), replacing
  an earlier Rs 1,000 cr by 2030 target now expected 2027-28 (same
  line).

(b) Aspiration without a specific numeric target:
- "In this backdrop, the Company's strategic outlook for FY 2026-27 and
  beyond remains focused on strengthening its positioning in high-growth
  application areas and enhancing long-term value creation... The
  Company aims to capitalize on the increasing demand for reliable and
  high-performance electrical switching components... Technological
  advancement will remain a key strategic priority... the Company
  intends to deepen customer relationships, expand its presence in
  domestic and export markets..." (Annual_Report.txt, Strategic Outlook,
  p.81-82.) No number is attached to any of these priorities.

(c) Capacity or capability only:
- Installed capacity and utilisation percentages are NOT DISCLOSED
  anywhere in the FY26 AR or results filings (B04, B09 input_gaps); the
  only capacity figures in the corpus are from the stale Mar-2024
  investor presentation, out of scope for FY26 conclusions (B04).

### 4. CONCENTRATION

Quote: "Customer Concentration Risk — A significant portion of the
Company's revenue is derived from a limited number of OEM customers. Any
reduction in business from key customers could have an adverse impact on
revenue and profitability." (Annual_Report.txt, MD&A Risk table, p.78-79.)

Comment: qualitative only; no top-customer or top-N percentage is
disclosed anywhere, despite being asked twice across sources four years
apart and deflected both times (B05). Product concentration: single
reported primary segment, no LV/MV/HV revenue split (Note 1, Note 47).
Geography concentration: export sales trigger secondary-segment
reporting because they exceed 10% of total sales (Note 47, p.179); FY26
export revenue was Rs 82.16 cr of Rs 710.33 cr total revenue (~11.56%
on the standard base), domestic ~88.4% (AR Directors' Report Export
Highlights, p.38, per B12a's corrected figure). Top product share and
top customer share: NOT DISCLOSED.

### 5. PROMISE LEDGER

| Promise | Date made | Delivery status | Evidence anchor |
|---|---|---|---|
| Revenue Rs 500 cr by FY25 | Sep-2022 (Investor Meet) | Partial — implied ~Rs 490 cr actual, ~98% of target, unacknowledged | Concall_Oct_2022_Transcript.pdf; AR Note 31 (B05) |
| Revenue Rs 1,000 cr by 2030 | Sep-2022 | Delivered/exceeded — now expected 2027-28, target raised to Rs 1,360 cr | AGM_43rd_Jul2026 transcript, line 73-74 (B05) |
| Normalized EBITDA margin 12-14% | Sep-2022 | Delivered/exceeded — FY26 record 16.1-16.2% | AGM transcript line 164; AR MD&A (B05) |
| New unnamed metal-segment expansion "sooner rather than later" | Sep-2022 | Missed / silently dropped — no mention ~3.9 years later | AGM transcript (silence on the topic); B05 dropped_triggers |
| FY27 revenue ~Rs 880 cr; "at least 10-12% profit" | Jul-2026 (AGM) | Partial — Q1 FY27 revenue +101.6% YoY, EBITDA margin ~18.5%, too early to call full-year delivery | B05 promise_delivery; Q1 FY27 results filing |
| MCPL depends on Modison for only ~25% of its sales | Jul-2026 (AGM) | Missed / contradicted — AR Explanatory Statement reads 48.76% (of the proposed ceiling against MCPL's own FY26 turnover) | AGM transcript line 106-108; Annual_Report.txt p.29-30 (this annex, Q8) |
| Vapi refinery fire recovered in 7-10 days, no orders lost | Jul-2026 (AGM) | Partial — directionally true but Rs 10.63 cr booked P&L loss, only Rs 1.70 cr of the claim admitted | AGM transcript line 170; AR Note 39/67 (B02) |

### 6. RESTATED BASES

A full-text search for "restat," "regroup" and "reclassif" across the
extracted FY26 AR text found no note stating prior-period comparatives
were restated for any reorganisation, transfer or reclassification. The
only "reclassified" language found is standard Ind AS accounting-policy
boilerplate on OCI items and equity-investment reserve movements (e.g.
"The Company recognises unrealised and realised gain on equity shares in
FVOCI - Equity investments. The reserve accumulated is reclassified to
retained earnings, when such investments are disposed off," Note
No.19.5, Annual_Report.txt) — a routine accounting-policy note, not a
comparative-period restatement. Comment: NOT DISCLOSED / not found. The
comparative FY25 column printed in the FY26 AR is not flagged anywhere
as restated; B02 independently confirmed restatements_found: [] across
its notes review.

### 7. CORPORATE-ACTION CLAUSES

No scheme of arrangement, demerger, merger, preferential issue or
buyback is in the corpus. Two CARO clauses confirm this directly:

Quote: "The Company did not raise any money by way of initial public
offer or further public offer (including debt instruments) and through
term loans during the year. Accordingly, clause 3(x)(a) of the Order is
not applicable to the Company." (Annual_Report.txt, CARO Annexure,
line 7282-7285.)

Quote: "The Company has not made any preferential allotment or private
placement of shares or convertible debentures (fully or partly or
optionally) and hence reporting under clause 3(x)(b) of the Order is not
applicable to the Company." (same source, line 7287-7290.)

The nearest corporate-action items actually present are two subsidiary
divestments and one material-RPT resolution, none of which carry a
scheme's undertaking/liability-allocation clause structure:

Quote: "M/s. Modison Solartech Private Limited (formerly known as
Modison Hitech Private Limited) ceased to be a subsidiary of the Company
with effect from June 09, 2025." (Directors' Report, line 2136-2138.)

Quote (ratio, dates, appointed-period language, the corpus's clearest
corporate-action clause): "...for an aggregate value of up to Rs.8,000
Lakhs (Rupees Eight Thousand Lakhs Only) for a period commencing from
the 43rd (Forty third) Annual General Meeting upto the date of 44th
(Forty Fourth) Annual General Meeting of the Company to be held in the
year 2027, subject to such contract(s)/arrangement(s)/transaction(s)
being carried out at arm's length and in the ordinary course of
business." (AGM Notice, Resolution 5, p.7, line 342-348.)

Comment: no undertaking or liability-allocation clause exists because
there is no scheme; the effective/appointed-date structure above is the
RPT ceiling's own start (43rd AGM, 21-Jul-2026) and end (44th AGM,
~2027) dates. The Modison HV Private Limited divestment (13-Aug-2026, to
the MD and JMD personally) postdates this AR and is NOT in the corpus as
a primary filing (B08, sourced only from aggregator media); name the
filing to fetch: the BSE board-meeting-outcome filing dated 13-Aug-2026
for Modison HV Private Limited, and any RoC/BSE filing naming the
Modison Solartech buyer and price (the AR's own RPT table for that line
is corrupted in extraction, B02, B08).

### 8. RELATED-PARTY PERIMETER

Named related parties in the AR's Note 43 RPT list (Annual_Report.txt,
p.171-173), nature of transactions as printed, FY26 latest year:

- Mr. Girdhari Lal Modi (Managing Director) — short-term employee
  benefits, post-retirement benefits; remuneration ratio to median
  employee pay 111.38x (Annexure C, B08); rupee figure for this specific
  RPT line not cleanly isolable from the corrupted Note 43 table (B02
  input_gap).
- Mr. Kumar Jay Modi (Joint Managing Director) — short-term employee
  benefits, post-retirement benefits; named as interested in MCPL (AR
  Explanatory Statement, p.28-29).
- Mr. Rajkumar Modi — short-term employee benefits, post-retirement
  benefits.
- Mrs. Chandramani Devi Modi — rent paid, post-retirement benefits.
- Mr. Murlidhar Narayan Nikam (Chief Executive Officer) — short-term
  employee benefits, post-retirement benefits, rent paid.
- Mr. Ramesh M. Kothari — short-term employee benefits.
- Ms. Pooja B. Sinha — short-term employee benefits: Rs 12.97 lakh
  (2025-26) vs Rs 1.71 lakh (2024-25), the one individual line item that
  extracted cleanly against its label (line 9367).
- Ms. Reema Solanki (former Company Secretary, exited Jan-2025) —
  short-term employee benefits.
- Modison Copper Private Limited (MCPL) — purchase/sale of goods and
  services: Rs 5,041.74 Lakh (Rs 50.42 cr) FY26 actual transaction
  value, 11.27% of Modison's annual consolidated turnover of Rs
  70,957.70 Lakh for FY2025-26 (AR Explanatory Statement A(3)/A(4),
  p.29-30); proposed FY27 forward ceiling Rs 8,000 Lakh (Rs 80 cr) = 48.76%
  of MCPL's own FY26 turnover of Rs 16,406.88 Lakh (provisional, subject
  to audit at the time of filing) (same source); MCPL holds 1.26% of
  Modison's paid-up equity via direct shareholding; Modison holds no
  equity in MCPL; MCPL is controlled by promoters and their immediate
  relatives holding over 98% of its equity (AR Explanatory Statement,
  p.28-29).
- Modicon Private Limited — royalty / purchase of goods; amount not
  cleanly isolable from the corrupted Note 43(B) table (B02 input_gap).
- Modison (Partnership Firm) — rent paid, service received /
  maintenance charges; amount not cleanly isolable.
- Dishah Innovative Solutions Private Limited — transactions listed;
  amount not cleanly isolable.
- Modison HV Private Limited (100% subsidiary, consolidated) — net
  worth Rs 28.26 Lakh FY26 (Annual_Report.txt, line 13465).
- Modison Solartech Private Limited (formerly Modison Hitech Private
  Limited) — ceased to be a subsidiary 9-Jun-2025 (line 2136-2138);
  "Sale of shares" RPT line appears against several individual related
  parties in the corrupted table, but the buyer identity and price are
  NOT DISCLOSED / not isolable from this corpus (B02, B08 input_gaps).

Comment: the Note 43(B) transaction-amount table (Annual_Report.txt
lines 9341-9417) extracted with the rupee-value column and the
line-item-name column misaligned. The MCPL Rs 50.42 cr / 11.27% and
48.76% figures are independently cross-verified against the AGM
Notice's Explanatory Statement, a cleanly-extracted table (p.29-30),
which is why they can be stated with confidence. The other related
parties' individual transaction amounts could not be reliably re-paired
to their line-item labels in this run (B02 input_gap, carried forward).

### 9. PLEDGE AND SHAREHOLDING

Quote (operator-supplied screener.in aggregate, NON-ANCHORED tier,
pasted 2026-09-03, twelve quarters Sep-2023 to Jun-2026):

"Promoters: 52.11, 52.11, 52.11, 52.11, 52.11, 52.11, 52.11, 52.11,
52.11, 52.11, 52.16, 52.23. FIIs: 0.00, 0.00, 0.41, 0.48, 0.53, 0.48,
0.55, 0.48, 0.48, 0.48, 0.48, 0.92. DIIs: 0.25, 0.00, 0.00, 0.00, 0.00,
0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00." (operator-supplied-
shareholding-pattern.md.)

Comment: this is the operator-supplied screener.in aggregate, NOT a
filed BSE/NSE shareholding-pattern PDF (NON-ANCHORED tier by the file's
own header). No filed shareholding-pattern PDF exists anywhere in the
ingested corpus for any quarter (B00, B03, B08 all separately confirm
NOT FOUND IN DOCUMENT for promoter %/pledge in the AR itself). The AR's
own Corporate Governance section carries only a shareholding-SIZE
distribution table, not a promoter/FII/DII category table — quote:
"Distribution of Shareholding: The shareholding distribution of the
equity shares as on March 31, 2026 is given below" (Annual_Report.txt,
p.103-104, line 5633-5634), followed by a holding-band table (1-100
shares through 100,001+ shares) with no promoter/institutional category
breakdown. Promoter pledge: NOT DISCLOSED anywhere in the corpus (AR,
CARE rating note, or operator lead); B08's independent search found no
pledge record in any source across the tracked period, not
independently confirmed against a filed encumbrance field. Institutional
holding latest (Jun-2026, non-anchored source): FII 0.92%, DII 0.00%.

### 10. VERIFICATION

Documents quoted in this annex, with filename and date:
- Annual_Report.txt (FY2025-26 Annual Report, 43rd AGM, year ended
  31-Mar-2026, signed 22-May-2026) —
  runs/modisonltd-2026-09-03/inputs/_extracted/annual-report/Annual_Report.txt
- AGM_43rd_Jul2026_webcast_operator_transcript.txt (43rd AGM webcast,
  Jul-2026, operator-supplied, non-filed) —
  runs/modisonltd-2026-09-03/inputs/_extracted/concalls/AGM_43rd_Jul2026_webcast_operator_transcript.txt
- operator-supplied-shareholding-pattern.md (screener.in aggregate,
  pasted 2026-09-03, NON-ANCHORED) —
  runs/modisonltd-2026-09-03/inputs/research/operator-supplied-shareholding-pattern.md

CORPUS COMMIT HASH: fb2cc81c0c7ffd30bab69981c198a37c2c5ce975
