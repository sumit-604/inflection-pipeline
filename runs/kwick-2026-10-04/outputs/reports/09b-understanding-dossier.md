# KWICK: Halt 1 Understanding Dossier (stage 09b)

Company: Kwick Forensic Solutions Ltd (KWICK, BSE SME 544895, listed 2026-09-03)
Run date: 2026-10-04
Units: All figures in Rs Cr unless the source says otherwise. The source unit is on the face of the document. The prospectus reports in Rs lakh (1 Cr = 100 lakh). Where a figure stays in Rs lakh, the text says so.
Mode: assembly from committed blocks B00 to B09 and verifier blocks B12a, B12b, B12c (phase 1 partial), B12d, plus confidence.yaml. Section 6 reads the corpus files for exact quotes. This file holds no valuation and no decision. Source fidelity correction carried: the 09-tam anchors "prospectus p.265" are wrong; use p.150, p.24 and p.264 (B12a MAJOR).
Basis note: B04 and B05 label the 27.06% margin "on COGS". Prospectus p.257 prints "Cost of goods sold as % of revenue from operations (%) 72.94%", so 27.06% is a margin on revenue (B12b). This file uses "gross margin on revenue".

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

Inventory only. Every line traces to B00 (inputs, inventory, freshness_pairs).

1. CONCALLS: ABSENT. Zero transcripts. B00 sets concalls_available false (no earnings call; listed one month). The 30-Sep-2026 Arihant investor conference left no transcript (B00 input_gaps). Most recent quarter covered: none. The first filing will be H1 FY27, so no reported quarter exists whose transcript could be missing. Peer calls are held for structure only: ZENTEC 4 (Oct-2025, Feb-2026, May-2026, Jul-2026), ADSL 4 (Nov-2025, Feb-2026, May-2026, Aug-2026), DSSL 3 (Feb-2026, Jun-2026, Aug-2026) (B00).
2. ANNUAL REPORTS: ABSENT. No annual report of any year is held. The latest completed FY (FY2025-26, year to 31-Mar-2026) is not present. Fewer than 3 years are held (zero). The substitute is the Final Prospectus dated 31-Aug-2026, 383 pages, Rs lakh, restated FY24 to FY26 (KWICK-Prospectus-2026-08-31.pdf) (B00). Directors' report, CARO, auditor's report with key audit matters and prior-year annual reports are not available (B03 input_gaps).
3. RESULTS FILINGS: ABSENT. No exchange results exist. The first filing is H1 FY27. The trading window closed 2026-10-01 (BSE filing 2026-09-28) (B00). FY24 to FY26 audited figures come from the prospectus restated statements only. No quarter-gap can be measured because no results filing and no annual report exist.
4. INVESTOR PRESENTATIONS: PRESENT. Investor_Presentation_1.pdf, the 22-page Arihant conference deck filed under Reg 30 on 2026-09-30, duplicated as announcements/20260930-4e7a525d-36ad-47cc-82ca-23adea2c95ab.pdf. Also KWICK-Product-Catalogue-2026.pdf (32 pages, company website, 2026) (B00). B04 rates the deck unreliable (customers 130 against 95; PBT 1,921.45 against 1,821.45 lakh).
5. RESEARCH / RATING: ABSENT. No broker note. No rating. Prospectus p.64 states: "As the Offer is of Equity Shares, the appointment of a credit rating agency is not required." No bank-facility rating found (B00).
6. CORPORATE ACTIONS: PARTIAL. Six BSE filings dated 2026-09-24 to 2026-09-30: conference intimation (09-24), market-movement clarification (09-26), Reg 30 note on the NFSU Varanasi campus (09-27), trading window closure (09-28), conference presentation (09-30), conference outcome (09-30). Plus SEBI order WTM/AS/CFD/CFD-SEC-5/32665/2026-27 dated 2026-08-18 against the lead manager, a regulator document held in announcements/ (B00). Filings from listing day 2026-09-03 to 2026-09-23 were not staged. B00 names a possible collector selection gap.
7. FRESHNESS PAIR CHECK (B00 freshness_pairs). Pair 1 RESULTS to CONCALL: SKIPPED (no results filing). Pair 2 RATING BULLETIN to RATIONALE: SKIPPED (no rating exists). Pair 3 SEBI ORDER to ORDER TEXT: PASS (order text fetched from sebi.gov.in into inputs/announcements/SEBI-Order-CCVPL-2026-08-18.pdf, 19 pages). Pair 4 AR to LATEST AUDITED ANNUAL RESULTS: FAILED. Trigger document held: prospectus restated financial information including audited FY2025-26. Mate absent: Kwick Forensic Solutions Ltd Annual Report FY2025-26 (directors' report, CARO, full audited notes). Expected source: BSE filing (Reg 34 or AGM notice), or kwickforensic.com/Home/Financial_Information?type=AnnualReport, which was empty on 2026-10-04 (B00). The orchestrator applies the downstream consequence of a failed pair. This dossier does not restate it.
   Empty folders the /step1 autonomy contract accepted as gaps without asking (B00 empty_folder_confirmation): annual-report, results, rating, concalls (declared), shareholding, research.
   Other gaps (B00): the shareholding folder is empty because the BSE API returned Access Denied on 2026-10-04. The Sep-2026 pattern (promoters 64.65%, FII 1.49%, DII 10.85%) is web, non-anchored. Screener sheets Profit & Loss, Quarters, Balance Sheet, Cash Flow and Customization came out empty for KWICK and the three peers; Data_Sheet.csv is populated for all four.
8. VERDICT LINE:

CORPUS GAPPED-FRESHNESS: missing mate document first, Kwick Forensic Solutions Ltd Annual Report FY2025-26 (BSE Reg 34 filing or company IR page). Further gaps: shareholding pattern (BSE, findable-missing, API blocked); BSE announcements 2026-09-03 to 2026-09-23 (BSE, findable-missing); H1 FY27 results, any rating, any concall and any broker note (plausibly-nonexistent for now: first filing not yet due, an equity issue needs no rating, no call held; the absence is itself a data point for opacity).

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT - PENDING OPERATOR SIGN-OFF**

Signing happens only in claude.ai after live-web stress testing. Nothing here is signed.

### PART A: THE FROM STATE

**A1. ARCHETYPE** (CLAUDE.md ARCHETYPE LIBRARY)
- Lines 1 to 4 (physical evidence kits 36.99%, cyber and digital forensics 33.32%, DNA forensics 10.76%, Mobile CSI vehicles and kits 10.00%; goods 91.08% of FY26 revenue): Order-book business. Tender and GeM procurement, working-capital heavy, execution pace and working capital decide the result (B04 revenue_streams, wc_intensity high, pricing_power weak). Fit is partial: the filings show no order book (B05, B07 input_gaps).
- Rental line (8.75%, equal to one customer, the Government of Bihar): fits no known archetype. Nearest is Outsourcing partner (contract stickiness) (B04 FLAG-CONCENTRATION, B09 candidate 4).
- AMC and other services (0.17%) carries no weight in the model (B04).

**A2. THE SIMPLE ANALOGY.** Kwick is a specialist trade supplier to the police. A state police force or forensic lab needs kits, scanners and lab tools that come mostly from foreign makers. Kwick holds non-exclusive supply rights with those makers (B04 moats_present). It bundles the items, bids for the contract on the government tender portal, wins at the lowest compliant bid, delivers, and waits for the state to pay (B05 triggers, B07 R1 note). It owns no plant. It runs on 33 payroll staff and a six-person sales team (B03 missing_risks; text prints 34, table 33). Think of a well-run wholesaler with one big edge, a new law that makes its customers shop. The wholesaler has not yet shown that it keeps more of each rupee as it grows. Gross margin on revenue fell from 37.30% to 27.06% in two years while EBITDA margin held at 18% (B04). That is where the arrow starts.

### PART B: THE TRANSITION

**B1. FROM TO TO** (CLAUDE.md QUALITY LADDER)
- Line: in-house devices and E-Forensics software layered on the resale base. This is the only line the filings present as a move upward. Revenue by in-house product is NOT FOUND (B07 input_gaps).
- FROM: R1 COMMODITY PRICE-TAKER. Lowest compliant tender price, pricing power weak, margin falling (B04). Spot ROCE 44.88% sits on a cash-heavy base and is not durable ROCE (B02 rank 12). The operator may rule R1 to R2 instead; the ladder says a business can sit between rungs.
- TO as implied by the filings' in-house narrative: R3 VALUE-ADDED / SPEC'D SUPPLIER (prospectus pp.151-152 as carried in B05 triggers 6 and B07 optionality_register). The company states no tier. R3 is the tier the narrative implies. R1 to R3 is a two-rung move. The ladder rule says a multi-rung leap needs extraordinary proof and is itself a red flag. No such proof exists in the corpus (B07 EM 11.6, classification NONE).
- Lines 1 to 4 and rental: no transition claimed.

**B2. THE ENGINE.** Two things must physically change (B05 triggers 3 and 6, B07 optionality_register, B04 key_lever):
1. Revenue mix moves to own products. The E-Forensics software (software CWIP 137.17 lakh, no commissioning date, B02 rank 6) must be commissioned and receive a first priced order. The handhelds (8D and 4D, not yet commercialised, B07) must make a first invoiced sale.
2. Gross margin on revenue must stop falling. Opex fell from 19.52% to 9.11% of revenue and carried EBITDA margin flat. That cushion is nearly spent (B04 FLAG-GM-COMPRESSION), so any further gross margin loss reaches EBITDA.
The mechanism is margin per rupee of revenue, not revenue size.

**B3. THE PROOF GATE.** Binary, read half-year by half-year once filings exist (B03 monitorables, B04 must_track_metrics, B12b basis correction):
- Gross margin on revenue at or above 27% in H1 FY27 (FY26: 27.06%, prospectus p.257), with revenue from in-house products shown as its own line and gross margin by line disclosed.
- CFO/PAT at or above 0.8 in H1 FY27 (FY26: 0.56x, B01 block_b_trend).
- Year-end receivable days at or below 80 (FY26 year-end: 79; B03 monitorables).
All three must hold in H1 FY27 and in the following half. Until they do, the transition is narrative. The gate has not fired (B03 best_fit_strategy, B13 gate recommendation).

**B4. THE RECOGNITION GAP (open question for Stage 11).** Does the TO state already look reflected in market pricing? This dossier does not conclude. Stage 11 confirms or denies it through the PE gap. If the TO state is already priced, the re-rating engine is spent and only earnings growth remains. Stage 11 has not run.

**B5. THE UGLINESS TEST.** Provisional classification: STRUCTURAL-FEATURE. The classification rests on today's evidence and Stage 13 may overturn it.
- Evidence for STRUCTURAL: pricing power weak (B04). No moat found (EM 11.6 NONE, 0.4 below the MODEST line, B07). Gross margin on revenue fell three years running, and domestic sourcing, the promised margin lever, did not lift it (B05 promise row 3, MISSED). Peers hold working capital low with supplier credit, and Kwick plans the opposite, creditor days 44 to 30 (B06 FLAG-SUPPLIER-CREDIT-DIVERGENCE). Cash conversion has stayed near half of profit (B01 DB4).
- Evidence for ARTIFACT-OF-CLIMB: debtor days improved on both bases while revenue rose 3.5x (average basis 83 / 89 / 74, year-end 144 / 111 / 79; B01 LBF-2). Over-six-month dues fell to 11.85% of gross (B02 receivables_trend). That fits growth that ate cash.
- The two readings: growth absorbed the cash and it returns as growth slows, or a tender reseller with weak supplier terms never converts much better. The observation that separates them: H1 FY27 CFO/PAT and trade receivables growth against revenue growth (B13 falsification line). The matrix row for proof NOT FIRED plus STRUCTURAL is VALUE-TRAP RISK (CLAUDE.md). The operator sets the posture at sign-off. B13 records the posture as NOT CLASSIFIED.

**B6. THE TRANSITION FALSIFIER.** Any one of these kills the arrow (B03 monitorables, B04 first_deterioration_signals, B05 kill signals):
- H1 FY27 gross margin on revenue below 25% (B04 red_flag) with CFO/PAT at or below 0.56x and trade receivables growing faster than revenue.
- No in-house product revenue line and no commissioning date for the Rs 1.37 Cr software by the H1 FY27 results (B05 trigger 6 kill signal, B07).
- No Reg 30 filing ties NFSU, MHA or a state to a named Kwick order by the H1 FY27 results (B05 trigger 7 kill signal).

### PART C: WHAT THE MODEL WATCHES

**C1. DOMINANT VARIABLES** (these become the Role 5.5 tracker signals)
1. Gross margin on revenue and in-house product revenue. Now 37.30 / 31.15 / 27.06% (prospectus p.257 via B05). Opex already 9.11% of revenue (B04). Segment margins NOT FOUND.
2. Cash conversion and working capital. CFO/PAT -0.92x / 0.54x / 0.56x; FY27 working-capital need Rs 44.42 Cr, IPO funds Rs 31.42 Cr (B01, B05 guidance). Cash determination INDETERMINATE (B13).
3. Customer identity and repeat. Non-government revenue Rs 47.34 Cr (44.78%), of which Rs 20.36 Cr is dealer-route kits for 95 vehicles equal to Top Customers 2 and 4 (B12b); Rs 26.98 Cr has no named customer (B13 gate note 3). Top customer 23.59%, top 10 77.64% (B03). Customers served 128 / 124 / 95 (B05).
4. Scheme demand continuity. SMFC (Rs 2,080.5 Cr, vans and state lab kit) ran FY22 to FY26 and ended 2026-03-31; successor NOT FOUND (B09 FLAG-SCHEME-CLIFF). Kwick scheme-linked revenue is about 18.9% of the Rs 416 Cr scheme floor (B09, an inference).

**C2. WHAT THE MODEL REJECTS.**
- The Rs 30,000 crore headline. It is a five-year Centre and States announcement, 6.5x the conservative five-year pool, not an equipment market (B09 FLAG-MGMT-CLAIM-INFLATED). The binding constraint is working capital and execution, not market size (B09 capacity_check).
- The headline debtor days of 74. Use year-end 79 and the ageing (B04 irrelevant_ratios).
- Spot ROCE 44.88% and fixed asset turnover 32.77x. The business is asset-light and supplier-funded (B04).
- Government share as a quality verdict, until customers are named (B04).
- The Gate 0 moat count of four. It rests on mechanical tests that flip on the window (B07 FLAG-GATE0-DIVERGENCE).
- Deck market-size and customer-count claims, until verified live (B04 FLAG-DECK-RELIABILITY).

**C3. THE BUSINESS FALSIFIER.** Evidence that forces a re-declaration of the FROM business itself:
- Live-web lookups show the customers behind the Rs 26.98 Cr, or the dealers behind the Rs 20.36 Cr, share directors or partners with the MD's four directorships or the eleven promoter-group entities (B08 analyst_note). The business would then be a related-party channel, not a tender reseller.
- The owner of the 65.84% parent of Gostocks Fintech proves to be the MD without arm's-length proof (B08 upgrade trigger).
- Top Supplier 1 (40.86% of purchases) proves to be a near pass-through of the cyber line, with cyber revenue Rs 35.23 Cr against Top Supplier 1 purchases Rs 32.68 Cr (B04 analyst_note). The business would then be a thin-margin agent, not an assembler.

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

Draft for Halt 1, as specified in prompts/13-synthesis-pipeline.md, BUSINESS UNDERSTANDING NARRATIVE. Stage 13 keeps the final version.

Kwick supplies the tools that police and forensic laboratories use to collect and test evidence (B04). Physical evidence kits are 36.99% of FY26 revenue. They are assembled from OEM tools and carried to crime scenes to capture fingerprints, body fluids and other traces (B04 revenue_streams; B07 optionality register). Cyber and digital forensics is 33.32% of revenue. It is mostly resale of OEM tools that copy and read seized phones and drives, and one supplier looks like a near pass-through for it (B04 analyst_note). DNA forensics is 10.76%, up from Rs 0.43 Cr to Rs 11.38 Cr in two years, and it is resale to state laboratories (B05 trigger 4). Mobile crime scene vehicles are 10.00% and are moving from whole vans to kits fitted by dealers and vehicle builders, Rs 20.36 Cr of kits for 95 vehicles in FY26 (B03). Rented handheld scanners are 8.75% and equal one customer, the Government of Bihar (B04). Police cannot skip these tools because the new criminal procedure law (BNSS) phases in mandatory forensic examination for serious offences, state by state (B09 FLAG-BNSS-PHASING).

The customers are state and central police, state forensic laboratories and central agencies. They procure by tender and on GeM at the lowest compliant price, which makes the work contract-by-contract (B07 R1; B05 trigger 1). The top customer is 23.59% of FY26 revenue and the top ten are 77.64% (B03). Customers served fell from 128 to 95 in two years while revenue rose 3.5x (B05). Government revenue fell from 86.98% to 55.22% of the total. Verifier B found that the dealer-route kit revenue equals Top Customers 2 and 4 and matches the Maharashtra and Rajasthan state totals, so the real customers may still be state police (B12b). Rs 26.98 Cr of non-government revenue has no named customer (B13). Maintenance contracts that could lock customers in are 0.17% of revenue (B04).

Present demand comes from scheme money. The nearest trackers are MHA and DFSS approvals and releases under SMFC and its successor, and GeM bid and order awards for forensic kits, DNA and cyber tools (B09 candidates 1 and 6). The Government of Bihar rental renewal is a signal by itself, because that one customer is the whole rental line (B09 candidate 4).

Demand should grow from four verifiable signals. State notifications under BNSS section 176(3) each start a five-year clock in that state (B09 candidate 2). NFIES, CFSL and NFSU campus tenders, including the Varanasi campus, could add lab equipment orders, though no Kwick order is named (B09 candidate 3, B05 trigger 7). The Union Budget and Demand for Grants for MHA forensic lines set the central pool (B09 candidate 5). NCRB and I4C cybercrime registrations drive the cyber line (B09 candidate 8). Against this, SMFC ended on 2026-03-31 and the run did not find its successor (B09).

The run found no moat in any line. The emerging moat scan scored 11.6, which is NONE and 0.4 below the MODEST line, and none of its 22 categories is Strong or Moderate (B07). Talent asymmetry and the cannibalisation barrier score zero (B07 analyst_note, 07-emoat.md scorecard rows 21 and 22). The kit line has non-exclusive OEM access (Sirchie, Thermo Fisher, Smallpond), which is the nearest thing to an edge, and it is weak and unproven in durability (B04 moats_present). The cyber and DNA lines are resale with no moat. The vehicle line is moving to dealers with no moat. The rental line is one contract and no moat. The only Moderate item is the BNSS and scheme tailwind, and every competitor shares it (B07 R1). The in-house E-Forensics software and handhelds are unproven and the run did not establish any revenue from them (B07).

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. VERTICALS FRAMED

**Vertical 1: Gross margin on revenue and in-house product revenue**
- Corpus establishes: gross margin on revenue 37.30 / 31.15 / 27.06% FY24 to FY26 (prospectus p.257; B05 promise row 3, B12b). Opex fell 19.52% to 9.11% of revenue and EBITDA margin sat flat near 18% (B04). The mix reading is cyber and DNA resale. The price-cutting reading is not ruled out (B04 analyst_note). Peer resale lines carry hardware cost risk of 25% to 50% (B06). Kwick at 27.06% sits above the peer resale band of single digits to 18% (B12b, B13).
- Cannot establish: segment or dealer-route gross margin, in-house product revenue, the input-cost exposure of the cyber line, Top Supplier 1 identity and terms (B04, B06 FLAG-INPUT-COST-NOT-IN-B05).
- Deciding questions: (1) What is the gross margin by line and by dealer route? (2) Did Top Supplier 1 raise its rates between bid and award? (3) When does the Rs 1.37 Cr software commission and which customer placed the first order?

**Vertical 2: Cash conversion and working capital**
- Corpus establishes: CFO -2.61 / 4.65 / 7.62 Cr against PAT 2.83 / 8.56 / 13.51 Cr (B01; B03 FLAG-CASH). FY26 CFO includes Rs 1.44 Cr of GST timing; FY25 includes Rs 7.17 Cr of extra payables (B03). Rs 1.31 Cr sits at 2 to 3 years, 20.7% provided (B02 rank 3). March quarter was 51% of FY25 sales (B05). FY27 need Rs 44.42 Cr, IPO Rs 31.42 Cr, creditor days planned 44 to 30 (B05 guidance).
- Cannot establish: any post-listing cash flow, receivables by customer class, an ECL rule, FY26 Q4 share of sales (B02, B03).
- Deciding questions: (1) What are H1 FY27 CFO/PAT and year-end receivable days? (2) How do Top Customers 2 and 4 age in the receivables? (3) Does the IPO fund growth or replace existing funding? B03 notes about Rs 22.87 Cr of the plan replaces existing funding.

**Vertical 3: Customer identity and repeat**
- Corpus establishes: government share 86.98 / 78.91 / 55.22%; non-government Rs 47.34 Cr, 82.7% of FY26 growth (B01, B02). Kit revenue Rs 20.36 Cr equals Top Customers 2 and 4 (Rs 12.01 Cr + Rs 8.34 Cr) and matches Maharashtra and Rajasthan totals; the end client does pre-dispatch inspection (B12b). Gujarat 29.39%, up 4.5x in two years (B07). No related-party sale in the RPT schedule, but completeness is untestable (B08).
- Cannot establish: names of any top-10 customer or dealer, customer class of the remaining Rs 26.98 Cr, receivables split by class (B02, B03).
- Deciding questions: (1) Who are the dealers and the end-user police forces behind Top Customers 2 and 4? (2) Do any non-government customers share directors with the MD's four directorships or the eleven promoter-group entities? (3) Did Gujarat and Top Customer 1 reorder in H1 FY27?

**Vertical 4: Scheme demand continuity**
- Corpus establishes: SMFC Rs 2,080.5 Cr, FY22 to FY26, ended 2026-03-31; scheme floor Rs 416 Cr a year; SOM Rs 126.4 Cr is a floor, not a forecast (B09). BNSS 176(3) gives states five years from their own notification and only Goa was found (B09 FLAG-BNSS-PHASING). Three counts of mobile labs are unreconciled: over 1,000 (deck), over 550 (prospectus), 433 vans (PIB scheme) (B09).
- Cannot establish: successor scheme, equipment share of NFIES and SMFC, state own-budget spend, primary text of the PIB release of 2026-01-03 and MHA replies (fetch blocked, B09 input_gaps).
- Deciding questions: (1) Is a funded successor to SMFC approved? (2) Which states notified BNSS 176(3) and when? (3) Does the NFSU Varanasi campus turn into a tender that Kwick wins?

### 4b. CANDIDATE SIGNAL TABLE

All rows are UNVERIFIED. Verification and tracker writes happen at Role 5.5 in claude.ai. Source types follow the Downstream Source Discovery Protocol registry (Type 1 listed company, Type 4 government entity, Type 5 regulator, Type 6 trade data).

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| MHA and DFSS approvals and releases under SMFC and successor scheme (B09 c1) | No funded successor approved by the H1 FY27 results, or releases to the states that ordered from Kwick stop | Event-Driven | MHA Lok Sabha and Rajya Sabha replies; MHA forensics section; PIB; sansad.in (Type 4) |
| State notifications under BNSS section 176(3) (B09 c2) | Fewer than the expected states notify, or notified states do not lift kit orders in the next two quarters | Event-Driven | State home department gazette notifications (Type 5) |
| NFIES, CFSL and NFSU campus tenders including Varanasi, foundation stone 2026-10-07 (B09 c3) | No Kwick order named in a Reg 30 filing by the H1 FY27 results (B05 trigger 7 kill signal) | Event-Driven | CPPP and GeM portals; NFSU tender page; BSE announcements (Type 4 and Type 1) |
| Government of Bihar equipment rental contract renewal (B09 c4) | Rental revenue (Rs 9.25 Cr, 8.75%) falls or the contract lapses | Event-Driven | Bihar e-procurement portal; Bihar police tenders (Type 4) |
| Union Budget and Demand for Grants, MHA forensic lines (B09 c5) | Central forensic line falls below the Rs 1,471 Cr FY27 secondary figure in the next budget | Event-Driven | Union Budget expenditure documents; PRS Demand for Grants analysis (Type 4) |
| GeM bid and order awards for forensic kits, DNA and cyber tools (B09 c6) | Kwick named in no award in two consecutive months while peers appear | Monthly | GeM public bid and order data (Type 4) |
| OEM partners and Top Supplier 1: Thermo Fisher partner awards, Sirchie, Smallpond (B09 c7) | Top Supplier 1 share stays above 40.86% with falling credit terms, or the OEM raises distributor rates | Quarterly | Customs import records and shipment data; OEM India distributor announcements (Type 6) |
| NCRB and I4C cybercrime registrations (B09 c8) | Registrations flatten while cyber revenue is expected to keep a 2.34x pace | Event-Driven | NCRB Crime in India; I4C portal statistics (Type 5) |

### 4c. FRAGILITY READ

- variable_count: 7. The bull case needs seven things to go right: (1) gross margin on revenue holds at or above 27%; (2) CFO/PAT rises to 0.8 or more; (3) the dealer-route customers prove arm's-length state police; (4) a funded successor to SMFC and BNSS notifications continue; (5) Gujarat and Top Customer 1 orders repeat; (6) OEM supply terms and hardware input costs stay workable; (7) in-house products and software commercialise.
- verifiability_ratio: 5 of 7 externally observable (variables 1, 2, 4, 5, 6 through filings, MHA replies, GeM awards and peer calls). 2 of 7 are company-narrated only until live-web work and the H1 FY27 filing close them (variable 3, the dealer-route customer class; variable 7, in-house commercialisation).
- single_point_failure: Gross margin on revenue. Opex is already 9.11% of revenue and the cushion is nearly spent (B04), so a fall below 25% falls straight into EBITDA margin. One variable alone can break the thesis.
- fragility_verdict: FRAGILE (seven variables, two company-narrated only, one kill-switch).

### 4d. RESEARCH BRIEF (the claude.ai work order)

The corpus cannot do these. Items 1 to 4 are the PENDING LIVE VERIFICATION links raised by the Section 4e chains. Item 17 is the chain-building work still owed.

1. PENDING LIVE VERIFICATION (chain 1): MHA Lok Sabha and Rajya Sabha replies on SMFC fund releases to Maharashtra and Rajasthan, and the dated release schedule. Claude web opens sansad.in replies and the MHA forensic modernisation page.
2. PENDING LIVE VERIFICATION (chain 1): GeM and e-procurement award pages for forensic van kits issued by Maharashtra and Rajasthan police in FY26, to name the dealers and vehicle builders behind Top Customers 2 and 4 and the payment status of those awards.
3. PENDING LIVE VERIFICATION (chain 2): Top Supplier 1 identity (Rs 32.68 Cr, 40.86% of FY26 purchases) through customs and shipment data (Type 6: Volza, Export Genius or similar), and its credit terms to Kwick.
4. PENDING LIVE VERIFICATION (chain 2): OEM India distributor announcements and partner award pages for Thermo Fisher, Sirchie and Smallpond, to find any change in distributor rates or terms since FY24.
5. MCA lookup of each customer or dealer named in items 2 and 3 against the MD's four directorships (Mokka Kefi and Cabana, Esource Lighting LLP, Brrain Source, Archos Techno Solutions) and the eleven promoter-group entities (B08).
6. MCA master data, charges and strike-off status for Gostocks Financial Services Pvt Ltd (65.84% parent of Gostocks Fintech), Gostocks Fintech Pvt Ltd and Extreme Covet Pvt Ltd; ownership of the parent (B08; Zauba returned 403).
7. Primary text of the PIB release dated 2026-01-03 (PRID 2211128) and the MHA reply that resolves Rs 185.28 Cr of Rs 245.29 Cr (prospectus) against Rs 128.28 Cr of Rs 245.29 Cr (secondary snippet) (B09).
8. Status of a successor to the MPF umbrella scheme after 2026-03-31 (B09).
9. State-by-state BNSS section 176(3) notifications and dates; Goa 2025-02-24 is the only one found (B09).
10. Government of Bihar rental contract: term, rate, renewal date, receivable status (B09 candidate 4).
11. Filed Sep-2026 shareholding pattern from BSE, names of the DII (10.85%) and the 23 FIIs (1.49%), and any link to the lead manager's funds (B08).
12. Independent confirmation of the SAT stay in CCV Appeal 278 of 2026 and the outcome of the Madras High Court hearing on 2026-08-19 (B08).
13. NFSU Varanasi: any Kwick order, tender or MHA letter behind the Reg 30 note of 2026-09-27; the 2026-10-07 foundation stone event (B05 trigger 7, B09 candidate 3).
14. Fetch the FY2025-26 annual report (BSE Reg 34 or company IR page) and the BSE announcements of 2026-09-03 to 2026-09-23 that were not staged; watch for the H1 FY27 results filing (B00).
15. Verify deck market claims: 433 vans, 35,000 experts by 2029, digital forensics $0.19bn to $1.39bn (Deloitte-DSCI path, not PIB), Rs 1,852 crore against Rs 185.28 Cr (B04, B09).
16. Verify the Union Budget FY27 MHA forensic line of Rs 1,471 Cr and the ICJS deduction used in the Rs 921 Cr central pool (B09, secondary tier).
17. Build chains 3 to 5 of the Rule F floor (see 4e), with live-web links, before Role 2. Suggested seeds from the corpus: the Bihar rental line (B09 candidate 4), the BNSS notification clock (B09 candidate 2), and the NFSU Varanasi note (B05 LBF-4).

### 4e. SECOND-ORDER STUB (Master Prompt v3.7, Rule F)

Two chains, drafted from corpus for Claude web to extend. Every Link 3 is labelled inference. Every starting fact carries its cite. No counterparty fact is stated that the corpus does not hold.

```
CHAIN 1: FY27 working-capital plan uses creditor days of 30 against 44 in FY26, and funds a Rs 44.42 Cr gap with Rs 31.42 Cr of IPO money (B05 guidance; prospectus pp.90, 96)
Link 1 [documented, 📄]: The same filing gives two reasons for the FY26 fall in creditor days. Page 91 says "conscious effort to settle payables faster" for better terms. Page 96 says suppliers "insist on shorter credit periods" and Kwick has "limited bargaining power" (B12b F2). Receivable days fell on both bases while revenue rose 3.5x (B01 LBF-2). Of the plan, about Rs 22.87 Cr replaces existing funding and about Rs 8.55 Cr is the increase over FY26 (B03 guidance_table; B05 red_flags).
Link 2 [PENDING LIVE VERIFICATION]: Who pays, and why now. The end payers behind the largest growth are, by inference from filed tables, the state police behind Top Customers 2 and 4 (B12b). Whether those states release scheme funds on schedule is not in the corpus. Claude web should open: (a) MHA Lok Sabha and Rajya Sabha replies on SMFC releases to Maharashtra and Rajasthan; (b) the GeM and e-procurement award pages for the forensic van kits issued by those two police forces in FY26. SMFC ended on 2026-03-31 (B09), so the timing question is live.
Link 3 [INFERENCE]: If suppliers force shorter credit while customers pay on state budget timing, and March quarter loading stays high (51% of FY25 sales, B05), year-end receivables stay elevated and payables shrink together. Cash conversion can then rise above 0.8 only with a collections step change. The IPO money would fund working capital that growth consumes, and it would not fund added growth.
Binding constraint: Working capital and the bank guarantee limit. Limit headroom is 207.15 of 800.00 lakh against about 40% implied FY27 revenue growth (B03 missing_risks). Bank guarantees outstanding Rs 5.93 Cr, 14.3% of net worth (B01 E4).
Unsaid: MD&A says the business is "not seasonal" while March quarter was 51% of FY25 sales (B05 red_flags). Customers served fell 128 to 95 with no explanation (B05). Customer advances show Rs 22.18 lakh against a management claim of 30% to 50% advance from private customers (B02 rank 8).
Observation that confirms or breaks this chain, and confirm-by date: Confirms: H1 FY27 CFO/PAT at or above 0.8, year-end receivable days at or below 80, creditor days near the 30 planned, bank guarantee outstanding below Rs 7.00 Cr (700 lakh), and the Maharashtra and Rajasthan awards shown as paid. Breaks: H1 FY27 CFO/PAT below 0.56 with trade receivables growing faster than revenue (B13 falsification line). Confirm-by date: the H1 FY27 results filing; the date is not in the corpus and B07 gives a window of about Nov 2026 to May 2027.
```

```
CHAIN 2: Cyber revenue is Rs 35.23 Cr and Top Supplier 1 purchases are Rs 32.68 Cr, while Top Supplier 1 holds 40.86% of FY26 purchases and gross margin on revenue fell to 27.06% (B04 analyst_note; B03; prospectus p.257)
Link 1 [documented, 📄]: Top Supplier 1 is 92.8% of cyber revenue and looks like a thin-margin pass-through, a hypothesis not confirmed (B03 missing_risks). The OEM ties are non-exclusive and run "deal to deal" (B04 moats_present; B12b). Peer calls document hardware cost rises of 25% to 50% that voided tenders at ADSL and cut DSSL gross margin from 18% to 14% (B06 FLAG-INPUT-COST-NOT-IN-B05; DSSL and ADSL transcripts).
Link 2 [PENDING LIVE VERIFICATION]: Who pays, and why now. Top Supplier 1 is unnamed in the corpus (B03 ar_new_downstream_entities). Whether it is an OEM, a distributor, or related to Kwick is not stated. Claude web should open: (a) customs and shipment records (Type 6 trade data) to name Top Supplier 1 and its consignee pattern; (b) OEM India distributor announcements and partner award pages for Thermo Fisher, Sirchie and Smallpond, to see any change in distributor rates or terms.
Link 3 [INFERENCE]: Tender rates are fixed at the bid, so a supplier cost rise between bid and award lands on Kwick's margin before it shows in any half-year average. Opex is already 9.11% of revenue (B04), so there is no cushion left to absorb the loss, and a gross margin below 25% would fall into EBITDA margin. Convergence toward the peer resale band, single digits to 18%, is the obvious bear question (B12b; B13).
Binding constraint: Cost cushion. Opex ratio fell from 19.52% to 9.11% (B04). Thin organisation of 33 to 34 staff and a six-person sales team (B03). Tenders go to the lowest compliant bid (B07 R1).
Unsaid: MD&A explains the margin fall by cyber mix only (RF13 p.32 as carried in B03) and is silent on input costs. Segment margins are NOT FOUND (B04). The promised margin lever, domestic sourcing, rose from 65.42% to 91.35% while margin fell (B05 promise rows 2 and 3).
Observation that confirms or breaks this chain, and confirm-by date: Confirms the chain: H1 FY27 gross margin on revenue below 27%, Top Supplier 1 share at or above 40.86% (FY26), and a documented OEM or distributor rate change since FY24. Breaks the chain: gross margin on revenue at or above 27% with Top Supplier 1 share below 40.86% and no rate change found. Confirm-by date: the H1 FY27 results filing; the date is not in the corpus and B07 gives a window of about Nov 2026 to May 2027.
```

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in claude.ai with live web, before Role 2.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. Kwick supplies forensic tools to Indian police and forensic labs. These include evidence kits, cyber tools, DNA systems and crime scene van kits (B04).
2. Revenue was Rs 30 Cr in FY24, Rs 65 Cr in FY25 and Rs 106 Cr in FY26. Profit after tax rose from Rs 2.8 Cr to Rs 13.5 Cr (B01, B13).
3. The firm mostly resells tools from foreign makers and assembles kits. It owns no plant and has about 33 staff (B04, B03).
4. Customers are state and central police, state labs and central agencies. They award contracts by tender at the lowest compliant rate (B07, B05).
5. The top ten customers give 77.64% of revenue. The number of customers fell from 128 to 95 in two years (B03, B05).
6. Rs 20.36 Cr of FY26 revenue came through dealers and vehicle builders. It equals two named top customers and probably serves state police. Rs 26.98 Cr of non-government revenue still has no named customer (B12b, B13).
7. Demand exists because a new law makes forensic examination mandatory for serious crimes. It phases in state by state, and government schemes pay for the kit (B09).
8. The main scheme, SMFC, ended on 31 March 2026. The run did not find a successor, so future demand has one open question (B09).
9. The large market figure management quotes, Rs 30,000 crore, is a five-year announcement, not an equipment market. The run sizes the visible scheme pool near Rs 416 Cr a year (B09).
10. The run found no moat. The scan scored 11.6, below the 12 point line for a modest moat. The only edge is non-exclusive access to foreign makers (B07, B04).
11. The mental model, in draft: a tender reseller that claims a climb toward a value-added supplier through in-house products. The proof gate has not fired. The model is not signed (Section 2).
12. The fragility read is FRAGILE. Seven things must go right, two cannot be checked yet, and one fall in gross margin alone can break it (Section 4c).
13. The corpus lacks the FY26 annual report, any filing since listing, any call, any rating and any shareholding pattern. Two stages ran partial (B00, B08, B09).
14. Gross margin fell from 37.30% to 27.06% of revenue in two years. Cost cuts held profit margin near 18%, and that cushion is nearly spent (B04).
15. The biggest open questions: do cash flows reach 0.8 of profit in H1 FY27, and who are the customers behind Rs 47.34 Cr of non-government revenue (B01, B13).

---

## SECTION 6: STANDING EXTRACTION ANNEX

All page anchors are PDF pages of KWICK-Prospectus-2026-08-31.pdf unless another file is named. Units are Rs lakh as printed.

### 1. UNITS

Quote: "During FY 2025-26, the Company supplied scientific and digital kits and related solutions for 95 Mobile Crime Scene Investigation Vehicles under this collaborative arrangement, contributing revenue of ₹2,035.74 lakhs." (KWICK-Prospectus-2026-08-31.pdf, p.150)
Quote: "Total number of customers served (Nos.) 95 124 128" and "No. of Mobile Forensic Vans Sold 25 47 21" for FY26, FY25, FY24 (p.164; p.259).
Comment: The prospectus prints no per-unit figure with a printed unit, such as revenue per van or per kit. The 95-vehicle line covers a basket (scientific and digital kits and related solutions), not one product. Volume and revenue lines to derive per-unit figures: Rs 2,035.74 lakh over 95 vehicles (derived Rs 21.43 lakh per vehicle kit, B09 and B12a), and Mobile CSI Vehicles revenue "1,056.76 10.00% 1,640.66 25.23% 405.09 13.42%" for FY26, FY25, FY24 (p.24) against the van count 25 / 47 / 21 (p.164). Revenue per customer served derives from FY26 revenue Rs 10,571.28 lakh (p.24) over 95 customers (B04: 111.3 lakh).

### 2. SEGMENT CAPITAL AND DEBT

Quote: "As the company has only one business segment, disclosure under Accounting Standard 17 on "Segment Reporting" issued by the Institute of Chartered Accountants of India is not applicable." (p.246)
Quote: "Secured Borrowings - Fund based -; Secured Borrowings - Non-Fund based 592.85; Unsecured Borrowings -" as at 2026-03-31 (p.255). "Total Borrowings -" and "Total Equity 4,140.67" (p.254).
Quote: "Short Term Borrowings (excluding cc) 129.09 267.93 -" for FY24, FY25, FY26 (p.90); "Increase in / (Repayment) of Short term Borrowings (325.61) 10.59 (285.20)" for FY26, FY25, FY24 (cash flow statement, Annexure III, p.228).
Comment: NOT DISCLOSED by segment: segment assets, segment liabilities and capital employed are not printed, because the company reports one segment. Borrowings are unallocated. Total fund-based borrowings are nil at FY26 against Rs 267.93 lakh of short-term borrowings at FY25 (excluding cash credit). The Rs 592.85 lakh is non-fund-based (bank guarantees). Segment margins are NOT FOUND (B04).

### 3. GUIDANCE VERSUS ASPIRATION

(a) Guidance with a period:
- Quote: "the Board of Directors of the company pursuant to its resolution dated 25-05-2026 has approved the estimated working capital requirements for Fiscal 2026-27" with "Total Working Capital Gap (A-B) 4,442.00", "Internal Accruals 1,300.00", "IPO Proceeds 3,142.00" (p.90). Comment: FY27 working-capital plan, period FY27.
- Quote: "Debtor days have been estimated at 74 days in FY 2026-27" (p.95); inventory days 48 and creditor days 30 for "FY 2026-27" (p.95; p.96). Comment: FY27 holding levels. Implied FY27 revenue is derived, not stated (B03, B05).
(b) Aspiration without a period:
- Quote: "E-forensics comprises of 10 apps ... Following are the apps that are under development", with development "From the start of F.Y 2025-26" (p.151). Comment: no completion date.
- Quote: "Setup a private forensic laboratory as a proof of concept ... is not being used for commercial sample processing at present." (prospectus txt L1958-1961, risk factor pages near p.31). Comment: no funding in the objects of the issue (B03).
- Quote: "We have been actively working towards reducing this concentration risk by expanding our presence across other regions of India." (p.152). Comment: no number, no period.
- Quote: "This strategic shift aimed at reducing dependency on imports, controlling costs, and improving gross margins." (p.153). Comment: no period; gross margin on revenue fell 37.30% to 27.06% (p.257).
- Quote: "These software platforms are currently under development and their features, deployment timelines, customer acceptance and commercialisation may be subject to technical development" (p.152). Comment: AI judicial platform and LIMS, no date.
(c) Capacity or capability only:
- Quote: "The Company, with its integrated portfolio of forensic and law-enforcement solutions, is well positioned to participate in such emerging opportunities." (announcements/20260927-a4e0e740-8719-4e83-b403-8e5bc74dfe9d.pdf, dated 2026-09-27). Comment: names a Rs 150 crore NFSU campus and no Kwick order.
No revenue, margin, order-book, capex or dividend guidance: NOT DISCLOSED (B05 guidance; no figure filed).

### 4. CONCENTRATION

Customer. Quote: "Top 1 Customer 2,493.65 23.59% ... Sum of all Top 10 Customers 8,207.23 77.64%" for FY26 (p.24; p.160). Top customer share 23.59%; top 10 share 77.64% (82.61% in FY24). Customers are unnamed.
Product. Quote: "Forensic Science & Physical Evidence Solutions 3,910.84 36.99%" (p.24). Top product share 36.99%; cyber 33.32%; the rental line equals one customer, "Top 3 Customer 925.42 8.75%" (p.24; B04).
Geography. Quote: "Gujarat 3,106.97 29.39%", "Maharashtra 1,204.55 11.39%", "Tamil Nadu 1,119.95 10.59%", "Bihar 953.22 9.02%", "Rajasthan 834.42 7.89%" for FY26 (p.159). Exports "Sri Lanka 17.04 0.16%" (p.159).
Supplier (added). "Top Supplier 1" is 40.86% of purchases in FY26 and 27.02% in FY25 (p.161; B03, B04).
Customer class. Quote: "Revenue from Government Entity 5,837.36 55.22% 5,131.51 78.91% 2,625.30 86.98%" and "Revenue from Non - Government Entity 4,733.92 44.78% 1,371.18 21.09% 393.03 13.02%" (p.160).
Comment: Customer, product, geography and supplier concentration are all disclosed. Customer names are NOT DISCLOSED.

### 5. PROMISE LEDGER

Delivery status from B05 promise_delivery (delivered 4, partial 3, missed 1; untestable rows added). No concall exists, so every promise comes from the prospectus and the 2026-09-30 deck.

| Promise (page) | Date made | Delivery status | Evidence anchor |
|---|---|---|---|
| Reduce dependence on Bihar and Gujarat (p.152) | 2026-08-31 (prospectus) | PARTIAL | Bihar 34.53% to 9.02%; Gujarat 22.77% to 29.39%; top two 57.30% to 38.41% (p.159) |
| Cut imports, raise domestic sourcing (p.153) | 2026-08-31 | DELIVERED | Domestic share 65.42% / 85.72% / 91.35% (p.153) |
| Domestic sourcing improves gross margins (p.153) | 2026-08-31 | MISSED | COGS % of revenue 62.70 / 68.85 / 72.94 (p.257) |
| Dealer and vehicle-builder model lowers working capital (p.150) | 2026-08-31 | PARTIAL | Company NWC days 141 to 124 (p.257); vans delivered 47 to 25 (p.259); customer class NOT FOUND |
| Debtor days fall through private mix and advances (pp.92-93, 97) | 2026-08-31 | PARTIAL | Average-basis days 89 to 74; year-end 111 to 79 (p.91; p.245) |
| Improved collections repaid all borrowings (p.266) | 2026-08-31 | DELIVERED | Borrowings Rs 3.26 Cr to nil, debt-to-equity 0.12 to 0 (p.257) |
| BNSS lifts DNA products (pp.150, 267) | 2026-08-31 | DELIVERED | DNA revenue 42.66 / 615.72 / 1,137.57 lakh (p.150) |
| Inventory management better, order-based procurement (p.266) | 2026-08-31 | DELIVERED | Inventory days on year-end cost of sales 61.7 to 49.4 (computed, B05) |
| E-Forensics 10 apps in development from start of FY26 (p.151) | 2026-08-31 | UNTESTABLE | CWIP Rs 0.62 Cr existed at 2025-03-31 (p.269); none commissioned |
| In-house products commercialised (p.151) | 2026-08-31 | UNTESTABLE | Revenue by in-house product NOT FOUND |
| Private forensic lab as proof of concept (p.31; deck p.5) | 2026-08-31; 2026-09-30 | UNTESTABLE | Demonstration only; not funded in objects |
| Debtor days 74 and creditor days 30 in FY27 (pp.95-96) | 2026-08-31 | UNTESTABLE | Due after FY27 year-end; H1 FY27 results pending |

### 6. RESTATED BASES

Quote: "Provision for gratuity accounted for as per AS 15- "Employee Benefits" based on Actuarial Valuation report for the period ended March 31, 2024." with "Profit After tax as per Books of Accounts 1,350.77 855.94 287.16" and "Restated Profit (Loss) after tax 1,350.77 855.94 283.47" (Annexure VII, p.249).
Quote: "Appropriate adjustments have been made in the summary statements of Assets and Liabilities Profits and Losses and Cash flows wherever required by reclassification of the corresponding items of income expenses assets and liabilities in order to bring them in line with the requirements of the SEBI Regulations." (p.249).
Quote: "Previous year figures are regrouped / rearranged, where necessary to confirm with the current year's classification / disclosure." (restated notes, txt L15378, p.248).
Quote (comparative as printed in the latest filing, the prospectus; no later filing exists): "Restated Reserves & Surplus 2,453.19 2,578.97 792.98" for FY26, FY25, FY24 (p.249).
Comment: Comparatives are restated for gratuity (FY24 PAT 287.16 to 283.47) and regrouped generally. No reorganisation or transfer restates comparatives. The product-line table in the risk factors (goods 9,628.00 and 5,622.71, p.24) differs from Note II.1 (9,620.04 and 5,608.52, p.239) with the same totals (B02 restatements_found).

### 7. CORPORATE-ACTION CLAUSES

No scheme of arrangement, demerger, merger or buyback is in the corpus. Quote: "There is no ―Buyback, ―Standby, or similar arrangement by our Company/Promoters/Directors/Lead Manager" (p.85, txt L6013). Nothing to fetch for a scheme.
Share-capital actions present (preferential and similar):
- Rights issue. Quote: "During FY 23-24, the company has made Rights issue for 16,00,050 shares of Face value ₹. 10 per share at issue price of ₹ 20 per share (securities premium of ₹ 10 per share) amounting to ₹ 320.01 Lakhs." (p.90). Ratio 5:1, allotted 2024-03-12 (p.80, B03).
- Private placement. Quote: "During FY 24-25, the company has made private placement for 1,79,295 shares of Face value Rs. 10 per share at issue price of ₹ 569 per share ... amounting to ₹ 1020.19 Lakhs ... of which ₹ 72.22 lakh was incurred as issue-related expenses, resulting in net proceeds of ₹ 947.97 lakh." (p.90). Dated 2024-12-28 (p.33).
- Bonus. Quote: "the Company issued bonus equity shares in the ratio of 7:1 on September 16, 2025" (p.33). 1,47,65,485 shares (pp.76, 79).
- Promoter OFS. Quote: "10,80,000 Equity Shares which are OFS shares held in demat account of "KWICK FORENSIC SOLUTIONS LIMITED-OFS ESCROW"" (p.79). Rs 972.00 lakh (B08, p.276).
Comment: Definition of any undertaking and liability allocation clauses do not apply. No scheme appointed or effective dates exist.

### 8. RELATED-PARTY PERIMETER

Annexure VIII (pp.250-251), FY26 amounts in Rs lakh:

| Entity (relationship printed) | FY26 transactions |
|---|---|
| Shammer Saralal Shah (KMP, MD) | Remuneration 126.72; rent 7.88; interest on directors loan 1.18; loan borrowed 101.89, repaid 246.18; balance payable nil |
| Sejal Shammer Shah (Director) | Remuneration 8.40; interest 0.86; loan borrowed 9.55, repaid 95.16; balance payable nil |
| Ashok Hinduja (KMP, COO) | Remuneration 77.83; salary payable 18.43 |
| Neeraj Bakulesh Jhaveri (Whole Time Director) | Remuneration 49.15 (includes pre-appointment salary) |
| Vishal Jain (KMP, CFO) | Remuneration 17.55 |
| Selvakumar Krithika (KMP, CS) | Remuneration 1.70 |
| Latha Venkatesh; Sonia Vaid (Additional Directors) | Sitting fees 0.68; 0.56 |
| Gostocks Fintech Private Limited ("Director having significant influence") | Purchase of asset (software) 20.00; software programming and integration fees 3.00 (FY25: 58.70 and 0.25) |
| Shah Infotech | Purchase of goods 35.68; repairs 0.03; research and development 0.07 |
| Shah Electronics | Purchase of goods 17.83 |
| Shah Trading & Co. | Purchase of goods 11.93; research and development 0.08 |
| The Style Salad | Purchase of goods 1.56 |
| Punita Shah (Relative of Director) | Commission 1.50 |
| Extreme Covet Private Limited | FY26: loan borrowed 3.02, repaid 41.05; no purchase (FY25 purchase 31.20) |
| Gee Gee Hire Purchase & Leasing Private Limited | FY26 nil (FY24 loan 200.00 borrowed and repaid) |
| Sangeetha Hinduja (Relative of shareholder KMP) | FY26 nil (FY25 consultancy 12.00) |

Comment: Group vendors depend on Kwick: Gostocks Fintech supplied Kwick with 62.3% and Extreme Covet with 48.3% of their FY25 turnover (pp.213-215; B03, B08). Guarantors Bina Shah and Saloni Shah are not in the RPT list (B02 FLAG-RPT). The owner of the 65.84% parent of Gostocks Fintech is NOT DISCLOSED (B08). The annual report RPT note is NOT AVAILABLE because no annual report exists; Annexure VIII is the substitute.

### 9. PLEDGE AND SHAREHOLDING

Quote: "However, the Equity Shares held by the Promoters of the Company are not under any Pledge." (p.84). Quote: "30. As on the date of this Prospectus, none of the shares held by our Promoters/ Promoter Group are pledged" (p.85).
Quote: Pre-offer promoter and promoter group "1,49,38,624 ... 88.53%" (shareholding pattern, p.75, txt L5268). Post-offer: "Grand Total (A+B) 1,49,38,624 88.54 1,38,58,624 64.65", "#Subject to finalisation of Basis of Allotment." (p.79).
Twelve quarters as filed: NOT DISCLOSED. The company listed on 2026-09-03 and no quarterly pattern has been filed; the shareholding folder is empty because the BSE API returned Access Denied (B00). Pledge is nil at every date in the build-up tables (B08 pledge_trend, pp.79-84).
Institutional holding, latest: NOT DISCLOSED in the corpus. Screener shows Sep-2026 FII 1.49% and DII 10.85%, promoters 64.65% (B00, B08), web and non-anchored; names NOT FOUND.

### 10. VERIFICATION

Documents quoted, with file and date:
- inputs/prospectus/KWICK-Prospectus-2026-08-31.pdf (and the .txt twin), final Prospectus dated 2026-08-31.
- inputs/announcements/20260927-a4e0e740-8719-4e83-b403-8e5bc74dfe9d.pdf, Reg 30 note dated 2026-09-27.
- inputs/announcements/20260926-d9074a8c-e3d8-44e2-b97a-4b6474311727.pdf, market-movement clarification dated 2026-09-26. It states: "The Company is not aware of any information, event, development or impending announcement concerning the" Company.
- Stage reports 01 to 09 and verifier blocks B12a, B12b, B12c, B12d in outputs/ (run 2026-10-04), for cited block facts.
- inputs/presentation/Investor_Presentation_1.pdf, deck dated 2026-09-30, quoted only through B04 and B05.

CORPUS COMMIT HASH: 3ff70054bd0c255edb65a08f83433405b582aae4
