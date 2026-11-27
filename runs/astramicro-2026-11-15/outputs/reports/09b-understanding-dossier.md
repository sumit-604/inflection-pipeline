# HALT 1 UNDERSTANDING DOSSIER: Astra Microwave Products Ltd (ASTRAMICRO), run 2026-11-15

Stage 09b. Assembled from committed blocks B00 to B09, B12a, B12b, B12c (phase 1 partial), B12d and confidence.yaml. Stage report ERRATA govern over report bodies. Verifier A's corrected page anchors (B12a) govern where a stage anchor slipped. The first five parts add no research. The chain stub in part 4e carries labelled inference. The last part, the extraction annex, quotes the corpus. This file states no valuation and no action. Units: Rs Cr unless a figure says Rs Lakhs. Filings and the annual report print Rs Lakhs. The unit rides with each figure.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

Inventory only. Source: B00 (input inventory, corpus manifest, freshness pairs). Run date 2026-11-15.

### 1.1 Concalls (company)

| File | Quarter | Call date |
|---|---|---|
| inputs/concalls/Concall_Feb_2026_Transcript.pdf | Q3 FY26 | 2026-02-13 |
| inputs/concalls/Concall_Jun_2026_Transcript.pdf (filename month is the filing month) | Q4 FY26 | 2026-05-27 |
| inputs/concalls/Concall_Aug_2026_Transcript.pdf | Q1 FY27 | 2026-08-11 |

Most recent quarter covered: Q1 FY27. A more recent quarter has reported. The Q2 FY27 results were filed 2026-11-12 and the Q2 FY27 call was held 2026-11-13 (B00). Its transcript is ABSENT. BSE carries only the audio filing 92bb686f (B00).

Peer concalls (context only): 8 files, APOLLO 4 and DATAPATTNS 4, dated 2025-11-13 to 2026-10-26 (B00 manifest). PARAS: ABSENT. No transcript exists in 90 BSE filings for scrip 543367 (B00, B06).

### 1.2 Annual reports

| File | Year | Filing letter |
|---|---|---|
| inputs/annual-report/Annual_Report_2026.pdf | FY26, 35th AR, AR of record | 2026-08-22 |
| inputs/annual-report/Annual_Report_2025.pdf | FY25, 34th AR, prior-year reference | 2025-08-20 |

The latest completed FY (FY26) is present. Two years are held, not three. The FY24 annual report is ABSENT. B03 records that FY23 CFO and the FY24 balance sheet are not in the FY26 AR. The ten-year series comes from the screener Data Sheet (B01). This item is raised by this stage from the three-year test. It is not in B00.input_gaps.

### 1.3 Results filings

| File | Period | Date |
|---|---|---|
| inputs/results/2026-11-12_Q2FY27_results_70cb396f.pdf | Q2 and H1 FY27, unaudited | 2026-11-12 |
| inputs/results/2026-08-10_Q1FY27_results_c4386b87.pdf | Q1 FY27, unaudited | 2026-08-10 |
| inputs/results/2026-05-26_Q4FY26_audited_results_f086a834.pdf | Q4 and FY26, audited | 2026-05-26 |

The latest AR covers the year to 2026-03-31. The latest results filing covers the half year to 2026-09-30. The quarter gap is two quarters (Q1 and Q2 FY27). Both are held. Q1 to Q3 FY26 quarterly filings are not held in results/. The screener Data Sheet carries quarters to Sep 2026 (B00).

### 1.4 Investor presentations

inputs/presentation/Investor_Presentation_1.pdf: Q2 FY27 deck, cover letter 2026-11-12. This is the only deck held. The Q2 FY27 press release (2026-11-12) sits in presentation/ and was left there (B00 identity note).

### 1.5 Research and rating

- inputs/rating/CRISIL_rationale_2026-08-28.txt: CRISIL rationale dated 2026-08-28, long term upgraded to A+/Stable, short term A1 reaffirmed (B00 manifest). Text only, no page markers.
- Two Reg 30 rating intimations: 2025-12-12 and 2026-08-31 (B00).
- research/ is empty. No broker or research note is held (B00).

### 1.6 Corporate actions

22 announcement filings, 2025-11-18 to 2026-11-12 (B00 manifest). They cover: subsidiary name change (2025-11-18); IMD order (2025-12-11); Astra Rafael Comsys (ARC) orders (2025-12-12, 2026-01-08, 2026-04-02); BEL MoU (2025-12-26); CFO change (2026-02-12); demerger in-principle approval and revised press release (2026-02-27); MD stepping down, two documents (2026-04-03); monitoring agency reports (2026-05-12, 2026-11-12); scheme board meeting notice and board approval (2026-06-01, 2026-06-10); HAL orders (2026-07-30); subsidiary conversion to public limited (2026-08-19); CRISIL rating (2025-12-12, 2026-08-31); AGM voting results (2026-09-18); exchange observation letters on the demerger (2026-10-29); deviation statement (2026-11-12). Shareholding: BSE pattern at 2026-09-30, text only (B00).

Anomaly carried from B00: the AGM voting results body text reads "held on September 18, 2025" against a 2026 letter date. Unresolved.

### 1.7 Freshness pair check (B00.freshness_verdict and freshness_pairs)

| Pair | Trigger held | Mate | Status |
|---|---|---|---|
| 1. Results to concall | Q2 FY27 results, 2026-11-12 | Q2 FY27 concall transcript (call 2026-11-13) | FAIL, mate ABSENT |
| 2. Rating bulletin to rationale | CRISIL 2026-08-28 | Full rationale | PASS |
| 3. SEBI order to order text | None found in the FY26 AR text | Order text | PASS (see web-sourced items below) |
| 4. AR to latest audited annual results | Q4 FY26 audited results, 2026-05-26 | FY26 AR | PASS |

Failed pair named: pair 1. The Q2 FY27 results filing is held. The Q2 FY27 concall transcript is not held. Expected source: BSE corporate announcements for scrip 532493, or the screener documents page (B00). The consequence for the phase 1 gate recommendation sits with the orchestrator.

### 1.8 Verdict line

**CORPUS GAPPED-FRESHNESS**

Missing mate first: Q2 FY27 concall transcript. Other gaps, repeated in full from B00.input_gaps:

Findable but missing (the operator upload list):
1. Q2 FY27 concall transcript (call 2026-11-13). Source: BSE scrip 532493 or screener documents page. Priority HIGH. Freshness pair 1.
2. Screener sheets Profit & Loss, Quarters, Balance Sheet, Cash Flow and Customization came out EMPTY (formulas with no cached values). No CSV written. Only screener-Data_Sheet.csv is populated (FY17 to FY26, quarters to Sep 2026). Fix: open Financials.xlsx once, save, run the collector with --push-again.
3. Filing on the successor MD appointment (Oct 2026 per the step 1 brief, web-sourced). Only the April 2026 stepping-down filings are held. Source: BSE.
4. Warrant and preferential allotment filing. It sits outside the 12-month BSE window. The monitoring agency reports (Q4 FY26, Q2 FY27) and the Q2 FY27 deviation statement are held. Source: BSE.
5. Three web-sourced SEBI items, none referenced in any corpus filing, so freshness pair 3 is not re-scored (B00, B08). None of the texts is in the corpus.
   a. SEBI inquiry email of 2 Mar 2026 on the FY24 results, company reply 6 Mar 2026. Media only. The company's Reg 30 text is not in corpus. Source: BSE.
   b. SEBI Adjudication Order SD/AO/65/2010 against M/s Suresh Kumar Somani. Identity with the Astra director NOT confirmed. Source: sebi.gov.in.
   c. SEBI order on Skanda Aerospace (Dec 2017, a shareholder). Source: sebi.gov.in.
6. FY24 annual report (company IR page). See 1.2.
7. Demerger scheme text with Appointed Date, and the ASTPL Information Memorandum, are not in the corpus (see the annex, question 7). Source: BSE and NSE scheme filings, company IR page.

Plausibly nonexistent:
8. PARAS peer concalls. None exist in 90 BSE filings (B00). The peer set is two, not three. Silence here is a data point on PARAS coverage, not on any topic.

Empty folders: prospectus/ (long-listed company, not expected) and research/ (no effect on anchored evidence). The empty-folder confirmation was suppressed under the /step1 autonomy contract. The standing answer was to go on with the gaps (B00).

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT - PENDING OPERATOR SIGN-OFF**

This is a draft for the operator. It is stress-tested on live web in claude.ai before any sign-off. Nothing in this file marks it final.

### PART A: THE FROM STATE

**A1. Archetype (per line).**
- Defence and strategic electronics: radar, electronic warfare, missile electronics and MMIC subsystems, plus exports including deemed exports. Defence 72.5% and exports 14.0% of FY26 standalone revenue (B04). Archetype: **Order-book business (EPC/defence/capital goods)**. The deciding variables are order inflow, book-to-bill, execution pace, working capital and margin on backlog (B04 must_track_metrics). The parts inside are build-to-spec subsystems.
- Space, meteorology and hydrology: ISRO and IMD work, 9.5% and 4.0% of revenue (B04). It leaves the listed company in the demerger (B05, B09). Archetype: **Build-to-spec component maker**.

**A2. The simple analogy.** Think of a firm that builds the sensitive ears and voice boxes for a country's watchtowers. The state designs each tower and tests every part for months. Astra makes the electronic parts that listen and shout, and sometimes the whole unit. The state is almost the only customer (B04: strategic customers 96.0%). It pays after the part passes inspection, so Astra holds large stock and large unpaid bills while it waits (B04: working capital intensity high). One tower order from HAL is now nearly half the work booked (B04: 47.7% of the book).

### PART B: THE TRANSITION

**B1. FROM to TO (defence line).** FROM: **R3 Value-added / spec'd supplier**. Evidence: consolidated ROCE 22.94% in FY26, inside the R3 band of 20 to 25% (B01); spec-in and switching costs on multi-year programmes (B04 moats_present); cash volatile, 10-year cumulative CFO to PAT 0.47 (B01). TO: **R4 Franchise / share-of-wallet leader**, ROCE 25 to 30% durable with strong cash. The claimed move, as the run reads management's narrative, is from supplier of parts to maker of systems and volume radars (B05 triggers 1 and 9; complete systems 27.8% of FY26 revenue against 12.0% in FY23, B03). This is one rung, inside the one-rung-per-2-to-3-years base rate. The management claim of 6 to 7x last year's turnover in 5 years (B05) is a scale claim, not a rung claim. B09 finds it larger than the whole FY31 serviceable pool (FLAG-MGMT-CLAIMS-INCONSISTENT). The space, meteorology and hydrology line does not transition in the listed entity. It exits.

**B2. The engine.** Two physical changes.
1. Mix shifts to production orders and complete systems. Gross margin rose from 43.87% to 49.18% and EBITDA before other income from 25.51% to 28.07% (B03). Management credits build-to-print exit. B04 calls the flat material cost unexplained: net material cost stayed flat while revenue grew 10.67% (B02 finding 12).
2. The HAL Uttam AAAU production ramp: 122 AAAU and 121 interface frames within 5 years, Phase 1 of 12 units by Sep 2027 (B05 trigger 1, B04). It turns development-era capability into volume production.

The optic that hides the engine: H1 FY27 standalone CFO of minus Rs 146 Cr, inventory Rs 793 Cr against Rs 609 Cr, current borrowings Rs 411 Cr against Rs 224 Cr (B04).

**B3. The proof gate.** The binary, read on the FY27 audited results (due about end May 2027, by the Q4 FY26 filing date of 2026-05-26 in B00): FY27 standalone EBITDA margin before other income **at or above 28.07%** (B03 monitorables, B05 trigger 4), AND FY27 standalone CFO **positive** with year-end inventory **at or below Rs 793 Cr** (B04 must_track_metrics, B05 trigger 8). A second stage follows: Uttam Phase 1 delivered by Sep 2027, with the margin and advance terms disclosed (B05 trigger 1). Status today: NOT FIRED. H1 FY27 CFO is negative (B05). Until it fires, the transition is narrative and the name is research, not a trade. FTTCP (/fttcp) tests this gate. The operator may reset the threshold at sign-off.

**B4. The recognition gap (open question for Stage 11).** Does the TO state, an R4 supplier with durable cash, already look reflected in market pricing? This dossier does not answer. The corpus carries no market input by design. Stage 11 resolves it through the PE gap. If the TO state is already priced, the re-rating engine is gone and only earnings growth remains. No number, no conclusion here.

**B5. The ugliness test: STRUCTURAL-FEATURE (provisional, most evidenced reading).** The ugly optic is weak cash conversion with a long working-capital cycle. Evidence it is structural, not a temporary feature of the climb:
- 10-year cumulative CFO to PAT is 0.47. CFO was negative in FY23, FY24 and FY25 (B01 deal-breaker DB4).
- Working-capital days were 460.23 in FY25 and 373.69 in FY26 (B01 data_notes). B04 rates working-capital intensity high.
- Peers carry similar cycles: Data Patterns 345 to 365 days, Apollo in the same range (B06 cross_peer_hypothesis). The pattern belongs to the sector channel as well as to Astra.
- The FY26 CFO of Rs 387 Cr leaned on a working-capital release of 35.4% and payable days stretched to about 72 from 40 (B02 finding 5).
- Over-2-year receivables rose to 8,158.33 from 4,591.91 (Rs Lakhs) with cover down to 14.9% from 19.6% (B02 finding 3).

The other reading: a build ahead of production orders (Uttam), seasonal and Q4 loaded. Management says March balances are always high (B05 analyst_note). The observation that separates the readings: FY27 year-end CFO and inventory (B05, B06 FLAG-PEER-CFO). Apollo's positive H1 CFO of Rs 22 Cr does not settle it (B06). No trade posture is drawn here. Stage 13 carries the classification.

**B6. The transition falsifier.** Any one of the following kills the arrow:
- FY27 standalone CFO negative again with inventory above Rs 793 Cr at year end (B05 trigger 8 kill signal).
- Uttam Phase 1 slips past Sep 2027, or DRDO bulk production clearance is delayed, or no advance is disclosed while working-capital borrowings keep rising (B05 trigger 1 kill signal).
- Q3 or Q4 FY27 EBITDA margin below 27%, or Uttam booked at a lower initial margin (B05 trigger 4 kill signal).
- Order book ex-HAL keeps falling below Rs 2,058 Cr while revenue is booked (B04 first deterioration signals).

### PART C: WHAT THE MODEL WATCHES

**C1. Dominant variables.** Four. They become the Role 5.5 tracker signals.
1. **HAL Uttam AAAU execution and terms.** Order Rs 1,878.8 Cr ex-tax is 47.7% of the Rs 3,937 Cr book. Margin and advance NOT FOUND on any call or filing (B04, B05).
2. **Cash conversion and working capital.** H1 FY27 CFO minus Rs 146 Cr. Inventory Rs 793 Cr. Current borrowings Rs 411 Cr. Gate 0 core 53, AVERAGE, held down by cash conversion (B01, B04).
3. **Margin held through mix.** Gross margin 49.18% and EBITDA before other income 28.07% in FY26 (B03). Q2 FY27 EBITDA margin 33.2% and H1 27.4% (B04).
4. **Order book ex-HAL and book-to-bill.** Ex-HAL book Rs 2,058 Cr against Rs 2,141 Cr at Mar-26 (B04). QRSAM orders slipped on three calls (B05).

**C2. What the model rejects.** Noise for this model:
- Market size questions. The runway class is GOOD, and Astra already holds 24.8% of the serviceable pool (B09). The binding constraint is execution and cash, not market size.
- The 6 to 7x turnover claim as an input. It exceeds the FY31 serviceable pool (B09). The goal moved three times in six months (B05).
- Quarterly or H1 margin alone, year-end receivable days and consolidated EBITDA as stand-alone signals (B04 irrelevant_ratios).
- Low institutional ownership as a risk. Mutual funds hold 15.58% and FPIs 10.48% anyway (B08).
- Sized-never headlines such as the DAC approvals pool and the Rafale supply chain (B05 dropped_triggers).

**C3. The business falsifier.** Evidence that forces re-declaring the FROM business, separate from B6:
- The listed remainder is not growing. FY26 revenue grew 10.67%, but Space and Met supplied 56.3% of the growth, the listed remainder grew about 5.1% and defence sales fell 0.5% (B03). If defence sales fall again in FY27 while Space and Met leave, the starting business is a flat defence supplier, not a growing order-book business.
- The exports and deemed-export line proves to be mostly related-party sales to ARC (B03 inference), with the ARC receivable of Rs 195.79 Cr unaged and ARC capitalised intangibles at 114.7% of its net assets (B02). If so, part of reported growth is a related-party financing loop and the starting business is something other than a spec'd supplier.
- Qualification lock-in proves thin on a named programme. Data Patterns is building a parallel Su-30 radar and says Astra is DcPP partner for the MCA variant, not the Su-30 variant, as it understands (B06 FLAG-PEER-COMPETE).

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE (draft at Halt 1)

Specification: prompts/13-synthesis-pipeline.md, BUSINESS UNDERSTANDING NARRATIVE (five questions, in order). Drafted from B01 to B09. Stage 13 holds the final copy.

Astra Microwave makes the radio frequency hardware that lets Indian radars, electronic warfare kits, military radios and satellites send and sense signals, including transmit and receive modules, radar subsystems, a few complete radars and missile electronics (B04). Defence was 72.5% of FY26 standalone revenue of Rs 1,155.67 Cr, with space electronics at 9.5%, weather and metrology at 4.0%, and exports including deemed exports at 14.0% (B04). The run reads most of the export line as sales to the Astra Rafael Comsys joint venture, which is an inference (B03). The customer cannot drop these parts easily, because each is qualified on a long DRDO or public sector programme, and a new supplier must pass the same tests again (B04, B07 category B2). The customers are almost all the Indian state, at 96.0% of revenue, and three unnamed customers took 52.84% of FY26 revenue (B04, B02, B03). HAL is now the largest single customer through one Uttam radar order of Rs 1,878.8 Cr, which is 47.7% of the Rs 3,937 Cr book (B04). The state pays after delivery, customer tests and inspection, so approvals and inspection slots set the pace of revenue (B05, B06). Present demand comes from indigenisation: the FY27 MoD capital acquisition budget is Rs 185,467 Cr with 75% earmarked for domestic firms, and DAC acceptance of necessity approvals fill the pool of programmes Astra can bid for (B09). The nearest verifiable demand signal is HAL Uttam AAAU Phase 1 deliveries, 12 units by Sep 2027 (B09, B05). Forward growth rests on awards not yet landed: the BEL QRSAM contract with Rs 700 to 800 Cr for the first three regiments, which slipped on three calls, the DRDO development to production milestones for Virupaksha, Angad and the AMCA AAAU, and India defence export value (B05, B09). ISRO and IMD order flow leaves with the demerger from 1 Apr 2027 (B09, B05). Each driver has an outside signal: HAL and BEL exchange filings, PIB releases on DAC approvals and exports, and the Astra Rafael Comsys order book through its rating rationale and MCA filings (B09). The run sizes the serviceable pool at about Rs 4,460 Cr in FY27, growing 10.5% a year, but that pool is management's own programme list, and Astra already holds 24.8% of it, so growth depends on pool growth and award timing more than on share gain (B09). The defence line has the clearest advantage: qualification lock-in on multi-year programmes such as Uttam is documented and scores Moderate in the emerging moat scan (B07). The radio and electronic warfare line has a second documented Moderate advantage through the Rafael partnership, yet the ARC receivable of Rs 195.79 Cr has no stated credit terms (B07 category H2, B02). Policy tailwind scores Moderate on claim evidence only and every Indian peer shares it, while talent asymmetry and the barrier to cannibalisation both score zero (B07 categories R1, I1, I2; B06). Pricing power comes from product mix, not from price, and the run did not establish a separate moat for the space, weather and hydrology lines (B04, B07). The scan totals 16.5 and the Verifier C recount gives 19.2, and both read MODEST (B07, B12c).

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. Verticals framed

**Vertical 1: HAL Uttam AAAU execution and terms.**
- Corpus establishes: order of 122 AAAU and 121 interface frames within 5 years (B05 guidance table); Rs 1,878.8 Cr ex-tax, Rs 2,205.23 Cr with taxes, a gap of 0.53% after the Verifier A correction (B04, B12a); 47.7% of the book (B04); Phase 1 of 12 units by Sep 2027, then about 25 a year (B05); management says PSU production orders carry no advance (B05).
- Cannot establish: order date, margin, advance terms, payment schedule (B03, B04, B05 NOT FOUND); HAL's side of the delivery schedule; DRDO bulk production clearance status.
- Deciding questions: (1) What margin and advance does the contract carry? (2) Is Phase 1 on schedule for Sep 2027? (3) What share of the Rs 3,937 Cr book converts inside 12 to 30 months (B04 mgmt_questions)?

**Vertical 2: Cash conversion and working capital.**
- Corpus establishes: Gate 0 AVERAGE with a cash-conversion deal-breaker (B01); FY26 CFO Rs 387 Cr leaned on a 35.4% working-capital release (B02); H1 FY27 CFO minus Rs 146 Cr, inventory Rs 793 Cr, current borrowings Rs 411 Cr (B04, B05); over-2-year receivables 8,158.33 Rs Lakhs with cover 14.9% (B02); March 2026 lender returns unfiled (B02 finding 6); management volunteered that part of the inventory is legacy stock with obsolescence risk (B12b).
- Cannot establish: management's explanation of the H1 outflow (Q2 call absent); ARC credit terms and ageing; the Rs 16,000.00 Lakhs year-end deposit balance at 30 Jun and 30 Sep 2026; peer H1 cash for Data Patterns (B06 NOT FOUND).
- Deciding questions: (1) Is FY27 year-end CFO positive? (2) Does inventory convert in H2 from Rs 793 Cr? (3) How much of the ARC receivable is past terms?

**Vertical 3: Margin held through mix.**
- Corpus establishes: gross margin 43.87% to 49.18%, EBITDA before other income 25.51% to 28.07% (B03); Q2 FY27 gross margin 55.7% and EBITDA 33.2% (B04); peer margins at or around Astra's level, mix the driver (B06 P5); flat net material cost with no stated reason (B02).
- Cannot establish: why material cost stayed flat; Uttam initial margin; segment margins (B04 NOT FOUND).
- Deciding questions: (1) Does gross margin hold at or above 49.2% in H2? (2) Does Uttam book below the present margin, as management said was possible (B05)? (3) Does the flat material cost reverse?

**Vertical 4: Order book ex-HAL and book-to-bill.**
- Corpus establishes: ex-HAL book Rs 2,058 Cr against Rs 2,141 Cr at Mar-26 (B04 calc); FY27 order inflow guidance Rs 1,600 Cr excluding Uttam (B05); QRSAM slipped on three consecutive calls (B05); Apollo reports a 50:50 BDL and private split of the first QRSAM lot, a cause of delay (B06).
- Cannot establish: BEL contract status; names of the three customers above 10%; reconciliation of deck IMD 18.0% and exports 11.9% with AR 4.0% and 14.0% (B04 FLAG-DATA).
- Deciding questions: (1) Is the BEL QRSAM contract awarded, and do Astra purchase orders follow? (2) Does ex-HAL book-to-bill stay above 1.0? (3) Does the AMCA AAAU contract land (B07 catalysts)?

### 4b. Candidate signal table (8 B09 candidates; UNVERIFIED, verification at Role 5.5 in claude.ai)

Source types follow B09's likely_source entries (Downstream_Source_Discovery_Protocol_v1_0 types as cited there).

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| HAL Uttam AAAU Phase 1 deliveries (12 units by Sep 2027) and the LCA Mk1A 97-aircraft schedule | Phase 1 slips past Sep 2027, or no advance while working-capital borrowings rise (B05 trigger 1) | Event-Driven | HAL exchange announcements and concall (Type 1); PIB; HAL Reg 30 filings |
| BEL QRSAM contract signing and Astra subsystem purchase orders | Further slip past FY27 year end (B05 trigger 3) | Quarterly | BEL exchange announcements, order-book disclosures and concall (Type 1) |
| DRDO development to production milestones (Virupaksha, Angad, AMCA AAAU, SDR) | No AAAU handover update; BEL view that Su-30 stays in development for years (B05 trigger 6) | Event-Driven | PIB (Ministry of Defence); Parliament questions, sansad.in (Type 4) |
| DAC acceptance of necessity approvals | Approvals skew to platforms with no qualified Astra role (draft, needs live check) | Event-Driven | PIB (Ministry of Defence) DAC releases (Type 4/5) |
| MoD capital acquisition budget and in-year capital expenditure | In-year capital spend falls short of the FY27 budget of Rs 185,467 Cr, or the domestic share falls below 75% (B09; draft) | Event-Driven | Union Budget documents; PIB; ICRA and CRISIL industry notes (Type 7) |
| Astra Rafael Comsys order book and revenue (Rs 622 Cr book at Mar-26) | ARC receivable ageing rises, or ARC sales aim held at Rs 360 Cr (B05 trigger 5) | Event-Driven | CRISIL or ICRA rating rationale for the unlisted JV; MCA filings (Type 2) |
| India defence export value and approvals | National export value flat while Astra's deemed-export line rises on ARC sales (draft) | Monthly | PIB defence export releases; DGCI&S tradestat (Type 6) |
| ISRO and IMD order flow for space and met lines (demerging) | Demerger date slips past 1 Apr 2027, or carve-out margin below the stated 18 to 20% PBT (B05 trigger 7) | Event-Driven | ISRO and IMD pages, PIB; Astra Space Technologies Information Memorandum (Type 4) |

### 4c. Fragility read

- variable_count: **7** external variables must go right: (1) Uttam schedule at HAL; (2) Uttam margin and advance terms; (3) BEL QRSAM contract and purchase orders; (4) DRDO development to production conversion for Su-30 and AMCA; (5) MoD capital budget and DAC flow; (6) ARC performance and payment to Astra; (7) customer acceptance and inspection timing behind the H2 FY27 catch-up (B05 analyst_note: H2 needs about Rs 913 Cr against about Rs 745 Cr).
- verifiability_ratio: **5 of 7 externally observable** in principle (variables 1, 3, 4, 5 and 6, through HAL and BEL filings, PIB and the ARC rating rationale). **2 of 7 company-narrated only**: Uttam margin and advance terms, and customer acceptance timing. None of the 7 is verified at Halt 1, because live-web work is pending.
- single_point_failure: **Yes.** Cash conversion on the HAL Uttam order. It is 47.7% of the book, a production order with no stated advance (B04, B05). If FY27 CFO stays negative with inventory above Rs 793 Cr, the proof gate fails on that one variable.
- fragility_verdict: **FRAGILE.** One kill-switch exists, and two of seven variables are company-narrated only. The count of seven is also high.

### 4d. Research brief (claude.ai live-web work order)

1. CHAIN 1 PENDING LIVE VERIFICATION. HAL side of the Uttam order. Open HAL's Reg 30 announcements and investor or annual materials on the Tejas Mk1A delivery schedule and vendor payment practice, and the PIB release on Uttam bulk production clearance.
2. CHAIN 2 PENDING LIVE VERIFICATION. ARC side of the receivable. Open the CRISIL or ICRA rating rationale for Astra Rafael Comsys Private Limited and its MCA filings (financial statements, charges, lender returns).
3. Chain 3 to build: BEL QRSAM contract status, Astra subsystem purchase orders, and the BDL and private 50:50 split reported by Apollo (B06). Open BEL Reg 30 filings and order-book disclosures. Counterparty link: PENDING LIVE VERIFICATION.
4. Chain 4 to build: DRDO development to production conversion for Virupaksha, Angad and the AMCA AAAU (B09 candidate). Open PIB (Ministry of Defence) and Parliament questions. Include the Data Patterns parallel Su-30 radar claim (B06). Counterparty link: PENDING LIVE VERIFICATION.
5. Chain 5 to build: MoD capital budget execution and DAC approvals, in-year capital spend against Rs 185,467 Cr and the 75% domestic share (B09). Open Union Budget documents and PIB. Counterparty link: PENDING LIVE VERIFICATION. An optional sixth chain: ARC export and deemed-export linkage.
6. Retrieve the Q2 FY27 concall transcript (call 2026-11-13) and have Claude Code extract management's explanation of the H1 FY27 CFO outflow, Uttam margin and advance terms, and the ARC FY27 sales aim (freshness pair 1).
7. Retrieve the Reg 30 text of the SEBI inquiry (email 2 Mar 2026, reply 6 Mar 2026) and find the outcome (B08).
8. Identity check of Suresh Kumar Somani in SEBI Order SD/AO/65/2010 against the Astra director, by DIN or PAN (B08).
9. Retrieve the successor MD appointment filing (Oct 2026) and the warrant allotment filing (B00).
10. Track receipt of the Rs 130.50 Cr warrant balance due by 29 Dec 2026 and any forfeiture terms (B03, B08).
11. Retrieve the full demerger scheme text (Appointed Date, liability allocation), the Astra Space Technologies Information Memorandum, the valuer report and fairness opinion, and the NCLT filing (B05, B07; annex question 7).
12. Identify the three customers above 10% of revenue. Reconcile the deck (IMD 18.0%, exports 11.9%) with the AR (Hydro-Met 4.0%, exports including deemed 14.0%) (B04 FLAG-DATA).
13. Fetch proxy-advisor reports (IiAS, SES, InGovern) for the 18 Sep 2026 AGM, including the dissent on the ARC Rs 200 Cr limit (B08).
14. Fetch the 12-quarter promoter holding and pledge series from BSE (B08; annex question 9).
15. Confirm PARAS has no transcripts. Find Data Patterns H1 FY27 operating cash flow (B06).
16. Source checks on market-size inputs: the MarketsandMarkets page (HTTP 403), Credence publication year, the deck market-slide sources, and the rupee rate for November 2026 (B09 stale-data list, FLAG-FX).
17. Test the management claim that the QIP-era order commitment is met, and the redefinition of the order-intake goal from 4 to 5 years (B12b).

### 4e. Second-order stub (Master Prompt v3.7, Rule F)

Evidence tags: [FACT-FILED] filed or official document; [MGMT] management statement; [INFERENCE] reasoning from the cited facts. No new number appears below.

```
CHAIN 1: HAL awarded Astra an order for 122 AAAU and 121 interface frames for the Uttam radar, Rs 1,878.8 Cr ex-tax, within 5 years, Phase 1 of 12 units by Sep 2027 (B05 guidance table, B04)
Link 1 [FACT-FILED]: The order is 47.7% of the Rs 3,937 Cr standalone book. The ex-HAL book is Rs 2,058 Cr against Rs 2,141 Cr at Mar-26 (B04 FLAG-CONC).
Link 2 [PENDING LIVE VERIFICATION]: Who pays, and why now. The payer is HAL. The corpus holds no HAL-side fact. Claude web to open: HAL's Reg 30 announcements and investor or annual materials on the Tejas Mk1A delivery schedule and vendor payment practice, and the PIB release on Uttam bulk production clearance (B09 lists these as the candidate sources).
Link 3 [INFERENCE]: Phase 1 is 12 units by Sep 2027 and the order is 122 units, with about 25 a year after (B05). So most Uttam deliveries fall after Sep 2027. The H2 FY27 revenue step that guidance needs (about Rs 913 Cr against about Rs 745 Cr in H2 FY26, B05 analyst_note) cannot rest on Uttam deliveries. It must come from the ex-HAL book that has already shrunk since March. Production orders carry no advance (B05), so Uttam material outlay may precede Uttam receipts. Whether the H1 FY27 inventory build is early Uttam purchasing is not stated in any document (B05).
Binding constraint: DRDO bulk production clearance (B05 trigger 1 kill signal). The supply chain: management cites stretched cross-border supply chains and minimum order quantities (B05 peer_questions). Working-capital funding: current borrowings Rs 411 Cr against Rs 224 Cr (B04). Capital commitments of 4,445.74 Rs Lakhs against 155.37 a year earlier (B02 finding 15).
Unsaid: No call or filing states the Uttam margin, advance or payment schedule, and the HAL order date is NOT FOUND (B03, B04, B05). The Q1 FY27 call counts the full Rs 4,300 Cr book "in the bag" against an order-intake commitment first framed as new bookings (B12b, order-book goalpost). The capital commitments footnote moves from 155.37 to 4,445.74 Rs Lakhs while the Q4 FY26 call said no additional capex (B02, B05).
Observation that confirms or breaks this chain, and confirm-by date: HAL or Astra filings, or the Q2 FY28 results, show 12 AAAU units delivered, and the Uttam margin and advance terms are disclosed by the Q3 FY27 call (Feb 2027). Breaks if Phase 1 slips past Sep 2027, or no advance with rising working-capital borrowings (B05 trigger 1). Confirm-by: 2027-10-31.
```

```
CHAIN 2: H1 FY27 standalone CFO was minus 14,612.63 Rs Lakhs against plus 23,632.34 in H1 FY26. Inventory is Rs 793 Cr against Rs 609 Cr. Current borrowings are Rs 411 Cr against Rs 224 Cr (B05 FLAG-CASH, B04)
Link 1 [FACT-FILED]: FY26 standalone CFO of 37,595.92 Rs Lakhs included a working-capital release of 35.4%. Payable days were about 72 against 40 (B02 finding 5). A 16,000.00 Rs Lakhs deposit sat inside year-end cash (B02 finding 7).
Link 2 [PENDING LIVE VERIFICATION]: Who pays, and why now. The largest identified related-party receivable is ARC at 19,579.28 Rs Lakhs, 27.9% of current gross receivables, with no ageing or credit terms (B02 finding 1). ARC sales rose 115.8% (B02). The corpus holds no ARC-side evidence. Claude web to open: the CRISIL or ICRA rating rationale for Astra Rafael Comsys Private Limited (B09 candidate), its MCA filings, and the Q2 FY27 concall transcript (call 2026-11-13).
Link 3 [INFERENCE]: The FY26 cash gain drew on one-time levers: collection of old receivables, stretched payables and a year-end deposit. H1 FY27 shows the stretch reversing as inventory builds. So the FY27 CFO sign depends on H2 collections from public sector customers and from ARC, and on a Q4 that carried 42.0% of FY26 revenue (B03). If collections slip, working-capital lines fund the gap.
Binding constraint: Sanctioned limits. Utilisation was 26.1% at year end against a stated aim below 22% (B03 guidance table). March 2026 quarter bank returns were not filed, and the auditor confirms it (B02 finding 6). 88.6% of assets are pledged (B02). The only identified external cash is the Rs 130.50 Cr warrant balance due by 29 Dec 2026 (B03, B08).
Unsaid: Management volunteered that part of reported inventory is legacy stock built over about three decades with obsolescence risk, yet said working capital would improve further (B12b, B05). The overlap between ARC and the three unnamed customers at 52.84% is not disclosed (B02 finding 2).
Observation that confirms or breaks this chain, and confirm-by date: The Q4 FY27 audited results show FY27 standalone CFO above zero, year-end inventory at or below Rs 793 Cr, current borrowings not above Rs 411 Cr, and the ARC receivable at or below 19,579.28 Rs Lakhs with ageing disclosed (B04 must_track_metrics). Breaks if CFO is zero or negative with inventory above Rs 793 Cr. Confirm-by: 2027-05-31.
```

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in claude.ai with live web, before Role 2.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. Astra Microwave builds the electronic parts that let Indian radars, electronic warfare kits, radios and satellites send and receive signals (B04).
2. Defence is 72.5% of FY26 revenue of Rs 1,155.67 Cr. Space is 9.5%, weather 4.0%, exports including deemed exports 14.0% (B04).
3. Most of the export line is probably sales to a joint venture with Rafael, which Astra half owns. This is an inference (B03).
4. Almost all customers are the Indian state, at 96.0% of revenue (B04). Three unnamed customers took 52.84% (B02).
5. One HAL order for the Uttam radar, Rs 1,878.8 Cr, is 47.7% of the Rs 3,937 Cr order book (B04).
6. Demand grows because India wants to procure defence gear from Indian firms. The FY27 capital acquisition budget is Rs 185,467 Cr, and 75% is set aside for domestic firms (B09).
7. The next growth steps are not yet won. They are the BEL QRSAM contract, DRDO programmes such as Virupaksha and Angad, and exports (B09, B05). The QRSAM contract slipped on three calls (B05).
8. Astra's pool of reachable programmes is Rs 4,460 Cr a year, and Astra holds 24.8% of it already. So growth needs the pool to grow and awards to arrive on time (B09).
9. The moat sits in qualification. A part that passed years of tests is hard to swap. This is documented and scores Moderate (B07).
10. The moat does not sit in price power or in talent. Both score zero, and margin comes from product mix (B07, B04).
11. The mental model, as a draft: a spec'd supplier at rung R3 tries to climb to rung R4 by shifting to production orders and complete systems. The proof is a positive FY27 cash flow with margin held at 28.07% or better (the Mental Model Declaration, B01, B03).
12. Fragility is rated FRAGILE. Seven outside things must go right, two of them known only from management, and one order can break the cash test (the fragility read, part 4c).
13. The corpus could not establish the Uttam margin and advance terms, the names of the three big customers, the ARC credit terms, or why the H1 FY27 cash flow was negative. The Q2 FY27 call transcript is missing (B05, B04, B02).
14. Big open question one: is the H1 FY27 outflow of Rs 146 Cr a build ahead of production or the old pattern? FY27 year-end cash flow and inventory will separate the two (B05, B06).
15. Big open question two: do the HAL Uttam Phase 1 deliveries land by Sep 2027, with margin and advance terms disclosed? Governance and the SEBI items add further open points (B05, B08).

---

## SECTION 6: STANDING EXTRACTION ANNEX

Quote-then-comment form. Page anchors are PDF pages (the "[page N]" markers of the .txt twins; the printed folio differs). Quotes keep the source wording. Tab characters and dash glyphs are normalised to spaces and hyphens. Filings and the AR print Rs Lakhs; the call transcripts print INR crores. Quotes of the AR and filings were retrieved from the .txt twins in this run.

### 1. UNITS

No per-unit figure (realisation per unit, price per unit) is printed for any product. The only unit-count disclosure is the HAL order.

- Quote: "procurement of 122 (One Hundred and Twenty-Two) Nos. of AAAU and 121 (One Hundred and Twenty-One) Interface Frames for Uttam Radar for a total consideration of Rs. 2205.23 Crores inclusive of all applicable taxes and GST." (2026-07-30_HAL-orders-jul26_5899cb8f.pdf, p.1; repeated in Annexure A, p.2)
  - Comment: a basket of two products at one total. No per-AAAU value is printed, so none is derived here. The ex-tax value Rs 1,878.8 Cr appears on the deck (Investor_Presentation_1.pdf p.6, "Radar HAL Production 1878.8").
- Quote: "the first Phase 1, the 12 numbers, which we are supposed to complete by September '27 ... thereafter, almost every year on the average of 25 numbers plus, we should execute." (Concall_Aug_2026_Transcript.pdf, p.10)
  - Comment: volume cadence in units for the same basket. Order of 122 AAAU in total.
- Quote: "(All amounts are in Rs. Lakhs, unless otherwise stated)" (2026-11-12_Q2FY27_results_70cb396f.pdf, p.3). The order book note prints crores: "an order book of Rs. 3,937.00 crores" (p.4).
  - Comment: results are in Rs Lakhs and the order book note is in Rs Cr. The unit is on the face of the document.
- Derivation lines available: revenue by order type appears as a pie on the deck (Investor_Presentation_1.pdf p.7), but the text extraction does not tie each percentage to its label, so no split is quoted here; total standalone revenue is "Rs. 1,155 Cr" (p.8). No physical volume line exists for the other products. NOT DISCLOSED: units shipped for radars, EW systems or modules.

### 2. SEGMENT CAPITAL AND DEBT

- Quote: "The Company has only one business segment i.e. it deals in Radio Frequency & Microwave products and hence segment wise reporting is not applicable." (Q2FY27 results p.4, note 2; consolidated, p.10: "The Group and Joint ventures have only one business segment")
  - Comment: no segment assets, segment liabilities or capital employed by business line. NOT DISCLOSED by line. Space, meteorology and hydrology carve-out figures are NOT FOUND (B02, B09).
- Quote (geographic segment assets, standalone, Rs Lakhs): "India 27,794.86 23,526.55 ... Outside India - - Total 27,794.86 23,526.55", defined as "non-current assets other than deferred tax assets and financial assets" (Annual_Report_2026.pdf, p.251, Note 33(b); March 31, 2026 and March 31, 2025). Consolidated total 28,266.20 and 24,006.20 (p.326, Note 34(b)).
  - Comment: the only segment-style capital figure. Not a capital employed measure.
- Borrowings are not allocated by segment. Total borrowings, standalone, Rs Lakhs, at 30 Sep 2026 against 31 Mar 2026: non-current 7,335.48 against 6,321.73; current 41,158.92 against 22,383.62 (Q2FY27 results p.5). Total liabilities 84,475.41 against 67,006.45.
  - Comment: borrowings are unallocated. Current borrowings rose between the two dates.

### 3. GUIDANCE VERSUS ASPIRATION

Classes: (a) guidance with a period; (b) aspiration without a period; (c) capacity or capability only. Call pages are PDF pages. B12a notes that B05's anchors used the printed footer page for about nine entries. The pages below are the PDF pages.

| Class | Quote | Anchor |
|---|---|---|
| (a) FY27 revenue | "top line growth of more than 15% year-on-year, resulting into about INR1,350 crores for this financial year" | Concall_Aug_2026, p.4 |
| (a) FY27 revenue band | "INR1,350 crores for the current year, plus/minus INR25 crores" | Concall_Aug_2026, p.7 |
| (a) FY28 revenue | "Next year, you're looking at about INR1,600 crores plus/minus INR50 crores." | Concall_Aug_2026, p.8 |
| (a) FY27 growth, earlier statements | "reaffirm our FY27 top line growth at 15% to 20% rate"; "planned to book sales of INR1300 crores to INR1400 crores, that is around 15% to 20% growth"; "revenue growth around 15% for FY '27" | Concall_Jun_2026, p.4 and p.6; Concall_Feb_2026, p.5 |
| (a) FY28 revenue, earlier statement | "INR1,650 crores, INR1,700 crores plus/minus" | Concall_Feb_2026, p.8 |
| (a) FY27 order inflow | "at least INR1,600 crores being added this year"; earlier "INR1600 crores plus orders which can be booked in the current year" | Concall_Aug_2026, p.7; Concall_Jun_2026, p.5 |
| (a) Order intake, 3 to 4 years | "Our order intake over the next 3 to 4 years, I think should be in the region of at least INR8,000 crores to INR9,000 crores to be executed over the next 5 to 6 years." | Concall_Aug_2026, p.7 |
| (a) Scale-up, loosely dated | "in the next 5 years or so, we are expecting to do at least 6 to 7x our last year's annual turnover" | Concall_Aug_2026, p.6 |
| (a) Scale-up, earlier statements | "more than double our turnover" (3 to 4 years); "nearly triple its turnover"; "next, down the line three to four years to triple the revenue or maybe you can say up to FY30 to FY31" | Concall_Feb_2026, p.6; Concall_Jun_2026, p.7 and p.14 |
| (a) FY27 EBITDA margin | "the margins are going to be similar to last year. You can expect a delta increase on that -- positive increase in that margins." | Concall_Aug_2026, p.16 |
| (a) ARC FY27 sales | "In the current year, we are planning to book sales of INR360 crores." Earlier: "expected to cross INR600 crores sales" | Concall_Aug_2026, p.4; Concall_Jun_2026, p.6 |
| (a) Space revenue inside FY27 | "close to about INR120 crores to INR150 crores is going to be from the space sector" | Concall_Aug_2026, p.16 |
| (a) Uttam Phase 1 | "the first Phase 1, the 12 numbers, which we are supposed to complete by September '27" and "Before FY '32, we must complete the total order." | Concall_Aug_2026, p.10 |
| (a) Capex, per year | "spending close to about INR40 crores, INR50 crores. So that will continue." | Concall_Jun_2026, p.11 |
| (a) AR: capex FY27 | "a capital expenditure programme of approximately Rs. 75 crore during FY2027" | Annual_Report_2026, p.192 |
| (a) AR: ARC FY27 | "revenues exceeding Rs. 600 crore during FY2027" | Annual_Report_2026, p.190 |
| (a) AR: revenue aim | "to scale revenues from Rs. 1,156 Crore in 2025-26 to more than Rs. 1,600 Crore by 2028-29" (the AR calls it "the aspiration") | Annual_Report_2026, p.30 |
| (b) New spin-off entity | "space and weather should be in the range of INR300-plus crores with at least 18% to 20% PBT margin" ("first year guidance", independent "from April 1, 2027, is our expectation") | Concall_Aug_2026, p.16 to p.17, p.8 |
| (b) Su-30 and ARC pipeline | "at least INR3,000 crores worth of business coming in from Su-30, Virupaksha as well as Angad"; "at least INR500 crores to INR750 crores orders from our Astra Rafael Comsys" | Concall_Aug_2026, p.7 |
| (b) QRSAM | "at least INR700 crores, INR800 crores worth of orders to be added from for QRSAM for the first 3 regiments only" | Concall_Aug_2026, p.7 |
| (b) Funding | "we won't be raising any equity capital for the support of the working capital" | Concall_Feb_2026, p.12 |
| (b) ARC profit share | "at least about INR20 crores plus of will be our share of p rofit for the entire year" | Concall_Jun_2026, p.19 |
| (c) Capability | "Our production lines and our team are fully ready in all aspects for seamless large-scale execution." | Concall_Aug_2026, p.5 |

Comment: the scale-up goal moved from "more than double" in 3 to 4 years (Feb 2026), to "nearly triple" (May 2026), to "6 to 7x" in 5 years (Aug 2026). B09 finds the 6 to 7x claim larger than the whole FY31 serviceable pool (FLAG-MGMT-CLAIMS-INCONSISTENT). The FY27 band of Rs 1,350 Cr is not printed in any document, only on the call (B04 FLAG-GUIDE).

### 4. CONCENTRATION

- Customer (filed): "The revenue from transactions with three external customer exceeds 10% of the total revenue of the company for the year ended March 31, 2026, amounting to Rs. 61,052.05 as against three external customer for the year ended March 31, 2025, amounting to Rs. 54,558.46" (Annual_Report_2026.pdf, p.251, Note 33(c); Rs Lakhs).
  - Comment: 61,052.05 of 1,15,535.00 is 52.84% (B02 calc). Top single-customer share: NOT DISCLOSED. The three names are NOT DISCLOSED.
- Customer (deck, standalone Rs 1,155 Cr): "1 DRDO 28.2% Development + Production; 2 BEL & Other DPSUs 22.7% Production; 3 IMD / Met Dept 18.0%; 5 Exports (via ARC + Aelius) 11.9%" (Investor_Presentation_1.pdf, p.8).
  - Comment: the AR prints different shares for the same lines (Hydro-Met 4.0%, exports including deemed 14.0%). Not reconciled (B04 FLAG-DATA).
- Related party customer: ARC sales "16,009.91" Rs Lakhs (Annual_Report_2026.pdf, p.247, Note 31(iii)), 13.86% of revenue (B02).
- Order concentration: "Radar HAL Production 1878.8" (Investor_Presentation_1.pdf, p.6) against the order book "3,937" (p.5). 47.7% is a calc (B04).
- Product (AR sector table, Rs Lakhs, FY 2025-26): "Defense 83,748 72 ... Space 10,975 10 ... Metrology/Civil Telecom/Others 4,584 4 ... Exports(including deemed exports) 16,228 14 ... Total 1,15,567 100" (Annual_Report_2026.pdf, p.191). Complete systems: "from 12.01% in 2022-23 to 27.8% in 2025-26" (p.26).
  - Comment: the AR prints whole-number shares. Top product line is defence. B04 computes 72.5%.
- Geography: "In India 1,15,319.07 ... Outside India* 215.93 ... *Segment revenue from outside India does not include deemed exports to export oriented units" (Annual_Report_2026.pdf, p.251, Note 33(a), Rs Lakhs). Deemed exports are carved out of the overseas line. Country split: NOT DISCLOSED in the filings (the deck names Israel, Singapore and EU OEMs as export regions, Investor_Presentation_1.pdf p.5).

### 5. PROMISE LEDGER

Status is B05's, adjusted by Verifier B (B12b) where noted. Dates are the call dates. Quotes that also appear in question 3 are repeated only where needed.

| Promise (made on) | Promise as stated | Status | Evidence anchor |
|---|---|---|---|
| FY26 revenue about 10% growth, Rs 1,150 Cr (Q3 FY26 call, 2026-02-13) | "approximately 10% growth in top line"; "INR1,150 crores as a top line" | Delivered | Concall_Feb_2026 p.4; revenue "115,566.75" Rs Lakhs, Q2FY27 results p.3 (year ended March 31, 2026) |
| FY26 order inflow Rs 1,300 to 1,400 Cr (2026-02-13) | "order inflows in the range of INR1,300 crores to INR1,400 crores" | Partial (B05): inflow Rs 1,336 Cr inside the range; a second figure on the same call (book Rs 1,400 to 1,450 Cr) was not met | Concall_Feb_2026 p.4 and p.5; AR p.191 "fresh orders aggregating Rs. 1,336 crore" |
| Q4 FY26 inflow Rs 550 to 600 Cr (2026-02-13) | "close to INR550 crores to INR600 crores" | Partial (B05): about Rs 530 Cr booked; Rs 300 Cr more at negotiation stage | Concall_Feb_2026 p.13; Concall_Jun_2026 p.5 ("approximately INR530 crores", "PNC of INR300 crores") |
| Uttam order from HAL in Q2 or Q3 FY27 (2026-05-27) | "expecting, you know, this particular order sometime in the Q2 or Q3" | Delivered: HAL order 2026-07-30 | Concall_Jun_2026 p.17; HAL filing 2026-07-30 p.1 |
| Man-portable SDR trials end, bids open about March (2026-02-13) | Man-Portable SDR question on the Feb call: "I think trial was over" | OPEN per Verifier B (B05 had it delivered); no later call reports bid opening, L1 or award | Concall_Feb_2026 p.14 and p.16; B12b spot check |
| QRSAM orders; BEL contract by June (2026-02-13, 2026-05-27) | "expecting contract by June or so"; Feb: orders "for the first quarter like QRSAM" | Missed: slipped on three calls; Aug 2026: "partly before this year-end" | Concall_Feb_2026 p.13; Concall_Jun_2026 p.17; Concall_Aug_2026 p.7 |
| FY26 revenue growth 15 to 20% (FY25 AR) | Guidance in the FY25 AR | Missed: delivered 10.67% | B03 guidance table (FY25 AR p.26); B05 |
| ARC FY26 revenue Rs 350+ Cr (2026-02-13) | "INR350-plus crores of top line" | Delivered: ARC sales "INR360 crores" | Concall_Feb_2026 p.12; Concall_Jun_2026 p.6 |
| Board scheme for the demerger within weeks (2026-05-27) | "scheme of demerger once it is formally approved by board, which is expected over the next few weeks" | Delivered: board approval 2026-06-10; exchange observation letters 2026-10-29 | Concall_Jun_2026 p.5; scheme filing 2026-06-10 p.1; observation letters p.12 |
| Maintain operating cash flow trend; working capital improves further (2026-05-27) | "operating cash flow of INR370 crores ... we expect to maintain the trend" | Missed: H1 FY27 standalone CFO minus 14,612.63 Rs Lakhs | Concall_Jun_2026 p.4; Q2FY27 results p.6 (cash flow statement); deck p.12 ("Net Cash from Operating Activities -146") |
| Astra-owned products before Diwali (2026-05-27, 2026-08-11) | "We are very well on track for Diwali, somewhere around Diwali, actually, for at least 2 complete radars of our own and one drone-mounted" | Partial (B05): July 2026 demos held; launch not evidenced in the Q2 FY27 filings | Concall_Aug_2026 p.4 (demos) and p.9 (Diwali remark); deck pp.1-42 show none (B07) |

Tally per B05: 5 delivered, 3 partial, 3 missed. Verifier B reads 4 delivered, 1 open (B12b). Credibility grade B in B05; Verifier B reads B minus (B12b).

### 6. RESTATED BASES

- Quote: "On June 10, 2026, the Board of Directors approved the Scheme of Arrangement between Astra Microwave Products Limited (the 'Demerged Company') and Astra Space Technologies Private Limited (the 'Resulting Company') ... Pending receipt of necessary approvals, no effect of the Scheme has been given in the standalone financial results for the quarter ended September 30, 2026." (Q2FY27 results p.4, note 6)
  - Comment: no restatement for the demerger. The comparatives are as originally filed.
- Comparative as printed in the latest filing (standalone, Rs Lakhs, Q2FY27 results p.3): Revenue from operations "21,295.73" for the quarter ended September 30, 2025 and "41,021.43" for the half year ended September 30, 2025.
- No note on restatement, regrouping or reclassification of prior-period comparatives was found in the three results filings (the only hits are the Ind AS 'items that will be reclassified' OCI headings) or in the FY26 AR text (no hits for regroup, restate or rearrange). B02 records: no restatement of prior-year figures declared. B02 also notes the comparative bases are mixed in the FY25 maturity table (Note 39, p.257), and B03 notes the EBITDA basis differs between FY26 and FY25 (FY26 includes other income, FY25 excludes it; B12a recomputed it exactly).
- Pro-forma: management quotes a base of Rs 1,057 Cr on the Q1 FY27 call against the filed Rs 1,155.67 Cr (B05 FLAG-NUMBERS). B09 notes the base for any post-demerger comparison is the defence plus exports remainder of Rs 1,000.1 Cr, which no filing prints.

### 7. CORPORATE-ACTION CLAUSES

In the corpus: the demerger of the Space, Meteorology and Hydrology business into Astra Space Technologies Private Limited (ASTPL), and the 2025 preferential issue of warrants. No merger, share repurchase or other scheme is in the corpus.

Demerger (scheme text itself NOT in the corpus; the clauses below come from the Reg 30 disclosure):
- Undertaking definition: "The Demerged Undertaking means all the business, undertakings, activities and properties of the Demerged Company pertaining to the Space, Meteorology and Hydrology Business as on the Appointed Date (as defined in the Scheme)." (2026-06-10_scheme-of-arrangement-board-approval_32c8cfe4.pdf, p.3)
- Size of the undertaking: "approximately INR. 157 Crores, representing 13.58% of the total turnover of the Demerged Company" for FY ended 31 March 2026 (same, p.3).
- Ratio: "1 fully paid-up equity share of INR 2 ... for every 1 fully paid-up equity share of INR 2 ... held in the Demerged Company ('Share Entitlement Ratio')"; "There is no cash consideration being discharged under the Scheme." (same, p.5). Post-scheme holding of ASTPL: promoters 6.45%, public 93.55% (same, p.5).
- Liability allocation: NOT DISCLOSED in the corpus. The nearest text is "together with all its assets, liabilities, rights, obligations and employees" (Annual_Report_2026.pdf, p.265, Note 47). The Appointed Date value is also NOT DISCLOSED.
- Dates: Board approval 2026-06-10 (filing p.1). In-principle approval 2026-02-27 (Note 47). Effective date: "The Scheme would become effective after receipt of all requisite approvals" (Q2FY27 results p.4). Exchange observation letters dated October 29, 2026, "The validity of this 'Observation Letter' shall be six months from October 29, 2026, within which the Scheme shall be submitted to NCLT." (2026-10-29_demerger-exchange-observation-letters-oct26_53cae40e.pdf, p.12). Management expectation: "the company shall operate as an independent entity from April 1, 2027, is our expectation" (Concall_Aug_2026, p.8).
- The exchange letter lists items still to be published, including "Value of assets and liabilities of the Demerged Undertaking that is being demerged to the Resulting Company and post-scheme balance sheet of the Resulting Company" (same, p.10).
- Filings to fetch: the Scheme of Arrangement document, the ASTPL Information Memorandum, the registered valuer report and fairness opinion, and the NCLT application (BSE and NSE scheme filings).

Preferential issue of warrants:
- Quote: "approved the allotment of up to 20,13,885 convertible warrants each convertible into, or exchangeable for, one fully paid up equity share of the Company, having a face value of Rs. 2, within the period of eighteen months ... at a price of Rs. 864 aggregating up to Rs. 173.99 crores" (Q2FY27 results p.4, note 1). Board May 20, 2025; shareholders at EGM June 13, 2025.
- Quote: "the Company has received 25% ... i.e., Rs. 43.50 crores (Upfront monies) on June 23, 2025 and June 24, 2025." (same). Allotment: "allotted to six warrant holders ... at its meeting held on 30 June 2025", conversion "on or before 29 December 2026" (Annual_Report_2026, p.180).
  - Comment: the balance of Rs 130.50 Cr (B03, B08 calc) is due by 29 Dec 2026. Allottee names are not in the corpus filings; B08 names them from media (MEDIA REPORTED).

### 8. RELATED-PARTY PERIMETER

The AR's RPT note (Note 31, Annual_Report_2026.pdf, pp.245 to 247, Rs Lakhs) names no promoter-group company as a counterparty. It lists subsidiaries, joint ventures, an associate and key managerial persons. The 6.30% holder Ratnabali Investment (B08) does not appear in the note. Latest year (FY26, year ended March 31, 2026):

| Entity (relationship) | Nature and amount, FY26, Rs Lakhs | Anchor |
|---|---|---|
| Astra Rafael Comsys Private Limited (joint venture, 50%) | Sales of products "16,009.91" (FY25 7,418.75); advance received 406.55; advance adjusted 12.16. Balances: trade receivables "19,579.28" (7,449.97); advance received 871.34; investment in equity 2,000.00; corporate guarantee "8,000.00" | p.246 to p.247 |
| Astra Defence Technologies Private Limited (subsidiary) | Purchase of raw materials / job work "2,130.99"; advance given 100.00; advance adjusted 107.46; sales 1.65; reimbursement 63.85; rent received 31.75. Balances: trade payables 241.95; investment 689.88; corporate guarantee 3,500.00 | p.246 to p.247 |
| Aelius Semiconductors Pte. Ltd. (subsidiary) | Sales 15.60; royalty received 8.62; purchases 255.07. Balances: receivables 19.50; payables 47.99; investment 552.42 | p.246 to p.247 |
| Astra Space Technologies Private Limited (subsidiary) | Balances: investment 10.00; advance for expenses 13.35 | p.246 |
| Navictronics Private Limited (joint venture) | Investment "912.00"; advance given 9.00. Balance: investment 914.00 | p.246 to p.247 |
| Janyu Technologies Private Limited (associate) | Balances: CCPS 53.74; assets held for sale 92.74; advance 21.00 | p.246 |
| Key managerial persons (named: S. Gurunatha Reddy, M. Venkateshwar Reddy, Atim Kabra, T. Anjaneyulu, S. R. Devathi, R. Rungta, B. Mallampati; directors P. A. Chitrakar, A. Chander, V. R. Kumar, A. Mookerjee, S. Varadarajan, K. Dhingra) | Remuneration, for example S. Gurunatha Reddy 339.64, M. Venkateshwar Reddy 338.26, Atim Kabra 130.80, P. A. Chitrakar 28.50 | p.247 |

Comment: Suresh Kumar Somani is listed as a Non-Executive Director (p.245) but has no transaction line. The Notice prints the ARC FY26 transactions as "Rs. 160.09 Crores" (Annual_Report_2026, Notice, near p.86, via B08), and the Board report says no material related party transactions (B08). Subsidiary Astra Private Limited (formerly Astra Foundation) ceased to be a subsidiary on September 16, 2025 (p.245).

### 9. PLEDGE AND SHAREHOLDING

The corpus holds the full pattern for one quarter and category tables for two year ends. The 12-quarter series is NOT DISCLOSED in the corpus. Ten of twelve quarters are missing. Source to fetch: BSE shareholding pattern history, scrip 532493.

| Date | Promoter and promoter group | Pledge | Institutions | Anchor |
|---|---|---|---|---|
| 30 Sep 2026 | 2 holders, 6,205,827 shares, 6.54% (plus 46,296 warrants) | "Whether any shares held by promoters are encumbered under 'Pledge'? No"; NDU No; other encumbrance No | Mutual funds 14,789,976 shares, 15.58%; FPI Category I 7,848,224, 8.27%; FPI Category II 2,099,737, 2.21% (FPI total 10.48% calc). Total shares 94,945,008 | BSE_shareholding_pattern_2026-09-30.txt (filed 2026-10-09; no page markers) |
| 31 Mar 2026 | "PROMOTER 3240830 3.41"; "PROMOTER RELATIVES 2964997 3.12" (6.53% calc) | Not stated in the category table | "INDIAN MUTUAL FUNDS 13251486 13.96"; "FOREIGN PORTFOLIO INVESTOR (CORPORATE) I 6063915 6.39"; "FOREIGN PORTFOLIO INVESTOR (CORPORATE) II 1112813 1.17" | Annual_Report_2026, p.180 |
| 31 Mar 2025 | "PROMOTER 32,40,830 3.41"; "PROMOTER RELATIVES 29,64,997 3.12" (6.53% calc) | Not stated in the category table | MF 11.21%; FPI I 4.86%; FPI II 0.44% | Annual_Report_2025, p.145 to p.146 |

Comment: promoter holding is flat at 6.53 to 6.54% across the three dates and pledge is nil at the one filing held. The institutional share rose from 13.96% (mutual funds) and 7.56% (FPIs) at Mar 2026 to 15.58% and 10.48% at Sep 2026 (B08). Pre-2019 promoter history (12.84%) is MEDIA REPORTED only (B08).

### 10. VERIFICATION

Documents quoted in this annex, with the date of each:

| File | Date |
|---|---|
| inputs/announcements/2026-07-30_HAL-orders-jul26_5899cb8f.pdf | 2026-07-30 |
| inputs/announcements/2026-06-10_scheme-of-arrangement-board-approval_32c8cfe4.pdf | 2026-06-10 |
| inputs/announcements/2026-10-29_demerger-exchange-observation-letters-oct26_53cae40e.pdf | 2026-10-29 |
| inputs/results/2026-11-12_Q2FY27_results_70cb396f.pdf | 2026-11-12 |
| inputs/annual-report/Annual_Report_2026.pdf | filing letter 2026-08-22 (35th AR, year ended 2026-03-31) |
| inputs/annual-report/Annual_Report_2025.pdf | filing letter 2025-08-20 (34th AR, year ended 2025-03-31) |
| inputs/concalls/Concall_Feb_2026_Transcript.pdf | call 2026-02-13 (Q3 FY26) |
| inputs/concalls/Concall_Jun_2026_Transcript.pdf | call 2026-05-27 (Q4 FY26) |
| inputs/concalls/Concall_Aug_2026_Transcript.pdf | call 2026-08-11 (Q1 FY27) |
| inputs/presentation/Investor_Presentation_1.pdf | cover letter 2026-11-12 (Q2 FY27 deck) |
| inputs/shareholding/BSE_shareholding_pattern_2026-09-30.txt | quarter ended 2026-09-30, filed 2026-10-09 |

Material cited by block and not re-quoted: B02, B03, B05, B08 and B12b for the Notice line in question 8, the FY25 AR guidance row in question 5, and the Verifier B spot checks. Where a stage anchor and a PDF page differed, the PDF page above governs (B12a).

CORPUS COMMIT HASH: d9e3931d1ffa0460d8ca74535201c7d801c5d7b8
