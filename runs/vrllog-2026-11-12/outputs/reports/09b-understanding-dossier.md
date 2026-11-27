# HALT 1 UNDERSTANDING DOSSIER: VRL Logistics Ltd (VRLLOG), run 2026-11-12

Stage 09b. Assembly from committed blocks B00 to B13 and the verifier outputs. Sections 1 to 5 hold no new research. Section 6 reads the corpus PDFs and their page-marked text copies. The dossier states no valuation and no decision. Units: Rs Cr unless the line says lakh. The annual report and the results filings state Rs lakh (100 lakh = 1 Cr). The presentation, the screener sheet and the rating note state Rs Cr.

Source-fidelity gate applied. Every Verifier A finding in 12a-errata.md was read before writing. Where a stage report carried a flagged figure, this file uses the source-truth value:
- Freight, handling and servicing cost to revenue is 59.0% in Q2 FY27 against 60.3% in Q2 FY26 (Verifier A). The 6.05% and 6.27% figures are the Hamali (loading and unloading) row, not freight.
- A 1% change in freight rate on Q2 revenue of Rs 961.9 Cr is Rs 9.62 Cr (Verifier A). The Rs 3.2 Cr figure in the stage 4 report is not used.
- Presentation page anchors for the balance sheet and cash flow are PDF p.13 and PDF p.14.
- Page anchors for concall quotes in this file are PDF pages ("[page N]" markers in the text copies). The stage 5 report used printed page numbers (one lower than the PDF page).

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

Inventory only. Source: B00 (inventory, concall_quarter_map, corpus_manifest, freshness_pairs).

1. CONCALLS (B00.concall_quarter_map)
   - Concall_Feb_2026_Transcript.pdf: Q3 FY26, call 6 Feb 2026, cover letter 10 Feb 2026.
   - Concall_May_2026_Transcript.pdf: Q4 FY26, call 19 May 2026, cover letter 22 May 2026.
   - Concall_Aug_2026_Transcript.pdf: Q1 FY27, call 5 Aug 2026, cover letter 8 Aug 2026.
   - Concall_Nov_2026_Transcript.pdf: Q2 FY27, call 5 Nov 2026, cover letter 7 Nov 2026.
   - Most recent quarter covered: Q2 FY27 (quarter ended 30 Sep 2026). Run date is 12 Nov 2026. A Q3 FY27 call is not yet due: the Q3 FY26 call was held on 6 Feb 2026 (B00), so the Q3 FY27 call is expected in early February 2027. No more recent transcript is plausibly missing.
   - Peer concalls held (outside the company folder): 12 transcripts, TCI Express, TCI and Delhivery, Q3 FY26 to Q2 FY27 (B00 inventory).
2. ANNUAL REPORTS
   - Annual_Report_2026.pdf: FY2025-26 (43rd report, AGM 4 Aug 2026).
   - Annual_Report_2025.pdf: FY2024-25 (42nd report, AGM 6 Aug 2025).
   - The latest completed FY (FY26, year to 31 Mar 2026) is present. Two years are held, so the "at least 3 years" test fails. Capex lines for FY17 to FY24 are NOT FOUND (B01 input_gaps).
3. RESULTS FILINGS
   - Results_Q4FY26_Mar2026.pdf: audited, board outcome 18 May 2026.
   - Results_Q1FY27_Jun2026.pdf: reviewed, board meeting 4 Aug 2026.
   - Results_Q2FY27_Sep2026.pdf: reviewed, board meeting 2 Nov 2026. This file is a scan with a poor OCR layer, so every figure is read from the PDF page (B00).
   - Latest filing: Q2 FY27, 2 Nov 2026. The latest AR ends 31 Mar 2026, so two quarters (Q1 and Q2 FY27) sit after it. Both are held. The Q3 FY26 results filing (quarter to 31 Dec 2025) is not held; its concall is.
4. INVESTOR PRESENTATIONS
   - Investor_Presentation_1.pdf: Q2 and H1 FY27, exchange cover letter 2 Nov 2026. It is the only presentation held. Earlier quarterly presentations are absent.
5. RESEARCH / RATING
   - ICRA_Rationale_139064.pdf: rating action dated 19 Nov 2025, outlook moved to Positive (B00). It is twelve months old. No newer ICRA rationale is listed on screener (B00).
   - research/ is empty: no broker or research note is held.
6. CORPORATE ACTIONS (17 announcement PDFs, 1 Sep 2026 to 12 Nov 2026, B00.corpus_manifest)
   - Buyback sequence: postal ballot notice (1 Sep), ISIN freeze (3 Oct), postal ballot result (6 Oct), revised record date (15 Oct), public announcement corrigendum (17 Oct), letter of offer (24 Oct), offer opening advertisement (26 Oct), post buyback advertisement (12 Nov).
   - Governance: director resignation (8 Oct).
   - Results cycle: investor meeting schedule (1 Sep), board meeting notice (24 Oct), earnings call schedule (28 Oct), results outcome and presentation cover (2 Nov), call audio link (5 Nov), transcript cover (7 Nov), conference attendance (11 Nov).
   - Three files have weak text (20261017-ff2c708b, 20261026-6bb8026d, 20261112-888c895a). No tesseract on this machine, so these were read from the PDF page.
7. FRESHNESS PAIR CHECK (B00.freshness_verdict = FRESHNESS PAIRS OK)
   - Results to concall: PASS (Q2 FY27 results with the Q2 FY27 transcript).
   - Rating bulletin to full rationale: PASS (ICRA rationale held in full).
   - SEBI order to order text: PASS (no order referenced at stage 0; stages 2, 3 and 8 re-check).
   - AR to latest audited annual results: PASS (FY26 audited results with the FY26 AR).
   - No pair failed. No missing mate to name.
   - Other corpus items: shareholding/ holds the NSE quarter master (to 30 Sep 2026) and the Sep 2026 XBRL filing. screening/ holds the screener Data Sheet (annual FY2017 to FY2026) and a TCI peer sheet.
   - Empty folders: prospectus/ (not expected, listed 2015) and research/. The stage 0 empty-folder question was suppressed under the /step1 autonomy contract, with the standing answer to continue with the gaps.
   - Screener Profit & Loss, Quarters, Balance Sheet and Cash Flow CSVs exported empty (formulas with no cached values). Only the Data Sheet is populated.
   - sector_cap_row is NOT FOUND (HIGH). No Section 1B logistics row fits an owned-fleet, low-working-capital parcel carrier. The operator rules it at the /fttcp pillar gate (B00).
   - Verifier A shadow was not run. The switch was left armed and claimed by runs/kusumgar-2026-11-12 (B00).
8. VERDICT LINE

CORPUS GAPPED: the gaps below are all missing documents or exports. No freshness pair failed.

| Missing item | Expected source | Kind |
|---|---|---|
| Screener Profit & Loss, Quarters, Balance Sheet, Cash Flow exports | screener.in export; open and save Financials.xlsx, then push again | findable-missing |
| Annual reports FY2023-24 and earlier (capex FY17 to FY24 NOT FOUND, B01) | company IR page / BSE | findable-missing |
| Q3 FY26 results filing (quarter to 31 Dec 2025) | BSE | findable-missing |
| Newer ICRA rationale, if one exists after 19 Nov 2025 | rating agency site (ICRA) | findable-missing (existence unconfirmed) |
| Bus division sale 2022: board outcome, valuation report, non-promoter vote result (B08) | BSE (Sep to Oct 2022 filings) | findable-missing |
| Reasons for independent director exits Nov 2023 and Mar 2024; FY26 AGM voting result on CMD pay (B08) | BSE | findable-missing |
| Revenue of unlisted organised carriers Safexpress, Gati, V-Trans (B09) | MCA filings / rating agency notes | findable-missing |
| Broker or research notes (research/ empty) | none published by the company | plausibly-nonexistent in corpus (operator supplies if wanted) |
| Prospectus | none; listed 2015 | plausibly-nonexistent (not expected) |

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT - PENDING OPERATOR SIGN-OFF.** Signature line: NOT SIGNED. Signing happens only in claude.ai after live-web stress-testing.

### PART A: THE FROM STATE

A1. ARCHETYPE (ARCHETYPE LIBRARY)
- LTL parcel line (90.2% of revenue, B04): Platform/network. It is the closest fit: network density (1,337 branches, 50 hubs), unit economics per tonne moved, repeat small shippers. The fit is imperfect. VRL has no take rate and owns the trucks and hubs (B04, B07).
- FTL line (8.7% of revenue, B04): fits no known archetype. It fills spare owned trucks and return trips. It has no moat (B07, B04).

A2. THE SIMPLE ANALOGY
VRL runs a bus network for parcels. A shipper with a few cartons drops them at a local branch. Parcels from many shippers share a truck to a hub, change trucks there, and a second truck takes them to the far branch. VRL owns most of the trucks, the hubs and the software, and most customers pay at booking or delivery, so VRL holds almost no unpaid bills (B04: working capital about 3% of revenue). The money comes from how many tonnes ride the network and what each tonne pays, less diesel, drivers and hub costs. Today the network is moving more tonnes at a higher rate per tonne than a year ago (B04, B05).

### PART B: THE TRANSITION

B1. FROM to TO (QUALITY LADDER), LTL line
- FROM: R2 COST-ADVANTAGED CONVERTER (nearest rung). Margin came from cost position and density. FY25 operating EBITDA margin was 18.2% and FY25 lease-inclusive ROCE was 14.4%, mid-teens (B02, B03).
- TO (claimed): R3 VALUE-ADDED / SPEC'D SUPPLIER. The claim is partial pricing power and 20-25% ROCE with stickiness. Evidence on the FY26 base: lease-inclusive ROCE 17.35% (B03). Management quotes ROCE of 30% plus on a basis that leaves out leases (B05, B03). The 30% claim would sit at R4. The model declares one rung only, because a multi-rung leap needs extraordinary proof. The model does not accept the R4 reading.
- A tier mismatch to note: R3 needs switching costs. B04 rates switching costs as weak (no contract floor, 16% of bookings on credit accounts). The FROM to TO move is therefore a pricing-power claim without a stickiness mechanism. The proof gate below tests it.
- FTL line: no transition claimed.

B2. THE ENGINE (mechanism, not narrative)
1. Realisation per tonne rose from Rs 8,079 (Q2 FY26) to Rs 8,840 (Q2 FY27), a gain of Rs 761. About Rs 471 of it (62%) reached EBITDA per tonne (B04). The rise rests on rate-card hikes since Q2 FY25, dropped low-margin contracts and smaller credit notes and discounts (B03, B04, B05).
2. Tonnage on a fixed-cost base. Volume of 1,079 thousand tonnes in Q2 FY27 is 10.6% above Q2 FY26 (B04, B05). Employee cost fell from 18.30% to 16.48% of revenue (B04), because staff and hub cost are semi-fixed. Branch additions (67 gross in H1 FY27, net +44, B07) and owned-fleet capacity (81,700 tonnes, B04) feed volume.

B3. THE PROOF GATE (binary, quarter by quarter)
The gate fires only if Q3 FY27 and Q4 FY27 each show all three of these at once (B05 triggers 1 to 3, B04 must_track_metrics, B13 falsification metric):
- tonnage growth of 9% or more year on year, and a quarterly print above the pre-reset peak of 1,104 thousand tonnes within three quarters of Q2 FY27 (B04);
- realisation per tonne at or above Rs 8,840 (B05 trigger 1);
- operating EBITDA margin, ex other income and on revenue from operations, at or above 21% (B05 trigger 2, B03 monitorable).
Until it fires, the transition is narrative and the name is research. The test is FTTCP's.

B4. THE RECOGNITION GAP (open question for Stage 11)
Does the market already price VRL at the R3 state? The corpus cannot say. Stage 11 will resolve it through the PE gap. This file states no number and no conclusion.

B5. THE UGLINESS TEST
Classification: ARTIFACT-OF-CLIMB, provisional.
- The ugly optic is the volume record: FY26 tonnage fell about 7% while revenue rose 2% (B03, B04), and H1 FY27 tonnage is still 3.0% below H1 FY25 despite a 10% rise (B04). The same optic carries a low current ratio (0.49 at March 2026, 1.00 at September 2026, B01) that B04 reads as a design choice (cash collected at booking).
- Evidence for ARTIFACT: tonnage rose 9.8% in H1 FY27 (B05), the lost-customer drag shrank from 18% to 14% of base (B05 report), and receivables are 9.7 days (B02).
- Evidence against, kept in view: 37% of FY26 revenue growth came from smaller credit notes and does not repeat (B02, B03). Peers report smaller realised rises (1.5% to 3%), so about half of the 9% is not explained by fuel (B06). Tonnage has not passed the pre-reset peak (B04).
- The classification flips to STRUCTURAL-FEATURE if tonnage growth stays under 6% for two quarters (B05 kill signal).

B6. THE TRANSITION FALSIFIER
Any one of these kills the arrow (B05 kill signals, B13):
- tonnage growth under 6% for two consecutive quarters;
- realisation per tonne falling more than 3% quarter on quarter without a matching diesel cut;
- operating EBITDA margin below 20% while realisation per tonne holds at or above Rs 8,840 (B13 falsification metric).

### PART C: WHAT THE MODEL WATCHES

C1. DOMINANT VARIABLES (Role 5.5 tracker signals)
1. Tonnage year on year on the reset base. Now: Q2 FY27 1,079 thousand tonnes (+10.6%), H1 FY27 2,099 thousand tonnes (+10%); management guide 9-10% for H2 (B04, B05).
2. Realisation per tonne against the diesel pass-through. Now: Rs 8,840 (+9% YoY, +3% QoQ); management rule Rs 2 per litre = 1% of freight; fuel explains half to two thirds of the 9% on that rule (B04, B05, B06).
3. Operating EBITDA margin ex other income, with employee cost share. Now: Q2 22.97%, H1 22.14%; employee cost 16.48% of revenue in Q2 (B03, B04). Headline 23.3% includes other income (B01, B05).
4. Net debt including leases after the buyback and capex. Now: ex-lease net debt Rs 337 Cr at September 2026 (Rs 440 Cr at March), about Rs 617 Cr after the buyback settles, leases Rs 682.5 Cr (B01).

C2. WHAT THE MODEL REJECTS
- Market size questions. The serviceable market is a floor of Rs 6,945 Cr and VRL already holds 46.4% of it (B09). The vendor figure is 13.5 times larger with an unknown definition (B09). The binding constraint is execution on the reset base (tonnage, fleet capacity, hub reach), not market size.
- The headline-margin argument (23.3% against 21-22%). It is a definition question already closed on the figures (B01, B05).
- Management's ROCE of 30% plus as a rung claim. It leaves out lease liabilities of Rs 698 Cr (B03).
- Gate 0 band movements as evidence of a climb. The framework verifier showed the GOOD label is fragile (B12c).
- The EV and CNG fleet count, the claim ratio and the proprietary ERP as drivers. None is measured (B07).

C3. THE BUSINESS FALSIFIER (re-declares the FROM business)
Evidence that the owned fleet and hub network is no longer the engine: lorry hire rising again as a share of income while the fleet count stays flat (fleet 5,932 at March 2026, 5,941 at September 2026, B03, B05 trigger 7), or net branch additions turning negative (B04), or LTL share of revenue falling away from about 90% (B04). That would move VRL from an owned-network carrier toward a broker of hired capacity. It is a different business from the one declared in A1. This differs from B6: B6 kills the climb; C3 changes the business that starts the climb.

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE (draft at Halt 1; stage 13 holds the final)

VRL Logistics moves small consignments by road across India. A shipper hands goods to one of 1,337 branches, VRL pools them with other loads at one of 50 hubs, carries them on its own trucks and delivers them at the far end (B04). Less than truckload parcel freight is 90.2% of revenue and full truckload hire is 8.7%, while courier and scrap are under 1% each (B04). A shipper with a few cartons cannot fill a truck, so a scheduled network that pools small loads is how it moves goods between states at a known rate.

The customers are more than 10 lakh businesses registered for GST (B04 report, AR p.79). The largest is 1% and the top ten are 3% of goods transport revenue (B04 report, AR p.79). Account customers are 16% of H1 FY27 bookings, and most others pay at booking or delivery (B04). There is no contract floor holding them, and management quotes 14% to 18% of customers leaving in a year while 15% to 20% join (B05 report). Textiles are 17% to 18% of volume and agri inputs 10% to 11% (B09).

Demand today is the volume of goods these businesses ship, so end-customer sector output for textiles, FMCG, agri inputs, pharma and autos is the first signal (B09 candidate: end-customer sector output). GST collections and e-way bill generation track goods movement and the shift of parcels to compliant carriers (B09 candidate: GST and e-way bills). The diesel pump price is about a quarter of cost and, by management's rule of Rs 2 per litre for 1% of freight, sets much of the rate (B09 candidate: diesel retail price).

Demand should grow through formalisation, branch reach and peer market growth. Peers show a market growing near 10% a year: TCI Express tonnage rose 7.5% and Delhivery PTL tonnage rose 14% to 18% (B06; B09 candidates: TCI Express quarterly tonnage, Delhivery PTL tonnage). MoRTH scrappage and 15-year vehicle rules may push small operators out, but they also force VRL to replace 814 of its own vehicles, 13.7% of the fleet (B03; B09 candidate: MoRTH rules). The run found no figure for how much volume moves from small operators, and the 70% unorganised share is management's claim with no source (B09). In H1 FY27 VRL grew tonnage at market pace, so it is riding the market, not yet taking share (B09, B06).

Only the LTL line shows a moat, and it is moderate. The Emerging Moat scan scored 12.8 against a floor of 12, on network density, owned land and hubs, the delivery record and the balance sheet (B07). The run did not measure the economic benefit of any of the four. Categories 21 (talent asymmetry) and 22 (cannibalisation barrier) scored zero (B07). The FTL line has no moat. Bulk diesel buying was once a cost edge but fell from 41.03% of fuel in H1 FY26 to 6.86% in H1 FY27, because bulk diesel cost more than retail (B07, B04).

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. VERTICALS FRAMED (one per dominant variable)

**Vertical 1: Tonnage on the reset base**
- The corpus establishes: tonnage Q2 FY27 1,079 thousand tonnes, +10.6% YoY; H1 FY27 +10%; H1 FY27 still 3.0% below H1 FY25 (B04). The FY27 guide changed from 10-11% (Feb) to 6-7% (May), 8% (Aug) and 9-10% (Nov) (B05). Peer tonnage: TCI Express +7.5%, Delhivery PTL +14% to +18% (B06). Fleet capacity fell from 85,261 to 81,700 tonnes (B04).
- It cannot establish: tonnage lost to dropped contracts (NOT FOUND, B05); the October +20% claim (unverifiable, B06); the organised share of the market (unsourced, B09); utilisation (NOT FOUND, B07).
- Deciding questions: (1) Is H1 growth lost volume returning or new volume? (2) Do peers and e-way bill data show the same October lift? (3) Does fleet capacity rise with tonnage, or does lorry hire fill the gap?

**Vertical 2: Realisation per tonne and the diesel pass-through**
- The corpus establishes: Rs 8,840 in Q2 FY27 against Rs 8,079 (B04). Management rule: Rs 2 per litre = 1% of freight; a pump fall of 5% or more leads to a rate rethink (B05). Peers report 1.5% to 3% realised rises (B06). Delhivery put under 30% of its PTL yield rise down to cost-linked revision (B06). On management's rule fuel explains between half and two thirds of the 9% (B06). Credit notes and discounts supplied 37% of FY26 revenue growth (B02).
- It cannot establish: how much of the rise is a rate that competitors will let stand (B06); the realised premium to unorganised operators (unverifiable, B06).
- Deciding questions: (1) What is the PPAC diesel path since April 2026 against VRL's two hikes? (2) Do peers cut rates when diesel falls? (3) Does TCI's remark that VRL takes express volume at lower rates mean a rate gap is opening?

**Vertical 3: Operating margin and the cost lines under it**
- The corpus establishes: Q2 22.97% and H1 22.14% ex other income; headline 23.3% and 22.6% include other income (B01, B03). Management gave 21-22%, 23% plus and 21% plus in one call (B05). Employee cost share fell from 18.30% to 16.48% (B04). The increment process is "under examination" with no timeline (B05). Source-truth note: freight, handling and servicing cost was 59.0% of revenue in Q2 FY27 against 60.3% in Q2 FY26; a 1% change in freight rate on Q2 revenue is Rs 9.62 Cr (12a errata).
- It cannot establish: which Q2 cost lines (staff, admin, toll) do not repeat; the Karnataka minimum wage path; a peer margin on a like-for-like basis, because VRL owns its fleet and peers hire (B06).
- Deciding questions: (1) What is the Q3 margin with and without other income? (2) When does the wage increment land and at what size? (3) What do lorry hire and repairs and maintenance do as the fleet ages (B02: trucks retired at about 85% depreciated)?

**Vertical 4: Balance sheet after the buyback and capex**
- The corpus establishes: H1 FY27 CFO Rs 362.5 Cr; capex Rs 158 Cr; ex-lease net debt Rs 337 Cr against Rs 440 Cr at March; current investments Rs 280.8 Cr held at September for the buyback; about Rs 617 Cr after settlement; leases Rs 682.5 Cr (B01). FY27 capex now points to about Rs 308-318 Cr against Rs 220-240 Cr said in August (B05, B07). The buyback funding arithmetic (Rs 500 Cr less Rs 240 Cr = Rs 260 Cr against Rs 280 Cr) does not close (B05). CFO is before about Rs 196 Cr of annual lease payments (B01).
- It cannot establish: H1 FY27 lease payments (NOT FOUND, B01); the Q3 FY27 balance sheet; dividend plans after the interim.
- Deciding questions: (1) Where does ex-lease net debt sit at 31 Dec 2026 against Rs 440 Cr? (2) What does "current level" mean in management's "flat debt" statement? (3) Did the lenders or the rating agency move after the buyback?

### 4b. CANDIDATE SIGNAL TABLE (UNVERIFIED; verification and tracker writes happen at Role 5.5 in claude.ai)

The Likely Source column carries the B09 source and its Downstream_Source_Discovery_Protocol_v1_0 type where B09 gave one.

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| GST collections and e-way bill generation | Two consecutive months of e-way bill volume growth under the growth VRL reports in tonnage, with GST goods collections flat | Monthly | GSTN / Ministry of Finance PIB releases |
| Diesel retail price (pump price) | A pump fall of 5% or more with VRL realisation not cut within a quarter (tests the Rs 2 = 1% rule); or a rise with no VRL rate step | Monthly | PPAC price series |
| TCI Express quarterly tonnage and revenue | Tonnage growth falling under VRL growth for two quarters while TCI Express rates rise (VRL growth then comes from rate, not share) | Quarterly | NSE / BSE announcements and concall transcripts (Type 1) |
| Delhivery PTL tonnage and revenue | Delhivery PTL yield growth turning negative, or PTL tonnage growth passing VRL growth by a wide margin for two quarters | Quarterly | NSE / BSE announcements, investor presentation (Type 1) |
| End-customer sector output: textiles, FMCG, agri inputs, pharma, autos | Textile or agri-input output contracting year on year while VRL reports tonnage growth above 9% | Monthly | ICRA / CRISIL industry notes, IBEF sector notes (Type 7) |
| MoRTH vehicle scrappage and 15-year vehicle rule notifications | A notification that delays or cancels the 15-year rule (removes the forced exit of small fleets) | Event-Driven | MoRTH notifications / PIB (Type 5) |

Candidate count: 6 (B09.downstream_candidates).

### 4c. FRAGILITY READ

- variable_count: 6 external variables must go right for the bull case: (1) diesel path and pass-through; (2) end-demand volume; (3) competitor rate response; (4) wage and toll cost step; (5) funding of buyback, capex and lease payments; (6) policy on scrappage, the Western DFC and rail.
- verifiability_ratio: 4 of 6 externally observable (diesel, end-demand, competitor rate response, policy). Two are company-narrated or company-filed only: the wage step (the timing is unstated, B05) and the funding path (the Q3 balance sheet is the only test, B05).
- single_point_failure: yes. Tonnage growth on the reset base. A growth rate under 6% for two quarters breaks the transition on its own, whatever happens to margin (B05 kill signal, B13 headline). Realisation per tonne is a second one-variable break for the margin leg (B05 kill signal).
- fragility_verdict: FRAGILE. The rule triggers on one kill-switch. Both kill-switches are quarterly filed numbers, so a failure would show within two prints.

### 4d. RESEARCH BRIEF (the claude.ai work order; live web the corpus cannot do)

Items 1 to 4 are the PENDING LIVE VERIFICATION links raised by the 4e chains.
1. PENDING LIVE VERIFICATION (Chain 1, who pays): open the ICRA or CRISIL sector notes on textiles and FMCG for H2 FY27 and read shipper volume and freight-rate acceptance. Textiles and agri inputs are 17-18% and 10-11% of VRL volume (B09).
2. PENDING LIVE VERIFICATION (Chain 1, why now): open the PPAC retail diesel price series for April to November 2026 and set each VRL rate step against it.
3. PENDING LIVE VERIFICATION (Chain 2, who pays): open the current ICRA rating rationale or rating action for VRL after 19 Nov 2025 (the held rationale is twelve months old).
4. PENDING LIVE VERIFICATION (Chain 2, why now): open the MCA21 charge register for VRL for new or modified bank charges in FY27, and read the lender side of the buyback and capex funding.
5. Build chains 3 to 5 to reach the Rule F floor of five: (3) fleet renewal, the 15-year rule and lorry hire (B03, B05); (4) tonnage against market growth and formalisation, using e-way bill data and peer tonnage (B06, B09); (5) wage increment, Karnataka minimum wage and the labour codes against operating leverage (B05, B06). A sixth is allowed on Western DFC and rail integration (B06).
6. Verify the 2022 and 2023 promoter stake sales (Vijay Sankeshwar 5.4% on 14 Dec 2022; Anand Sankeshwar 4% in Sep 2023) against exchange bulk-deal records. They rest on press reports (B08).
7. Retrieve the bus division sale documents (board outcome 15 Sep 2022, valuation report, non-promoter vote result) from BSE (B08).
8. Search SEBI orders and SCORES, MCA21 entity status, NCLT, eCourts and ED/SFIO. None was queried (B08).
9. Retrieve the FY26 AGM voting result on CMD reappointment and pay, and any proxy adviser note (B08).
10. Read the reason for the 7 Oct 2026 director resignation and the mismatch between the letter date (6 Oct) and the intimation (7 Oct) (B08).
11. Verify the 70% unorganised and 30% organised split with a sourced figure (B09, B06).
12. Find revenue for Safexpress, Gati and V-Trans, and the vendor LTL market definition behind Rs 3,11,610 Cr (B09).
13. Resolve the EV and CNG fleet count: AR 31 units against presentation 77 EV and 109 CNG (B07).
14. Forum archaeology: shipper complaints, claim and damage reports, and the lost-customer return that management describes (B05, B07).
15. Retrieve the Q3 FY26 results filing and older ARs (FY2023-24 and earlier) for capex, receivables and promoter holding history (B01).
16. Operator ruling needed: sector_cap_row (B00); and the two Gate 0 readings G0-07 and G0-27 named in B13.
17. Verify the status of the Rs 52 Cr CPC tax demand (section 154 order) outside the contingent table (B02 finding 2).
18. Check the stock statement filing to banks for March 2026 and later, and the database audit trail date (B03).

### 4e. SECOND-ORDER STUB (Master Prompt v3.7, Rule F)

Facts below carry block cites. Every inference carries [INFERENCE]. No new number is introduced.

```
CHAIN 1: Realisation per tonne reached Rs 8,840 in Q2 FY27, +9% YoY and +3% QoQ, with tonnage +10.6% (B04, B05)
Link 1 [filed and management claim]: The presentation prints Rs 8,840 against Rs 8,079 (B04). Management says the rise is fuel-led and passes through at Rs 2 per litre for 1% of freight, both on the way up and on the way down (B05). On that rule, fuel explains between half and two thirds of the 9% (B06). Peers report 1.5% to 3% realised rises, and Delhivery puts under 30% of its PTL yield rise down to cost-linked revision (B06). Credit notes and discounts gave 37% of FY26 revenue growth (B02, B03).
Link 2 [PENDING LIVE VERIFICATION]: Who pays, and why now. Shippers carry the rise. The corpus holds no shipper-side evidence. Claude web should open (a) the ICRA or CRISIL sector notes on textiles and FMCG for H2 FY27 to read shipper volume and rate acceptance (research brief item 1), and (b) the PPAC retail diesel series for April to November 2026 to separate fuel from non-fuel steps (research brief item 2). No counterparty fact is stated here.
Link 3 [INFERENCE]: If fuel explains only half to two thirds of the rise, the remainder is a rate the customer accepted without a contract floor (B04: switching costs weak, RPO Rs 12.73 Cr). That remainder holds only while rivals also hold rates. A diesel fall of 5% or more triggers a management rate cut under its own rule (B05), and the non-fuel part is the portion a competitor can undercut. TCI says VRL already takes express volume at lower rates (B06). The margin therefore depends on a part of the rate that has no contractual protection.
Binding constraint: Owned-fleet capacity of 81,700 tonnes, down from 85,261, with the existing fleet "utilised at an optimum level" (B04, B05). More volume needs added trucks or hired vehicles, and hired capacity costs more (B05). Employee cost per tonne has fallen, which is the other lever (B04).
Unsaid: The calls never mention that smaller credit notes and discounts gave 37% of FY26 revenue growth (B02; 05-concall.md Section 2D). They never answer ton-kilometres or lead distance (B05). They never size the lost contracts (B05).
Observation that confirms or breaks this chain, and confirm-by date: Q3 FY27 results and call, expected by 28 Feb 2027 (the Q3 FY26 call was on 6 Feb 2026, B00). Confirms: realisation at or above Rs 8,840 with tonnage growth near 9% (B05 trigger 1). Breaks: realisation down more than 3% QoQ with no matching diesel cut (B05 kill signal).
```

```
CHAIN 2: Buyback of Rs 280 Cr settled on 9 Nov 2026 while FY27 capex has moved to about Rs 308-318 Cr (B05, B07)
Link 1 [filed]: H1 FY27 CFO was Rs 362.5 Cr and H1 capex Rs 158 Cr (B01). Ex-lease net debt was Rs 337 Cr at September against Rs 440 Cr at March, after netting Rs 280.8 Cr of investments held for the buyback (B01). After settlement the run's arithmetic gives about Rs 617 Cr, with leases of Rs 682.5 Cr on top (B01). Management said year-end net debt would sit at "the same level" after capex plus buyback, and its funding sum (Rs 500 Cr less Rs 240 Cr = Rs 260 Cr against Rs 280 Cr) does not close (B05). The capex band moved three times (B05).
Link 2 [PENDING LIVE VERIFICATION]: Who pays, and why now. The lenders carry any gap. The corpus holds the ICRA rationale of 19 Nov 2025 only, twelve months old. Claude web should open (a) the current ICRA rationale or rating action for VRL after that date (research brief item 3), and (b) the MCA21 charge register for new or modified bank charges in FY27 (research brief item 4). No lender fact is stated here.
Link 3 [INFERENCE]: Management's phrase "current level" has at least three readings: Rs 391 Cr (the figure at the August call), Rs 440 Cr (March) and Rs 337 Cr (September) (B05, B01). None equals the post-settlement figure of about Rs 617 Cr. Year-end net debt can sit near any of these only if H2 cash after capex of Rs 150-160 Cr, annual lease payments of about Rs 196 Cr, and any dividend adds back to the buyback outflow. Operating cash is reported before lease payments, so the CFO figure overstates the cash available for the gap (B01). The statement is testable only on the 31 Dec 2026 balance sheet.
Binding constraint: Current ratio 0.49 at March 2026 (1.00 at September), demand facilities in current borrowings, and undrawn limits of Rs 127 Cr (B01, B03). Lease payments are fixed at about Rs 196 Cr a year (B01).
Unsaid: H1 FY27 lease payments are not in the condensed cash flow (B01). The Q2 call did not reconcile the capex band to the funding sum (B05). The calls never address the promoter non-tender and the 7 Oct director resignation (B05).
Observation that confirms or breaks this chain, and confirm-by date: Q3 FY27 results by 28 Feb 2027 (B00 call timing). Confirms: equity reduced for the buyback, EPS higher, ex-lease net debt not above Rs 440 Cr (B05 trigger 4). Breaks: net debt rising without cash flow cover (B05 kill signal).
```

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in claude.ai with live web, before Role 2.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. VRL Logistics carries small parcels by road across India. It earns 90.2% of revenue from this less-than-truckload work (B04).
2. VRL owns most of its trucks, hubs and software. It has 1,337 branches and 50 hubs, and about 5,940 vehicles (B04, B05).
3. Revenue in FY26 was Rs 3,221 Cr (B09). Working capital is about 3% of revenue, because most customers pay when they book or when goods arrive (B04).
4. More than 10 lakh businesses use VRL. The largest is 1% of goods transport revenue and the top ten are 3% (B04 report). Only 16% of bookings sit on credit accounts (B04).
5. Textile goods are 17% to 18% of volume and farm inputs 10% to 11% (B09). So VRL volume follows what these sectors ship.
6. Demand comes from the goods these firms move. The first signals to track are GST and e-way bill data, the diesel pump rate, and the tonnage that TCI Express and Delhivery report (B09).
7. Demand may grow as parcels move from small operators to carriers that comply with rules. The run found no number for this shift, and the 70% unorganised share is management's unsourced claim (B09).
8. Peers say the market grows near 10% a year, and VRL grew tonnage 10% in H1 FY27 (B06, B04). That is market pace, not clear share gain (B09).
9. The moat sits in the parcel line only, and it is moderate: network density, owned land and hubs, delivery record and balance sheet scored 12.8 against a floor of 12 (B07). The truckload line has no moat. Customers have no contract floor, so rates hold only while rivals hold theirs (B04, B06).
10. Mental model (draft): VRL is a parcel network that raised its rate per tonne and now says volume is back. The claimed climb is one rung, from cost-advantaged converter to value-added supplier. It fires only if Q3 and Q4 FY27 each show tonnage of 9% or more, realisation of Rs 8,840 or more, and operating margin of 21% or more (Section 2).
11. The thesis is FRAGILE under the stated rule. Six outside variables must go right, four can be checked outside the company, and tonnage growth alone can break it (Section 4c).
12. The corpus could not establish how much tonnage was lost to dropped contracts, how much of the 9% rate rise is fuel, or the benefit per branch or per owned hub (B05, B06, B07).
13. The corpus also lacks a sourced market size for parcel freight. The two estimates are 13.5 times apart (B09). Revenue of the unlisted carriers Safexpress, Gati and V-Trans is missing (B09).
14. Biggest open question one: is the 9% rate rise mostly fuel, or is half of it a rate rivals can undercut? Peer filings point to the second reading (B06).
15. Biggest open question two: can cash cover the Rs 280 Cr buyback and capex of about Rs 308-318 Cr without more net debt? The Q3 FY27 balance sheet is the test (B01, B05).

---

## SECTION 6: STANDING EXTRACTION ANNEX

Quote-then-comment form. Anchors are filename plus PDF page ("[page N]" marker in the text copy). Units are stated with each figure. Annual report and results figures are in Rs lakh; presentation figures are in Rs Cr. Where a figure is a sum or ratio of printed lines, it is marked DERIVED. The buyback terms below are filed clauses, not market views. Dash characters inside source quotes are shown as plain hyphens.

### 1. UNITS

- Realisation per tonne. Quote (Investor_Presentation_1.pdf, p.12, "Volume & Realisation" slide, "Realisation per ton (₹)"): series "6723 7241 7390 7944 7852 8079 8117 8147 8546 8840" for Q1 FY25 to Q2 FY27. Q2 FY27 is Rs 8,840 and Q2 FY26 is Rs 8,079.
  Comment: one figure for the whole goods transport business, so it covers a basket (LTL plus FTL), not one product. Courier and scrap sit outside it.
- Tonnage. Quote (Investor_Presentation_1.pdf, p.6): "976 1079 Q2FY26 Q2FY27" and "1911 2099 H1FY26 H1FY27", titled "Tonnage ( in '000s)". Unit: thousand tonnes.
  Comment: Q2 FY27 is 1,079 thousand tonnes, H1 FY27 is 2,099 thousand tonnes. The FY26 total of about 3,955 thousand tonnes is a sum of chart labels (B01 data_notes), not a printed total.
- Basket. Quote (Investor_Presentation_1.pdf, p.6): "H1FY27 Sales Mix (%) ... 90.4% 8.2% 1.4% LTL FTL Others". Quote (Annual_Report_2026.pdf, p.209, Rs lakh): "Full Truck Load ('FTL') ... 28,081 ... Less than Truck Load ('LTL') ... 290,468 ... Courier services ... 1,828".
  Comment: LTL, FTL and others sit in one realisation figure.
- Management also quotes per kilogram. Quote (Concall_Nov_2026_Transcript.pdf, p.6, Jainam Shah, analyst): "Our realization has improved from around INR6 per kg to around INR9 per kg as of now."
  Comment: the unit is rupees per kilogram, the same scale as Rs 6,000 to Rs 9,000 per tonne. It is the analyst's phrase, not management's.
- Derived FY26 figure: goods transport revenue Rs 318,549 lakh (Annual_Report_2026.pdf, p.209) over about 3,955 thousand tonnes is about Rs 8,054 per tonne (B04, DERIVED).
- Per-unit figures not printed: ton-kilometres, lead distance, revenue per kilometre. The calls deflected these questions in two quarters (B05). NOT DISCLOSED.

### 2. SEGMENT CAPITAL AND DEBT

- Segment note. Quote (Annual_Report_2026.pdf, p.226, Note 37): "The Company is primarily engaged into business of goods transport services. The Chief Operating Decision Maker (CODM) reviews the Company's performance as a single segment."
  Comment: there is one reportable segment, so segment assets, segment liabilities and segment capital employed are NOT DISCLOSED separately. Borrowings are unallocated and company-wide.
- Company totals, Rs lakh (Annual_Report_2026.pdf, p.170, balance sheet, 31 Mar 2026 / 31 Mar 2025):
  - "Total assets 260,514 258,567".
  - "Borrowings 13 33,414 36,723" (non-current) and "Borrowings 13 12,155 8,222" (current). Sum 45,569 and 44,945 (DERIVED).
  - "Lease liabilities 32 54,582 60,369" (non-current) and "Lease liabilities 32 15,262 17,494" (current). Sum 69,844 and 77,863 (DERIVED).
  - Equity "114,244 108,455".
- Company totals, Rs Cr (Investor_Presentation_1.pdf, p.13): Sep 2026 "Total Assets 2961.3", "Total Equity 1324.0", borrowings "446.5" (non-current) and "183.7" (current), lease liabilities "525.6" and "156.9". Sum of borrowings 630.2 and of leases 682.5 (DERIVED).
  Comment: the comparative column on that slide is headed "SEP-25" but holds the 31 Mar 2026 balance sheet. Its total assets of 2605.1 equal the AR figure of 260,514 lakh (B01 data_notes).

### 3. GUIDANCE VERSUS ASPIRATION

Classes: (a) guidance with a period; (b) aspiration without a period; (c) capacity or capability only.

| # | Quote | File and page | Class |
|---|---|---|---|
| 1 | "that will lead to at least around 10% to 11% growth in the tonnage"; "11% revenue growth, that will lead to the revenue of around INR3,600 crores in the financial year '27 ... EBITDA of around 20.5% ... INR730 crores, INR740 crores" | Concall_Feb_2026_Transcript.pdf p.7 | (a) FY27; superseded |
| 2 | "we are expecting to grow at least around 6% to 7% for the full year basis ... at least around 2% quarterly growth on a sequential basis" | Concall_May_2026_Transcript.pdf p.6 | (a) FY27; superseded |
| 3 | "Full year basis, now the expectation will be around 8%." | Concall_Aug_2026_Transcript.pdf p.7 | (a) FY27; superseded |
| 4 | "this 9%-10% growth in the volume growth will continue ... The similar growth we are expecting even in the second half of the year." | Concall_Nov_2026_Transcript.pdf p.7 | (a) H2 FY27 |
| 5 | "increasing volume of around 6% to 7% going forward in next three, four years ... EBITDA level of around 20% to 21% is maintainable, even for next 3 to 4 years." | Concall_Aug_2026_Transcript.pdf p.11 | (a) 3 to 4 years |
| 6 | "around 21%-22% is a sustainable EBITDA margin even going forward." Also "the 23% plus margin is sustainable." (p.13) | Concall_Nov_2026_Transcript.pdf p.7; p.13 | (b) no period |
| 7 | "the capital expenditure will be at least around INR250 crores-INR300 crores every year it will continue" | Concall_Nov_2026_Transcript.pdf p.7 | (b) no period |
| 8 | "the CAPEX will be around Rs. 220 crores - Rs. 240 crores, roughly, in a full year basis" | Concall_Aug_2026_Transcript.pdf p.7 | (a) FY27; moved |
| 9 | "in the second half, again, we are expecting a capital expenditure of around INR150 crores, INR160 crores" | Concall_Nov_2026_Transcript.pdf p.7 | (a) H2 FY27 |
| 10 | "the debt level will not increase ... at the end of the year, definitely, it will reach again at the same level of debt what we are having today." | Concall_Aug_2026_Transcript.pdf p.7 | (a) FY27 |
| 11 | "this year we are expecting our ROCE will be at least around 30% plus." | Concall_Nov_2026_Transcript.pdf p.10 | (a) FY27 |
| 12 | "we can expect at least around 10%-12% growth in the revenue. Assume that there will not be no price realization change" | Concall_Nov_2026_Transcript.pdf p.13 | (a) next year, conditional |
| 13 | "Net branches itself, we are expecting at least around 100 numbers in the coming year." | Concall_May_2026_Transcript.pdf p.9 | (a) FY27 |
| 14 | "out of these 500 vehicles, around 100 vehicles have been already delivered in the month of January." | Concall_Feb_2026_Transcript.pdf p.4 | (a) CY2026 (500-vehicle plan); count not updated |
| 15 | "If any reduction on the fuel price, that too in a substantial number, at least around 5%, more than 5% or so, then definitely we have to rethink on the freight rates." | Concall_Nov_2026_Transcript.pdf p.11 | (b) no period (rule of conduct) |
| 16 | "we are looking for further expansion in the fleet, basically on higher capacity vehicles ... overall capacity increase will be more or less equivalent to our tonnage growth." | Concall_Nov_2026_Transcript.pdf p.10 | (c) capacity |
| 17 | "up to INR280 crores at a price of INR320 per equity share ... up to 87.5 lakh equity shares, representing approximately 5%" | Concall_Nov_2026_Transcript.pdf p.5 | (a) Oct to Nov 2026; executed (settlement 9 Nov) |

Comments: rows 1 to 3 show the FY27 tonnage guide changed three times; the May cut came with no stated reason (B05). Row 6 is margin stated three ways in one call (B05). Row 13: the transcript says "net". The stage 5 summary and B07 count 67 gross and 44 net additions in H1 FY27, against "at least around 100" net (B07). Row 8 does not reconcile with rows 9 and 7: H1 capex Rs 158 Cr plus H2 Rs 150-160 Cr is Rs 308-318 Cr (B05, DERIVED).

### 4. CONCENTRATION

- Customer. Quote (Annual_Report_2026.pdf, p.79): "the Company's largest customer and the top 10 customers put together contributed only 1% and 3% of the revenues of the Goods Transport business respectively." Also "a very well diversified customer base of ~10 lakhs plus".
  Comment: largest customer 1%, top ten 3%. Account customers were 16% of H1 FY27 bookings (B04 report, presentation p.22).
- Product. Quote (Annual_Report_2026.pdf, p.209, Rs lakh): "Less than Truck Load ('LTL') 290,468" of total "320,377". LTL is 90.7% of revenue from contracts with customers (DERIVED); B04 reports 90.2% of revenue from operations of Rs 322,111 lakh. By commodity, quote (Concall_May_2026_Transcript.pdf, p.12): "textile and cloths industry ... contribution f rom this facility is around 17% to 18%" and "agricultural ... around 10% to 11%".
  Comment: the top product line is LTL. The top commodity is textiles at 17% to 18%. No commodity is in a filed table; both figures are management statements.
- Geography. Quote (Annual_Report_2026.pdf, p.209): "India 320,377 ... Outside India -". Quote (p.122): "operations are spread across 23 States and 5 Union Territories. There is no single area or office with significant business concentration."
  Comment: 100% India. Revenue by state is NOT DISCLOSED.

### 5. PROMISE LEDGER

Promise dates are the call dates. Rows marked (V) were checked in this stage against the call PDF text (PDF page). Other rows use the stage 5 report (05-concall.md Section 2A, row number), which used printed page numbers, one lower than the PDF page on the Q1 and Q2 FY27 calls. Evidence anchors: Investor_Presentation_1.pdf ("Pres.") and the Q2 FY27 transcript.

| # | Made | Promise | Status | Evidence anchor |
|---|---|---|---|---|
| 1 | 6 Feb 2026 | Q4 FY26 tonnage +3-4% QoQ | Delivered (about +5.5% daily tonnage QoQ) | 05-concall.md row 1; Q4 FY26 call |
| 2 | 6 Feb 2026 | Realisation held at Q4 exit | Delivered (Rs 8,147 vs Rs 8,117) | Pres. p.12; row 2 |
| 3 | 6 Feb 2026 | FY27 tonnage +10-11% (V, Feb p.7) | Missed as guided: cut to 6-7% in May with no reason stated | Concall_May p.6 (V); row 3 |
| 4 | 6 Feb 2026 | FY27 EBITDA about 20.5% (V, Feb p.7) | Delivered: Q1 21.76%, Q2 23.34% | Pres. p.10 |
| 5 | 6 Feb 2026 | No rate change unless costs change substantially | Partial: about 9% fuel-led rise | Pres. p.8; row 5 |
| 6 | 6 Feb 2026 | 500 vehicles by Dec 2026 (V, Feb p.4) | Partial: 100 delivered by Jan; fleet 5,941 at Sep vs 5,932 at March | Concall_Nov p.5 (V); B03 |
| 7 | 6 Feb 2026 | No wage increment before March 2027 | Partial: Nov says increment process under examination (V, Nov p.11) | row 7 |
| 8 | 19 May 2026 | Q1 margin 21% plus, fuel passed through within a month | Delivered: Q1 21.76% | Pres. p.10 |
| 9 | 19 May 2026 | FY27 tonnage 6-7% (V, May p.6) | Delivered, beaten: H1 +10% | Pres. p.6 |
| 10 | 19 May 2026 | At least 2% sequential tonnage growth each quarter (V, May p.6) | Missed in Q1 (-1.73%), met in Q2 (+5.9%, DERIVED) | Pres. p.12 chart; row 10 |
| 11 | 19 May 2026 | At least 100 net branches in FY27 (V, May p.9) | Partial: 67 gross, 44 net in H1 | B07 (Pres. p.16) |
| 12 | 19 May 2026 | Fuel pass-through lag within a month | Delivered: Q1 realisation +5% QoQ | Pres. p.12 |
| 13 | 5 Aug 2026 | Q2 tonnage about 9% YoY | Delivered: +10.6% (DERIVED) | Pres. p.6 |
| 14 | 5 Aug 2026 | FY27 tonnage about 8% (V, Aug p.7) | Delivered, beaten: H1 +10%, H2 guided 9-10% | Pres. p.6; Concall_Nov p.7 |
| 15 | 5 Aug 2026 | Realisation Rs 8,546 holds or improves | Delivered: Rs 8,840 | Pres. p.12 |
| 16 | 5 Aug 2026 | EBITDA 20-21% maintainable (V, Aug p.11) | Delivered: 23.34% in Q2 (headline basis, includes other income) | Pres. p.9 |
| 17 | 5 Aug 2026 | FY27 capex Rs 220-240 Cr and year-end debt flat (V, Aug p.7) | Missed on capex: H1 Rs 158 Cr plus H2 Rs 150-160 Cr (DERIVED Rs 308-318 Cr); debt claim open to Q3 FY27 | Concall_Nov p.7, p.12 |
| 18 | 5 Aug 2026 | Buyback Rs 280 Cr, promoters not tendering | Delivered: window closed 2 Nov, settlement 9 Nov | Concall_Nov p.5-6 (V); Letter of Offer p.20 |

Totals (B05): 11 delivered, 4 partial, 3 missed. Credibility grade B.

### 6. RESTATED BASES

- Ratios re-based. Quote (Annual_Report_2026.pdf, p.225, Note 36): "Debt - equity ratio Times Debt Net worth 0.40 0.41" and "Debt service coverage ratio ... 1.60 1.47". Definition (p.226): "Debt = Non current borrowings + Current borrowings".
  The comparative as printed in the FY25 AR (Annual_Report_2025.pdf, p.224): "Debt - equity Ratio 1.13 1.10 3.24%" and "Debt Service Coverage Ratio 0.40 0.34 17.65%", with the definition "Debt - Equity Ratio = (Total Borrowings + Total Lease Liabilities + Accrued Interest Payable) / Shareholders' Equity".
  Comment: leases left "debt" in FY26, so the FY25 comparative moved from 1.13 to 0.41 and DSCR from 0.40 to 1.47. The FY26 AR gives the new definition but no note on the change. Disclosed ROCE of 24.56% (p.225) also leaves out lease liabilities; the lease-inclusive figure is 17.35% (B03, DERIVED).
- Cash classification. Quote (Annual_Report_2026.pdf, p.199, Note 13): "As at 31 March 2025, the balance was classified under 'cash and cash equivalents'" (the ICICI demand loan and the cash credit). The FY25 column is not restated and the effect is not quantified (B02).
- Regrouping. Quote (Annual_Report_2026.pdf, p.227, Note 41): "Previous year figures have been regrouped, reclassified and rearranged wherever necessary, to conform to this year's presentation, and these are not material to the financial statements."
- Bonus. Quote (Annual_Report_2026.pdf, p.213): "the figures of earnings per share presented have been restated to give the effect of allotment of bonus shares." Diluted EPS is Rs 13.54 (FY26) and Rs 10.46 (FY25, restated). See also p.53: "87468495 Equity shares ... Bonus Shares in the ratio of 1:1".
- Presentation comparatives (Investor_Presentation_1.pdf, p.13): the balance sheet column headed "SEP-25" holds the 31 Mar 2026 balance sheet (B01 data_notes).
- Q2 FY27 results face comparatives: the PDF is a scan; no restatement note was read there. NOT ESTABLISHED in this stage.

### 7. CORPORATE-ACTION CLAUSES

- Buyback (the one live action). File: announcements/20261024-44aad60b-60ec-4107-8538-3bfea948117d.pdf (Letter of Offer dated 24 Oct 2026).
  - Dates. Quote (p.2): "Buyback Window Opening Date Tuesday, October 27, 2026 ... Buyback Window Closing Date Monday, November 02, 2026". Quote (p.6): "Last date of payment of consideration to Eligible Shareholders who participated in the Buyback November 09, 2026 Monday". Record date: October 22, 2026 (p.1).
  - Size and rate. Quote (p.1): "UP TO 87,50,000 (EIGHTY SEVEN LAKHS FIFTY THOUSAND ONLY) FULLY PAID-UP EQUITY SHARES OF FACE VALUE OF ₹ 10" and "THROUGH THE TENDER OFFER ROUTE AT A PRICE OF ₹ 320/- ... PER EQUITY SHARE PAYABLE IN CASH FOR AN AGGREGATE CONSIDERATION OF UP TO ₹28,000 LAKHS". The route is a tender offer, proportionate, with a small shareholder reservation.
  - Ratios. Quote (p.2): "RESERVED CATEGORY FOR SMALL SHAREHOLDERS 14 Equity Share for every 99 Equity Shares held" and "GENERAL CATEGORY FOR ALL OTHER ELIGIBLE SHAREHOLDERS 19 Equity Share for every 154 Equity Shares held".
  - Promoter clause. Quote (p.20, para 11.2): "the Promoter and Promoter group have expressed their intention to not participate in the Buyback vide their letters August 04, 2026 ... shall increase to 63.41% of the post-Buyback total paid-up Equity Share capital of the Company from 60.24%".
  - Size limit. The Letter of Offer states the size of "₹ 28000 Lakhs (Rupees Twenty Eight Thousand lakhs only)" and that it "does not exceed 25% of the aggregate" paid-up capital and free reserves (declaration, line 796 of the text copy).
  Comment: no undertaking transfer or liability allocation applies to a buyback. The 3.94 times subscription and the 25.02% share taken by HDFC Small Cap come from the post buyback advertisement of 12 Nov 2026 (B08). That file's text layer is weak, so those two figures rest on B08.
- Bonus issue FY26. Quote (Annual_Report_2026.pdf, p.53): "issued 87468495 Equity shares of Rs.10/- each fully paid by way of Bonus Shares in the ratio of 1:1, increasing the paid-up capital of the Company from Rs. 87,46,84,950/- to Rs.174,93,69,900/-".
- Bus division sale to promoter company Vijayanand Travels (Sep 2022, Rs 230 Cr, B08) and the air business sale (Rs 1,700 lakh, FY24): not in the corpus as a scheme. The FY25 AR shows only the effect. Quote (Annual_Report_2025.pdf, p.220): "Sale of Transportation of Passengers by Air Operations Vijayanand Travels Private Limited ... - 1700.00". File to fetch: the BSE board outcome of 15 Sep 2022, the postal ballot notice and result, and the valuation report.
- No demerger, merger or preferential issue is in the corpus.

### 8. RELATED-PARTY PERIMETER

- FY26 AR, Note 35 (Annual_Report_2026.pdf, p.223-224, Rs lakh). Entities named (p.223): Vijayanand Foods Private Limited; VRL Steel Private Limited; Vijayanand Logistics Private Limited (struck off); Vijayanand Infotech Private Limited; Vijayanand Travels Private Limited; VRL Media Private Limited; Vijaykant Dairy And Food Products Limited; Sankeshwar Minerals Private Limited; Sankeshwar Printer Private Limited; Hyperkonnect Technologies Private Limited; VRL Foundation; Aradhana Trust; Shri Ayyappa Bhakta Vrunda Trust; Karnataka Cancer Therapy and Research Institute.
- Quote, amounts by nature, all with the relationship "Enterprise in which KMP or their close family members have control or significant influence" (FY26 / FY25): goods transport services 337 / 202; rental income 323 / 226; sale of spares and services 18 / 153; sale of PPE 10 / 1,488; lorry hire 76 / 80; travelling and conveyance 535 / 113; printing and stationery 81 / 87; advertisement 4 / 5; purchase of PPE 15 / nil; rent 76 / 13.
  Comment: the FY26 note no longer names the counterparty line by line, so amounts cannot be tied to named entities. NOT DISCLOSED per entity. Total flows are 0.46% of revenue (B08). Note text: "There have been no guarantees received or provided for any related party" (p.224) and "All the related party transactions are made on terms equivalent to those that prevail in an arm's length transaction".
- Per-entity detail exists only for FY25 (Annual_Report_2025.pdf, p.220-222, Rs lakh, FY25 / FY24): rent income, VRL Media 216.94 / 185.37, Vijayanand Travels 5.48 / 6.34; freight income, VRL Media 178.04 / 131.66; sale of spares, Vijayakant Dairy 141.39 / nil; sale of air operations, Vijayanand Travels nil / 1700.00; sale of PPE, Vijayanand Travels 1488.00 / nil; directors' travelling expense, Vijayanand Travels 112.88 / 149.19; printing, Sankeshwar Printers 87.37 / 63.13; courier hire, Vijayanand Travels 79.28 / 80.98.
  Comment: the FY26 line "Travelling and conveyance 535" against 113 is a fivefold step with no counterparty named. Whether VRL leases property from promoter entities under Ind AS 116 is not shown (B02). The Karnataka Cancer Therapy and Research Institute is new to the list and shows no FY26 transaction (B03).
- Key management pay. Quote (Annual_Report_2026.pdf, p.224): "(i) Short term employee benefits ... 1,416 ... 1,342" (FY26 / FY25).

### 9. PLEDGE AND SHAREHOLDING

- Promoter holding as filed (SHP_master_NSE.txt, columns "quarter_end | promoter_and_group_% | public_%"): each of 31-MAR-2024, 30-JUN-2024, 30-SEP-2024, 31-DEC-2024, 31-MAR-2025, 30-JUN-2025, 30-SEP-2025, 31-DEC-2025, 31-MAR-2026, 30-JUN-2026 and 30-SEP-2026 prints "60.24 | 39.76". The master also carries an 18-AUG-2025 row at "60.24 | 39.76".
  Comment: the master holds eleven quarter-ends from March 2024 to September 2026, plus the August 2025 row, which makes twelve rows. A full twelve quarters needs December 2023, which the master does not list (NOT FOUND). Holding is flat at 60.24% across the span. The 105,381,942 promoter shares are confirmed in the Sep 2026 XBRL. B08 counts twelve rows as "12 quarters"; the quarter-end count is eleven.
- Pledge. Quote (SHP_Sep2026_NSE_xbrl.txt): "WhetherAnySharesHeldByPromotersAreEncumberedUnderPledged contextRef="MainI">false". Quote (Annual_Report_2026.pdf, p.150): "No pledge has been created over the equity shares held by either Promoters and / or Promoter Group".
  Comment: pledge is nil at 31 Mar 2026 and 30 Sep 2026. The master has no pledge column, so the pledge for the other quarters is NOT DISCLOSED in the files held (B08 reads it as stable at 0%).
- Institutional holding, latest (SHP_Sep2026_NSE_xbrl.txt, quarter to 30 Sep 2026, ShareholdingAsAPercentageOfTotalNumberOfShares): Mutual Funds or UTI "0.2368" (41,433,312 shares); Institutions Domestic "0.245" (42,867,356 shares); FPI Category One "0.0322"; FPI Category Two "0.0047"; Institutions Foreign "0.0369" (6,452,487 shares).
  Comment: mutual funds hold 23.68%, domestic institutions 24.50% and foreign institutions 3.69%. The XBRL lines read do not print a single combined institutional total, so none is stated. HDFC Small Cap took 25.02% of the accepted buyback shares (B08, from the 12 Nov 2026 advertisement).

### 10. VERIFICATION

Documents quoted in this annex, with filename and the document date:
- Investor_Presentation_1.pdf: Q2 and H1 FY27, cover letter 2 Nov 2026.
- Annual_Report_2026.pdf: FY2025-26, financials signed 18 May 2026, AGM 4 Aug 2026.
- Annual_Report_2025.pdf: FY2024-25, AGM 6 Aug 2025.
- Concall_Feb_2026_Transcript.pdf: call 6 Feb 2026 (cover 10 Feb 2026).
- Concall_May_2026_Transcript.pdf: call 19 May 2026 (cover 22 May 2026).
- Concall_Aug_2026_Transcript.pdf: call 5 Aug 2026 (cover 8 Aug 2026).
- Concall_Nov_2026_Transcript.pdf: call 5 Nov 2026 (cover 7 Nov 2026).
- announcements/20261024-44aad60b-60ec-4107-8538-3bfea948117d.pdf: Letter of Offer, 24 Oct 2026.
- SHP_master_NSE.txt: NSE master fetched 12 Nov 2026, latest quarter 30 Sep 2026.
- SHP_Sep2026_NSE_xbrl.txt: XBRL filing for the quarter to 30 Sep 2026, submitted 13 Oct 2026.
- Stage reports used for B-block facts: 04-bizmodel.md, 05-concall.md, 12a-errata.md (run 2026-11-12).

CORPUS COMMIT HASH: e35c4a6931979bde84300b532fbad9bc061eeaff
