# HALT 1 UNDERSTANDING DOSSIER — Insolation Energy Ltd (INA Solar)

Ticker: INA (NSE) / 543620 (BSE). CIN L40104RJ2015PLC048445. Run: ina-2026-09-06.
CMP Rs 90.24, market cap Rs 1,989.36cr. Phase 1 only (stages 0-9 plus verifiers A-D).
No valuation has run. This is an UNDERSTANDING document. It carries no price, no
exit multiple, no fair value, and no verdict-set language. The kill or proceed
decision belongs to the operator, made after reading this.

---

# SECTION 1: CORPUS COMPLETENESS AUDIT

## 1. Concalls

Three company transcripts held: Concall_Jun_2025 (FY25 results call), Concall_Feb_2026
(Q3 FY26 call), Concall_Jun_2026 (FY26 results call) (B00, B05). The most recent
quarter covered by any call is Q4 FY26 (call dated 27-May-2026). Given the run date
of 2026-09-06, a more recent quarter has plausibly reported: screener-Data_Sheet.csv
carries a Q1FY27 print (quarter ended 30-Jun-2026, sales Rs 740.70cr, net profit
Rs 37.04cr) whose filing and concall are both ABSENT from the corpus (B00, B05 flags).

Eleven of eleven listed peer transcripts are close to complete: Waaree (4: Jan-2026,
Feb-2026 special call, May-2026, Aug-2026), Premier Energies (4: Nov-2025, Jan-2026,
May-2026, Aug-2026), Websol Solar (3: Feb-2026, May-2026, Aug-2026; no Nov-2025 call
held) (B00 gap `peer-concalls-partial`, LOW).

## 2. Annual reports

One annual report held: FY2026 (year ended 31-Mar-2026) (B00 corpus_inventory).
This IS the latest completed FY. Fewer than 3 years are held; the run has only one
AR, so no independently-filed FY2022-2025 annual reports exist in the corpus. The
backward five-year series in Gate 0 survives only via screener-Data_Sheet.csv and
the FY2026 AR's own restated comparatives (B01 data_notes).

## 3. Results filings

ZERO quarterly results PDFs are held (B00 gap `results`, HIGH). The latest filing
evidenced anywhere in the corpus is the FY2026 annual results embedded in the AR
itself (year ended 31-Mar-2026). The quarter-gap between that and the most recent
quarter plausibly reported (Q1FY27, quarter ended 30-Jun-2026) is one full quarter,
and it is the corpus's single largest gap (B00 analyst_note).

## 4. Investor presentations

One presentation held, dated Jul-2026 per its own slide 25 order-book table (B03
catalysts_12m; B07 catalysts_12m). No later presentation is held.

## 5. Research / rating

ZERO research notes and ZERO rating rationale PDFs are held (B00 gaps `research`
LOW, `rating` MEDIUM). No broker note, no CARE/CRISIL/ICRA/India Ratings rationale
for the FY2026 borrowing step-up from Rs 108cr to Rs 888cr (B00).

## 6. Corporate actions

One announcement file is held: a 2-page Reg 30 AR-weblink letter dated 2026-09-04
with no material-event content (B00 gap `announcements-thin`, MEDIUM). No order,
JV, capex, or capital-raise announcement filings are held despite the FY2026 AR
itself disclosing a Dec-2024 preferential issue (Rs 395.196cr, Note 15(e), AR p.123)
and Rs 901.43cr of FY2026 capital commitments (Note 42(b), AR p.138). The
documented-ACTION record is effectively absent (B00 analyst_note).

## 7. Freshness pair check

B00.freshness_verdict is CORPUS GAPPED-FRESHNESS. Of the four defined pairs:
- **results-to-concall: FAIL.** Trigger document: the Q1FY27 print (QE 30-Jun-2026,
  sales Rs 740.70cr, PAT Rs 37.04cr), evidenced in screener-Data_Sheet.csv, against
  Q4FY26 sales Rs 793.93cr, PAT Rs 70.07cr. Mate absent: the Q1FY27 results filing
  and its earnings-call transcript, both missing from the corpus.
- rating-bulletin-to-rationale: N/A, no rating bulletin exists anywhere.
- sebi-order-to-order-text: N/A, no SEBI order referenced anywhere.
- ar-to-latest-audited-annual: PASS, the FY2026 AR is the latest audited annual and
  is held.

## 8. Verdict line

**CORPUS GAPPED-FRESHNESS.**

Missing mate document (named first, per the freshness-pair precedence rule): the
Q1FY27 results filing (quarter ended 30-Jun-2026) and its earnings-call transcript.
Expected source: BSE and NSE corporate filings for Insolation Energy Ltd, or the
company investor relations page.

Other gaps, findable-but-missing (operator upload list):
- Prospectus (HIGH). IPO FY2022-23 on BSE SME; main-board listing 09-Mar-2026.
  Pre-IPO restated financials and full promoter/group map unavailable elsewhere.
  Expected source: BSE SME prospectus archive / company IR page.
- Any credit rating rationale (MEDIUM). No rationale for the FY2026 borrowing
  step-up. Expected source: CARE / CRISIL / ICRA / India Ratings.
- Shareholding pattern filing (MEDIUM). FII+DII split and pledge trend both
  unresolved; falls back to AR, which itself carries no pledge disclosure or NIL
  statement. Expected source: BSE/NSE quarterly shareholding-pattern filing.
- Research/broker notes (LOW). Non-anchored source category; no effect on evidence.
  Expected source: broker research if any exists.
- Screening companion CSVs (MEDIUM). Profit_Loss/Balance_Sheet/Cash_Flow/Quarters
  CSVs are header-only shells for the subject and all three peers; only
  Data_Sheet.csv is populated. Known collector defect, findable by re-running the
  collector, not a company-side gap.

Plausibly-nonexistent (a data point in its own right):
- Corporate-action filings beyond the one thin Reg 30 letter. The company appears
  not to file granular order/capex announcements in a form that reached this
  corpus; this is itself a disclosure-thinness signal, not merely an upload gap.

Also carried: the AR's own omission of the Notes 1-3 Material Accounting Policies
text (HIGH). Both consolidated and standalone balance sheets, and the audit report,
cross-reference Notes 1-3, but the text is absent from the entire 200-page
extraction. Verified by two independent extractors; no image-only pages found
(B00 gap `annual-report-notes-1-3-absent`; B02 top_findings rank 12). Revenue
recognition policy, ECL methodology, inventory valuation, and depreciation policy
are all unreadable as a direct result.

This verdict takes precedence over a plain CORPUS GAPPED and caps the phase-1 gate
recommendation at PROCEED WITH CAVEATS per the orchestrator (B00 flag FLAG-FRESHNESS).

---

# SECTION 2: MENTAL MODEL DECLARATION

**DRAFT - PENDING OPERATOR SIGN-OFF.** Nothing below is signed. Signing happens only
in claude.ai after live-web stress-testing.

## PART A — THE FROM STATE (the anchor, not the model)

**A1. Archetype.** Two lines, treated separately per CLAUDE.md ARCHETYPE LIBRARY:

- Module manufacturing and trading line (98.9% of FY2026 revenue: 81.9%
  own-manufactured Finished Goods + 17.0% Trading Sales; B04): **Commodity
  converter**, close cousin to a build-to-spec component maker, but the framework's
  own converter classification fits best. Raw material (bought-in cells, wafers,
  aluminium frames) runs about 78% of revenue, pricing_power is scored "weak" (B04),
  and the moat scan finds no differentiated design-win or spec-in relationship, only
  ALMM/BIS/IEC certification as an entry gate rather than a premium (B04 valuation
  notes).
- Sale-of-electricity (IPP/PM-KUSUM) line (0.2% of FY2026 revenue; B04): **Licence /
  scarcity business**, the archetype fitting a PM-KUSUM allotment held under a state
  tender. Currently a shell of a business line: Rs 4.22cr of revenue against a
  guided 400MW capacity build and roughly 38-40MW commissioned by the Q4 FY26 call
  (B03 monitorables; B04).

**A2. The simple analogy.** Insolation Energy buys most of the costly ingredient
that goes into a solar panel, the cell, from other companies, then assembles,
tests, and sells the finished panel under its own brand to government-linked solar
projects and to a dealer network. It also resells some panels it did not make at
all. That is the whole business today: an assembler and a reseller, not a maker of
the ingredient. A side venture owns and runs a handful of small solar farms of its
own and sells the power, but that venture is barely earning money yet.

## PART B — THE TRANSITION (the model)

**B1. FROM to TO (quality-tier migration, CLAUDE.md QUALITY LADDER).**

| Line | FROM | TO |
|---|---|---|
| Module manufacturing/trading | R1 COMMODITY PRICE-TAKER (no pricing power; ROCE 19% FY26 down from a claimed 60% FY25 on the CFO's own restated figures; B12b M7-M8; margins commodity-linked, B04 pricing_power "weak") | R2 COST-ADVANTAGED CONVERTER (the claimed destination once cell/wafer backward integration lands and margin is meant to move from durable-mid-teens toward the 20%+ range CFO guides; B05 guidance_table) |
| IPP/KUSUM | R0 NON-OPERATING / pre-operating (0.2% of revenue, no established operating economics yet; B04) | R1 COMMODITY PRICE-TAKER at best (a tariff-taking power seller under a government scheme, no evidence yet of a differentiated economics; the stated 400MW capacity build, if it materialises, still sells at a regulated PPA tariff) |

**B2. The engine.** One thing physically changes for the primary line: backward
integration into cell manufacture (a 4.5GW TOPCon line at Narmadapuram, funded
inside Rs 901.43cr of capital commitments, under construction; B03 guidance_table).
The stated mechanism is that owning the cell removes a bought-in cost that is
~78% of revenue and lifts EBITDA margin by 400-500bps toward 20% (B05 guidance
item "Cell EBITDA impact"). Wafer/ingot integration is a second, less advanced leg
(DPR in progress, no technology partner named; B07 optionality_register).

**B3. The proof gate.** The hard binary observation: the Narmadapuram cell line
reaches commercial production on a date that holds, and group EBITDA margin moves
visibly toward the 20%+ range in the two to three quarters after commissioning,
without the corresponding PAT margin falling on a like-for-like basis (guarding
against the guidance-basis switch already found, B12b C3). Until commercial cell
output shows up as a segment-visible or at least revenue-disaggregation-visible
line, the shift is narrative. The gate has not fired: the corpus carries three
inconsistent COD dates for the same facility (Q3 FY27, Q4 FY27, December 2026, two
of them stated within the same call; B07 top_moat_risks; B12a/B12b corroborate).

**B4. The recognition gap — OPEN QUESTION (to be resolved at Stage 11).** Whether
the market's current pricing of INA already reflects the claimed cell-integration
margin uplift, or whether that uplift is still unpriced, is not addressed by this
phase. Stage 11 resolves this via the Section 1B PE gap. No number, no fair value,
no conclusion is stated here.

**B5. The ugliness test.** Today's ugly optic is the FY2026 cash-conversion
inversion: PAT rose 59% to Rs 200.63cr while consolidated operating cash flow went
to minus Rs 73.13cr, working capital days rose from 31.48 to 62.58, and receivables
aged beyond six months rose from 5.7% to 12.1% to 39.5% of a 2.56x-larger book
(B01, B02, B03). Classification: **INDETERMINATE, leaning toward evidence that
could support either read, not yet resolved** (matching the run's own FLAG-CASH
determination). Arguments for ARTIFACT-OF-CLIMB: capacity genuinely scaled in the
same year (5.5GW module capacity delivered), capex tracks capital commitments
cleanly, and the ageing sits entirely at the subsidiary while the parent's own book
stayed near 6% (B03 strengths_top3). Arguments for STRUCTURAL-FEATURE: a working
capital ramp should add current receivables, not age an existing book; ageing
nearly tripled in one year against zero ECL provision in every bucket and every
year; and the peer comparator using the same letter-of-credit mechanism (Websol)
converted 84% of PAT to cash in the same year INA converted none (B06 Q7, decisive
per B06.analyst_note). This is not resolved in this document; it is the run's
single largest open finding and its own falsification metric is named in Section 4.

**B6. The transition falsifier.** The Narmadapuram cell line fails to reach
commercial production within a further 12 months of any of its three stated dates,
OR it reaches production but group EBITDA margin does not move toward the guided
range within two to three quarters, OR the margin uplift arrives only via a PAT-to-
EBITDA guidance-basis change that conceals no real PAT improvement (the switch
already found once; B12b C3). Any of these three kills the transition thesis
specifically, independent of whether the base module/trading business survives.

## PART C — WHAT THE MODEL WATCHES (derived from the transition)

**C1. Dominant variables**, derived from B2 (the engine) and B3 (the proof gate):

1. **Narmadapuram 4.5GW cell line COD and post-COD margin trajectory.** Current
   state: under construction, three internally inconsistent guided dates, no
   commercial output yet (B07 top_moat_risks).
2. **Consolidated CFO/PAT and CFO/EBITDA ratios, and receivables aged beyond six
   months.** Current state: CFO/PAT -36.5%, CFO/EBITDA -24.0%, aged-receivables
   share 39.5% (B01, B02).
3. **Usable cell/module capacity as a share of nameplate.** Current state:
   internally contested even within the company (CFO states 50-55% of nameplate is
   the norm; the company's own reported output implies 84-89%; peers report
   70-92%) (B12b C2, M9).
4. **DCR cell-supply dependency (Emvee/Premier tie-up) and the ALMM Part 2/ALCM
   enforcement date.** Current state: DCR is roughly 15% of INA volume but carries
   the entire price premium; the governing date has already moved once in peer
   calls dated after INA's own corpus closes (June 2026 to December 2026), and
   Premier states it will keep fewer cells for external sale as its own line ramps
   (B12b C7; B06 Q5).

**C2. What the model rejects.** Total addressable market size is not a binding
constraint and is declared noise here: the Indian module TAM (Rs 110,880cr to
Rs 128,120cr, 16% growth) gives 36.7x revenue headroom against INA's current SAM
share of 2.7% (B09, runway_class MASSIVE). The binding constraints are execution
(a COD date that has moved three times) and cash conversion, not market size.
Equally rejected as noise at this stage: the BESS-assembly and US-export
optionality lines, both long-dated, low-conviction, and unchanged in status across
all three calls (B05 triggers priority 8-9; B07 optionality_register).

**C3. The business falsifier**, distinct from B6. Evidence that would force
re-declaring the FROM business itself (not merely the transition): the
module/trading engine's own cash-conversion problem proves structural rather than
a one-year ramp (receivables aged beyond six months continuing past the FY26 level
of 39.5% into FY2027, with the parent's own book also beginning to deteriorate from
its current ~6% level), combined with the corporate guarantee structure (Rs
1,654.01cr, 205% of consolidated net worth, 3.0x the parent's own standalone
assets; B02, B03) crystallising against the listed parent. That combination would
mean the FROM-state business itself, not merely its claimed climb, has a
going-concern-adjacent capital structure problem. Separately, credibility grade D
on eleven tracked promises (one delivered, five partial, five to eight missed;
B05, B12b) is a business-quality falsifier candidate in its own right if it recurs
against the cell-line COD specifically.

---

# SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

Per prompts/13-synthesis-pipeline.md BUSINESS UNDERSTANDING NARRATIVE (the shared
five-question spec, not restated here). Drafted from B01-B09 for Halt 1; stage 13's
copy is the final version.

Insolation Energy makes solar photovoltaic modules, the flat panels that turn
sunlight into direct current electricity. Own-manufactured modules were 81.9
percent of FY2026 revenue, bought-and-resold goods booked as trading sales were
17.0 percent, sale of electricity from the company's own plants was 0.2 percent,
and other operational income was 0.5 percent (B04). Only two streams clear ten
percent of sales, so this is a module maker with a trading desk attached. A buyer
building a solar plant cannot skip the panel, but can buy the same panel from
about ten other listed Indian makers (B01 M7 data). What the buyer cannot
substitute is a panel on the government ALMM approved list, because
scheme-linked projects accept nothing else.

Customers fall into three classes: government scheme developers, EPC contractors
who build plants for them, and a dealer channel. One customer is named in the
accounts, Solarworld Energy Solutions Ltd, at 12.4 percent of FY2026 revenue and
nil the year before (B02, Note 46 p.144-145). The dealer channel is shrinking:
dealer count fell from 93 to 82 and dealer-channel sales fell from 12.44 percent
to 11.61 percent of total sales in one year (B07 FLAG-EMOAT-DEALER-DECLINE).
Qualification runs through the ALMM list, not through the maker, so a customer
can switch supplier without requalifying anything. Peers say orders turn firm
only against advances of 5 to 15 percent of value, while INA says it moved
customers to 45-day letter-of-credit terms (B06).

Demand today comes from government procurement, and three named signals size it:
SECI and NTPC solar tender awards and cancellations, PM-KUSUM state nodal agency
tender and PPA awards, and MNRE ALMM List I and List II updates and effective-date
notifications (B09 downstream_candidates). Each of the three is published outside
the company, so the demand driver is verifiable without management (B09
demand_externally_verifiable: true).

Demand should grow because the Indian module market is Rs 110,880 crore to
Rs 128,120 crore and is growing about 16 percent a year, against INA's 2.7
percent share of the serviceable slice (B09). The growth is not uniform. Peers
state that DCR demand under government schemes is tight while non-DCR module
demand is oversupplied and unprofitable (B06 industry_cross_read), so the forward
signals that matter are the module and cell ASP benchmark trackers, the silver
and polysilicon commodity price indices, and the US anti-dumping and
countervailing-duty rulings on Indian solar imports, all published monthly or on
event (B09 downstream_candidates).

Competitive advantage sits in one place and is not yet built. The module line has
no moat: the emerging moat scan scored 9 of 92 against a 12-point floor and
classified NONE (B07 em_score, em_classification), R&D spend was 0.00 percent of
total R&D plus capex, and exports were NIL percent of turnover (B07 FLAG-EMOAT-RD-
ZERO, FLAG-EMOAT-EXPORTS-ZERO). The trading line has no moat and is stated plainly
as resale. The IPP line holds a licence-like position through PM-KUSUM allotments
but produced Rs 4.22cr of revenue, so the run did not establish its economics
(B04). Only two forward categories scored active in the moat scan: backward
integration into cells, which has real capital behind it and a line under
construction, and the ALMM regulatory tailwind, which management itself says is
shared equally with Waaree, Premier Energies and Websol (B07 active_categories).

---

# SECTION 4: DOWNSTREAM DOSSIER

## a. Verticals framed (per dominant variable, Section 2 C1)

**Vertical 1 — Cell-line commissioning and post-COD margin.** The corpus
establishes: the facility exists, has drawn IREDA financing, and sits inside
Rs 901.43cr of capital commitments (B01 data_notes; B03 guidance_table). It cannot
establish: which of three stated COD dates governs, or whether post-COD margin
will move on a PAT basis rather than only an EBITDA basis (B12b C3, C6).
Deciding questions: (1) Does the facility report first commercial production on
an exchange filing, and on which date? (2) Does the group's PAT margin, not only
EBITDA margin, move in the two quarters after that filing? (3) Does management
name a technology partner and firm capex figure for the wafer/ingot leg, or does
it stay "under evaluation"?

**Vertical 2 — Cash conversion and receivables ageing.** The corpus establishes:
the FY2026 numbers precisely (CFO -Rs73.13cr, aged share 39.5%, zero ECL; B02).
It cannot establish: whether this is a one-year ramp or a structural revenue-
quality problem, because the ECL methodology (Notes 1-3) is missing from the AR
and one further quarter of post-FY26 data (Q1FY27) is absent from the corpus
(B00, B02.analyst_note). Deciding questions: (1) What does the trade receivables
ageing note in the next filed quarter or annual report show? (2) Does the
parent's own standalone book, currently ~6% aged, begin to deteriorate? (3) Does
the company or its auditor ever publish the ECL methodology it currently omits?

**Vertical 3 — Usable capacity versus nameplate.** The corpus establishes: at
least three different percentages stated by INA's own management in a single
call (50-55% CFO norm, 84-89% implied by reported output, "not more than 70%"
Chairman) (B12b M9). It cannot establish which governs, because no independent
capacity-utilisation disclosure exists. Deciding questions: (1) Does a future
quarter disclose actual production volume against nameplate capacity in a way
that resolves the three figures? (2) Do peer disclosures (Waaree 70-75%, Websol
70-75%/81% achieved, Premier 75-80% module/~90% cell; B12b C2) remain the best
available yardstick, or does INA ever publish its own?

**Vertical 4 — DCR cell-supply dependency and the ALMM/ALCM date.** The corpus
establishes: DCR is roughly 15% of INA's volume but carries the full price
premium, and the governing enforcement date has already moved once, in peer
calls dated after INA's own corpus closes (B06 Q5, flags). It cannot establish
whether Premier will continue to supply INA's DCR cell needs once Premier's own
cell line ramps and Premier states it will keep more cells for internal use
(B12b C7). Deciding questions: (1) Does INA name an alternate DCR cell supplier
or its own DCR-capable output? (2) What does the December 2026 ALMM-2 deferral,
found in peer calls, do to INA's own margin-bridge timeline? (3) Does MNRE
confirm or further defer the date?

## b. Candidate signal table

Expanded from B09.downstream_candidates[] (7 signals).

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| SECI/NTPC solar tender awards and cancellations | A sustained run of cancelled or undersubscribed tenders in INA's addressable segment | Event-Driven | SECI/NTPC e-tender portals, PIB press releases |
| MNRE ALMM List I/II updates and effective-date notifications | A further deferral beyond December 2026, or removal of INA from the list | Event-Driven | MNRE circulars, mnre.gov.in ALMM portal |
| PM-KUSUM state nodal agency tender/PPA awards | Commissioning pace stays near the ~38-40MW level for multiple further quarters against the stated 400MW capacity build | Quarterly | State nodal agency press releases / MNRE PM-KUSUM dashboard |
| Module/cell ASP benchmark trackers (DCR vs non-DCR, Rs/watt) | INA's realised ASP diverges materially (adversely) from the tracked benchmark for two consecutive quarters | Monthly | Mercom India / JMK Research monthly price bulletins |
| Silver and polysilicon commodity price indices | A sustained input-cost spike with no corresponding INA price pass-through disclosed | Monthly | LME/commodity exchange data, trade press |
| US anti-dumping/countervailing duty rulings on Indian solar imports | A ruling that reopens the US export channel and redirects non-DCR volume, easing domestic oversupply pressure (or the reverse) | Event-Driven | US Department of Commerce / USITC filings |
| Solarworld Energy Solutions Ltd order flow and receivables signals | Any disclosed deterioration in Solarworld's own financial health, or a sharp decline in its order flow to INA | Quarterly | Solarworld's own exchange filings if listed, else MCA filings |

## c. Fragility read

- **variable_count:** 4 (the C1 dominant variables: cell-line COD/margin,
  cash-conversion/ageing, usable-capacity basis, DCR cell-supply/ALMM date).
- **verifiability_ratio:** 2 of 4 externally observable (ALMM/ALCM date via MNRE
  circulars; DCR cell-supply dynamics partly via peer, i.e. Premier's own,
  disclosures). The other 2 (cell-line COD and its margin effect; cash conversion
  and receivables ageing) are currently observable only through company-filed
  numbers, i.e. company-narrated in the sense that no independent counterparty
  discloses them, though the receivables ageing note itself is an audited,
  filing-anchored figure once filed.
- **single_point_failure:** none - failure requires conjunction. No single
  variable alone kills the thesis in this run's own evidence: even a further
  cell-line COD slip does not by itself resolve the cash-conversion question, and
  a resolved cash-conversion question does not by itself confirm the cell-line
  margin case. The two together, however, are close to a joint kill-switch per
  Section 2 B6/C3.
- **fragility_verdict:** FRAGILE. Four variables, half of them observable mostly
  through company narration, one already showing an internal three-way
  inconsistency (usable capacity) and one already showing a documented D-grade
  promise-delivery record (B05, B12b) on the exact category (capex/COD dates)
  the thesis depends on.

## d. Research brief (claude.ai live-web work order)

1. Verify whether the Q1FY27 results filing and its concall have since been
   published, and pull both; this closes the corpus's largest single gap.
2. Pull a credit-rating rationale for the FY2026 borrowing step-up (Rs 108cr to
   Rs 888cr) from CARE, CRISIL, ICRA, or India Ratings if one exists.
3. Pull the SEBI shareholding-pattern filing directly (not a third-party
   aggregator) to establish the actual promoter pledge trend across the last
   twelve quarters and the FII/DII split.
4. Search for the missing IPO-era prospectus (BSE SME, FY2022-23) to establish
   pre-IPO restated financials and the full promoter/group map.
5. Verify, via MCA company-master search, the corporate history and current
   status of Happy Buildmart LLP, Harmony Buildstate LLP, Fluidcon Engineers,
   Pinkcity Pipe Fittings Private Limited, and VM Portfolio Private Limited
   (B08 searches_skipped, no MCA tool access this session).
6. Verify via ICAI member records whether "CA Subhash Chand Gupta" at outgoing
   auditor Badaya & Co. has any relationship to Manish Gupta's late father,
   named in the AR's security schedule (B08 unverified lead, do not treat as
   fact without this check).
7. Check MNRE's own ALMM portal directly for the current effective date of
   ALCM/ALMM Part 2, given the date has already moved once (June 2026 to
   December 2026) in sources outside this corpus.
8. Check whether Solarworld Energy Solutions Ltd is itself listed or otherwise
   discloses financials, given its 12.4% customer concentration and complete
   absence from management or analyst commentary on any call.
9. Search for any exchange filing on the Narmadapuram cell line's actual
   commissioning, since the corpus carries three internally inconsistent guided
   dates and none of them has yet passed as of the run date.
10. Verify, via forum/employee-review archaeology (e.g. Glassdoor, AmbitionBox),
    any independent read on operational execution culture, given the B05
    credibility grade of D (B08 searches_performed lists this as attempted but
    not resolved this session).

---

# SECTION 5: PLAIN-LANGUAGE SUMMARY

1. Insolation Energy makes and sells solar panels, mostly built in its own
   factories in Jaipur and Sawarda, Rajasthan.
2. It also buys finished panels from others and resells them; that trading
   business is 17 percent of sales.
3. A small side business owns solar plants and sells the power, but it is only
   0.2 percent of revenue so far.
4. Buyers are government-linked solar developers, EPC contractors who build for
   them, and a shrinking network of dealers.
5. One customer, Solarworld Energy Solutions, is 12.4 percent of last year's
   sales and was zero the year before.
6. Buyers need a panel on the government's approved list. They do not need this
   particular maker; about ten other listed Indian makers qualify too.
7. The Indian solar panel market is large and still growing about 16 percent a
   year, and this company holds only a small slice of it.
8. Demand growth is uneven: government-scheme demand is tight, but demand
   outside those schemes is oversupplied and not very profitable right now.
9. The company has almost no protection from competition today. Research
   spending was zero. Exports were zero. Its dealer count is shrinking, not
   growing.
10. The one real building block for an advantage is a cell factory under
    construction, meant to stop the company from buying its main raw material
    from outside suppliers.
11. The story being told is a climb from assembler to integrated maker. That
    climb has not yet shown up in the accounts; the cell factory has not
    started making cells yet, and its start date has changed three times.
12. This business depends on execution and on cash coming in on time, not on
    the market being big enough. The market has room; the company's own record
    on hitting dates and collecting cash does not yet match its plans.
13. The single biggest open question is cash. Profit rose sharply last year,
    but the company's own operating cash flow went negative, and money owed to
    it by customers has aged badly with no bad-debt provision set aside.
14. The corpus cannot say whether that cash problem is a one-time side effect
    of fast growth or a lasting weakness, because the exact accounting policy
    that would explain it is missing from the annual report, and the newest
    quarter of results is not in this corpus at all.
15. The two biggest open questions going forward are: will the cell factory
    actually start on schedule and lift margins the way management says, and
    will the cash-collection problem improve or get worse in the next
    quarter's numbers.

---

# SECTION 6: STANDING EXTRACTION ANNEX

## 1. Units

No per-unit (Rs/Watt) figure is printed anywhere in the annual report. Quote,
Note 25 revenue disaggregation basis (AR p.130, cross-referenced at B04): the AR
discloses "Sale of Products — Finished Goods" at Rs 1,757.22cr and "Trading
Sales" separately, as rupee totals, with no per-watt breakout. B04's own field
states: "Revenue per unit (Rs/Watt or ASP) | NOT FOUND, check investor
presentation or concall" and "Cost per unit (Rs/Watt) | NOT FOUND, check
investor presentation or concall" (04-bizmodel.md lines 230-231).

**Comment.** This covers a basket (all module SKUs and both DCR/non-DCR grades
combined), not one product; no per-unit figure exists to disaggregate by grade
either. The volume and revenue lines from which one could be derived: FY2026
module production/sales volume was guided at "~2,000-2,100MW" for FY26 (B05
guidance_table, stated Jun-2025 call) against Finished Goods revenue of
Rs 1,757.22cr (Note 25, AR p.130); management-stated realisation bands of
Rs 13-14/watt (non-DCR) and Rs 20-22/watt (DCR) appear only in concall
commentary, not in the AR (B05, B06 verified claim). NOT DISCLOSED as a printed
AR figure.

## 2. Segment capital and debt

Quote, Note 46 (Ind AS 108), AR p.144: "The Group operates only in one Business
Segment i.e. 'Manufacturing & Trading of Solar Photovoltaic Modules', hence does
not have any reportable Segments as per Ind AS 108 'Operating Segments'."

**Comment.** NOT DISCLOSED by segment; there is only one reportable segment, so
no segment-level assets, liabilities, capital employed, or borrowings split
exists. Borrowings are unallocated at the whole-entity level. Total consolidated
borrowings for FY2026: secured non-current borrowings Rs 468.89cr (Note 18A,
AR p.124/126) against an IREDA sanction of Rs 1,134cr, plus short-term borrowings
which the CFO stated as Rs 300cr on the Jun-2026 call, an amount that does not
reconcile arithmetically against the CFO's own stated Rs 835cr total (B12b M6,
Concall_Jun_2026 p10). Total borrowings across the balance sheet are quoted
elsewhere in this run at Rs 887.91cr (B01 data_notes).

## 3. Guidance versus aspiration

From B05.guidance_table (concall-sourced, not AR-printed; classified here):

| Claim | Classification | Quote/figure | Period |
|---|---|---|---|
| FY26 revenue Rs 3,300cr | (a) guidance with a period | "Rs3,300cr" | FY26, stated Jun-2025 call |
| FY27 revenue Rs 5,500cr+ | (a) guidance with a period | "Rs5,500cr+" | FY27, stated Jun-2025 call |
| FY28 revenue Rs 8,500cr+, later cut to >Rs 5,000cr | (a) guidance with a period, revised | "Rs8,500cr+" then "more than Rs5,000cr" (Concall_Jun_2026), never acknowledged as a cut | FY28 |
| Cell line capex ~Rs1,300cr, later Rs1,500cr | (a) guidance with a period | "~Rs1,300cr, 3GW, production start Jan '27" then "Rs1,500cr" | FY27 |
| Wafer/Ingot expansion, 4.5GW | (c) capacity or capability only | "some 2-3 months time to finalize DPR", no firm capex figure, no technology partner named | Undated |
| BESS assembly entry | (c) capacity or capability only | "Capacity to be announced shortly" | Undated |
| US export market entry | (b) aspiration without a period | Named as an opportunity across all three calls; no order or certification milestone named | Undated |
| MP government incentive package (17-35%) | (b) aspiration without a period | Claimed benefit percentage; no grant or subsidy income recognised in the AR financial statements | Undated |

**Comment.** The company's own record on category (a) guidance is poor: of eleven
tracked promises with an evaluable outcome, one was delivered, five partial, five
missed on B05's own count, rising to eight missed once Verifier B's three
additions are included (B12b M15). No AR-printed forward guidance line exists;
every figure above is concall-sourced only, which is itself a disclosure-quality
finding (guidance lives entirely in unaudited commentary, not the filed
annual report).

## 4. Concentration

Quote, Note 46(ii), AR p.144-145: "from one customer the Group (Solarworld
Energy Solutions Ltd) has revenue of Rs 26,518.78 Lakh (March 31, 2025: Nil)
which is more than 10% of the total revenue from operations." This equals
Rs 265.19cr, 12.4% of FY2026 revenue (B02 top_findings rank 10; B03
ar_new_downstream_entities).

**Comment.** Top customer share: 12.4% (Solarworld), NIL the prior year. Top
product share: 81.9% own-manufactured Finished Goods is effectively the "top
product" given the single-segment classification (Note 25, AR p.130). Geography
concentration: NOT DISCLOSED in the extraction. The AR's Note 46(iii) heading
"Information about Geographical revenue and non-current asset" is present at
AR p.145, but the extraction breaks between that heading and Note 47, so the
geographical figures themselves are NOT FOUND in the extracted text (a possible
extraction artefact, not confirmed as an AR omission; distinct from the
confirmed Notes 1-3 omission).

## 5. Promise ledger

From B05.promise_delivery (source: three company concall transcripts,
cross-checked by B12b promise_delivery_spot_checks: 6 checked, 6 confirmed, 0
wrong):

| Promise (date made) | Status | Evidence anchor |
|---|---|---|
| FY26 revenue Rs 3,300cr (FY25 call) | Missed | Actual Rs 2,146cr, ~35% below; Concall_Feb_2026 (Ravi Dusad), "beyond our control" |
| FY26 PAT margin 11.1% (FY25 call) | Missed | Actual 9.3%, never separately reconciled |
| FY26 PAT Rs 300cr+ (FY25 call) | Missed | Actual ~Rs 201cr |
| Unit 3 Jaipur operational in 4-6 weeks (FY25 call) | Missed | Still ramping ~7 months later, Concall_Feb_2026, no reason given |
| Cell production start Jan '27 (FY25 call) | Partial | Revised Q3 FY27 (Concall_Feb_2026), then stated as both Q3 and Q4 FY27 within Concall_Jun_2026 itself |
| Mainboard migration ~Dec 2025 (FY25 call) | Partial | Actual completion 9-Mar-2026; revised interim timeline was met |
| Module capacity 4GW by FY26-end (FY25 call) | Delivered | 5.5GW installed by 31-Dec-2025 per Concall_Feb_2026 |
| FY27 monthly production 300MW/>3.5GW annual (Q3 FY26 call) | Missed | Cut to ~2-2.5GW annual within 3 months, Concall_Jun_2026 |
| FY26 cash accruals ~Rs 220cr (Q3 FY26 call) | Missed | Actual consolidated CFO minus Rs 73.13cr, never reconciled on any call |
| IPP 400MW KUSUM, ~Sept 2026 pace (Q3 FY26 call) | Partial | ~38-40MW commissioned as of Concall_Jun_2026, no revised date |
| Sustained EBITDA margin 14.5-15% FY26 (Q3 FY26 call) | Partial | Actual 14%, close to but below range |
| FY26 module volume 2,000-2,100MW (FY25 call) | Missed (not on B05's original tracker; added by Verifier B) | Delivered ~1,224MW, ~41% miss (B12b M15) |
| FY26 EPC revenue Rs 400cr (FY25 call) | Missed (added by Verifier B) | Delivered as "very small realization" (B12b M15) |
| Units 1-2 MonoPERC-to-TOPCon by Sept 2025 (FY25 call) | Missed (added by Verifier B) | Eight months later required new civil construction (B12b M15) |

**Comment.** Tally on the full, verifier-corrected count: 1 delivered / 5 partial
/ 8 missed. Credibility grade D (B05 credibility_grade; B12b concurs, "the
additional evidence removes any case for a higher grade").

## 6. Restated bases

Quote, Note No. 52 (consolidated) / Note No. 54 (standalone), AR p.150/AR
standalone equivalent: "Regrouped, Recast, Reclassified. a. All amounts
disclosed in the financial statements and notes have been rounded off to the
nearest Lakhs upto two decimals as per the requirements of Schedule III, unless
otherwise stated. b. Previous period's figures in the financial statements,
including the notes thereto, have been reclassified wherever required to
confirm to the current period's presentation/classification."

**Comment.** This is standard boilerplate; no specific quantified restatement is
separately identified in that note (B02 restatements_found). However, B01
independently found that the AR's FY2024 (1-Apr-2024) opening balance sheet
column IS restated for six subsidiaries incorporated Jul-2024 to Aug-2025:
restated FY2024 Total Assets Rs 274.69cr (AR p.116) and FY2025 CWIP Rs 52.88cr
(AR p.116) do not match screener's own unrestated FY2024/25 figures of
Rs 262.78cr and Rs 46.10cr respectively (B01 data_notes). The comparative as
printed in the latest filing is the AR's own restated Rs 274.69cr/Rs 52.88cr
figures; the unrestated screener figures are not printed in the AR itself.

## 7. Corporate-action clauses

No scheme of arrangement, demerger, merger, or buyback exists in the corpus.
Quote, AR p.150 (ix): "There is no Scheme of Arrangements has been approved by
the Competent Authority in terms of sections 230 to 237 of the Companies Act,
2013 during the Year ended March 31, 2026 and March 31, 2025."

One preferential issue is disclosed. Quote, Note 15(e), AR p.123: "During the
Financial year 2024-25 on 11/12/2024 company has raised money of Rs. 39519.60
lakhs by issuing through Preferential Share issue of 12,02,300 shares of Rs. 10
each on a premium of Rs. 3277 per share (Rs. 3287 Including premium) total
amounting of Rs. 39,51,960,100 through preferential share issue."

**Comment.** No undertaking definitions, liability-allocation clauses, or
appointed/effective dates apply to a preferential share issue in the way they
would to a scheme; those concepts are NOT APPLICABLE here. The disclosed
mechanics are: date 11-Dec-2024, 12,02,300 shares issued at Rs 3,287/share
including premium, aggregate Rs 395.196cr raised. B08's search for the full
117-name allottee list (referenced elsewhere in market commentary) was skipped
this session for lack of a working BSE corrigendum PDF fetch (B08
searches_skipped); the allottee identities are NOT FOUND in this corpus.

## 8. Related-party perimeter

Quote, Note 8, AR p.121, on the two LLP investments: "The company has investment
in Happy Buildmart LLP dated on 26 Feb. 25 at C-02, Fluidcon House, New Aatish
market... (b): The company has investment in Harmony Buildstate LLP dated on 26
Feb. 25 at C-02, Fluidcon House, New Aatish [market]..." Amounts per B08: Rs
32.5cr to Rs 34.5cr (Rs 4cr fixed + Rs 12.25cr current capital, x2), each LLP
90% owned by one promoter-director couple, 10% held by the company's own
wholly-owned subsidiary.

Other named related parties from Note 41 (AR p.135-137), per B08's independently
verified read: Fluidcon Engineers (active trading relationship, promoter-linked),
rent paid to Manish Gupta and Vikas Jain personally, consultancy fees to
Mahendra Kumar Jain (Rs 2.87 lakh FY26 / Rs 9.84 lakh FY25), staff training fees
to Navya Gupta, loans to/from VM Portfolio Private Limited, personal guarantees
by promoter-directors, and KMP remuneration.

Quote, AOC-2 (Annexure III), AR p.64, on the same-year RPT disclosure: states
"Not applicable" for both arm's-length and non-arm's-length related-party
transaction categories, directly beside Note 41's full page of named, quantified
transactions (B08 verdict_basis).

**Comment.** The related-party perimeter is real and multi-entity, but the
company's own summary disclosure (AOC-2) contradicts its own detailed note
(Note 41) on whether any RPTs occurred at all. No arm's-length pricing statement
is disclosed for either LLP investment or for Fluidcon Engineers.

## 9. Pledge and shareholding

Quote, AR corporate governance section (unclaimed-shares shareholding-pattern
table), AR p.82: "Promoter and Promoter Group" = 14,57,21,001 shares = "66.12"
[percent], against "Foreign Portfolio Investor" = 24,09,259 shares = "1.09"
[percent].

**Comment.** No pledge or encumbrance disclosure, and no explicit NIL statement,
exists anywhere in the AR (B02 top_findings rank 13; B08 pledge_trend). Full-text
search for "pledge"/"encumbrance" finds only fixed-deposit pledges for bank
guarantees, share pledges of SPV equity as loan security, and land mortgages,
none of which are promoter personal-shareholding pledges (B08). Twelve-quarter
pledge and holding history as filed is NOT DISCLOSED in this corpus; the SEBI
quarterly shareholding-pattern filing itself is absent (B00 gap `shareholding`).
Third-party aggregator data (MEDIA tier, not filing-anchored in this corpus)
reports 0.00% pledge as of the FY26 SEBI filing and FII holding rising from
0.94% (Mar-2025) to 1.09% (Mar-2026) (B08 transition_evidence); this is recorded
as MEDIA-tier evidence only, not verified from a primary filing in this corpus.

## 10. Verification

Documents quoted in this annex, with filename and date:
- Annual Report 2025-26 (FY ended 31-Mar-2026): `annual-report__Annual_Report_2026.txt`,
  pages 82, 116, 121, 123, 130, 135-137, 144-145, 150, per the "===== PAGE N ====="
  extraction markers (never the transcript printed footer, per this run's known
  citation defect).
- B01-gate0.yaml, B02-notes.yaml, B03-ardeep.yaml, B04-bizmodel.yaml,
  B05-concall.yaml, B06-peers.yaml, B07-emoat.yaml, B08-promoter.yaml,
  B09-tam.yaml, and verifier blocks B12a-B12d (all dated 2026-09-06, this run).
- Stage reports 02-notes-pass1/2/3.md, 03-ardeep.md, 04-bizmodel.md,
  05-concall.md, 08-promoter.md (dated 2026-09-06, this run), used to retrieve
  quotes and page anchors already established at stage level.

CORPUS COMMIT HASH: 1b59eddc18060027eb405351cb35950fbf6419f7

---

```yaml
stage: B09b-dossier
company: "INA"
run_date: "2026-09-06"
model: claude-sonnet-5
status: complete
corpus_verdict: "CORPUS GAPPED-FRESHNESS"
corpus_gaps:
  - document: "Q1FY27 results filing (QE 30-Jun-2026) and its concall transcript"
    expected_source: "BSE / NSE corporate filings; company IR page"
    kind: "freshness-pair"
  - document: "Prospectus (IPO FY2022-23, BSE SME)"
    expected_source: "BSE SME prospectus archive / company IR page"
    kind: "findable-missing"
  - document: "Credit rating rationale for FY2026 borrowing step-up"
    expected_source: "rating agency site (CARE / CRISIL / ICRA / India Ratings)"
    kind: "findable-missing"
  - document: "SEBI shareholding-pattern filing (pledge trend, FII/DII split)"
    expected_source: "BSE / NSE quarterly shareholding-pattern filing"
    kind: "findable-missing"
  - document: "Research / broker notes"
    expected_source: "broker research, if any exists"
    kind: "findable-missing"
  - document: "Screener companion CSVs (Profit_Loss/Balance_Sheet/Cash_Flow/Quarters)"
    expected_source: "collector re-run (known defect, not company-side)"
    kind: "findable-missing"
  - document: "Granular corporate-action filings (orders/JV/capex) beyond one thin Reg 30 letter"
    expected_source: "BSE / NSE corporate announcements"
    kind: "plausibly-nonexistent"
  - document: "AR Notes 1-3, Material Accounting Policies text"
    expected_source: "company IR page / BSE-NSE filed annual report (re-extraction)"
    kind: "findable-missing"
archetypes:
  - line: "Module manufacturing and trading (98.9% of FY2026 revenue)"
    archetype: "Commodity converter"
  - line: "Sale of electricity (IPP / PM-KUSUM, 0.2% of FY2026 revenue)"
    archetype: "Licence / scarcity business"
transition:
  - line: "Module manufacturing and trading"
    from_tier: "R1 COMMODITY PRICE-TAKER"
    to_tier: "R2 COST-ADVANTAGED CONVERTER"
    engine: "Backward integration into cell manufacture (4.5GW TOPCon line, Narmadapuram) removing a bought-in cost that is ~78% of revenue"
    proof_gate: "Narmadapuram cell line reaches commercial production on a date that holds, and group EBITDA margin moves visibly toward 20%+ within 2-3 quarters after commissioning, without the corresponding PAT margin falling on a like-for-like basis"
    recognition_gap: "OPEN QUESTION: whether the market's current pricing of INA already reflects the claimed cell-integration margin uplift; resolved at Stage 11 via the Section 1B PE gap, no number stated here"
    ugliness: "INDETERMINATE (not yet classified ARTIFACT-OF-CLIMB vs STRUCTURAL-FEATURE; evidence supports both reads, see Section 2 B5)"
    transition_falsifier: "Cell line fails to reach commercial production within 12 further months of any of its three stated dates, OR margin does not move toward the guided range post-COD, OR the uplift arrives only via a PAT-to-EBITDA guidance-basis switch"
  - line: "Sale of electricity (IPP / PM-KUSUM)"
    from_tier: "R0 NON-OPERATING / pre-operating"
    to_tier: "R1 COMMODITY PRICE-TAKER"
    engine: "PM-KUSUM allotment commissioning from ~38-40MW toward the stated 400MW capacity build"
    proof_gate: "Sale-of-electricity revenue line scales toward a run-rate consistent with commissioned MW x load factor x tariff, rather than staying near Rs 4-5cr for multiple quarters past stated commissioning dates"
    recognition_gap: "OPEN QUESTION: not separately assessed for this near-zero-revenue line; folded into the overall Stage 11 PE-gap resolution"
    ugliness: "ARTIFACT-OF-CLIMB candidate (pre-revenue build phase), not yet tested"
    transition_falsifier: "Commissioning pace stays near the current ~38-40MW level for multiple further quarters with no revised date given"
dominant_variables:
  - "Narmadapuram 4.5GW cell line COD and post-COD margin trajectory (three internally inconsistent guided dates)"
  - "Consolidated CFO/PAT and CFO/EBITDA ratios, and receivables aged beyond six months (39.5% FY26)"
  - "Usable cell/module capacity as a share of nameplate (internally contested, 50-55% to 84-89% within one company)"
  - "DCR cell-supply dependency (Emvee/Premier tie-up) and the ALMM Part 2/ALCM enforcement date (already deferred once)"
business_falsifier: "The module/trading engine's cash-conversion problem proves structural rather than a one-year ramp (aged receivables continuing past 39.5% into FY2027, spreading to the parent's own book), combined with the Rs 1,654.01cr corporate guarantee structure (205% of net worth, 3.0x parent assets) crystallising against the listed parent"
mental_model_status: "DRAFT - PENDING OPERATOR SIGN-OFF"
fragility:
  variable_count: 4
  verifiability_ratio: "2 of 4 externally observable"
  single_point_failure: "none - failure requires conjunction"
  fragility_verdict: "FRAGILE"
candidate_count: 7
research_brief_items: 10
plain_summary_points: 15
annex:
  present: true
  questions_answered: 10
  corpus_commit_hash: "1b59eddc18060027eb405351cb35950fbf6419f7"
```
