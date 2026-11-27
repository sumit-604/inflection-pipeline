# HALT 1 UNDERSTANDING DOSSIER: DEE Development Engineers Ltd (DEEDEV), run 2026-11-15

Stage 09b. Assembly only from committed blocks B00 to B09, B12a to B12d, confidence and B13-lite, plus stage reports for quotes. This is an understanding file only. It carries no decision language. The Mental Model Declaration in Section 2 is a draft and is not signed.

Units line: All figures in Rs crore (Rs cr) unless the source says otherwise. The source unit is on the face of the document. Results filings and the annual report print INR lakhs ("lacs"; 100 lakhs = Rs 1 cr). The prospectus prints INR million (10 million = Rs 1 cr). The unit is stated with each figure. Block cites sit in brackets, for example (B04).

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

Inventory only. Source: B00 (inventory, input_gaps, freshness_pairs, corpus_manifest) and the stage blocks that name documents. Run date 2026-11-15.

### 1.1 Concalls

| Item | File | Document date |
|---|---|---|
| Company call, Q3 FY26 | inputs/concalls/Concall_Feb_2026_Transcript.pdf | call 5 Feb 2026 (B05 report) |
| Company call, Q4 FY26 | inputs/concalls/Concall_May_2026_Transcript.pdf | call 22 May 2026 (B05 report) |
| Company call, Q1 FY27 | inputs/concalls/Concall_Aug_2026_Transcript.pdf | call 6 Aug 2026 (B05 report) |
| Company call, Q2 FY26 | inputs/other/ (preserved, never consumed) | not used (B00) |
| Peer calls, 12 | inputs/peer-concalls/: ANUP 4, ISGEC 4, RATNAMANI 4 | quarters in B06 peer_coverage_map |
| Company call, Q2 FY27 | ABSENT | call set for 17 Nov 2026 (B00) |

Most recent quarter covered by a held transcript: Q1 FY27 (quarter ended 30 Jun 2026, call 6 Aug 2026). A more recent quarter has reported: the Q2 FY27 results were filed 14 Nov 2026 (B00). Its call falls on 17 Nov 2026, two days after the run date, per the BSE intimation 20261111-74e7b622 (B00). No transcript can exist yet. The Q2 FY27 reading in every stage rests on the filing, not on management speech (B05).

### 1.2 Annual reports

| Item | File | Date |
|---|---|---|
| FY2025-26 annual report (352 pp, INR lakhs) | inputs/annual-report/Annual_Report_2026.pdf | year ended 31 Mar 2026; BSE transmittal letter 27 Aug 2026 (B00) |
| FY2024-25 annual report | inputs/other/ (preserved, never consumed; B03 logged it absent, B04 analyst_note records the file) | FY ended 31 Mar 2025 |

The latest completed FY (FY26) is present. Three or more annual reports are not held for use. One is consumed. The FY25 report sits in inputs/other/ and no stage read it, so prior-year guidance and drift over time were untestable (B03, B07). The prospectus (22 Jun 2024) carries restated FY21 to FY23 data that Gate 0 used (B01).

### 1.3 Results filings

| File | Document date |
|---|---|
| inputs/results/Results_Q2FY27_20261114.pdf | 14 Nov 2026 |
| inputs/results/Results_Q1FY27_20260804.pdf | 4 Aug 2026 |
| inputs/results/Results_Q4FY26_20260521.pdf (FY26 audited; 22 of 25 pages are scanned images, text is an OCR layer) | 21 May 2026 |
| Q3 FY26 results | inputs/other/ (preserved, never consumed) |

Quarter gap between the latest results filing (quarter ended 30 Sep 2026) and the latest annual report (year ended 31 Mar 2026): two quarters, Q1 FY27 and Q2 FY27. Both are held.

### 1.4 Investor presentations

Latest held: inputs/presentation/Investor_Presentation_1.pdf, Q1 FY27, 36 slides, filed 5 Aug 2026 (B00). A Q2 FY27 presentation is ABSENT: none was filed on BSE to 14 Nov 2026 (B00).

### 1.5 Research and rating

| Item | File | Date |
|---|---|---|
| CARE full rationale (7 pp) | inputs/rating/CARE_Rationale_20261109.pdf | 9 Nov 2026 |
| CARE rating revision filing | inputs/announcements/20261104-5af20912-a1ab-4f1e-8cbb-b1ac021a5e90.pdf | 4 Nov 2026 |
| Broker or research notes | inputs/research/ is EMPTY | none collected (B00) |

### 1.6 Corporate actions and other held documents

- Announcements: 33 PDFs, 6 Jan 2026 to 14 Nov 2026 (B00). They include board outcomes (6 Jan, 3 Jun, 21 Aug, 14 Nov 2026), the seamless plant start (19 Mar 2026), the PSERC final tariff order for Malwa Power (1 Apr 2026), contract wins (30 May, 2 Jun, 20 Aug 2026), the EGM outcome and the preferential allotment (27 Jun, 8 Jul 2026), the AGM outcome and voting results (24 Sep 2026), monthly execution and order position filings (9 Oct and 13 Nov 2026), the nuclear framework agreement (16 Oct 2026), the call intimation (11 Nov 2026) and the monitoring agency report (14 Nov 2026).
- Two duplicate pairs by first page: 20260106-2c11dce8 with 20260106-8bc396f6, and 20261114-0f6763ea with 20261114-aa9b1cd6 (B00 intake_check). Two files have mostly image pages (AGM outcome 20260924-45f61375, scrutinizer report 20260924-87246f76; low value).
- Prospectus: inputs/prospectus/DEE_Prospectus_June2024.pdf, final prospectus dated 22 Jun 2024, 510 pp, INR million (B00). Listing date 26 Jun 2024.
- Shareholding: inputs/shareholding/shareholding-30Sep2026.txt, NSE XBRL flattened to text, quarter ended 30 Sep 2026, submitted 16 Oct 2026 (B00).
- Screening: four Data_Sheet CSVs (DEEDEV, ANUP, ISGEC, RATNAMANI) (B00).

### 1.7 Freshness pair check (B00 freshness_verdict and freshness_pairs)

| Pair | Trigger document held | Mate | Status |
|---|---|---|---|
| Results to concall | inputs/results/Results_Q2FY27_20261114.pdf | Q2 FY27 earnings call transcript | FAILED. Mate absent. Call on 17 Nov 2026. Expected source: BSE/NSE filing or the screener Concalls list, a few days after the call (B00) |
| Rating bulletin to rationale | CARE_Rationale_20261109.pdf | full CARE rationale | PASS. The file is the full 7-page rationale (B00) |
| SEBI order to order text | none found | none | PASS. No SEBI order reference in the FY26 AR text; re-checked after stages 3 and 8 (B00) |
| AR to latest audited annual results | Results_Q4FY26_20260521.pdf (FY26 audited) | FY2025-26 annual report | PASS (B00) |

Failed pair, by name: the trigger is the Q2 FY27 results filing of 14 Nov 2026. The missing mate is the Q2 FY27 earnings call transcript. This failure caps the phase 1 gate recommendation (B13-lite caps), so the line below is never softened.

### 1.8 Gaps carried from B00.input_gaps (full list)

1. COLLECTOR: shareholding/ was empty (no automated source). Closed at /step1: the NSE XBRL pattern for 30 Sep 2026 was fetched (B00).
2. COLLECTOR: the screener export sheets came out empty (formulas with no cached values): Profit & Loss, Quarters, Balance Sheet, Cash Flow, Customization for DEEDEV, ANUP, ISGEC and RATNAMANI. OPEN. Fix: open Financials.xlsx once, save, run --push-again. Data_Sheet CSVs are populated and carry the same raw series. DEEDEV and ANUP "Adjusted Equity Shares in Cr" is blank; the DEEDEV market-quote row and ANUP Borrowings are partly filled (B00).
3. COLLECTOR: no results PDFs. Closed at /step1 (three results filings fetched from BSE) (B00).
4. COLLECTOR: no rating PDF. Closed at /step1 (CARE rationale from careratings.com) (B00).
5. REPAIRED at /step1: three results filings, 18 further Reg 30 filings, the CARE rationale, the prospectus (SEBI) and the shareholding pattern (NSE XBRL) (B00).
6. CONCALL (freshness failure): the Q2 FY27 concall transcript is ABSENT. Call on 17 Nov 2026, after the run date (B00).
7. PRESENTATION: no Q2 FY27 investor presentation filed on BSE to 14 Nov 2026. The latest is Q1 FY27, filed 5 Aug 2026 (B00).
8. SCREENING: Data_Sheet CSVs are populated; the P&L, Quarters, Balance Sheet and Cash Flow sheets are absent (see item 2) (B00).
9. SHAREHOLDING: the corpus copy is the NSE XBRL as text, not a PDF (B00).
10. RESEARCH: empty. No broker notes collected (B00).
11. OCR TEXT LAYER: Results_Q4FY26_20260521.pdf has 22 of 25 pages as scanned images; the .txt is Tesseract OCR. Load-bearing figures are checked on the PDF page (B00).
12. IMAGE PAGES: announcements 20260924-45f61375 (AGM) and 20260924-87246f76 (scrutinizer report) are mostly image pages and not OCR-repaired (B00).
13. EMPTY-FOLDER CONFIRMATION was suppressed under /step1 (standing answer: continue with the gaps). Empty folder: research (B00).
14. TEXT ROUTE: every inputs/ PDF has a page-marked .txt twin ([page N] markers). Stages read the .txt and open the PDF page where the text is garbled (B00).

Further gaps named by the stage blocks:
- Tonnes shipped, revenue per tonne, order book by customer, market share and competitor financials: not found in the AR, deck or calls (B04).
- Top-10 customers about 80% of FY26 income: found in CARE p.2 only, not in the AR (B04, B03).
- Management net debt definition and company working-capital day-count basis: not found (B05).
- Promoter pledge for quarters between Jun 2024 and Jun 2026: not in the corpus (B08).
- Covenant headroom, Thailand DCF inputs, nature of the Rs 7.63 cr (762.90 lacs) payable to Shikha Bansal, Abohar billing since 1 Apr 2025: not found (B02, B03, B08).
- Peer piping-only revenue, product-fit and capability share of the market, HRSG market size, current thermal GW under construction, USD/INR rate: not found (B09).
- R&D spend; capex for FY20 and FY24; payables FY20 and FY24; current liabilities FY20 to FY24: not found (B01).

### 1.9 Verdict line

Missing document first: the Q2 FY27 earnings call transcript (findable-missing after 17 Nov 2026; expected source BSE/NSE filing or the screener Concalls list; freshness-pair failure). Other gaps list under it: Q2 FY27 investor presentation (BSE or company IR page; findable-missing once filed), broker research (none collected; operator upload), screener export sheets (findable-missing; re-save and push), intermediate-quarter shareholding patterns Jun 2024 to Jun 2026 (BSE/NSE; findable-missing). Plausibly nonexistent items, which are themselves a data point on disclosure: tonnes shipped and revenue per tonne, and order book by customer, which no filed source carries (B04).

VERDICT LINE: CORPUS GAPPED-FRESHNESS

---

## SECTION 2: MENTAL MODEL DECLARATION

DRAFT - PENDING OPERATOR SIGN-OFF

This declaration is not signed. Signing happens only in claude.ai after live-web stress tests. Archetype and ladder terms come from CLAUDE.md.

### PART A: THE FROM STATE

**A1. Archetype, per line**

| Line | Share of FY26 revenue | Archetype (FROM anchor) |
|---|---|---|
| Piping division (made-to-order spools, bends, fittings, skids; includes job work 16.4% of standalone revenue) | 87.7% (B04) | Build-to-spec component maker. It carries order-book traits: order book of Rs 2,531.04 cr at 30 Sep 2026 against FY26 revenue of Rs 1,142 cr (B04, B09), about 2.1x revenue (B04) |
| Biomass power (Abohar, Muktsar; pellets from Q1 FY27) | 4.9% (B04) | Licence/scarcity business: a regulated tariff under a purchase agreement, with renewal and tariff-order risk (B02, B04) |
| Heavy fabrication (wind towers, stacks; subsidiary DFIPL) | 7.0% (B04) | Build-to-spec component maker; no separate transition claim |

The archetype is not a commodity converter. The Amendment 17 converter test is not triggered by this archetype in any block. The cap row ("Cables / Industrial products", 25x) is a loose fit that the operator rules at the /fttcp gate (B00 sector_cap_evidence, B04 sector-cap-fit item).

**A2. The simple analogy**

DEE is a custom plumbing workshop for power stations and refineries. A boiler maker or an engineering contractor sends a drawing. DEE cuts, bends and welds steel pipe to that drawing, tests it, and ships the finished pipe sections for the customer to install. The customer fixes the rate when the order is signed and allows no extra for steel cost swings. DEE therefore purchases about half of the order value in steel as soon as it wins the job (B04). The customer pays in stages, so cash comes back slowly. The workshop has just built more floor space and its own pipe-making machine, and it is not yet full. Today the workshop is busy with a large order book. The open question is whether a fuller workshop turns that book into profit and cash.

### PART B: THE TRANSITION

**B1. FROM to TO (piping line; the only line with a transition claim)**

- FROM: R2 COST-ADVANTAGED CONVERTER, with a qualification. Margin comes from procurement and overhead leverage, not from pricing power (B04 one_line_verdict, B03). Return on capital sits below the mid-teens R2 neighbourhood: spot 10.1% (B04), median 7.65% on the proxy basis over FY20 to FY26 (B01), and 14.9% for FY26 on the strict basis (B01 data_notes). The line therefore sits between R1 and R2 on durability of ROCE. This is a finding, not a gap to paper over.
- TO: R3 VALUE-ADDED / SPEC'D SUPPLIER. This is a one-rung climb, inside the base rate of one rung per 2 to 3 years. Management's own words place the climb on seamless backward integration and HRSG/GT qualification (B05 triggers 3, 5). The ladder footprint for R3 is ROCE of 20 to 25% with stickiness. The run has no evidence of any multi-rung leap.

**B2. The engine (what physically changes)**

1. Utilisation of capacity already built. Anjar is at about 50% now, with statements of 60-65% in FY27 and 70-100% for FY28 (B05 trigger 6; B07 Anjar utilisation item). Fixed overhead per rupee of revenue falls as the plant fills. FY26 EBITDA rose on overhead leverage: employee cost fell from 19.5% to 16.4% of revenue while gross margin fell from 65.0% to 58.1% (B04 gross-margin-mix item). The ugly optic is the falling gross margin, which came with material-supplied power jobs.
2. Backward integration and qualification. The 7,000 MTPA seamless plant began commercial production on 19 Mar 2026 at a cost of Rs 89.74 cr (B07 capex_for_stage9). The Thailand HRSG capacity reservation starts 1 Jun 2027 at a minimum of US$15.27 m a year (B07 analyst_note). Management expects about 20% EBITDA on seamless (B05 1B). These are the two active emerging-moat categories, B1 and B2 (B07).

**B3. The proof gate (binary, quarter by quarter)**

All three legs hold in the same period, tested on the Q3 FY27 results (Feb 2027) and the FY27 results (May 2027):
- Margin leg: consolidated operating EBITDA margin at or above 19% for H2 FY27, with gross profit in rupees rising (B05 trigger 1; B04 must_track_metrics).
- Cash leg: H2 FY27 consolidated operating cash flow positive, with CFO/EBITDA at or above 0.5 (FY26 was 0.10) (B04 must_track_metrics; B03 monitorables).
- Cycle leg: the FY27 operating cycle printed at or below 220 days (FY26 was 261; Q1 FY27 was 263) (B13-lite; gate recommendation, cash section, falsifying observation).

State at the run date: the margin leg has one quarter in the guided zone (Q2 FY27 operating margin 20.1%, derived; H1 18.5%, derived) (B05). The cash leg has not moved: H1 FY27 operating cash flow was Rs -6.79 cr (-679.09 lacs) on PBT of Rs 49.92 cr (B01, B03). The gate has not fired. Until it fires, the transition is narrative and the name is research, not a trade (B13-lite transition_posture).

**B4. The recognition gap (open question for Stage 11)**

Open question: does the TO state, a one-rung climb to R3, already appear reflected in market pricing? This dossier states no number and draws no conclusion. Stage 11 resolves it by comparing the current PE with the PE gap that the TO rung implies. If the TO state is already priced, the re-rating engine is gone and only earnings growth remains.

**B5. The ugliness test**

Classification: UNRESOLVED between ARTIFACT-OF-CLIMB and STRUCTURAL-FEATURE. The blocks do not settle it (B13-lite cash_determination INDETERMINATE). The evidence on each side:
- ARTIFACT-OF-CLIMB: order book rose from Rs 1,228.17 cr (31 Mar 2025) to Rs 2,531.04 cr (30 Sep 2026); inventory days fell from 227 to 174; two plants started inside twelve months; CARE expects 50 to 60 days off the cycle in FY27 as faster power orders execute (B04; gate recommendation, cash section, reading A).
- STRUCTURAL-FEATURE: about 50% of order value is bought in steel at order receipt under fixed-rate contracts with no escalation clause (CARE p.2 via B04); creditor days fell from 122 to 66 to 34; debtor days rose from 99 to 123; the Q1 FY27 cycle of 263 days is only 13 days shorter than a year earlier; peers run about 120 to 165 days (B05 row 11, B06). Verifier D adds one peer, ANUP, that ran 190 to 200 days in the stressed FY26 with management aiming at 120 (B12d).
- Separating observation: H2 FY27 operating cash flow, read with a disclosed Anjar utilisation above 60% (B07 analyst_note; B13-lite).
- Transition posture is not assigned. Candidate cells are RESEARCH / WATCH (ARTIFACT) or VALUE-TRAP RISK (STRUCTURAL) (B13-lite transition_posture).

**B6. The transition falsifier (kills the arrow)**

Any one of these ends the climb thesis:
- Q3 FY27 consolidated revenue at or below Q2's Rs 292.99 cr, leaving about Rs 620 cr (derived) for Q4 against the Rs 1,500 cr guide (B13-lite falsification_metric).
- H2 FY27 revenue under Rs 800 cr, or H2 margin below 18% (B05 trigger 1 kill_signal).
- H2 FY27 operating cash flow negative while the order book still rises; new term loans in the cash flow statement (B05 trigger 4; gate recommendation, cash section).
- Anjar utilisation near 50% through FY27 (B05 trigger 6 kill_signal).
- No GE purchase order for 15 to 16 HRSG units by Q4 FY27 (B05 trigger 3 kill_signal).

### PART C: WHAT THE MODEL WATCHES

**C1. Dominant variables (become Role 5.5 tracker signals)**

1. Order conversion to revenue at the guided margin. State: H1 FY27 Rs 587.45 cr; H2 needs Rs 912.55 cr, +55.3% (B01); Q2 Rs 292.99 cr below Q1 Rs 294.46 cr (B05); October executed Rs 93.02 cr against Rs 152.1 cr a month needed (B09 guidance item).
2. Cash conversion and the working-capital cycle. State: FY26 consolidated CFO Rs 19.55 cr against EBITDA Rs 191.21 cr (B03); H1 FY27 CFO Rs -6.79 cr (B01); receivables +68.9% against revenue +43.8%, with Rs 159.39 cr (15,938.75 lacs) sold without recourse (B02).
3. Utilisation of Anjar and the seamless plant. State: Anjar about 50% now, three differing statements (B07); seamless external orders in the Rs 58 cr and Rs 68 cr class (B07); FY27 capex Rs 20-30 cr guide against about Rs 150 cr in CARE and Rs 58.02 cr spent in H1 (B07 capex gap).
4. The thermal and HRSG order pipeline. State: power is 64.9% of the 31 Oct 2026 order book (B09 power-mix item); BHEL slower than expected; GE HRSG order for 15-16 units not issued (B05); the Thailand reservation starts 1 Jun 2027 (B07).

**C2. What the model rejects**

- The market-size debate between the D&B figure (Rs 25,400 cr, FY23) and the Grand View Research figure, about ten times smaller. The binding constraint is capacity and cash, not market room: installed plus committed capacity supports about Rs 1,302-1,470 cr at FY26 asset turns against a Rs 2,500 cr FY30 plan (B09 analyst_note, capacity item).
- The sizing of nuclear, data-centre, green-hydrogen and Middle East options. These are options, not orders (B07 optionality_register). Management itself excludes Middle East reconstruction from its projections (B05 T10).
- The biomass power segment as a value driver. It is 4.9% of revenue and loss-making (B04). It matters as a risk item only, through the Malwa and Abohar disputes.
- Peer market-share comparisons in piping. No peer is a listed pure-play, and the run found no piping-only peer revenue (B06, B09).

**C3. The business falsifier (forces re-declaration of the FROM business)**

Evidence that DEE is not a build-to-spec fabricator with a real order book of its own work:
- The order book proves to be reserved capacity and letters of intent instead of orders. About Rs 380 cr, about 15.6% of the Rs 2,428 cr June book (Verifier B arithmetic), is a GE letter of intent with no inputs, and the Thailand "booked for three years" claim sits beside a Thailand book of about Rs 200 cr against Rs 170-200 cr a year (B12b-01, B12b-04).
- Revenue shifts toward pass-through trading in which the material is 95 to 100% of the order value, so the line becomes a reseller of steel. Management cited such trading to explain the Q4 FY26 gross-margin dip (B12b-20).
- A third qualified audit opinion on a group entity, or a court order that forces the biomass segment liabilities onto the parent, would re-open the group perimeter (B05 trigger 7 kill_signal; B02 top findings 1 and 2).

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

Draft at Halt 1 from B01 to B09, per the five-question spec in prompts/13-synthesis-pipeline.md. Stage 13's copy stays the final version.

DEE makes pipe systems to each customer's drawing in its own plants in India and Thailand (B04). The piping division gave 87.7% of FY26 revenue, which was Rs 1,142 cr (B04, B09). The parts are spools, bends, fittings and skids that carry high-pressure steam and process fluid inside power plants and refineries (B04). A customer cannot switch to an unapproved fabricator, because NTPC, NPCIL, ASME and PED vendor approvals take time to earn and need renewal and audits (B04). Since 19 Mar 2026 a 7,000 MTPA plant also makes thick-wall seamless pipe, which the deck calls 100% import-dependent in India (B07, B09). Heavy fabrication (7.0%) makes wind towers and stacks. Biomass power (4.9%) supplies power under a regulated tariff and recorded a segment loss of Rs 10.83 cr (1,083.14 lacs) in FY26 (B04, B03). The customers are boiler and turbine makers and engineering contractors such as BHEL, L&T, JSW, Nooter Eriksen, Siemens and GE, and project owners such as Numaligarh Refinery and Dow Chemical Canada (B05, B09). These customers tender each project at a fixed rate with no escalation clause and pay on milestones, so DEE purchases about half of each order's value in steel when it wins the order (B04). The top ten customers gave about 80% of FY26 income, up from 59%, and Numaligarh and Dow gave 15.12% and 9.67% of consolidated revenue (B04, B09). Demand exists today because power plants are in build: power is 64.9% of the 31 Oct 2026 order book, tied to the BHEL thermal boiler and pressure-part tender awards and the CEA thermal project monitoring candidates, with refinery and chemical work tied to the Numaligarh Refinery and Dow candidates (B09). Demand should grow with the 80 GW thermal plan to FY32, refining capacity rising from 258 to about 310 MMTPA by 2030, a GE Vernova HRSG purchase order for 15 to 16 units, Siemens Energy gas turbine backlog, and NPCIL/DAE fleet-mode awards, where the 16 Oct 2026 framework is an option and not an order (B09). The run did not establish when BHEL will award, or the order book by customer (B04). The competitive advantage sits in the piping line only. It is a narrow moat of vendor approvals and port-side scale at Anjar, and scale helps only at high utilisation (B04). The emerging moat scan scored 10.1 (NONE) on the stage path and 12.1 to 12.8 (MODEST) on the Verifier C path, with only seamless integration (B1) and HRSG qualification lock-in (B2) active (B07, B12c F-EM-1). Talent asymmetry and the cannibalisation barrier (categories 21 and 22) scored zero, because a rival gives up nothing to copy DEE (07-emoat.md, Family I). Heavy fabrication and biomass power have no moat in the blocks (B04, B07).

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. Verticals framed

**Vertical 1: Order conversion to revenue at the guided margin**
- The corpus establishes: H1 FY27 revenue Rs 587.45 cr and an H2 need of Rs 912.55 cr (+55.3%) for Rs 1,500 cr (B01); Q2 Rs 292.99 cr below Q1 Rs 294.46 cr despite a stated Rs 25 cr deferral (B05); order book Rs 2,531.04 cr at 30 Sep 2026 (B04) and Rs 2,586.43 cr at 31 Oct 2026 (B05 report, corrected); October executed Rs 93.02 cr against Rs 152.1 cr a month needed (B09). Q2 operating margin 20.1% and H1 18.5%, both derived (B05). Capacity supports about Rs 1,302-1,470 cr at FY26 asset turns (B09). Peers report cost rises on fixed-rate orders and ANUP cut its FY27 EBITDA guide to about 15%, while DEE's May and August calls never mention input inflation (B12b-05).
- It cannot establish: the order book by customer and by execution quarter; the reason Q2 revenue sits below Q1; tonnes shipped; the power division's Q2 revenue fall from 1,836.76 to 463.57 lacs (B04).
- Deciding questions: (1) Which orders, by customer and quarter, support Rs 913 cr in H2? (2) What are H2 gross profit in rupees and H2 margin against the 18% kill line and the 19% guide? (3) Did the Rs 25 cr of deferred dispatches ship in Q2, or later?

**Vertical 2: Cash conversion and the working-capital cycle**
- The corpus establishes: FY26 consolidated CFO Rs 19.55 cr against PAT Rs 77.17 cr and EBITDA Rs 191.21 cr (B03); standalone CFO Rs -44.50 cr (FY25 Rs -154.29 cr) (B02); FY25 plus FY26 screener CFO Rs -98.91 cr on PAT Rs 120.80 cr (B01); H1 FY27 CFO Rs -6.79 cr (B01); receivables +68.9% with Rs 159.39 cr sold and an over-six-month share of 9.2% against 5.3%, and a nil loss allowance (B02); operating cycle 263 days in Q1 FY27 (B04); promise of positive H1 cash missed (B05). The Rs 300 cr equity issue repaid Rs 225 cr of short-term debt (B05 row 21).
- It cannot establish: movement in customer advances over H1; recourse terms on the Rs 159.39 cr sold; covenant headroom; the company's own day-count basis (B02, B05, gate recommendation).
- Deciding questions: (1) Does H2 FY27 operating cash flow turn positive while the order book still rises? (2) Did customer advances build in H1? (3) What is the recourse and discounting cost on sold receivables, and does the FY27 Ind AS 1 covenant rule change borrowing classification?

**Vertical 3: Utilisation of Anjar and the seamless plant**
- The corpus establishes: Anjar reached 30,000 MTPA in Sep 2025, on time; the seamless plant started 19 Mar 2026, about 2.5 months late (B03); Anjar utilisation about 50% now, with three statements (almost optimal in FY27; 60-65% in FY27 and about 100% by end of next year; 70-75% next year) (B07, B12b-16); seamless external orders in the Rs 58 cr and Rs 68 cr class (B07); capex FY27 guide Rs 20-30 cr, CARE about Rs 150 cr, H1 actual Rs 58.02 cr, CWIP Rs 87.48 cr (B07).
- It cannot establish: utilisation by plant as a filed figure, tonnes, or the cost of the Anjar expansion, pellet plant and nuclear/HRSG capacity (B07 not_found).
- Deciding questions: (1) What Anjar utilisation does the Q3 FY27 filing or call state? (2) Do named seamless orders beyond the Rs 58 cr and Rs 68 cr class appear? (3) Which capex number is right for FY27?

**Vertical 4: The thermal and HRSG order pipeline**
- The corpus establishes: power is 64.9% of the order book (B09); BHEL "slightly slower than our expectation", with about Rs 200 cr ordered in Q1 FY27 (B05 row 17); GE HRSG order for 15-16 units not issued; Siemens understanding recorded only as a minute of meeting with no confirming filing (B05, B12b-12); the Thailand reservation starts 1 Jun 2027 (B07); ISGEC lost two orders worth about Rs 550 cr in FY26 (B06); Rajasthan cancelled 3.2 GW (B07). Peers confirm direction of thermal demand but give no BHEL award pace (B06).
- It cannot establish: BHEL award timing; whether the GE line is an order or reserved capacity; the Thailand order book against the "booked for three years" statement (B12b-01).
- Deciding questions: (1) Does a GE purchase order for 15-16 units appear by Q4 FY27? (2) Do the BHEL tenders (about Rs 210 cr at L1) convert to awards? (3) Does the Thailand line in the next order-position filing support the three-year claim?

### 4b. Candidate signal table (all UNVERIFIED; verification and tracker writes happen at Role 5.5 in claude.ai)

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| BHEL thermal boiler and pressure-part tender awards (about Rs 210 cr L1) (B09) | BHEL awards slip past FY27, or thermal cancellations broaden (B05 T1 kill_signal) | Event-Driven | BHEL Reg 30 order disclosures and tender results on BSE/NSE (Protocol Type 1) |
| CEA thermal project monitoring: GW under construction and commissioned (B09) | Commissioned additions fall short of the plan for two consecutive progress reports; B09 records a FY25 miss of 4.53 GW against 15.4 GW from a search summary | Quarterly | CEA thermal project progress reports, Ministry of Power (Protocol Types 5 and 7) |
| GE Vernova HRSG purchase order for 15-16 units and gas turbine backlog (B09) | No purchase order by Q4 FY27; reservation lapses (B05 T3 kill_signal) | Quarterly | GE Vernova quarterly results and filings (Protocol Type 3, SEC EDGAR); DEE Reg 30 |
| Siemens Energy gas turbine backlog and Anjar vendor clearance (B09) | Anjar clearance not granted, or no first piping order within 6-12 months (B07 catalysts) | Quarterly | Siemens Energy quarterly reports (Protocol Type 3); DEE Reg 30 |
| Numaligarh Refinery and other refinery expansion capex (15.12% of FY26 revenue) (B09) | No new package from the refinery to DEE, so the 15.12% share cannot repeat (B03: repeatability unproven) | Quarterly | Refinery annual reports and board capex approvals; PPAC capacity data (Protocol Types 1 and 7) |
| Dow and chemical-sector capex announcements (9.67% of FY26 revenue) (B09) | Dow capex deferred, or no repeat order after the move from 0.12% to 12.03% of standalone revenue (B03) | Quarterly | Dow Inc. quarterly results (Protocol Type 3, SEC EDGAR); Indian chemical company capex filings |
| NPCIL / DAE nuclear fleet-mode PHWR awards and the 16 Oct 2026 framework agreement (B09) | No order or board-approved facility by FY28 (B05 T8 kill_signal) | Event-Driven | NPCIL and DAE releases, PIB, DEE Reg 30 (Protocol Types 4 and 5) |

### 4c. Fragility read

- variable_count: 7. The external variables that must go right for the climb: (1) BHEL and L&T thermal award pace; (2) GE HRSG order and Siemens clearance; (3) repeat orders from project customers such as Numaligarh and Dow; (4) steel and freight cost on fixed-rate orders; (5) customer payment behaviour on milestone and retention terms; (6) Anjar and seamless utilisation; (7) Malwa APTEL and Abohar High Court outcomes (B05, B09, B06, B02).
- verifiability_ratio: 4 of 7 externally observable. Observable: BHEL awards, project-customer capex, input costs seen in peer filings, court and regulator orders. Company-narrated only: the GE and Siemens reservations until a DEE filing appears, customer payment behaviour until the quarterly balance sheet, and utilisation, which is never a filed figure (B07, B09).
- single_point_failure: cash conversion (variable 5). If H2 FY27 operating cash flow stays negative while the order book rises, the cash determination moves to STRUCTURAL and the proof gate fails on its cash leg alone (gate recommendation, cash section, falsifying observation; B13-lite).
- fragility_verdict: FRAGILE. Seven variables, three company-narrated, and one kill-switch, under the definitions in the stage instruction.

### 4d. Research brief (claude.ai work order; items 1 and 2 carry the PENDING LIVE VERIFICATION links of the 4e chains)

1. PENDING LIVE VERIFICATION (Chain 1, Link 2). Customer payment behaviour. Open the BHEL FY26 annual report and its Q2 FY27 results (trade payables ageing, supplier payment terms, MSME payables), the L&T FY26 annual report (trade payables note), and the latest Numaligarh Refinery annual report (trade payables and supplier payment note). Read how long these customers hold supplier money. These are counterparty facts the corpus does not hold.
2. PENDING LIVE VERIFICATION (Chain 2, Link 2). Who orders and why now. Open the BHEL Reg 30 order and tender-award disclosures since Aug 2026 and its latest results call on boiler order inflow; the GE Vernova latest quarterly release and filing for gas power backlog and HRSG slot reservations; the Siemens Energy latest quarterly report on gas turbine backlog; and the CEA Apr-Jun 2026 thermal progress report that stage 9 skipped.
3. Build Chain 3: Anjar and seamless utilisation to fixed-overhead leverage to margin (B04 key_lever; B05 T3, T4).
4. Build Chain 4: input cost on fixed-rate orders. Peers report war-driven cost rises and a cut in ANUP's FY27 EBITDA guide; DEE's calls are silent (B12b-05).
5. Build Chain 5: customer concentration and repeat orders from Numaligarh and Dow (B03, B09).
6. Chains 6 and 7 if time allows: nuclear framework conversion (B07 optionality register); Malwa and Abohar legal outcomes and their cash cost (B02).
7. Capture the Q2 FY27 call (17 Nov 2026) and Q2 deck when filed. Questions from B05 analyst_note: the Rs 25 cr deferral, working-capital days, Rs 47.71 cr against Rs 80 cr non-core revenue, the Malwa impairment, and the Rs 21 cr gap between the two FY27 inflow columns in the 13 Nov 2026 order filing.
8. Promoter and legal registries (B08 searches_skipped): sebi.gov.in enforcement and settlement orders by entity name; MCA21 master data and charge register for Malwa Power, DEE Fabricom, DDE Piping Components and Uprise Trade Solutions LLP; IiAS, SES and InGovern view on the 2026 AGM.
9. Policy status (B09 searches_skipped): current thermal GW under construction from CEA; the 83.5 GW article that returned HTTP 403; HRSG and engineered-spool market size for India and export.
10. Scope and FX (B09): a USD/INR source for the Grand View Research conversion; piping-only revenue of named peers, which separates the D&B and GVR readings of market size.
11. Source URL verification for every web-sourced item in B08 and B09 that Verifier A did not check: Grand View Research page, GE Vernova and Siemens backlog figures, the 80-83.5 GW thermal plan figures, media items, AmbitionBox and Trendlyne (B12a coverage_note).
12. Pledge history: quarterly shareholding patterns for Jun 2024 to Jun 2026 from BSE/NSE, to complete the twelve-quarter series (B08).
13. Court and regulator status: Malwa Power APTEL appeal and PSERC; Abohar High Court case, including the stay date conflict between 23 Sep and 23 Oct 2025 (B05 red items; B02).
14. Forum archaeology: the background of the new CFO from 7 Jan 2026 (B08: not found); employee reviews beyond AmbitionBox (B08); the status of the Shikha Bansal income tax appeal at CIT(A) or ITAT and of the ED FEMA information order (B08).
15. NPCIL approval status: RATNAMANI says its plant is the only nuclear-approved facility from India for NPCIL; DEE says "advanced stage of discussions". Check the NPCIL vendor list (B12b-06).
16. Thailand booking: the 21 May 2026 Reg 30 reservation filing, Nooter Eriksen disclosures, and the Thailand line in the next order-position filing against the "booked for three years" statement (B12b-01).

### 4e. Second-order stub (Master Prompt v3.7, Rule F)

Two chains off the two dominant variables the evidence base can carry: cash conversion (variable 2) and order conversion with the thermal and HRSG pipeline (variables 1 and 4). Facts carry block cites. Inference is labelled.

```
CHAIN 1: H1 FY27 consolidated operating cash flow was Rs -6.79 cr on PBT of Rs 49.92 cr, while the order book stood at Rs 2,531.04 cr (B01, B04)
Link 1 [DOC]: Contracts are fixed-rate with no escalation clause, and about 50% of order value is bought as steel on receipt of the order (CARE p.2, via B04). Creditor days fell from 122 to 66 to 34. Debtor days rose from 99 to 123. Inventory days fell from 243 to 174. The cycle moved from 276 to 263 days (B05 row 11, B04).
Link 2 [PENDING LIVE VERIFICATION]: Who pays, and why now. Eight customers hold about 71% of standalone receivables, up from 33% (B02 rank 3). CARE names BHEL and L&T as the source of order growth (B04, B09). How long these customers hold supplier money is a counterparty fact the corpus does not hold. Claude web should open the BHEL FY26 annual report and Q2 FY27 results (trade payables ageing, supplier payment terms), the L&T FY26 annual report (trade payables note) and the latest Numaligarh Refinery annual report (trade payables note).
Link 3 [INFERENCE]: If order growth sits with milestone-paying, retention-bearing project customers, debtor days can keep rising while inventory days fall. The peer read says cycle length follows advance share and customer mix, and Verifier D confirms the PSU-terms point (B06, B12d). The 3.8x rise in receivables sold without recourse (B02) then works as a bridge, not a cure, and a 190-200 day cycle needs the advance share to rise.
Binding constraint: Liquidity. Undrawn working-capital lines fell to Rs 13.05 cr from Rs 49.64 cr at 31 Mar 2026 (1,304.77 and 4,964.13 lacs; B02 rank 4). Covenant headroom is not found, and the Ind AS 1 covenant rule for FY27 is under assessment (B03, B02 rank 5). H1 FY27 brought Rs 57.53 cr of new long-term loans against Rs 20.88 cr repaid, and capex of Rs 58.02 cr against a Rs 20-30 cr guide (B05 rows 6, 7). The Rs 300 cr issue has already repaid Rs 225 cr of short-term debt (B05 row 21), so the next call on cash is working capital again.
Unsaid: No call discusses the top-10 customer share of about 80% (B05 red items). Management's answers on how order-book growth and working capital will be funded changed between quarters (B05 repeated_evasions). The risk note calls the business "majorly cash based" while 72.1% of receivables are not yet due and eight customers hold 71% (B02 rank 3). Customer advances for H1 FY27 and the recourse terms on the Rs 159.39 cr sold are not printed in the corpus (gate recommendation, missing evidence 2 and 4).
Observation that confirms or breaks this chain, and confirm-by date: Confirms (moves the cash determination to GROWTH-INDUCED): H2 FY27 consolidated operating cash flow positive, CFO/EBITDA at or above 0.5, and the FY27 operating cycle printed at or below 220 days. Breaks (moves it to STRUCTURAL): H2 FY27 operating cash flow negative while the order book rises. Read the 9-month cash flow in the Q3 FY27 results (Feb 2027) as the interim check; confirm-by is the FY27 audited results (May 2027; the FY26 results were filed 21 May 2026, B00).
```

```
CHAIN 2: The Rs 1,500 cr FY27 revenue guide needs Rs 912.55 cr in H2, +55.3% over H1, while October 2026 executed Rs 93.02 cr against Rs 152.1 cr a month needed (B01, B09)
Link 1 [DOC]: The order book was Rs 2,586.43 cr at 31 Oct 2026, of which power was Rs 1,677.48 cr, or 64.9% (B05 report, corrected for source fidelity; B09). Installed plus committed capacity supports about Rs 1,302-1,470 cr of revenue at FY26 asset turns (B09 capacity item).
Link 2 [PENDING LIVE VERIFICATION]: Who orders, and why now. BHEL tenders (about Rs 210 cr at L1) and a GE HRSG purchase order for 15 to 16 units are the two orders the plan leans on (B09, B05 T1, T2). Whether BHEL awards, and whether GE and Siemens convert reserved capacity into orders, are counterparty facts the corpus does not hold. Claude web should open the BHEL Reg 30 award disclosures and results call since Aug 2026, the GE Vernova latest quarterly release and filing (gas power backlog and HRSG slots), the Siemens Energy latest quarterly report, and the CEA Apr-Jun 2026 thermal progress report.
Link 3 [INFERENCE]: About Rs 380 cr, about 15.6% of the June book, is a GE letter of intent with no inputs (B12b-04), and the Thailand reservation term starts 1 Jun 2027 (B07). H2 FY27 revenue must therefore come mostly from the domestic power and refinery book, executing at 1.63x the October run rate (B09). DEE's own words say material ordering waits on drawings and inputs (B12b-05). A one-quarter slip in customer drawings would push revenue into FY28 with no change to the order book.
Binding constraint: Capacity and people. The Rs 1,500 cr guide sits at or above the Rs 1,302-1,470 cr range that capacity supports at FY26 asset turns (B09). Anjar runs at about 50% (B05 T3). Management volunteered a "considerable reduction" in headcount while guiding about 31% growth (B12b-19). Steel is bought on order receipt at fixed rates, so a delayed order ties up cash (B04).
Unsaid: Order book by customer is not found (B04). The 13 Nov 2026 order filing prints two FY27 inflow columns that differ by Rs 21 cr and does not explain the gap (B05 row 19). FY26 order inflow is not found, and the FY25 order book base of Rs 1,228 cr is marked "to be reconciled" in the printed AR (B03 guidance_table). The power division's revenue fell from 1,836.76 to 463.57 lacs between Q1 and Q2 with no reason given (B04).
Observation that confirms or breaks this chain, and confirm-by date: Confirms: executed revenue per month in the Nov 2026 and Dec 2026 order-position filings (filed Dec 2026 and Jan 2027) rises toward Rs 152.1 cr, and Q3 FY27 consolidated revenue prints above Rs 292.99 cr. Breaks: Q3 FY27 revenue at or below Rs 292.99 cr (B13-lite falsification_metric), or no GE HRSG purchase order by Q4 FY27 (B05 T3 kill_signal). Confirm-by: Q3 FY27 results (Feb 2027) for revenue; 31 Mar 2027 for the GE order.
```

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in claude.ai with live web, before Role 2.

### 4f. Open items for the operator

(a) Verifier B states its acceptance rate two ways. The block field reads 88.9% (caught plus partially caught, the field definition "ones the pipeline already had"). Counting only fully caught items it is 8 of 18 = 44.4%, below the 60% line in OR-29. The orchestrator used the block field. The operator rules which basis governs (confidence.yaml; B12b coverage_basis).
(b) B08 (promoter) and B09 (market size) closed with status partial. B08 skipped the sebi.gov.in search, the MCA21 charge register, the proxy-adviser search, Glassdoor and the CIT(A) status. B09 could not fetch one thermal article (HTTP 403), did not read the CEA Apr-Jun 2026 totals, did not retrieve USD/INR, and found no peer piping revenue or HRSG market size. Each is PENDING LIVE VERIFICATION (B08, B09).
(c) The stage 7 agent stalled after writing its report. The orchestrator built the B07 block file from the report (B13-lite open_items c).
(d) Verifier C findings F-G0-1 (strict ROCE formula where inputs exist: Core 41, deal-breaker 3 off), F-G0-2 (M5 scored 3 while the peer list was marked PEER DATA NEEDED: grand total 48, moat class THIN) and F-EM-1 (emerging moat 12.1-12.8 MODEST against 10.1 NONE) change scores, not the Gate 0 screen's lowest-tier outcome, which rests on the leverage override. F-EM-1 must be settled before stage 11 reads Pillar 3 (B12c, B13-lite open_items d).
(e) The Verifier A shadow run was not executed in this session, by operator batch instruction (B00 verifier_a_shadow).

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. DEE makes steel pipe systems to each customer's drawing, in plants in India and Thailand. The piping division gave 87.7% of FY26 revenue (B04).
2. FY26 revenue was Rs 1,142 cr, up 38%. Rated piping capacity is 93,500 MTPA. Anjar reached 30,000 MTPA in Sep 2025 and a 7,000 MTPA seamless plant started on 19 Mar 2026 (B09, B04, B03, B07).
3. Two small lines sit beside it: heavy fabrication at 7.0% and biomass power at 4.9%. The power line lost Rs 10.83 cr at segment profit level in FY26 (B04, B03).
4. The customers are boiler and turbine makers, engineering contractors and project owners such as BHEL, L&T, GE, Siemens, Numaligarh Refinery and Dow Chemical Canada (B05, B09). They are few: the top ten gave about 80% of FY26 income, against 59% a year earlier (B04).
5. Customers set a fixed rate with no escalation clause and pay in stages. DEE purchases about half of each order's value in steel as soon as it wins the order (B04).
6. Demand exists because power plants are being built. Power is 64.9% of the 31 Oct 2026 order book, and refinery and chemical projects make up most of the rest (B09).
7. Demand may grow with the 80 GW thermal plan to FY32, refinery expansion, a possible GE order for 15 to 16 HRSG units, and a nuclear option. The nuclear framework agreement of 16 Oct 2026 is not an order (B09).
8. Demand may not convert fast enough. Q2 revenue fell below Q1, H2 must be 55.3% above H1 for the Rs 1,500 cr guide, and capacity supports about Rs 1,302-1,470 cr at FY26 asset turns (B01, B05, B09).
9. The moat is narrow and sits in the piping line only. It rests on vendor approvals and port-side scale. The emerging moat score is 10.1 (NONE) on the stage path and 12.1 to 12.8 (MODEST) on the Verifier C path. Heavy fabrication and biomass power have no moat in the blocks (B04, B07, B12c).
10. The mental model, in draft: DEE climbs one rung, from a cost-advantaged converter to a value-added supplier, by filling Anjar and the seamless plant. The proof is H2 FY27 margin at or above 19% and positive operating cash flow (Section 2).
11. The fragility read is FRAGILE: seven outside variables must go right, three are company-narrated, and cash conversion alone can break the thesis (Section 4c).
12. Cash is the sore point. H1 FY27 operating cash flow was Rs -6.79 cr. Receivables rose 68.9% in FY26 and Rs 159.39 cr were sold without recourse. The Q1 FY27 cycle was 263 days. Two readings exist, growth-induced and structural, and H2 FY27 cash separates them (B01, B02, B04, B13-lite).
13. The accounts and governance carry open items. The auditor qualified the group opinion on Malwa Power assets of Rs 47.62 cr. Rs 13.85 cr owed in the Abohar tariff dispute is unprovided. Institutions voted down a pay rise for a promoter-family director at the 23 Sep 2026 AGM. Promoter pledge is nil (B02, B08).
14. The corpus could not establish the Q2 FY27 call (17 Nov 2026), the Q2 deck, order book by customer, tonnes shipped, customer advances, or peer piping revenue. Peers verified none of seven questions outright, and the promoter and market-size stages are partial (B00, B04, B06, B08, B09).
15. The biggest open questions: does H2 FY27 operating cash flow turn positive, does H2 revenue reach Rs 913 cr at a margin of 19% or more, and which basis rules Verifier B's acceptance rate and the emerging moat band (B13-lite open_items).

---

## SECTION 6: STANDING EXTRACTION ANNEX

Quote-then-comment. Quotes are as printed, with filename and page anchor. Dashes inside printed number ranges are written as hyphens. Page numbers are PDF page numbers from the [page N] markers in the .txt twins (the marker precedes the page content). Units are stated per figure.

### 6.1 Units

No per-tonne, per-case or per-unit rate is printed in the AR, deck, results or calls. Revenue per tonne is NOT DISCLOSED: tonnes shipped are not printed. The printed volume-type figures are capacity figures.

- Quote: "capacity of 93,500 MTs per annum in piping division and 32,400 MTs per annum in heavy fabrication division as on March 31," (CARE_Rationale_20261109.pdf, p.4). The deck prints "Installed Capacity: 93,500 MTPA (Piping) 32,400 MTPA (Heavy Fabrication)" (Investor_Presentation_1.pdf, p.8).
- Quote: Piping division "Total Revenue 1,00,197.90" INR lacs for FY26 (Annual_Report_2026.pdf, p.333, consolidated segment note).
- Comment: the two lines allow a capacity-based reference only: 1,00,197.90 lacs over 93,500 MT of rated capacity is about 1.07 lacs per rated MT (derived, B04). It is not a realisation: it mixes unfilled capacity, job work and Thailand work, and the piping basket spans spools, bends, fittings and skids.
- Per-unit figure on the Q1 FY27 call: "EUR 1-1.5 mn per GT unit", one product (a gas turbine piping package), as recorded in 05-concall.md section 1A T2 (Concall_Aug_2026_Transcript.pdf). Comment: per-unit, not per-tonne, and one product line.

### 6.2 Segment capital and debt

Consolidated segment note, INR lacs. Segment assets and liabilities, latest two periods (Results_Q2FY27_20261114.pdf, p.6) and the two years in the AR (Annual_Report_2026.pdf, p.333 for FY26, p.334 for FY25).

| Segment | Assets 30 Sep 2026 | Liabilities 30 Sep 2026 | Assets 31 Mar 2026 | Liabilities 31 Mar 2026 |
|---|---|---|---|---|
| Piping division | 1,94,985.17 | 85,841.68 | 1,77,256.63 | 95,990.99 |
| Power division | 7,915.56 | 2,404.11 | 9,274.53 | 3,172.54 |
| Heavy fabrication | 11,215.11 | 8,415.44 | 4,297.38 | 1,476.48 |
| Unallocated | 8,140.45 | 2,977.50 | 1,544.18 | 2,689.02 |
| Total | 2,22,256.29 | 99,638.73 | 1,92,372.72 | 1,03,329.03 |

The FY25 column of the AR (31 Mar 2025): Piping 1,44,958.45 assets and 72,281.35 liabilities; Power 10,048.74 and 2,926.23; Heavy fabrication 3,793.91 and 1,841.22; Unallocated 548.81 and 2,243.87; Total 1,59,349.89 and 79,292.67 (Annual_Report_2026.pdf, p.334).

Capital employed is not printed by segment. By subtraction (assets less liabilities, derived): at 30 Sep 2026 Piping 1,09,143.49, Power 5,511.45, Heavy fabrication 2,799.67, Unallocated 5,162.95, Total 1,22,617.56, which equals total equity in the same filing. At 31 Mar 2026 Piping 81,265.64, Power 6,101.99, Heavy fabrication 2,820.90, Unallocated (1,144.84), Total 89,043.69, which equals total equity (Results_Q2FY27_20261114.pdf, p.5).

Borrowings are not allocated as a separate line. The AR prints: "Segment liabilities primarily include trade payable, lease liabilities, borrowings and other liabilities" (Annual_Report_2026.pdf, p.333). Consolidated borrowings in total: non-current 16,092.44 plus current 40,240.72 = 56,333.16 lacs at 30 Sep 2026; non-current 13,348.78 plus current 55,345.20 = 68,693.98 lacs at 31 Mar 2026. Trade credits from banks and others are a further 7,242.76 and 6,577.63 lacs (Results_Q2FY27_20261114.pdf, p.5). The Piping division carries 5,412.58 of the 5,617.13 lacs FY26 finance cost (Annual_Report_2026.pdf, p.333), so the debt sits in Piping in substance, though the allocation is not stated.

Standalone, INR lacs (Annual_Report_2026.pdf, p.231 and p.232): FY26 Piping assets 1,59,925.42, liabilities 91,390.54; Power 5,097.14 and 1,859.73; Unallocated 18,901.31 and 1,966.75; Total 1,83,923.87 and 95,217.02. FY25 Piping 1,29,006.58 and 66,967.30; Power 5,189.50 and 1,720.03; Unallocated 18,222.63 and 1,984.66; Total 1,52,418.71 and 70,671.99.

Comment: Piping liabilities fell from 94,349.43 lacs at 30 Jun 2026 to 85,841.68 at 30 Sep 2026 after the Rs 225 cr debt repayment, while Piping and Heavy fabrication assets grew (Results_Q2FY27_20261114.pdf, p.6).

### 6.3 Guidance versus aspiration

Classes: (a) guidance with a period, (b) aspiration without a period, (c) capacity or capability only. Calls: F = Concall_Feb_2026_Transcript.pdf (5 Feb 2026), M = Concall_May_2026_Transcript.pdf (22 May 2026), A = Concall_Aug_2026_Transcript.pdf (6 Aug 2026). Page anchors are the stage 5 anchors, as recorded in 05-concall.md, where "txt page" is the [page N] marker.

| Item | Quote or printed figure | Class | Anchor |
|---|---|---|---|
| FY27 consolidated revenue | "top line of Rs 1.500 crores plus and EBITDA margin of more than 19%. 100% without any doubt" | (a) FY27 | A, txt p.9 |
| FY27 revenue, AR wording | "core revenue in the range of ₹1400-1500 crore, and core EBITDA margins of 18-20%" | (a) FY27 | Annual_Report_2026.pdf, p.101 |
| FY27 order inflow | "order inflows exceeding ₹2,000 crore (approximately 60% power, 40% oil & gas; ~60% domestic, 35-40% export)" | (a) FY27 | Annual_Report_2026.pdf, p.101 |
| FY27 piping revenue | "between Rs 1,150 crores to Rs 1,250 crores from our piping segment" | (a) FY27 | A, txt p.8 |
| FY27 EBITDA margin | "above 19% on console level... in any case" (May); 18-20% core (Feb) | (a) FY27 | M, txt p.7; F, txt p.7 |
| Working capital cycle | CFO "around 200 days in FY2027"; CMD "Our projection is 180 days" (May); "180 to 200 days" (Aug) | (a) FY27 | M, txt p.8, p.16; A, txt p.16 |
| Net debt | "below Rs 400-425 cr" at FY27 end | (a) FY27 | A, txt p.12 |
| FY27 capex | Rs 10-15 cr (Feb); Rs 20-30 cr (May); deck "Rs 15-20 cr maintenance only" | (a) FY27 | F, txt p.11; M, txt p.13; Investor_Presentation_1.pdf p.30 (as recorded) |
| Non-core FY27 revenue | "projected revenue for FY 27 shall be ~Rs. 47.71 crores which includes Rs. 23.4 crores from the pallete plant" (13 Nov 2026 filing), replacing Rs 80 cr said on the Aug call | (a) FY27 | 20261113-2bc19af2 order-position filing, p.3; A, txt p.4 |
| FY26 power drain | Rs 36 cr "will not be there" in FY27; EBITDA neutral | (a) FY27 | F, txt p.9, p.12-13 |
| Debt service | repay about Rs 40 cr a year; "absolutely no new inflow of any term loan" | (a) FY27 | F, txt p.11 |
| Anjar utilisation | "60-65% this year... almost 100% by end of next year" (Aug); on the same call 70-75% next year | (a) FY27-FY28 | A, txt p.8, p.17 |
| Seamless utilisation | 60-70% ramp in FY27 | (a) FY27 | M, txt p.7 |
| Order inflow booked | Rs 700 cr by 6 Aug; remainder minimum Rs 1,300 cr, up to Rs 1,800 cr | (a) FY27 | A, txt p.9 |
| Tax rate | 25.17% standalone; consolidated 20-21% | (a) FY27 | F, txt p.8; A, txt p.16-17 |
| Long-range revenue | "Vision 2030 ... revenue in excess of ₹2,500 crore" (AR, verb omitted); "we are trying that it should happen in FY29" | (a) FY30, maybe FY29 | Annual_Report_2026.pdf, p.101; A, txt p.14 |
| Anjar peak revenue | about Rs 1,500 cr by FY29 | (a) FY29 | A, txt p.17 |
| Net cash or minimal net debt | stated by FY29 | (a) FY29 | B03 guidance_table (AR p.101-102) |
| Thailand revenue | Rs 130 cr last year; goal Rs 170-200 cr; "no expansion" | (b) no period | A, txt p.6, p.8 |
| Seamless plant economics | peak revenue Rs 450 cr; IRR 30-35%; Rs 90 cr capex | (b) "peak", no period | F, txt p.3 |
| Seamless margin | about 20% EBITDA | (b) no period | M, txt p.13; A, txt p.12, p.14 |
| Nuclear partner | agreement "in Q2 under any circumstances" | (a) Q2 FY27; delivered late as a domestic framework (16 Oct 2026) | A, txt p.11 |
| Middle East reconstruction | "we have not accounted for these numbers in our projections even till next five years" | (b) no number | A, txt p.17 |
| Capacity ceiling | Rs 2,300-2,500 cr at 90% utilisation on present facilities | (c) capacity | F, txt p.12; M, txt p.11 |
| Installed capacity | Anjar 30,000 MTPA; seamless 7,000 MTPA; pellets 72,000 MTPA; 93,500 and 32,400 MTPA group | (c) capacity | Annual_Report_2026.pdf, p.11 and p.14; Investor_Presentation_1.pdf, p.8 |
| HRSG reservation | minimum US$15.27 m a year from 1 Jun 2027 | (c) capability, documented | Reg 30 filing 21 May 2026, Annex A (as recorded in B07 analyst_note) |

Comment: the AR frames guidance as "core" and the calls as "consolidated", and the basis differs (B04 guidance-wording item). The AR p.101 pages are as cited by B03 and B04.

### 6.4 Concentration

- Product. Consolidated FY26 revenue by segment, INR lacs: Piping division "Total Revenue 1,00,197.90", Power division 5,546.64, Heavy fabrication 8,042.75, Unallocated 412.63, total 1,14,199.92 (Annual_Report_2026.pdf, p.333). The Piping division is 87.7%, Heavy fabrication 7.0%, Power 4.9% (B04). Product shares inside Piping (spools, bends, fittings, skids, job work) are NOT DISCLOSED beyond job work at 16.4% of standalone revenue (B04). Comment: top product share is the Piping division at 87.7%.
- Customer, consolidated, INR lacs: "Numaligarh Refinery Limited 17270.65 ... % of Revenue 15.12%"; "Dow Chemical Canada ULC 11048.38 ... % of Revenue 9.67%"; "Punjab State Electricity Board 5138.78 ... 4.50%"; "Gail India Limited 4402.20 ... 3.85%" (Annual_Report_2026.pdf, p.336). Standalone: Numaligarh "17,268.79 ... 18.80%" and Dow "11,048.38 ... 12.03%" (Annual_Report_2026.pdf, p.234). Top 10: "Top 10 customers in FY26 contributed ~80% of the DDEL's TOI compared to 59% contribution in FY25, exposing it to customer concentration risk" (CARE_Rationale_20261109.pdf, p.2). Comment: the top-customer share is 15.12% consolidated and 18.80% standalone; the 80% figure sits in CARE only, not in the AR (B04).
- Geography, consolidated, INR lacs: "India 67,938.92 ... Outside India 46,261.00" for FY26, against 50,150.05 and 32,586.17 for FY25 (Annual_Report_2026.pdf, p.335). Outside India is 40.5% of FY26 revenue (derived, B07). Management said exports are more than 50% on the Aug call (A, txt p.13, as recorded in B07 export-share item). Trade receivables: India 27,427.62, outside India 10,906.43 lacs (Annual_Report_2026.pdf, p.335).
- Order-book mix, Rs cr, 31 Oct 2026: power 1,677.48, oil and gas 889.95, others 19.00, total 2,586.43 (20261113-2bc19af2 order-position filing, p.2, corrected closing column). Comment: order book by customer is NOT DISCLOSED in any filed source (B04).

### 6.5 Promise ledger

Dates are call dates: F 5 Feb 2026, M 22 May 2026, A 6 Aug 2026. Status is the stage 5 status (B05 report section 2A). "VB" marks a Verifier B re-reading (B12b). Stage 5 tally: 8 delivered, 7 partial, 5 missed, 4 pending. Verifier B states the tally becomes 6 delivered, 9 partial, 5 missed after rows 12 and 22 are re-scored (B12b-11), and asks that row 13 be held unverified (B12b-12).

| # | Made | Promise | Status | Evidence anchor |
|---|---|---|---|---|
| 1 | F, 5 Feb 2026 | Capex 95-98% done by Mar 2026; seamless plant nearing commissioning | Delivered | Reg 30 filing 19 Mar 2026 (commercial production) |
| 2 | F | Malwa PSERC order, relief near Rs 5.5/unit | Delivered | PSERC final order 27 Mar 2026 at Rs 5.224 (Results_Q2FY27, note 6, p.9) |
| 3 | F | Pellet plant start "very shortly", EBITDA neutral | Partial (about one quarter late) | A, txt p.4; commissioned mid-Q1 FY27 |
| 4 | F | FY26 power drain of Rs 36 cr will not recur | Partial | H1 FY27 Power EBIT Rs -2.71 cr (Results_Q2FY27, p.6); Rs 36 cr not reconciled to the segment note |
| 5 | F | Positive cash flow in H1 FY27 | Missed | H1 FY27 operating cash flow Rs -6.79 cr (Results_Q2FY27, p.7) |
| 6 | F | No new term loan; repay about Rs 40 cr a year | Missed | H1 FY27 long-term borrowings drawn Rs 57.53 cr, repaid Rs 20.88 cr (Results_Q2FY27, p.7) |
| 7 | F | FY27 capex Rs 10-15 cr (raised to Rs 20-30 cr in May) | Missed | H1 FY27 capex Rs 58.02 cr; CWIP Rs 87.48 cr (Results_Q2FY27, p.5, p.7) |
| 8 | F | Many L1 bids; Rs 300-400 cr of orders | Delivered | Order book Rs 1,303 cr (Dec 2025) to Rs 2,531 cr (30 Sep 2026) (CARE p.2) |
| 9 | F | FY26 margin 16-18% | Delivered | FY26 operating EBITDA margin 16.7% (M, txt p.4) |
| 10 | F, M | FY27 EBITDA margin 18-20%, then above 19% | Partial | Q1 16.9%; Q2 20.1% and H1 18.5% (derived, Results_Q2FY27, p.4). VB: CMD said margin "may drop on the face of it in terms of percentage" (M, txt p.7) |
| 11 | M, 22 May 2026 | Working-capital cycle 190-200 days; payables 70-75, debtors 95-100 | Partial | Q1 FY27 inventory 174, debtors 123, creditors 34, cycle 263 (A, txt p.16) |
| 12 | M | Nooter Eriksen capacity agreement; more OEM agreements | Delivered; VB: unverified | Reg 30 filing 21 May 2026; VB: Thailand "100% booked for three years" beside a book of about Rs 200 cr (A, txt p.5, p.6, p.13) |
| 13 | M | Siemens agreement expected | Delivered; VB: unverified | A, txt p.5-6: a "MOM" with 10 units next year; no confirming filing |
| 14 | M | GE HRSG and GT piping orders | Partial | A, txt p.5, p.15: HRSG PO for 15-16 units "yet to come" |
| 15 | M | Anjar "almost" optimal in FY27 | Missed (timeline) | A, txt p.8: 60-65% in FY27, about 100% by end FY28 |
| 16 | M | Capacity blueprint "very close... very soon" | Partial | A, txt p.5: no size or date; nuclear framework with a domestic EPC filed 16 Oct 2026 |
| 17 | M | BHEL orders feed the Rs 2,000 cr inflow | Partial | A, txt p.6-7: BHEL slower than expected; about Rs 200 cr in Q1 FY27 |
| 18 | M | No impairment needed; clean audit opinion "by third quarter" | Pending | Q2 FY27 review report still carries the qualified paragraph (Results_Q2FY27, p.2) |
| 19 | M | FY27 order inflow above Rs 2,000 cr | Pending | 13 Nov 2026 filing, p.2: cumulative inflow Rs 1,327.06 cr or Rs 1,348.52 cr to 31 Oct (two columns) |
| 20 | A, 6 Aug 2026 | Rs 25 cr of Q1 dispatches arrive in Q2 | Pending (not visible) | Q2 revenue Rs 292.99 cr below Q1 Rs 294.46 cr (Results_Q2FY27, p.4) |
| 21 | A | Rs 225 cr of Rs 293 cr net issue funds repay debt | Delivered | Rs 225.00 cr short-term debt repaid (Results_Q2FY27, note 4, p.8) |
| 22 | A | Nuclear partner agreement in Q2 FY27 | Delivered (late, different scope); VB: partial | 20261016 filing: domestic EPC framework, "not, by itself, an order" |
| 23 | A | Non-core FY27 revenue about Rs 80 cr | Missed (walked back) | 13 Nov 2026 filing, p.3: Rs 47.71 cr |
| 24 | A | Net debt below Rs 400-425 cr at FY27 end | Pending | Management net debt definition NOT FOUND (A, txt p.12) |

Comment: orders, plants, the tariff order and use of equity funds were delivered. Cash, loans, capex, working capital and number consistency were missed (B05 credibility basis). Credibility grade B (B05); Verifier B reads it at the B/C border (B12b).

### 6.6 Restated bases

- Quote, standalone: "47. The figures for the corresponding previous year have been regrouped/ reclassified, wherever considered necessary, to make them comparable with current year classification." (Annual_Report_2026.pdf, p.251). Consolidated Note 46 repeats it (Annual_Report_2026.pdf, p.351). No amounts are given. No formal restatement for a reorganisation, transfer or reclassification is stated (B02 restatements_found).
- Comparatives as printed in the latest filing: Q2 FY26 revenue from operations "26,999.99" INR lacs and Q2 FY27 "29,298.68" (Results_Q2FY27_20261114.pdf, p.6, consolidated segment statement). FY26 "1,14,199.92" against FY25 "82,736.22" (Annual_Report_2026.pdf, p.333, p.334). The Q2 filing carries no restatement note.
- Basis changes named by the stage 2 review: the standalone payables ageing for FY25 sits mostly in "overdue under 1 year" (12,904.65) while FY26 sits in "not due" (4,688.20), basis unexplained (Annual_Report_2026.pdf, p.207-208); the consolidated liquidity table drops trade credits of 6,577.63 that the FY25 line included at 8,120.50 (Annual_Report_2026.pdf, p.342); the consolidated customer table shows Numaligarh FY25 as nil against 2,798.38 in the standalone table (Annual_Report_2026.pdf, p.336 and p.234); the Heavy fabrication segment FY25 shows nil raw material cost (Annual_Report_2026.pdf, p.334) (all B02 restatements_found).
- Prospectus figures are restated consolidated information under the offer document, INR million (DEE_Prospectus_June2024.pdf), and Gate 0 used them for FY21 to FY23 (B01).
- Comment: the heavy fabrication segment appears from the FY26 note onward and the Molsieve entity joined on 19 May 2025, so FY25 and FY26 segment profit are not like-for-like (B02).

### 6.7 Corporate-action clauses

No scheme of arrangement, demerger, merger or share repurchase appears in the corpus or in any stage block (B00 to B09). Definitions of undertaking, liability allocation clauses, ratios, and appointed and effective dates therefore do not apply. If the operator suspects a scheme, the filing to fetch is the "Scheme of Arrangement" category on the BSE corporate announcements page for scrip code 544198, and the MCA21 filing of the order. Actions that are in the corpus:

1. Preferential issue (the largest). Board approval 3 Jun 2026: "Up to 59,76,096 Equity Shares of face value of ₹ 10/- each at ... ₹ 502/- each including the Premium of ₹ 492/- each, aggregating to an amount of ₹ 300, 00,00,192 under Promoter & Promoter Group category and Non-Promoter Category" (20260603-692306e6, p.1; the word between "at" and the rate is omitted). EGM called for 27 Jun 2026, cut-off 20 Jun 2026 (same, p.1). Promoter category: "Up to 3,98,406 Equity Shares ... for an aggregate consideration of Rs. 19,99,99,812/-" (same, p.3). Non-promoter category: "Up to 55,77,690 Equity Shares" (same, p.4). Allotment 8 Jul 2026: "the issuance of 59,76,096 equity shares ... Rs. 502 per Equity Shares including a premium of Rs. 492 ... aggregate consideration of Rs. 300, 00,00,192.00 ... on a preferential allotment on a private placement basis" (20260708-0f25c10a, p.1). Type: "Preferential Issue in accordance with Chapter V of the SEBI ICDR Regulations" (same, p.2). Trading approval filed 29 Jul 2026 (20260729-26299ab0). Use of funds: Rs 225.00 cr short-term debt repaid, Rs 68.56 cr general purposes (Results_Q2FY27, note 4, p.8). Comment: the promoter category (CMD, 3,98,406 shares) is inside the 59,76,096 total, so the Rs 300 cr is one issue, not Rs 300 cr plus Rs 20 cr (3,98,406 plus 55,77,690 equals 59,76,096). The promoter fall from 70.17% to 65.13% is dilution (B08).
2. Acquisition of Molsieve Designs Limited: "for a total consideration of Rs 658.82 lacs, thereby obtaining 70% equity shareholding" (Annual_Report_2026.pdf, standalone Note 43, p.250); goodwill arising 602.56 lacs; effective 19 May 2025 (Annual_Report_2026.pdf, p.327, Note 29(A)). No separate impairment test is shown (B02 rank 12).
3. IPO of June 2024 (fresh issue and offer for sale): post-Offer promoter holding 68.05% plus 2.12% against 97.24% plus 2.76% pre-Offer (DEE_Prospectus_June2024.pdf, capital structure table, as recorded in 01-gate0.md section E2). Listing 26 Jun 2024 (B00).
4. ESOP: 93,920 options granted and an allotment filed 6 Nov 2026 (20261106-5ef73e39, as typed in the B00 manifest). FY26 ESOP allotment 2,09,264 shares (B07).
5. Preferential-issue monitoring agency report for the quarter ended 30 Sep 2026, filed 14 Nov 2026 (20261114-ac6313bb, B00 manifest). Not read in full.

### 6.8 Related-party perimeter

Standalone Note 31 (Annual_Report_2026.pdf, p.222-226) and consolidated Note 29 (Annual_Report_2026.pdf, p.327-330). INR lacs, FY26 (FY25 in brackets). The note names these entities and persons.

| Entity | Relationship (as printed) | Nature and amount of transactions, FY26 |
|---|---|---|
| Malwa Power Pvt. Ltd. | wholly owned subsidiary | Sales of product 337.21 (114.28); interest income 10.93; interest expense 14.34; loan given 276.00, repaid 420.00; corporate guarantee given 2,300.00 (768.74); balances: loans 151.00, trade receivable 310.05, guarantee 527.04 (standalone p.223, p.224) |
| Dee Piping Systems (Thailand) Co. Ltd. | wholly owned subsidiary | Sales 655.46 (690.80); interest income 255.49 (549.53); purchases of traded goods 86.33; purchase of fixed assets 169.66; balances: loans 3,630.51, interest receivable 2,894.76, trade receivable 760.52, trade payable 128.08 (standalone p.223, p.224) |
| Dee Fabricom India Pvt. Ltd. | wholly owned subsidiary | Sales 6.11 (121.71); interest income 64.34; loan given 415.00, repaid 915.00; guarantee given 1,916.33; rent paid 12.00; fixed asset purchases 226.15 and sales 104.83; balances: loans 400.00, guarantee 141.85 (standalone p.223, p.224) |
| Atul Krishan Bansal Foundation | listed among subsidiary-type parties | CSR contribution 54.29 (42.50) (standalone p.223) |
| Molsieve Designs Limited | majority-owned subsidiary (from 19 May 2025) | Rent received 2.18; electricity 1.00; trade receivable 2.56 (standalone p.223, p.225) |

Persons (consolidated, p.328-329): Krishan Lalit Bansal remuneration 286.51 (271.79), loan received 110.00, repaid 765.00, rent 1.68; Ashima Bansal 93.30 (83.60); Shikha Bansal 171.04 (170.32), payable 762.90 (678.30), advance 29.46; Shruti Aggarwal 67.34; Sameer Agarwal (CFO until 6 Jan 2026) 63.44; Charu Agarwal 42.05 and Naveen Kishore Agarwal 27.67 (both until 6 Jan 2026); Sudhir Bhalla 99.51, loan received 152.90 and director loan balance 143.93; Ashvika Bansal 3.85. Standalone Shikha Bansal remuneration is 42.81 and payable 26.76. Personal guarantees from K.L. Bansal, Ashima Bansal, Madhubala, Shikha Bansal and Krisanakorn Triwattanathongchai are given for bank and NBFC borrowings; no fee is disclosed (consolidated p.329; B08).

Comment: DDE Piping Components Private Limited holds 75,32,275 shares as a promoter-group entity (Annual_Report_2026.pdf, p.73), and I did not find it named in the lists at standalone Note 31(A) or consolidated Note 29(A). The 762.90 payable to Shikha Bansal pertains to "salary payable... and Trade payable" with no split (consolidated p.329).

### 6.9 Pledge and shareholding

The corpus holds three promoter data points, not twelve quarters. Quarterly shareholding patterns for Sep 2023 to Jun 2026 are NOT DISCLOSED in the corpus: they were not collected, and B08 records the gap.

| Date | Promoter and group | Pledge | Anchor |
|---|---|---|---|
| Pre-Offer, Jun 2024 prospectus | 97.24% plus 2.76% = 100.00% | nil (Prospectus p.129 para 23, as recorded in B08) | DEE_Prospectus_June2024.pdf |
| Post-Offer, Jun 2024 | 68.05% plus 2.12% = 70.17% | nil | DEE_Prospectus_June2024.pdf, as recorded in 01-gate0.md |
| 31 Mar 2026 | "Promoter & Promoter Group 6 4,86,06,381 70.18" | not printed in the distribution table; Note 9F prints 70.17% | Annual_Report_2026.pdf, p.73; p.195 |
| 30 Sep 2026 | 65.13% (49,004,787 shares) | "WhetherAnySharesHeldByPromotersAreEncumberedUnderPledged | 2026-09-30 | | false" | shareholding-30Sep2026.txt, lines 39, 77 |

Institutional holding latest (30 Sep 2026, shareholding-30Sep2026.txt): mutual funds 7.95%, alternative investment funds 5.60%, domestic institutions 13.54%, foreign institutions 5.25% (foreign portfolio investors category one 4.11% and category two 1.13%), public 34.87%. At 31 Mar 2026 the AR printed mutual funds and AIF 13.91% and FPIs 0.98% (Annual_Report_2026.pdf, p.73). Comment: the promoter share fell because of the 59,76,096-share issue while promoter shares rose by 3,98,406 (B08). Pledge is nil on both dated filings.

### 6.10 Verification

Documents quoted in this annex, with filename and date:
- inputs/annual-report/Annual_Report_2026.pdf: FY2025-26 annual report, year ended 31 Mar 2026, BSE transmittal 27 Aug 2026.
- inputs/results/Results_Q2FY27_20261114.pdf: filed 14 Nov 2026.
- inputs/rating/CARE_Rationale_20261109.pdf: 9 Nov 2026.
- inputs/presentation/Investor_Presentation_1.pdf: Q1 FY27 deck, filed 5 Aug 2026.
- inputs/concalls/Concall_Feb_2026_Transcript.pdf (5 Feb 2026), Concall_May_2026_Transcript.pdf (22 May 2026), Concall_Aug_2026_Transcript.pdf (6 Aug 2026), quoted through the anchors in outputs/reports/05-concall.md.
- inputs/announcements/20260603-692306e6-da6e-4e6a-ba7b-6f42bf80d9fa.pdf (3 Jun 2026), 20260708-0f25c10a-7279-4dda-ada7-60c991719a2f.pdf (8 Jul 2026), 20260729-26299ab0-d88f-40b8-b73f-3d17e96a80a7.pdf (29 Jul 2026), 20261016-2b35419a-cd31-4cdc-a4f8-c22611f0e093.pdf (16 Oct 2026), 20261113-2bc19af2-8c1c-4e90-92ea-089d6872cd3d.pdf (13 Nov 2026), 20261106-5ef73e39-e6b2-453a-a469-d272f48e8e19.pdf (6 Nov 2026), 20261114-ac6313bb-0696-4cd9-9095-f055dd73fb05.pdf (14 Nov 2026).
- inputs/shareholding/shareholding-30Sep2026.txt: NSE XBRL, quarter ended 30 Sep 2026, submitted 16 Oct 2026.
- inputs/prospectus/DEE_Prospectus_June2024.pdf: 22 Jun 2024, quoted through outputs/reports/01-gate0.md and B08.

CORPUS COMMIT HASH: 21c75533b8196b8769070f8f871fad646740657b

```yaml
stage: B09b-dossier
company: "DEEDEV"
run_date: "2026-11-15"
model: claude-sonnet-5-5
status: complete
corpus_verdict: "CORPUS GAPPED-FRESHNESS"
corpus_gaps:
  - document: "Q2 FY27 earnings call transcript (call 17 Nov 2026)"
    expected_source: "BSE"
    kind: "freshness-pair"
  - document: "Q2 FY27 investor presentation (none filed to 14 Nov 2026)"
    expected_source: "company IR page"
    kind: "findable-missing"
  - document: "Broker or research notes (research folder empty)"
    expected_source: "company IR page"
    kind: "findable-missing"
  - document: "Screener export sheets: Profit & Loss, Quarters, Balance Sheet, Cash Flow, Customization for four companies (empty export)"
    expected_source: "company IR page"
    kind: "findable-missing"
  - document: "Quarterly shareholding patterns Jun 2024 to Jun 2026 (promoter pledge history)"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "Order book by customer"
    expected_source: "company IR page"
    kind: "plausibly-nonexistent"
  - document: "Tonnes shipped and revenue per tonne"
    expected_source: "company IR page"
    kind: "plausibly-nonexistent"
archetypes:
  - line: "Piping division (87.7% of FY26 revenue) and Heavy fabrication (7.0%)"
    archetype: "Build-to-spec component maker"
  - line: "Biomass power (4.9% of FY26 revenue)"
    archetype: "Licence/scarcity business"
transition:
  - line: "Piping division"
    from_tier: "R2 COST-ADVANTAGED CONVERTER (ROCE below the mid-teens R2 neighbourhood, between R1 and R2)"
    to_tier: "R3 VALUE-ADDED / SPEC'D SUPPLIER"
    engine: "Fill Anjar (about 50% now) and the 7,000 MTPA seamless plant against fixed overhead; seamless backward integration and Thailand HRSG reservation (from 1 Jun 2027)"
    proof_gate: "H2 FY27 consolidated operating EBITDA margin at or above 19% with gross profit in rupees rising; H2 FY27 consolidated operating cash flow positive with CFO/EBITDA at or above 0.5; FY27 operating cycle at or below 220 days"
    recognition_gap: "Open question: does the TO state already appear reflected in market pricing; Stage 11 resolves it via the PE gap"
    ugliness: "UNRESOLVED between ARTIFACT-OF-CLIMB and STRUCTURAL-FEATURE (cash determination INDETERMINATE; separated by H2 FY27 operating cash flow with Anjar utilisation above 60%)"
    transition_falsifier: "Q3 FY27 consolidated revenue at or below Rs 292.99 cr; H2 FY27 revenue under Rs 800 cr or H2 margin below 18%; H2 FY27 operating cash flow negative while the order book rises; Anjar near 50% through FY27; no GE HRSG purchase order by Q4 FY27"
dominant_variables:
  - "Order conversion to revenue at the guided margin (H2 FY27 need Rs 912.55 cr; margin at or above 19%)"
  - "Cash conversion and the working-capital cycle (CFO/EBITDA, operating cycle, receivables sold)"
  - "Utilisation of Anjar and the seamless plant (disclosed utilisation, external seamless orders, capex)"
  - "Thermal and HRSG order pipeline (BHEL awards, GE HRSG purchase order, Siemens clearance, Thailand reservation)"
business_falsifier: "The order book proves to be reserved capacity and letters of intent rather than orders (GE line about Rs 380 cr; Thailand booking claim), or revenue shifts to pass-through trading where material is 95-100% of order value, or a third qualified group audit opinion re-opens the group perimeter"
mental_model_status: "DRAFT - PENDING OPERATOR SIGN-OFF"
fragility:
  variable_count: 7
  verifiability_ratio: "4 of 7 externally observable"
  single_point_failure: "Cash conversion: H2 FY27 operating cash flow negative while the order book rises fails the proof gate on its cash leg alone"
  fragility_verdict: "FRAGILE"
candidate_count: 7
second_order:
  chains_drafted: 2
  pending_live_links: 2
  confirm_by_observations: 2
research_brief_items: 16
plain_summary_points: 15
annex:
  present: true
  questions_answered: 10
  corpus_commit_hash: "21c75533b8196b8769070f8f871fad646740657b"
```
