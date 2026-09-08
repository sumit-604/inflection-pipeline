# HALT 1 UNDERSTANDING DOSSIER — FRATELLI VINEYARDS LTD (FRATELLI)
Run: fratelli-2026-09-07 | Phase 1 close out | Corpus commit 7ff6592de8194c907b07449e3dc4201ece4df070

This dossier assembles what stages 0 through 9 and the four verifiers found. It
values nothing and recommends nothing. Section 2's Mental Model Declaration is
a DRAFT for the operator to sign or reject in claude.ai after live-web
stress-testing. Nothing here marks it signed.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

**1. Concalls.** Five Fratelli transcripts held, oldest first: Q4 FY25
(Concall_Q4FY25_Jun2025_Transcript.pdf, call 30-May-2025), Q1 FY26
(Concall_Q1FY26_Aug2025_Transcript.pdf, 13-Aug-2025), Q2 FY26
(Concall_Q2FY26_Nov2025_Transcript.pdf, 18-Nov-2025), Q3 FY26
(Concall_Q3FY26_Feb2026_Transcript.pdf, 16-Feb-2026), Q4 FY26
(Concall_Q4FY26_Jun2026_Transcript.pdf, 2-Jun-2026) (B00 concall_quarter_map;
B05). The most recent quarter covered is Q4 FY26 (year ended 31-Mar-2026).
Given the run date of 07-Sep-2026, a more recent quarter has plausibly
reported and its transcript is plausibly missing: Q1 FY27 results (quarter
ended 30-Jun-2026) were filed 11-Aug-2026 and the matching call was held
14-Aug-2026, but no transcript has been published (B00, B05 input_gaps).

**2. Annual reports.** Two years held: Annual_Report_FY2025.pdf and
Annual_Report_FY2026.pdf (B00 inventory). The latest completed FY (FY26,
year ended 31-Mar-2026, board-adopted 30-May-2026) is present. At least 3
years are NOT held; FY2022 and FY2023 are absent from every source in the
corpus, screener included (B00 input_gaps; B01 input_gaps; B03 input_gaps).

**3. Results filings.** Six filings held: Q4FY25/FY25 (28-May-2025), Q1FY26
(11-Aug-2025), Q2FY26 (14-Nov-2025), Q3FY26 (12-Feb-2026), Q4FY26/FY26
(30-May-2026), Q1FY27 (11-Aug-2026) (B00 analyst_note). The latest is Q1FY27,
filed 11-Aug-2026. No quarter-gap exists between the latest results filing
and the latest AR: the FY26 AR is the audited annual results for the year the
last full-year filing covers, and Q1FY27 is the one quarter filed since.

**4. Investor presentations.** Six held, one per quarter Q4FY25 through
Q1FY27; the latest is Investor_Presentation_Q1FY27_Aug2026.pdf (B00
inventory: presentation 6).

**5. Research / rating.** None held. inputs/rating/ and inputs/research/ are
both empty. No credit rating covers the wine entity; the newest rating
identified anywhere in this run's evidence is an Infomerics rating dated
26-Sep-2023 issued to Tinna Trade before the wine pivot, and it is not in the
corpus (B00 input_gaps; B01 input_gaps).

**6. Corporate actions.** Fifteen announcement filings held, dated
30-May-2025 through 07-Sep-2026: preferential allotments (28-Oct-2025,
12-Nov-2025), a director resignation (14-Nov-2025), warrant lapse
(28-Feb-2026), voluntary delisting from the Calcutta Stock Exchange
(27-Feb-2026), change in management and company-secretary filings
(03-Apr-2026), the two inter-se promoter gift-transfer intimations
(14-Aug-2026, 21-Aug-2026) and the matching SAST Regulation 29(3) intimation
(21-Aug-2026), a postal ballot notice (22-Aug-2026), and an AGM/shareholder
letter (07-Sep-2026) (B00 inventory; work/text/announcements listing).

**7. Freshness pair check.** One of the four pairs FAILED. RESULTS to
CONCALL: trigger document Results_Q1FY27_2026-08-11.pdf is held; the mate,
the Q1FY27 concall transcript (call held 14-Aug-2026), is absent (B00
freshness_pairs). The other three pairs PASS: no rating bulletin exists to
trigger the RATING to RATIONALE pair; no SEBI order is referenced anywhere in
the corpus to trigger the SEBI ORDER pair; and AR to LATEST AUDITED ANNUAL
RESULTS passes, since the FY2026 AR is present and matches the audited FY26
results filing (B00 freshness_pairs).

**8. VERDICT LINE: CORPUS GAPPED-FRESHNESS.**

The Q1FY27 results and investor deck are present; the matching Q1FY27
concall transcript, for the call held 14-Aug-2026, was never published as of
the 07-Sep-2026 run date (B00 freshness_pairs, FAIL). This verdict takes
precedence and carries the downstream consequence that the phase-1 gate
recommendation caps at PROCEED WITH CAVEATS on freshness alone (B00 flags,
FLAG-CORPUS-FRESHNESS).

Other gaps, listed under this verdict:

- No prospectus. Structural, not collectable: the wine business listed
  through the Tinna Trade shell; there was no IPO (B00 input_gaps).
- No credit rating covering the wine entity. Findable-but-missing only in
  the sense that a future rating could appear on a rating agency site; none
  exists today for Fratelli Wines Pvt Ltd or Fratelli Vineyards Ltd (B00, B01
  input_gaps).
- No shareholding-pattern file. The two ARs' Corporate Governance Report
  distribution tables and the SAST filings substitute; expected source is the
  BSE shareholding-pattern endpoint, findable-but-missing (B00 input_gaps).
- No broker research. Plausibly nonexistent for a micro-cap this size;
  findable at BSE/company IR if one is ever published (B00 input_gaps).
- FY2022 and FY2023 absent from every source, screener included. Genuine
  data gap, findable-missing from BSE historical filings (B00, B01, B03
  input_gaps).

### Analysis defects the operator should read this dossier against

This run's gate recommendation is **REWORK, on a confidence delta of 31
against a 60 floor** (confidence.yaml revision 2). That verdict judges the
ANALYSIS this pipeline produced, not the company. Nothing in this dossier is
a buy, sell, hold or watch call.

Stage 5 (concall analysis) and stage 6 (peer cross-read) were each rerun once
under the first REWORK verdict. Verifiers B and D re-measured the reran
output independently, without being shown the first audit's findings, so
both re-measures stand on their own. Neither rerun stage cleared the gate on
the second pass. The operator then ruled there would be no third rerun and
directed the run be closed with the defects recorded (gate-recommendation.md,
OPERATOR RULING 2026-09-07).

- **Verifier B (red flags) coverage is 31%.** Of 29 flags Verifier B found
  independently in the reran stages 5 and 6, 9 were caught and 10 partially
  caught (B12b). Two findings are CRITICAL. The first is a miss: a
  discounting and trade-promotion contradiction runs across four consecutive
  Sula calls and is compounded by Fratelli contradicting itself between the
  December 2025 and March 2026 quarter calls on the same topic; neither
  reran stage mentions discounting at all, and it bears on whether the 78.1%
  gross margin and the operating-leverage story survive the trade spend
  needed to hold shelf (B12b findings, CRITICAL row 2).
- **Verifier B rules the reran stage 5's headline flag OVERSTATED.** The
  EBITDA-SIGN-FLIP flag applied a consolidated recomputation to figures
  management reported on the wine-subsidiary basis, the very basis mismatch
  stage 5's own UNDISCLOSED-BASIS-CHANGE flag identified elsewhere in the
  same block. On the subsidiary basis the claims largely reconcile (B05
  supersessions; B12b CRITICAL row 1). **This framing is not carried forward
  anywhere else in this dossier.** Credibility grade D still stands, on
  guidance discipline, repeated evasion, undisclosed filed items and
  peer-contradicted claims; Verifier B concurs with the grade on those
  grounds (B05 credibility_basis; B12b credibility_grade_concur).
- **Verifier D (peer cross-read) citation acceptance is 50%, with eight
  MAJOR anchor errors in the reran stage 6**, including one load-bearing
  figure cited to the wrong document entirely (B12d). Peer utilisation is
  67%: one of six mandated peer presentations was never mentioned in the
  rerun, in any category (B12d unused_but_relevant). Stage 6's ARITHMETIC
  verdicts were independently re-derived and HELD; the market-share
  calculation re-derives to 7.81-9.46% against the stage's stated 7.5-9.5%,
  and the EBITDA-benchmark gap to 0.9-15.3 points against the stated 5-15.
  Both are imprecision, not verdict failures — **the substance of the rerun
  stands; the citation layer does not** (B12d arithmetic_verdicts_note).

Every figure and finding used elsewhere in this dossier is drawn only from
what survives this audit: the corrected numbers, the arithmetic verdicts
that HELD, and the credibility grade on the grounds Verifier B concurs with.

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT — PENDING OPERATOR SIGN-OFF.**

### PART A — THE FROM STATE

**A1. Archetype.** Two revenue lines, both starting from the same claimed
archetype with different demonstrated distance from it (B04 revenue_streams;
B04 FLAG-QUALITY-LADDER).

- *Still wine (about 90% of revenue).* Claimed archetype: Brand/franchise
  consumer — volume growth, pricing power, distribution reach, gross margin,
  advertising efficiency (B04: "branded consumer manufacturing, domestic
  retail/HoReCa"). Demonstrated distance from that archetype is large: the
  wine segment itself has posted two consecutive years of loss (Ind AS 108
  result -Rs10.49cr FY25, -Rs10.61cr FY26, against +Rs18.92cr FY24) and Gate
  0 confirmed zero moats (B01 moat_class NONE; B04 must_track_metrics).
- *Shotgun RTD + TiLT wine-in-a-can (about 10% of revenue).* Claimed
  archetype: the same Brand/franchise consumer label the deck language
  implies, but the underlying economics fit no known archetype cleanly.
  Shotgun needs no vineyard; any beverage maker with a canning line and a
  distributor can enter (B04: "no case-level ASP/margin split... light,
  fast-turning, low entry barriers"; B07 em_score 13, MODEST).

**A2. The simple analogy.** Fratelli grows grapes on its own and contracted
land near Akluj and Jambhali in Maharashtra, turns them into wine at a 5.4
million litre winery, and sells more than 50 labels through 31,000 retail
and hospitality touch points, government beverage corporations, and 29
defence canteens (B04 business narrative build; B00). Since February 2025 it
has also filled cans with a ready-to-drink alcoholic product, Shotgun, using
the same winery and the same field sales team (B04, B07). No customer needs
either product; both compete for a discretionary rupee in a category that is
under 1% of India's alcohol market by volume (B09 market_definition; B06
industry_cross_read).

### PART B — THE TRANSITION

**Line: Still wine.**

- **B1. FROM to TO.** FROM: R0/R1 on the CLAUDE.md Quality Ladder —
  non-operating-adjacent to commodity price-taker, given the FY24-FY26
  history downgrade, moat NONE, and negative ROCE/ROE in every comparable
  window (B01 classification AVOID, history_downgrade true; B04
  FLAG-QUALITY-LADDER). TO, as claimed by management: R4/R5, franchise or
  brand/scarcity owner — a claimed one-third domestic market share, an
  85-90% duopoly with Sula, and luxury-tier pricing power (B06 flags
  MARKET-SHARE-ARITHMETIC-CONTRADICTED; B09 flags FLAG-MGMT-SHARE-INFLATED).
  This is a claimed multi-rung leap from an unstable base, itself a red flag
  under the CLAUDE.md ladder rule (B04 FLAG-QUALITY-LADDER).
- **B2. The engine.** Two things: a premiumisation mix shift toward the
  above-Rs2,000 luxury tier (J'NOON +44% YoY, Sette +5% YoY, luxury segment
  +15% YoY in FY26) and 15 years of proprietary grape-clone work, imported
  varietals grafted onto Indian rootstock, that the company calls hard to
  copy in the near-to-medium term (B04 moats_present; B05 1A trigger 4).
- **B3. The proof gate.** The wine-segment Ind AS 108 result (Note 37
  equivalent) turning and staying positive for a full fiscal year, breaking
  the two-year loss streak of -Rs10.49cr (FY25) and -Rs10.61cr (FY26), on
  the recomputed EBITDA method (PBT + finance cost + depreciation) applied
  consistently on one stated, held basis — not switched between subsidiary
  and consolidated mid-argument (B03 monitorables; B04 must_track_metrics;
  B05 triggers priority 2).
- **B4. The recognition gap (open question, resolved at Stage 11).**
  Whether the market has already priced the claimed R4/R5 positioning —
  luxury leadership, a third of the market, the largest distribution network
  — even though the wine segment posted a second consecutive loss in FY26
  and Fratelli's own audited FY26 revenue against its own AR-cited market
  size implies about 7.5-9.5% share (independently re-derived at
  7.81-9.46%), not a third (B06 flags; B09 flags; B12d arithmetic_verdicts_
  note). Stage 11 resolves this through the destination-PE gap; no number or
  conclusion is stated here.
- **B5. The ugliness test.** STRUCTURAL-FEATURE, not artifact-of-climb, on
  the cash and working-capital evidence. Wine-segment revenue was flat to
  declining across FY24-FY26 (Rs212.88cr, Rs178.44cr, Rs181.20cr per Note
  37) while consolidated working-capital days rose from 149 to 349 over the
  same window (B01 block_b_trend; B02 finding 2/receivables_trend). Cash
  absorption on flat-to-declining revenue cannot be growth-induced, which
  leaves the structural reading (B02 findings 3, 4, 8, 9, 15; B03 FLAG-CASH;
  this determination is also recorded in outputs/final/gate-recommendation.md
  FLAG-CASH, built from the same block evidence).
- **B6. The transition falsifier.** A third consecutive negative year for
  the wine-segment Ind AS 108 result (i.e., a negative print in the FY27
  AR's equivalent note) kills the transition thesis regardless of what the
  topline does; it means the second engine did not rescue the first (B03
  monitorables item 2).

**Line: Shotgun RTD + TiLT.**

- **B1. FROM to TO.** FROM: R1, an undifferentiated commodity-style new
  entrant with zero confirmed moat and one year of data (B07 em_score 13,
  MODEST; B04 valuation not_applicable list). TO, as claimed: category
  leadership — management states "more than 90% market share in the
  Wine-in-a-Can segment," a claim never tested against Sula's own competing
  leadership claim on the same question (B12b PARTIAL finding, B06 Q5/B05
  3A).
- **B2. The engine.** Shared manufacturing and distribution infrastructure —
  riding the existing winery, field sales team, and 31,000-touch-point
  network to add outlet count and case volume without a new capital base
  (B04 unit_economics key_lever; B07 active_categories A4, B2).
- **B3. The proof gate.** Case-volume growth sustaining the roughly
  1.5x-2x YoY cadence delivered to date, toward the 200,000-case FY27
  target (double FY26's ~100,000 cases), without the RTD line's lower gross
  margin (65-70% versus wine's 70%+) dragging the blended margin as mix
  rises (B05 triggers priority 1; B04 first_deterioration_signals).
- **B4. The recognition gap (open question, resolved at Stage 11).**
  Whether the market already prices Shotgun's early scale (18 states,
  ~9,000 outlets, ~100,000 cases) as a proven second engine, when the RTD
  market-size, case-count and share figures management has given are
  internally inconsistent within single answers (10% share by cases, 3.6%
  by value, 6% claimed elsewhere) and the category's own claimed 25-30%
  quarter-on-quarter growth is contradicted by the nearest peer disclosing
  slow traction (B12b missed finding; B06 contradicted). No number or
  conclusion is stated here; Stage 11 resolves it.
- **B5. The ugliness test.** ARTIFACT-OF-CLIMB, tentatively. The RTD line is
  one year old; its early metrics (state count, outlet count, case volume)
  have been delivered or exceeded against management's own targets (B05
  promise_delivery rows 13, 14), and B07's forward moat scan finds real,
  documented (not merely claimed) motion in product-platform reuse and CSD
  qualification access. This reading is weaker than the wine line's
  structural call: no independent unit-economics disclosure exists to test
  whether the margin holds as scale rises (B04 unit_economics; B07
  optionality_register).
- **B6. The transition falsifier.** Case growth stalling below roughly 1.5x
  YoY, or RTD's lower gross margin dragging the blended margin as mix
  shifts, would falsify this line's transition independent of what still
  wine does (B05 triggers priority 1 kill_signal).

### PART C — WHAT THE MODEL WATCHES

**C1. Dominant variables**, derived from the engines and proof gates above,
current state one line each:

1. **Recomputed EBITDA, stated on one basis and held there.** Current state:
   Q1 FY27 recomputed at +Rs0.95cr / 2.1% margin is the first genuinely
   positive quarter in the sample; every other checked quarter from Q3 FY26
   onward recomputes negative against management's live-call claims (B05
   red_flags, analyst_note).
2. **Wine-segment Ind AS 108 result (Note 37 equivalent).** Current state:
   two consecutive years of loss, -Rs10.49cr FY25 and -Rs10.61cr FY26,
   against +Rs18.92cr FY24 (B02 finding 2; B04 must_track_metrics).
3. **Shotgun RTD case volume and blended margin as mix shifts.** Current
   state: ~100,000 cases FY26 against a 200,000-case FY27 target; no
   case-level margin disclosed to test the drag as mix rises (B04
   unit_economics; B05 triggers priority 1).
4. **Cash against the Rs114.50cr related-party guarantee, and working-capital
   days.** Current state: consolidated cash Rs7.78 lakh, standalone
   Rs0.88 lakh, against Rs119.74cr of Group borrowings and a guarantee the
   going-concern notes never name; WC days at 349 (B02 findings 3, 4, 15;
   B01 block_b_trend).

**C2. What the model rejects.** Whether the addressable market is big enough.
Stage 9's own sizing shows a GOOD runway class with roughly 10.6x revenue
headroom against the attainable-share ceiling (B09 revenue_headroom_x,
runway_class), so market size is not the binding constraint. The binding
constraint is whether the two claimed engines convert distribution and
brand assets that already exist into segment profit — a conversion question,
not a sizing question. The model also rejects the "duopoly" framing as a
variable worth tracking on its own terms: it is a labelling dispute
(B06 flags ZERO-PEER-RECOGNITION) that does not change what either engine
needs to prove.

**C3. The business falsifier**, distinct from either line's transition
falsifier. The Rs114.50cr related-party guarantee being called while
consolidated cash stays at token levels and gearing stays above the FY26
peak of 88.0%, or the auditor's going-concern Emphasis of Matter repeating
or strengthening in the FY27 audit, would force re-declaring this from a
transition-story small-cap into a solvency-risk name, independent of
whether either transition line is climbing (B02 findings 3, 4, 8; B03
FLAG-CASH).

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

*(Drafted at Halt 1 from B01-B09, per prompts/13-synthesis-pipeline.md's
five-question spec. This is the draft version; Stage 13's copy, when it
runs, is the final one. The text below is the version already assembled in
outputs/final/business-narrative.md from the same block evidence and is
reused here rather than re-derived, per the operating rule against
re-analysis.)*

Fratelli grows grapes and turns them into wine. It farms about 400 owned
acres and about 1,000 contract farmed acres at Akluj and Jambhali in
Maharashtra, ferments and ages the fruit at a winery holding 5.4 million
litres, and bottles more than 50 labels across luxury, super premium,
premium and value tiers. Bottled still wine is about 90 percent of revenue,
and the luxury names Sette and J'NOON carry the brand claim, with 250 awards
and five Decanter scores above 90 points behind them. The second product is
Shotgun, a canned ready to drink alcoholic drink launched in February 2025,
made on the same winery infrastructure and moved by the same field sales
team, which with TiLT wine in a can is about 10 percent of revenue. No
customer has to buy either product, so demand rests on preference and
price, not on need; the honest version of "why the customer cannot do
without it" is that the customer can, and wine is under 1 percent of
India's alcohol market by volume.

The buyers are private distributors and retailers across 29 states and
union territories, government beverage corporations in the states that run
a corporation model, hotel and restaurant venues, 29 Canteen Stores
Department canteens that supplied about 8 percent of the June 2026 quarter
topline, and export buyers in 15 to 17 countries who took about 1.7 percent
of FY26 revenue. Buying behaviour is thin on lock in: no long term customer
contract is disclosed, no reorder rate or active outlet metric is disclosed
against the 31,000 touch point count, and the largest single customer fell
from 17.3 percent to 11.6 percent of group revenue in one year. A
substantial portion of receivables sits with government corporations that
set their own payment cadence, which is one reason collection runs at 212
days.

Demand today comes from premiumisation among urban affluent drinkers and
from the fast start of the canned format, and it is gated by rules rather
than by taste. The run named six downstream signals that carry that demand:
state excise duty and licensing notifications, which control market access
and shelf price; CSD empanelment and procurement, the one assured demand
channel; the India EU FTA wine tariff schedule; the USD to INR rate; the
Nashik and Akluj table grape price index; and the quarterly disclosures of
Sula Vineyards and Grover Zampa, the only independent read on share. Each of
the six is externally checkable, in state excise gazettes, Ministry of
Defence procurement data, DGFT notifications, the RBI reference rate, and
APMC Nashik price bulletins.

Whether demand should grow is contested inside this run's own evidence.
Management and the annual report cite a wine market of roughly Rs 1,900 cr
to Rs 2,300 cr growing near 16 percent a year to the early 2030s, and the
independent market data corroborates the size. The market leader told its
own investors in August 2026 that the category has shown low single digit
growth at best over two years and that its own revenue has been almost flat
near Rs 600 cr for three to four years. The pipeline used the realised rate,
about 4 percent, not the projected 16 percent, and the India EU FTA cuts
the other way by pulling landed import prices toward Rs 2,000, which is the
exact boundary Fratelli uses to define the luxury tier it calls its fastest
growing engine.

The competitive advantage sits, to the extent it sits anywhere, in the
still wine line and not in the canned line. Still wine has the two best
evidenced candidates: 15 years of proprietary grape clone work, imported
varietals grafted onto Indian rootstock that the company itself calls hard
to copy in the near to medium term, and a distribution network of 31,000
touch points across 29 states. The canned line has no moat and should be
said so plainly: Shotgun needs no vineyard, and any beverage maker with a
canning line and a distributor can enter. The forward moat scan scored 13
out of a possible far higher total and classified the position MODEST, with
three moderate categories, product platform reuse, backward integration
into grapes, and CSD qualification access, and its two newest categories,
tested on a two leg standard and on a named sacrifice standard, both scored
zero. Gate 0 scored the moat at NONE, and the wine segment result went from
a profit of Rs 19 cr in FY24 to losses of Rs 10.5 cr in FY25 and Rs 10.6 cr
in FY26, so none of the three moderate categories has yet converted into
segment profit.

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. Verticals framed, one per dominant variable

**Vertical 1 — Recomputed EBITDA reliability.** The corpus establishes a
consistent recomputation method (PBT + finance cost + depreciation) applied
to filed results across five quarters, showing the metric turning positive
for the first time in Q1 FY27 at +Rs0.95cr / 2.1% margin (B05
red_flags/analyst_note). It cannot establish which basis (subsidiary or
consolidated) management intends to hold going forward, since the two bases
diverge materially and Verifier B ruled the prior sign-flip framing
overstated rather than resolving which basis is the right one to track
(B05 supersessions; B12b). Questions: (1) On which basis, subsidiary or
consolidated, will management report EBITDA from Q2 FY27 onward, and will
it hold that basis consistently? (2) Does the Q1 FY27 positive print
survive Q2 FY27, or does it revert? (3) Does the Q1 FY27 transcript, if
ever published, reconcile management's own claim to the filed number on the
call?

**Vertical 2 — Wine-segment profitability.** The corpus establishes the
audited Ind AS 108 segment result for three years: +Rs18.92cr (FY24),
-Rs10.49cr (FY25), -Rs10.61cr (FY26) (B02 finding 2; B04 must_track_metrics).
It cannot establish a case-level or SKU-level profitability split within the
segment, or a winery utilisation rate to test whether the loss is a fixed-
cost-absorption problem or a pricing problem (B04 input_gaps). Questions:
(1) Does the FY27 AR's segment note turn positive, breaking the two-year
streak? (2) What is winery utilisation, and is the loss driven by
under-utilisation of the 5.4 million litre capacity? (3) What is the
selling/distribution/marketing ratio trend (23.3% of wine revenue in FY26,
down from 25.7%) — does it keep falling as management promised, or does it
flatten as it did through most of FY26 (B04 must_track_metrics; B12b missed
finding on the A&P reduction promise)?

**Vertical 3 — Shotgun RTD scale and margin.** The corpus establishes
outlet, state and case-volume counts (18 states, ~9,000 outlets, ~100,000
cases FY26) that management has met or exceeded against its own targets
(B05 promise_delivery rows 13, 14). It cannot establish case-level ASP or
gross margin for RTD versus still wine, since the audited segment note
reports them as one line (B04 unit_economics; mgmt_questions). Questions:
(1) Does case growth sustain the roughly 1.5x-2x YoY cadence toward
200,000 cases FY27? (2) Does the blended gross margin hold as RTD mix
rises, given RTD's disclosed 65-70% margin sits below wine's 70%+? (3) Do
the internally inconsistent RTD market-size and share figures management
has given (10% by cases, 3.6% by value, 6% claimed elsewhere) ever get
reconciled to one number?

**Vertical 4 — Cash against the guarantee, and working capital.** The corpus
establishes consolidated cash of Rs7.78 lakh and standalone cash of
Rs0.88 lakh against Rs119.74cr of Group borrowings and a new Rs114.50cr
related-party guarantee the going-concern notes never name or stress-test
(B02 findings 3, 4, 15; B03 triple_pass_verification). It cannot establish
the split of receivables between government-corporation and private-party
customers, which Note 36(C) says only "a substantial portion" sits with
corporation customers (B02 receivables_trend; gate-recommendation.md
missing-evidence item 2). Questions: (1) Is the guarantee called, or is the
cash cushion rebuilt materially above token level? (2) Does the FY27
AR's going-concern language change? (3) Does the rebate/payables-accrual
balance (Rs840.81 lakh to Rs1,598.00 lakh in FY26) that drove the one
positive operating-cash-flow year revert in FY27, confirming FY26 was a
timing effect rather than an inflection (B02 finding 15/analyst_note; B03
monitorables item 3)?

### 4b. Candidate signal table

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| Maharashtra (and other state) excise duty/licensing notifications | A new state-level restriction lands on a Fratelli core state (Maharashtra, Telangana, Karnataka, Delhi) without a matching peer disruption, showing the excuse pattern is company-specific, not sector-wide | Event-driven | State excise department gazette notifications/circulars (B09) |
| CSD (Canteen Stores Department) wine empanelment and procurement disclosures | CSD share of revenue stalls below the current ~8%, or the claimed ~45% CSD share is not corroborated by CSD's own procurement data | Quarterly | Ministry of Defence / CSD annual procurement data (B09) |
| India-EU FTA wine tariff implementation schedule (CIF thresholds, phased duty cuts) | The duty-phasing schedule that lands differs from Fratelli's stated terms (75% initial, easing to 20%/30%, EUR2.5 CIF floor), or lands faster than guided | Event-driven | DGFT / Ministry of Commerce FTA notifications (B09) |
| USD/INR exchange rate | A sustained rupee depreciation materially cuts the post-FTA landed-cost gap Fratelli's luxury tier depends on | Monthly | RBI reference rate (B09) |
| Nashik/Akluj table grape price index (harvest cost) | A further harvest cost spike (following Sula's disclosed near-doubling in the 2026 harvest) with continued silence from Fratelli on the identical input, contradicting Fratelli's "no major changes" framing | Event-driven | APMC Nashik market price bulletins / state agri-marketing board (B09) |
| Sula Vineyards and Grover Zampa quarterly/annual disclosures | A subsequent Sula or Grover Zampa filing continues to omit any mention of Fratelli as a competitor, or discloses a combined share figure further from the claimed duopoly | Quarterly | Company investor presentations, exchange filings (B09) |

### 4c. Fragility read

- **variable_count: 7.** (1) Recomputed EBITDA turning and staying positive
  on one held basis; (2) wine-segment Ind AS 108 result turning positive;
  (3) Shotgun case-volume growth sustaining without margin drag; (4) cash
  rebuilt / guarantee not called; (5) state excise and licensing stability
  across multiple states simultaneously; (6) EU FTA duty-phasing not
  compressing the luxury tier faster than management's guided schedule; (7)
  independent (peer or third-party) confirmation that the claimed market
  share and duopoly framing hold up over time.
- **verifiability_ratio: 5 of 7 externally observable** via audited filings,
  gazette notifications, or peer disclosure (wine-segment result, cash and
  guarantee status, state excise notifications, the FTA schedule, and peer
  share confirmation). Two of seven — the recomputed-EBITDA basis management
  chooses to report and hold, and Shotgun's case-volume/margin trajectory —
  are verifiable only through company-narrated figures, against a
  credibility grade of D (B05 credibility_grade; B12b credibility_grade_
  concur).
- **single_point_failure:** the Rs114.50cr related-party guarantee being
  called against near-zero cash (Rs7.78 lakh consolidated, Rs0.88 lakh
  standalone). That alone would force the business-falsifier reading in
  Part C3 regardless of how either transition line is performing (B02
  findings 3, 4; B03 FLAG-CASH).
- **fragility_verdict: FRAGILE.** Seven variables, two of them verifiable
  only through a management track record graded D, and one named
  single-point-failure that does not require any other variable to break
  first.

### 4d. Research brief — live-web work this corpus cannot do

1. Check the BSE announcements feed and the company investor page for the
   Q1FY27 concall transcript, and for any subsequent commentary on the
   30%/breakeven FY27 guidance.
2. Pull Sula Vineyards' and Grover Zampa's next quarterly disclosures to
   test the one-third-share and duopoly claims longitudinally.
3. Verify Grover Zampa's reported 12-15% market share against a primary
   source; the current figure rests on a general web search and a stale
   2016-2022 Statista series (B09 stale_data_flags).
4. Query the SEBI SCORES complaints-redressal database and SEBI/SAT order
   search directly for Bhupinder Kumar Sekhri, Gaurav Sekhri, Tinna Trade
   and Tinna Rubber and Infrastructure; this container has no tool access to
   those portals (B08 searches_skipped).
5. Verify Mayank Singhal's board seat on Fratelli Wines Pvt Ltd and his
   TP Buildtech Private Limited co-directorship with Gaurav Sekhri via
   Zauba, Tofler or the MCA portal; direct fetches were blocked by the
   network egress proxy in this container (B08 searches_skipped).
6. Confirm whether any credit rating agency has since rated the wine entity,
   post the FY26 AR.
7. Check the current DGFT/Ministry of Commerce status of the India-EU FTA
   wine tariff schedule, given management's own inconsistent framing of it
   across quarters (B05 1C).
8. Check state excise department gazette notifications for Maharashtra,
   Telangana, Uttarakhand, Karnataka and Madhya Pradesh for FY27
   developments affecting Fratelli and its peers.
9. Pull CSD procurement data to verify the claimed ~45% CSD share.
10. Run a dedicated news-archive search (Economic Times, Mint, Business
    Standard) for investigative coverage of the Sekhri family and the Tinna
    Trade history; triaged out of the promoter check on this run for time
    (B08 searches_skipped).
11. Watch for a stated rationale or a board appointment for Bhupinder Kumar
    Sekhri following the August 2026 20.79% gift transfer.
12. Watch for the CIT(Appeals) ruling on the Rs663.03 lakh Section 270
    misreporting-of-income penalty (AY 2018-19).

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. Fratelli grows grapes in Maharashtra and turns them into wine, sold under
   more than 50 labels, from luxury down to value.
2. Since February 2025 it also fills cans with a ready-to-drink alcoholic
   drink called Shotgun, using the same winery and sales team.
3. FY26 revenue was Rs181 cr and the net loss was Rs25 cr; the business
   listed through an old commodity-trading shell, not through an IPO.
4. Buyers are private shops and restaurants across 29 states, government
   beverage corporations, and 29 defence canteens; nobody has to buy wine,
   so demand depends on taste and price, not need.
5. The biggest single customer fell from 17.3% to 11.6% of revenue in one
   year, and no reorder rate is disclosed for the 31,000 sales outlets the
   company claims.
6. Demand growth is disputed even inside this run's own sources: management
   cites a market growing about 16% a year, while the market leader told its
   own investors growth has been low single digits for two years.
7. A tariff cut on European wine, expected under the India-EU trade deal,
   threatens exactly the luxury price band Fratelli calls its fastest
   growing and best protected segment.
8. The strongest edge sits in still wine, not the cans: 15 years of grape
   breeding work that is hard to copy quickly, plus a large sales network.
9. Shotgun, the canned drink, has no real moat. Any drinks maker with a
   canning line and a distributor can make something similar.
10. A forward-looking scan of new advantages scored this business MODEST,
    not strong, and found none of its promising signs has yet turned into
    segment profit.
11. The mental model here is a bet on two changes at once: still wine
    proving its two-year loss streak was temporary, and the new can product
    scaling without losing margin, while cash stays thin against a large
    related-party guarantee.
12. On the evidence gathered, that bet is fragile: seven things have to go
    right, most of the company-only claims carry a poor credibility grade,
    and one single event, the guarantee being called against near-empty
    cash, could break the whole thesis on its own.
13. The corpus could not establish per-case pricing or margin for either
    wine or Shotgun, or the winery's utilisation rate, so no unit-level
    profitability check was possible.
14. The corpus also could not establish an independent, non-company market
    share figure; Fratelli's own audited numbers put its share nearer 8%
    of its own cited market, not the one-third the company claims.
15. The two biggest open questions for the next quarter: does recomputed
    EBITDA stay positive on one basis for two quarters running, and is the
    Q1 FY27 concall transcript ever published, given all three peers filed
    theirs on schedule and Fratelli did not.

---

## SECTION 6: STANDING EXTRACTION ANNEX

Ten standing questions, answered from corpus. Quote-then-comment; filename
and PDF page anchor confirmed against the page marker on every quote before
writing it, per this run's citation-accuracy audit finding against stage 6.

### 1. UNITS

No per-case, per-bottle or per-litre realisation figure is printed anywhere
in the corpus for either still wine or Shotgun RTD. The closest management
gets is aggregate case-volume counts with no matching rupee figure attached
in the same sentence:

> "Sold around 100K cases in FY26. Targeting to double sales in FY27"
> (Investor_Presentation_Q4FY26_May2026.pdf, p.13)

Comment: this is a volume figure with no realisation attached. The revenue
line it maps to is wine-manufacturing-and-sales segment revenue of
Rs18,120.04 lakh (Rs181.20cr) for the year ended 31-Mar-2026
(Annual_Report_FY2026.pdf, p.190, Note 37 Segment Information), which covers
still wine and Shotgun combined with no split. No case-level ASP or margin
figure exists in any AR note, results filing, investor deck, or concall
transcript reviewed across this run (B04 unit_economics: "NOT FOUND — only
SKU-level MRPs disclosed"). SKU-level MRPs are retail ceilings, not company
realisation, and are not summed here because they do not represent what
Fratelli actually receives per unit.

### 2. SEGMENT CAPITAL AND DEBT

> "Segment Assets / Agro Commodities 14.91 1,331.51 / Steel Abrasives - - /
> Wine manufacturing and sales 34,498.16 31,126.25 / Segment operating
> assets 34,513.07 32,457.76 ... Segments liabilities / Agro Commodities
> 56.33 35.13 / Steel Abrasives - - / Wine manufacturing and sales 20,920.77
> 17,061.55 / Segment Operating Liabilities 20,977.10 17,096.68 /
> Reconciliation of segment operating liabilities to total liabilities /
> Borrowings (refer note 17) - 611.44"
> (Annual_Report_FY2026.pdf, p.190, Note 37 Segment Information, consolidated,
> figures in Rs lakh, FY26 column first, FY25 comparative second)

Comment: segment assets and liabilities are disclosed by segment
(Agro Commodities, Steel Abrasives, Wine manufacturing and sales) for both
FY26 and FY25. Borrowings are explicitly UNALLOCATED to any segment: the
note reconciles segment operating liabilities to total liabilities by adding
back "Borrowings" as a separate, unallocated line — Rs Nil in FY26 and
Rs611.44 lakh in FY25 (the FY25 figure being the parent's own standalone
borrowing before the Group's Rs119.74cr of FY26 Group borrowings sat
entirely outside segment allocation). Capital employed by segment is not a
separately labelled line; it can be derived as segment assets less segment
liabilities: wine manufacturing and sales carried Rs34,498.16 lakh of
segment assets against Rs20,920.77 lakh of segment liabilities in FY26.

### 3. GUIDANCE VERSUS ASPIRATION

Classified (a) guidance with a period, (b) aspiration without a period, (c)
capacity/capability only, drawn from the concall record (B05 1B, quotes
retained in that stage's own extraction):

- (a) Guidance with a period: "FY26 revenue guidance... ~Rs250cr (20% to 25%
  growth, excl. Shotgun)" (Concall_Q4FY25_Jun2025_Transcript.pdf, p.12, per
  B05 1B), successively revised to 15-20% (Q1 FY26 call, p.11), 12-15%/also
  "10% to 15%" (Q2 FY26 call, p.9 and p.14), and ~7% (Q3 FY26 call, p.13),
  against an actual delivered growth of ~1% (Q4 FY26 call, p.6). "FY27
  revenue guidance... ~30% growth, 'PAT breakeven'" (Concall_Q4FY26_
  Jun2026_Transcript.pdf, p.7, per B05 1B). "FY27 EBITDA margin target...
  10%-12%" (Q3 FY26 call, p.13-14, per B05 1B).
- (b) Aspiration without a period: "Long-term EBITDA margin aspiration...
  15%-20%" (Q3 FY26 call, p.14, per B05 1B). "Long-term revenue target...
  Rs500cr... By 2030" — this one does carry a period (FY30/Vision 2030) and
  is better classified with the guidance items above once the 2030 date is
  attached (Q1 FY26 call, p.13; Q3 FY26 call, p.14; Q4 FY26 call, p.15, per
  B05 1B); B09 independently finds this target requires a 28.9% FY26-FY30
  CAGR against a stage-derived attainable ~9% (B09 flags
  FLAG-VISION2030-GAP).
- (c) Capacity/capability only: winery capacity of 5.4 million litres is
  stated as a physical capability with no utilisation percentage or output
  target attached (B04 input_gaps: "Winery utilisation rate (%) not
  disclosed; only capacity (5.4mn litres)").

### 4. CONCENTRATION

**Customer:**

> "Information about customers / Customers contributing more than 10% of
> the Group's total revenue from one external customer: / 2,103.64 5,243.04"
> (Annual_Report_FY2026.pdf, p.191, Note 37, consolidated, Rs lakh, FY26 then
> FY25)

Comment: Rs2,103.64 lakh on Rs18,128.65 lakh FY26 segment revenue is 11.6%
from the single largest customer; Rs5,243.04 lakh on Rs30,209.66 lakh FY25
revenue is 17.3% — the fall B02 finding 9's cross-reference describes.

**Product:** still wine is approximately 90% of revenue and Shotgun RTD plus
TiLT wine-in-a-can approximately 10%, per B04 revenue_streams (pct_of_revenue
90 and 10); no case-level split within either bucket is disclosed anywhere
in the corpus (see Question 1).

**Geography:**

> "Revenue - Domestic Market 17,160.56 / Revenue - Overseas Market 313.95 /
> 17,474.51 29,557.91" [sic, prior-year total column]
> (Annual_Report_FY2026.pdf, p.191, Note 37, consolidated, Rs lakh, FY26
> domestic/overseas split shown first)

Comment: overseas revenue is Rs313.95 lakh against Rs17,160.56 lakh domestic
in FY26, about 1.8% of the revenue-by-location total shown — consistent
with the ~1.7% export share cited elsewhere in this run's evidence. No
state-by-state or country-by-country revenue breakdown is disclosed; NOT
DISCLOSED for a named top state or top export country.

### 5. PROMISE LEDGER

Table reproduced from B05's chronological tracker (2A), with the
verifier-corrected read carried where Verifier B's audit changed a row's
classification (B12b). Rows 6, 7 and the totals below reflect the correction;
the original stage-5 language for those rows is not carried forward per
this dossier's rule against repeating the superseded sign-flip framing.

| # | Promised in | Promise | Outcome (as corrected by B12b where applicable) | Evidence anchor |
|---|---|---|---|---|
| 1 | Q4 FY25 call | FY26 revenue ~Rs250cr (20-25% growth) | Missed — Rs181.29cr delivered, ~1% growth | Concall_Q4FY25_Jun2025_Transcript.pdf p.12; Results_Q4FY26_and_FY26_2026-05-30.txt |
| 2 | Q1 FY26 call | FY26 growth 15-20% | Missed | Concall_Q1FY26_Aug2025_Transcript.pdf p.11 |
| 3 | Q2 FY26 call | FY26 growth 12-15% (also 10-15%) | Missed | Concall_Q2FY26_Nov2025_Transcript.pdf p.9, p.14 |
| 4 | Q3 FY26 call | FY26 growth ~7% | Missed, even the final restatement | Concall_Q3FY26_Feb2026_Transcript.pdf p.13 |
| 5 | Q2 FY26 call | Q2 FY26 EBITDA positive, Rs1.47cr | Delivered on the subsidiary basis Fratelli was quoting | Concall_Q2FY26_Nov2025_Transcript.pdf p.4 |
| 6 | Q3 FY26 call | Q3 FY26 EBITDA Rs5.5cr / 8.6% margin | Delivered on the subsidiary basis (Rs5.42cr/8.5% recomputed on that basis, per B12b) | Concall_Q3FY26_Feb2026_Transcript.pdf p.6; B12b finding row "not supported" |
| 7 | Q3 FY26 call | 9M FY26 EBITDA Rs4.7cr; Q3 PBT/PAT positive | Q3 subsidiary PBT +Rs11.79 lakh against a claim of roughly Rs0.1cr, an approximate match on the subsidiary basis (B12b); not tested further at the 9-month level in this dossier | Concall_Q3FY26_Feb2026_Transcript.pdf p.5; B12b |
| 8 | Q4 FY26 call | Q4 FY26 breakeven, EBITDA +Rs1.06cr | Subsidiary EBITDA -Rs3.97cr against a stated -Rs3.7cr, an approximate match on the subsidiary basis (B12b) | Concall_Q4FY26_Jun2026_Transcript.pdf p.3; B12b |
| 9 | Q4 FY26 call | FY26 EBITDA +Rs1cr, improved marginally | Subsidiary EBITDA approximately +Rs0.65cr, positive, against a claim of +Rs1.06cr (B12b) | Concall_Q4FY26_Jun2026_Transcript.pdf p.6; B12b |
| 10 | Q1/Q2 FY26 calls | Hospitality construction early 2026, open 2028, budget Rs100cr | Slipped ~1 year to CY27-28, budget revised to Rs70-80cr, opening date never restated | Concall_Q2FY26_Nov2025_Transcript.pdf p.4; Concall_Q4FY26_Jun2026_Transcript.pdf p.9 |
| 11 | Q1 FY26 call | Karnataka greenfield winery | Dropped, never mentioned again | Concall_Q1FY26_Aug2025_Transcript.pdf p.4 |
| 12 | Q2 FY26 call | Equity fundraise for Rs100cr capex programme | Dropped | Concall_Q2FY26_Nov2025_Transcript.pdf p.6-7 |
| 13 | Q4FY25/Q1FY26 calls | Shotgun in 10-15 states by FY26-end | Delivered/exceeded — 18 states | Concall_Q4FY26_Jun2026_Transcript.pdf p.4 |
| 14 | Q3 FY26 call | Shotgun ~100,000 cases by FY26-end | Delivered | Concall_Q4FY26_Jun2026_Transcript.pdf p.4 |

Four further unkept promises Verifier B found that stage 5 never tracked:
the CFO's Q4FY25 deferred-tax guidance (25% ETR, DTA to reverse against
profit), falsified by the FY26 write-off of the entire DTA (Concall_
Q4FY25_Jun2025_Transcript.pdf p.10 vs Results_Q4FY26_and_FY26_2026-05-30
p.11); a holdco-receivable recovery promised "within FY26," with Rs46.72
lakh still outstanding at 31-Mar-2026 (Concall_Q3FY26_Feb2026_Transcript.pdf
p.5); an A&P reduction promised in FY25 (100bps down, 5-6% destination by
2028-30), never delivered, with the destination quietly raised to 7-8% a
year later (Concall_Q4FY25_Jun2025_Transcript.pdf p.11, p.20 vs Concall_
Q3FY26_Feb2026_Transcript.pdf p.7, p.9); and the RTD run-rate disclosure
whose headline numbers are internally inconsistent within one answer
(Concall_Q4FY26_Jun2026_Transcript.pdf p.8) (all per B12b findings).

Verifier B's corrected tally: approximately 5 delivered, 1 partial, 7
missed, before adding the four untracked unkept promises above (B12b
pipeline_flags_not_supported).

### 6. RESTATED BASES

> "1. Corporate Information / Fratelli Vineyards Limited (formerly known as
> Tinna Trade Limited)... is primarily engaged in the trading of agro
> commodities such as wheat, yellow peas, chana, lentils, oilseeds, and oil
> meals, as well as steel abrasives including steel shots and steel cut wire
> shots... It has a subsidiary engaged in manufacturing, purchases & sales of
> wines with European technological expertise and is one of India's luxury
> winemaker."
> (Annual_Report_FY2026.pdf, p.148, Note 1, Corporate Information, consolidated)

Comment: this is the FY26 consolidated financial statements' own
description of the Holding Company as "primarily engaged" in agro/steel
trading, filed alongside a year in which the Group's own segment note shows
wine manufacturing and sales as 99.9% of segment revenue (B02 finding 2).
No Ind AS 105 discontinued-operations restatement exists to formally retire
the trading description; Note 1 was not updated for the wine-only reality
(B02 restatements_found).

> "During the previous year ended March 31, 2025, the Company prepared its
> consolidated financial statements for the first time pursuant to the
> acquisition of its wholly owned subsidiary, Fratelli Wines Private
> Limited. The business combination, being a common control transaction,
> was accounted for using the pooling of interest method in accordance with
> Appendix C to Ind AS 103 – Business Combinations. Accordingly, the
> comparative figures for the year ended March 31, 2025 presented in these
> consolidated financial statements are the restated consolidated figures
> prepared in the previous year in accordance with Paragraph 9(iii) of
> Appendix C to Ind AS 103."
> (Annual_Report_FY2026.pdf, p.197, Note 43, Share Swap, consolidated)

Comment: the FY25 comparative figures carried in the FY26 AR are themselves
restated under the Appendix C pooling-of-interests method, not the original
figures as first reported. This is the mechanism behind the FY24 pooling
restatement B01 and B02 both flag as mixing wine with the exited agri-
trading book (B01 data_notes; B02 top_findings rank 2).

### 7. CORPORATE-ACTION CLAUSES

**Share swap (business combination), the mechanism that brought the wine
business into the listed shell:**

> "Share swap Arrangement approved by the shareholders on April 01, 2024,
> Fratelli Vineyards Limited (Formerly Known as Tinna Trade Limited)
> acquired Fratelli Wines private Limited, a wholly owned subsidiary under
> common control... The acquisition was effected through a share swap...
> This transaction falls under the purview of Appendix C to Ind AS 103 –
> Business Combinations of Entities under Common Control. As per the
> Appendix, such combinations are accounted for using the pooling of
> interests method... a) The assets and liabilities of the combining
> entities are reflected at their carrying amounts as appearing in the
> books of the transferor. b) No adjustments are made to reflect fair
> values or recognize any new assets or liabilities. c) No goodwill is
> recognized. d) The difference, if any, between the consideration (fair
> value of shares issued) and net assets acquired is recognized in capital
> reserve... The Company issued 3,07,79,177 equity shares of ₹10 each to
> the shareholders of Fratelli Wines Private Limited in the ratio of 2.5 as
> per the scheme."
> (Annual_Report_FY2026.pdf, p.197, Note 43, Share Swap, consolidated)

Comment: liability-allocation clause is at carrying amounts, no fair-value
step-up, no goodwill; the ratio is 2.5 Fratelli Vineyards shares per Fratelli
Wines share; the appointed/effective date for the 100% acquisition is
"With effect from April 22, 2024" (Annual_Report_FY2026.pdf, p.148, Note 1).
The transaction carried no cash or contingent consideration.

**Preferential allotment and warrants (2024-25):**

> "During the year ended March 31, 2025, the Company has made preferential
> allotment of 10,72,466 equity shares at ₹300 per share (with a securities
> premium of ₹290 per share)... During the year ended March 31, 2025, the
> Company has converted 28,61,500 share warrants at an issue price of ₹72...
> The Company had allotted 5,57,650 fully convertible share warrants to the
> promoters on August 23, 2024 at an issue price of ₹300/-... At the time of
> allotment, the Company received 25% of the issue price (₹75 per warrant)."
> (Annual_Report_FY2026.pdf, p.108, Note 13(e), standalone)

> "As per the terms of issue... the warrants were required to be converted
> within 18 months from the date of allotment, i.e., on or before February
> 22, 2026, failing which the warrants would lapse... Accordingly, the
> balance 3,63,150 fully convertible share warrants were not exercised
> within the stipulated conversion period and consequently lapsed with
> effect from February 23, 2026."
> (Annual_Report_FY2026.pdf, p.109, Note 13(e)-(f), standalone)

Comment: 3,63,150 of 5,57,650 warrants lapsed, 65.1%, confirming the
correction the operator flagged over the earlier 39.5% figure (B02 finding
5; B12a).

**Inter-se promoter gift transfer (August 2026):**

> "Total 90,36,779 20.79%" ... "The Aggregate holding of promoter and
> promoter group before and after the above inter-se transaction shall
> remain the same." ... "4f. Rationale, if any, for the proposed transfer:
> Inter-se transfer by way of Gift amongst Promoters" ... "8. Declaration by
> the acquirer... The proposed acquisition is by way of gift without
> consideration. Accordingly, the acquisition price is nil."
> (2026-08-14_inter-se-transfer-promoter-group.pdf, p.1, p.4-5)

Comment: 20.79% of the company moves from Gaurav Sekhri (MD), Aarti Sekhri,
Shobha Sekhri and Puja Sekhri to Bhupinder Kumar Sekhri, a promoter with no
board seat, for nil consideration, with no rationale beyond "gift" (B08
adverse_findings). No scheme, demerger, merger or buyback appears anywhere
in this corpus beyond the two corporate actions quoted above.

### 8. RELATED-PARTY PERIMETER

Every promoter-group entity named in Note 33's RPT note, FY26 (all figures
Rs lakh, consolidated):

| Entity | Nature of transaction, FY26 |
|---|---|
| Tinna Tradefin Limited (formerly Tripat Ventures Limited) | Nil FY26 transactions listed; FY25 comparator only |
| BGK Shipping LLP | Export Expense 1.56 |
| Tinna Rubber and Infrastructure Limited | Nil FY26 transactions listed; FY25 comparator only |
| Gaurav Sekhri (MD) | Loan received 775.50, loan repaid 589.00, reimbursement 3.68, interest on loan 50.46, lease payments 11.10, proceeds from share capital 67.50 |
| Rajesh Kumar Garg (CFO) | Remuneration paid 48.06 |
| Adhiraj Amar Sarin, Rahul Rama Narang, Nakul Nitin Zaveri, Sanjit Singh Randhawa, Sanjay Kumar Jain, Sanvali Kaushik | Director sitting fees, 0.12 to 4.48 each |
| Charme Di Secci Alessio E Secci Andrea SNC | Consultancy services 38.16 |
| Ran Vijay Farms & Developers Pvt Ltd | Lease payments 30.17 |
| Shivratna Agro Products Pvt Ltd | Lease payments 41.54 |
| Sanyuktarjun Agro Farms Pvt Ltd | Interest paid on loan 15.00, lease payments 35.08 |
| Shankarratna Agro Farms Pvt Ltd | Lease payments 46.64 |
| Chin Min Developers Private Limited | Nil FY26 transactions listed; FY25 comparator only |
| Mrs. Puja Sekhri (ED) | Purchase of raw material 1.43, issue of share capital 67.50, reimbursement 28.92, loan taken 240.00, loan repaid 190.00, interest paid on loan 0.29, lease payments 7.04, remuneration paid 115.96 |
| Alessio Secci | Consultancy services 58.03, reimbursement 18.55; Advance Given balance Nil FY26 (was 294.58 FY25) |
| Mrs. Shobha Sekhri | Issue of share capital 167.63 |
| Mrs. Aarti Sekhri | Issue of share capital 67.50 |
| Mr. Aditya Brij Sekhri (ED) | Remuneration paid 64.60, lease payments 11.10, reimbursement 43.77 |
| Mr. Keshav Sekhri | Remuneration paid 5.48, reimbursement 2.78 |
| Mr. Mohit Kumar (Company Secretary, up to Apr-2026) | Remuneration paid 13.01, reimbursement 0.57 |
| TP Buildtech Private Limited | Reimbursement of expenses 0.40 |

> (Annual_Report_FY2026.pdf, p.181-183, Note 33, Related party disclosure,
> consolidated)

Comment: this is the FY26 column of a table that also lists FY25
comparators for every row; only FY26 amounts are reproduced here per the
question's "latest year" scope. Entities named as related parties but with
no FY26 transaction value shown in the note (Gee Ess Pee Land Developers
Pvt. Ltd, B.G.K Infratech Pvt. Ltd, Prasidh Estates Pvt. Ltd, Sekhri Family
Annuity Trust) are listed in the entity roster (Annual_Report_FY2026.pdf,
p.181, Note 33(A)(ii)) but their FY26 transaction amounts, if any, were not
located in the transaction table reviewed for this annex; B08 separately
flags the Sekhri Family Annuity Trust's on-market accumulation from 100 to
15,502 shares FY25 to FY26 (B08 transition_evidence).

### 9. PLEDGE AND SHAREHOLDING

**Pledge:**

> "According to the information and explanations given to us and based on
> our examination of the Standalone Financial Statements of the Company,
> the Company has not raised loans during the year on the pledge of
> securities held in its subsidiary. Accordingly, the requirement to report
> on clause 3(ix)(f) of the Order is not applicable to the Company."
> (Annual_Report_FY2026.pdf, p.83, CARO Annexure A, clause (ix)(f), standalone
> Independent Auditor's Report)

Comment: this is the auditor's CARO clause confirming no loans were raised
against a pledge of the subsidiary's securities; it does not, on its own,
certify zero promoter share pledge in general, but no promoter-share-pledge
disclosure of any kind was located anywhere in either AR (B08
pledge_pct_latest: 0; pledge_trend: "stable at 0% across FY25 and FY26; no
promoter share pledge found... only routine fixed-deposit pledges against
bank borrowings, unrelated to promoter shares"). No dedicated
Regulation-31-style encumbrance table by quarter exists in this corpus;
NOT DISCLOSED for a quarter-by-quarter pledge percentage. Promoter pledge
for the last twelve quarters as filed: NOT DISCLOSED — inputs/shareholding/
is empty and no quarterly shareholding filing is in the corpus; only the two
annual-report snapshots (31-Mar-2025, 31-Mar-2026) and the August 2026 SAST
filings exist (B00 input_gaps).

**Shareholding, latest annual snapshot:**

> "(A) Promoter and Promoter Group / (1) Indian 22 24860106 57.19 ... Total
> Promoter & Promoter Group (A) 22 24860106 57.19 / (B) Public Shareholding
> / (1) FII/FPIs 1 209170 0.48 / (2) Central/State Government 1 28200 0.07 /
> (3) NBFC (registered with RBI) 1 1000 0.00 / (4) NRIs 52 92925 0.21 / (5)
> Foreign Nationals 2 2256698 5.19 / (6) Body Corporate 54 1718874 3.95 /
> (7) Resident Individuals 7421 14111559 32.46 / (8) Others 94 193862 0.45 /
> Total Public Shareholding (B) 7626 18612288 42.81"
> (Annual_Report_FY2026.pdf, p.68, Corporate Governance Report, "Distribution
> of Shareholdings," as on 31-Mar-2026)

Comment: institutional holding latest (31-Mar-2026) reads FII/FPI 0.48% and
Central/State Government 0.07%; no separate domestic-institutional (DII)
line is broken out in this table, and no mutual-fund or insurance-company
holding line appears, implying DII holding is at or near nil or is folded
into "Body Corporate" (3.95%) or "Others" (0.45%) without further
disaggregation — NOT DISCLOSED as a separate DII figure. Promoter and
promoter-group holding stands at 57.19% as of 31-Mar-2026, unchanged in
aggregate by the August 2026 inter-se gift transfer, which redistributes
20.79 percentage points within the promoter group without changing the
group total (2026-08-14_inter-se-transfer-promoter-group.pdf, p.2, "The
Aggregate holding of promoter and promoter group before and after the
above inter-se transaction shall remain the same").

### 10. VERIFICATION

Every filename and date quoted in this annex:

- Annual_Report_FY2026.pdf — board-adopted 30-May-2026 (per Note 1,
  p.148: "These consolidated financial statements are adopted by the Board
  of Directors during the meeting held on May 30, 2026")
- 2026-08-14_inter-se-transfer-promoter-group.pdf — dated 14-Aug-2026
- Investor_Presentation_Q4FY26_May2026.pdf — dated May 2026, per B00 inventory
- Concall_Q4FY25_Jun2025_Transcript.pdf — call 30-May-2025
- Concall_Q1FY26_Aug2025_Transcript.pdf — call 13-Aug-2025
- Concall_Q2FY26_Nov2025_Transcript.pdf — call 18-Nov-2025
- Concall_Q3FY26_Feb2026_Transcript.pdf — call 16-Feb-2026
- Concall_Q4FY26_Jun2026_Transcript.pdf — call 2-Jun-2026
- Results_Q4FY26_and_FY26_2026-05-30.pdf — filed 30-May-2026

CORPUS COMMIT HASH: 7ff6592de8194c907b07449e3dc4201ece4df070
