# CAPILLARY: HALT 1 UNDERSTANDING DOSSIER

Company: Capillary Technologies India Ltd (CAPILLARY). Run date: 2026-09-19.
Assembled from committed blocks B00-B09, verifier blocks B12a-B12d,
confidence.yaml, B13-synthesis-lite.yaml, and the stage reports and final
files in this run. No new research. No valuation, price, or verdict
vocabulary appears anywhere below, except the one scoped exception named in
Section 2 Part B4.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

**1. Concalls.** Three transcripts held, all post-listing: Q3 FY26
(Concall_Feb_2026_Transcript.pdf, called 06-Feb-2026), Q4 FY26
(Concall_May_2026_Transcript.pdf, called 06-May-2026), Q1 FY27
(Concall_Aug_2026_Transcript.pdf, called 04-Aug-2026, quarter ended
30-Jun-2026). Most recent quarter covered: Q1 FY27. No Q2 FY26 call exists;
the company listed 21-Nov-2025, after that quarter closed. Given the
run date of 2026-09-19, the next quarter (Q2 FY27, ending 30-Sep-2026) has
not yet closed, so no more recent transcript is plausibly missing. (B00)

**2. Annual reports.** One AR held: Annual_Report_2026.pdf, FY 2025-26
(Reg 34 filing, 271pp, signed 06-May-2026). This is the latest completed FY
and it is present. Fewer than 3 years are held, because the company was
unlisted before FY26; no FY25 or earlier AR exists as a listed filing. The
UDRHP-I (June 2025) carries restated pre-IPO financials as the closest
substitute for the missing years. (B00)

**3. Results filings.** Latest quarterly filing: Q1 FY27
(Results-Q1FY27-20260804.pdf, 04-Aug-2026, quarter ended 30-Jun-2026). No
quarter-gap exists between the latest results filing (Q1 FY27) and the
latest AR (FY26, audited results filed 06-May-2026): one ordinary quarter
separates them. (B00)

**4. Investor presentations.** Latest held: two Q1 FY27 decks, both dated
04-Aug-2026 (Investor_Presentation_1.pdf, 59pp, and
20260804-Investor-Presentation-30pp.pdf, 30pp). Also held: a 65pp deck dated
14-May-2026 and the SessionM acquisition deck dated 24-Feb-2026. (B00)

**5. Research / rating.** research/ is EMPTY: no broker note, no rating
rationale, held. rating/ is EMPTY: the FY26 AR states the company "has
neither obtained nor revised any credit rating" and lists credit ratings as
"Not obtained" (AR, Board's Report and Corporate Governance Report). This is
not a collection gap; no rating exists to collect. Per the /step1 autonomy
contract, this EMPTY-FOLDER CONFIRMATION was suppressed at intake with the
standing answer "proceed with the gaps." Both empty folders are repeated
here per that same instruction: **rating/ (declared: no rating obtained),
research/ (empty).** (B00)

**6. Corporate actions.** 38 Reg 30 / SAST / postal-ballot / AGM /
monitoring-agency filings, hand-staged from BSE, dated Nov-2025 to Sep-2026.
Curated, not exhaustive: routine trading-window, ESOP-grant/allotment,
newspaper and duplicate board-outcome filings were left out. Six of the 38
are scanned image-only filings with no text layer, read via PNG pages in
inputs/announcements/page-images/. (B00)

**7. Freshness pair check.** B00's `freshness_verdict` is **FRESHNESS PAIRS
OK**. All four pairs PASS: RESULTS to CONCALL (Q1 FY27 results paired to the
Aug-2026 concall for the same quarter); RATING BULLETIN to RATIONALE (no
rating exists, so no bulletin to pair, PASS by absence); SEBI ORDER to
ORDER TEXT (no SEBI order referenced anywhere in the corpus, PASS by
absence); AR to LATEST AUDITED ANNUAL RESULTS (the FY26 AR pairs to the
FY26 audited results filing). No pair FAILED.

**8. Verdict line: CORPUS GAPPED.** Freshness pairs are OK, so the
GAPPED-FRESHNESS cap does not apply. Findable-but-missing items, each with
its expected source:
- Final RHP / Prospectus (Nov-2025, final offer size Rs 877.5 Cr, band
  Rs 549-577): capillarytech.com returned HTTP 403 to scripted download.
  UDRHP-I (June 2025) is held as a substitute; differences (updated stub
  period, final pricing) are not in the corpus. Expected source: company IR
  page or BSE.
- FII/DII split: absent from the BSE Reg 31 shareholding summary held for
  Dec-2025, Mar-2026, Jun-2026. Expected source: BSE or NSE full
  shareholding pattern.
- screener P&L / Balance Sheet / Cash Flow / Quarters export sheets: came
  out empty (formulas with no cached values) for CAPILLARY and all three
  peers; only the Data_Sheet CSVs are populated. Expected source: re-open
  and re-save Financials.xlsx, then re-run the collector.
Plausibly-nonexistent: no sell-side research or broker coverage was found
anywhere in the corpus or in B08's web search; consistent with a company
three quarters into its listed life with no credit rating. This is itself
a data point on the company's visibility, not a collection failure.

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT - PENDING OPERATOR SIGN-OFF.** This declaration is not signed. It is
the run's evidence read, assembled for the operator to test, amend and sign
in claude.ai after live-web stress-testing.

### PART A: THE FROM STATE

**A1. Archetype.** Capillary reports a single Ind AS 108 segment, "CRM
services" (AR Note 33), so one line applies. It fits no archetype in the
CLAUDE.md library cleanly. The two nearest are Platform/network (the
delivery model: cloud SaaS, retention-driven, unit economics per member or
transaction) and Outsourcing partner / CDMO-EMS-IT services (the commercial
profile: client concentration at 58.71% of FY25 revenue in the top 10,
UDRHP-I p.40-41; contract stickiness from 3-7 year terms and the owned
points ledger; wallet-share expansion via cross-sell of Engage+, Insights+,
Rewards+ and aiRA onto the Loyalty+ base, B04). Neither fits whole: B04
found network effects explicitly ABSENT (each brand's programme is closed
to its own members), and the business is asset-light with no capacity-fill
dynamic. The mismatch is itself the finding: this is a subscription SaaS
roll-up, a growth engine the archetype library does not name.

**A2. The simple analogy.** Capillary runs the digital version of the
punch card for big brands. Every time a shopper earns or redeems points at
a store, an airline or a bank that uses Capillary, there is a good chance
Capillary's software is the ledger keeping score behind the scenes. The
brand pays a subscription, the way a shopkeeper pays rent, not a one-time
price for a single sale. Because the points bank lives inside Capillary's
system, it is a hassle for the brand to rip it out, the way you would not
switch banks mid-relationship. Capillary also buys smaller versions of
itself and moves those brands' customers onto its own system, pocketing the
gap between the smaller company's thin margin and its own fatter one. The
risk: a handful of big brands still account for a large share of the till,
so losing one hurts more than it would for a shop with a thousand small
customers. (B04 1E, adapted)

### PART B: THE TRANSITION

**B1. FROM to TO (single line, CRM services).** FROM sits between R1 and
R2 on the Quality Ladder: real switching-cost pricing power exists (owned
ledger, ~9 integrations per customer, 3-7 year contracts, B04), but ROCE
has never cleared 10% in six disclosed years (median -1.83%, FY23-FY26
window; five-year arc FY22 ~0.0%, FY23 -70.43%, FY24 -14.53%, FY25 4.56%,
FY26 8.82%, AR p.11-12; B01 deal-breaker). TO, as management states its own
destination, is R3 VALUE-ADDED / SPEC'D SUPPLIER, with a stated ambition
toward R4 FRANCHISE / SHARE-OF-WALLET LEADER: a 25-30%+ steady-state EBITDA
margin (70% gross margin, ~15-16% tech, similar S&M, 5-7% G&A, Q4 FY26
call), NRR-driven expansion above 110%, and a "cash ROIC 22%" figure
management volunteered on one call (B12b minor finding) in place of the
8.82% statutory ROCE. The rung-jump base rate (CLAUDE.md: one rung per 2-3
years) applies to whatever climb Stage 11 eventually measures; the company's
own claimed endpoint is itself a multi-rung reach from where the six-year
record sits today.

**B2. The engine.** Two mechanisms, both named directly by the company: (1)
migrating each acquired customer book from roughly 30% gross margin
as-acquired to Capillary's own 65-70% steady-state gross margin over a
typical 3-4 year window (AR p.79-80; three of five completed deals, Persuade,
Brierley and Rewards+, have reached 40-45% contribution margin; Kognitiv and
SessionM are explicitly "in progress"); (2) operating leverage on the core
cost base, where technology, sales and marketing and corporate overhead grew
about 14% against 23% total revenue growth in FY26 (AR p.79-80; B03),
credited to AI-led, software-delivered service replacing the agency
industry's roughly 30-people-per-programme model (AR p.76, p.96).

**B3. The proof gate.** The exact metric and threshold this run's own
falsification line already names: H1 FY27 organic revenue growth at
constant currency, printed with the Q2 FY27 results (expected ~Nov-2026),
must hold at or above 15%; sustained growth below 15% is the stated red-flag
line (B04 3B, B05 dropped_triggers cross-reference, gate-recommendation
falsification line). Paired with that: ROCE above 10% for two consecutive
reporting periods (B03 monitorable), the Gate 0 deal-breaker threshold
Capillary has never yet cleared. Until both print, the transition is
narrative, not proof. NOT FIRED on current evidence: organic growth itself
carries three live readings (see C1 below), and FY26 ROCE (8.82%) is the
best on record and still under 10%.

**B4. The recognition gap: OPEN QUESTION, resolved at Stage 11.** Per the
one scoped exception this dossier carries: does Capillary's current market
pricing already reflect the TO-state margin and ROCE improvement described
above, or does it still price the FROM-state's six-year record of ROCE
below 10%? This dossier states no number and no conclusion. Stage 11
resolves it via the Section 1B destination-PE gap. If the TO state is
already priced, the re-rating engine described in B2 is spent and any
return would have to come from earnings growth alone, per the Transition
Decision Matrix in CLAUDE.md.

**B5. The ugliness test: ARTIFACT-OF-CLIMB, on current evidence.** The low
ROCE tracks four historical loss years (FY21-24), a post-IPO equity base
that roughly doubled, and acquisition goodwill sitting on the balance sheet,
not a falling unit economics story: subscription gross margin actually rose
from 66.4% to 67.2% in FY26 (AR p.99, p.190), and organic revenue compounded
42% a year FY23-26 (AR p.79). The evidence that would flip this to
STRUCTURAL-FEATURE is the one contrary data point already on record:
inorganic (acquired-book) NRR fell from 96% to 94% in FY26, and the
Rs 24.96 Cr Kognitiv churn indemnity was triggered because the seller
failed agreed commitments (Q4 FY26 call; B12b MAJOR finding 6), a signal
that at least one acquired book is not yet migrating cleanly. Both readings
sit in the same evidence base; no verdict is stated here.

**B6. The transition falsifier.** Two consecutive quarters in which organic
EBITDA margin (exceptional items stripped) fails to rise toward the 25-30%
steady-state band management has itself named, occurring together with
either SessionM's or Kognitiv's contribution margin stalling below 15% by
Q4 FY27 (B05 kill_signal, priority 2), that combination would disprove the
margin-bridge mechanism itself (B2), not merely delay it. This is distinct
from the business falsifier in C3 below: this falsifier kills the CLIMB, not
the underlying SaaS business.

### PART C: WHAT THE MODEL WATCHES

**C1. Dominant variables.**
1. Organic revenue growth at constant currency. Current state: UNRESOLVED,
   three live readings from the same set of calls: management's 17%
   (which may already include about 6 points of currency, Q1 FY27 call),
   an analyst's own Q1 arithmetic near 11% (Q1 FY27 call), and a
   plan-arithmetic inference of 3-6% built from management's own organic/
   acquired split of the FY27 guide (B12b MAJOR finding 1, labelled
   [INFERENCE] in that verifier's own working).
2. Acquired-book margin migration (SessionM, Kognitiv). Current state: both
   explicitly "in progress" (AR p.80). Kognitiv's first migrated customer
   was due live 01-Sep-2026, full migration targeted by Sept-2027 (Q1 FY27
   call). SessionM's ARR figure moved from "USD 35m business, 40+ logos"
   (Q4 FY26 call) to "USD 32m ARR, 45-odd customers" (Q1 FY27 call) without
   comment (B12b MAJOR finding 4).
3. ROCE. Current state: 8.82% FY26 (AR-published), the best year on record
   and still below the 10% Gate 0 deal-breaker threshold on every
   calculation basis tried (B03 Phase 3B: independent recomputes give
   2.96-5.30%, all below the AR's own figure).
4. Organic Net Revenue Retention, ex-large-account. Current state: 114%
   organic FY26 (AR MD&A p.80), 111% or 116% ex one large healthcare
   customer in Q1 FY27 depending on the exclusion (B05); whether that flat
   Q1 FY27 account is the same account Q3 FY26 described as growing 50% is
   unconfirmed (B12b MAJOR finding 2).

**C2. What the model rejects.** Market-sizing questions are noise here:
B09 already found the obtainable market (Rs 1,361 Cr in 3 years, Rs 1,913 Cr
in 5, a STRONG runway with 7.9x headroom over current SAM share) is not the
binding constraint; management's own USD 18.2bn TAM figure runs about 18
times the correctly-defined software-only pool and is not the number this
model tracks (B09). The model also rejects "will AI disrupt loyalty
software" as a binary question: every peer transcript treats agentic AI as
a manageable, addressable risk rather than an existential one (B06), so the
real question is execution of aiRA's own monetisation (still a $2-2.5m ARR
pilot against a 5-10% of FY27 revenue target, B05), not whether AI
disruption happens at all.

**C3. The business falsifier (distinct from B6).** Evidence that would force
a re-declaration of the FROM business itself, not just the climb: goodwill
impairment on the Rs 309.58 Cr goodwill balance (24% of consolidated
assets, tested at a 27.70% WACC with no disclosed sensitivity headroom, a
named Key Audit Matter, AR Note 4 p.219-220), or a second cyber-fraud-type
integration failure at an acquired entity following the EUR 3.0m Czech
subsidiary fraud already under KPMG forensic audit (B04
first_deterioration_signals). Either would show the M&A engine destroying
value on integration rather than creating it, which is a different claim
than the transition merely stalling.

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

Drafted per the five-question spec in prompts/13-synthesis-pipeline.md
(products and why they matter; who the customers are; why demand exists;
why demand grows; where the competitive advantage sits per line), from
B01-B09. This is the Halt 1 draft; Stage 13's copy is the version later
stages update.

Capillary sells a cloud platform that runs loyalty programmes for large
consumer brands. Subscriptions to that platform made 89% of FY26 revenue.
The core product, Loyalty+, keeps the points ledger itself: every point a
shopper earns, spends or loses to expiry sits in Capillary's system,
audited like a financial ledger. Engage+, Insights+, Rewards+ and the aiRA
AI layer sit on top, and the brand pays per member or per transaction, not
per user seat, on contracts of three to seven years (AR p.76). A brand
cannot drop it quickly, because the ledger holds its members' live balances
and an average customer runs about nine integrations into its tills, online
stores and data systems. Installation fees, 10% of revenue, pay once for
connecting a new or migrated customer, and campaign services, under 1%, are
run as agent.

The buyers are about 415 brands in 49 countries, around 20 of them Fortune
500 names, across retail (now under a third of revenue), banking, telecom,
travel, hospitality and healthcare (AR p.75-76, p.98). Buying is
concentrated: the top 10 customers made 58.71% of FY25 revenue
(UDRHP-I p.40-41), the company has not disclosed the FY26 figure (Note
36(iii) is incomplete, B02), and the United States supplied 55.6% of FY26
revenue (AR Note 22).

Demand today comes from brands moving money into keeping customers, because
the company's cited industry data says winning a new customer costs five
times as much as keeping one (Investor Presentation May-2026 p.9, sourced
to Zinnov). The run tracks that demand through named downstream signals:
"Fortune 500/large-enterprise new-logo referrals via System Integrators and
Consulting Partners," which brought about 40% of FY26 new customers (AR
p.80); "US enterprise MarTech/customer-engagement software budget growth,"
since about 56% of FY26 revenue is US-sourced; and "named large/flagship
end-customer renewal and expansion decisions" (B09).

Growth should come from software taking share in a loyalty market
management says is still over 90% agency spend, a claim no peer transcript
could verify (B06 unverifiable claims). It should also come from buying and
migrating fragmented agency rivals at 0.4x-3x revenue (AR p.79-80), and from
privacy rules that push brands toward owned customer data, tracked as
"Data-privacy regulatory activity (GDPR enforcement, US state privacy laws,
India DPDP Rules rollout)" (B09). Two outside signals cut both ways:
"Enterprise generative-AI/agentic-AI adoption rate among marketing
organisations" can lift aiRA or let brands build their own tools, and
"USD/INR and other cross-currency rates" added about 6% to Q1 FY27 growth
(B09).

The subscription line holds the one clear moat: switching costs from the
owned ledger and the integrations (B04). The emerging moat scan landed in
the MODEST band (24.0 stage score; 21.9 on Verifier C's recompute before
further rescoring, still MODEST), and its strongest row, the acquisition
roll-up, fails the sacrifice test because a well-funded rival could run the
same roll-up without giving anything up (B07, B12c F-E1). The security
certifications are table stakes for the enterprise segment, aiRA's usage
pricing is an untested counter-position against seat-priced rivals, and the
scan scored talent asymmetry and the cannibalisation barrier at zero. The
installation and campaign-services lines carry no moat of their own.

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. Verticals framed

**Vertical 1: Organic revenue growth at constant currency.**
The corpus establishes: FY27 total revenue guidance Rs 1,000-1,050 Cr
against FY26 Rs 735 Cr (B05 guidance table, Q4 FY26 call), later sharpened
to "will definitely beat" Rs 1,065 Cr (Q1 FY27 call); management's own plan
split implies roughly Rs 673 Cr organic against roughly Rs 390 Cr acquired
(Q1 FY27 call, B12b MAJOR finding 1); Q1 FY27 organic growth stated at
"about 17%," which may already include about 6 points of currency (Q1 FY27
call). The corpus cannot establish which of the three readings (17%, ~11%,
3-6%) is correct, all three come from the same three calls without
reconciliation. Questions that decide it: (1) What is H1 FY27 organic
revenue growth at constant currency, reported on a single consistent
basis? (2) Does management's "17% organic" figure already net out FX, and
if not, what is the FX-adjusted number? (3) Does the implied organic/
acquired split of the FY27 plan hold steady quarter to quarter, or does it
move as SessionM/Kognitiv contributions land?

**Vertical 2: Acquired-book margin migration (SessionM, Kognitiv).**
The corpus establishes: Kognitiv acquired 01-May-2025 for CAD 23.44mn, with
62% of consideration allocated to goodwill, mainly "assembled workforce and
estimated synergies" (AR Note 39, p.254); Kognitiv's first customer targeted
live on the Capillary platform 01-Sep-2026, full migration by Sept-2027 (Q1
FY27 call); SessionM acquired from Mastercard International Incorporated for
a total consideration of USD 20.00 million, transaction completed
01-May-2026 (AR Note 44, p.259); a Q1 FY27 call reference to a net price of
about Rs 17 Cr after an unexplained debt true-up (B12b MAJOR finding 5); the
acquired customer base restated from "USD 35m business, 40+ logos" (Q4 FY26
call) to "USD 32m ARR, 45-odd customers" (Q1 FY27 call) without comment. The
corpus cannot establish the SessionM purchase price allocation or
goodwill/intangible split (NOT FOUND; the AR's only SessionM mention is the
single Note 44 event-after-reporting-period sentence, five days before the
deal closed), nor the composition of the roughly USD 18m gap between the
USD 20m headline and the Rs 17 Cr net figure. Questions that decide it: (1)
What is the SessionM PPA goodwill/intangible split, once filed? (2) What
explains the roughly USD 18m adjustment cited on the Q1 FY27 call? (3) Is
Kognitiv's first-customer migration still on track for 01-Sep-2026?

**Vertical 3: ROCE / capital efficiency.**
The corpus establishes: AR-published consolidated ROCE 8.82% FY26 (AR
p.101), the best year on a five-year arc that ran FY22 ~0.0%, FY23 -70.43%,
FY24 -14.53%, FY25 4.56% (AR p.11-12); an independent recompute using PBT
before or including the exceptional item against average or year-end
capital employed gives 2.96% or 5.30% (B03 Phase 3B), both below the AR's
own 8.82%; management volunteered "about 3%" on one call, then reframed the
metric as "cash ROIC 22%" (Q4 FY26 call, B12b minor finding). The corpus
cannot establish which capital-employed base reconciles the AR's 8.82% to
either the independent recompute or management's own "about 3%" comment on
the call. Questions that decide it: (1) What capital-employed base produces
the AR's 8.82% figure? (2) Is "cash ROIC 22%" a legitimate parallel metric
with a disclosed formula, or a substitute offered in place of a weaker
statutory number? (3) Does ROCE clear 10% for two consecutive periods, the
Gate 0 deal-breaker threshold?

**Vertical 4: Organic Net Revenue Retention, ex-large-account.**
The corpus establishes: blended NRR 110%, organic 114%, inorganic
(acquired-book) 94% (AR MD&A p.80, FY26); Q1 FY27 organic NRR given as 111%
overall or 116% excluding one large healthcare customer that did not grow
(Q1 FY27 call); Q3 FY26 separately described a top-5 healthcare payer's
member base growing 50% with a CY26 revenue bump (Q3 FY26 call). The corpus
cannot establish whether the flat Q1 FY27 healthcare account is the same
account Q3 FY26 described as growing 50% (B12b MAJOR finding 2, identity
unconfirmed), nor the FY26 top-10 customer concentration percentage (Note
36(iii) is grammatically incomplete, B02). Questions that decide it: (1) Is
the flat Q1 FY27 healthcare account the same one Q3 FY26 described as
growing? (2) What is organic NRR with no customer exclusions applied? (3)
What is the FY26 top-10 customer concentration percentage?

### 4b. Candidate signal table

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| Fortune 500/large-enterprise new-logo referrals via System Integrators and Consulting Partners (~40% of FY26 new logos) | SI/consulting referral share falls materially below 40% of new logos for two consecutive quarters | Quarterly | Capillary Reg 30 filings / named partner-program announcements (Downstream Source Discovery Protocol) |
| US enterprise MarTech/customer-engagement software budget growth | Independent survey shows US MarTech budget growth turning negative or flat for two consecutive readings | Quarterly | Gartner Marketing Technology Survey / CMO Spend Survey |
| USD/INR and other cross-currency rates | Sustained rupee strengthening reverses the ~6% Q1 FY27 FX tailwind into a headwind for two consecutive quarters | Quarterly | RBI reference rate / company quarterly disclosure |
| Named large/flagship end-customer renewal and expansion decisions | A Reg 30 non-renewal disclosure from a top-10 customer, or confirmation the flat Q1 FY27 healthcare account keeps shrinking | Event-driven | Reg 30 non-renewal disclosures / the customer's own investor filings |
| Data-privacy regulatory activity (GDPR enforcement, US state privacy laws, India DPDP Rules rollout) | A regulatory rollback or enforcement pause removes the first-party-data tailwind | Event-driven | EU Data Protection Board / India MeitY DPDP notifications / US state AG offices |
| Enterprise generative-AI/agentic-AI adoption rate among marketing organisations | Adoption data shows brands building in-house (vibe-coding) tools at a materially higher rate than buying, or aiRA paying customers stay under 10 of 150+ through FY27 | Annual (survey) / Quarterly (aiRA disclosure) | Gartner/Forrester enterprise AI adoption surveys; Capillary quarterly aiRA disclosure |

### 4c. Fragility read

- **variable_count:** 7, the four dominant execution variables from
  Section 2 C1 (organic growth, acquired-book margin migration, ROCE, NRR
  ex-large-account) plus three external/macro variables that gate the bull
  case (FX rate direction, US enterprise MarTech budget growth, enterprise
  AI-adoption direction).
- **verifiability_ratio:** 3 of 7 externally observable (FX via RBI
  reference rate; US MarTech budget growth via Gartner/CMO surveys;
  AI-adoption direction via Gartner/Forrester surveys). The other 4 are
  company-narrated figures under active dispute across Capillary's own
  three calls (B12b logged 9 MAJOR findings, four of which sit directly on
  these four variables: organic growth, healthcare-account NRR, SessionM
  ARR restatement, gross margin).
- **single_point_failure:** Organic revenue growth at constant currency
  comes closest to one. If H1 FY27 confirms near the plan-arithmetic low
  end (3-6%) rather than management's claimed 17%, the FY27 guide becomes
  acquisition-carried rather than organic-engine-carried, and the NRR,
  margin-bridge and ROCE narratives built on an organic-growth premise all
  need re-reading around that single number. It is not a clean single point
  because the other three variables are also independently contested, so
  "none - failure requires conjunction" is the more literal reading; but
  organic growth is the variable every other reading depends on.
- **fragility_verdict: FRAGILE.** Many variables, a majority company-
  narrated rather than externally verifiable, one variable (organic growth)
  load-bearing across the other three, and a verifier-documented pattern of
  the same underlying figures moving between calls without reconciliation
  (B12b: aiRA sizing, SessionM ARR, platform gross margin, organic growth
  all cited as examples).

### 4d. Research brief (claude.ai work order)

1. Verify H1 FY27 organic revenue growth at constant currency once the Q2
   FY27 results and call are out (expected ~Nov-2026); this resolves LBF1
   and the stated falsification line.
2. Confirm whether the Q1 FY27 flat large healthcare customer is the same
   account Q3 FY26 described as growing 50%, check the account identity
   against later investor-deck footnotes or an IR query.
3. Retrieve the SessionM purchase price allocation and goodwill/intangible
   split from the Q2 FY27 results notes (BSE, expected ~Nov-2026).
4. Verify the composition of the roughly USD 18m gap between the USD 20m
   SessionM headline price and the roughly Rs 17 Cr net price cited on the
   Q1 FY27 call (deferred revenue, assumed liabilities, or another debt
   true-up item).
5. Independently verify Chairperson Neelam Dhawan's cross-board Audit/
   Stakeholders Relationship Committee count (12, per the FY26 AR and AGM
   Annexure-A) against the SEBI/MCA registry for a Regulation 26(1)
   compliance read this container cannot perform.
6. Track the KPMG forensic audit findings and the insurance recovery
   quantum against the Rs 33.4 Cr Q1 FY27 exceptional loss, expected via
   Reg 30 filing in H2 FY27.
7. Confirm whether Gowthami Agro Industries (a promoter-group entity) is
   named in any Andhra Pradesh SIT chargesheet beyond the disclosed
   information notice (UDRHP-I p.4461-4464).
8. Verify management's claim that loyalty software is under 10% of the
   overall loyalty market (the TAM-denominator claim underlying B09's
   market-definition choice) against a named third-party source, since no
   peer transcript corroborates it (B06 unverifiable).
9. Verify whether 110%+ net revenue retention is genuinely "top-decile" for
   global SaaS against an independent SaaS benchmark report; no peer
   transcript corroborates this either (B06 unverifiable).
10. Confirm further CTIPL or PE-holder block sales via SAST Reg 29 filings
    and the next quarterly shareholding pattern (Sept-2026 quarter, due
    ~Oct/Nov 2026).
11. [Chain 1 pending link] Identify the named System Integrator or
    consulting partner(s) behind the ~40% of FY26 new-logo referrals; no
    partner is named anywhere in the AR or the four investor presentations
    reviewed.
12. [Chain 2 pending link] Search Mastercard's own SEC filings (8-K, 10-Q)
    around Feb-May 2026 for any disclosed SessionM divestiture
    consideration or revenue figure that could independently corroborate or
    contradict Capillary's USD 32m ARR claim.

### 4e. Second-order stub (Master Prompt v3.7, Rule F)

Two chains, drafted from corpus, off the two dominant variables the
evidence base can carry furthest today. Claude web extends this stub to the
Rule F floor of five, with live-web links, before Role 2.

```
CHAIN 1: ~40% of FY26 new customers were referred by System Integrators and
Consulting Partners (AR "Business Strategy and Growth Drivers," p.79-80; B09
downstream candidate).
Link 1 [FILED]: The AR states, without naming a partner, that roughly 40%
of FY26 new-logo customers were referred through Systems Integrator and
Consulting Partner relationships.
Link 2 [FILED]: No named SI or consulting partner, no referral-fee or
revenue-share arrangement, and no partner-program agreement terms appear
anywhere in the AR notes or the four investor presentations reviewed (B04
gap: no named channel partner found in this corpus).
Link 3 [INFERENCE]: If SIs and consulting partners are paid a referral fee
or margin share for steering enterprise loyalty-platform mandates to
Capillary, that cost likely sits inside the disclosed professional/
consultancy expense line (14.7% of FY26 revenue, AR p.190) rather than as
a separately disclosed distribution cost, meaning the "40% of new logos
via SI referral" channel could be a paid-distribution arrangement, not an
organic reputation referral, and its true cost per referred logo is not
visible in any filed number.
Binding constraint: whether the SI/consulting-partner channel can hold or
grow its ~40% share as Capillary's own direct sales motion scales, or
whether it is capped by how many SIs are willing to carry a smaller
vendor's loyalty product alongside their own larger platform mandates.
Unsaid: the AR names no specific SI or consulting partner anywhere in this
corpus (a search for large global SI/consulting names found none), so the
channel's durability rests entirely on an unnamed set of relationships.
Observation that confirms or breaks this chain, and confirm-by date: a
named SI/consulting-partner-program announcement, or a Reg 30 filing naming
a partner, by the Q2 FY27 results date (~Nov-2026). PENDING LIVE
VERIFICATION, named for claude.ai: search "Capillary Technologies" plus
"systems integrator" or "consulting partner" press releases, and re-check
the two Q1 FY27 investor decks (Investor_Presentation_1.pdf,
20260804-Investor-Presentation-30pp.pdf) for a named-partner slide.

CHAIN 2: SessionM Inc., plus its Czech step-down subsidiary, acquired from
Mastercard International Incorporated for a total consideration of USD
20.00 million, transaction completed 01-May-2026 (AR Note 44, consolidated,
p.259).
Link 1 [FILED]: The Q1 FY27 concall cites a net price of about Rs 17 Cr
after a debt true-up management did not fully explain on the call, against
the USD 20m headline consideration (B12b MAJOR finding 5; roughly USD 18m
unexplained).
Link 2 [FILED]: The AR's own Kognitiv purchase price allocation (Note 39,
p.254) allocated 62% of that deal's consideration to goodwill, mainly
"assembled workforce and estimated synergies," against Rs 390.37mn to
customer relationships and Rs 172.43mn to IP, the only filed comparable
for how a Capillary loyalty-tech acquisition's PPA has actually split.
Link 3 [INFERENCE]: If SessionM's PPA follows the Kognitiv template, most
of the USD 20m consideration will land in goodwill rather than in an
identifiable customer-relationship or technology intangible, which means
the "USD 32m ARR, profitable within two months" claim (management's own
framing, B05) is not yet backed by a disclosed acquired-revenue valuation
exhibit; the ARR figure currently rests on management's word alone.
Binding constraint: whether Mastercard, as a US-listed seller under its own
disclosure regime, discloses a SessionM revenue or ARR figure anywhere that
could independently corroborate or contradict Capillary's USD 32m claim.
Unsaid: the AR's only mention of SessionM is the single post-balance-sheet
event sentence in Note 44; it gives no revenue, customer-count basis, or
explanation for why "40+ logos" (Q4 FY26 call) became "45-odd customers"
(Q1 FY27 call) without comment (B12b MAJOR finding 4).
Observation that confirms or breaks this chain, and confirm-by date: the
SessionM purchase price allocation and goodwill/intangible split, due in
the Q2 FY27 results notes (~Nov-2026). PENDING LIVE VERIFICATION, named for
claude.ai: search Mastercard's SEC filings (8-K, 10-Q) around Feb-May 2026,
and Mastercard's own investor relations site and SEC EDGAR, for any
disclosed SessionM divestiture consideration or revenue figure.
```

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in
claude.ai with live web, before Role 2.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. Capillary sells cloud software that runs loyalty programmes for big
   brands, like a digital punch card kept on the brand's behalf.
2. The software also holds the points ledger itself: every point a shopper
   earns, spends or loses to expiry lives inside Capillary's system.
3. Nine tenths of FY26 revenue was subscription. The rest was one-time
   setup fees and small campaign-management fees run as agent.
4. Buyers are about 415 large brands in 49 countries, in retail, banking,
   telecom, travel, hospitality and healthcare. About 20 are Fortune 500
   names.
5. The top 10 customers made 58.71% of FY25 revenue. The company has not
   disclosed the FY26 figure; the disclosure note meant to carry it is
   incomplete in the filed annual report.
6. Brands buy loyalty software instead of running loyalty in-house because
   Capillary's own cited data says winning a new customer costs five times
   more than keeping one.
7. Growth is meant to come from two places: software taking share from
   loyalty agencies, and Capillary buying smaller loyalty companies and
   moving their customers onto its own platform.
8. No independent source in this run's evidence confirms that loyalty
   software is under a tenth of total loyalty spending, which is the claim
   behind management's stated market size.
9. The moat sits in the subscription line: once a brand's points ledger and
   nine average system integrations live inside Capillary, switching is a
   hassle.
10. The moat does not sit in the acquisition strategy itself: a
    well-funded rival could run the same buy-and-migrate playbook without
    giving up anything of its own.
11. The mental model in one point: this is a business moving from unproven
    capital returns toward a claimed high-margin, high-retention endpoint,
    and the number that decides whether that move is real is organic
    revenue growth once currency is stripped out, a number management, an
    analyst and the company's own guidance arithmetic currently disagree
    on.
12. The fragility read is FRAGILE: several of the variables the bull case
    needs are reported by the company alone, not checkable outside its own
    calls, and those numbers have moved between calls without explanation.
13. The corpus could not establish the FY26 top-10 customer share, the
    SessionM purchase price breakdown, or a clean reconciliation of the
    company's 8.82% return on capital against an independent recomputation.
14. The corpus also could not confirm whether the healthcare customer that
    stayed flat in the most recent quarter is the same customer that grew
    50% two quarters earlier.
15. The two biggest open questions for the operator: is organic growth
    really near 17%, or closer to the low single digits once acquisitions
    are stripped out; and will the goodwill sitting on the balance sheet,
    tested at a high discount rate with no stated safety margin, hold up as
    two more acquisitions get folded in.

---

## SECTION 6: STANDING EXTRACTION ANNEX

Ten standing questions, answered from the corpus in quote-then-comment
form. Every quote carries filename and page anchor. NOT DISCLOSED is
written where the corpus does not carry an item.

**1. UNITS.**
Quote: "Capillary sales long-term subscription contracts, typically running
3-7 years with many renewing them subsequently, priced on the number of
members or transactions on the platform rather than on user seats or gross
merchandise value." (Annual_Report_2026.pdf, p.76, MD&A "Business Model")
Comment: this is a basket description, not a per-unit figure. No average
revenue-per-member, per-transaction, or per-customer rupee figure is
printed anywhere in the AR or the four investor presentations reviewed
(B04 3D: "Revenue per unit: NOT FOUND"). The closest disclosed proxies are
total subscription revenue (Rs 6,562.00mn, 89.3% of FY26 revenue from
operations, AR p.190) and CAC as a percentage of new ACV (16.9% FY26, down
from 17.9% FY25, AR p.79-80), from which a rupee-per-customer figure could
be derived only against an undisclosed customer count.

**2. SEGMENT CAPITAL AND DEBT.**
Quote: "CODM evaluates the performance of the Group based on the single
operative segment as cloud based intelligent customer engagement software
solutions to retail chain operators ('CRM Services'). Therefore, there is
only one reportable segment called CRM services in accordance with the
requirement of Ind AS 108 'Operating Segments'." (Annual_Report_2026.pdf,
consolidated Note 33, p.[251] area; standalone equivalent p.[122] area)
Comment: because the Group and the Company each report one segment, no
segment-level split of assets, liabilities, capital employed or borrowings
exists to disclose; none is required under Ind AS 108 paragraph 4 once a
single segment applies. The whole-entity figures stand in for a segment
figure: total consolidated borrowings (current + non-current) fell from
Rs 1,000.94mn (FY25) to Rs 447.21mn (FY26) (B03 Phase 3B, AR Balance Sheet
p.189); none of it is segment-allocated, because there is only one segment.

**3. GUIDANCE VERSUS ASPIRATION.**
- (a) Guidance with a period: "FY27 revenue guidance Rs 1,000-1,050 Cr"
  (Q4 FY26 call, B05 guidance table), later sharpened to "will definitely
  beat Rs 1,065 Cr revenue and Rs 172 Cr EBITDA" (Q1 FY27 call). Comment:
  a dated, numeric guide, twice reaffirmed and once sharpened.
- (a) Guidance with a period: "New ACV full year at least 30-40% more than
  FY26's Rs 121 Cr" (Q1 FY27 call, B05 guidance table). Comment: dated to
  FY27; the FY26 Rs 121 Cr base itself was not found stated in the
  transcript by Verifier B (B12b MAJOR finding 8), so the guide's own
  denominator is unverified in this corpus.
- (b) Aspiration without a period: "Steady-state EBITDA margin 25-30%+ (70%
  gross margin, ~15-16% tech, similar S&M, 5-7% G&A)" (Q4 FY26 call, B05
  guidance table). Comment: no date attached; a destination, not a
  forecast.
- (b) Aspiration without a period: "Rule of 40 (revenue growth % + EBITDA
  margin %) target of at least 40" (AR MD&CEO letter, p.[9]). Comment:
  ongoing target; FY26 achieved 38, a shortfall the company names itself
  rather than rounding away (B03 4D).
- (c) Capacity/capability only: "aiRA target 5-10% of revenue; current
  run-rate $2-2.5m ARR" (Q1 FY27 call, B05 guidance table). Comment: framed
  as a target share of FY27 revenue, but the current base is a usage-metric
  pilot, not yet a comparable run-rate disclosure across quarters (B12b
  MAJOR finding 3 notes the sizing basis itself shifted between calls).

**4. CONCENTRATION.**
Quote: "Revenue from one customer for March 31, 2026 and March 31, 2025
that individually accounted for more than 10% of the total revenue."
(Annual_Report_2026.pdf, consolidated Note 36(iii), p.246-247), the
sentence ends there, with no name, amount, or "Nil" following. Comment:
confirmed genuine drafting gap by independent re-reads at both B02 and B03;
not an extraction artefact. Top product share: NOT DISCLOSED (single Ind
AS 108 segment, no product-line revenue split, AR p.78). Top customer
share: NOT DISCLOSED for FY26. The only concentration figure on record is
the stale FY25 UDRHP-I figure: top 10 customers = 58.71%, top 5 = 43.35%
(UDRHP-I p.40-41). Geographic concentration is disclosed: USA 55.6%, UK
15.4%, Others 29.0% of FY26 consolidated revenue (AR Note 22, p.232-233).

**5. PROMISE LEDGER.**

| Promised in | Promise | Delivery status | Evidence anchor |
|---|---|---|---|
| Q3 FY26 call | Tech + corp cost keeps falling as % of revenue | Delivered (directionally) | Q4 FY26 EBITDA margin 14.7%; organic margin ~23% by Q1 FY27 (B05) |
| Q3 FY26 call | OCF/adjusted EBITDA normalises to 105-110% | Missed / unreconciled on the stage's own reading; Verifier B rates this OVERSTATED, management's Q4 answer ("we bill and collect money upfront in a healthy growing business") treats 105-110% as a norm, not a promise | Q4 FY26 call, Anant [p10] L409-412; B12b finding 19 |
| Q4 FY26 call | Q1 FY27 margin softness expected from salary hikes | Occurred as guided; the stage's "delivered, better than guided" label is wrong per Verifier B, margin fell from ~19% (Q4) to 17% (Q1), the guided softness | Q4 FY26 [p6] L250-251; Q1 FY27 [p8] L316; B12b finding 18 |
| Q4 FY26 call | SessionM break-even Year 1, positive margin Year 2 | Cash-positive within two months (Rs 5-6 Cr), which is a cash result, not an EBITDA result; the stage's "ahead of schedule" label overstates this per Verifier B | Q1 FY27 [p7] L270-273; B12b finding 20 |
| Q4 FY26 call | FY27 revenue guidance Rs 1,000-1,050 Cr | On track / reaffirmed and sharpened | Q1 FY27 ARR Rs 1,026.6 Cr; guidance sharpened to "will definitely beat" Rs 1,065 Cr |
| Q3 FY26 call | AI/agentic wave will not disrupt Capillary's system-of-record position | Reaffirmed, no contradicting evidence found | Q1 FY27 call, expanded framing |
| Q3 FY26 call | aiRA monetisation clarity "in a couple of quarters" | Partial; sizing basis shifted quarter to quarter (4-5% of revenue in Q4 vs $2-2.5m run-rate, <10 paying customers in Q1) | B12b MAJOR finding 3 |
| Q4 FY26 call | Kognitiv AI-led upgrade cycle, a "12-to-18-month type period" | Partial; Q1 FY27 gives longer concrete dates (first customer live Sep-2026, full completion latest Sept 2027, ~28 months from the May-2025 deal) | B05 timeline_slippages |

Comment: Verifier B's independent read lowers the stage's B credibility
grade to B-minus/C-plus, on the basis that four figures (organic growth,
aiRA sizing, SessionM base, gross margin) moved between calls without
acknowledgement, on top of the promise-ledger items above (B12b).

**6. RESTATED BASES.**
Quote: "In its measurement of EBITDA, the Group includes other income but
does not include depreciation... as a separate line item on the face of
the restated Consolidated Statement of Profit and Loss." (Annual_Report_
2026.pdf, consolidated, p.[199] area, line 15218-15220 of the extracted
text) Comment: the word "restated" here is a labelling carryover from the
IPO/UDRHP drafting template. No actual prior-year figure was found restated
anywhere in the note set on independent re-read (B02 Pass 3, finding 4);
standalone Note 40 (p.177) carries only standard "regrouped/reclassified
wherever necessary" boilerplate, and the FY25 comparatives printed in the
FY26 AR match the figures Company Memory and the earlier UDRHP carry for
that year with no reclassification note attached.

**7. CORPORATE-ACTION CLAUSES.**
Quote (SessionM, the one in-corpus scheme of this kind): "On February 24,
2026, Capillary Technologies LLC entered into a Share Purchase Agreement
with Mastercard International Incorporated for the acquisition of all
issued and outstanding common stock of Session M Inc. (Delaware, USA),
together with its wholly owned subsidiary, SessionM Czech Republic s.r.o.,
for a total consideration of USD 20.00 millions. As part of the
transaction, SessionM Czech Republic s.r.o. has been transferred to
Capillary Pte. Ltd. The transaction is completed with effect from May 01,
2026." (Annual_Report_2026.pdf, consolidated Note 44, p.259) Comment: this
gives the parties, the appointed date (24-Feb-2026 agreement), the
effective date (01-May-2026), and the consideration (USD 20.00m), but no
liability-allocation clause, no earn-out or indemnity ratio, and no
purchase price allocation, those are NOT FOUND in this AR (it predates
closing by five days) and remain PENDING LIVE VERIFICATION against the Q2
FY27 results notes. The one filed comparable with full allocation detail is
Kognitiv: "the Group acquired a 100% equity interest in Kognitiv Solutions
Inc., for a purchase consideration of CAD$ 23.44 million (₹1,447.43
million)" with "the resultant goodwill amounting to US$ 10.75 million
(₹909.53 million)" (Annual_Report_2026.pdf, consolidated Note 39/Auditor's
KAM, p.254 and p.[180-181]), 62% of consideration to goodwill against
Rs 390.37mn to customer relationships and Rs 172.43mn to IP (B02/B03).

**8. RELATED-PARTY PERIMETER.**
Quote (segment relevant to promoter perimeter): "As on March 31, 2026,
Capillary Technologies International Pte. Ltd. ('CTIPL') which holds 39.47
million equity shares together with its..." (Annual_Report_2026.pdf,
Board's Report §7, p.[34] area, line 3690-3692), CTIPL held 49.70% of the
Company at FY26-end, having ceased to be a "holding company" on listing but
continuing as promoter. Direct promoter-entity RPT for FY26 (AR Note 32,
Standalone, p.166-168, per B08): other non-operating income Rs 19.93mn
(FY25: Rs 13.67mn); other receivables Rs 30.57mn; trade payables Rs 41.86mn;
nil interest on borrowings; nil corporate guarantees taken from CTIPL.
Comment: no royalty, management fee, above-market rent, promoter loan, or
guarantee to a promoter-controlled entity was found in either the
standalone or consolidated RPT notes (B08 verified clean on direct
self-dealing). The dominant RPT fact in this corpus is structural, not
promoter-driven: standalone revenue is 75.7% related-party through
Capillary Pte Ltd, Singapore (a subsidiary, not a promoter entity), with
the FY26 transfer-pricing study still "in process" at the 06-May-2026
sign-off date (AR Note 20/32, p.155-156, p.166-168).

**9. PLEDGE AND SHAREHOLDING.**
Quote: "Whether any shares held by promoters are pledge or otherwise
encumbered? | No" (BSE-SHP-summary-Jun2026.txt, BSE Reg 31 shareholding
pattern summary, quarter ending June 2026). The same "No" appears in the
Dec-2025 and Mar-2026 summaries (B08 pledge_trend). Comment: only three
quarters of filed BSE data exist since the 21-Nov-2025 listing, not twelve;
a 3-year/12-quarter trend is not computable (B01 input_gaps). Promoter and
Promoter Group held 51.45% as at Jun-2026 (4,08,86,138 shares of
7,94,71,983 total), with 1,60,32,800 shares (39.21% of the promoter block)
still locked in, consistent with the 18-month minimum-promoter-contribution
tranche running to roughly May-2027 (BSE-SHP-summary-Jun2026.txt; B08).
Institutional holding: promoters 51.45%, DII 19.38%, FII 3.34% per Company
Memory (step1-business-brief.md, screener, weighed not anchored); the BSE
Reg 31 summary itself does not split FII from DII (B00 input gap).

**10. VERIFICATION.**
Documents quoted in this annex: Annual_Report_2026.pdf (FY 2025-26, signed
06-May-2026, Reg 34 filing); UDRHP-I (Capillary-UDRHP-I-SEBI-Jun2025.pdf,
SEBI, June 2025); BSE-SHP-summary-{Dec2025,Mar2026,Jun2026}.txt (BSE Reg 31
shareholding pattern summaries, retrieved 2026-09-19); Concall_Feb_2026_
Transcript.pdf, Concall_May_2026_Transcript.pdf, Concall_Aug_2026_
Transcript.pdf (Q3 FY26, Q4 FY26, Q1 FY27 earnings calls).

CORPUS COMMIT HASH: 281ce41dcbf55ff5ebc8fe2bd7849c9ebde8e072
