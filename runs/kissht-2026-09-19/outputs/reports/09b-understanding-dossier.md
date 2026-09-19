# HALT 1 UNDERSTANDING DOSSIER: KISSHT (OnEMI Technology Solutions Ltd)

Run date 2026-09-19. Assembled from committed blocks B00 through B09, the
verifier blocks B12a-B12d, the confidence-delta block, and the phase-1-lite
B13-synthesis outputs. No new research. No web claims. No valuation, price,
or verdict vocabulary, except the one scoped exception in Part B4 below.

This dossier is the Halt 1 deliverable. The operator reads it, resolves the
named corpus gaps, signs the Mental Model Declaration in claude.ai, and
decides KILL / SHALLOW WATCH / PROCEED. Nothing here is that decision.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

**1. Concalls.** Two transcripts held: Q4 FY26 (Concall_Jun_2026_Transcript.pdf,
call 29-May-2026) and Q1 FY27 (Concall_Aug_2026_Transcript.pdf, call
30-Jul-2026). These are ALL calls the company has held since its 08-May-2026
listing (B00). Most recent quarter covered: Q1 FY27 (quarter ended
30-Jun-2026). Today is 19-Sep-2026, inside Q2 FY27 (Jul-Sep), which has not
yet closed. No more recent quarter has plausibly reported; nothing is
missing here.

**2. Annual reports.** One held: Annual_Report_2026.pdf, FY2025-26, 138 pp
(B00). This is the latest completed FY (year ended 31-Mar-2026) and it is
present. Fewer than 3 years are held: the company was unlisted before
08-May-2026 and published no prior listed-company AR. The RHP's restated
FY23-FY25 financials carry the backward baseline instead (B00 input_gaps).

**3. Results filings.** Two held: Q1 FY27 unaudited (board 29-Jul-2026) and
FY26 audited including Q4 (board 27-May-2026) (B00 inventory.results). Latest
filing is Q1 FY27. No quarter-gap against the AR: FY26 audited results
(year end) and the AR cover the same period. No Q3 FY26 results filing
exists on BSE for this company; it was unlisted until 08-May-2026, so this
is plausibly-nonexistent, not a collection miss (B00 input_gaps).

**4. Investor presentations.** Two held: Q1 FY27 deck (Investor_Presentation_1.pdf,
29-Jul-2026) and Q4 FY26 deck (28-May-2026) (B00 inventory.presentation).
Latest held matches the latest results filing.

**5. Research / rating.** One rating document: CRISIL rationale for
subsidiary Si Creva Capital Services, dated 13-Feb-2026
(inputs/rating/CRISIL-SiCreva-RR-2026-02-13.txt). It rates the subsidiary,
not the listed parent (B00). Research folder is EMPTY: no broker notes exist
in the corpus (B00 input_gaps).

**6. Corporate actions.** 26 BSE Reg 30 / LODR filings held, dated
08-May-2026 to 18-Sep-2026: KPI filings, press releases, a monitoring
agency report, two acquisitions, management changes, a director
resignation, a postal ballot, an ESOP allotment, an MoA/AoA amendment, and
the 17-Sep-2026 preferential issue plus its 18-Sep-2026 press release (B00
inventory.announcements).

**7. Freshness pair check.** B00's freshness_verdict is FRESHNESS PAIRS OK.
All four pairs PASS: RESULTS to CONCALL (Q1 FY27 results matched by the
Aug-2026 concall), RATING BULLETIN to RATIONALE (the CRISIL file IS the full
rationale, not a bulletin), SEBI ORDER to ORDER TEXT (no SEBI order found
anywhere in the corpus; only an FIU-IND notice and an NFAC tax SCN, neither
a SEBI order), AR to LATEST AUDITED ANNUAL RESULTS (FY26 audited results
match the FY26 AR). No pair failed.

**8. Verdict line: CORPUS GAPPED.**

- FII/DII institutional sub-split within the 75.20% public shareholding:
  NOT FOUND. Findable-but-missing; expected source: BSE shareholding
  pattern detail filing, not yet automated by the collector (B00 input_gaps,
  B01 input_gaps E1).
- SBICARD screening Data_Sheet CSV: NOT FOUND (screener export defect).
  Findable-but-missing; expected source: screener.in export, re-pushed after
  the collector fix (B00, B01 input_gaps M5).
- Q3 FY26 (and earlier) results filings: plausibly-nonexistent. The company
  was a private entity until 08-May-2026 and filed no BSE results before
  listing (B00 input_gaps).
- Prior-year (FY25 and earlier) listed annual reports: plausibly-nonexistent
  for the same reason.
- Broker research notes: plausibly-nonexistent this early post-listing (one
  quarter, two concalls); itself a data point, not yet a gap to chase.
- FLDG-in-opex quantum for Q1 FY27 and the numeric DPD write-off trigger:
  NOT FOUND anywhere filed. This is not a collector gap; management could
  not supply the FLDG figure on request on its own call (B05 input_gaps),
  and no filed note in the AR or the RHP states a numeric write-off trigger
  (B02, B03). Findable only through a live management query or a future
  filing.
- MCA/RoC status for nine promoter-group private entities, and SEBI SCORES
  complaint history: NOT FOUND; both need a paid lookup service outside this
  container (B08 input_gaps).

---

## SECTION 2: MENTAL MODEL DECLARATION

**STATUS: DRAFT - PENDING OPERATOR SIGN-OFF.** Nothing in this section is
signed. Signing happens only in claude.ai after live-web stress-testing.

### PART A: THE FROM STATE

**A1. Archetype.** Lender (CLAUDE.md ARCHETYPE LIBRARY). Confirmed at B00
and re-confirmed at B04: revenue is interest and fee income on a loan book,
not a software or platform fee; the collector's initial "Platform / SaaS /
IT services" guess is rejected (B00 sector_cap_row_evidence, B04
sector_cap_row_confirmed). The listed parent, OnEMI, does not itself lend;
on-book interest income sits entirely inside wholly owned NBFC subsidiary
Si Creva, and the parent earns sourcing fees plus an intercompany guarantee
fee (B04 analyst_note).

**A2. The simple analogy.** Kissht is an app that gives small, short unsecured
loans to people who want credit fast without visiting a branch. Personal
loans are 92.3% of the Rs 8,001 Cr loan book (Jun-2026); a newer loan
against property product sold through 101 branches is the other 7.7% (B04,
B00 analyst_note). About half the book, 53.6%, sits on eight partner
lenders' balance sheets rather than Kissht's own; Kissht covers a slice of
their first losses. Interest earned on loans Kissht holds itself is 58.4%
of revenue, fees for sourcing and servicing partner-held loans are 26.6%,
late and foreclosure fees are 11.1% (B04 revenue_streams).

### PART B: THE TRANSITION

**B1. FROM to TO** (lender-specialised rungs, asset quality and RoA, not
product spec, per CLAUDE.md QUALITY LADDER).

*Line 1: unsecured personal loan book (92.3% of AUM).* FROM = R1
COMMODITY PRICE-TAKER, lender-specialised: weak pricing power (B04
pricing_power: "weak"), cyclical asset quality (B04 cyclicality:
"cyclical"), a credit-cost history that ran 8.85% to 9.7% of average AUM as
recently as FY25-26 (step1 brief; Concall_Jun_2026 p.8), and ROE not yet
proven durable across a stress cycle. Two readings separate on the TO
state, and the evidence does not yet resolve them: **Reading 1 (more
evidenced):** R2 COST-ADVANTAGED CONVERTER, lender-specialised, margin
improving from a funding-cost advantage (CRISIL A- upgrade, Feb-2026;
guided 100-300 bps further cuts, Concall_Aug_2026 p.11-12) and from
underwriting selection, not from pricing power the company does not have.
**Reading 2 (management's own claim):** R3 VALUE-ADDED / SPEC'D SUPPLIER,
lender-specialised, where the proprietary underwriting-data stack (400+
variables, AUC 66% to 74%, B07 D1) gives durable, stickier, lower-loss
economics in the 20-25% RoE band the company guides to (19-21% FY27,
Concall_Jun_2026 p.9). **The observation that separates them:** B07's own
Family I test scores the underwriting edge 0 for cannibalization barrier
(I2): no competitor has to sacrifice anything to copy it, which makes it an
execution lead, not a structural barrier (B07 flags,
FLAG-EMOAT-EXECUTION-LEAD). Repeat-customer AUM share, the direct evidence
of the stickiness Reading 2 needs, fell from 73% to 49% in one year (AR p.7,
B04 FLAG-BUSINESS-MODEL). The most evidenced path is Reading 1: a
cost-of-funds and underwriting-selection improvement inside the R1/R2
boundary, with Reading 2's franchise claim not yet evidenced.

*Line 2: loan against property, LAP (7.7% of AUM, embryonic).* FROM =
sits below R1, not yet an established rung: a nascent, branch-dependent
product line disclosed inconsistently across three filed documents (AR up
to Rs 30 lakh/15yr, Q1 FY27 deck up to Rs 15 lakh/10yr, CRISIL up to Rs 20
lakh/10yr; B04 FLAG-DISCLOSURE-INCONSISTENCY). TO, per management's own
claim = R2, a cost-advantaged secured lending line diversifying the book,
but this is not yet evidenced: branch rollout added only 3 branches in Q1
FY27 against a guided pace implying about 27 a quarter (B05
FLAG-LAP-PACE), and no LAP-specific asset-quality figure is disclosed
anywhere in the corpus (B12b I16).

**B2. The engine** (Line 1, the load-bearing line). Two things, evidenced:
(1) funding-cost decline from rating upgrades: CRISIL upgraded Si Creva to
A-/Stable on 13-Feb-2026 (step1 brief), and management guides a further
100-300 bps cut over the next 3 quarters to 3 years (Concall_Aug_2026
p.11-12, p.15). (2) underwriting and collections model improvement: AUC
rose from 66% to 74% between 2023 and 2026 (B07 active_categories D1),
alongside a stated, deliberate shift toward higher-quality borrower
segments even at the cost of near-term yield compression (Concall_Jun_2026
p.7-8).

**B3. The proof gate.** Sequential Gross NPA (Stage 3) at or below 2.25%
(the guided FY27 ceiling, Concall_Jun_2026 p.9) AND Stage 2 back at or
below 2.4% (its Q4 FY26 level; it rose to 3.15% in Q1 FY27, B12b I3) for
two consecutive quarters, reported together with a write-off rate that has
not accelerated past the FY26 pace of about 15.7% of the average book (B02
rank 2). This is the exact metric and threshold Stage 11 FTTCP should test.
Until it fires across two quarters, the asset-quality leg of the engine is
narrative, not proof: one quarter (Q1 FY27) already moved the wrong way
while management called it "a technicality... not anything to do with
credit quality" (B05 FLAG-FRAMING-GNPA) and, separately, "seasonal", a
framing same-quarter peers SBICARD and POONAWALLA do not support with their
own improving asset quality (B12b finding P1).

**B4. The recognition gap (OPEN QUESTION, resolved at Stage 11).** Whether
the market already prices the TO state (a cost-advantaged, or franchise-tier,
lender) is an open question this dossier does not answer. Step-1 carried a
trailing PE of about 19.9x at a CMP of Rs 356 against a sector cap row of
18x P/B-primary for Banks/NBFCs/MFIs (B00 sector_cap_row); whether that gap
is already closed, and by how much, is exactly the PE gap Stage 11 resolves
under the Section 1B lender variant. No number, no fair value, and no
conclusion is stated here.

**B5. The ugliness test.** Two ugly optics, read differently. (a) Cumulative
CFO of minus Rs 1,648.00 Cr against cumulative PAT of plus Rs 671.20 Cr,
FY21-26 (B01 flags FLAG-CASH), narrowing from minus Rs 661.43 Cr to minus
Rs 460.82 Cr FY25 to FY26 (B01 block_b_trend): classified
**ARTIFACT-OF-CLIMB**. Three stages independently read this as an Ind AS 7
loan-growth mechanic, not a cash-quality failure (B01, B03 strengths_top3,
B04 irrelevant_ratios), and B13's own FLAG-CASH determination stops short
of calling it resolved (INDETERMINATE, not GROWTH-INDUCED), because the
loss content behind the growth is not yet certified. (b) The parent
corporate guarantee to Si Creva's lenders, 228% of the parent's own
standalone net worth in FY26, rising every year for four years from 70.3%
in FY23 and first exceeding 100% in FY24, two years pre-IPO, backing 99.8%
of the subsidiary's NCD book: classified **STRUCTURAL-FEATURE**, in the
evidence stage's own words, "a structural, worsening trend independent of
the IPO, not an IPO-adjacent optic" (B02 top_findings rank 1). It is never
named in the AR's own "Balanced liability base" diversification narrative
(B03 analyst_note) and never raised on either call (B05
FLAG-SILENCE-GUARANTEE).

**B6. The transition falsifier.** The single most damaging near-term print:
Q2 FY27 gross NPA above 2.25% with Stage 2 not back toward 2.4% (B13
falsification_metric). A second, independent falsifier: cost-to-income
continuing to worsen past 56.64% (FY26, up from 45.54% FY24, B01
FLAG-QUALITY) for another year, which would directly contradict the
"opex falls with scale" claim the engine depends on (B04 FLAG-BUSINESS-MODEL,
Investor_Presentation_1 p.5).

### PART C: WHAT THE MODEL WATCHES

**C1. Dominant variables.**
1. GNPA / Stage-3 trajectory versus the write-off rate. Current state: GNPA
   2.12% FY26, 2.25% Q1 FY27 (sequential rise); write-offs about 15.7% of
   average book (+10.7% YoY) against new Stage-3 inflow up 28.9% YoY (B02
   rank 2, B03 FLAG-ASSET-QUALITY).
2. FLDG cost and off-book loss content. Current state: off-book AUM Rs
   4,284 Cr (53.6%), FLDG outstanding at the parent Rs 737.80 mn (AR p.118
   CARO Annexure A, B03), FLDG cost more than tripled to about Rs 2.5 bn
   group-wide in FY26 (B02 rank 3), booking line (credit cost vs opex)
   unquantified and answered inconsistently on the Q1 FY27 call (B12b I1).
3. Cost of borrowing, tied to the rating trajectory. Current state: A-
   rating (CRISIL, Feb-2026); guided 100-300 bps further cut, contradicted
   by same-quarter peer commentary on system-wide funding costs (B06
   FLAG-COST-OF-BORROWING-TAILWIND-CONTRADICTED).
4. Cost-to-Income ratio, the operating-leverage claim. Current state:
   worsened from 45.54% (FY24) to 56.64% (FY26) even as AUM grew 73% (B01
   FLAG-QUALITY, B04 FLAG-BUSINESS-MODEL).

**C2. What the model rejects.** Market size. TAM is about Rs 26-27 lakh
crore growing roughly 20-22%, the digital-lender SAM is growing roughly 47%
off a 2.3%-of-TAM base, and Kissht holds about 6.2% of that SAM with 23.4x
revenue headroom; the run grades the runway MASSIVE (B09). Market size is
not the binding constraint; execution and disclosure on the loss side are.
The model also rejects "which named competitor gains share" as a live
question for now: no peer transcript in this container names Kissht,
Bajaj, or Chola as a share gainer or loser (B06 unverifiable), so this
question has no evidence to move on yet.

**C3. The business falsifier** (distinct from B6, kills the FROM business,
not just the transition). The parent corporate guarantee (228% of the
parent's own net worth, FY26) being called upon, or disclosed to be
crystallising in any form, would convert a fee-earning listed holding
company into a distressed guarantor of its own subsidiary's lenders,
re-declaring the FROM business itself from "asset-light fee earner over a
funded lending subsidiary" to "contingent-liability-exposed guarantor" (B02
rank 1 and rank 4, B03 FLAG-CAPITAL-STRUCTURE).

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

*(Drafted per the five-question spec in prompts/13-synthesis-pipeline.md,
BUSINESS UNDERSTANDING NARRATIVE section, from B01-B09. Stage 13's own copy
is the version of record and updates as later stages run.)*

**What it sells, and why it matters.** Kissht sells small unsecured
personal loans through a mobile app, 92.3% of its Rs 8,001 Cr loan book,
and a newer loan against property product sold through 101 branches, the
other 7.7% (B04, B00). The listed parent does not lend; the loans sit in
wholly owned NBFC subsidiary Si Creva, and the parent earns sourcing fees
and a guarantee fee instead (B04 analyst_note). Interest on loans it holds
itself brings 58.4% of revenue, fees for sourcing and servicing loans that
partner lenders hold bring 26.6%, and late-payment and foreclosure charges
bring 11.1% (B04 revenue_streams).

**Who buys, and why.** The borrower is a mass-market or mass-affluent
Indian who wants credit fast without a branch visit (B04, B09
market_definition). These borrowers are not locked in: repeat-customer
share of the book fell from 73% to 49% in one year, and management states
about 45% of customers already carry another personal loan elsewhere (AR
p.7, B04 FLAG-BUSINESS-MODEL; B12b I8). The second buyer is the partner
lender: eight partners hold 53.6% of the book off Kissht's own balance
sheet, and Kissht covers a capped slice of their first losses in exchange
for sourcing and servicing fees (B04, step1 brief).

**Why demand exists.** Across all lenders, the India personal loan and LAP
market is about Rs 26-27 lakh crore (B09 tam_cr), independently corroborated
within 2-13% on the personal-loan leg by four market-research aggregators
(B09 flags FLAG-TAM-SOURCE). The "new age / digital lender" slice
management targets was Rs 60,000 Cr in FY25, about 2.3% of that total (B09
sam_cr, sam_pct_of_tam). Bureau data (CRIF High Mark, TransUnion CIBIL,
Equifax) and the RBI Financial Stability Report are the outside checks on
whether that demand stays healthy; neither was fetched in full in this
container (B09 downstream_candidates, stale_data_flags).

**Why demand should grow.** Formal employment and tax-filing growth widen
the pool of borrowers who qualify for credit; EPFO payroll additions, GST
collections and ITR filing counts are the monthly proxies for that (B09
downstream_candidates). The digital-lender slice is forecast to reach Rs
4.1 lakh Cr by FY30 in the company-commissioned 1Lattice study (B09
mgmt_claim_cr), a forecast independently corroborated only on its
personal-loan leg, not on the LAP leg or the mass-market funnel used for
SAM (B09 flags). How much of that demand Kissht itself can serve also
depends on partner appetite: 53.6% of the book already sits off-balance
sheet, and RBI's co-lending and digital-lending directions set the ceiling
on how far that share can run (B09 downstream_candidates).

**Where the advantage sits, and where it does not, per line.** On the
personal-loan line, the one documented edge is underwriting: 400+
variables, 40 models, AUC up from 66% to 74% between 2023 and 2026 (B07
D1). It is, on the corpus's own moat-family test, an execution lead rather
than a structural barrier: no named competitor would have to sacrifice
anything in its own business to copy it (B07 I2, FLAG-EMOAT-EXECUTION-LEAD).
Brand (a Sachin Tendulkar endorsement), distribution breadth, and a
cross-sell funnel are each rated moderate at best, and the cross-sell claim
sits beside a same-document contradiction: repeat-customer share falling,
not rising (B04 moats_present, B07 top_moat_risks). On the LAP line, no
moat evidence exists at all; the line is 7.7% of AUM, disclosed
inconsistently across three filed documents, and running at roughly a
ninth of its guided branch-expansion pace (B04 FLAG-DISCLOSURE-INCONSISTENCY,
B05 FLAG-LAP-PACE).

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. Verticals framed (from the dominant variables, Part C1)

**Vertical 1: GNPA / Stage-3 trajectory versus write-off rate.**
Corpus establishes: GNPA improved 2.89% (FY25) to 2.12% (FY26) while
write-offs ran about 15.7% of the average book, up 10.7% YoY, against new
Stage-3 inflow up 28.9% YoY (B02 rank 2); Q1 FY27 GNPA rose sequentially to
2.25% and Stage 2 rose from 2.4% to 3.15% (B12b I3); the 150-DPD write-off
trigger management cited on the Q4 FY26 call appears in no filed note of
the AR or the RHP (B02, B03). Corpus cannot establish: whether the
underwriting edge (AUC 66% to 74%) holds through a genuine stress cycle
rather than the benign one since IPO (B07 optionality_register); whether
bureau-level data corroborates or contradicts management's "divergence
beneath a calm surface" framing (B09 downstream_candidates). Deciding
questions: (1) does GNPA/Stage 2 revert in Q2 FY27 without an accelerating
write-off rate? (2) does a numeric write-off trigger ever get disclosed?
(3) do bureau reports show the same divergence pattern management
describes?

**Vertical 2: FLDG cost and off-book loss content.**
Corpus establishes: off-book AUM is Rs 4,284 Cr (53.6%) across eight
partners; FLDG outstanding at the parent is Rs 737.80 mn (AR p.118 CARO
Annexure A); FLDG cost more than tripled group-wide to about Rs 2.5 bn in
FY26 (B02 rank 3). Corpus cannot establish: whether FLDG utilisation books
in credit cost or opex (management could not answer on the Q1 FY27 call,
and gave inconsistent answers within that same call, B05 input_gaps, B12b
I1); which partner banks/NBFCs carry the off-book exposure, or their own
capacity to keep extending it. Deciding questions: (1) does a Q2 FY27
disclosure finally quantify FLDG-in-opex bps? (2) does any partner get
named? (3) does RBI tighten DLG/co-lending caps in the interim?

**Vertical 3: Cost of borrowing tied to the rating trajectory.**
Corpus establishes: CRISIL upgraded Si Creva to A-/Stable, 13-Feb-2026;
management guides a further 100-300 bps cut over 3 quarters to 3 years
(Concall_Aug_2026 p.11-12, p.15); same-quarter peers SBICARD and
POONAWALLA independently describe funding costs as flat-to-rising, not
easing, contradicting Kissht's cited system-wide tailwind (B06
FLAG-COST-OF-BORROWING-TAILWIND-CONTRADICTED). Corpus cannot establish:
whether a second rating-agency notch upgrade actually lands within FY27
(B07 catalysts_12m, "claim" evidence type only). Deciding questions: (1)
does a second upgrade print? (2) does incremental cost of borrowing keep
falling company-specifically even as peers report rising funding costs?

**Vertical 4: Cost-to-Income ratio, the operating-leverage claim.**
Corpus establishes: Cost-to-Income worsened from 45.54% (FY24) to 56.64%
(FY26) even as AUM grew 73% and PAT grew (AR p.10 KPI table, B01
FLAG-QUALITY); management's own operating-leverage claim (opex and cost of
borrowing as % of avg AUM falling with scale, Investor_Presentation_1 p.5)
runs the opposite direction of the disclosed record so far (B04
FLAG-BUSINESS-MODEL). Corpus cannot establish: a driver-level breakdown of
what is pushing Cost-to-Income up (branch rollout cost, technology spend,
FLDG-related opex, or something else); no note isolates the cause.
Deciding questions: (1) does Cost-to-Income turn down in FY27? (2) can
management name the specific driver of the FY24-26 rise when asked?

### 4b. Candidate signal table (expanded from B09 downstream_candidates)

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| RBI Master Directions on Digital Lending / Co-Lending (FLDG caps, risk weights) | A new circular tightening DLG caps or unsecured-PL risk weights below what the current 53.6% off-book share assumes | Event-driven | RBI press releases / Master Directions |
| CRIF High Mark / TransUnion CIBIL / Equifax bureau-level unsecured-PL and small-ticket delinquency reports | Bureau data shows system-wide deterioration NOT matched by Kissht's own reported GNPA improvement, or shows deterioration Kissht's write-off rate is quietly absorbing | Quarterly | CRIF High Mark / TransUnion CIBIL published reports |
| Off-book lending partner banks/NBFCs (45+ active co-lending/DA partners) | Any named partner publicly reduces or exits its co-lending line with Kissht/Si Creva | Quarterly | RBI co-lending sector data; individual partner disclosures |
| Named new-age peer AUM/PAT prints (KreditBee, Navi, Fibe, Moneyview) | Kissht's AUM growth or asset quality falls behind this peer set for two consecutive periods | Event-driven | CARE Ratings / CRISIL rating rationales; peer ARs/DRHPs |
| EPFO net payroll additions, GST collections, ITR filing counts | A sustained multi-month deceleration in formal-sector payroll additions | Monthly | EPFO, GSTN/CBIC, CBDT releases |
| RBI Financial Stability Report (systemic credit growth, retail slippage composition) | The FSR flags unsecured-retail stress as systemic and worsening, contradicting the "divergence, not sector-wide" framing management uses | Event-driven (semi-annual) | RBI Financial Stability Report |

### 4c. Fragility read

- **variable_count:** 5 (GNPA/write-off truth; FLDG/off-book loss content;
  cost of borrowing/rating trajectory; Cost-to-Income; AUM growth
  sustaining the >40% FY27 guidance).
- **verifiability_ratio:** 3 of 5 externally observable (AUM growth via BSE
  filings; cost of borrowing via public rating-agency actions; Cost-to-Income
  via the audited AR). 2 of 5 company-narrated only, with no independent
  cross-check found in this container: the true write-off-adjusted asset
  quality, and FLDG loss content and its booking line.
- **single_point_failure:** FLDG/off-book loss content and its booking
  line. It is undisclosed, management could not quantify it on request, and
  gave contradictory answers within the same call (B05 input_gaps, B12b
  I1). If it proves materially worse than the 6.80% credit-cost figure
  implies, it would undercut the credit-cost leg of the engine (B2) and the
  business falsifier (C3) at once, since the same guarantee structure
  backstops both the on-book and off-book losses.
- **fragility_verdict: FRAGILE.** Two of five dominant variables are
  company-narrated only, one of those two is a named single point of
  failure, and an independent verifier (B12b) and an independent peer
  cross-check (B06) each separately found management's own framing
  overstated or unsupported on at least one material claim in the same
  quarter it was made.

### 4d. Research brief (claude.ai live-web work order)

1. FLDG utilisation in bps of off-book AUM, and its booking line (credit
   cost vs opex): check the Q2 FY27 results annexures and investor deck
   (Chain 1 below).
2. Identify the off-book partner banks/NBFCs (45+ partners, 8 carrying
   53.6% of AUM) via RBI co-lending sector data or partner disclosures
   (Chain 1 binding constraint).
3. Cross-check CRIF High Mark / TransUnion CIBIL / Equifax bureau-level
   unsecured-PL delinquency data against Kissht's own asset-quality claims
   for the same period (Chain 2 below).
4. Check the Q2 FY27 concall/results for whether GNPA and Stage 2 revert,
   and whether management engages the write-off-rate mechanic directly
   this time (Chain 2 confirm-by).
5. Monitor RBI Master Directions on digital lending / co-lending / DLG caps
   for any tightening (B09 candidate 1).
6. Pull named new-age peer AUM/PAT prints (KreditBee, Navi, Fibe,
   Moneyview) via CARE/CRISIL rating rationales or DRHPs (B09 candidate 4).
7. Track EPFO net payroll additions, GST collections, and ITR filing counts
   monthly as the TAM-growth proxy (B09 candidate 5).
8. Fetch and parse the full RBI Financial Stability Report (only a
   search-engine synthesis was used in this container, B09 stale_data_flags).
9. Fetch and parse the CRIF High Mark "How India Lends" / DLAI-CRIF Fintech
   Barometer PDFs (links surfaced, not parsed, B09 searches_skipped).
10. Check the outcome of the 14-Oct-2026 EGM on the Rs 832 Cr preferential
    issue, and whether any numeric capital-need rationale is finally given
    (LBF-4, B05 FLAG-CAPITAL-RAISE-SILENCE).
11. Verify the current status of the ED (Enforcement Directorate) PMLA
    summons to Si Creva, dated 23-Mar-2023, open as of the RHP (B08
    searches_skipped: court-docket verification).
12. Run a paid MCA/RoC company-master lookup on the nine promoter-group
    private entities named in the RHP (B08 STAGE-8 ADDITION).
13. Check SEBI SCORES for any complaint history against the company or its
    promoters (B08 searches_skipped).
14. Obtain the FII/DII institutional sub-split from the next BSE
    shareholding pattern filing, to close the UA institutional qualifier
    (B00/B01 E1, NOT FOUND).
15. Find an independent, non-1Lattice source for LAP-only market size (B09
    STAGE-9 SPECIFIC gap).
16. Verify the live CMP, market cap, and trailing PE (step1 brief figures:
    Rs 356, Rs 6,312 Cr, 19.9x) against a current quote before Stage 11
    uses any pricing input.

### 4e. Second-order stub (Master Prompt v3.7, Rule F)

Two chains drafted from corpus. Rule F floor is five; the remaining three
are built in claude.ai with live web.

```
CHAIN 1: Off-book AUM is Rs 4,284 Cr (53.6% of Rs 8,001 Cr total AUM);
parent FLDG outstanding Rs 737.80 mn (CARO Annexure A, AR p.118); FLDG
cost more than tripled group-wide to about Rs 2.5 bn in FY26 (B02 rank 3,
Standalone Note 25 p.84, Consolidated Note 29 p.119-120).
Link 1 [documented, filed]: Off-book partners hold the loans on their own
  balance sheets; Kissht provides a first-loss default guarantee (FLDG) up
  to 5% upfront on partner books (step1 brief, B04).
Link 2 [documented, concall]: Management could not supply the FLDG-in-opex
  figure on request on the Q1 FY27 call ("not readily available... handy",
  Concall_Aug_2026 p.19-20), and the verifier found three answers on that
  same call that do not agree (B12b I1).
Link 3 [INFERENCE]: If FLDG utilisation books in opex rather than credit
  cost, the reported 6.80%-of-AUM credit cost understates the true loss
  rate on the whole managed book (on- and off-balance-sheet), which would
  mean the credit-cost leg of the transition engine (Part B2) is partly an
  accounting-location effect, not a real risk reduction.
Binding constraint: whether the eight off-book partners keep extending
  co-lending/DA lines at the current 53.6% share depends on their own
  capital and risk appetite, a fact the AR's "Balanced liability base"
  narrative discusses only as diversification, never as a dependency (B03
  analyst_note).
Unsaid: neither call names a single off-book partner, a per-partner FLDG
  cap, or a specific utilisation number; the parent guarantee that
  ultimately backstops much of this structure (228% of parent net worth)
  is never mentioned on either call either (B05 FLAG-SILENCE-GUARANTEE).
Who pays, and why now: PENDING LIVE VERIFICATION. Claude web should open
  the Q2 FY27 results annexures and investor deck (expected late Oct/early
  Nov 2026), and any RBI co-lending or DLG circular update, to find whether
  FLDG utilisation is now disclosed, which off-book partner banks/NBFCs are
  named, and why they continue funding an unsecured PL book at current DLG
  caps.
Observation that confirms or breaks this chain, and confirm-by date: a
  numeric FLDG utilisation figure (bps of off-book AUM) and its booking
  line (credit cost vs opex), disclosed on or before the Q2 FY27 results
  (expected late Oct/early Nov 2026). A third consecutive quarter with no
  number breaks confidence in the credit-cost narrative.

CHAIN 2: GNPA (Stage 3) improved from 2.89% (FY25) to 2.12% (FY26) while
write-offs ran about 15.7% of the average book (+10.7% YoY) against new
Stage-3 inflow up 28.9% YoY (B02 rank 2, Consolidated Note 41 pp.127-129,
Note 26 p.119); Q1 FY27 GNPA rose sequentially to 2.25% and Stage 2 rose
from 2.4% to 3.15% (B12b I3, Concall_Aug_2026 p.5-6, p.8-10).
Link 1 [documented, filed]: the 150-DPD write-off trigger management cited
  on the Q4 FY26 call, moved from 120 DPD, appears in no filed note of the
  AR or the RHP (B02, B03).
Link 2 [documented, concall]: management framed the Q1 FY27 rise as "a
  technicality... not anything to do with credit quality" on the Q4 call
  (B05 FLAG-FRAMING-GNPA, Concall_Jun_2026 p.19-20) and as seasonal on the
  Q1 call, while same-quarter peers SBICARD and POONAWALLA both improved
  asset quality (B12b finding P1).
Link 3 [INFERENCE]: if the FY26 GNPA improvement is substantially a
  write-off-timing effect rather than an underwriting-quality effect, the
  FY27 guidance path (GNPA below 2.25%, credit cost down 10-15%) is more
  fragile than management's framing suggests: the same write-off lever
  cannot indefinitely mask a rising Stage-3 inflow rate without either an
  accelerating write-off pace, which would raise future credit cost, or an
  eventual headline GNPA breach.
Binding constraint: the underwriting AUC edge (66% to 74%, 2023-2026) is
  documented, but whether it holds through a genuine stress cycle, not just
  the benign one since IPO, is an open, unconverted optionality item, not
  yet evidenced (B07 optionality_register).
Unsaid: neither call cites an independent bureau-level cross-check of the
  borrower base, and no analyst on either call asks about the 228%-of-net-
  worth parent guarantee that ultimately backstops the funding behind this
  book (B05 FLAG-SILENCE-GUARANTEE).
Who pays, and why now: PENDING LIVE VERIFICATION. Claude web should check
  CRIF High Mark / TransUnion CIBIL / Equifax bureau-level unsecured-PL
  delinquency data for the same period, and the Q2 FY27 concall/results for
  whether management engages the write-off-rate mechanic directly, rather
  than repeating a "technicality" or "seasonal" framing.
Observation that confirms or breaks this chain, and confirm-by date: Q2
  FY27 results (expected late Oct/early Nov 2026) showing GNPA at or below
  2.25% AND Stage 2 at or below 2.4% AND a write-off rate that has not
  accelerated past the FY26 pace, reported together. A further sequential
  GNPA/Stage-2 rise, or an unexplained write-off-rate acceleration, breaks
  the chain.
```

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in
claude.ai with live web, before Role 2.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. Kissht is an app that gives small personal loans fast, without a branch
   visit, and it also runs a small property-backed loan business through
   101 branches.
2. The loans sit inside a lending subsidiary, Si Creva. The listed parent
   does not lend directly; it earns sourcing fees and a guarantee fee.
3. About half the loan book, 53.6%, sits on eight partner lenders' books,
   not Kissht's own, and Kissht covers a slice of their first losses.
4. Borrowers are mass-market and mass-affluent Indians who want quick
   credit. Almost half already carry another personal loan elsewhere.
5. These borrowers are not loyal. The share of the book from repeat
   customers fell from 73% to 49% in one year.
6. Demand for personal credit in India is large and growing. Bureau reports
   and payroll data are the outside checks on whether that demand stays
   healthy; those checks are not yet done in this container.
7. Market size is not the limit here. Kissht holds a small share of a fast
   growing slice of a very large market.
8. The one real edge is underwriting: 400-plus data variables and a rising
   model accuracy score. No competitor has to give up anything to copy it,
   so it is a lead, not a wall.
9. The company's mental model is a climb from a plain, cyclical, unsecured
   lender toward a lender with a real cost or data edge. The most evidenced
   reading is a funding-cost and underwriting-selection improvement, not
   yet the fuller franchise story management itself claims.
10. This model is fragile. Two of five variables that must go right rest on
    the company's own word alone, with no outside source to check them.
11. The single biggest risk to watch: the cost of covering partner-loan
    losses (FLDG). Management could not give a number for it, and gave
    answers on one call that did not agree with each other.
12. The corpus could not establish a numeric trigger for when a loan gets
    written off, even though management named one on a call.
13. The corpus could not establish who the eight off-book partner lenders
    are, or how much of the guarantee behind them the parent could actually
    honour if called upon.
14. The two biggest open questions: does asset quality reverse its Q1 FY27
    slip, and does the company ever put a number on its guarantee cost and
    its funding structure's limits.
15. A parent guarantee to the lending subsidiary's lenders, now 228% of the
    parent's own net worth, has never been named as a risk in the annual
    report's own risk narrative, and neither call has raised it.

---

## SECTION 6: STANDING EXTRACTION ANNEX

**1. UNITS.** No single per-unit figure (like realisation per tonne) applies
to a lender; the closest printed equivalents are return ratios per unit of
average AUM. Quote (AR KPI table, Annual_Report_2026.pdf p.5): "5.05%
RoAAUM +25 bps" and "23.97% RoAE +622 bps". Both cover the whole loan book
(PL plus LAP combined), not a single product. Comment: these are basket
figures, not product-specific. The volume and revenue lines from which a
product-level figure could in principle be derived are printed separately:
AUM Rs 8,001 Cr with PL 92.3% / LAP 7.7% (Q1 FY27 press release), and Total
Income Rs 2,209 Cr FY26 (AR KPI table, same page). No product-level yield
or NIM percentage is printed anywhere in this container (B04
STAGE-4 SPECIFIC gap).

**2. SEGMENT CAPITAL AND DEBT.** Quote (Annual_Report_2026.pdf p.93,
Standalone Note 40 / p.126, Consolidated Note 44): "The Company operates in
a single business segment. There are no other separate reportable segments.
Hence, no disclosures related to segments is required to be given under...
Ind AS 108." and, at Group level: "The Group's operating businesses are
organised and managed as a single business segment... The Group is
primarily engaged in a single line of business and operates in a single
economic environment... The Group's operations are predominantly within
India and therefore no separate geographical segment disclosure is
considered necessary." Comment: no segment-level assets, liabilities,
capital employed, or borrowings breakout exists, standalone or consolidated,
for the two latest periods, because the company discloses only one
reportable segment. Total consolidated borrowings (debt securities plus
other borrowings) are disclosed unallocated at Rs 23,961.02 mn as at
31-Mar-2026 versus Rs 15,075.81 mn as at 31-Mar-2025 (Consolidated Note 39,
Annual_Report_2026.pdf p.125, fair value table).

**3. GUIDANCE VERSUS ASPIRATION.**
- (a) Guidance with a period. Quote (Concall_Jun_2026_Transcript.pdf p.8-9):
  "We expect to grow at north of 40% in AUM... we are targeting gross NPA
  below 2.25%, year-on-year reduction in impairment costs of 10%-15%...
  we are targeting a return on average AUM in the range of 4.5%-5%, which
  entails a return on average equity in the range of 19-21%." All stated
  for FY27.
- (a) Guidance with a period, cost of borrowing: quote (B05 guidance, from
  Concall_Aug_2026_Transcript.pdf p.11-12, p.15): a minimum 100 bps cut over
  the next 3 quarters from Q1 FY27, and 200-300 bps cumulative over 3
  years.
- (b) Aspiration without a period. Quote (Concall_Jun_2026_Transcript.pdf
  p.22, per B05 guidance): a steady-state on-book leverage of "2.5x-3.0x
  debt-to-equity," stated as a long-run target with no calendar date. Also
  (Concall_Aug_2026_Transcript.pdf p.15, per B05 guidance): an "organic
  acquisition channel share, long-run, of 40-45% (or 40-50%)", unstated
  horizon.
- (c) Capacity or capability only. Quote (Concall_Jun_2026_Transcript.pdf
  p.8): "Off-book AUM stands at Rs 3,510 crore, where we provide FLDG up to
  5%, which is the First Loss Default Guarantee." This states a capped
  exposure mechanism, not a forward growth number.

**4. CONCENTRATION.** Product: PL 92.3% / LAP 7.7% of AUM (Q1 FY27 press
release, per B00 analyst_note). Customer, standalone: quote
(Annual_Report_2026.pdf p.93, Note 40): "The company has identified
customers that individually contributes 10% or more of its total revenue
from external customers. During the year ended 31st March 2026, revenue
from three such customers amounted to Rs 1,936.42 million, Rs 1,711.53
million and Rs 1,570.49 million respectively." These three sum to about
74.7% of standalone revenue from contracts with customers of Rs 6,981.74
million (same page). Customer, consolidated: quote
(Annual_Report_2026.pdf p.126, Note 44): "no revenue from transactions with
a single external customer amounted to 10% or more of the Group's total
revenue during the year ended 31 March 2026 and 31 March 2025." Comment:
the standalone concentration is real (three named-elsewhere partner
counterparties account for most standalone fee revenue) but is masked at
the Group level because those same counterparties are not "external" once
the fee flows are viewed against the whole managed book; B02 flags this as
a genuine cross-statement framing gap (B02 rank 11). Geography: NOT
DISCLOSED separately; the AR states operations are "predominantly within
India" with no state or region-level breakout (Note 44 above).

**5. PROMISE LEDGER.**

| Promise | Date made | Delivery status | Evidence anchor |
|---|---|---|---|
| AUM growth >40% FY27 | Q4 FY26 call | Delivered so far (+61% YoY, +13% QoQ to Rs 8,001 Cr) | Concall_Aug_2026_Transcript.pdf p.3, p.7 |
| Credit cost -10 to -15% YoY FY27 | Q4 FY26 call | Delivered so far (6.80% vs 8.85%) | Concall_Aug_2026_Transcript.pdf p.4, p.9 |
| GNPA below 2.25% FY27 | Q4 FY26 call | Partial (printed exactly 2.25%, up from 2.12%) | Concall_Aug_2026_Transcript.pdf p.4 |
| RoAUM 4.5-5%, RoAE 19-21% FY27 | Q4 FY26 call | Delivered so far (5.05%, 21.20%) | B05 promise_delivery |
| Further cost-of-borrowing cut on second rating upgrade | Q4 FY26 call | Partial (incremental cost down but no second upgrade confirmed) | B05 promise_delivery |
| LAP: at least 80 more branches (98 to 178+) by FY27-end | Q4 FY26 call | Missed pace (only 3 added, 98 to 101) | Concall_Jun_2026_Transcript.pdf p.20 |
| LAP breakeven "a year or two away" | Q4 FY26 call | Reframed, inconsistent (to "around Q3" on Q1 call; B12b found the original flag itself not supported) | Concall_Jun_2026 p.15; Concall_Aug_2026 p.18 |
| 450 pin codes paused, to be reviewed on data | Q4 FY26 call | Delivered (180 of 450 reopened by Q1 FY27) | B05 promise_delivery |
| RHP objects of fresh issue: 75% to Si Creva, 25% general corporate | RHP, 25-Apr-2026 | Delivered (Rs 636.8 Cr of Rs 637.5 Cr utilised, no deviation) | Monitoring Agency Report 20260729-4997d936 p.5, p.8 |

**6. RESTATED BASES.** Quote (OnEMI_RHP_2026-04-25.txt p.334, per B02
restatements_found): the RHP's mandatory restatement schedule shows the
only quantified regrouping in the FY23-FY25 window is "Rs 0.17 mn" (a FY24
revenue/other-income reclassification, immaterial). Quote
(Annual_Report_2026.pdf p.93/125, standalone Note 43 and consolidated Note
46): "Previous year figures have been regrouped and reclassified, wherever
considered necessary, to conform to the current year presentation, to the
extent applicable." Comment: this FY26-vs-FY25 comparative regrouping
language is not quantified anywhere in the AR, and it falls outside the
RHP's own restatement window (which predates FY26 audited figures). Open;
likely immaterial by the FY23-FY25 precedent, but not confirmed (B02).

**7. CORPORATE-ACTION CLAUSES.** The one scheme-type action in the corpus
is the 17-Sep-2026 preferential issue. Quote
(inputs/announcements/20260917-acc1d37a...txt p.1, p.3-4): "Funds raising by
way of a preferential issue on a private placement basis of up to
2,64,93,882 fully paid-up equity shares... at an issue price of INR 314.11/-
... including premium of INR 313.11/- per share, for an amount aggregating
to INR 8,32,19,93,275.02/-... to identified investors (non-promoters)...
subject to the approval of shareholders." Convening date: "an Extra-Ordinary
General Meeting... on Wednesday, October 14, 2026." Number of investors: 34,
per the disclosed Schedule I, all non-promoter institutional/fund
investors (238 Plan Associates LLC, 360 One Equity Opportunity Fund, Axis
Flexi Cap Fund, HDFC Banking & Financial Services Fund, Massachusetts
Institute of Technology, Unity Small Finance Bank Ltd, and 28 others),
with the pre/post-preferential shareholding for each. Relevant date for
pricing: 11-Sep-2026. No promoter or promoter-group entity appears among
the 34 allottees (B08 transition_evidence). Appointed/effective date: not
yet effective; conditional on the 14-Oct-2026 EGM approval. No demerger,
merger, or buyback exists in this corpus.

**8. RELATED-PARTY PERIMETER.** Quote (Annual_Report_2026.pdf p.89,
Standalone Note 34): related parties are the subsidiary, Si Creva Capital
Services Private Limited; KMP Krishnan Vishwanathan (CFO & Director),
Ranvir Singh (CEO & Director), Amit Gupta (CFO, 20-Aug-2024 to
17-Jul-2025), company secretaries Devangi Singh and Shraddha Patangia;
independent directors Alok Bansal, Sangeeta Tanwani, Atul Bheda, Yogesh
Chadha; and nominee director Piyush Kharbanda. FY26 transactions with the
subsidiary: "Corporate Guarantee Fees Income 394.06" (Rs mn), "Interest
Income on loan 66.12", "Sourcing fees income 1,413.15", "Other fees &
charges 240.00", "Grant of ESOP's to employees of subsidiary company
236.17", "Investment in Subsidiary Company 2,250.00" (all Rs mn, FY26 vs
FY25 comparatives in the same note). Note also: "the company has given
corporate guarantee for loans sanctioned to subsidiary company of
Rs24,389.11 million (Previous year: Rs13,134.84 million)." KMP compensation,
FY26: Krishnan Vishwanathan Rs 10.00 mn and Ranvir Singh Rs 10.00 mn each,
standalone (Note 34C, p.89), versus Rs 25.00 mn each, consolidated
(Note 38, p.124-125): "Mr. Krishnan Vishwanathan 25.00... Mr. Ranvir Singh
25.00" (FY26). Comment: the consolidated figure is the fuller compensation
picture; an investor reading only the standalone note understates CEO/CFO
pay by 60% (B02 rank 10).

**9. PLEDGE AND SHAREHOLDING.** Only two shareholding snapshots exist for a
company listed 08-May-2026; no twelve-quarter history is possible. Quote
(inputs/shareholding/BSE-shareholding-summary-Jun2026.txt, quarter ending
Jun-2026): "(A) Promoter & Promoter Group | 2 | 4,17,85,126 | ... | 24.80
[%]"; "Whether any shares held by promoters are pledge or otherwise
encumbered? | No"; "Whether any shares held by promoters are encumbered
under Non-Disposal Undertaking? | No". Institutional (public-category)
holding is not sub-split into FII/DII in this filing; public holding is
75.20% undifferentiated. The AR's own pre-IPO cap table (as at 31-Mar-2026)
gives a fuller picture at that earlier date: Promoter 35.18%, Institutions
Domestic 15.31%, Institutions Foreign 46.65%, Non-Institutions 2.86% (B03
input_gaps). Comment: promoter pledge is 0% at both snapshots available; no
trend exists to report beyond these two points.

**10. VERIFICATION.** Documents quoted in this annex: Annual_Report_2026.pdf
(FY2025-26, 138 pp); Concall_Jun_2026_Transcript.pdf (call 29-May-2026, filed
04-Jun-2026); Concall_Aug_2026_Transcript.pdf (call 30-Jul-2026, filed
04-Aug-2026); OnEMI_RHP_2026-04-25.pdf (dated 25-Apr-2026); BSE
announcement 20260917-acc1d37a-9690-4c21-9a12-e6b82b876843.pdf (17-Sep-2026);
inputs/shareholding/BSE-shareholding-summary-Jun2026.txt (BSE API, fetched
2026-09-19, data as at quarter ending Jun-2026); results filing
20260729-9867adf0-...pdf (Q1 FY27, board 29-Jul-2026, per B05/B12b
citations).

CORPUS COMMIT HASH: 072df3a4c8be75e13aa9c5220b023bc0a057cc70
