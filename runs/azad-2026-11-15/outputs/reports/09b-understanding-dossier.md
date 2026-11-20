# Halt 1 Understanding Dossier: Azad Engineering Ltd (AZAD), run 2026-11-15

Stage 09b, model claude-sonnet-5-5. Assembly from committed blocks B00 to B09, verifier blocks B12a to B12d, conflicts.yaml, confidence.yaml and B13-lite. Units: ₹ Cr unless stated. The filings print INR million (Mn); ₹1 Cr = ₹10 Mn, and filing figures show the Mn unit. Settled figures from conflicts.yaml govern; unresolved ones are named as open items. Verifier A source-fidelity findings apply: the consolidated 5% USD sensitivity is ₹104.07 Mn (Annual_Report_2026.pdf [page 245]), and standalone FY26 operating cash flow sits on [page 123]. This file assembles understanding. It states no price view and no decision.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

Inventory only. Source: B00-inputs, B00-intake. The intake list held 54 files (B00).

**1. Concalls.**

| Quarter | File | Call date (from page 2 header) |
|---|---|---|
| Q4 FY26 | AZAD_Q4FY26_concall_transcript_2026-05-22.pdf | 2026-05-16 (filed 2026-05-22) |
| Q1 FY27 | AZAD_Q1FY27_concall_transcript_2026-08-14.pdf | 2026-08-08 (filed 2026-08-14) |
| Q2 FY27 | AZAD_Q2FY27_concall_transcript_2026-11-14.pdf | 2026-11-07 (cover letter misprints 2025; filed 2026-11-14) |

Held but preserved, never consumed: Q2 FY26 (inputs/other/AZAD_Q2FY26_concall_transcript_2025-11-08.pdf, call 2025-11-03) and Q3 FY26 (inputs/other/AZAD_Q3FY26_concall_transcript_2026-02-20.pdf, call 2026-02-14) (B00-intake). Peer calls: MTARTECH four (files dated 2026-02-05, 2026-05-20, 2026-08-06, 2026-11-06), UNIMECH four (2026-05-04, 2026-06-03, 2026-08-08, 2026-10-31), PTCIL one (2023-06-09, stale) (B00). The most recent quarter covered is Q2 FY27, quarter ended 2026-09-30. Run date is 2026-11-15. The Q2 FY27 results were filed 2026-11-06. The next quarter, Q3 FY27, reported last year on 2026-02-13 (Q3 FY26 results, B00-intake), so no newer Azad quarter has plausibly reported and no transcript is absent for that reason.

**2. Annual reports.** Annual_Report_2025.pdf is FY2024-25 (cover letter 2025-09-08, 42nd AGM). Annual_Report_2026.pdf is FY2025-26 (cover letter 2026-09-07, 43rd AGM) (B00-intake). The latest completed FY is present. Fewer than three are held (two). FY21 to FY23 financials come from the prospectus and FY24 from AR2025, so the six-year Gate 0 series is complete (B01).

**3. Results filings.** Q2 FY27 unaudited, board date 2026-11-06 (AZAD_Q2FY27_results_2026-11-06.pdf, with H1 cash flow and balance sheet). Q1 FY27 unaudited, 2026-08-07. Q4 FY26 audited, 2026-05-15. The Q3 FY26 results (board 2026-02-13) sit in announcements/ (B00). The latest results filing (September 2026) is two quarters past the latest AR (March 2026): Q1 FY27 and Q2 FY27. Q1 filings carry no cash flow statement (B01).

**4. Investor presentations.** AZAD_Q2FY27_investor_presentation_2026-11-06.pdf (letter 2026-11-05) is the latest. AZAD_Q1FY27_investor_presentation_2026-08-07.pdf is the prior one (B00-intake).

**5. Research and rating.** AZAD_CARE_rating_rationale_2026-06-22.pdf (CARE press release, FY26 audited basis). A CARE rating letter dated 2026-06-16 sits in inputs/other/. research/ holds nothing: no broker note is held (B00).

**6. Corporate actions.** Twenty-five Reg 30 filings in announcements/, 2025-11-18 to 2026-11-07 (B00): orders and agreements (Pratt & Whitney Canada 2025-11-18, Mitsubishi Heavy Industries 2026-03-26, Nuovo Pignone amendment 2026-04-23, BHEL rate contract 2026-10-12); facility news (press release 2026-04-23, GE Vernova lean facilities 2026-09-28); the first indigenous turbojet delivery (2026-07-22); QIP monitoring agency reports (2026-02-14, 2026-05-13, 2026-11-06); ESOP grant (2026-05-12); management and auditor changes (2025-11-28, 2025-11-29, 2026-01-22, 2026-05-12, 2026-09-30); a GST penalty order (2026-03-25); four earnings-call recording notices; the Q3 FY26 results; AGM notice, BRSR and AGM outcome (2026-09-07 to 2026-09-29). The Sep 2026 shareholding pattern is held as NSE XBRL and a text rendering. The RHP (2023-12-14), the Prospectus (2023-12-23) and the DRHP (2023-09-29, in other/) are held.

**7. Freshness pair check.** B00 freshness_verdict is FRESHNESS PAIRS OK. All four pairs PASS: results to same-quarter concall (Q2 FY27 results, Q2 FY27 concall held); rating bulletin to full rationale (held); SEBI order to order text (no SEBI order found in the corpus; the 2026-03-25 filing is a GST penalty order); AR not older than latest audited annual results (Q4 FY26 audited results, FY2025-26 AR held). No failed pair.

Input gaps repeated from B00.input_gaps, so the operator sees the full list. The EMPTY-FOLDER CONFIRMATION was suppressed by the /step1 autonomy contract (standing answer: continue with the gaps):
- research/ is empty. No broker notes. Non-anchored source only; no effect on anchored evidence.
- Five screener formula sheets are absent (Profit & Loss, Quarters, Balance Sheet, Cash Flow, Customization). screener-Data_Sheet.csv is populated and carries the raw values.
- Peer concalls: 9 of 12 held. PTCIL has one transcript, dated June 2023 (stale). PTC Industries files no transcripts on BSE or NSE; tried BSE, NSE, ptcil.com, screener.
- The QIP placement document (2025) is not collected. The monitoring agency reports are held in announcements/.
- The collector warnings on shareholding/, results/ and rating/ were repaired at Step F (Sep 2026 pattern, three results filings, CARE rationale fetched).
- annual-report/ holds two ARs. FY2025-26 is the AR of record. FY2024-25 is a prior-year reference.
- Stage 8 (promoter) and stage 9 (market) are status partial because web searches were skipped or blocked (B08, B09). Stages 6 and 7 stalled once on a stream timeout and were resumed; both completed.
- The EY industry report is not held; only the prospectus extract and the Q2 FY27 deck slides carry it (B09).

**8. Verdict line.**

CORPUS GAPPED: (a) research/ broker notes, expected source operator-supplied from broker platforms, findable-missing, non-anchored; (b) five screener formula sheets (Profit & Loss, Quarters, Balance Sheet, Cash Flow, Customization), expected source the screener.in export re-saved by the operator, findable-missing; (c) QIP placement document of March 2025, expected source BSE, findable-missing; (d) shareholding patterns for Dec 2025, Mar 2026 and the other quarters of the twelve-quarter history, expected source BSE, findable-missing; (e) peer financials for MTAR, Unimech and PTC Industries (Gate 0 M2, M5, M9 scored 0), expected source BSE, findable-missing; (f) PTC Industries current-period transcripts, expected source company IR page, plausibly-nonexistent because the company files none on BSE or NSE, which is itself a data point on peer opacity; (g) a Q1 FY27 cash flow statement, expected source BSE, plausibly-nonexistent because the company files cash flow statements for the half year only.

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT - PENDING OPERATOR SIGN-OFF**

This is a transition thesis drafted from committed evidence. It is stress-tested live in claude.ai before the operator decides. The company-memory record of July 2026 stands as of its run and is not re-derived here.

### PART A: THE FROM STATE

**A1. Archetype.**
- Energy and oil and gas line (81.5% of FY26 standalone revenue, B04): Build-to-spec component maker. Drivers are the customer capex cycle, design-win pipeline, content per unit and input-cost pass-through. Evidence: parts qualified per component over 30 to 48 months under 3 to 10 year OEM contracts (B04).
- Aerospace and defence line (17.2%, B04): Build-to-spec component maker at an earlier stage. Engine programmes with Rolls-Royce, Pratt & Whitney Canada and Safran are in qualification and had not reached production (B05, B07).

**A2. The simple analogy.** Azad is a specialist machine shop that cuts the blades inside power turbines and jet engines. The maker of the turbine hands over a drawing. Azad cuts the part to it. The turbine maker then spends years testing the part, so it rarely changes supplier. Azad now runs six factories built for single customers. They are finished, but the parts inside are still being approved, so the money spent on them has not come back yet (B04, B05).

### PART B: THE TRANSITION

**B1. FROM to TO (QUALITY LADDER).**
- Energy and oil and gas line, including the hot-section work: FROM R3 (value-added, spec'd supplier), sitting low on the rung. Pricing power and switching costs meet R3 (B04). The ROCE leg does not: the six-year median ROCE is 14.95% (B01), FY26 statutory ROCE 11.5% (B01) and adjusted ROCE 15.3% (B03), which is R2 territory. TO R4 (franchise, share-of-wallet leader): customers capture dedicated plants and Azad holds under 2% of their wallet (B04, B09), so a repeat-economics runway exists on paper. Durable ROCE of 25% to 30% is not evidenced. One rung, inside the rung-jump base rate.
- Aerospace and defence line: FROM R2 (qualified part families, durable pricing power unproven). TO R3 on production acceptance at Rolls-Royce, Pratt & Whitney Canada and Safran. One rung.

**B2. The engine.** Two things change physically.
1. Six dedicated plants (44,800 sq m, six of eight planned, B04, B05) move from built to billing as delta qualifications clear. Management says throughput starts Q3 FY27, revenue ramps in Q4 FY27 and the full ramp lands in Q2 FY28, for an annual run rate above ₹1,300 Cr by end FY28 against FY26 revenue of ₹602.98 Cr (B05, B09). That path needs about 9.3% sequential growth for six quarters; Q1 and Q2 FY27 delivered 8.3% and 10.1% (B04, B05).
2. Mix shifts into single-source and higher-value work: the Mitsubishi Heavy Industries hot-section nozzle vane contract (eight-year single source, facility due about March to April 2027) and aero engine airfoils (B05, B07). The mechanism is parts that no second supplier holds, not volume alone.

The ugly optic this engine hides: operating cash flow of ₹(43.62) Cr in H1 FY27 (B01), ROCE diluted by QIP cash and unfinished plant (B01), and EBIT that lags EBITDA because depreciation rose 89% (B04).

**B3. The proof gate.** The gate fires only when both legs hold in the same reporting cycle.
- Leg 1, revenue: Q3 FY27 consolidated revenue from operations at least 5% above Q2's ₹190.94 Cr (₹1,909.35 Mn), and H2 FY27 at or above ₹390.19 Cr (₹3,901.85 Mn). Sequential growth under 5% is the first sign the ramp failed (B04, B13-lite).
- Leg 2, cash: FY27 consolidated operating cash flow above zero before bill discounting, factoring and the USD 4.5 Mn OEM advance, with September 2026 inventory of ₹427.35 Cr (₹4,273.54 Mn) falling and the ₹72 Cr work in progress invoiced (B04, B05, B13-lite).
- Read dates: Q3 FY27 results about February 2027 (Leg 1); Q4 FY27 audited results about May 2027 (Leg 2). Until both fire, the transition is narrative and FTTCP tests it at /fttcp.

**B4. The recognition gap (to be resolved at Stage 11).** Open question: does the market already reflect the R4 state for Azad, the TO rung of the energy line? This dossier does not conclude. Stage 11 confirms or denies it through the PE gap between the current PE and the PE the R4 rung implies. If the TO state is already reflected, the re-rating engine is gone and only earnings growth remains. No number, no conclusion appears here.

**B5. The ugliness test.** Draft classification, split by leg, with the operator to rule.
- Returns and depreciation optic: ARTIFACT-OF-CLIMB. ROCE fell from 18.3% (FY24) to 8.7% (FY25) and 11.5% (FY26) as ₹700 Cr of QIP cash and ₹256.68 Cr of CWIP sat in capital before earning (B01). CWIP fell from ₹256.68 Cr to ₹212.49 Cr in H1 FY27 as plant entered service (B01).
- Working-capital and cash optic: held open between ARTIFACT-OF-CLIMB and STRUCTURAL-FEATURE. B13-lite records the cash determination as INDETERMINATE. Reading A (climb): CARE ties the inventory build to development parts and three new dedicated units and expects it to normalise once serial production starts (B13-lite, CARE rationale 2026-06-22 [page 3]). Reading B (structural): revenue-basis working-capital days rose from 147 (FY21) to 336 (FY26), most of the rise before the dedicated plants existed, and operating cash flow was negative in FY23, FY24 and FY26 (B01); the annual report calls working capital 'structural to the business' (B03). The one observation that separates them is Leg 2 of the proof gate.

**B6. The transition falsifier.** Any one of these kills the arrow (B04, B05, B07, B13-lite):
- Q3 FY27 consolidated revenue flat on Q2's ₹190.94 Cr, or sequential growth under 5%.
- No Rolls-Royce qualification acceptance by Q4 FY27 after the batch due in Q2 FY27 slipped.
- FY27 operating cash flow at or below zero, or positive only through bill discounting, factoring or the OEM advance.
- A new equity raise while operating cash flow is negative.

### PART C: WHAT THE MODEL WATCHES

**C1. Dominant variables** (these become the Role 5.5 tracker signals).
1. Dedicated-plant revenue ramp. State: Q2 FY27 consolidated revenue ₹190.94 Cr, +10.1% sequential; ramp date slipped from Q3 to Q4 FY27 between August and November; management declined to say how many customers remain in delta qualification (B05, B12b).
2. Cash conversion on one defined basis. State: H1 FY27 operating cash flow ₹(43.62) Cr against ₹(75.89) Cr a year earlier; days stand at 344 (CARE), 244 (company), 336 and 369 (run calculation) and about 200 (management goal), none comparable (B01, B04, B05).
3. End demand from gas turbine makers. State: GE Vernova gas equipment backlog plus slot reservations 122 GW at Q3 2026, an outside read; gas turbine demand cannot be tested from the peer set (B06, B09).
4. Qualification acceptance in the higher-value lines. State: Rolls-Royce first batch undelivered on 2026-11-07; MHI hot-section facility not built; second GTRE engine pending (B05, B07).

**C2. What the model rejects.** Market size questions: the market does not bind. Azad holds about 2.25% of a serviceable market and needs 4.4% at FY29, so conversion and capacity bind, not demand (B09). Management's ₹343,000 Cr market claim is 4.15 times the conservative figure and rests on customer revenue, so it is noise (B09). The ₹6,500 Cr order book headline is noise until the delta-qualification count and the executable share are stated; management called it 'not order backlog' in November (B05). The rupee lift, the Saudi plan and Phase 2 land do not decide the climb inside twelve months (B05, B07).

**C3. The business falsifier.** Evidence that forces a re-declaration of the FROM business, kept apart from B6: disclosure that the dedicated plants run on customer-owned, cost-plus or captive terms, or that the job work line (19.8% of revenue, +71.7%, B04) is conversion of customer-supplied material. Either would move Azad from a build-to-spec maker with pricing power to an outsourcing partner with capacity fill and contract stickiness as the drivers. A margin drop when the ₹72 Cr work in progress is invoiced would show part of the 37.5% EBITDA margin sits in inventory (B05, B07). A top customer at or above 20% (18.64% now) or a top five at or above 65% (47.02% now) would also force re-declaration (B03, B04).

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

Draft per the shared spec in prompts/13-synthesis-pipeline.md. Stage 13's copy is the final version. Sourced from B03, B04, B05, B06, B07 and B09.

Azad Engineering makes precision metal parts to its customers' drawings in Hyderabad (B04). Most of the parts are airfoils and other rotating and stationary hardware for gas, steam and nuclear turbines and for aircraft engines (B09). Energy and oil and gas parts made 81.5% of FY26 standalone revenue, aerospace and defence parts 17.2%, and other items 1.35% (B04). Sale of products was 78.8% of FY26 consolidated revenue and job work billed as a service was 19.8%; job work grew 71.7%, and the run did not establish who owns the material in that work (B04). A turbine maker cannot easily replace these parts, because each part is qualified for one engine or turbine over 30 to 48 months, and a new supplier must repeat that process (B04). The customers are a short list of global makers: GE Vernova, Siemens Energy, Mitsubishi Heavy Industries, Baker Hughes and BHEL in energy, and Rolls-Royce, Pratt & Whitney Canada and Safran still qualifying in aero engines (B05, B03). The top customer took 18.64% of FY26 revenue, the top five about 47.02%, and two customers sit at or above 10%; their names are not in the corpus (B03, B04). Six plants are built for single customers, three of them for GE Vernova, which is 50.9% of dedicated plant area (B07). Customers order under contracts of 3 to 10 years, pay in foreign currency, and take 88% to 93% of output abroad (B04, B09). Present demand comes from gas turbine orders. The signal is the GE Vernova gas equipment backlog plus slot reservations at 122 GW in Q3 2026, read beside Siemens Energy Gas Services orders and backlog and Mitsubishi Heavy Industries gas turbine orders (B09). The ₹6,500 Cr order book is management's own estimate, and in November management said it is not an order backlog (B05). Demand should grow on four lines that outside sources can check: the Mitsubishi hot-section facility, due about March to April 2027 under an eight-year single source contract; Rolls-Royce, Pratt & Whitney Canada and Safran qualification acceptance and production orders; a GTRE ATGG engine production order with the Ministry of Defence indigenisation policy; and BHEL and domestic thermal and nuclear orders, which lifted the domestic share to 12% of H1 FY27 revenue from 6.1% (B05, B09). Howmet Engine Products revenue, +33% to USD 1,451 Mn in Q3 2026, is the peer read on whether engine hardware stays short of capacity, and the USD/INR reference rate sets the rupee value of each export invoice (B09). The market does not bind the climb; conversion and capacity do (B09). The moat sits in the energy airfoil line, where qualification lock-in scores strong on four filed agreements (B07, B12c). That lock-in is strong per part and weak per customer, because management puts wallet share under 2% and the dedicated plants raise Azad's dependence on one maker as much as they raise that maker's cost of switching (B04, B07). The hot-section and aero engine lines have no moat yet: the hot-section facility is not built and the Rolls-Royce batch was undelivered on 2026-11-07 (B05, B07). Job work and oil and gas show no moat evidence in the run (B07). The Emerging Moat scan scores 12.0 at the floor of the MODEST band, and Verifier C recomputes 13.0 with the same class (B07, B12c).

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. Verticals framed

**Vertical 1: Dedicated-plant revenue ramp (C1.1).**
- Corpus establishes: six of eight plants built, 44,800 sq m (B04); Q1 +8.3% and Q2 +10.1% sequential, ramp date moved Q3 to Q4 FY27 (B05); CWIP down from ₹256.68 Cr to ₹212.49 Cr (B01); depreciation +88.7% and further steps in Q3 and Q4 (B04); employee cost +23.7% quarter on quarter against revenue +10.1% (B05); the Aug 'full throttle' and Nov 'spindles just started' reversal (B12b).
- Cannot establish: customers in delta qualification, revenue held behind each, per-plant utilisation, take-or-pay or minimum volume terms, order values for MHI, Baker Hughes Amendment 3 and ATGG (B04, B07, B12b).
- Deciding questions: (1) How many customers remain in delta qualification, and when does each clear? (2) What do the dedicated-plant contracts say on minimum volume and termination? (3) Is Q3 FY27 revenue at least 5% above ₹190.94 Cr?

**Vertical 2: Cash conversion (C1.2).**
- Corpus establishes: FY26 operating cash flow ₹(118.97) Cr; H1 FY27 ₹(43.62) Cr; inventory ₹427.35 Cr; receivables +₹83.75 Cr and inventory +₹98.24 Cr in H1 (B01, B04, B05); no factoring, discounting or recourse wording in the AR (B02, B03); promised sources are bill discounting from Q4 FY27 (recourse not stated), a USD 4.5 Mn advance from one OEM, and a ₹100 Cr GST credit by H1 FY28 (B05); MTAR's fall from 260 to 50 days came from customer terms and advances, and MTAR calls 50 days not sustainable (B06, B12d).
- Cannot establish: working-capital days on one defined basis at H1 FY27; the composition of the ₹110.25 Cr government balance; whether discounting has begun; the net debt gap (₹474.07 Cr by calculation against ₹423.8 Cr from management) (B04, B05, conflicts.yaml).
- Deciding questions: (1) What is the definition of the 244 days, and how does it map to CARE's 344? (2) What is the recourse term of the ICICI Bank and DP World lines and where do they show in the cash flow statement? (3) Is FY27 operating cash flow positive before discounting, factoring and the advance?

**Vertical 3: End demand from gas turbine makers (C1.3).**
- Corpus establishes: GE Vernova holds 3 of 6 dedicated plants; energy and oil and gas are 81.5% of revenue; a 25% growth guide with customer schedules said to be firm (B05, B07); no peer is a gas turbine OEM supplier (B06); a 2023 PTC Industries meeting calls industrial gas turbines an evolving market with shorter approvals (B12d); the third-party energy forecast pre-dates the 2025-26 order boom (B09).
- Cannot establish: gas turbine demand from the peer set, the outsourced airfoil spend, the Siemens Energy and MHI backlog from primary releases (B06, B09).
- Deciding questions: (1) Does the GE Vernova backlog plus slot reservations keep rising? (2) Do Siemens Energy and MHI show the same order intake? (3) Do the OEMs state supplier capacity as a constraint?

**Vertical 4: Qualification acceptance in higher-value lines (C1.4).**
- Corpus establishes: MHI eight-year single-source contract filed 2026-03-26; facility 7 to 8 months from August 2026; Rolls-Royce first batch promised H2, then within Q2, then 'very soon', still undelivered 2026-11-07; first indigenous turbojet delivered 2026-07-22 with the second engine pending; Safran is an MOU only (B05, B07).
- Cannot establish: contract values, margins by component, civil against defence split of aerospace and defence (B04, B07).
- Deciding questions: (1) Is the Rolls-Royce batch accepted by Q4 FY27? (2) Is the MHI facility built and qualified by about April 2027? (3) Does a GTRE production order state count and value?

### 4b. Candidate signal table

Unverified. Verification and tracker writes happen at Role 5.5 in claude.ai. Candidates are the eight from B09 (candidate_count 8).

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| GE Vernova gas equipment backlog plus slot reservations (122 GW at Q3 2026) | Backlog plus reservations falls in two consecutive quarters | Quarterly | SEC EDGAR 8-K and 10-Q, earnings transcript (Registry Type 3) |
| Siemens Energy Gas Services orders and backlog | Gas Services order intake falls year on year in two consecutive quarters | Quarterly | Siemens Energy quarterly release and half-year report, IR page (Registry Type 3) |
| MHI gas turbine orders and the hot-section facility milestone | Facility slips past FY28, or gas turbine order intake falls year on year | Quarterly | MHI TSE filings and IR library, English releases (Registry Type 3) |
| Rolls-Royce, Pratt & Whitney Canada and Safran qualification acceptance and production orders | No Rolls-Royce acceptance by Q4 FY27, or a fourth date slip | Event-Driven | Rolls-Royce half-year report, RTX 10-Q, Safran half-year report, Azad exchange filings (Registry Types 3 and 1) |
| Howmet Engine Products revenue and gas turbine commentary | Engine Products growth turns negative year on year, or commentary moves from capacity-constrained to demand-constrained | Quarterly | SEC EDGAR 10-Q and earnings transcript (Registry Type 3) |
| GTRE ATGG production order and MoD indigenisation policy | No production order with count and value by FY28, or a test failure | Event-Driven | PIB releases, Parliament questions (sansad.in), Azad exchange filings (Registry Types 4 and 1) |
| BHEL and domestic thermal and nuclear orders (domestic share 12% of H1 FY27 revenue) | Domestic share falls back toward 6% | Quarterly | BHEL concall transcripts and exchange announcements (Registry Type 1) |
| USD/INR reference rate | A 5% rupee recovery cuts pre-tax profit by ₹10.41 Cr (₹104.07 Mn net long USD sensitivity, Annual_Report_2026.pdf [page 245]) | Monthly | RBI / FBIL reference rate (Registry Type 7) |

### 4c. Fragility read

- variable_count: 6 external variables must go right for the bull case: (1) gas turbine makers keep ordering; (2) delta qualifications clear on schedule; (3) customers grant advances or shorter terms; (4) Rolls-Royce, Pratt & Whitney Canada and Safran accept qualification parts; (5) the Mitsubishi hot-section facility is built and qualified; (6) USD/INR stays supportive.
- verifiability_ratio: 3 of 6 externally observable. Variables 1, 4 (partly, through OEM reports and Azad filings) and 6 are observable. Variables 2, 3 and 5 are company-narrated only (B05, B06, B07, B09).
- single_point_failure: the dedicated-plant revenue ramp. A Q3 FY27 print flat on Q2 alone shows plants built but not billing, the reading where Azad funds capacity its customers control (B13-lite falsification line, B07).
- fragility_verdict: FRAGILE. One kill-switch exists and half the variables are company-narrated.

### 4d. Research brief (claude.ai work order)

Live-web work the corpus cannot do. Items 1 and 2 are the PENDING LIVE VERIFICATION links raised by the Section 4e chains. Items 3 to 5 are the chains still to be built to the Rule F floor.

1. PENDING LIVE VERIFICATION, Chain 1 link 2: open the GE Vernova Q3 2026 Form 10-Q and Q3 2026 earnings transcript on SEC EDGAR, and the Siemens Energy and Mitsubishi Heavy Industries primary Q3 2026 releases. Read supplier-capacity language, gas backlog and slot reservations, and who accepts and pays for delta-qualified parts.
2. PENDING LIVE VERIFICATION, Chain 2 link 2: open the GE Vernova Q3 2026 Form 10-Q note on supplier finance and advances to suppliers, and the Siemens Energy fiscal 2026 annual report note on customer prepayments, to learn which OEMs pay supplier advances and on what terms. Identify the unnamed OEM that agreed to a 50% advance (USD 4.5 Mn) from Azad's FY27 exchange filings.
3. Build chain 3: aero engine airfoils, Rolls-Royce batch acceptance and Pratt & Whitney Canada and Safran production orders, with the counterparty read from RTX and Rolls-Royce reports.
4. Build chain 4: the Mitsubishi hot-section facility and single-source economics, with MHI TSE filings.
5. Build chain 5: captive capacity and customer power, GE Vernova holding 3 of 6 plants and the top customer at 18.64% against a 20% line.
6. Customer-health reads from counterparty filings for GE Vernova, Siemens Energy, Mitsubishi Heavy Industries, Baker Hughes and Howmet (B09 skipped the Siemens Energy and MHI primary releases).
7. CARE follow-up: any rating action after 2026-06-22 and the basis of the 344-day working-capital cycle against Azad's 244 (rating agency site).
8. Forum archaeology on the 2025-06-06 block sale of 31,67,702 shares: reason, counterparties and the other parties to the block (BSE bulk deal archive, NSE archive; Trendlyne returned HTTP 405 and Tradebrains HTTP 403) (B08).
9. BSE insider trading disclosures for scrip 544061 and the SEBI orders database, to evidence or clear the SEBI PIT matter named in company memory (B08: NOT FOUND).
10. Policy status: GTRE ATGG programme and MoD indigenisation (PIB, sansad.in), and BHEL rate contract execution.
11. Shareholding patterns for Dec 2025 and Mar 2026 (pledge status), and for Dec 2026 and Mar 2027 after the promoter lock-in on 1,18,27,600 shares ends about December 2026 (BSE, NSE).
12. Writ Petition 18735 of 2024 (Mangampet land, Telangana High Court) and the MCA cost-records notice of 2023-03-17 (MCA21) (B08).
13. Source URL verification: the Business Today and Outlook Business block-deal articles, the azad.in proxy-adviser reports (IiAS and SES, EGM 2025-01-28), and the JUNSHP2025_Q1.pdf pattern read by B08 (B08).
14. Companies Act Schedule II useful life for plant and machinery (7.5 years in the annual report policy table against the 15 years Azad uses) (B03).
15. FBIL reference rate for 2026-11-13, and the Siemens Energy and MHI backlog from primary releases (B09).
16. Industry reports for outsourced airfoil and machined aero engine component spend (IBEF, CRISIL, ICRA, Mordor, Ken, RedSeer; B09 skipped these).
17. QIP placement document of March 2025 (BSE, NSE) to read the use of the ₹156.21 Cr (₹1,562.10 Mn) general corporate purposes bucket (B02, B03).
18. Peer financials for MTAR, Unimech and PTC Industries to score Gate 0 M2, M5 and M9, and any current-period PTC Industries disclosure (B01, B06).

### 4e. Second-order stub (Master Prompt v3.7, Rule F)

Two chains drafted from corpus. Links 1 carry block cites. Links 3 are labelled inference and add no number and no fact.

```
CHAIN 1: Six dedicated plants are built, but the revenue ramp moved to Q4 FY27 and in November spindles had "just started" and Azad was "not seeing revenue today" (B05, B12b)
Link 1 [FILED and CLAIM]: Q2 FY27 consolidated revenue from operations was ₹190.94 Cr (₹1,909.35 Mn), +10.1% sequential; the over 25% FY27 guide needs H2 FY27 consolidated revenue of at least ₹390.19 Cr (₹3,901.85 Mn); inventory stood at ₹427.35 Cr (₹4,273.54 Mn) including ₹72 Cr of work in progress that Azad "can invoice only after customer approval" (B04, B05; Q2 FY27 results [page 10]).
Link 2 [PENDING LIVE VERIFICATION]: who pays, and why now. Counterparty evidence this container cannot reach. Claude web should open the GE Vernova Q3 2026 Form 10-Q and earnings transcript (SEC EDGAR) and the Siemens Energy and Mitsubishi Heavy Industries Q3 2026 primary releases, and read supplier-capacity language and how each OEM accepts delta-qualified parts. No counterparty fact is stated here.
Link 3 [INFERENCE]: GE Vernova holds 3 of the 6 plants, 50.9% of dedicated area (B07). If the plants are customer-captured capacity, the billing date follows the customer's acceptance of delta-qualified parts and its own build slots, not Azad's machine hours, so Q3 revenue can stay flat while machines run. [INFERENCE]: the cost base is already in place (employee cost +23.7% quarter on quarter, depreciation stepping up in Q3 and Q4, B05, B04), so a flat quarter would reach EBIT harder than EBITDA.
Binding constraint: the count of customers still in delta qualification, which management declined to give (B12b); unexecuted capital orders of ₹118.28 Cr (₹1,182.77 Mn, Annual_Report_2026.pdf Note 28(b), B02); ₹75.54 Cr of the QIP capex object unspent with a deadline of 2027-03-31 (B01, B03); Mangampet land under a High Court writ (B03).
Unsaid: no take-or-pay or minimum volume term for the dedicated plants appears anywhere in the corpus (B07); eight planned plants became six without comment (B05); the customs duty contingency of ₹22.09 Cr (₹220.94 Mn, +194%, export obligation certificates pending, no provision) sits in a footnote tied to export volumes under the capacity build (B02 rank 10).
Observation that confirms or breaks this chain, and confirm-by date: Q3 FY27 consolidated revenue from operations at least 5% above ₹190.94 Cr, with the number of customers in delta qualification stated on the call, confirms; flat or under 5% breaks it (B04, B13-lite). Confirm-by: Q3 FY27 results and call, about February 2027.
```

```
CHAIN 2: H1 FY27 consolidated operating cash flow was ₹(43.62) Cr (₹(436.24) Mn), and the promised cash sources are bill discounting lines usable from Q4 FY27 and a USD 4.5 Mn advance from one OEM (B01, B04, B05)
Link 1 [FILED]: the H1 improvement of ₹30.71 Cr (₹307.09 Mn, standalone) came from operating profit and lower tax paid; the working-capital line was 3% worse; receivables rose ₹83.75 Cr (₹837.45 Mn) and inventories ₹98.24 Cr (₹982.41 Mn) in the half (B05, Q2 FY27 results [page 11]). FY26 operating cash flow was ₹(118.97) Cr (B01).
Link 2 [PENDING LIVE VERIFICATION]: who pays, and why now. Claude web should open the GE Vernova Q3 2026 Form 10-Q note on supplier finance and advances to suppliers, and the Siemens Energy fiscal 2026 annual report note on customer prepayments, then identify the OEM that agreed to a 50% advance from Azad's FY27 exchange filings. No counterparty fact is stated here.
Link 3 [INFERENCE]: if Q4 FY27 operating cash flow turns positive, the source is borrowing (discounting, recourse not stated) or one customer's advance, so cash then follows customer bargaining posture, not Azad's discipline. MTAR's fall from 260 to 50 days is credited to customer terms and advances, and MTAR itself calls 50 days not sustainable (B06, B12d). [INFERENCE]: this chain links to Chain 1, because each delta qualification that clears converts work in progress to invoices and is the only source of cash that does not add debt.
Binding constraint: current borrowings of ₹274.66 Cr (₹2,746.58 Mn) against ₹175.69 Cr (₹1,756.92 Mn) six months earlier (B04); interest cover 5.6x against 7.2x and 76.7% floating-rate debt (B02); consolidated net debt of ₹474.07 Cr by calculation against ₹423.8 Cr from management, a gap of about ₹50 Cr unresolved (B04, conflicts.yaml); the chairman's remark that Azad will "go for a QIP" while operating cash flow is negative (B05).
Unsaid: the annual report has no factoring, discounting or recourse wording (B02, B03); the H1 'other financial liabilities' inflow of ₹23.97 Cr (₹239.74 Mn) has no stated content (B05); the ₹110.25 Cr (₹1,102.51 Mn) government balance has no composition (B02, B03); the chairman said the discounting had started while the Whole Time Director said the lines are 'in reserve' (B12b).
Observation that confirms or breaks this chain, and confirm-by date: FY27 consolidated operating cash flow above zero before bill discounting, factoring and the USD 4.5 Mn advance, with discounted receivables shown within borrowings, confirms; zero or below, or positive only through those items, breaks it (B13-lite). Confirm-by: Q4 FY27 audited results with the full-year cash flow statement, about May 2027.
```

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in claude.ai with live web, before Role 2.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. Azad Engineering is a precision parts maker in Hyderabad. It cuts metal parts to its customers' drawings (B04).
2. Most parts are blades and other hardware for turbines. Energy and oil and gas made 81.5% of FY26 standalone revenue (B04).
3. Aerospace and defence made 17.2%. Job work billed as a service was 19.8% of consolidated revenue and grew 71.7%, and the run could not say who owns the material (B04).
4. The customers are a short list of global turbine and engine makers. The top customer took 18.64% of FY26 revenue and the top five about 47.02% (B03).
5. Each part is approved for one customer over 30 to 48 months. That makes the part hard to replace (B04).
6. Demand today comes from gas turbine orders. GE Vernova's gas backlog plus slot reservations stood at 122 GW at Q3 2026 (B09).
7. Demand should grow if the new plants start billing, if hot-section and aero engine parts pass approval, and if domestic orders hold. The market does not limit Azad. Conversion and capacity do (B09).
8. Revenue grew 28.6% in H1 FY27 to ₹363.53 Cr on a consolidated basis (B01).
9. The moat sits in per-part approval in energy airfoils. It is weak per customer, because Azad holds under 2% of customer wallets and six plants serve single customers (B04, B07).
10. The hot-section and aero engine lines have no proof yet. The hot-section factory is unbuilt and the first Rolls-Royce batch was undelivered on 2026-11-07 (B05, B07).
11. The mental model, in draft: a build-to-spec parts maker at rung R3 tries to climb to R4 by turning six dedicated plants into billing and adding single-source hot-section work. The proof gate has not fired.
12. The fragility verdict is FRAGILE. Six outside variables must go right, three are observable, and one switch alone can break the case: plants that are built but not billing (Section 4c).
13. The corpus could not establish the names of the two largest customers, the contract terms of the dedicated plants, the number of customers still in delta qualification, the recourse terms of bill discounting, or working-capital days on one defined basis (B04, B07, B12b). The promoter and market stages are partial because web searches were blocked (B08, B09).
14. The biggest open question is cash. H1 FY27 operating cash flow was ₹(43.62) Cr, and the July falsifier is not cleared (B01).
15. The second open question is whether the market already reflects the climb. Stage 11 answers it through the PE gap. A third open item is a net debt gap of about ₹50 Cr between the run's calculation and management (conflicts.yaml).

---

## SECTION 6: STANDING EXTRACTION ANNEX

Quote-then-comment. Filing figures are INR million (Mn) as printed. Anchors are file name and [page N] marker of the page-marked .txt extraction. Management speaks in ₹ Cr.

### 1. UNITS

> "each of these plants are poised to generate at full utilization and full capacity from INR150 crores to, let's say, about INR180-odd crores" (AZAD_Q1FY27_concall_transcript_2026-08-14.pdf [page 14])

Comment: this is revenue per dedicated plant at full capacity, a basket of parts per plant. No per-part or per-tonne realisation is printed anywhere in the corpus. Revenue per part is NOT DISCLOSED.

> "in excess of 1,700 individual components" (Annual_Report_2026.pdf [page 32])

Comment: a count of qualified components, not a volume. Volume lines (parts delivered a year) are NOT DISCLOSED, so no unit figure can be derived. The revenue lines that exist: Sale of products 4,751.51 and Sale of services 1,193.62 (FY26, INR million, Annual_Report_2026.pdf [page 229]). The pipeline uses Rs 100 of consolidated revenue as its unit (B04).

### 2. SEGMENT CAPITAL AND DEBT

> "Based on the Company's business model, manufacturing high precision and OEM components, have been considered as a single business segment ... there are no separate reportable segments in accordance with the requirements of Ind AS 108" (Annual_Report_2026.pdf [page 236])

> "The company has total segment assets within India. Hence, separate figures have not been furnished" (Annual_Report_2026.pdf [page 237])

Comment: segment assets, liabilities and capital employed are NOT DISCLOSED, because there is one reportable segment. The Q2 FY27 results repeat it: "there is only one primary reportable segment as per Ind AS 108" (AZAD_Q2FY27_results_2026-11-06.pdf [page 12]). Borrowings are unallocated. Consolidated totals, INR million:

| Line | 30 Sep 2026 | 31 Mar 2026 | 31 Mar 2025 |
|---|---|---|---|
| Non-current borrowings | 2,869.67 (Q2 results [page 10]) | 2,809.47 (Q2 results [page 10]; AR2026 [page 191]) | 1,708.65 (AR2026 [page 191]) |
| Current borrowings | 2,746.58 (Q2 results [page 10]) | 1,756.92 (same) | 727.17 (AR2026 [page 191]) |
| Total | 5,616.25 [calc] | 4,566.39 [calc] | 2,435.82 [calc] |

### 3. GUIDANCE VERSUS ASPIRATION

Every forward number below is classified: (a) guidance with a period, (b) aspiration without a period, (c) capacity or capability only.

| # | Quote | Class | Anchor | Comment |
|---|---|---|---|---|
| G1 | "we remain confident in delivering 25% plus top line trajectory, not just for FY '27, but on a multiyear basis" | (a) FY27 and multiyear | AZAD_Q4FY26_concall_transcript_2026-05-22.pdf [page 5] | Reiterated: "we reiterate our long-term annual growth guidance of over 25% plus" (AZAD_Q2FY27_concall_transcript_2026-11-14.pdf [page 5]); AR: "sustained revenue growth in excess of 25% per annum" (Annual_Report_2026.pdf [page 36]). |
| G2 | "reach an annual revenue run rate of over INR1,300 crores by the end of FY28, more than double of our FY 2026 revenue" | (a) end FY28; also (c) as it rests on installed capacity | Q2 concall [page 5] | The FY26 base is consolidated ₹602.98 Cr (B09). |
| G3 | "We expect revenue to ramp up Q4 of FY27 onwards, and all the plants will be fully ramped up by Q2 of FY 2028" | (a) Q4 FY27 to Q2 FY28 | Q2 concall [page 5] | Moved from "from Q3 onwards" in August. |
| G4 | "each of these plants are poised to generate at full utilization ... INR150 crores to ... INR180-odd crores" | (c) | Q1 concall [page 14] | No date attached. |
| G5 | "you will see a drastic change coming to closer to 200 days. And H2, we get down to 160, 170 days" | (a) H1 and H2 FY27 | Q4 concall [page 9] | Q1 call widened H2 to "160 to 180 type of days" (Q1 concall [page 11], via 05-concall.md); no days figure on the Q2 call (B05). |
| G6 | "33% to 35% plus"; "32%, 35% is a good number ... for calculation purpose" | (b) EBITDA margin band, no period | Q4 concall [page 11]; Q1 concall [page 12] (via 05-concall.md) | Delivered margin 37.5% in Q2 FY27 standalone (B05). |
| G7 | "strong operating cash flow in FY '27 and beyond"; "Q4 is where we can see the cash flowing out of the company ... Q1 of next year would be perfectly in" | (a) FY27, then Q4 FY27 to Q1 FY28 | Q4 concall [page 7] (via 05-concall.md); Q2 concall [page 11] (via 05-concall.md) | The date slipped between May and November. |
| G8 | "We now have these lines in place with ICICI Bank and DP World, which can be used from Q4 FY27 onwards" | (c) capability, with a start period | Q2 concall [page 9] | Recourse not stated. |
| G9 | "One of our OEMs have agreed to give us a 50% advance against purchase orders, and we expect to receive close to about $4.5 million under this arrangement" | (a) FY27 per B05 | Q2 concall [page 9] | One unnamed OEM. |
| G10 | "GST credit of approximately INR100 crores ... which we expected to realize by H1 FY '28" | (a) H1 FY28 | Q4 concall [page 7] | Not repeated on later calls (B05). |
| G11 | "Energy contributing between 55% and 60% of revenue over four to five years" | (a) | Annual_Report_2026.pdf [page 36] | Energy share rose in FY26 (B03). |
| G12 | "around 7 to 8 months away from now" (hot-section facility) | (a) about March to April 2027 | Q1 concall [page 11] | Contract value confidential. |
| G13 | "in next 4 to 6 weeks is what we know" (weapon test); "8 to 12 weeks or you can say, 3 to 4 months" (4 to 5 engines) | (a) Aug to Nov 2026 | Q1 concall [page 8]; [page 13] | Both missed by 2026-11-07 (B05). |
| G14 | "commercial-scale supply expected to commence over the coming fiscal year as remaining qualification milestones are achieved" | (a) FY27 | Annual_Report_2026.pdf [page 31] | The first batch was undelivered on 2026-11-07. |
| G15 | "very soon you will have information that we have delivered our first qualification batch" | (b) | Q2 concall [page 12] | The "within this quarter" version of August was missed (B05). |
| G16 | "INR180 crores to INR190 crores will be coming there" (QIP balance) | (a) FY27 | Q4 concall [page 15] | QIP object deadline moved to 2027-03-31 (Annual_Report_2026.pdf [page 74], via B03). |
| G17 | "and towards full utilisation in FY 2027-28" | (a) | Annual_Report_2026.pdf [page 8] | The MD&A speaks of peak utilisation over a longer horizon (B03). |
| G18 | "maybe next quarter I can update you exactly what would be the range" | (b) guidance revisit, no firm period | Q2 concall [page 11] | Deferred on three calls (B05). |

### 4. CONCENTRATION

Customer, INR million, consolidated:

> "Revenue from top customer 1,123.97 648.81 / Revenue from top 5 customers 1,711.10 1,703.84" (Annual_Report_2026.pdf [page 242], FY26 and FY25 columns)

> "During the year the Company has derived revenue from 2 customers (March 31, 2025: 1) which amounts to 10% or more of its total revenue." (Annual_Report_2026.pdf [page 237])

Comment: revenue from operations is 6,029.75 (FY26, [page 237]), so the top customer is 18.64% [calc] (B03). The standalone note prints the second line as "Revenue from top 5 customers (other than above customer) 1,711.10" (Annual_Report_2026.pdf [page 172]). B03 settled it at the source: the 1,711.10 line excludes the top customer, so top five including the top customer is 2,835.07, or 47.02% [calc], and the AR prints no percentage. Names of the two customers at or above 10% are NOT DISCLOSED. H1 FY27 concentration is NOT DISCLOSED.

Geography, INR million: "Within India 534.05 388.12 / Outside India 5,495.70 4,185.42 / Total 6,029.75 4,573.54" (Annual_Report_2026.pdf [page 237]). Export share of revenue was 88% in Q2 FY27 (B09 range 88% to 93%).

Product and end market: "Energy and Oil & Gas contributed 81.5% of FY 2025-26 revenue, concentrated among three OEMs" (Annual_Report_2026.pdf [page 33]). The segment table prints Energy and Oil & Gas 4,811.3, Aerospace and Defence 1,012.6, total revenue from operations 5,903.8 (standalone, [page 31]). Top single product or component share is NOT DISCLOSED (no component-level revenue is printed). Order book mix: the AR gives Energy 57%, A&D 29%, O&G 14%, and CARE gives Energy ₹3,966 Cr (61.0%) (as read by B09, FLAG-ORDERBOOK-MIX; differs by ₹261 Cr).

### 5. PROMISE LEDGER

Call dates: Q4 FY26 2026-05-16, Q1 FY27 2026-08-08, Q2 FY27 2026-11-07 (B00-intake). Statuses follow B05 as corrected by Verifier B (B12b): D4 reads PARTIAL and M7 reads PENDING. The tally after correction is 5 delivered, 6 partial, 7 missed and 7 pending; the credibility grade C holds (B12b). Anchors are in Q-call [page N] form from 05-concall.md unless a filing is named.

| # | Promise | Made | Status | Evidence anchor |
|---|---|---|---|---|
| D1 | Revenue growth 25% plus in FY27 | Q4 call 2026-05-16 | DELIVERED for H1 (consolidated +25.9%, +31.1%, +28.6%) | Q4 [page 5]; Q2 FY27 results [page 3], [page 9] |
| D2 | EBITDA margin band; hold 37.6% | Q4 and Q1 calls | DELIVERED (37.6% Q1, 37.5% Q2 standalone) | Q1 [page 6]; Q2 results [page 3] |
| D3 | ATGG engine delivery "weeks" away | Q4 call | DELIVERED, filed 2026-07-22 | announcements/AZAD_2026-07-22 [page 1] |
| D4 | Remaining major activities done by mid-Q2, full closure Q3 | Q1 call 2026-08-08 | PARTIAL (B12b correction; closure pending, 2 to 3 week delay admitted) | Q1 [page 5]; Q2 [page 10] |
| D5 | Other income moderates as QIP funds are spent | Q4 call | DELIVERED (Q2 other income 46.55 vs 127.23, INR million) | Q2 results [page 3] |
| D6 | Revenue up in Q1 | Q4 call | DELIVERED (+8.3% Q1, +10.1% Q2 sequential) | Q1 [page 6]; Q2 [page 5] |
| P1 | Four more dedicated plants in six months, "on track" | Q4 call | PARTIAL (two added, six of eight) | Q4 [page 9]; Q2 [page 3] |
| P2 | Revenue reflection from Q3 | Q1 call | PARTIAL (Nov: throughput Q3, revenue ramp Q4) | Q1 [page 4]; Q2 [page 5] |
| P3 | Bill discounting lines in place; exports hedged by Q4 | Q1 call | PARTIAL (lines usable from Q4 FY27) | Q1 [page 19]; Q2 [page 9] |
| P4 | Oil and gas ramp with material numbers in FY27 | Q4 call | PARTIAL (moved to "from Q4 FY27", no figure) | Q4 [page 13]; Q2 [page 4] |
| P5 | QIP balance of ₹180 to 190 Cr deployed | Q4 call | PARTIAL (₹75.54 Cr left at 30 Sep 2026; deadline moved to 2027-03-31) | Q4 [page 15]; announcements/AZAD_2026-11-06_Monitoring_Agency_Report |
| M1 | Working-capital days about 200 in H1 FY27 | Q4 and Q1 calls | MISSED (no figure reported; revenue-basis days 336 to 369) | Q4 [page 9]; Q1 [page 11]; B01 |
| M2 | Strong operating cash flow in FY27 | Q4 call | MISSED on timing (H1 ₹(43.62) Cr; date moved to Q4 end and Q1 FY28; full year pending) | Q4 [page 7]; Q2 results [page 11] |
| M3 | Rolls-Royce first batch within the quarter | Q1 call | MISSED (undelivered 2026-11-07) | Q1 [page 13]; Q2 [page 12] |
| M4 | ATGG weapon test in 4 to 6 weeks | Q1 call | MISSED (testing ongoing) | Q1 [page 8]; Q2 [page 14] |
| M5 | 4 to 5 engines in 8 to 12 weeks | Q1 call | MISSED (second engine pending) | Q1 [page 13]; Q2 [page 14] |
| M6 | Capex plan beyond FY29 "next quarter" | Q1 call | MISSED (deferred again) | Q1 [page 10]; Q2 [page 13] |
| M7 | Revisit the 25% plus guidance when stabilised | Q4 and Q1 calls | PENDING (B12b: hedged and conditional; B05 had MISSED) | Q4 [page 8]; Q1 [page 14]; Q2 [page 5] |
| M8 | Saudi Baker Hughes facility | Q4 call | MISSED (disclosed slip; silent on later calls) | Q4 [page 15] |
| E1 | H2 FY27 working-capital days 160 to 170, then 160 to 180 | Q4 and Q1 calls | PENDING (loosened from 140 to 150 in Feb 2026) | Q4 [page 9]; Q1 [page 11] |
| E2 | Employee cost normalises in Q3 and Q4 | Q1 call | PENDING (Q2 +23.7% quarter on quarter) | Q1 [page 18]; Q2 results [page 3] |
| E3 | GST credit of about ₹100 Cr realised by H1 FY28 | Q4 call | PENDING | Q4 [page 7] |
| E4 | Run rate over ₹1,300 Cr by end FY28 | Q2 call | PENDING | Q2 [page 5] |
| E5 | MHI hot-section facility in 7 to 8 months | Q1 call | PENDING | Q1 [page 11] |
| E6 | Subsidiaries on track with a turnaround plan | Q1 call | PENDING (undefined, unverifiable) | Q1 [page 6] |
| A1 | Revenue growth about 30% in FY26 | AR2025 (letter 2025-09-08) | DELIVERED (+31.8% consolidated) | Annual_Report_2025.pdf [page 40]; Annual_Report_2026.pdf [page 38] (via B03) |
| A2 | Working-capital efficiency benefits from FY26 | AR2025 | MISSED (244 days against 202; revenue basis 336 against 266) | Annual_Report_2025.pdf [page 21]; Annual_Report_2026.pdf [page 7] |
| A3 | QIP objects completed by 2026-03-31 | AR2026 (letter 2026-09-07) | PARTIAL (₹368.67 Cr of ₹525.00 Cr used at 31 Mar 2026; deadline moved to 2027-03-31) | Annual_Report_2026.pdf [page 74] (via B03), [page 249] |
| A4 | Rolls-Royce first shipments before end of FY27 | AR2026 | PENDING | Annual_Report_2026.pdf [page 22] (via B03) |

### 6. RESTATED BASES

> "Revenue from top customer 648.81 554.38 / Revenue from top 5 customers 2,352.65 1,536.28" (Annual_Report_2025.pdf [page 238], consolidated, FY25 and FY24 columns)

> "Revenue from top customer 1,123.97 648.81 / Revenue from top 5 customers 1,711.10 1,703.84" (Annual_Report_2026.pdf [page 242], FY26 and FY25 columns)

Comment: the FY25 top-five comparative changed from 2,352.65 (INR million) to 1,703.84 with no restatement note. The top customer, 648.81, did not change, so the FY26 AR re-split the line to exclude the top customer; the difference of 648.81 matches (B02). The standalone note relabelled FY25 "top 5 customers" to "other than above customer" but kept 2,314.75 (Annual_Report_2026.pdf [page 172]). The search for a restatement, regrouping or reclassification note in the AR2026 text found none beyond OCI reclassification lines: a note on restated comparatives is NOT DISCLOSED. Minor FY25 differences between the ARs: depreciation 294.84 against 294.85, and Note 44 net assets 13,930.68 against balance sheet 13,930.26 (B02).

### 7. CORPORATE-ACTION CLAUSES

> "There are no scheme of arrangements which have been approved by the Competent Authority in terms of sections 230 to 237 of the Companies Act, 2013 during the reporting period." (Annual_Report_2026.pdf [page 250], Note 41(k))

Comment: no demerger or merger is in the corpus, and the AR reports no share repurchase in the last five years. No undertaking definitions, liability allocation clauses, ratios or appointed dates exist to quote. The AR records a bonus issue of "4,12,95,650 bonus equity shares of Rs. 2/- each" by capitalising reserves of "C 825.90" (INR million) in FY2023-24 (Annual_Report_2026.pdf [page 152]); the bonus ratio is not printed on that page. Other actions in the corpus:

> "the Company issued and allotted 5,468,750 equity shares of face value of C 2 each ... at the issue price of C 1,280 (including a premium of C 1,278 per equity share) aggregating to C 7,000.00 Mn" (Annual_Report_2026.pdf [page 249], Note 40)

Comment: QIP in the quarter ended 31 March 2025; the exact allotment date is NOT DISCLOSED in the note. Objects: capex 5,250.00, general corporate purposes 1,562.10, issue expenses 187.90 (INR million); used to 31 March 2026: 3,686.65, 1,562.10 and 153.98. Fetch the QIP placement document (BSE or NSE, March 2025).

> "INITIAL PUBLIC OFFER OF 14,122,108 EQUITY SHARES ... COMPRISING A FRESH ISSUE OF 4,580,151* EQUITY SHARES AGGREGATING UP TO ₹2,400.00 MILLION* BY OUR COMPANY ... AND AN OFFER FOR SALE OF 9,541,957* EQUITY SHARES" (AZAD_Prospectus_2023-12-23.pdf [page 3])

Comment: IPO of December 2023 at ₹524 per share, with 3,911,545 of the offered shares from Rakesh Chopdar (same page). Listing 2023-12-28 (B00).

> "As per terms of Shareholders Agreement ['SHA'] dated July 25, 2024 ... the revised shareholding stands at 51% by Holding Company and 49% by Leo Prime ... Call Option ... Put Option ... shall be the higher of: (i) Fair Market Value ... or (ii) an amount of INR 225.63 Mn" (Annual_Report_2026.pdf [page 250], Note 42, Azad Prime)

Comment: advance of C 54.13 Mn is non-refundable and deductible from the exercise amount ([page 250] to [page 251]). Azad VTC: SHA dated May 9, 2024, 51% and 49%, call option only, advance of C 23.3 Mn, refundable ([page 251], Note 43). Event definitions sit in the SHAs, which are NOT DISCLOSED in the corpus. B02 notes the Prime liability of 171.50 is held flat at the 225.63 floor.

> "The Company has granted 80,000 options to eligible employee(s) under the Employee Stock Option Scheme on May 12, 2026 ... at an exercise price of ^1050/-" (AZAD_Q2FY27_results_2026-11-06.pdf [page 12])

Comment: ESOP grant; the Sep 2026 shareholding file shows 80,000 options outstanding (AZAD_shareholding_2026-09-30_rendered.txt). No preferential issue appears in the corpus.

### 8. RELATED-PARTY PERIMETER

Consolidated Note 31, INR million, FY26 and FY25 (Annual_Report_2026.pdf [page 233] to [page 235]).

> "Entities over which KMPs/ directors and/ or their relatives are able exercise significant influence: Forgen Power Parts Private Limited, Atlas Fasteners, Swastik Coaters Pvt Ltd, Rouland Chemicals Pvt Ltd, Agrima Logipark" ([page 234])

| Entity | Transactions FY26 (FY25), INR million | Balances at 31 Mar 2026 (2025), INR million |
|---|---|---|
| Atlas Fasteners | Sale of goods or services 17.19 (2.24); purchase of PPE 5.31 (nil); job work expense 0.59 (1.11) | Trade receivables 23.98 (3.90); advance to suppliers 10.80 (12.40) |
| Swastik Coaters Pvt Ltd | Rent 1.56 (1.48); reimbursements 0.71 (nil); interest income 0.20 (0.20) | Security deposit 4.96 (4.96); advances for purchases 0.33 (0.83) |
| Rouland Chemicals Pvt Ltd | Rent 1.56 (1.48); interest income 0.20 (0.20) | Security deposit 4.96 (4.96); trade payables 1.29 (0.89) |
| Agrima Logipark | Rent 13.06 (12.20) | Trade payables 6.86 (nil) |
| Forgen Power Parts Private Limited | None printed | Security deposit 2.00 (2.00) |

Key managerial remuneration, FY26 (FY25), INR million ([page 234]): Rakesh Chopdar 48.00 (48.00); Jyoti Chopdar 12.00 (12.00); Vishnu Pramodkumar Malpani 7.20 (7.42); Murali Krishna Bhupatiraju 16.71 (9.99); Ronak Jajoo 5.55 (5.28). Relatives' remuneration: Kartik Chopdar 5.75 (4.87); Satwik Chopdar 0.92 (0.48). Sitting fees 5.56 (2.09). Comment: the perimeter is small in rupees. B02 records that promoter-linked entities are 98.9% of short-term rent, and Atlas Fasteners sales to a related party rose 667%. The AR states there are no related-party loans (B03).

### 9. PLEDGE AND SHAREHOLDING

Twelve quarters as filed: the corpus holds four points. The other eight quarter-end patterns are NOT DISCLOSED in the corpus (the patterns were not collected; fetch from BSE or NSE, scrip 544061).

| Date | Promoter (Rakesh Chopdar) | Promoter and group | Pledge | Anchor |
|---|---|---|---|---|
| 31 Mar 2024 | 3,83,30,255 shares, 64.84% | NOT DISCLOSED in the pages read | NOT DISCLOSED | Annual_Report_2026.pdf [page 152] |
| 31 Mar 2025 | 3,83,30,255 shares, 59.35% | 3,89,57,607, 60.32% | NOT DISCLOSED | Annual_Report_2025.pdf [page 80] |
| 31 Mar 2026 | 3,54,44,988, 54.88% | 3,60,64,240, 55.84% | NOT DISCLOSED in the AR | Annual_Report_2026.pdf [page 71] |
| 30 Sep 2026 | 3,54,44,988, 54.88% | 3,60,64,240, 55.84% | "WhetherAnySharesHeldByPromotersAreEncumberedUnderPledged: false" (also false for non-disposal undertaking and other encumbrance) | AZAD_shareholding_2026-09-30_rendered.txt |

Comment: B08 read a 30 June 2025 pattern on the web (outside the corpus) showing 63 shares pledged plus a non-disposal undertaking on 2,97,300 shares, since cleared (B08). Institutional holding, latest (30 Sep 2026): mutual funds 8.81% (5,691,156 shares); domestic institutions 10.40%; foreign institutions 12.70%; public 44.16%; total shares 64,581,743; locked-in 1,18,27,600 (all in AZAD_shareholding_2026-09-30_rendered.txt). At 31 Mar 2026 the AR printed foreign portfolio 14.75% and mutual funds 10.19% ([page 71]).

### 10. VERIFICATION

Documents quoted in this annex, with their dates:
- Annual_Report_2026.pdf (FY2025-26, cover letter 2026-09-07)
- Annual_Report_2025.pdf (FY2024-25, cover letter 2025-09-08)
- AZAD_Q2FY27_results_2026-11-06.pdf (board 2026-11-06)
- AZAD_Q4FY26_concall_transcript_2026-05-22.pdf (call 2026-05-16)
- AZAD_Q1FY27_concall_transcript_2026-08-14.pdf (call 2026-08-08)
- AZAD_Q2FY27_concall_transcript_2026-11-14.pdf (call 2026-11-07)
- AZAD_Prospectus_2023-12-23.pdf (2023-12-23)
- AZAD_shareholding_2026-09-30_rendered.txt (as on 2026-09-30, broadcast 2026-10-14)
- announcements/AZAD_2026-07-22 (turbojet delivery) and announcements/AZAD_2026-11-06_Monitoring_Agency_Report__69e0e356.pdf (named in the ledger)
- Quote reuse from stage reports: runs/azad-2026-11-15/outputs/reports/05-concall.md (anchors checked against the transcripts where marked; items marked "via" were not re-read)

CORPUS COMMIT HASH: e23ed3a7f2f377a012d5562cc9b26381ba966e1b

---

```yaml
stage: B09b-dossier
company: "AZAD"
run_date: "2026-11-15"
model: claude-sonnet-5-5
status: complete
corpus_verdict: "CORPUS GAPPED"
corpus_gaps:
  - document: "research/ broker notes (folder empty)"
    expected_source: "broker platforms via the operator"
    kind: "findable-missing"
  - document: "Five screener formula sheets (Profit & Loss, Quarters, Balance Sheet, Cash Flow, Customization)"
    expected_source: "screener.in export re-saved by the operator"
    kind: "findable-missing"
  - document: "QIP placement document, March 2025"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "Shareholding patterns for Dec 2025, Mar 2026 and the other quarters of the twelve-quarter history"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "Peer financials for MTAR, Unimech and PTC Industries (Gate 0 M2, M5, M9)"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "PTC Industries current-period transcripts (2 of 3 PTCIL slots empty; one 2023 document held)"
    expected_source: "company IR page"
    kind: "plausibly-nonexistent"
  - document: "Q1 FY27 cash flow statement"
    expected_source: "BSE"
    kind: "plausibly-nonexistent"
archetypes:
  - line: "Energy and oil and gas turbine components"
    archetype: "Build-to-spec component maker"
  - line: "Aerospace and defence engine components"
    archetype: "Build-to-spec component maker"
transition:
  - line: "Energy and oil and gas turbine components, including hot section"
    from_tier: "R3 VALUE-ADDED / SPEC'D SUPPLIER (low on the rung; ROCE leg unproven, six-year median 14.95%)"
    to_tier: "R4 FRANCHISE / SHARE-OF-WALLET LEADER"
    engine: "Six dedicated plants move from built to billing as delta qualifications clear (throughput Q3 FY27, revenue ramp Q4 FY27, full ramp Q2 FY28); mix shifts into single-source hot-section and aero engine parts"
    proof_gate: "Leg 1: Q3 FY27 consolidated revenue at least 5% above Q2's Rs 190.94 Cr and H2 FY27 at or above Rs 390.19 Cr. Leg 2: FY27 consolidated operating cash flow above zero before bill discounting, factoring and the USD 4.5 Mn advance, with Sep 2026 inventory of Rs 427.35 Cr falling. Both legs in the same cycle (Q3 FY27 results about Feb 2027, Q4 FY27 audited results about May 2027)"
    recognition_gap: "Open question for Stage 11: does the market already reflect the R4 state? Resolved through the PE gap. No number and no conclusion here"
    ugliness: "SPLIT: ARTIFACT-OF-CLIMB for returns and depreciation; working-capital and cash leg held open between ARTIFACT-OF-CLIMB and STRUCTURAL-FEATURE (INDETERMINATE per B13-lite); operator rules"
    transition_falsifier: "Q3 FY27 revenue flat or under 5% sequential; no Rolls-Royce acceptance by Q4 FY27; FY27 operating cash flow at or below zero or positive only via discounting, factoring or the advance; new equity raise while operating cash flow is negative"
  - line: "Aerospace and defence engine components"
    from_tier: "R2 COST-ADVANTAGED CONVERTER (qualified part families; durable pricing power unproven)"
    to_tier: "R3 VALUE-ADDED / SPEC'D SUPPLIER"
    engine: "Rolls-Royce, Pratt & Whitney Canada and Safran engine programmes move from qualification to production acceptance"
    proof_gate: "Rolls-Royce first qualification batch delivered and accepted by Q4 FY27, followed by a production order with value (Azad exchange filing or concall)"
    recognition_gap: "Open question for Stage 11: does the market already reflect the R3 state for this line? Resolved through the PE gap. No number and no conclusion here"
    ugliness: "ARTIFACT-OF-CLIMB (qualification-stage cost ahead of revenue); evidence is thin because order values, margins and the civil against defence split are NOT FOUND"
    transition_falsifier: "Fourth date slip on the Rolls-Royce batch, no acceptance by Q4 FY27, or no GTRE production order with count and value by FY28"
dominant_variables:
  - "Dedicated-plant revenue ramp (Q3 and Q4 FY27 sequential growth, delta-qualification count)"
  - "Cash conversion on one defined basis (operating cash flow source, inventory against revenue, working-capital days)"
  - "End demand from gas turbine makers (GE Vernova backlog plus slot reservations, Siemens Energy, MHI)"
  - "Qualification acceptance in higher-value lines (Rolls-Royce batch, MHI hot-section facility, GTRE engine order)"
business_falsifier: "Disclosure that the dedicated plants run on customer-owned, cost-plus or captive terms, or that job work (19.8% of revenue) is conversion of customer-supplied material, moving Azad toward an outsourcing partner; a margin drop when the Rs 72 Cr work in progress is invoiced; or a top customer at or above 20% or top five at or above 65%"
mental_model_status: "DRAFT - PENDING OPERATOR SIGN-OFF"
fragility:
  variable_count: 6
  verifiability_ratio: "3 of 6 externally observable"
  single_point_failure: "Dedicated-plant revenue ramp: a Q3 FY27 print flat on Q2 alone shows plants built but not billing"
  fragility_verdict: "FRAGILE"
candidate_count: 8
second_order:
  chains_drafted: 2
  pending_live_links: 2
  confirm_by_observations: 2
research_brief_items: 18
plain_summary_points: 15
annex:
  present: true
  questions_answered: 10
  corpus_commit_hash: "e23ed3a7f2f377a012d5562cc9b26381ba966e1b"
```
