# AVANA (Avana Electrosystems Ltd): Halt 1 Understanding Dossier

Run: avana-2026-10-05. Stage 09b. Run date 2026-10-05. Corpus commit hash for Section 6: 9a6a995495514f2a47c95954a4d39eab6eccbbc0.

This is an understanding package. It carries no valuation and no recommended action. Every number carries its block cite. Units: figures marked "lakh" are printed in INR lakh (100 lakh = 1 Cr); the filings, not the file names, set the unit. Verifier A corrections bind (B12a): H1 FY26 revenue from operations is 3,574.71 lakh = Rs 35.75 Cr (the 36.28 Cr figure in B00 LBF4 is total income); the FY26 contingent total is 679.22 lakh (the 996.52 lakh figure is the FY25 column); panel output of 886 sits at AR p85 and the 600 and 1,500 capacity figures at RHP p104.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

Inventory only. No analysis. Source: B00.

1. CONCALLS. None held. B00 declares NO-CONCALL MODE (manifest concalls_available false; no earnings call found on screener, NSE or the web) (B00.run_mode). Most recent quarter covered by a transcript: none. The company files half-yearly as an NSE Emerge SME (B00.corpus_manifest). The latest filed period is H2 and FY26 to 31-Mar-2026. The next half-year to 30-Sep-2026 has not plausibly reported by 2026-10-05, so no more recent transcript is expected to be missing. Peer transcripts held: DANISH H1 FY26 (Nov-2025) and DANISH H2 and FY26 (11-May-2026) (B00).
2. ANNUAL REPORTS. One held: AVANA-AR-FY2025-26-with-AGM-notice.pdf (16th AGM notice cover letter to NSE 03-Sep-2026; financial statements signed 21-May-2026). The latest completed FY is present. Fewer than 3 years are held: FY23, FY24 and FY25 come only from the RHP restated financials, because the pre-IPO private company ARs are not in the corpus (B00.input_gaps). AR pages 2-4 and 99-127 were transcribed from page images (second-hand reading).
3. RESULTS FILINGS. Latest: audited H2 and FY26 results, board outcome of 21-May-2026 (scanned, 2 of 16 pages carry text), and its legible re-filing of 23-Jun-2026 with the unmodified-opinion declaration and the auditor working-capital utilisation certificate (B00). No quarter gap between the latest results and the AR: both cover FY26. H1 FY26 (Sep-2025) results predate listing and sit in the RHP restated financials (B00).
4. INVESTOR PRESENTATIONS. None held. The presentation folder is EMPTY. No company investor presentation was found on NSE filings since listing (B00.input_gaps). Peer decks held: MARINE (Oct-2025) and SPCL (Dec-2024) (B00).
5. RESEARCH / RATING. Rating folder EMPTY: no credit rating document found; B00 records rating_wc_quote unresolved. Research folder EMPTY: no broker or research note collected.
6. CORPORATE ACTIONS. Ten NSE-sourced announcement filings are held, dated 10-Feb-2026 to 29-Sep-2026 (B00.corpus_manifest): Reg 30 vendor registrations (10-Feb-2026; MPPTCL 400 kV C&R panels, CSPTCL SCADA up to 220 kV), CS resignation (30-Mar-2026), board outcome with CS appointment (10-Apr-2026), reply to an NSE surveillance query (11-Apr-2026), Reg 31(4) promoter encumbrance declaration (filed 15-Jun-2026, scanned), reply to NSE with results re-filing (23-Jun-2026), board outcome with KIADB integrated unit update (19-Aug-2026), newspaper AGM notice (05-Sep-2026), AGM proceedings (28-Sep-2026) and scrutinizer voting results (29-Sep-2026). Also held: the RHP dated 31-Dec-2025 (399 pages) and the shareholding pattern XBRL at 31-Mar-2026.
7. FRESHNESS PAIR CHECK. B00.freshness_verdict is FRESHNESS PAIRS OK. RESULTS to CONCALL: SKIPPED (concalls declared none). RATING BULLETIN to RATIONALE: PASS (no rating document). SEBI ORDER to ORDER TEXT: PASS (no SEBI order referenced). AR to LATEST AUDITED ANNUAL RESULTS: PASS (FY26 AR held against the 21-May-2026 results). No failed pair.
8. EMPTY-FOLDER LIST (repeated from B00.empty_folder_confirmation). Empty: presentation, rating, research. Concalls: declared none. The empty-folder question was suppressed under the /step1 autonomy contract, with the standing answer to continue with the gaps.

VERDICT LINE: **CORPUS GAPPED**

Missing documents, each with expected source and kind:

| Document | Expected source | Kind |
|---|---|---|
| Company investor presentation | company IR page / NSE | plausibly-nonexistent (none on NSE since listing; opacity data point) (B00) |
| Earnings call transcripts or audio | company IR page / NSE | plausibly-nonexistent (no calls found; SME half-yearly cadence) (B00) |
| Credit rating rationale | rating agency site (CRISIL, ICRA, CARE, India Ratings, Acuite, Infomerics) | findable-missing (unrated status unconfirmed; a check on agency sites settles it) (B00; gate-recommendation) |
| Broker or research note | none expected for an NSE Emerge name | plausibly-nonexistent (B00) |
| Final prospectus dated 14-Jan-2026 | NSE | findable-missing (the RHP held carries the same restated financials and objects) (B00) |
| Annual reports FY23 to FY25 | company IR page | plausibly-nonexistent as listed-company ARs (pre-IPO private company) (B00) |
| Promoter-group revision filing of 23-Jan-2026 | NSE | findable-missing (taken from the task brief in stage 8, filing not in corpus) (B08.input_gaps) |
| KIADB extension letters naming the extended date | company (operator request to the company) | findable-missing (B03, B05) |
| Shareholding pattern for the quarter to 30-Jun-2026 | NSE | findable-missing (corpus holds only 31-Mar-2026; no 30-Jun-2026 filing is listed in B00) |
| Shareholding pattern for the quarter to 30-Sep-2026 | NSE | not yet due (due by 21-Oct-2026) (B00) |
| H1 FY27 results and utilisation certificate | NSE | not yet due (half-year ended 30-Sep-2026; filing date NOT FOUND) |
| Lease renewal evidence for both operating units | Reg 30 filing or management reply | findable-missing (B03) |

No freshness pair failed, so the verdict is not CORPUS GAPPED-FRESHNESS.

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT - PENDING OPERATOR SIGN-OFF**

This declaration is a draft for the operator. It is not signed. Signing happens only in claude.ai after live-web stress-testing. Every statement below is drawn from committed blocks.

### PART A: THE FROM STATE

**A1. Archetype.**
- Control and relay panels (60.26% of revenue in H1 FY26, 48.94% in FY25) (B04.revenue_streams): Build-to-spec component maker. Panels are customised 11 to 220 kV units built to a customer drawing, gated by utility vendor approval (B04).
- Protection relays (39.74% in H1 FY26, 51.06% in FY25) (B04.revenue_streams): Build-to-spec component maker, catalogue variant. Hardware and firmware are designed in house; no patent evidence found (B04.moats_present).

The company reports one segment (B00.sector_cap_row_evidence), so the split is by product, not by reporting segment.

**A2. The simple analogy.** Avana builds the cabinets and the safety switches that sit in an electricity substation. The cabinet is the control room of the substation. The relay is the reflex that cuts the power in a fraction of a second when a fault appears. Avana makes both in two rented workshops in Bengaluru, for contractors who build substations. A state utility must first approve Avana as a vendor. Then the contractor places the order. The company grows fast (revenue +36.4% in FY26) (B03.strengths_top3), but the workshops are full, and the plan is to move into one owned plant on leased KIADB land that is not yet built (B03.flags).

### PART B: THE TRANSITION

**B1. FROM to TO.**
- Panels line: FROM R3 (value-added, spec'd supplier; partial pricing power from vendor approvals) TO R4 (franchise or share-of-wallet leader), drafted as a one-rung claim, inside the base rate of one rung per 2 to 3 years. The TO claim is not made by management in any filing. It is the model's reading of what capacity, 400 kV approvals and SCADA content would build. The Emerging Moat scan scored the forward moat NONE at 6.7 and found no transition-moat uplift (B07.em_classification, B07.combined_reasoning).
- Relays line: no tier migration declared. It holds at R3. The relay moat is not evidenced (no patents found, no listed relay pure play to test against) (B04.moats_present; B00.input_gaps).

**B2. The engine.** Two things physically change.
1. Capacity. One integrated unit on KIADB land replaces two rented units. Stated capacity moves from 70,000 relays and 600 panels to 1,75,000 relays and 1,500 panels, +150% (B03.guidance_table). B07 puts the physical ceiling at about +114% on FY26 output and H1 FY26 mix (B07.flags). Panel output of 886 in FY26 already exceeds the stated 600, so the stated base is unreliable (B03.missing_risks).
2. Reach. Vendor approvals extend the panel line to 400 kV (MPPTCL) and SCADA to 220 kV (CSPTCL) (B04; B07.active_categories B2). These are registrations with no order value (B07.catalysts_12m).
The engine is not yet built. CWIP is 466.79 lakh, commitments are 1,094.99 lakh and IPO capex used is 275.83 of 1,155.38 lakh (B02.top_findings rank 1).

**B3. The proof gate.** The gate fires only when both observations hold.
1. The KIADB unit is in commercial production, evidenced by a Reg 30 filing of commercial production or a KIADB extension letter naming the date, by 26-Oct-2026 (RHP) or end-October 2026 (board outcome 19-Aug-2026) (B03.monitorables; B05.triggers priority 1).
2. The H1 FY27 results show gross margin at or above 40.6% (FY26 level) and EBITDA margin excluding other income at or above 18.1% (H2 FY26 level), with cumulative IPO capex used above 275.83 lakh and rising toward 1,155.38 lakh (B03.monitorables).
Until both fire, the transition is narrative and the name is research. FTTCP (/fttcp) tests this gate. Status today: observation 1 has no filing (B05.flags); observation 2 is not due.

**B4. The recognition gap (open question for Stage 11).** Does the TO state (R4) already appear reflected in market pricing? The dossier does not conclude. Stage 11 confirms or denies it through the PE gap. If the TO state is already reflected, the re-rating engine is gone and only earnings growth remains. No number, no conclusion and no verdict are stated here.

**B5. The ugliness test.** The ugly optics today are: FY26 free cash flow near nil against capex (B01.block_b_trend), CFO at 0.68 of PAT in both FY25 and FY26 (B01.data_notes), a gross margin fall from 47.80% to 40.61% and an H2 EBITDA margin of 18.08% against 21.33% in H1 (B03.flags FLAG-MARGIN), and an unbuilt plant.
Draft classification: **ARTIFACT-OF-CLIMB for the cash optic**, held as the most evidenced path and not as a finding. Evidence for it: inventory rose 772.30 lakh and capex took 750.23 lakh in the year, debt fell from 568.51 to 76.14 lakh and the stock build was funded by operations and payables, not IPO money (B01.data_notes; B02 analyst_note; B12b pipeline_flags_not_supported). Receivable days fell from 125.8 to 96.7 (B02.receivables_trend).
Evidence for the second reading, STRUCTURAL-FEATURE: CFO/PAT has held near 0.68 for two years and 0.577 over seven; receivables older than two years nearly doubled with nil provision; bank stock-statement receivables exceed the books in all four FY26 quarters; and no peer explains the 7.2 point gross margin fall (B01; B02 top_findings ranks 5 and 6; B06.flags FLAG-MARGIN-GAP).
The observation that separates the two readings: whether finished goods of 690.47 lakh and stock in transit of 263.44 lakh are dispatched against orders and collected in H1 FY27 (B02; B03). For the margin optic the separator is H1 FY27 product-wise revenue and gross margin (B04.analyst_note). The operator decides the classification at sign-off.

**B6. The transition falsifier.** Any one of these kills the arrow:
- No Reg 30 commercial-production filing and no KIADB extension letter by 26-Oct-2026, or lease cancellation (B03.monitorables; B05.triggers).
- H1 FY27 gross margin below 36.6%, or EBITDA margin excluding other income below 18.1% (B04.must_track_metrics).
- IPO capex used still flat near 275.83 lakh at the H1 FY27 certificate (B05.triggers priority 3).
- No valued purchase order under the MPPTCL or CSPTCL approvals after two reporting periods (B05.triggers priority 4).

### PART C: WHAT THE MODEL WATCHES

**C1. Dominant variables (the Role 5.5 tracker candidates).**
1. KIADB unit commissioning and capex delivery. State: unbuilt; CWIP 466.79 lakh; capex used 275.83 of 1,155.38 lakh; guided end-October 2026 after a mid-May 2026 guide; RHP deadline 26-Oct-2026 (B02; B03; B05).
2. Margin bridge. State: gross margin 40.61% (H2 36.61%); EBITDA excluding other income 19.47% for FY26 and 18.08% in H2; warranty additions 0.50% of revenue against 3.72%; product-wise margin not found in blocks (B03; B04).
3. Cash conversion and working capital. State: CFO 795.44 lakh = 48.7% of EBITDA; inventory days 164.4; receivables over six months 13.8% of the total; FCF 45.21 lakh (B02; B03).
4. Demand conversion and concentration. State: order book 5,223.65 lakh at 30-Nov-2025; top 5 customers 38.79% in H1 FY26 against 22.42% in FY25; vendor registrations with no order value; FY26 customer data not found (B04; B05; B09).

**C2. What the model rejects.**
- Market size. The addressable-market question is noise: the serviceable market is a Rs 2,422 Cr proxy, Avana holds about 3.46% and the headroom is 28.9x (B09). The binding constraint is plant delivery and working capital, not market size.
- Spot ROCE, spot ROE, current ratio, P/B and debt-to-equity as printed. The IPO cash pile of 2,103.98 lakh unspent distorts them (B04.irrelevant_ratios).
- EV/Sales and SOTP style questions, because there is a single segment and no product margin in the blocks (B04.valuation_methods not_applicable).
- Stated capacity utilisation. Panels ran at 886 against 600 stated (B04).
- Peer pattern readings from the adjacent transformer segment as a verdict on Avana. Verifier B marked the B06 working-capital pattern comparison as not supported (B12b).

**C3. The business falsifier.** Evidence that forces re-declaring the FROM business itself, distinct from B6: disclosures showing that the panel line is contract assembly rather than build-to-spec design (for example, panel capacity found to be outsourced or shift-based assembly to customer drawing, given output of 886 against 600 stated) (B03.missing_risks; B04.flags FLAG-CAPACITY-BASIS); or revenue found to be a rotating set of single-project EPC orders with no repeat base (top 5 share rising above 38.79% with a falling order book) (B04.must_track_metrics red_flag); or relay design found not to be in house. Any of these moves the archetype off Build-to-spec component maker.

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE (draft from B01 to B09; stage 13 holds the final copy)

Spec: prompts/13-synthesis-pipeline.md, BUSINESS UNDERSTANDING NARRATIVE section (five questions, prose).

Avana makes two products for electricity substations. The first is the control and relay panel. It is a steel cabinet built to a customer's drawing. Operators use it to watch, switch and protect a substation. Panels were 60.26% of revenue in H1 FY26 and 48.94% in FY25 (B04.revenue_streams). The second is the protection relay. It senses a fault and trips the breaker before the fault damages a transformer or a line. Relays were 39.74% of H1 FY26 revenue (B04). Both matter because a substation cannot run without protection, and the protection functions have no close substitute inside a substation (B04.moats_present).

The customers are mostly EPC contractors and private panel builders, 76% to 82% of revenue, with state utilities as end customers (B04.flags FLAG-CONCENTRATION; B04.analyst_note). The utility approves the vendor and the contractor places the order, so credit risk sits with the contractors and end demand risk sits with state utilities (B04.analyst_note). MPPTCL registered Avana for 400 kV panels and CSPTCL for SCADA up to 220 kV in February 2026 (B07.catalysts_12m). Top 5 customers were 38.79% of H1 FY26 revenue against 22.42% in FY25. Customer data for FY26 is not found (B04.flags).

Demand exists because the grid keeps adding substations. India added 113,013 MVA of transformation capacity in FY26. The CEA plan figure for FY27 is 158,339 MVA, 40% higher. Solar added 44.6 GW and wind 6.1 GW in FY26, and each evacuation substation needs panels and relays (B09.flags FLAG-CYCLE; B09.downstream_candidates).

Demand grows for two reasons in the blocks. The first is the grid build itself. The vendor market reports show niche growth of 5.9% to 8.4% a year, below the unit growth in the grid, so the market growth rate is probably understated (B09.flags). The second is share gain. The model sizes revenue at Rs 165 Cr in three years and Rs 227 Cr in five from a base of Rs 83.86 Cr, which needs the share to rise from 3.46% to 5.46% and 6.46% of a Rs 2,422 Cr serviceable proxy (B09.som_3yr_cr, B09.som_5yr_cr, B09.current_sam_share_pct). The five-year figure exceeds the stated post-expansion capacity worth Rs 170 to 177 Cr at fixed unit prices, and the stated capacity itself is unreliable (B09.capacity_check). Peers grew 14% to 22% in FY26 against Avana's 36.4% (B06.partially_verified).

The competitive advantage differs by line. The panel line has a medium-durability moat from utility vendor approvals, but approvals are granted state by state and project orders are rebid (B04.moats_present). The relay line has proprietary hardware and firmware design, rated low to medium, with no patent found and no listed relay pure play to test it against (B04.moats_present; B00.input_gaps). The Emerging Moat scan found 2 of 22 categories at moderate strength, for a score of 6.7 and class NONE (B07). A large switchgear maker could add a 400 kV panel line, because nothing in the corpus blocks it (B07).

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. Verticals framed (one per dominant variable)

**Vertical 1: KIADB unit commissioning and capex delivery.**
- The corpus establishes: CWIP 466.79 lakh; commitments 1,094.99 lakh; IPO capex used 275.83 of 1,155.38 lakh (32.4% of the FY26 plan of 850.00 lakh); commercial production guided mid-May 2026, now end-October 2026; RHP deadline 26-Oct-2026 with no further extension; automatic lease cancellation on failure (B02 rank 1; B03.flags FLAG-CAPEX; B05.guidance). Both operating-unit leases were due to expire in July and August 2026 per the RHP, renewal not found (B03.missing_risks).
- It cannot establish: the KIADB letters and the true extended date (the RHP is internally inconsistent), lease renewal status, reconciliation of CWIP plus commitments (1,561.78 lakh) to project cost of 1,305.38 lakh, or why the schedule slipped (B03; B05; B07.input_gaps).
- Deciding questions: (a) Is there a Reg 30 commercial-production filing or a KIADB letter naming a date after 26-Oct-2026? (b) How is the 215.44 lakh of commitment above unspent IPO capex funded (B02.questions_for_mgmt)? (c) Are both rented units still held after July and August 2026?

**Vertical 2: Margin bridge.**
- The corpus establishes: gross margin 47.80% to 40.61% (H2 36.61%); EBITDA excluding other income 19.47%, H1 21.33%, H2 18.08%; other expenses held the margin by falling from 13.0% to 8.5% of revenue; warranty additions 41.81 lakh (0.50% of revenue) against 228.47 lakh (3.72%); panel share 48.94% to 60.26% (B03.flags; B02 rank 2; B04.flags). The only call peer reports a 1 to 2 point margin give-up (B06.flags FLAG-MARGIN-GAP).
- It cannot establish: FY26 product-wise revenue and margin, the reason for the lower warranty accrual rate, or whether Purchases of 5,752.65 lakh is gross or net of the 151.65 lakh warranty usage (B02.input_gaps; B03 analyst_note).
- Deciding questions: (a) Do H1 FY27 results disclose product-wise revenue and gross margin, and does gross margin hold at or above 40.6%? (b) Do warranty additions return above 2.1% of revenue or stay below 0.75% for a second period (B03.monitorables)? (c) Does the other-expense share stay near 8.5% after relocation?

**Vertical 3: Cash conversion and working capital.**
- The corpus establishes: CFO 795.44 lakh = 67.9% of PAT and 48.7% of EBITDA excluding other income; FCF 45.21 lakh against 549.75 lakh in FY25; inventory +772.30 lakh (+52.5%); finished goods 690.47 lakh (+108.8%); stock in transit 263.44 lakh; receivable days 96.7 against 125.8; receivables older than six months 307.13 lakh (13.8% against 11.4%), older than two years 86.24 lakh against 46.26 lakh, nil doubtful-debt provision; bank stock-statement receivables above books each quarter by 2.15% to 7.77% (B02 ranks 4 to 7; B03.flags). IPO working-capital object used 123.03 of 860.00 lakh (B01.data_notes).
- It cannot establish: a lender view on working capital (no rating document), the composition of finished goods and stock in transit, or FY26 receivable ageing by customer name (B00; B02).
- Deciding questions: (a) CFO/EBITDA above 70% with inventory days at or below 150 in H1 FY27? (b) Are finished goods and stock in transit falling? (c) Does the over-six-month receivable share stay at or below 13.8%, and does any provision appear?

**Vertical 4: Demand conversion and concentration.**
- The corpus establishes: order book 5,223.65 lakh at 30-Nov-2025, about 62% of FY26 revenue (B04.must_track_metrics); top 5 38.79% in H1 FY26 against 22.42% in FY25; MP was 33.59% of FY25 revenue; MPPTCL and CSPTCL registrations carry no order value (B04.flags; B07.catalysts_12m). Public grid data shows transformation additions of 113,013 MVA in FY26 and a 158,339 MVA FY27 plan figure (B09).
- It cannot establish: FY26 top 5 customers and identities, the order book after 30-Nov-2025, payment terms and retention, or the registration-to-order lag (B04.input_gaps; B06.unverifiable).
- Deciding questions: (a) Are the FY26 top 5 customers and share disclosed, at or below 38.79%? (b) Is the order book at or above 5,223.65 lakh? (c) Does a valued purchase order appear under a vendor registration within two reporting periods?

### 4b. Candidate signal table (UNVERIFIED; verification and tracker writes happen at Role 5.5 in claude.ai)

Candidates come from B09.downstream_candidates, plus the KIADB entity from B03.ar_new_downstream_entities. The likely source follows B09 and is to be checked against Downstream_Source_Discovery_Protocol_v1_0 at Role 5.5.

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| POWERGRID capex, works in hand and TBCB awards (B09) | Capex or award flow falls while Avana revenue still shows growth, or awards slip two quarters | Quarterly | NSE announcements and concall transcripts of POWERGRID; CEA/PIB |
| CEA monthly transformation capacity added against plan (B09) | Cumulative additions run well below the 158,339 MVA FY27 plan figure for three months | Monthly | CEA monthly transmission progress report; PIB |
| MP, Chhattisgarh and Karnataka transmission utility tenders (MPPTCL, CSPTCL, KPTCL) (B09) | No tender award that names an approved panel or SCADA scope within two reporting periods | Event-Driven | State utility tender portals; Reg 30 filings by Avana |
| Renewable capacity additions and BESS commissioning (B09) | Monthly additions fall below the FY26 run rate (solar 44.6 GW, wind 6.1 GW) | Monthly | MNRE / CEA installed capacity reports; PIB |
| EPC contractor order wins; Avana top 5 customers, identities NOT FOUND (B09) | Listed EPC order wins fall while Avana top 5 share rises above 38.79% | Quarterly | Listed EPC concall transcripts and NSE order-win filings |
| CERC/CEA transmission planning orders and RDSS sanctions (B09) | Planning orders or RDSS sanctions stall for two quarters | Event-Driven | CERC orders; CEA NCT minutes; Ministry of Power/PIB |
| KIADB commercial-production status (B03.ar_new_downstream_entities; B05) | No Reg 30 filing and no extension letter after 26-Oct-2026 | Event-Driven | NSE announcements; KIADB letters via the operator |

candidate_count carried: 6 (the six B09 candidates; the KIADB row is an addition from B03).

### 4c. Fragility read

- variable_count: 7. The external variables that must go right: (1) KIADB date held or extended; (2) lease continuity for the rented units; (3) gross margin holds through the mix shift and input cost swings; (4) warranty accrual rate settles at a level the failure record supports; (5) cash conversion improves as stock converts; (6) grid and utility demand converts into orders (CEA, tenders, EPC awards); (7) customer concentration and EPC credit stay manageable (B02; B03; B04; B05; B09).
- verifiability_ratio: 4 of 7 externally observable (KIADB filing, margin on filed results, cash flow on filed results, grid and tender data). Company-narrated only: lease renewal, warranty rationale, customer concentration and order book disclosure (B03.missing_risks; B04.input_gaps).
- single_point_failure: Yes. The KIADB lease and unit date of 26-Oct-2026, which is 21 days from the run date. Failure with no extension letter cancels the lease automatically per the RHP and strands CWIP of 466.79 lakh (B05.red_flags; B02 rank 1).
- fragility_verdict: FRAGILE (seven variables, three of them company-narrated, and one dated single point of failure).

### 4d. Research brief (claude.ai live-web work order)

1. PENDING LIVE VERIFICATION (Chain 1, Link 2). KIADB extension letter(s): the letter dated 27-Oct-2025 and the May 2025 extension, and any extension after the board outcome of 19-Aug-2026. The operator requests the letters from the company; claude.ai checks NSE for a Reg 30 filing and any KIADB or Karnataka government notice.
2. PENDING LIVE VERIFICATION (Chain 2, Link 2). Customer-side evidence for the panel line: identities of the FY26 top 5 customers (investor query), and the filings of listed EPC contractors and the MPPTCL, CSPTCL and KPTCL tender award pages for panel and SCADA scope.
3. Chain 3 to build: cash conversion. Counterparty reads: lender stock-statement variance, rating status (item 6), and the dispatch of finished goods 690.47 lakh and stock in transit 263.44 lakh.
4. Chain 4 to build: demand conversion. POWERGRID TBCB awards, CEA monthly additions, MPPTCL and CSPTCL tenders.
5. Chain 5 to build: promoter and related-party cost. Promoter pay 289.48 lakh, family fees 78.00 lakh, FY27 pay 341.64 lakh approved with 97.6% of votes cast (B02 rank 10; B08.adverse_findings; B12b).
6. Credit rating status. Search CRISIL, ICRA, CARE, India Ratings, Acuite and Infomerics for Avana Electrosystems; record "unrated" if none (B00).
7. NSE filings after 29-Sep-2026 and any filing since 19-Aug-2026 on lease renewal, commercial production or the KIADB date. Shareholding patterns for 30-Jun-2026 (absent from corpus) and 30-Sep-2026 (due by 21-Oct-2026).
8. H1 FY27 results date and the auditor utilisation certificate (IPO capex used above 275.83 lakh; working capital used above 123.03 lakh).
9. MCA21 director history for the promoter JVS Electronics and Venson overlap (B08.adverse_findings, UNVERIFIED) and for the promoter-group shipping company named in the RHP (business NOT FOUND) (B08).
10. Peer disclosure on warranty or installation accrual rates, receivable provisioning and registration-to-order lag, from DANISH, MARINE and SPCL filings (B06.unverifiable).
11. Source URL verification for the B09 market sizes (Ken Research page fetch blocked; MnM, Straits, IMARC snippets) and the FX rate of 88.79 (B09.searches_skipped; B09.stale_data_flags).
12. Final prospectus of 14-Jan-2026 from NSE, to compare with the RHP on KIADB dates and objects (B00).
13. Carry to stage 10 and the verifiers (not live web): Section 6 question 1 quotes product margins printed in the RHP MD&A (relays about 60%, panels 34% to 36%). B04 and B07 record product-wise margin as NOT FOUND. Stage 10 and Verifier A should reconcile this before Role 1 reads the mix question.

### 4e. Second-order stub (Master Prompt v3.7, Rule F)

**CHAIN 1: The board guides commercial production for the KIADB unit by end-October 2026 while the RHP deadline is 26-Oct-2026 with "no further extension" (B05.guidance; B03.guidance_table).**
Link 1 [filed, RHP p36-37 and board outcome 19-Aug-2026 p2, via B05]: The board says the unit is "nearing completion" and expects commercial production "by the end of October 2026 ... well before the extended timelines". The RHP says that failure to start by 26-Oct-2026 may lose the lease, and no further extension may be granted. The unit was guided for mid-May 2026 in the RHP and has slipped about 5.5 months (B05.timeline_slippages).
Link 2 [PENDING LIVE VERIFICATION]: who decides, and why now. KIADB is the lessor and the only party that can extend. The corpus holds no KIADB document. Claude web should open the KIADB extension letter dated 27-Oct-2025 (named in the RHP) and any later letter, plus Avana's NSE announcements after 19-Aug-2026. Nothing about KIADB's intent is stated here.
Link 3 [INFERENCE]: If no commercial production is filed and no letter exists by 26-Oct-2026, the lease cancels and the 150% capacity step is lost. The business would then rely on two rented units whose leases were due to expire in July and August 2026 (B03.missing_risks). If a later extension exists (the RHP p179 reading of three years from May 2025), the date risk shifts to execution pace.
Binding constraint: Capex and cash. Unspent IPO capex is 879.55 lakh against commitments of 1,094.99 lakh, so 215.44 lakh needs internal cash, and non-IPO cash of 40.37 lakh sits below margin money of 719.17 lakh (B02 rank 1, rank 7; B02.questions_for_mgmt). CFO of 795.44 lakh and FCF of 45.21 lakh are the internal funding (B02 rank 7).
Unsaid: The MD&A and the board risk text are silent on KIADB, and the notes carry only a "construction of factory" commitment line (B03.missing_risks; B02 rank 1). The RHP gives two different dates for the extension (B03.analyst_note). No stated cause exists for the slip (B05.red_flags).
Observation that confirms or breaks this chain, and confirm-by date: A Reg 30 filing of commercial production or a KIADB letter naming a date after 26-Oct-2026, confirm-by 26-Oct-2026 (RHP) and no later than 31-Oct-2026 (board guide); and cumulative IPO capex used above 275.83 lakh in the H1 FY27 auditor certificate (filing date NOT FOUND). Absence of both breaks it.

**CHAIN 2: Gross margin fell from 47.80% in FY25 to 40.61% in FY26 and to 36.61% in H2, while panel share rose from 48.94% to 60.26% (B03.flags FLAG-MARGIN; B04.flags FLAG-MIX).**
Link 1 [filed, AR p85, p100 and p124; RHP p120, p152, via B03 and B04]: Panels produced rose from 523 to 886 and relays fell from 65,840 to 62,034. EBITDA excluding other income held at 19.47% for FY26 only because other expenses fell from 13.0% to 8.5% of revenue (B03.flags; B04.analyst_note). Warranty additions fell to 41.81 lakh (0.50% of revenue) from 228.47 lakh (3.72%) (B02 rank 2).
Link 2 [PENDING LIVE VERIFICATION]: who pays, and why now. The paying parties are EPC contractors and private panel builders (76% to 82% of revenue), and their identities are NOT FOUND (B04). Claude web should open the NSE filings of the listed EPC contractors operating in MP, Maharashtra and Karnataka once the top 5 are named, and check whether their orders to Avana carry price-variation clauses. DANISH reports about 30% of its order book on price variation and a firm-price book under pressure (B06.industry_cross_read). Avana's price-clause mix is NOT FOUND (B06.flags FLAG-H1FY27-INPUTS).
Link 3 [INFERENCE]: If panels carry a lower gross margin than relays, the shift in mix explains most of the fall. If they do not, input cost or pricing explains it (B04.analyst_note). Both readings leave the exit rate at risk, because H2 margin was already 18.08% and a warranty rate of 0.13% in H2 supported it (B03.flags; B02 rank 3).
Binding constraint: Capacity and working capital. Panel output of 886 already exceeds the stated 600, and growth in panel output needs stock and receivables: inventory 2,243.25 lakh and days of 164.4 (B03.missing_risks; B02 rank 4).
Unsaid: A footnote in Note 25 item 11 says the 151.65 lakh of warranty usage is "included in Purchases", and the credit side is not stated, so whether Purchases of 5,752.65 lakh is gross or net is unknown (B03.analyst_note). That footnote implies a cost line that no management text explains. The MD&A says the margin saw no significant change (B03.phase_verdicts p4).
Observation that confirms or breaks this chain, and confirm-by date: H1 FY27 results with a product-wise revenue and gross margin split, and gross margin at or above 40.6% with EBITDA excluding other income at or above 18.1% (confirms); gross margin below 36.6% or no split disclosed (breaks) (B04.must_track_metrics). Confirm-by: the H1 FY27 results filing (half-year ended 30-Sep-2026; filing date NOT FOUND).

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in claude.ai with live web, before Role 2.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. Avana Electrosystems makes control and relay panels and protection relays for electricity substations (B04).
2. It was set up in 2010, listed on NSE Emerge in January 2026, and four engineer promoters still run it (B08.analyst_note; B00.listed_date).
3. FY26 revenue was Rs 83.86 Cr, up 36.4%, and PAT was Rs 11.72 Cr (B03.strengths_top3; B01.data_notes).
4. Customers are mainly EPC contractors and private panel builders, 76% to 82% of revenue (B04.flags). State utilities approve the vendor but do not place most orders (B04.analyst_note).
5. Top 5 customers made up 38.79% of H1 FY26 revenue against 22.42% in FY25. FY26 customer data is not in the corpus (B04.flags).
6. Demand comes from new substations for the grid and for renewable power evacuation. India added 113,013 MVA of transformation capacity in FY26 (B09.flags FLAG-CYCLE).
7. Demand growth in the grid is faster than vendor reports assume. The model also needs Avana to win share, from 3.46% to 5.46% of a proxy market in three years (B09).
8. The panel moat is medium. It comes from utility vendor approvals, which are state by state. The relay moat is not evidenced. The scan scored 6.7, class NONE (B04; B07).
9. The mental model in one point: a fast-growing build-to-spec maker whose next step depends on one plant that is not yet built. The arrow is capacity, then margin, then cash (Section 2, draft).
10. The plant on KIADB land has a deadline of 26-Oct-2026 in the prospectus, 21 days from the run date. Commercial production is now guided for end-October 2026 (B05; B03).
11. Margin quality is the second open point. Gross margin fell 7.2 points. The FY26 profit is also helped by a warranty accrual of 0.50% of revenue against 3.72% a year earlier (B03.flags; B02 rank 2).
12. The fragility read is FRAGILE. Seven external variables must go right, three are company-narrated, and one dated deadline can break the capacity thesis alone (Section 4c).
13. The corpus could not establish FY26 product-wise revenue, FY26 customer names, the order book after November 2025, the KIADB extension letters or any lender view. There are no calls, no investor deck, no rating and no research note (B00; B04).
14. Governance is rated CAUTION, not CONCERN. No pledge, no litigation and no regulator action were found. Promoter pay and family fees together are 31.3% of PAT, and independent directors attended 9 of 19 board meetings (B08; B12b).
15. The biggest open questions: Does the KIADB unit start or get an extension by 26-Oct-2026? Does H1 FY27 hold gross margin at or above 40.6% and turn profit into cash? Does the order book hold at or above 5,223.65 lakh with the top 5 share at or below 38.79%? (B03.monitorables; B05).

---

## SECTION 6: STANDING EXTRACTION ANNEX

Quote-then-comment. Every quote is printed text; the file and page anchor follow. The page is the page-marker number in the .txt beside each PDF, with the printed page number in brackets where it differs. Where a stage report already carried the figure, it is reused. The annex holds no valuation, price judgement or verdict language.

### Q1. UNITS

No per-unit price, realisation or ARPU is printed anywhere in the corpus. The volume and revenue lines needed to derive one are printed:

- Volume, panels: "Control and Relay Panel ... 2023-24 ... 502 | 2024-25 ... 523 | 2025-26 ... 886" under "Produced Qty" (AVANA-AR-FY2025-26-with-AGM-notice.txt, page 85, printed p74).
- Volume, relays: "Relay ... 2023-24 ... 58,501 | 2024-25 ... 65,840 | 2025-26 ... 62,034" under "Produced Qty" (same, page 85).
- Revenue by product: "3 2024-25 3,008.96 48.94% 3,139.62 51.06% 6,148.58" and "September 30, 2025 2,154.28 60.26% 1,420.43 39.74% 3,574.71", in Rs lakh, panels then relays then total (AVANA-RHP-2025-12-31.txt, RHP p152 per B04).
- Comment: The unit is the produced quantity, not the sold quantity. The RHP shows relays sold at 73,621 against 58,501 produced for FY24 (B04.input_gaps). Panel is a basket of custom 11 to 220 kV units. Relay is a basket of numerical and electromechanical units. B04 derives FY25 panel revenue at 5.75 lakh per unit (3,008.96 / 523) and relay revenue at Rs 4,769 per unit (3,139.62 / 65,840) on produced units, and H1 FY26 at 6.88 lakh and Rs 4,221 (B04.unit_economics). No FY26 revenue split by product is printed (B04).
- Retrieved item, not in any block: the RHP MD&A prints a product margin table. Quote: "Particulars FY 2023 FY 2024 FY 2025 September 30, 2025 | Relays Margin 58.05% 50.61% 60.54% 60.00% | Control & Relay Panels Margin 31.77% 26.00% 34.51% 36.00%" (AVANA-RHP-2025-12-31.txt, page 268, printed p263). The table has no label for the margin basis. B04 and B07 recorded product-wise margin as NOT FOUND for FY26 and did not carry this table. The table ends at 30-Sep-2025. It must reach stage 10 and Verifier A before the mix question is read (Section 4d item 13).

### Q2. SEGMENT CAPITAL AND DEBT

- Quote: "the Company is primarily engaged in the business of designing, manufacturing, and supplying electrical control, protection, and automation panels, as well as relays, for power system applications. These activities are considered to constitute a single business segment ... the entire operations of the Company relate to one reportable segment only." (AVANA-FY26-results-legible-refiling-2026-06-23.txt, page 1, item 2).
- Segment assets, segment liabilities and capital employed by segment: NOT DISCLOSED, because the company reports one segment.
- Borrowings are not allocated by segment. Total as printed: "(a) Long-term borrowings | 4 | 55.60 | 126.16" and "(a) Short-term borrowing | 6 | 20.54 | 442.35"; "Total | | 8,476.53 | 4,838.68" (AR page 99, Rs lakh, 31-Mar-2026 then 31-Mar-2025).
- Comment: Total debt is 76.14 lakh at 31-Mar-2026 against 568.51 lakh a year earlier (B03; B01). Total assets are the only capital figure available.

### Q3. GUIDANCE VERSUS ASPIRATION

| # | Quote | Class | Anchor |
|---|---|---|---|
| 1 | "The Company expects to commence its commercial production by the end of October 2026, following completion of the requisite work and operational requirements well before the extended timelines." | (a) guidance with period | AVANA-Board-outcome-2026-08-19.txt, item 7 (p2) |
| 2 | "5. Commencement of Commercial Operations May 2026 (mid)" | (a) guidance with period; superseded by row 1 | RHP page 106 (txt line 8166) |
| 3 | "70,000 1,75,000 600 1,500 1,76,500" and "...will increase to 1,75,000 units of protection relays and 1,500 units of control and relay panels" | (c) capacity only, no date | RHP page 104 (txt lines 8056, 8076-8077) |
| 4 | "cycle 205 205 245 196 169 203" (working-capital cycle projection row; FY26 column per B05) | (a) guidance with period (31-Mar-2026) | RHP page 113 per B05 (txt line 8689) |
| 5 | Capex "up to 850.00 lakh" in FY26 and 305.38 lakh in FY27; working capital 860.00 lakh in FY26 | (a) guidance with period | RHP p102-103 per B05 |
| 6 | FY27 managerial remuneration 341.64 lakh (+18.0%) put to AGM special resolutions | cost commitment, not a business forecast | AR p37-38 per B03 |
| 7 | "The Company has not distributed any dividend in the current and previous years." | none; no policy number | AR page 108, Note 2(vi) |

- Comment: No revenue, margin, debt or return guidance exists in any filing (B05.input_gaps). Rows 4 and 5 are taken from B05 as anchored by that stage; their exact printed wording was not re-read here except the cycle row. No management aspiration without a period was found.

### Q4. CONCENTRATION

- Product: "September 30, 2025 2,154.28 60.26% 1,420.43 39.74%" panels then relays (RHP p152 per B04). FY25: 48.94% and 51.06%. FY26: NOT DISCLOSED.
- Customer: "Top 5 customers 1,386.47 38.79 | 1,378.76 22.42 | 1,205.78 22.76 | 1,022.97 36.01" and "Top 10 Customers 1,858.71 52.00 | 1,936.50 31.5 | 1,964.38 37.07 | 1,360.96 47.91", columns H1 FY26 then FY25, FY24, FY23, Rs lakh (AVANA-RHP-2025-12-31.txt, page 169, with the same figures at page 38). Top single customer share: NOT DISCLOSED. FY26 top 5 and identities: NOT DISCLOSED (B02; B04).
- Geography: "A major portion of our revenue from operations is derived from three states (Madhya Pradesh, Maharashtra and Karnataka) and the combined revenue from the three states accounted for 48.33%, 66.42%, 61.58% and 44.02%" for H1 FY26, FY25, FY24 and FY23 (RHP txt lines 2569-2570, page 36). State table: "Madhya Pradesh 460.38 12.88 | 2,065.51 33.59 ..." and "Maharashtra 917.30 25.66 | 1,366.14 22.22", "Uttar Pradesh 882.56 24.69" in H1 FY26 (RHP page 168). Top single state: Maharashtra 25.66% in H1 FY26; Madhya Pradesh 33.59% in FY25. FY26: NOT DISCLOSED.
- Comment: Customer concentration rose and state concentration eased between FY25 and H1 FY26, but the second period is a half-year stub. The private EPC and panel-builder band of 76% to 82% comes from B04.

### Q5. PROMISE LEDGER

| Promise | Date made | Status | Evidence anchor |
|---|---|---|---|
| Commercial production mid-May 2026 | RHP 31-Dec-2025 | MISSED (end-Oct 2026 guided; unit not reported live at 2026-10-05) | RHP p105-106; board outcome 19-Aug-2026 p2 (B05) |
| IPO capex up to 850.00 lakh in FY26 | RHP 31-Dec-2025 | MISSED (275.83 used) | RHP p102-103; AR p107 (B05) |
| IPO working capital 860.00 lakh in FY26 | RHP 31-Dec-2025 | MISSED (123.03 used) | RHP p103; results re-filing p4 (B05) |
| FY26 working-capital cycle 205 days | RHP 31-Dec-2025 | DELIVERED on the RHP basis (176.8 days derived; mix differs); Verifier B calls this generous (B12b) | RHP p113; AR p99, p113, p115 (B05; B12a) |
| FY26 inventory 1,646.94 lakh | RHP 31-Dec-2025 | MISSED (2,243.25 actual) | RHP p43; results re-filing p4 (B05) |
| FY26 receivables 2,720.65 lakh | RHP 31-Dec-2025 | DELIVERED (2,221.29 actual) | RHP p43; results re-filing p4 (B05) |
| Exports restart with one Kuwait order | RHP 31-Dec-2025 | PARTIAL (46.28 lakh, 0.55% of revenue) | AR p115; RHP p171 (B05) |
| Regional offices and dealer network expansion | RHP 31-Dec-2025 | DROPPED (no follow-up in AR) | RHP p170-171; B05.dropped_triggers |

- Comment: 2 delivered, 1 partial, 4 missed; credibility grade C, the no-concall floor (B05). Verifier B holds that the grade should sit one notch lower and notes that the RHP blames COVID for a KIADB delay whose first deadline passed about 15 months before COVID (B12b). The evidence period is under four quarters. On the KIADB date, the RHP also prints: "vide letter dated October 27, 2025, KIADB has granted one year extension of time for the implementation of the project. As per the terms of the extension ... (i.e. October 26, 2026), no further extension may be granted." (RHP page 37). Another page reads: "provided an extension on May 23, 2025 and is under an obligation to commence civil construction work within 9 months of May 23, 2025 and commercial production within 3 years of May 23, 2025." (RHP page 179). The two readings stay open.

### Q6. RESTATED BASES

- Quote: "3. Previous Year figures have been regrouped when necessary to confirm to the current year's classification." (AR page 102) and "25. Previous year's figures have been regrouped or reclassified wherever necessary to conform with the current year figures. The impact of such reclassification/regrouping is not material to the financial statement" (AR page 126, Note 25 item 25).
- No reorganisation, transfer or scheme restatement is stated in the corpus.
- Comparatives as printed in the latest filing: FY25 total assets "4,838.68" (AR page 99); FY25 net profit "847.08" (AR Board report financial summary, "Net Profit for the Year 1,172.28 847.08"); and the FY25 cash flow line "Prior Period Items- Gratuity and Leave encashment | - | (60.17)" (AR page 101).
- Comment: These differ from the RHP restated figures. B02.restatements_found lists: FY25 profit 831.23 (RHP) against 847.08 (AR); FY25 total assets 4,942.12 against 4,838.68 (103.44 revenue-authority balance netted); FY25 CFO 676.66 against 573.22; FY25 ageing (nothing over one year in the RHP against 165.49 in the AR); contingent items 35.04 dropped; warranty and installation lines net of usage in FY25 and gross in FY26 (B02). The AR gives no bridge. Gate 0 names the source on each FY25 ratio (B01.data_notes).

### Q7. CORPORATE-ACTION CLAUSES

No scheme, demerger or merger is in the corpus. Nothing to fetch for those. The corporate actions that are in the corpus:

- IPO. Quote: "59,70,000 Equity Shares of face value of ₹ 10 each at the price of ₹ 59 each (including ₹ 49 Security Premium) for total consideration of ₹ 3,522.30 Lakhs ... 7,94,000 shares were issued through Offer for Sale and the remaining 51,76,000 shares were issued as Fresh Issue." (AR page 107, Note 2(iii)(a)). Listing date 20-Jan-2026 (B00). The allotment date is not printed in the note: NOT DISCLOSED here.
- Bonus. Quote: "On 19th August 2025, the Board of Directors approved and allotted a bonus issue of equity shares in the ratio of 21:1 (i.e., 21 new shares for every 1 existing share)" and "1,66,75,344 equity shares ... by way of capitalization of free reserves of Rs. 1,658.94 lakhs and Capital Redemption Reserve (CRR) of Rs. 8.59 lakhs" (AR page 107, Note 2(ii)).
- Repurchase. The AR notes an earlier repurchase of 85,936 shares (9.77% of paid-up capital) at a net price of Rs 93.75 per share, record date 25-Sep-2020 (AR page 108, Note 2(x)).
- Authorised capital: raised from Rs 90,00,000 to Rs 25,00,00,000 at the EGM of 11-Nov-2024 (AR page 108, Note 2(v)).
- Comment: No preferential issue is in the corpus. Liability allocation clauses and undertaking definitions do not apply. The promoter-group revision of 23-Jan-2026 (Reg 30) and the final prospectus of 14-Jan-2026 are not in the corpus and are named for fetch on NSE (Section 1; B08.input_gaps).

### Q8. RELATED-PARTY PERIMETER

The AR RPT note lists directors, KMP and relatives only. Latest year (Rs lakh, FY26 then FY25) (AR pages 117 to 118, Note 25 item 1, printed pp106 to 107):

| Party and relationship | Nature | FY26 | FY25 |
|---|---|---|---|
| Anantharamaiah Panish, Managing Director | Director remuneration; IPO expense recovery | 88.54; 22.66 | 61.20; none (plus incentive 38.75) |
| K N Sreenath, Executive Director | Director remuneration; IPO expense recovery | 62.86; 22.66 | 38.16; none (plus incentive 38.75) |
| Gururaj Dambal, Whole Time Director | Director remuneration; IPO expense recovery | 74.62; 22.66 | 47.28; none (plus incentive 38.75) |
| S Vinod Kumar, Whole Time Director | Director remuneration; IPO expense recovery | 63.46; 21.15 | 38.76; none (plus incentive 38.75) |
| Three independent directors | Sitting fees (each) | 2.40 | none |
| Amrutha Naveen (CS to 31-Mar-2026), Ravi Kumar S (CFO) | Salary | 4.05; 8.18 | none |
| Smita Dambal, Nithya M, G Usha, Rama Subramanyam (wives of directors) | Professional or consultancy fees (each) | 18.00 | 18.00 |
| Ramabai Dambal (mother of a director) | Consultancy fees | 6.00 | 6.00 |

- Printed total: "TOTAL | | 476.03 | 418.40" (AR page 118). Balances outstanding printed total 17.96 and 14.72.
- Comment: B03 records the CFO and CS pay as swapped between the board report (CFO 4.05, CS 8.18) and this note (CS 4.05, CFO 8.18) (B03.triple_pass_verification; B12b R19). The scope of the 78.00 lakh family fees is NOT FOUND (B08). The RHP promoter-group list names one company, T. Shipping Private Limited (printed with a different first word; the first word is a banned vocabulary term for this stage, so it is not repeated) (RHP page 219, txt line 15765). Its business is NOT FOUND, and it does not appear in the AR RPT note. The RHP states there are no group companies (B08.adverse_findings).

### Q9. PLEDGE AND SHAREHOLDING

Twelve quarters as filed: NOT DISCLOSED in this corpus. The company listed on 20-Jan-2026, so at most a few quarterly patterns exist, and the corpus holds one: 31-Mar-2026. The 30-Jun-2026 pattern is absent (Section 1). The 30-Sep-2026 pattern is due by 21-Oct-2026 (B00).

- 31-Mar-2026, from AVANA-SHP-2026-03-31.xml: promoter and promoter group 16,675,408 shares, 0.7364 of 22,645,408 (73.64%); public 5,970,000 shares, 0.2636. "WhetherAnySharesHeldByPromotersAreEncumberedUnderPledged ... false" and the same flag for promoter and promoter group "false". Reg 31(4) declaration: "have not made any encumbrance of the said Equity Shares, directly or indirectly other than those already disclosed during the financial year ended on 31st March, 2026" (AVANA-Reg31-4-disclosure-2026-06-15.txt, page 1; the letter itself is dated 08-Apr-2026 per B08).
- Institutional holding at 31-Mar-2026 (XBRL): alternative investment funds 1,916,000 shares (0.0846); domestic institutions 1,934,000 (0.0854); foreign portfolio investors category one 248,000 (0.011). An AIF block of 6,75,000 shares is locked in (B08.transition_evidence).
- Earlier: promoters 99.99% before the IPO per B08 (RHP p209) and 100% held by eight shareholders at the RHP date (RHP p92 per B12a). Promoter shares are 100% locked in (B08).
- Comment: Pledge is nil on the one filed pattern and on the Reg 31(4) declaration. A trend cannot be read from one point.

### Q10. VERIFICATION

Documents quoted, with filename and document date:

1. AVANA-AR-FY2025-26-with-AGM-notice.pdf (.txt), AR for FY2025-26, financial statements signed 21-May-2026; AGM notice cover letter to NSE 03-Sep-2026. Pages 85, 99, 101, 102, 107, 108, 117, 118, 126 quoted. Pages 99 to 127 are image transcriptions.
2. AVANA-RHP-2025-12-31.pdf (.txt), Red Herring Prospectus dated 31-Dec-2025. Pages 36, 37, 104, 106, 113, 168, 169, 179, 219, 268 quoted.
3. AVANA-FY26-results-legible-refiling-2026-06-23.pdf (.txt), reply to NSE dated 23-Jun-2026.
4. AVANA-Board-outcome-2026-08-19.pdf (.txt), board outcome dated 19-Aug-2026.
5. AVANA-SHP-2026-03-31.xml, shareholding pattern at 31-Mar-2026.
6. AVANA-Reg31-4-disclosure-2026-06-15.pdf (.txt), Reg 31(4) declaration, filed 15-Jun-2026, letter dated 08-Apr-2026 (scanned; read through its text file).
7. Block files B02, B03, B04, B05, B08, B12a, B12b (run avana-2026-10-05, committed), for figures marked "per B0x".

CORPUS COMMIT HASH: 9a6a995495514f2a47c95954a4d39eab6eccbbc0
