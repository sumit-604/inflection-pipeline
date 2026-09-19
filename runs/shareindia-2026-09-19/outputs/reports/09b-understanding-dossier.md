# SHAREINDIA: HALT 1 UNDERSTANDING DOSSIER

Share India Securities Ltd (NSE SHAREINDIA, BSE 540725). Run date 2026-09-19.
Step-1 intake run (operator standing ruling 2026-09-05). Assembly-only from
committed blocks B00-B09, verifier blocks B12a-B12d, confidence.yaml and
B13-synthesis-lite. No new research. No valuation, price, or verdict
vocabulary except the one scoped exception named in Part B4 below.

This dossier is the Halt 1 deliverable. It carries no KILL/SHALLOW/PROCEED
recommendation. The operator makes that call after reading it.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

**1. Concalls.** Three transcripts held: Q3 FY26 (30-Jan-2026), Q4 FY26
(23-May-2026), Q1 FY27 (31-Jul-2026) (B00 inventory.concalls). Most recent
quarter covered: Q1 FY27 (quarter ended 30-Jun-2026). Given the run date
(19-Sep-2026), Q2 FY27 (quarter ended 30-Sep-2026) has not yet closed, so no
transcript is plausibly missing at this run date.

**2. Annual reports.** One AR held: FY26 (filed 05-Sep-2026, 335pp) (B00
inventory.annual-report). The latest completed FY (FY26) is present. Only one
year is held in inputs/annual-report/; a FY25 AR is preserved in inputs/other/
but is not a primary source per run instructions (B03 input_gaps). Fewer than
3 years of AR are held as primary corpus; the 11-year Gate 0 financial series
(B01 data_years/fy_range) comes from screener CSVs, not from multiple ARs.

**3. Results filings.** Three quarterly results held: Q1 FY27
(24-Jul-2026), Q4 FY26/FY26 audited (19-May-2026), Q3 FY26 (27-Jan-2026)
(B00 inventory.results). Q2 FY26 results are held in inputs/other/ only,
the contract caps results/ at the 3 most recent (B00 input_gaps). Latest
results filing (Q1 FY27, 24-Jul-2026) is one quarter ahead of the AR
(FY26, filed 05-Sep-2026 but covering the year to 31-Mar-2026); no
quarter-gap between the two.

**4. Investor presentations.** Three held: Q1 FY27 (27-Jul-2026), Q4 FY26
(20-May-2026), and one dated 20-Mar-2026 (B00 inventory.presentation).
Latest held is Q1 FY27, 27-Jul-2026.

**5. Research / rating.** No broker note or independent research note held
(research/ is empty; B00 inventory.research count 0). Rating material held:
the Sep-2026 Infomerics Reg 30 letter and rationale (16/18-Sep-2026) plus the
prior detailed rationale it refers to (22-Sep-2025) (B00 inventory.rating).

**6. Corporate actions.** 99 announcement filings held, 97 Reg 30 filings
19-Sep-2025 to 18-Sep-2026 plus scheme-of-arrangement updates from Jul-2025
and the SEBI settlement order text (B00 inventory.announcements).

**7. Freshness pair check.** Per B00 freshness_pairs: RESULTS-to-CONCALL
PASS; RATING BULLETIN-to-RATIONALE PASS; AR-to-LATEST-AUDITED-RESULTS PASS.
One pair FAILED: SEBI ORDER to ORDER TEXT (NSE co-location adjudication).
Trigger document held: the 21-Aug-2026 NCLT scheme-of-arrangement filing,
whose pending-litigation annexure names a SEBI Adjudication Order against
Share India Securities Ltd in the NSE co-location matter, dated on or about
30-May-2022, Rs 3 lakh penalty. The order text itself (expected source:
sebi.gov.in > Enforcement > Orders > Orders of AO, May-2022) is absent from
the corpus; an automated search did not locate it and SEBI's search endpoint
blocked the request (B00 freshness_pairs, amended after stage 8).

**8. Verdict line: CORPUS GAPPED-FRESHNESS.**
Missing mate document (freshness-pair failure): SEBI Adjudication Order,
NSE co-location matter, ~30-May-2022, Rs 3 lakh penalty (findable, expected
source sebi.gov.in).
Other gaps, all findable-but-missing:
- research/ is empty: no broker note or rating-agency research note
  collected (expected source: broker platforms, rating agency sites).
- Aug-2026 warrant-allotment filings (21-Aug-2026, 27-Aug-2026) returned
  HTTP 403 on direct fetch; the allottee identity is unresolved (expected
  source: BSE).
- Silverleaf Capital Services Pvt Ltd pre-merger shareholder list is not
  named in the NCLT order (expected source: MCA register / NCLT case file).
- BSE SHP promoter-level pledgee-name and FII/DII split detail tables were
  not fetchable (expected source: BSE API/portal).
- Screener Financials.xlsx (Data_Sheet) is absent; the collector's screener
  session was logged out (expected source: screener.in with a logged-in
  session, or company IR page).
Two folders are empty and, per the Step-1 AUTONOMY CONTRACT, their absence
was accepted rather than paused on: **research/** (empty, no broker notes)
and **prospectus/** (empty, not expected for a long-listed company). The
empty-folder confirmation prompt was SUPPRESSED under the operator's
standing answer "proceed with the gaps" (B00 empty_folder_confirmation).
This verdict caps the phase-1 gate recommendation at PROCEED WITH CAVEATS
per the orchestrator rule, and is not softened by the REWORK verdict
already active for other reasons (B13 verdict, freshness_cap line).

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT - PENDING OPERATOR SIGN-OFF.** Signing happens only in claude.ai
after live-web stress-testing. Nothing below is a signed model.

### PART A: THE FROM STATE

**A1. Archetype (per line).**
- Proprietary trading book (58.3% of FY26 consolidated income, Note 31;
  B04 revenue_streams): fits no archetype in the CLAUDE.md library cleanly.
  Closest unnamed pattern is a market-maker/prop-trading desk (B04
  FLAG-ARCHETYPE-GAP analyst_note).
- NBFC lending (Share India Fincap, MTF book): Lender archetype (AUM
  growth, NIM, asset quality, RoA/RoE), cleanly evidenced KPIs (B04
  analyst_note; NIM 17.64% FY26, AR p.74).
- Digital/algo platform (uTrade Algos, Algowire, Silverleaf): Platform/
  network archetype, self-asserted, unverified against peers (B04
  moats_present; B07).
- Broking, merchant banking, wealth/PMS/AIF, insurance distribution
  (11.1%+0.6% of FY26 income, fee/commission and service lines): fits no
  single archetype; closest is Outsourcing partner-style fee-for-service,
  weakly evidenced (B04 revenue_streams).

**A2. The simple analogy.** Share India runs a trading desk that bets its
own capital in the derivatives and commodity markets, and that desk earned
most of the group's profit in FY26. Beside it sits a more familiar broking
and lending business: it lends money to clients who want to buy more shares
than their cash allows (margin trading), lends through a small finance
company, takes commissions for executing trades and distributing mutual
funds and insurance, and sells its own trade-automation software to other
traders. The trading desk's profit swings with the market. The broking and
lending side earns fees and interest that should be steadier, but it is the
smaller engine today.

### PART B: THE TRANSITION

**B1. FROM to TO.**
Line: group revenue and profit mix (prop trading vs client/annuity
business).
FROM: R1 COMMODITY PRICE-TAKER neighbourhood, the prop-trading engine
takes the market's price, has no pricing power, and its 58.3% income share
means group ROCE moves with market direction, not with a durable spread
(B04 pricing_power "weak"; cyclicality "cyclical").
TO (claimed): R3 VALUE-ADDED / SPEC'D SUPPLIER neighbourhood, specialised
for this hybrid, institutional broking relationships, a scaled MTF book,
and wealth/PMS/AIF fee lines that management says will carry 55-70% of
profit within one to three years (B05 guidance: "client 60% / prop 40%"
by end FY27; "client 70% / prop 30%" in 3 years). The NBFC sub-line sits
on its own lender ladder (AUM, NIM, asset quality) and has NOT climbed in
FY26: revenue -2.4%, EBIT -5.7%, branch count 80 to 73 (B04 revenue
streams; B07 top_moat_risks).

**B2. The engine.** Two things must physically change: (1) fee and
commission income must grow as a rising share of total income while prop
fair-value gains fall as a share: in FY26 fee income instead FELL 12.7%
standalone / 18.6% consol (B04 FLAG-DISCLOSURE-CONTRADICTION); (2) the
MTF/NBFC book and the new branch network must scale on disciplined,
disclosed credit quality, and the PMS/AIF/institutional lines must convert
management's stated targets into filed Rs Cr revenue, not volume or
subscriber counts (B07 optionality_register; B09 flags).

**B3. The proof gate.** A single, consistently-defined revenue AND profit
split between prop and client business (not a volume metric), disclosed
the same way for two consecutive quarters, showing the prop share of
profit falling from its current ~52% (Q4 FY26 and Q1 FY27 concalls, per
B12b) toward management's own 45% end-FY27 target, together with fee and
commission income returning to positive year-on-year growth (B05 trigger
priority 3, confirm_signal; B13 falsification_metric). On the evidence
assembled through phase 1, this gate has NOT fired (B13
transition_posture: "proof gate NOT FIRED on phase 1 evidence").

**B4. The recognition gap: OPEN QUESTION, resolved at Stage 11.**
Whether the market already prices SHAREINDIA at a level consistent with
the claimed client-annuity TO state, or still at a level consistent with a
prop-trading-dependent FROM state, is not concluded here. Company memory
(step1-business-brief.md, screener, 18-Sep-2026) notes a trailing PE near
13.7x against a 0% three-year profit CAGR; whether that multiple already
reflects, discounts, or simply ignores the claimed transition is the PE-gap
question Stage 11 resolves through the Section 1B destination-PE framework,
not here. No number, no fair value, and no conclusion is stated on this
question in this dossier.

**B5. The ugliness test.** Classification: **STRUCTURAL-FEATURE**, not
ARTIFACT-OF-CLIMB, on the evidence assembled. Reasoning: cash conversion
has been negative in 3 of the last 4 years and cumulative CFO/PAT is 0.085x
over 11 years, worsening not improving (B01 block_b_trend; B03 FLAG-CASH);
contingent liabilities rose 48% YoY to 122.7% of net worth, scaling with
the prop book rather than a finite build (B02 top_findings rank 6);
promoter pledge sits above 40% of promoter holding in every available
quarter and rose sharply in the most recent one, unexplained (B08
pledge_trend); a live, undisclosed SEBI show-cause notice and an MCX
penalty sit inside the exact activity (proprietary trading) the transition
needs to shrink (B08 adverse_findings); and the prop share of profit has
NOT moved off ~52% across the two most recent quarters despite the stated
target (B12b MAJOR finding). None of these read as a temporary optic of a
real climb already underway; they read as features of how this group is
currently built and funded. This classification is a finding for the
value-trap test at Stage 13/Role 3 to carry; it is not a trade verdict.

**B6. The transition falsifier.** A further one to two quarters where the
prop share of profit, measured on one consistent basis, does not decline
below its current ~50-52% level, combined with a second consecutive year
of decline in fee and commission income (B04 must_track_metrics; B13
falsification_metric: Q2 FY27 consol fee income YoY). This is distinct
from what would kill the underlying business (Part C3).

### PART C: WHAT THE MODEL WATCHES

**C1. Dominant variables** (derived from B2/B3, not the static snapshot):
1. Fee and commission income YoY growth (client engine health; fell
   12.7%/18.6% FY26, B04 must_track_metrics).
2. Prop share of profit/revenue on a single, consistent basis (currently
   ~52% and flat across two quarters against a 45% end-FY27 target,
   B12b MAJOR finding).
3. MTF book growth against management's own restated targets (book grew
   3% in six months against a target restated three times, B12b MAJOR
   finding; B05 triggers priority 1).
4. Cash conversion and debt/rating access (CFO negative 3 of 4 years;
   Infomerics ISSUER NOT COOPERATING since 22-Nov-2024; NCD
   holders' meeting adjourned Aug-Sep 2026; B00 LBF3/LBF4; B08).
These four become the Role 5.5 tracker signals.

**C2. What the model rejects.** Total addressable market size for the
client-annuity pool is not the binding constraint: B09 finds revenue
headroom of 8.3x within a Rs 3,650 Cr SAM and a STRONG runway class, while
the one clean filed trend (fee income) is currently moving the opposite
direction from the SOM math's assumed 1.4-2.9pp of share gain (B09
FLAG-TREND-CONTRADICTS-SOM-DIRECTION). The model treats market-size
questions as noise; execution and funding access are the binding
constraints. Similarly, the overall revenue growth headline (+1.5% FY26)
is rejected as a standalone signal because it can move purely on
trading-book mark-to-market, unrelated to franchise growth (B04
irrelevant_ratios).

**C3. The business falsifier** (distinct from B6, the transition
falsifier). A funding-access shock that forces the group to shrink its own
balance sheet: a failed or unfavourable NCD redemption/refinancing,
continued or deepened Infomerics ISSUER NOT COOPERATING status blocking
bank or NCD access, or an adverse order in the still-open SEBI show-cause
notice or MCX appeal that touches the prop book's capital base, would
force a re-declaration of the FROM business itself as capital-constrained,
not merely prop-trading-dependent (B00 LBF4; B08 verdict CONCERN; B02/B03
FLAG-CASH). This kills the starting business's current operating model,
not just the transition narrative.

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

*(Drafted at Halt 1 from B01-B09, per the shared spec in
prompts/13-synthesis-pipeline.md. Stage 13's copy, already produced in this
run as outputs/final/business-narrative.md, is the current version of
record; reproduced here unchanged, assembly-only.)*

Share India is a Noida capital markets group, and its largest income line
is trading its own money in equity, derivatives and commodity markets.
That proprietary book produced 58% of FY26 income as fair value gains. A
further 9% came from gross sales of securities held as stock in trade,
which is the same trading economics reported gross. Neither line has a
customer behind it; the buyer is the market on the other side of each
trade. Interest income, 18% of FY26 income, comes from margin trading
loans against clients' shares and from the Share India Fincap NBFC, which
lends to retail and small business borrowers. Fees and commissions, 11% of
income, pay for trade execution, depository accounts, mutual fund and
insurance distribution, merchant banking and portfolio management. The
customers are retail, HNI and institutional traders, margin and NBFC
borrowers, and companies that raise capital, and institutional clients
rose from 154 to 212 over three quarters. No filing shows switching costs
or network effects, so a trader can move to another broker at will.
Present demand follows exchange activity, which the NSE and BSE monthly
cash and F&O average daily turnover and options premium turnover series
track, together with the SEBI active derivatives trader count. SEBI F&O
circulars and the RBI intraday funding and bank guarantee circular set how
much of that activity, and how much prop desk capital, the rules allow.
Demand for the client lines should grow with NSDL and CDSL demat account
additions, AMFI mutual fund AUM and SIP flows, and SEBI DRHP and SME
platform IPO listing counts, all public series. The company's own growth
plan rests on margin lending, 25 to 30 new Tier 3 branches over two years,
PMS and AIF fees and institutional broking, and peer disclosed MTF book
sizes and interest rates are the outside check on the lending bet, while
Infomerics rating cooperation status is the check on the debt that funds
it. The prop trading line has no moat, because it takes the price the
market sets. Broking has weak pricing power, and fee income fell 13%
standalone and 19% consolidated in FY26. Margin lending and the NBFC price
on credit risk, not brand, and the NBFC's revenue and branch count both
fell in FY26. The SEBI and RBI licences are a real entry barrier, but
every licensed peer shares them. The emerging moat scan found two moderate
signals, rising institutional client counts and uTrade algo platform
subscriptions at 6,543 paid users, but neither has a disclosed rupee
revenue figure, and the scan scored about 10, below the lowest band of 12,
so the run found no meaningful emerging moat.

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. Verticals framed (one per dominant variable, Section 2 C1)

**Vertical 1: Fee and commission income growth.** Corpus establishes: FY26
fee and commission income fell 12.7% standalone / 18.6% consolidated
(B04), in the same year the AR's own MD&A claims reduced prop-trading
dependence (B03 red_flags_top3). Corpus cannot establish: a monthly or
even reliable quarterly decomposition of WHY fees fell (client attrition,
pricing pressure, or mix shift within fee lines), the AR gives only an
annual note. Questions that decide it: (1) does Q2/Q3 FY27 fee income
resume growth on a standalone basis? (2) is the FY26 fall concentrated in
one fee line (broking vs distribution vs merchant banking) or broad-based?
(3) does peer fee-income growth (SMC Global, Choice International) move
the same direction over the same period, i.e. is this industry-wide or
company-specific (B06 industry_cross_read)?

**Vertical 2: Prop share of profit/revenue on a consistent basis.**
Corpus establishes: the AR's segment note reports broking/trading as one
undifferentiated line (93.2% of FY26 segment revenue, Note 45), and the
BRSR Annexure 7 discloses 73.47% of turnover from Trading in Securities vs
15.19% from broking (AR printed p.84-85), both structurally unable to
give a profit-level split (B02 rank 1; B03). Corpus cannot establish: a
profit-level, consistently-defined prop/client split on a quarterly
cadence; management's own concall framing shifts unit (volume, turnover,
profitability) every quarter (B05 red_flags HIGH). Questions that decide
it: (1) will management disclose revenue AND profit, not volume, on one
basis for two consecutive quarters? (2) does the FY27 AR's BRSR Annexure
move the 73.47%/15.19% split, and in which direction? (3) can the segment
note ever be restated to separate prop from client within the broking/
trading line?

**Vertical 3: MTF book growth against restated targets.** Corpus
establishes: the two-year MTF target has been restated three times across
three quarters (Rs 900-1,000 Cr from Jan-2026; Rs 650 Cr for FY27; Rs
1,000 Cr from Jul-2026), while the book itself grew from Rs 457 Cr to Rs
424 Cr (seasonal dip) to Rs 470 Cr (B05 guidance; B12b MAJOR finding: book
+3% in six months). Corpus cannot establish: the book's credit-quality
detail (it carries a NIL impairment allowance and remains always-Stage-1
across two years of 69.8% growth, untested against the group NBFC's 4.30%
GNPA, B02 red_flags). Questions that decide it: (1) does the book cross
Rs 500 Cr, the confirm_signal midpoint, on a sustained basis? (2) does
management stop restating the target basis (years-from-date keeps
resetting)? (3) does an impairment allowance appear on the MTF book as it
scales?

**Vertical 4: Cash conversion and debt/rating access.** Corpus
establishes: CFO negative in FY23 (-Rs 170 Cr), FY24 (-Rs 310 Cr) and FY26
(-Rs 182 Cr consol / -Rs 164 Cr standalone); cumulative CFO/PAT 0.085x
over 11 years (B01 block_b_trend); Infomerics moved to ISSUER NOT
COOPERATING status on 22-Nov-2024, four downgrades since, most recently
16-Sep-2026 (B08 adverse_findings); an NCD holders' meeting was adjourned
Aug-Sep 2026 and a Rs 99.90 Cr NCD early redemption was Board-approved
19-May-2026 with its own DSCR-exclusion footnote (B02 rank 4/5). Corpus
cannot establish: a CFO decomposition separating MTF-book growth from
pledged-deposit/exchange-guarantee growth on one basis (B13
gate-recommendation, "missing evidence" list); the rating agency's current
liquidity view, unavailable while the company does not cooperate.
Questions that decide it: (1) does H1 FY27 consolidated CFO turn positive
or improve against the H1 MTF book change? (2) does the company restore
cooperation with Infomerics? (3) does the Rs 99.90 Cr NCD redemption and
the Rs 30.85 Cr subsidiary NCD (due 1-Oct-2026) execute without a
refinancing gap?

### 4b. Candidate signal table

*(Expanded from B09 downstream_candidates. Falsifier and cadence are
DRAFTS; verification and tracker writes happen at Role 5.5 in claude.ai.)*

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| NSE/BSE cash and F&O average daily turnover (ADTO), options premium turnover | Two consecutive months of ADTO decline with no matching commentary from Share India on prop/brokerage impact | Monthly | NSE/BSE monthly business-growth bulletins (B09) |
| SEBI active-derivatives-trader count and F&O regulatory circulars | A new circular tightening retail F&O access (e.g. expiry-count reduction) with no Share India concall acknowledgement within one quarter | Monthly / event-driven | SEBI monthly bulletin, SEBI board circulars (B09) |
| RBI intraday-funding and bank-guarantee circular status | A quarter where bank-guarantee/limit constraints visibly compress prop-desk profitability (B05 trigger 6 kill_signal) | Event-driven | RBI notifications/circulars (B09) |
| NSDL/CDSL total demat-account additions | Sustained deceleration in net new demat accounts, signalling client-pool growth stalling | Monthly | NSDL/CDSL monthly investor-data releases (B09) |
| AMFI mutual-fund AUM and SIP flow data | PMS/AIF AUM growth stalling below the Rs 200-250 Cr FY27 target despite healthy AMFI-wide SIP flows | Monthly | AMFI monthly data release (B09) |
| Peer-disclosed MTF book size and interest-rate changes | A peer (SMC Global, Choice International, Angel One) posts MTF growth materially above Share India's for two consecutive quarters | Monthly | NSE/BSE MTF disclosure data; peer investor presentations (B09; peer MTF growth already outpacing Share India per B12b) |
| Infomerics/rating-agency cooperation status | A further downgrade or a new "ISSUER NOT COOPERATING" notation on a different rating line | Event-driven | Infomerics rating rationale, Reg 30 filings (B09) |
| SEBI DRHP filings / SME-platform IPO listing counts | A sustained fall in DRHP filings or SME IPO listings without a matching fall in Share India's merchant-banking approvals count | Quarterly | SEBI DRHP filings; NSE/BSE SME platform listing data (B09) |

### 4c. Fragility read

- **variable_count:** 4 (the Section 2 C1 dominant variables: fee income
  growth, prop-share consistency, MTF book growth vs target, cash
  conversion/rating access).
- **verifiability_ratio:** 3 of 4 externally observable via exchange or
  rating-agency filings independent of management's own framing (fee and
  commission income is an audited P&L line; MTF book size appears in
  investor presentations and is cross-checkable against peer disclosure;
  cash conversion and rating-cooperation status are filed with BSE and
  Infomerics respectively). 1 of 4 (the prop share of profit on a
  consistent basis) is currently company-narrated only, and the company's
  own framing has shifted basis (volume/turnover/profitability) every
  quarter to date (B05 red_flags HIGH).
- **single_point_failure:** funding access / cash conversion. CFO has been
  negative in 3 of the last 4 years, Infomerics has held the rating at
  ISSUER NOT COOPERATING since 22-Nov-2024 through four downgrades, and an
  NCD holders' meeting was adjourned in the same window as a Board-approved
  early redemption whose own DSCR footnote admits exclusion (B00 LBF3/LBF4;
  B02 rank 4/5). A further debt-access shock would stall the branch, MTF
  and AIF growth plan regardless of how the prop/client mix resolves,
  because that plan is currently funded by new debt, not retained cash
  (B02 FLAG-CASH; B09 capacity_check).
- **fragility_verdict: FRAGILE.** Three of four variables are externally
  verifiable, which argues against the worst case, but one of the four
  carries a live, already-stressed single point of failure (funding
  access) and the fourth (prop-share consistency) is company-narrated and
  shifting basis every quarter. Per the fragility definition, one
  kill-switch variable already showing deterioration is sufficient to
  set the band at FRAGILE rather than MODERATE.

### 4d. Research brief (claude.ai live-web work order)

1. Locate the SEBI Adjudication Order text, NSE co-location matter,
   ~30-May-2022, Rs 3 lakh penalty (sebi.gov.in > Enforcement > Orders >
   Orders of AO, May-2026), closes the failed freshness pair (Section 1).
2. Identify the allottee(s) of the 21-Aug-2026 and 27-Aug-2026 preferential
   warrant filings (BSE, both returned HTTP 403 to automated fetch), this
   is the PENDING LIVE VERIFICATION item named in Chain 1 below.
3. Identify the pre-merger shareholders of Silverleaf Capital Services Pvt
   Ltd from NCLT scheme documents or the MCA register, to confirm or rule
   out promoter/promoter-group ownership of the transferor entity ahead of
   its 500-shares-for-1 amalgamation into Share India (B08 input_gaps).
4. Fetch the BSE SHP promoter-level detail table (pledgee names) for
   Jun-2026 and Sep-2026, to establish who holds the pledge and why the
   pledge jumped from 42.87% to 57.80% of promoter holding in one quarter
   (B08 input_gaps), this is the PENDING LIVE VERIFICATION item named in
   Chain 2 below.
5. Check whether Share India, in any Q2/Q3 FY27 investor presentation,
   concall, or sell-side note, finally discloses a revenue-and-profit
   (not volume) prop/client split reconciling to the BRSR method, and
   compare the disclosure format to Choice International's existing
   segment revenue split (broking 59% / NBFC 15%, B06) as a benchmark for
   what such a disclosure would look like.
6. Verify the current status of the three open regulatory matters named in
   B08 (the SEBI abnormal-profits show-cause notice, the MCX position-
   aggregation appeal, and the NSE SAT appeal) via SEBI/MCX/SAT order
   registries, since none is disclosed in the FY26 AR itself.
7. Check Infomerics' or another rating agency's public site for whether
   cooperation has been restored since the 16-Sep-2026 downgrade, and for
   any liquidity/working-capital commentary once a cooperating rationale
   is issued.
8. Cross-check the three-to-five-chain Rule F floor: extend the two chains
   stubbed in Section 4e to five, adding live-web links for at least one
   chain built around peer MTF/algo competitive dynamics (B12b MAJOR
   findings on SMC Global's algo platform and MTF growth) and one chain
   built around the FY27 merchant-banking/DRHP pipeline (B05 guidance:
   6 approvals, 2 main-board IPOs filed).

### 4e. Second-order stub (Master Prompt v3.7, Rule F)

Stub carries the first TWO of the Rule F floor of five chains, drafted
from corpus. Chains 3 to 5 are built in claude.ai with live web, before
Role 2 (see 4d item 8). The "who pays, and why now" links below are
marked PENDING LIVE VERIFICATION per the CHAIN EXCEPTION; no counterparty
fact is fabricated.

```
CHAIN 1: Board approved early redemption of the Rs 99.90 Cr First-Issue
NCD on 19-May-2026, after holders/Trustee refused the original end-use
change (B02 rank 4, Note 17e standalone p.171), in the same year
standalone CFO was Rs (164.27) Cr negative on PAT of Rs 297.69 Cr
(B03 FLAG-CASH).
Link 1 [FACT, VERIFIED]: The company's own footnote states reported
DSCR/ISCR exclude the impact of the proposed NCD early redemption
(B02 rank 5; Note 58a standalone p.218, Note 63a consol p.328).
Link 2 [FACT, VERIFIED]: A separate Rs 30.85 Cr subsidiary NCD matures
1-Oct-2026 (B02 rank 4), and contingent liabilities (mostly NSE/MCX
clearing-margin guarantees) rose 48.3% YoY to Rs 3,232.72 Cr, 122.7% of
net worth, backed by Rs 1,526.88 Cr of pledged fixed deposits
(B02 top_findings rank 6; Note 44/44a consol p.288).
Link 3 [INFERENCE]: If the Rs 99.90 Cr redemption executes on the terms
the company's own DSCR-exclusion footnote implies, near-term debt-service
coverage falls below the reported ratio at the same moment Infomerics has
downgraded the group to ISSUER NOT COOPERATING (16-Sep-2026) and a
separate NCD holders' meeting was adjourned (Aug-Sep 2026, B00 LBF4),
tightening the same funding channel (net financing inflow of Rs 215.05 Cr,
Note 57, funded the FY26 MTF book growth) that the branch/MTF/AIF growth
plan depends on (B09 capacity_check).
Binding constraint: The Rs 99.90 Cr NCD principal and its early-redemption
terms (Note 17e p.171), the Rs 30.85 Cr subsidiary NCD due 1-Oct-2026, and
Rs 3,232.72 Cr of exchange-guarantee contingent liabilities sitting behind
the same balance sheet.
Unsaid: The AR's own events-after-reporting-date note records no
significant events, despite the same-day 19-May-2026 Board resolution
sitting inside the debt note only, not the subsequent-events note
(B02 rank 13, Note 62/66 vs Note 17e/18e), a disclosure-placement gap the
company has repeated across at least three separate document types
(B08 analyst_note).
Observation that confirms or breaks this chain, and confirm-by date: H1
FY27 consolidated CFO in the half-year cash-flow statement filed with Q2
FY27 results (expected filing window Oct-Nov 2026), set against the
half-year MTF book change; if the outflow exceeds the half-year MTF book
increase, the structural reading of the cash-conversion flag holds
(B13 gate-recommendation, resolving metric).
Who pays, and why now: PENDING LIVE VERIFICATION. Claude web should open
the BSE Reg 30 filings on the adjourned NCD holders' meeting and any
subsequent announcement on the outcome of the 19-May-2026 early-redemption
resolution, to identify which NCD holders/institutions are being asked to
accept redemption, on what terms, and why the Trustee refused the original
end-use change (BSE corporate announcements, scrip 540725).
```

```
CHAIN 2: The FY26 AR's MD&A states the group is "reducing dependence on
proprietary trading by increasing client-led and fee-based business"
(B03 guidance_table), while the same AR's BRSR Annexure 7 discloses 73.47%
of turnover from Trading in Securities vs 15.19% from Stock Broking
Services (AR printed p.84-85; B03 red_flags_top3).
Link 1 [FACT, VERIFIED]: Fees and commission income fell 12.7% standalone
/ 18.6% consolidated in FY26, the same year as the MD&A claim
(B04 FLAG-DISCLOSURE-CONTRADICTION).
Link 2 [FACT, VERIFIED]: Note 45 reports "Share broking/trading" as one
undifferentiated segment (93.2% of FY26 segment revenue, 93.4% of segment
profit; consol segment assets Rs 4,58,986.15 Lakh, segment liabilities
Rs 1,93,501.41 Lakh, AR printed p.289-290), so the accounts structurally
cannot show a prop/client split at the profit line, and the note's own
text confirms borrowings are excluded from segment allocation as
"unallocable" (B02 rank 1; B04 FLAG-SEGMENT-OPACITY).
Link 3 [INFERENCE]: Management's concall framing of the mix shifts unit
every quarter (Q3 FY26 volume framing to a Q4 FY26 profit target of 55%
client/45% prop by end-FY27 to a Q1 FY27 claim that 60% client "by volume"
is already achieved), without ever restating the prior quarter's number on
the same basis (B05 red_flags HIGH; B12b MAJOR finding that prop profit
share was flat at ~52% in both Q4 FY26 and Q1 FY27). This pattern is more
consistent with a transition whose engine has not yet shown up in the one
audited number that would prove it (fee income, which fell) than with a
transition underway but merely hard to measure.
Binding constraint: The segment note's structural inability to separate
prop from client profit (Note 45, printed p.289-290) and the BRSR's
annual-only cadence (AR printed p.84-85) as the only filed disclosure
point that has ever answered the split, on a basis different from
management's spoken framing.
Unsaid: No concall across three quarters proactively raises the fee-income
decline, the 48.3% rise in contingent liabilities, the promoter pledge, or
the NCD early redemption (B05 flags, "Material balance-sheet items ...
never raised proactively"): silence on the exact filed metrics that would
falsify the transition story fastest.
Observation that confirms or breaks this chain, and confirm-by date: A
single, consistently-defined revenue AND profit split disclosed the same
way for two consecutive quarters, reconciling with the AR's BRSR method
(B05 trigger priority 3, confirm_signal), first checkable at Q2 FY27
results/concall (expected late Oct 2026) and confirmed or broken at the
FY27 AR's BRSR Annexure (expected ~Sep 2027).
Who pays, and why now: PENDING LIVE VERIFICATION. Claude web should open
Share India's FY27 Q2/Q3 investor presentations and concall transcripts
once filed, and any available sell-side note on Share India, to check
whether a revenue-and-profit prop/client split finally reconciles to the
BRSR method, and should check Choice International's existing segment
revenue disclosure (broking 59% / NBFC 15%, per B06) as the comparator
format such a disclosure would need to match.
```

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in
claude.ai with live web, before Role 2.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. Share India is a Noida-based capital markets group: it trades its own
   money, lends against shares (MTF) and through a small finance company,
   runs a broking and depository business, sells trading software, and
   distributes mutual funds, insurance and merchant-banking services.
2. Its biggest income line is not a customer transaction. It is gains from
   trading its own capital, 58% of FY26 income.
3. A further 9% of FY26 income comes from selling securities it holds as
   stock, reported gross; that is the same trading activity, counted a
   second way.
4. Its customers span retail and institutional traders, margin borrowers,
   NBFC loan customers, and companies raising capital through its
   merchant-banking arm.
5. Institutional clients are the one steadily rising number the corpus
   shows: 154 to 212 over three quarters.
6. Trading activity across the whole exchange, tracked by NSE and BSE
   turnover data and the SEBI derivatives-trader count, drives demand for
   both the trading book and the broking business.
7. Fee and commission income, the part of the business meant to grow with
   client relationships rather than market mood, fell 13% standalone and
   19% consolidated in FY26, the same year management said it was cutting
   reliance on proprietary trading.
8. The prop-trading engine has no moat: it takes the price the market
   sets, and it earns nothing from being liked or trusted by a customer.
9. Broking, lending and distribution have weak pricing power too: SEBI and
   RBI licences are a real barrier to new entrants, but every rival broker
   holds the same licences.
10. The one plan-dependent model here is a mix shift: from a
    prop-trading-heavy earnings stream toward client fees, margin lending
    and wealth management. On FY26's numbers, that shift has not yet
    shown up: the group's parent-level profit concentration actually rose,
    and fee income moved the wrong way.
11. The scan for new, still-forming strengths found only two moderate
    signals (institutional client growth and a paid trading-software
    subscriber base), neither with a disclosed rupee value, and scored
    below the level the framework treats as a meaningful new strength.
12. The corpus could not establish a profit-level split between
    proprietary trading and client business; the accounts report them as
    one segment, and management's own description of the split has
    changed basis every quarter.
13. The corpus could not establish why the promoter's pledged share of
    holding jumped from 43% to 58% in the most recent quarter, or who
    received the group's new preferential warrant issue.
14. The single question that decides most of this dossier is whether cash
    generation and access to debt hold up: operating cash flow has been
    negative in three of the last four years, and the credit-rating agency
    has marked the group as not cooperating with its review since late
    2024.
15. The biggest open questions carried into live verification are: what
    the still-open SEBI and MCX regulatory matters inside the
    proprietary-trading book will resolve to, and whether a single,
    consistent, filed number ever shows the prop-to-client mix actually
    moving.

---

## SECTION 6: STANDING EXTRACTION ANNEX

*(Ten standing questions, answered from the corpus for every company. The
ANNEX EXCEPTION permits opening corpus PDFs/.txt directly for anchored
quotes not already carried in a stage report.)*

**1. UNITS.**
Quote: "Net Interest Margins remained strong at 17.64%" (AR FY26 MD&A,
printed p.74). This is the NBFC segment's interest-spread metric, a
basket figure (the whole MTF + Fincap lending book), not a single loan or
per-client figure. Comment: this is the only per-unit-style figure printed
for any revenue line. Per-trade brokerage rate and MTF interest rate are
NOT FOUND anywhere in the AR or investor presentations (B04 input_gaps;
B09 input_gaps). Where no per-unit figure is printed, the volume and
revenue lines from which one could be derived are: fee and commission
income (Note 30 consol, FY26) and client/institutional-client counts
(154 to 212 over three quarters, B05); no consistent denominator (per
trade, per client, per lakh of turnover) links the two in the corpus.

**2. SEGMENT CAPITAL AND DEBT.**
Quote (Note 45, consolidated, "(` in Lakhs)", AR printed p.289):
"Segment assets: Share broking/trading business 4,22,617.16 [FY25]
... Total 4,58,986.15 [FY26] 3,78,049.49 [FY25]" and "Segment liabilities:
Share broking/trading business 1,83,207.05 [FY26] 1,27,131.12 [FY25] ...
Total 1,93,501.41 [FY26] 1,43,156.59 [FY25]." Latest two periods (FY26,
FY25) both quoted. Borrowings are explicitly NOT allocated by segment: the
note's own text states "Segment assets and segment liabilities represent
assets and liabilities in respective segments. Investments, tax related
assets, borrowings and other assets and liabilities [not allocable to a
segment on reasonable basis] have been disclosed as 'unallocable'" (AR
printed p.287, Note 45 accounting policy). Total consolidated debt
securities (NCDs) were Rs 14,327.95 Lakh FY26 / Rs 3,008.00 Lakh FY25
(Note 18 consol); standalone debt securities Rs 11,243.17 Lakh FY26 / nil
FY25 (Note 17 standalone). Comment: capital employed by segment is not
derivable beyond assets-minus-liabilities per line above; a true
capital-employed or debt-by-segment figure is NOT DISCLOSED.

**3. GUIDANCE VERSUS ASPIRATION.**
Classified from B05/B03 guidance tables, quote-then-comment:
(a) Guidance with a period: "MTF book two-year target ... Rs 900-1,000 Cr
(double from ~Rs 450 Cr) ... 2 years from Jan-2026" (Q3 FY26 concall,
B05 guidance), later restated to "Rs 650 Cr" for FY27 (Q4 FY26) and then
"Rs 1,000 Cr ... 2 years from Jul-2026" (Q1 FY27): three different bases
inside three quarters. "EBITDA margin guideline ~38% (+/-2%)" and "PAT
margin guideline ~22% (+/-2%)," both "standing" (Q4 FY26 concall).
(b) Aspiration without a firm period: "Client vs prop mix (3-year
vision): client 70% / prop 30%" (Q4 FY26 concall, B05), a vision, not a
dated commitment.
(c) Capacity/capability only: "Category III AIF launch ... awaiting
regulatory approval, no date given" originally, later given as "Q3 FY27"
(B03 guidance_table; B05), still contingent on regulatory approval, not a
company-controlled date.

**4. CONCENTRATION.**
Quote (BRSR Annexure 7, AR printed p.84-85): "1. Financial Service Stock
Broking Services (Securities, Commodities Brokerage and Currency
Derivatives Services), Depository Services and Distribution of financial
products. 15.19% 2. Financial Service Trading in Securities 73.47%" and,
by NIC product code, "66120 15.19% ... 64990 73.47%." This is product
concentration by turnover (top product/product-group share): 73.47% in
one activity. Geography (Note 28(b), standalone, printed p.191, "(`
in Lakhs)"): "Primary geographical market: In India 35,845.56 [FY26];
Outside India 438.82 [FY26]", roughly 98.8% India by this
revenue-from-contracts disaggregation (note: this is standalone Ind AS
115 "revenue from contracts with customers," a subset of total income
that excludes the prop fair-value gains line). Customer concentration
(top-customer share): NOT DISCLOSED anywhere found in the AR, investor
presentations or concalls; no top-10 or top-customer revenue share table
exists in the corpus (confirms B04 input_gaps on competitor/customer
detail).

**5. PROMISE LEDGER.**
| Promised in | Promise | Delivery status | Evidence anchor |
|---|---|---|---|
| Q3 FY26 | Silverleaf NCLT approval by end of Q4 FY26 | Missed | Q3 FY26/Q4 FY26/Q1 FY27 concalls (B05 promise_delivery) |
| Q3 FY26 | uTrade multi-broker rollout FY27, 2x-3x revenue in 1-2 yrs | Missed | Q4 FY26 concall (new SEBI circular cited); dropped Q1 FY27 (B05) |
| Q3 FY26 | Insurance segment 20-25% FY26 growth | Partial | Never re-confirmed with a number (B05) |
| Q3 FY26 | MTF two-year target Rs 900-1,000 Cr | Delivered (glide path intact per B05, though B12b MAJOR finding disputes the "on track" scoring given the target's own restatement and 3% six-month growth) | Q1 FY27 concall |
| Q4 FY26 | PMS FY27 AUM target Rs 200 Cr | Delivered | Q1 FY27 concall, Rs 150 Cr at Q1 end, target raised to ~Rs 250 Cr (B05) |
| Q4 FY26 | AIF approval by end Q2 FY27, ops this FY | Partial | Q1 FY27: launch pushed to Q3 FY27 (B05) |
| Q4 FY26 | 6 more branches by end FY27 | Partial | Zero net new branches reported Q1 FY27 (B05) |
| Q4 FY26 | Client volume share to 60% by end FY27 | Delivered (volume metric only, not the revenue/profit split the AR discloses differently) | Q1 FY27 concall (B05) |
| Q4 FY26 | RBI curb ~20% deposit/limit impact, minimal bottom-line impact | Delivered | Q1 FY27 strongest quarter to date (B05) |
| Q1 FY27 | Enshrine Leasing acquisition up to Rs 45 Cr | Delivered | Closed 17-Sep-2026 at Rs 39.72 Cr (B05; Reg 30 filing) |
Credibility grade: C (B05 credibility_grade). B12b verifier finding: the
"Good" operational-delivery sub-read is overstated once the MTF
restatement pattern and the flat Q4/Q1 prop profit share are weighed.

**6. RESTATED BASES.**
Quote: document-wide search found "zero matches for restate/restated" in
the FY26 AR (B02 restatements_found). The only prior-period-adjustment
language found is generic: "previous year figures have been
regrouped/reclassified... does not affect overall financial position,"
with no rupee amount disclosed (Note 64 standalone printed p.221; Note 68
consol printed p.331, per B02). Comment: no reorganisation, transfer, or
reclassification of comparatives is quantified anywhere in the AR.

**7. CORPORATE-ACTION CLAUSES.**
Scheme: Amalgamation of Silverleaf Capital Services Pvt Ltd ("Transferor
Company") into Share India Securities Ltd, NCLT Ahmedabad
CP(CAA)/17(AHM)2026 in CA(CAA)/53(AHM)2025. Quote (Reg 30 filing,
21-Aug-2026): "seeking approval of the proposed Scheme of Amalgamation
(Scheme) with the Appointed Date being 01.10.2023" and the share exchange
ratio, "[Share India] will issue 500 (five hundred) Equity Shares of
Rs.2 each, credited as fully paid up, to the Equity Shareholders of the
Transferor Company for every 1 (one) Equity Share of Rs.10 each held."
Appointed Date: 01-Oct-2023. Effective Date: defined in the Scheme as
occurring on ROC certification, not a fixed calendar date in the excerpts
retrieved. Liability-allocation and undertaking definitions: not fully
retrieved in this pass; NCLT filing also records "no such details of fair
value of Assets and Liabilities of the Transferor Company is provided" as
an objection noted in the filing itself. Comment: the Transferor's
pre-merger shareholder identity is NOT NAMED in the retrieved excerpt
(confirms B08 input_gaps, PENDING LIVE VERIFICATION). NCD early redemption
(not a scheme, but a corporate-action clause): Board resolution
19-May-2026 for early redemption of the Rs 99.90 Cr First-Issue NCD (Note
17e standalone printed p.171); ratios/appointed dates not applicable to a
debt redemption.

**8. RELATED-PARTY PERIMETER.**
Quote (AR printed p.43, Corporate Governance Report, "Relationship between
Directors"): "Amongst all the Directors, Mr. Parveen Gupta and
Mr. Rajesh Gupta are brothers, and Ms. Saroj Gupta is mother of
Mr. Sachin Gupta. Apart from this, none of the other Directors are in any
way related to each other." Named promoter-group/related entities with
FY26 transactions per Note 52 (standalone, printed pp.202-206, per B02/
B08): Rajesh Gupta (interest paid, up 12.9x YoY to Rs 19.88 Lakh; also
6.47%/6.48% direct shareholder per the shareholding note, printed p.174);
Saroj Gupta (interest on pledged shares per Corp Gov Report narrative,
p.46, though no matching Note 52 "interest paid" line was found for her,
an internal inconsistency, B08 input_gaps); R S Futures LLP and R S
Securities (KMP/relative-controlled entities named on Note 52's list,
also the two entities MCX aggregated with the company's own prop account
for its position-limit penalty, B08); Idhyah Futures (brokerage income
collapsed 99.2% YoY, B02 rank 14); Aggarwal Enterprises (rent paid, up
133.0% YoY, B02 rank 14). Comment: BSE SHP notes that Rising Futures and
Skywealth Solutions, disclosed as promoter-group entities as of Mar-2026,
"have been dissolved" and are absent from the Jun-2026 shareholding
pattern (BSE SHP summary, Jun-2026).

**9. PLEDGE AND SHAREHOLDING.**
Quote (BSE SHP summary, quarter ending June 2026): promoter/promoter-group
holding "10,63,85,244" shares, "48.62" percent of total; shares pledged
or otherwise encumbered "6,14,92,594," "57.80" [percent of promoter
holding]; as percent of total company shares, "28.10." Prior quarters
(BSE SHP summaries, same format): Mar-2026, pledged shares "4,56,07,594,"
"42.87" percent of promoter holding, "20.84" percent of total; Dec-2025
44.75% of promoter holding; Sep-2025 52.16% of promoter holding (B08
pledge_trend). Only four quarters (Sep-2025 to Jun-2026) are held in the
corpus; twelve quarters of history are NOT DISCLOSED in this corpus
(BSE SHP summary-level files only go back to Sep-2025, B00
inventory.shareholding). Institutional holding latest (Jun-2026,
screener-sourced per B08/B00): FII 1.87%, DII 0.48% (combined 2.35%),
screener-level not filing-level.

**10. VERIFICATION.**
Documents quoted in this annex and their dates: SHAREINDIA-AR-FY26.pdf
(FY26 Annual Report, filed 05-Sep-2026); BSE SHP summary .txt files dated
Sep-2025, Dec-2025, Mar-2026, Jun-2026; the Reg 30 NCLT scheme-of-
arrangement filing dated 21-Aug-2026 (Silverleaf amalgamation); Infomerics
rating rationales dated 22-Sep-2025 and 16-Sep-2026; SHAREINDIA
concall transcripts Q3 FY26 (30-Jan-2026), Q4 FY26 (23-May-2026), Q1 FY27
(31-Jul-2026).

**CORPUS COMMIT HASH: 0cd9060d0e3245706018992c95730a73805a947e**
