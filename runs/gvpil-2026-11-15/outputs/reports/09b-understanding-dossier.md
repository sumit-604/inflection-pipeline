# HALT 1 UNDERSTANDING DOSSIER: GE Power India Limited (GVPIL)

Run date: 2026-11-15. Stage: 09b. Model: claude-sonnet-5-5.
Units: figures keep the unit of their source. Filings and the annual report print INR million (INR M). Calls and decks speak in crore (Rs Cr). No figure is converted silently. "(calc)" marks arithmetic done by a stage, never by this file.
This file values nothing. It assembles what blocks B00 to B09 and the verifier blocks already found. Sections 1 to 5 add no new fact. Section 4e carries labelled inference. Section 6 quotes the corpus.
Erratum rule applied: the ORCHESTRATOR ERRATUM lines on reports 02, 03, 04, 08 and 09 govern over report bodies. Used here: 55.2% (not 55.3%) for the profit step-up share (B02 erratum); group materials purchases INR M 699.1 (not 697.6); Q2 FY27 material cost 64.4% on the net basis (not 67.6% gross); FY26 other assets INR M 1,601.4.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

Inventory only. Source: B00 (inputs, intake, inventory) and the stage blocks.

**1. CONCALLS (earnings calls held)**
- Concall_Nov_2025_Q2FY26_Transcript.pdf: Q2 FY26 call, 14 Nov 2025.
- Concall_Feb_2026_Transcript.pdf: Q3 FY26 call, 17 Feb 2026.
- Concall_May_2026_Transcript.pdf: Q4 FY26 call, 12 May 2026.
- Most recent quarter covered by a call: Q4 FY26 (12 May 2026) (B00.concalls).
- No Q1 FY27 earnings call was held. Only investor meets on 6 Jul 2026 and 10 Jul 2026 exist (InvestorMeet_2026-07-06_Transcript.pdf, InvestorMeet_2026-07-10_Transcript.pdf, held under other/) (B00, B05).
- Q2 FY27 results were filed on 13 Nov 2026. A more recent quarter has therefore reported, and its call transcript is absent. The call is scheduled for 16 Nov 2026, one day after the run date, so the transcript does not yet exist (B00.freshness_pairs).

**2. ANNUAL REPORTS**
- Annual_Report_2026.pdf: FY2025-26, 332 pages (primary).
- Annual_Report_2025.pdf: FY2024-25, 353 pages (prior-year reference) (B00.inventory).
- The latest completed FY (year ended 31 Mar 2026) is present. Two annual reports are held, so the "at least 3 years" test is not met. Ten years of annual numbers come from the screener Data Sheet (B01), not from three reports.

**3. RESULTS FILINGS**
- Results_Q2FY27_30Sep2026.pdf (quarter and half year ended 30 Sep 2026; letter 13 Nov 2026). A re-OCRed text copy exists (.ocr.txt) because the first text was weak; Q2 FY27 receivables and days stay unreadable (B05).
- Results_Q1FY27_30Jun2026.pdf (letter 13 Aug 2026).
- Results_Q4FY26_31Mar2026_audited.pdf (letter 11 May 2026).
- Results_Q3FY26_31Dec2025.pdf (filed 11 Feb 2026; moved from announcements/ after a page-1 check) (B00.moves).
- Quarter gap against the latest annual report: the AR covers the year to 31 Mar 2026. Two quarters (Q1 and Q2 FY27) sit after it, and both are held as filed results. No standalone Q1 FY26 or Q2 FY26 results filing is held; those quarters appear only as comparatives inside later filings (B00.inventory lists four results files).

**4. INVESTOR PRESENTATIONS**
- Investor_Presentation_1.pdf: investor meets 6 and 10 Jul 2026 (cover letter 3 Jul 2026).
- Investor_Presentation_Q4FY26_2026-05-11.pdf: Q4 FY26 earnings call, 12 May 2026 (cover letter 11 May 2026).
- Investor_Presentation_Q3FY26_2026-02-16.pdf: Q3 FY26 earnings call, 17 Feb 2026 (moved from announcements/).
- Latest held: Jul 2026 investor-meet deck. No Q2 FY27 deck is held (B00).

**5. RESEARCH AND RATING**
- ICRA_Rationale_2026-03-03.pdf: ICRA rating action, 3 Mar 2026, cites 9M FY2026; full rationale, 7 pages (B00).
- Broker or research notes: none (research/ is empty) (B00).

**6. CORPORATE ACTIONS (announcements/)**
- 31 Reg 30 and Reg 29 filings, 10 Dec 2025 to 15 Nov 2026, date-prefixed (B00, B00-intake).
- Items the stage blocks draw on: KMP changes (4 Feb, 13 Mar, 23 Mar, 19 Jun 2026); Vadodara repair facility (20 May 2026); Shoaiba order notice (12 Aug 2026); GST demand order (8 Sep 2026); NCLT certified copy filing (14 Oct 2026); results board intimation (4 Nov 2026); call intimation (6 Nov 2026) (B07, B08).
- One file is garbled beyond page 1: 20261115-f68052f4-d056-4ada-88e0-b645cb131036 (newspaper notice of results). No FGD contract termination filing (Jaypee Bina, Nigrie) appears in the 12-month list (B00.input_gaps).
- Other held material: 12 peer transcripts (BHEL four, ISGEC four, POWERMECH four) and four screener Data Sheet CSVs (B00).

**7. FRESHNESS PAIR CHECK** (B00.freshness_verdict and freshness_pairs[])
- FAILED: RESULTS to CONCALL. The trigger document is Results_Q2FY27_30Sep2026.pdf (letter 13 Nov 2026). The mate, a Q2 FY27 earnings-call transcript in inputs/concalls/, is absent. It does not exist on the run date. Source when filed: BSE scrip 532309 or the company IR page.
- PASS: RATING BULLETIN to RATIONALE (full ICRA rationale held).
- PASS: SEBI ORDER to ORDER TEXT (no SEBI order found in AR FY26, results or announcements).
- PASS: AR to LATEST AUDITED ANNUAL RESULTS (AR FY2025-26 held beside the audited Q4 FY26 results).

**Empty or partial folders, repeated in full from B00** (the empty-folder question was not asked; the /step1 autonomy contract standing answer is to run on with the gaps):
- prospectus: empty; not expected (long-listed company).
- research: empty.
- shareholding: partial; screener-derived table to Sep 2026 only, not the filed BSE pattern; no pledge detail.
- screening: partial; Data Sheet CSVs only. Profit and Loss, Quarters, Balance Sheet, Cash Flow and Customization sheets exported empty for all four companies.
- peer-concalls: BHEL stale (latest Q4 FY24, May 2024). ISGEC and POWERMECH current.
- presentation: no Q2 FY27 deck.
- concalls: no Q1 or Q2 FY27 earnings call.

**8. VERDICT LINE**

CORPUS GAPPED-FRESHNESS

Missing mate first: the Q2 FY27 earnings-call transcript (kind: freshness-pair; source: BSE scrip 532309 or company IR page; it exists only after the 16 Nov 2026 call). The phase-1 gate recommendation carries a cap because of this verdict (B00.degradation_applied). Other gaps, listed under it:

| Missing item | Expected source | Kind |
|---|---|---|
| Q2 FY27 earnings-call transcript | BSE / company IR page | freshness-pair |
| Filed BSE shareholding pattern with promoter pledge and encumbrance detail | BSE | findable-missing |
| AGM 14 Aug 2026 voting results for Items 8, 9, 10 | BSE / NSE | findable-missing |
| Durgapur scheme document (consideration, liability allocation) | BSE (Reg 30, 18 Sep 2025 scheme filing) | findable-missing |
| Q2 FY27 investor presentation | company IR page / BSE | findable-missing (when filed) |
| Screener Profit and Loss, Quarters, Balance Sheet, Cash Flow sheets (exported empty) | operator re-export from screener | findable-missing |
| Current BHEL concall (none on BSE in the last 12 months) | BHEL IR / BSE | plausibly-nonexistent (opacity is a data point) |
| Jaypee Bina and Nigrie FGD termination filing | BSE | findable-missing or plausibly-nonexistent; not established (B00) |
| Broker or research notes | none required | plausibly-nonexistent |
| Prospectus | not expected | plausibly-nonexistent |

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT - PENDING OPERATOR SIGN-OFF**

Nothing here is signed. Signing happens only in claude.ai after live-web stress-testing.

### PART A: THE FROM STATE

**A1. ARCHETYPE** (CLAUDE.md ARCHETYPE LIBRARY)
- Legacy project lines (FGD equipment contracts, new-build projects): Order-book business (EPC/defence/capital goods). Revenue runs through contracts booked over time, 60.2% of FY26 revenue by accounting nature (B04). The Gate 0 sector row is "EPC / Civil construction" (B00).
- Core services lines (spares, repairs, upgrades on coal boilers, turbines and generators): Order-book business, in its short-cycle form. Jobs arrive one at a time, and most finish inside about 12 months (B05). Two features pull away from the library: the OEM drawings come from the parent under licence (B04), and the run did not establish revenue by line (B04). No library entry fits the services line cleanly. The nearest is Order-book, so the declaration uses it and says so.
- The Durgapur boiler-components factory is not a line in this declaration. It leaves for JSW Energy; NCLT sanctioned the scheme on 1 Oct 2026 and the scheme was not effective at 30 Sep 2026 (B04, B05).

**A2. THE SIMPLE ANALOGY**
Picture a garage that keeps ageing power stations running. It once also built new machinery and fitted pollution filters, and those jobs lost money. Today its steady work is repair: it rewinds a generator, replaces turbine blades and supplies spare parts when a plant stops or comes up for its planned overhaul. The garage holds the original maker's drawings under a licence from its parent. It also depends on that parent for bank guarantees and has parked a large part of its cash in the parent's cash pool (B02, B03, B04). Two customers give it more than a third of its income (B02). The arrow starts here: a garage that is cleaning out its loss-making past and says its repair work will grow to 60% and then 80% of revenue (B05). That claim is management's and is not yet proved by filed numbers.

### PART B: THE TRANSITION

**B1. FROM TO.** Quality ladder (CLAUDE.md).
- Line: entity mix shift to core services. FROM: R1 COMMODITY PRICE-TAKER for the project lines (FY22 to FY24 losses, negative operating cash FY19 to FY21 (B01); FGD contracts carried the losses (step-1 brief via B04)). TO as claimed: R3 VALUE-ADDED / SPEC'D SUPPLIER (OEM drawings and installed-base data give partial pricing power (B04)).
- R1 to R3 is two rungs. The rung-jump base rate is one rung per 2 to 3 years, and a multi-rung leap is itself a warning sign. The evidence for R3 is thin: pricing power is "moderate" (B04), the Emerging Moat scan gives NONE at 11.6 (B07; Verifier C recomputes 10.6, B12c), and ICRA reports intense competition (B07). The operator rules whether the declared TO is R2 or R3.

**B2. THE ENGINE.** Two things change physically.
1. Revenue mix: the loss-making FGD and new-build revenue runs off while core services order intake grows (Rs 734 Cr in FY26 vs Rs 548 Cr; third-party fleet orders Rs 162 Cr to Rs 320 Cr) (B07, B05). Intake figures are deck claims, scored at 0.7x (B07). Durgapur cost of INR M 548.0 in FY26 (INR M 604.8 in FY25) already sits outside the continuing profit and loss account and stops at effectiveness (B02, B05).
2. Cost structure: materials fell from 67.3% to 60.2% of revenue and employee cost from 18.5% to 14.5% (B03).

**B3. THE PROOF GATE.** Both conditions below must hold. Until they do, the transition is narrative and the name is research.
- Metric 1: continuing-operations EBITDA margin excluding other income and excluding allowance reversals is at or above 11% in Q3 FY27 (reported about Feb 2027) and again in Q4 FY27 (B05 trigger 2, B03 monitorable; the 11% is a brief-level threshold that B03 marks unverified). Filed readings so far: 12.4% FY26, 14.5% Q1 FY27, 9.8% Q2 FY27, 12.2% H1 FY27 (all calc) (B04, B05).
- Metric 2: core services order intake in FY27 above Rs 734 Cr and services backlog at 31 Mar 2027 above Rs 1,218 Cr (B04 must-track).
- The single separating observation from B05: Q3 FY27 margin above or below 11%.

**B4. THE RECOGNITION GAP (to be resolved at Stage 11).**
Open question only: does the TO state, a services-led business with a clean margin, already appear reflected in market pricing? This file does not conclude. Stage 11 confirms or denies it through the PE gap. If the TO state is already reflected, the re-rating engine is gone and only earnings growth remains.

**B5. THE UGLINESS TEST.** Classification: ARTIFACT-OF-CLIMB, provisional.
- Optics: Q2 FY27 margin 9.8% against 14.5% in Q1; other income 59.0% of Q2 FY27 PBT before exceptional and 51.9% for H1; order book (RPO) down 38.9% to INR M 16,278; a discontinued-operations loss of INR M 304.2 in H1 FY27 (B04, B05, B02).
- Why artifact: INR M 7,749 of the RPO fall is the Jaypee FGD termination, and like for like the fall is 13.8% (calc) (B04). The discontinued loss ends when the Durgapur scheme takes effect (B05 trigger 4).
- What is not yet explained: the Q2 FY27 margin drop (no call was held, B05) and the composition of other income (pool interest at 5.5% to 6.35% on INR M 4,500 explains only about a quarter of it, calc) (B04). If Q3 FY27 repeats a margin under 10% with no named mix reason, the classification moves toward STRUCTURAL-FEATURE (B05 kill signal).

**B6. THE TRANSITION FALSIFIER.** Evidence that kills the arrow:
- A second quarter with margin ex other income under 10% and no named mix reason (B05 kill, trigger 2).
- Core intake below the prior-year quarter, or services backlog under Rs 1,124 Cr (the Mar 2025 level) (B04, B05 trigger 1).
- Cost of materials above 67% of revenue after the Durgapur supply terms start (B04 first-deterioration signals); or a JSW supply cost above INR M 247.0 a year (B05 trigger 4).
- Third-party fleet share of core orders staying under about 50%; the FY26 full-year share is 43.6% (calc) (B07).

### PART C: WHAT THE MODEL WATCHES

**C1. DOMINANT VARIABLES** (these become Role 5.5 tracker signals)
1. Core services order intake and services backlog. Now: FY26 intake Rs 734 Cr; services backlog Rs 1,218 Cr (includes FGD operation and maintenance, not core only) (B04, B05); total RPO INR M 15,273 at Q2 FY27, down 16.3% YoY (B05).
2. Continuing EBITDA margin ex other income and ex reversals. Now: 14.5% Q1, 9.8% Q2, 12.2% H1 FY27 (calc) (B05).
3. Durgapur demerger effectiveness and post-demerger supply terms. Now: NCLT sanction 1 Oct 2026, not effective at 30 Sep 2026; supply cost after the scheme NOT FOUND; five-year JSW supply agreement (B05, B02, B07).
4. Cash quality and group exposure. Now: FY26 CFO INR M 4,692.5 carried by a receivables release of INR M 5,136.0; INR M 4,500.0 unsecured demand deposit with the group cash-pool header; enabling limit proposed to rise to INR M 10,000 (B02, B03, B08).

**C2. WHAT THE MODEL REJECTS**
- The market-size dispute (Rs 2,500 Cr defined against Rs 3,500 to 4,000 Cr undefined). The binding constraint is order conversion and margin, not market size: the market stage's own share-based figure grows at 6.4% a year over three years, below the 25% intake growth of the last four years (B09).
- The reported 27.0% EBITDA margin, the FY26 EPS and RoNW, and the book-to-bill of 0.18. All are distorted (B04 irrelevant_ratios).
- A revival of FGD orders and the gas and hydro lines as growth drivers (B05 dropped_triggers).
- Peer margin comparison across unlike bases (POWERMECH includes other income) (B06).

**C3. THE BUSINESS FALSIFIER.** Evidence that forces re-declaring the FROM business itself:
- Group-sourced income (INR M 851.9, 25.1% of profit before exceptional items in FY26) growing to the main source of profit, which would make this a captive service arm of the parent rather than a customer-facing business (B02).
- Withdrawal of the parent's IP licence, the India-region mandate or the parent guarantees that carry INR M 16,000 of bank capacity (B02, B03, B07).
- A filed revenue split by line showing core services well under the 55% stated for Q2 FY26 (B04). The run did not establish this split.

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

(Draft at Halt 1, from B01 to B09, five-question spec in prompts/13-synthesis-pipeline.md.)

GE Power India repairs, upgrades and supplies spare parts for coal boilers, steam turbines and generators in India (B04, B09). Its filings split FY26 revenue by accounting nature only: 60.2% from construction contracts booked over time, 38.7% from product and spares sales and 0.9% from services (B04). The run did not establish revenue by business line, and management put core services at about 55% of revenue in Q2 FY26 (B04). The core work is short cycle, such as a generator stator repair at Monnet Power or an electrostatic precipitator refurbishment at RRUVNL Kalisindh (B03). A coal unit that trips loses generation, and its critical rotating parts need OEM drawings that the company holds under licence from its parent (B04). The legacy lines are FGD pollution-control equipment and new-build projects, and the Durgapur boiler factory leaves for JSW Energy (B04, B05). Customers are central, state and private coal generators, among them Monnet Power, RattanIndia Power, RRUVNL Kalisindh and Adani units, plus Jaypee and BHEL on the legacy side (B03, B05). The top two customers took 38.6% of FY26 revenue against 34.8% in FY25, and the filings do not name them (B02, B04). Orders come job by job, and management says most finish within 12 months (B05). Present demand comes from outages and breakdowns on an ageing fleet, tracked as "NTPC and state genco outage plans and spares tenders" and "All-India coal PLF and generation" (B09). "Non-GE fleet owners (Adani Power, JSW Energy, Chinese-make operators)" gave 53% of core orders in Q3 FY26 but 43.6% across FY26 (B09, B07). Forward demand rests on "CEA R&M and life extension programme phases", where a 2022 list holds 63.4 GW of units, and on turbine upgrades that take three to four years to commission (B09, B05). "MoEFCC FGD applicability notification and compliance dates" now work against the FGD line, because only about 8 GW of category A plants must still fit FGD (B09). "BHEL spares and services bookings" measure a rival on the same fleets, and "JSW Energy Durgapur demerger completion and supply terms" track a party that is both customer and future supplier (B09). On its own GE fleet the company holds an installed-base pull, which the moat scan scores Moderate on management claims (B07 C1). On other makers' fleets the scan also scores a Moderate engine on claims, finds nothing a rival must give up to copy it, and ICRA reports intense competition (B07). No scored category covers the FGD, new-build or Durgapur lines, so the run found no moat there (B07). The emerging moat score is 11.6, classed NONE and 0.4 under the band edge; Verifier C recomputes it at 10.6 (B07, B12c).

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. VERTICALS FRAMED

**Vertical 1: Core services order intake and services backlog**
- The corpus establishes: FY26 core intake Rs 734 Cr vs Rs 548 Cr (+33.9% calc); third-party fleet orders Rs 162 Cr to Rs 320 Cr; FY26 third-party share 43.6% (calc) against 53% in Q3 FY26 alone (B07). Services backlog Rs 1,218 Cr vs Rs 1,124 Cr (+8.4% calc) (B05). Total RPO INR M 15,273 at Q2 FY27 (B05). Top two customers 38.6% (B02).
- It cannot establish: core-only backlog (Rs 1,218 Cr includes FGD operation and maintenance), order inflow for GVPIL in the filings (derived only), the names behind 38.6%, revenue by line, and how Shoaiba (about Rs 550 Cr, notified 12 Aug 2026) sits in the backlog (B04, B05, B07).
- Deciding questions: (1) Is the 85% to 90% execution figure about the whole Rs 1,628 Cr order in hand or a named services backlog (B04 mgmt_questions)? (2) What do Q3 FY27 and Q4 FY27 decks show for core intake against Rs 734 Cr? (3) Is the third-party share a trend or a one-quarter peak?

**Vertical 2: Continuing margin ex other income**
- The corpus establishes: 12.4% FY26, 14.5% Q1 FY27, 9.8% Q2 FY27, 12.2% H1 (calc) (B04); the 11% is the FY26 entity-level figure including discontinued Durgapur, not an FY27 guide (B05); Q2 FY27 cost of materials 64.4% net of WIP against 59.7% in Q1 (B05, B12a); ISGEC margins rose in the same quarter (B06).
- It cannot establish: why Q2 fell 4.7 points (no call), segment margins (refused on three calls, B05), or the composition of INR M 631.6 H1 other income (B04).
- Deciding questions: (1) What explains the Q2 FY27 drop? (2) Does Q3 FY27 sit above or below 11%? (3) How much of other income is pool interest and how much is write-backs or group income?

**Vertical 3: Durgapur demerger and supply terms**
- The corpus establishes: scheme approved by the board on 18 Sep 2025, appointed date 1 Jul 2025, share ratio 10 JSW shares for every 139 GVPIL shares, NCLT sanction 1 Oct 2026, not effective at 30 Sep 2026 (AR26 p.28, p.194; Results Q2 FY27 p.7); five-year capacity-reserved supply agreement (B04); discontinued loss INR M 548.0 FY26 and INR M 304.2 H1 FY27 (B02, B05); INR M 247.0 of internal billing not charged to continuing cost (B02).
- It cannot establish: consideration to GVPIL, supply cost after the scheme, or liability allocation (B02, B08).
- Deciding questions: (1) When is the certified order filed with the RoC and the scheme effective? (2) What supply terms does JSW charge? (3) Does the alternate supply chain (about 18 months from May 2026, "very soon" in Jul 2026) have a date?

**Vertical 4: Cash quality and group exposure**
- The corpus establishes: CFO INR M 4,692.5 vs PAT; receivables fell INR M 5,136.0 including INR M 3,430.6 of one-time BHEL cash; INR M 4,500.0 ICD to LM Wind Power Blades (India) (21.4% of total assets, 106% of cash, calc); net cash INR M 8,473.1 with the ICD and INR M 3,973.1 without; bank-guarantee lines INR M 7,977.6 used against INR M 16,000 needed (B02, B03).
- It cannot establish: the guarantee cover on the present ICD balance (Notice reads secured; Note 16 and CARO read unsecured at 31 Mar 2026), AGM vote tallies, and pledge detail (B03, B08).
- Deciding questions: (1) Does a written guarantee cover 100% of the ICD principal today? (2) Does the ICD balance stay at or below INR M 4,500.0? (3) Does CFO excluding group-deposit movements stay at or above PAT?

### 4b. CANDIDATE SIGNAL TABLE (UNVERIFIED; verification and tracker writes at Role 5.5 in claude.ai)

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| NTPC and state genco outage plans and spares tenders (B09, end-customer) | Outage-linked spares and repair tenders at named gencos fall YoY for two consecutive quarters while GVPIL core intake also falls | Event-Driven | NTPC and genco tender portals and exchange filings per Downstream_Source_Discovery_Protocol_v1_0 registry |
| Non-GE fleet owners: Adani Power, JSW Energy, Chinese-make operators (B09, end-customer) | These owners' disclosed maintenance spend or outage commentary shows work moving to in-house or local repairers | Quarterly | Owners' results and earnings calls per registry |
| CEA R&M and life extension programme phases (B09, regulatory) | No award from the 63.4 GW list through FY27; upgrade share of backlog keeps running off | Event-Driven | CEA R&M programme page and CERC orders per registry |
| All-India coal PLF and generation (B09, macro) | Coal PLF falls for two consecutive months while GVPIL spares intake stays flat | Monthly | CEA monthly generation reports and Grid-India |
| MoEFCC FGD applicability notification and compliance dates (B09, regulatory) | A category A award to GVPIL appears (breaks the run-off view); or category A scope shrinks below about 8 GW | Event-Driven | MoEFCC notifications per registry (regulator orders page) |
| BHEL spares and services bookings (B09, counterparty) | BHEL reports rising service bookings on non-BHEL fleets while GVPIL third-party share falls under 50% | Quarterly | BHEL results calls and exchange filings (BHEL transcripts stale, B06) |
| JSW Energy Durgapur demerger completion and supply terms (B09, counterparty) | Scheme effectiveness slips beyond 31 Mar 2027, or supply terms push cost of materials above 67% of revenue | Event-Driven | BSE and NSE filings, NCLT order, RoC filing per registry |

### 4c. FRAGILITY READ

- variable_count: 6 external variables must go right: (1) core services intake growth; (2) third-party fleet conversion; (3) margin at or above 11% ex other income; (4) Durgapur effectiveness and acceptable supply terms; (5) outage and PLF demand on the coal fleet; (6) parent guarantee and bank-line support.
- verifiability_ratio: 4 of 6 externally observable (margin through filed results; Durgapur through NCLT and RoC filings; outage and PLF demand through CEA and Grid-India; guarantee through filed notes). Intake growth and third-party conversion are company-narrated (deck claims, B07; peers cannot test them, B06).
- single_point_failure: parent guarantee and bank-line dependence. All bid capacity rests on one guarantor, and banks require GE Vernova to keep majority ownership (B02, B03). The risk is low today because the promoter withdrew its exit plan on 25 Jul 2024 (B08), but the dependence is structural.
- fragility_verdict: MODERATE. The operator may rule it up to FRAGILE on the single point.

### 4d. RESEARCH BRIEF (claude.ai work order)

1. Q2 FY27 earnings-call transcript (call 16 Nov 2026): BSE scrip 532309 or IR page. Read the Q2 margin explanation, other income composition, Shoaiba treatment, the Q4 FY26 revenue one-off question (CFO Q3 and Q4 answers conflict, B12b) and the three-party BHEL settlement group-side amounts (B12b).
2. Filed BSE shareholding pattern for Sep 2026: promoter pledge or encumbrance, FII and DII (closes the UA qualifier and pledge trend).
3. AGM 14 Aug 2026 voting results for Items 8, 9, 10 (BSE and NSE); proxy adviser reports (IiAS, SES, InGovern).
4. A written GE Vernova Inc. Parent Corporate Guarantee covering the INR M 4,500.0 ICD, and the post-AGM ICD balance.
5. Durgapur scheme document (BSE Reg 30 of 18 Sep 2025): consideration, liability allocation, definitions; RoC filing date and effectiveness; JSW Energy disclosures of supply terms.
6. Shoaiba: signed contract, backlog entry, customer filings (Reg 30 of 12 Aug 2026).
7. PENDING LIVE VERIFICATION (Chain 1, Link 2): the customer-health read for third-party fleet owners. Open JSW Energy Limited's latest annual report and Q2 FY27 earnings-call transcript, and Adani Power Limited's Q2 FY27 earnings-call transcript, for maintenance spend and outage commentary. Also open NTPC Limited's latest overhaul programme and annual report.
8. PENDING LIVE VERIFICATION (Chain 2, Link 2): the borrower and guarantor read. Open the latest financial statements of LM Wind Power Blades (India) Private Limited from MCA (the Notice says its rating is not available, B08), and GE Vernova Inc.'s latest 10-Q for guarantee commitments and credit position.
9. Build Rule F chains 3 to 5 with live links before Role 2. Candidate topics from the corpus: Durgapur supply terms to margin; CEA R&M awards to upgrade orders; parent IP licence and royalty perimeter to margin.
10. BHEL: current spares and services bookings and a current concall (BHEL posted no transcript on BSE in 12 months, B00).
11. Fleet MW or unit list behind the Rs 2,500 Cr defined market and the Rs 3,500 to 4,000 Cr restated market (B09 separating observation); CEA R&M document market value (B09 skipped).
12. Policy status: MoEFCC FGD notification dates (the calls cite July, 11 July and 11 June 2025, B12b) and category sizes (B12b).
13. Competitor thermal-services revenue: Doosan, Thermax, L&T, Power Mech, ISGEC services division (B09 skipped).
14. Governance searches not reached: MCA and RoC, SEBI orders portal, SAT, SFIO, ED, employee-review sites for the 71.11% turnover (B08 skipped).
15. Source URL verification of web-sourced figures Verifier A could not check: CEA 224.15 GW, 44 GW under construction, IMARC USD 1,043.6M, BHEL Rs 75,000 Cr (B09); SEC USD 200M and vote percentages (B08); ICRA-attributed PLF 65.2% that the corpus ICRA rationale does not contain (B12a).
16. Royalty: reconcile the INR M 310.0 gap between Note 36 (INR M 435.7) and the P&L line (INR M 125.7) (B02).
17. Reconcile CARO vii(b) disputed dues INR M 8,022.1 with Note 39 INR M 4,575.9 (B03).

### 4e. SECOND-ORDER STUB (Master Prompt v3.7, Rule F)

```
CHAIN 1: Core services intake grew while the backlog barely moved. FY26 core intake Rs 734 Cr vs Rs 548 Cr (+33.9% calc) and third-party fleet orders Rs 162 Cr to Rs 320 Cr (B07); services backlog Rs 1,218 Cr vs Rs 1,124 Cr (+8.4% calc), against a spoken "core order in hand up ~40%" (B05)
Link 1 [management deck claim, scored 0.7x in B07]: Intake rose about a third in FY26, but the Rs 1,218 Cr backlog includes FGD operation and maintenance and is not core only, so the intake and the backlog do not yet agree (B05).
Link 2 [PENDING LIVE VERIFICATION]: Who pays, and why now. The named payers for third-party jobs are Adani Power, JSW Energy and Chinese-make operators (B09). Claude web must open: JSW Energy Limited latest annual report and Q2 FY27 earnings-call transcript (maintenance spend, outage plans); Adani Power Limited Q2 FY27 earnings-call transcript; NTPC Limited latest overhaul programme. No counterparty fact is stated here.
Link 3 [INFERENCE]: If third-party owners hire GVPIL only where unit geometry matches its OEM drawings, intake growth is bounded by the count of similar units, not by market size. The drop from 53% in one quarter to 43.6% across FY26 (B09, B07) fits that reading and also fits a lumpy quarter. The two readings are separated by the Q3 and Q4 FY27 third-party share.
Binding constraint: Repair capacity is not stated (B09 capacity_check NOT FOUND). The dedicated Vadodara repair facility setup period ends about 25 May 2027 (calc from 20 May 2026) (B07). Boiler-component supply depends on a five-year JSW agreement while an alternate chain is built (B05). Inventory rose 69.9% against revenue up 21.2% (71 vs 46 days, calc) (B02).
Unsaid: The NTPC GE Power Services joint venture is a customer, supplier, receivable holder and advance giver at once: revenue INR M 1,111.6 (8.8% of revenue), receivable INR M 703.0, advances INR M 833.0 (B02 rank 10). No call mentioned customer concentration, and the names behind the top two customers at 38.6% are NOT FOUND (B05 2D, B04).
Observation that confirms or breaks this chain, and confirm-by date: Confirms if Q3 FY27 core order intake exceeds the Q3 FY26 base of Rs 136 Cr (B05 1C) and FY27 core intake exceeds Rs 734 Cr with services backlog above Rs 1,218 Cr at 31 Mar 2027. Breaks if intake falls below the prior-year quarter or backlog falls below Rs 1,124 Cr (B04, B05 trigger 1). Confirm-by: Q3 FY27 results and deck (about Feb 2027) for the first test; Q4 FY27 results and deck (about May 2027) for the full-year test.
```

```
CHAIN 2: The INR M 4,500.0 group deposit absorbed 95.9% of FY26 operating cash. FY26 CFO INR M 4,692.5 rested on a receivables fall of INR M 5,136.0; the whole INR M 4,500.0 went to an unsecured demand deposit with LM Wind Power Blades (India), the group cash-pool header; the board approved raising the enabling limit from INR M 4,500 to INR M 10,000 on 19 Jun 2026 (B03; AR26 Notice p.311)
Link 1 [filed, AR26 Notes 16, 36]: The deposit sat at the approved cap at 31 Mar 2026. Note 16 and CARO read it as unsecured. The Notice (outside the notes) says a GE Vernova Inc. guarantee secures the lending, and B03 reads that as the proposed INR M 10,000 guarantee, starting after the 14 Aug 2026 vote, outcome NOT FOUND (B02, B03).
Link 2 [PENDING LIVE VERIFICATION]: Who pays, and why now. The borrower is LM Wind Power Blades (India) Private Limited, an indirect wholly owned GE Vernova Inc. subsidiary with rating not available per the Notice (B08). Claude web must open: LM Wind Power Blades (India) Private Limited's latest financial statements on MCA, and GE Vernova Inc.'s latest 10-Q for guarantee commitments and credit position. No counterparty fact is stated here.
Link 3 [INFERENCE]: If the deposit moves toward INR M 10,000, a larger share of the company's liquidity depends on one group borrower and one guarantor. The cash left outside the pool (INR M 3,973.1 net, B02) would then fund the working capital for services growth, including the inventory build. Growth in the services lane would then compete with the group deposit for the same cash.
Binding constraint: Bank-guarantee capacity rests on one guarantor: INR M 7,977.6 used against INR M 16,000 needed (peak FY26 INR M 20,432), and the banks require GE Vernova to keep majority ownership (B02, B03). Working capital: gross receivables INR M 8,260.5, with 15.9% aged over six months (B02).
Unsaid: Note 42 and the Note 43 credit text omit the ICD (B02). The Directors' Report says no guarantee was provided while Note 36 labels INR M 7,977.6 "Corporate Guarantee issued" (B03). CARO ii(b) says no working-capital facility was sanctioned while the Notice shows INR M 610 fund-based sanctioned (B03). The call framed the deposit as surplus working capital and was silent on the unsecured status (B05 2D).
Observation that confirms or breaks this chain, and confirm-by date: Confirms if the ICD balance stays at or below INR M 4,500.0 and a written guarantee covers 100% of principal, with the ICD included in the credit-risk notes (B03 monitorable). Breaks if the balance rises above INR M 4,500.0 without cover. Confirm-by: Q3 FY27 results notes (about Feb 2027) for the balance; AR27 Notes 16 and 36 (about Jun 2027) for the guarantee text and the credit-risk note.
```

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in claude.ai with live web, before Role 2.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. GE Power India repairs, upgrades and supplies parts for coal power plants in India (B04, B09).
2. FY26 revenue was INR M 12,692.7. Contract work booked over time was 60.2% of it, product and spares sales 38.7% (B04; AR26 p.176).
3. It once also built FGD pollution filters and new plants. Those lines lost money and are running off. The Durgapur boiler factory goes to JSW Energy, and the scheme was not yet effective at 30 Sep 2026 (B04, B05).
4. Customers are state, central and private coal power generators. Two customers gave 38.6% of FY26 revenue, and their names are not filed (B02, B04).
5. They pay when a plant needs spares, a repair or a planned overhaul. Most jobs finish within about 12 months (B05).
6. A large share of the work depends on drawings the company holds under licence from its GE parent (B04).
7. Demand today comes from ageing plants running hard. The tracker watches plant load, outage plans and spares tenders (B09).
8. Demand could grow from life-extension work on a 2022 list of 63.4 GW and from large turbine upgrades. These take three to four years (B09, B05). FGD work is shrinking because only about 8 GW must still fit it (B09).
9. The company has a Moderate edge on its own GE fleet and a Moderate edge on other makers' plants, both resting on management claims. It has no scored edge in its FGD, new-build or Durgapur lines (B07).
10. The draft mental model: a business climbing from a loss-making project past to a services-led core. The claim is two rungs, R1 to R3, which is a warning sign in itself. It is proved only if the margin ex other income holds at 11% or more in Q3 and Q4 FY27 and core orders rise (B02, B05, B07).
11. The fragility read is MODERATE. Six outside things must go right, four can be watched from filings, and all bank-guarantee capacity rests on one parent (B02, B03).
12. The corpus could not establish revenue by business line, the names of the top customers, or the reason margin fell from 14.5% to 9.8% in Q2 FY27 (B04, B05).
13. It also lacks the filed shareholding pattern, so promoter pledge is not known (B03, B08). No earnings call explains Q1 or Q2 FY27 (B05).
14. Open question one: is FY26 profit a base? Of the INR M 3,174.4 profit step-up, 55.2% came from a credit-loss reversal and higher other income (B02 erratum), and other income was 51.9% of H1 FY27 PBT (B04).
15. Open question two: is the INR M 4,500.0 group deposit safe, and will cash from operations be enough to fund growth without a repeat of the one-time receivables release (B02, B03)?

---

## SECTION 6: STANDING EXTRACTION ANNEX

Quote-then-comment. Page anchors are PDF page markers in the page-marked .txt unless noted. "via report" means the quote comes from a stage report and the source page was not re-opened here.

### 1. UNITS
- No per-unit figure (price per MW, per job, per tonne, ARPU) is printed. Volume lines (MW serviced, jobs, units) are NOT DISCLOSED.
- Quote: "Revenue from operations  12,692.7  10,471.0" (Annual_Report_2026.pdf p.176, Note 35, INR M, FY26 and FY25). The basket is all product, contract and service revenue together.
- Quote: "Construction contracts (Over the time)  7,640.3  6,215.2 / Sale of Products (Point in Time)  4,911.7  4,130.8 / Sale of services  109.5  111.7" (Annual_Report_2026.pdf p.176, INR M).
- Quote via report: core services order intake Rs 734 Cr FY26 and Rs 548 Cr prior year; third-party fleet orders Rs 320 Cr vs Rs 162 Cr (Investor_Presentation_Q4FY26_2026-05-11.pdf p.10, cited by 07-emoat.md).
- Comment: a per-job unit cannot be derived. The only derivable base is Rs 100 of revenue (B04.unit_economics). Intake is order value, not revenue.

### 2. SEGMENT CAPITAL AND DEBT
- Quote: "Company's business activity falls within a single operating segment i.e. Power Generation equipment and related services." (Annual_Report_2026.pdf p.176, Note 35).
- Segment assets, segment liabilities, capital employed and segment borrowings: NOT DISCLOSED (single segment). Note 35 prints only revenue by nature, revenue by geography and non-current assets by geography: "India  1,224.6  1,455.5 / Outside India - -" (p.176, INR M, FY26 and FY25).
- Borrowings are not allocated by segment. The only borrowing printed in the pages read is the held-for-sale Durgapur block: "Borrowings 330.0" with "Total assets 344.0" and "Total equity (548.7)" at 31 Mar 2026 (Annual_Report_2026.pdf p.195, Note 47(v), INR M). The FY25 comparative of that block was not read for this annex; B02 states the 330.0 is the bank fund-based draw, so debt is not nil (B02 rank 6).
- Comment: the entity is a single reporting unit, so segment capital cannot be built from filings.

### 3. GUIDANCE VERSUS ASPIRATION

| # | Quote (exact) | Source | Class |
|---|---|---|---|
| 1 | "the order in hand that you see as on, say, 31st March 2026, expect around 85% to 90% of that to be executed in FY'26-'27." | Concall_May_2026_Transcript.pdf p.8 (Ghai, CFO) | (a) guidance with a period (FY27). No backlog figure named. |
| 2 | "at least I can give you a range that we expect in the range where we are in this year plus minus 5%. So we will be for the next year and the year after we expect a plus 5% to 8% kind of a compounded growth in the top line." | Concall_Feb_2026_Transcript.pdf p.11 (Ghai) | (a) FY27, then FY28 |
| 3 | "we expect between INR 300 crores to INR 320 crores as the average range quarterly top line." | Concall_Feb_2026_Transcript.pdf p.16 (Ghai) | (a) "post restructuring", period loose |
| 4 | "effectively an EBITDA of 10% plus is what we are expecting going forward." | Concall_Feb_2026_Transcript.pdf p.11 (Ghai) | (b) aspiration without a period |
| 5 | "we expect a good 30% plus gross margin number" | Concall_Feb_2026_Transcript.pdf p.11 (Ghai) | (b) aspiration without a period |
| 6 | "at par if not more at least but at least at par for the for the future years. So, I would not I can't give you a range or something on the guidance for the future in terms of margins" | Concall_May_2026_Transcript.pdf p.15 (Ghai); the FY26 11% base is "at the entity level including discontinued operations of Durgapur perimeter" | (b) aspiration without a period |
| 7 | "that I expect around 60% coming from core services." ... "would go up to 80% post two years. So 80% sustainably would be the volume mix" | Concall_Feb_2026_Transcript.pdf p.10 (Ghai) | 60% is (a) two years; 80% is (b) no firm period |
| 8 | "The realistic timelines, well within 12 months is definitely there." and "within 12 months from, say, 31st March of 2026 is definitely the expectation." | Concall_May_2026_Transcript.pdf p.13 | (a) Durgapur close, by 31 Mar 2027 |
| 9 | "over the next 18 months, I would say, we would be in a very good shape to have developed an alternate supply chain" | Concall_May_2026_Transcript.pdf p.15 | (a) loosely dated (about Nov 2027); the Jul 2026 meets say "very soon" (B05) |
| 10 | "India's installed base ... would be about INR 2,500 crores or something like that, which comprises of the assets which are both GEPIL assets as well as non-GEPIL assets." and "it's a yearly opportunity which is an averaged out" | Concall_Feb_2026_Transcript.pdf p.7 and p.14 (Bhatla) | (c) market capability, not a forecast |
| 11 | "Market size, it will be about INR3,500 crores to INR4,000 crores" ... and "currently we have roughly 18% of the market share there" | Concall_May_2026_Transcript.pdf p.8 and p.9 | (c) market size, no definition |
| 12 | "Our endeavor is to grow that market share, stabilize for the next year or so" | Concall_May_2026_Transcript.pdf p.9 | (b) aspiration |
| 13 | "Company has recommended a final dividend of 70% i.e. H7/- (Rupees Seven Only) per equity share" | Annual_Report_2026.pdf (Board report); Note 61 p.204 gives INR M 470.6 | declared item, not forward guidance |
| 14 | "enhancement of the existing enabling limit from H4,500 million to H10,000 million" (cash-pool lending) and "Parent Corporate Guarantees aggregating up to ₹16,000 million" | Annual_Report_2026.pdf Notice, p.311 and p.320 | (c) capacity only |
| 15 | Shoaiba order, about Rs 550 Cr over about 2.5 years (Reg 30, 12 Aug 2026) | via report: 05-concall.md, 07-emoat.md | an order notice, not guidance |

Comment: guidance is soft or management-defined. The guider, CFO Ghai, ceased on 13 May 2026 (B05).

### 4. CONCENTRATION
- Customer: "Top two customers accounts for 38.6% approximately (previous year two customers accounts for 34.8% approximately) of Company's total revenue from operation." (Annual_Report_2026.pdf p.176, Note 35). Top single customer share and customer names: NOT DISCLOSED.
- Geography: "India  12,343.2  10,109.3 / Outside India  349.5  361.7 / Total  12,692.7  10,471.0" (p.176, INR M). Outside India is 2.75% in FY26 (B07).
- Product: by nature only: construction contracts 7,640.3, products 4,911.7, services 109.5 (p.176, INR M). Line split (core services, upgrades, FGD, legacy): NOT DISCLOSED. One quarterly statement: "now majority of it, around 55% comes from core services where we have better gross margins." (Concall_Nov_2025_Q2FY26_Transcript.pdf, Ghai; printed page 6 of 15 per B04).
- Joint venture: NTPC GE Power Services revenue INR M 1,111.6 against INR M 265.1 (Annual_Report_2026.pdf p.181, Note 36), 8.8% of FY26 revenue (calc, B02).
- Comment: the largest share is a pair of unnamed customers; the single top share is not filed.

### 5. PROMISE LEDGER
(B05, with anchors; dates are call dates.)

| Promise | Made | Status | Evidence anchor |
|---|---|---|---|
| Jaypee settlement concluded in Oct to Dec, "breakeven, 2-4 cr impact" | Q2 FY26 call, 14 Nov 2025 | Delivered | Q3 FY26 call: Rs 25 Cr received, both parties discharged (B05) |
| BHEL Rs 340 Cr collected over 2 to 3 quarters | Q2 FY26 call | Delivered | Q4 FY26 call: Rs 343 Cr in FY26; Results Q2 FY27 note 4: INR M 3,430.6 |
| Core double-digit YoY growth | Q2 FY26 call | Delivered | Q3 call core orders +21%; Q4 call +32% |
| Normalised EBITDA "10% plus" for FY26 | Q3 FY26 call, 17 Feb 2026 | Delivered | Q4 call: 11% entity level (management definition) |
| Further about Rs 125 Cr BHEL cash, total Rs 340 Cr in FY26 | Q3 FY26 call | Delivered | Q4 call: Rs 343 Cr |
| Average quarterly revenue Rs 300 to 320 Cr | Q3 FY26 call | Delivered | Q4 FY26 Rs 316 Cr (call); Q1 FY27 INR M 3,086.9; Q2 FY27 INR M 3,112.3 (Results, revenue from operations) |
| Durgapur NCLT approval within calendar 2026 | Q3 FY26 call | Delivered (sanction); not yet effective | NCLT order 1 Oct 2026 (Results_Q2FY27 p.7) |
| BHEL reversal impact ends 31 Mar 2026, no FY27 repeat | Q4 FY26 call, 12 May 2026 | Delivered | Results Q2 FY27 note 4 lists reversals only in Q2 to Q4 FY26 |
| FY26 11% base, "at par if not more" for FY27 | Q4 FY26 call | Partial | Filed continuing ex other income: Q1 14.5%, Q2 9.8%, H1 12.2% (calc); different basis |
| 85% to 90% of Mar 2026 order in hand executed in FY27 | Q4 FY26 call | Open | FY27 not complete |
| FY27 revenue FY26 level plus or minus 5% | Q3 FY26 call | Open | H1 FY27 INR M 6,199.2 vs 5,672.5, +9.3% (calc, B05) |
| Core services 60% of revenue in two years | Q3 FY26 call | Open | Revenue by line NOT FOUND |
| Alternate supply chain in about 18 months | Q4 FY26 call | Open, wording slipped | "very soon" at Jul 2026 meets (B05) |
| Durgapur effective within calendar 2026 / 12 months of 31 Mar 2026 | Q3 and Q4 FY26 calls | Open | Sanctioned 1 Oct 2026; effectiveness pending |

Comment: the B05 block tallies 7 delivered and 1 partial, but its row table lists 8 Delivered and 1 Partial. The tally and the rows disagree by one. The table above follows the rows; the operator should note the difference. Credibility grade B (B05).

### 6. RESTATED BASES
- Quote: "the figures for the previous periods relating to Demerged business undertaking have been re-presented in the Standalone profit and loss and Statement of cash flows." (Annual_Report_2026.pdf p.194, Note 47(iii)). The same sentence form appears for the Gas and Hydro sales (p.194).
- Comparative as printed in the latest filing: "Profit(+)/Loss(-)  before exceptional items from continuing operations  3,399.0  224.6" (Annual_Report_2026.pdf p.132, INR M, FY26 and FY25).
- The FY25 figure as first reported: "Profit/(loss) before exceptional items and tax from Continuing Operations (380.2)" (Annual_Report_2025.pdf, statement of profit and loss; p.168 per B02). Difference INR M 604.8: Durgapur cost moved to discontinued operations (employee 399.4, other expenses 181.6, depreciation 6.4, materials 17.4) (B02).
- Not restated: the Note 36 related-party FY25 column still includes Gas and Hydro flows (B02). Note 26 FY26 deductions labelled "slump sale" (warranty 185.0, loss orders 137.7) repeat FY25 values to one decimal (B02).
- Quote: "the financial results for the previous periods relating to Demerged business undertaking have been re-presented in the Standalone financial results" (Results_Q2FY27_30Sep2026.ocr.txt, note on the scheme, p.7).
- Comment: FY24 comparatives held from AR25 include Gas and Hydro and are not like for like with FY25 and FY26 continuing figures (B02).

### 7. CORPORATE-ACTION CLAUSES
- Durgapur demerger. Definition of the undertaking: "the demerger and transfer of the Company's Durgapur facility, comprising the business of manufacture and supply of power boiler components, pressure vessels, piping and coal mills for thermal power plants (the "Demerged Undertaking"), as a going concern and on an "as is where is" basis from Company to JSW." (Annual_Report_2026.pdf p.28). Ratio: "10 (Ten) fully paid-up equity shares of H10/- ... of JSW for every 139 (One Hundred Thirty Nine) fully paid-up equity shares of H10/- ... held in the Company" (p.28). Appointed date: "with an appointed date of 1 July, 2025" (p.194, Note 47(iii)). Board approval 18 Sep 2025. Fallback: if demerger is not feasible, transfer "shall take place by way of slump sale" (p.28). Exchange letters: BSE "No Adverse Observations" and NSE "No Objection" dated 01 April 2026 (p.28). Shareholders and creditors approved on 20 Jul 2026; "The NCLT, vide its order dated 1 October, 2026, has sanctioned the Scheme. The Scheme will become effective on fulfilment of the conditions precedent and on filing of the certified copy of the order with the Registrar of Companies." (Results_Q2FY27_30Sep2026.ocr.txt p.7, OCR text, reads cleaner in the standalone note than the consolidated one). Effective date: not yet. Liability allocation clauses and consideration to the company: NOT DISCLOSED in the corpus (the scheme document is absent). Fetch: BSE Reg 30 scheme filing of 18 Sep 2025 and the NCLT order. The held-for-sale block shows "Total equity (548.7)" (p.195).
- Gas sale. "for a lumpsum consideration of H 438.6 million excluding all applicable taxes" to GE Renewable Energy Technologies Private Limited; completed 30 Sep 2024; gain INR M 583.4 (Annual_Report_2026.pdf p.194).
- Hydro sale. "for a lumpsum consideration of H 1/- excluding all applicable taxes" to GE Vernova Hydro Power India Private Limited; completed 31 Mar 2025; net liability INR M 2,978.9, independent valuation negative INR M 609.0, gain INR M 2,369.9 to profit and loss and INR M 609.0 to equity (p.194).
- Cash-pool and guarantee approvals: "The said loan is secured through Parent Corporate Guarantee from GE Vernova Inc., ultimate Parent Company." (Annual_Report_2026.pdf p.315); "Parent Corporate Guarantee from GE Vernova Inc. (Ultimate Parent Company) of H10,000 million, intended to provide credit support in respect of the principal amount proposed to be outstanding under the lending arrangement, with 100% coverage." (p.317). Dates: board 19 Jun 2026; AGM 14 Aug 2026.
- Dividend: final INR 7 per share, record date Friday, 31 July 2026 (Annual_Report_2026.pdf, Board report and Notice).
- Merger, preferential issue, share repurchase: none found in the Annual_Report_2026.txt search or in the stage blocks; not exhaustively searched in the 31 announcements.

### 8. RELATED-PARTY PERIMETER
Source: Annual_Report_2026.pdf Note 36, p.177 to p.183, INR M, FY26 then FY25. The note lists about 90 group entities (p.177 to p.179); those with FY26 transactions:
- Ultimate holding GE Vernova Inc.: corporate guarantee (received, labelled "issued") 7,977.6 vs 28,100.0 (p.182).
- LM Wind Power Blades (India) Private Limited: inter-corporate deposit given 4,500.0 vs nil; interest income on ICD 199.8 vs 20.4; interest expense on borrowings nil vs 117.8; borrowings repaid nil vs 1,019.0; trade payable 56.4 (p.181, p.183).
- Royalty and trademark fee: GE Steam Power Switzerland GmbH 305.1 vs 270.0; GE Vernova Infrastructure Technology LLC 110.1 vs 140.3; GE Vernova Technology GmbH 20.5 vs 28.9; total 435.7 against the P&L line INR M 125.7; gap INR M 310.0 (p.180; B02).
- Other income: GE Vernova (Switzerland) GmbH 188.6 vs nil; GE Vernova Technology GmbH 156.7 vs 77.6; GE Steam Power Switzerland GmbH 106.0 vs 82.2; GE Renewable Technologies 78.7 vs 15.6; Powerstatic Solutions 30.6 vs 8.7; Other 72.5 vs 21.2 (p.180).
- Revenue from operations: GE Power Systems India 74.2 vs 140.8; GE Steam Power, Inc. 72.9 vs 10.5; Powerstatic Solutions 59.2 vs 9.5; GE Steam Power Switzerland 40.1 vs 91.3; GE Energy Switzerland 31.1 vs 82.7; GE Vernova Global Services GmbH 27.4 vs 30.1; GE Hydro France 4.2 vs 548.7; GE Vernova Operations LLC nil vs 273.6; Others 63.8 vs 301.8 (p.180).
- Purchases of materials and components (sum 699.1 FY26): GE Power Sp. z o.o. 71.1; Nexus Controls LLC 182.6; GE Power GmbH 106.1; GE Steam Power UK 68.7; GE Power Systems India 41.6; GE Steam Power Switzerland 96.5; GE Vernova Power Services Romania 55.2; GE Steam Power, Inc. 53.9; Others 23.4 (p.181). Purchases of services: Powerstatic Solutions 239.7 vs 107.0 (p.181).
- Other expense and reimbursement payments: GE Renewable Energy Technologies Private Limited 248.5 vs 0.3; GE Power Systems India 63.8 vs 1.6 (p.180).
- Gratuity payment due to business combination: GE Vernova Hydro Power India 226.2 (p.181). Provident fund: ACC Babcock Staff Provident Fund 169.4 vs 306.0 (p.181).
- Joint venture NTPC GE Power Services: revenue 1,111.6 vs 265.1; other income 19.0; purchases of materials 225.0 vs 60.3; purchase of services 181.1 vs 139.4; receivable 703.0 vs 247.9; advances received 833.0 vs 718.4; payable 70.5 vs 44.9; equity investment 72.0 (p.181 to p.183).
- Subsidiary GE Power Boilers Services Limited: revenue 0.4 (p.182).
- Key management personnel: Puneet Bhatla 48.4 vs 30.9; Aashish Ghai 10.1 vs 5.8; Kamna Tiwari 5.4 vs 5.3; director fees 11.5 (p.182).
- Comment: the continuing-basis FY25 column was not re-presented (B02), so FY25 comparatives mix continuing and sold lines.

### 9. PLEDGE AND SHAREHOLDING
Source: Shareholding_Pattern_screener_Sep2026.csv, a screener-derived table, "NOT the filed BSE shareholding PDF" (row 1 of the file).

| Quarter | Promoters % | FIIs % | DIIs % |
|---|---|---|---|
| Dec 2023 | 68.58 | 0.11 | 3.87 |
| Mar 2024 | 68.58 | 0.25 | 3.50 |
| Jun 2024 | 68.58 | 0.39 | 2.99 |
| Sep 2024 | 68.58 | 0.43 | 2.80 |
| Dec 2024 | 68.58 | 0.85 | 2.80 |
| Mar 2025 | 68.58 | 0.41 | 2.30 |
| Jun 2025 | 68.58 | 0.56 | 0.46 |
| Sep 2025 | 68.58 | 0.11 | 0.40 |
| Dec 2025 | 68.58 | 0.15 | 0.43 |
| Mar 2026 | 68.58 | 1.26 | 1.13 |
| Jun 2026 | 68.58 | 1.17 | 1.05 |
| Sep 2026 | 68.58 | 0.73 | 0.70 |

- Promoter pledge: NOT DISCLOSED. The CSV has no pledge row, and the Annual_Report_2026.pdf corporate governance table (p.114) has no pledge column. The only "pledged" text in the AR is bank deposits pledged against bank guarantees (p.158, p.159). The promoter holding is flat at 68.58% for all 12 quarters.
- Quote: "Promoters 46,102,083 68.58" and "Foreign Institutional Investors 843,602 1.25" (Annual_Report_2026.pdf p.114, 31 Mar 2026); "Equity share by GE Steam Power International BV ... 46,102,083  68.6  46,102,083  68.6 0%" (p.160, Note 19(e)).
- Institutional holding, latest (Sep 2026, screener): FIIs 0.73%, DIIs 0.70%. The AR categories at 31 Mar 2026 differ from the screener ones (Mutual Funds 0.15%, Financial Institutions/Banks 0.03%, Insurance 0.32%, FII 1.25%, p.114), and the two sets are not reconciled.
- Comment: the filed pattern with pledge detail must come from BSE (research brief item 2).

### 10. VERIFICATION
Documents quoted in this annex, with dates:
- Annual_Report_2026.pdf (FY2025-26; accounts approved 11 May 2026; Notice for the AGM of 14 Aug 2026): pages 28, 114, 132, 158, 159, 160, 176 to 183, 194, 195, 204, 311, 315, 317, 320.
- Annual_Report_2025.pdf (FY2024-25): statement of profit and loss comparative (p.168 per B02).
- Results_Q2FY27_30Sep2026.pdf and Results_Q2FY27_30Sep2026.ocr.txt (letter 13 Nov 2026): pages 3, 7, 15.
- Concall_Nov_2025_Q2FY26_Transcript.pdf (14 Nov 2025), Concall_Feb_2026_Transcript.pdf (17 Feb 2026), Concall_May_2026_Transcript.pdf (12 May 2026).
- Shareholding_Pattern_screener_Sep2026.csv (read 2026-11-15 via Chrome; screener-derived).
- Quoted via stage reports, source page not re-opened: Investor_Presentation_Q4FY26_2026-05-11.pdf (11 May 2026) p.8 and p.10; Reg 30 filing of 12 Aug 2026 (Shoaiba) and Reg 30 filing of 13 Mar 2026 (CFO resignation).
- Blocks and verifier reports consulted: B00 to B09, B12a to B12d, confidence.yaml, and reports 02, 03, 04, 05, 07, 08, 09 with their appended errata.

CORPUS COMMIT HASH: e80effccab4dc0301c83118e758949579cc0c351

---

```yaml
stage: B09b-dossier
company: "GVPIL"
run_date: "2026-11-15"
model: claude-sonnet-5-5
status: complete
corpus_verdict: "CORPUS GAPPED-FRESHNESS"
corpus_gaps:
  - document: "Q2 FY27 earnings-call transcript (call 16 Nov 2026)"
    expected_source: "BSE"
    kind: "freshness-pair"
  - document: "Filed BSE shareholding pattern with promoter pledge detail"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "AGM 14 Aug 2026 voting results, Items 8, 9, 10"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "Durgapur scheme document (consideration, liability allocation)"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "Q2 FY27 investor presentation"
    expected_source: "company IR page"
    kind: "findable-missing"
  - document: "Screener Profit and Loss, Quarters, Balance Sheet, Cash Flow sheets (exported empty)"
    expected_source: "company IR page"
    kind: "findable-missing"
  - document: "Current BHEL concall (none on BSE in last 12 months)"
    expected_source: "BSE"
    kind: "plausibly-nonexistent"
  - document: "Jaypee Bina and Nigrie FGD termination filing"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "Broker or research notes"
    expected_source: "rating agency site"
    kind: "plausibly-nonexistent"
archetypes:
  - line: "Legacy project lines (FGD equipment, new build)"
    archetype: "Order-book business (EPC/defence/capital goods)"
  - line: "Core services (spares, repairs, upgrades)"
    archetype: "Order-book business (EPC/defence/capital goods), short-cycle form; nearest library fit"
transition:
  - line: "Entity mix shift to core services"
    from_tier: "R1 COMMODITY PRICE-TAKER"
    to_tier: "R3 VALUE-ADDED / SPEC'D SUPPLIER (claimed; two-rung leap, operator rules R2 or R3)"
    engine: "Loss-making FGD and new-build revenue and Durgapur cost run off while core services intake grows; materials 67.3% to 60.2% and employee cost 18.5% to 14.5% of revenue"
    proof_gate: "Continuing EBITDA margin ex other income and ex reversals at or above 11% in Q3 FY27 and Q4 FY27, plus FY27 core intake above Rs 734 Cr and services backlog above Rs 1,218 Cr at 31 Mar 2027"
    recognition_gap: "Open question: does the TO state already appear reflected in market pricing? Resolved at Stage 11 via the PE gap"
    ugliness: "ARTIFACT-OF-CLIMB"
    transition_falsifier: "Second quarter under 10% margin ex other income with no named mix reason; core intake below prior-year quarter or services backlog under Rs 1,124 Cr; cost of materials above 67% of revenue after Durgapur supply terms start"
dominant_variables:
  - "Core services order intake and services backlog"
  - "Continuing EBITDA margin ex other income and ex reversals"
  - "Durgapur demerger effectiveness and post-demerger supply terms"
  - "Cash quality and group deposit exposure (CFO ex deposit vs PAT, ICD balance and guarantee cover)"
business_falsifier: "Group-sourced income becoming the main source of profit (INR M 851.9 is 25.1% of FY26 profit before exceptional items), withdrawal of the parent IP licence, India mandate or guarantees behind INR M 16,000 of bank capacity, or a filed line split showing core services well under the 55% stated for Q2 FY26"
mental_model_status: "DRAFT - PENDING OPERATOR SIGN-OFF"
fragility:
  variable_count: 6
  verifiability_ratio: "4 of 6 externally observable"
  single_point_failure: "Parent guarantee and bank-line dependence (INR M 16,000 needed; banks require GE Vernova majority ownership)"
  fragility_verdict: "MODERATE"
candidate_count: 7
second_order:
  chains_drafted: 2
  pending_live_links: 2
  confirm_by_observations: 2
research_brief_items: 17
plain_summary_points: 15
annex:
  present: true
  questions_answered: 10
  corpus_commit_hash: "e80effccab4dc0301c83118e758949579cc0c351"
```
