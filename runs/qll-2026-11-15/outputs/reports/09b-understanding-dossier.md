# HALT 1 UNDERSTANDING DOSSIER: Qualitek Labs Ltd (QLL; BSE SME 544091)

Run date: 2026-11-15. Stage 09b, model claude-sonnet-5-5. Assembled from blocks B00 to B09, B12a to B12d, confidence.yaml and B13. The annex in section six quotes the corpus directly.

Units. Filings report in INR Lakh. Presentations report in INR Crore. Every figure keeps the unit of its source. Four stage reports (01, 02, 03, 07) carry an orchestrator erratum. The corrected value governs here: H1 FY26 consolidated revenue is Rs 5,424.38 Lakh and H1 FY27 growth is +33.2% (B12a finding 1); H1 FY27 net cash change is (400.51) Lakh (B12a finding 2); H1 FY27 derived gross capex is 3,578.79 Lakh (B12a finding 3); ITCPL own net worth is 1,905.65 Lakh, and 752.02 is its share in consolidated net assets (B12a finding 4; B03).

This file is an understanding document. It holds no valuation and no decision. The Mental Model in section two is a draft. The operator signs it in claude.ai only.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

Inventory only. Source: B00 inputs and corpus manifest.

1. CONCALLS (main company). None held. The folder inputs/concalls/ is EMPTY (B00 inventory concalls: 0; concalls_available false). No transcript is published on screener, BSE or the company site (B00 input_gaps). The company does hold calls: intimations were filed, and screener shows Transcript chips with no link for May 2026 and May 2025 (B00). Most recent quarter covered by a held transcript: none. A more recent quarter has reported: H1 FY27 results were filed on 13 Nov 2026 (inputs/results/20261113-190e3152-723f-4dd6-b960-3db581435d45.pdf). Its call is intimated for 24 Nov 2026 (20261114-ffae6832) and had not been held at the run date (B00). Stage 5 ran in no-concall mode (B05). Twelve peer-company transcripts are held (Vimta, Krsnaa, Dr Lal PathLabs; each Feb, May, Jul or Aug, and Nov 2026 files; B00). None is a QLL transcript.
2. ANNUAL REPORTS. Two held: FY2025-26 (Annual_Report_2026.pdf, 191 pp, BSE cover letter 3 Sep 2026) and FY2024-25 (Annual_Report_2025.pdf, 183 pp, BSE cover letter 3 Sep 2025) (B00 manifest). The latest completed FY (FY26, year ended 31 Mar 2026) is present. Three years are not held: only two ARs are on file. FY2023-24 is covered by the Jan 2024 prospectus (restated FY23 and H1 FY24) and the comparatives in AR25 (B01 input_gaps). The company listed on 29 Jan 2024 (B00 listed_date).
3. RESULTS FILINGS. Three held: H1 FY26 (20251112-d1d63f49, dated 12 Nov 2025), FY26 audited (20260520-dc0311a3, dated 20 May 2026) and H1 FY27 (20261113-190e3152, dated 13 Nov 2026, period ended 30 Sep 2026, unaudited) (B00 manifest). Latest filing: 13 Nov 2026. The company reports by half year (B05). There is no quarter-gap between the latest results and the corpus; the latest results post-date the latest AR (31 Mar 2026) by one half-year. Results before Nov 2025 are not held as filings.
4. INVESTOR PRESENTATIONS. Two held: Investor_Presentation_May2026_H2FY26.pdf (BSE cover letter 21 May 2026) and Investor_Presentation_May2025_H2FY25.pdf (May 2025) (B00 manifest). The H1 FY27 presentation was not filed at the run date (B00 input_gaps; B04 input_gaps).
5. RESEARCH / RATING. None. rating/ is EMPTY: no credit rating rationale found in web and BSE searches covering 2023-12 to 2026-11, so the company may be unrated (B00 input_gaps; that is a collector gap, not proof of no rating). research/ is EMPTY: no broker notes (B00).
6. CORPORATE ACTIONS. 58 BSE Reg 30 filings, dated 2025-11-16 to 2026-11-14 (B00 inventory). Among them: HDFC corporate guarantee outcome (20251211-5ef25fa8); board outcome on NCD issue up to Rs 65 Cr (20251220-0fab5880); company secretary cessation (20260209-7b6ff1b4); MD&A filing of 20 May 2026 (20260520-78cbc582); NABCB accreditation (20260625-fe69b871); company secretary exit (20260730-44102f7e); pay-cap withdrawal (20260907-d2d6e19d); EGM notice for the preferential issue (20260924-fd526286); EGM voting result (20261018-d0ca2f7e); independent director resignation (20261029-5e7edc16); objects-clause EGM notices (20261113-c4dee558, 20261113-05e9700a); call intimation (20261114-ffae6832) (B03, B07, B08). The set holds 8 same-day duplicate pairs and 4 cross-folder copies, kept. Two Hindi newspaper adverts extract garbled; their cover letters are clean (B00). Filings before 2025-11-16 are absent (the ITCPL share-swap approval and allotment filings, the LabOps acquisition of 23 May 2025).
7. FRESHNESS PAIR CHECK. B00 freshness_verdict: FRESHNESS PAIRS OK. No pair failed. Pair detail: RESULTS to CONCALL is SKIPPED (concalls_available false; trigger H1 FY27 results; expected mate H1 FY27 concall transcript; the call is not yet held). RATING BULLETIN to RATIONALE passes (no rating bulletin). SEBI ORDER to ORDER TEXT passes (no order found; B03 reports no SEBI order). AR to LATEST AUDITED RESULTS passes (FY26 audited results held with the FY2025-26 AR) (B00).

Empty input folders, repeated for the operator because the empty-folder confirmation was suppressed under the /step1 autonomy contract (standing answer: continue with the gaps) (B00 empty_folder_confirmation): rating/, concalls/ (declared), research/.

Other input gaps from B00, repeated:
- shareholding/ holds a screener extract only (Sep 2026). The BSE pattern filing was blocked by a 403 bot wall, so FII, DII and pledge figures are screener-derived.
- QLL Data_Sheet Quarters block is EMPTY. P&L, Balance Sheet and Cash Flow carry FY21, FY22, FY25, FY26 only. Screener formula sheets exported empty for all four companies.
- The H1 FY27 investor presentation is not yet filed.
- annual-report/ holds two ARs against a 0-1 contract; FY2025-26 is primary and FY2024-25 is supporting history.
- VIMTALABS Data_Sheet latest year is FY2023-24.
- Two newspaper-advert announcements extract garbled.

Stage-level gaps that bear on the corpus: stage 8 (promoter) ran partial because SEBI, SAT, eCourts and MCA21 portals were out of reach (B08); stage 9 (market sizing) ran partial and skipped peer revenue aggregation and a global benchmark (B09).

CORPUS GAPPED: the main-company concall transcripts for May 2025 and May 2026 (calls held, never published; plausibly-nonexistent as public documents, itself a data point on disclosure opacity; check the company IR page for audio or transcript); the H1 FY27 concall transcript and H1 FY27 investor presentation (not yet held or filed; findable-missing after 24 Nov 2026 on BSE and the company IR page); the BSE shareholding pattern filing for Sep 2026 with the pledge line (findable-missing, BSE); the FY2023-24 annual report (findable-missing, BSE; B08 records it was filed 342 days late); BSE filings before 2025-11-16 including the ITCPL share-swap approval and valuation papers (findable-missing, BSE); a credit rating rationale (plausibly-nonexistent, rating agency sites; the company may be unrated); broker or research notes (plausibly-nonexistent for a BSE SME name; not confirmed); screener P&L, Balance Sheet, Cash Flow and Quarters sheets (findable-missing, screener re-export then collect_to_repo.py --push-again).

---

## SECTION 2: MENTAL MODEL DECLARATION

DRAFT - PENDING OPERATOR SIGN-OFF

This declaration is a draft. It is not signed. Signing happens only in claude.ai after live-web stress-testing. The transition read below is the dossier's reading of management's filed claims, not a management statement of rung migration.

### PART A: THE FROM STATE

A1. ARCHETYPE.
- Transport, defence, mechanical testing (40-45% of revenue by management range; FY26 actual NOT FOUND) (B04): Outsourcing partner. Drivers: customer capex and development cycles, wallet share, capacity fill, price per test.
- Food and feed testing (25-30%, management range) (B04): Outsourcing partner. Regulation-driven volume; weak on price (B04 narrative).
- Pharma, cosmetics and life sciences testing (15-20%, management range) (B04): Outsourcing partner. Partial pricing power in niche accredited scope.
- Minerals, metals, PPP lab operation, inspection, software (residual, NOT FOUND) (B04): PPP lab operation fits Outsourcing partner with a government payer. The six PPP labs are the nearest thing to a licence, but the terms are not filed (B04, B07).
- Note. Accreditation looks like a licence, but the emerging moat scan finds it replicable (B07, B04). The Licence/scarcity archetype is therefore not used. The acquisition roll-up pattern is an overlay on the archetype, not a separate archetype in the library. The vertical shares are management ranges because the company files one segment (B04 FLAG-MIX-UNREPORTED).

A2. THE SIMPLE ANALOGY. Think of a company that runs 16 accredited examination rooms across India. Ten are its own. Six belong to state governments, which hire it to run them (B04, B09). A maker of car parts, a food exporter or a drug maker cannot place a regulated product on the market without a stamped test report. The company is the room that issues the stamp, and it bills each time a report is issued (B04). The rooms are only as good as how full they are, because the staff and the machines cost money whether or not a customer walks in (B04 key_lever). In the last two years the owners added rooms by acquiring other labs and by building new ones. The business today is a fast-growing chain of rooms, many of them new, with the bills coming in more slowly than the work (B03, B07).

### PART B: THE TRANSITION

B1. FROM TO TO (quality ladder, per line).
- Line one: transport, defence, mechanical and pharma testing in spec'd, accredited scope. FROM: R2 (the rung is defined by margin from position and mid-teens ROCE; FY26 consolidated ROCE is 10.8% (B01), which sits below the R2 description, and pricing power is moderate (B04), so the name sits between R1 and R2 and is declared at the upper edge). TO: R3 VALUE-ADDED / SPEC'D SUPPLIER (partial pricing power, ROCE 20-25%). The claim for R3 rests on defence standards JSS 55555 and MIL 810, USFDA-grade pharma work and the 25-27% margin guide (B03, B07). One rung in the 2 to 3 year base rate; no multi-rung leap is claimed.
- Line two: food and feed testing, minerals and metals assay. FROM: R1 (weak price power, B04 narrative). TO: R2 (scale and fill in clusters). No higher claim is evidenced.
- Fits-no-rung finding: the deck prints ROE 22% and ROCE 17% (B04), while the AR prints RoNW 6.9% and ROCE 7.4% (B12b). The ladder cannot be placed on the deck's figures. The AR basis is used.

B2. THE ENGINE. Two things physically change.
1. Fill of new and acquired labs. Fixed lab cost is absorbed as test volume rises, which lifts margin. FY26 incremental EBITDA margin was 24.0%, equal to the average, so no operating leverage showed yet (B04 FLAG-NO-LEVERAGE). H2 FY26 consolidated EBITDA margin was 25.7% (B05), then H1 FY27 was 21.6% (B05). Capex in progress is Rs 6,977.28 Lakh at 30 Sep 2026 and only 11.5% of CWIP was capitalised in FY26, against 31.5% in FY25 (B07).
2. Mix toward regulated, spec'd scope: NABCB ISO/IEC 17020 inspection accreditation (June 2026), USFDA-grade pharma lab, defence standards (B07, B03). The evidence is claim-tier. No inspection revenue line is filed (B03).

The ugly optic this engine hides: margin fell, cash conversion fell, borrowings rose (B03 FLAG-CASH, B05).

B3. THE PROOF GATE. Primary gate, tested at half-yearly prints (the company reports by half year, B05): consolidated EBITDA margin at or above 27.0% in H2 FY27, on H2 FY27 revenue at or above Rs 9,583 Lakh, with growth that comes from existing labs and a standalone versus subsidiary margin split disclosed (B03 monitorables; B04; B06 cross-peer hypothesis). A full year of 25% needs H2 FY27 at 27.4 to 27.6% (B12b). Companion gate for cash: FY27 consolidated CFO/PBT above 90% with the over-6-month receivable share below 20% (B03 monitorables). Until both fire, the transition is narrative and the name is research. FTTCP (phase 2, /fttcp) tests these.

B4. THE RECOGNITION GAP (open question for Stage 11). Does the TO state (R3 margins and returns) already appear reflected in market pricing? This dossier does not conclude. Stage 11 resolves it through the PE gap. If the TO state is already reflected, the re-rating engine is spent and only earnings growth remains.

B5. THE UGLINESS TEST. Classification: ARTIFACT-OF-CLIMB, provisional, with low confidence on the cash leg.
- Evidence for ARTIFACT-OF-CLIMB: the depressors date from the post-listing build (B01 analyst_note); ROCE fell 22.4% (FY23) to 10.8% (FY26) as capital employed grew about ten times on goodwill and CWIP (B01); the H1 FY27 margin gap sits in the acquired subsidiaries (derived 14.6% against 18.6%) while the standalone company held 25.9% (B12b); the aged receivable share barely moved, 22.2% to 22.4% (B02); same-half EBITDA margin rose 20.7% to 21.6%, so H1 is the weak half (B12b).
- Evidence for STRUCTURAL-FEATURE: free cash flow was negative in all six years (B01); H1 FY27 CFO/PBT is 42.0% (B03); the standalone receivable days rose 93.8 to 106.4 (B02); the red flag verifier reads the pattern as disclosure integrity, graded D (B12b); credit rests on promoter-side guarantees covering about 84% of bank debt (B02). The cash determination is INDETERMINATE (B13 gate file; B03).
- Two readings and the observation that separates them: growth-induced (the book grows with new labs and acquisitions) or structural (a payer problem at the six PPP labs). Separator: receivables ageing by customer type plus FY27 CFO/PBT (B02, B03). The Stage 13 value-trap test carries this classification. No trade verdict is made here.

B6. THE TRANSITION FALSIFIER. H2 FY27 consolidated EBITDA margin below 24%, with growth coming from labs under 12 months old and PPP billing, while CWIP keeps rising and is not capitalised (B05 kill_signal; B06 hypothesis; B07). Also: the Hyderabad and Bengaluru lab completions slip again without a completion filing (B07 catalysts).

### PART C: WHAT THE MODEL WATCHES

C1. DOMINANT VARIABLES (these become the Role 5.5 tracker signals).
1. Consolidated EBITDA margin in H2 FY27, split standalone versus subsidiaries. State now: 21.6% in H1 FY27; standalone 25.9%, subsidiaries 14.6% (derived) (B05, B12b).
2. Lab fill and commissioning: revenue per lab and CWIP capitalisation. State now: CWIP Rs 6,977.28 Lakh at 30 Sep 2026; 11.5% capitalised in FY26; 3 of 9 capex completion rows delivered (B07).
3. Cash conversion and payer quality. State now: CFO/PBT 75.7% FY26, 42.0% H1 FY27; receivables over 6 months 22.4% of a Rs 4,220.12 Lakh gross book against a Rs 6.08 Lakh provision (B03, B02).
4. Funding and leverage. State now: borrowings Rs 9,297.55 Lakh at 31 Mar 2026 to Rs 11,466.88 Lakh at 30 Sep 2026; net debt/EBITDA about 3.6x annualised; interest cover 3.21x (B03, B05).

C2. WHAT THE MODEL REJECTS. Market size is noise: the three core verticals are a Rs 24,354 to 27,871 Cr market and QLL holds 0.78% of the part it can serve (B09). The binding constraint is capacity, margin and cash, not market (B09 FLAG-SHARE-IS-NOT-THE-CONSTRAINT). Also noise: the Rs 500 Cr FY31 ambition as a forecast input (it depends on acquisitions, B09), the headline +77% growth (acquisition-inflated; B04), and deck return ratios (B12b).

C3. THE BUSINESS FALSIFIER. Evidence that forces a re-declaration of the FROM business itself, separate from B6: (a) standalone organic growth under 15% once the Mumbai slump-sale lab is removed (B04 red flag line; B12b); (b) ITCPL PAT under Rs 710.83 Lakh, or goodwill test inputs showing impairment of the Rs 7,811.56 Lakh balance (B03, B04); this would make QLL an acquisition roll-up with an impaired core, not a lab operator; (c) PPP payers proving to be most of the incremental revenue, which would re-declare the line as a government-contract operator; (d) an NABL scope suspension at a lab that carries a vertical (B09 candidate).

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

Draft at Halt 1 from B01 to B09 and the verifier blocks. Stage 13 holds the final copy.

QLL runs 16 accredited testing labs, ten its own and six government labs run under PPP contracts (B04, B09). The largest line tests transport, defence and mechanical parts, including vibration, durability, corrosion, emission and EV battery tests, some to the standards JSS 55555 and MIL 810 (B07). Food and feed labs check residues, allergens and shelf life, and pharma labs test impurities, stability and sterility (B04). Management puts these lines at 40 to 45%, 25 to 30% and 15 to 20% of revenue, but those are ranges for the FY27 growth drivers and the company files one segment, so the run did not establish the FY26 split (B04). A customer cannot place a regulated product on the market without an accredited test report, and QLL bills per test when it issues the report (B04). The customers are auto and component makers, defence suppliers, food and feed makers, exporters, drug makers, miners and public bodies such as Indian Oil and the Quality Council of India (B03). The last filed customer concentration is a top-ten share of 32.34% at H1 FY24, and the run found no retention or repeat revenue data to prove switching costs (B04). Present demand is mandated testing, tied to "BIS Quality Control Orders and FSSAI NABL-lab mandates", "India vehicle and EV production and registrations" and "Mineral output and Paradip port cargo volumes" (B09). Demand should grow with "USFDA inspection outcomes and CDSCO approvals for Indian pharma", "Ministry of Defence indigenisation lists and procurement orders" and "India food and pharma export volumes and export-rejection notices", all visible in public data (B09). The three core verticals form a Rs 24,354 to 27,871 Cr market growing about 8.9% a year, and QLL holds 0.78% of the part it can serve (B09). No testing line has a proven moat, because the emerging moat scan scored 11.0 and found none (B07). Transport, defence and pharma testing hold partial pricing power in niche accredited scope, food and minerals testing are weak on price, and accreditation is real but any lab can earn the same scope, so each line stands or falls with "NABL accreditation scope grants and suspensions for QLL labs" (B04, B07, B09). The six PPP labs, one on a Bhubaneswar contract of 27 years, give local scale and are the nearest thing to a moat, yet their terms are not filed and their cash depends on "Odisha and other state PPP payers: payment cadence and contract renewals" (B04, B09).

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. VERTICALS FRAMED

Vertical 1. Consolidated EBITDA margin path (dominant variable 1).
- The corpus establishes: FY26 consolidated EBITDA margin 23.6% (B03); H2 FY26 25.7% and H1 FY27 21.6% (B05); FY27 guide 25-27% (B03 guidance_table); standalone 25.9% in H1 FY27 against derived subsidiary 14.6% (B12b); FY26 incremental margin 24.0% (B04). Peers: new labs dilute margin first and recover with fill; Vimta cites 2 to 3 years for new capacity; no peer shows margin rising within four quarters of fast new-footprint growth (B06).
- It cannot establish: margin by vertical or lab, utilisation by lab, cause of the H1 gap in management's words (B04 input_gaps; no concall), the subsidiary cost structure (B12b).
- Questions that decide it: (1) What are revenue and EBITDA by entity and by lab for H1 FY27? (2) Does H2 FY27 growth come from labs older or younger than 12 months? (3) Why does the MD&A name the acquired entities as the FY27 margin driver while they carry the gap (B12b)?

Vertical 2. Lab fill and commissioning (dominant variable 2).
- The corpus establishes: CWIP Rs 6,977.28 Lakh (+2,449.03 Lakh in H1) funded by debt; capitalisation ratio 11.5% FY26; Rs 151.81 Lakh of CWIP older than 3 years; 3 of 9 capex rows delivered; pattern fast on deals, slow on commissioning (B07). Capex-embedded growth is 98% as the rule is written; the stage's 72% is a sensitivity (B12c E08; confidence.yaml). Committed capacity supports about Rs 214 Cr of revenue (B09).
- It cannot establish: CWIP by project, cost to complete, utilisation, status of the Hyderabad food lab and Bengaluru USFDA lab (B07 input_gaps, B05).
- Questions: (1) What is the CWIP split at 30 Sep 2026 and the commissioning date per project? (2) Is Hyderabad completed, and at what cost? (3) What revenue per lab does the 214 Cr capacity assume?

Vertical 3. Cash conversion and payer quality (dominant variable 3).
- The corpus establishes: CFO/PBT 100.8% FY25, 75.7% FY26, 42.0% H1 FY27 (B03); standalone receivable days 93.8 to 106.4, receivables +67.2% on revenue +47.4% (B02); over-6-month receivables Rs 944.10 Lakh with provision Rs 6.08 Lakh (B02); no rating rationale (B00); peer Krsnaa DSO 139-155 days with government payers, Lal 17 days (B06).
- It cannot establish: receivables by customer type, the PPP contract terms and payment cadence, why MD&A is silent on ageing (B03, B04).
- Questions: (1) What share of receivables sits with state PPP payers? (2) Are the Rs 220 Lakh older than three years recoverable? (3) Is the AAL Biosciences receivable of Rs 77.82 Lakh (2.1x its sales of Rs 37.30 Lakh) collected (B02)?

Vertical 4. Funding and leverage (dominant variable 4).
- The corpus establishes: borrowings +86% in FY26, then +23% in six months (B03); promoter-side guarantees cover about 84% of bank debt at Rs 0.20 Lakh fees each (B02); NCD up to Rs 65 Cr approved 20 Dec 2025, status NOT FOUND (B03); preferential issue of Rs 4,698.06 Lakh with Rs 2,200 Lakh for unnamed acquisitions (B03, B07); current ratio 0.78 at 30 Sep 2026 (B01).
- It cannot establish: covenants, TIC Services' source of funds for the warrants, NCD uptake (B08, B03).
- Questions: (1) Will TIC pay the Rs 20.22 Cr balance within 18 months? (2) Does the NCD close, and at what cost? (3) What happens to bank lines if a guarantor withdraws?

### 4b. CANDIDATE SIGNAL TABLE

UNVERIFIED. Verification and tracker writes happen at Role 5.5 in claude.ai. Eight B09 candidates carried.

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| BIS Quality Control Orders and FSSAI NABL-lab mandates | A mandate is withdrawn, deferred or diluted for a category QLL labs test | Event-Driven | BIS and FSSAI gazette notifications, Ministry of Commerce DGFT notices (Downstream_Source_Discovery_Protocol_v1_0 regulatory row) |
| India vehicle and EV production and registrations | Two consecutive months of year-on-year decline in production for the segments QLL tests | Monthly | SIAM monthly production data, MoRTH VAHAN dashboard |
| USFDA inspection outcomes and CDSCO approvals for Indian pharma | A fall in USFDA-regulated exporter inspections or approvals, or a data-integrity clampdown that moves testing in-house | Event-Driven | USFDA warning letter and 483 database, CDSCO order registers |
| Ministry of Defence indigenisation lists and procurement orders | Indigenisation lists stall or procurement orders shift away from private qualification testing | Event-Driven | MoD and PIB press releases, DRDO tender portals |
| Odisha and other state PPP payers: payment cadence and contract renewals | Payment delay beyond the cadence Krsnaa saw (DSO 139-155 days), or a non-renewed contract | Quarterly | State finance department budget documents, Reg 30 contract disclosures |
| Mineral output and Paradip port cargo volumes | Output or cargo falls year on year for two periods at Bhubaneswar and Paradip catchments | Monthly | Ministry of Mines monthly production data, Paradip Port Authority traffic |
| India food and pharma export volumes and export-rejection notices | Export volumes fall for two periods, with no rise in rejection notices that would drive pre-shipment testing | Monthly | Ministry of Commerce monthly trade data, APEDA, Pharmexcil, EU RASFF |
| NABL accreditation scope grants and suspensions for QLL labs | Any suspension or lapse at a lab that carries a vertical; no new scope grants for two quarters | Event-Driven | NABL accredited-lab directory, company Reg 30 filings |

### 4c. FRAGILITY READ

- variable_count: 8. Variables that must go right for the bull case: (1) transport, defence and EV testing demand; (2) food and pharma mandate and export volumes; (3) state PPP payer cadence; (4) NABL accreditation scope continuity; (5) lab fill after commissioning; (6) acquired subsidiary margin recovery; (7) bank credit continuity under promoter-side guarantees; (8) execution of the Rs 2,200 Lakh unnamed acquisition pool (B09, B07, B03, B02).
- verifiability_ratio: 4 of 8 externally observable (variables 1 to 4 via the B09 candidates; B09 demand_externally_verifiable true). Variables 5 to 8 rest on company narration or on filings the company controls.
- single_point_failure: Bank credit continuity resting on promoter-side guarantees (about 84% of bank debt, B02) while CFO/PBT is 42.0% (B03) and the current ratio is 0.78 (B01). Loss of that support alone would stall the build. It is a conditional kill-switch, not an observed event.
- fragility_verdict: FRAGILE. Half the variables are company-narrated and one kill-switch exists. The demand side is the robust part (B09: market is not the constraint).

### 4d. RESEARCH BRIEF (claude.ai work order)

1. PENDING LIVE VERIFICATION (chain 1, who pays and why now): open the SIAM monthly production and sales release for the latest month and the MoRTH VAHAN dashboard, and read the latest filings or orders of the auto and EV customers named in B03 (Tata, Reliance and others; no revenue share disclosed) and the Indian Oil 2G Ethanol QC lab order text (inputs/announcements; B03 ar_new_downstream_entities). Confirm auto and EV test demand is rising for the segments QLL serves.
2. PENDING LIVE VERIFICATION (chain 2, who pays and why now): open the Odisha Department of Finance budget documents and the PPP concession agreement for the Bhubaneswar lab (27-year contract, B04), and any other state PPP payer filing. Confirm payment cadence and renewal terms. Neither document is in the corpus.
3. Build chain 3: food and feed. Open FSSAI NABL-lab notifications, APEDA export data and the EU RASFF notice database. Test the link from export rejections to pre-shipment tests at Chennai, Mumbai, Bhubaneswar and the Hyderabad lab.
4. Build chain 4: pharma. Open the USFDA warning letter and 483 database and CDSCO registers. Test the Bengaluru USFDA lab link and identify the counterparty of the lab acquisition (cost NOT FOUND, B03).
5. Build chain 5: defence and EMI/EMC. Open MoD indigenisation lists and DRDO tender portals. Test the Pune EMI/EMC build against Vimta's note that EMI/EMC volumes arrive once per development cycle (B12b).
6. Search the rating agency sites (CRISIL, CARE, ICRA, India Ratings, Acuite, Infomerics) for any rationale on QLL or ITCPL. The company may be unrated (B00).
7. Check NCD issue status (up to Rs 65 Cr; 20251220-0fab5880) with BSE debt filings and the debenture trustee (B03).
8. Check eCourts and Calcutta High Court for CS/159/2022, ITC Ltd v Interstellar Testing Centre, Rs 50 Cr claim (B03, B08).
9. Check SEBI orders, SAT and MCA21 for TIC Services, SKM Realcon, the ASC group and the AAL entities (B08 input_gaps).
10. Fetch the BSE Sep 2026 shareholding pattern filing and confirm the pledge line (B00, B08).
11. Establish TIC Services Pvt Ltd's source of funds for Rs 6.74 Cr upfront and Rs 20.22 Cr balance on the warrants (B08).
12. Verify the NABL directory scope for each of the 16 labs and the NABCB ISO/IEC 17020 certificate in the company's name (B07).
13. Fetch Hyderabad and Bengaluru lab completion filings, and the status of Nellore, Karnal and Gandhidham labs (B07 optionality register).
14. Verify the source URLs and dates of the stage 9 market reports (Mordor updated 30 May 2026, IMARC, DataM) and the prospectus unit error (USD 26 million for a market in billions) (B09).
15. Run the listed testing peer revenue aggregation and the global per-capita benchmark that stage 9 skipped (B09).
16. Check the company secretary appointment after 30 Jul 2026 and the independent director replacement after 29 Oct 2026 (B08).
17. Confirm the statutory auditor's peer-review status and group audit fees (B03 input_gaps).
18. Verify the managing director podcast referenced by the red flag verifier, listed as PENDING LIVE VERIFICATION (B12b coverage_basis).

### 4e. SECOND-ORDER STUB (Rule F)

CHAIN 1: FY27 guide of EBITDA margin 25-27% against H1 FY27 21.6%, with H2 FY27 needing about 27.5% (B03 guidance_table; B05)
Link 1 [DOC]: The H1 FY27 margin gap sits in the acquired subsidiaries. Derived subsidiary EBITDA margin was 14.6% against 18.6% a year earlier, while the standalone company held 25.9% (B12b; H1 FY27 results pp.4, 11). The MD&A named the acquired entities as the FY27 margin driver (B12b).
Link 2 [PENDING LIVE VERIFICATION]: Who pays, and why now. The customers of the subsidiary labs (auto analytical, EMI/EMC, minerals and the Indian Oil ethanol lab) must send more tests per lab in H2 FY27. The corpus cannot show this. Claude web should open the SIAM monthly production release, the MoRTH VAHAN dashboard and the Indian Oil ethanol lab order text. No counterparty fact is stated here.
Link 3 [INFERENCE]: If H2 growth comes mainly from labs under 12 months old, the fixed cost of those labs sits ahead of their fill. Margin would then stay near the H1 level, not reach 27% (reasoning from B06 cross-peer hypothesis, B04 key lever, B07 capitalisation ratio). If growth comes from existing labs, margin should reach 27% or more, as at Dr Lal PathLabs (B06).
Binding constraint: commissioning, not demand. CWIP is Rs 6,977.28 Lakh and only 11.5% of CWIP was capitalised in FY26 (B07). Employee cost above 36% of revenue is the first deterioration signal (B04).
Unsaid: standalone includes the Mumbai food lab acquired by slump sale from 1 Sep 2025, so the 25.9% standalone margin is not fully organic and the +47% is overstated by an amount NOT FOUND (B12b; H1 FY27 results note 7, p.5). The deck and the AR do not give margin by lab.
Observation that confirms or breaks this chain, and confirm-by date: H2 FY27 consolidated EBITDA margin at or above 27% with H2 revenue at or above Rs 9,583 Lakh confirms; below 24% breaks (B05 triggers; B04). Read in the FY27 audited results, about May 2027. Interim read at the 24 Nov 2026 call: ask for the subsidiary split.

CHAIN 2: Cash conversion fell from CFO/PBT 100.8% in FY25 to 75.7% in FY26 and 42.0% in H1 FY27 (B03; B02 FLAG-CASH)
Link 1 [DOC]: Receivables over six months were Rs 944.10 Lakh, 22.4% of a Rs 4,220.12 Lakh gross book, with a provision of Rs 6.08 Lakh. Standalone receivable days rose from 93.8 to 106.4 and receivables grew 67.2% on revenue growth of 47.4% (B02 C-Note 15 p.127, S-Note 16 p.176).
Link 2 [PENDING LIVE VERIFICATION]: Who pays, and why now. The six PPP labs bill state payers. Their payment cadence and renewal terms are not in the corpus (B04, B09). Claude web should open the Odisha Department of Finance budget documents and the Bhubaneswar PPP concession agreement. No counterparty fact is stated here.
Link 3 [INFERENCE]: If PPP billing grows as a share of revenue, receivable days drift toward the 139 to 155 days Krsnaa reports with government payers (B06). That would tie more cash in working capital, push borrowings up, and make bank credit the binding limit before demand does (reasoning from B03 interest cover 3.21x, B02 guarantee cover 84%).
Binding constraint: bank credit resting on promoter-side guarantees (about 84% of bank debt, B02), borrowings Rs 11,466.88 Lakh, net debt/EBITDA about 3.6x annualised, current ratio 0.78 (B03, B01).
Unsaid: the MD&A does not discuss receivable ageing or cash conversion (B03 missing_risks). The contingent liability note omits the ITC Ltd Rs 50 Cr suit while listing Rs 2,133 Lakh and Rs 4,911 Lakh of intra-group bank guarantees (B03; Annual_Report_2026.pdf [page 137]). The receivables are not split by customer type (B02).
Observation that confirms or breaks this chain, and confirm-by date: FY27 consolidated CFO/PBT above 90% with the over-6-month receivable share below 20% supports a growth-induced read; below 60% reads structural (B03 monitorables; B04). Read in the FY27 cash flow statement, about May 2027, and Note 15 of the FY27 annual report, about Aug 2027.

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in claude.ai with live web, before Role 2.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. Qualitek Labs tests products so makers can prove they meet a rule. It runs 16 labs, ten of its own and six run for state governments (B04, B09).
2. It bills for each test report it issues. A maker cannot place a regulated product on the market without that report (B04).
3. The company grew to Rs 12,452 Lakh of revenue in FY26, up 77%, mostly by acquiring lab groups. Standalone growth was 47%, and some of that came from one lab it acquired (B03, B12b).
4. The customers are car and part makers, defence suppliers, food and drug makers, exporters and public bodies. The last customer concentration filed is from H1 FY24 (B03, B04).
5. The run found no proof that customers stay and repeat. Switching costs are plausible but unproven (B04).
6. Demand comes from rules that force testing. These include quality orders, food safety rules, EV growth and defence local-sourcing (B09).
7. The market is large and growing about 8.9% a year, and QLL holds under 1% of it. Market size is not the limit (B09).
8. Growth depends on capacity, margin and cash. Committed capacity supports about Rs 214 Cr of revenue (B09).
9. No testing line has a proven moat. Accreditation is real but any lab can earn it. The six state labs are the closest thing to a moat, but their terms are not filed (B04, B07).
10. The mental model, in one line: a roll-up of testing labs that must fill its new rooms to lift margin and cash, one rung up the quality ladder, with the proof still to come (section two of this file).
11. The fragility read is FRAGILE. Half of the things that must go right rest on company statements, and bank credit rests on promoter guarantees (section 4c).
12. The record so far is mixed. Margin is 21.6% against a 25 to 27% guide, cash conversion is 42%, and debt rose 23% in six months (B05, B03).
13. The corpus could not establish the revenue split by line, customer concentration after H1 FY24, receivables by customer type, state contract terms, or any management words on the margin gap, because no call is published (B04, B05, B00).
14. The biggest open question is whether the H1 margin dip is timing or a lasting level. The H2 FY27 margin and the subsidiary split decide it (B12b, B06).
15. The second open question is the Rs 7,812 Lakh of goodwill, mostly from a deal with the promoter holding company with no valuation report on file (B02, B12b).

---

## SECTION 6: STANDING EXTRACTION ANNEX

Quote-then-comment form. Page anchors use the [page N] markers in the .txt beside each PDF. Text extraction in the AR drops some spaces; quotes are cleaned for spacing only.

### 1. UNITS

- Quote: "an installed testing capability of more than 5 million tests annually" (Annual_Report_2026.pdf, MD&A, [page 70]). Also: "10 owned laboratories and 6 laboratories operated under Public-Private Partnership ("PPP") arrangements" (same page).
- Comment: This is a capacity figure for the whole basket of tests, not a delivered volume. No price per test, revenue per test or test count delivered is printed in the corpus. The lines to derive one are: consolidated revenue from operations Rs 12,451.81 Lakh for FY26 (20261113-190e3152 [page 11], FY26 column) and tests actually performed, which are NOT DISCLOSED. B04 derives revenue per lab-year of about Rs 7.8 Cr as an upper bound (B04 unit_economics). Per-test price: NOT DISCLOSED.

### 2. SEGMENT CAPITAL AND DEBT

- Quote: "The Group has only one primary business segment, i.e. testing & inspection services, and operates majorly in one geographical segment. All the revenue, trade receivables and non-current assets of the Group are located within India. Accordingly, no separate segment information is required to be disclosed under Accounting Standard (AS) 17" (Annual_Report_2026.pdf [page 137], Note 29).
- Comment: Segment assets, segment liabilities, capital employed and allocated borrowings: NOT DISCLOSED, because one segment is reported. Borrowings are unallocated. Totals as printed in the H1 FY27 consolidated balance sheet (20261113-190e3152 [page 12]): Long Term Borrowings 6612.40 (30 Sep 2026) and 6012.15 (31 Mar 2026); Short Term Borrowings 4854.48 and 3285.40 (Rs Lakh). The sums are 11,466.88 and 9,297.55 Lakh (B03). Shareholders' funds are 15902.62 and 15242.60 Lakh (same page).

### 3. GUIDANCE VERSUS ASPIRATION

| Item | Quote | Class | Anchor |
|---|---|---|---|
| FY27 revenue, EBITDA, PAT margin (May 2026) | "For FY27, we are guiding to consolidated revenue growth of 35–40% over the FY26 base, with consolidated EBITDA margin in a range of 25 –27% and PAT margin in a range of 15 –17%." | (a) guidance with a period (FY27) | 20260520-78cbc582 [page 3] |
| FY27 margins (AR, Aug 2026) | "consolidated revenue growth of 35-40% over the FY26 base, with consolidated EBITDA margin in the range of 25-27% and PAT margin of 14-15%" and, in the MD&A, "the Company has indicated an aspiration for consolidated revenue growth of approximately 35%-40% ... PAT margin in the range of 14%-15%. These are management expectations" | (a) guidance with a period (FY27). The AR word is "aspiration" and the PAT range is cut from 15-17% without a stated reason | Annual_Report_2026.pdf [page 23], [page 73] |
| Net debt/EBITDA | "Net Debt to EBITDA at approximately 3.0x ... is expected to compress meaningfully as the acquired entities deliver their first full year of consolidated contribution in FY27" | (a) guidance with a period (FY27) | 20260520-78cbc582 [page 3] |
| Revenue ambition | "taking consolidated revenue past ₹500 Crore by FY31" | (a) period given (FY31); depends on acquisitions (B09) | 20260520-78cbc582 [page 3]; AR [page 24] ("₹500+ Crore of consolidated revenue by FY31") |
| Operating margin | "lifting consolidated operating margin above 30% over the next three years" | (a) period given; dropped from the AR | 20260520-78cbc582 [page 3] |
| Overseas share | "generating at least 30% of revenue from overseas customers by FY31" | (a) period given; dropped from the AR | 20260520-78cbc582 [page 3] |
| Debt-free | "operating the business on a cash-surplus, debt-free basis by FY32" | (a) period given; dropped from the AR | 20260520-78cbc582 [page 3] |
| Doubling and margin (May 2025 deck) | "2X Revenue in every 2 years & profitability improvement - 30% EBITDA margin" | (a) period given (two-year rolling) for the revenue goal; the 30% carries no date in the deck, so (b) | Investor_Presentation_May2025_H2FY25.pdf [page 13] |
| Vertical mix drivers (May 2026 deck) | "40–45% of Consolidated Revenue" (Transport, Defence & Mechanical); "15–20%" (Pharma); "25–30%" (Food & Feed) | (b) ranges of share without a period | Investor_Presentation_May2026_H2FY26.pdf [page 23] |
| Lab openings | "Acquisition of USFDA lab underway, commercial by June 2026"; "Hyderabad acquisition expected to complete by June 2026" | (a) period given (June 2026); no completion filing through 14 Nov 2026 (B03) | Investor_Presentation_May2026_H2FY26.pdf [page 23] |
| Capacity | "10 owned labs and 6 PPP labs ... more than 1,200 colleagues including 450 scientists, and an installed capability of more than 5 million tests per year" | (c) capacity or capability only | 20260520-78cbc582 [page 3] |
| Use of new funds | "Unidentified Acquisitions-Food, Pharma & Cybersecurity. 2200.00 Within 24 months"; "Expansion of Automotive Business 600.00 Within 24 months"; "Working Capital Requirement 800.00 Within 24 months" (Rs Lakh) | (a) allocation with a 24-month window | 20260924-fd526286 [page 12] |

Comment: the standalone margin "re-converge to historical levels" is a B03 derived range of about 26-29%, not a printed number (B03 guidance_table). It is left out of the quoted rows.

### 4. CONCENTRATION

- Product: management ranges only, "40–45%", "15–20%", "25–30%" of consolidated revenue (Investor_Presentation_May2026_H2FY26.pdf [page 23]). FY26 actual by product: NOT DISCLOSED (one segment, Annual_Report_2026.pdf [page 137]). Top product share: NOT DISCLOSED; management's largest range is 40-45%.
- Customer: "Our top 10 customers contribute 38.22%, 43.21%, 54.39% and 32.34% of our revenues during the Financial Year 2022-23, 2021-22, 2020-21 and period ended on September 30, 2023" (Qualitek_Final_Prospectus_Jan2024.pdf [page 278]/[page 279] risk factor 8); table: Top 5 268.49 Lakh = 21.50% and Top 10 403.92 Lakh = 32.34% for the period ended 30 Sep 2023 ([page 150]). Latest: 32.34%, H1 FY24. No later figure is filed. Top single customer: NOT DISCLOSED. The AR names Tata, Cipla, Reliance, Sun Pharma, Dr Reddy's and Patanjali as customers with no revenue share (B03).
- Geography: Annual_Report_2026.pdf [page 137], Note 29: revenue from operations "12118.75 6981.50 333.06 41.19" (Rs Lakh; Within India FY26, FY25; Outside India FY26, FY25), trade receivable 4113.19 / 2868.98 and 100.85 / 16.77. The same note says "All the revenue, trade receivables and non-current assets of the Group are located within India." The two statements conflict (B12b).
- Comment: Government and PPP dependence is NOT DISCLOSED as a share of revenue (B03).

### 5. PROMISE LEDGER

| # | Promise | Made | Status (B05) | Evidence anchor |
|---|---|---|---|---|
| 1 | Use IPO net funds of 1831.18 Lakh on capex, promoter loan repayment, working capital, general corporate purposes | Prospectus, 12 Jan 2024 | Delivered (company-reported) | Annual_Report_2026.pdf standalone Note 38 [page 188] (per B02, B05); B05 row 1 |
| 2 | 2X revenue every 2 years | May 2025 deck | Delivered by consolidation: 29.18 Cr FY24 to 124.52 Cr FY26; standalone +47% in FY26 (B05); B12b says organic is below 47% by an amount NOT FOUND | Investor_Presentation_May2025_H2FY25.pdf [page 13]; 20260520-78cbc582 [page 2] |
| 3 | 30% EBITDA margin | May 2025 deck | Missed: FY26 consolidated 23.5% | Investor_Presentation_May2025_H2FY25.pdf [page 13]; 20260520-78cbc582 |
| 4 | FY27 revenue +35-40% | 20 May 2026 | Partial: H1 FY27 +33.2%, H2 needs +36% to +45% | 20260520-78cbc582 [page 3]; 20261113-190e3152 [page 11] |
| 5 | FY27 EBITDA margin 25-27%, holding the H2 FY26 exit of 25.7% | 20 May 2026 | Missed at H1: 21.6%. B12b reads H1 as the weak half, so the full-year outcome is open | 20260520-78cbc582 [page 3]; 20261113-190e3152 [page 11] |
| 6 | FY27 PAT margin 15-17% (cut to 14-15% in the AR) | 20 May 2026 | Missed at H1: 9.1% | 20260520-78cbc582 [page 3]; Annual_Report_2026.pdf [page 23] |
| 7 | Standalone margin re-converges to historical levels | 20 May 2026 | Partial: standalone H1 FY27 25.9% (B03 derived) | 20260520-78cbc582 [page 3]; 20261113-190e3152 [page 4] |
| 8 | Net debt/EBITDA to compress from about 3.0x | 20 May 2026 | Missed at H1: about 3.6x annualised; borrowings 9,297.55 to 11,466.88 Lakh | 20261113-190e3152 [page 12] |
| 9 | USFDA pharma lab commercial; Hyderabad acquisition complete by June 2026 | May 2026 deck | Partial per B05; B12b reads Hyderabad as missed to date. No completion filing through 14 Nov 2026 | Investor_Presentation_May2026_H2FY26.pdf [page 23] |

Comment: B05 counts 2 delivered, 3 partial, 4 missed. The long-dated goals dropped from the AR (FY29 margin, FY31 overseas, FY32 debt-free) are listed in the guidance table above, not scored here. The red flag verifier grades credibility D against B05's C (B12b).

### 6. RESTATED BASES

- Quote (consolidated): "Figures for the previous year have been re-grouped/re-arranged, wherever considered necessary to confirm with the classification of current year figures." (Annual_Report_2026.pdf, end of consolidated notes, [page 143]). Reclassification detail: "For better presentation Advance Income Tax has been re-grouped from Short-term Loan and Advances in current year." (Annual_Report_2026.pdf [page 126]) and "Recoverable from employees has been re-grouped from Short-term Loans and Advances" ([page 128]).
- Quote (results): "Previous year/period figures have been re-grouped/ re-arranged, wherever necessary to confirm [sic] with classification of current year/period." (20260520-dc0311a3 [page 6], note 12; the same note 12 in 20261113-190e3152 [page 5]).
- Comment: B02 found no restatement of FY25 lines (revenue 7022.69, PAT 768.36, receivables 2885.75, goodwill 3303.78, checked against Annual_Report_2025.pdf) and only the reclassifications above. No reorganisation restatement. The comparatives are not like-for-like on scope: ITCPL is consolidated from 11 Sep 2024 in FY25 and for the full year in FY26, and the Navi Mumbai lab sits in standalone from 1 Sep 2025. Comparative as printed in the latest filing (20261113-190e3152 [page 11], consolidated, half year ended 30 Sep 2025): revenue from operations 5424.38 Lakh (the OCR text layer reads 5421.38; the PDF image and the FY26 results confirm 5,424.38, per B12a finding 1). FY26 EPS appears as 12.49 on the H1 FY27 sheet (same page) against 13.38 in the 20 May 2026 results and the deck, a disclosure conflict (B03).

### 7. CORPORATE-ACTION CLAUSES

No scheme of arrangement, demerger or merger is in the corpus, and the AR records no share repurchase. Quote: "The Company has not entered into any scheme of arrangement which has an accounting impact on current or previous financial years." (Annual_Report_2026.pdf [page 187], standalone notes). There is no scheme document to fetch from this corpus; BSE filings before 2025-11-16 may hold the ITCPL swap papers.

Corporate actions that are in the corpus:
- ITCPL share swap. Quote: "the Company has acquired the remaining 50.01% shares of ITCPL by allotting 16,72,531 equity shares of the Company to the external equity shareholders of ITCPL in the ratio of 6.56 shares for every 1 share held in ITCPL. Thus, ITCPL became a wholly-owned subsidiary of the Company w.e.f. 10th September 2025." (Annual_Report_2026.pdf [page 139], Note 33d). Aggregate consideration of Rs 8,498.99 Lakh, "paid partly in cash" (Rs 3,299.26 Lakh by subtraction from the OCR text, which reads "23,299.26") "and balance by way of allotment" (20261113-190e3152 [page 5], note 5). Of the shares, "11,70,881 equity shares to TIC Services Private Limited (Ultimate Holding Co.) in consideration of acquisition of 1,78,488 equity shares of Interstellar Testing Centre Private Limited" (Annual_Report_2026.pdf [page 134], note k). Effective date 10 Sep 2025. Liability allocation, definition of undertaking, valuation report: NOT DISCLOSED in the corpus. The filing text calls the vendors "external equity shareholders", but TIC Services is the Ultimate Holding Company (Annual_Report_2026.pdf [page 131]).
- LabOps Global. "740 equity shares representing 74% holding in LabOps Global Private Limited (LGPL) for a consideration of ₹ 0.07 Lakh at face value, paid entirely in cash ... w.e.f. 23rd May 2025" (Annual_Report_2026.pdf [page 139]).
- Navi Mumbai lab slump sale. "by way of slump sale, a food testing laboratory in Navi Mumbai, Maharashtra w.e.f. 01 September, 2025 for a lumpsum consideration of ₹ 882.00 Lakh ... net value of assets and liabilities acquired was ₹ 662.14 Lakh resulting in a Goodwill of ₹ 219.86 Lakh" (20261113-190e3152 [page 5], note 7; 20260520-dc0311a3 [page 6]). The undertaking is the one lab; no further liability clauses are printed.
- Preferential issue, approved by the board on 22 Sep 2026 and by shareholders on 16 Oct 2026. Quote: "(i) Up to 3,86,000 equity shares of face value ₹10 each fully paid-up at an issue price of ₹518.55/- per share ... aggregate consideration of up to 2001.60 Lakh ... (ii) up to 5,20,000 fully convertible share warrants at an issue price of ₹518.55/- for an aggregate consideration of up to 2696.46 Lakh ... to the persons/entities belonging to the 'Promoter & Promoter Group'" (20261113-190e3152 [page 5], note 9, text as read from the OCR layer). Warrant terms: conversion "at any time, in one or more tranches, within a period of eighteen (18) months"; the allottee pays "at least 25%" of the warrant issue price on allotment and the "balance of 75%" on conversion (20260924-fd526286 [page 4]). Relevant Date 16 Sep 2026; EGM 16 Oct 2026 (20260924-fd526286 [page 14]). Status at the run date: "The Company is awaiting in-principle approval from BSE Limited" (20261113-190e3152 [page 5]). Total of the two instruments: Rs 4,698.06 Lakh (B03).
- Objects-clause alteration to add testing, inspection and certification work: EGM on 5 Dec 2026 (20261113-c4dee558, 20261113-05e9700a; B07 catalysts). Text not re-read for this annex.
- NCD up to Rs 65 Cr: board outcome 20 Dec 2025 (20251220-0fab5880). Issue status NOT FOUND (B03).

### 8. RELATED-PARTY PERIMETER

Source: Annual_Report_2026.pdf, consolidated Note 26, [page 131] to [page 134], Rs Lakh, FY26 then FY25 in brackets. Ultimate holding company TIC Services Pvt Ltd; subsidiaries ITCPL, QTIPL, LabOps. Promoter-group and KMP-influenced entities named:

| Entity | Relationship (as printed) | FY26 transactions (Rs Lakh) |
|---|---|---|
| TIC Services Private Limited | Ultimate Holding Company | Loan repaid 88.36 (96.50); issue of shares for consideration other than cash 3640.15 (nil); corporate guarantee service charge 0.20; balance payable 0.24 |
| ASC Consulting Private Limited | Enterprise in which KMPs have significant influence | Loan taken 715.00 and repaid 715.00 (120.00 each); consulting fee 22.77 (7.64); interest paid 4.79 (2.05); loan payable 20.00 (20.00); sale of services 0.19 |
| ASC Outsourcing Private Limited | same | Manpower supply 5.26 (0.60) |
| A S C B S R And Company LLP | same | Professional fees 3.21 (3.21) |
| SKM Realcon Private Limited | same | Lease rent 153.6 (21.60); corporate guarantee charge 0.20; balance payable 0.24 (9.72) |
| AAL Biosciences Research Private Limited | same | Sale of services 37.30 (5.15); outsourcing expenses 19.12 (0.65); advance given 262.00 and recovered 262.00; loan taken 148.00, repaid 60.00; trade receivable 77.82 (33.80); unsecured loan payable 88.00 |
| AAL Research And Solution Private Limited | same | Purchase of property, plant and equipment 24.78 (9.50); advance given 148.00 (21.80), recovered 8.00; advance recoverable 151.06 (11.48) |
| Relatives of KMP: Divya Grover, Kishan Chand Grover | Relative of KMP | Employee benefit expenses 26.72 (14.00) and 10.02 (7.00); advance written-off 1.98 (Divya Grover) |
| KMPs (Nayak, Kamal Grover, Bhosale, Gupta, others) | KMP | Employee benefit expenses: Nayak 143.12 (64.26); Grover 46.36 (19.50); Bhosale 159.15 (92.89); Gupta 39.41 (20.36) |

Guarantees (notes on [page 133] and [page 134]): TIC Services 6449.00 sanctioned, 5739.65 outstanding; ASC Consulting 7446.00 and 6718.98; SKM Realcon 7664.00 and 6874.29 (also an equitable mortgage); personal guarantees by Antaryami Nayak 7583.71 and 6295.50, Kamal Grover 7525.84 and 6243.14, Alok Kumar Agarwal 7244.00 and 6212.63, Anju Agarwal 7664.00 and 6874.29. Quote: "Loans and advances to related parties are unsecured, carry an interest rate of 8.50% per annum ... the Group has waived the interest accrued on the above loans for the period April 01, 2025 to March 31, 2026" ([page 134], note i). Interest waived amount: NOT DISCLOSED.

Comment: the note says related-party transactions "have been conducted in the ordinary course of business" ([page 133]), and B02 finds that other notes state no related-party loans were given, against the 151.06 Lakh advance (B02 rank 4). Which KMP controls AAL Biosciences and AAL Research: NOT FOUND (B08).

### 9. PLEDGE AND SHAREHOLDING

Source: inputs/shareholding/screener-shareholding-pattern-extract-2026-11-15.txt (screener.in, fetched 2026-11-15; secondary extract, not the BSE filing; no page markers). The company listed on 29 Jan 2024, so fewer than twelve quarters exist, and the extract shows half-yearly points only.

| Date | Promoters | FIIs | DIIs | Public | Shareholders |
|---|---|---|---|---|---|
| Mar 2024 | 73.35% | 0.00% | 0.00% | 26.65% | 646 |
| Sep 2024 | 73.35% | 0.00% | 0.02% | 26.62% | 632 |
| Mar 2025 | 54.19% | 1.77% | 0.26% | 43.79% | 750 |
| Sep 2025 | 54.19% | 1.77% | 0.15% | 43.90% | 873 |
| Mar 2026 | 56.46% | 1.60% | 0.10% | 41.84% | 876 |
| Sep 2026 | 56.46% | 1.54% | 0.15% | 41.85% | 1,014 |

- Institutional holding latest (Sep 2026): FIIs 1.54%, DIIs 0.15%.
- Quarters not shown (Jun and Dec points): NOT DISCLOSED in the corpus; the BSE filing was blocked by a 403 bot wall (B00).
- Pledge: Quote, "have not created any encumbrance on the shares held in the Company, directly or indirectly, during the financial year ended 31st March, 2026" (20260406-e7da577b, page 1, Reg 31(4) SAST declaration covering Nayak, Alok Agarwal, Grover, TIC Services and Anju Agarwal; B08). Pledge percentage for each quarter: NOT DISCLOSED in the extract. B08 records pledge_pct_latest 0 from the declaration, not from a pattern filing.
- Comment: the promoter share fell 73.35% to 54.19% by dilution (Mar 2025) and rose to 56.46% by the share swap (Mar 2026); B08 found no promoter disposal. Ashish Kacholia holds 4.35%, rising to 5.65% after the Sep 2026 issue (20260924-fd526286 [page 15]; B08).

### 10. VERIFICATION

Documents quoted in this annex, with filename and document date:
- Annual_Report_2026.pdf (FY2025-26; BSE cover letter 3 Sep 2026)
- Annual_Report_2025.pdf (FY2024-25; BSE cover letter 3 Sep 2025; used only through the B02 spot-check figures)
- 20260520-dc0311a3-a98d-4699-a9a5-cc8f0292bda1.pdf (FY26 audited results, 20 May 2026)
- 20261113-190e3152-723f-4dd6-b960-3db581435d45.pdf (H1 FY27 results, 13 Nov 2026)
- inputs/announcements/20260520-78cbc582-e5c2-400d-b9a9-0e6e2cd444b1 (MD&A filing, 20 May 2026)
- inputs/announcements/20260924-fd526286-de9e-4a0a-ba14-9e05bdd71682 (EGM notice, 24 Sep 2026)
- inputs/announcements/20260406-e7da577b-0ea8-4d13-bb4b-eb4fe0ae1d78 (Reg 31(4) declaration, 6 Apr 2026)
- inputs/presentation/Investor_Presentation_May2026_H2FY26.pdf (21 May 2026)
- inputs/presentation/Investor_Presentation_May2025_H2FY25.pdf (May 2025)
- inputs/prospectus/Qualitek_Final_Prospectus_Jan2024.pdf (dated 12 Jan 2024)
- inputs/shareholding/screener-shareholding-pattern-extract-2026-11-15.txt (fetched 15 Nov 2026)

The inputs/ corpus itself was committed at eef459817321f370575aed243386e9d2efa68ae3 and is unchanged since. The run branch HEAD supplied for this annex is the hash below.

CORPUS COMMIT HASH: ce04e6b16b8a6297d50db9e1b14922aa89723eb5
