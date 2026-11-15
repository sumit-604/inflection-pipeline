MISSING MATE DOCUMENT: Q2 FY27 earnings call transcript (call held 2026-11-13; the Q2 FY27 results filing of 2026-11-12 is in the corpus, its mate is not). Expected source: BSE corporate announcements for scrip 532493, or the screener documents page for ASTRAMICRO.

VERDICT: PROCEED WITH CAVEATS

# ASTRAMICRO (Astra Microwave Products Ltd): FTTCP gate recommendation, run 2026-11-15

Mode: Phase 1 lite. This is the go/no-go into FTTCP deliberation on evidence alone. Stages 10 and 11, the FTTCP deliberation and the valuation half of Verifier C have not run. The Mental Model Declaration is unsigned, and the Halt 1 decision is the operator's.

## Verdict block

Verdict: PROCEED WITH CAVEATS. Selection rule that fired: rule 3 (FLAG-CASH active with determination INDETERMINATE, which caps at PROCEED WITH CAVEATS). The freshness cap binds at the same level.

How each rule was tested, in order:

1. REWORK: not fired. Verifier A logged 0 CRITICAL rows. Acceptance rates are A 97.3, B 91.7 as emitted, C phase 1 87.0 and D 100. No rate sits below 60 on a denominator of 4 or more. Overall confidence is 87.0. Verifier A marked six MINOR rows source_fidelity true. All six are page anchor slips: every value exists at the corrected page that Verifier A gives, and this file and the narrative use those corrected pages. No source fidelity MISMATCH touches a Gate 0 input or a sector cap row input. The Verifier A MAJOR (HAL order value gap) is an arithmetic slip with source_fidelity false. The correct gap is 0.53%, not about 1.2%, so the two HAL figures reconcile within rounding on an 18% tax basis.
2. INSUFFICIENT EVIDENCE: not fired. Stages 2 and 3 ran on the FY26 annual report. Gate 0 ran on the screener Data Sheet and three results filings (Q4 FY26, Q1 FY27, Q2 FY27). The named gaps below leave the record intact for a go/no-go into deliberation. Each gap caps the verdict at CAVEATS, and each is named with its source.
3. FLAG-PROMOTER is not active, because stage 8 returned CAUTION and the flag fires on CONCERN or AVOID only. FLAG-CASH is active with determination INDETERMINATE. INDETERMINATE never resolves to PROCEED. It caps at PROCEED WITH CAVEATS, and the missing evidence is named in the FLAG-CASH block.
4. Freshness cap (binding): the intake verdict is CORPUS GAPPED-FRESHNESS. Freshness pair 1 (results to concall) FAILS on the missing Q2 FY27 transcript. The verdict caps at PROCEED WITH CAVEATS whatever the flag count.
5. Rule 4 would land at the same level on its own: the verifiers logged 6 MAJORs worth carrying (Verifier A 1, Verifier B 4, Verifier C 1).

Stages 8 and 9 ran PARTIAL. Both are search stages on questions that matter for the decision, and the gaps are named here.

- Stage 8 (promoter check), searches skipped: MCA and RoC director network and strike off check for promoter group entities (no MCA access); eCourts, NCLT, SAT, NGT, CCI and consumer forum searches by name; SCORES complaint history; IiAS, SES and InGovern reports on the 2026 AGM (not public); the original BSE or NSE text of the SEBI inquiry disclosure and of the 2026 warrant allotment filing; a 12 quarter pledge history; two SEBI result URLs found but not opened (feb-2024 1708514961658.pdf and apr-2023 1682679608810_1.pdf); individual name checks on Renuka Chitrakar, Dr M.V. Reddy, Anuradha Mookerjee, Avinash Chander, Rahul Rungta and Srinivasarao Devathi; a separate reputation check on Rafael Advanced Defense Systems; the ownership link between Strategic Ventures Limited (1.76% holder) and the Kabra linked Strategic Ventures Fund (Mauritius); Glassdoor (only AmbitionBox found). The biggest open question in this list is the identity check on the 2010 SEBI order against a Suresh Kumar Somani.
- Stage 9 (market sizing), searches skipped or failed: the Bain defence electronics report (the link returned the Bain homepage, so the figure is unverified and unused); the MarketsandMarkets military radar page (HTTP 403, so snippet figures carry a STALE flag); IBEF, CRISIL, ICRA and Mordor sector pages (not fetched); the rupee rate for November 2026 (the latest sourced rate is 94.68 on 22 Jun 2026); a named competitor list and top 3 concentration (no source found). The serviceable market figure therefore rests on management's own programme pool.

Missing evidence named for the cash determination: the Q2 FY27 call transcript (management's explanation of the H1 outflow and inventory build); the Uttam advance and payment terms; ARC credit terms and receivable ageing; the receivable ageing basis (invoice date or due date) and a 30 Sep 2026 ageing; the share of inventory that is legacy stock and its provision; capex and trade payables history for FY17 to FY24.

## Transition posture

POSTURE: NOT CLASSIFIED. The matrix reads three state variables from the signed model, and none is set yet. The proof gate needs the FTTCP transition read. The ugliness class needs Part B5 of the signed model. The recognition gap needs stage 11.

What each variable will draw on:
- Proof gate: the HAL Uttam order is booked, but Phase 1 delivery (12 units by Sep 2027) and a disclosed margin and advance have not happened.
- Ugliness: the ugly optic is cash conversion. CRISIL calls the working capital requirement a product of long gestation, tests and third party inspection, and expects 420 to 440 days of gross current assets.
- Recognition gap: stage 11 has not run.

[INFERENCE] The cash record makes STRUCTURAL FEATURE a live candidate for Part B5. If the signed model lands there with the proof gate not fired, the matrix gives VALUE-TRAP RISK. The operator should test that cell first at Halt 1. The observation that separates it from RESEARCH / WATCH is the FY27 year end standalone CFO and inventory.

## Phase 1 confidence delta

| Component | Value | Source | Basis |
|---|---|---|---|
| numerical_acceptance | 97.3 | B12a | 692 numbers checked; mandatory tier 234 of 234; 0 CRITICAL, 1 MAJOR, 6 MINOR |
| redflag_coverage | 91.7 | B12b | material 12, caught 11 (7 caught + 4 partially caught); caught only reading 58.3, reported by the verifier, not applied |
| framework_adherence (phase 1 portion) | 87.0 | B12c | Gate 0 + Emerging Moat: 40 of 46 rules; valuation component PENDING PHASE 3 |
| peer_utilisation | NOT APPLICABLE | B12d | 2 of 2 peers used substantively (denominator below 4); B12d acceptance 100 reported as a count |
| overall | 87.0 | confidence.yaml | set by framework_adherence phase 1 portion; band 75 to 89, normal, note specifics |

Weakest component: framework adherence at 87.0 sets the overall. On the verifier's own sensitivity, red flag coverage is the softest: it reads 58.3 if only fully caught items count.

## Flag blocks

### FLAG-CASH: ACTIVE. Determination: INDETERMINATE

Two readings:
- STRUCTURAL: high working capital is part of the business model, and conversion stays weak through the Uttam ramp.
- GROWTH-INDUCED: the H1 FY27 build is inventory for a back loaded H2 and the Uttam ramp, and it releases by year end as FY26 did.

Most evidenced path: high working capital is a permanent feature of the model. CRISIL guides gross current assets of 420 to 440 days, so no further fall. The record does not yet prove whether conversion gets worse with Uttam. The separating observation is the FY27 year end standalone CFO and the 31 Mar 2027 inventory against Rs 793 Cr.

Evidence for the STRUCTURAL reading:
- Ten year cumulative CFO/PAT is 0.47 (B01, deal breaker DB4). CFO was negative in FY23 (-25.47), FY24 (-181.52) and FY25 (-90.15) Rs Cr consolidated (B01; screener Data Sheet). Receivables went from 283.65 to 786.13 Rs Cr and inventory from 419.06 to 615.94 Rs Cr between FY23 and FY25 (B01; screener Data Sheet).
- FY26 standalone CFO was 37,595.92 Rs Lakhs, and 13,324.69 of it (35.4%) was a working capital release (B02 rank 5; AR FY26 CFS p.209). Payable days were 72 against 38 (B03; BRSR p.134). A 16,000.00 Rs Lakhs year end deposit sits inside cash: net debt to equity is 10% with it and 21.9% without it (B02 rank 7; AR Note 10(a) p.233, Note 14 p.236).
- H1 FY27 standalone CFO was -14,612.63 Rs Lakhs (consolidated -14,784.83). Inventory was Rs 793 Cr against Rs 609 Cr, and current borrowings were Rs 411 Cr against Rs 224 Cr (B04, B05; investor presentation pp.11-12). The Q4 FY26 call said the CFO trend would be maintained (B05 promise row, outcome missed).
- Receivables more than two years past due were 8,158.33 against 4,591.91 Rs Lakhs, and ECL cover on that bucket fell to 14.9% from 19.6%. The ageing schedule does not roll forward (B02 ranks 3 and 4; AR Notes 39, 44, pp.255-256, 263).
- The ARC receivable is 19,579.28 Rs Lakhs (27.9% of current gross), with no ageing and no credit terms (B02 rank 1; AR Note 31 pp.246-247).
- Management said PSU production orders carry no advance (B05 red flags; Q3 FY26 call PDF p.12, corrected anchor per Verifier A). The Uttam order is a production order from a PSU.
- Management volunteered that part of reported inventory is legacy stock built up over about three decades, with obsolescence risk (B12b MISSED MAJOR; Q3 FY26 call, Atim Kabra, PDF pp.6-7).

Evidence for the GROWTH-INDUCED reading:
- CRISIL adjusted debtor days fell to 218 from 273, and inventory days fell to 275 from 286, in FY26 (CRISIL rationale 2026-08-28).
- Q4 was 42.0% of FY26 revenue (B03; AR p.12). Management said March balances are always high and that Q3 and Q4 carry the pressure (B05 analyst note).
- Peers say a back ended year with an inventory build is industry normal. Apollo still showed H1 FY27 CFO of +Rs 22 Cr, so peers do not settle the question (B06 P2 partially verified; FLAG-PEER-CFO; Apollo Q2 FY27 call p.3).

Rating agency commentary, verbatim (CRISIL rationale dated 28 Aug 2026, inputs/rating/CRISIL_rationale_2026-08-28.txt, "Key Rating Drivers - Weaknesses", text line 108; the file has no page markers, so the anchor is the line):

"Large working capital requirement despite improvement in fiscal 2026: The company has sizable working capital requirement due to higher gestation period of the product and complex nature of the products. Longer gestation period has led to sizeable inventory and receivables owing to many tests and approvals required from customers and 3rd party inspections before clearance of the bill. However, in fiscal 2026, the company has improved the overall working capital requirement due to moderation in inventory and receivables. Overall inventory and debtors moderated to 275 days and 218 days, respectively, (Crisil Ratings-adjusted) in fiscal 2026 from 286 days and 273 days, respectively, in fiscal 2025. This resulted in moderation in overall GCAs (net of cash) to 429 days as on March 31, 2026, from over 500 days in fiscal 2025. This resulted in reduction in working capital debt, through strong focus on realisation of receivables and innovative inventory management. The GCAs are expected to be maintained at 420-440 days over the medium term as the company continues to rationalise debtors and strong inventory management practices."

Rating downgrade factor, verbatim (same file, text line 151): "Weakening of the financial risk profile on account of higher-than-anticipated debt or stretch in the working capital cycle with GCAs of over 500 days".

Provenance note: no stage carried this quote. Stage 13 retrieved it from the corpus rationale for quoting only and did not re-analyse it. No verifier has checked it.

Capex commissioning timeline: NOT FOUND (B07 input gaps: facility utilisation, installed capacity and capex commissioning dates are in no document). Capex guidance conflicts: Rs 40 to 50 Cr a year (Q4 FY26 call p.11) against Rs 75 Cr for FY27 (AR p.192). H1 FY27 cash capex was already Rs 59.97 Cr (B07 FLAG-CAPEX).

Receivables composition: net 69,343.47 Rs Lakhs (AR Note 9). The ARC related party balance is 19,579.28 (27.9% of current gross). Past due more than 2 years is 8,158.33 (11.5% of gross 70,825.05). Three unnamed customers took 52.84% of FY26 revenue (AR Note 33(c) p.251). Government share of the old bucket: NOT FOUND.

Separating metric (stated so the next print can resolve the flag): FY27 standalone CFO at 31 Mar 2027 (Q4 FY27 results, May 2027).
- Negative CFO with inventory above Rs 793 Cr confirms STRUCTURAL.
- Positive CFO with inventory below Rs 793 Cr and the over two year bucket at or below 8,158.33 Rs Lakhs supports GROWTH-INDUCED.
- The CRISIL trigger to watch is gross current assets over 500 days.

### FLAG-GATE0: ACTIVE

- Score: grand total 68 of 160; core 53 of 100; moat 15 of 60; moats confirmed 3 of 12; moat class MODERATE; classification AVERAGE (B01).
- Blocks: A 16, B 0, C 12, D 17, E 8 (B01).
- Deal breaker DB2: Block B is 0 (below 8), which caps at GOOD. B1 is 0.47 and real. B2 to B4 are NOT FOUND, because the capex and trade payables history for FY17 to FY24 is missing (B01).
- Deal breaker DB4: cumulative CFO/PAT is 0.47 (below 0.50), which caps at AVERAGE. The driver is negative CFO in FY23 to FY25 (B01).
- Depressors: cash conversion, not returns. ROCE was 22.94% in FY26 (AR p.11), and net debt to EBITDA was 0.10 in FY26. On Sep 2026 data, Block D is unchanged: net debt to EBITDA 0.77 TTM, interest cover 6.69, D/E 0.36, current ratio 2.55 (B01 data notes). Block B is trending worse: H1 FY27 CFO was -147.85 Rs Cr consolidated (Q2 FY27 results p.12) (B01).
- Robustness: the stage says that with every NOT FOUND item at its best partial value, core reaches 64 and DB4 still caps at AVERAGE (B01 analyst note). Verifier C finding C-P1-06 tested two window readings: grand total 65 with moat 12, or core 61 with DB2 off. AVERAGE and MODERATE hold under both (B12c).

### FLAG-FRESHNESS: ACTIVE

The latest filed call is Q1 FY27 (11 Aug 2026). The Q2 FY27 call (13 Nov 2026) is not in the corpus (B00 freshness pair 1 FAIL; B05). Q2 FY27 delivery was checked only against the results, the press release and the presentation. Management's explanations of the H1 FY27 cash outflow, the ARC FY27 target and the Uttam terms are NOT FOUND.

### FLAG-PROMOTER: not active

Stage 8 verdict: CAUTION (scorecard: clean 4, caution 6, red 0; no deal breakers) (B08). The flag fires on CONCERN or AVOID only. The verdict is carried here as a caveat, with its basis.
- Top finding 1: the Item 9 ARC related party limit (Rs 200 Cr, FY27) passed with 35.687% of institutional votes against. The promoter group voted 6,205,827 shares FOR on a resolution marked "promoter interested: Yes", while the Notice says related parties shall abstain. The non promoter vote still passes at 83.7% (calc). The Directors' Report says there was no material RPT in FY26, yet ARC FY26 transactions were Rs 160.09 Cr (VERIFIED; voting results 2026-09-18 pp.4-13; AR FY26 Notice pp.82-86, Directors' Report p.95) (B08).
- Top finding 2: Audit Committee member Suresh Kumar Somani (non independent NED) holds 0.10% of ARC and 289,351 warrants personally. His Ratnabali bloc holds 6.30% of AMPL, and the Somani group took 40.2% of the warrant issue (VERIFIED; AR FY26 CG pp.167, 171; BSE shareholding 2026-09-30) (B08). A 2010 SEBI adjudication order names a Kolkata broker of the same name. Identity is NOT confirmed (UNVERIFIED; sebi.gov.in) (B08).
- Transition evidence (B08): two independent directors with strong credentials added on 22 May 2025, with Anuradha Mookerjee chairing the Audit Committee (AR CG pp.168-170). Internal MD succession: Dr M.V. Reddy is MD from 1 Oct 2026, passed 99.9999% for (AR p.96; voting results p.10). Mutual funds rose to 15.58% and FPIs to 10.48% at 30 Sep 2026, from 13.96% and 7.56% (BSE shareholding). Promoter pledge, NDU and other encumbrance are nil (BSE shareholding cover items 7-9). The demerger is a one for one mirror with no cash (Reg 30 2026-06-10 Annexure A). Insiders put their own money into the warrants (BSE shareholding; calc).

## Contradicted claims (priority monitoring items)

From the peer stage:
1. "Rs 40 to 50 Cr a year capex suffices for a tripling, no additional capex" (Astra, Q4 FY26 call p.11). CONTRADICTED with a weighting. Data Patterns plans Rs 150 to 200 Cr minimum over two years (DP Q1 FY27 call p.16), and Apollo is building capacity about 12 times its present facility (Apollo Q2 FY27 call p.7). Verifier B rates this OVERSTATED: the peers describe their own scale up, which does not test Astra's need. Treat it as a reconcile item against the Rs 75 Cr FY27 capex in AR p.192, not as proof of error.
2. Astra as "Tier 1" on the Su-30 radar (Q1 FY27 call p.7). This is a hedged contradiction. Data Patterns says "Astra is a DcPP partner for MCA variant, not the Su30 variant as I understand" (DP Q1 FY27 call p.18). The peer stage scored it as partial support. Verifier B reclassifies it as a hedged contradiction on the Su-30 sub claim.

Company statements that its own filings contradict (concall and AR stages, for completeness):
3. The Q4 FY26 call promised to keep the CFO trend and improve working capital further. H1 FY27 standalone CFO was -14,612.63 Rs Lakhs (Q2 FY27 investor presentation p.12).
4. ARC was called a JV on one call and a wholly owned subsidiary on the next. Its FY27 sales target moved from Rs 600+ Cr (Q4 FY26 call p.5) to Rs 360 Cr (Q1 FY27 call PDF p.4). AMPL holds 50.00% (AR p.101).
5. The Q1 FY27 call gave FY26 turnover as Rs 1,057 Cr (PDF p.19). The filed standalone figure is Rs 1,155.67 Cr (AR p.191).
6. The Directors' Report says there was no material RPT in FY26 (AR p.95). ARC transactions were Rs 160.09 Cr, 13.85% of revenue, and the Notice seeks a Rs 200 Cr limit (AR pp.82-86).
7. The FY26 AR prints four credit rating versions (pp.7, 26, 34, 94). The CRISIL rationale of 28 Aug 2026 settles the current rating at A+/Stable, upgraded from A/Positive.

## Monitorables and triggers

1. Watch FY27 cash conversion. Pull the standalone CFO and inventory from the Q4 FY27 results (May 2027) and compare them with H1 CFO of -Rs 146 Cr and inventory of Rs 793 Cr. Positive CFO with lower inventory supports a growth build. Negative CFO with higher inventory marks the gap as structural. This tests FLAG-CASH and the Part B5 ugliness class.
2. Watch Q3 FY27 standalone revenue in the Feb 2027 results against Rs 258.2 Cr in Q3 FY26. H2 must reach about Rs 913 Cr to deliver the Rs 1,350 Cr guide (Q1 FY27 call PDF p.4 and p.7). Also check the gross margin against 49% and EBITDA before other income against 28.07%. A miss moves credibility from B toward C and tests whether the margin gain is mix or timing.
3. Watch for the first disclosure of Uttam margin and advance terms on the Q2 or Q3 FY27 call. Track Phase 1 delivery of 12 units by Sep 2027 in HAL and Astra filings (Reg 30, 2026-07-30; Q1 FY27 call PDF p.10). No advance, with borrowings rising, means the order funds itself through working capital debt. This tests the qualification lock in moat and the cash flag.
4. Watch the ARC receivable against 19,579.28 Rs Lakhs and look for any ageing or credit terms. Use the half year related party disclosure and the FY27 AR Note 31. Check that ARC FY27 sales land at the stated figure (Rs 360 Cr on the Q1 FY27 call). A receivable growing faster than ARC sales breaks the partnership moat and raises the related party concern.
5. Watch receivables more than two years old against 8,158.33 Rs Lakhs, with ECL cover at or above 14.9% (FY27 AR Note 44). Read the next CRISIL rationale for gross current assets against the 500 day downgrade trigger and the 400 day upgrade trigger. This tests collection quality.
6. Watch the order book without HAL against Rs 2,058 Cr in each quarterly deck. Look for Reg 30 filings of the BEL QRSAM contract (Rs 700 to 800 Cr of Astra subsystems) and the AMCA antenna unit contract (Astra L1). A book without HAL that keeps falling while revenue is booked shows single order dependence.
7. Watch for the BSE allotment filing that confirms receipt of the Rs 130.50 Cr warrant balance by 29 Dec 2026 (AR CG pp.180, 183). CRISIL counts this money in liquidity. A shortfall is both a cash hole and an insider confidence signal.
8. Watch the demerger. The NCLT filing must come within the window of the 29 Oct 2026 exchange letters (about 29 Apr 2027), and carve out financials should follow. The claimed independent start is 1 Apr 2027. The space and weather lines carry 25.1% of the FY26 order book and supplied 56.3% of FY26 growth, so the base for every growth number changes when they leave.

## Falsification line

The single next quarter print that would do the most damage: Q3 FY27 standalone revenue below Q3 FY26's Rs 258.2 Cr (Feb 2027 results), with no statement on the Q3 call that material for Q3 and Q4 execution has arrived. That print puts the Rs 913 Cr H2 out of reach and repeats the FY26 guidance miss. It also leaves the H1 inventory build without the revenue that would release it.

## Open items for the operator at Halt 1

(a) Verifier B sensitivity. Red flag acceptance is 91.7 as emitted, because the verifier prompt counts PARTIALLY CAUGHT as found (11 of 12). If only fully caught items count, the rate is 7 of 12 = 58.3, below the 60 line. The verifier reported this reading and did not apply it. The block governs, so REWORK does not fire. The operator decides whether the sensitivity changes how far to rely on the concall stage. The concall stage missed one MAJOR (the legacy inventory admission) and partly caught three (order book goalpost redefinition, 18 month senior churn, turnover multiples on a base that includes the demerging lines).

(b) Verifier C MAJOR C-P1-01. The verifier recomputes em_score as 19.2 (range 18.7 to 19.2) against the stage's 16.5. A3, A4 and G2 were scored 0 although evidence matches a listed indicator. The band stays MODEST and active categories do not change. The stage's fragility claim fails: the downside case with B2 and H2 both failing is 13.2, not 10.5, and the gap to STRENGTHENING is 5.8, not 8.5. Stage 7 was not re-run (no REWORK trigger, and a re-run would use the one remediation cycle). Six framework gaps need an operator ruling:
   1. prompts/01: per metric minimum window undefined (C-P1-06).
   2. prompts/07: Strong / Moderate / Weak / None cut-offs undefined; the stage used its own.
   3. prompts/07: combined matrix mapping absent (labels only); 6D is not re-derivable in phase 1 scope.
   4. prompts/07: "active" in the completionist guard undefined (non zero against Strong/Moderate).
   5. prompts/07: multiplier rule for mixed class evidence undefined.
   6. prompts/07 2C: "historical" fixed asset turnover (latest against mean) and the treatment of intangibles under development undefined.

(c) Stages 8 and 9 ran PARTIAL. The skipped searches are listed in the verdict block above. The ones that matter most at Halt 1 are three. First, the DIN or PAN identity check on the 2010 SEBI order. Second, the outcome of the March 2026 SEBI inquiry on the FY24 results. Third, an independent market size that does not rest on management's programme pool.

(d) Corpus gaps from the intake list:
   - ABSENT: Q2 FY27 concall transcript (call held 2026-11-13; BSE carries only the audio filing 92bb686f). HIGH. Freshness pair 1 fails. Source: BSE announcements, scrip 532493, or the screener documents page.
   - ABSENT: screener export sheets Profit & Loss, Quarters, Balance Sheet, Cash Flow and Customization came out empty. Only the Data Sheet is populated. Fix: open Financials.xlsx in Excel or LibreOffice, save it, then run collect_to_repo.py --push-again.
   - ABSENT: PARAS peer concalls (see item e).
   - ABSENT in announcements/: the filing on the successor MD appointment (Oct 2026). The April 2026 Reg 30 said the outgoing MD stays as Executive Director, but the AR says he leaves the Board on 30 Sep 2026. The successor filing resolves this. Source: BSE announcements.
   - ABSENT in announcements/: the warrant or preferential allotment filing (outside the 12 month BSE window). Allottee names rest on a numeric match to the BSE shareholding pattern plus a Bajaj Broking article (MEDIA REPORTED). Source: BSE announcements for 2025.
   - UNRESOLVED: the AGM voting results letter dated 2026-09-18 says in its body that the AGM was "held on September 18, 2025".
   - The three SEBI items stage 8 found on the web, none of them in the corpus (operator upload list): (1) the SEBI inquiry email of 2 Mar 2026 on the FY24 results and the company reply of 6 Mar 2026, seen only in media (the company's Reg 30 text is needed); (2) SEBI Adjudication Order SD/AO/65/2010 against M/s Suresh Kumar Somani, with identity against the Astra director NOT confirmed; (3) the SEBI order on Skanda Aerospace (Dec 2017, a shareholder), media only.
   - Resolved at intake Step F: shareholding (BSE Sep 2026 pattern), results (Q4 FY26, Q1 FY27, Q2 FY27) and the CRISIL rationale of 28 Aug 2026 are now in the corpus. The prospectus and research folders are empty, which is not a gap for a long listed company.
   - Other NOT FOUND items the stages named: names of the three customers above 10% of revenue; ARC credit terms and receivable ageing; promoter pledge history beyond 30 Sep 2026; covenant terms; the bid value behind the 9.68% strike rate; a timeframe for the Rs 6,000 to 8,000 Cr pipeline; the Uttam margin, advance and payment schedule; demerger carve out figures; the 30 Jun 2026 deposit and working capital lines; segment margins; named competitors.

(e) PARAS has no transcripts. Screener lists none, and 90 BSE filings (scrip 543367, Nov 2025 to Nov 2026) hold no transcript. The peer set is two (Data Patterns, Apollo), and peer utilisation is NOT APPLICABLE on a denominator below 4. The operator decides whether to replace PARAS with a peer that files transcripts before FTTCP.

(f) Further items carried for Halt 1:
   - Verifier A MAJOR: the HAL order gap is 0.53%, not about 1.2%. The Rs 1,878.8 Cr (deck) and Rs 2,205.23 Cr incl. taxes (AR p.28) figures reconcile within rounding. The "not reconciled" framing in the business model stage's concentration flag is withdrawn on that point.
   - Verifier B reads credibility as B minus. Delivered is 4, not 5, because man portable SDR is OPEN. The trigger for a C grade is unchanged: H2 FY27 revenue near Rs 913 Cr and FY27 year end CFO.
   - Ownership basis: the brief says ARC is 51%. AMPL holds 50.00% (AR p.101), and directors hold 0.80% personally (AR p.86).
   - March 2026 quarter lender returns were not filed (AR Note 43(iii) p.260; CARO ii(b) p.204). Confirm that the Q1 and Q2 FY27 returns were filed.
   - The deck says IMD is 18.0% of FY26 revenue and exports 11.9% (IP p.8). The AR says Hydro-Met is 4.0% and exports including deemed exports 14.0% (AR p.191). These are not reconciled.
   - The Mental Model Declaration is unsigned. Nothing in this file marks it signed. FTTCP and any valuation wait for the signature and a PROCEED decision at Halt 1.

## Excluded by mode

This gate decision rests on evidence alone. It carries no BUY, WATCHLIST or AVOID decision, no entry range, no MoS price, no destination PE track, no Hurdle verdict and no zone reachability line. Stage 11 has not run.

## Publish check

No publish candidate this analysis.
