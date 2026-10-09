# MMP Industries Ltd (MMP): Halt 1 understanding dossier

Run date 2026-10-05. Folder runs/mmp-2026-10-04. Stage 09b, assembly from committed blocks B00 to B09, B12a to B12d and confidence.yaml. This file holds no valuation, no price and no decision. The Mental Model Declaration in Section 2 is a draft pending operator sign-off.

Citation convention. A cite such as (B04) points to a stage block. A page cite such as "AR26 p.226" uses the page marker in the page-marked .txt beside each PDF. The printed AR26 page number sits 5 lower than that marker. Units: results and AR in INR Lakhs (L), press releases in INR Mn, decks, rating and screener in INR Cr (B00.reporting_units).

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

Inventory only. Source: B00 corpus_manifest and input_gaps, with filename dates read from the inputs folders.

**1. Concalls**

| Item | Filename | Date |
|---|---|---|
| Q4 FY26 call transcript | inputs/concalls/Concall_May_2026_Transcript.pdf | call held 25-May-2026 (B00) |
| Q1 FY23 call transcript | inputs/concalls/Concall_Jul_2022_Transcript.pdf | July 2022 (B00) |
| Peer transcripts, APARINDS (4) | inputs/peer-concalls/APARINDS-* | Oct 2025 to Jul 2026 (B06) |
| Peer transcripts, MAANALU (4) | inputs/peer-concalls/MAANALU-* | Nov 2025 to Aug 2026 (B06) |
| Peer transcripts, ARFIN | none collected | ABSENT (B00, B06) |

Most recent MMP quarter covered by a call: Q4 FY26. Q1 FY27 reported in August 2026 (B05), so its call is the plausible missing item. B00 records that the company holds about one call a year, which makes a Q1 FY27 call plausibly nonexistent, but the corpus does not prove it. Q2 FY27 results are not yet due on the run date of 5 Oct 2026. Transcripts for Q2 FY26, Q3 FY26 and Q1 FY27 are absent (B05 input_gaps). Analyst meets on 6-Mar-2026 and 30-Sep-2026 sit in announcements/ with no transcript.

**2. Annual reports**

| Item | Filename | Date |
|---|---|---|
| FY2025-26 | inputs/annual-report/Annual_Report_2026.pdf | filed 18-Aug-2026 (B00) |
| FY2024-25 | inputs/annual-report/Annual_Report_2025.pdf | filed 14-Aug-2025 (B00) |

Latest completed FY (FY26) is present. Two years are held, so the 3-year test is not met by ARs alone. FY24 balance sheet and cash flow lines come as comparatives inside AR25 (B01 gap list).

**3. Results filings**

| Item | Filename | Date |
|---|---|---|
| Q1 FY27 board outcome and unaudited results, machine readable | inputs/results/MMP_14082026140309_MMPILBMOutcomeFR30062026MR.pdf | period 30-Jun-2026; filename stamp 14-Aug-2026 |
| Q4 and FY26 audited results, scanned (no OCR) | inputs/results/MMP_23052026151817_MMPILBMOutcomeFR31032026.pdf | 23-May-2026 |
| Q3 FY26 results, scanned (no OCR) | inputs/results/MMP_13022026135642_MMPBMOutcomeResults31122025.pdf | 13-Feb-2026 |

Quarter gap between the latest results filing and the latest AR: one quarter (Q1 FY27, period to 30-Jun-2026). It is covered by the results filing, the 10-Aug-2026 press release and the Q1 FY27 deck. The Q2 FY26 results filing is absent; only its press release (07-Nov-2025) is held. The Q1 FY27 filing text is OCR-garbled in places (B05 input_gaps).

**4. Investor presentations**

| Item | Filename | Date |
|---|---|---|
| Q1 FY27 deck (latest) | inputs/presentation/MMP_13082026171648_MMPILInvestorPPT30062026.pdf | 13-Aug-2026 |
| Q4 FY26 deck | inputs/presentation/MMP_25052026103403_MMPInvestorPresentationMarch2026.pdf | 25-May-2026 |

**5. Research and rating**

| Item | Filename | Date |
|---|---|---|
| CRISIL letter enclosed in company cover | inputs/rating/MMP_30042026121825_MMPRating2026.pdf | 30-Apr-2026 |
| CRISIL rationale (HTML text, no page numbers) | inputs/rating/CRISIL_RatingRationale_MMP_2026-04-27.md | 27-Apr-2026 |
| Broker or research notes | research/ is empty | ABSENT (B00) |

**6. Corporate actions (announcements/)**

B00 lists 11 Reg 30 PDFs, Nov 2025 to Sep 2026. The folder holds 12 page-marked .txt files; the count difference is not reconciled in B00. Files by name stamp:

| Filename | Stamp date |
|---|---|
| MMP_07112025171739_MMPILPressReleaseSept2025 | 07-Nov-2025 |
| MMP_13022026172824_MMPPressReleaseDec2025Results | 13-Feb-2026 |
| MMP_06032026163331_MMPILInvestormeeting | 06-Mar-2026 |
| MMP_27032026122730_MMPILBMOutcome27032026 | 27-Mar-2026 |
| MMP_23052026181319_MMPPressRelease31032026 | 23-May-2026 |
| team_sandeshc_11062026115901_46 (SAST disclosure per B00) | 11-Jun-2026 |
| MMP_27062026122254_MMPILBMOutcome27062026 | 27-Jun-2026 |
| MMP_07072026181258_MMPILPressRelease7July | 07-Jul-2026 |
| MMP_10082026134252_MMPILPressRelease30062026 | 10-Aug-2026 |
| MMP_21082026132908_MMPILPressRelease21082026 | 21-Aug-2026 |
| MMP_12092026171459_MMPILAGM*2026 (AGM minutes and results filing) | 12-Sep-2026 |
| MMP_27092026145120_MMPArihantConf30092026 | 27-Sep-2026 |

Other inventory: inputs/shareholding/SHP_MMP_2026-06-30.md (NSE XBRL, submitted 11-Jul-2026, revised 13-Jul-2026; machine conversion). inputs/screening/*-Data_Sheet.csv (4 files, to FY26). prospectus/ is empty (not expected for a long-listed name, B00).

**7. Freshness pair check (B00.freshness_verdict: FRESHNESS PAIRS OK)**

| Pair | Status (B00) | Note |
|---|---|---|
| Newest results to same-quarter concall | SKIPPED | concalls_available false; Q1 FY27 transcript not held; not a failed pair |
| Rating bulletin to full rationale | PASS | CRISIL letter 30-Apr-2026 and rationale 27-Apr-2026 both held |
| Referenced SEBI order to order text | PASS | no SEBI order referenced; AR26 cites only boilerplate |
| AR not older than latest audited annual results | PASS | AR FY26 follows FY26 audited results |

No pair failed. No mate document is named as missing by the freshness check.

**Empty or gapped input folders (full list, repeated from the intake).** The empty-folder question was suppressed under the /step1 autonomy contract. The standing answer taken was to go on with the gaps (task message; B00 input_gaps).

1. announcements/: collector found no BSE scrip code, so the folder came up empty. Repaired by hand with a selection of NSE filings, not the full list.
2. shareholding/: empty at collection. Repaired with the Jun-2026 pattern only (machine conversion). Eight quarters of promoter holding come from an NSE API table.
3. screener sheets: Profit & Loss, Quarters, Balance Sheet, Cash Flow and Customization came out empty for MMP, ARFIN, APARINDS and MAANALU. Not repaired. Data_Sheet.csv carries the raw values.
4. results/: no screener PDFs. Repaired from NSE. The Q4 FY26 and Q3 FY26 filings are image scans with no OCR. The Q2 FY26 results filing is absent.
5. rating/: no PDF at collection. Repaired with the CRISIL letter and rationale text.
6. concalls/: two transcripts only, so no-concall mode applies. Q2 FY26, Q3 FY26 and Q1 FY27 transcripts absent.
7. peer-concalls/: ARFIN has none. APARINDS 4 and MAANALU 4 held.
8. research/: empty.
9. prospectus/: empty, not expected.
10. Exchange clarifications of 05-Mar-2026 and 23-Jun-2026: the company reply is not in the corpus.
11. Resignation filing for the two independent directors of 10-Aug-2026: not in the corpus (B08).

**8. Verdict line**

CORPUS GAPPED: findable-but-missing (operator upload list): full NSE/BSE Reg 30 list for Nov 2025 to date (BSE / NSE); Q2 FY26 results filing (BSE / NSE); shareholding patterns for the quarters before Sep-2024 (BSE / NSE); the company reply to the 05-Mar-2026 and 23-Jun-2026 exchange clarifications (BSE / NSE); resignation filing of the independent directors, 10-Aug-2026 (BSE / NSE); machine-readable (OCR) copies of the Q4 FY26 and Q3 FY26 results (company IR page / BSE); ARFIN peer transcripts (company IR page); screener full export sheets (screener.in re-export). Plausibly nonexistent (itself a data point): Q2 FY26, Q3 FY26 and Q1 FY27 call transcripts (company holds about one call a year, B00); broker or research notes (research/ empty, B00); prospectus (long-listed, B00).

**Open operator rulings carried into Halt 1** (no ruling is made here):

- B01 open rulings: (a) rule 6 scope, per-metric windows versus a full 10-year window; (b) admissibility of the ROCE proxy; (c) confidence tier keyed to the 10-year history or to the 3-year shortest scored window; (d) E2 window, where the 3-year start (Jun-2023) is NOT FOUND and a 27-month change of +0.01 pp is the alternative (B01 analyst_note, data_notes). Under the full-window reading with the proxy rejected the core score is 38, and under the 3-year tier the class falls from the middle band to the lowest Gate 0 band (B01; B07 combined_reasoning).
- B12c run 2 F1 (MAJOR): capex definition. PPE line only gives core 54. PPE plus CWIP increase plus capital advances gives core 50. Gate 0 class is the same either way (B12c).
- B12c run 2 F2 (MAJOR): M9 gross margin basis. Net of change in inventory the gap is 3.56 pp, M9 scores 1 and the moat class moves from MODERATE (12) to THIN (10). Gate 0 class is the same (B12c).
- B12c run 2 F5 (MAJOR): capex_embedded_growth_pct. B07 states 20.4. Counting only documented capex (wire rod; solar is a claim) gives 8.7, range 7.8 to 9.7. B12c asks that 8.7 be emitted and 20.4 kept as the upper bound (B07, B12c).
- Gate-recommendation reading: the phase 1 gate recommendation applied the confidence band (overall 67, band 60 to 74) on top of the cash-determination cap. A first-match reading of the same rules stops at the cap and lands one level more favourable. The operator may rule between the two at Halt 1 (outputs/final/gate-recommendation.md, "How the verdict was reached"; confidence.yaml).

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT - PENDING OPERATOR SIGN-OFF**

The model is a transition thesis. The FROM business anchors it. Sign-off happens only in claude.ai after live-web stress-testing. The classification in B5 is the draft reading; the operator may overrule it.

### PART A: THE FROM STATE

**A1. Archetype (per line)**

| Line | Share of FY26 revenue | Archetype from the library | Basis |
|---|---|---|---|
| Aluminium powders and pastes | 61.2% (B04) | Commodity converter, hybrid with an unquantified specialty tail | B04 archetype-hybrid marker; specialty share NOT FOUND |
| Aluminium foils | 26.1% (B04) | Commodity converter | B04; segment margin 2.00% |
| Conductors and cables | 12.1% (B04) | Commodity converter | B04; segment margin 4.86% |
| Polymer insulators (MMP Electricals) | 0.3% (B04) | Build-to-spec component maker, on intent only | revenue 231.94 L, loss (329.13) L (B04; AR26 p.226) |

**A2. The simple analogy.** MMP is a Nagpur metal kitchen. It takes in aluminium ingots and rolls, grinds and draws them into powder, foil and wire. It earns its keep from the gap between the metal it pays for and the product it ships. The powder kitchen is the busiest and earns about 12 cents of profit per dollar of sales. The foil kitchen earns about 2 cents. The wire kitchen earns about 5 cents (B04: segment margins 11.88%, 2.00%, 4.86%). The owners now spend the powder kitchen's cash to build three new rooms. One room makes insulators for power lines, one makes wire rod from raw metal, and one makes armoured cable. None of the three has yet shipped more than a trial order (B05).

### PART B: THE TRANSITION

**B1. FROM to TO (QUALITY LADDER)**

| Line | FROM | TO | Basis |
|---|---|---|---|
| Group core, powder-funded move into approval-gated electrical products (insulators, LT cable) | R2 cost-advantaged converter, at its low end | R3 value-added or spec'd supplier | FY26 ROCE 12.91% on the fixed formula, 15.26% before the one-time fire loss (B01; B12c F3). Mid-teens ROCE is the R2 mark. The business sits near the low edge of the rung. |
| Foils and conductors | R1 commodity price-taker | R2 cost-advantaged converter | Segment margins 2.00% and 4.86% with weak pricing power (B04). Wire rod and printed foil are the claimed cost and mix levers (B05). |
| Powders | R2, no rung move claimed | none claimed | Management claims better export margin, which is a within-rung lift (B05; AR26 p.26) |

The multi-rung rule applies: one rung per 2 to 3 years. No block shows a claim of more than one rung per line.

**B2. The engine (what physically changes)**

1. Approval-gated lines reach revenue. MMP Electricals (insulators), the LT power cable pilot at Bhandara and lidding or security printing foil must pass utility, BIS and pharma qualification and then ship. Q1 FY27 insulator revenue was ₹5 Mn against an FY27 guide of ₹18 to 20 Cr (B05).
2. Backward integration lowers conversion cost. The 18,000 MTPA wire rod plant (MMP Cables) and the 7 MW captive solar park cut metal and power cost (B05, B07). Wire rod trials are due by end Q3 FY27 and commercial production in Q4 FY27 (Q1 FY27 PR p.5 via B05).

**B3. The proof gate (hard binary, quarter by quarter)**

The gate has two legs. Both must read true in the same filing window. Thresholds come from B05 triggers 2 and 3, B07 optionality and B03 monitorables; the operator may reset them at sign-off.

- Leg 1: MMP Electricals quarterly revenue at or above ₹3 Cr (30 Mn) by Q3 FY27, with a PGCIL or state utility registration letter on file (B05 trigger 3; B07 optionality_register).
- Leg 2: foil segment margin above 4% for two consecutive quarters after the Q3 FY27 lidding foil launch (B07 optionality_register; B05 trigger 2). FY26 base is 2.00% (B04).

Until both legs read true, the transition is narrative and the name is research, not a trade. On the filed record the gate has not fired. FTTCP tests it in phase 2.

**B4. The recognition gap (open question for Stage 11)**

Does the TO state (R3 value-added supplier economics) already look reflected in the market pricing of MMP today? This dossier does not answer it. Stage 11 resolves it through the PE gap. If TO is already reflected, the re-rating engine is spent and only earnings growth remains.

**B5. The ugliness test (draft classification: STRUCTURAL-FEATURE, split reading)**

Today's ugly optic: FY26 EBITDA margin down about 133 bps to 8.0%, FY26 PAT down 20%, FY26 ROCE 12.91% from 16.31% (B00 LBF1; B03; B01).

Evidence for ARTIFACT-OF-CLIMB:
- 2.35 of the 3.40 point ROCE fall is the one-time fire exceptional loss (B12c F3).
- The Directors' report puts the net fire hit to EBITDA at ₹7 to 8 Cr, about 64% to 73% of the 133 bps fall (B02 analyst_note, derived).
- Q1 FY27 EBITDA was ₹210 Mn on ₹2,328 Mn revenue, about 9.0% (PR; B05), and powders grew 15% in FY26 against a single digit guide (B03).

Evidence for STRUCTURAL-FEATURE:
- Segment arithmetic gives mix -0.36 pts and within-segment rate -1.05 pts of the -1.41 pt segment margin fall. The foil segment gave 46.0% of segment revenue growth at 2.00% (B04).
- Over nine years PAT grew 6.8% a year against 16.8% for revenue. B01 says this gap is long run, not a post-IPO rebase or fire effect (B01 Gate 0 concern list; gate-recommendation.md).
- The FY25 margin base held a 2,069.76 L stock-build credit, 45% of FY25 standalone PBT (B03 analyst_note).
- The CFO said foil was a drag for 3 to 4 years (May-26 call p.18 via B05).

Draft classification: STRUCTURAL-FEATURE for the group margin and return gap, with the fire as an ARTIFACT slice inside it. One observation separates the readings: Q2 and Q3 FY27 powder segment margin back to 12.4% and foil segment margin above 2% (B04 analyst_note; B03 monitorables). The matrix posture is not set here.

**B6. The transition falsifier (kills the arrow)**

Any one of these, from the blocks:
- Q2 FY27 insulator revenue below ₹15 Mn, or an insulator segment loss above ₹1.0 Cr again (B05 trigger 3).
- Foil segment margin at or below 2.0% through H1 FY27 after the lidding and printing launches (B04 first_deterioration_signals; B05 trigger 2).
- LT cable BIS approval not received by the Q3 FY27 results, or wire rod trials moving beyond Q4 FY27 (B05 triggers 4 and 5).

### PART C: WHAT THE MODEL WATCHES

**C1. Dominant variables (become Role 5.5 tracker signals)**

1. Approval-gated line ramp: insulator quarterly revenue, PGCIL and utility registration, BIS licence for LT cable. State: ₹5 Mn in Q1 FY27; segment loss about 1.46 Cr in Q1 FY27 on OCR text (B05); LT cable pilot production started 7 Jul 2026 and BIS is pending (B05).
2. Segment margin mix: powder, foil and conductor segment margins. State: 11.88%, 2.00% and 4.86% in FY26 (B04). Q1 FY27 gross margin 21.0% (B04).
3. Backward integration delivery: wire rod trials and solar commissioning dates, and conductor margin recovery. State: wire rod budget moved from ₹13 to 15 Cr to ₹20 to 25 Cr in 11 weeks (B07 wire-rod budget marker); conductor Q1 FY27 revenue ₹171 Mn, down 42% (B05).
4. Cash and funding capacity of the powder engine: CFO net of short-term borrowing and payables as a share of EBITDA, and debt due within a year. State: 25.6% in FY26 and 76.6% of group debt due within a year (B03 cash-conversion and funding markers).

**C2. What the model rejects**

- Market size questions for the core. Core powder plus foil SAM is ₹1,852 Cr against ₹719 Cr of FY26 revenue, so market headroom of 2.6x is not the binding limit; execution, capacity and funding are (B09 analyst_note and capacity-gap marker).
- The management market claim. It is 5.3x the run's conservative TAM and covers the whole Indian aluminium industry (B09 mgmt_claim_read: inflated).
- Spot-year ROCE and rupee working-capital trends as inputs for a converter (B04 irrelevant_ratios; Amendment 17).
- Revenue growth percent read alone, because the price and volume split is NOT FOUND (B04).
- Headline earnings per share without the associate share, since associates were 20.5% of FY26 PBT and mostly non-cash (B04, B01).

**C3. The business falsifier (kills the starting business)**

Q2 or Q3 FY27 powder segment revenue growth below 10% YoY, or powder segment margin below FY26's 11.88% for two straight quarters (B05 trigger 1 kill signal; gate-recommendation.md falsification line). Powders carry 89.6% of segment result (B03), so a stalled powder engine ends the funding source for the build. A second trigger: a disclosure that the powder specialty tail is nil, which would re-declare powders as a pure commodity converter (B04 archetype-hybrid marker).

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE (draft from B01 to B09)

MMP turns bought aluminium into powder, foil and conductor wire at plants near Nagpur (B04). Powders made 61.2% of FY26 revenue and about 90% of segment result. They come as atomised, pyro, flake and leafing grades that go into mining explosives, AAC (autoclaved aerated concrete) blocks, pesticides, paints and pyrotechnics (B04, B09). Foils made 26.1% of revenue and go into pharma strip and blister packs, food foil and printed packaging. Conductors made 12.1% as bare and bundled aluminium wire for overhead power lines (B04). The customers are explosives makers, AAC makers, agrochemical and paint makers, pharma packagers, state utilities and EPC contractors, plus AVL Metal Powders in Belgium under a long-term contract (B03, B04). The company discloses no customer names or concentration, so the run did not establish this (B04). Customers qualify powder and pharma foil over long cycles, and utility vendor approval takes 1.5 to 2 years by management's account. Conductor customers order on tender and pay late (B04, B05). Present demand follows mining and explosives volumes, AAC block output and PMAY-U housing, pharma output and exports, state utility payments and RDSS disbursement, and the aluminium ingot price on LME and MCX, which sets revenue per tonne in every line (B09 downstream candidates). Forward demand rests first on exports, up 66.8% in FY26 and guided up 40 to 50% in FY27, a claim the AR27 export line will test and one that peer reports of stalled Gulf shipments leave open (B07, B05, B06). The DGTR duty on Chinese foil, read with China import volumes, and listed explosives makers' volumes lead foil and powder demand. PGCIL registration and BIS licences gate the insulator, LT cable and AL59 conductor revenue that management plans (B09). Powders are the only line with a plausible edge: four decades of process know-how and the AVL and Toyo links, which the emerging moat scan rates Moderate as partnerships but which margin does not yet confirm (B04, B07). Foils earned 2.00% and conductors 4.86% in FY26, so neither line has a moat. Insulators and LT cable are start-ups with no moat yet. The scan scored zero on talent asymmetry and cannibalization barrier (Categories 21 and 22) and 11.6 in total, 0.4 under the 12.0 floor (B07).

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. Verticals framed

**Vertical 1: Approval-gated line ramp (insulators, LT cable)**
- Corpus establishes: insulator segment FY26 revenue 231.94 L, result (329.13) L, segment assets 3,489.42 L (B03; AR26 p.226-227). Q1 FY27 revenue ₹5 Mn against an FY27 guide of ₹18 to 20 Cr and a FY28 guide of ₹45 to 50 Cr (B05). PGCIL registration moved from early Q1 FY27 to Q2 FY27 to "coming months" (B05 timeline_slippages). LT cable launch slipped from Q4 FY26 to 7 Jul 2026 and BIS is pending (B05).
- Corpus cannot establish: any PGCIL or utility registration status; named customers for the Nepal order and US prospects (B03); BIS filing status for LT cable (B07 NOT FOUND); insulator capex budget versus actual.
- Deciding questions: (1) Has PGCIL or any state utility registered MMP Electricals, and on what date? (2) Is the Q2 FY27 insulator revenue at or above ₹15 Mn? (3) Does BIS grant the LT cable licence before the Q3 FY27 results?

**Vertical 2: Segment margin mix (powder, foil, conductor)**
- Corpus establishes: powder 11.88% (FY25 12.37%), foil 2.00%, conductor 4.86% (FY25 8.27%) (B04; B05). Foil holds 25.0% of segment assets for 6.4% of segment result (B04). Q1 FY27 gross margin 21.0%, with operating expense unchanged at 12.0% of revenue, so the quarter's gain came from gross margin (B04 unit_economics).
- Corpus cannot establish: tonnage volumes, realisation per tonne, grade mix inside powders, export versus domestic margin (B04 NOT FOUND). Per-tonne EBITDA guides rest on management's word only (B04 analyst_note).
- Deciding questions: (1) Do Q2 and Q3 FY27 powder margins return to 12.4%? (2) Does foil segment margin rise above 2% once lidding foil launches in Q3 FY27? (3) How large are inventory gains at open metal exposure, given peers hedge back to back (B06 hedge-difference marker)?

**Vertical 3: Backward integration delivery (wire rod, solar, conductor margin)**
- Corpus establishes: wire rod 18,000 MTPA, budget ₹20 to 25 Cr in the Q1 FY27 deck against ₹13 to 15 Cr in the Q4 FY26 deck (B07). AR26 p.30 says installation from July 2027, while the Q1 FY27 PR p.5 says installation is under way with trials by end Q3 FY27 (B05). Solar moved dates four times (B05). Four of four completed plants met or beat AR dates (B07 execution-split marker).
- Corpus cannot establish: the wire rod date that is correct; funding source for solar and Umred LVPC (B07 NOT FOUND); conductor order book; the payment-delay explanation, which no peer confirms (B06).
- Deciding questions: (1) Does wire rod start trials by end Q3 FY27? (2) Does conductor revenue return above ₹20 Cr in Q2 FY27 (the deferral reading, B06)? (3) Does conductor segment margin reach 8.27%?

**Vertical 4: Cash and funding capacity**
- Corpus establishes: FY26 consolidated CFO 5,328.97 L includes 1,723.34 L of short-term borrowing and 1,909.56 L of payables build. CFO net of both is 1,696.07 L against gross capex of about 5,560.50 L (B03 cash-conversion marker). Parent cash 56.38 L, guarantees 6,688 L (22.0% of standalone net worth), commitments 5,642.27 L against undrawn subsidiary term loans 3,126.32 L (B02). 76.6% of group debt falls due within a year (B03). Trade receivables are clean (96.3% not due; B02).
- Corpus cannot establish: insurer acceptance of the 793.05 L claim; the debtor and age of the 703.86 L other receivables; the fire PPE add-back tie-out (B02 NOT FOUND); the funding plan for the ₹85 to 90 Cr Umred programme (B07).
- Deciding questions: (1) Does H1 FY27 CFO net of short-term borrowing and payables exceed 50% of EBITDA with payable days not above 24.8? (2) Has the insurer paid any of the 793.05 L? (3) What named mix of internal accrual, term debt and equity funds the FY27 capex inside the stated net debt to equity limit of 1.0?

### 4b. Candidate signal table (all UNVERIFIED; verification and tracker writes at Role 5.5 in claude.ai)

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| India monthly coal production and explosives offtake (B09) | Coal output flat or falling for two straight quarters while MMP guides powder growth of 13 to 15% | Monthly | Ministry of Coal, Coal India monthly releases, PIB (B09) |
| Listed explosives makers' volume commentary (B09; customer names NOT FOUND in the corpus) | Dependency owner reports YoY volume decline for two quarters | Quarterly | Quarterly filings and concall transcripts of the named dependency owners via BSE/NSE (B09) |
| AAC block output and PMAY-U 2.0 housing approvals (B09) | Sanction pace or AAC output falls YoY for two quarters | Quarterly | MoHUA and PIB releases, PMAY-U sanction data, industry association notes (B09) |
| DGTR and CBIC order on Chinese foil, with China foil import volumes (B09) | Imports under HS 7607 do not fall after the duty, or the duty lapses early. Note: the deck prints US$619 to 873 per MT (Q1 FY27 deck p.25), B09 carries USD 479 to 721; the notification settles it | Event-driven | DGTR findings, CBIC notification, DGCI&S tradestat HS 7607 (B09) |
| India pharma exports and domestic production (B09) | Pharma exports decline YoY for two quarters | Monthly | DGCI&S tradestat, Pharmexcil, CDSCO (B09) |
| State utility payments and RDSS disbursement (B09; shared) | RDSS disbursement normal while MMP conductor revenue stays below ₹20 Cr in Q2 FY27, which breaks the payment-delay story (B05, B06) | Quarterly | PFC and REC RDSS dashboards, utility results, CEA data (B09) |
| PGCIL vendor registration and BIS licences for LT cable and AL59 (B09; shared) | No PGCIL registration, or no BIS licence for LT cable, by the Q3 FY27 results (B05) | Event-driven | BIS licence database, PGCIL vendor list, utility tender portals (B09) |
| Aluminium ingot price on LME and MCX (B09; shared) | Metal flat or falling in Q2 FY27 while gross margin stays at or below 19% (B05 separator; B04 red-line threshold) | Monthly | LME and MCX price series (B09) |

### 4c. Fragility read

- variable_count: 7. External variables that must go right: powder demand and exports; insulator approvals and ramp; LT cable BIS and first sales; wire rod and solar commissioning; foil margin lift; funding headroom; aluminium price pass-through (B05, B07, B09).
- verifiability_ratio: 4 of 7 externally observable (powder demand through B09 candidates, PGCIL registration, BIS licence, LME price). Company-narrated only: wire rod and solar timing, foil margin lift via named customers, funding plan.
- single_point_failure: yes. The powder segment. It carries 89.6% of segment result (B03) and funds every start-up. A powder growth fall below 10% YoY, the falsification line in gate-recommendation.md, ends the funding source. A second candidate is the roll-over of short-term lines, because 76.6% of group debt is due within a year (B03).
- fragility_verdict: FRAGILE. Many variables, three of seven company-narrated and one kill-switch.

### 4d. Research brief (claude.ai work order; the corpus cannot do these)

1. PENDING LIVE VERIFICATION (Chain 1): NSE and BSE Reg 30 announcements for MMP from 1-Aug-2026 onward for any new sanction, rating action or reply to the 23-Jun-2026 exchange clarification.
2. PENDING LIVE VERIFICATION (Chain 1): CRISIL ratings page for MMP Industries for any rating action after 27-Apr-2026, and the FY26 actual GCA, inventory and receivable days.
3. PENDING LIVE VERIFICATION (Chain 2): PGCIL approved vendor list or registration page for MMP Electricals.
4. PENDING LIVE VERIFICATION (Chain 2): vendor approval notices from MSEDCL, PGVCL and CSPDCL for MMP Electricals (named in the Q1 FY27 PR p.5, B05).
5. Chain 3 to build: powder export route. Gulf and GCC shipments, freight and the AVL Belgium contract against the +40 to 50% export guide (B06 export-contradiction marker).
6. Chain 4 to build: conductor payment cycle. RDSS and utility payment data against MMP conductor revenue down 42% in Q1 FY27 while APARINDS conductor revenue rose 19.9% (B06).
7. Chain 5 to build: foil margin. DGTR duty sunset and foil import volumes, Hindalco as foil stock supplier (named in AR25, absent in AR26; B03), and lidding foil customers.
8. Umred FIR text, or the company's Reg 30 reply, to settle whether the whole time director is the general manager booked in April 2025 (B08 analyst_note).
9. Reason filings for the 10-Aug-2026 independent director exits, and the AGM e-vote outcome (B08).
10. Insurer acceptance and cash receipt against the 793.05 L claim (B02).
11. CRISIL Issuer Not Cooperating start date (B08 NOT FOUND).
12. Anti-dumping duty effective date, rate and sunset. The deck and B09 carry different rate ranges (B04, B09).
13. Source URL verification for B09 market sizing and the foil volume divergence (337 kt, about 510 kt, 915 kt; separator DGCI&S HS 7607 data; B09 foil-volume divergence marker).
14. AVL Belgium contract value and tonnage, ISRO qualification, and exclusivity terms in the AVL and Toyal agreements (B07 NOT FOUND).
15. Q1 FY27 and Q2 FY27 results filings and any transcript for MMP (Nov 2026 for Q2). Also the BSE/NSE full filings list.
16. Court docket status for the Umred case and MCA charge checks on Star Circlips, Rohini Farms and Mayank Fasteners (B08 searches_skipped).

### 4e. Second-order stub (Master Prompt v3.7, Rule F)

**CHAIN 1: Group capital commitments 5,642.27 L against undrawn subsidiary term loans 3,126.32 L and parent liquidity 298.62 L (B02 funding marker)**
Link 1 [VERIFIED, filed AR26]: FY26 consolidated CFO net of short-term borrowing and payables was 1,696.07 L against gross capex of about 5,560.50 L (B03 cash-conversion marker). Parent cash was 56.38 L and corporate guarantees stood at 6,688 L, 22.0% of standalone net worth (B02).
Link 2 [PENDING LIVE VERIFICATION]: Who pays, and why now. The corpus names Kotak Mahindra Bank as lender to MCPL (term loan 3,188 L sanctioned, 512.70 L drawn; B03 ar_new_downstream_entities). Why now: wire rod trials and solar commissioning are due in Q3 FY27 (B05). The sanction terms, any rating action after 27-Apr-2026 and the company reply to the 23-Jun-2026 exchange clarification are not in the corpus (B00). Claude web should open the NSE and BSE announcement list for MMP from 1-Aug-2026 and the CRISIL ratings page for MMP Industries.
Link 3 [INFERENCE]: Commitments exceed the undrawn subsidiary lines, so the gap needs one of three sources: more parent working-capital lines, longer supplier credit, or promoter support, of which the 280 L interest-free promoter loans to MEPL are the precedent (B02). Each source has a visible trace in the H1 FY27 filing: short-term borrowing up, payable days above 24.8, or a new related-party loan.
Binding constraint: parent liquidity and the roll-over of working-capital lines. 76.6% of group debt is due within a year (B03). The bank limit ran 89% utilised in the 12 months to March 2026 (CRISIL rationale line 35, quoted in gate-recommendation.md). Revenue-basis working capital ran 88.9 days against peers at 45 to 60 days (B01; B06). The capex schedule has wire rod trials and solar in Q3 FY27 and Umred LVPC in H1 FY28 (B05).
Unsaid: the consolidated maturity table shows nil over 5 years although loans run to 2032 and 2033 (B02 funding marker). About 580 L of subsidiary reimbursement flows carry no closing balance, with MCPL 471.75 L expected (B03 monitorables). No analyst asked about guarantees, associates or related-party flows on the May call (B05).
Observation that confirms or breaks this chain, and confirm-by date: H1 FY27 consolidated cash flow in the Q2 FY27 results filing (NSE, November 2026). CFO net of short-term borrowing and payables above 50% of EBITDA, with payable days not above 24.8, confirms internal funding. At or below 25.6% with short-term borrowing or payables rising breaks it (B03 monitorables; gate-recommendation.md).

**CHAIN 2: Insulator segment FY26 revenue 231.94 L, loss (329.13) L, segment assets 3,489.42 L (B03; AR26 p.226-227)**
Link 1 [VERIFIED, filed AR26 and PR]: FY26 insulator segment capex was 2,128.27 L (AR26 p.227). Q1 FY27 insulator revenue was ₹5 Mn against an FY27 guide of ₹18 to 20 Cr (B05). The guide needs about ₹60 Mn a quarter in Q2 to Q4 (B05 trigger 3).
Link 2 [PENDING LIVE VERIFICATION]: Who pays, and why now. The paying classes are PGCIL, state transmission and distribution utilities, EPC contractors and export customers. The corpus names MSEDCL, PGVCL and CSPDCL (Q1 FY27 PR p.5 via B05) and Adani Renewables up to 33 kV (B05 red flags). The Nepal commercial customer and US prospects are unnamed (B03). Why now: MMP says approvals conclude "over the coming months" (B05 timeline_slippages). Claude web should open the PGCIL approved vendor list and the MSEDCL, PGVCL and CSPDCL vendor approval notices for MMP Electricals.
Link 3 [INFERENCE]: The CMD said validation takes 6 to 8 months for utilities, more for PGCIL, and at least 1.5 to 2 years in full, and that PGCIL wants performance elsewhere first (May-26 call p.16). APARINDS reports a PGCIL past-performance rule (B06). Early revenue can therefore come only from state utilities, EPC contractors and the 11 and 33 kV classes. The CMD places Chinese imports in those classes and says the company's focus is 220 to 765 kV (May-26 call p.16). The 20% EBITDA mix (May-26 call p.11) may arrive later than the first revenue.
Binding constraint: approval time, already sunk capital and funding. Insulator segment assets are 3,489.42 L with a further ₹8 to 10 Cr for balancing equipment and moulds (B05; May-26 call p.15-16). MEPL is funded by 280 L interest-free promoter loans and a 7.00% preference share against about 8.6% own borrowing cost (B02, B03 funding markers).
Unsaid: Star Circlips, an unlisted promoter-group associate, is to supply forged end fittings once its ₹25 Cr plant runs, with no stated pricing method (B05 capex programme; B04 mgmt_questions). The unnamed Nepal and US customers and the missing PGCIL registration are not mentioned in the guidance sentence (B03; B05).
Observation that confirms or breaks this chain, and confirm-by date: Q3 FY27 results (February 2027). Confirms: quarterly insulator revenue above ₹30 Mn with a PGCIL registration letter on file. Breaks: Q2 FY27 insulator revenue below ₹15 Mn, or a segment loss above ₹1.0 Cr again (B05 trigger 3).

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in claude.ai with live web, before Role 2.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. MMP Industries is a Nagpur company that turns bought aluminium into powder, foil and wire. FY26 revenue was ₹824 Cr, up 19% (B07, B00).
2. Powders are 61% of sales and about 90% of segment profit. Foils are 26% and conductors 12% (B04, B03).
3. FY26 profit fell. EBITDA margin dropped about 1.3 points to 8.0% and PAT fell 20%. A fatal fire at the Umred powder plant in April 2025 stopped it for about 50 days (B00, B03, B08).
4. Customers are explosives, AAC block, paint and pesticide makers, pharma packagers, state utilities and EPC contractors. A Belgian partner, AVL, takes powder under a long-term contract (B03, B04).
5. The company does not name its customers or give concentration. This run could not establish it (B04).
6. Demand follows mining, housing, pharma and grid spending. The aluminium price sets revenue per tonne in all lines (B09, B04).
7. Management expects growth from exports, up 40 to 50% in FY27, and from new lines. Peers report stalled Gulf shipments, so this claim is open (B05, B06).
8. FY27 growth guidance fell from 20 to 25% to 15 to 18% in 11 weeks (B05).
9. The moat is thin. Powders have four decades of know-how and moderate partnership evidence. Foils earn 2% and conductors 5%, so those lines have no moat. The moat scan scored 11.6, just under the 12.0 floor (B04, B07).
10. The mental model, in draft: a powder converter, near the low edge of the cost-advantaged converter rung, uses powder cash to build insulators, cables and wire rod to climb to a value-added supplier rung. No proof gate has fired yet (Section 2).
11. The fragility verdict is FRAGILE. Seven things must go right, three rest on company statements alone, and a slowdown in powders alone would break the funding (Section 4c).
12. Cash is the weak spot. About 68% of FY26 operating cash came from borrowing and supplier credit. 77% of group debt is due within a year (B03).
13. The corpus could not establish: customer concentration, tonnage and price per tonne, the insurer's payment on the 793.05 L claim, and whether the whole time director is the officer booked in the Umred case (B04, B02, B08).
14. The corpus has gaps: no call for Q1 FY27, two scanned results filings without OCR, a hand-picked list of exchange filings, and no research notes (Section 1).
15. The biggest open questions are three. Do insulator and cable approvals arrive on time? Do powder and foil margins recover in Q2 and Q3 FY27? Does cash conversion improve in the H1 FY27 filing? (B05, B03).

---

## SECTION 6: STANDING EXTRACTION ANNEX

Quote-then-comment form. Page cites use the page marker in the page-marked .txt beside each PDF. The printed AR26 page number is 5 lower. Amounts are in INR Lakhs unless the quote says otherwise.

### 1. UNITS

No realisation per tonne, revenue per case or price per litre is printed in AR26, the decks or the press releases (B04 revenue_per_unit NOT FOUND; tonnage by segment NOT FOUND). Per-unit figures that are printed:

- Installed capacity (call): "Currently, we have installed capacities of 12,000 tons per annum for atomized powders, 16,800 tons per annum for pyro & flakes and 300 tons per annum for leafing powders." (Concall_May_2026_Transcript.pdf p.4). Comment: capacity, not volume. Powder products by grade.
- Foil capacity: "installed capacities of 8,400 tons per annum in the rolling mill division and 3,600 metric tons in the conversion division" (same file p.4). Comment: capacity of two foil stages.
- EBITDA per tonne guide: "Powder will give us around 37,000 to 42, 000 per metric ton. And the foil business we are estimating around 12,000 to 15,000 per ton. And the conductors and cable business will give around 15,000 to 18,000 per ton." (same file p.20). Comment: each figure covers a segment basket, not one product; the unit is "per ton" with no currency printed; undated; filings give no tonnage to test it.
- Wire rod: "around INR10,000 to INR12,000 per ton" (same file p.13). Comment: standalone wire rod, one product.
- Insulator price: "the price range presently in the market is ranging from maybe INR150 per piece to INR9,000 a piece." (same file p.11). Comment: a basket across KV classes from 11 kV to 765 kV.
- Anti-dumping duty: "$619-$873/MT anti-dumping duty on Chinese aluminium foil" (MMP_13082026171648_MMPILInvestorPPT30062026.pdf p.25). Comment: US dollars per tonne; B09 carries a different range (USD 479 to 721), so the notification settles it.

Derivation path if the operator needs a per-tonne figure: segment revenue is printed (AR26 p.226: Powder and Paste 50,403.67 L, Foils 21,520.37 L, Conductors 9,997.96 L) but volumes are not, so no per-tonne figure can be derived from the corpus.

### 2. SEGMENT CAPITAL AND DEBT

AR26 consolidated segment note (Annual_Report_2026.pdf p.227). Columns: Powder and Paste, Foils, Conductors, Insulators, Others, Total.

| Item | FY26 (2025-26) | FY25 (2024-25) |
|---|---|---|
| Segment assets | "32473.91 13,511.96 3,541.78 3,489.42 1,101.65 54,118.85" | "29,303.75 12,487.44 3,789.20 1,016.47 136.38 46,733.24" |
| Unallocated corporate assets | 8,374.81 | 8,169.77 |
| Total assets | 62,493.66 | 54,903.01 |
| Segment liabilities | "6,545.16 868.07 590.73 2,388.16 511.31 10,903.43" | "8,363.90 312.80 614.74 427.08 571.94 10,290.46" |
| Unallocated corporate liabilities | 16,939.45 | 12,268.35 |
| Total liabilities | 27,842.88 | 22,558.81 |
| Capital expenditures (segment) | "1,570.86 35.47 583.04 2,128.27 - 4,317.65" | "3,959.69 19.76 108.37 790.41 30.42 4,908.65" |
| Unallocated capex | 597.22 | 158.15 |

Capital employed by segment is not printed; it can be derived as segment assets less segment liabilities, not computed here. Borrowings are not allocated by segment. The note defines "Unallocable Assets" and "Unallocable Liabilities" as items "that relate to the Group as a whole" (p.225). The consolidated balance sheet prints total borrowings (Annual_Report_2026.pdf p.171): non-current "Borrowings 18 4,317.62 3,213.91" and current "Borrowings 23 14,134.83 12,411.50", which sum to 18,452.45 for FY26 (derived; B03 prints 18,452.46). Comment: borrowings sit inside unallocated liabilities of 16,939.45.

### 3. GUIDANCE VERSUS ASPIRATION

(a) Guidance with a period
- FY27 group revenue: "the Company is hopeful to achieve revenue growth of 15 –18% in FY27." (MMP_10082026134252_MMPILPressRelease30062026 p.3). It replaces 20 to 25% from the Q4 FY26 deck p.9 (B05 guidance-cut marker).
- FY27 blended margin: "Blended EBITDA margins are also expected to improve, subject to stable metal prices" (same file p.3). Direction only; the CFO declined a percentage (May-26 call p.20).
- FY27 exports: "exports are expected to increase by approximately 40–50% in FY27" (same file p.3).
- FY27 powders: "FY27 revenue growth of ~13 to 15% along with improvement in EBITDA margins." (Annual_Report_2026.pdf p.26).
- FY27 foils: "the Company expects the Aluminium Foils business to deliver 15% YoY growth in FY27." (AR26 p.26).
- Security printing and lidding foil: "Both product launches are expected by early Q3FY27" (AR26 p.26).
- AL59 conductors: "expects meaningful traction in this segment beginning H1FY27" (AR26 p.26).
- Wire rod: "Plant trials are expected to commence by the end of Q3FY27" (Q1 FY27 PR p.5). AR26 p.30 says installation from July 2027 (B05).
- Solar: "planned investment of ₹30 Cr" with commissioning in Q3 FY27 (Q1 FY27 PR p.5 and p.6; B05).
- ROCE: "in the next year, the ROCE will be around in the range of 13%- 14% and in FY27-28, it will be around, it will be more than 15%." (Concall_May_2026_Transcript.pdf p.19).
- Insulators: "around INR18 crores to INR20 crores revenue from poly mer insulator division in FY26-27 and around INR45 crores to INR50 crores in the 27-28 financial year." (same file p.15).
- Foil utilisation: "hopefully in this year we will be able to achieve around 60%, 65% capacity utilization in the foil section." (same file p.21).

(b) Aspiration without a period
- "Yeah, so we will not go beyond one." on net debt to equity (same file p.15). FY26 is 0.53 (B05).
- "the peak revenue for this division will be around INR130 crores, INR140 crores" for insulators (same file p.16).
- EBITDA per tonne, powder 37,000 to 42,000, foil 12,000 to 15,000, conductors and cable 15,000 to 18,000 (same file p.20), and "around 3.5 assets turn ... around 20% EBITDA margin" for insulators (same file p.11). LT cable 14 to 15% EBITDA margin (B05 guidance, May-26 call).

(c) Capacity or capability only
- Wire rod: "Construction of the 18,000 MTPA Aluminium Wire Rod facility is at an advanced stage" (Q1 FY27 PR p.5).
- Umred LVPC ₹85 to 90 Cr in two phases of 6,000 MTPA; Bhandara LT cable pilot 100 MT a month (B05; B07).
- Installed powder and foil capacity as quoted in item 1; "no capex for at least 2 years" in powder and foil (B05, May-26 call p.16, p.18, p.21).

### 4. CONCENTRATION

- Product (Annual_Report_2026.pdf p.132, standalone): "Aluminium Powder and Paste 50,403.54 43,793.05", "Aluminium Foils 21,520.37 15,417.53", "Aluminium Conductors 9,997.96 9,666.99", "Total Revenue from Operations…(`) 82,168.59 69,185.99". Comment: powders are the top product at 61.2% (B04).
- Geography (same page): "In India 78,257.99 66,833.74", "Outside India 3,836.87 2,300.88". Comment: outside India is about 4.7% of contract revenue in FY26 (derived).
- Customer: NOT DISCLOSED. AR26 prints no single-customer revenue share and no major-customer note (B04 NOT FOUND; a search of AR26 for major-customer or 10%-of-revenue text found none). AR26 p.26 says only "a diversified customer base". Named related customer: Toyal MMP India sales "1,801.51" (p.152), 2.19% of standalone revenue (B02).

### 5. PROMISE LEDGER (B05 promise_delivery; 18 closed items)

| Date made | Source | Promise | Status | Evidence anchor |
|---|---|---|---|---|
| 14-Aug-2025 | AR25 p.18 | Powders FY26 single-digit growth | delivered | +15.1% (AR26 S p.132) |
| 14-Aug-2025 | AR25 p.18 | Phase III 2,500 MTPA operational by end Q2 FY26 | delivered | Q2 FY26 PR p.3; no tonnage test possible |
| 14-Aug-2025 | AR25 p.18, p.22 | MEPL Phase I commercial production Q2 FY26 | delivered | Q2 FY26 PR p.4; revenue only 23 Mn in FY26 |
| 13-Feb-2026 | Q3 FY26 PR p.3 | MEPL Phase II by mid-March 2026 | delivered | Q4 FY26 PR p.4; AR26 p.30 |
| 07-Nov-2025 | Q2 FY26 PR p.3 | Powders H2 FY26 revenue 20 to 25% above H1 | delivered | 2,804 vs 2,236 Mn, +25.4% (derived) |
| 07-Nov-2025 | Q2 FY26 PR p.3 | Strong H2 FY26 margin improvement | delivered | H2 8.75% vs H1 7.13% (derived) |
| Jul 2022 | Jul-2022 call p.6 | Second foil rolling mill, 700 MT a month | delivered | 8,400 tpa = 700 MT a month (May-26 call p.4) |
| 14-Aug-2025 | AR25 p.24 | Fire loss 150 to 200 Mn, fully insured | partial | loss 167.2 Mn in range; claim 793.05 L, 47.4%, nil received (B03) |
| Jul 2022 | Jul-2022 call p.18 | Foil revenue ₹240 to 250 Cr with the second mill | partial | FY26 foil revenue ₹215 Cr (AR26 C p.226) |
| 14-Aug-2025 | AR25 p.18 | Conductors positive momentum with better margins | missed | segment margin 4.86% vs 8.27% (AR26 C p.226-227) |
| 07-Nov-2025 | Q2 FY26 PR p.3 | Conductors H2 FY26 revenue to double vs H1 | missed | 520 vs 480 Mn, +8% (derived) |
| 13-Feb-2026 | Q3 FY26 PR p.3 | Conductor execution pick-up by end March | missed | Q4 FY26 276 Mn, -26% YoY; Q1 FY27 171 Mn |
| 07-Nov-2025 | Q2 FY26 PR p.3 | Utilisation about 90% in H2 FY26 | missed | powder about 80%, conversion about 45% (May-26 call p.16) |
| 07-Nov-2025 | Q2 FY26 PR p.3 | LT cable trials Dec 2025, launch Q4 FY26 | missed | production began 7 Jul 2026; BIS pending |
| 07-Nov-2025 | Q2 FY26 PR p.4 | Umred LVPC commercial production H2 FY27 | missed | moved to H1 FY28 (Q3 FY26 PR p.5) |
| 13-Feb-2026 | Q3 FY26 PR p.4 | PGCIL registration early Q1 FY27 and MEPL ramp Q1 FY27 | missed | moved to Q2 and Q3 FY27 (May-26 call); Q1 FY27 insulator revenue 5 Mn |
| Jul 2022 | Jul-2022 call p.6 | No external borrowing, expansion from accruals | missed | FY26 gross debt 18,452.46 L, 76.6% short-term (B03) |
| Jul 2022 | Jul-2022 call p.7 | Working capital cycle 60 to 70 days | missed | FY26 cycle 102.5 days (B03 derived; basis may differ) |

Tally from B05: 7 delivered, 2 partial, 9 missed. Verifier B would move the two-part MEPL promise from delivered to partial, which gives 6, 3 and 9 (B12b). Verifier B also lists untracked pledges: foil conversion utilisation flat at 45 to 50% since 2022, and the 2022 pledges of 5x asset turn, gross margin near 27% and positive free cash flow in FY24 (B12b).

### 6. RESTATED BASES

No restatement for a reorganisation, transfer or reclassification is shown (B02 restatements_found: "None material"). Printed notes:

- "56 Previous years audited figures has been regrouped / recasted / rearranged wherever necessary to make them comparable for the purpose of preparation and presentation of standalone financial statements." (Annual_Report_2026.pdf p.160).
- "59 Previous years audited figures has been regrouped / recasted / rearranged wherever necessary to make them comparable for the purpose of preparation and presentation of consolidated financial statements." (p.244).
- "there was no change in the nature of business of the Company" after incorporation of MMP Cables and MMP Alutech (p.26).
- Comparative as printed in the latest filing: "Total Revenue from Operations…(`) 82,168.59 69,185.99" standalone (p.132) and consolidated segment "c) Total Revenue ... 82533.67 ... 69,290.62" (p.226).
- Comment: FY25 comparatives differ from AR25 by under 2 L in several lines (standalone total assets 50,553.98 vs 50,554.05; MSME payables 833.86 vs 832.28; B02). The Insulators segment has no FY25 revenue line ("-") in the AR26 segment note (p.226).

### 7. CORPORATE-ACTION CLAUSES

No scheme, demerger, merger or share repurchase is in the corpus.

- Share repurchase: the AR lists the SEBI 2018 regulations on repurchase of securities as "Not Applicable to the Company during the audit period" (Annual_Report_2026.pdf p.45, secretarial audit list item g).
- Preferential issue: "The Company has not made any preferential allotment or private placement of shares or convertible debentures" (p.89, CARO).
- Intra-group capital actions: MMP Cables and MMP Alutech incorporated as wholly owned subsidiaries (p.26). Equity "MMP Cables Private Limited ` 500.00", "MMP Electricals Private Limited ` 400.00", "MMP Alutech Private Limited ` 25.00" and "Preference Shares in Wholly Owned Subsidiary ... MMP Electricals Private Limited ` 500.00" (p.153).
- Definitions of undertaking, liability allocation, ratios, appointed and effective dates: not applicable, no scheme in the corpus. To fetch if the operator suspects one: NSE and BSE Reg 30 filings for any scheme of arrangement, and MCA filings.

### 8. RELATED-PARTY PERIMETER (Annual_Report_2026.pdf Note 45, standalone, p.150 to 155; INR Lakhs, FY26 with prior year)

| Entity or person | Nature | FY26 amount (prior year) |
|---|---|---|
| Star Circlips and Engineering Ltd (associate, 26.06%) | Purchases; job work receipts; dividend income; dividend paid | 01.49 (03.68); 277.06 (262.49); 09.98 (49.91); 23.16 (17.37) |
| Toyal MMP India Pvt Ltd (associate, 26.00%) | Sales of goods; trade receivable | 1,801.51 (2,027.19); 03.45 Dr (43.77 Dr) |
| MMP Electricals Pvt Ltd (subsidiary) | Reimbursement incurred; repayment; equity; preference shares; loans granted and repaid | 192.49 (553.85); 312.46 (325.00); 400.00 (100.00); 500.00 (NIL); 125.00 (285.00) and 125.00 (NIL) |
| MMP Cables Pvt Ltd (subsidiary) | Reimbursement incurred; repayment; equity; loans granted and repaid; service offered | 1,139.54 (NIL); 667.79 (NIL); 500.00 (NIL); 90.00 and 90.00 (NIL); 05.92 (NIL) |
| MMP Alutech Pvt Ltd (subsidiary) | Reimbursement; unsecured loan received and repaid; equity | 03.60; 24.00 and 20.40; 25.00 (all PY NIL) |
| Mayank Fasteners Pvt Ltd (promoter-linked) | Office rent; dividend paid | 03.00 (00.90); 95.69 (71.77) |
| Rohini Farms and Agriculture Pvt Ltd (listed in the table as Rohini Horticulture Pvt Ltd) | Dividend paid | 02.48 (01.86) |
| Arun Bhandari (MD) | Remuneration; dividend | 134.40 (134.40); 139.19 (104.39) |
| Lalit Bhandari (WTD) | Remuneration | 35.13 (35.37) |
| Mayank Bhandari (non-executive director) | Dividend | 11.31 (08.48) |
| Rohini Bhandari (non-executive director) | Legal and professional charges; dividend (relative column) | 30.00 (30.00); 04.48 (03.36) |
| Saroj Bhandari, Sakshi Bhandari, Vivaan Bhandari (relatives) | Salary; dividend | Saroj 61.98 (61.98) and 65.12; Sakshi 25.83 (25.78) and 07.81; Vivaan dividend 29.19 (21.89) |

Terms printed (p.151): "Purchases from and sales to related parties are undertaken on terms equivalent to those applicable to unrelated parties, on arm's length basis." Comment: B02 notes the 255.21 L paid to promoter family and entities, 5.5% of pre-exceptional PBT (derived), a 30.00 L related-party loan absent from the balance table, about 580 L of subsidiary reimbursement flows with no closing balance, and an arm's-length method not stated (B02 rank 10).

### 9. PLEDGE AND SHAREHOLDING (inputs/shareholding/SHP_MMP_2026-06-30.md; NSE XBRL, submitted 11-Jul-2026, revised 13-Jul-2026)

Promoter and group holding as filed: 30-Jun-2026 74.49; 31-Mar-2026 74.48; 31-Dec-2025 74.48; 30-Sep-2025 74.48; 30-Jun-2025 74.48; 31-Mar-2025 74.48; 31-Dec-2024 74.48; 30-Sep-2024 74.48. 31-Mar-2024 74.48 comes from AR25 note 16(d) p.112 (B01). Comment: eight quarters are held in the SHP table plus one from AR25. NOT DISCLOSED in the corpus for the remaining quarters of the twelve (Sep-2023, Dec-2023, Jun-2024), reason: the NSE table starts at 30-Sep-2024 and no earlier pattern is held (B01 gap list).

Pledge: "WhetherAnySharesHeldByPromotersAreEncumberedUnderPledged: false", and the five other encumbrance fields read false at 30-Jun-2026 (SHP). The SAST Reg 31(4) letter of 06-Apr-2026 says no encumbrance was created in FY26 (B08). Pledge for the other quarters is NOT DISCLOSED in the corpus, reason: the NSE table carries holding percentages, not pledge, for earlier dates.

Institutional holding, latest (30-Jun-2026): "InstitutionsForeign | 2 | 4995 | 0.0002" (FPI, 2 holders, 4,995 shares, 0.02%). No domestic institution row appears in the converted facts (B08: no institutional entry). Public holding is "PublicShareholding | 11192 | 6480834 | 0.2551".

### 10. VERIFICATION

Documents quoted in this annex, with dates:

- Annual_Report_2026.pdf, FY2025-26, filed 18-Aug-2026 (Board's report dated 10-Aug-2026).
- Annual_Report_2025.pdf, FY2024-25, filed 14-Aug-2025 (cited through B01 and B05 only).
- Concall_May_2026_Transcript.pdf, call held 25-May-2026.
- Concall_Jul_2022_Transcript.pdf, July 2022 (cited through B05 only).
- MMP_10082026134252_MMPILPressRelease30062026 (Q1 FY27 press release), 10-Aug-2026.
- MMP_13082026171648_MMPILInvestorPPT30062026.pdf (Q1 FY27 deck), 13-Aug-2026.
- inputs/shareholding/SHP_MMP_2026-06-30.md, submitted 11-Jul-2026, revised 13-Jul-2026.
- Q2 FY26 and Q3 FY26 press releases (07-Nov-2025 and 13-Feb-2026) and AR25, cited through B05 only.

CORPUS COMMIT HASH: f65dc68863d4a9363cf1c2733c979629e0eab59f
