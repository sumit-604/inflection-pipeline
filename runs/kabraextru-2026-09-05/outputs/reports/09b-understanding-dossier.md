# HALT 1 UNDERSTANDING DOSSIER — Kabra Extrusion Technik Ltd (KABRAEXTRU)

Run date: 2026-09-05. Model: claude-sonnet-5. Assembled from committed blocks B00-B09,
B12a-B12d, confidence-delta and B13-synthesis, and their stage reports. No valuation has
run. No price and no verdict-set word appears anywhere in this file, except the one scoped
exception inside Section 2 Part B4, which poses an open pricing question and states no
number and no conclusion. This is an understanding document. What happens next is a
decision for the operator, made after reading it.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

**1. CONCALLS.** None held for KABRAEXTRU itself. `concalls_available: false`, NO-CONCALL
mode declared at intake (B00). No transcript exists for this company at any date. Five
peer-concall files sit in corpus, none of them KABRAEXTRU's own: RAJOOENG Q4 FY23
(16-May-2023), RAJOOENG Q2 FY24 (6-Nov-2023), RAJOOENG Q4 FY24 (18-Apr-2024), RAJOOENG Q2
FY25 (22-Oct-2024, filename mislabeled `Nov_2025`), and HBLENGINE's FY25 AGM transcript
(25-Sep-2025, not an earnings call) (B00 quarter-map). The newest genuine peer earnings
call reaches only October 2024, about 17 months before KABRAEXTRU's own FY26 close
(31-Mar-2026). Since the company itself never files transcripts, this is a structural
company characteristic, not a fresh gap against the run date.

**2. ANNUAL REPORTS.** Two held: `Annual_Report_2026.pdf` (FY2025-26, 170pp, filed
20-Jul-2026) and `Annual_Report_2025.pdf` (FY2024-25, 168pp, filed 24-Jun-2025) (B00). The
latest completed FY (year ended 31-Mar-2026) is present. Only 2 years of bound AR are
held, not 3. Ten years of unanchored screener spreadsheet data (FY17-FY26, Data_Sheet.csv)
extend the backward numeric baseline, but that is not a filed AR (B00, B01).

**3. RESULTS FILINGS.** ABSENT. `results/` holds zero files (B00). No quarterly results
PDF exists in corpus at any date. The newest quarter, Q1 FY27 (ended 30-Jun-2026), exists
only as unanchored screener numbers (sales Rs124.49 Cr, PAT Rs-1.74 Cr) (B01 input_gaps).
Quarter-gap: SEBI LODR requires quarterly results within 45 days of quarter-end, so a Q1
FY27 filing should plausibly exist by mid-August 2026, three weeks before this run date;
none is in corpus. The FY26 audited annual results filing itself (as a discrete BSE/NSE
filing, separate from the bound AR PDF) is also absent.

**4. INVESTOR PRESENTATIONS.** One held: `Investor_Presentation_1.pdf`, quarter ended
31-Dec-2023 (Q3 FY24), filed 25-Jan-2024, 32pp (B00). 2.5 years stale against the run date.
No later deck exists in corpus.

**5. RESEARCH / RATING.** `rating/` and `research/` both hold zero files (B00; research/
carries only a `.gitkeep`). No CRISIL rating rationale and no broker note exist in corpus
at any date. The only rating disclosure anywhere in the corpus sits inside the AR FY26
Corporate Governance Report (p.51): CRISIL long-term A+/Negative to A/Negative (by
5-Apr-2025), then A-/Stable w.e.f. 13-May-2026; short-term A1 to A2+; reason given only as
"basis performance reported for Quarter 3" (B01, B02, B03).

**6. CORPORATE ACTIONS.** `announcements/` holds zero files (B00). No Reg 30 filing (order,
JV, capex, raise) at any date range exists in corpus. The only corporate-action evidence
anywhere is embedded inside the two ARs: the 2022 convertible-warrant preferential issue
(EGM 21-Jan-2022, Rs101.02 Cr, restated annually per Reg 32(7A), AR26 p.18/51-52) and the
FY25 Penta Auto Feeding JV divestment (an exceptional-item stake sale, AR25). The
media-reported 2026 preferential issue (~Rs120-141 Cr, EGM reportedly 2-Sep-2026) is NOT in
corpus at all; AR FY26 is signed 28-May-2026, before that reported EGM (B07, B08).

**7. FRESHNESS PAIR CHECK** (B00 `freshness_pairs`, `freshness_verdict`):
- RESULTS -> CONCALL: SKIPPED (results/ empty; no calls ever held; not applicable).
- RATING BULLETIN -> RATIONALE: **FAIL.** Trigger document: the AR FY26 Corporate
  Governance Report's own table naming the 13-May-2026 CRISIL rating action. Mate expected:
  the CRISIL rating rationale or press release for that action. No bulletin sits in
  `inputs/rating/`; the AR is treated as the present filing that names the action whose
  rationale is missing.
- SEBI ORDER -> ORDER TEXT: PASS. No SEBI order is referenced in the AR beyond the standard
  director not-debarred boilerplate.
- AR -> LATEST AUDITED ANNUAL RESULTS: PASS. FY2025-26 is both the latest audited annual
  and the AR held.

**8. VERDICT LINE: CORPUS GAPPED-FRESHNESS.**

The failed pair's missing mate is **the CRISIL rating rationale for the 13-May-2026 rating
action** (expected source: crisilratings.com press release, or the company's exchange
intimation of the rating revision). Every other gap sits beneath this verdict:

| Gap | Kind | Expected source |
|---|---|---|
| FY26 audited annual results filing (discrete BSE/NSE filing) | findable-missing | BSE / NSE |
| Q1 FY27 (Jun-2026) results filing | findable-missing | BSE / NSE |
| Reg 30 announcements record (orders, JVs, capex, raises) | findable-missing | BSE / NSE |
| Quarterly shareholding-pattern (SAST) filings, twelve quarters | findable-missing | BSE / NSE |
| Broker / research notes | plausibly-nonexistent (thin small-cap coverage; no evidence either way) | company IR page |
| Prospectus | plausibly-nonexistent (long-listed since 1982, CIN L28900MH1982PLC028535) | BSE |
| Investor presentation newer than Q3 FY24 (Dec-2023) | findable-missing | company IR page |
| Windsor Machines peer transcript (named unprompted by Rajoo Engineers as a tracked competitor) | findable-missing | company IR page |
| 2026 preferential issue Reg 30 filings and Form PAS-3 allotment | findable-missing | BSE / NSE |
| Peer transcript freshness (newest genuine peer call Oct-2024, ~17 months short of FY26 close) | structural, not a document gap | n/a |
| Screener CSV defect (Profit_Loss/Balance_Sheet/Cash_Flow/Quarters CSVs are empty formula shells; only Data_Sheet populated, main and all three peers) | technical, collector defect | n/a |
| Sector cap-row ("Cables / Industrial products" flagged for phase-3 confirmation against a capital-goods/industrial-machinery row if one exists) | classification item | n/a |

---

## SECTION 2: MENTAL MODEL DECLARATION

# DRAFT - PENDING OPERATOR SIGN-OFF

This declaration is a transition thesis, not a business description. It is assembled
entirely from B01-B09. Nothing here is signed. Signing happens in claude.ai after live
stress-testing.

### PART A — THE FROM STATE (the anchor, not the model)

**A1. ARCHETYPE** (ARCHETYPE LIBRARY, CLAUDE.md)

| Line | Archetype | Why this fits |
|---|---|---|
| Extrusion Machinery Division | Order-book business (EPC/defence/capital goods) | Engineer-to-order capital equipment sold against an advance plus milestones; exposed to a government infrastructure capex cycle (Jal Jeevan Mission); high working-capital intensity; no order-book total is ever disclosed, itself consistent with this archetype's "order inflow, book-to-bill" variables being the ones that matter (B04, B05 FLAG-NO-ORDER-BOOK-TOTAL-DISCLOSED) |
| Battery Division (Geon, erstwhile Battrixx) | Build-to-spec component maker | Designs pack architecture, battery-management system and housing to each EV-OEM's specification, does not manufacture the cell itself, and is exposed to cell-price/FX pass-through; the archetype's "design-win pipeline" and "content per unit" variables map directly onto the abandoned 90%+ design-win claim and the per-vehicle pack content story (B04, B07) |

**A2. THE SIMPLE ANALOGY.** Kabra Extrusion Technik runs two businesses under one listed
company. The older business, in place for four decades, designs and builds large machines
that turn plastic granules into pipe, film, sheet and compound. Customers pay an advance
plus milestones and take delivery of a finished machine (B04). Six years ago the company
opened a second business, Geon, that buys lithium-ion cells from global suppliers and
assembles them, with a battery-management system and a housing, into packs for electric
two- and three-wheelers, at a plant in Chakan near Pune (B04). The machine business made
more than two-thirds of FY26 revenue and stayed profitable, though its profit fell. The
battery business made under a third of FY26 revenue and lost more money than the year
before, even though it sold more (B04, Note 38). Stopping here, at what the business is
today, misses the point: the company is trying to become something else. That attempt is
the model Part B tests.

### PART B — THE TRANSITION (the model)

Only the Battery/Geon line carries an active, management-narrated tier migration in the
corpus. The Extrusion Machinery line funds the attempt; it carries no claimed migration of
its own in either AR.

**B1. FROM to TO** (QUALITY LADDER, CLAUDE.md), Battery Division (Geon):

- **FROM: R1 COMMODITY PRICE-TAKER.** No pricing power is evidenced. Segment result was
  -31.9% of segment revenue in FY26, widening from -20.1% in FY25 even as segment revenue
  grew 7.2% — the opposite of pricing power or scale economics (Note 38, AR26 p.160-161/
  p.105-106; B04). The emerging-moat scan found NONE, em_score 9 of 92 (B07).
- **TO (claimed): R3 VALUE-ADDED / SPEC'D SUPPLIER.** Management's narrative claims
  spec-in and design capability: a 100+ engineer R&D team, and (in the 2.5-year-stale
  Dec-2023 deck) a 90%+ customer design-win rate, ARAI/AIS-156 accreditation and an
  IATF-approved facility, plus diversification into BESS, telecom, solar and D2C content
  lines (AR26 p.34-38; B04, B07). This claimed destination sits in tension with
  management's own description of the current model as "technology-agnostic" and
  "asset-light" (AR26 p.36) — language that describes something closer to R1/R2, not R3 —
  and the segment's own asset base contradicts "asset-light" outright: Battery ties up more
  net segment capital than the profitable Extrusion line (Rs311.80 Cr vs Rs242.31 Cr,
  standalone Note 38 p.106; B02 rank 10; B12b finding 5).

**B2. THE ENGINE.** (1) Converting the built-out ~7 GWh Chakan capacity (~Rs250 Cr sunk,
capex substantially commissioned — capital work-in-progress fell from Rs50.35 Cr to
Rs12.21 Cr and depreciation rose 89.9% to Rs29.57 Cr in FY26) into utilisation against
management's own claimed Rs1,500+ Cr "optimal" ceiling, so fixed costs are absorbed (AR26
p.36-37; B02 rank 9; B07). (2) Locking in OEM design-in and certification — the abandoned
ARAI/AIS-156, IATF and 90%+ design-win claims — across multiple vehicle programs, replacing
the single-customer concentration pattern that already failed once (Hero Electric/HEVPL,
Rs30.39 Cr receivable, NCLT insolvency admitted 20-Dec-2024) with switching-cost-bearing,
program-level revenue (B04, B07).

**B3. THE PROOF GATE.** Battery/Geon segment result as a percentage of segment revenue
(Note 38 equivalent), at the next full-year or, once resumed, quarterly segment
disclosure. Threshold: the loss ratio must narrow versus the FY26 print of -31.9% (FY25:
-20.1%). **As of this run the gate has NOT fired.** FY26 printed a wider loss ratio than
FY25 — the opposite of the required direction (Note 38, AR26 p.160-161; B04).

**B4. THE RECOGNITION GAP** (open question, resolved at Stage 11). Whether a Battery/Geon
destination beyond its current commodity-assembly state already sits in market pricing is
an open question this run does not resolve. FY26 basic EPS is negative on both the
standalone and the consolidated basis (AR26 p.37, p.122), so no trailing earnings multiple
exists on the current earnings basis to test against. Stage 11's work against the Section
1B framework is what will confirm or deny whether the claimed TO state is already
reflected in pricing, via the PE gap it computes. No number and no conclusion are stated
here.

**B5. THE UGLINESS TEST.** **Draft classification: STRUCTURAL-FEATURE.** This is a
contested, operator-challengeable call; both readings are given in full.

Evidence read as ARTIFACT-OF-CLIMB: the FY26 depressor is segment-identifiable, not
company-wide. The Extrusion Machinery core stayed profitable throughout (segment result
+Rs50.75 Cr FY26, down from +Rs70.14 Cr FY25) (B01). Capex on the Battery facility was
genuinely being commissioned in FY26 — CWIP falling, depreciation stepping up — consistent
with an early-stage capacity build (B02 rank 9; B07).

Evidence read as STRUCTURAL-FEATURE, weighed more heavily in this draft: the segment's own
operating-leverage signature is negative, not merely still-negative. The loss ratio widened
as revenue grew — the opposite of the pattern a temporary capacity ramp would show (B04).
The one hard, quantified forward capex commitment (Rs31.77 Cr) implies only about 16.6%
incremental revenue at the company's own historical fixed-asset turnover, a small fraction
of the claimed Rs1,500+ Cr ceiling, so little committed capital sits behind an imminent
conversion (B07). The emerging-moat scan found NONE (9 of 92) even after crediting the two
strongest available signals (B07). A recurring pattern across both annual reports is of
differentiating claims — market share, ARAI/AIS-156, IATF, 90%+ design-win, a data network
effect — being made once and then dropped rather than updated (B04, B07). The one major
customer relationship on record failed into insolvency (B04, Note 9). This draft weighs
that pattern as the stronger read, but the competing artefact-of-climb evidence above is
real and should be tested directly, not assumed away, in live verification.

**B6. THE TRANSITION FALSIFIER.** A second consecutive full-year, or, once quarterly
filings resume, two consecutive quarters, in which the Battery/Geon segment loss ratio
fails to narrow from the FY26 print of -31.9% of segment revenue despite continued revenue
growth, falsifies the "moving towards profitability as volumes scale" claim specifically
(AR26 p.38; B04, B05). Separately, if the ~Rs150 Cr FY27 order does not convert into
recognised Battery segment revenue, and customer advances — the only order-book proxy
disclosed, down 18.9% to Rs59.39 Cr in FY26 — keep falling, the "order visibility" pillar
of the transition narrative is falsified specifically (B04, B05).

### PART C — WHAT THE MODEL WATCHES (derived from the transition)

**C1. DOMINANT VARIABLES** (derived from B2 and B3):

1. Battery/Geon segment result as % of segment revenue (Note 38). Current state: FY26
   -31.9%, FY25 -20.1%, widening despite revenue growth (B04).
2. Battery/Geon capacity utilisation of the ~7 GWh Chakan facility against the claimed
   Rs1,500+ Cr ceiling. Current state: implied ~9% on FY26 revenue, no company-disclosed
   utilisation figure exists (B04, B07).
3. OEM design-win / customer diversification and credit quality. Current state: one
   customer at 19.11% of FY26 revenue, down from two at 26.94% FY25, but the improvement
   coincides with the HEVPL insolvency, not confirmed new wins (B07, Note 38).
4. The ~Rs150 Cr FY27 order's conversion to recognised revenue. Current state: no
   counterparty named, no Reg 30 corroboration, and customer advances (the order-book
   proxy) fell 18.9% to Rs59.39 Cr in the same year the order is described as secured
   (B04, B05).

**C2. WHAT THE MODEL REJECTS.** The market-size question. B09's own sizing shows a total
addressable market of Rs6,135-10,480 Cr, growing about 15.9% a year, with the company
holding only 7.35% of the served market and 13.6x revenue headroom, a runway classed
STRONG (B09). Yet consolidated revenue fell 5.45% in FY26 while both cited markets grew,
and Battery segment revenue grew at under a third of the cited India EV industry unit
growth rate (7.2% vs 24.6%) (B04, B09). The binding constraint is demonstrated execution
inside a market that already exists, not whether enough market exists to grow into. The
model also rejects the ~40% extrusion market-share claim and the various self-reported
certification and design-win claims as decision-relevant: each was made once, on an
undefined or unsourced base, and dropped rather than repeated or defended the following
year (B04, B05, B07); a peer's own quantified domestic sizing puts KABRAEXTRU's extrusion
revenue at 16-21% of the market, not ~40% (B06 and its verifier finding).

**C3. THE BUSINESS FALSIFIER** (distinct from B6). Evidence that would force re-declaring
the FROM business itself: (1) the Extrusion Machinery segment swinging to a full-year
segment LOSS, not merely a declining profit — this would mean the "profitable core funding
a loss-making bet" framing this whole thesis rests on no longer holds, and the business
would need re-declaring as one with two impaired lines, not one funding engine and one bet
(B01, B04); (2) a further CRISIL downgrade that removes access to the secured, on-demand
working-capital lines the company depends on (Rs140.92 Cr against Rs1.97 Cr standalone
cash) — a funding-structure failure independent of either segment's operating performance
(B02, B03).

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

Drafted per the shared spec at prompts/13-synthesis-pipeline.md, BUSINESS UNDERSTANDING
NARRATIVE section (the five-question spec, defined once and shared with Stage 13; not
restated here). Sourced from B03/B04/B06/B07/B09. This Halt 1 draft is built from the same
evidence base as, and matches, the copy Stage 13 already produced; Stage 13's copy remains
the version of record, updated by later stages.

Two unrelated businesses sit inside one listed company. The Extrusion Machinery Division
made 69.8 percent of FY26 revenue, Rs 314.89 Cr of Rs 451.05 Cr (AR FY26 Note 38
p.160-161). It designs and assembles the machines that turn plastic granules into pipe,
blown film, sheet and compounds, and a pipe maker cannot make pipe without one (AR FY26
p.35-36). The Battery Division, called Geon and formerly Battrixx, made 30.2 percent of
FY26 revenue, Rs 136.11 Cr (AR FY26 Note 38 p.160-161). It buys lithium ion cells from
global suppliers, designs the pack, the battery management system and the housing, and
assembles at Chakan near Pune, but it does not make cells (AR FY26 p.36). Extrusion
customers are pipe, film and flexible packaging makers, mostly Indian, buying engineer to
order machines against an advance plus milestone payments (AR FY26 p.35-36). Exports were
Rs 57.52 Cr, 12.8 percent of FY26 revenue (AR FY26 Note 38 p.160-161). Battery customers
are electric two and three wheeler OEMs, plus retail buyers of a direct to consumer
inverter battery launched in FY26 (AR FY26 p.4-5, p.36). Concentration has already cost
money: one customer was 19.11 percent of FY26 revenue, and Hero Electric, owing Rs 30.39
Cr, went into NCLT insolvency in December 2024 (AR FY26 Note 38 p.106; Note 9 p.87-88).
Neither annual report gives churn, retention or qualification lock in data, so switching
costs are not established.

Machine demand today rides on water infrastructure spending, and the company names Jal
Jeevan Mission disbursement delays as the cause of its FY26 decline, tracked here as the
downstream candidate Jal Jeevan Mission 2.0 fund disbursement pace (AR FY26 p.36). Battery
demand today rides on India EV retail registrations, up 24.6 percent to 2.45 million units
in FY26, tracked as the downstream candidate India EV retail registrations by category (AR
FY26 p.32-33). Forward, the two markets size to Rs 6,135 Cr on the conservative basis and
Rs 10,480 Cr on the realistic basis, growing about 15.9 percent a year, against a served
share of 7.35 percent and 13.6 times revenue headroom. Three outside signals test that
runway: Union Budget capex allocation on the Jal Jeevan Mission and PLI-ACC lines, PLI-ACC
and PM E-DRIVE disbursement milestones, and the lithium carbonate and cell price index. The
company is not capturing it yet, because consolidated revenue fell 5.45 percent in FY26
while both cited markets grew, and battery revenue grew 7.2 percent against the 24.6
percent industry figure printed in the same report (AR FY26 Note 38 p.160-161; p.32-33).
The emerging moat scan scored 9 of 92 and classified NONE, and the machine line carries no
moat: the ~40 percent market share claim appears only in the FY25 report, and gross margin
fell from 38.9 percent to 35.64 percent (AR FY25 p.37; AR FY26 p.37). The battery line
carries none either, because management calls its model technology agnostic and asset
light, a design any entrant can copy, and the Dec 2023 deck claims of ARAI AIS-156
accreditation, an IATF approved facility and a 90 percent plus design win rate appear in
neither annual report (AR FY26 p.36; Dec 2023 deck p.16, p.22). The last two scan
categories agree: category 21, cannibalisation barrier, found no evidence, and category
22, regulatory tailwinds, scored weak because JJM 2.0, PM E-DRIVE and PLI-ACC reach every
competitor equally.

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. Verticals framed (one per dominant variable, Section 2 C1)

**Vertical 1 — Battery/Geon segment result as % of segment revenue.**
- What the corpus establishes: FY26 segment result Rs-43.35 Cr on Rs136.11 Cr segment
  revenue, -31.9%, versus FY25 Rs-25.53 Cr on Rs126.98 Cr, -20.1% (Note 38, AR26
  p.160-161/p.105-106; B04, B02 rank 1). Segment assets Rs364.37 Cr against liabilities
  Rs52.57 Cr, net Rs311.80 Cr, a heavier capital base than the profitable Extrusion line's
  net Rs242.31 Cr (Note 38, standalone p.106; B02 pass-2 finding).
- What it cannot establish: no segment-level cost breakdown (materials, employee cost)
  exists to isolate the margin-compression driver between the two businesses (B04). No
  quarterly segment disclosure exists in corpus to see the trend inside FY26 itself
  (NO-CONCALL, no results filings).
- Questions that decide it: (1) Does the next full-year or quarterly segment print show
  the loss ratio narrowing or widening further? (2) What is the cost composition driving
  the -31.9% margin, and how much of the change is the FY26 depreciation step-up (+89.9%)
  versus genuine unit losses? (3) Is a quarterly segment disclosure obtainable before the
  next AR, to shorten the observation window?

**Vertical 2 — Battery/Geon capacity utilisation against the claimed Rs1,500+ Cr ceiling.**
- What the corpus establishes: ~7 GWh installed capacity at Chakan, ~Rs250 Cr cumulative
  investment (AR26 p.36-37); FY26 segment revenue of Rs136.11 Cr implies roughly 9%
  utilisation of the claimed ceiling, a computed cross-check, not an AR-stated figure
  (B04). Capex substantially commissioned in FY26 — CWIP down, depreciation up (B02 rank
  9).
- What it cannot establish: no company-disclosed utilisation percentage exists anywhere in
  either AR (B04, B07). No segment-level capex split between Extrusion and Battery is
  disclosed, so the Rs31.77 Cr new capital commitment cannot be attributed to either
  business with certainty (B07, B09).
- Questions: (1) Will the company ever disclose a utilisation figure? (2) Is the Rs31.77
  Cr new commitment aimed at Battery capacity, and does its implied ~16.6% incremental
  revenue (B07) square with the Rs1,500+ Cr claim? (3) What did the FY26 gross PP&E
  addition of Rs68.12 Cr actually build?

**Vertical 3 — OEM design-win / customer diversification and credit quality.**
- What the corpus establishes: concentration improved on a headline basis, from two
  customers at 26.94% of FY25 revenue to one customer at 19.11% in FY26 (Note 38, AR26
  p.106); the prior largest relationship on record, Hero Electric (HEVPL), carries a
  Rs30.39 Cr receivable under NCLT insolvency (CIRP admitted 20-Dec-2024), disclosure
  still dated "as at 31-March-2025" in the FY26 report (Note 9, AR26 p.87-88; B04, B07).
- What it cannot establish: whether the concentration improvement reflects genuine
  new-customer wins or is mechanical, the fall-off of the failed HEVPL relationship (B07).
  No customer names, credit-vetting process, or order-book total is disclosed for the
  remaining or new OEM relationships (B04).
- Questions: (1) Who is the remaining ~19% customer, and is it credit-sound? (2) What new
  customers, if any, has Geon signed since the HEVPL failure, and on what payment terms?
  (3) Has a credit-vetting process been put in place for new EV-OEM and D2C customers
  following the HEVPL write-off?

**Vertical 4 — The ~Rs150 Cr FY27 order and the customer-advances proxy.**
- What the corpus establishes: AR FY26 (p.34/37) states a "~INR 150 Crore order secured
  for execution in the upcoming year" with no counterparty named; customer advances, the
  only order-book proxy the AR discloses, fell 18.9% year-on-year, Rs73.22 Cr to Rs59.39
  Cr, in the same year this order is described as secured (Note 20; B04, B05).
- What it cannot establish: no Reg 30 filing or exchange announcement corroborates the
  order; no counterparty, contract terms, or delivery schedule are disclosed (B04, B05).
- Questions: (1) Is there a Reg 30 filing naming the counterparty and terms? (2) Does FY27
  Battery segment revenue show a step-up consistent with a Rs150 Cr order landing? (3) Why
  did customer advances fall in the same year a large order is described as secured?

### 4b. Candidate signal table (B09 SECTION 6 candidates, expanded; UNVERIFIED, verification
happens at Role 5.5 in claude.ai)

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| Jal Jeevan Mission 2.0 fund disbursement pace | Disbursement pace recovers or holds flat while Extrusion segment revenue keeps falling, showing the "JJM delay" explanation for the FY26 decline does not hold | Monthly | JJM dashboard (jaljeevanmission.gov.in), PIB (Ministry of Jal Shakti), sansad.in Q&A |
| India EV retail registrations by category (E-2W/3W/4W/CV) | Registrations keep growing while Battery segment revenue growth stays below half the registration growth rate, confirming share loss rather than a market lag | Monthly | Vahan Dashboard (MoRTH) / FADA monthly retail data |
| Union Budget capex allocation (JJM and PLI-ACC/PM E-DRIVE lines) | Allocation rises for both lines with no matching revenue response in the following two quarters | Event-driven | Union Budget documents (indiabudget.gov.in), CGA monthly expenditure data |
| HEVPL (Hero Electric) NCLT insolvency resolution status | A resolution plan, write-off, or recovery is disclosed and the Rs30.39 Cr receivable position does not change in the company's next filing, showing the disclosure has gone stale again | Event-driven | NCLT cause list / IBBI CIRP filings; MCA-21 filings |
| PLI-ACC / PM E-DRIVE scheme disbursement and localisation milestones | Scheme disbursement proceeds on schedule while Geon's own segment margin does not improve, showing the scheme is not the binding constraint | Quarterly | PIB releases (Ministry of Heavy Industries) / PLI scheme portal |
| Lithium carbonate / EV cell price index | Cell prices fall industry-wide while Battery segment margin still does not improve, isolating the problem to execution rather than input cost | Monthly | Trading Economics / Benchmark Mineral Intelligence spot price; BloombergNEF annual Battery Price Survey |

### 4c. Fragility read

- **variable_count: 7.** Battery loss-ratio narrowing; Battery capacity utilisation rising;
  OEM design-win/customer credit quality without repeat failures; the Rs150 Cr order
  converting; Extrusion recovering as JJM disbursement normalises; cash/liquidity
  stabilising (CFO recovery, no further rating cut) so funding continues; lithium
  cell price/FX not spiking against the pass-through risk the MD&A itself names.
- **verifiability_ratio: 4 of 7 externally observable.** JJM disbursement pace, EV retail
  registrations, the CRISIL rating action and the lithium/cell price index each have a
  named, independent source. Battery segment loss ratio, OEM design-win/customer credit
  quality, and the Rs150 Cr order's conversion are company-narrated only; no independent
  corroboration source is named in corpus for any of the three.
- **single_point_failure:** Battery/Geon segment loss ratio (Note 38 equivalent) failing
  to narrow from the FY26 print of -31.9% of segment revenue. Per B13's own falsification
  metric, this alone converts the transition from unproven to a demonstrated capital sink,
  regardless of the other six variables.
- **fragility_verdict: FRAGILE.**

### 4d. Research brief (live-web work order for claude.ai)

1. Obtain the CRISIL rating rationale for the 13-May-2026 action (and the pre-5-Apr-2025
   action) from crisilratings.com or the company's exchange intimation, to close the
   corpus's freshness gap and the cash-conversion determination named in the flag record.
2. Fetch the FY26 audited annual results filing and the Q1 FY27 (Jun-2026) results filing
   from BSE/NSE.
3. Fetch the SEBI settlement order text (SO/EFD-2/SD/373/FEBRUARY/2021) against Ekta Anand
   Kabra from sebi.gov.in to verify the disgorgement amount and terms independently of
   secondary aggregation.
4. Fetch the 2026 preferential issue's Reg 30 board-outcome filing (7-Aug-2026), the EGM
   notice and outcome (reportedly 2-Sep-2026), and the Form PAS-3 allotment from BSE/NSE,
   including the final allotment size to Independent Director Utpal Sheth.
5. Fetch quarterly shareholding-pattern (SAST) filings for the last twelve quarters from
   BSE/NSE, to establish promoter pledge and institutional holding on a primary-filing
   basis (the corpus currently relies on secondary aggregator snapshots only).
6. Verify the ~40% extrusion machinery market-share claim (AR FY25 p.37, dropped from AR
   FY26) against an independent industry source; the peer's own quantified domestic sizing
   already implies 16-21%.
7. Corroborate the ~Rs150 Cr FY27 order's counterparty and terms via a Reg 30 announcement
   or investor-relations disclosure, if one has since been filed.
8. Check the Windsor Machines corporate filings/IR page directly, since its FY26 screening
   CSV, the one peer source that reaches the FY26 window, shows sales up 72.9% and was
   never examined narratively by the pipeline's peer stage.
9. Check IBBI CIRP filings and the NCLT cause list for the current status of the HEVPL
   (Hero Electric) insolvency proceeding and the Rs30.39 Cr receivable.
10. Check for any proxy-advisory coverage (IiAS, SES, InGovern) of KABRAEXTRU that may
    exist outside the corpus and outside this run's web search.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. Kabra Extrusion Technik runs two businesses in one listed company: a plastics-machine
   maker and a battery-pack assembler.
2. The machine business builds large machines that turn plastic pellets into pipe, film,
   sheet and compound products.
3. The battery business, called Geon, buys lithium-ion cells and assembles them into packs
   for electric two- and three-wheelers at a plant near Pune.
4. Machine customers are pipe and film makers, mostly in India, who pay an advance plus
   milestones for each machine.
5. Battery customers are electric-vehicle makers, plus a new line of retail battery sales
   for inverters started in FY26.
6. One customer relationship already failed: Hero Electric owed Rs 30 crore and went into
   bankruptcy proceedings in December 2024.
7. Demand for machines depends on government water-pipe spending, which the company says
   slowed in FY26.
8. Demand for batteries depends on electric-vehicle sales, which grew fast in FY26, but the
   company's own battery revenue grew much slower than that market.
9. The addressable market for both businesses combined is large and growing, and the
   company holds only a small share of it, so market size is not the constraint; using
   that share is.
10. The machine business has no proven pricing edge: its claimed leadership position and
    market-share number were dropped from the newest annual report with no explanation.
11. The battery business has no proven edge either: an outside scan found no meaningful
    sign of a moat, and several of its differentiator claims from an older investor deck
    never reappeared in either annual report.
12. The core idea under test: an old, profitable machine maker is trying to become a newer
    battery-pack supplier, and the newer business currently loses more money as it grows,
    not less.
13. Weighing the pieces together, the pattern reads more like a feature of the business
    than a passing phase, because a loss should shrink as sales grow if this were simple
    early scaling, and here it grew wider instead.
14. The corpus could not establish a rating agency's reasoning for two rating downgrades
    in the same year, and could not establish twelve quarters of promoter pledge or share
    ownership, because those documents are missing.
15. The biggest open questions are whether the battery business's loss will narrow in the
    next reporting period, and whether the company's cash position and credit rating can
    hold while it waits to find out.

---

## SECTION 6: STANDING EXTRACTION ANNEX

Ten standing questions, answered from the corpus, quote-then-comment, filename and page
anchor on every printed number. NOT DISCLOSED is written where the corpus does not carry
an answer, with the reason and the filing to fetch named.

### 1. UNITS

No per-unit realisation figure is printed for either segment in either Annual Report. The
closest volume figure printed is: *"installed battery pack manufacturing capacity of
approximately 7 GWh... over 400,000 battery packs deployed in the field"* (Annual_Report_2026.pdf
p.5, repeated in substance p.36-37). This is a cumulative, since-2020 figure, not an FY26
unit count, and it is a basket figure (multiple pack configurations), not a single SKU.
Comment: no realisation-per-tonne, per-pack ASP, or per-machine price is printed anywhere
in either AR; B04's own review confirms `revenue_per_unit` and `margin_per_unit` NOT FOUND
for both segments. The volume and revenue lines from which no reliable per-unit figure can
be derived: Extrusion segment revenue Rs314.89 Cr and Battery segment revenue Rs136.11 Cr
(Note 38, Annual_Report_2026.pdf p.160-161), against the cumulative "400,000+" packs figure
above and no disclosed FY26 machine count for Extrusion.

### 2. SEGMENT CAPITAL AND DEBT

Standalone Note 38 (Annual_Report_2026.pdf p.106), FY26 only (FY25 segment
assets/liabilities were not extracted in this run's passes and are not quoted here):

| | Segment assets | Segment liabilities | Net segment capital |
|---|---|---|---|
| Extrusion Machinery | Rs363.38 Cr (Rs36,338.05 lakh) | Rs121.07 Cr (Rs12,107.34 lakh) | Rs242.31 Cr |
| Battery Division (Geon) | Rs364.37 Cr (Rs36,437.25 lakh) | Rs52.57 Cr (Rs5,256.96 lakh) | Rs311.80 Cr |

Comment: the loss-making Battery Division ties up more net capital than the profitable
Extrusion line. Borrowings are **not allocated by segment anywhere in either AR.** The
total, unallocated company borrowing: current secured borrowings Rs141.03 Cr (Rs14,102.70
lakh, Note 17, standalone balance sheet, Annual_Report_2026.pdf p.64); total borrowings
Rs141.09 Cr FY26 versus Rs125.79 Cr FY25 (Note 43/35). Note 38 gives segment assets and
liabilities but not segment borrowings, so it cannot be said from the corpus which
segment's cash needs the secured working-capital facility is actually funding.

### 3. GUIDANCE VERSUS ASPIRATION

| Claim (quote) | Source | Classification |
|---|---|---|
| *"KET enjoys market leadership status in the extrusion market with ~40% market share in its product category as on FY25"* | AR FY25 p.37 | (a) guidance-adjacent claim with a period (FY25 snapshot); dropped from AR FY26 entirely, no restated figure |
| *"actively pursuing new industry segments, including E-Low Commercial Vehicles, E-4 Wheelers etc. in the upcoming fiscal year"* | AR FY25 p.38, for FY26 | (a) guidance with a period (FY26); AR FY26 does not confirm entry into either named segment |
| *"secured a ~INR 150 Crore order for execution in the upcoming year"* | AR FY26 p.34/37, for FY27 | (a) guidance with a period (FY27); no counterparty, no Reg 30 corroboration |
| *"at optimal levels, the existing facility can generate INR 1,500+ crore revenue"* | AR FY26 p.34/37 | (c) capacity/capability only, no period |
| *"The battery business is expected to move towards profitability as volumes scale up"* | AR FY26 p.38 | (b) aspiration without a period |
| *"Geon aspires to be a key player in the BESS arena in the coming years"* | AR FY25 p.38, repeated in substance AR FY26 p.38 | (b) aspiration without a period; repeated across both years with no progress metric |
| Capital commitment (contracted, not yet executed): Rs31.77 Cr (Rs3,177.38 lakh) | AR FY26 Note 41(b) p.110 | not a forward claim; a disclosed contractual commitment, included for completeness |

### 4. CONCENTRATION

- **Product:** disclosed only at the two-segment level — Extrusion 69.8% (Rs314.89 Cr),
  Battery 30.2% (Rs136.11 Cr) of FY26 revenue (Note 38, Annual_Report_2026.pdf
  p.160-161). No finer product/machine-type breakdown is printed. **Top product share:
  NOT DISCLOSED** below the segment level.
- **Customer:** *"one customer accounted for 19.11% of FY26 revenue from operations
  (previous year: two customers, 26.94%)"* (Note 38, Annual_Report_2026.pdf p.106,
  paraphrase of the disclosed percentages; the customer is not named, consistent with Ind
  AS 108's non-naming convention). **Top customer share: 19.11% (FY26), name NOT
  DISCLOSED.**
- **Geography:** exports Rs57.52 Cr of Rs450.998 Cr FY26 revenue, 12.8% (Note 38,
  Annual_Report_2026.pdf p.160-161); domestic 87.2% by residual.

### 5. PROMISE LEDGER

| Promised in | Promise (quote or close paraphrase) | Outcome | Evidence anchor |
|---|---|---|---|
| AR FY25 p.36/38 | Geon to enter E-Low Commercial Vehicles and E-4 Wheelers in FY26 | Not confirmed by name in AR FY26; different new segments (RESS, inverter D2C) substituted instead, no explanation given | B05 promise_delivery row 1 |
| AR FY25 p.37 | ~40% extrusion market share maintained | Claim dropped entirely from AR FY26; extrusion segment revenue fell 13.2% and segment result fell 27.6% | B05 promise_delivery row 2 |
| AR FY25 p.37 outlook | "Well-positioned to capitalize on anticipated growth across both divisions" | Revenue -5.45%, EBITDA -74.88%, PAT swung to a loss, dividend cut to nil; external causes cited for extrusion only, none given for battery | B05 promise_delivery row 3 |
| AR FY25 p.38 | Geon to become a key player in BESS | RESS/BESS/inverter D2C products launched (real progress), but battery segment loss widened 69.8% despite 7.2% revenue growth, no explanation given | B05 promise_delivery row 4 |
| AR FY25 p.30-31, p.36-37 | Continued R&D investment across both divisions | R&D spend cut 67.1% (Extrusion) and 78.6% (Geon), while AR FY26 narrative claims Geon "accelerated its R&D," a direct contradiction, unaddressed | B05 promise_delivery row 5 |

Delivered: 0 of 5. Partial: 2. Missed: 3. Credibility grade assigned by the no-concall
delivery check: D (B05 `credibility_grade`).

### 6. RESTATED BASES

Quote, standard note both statements: *"Previous year's figures have been regrouped
wherever considered necessary to make them comparable with those of the current year"*
(standalone Note 47, Annual_Report_2026.txt, p.113 by page-marker position; consolidated
equivalent p.169). No quantified regrouping schedule accompanies this boilerplate. Against
it, an exactly offsetting reclassification is independently identifiable in the printed
comparatives: standalone employee benefits expense reads Rs5,907.53 lakh in AR FY25 (Notes
26/29, AR FY25 p.19) but Rs6,328.67 lakh as the FY25 comparative printed in AR FY26 (p.17),
while standalone other expenses reads Rs7,473.91 lakh in AR FY25 but Rs7,052.77 lakh as the
FY25 comparative in AR FY26 — a Rs421.14 lakh reclassification, present identically in both
the standalone and consolidated columns. Comment: the boilerplate note covers this
reclassification, but the note itself names no amount, no head, and no reason; the effect
is real (FY26 employee cost reads as a smaller or larger year-on-year change depending on
which base is used) and is only findable by comparing the two ARs' own printed comparative
columns against each other, not from either AR read alone (B12b finding 3; B13 rerun item
1).

### 7. CORPORATE-ACTION CLAUSES

**In corpus:** the 2022 convertible-warrant preferential issue. Quote: *"30,70,516
convertible warrants"* issued to the promoter group and investors at Rs329/share, approved
at an EGM held 21-Jan-2022, raising Rs101.02 Cr cumulatively; the FY26 Board's Report and
the Corporate Governance Report's Reg 32(7A) utilisation table both restate that *"entire
proceeds... [were] fully utilized"* as at 31-Mar-2026 (Annual_Report_2026.pdf p.18,
p.51-52). Ratio: one equity share per warrant on conversion (100% converted, no lapse).
Appointed/effective date: EGM approval 21-Jan-2022; full utilisation confirmed as at
31-Mar-2026. No liability-allocation clause applies; this is a capital-raise instrument,
not a demerger or merger.

The FY25 Penta Auto Feeding JV divestment is an exceptional-item stake sale (AOC-1 records
the prior holding at 49.94%, not the 50:50 the Dec-2023 deck had claimed), not a scheme
under the Companies Act or SEBI ICDR; no undertaking, liability-allocation clause, or
appointed/effective date is printed for it, since none is required for a stake sale of this
kind.

**Not in corpus:** the 2026 preferential issue (~Rs120-141 Cr at Rs375/share to Singularity
Large Value Fund III, Nitish Mittersain, Utpal Sheth and others, board approval reportedly
7-Aug-2026, EGM reportedly 2-Sep-2026) is entirely absent; AR FY26 is signed 28-May-2026,
before this reported EGM. Filing to fetch: the BSE/NSE Reg 30 board-outcome filing, the EGM
notice and outcome, and the Form PAS-3 allotment (naming ratios, pricing basis under SEBI
ICDR, and the allotment to each allottee including Independent Director Utpal Sheth).

### 8. RELATED-PARTY PERIMETER

Standalone Note 39C, FY26 (Annual_Report_2026.pdf p.105-106), promoter-group and JV
entities named, nature and amount of transaction:

| Entity | Nature | FY26 amount |
|---|---|---|
| Kolsite Corporation LLP (promoter entity) | Rent income | Rs59.73 lakh |
| Kolsite Corporation LLP | Reimbursement expenses | Rs2.24 lakh (Rs2.19 lakh FY25) |
| Plastiblends India Ltd (promoter cross-holding, listed) | Purchase of goods & services | Rs8.43 lakh (Rs12.58 lakh FY25) |
| Plastiblends India Ltd | Rent expense | Rs14.86 lakh |
| Plastiblends India Ltd | Rent income | Rs3.03 lakh |
| Plastiblends India Ltd | Reimbursement income | Rs0.36 lakh (Rs15.84 lakh FY25) |
| Plastiblends India Ltd | Reimbursement expense (new category, NIL FY25) | Rs16.68 lakh |
| Maharashtra Plastics & Industries | Purchase of goods & services | Rs0 (Rs0.05 lakh FY25) |
| Maharashtra Plastics & Industries | Rent income | Rs2.01 lakh |
| Kabra Mecanor Belling Technik (JV) | Reimbursement income | Rs1.07 lakh (Rs1.95 lakh FY25) |
| VTRO Motors Pvt Ltd (other entity) | Legacy credit balance | Rs149.70 lakh at FY25-end, cleared to nil by FY26-end |

Comment: total standalone RPT quantum across these lines is approximately Rs2.18 Cr against
Rs450.998 Cr standalone revenue, about 0.48% — immaterial. No loans to promoters, directors
or KMP (Note 46(a)); no corporate guarantee outstanding for a related party (the Varos
guarantee line shows nil both years). The Board's Report and Corporate Governance Report
both state: *"there were no materially significant related party transactions that may have
potential conflict with the interests of the Company at large"* (Annual_Report_2026.pdf
p.18, p.51). The Plastiblends "Reimbursement expense" of Rs16.68 lakh (a first-time RPT
category, FY26 only) is a different, smaller item from the unrelated Rs1,668.41 lakh
(Rs16.68 Cr) unexplained "Other" line inside Note 23 other income; the two figures share a
number by coincidence and should not be conflated.

### 9. PLEDGE AND SHAREHOLDING

Promoter holding, AR Note 14.4, the only in-corpus source (three annual snapshots, not
quarterly): FY24 60.24%, FY25 60.24% (stated change +0.00%), FY26 60.49% (stated change
+0.25%). **Twelve quarters of pledge and shareholding as filed: NOT DISCLOSED.** Reason:
`shareholding/` holds zero files in corpus; no primary NSE/BSE quarterly shareholding-pattern
(SAST, SEBI LODR Regulation 31) filing was collected. Filing to fetch: NSE/BSE quarterly
shareholding-pattern filings for the last twelve quarters. Promoter pledge does not appear
in either AR at all; secondary aggregator sources (Trendlyne, upmazing.ai, undated
snapshots) report 0.00%, but this is web/secondary evidence, not a primary filing, and is
not treated as anchored corpus evidence here (B08).

Institutional holding, latest (FY26), from the AR26 Corporate Governance Report
shareholding-category table: Mutual Funds 0.01%, FPI 0.35% (Annual_Report_2026.pdf
p.49-50, as reported by B08's promoter check).

### 10. VERIFICATION

Documents quoted in this annex:
- `Annual_Report_2026.pdf` / `Annual_Report_2026.txt` — Annual Report FY2025-26, filed
  20-Jul-2026 (170pp).
- `Annual_Report_2025.pdf` / `Annual_Report_2025.txt` — Annual Report FY2024-25, filed
  24-Jun-2025 (168pp).
- `screening/screener-Data_Sheet.csv` — screener.in consolidated data, undated live
  snapshot, cited only as screener data, never as a filing.

CORPUS COMMIT HASH: c446c2471c9f8ff2838694ce6169f1c95597599b

```yaml
stage: B09b-dossier
company: "KABRAEXTRU"
run_date: "2026-09-05"
model: claude-sonnet-5
status: complete
corpus_verdict: "CORPUS GAPPED-FRESHNESS"
corpus_gaps:
  - document: "CRISIL rating rationale for the 13-May-2026 action (and the pre-5-Apr-2025 action)"
    expected_source: "rating agency site"
    kind: "freshness-pair"
  - document: "FY26 audited annual results filing (discrete BSE/NSE filing)"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "Q1 FY27 (Jun-2026) results filing"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "Reg 30 announcements record (orders, JVs, capex, raises)"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "Quarterly shareholding-pattern (SAST) filings, last twelve quarters"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "Broker / research notes"
    expected_source: "company IR page"
    kind: "plausibly-nonexistent"
  - document: "Prospectus"
    expected_source: "BSE"
    kind: "plausibly-nonexistent"
  - document: "Investor presentation newer than Q3 FY24 (Dec-2023)"
    expected_source: "company IR page"
    kind: "findable-missing"
  - document: "Windsor Machines peer transcript"
    expected_source: "company IR page"
    kind: "findable-missing"
  - document: "2026 preferential issue Reg 30 filings and Form PAS-3 allotment"
    expected_source: "BSE"
    kind: "findable-missing"
archetypes:
  - line: "Extrusion Machinery Division"
    archetype: "Order-book business (EPC/defence/capital goods)"
  - line: "Battery Division (Geon, erstwhile Battrixx)"
    archetype: "Build-to-spec component maker"
transition:
  - line: "Battery Division (Geon)"
    from_tier: "R1 COMMODITY PRICE-TAKER"
    to_tier: "R3 VALUE-ADDED / SPEC'D SUPPLIER (claimed)"
    engine: "(1) Converting the built-out ~7 GWh Chakan capacity (~Rs250 Cr sunk, capex substantially commissioned) into utilisation against the claimed Rs1,500+ Cr ceiling; (2) locking in OEM design-in/certification across multiple vehicle programs to replace single-customer concentration with program-level, switching-cost-bearing revenue"
    proof_gate: "Battery/Geon segment result as % of segment revenue (Note 38 equivalent) narrowing versus the FY26 print of -31.9% (FY25: -20.1%); NOT fired as of this run, since FY26 widened rather than narrowed"
    recognition_gap: "Open question, resolved at Stage 11 via the PE gap: whether a Battery/Geon destination beyond its current commodity-assembly state is already reflected in market pricing; FY26 EPS is negative on both bases, so no trailing earnings multiple exists on the current earnings basis to test against"
    ugliness: "STRUCTURAL-FEATURE"
    transition_falsifier: "A second consecutive full-year, or two consecutive quarters once resumed, in which the Battery/Geon segment loss ratio fails to narrow from the FY26 print of -31.9% of segment revenue despite continued revenue growth; or the ~Rs150 Cr FY27 order failing to convert into recognised segment revenue while customer advances keep falling"
dominant_variables:
  - "Battery/Geon segment result as % of segment revenue (Note 38): FY26 -31.9%, FY25 -20.1%, widening despite revenue growth"
  - "Battery/Geon capacity utilisation of the ~7 GWh Chakan facility against the claimed Rs1,500+ Cr ceiling: implied ~9% on FY26 revenue, no company-disclosed utilisation figure"
  - "OEM design-win / customer diversification and credit quality: concentration improved to one customer at 19.11% FY26 from two at 26.94% FY25, but coincides with the HEVPL insolvency, not confirmed new wins"
  - "The ~Rs150 Cr FY27 order's conversion to recognised revenue, against customer advances (the order-book proxy) falling 18.9% to Rs59.39 Cr in FY26"
business_falsifier: "Extrusion Machinery segment swinging to a full-year segment LOSS (not merely declining profit), which would mean the profitable-core-funding-a-loss-making-bet framing no longer holds; or a further CRISIL downgrade removing access to the Rs140.92 Cr of on-demand secured working-capital lines the company depends on against Rs1.97 Cr standalone cash"
mental_model_status: "DRAFT - PENDING OPERATOR SIGN-OFF"
fragility:
  variable_count: 7
  verifiability_ratio: "4 of 7 externally observable"
  single_point_failure: "Battery/Geon segment loss ratio (Note 38 equivalent) failing to narrow from the FY26 print of -31.9% of segment revenue"
  fragility_verdict: "FRAGILE"
candidate_count: 6
research_brief_items: 10
plain_summary_points: 15
annex:
  present: true
  questions_answered: 10
  corpus_commit_hash: "c446c2471c9f8ff2838694ce6169f1c95597599b"
```
