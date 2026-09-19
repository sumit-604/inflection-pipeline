# HALT 1 UNDERSTANDING DOSSIER: eMudhra Ltd (EMUDHRA)

Run date: 2026-09-19. Assembled from committed blocks B00 through B09 and
verifier blocks B12a through B12d (round 2) plus confidence.yaml. This is an
understanding document. It carries no valuation, no price, no verdict.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

### 1. Concalls
Three transcripts held, all earnings calls:
- Q3 FY26, call date 2026-02-03 (inputs/concalls/Concall_Feb_2026_Q3FY26_Transcript.pdf)
- Q4 FY26, call date 2026-05-07 (inputs/concalls/Concall_May_2026_Transcript.pdf)
- Q1 FY27, call date 2026-07-30 (inputs/concalls/Concall_Aug_2026_Transcript.pdf)

Most recent quarter covered: Q1 FY27 (quarter ended 30-Jun-2026). Against
the run date of 19-Sep-2026, Q2 FY27 (quarter ending 30-Sep-2026) has not
yet closed, so no later transcript is plausibly outstanding. (B00)

A fourth item, the 3i Infotech special investor call of 06-Feb-2026, was
moved by the collector from concalls/ to announcements/ because it answers
one legal matter, not an earnings quarter (B00).

### 2. Annual reports
Only the FY26 annual report sits in the annual-report/ folder (contract is
0-1 year; B00). A FY25 annual report was collected but moved to other/ and
preserved, not consumed, because of that contract. The FY26 AR is the
latest completed FY and is present. Fewer than 3 years of standalone AR
PDFs are held; multi-year figures beyond the FY26 AR's own two-year face
comparatives come from screener Data_Sheet exports, not from AR text
(B00, B03).

### 3. Results filings
Three filings held: Q3 FY26 (31-Dec-2025), FY26 Audited (31-Mar-2026), Q1
FY27 (30-Jun-2026). Latest is Q1 FY27, filed 30-Jun-2026 quarter end. No
quarter-gap exists between the latest results filing and the latest AR:
the FY26 AR (year end 31-Mar-2026) predates Q1 FY27 results by one normal
quarter, the expected sequence (B00).

### 4. Investor presentations
Two held: Q4 FY26 (20260507_Investor_Presentation_Q4FY26.pdf, dated
07-May-2026) and Q1 FY27 (20260730_Investor_Presentation_Q1FY27.pdf, dated
30-Jul-2026). Latest is Q1 FY27, 30-Jul-2026 (00-inputs.md manifest).

### 5. Research / rating
No broker note or research report is held (research: 0, B00). Rating
documents held: an ICRA reaffirmation letter dated 29-Jun-2026
([ICRA]A Stable/A1), a full rationale dated 02-Jun-2025 (the prior
upgrade), and a material-event update dated 08-Jul-2025. No full rationale
for the 29-Jun-2026 reaffirmation is held; see the freshness pair check
below.

### 6. Corporate actions
30 announcement PDFs held, Step 1 hand-fetched 29 material Reg 30 filings
plus the special-call transcript, spanning roughly 03-Feb-2026 (the 3i
Infotech clarification letter) to 18-Aug-2026 (the EOW civil-closure
letter). The set covers the 3i Infotech dispute correspondence, the
Cryptas/AI Cyberforge acquisition disclosures, and the postal-ballot board
appointment notice (B00, B03, B08).

### 7. Freshness pair check
B00's freshness_verdict is CORPUS GAPPED-FRESHNESS. Of the four defined
pairs:
- RESULTS to CONCALL: PASS.
- RATING BULLETIN to RATIONALE: **FAIL**. Trigger document held: the ICRA
  reaffirmation letter dated 29-Jun-2026. Mate expected: an ICRA rating
  rationale dated on or about 29-Jun-2026. Missing. Only the 02-Jun-2025
  rationale is held; icra.in blocks scripted retrieval.
- SEBI ORDER to ORDER TEXT: PASS (no triggering order referenced beyond
  director-eligibility boilerplate).
- AR to LATEST AUDITED ANNUAL RESULTS: PASS.

### 8. Verdict line

**CORPUS GAPPED-FRESHNESS**: the RATING BULLETIN to RATIONALE pair failed.
Missing mate: the ICRA rating rationale for the 29-Jun-2026 surveillance
action, expected source rating agency site (icra.in). This verdict takes
precedence; the phase-1 gate recommendation caps at PROCEED WITH CAVEATS
per the orchestrator (B00).

Other gaps carried under this verdict, findable-but-missing (operator
upload list):
- Prior-year annual reports beyond FY26 (FY24 and earlier), expected
  source: BSE / company IR page. Only 1 AR year sits in the working
  folder; a second (FY25) exists but is out of stage scope.
- Full 12-quarter (3-year) BSE shareholding-pattern history for the pledge
  and promoter-trend check. Only two Reg 31 summaries are held (Mar-2026,
  Jun-2026). Expected source: BSE.
- FII/DII institutional split, not present in the AR text or the BSE
  summaries held; only available on screener (non-anchored). Expected
  source: BSE shareholding pattern detail pages.

Plausibly-nonexistent (a data point in itself, opacity feeds the operator
decision, not the pipeline's):
- No broker research coverage exists in the corpus and none was found; a
  small/micro-cap with limited sell-side coverage.

**EMPTY-FOLDER CONFIRMATION** (repeated per task instruction; the /step1
autonomy contract suppressed the standing prompt with "proceed with the
gaps"): prospectus/ is empty (not a gap, listed June 2022, more than 3
years before this run) and research/ is empty (no broker notes exist).
Both folders were accepted as gaps at intake; the run proceeds on the
degradation map.

**Open operator rulings carried into this dossier, unresolved, from the
evidence stages**:
- Gate 0 Block B window convention. B01 filed GOOD+ (core 74, Block B 12,
  scoring B2 through B4 on a 2-year FY25 to FY26 window because the full
  8-year trade-payables/FCF history is not extractable). B01 also states
  the alternative reading, GOOD (core 67, Block B 5, deal-breaker #2
  triggers) if that window is rejected. Verifier C (B12c, round 2)
  independently recomputed a third reading and found the filed approach
  MAJOR-noncompliant on a different rule: B4's "earliest year" should be
  FY19 (matching A4's window), not FY25; FY19 trade payables are not in
  the provided data, so B4 should be N/A/0, giving Block B 7, core 69,
  and the same deal-breaker #2, landing at GOOD, not GOOD+. All three
  readings (B01 primary GOOD+, B01 alternative GOOD, B12c recomputed GOOD)
  need one operator ruling on the window convention; every downstream
  stage that reads B01's classification (notably B07's combined_assessment)
  currently carries GOOD+ / GOOD as parallel, unresolved readings.
- prompts/07 Section 6D references a combined backward-times-forward
  8-tier classification matrix (EXCEPTIONAL / EXCELLENT+ / HIGH POTENTIAL /
  GOOD+ / GOOD / TURNAROUND / AVERAGE / AVOID) that B07 and Verifier C both
  independently searched for and could not locate in frameworks/ or
  prompts/. B07's GOOD+/GOOD combined labels are derived from first
  principles, not read off this table. Flagged for Stage 9/13 (O1, B12c).
- Sector cap row: Platform / SaaS / IT services (45x neighbourhood) was
  used, not Cybersecurity / VAD (25x), on the reasoning that eMudhra owns
  its PKI/identity/signing IP outright rather than distributing certified
  third-party products (B00, confirmed by B04). The ~21% pure-services
  revenue line argues partly the other way. Flagged for phase-3
  confirmation before Stage 11 applies it.

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT - PENDING OPERATOR SIGN-OFF.** Nothing in this section is signed.
Signing happens in claude.ai after live-web stress-testing.

### PART A: THE FROM STATE

**A1. Archetype (per line).**
- Trust Services (20% of FY26 revenue, licensed certifying-authority
  business): **Licence/scarcity business**. A Government of India CCA
  licence (renewed every 5 years) plus WebTrust accreditation gate entry;
  only 24 licensed Indian CAs exist, 10 actively issuing (Q4FY26 Inv.
  Pres. slide 8, cited in B04). Regulated price, capacity effectively
  capped by licence count, not by demand.
- Enterprise Solutions (59% of FY26 revenue, owned PKI/identity/signing/
  contract-lifecycle software sold globally): closest fit is
  **Platform/network**, with a switching-cost core (67% existing-customer
  revenue share, AR p.55, B04) more than a network effect (B04 explicitly
  finds no evidenced network effect). The remaining 21% (project consulting)
  folds statutorily into this segment under Ind AS 108 Note 49 (AR p.288,
  B04) and does not carry its own archetype.

**A2. The simple analogy.** eMudhra today runs two businesses under one
roof. One is a government-licensed notary: it stamps digital signatures
under an Indian regulator's certificate, a fee-per-signature business,
much like a toll booth on paperwork, serving mostly Indian individuals and
firms through CA partners who take a 45 to 50% commission (B04). The
other is a software company that sells identity, signing, and
contract-management tools to enterprises worldwide, priced like
subscription software, now 64% sold outside India (company memory,
corroborated by AR segment splits, B04). The notary business is small,
stable, and cash-generative; the software business is the one the company
wants to be judged on, and the one it has spent two acquisitions this
year building out.

### PART B: THE TRANSITION

**B1. FROM to TO.** One declared line (the two segments do not report
separate capital employed, so the transition is declared at the
consolidated level, evidence noted by segment where it differs).
FROM: **R2 COST-ADVANTAGED / LICENCE-PROTECTED CONVERTER.** Consolidated
ROCE sits at 12.9% (closing capital employed) to 14.9% (average capital
employed) FY26 (B03), near but under the "durable mid-teens" R2 band; the
Trust Services licence and Enterprise Solutions switching costs lift the
business above a pure commodity price-taker (R1), but blended ROCE has not
yet cleared the R3 20 to 25% band.
TO (claimed): **R3 VALUE-ADDED / SPEC'D SUPPLIER**, with a stretch claim
toward R4 FRANCHISE if the India Enterprise Solutions segment's 57.5%
margin (FY26, Note 49, AR p.288) is a preview of where the international
book lands once scaled. This dossier states the claim as claimed, not
proven: the one year of segment evidence available runs the wrong way
(Part B3).

**B2. The engine.** Two things must physically change for FROM to become
TO. First, the revenue mix keeps shifting from India-only Trust Services
fee income toward global Enterprise Solutions subscription/licence
revenue, already 64% international (company memory, corroborated by
segment data, B04). Second, and this is the one the model actually rests
on, the international Enterprise Solutions segment margin must close
toward the India segment's margin as overseas headcount investment
matures into revenue scale (AR p.152 attributes the 17.6% to 19.46%
employee-cost rise to "addition of senior management resources in
overseas geographies," B04). Two 2025-vintage acquisitions, Cryptas
(Europe, PKI/digital trust, consolidated 1-Jul-2025) and AI Cyberforge
(US, key and secrets management, consolidated 1-Jul-2025), are the
accelerant for the first change, not a substitute for the second (B02,
B03).

**B3. The proof gate.** Exact metric and threshold: **Outside-India
Enterprise Solutions segment operating margin (Ind AS 108 Note 49, AR
p.288) narrows for two consecutive annual prints toward the India
segment's 51 to 58% band, without a disclosed one-off cost relief
explaining the move.** This has **not fired**. The one year of data
available moved the wrong way: 26.0% (FY25) to 21.9% (FY26), even as
international revenue grew 38.3% (B04). A secondary, faster-cadence
corroborating signal exists in consolidated EBITDA margin holding above
roughly 25% for two or more consecutive quarters (B05 trigger 1), but
Verifier B found the one quarter that cleared this bar, Q1 FY27 at 26.2%,
was partly a mix artefact of temporarily lower low-margin token sales per
management's own words, not a clean read of the underlying trend (B12b
MAJOR finding). Until the AR-level segment metric moves, the transition is
narrative.

**B4. The recognition gap** (open question, resolved at Stage 11). Whether
the market's current multiple already prices in the margin-convergence
story this dossier describes, or still leaves room to reward it once the
proof gate in Part B3 fires, is not answered here. Stage 11's exit-multiple
work resolves it via the PE-gap read; this dossier states no figure and
draws no conclusion.

**B5. The ugliness test.** Today's ugly optic: FY26 free cash flow turned
negative for the first time, Rs -52.52 Cr, on capex nearly doubling (Rs
832.02 Mn to Rs 1,853.68 Mn, +122.8%) while CFO grew only 30.8% (B01, B03).
In the same year, goodwill nearly tripled (Rs 1,254.60 Mn to Rs 2,940.46
Mn) on the two acquisitions, and a Rs 881.45 Mn contingent-consideration
liability appeared, uncapped on the EBITDA upside (B02).

Classification: **ARTIFACT-OF-CLIMB**, with a named caveat. Supporting the
artifact reading: CFO stayed above PAT in both years (1.21x FY26, 1.16x
FY25, B03); consolidated working-capital days actually *improved* 11.91
days in the same year the FCF turned negative (81.12d to 69.21d, B01
Correction 2); and the FCF dip traces cleanly to a discrete capex and
acquisition outlay (Rs 1,853.68 Mn capex plus Rs 629.03 Mn net M&A
payment, matching the AR's own MD&A prose figure of Rs 2,482.71 Mn
exactly, B07), not to a broad cash-conversion breakdown. Every phase of
B03's own kill-switch read across governance, accounting, balance sheet,
and earnings independently concluded "would NOT stop here."

The caveat: two items sit outside the FCF story and are not yet resolved
either way. Unbilled revenue (+40.6% YoY) and trade payables (+91% YoY)
both outran 35.1% revenue growth this same year (B02 Pattern A), a
working-capital-funded-growth signal distinct from the capex story. And
the goodwill and contingent-consideration items both carry undisclosed
impairment/fair-value sensitivity assumptions (B02 finding 3, 5), a
disclosure gap specific to the Cryptas deal, not a general transparency
shortfall (B02 analyst note). Neither item alone moves this classification
to STRUCTURAL-FEATURE, but both are the first place a re-classification
would start.

**B6. The transition falsifier** (distinct from the business falsifier,
Part C3). The evidence that would kill the transition thesis specifically:
Outside-India Enterprise Solutions segment operating margin (Note 49)
fails to narrow toward the India segment's band for two more consecutive
annual prints (stays at or below roughly 21 to 22% through the FY27 and
FY28 ARs) while international revenue keeps growing. That combination
would prove the "operating leverage from mix shift" engine (Part B2) does
not exist, and that international growth is margin-dilutive on a lasting
basis, not margin-accretive with a lag.

### PART C: WHAT THE MODEL WATCHES

**C1. Dominant variables** (derived from the engine and the proof gate,
not the static snapshot):
1. **Outside-India Enterprise Solutions segment operating margin** (Note
   49, AR p.288). Current state: 21.9% FY26, down from 26.0% FY25, moving
   against the transition (B04).
2. **Consolidated EBITDA margin trend.** Current state: 23.2% FY26 full
   year, 26.2% Q1 FY27, though Verifier B found the Q1 FY27 print partly
   flattered by temporarily lower token-sales mix, not yet a clean
   corroborating signal (B05, B12b).
3. **Enterprise Solutions organic growth ex-M&A versus the FY27 15 to 18%
   organic guide.** Current state: whole-company organic growth roughly
   15% in Q1 FY27 (28% total income growth, about 13 points from Cryptas),
   against a segment-level management claim of roughly 25% organic for the
   product line specifically; the two readings are not reconciled in the
   corpus (B01, B04, B05).
4. **Free cash flow (CFO minus capex).** Current state: Rs -52.52 Cr FY26,
   the first negative print (B01, B03).

**C2. What the model rejects.** Two sizing questions this model treats as
noise, because the binding constraint is execution, not market size.
First, total-addressable-market size: B09 found 2.69x revenue headroom
against the current serviceable-addressable-market share and a MODERATE
runway class even on the conservative (peer-aggregation) TAM reading; the
SOM-implied CAGR of 24.5 to 25.1% sits above the organic guide precisely
because it assumes continued bolt-on M&A, not because demand is scarce.
Second, the Trust Services CCA-licence renewal cycle: the licence is
mid-cycle with no near-term renewal event disclosed in this corpus, and
the transition this model is built around runs through the Enterprise
Solutions margin question (Part C1.1), not through the licence.

**C3. The business falsifier** (distinct from the transition falsifier,
Part B6; this one kills the FROM business, not just the arrow). Two
candidates, kept together because both threaten the Trust Services
identity or the promoter's standing rather than the software transition:
first, loss of WebTrust accreditation or a browser-vendor distrust/removal
notice for eMudhra's roots, which would be existential for the SSL/TLS and
CA identity the whole company anchors on (B04 first-deterioration
signal). Second, the 3i Infotech matter escalating past the EOW's
13-Aug-2026 civil-not-criminal closure into a confirmed SEBI complaint or
an adverse civil finding against the Executive Chairman, which would
question the FROM business's own governance standing independent of any
software transition (B08). Neither has occurred as of this run.

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

eMudhra sells two things. It issues digital signature certificates under
an Indian government certifying-authority licence, a one-time or two-year
identity credential priced around Rs 1,500, that lets an individual or
business sign tax filings, tenders, bank KYC forms, and contracts without
paper (Q4FY26 Inv. Pres. slide 8, AR p.147, p.156-157, B04). It also
builds and sells owned software, emSigner, SecurePass, and CertiNext, plus
the newly acquired Cryptas and AI Cyberforge product lines, that give
enterprises PKI, identity and access management, e-signature workflow, and
secrets management as licensed or subscribed platforms (AR p.55, B04).
This Enterprise Solutions line is 59% of FY26 revenue; Trust Services is
20%; a smaller project-consulting arm is 21%, folded into the Enterprise
Solutions statutory segment (Note 49, AR p.288, B04).

Trust Services customers are Indian individuals and small businesses,
mostly reached through a CA-partner channel that takes 45 to 50%
commission, with roughly 30% sold direct (Q4FY26 Inv. Pres. slide 8, B04).
Enterprise Solutions customers are named-account enterprises and
governments, disclosed as classes rather than individual names in this
corpus: a US university consortium (InCommon), an unnamed Indian PSU
bank, and government and BFSI buyers in the Middle East (B05, B06). 67%
of FY26 revenue came from existing customers, a switching-cost signal (AR
p.55, B04), though no customer-concentration percentage is disclosed in
any of the three transcripts read (B05). SecurePass deals run Rs 4 to 6 Cr
for a large bank or government entity, Rs 10 Cr or more for a full
PIM/PAM suite (Q1 FY27 call, B05), evidence of a qualification-cycle,
enterprise-procurement buying pattern, not a retail one.

Demand exists for two separate reasons that the corpus can name. Trust
Services demand is regulatory: mandated e-signature and KYC digitisation
in India, and, in the licensed-CA business specifically, downstream
candidates named in B09 such as the Controller of Certifying Authorities'
own licensing rules and browser root-store requirements govern who can
sell at all. Enterprise Solutions demand is compliance-and-modernisation
driven: eMudhra names EU NIS2/DORA implementation as a structural driver
for its Cryptas/PrimeSign European book (B09 downstream candidate, AR
p.21 cites the EU Digital Identity Wallet mandatory-deployment date of
31-Dec-2026), and DPDP Act Phase 2 in India (Significant Data Fiduciary
obligations effective 13-Nov-2026, AR p.29) as the trigger for its
PrivaTrust consent-management product (B07).

Demand should grow if two forward drivers hold, each tied to an
externally verifiable signal named in B09's downstream candidates. First,
the UAE's in-country data-centre mandate and TDRA QTSP licensing process
gates a Middle East Trust Services build-out where infrastructure is
already operating but the licence itself has slipped once already, from
an April to June 2026 target to September to October 2026 (B05). Second,
Gartner and IDC's published cybersecurity and PKI-as-a-Service spend
forecasts are the macro backdrop management itself cites; a material
downward revision there would weaken the demand case independent of
eMudhra's own execution (B09). Peer evidence partially corroborates the
underlying demand picture: NEWGEN and PROTEAN independently confirmed
Middle East order-timing disruption in the same quarter eMudhra's own
calls flag it (B06), the single strongest piece of independent
corroboration this run produced, but the peer set could not corroborate
or contradict the India CA competitive-leadership claim, the NIS2/DORA
acceleration claim, or the UAE mandate's industry-wide reach, all marked
UNVERIFIABLE on structural silence, no true PKI/CA-listed peer exists
(B06).

Where the competitive advantage sits differs sharply by line. Trust
Services carries a real, narrow moat: the CCA licence and WebTrust
accreditation are a regulatory barrier that only 24 Indian entities hold,
10 actively issuing, rated "high durability, narrow scope" (B04, B07
category B2 Qualification lock-in, Moderate strength). Enterprise
Solutions carries a moat built on switching costs and platform breadth
(B07 category A4 Product platform, C1 Customer ecosystem, both Moderate),
but this line has no pricing-power moat yet proven at the margin: the same
segment note that supports the switching-cost claim also shows the
international slice of this business running at less than half the
domestic slice's margin (21.9% versus 57.5% FY26, Note 49, AR p.288, B04),
the opposite of the operating-leverage story the transition thesis names.
The 21% project-consulting line carries no distinct moat; it is described
plainly as a time-and-materials, project-lumpy business with low
predictability (B04). B07's overall Emerging Moat score is MODEST (22.1,
band 12-24), confirmed as MODEST under both open readings of the Gate 0
classification (B07 combined_assessment).

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. Verticals framed (one per Section 2 dominant variable)

**Vertical 1: Outside-India Enterprise Solutions segment margin.**
What the corpus establishes: the India segment runs at 57.5% margin
(FY26) on effectively the same product set that the Outside-India segment
sells at 21.9%, down from 26.0% the prior year, even as Outside-India
revenue grew 38.3% (Note 49, AR p.288, B04). Employee cost rose from 17.6%
to 19.46% of consolidated revenue, attributed in the MD&A to senior
overseas hiring (AR p.152). What it cannot establish: no per-hire revenue
productivity figure, no stated timeline for margin convergence, and no
breakdown of the Outside-India segment by individual geography (US versus
Europe versus Middle East) exists anywhere in the corpus read. Questions
that decide it: (1) Is the FY26 margin dip front-loaded hiring cost ahead
of revenue, or a structurally lower-margin cost base in the new
geographies? (2) What specific named pipeline is the recent overseas
hiring meant to convert? (3) Does the Cryptas/AI Cyberforge integration
add or dilute this segment's margin once fully consolidated for a full
year?

**Vertical 2: Consolidated EBITDA margin trend.**
What the corpus establishes: FY26 full-year EBITDA margin 23.2%
(comparable-quarter read), rising to 26.2% in Q1 FY27 (B05). What it
cannot establish cleanly: Verifier B found management itself described
the Q1 FY27 print as partly a mix artefact of temporarily lower low-margin
token sales, with a sustainable guide closer to 25%, a caveat B05's
original draft missed (B12b MAJOR finding). Questions that decide it: (1)
Does the margin hold above roughly 25% once token/DSC volumes normalise,
expected "mostly by September" per the Q1 FY27 call? (2) Is the FY26 to
FY27 margin trend driven by the same mix shift as Vertical 1, or by a
separate cost lever?

**Vertical 3: Organic growth ex-M&A versus the FY27 guide.**
What the corpus establishes: whole-company organic growth ran near 15% in
Q1 FY27 against total income growth of 28% (about 13 points from
Cryptas), while the FY27 organic guide itself narrowed from a 15 to 18%
band toward "most likely 18%" (Q4 FY26 call) to a flat 18% restated (Q1
FY27 call), and PAT guidance narrowed from a 25 to 30% band to a flat 25%
(B01, B05). What it cannot establish: the organic-versus-acquired split is
disclosed only at the Enterprise Solutions segment level in the AR (+55%
total, +23 pts organic / +32 pts inorganic), not at the whole-company
level that the guide is framed against (B04). Questions that decide it:
(1) Does Q2/Q3 FY27 organic growth move back toward 18% as the token
transition normalises, or hold near 15%? (2) Is the segment-level organic
split reconcilable with the whole-company figure management cites on
calls?

**Vertical 4: Free cash flow.**
What the corpus establishes: FY26 FCF turned negative for the first time,
Rs -52.52 Cr, on capex nearly doubling while CFO grew 30.8%; CFO stayed
above PAT both years (B01, B03). What it cannot establish: whether FY26's
capex level (data-centre build, new-product capitalisation, and
acquisition payments) recurs in FY27 or was a one-time step-up; management
was not asked this directly in any of the three calls read. Questions
that decide it: (1) Does FY27 FCF return positive? (2) Does the
unbilled-revenue and payables growth flagged in B02 Pattern A (both
outrunning revenue growth) persist or normalise alongside the capex
story?

### 4b. Candidate signal table

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| CCA (Controller of Certifying Authorities, MeitY) licensing/model changes | A licence-fee or model change filed, repeating the July-2024 pattern, with no compensating Trust Services price pass-through disclosed within 2 quarters | Event-driven | MeitY / CCA government portal |
| CA/Browser Forum and browser root-store vendors (Chrome, Microsoft, Mozilla, Apple) | A qualified WebTrust audit opinion, or a browser-vendor distrust/removal notice naming eMudhra roots | Event-driven | CA/Browser Forum public records; browser-vendor security blogs |
| UAE Telecommunications and Digital Government Regulatory Authority (TDRA) | QTSP licence not granted by Q3 FY27 with no new firm date given (B05 kill signal already once triggered) | Event-driven | TDRA government portal |
| EU NIS2/DORA regulatory implementation (ENISA, national regulators) | ENISA or a national regulator delays or narrows implementation scope in a way that removes the cited demand driver for Cryptas/PrimeSign | Quarterly | ENISA / EU Official Journal publications |
| Large India public-sector/BFSI customers and the InCommon US consortium | No named large order win disclosed for 2 or more consecutive quarters despite guided growth | Event-driven | Customer/counterparty public procurement disclosures, press releases |
| Gartner / IDC global cybersecurity and PKI-as-a-Service spend trackers | Published forecast growth revised materially below the roughly 20-21% rate this run's TAM triangulation found | Quarterly | Gartner/IDC published forecast updates (press-release summaries) |
| Named global PKI/IAM competitors (DigiCert, Keyfactor, Venafi/CyberArk, Entrust) | A competitor discloses aggressive India/APAC pricing, or a named direct-competitive loss against eMudhra | Event-driven | Company press releases; private-company revenue aggregators (Owler/Craft) |

These are UNVERIFIED. Verification and Role 5.5 tracker writes happen in
claude.ai, unchanged.

### 4c. Fragility read

- **variable_count**: 5. Outside-India segment margin narrowing;
  consolidated EBITDA margin holding above roughly 25%; organic growth
  closing toward the 15 to 18% guide; FCF returning positive; Cryptas
  cross-sell converting to profitability without the contingent
  consideration crystallising toward its uncapped upside.
- **verifiability_ratio**: 3 of 5 externally observable through filed
  financial statements (segment margin via Note 49, EBITDA margin via
  results filings, FCF via the cash flow statement). 2 of 5 are
  company-narrated only at present (the whole-company organic-versus-
  acquired split, and Cryptas's own EBITDA trajectory versus the
  contingent-consideration target).
- **single_point_failure**: Outside-India Enterprise Solutions segment
  operating margin (Note 49). This is the literal proof gate named in Part
  B3. If it does not narrow, the transition engine described in Part B2
  has no remaining mechanism, independent of how the other four variables
  perform.
- **fragility_verdict**: MODERATE. Three of five variables are externally
  verifiable from filed statements, which argues against FRAGILE, but one
  named single point of failure exists and the one year of evidence
  available on it moved the wrong way, which argues against ROBUST.

### 4d. Research brief

Numbered live-web work items for claude.ai. Items 1 and 2 are the
PENDING LIVE VERIFICATION links raised by the Section 4e chains below.

1. Confirm whether any named international enterprise or government
   customer wins were disclosed via Reg 30 filing or press release in H2
   FY27, to test whether the overseas headcount build (Vertical 1, Chain
   1) is tracking against a real, dated pipeline.
2. Confirm the named counterparties and any disclosed deal value behind
   eMudhra's 2 named FY27 Cryptas cross-sell wins, via FY27 Reg 30 filings
   and Q2/Q3 FY27 concall transcripts (not yet in this corpus) (Chain 2).
3. Fetch the ICRA rating rationale for the 29-Jun-2026 reaffirmation
   directly from icra.in (blocked to this container's scripted retrieval)
   to close the freshness-pair gap named in Section 1.
4. Verify the exact ownership chain and timing of Executive Chairman V.
   Srinivasan's personal investment connection to Capital MXT, the entity
   that acquired a 5% stake in 3i Infotech, the company alleging fraud
   against him (B05 MAJOR flag, disclosed only under direct questioning,
   never volunteered).
5. Check whether 3i Infotech has filed a SEBI complaint or civil suit
   since the EOW's 13-Aug-2026 civil-not-criminal closure (media-reported,
   unconfirmed as of this run, B08).
6. Source 3i Infotech's own complaint text and its 10-Feb-2026 response
   letter (unreadable, encoded PDF, in this run's corpus) to read the
   dispute from both sides, not eMudhra's filings alone (B08 input gap).
7. Independently verify eMudhra's claimed leadership in the Indian
   certifying-authority space against named competitors (Capricorn,
   Verasys, PentaSign); this run's peer set could not corroborate it,
   no PKI/CA-listed peer exists (B06 UNVERIFIABLE item).
8. Check whether India's DSC/token industry saw a broad volume hit from
   the FIPS 140-3 recertification transition into September 2026,
   industry-wide or eMudhra-specific (B06 UNVERIFIABLE item, ties to
   Vertical 3's Q1 FY27 organic dip).
9. Attempt to resolve the exact per-holder promoter/promoter-group
   shareholding percentages (three of five figures unreadable in both text
   layers of the AR, p.247/339); may require the AR page image or the BSE
   shareholding-pattern PDF directly (B08 input gap).
10. Pull the FII/DII institutional-ownership split from BSE's
    shareholding-pattern detail pages; not present in the AR text or the
    two Reg 31 summaries held, screener-only and non-anchored in this run
    (B00, B03).

### 4e. Second-order stub (Master Prompt v3.7, Rule F)

Stub carries 2 of the Rule F floor of 5. Drafted from the two dominant
variables (Section 2, Part C1) the evidence base can actually carry.

```
CHAIN 1: Outside-India Enterprise Solutions segment operating margin
compressed from 26.0% (FY25) to 21.9% (FY26) even as segment revenue grew
38.3% to Rs 4,375.72 Mn (Note 49, AR p.288; B04).
Link 1 [DOCUMENTED]: Consolidated employee cost rose from 17.6% to 19.46%
of revenue in FY26, attributed in the MD&A to "addition of senior
management resources in overseas geographies" (AR p.152; B04).
Link 2 [DOCUMENTED]: The India Enterprise Solutions segment, largely the
same product set, ran at 57.5% margin FY26 (up from 51.1% FY25), so the
destination economics already exist domestically, not internationally
(Note 49, AR p.288; B04).
Link 3 [INFERENCE]: If the overseas headcount additions are front-loaded,
new senior hires added ahead of the revenue they are meant to win, the
margin dip reads as a lag effect that should narrow as FY26-vintage hires
reach full productivity in FY27-28, consistent with a typical 12 to 24
month sales-cycle ramp for enterprise software sold by newly built
regional teams. This is not disclosed as management's own explanation; it
is the most evidenced reading available from the cost-line and segment
data alone.
Binding constraint: who pays, and why now, for the international pipeline
this cost base is meant to serve is not stated in any corpus document
read. PENDING LIVE VERIFICATION for claude.ai: check eMudhra's Reg 30
filings and press-release page for named international order wins in H2
FY27, to test whether a real, dated pipeline sits behind the cost build.
Unsaid: the AR MD&A frames the whole cost rise as senior-management
addition and never states an international headcount number, a
revenue-per-hire ratio, or any timeline for margin convergence anywhere
in the corpus (B04 gap).
Observation that confirms or breaks this chain, and confirm-by date: the
FY27 AR's Note 49 (or an interim segment disclosure, if given) shows
Outside-India Enterprise Solutions margin at or meaningfully above the
FY26 print, narrowing toward the India band. Confirm-by: FY27 AR
publication, expected on this year's cadence around May 2027 (this year's
AR was signed 6-May-2026).

CHAIN 2: Cryptas contingent consideration (Rs 881.45 Mn, uncapped on the
EBITDA upside, Note 17a/47/48, priced on a 10x-FY26-EBITDA mechanic;
B02) is meant to be converted into value by cross-selling Cryptas
products into eMudhra's existing accounts; management names 2 such wins
in FY27 (B07 optionality register).
Link 1 [DOCUMENTED]: Cryptas's own profitability narrative drifted across
three consecutive calls, positive PAT (Q3 FY26), to almost breakeven
(Q4 FY26), to "not profitable at all" describing the same broad period
(Q1 FY27), alongside a fresh roughly Rs 4 Cr Q1 FY27 loss in the entity
housing Cryptas, never reconciled by management (B05 MAJOR flag).
Link 2 [DOCUMENTED]: The group's own smaller prior acquisition, Two95
International, already shows a partial earn-out miss this year, sellers
did not meet performance conditions, Rs 13.01 Mn of upside-bonus liability
reversed (Note 53(a); B02 finding 12), a disclosed, company-specific base
rate for handicapping the larger, untested Cryptas earn-out.
Link 3 [INFERENCE]: If Cryptas is currently loss-making while the
contingent-consideration liability is fixed to a 10x-EBITDA formula with
no ceiling, the near-term arithmetic favours eMudhra, a lower EBITDA base
means a lower eventual payout, but it also means the cross-sell narrative
management uses to justify the deal has not yet shown up in Cryptas's own
numbers. The 2 named wins are revenue events, not yet disclosed as
profitability events; the gap between a revenue win and an
EBITDA-accretive one is what decides whether the liability ever grows
toward its uncapped upside or stays anchored near its floor.
Binding constraint: who pays, and why now, for the 2 named FY27 Cryptas
cross-sell wins, meaning the counterparties and any disclosed deal value,
is not stated in any corpus document read. PENDING LIVE VERIFICATION for
claude.ai: check eMudhra's FY27 Reg 30 filings and the Q2/Q3 FY27 concall
transcripts (not yet held in this corpus) for named customers and deal
value behind these wins.
Unsaid: no corpus document discloses a discount rate, an EBITDA
growth-rate assumption, or a scenario probability for the Level 3
fair-value estimate behind the Rs 881.45 Mn liability (Note 47/48; B02
finding 5), the single biggest judgment call behind a number that could
grow or shrink materially.
Observation that confirms or breaks this chain, and confirm-by date: any
FY27 quarterly result or the FY27 AR disclosing Cryptas actual EBITDA
against the implicit 10x contingent-consideration target (B03
monitorable), or a change in the Note 17a liability balance ahead of
disclosed Cryptas performance. Confirm-by: each FY27 quarterly result,
first opportunity the Q2 FY27 results, expected around November 2026.
```

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in
claude.ai with live web, before Role 2.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. eMudhra runs two businesses. One issues government-licensed digital
   signatures in India. The other sells owned identity and security
   software to enterprises worldwide.
2. The software business is 59% of FY26 revenue. The licensed-signature
   business is 20%. A smaller consulting arm is 21%.
3. The software business grew fast in FY26, helped by two acquisitions,
   Cryptas in Europe and AI Cyberforge in the US, both added from
   1-Jul-2025.
4. Trust Services customers are mostly Indian individuals and small firms,
   reached through partner agents who take a large commission.
5. Enterprise Solutions customers are named enterprises and governments,
   in India, the US, Europe, and the Middle East, with long buying cycles
   and real switching costs once a company's PKI or signing workflow is
   wired in.
6. 67% of FY26 revenue came from existing customers, a sign the switching
   costs are real, though no specific customer-concentration number is
   disclosed anywhere in the concalls read.
7. Demand grows on two forces: regulatory mandates in India (KYC,
   e-signature rules) and abroad (EU digital-trust rules, India's new
   data-protection law), plus a broad rise in enterprise cybersecurity
   spend that eMudhra cites but does not size for its own niche.
8. A UAE licence needed for Middle East expansion has already slipped once
   and is not yet granted.
9. The licensed-signature business has a real but narrow moat: only 24
   Indian firms hold the licence eMudhra holds.
10. The software business's moat is weaker where it matters most right
    now: the international slice of that business earns less than half
    the margin of the same business sold in India, and the gap widened
    this year, not narrowed.
11. The mental model here is a bet that this margin gap closes as
    overseas hiring matures into revenue. That bet has not yet been proven
    by one full year of segment evidence; the gap moved the wrong way in
    FY26.
12. The fragility read on this bet is MODERATE: three of the five things
    that must go right can be checked in filed financial statements, two
    depend on management's own account of events.
13. The corpus could not establish the exact per-holder promoter
    shareholding split, the FII and DII ownership split, or a segment-level
    capital-employed and debt breakdown; none of these are in the readable
    text of this year's annual report.
14. The corpus could not establish whether the current FY26 capex and
    cash-flow dip is a one-time step, or something that recurs in FY27;
    management was not asked this directly on any call read.
15. The two biggest open questions are whether the international margin
    gap is a hiring lag or a structural feature of selling this product
    abroad, and whether the 3i Infotech legal matter, closed as civil by
    the police in August 2026, stays closed given the Executive Chairman's
    disclosed personal connection to the company's new 5% shareholder.

---

## SECTION 6: STANDING EXTRACTION ANNEX

Ten standing questions, answered from corpus in quote-then-comment form.
Filename and page anchor on every number.

### 1. Units

**Trust Services, DSC unit.** "~Rs 1,500 for a 2-year DSC" (as extracted
from Q4FY26 Investor Presentation slide 8, reused from 04-bizmodel.md
Section 4B; the presentation's own printed wording was not independently
re-read this pass; the figure and page anchor are carried from the stage
report). Comment: covers one product (a single 2-year-validity Digital
Signature Certificate), not a basket; CA-partner commission of 45 to 50%
is taken where the roughly 70% partner channel is used.

**Enterprise Solutions, per-account ACV.** NOT FOUND. No per-account
average contract value is printed anywhere in the AR, results filings, or
investor presentations read. The volume and revenue lines it could be
derived from: Enterprise Solutions segment revenue Rs 5,615.72 Mn FY26
(India Rs 1,240.00 Mn + Outside India Rs 4,375.72 Mn, Note 49, AR p.288),
against 240 new enterprise customers added in FY26 (MD&A, AR p.148/151),
undisclosed base customer count, so no clean per-account figure can be
derived from these two lines alone.

**SecurePass deal size.** "Rs 4-6 Cr per large bank/government entity, Rs
10 Cr+ for full PIM/PAM suite" (Q1 FY27 call, per B05 guidance table).
Comment: a disclosed deal-size range, not a per-unit realisation; covers
one product line only (SecurePass/IAM), stated as ongoing guidance, not
tied to one quarter.

### 2. Segment capital and debt

Ind AS 108 Note 49 (AR p.288) discloses segment revenue and segment
operating result (margin) for the two reportable segments, Trust Services
and Enterprise Solutions. **No segment assets, segment liabilities, or
segment capital-employed table was located** in either text-extraction
layer of the AR by any stage that read Note 49 (B03, B04). This may sit
in a portion of Note 49 or its surrounding pages (AR pp.286-289) that both
text layers rendered with column-scrambling (B02, B03 both flag pp.286-289
as partially scrambled); a raster or Claude web check of these pages is
recommended before relying on this absence.

Borrowings are **not allocated by segment** in the disclosed notes.
Consolidated borrowings, non-current Rs 129.88 Mn plus current Rs 108.85
Mn, total Rs 238.73 Mn (B03 balance-sheet table), reconcile exactly to
four named entity-level facilities in Note 16 (per 02-notes-pass1.md):
term loan, PrimeSign GmbH, Rs 69.27 Mn (incl. Rs 11.55 Mn current), 3.245%
p.a.; term loan, Cryptas IT Security GmbH, Rs 86.59 Mn (incl. Rs 14.43 Mn
current), 3.245% p.a.; related-party loan from Taarav Pte Ltd, Rs 45.15
Mn, 8% p.a., unsecured, repayable on demand; related-party loan from
Executive Chairman V. Srinivasan, Rs 37.72 Mn, interest-free, unsecured,
repayable on demand. All four facilities sit inside the newly acquired
Cryptas-linked entities (the two term loans) or fund those entities (the
two related-party loans); none is India-domiciled bank debt.

### 3. Guidance versus aspiration

| Claim | Class | Quote / figure | Period stated | Source |
|---|---|---|---|---|
| FY27 organic revenue growth | (a) Guidance, period stated | "15-18%," later restated "organic 18%" | FY27 | Q4 FY26 call; restated Q1 FY27 call (B05) |
| FY27 PAT growth | (a) Guidance, period stated | "25-30%, most likely 27-28%," later narrowed to "flat 25%" | FY27 | Q4 FY26 call; restated Q1 FY27 call (B05) |
| PAT doubling | (a) Guidance, period stated | "2x PAT over 3 years" | FY27-FY29 | Q4 FY26 call, reaffirmed Q1 FY27 call (B05) |
| UAE QTSP licence completion | (a) Guidance, period stated (slipped once) | "end of this quarter to beginning of next" | ~Sep-Oct 2026 | Q1 FY27 call (B05) |
| Token/DSC recertification normalisation | (a) Guidance, period stated | "mostly by September" | Q2 FY27 | Q1 FY27 call (B05) |
| R&D intensity versus global peers | (b) Aspiration, no period | "7-8% of revenue vs 15-20% for global peers" | none stated | Q4FY26 Inv. Pres. p.24 (B07) |
| 65% recurring revenue | (c) Capacity/capability only | "65% of total company revenue is described as recurring" | not forward-looking | Q4FY26 Inv. Pres. slide 5 (04-bizmodel.md) |
| SecurePass typical deal size | (c) Capacity/capability only | "Rs 4-6 Cr / Rs 10 Cr+" | ongoing, not a forward commitment | Q1 FY27 call (B05) |
| ROE target level | (c) Capacity/capability only, framed as a ceiling not a target | "~14.5-15%, framed as close to a maintainable ceiling" | ongoing | Q1 FY27 call (B05) |

### 4. Concentration

**Customer concentration.** NOT DISCLOSED. "No customer-concentration
disclosure in any of the three calls" (B05 flag, verbatim finding).

**Product concentration.** Enterprise Solutions 59% of FY26 revenue,
Trust Services 20%, Services 21% (AR p.55, "By line of business"; consol
Rs 1,400.08 Mn Trust Services of Rs 7,015.80 Mn total, Note 49, AR p.288;
per 04-bizmodel.md). Comment: this is the top-line product mix, not a
top-product-share-of-one-segment figure; no single named product's
revenue share is separately disclosed.

**Geography concentration.** Anchored to the AR: Enterprise Solutions
India Rs 1,240.00 Mn versus Outside India Rs 4,375.72 Mn of the segment's
Rs 5,615.72 Mn total (Note 49, AR p.288), roughly 78% of this segment
sold outside India. The whole-company "64% international" figure, and its
regional breakdown (North America 34%, Europe 12%, Middle East and Africa
11%, APAC 7%, India 36%), is company memory sourced from a third-party
concall summary site (inve.money), not independently re-verified against
the AR text this pass; flagged as company memory, to weigh not cite, per
task instructions.

### 5. Promise ledger

| Promised in | Promise | Outcome | Evidence anchor |
|---|---|---|---|
| Q3 FY26 call | FY26 total revenue Rs 700 Cr | Delivered | Actual Rs 713.2 Cr per Q4 FY26 call |
| Q3 FY26 call | FY26 Trust Services growth 22-25% | Delivered, with caveat | Actual 32%, partly channel stocking ahead of the FIPS 140-3 deadline that reversed into the Q1 FY27 decline |
| Q3 FY26 call | Adjusted EBITDA margin ~25.8% sustained | Partial | FY26 full-year adjusted margin 25.7% close to claim, but reported (non-adjusted) margin fell to 22.4% in Q4 FY26 from 23.1% in Q3 FY26 |
| Referenced Q3 FY26 call | 5-6 major US customers signed, revenue to follow | Partial | Customers retained, one customer's revenue shifted Q3 to Q4 FY26 on usage-based recognition timing |
| Q3 FY26 call | UAE data centre commissioning after a 2-3 month audit (~Apr-Jun 2026) | Missed | QTSP licence still pending as of Q1 FY27 call, now targeted ~Sep-Oct 2026; DC infrastructure itself confirmed operating Q4 FY26 |
| Q3 FY26 call | Stock-in-trade cost drag (~Rs 3 Cr/quarter) to normalise in 1-2 quarters | Missed | Never revisited or confirmed resolved in Q4 FY26 or Q1 FY27 calls |
| Q4 FY26 call | FY27 organic revenue growth 18% | Partial | Q1 FY27 print: total income +28%, ~13 points from Cryptas, company-wide organic ~15%; product-segment organic framed separately at ~25% |
| Q4 FY26 call | FY27 PAT growth 25-30%, most likely 27-28% | Delivered | Q1 FY27 PAT +27.9% YoY, though spoken guide language later narrowed to a flat 25% |

Delivered 3, partial 3, missed 2 (B05). Credibility grade: **C**, re-rated
down from an original B by Verifier B on the promise-ledger balance and
two management-credibility findings outside the ledger itself (the
unreconciled Cryptas profitability narrative and the Capital MXT
connection); see Section 2 Part B5 and B08 (B05, B12b).

### 6. Restated bases

"restatements_found: []" (B02, verbatim field). No restated comparatives
were found for any reorganisation, transfer, or reclassification. Prior
period comparatives in the FY26 AR are stated on a like-for-like basis.
Comment: this stage's own internal Gate 0 ROCE re-computation (B01
Correction 2, moving from a mixed computed/AR-disclosed basis to a single
consistent computed basis across all 8 years) is a pipeline analysis
methodology fix, not a company restatement of filed comparatives.

### 7. Corporate-action clauses

Two acquisitions completed this year, both consolidated 1-Jul-2025 (Note
4a(c), 4a(d), AR p.243, per B02/B03):
- **Cryptas International GmbH** (Europe, PKI/digital trust). Purchase
  price landed almost entirely in goodwill (net identifiable assets
  approximately nil, Rs 1,315.25 Mn to goodwill, B02 finding 3).
  Contingent consideration: fair value EUR 7.95 Mn at acquisition, EUR
  9.18 Mn undiscounted at 31-Mar-2026 (Rs 932.11 Mn per the report; Rs
  881.45 Mn is the Note 17a non-current balance-sheet carrying figure),
  on a 10x-FY26-EBITDA mechanic, no ceiling disclosed. A separate 49%
  stake put/call option runs 2028-2030 on the same 10x-EBITDA basis,
  floored at 1x trailing revenue on the downside (Note 4a(c), 17a, 53(b),
  AR p.243/255/290-291).
- **AI Cyberforge Inc.** (US, key and secrets management), also
  consolidated 1-Jul-2025 (Note 4a(d), AR p.243). No contingent-
  consideration mechanic comparable to Cryptas's is described in the
  blocks read for this entity.

No demerger, merger, or buyback exists in this corpus.

**Board change via Postal Ballot**, effective 1-Apr-2026 (just after FY26
year-end): two promoter-family members, Kaushik Srinivasan and Arvind
Srinivasan, added to the board, expanding it from 7 to 9 members and the
executive/promoter-family count from 2-of-7 to 4-of-9 (B03, B08 Postal
Ballot notice, inputs/announcements/20260209-a7e3e2bf).

### 8. Related-party perimeter

Full FY26 related-party universe, Note 44 (AR p.267-271), reused from
02-notes-pass1.md's assembled table:

| Nature | Counterparty | FY26 (Rs Mn) | FY25 (Rs Mn) |
|---|---|---|---|
| Sales of products/services | Bluesky Infotech (promoter-influenced partnership) + others | 57.28 | 21.00 |
| Software licensing fee received (parent-level) | eMudhra Consumer Services, eMudhra INC, eMudhra BV, eMudhra DMCC, PT Indonesia, Smart Craft | ~169.9 combined | ~79.8 combined |
| Purchase of products/services | Bluesky Infotech, Smart Craft | 164.72 + 6.34 | 88.64 + 3.62 |
| Commission paid | Bluesky Infotech | 11.56 | 6.00 |
| Rental income | eMudhra Technologies, eMudhra Consumer Services, Lifeuno | 0.60+12.00+0.30 | 0.60+12.00 |
| Borrowings taken from related parties/director (new this year) | Taarav PTE Ltd to eMudhra DMCC | 23.57 | 0 |
| Borrowings taken from related parties (new) | Taarav PTE Ltd to eMudhra PTE | 21.58 | 0 |
| Borrowing from director, interest-free | V. Srinivasan to eMudhra DMCC | 37.72 | 0 |
| Dividend paid to promoters/KMP | V. Srinivasan, Mythili Srinivasan, Taarav PTE, Kaushik Srinivasan, Lakshmi Kaushik, Arvind Srinivasan | 17.97+15.94+17.30+1.16+7.12+3.94 | broadly similar |
| Investment by parent into subsidiaries | eMudhra INC, eMudhra PTE, eMudhra BV | 480.49 combined | 851.45 (mostly eMudhra INC) |

Related-party receivables grew from Rs 4.91 Mn to Rs 68.18 Mn (13.9x),
related-party payables from Rs 1.89 Mn to Rs 104.01 Mn (~55x), both
concentrated in Bluesky Infotech (Note 10 AR p.249, Note 44.2 AR p.269).
Related-party sales are 0.8% of revenue, immaterial in size (02-notes-pass1.md).
Directors' commission: 1% of parent net profit to non-executive directors,
within the Section 198 limit (Note 44.1, AR p.267-268).

### 9. Pledge and shareholding

**Pledge.** "0%" for the two quarters directly verified: BSE Reg 31
summaries dated 31-Mar-2026 and 30-Jun-2026 both answer "No" to
pledge/NDU/other-encumbrance questions (B08). Comment: full 12-quarter
(3-year) direct verification is NOT DISCLOSED in this run's inputs; only
2 quarterly BSE files were held (see Section 1 gaps). Company memory
(screener, non-anchored) reports no pledge historically, consistent but
not independently confirmed for the missing 10 quarters.

**Promoter holding.** 54.40% (both the Mar-2026 and Jun-2026 BSE Reg 31
summaries, per B00/B08), flat over the two quarters directly held. The
per-holder AR shareholding table (consol p.247/252, standalone p.339)
is scrambled in both text-extraction layers beyond confident row
reconstruction; two names anchor cleanly (V Srinivasan 17.36%, Taarav Pte
Ltd 15.40%), three remaining values (16.72%/3.81%/1.12%) sum correctly to
54.40% with the first two but could not be mapped to the three remaining
named holders (Mythili Srinivasan, Arvind Srinivasan, Kaushik Srinivasan)
(B08).

**Institutional holding.** FII 3.92%, DII 10.55% at Jun-2026 (screener,
non-anchored; NOT FOUND in the AR text or either BSE Reg 31 summary held,
per B00/B03/B08).

### 10. Verification

Documents quoted in this annex, filename and date:
- Annual_Report_2026.pdf (and its .mupdf.txt / raster layers), FY2025-26
  Annual Report, signed 6-May-2026.
- FY26-Q3_Results_31Dec2025.pdf, results filing, quarter ended 31-Dec-2025.
- FY26_Audited_Results_31Mar2026.pdf, audited annual results, year ended
  31-Mar-2026.
- FY27-Q1_Results_30Jun2026.pdf, results filing, quarter ended 30-Jun-2026.
- Concall_Feb_2026_Q3FY26_Transcript.pdf, earnings call, 03-Feb-2026.
- Concall_May_2026_Transcript.pdf, earnings call, 07-May-2026.
- Concall_Aug_2026_Transcript.pdf, earnings call, 30-Jul-2026.
- 20260507_Investor_Presentation_Q4FY26.pdf, investor presentation,
  07-May-2026.
- 20260730_Investor_Presentation_Q1FY27.pdf, investor presentation,
  30-Jul-2026.
- inputs/announcements/20260204-d507034d.pdf, Reg 30 clarification letter,
  04-Feb-2026.
- inputs/announcements/20260209-a7e3e2bf.pdf, Postal Ballot notice,
  09-Feb-2026.
- inputs/announcements/20260209-3i-Infotech-Investor-Call-Transcript.pdf,
  special investor call, 06-Feb-2026.
- inputs/announcements/20260818-7509d90d.pdf, EOW civil-closure letter,
  18-Aug-2026.
- inputs/rating/20260629_Credit_Rating_Intimation.pdf, ICRA reaffirmation
  letter, 29-Jun-2026.
- inputs/rating/20250602_ICRA_Rationale_Upgrade_A_Stable.pdf, ICRA full
  rationale, 02-Jun-2025.
- BSE-SHP-summary-Mar2026.txt and BSE-SHP-summary-Jun2026.txt, BSE Reg 31
  shareholding pattern summaries.

**CORPUS COMMIT HASH: 15e51891e556b28bc70dece85bc4ed6b162948c2**
