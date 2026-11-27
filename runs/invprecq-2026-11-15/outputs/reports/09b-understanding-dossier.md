# Halt 1 Understanding Dossier: Investment & Precision Castings Ltd (INVPRECQ)

Run date 2026-11-15. Stage 09b. Assembly only from committed blocks B00 to B09 and verifier blocks B12a to B12d, with the Section 4e chain exception and the Section 6 annex exception. No valuation, no verdict. Units: filings in INR lakh, CARE and screener in INR crore (B00.reporting_units). AR page anchors are PDF pages; stage 2 anchors ran one page high and are corrected as Verifier A found (B12a, source_fidelity findings).

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

Inventory only. Source: B00-inputs, B00-intake, and the stage blocks that name documents.

1. CONCALLS. None held. Declared: `concalls_available: false`, the company holds no earnings calls (B00). Most recent quarter covered by a transcript: none. The newest results filing is Q2 FY27, dated 14-Nov-2026 (B00). Run date is 2026-11-15, so no later quarter has plausibly reported; the next one (Q3 FY27) is expected about Feb 2027 (B07, inferred from the 04-Feb-2026 Q3 FY26 board outcome). The missing transcript is absent by design, not by collection failure. Stage 5 ran in NO-CONCALL MODE (B05.no_concall_mode). Twelve peer transcripts are held (Azad x4, Steelcast x4, Alicon x4, Nov 2025 to Aug 2026); they are peers, not the company (B00.inventory, B06).
2. ANNUAL REPORTS. FY2025-26 (year ended 31-Mar-2026; annual-report/Annual_Report_FY2025-26.pdf) and FY2024-25 (inputs/other/Annual_Report_FY2024-25; kept there so the one-AR contract holds, B00.input_gaps). The latest completed FY is present. Two years are held, not three or more.
3. RESULTS FILINGS. Latest: Q2 FY27, 20261114-Q2FY27-results.pdf, dated 14-Nov-2026. Also held: Q1 FY27 (13-Aug-2026), Q4 FY26 (19-May-2026 original and 25-May-2026 resubmission, both dated 19.05.2026 on page 1; the reason for the re-filing is not stated, B00.input_gaps), Q3 FY26 (04-Feb-2026). All five are scanned images read through OCR; rotated table pages were re-read and column headers are lost (B00.text_extraction, run-log). Quarter gap between latest results and latest AR: the AR ends 31-Mar-2026; Q1 FY27 and Q2 FY27 post-date it and are both held. No missing quarter.
4. INVESTOR PRESENTATIONS. Latest: Q2 FY27 deck, 20261114-Q2FY27-investor-presentation.pdf, 14-Nov-2026. Also held: Q4 FY26 deck (19-May-2026), Q2 FY26 quarterly performance report (about Nov 2025; filename date is a placeholder, period from page 2), Q4 FY25 deck (about May 2025; placeholder date) (B00.input_gaps). No Q1 FY27 deck was found in the 12-month BSE listing (B00). No Q3 FY26 deck is held (B05 input_gaps).
5. RESEARCH / RATING. CARE Ratings rationale, 09-Jul-2026 (7 pages), plus the BSE Reg 30 filing of the same text, 10-Jul-2026 (B00.inventory). Broker or research notes: none (research/ is empty).
6. CORPORATE ACTIONS. 15 Reg 30 and related filings, 11-Dec-2025 to 14-Nov-2026 (B00.inventory): award intimation 11-Dec-2025; Q3 FY26 board outcome 04-Feb-2026; significant order (GTRE) 13-Feb-2026; solar plant commissioning 31-Mar-2026; Reg 30 intimation (MKU) 16-Apr-2026; Q4 FY26 board outcome 19-May-2026; exchange query reply 30-Jun-2026; Q1 FY27 board outcome 13-Aug-2026; order receipt (HAL) 07-Sep-2026; PLR Systems filing 23-Sep-2026; share transfer agent certificate 09-Oct-2026; CQB carbine series production 17-Oct-2026; board meeting notice 02-Nov-2026; analyst meeting notice 12-Nov-2026 (Motilal Oswal one-on-one on 16-Nov-2026); Q2 FY27 board outcome 14-Nov-2026. Order values are withheld in the five defence filings (B05.input_gaps). Shareholding: one text capture of the BSE Sep 2026 pages (no PDF exists).
7. FRESHNESS PAIR CHECK. B00.freshness_verdict reads FRESHNESS PAIRS OK. Results to concall: SKIPPED (concalls_available false). Rating bulletin to full rationale: PASS. SEBI order to order text: PASS (no SEBI order referenced anywhere in the corpus text). AR to latest audited annual results: PASS. No pair failed.
8. EMPTY INPUT FOLDERS AND GAPS (restated from B00; the stage-0 empty-folder question was suppressed under the /step1 autonomy contract, and the standing answer was to carry on with the gaps):
   - Empty folders: concalls (declared), prospectus (long-listed company, CIN year 1975, not expected), research (B00.empty_folder_confirmation).
   - Screener export sheets Profit & Loss, Quarters, Balance Sheet, Cash Flow, Customization came out empty; only screener-Data_Sheet.csv (FY17 to FY26) is populated (B00.input_gaps). The Data_Sheet share-count cell is blank; shares come from the shareholding pattern (1,00,00,000).
   - Shareholding: one quarter (Sep 2026) only; no multi-quarter trend; institutions row reads 0 holders (B00).
   - Q1 FY27 investor presentation: none found in the 12-month BSE listing (B00).
   - Q4 FY26 results filed twice; reason not stated (B00).
   - FY2024-25 AR sits in other/, not annual-report/ (B00).
   - Peer set: PTC Industries (closest process comparable) not collected; peers are AZAD, STEELCAS, ALICON (B00, B06).
   - No FY2025-26 AR gap. Stage 1 recorded that the Q2 FY27 pages it called illegible were repaired afterwards; later stages read the repaired pages (run-log erratum).

VERDICT LINE:

**CORPUS GAPPED**

Findable-but-missing (operator upload list):
- Quarterly shareholding patterns for earlier quarters, to build a 12-quarter pledge and holding trend: BSE shareholding pattern pages (B00, B01, B08).
- AGM 13-Aug-2026 voting result on Item 4 (Rs 18.00 Cr managerial pay ceiling): BSE (B03, B08).
- BSE notice of the Regulation 17 fine (amount and date): BSE (B03, B08).
- Annual reports before FY2024-25 (current liabilities, payables and PPE purchases for FY17 to FY24): BSE or company IR page (B01.input_gaps; B12c G-04 and G-07 separating observation).
- Screener Quarters, Cash Flow, Customization sheets (re-save the workbook and push again): operator machine (B00).
- PTC Industries concall transcripts, the closest process peer: screener or company IR page (B00, B06).
- Meche Pvt Ltd and Tamboli Foundry Supplies and Services financials after March 2021: Registrar of Companies filings (B08).

Plausibly nonexistent (company publishes no such document; opacity is itself a data point for the kill decision):
- Earnings call transcripts (company holds no calls) (B00).
- Prospectus (long-listed; not expected) and broker research (none in folder) (B00).
- Q1 FY27 investor presentation (none in 12-month BSE listing) (B00).
- Order values and an order book for GTRE, MKU, HAL, PLR and CQB (withheld by the company in all five filings) (B05).
- A filed rupee split of aerospace and defence for H1 FY27 (single segment from FY27, Q2 FY27 results note 2) (B05).

No FRESHNESS failure exists, so the verdict is CORPUS GAPPED, not CORPUS GAPPED-FRESHNESS.

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT - PENDING OPERATOR SIGN-OFF**

This declaration is a draft. Nothing here is signed. Signing happens only in claude.ai after live-web stress-testing.

### PART A: THE FROM STATE

**A1. ARCHETYPE.**
- Line 1, auto and non-auto industrial castings (63.84% auto, 30.30% non-auto of the industry split; B04): Build-to-spec component maker. Built to the customer's print; customer build schedules, content per unit and metal-cost pass-through drive it (B04).
- Line 2, aerospace and defence castings (5.86%; B04): Build-to-spec component maker, at an earlier stage. Qualified programme supply with a design-win pipeline (B04 revenue_streams: "qualified programme supply").
- The power segment (1.41% of revenue; B04) supports the castings lines and is not a declared line.

**A2. THE SIMPLE ANALOGY.** Think of a custom tailor who works only from the customer's own pattern. Here the pattern is a metal part drawing, and the cloth is steel or a nickel and cobalt superalloy. The firm makes a wax copy of the part, coats it in ceramic, melts the wax out and pours hot metal in. Then it machines and checks the part. Most of the orders come from car makers, who set the terms and order against their own build plans (B04, B07). A small and growing share goes to aircraft engine and defence programmes, where a part must pass long audits before the first order (B04). Today the firm is a car-parts caster at one site. The arrow points at the defence and aerospace corner of the shop.

### PART B: THE TRANSITION

**B1. FROM to TO (per line).**
- Auto and industrial lines: no transition claimed. They stay where they are. Their tier sits at the R1 to R2 boundary of the QUALITY LADDER: pricing power is weak (B04), ROCE ran 4.15 to 4.86% in FY20 to FY22 and 9.77% in FY25, 13.3% in FY26, median 10.7% (B01).
- Aerospace and defence line, and the company mix it drives: FROM R2 (cost-advantaged converter, at its lower edge) TO R3 (value-added, spec'd supplier: partial pricing power from spec-in and switching costs, ROCE 20 to 25% with stickiness). Declared as one rung. Operator note: if the operator places the FROM tier at R1, the claim becomes two rungs, which the ladder's base rate treats as a red flag in itself. Moat evidence for the TO tier is B07 em_score 7.8, class NONE, with two moderate rows (A1 rare vacuum superalloy capability, B2 qualification lock-in) (B07).

**B2. THE ENGINE.** Two things must change physically.
1. Nominated A&D parts (HAL, GTRE, MKU, PLR Systems, CQB carbine) move from development and first orders into monthly series supply (B05 trigger 1; B07 catalysts). Five Reg 30 filings between Feb and Oct 2026 show orders exist; values are withheld (B05).
2. Fixed-cost absorption: utilisation rises from about 51% (FY26) to about 60% (H1 FY27) on 3,060 t nameplate, and incremental margin on added tonnes runs about 36 to 37% (B04 unit_economics; B05 trigger 2). Note for the model: the FY26 operating margin gain of 277 bp came from power and fuel (-168 bp) and materials (-134 bp), not from A&D mix (B03 strengths_top3).

**B3. THE PROOF GATE.** Binary, read quarter by quarter, in these terms from the blocks:
- Filed A&D rupees at or above 11% of revenue per half-year, with at least one order carrying a stated value (B05 trigger 1 confirm signal). First test: Q3 FY27 results, about Feb 2027; filed industry split in the FY27 AR (B07 catalysts).
- Operating EBITDA margin excluding other income and excluding the inventory credit holds at or above the level the block names: near 14% or above (B05 trigger 2); the FY26 operating level was 16.40% and the monitorable reads at or above 16.0%, below 15.0% is reversal (B03 monitorables, B04 must_track_metrics).
- H2 FY27 operating cash flow at or above profit (B05 trigger 3).
The gate has not fired. The 11% share is a company slide with no filed rupee split (B05, B07). Until it fires, the transition is narrative and the name is research, not a trade. Which of the three observations the operator treats as the binding one is an operator choice at sign-off; the blocks name all three.

**B4. THE RECOGNITION GAP (open question for Stage 11).** Does the TO state, an A&D-led R3 supplier, already look reflected in how the market prices the stock today? This dossier does not answer. Stage 11 resolves it through the PE gap. If the TO state is already reflected, the re-rating engine is gone and only earnings growth remains. No number, no conclusion here.

**B5. THE UGLINESS TEST.** Today's ugly optic is the H1 FY27 cash lag: operating cash flow Rs 348.50 lakh against profit of Rs 1,079.22 lakh (0.32x), inventory up Rs 1,145.75 lakh, and an inventory credit of Rs 863.65 lakh inside a 21.6% EBITDA margin (B01 FLAG-CASH; B05). Classification: ARTIFACT-OF-CLIMB, provisional, resting on one observation.
- For the artifact reading: 10-year CFO/PAT 2.62x and FY26 2.19x (B01); operating cycle fell from 150 to 133 days in FY26 (CARE p.3; B05); receivables over six months are 0.15% of the book (B02); peer Azad's CFO ties its lower consumption line to work-in-progress process content (B06 PEER-WIP-MARGIN); peers show inventory piling up during a ramp (B06); a second reading of the same cash figure runs up to about 0.61x if Rs 307.79 lakh sits in capital advances (B12b F3).
- Against it: the FY26 growth was auto-led (about 91% of the increase; B03, B12b R5), so the climb the build-up serves is not yet shown in filed rupees; the 603.73 lakh Q2 credit is 72.5% of Q2 PBT (B04); Gate 0 on strict written formulas gives a core of 38 (B12c G-04 and G-07); the cash read is INDETERMINATE until H2 FY27 (B01, B05).
- Separating observation: H2 FY27 operating cash at or above profit and a shrinking inventory credit confirms ARTIFACT. Operating cash below profit through FY27 moves it to STRUCTURAL-FEATURE (B05 trigger 3 kill signal).

**B6. THE TRANSITION FALSIFIER.** Any of these kills the arrow (B05, B04, B07):
- A&D share below 8% in H2 FY27 or in the FY27 AR industry split (B05 trigger 1 kill; B07 top_moat_risks).
- Margin falls when the inventory credit shrinks (B05 trigger 2 kill).
- Gearing above 0.80x with utilisation near 60% after the Rs 100 Cr programme is funded (B05 trigger 4 kill).

### PART C: WHAT THE MODEL WATCHES

**C1. DOMINANT VARIABLES** (these become the Role 5.5 tracker signals).
1. A&D conversion into filed rupees and monthly supply. Now: 10.87 Cr, 5.86% in FY26 (B03); 11% on one H1 FY27 slide; five orders, values withheld (B05).
2. Cash conversion and work-in-progress absorption. Now: 0.32x H1 FY27, up to about 0.61x on the second reading; INDETERMINATE (B01, B12b F3, B05).
3. Utilisation and fixed-cost absorption. Now: about 60% vs 51%; operating margin 16.40% FY26; H1 21.6% includes the credit, 13.9% is a floor, not a forecast (B03, B05, B12b F8).
4. Funding of the Rs 100 Cr programme. Now: 88.8% of 30-Sep-2026 equity, gearing 0.71x, 75.8% of debt short term and floating, mix and timeline NOT FOUND (B05, B02).

**C2. WHAT THE MODEL REJECTS.**
- Market size questions. The binding constraint is execution and qualification, not market size: the India served market could not be filtered, so headroom of 27.6x is overstated (B09), and the year-5 case needs 111.8% of nameplate tonnage (B09).
- The management global market claim (USD 17 to 20 bn), which is 30.1x the India figure and not an India claim (B09).
- Single-quarter PAT growth (low Q2 FY26 base), screener cash conversion cycle 245 days (method differs from Note 39 and CARE), spot ROCE while solar assets sit in the base, EBITDA margin including other income, book value as a floor (B04 irrelevant_ratios).

**C3. THE BUSINESS FALSIFIER.** Evidence that forces a re-declaration of the FROM business itself: auto remains the earnings base and the volume driver through the FY27 AR (auto gave 90.8% of FY26 growth; B03) while the margin gain reverses and the metal-cost pass-through lag widens, so the firm behaves as a metal pass-through converter, not a build-to-spec maker. Observables: dispatch tonnes and auto revenue (B04 first_deterioration_signals), materials consumed over revenue (31.96% FY26; B04), and external processing over revenue (27.77%; B04). A second business falsifier: a promoter-entity transfer that changes who the economic operator is, for example the unmoved Rs 306.00 lakh capital advance or the Meche purchases of Rs 319.88 lakh becoming a larger share of costs (B08, B02). This falsifier is distinct from B6.

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

Draft at Halt 1 from B01 to B09, per the shared spec in prompts/13-synthesis-pipeline.md. Stage 13's copy remains the final version.

Investment & Precision Castings makes metal parts to each customer's drawing, from 8 g to 330 kg, at one site, by pouring steel or superalloy into ceramic shells built over wax copies (B04, B07). Auto castings for engines, transmissions and turbos made 63.84% of castings sales in FY26 (B04). Industrial, energy, pump and farm parts made 30.30%, and aerospace and defence parts made 5.86% (B04). A customer cannot switch easily, because each part is built to print and qualified, and defence approvals (DGAQA, CEMILAC, HAL, Nadcap, EN 9100) take long audit cycles (B04 moats_present). The named auto customers are Maruti Suzuki, Mahindra & Mahindra, Tata Motors and Royal Enfield, and the top five customers take about 50% of income (CARE rationale p.2, carried in B05 and B07). The company holds the weaker bargaining position (CARE p.2). The defence names in the filings are HAL, the Gas Turbine Research Establishment of DRDO, MKU and PLR Systems, a joint venture of Adani Group and Israel Weapon Industries (B03, B05). Present demand rests on Indian vehicle production, which gave about 91% of the FY26 sales increase (B03; downstream candidate: Indian vehicle production, ICE and hybrid, B09). Tractor and farm equipment volumes carry 10.02% of sales, and India casting exports and US tariff changes govern the 11.82% sold abroad (B09 candidates). Forward growth outside auto depends on HAL purchase orders and supply schedules, GTRE and DRDO engine programmes, and MoD capital procurement and defence production data, the one budget behind all three (B09 candidates). The plant runs at about 60% of its 3,060 t capacity, so volume can rise without new tonnage (B05, B09). Peer calls show new programmes arriving 6 to 18 months after the first stated date, and nickel and cobalt cost sets the cost of each superalloy part (B06, B09). The auto line has no moat: pricing power is weak and the customer sets the terms (B04). The industrial line has qualification stickiness, but the run did not establish a moat there (B07). The aerospace and defence line has a narrow moat that is still forming: rare vacuum superalloy capability and qualification lock-in each score moderate, and the emerging moat score of 7.8 classifies as none (B07). Own solar and wind supply about 40% of energy, a cost edge of short to medium life, not a moat (B04). The run did not establish customer-level shares, the order book, or true plant capacity (B03, B04).

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. VERTICALS FRAMED

**Vertical 1: A&D conversion into filed rupees and monthly supply.**
- The corpus establishes: A&D revenue 10.87 Cr in FY26 against 5.39 Cr, 5.86% of revenue (B03, B12a). Five Reg 30 filings between Feb and Oct 2026, order values withheld (B05). HAL order dated 05-Sep-2026, 25 days before the half closed (B07 FLAG-CLAIM). CQB series production scheduled to start in Nov 2026 (B05 guidance). The 11% H1 FY27 share is a deck slide (B05, B07). Peers show 6 to 18 months of slip from first stated date (B06).
- It cannot establish: any order value, any monthly supply volume, the A&D share in filed rupees for H1 FY27, civil aviation orders (B05, B03).
- Deciding questions: (1) What are the rupee value and delivery schedule of each of the five orders? (2) Does the 11% reconcile to a filed figure in the FY27 AR industry split? (3) How long from purchase order to series supply at this firm, against the 2.5 years Azad cites to a first qualification batch (B06)?

**Vertical 2: Cash conversion and work-in-progress absorption.**
- Establishes: H1 FY27 operating cash 348.50 lakh vs profit 1,079.22 lakh; inventory +1,145.75 lakh; borrowings 7,009.87 to 8,018.66 lakh (B01, B05). Q2 inventory credit 603.73 lakh, 72.5% of Q2 PBT; other expenditure +77% year on year (B04). Receivables are clean at 0.15% over six months (B02). Second reading up to about 0.61x (B12b F3). 13.9% is a lower bound (B12b F8).
- Cannot establish: how the credit splits between work in progress and finished goods; overhead absorbed in stock; H2 cash; whether other assets of Rs 307.79 lakh are capital advances (B05, B12b).
- Questions: (1) What share of the Q2 credit is fixed overhead parked in stock? (2) Does H2 FY27 operating cash reach profit? (3) What is the Q3 FY27 inventory line?

**Vertical 3: Utilisation and fixed-cost absorption.**
- Establishes: operating margin excluding other income 16.40% (FY26) vs 13.63% (FY25), explained by power and fuel and materials lines (B03); utilisation about 51% to about 60% on 3,060 t (B05); revenue per tonne Rs 12.10 lakh and operating EBITDA Rs 1.98 lakh per tonne in FY26 (B04). Solar 4 MW commissioned 30-Mar-2026 (B05); depreciation steps up by Rs 131.83 to 247.18 lakh a year (B02).
- Cannot establish: plant-wise output; H1 FY27 tonnes; solar cost, generation and saving; capacity basis beyond the 3,060 t vs 1,500 t print conflict (B03, B07).
- Questions: (1) What is the margin excluding the whole inventory line and net of the solar depreciation step? (2) What are H1 FY27 dispatch tonnes? (3) Do power and fuel fall below 8% of revenue for two quarters (B05 trigger 5)?

**Vertical 4: Funding of the Rs 100 Cr programme.**
- Establishes: approval of up to Rs 100 crore on 14-Nov-2026, 88.8% of 30-Sep-2026 standalone equity of 11,261.47 lakh; funding "internal accruals and debt", no split; gearing 0.71x; interest cover 5.12x (B05). 75.8% of debt is short term and floating (B02). CARE's upgrade rested on the absence of planned major debt-funded capex (B05 FLAG-CAPEX). Peers fund differently: Steelcast from cash, Azad from a QIP plus term debt (B06).
- Cannot establish: mix, phasing, lenders, rates, covenants, project list, capital commitment note (B02, B03, B07).
- Questions: (1) Which loans are sanctioned and on what terms? (2) What happens to the rating path and the promoter personal guarantee when the programme is funded? (3) Is the capex phased with customer orders?

### 4b. CANDIDATE SIGNAL TABLE (UNVERIFIED; verification and tracker writes happen at Role 5.5 in claude.ai)

Sources follow the B09 likely_source column and are consistent with the registry types in Downstream_Source_Discovery_Protocol_v1_0 (PIB, DGCI&S, LME and SIAM rows).

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| Indian vehicle production, ICE and hybrid (auto 63.84% of FY26 revenue; B09) | Two consecutive months of falling domestic passenger and two-wheeler production while the firm's dispatch tonnes also fall | Monthly | SIAM monthly production data |
| Tractor and farm equipment volumes (farm 10.02% of revenue; B09) | Two consecutive quarters of falling tractor volumes with farm revenue falling in the next filing | Monthly | Tractor Manufacturers Association releases (PENDING LIVE VERIFICATION, B09) |
| HAL purchase orders and supply schedules (PO 05-Sep-2026; B09) | No HAL-linked order value or schedule appears in a Reg 30 filing or the FY27 AR split by Mar 2027 | Event-Driven | HAL results and releases; I&PCL Reg 30 on BSE |
| GTRE/DRDO engine programmes (order Feb 2026; B09) | Programme slip announced by DRDO or GTRE, or no repeat order after the first supply order | Event-Driven | PIB Ministry of Defence; DRDO releases |
| MoD capital procurement and defence production data (shared across HAL, GTRE, MKU; B09) | Defence production growth falls below the government path in the next PIB annual release, or the procurement budget for the related programmes is cut | Event-Driven | PIB Ministry of Defence |
| India casting exports and US tariff changes (exports 11.82% of revenue; B09) | Foreign exchange earned stays at or below 2,227.15 lakh in FY27 (B07 optionality) or a US tariff step cuts export orders | Monthly | DGCI&S tradestat.commerce.gov.in |
| Nickel and cobalt cost (superalloy input; B09) | A sustained metal cost rise with no matching lift in sales terms within one quarter | Monthly | LME and exchange quote feeds; peer disclosures |

candidate_count carried: 7 (B09.downstream_candidates).

### 4c. FRAGILITY READ

- variable_count: 7 (the seven B09 candidates: vehicle production, tractor volumes, HAL, GTRE/DRDO, MoD procurement, exports and US tariff, nickel and cobalt cost).
- verifiability_ratio: 5 of 7 externally observable (vehicle production, tractor volumes, MoD data, exports, nickel and cobalt cost). The two variables that carry the A&D thesis, HAL and GTRE order flow to this firm, are company-narrated: values are withheld in the filings (B05, B09).
- single_point_failure: yes. The conversion of the nominated A&D programmes into filed monthly supply. B05 and B07 name an A&D share below 8% as the break of the thesis.
- fragility_verdict: FRAGILE (one kill-switch, and the variables that carry the thesis are company-narrated).

### 4d. RESEARCH BRIEF (the claude.ai work order; live-web work the corpus cannot do)

PENDING LIVE VERIFICATION items raised by the Section 4e chains are items 1 to 3.

1. PENDING LIVE VERIFICATION (Chain 1): HAL. Open HAL's latest annual report and quarterly results; read how HAL describes indigenisation, supplier qualification and any casting content, and whether the 05-Sep-2026 purchase order to this firm shows in any HAL source.
2. PENDING LIVE VERIFICATION (Chain 1): GTRE/DRDO. Open the Ministry of Defence PIB releases and DRDO releases on the engine programme named in the 13-Feb-2026 filing; confirm programme stage and the supply-order path.
3. PENDING LIVE VERIFICATION (Chain 2): auto customers. Open the latest quarterly filings of Maruti Suzuki, Mahindra & Mahindra and Tata Motors (named in the CARE rationale) and read payable days and supplier terms.
4. Nadcap register entry for the firm's heat treatment (B07 PENDING LIVE VERIFICATION).
5. MKU: identify the counterparty named in the 16-Apr-2026 filing and read its filings. Do not rely on memory for what the counterparty is or does.
6. PLR Systems (Adani Group and Israel Weapon Industries joint venture) and Adani Defence and Aerospace: programme status and order path for the 21-Sep-2026 filing.
7. MoD capital procurement: primary PIB release for FY26 defence production (the corpus holds a press mirror; B09), and the source of the AR's "159 bn to 538 bn" defence export numbers (B03).
8. SIAM monthly vehicle production, ICE and hybrid split.
9. Tractor Manufacturers Association volumes (B09 PENDING LIVE VERIFICATION).
10. Nickel and cobalt on LME, and the pass-through clauses peers describe (B06).
11. DGCI&S monthly casting exports and the status of US tariffs on castings.
12. CARE annual review path; any Reg 30 loan sanction for the Rs 100 Cr programme; the 2014 CRISIL suspension on non-cooperation (B12b R19) as background.
13. AGM 13-Aug-2026 voting result on Item 4 (Rs 18.00 Cr pay ceiling).
14. BSE notice of the Regulation 17 fine: amount and date.
15. Meche Pvt Ltd and Tamboli Foundry Supplies and Services financials after March 2021 (Registrar of Companies filings).
16. SEBI orders database, eCourts, NCLT and MCA21 charge data; these were not reachable in stage 8 (B08).
17. Primary-source check of the market-size figures: IMARC, MRFR and Grand View pages, and the press mirrors used for PIB, ACMA, IIF and PTC figures (B09 input_gaps).
18. PTC Industries calls and filings as the closest process peer (absent from the corpus; B00, B06).
19. Build Chain 3 (to reach the Rule F floor): Indian auto build, ICE and hybrid mix, electrification exposure of the firm's part list, and the resulting tonnes (B03 INFERENCE, B09).
20. Build Chain 4: MoD capital procurement and defence production as the one budget behind HAL, GTRE and MKU, and the correlated-catalyst test (B09 shared signal).
21. Build Chain 5: nickel and cobalt cost, pass-through lag, work-in-progress build and working capital (B06, B09).

research_brief_items: 21.

### 4e. SECOND-ORDER STUB (Master Prompt v3.7, Rule F)

Two chains drafted from corpus. Links 1 name the counterparty step as PENDING LIVE VERIFICATION. Every fact carries its block cite. Inference is labelled.

```
CHAIN 1: HAL purchase order dated 05-Sep-2026 and five defence orders Feb to Oct 2026, values withheld (B07 FLAG-CLAIM; B05)
Link 1 [PENDING LIVE VERIFICATION]: Who pays, and why now. The paying counterparties are HAL, GTRE (DRDO), MKU, PLR Systems and a domestic CQB carbine maker (B03, B05). Their own demand and funding are not in this container. Claude web to open: HAL's latest annual report and results (indigenisation and supplier lists), the MoD and DRDO PIB releases on the engine programme, and the filings of the other named customers. Not stated here: any customer-side fact.
Link 2 [DOCUMENTED]: What binds. Vacuum capacity is printed as 60 t and as up to 100 t (B07 input_gaps). Capacity is printed as 3,060 t and 1,500 t on one AR page, so utilisation is undecidable on filed text (B03). Inventory rose Rs 1,145.75 lakh in six months and borrowings rose to Rs 8,018.66 lakh (B05). Capital in progress is Rs 383.89 lakh, which is 1.9% of embedded growth (B07). One factory address (B03). External processing is 27.4% of revenue against a "fully integrated" claim (B03).
Link 3 [INFERENCE]: Each nominated part that moves to monthly supply needs work-in-progress stock ahead of dispatch, so a faster A&D ramp raises the working-capital draw before it raises cash. This links the A&D ramp (variable 1) to the cash read (variable 2) and to the short-term debt that funds both (B02: 75.8% short term, floating).
Binding constraint: Qualified capacity and working-capital funding, not demand. Order values are withheld, so the revenue per programme cannot be sized from the corpus (B05).
Unsaid: The AR names HAL only as an award for indigenisation; MKU and monthly supply are NOT FOUND in the AR (B03). Civil aviation was called a "decisive phase of growth" in the AR and dropped from the H1 FY27 deck (B05). Five filings withhold the value (B05; B12b F4 asks to re-grade this as a repeated non-disclosure).
Observation that confirms or breaks this chain, and confirm-by date: Confirm if the Q3 FY27 results (about Feb 2027, B07 inferred date) or the FY27 AR industry split (about May to Jul 2027, B07) show A&D rupees at or above 11% of revenue in a half-year, or any order with a stated value. Break if A&D is below 8% in H2 FY27 or the FY27 AR split (B05 trigger 1).
```

```
CHAIN 2: Q2 FY27 change-in-inventories credit of Rs 603.73 lakh, 72.5% of Q2 PBT, and H1 FY27 operating cash of Rs 348.50 lakh against profit of Rs 1,079.22 lakh (B04; B01 FLAG-CASH)
Link 1 [PENDING LIVE VERIFICATION]: Who pays, and why now. The stock built in H1 is meant to convert to dispatch to the auto customers that give 63.84% of sales (B04) and take about 50% of income through five names (CARE p.2). Their supplier payment days and production schedules are not in this container. Claude web to open: the latest quarterly filings of Maruti Suzuki, Mahindra & Mahindra and Tata Motors. Not stated here: any customer-side fact.
Link 2 [DOCUMENTED]: What binds. Average use of fund-based working-capital limits was about 90% for 12 months to April 2026 (CARE p.3). 75.8% of debt is short term and floating, all by sensitivity, with a director personal guarantee, and no rates, maturities or covenants are disclosed (B02). The Rs 100 Cr approval is 88.8% of equity, funding "internal accruals and debt" (B05). CARE assumed no major debt-funded capex (B05). Net debt on free cash is Rs 6,790.30 lakh (B02).
Link 3 [INFERENCE]: If the Q2 credit is mostly work-in-progress that converts in H2, operating cash catches up with profit and the margin excluding the credit lands near the floor the blocks name (13.9%, a lower bound; B05, B12b F8). If it does not convert, borrowings fund the gap while the same lenders are asked to fund the Rs 100 Cr programme, so the cash read (variable 2) feeds the funding read (variable 4).
Binding constraint: Short-term floating funding against a stock build, with undisclosed lender terms and a rating at BBB (B02, B05).
Unsaid: The Rs 100 Cr mix, phasing and timeline are NOT FOUND; the notes carry no capital commitment note and no events-after-date note on the approval (B02, B03). The best fit for the 77.84 lakh lien-deposit build inside operating cash flow is an inference (B02). The split of the Q2 credit between work in progress and finished goods is NOT FOUND (B05).
Observation that confirms or breaks this chain, and confirm-by date: Confirm if H2 FY27 operating cash is at or above profit and the Q3 FY27 inventory credit shrinks (Q3 FY27 results about Feb 2027; the Mar-2027 cash flow, B07 optionality). Break if operating cash stays below profit through FY27 or gearing passes 0.80x (B05 triggers 3 and 4; B04 must_track_metrics).
```

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in claude.ai with live web, before Role 2.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. The company makes metal parts to each customer's drawing, at one site in Bhavnagar (B04, B03).
2. It pours molten steel or superalloy into ceramic shells built over wax copies, then machines and checks the part (B04).
3. FY26 revenue from operations was Rs 18,844.62 lakh, up 14.16% (B02).
4. Car makers take 63.84% of castings sales, and the top five customers take about half of income (B04, CARE p.2).
5. Aerospace and defence parts are 5.86% of sales. The customers named in filings are HAL, GTRE, MKU and PLR Systems (B03, B05).
6. Demand today rests on Indian vehicle production, which gave about 91% of the FY26 growth (B03, B09).
7. Growth outside cars depends on defence orders and on one government budget behind them. The company has not filed any order value (B05, B09).
8. Peers show new programmes arrive 6 to 18 months after the first stated date, so the ramp may be slower than the slides say (B06).
9. The auto line has no moat. The defence line has a narrow moat still forming, scored 7.8 and classed none (B04, B07).
10. The mental model: a caster of car parts claims to climb one rung to a value-added defence supplier. The climb has not been proven in filed rupees (B04, B05, B07).
11. The fragility read is FRAGILE: seven outside variables, five of them observable, and one failure point in the defence ramp (Section 4c).
12. The cash read is not settled. Operating cash was 0.32 times profit in H1 FY27, and part of the margin came from a stock credit (B01, B05, B12b).
13. The corpus could not establish order values, an order book, true capacity, or the funding mix for the Rs 100 Cr programme. There are no earnings calls (B05, B03, B07).
14. The promoter read is CAUTION on structure, not integrity. Family pay and fees are 29.1% of pre-exceptional profit, and legal-database searches could not run (B08, B02).
15. The biggest open questions: do the defence orders reach monthly supply with filed rupees, and does cash catch up with profit in H2 FY27 (B05, B07)?

plain_summary_points: 15.

### Open items carried for the operator at Halt 1 (as the artifacts state them)

- Verifier C G-04 and G-07 (MAJOR): the filed Gate 0 used substitute formulas for ROCE (EBIT over equity, reserves and borrowings) and FCF (CFO plus CFI). Written strictly each gives core 43 and 44; together the core falls to 38, the lowest Gate 0 class, against the filed AVERAGE (core 49). An operator ruling is needed (B12c). EM-11 (MAJOR): the offset rule that zeroes E2, G1, G2, H2, C1, F1 is not in prompts/07; the written matrix gives 10.8 to 12.6 against the filed 7.8, band NONE vs MODEST at the edge; an operator ruling is needed (B12c). EM-12 (MAJOR) is also recorded: the A1 multiplier, no decision effect on the filed set.
- Verifier B states two readings of its own rate: 71% counting PARTIALLY CAUGHT as caught (5 of 7, the block field the confidence file uses) and 29% on full catches only (2 of 7). On the strict count the component would sit below 60% on a denominator of 7 and the mechanical trigger for a remediation cycle would fire. The orchestrator did not re-score a verifier; this is an open item (confidence.yaml notes).
- Stage 8 (promoter) status is partial: CMD biography, Regulation 17 fine amount, AGM voting result, Meche and Foundry financials, and SEBI, eCourts, NCLT and MCA21 checks are NOT FOUND or skipped (B08).
- FLAG-CASH: INDETERMINATE. H1 FY27 operating cash 0.32x profit; second reading up to about 0.61x; resolves with H2 FY27 cash (B01, B05, B12b F3).
- Verifier A: one MAJOR (the derived India defence production rate; 18.8% over four years, not 14.8%; B12a) and six MINOR, three of them source-fidelity findings on page anchors. This dossier uses the corrected anchors.
- Confidence overall 71, set by redflag_coverage (confidence.yaml). Shadow Verifier A was not run in this session.

---

## SECTION 6: STANDING EXTRACTION ANNEX

AR = annual-report/Annual_Report_FY2025-26.pdf, PDF page. Quotes are as printed after text extraction; extraction spacing and rupee-sign glyphs normalised. Units INR lakh unless stated.

### 1. UNITS

- Quote: "Dispatch ( In T onnes )" series, years 2021-22 to 2025-26, values "1429 / 1519 1452 / 1372 / 1557" (AR p.23). Comment: 1,557 t is the FY26 dispatch (B04 reads the last value as FY26; the chart text order is extraction order). The unit is tonnes of castings dispatched; it is a basket of auto, industrial, farm and A&D parts, not one product.
- Quote: "Casting Capacity 3,060 metric tonnes across all plants" (AR p.30). Comment: nameplate basket capacity. B03 notes 1,500 appears elsewhere on the same page as an alternative print; B09 confirms 3,060 t because 1,557 t is 50.9% of 3,060 t (deck: 51%).
- No per-tonne figure is printed. Derivation lines: revenue "Total Revenue 18,579.08 ... 265.54 ... 18,844.62" (AR Note 38 segment table, p.172) and dispatch 1,557 t. B04 derives Rs 12.10 lakh per tonne (18,844.62 lakh over 1,557 t, power segment included) and Rs 1.98 lakh operating EBITDA excluding other income per tonne (3,089.77 lakh over 1,557 t); FY25 Rs 1.64 lakh. Comment: the figure is a blended basket, not a product realisation; castings-only revenue is the 18,579.08 lakh line.
- Quote: "Capacity utilization ~60%" with "H1 FY 27" (Q2 FY27 presentation p.17). Comment: FY26 utilisation about 51% (Q4 FY26 deck p.6, B05). H1 FY27 tonnes are NOT DISCLOSED (B07 input_gaps).

### 2. SEGMENT CAPITAL AND DEBT

- Quote (AR p.173, consolidated Note 38, "SEGMENT ASSETS AND LIABILITIES"): "Segment Assets 19,752.80 19,281.29 1,903.97 188.59 21,656.77 19,469.88"; "Segment Liabilities 10,269.30 10,343.35 1,126.48 - 11,395.78 10,343.35". Column order: Investment Casting 2026, 2025; Power Generation 2026, 2025; Total 2026, 2025. Unallocated corporate assets and liabilities print as "-".
- Comment: power segment assets rose from 188.59 to 1,903.97 and liabilities from nil to 1,126.48, which tracks the 4 MW solar plant commissioned 30-Mar-2026 (Reg 30, announcements/20260331-solar-commissioning). Capital employed by segment is not printed; the assets and liabilities above are the inputs.
- Borrowings by segment: NOT DISCLOSED. AR p.172: "The Group's financing (including finance costs and finance income) and income taxes are managed on a Group basis and are not allocated to operating segments." Comment: total debt is Rs 7,009.87 lakh at 31-Mar-2026 (B02, Note 17) and 8,018.66 lakh at 30-Sep-2026 (Q2 FY27 results p.5 and p.6, as carried in the synthesis-lite anchor table). From FY27 the company reports one segment: "the Company has from this year, identified Investment Casting Activities as its only reportable segment" (Q2 FY27 results note 2), so no segment balance sheet exists for H1 FY27.

### 3. GUIDANCE VERSUS ASPIRATION

No document carries a numeric revenue, margin, order book or return figure as a forward statement (B05 guidance row: "NOT FOUND"). The forward statements:

| Statement (quote) | Source | Class | Comment |
|---|---|---|---|
| "The Board has approved a capital investment of up to [Rs] 100 crore towards the development and execution of various projects in the Aerospace, Defence & Energy sector" | Q2 FY27 results note 6 (OCR reads "2100 crore"; deck p.6 reads "up to Rs 100 crore"); presentation p.6 | (b) aspiration without a period; also (c) capability | No timeline, no funding split. Deck p.11: "Funded through internal accruals and debt". |
| "In the second half, our focus is moving more nominated parts into monthly supply and continuing to build new capabilities." | Q2 FY27 presentation p.6 | (a) qualitative, period H2 FY27; no number | No rupee or tonne figure. |
| "Supplies are scheduled to commence shortly ... Delivery commencement: Scheduled for November 2026" | announcements/20261017-reg30-update p.1 | (a) guidance with a period | CQB carbine components; no value. |
| "The project is in the development phase, with operational [...] for the second half of FY 2026." | AR p.74 (Annexure 4); one word omitted by the dossier for vocabulary rules | (a) guidance with a period, elapsed | Plant was commissioned 30-Mar-2026 (Reg 30); B03 rates credibility LOW because the AR printed the old line after commissioning. |
| Solar "lower energy costs and improved operating margins" | AR p.19 (CFO message, via B03) | (b) aspiration without a period | No kWh or rupee figure. |
| Civil aviation "decisive phase of growth" | AR p.36 (via B03) | (b) aspiration without a period | Absent from the H1 FY27 deck (B05). |
| Final dividend "of Rs 1 per share" | AR (Directors' report; B03 cites p.55) | (a) with a period, the AGM of 13-Aug-2026 | B05 records it paid, 99.28 lakh in the H1 FY27 cash flow. |
| "Casting Capacity 3,060 metric tonnes across all plants"; programme listed as lost-foam, CNC, heat treat, vacuum | AR p.30; Q2 FY27 presentation p.5 and p.11 (via B05, B07) | (c) capacity or capability only | Commissioning dates NOT FOUND. |

The government defence production path of Rs 3 lakh crore by 2029 appears in the deck (p.16). It is a third-party path, not management guidance; the derived rate is 18.8% over four years (B12a).

### 4. CONCENTRATION

- Product: "Auto 118.35 Cr 63.84% Of Revenue; Industrials 37.60 Cr 20.28%; Farm 18.58 Cr 10.02%; Aerospace & Defence 10.87 Cr 5.86%" (AR p.22). Top product class share: auto 63.84%. Industry split in lakh (Note 38, AR p.173): "Auto 11,835.19; Non auto 5,617.90; Aerospace and Defence 1,086.42; total 18,539.51".
- Customer: "50+ Major Customers" (AR p.20). "IPCL's top five customers constituted ~50% (PY: 47%) of its TOI in FY26, exhibiting moderate customer concentration risk" (CARE rationale p.2). Top single customer share: NOT DISCLOSED (no major-customer note in the AR; B03 missing_risks).
- Geography: "India 16,617.47 14,872.81; Outside India 2,227.15 1,634.56" (AR p.173). CARE: domestic "~88% (PY: ~90%) of total sales" (p.2). US share of exports: NOT DISCLOSED.

### 5. PROMISE LEDGER

| Promise (quote or paraphrase) | Date made | Status | Evidence anchor |
|---|---|---|---|
| 4 MW solar operational "second half of 2025" | Q4 FY25 deck, about May 2025 (placeholder filename date) | PARTIAL: commissioned 30-Mar-2026, about 3 months late; AR re-stated the line as "second half of FY 2026"; Verifier B says the slip is understated (B12b F6) | presentation/Q4 FY25 deck p.11; announcements/20260331 p.1; AR p.74 |
| Long-term international defence project from March 2025 | Q4 FY25 deck, about May 2025 | DELIVERED as a status statement; B12b F14 asks to tie it to PLR evidence | Q4 FY25 deck p.11; AR p.22 (A&D 10.87 vs 5.39 Cr) |
| Strong defence order inflow; non-auto gains in coming quarters | Q2 FY26 report, about Nov 2025 | DELIVERED for orders (five Reg 30 filings, Feb to Oct 2026, values withheld); non-auto fell about 13% in FY26 (B12b R5) | Q2 FY26 report p.12; Reg 30 filings 13-Feb, 16-Apr, 7-Sep, 23-Sep, 17-Oct-2026 |
| Robust growth momentum | Q2 FY26 report | PARTIAL after Verifier B F7: sales rose each quarter (4,395.53 to 5,795.19 lakh standalone) but growth was auto-led | Q2 FY26 report p.12; results filings; AR p.24 |
| Spare capacity, ready to ramp | Q4 FY26 deck, 19-May-2026 | DELIVERED, low bar: utilisation 51% to about 60% | Q4 FY26 deck p.6; Q2 FY27 deck p.17 |
| Dividend Rs 1 per share | AR / Board, May 2026 | DELIVERED: 99.28 lakh paid in H1 FY27 | AR (Directors' report); Q2 FY27 results cash flow p.6 |
| Solar to improve cash flow, energy cost and margin | Q2 FY26 report p.12; AR p.19 | NOT YET TESTABLE: power and fuel 8.99% vs 9.17% of revenue; H1 FY27 cash 0.32x | Q2 FY27 results; B05 row 7 |
| Civil aviation "decisive phase of growth" | AR p.36 | UNSCORABLE: no civil order named; dropped from H1 FY27 deck | AR p.36 via B03; B05 dropped_triggers |

Counts as Verifier B stated them: delivered 4, partial 2, missed 0 (B12b). Credibility grade C (B05; B12b concurs at its low end). The five written statements Verifier B finds contradicted by company filings: R5 (broad-based growth, twice), R10, R11 (debt to equity framing), R12 (interest-cover comparator) (B12b credibility_grade_concur).

### 6. RESTATED BASES

- Quote: "Previous period's figures have been reclassified, wherever necessary, to correspond with those of the current period." (Q2 FY27 results note 5.) Quote: "Previous year's figures have been regrouped and rearranged, wherever necessary." (AR p.175, Note 45). Neither quantifies the change.
- Comparative as printed in the latest deck (Q2 FY27 presentation p.21, appendix): "Revenue from Operations 5,800.16 | 5,337.20 | 8.67% | 4,408.90 | 31.56% | 18,579.07" under the headers "Q2 2026-27, Q1 2026-27, Q-o-Q, Q2 2025-26, Y-o-Y, FY 2025-26". "Power & Fuel ... 1,706.49" for FY 2025-26 on the same slide.
- Audited FY26 base: "External revenue 18,579.08 (castings) + 265.54 (power) = 18,844.62" (AR p.172, Note 38).
- Comment: the deck's FY26 revenue is 265.55 lakh below the audited 18,844.62; B05 reads the difference as a wind credit netted against power and fuel from FY27, with Q2 FY26 re-presented from 4,502.23 to 4,408.90 lakh (05-concall.md; the filing notes quoted above do not state the reason). Treat that reason as a stage-5 reading, not a filed statement. The results show 18,539.50 lakh as a third basis and the cause of the 39.57 lakh gap is NOT FOUND (B04). Consolidated FY25 EPS prints 3.03 where 6.06 is arithmetic after the bonus issue (B02, a printing error not a restatement, B12a).

### 7. CORPORATE-ACTION CLAUSES

- No scheme of arrangement, demerger, merger, preferential issue, share repurchase or rights issue exists in the corpus. Quote: "There was no preferential allotment or qualified institutions placement as specified under Regulation 32 (7A)" (AR p.90). Quote: "The Company has not made any preferential allotment or private placement of shares or fully/partly convertible debentures during the year" (AR p.103, CARO). A search for scheme, demerger, merger, repurchase and rights issue across the AR and all 15 announcements found only these lines and a list of SEBI regulations in the AR's compliance section. Nothing to fetch.
- One corporate action: bonus issue. Quote: "The Parent Company has issued 5,000,000 equity shares of Rs 10 each as fully paid up Bonus Shares in the ratio of 1:1 on 27th June, 2025 by capitalization of securities premium account and general reserve." (AR p.174, Note 42). Comment: MGT-9 shareholding tables print the bonus date as 01.07.2025 (AR p.68 and p.69); the two dates differ by four days in the same AR (record date vs allotment is not stated). Appointed date, effective date, undertaking definitions and liability allocation: not applicable.

### 8. RELATED-PARTY PERIMETER

AR Note 38, pp.134 and 135 (INR lakh, FY26 then FY25). The AR lists as "Associates": Tamboli Foundry Supplies and Services Limited, Shri Tamboli Foundation, Meche Private Limited, Piyush I Tamboli - HUF. Subsidiary: I&PCL Vacuum Cast Limited.

| Entity | Nature | FY26 | FY25 |
|---|---|---|---|
| Meche Private Limited (16.19% promoter group shareholder; BSE Sep 2026) | Purchase of materials and services | 319.88 | 254.93 |
| Meche Private Limited | Security deposits given | 100.00 | 100.00 |
| Meche Private Limited | Trade advances to suppliers | 49.75 | 61.11 |
| Tamboli Foundry Supplies and Services Limited | Capital advance | 306.00 | 306.00 |
| Tamboli Foundry Supplies and Services Limited | Trade receivables | 3.81 | 3.81 |
| Shri Tamboli Foundation | Corporate social responsibility | 13.86 | 17.56 |
| Piyush I Tamboli - HUF | Rent | 24.00 | 20.00 |
| Piyush I Tamboli - HUF | Trade payables | 1.80 | 1.80 |
| Shri Piyush I Tamboli (CMD) | Remuneration | 347.11 | 229.54 |
| Shri Piyush I Tamboli | Guarantee commission | 84.52 | 71.42 |
| Shri Jainam P Tamboli (WTD and CFO) | Remuneration | 46.28 | 27.44 |
| Shri B. Pratapkumar (WTD) | Remuneration | 32.00 | 32.55 |
| Smt. Hetal Kapadia (Company Secretary) | Remuneration | 2.40 | 2.40 |
| Ms. Kavya P Tamboli (relative) | Salary | 6.00 | 5.00 |
| Independent directors and Smt. Vishakha P Tamboli | Sitting fees (total) | 8.87 | 6.33 |
| Piyush I Tamboli, Jainam P Tamboli, Kavya P Tamboli | Trade payables outstanding (total) | 25.15 | 19.27 |
| I&PCL Vacuum Cast Limited (subsidiary) | Advance granted/(received back); trade payables | (0.92); trade payables 6.49 | (1.87); trade payables 7.41 |

Comment: B02 totals the flows at 884.92 lakh, 4.70% of revenue, and the family cash take at 507.91 lakh, 29.1% of pre-exceptional PBT; no arm's-length benchmark is disclosed (B02, B08). The Rs 306.00 and 100.00 lakh balances did not move in a year.

### 9. PLEDGE AND SHAREHOLDING

Twelve quarters as filed: NOT DISCLOSED in the corpus. Only one quarterly pattern (Sep 2026) is held, plus year-start and year-end figures from two ARs. Findable at the BSE shareholding pattern pages (gap listed in Section 1).

| As at | Promoter and group holding | Pledged | Source |
|---|---|---|---|
| 01-Apr-2024 | 25,95,626 shares, 51.92% | 0 | FY2024-25 AR (inputs/other/Annual_Report_FY2024-25.pdf), p.52 |
| 31-Mar-2025 | 25,98,657 shares, 51.98% (printed) | 0 | FY2024-25 AR p.52 |
| 01-Apr-2025 | 2,598,657 shares, 51.97% (the FY26 AR cumulative row also prints 51.91% for 2,595,626 shares) | 0 | FY2025-26 AR p.68 |
| 31-Mar-2026 | 5,197,314 shares, 51.97% (after 1:1 bonus) | 0 | FY2025-26 AR p.68 |
| 30-Sep-2026 | 51,97,314 shares, 51.97% | "promoter pledge or encumbrance (pledge, NDU, other)": No | shareholding/20260930-shareholding-pattern-Sep2026-BSE-page.txt |

Quote (AR p.68, Change in promoter's shareholding): "At the beginning of the year (As on 01/04/2025) 2,595,626 51.91 ... Bonus issue (1:1) 3,031 0.06 ... At the End of the Year (As on 31/03/2026) 2,598,657 51.97 5,197,314 51.97". Comment: the begin and end rows mix pre-bonus and post-bonus share counts in one table, which is a printing defect; percent holding is 51.97% at the end. One promoter-group holder, R K Menon (1,600 shares, 0.03%), appears in the opening table and has no closing holding (AR p.68).

Institutional holding, latest: "Institutions (domestic, foreign) and Central/State Govt: 0 holders, 0 shares, 0.00%" (shareholding/20260930-shareholding-pattern-Sep2026-BSE-page.txt). Public holding 48.03% across 5,304 holders, of which one holder, Rekha N Shah, holds 10.00% (same file). B08: pledge stable at nil on all dates held.

### 10. VERIFICATION

Documents quoted in this annex, with dates:
- runs/invprecq-2026-11-15/inputs/annual-report/Annual_Report_FY2025-26.pdf (year ended 31-Mar-2026; pages 20, 22, 23, 30, 68, 69, 74, 90, 103, 172 to 175).
- inputs/other/Annual_Report_FY2024-25.pdf (year ended 31-Mar-2025; page 52).
- inputs/results/20261114-Q2FY27-results.pdf (14-Nov-2026; notes 2, 5, 6; OCR; rupee sign can read as "2").
- inputs/presentation/20261114-Q2FY27-investor-presentation.pdf (14-Nov-2026; pages 6, 11, 17, 21).
- inputs/rating/20260709-CARE-rationale.pdf (09-Jul-2026; pages 1 to 3).
- inputs/announcements/20261017-reg30-update.pdf (17-Oct-2026) and 20260331-solar-commissioning.pdf (31-Mar-2026).
- inputs/shareholding/20260930-shareholding-pattern-Sep2026-BSE-page.txt (text capture, 15-Nov-2026, quarter Sep 2026).
- Stage reports and blocks used for derived figures: outputs/blocks/B01 to B09, B12a to B12d, confidence.yaml; outputs/reports/05-concall.md (wind credit reading).

CORPUS COMMIT HASH: 8574d70aa0e6b7ebaf9d7a8c5e6f292f1006da08
