# HALT 1 UNDERSTANDING DOSSIER — TAAL Tech Ltd (TAALTECH)

Run: runs/taaltech-2026-09-10 | Run date: 2026-09-10 | Phase 1 (evidence) only.
Assembled from committed blocks B00-B09, the four phase-1 verifier blocks
(B12a-B12d), confidence.yaml, B13-synthesis-lite.yaml and the stage reports.
No new research. No valuation, price or verdict vocabulary except the one
scoped exception named in Section 2, Part B4. Stages 10 and 11 did not run.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

**1. CONCALLS.** None held. TAAL Tech holds no earnings calls
(`manifest.concalls_available: false`, B00). NO-CONCALL MODE is active for
every downstream stage. This is declared, not a collection miss. The most
recent quarter with any management commentary in corpus is Q1 FY27 (quarter
ended 30 June 2026), covered only by the results filing, not a call. Given
run date 2026-09-10, no more recent quarter has plausibly reported: Q2 FY27
(quarter ending 30 September 2026) is still in progress.

**2. ANNUAL REPORTS.** One held: Annual_Report_2026.pdf, FY2025-26, filed to
BSE 7 August 2026 under scrip code 539956. It is the latest completed FY.
Fewer than three years are held. Pre-FY2022 annual reports are absent
(B00, B01 input_gaps), which is the direct cause of the unresolved
pre-FY2022 business-mix question carried in FLAG-GATE0 below.

**3. RESULTS FILINGS.** Three held: Q3 FY26 (quarter ended 31 December
2025), Q4 FY26 (audited full year, quarter ended 31 March 2026), Q1 FY27
(quarter ended 30 June 2026). The latest is Q1 FY27. No quarter-gap exists
between the latest results filing and the latest AR: the AR covers FY26,
which Q1 FY27 properly postdates. A gap exists further back: quarterly
filings for FY25 and the first half of FY26 (Q1/Q2 FY26, and any FY25
quarters) are not in corpus, so the pre-acceleration quarterly trend line
running into the three-quarter jump cannot be built further back than Q3
FY26.

**4. INVESTOR PRESENTATIONS.** None held. TAAL Tech publishes no investor
presentation. Verified against the company investor page and the screener
documents list, 2026-09-10 (B00). This is the company's own disclosure
posture, not a collection gap.

**5. RESEARCH / RATING.** No broker note or research note is held (ABSENT).
No rating bulletin is held, and none is expected: the FY2025-26 AR states
the Company was not required to obtain a credit rating because fund-based
and non-fund-based facilities were NIL (extracted AR text, lines
3270-3271; B00 declared_not_gaps). The rating absence is explained by the
filing. The research absence is not explained by any filing and should be
checked at Halt 1 in case coverage exists that this container could not
find.

**6. CORPORATE ACTIONS.** No announcement or Regulation 30 filings are held
(ABSENT, B00). Corporate actions visible only because they are narrated
inside the AR itself: the NCLT order of 21 May 2025 merging TAAL Tech India
Pvt Ltd into the listed parent; the company name change effective 4
November 2025; a 26 May 2026 results filing carrying two numerical errors,
one corrected by a 27 May 2026 corrigendum and one (Note 41) never
corrected (B02, B05); a 1:5 stock split with record date 22 September 2026
(B08, aggregator-sourced, not primary-verified). No BSE announcement
archive was collected to confirm completeness of this list or to check for
a Regulation 30 filing on the Rs10cr Vishkul loan.

**7. FRESHNESS PAIR CHECK.** B00's `freshness_verdict` is "FRESHNESS PAIRS
OK". All four pairs pass or are skipped by declaration:
- RESULTS to CONCALL: SKIPPED. No concalls exist for this company; the
  orchestrator rule skips this pair when `concalls_available` is false.
- RATING BULLETIN to RATIONALE: PASS. No rating bulletin exists to trigger
  the pair; the AR explains why (facilities NIL, no rating required).
- SEBI ORDER to ORDER TEXT: PASS. No SEBI order against the Company or its
  directors is referenced in any corpus filing.
- AR to LATEST AUDITED ANNUAL RESULTS: PASS. Annual_Report_2026.pdf is the
  FY2025-26 report and does not trail the latest audited annual result.

No pair failed. The verdict line below is therefore a plain CORPUS GAPPED,
not CORPUS GAPPED-FRESHNESS.

**8. VERDICT LINE**

**CORPUS GAPPED**

| Gap | Expected source | Kind |
|---|---|---|
| Investor presentation | Company IR page | Plausibly-nonexistent (company's own disclosure posture; declared, not a collection miss) |
| Exchange announcements / Regulation 30 filings (FY25-27) | BSE | Findable-missing. This is the single largest procedural gap: it is the only place a Vishkul-loan disclosure, a SEBI action, or corroboration of the revenue acceleration could independently surface. |
| Quarterly shareholding pattern filings after 31 March 2026 (e.g. June 2026) | BSE | Findable-missing. The AR carries the pattern only as at 31 March 2026 and 31 March 2025; no quarterly cadence is in corpus. |
| Broker / research notes | Rating agency site / broker research | Plausibly-nonexistent for a silent micro-cap filer, but not confirmed; operator should check at Halt 1. |
| Pre-FY2022 (FY2017-FY2021) annual reports | BSE / company IR page | Findable-missing. Needed to resolve the pre-FY2022 air-charter-versus-engineering business-mix question carried in FLAG-GATE0. |
| Populated screener P&L / Balance Sheet / Cash Flow / Quarterly CSVs (four of the five screener CSVs are header-only, a known collect_to_repo v3 defect; the fifth, Data_Sheet.csv, is fully populated and was used) | Collector re-run / BSE | Findable-missing, a tooling defect rather than an absent public document. |

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT — PENDING OPERATOR SIGN-OFF**

This declaration is a transition thesis, not a business description. It is
signed only in claude.ai after live-web stress-testing. Nothing in this
file marks it signed.

### PART A — THE FROM STATE (the anchor, not the model)

**A1. ARCHETYPE.** One business line. Outsourcing partner (CLAUDE.md
archetype library: client concentration, wallet share, capacity fill,
contract stickiness, price per unit). B04 tested this directly and it
fits: 95.5% time-and-material revenue, 4.5% fixed-price, 99.82% billed
outside India, 521 employees, a derived revenue-per-engineer proxy of
about Rs36.5 lakh (standalone revenue Rs190.10cr / 521 employees, B04; no
printed per-engineer figure exists in the AR itself, see Section 6, Q1).

**A2. THE SIMPLE ANALOGY.** TAAL Tech is an engineering staffing shop.
Around 521 engineers in Bangalore design plant equipment, aerospace parts,
transport systems and buildings for large industrial companies abroad.
Most of the bill is by the hour: a client buys design capacity it does not
want to hire and carry itself. Switching supplier mid-project means
requalifying a delivery team, which is why more than 70% of the business
comes from relationships over ten years old (AR p.37). The company owns no
factory, holds no patent, and names no customer in its filings. It sells
time, not a product.

### PART B — THE TRANSITION (the model)

**B1. FROM to TO.** One line, one transition read.

FROM: **R2 COST-ADVANTAGED CONVERTER.** The mechanism the evidence
actually traces is a cost position, not a price. A verifier finding (B12b,
B13) shows the group's US subsidiary, TAAL Technologies Inc, bills the
Indian parent Rs4,734.48 lakh, 88.5% of its own turnover, at a 5.68% net
margin, while the Indian parent earns 28.3% on the same contracts (AOC-1
p.162; Note 37(B) p.98). Delivery sits offshore in Bangalore at Indian
cost; the onshore arm is a thin billing conduit. That is a converter's
mechanism: margin from where the cost sits, not from a demonstrated price
premium.

TO (claimed, not proven): **R3 VALUE-ADDED / SPEC'D SUPPLIER.** The
evidence offered for this claim is the ten-year-plus client tenure
statistic and the top customer's rising share of revenue (21% to 24.05%,
Note 42), both read as switching-cost stickiness and partial pricing
power. Recomputed ROCE (Verifier C, B12c) is 22.5-22.6%, which sits inside
R3's stated 20-25% band, above R2's "durable mid-teens." That is a genuine
tension the operator must weigh, not a settled answer: a return metric
that already prints at the TO rung's level, riding on a mechanism that
still reads as the FROM rung's mechanism, and on a reported-ratio base
(company's own Operating Profit Margin, RONW, ROE) that B02 and B04 both
flag as inflated by non-operating other income. No bill-rate, utilisation,
or per-account margin figure exists anywhere in the corpus to confirm
pricing power, specifically, is what separates TAAL Tech's returns from a
plain cost-position converter (B04, B07 FLAG-MARGIN-UNEXPLAINED). The
emerging moat scan scored 4 and classified NONE; only client tenure (C1)
cleared Moderate, and the AR's forward statement on the largest business
event in the run, the revenue acceleration, is one unnamed, unquantified
sentence (B05 FLAG-SILENCE).

**B2. THE ENGINE.** Two things must physically change to move the
business from R2 to R3. First, growth needs to broaden from one deepening
account into named, diversified wins. The corpus cannot yet separate
wallet-share deepening at a single account (concentration rising to
24.05%) from genuine new-logo diversification (B07 FLAG-CONCENTRATION-DUAL-READ).
Second, the margin needs a demonstrated pricing mechanism, a realised
bill-rate premium or a utilisation gain, distinct from the cost-position
structure the US subsidiary disclosure already explains (B13
margin_mechanism_partly_settled). Neither is disclosed. Both are the
variables Role 5.5 and Stage 11 must chase.

**B3. THE PROOF GATE.** The exact testable pair, both halves due in the
same filing: quarterly consolidated revenue sustaining above Rs57-60cr for
two more quarters (Q2 FY27, due on or around November 2026; Q3 FY27, due
on or around February 2027), WHILE operating cash flow over profit after
tax recovers above 0.7x and unbilled revenue reverts below 15% of that
quarter's revenue, in the H1 FY27 cash flow statement due around November
2026 (gate-recommendation.md monitorables 1-3; B13 cash_determination).
Revenue holding without cash recovering leaves the transition as growth
financed by working capital, unproven. Cash recovering without revenue
holding removes the growth leg entirely. Both firing together is the
gate. Until it fires, this is a name to watch, not a transition to trade.

**B4. THE RECOGNITION GAP (open question, resolved at Stage 11).** Whether
the market has already priced the claimed TO state, the spec'd-supplier,
deepening-wallet-share reading, into the current multiple, or whether it
is still pricing the FROM state, a cost-advantaged converter whose recent
revenue jump the company itself has not explained. This run carries no
price, no fair value and no multiple. Stage 11 resolves the question via
the Section 1B destination-PE gap. Until then the direction of any
re-rating engine, if one exists, is unknown.

**B5. THE UGLINESS TEST.** The cash-conversion fall is classified
**INDETERMINATE**, following B13's ruling, because the evidence does not
yet decide either way and the reasons run in both directions at once.
Against GROWTH-INDUCED: over FY26 as a whole, working capital grew about
eight times faster than sales, and all three peers in the same window
moved cash conversion the other way (B06 FLAG-WC-GAP), which removes the
"normal ER&D growth-phase pattern" reading. Against STRUCTURAL: the
receivables ageing tail is clean at 2.0% of gross (up only from 1.5%), the
company carries zero debt and a 9.49x current ratio, and the 31 March 2026
balance-sheet date sits one month after a 24.6% sequential revenue step
that mechanically inflates a same-date contract asset. The missing
evidence that would close this, and that no other item substitutes for:
a contract-asset (unbilled revenue) rollforward or ageing schedule, absent
from both note sets; the H1 FY27 cash flow statement, due around November
2026; and any management statement on the billing cycle, of which none
exists in any filed document (B03, gate-recommendation.md).

**B6. THE TRANSITION FALSIFIER.** Two things together kill the transition
thesis, kept separate from what would kill the FROM business itself (Part
C3). First, quarterly revenue reverting into the Rs44-49cr band held from
March 2024 through September 2025 (B05 kill_signal), removing the growth
leg entirely. Second, in that same lower-revenue filing, unbilled revenue
holding at or above 20% of the (now smaller) quarter's revenue (B13
falsification_metric), which removes the mechanical, exit-quarter-timing
explanation for the cash fall and leaves only the structural reading
standing. Either print alone weakens the case. Both together, in one H1
FY27 or Q2 FY27 filing, falsify the transition.

### PART C — WHAT THE MODEL WATCHES (derived from the transition)

**C1. DOMINANT VARIABLES.**
1. Quarterly consolidated revenue run-rate against the Rs57-60cr
   threshold. Current state: three consecutive quarters accelerating,
   Rs45.79cr to Rs57.04cr to Rs64.81cr, unexplained by management (B05).
2. Operating cash flow over profit after tax, and unbilled revenue as a
   share of quarter revenue. Current state: 0.33x (down from 0.84x);
   unbilled revenue 24.1% of exit-quarter revenue (up from 10.4%) (B01,
   B02, B13).
3. Top-customer revenue concentration against a 28-30% dependency
   threshold. Current state: 24.05% of FY26 revenue, up from about 21%,
   rising (B04, B07, Note 42).
4. Disclosure of a transfer-pricing study, an advance pricing agreement,
   or a US tax event bearing on the 28.3% India-booked margin. Current
   state: none disclosed anywhere in 164 AR pages (B13
   margin_mechanism_still_open).

**C2. WHAT THE MODEL REJECTS.** Market size. B09's total- and
served-market figures are explicit floors, built under a complete
WebSearch failure (20 of 20 calls), yet revenue headroom still computes
to 5.6x at a GOOD runway class. The binding constraint on this name is
not addressable market; it is execution, disclosure and governance. The
model also does not treat AI-driven disruption as a near-term dominant
variable: peers confirm AI has not yet compressed core ER&D pricing,
scope or headcount in the same window (B06 verified, 7 anchors), though
management has not itself assessed the question (B04, B09
FLAG-AI-UNRESOLVED), which keeps it a longer-horizon watch item, not a
current-cycle variable.

**C3. THE BUSINESS FALSIFIER.** Loss of, or a material slowdown at, the
top customer (24.05% of FY26 revenue) or the top two customers combined
(34.03%), without a named replacement, in a business whose one confirmed
moat is client tenure and whose filings disclose no pipeline, no backlog
and no contract-minimum figure (B04, B07, Note 42). That evidence would
force a re-declaration of the FROM business itself, not only the
transition claim, because relationship tenure is the one thing this scan
found holding the business up at all.

**mental_model_status: DRAFT - PENDING OPERATOR SIGN-OFF**

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

TAAL Tech sells engineering hours. Its Bangalore engineers do plant
engineering, product design, aerospace design, transport engineering and
building information modelling for industrial clients outside India. Time
and material contracts, billed by engineer time, are 95.5% of revenue.
Fixed price milestone projects are 4.5%. A sale of goods line is 0.01%
and does not matter. So the whole company is one revenue stream sold two
ways. The customer buys design and engineering capacity it does not want
to hire and carry in house, and switching means requalifying a delivery
team in the middle of a live project. That is why the annual report can
say more than 70% of business comes from clients of ten years or more (AR
p.37).

The filings never name a customer. Note 42 (AR p.156) discloses one
customer at 24.05% of FY26 revenue, up from roughly 21% the year before,
and a second close to 10%. Revenue is 99.82% billed outside India:
Rs34.78 lakh inside, Rs19,708.14 lakh outside (consolidated Note 42, p.156).
The run did not establish who these customers are, what they buy, or how
long the contracts run.

Present demand reaches the company through six signals the run named. The
unnamed top customer at 24.05% of revenue is the largest single one. The
other five are the quarterly results of the listed India ER&D peer set
(LTTS, Cyient, Tata Elxsi, Onward Technologies, Sasken), the USD-INR and
EUR-INR rates, the North America and Europe industrial and aerospace
capex cycle read through ISM and Markit PMI and the Boeing and Airbus
order backlogs, the adoption pace of GenAI tooling in engineering
services, and the Bangalore ER&D engineer wage and attrition trend.

Forward demand did not verify. No peer transcript in the January to June
2026 window describes a sector step up: Tata Elxsi grew 0.9% to 1.3%
quarter on quarter in constant currency, Cyient's digital engineering
unit shrank 2.4% then 0.5%. One exception maps to a TAAL Tech vertical:
Cyient's aerospace-linked Transportation and Mobility cluster grew 13.2%
to 14.8% year on year in constant currency. Total market was measured at
Rs23,678cr to Rs23,875cr and the served market at Rs1,100cr, both
explicit floors built from peer aggregation after web search failed on
all 20 calls. Runway class is GOOD and revenue headroom is 5.6x against
those floors.

Competitive advantage is thin on filed evidence. The emerging moat scan
scored 4 and classified NONE. One category cleared Moderate: customer
ecosystem and embedded relationships (C1), resting on the ten-year tenure
statement and the rising top-customer share. Categories 21 and 22 both
scored zero. The fixed-price line has no moat. The time-and-material line
has one partial moat, client tenure, and the same rising customer share
that evidences it is also the top risk to it. R&D was Rs37.55 lakh, 0.20%
of revenue, and technology absorption is reported "NA" (Annexure A,
p.49). No patent, design registration or IP filing appears anywhere in
the 164-page annual report.

*This is the draft copy for Halt 1, assembled from B01-B09. Stage 13's
copy is the final version, updated by later stages, per
prompts/13-synthesis-pipeline.md.*

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. Verticals framed

**Vertical 1: Revenue run-rate durability** (dominant variable 1)
What the corpus establishes: a three-quarter revenue acceleration, filed
and verified by two separate audits, Rs45.79cr to Rs57.04cr to Rs64.81cr,
the last 41.6% above the prior year (B00, B05, Verifier A 96.9%
acceptance). No peer transcript in the same window shows a matching
sector-wide step-up (B06 FLAG-DEMAND-GAP). What it cannot establish: the
cause. No customer name, no contract size, no scope description exists in
any document management wrote (B05 FLAG-SILENCE). Questions that decide
it: (1) Does Q2 and Q3 FY27 sustain above Rs57-60cr? (2) Is the jump
concentrated in the top customer, per next year's Note 42, or broad-based?
(3) Does any client-side announcement corroborate a new engagement in this
window?

**Vertical 2: Cash conversion / unbilled revenue** (dominant variable 2)
What the corpus establishes: CFO/PAT fell from 0.84x to 0.33x; unbilled
revenue nearly tripled, decoupling from 6.6% revenue growth (B01, B02);
all three peers moved working capital the opposite direction in the same
window (B06 FLAG-WC-GAP); the receivables ageing itself stayed clean
(B13). What it cannot establish: no contract-asset rollforward exists in
either note set to separate opening balance, additions, billings and
reversals (B03). Questions that decide it: (1) Does H1 FY27 show unbilled
revenue reverting below 15% of quarter revenue? (2) Does CFO/PAT recover
above 0.7x? (3) Does the top customer show a payment-term extension in
its own filings in the same window?

**Vertical 3: Customer concentration** (dominant variable 3)
What the corpus establishes: top customer at 24.05% of FY26 revenue, up
from about 21%; the AR names no customer and its only narrative line is
the reassuring 70%-tenure aggregate (B04, B06, Note 42). What it cannot
establish: whether the rise is broad wallet-share deepening or a
single-program ramp (B07 FLAG-CONCENTRATION-DUAL-READ), or the customer's
identity. Questions that decide it: (1) Does next year's Note 42 cross
28-30%? (2) Can live web identify the customer via any counterparty
announcement? (3) What is the contract's minimum or termination
structure, if ever disclosed?

**Vertical 4: Margin mechanism / transfer-pricing durability** (dominant
variable 4)
What the corpus establishes: genuine EBIT margin 27.84%, Other Income
excluded; the US subsidiary bills the parent Rs4,734.48 lakh at a 5.68%
net margin while the parent earns 28.3% (B13; AOC-1 p.162; Note 37(B)
p.98); no transfer-pricing study or advance pricing agreement is
disclosed anywhere. What it cannot establish: whether the 28.3%
India-booked margin survives a US transfer-pricing challenge; the
residual gap against Onward Technologies, similarly offshore-heavy and
earning about 13%, stays open (B13 margin_mechanism_still_open).
Questions that decide it: (1) Does any AR or exchange filing ever
disclose a transfer-pricing study or an APA? (2) Does a US tax assessment
or adjustment appear in a future filing? (3) What is the realised
bill-rate or utilisation figure, if ever disclosed, that would separate
cost position from demonstrated pricing power?

### 4b. Candidate signal table

Expanded from B09's downstream_candidates. UNVERIFIED; verification and
tracker writes happen at Role 5.5 in claude.ai.

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| Top customer revenue concentration (unnamed, 24.05% of FY26 revenue) | Share crosses 28-30% at next AR Note 42, or an exchange filing reports the account's loss or slowdown | Event-driven (also annual, Note 42) | Next AR Note 42; BSE Regulation 30 filings; Downstream_Source_Discovery_Protocol customer-health tier |
| Listed India ER&D peer quarterly results (LTTS, Cyient, Tata Elxsi, Onward Technologies, Sasken) | A peer reports the same sector-wide step-up TAAL Tech shows, reversing FLAG-DEMAND-GAP | Quarterly | Company quarterly results / investor releases |
| USD-INR and EUR-INR exchange rates | A sharp INR appreciation compresses realised revenue without a matching volume story | Monthly | RBI reference rate / FBIL |
| NA/Europe industrial and aerospace capex cycle | PMI or Boeing/Airbus backlog data turns down sharply while TAAL Tech revenue keeps accelerating, widening the read-across gap | Monthly | ISM/Markit PMI; Boeing/Airbus order and delivery reports |
| GenAI/AI tooling adoption pace in engineering services | A peer reports AI-driven billable-hour compression or pricing pressure in core ER&D scope | Event-driven | Nasscom/Zinnov AI-in-ER&D commentary; peer earnings-call AI commentary |
| Bangalore ER&D engineer wage and attrition trend | A sustained attrition spike or wage-inflation jump outpaces the 13.9-16.6% headcount CAGR the SOM path implies | Quarterly | Nasscom talent-supply reports; peer (LTTS, Cyient) attrition disclosures |

### 4c. Fragility read

- **variable_count: 6.** (1) quarterly revenue run-rate holding above
  Rs57-60cr; (2) CFO/PAT recovering above 0.7x with unbilled revenue below
  15%; (3) top-customer concentration not crossing 28-30%; (4)
  transfer-pricing structure surviving a US challenge; (5) the NA/Europe
  industrial and aerospace capex cycle; (6) GenAI/AI adoption pace not
  compressing billable-hour economics.
- **verifiability_ratio: "4 of 6 externally observable, 2 of 6
  company-narrated only or presently undisclosed."** Externally
  observable via BSE filings, PMI/Boeing/Airbus data, or peer disclosure:
  revenue run-rate, cash conversion, the capex cycle, AI adoption pace.
  Company-narrated only or undisclosed: customer concentration (behind an
  unnamed customer in Note 42, no independent corroboration possible
  without an identity); transfer-pricing survival (no study or APA is
  disclosed at all, so there is nothing to check externally until an
  event occurs).
- **single_point_failure:** Quarterly consolidated revenue reverting
  below Rs57cr while unbilled revenue stays at or above 20% of that
  quarter's revenue (B13's falsification_metric). One print, due around
  November 2026, ends the growth leg and removes the growth-induced
  reading of the cash leg at the same time.
- **fragility_verdict: FRAGILE.** Six variables must move favourably, a
  third of them not independently checkable from outside the company, the
  margin mechanism is only partly settled, and a single disclosed number
  can break two legs of the thesis in one print.

### 4d. Research brief

Numbered live-web work items for claude.ai. Includes every PENDING LIVE
VERIFICATION link raised in 4e.

1. Identify who controls Vishkul Enterprises Private Limited: directors,
   shareholders, financials. Ten-plus MCA/Zauba/Tofler/InstaFinancials
   attempts failed in this container (B08).
2. Check BSE scrip 539956 for any Regulation 30 disclosure or shareholder
   approval covering the Rs10cr loan to Vishkul, and for the postal
   ballot record beyond the FY26 name-change item (B08).
3. Check whether Narayan Karbhase recused from Audit Committee
   deliberation of the Vishkul loan, or declared the interest under
   Section 184; not found in the corpus (B03, B08, Verifier B CRITICAL
   finding).
4. Check the Muralidhar Chitteti Reddy independence question: he is
   proposed as an independent director under a Section 149(6) declaration
   while Note 37(B) records sitting fees paid to him as a Non-Whole-Time
   Director of an amalgamated entity (Verifier B CRITICAL finding, not
   yet reflected in the B08 promoter verdict).
5. Check any proxy advisory note (IiAS, SES, InGovern) on TAAL Tech;
   searches did not complete in this container (B08 searches_skipped).
6. Check the unverified "SEBI warning letter dated 23 April 2026" claim
   surfaced in one search summary; NOT ADOPTED here, underlying BSE PDFs
   returned 403 in this container (B08).
7. Confirm whether Q2 FY27 results have printed by the time of Halt 1
   review, and if so, pull the unbilled-revenue and CFO/PAT figures
   directly (this is the proof-gate observation, Part B3).
8. Check whether TAAL Tech, its US subsidiary, or any counterparty
   discloses a transfer-pricing study, an advance pricing agreement, or a
   US tax assessment bearing on the 5.68%/28.3% split (Part B2, B4d
   vertical 4).
9. Check the 2015 demerger and 2025 merger history for any minority
   shareholder dispute or swap-ratio challenge; searches did not
   complete in this container (B08 input_gaps).
10. Check employee-reputation sources (Glassdoor, AmbitionBox) for
    attrition or culture signal that might corroborate or contradict the
    revenue acceleration; not attempted in this container (B08
    searches_skipped).
11. CHAIN 1 PENDING LIVE VERIFICATION (Section 4e): identify the top
    customer's identity via any Reg 30 large-order disclosure or any
    counterparty announcement of a new engineering-services vendor award
    in the Q4 FY26 / Q1 FY27 window.
12. CHAIN 2 PENDING LIVE VERIFICATION (Section 4e): check whether the top
    customer (once identified) shows its own payment-term extension or
    cash constraint in its own filings in the same window.

### 4e. Second-order stub (Master Prompt v3.7, Rule F)

Rule F sets a floor of five chains for Role 2, Role 6 and FTTCP. Halt 1 is
earlier than all three and has no live web, so it carries a STUB: the
first two chains, drafted from corpus, for Claude web to extend to the
Rule F floor with live-web links.

```
CHAIN 1: TAAL Tech's Q1 FY27 revenue reached Rs64.81cr, up 41.6% YoY, the
third of three consecutive accelerating quarters (Rs45.79cr, Rs57.04cr,
Rs64.81cr) [B00 load_bearing_facts; Results_Q1FY27_Jun_2026]
Link 1 [documented, B04/Note 42]: the top customer already stood at
24.05% of FY26 revenue, up from about 21% the year before, and rising.
Link 2 [documented, B06]: peer transcripts across Tata Elxsi and Cyient
in the same January-June 2026 window show flat-to-negative sequential
growth, so the acceleration is not sector-wide (B06 FLAG-DEMAND-GAP,
contradicted claim 1).
Link 3 [INFERENCE]: because the jump is not sector-wide and the top
customer's share is already rising, the more probable driver of the
Q4 FY26/Q1 FY27 acceleration is deepening spend from the existing top
account or a small number of existing accounts, rather than a broad wave
of new-logo wins. This is a probability read across two filed facts, not
a filed fact itself.
Binding constraint: the corpus carries no customer identity, no contract
minimum, no termination clause and no backlog figure. Nothing filed says
what caps or protects this revenue if the account slows (B04, B07).
Unsaid: the annual report's only candidate sentence, "won multiple
strategic accounts," is unquantified, unnamed and undated (AR p.37,
Outlook). That is filed silence on the single largest business event in
the corpus (B05 FLAG-SILENCE).
Who pays, and why now: PENDING LIVE VERIFICATION. Claude web should
attempt to identify the top customer, to the extent legally disclosable,
via any Regulation 30 large-order disclosure on BSE scrip 539956, or via
a counterparty's own announcement of a new engineering-services vendor
award or contract expansion in the Q4 FY26/Q1 FY27 window. TAAL Tech's
own filings name no customer; this container cannot supply one and does
not fabricate one.
Observation that confirms or breaks this chain, and confirm-by date:
Q2 FY27 results (on or around November 2026): does the next Note 42-style
disclosure or any interim filing show concentration crossing 28-30%, and
does quarterly revenue hold above Rs57-60cr? Confirm-by 2026-11-30.
```

```
CHAIN 2: Consolidated CFO/PAT fell from 0.84x (FY25) to 0.33x (FY26)
[B01, B02, B13]
Link 1 [documented, B02, Note 14 p.137]: unbilled revenue nearly tripled,
Rs4.64cr to Rs13.75cr, decoupling from 6.6% full-year revenue growth.
Link 2 [documented, B06 FLAG-WC-GAP]: all three peers moved working
capital the opposite direction in the same window: Onward Technologies
improved DSO from 73 to 70 days; Cyient converted free cash flow to
profit at 163% then 80.5%, narrating collections discipline both times.
This removes the "normal ER&D growth-phase pattern" reading as the
charitable explanation.
Link 3 [INFERENCE]: because the receivables ageing tail stays clean at
2.0% of gross and the 31 March 2026 balance-sheet date sits one month
after a 24.6% sequential revenue step, part of the contract-asset build
is probably a mechanical, one-time bulge from exit-quarter timing rather
than a structural billing-cycle break. This inference cannot rule out a
genuine lengthening tied to the same unexplained concentration deepening
named in Chain 1, because working capital still grew about eight times
faster than sales over the full year, which a one-quarter timing effect
alone would not produce.
Binding constraint: no contract-asset rollforward exists in either the
standalone or the consolidated note set to separate opening balance,
additions, billings and reversals (B03).
Unsaid: no management statement anywhere addresses the billing cycle; the
MD&A does not mention cash flow at all (B03 missing_risks).
Who pays, and why now: PENDING LIVE VERIFICATION. Claude web should check
whether the top customer identified in Chain 1, once named, shows its own
payment-term extension or cash constraint in its own public filings in
the same window. A client-side payment-term extension would explain an
unbilled build and a revenue-concentration deepening at the same time.
This container has no counterparty identity to check and does not
fabricate one.
Observation that confirms or breaks this chain, and confirm-by date: the
H1 FY27 cash flow statement (on or around November 2026). Unbilled
revenue below 15% of quarter revenue with CFO/PAT above 0.7x resolves the
flag toward growth-induced. At or above 24% with CFO/PAT below 0.5x for a
second consecutive period resolves it toward structural. Confirm-by
2026-11-30.
```

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in
claude.ai with live web, before Role 2.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. TAAL Tech sells engineering hours from Bangalore to industrial clients
   abroad, billed mostly by time and material, 95.5% of revenue (B04).
2. It designs plant equipment, aerospace parts, transport systems and
   buildings. It does not manufacture or sell a physical product (B04).
3. Revenue is 99.82% billed outside India. The filings never name a
   single customer anywhere in the annual report (B04, Note 42).
4. One customer bought 24.05% of FY26 revenue, up from about 21% the
   year before, and rising (Note 42, B04, B07).
5. Clients stay a long time. More than 70% of the business comes from
   relationships over ten years old (AR p.37).
6. Revenue grew slowly for years, then jumped. Three quarters ran
   Rs45.79cr, Rs57.04cr, Rs64.81cr, the last one 41.6% above a year
   earlier (B00, B05).
7. No peer reports a matching sector-wide demand jump in the same window.
   The acceleration looks company-specific, not industry-wide (B06).
8. The moat scan found almost nothing. It scored 4 and classified NONE.
   Only client tenure cleared a Moderate rating, and the same rising
   concentration that supports it is also its biggest risk (B07).
9. The company's margin, 27.84%, beats similarly sized peers. A verifier
   traced part of the reason to a US subsidiary that bills the parent at
   a thin 5.68% margin while the Indian parent keeps 28.3% (B13,
   AOC-1 p.162, Note 37(B) p.98).
10. That mechanism is a cost-structure advantage, not proven pricing
    power. Whether it survives a transfer-pricing challenge is not
    disclosed anywhere in the corpus (B13, Section 2 Part B2).
11. Cash stopped matching profit. Operating cash flow covered only 33% of
    profit in FY26, down from 84% the year before (B01, B02).
12. The mental model is a possible climb from a cost-advantaged converter
    toward a spec'd supplier with real pricing power, but the evidence
    for pricing power itself is thin and the cash story is unresolved
    (Section 2).
13. The fragility verdict is FRAGILE. Several variables must move
    favourably together, and a third of them cannot be checked
    independently from outside the company (Section 4c).
14. The corpus could not establish who controls Vishkul Enterprises, the
    company's 50.74% holding-company owner, or whether the Rs10cr loan to
    it was ever disclosed to the exchange (B08).
15. The two biggest open questions: does the revenue acceleration hold
    into Q2 and Q3 FY27, and does cash conversion recover in the same
    filing. One print, due around November 2026, can answer both at once
    (B13 falsification line).

---

## SECTION 6: STANDING EXTRACTION ANNEX

Ten standing questions, answered from corpus, quote-then-comment, for
Claude web to carry into live verification. Page anchors are PDF page
numbers matching the "===== PAGE n =====" markers in the extracted text,
which match the PDF's own pagination.

**1. UNITS.**

Quote: "The number of permanent employees on the rolls of the company as
on March 31, 2026 was 521." (Annual_Report_2026, page 50, Annexure C to
the Board's Report, Particulars of Employees)

Quote: "The median remuneration of employees of the Company during the
financial year 2025-26 was Rs. 9.40 Lakhs p.a." (Annual_Report_2026, page
50, same annexure)

Comment: No bill rate, utilisation figure, or realised revenue-per-engineer
number is printed anywhere in the 164-page annual report or the three
results filings. A derived proxy, about Rs36.5 lakh revenue per employee
per year, can be built from standalone revenue (Rs190.10cr) divided by
521 employees (B04), but it is not a filed figure. It covers the whole
company as one basket, not one product: 95.5% of that basket bills as
time-and-material and 4.5% as fixed-price (B04), so the proxy blends two
different pricing models and cannot be split between them from filed
evidence.

**2. SEGMENT CAPITAL AND DEBT.**

Quote: "The Management believes that it is currently not practicable to
provide disclosure of geographical location-wise assets, since the
meaningful se[g]regation of the available information is onerous."
(Annual_Report_2026, page 156, Consolidated Note 42(A), Segment
reporting)

Quote: geographical revenue split, FY26 versus FY25 (Rs lakh): "India
34.78 / Outside India 19,708.14 / Total 19,742.92" against "India 43.50 /
Outside India 18,470.52 / Total 18,514.02" (Annual_Report_2026, page 156,
same note)

Comment: TAAL Tech discloses one operating segment (engineering design
services) and only a geographic revenue split. Segment assets, segment
liabilities, capital employed and borrowings allocated by segment are
NOT DISCLOSED, and the AR states why: management calls the allocation
exercise "onerous." Borrowings are not a live question regardless: the
company carries zero debt company-wide, both years (B01 Block D, 20/20
score).

**3. GUIDANCE VERSUS ASPIRATION.**

Quote: "The outlook for the company remains very positive. In the past
years we have deepened our engagements with existing customers, we have
added new capabilities and we have won multiple strategic accounts. We
believe that these efforts will continue to yield and deliver very
positive results in the coming years." (Annual_Report_2026, page 37,
MD&A, Outlook)

Quote: "we are yet to be able to assess the full impact of AI on the
engineering services sector. We will assess this as we go along. For
now, we are keeping our selves abreast of industry trends and taking
steps to adopt the technology to improve efficiencies." (Annual_Report_2026,
page 37, MD&A)

Comment: Both statements are (b) aspiration without a period: no revenue,
margin, headcount or timeframe number is attached to either. Nothing in
the corpus classifies as (a) guidance with a period; the run found zero
numeric guidance across 164 AR pages and three results filings (B05
credibility_basis). The AI statement is closer to (c) capacity/capability
only: a stated intent to monitor, not a commitment.

**4. CONCENTRATION.**

Quote: "Revenue from two customer of Company's engineering design
services segment amounting to INR 5,734.36 lakhs (March 31, 2025: revenue
from two customer amounting to INR 5,734.36 lakhs) is more than 10% of
the total revenue of the company." Table: "Customer - 1: 4,572.48 /
24.05% (Mar-26); 3,805.03 / 20.55% (Mar-25). Customer - 2: 1,897.74 /
9.98% (Mar-26); 1,929.33 / 10.42% (Mar-25)." (Annual_Report_2026, page
156, Consolidated Note 42)

Comment: Product concentration is effectively 100% in one disclosed
segment (engineering design services); no sub-product split is given.
Geography concentration is 99.82% outside India (see Q2 quote).
Customer concentration is disclosed by percentage only; no customer is
named anywhere in the corpus. NOT DISCLOSED: customer identity, industry,
contract type or duration for either of the two customers named only as
"Customer - 1" and "Customer - 2."

**5. PROMISE LEDGER.**

| Promise | Date made | Delivery status | Evidence anchor |
|---|---|---|---|
| None found | NOT APPLICABLE | NOT APPLICABLE | NOT APPLICABLE |

Comment: NOT DISCLOSED / NOT APPLICABLE. No earnings calls, no investor
presentation, and zero numeric forward guidance exist anywhere in the
164-page AR or the three results filings (B05 promise_delivery: delivered
0, partial 0, missed 0, rows []; credibility_basis). There is nothing to
track against.

**6. RESTATED BASES.**

Quote: "After the receipt of the NCLT Order and the filing of Form INC
28 the Company has approved restated accounts from Appointed date i.e.
April 01, 2023. The figures for the quarter ended March 31, 2026 are the
balancing figures in respect of full financial year and year to end
figures for respective quarter and year ended." (Annual_Report_2026, page
104, Standalone Note 47)

Comment: FY25 comparatives in this AR are the merged/restated entity,
carrying TAAL Tech India Pvt Ltd's results back to the 1 April 2023
appointed date via pooling-of-interest accounting (B02 restatements_found;
Note 48, both note sets, pages 104-105 / 159-160). This means no
pre-FY2022 row in the ten-year Gate 0 series can be assumed comparable to
FY25/FY26 without checking the pre-2022 business mix, which this corpus
cannot do (see Section 1, item 2).

**7. CORPORATE-ACTION CLAUSES.**

Quote (2015 demerger): "TTL was earlier a wholly owned subsidiary of
Taneja Aerospace and Aviation Limited (TAAL). However, pursuant to
approval of the Scheme of Arrangement under Section 391 to 394 of the
Companies Act, 1956 between TAAL & TTL, the Air Charter business of TAAL
including investment in First Airways, Inc, USA and Engineering Design
Services business conducted through TAAL Tech India Private Limited
(TTIPL) has been demerged into TTL w.e.f. October 1, 2014 and TTL has
seized to be a subsidiary of TAAL." (Annual_Report_2026, page 69,
Standalone Note 1, General information)

Quote (2025 merger): "Pursuant to the order dated 21st May 2025 issued by
National Company Law Tribunal under Section 230 to 232 of the Companies
Act, 2013, TAAL Tech Limited TTL (formerly Enterprises Limited) has
merged with its wholly owned subsidiary TTIPL, w.e.f April 01,2023."
(Annual_Report_2026, page 69, Standalone Note 1)

Quote (authorised capital effect): "There was no change in the paid-up
share capital of the Company during the year under review. However
Authorized Share capital of the Company was increased from Rs.
5,00,00,000/- to Rs. 6,00,00,000/- pursuant to aforesaid order."
(Annual_Report_2026, page 36, Board's Report, General section)

Comment: Both actions are in corpus. The 2015 event demerged the Air
Charter business and TAAL Tech India (TTIPL) from Taneja Aerospace into
the listed parent, effective 1 October 2014, and no prospectus applies
(TAAL Tech has been listed since 2016, long before the three-year
corpus window; B00). The 2025 event was a wholly-owned-subsidiary
amalgamation, TTIPL into the listed parent, appointed date 1 April 2023,
NCLT order 21 May 2025. No share-exchange ratio applies to the 2025
merger: TTIPL was already a wholly owned subsidiary, so no new shares
were issued and no minority allocation clause exists to quote. Paid-up
capital was unchanged; only authorised capital rose. Liability-allocation
clauses beyond the standard pooling-of-interest treatment (Note 47/48
above) are NOT FOUND in this AR; the 2015 Scheme of Arrangement document
itself is not in corpus (see Section 1, item 6).

**8. RELATED-PARTY PERIMETER.**

Quote: "Holding company: Vishkul Enterprises Private Limited, India.
Entities under common control: Laurus Tradecon Private Limited (erstwhile
known as Lighto Technologies Private Limited) (Upto 14th February 2025);
Taneja Aerospace and Aviation Limited; Katra Auto Engineering Private
Limited; Asscher Enterprises Limited (erstwhile known as Indian Seamless
Enterprises Limited)." (Annual_Report_2026, page 97, Standalone Note
37(A))

Quote (Vishkul transaction, latest year): "Vishkul enterprises Pvt. Ltd.
... Loans given to related parties during the year: 1,000.00 (Mar-26); -
(Mar-25). Interest income: 98.55 (Mar-26); - (Mar-25)." (Annual_Report_2026,
page 98, Standalone Note 37(B), Rs lakh)

Quote (US subsidiary transaction): "TAAL Technologies Inc, USA-Service
Received: 4,734.48 (Mar-26); 4,374.46 (Mar-25). ... Balance
receivable/(payable) as at the end of the year: TAAL Technologies Inc,
USA: (2,000.51) (Mar-26); (603.70) (Mar-25)." (Annual_Report_2026, page
98, Standalone Note 37(B), Rs lakh)

Comment: Note 36(A)/37(A) names one holding company (Vishkul) and four
entities under common control (Laurus Tradecon, Taneja Aerospace and
Aviation, Katra Auto Engineering, Asscher Enterprises). Of these, only
Vishkul (the Rs10cr loan) and TAAL Technologies Inc, USA (the intra-group
billing that explains most of the margin question, Part B2) carry
material FY26 transaction amounts in the standalone note. Taneja
Aerospace shows only a trivial FY26 transaction (a Rs1.50 lakh car sale;
B01 FLAG-RPT names this explicitly: the material related-party exposure
is Vishkul, not Taneja Aerospace). The transaction table's own heading
labels Vishkul's transactions under "Entities under common control," even
though Note 37(A) names Vishkul as the "Holding company" two lines above;
this labelling inconsistency is left as found, not resolved.

**9. PLEDGE AND SHAREHOLDING.**

Quote: "Vishkul Enterprises Pvt. Ltd.: 15,81,302 shares / 50.74% (as at
March 31, 2026); 15,81,302 shares / 50.74% (as at March 31, 2025).
Mukul Mahavir Prasad Agrawal: 2,77,931 shares / 8.92% (both dates)."
(Annual_Report_2026, page 86, Standalone Note 16(d))

Quote (promoter group): "Vishkul Enterprises Private Limited: 15,81,302
shares, 50.74%, no change during the year. Salil Baldevraj Taneja: 1,237
shares, 0.04%, no change. Asscher Enterprises Limited (erstwhile known as
Indian Seamless Enterprises Limited): 582 shares, 0.02%, no change."
(Annual_Report_2026, page 86, Standalone Note 16(f), Shareholding of
Promoters)

Comment: The AR discloses shareholding at exactly two dates, 31 March
2026 and 31 March 2025, both annual balance-sheet dates. NOT DISCLOSED:
any quarterly shareholding pattern (the last twelve quarters this
question asks for); no such filing is in corpus (Section 1, gap 3). NOT
DISCLOSED: promoter pledge percentage; the figure of zero pledge carried
elsewhere in this run (B08 pledge_pct_latest: 0) is aggregator-sourced
(screener.in, tijorifinance.com, marketsmojo.com), not primary-verified,
because the primary SEBI shareholding-pattern filing returned a 403 error
on fetch (B08). NOT DISCLOSED in this AR: institutional (FII/DII) holding
as a distinct figure; B00 notes the FY2025-26 AR carries the pattern only
to 31 March 2026, so any post-March-2026 institutional trend is stale by
at least one quarter relative to run date.

**10. VERIFICATION.**

| Document quoted in this annex | Date |
|---|---|
| Annual_Report_2026.pdf (FY2025-26 Annual Report) | Filed to BSE 7 August 2026 |
| Results_Q4FY26_Mar_2026.pdf | Quarter/year ended 31 March 2026 |
| Results_Q1FY27_Jun_2026.pdf | Quarter ended 30 June 2026 |
| Results_Q3FY26_Dec_2025.pdf | Quarter ended 31 December 2025 |
| other/Revised_Consolidated_Assets_Liabilities_Mar_2026.pdf (27 May 2026 corrigendum) | 27 May 2026 |

CORPUS COMMIT HASH: 299e832a8af4c1ded9d2ec549166a8c25f324510

---

*End of Halt 1 Understanding Dossier. Stages 10 and 11 did not run. No
fair value, no destination PE, no entry zone and no BUY/WATCHLIST/AVOID
appear anywhere in this document. The operator reads this dossier, closes
the corpus gaps named in Section 1, signs the Mental Model Declaration in
claude.ai, and decides KILL / SHALLOW WATCH / PROCEED.*
