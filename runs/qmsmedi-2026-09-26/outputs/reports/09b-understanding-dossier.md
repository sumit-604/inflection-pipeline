# HALT 1 UNDERSTANDING DOSSIER — QMS Medical Allied Services Ltd (QMSMEDI)

Run date: 2026-09-26. Assembled from committed blocks B00-B09 and verifier
blocks B12a-B12d, confidence.yaml. No web search, no new numbers, no
re-analysis, except the Section 6 annex (corpus PDF quote retrieval) and the
Section 4e stub (labelled inference), both licensed exceptions named in the
stage instructions.

Units: All figures in ₹ Cr unless the source says otherwise; the source unit
is on the face of the document, not in the filename.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

1. CONCALLS. Four transcripts held: Q1 FY26 (Concall_Aug_2025, call
   Aug-2025), Q2 FY26 (Concall_Nov_2025), Q4 FY26 (Concall_Jun_2026, call
   04-Jun-2026), Q1 FY27 (Concall_Aug_2026, quarter ended 30-Jun-2026)
   (B00). Most recent quarter covered: Q1 FY27. No Q3 FY26 transcript
   exists because the company held no Q3 FY26 earnings call; it filed a
   20-Feb-2026 investor presentation and a 02-Mar-2026 investor-meet
   intimation instead, neither with Q&A (B00, B05 input_gaps). Given the
   run date of 2026-09-26, Q2 FY27 (quarter ended 30-Sep-2026) has not yet
   closed, so no newer transcript could plausibly exist yet.

2. ANNUAL REPORTS. Two held: FY26 (Annual Report 2025-26, 9th AGM,
   147pp) and FY25 (Annual Report 2024-25, 120pp) (B00). The latest
   completed FY (FY26, year ended 31-Mar-2026) is present. Fewer than 3
   years are held; FY24 and earlier ARs are absent from the corpus
   (findable-missing: company IR page or BSE/NSE archive, though the
   company is NSE-only).

3. RESULTS FILINGS. Latest is Q1 FY27 (14-Aug-2026, quarter ended
   30-Jun-2026). No quarter-gap to the latest AR: FY26 AR covers the year
   ended 31-Mar-2026, and Q1 FY27 is the very next quarter (B00).

4. INVESTOR PRESENTATIONS. Latest held is the Q1 FY27 revised deck
   (Investor_Presentation_1.pdf, 17-Aug-2026) (B00).

5. RESEARCH / RATING. rating/ is EMPTY: no credit rating found on the
   screener documents page or by web search, and the FY26 AR text carries
   no rating reference (B00, B02). research/ is EMPTY: no broker notes
   (B00, B02).

6. CORPORATE ACTIONS. 51 Reg 30 filings held, Jul-2025 to 25-Sep-2026,
   deduplicated and curated (B00): rights issue outcome and allotment,
   EGM notice and results, statements of deviation, Monitoring Agency
   reports, Saarathi acquisition intimations (28-Oct-2025, 19-Feb-2026
   amended, 17-Sep-2026), mainboard migration (Mar-Jun 2026), SOC 2
   (21-Jul-2026), and the 25-Sep-2026 board outcome on the composite
   scheme of arrangement (19pp).

7. FRESHNESS PAIR CHECK. B00 `freshness_verdict`: FRESHNESS PAIRS OK. All
   four pairs PASS: RESULTS to CONCALL (Q1 FY27 results paired with
   Concall_Aug_2026); RATING BULLETIN to RATIONALE (no rating held, no
   pair to fail); SEBI ORDER to ORDER TEXT (none identified); AR to
   LATEST AUDITED ANNUAL RESULTS (FY26 audited results paired with
   Annual_Report_2026.pdf). No pair failed.

8. VERDICT LINE: **CORPUS GAPPED**.
   - No credit rating exists in any source found (plausibly-nonexistent;
     the company appears never to have sought one — itself a data point
     for a lender-facing entity carrying ₹74.5 Cr of consolidated
     borrowings).
   - No Q3 FY26 call transcript exists because none was held
     (plausibly-nonexistent; the company substituted a slide deck).
   - No research/broker notes held (plausibly-nonexistent so far as this
     corpus shows; expected source would be broker/IR distribution
     lists).
   - The 2022 SME IPO prospectus was not collected (findable-missing:
     NSE Emerge archive; not mandatory since the company has been listed
     over 3 years, so this is not a HIGH gap).
   - Fewer than 3 years of annual reports are held; FY24 and earlier are
     findable-missing (company IR page, NSE archive).
   - Freshness pairs are OK, so the CORPUS GAPPED-FRESHNESS precedence
     rule does not apply.

   EMPTY-FOLDER NOTE (per the operator's standing autonomy-contract
   answer, "proceed with the gaps"): the empty folders are **rating/**
   and **research/**.

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT - PENDING OPERATOR SIGN-OFF**

### PART A — THE FROM STATE

**A1. ARCHETYPE (per line).**
- Products line (≈69% of FY26 revenue: B2B pharma/hospital device resale,
  Point of Care consumables, e-commerce; B04 revenue_streams): closest
  fit is **Licence/scarcity business** (CDSCO import/distribution licence
  gates entry; 30-year exclusive brand tie-ups with 3M, Heine, Rossmax
  gate supply), though the fit is weak — there is no regulated price and
  no hard capacity cap, only a renewal-risk gate (B04 moats_present).
  Flagged, not forced.
- Services line (≈31% of FY26 revenue, 41% of Q1 FY27: B2B health camps,
  Patient Support Programmes incl. Saarathi; B04 revenue_streams): closest
  fit is **Outsourcing partner (CDMO/EMS/IT services)** — client
  concentration (>50 pharma companies, top-client share undisclosed),
  wallet share, capacity fill (150-seat call centre), contract
  stickiness (60-70% rollover), price per unit (per-camp, per-PSP fee)
  (B04 business_type "hybrid", unit_economics, moats_present).

**A2. THE SIMPLE ANALOGY.** QMS is a middleman for hospitals and drug
companies. On one side it buys foreign-brand medical devices, BP
monitors, stethoscopes, braces, and resells them to pharma companies and
hospitals. On the other side, drug companies pay QMS to run free
health-check camps and to have nurses and call-centre staff phone
patients and keep them on their medicine, because doctors can no longer
be pitched to as directly as before. Today most of the money, about
seven of every ten rupees, still comes from reselling other people's
devices; less than a third comes from the patient-service work (B04
revenue_streams; B00 LBF1).

### PART B — THE TRANSITION

**B1. FROM to TO** (per line, quality ladder, CLAUDE.md):
- Products line: stays near **R1 COMMODITY PRICE-TAKER** (weak pricing
  power, B04; products gross margin fell 26.3% to 23.6% FY25→FY26, B02
  top_findings rank 1). No credible TO is claimed for this line beyond a
  brand-by-brand exclusivity gain (HEINE sole-distributorship from
  1-Jan-2027, B09), which keeps it in the R1/R2 neighbourhood, not a
  rung jump.
- Services line: management's own narrative claims a shift **FROM R2
  COST-ADVANTAGED CONVERTER-like, project-based fee-for-service work**
  (camps: fee-for-service, predictability M, B04) **TO R3/R4
  VALUE-ADDED / FRANCHISE-like recurring PSP work** (multi-month
  retainer contracts, CRM lock-in, SOC 2 Type II certification, 5-12%
  annual price escalators, predictability M-H, B04 revenue_streams,
  B07 active_categories B2/H2).

**B2. THE ENGINE.** Two things must physically change: (1) the revenue
mix must keep moving from Products toward Services (31%→41% of revenue
FY26→Q1 FY27, driven by the Saarathi buyout and organic PSP signings,
B00 LBF1); (2) the Services book must convert from one-off camps toward
signed, multi-month PSP retainer contracts with escalator clauses,
which requires front-loaded headcount (call-centre counsellors) ahead of
revenue recognition (B04 must_track_metrics, employee-cost flag).

**B3. THE PROOF GATE.** The hard binary: consolidated EBITDA margin must
turn up, not merely hold, above the FY26 baseline of 15.0% while
Services stays at or above 40% of consolidated revenue for at least two
consecutive quarters. As of Q1 FY27, Services was 41% of revenue and
margin printed 14.6%, below both the FY26 (15.0%) and FY25 (16.3%)
marks (B04, B05, gate-recommendation.md falsification line). Until
margin turns up with Services above 40%, the shift is a revenue-mix
change only, not a quality-tier climb. This is the exact observation
Stage 11 FTTCP must test.

**B4. THE RECOGNITION GAP (open question, resolved at Stage 11).**
Whether the market already prices QMS as a higher-margin services
business, given the FY26 mainboard migration and the services-led
investor narrative running since Q1 FY26, or still prices it purely as
an AVERAGE-graded device distributor, is unresolved here. Stage 11
confirms or denies this via the PE gap; this dossier states no number
and no conclusion.

**B5. THE UGLINESS TEST.** UNRESOLVED IN THIS CORPUS — two live
readings, not adjudicated here. ARTIFACT-OF-CLIMB reading: the margin
dip and cash drag come from hiring ahead of signed cost-plus programmes
and from consolidating Saarathi, and should fade as programmes bill out
(B04 unit_economics key_lever). STRUCTURAL-FEATURE reading: a device
reseller carrying ~181 inventory days, an aging pharma receivables book
(>6-month share doubled 14.5%→30.6%, B02), and weak pricing power (B04)
carries this drag permanently, and the Services slice is still too
small (41% of revenue) to offset it. The observation that separates the
two readings: the H1 FY27 cash flow statement read after removing the
change in short-term borrowings, together with the Q2 FY27 margin print
at the reported Services share (B03 monitorables).

**B6. THE TRANSITION FALSIFIER.** The transition thesis fails if (a)
consolidated EBITDA margin does not turn up while Services crosses
40-45% of revenue for two more consecutive quarters, and/or (b) the H1
FY27 normalized operating cash flow (operating cash less the change in
short-term borrowings) prints at or below zero, confirming the margin
dilution and cash drag are contract-mix features, not a temporary
investment phase (B04, B03 falsification metrics). Separately, the
25-Sep-2026 composite scheme of arrangement, which moves QMS's own
healthcare-services undertaking (₹37.17 Cr, 24.41% of FY26 standalone
turnover) into a to-be-separately-listed Saarathi (see Section 6,
Q7), raises an entity-boundary qualifier: if the Services undertaking
transfers out of listed QMSMEDI, a transition thesis built on QMSMEDI's
own services climb may need to be re-pointed at a different listed
entity (B07, B08).

### PART C — WHAT THE MODEL WATCHES

**C1. DOMINANT VARIABLES.**
1. Services % of consolidated revenue AND consolidated EBITDA margin,
   moving together (the proof-gate pair). Current state: 41% Services,
   14.6% margin, moving apart, not together (B04, B05).
2. Normalized operating cash flow (operating cash flow less the change
   in short-term borrowings) as a multiple of PAT. Current state: 0.23x
   consolidated, 0.31x standalone FY26, both below the FY25 base (B03).
3. The entity boundary of the 25-Sep-2026 Saarathi/HCAH composite
   scheme: which listed entity holds the Services undertaking once NCLT
   and shareholder approval complete. Current state: scheme approved by
   the board, not yet by NCLT/shareholders; per the filing text itself,
   Saarathi (the "Resulting Company") issues shares directly to QMS's
   own shareholders and QMS's existing holding in Saarathi is cancelled
   without consideration (see Section 6, Q7) (B07, B08).
4. GLP-1-linked PSP pipeline conversion into signed, cost-plus contracts
   versus the headcount already committed against it. Current state:
   one signed programme reportedly needs ~1,200 hires against a company
   headcount near 250; Q1 FY27 employee cost rose from ₹3.2 Cr to
   ₹11.2 Cr YoY while COGS stayed flat (B04, B05).

**C2. WHAT THE MODEL REJECTS.** Market-sizing questions: the global "$70
billion" PSP figure management juxtaposes against its India-only P&L
(flagged as a TAM=SAM misread, B09 FLAG-TAM-SCOPE); the 18.6x
revenue-headroom arithmetic against the ₹3,218 Cr SAM (B09), since the
binding constraint on this thesis is margin conversion and entity
ownership, not addressable market size. The India device-market top-down
figure (₹1,61,000 Cr) is held as unreachable context only (B09), never
used as a Products TAM headline.

**C3. THE BUSINESS FALSIFIER** (distinct from B6; kills the FROM
business, not the transition arrow). Interest cover falling below 3x
(currently 3.51x, one band above the Gate-0 deal-breaker line) or the
audited DSCR staying below 1.0x (currently 0.79x, down from 2.54x) while
receivables ageing keeps deteriorating, forcing a liquidity or covenant
event, would force re-declaring QMS as a distressed distributor under
funding strain rather than a GARP transition candidate (B01 Block D one
band from two separate deal-breaker thresholds; B02, B03).

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

*(Drafted per the five-question spec in prompts/13-synthesis-pipeline.md;
that file's spec governs and is not restated here. This draft, built
from B01-B09, is carried forward from the run's own final synthesis
narrative; Stage 13's copy is the version of record and is updated by
later stages.)*

QMS sells two things to drug companies: branded medical devices and
patient services. About 57% of FY26 revenue came from reselling devices
such as BP monitors, stethoscopes, orthotics and surgical kits made by
3M, Heine and Rossmax to pharma companies and hospitals, and another 11%
came from point of care test consumables used in clinic camps. Services
made up 31% of revenue. That line runs about 32,380 health camps a year
with field teams of physiotherapists, phlebotomists and nurses, plus 20
patient support programmes (PSPs), where counsellors and a 150 seat call
centre keep patients on their prescribed therapy for months at a time. A
pharma client finds these services hard to drop because tighter limits
on direct promotion to doctors push drug companies toward patient
programmes, and a running PSP ties the vendor's CRM dashboards into the
client's own tracking. The customers are more than 130 institutional
buyers, including more than 50 pharma companies with the top 10 among
them, hospitals since FY25, and a small online retail slice under 1% of
revenue. PSP contracts run for several months, and management puts
rollover at 60 to 70%, which also means 30 to 40% of programmes do not
renew. No filing discloses the top client's share of revenue, so the run
did not establish customer concentration. Present demand rests on pharma
promotion budgets: the Indian pharma market grew 9% in CY2025 after
6.4% the year before, and the slice spent on patient programmes and
screening camps was Rs 1,613 Cr in 2024, which the "IQVIA Indian
Pharmaceutical Market size and promotional-spend %" signal tracks. The
live driver that QMS and two peers name is the wave of GLP-1 obesity and
diabetes drugs, tracked by "GLP-1/anti-obesity drug India launches and
generic entries", and the peers confirm the tailwind is real but broader
than the QMS framing. Forward demand has two documented legs. HEINE made
QMS its sole India distributor for five years from 1 January 2027, on an
India revenue base of about Rs 30 Cr that HEINE expects to reach Rs 70
Cr by 2031, tracked by "HEINE Optotechnik India revenue delivery vs Rs
30 Cr (2026) to Rs 70 Cr (2031) path". The second leg is the composite
scheme that folds the QMS and HCAH patient programme books into
Saarathi, promising 160 plus programmes and 1.2 million patients,
tracked by "HCAH/Saarathi composite scheme NCLT and shareholder approval
progress" and still short of court and shareholder approval. Management
sizes the India PSP market at about US$1 bn by 2030, growing 15 to 20% a
year, while the US$70 bn figure in its deck is a global number with no
QMS revenue in it; the "CDSCO import/distribution licence status" and
"Named pharma-client relationship count and renewal" signals gate the
product and client sides. The products line has no moat of its own: its
edge is supplier granted exclusivity plus a CDSCO licence, smaller
traders still compete, and pricing power is weak. The services line
carries moderate advantages: the emerging moat scan scored qualification
lock in through the SOC 2 Type II certificate, customer relationships
and execution as Moderate, and strategic partnerships (HEINE and HCAH)
as Strong. Talent asymmetry (Category 21) and the cannibalization
barrier (Category 22) both scored zero, because a funded rival such as
Indegene could build a comparable PSP platform without destroying
anything of its own. The own brand, Q-Devices, is small at Rs 14 Cr in
FY26 and three years old, so its brand advantage is low to moderate, and
the scan's total of 17 sits in the MODEST band.

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. VERTICALS FRAMED (one per dominant variable, Section 2 C1)

**Vertical 1 — Services margin vs mix.** The corpus establishes: Services
rose from 31% (FY26) to 41% (Q1 FY27) of consolidated revenue (B00
LBF1); consolidated EBITDA margin fell from 16.3% to 15.0% and printed
14.6% in Q1 FY27 (B04); no segment result note exists in either AR to
show which line drives the fall (B02, B03); a note-level cost inference
points to Products, not Services, as the FY26 margin drag (B02 top
finding rank 1); management stated in August 2026 that PSP margin sits
below camps margin (B12b F7, referencing Concall_Aug_2026). What it
cannot establish: an audited products-vs-services margin split, or
whether the margin dip is transient (front-loaded hiring against signed
contracts) or a permanent feature of cost-plus PSP pricing. Questions
that decide it: (1) Will the FY27 AR add a segment result? (2) Does
consolidated margin turn up as Services crosses 40-45% for two more
quarters? (3) What is the actual gross margin, by line, once the scheme
valuation report or NCLT petition discloses carve-out financials for
the Services undertaking?

**Vertical 2 — Cash quality and working capital.** The corpus
establishes: FY26 reported consolidated operating cash flow of ₹19.44 Cr
(1.63x PAT) falls to ₹2.77 Cr (0.23x PAT) once the year's ₹16.67 Cr
short-term borrowings increase, embedded inside operating activities in
both cash flow statements with no policy note, is removed (B03);
receivables aged over six months doubled 14.5%→30.6% with zero ECL
provisioning (B02); audited DSCR fell to 0.79x against an MD&A-stated
1.99x for the same year (B02, B03); a new ₹19.69 Cr bill-discounting
facility appeared while payables turnover rose 23.9% (B02). What it
cannot establish: whether this is GROWTH-INDUCED (funding a real
receivables build behind revenue growth) or STRUCTURAL (a permanent
funding gap), because no receivables composition by product line or top
debtor exists, and no rating agency or management collection-plan
statement exists (B01 FLAG-CASH, INDETERMINATE). Questions that decide
it: (1) Does the H1 FY27 cash flow statement, ex short-term borrowing
change, clear 0.7x H1 PAT? (2) Does the receivables >6-month share fall
in the FY27 AR? (3) What interest rate applies to the Saarathi ICD, and
does interest cover hold above 3x?

**Vertical 3 — Entity boundary of the Saarathi/HCAH scheme.** The corpus
establishes: the 25-Sep-2026 board outcome approves a composite scheme
moving QMS's healthcare-services undertaking and HCAH's programme book
into Saarathi (the "Resulting Company"), which issues shares directly,
1-for-1, to QMS's own equity shareholders as of Record Date 1, and
cancels QMS's own existing holding in Saarathi without consideration;
post-arrangement, public holders take 59.5% of Saarathi and promoters
40.5% (see Section 6, Q7, for the printed clause). What it cannot
establish: the scheme's own effective/completion date (only the linked
BeamOptics indicative date of 30-Nov-2027 is given, B07); whether NCLT
and shareholder approval will complete on the terms filed; the combined
entity's actual post-scheme financials. Questions that decide it: (1)
Does NCLT approve the scheme as filed? (2) What carve-out financials
does the valuation report annexed to the scheme show for the Services
undertaking? (3) Does the FTTCP need to be re-pointed at a different
listed entity once the scheme is effective?

**Vertical 4 — PSP/GLP-1 pipeline conversion.** The corpus establishes:
QMS and peers name GLP-1 launches as a PSP demand driver (B05, B06);
management states one signed programme needs ~1,200 hires against a
company headcount near 250 (B12b F1 context); Q1 FY27 employee cost rose
₹3.2 Cr to ₹11.2 Cr YoY (3.5x) while COGS stayed flat and revenue grew
only 1.22x (B04 FLAG-COST). What it cannot establish: how many GLP-1-
linked programmes are actually signed versus pipeline (count moved from
7 in Jun-2026 to "4-5" in Aug-2026 with none named, B12b F14); whether
the hiring converts to margin-accretive revenue or stays cost-plus thin
(B12b F7). Questions that decide it: (1) Do Q2/Q3 FY27 PSP revenues
track toward the ₹90-105 Cr FY27 guided range? (2) Does the company ever
name a signed GLP-1 programme? (3) Does margin move with, or against,
the reported services share next quarter?

### 4b. CANDIDATE SIGNAL TABLE (expanded from B09 Section 6 candidates)

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| HCAH/Saarathi composite scheme NCLT and shareholder approval progress | Scheme rejected, materially amended, or stalled beyond 12-24 months without approval | Event-Driven | NCLT cause-list / MCA filing portal; QMS Reg 30 filings |
| HEINE Optotechnik India revenue delivery vs Rs 30 Cr (2026) to Rs 70 Cr (2031) path | HEINE India revenue flat or declining against the stated path, or exclusivity not renewed at term end | Annual | QMS Reg 30 updates; HEINE Optotechnik GmbH disclosures if public |
| GLP-1/anti-obesity drug India launches and generic entries | No new India launches/generic entries for 2-3 consecutive quarters while QMS still cites GLP-1 as the primary PSP driver | Quarterly | Company press releases (Novo Nordisk India, generic manufacturers); IQVIA India monthly data |
| IQVIA Indian Pharmaceutical Market size and promotional-spend % | Promotional-spend share of IPM flat or falling while QMS guides rising Services growth off this base | Quarterly | IQVIA India Quarterly Insights reports |
| CDSCO import/distribution licence status | Licence lapse, suspension, or non-renewal | Event-Driven | CDSCO portal |
| Named pharma-client relationship count and renewal (50+ companies per HEINE press release) | Client count or top-10 concentration worsens with no offsetting new signings disclosed | Quarterly | Individual pharma-company investor disclosures; QMS AR client references if disclosed |

### 4c. FRAGILITY READ

- **variable_count:** 6 (Services margin/mix convergence; normalized cash
  quality; the scheme's entity-boundary outcome; GLP-1 pipeline
  conversion; HEINE exclusivity/inventory ramp; Q-Devices ramp against
  its reset target).
- **verifiability_ratio:** 3 of 6 externally observable (GLP-1 India
  launch dates, CDSCO licence status, and NCLT/scheme filing progress
  are outside-company evidence); 3 of 6 company-narrated only (Services
  margin split with no segment note, cash-quality resolution reads
  through the company's own future filings, Q-Devices ramp has no
  independent source).
- **single_point_failure:** the Sep-2026 scheme's entity outcome. If the
  Services undertaking transfers out of listed QMSMEDI into a
  separately listed Saarathi on the filed terms (see Section 6, Q7),
  the services-led transition thesis for the listed entity QMSMEDI
  fails regardless of how every other variable performs (B07, B08).
- **fragility_verdict:** **FRAGILE** — six variables, half company-
  narrated only, one clean single point of failure, against a backward
  financial picture already showing deteriorating cash conversion and a
  credibility grade at the C/D boundary (B03, B05, B12b).

### 4d. RESEARCH BRIEF (claude.ai live-web work order)

1. Verify the 25-Sep-2026 scheme's NCLT/shareholder approval status and
   any amendment to its terms (Section 4e Chain 1 equivalent; PENDING
   LIVE VERIFICATION).
2. Verify HEINE Optotechnik's India and global revenue independently of
   the QMS press release (single-source risk, B09 searches_skipped).
3. Verify semaglutide/GLP-1 generic launch dates and the count of
   launching firms in India.
4. Verify any government duty or anti-dumping action on medical device
   imports from China or ASEAN countries (raised repeatedly by peer
   POLYMED, never by QMS, B06).
5. Confirm the outgoing FY24-25 statutory auditor's identity and
   resignation reason via the NSE Emerge filing archive (B08 deal-
   breaker item, undisclosed in this corpus).
6. Confirm MCA/RoC status of Queens Promotional Services, UMC Medical
   Allied Services, ABAE Technologies, and any Mayukh Healthcare
   Services LLP link to Saarathi (B08 searches blocked by HTTP 403).
7. Pull current CMP and P/E for QMSMEDI at valuation time (B09 gap; web
   search during this run returned inconsistent, stale readings).
8. Verify CDSCO import/distribution licence current status directly
   from the CDSCO portal.
9. Verify the Saarathi/HCAH scheme's valuation report and NCLT petition
   for carve-out financials of the Services undertaking.
10. Track Indegene, Entero and Poly Medicure's Q2/Q3 FY27 disclosures as
    they publish, for continued peer cross-checks on margin mix,
    working-capital days, and the Chinese-dumping and GLP-1 claims.

### 4e. SECOND-ORDER STUB (Master Prompt v3.7, Rule F)

CHAIN 1: Services rose from 31% of FY26 consolidated revenue to 41% of
Q1 FY27 revenue, while consolidated EBITDA margin fell from 16.3% (FY25)
to 15.0% (FY26) and printed 14.6% (Q1 FY27) (B04, B05).
Link 1 [FILED]: No segment result note exists in either the FY26 or
FY25 annual report; management has never disclosed a products-vs-
services margin split (B02, B03).
Link 2 [FILED]: A note-level cost inference from the AR's disclosed
cost lines suggests products gross margin compressed from 26.3% to
23.6% FY25→FY26, the opposite of a naive "services mix hurt margin"
read (B02 top_findings rank 1).
Link 3 [INFERENCE]: If products, not services, is the margin drag, the
stated transition (mix shifting toward higher-margin services) should
already be lifting group margin, and its absence points either to new
PSP contracts pricing cost-plus with a thin markup (management's own
Aug-2026 admission that PSP margin sits below camps margin, per B12b
F7) or to the products drag currently outweighing the services lift.
Binding constraint: no filed segment result exists to test which
reading holds; the constraint is disclosure, not arithmetic.
Unsaid: neither annual report explains why a Significant Accounting
Policies note or a segment note is absent for two consecutive years,
despite both auditor's reports referencing policy notes that do not
appear in the filed text (B02 top_findings rank 5).
Observation that confirms or breaks this chain, and confirm-by date: a
filed segment result (FY27 AR, expected ~May-2027) or the Sep-2026
scheme's valuation report / NCLT petition, whichever files carve-out
financials for the Services undertaking first (B02, B08). NCLT filing
status: PENDING LIVE VERIFICATION — Claude web should check the NCLT
cause-list and MCA filing portal for the scheme's case status.

CHAIN 2: FY26 consolidated operating cash flow of ₹19.44 Cr (1.63x PAT
as reported) falls to ₹2.77 Cr (0.23x PAT) once the year's ₹16.67 Cr
short-term borrowings increase, embedded inside operating activities in
both cash flow statements with no policy note, is removed (B03).
Link 1 [FILED]: Standalone DSCR fell to 0.79x in the audited financial-
statement ratio note (Note 46), down from 2.54x, while the same annual
report's MD&A states DSCR of 1.99x for the identical year (B02, B03).
Link 2 [FILED]: Receivables aged over six months rose from 14.5% to
30.6% of the due book with zero ECL provisioning, and a new ₹19.69 Cr
bill-discounting facility (nil in FY25) appeared while trade payables
turnover rose 23.9%, meaning the company paid suppliers faster while
collecting from customers slower (B02).
Link 3 [INFERENCE]: A company funding its receivables gap with fresh
short-term bank lines and bill discounting, against an interest cover
already at 3.51x (one band above the Gate-0 3x deal-breaker line), has
little room left before a single quarter of slower collections or a
rate rise pushes coverage below the deal-breaker threshold, independent
of whether the underlying operating business is improving.
Binding constraint: no credit rating and no financial-instruments/
risk-management note exist anywhere in the corpus to independently
benchmark this coverage headroom (B00, B02).
Unsaid: the annual report gives no management explanation anywhere for
the receivables-ageing deterioration or the new bill-discounting
facility, despite both appearing in the same year the company also
raised a rights issue (B02).
Observation that confirms or breaks this chain, and confirm-by date:
the H1 FY27 cash flow statement (Q2 FY27 results, expected mid-Nov-
2026), read after removing the change in short-term borrowings from
operating cash flow (B03 monitorables). Counterparty/rating evidence
this container cannot reach: whether any bank covenant sits behind the
new bill-discounting facility. PENDING LIVE VERIFICATION — Claude web
should check for any disclosed facility covenant or bank-sanction
letter reference in later Reg 30 filings; never fabricate a
counterparty fact.

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in
claude.ai with live web, before Role 2.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. QMS Medical Allied Services buys foreign-brand medical devices and
   resells them to pharma companies and hospitals in India.
2. It also runs paid health camps and phone-based patient support
   programmes for drug companies, using nurses, counsellors and a
   150-seat call centre.
3. Device reselling made about 69% of FY26 revenue; the patient-service
   work made about 31%, rising to 41% in the first quarter of FY27.
4. Pharma companies buy the services because rules limit direct pitching
   to doctors, so they pay QMS to reach and retain patients instead.
5. More than 130 institutional buyers use QMS, including over 50 pharma
   companies, but no filing names the top client's share of revenue.
6. Demand today tracks pharma promotion budgets, which grew as the
   Indian pharma market grew 9% in the last full year.
7. A new wave of GLP-1 weight-loss and diabetes drugs is the demand
   driver both QMS and its peers point to for future patient-programme
   growth.
8. Two future demand legs stand out: a five-year sole-distribution deal
   with device maker HEINE from January 2027, and a merger scheme that
   combines QMS and a partner's patient programmes inside a company
   called Saarathi.
9. The device-reselling line has no real moat: it depends on a licence
   and on suppliers choosing to keep QMS as their distributor, and other
   traders could compete for the same brands.
10. The patient-services line has some real advantages: a security
    certificate, sticky multi-month contracts and two strong named
    partnerships, but nothing that stops a well-funded rival from
    copying it.
11. The core idea being tested is whether QMS is shifting from a
    lower-quality device-trading business to a higher-quality,
    contract-based services business, and whether that shift shows up
    in profit, not just in revenue mix.
12. On the evidence gathered, this shift looks fragile: six things must
    go right, half of them can only be checked through the company's own
    future statements, and one event, a September 2026 corporate
    restructuring, could move the entire services business out of this
    listed company.
13. The company's own annual report cannot answer the most important
    question, whether services or devices earn the better margin,
    because it carries no breakdown of profit by business line.
14. Cash generation looks weaker than the headline number suggests once
    new short-term borrowing is stripped out of the reported operating
    cash flow, and no credit rating exists anywhere to check this
    independently.
15. The two biggest open questions are: does the September 2026
    restructuring keep the patient-services business inside this listed
    company, and does profit actually rise as patient services grow, or
    does it keep falling.

---

## SECTION 6: STANDING EXTRACTION ANNEX

**1. UNITS.** No per-camp or per-PSP fee is printed anywhere in the
corpus. The 04-Jun-2026 investor presentation (Analysts-Institutional-
Investor-Meet deck) prints camp counts and camp revenue by year on the
same slide: "24,823 / 30,393 / 32,380" camps for FY24/FY25/FY26 against
"17.0 / 17.5 / 22.9" (₹ Cr camps revenue) for the same years
(20260604-Analysts-Institutional-Investor-Meet-Con-QMS deck, page
[page 18] per its page markers). Comment: this is a basket figure (all
B2B camps combined, not per-camp), and a per-camp average can be derived
(₹22.9 Cr / 32,380 camps ≈ ₹7,072/camp for FY26) but is not itself a
disclosed figure; treat any per-unit number as [INFERENCE], never as a
printed unit price (B04 confirms unit economics are derived, not
disclosed).

**2. SEGMENT CAPITAL AND DEBT.** NOT DISCLOSED. No segment result note
(revenue, assets, liabilities or capital employed by segment) exists at
either the standalone or consolidated level in either the FY26 or FY25
annual report; only a one-sentence single-segment statement is printed
(B02 top_findings rank 1, "STAGE 2 OWN GAP"). Total consolidated
borrowings are ₹74.48 Cr and standalone short-term borrowings ₹67.51 Cr
(B00 LBF2), unallocated by segment because no segment structure is
disclosed at all.

**3. GUIDANCE VERSUS ASPIRATION.** From B05 guidance_table and
promise_delivery (concall-sourced, quote-then-comment where the
transcript text is already anchored in B05):
- (a) Guidance with a period: "FY27 revenue guidance Rs 216 Cr," stated
  Q4 FY26 call (Jun-2026), reaffirmed Q1 FY27. Comment: has a stated
  period and number; tracking at ~26% of target after Q1.
- (a) Guidance with a period: "FY27 EBITDA margin guidance 18-19%,"
  stated Q4 FY26 call, reaffirmed Q1 FY27 despite a 14.6% Q1 print.
  Comment: guidance held unchanged against a contradicting quarter.
- (b) Aspiration without a firm period: "Rs 500 Cr revenue by FY29"
  (companies/QMSMEDI.md LBF4). Comment: per B05, this number was never
  stated on any of the four transcripts read; it appears only in the
  27-Aug-2026 HEINE press release and has never been defended under
  live analyst questioning (B05 input_gaps, B07 catalysts_12m anchor).
- (c) Capacity/capability only: "Services growth vs product: double the
  product growth rate (~25%)," Q2 FY26 call (Nov-2025). Comment: framed
  as a rate relationship, not a firm rupee target, and was itself
  revised in later calls (B05 timeline_slippages).

**4. CONCENTRATION.** Product, customer and geography concentration:
NOT DISCLOSED. "Top-client / customer revenue concentration percentage
not disclosed anywhere in the corpus" (B04 input_gaps). More than 130
institutional buyers and more than 50 pharma companies are named as the
customer base, with "the top 10 among them" referenced qualitatively
but never quantified (Section 3 narrative, sourced to B04/B00). No
geography breakdown (branch count, state-wise revenue) is disclosed
anywhere (B04 input_gaps).

**5. PROMISE LEDGER.** From B05 promise_delivery.rows (concall-sourced,
each already anchored to its stated-in call):

| Promised in | Promise | Status | Evidence anchor |
|---|---|---|---|
| Q1 FY26 (Aug-2025) | Q-Devices FY26 revenue at least Rs 25 Cr | MISSED — actual Rs 14 Cr | Concall_Aug_2025 |
| Q1 FY26 (Aug-2025) | Combined services revenue at least Rs 60 Cr FY26 | PARTIAL — actual ~Rs 53.9 Cr | Concall_Aug_2025 |
| Q1 FY26 (Aug-2025) | Saarathi stake to 76% by Sep-2025, 100% by Sep-2026 | DELIVERED on schedule | Concall_Aug_2025; B00 corpus |
| Q2 FY26 (Nov-2025) | Margins normalize in FY27 | PARTIAL/ONGOING — FY26 15% vs ~17% guide | Concall_Nov_2025 |
| Q4 FY26 (Jun-2026) | FY27 revenue guidance Rs 216 Cr | TRACKING — ~26% of target after Q1 | Concall_Jun_2026 |
| Q4 FY26 (Jun-2026) | Camps revenue Rs 18-20 Cr FY27 | PARTIAL/TRACKING — base figure disputed, ~32-36% of target after correction | Concall_Jun_2026; Concall_Aug_2026 |
| Q4 FY26 (Jun-2026) | Employee cost stabilizing, implying operating leverage | PARTIAL/REFRAMED — rose further QoQ | Concall_Jun_2026; Concall_Aug_2026 |
| Q1 FY26 (Aug-2025) | Inorganic discussions ongoing in B2B distribution | MISSED/DROPPED — no later update | Concall_Aug_2025 |

**6. RESTATED BASES.** Two restatements found, both unquantified in the
filed text (B02 restatements_found): "Previous year figures have been
regrouped to comply with current period groupings" — quoted from Note
45 standalone (AR p.113) / Note 43 consolidated (AR p.145), with no
quantification of what was regrouped or its amount, either year. The
gratuity actuarial note (Note 33 consolidated, AR p.141) shows the FY26
opening defined-benefit obligation as "Rs 0.00 lakh" on a restated
basis, against a prior-year (FY25) opening figure of Rs 21.22 lakh,
with no note explaining the restatement's driver or quantum.

**7. CORPORATE-ACTION CLAUSES.** The 25-Sep-2026 composite scheme of
arrangement (20260925-Acquisition-QMS_25092026185825_Outcome250926.pdf)
is in the corpus. Definitions: "QMS" is defined as the "Demerged
Company 1"; Saarathi (Health Care at Home India Private Limited's
merger partner entity) is defined as the "Resulting Company"; a second
entity is the "Demerged Company 2" (HCAH) (filing, opening recitals,
line 29-31). Ratios: for QMS shareholders, "1 fully paid Equity Share
of INR 10/- each in the Resulting Company for every 1 fully paid Equity
Share of INR 10/- each held in the Demerged Company 1" (filing, lines
271-275). Liability allocation / share entitlement: "the Resulting
Company shall... issue and allot on a proportionate basis its equity
shares... to QMS Equity Shareholders as on the Record Date 1" (filing,
lines 264-269), and separately, "the entire existing paid-up share
capital of the Resulting Company held by the Demerged Company 1
(directly and/or through nominees) shall stand cancelled, reduced and
extinguished, without any consideration" (filing, lines 192-197). Pre-
arrangement, Saarathi is 100% held by QMS (8,25,000 shares); post-
arrangement, Saarathi's public holders (i.e., QMS's own erstwhile
public shareholders) hold 59.5% and promoters 40.5% (filing, lines
213-247). **This resolves the OPEN CONFLICT between B08 and B07: the
filing's printed clause confirms B08's reading — QMS shareholders
receive Saarathi shares directly, one-for-one, on Record Date 1, and
QMS's own holding in Saarathi is cancelled without consideration, not
retained as a stake.** Appointed/effective dates: the scheme's own
completion date is not separately printed in this filing; only the
linked BeamOptics indicative date of 30-Nov-2027 is given (B07
input_gaps), so the scheme's own effective date is NOT DISCLOSED in
this document and should be fetched from the eventual NCLT order or a
later Reg 30 filing.

**8. RELATED-PARTY PERIMETER.** From B08/B02 (AR FY26 Note 31, p.108-
109, latest year FY26): Mahesh Makhija (MD), remuneration Rs 200.00
lakh (+19.05%); Guddi Makhija (wife, non-board salaried employee),
remuneration Rs 29.00 lakh (+107%); Diti Makhija (daughter),
remuneration Rs 19.10 lakh (+40%); rent of Rs 2.40 lakh paid to Mahesh
Makhija (nil FY25); Saarathi Healthcare (24%-minority-held subsidiary
through FY26), inter-corporate deposit payable Rs 1,885.95 lakh year-
end, interest paid Rs 136.61 lakh on a principal draw of Rs 1,644.09
lakh, interest rate NOT DISCLOSED (contrast: One Billion Diagnostics
loan carries a disclosed 9% p.a. rate, Note 32).

**9. PLEDGE AND SHAREHOLDING.** Promoter pledge: 0% across all three
shareholding-pattern XBRL snapshots held in the corpus (30-Jun-2025,
31-Mar-2026, 30-Jun-2026); the corpus does not hold twelve quarters, only
these three, so the full 12-quarter series is NOT DISCLOSED in this
corpus (B00, B08 pledge_trend). Promoter holding: 73.67% (30-Jun-2025)
→ 68.11% (30-Jun-2026), attributed to Sep-2025 rights-issue dilution,
not a promoter sale (B00, B01 data_notes). Institutional (FII/DII)
holding percentage: NOT DISCLOSED in any stage block; the raw XBRL
files (inputs/shareholding/QMSMEDI-SHP-*.xml) were not parsed for this
figure by any stage this run.

**10. VERIFICATION.**
- FY26 AR: Annual_Report_2026.pdf, Annual Report 2025-26 (9th AGM).
- FY25 AR: Annual_Report_2025.pdf, Annual Report 2024-25.
- 25-Sep-2026 scheme filing:
  20260925-Acquisition-QMS_25092026185825_Outcome250926.pdf.
- 04-Jun-2026 investor deck:
  20260604-Analysts-Institutional-Investor-Meet-Con-QMS_04062026111529_SdInvestorPresentation.pdf.
- Concall transcripts: Concall_Aug_2025_Transcript.pdf,
  Concall_Nov_2025_Transcript.pdf, Concall_Jun_2026_Transcript.pdf,
  Concall_Aug_2026_Transcript.pdf.
- Rights issue Letter of Offer:
  20250903-Rights-Issue-Letter-of-Offer-QMS_03092025204344_SdIntimationLOF.pdf.
- Shareholding XBRL: QMSMEDI-SHP-2026-06-30-NSE.xml,
  QMSMEDI-SHP-2026-03-31-NSE.xml, QMSMEDI-SHP-2025-06-30-NSE.xml.

CORPUS COMMIT HASH: baa9adc51fd2652a36db08823e6c48e5e610b987
