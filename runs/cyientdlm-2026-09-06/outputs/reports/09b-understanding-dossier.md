# HALT 1 UNDERSTANDING DOSSIER: Cyient DLM Ltd (CYIENTDLM)
Run date: 2026-09-06 | Assembled by: Stage 09b | Model: Sonnet 5
Corpus commit: 325c97abbbbbf9d13da4b97ac332767b5c2b2edf

This dossier assembles what the evidence stages (B00-B09) and the phase-1
verifiers (B12a-B12d) already found. It carries no valuation, no price, and
no verdict. Stages 10 and 11 did not run. The phase-1 gate recommendation
is REWORK, on two mechanical triggers (verifier B acceptance 33%, overall
confidence delta 54, both below the 60 floor). REWORK judges the concall
analysis (stage 5), not the company. Read this dossier alongside
outputs/final/gate-recommendation.md, which carries the full trigger
detail, the binding adjudications, and the flag record.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

### 1. Concalls
Four transcripts held, all primary-company:

| File | Date | Quarter |
|---|---|---|
| Concall_Oct_2025_Transcript.pdf | 2025-10-14 | Q2 FY26 |
| Concall_Jan_2026_Transcript.pdf | 2026-01-20 | Q3 FY26 |
| Concall_Apr_2026_Transcript.pdf | 2026-04-21 | Q4 FY26 / FY26 full year |
| Concall_Jul_2026_Transcript.pdf | 2026-07-21 | Q1 FY27 |

(B00 concall_quarter_map)

Most recent quarter covered: Q1 FY27 (call dated 21-Jul-2026). Given the
run date of 2026-09-06, roughly six weeks after that call, a Q2 FY27
results call has plausibly not yet been held (EMS peers in this corpus
report Q2 calls in Oct/Nov, per B06 peer_coverage_map). No transcript is
plausibly missing on quarter-timing grounds. Twelve peer concall
transcripts are also held (AVALON, KAYNES, SYRMA, four quarters each);
these are B06/B12d scope, not the primary-company inventory.

### 2. Annual reports
Two held: AR FY2024-25 (Annual_Report_2025.pdf, 287pp) and AR FY2025-26
(Annual_Report_2026.pdf, 174pp). The latest completed FY (FY2025-26,
year ended 31-Mar-2026) is present and is the primary source. Only two
years are held against a corpus norm of three-plus; this is OVER the
0-1 contract for this run (B00 input_gaps, type annual-report,
OVER_CONTRACT), but it still means the company's own audited history in
the corpus reaches back only to FY2023 comparatives inside these two
reports (data_years: 4, fy_range FY2023-FY2026, B01). No prospectus and
no FY2023-24 AR exist in the corpus, so nothing carries figures earlier
than FY2023.

### 3. Results filings
ABSENT. No quarterly or annual results filing (BSE/NSE Reg 33 outcome) is
in the corpus (B00 input_gaps, type results). Gate 0 fell back to
screener-Data_Sheet.csv plus the AR financial statements (B01). There is
therefore no results-to-AR quarter gap to name; there is simply no results
filing of any date. Promise-versus-delivery in B05 was checked against the
next transcript's own restatement of the prior quarter, never against a
filed results PDF (B05 method note).

### 4. Investor presentations
One held: Investor_Presentation_1.pdf, described in B04 as the Q1 FY27
deck, which postdates the AR FY2025-26 and was used for trend
confirmation (B04 input_gaps). No date range across multiple decks exists
in the corpus.

### 5. Research / rating
Both ABSENT. No rating rationale (B00 input_gaps, type rating; B01
input_gaps) and no broker note or research report of any kind (B00
input_gaps, type research). B09 confirms no independent third-party
market-sizing document exists in the corpus either; web search was the
only route the stage had to cross-check the company's TAM claim, and that
falls outside this evidence corpus.

### 6. Corporate actions
ABSENT as a filing type. No Reg 30 announcement folder exists in the
corpus (B00 input_gaps, type announcements). The one corporate action
found in the run, the Altek Electronics Inc acquisition (04-Oct-2024, via
Share Purchase Agreement), is known only through the AR's own Note 32/33
Business Combinations disclosure (AR FY2025-26, p.169-170), not through a
contemporaneous exchange filing. The "documented-ACTION" half of any
intent-versus-action cross-check could not be built (B03 kill_switch_notes
phase 1; gate-recommendation corpus table).

### 7. Freshness pair check
B00 freshness_verdict: **FRESHNESS PAIRS OK**. Read this correctly, per
the orchestrator's own instruction carried in B00's analyst_note. Of the
four defined pairs:

- Pair 1 (newest results filing to same-quarter concall): NO_TRIGGER.
  inputs/results/ is empty, so there is no results filing to trigger the
  check.
- Pair 2 (rating bulletin to full rationale): NO_TRIGGER. inputs/rating/
  is empty.
- Pair 3 (referenced SEBI order to order text): NO_TRIGGER. No SEBI
  order, penalty, adjudication or show-cause reference was found anywhere
  in AR FY2025-26.
- Pair 4 (AR not older than latest audited annual results): PASS. AR
  FY2025-26 (year ended 31-Mar-2026) is the newest audited annual result
  in existence; nothing newer exists to make it stale.

Three of the four pairs did not fail; they never fired, because their
trigger documents are themselves absent from the corpus. Only the fourth
pair had a live trigger, and it passed on its own merits. FRESHNESS PAIRS
OK is not a statement that the corpus is complete (B00 analyst_note).

### 8. VERDICT LINE

**CORPUS GAPPED.**

| Document | Status | Priority | Expected source | Kind |
|---|---|---|---|---|
| IPO Prospectus (DRHP/RHP) | ABSENT | HIGH | SEBI-hosted RHP page / BSE-NSE IPO filings | findable-missing |
| Results filings (quarterly/annual) | ABSENT | MEDIUM | BSE/NSE Reg 33 filings | findable-missing |
| Rating rationale | ABSENT | MEDIUM | Rating agency site (CRISIL/ICRA/CARE), if one exists for this issuer's bank facilities | findable-missing (existence itself unconfirmed) |
| Announcements (Reg 30) | ABSENT | MEDIUM | BSE/NSE corporate announcements | findable-missing |
| Shareholding pattern filing (quarterly) | ABSENT, partly substituted from AR ownership tables at 31-Mar-2026 | LOW | BSE/NSE Reg 31 shareholding pattern filing | findable-missing |
| Research / broker notes | ABSENT | LOW | Broker research platforms | findable-missing |

The company listed in FY2023-24 (about 3.2 years before this run date),
which is why the prospectus is HIGH priority: it is the only document type
that could carry pre-IPO restated financials, the promoter and group-company
history, and a group-company map, and nothing else in the corpus holds them
(B00 input_gaps). No document type here is judged plausibly-nonexistent by
this run; the rating gap is the closest candidate, since the company's debt
is bank-facility, not necessarily a rated instrument, but this run could not
confirm either way and treats it as findable-missing pending Halt 1 checking.

---

## SECTION 2: MENTAL MODEL DECLARATION
**STATUS: DRAFT - PENDING OPERATOR SIGN-OFF.** Nothing in this section is
signed. Signing happens only in claude.ai after live-web stress-testing.

### PART A: THE FROM STATE

**A1. Archetype.** Outsourcing partner (CDMO/EMS/IT services), per the
CLAUDE.md Archetype Library: client concentration, wallet share, capacity
fill, contract stickiness, price per unit. The company operates as a
single reportable business segment, "Electronic manufacturing solutions"
(AR FY2025-26, standalone Note 33 p.136 and consolidated Note 34 p.171),
so one archetype line covers the whole company; the engagement-model split
inside that one segment (Build-to-Print against Build-to-Spec) is the axis
the transition below runs on, not a second business line.

**A2. The simple analogy.** Cyient DLM takes another company's finished
circuit-board design, or a design it partly helped shape, and builds it to
an exacting, certified standard: the kind of part that goes inside an
aircraft, a medical scanner or a defence system, where a failure is not
survivable. Ninety-four percent of its FY26 revenue is Build-to-Print
work: the customer supplies the drawings and the bill of materials, and
Cyient DLM's job is to manufacture and test the part exactly as specified,
passing through the customer's input-cost movements rather than setting
its own price (B04 revenue_streams, pricing_power "weak"). The customer
cannot switch suppliers quickly, because every part number is qualified
into a named programme under AS9100, NADCAP, ITAR, ISO13495 or IATF16949,
and requalifying a second supplier runs for years (B04 moats_present;
B07 category B2). That certification wall is the one durable thing in the
business today. Everything else, the design ownership, the pricing power,
the margin upside, sits in the small slice of revenue this section turns
to next.

### PART B: THE TRANSITION

**B1. From-to.**

| Line | From tier | To tier |
|---|---|---|
| Engagement-model mix (single segment; B2P against B2S) | R2 COST-ADVANTAGED CONVERTER (certification-driven barrier to entry gives a cost position, not pricing power; but FY26 ROCE of 11.4% sits below R2's "durable mid-teens" description, a fit gap the operator should weigh, not paper over — AR FY2025-26 p.27, B01 data_notes) | R3 VALUE-ADDED / SPEC'D SUPPLIER (Build-to-Spec gives design ownership and BOM influence, with 9-20 year programme lengths cited for anchor customers, and management's own claimed 250-300bps EBITDA uplift sits inside R3's 20-25% ROCE band's direction of travel — B04 revenue_stream_note; B05 guidance) |

A second, non-ladder dimension runs alongside this: a geographic shift
from an India-only base to a dual-shore India-and-US footprint via the
Altek Electronics Inc acquisition (closed 04-Oct-2024, AR FY2025-26 Note
32 p.169-170). This is a diversification vector, not a pricing-power
migration, so it is not scored as a second quality-ladder line; it is
carried in Part C as a dominant variable because the FY26 numbers show it
moving in the opposite direction from the India core (see B2 and C1
below).

**B2. The engine.** Two things must physically change to move the
engagement-model line from FROM to TO. First, Build-to-Spec's share of
revenue must scale off its FY26 base. The working number for that base is
6% (B04 revenue_streams; verifier-A-adjudicated per B12a: the AR's own
BRSR Section 16 states 25% of turnover, AR FY2025-26 p.62-63, on a
statutory classification basis that the AR never reconciles to the 6%
figure; the 6% is corroborated twice independently, by the $133.1M B2P
against $8.8M B2S dollar split, AR p.61, and by the standalone Ind-AS
services-transferred-over-time line at 10.3% of standalone revenue, AR
Note 20 p.144). Second, the new certifications obtained this year
(IATF16949, a NADCAP cable-harness re-scope) must convert into design-led,
spec-in wins beyond the single automotive pilot disclosed so far, which
fell to about 1% of revenue within two quarters of being announced (B04
flags; B07 top_moat_risks; B05 1C).

**B3. The proof gate.** Build-to-Spec share, tracked on the standalone
services-transferred-over-time proxy (AR Note 20, 10.3% of standalone
revenue for FY26, not the disputed 25% BRSR figure), crossing into
double digits and holding for two consecutive reporting quarters, WITH
reported (not normalised) consolidated EBITDA margin showing at least
100bps of the 250-300bps uplift management has attached to the transition
over a stated 12-18 month window (Q1 FY27 call, 21-Jul-2026, p.14). Until
both legs move together, the transition is narrative.

**B4. The recognition gap (OPEN QUESTION — resolved at Stage 11).** This
run did not compute a price, a multiple, or a fair value. The open
question Stage 11 must resolve: does the market price already reflect a
Build-to-Spec transition premium for CYIENTDLM, given the name has fallen
about 34.8% over the trailing year (B03 phase_verdicts p6) alongside a
record order book (Rs24,166mn, B03 guidance_table) and an improving
reported EBITDA margin (9.0% to 10.1%, B03/B04)? If the TO state is
already priced, the re-rating engine this thesis needs is gone and only
earnings growth would remain. This run states no number and no
conclusion; the PE gap at Stage 11 answers it.

**B5. The ugliness test.** The ugly optic is the cash-conversion record:
cumulative FY23-26 operating cash flow of -Rs25.07cr against cumulative
PAT of +Rs234.29cr (B01 deal_breakers), and net working capital days
rising 48, 79, 127, 145 across those four years to 161 by Q1 FY27 (B01
data_notes; B04 flags). Management's own framing calls this a deliberate
growth investment behind large-deal execution and post-IPO capacity build
(AR FY2025-26 p.27, cited in B01 flags) — an ARTIFACT-OF-CLIMB framing.
This run's own evidence does not support that framing. The Gate 0
determination is STRUCTURAL (gate-recommendation FLAG-CASH), built on:
management's own twice-broken normalisation promise (promised by Q4 FY26,
Q3 FY26 call p.8; missed, then replaced by a vaguer 100-120 day, "couple
of years" target, Q4 FY26 call p.16); the fact that the build is
inventory-driven, not receivable-driven (Note 9 finished goods +52.0%,
p.155; Note 17 payable days about 84 to about 127, p.161-162); and a
direct peer contradiction (B06) showing two of three EMS peers (AVALON,
SYRMA) improved working capital while growing revenue 27-46% in the same
window that CYIENTDLM's consolidated revenue fell 17.0%, which removes
the "this is just what growth costs" defence. Classification:
**STRUCTURAL-FEATURE**, carried forward as the operator's working
classification pending any Halt 1 evidence that would move it back toward
artifact.

**B6. The transition falsifier** (kept separate from what kills the FROM
business, Part C3). Build-to-Spec share stays at or near its 6% working
level, or the 25%/6% AR disclosure gap resolves toward the lower, artifact
reading, with no named customer converting beyond the single automotive
pilot and no margin uplift appearing in reported EBITDA, through FY28.
That combination says the design-led mix shift is a narrative device, not
an operating change, independent of whatever the India-core B2P business
does on its own.

### PART C: WHAT THE MODEL WATCHES

**C1. Dominant variables.**

1. **Build-to-Spec revenue share against the double-digit FY27 target**,
   tracked via the standalone services-transferred-over-time proxy (Note
   20), not the disputed 25% BRSR figure. Current state: 6% FY26, working
   number (B04, verifier-A-adjudicated).
2. **Consolidated net working capital days and quarterly operating cash
   flow**, against the company's own restated 100-120 day target. Current
   state: 145 days FY26, 161 days Q1 FY27, negative cumulative FY23-26 CFO
   (B01; B05 guidance).
3. **Standalone (India parent) revenue and PAT, reported separately from
   consolidated.** Current state: standalone revenue -29.9%, standalone
   PAT -26.6% FY26, while consolidated PAT rose 7.65% entirely on the US
   subsidiary swing (B02 top_findings rank 1).
4. **Altek Electronics Inc standalone profitability and earn-out
   remeasurement direction.** Current state: Altek's full FY26 profit
   (Rs31.32mn) is below its roughly six-month FY25 profit (Rs39.70mn),
   and the earn-out liability has already been marked down once (B02
   top_findings rank 4; B03 monitorables).

**C2. What the model rejects.** The global EMS market-size figure
management cites (about $650bn 2025 rising to about $1.1 trillion by
2033/2034) is noise for this name: it runs about 70 times the conservative
TAM this run built for CYIENTDLM's actual certified, four-vertical niche,
no peer cites it, and the AR itself gives the terminal year two ways
(2033 in the concalls, 2034 in the MD&A) (B09 mgmt_claim_ratio, flags).
Market size generally is not the binding constraint here: the run's own
TAM work found revenue headroom of about 17 times current capture with a
STRONG runway class (B09 revenue_headroom_x, runway_class); the binding
constraint is execution (cash conversion, credibility, and whether B2S
actually scales), not market size. The AI-data-centre, robotics and
semiconductor-equipment "Expand" narrative is also rejected as a present
signal: it carries no named customer, no disclosed revenue, and was
formalised into a named strategy phase only after the single toughest
analyst challenge in the whole record (B07 catalysts_12m; B05 1C
analyst_note). The order-book-growth parity claim against a 35-40% peer
benchmark is rejected as load-bearing: the benchmark itself is not
representative of the peer set, which spans about 23% to 50% (B06
partially_verified).

**C3. The business falsifier** (distinct from the transition falsifier,
B6; this one kills the FROM business, not just the arrow). Standalone
India-parent revenue and PAT keep declining beyond FY27, DSCR stays
sub-1.0x for a second consecutive year on a consistently-defined basis
(B03 monitorables), and a top-5 customer is lost or a qualified programme
is not renewed, against a backdrop where customer concentration is already
55.71% consolidated and 70.54% standalone (B02 top_findings rank 9). That
combination would say the certification-locked B2P core itself is
structurally shrinking, not merely absorbing the one-time completion of a
large FY25 defence order, which is management's own stated explanation for
this year's decline (B04 first_deterioration_signals).

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE (draft)

Cyient DLM builds electronic assemblies that sit inside machines where a
failure is not survivable, under four certifications, AS9100, NADCAP,
ITAR and ISO13485, plus IATF16949 for its newest automotive work (B04
moats_present; B07 category B2). Printed circuit board assembly is 52% of
FY26 revenue, box build is 30%, precision machining is 16%, and cable
harness assembly is 2% (B04 revenue_streams; AR FY2025-26 p.24, via B03).
A box build is the finished sub-system, boards and wiring and metalwork
assembled into one unit the customer installs directly. Ninety-four
percent of revenue is Build-to-Print: the customer owns the design and
the bill of materials, and the company earns a manufacturing margin with
weak pricing power of its own, passing through input-cost movement as its
main protection (B04 revenue_streams, pricing_power). The remaining 6%,
Build-to-Spec, is where the company holds design influence and where
programme lengths of 9 to 20 years are cited (B04; B07 catalysts_12m).

The customers are global and regional OEMs and Tier-1 suppliers across
four verticals: aerospace 43% of FY26 mix, industrial 27%, medical 19%,
defence 9%, automotive 2% (B03 ar_new_downstream_entities framing; AR
p.51 via B04). Honeywell Aerospace and Thales are named anchor accounts;
Deutsche Aircraft is a new design-led logo; an unnamed Japanese eVTOL
company holds a nine-year programme reaching mass production later this
decade (B03 ar_new_downstream_entities). Buying behaviour cuts both ways:
qualification cycles that run for years lock a customer in once won, but
the same lock-in concentrates risk, with top customers at 55.71% of
consolidated and 70.54% of standalone revenue (B02 top_findings rank 9).

Demand today traces to a short list of drivers the run named and can
check outside the company: BEL repeat orders for the Indian Navy and
Ministry of Defence set the defence order pool; India MoD modernisation
and the defence budget allocation set its size; MeitY PLI and ECMS scheme
disbursement fund the wider ESDM base the company sits inside; Honeywell
Aerospace and Thales order flow drives the aerospace vertical directly
(B09 downstream_candidates). Inside the company, order intake of about
Rs1,843cr in FY26, up 90% YoY, an order book of about Rs2,417cr, and a
full-year book-to-bill of 1.5x are the matching internal evidence (B03
guidance_table; B05 1A).

Demand should grow on drivers that sit outside the company and can be
checked there: the EU ReArm Europe initiative, sized at EUR800bn, feeds
the European defence-electronics pipeline Thales sits inside; the US
CHIPS Act pulls semiconductor capital-equipment subsystem orders, a
vertical the company has only begun naming (B09 downstream_candidates;
B07 optionality_register). Whether demand actually grows through the
company rather than around it is unresolved: all three named EMS peers
grew revenue 27-46% in the same FY26 window that CYIENTDLM's consolidated
revenue fell 17.0% (B06 industry_cross_read), which the peer stage reads
as pointing to execution or company-specific issues rather than a demand
problem.

Competitive advantage sits in one place and is explicitly absent
elsewhere. Build-to-Print, 94% of revenue, carries no moat of its own; it
is a cost-pass-through model, and the company itself names pass-through
clauses as its main hedge (B04 pricing_power, "weak"; irrelevant_ratios).
The one durable advantage, certification and qualification lock-in
(category B2, scored Strong on documented evidence), predates FY26 and is
not itself an emerging moat (B07 active_categories; B12c F-E01). What is
newer and smaller, Build-to-Spec design ownership and the fresh
certifications, is real but modest: the Emerging Moat scan scored 21 on a
scale to about 90 and classed the forward position MODEST, below its own
25-point threshold for an uplift qualifier (B07 em_score, em_classification,
ua_qualifier_met). The AI-data-centre and robotics lanes carry no named
customer and no disclosed revenue and are not scored as active categories
(B07 optionality_register; catalysts_12m).

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. Verticals framed (one per dominant variable, Section 2 C1)

**Vertical 1 — Build-to-Spec revenue share.** The corpus establishes two
internally conflicting figures in the same AR: 25% of turnover (BRSR
Section 16, p.62-63) and 6% (SET-framework infographic, p.7), with the 6%
figure corroborated twice independently (the $133.1M/$8.8M dollar split,
p.61; the standalone services-transferred-over-time line at 10.3% of
standalone revenue, Note 20 p.144) (B04 flags; B12a adjudication). The
corpus cannot establish which basis, if either, management itself
believes is the "real" number, because the AR offers no reconciliation
(B04 mgmt_questions). Questions this leaves open: (1) which figure does
management use internally to track the FY27 double-digit target; (2) has
the FY27 double-digit target itself weakened, given it was silently
dropped from the Q4 FY26 call framing verifier B found (B12b MAJOR
finding, B05 1B/1C/4D); (3) what is the actual product-level margin
differential between B2P and B2S that makes the mix shift matter.

**Vertical 2 — Net working capital / cash conversion.** The corpus
establishes the trend with primary-source precision: 48, 79, 127, 145
NWC days FY23-26 (AR p.27), 161 days by Q1 FY27 (investor deck via B04),
cumulative FY23-26 CFO of -Rs25.07cr against cumulative PAT of +Rs234.29cr
(B01), and a peer cross-check showing two of three peers improved working
capital at higher growth in the same window (B06 contradicted). The
corpus cannot establish a rating agency's independent read (no rating
document exists), nor can it establish whether the FY26 positive CFO
print (a receivable-and-payable timing artefact per B03) will repeat.
Questions: (1) does NWC fall toward 120 days with positive OCF in the
same quarter (the falsification metric already set by the gate
recommendation); (2) is the inventory build (finished goods +52%)
selling through or building toward a write-down; (3) why did the
Citibank loan get amended eight days before year-end, reducing margin and
accelerating instalments (B02 top_findings rank 15, questions_for_mgmt).

**Vertical 3 — Standalone (India-core) versus consolidated.** The corpus
establishes the split precisely: standalone revenue -29.9%, standalone
PAT -26.6%, India-geography revenue -83% to -84%, against consolidated
revenue -17.0% and consolidated PAT +7.65%, the entire swing attributable
to the US subsidiary moving from a Rs84.69mn loss to a Rs246.69mn profit
(B02 top_findings rank 1-2; AR Note 35 p.171). The corpus cannot establish
a standalone FY27 guidance number, because management has declined to
give one independent of the consolidated figure (B04 mgmt_questions).
Questions: (1) what is standalone revenue guidance for FY27; (2) is the
India-geography collapse (14% to 6% of revenue per B05 3D) a deliberate
strategic pivot away from India-domestic demand or a demand loss; (3) does
the consolidated customer-concentration improvement (69.21% to 55.71%)
survive once Altek's growth normalises, given it may be a consolidation
artefact rather than organic India-core diversification (B07 flags).

**Vertical 4 — Altek Electronics Inc.** The corpus establishes the
acquisition terms (Share Purchase Agreement, 04-Oct-2024, consideration
Rs1,537.30mn, goodwill Rs638.44mn at acquisition date per Note 32 p.169;
a further remeasured goodwill figure of Rs718.77mn appears elsewhere in
the notes per B03 monitorables, likely reflecting FX translation, not
independently reconciled by this run) and the earn-out reversal evidence
(Altek FY26 full-year profit Rs31.32mn below its roughly six-month FY25
profit of Rs39.70mn) (B02 top_findings rank 4). The corpus cannot
establish Altek's standalone P&L: management declined to disclose it
across all four concalls despite direct, repeated questioning (B05 2D
what-they-are-not-saying). Questions: (1) will there be a further
downward earn-out remeasurement; (2) is the 18-months-post-acquisition
"trial basis" cross-pollination synergy (Q4 FY26 call p.13) ever going to
convert; (3) does the US subsidiary's margin structurally lag the India
business, and by how much.

### 4b. Candidate signal table (expanded from B09 Section 6)

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| BEL (Bharat Electronics Ltd) repeat orders for Indian Navy/MoD | No repeat order within a defence budget cycle where one was expected, or a named order going to a competitor instead | Event-driven | BEL corporate announcements; MoD Press Information Bureau releases (B09) |
| India MoD modernisation programme and defence budget allocation | A Union Budget defence-electronics allocation flat or down YoY against a rising order-book claim | Event-driven (annual budget, plus any mid-year revision) | Union Budget defence allocation; MoD Annual Report; PIB (B09) |
| MeitY PLI (electronic components) / ECMS scheme disbursement | Scheme disbursement announced with no CYIENTDLM enrolment named after two further cycles | Event-driven | MeitY official notifications; PIB (B09) |
| Honeywell Aerospace order flow | No disclosed ramp progress within the 18-month window management itself gave (from Q1 FY27, per B05 4A) | Quarterly | Honeywell Aerospace 10-K/10-Q and investor disclosures on outsourcing and supply chain (B09) |
| Thales order flow | European defence-budget expansion with no matching Thales-linked order growth at CYIENTDLM | Quarterly | Thales Group financial disclosures (B09) |
| EU ReArm Europe initiative (EUR800bn) | Programme delayed, descoped, or redirected away from electronics subsystem procurement | Event-driven | European Commission and European Defence Agency publications (B09) |
| US CHIPS Act / semiconductor capital-equipment OEM customers | No named semiconductor-equipment customer or disclosed revenue line after two further quarters of "Expand"-phase promotion | Event-driven | US Department of Commerce CHIPS Program Office; semiconductor-equipment OEM investor disclosures (B09) |

All seven candidates are UNVERIFIED at this stage. Verification and
tracker writes happen at Role 5.5 in claude.ai, unchanged.

### 4c. Fragility read

- **variable_count: 6** — the variables that must go right for the
  transition case: (1) Build-to-Spec share scaling past 6% toward
  double digits; (2) NWC/cash conversion normalising toward the 100-120
  day target; (3) standalone India-core revenue and PAT stabilising or
  growing; (4) Altek delivering real (not earn-out-reversal) profit
  growth; (5) the order book converting into revenue without further
  quarterly slippage (verifier B found the bridge fails to reconcile in
  every FY26 quarter, B12b MAJOR finding); (6) the aerospace OEM ramp
  (Honeywell) landing within the stated 18-month window.
- **verifiability_ratio: "4 of 6 externally observable"** — NWC days and
  the standalone/consolidated split are AR- and filing-disclosed and
  externally checkable each period; the Honeywell/Thales ramp is
  cross-checkable against those companies' own disclosures (B09
  downstream_candidates); the order-book bridge is arithmetically
  checkable from the company's own disclosed figures. Build-to-Spec
  share (given the unreconciled 25%/6% AR conflict) and Altek's
  standalone profitability (never disclosed across four calls, B05 2D)
  are company-narrated only, with no independent third-party read
  available in this corpus.
- **single_point_failure:** Net working capital / cash conversion. The
  run's own peer cross-check (B06) already removes the "this is what
  growth costs" defence, so continued deterioration here breaks the
  re-rating case even if every other variable in the list goes right;
  it is also the item the gate recommendation names as "the single
  load-bearing item in the file."
- **fragility_verdict: FRAGILE** — six variables, a bare majority
  externally verifiable, and one of them (cash conversion) already
  carrying a STRUCTURAL determination from this run's own evidence.

### 4d. Research brief (live-web work order for claude.ai)

1. Fetch the SEBI-hosted RHP/DRHP directly (sebi.gov.in was blocked at
   this container's network egress; B08 status_reason) and extract
   pre-IPO promoter and group-company history.
2. Run the SEBI enforcement-order database name search directly for
   Cyient Limited, Krishna Bodanapu and B.V.R. Mohan Reddy (same egress
   block; B08 searches_skipped), rather than the web-search-indexed
   substitute this run used.
3. Pull the last twelve quarters of shareholding-pattern filings (BSE/NSE
   Reg 31) to get a real promoter pledge and holding trend; the corpus
   holds only two AR-anchored point-in-time snapshots (31-Mar-2025 and
   31-Mar-2026).
4. Confirm whether any rating agency covers CYIENTDLM's bank facilities
   at all; if none exists, that is itself a data point, not a gap to keep
   chasing.
5. Cross-check Honeywell Aerospace's and Thales's own investor
   disclosures for any mention of outsourcing to Cyient DLM or Altek, to
   test the "18-month ramp" and "9-20 year programme" claims from an
   independent source.
6. Ask management, in writing, to reconcile the BRSR 25% and infographic
   6% Build-to-Spec figures, and to explain the DSCR comparability break
   between the two ARs (1.67x against 0.15x for the identical FY25 year).
7. Ask management to reconcile the order-book bridge verifier B found
   failing to close in every FY26 quarter (about Rs30cr Q2, Rs26cr Q3,
   about Rs120cr full year against the claimed 1.5x book-to-bill), with
   no cancellation, de-scope or FX disclosure anywhere (B12b MAJOR).
8. Check whether Altek Electronics Inc, as a US private company, files
   anything publicly (state-level filings, UCC filings) that would give
   an independent read on its standalone financial condition.
9. Verify the gross-margin/component-cost-shock claim gap verifier B
   flagged as CRITICAL: confirm whether CYIENTDLM faced the same
   component and PCB cost shock that Kaynes and Syrma both disclosed in
   the Jan-Jun 2026 window, and why the Q1 FY27 call did not address it.
10. Confirm the India MoD order-revival lead raised once in the Q2 FY26
    call and never revisited (B05 dropped_triggers) — has it lapsed, or
    is it still live and simply undisclosed.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. Cyient DLM makes electronic parts and assemblies for machines where a
   failure cannot happen: aircraft, defence systems, medical scanners,
   industrial equipment.
2. Most of its work, 94% of FY26 revenue, is build-to-print. The
   customer designs the part. Cyient DLM builds it to spec and passes
   through most input-cost changes.
3. A small slice, 6% of FY26 revenue by the working number this run
   used, is build-to-spec. Here the company helps design the part and
   holds influence over what goes into it.
4. The buyers are aerospace, defence, medical and industrial OEMs.
   Honeywell and Thales are named anchor customers.
5. Customers cannot switch suppliers quickly. Every part is certified
   into a named programme. Requalifying a new supplier takes years.
6. That same lock-in cuts both ways. The top customers are 56% of
   consolidated revenue and 71% of standalone revenue.
7. Demand today rests on real, checkable drivers: defence budgets,
   government electronics schemes, and named aerospace customers placing
   orders.
8. Demand should grow if European defence spending and US chip-equipment
   investment keep flowing toward the company's certified niche. Neither
   is yet visible in named customer wins beyond the ones already listed.
9. All three peer companies this run checked grew revenue 27% to 46% in
   FY26. Cyient DLM's consolidated revenue fell 17%. That gap is not yet
   explained by demand alone.
10. The one real, durable advantage is the certification wall around its
    build-to-print work. It already existed before this year. It is not
    itself new or growing.
11. The build-to-spec work, where a real advantage could grow, is still
    too small to carry the business and its size is disputed inside the
    company's own annual report.
12. The core model this run holds: a certified contract manufacturer
    trying to shift a small slice of its work from spec-taker to
    spec-shaper, while its cash conversion and its India-based core
    business both go the wrong way in the same year.
13. This run's fragility read is FRAGILE. Six things must go right for
    the growth case, only about half are checkable from outside the
    company, and one of them, cash conversion, can break the case on
    its own.
14. The corpus could not establish Altek's own profit and loss, even
    though the company disclosed an earn-out reversal that implies Altek
    missed its own acquisition targets.
15. The two biggest open questions: does the company's own annual report
    tell the truth about how big its design-led business really is, and
    is its cash-conversion problem a temporary cost of growth or a
    permanent feature of the business.

---

## SECTION 6: STANDING EXTRACTION ANNEX

### 1. Units

No per-unit realisation figure (price per board, revenue per assembly,
ARPU) is printed anywhere in the AR, the investor deck, or any concall
transcript in this corpus.

> "PRODUCT-WISE REVENUE SHARE / PCBA Box Build Cable Harness Assembly
> Mech & Others / 52% 30% 2% 16%" — AR FY2025-26, p.24.

Comment: this is a basket-level revenue-share disclosure across four
product categories, not a per-unit figure. The rupee lines attached to
the two largest categories are printed alongside the percentages:

> "PRINTED CIRCUIT BOARD ASSEMBLY (PCBA) [Rs]6,551 Mn revenue ... BOX
> BUILD [Rs]3,843 Mn revenue" — AR FY2025-26, p.24.

Comment: no unit count (boards, assemblies, or programmes) is disclosed
alongside either rupee figure, so a true per-unit realisation cannot be
derived even from these two lines; only the revenue and the percentage-
of-total are available (B04 unit_economics: "revenue_per_unit: NOT
FOUND").

### 2. Segment capital and debt

The company discloses a single reportable business segment, so there is
no cross-segment capital or debt allocation to report.

> "The Company's operations fall within a single operating segment
> 'Electronic manufacturing solutions' which is considered as the primary
> reportable business segment." — AR FY2025-26, standalone Note 33, p.136.

> "The Group's operations fall within a single operating segment
> 'Electronic manufacturing solutions' which is considered as the primary
> reportable business segment." — AR FY2025-26, consolidated Note 34,
> p.171.

Comment: with a single operating segment, "segment assets, segment
liabilities, capital employed" as line items do not exist as a
disclosure category; the only sub-company split disclosed is geographic.
Geographic revenue (consolidated, Note 34, p.171) is: India Rs1,218.90mn
(FY26) against Rs7,256.92mn (FY25); NAM Rs6,866.32mn against Rs3,906.97mn;
EMEA Rs4,065.04mn against Rs3,761.77mn; APAC-ex-India Rs464.59mn against
Rs270.60mn. Geographic non-current assets (excluding financial assets and
deferred tax) are India Rs2,286.94mn and NAM Rs1,611.17mn as at
31-Mar-2026 (same note). Borrowings are not geography- or
segment-allocated; the consolidated gearing note (33.1.1, p.168) states
total borrowings of Rs1,061.25mn as at 31-Mar-2026 (Rs2,437.56mn FY25)
with no sub-split.

### 3. Guidance versus aspiration

Classified per item, all concall-sourced (results filings are ABSENT, so
no filed guidance document exists):

| Item | Class | Quote |
|---|---|---|
| Book-to-bill FY26 | (a) guidance, period stated | "1.4x-1.5x" for full-year FY26, Q2 FY26 call, 14-Oct-2025, p.5 |
| Q4 FY26 revenue growth | (a) guidance, period stated | reaffirmed "not only QoQ but YoY growth" from Q4, Q3 FY26 call, 20-Jan-2026, p.9,16 |
| FY27 revenue growth | (a) guidance, period stated, later withdrawn | "Yes, absolutely... 20-25%, no doubt" — Deepak Lalwani exchange, Q3 FY26 call p.15; then "we will not be giving any guidance" — Q4 FY26 call p.13 |
| NWC normalisation | (a) then downgraded to (b) aspiration | "expected to result in better NWC levels by end of Q4" (period-stated), Q3 FY26 call p.8; replaced by "100-120 days" over "a couple of years" (no fixed period), Q4 FY26 call p.16 |
| Build-to-Spec FY27 share | (b) aspiration, no fixed date within the year | "double-digit%", Q3 FY26 call p.16, reaffirmed Q4 FY26 call p.14 |
| Build-to-Spec margin uplift | (b) aspiration, window given but not a fixed date | "+250-300 bps consolidated EBITDA" over "next 12-18 months", Q1 FY27 call, 21-Jul-2026, p.14 |
| Regular annual capex | (c) capacity/capability statement | "1%-2% of revenue", ongoing, Q3 FY26 call p.13 |
| Order pipeline size | (b) aspiration/estimate, inconsistent across quarters | "$0.5 billion", Q4 FY26 call p.15; disputed as "substantially higher" with no number, Q1 FY27 call p.13-14 |
| Aerospace OEM ramp (Honeywell) | (a) guidance, window stated | "ramp-up within 18 months" from Q1 FY27, Q1 FY27 call p.17-18 |
| BTS anchor customers, revenue timing | (a) guidance, period stated | "meaningful contribution from FY28 onwards", Q3 FY26 call p.6, reconfirmed "flag end of FY27 and also FY28 both", Q4 FY26 call p.14 |

(All rows sourced from B05 guidance table and promise_delivery rows,
cross-checked against the concall transcripts named.)

### 4. Concentration

Product concentration: not separately disclosed by product-line
customer; only the aggregate top-customer figures below exist.

Customer concentration (both statements, Note 20 standalone / Note 34
consolidated, AR FY2025-26 p.136/171):

> "Revenue from top customers (*) 6,649.93 [Rs mn] 70.54% [FY26] ...
> 10,516.72 [Rs mn] 78.19% [FY25]" — standalone, p.136.

> "Revenue from top customers (*) 7,027.51 [Rs mn] 55.71% [FY26] ...
> 10,516.72 [Rs mn] 69.21% [FY25]" — consolidated, p.171.

Comment: both figures are for customers individually at or above 10% of
revenue, aggregated (B02 top_findings rank 9). The consolidated figure
improved faster than the standalone figure, which B07 flags as
substantially an Altek-consolidation artefact rather than organic
India-core diversification.

Geography concentration: see Section 6.2 above (geographic revenue
table, Note 34 p.171). Export/rest-of-world share rose from about 85%
(Q2 FY26 call p.7) to about 94% (Q1 FY27 call p.9) of revenue; India fell
from about 14% to about 6% over the same four quarters (B05 3D).

Top product share: PCBA is the largest single product category at 52% of
FY26 revenue (AR p.24, Section 6.1 above); no further product-level
customer concentration is disclosed.

### 5. Promise ledger

| Promise | Date made | Delivery status | Evidence anchor |
|---|---|---|---|
| Book-to-bill 1.4x-1.5x for FY26 | Q2 FY26 call, 14-Oct-2025, p.5 | DELIVERED — full-year book-to-bill 1.5x confirmed | Q4 FY26 call, 21-Apr-2026, p.3 |
| Q4 FY26 revenue returns to positive YoY growth | Q2 FY26 call p.5-6, reaffirmed Q3 FY26 call p.9,16 | MISSED — Q4 FY26 revenue down 13.8% YoY | Q4 FY26 call p.6-7 |
| NWC to normalise by end of Q4 FY26 | Q3 FY26 call, 20-Jan-2026, p.8 | MISSED — FY26 NWC 145 days, worse than FY25's 127 days; promise itself replaced by a vaguer target | AR FY2025-26 p.27; Q4 FY26 call p.16 |
| FY27 revenue growth of 20-25%, "no doubt" | Q3 FY26 call p.15 | PARTIAL — Q1 FY27 actual +34.3% YoY beat the range, but the specific number was withdrawn under questioning twice | Q4 FY26 call p.13; Q1 FY27 call p.11 |
| Q4 FY26 order intake rebounds to about Rs500cr/quarter | Q3 FY26 call p.14 | MISSED (derived) — implied gross Q4 intake near Rs430-440cr, still close to Q3's depressed level | Q4 FY26 call p.6 (net order-book addition INR672mn against Q4 revenue ~Rs369cr) |
| Altek contribution "healthy and profitable" | Q3 FY26 call p.9 | PARTIAL — Q4 FY26 call admits US/Altek margin is structurally lower; no hard Altek P&L ever disclosed | Q4 FY26 call p.13 |
| Order pipeline approximately $0.5 billion | Q4 FY26 call p.15 | PARTIAL/inconsistent — disputed the next quarter with no replacement figure | Q1 FY27 call p.13-14 |
| 4 BTS anchor customers, revenue within 2 years, meaningful from FY28 | Q3 FY26 call p.6 | DELIVERED (on-track, unchanged) | Q4 FY26 call p.14 |

(B05 promise_delivery; totals: 2 delivered, 3 partial, 3 missed;
credibility grade C per B05, which verifier B would grade C-minus to D,
B12b credibility_grade_concur.)

### 6. Restated bases

No restatement of prior-period financial-statement comparatives was
found in AR FY2025-26. The only "restated" language located in the
document concerns non-financial BRSR data points (water-stress-area
reporting and RBI-classification-driven location reclassification for
environmental metrics), not the financial statements:

> "The water footprint from water stress areas for FY 2024-25 have been
> restated due to reconciliation of withdrawal locations..." — AR
> FY2025-26, BRSR section, p.[BRSR environmental table].

> "The numbers for FY 2024-25 have been restated owing to reclassification
> of locations in alignment with RBI's classification." — AR FY2025-26,
> BRSR section.

Comment: these are environmental/CSR-location reclassifications, not
financial restatements. B02's triple-pass review of both years' notes
found no financial-statement restatement disclosure (B02
restatements_found: []). The only cross-report comparability break found
in the corpus concerns DSCR, which is a disclosure-method inconsistency
across two separate ARs, not a restatement within one AR (see Section 6.10
adjudication note below; B12a adjudication 1).

### 7. Corporate-action clauses

One corporate action sits in the corpus: the Altek Electronics Inc
acquisition. No scheme, demerger, or preferential issue is in the corpus.

> "On October 04, 2024, the Company through it's wholly owned subsidiary
> Cyient DLM Inc., USA entered into Share Purchase Agreement with
> Altschuler Holdings, Inc. and acquired 100% of the shares of Altek
> Electronics Inc, USA ('Altek')... for a consideration of [Rs]1,537.30
> [mn], consisting of an upfront cash payment of [Rs]1,184.48 [mn] (post
> working capital adjustments) and performance based contingent payments
> of [Rs]352.82 [mn]." — AR FY2025-26, consolidated Note 32, p.169.

> "Altek became a subsidiary of Cyient DLM Inc., USA effective October 04,
> 2024 on satisfactory completion of the closing conditions under the SPA
> and has been consolidated with effect from that date." — AR FY2025-26,
> p.169-170.

> "The fair value of net assets acquired (including intangible assets) as
> of the acquisition date amounted to [Rs]898.86 [mn] (total assets of
> [Rs]2,322.88 [mn] & total liabilities of [Rs]1424.02 [mn])... The
> goodwill, amounting to [Rs]638.44 [mn] is attributable to the assembled
> workforce and the expected future profitability of the acquired
> business... not deductible for tax purposes." — AR FY2025-26, p.170.

> "The fair value of the contingent consideration, recognised on the
> acquisition date is determined by discounting the estimated amount
> payable to the previous owners on achievement of certain financial
> targets applying the discounted cash flow approach. The key inputs used
> for the estimation of fair values are discount rate of 13.9% and
> probabilities of achievement of financial targets." — AR FY2025-26,
> p.170.

Comment: the appointed/effective date is 04-Oct-2024 in both cases (no
separate appointed-versus-effective-date gap, unlike a court-scheme
transaction). No liability-allocation clause beyond the standard SPA
indemnity structure is disclosed; the contingent-consideration mechanism
is the load-bearing clause, and it has already been remeasured downward
once (B02/B03; the fair-value liability moved from Rs352.82mn to
Rs179.89mn per the fair-value-measurement table, p.[33.1.2], reflecting
Altek's underperformance against its earn-out targets). No RHP/DRHP or
Reg 30 filing exists in the corpus to cross-check this against a
contemporaneous exchange announcement; the AR is the only source.

### 8. Related-party perimeter

Every promoter-group entity named in the AR's RPT note (Note 30,
consolidated, AR FY2025-26 p.169), with FY26 transaction nature and
amount:

| Party | Relationship | Nature of transaction | FY26 amount (Rs mn) | FY25 amount (Rs mn) |
|---|---|---|---|---|
| Cyient Limited | Ultimate holding company | Sub-contracting charges | 537.56 | Nil |
| Cyient Limited | Ultimate holding company | Revenue from operations | 15.03 | 4.57 |
| Cyient Limited | Ultimate holding company | Reimbursement of expenses (net) | 33.77 | 27.07 |
| Cyient Limited | Ultimate holding company | Financial guarantee closure | 4,470.00 | Nil |
| Cyient Limited | Ultimate holding company | Term loan repaid | 746.72 | 248.91 |
| Cyient Limited | Ultimate holding company | Interest on loans | 14.43 | 74.93 |
| Cyient Limited | Ultimate holding company | Working capital loan repaid | Nil | 340.00 |
| Cyient Limited | Ultimate holding company | Services availed | Nil | 62.40 |
| Cyient Limited | Ultimate holding company | Share-based payment expenses | 2.86 | 2.41 |
| Cyient Limited | Ultimate holding company | Trade payable (year-end balance) | 442.12 | 123.73 |
| Cyient Limited | Ultimate holding company | Advance from customer (balance) | 7.20 | 7.20 |
| Cyient Inc. | Fellow subsidiary | Revenue from operations | 39.27 | Nil |
| Cyient Inc. | Fellow subsidiary | Trade payable (year-end balance) | 92.81 | 351.17 |
| Cyient Inc. | Fellow subsidiary | Trade receivable (year-end balance) | 9.62 | 44.62 |
| Cyient GmbH | Fellow subsidiary | Revenue from operations | 63.47 | Nil |
| Cyient GmbH | Fellow subsidiary | Trade payable (year-end balance) | 17.53 | 33.05 |
| Cyient Israel India Limited | Fellow subsidiary | Trade payable (year-end balance) | 48.90 | 45.40 |
| Cyient Europe Limited | Fellow subsidiary | Trade payable (year-end balance) | Nil | 34.87 |
| Cyient Singapore Pte Limited | Fellow subsidiary | Trade payable (year-end balance) | Nil | 31.83 |
| Cyient Schweiz GmbH | Fellow subsidiary | Trade payable (year-end balance) | Nil | 18.24 |
| Cyient K.K | Fellow subsidiary | Reimbursement of expenses | 0.57 | 0.34 |
| Cyient Foundation | Entity with common KMP | CSR expenditure | 16.14 | 11.66 |
| Key Managerial Personnel (all named individually in Note 30(i)) | KMP | Short-term benefits, share-based payment, commission | 131.62 + 5.54 + 7.40 combined FY26 | 111.15 + 66.77 + 6.00 combined FY25 |

(AR FY2025-26, consolidated Note 30, p.164-166; standalone Note 30
p.132-134 carries an equivalent standalone-only table.) The AR states:

> "The Group's related party transactions during the year ended March 31,
> 2026 and March 31, 2025 and outstanding balances as at March 31, 2026
> and March 31, 2025 are with its ultimate holding company and fellow
> subsidiaries with whom the Group generally enters into transactions
> which are at arms length and in the ordinary course of business." — AR
> FY2025-26, p.166.

Comment: this is boilerplate arm's-length assertion with no supporting
benchmarking study disclosed for the new Rs537.56mn sub-contracting flow
that appeared from nil in FY26 (B02 top_findings rank 6; B03
flags/missing_risks). The two most senior Cyient Limited executives,
B.V.R. Mohan Reddy and Krishna Bodanapu, sit on the Cyient DLM board as
Non-Executive, Non-Independent Directors (Note 30(i), p.164-165) and
oversee, via the Audit Committee, the same related-party flow.

### 9. Pledge and shareholding

No promoter-pledge percentage figure is disclosed anywhere in the AR
FY2025-26 text located by this run; the AR's corporate governance section
carries only the ownership-category and over-1%-holder tables reproduced
below. Promoter pledge information in this run came from B08's web
search, a weaker, non-filing-anchored tier (media-reported):

> "Zero promoter pledge maintained per FY26 Reg 31(4) SAST compliance
> filing" — B08 transition_evidence, evidence_tier "MEDIA REPORTED",
> source ScanX/Whalesbook/Trendlyne, accessed 2026-09-06. NOT a
> filing-anchored figure in this corpus.

Shareholding, as filed in the AR corporate governance section (this run
holds two point-in-time snapshots, not twelve quarters; no quarterly
shareholding-pattern filing is in the corpus):

> "Distribution of Shareholding on the basis of ownership as on March 31,
> 2026 ... Promoters 1 [holder] 4,13,66,502 [shares] 52.1222[%]" — AR
> FY2025-26, p.100.

> "Shareholders of the Company, having more than 1% shareholding as on
> March 31, 2026 / CYIENT LIMITED Promoter 4,13,66,502 52.12[%] / HDFC
> MUTUAL FUND - HDFC DEFENCE FUND Mutual Fund 55,10,876 6.943[%]" — AR
> FY2025-26, p.101.

> "Distribution of Shareholding on the basis of ownership as on 31 March,
> 2025 ... Promoters 1 [holder] 4,13,66,502 [shares] 52.16[%]" — AR
> FY2024-25, p.150.

Comment: the promoter's absolute share count (4,13,66,502) is identical
across both year-ends; the percentage moved from 52.16% to 52.1222% purely
because total shares outstanding rose slightly (ESOP/RSU exercises), not
because the promoter sold or bought. Institutional holding at 31-Mar-2026:
Mutual Funds 26.0538% (26,77,439... row total 2,06,77,439 shares),
Foreign Portfolio-Corp 0.7938%, Qualified Institutional Buyer 0.1471% (AR
p.100). No twelve-quarter trend and no encumbrance/pledge disclosure
exists in this corpus; this is the gap named in Section 1 above.

### 10. Verification

Every document quoted in this annex:

- Annual_Report_2026.pdf (AR FY2025-26, year ended 31-Mar-2026, 174pp),
  cited at pp.24, 62-63, 100-101, 132-134, 136, 144, 164-171.
- Annual_Report_2025.pdf (AR FY2024-25, 287pp), cited at p.150.
- Concall_Oct_2025_Transcript.pdf (Q2 FY26, 14-Oct-2025), cited at
  pp.5-8.
- Concall_Jan_2026_Transcript.pdf (Q3 FY26, 20-Jan-2026), cited at
  pp.6,8-9,14-16.
- Concall_Apr_2026_Transcript.pdf (Q4 FY26/FY26 full year, 21-Apr-2026),
  cited at pp.3,6-7,9,13-16.
- Concall_Jul_2026_Transcript.pdf (Q1 FY27, 21-Jul-2026), cited at
  pp.6-7,9,11,13-14,17-18.

CORPUS COMMIT HASH: 325c97abbbbbf9d13da4b97ac332767b5c2b2edf
