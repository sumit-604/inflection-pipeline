# AWFIS — HALT 1 UNDERSTANDING DOSSIER
Awfis Space Solutions Ltd | Run date 2026-09-19 | Stage 09b (assembly only, no new research)

This file assembles what stages 0 through 9 and the phase-1 verifiers already
found. It states no price, no exit multiple, no fair value and no verdict.
The Mental Model Declaration in Section 2 is a DRAFT. Signing happens only
in claude.ai after live-web stress-testing, and no valuation runs until it
is signed and the Halt 1 decision is PROCEED (CLAUDE.md, SPEAR GATE and
PIPELINE SEQUENCE).

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

**1. Concalls.** Four transcripts held: Q2 FY26 (Nov-2025), Q3 FY26
(Feb-2026), Q4 FY26 (May-2026), Q1 FY27 (Aug-2026, quarter ended
30-Jun-2026) (B00 corpus_manifest). The most recent quarter covered is Q1
FY27. Awfis's Q2 FY27 quarter (ending 30-Sep-2026) has not yet closed as of
the 2026-09-19 run date, so no more recent transcript is plausibly missing
(B00 freshness_pairs, RESULTS to CONCALL: PASS).

**2. Annual reports.** Only the FY26 Annual Report is held (176pp including
the 12th AGM notice) (B00). The latest completed FY (year ended 31-Mar-2026)
is present. Fewer than 3 years are held: no FY25, FY24 or earlier AR is in
the corpus. The IPO Prospectus (27-May-2024) carries restated FY21-FY23 and
9M-FY24 financials as a partial backward substitute (B00 corpus_manifest),
but it is not an Annual Report and does not carry Notes, CARO or governance
detail for those years.

**3. Results filings.** The latest quarterly filing is Q1 FY27 (filed
13-Aug-2026, quarter ended 30-Jun-2026) (B00). No quarter-gap exists between
the latest results filing and the latest AR: the FY26 audited results
(25-May-2026) and the FY26 AR share the same board-approval date, and Q1
FY27 results post-date both.

**4. Investor presentations.** Only the Q1 FY27 deck (13-Aug-2026) is held
(B00 input_gaps: "presentation: 1 deck ... Q4 FY26 and earlier decks are
not held"). This deck carries the load-bearing agreed-upon-procedures cash
EBITDA bridge (B04 FLAG-CASH-BRIDGE-CONFIRMED), so the single held deck is
substantive, but no quarterly history before it exists in the corpus.

**5. Research / rating.** research/ is EMPTY: no broker note is held (B00).
rating/ holds the India Ratings letter of 03-Jul-2026 (full rationale,
9pp, read via page-images because the PDF text layer is scrambled) and the
prior rationale of 16-May-2025 (upgrade to IND A+) (B00). No proxy-advisory
(IiAS/SES/InGovern) coverage was found in the corpus or by web search (B08
input_gaps).

**6. Corporate actions.** 29 Reg 30 filings, Sep-2025 to Sep-2026, staged
by hand from BSE (B00). Coverage is curated, not exhaustive: routine
trading-window, ESOP-allotment and analyst-meet filings were excluded, and
the collector's own automated fetch returned only 5 of these (B00
input_gaps).

**7. Freshness pair check.** All four pairs PASS (B00 freshness_verdict:
"FRESHNESS PAIRS OK"). RESULTS to CONCALL: Q1 FY27 results (13-Aug-2026)
pair to the Aug-2026 concall transcript for the same quarter. RATING
BULLETIN to RATIONALE: the 03-Jul-2026 Ind-Ra letter carries its own full
rationale on pages 2-9. SEBI ORDER to ORDER TEXT: not applicable, no SEBI
order is referenced anywhere in the corpus. AR to LATEST AUDITED ANNUAL
RESULTS: the FY26 audited results filing pairs to the FY26 AR. No pair
failed.

**8. Verdict line: CORPUS GAPPED.**
- FY25 (and earlier) Annual Report — findable-but-missing, BSE or company
  IR page.
- Investor presentations for Q2, Q3 and Q4 FY26 — findable-but-missing, BSE
  or company IR page.
- The FII/DII split within institutional ownership — findable-but-missing
  in more granular form, BSE detailed shareholding pattern (the BSE summary
  held gives only a 17.00% promoter/83.00% public split; the FY26 AR's own
  Note 15(c) partially closes this with FIIs 13.46%, Mutual Funds 35.50%,
  Insurance 0.66%, AIF 3.38% of the register at 31-Mar-2026, but this is one
  point in time, not a trend, and sits in a stage report rather than a
  dedicated filing) (B00, B03 5D).
- Independent broker/analyst research notes — plausibly-nonexistent given
  the company's May-2024 listing and small size, but not confirmed either
  way; no search for named broker coverage was run inside this container.
- Screener financial-statement export sheets (P&L, Balance Sheet, Cash
  Flow, Quarters, for AWFIS and all three peers) — a tooling defect on the
  operator's collector, not a missing filed document; the Data_Sheet CSVs
  substituted (B00 input_gaps).

None of these gaps triggered a freshness-pair failure; the verdict is
CORPUS GAPPED, not CORPUS GAPPED-FRESHNESS.

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT - PENDING OPERATOR SIGN-OFF.** Nothing in this section is signed.
Signing happens only in claude.ai after live-web stress-testing.

### PART A — THE FROM STATE

**A1. Archetype.**
- Coworking (co-working space and allied services, 82.8% of FY26 revenue,
  B04): **Outsourcing partner** (CDMO/EMS/IT services archetype). This is
  the closest fit per B04's own analyst note: wallet share grows through
  multi-centre clients (48% of active clients use more than one centre),
  capacity fill is the central economic variable (occupancy), and contract
  stickiness comes from a 26-month weighted lock-in rather than from a
  licence, a brand, or a cost curve (B04).
- Transform (construction and fit-out projects / Design & Build, 17.2% of
  FY26 revenue, B04): **Order-book business** (EPC/defence/capital goods
  archetype). Revenue is project-based, recognised on a percentage-of-
  completion basis (B03 2A), and depends on order inflow (GCC and enterprise
  fit-out mandates) and execution pace, not on a recurring licence fee.

**A2. The simple analogy.** Awfis takes long leases on whole office floors
from building owners, most often 5 to 10 years, then fits the space out and
rents desks, private cabins and whole managed offices to other companies by
the month, on lock-ins of about 26 months (B04, AR Note 38). A client gets
a finished office without paying for its own fit-out, at roughly 20 to 22%
less than a traditional three-year lease for a 100-seat occupier over the
same period (Prospectus, cited in business-narrative.md, sourced from B03/
B04). A second, smaller arm, Transform, does the physical fit-out work
itself, both for Awfis's own new centres and, increasingly, for outside
corporate clients (B04). That is the business as it stands today: a
landlord-to-occupier rent arbitrage, plus a construction contractor riding
alongside it.

### PART B — THE TRANSITION

**Line 1: Coworking (82.8% of FY26 revenue)**

- **B1. From → To.** FROM: **R1 COMMODITY PRICE-TAKER** — an undifferentiated
  desk-rental business with no durable pricing power evidenced through
  FY19-FY24, years in which the company lost money every year (B01, B03).
  TO (claimed by management, not yet proven): **R3 VALUE-ADDED / SPEC'D
  SUPPLIER**, reached via GCC client stickiness, premiumization (Gold/Elite
  formats claiming a 30-50% realization premium) and deepening multi-centre
  relationships (B04, B07 optionality_register). The evidence collected so
  far supports at most an early **R2 COST-ADVANTAGED CONVERTER** footing —
  the emerging-moat scan scored the forward case 12.5/92, classed MODEST,
  and a verifier recomputes 9.8-11.8, classed NONE (B07, B12c) — so the
  claimed R3 destination is not yet evidenced at R3 strength.
- **B2. The engine.** Two things must physically change for the climb to be
  real. First, the Managed Aggregation (MA) supply mix, where the landlord
  co-funds fit-out for a revenue share, shifting capex and rent-reset risk
  off Awfis's own balance sheet (B04 FLAG-ALM-QUANTIFIED). Second,
  premiumization and GCC mix shift, raising realization per seat as
  Gold/Elite-format and GCC-anchored centres mature past their lock-in
  (B04, B07).
- **B3. The proof gate.** Cash EBITDA margin, after actual cash rent paid,
  must rise each quarter from the Q1 FY27 print of 10.1% (₹44 Cr on ₹425 Cr
  revenue, agreed-upon-procedures reviewed by MSKA & Associates, B04
  FLAG-CASH-BRIDGE-CONFIRMED) toward the FY27 guide-implied level (₹195-200
  Cr cash EBITDA on ~₹1,800 Cr revenue, roughly 10.8-11%, B05 guidance),
  with the second half of FY27 exceeding the first half as management
  states (B05). Until at least one more quarter confirms the climb, the
  gate has not fired (B05 analyst_note: "only one data point so far").
- **B4. The recognition gap (OPEN QUESTION, resolved at Stage 11).** Does
  the market's current price already reflect a cash-margin climb to the
  FY27 guide, or does it still price the 36.8% reported-EBITDA optic, or
  the backward scorecard's own fixed classification (B01)? This dossier
  states no number, no conclusion. Stage 11 resolves it via the PE gap; if
  the TO state is already priced, the re-rating engine is gone and only
  earnings growth remains (CLAUDE.md QUALITY LADDER).
- **B5. The ugliness test.** MIXED, and unresolved by this run. Two readings
  compete, and the run cannot yet choose between them (B13 flag block,
  "the two readings"). Reading one: the 28.1-point gap between reported
  EBITDA (36.8%) and cash EBITDA (10.1%), and the near-zero FY26 post-lease
  free cash flow (about ₹(64) million, B03 FLAG-CASH), are **ARTIFACT-OF-
  CLIMB** — mechanical Ind AS 116 lease accounting on a balance sheet that
  is net-cash on the company's own ex-lease basis (B01 FLAG-LEASE-
  ACCOUNTING). Reading two: the occupancy plateau trailing all three peers
  by 5 to 16 points (76% blended vs 81-92%, B06 CONTRADICTED claim), the
  credibility grade of C on guidance discipline with a verifier arguing for
  lower (B05, B12b), and rising customer concentration (B02, B03) point
  toward a **STRUCTURAL-FEATURE**. The cohort cash-margin observation named
  under B13's FLAG-CASH (centres older than 12 months versus ramping
  centres, withheld on three consecutive calls, B12b F1) is the one
  observation built to separate these two readings; it has not yet been
  given.
- **B6. The transition falsifier.** A Q2 FY27 cash EBITDA print at or
  below the Q1 FY27 level of ₹44 Cr / 10.1% (B13 provisional falsifier); or
  a fourth consecutive quarter of Managed Aggregation share decline (it has
  already fallen from about 65% in Nov-2025 to 57% in Aug-2026, B05) with
  no reason given; or a further widening of the occupancy gap to peers.

**Line 2: Transform (17.2% of FY26 revenue)**

- **B1. From → To.** FROM: R1 COMMODITY PRICE-TAKER, a price-competed
  fit-out contractor. TO: **no forward TO claim is evidenced in the
  corpus.** Total segment revenue fell 7.8% and segment PBT fell 31.9% in
  FY26, even as the third-party slice alone grew (B03, B04
  FLAG-TRANSFORM-QUIET-RETREAT). The Chairman's Letter frames Transform as
  a "growth engine," but that framing describes only the growing
  third-party slice, not the shrinking total (B04).
- **B2. The engine.** Not evidenced as an active climb. The observable
  move is a structural carve-out — the Design & Build undertaking is being
  sold to a wholly-owned subsidiary, Awfis Transform Pvt Ltd, on a slump
  sale basis, at a consideration still pending a revised valuation (AR Note
  40, p.122) — not a quality-tier engine change.
- **B3. The proof gate.** None stated by management with a metric and a
  threshold. The only dated commitment in the corpus is the transfer's
  completion timeline, extended to 31-Dec-2026 (AR Note 40).
- **B4. The recognition gap.** Not applicable; no TO state is claimed to be
  priced for this line.
- **B5. The ugliness test.** **STRUCTURAL-FEATURE** is the better-evidenced
  read here: shrinking total segment revenue, falling segment PBT, and a
  related-party transfer at an unresolved consideration, not an artifact of
  any stated climb (B03, B04).
- **B6. The transition falsifier.** Not applicable for a claimed climb; see
  Part C3 for the business-level falsifier this line feeds.

### PART C — WHAT THE MODEL WATCHES

**C1. Dominant variables.**
1. **Cash EBITDA margin, post-rent.** Current state: 10.1% (Q1 FY27, ₹44
   Cr), up from an AR-implied ~9.2% for full FY26 (B03, B04). The proof
   gate for the whole transition.
2. **Managed Aggregation share of supply.** Current state: 57% (Aug-2026
   call), down from ~65% (Nov-2025) and 62% (Feb-2026), against a
   reiterated 60:40 MA:straight-lease target (B05).
3. **Occupancy: mature (>12 months) vs blended, and single-client churn.**
   Current state: 83-84% mature / 76% blended, flat for three straight
   quarters, with a ~3,000-seat single-client exit in Q1 FY27 the quarter
   after a churn reassurance (B03, B05). All three peers report higher
   occupancy (B06).
4. **Top-10 customer / receivable concentration.** Current state: 61.66%
   of trade receivables in FY26, up from 42.74% in FY25 (AR Note 36, B02,
   B03), even as the multi-centre "deepening relationship" narrative is
   told alongside it (B07 FLAG-CONCENTRATION-CONTRADICTS-C1).

**C2. What the model rejects.** Sizing questions. The run treats the
addressable market as adequate on both the conservative and the realistic
track — the realistic estimate (₹52,200 Cr, cross-validated twice by the
same research-house family two years apart) sits within 2% of management's
own figure, and even the data-availability-limited conservative floor still
implies roughly 14x revenue headroom (B09). The binding constraint the
model watches is execution — cash margin, occupancy, and the reliability of
what management says on calls — not whether the flexible-workspace market
is large enough. The run also rejects the flex-penetration debate (21% vs
25-27% of total office leasing by 2027) and the GCC-count macro trend as
primary variables: both are demand-side tailwinds the corpus finds credible
in direction (B09, B06 industry_cross_read), but neither is the thing that
decides whether Awfis itself converts that demand into a rising cash
margin.

**C3. The business falsifier.** Free cash after lease service and capex
turning negative and staying negative for two consecutive years — FY26 was
already near breakeven at about ₹(64) million (B03 FLAG-CASH) — together
with the standalone net current liability position continuing to widen
past its FY26 pace of +58.3% year on year (B02), or the going-concern
language in Note 2 escalating from a management disclosure to an auditor
Emphasis of Matter (B02, B03). That combination would mean the core
lease-arbitrage engine itself, not just the premiumization and GCC climb
layered on top of it, has stopped working. This is distinct from B6: B6
kills the claim that Awfis is climbing the quality ladder; C3 kills the
claim that the underlying rent-arbitrage business is sound at all.

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

Awfis takes long leases on office floors from building owners and lets
desks, cabins and managed offices to companies by the month; a company
avoids the cost and time of fitting out its own office, and the
co-working line made 82.8% of FY26 revenue of ₹1,493 Cr (B04). A second
line, Transform, designs and builds office fit-outs, for Awfis's own new
centres and for outside corporate clients; it made 17.2% of revenue, and
its total revenue fell 7.8% in FY26 as the board moved it into a
wholly-owned subsidiary, Awfis Transform Private Limited (B03, B04). The
customers are named classes, not named companies in the corpus: enterprises
and multinationals, small and medium businesses, and start-ups, with global
capability centres (GCCs), the India back offices of foreign firms, the
fastest-growing group (B04, B05). Clients sign a weighted lock-in of about
26 months and typically stay about 37 months, a shorter commitment than
Awfis's own 5-to-10-year leases with landlords, which India Ratings calls a
moderate asset-liability mismatch (B04, rating letter). The top 10 clients
held 61.66% of trade receivables in FY26, up sharply from 42.74% a year
earlier, even as no single customer contributed 10% or more to Group
revenue (AR Note 31D, B02, B03). Demand today comes from the GCC set-up
cycle and from flexible space taking a growing share of total Indian office
leasing, tied by name to two of B09's downstream candidates: the quarterly
India Grade A office leasing and flex-share data from CBRE, JLL, Knight
Frank and Colliers, and the Nasscom-Zinnov annual GCC count and revenue
tracker (B09). Demand should grow further if more first-time GCCs set up in
India and if large enterprise or GCC mandates above 2,000 seats keep
closing, each checkable against the new-GCC-setup and large-transaction
downstream candidates B09 names (B09). The run could not establish the pace
of flex penetration with confidence, because peer transcripts only
partially verify the claimed path from about 21% to 25-27% of leasing by
2027 (B06 partially_verified). On competitive advantage, the coworking line
carries a moderate moat from multi-centre stickiness (48% of clients use
more than one centre) and from Managed Aggregation access to Grade-A
landlords, but no cost advantage and no proven brand premium; the emerging-
moat scan scored the forward case 12.5 of 92, classed MODEST, and a
verifier recomputes it lower, classed NONE, with the talent-asymmetry and
cannibalization categories (21 and 22) both scoring zero (B07). Transform
has no moat the run could find: it is a price-competed fit-out contractor
whose total segment revenue is shrinking even as its third-party slice
grows (B04, B07).

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. Verticals framed

**Vertical 1 — Cash EBITDA margin, post-rent.** The corpus establishes an
AR-implied FY26 margin of about 9.2% (rebuilt from the consolidated cash
flow statement, B03 LBF1), a company-published and AUP-reviewed Q1 FY27
figure of 10.1% (₹44 Cr, B04), and a management guide of ₹195-200 Cr on
~₹1,800 Cr revenue for FY27, weighted H2-over-H1 (B05). It cannot establish
cohort-level (centre-age) cash margin — withheld on the Nov-2025, Feb-2026
and Aug-2026 calls (B12b F1) — or whether the H1-weaker/H2-stronger
explanation holds up beyond one quarter of new-metric data (B05
analyst_note). The deciding questions: does the margin climb quarter over
quarter toward the guide; is the rent-reset explanation for H1 FY27
pressure genuine, given peers describe the same 2020-21 lease vintage as a
repricing opportunity rather than a drag (B12b F5); and will management
ever disclose the cohort-level number three calls have withheld.

**Vertical 2 — Occupancy and single-client churn.** The corpus establishes
an 83-84% mature-vintage / 76% blended occupancy plateau across three
straight quarters, a ~3,000-seat single-client exit in Q1 FY27 the quarter
after a churn reassurance, and a materially higher occupancy band at all
three peers, 81% to 92% depending on the measure (B03, B05, B06). It
cannot establish a consistent churn definition — management cites 1.5-2%
of inventory monthly on the Aug-2026 call, while India Ratings cites a 1.2%
net monthly churn rate, different bases not reconciled in the corpus (B13
LBF4) — or the notice date of the 3,000-seat exit relative to the May-2026
call's occupancy-gain promise (B12b F3, unresolved). The deciding
questions: is the plateau company-specific or a broader-market pattern
(peers contradict a market-wide reading, B06); what is the true churn rate
on one consistent definition; and was the client exit known before the May
call's reassurance was made.

**Vertical 3 — Managed Aggregation supply mix.** The corpus establishes the
MA share fell from ~65% (Nov-2025) to 62% (Feb-2026) to 57% (Aug-2026),
against a target reiterated at 60:40 throughout (B05), alongside rising
capex per gross seat, from about ₹69,000 in FY26 toward an implied
₹80,000-95,000 for FY27 (B12b inference, B07). It cannot establish the MA
accounting policy or a numeric incremental borrowing rate for MA-related
lease liabilities (B02 gap), or whether the share's decline is a deliberate
strategic choice or a sign that landlords are less willing to co-fund
fit-out on Awfis's terms — no call names a reason (B05 input_gaps). The
deciding questions: why is MA share falling against a stated target; does
the decline structurally raise self-funded capex intensity; and does the
pipeline of "a couple more" developer-partnership deals (Malpani-style)
actually close within the 1-2 quarters management named (B07).

**Vertical 4 — Top-10 customer / GCC concentration.** The corpus
establishes the receivable concentration jump from 42.74% to 61.66% in
FY26 (AR Note 36, B02, B03), GCC clients at about 24% of rental revenue and
the fastest-growing client class (B04), and the AR's own statement that no
single customer reaches 10% of Group revenue (AR Note 31D). It cannot
establish the identity of the top-10 customers, whether the FY26 jump is a
genuine trend or an artifact of the Design & Build carve-out's receivable
reclassification (B02 receivables_trend), or whether the 48%-of-clients
multi-centre narrative is strengthening or weakening given the same-period
concentration jump the emerging-moat scan flags as a direct contradiction
(B07 FLAG-CONCENTRATION-CONTRADICTS-C1). The deciding questions: who are
the top-10 customers; is the concentration rise structural or a one-year
distortion; and does it make the next single-client exit a bigger swing
factor than the aggregate occupancy number suggests.

### 4b. Candidate signal table

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| Quarterly India Grade A office gross leasing & flex-share-of-leasing data | Flex share of total office leasing stalls or falls for two consecutive quarters | Quarterly | CBRE / JLL / Knight Frank / Colliers quarterly India office market report |
| Nasscom-Zinnov / Colliers annual GCC count and aggregate GCC revenue tracker | Annual GCC count growth decelerates sharply or turns negative | Event-Driven (annual release) | Nasscom-Zinnov GCC Landscape Report |
| Peer quarterly occupancy, seat-addition and cash-margin disclosures (Smartworks, Indiqube, DevX) | Peer occupancy converges down toward Awfis's level (market-wide read) or stays materially higher (company-specific read) | Quarterly | Peer BSE/NSE quarterly results filings and earnings calls |
| New / first-time GCC set-up announcements in India | Quarterly new-GCC-setup count falls below the ~20-30/quarter run-rate cited in the corpus | Quarterly | Nasscom-Zinnov GCC tracker / SEZ-STPI new-unit registrations |
| GST Council / CBIC commercial-leasing and works-contract GST notifications | A new adverse GST notification affecting lease or works-contract treatment | Event-Driven | CBIC / GST Council press releases |
| Large enterprise/GCC office-leasing transaction announcements (mandates >2,000 seats) | No mandate above 2,000 seats closes for two consecutive quarters | Event-Driven | CBRE/JLL/Knight Frank transaction trackers; Awfis Reg 30 filings |

These are UNVERIFIED. Verification and tracker writes happen at Role 5.5 in
claude.ai, unchanged.

### 4c. Fragility read

- **variable_count:** 4 (the C1 dominant variables: cash EBITDA margin,
  Managed Aggregation share, occupancy/churn, top-10 concentration).
- **verifiability_ratio:** 1 of 4 externally auditable (top-10/receivable
  concentration is a filed, audited Annual Report note); 3 of 4 are
  company-narrated only (cash EBITDA margin is reviewed under agreed
  procedures by MSKA but not audited; occupancy and Managed Aggregation
  share are self-reported KPIs whose definitions have already shifted
  across calls, B04, B05, B12b).
- **single_point_failure:** cash EBITDA margin (post-rent) failing to
  climb toward the FY27 guide. This alone breaks the transition thesis
  even if occupancy, MA mix and concentration hold steady, because it is
  the named proof gate (B13 FLAG-CASH, Part B3 above).
- **fragility_verdict: FRAGILE.** Three of four dominant variables are
  company-narrated rather than independently verifiable, and one variable
  alone can break the case — both conditions the framework treats as
  sufficient for a FRAGILE read.

### 4d. Research brief

Numbered live-web work order for claude.ai. Items 16 and 17 are the
PENDING LIVE VERIFICATION links raised by the two Section 4e chains below.

1. Confirm the current status of the DoIT Urban Ventures arbitration
   (~₹208 Cr claim against Amit Ramani personally, Prospectus p.402-403).
   A secondary source indicates withdrawal; the primary court record
   returned HTTP 403 to this container (B08).
2. Confirm the current status of the Enhance Lifestyle Pvt Ltd criminal
   complaint (CT Case 196/2023, Saket Court) against Ncube and Amit Ramani
   (Prospectus p.401, B08).
3. Confirm the current status of the two PMLA Section 8(2) applications
   (Ncube/PAFM/Petra vs ED, tied to the Rana Kapoor case, Prospectus
   p.403-404, B08).
4. Ask for cash EBITDA margin by centre vintage (older than 12 months vs
   ramping) and revenue per seat; withheld on three consecutive calls
   (B12b F1, B13). Ask on the Q2 FY27 call or through investor relations.
5. Ask for the Managed Aggregation accounting policy and the lease-cash-
   outflow split between MA and straight-lease centres; not in the FY26 AR
   notes (B02 input_gaps, B13).
6. Retrieve the FY22 Annual Report to quantify the 2021 lease resets named
   in company memory; not in this corpus (B13, B03).
7. Retrieve the Q4 FY26 and earlier investor decks (BSE or company IR) to
   build a quarterly cash EBITDA history predating Q1 FY27 (B00, B13).
8. Ask management for the bridge between normalized EBITDA (14.3% FY26)
   and cash EBITDA (10.1% Q1 FY27); offered "one-on-one" on the May-2026
   call but not given on the call itself (B13).
9. Check the FY27 Annual Report, once filed, for receivables ageing broken
   out by top-10 customer (B13).
10. Confirm the operator's ruling on the sector-cap row used at intake,
    "Real estate" (20x); no dedicated flexible-workspace row exists in the
    current Section 1B table (B00 sector_cap_row_evidence).
11. Retrieve the FY25 Annual Report (BSE or company IR) to extend the
    annual-report window beyond the single FY26 year on file (B00).
12. Retrieve the detailed BSE shareholding pattern (not the summary) to
    close the FII/DII split gap (B00, B01 FLAG-SHAREHOLDING-GAP).
13. Confirm the current (Sep-2026) exact shareholding of Peak XV Partners
    Investments V, absent from the AR's >5% holder table at 31-Mar-2026
    (B08).
14. Confirm the company-specific cause, if any, of the 17.41% share-price
    rise on 15-Sep-2026; no disclosed event was found (B08).
15. Retrieve the terms of the loan facilities approved at the 25-May-2026
    board meeting, and the content of the 13-Aug-2026 "change in
    management and issue of securities" filing; neither was read by any
    stage (B13 LBF3 open items).
16. PENDING LIVE VERIFICATION (Chain 1 below): confirm the landlord-side
    underwriting terms of named Managed Aggregation partnerships (Malpani
    Estates, Embassy Tech Village, DLF Cybercity, Gigaplex IT Park) from
    Reg 30 filings and real-estate trade press, to test why MA share is
    falling against a reiterated target.
17. PENDING LIVE VERIFICATION (Chain 2 below): confirm the identity and
    expansion or consolidation posture of Awfis's concentrated top-10
    customers and the client that exited about 3,000 seats, from
    named-tenant press coverage and the Nasscom-Zinnov GCC tracker.

### 4e. Second-order stub (Master Prompt v3.7, Rule F)

```
CHAIN 1: Managed Aggregation share fell from ~65% (Nov-2025 call) to 62%
(Feb-2026) to 57% (Aug-2026), against a target reiterated at 60:40
throughout the same three calls (B05).
Link 1 [filed, concall]: Management reiterates the 60:40 MA:straight-lease
target on every call while the actual share keeps falling, with no stated
reason for the gap (B05 repeated_evasions, red_flags).
Link 2 [filed, AR Note 38 / B07 capex]: What binds — capex per gross seat
is rising, from about Rs69,000 in FY26 toward an implied Rs80,000-95,000
for FY27, even as the FY27 capex guide stays flat at Rs200-210 Cr and
self-funded from internal accruals (B12b inference; B07 catalysts_12m).
If MA share keeps falling, Awfis funds more of its own fit-out capex
per seat inside the same guided capex envelope, which means fewer seats
added for the same rupee outlay.
Link 3 [INFERENCE]: A falling MA share paired with a flat capex guide and
rising capex-per-seat is consistent with landlords becoming less willing
to co-fund fit-out on Awfis's current terms, not with Awfis choosing to
retreat from MA by strategy; if that reading is right, the "capital-light"
framing of the FY27 plan is under more pressure than the guide numbers
alone show.
Binding constraint: whether landlords keep offering MA deals at
economically similar terms as Awfis's own negotiating position and scale
become more visible in the market — this is the "who pays, and why now"
question, and it needs landlord-side evidence this container cannot reach.
Unsaid: no call, on any of the three transcripts checked, names why MA
share is falling. Management addresses the ratio only when asked, and the
stated position has changed three times without being flagged as a change
(B05 repeated_evasions).
Observation that confirms or breaks this chain, and confirm-by date: MA
share and capex-per-seat disclosed in the Q2 FY27 investor deck, expected
around early November 2026 at the normal quarterly results cadence.
```

```
CHAIN 2: Top-10 customer receivable concentration rose from 42.74% to
61.66% in FY26 (AR Note 36(b)(II), p.116, B02/B03), the same year a
~3,000-seat single client exited (Q1 FY27, B05) after a churn reassurance
given the prior quarter, and blended occupancy held flat at ~75-76% for
three straight quarters despite the multi-centre "deepening relationship"
narrative (B04, B07 FLAG-CONCENTRATION-CONTRADICTS-C1).
Link 1 [filed, concall]: Management attributes part of the H1 FY27 margin
pressure to rent resets on leases signed in 2021, a timing story about
cost, not about client concentration (B05).
Link 2 [filed, AR Note 2 / Note 36]: What binds — the standalone net
current liability position grew 58.3% year on year in FY26 (AR Note 2,
p.92, B02), driven by the current portion of lease liabilities, at the
same time the customer base funding collections became more concentrated.
A smaller number of large clients now carries a larger share of both the
occupancy base and the receivables the working-capital position depends
on.
Link 3 [INFERENCE]: A business with rising customer concentration and a
flat occupancy plateau is more exposed to any single future exit than the
aggregate 76% figure suggests; the next exit at a similar scale to the Q1
FY27 one could move blended occupancy by a full point or more on its own,
independent of whether the broader GCC demand thesis holds.
Binding constraint: whether the specific enterprises and GCCs inside the
top-10 concentration pool are themselves expanding or consolidating their
India real-estate footprint — this needs counterparty-side evidence
(their own capex, hiring and site-consolidation plans) this container
cannot reach.
Unsaid: no concall names the identity of the top-10 customers, and none
states whether the client that exited in Q1 FY27 was inside or outside
that concentrated pool (B02, B05 gap).
Observation that confirms or breaks this chain, and confirm-by date:
quarterly blended-versus-mature occupancy trend in the Q2 FY27 investor
deck (confirm-by ~early November 2026), and top-10 concentration in the
FY27 Annual Report (confirm-by ~May 2027).
```

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in
claude.ai with live web, before Role 2.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. Awfis rents whole office floors from landlords, fits them out, and
   rents desks and private offices to companies by the month.
2. A second business, Transform, designs and builds office fit-outs, for
   Awfis's own centres and for outside clients; it made 17% of FY26
   revenue.
3. Awfis calls itself India's largest flexible workspace operator by
   centre count. The run could not check this against a named list of
   competitors.
4. Enterprises and multinationals make up most clients. Global capability
   centres, the India offices of foreign companies, are the
   fastest-growing group.
5. Clients sign up for about 26 months and typically stay about 37
   months. Awfis itself signs 5 to 10 year leases with landlords, a
   timing gap the rating agency calls a moderate risk.
6. Ten clients now hold 62% of trade receivables, up from 43% a year
   earlier. The client base is growing more concentrated even as the
   company talks about deepening relationships.
7. Demand should grow if flexible offices keep taking a bigger share of
   total office leasing, and if more foreign companies open India back
   offices. Neither path is fully proven in the documents on file.
8. The company's own market-size claim sits close to the best outside
   estimate the run found, so the addressable market looks large enough
   to support years of growth.
9. The coworking business has some staying power, from clients using more
   than one centre and from landlord partnerships, but no real cost or
   brand edge over rivals. A well-funded competitor could copy it with
   time and capital.
10. The fit-out business, Transform, has no moat the run could find. Its
    total revenue fell 8% in FY26 as the board moved it into a separate
    subsidiary.
11. The story to test is cash margin, not revenue. Reported profit margin
    is 37% of revenue, but after paying rent it falls to about 9 to 10%.
    Whether that cash margin climbs toward management's guide is the
    whole model.
12. This case reads FRAGILE. Most of the numbers that decide it come from
    the company itself, not from an outside check, and one of them, the
    cash margin, can break the whole story on its own.
13. The corpus could not confirm the current status of the founder's own
    past legal disputes, or the exact terms of two recent board decisions
    on a loan facility and a business transfer.
14. The corpus holds only one annual report and one investor deck, and no
    independent broker research. It could not confirm three years of
    annual reports, or a detailed split between foreign and domestic
    institutional owners.
15. Two questions matter most now. Does the cash margin actually climb
    toward the FY27 guide. And is the occupancy plateau, well below all
    three peers, a company problem or a market one.

---

## SECTION 6: STANDING EXTRACTION ANNEX

### 1. Units

No single company-disclosed per-unit figure (revenue per seat, cash
EBITDA per seat) exists in the corpus. The nearest printed figures:

> "About 159,000 operational seats" (AR p.8-9, FY26-at-a-glance, basket
figure covering hot desks, dedicated desks, cabins and managed offices,
not one product) and FY26 co-working & allied services revenue of
₹12,369.00 million (consolidated segment note, AR p.153).

Comment: this is a basket figure, not a per-product rate. B04 derives, not
quotes, a revenue-per-seat range of about Rs74,000/year (capacity basis, on
~170,000 seats) to about Rs97,400/year (occupied basis, on ~159,000 seats)
by dividing the co-working revenue line by the seat-count lines above; both
are stage-4 derivations, flagged as such (B04 input_gaps, unit_economics).

> "Rs 44 Cr" cash EBITDA, Q1 FY27 (Investor Presentation p.20-21, AUP-
reviewed by MSKA & Associates).

Comment: dividing by ~159,000 operational seats gives a stage-derived
~Rs923/seat/month; not a company-printed per-seat figure.

Capex per gross seat: FY26 capex of ₹208 Cr (B05 promise_delivery,
delivered against a ₹200-210 Cr guide) divided by ~30,000 gross seats
added in FY26 gives a derived ~Rs69,000 per gross seat; the FY27 guide of
₹200-210 Cr capex against 22,000-25,000 gross seats implies a derived
Rs80,000-95,000 per gross seat (B12b F10 inference; B07 catalysts_12m). No
company-printed capex-per-seat figure exists in the corpus.

### 2. Segment capital and debt

Consolidated segment note, two periods (AR p.153, Note 31):

> "Segment assets [by segment, 31 March 2026 / 31 March 2025, Rs million]:
Co-working space on rent and allied services: 24,515.53 / 21,575.03.
Construction and fit-out projects: 1,771.57 / 1,429.11. Others: 3.84 /
2.47. Unallocated: 2,810.95 / 2,063.23. Total: 29,101.89 / 25,069.84."

> "Segment liabilities [by segment, 31 March 2026 / 31 March 2025, Rs
million]: Co-working space on rent and allied services: 21,355.29 /
19,364.72. Construction and fit-out projects: 1,517.01 / 716.44. Others:
9.88 / 21.28. Unallocated: 695.25 / 375.21. Total: 23,577.43 / 20,477.65."

Borrowings are not allocated by segment. They appear only in the
reconciliation-of-liabilities table:

> "Borrowings including interest accrued on borrowings 509.31 [FY26]
234.57 [FY25]" (AR p.153, reconciliation to consolidated total liabilities
of 23,577.44 FY26 / 20,477.65 FY25).

Comment: the coworking segment carries the large majority of both assets
and liabilities (about 84% of segment assets, 91% of segment liabilities
in FY26); Transform (construction and fit-out) is a small fraction of the
balance sheet despite being 17.2% of revenue, consistent with its
project/contracting model rather than an asset-heavy one. Total borrowings
of Rs509.31mn are not split by segment in the corpus.

### 3. Guidance versus aspiration

| Forward number | Class | Source |
|---|---|---|
| FY26 seat addition, ~40,000 gross seats | (a) guidance, FY26 | B05, referenced Q3 FY26 call |
| FY26 revenue/EBITDA growth, 30%/30% | (a) guidance, FY26 | B05, referenced Q3 FY26 call |
| FY26 seat addition, revised 32,000-33,000 gross | (a) guidance, FY26 | B05, Q3 FY26 call |
| FY26 capex, Rs200-210 Cr | (a) guidance, FY26 | B05, Q3 FY26 call |
| FY26 normalized EBITDA margin, stable 14-15% | (a) guidance, FY26 | B05, Q2 FY26 call |
| FY27 seat addition, 22,000-25,000 gross (~1.25msf) | (a) guidance, FY27 | B05, Q4 FY26 call |
| FY27 capex, ~Rs200-210 Cr | (a) guidance, FY27 | B05, Q4 FY26 call, reiterated Q1 FY27 call |
| FY27 coworking revenue growth, 25-27% then restated 23-25% | (a) guidance, FY27 (two vintages, no explanation for the revision) | B05, Q4 FY26 and Q1 FY27 calls |
| FY27 Transform revenue growth, 22-25% then restated ~20% | (a) guidance, FY27 (two vintages) | B05, Q4 FY26 and Q1 FY27 calls |
| FY27 total revenue, "past Rs1,800 crore" | (a) guidance, FY27 | B05, Q1 FY27 call |
| FY27 cash EBITDA, Rs195-200 Cr (also stated Rs190-200 Cr in the same call), H2>H1 | (a) guidance, FY27, internally inconsistent within one call | B05, B12b F12; Q1 FY27 call |
| Premiumization (Gold/Elite) realization premium of 30-50% | (b) aspiration, no period; asked about on three calls, never quantified | B12b F1; B07 optionality_register |
| "60%+ RoCE" / "Annualised RoCE Q4 FY26 60%" | (c) capacity/capability claim on an undefined "Cash EBIT" formula, not forward guidance | AR p.6, p.9, p.11 (B03 3B) |
| Frame by Awfis (furniture vertical): "H2, 2-3 mandates" | (b) aspiration, timeline slipped across four calls then dropped entirely | B05 timeline_slippages, dropped_triggers |
| 2-3 more developer-partnership deals beyond Malpani | (a) guidance with a loose period, "1-2 quarters" in management's own words | B07 catalysts_12m |
| 13 GCC mandates in pipeline going live | (a) guidance with a period, "2-3 quarters" | B07 catalysts_12m |

### 4. Concentration

Product concentration: coworking & allied services 82.8% of FY26 revenue,
construction & fit-out (Transform) 17.2% (B04).

Customer concentration:

> "No single customer contributed 10% or more to Group's revenue."
(AR p.153, Note 31D "Information about major contracts")

> Top-10 customer receivable concentration: 42.74% (FY25) to 61.66% (FY26)
of total trade receivables outstanding (AR Note 36(b)(II), p.116, per B02
finding 11 / B03 2D).

Geography concentration:

> "Group's operations are in India and therefore, no separate geographical
information is disclosed. All the non-current operating assets of the
Group are located in India." (AR p.153, Note 31C)

Comment: no city-wise or region-wise revenue split is disclosed in the AR;
the 18-cities / 251-centres figures are business-description KPIs (B04),
not a segment-note geographic breakdown.

### 5. Promise ledger

| Promised in | Promise | Outcome | Evidence anchor |
|---|---|---|---|
| Pre-Q3 FY26 (original guide) | 40,000 gross seat additions FY26 | MISSED (cut twice, actual 30,000 gross / ~22,000 net) | B05, Q3 FY26 call |
| Pre-Q3 FY26 (original guide) | 30% revenue growth, 30% EBITDA growth FY26 | PARTIAL: consolidated revenue +24% (miss), EBITDA +37% (beat) | B05 |
| Q3 FY26 call | Mature-cohort occupancy to rise 100-150bps in 1-2 quarters | PARTIAL: blended rose ~100bps, mature cohort held flat at 84% | B05, Q4 FY26 call |
| Q3 FY26 call | FY26 capex Rs200-210 Cr | DELIVERED: Rs208 Cr actual | B05 |
| Q2 FY26 call | Normalized EBITDA margin stable 14-15% FY26 | DELIVERED: 14.3% actual | B05 |
| Q4 FY26 call | FY27 coworking 25-27%, Transform 22-25%, 22,000-25,000 gross seats | PARTIAL/already revised: Q1 FY27 call restated lower with no explanation | B05, Q1 FY27 call |
| Q4 FY26 call | 5% FY26 churn rate would not repeat | MISSED: a further ~3,000-seat single-client exit disclosed the next quarter; a verifier finds the exit may have been known at the May call itself, unresolved (B12b F3) | B05, B12b |
| Q2 FY26 call | Maintain MA:straight-lease mix ~65:35, no change in strategy | CHANGED: 62% (Q3 FY26), 60:40 target reiterated (Q4 FY26), 57% actual (Q1 FY27) | B05 |
| Q3 FY26 call | Clearer Frame (furniture) guidance in Q4 FY26 call | PARTIAL then DROPPED: qualitative detail given, no revenue figure, then no mention at all in Q1 FY27 call | B05 |

Verifier note: B12b finds a further, uncredited pattern the ledger above
does not carry as a separate row: management gave no revenue-per-seat or
cash-margin-by-centre-age figure across all three calls checked, despite
being asked each time, and all three named peers disclose theirs (B12b F1,
CRITICAL).

### 6. Restated bases

> "48 Previous year figures have been regrouped/reclassified, wherever
necessary to conform to this year's classification. Such
regrouping/reclassification are not material to the standalone financial
statements." (AR p.125, standalone Note 48)

> "46 Previous year figures have been regrouped/reclassified, wherever
necessary to confirm to this year's classification. Such
regrouping/reclassification are not material to the consolidated financial
statements." (AR p.166, consolidated Note 46)

Comment: boilerplate, no items named. The one substantive comparability
issue in the corpus is the Design & Build disposal group: its FY25
comparatives sit only in the supplementary Note 40 (discontinued
operations), not restated as a continuing-operations-only column
throughout every other note (Notes 8, 22), moving Rs937.14 million of
receivables to a held-for-sale bucket and materially flattering the
standalone receivables-ageing trend if read without that context (Ind AS
105-compliant, not an error; B02 restatements_found, B03 2D).

### 7. Corporate-action clauses

The one corporate action in the corpus, the Design & Build transfer to
Awfis Transform Pvt Ltd (ATPL):

> "40 Discontinued operations. Pursuant to approval of the Board of
Directors of the Company at their meeting held on 23 December 2025, the
Company has entered into a Business Transfer Agreement ('BTA') with Awfis
Transform Private Limited ('Acquirer'/'ATPL') a wholly-owned subsidiary of
the Company, incorporated on 03 December 2025, for sale of the Company's
segment engaged in the business of construction and fit-out project
('Undertaking'), as a going concern and on a slump sale basis for a
consideration of ₹265.91 million ('Initial Purchase Price'). The same was
approved by the shareholders through special resolution passed through
postal ballot. The Board of Directors at their meeting held on 26 February
2026 considered and approved the extension of the timeline for completion
of the transfer of the Undertaking, which is now expected to be completed
by 31 December 2026 ... The consideration for the sale of the Business
Undertaking shall be determined as per an updated valuation report for the
Business Undertaking ..., with the reference date of valuation being the
revised date of completion of the transaction ..." (AR p.122, Note 40)

Comment: board approval date 23-Dec-2025 (definitions and initial
consideration set); shareholder approval by postal ballot; timeline
extension approved 26-Feb-2026, new expected completion 31-Dec-2026; the
consideration itself is not fixed, it will be set by a future valuation
report dated to the revised completion date. No liability-allocation
clause beyond the slump-sale consideration is printed in this note; no
share-exchange ratio applies (cash consideration, wholly-owned subsidiary).
No other scheme, demerger, merger, preferential issue or buyback is in the
corpus.

### 8. Related-party perimeter

Standalone Note 32 (AR p.111-112), per B03 2B: related parties are the two
wholly-owned subsidiaries (Awliv Living Solutions Pvt Ltd, Awfis Transform
Pvt Ltd) and KMP plus close family. Transactions, latest year (FY26):

> Revenue from Awliv Living Solutions: Rs10.76 million. Communication
expenses paid to Awliv: Rs154.27 million (58.2% of the entire standalone
"Communication expenses" line of Rs264.84 million, Note 29). ATPL equity
investment: Rs0.10 million. Total identified RPT (excluding KMP
compensation): approximately Rs165 million, about 1.3% of standalone
revenue (Note 32, p.111-112).

CMD (Amit Ramani) compensation is disclosed as two different figures in
the same Annual Report, unbridged:

> Rs41.57 million (Note 32, Ind AS 24 "short-term employee benefits
[compensation]", p.112) versus Rs29.90 million (Board's Report Annexure-5,
Section 197(12) disclosure, p.49).

Comment: RPT is immaterial in aggregate and eliminates on consolidation
(both counterparties are subsidiaries); no related party sits outside the
promoter/subsidiary structure. The Awliv communication-expense line is a
standalone-only observation, not a group-level value-extraction signal
(B03 2B). The CMD remuneration discrepancy is a disclosure-consistency gap
the run could not bridge from the AR alone (B03 new finding).

### 9. Pledge and shareholding

> "(A) Promoter & Promoter Group | 2 [holders] | 1,21,63,084 [shares] |
17.00 [%] | ... Whether any shares held by promoters are pledge or
otherwise encumbered? No" (BSE shareholding pattern summary, quarter ended
June 2026)

> "(e) Details of shares held by promoters. As at 31 March 2026 ... Amit
Ramani 12,018,812 (16.80%). Moneesha Ramani 144,272 (0.20%). Total
12,163,084 (17.00%)." (AR p.104, standalone Note 15(e))

> "*During the year ended 31 March 2026, Peak XV Partners Investments V
(holding 23,15,525 equity shares i.e. 3.24% of the total equity) has
reclassified from 'Promoter and Promoter Group' to 'Public' category
pursuant to shareholder approval via postal ballot dated 10 July 2025 ..."
(AR p.104, Note 15(e) footnote)

Comment: promoter and promoter-group holding is 17.00% at both 30-Jun-2026
(BSE) and 31-Mar-2026 (AR), with nil pledge at both observation points.
Twelve-quarter pledge history is not constructible from the corpus: only
two dated observations exist (31-Mar-2026, 30-Jun-2026), both nil. The
year's apparent 3.40-point decline (20.40% to 17.00%) is 3.24 points a
reclassification of a co-investor, not a promoter sale; Amit Ramani's own
personal holding rose slightly before an intra-family gift to his spouse
(B03 5D, B08). Institutional holding at 31-Mar-2026, from the AR's
Categories of Shareholders table: FIIs/QFIs/FPIs 13.46%, Mutual Funds
35.50%, Insurance 0.66%, Alternate Investment Funds 3.38%, about 52.9% of
the register combined (B03 5D). This is latest-quarter institutional
holding, not a twelve-quarter trend; no more granular FII/DII split is in
the corpus (Section 1, gap 3).

### 10. Verification

Documents quoted in this annex, with filename and date:
- AR-FY26-with-AGM-notice.pdf (Awfis Space Solutions Ltd Annual Report
  FY2025-26 + 12th AGM Notice, Reg 34 filing), pages 62, 92, 104-105, 111-
  113, 116, 122-123, 125, 153, 166.
- BSE-SHP-summary-Jun2026.txt (BSE Reg 31 shareholding pattern summary,
  scrip 544181, quarter ended June 2026).
- 20260813-ef5b8155-a44a-4a36-9865-1e326f798b07.pdf (Q1 FY27 results
  filing, 13-Aug-2026).
- Investor_Presentation_1.pdf (Q1 FY27 investor presentation, 13-Aug-2026,
  p.20-21).
- Concall_Nov_2025_Transcript.pdf, Concall_Feb_2026_Transcript.pdf,
  Concall_May_2026_Transcript.pdf, Concall_Aug_2026_Transcript.pdf
  (Q2 FY26 through Q1 FY27 earnings calls).
- 20260703-2cce03ab-2b56-4bfb-83ed-2f4e3cd074cb.pdf (India Ratings letter
  and press release, 03-Jul-2026).
- Awfis-Prospectus-May2024.pdf (IPO Prospectus, 27-May-2024).

CORPUS COMMIT HASH: 2447bbd4074fce493f996f409b4640d93557dc03 (HEAD of
branch run/awfis-2026-09-19 at invocation of this stage; the corpus itself
landed in commit f06f9430b9725c1376e0b11144ff879a25b6c13b).
