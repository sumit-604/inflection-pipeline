# CREDENT: HALT 1 UNDERSTANDING DOSSIER (stage 09b)

Company: Credent Connect N Care Ltd (CREDENT). Run date: 2026-11-12. Model: claude-sonnet-5-5.

This file is an understanding package. It holds no valuation, no price view and no decision. Sections 1 to 5 assemble committed blocks (B00 to B09, B12a to B12d, confidence). Section 4e reasons forward under the scoped chain exception and labels every inference. Section 6 quotes the corpus.

Units: filings report in INR Lakhs, presentations in INR Mn, the call in INR crore (100 Lakhs = 1 Cr; 10 Mn = 1 Cr). Every number carries its unit. Verifier A source-fidelity corrections bind this file: H1 FY27 balance-sheet cash and bank is 7,419.72 INR Lakhs (6,919.72 is cash and cash equivalents on the cash flow statement); H1 FY27 purchase of fixed assets is (443.12) and FD investment is (656.67) INR Lakhs (B12a, confidence.yaml).

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

Inventory only. Source: B00-inputs, B00-intake (34 rows verified, 0 moves, 0 unreadable).

1. CONCALLS.
   - Held: CREDENT-Concall_H1FY27_2026-10-29_Transcript.pdf. Call held 2026-10-29; filing cover letter dated 2026-11-03. Scanned PDF with OCR text (B00-intake).
   - This is the first call as a listed company. The MD calls it the first interaction with the investor community (B05).
   - Most recent period covered: H1 FY27, the half year ended 2026-09-30.
   - Later period plausibly reported: none. The company reports half-yearly (B00.input_gaps) and the next period, H2 FY27, ends 2027-03-31, after the run date.
   - An analyst and investor meeting dated 2026-11-12 was notified on 2026-11-08 (CREDENT_08112026013152_Intimation_for_Investor_Call.pdf). It falls on the run date, so no record of it can exist in the corpus.
   - Peer transcripts held: 12 (THYROCARE 4, TCIEXP 4, KRYSTAL 4), dated 2025-05-05 to 2026-11-10 (B00-intake).
2. ANNUAL REPORTS.
   - Held: CREDENT-Annual_Report_FY2025-26.pdf (121 pp; filing letter dated 2026-09-05).
   - Latest completed FY (FY2025-26): present. Three years held: NO. One AR only. FY24 and FY25 history comes from the RHP restated financials (B01.data_notes, B03.input_gaps).
3. RESULTS FILINGS.
   - Held: CREDENT-H1FY27-results-outcome-BM-2026-10-28.pdf (27 pp), dated 2026-10-28, half year ended 2026-09-30.
   - Gap to the AR: none. The AR covers the year to 2026-03-31 and the H1 filing is the next period. No earlier post-listing result exists because the company listed on 2026-08-20 (B00.input_gaps).
4. INVESTOR PRESENTATIONS.
   - Held: CREDENT-Investor_Presentation_H1FY27.pdf (filing letter 2026-10-28) and CREDENT-Investor_Presentation_listing_2026-08-20.pdf (transmittal 2026-08-20).
   - Latest: H1 FY27, 2026-10-28.
5. RESEARCH / RATING.
   - rating/ is empty. research/ is empty. No rating rationale, broker note or research note is held (B00.empty_folders).
   - The stage-0 empty-folder question was suppressed under the /step1 autonomy contract. Standing answer: go on with the gaps (B00.empty_folder_confirmation).
6. CORPORATE ACTIONS.
   - Nine NSE filings held, dated 2026-09-05 to 2026-11-08, of 22 filed since listing (B00.input_gaps):
     - 2026-09-05 board outcome (Directors' report, AGM notice, auditor appointment);
     - 2026-09-18 board outcome (CFO resignation and appointment);
     - 2026-09-29 AGM summary;
     - 2026-10-01 voting result;
     - 2026-10-01 auditor appointment disclosure;
     - 2026-10-28 results press release;
     - 2026-11-04 board outcome (inter-corporate loan);
     - 2026-11-04 Reg 30 disclosure (inter-corporate loan agreement);
     - 2026-11-08 investor call intimation (image only).
   - Left out as routine: audio-recording link, call intimations (22 and 24 Oct), Reg 74(5) certificate, trading window notice, newspaper advertisement, e-voting intimation, duplicate 18 Sep board outcome (B00.input_gaps).
   - Prospectus: CREDENT-RHP-Aug-2026.pdf (324 pp), dated 2026-08-08. The final prospectus with issue price and final objects amounts is absent.
   - Shareholding: two NSE XBRL files, DateOfReport 2026-08-19 and 2026-09-30 (stored as .txt).
   - Screening: screener-Data_Sheet.csv (one annual period, FY26, report date 2026-03-31) and the screener Financials workbook. The Profit and Loss, Quarters, Balance Sheet and Cash Flow sheets exported empty for CREDENT and all three peers (B00.input_gaps).
7. FRESHNESS PAIR CHECK.
   - B00.freshness_verdict: FRESHNESS PAIRS OK. All four pairs PASS: results to concall (H1 FY27 filing and H1 FY27 call both held); rating bulletin to rationale (no bulletin held); SEBI order to order text (none identified); AR to latest audited annual results (FY2025-26 AR held).
   - No pair failed, so no failed-pair mate is named here.
8. COLLECTION AND INTAKE NOTES.
   - The corpus was built by hand after the collector browser failed (Playwright Chromium could not launch). The screener exports came through the operator's Chrome (B00.input_gaps).
   - The collector name scrape returned "Credent" and was corrected to "Credent Connect N Care Ltd". The company is listed on NSE Emerge only and has no BSE scrip code (B00.input_gaps).
   - Verifier A shadow: NOT RUN. The switch reads armed and was left armed, an open item for the operator (B00.verifier_a_shadow).
   - Stage 8 (B08) and stage 9 (B09) are status partial. Their blocked web fetches are listed in B08.searches_skipped and B09.searches_skipped.
   - Verifier B counting basis is an open item: 80% with partially caught counted, 50% on fully caught only (confidence.yaml notes).
   - The stage-0 sector cap row "Logistics (asset-light)" is a classification for the operator to rule at /fttcp (B00.sector_cap_row). B04 states it fits the asset side only (B04 model-fit note). The dossier states no multiple.
9. SPEAR LINE CARRY-OVER (companies/CREDENT.md; memory to weigh, not a source). Spear: OVERRIDE 2026-11-12 (operator standing ruling 2026-09-05: Step-1 intake replaces the web spear). What the evidence found for each load-bearing fact:
   - Customer concentration. The call says no single customer above 10% (call p.5). The RHP and AR show the top customer at 3,374.48 INR Lakhs, 15.76% of FY26 revenue, and the top ten at 81.76% (B02, B04). The press release gives top ten at 80.60% at 2026-09-30. The H1 top-1 share is NOT FOUND (B05).
   - Organic versus acquired growth. The AR says the FY26 step-up "largely reflects" consolidating three acquired subsidiaries (B04, B03). All three came from promoter-side owners (B08). The call calls the 45% plan organic (B05). Alltrak H1 revenue is NOT FOUND (B05).
   - Cash conversion. FY26 consolidated CFO is (662.34) INR Lakhs against PAT 1,836.45 (B01, B02). H1 FY27 CFO is Rs (39) Mn (B01). Receivables went from 588 Mn to 788 Mn in six months (B05). The call says debtors age 60 days (B05). The RHP assumes 95 days (B05).
   - IPO money and group lending. Utilised 21.65 INR Cr of 93.90 INR Cr gross by 2026-09-30; unutilised 72.25 INR Cr (B05, results Annexure A). The 450.00 INR Lakhs loan to Kartavya Healtheon, approved 2026-11-04, is outside the RHP objects (B05, B08). The company states Kartavya is unrelated. Its owners are NOT FOUND (B08).

VERDICT LINE:
CORPUS VERDICT: CORPUS GAPPED

Gaps, by name and expected source:

| Missing document | Expected source | Kind |
|---|---|---|
| Final prospectus (issue price, final objects amounts) | company IR page / NSE | findable-missing |
| 13 of 22 NSE filings since listing (including any IPO monitoring agency report and routine SAST or PIT disclosures) | NSE corporate announcements | findable-missing |
| Screener Profit and Loss, Quarters, Balance Sheet, Cash Flow sheets (exported empty) | screener.in through the operator's Chrome | findable-missing |
| Pre-IPO investor calls the analyst refers to (call p.8), against the MD's "first interaction" (B05, B12b R16) | company IR page | findable-missing |
| Peer annual reports and presentations | NSE / BSE | findable-missing |
| Credit rating rationale (bank facilities) | rating agency site | plausibly-nonexistent (existence not established; stage 10 marks the rating quote unresolved) |
| Broker or research notes | none | plausibly-nonexistent (newly listed SME issuer; opacity is a data point) |
| Earlier annual reports, earlier post-listing results, earlier shareholding patterns | none | plausibly-nonexistent (listed 2026-08-20) |

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT - PENDING OPERATOR SIGN-OFF**

The operator signs only in claude.ai after live-web stress-testing. Nothing here is signed. Rung labels are classifications from block evidence for the operator to confirm or change.

### PART A: THE FROM STATE

**A1. ARCHETYPE (per line).**
- Healthcare Services (43.04% of FY26 revenue) and Operations and Supply Chain Management (24.93%): Outsourcing partner. These two lines are deployed people, about 68% of FY26 revenue (B04.revenue_streams, B04 model-fit note). The archetype variables fit: client concentration, wallet share, capacity fill, contract stickiness, price per unit.
- Logistics Services (25.26%): Outsourcing partner is the nearest fit. The ARCHETYPE LIBRARY holds no logistics entry. Revenue is per pickup and per route (B04). Route density is the lever (B04.unit_economics).
- The small lines (IT services 2.81%, Marketing 2.75%, other 1.20%) are project work and carry no archetype of their own (B04).

**A2. THE SIMPLE ANALOGY.** Credent is a staffing and courier firm for medical labs. A lab sends a sample from a patient's home to a testing centre, and that trip must be fast and cold. A lab also needs trained people to draw blood and to sit inside its labs. Credent supplies those people and those trips and bills per collection, per pickup or per stationed person. A lab can do the same work with its own staff. Credent gives the lab a variable cost in place of a fixed one. It holds few assets, so it grows by hiring people and by waiting to be paid (B04, B05).

### PART B: THE TRANSITION

**B1. FROM to TO (one transitioning line).**
- Line: Healthcare Services and Operations and Supply Chain (the deployed-people lines).
- FROM: the R1 to R2 boundary on the QUALITY LADDER. The evidence reads as outsourced labour at cost plus: pricing power weak, contracts terminable, EBITDA margin 13.29% in FY26 and about 13% in H1 FY27 (B04.pricing_power, B04.analyst_note, B01 data_notes). "Fits no rung cleanly" is the honest label for the logistics line (B04).
- TO (claimed): R3, value-added supplier with partial pricing power. Management language reaches toward R4. It says healthcare services is "a monopoly kind of" process and that Credent is "the leader" (call p.8, p.13; B05). The 15% to 16% EBITDA margin in three years is the stated destination (call p.8, B05.guidance).
- Rung-jump base rate: one rung per 2 to 3 years. The claim spans one to two rungs inside about four years (B05.guidance). That span calls for extraordinary proof.
- Logistics: no transition is claimed. The CFO and MD call it competitive and lower margin (call p.8; B05).

**B2. THE ENGINE.** Two things must physically change (B05.triggers 2 and 3; B02; B03):
1. Mix and unit economics. More healthcare services, wellness and the On-Demand product, with Alltrak tracking software lifting output per person (B05.triggers 2, 5). H1 FY27 healthcare services share was 45.84% against 45.82% in H1 FY26 (press release p.3). The mix has not moved year on year.
2. The float. IPO money (72.25 INR Cr unutilised at 2026-09-30, B05) must replace borrowings as the funder of receivables. Receivable days must fall from about 100 toward 60 (B03, B05). Total borrowings were about 21.62 INR Cr at 2026-09-30 (press release p.2).

**B3. THE PROOF GATE.** Observed at the H2 FY27 results filing (half year ending 2027-03-31), both parts at once (B03.monitorables, B05.triggers 2 and 3, B04.must_track_metrics):
- Consolidated EBITDA margin above 13.3%, with segment margin by line disclosed; and
- Consolidated CFO positive, CFO/PAT at or above 0.7, and receivable days including unbilled at or below 80.

FTTCP tests this. Until both fire, the transition is narrative and the name is research. The corpus holds no segment margin and no per-unit price today (B04, B09).

**B4. THE RECOGNITION GAP (open question for Stage 11).** Does the TO state, a pricing-power platform with a 15% to 16% margin, already look reflected in market pricing? This dossier does not answer it. Stage 11 resolves it through the PE gap. If the TO state is already priced, the re-rating engine is spent and only earnings growth remains. The sector cap row stays a stage-0 classification for the operator to rule at /fttcp (B00.sector_cap_row).

**B5. THE UGLINESS TEST.** Today's ugly optic is negative operating cash flow, receivables growing faster than revenue, 81.76% top-ten concentration and a restated profit history.
- Classification: STRUCTURAL-FEATURE, provisional.
- Evidence for it. The cash drag continued in H1 FY27, a half with no new acquisition. CFO was Rs (39) Mn and receivables rose 34% in six months (B01, B05). Peers do not show 45-day collection at high growth. Krystal runs about 118 days at +46% growth and TCIEXP runs 58 to 60 days (B06 peer cash note). The 5-day creditor assumption sits beside 95 debtor days in the RHP (RHP p.95, quoted in Section 6, Q3). The top-ten share moved only from 81.76% to 80.60% (B05).
- Evidence against it. IPO money arrived only on 2026-08-20. One half is a short test of the float. The FY26 CFO drag fell in an acquisition year (B01.analyst_note).
- Two readings: IPO money cures the float and the drag is temporary, or collection terms are set by customers and the drag is permanent at this scale. The separating observation is H2 FY27 consolidated CFO and receivable days. Stage 13 carries this classification into the value-trap test. No trade conclusion is drawn here.

**B6. THE TRANSITION FALSIFIER.** Any one of these at the H2 FY27 filing kills the arrow (B05.triggers 1 to 3 kill signals):
- Receivable days above 100 with consolidated CFO still negative.
- EBITDA margin flat or lower while resources rise from 6,789 toward 15,000.
- H2 revenue below about 165 INR Cr, or growth shown to come only from acquired entities.

### PART C: WHAT THE MODEL WATCHES

**C1. DOMINANT VARIABLES** (derived from B2 and B3; these become the Role 5.5 tracker signals).
1. Cash conversion: consolidated CFO/PAT and receivable days including unbilled. Now: CFO (662.34) INR Lakhs FY26, Rs (39) Mn H1 FY27; days about 100.3 FY26 (B01, B03, B05).
2. Customer concentration and retention: top-1 and top-10 share. Now: 15.76% and 81.76% FY26; top-10 80.60% at 2026-09-30; H1 top-1 NOT FOUND (B04, B05).
3. Organic versus acquired revenue: H2 FY27 revenue against the 181.91 INR Cr that the FY27 revenue guidance implies, with Alltrak and Healthcare shown separately. Now: FY26 growth largely acquired; Alltrak H1 revenue NOT FOUND (B03, B05).
4. EBITDA margin by line and price per collection. Now: 13.29% FY26, about 13% H1 FY27; segment margin and unit price NOT FOUND (B04, B09).

**C2. WHAT THE MODEL REJECTS.**
- The market-size debate. Management's 1,000 INR Cr market equals its FY30 revenue goal, and its own arithmetic gives 10,000 INR Cr (B09 note that the market figure equals the revenue goal). Execution is bound by hiring and working capital, not by market size (B09.capacity_check).
- Spot-year ROCE and ROE. They sit on mixed standalone and consolidated bases (B04.irrelevant_ratios).
- Headline FY24 to FY26 revenue and PAT growth. They are mostly acquired and not like for like (B04, B02).
- Debt-to-equity of 0.50 and the current ratio. They hide working-capital debt and receivables of uncertain quality (B04).
- ISO certifications and the ESOP pool. Table stakes and a pool with no grants (B04, B07).

**C3. THE BUSINESS FALSIFIER** (re-declares the FROM business, distinct from B6).
- Evidence that top-customer revenue is group or related-party revenue, or that top customers insource the work. FY24 top-customer revenue of 1,416.34 INR Lakhs equals FY24 services to Alltrak to the paisa (B02, an inference in B02). Thyrocare, a named client, runs its own fleet of about 2,000 to 2,100 phlebotomists (B06). Either finding would re-declare Credent from an outsourcing partner to a captive or fringe vendor.
- Evidence that chains purchase only a small share of collection and logistics from outside vendors. That share decides the real market and is NOT FOUND (B09.analyst_note). A share near zero would remove the business, not slow it.

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

Drafted at Halt 1 under the five-question spec in prompts/13-synthesis-pipeline.md. Stage 13 holds the final copy.

Credent provides three services to diagnostic labs, hospitals, and pharma and IVD firms (B04). Phlebotomists draw blood at homes and client centres, and this healthcare services line made 43.04% of FY26 revenue of 21,416.18 INR Lakhs (B04). Riders carry samples in a cold chain (logistics, 25.26%), and a third line places lab staff inside client labs (24.93%) (B04). A late or warm sample is a failed test, but labs can hire the same people, and Credent's contracts carry no firm commitment (B07, B04, B02). About 280 customers use the services, mostly diagnostic chains, hospitals and pharma firms (B05, call p.5). The top customer took 15.76% of FY26 revenue and the top ten took 81.76% (B04). Management named Dr Lal, Metropolis, Apollo, Thyrocare, Neuberg and LifeCell as clients, but no filing names a customer (B05). Demand today comes from chain test volumes and home collection, so "Thyrocare, Dr Lal, Metropolis quarterly volumes and collection-cost line" is the first outside signal (B09). The second signal is "Credent top-10 customer share and top-1 customer" (B09). Forward demand rests on market growth cited at 11.1% a year, tracked by "Organised share of diagnostics and diagnostic market growth" (B09). "NABL accreditation and diagnostic lab regulation" could push chains toward specialised handlers, and "Wockhardt and Thyrocare prepaid On-Demand wallet onboarding" adds a pay-per-order product with no revenue disclosed (B09, B05). "Labour code and minimum wage changes" sit on the cost side, since deployed people carry about 68% of revenue (B09, B04). The run did not establish what share of chain collection and logistics spend goes to outside vendors (B09). No line holds a proven moat, and the emerging moat scan scored 10.5, classification NONE (B07). Healthcare services and stationed staff are labour supply with weak pricing power (B04). Logistics has the best claim through route density, with 2,530 labs and 19,000 pincodes, but route economics are not disclosed (B04, B07). Thyrocare, a named client, runs about 2,000 to 2,100 phlebotomists of its own, so large customers can do this work in house (B06, B12b R22). Alltrak, the tracking software bought in February 2026, shows no disclosed adoption (B04, B07).

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. VERTICALS FRAMED

**Vertical 1: Cash conversion.**
- Corpus establishes: FY26 consolidated CFO (662.34) INR Lakhs against PAT 1,836.45 (B01, B02). Standalone receivables rose 126.9% on revenue +70.4%; nil provision; 240.23 INR Lakhs aged one to two years against 3.91 (B02.receivables_trend). H1 FY27 receivables 588 Mn to 788 Mn (B05). The RHP assumes 95 debtor days and 5 creditor days for FY27 and FY28 (RHP p.95, Section 6 Q3). Peers: Krystal about 118 days, TCIEXP 58 to 60 (B06).
- Cannot establish: customer credit terms, the identity of the 240.23 INR Lakhs debtors, covenants, any rating view (B02.input_gaps, B00).
- Deciding questions: (1) Do consolidated CFO and receivable days turn at H2 FY27? (2) Who owes the aged balance and is a provision booked? (3) Does the 72.25 INR Cr of unspent IPO money fund receivables rather than the stated objects?

**Vertical 2: Customer concentration and retention.**
- Corpus establishes: top 1 15.76%, top 5 59.05%, top 10 81.76% of FY26 revenue (RHP p.25-26, Section 6 Q4); top 10 at 80.60% at 2026-09-30 (B05). No top-ten customer was lost in three fiscals (RHP p.26). Contracts terminable (B04). The call says no customer above 10% (B05).
- Cannot establish: the top customer's name, whether it is related, the H1 top-1 share, the basis of the call claim (B02, B05, B08).
- Deciding questions: (1) Who is the FY26 top customer, and was the FY24 top customer Alltrak? (2) What is the H1 FY27 top-1 share? (3) Does any named chain move collection in house?

**Vertical 3: Organic versus acquired revenue.**
- Corpus establishes: three FY26 acquisitions from promoter-side owners for 1,152.23 INR Lakhs combined, goodwill 234.62 (B02, B08). Alltrak booked 172.40 of 199.64 INR Lakhs full-year profit in the 34 days after 2026-02-26 (B02). Standalone revenue grew 70.4%, or 20.1% without the operations and supply chain line (B03.guidance_table). H1 FY27 revenue 13,808.65 INR Lakhs, +53.4% (results p.5, press release p.2).
- Cannot establish: organic growth by entity, Alltrak revenue for April to September 2026 (B05, B03).
- Deciding questions: (1) What did Alltrak, Healthcare and Team each earn per half? (2) What is Alltrak's SaaS revenue policy? (3) Does H2 FY27 revenue reach the 181.91 INR Cr implied by guidance with acquired entities shown separately?

**Vertical 4: EBITDA margin by line and unit price.**
- Corpus establishes: EBITDA margin 13.29% FY26 (AR p.14); about 13% H1 FY27 (call p.7). CFO says stable at 13%, the MD says 15% to 16% in three years (call p.8). Peers: Krystal guides 6.25% to 7.5%, TCIEXP is at 11% to 13% with 15% a two-to-three-year goal (B06). Other expenses fell from 23.12% to 12.87% of revenue with no stated reason (B04.mgmt_questions).
- Cannot establish: segment margins, price per collection or per pickup, last renewal terms (B04, B09).
- Deciding questions: (1) What is the price per collection and per pickup, and how did it move at renewal? (2) What explains the fall in other expenses? (3) How much wage inflation passes through to clients?

### 4b. CANDIDATE SIGNAL TABLE

All rows are UNVERIFIED. Verification and tracker writes happen at Role 5.5 in claude.ai. Candidates come from B09.downstream_candidates (6).

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| Thyrocare, Dr Lal, Metropolis quarterly volumes and collection-cost line | Chain volumes grow well below the 45% plan, or a chain reports collection moving in house | Quarterly | Company results and concall transcripts on NSE/BSE |
| Credent top-10 customer share and top-1 customer | Top-10 share rises above 80.60% or a top-ten customer is lost (B05) | Quarterly (Credent reports half-yearly; read each filing) | Credent results press release, shareholding and results filings on NSE; FY27 AR |
| Wockhardt and Thyrocare prepaid On-Demand wallet onboarding | No On-Demand revenue line disclosed by the FY27 AR (B05 kill signal) | Quarterly | Credent concall and segment disclosure |
| NABL accreditation and diagnostic lab regulation | No tightening of chain-of-custody or temperature rules, or rules that let chains self-handle | Event-Driven | NABL and CDSCO / Ministry of Health notifications |
| Labour code and minimum wage changes | Employee expense ratio above 39.5% with no matching client price reset (B04) | Event-Driven | Ministry of Labour and Employment gazette |
| Organised share of diagnostics and diagnostic market growth | Market growth reported below the 11.1% cited, or organised-share data that stays stale | Event-Driven | CareEdge, CRISIL, ICRA industry reports |

### 4c. FRAGILITY READ

- variable_count: 7 external variables must go right for the bull case (B05 guidance, B09, B06): (1) outsourced share of chain pre-analytics spend; (2) top-ten customers stay and keep volume; (3) customers pay on 30 to 45 day terms; (4) wage and labour-code cost passes through; (5) named customers do not insource or densify labs; (6) new enterprise and mid-size client wins and On-Demand uptake; (7) acquired revenue, mainly Alltrak, persists.
- verifiability_ratio: 4 of 7 externally observable. Observable: (1) in chain filings, (2) in chain volume reports, (4) in gazette notices, (5) in customer concalls. Company-narrated only: (3) collection days, (6) client wins, (7) Alltrak revenue (B05, B09.demand_externally_verifiable).
- single_point_failure: YES. Loss or insourcing of one top customer. The top customer is 15.76% of FY26 revenue, the top ten are 81.76%, and contracts are terminable with no firm commitment (B04, B02).
- fragility_verdict: FRAGILE (many variables, three company-narrated only, and one kill-switch).

### 4d. RESEARCH BRIEF (the claude.ai work order; live-web work the corpus cannot do)

1. PENDING LIVE VERIFICATION (Chain 1, counterparty payment terms). Open the FY2025-26 annual reports of Dr Lal PathLabs, Metropolis and Thyrocare, the clients management named on the call. Read the trade payables note and any MSME vendor payment-days note. Read the vendor payment policy on the Thyrocare Q2 FY27 call.
2. PENDING LIVE VERIFICATION (Chain 2, insourcing). Open the Thyrocare Q2 FY27 investor presentation (NSE filing, call held 2026-10-29) and the Thyrocare FY2025-26 annual report. Read the lab roll-out schedule, in-house phlebotomist headcount and any disclosure of outsourced collection or logistics vendors.
3. Identify the FY26 top customer (15.76%). Search customer-side related-party and vendor disclosures and MCA filings. Test whether the FY24 top customer was Alltrak (B02).
4. MCA shareholder list, OCPS holders and charge filings for Kartavya Healtheon Private Limited (B08 gap; paywalled or blocked).
5. Request through Role 5.5 the Alltrak monthly revenue for April to September 2026 and its SaaS revenue policy (B02, B03 separator).
6. Check whether a bank-facility credit rating rationale exists on CRISIL, ICRA, CARE, India Ratings and Acuite sites. Check the HDFC 260 limit that B02 calls undisclosed.
7. Fetch the 13 uncollected NSE filings since listing, the final prospectus with issue price, any IPO monitoring agency report, and the quarterly shareholding filings (B00.input_gaps).
8. Search SEBI, NSE surveillance, eCourts, NCLT and MCA compounding orders for the promoters and Credent Healthcare (B08.searches_skipped).
9. Proxy advisor, forum and news archaeology on the promoters and the 2025-09-08 auditor resignation (B08.searches_skipped).
10. Policy status: labour code implementation date and state minimum wage notifications that touch contract staff cost.
11. Chain 3 (to build): wage inflation and labour-code pass-through. Live link needed: Krystal and TCIEXP contract-reset terms and labour-code recovery wording (B06 risks_peers_raise), plus the Ministry of Labour notification.
12. Chain 4 (to build): Alltrak and the acquired-revenue run rate. Live link needed: Alltrak filings on MCA and any Alltrak customer disclosure.
13. Chain 5 (to build): IPO use and group lending. Live link needed: the Kartavya Healtheon loan agreement date, owners and the H2 utilisation report.
14. Chain 6 (optional, to build): Thyrocare lab densification against long-haul sample logistics (B12b R23). Live link needed: Thyrocare lab count by quarter.
15. Re-fetch the Dr Lal PathLabs Q4 FY26 release for the collection-centre fee ratio (14.5%, blocked in B09). Find any chain note that splits collection cost between in-house and outsourced.
16. Source URL verification for B09 market data (CareEdge November 2023, Business Standard June 2022, NATHEALTH 2019) and a FY26 average INR/USD rate (B09 stale-data list, B09 FX note).
17. Company IR page: recording or notes of the 2026-11-12 investor meeting and the H1 FY27 audio-recording link left out of the corpus (B00.input_gaps).

### 4e. SECOND-ORDER STUB (Master Prompt v3.7, Rule F)

Two chains drafted from the corpus. Facts carry block cites. Every inference carries the label [INFERENCE]. No counterparty fact is asserted: the who-pays link is PENDING LIVE VERIFICATION in each chain.

```
CHAIN 1: Receivables rose from 5,882.73 INR Lakhs (2026-03-31) to 7,884.82 INR Lakhs (2026-09-30) in a half with no new acquisition, while consolidated CFO was (392.43) INR Lakhs in H1 FY27 and (662.34) in FY26 (results p.4; B03 cash note; B01).
Link 1 [filed, H1 balance sheet and cash flow]: Trade receivable grew by 2,002.09 INR Lakhs in six months (results p.4 and p.6). Management says debtors age 60 days and that new clients get 30-day terms, with older clients on 45 to 60 days (call p.14, p.16; B05).
Link 2 [PENDING LIVE VERIFICATION]: Who pays, and why now. The paying side is the diagnostic chains management named as clients (call p.12). Claude web must open the FY2025-26 annual reports of Dr Lal PathLabs, Metropolis and Thyrocare and read the trade payables and MSME vendor payment-days notes. The stub asserts no counterparty payment fact.
Link 3 [INFERENCE]: The top ten customers hold 81.76% of revenue (B04). Terms agreed with new clients move the blended collection days slowly, because the old clients dominate the book. Customer behaviour, not Credent policy, would then set the pace of cash conversion.
Binding constraint: Working capital. The RHP assumes 95 debtor days against 5 creditor days for FY27 and FY28 (RHP p.95). Receivables absorbed 2,002.09 INR Lakhs in one half, against 7,225 INR Lakhs of unspent IPO money at 2026-09-30 (results Annexure A, p.19).
Unsaid: Unbilled revenue of 874.55 INR Lakhs (consolidated) is the auditor's Key Audit Matter, 240.23 INR Lakhs sits in the one-to-two-year bucket against 3.91, no provision exists, and the ageing runs from invoice date with no not-due bucket (B02 top finding 1; AR Note 15 p.84). The call says "as such no risk into the business" (call p.18; B05).
Observation that confirms or breaks this chain, and confirm-by date: H2 FY27 results filing (no date in the corpus; the H1 filing came 28 days after period end, B00-intake). Confirms: consolidated CFO positive, CFO/PAT at or above 0.7, receivable days including unbilled at or below 80, 1-2 year bucket below 100 INR Lakhs (B03.monitorables). Breaks: days above 100 and CFO negative (B05 trigger 3 kill signal).
```

```
CHAIN 2: The top ten customers gave 81.76% of FY26 revenue and the top customer gave 15.76% (3,374.48 INR Lakhs), with no firm customer commitments (RHP p.25-26; B04 concentration note; B02).
Link 1 [filed, RHP risk factor 1]: "While we have not had any instances of loss of our top 10 customers by revenue in the last three Fiscals, there can be no assurance that it will not happen in the future" (RHP p.26). Contracts are terminable on notice and carry price-cut risk (B04, RHP p.27 as cited in B04).
Link 2 [PENDING LIVE VERIFICATION]: Who pays, and why now. Thyrocare is a named client on the call (call p.12) and runs about 2,000 to 2,100 phlebotomists in house and is adding labs so fewer samples reach its central lab (B06; B12b R22, R23). Claude web must open the Thyrocare Q2 FY27 investor presentation (NSE filing for the call of 2026-10-29) and the Thyrocare FY2025-26 annual report, and read the lab roll-out and vendor disclosure. The stub asserts no counterparty plan.
Link 3 [INFERENCE]: A chain that adds labs shortens the sample haul, so the logistics line (24.81% of H1 revenue, press release p.3) loses distance-based work first. A chain with its own phlebotomists reduces the pool for the healthcare services line. Contracts that end on notice let either shift happen without a breach.
Binding constraint: Contract terms. No firm commitment and termination on notice (B04). Revenue durability rests on relationships, with no multi-year lock-in evidenced.
Unsaid: FY24 top-customer revenue of 1,416.34 INR Lakhs equals FY24 services to Alltrak to the paisa (RHP p.216; B02, an inference in B02), and Alltrak was a promoter-side company until 2026-02-26 (B03). The call names clients but gives no revenue by customer and says no customer exceeds 10% (call p.5, p.12; B05).
Observation that confirms or breaks this chain, and confirm-by date: H2 FY27 results filing and the FY27 AR (no dates in the corpus). Confirms: top-ten share below 80.60% (press release p.3), top-1 share disclosed and at or below 15.76%, customer disclosure in the FY27 AR (B03.monitorables). Breaks: any top-ten customer lost, or the top-ten share rising above 80.60% (B05 trigger 4 kill signal).
```

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in claude.ai with live web, before Role 2.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. Credent is a Delhi firm that collects and moves medical samples for labs. It listed on NSE Emerge on 2026-08-20 (B00, B04).
2. It has three main lines in FY26: healthcare services 43.04%, logistics 25.26%, and operations and supply chain 24.93% (B04).
3. It bills per collection, per pickup or per stationed person. No filing states the price of one unit (B04, B09).
4. Its customers are diagnostic chains, hospitals and pharma firms. Ten of them gave 81.76% of FY26 revenue (B04).
5. Management says labs gain a variable cost in place of a fixed cost by hiring Credent (call p.13; B05).
6. Demand rests on chain test volumes and home collection. Market growth is cited at 11.1% a year (B09).
7. Management plans about 45% yearly growth to FY30. The AR says FY26 growth came largely from three acquired firms (B05, B03).
8. No peer shows 45% organic growth. Peers cite market growth of 10% to 11% (B06).
9. Profit is not turning into cash. FY26 CFO was (662.34) INR Lakhs against PAT of 1,836.45, and H1 FY27 CFO was Rs (39) Mn (B01, B02, B05).
10. No business line holds a proven moat. The best claim is logistics route density, which is not yet measured (B07, B04).
11. The draft model: a labour-supply outsourcer at the R1 to R2 boundary claims a climb to R3. Proof comes from margin and cash at H2 FY27 (Section 2).
12. The fragility verdict is FRAGILE. Seven outside variables must go right and one lost top customer could break the case (Section 4c).
13. The run did not establish the price per collection, margin by line, the top customer's name, Alltrak's H1 revenue or Kartavya's owners (B04, B05, B08).
14. Open question one: is growth organic? The call says yes and the AR says largely acquired. Alltrak earned 172.40 of 199.64 INR Lakhs profit in 34 days (B05, B03, B02).
15. Open question two: why does the call say no customer exceeds 10% when the filings show 15.76%? Also, why did a 450.00 INR Lakhs loan to Kartavya go out six days later (B05, B08)?

---

## SECTION 6: STANDING EXTRACTION ANNEX

Quote-then-comment. Page anchors follow the page-marker convention of the .txt files unless noted. Where a printed folio differs, the note says so. The concall and the H1 results are scanned: OCR text was checked against the page image where marked.

### Q1. UNITS

- No per-unit price is printed. Quote: "we are charging on per collection, per pickup basis, so volume will be increased, that's why only the value should be increased" (CREDENT-Concall_H1FY27_2026-10-29_Transcript.pdf p.9). Quote: "Per patient, per collection is our collection revenue, per center, per pickup is our logistic revenue" (same file, p.10). Quote: "No, sir, it's a value growth." (p.9).
- Comment: the basket is three revenue lines, each billed on its own unit. Collection is per patient, logistics per pickup, and stationed staff per head (B04). No volume of collections or pickups is printed, so no price per unit can be derived (B09.input_gaps). The call says Credent does not realise "on a per test basis" (p.10).
- Derivable lines. FY26 revenue 21,416.18 INR Lakhs and 6,338 people at year end (AR p.3 and p.18, CREDENT-Annual_Report_FY2025-26.pdf). B04 derives 3.38 INR Lakhs per head. The base is mixed: year-end heads against revenue that includes part-year acquired entities (B04.unit_economics).
- Other printed counts: "relationships with 2,530 diagnostic laboratories nationwide" and "a fleet of 97 commercial vehicles and a workforce of 2,589 riders" (AR p.3). "Resources deployed (no.) 6789 6338 5711" at 2026-09-30, 2026-03-31 and 2025-09-30 (CREDENT_28102026191521_PressFinal.pdf p.3).

### Q2. SEGMENT CAPITAL AND DEBT

- Quote: "The Group has evaluated its operations and has concluded that its activities constitute a single reportable business segment" (AR p.107, consolidated note 11). Standalone: "operates in a single business segment" (AR p.79). H1 FY27: "operates in a single business segment" (CREDENT-H1FY27-results-outcome-BM-2026-10-28.pdf p.7).
- Comment: NOT DISCLOSED by segment. Segment assets, segment liabilities, capital employed and allocated borrowings are not printed, because AS 17 reports a single segment. Borrowings are unallocated.
- Totals (consolidated, INR Lakhs, H1 results p.4, checked on the page image): long-term borrowings 198.08 at 2026-09-30 and 519.80 at 2026-03-31; short-term borrowing 1,964.16 and 1,674.95; total assets 18,200.92 and 8,156.82. The press release prints "total borrowings of ₹21.62 Crore" at 2026-09-30 (PressFinal.pdf p.2).
- Cash correction (Verifier A): balance-sheet "Cash and Bank Balances" is 7,419.72 INR Lakhs at 2026-09-30 (results p.4). The cash flow statement shows cash and cash equivalents of 6,919.72 (results p.6). The 500.00 gap is fixed deposits. The cash flow also shows purchase of fixed assets (443.12) and FD investment (656.67) (results p.6, image-checked by Verifier A).

### Q3. GUIDANCE VERSUS ASPIRATION

| Item | Quote and anchor | Class |
|---|---|---|
| FY27 revenue | "approximately INR320 plus crores of revenue in this year FY27" (call p.10). Press release: "Company guides for FY27 consolidated revenue of ¥320 Crore plus and PAT of ¥28 Crore" (PressFinal.pdf p.2); FY27 guidance table prints 320 plus and 28.00, PAT margin "~8.75%" (p.4) | (a) guidance with a period |
| FY27 H2 path | "Meeting guidance implies H2 FY27 revenue of about 3181.91 Crore and PAT of about 313.35 Crore" (PressFinal.pdf p.4, OCR; B05 reads 181.91 and 13.35 INR Cr) | (a) derived by the company, period H2 FY27 |
| Revenue growth to FY30 | "approximately 45% revenue CAGR through FY30 and 5x multiple from the 2026 revenue" (call p.6); "This is an ambitious growth objective" (p.6) | (a) with period FY30, long range |
| FY30 revenue | "somewhere around of INR1,000 crores plus minus 10%, 15% in 2030" (call p.10) | (a) with period 2030, hedged by "tentatively" |
| FY30 profit | "it's around INR100 plus crores of PAT" (call p.10); "INR 1,000 crores of revenue tentatively in 2030 with the PAT of 10%" (p.11) | (a) with period 2030 |
| EBITDA margin | "the EBITDA margin would remain stable at 13%" and "So, we will reach around 15% to 16% of EBITDA margin over the three years" (call p.8); "with the PAT EBITDA of 15% to 16% of revenue" (p.11) | (a) three years, undated start; the two quotes disagree (B05 FLAG-CALL-CONSISTENCY) |
| H2 margin | "we expect EBITDA margins to improve in the second half as new deployments mature and route density increases" (PressFinal.pdf p.3) | (a) period H2 FY27, no number |
| Enterprise and mid-size clients | "we are adding this year approximately two enterprises new clients for this listing" (call p.9); "one enterprise client is giving us approximately INR12 crores to INR18 crores of revenue in a year" and "INR4 crores to INR6 crores" for a mid-size client (p.9) | (a) period FY27; the client revenue range is (c) capability |
| Debtor days | "our aging in terms of debtors is 60 days" (call p.14) and "we try to close the aging of the debtors less than 45 days" (p.16) | 60 days is a present claim, not guidance; under 45 days is (b) aspiration, no period |
| Cash flow positive | "Maybe by next year, H2." (call p.16) | (b) hedged, no firm period; B05 reads H2 FY28 |
| Fleet | "till the INR1,000 crores of revenue, our fleet size should be around 15,000 to 16,000" and "maybe 20,000 of employment" (call p.11) | (c) capacity |
| Capex | "we do not require much more capex in terms of Credent because Credent is a low capex company" (call p.11); "for organic business, till 2030 we are not looking for the funds" (p.14) | (c) capability |
| Main board | "INR1,000 crores of revenue we migrate to the main board in FY30" (call p.14) | (a) period FY30 |
| M&A | "the multiple of 10 to 12 kind of multiple companies with the revenue of less than INR 100 crores" (call p.12); "Till today we don't have any finalizations." | (c) criteria only |
| Overseas | "we are not expanding this year overseas, but maybe next year or after next year we will expand surely" (call p.17) | (b) aspiration, loose period |
| Market size | "is minimum tentatively INR1,000 crores of revenue" (call p.13) | (b) not guidance; B09 notes it equals the FY30 revenue goal |

Comment: only the FY27 revenue and PAT figures are formal guidance in a filed document. The FY30 figures are spoken. RHP assumption for FY27 and FY28: "Debtors Turnover days 73 68 96 95 95" and "Creditors Turnover days 10 7 5 5 5" (RHP p.95), with "the holding level for debtors is anticipated at 95 days" (RHP p.95). The call says 60 days now and under 45 days later (B05).

### Q4. CONCENTRATION

- Customer. Quote: "Top 1 Customer 3,374.48 15.76% 1,748.59 22.43% 1,416.34 18.70%" (CREDENT-RHP-Aug-2026.pdf p.25, INR Lakhs, FY26, FY25, FY24). "Top 5 Customer 12,645.59 59.05% 4,368.41 56.05% 4,950.54 65.37%" and "Top 10 Customer 17,509.03 81.76% 6,493.08 83.31% 6,658.53 87.92%" (RHP p.26). AR: "the top 10 customers contributed 81.76% of FY26 revenue (83.31% in FY25, 87.92% in FY24), with the single largest customer contributing 15.76%" (AR p.14). Press release: "Top 10 customers' share of revenue (%) 80.60% 81.76% 84.20%" at 2026-09-30, 2026-03-31, 2025-09-30 (PressFinal.pdf p.3).
- Call: "no single customer contributed more than 10%" (call p.5). Comment: the call names no period. The H1 FY27 top-1 share is NOT DISCLOSED. The customer name is NOT DISCLOSED in any filing (B04, B05).
- Product (revenue line, FY26). Healthcare Services 43.04%, Logistics 25.26%, Operations and Supply Chain 24.93% (AR p.3). AR p.11 prints "Operations&SupplyChainManagement ... 27.67%" and "other services contributing ... 4.03%", so the AR gives two mixes. H1 FY27: "Healthcare services share of revenue (%) 45.84%", "Logistics services share of revenue (%) 24.81%", "IT, Operation and Supply chain, etc % 29.35%" (PressFinal.pdf p.3). Top product share: healthcare services.
- Geography. "Maharashtra 6,296.35 29.40%" and "Uttar Pradesh 5,745.83 26.83%" of 21,416.18 INR Lakhs (AR p.13). Together 56.23%. Comment: all revenue is in India (AR p.79).

### Q5. PROMISE LEDGER

Dated promises only. Built from stated intent in the RHP, listing deck and AR against H1 FY27 results, because there is one call and no earlier call (B05.input_gaps). Counts: 2 delivered, 5 partial, 0 missed (B05).

| Promise | Made | Status | Evidence anchor |
|---|---|---|---|
| Repay 6.00 INR Cr of borrowings in FY27 | RHP, 2026-08-08 | Delivered | Results Annexure A: repayment 6.00 utilised, unutilised 0.00 (results p.19, OCR). Gross borrowings 219 Mn to 216 Mn as short-term rose (B05) |
| No specific acquisition identified | RHP, 2026-08-08 | Delivered | "Till today we don't have any finalizations." (call p.12). The Kartavya loan with an equity option is outside this test (B05) |
| Deploy 29.50 INR Cr to working capital in FY27 | RHP, 2026-08-08 | Partial | 5.31 INR Cr utilised by 2026-09-30, about 18% (results p.19; B05) |
| Spend 3.00 INR Cr on 14 sonography and 4 X-ray machines in FY27 | RHP, 2026-08-08 | Partial | RHP: "231.90 Lakhs ... fourteen (14) sonography machines" and "73.08 Lakhs ... four (4) digital X-ray machines" (RHP p.94). Nil utilised (results p.19); call says low capex |
| About 45% revenue CAGR through FY30 | Listing deck, 2026-08-20 | Partial | H1 FY27 +53.4%, includes Alltrak and Team absent from H1 FY26 (PressFinal.pdf p.2; B05) |
| Pay-per-order models for smaller providers | RHP, 2026-08-08 | Partial | On-Demand platform launching, two clients named, revenue and rate not disclosed (call p.14 to p.16; B05) |
| EBITDA margin to improve in H2 as deployments mature | Press release, 2026-10-28 | Partial | Not yet testable (PressFinal.pdf p.3; B05) |

Comment: B05 grades credibility C. Verifier B concurs lower, at the C/D boundary, citing selective naming of prepaid clients to one analyst on the call (p.15) and two refusals on the volume-price and acquired-entity questions (B12b). Both extra checks are open items for Role 5.5.

### Q6. RESTATED BASES

- Quote (RHP, restated): "Net Profit/(loss) after Tax as per audited accounts but before adjustments for restated accounts:(a) 1,836.45 553.23 340.86" and "Net Profit/(Loss) After Tax as per Restated Accounts:(a+b) 1,844.78 224.67 266.44" for FY26, FY25, FY24 in INR Lakhs (RHP p.193, marker; printed folio 189). The unbilled revenue adjustment reads "(388.05)" in FY25 and "(89.72)" in FY24 (same page).
- Quote (AR comparatives, unrestated): "Profit after tax (PAT) for FY 2025-26 stood at ₹1,836.45 lakhs (consolidated) as against ₹553.23 lakhs in FY 2024-25 (standalone)" and "compared to standalone revenue of ₹8,182.32 lakhs in FY 2024-25" (AR p.13). The RHP prints the restated FY25 revenue as 7,794.26 (RHP p.30, half-yearly revenue table total; B02).
- Quote (reclassification note, H1 results): "Figures for the previous periods / year have been regrouped, rearranged or reclassified wherever necessary to conform to the classification of the current" (results p.7). The note names no reorganisation.
- Comment: FY24 and FY25 are standalone restated; FY26 is consolidated and includes three acquired entities, so the years are not like for like (B00, B03). The H1 deck labels FY25 revenue 818 Mn and PAT 55 Mn as restated, yet these equal the unrestated AR figures. The listing deck shows restated 7,794.26 and 224.67 INR Lakhs (B04 FLAG-DECK-INCONSISTENCY). The latest H1 FY27 filing prints H1 FY26 comparatives of 9,002.96 INR Lakhs revenue and 752.51 PAT (results p.5, OCR).

### Q7. CORPORATE-ACTION CLAUSES

No scheme, demerger or merger exists in the corpus. Quote: "Except as disclosed above, our Company has not made any material acquisitions or divestments of any business or undertakings, mergers, amalgamation or revaluation of assets in the last 10 years" (RHP p.152, printed folio 148). No share repurchase is recorded in the notes read (AR p.81, Note 2.5). The filings to fetch for any later scheme are NSE Reg 30 announcements.

Acquisitions (the corporate actions in the corpus). Quotes from RHP p.152-153 (printed folios 148-149):
- Healthcare: "Our Company has acquired the shares of Credent Healthcare Private Limited by Agreement dated April 01, 2025" and "Share purchase agreement dated April 02, 2025 ... has acquired 100,000 equity shares from Ashok Kumar Sharma and Dimple Sharma ... for a total consideration of ₹ 11,45,20,000". Valuer's per-share figure: "₹ 11,440.00 per share. The valuation was determined using the method Adjusted NAV Method." The SPA carries "indemnity clauses covering losses arising out of the breach of agreement". The RHP prints two dates, April 01 and April 02, 2025. AR Annexure A prints "Subsidiary w.e.f 02.04.2025, further become Wholly Owned Subsidiary w.e.f October 05, 2025" (AR p.92).
- Team: "Share purchase agreement dated October 10, 2025 ... Karan Sharma and Dimple Sharma ... for a total consideration of ₹ 6,00,000" at "₹ 12 per share". AR p.92: "Wholly Owned Subsidiary w.e.f December 26, 2025".
- Alltrak: "Share purchase agreement dated October 10, 2025 ... Amit Gupta and Tarun Sharma ... a total consideration of ₹ 1,00,000 ... All the share were acquired on face value of share i.e. ₹ 10/- each." AR p.92: "w.e.f February 26, 2026".
- Comment: no undertaking definition, liability allocation clause or ratio applies, since these are share purchases. The AR p.11 control dates (December 26, 2025 and February 26, 2026) follow the SPA dates by about 2.5 and 4.5 months (B02). The cash flow note and Note 1 say Healthcare was consolidated from 2025-04-02, while AR p.11 says 2025-10-08 (B03, B04).

Issue of shares.
- Bonus: "1,29,95,000 Bonus Equity Shares of ₹10/- each to shareholders in the ratio 50:1" (AR p.33); date "09th February, 2026" (AR p.81).
- Loan conversion: "59,900 Equity Shares of ₹10/- each for consideration other than cash, pursuant to conversion of loan into equity" (AR p.33). Conversion amount 944.02 INR Lakhs (B02).
- IPO: "INITIAL PUBLIC OFFER OF UPTO 49,68,000* EQUITY SHARES OF FACE VALUE OF ₹ 10/- EACH" (RHP cover, p.1-2; issue price blank in the RHP). Gross raised "₹93.90 Crore" (call p.13; PressFinal.pdf p.2). Final prospectus absent.

Inter-corporate loan to Kartavya Healtheon (a new corporate action, not a scheme). Quote: "Interest: Nil up to 25 November 2026. After that, on unsettled principal, 12% per annum, compounded monthly" and "Such percentage, up to 26%, of the equity share capital through primary/secondary on a Fully Diluted Basis as the Lender elects"; "Nature of loan: Unsecured"; "Whether, the said parties are related ... No"; "The Borrower shall apply the whole of the Loan only towards repayment of its OCPS and other loans" (CREDENT_04112026205344_C3_Disclosure_merged__1_.pdf p.2-3; the board outcome CREDENT_04112026204029_C3_Outcome_BM_merged.pdf is dated 2026-11-04). The agreement execution date is NOT DISCLOSED in the filing (B05).

### Q8. RELATED-PARTY PERIMETER

Latest year FY2026, INR Lakhs. AR Annexure A, standalone (AR p.92-93) and consolidated (AR p.119-120). Quote: "There have been no guarantees provided or received for any related party receivables or payables" (AR p.93). Comment: B02 notes a corporate guarantee of 261.31 for a subsidiary's Axis facility that CARO lists and the contingent liability note omits.

| Party (as named) | Nature | FY26 amount as printed |
|---|---|---|
| Credent Healthcare Pvt Ltd (ex Credent Managements and Consultants) | Entity owned or influenced by directors; interest and loans | "Interest Expenses during the year 59.25"; loan taken 2,529.76; repaid 2,577.75; "Closing Balances ... Loan Taken 452.78" (AR p.92) |
| Credent Team Pvt Ltd | Same | Professional fees "-" (FY25 15.27); loan given closing 0.00 (AR p.92) |
| Alltrak Technologies Pvt Ltd | Same; customer and borrower | "Services rendered by the company including unbilled services 130.33" (FY25 869.38); interest received 26.00; debtors 374.17; "Closing Balances ... Loan Given 285.24" (AR p.92) |
| Credent Foundation | Group entity | Named; no transaction printed (AR p.92; B03) |
| Karan Sharma (WTD) | Director | Remuneration 18.66; loan closing 23.43 (AR p.92) |
| Dimple Sharma | Director | Sitting fees 0.24; loan taken 584.00; conversion to share capital 472.01; repaid 52.57; closing 125.42 (AR p.93) |
| Tarun Sharma (MD) | Director | Loan taken 203.86; repaid 183.64; closing 20.21 (AR p.93). Alltrak paid him 24.00 remuneration (consolidated, AR p.120) |
| Ashok Kumar Sharma | Director | Loan taken 573.97; conversion 472.01; repaid 2.49; closing 99.47 (AR p.93) |
| Tanveen | Promoter and significant control | Salary 17.96; loan 5.91 taken and repaid (AR p.93) |
| Paras Gemini | Director's brother | Salary 7.06; reimbursement 4.54; loan 9.00 taken and repaid (AR p.93) |
| Shivani Sharma | Director's wife | Salary 18.00 (consolidated, AR p.120) |
| Amit Gupta (COO) | KMP | Remuneration from subsidiary 22.50 (consolidated, AR p.120) |
| Kishore Gemini | Brother of Dimple Sharma | Reimbursement 0.31 (AR p.93) |
| Karan Sharma HUF, Tarun Sharma HUF, Ashok Kumar Sharma HUF | HUFs of directors | Named; no transaction printed (AR p.92) |

Comment: the Kartavya Healtheon loan is dated 2026-11-04, after the AR, and the company states Kartavya is unrelated. It does not appear in the AR RPT note (B02).

### Q9. PLEDGE AND SHAREHOLDING

- Twelve quarters as filed: NOT DISCLOSED. The company listed on 2026-08-20, so only two NSE XBRL filings exist (CREDENT-shareholding-pattern-19-AUG-2026-NSE-XBRL.txt and CREDENT-shareholding-pattern-30-SEP-2026-NSE-XBRL.txt).
- Promoter: 11,616,300 shares on both dates; "0.6375" of total shares on 2026-09-30 (XBRL ShareholdingAsAPercentageOfTotalNumberOfShares, promoter group context). Total shares 18,222,900 (30-SEP file).
- Pledge: "WhetherAnySharesHeldByPromotersAreEncumberedUnderPledged ... false" and the non-disposal and other-encumbrance fields "false" on both dates. Pledge is nil.
- Institutional, 2026-08-19 and 2026-09-30 (fractions as printed): alternative investment funds 0.0722 then 0.0541; domestic institutions 0.0923 then 0.0571; foreign institutions 0.0306 then 0.0213. The 30-SEP file also prints sovereign wealth funds (domestic) 0.003 and public 0.3625.
- Pre-IPO (RHP p.80 marker, printed folio 76): promoters held 20,00,000 shares, 100.00% at 2024-08-07, each of two founders 50.00% (B12a). Comment: B01 records pre-IPO promoter holding 87.52% on an unpaged RHP cite (B12c G02). The fall of domestic institutional holding between the two XBRL points is a fact to ask about at Role 5.5.

### Q10. VERIFICATION

Documents quoted, with date:
- CREDENT-Annual_Report_FY2025-26.pdf (AR for year to 2026-03-31; filing letter 2026-09-05).
- CREDENT-H1FY27-results-outcome-BM-2026-10-28.pdf (2026-10-28; balance sheet page 4 checked on the page image by Verifier A and this stage).
- CREDENT-Concall_H1FY27_2026-10-29_Transcript.pdf (call 2026-10-29; filing letter 2026-11-03; OCR text, page markers used).
- CREDENT-RHP-Aug-2026.pdf (2026-08-08).
- CREDENT_28102026191521_PressFinal.pdf (2026-10-28).
- CREDENT_04112026204029_C3_Outcome_BM_merged.pdf (2026-11-04).
- CREDENT_04112026205344_C3_Disclosure_merged__1_.pdf (2026-11-04).
- CREDENT-shareholding-pattern-19-AUG-2026-NSE-XBRL.txt (DateOfReport 2026-08-19).
- CREDENT-shareholding-pattern-30-SEP-2026-NSE-XBRL.txt (DateOfReport 2026-09-30).
- Held but not quoted: the other announcement PDFs (2026-09-05, 2026-09-18, 2026-09-29, 2026-10-01 voting result, 2026-10-01 auditor appointment, 2026-11-08 intimation). They were taken from B00-intake and B08.

Page-anchor note: B05 and B08 cite some call pages by printed folio, which run one page apart from the .txt markers (B12a, B12b). This annex uses the .txt markers.

Corpus committed at 835a6ea40e80f0e4e3e668879edeab6d30899b54 (ancestor of the hash below).

CORPUS COMMIT HASH: b911be66ba9b4942296587394babe2a59c4f03c0
