# KROSS: Halt 1 Understanding Dossier (Phase 1, run 2026-09-27)

Assembly only. Every claim below traces to a committed block (B00-B09,
B12a-d, confidence, B13) or, in Section 6 only, to a corpus PDF page. No
web search ran in this container. No valuation, price, or verdict
vocabulary appears except the one Section 2 Part B4 exception and the
corpus verdict line permitted by the operating rules.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

1. **CONCALLS.** Four transcripts held: Concall_Nov_2025 (Q2 FY26),
   Concall_Feb_2026 (Q3 FY26), Concall_May_2026 (Q4 FY26), Concall_Jul_2026
   (Q1 FY27) (B00 corpus_manifest). Most recent quarter covered: Q1 FY27
   (quarter ended 30-Jun-2026). Given the run date (27-Sep-2026), the next
   reportable quarter is Q2 FY27 (ended 30-Sep-2026), whose results and
   call are not yet due under the SEBI 45-day window; no more-recent
   transcript is plausibly missing.
2. **ANNUAL REPORTS.** Two years held: Annual_Report_2026.pdf (FY2025-26,
   primary) and Annual_Report_2025.pdf (FY2024-25, backward check) (B00).
   The latest completed FY (FY26) is present. Fewer than 3 years are held
   as annual reports; Kross listed 16-Sep-2024, so only two ARs exist as a
   public company. The prospectus (Sep-2024) carries restated FY22-FY24
   financials as the backward substitute (B00 corpus_manifest).
3. **RESULTS FILINGS.** Latest: Q1 FY27 unaudited results, filed
   24-Jul-2026 (board outcome, quarter ended 30-Jun-2026). Also held: Q4
   FY26 / FY26 audited (12-May-2026) and Q3 FY26 unaudited (29-Jan-2026)
   (B00). Quarter-gap: Q2 FY26 results filing is not held (B00 input_gaps,
   "RESOLVED AT INTAKE" note; gate-recommendation.md Gaps table). No gap
   between the latest results filing and the latest AR.
4. **INVESTOR PRESENTATIONS.** Two decks held: Q4 FY26 (12-May-2026) and Q1
   FY27 (25-Jul-2026, the latest) (B00). Q3 FY26 and Q2 FY26 decks are not
   held.
5. **RESEARCH / RATING.** rating/ holds the 02-Jun-2026 Reg 30 letter
   enclosing the full India Ratings rationale of 01-Jun-2026 (IND
   A/Stable/IND A1 affirmed) (B00). The CARE withdrawal (04-Dec-2025) sits
   in announcements/, not rating/. research/ is EMPTY: no broker note of
   any kind (B00 input_gaps, "research: EMPTY. No broker notes.").
6. **CORPORATE ACTIONS.** 23 announcement filings held, Nov-2025 to
   Sep-2026: monitoring agency reports, statement of deviation, CARE
   withdrawal, product launch, capacity addition, SAST 29(2) disclosures,
   secretarial compliance, resignations and directorate change (24-Jul-26),
   Q1 FY27 press release, preferential issue board outcome and postal
   ballot notice (31-Aug-26), AGM outcome, postal ballot corrigendum
   (23/24-Sep-26) (B00). Filings before Nov-2025 (Q1/Q2 FY26 period) are
   not held: a PARTIAL documented-action record.
7. **FRESHNESS PAIR CHECK.** B00 `freshness_verdict` = "FRESHNESS PAIRS OK".
   All four named pairs PASS: RESULTS to CONCALL (Q1 FY27 results paired
   with Concall_Jul_2026); RATING BULLETIN to RATIONALE (same PDF carries
   both); SEBI ORDER to ORDER TEXT (no SEBI order found in the corpus at
   all, so the pair is vacuously satisfied, flagged for a stage 8
   re-check, which B03/B08 both performed and found nothing); AR to LATEST
   AUDITED ANNUAL RESULTS (Annual_Report_2026.pdf pairs with the
   12-May-2026 audited results). No pair failed.
8. **VERDICT LINE.**

   **CORPUS GAPPED**: research/ is EMPTY (no broker note; findable-but-
   plausibly-nonexistent — this is an under-covered small/micro-cap and the
   absence is itself a data point on coverage, not a collection failure,
   per B00 corpus_verdict_hint). Other named gaps, all findable-but-missing:
   Q2 FY26 results filing (BSE); pre-Nov-2025 announcement filings (BSE);
   Q2 FY26 and Q3 FY26 investor decks (company IR page); shareholding
   filings before 31-Mar-2026 (NSE, needed to verify the COMPANY MEMORY
   claim of DII 9.72% at Mar-2025, per B08 input_gaps); FY25 Bull Auto
   Parts related-party amount, held in Annual_Report_2025.pdf but not
   extracted in this run (B08 input_gaps); identity of three of four
   Aug-2026 preferential-issue non-promoter allottees (claude.ai live
   check, B08 input_gaps); the postal ballot result and allotment, due
   03-Oct-2026, after this run's date (B00 pending_events). None of these
   gaps is a freshness-pair failure.

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT - PENDING OPERATOR SIGN-OFF.** This is a transition thesis, not a
business description. Signing happens only in claude.ai after live-web
stress-testing.

### PART A — THE FROM STATE

**A1. ARCHETYPE.** Single reporting business (Note 45: "the Company is
engaged in manufacturing of critical components for commercial vehicles
and Tractors... assessed and reviewed by the Chief Operating Decision
Maker as a single operating segment," AR PDF p.81, printed p.156). Primary
archetype: **build-to-spec component maker** (customer capex cycle,
design-win/re-qualification pipeline, input-cost pass-through) (B04
business_type, analyst_note). A **commodity-converter** engine (spread
between purchased and self-made steel shapes) is layered on top of this
base as the transition mechanism (B04 analyst_note), not a separate FROM
archetype; Section 1B Amendment 17 restrictions on converter-classified
names should be checked against how much of the thesis rests on this
spread versus continued OEM demand (B04 analyst_note).

**A2. THE SIMPLE ANALOGY.** Kross forges, casts, machines and now
increasingly extrudes the heavy steel parts that let trucks, trailers and
tractors carry load and turn without breaking. It buys steel, shapes it
into axles, suspension parts, shafts and gears to a customer's drawing or
its own design, and sells to truck and tractor makers on purchase orders
with no long-term contracts (B04 revenue_streams; business-narrative.md).
Two of every five rupees of revenue come from Kross's own trailer axle
and suspension design; the rest is built to somebody else's print
(B04 revenue_streams, 42.61% + 42.97% + 9.48% + 3.60% + 1.38%).

### PART B — THE TRANSITION

**B1. FROM to TO.** One line (the whole company, per Note 45 single
segment). FROM: **R2 COST-ADVANTAGED CONVERTER-adjacent build-to-spec
supplier** — mid-teens ROCE (15.03% FY26, down from a post-IPO-rebase
28.15% FY24, Note 52, AR PDF p.82-83 printed p.159-160), weak general
pricing power (steel cost passes through with a lag, confirmed by all
three peers, B06 industry_cross_read), moderate switching costs from
OEM safety-critical requalification (B04 moats_present). TO (most
evidenced path): **R3 VALUE-ADDED / SPEC'D SUPPLIER** — the claim is that
completed backward integration (axle beam extrusion, seamless tube) plus
proprietary design (India's first single-piece axle beam extrusion
process, B04 moats_present) lift margin from ~13% toward 14-15% and
deepen spec-in beyond generic build-to-print (B04, B07). Alternate
reading not ruled out: the company stays at R2, with the backward
integration only defending the existing mid-teens margin rather than
lifting it to spec'd-supplier economics (ROCE has fallen for two straight
years even as the IPO tripled net worth, B01 FLAG-ROCE-BASE-EFFECT; B03).
The observation that separates the two readings is Q2/Q3 FY27 EBITDA
margin and ROCE once both plants are running above 50% utilisation.

**B2. THE ENGINE.** (1) Backward integration into steel shapes: the Rs 25
Cr axle beam extrusion line (in commercial production Jul-2026, ~6 months
late) and the Rs 167 Cr, 1,20,000-tonne seamless tube plant (due around
Q4 FY27) replace a purchased input with a self-made one (AR PDF p.13
printed p.20-21; PDF p.30 printed p.58; B04 moats_present; B05 guidance).
(2) Proprietary design: Kross's own trailer axle/suspension design and
the axle-beam-extrusion process itself, which the corpus places Kross
among "a handful of integrated makers" in India (B04 moats_present;
business-narrative.md).

**B3. THE PROOF GATE.** Standalone EBITDA margin at or above 14.0% for
two consecutive quarters, once axle beam extrusion utilisation clears
50% of the 7,500 units/month line (B04 must_track_metrics; B04
unit_economics key_lever; B05 quarters_analysed guidance). Until this
fires, the margin-transition claim is narrative: Q1 FY27 delivered 12.23%,
one quarter after management reaffirmed 14-15% (B05 FLAG-MARGIN-MISS).

**B4. THE RECOGNITION GAP** (to be resolved at Stage 11). Open question,
not concluded here: does the market already reflect the margin-recovery /
spec'd-supplier TO state in current pricing, leaving little re-rating
room even if the transition proves real? Or does pricing still sit at the
FROM-state converter/build-to-spec level, leaving the re-rating engine
intact if the margin claim is confirmed? Stage 11 resolves this via the
Section 1B destination-PE gap; no number or conclusion is stated here.

**B5. THE UGLINESS TEST.** Today's ugly optic is cash conversion: CFO/PAT
0.180x (FY25) and 0.503x (FY26), FCF negative and worsening to -Rs72.43
Cr (FY26), working-capital days up from 89.01 (FY22) to 131.73 (FY26)
(B01 Block B; B03 FLAG-CASH). Most evidenced reading: **ARTIFACT-OF-
CLIMB** — the FCF gap tracks the capex ramp (capex Rs100.18 Cr FY26 on
CFO Rs27.75 Cr) funded by IPO proceeds, and the company's own Note 52
remark ties rising working capital to "increase in revenue along with
increase in working capital following lower current liabilities"
(AR PDF p.82-83, printed p.159-160). A minority reading is not ruled
out: **STRUCTURAL-FEATURE** — receivables turnover has fallen for three
straight years (7.67x to 4.25x to 3.55x), the >6-month aged bucket grew
from 8.9% to 11.0% of gross while the ECL allowance stayed flat at
Rs14.35 Mn, and Rs349.00 Mn of bills are discounted with the banks with
recourse (B02 rank 1, 2, 4; Note 11 AR PDF p.69 printed p.132-133; Note
34 AR PDF p.76-77 printed p.146-147). The observation that separates the
two: H1 FY27 (to 30-Sep-2026) receivables growth against revenue growth,
read with the aged-bucket split by customer class (fabricator vs OEM vs
export) (gate-recommendation.md FLAG-CASH block).

**B6. THE TRANSITION FALSIFIER.** EBITDA margin stays below 13% for two
or more quarters after BOTH the axle beam extrusion line and the seamless
tube plant are fully commissioned and running above 50% utilisation. If
the engine is built and running but the P&L never shows the claimed
spread, the transition thesis (not necessarily the underlying component
business) is falsified.

### PART C — WHAT THE MODEL WATCHES

**C1. DOMINANT VARIABLES.**
1. EBITDA margin trajectory vs the 14-15% FY27 guide. Current state: Q1
   FY27 delivered 12.23%, missing guidance reaffirmed one quarter earlier
   (B05 FLAG-MARGIN-MISS).
2. Axle beam extrusion utilisation (7,500 units/month capacity). Current
   state: actual output ~3,500-4,000 axles/month, under 50% (B12b finding;
   B05 guidance).
3. Seamless tube commissioning against the "around Q4 FY27" target.
   Current state: "construction completed" (Q3 FY26 call) walked back to
   "almost complete" (Q4 FY26 call), no reconciliation given (B05
   timeline_slippages).
4. Cash conversion / working-capital days. Current state: CFO/PAT 0.503x
   FY26, WC days 131.73 FY26, both deteriorating (B01 Block B; B03
   FLAG-CASH).

**C2. WHAT THE MODEL REJECTS.** Market-size questions. Stage 9 grades the
runway GOOD with 4.01x revenue headroom against the serviceable
addressable market, and finds capacity (the 81% mechanical capex-embedded-
growth ceiling) "comfortably exceeds" the 5-year SOM's incremental revenue
need (B09 capacity_check, runway_class). The binding constraint this
model names is execution and margin delivery, not market size or plant
capacity; questions that ask "is the market big enough" are noise this
model declares resolved.

**C3. THE BUSINESS FALSIFIER.** Loss of a named top-5 OEM program (Tata
Motors or Ashok Leyland, the two largest and longest-tenured relationships,
B03 ar_new_downstream_entities context) or documented evidence of OEM
in-sourcing or de-qualification, given 59.47% top-five customer
concentration and no long-term contracts on any revenue line (B04
revenue_streams; B04 first_deterioration_signals; business-narrative.md
anchors). This would force a re-declaration of the FROM business itself
(the safety-critical component supply relationship), distinct from B6,
which only kills the margin-transition claim while leaving the base
supply business intact.

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

Kross makes the heavy metal parts that let trucks, trailers and tractors
carry load and turn without breaking. In FY26, 43% of sales came from
complete trailer axles and suspension assemblies built to Kross's own
design, and another 43% came from axle shafts, flanges, differential
spiders and anti-roll bars forged and machined to truck makers' drawings
(B04 revenue_streams, AR PDF p.23 printed p.40). Tractor parts made up 9%,
exports 4%, and tipping jacks and other items the rest. These are safety-
critical parts, so a truck or tractor maker must test and requalify a new
supplier before it can switch (B04 moats_present). The buyers are Tata
Motors and Ashok Leyland in trucks, and trailer builders and fabricators,
plus a small export book including Leax Falun AB and an unnamed European
Tier-1 supplier (B03 ar_new_downstream_entities; business-narrative.md).
They buy on running purchase orders with no long-term contracts, and the
top five customers took 59.47% of Q1 FY27 revenue (business-narrative.md
anchors). Present demand follows the truck cycle: Tata Motors and Ashok
Leyland production volumes and SIAM monthly M&HCV, tipper and
tractor-trailer dispatch data are the first signals to track, alongside
TMA tractor sales and the domestic steel price index for the cost side
(B09 downstream_candidates). The peers do not agree on that cycle:
Ramkrishna Forgings and Happy Forgings see truck demand firming, while
Automotive Axles guides FY27 heavy-truck volumes down 5-10% (B06
industry_cross_read). Growth from here rests on four drivers the company
names: more trailer-axle share from the new axle beam extrusion line,
tractor parts rising toward 15% of sales, exports rising toward 8%, and a
replacement wave from the Delhi NCR Parivartan scheme and the BS4 truck
phase-out due 30-Oct-2026 (B05 triggers; B09 downstream_candidates). Each
driver has an outside check: Ramkrishna Forgings' own trailer-axle
disclosures, a Reg 30 filing on any Leax Falun AB order, TMA data, and the
Delhi transport notices (B09 downstream_candidates). The trailer-axle and
suspension line is the only line with a moat: its own design, India's
first single-piece axle-beam-extrusion process, and in-house forging,
casting and heat treatment put it among a handful of integrated makers
(B04 moats_present). The emerging-moat scan scores that one engine, rare
manufacturing capability plus backward integration, at MODEST, and finds
almost nothing else forming (B07 em_score, em_classification). The CV
component line is built to other people's drawings in a crowded field,
and its only protection is the cost of requalifying a supplier (B04). The
tractor and export lines have long relationships but no moat, and pricing
power across the company is weak because steel costs pass through to
customers with a lag (B04 pricing_power; B06 industry_cross_read).

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. VERTICALS FRAMED

**Vertical 1 — EBITDA margin trajectory.** Corpus establishes: FY24-FY26
delivered margin ~13% (B01, B04), Q4 FY26 hit the guided 14.9% (B05
promise_delivery), Q1 FY27 fell to 12.23% (B05 FLAG-MARGIN-MISS), and
Automotive Axles' own margin rose 12.4% to 13.6% in the same quarter under
the same steel/LPG inputs (B12b finding, missed by B06). Corpus cannot
establish: a per-unit cost or margin figure for extruded versus purchased
axle beams (B04 unit_economics NOT FOUND); whether the Q1 miss is a
one-quarter settlement lag or a repeating pattern. Questions that decide
it: (1) does Q2/Q3 FY27 margin cross 14%? (2) does the "other expenses"
creep (26.5-28% of sales vs a promised revert to 22-23%, B12b finding 3)
resolve or persist? (3) does the peer margin divergence (Kross down,
Automotive Axles up) repeat next quarter?

**Vertical 2 — Axle beam extrusion utilisation.** Corpus establishes:
7,500 units/month installed capacity (B05 guidance), commercial production
from Jul-2026 (B05 timeline_slippages), current output ~3,500-4,000
axles/month against a 5,000-axle order book not met (B12b finding).
Corpus cannot establish: the utilisation threshold at which margin
actually moves, beyond management's unquantified claim of "significantly
above 50%" (B04 unit_economics key_lever); the reconciled capacity-
addition percentage (50% vs 60% conflict, B07 input_gaps). Questions:
(1) what is disclosed or inferable utilisation at Q2/Q3 FY27? (2) is a
margin uplift visible at higher utilisation? (3) is the capacity-addition
percentage conflict (Reg 30 vs AR) reconciled?

**Vertical 3 — Seamless tube commissioning.** Corpus establishes: Rs167
Cr capex, 1,20,000-tonne capacity, "around Q4 FY27" target (AR PDF p.30
printed p.58; B05 guidance), a walk-back from "construction completed"
(Q3 FY26) to "almost complete" (Q4 FY26) with no reconciliation (B05
timeline_slippages; B12b finding). Corpus cannot establish: the funding
plan for the remaining spend given weak FCF (B04 mgmt_questions); any
named customer for the oil-and-gas surplus-capacity optionality (B07
optionality_register). Questions: (1) any further slip beyond Q4 FY27?
(2) how is the balance financed? (3) is there a named order for the
oil-and-gas optionality?

**Vertical 4 — Cash conversion / working-capital days.** Corpus
establishes: CFO/PAT 0.180x (FY25), 0.503x (FY26); WC days 89.01 to
131.73 (FY22-FY26); receivables ageing deteriorating; bills discounted
with recourse Rs349.00 Mn (B01, B02, B03). Corpus cannot establish: a
STRUCTURAL vs GROWTH-INDUCED determination — B13 verdict marks it
INDETERMINATE; the India Ratings rationale's own working-capital
paragraphs are held (inputs/rating/2026-06-02_credit_rating_reg30.pdf, pp
2-9) but no stage extracted them (gate-recommendation.md). Questions:
(1) does H1 FY27 receivables growth outrun revenue growth? (2) what does
the receivables ageing split by customer class show? (3) what does the
rating agency's own working-capital paragraph say?

### 4b. CANDIDATE SIGNAL TABLE (from B09, expanded)

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| Tata Motors / Ashok Leyland M&HCV production and dispatch volumes | Production pace decouples from Kross's own trailer/CV segment growth for 2+ quarters | Monthly | SIAM monthly wholesale dispatch data / company investor releases (B09) |
| SIAM CV segment (M&HCV, tractor-trailer, tipper) wholesale volume data | Kross's claimed segment growth diverges from the independent industry print for 2+ quarters | Monthly | SIAM monthly release (B09) |
| Domestic steel (HRC/alloy) price index | A steel spike with no matching margin recovery in the following quarter breaks the "one-quarter lag" excuse | Monthly | Ministry of Steel / SteelMint / CRISIL commodity tracker (B09) |
| TMA domestic tractor sales data | Tractor segment % stalls below 10% for 3+ quarters despite rising TMA volumes | Monthly | Tractor Manufacturers Association monthly release (B09) |
| Ramkrishna Forgings trailer-axle segment disclosure (Rs120cr to Rs250cr, 4-5% to 10% share) | RKFORGE's implied market size keeps Kross's trailer share nearer 10-12% than the claimed 26-28% for 2+ quarters | Quarterly | RKFORGE quarterly concall transcripts and investor presentations (B09; B06) |
| Leax Falun AB / second European Tier-1 export order confirmation | No Reg 30 filing or order confirmation within 12 months of the claim | Event-driven | Company Reg 30 exchange filing / investor presentation (B09) |
| Delhi NCR Parivartan scheme / BS4 CV phase-out implementation (30-Oct-2026) | Notification delayed or scheme scope narrowed below the replacement-demand story cited | Event-driven | Delhi Transport Department / MoRTH notification (B09) |

### 4c. FRAGILITY READ

- **variable_count:** 8 — the seven B05 bull-case triggers (M&HCV cyclical
  recovery, axle beam extrusion ramp/margin, FY27 margin recovery, export
  ramp, seamless tube commissioning, tipping jack ramp, tractor mix
  expansion) plus cash conversion resolving favourably (B05 triggers;
  gate-recommendation.md FLAG-CASH).
- **verifiability_ratio:** 3 of 8 externally observable outside company
  disclosure (M&HCV/OEM volumes via SIAM, RKFORGE's own peer disclosure on
  trailer-axle share, the Delhi Parivartan/BS4 notification); the other 5
  (margin recovery, extrusion utilisation, seamless-tube progress, export
  order status, tipping-jack volume, cash conversion) rest on company
  disclosure alone, since the corpus names no independent verifier for
  any of them.
- **single_point_failure:** EBITDA margin failing to recover toward 14%
  even after both backward-integration plants run above 50% utilisation is
  close to a single point of failure for the TRANSITION thesis specifically
  (B03; B04; B05 FLAG-MARGIN-MISS) — though not for the underlying
  component-supply business, which could continue on volume growth alone
  at the FROM-state margin. Cash conversion turning STRUCTURAL is a
  second, largely independent way the thesis could break; failure does
  not strictly require conjunction of every variable, but the two
  candidate single points (margin, cash) are themselves independent.
- **fragility_verdict:** FRAGILE. Eight variables, five of eight
  verifiable only through company disclosure, a credibility grade of C
  (B05 credibility_grade; B12b concurs lower at C-) with a documented
  pattern of guidance dilution (export target cut three consecutive calls
  without acknowledgment, B05 FLAG-GUIDANCE-DILUTION) and missed product
  targets (Tipping Jack, B05 FLAG-NEW-PRODUCT-MISS).

### 4d. RESEARCH BRIEF (claude.ai work order)

1. Extract the India Ratings 01-Jun-2026 rationale's working-capital and
   liquidity paragraphs verbatim (held: inputs/rating/2026-06-02_credit_
   rating_reg30.pdf, pp 2-9) — feeds the cash-conversion determination.
2. Ask management (or seek disclosure) for receivables ageing split by
   customer class (fabricator vs OEM vs export) — not in AR Note 11.
3. Verify the identity and relationship of three of four Aug-2026
   preferential-issue non-promoter allottees (Dhruv Agarwal, Saroj V
   Rathore, Richa Gauravrajsingh Rathore) beyond Rathore Gauravrajsingh
   Vijaysingh (B08 input_gaps).
4. Track the postal ballot result and allotment outcome, due on or before
   03-Oct-2026 (B00 pending_events).
5. Confirm SIAM monthly M&HCV/tipper/tractor-trailer wholesale volumes
   against Kross's claimed 34% YoY Q1 FY27 trailer-segment growth (B06
   FLAG-TRAILER-GROWTH-DRIVER-DISPUTED).
6. Confirm any Reg 30 filing or public order value for the Leax Falun AB
   or unnamed European Tier-1 relationship (B09 downstream_candidates).
7. Check the Delhi NCR Parivartan scheme / BS4 CV phase-out (30-Oct-2026)
   implementation status against the replacement-demand narrative (B09).
8. Retrieve RKFORGE's next quarterly trailer-axle segment disclosure
   (Rs120cr toward Rs250cr, 4-5% toward 10% share) and re-test Kross's
   claimed 26-28% share against it (B06 analyst_note; B12b finding).
9. PENDING LIVE VERIFICATION (from Chain 2 below): search for any named
   trailer-fabricator customer of Kross, or public commentary on
   fabricator-segment payment terms in the CV component supply chain; the
   corpus names no specific fabricator, only "fabricators" as a class.
10. Verify pre-Mar-2026 promoter and institutional shareholding trend
    (the COMPANY MEMORY claim of DII 9.72% at Mar-2025 cannot be confirmed
    from the two shareholding filings held in this corpus, B08 input_gaps).

### 4e. SECOND-ORDER STUB (Master Prompt v3.7, Rule F)

Stub carries the first TWO chains, drafted from corpus, for Claude web to
extend to the Rule F floor of five with live-web links.

```
CHAIN 1: Axle beam extrusion commissioned into commercial production
Jul-2026 at 7,500 units/month installed capacity, against actual output
of about 3,500-4,000 axles/month and management's own unquantified claim
that margin improves "significantly above 50% utilisation" (B04
unit_economics key_lever; B05 timeline_slippages; B12b finding on axle
output).
Link 1 [DOCUMENTED]: Self-manufactured axle beam extrusion replaces a
purchased-steel-shape cost line with an in-house conversion cost (B04
moats_present, "cost advantage: backward integration"; AR PDF p.13
printed p.20-21).
Link 2 [DOCUMENTED]: One quarter after commercial production began,
EBITDA margin fell to 12.23%, below both the FY26 delivered level
(13.08-13.10%) and the reaffirmed 14-15% guide (B05 FLAG-MARGIN-MISS).
Link 3 [INFERENCE]: If utilisation is running near 47-53% of the
7,500/month line (3,500-4,000 actual, B12b) and margin has not moved,
either the claimed spread benefit needs a higher utilisation threshold
than management has stated, or the saving is being offset by the
"other expenses" creep an independent verifier found and the pipeline
missed (other expenses 26.5-28% of sales vs a promised revert to
22-23%, B12b finding 3) plus the FY27 finance-cost step-up on a full
year of FY26's progressively-drawn borrowing (B02 rank 12). The engine
may be running without yet showing in the P&L because a different cost
line is absorbing the gain.
Binding constraint: whether the per-unit steel/conversion-cost saving
from self-manufactured axle beams, at current volumes, is large enough
to outrun the other-expense creep and the finance-cost step-up.
Unsaid: no transcript or filing in the corpus discloses a per-unit cost
or margin figure for extruded versus purchased axle beams (B04
unit_economics NOT FOUND); the "above 50% utilisation" threshold itself
is asserted by management, never evidenced with a number.
Observation that confirms or breaks this chain, and confirm-by date:
Q2 FY27 results (quarter ended 30-Sep-2026, due by mid-Nov-2026 under the
45-day SEBI window) showing EBITDA margin at or above 14% alongside a
disclosed or inferable extrusion utilisation figure above 50%. If margin
stays sub-13% while utilisation is reported above 50%, the chain breaks
and the margin claim itself, not the utilisation ramp, is the failure
point.
```

```
CHAIN 2: Trade receivables >6-month aged bucket rose from 8.9% to 11.0%
of gross while the ECL allowance held flat at Rs14.35 Mn for two years,
and receivables turnover fell from 7.67x (FY24) to 3.55x (FY26) (B02
rank 1, 4; Note 11 AR PDF p.69 printed p.132-133; Note 52 AR PDF p.82-83
printed p.159-160).
Link 1 [DOCUMENTED]: Bills discounted with recourse rose 7.6% YoY to
Rs349.00 Mn, 88% of total contingent liabilities, sitting off the
receivables line while credit risk is retained (B02 rank 2; Note 34, AR
PDF p.76-77 printed p.146-147).
Link 2 [DOCUMENTED]: Customers individually holding more than 5% of the
receivables balance account for 54.19% of the FY26 gross balance, down
from 66.06% in FY25 (Note 39(a), AR PDF p.79 printed p.153) — the
deterioration concentrates among a small number of named-scale
counterparties, not a diffuse retail book.
Link 3 [INFERENCE]: A mix shift toward slower-paying trailer fabricators
(rather than the large OEMs) is plausible, given the company's own Note
52 remark tying rising working capital to revenue growth, and
management's own concall admission of "fabricator receivables above 90
days" and constrained operating cash flow in H1 FY26 (B12b missed item 2,
Concall_Nov_2025 p.10-11) — a fact the concall stage itself failed to
absorb. The corpus does not name which customer class is actually
slipping.
Binding constraint: whether the answer to "who pays, and why now" is a
mix shift toward slower-paying trailer fabricators (growth-induced,
would reverse as OEM share rises) or a genuine payment-behaviour
deterioration inside the existing customer base (structural).
Unsaid: no stage or filing discloses receivables ageing split by
customer class (fabricator vs OEM vs export) — the one fact that would
resolve this chain is not in the corpus (B08 gap; gate-recommendation.md
missing-evidence item 2). PENDING LIVE VERIFICATION: no specific
trailer-fabricator counterparty is named anywhere in the corpus; Claude
web should search for any named fabricator customer or public commentary
on fabricator-segment payment terms in the Indian CV component supply
chain, and separately open the India Ratings rationale (held, pp 2-9)
for the agency's own working-capital read, not yet extracted by any
stage.
Observation that confirms or breaks this chain, and confirm-by date: the
H1 FY27 (half year to 30-Sep-2026) balance sheet and cash flow, filed
with Q2 FY27 results (due by mid-Nov-2026): receivables growth against
revenue growth, and any ageing-by-customer-class disclosure, would
confirm or break the growth-induced reading.
```

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in
claude.ai with live web, before Role 2.

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. Kross makes forged, cast and machined steel parts for trucks, trailers
   and tractors, plus complete trailer axle and suspension assemblies of
   its own design (B04).
2. It is a Jamshedpur family business, run by the Rai family, who own
   68.57% of the shares and have pledged none of them (B08).
3. It listed in September 2024 through a Rs 500 Cr IPO, of which Rs 250
   Cr was fresh money for capex, debt repayment and working capital (B00).
4. The buyers are truck and tractor makers, chiefly Tata Motors and Ashok
   Leyland, plus trailer fabricators and a small export book (B03; B04).
5. They buy on purchase orders with no long-term contracts, and the top
   five customers took 59.47% of Q1 FY27 revenue (business-narrative.md
   anchors).
6. Demand follows the truck production cycle, and the three peer
   companies disagree on where that cycle stands right now (B06).
7. Growth is meant to come from four places: more trailer-axle share,
   a bigger tractor-parts mix, more exports, and a coming truck
   replacement scheme in Delhi (B05 triggers).
8. Each of those four growth claims has weakened at least once on a
   concall without the company naming the change as a cut (B05
   FLAG-GUIDANCE-DILUTION; B05 FLAG-NEW-PRODUCT-MISS).
9. The only real moat sits in the trailer-axle and suspension line: its
   own design and in-house forging, casting and extrusion. Everything
   else is built to another company's drawing, protected only by the cost
   of requalifying a new supplier (B04).
10. The company is trying to make its own steel shapes instead of buying
    them, to lift margin from about 13% toward 14-15%. That claim is not
    yet visible in the numbers (B04; B05).
11. Cash generation is the weakest part of the record: profit has grown,
    but the cash backing that profit has not kept pace, and the gap
    between the two has widened for three years running (B01; B02; B03).
12. Two readings explain that cash gap. One says it is capex and a
    growing trailer-fabricator book. The other says some customers are
    paying slower for reasons that will not reverse (gate-recommendation.md).
13. The corpus could not establish which of those two readings is right;
    the rating agency's own view on working capital is held in the corpus
    but no stage has yet pulled the exact paragraph out (B13; gate-
    recommendation.md).
14. The biggest open question is whether the margin gain from the new
    plants shows up once both are running near full capacity, or whether
    an unrelated rise in other costs and finance charges eats the gain
    before it reaches the profit line (Section 4e Chain 1).
15. The second open question is who, exactly, is paying slower: a
    specific class of customer (fabricators) the corpus cannot name, or a
    broader shift the company has not disclosed (Section 4e Chain 2).

## SECTION 6: STANDING EXTRACTION ANNEX

**1. UNITS.** No per-unit realisation (ASP), revenue-per-tonne, or
revenue-per-axle figure is printed anywhere in the corpus for any line.
The company discloses volumes for individual products in units-per-month
(e.g., "installed capacity of 7,500 axle beams per month," Concall_Feb_2026,
per B05 guidance) and revenue mix as a percentage of total revenue (AR PDF
p.23, printed p.40-41: "Trailer Axle and Suspension... 42.61%... Commercial
Vehicle Components... 42.97%... Tractor Components... 9.48%... Exports...
3.60%... Others... 1.38%"), but never combines a rupee revenue figure with
a matching unit count for any single product to derive an ASP. This is a
basket, not a single-product line, so no per-unit figure can be derived
without an unpublished unit-count breakdown by revenue stream.
Comment: revenue-per-unit and margin-per-unit are both NOT FOUND (B04
unit_economics), confirmed by direct search of the AR text for a matching
volume-and-rupee pair; the closest available proxy is the segment
percentage-of-revenue mix above.

**2. SEGMENT CAPITAL AND DEBT.** "The Company is engaged in manufacturing
of critical components for commercial vehicles and Tractors. The
performance of the Company is assessed and reviewed by the Chief
Operating Decision Maker ('CODM') as a single operating segment and
accordingly logistics and allied services is the only operating segment"
(Note 45, AR PDF p.81, printed p.156). Comment: Kross reports one
operating segment under Ind AS 108, so no segment-wise assets,
liabilities, capital employed, or borrowings allocation exists. Total
company borrowings (unallocated by definition): Rs 523.65 Mn (Rs 52.37
Cr) at FY26-end per the AR (Note 16, AR PDF p.72-73 printed p.138-139),
against Rs 53.73 Cr in the screener extract, a difference of Rs 1.36 Cr
traced by Verifier A to lease liabilities included in the screener figure
(B12a finding; gate-recommendation.md Verifier A section).

**3. GUIDANCE VERSUS ASPIRATION.**

| Claim | Classification | Quote / figure | Source |
|---|---|---|---|
| FY27 revenue growth ~22%, EBITDA margin 14-15% | (a) guidance with period (FY2026-27) | "~22%" / "14-15%" | Concall_May_2026 (Q4 FY26 call), per B05 guidance |
| Export share "double-digit" | (b) aspiration without a fixed period, later dated then diluted | first "by FY27", then "by FY28" (same-call internal contradiction), then "8% in the next two years" | Concall_Nov_2025, Concall_Feb_2026 (opening vs Q&A), Concall_Jul_2026, per B05 guidance/FLAG-GUIDANCE-DILUTION |
| Tractor segment revenue contribution ~15% | (b) aspiration with a stated period ("next two years") | "~15%... next two years" | Concall_Nov_2025, per B03 guidance_table |
| Tipping Jack FY26 volume 600 units by March | (a) guidance with period, missed | "600 units... by Mar-2026" | Concall_Nov_2025, per B05 guidance; outcome "Missed" (75-80 kits actual) per B05 promise_delivery |
| Tipping Jack FY27 revenue Rs 45-50 Cr | (a) guidance with period, unresolved/orphaned | "₹45-50 crore... FY27" | Concall_Feb_2026, per B05 guidance; B12b notes it was never restated after Q3 FY26 and is unreachable on the Q1 FY27 run-rate |
| Seamless tube commissioning "around Q4 FY27" | (c) capacity/capability with a stated but softening date | "around Q4 of FY27" | Concall_May_2026, reaffirmed Concall_Jul_2026, per B05 guidance |
| Robotic forging facility operational | (c) capability milestone with a near-term date | "September 2026" | AR Strategic Priorities, AR PDF p.20 printed p.35, per B03 guidance_table |
| Extruded axle market share target 35% (from 26-28%) | (b) aspiration, no fixed period | "35% (from 26-28%)" | Concall_Feb_2026, per B05 guidance, "not dated" |

**4. CONCENTRATION.** Product: revenue mix 42.61% / 42.97% / 9.48% / 3.60%
/ 1.38% across trailer axle & suspension, CV components, tractor
components, exports and others (AR PDF p.23, printed p.40-41, per B04).
Customer: "top five customers 59.47% of Q1 FY27 revenue" (Q1 FY27
investor presentation, slide 20, per business-narrative.md anchors); no
single largest customer's individual percentage is disclosed anywhere in
the corpus — NOT DISCLOSED, reason: the AR and decks report only the
aggregate top-5 figure and name Tata Motors/Ashok Leyland as the largest
relationships without an individual percentage. A second, receivables-
side concentration cut exists: "customers individually representing more
than 5% of the total trade receivables balance... accounted for
approximately 54.19% as at March 31, 2026, 66.06% as at March 31, 2025"
(Note 39(a), AR PDF p.79, printed p.153). Geography: exports 3.55-3.60% of
FY26 revenue (Board's Report vs revenue-mix pie disagree at the second
decimal, AR PDF p.27 printed p.49 vs AR PDF p.23 printed p.40-41, per B04
FLAG-DISCLOSURE), rising to 4.51% in Q1 FY27; the remaining 96%+ is
domestic (B09 market_definition).

**5. PROMISE LEDGER.**

| Promised in | Promise | Outcome | Evidence anchor |
|---|---|---|---|
| Q2 FY26 | Extrusion plant commercial production by end Q3 FY26 | Partial | Concall_Nov_2025; commissioned Q4 FY26, selling from May-2026 (B05) |
| Q2 FY26 | Tipping Jack 600 units FY26 (by March) | Missed | Concall_Nov_2025; 75-80 kits actual (B05) |
| Q3 FY26 | Tipping Jack 300 units in Q4 FY26 | Missed | Concall_Feb_2026; 75-80 kits actual (B05) |
| Q2/Q3 FY26 | Export "double-digit" share by FY27 | Missed | Concall_Nov_2025/Feb_2026; diluted to 8% in two years by Q1 FY27, no acknowledgment (B05) |
| Q3 FY26 | Q4 FY26 EBITDA margin ~14-15% | Delivered | Concall_Feb_2026; 14.9% actual (B05) |
| Q4 FY26 | FY27 quarterly EBITDA margin 14-15% | Missed | Concall_May_2026; 12.23% actual Q1 FY27 (B05) |
| Q4 FY26 | FY27 revenue growth ~22% | Delivered (exceeded) | Concall_May_2026; 32% actual Q1 FY27 (B05) |
| Q2 FY26 | IPO proceeds 84% deployed, balance 16% within FY26 | Delivered | Concall_Nov_2025; 90% by Q3 FY26, 100% by Q4 FY26 (B05); confirmed nil-deviation, Note 54, AR PDF p.84 printed p.163 |
| Q3 FY26 | Seamless tube construction completed | Partial | Concall_Feb_2026; walked back to "almost complete" Q4 FY26, no reconciliation (B05) |
| Q2 FY26 | Trailer axle market share rising 26-28% toward 35% | Partial | Concall_Nov_2025; management stopped commenting by Q1 FY27 (B05) |

**6. RESTATED BASES.** "Previous year figures have been regrouped/
rearranged/reclassified wherever necessary. Further, there are no
material regrouping/reclassifications during the year" (Note 62:
Reclassification, AR PDF p.84, printed p.163). Comment: no restatement of
FY26 comparatives against a reorganisation, transfer, or reclassification
is disclosed; B02's independent reading concurs (`restatements_found: []`).
The prospectus (Sep-2024) separately carries restated FY22-FY24 figures
for IPO purposes, a different kind of restatement (offer-document
standardisation, not an in-year reclassification) and outside this
question's scope.

**7. CORPORATE-ACTION CLAUSES.** No scheme, demerger, merger, or buyback
appears anywhere in the corpus (confirmed by B00's SEBI-order freshness
pair check and B03/B08's independent searches). The one corporate action
in the corpus is the 31-Aug-2026 preferential issue plus convertible
warrants. Equity shares: "Issue of up to 15,00,000 (Fifteen Lakh) Equity
Shares at an issue price of ₹212/- per equity share... aggregating to
₹31,80,00,000/-" to "Up to 4" named investors per Annexure A (Reg 30
letter, 31-Aug-2026, Annexure I). Warrants: "Issue of up to 15,00,000
(Fifteen Lakhs) Convertible Warrants at an issue price of Rs 212/- per
warrant, each convertible into (01) Equity Share of face value of ₹05/-
each... on a preferential basis" to "Up to 2" named investors per
Annexure B (same filing, Annexure II); conversion ratio 1:1; "An amount
equivalent to at least 25% of the warrant issue price shall be payable
upfront... and the balance 75%... on the exercise of option of
conversion"; exercise window "within a maximum period of 18 months from
the date of allotment"; on lapse, "entitlement of conversion will be
lapsed, and the upfront consideration paid by the warrant holder shall be
forfeited." Approval/record dates: Board approval and Postal Ballot
Notice both dated 31-Aug-2026; remote e-voting 01-Sep-2026 09:00 to
30-Sep-2026 17:00; a corrigendum to the notice was issued 23-Sep-2026
correcting the post-issue shareholding table and allottee promoter/
non-promoter status column (B08 adverse_findings). Outcome/allotment:
NOT FOUND — due on or before 03-Oct-2026, after this run's date (B00
pending_events).

**8. RELATED-PARTY PERIMETER.** Full list per Note 51(a), Related Party
Disclosures (AR PDF p.81, printed p.157): control-related entities —
Tuff Seals Private Limited ("Enterprises over which Key Management
Personnel and their relatives are able to exercise significant
influence"), Bull Auto Parts ("Firm where director is a proprietor" —
Kunal Rai, CFO), Dipak Rai (HUF) ("Hindu undivided Family of Director" —
Sudhir Rai, Karta); KMP — Sudhir Rai (CMD), Anita Rai (WTD), Sumeet Rai
(WTD), Kunal Rai (WTD Finance & CFO), K Suresh Babu (ceased Oct-2023),
Rahul Rungta (ceased May-2023), Sangita Kumari Agarwal (ceased Nov-2023),
Debolina Karmakar (CS), and independent directors Sanjiv Paul, Gurvinder
Singh Ahuja, Mukesh Kumar Agarwal, Deepa Verma. Transactions, latest year
(Note 51(b), AR PDF p.82, printed p.158, INR Mn): Tuff Seals Private
Limited, purchase of goods, Rs 1.01 Mn FY26 (Rs 2.84 Mn FY25); Bull Auto
Parts, sale of goods, Rs 93.54 Mn FY26 outstanding Rs 49.38 Mn (Rs 121.01
Mn FY25 outstanding Rs 70.21 Mn); Sudhir Rai, remuneration Rs 3.60 Mn plus
an unsecured loan outstanding Rs 12.53 Mn (both years); Anita Rai,
remuneration Rs 2.40 Mn, unsecured loan outstanding Rs 3.42 Mn; Sumeet
Rai, remuneration Rs 2.40 Mn, unsecured loan outstanding Rs 0.86 Mn; Kunal
Rai, remuneration Rs 2.40 Mn, unsecured loan outstanding Rs 0.79 Mn;
Debolina Karmakar, salary Rs 1.11 Mn (Rs 0.73 Mn FY25); four independent
directors, sitting fees Rs 0.18 Mn each FY26. No arm's-length pricing
comparison is disclosed for the Bull Auto Parts sales (B02 rank 3;
questions_for_mgmt).

**9. PLEDGE AND SHAREHOLDING.** Only two shareholding-pattern filings are
held in this corpus — 31-Mar-2026 and 30-Jun-2026 — not the twelve
quarters the question asks for; the remaining historical quarters back to
listing come from a secondary compiled file (NSE_shareholding_master_
KROSS.json), not primary XBRL filings (B08). From the two primary
filings: promoter and promoter-group holding 68.52% (31-Mar-2026) to
68.57% (30-Jun-2026); pledge: `WhetherAnySharesHeldByPromotersAreEncumberedUnderPledged`
= false at both dates (SHP_30-JUN-2026_KROSS_NSE_xbrl.txt). From the
compiled master series (B08 transition_evidence, not independently
re-verified against primary filings for quarters other than the two
above): promoter holding rose every disclosed quarter since listing,
67.70% (30-Sep-2024) to 68.57% (30-Jun-2026), no quarter showing a
decline. Institutional holding, latest (30-Jun-2026, from the primary
XBRL): DII (Institutions Domestic) 6.05%, FII (Institutions Foreign, FPI
Cat I+II) 2.51% (up from 6.03%/2.62% at 31-Mar-2026) — roughly flat, not
falling (B08, correcting a COMPANY MEMORY claim of DII 9.72% at Mar-2025
that cannot be verified because that filing is not held in this corpus).

**10. VERIFICATION.** Documents quoted in this annex, with filename and
date: Annual_Report_2026.pdf (FY2025-26, board-approved 12-May-2026,
signed 24-Jul-2026) — Notes 11, 16, 34, 39(a), 45, 51, 52, 54, 62, AR
Board's Report and Strategic Priorities sections; SHP_30-JUN-2026_KROSS_
NSE_xbrl.xml / .txt (shareholding pattern as at 30-Jun-2026); NSE_
shareholding_master_KROSS.json (compiled historical series, secondary);
inputs/announcements/20260831-5dfd2e9c-cf64-49a4-a5c3-b16f91e0c2b0.txt
(Reg 30 outcome of Board Meeting, 31-Aug-2026, preferential issue and
warrants, Annexures I and II); B05/B02/B03/B04/B08 stage blocks and
gate-recommendation.md for cross-referenced figures not directly
re-read from a PDF in this pass.

CORPUS COMMIT HASH: 0f7744a4e776690d7bb53fba71b5630d9c9316e2
