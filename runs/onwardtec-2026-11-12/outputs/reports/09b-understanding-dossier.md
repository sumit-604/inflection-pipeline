# Halt 1 Understanding Dossier: Onward Technologies Ltd (ONWARDTEC)

Run date: 2026-11-12. Stage 09b, assembly only. Sections 1 to 5 draw on committed blocks (B00 to B09, B12a to B12d, confidence, B13). Section 4e carries labelled inference. Section 6 is the annex and quotes the corpus. No pricing, worth or decision language appears here. The Mental Model in Section 2 is a draft and is not signed.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

Inventory only. Source: B00 (inventory, input_gaps, corpus_manifest, freshness_pairs). Today is 2026-11-12.

1. CONCALLS (B00.concall_quarter_map)
   - Concall_Jan_2026_Transcript.pdf: Q3 FY26, call 16 Jan 2026.
   - Concall_May_2026_Transcript.pdf: Q4 FY26, call 5 May 2026.
   - Concall_Jul_2026_Transcript.pdf: Q1 FY27, call 16 Jul 2026.
   - Concall_Oct_2026_Transcript.pdf: Q2 FY27, call 16 Oct 2026.
   - Most recent quarter covered: Q2 FY27 (quarter ended 30 Sep 2026). The next quarter, Q3 FY27, ends 31 Dec 2026, so it has not reported. The prior-year Q3 call was 16 Jan 2026 (B00). No more recent transcript is plausibly missing.
   - Peer concalls held for context: 11 (LTTS 3, Tata Technologies 4, Cyient 4; B00.inventory).
2. ANNUAL REPORTS: Annual_Report_2026.pdf (FY26, year ended 31 Mar 2026, 35th AGM) and Annual_Report_2025.pdf (FY25, 34th AGM). The latest completed FY is present. Two years are held, which is fewer than three. FY21 to FY24 reports are absent (B01.input_gaps, B03.input_gaps).
3. RESULTS FILINGS: latest is Results_Q2FY27_BoardOutcome_2026-10-16.pdf (quarter and half year to 30 Sep 2026). Also held: Q1 FY27 board outcome dated 2026-07-16 (scanned image, no OCR; B00) and Q4 FY26 results (audited FY26). Quarter-gap between the latest results and the latest AR: two quarters (Q1 FY27 and Q2 FY27) are filed after the FY26 AR, and both are held.
4. INVESTOR PRESENTATIONS: Investor_Presentation_1.pdf, the Q2 FY27 earnings presentation, transmittal dated 16 Oct 2026 (B00). Earlier decks are absent.
5. RESEARCH / RATING: no broker or research note held (research/ empty). Rating: ICRA rationale dated 2023-03-27 and ICRA withdrawal dated 2023-11-13. No live rating exists (B00.input_gaps).
6. CORPORATE ACTIONS (announcements/, hand-filled, not the full Reg 30 record): Q4FY26, Q1FY27 and Q2FY27 press releases; Buyback_Board_Outcome_2026-05-12.pdf, Buyback_Letter_of_Offer_2026-05-20.pdf, Buyback_Extinguishment_2026-06-15.pdf. Range: 12 May 2026 to 16 Oct 2026. Shareholding: SHP_Q2FY27_Sep2026.pdf only (quarter ended 30 Sep 2026). Screening: four Data_Sheet CSVs (Onward, LTTS, Tata Technologies, Cyient; FY26).
7. FRESHNESS PAIR CHECK (B00.freshness_verdict = FRESHNESS PAIRS OK). All four pairs read PASS: results to concall (Q2 FY27 results with the Q2 FY27 transcript), rating bulletin to rationale (the withdrawal document is the full ICRA rationale; rating is withdrawn, not live), SEBI order to order text (no SEBI order referenced at stage 0), AR to latest audited annual results (FY26 AR with Q4 FY26 results). No pair failed.

EMPTY OR HAND-FILLED FOLDERS (full list, repeated for the operator; the stage-0 question was suppressed under the /step1 standing default "continue with the gaps"):
- prospectus: empty. Not expected (long-listed company, incorporated 1991).
- research: empty. No broker notes.
- announcements: hand-filled from onwardgroup.com. The collector BSE fetch failed. It is not the full Reg 30 record and is never evidence that nothing else was filed.
- shareholding: one quarter only (Sep 2026), hand-filled.
- results: hand-filled. The Q1 FY27 file is a scanned image; tesseract is absent, so stages read the PDF pages directly.
- rating: withdrawn 2023. No live rating.
- screening: Data_Sheet CSVs only. The screener Profit and Loss, Quarters, Balance Sheet and Cash Flow exports came out empty (formulas with no cached values) for Onward and all three peers.

8. VERDICT LINE
CORPUS GAPPED: findable-but-missing documents (operator upload list): (a) FY2021 to FY2024 annual reports, from BSE or the company IR page (B01, B03, B08 all name this; it blocks the 10-year ROCE, free cash flow and working-capital series and the promoter path from 61.71% to 38.12%); (b) shareholding patterns before Sep 2026, in particular Sep 2023 (the E2 input) and the 12-quarter pledge and holding history, from BSE; (c) the full Reg 30 announcement record, including the 2021 EGM notice, the Investment Agreement dated 2021-05-27 with Infinity Direct Holdings, and Reg 29 and bulk-deal records for Jun 2023 to Mar 2024, from BSE; (d) the Q2 FY27 Corporate Governance Report (Audit Committee chair after 2026-07-20 is NOT FOUND), from BSE; (e) screener Profit and Loss, Quarters, Balance Sheet and Cash Flow exports for Onward and the three peers, from the collector (open Financials.xlsx, save, run --push-again); (f) Arihant Capital March 2026 conference notes (B05 gap), source unknown. Plausibly nonexistent or not expected: prospectus (long-listed company); broker research (none held; the absence is a leads gap only); a live credit rating (ICRA withdrew in 2023, which is itself a data point on external scrutiny).

OPEN ITEMS carried from confidence.yaml (stated, not analysed):
- Verifier C did not audit B01 run 2. A second Verifier C run needs operator approval (verifier cap). Proposed scope: the Gate 0 half only, on 01-gate0.md run 2.
- The Gate 0 class depends on missing inputs. It reads AVERAGE if a full 10-year series is demanded (core 55) and EXCELLENT in the other sensitivity (core 84). Headline GOOD+ at core 79 (B01). Closing documents: FY2017 to FY2023 annual reports, the Sep 2023 shareholding pattern, the screener re-export.
- Verifier A MINOR anchor slips in the 05, 06, 04, 07 and 09 reports were not edited; corrected pages sit in B12a.
- Verifier A shadow was not run (claimed by another session; .claude/shadow.yaml untouched).
- The one remediation cycle of this Phase 1 is used and closed (stage 1 re-run, E4 input corrected to Rs 394.68 lakhs; stage 5 anchor corrected from p.4/p.8 to p.3/p.9). A second cycle is refused (confidence.yaml.remediation).
- Peer utilisation is the lowest confidence component: 7 of 11 peer transcripts used in substance (B12d, B06 coverage map).
- B08 and B09 carry status partial (blocked fetches, assumed SAM filters).

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT - PENDING OPERATOR SIGN-OFF**

This declaration is a draft. It is signed only in claude.ai after live-web stress-testing. Nothing here marks it signed.

### PART A: THE FROM STATE

A1. ARCHETYPE. One line, one reporting segment ("a single segment i.e., for the ER&D and Digital services", AR26 p.93; Q2 FY27 results p.3). Archetype: Outsourcing partner (CDMO/EMS/IT services), with the variables client concentration, wallet share, capacity fill, contract stickiness and price per unit (B04: services, 88% time and material in FY26, asset light, pricing power weak). The three verticals (industrial equipment and heavy machinery 63%, transportation and mobility 34%, healthcare 3% of FY26 revenue, AR26 p.46) share this archetype. The run does not split the archetype by vertical.

A2. THE SIMPLE ANALOGY. Onward rents out teams of engineers by the month, the way a factory owner might rent a team of skilled toolmakers who learn the factory's own machines. The factory owner pays for the hours (88% of FY26 revenue, B04). The team stays for years, because it knows the machines (engagements of 5 to 8 years, B04). The rental firm earns its margin from the gap between what it pays the toolmakers and what it bills. About 70% of the work is done from Indian centres, where pay is lower (B04). One large factory owner supplies 18.3% of the bill (B03).

### PART B: THE TRANSITION

B1. FROM to TO (Quality Ladder, CLAUDE.md). Single line. FROM: R2 (cost-advantaged). Margin comes from a cost position, namely offshore delivery on a mostly fixed pay cost, not from price. B04 rates pricing power weak and calls the offshore cost edge "low durability, every peer has the same arbitrage". ROCE ran 19.84%, 14.97%, 20.06% over FY24 to FY26 (B01). TO as claimed: R3 (value-added, spec'd supplier). Management points to digital engineering, wallet share in strategic accounts and revenue per employee of Rs 30-40 lakh as an aspiration (B05, guidance table, aspiration without a period). This is one rung, inside the base rate of one rung per 2 to 3 years. The rung mapping is this draft's reading. Management does not state rung labels. The operator may change it at sign-off. B07 scores the forward moat evidence at 12.4 (MODEST), carried by two categories at Moderate strength: qualification lock-in and customer ecosystem (B07).

B2. THE ENGINE. Two things physically change.
1. Offshore leverage and utilisation on a mostly fixed pay cost. Employee cost fell to 69.4% of revenue in Q2 FY27 from 72.8% in FY26 (B04). The sequential gain ex-credit is real: margin ex the R&D credit rose from 12.3% (Q1) to 13.9% (Q2) (B05). The filed offshore share did not support the offshore explanation: it fell from 72% to 69% year on year (B04, B05, B07).
2. Wallet share through large multi-year programmes: a Rs 33 Cr offshore development centre for a power-management maker and a Rs 44.5 Cr three-year renewal, up 72% (B05, B07). Clients above USD 1 mn rose from 16 to 18 (B05).

B3. THE PROOF GATE. Not fired. Metric: EBITDA margin excluding the UK R&D credit and other one-offs, at or above 14.0% in each of Q3 FY27 and Q4 FY27, read together with offshore share at or above 72% (B05 trigger 2 confirm signal; B07 optionality register). Supporting reads: employee cost ratio ex-credit under 71% (B05), DSO under 75 days by Q3 FY27 (B05 trigger 3). Reference points: FY26 ex-credit margin 12.96% (B03); Q2 FY27 ex-credit 13.87% to 13.9% (B01, B04, B05); guidance band 13.8% to 14.3% (B05). FTTCP tests this gate. Until it fires, the transition is narrative.

B4. THE RECOGNITION GAP (open question; Stage 11 resolves it via the PE gap). Does the TO state (the R3 neighbourhood) already look reflected in the market's pricing of the shares? This dossier states no number and no conclusion. If TO is already reflected, the re-rating engine is spent and only earnings growth remains. Stage 11 confirms or denies this by comparing the current PE with the PE gap the ladder implies.

B5. THE UGLINESS TEST. The ugly optics today: Q2 FY27 ex-credit margin 13.9% against 14.3% a year earlier (B05); H1 FY27 operating cash flow Rs 1,844.79 lakhs against Rs 3,502.46 lakhs (B05); DSO 80 days against a 65-70 day goal (B04); unbilled revenue growing faster than revenue (B02); one customer at 18.3% (B03). Classification: ARTIFACT-OF-CLIMB, provisional and not settled. Evidence for the classification: the cash drop sits with a fast ramp (432 net hires; receivables and unbilled up Rs 2,867.01 lakhs in H1; B04, B05), and the peers show DSO of 78 to 102 days and unbilled build-ups during their own ramps (B06 verified). Evidence against, which keeps it provisional: unbilled outgrew revenue (13.2% against 10.7%) and subsidiary billed days rose from 70.1 to 81.3 in FY26, before the ramp (B02); the auditor could not comment on the audit trail of the revenue billing system for a second year (B02, B03); the 18.3% customer is a permanent feature until the contract terms are known (B03). Two readings, one separator: Q3 FY27 DSO under 75 days supports the growth-induced reading. DSO above 80 days, or unbilled outgrowing revenue again, moves the read toward STRUCTURAL-FEATURE (B13.falsification_metric).

B6. THE TRANSITION FALSIFIER. Q3 FY27 EBITDA margin ex-credit at or below 13.0%, with offshore share still under 72% (B13.falsification_metric; B05 trigger 2 kill signal). Second kill condition: top-5 client share above 50% or the single-customer share above 20% (B05 trigger 4 kill signal). Either shows the margin gain was the credit, currency and a peak, not an engine.

### PART C: WHAT THE MODEL WATCHES

C1. DOMINANT VARIABLES (these become the Role 5.5 tracker signals).
1. Ex-credit EBITDA margin with offshore share and employee cost ratio. State: 13.87% ex-credit in Q2 FY27, offshore 69% (B01, B04). Guidance basis (credit inside or outside the 13.8-14.3% band) is NOT FOUND (B05).
2. Revenue conversion of the hiring ramp and the large programmes. State: the Q2 run rate would give an H2 of about Rs 340 Cr; the 15-18% guide implies H2 of about Rs 306-322 Cr (B04, derived there). Q3 FY27 revenue against Rs 170 Cr separates the two readings of FY27 (B05 trigger 1; B09).
3. Cash conversion: DSO and unbilled against revenue. State: DSO 80, H1 CFO down about 47%, CFO/EBITDA about 41% (B05).
4. Client concentration and wallet share. State: one customer 18.3%, top 5 at 48%, top 25 at 87%; clients above USD 1 mn at 18 (B03, B05).

C2. WHAT THE MODEL REJECTS.
- Market size. B09 rates the runway STRONG, but every SAM filter is an assumption and the binding limits are concentration and utilisation, not market size or capacity (B09, B13 narrative). Questions on the size of the pool are noise.
- Reported ROCE of 25.42% and interest cover of 1.68. B03 and B04 call both not reproducible and say to use revenue per head, margin ex-credit and tax-adjusted PAT.
- Gross margin and inventory ratios. There is no cost of goods (B04 irrelevant_ratios).
- Management's market figure of Rs 23.67 lakh Cr, 30.7 times the vendor pool (B09).
- The "fastest organic growth" claim, which B06 contradicts for the current period only. The window is untestable.
- The backward Gate 0 class as a driver of the thesis. It is input-gap sensitive (B01, confidence.yaml).

C3. THE BUSINESS FALSIFIER (kills the starting business, not the arrow). Evidence that Onward is not a diversified outsourcing partner but a captive vendor to one OEM: the 18.3% customer's share rising toward a majority of growth, or its contract lapsing without a replacement, would force a re-declaration of the FROM business itself (B03, B02). A third audit-trail carve-out on the revenue billing system, or a qualified opinion, would force a re-declaration of whether reported revenue and unbilled are reliable (B02, B03 monitorable). Neither is the transition falsifier in B6.

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

Drafted at Halt 1 from B01 to B09 per the shared spec in prompts/13-synthesis-pipeline.md. Stage 13's copy remains the final version.

Onward offers engineering work done by teams of engineers: product design, testing, embedded electronics and software, and digital engineering for the products its clients make (B04). Most of it, 88% of FY26 revenue, is billed by time and material, and 12% is fixed price, a share that reached 15% in Q2 FY27 (B04). The customer keeps the same team for years because the engineers learn its products and processes, and engagements run 5 to 8 years (B04). The 72 active clients sit in three groups: industrial equipment and heavy machinery makers (63% of FY26 revenue), transportation and mobility makers (34%) and healthcare companies (3%) (AR26 p.46, as carried in the final business narrative). The top 5 clients give 48% of revenue and the top 25 give 87%, and one unnamed customer gave 18.3% in FY26, up from 12.7% in FY24 (B03, B02). These customers hold the approvals and the rate cards, and no volume floor is disclosed (B02, B03). Present demand comes from original equipment makers that outsource engineering, a global vendor pool of USD 81.5 bn in 2024 (B09 stale_data_flags). Two disclosed contracts show where the work comes from: a Rs 33 Cr offshore centre for a power-management maker's data-centre unit, and a Rs 44.5 Cr three-year renewal with a construction and mining equipment maker (B05, B07). They tie to the tracker signals "Order backlog of data-centre power and cooling OEMs", "Hyperscaler data-centre capex guidance" and "Construction, mining and heavy machinery OEM order books and R&D spend" (B09). Demand should grow with the outsourced engineering pool, which the run sizes at 8.6% a year, and the "Nasscom/Everest ER&D market releases" signal updates that input (B09). Peer calls partly confirm the data-centre and energy pull, so "Peer ER&D services quarterly revenue and deal wins" is the earliest outside check (B06, B09). Management says "US PERM and onsite work rules" push work offshore, but the run found no peer that confirms the link, and the filed offshore share fell from 72% to 69% (B06, B07). The rupee added 4.7 points to reported growth in the September quarter, and the "USD/INR" signal tracks that (B09). The moat scan scores 12.4, rated MODEST and only 0.4 above its line, resting on qualification lock-in from three-year contracts and on embedded customer relationships (B07). The time and material line has moderate switching cost and no evidenced pricing power, and its offshore cost edge is one every peer shares (B04). The fixed price line and the healthcare line show no moat in the run, and the cannibalisation tests I1 and I2 scored zero, because a larger rival could quote the same offshore centre and give up no existing revenue (B04, B07).

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. VERTICALS FRAMED (one per dominant variable)

**Vertical 1: Ex-credit margin, offshore share, employee cost ratio**
- Corpus establishes: Q2 FY27 margin 15.6% reported, 13.87% ex the Rs 2.93 Cr credit (B01, B04). H1 FY27 ex-credit margin 13.1% against 13.6% in H1 FY26 (B04). Offshore share down 72% to 69%; fixed price up 11% to 15% (B04). FY26 ex-credit margin 12.96% (B03). Peers book increments at 50 to 100+ bps of margin (B06). Guidance 13.8% to 14.3% for FY27 (B05).
- Corpus cannot establish: whether the guide counts the credit (about 100 bps of H2 margin; B05); utilisation by centre (B06, B07); fixed-price margin against time and material (B04); the currency basis of the guide (B12b F1: reported growth 22.4% against 17.7% constant currency).
- Deciding questions: (1) Is the Rs 2.93 Cr credit inside the 13.8-14.3% band? (2) What produced the sequential gain: utilisation, rate or currency? (3) Does ex-credit margin hold at or above 14.0% in Q3 and Q4 FY27 with offshore at or above 72%?

**Vertical 2: Revenue conversion of the ramp and the large programmes**
- Corpus establishes: guide 15% to 18% (raised) against H1 FY27 growth of 17.5%; H2 implied by the guide sits flat to 4% below H1 (B05). 432 net hires in H1 (B04). Rs 33 Cr ODC and Rs 44.5 Cr renewal (B05, B07). Two readings of FY27 revenue, Rs 625-642 Cr against a flat run rate of Rs 660 Cr (B09).
- Corpus cannot establish: customer names (NDA; B07, B09); price versus scope in the Rs 44.5 Cr renewal (B04, B07); ODC status after the Q1 call (B05 dropped triggers); data-centre share of revenue (B04, B09).
- Deciding questions: (1) Does Q3 FY27 revenue reach Rs 170 Cr or more, with Q4 above Q3 (B05 trigger 1)? (2) What utilisation and billing lag sit on the 432 hires? (3) Does the ODC reach full revenue in Q3 as stated?

**Vertical 3: Cash conversion (DSO and unbilled)**
- Corpus establishes: FY26 CFO 1.47x PAT, with 15.3% of CFO from unpaid pay accruals (B02, B03). H1 FY27 CFO Rs 1,844.79 against Rs 3,502.46 lakhs, DSO 80 against 70 in Dec 2025 (B05). Subsidiary billed days 70.1 to 81.3, of which up to about 5 days is currency (B02, B03). Peer DSO in ramps 78 to 102 (B06). Management goal 65-70 days within two quarters (B05).
- Corpus cannot establish: customer share of receivables and unbilled (B02, B03); ageing of unbilled; which approvals are delayed.
- Deciding questions: (1) Is Q3 FY27 DSO under 75 days? (2) Does unbilled grow slower than revenue? (3) Does CFO/EBITDA return above 70% (B05 trigger 3)?

**Vertical 4: Client concentration and wallet share**
- Corpus establishes: one customer 18.3% (Rs 9,965.52 lakhs of Rs 54,385.24 lakhs), up from 12.7% in FY24; top 5 48%; top 25 87% (B02, B03). Clients above USD 1 mn: 16, 18, 18 (B05). The single-customer share was never disclosed on the calls and the risk table is silent (B03, B05).
- Corpus cannot establish: the customer's name, vertical, contract term and renewal date, volume floor, receivable share (B02, B03, B04).
- Deciding questions: (1) What share of unbilled and receivables sits with the 18.3% customer? (2) When does its contract renew? (3) Does top-5 share stay at or below 48% (B03 monitorables)?

### 4b. CANDIDATE SIGNAL TABLE (7 B09 candidates; all UNVERIFIED)

Verification and tracker writes happen at Role 5.5 in claude.ai. "Likely source" is B09's entry; the match to the Downstream_Source_Discovery_Protocol registry is made at Role 5.5.

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| Order backlog of data-centre power and cooling OEMs | Backlog flat or falling for two consecutive quarters while the Onward ODC is ramping | Quarterly | OEM quarterly filings, SEC EDGAR (B09) |
| Hyperscaler data-centre capex guidance | Guidance cut, or lower sequential capex, for two consecutive quarters | Quarterly | Hyperscaler 10-Q and earnings calls; Dell'Oro (B09) |
| Construction, mining and heavy machinery OEM order books and R&D spend | Class-level order books and R&D spend down year on year for two consecutive quarters | Quarterly | OEM quarterly filings, SEC EDGAR (B09) |
| Peer ER&D services quarterly revenue and deal wins | Two of three peers (LTTS, Tata Technologies, Cyient) report falling constant-currency revenue, or rate concessions on renewals | Quarterly | BSE/NSE filings and concall transcripts (B09) |
| US PERM and onsite work rules | Rule not enacted or delayed, or offshore share stays under 72% for two quarters after it takes effect | Event-Driven | USCIS, Department of Labor, Federal Register (B09) |
| USD/INR | Gap between reported and constant-currency growth (4.7 points in Q2 FY27) closes to nil, removing the currency lift from reported growth | Monthly | RBI reference rate (B09) |
| Nasscom/Everest ER&D market releases | Outsourced-pool growth restated below the 8.6% input | Event-Driven | Nasscom Strategic Review; Everest Group ER&D reports (B09) |

### 4c. FRAGILITY READ

- variable_count: 6 external variables must go right for the bull case: data-centre OEM demand; heavy-machinery OEM R&D spend; retention and renewal of the 18.3% customer; US onsite-work rules (offshore mix); USD/INR; no AI-linked rate or hours pressure on an 84-85% time-and-material book (B09, B05, B06, B03, B04).
- verifiability_ratio: 4 of 6 externally observable (data-centre OEM demand, heavy-machinery OEM spend at entity-class level since customer names are NOT FOUND, US rules, USD/INR). Two are company-narrated or only partly observable: retention of the 18.3% customer and the AI pressure on Onward's own rates (peer calls give only partial cover; B06).
- single_point_failure: yes. The 18.3% customer. A cut or loss alone breaks the revenue and margin legs, and the run found no disclosed volume floor, contract term or renewal date (B02, B03). Its share rose from 12.7% to 18.3% in two years.
- fragility_verdict: FRAGILE (one kill-switch variable, per the rule). The read is on structure, not on company quality.

### 4d. RESEARCH BRIEF (the claude.ai work order; live web only)

1. PENDING LIVE VERIFICATION (Chain 1, Section 4e). Open the latest quarterly filing (10-Q or earnings release) of the power-management maker whose data-centre unit is the client of the Rs 33 Cr ODC, plus the latest hyperscaler capex guidance. The client name is NOT FOUND in the corpus (NDA; B07). Identify it from the Q1 FY27 press release or deck wording first, or ask management.
2. PENDING LIVE VERIFICATION (Chain 2, Section 4e). Open the Q3 FY27 investor presentations of LTTS and Tata Technologies for DSO and unbilled during ramps, and Onward's own Q3 FY27 deck (DSO slide, unbilled line) when filed.
3. Chain 3 to build: the construction and mining equipment maker behind the Rs 44.5 Cr renewal (R&D spend, order book). Name NOT FOUND (B07).
4. Chain 4 to build: US onsite-work rules (USCIS, Department of Labor, Federal Register) against the filed offshore share fall from 72% to 69% (B07 FLAG-POLICY-CONTRADICTION).
5. Chain 5 to build: AI productivity pass-through on time-and-material contracts (LTTS bids, Tata Technologies commentary) against Onward's 84-85% time-and-material book (B06).
6. Promoter path from 61.71% (Mar 2021) to 38.12% (Mar 2024): Reg 29, Reg 31(4), bulk-deal and SAST records for Jun 2023 to Mar 2024, the 2021 EGM notice and the Investment Agreement dated 2021-05-27. The counterparty to the sale of about 15 lakh promoter shares is NOT FOUND (B08).
7. Audit Committee chair after 2026-07-20 (single press source; successor NOT FOUND) and the Q2 FY27 Corporate Governance Report (B08).
8. UK R&D credit scheme rules, and whether the Q2 FY27 note names the UK (only management names it; B07 gap). Whether peers book such credits inside EBITDA (B06 unverifiable).
9. Currency basis of the 15-18% revenue guide and the FX share of reported growth (B12b F1, MAJOR missed item).
10. Selective-disclosure allegation at the Arihant Capital conference, March 2026: the notes are not in the corpus (B05, B12b F2).
11. Latest USD/INR and the Nov 2026 rate; the 94.68 figure is from a 22 Jun 2026 snippet (B09 FLAG-FX).
12. Nasscom/Everest 2026 ER&D releases for the 8.6% pool growth input; vertical split of outsourced ER&D (NOT FOUND, B09).
13. Employee sentiment and attrition: 14.85% against 37.93% in the same AR (B03, B08). Live review sources are single-source (B08).
14. Sector-cap row ruling (Consulting / Engineering services against Platform / SaaS / IT services, B00.sector_cap_row_evidence) is for the operator at the /fttcp pillar gate, not for web research. Listed so the brief is complete.
15. Operator upload list (not web): FY2021 to FY2024 annual reports, Sep 2023 and earlier shareholding patterns, full Reg 30 record, screener re-export, Q2 FY27 Corporate Governance Report (Section 1 verdict).

### 4e. SECOND-ORDER STUB (Master Prompt v3.7, Rule F)

Labels: [FILED] filed in the corpus; [COMPANY CLAIM] stated by management or the deck; [PENDING LIVE VERIFICATION] needs a counterparty document this container cannot reach; [INFERENCE] reasoning from the cited facts.

```
CHAIN 1: Rs 33 Cr three-year offshore development centre for a power-management maker's data-centre unit (B05 guidance table; B07 catalysts)
Link 1 [COMPANY CLAIM]: The contract is documented in the Q2 FY27 deck, p.14 (B07 anchor), with about 40 engineers to start, billing from Q2 and full revenue in Q3 (B05, Q1 FY27 call). Contract text and client name are NOT FOUND (NDA; B07 gaps).
Link 2 [PENDING LIVE VERIFICATION]: Who pays, and why now. Claude web should open the latest quarterly filing of the power-management maker (name to be identified, see Research Brief 1) and the latest hyperscaler capex guidance, to read the data-centre unit's order backlog and engineering spend. Not read here; no counterparty fact is stated.
Link 3 [INFERENCE]: If that backlog is growing and the ODC bills as stated, then because the work is offshore (the deck cites a 70%+ offshore mix for it, B07), it should help the offshore share and the ex-credit margin. A three-year contract of Rs 33 Cr is small against the Q2 run rate, which would give an H2 of about Rs 340 Cr (B04). It cannot carry the guide raise alone. The raise also needs the renewal and the wider hiring ramp.
Binding constraint: Hiring and billing lag. 432 net hires in H1 FY27 ran ahead of revenue (B04, FLAG-LOW-OPERATING-LEVERAGE-H1). Lab capex of about Rs 25 Cr over two years (B05). DSO at 80 days means billed work is slow to turn into cash (B05).
Unsaid: The Q1 call said the ODC goes live in August. The Q2 call was silent on its status (B05 trigger evolution table, dropped triggers). The data-centre share of Onward revenue is NOT FOUND (B04, B09). Neither call gave a revenue figure for the ODC.
Observation that confirms or breaks this chain, and confirm-by date: The Q3 FY27 deck or call states the ODC as live and billing, and Q3 FY27 revenue from operations is at or above Rs 170 Cr with Q4 above Q3 (B05 trigger 1). Breaks if Q3 revenue is below Rs 160 Cr or the ODC status is again not stated (B05 kill signal). Confirm-by: Q3 FY27 results, expected mid-January 2027 on the prior-year pattern (Q3 FY26 call dated 16 Jan 2026, B00); Q4 read at the Q4 FY27 results.
```

```
CHAIN 2: DSO at 80 days, unbilled up and H1 FY27 operating cash flow down (B05 FLAG-CASH; B02)
Link 1 [FILED]: H1 FY27 CFO Rs 1,844.79 lakhs against Rs 3,502.46 lakhs a year earlier. Receivables and unbilled up Rs 2,867.01 lakhs. DSO 80 against 70 in Dec 2025 (B05). Unbilled at Rs 3,429.35 lakhs in Mar 2026 grew 13.2% against revenue 10.7%, with no ageing or allowance (B02, Note 6).
Link 2 [PENDING LIVE VERIFICATION]: Who pays, and why now. The customers holding the unbilled and delayed approvals are unnamed (receivable share NOT FOUND, B02). Claude web should open the Q3 FY27 investor decks of LTTS and Tata Technologies for peer DSO and unbilled during ramps (Research Brief 2), and Onward's own Q3 FY27 deck when filed. No customer payment fact is stated here.
Link 3 [INFERENCE]: If the cause is the fast ramp and customer approval delays, as management states (B05), DSO falls toward 65-70 as approvals clear and the large programmes move from milestone to routine billing. If the cause is structural, DSO stays above 80 and unbilled keeps outgrowing revenue. The audit-trail carve-out on the revenue billing system (second year; B02, B03) means the unbilled line is the least independently controlled revenue-linked line, so the structural reading cannot be dismissed from the filings alone.
Binding constraint: Unaged, unprovided unbilled (40.0% of net billed receivables, B02). 15.3% of FY26 CFO came from pay accruals that reverse (B02). A gratuity cash call of Rs 1,339.10 lakhs is expected in FY27 (B02, Note 17). The balance sheet has no borrowings, so the constraint is cash timing, not solvency (B01, B02).
Unsaid: Neither the Q1 nor the Q2 call raised the fall in CFO (B05 red flag 2). Management blamed the ramp and approvals but gave no customer split. The footnote that implies a drift nobody mentioned: Note 6 unbilled with no ageing (B02).
Observation that confirms or breaks this chain, and confirm-by date: Q3 FY27 DSO under 75 days and unbilled growth below revenue growth confirm the growth-induced reading. DSO above 80 days, or unbilled growing faster than revenue two quarters running, breaks it (B05 trigger 3; B13.falsification_metric). CFO/EBITDA above 70% is the cash confirmation (B05). Confirm-by: Q3 FY27 results (expected mid-January 2027, B00) for DSO and unbilled; Q4 FY27 results (prior-year Q4 call 5 May 2026, B00) for CFO/EBITDA.
```

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in claude.ai with live web, before Role 2.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. Onward Technologies sells engineering work. Teams of engineers design, test and write software for products that other companies make (B04).
2. It is a small firm. FY26 revenue was Rs 543.85 Cr and it had 2,917 engineers at September 2026 (B09, B04).
3. It bills mostly by the hour or team month. This was 88% of FY26 revenue, and 85% in the September 2026 quarter (B04).
4. Its customers are makers of industrial machines, vehicles and medical devices in North America and Europe. Industrial and heavy machinery makers were 63% of FY26 revenue (AR26 p.46, via the final narrative).
5. Customers keep the same team for 5 to 8 years because the engineers learn their products (B04). That makes the customers loyal. It also makes Onward dependent on a few of them.
6. One customer gave 18.3% of FY26 revenue, up from 12.7% in FY24. The top 25 gave 87% (B03, B02).
7. Demand grows with the outsourced engineering market, which the run sizes at 8.6% a year (B09). Data-centre power work is the new pull, backed by a Rs 33 Cr contract (B05, B07). Peer calls support part of this (B06).
8. Management lifted FY27 growth guidance to 15 to 18%. The first half grew 17.5% (B05). The guide implies a flat or lower second half, so it may be prudent (B04, B05).
9. The moat is thin. Long contracts and embedded teams give moderate switching cost (B07). Offshore cost is an edge every peer shares. There is no evidenced pricing power (B04).
10. The mental model, in one point: Onward claims to climb one rung, from a cost-led engineering supplier to a value-added one, and the margin must prove it. The proof gate is an ex-credit EBITDA margin at or above 14.0% for two quarters with offshore share at or above 72%. That gate has not fired (Section 2).
11. The September quarter margin of 15.6% includes a Rs 2.93 Cr credit. Without it the margin was 13.9%, below 14.3% a year before (B05, B04).
12. Fragility reads FRAGILE. Six outside conditions must hold, four can be watched from outside, and one customer could break the story alone (Section 4c).
13. The corpus could not establish the name or contract terms of the 18.3% customer, whether the margin guide counts the credit, or how the promoter stake fell from 61.71% to 38.12% (B03, B05, B08).
14. The corpus also lacks FY21 to FY24 annual reports and earlier shareholding patterns, so the backward quality score swings from AVERAGE to EXCELLENT with the inputs chosen (B01, confidence.yaml).
15. Biggest open questions: does cash conversion recover from DSO of 80 days, and does margin hold at 14% without the credit? The Q3 FY27 results in January 2027 are the first test (B05, B13).

---

## SECTION 6: STANDING EXTRACTION ANNEX

All figures are in the unit printed on the source document (INR lakhs in results and AR financial statements; INR Crore in the deck). Page numbers are PDF page numbers from the page-marked .txt files unless stated. Anchors carried from stage reports are marked "(via report)". Filenames and quoted filings contain the word "Buyback" as printed.

### 1. UNITS

- Revenue per employee, printed aspiration: "Aspire to achieve ₹30 - 40L Revenue/Employee" (Investor_Presentation_1.pdf p.13). Comment: an aspiration, not a result. No achieved figure is printed.
- Average revenue per client, printed: "1.9 / 2.1 / 2.4" in ₹ cr for Q2FY26, Q1FY27, Q2FY27 (Investor_Presentation_1.pdf p.12, label "Average Revenue per Client (₹ cr)"). Comment: one basket, all clients, not per product.
- Headcount, printed: "2,917 ... Employees" (Investor_Presentation_1.pdf p.5).
- No billed-hours, utilisation, realisation per hour or per engineer is printed (B04 input_gaps: "Realised rate per billed hour or per FTE ... NOT FOUND"). Comment: the business is one basket, a single reporting segment. The volume and revenue lines to derive one: revenue from operations Rs 54,385.24 lakhs for FY26 (Annual_Report_2026.pdf p.93) and an average of 2,533 heads (B04, derived, AR26 p.46-47). B04 derives Rs 21.47 lakh per head for FY26 and about Rs 23.3 lakh annualised for Q2 FY27 on 2,917 closing heads (derived, not printed).

### 2. SEGMENT CAPITAL AND DEBT

- Quote: "the Group evaluates the performance of the Group on the basis of a single segment i.e., for the ER&D and Digital services" (Annual_Report_2026.pdf p.93, Note 34; the same wording in Results_Q2FY27_BoardOutcome_2026-10-16.pdf p.3). Comment: segment assets and liabilities equal the consolidated totals. No segment capital employed is printed.
- Consolidated, INR lakhs, Results_Q2FY27_BoardOutcome_2026-10-16.pdf p.4 (Sep 2026 unaudited; Mar 2026 audited): Total assets 37,652.61 and 37,056.82. Total liabilities 13,008.95 and 11,706.12. Total equity 24,643.66 and 25,350.70.
- Borrowings: none allocated or unallocated as financial debt. The balance sheet shows lease liabilities only: non-current 3,119.98 and 2,933.81; current 1,234.65 and 1,050.52 (same page). The AR26 lease note shows total lease liabilities 3,984.33 at Mar 2026 and 3,215.97 at Mar 2025 (Annual_Report_2026.pdf p.89, Note 28). B01 records no financial borrowings (reconciliation, AR25 PDF p.116). Comment: "Borrowings 39.84 Cr" in the Data_Sheet equals the lease liabilities (B01).

### 3. GUIDANCE VERSUS ASPIRATION

| Item | Quote or as-quoted | Class |
|---|---|---|
| FY27 revenue growth | "We now expect revenue growth of 15% to 18% for FY27 and an EBITDA margin in the range of 13.8% to 14.3%." (Concall_Oct_2026_Transcript.pdf p.4) | (a) guidance, FY27 |
| FY27 EBITDA margin | same quote, p.4; again "We believe we will be between 13.8% and 14.3%." (p.11) | (a) guidance, FY27 |
| DSO | "the sweet spot for us ... is about 65 to 70 days, and I think that will normalize in the next 2 quarters." (Concall_Oct_2026_Transcript.pdf p.13) | (a) guidance, two quarters |
| Revenue per employee | "it was an aspiration, which is a platinum standard in our industry . The INR35 lakhs to INR40 lakhs are what some of the best companies globally do." (Concall_Oct_2026_Transcript.pdf p.10); deck "Aspire to achieve ₹30 - 40L Revenue/Employee" (Investor_Presentation_1.pdf p.13) | (b) aspiration, no period |
| Double-digit revenue and EBITDA growth, mid and long term | "double-digit Revenue and EBITDA growth over mid and long term" (Investor_Presentation_1.pdf p.13) | (b) aspiration, no fixed period |
| FY27 revenue from existing clients | 95% to 98% (via report 05 table 1B; Q4 FY26 call) | (a) guidance, FY27 budget |
| Lab capex for existing clients | about Rs 25 Cr over two years from May 2026 (via report 05; Q4 FY26 call) | (c) capacity |
| Rs 33 Cr ODC | about 40 engineers to start, billing from Q2, full revenue in Q3 (via report 05; Q1 FY27 call) | (c) capacity, with a period |
| Rs 44.5 Cr renewal | 3 years, Aug 2026 to Aug 2029 (via report 05; Q2 FY27 call, deck) | contracted value, not guidance |
| Time and material share | 80% to 90% for the year (via report 05; Q1 FY27 call) | (a) guidance, FY27 |
| Client count | down to 50 "in the next couple of quarters" (via report 05; Q4 FY26 call) | (a) guidance, two quarters |
| Embedded share of revenue | 18% to 30% "in next couple of years" (via report 05; Q4 FY26 call) | (a) guidance, about FY28 |
| Overseas headcount | 125 now, 200 to 300 "in the next few years" (via report 05; Q4 FY26 call) | (c) capability, loose period |
| Headcount near 3,000 at Rs 1,000 Cr revenue | via report 05; Q3 FY26 call | (b) aspiration, no period |
| Healthcare growth | 20% to 50% a year (via report 05; Q1 FY27 call) | (b) aspiration |
| Share repurchase | up to 5,48,780 shares, up to ₹18,00,00,000 (Buyback_Board_Outcome_2026-05-12.pdf p.1) | done, see Question 7 |
| Dividend | Rs 8 per share for FY26 (via report 05; Q4 FY26 call) | declared |

Comment: the guidance basis (credit inside or outside the 13.8-14.3% band) is NOT FOUND in any call (B05).

### 4. CONCENTRATION

- Customer: "Revenue from one customer amounted to ` 9,965.52 Lakhs (March 31, 2025: ` 8,447.58 Lakhs)" (Annual_Report_2026.pdf p.93, Note 34). Total revenue Rs 54,385.24 lakhs (same page). Customer name and vertical: NOT DISCLOSED.
- Top 5, 10, 25 clients, AR chart (Annual_Report_2026.pdf p.12, chart text, label order Top 5, Top 10, Top 25): FY26 "48 / 64 / 87"; FY25 "50 / 66 / 84"; FY24 "50 / 66 / 84". Narrative: "our top 25 clients contribute 87% of revenues" (Annual_Report_2026.pdf p.10). Comment: read in label order; the chart is extracted text, so the operator should confirm the mapping against the printed graphic.
- Deck (Investor_Presentation_1.pdf p.12), Q2FY26 / Q1FY27 / Q2FY27: top 5 "48 / 46 / 47", top 10 "64 / 63 / 63", top 25 "87 / 87 / 87". Clients billed over US$1 mn: "16 / 18 / 18".
- Product or service (revenue by industry, Annual_Report_2026.pdf p.46): IEHM 63%, Transportation & Mobility 34%, HCLS 3% (FY26); 57%, 38%, 4% (FY25). Top vertical share 63%. Contract type: "Time & Material 88% 86% / Fixed Time, Fixed Price 12% 14%" (same page).
- Geography, FY26 customer location (Annual_Report_2026.pdf p.93): India 29,815.23; USA 16,177.39; Europe 1,920.10; Others (Canada, UK) 6,472.52 lakhs. Deck Q2 FY27 (Investor_Presentation_1.pdf p.11): USA 41%, Europe 12%, India 47%. Comment: the AR p.46 shows India 52%, USA 36%, Europe 12%; the basis differs (B04 FLAG-GEOGRAPHY-CONFLICT). The calls say 70% North America and 30% Europe (B05).

### 5. PROMISE LEDGER

Key: K1 = Concall_Jul_2026_Transcript.pdf (call 16 Jul 2026); K2 = Concall_Oct_2026_Transcript.pdf (16 Oct 2026); K3 = Concall_Jan_2026_Transcript.pdf (16 Jan 2026); K4 = Concall_May_2026_Transcript.pdf (5 May 2026); PRES = Investor_Presentation_1.pdf (16 Oct 2026). Anchors are as carried in 05-concall.md (via report); K3 anchors there may use the printed page (PDF page minus one; B12b F7).

| # | Date made | Promise | Status | Evidence anchor |
|---|---|---|---|---|
| 1 | Q3 FY26 call, 16 Jan 2026 (K3 p.5, p.8) | Double-digit revenue and EBITDA growth, FY26 | Delivered | FY26 revenue +10.5%, EBITDA +60.9% (K4 p.3); H1 FY27 revenue +17.5%, EBITDA +21.4% (PRES p.10) |
| 2 | 16 Jan 2026 (K3 p.7) | EBITDA 11-12% for FY26, "12% sustainable" | Delivered | FY26 13.2% (K4 p.3); Q4 alone 11.2% (K4 p.4) |
| 3 | 16 Jan 2026 (K3 p.4) | DSO continues to improve, 70 days | Missed | 75 in Q1 FY27 and 80 in Q2 FY27 (PRES p.9) |
| 4 | 16 Jan 2026 (K3 p.11) and 5 May 2026 (K4 p.7) | Repurchase under consideration | Delivered | Board 12 May 2026; tender closed 29 May; shares extinguished 11 Jun 2026 (Buyback_Board_Outcome_2026-05-12.pdf p.1; Buyback_Extinguishment_2026-06-15.pdf p.5) |
| 5 | 16 Jan 2026 (K3 p.4) | Chennai adds a few hundred seats | Delivered | "fully operational, a few hundred people" (K1 p.9) |
| 6 | 16 Jan 2026 (K3 p.8) | Headcount near 2,500; 3,000 at Rs 1,000 Cr | Partial | 2,917 at Sep 2026 (PRES p.5, p.7) |
| 7 | 5 May 2026 (K4 p.4) | Chennai digital AI lab "in the next couple of months" | Missed | "up and running by Q4 or early 2027" (K2 p.6) |
| 8 | 5 May 2026 (K4 p.16) | Client count down to 50 "in the next couple of quarters" | Missed | 73 (K1 p.5), 70-plus (K2 p.8), 72 (PRES p.5) |
| 9 | 5 May 2026 (K4 p.10) | "very strong visibility for much better performance" | Delivered | H1 FY27 revenue +17.5%, PAT +13.4% (PRES p.10) |
| 10 | 5 May 2026 (K4 p.8, p.14) | Transport vertical returns to growth | Delivered (partial evidence) | Transport share 32% against 34% on higher revenue (PRES p.11), about +15% on rounded shares, derived in report 05 |
| 11 | 16 Jul 2026 (K1 p.6) | Offshore improvement year on year | Missed | Offshore 69% against 72% (PRES p.11) |
| 12 | 16 Jul 2026 (K1 p.10) | Time and material 80-90% this year | Partial | 85% Q2 FY27, 84% Q1 (PRES p.11) |
| 13 | 16 Jul 2026 (K1 p.9) | Fourth Pune centre in August | Partial | Opened in October (K2 p.7) |
| 14 | 16 Jul 2026 (K1 p.6) | EBITDA to improve QoQ and YoY | Delivered | Q2 EBITDA Rs 26.6 Cr, +33.7% YoY (PRES p.8-9); ex-credit margin year on year is 40 bps lower |
| 15 | AR25 (B03, AR25 p.16) | Double-digit revenue and EBITDA growth over three years from FY26 | On track | FY26 revenue +10.7% at the floor, EBITDA +60.7% (B03 guidance table) |
| 16 | AR25 (B03, AR25 p.16) | Capex budget Rs 12 crore for FY26 | Exceeded | Cash capex Rs 1,911.07 lakhs (Annual_Report_2026.pdf p.66, B03) |
| 17 | AR25 (B03, AR25 p.16) | Client count to consolidate at about 80 | Met | 72 active clients (B03) |

Totals on the call-based rows 1 to 14: 7 delivered, 3 partial, 4 missed (B05). Rows 15 to 17 are from the AR and are not in the B05 tally.

### 6. RESTATED BASES

- No restatement, regrouping or reclassification note was located in the held AR26, AR25 or results files (B02.restatements_found is empty; a text search of the AR and results files for "regroup", "reclassif", "restat" returned nothing).
- One presentation change is visible and is not a restatement note. AR26 geography (Annual_Report_2026.pdf p.93) reads: "Within India 29,815.23; USA 16,177.39; Europe 1,920.10; Others* 6,472.52 (* includes Canada and United Kingdom)". The latest results (Results_Q2FY27_BoardOutcome_2026-10-16.pdf p.3) show the same FY26 total but a new grouping for the Mar 2026 column: "North America 18,541.44; Europe & UK 6,028.57". Comment (derived): North America less USA is 2,364.05, and Europe & UK less Europe is 4,108.47; the two sum to the AR "Others" of 6,472.52. So UK revenue moved from "Others" into "Europe & UK". This bears on the Europe 12% against 3.5% conflict in B03.
- The FY26 exceptional item of 315.50 lakhs (labour code) is shown on its own line; the Q2 FY27 note says it was presented as an "Exceptional Item" in the previous year, and prior periods are not recast (Results_Q2FY27_BoardOutcome_2026-10-16.pdf p.2-3, note 4).
- Comparatives as printed in the latest filing (Results_Q2FY27_BoardOutcome_2026-10-16.pdf p.2, quarter ended 30 Sep 2025, INR lakhs): revenue from operations 13,896.89; profit before tax 1,582.67; net profit 1,193.92; six months to 30 Sep 2025 revenue 27,211.97.

### 7. CORPORATE-ACTION CLAUSES

- No scheme, demerger or merger is in the corpus. No preferential issue document is held in inputs/. The 2021 preferential issue to Infinity Direct Holdings was read by stage 8 from the 2021 EGM notice on the company site: "11 lakh shares plus 43 lakh warrants to Infinity Direct at Rs 130, Investment Agreement 2021-05-27" (B08 analyst_note). Filings to fetch: the 2021 EGM notice (dated 2021-06-24), the Investment Agreement of 2021-05-27, and the allotment and warrant-conversion intimations (BSE).
- Share repurchase (in corpus). Board, 12 May 2026: "No. of shares proposed to be bought back 5,48,780 Equity Shares. Buyback price ₹ 328. Maximum Buyback Offer size* Upto ₹ 18,00,00,000" and "tender offer route on a proportionate basis" (Buyback_Board_Outcome_2026-05-12.pdf p.1). Promoters: "The Board noted the intention of the Promoters and members of the Promoter Group of the Company not to participate in the proposed Buy Back." (same page). Ratio: "being 2.41% of the total number of equity shares in the total paid-up equity share capital" (Results_Q2FY27_BoardOutcome_2026-10-16.pdf p.3, note 6).
- Dates: public announcement 13 May 2026, published 14 May; Letter of Offer 19 May 2026; record date 18 May 2026; tendering period 22 May to 29 May 2026; extinguishment 11 Jun 2026; intimation 15 Jun 2026 (Buyback_Extinguishment_2026-06-15.pdf p.1, p.5; Results p.3). Recording: "the Company has extinguished 5,48,780 Equity Shares which were in dematerialized form" and share capital moved from 2,27,60,670 to 2,22,11,890 shares (Buyback_Extinguishment_2026-06-15.pdf p.1).
- Pre and post pattern: promoters "88,90,059 39.07%" before and "88,90,059 40.02%" after (Buyback_Extinguishment_2026-06-15.pdf p.6, Annexure C). Comment: promoters did not tender; their percentage rose from the smaller base.
- Undertaking definitions and liability-allocation clauses: not applicable, no scheme in the corpus.
- ESOP 2024 scheme (approved at the EGM of 6 Feb 2026): options vest 10:20:30:40 over four years, one share per option (Annual_Report_2026.pdf p.93, Note 35). Grant cost 454.68 lakhs over four years (B02).

### 8. RELATED-PARTY PERIMETER

Source: Annual_Report_2026.pdf Note 27 (table on p.88, note opens p.87). INR lakhs, FY26 against FY25.

| Entity (relationship as printed) | Nature | FY26 | FY25 |
|---|---|---|---|
| JHM Enterprises Private Limited (entity having significant influence; promoter holder of 78,75,000 shares, SHP p.4) | Dividend paid | 392.50 | 379.89 |
| Infinity Direct Holdings, Mauritius (entity having significant influence) | Dividend paid | 99.00 | 195.00 |
| Infinity Portfolio Holdings, Mauritius (w.e.f. 27 Sep 2024) | Dividend paid | 96.00 | - |
| PHM Growth Private Limited (entity controlled by KMP) | Rent expense | 53.58 | 51.03 |
| PHM Growth Private Limited | Reimbursement of expenses paid | 9.12 | 8.36 |
| PHM Growth Private Limited | Reimbursement of expenses received | - | 0.30 |
| Desai & Diwanji (entity controlled by KMP) | Professional fees | 9.76 | 3.36 |
| JNTL Consumer Health (India) Private Limited (common director, w.e.f. 8 May 2025) | Revenue from operations | 160.63 | - |
| Mr. Harish Mehta (Executive Chairman) | Short term benefits; dividend | 383.17; 11.00 | 372.24; 10.83 |
| Mr. Jigar Mehta (Managing Director) | Short term benefits; dividend | 459.80; 20.00 | 384.16; 18.81 |
| Ms. Heral Mehta (relative of KMP) | Dividend paid | 12.50 | 12.15 |
| Ms. Prachi Mehta (relative of KMP) | Dividend paid | 7.50 | 7.50 |

Outstanding balances, Mar 2026 against Mar 2025: PHM Growth lease liabilities 49.79 against 92.49 and security deposits 18.82 against 18.82; JNTL trade receivables 10.60 against nil; Harish Mehta short term benefits payable 224.83 against 54.69; Jigar Mehta 275.78 against 218.49 (same page).
Quote: "All transactions with these related parties are priced on an arm length basis." (p.88). Comment: the Infinity entities appear as "significant influence", not as promoter group (SHP p.4 lists 5 promoter holders). A CSR donation of 10 lakhs went to a trust in which a director is interested (p.88). B02 notes that RPT receivables exceed the standalone Note 8 by 345.60 lakhs and that a Canada advance of 358.63 lakhs has no revenue trail (B02).

### 9. PLEDGE AND SHAREHOLDING

- Twelve quarters as filed: NOT DISCLOSED in the corpus. Only one quarterly pattern (Sep 2026) is held; the folder is hand-filled (B00). The points the corpus does carry:

| Date | Promoter and promoter group | Source |
|---|---|---|
| Mar 2024 | 38.12% | Annual_Report_2025.pdf p.147 (B01, B03) |
| Mar 2025 | 38.65% | Annual_Report_2025.pdf p.147 (B01) |
| Mar 2026 | 39.61% | Annual_Report_2026.pdf p.81 (B01) |
| 18 May 2026 (record date) | 39.07% (88,90,059 shares) | Buyback_Extinguishment_2026-06-15.pdf p.6 |
| After extinguishment | 40.02% (88,90,059 shares) | same page |
| 30 Sep 2026 | "(A) Promoter & Promoter Group 5 8945186 ... 40.20" (39.54 fully diluted) | SHP_Q2FY27_Sep2026.pdf p.3 |

  Comment: denominators differ across rows (B01 data note on E2). The promoter share count rose at each date: 85.84, 87.70, 88.90, 89.45 lakh shares (B03).
- Pledge: "Whether any shares held by promoters are encumbered under 'Pledged'? No" (SHP_Q2FY27_Sep2026.pdf p.2, row 7). Nil at Mar 2024, Mar 2025 and Mar 2026 per B03 and B08. Earlier quarters: NOT DISCLOSED.
- Foreign ownership limit used (SHP_Q2FY27_Sep2026.pdf p.6, Table VI): "As on shareholding date 100.00 18.06; previous 1st quarter 18.12; 2nd 18.15; 3rd 18.52; 4th 18.46". This covers the last five quarters (Sep 2025 to Sep 2026) and includes the Infinity entities.
- Institutional holding, latest (SHP_Q2FY27_Sep2026.pdf p.4): Mutual Funds 3 holders, 319,350 shares, 1.44%; Alternate Investment Funds 65,470, 0.29%; Banks 350, 0.00%; domestic institutions sub-total 386,570, 1.74%; Foreign Portfolio Investors Category I 1,896,752, 8.52%; Category II 166,309, 0.75%; foreign institutions sub-total 2,064,311, 9.28%. Public "Foreign Companies" 1,901,629, 8.55%. Employee welfare trust 338,260, 1.52%. Comment: names of holders above 1% are not printed in the held sheet; the Infinity block of 17.37% (B08) is not reconcilable to a single row here.

### 10. VERIFICATION

Documents quoted in this annex, with filename and document date:
- Annual_Report_2026.pdf (FY26, year ended 31 Mar 2026; AR published 22 Jun 2026 per B03)
- Annual_Report_2025.pdf (FY25; cited through B01 and B03 for p.147)
- Results_Q2FY27_BoardOutcome_2026-10-16.pdf (16 Oct 2026)
- Concall_Oct_2026_Transcript.pdf (call 16 Oct 2026)
- Concall_Jul_2026_Transcript.pdf, Concall_Jan_2026_Transcript.pdf, Concall_May_2026_Transcript.pdf (calls 16 Jul 2026, 16 Jan 2026, 5 May 2026; via report 05 only)
- Investor_Presentation_1.pdf (transmittal 16 Oct 2026)
- SHP_Q2FY27_Sep2026.pdf (quarter ended 30 Sep 2026)
- Buyback_Board_Outcome_2026-05-12.pdf (12 May 2026)
- Buyback_Extinguishment_2026-06-15.pdf (15 Jun 2026)
- Buyback_Letter_of_Offer_2026-05-20.pdf (20 May 2026; via B01 only)

CORPUS COMMIT HASH: 93429c143b6f4094e66b8ae2226885930d7b8f2e

---

```yaml
stage: B09b-dossier
company: "ONWARDTEC"
run_date: "2026-11-12"
model: claude-sonnet-5-5
status: complete
corpus_verdict: "CORPUS GAPPED"
corpus_gaps:
  - document: "Annual reports FY2021 to FY2024"
    expected_source: "BSE | company IR page"
    kind: "findable-missing"
  - document: "Shareholding patterns before Sep 2026 (Sep 2023 and the 12-quarter history)"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "Full Reg 30 announcement record, 2021 EGM notice, Investment Agreement 2021-05-27, Reg 29 and bulk-deal records Jun 2023 to Mar 2024"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "Q2 FY27 Corporate Governance Report"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "Screener Profit and Loss, Quarters, Balance Sheet, Cash Flow exports (Onward and three peers)"
    expected_source: "company IR page"
    kind: "findable-missing"
  - document: "Arihant Capital March 2026 conference notes"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "Broker research notes"
    expected_source: "BSE"
    kind: "plausibly-nonexistent"
  - document: "Live credit rating (ICRA withdrew 2023-11-13)"
    expected_source: "rating agency site"
    kind: "plausibly-nonexistent"
archetypes:
  - line: "Engineering and digital services (single reporting segment)"
    archetype: "Outsourcing partner (CDMO/EMS/IT services)"
transition:
  - line: "Engineering and digital services"
    from_tier: "R2"
    to_tier: "R3"
    engine: "Offshore leverage and utilisation on a mostly fixed pay cost; wallet share through large multi-year programmes (Rs 33 Cr ODC, Rs 44.5 Cr renewal)"
    proof_gate: "EBITDA margin ex R&D credit at or above 14.0% in each of Q3 FY27 and Q4 FY27 with offshore share at or above 72%; supporting: employee cost ratio ex-credit under 71%, DSO under 75 days by Q3 FY27"
    recognition_gap: "Open question: does the R3 neighbourhood already look reflected in market pricing; Stage 11 resolves via the PE gap"
    ugliness: "ARTIFACT-OF-CLIMB"
    transition_falsifier: "Q3 FY27 EBITDA margin ex-credit at or below 13.0% with offshore share under 72%; top-5 share above 50% or single-customer share above 20%"
dominant_variables:
  - "Ex-credit EBITDA margin with offshore share and employee cost ratio"
  - "Revenue conversion of the hiring ramp and large programmes"
  - "Cash conversion: DSO and unbilled against revenue"
  - "Client concentration and wallet share"
business_falsifier: "The 18.3% customer lapsing or driving a majority of growth (captive-vendor re-declaration), or a third audit-trail carve-out or qualified opinion on the revenue billing system"
mental_model_status: "DRAFT - PENDING OPERATOR SIGN-OFF"
fragility:
  variable_count: 6
  verifiability_ratio: "4 of 6 externally observable"
  single_point_failure: "The 18.3% customer (retention and renewal)"
  fragility_verdict: "FRAGILE"
candidate_count: 7
second_order:
  chains_drafted: 2
  pending_live_links: 2
  confirm_by_observations: 2
research_brief_items: 15
plain_summary_points: 15
annex:
  present: true
  questions_answered: 10
  corpus_commit_hash: "93429c143b6f4094e66b8ae2226885930d7b8f2e"
```
