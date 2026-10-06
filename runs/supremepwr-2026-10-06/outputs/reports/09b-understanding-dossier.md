# HALT 1 UNDERSTANDING DOSSIER: Supreme Power Equipment Ltd (SUPREMEPWR)

Run date: 2026-10-06. Stage 09b. Model: Sonnet 5.5. Built from blocks B00 to B09, B12a to B12d and confidence.yaml. Units: Rs Cr unless a source says Rs lakh; AR statements and results are in Rs lakh on their face (B00).

This file is an understanding package. It states no price, no verdict and no recommendation. The Mental Model Declaration in Section 2 is a DRAFT.

Page anchors in this file follow the file's own [page N] markers. The printed page of a transcript is N-1 (B05 analyst note).

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

Inventory only. Every line comes from B00 unless another block is named.

1. CONCALLS. Held and read: Q3 FY26 call 11-Feb-2026; H2 FY26 call 02-Jun-2026; Q1 FY27 call 17-Aug-2026 (B00, B05). Held but preserved, never read by any stage: H2 FY25 (Jun-2025), Q1 FY26 (Aug-2025) and H1 FY26 (Nov-2025) transcripts in inputs/other/ (B00). Most recent quarter covered: Q1 FY27 (Apr to Jun 2026). Q2 FY27 has not reported as of the run date: B00 records no Q2 FY27 business update filed, and B03 places the Q2 FY27 results in Nov-2026. No more recent transcript is plausibly missing.
2. ANNUAL REPORTS. Read: AR FY2025-26 with the 21st AGM notice, filed with NSE 01-Sep-2026 (B00). Held but never read: AR FY2024-25 in inputs/other/ (B00). The latest completed FY is present. Fewer than three years are held: one read AR and one preserved AR. AR FY2023-24 is ABSENT. B02 and B03 name the unread FY25 AR as the reason Phase 6D tone drift is NOT FOUND.
3. RESULTS FILINGS. Latest: Q1 FY27 unaudited standalone and consolidated, board date 13-Aug-2026 (B00; Results_Q1FY27_30Jun2026 p.1). Also held: FY26 audited results, board date 27-May-2026 (B00). The Q1 FY27 filing sits one quarter after the AR year end; no results quarter is missing between them. Results filings for Q1 FY26, H1 FY26 and Q3 FY26 are not in the manifest (B00); their comparatives appear only inside later filings.
4. INVESTOR PRESENTATIONS. Latest: Q1 FY27, 17-Aug-2026. Also held: H2 FY26, 01-Jun-2026 (B00).
5. RESEARCH AND RATING. CRISIL full rating rationale 20-Mar-2026 and the CRISIL letter 20-Mar-2026 (B00). The research/ folder is empty: no broker note is held (B00).
6. CORPORATE ACTIONS. 17 filings from 20-Mar-2026 to 25-Sep-2026: nine order intimations 07-Apr to 13-Jul-2026; AGM proceedings 25-Sep-2026; change in management 13-Aug-2026 (XBRL only, the scanned letter has no text layer); Reg 32 statement for Q1 FY27; Q1 FY27 and H2 FY26 press releases; general update 24-Apr-2026; investor meet outcome 21-Sep-2026 (B00). Order intimations from Oct-2025 to Feb-2026 were not pulled under the operator cap (B00). The Aug-2025 warrant allotment filings are not held.
7. FRESHNESS PAIR CHECK. B00 freshness_verdict reads FRESHNESS PAIRS OK. All four pairs PASS: results to same-quarter concall (Q1 FY27 transcript held); rating bulletin to full rationale (held); SEBI order to order text (none referenced); AR to latest audited annual results (FY26 AR held) (B00). No pair failed.
8. Other documents held: shareholding pattern 31-Mar-2026, submitted 10-Apr-2026 (SME files half-yearly; the Sep-2026 pattern is not yet filed); screener Data_Sheet exports FY23 to FY26; peer transcripts for Shilchar (4 calls) and Danish Power (2 calls); screener Profit and Loss, Quarters, Balance Sheet and Cash Flow sheets came out EMPTY and are ABSENT (B00).

VERDICT LINE: **CORPUS GAPPED**

Findable but missing (operator upload list):
- Prospectus, Dec-2023 listing: HIGH gap. Source: NSE Emerge filing or lead manager page. Not pulled under the 12-document cap (B00). Backward baseline and promoter group map run without it (B00, B08).
- Order intimations Oct-2025 to Feb-2026. Source: NSE announcements (B00).
- Earlier shareholding patterns, all periods before 31-Mar-2026. Source: NSE. B08 records them as NOT FOUND.
- 20th AGM notice dated 26-Aug-2025 and AGM and EGM voting results. Source: NSE and company IR page. The fetch timed out twice (B08). Needed for the section 185 resolution date.
- Results filings for Q1 FY26, H1 FY26 and Q3 FY26. Source: NSE.
- AR FY2023-24. Source: company IR page or NSE.

Plausibly nonexistent (itself a data point on opacity):
- Danya Electric partnership deed, auditor and standalone accounts. B02 and B03 mark them NOT FOUND IN DOCUMENT. B08 notes partnership firms are not on MCA. Expected source: management only.
- Peer INDOTECH transcripts: none on screener (B00). Peer INDOTECH is UNUSED (B06).
- Broker research: the folder is empty and none is known to exist (B00).

No freshness gap.

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT - PENDING OPERATOR SIGN-OFF.** Not signed. Signing happens only in claude.ai after live-web stress-testing.

### PART A: THE FROM STATE

**A1. ARCHETYPE** (CLAUDE.md ARCHETYPE LIBRARY)

| Line | Archetype | Basis |
|---|---|---|
| Distribution and inverter duty transformers, up to about 25 MVA (Unit 1, Thirumazhisai) | Order-book business (EPC, defence, capital goods) | Orders won against tenders, delivered over 7 to 17 months, margin set on the backlog (B04, B05). Revenue split by product is NOT FOUND (B04). |
| Power transformers, above 25 MVA up to 200 MVA / 220 kV (Unit 2, Kannur) | Order-book business (EPC, defence, capital goods) | Same mechanics. Order book mix is about 72 to 77% power, 18 to 20% distribution, 5 to 8% inverter duty (B04, B05). |

The company reports one segment (B02, B03). The two lines share an archetype and differ in qualification and loading.

**A2. THE SIMPLE ANALOGY.** Think of a metal workshop that builds the big grey boxes you see inside an electricity substation. Each box takes high voltage power from a transmission line and steps it down, so homes and factories can use it. Customers order a box months ahead, the workshop builds it to a drawing, and the customer pays on delivery and installation. The workshop had one small floor that built boxes up to a medium size. It has just opened a second, much larger floor (Rs 95 to 100 Cr, B05) that can build the very large boxes. The floor is built and paid for, but only about a fifth to a quarter is busy (B05). The staff on it are mostly freshers in training (B05). The workshop also works hand in hand with a small partnership firm, Danya Electric, that it owns 90% of by profit share (B02).

### PART B: THE TRANSITION

**B1. FROM to TO** (CLAUDE.md QUALITY LADDER)

| Line | FROM | TO |
|---|---|---|
| Power transformers (Kannur) | R2 COST-ADVANTAGED CONVERTER side of R2/R3: tender-market supplier, pricing power weak (B04), ROCE fell from 28.1% to 20.1% FY24 to FY26 (B01), Emerging Moat NONE at 8.3 (B07) | R3 VALUE-ADDED / SPEC'D SUPPLIER: spec-in through a 220 kV type test and utility qualification (B05, B07) |
| Distribution and inverter duty (Unit 1) | R2. No transition is claimed for this line (B05) | No move claimed |

The claim is one rung on one line. That sits inside the one-rung-per-2-to-3-years base rate. The run did not find any claim of a multi-rung leap.

**B2. THE ENGINE.** Two things physically change.
1. Kannur load. Installed capacity rose from 2,500 MVA to about 9,000 MVA (B03). Use is 20% to 25% (B05). Fixed costs have arrived first: employee cost 0.81 to 1.92 and depreciation plus interest step-ups in Q1 FY27 (B03, B05). The engine works when MVA shipped rises against a fixed cost base.
2. The 220 kV credential. Type tests exist only up to 25 MVA / 110 kV (B03, B07). A 160 MVA / 220 kV prototype test at CPRI is planned for Dec-2026 or Jan-2027 (B05). A pass would let the above-25 MVA part of the Rs 590.06 Cr book (B05) and the 220 kV and data centre classes be built and approved.

**B3. THE PROOF GATE.** Binary, quarter by quarter. Every threshold below is already in B03 or B05; none is new.
- Gate 1, Q2 FY27 results (Nov-2026, B03). It fires only if all three hold: consolidated revenue at or above Rs 55 Cr (B03); Kannur utilisation stated with its basis at or above 30% (B05 confirm signal); depreciation plus interest take no more than 50% of the EBITDA gain (Q1 FY27 was 69.7%, B03).
- Gate 2, Q3 FY27. Kannur utilisation above 25%. Flat at or below 25% is the kill signal (B05).
- Gate 3, by 31-Mar-2027. CPRI certificate for 160 MVA / 220 kV filed (B05, B07).
Until Gate 1 fires, the transition is narrative and the name is research, not a trade. FTTCP tests these thresholds.

**B4. THE RECOGNITION GAP (to be resolved at Stage 11).** Open question: does the market's current pricing already reflect the TO state, a power transformer maker with a loaded Kannur plant and a 220 kV credential? The blocks do not carry a market pricing read, so this file does not answer it. Stage 11 resolves it through the PE gap. If the TO state is already reflected, the re-rating engine is spent and only earnings growth remains. This file states no number and no conclusion.

**B5. THE UGLINESS TEST.** Classification: **ARTIFACT-OF-CLIMB**, provisional, with a stated structural carve-out.
- Why artifact. Q1 FY27 revenue rose 37.5% (48.23 vs 35.07) while profit for the period rose 9.6% (B01). Depreciation plus interest took 69.7% of the EBITDA gain (B03). Employee cost rose 0.81 to 1.92 (B01). Capex 57.48 against CFO 25.90 and FCF of -31.58 in FY26 sit on the Kannur build peak (B01). These are timing features of a plant that is paid for before it is loaded.
- Two readings. Reading A: the cost step-up is temporary and loading will absorb it. Reading B: the load does not arrive, and the optic is permanent. The one observation that separates them is the Q2 FY27 depreciation-plus-interest share of EBITDA gain and the Kannur MVA shipped (B03, B05). B07 adds that a revenue-basis Kannur reading is near 10% if Unit 1 was flat, against the stated 20% to 25%.
- Structural carve-out. The Danya loop (61.3% of its turnover goes to SPEL, B02), the supplier-funded working capital (payables 62.20 equal inventory 62.10, B01) and weak pricing power (B04) are not artifacts of the climb. The climb does not explain them. They carry as tripwires, not as part of this classification.

**B6. THE TRANSITION FALSIFIER.** Any one of these kills the arrow (B05, B07):
- Q2 FY27 revenue below Rs 55 Cr (B03), or Kannur utilisation flat at or below 25% at Q3 FY27 (B05).
- The 160 MVA / 220 kV test slips beyond Mar-2027 or fails (B05, B07).
- The depreciation-plus-interest share of EBITDA gain stays above 70% for a second quarter (B04).
- A peer's first 220 kV order clears at full margin, which would remove the entry-pricing reading, or three or more peers qualify in the same window and make the niche common (B06 cross-peer hypothesis, B09).

### PART C: WHAT THE MODEL WATCHES

**C1. DOMINANT VARIABLES** (these become the Role 5.5 tracker signals)
1. Kannur load: MVA produced and delivered per quarter, with the utilisation basis. Now: 20% to 25% stated, four utilisation readings that do not reconcile (B04, B05).
2. 220 kV qualification: CPRI certificate for 160 MVA / 220 kV, and the first 220 kV order margin. Now: type tests only to 25 MVA / 110 kV; test planned Dec-2026 or Jan-2027 (B05, B07).
3. Fixed-cost absorption: depreciation plus interest share of EBITDA gain, and gross margin. Now: 69.7% share in Q1 FY27 (B03); gross margin 23.80% to 28.82% with the inventory-gain question unanswered (B12b).
4. Funding of the climb: CFO against capex, standalone advances and payables, DSCR, warrant receipts. Now: CFO 25.90 vs capex 57.48 (B01); payables 62.20 vs inventory 62.10 (B01); DSCR 2.44x (B02); warrant balance Rs 15.81 Cr due by 27-Feb-2027 (B03, B07).

**C2. WHAT THE MODEL REJECTS** (declared noise)
- Market size. B09 puts revenue headroom at 29.6x and the capacity, not the market, as the limit (B09). The binding constraint is execution. The Rs 9.15 lakh Cr transmission headline is an investment programme, not a transformer market (B09).
- Spot ROCE and spot ROE during a build year: Kannur capital sits in the base before it earns (B04).
- Debt to equity 0.42x and current ratio 1.28x: advances and payables inflate both (B04).
- Reported utilisation percent: use MVA delivered (B04).
- Quarterly year-on-year revenue growth: delivery timing makes it lumpy (B04).
- Consolidated EBITDA margin 18.1% against standalone 15.1%: a denominator effect from the Rs 50.18 Cr elimination (B04).

**C3. THE BUSINESS FALSIFIER.** This kills the starting business, not the arrow. Evidence that would force a re-declaration of the FROM business itself: a Danya partnership deed or a third-party price benchmark showing that SPEL's reported revenue and profit rest on pass-through trade with a firm that two promoter-directors co-own (B02, B08), so SPEL is closer to a tender-channel partner than an independent maker. Or a Danya default that crystallises the Rs 14.70 Cr guarantee (B08). Or a named-customer disclosure that shows the Hyderabad-based Q1 FY27 inflow, 65.4% (B07), comes from one group with no repeat order (B05). Any one of these changes what the starting business is.

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE (DRAFT)

SUPREMEPWR builds power and distribution transformers at two plants in Tamil Nadu, Thirumazhisai and Kannur (B03, B04). A transformer steps grid voltage up or down, so no substation, wind farm or solar plant can run without one (B04). Transformers are 99.6% of revenue and repair and testing services are 0.4% (B04). The order book of Rs 590.06 Cr is about 72 to 77% power transformers, 18 to 20% distribution and 5 to 8% inverter duty units (B03, B05). The run did not establish the FY26 revenue split by product (B04). Customers come in five classes: state utilities, EPC contractors, renewable developers, industrial users and public sector units (B03). Government exposure is 30.10% of the order book (B05). Hyderabad-based customers placed Rs 128.00 Cr of the Rs 195.64 Cr Q1 FY27 inflow, 65.4%, and no filing names them (B07). State vendor approvals with TANGEDCO, KSEB, KPTCL and TNPDCL are an entry ticket into tenders, not a lock on price (B04, B07). Demand exists because India adds substation capacity every year, 113,013 MVA in FY26 by the CEA monthly transformation capacity candidate, and because state distribution utilities replace old units through TNPDCL tenders and RDSS (B09). The run sizes the market at Rs 31,200 to 36,465 Cr and puts SPEL at 3.4% of its serviceable slice (B09). Market growth runs near 8.2% a year, with the 220 kV class, data centres and inverter duty units as extra drivers (B09, B05). The 220 kV and data centre drivers depend on a CPRI type test not yet taken, and the company has no data centre order (B05, B07). Peers confirm firm demand, but Shilchar, Danish Power, Voltamp and TARIL are adding 220 kV class capacity in the same window, so the claim that few players exist is not supported (B06, B09). The power transformer line has new capacity and no proven moat: the Emerging Moat scan scores 8.3 and the band is NONE (B07). The distribution and inverter duty line has no moat, and pricing power is weak across the company (B04). State empanelments score Moderate as an access ticket in a tender market (B07). Danya Electric is a working execution arm, not a credited moat (B07).

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. VERTICALS FRAMED

**Vertical 1: Kannur load** (dominant variable 1)
- Corpus establishes: installed capacity about 9,000 MVA against 2,500 MVA before (B03). FY26 output 1,750 MVA equals Unit 1 at about 70% of 2,500 MVA, so FY26 is a Unit 1 result (B04). Four utilisation readings do not agree: AR 45 to 50%, 19.4% derived, presentation 70 to 80% for Unit 1, CMD 20% to 25% for Kannur (B04). Q1 FY27 revenue rose only Rs 13.16 Cr (B07). The FY27 revenue guide fell from more than 300 to 275-300 to 250-300 (B05). Two readings of FY27 exist: a capacity-derived Rs 225 to 275 Cr (B05) and a demonstrated-output Rs 282 to 327 Cr (B12b). Q2 FY27 revenue separates them.
- Cannot establish: Kannur MVA by plant, the utilisation basis, how many 20 MVA-class orders load on Kannur against Unit 1. Eight of ten Q1 FY27 orders are 20 MVA units that Unit 1 can build (B05).
- Deciding questions: (1) What MVA did Kannur produce and deliver in Q2 FY27, and on what basis? (2) Does Q2 FY27 revenue reach Rs 55 Cr or more (B03)? (3) Which plant carries the 20 MVA orders, and does any above-25 MVA order ship before the type test?

**Vertical 2: 220 kV qualification** (dominant variable 2)
- Corpus establishes: type tests cover only up to 25 MVA / 110 kV (B03, B07). The planned 160 MVA / 220 kV test is about 8 to 9 months after the order, against the CMD's own norm of 1.5 to 2 years (B07). Prototype cost is Rs 14 to 16 Cr (B05). Two 112.5 MVA / 330 kV orders sit above the 220 kV class (B07). Peers enter 220 kV in the same window (B06, B09). Only 18.8% of Q1 FY27 wins are above 25 MVA (B05).
- Cannot establish: the number of qualified 220 kV makers (NOT FOUND, B07); EHV market share (B09); whether any CPRI slot or date is confirmed.
- Deciding questions: (1) Is the CPRI certificate filed by 31-Mar-2027? (2) At what margin does the first 220 kV order price (B06 hypothesis)? (3) Does the 330 kV order ship, and with what test equipment (Rs 7.77 Cr still in CWIP, B07)?

**Vertical 3: Fixed-cost absorption** (dominant variable 3)
- Corpus establishes: Q1 FY27 revenue +37.5% against profit +9.6% (B01). Depreciation plus interest took 69.7% of the EBITDA gain (B03). Depreciation run-rate is about 1.24 Cr a quarter against Q1 0.80 (B12a, B03). Gross margin rose from 23.80% to 28.82%, and management did not answer whether an inventory gain from a March advance purchase of oil and copper is inside it (B12b). The company says 80 to 85% of the book has price variation clauses; Danish says about 30% (B06). CRISIL sees an industry margin of 8 to 10% against SPEL's 18 to 20% guide (B09).
- Cannot establish: gross margin by product, the filed order terms behind the price variation claim (B06), margin on above-25 MVA orders.
- Deciding questions: (1) What is Q2 FY27 gross margin? Reading A: price variation run-rate. Reading B: one-time advance-purchase gain (B12b). (2) Does the depreciation-plus-interest share fall to 50% or below (B03)? (3) What is the gross margin on above-25 MVA orders?

**Vertical 4: Funding of the climb** (dominant variable 4)
- Corpus establishes: FY26 CFO 25.90 against capex 57.48 (B01). Payables plus customer advances added about 78.7% of consolidated capex (B03). Payables 62.20 now equal inventory 62.10 (B01). Borrowings rose 18.75 to 49.97 (B01). DSCR is 2.44x against 10.47x in FY25 (B02). There are no undrawn facilities and ICICI is 97.2% of term debt (B02). A warrant balance of Rs 15.81 Cr falls due by 27-Feb-2027, 63.9% from non-promoters (B02, B03). The SPEL guarantee for Danya is Rs 14.70 Cr and FY27 authority sought is higher (B02, B08).
- Cannot establish: capex creditors inside payables (NOT FOUND, B02); ICICI covenants and rate type (NOT FOUND, B02); the Danya deed (B03).
- Deciding questions: (1) Do standalone advances stay near 17.10 and payables near 59.54 at H1 FY27 (B03)? (2) Is the Rs 15.81 Cr warrant balance received by 27-Feb-2027 (B03)? (3) Does Danya gross trade with SPEL stay at or below Rs 50.2 Cr a year and the guarantee at Rs 14.70 Cr (B03)?

### 4b. CANDIDATE SIGNAL TABLE (UNVERIFIED; verification and tracker writes happen at Role 5.5 in claude.ai)

Candidates come from B09 downstream_candidates. Likely sources are as B09 states them. Registry match against Downstream_Source_Discovery_Protocol_v1_0 is a Role 5.5 task.

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| CEA monthly transformation capacity added (MVA) and the FY27 CEA plan figure of 158,339 MVA (B09) | Monthly additions fall below the FY26 pace of 113,013 MVA a year (B09) for two straight quarters | Monthly | CEA transmission monthly progress reports; Ministry of Power (B09) |
| TNPDCL / TNEB distribution transformer replacement tenders, 40,000 units, Rs 2,000 Cr plan (B09) | Tender cancelled or deferred, or no SPEL or Danya award across two tender cycles | Event-Driven | Tamil Nadu e-procurement portal and TNPDCL notices (B09) |
| KPTCL and KSEB substation transformer tenders and awards (B09) | Awards go to peers with no SPEL award for two quarters while SPEL's 20 MVA class orders stop | Event-Driven | KPTCL and KSEB tender portals; state utility capex plans (B09) |
| CPRI 220 kV / 160 MVA type-test certificate (B09) | Not filed by 31-Mar-2027, or test fails (B05) | Event-Driven | CPRI certificate; company Reg 30 filing (B09) |
| RDSS sanction and progress after extension to 31-Mar-2028 (B09) | Sanctioned outlay or distribution transformer progress stalls on the dashboard | Quarterly | Ministry of Power RDSS dashboard; parliamentary replies (B09) |
| Peer order books and capacity: Voltamp, Shilchar, Danish, TARIL (B09) | Peer inflow below peer revenue for two quarters, or a peer first 220 kV order clears at full margin (B06) | Quarterly | Peer investor presentations and Reg 30 intimations (B09) |
| Hyderabad-based unnamed customers, Rs 128.0 Cr of the ten Q1 FY27 orders (B09) | Hyderabad share stays above 60% of inflow with no repeat order (B05 kill signal) | Event-Driven | Company Reg 30 order intimations; Telangana DISCOM and CTUIL filings (B09) |

### 4c. FRAGILITY READ

External variables that must go right for the bull case, seven:
1. Kannur MVA loading rises as stated. Company-narrated (basis undisclosed, B04, B05).
2. CPRI 220 kV type test passes by 31-Mar-2027. Externally observable (certificate, Reg 30; B05, B07).
3. Order-book conversion on schedule, with customer extensions held below 10 to 20% (B05). Company-narrated.
4. Price pass-through holds on 80 to 85% of the book. Company-narrated; Danish says about 30% (B06).
5. Funding float holds and the warrant balance arrives. Externally observable (exchange allotment filings, balance sheet; B03).
6. The Danya loop stays inside current bounds. Externally observable in part (RPT filings, guarantee amount); the deed is not (B08).
7. Utility and project demand and the peer 220 kV race stay benign. Externally observable (CEA, tenders, peer filings; B09, B06).

- variable_count: 7
- verifiability_ratio: 4 of 7 externally observable (items 2, 5, 6, 7)
- single_point_failure: the 160 MVA / 220 kV CPRI type test. B07 states that a fail or a slip past Mar-2027 strands the Kannur premise. B05 shows eight of ten Q1 FY27 orders are 20 MVA units that Unit 1 can build, so the damage falls on the Kannur loading, not on the whole company.
- fragility_verdict: **FRAGILE**. Reason: one kill-switch, and the two variables that decide the engine (Kannur loading and price pass-through) are company-narrated.

### 4d. RESEARCH BRIEF (the claude.ai work order)

1. PENDING LIVE VERIFICATION (Chain 1): identify the Hyderabad-based customers behind the Rs 128.00 Cr of Q1 FY27 inflow (B07). Open the order intimations dated 22-Apr-2026 and 13-Jul-2026 on the NSE announcement page for SUPREMEPWR, then Telangana DISCOM and CTUIL award records, then MCA21 master data for any named counterparty.
2. PENDING LIVE VERIFICATION (Chain 2): open the rating rationale for Danya Electric Company (BB-/A4+, B02, B08; the agency is not named in the blocks) and the ICICI Bank sanction terms. Confirm rate type, covenants, repayment schedule and the guarantee linkage.
3. Chain 3 to build: the 220 kV entrant cluster. Voltamp +6,000 MVA EHV (Oct-2026), Shilchar +6,500 MVA (Apr-2027), Danish +12,000 to 15,000 MVA, TARIL +15,000 MVA (B09). Test the first 220 kV order margin at peers (B06 cross-peer hypothesis). Source: peer Reg 30 filings and calls.
4. Chain 4 to build: input cost and price variation. Oil about +100%, other inputs +10 to 25% since Feb-2026 (B06). Test the 80 to 85% price variation claim against filed order terms (B06 price variation outlier note, handed to Verifier A).
5. Chain 5 to build: utility counterparty health. Read TNPDCL, KSEB, KPTCL and TANGEDCO audited accounts and payment-cycle disclosures. B06 notes Danish raises government discom payment delays.
6. Identify the unnamed Navratna public sector unit behind the Rs 60.90 Cr inverter duty order (B03). Customer-health read from its own filings.
7. Policy status: RDSS extension to 31-Mar-2028 and sanctioned outlay; the NEP transmission programme status (B09).
8. Verify the NEP 2032 GVA endpoint. B12a records that 2,342 appears in B09 both as the NEP 2032 GVA and as the Voltamp order book. Verify it before the 8.2% growth rate is used.
9. Source URL verification for B09 web inputs: CRISIL 12-Aug-2025 market size, Mordor 05-Aug-2026, RBI reference rate about 96, CEA FY26 MVA, undated tndindia and enggpro pages (B09 stale-data list).
10. Section 185 trail on the Danya guarantee: 20th AGM notice 26-Aug-2025, EGM 14-Jul-2025 and 21st AGM voting results (B08 skipped searches).
11. Danya deed, auditor, capital ratio and standalone accounts. Not in the corpus; ask management (B02, B03).
12. Prospectus Dec-2023: litigation and group-company chapters (B08 notes an IPO page risk line on legal proceedings, nature NOT FOUND).
13. Skipped regulatory searches from B08: eCourts and NCLT party search, SEBI and SAT direct query, NSE surveillance status, promoter Reg 7 trades, dividend history.
14. QMax Test Equipments listing status and the independence analysis for the Audit chair who guarantees an ICICI tranche (B03, B08).
15. Main board migration eligibility window after Dec-2026 (B05).
16. Q2 FY27 print check list for the operator calendar, Nov-2026: revenue, Kannur MVA with basis, gross margin, depreciation, advances and payables (B03, B05, B12b).

### 4e. SECOND-ORDER STUB (Master Prompt v3.7, Rule F)

Tier labels: DOCUMENTED = filed or printed in the corpus; DERIVED = arithmetic on documented figures; CLAIM = management statement; INFERENCE = forward reasoning from the links above it.

```
CHAIN 1: Hyderabad-based customers placed Rs 128.00 Cr of the Rs 195.64 Cr Q1 FY27 inflow, 65.4%, and no filing names them (B07 inflow concentration note).
Link 1 [DOCUMENTED]: Eight of the ten Q1 FY27 orders are 20 MVA power transformers, and only two orders (112.5 MVA and 160 MVA, Rs 13.50 Cr and Rs 23.30 Cr) are above 25 MVA (B05 qualification gap note). Unit 1 is rated up to 25 MVA (B05).
Link 2 [PENDING LIVE VERIFICATION]: who pays, and why now. The corpus cannot name the Hyderabad counterparties or say why they ordered in Q1. Claude web should open the NSE order intimations of 22-Apr-2026 and 13-Jul-2026 and the Telangana DISCOM or CTUIL award records, then MCA21 for any named party. No counterparty fact is asserted here.
Link 3 [INFERENCE]: If most of the Hyderabad inflow is 20 MVA units, it can be built on Unit 1, so it does not itself load Kannur (B05). Kannur loading in FY27 then rests on the thin above-25 MVA flow (18.8%, DERIVED in B05) and on cross-loading. The absorption of the new fixed cost (employee 1.92 against 0.81, B01) would depend on cross-loading and on the 220 kV test, not on order volume.
Binding constraint: working capital and the delivery calendar. Payables 62.20 equal inventory 62.10 and borrowings are 49.98 (B01). There are no undrawn lines (B02). Rs 140.14 Cr (71.6%) of Q1 FY27 wins fall due after Mar-2027 and only Rs 55.50 Cr (28.4%) by Mar-2027 (B07 DERIVED), so the Rs 377 Cr due before March (B05) leans on older orders. The Rs 39.90 Cr order has a 13 to 17 month execution window (InvestorPresentation_Q1FY27_17Aug2026, file p.5).
Unsaid: AGM Items 7 and 8 seek borrowing and security limits of Rs 500 Cr each, about 10x gross debt, with no project named (B03, B08). Management named no capex after Kannur on any call (B03 NOT FOUND; B05 land not bought). The limit implies a funding need nobody described. Capital commitments read Nil against CWIP 2,797.98 lakh (B02 finding 10).
Observation that confirms or breaks this chain, and confirm-by date: Q2 FY27 results, due by 30-Nov-2026 (B03 window Nov-2026). Confirms: consolidated revenue at or above Rs 55 Cr, Kannur MVA produced stated with its basis at or above 30%, and depreciation plus interest at or below 50% of the EBITDA gain (B03, B05). Breaks: Kannur MVA not disclosed, or utilisation still at 20% to 25%, with revenue under Rs 55 Cr.
```

```
CHAIN 2: FY26 CFO was Rs 25.90 Cr against capex Rs 57.48 Cr, and payables plus customer advances added about 78.7% of consolidated capex (B01, B03).
Link 1 [DOCUMENTED]: Standalone customer advances rose to 17.10 and payables to 59.54, and payable days are 126.3 against inventory days of 124.8 (B03, B01). Borrowings rose 18.75 to 49.97 (B01). DSCR is 2.44x against 10.47x in FY25 on the company's definition of interest plus year-end current maturities (B02).
Link 2 [PENDING LIVE VERIFICATION]: who pays, and why now. The corpus cannot say whether suppliers or customers extended terms by choice or by the shape of this build year, nor what ICICI's covenants allow. Claude web should open the rating rationale for Danya Electric Company (BB-/A4+) and the ICICI Bank sanction terms, and check supplier terms from named suppliers' filings. No counterparty fact is asserted here.
Link 3 [INFERENCE]: SPEL owes Danya Rs 6.63 Cr in payables (662.82 lakh, B02), guarantees Danya's bank debt at Rs 14.70 Cr (B08), and lends to Danya at 8.00 to 9.00% on demand while its own ICICI debt costs 9.50% (B08). If SPEL tightens payments to Danya to conserve cash, Danya's liquidity tightens and the guarantee becomes the backstop. The float and the Danya loop are one liquidity system, so a reversal in one loads the other.
Binding constraint: no undrawn facilities (B02 Note 25(2)), current maturities of 1,095.48 lakh (B02), and a warrant balance of Rs 15.81 Cr due by 27-Feb-2027 with 63.9% from non-promoters (B03, B02). The ICICI table does not reconcile: current principal 1,005.19 lakh exceeds 12 months of EMI cash 713.28 lakh (B02 finding 4).
Unsaid: The calls never name Danya's rating, trade with SPEL or the guarantee, and no analyst asked (B05 Danya note). FY27 authority sought for Danya is Rs 125 Cr of related party trade against FY26 gross trade of Rs 50.18 Cr (B08). Capex creditors inside payables are NOT FOUND (B02), so the true cash conversion is not measurable from the Notes.
Observation that confirms or breaks this chain, and confirm-by date: H1 FY27 balance sheet, due by 30-Nov-2026 (B03). Confirms: standalone advances near 17.10 and payables near 59.54, Danya gross trade at or below Rs 25.1 Cr per half and the guarantee at Rs 14.70 Cr (B03). Breaks: advances under about 10 with payables above 59 (B03 reversal signal), or the guarantee moving toward Rs 25 Cr. Second observation: Rs 15.81 Cr warrant balance received by 27-Feb-2027 (B03).
```

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in claude.ai with live web, before Role 2.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. SUPREMEPWR builds transformers. These are the large boxes in substations that step electricity voltage up or down (B04).
2. It has two plants. Unit 1 near Chennai builds units up to about 25 MVA. Unit 2 in Kannur can build up to 200 MVA at 220 kV, and it started commercial production in Feb-2026 (B03, B05).
3. Almost all revenue is transformer sales. Repair and testing services are 0.4% (B04).
4. Customers are state utilities, EPC contractors, renewable developers, industrial users and public sector units. Government exposure is 30.10% of the order book (B03, B05).
5. Hyderabad-based customers placed 65.4% of Q1 FY27 inflow, and no filing names them (B07).
6. Demand is firm today. India added 113,013 MVA of substation capacity in FY26, and the run sizes the market at Rs 31,200 to 36,465 Cr (B09).
7. Demand should keep growing at about 8.2% a year (B09). Peers describe the same firm demand but say it is a 3 to 7 year cycle, not 10 years (B06).
8. The big extra growth idea is 220 kV and data centre transformers. It depends on a type test not yet taken, and there is no data centre order (B05, B07).
9. The moat is thin. State vendor approvals are an entry ticket. The Emerging Moat scan scores 8.3, band NONE, and pricing power is weak (B04, B07).
10. Peers are building 220 kV capacity in the same window, so the claim that few players exist is not supported (B06, B09).
11. Mental model in one point: a tender-market order-book maker climbing one rung, from R2 toward R3, by loading a new plant and earning a 220 kV credential. Draft, not signed (Section 2).
12. Fragility verdict: FRAGILE. Seven things must go right, four can be observed from outside, and the single kill-switch is the CPRI type test (4c).
13. The corpus could not establish: the product revenue split, Kannur MVA by plant, the Danya deed, ICICI covenants and the prospectus (B04, B02, B00). Verifier results show 97.5% number acceptance and 76% coverage of independently found concerns, so overall confidence is 76 (confidence.yaml).
14. Biggest open question 1: is Kannur really loading? Four utilisation readings disagree, and Q2 FY27 revenue and MVA decide it (B04, B05).
15. Biggest open question 2: can cash and the Danya loop carry the build? Payables equal inventory, there are no undrawn lines, and a warrant balance of Rs 15.81 Cr is due by Feb-2027 (B01, B02, B03).

---

## SECTION 6: STANDING EXTRACTION ANNEX

Page anchors are the file's own [page N] markers in the page-marked .txt beside each PDF. Quote-then-comment form. Corpus commit hash is the last line.

### 1. UNITS

- Printed: "9,000MVA Production Capacity", "1,750 MVA Actual Production", "45 to 50 % Capacity Utilization" (Annual_Report_FY2025-26, file p.4). Comment: one basket, all nine transformer classes. The utilisation basis is not printed. The 1,750 MVA is plant production; the plant it comes from is not named.
- Printed: "Revenues 113.46 148.72 181.64" for FY24, FY25, FY26 consolidated, Rs Cr (InvestorPresentation_Q1FY27_17Aug2026, file p.37).
- No per-unit realisation is printed anywhere in the corpus. Derivation inputs: standalone FY26 revenue Rs 190.08 Cr (Results_Q1FY27_30Jun2026 p.5 and p.8, in lakh) and 1,750 MVA. B04 derives about Rs 10.9 lakh per MVA. The AR peak Rs 550 Cr on 9,000 MVA gives Rs 6.1 lakh per MVA (B04). The two do not agree, so capacity multiples will not map to revenue multiples.
- Printed order units: "₹23.30 Cr Company from Hyderabad 160 MVA, 220 kV Transformer 13 Months" (InvestorPresentation_Q1FY27_17Aug2026, file p.5). Value is printed per order, not per MVA.
- Cumulative units: "Energy efficient transformers 9,750+", "Power transformers 450+" (Annual_Report_FY2025-26, file p.18). A count, not a price.

### 2. SEGMENT CAPITAL AND DEBT

- Printed: "The Company operates in a single reportable business segment - the manufacture and supply of transformers and related equipment" (Annual_Report_FY2025-26, file p.18). Standalone Note 32: "The Company operates in a single business segment." (file p.76).
- Segment assets, segment liabilities, capital employed and borrowings by segment: NOT DISCLOSED, because there is one segment. Borrowings are not allocated.
- Total borrowings as filed (Rs lakh, B02 top finding 3; consolidated balance sheet Annual_Report_FY2025-26 p.81 per B12a): standalone 1,633.84 to 4,572.70; consolidated 1,874.56 to 4,997.30. Results_FY26_Audited_31Mar2026 prints consolidated Long-Term Borrowings "3,311.60" against "909.25" and Short-Term Borrowings "1,685.70" against "965.31" (OCR-quality text layer; read the page before reuse).
- Comment: ICICI is 97.2% of term debt, standalone 3,974.89 lakh (B02). Capital employed is not printed; B01 computes it as total assets less current liabilities.

### 3. GUIDANCE VERSUS ASPIRATION

| # | Quoted as printed | Source and anchor | Class |
|---|---|---|---|
| 1 | "Outlook, we are expecting more than INR300 crores next year." | Concall_Feb_2026_Transcript p.6 | (a) FY27 |
| 2 | "[...] to achieve between INR275 crores to INR300 crores." | Concall_Jun_2026_Transcript p.5 | (a) FY27 |
| 3 | "Yes, maximum, we can go up to INR250 crores to INR300 crores." | Concall_Aug_2026_Transcript p.6 | (a) FY27 |
| 4 | "It may cross INR300 crores also." | Concall_Aug_2026_Transcript p.16 | (b) no period beyond FY27 |
| 5 | "management guided to consolidated revenue of Rs.275-300 Crore for FY2026-27, with a further step-up expected in FY2027-28, and to EBITDA margins being maintained in the range of 15-18%" | Annual_Report_FY2025-26 p.19 | (a) FY27 revenue and margin; FY28 step-up unquantified |
| 6 | "we are planning up to INR50 crores to INR60 crores in this first quarter" | Concall_Jun_2026_Transcript p.11 | (a) Q1 FY27. Actual revenue 4,823.20 lakh (Results_Q1FY27 p.8) |
| 7 | "Year-on-year, 30% -- minimum 30% rise will be there on the revenue." | Concall_Aug_2026_Transcript p.8 | (a) FY28 |
| 8 | "It will be INR600 crores to INR650 crores." and "FY29. We believe..." | Concall_Aug_2026_Transcript p.8 | (a) FY29 peak, stated as belief |
| 9 | "The total revenue may come to INR600 crores, INR550 crores to INR600 crores in FY29." | Concall_Aug_2026_Transcript p.9 | (a) FY29; conflicts with row 8 |
| 10 | "PAT margin will be around, we believe it will be around 9% to 12%." | Concall_Aug_2026_Transcript p.14 | (a) FY27 |
| 11 | "peak revenue potential from the combined installed base is of the order of Rs.550 Crore" | Annual_Report_FY2025-26 p.18 | (b) no period |
| 12 | "expected to reach optimal utilisation of approximately 90% over a two to three year period" | Annual_Report_FY2025-26 p.18 | (a) 2 to 3 years |
| 13 | "Will be between 30% to 50%." (utilisation, Q4 FY27) | Concall_Aug_2026_Transcript p.6 | (a) Q4 FY27 |
| 14 | "we are planning to do this test end of this year, that is on December, which on January, we will do the test." | Concall_Jun_2026_Transcript p.12 | (a) Dec-2026 or Jan-2027 |
| 15 | "approximately 9,000 MVA per annum" installed capacity | Annual_Report_FY2025-26 p.18 | (c) capacity |

Comment: no row carries a stated basis for the margin guide. B05 shows the FY27 revenue guide fell from more than 300 to 275-300 to 250-300, and the FY26 guide cascade 225 to 200 to 190 against 181.64 actual (B05).

### 4. CONCENTRATION

- Product (order book): "approximately 72% power transformers, 20% distribution transformers and 7-8% inverter duty transformers" (Annual_Report_FY2025-26 p.18). Revenue by product: NOT DISCLOSED in machine-readable form; the FY26 mix slide has ten percentages and no label order (B04).
- Customer: the presentation slide "Top Ten Customers Contribution" prints 34.93%, 26.35%, 31.73% and others 65.07%, 73.65%, 68.27% for FY24 to FY26 (InvestorPresentation_Q1FY27_17Aug2026, file p.37). The text layer does not fix which value belongs to which year, so the FY26 top-ten share and any single top-customer share are NOT DISCLOSED in readable form. No single-customer percentage is printed.
- Government share: 30.10% of the order book on 13-Aug-2026 (B05).
- Q1 FY27 inflow: four of ten orders are labelled "from Hyderabad" (InvestorPresentation_Q1FY27_17Aug2026, file p.5), Rs 128.00 Cr of Rs 195.64 Cr, 65.4% (B07 DERIVED).
- Geography: "Geographic concentration primarily in South India" (InvestorPresentation_Q1FY27_17Aug2026, line 1225 of the .txt). Comment: concentration is real in geography and in one city's inflow; the customer identity is never named in filings.

### 5. PROMISE LEDGER

| Promise | Made | Status | Evidence anchor |
|---|---|---|---|
| Q4 FY26 revenue Rs 70-80 Cr | Q3 FY26 call 11-Feb-2026 | DELIVERED at floor (70.72, DERIVED) | B05; Concall_Feb_2026 p.6 |
| PAT margin 10-12% | 11-Feb-2026 | DELIVERED (FY26 11.4%) | B05 |
| New plant first invoice in Q4 FY26 | 11-Feb-2026 | DELIVERED one quarter late | B05; InvestorPresentation_H2FY26 |
| Government exposure below 50% | 11-Feb-2026 | DELIVERED (30.10%); B12b calls this a padded row | B05, B12b |
| FY26 revenue 180-200 Cr | 11-Feb-2026 | PARTIAL (181.64 at the floor) | B05 |
| Receivables cut to 80-90 days | 11-Feb-2026 | PARTIAL (94 days, then 80-100) | B05 |
| No equity dilution planned | 11-Feb-2026 | PARTIAL (FY28 may require) | B05 |
| Kannur output in 3-4 months with 150-200 staff | 02-Jun-2026 | PARTIAL (20-25% at about 6 months); B12b calls it premature | B05, B12b |
| New plant adds Rs 30-40 Cr in Q4 FY26 | 11-Feb-2026 | MISSED (Rs 20-25 Cr for the year) | B05; Concall_Jun_2026 |
| Q1 FY27 revenue Rs 50-60 Cr | 02-Jun-2026 | MISSED (48.23) | Concall_Jun_2026 p.11; Results_Q1FY27 p.8 |
| Identify land for next expansion within a quarter | 11-Feb-2026 | MISSED (no land purchased by 17-Aug-2026); B12b calls it hedged intent | B05, B12b |

Comment: B05 tallies 4 delivered, 4 partial, 3 missed, grade C. B12b removes one padded and one premature row and tallies 3 delivered, 3 partial, 3 missed, grade unchanged, and notes one untabled positive: order book from Rs 311 Cr to Rs 588.17 Cr.

### 6. RESTATED BASES

- Printed: "The figures of the previous period have been re-grouped / reclassified / restated, wherever necessary, to make them comparable with those of the current period" (Results_Q1FY27_30Jun2026, file p.5 note 5).
- Printed: "Previous year's figures have been regrouped / reclassified wherever necessary to correspond with current year's classification." (Annual_Report_FY2025-26, standalone Note 33, file p.76). FY26 audited results note 7 says the same (Results_FY26_Audited_31Mar2026, file p.8).
- Comparative as printed in the latest filing: Revenue from Operations, consolidated, quarter ended 30-Jun-2025: "3,506.69"; FY26 "18,164.04"; FY25 "1487170" (OCR text, reads 14,871.70) (Results_Q1FY27_30Jun2026, file p.8, Rs lakh).
- Comment: no quantified restatement and no reorganisation or transfer is named (B02). B02 records the Danya payable swinging between MSME and Others classes across FY25 and FY26 without explanation, and consolidated Note 30.6 reprinting standalone balances.

### 7. CORPORATE-ACTION CLAUSES

- The only corporate action in the corpus is the preferential issue of convertible warrants. No scheme, demerger, merger or share repurchase is in the corpus. If any exists, the filing to fetch is the NSE corporate actions list for SUPREMEPWR (not held).
- Printed: "the Company allotted 12,47,000 Convertible Warrants on a preferential basis at an issue price of RS 169/- per Warrant, each convertible into one Equity Share of RS 10/- each within 18 months from the date of allotment. NSE Limited granted its in-principle approval on August 13, 2025, and the Board allotted the Warrants on August 27, 2025." (Annual_Report_FY2025-26, Board's Report, file p.39).
- Printed: "approved in the Extra-Ordinary General Meeting held on July 14, 2025" and "subscription price of Rs.42.25 (25% of the issue price) and a warrant exercise price of Rs.126.75 (75% of the issue price)" (Annual_Report_FY2025-26, Note 5, file p.64 to p.65). Ratio: one equity share per warrant.
- Printed: "the Company has received Rs.5,26,85,750/- representing the subscription amount" (Annual_Report_FY2025-26, Note 5, and Board's Report file p.39).
- Comment: the balance of Rs 15.81 Cr falls due by about 27-Feb-2027 (B03). 449,500 warrants sit with the promoter group in the shareholding pattern (SHP_31Mar2026, file p.1). The definition of any undertaking and liability allocation clauses: NOT DISCLOSED, because no scheme exists in the corpus. Related Danya guarantee clause: "corporate guarantee of Rs.14.70 crores in favour of IndusInd Bank Limited" (Annual_Report_FY2025-26, Note 21, file p.74).

### 8. RELATED-PARTY PERIMETER (AR Note 21, FY26, Rs lakh; Annual_Report_FY2025-26, file p.73 to p.74)

Promoter-group entities and related persons named: Danya Electric Company (partnership firm, "Supreme have Significant Control over the firm"); Jai Bharath Exchangers ("Partnership firm in which the partners have significant control / common control"). Key managers and relatives: Vee Rajmohan (MD); K.V. Pradeep Kumar (WTD); R Sribarati (daughter of MD); Tarun Pradeep (son of WTD).

| Entity | Nature | FY26 | FY25 |
|---|---|---|---|
| Danya Electric Company | Purchases | 2,558.08 | 1,278.20 |
| Danya Electric Company | Sales | 2,459.83 | 1,164.89 |
| Danya Electric Company | Corporate guarantee given | 1,470.00 | 1,470.00 |
| Danya Electric Company | Payable outstanding | 662.82 | 575.64 |
| Jai Bharath Exchangers | Purchases | 153.77 | 267.56 |
| Jai Bharath Exchangers | Sales | 1.12 | 110.97 |
| Jai Bharath Exchangers | Receivable outstanding | 56.60 | 8.65 |
| Vee Rajmohan | Remuneration | 60.00 | 60.00 |
| K.V. Pradeep Kumar | Remuneration | 54.00 | 54.00 |
| Devaraja Iyer Krishna Iyer | Professional fees and sitting fees | 15.00 | nil |
| R Sribarati; Tarun Pradeep | Relatives of KMP | 2.46; 2.80 | nil |

Comment: guarantors Savita Pradeep and V Rajagopalan are named in Note 6 (file p.66) and absent from this table (B02 finding 11). The notice also prints Danya capital contribution "Rs. 12.67 Crores as at 31 March, 2026" and FY27 proposed transactions "Upto Rs. 125 Crore per financial year (2026-2027)" (Annual_Report_FY2025-26, Notice Item 6, file p.28 to p.29).

### 9. PLEDGE AND SHAREHOLDING

- Printed, 31-Mar-2026 (SHP_31Mar2026, file p.1; submitted 10-Apr-2026): promoter pledge, non-disposal undertaking and other encumbrance fields all "false". Promoter and promoter group: 14,284,665 shares, ShareholdingAsAPercentage 0.5716. Locked in: 0.35. Promoter warrants: 449,500.
- Annual_Report_FY2025-26 file p.64 prints two named promoters: "Total 1,30,13,335 ... 52.07% ... 0.00%" change in FY26. The gap to 57.16% is promoter group holders (B02, B01).
- Institutional, latest: foreign portfolio investors category one 145,000 shares, 0.0058; domestic institutions 10,235 shares, 0.0004; insurance companies 10,000 shares, 0.0004 (SHP_31Mar2026, file p.1).
- Last twelve quarters: NOT DISCLOSED in the corpus. One filed pattern is held (31-Mar-2026). SME issuers file half-yearly, and the earlier patterns were not collected (B00, B08). The Sep-2026 pattern is not yet filed (B00).

### 10. VERIFICATION

Documents quoted in this annex, by filename and date:
- Annual_Report_FY2025-26.pdf (21st AGM notice, filed with NSE 01-Sep-2026; Board's Report dated 27-May-2026)
- Results_FY26_Audited_31Mar2026.pdf (board date 27-May-2026)
- Results_Q1FY27_30Jun2026.pdf (board date 13-Aug-2026)
- Concall_Feb_2026_Transcript.pdf (call 11-Feb-2026)
- Concall_Jun_2026_Transcript.pdf (call 02-Jun-2026)
- Concall_Aug_2026_Transcript.pdf (call 17-Aug-2026)
- InvestorPresentation_Q1FY27_17Aug2026.pdf (17-Aug-2026)
- SHP_31Mar2026 (NSE XBRL, quarter ended 31-Mar-2026, submitted 10-Apr-2026)
- Blocks B01 to B09, B12a, B12b, confidence.yaml (run 2026-10-06)

The corpus itself landed in commit 962ea0b29c3b03eaf10b9d2c87722048efcb6bf9. The hash below is HEAD on branch run/supremepwr-2026-10-06 before this stage ran.

CORPUS COMMIT HASH: 38be1cb6ba914fdbc823d1954ef2b1f3c98204bd

---

```yaml
stage: B09b-dossier
company: "SUPREMEPWR"
run_date: "2026-10-06"
model: claude-sonnet-5-5
status: complete
corpus_verdict: "CORPUS GAPPED"
corpus_gaps:
  - document: "Prospectus (Dec-2023 listing)"
    expected_source: "company IR page"
    kind: "findable-missing"
  - document: "Order intimations Oct-2025 to Feb-2026"
    expected_source: "NSE"
    kind: "findable-missing"
  - document: "Shareholding patterns before 31-Mar-2026"
    expected_source: "NSE"
    kind: "findable-missing"
  - document: "20th AGM notice 26-Aug-2025 and AGM and EGM voting results"
    expected_source: "NSE"
    kind: "findable-missing"
  - document: "Results filings Q1 FY26, H1 FY26, Q3 FY26"
    expected_source: "NSE"
    kind: "findable-missing"
  - document: "Annual Report FY2023-24"
    expected_source: "company IR page"
    kind: "findable-missing"
  - document: "Danya Electric partnership deed, auditor and standalone accounts"
    expected_source: "company IR page"
    kind: "plausibly-nonexistent"
  - document: "Peer INDOTECH transcripts"
    expected_source: "company IR page"
    kind: "plausibly-nonexistent"
archetypes:
  - line: "Distribution and inverter duty transformers up to about 25 MVA (Unit 1)"
    archetype: "Order-book business (EPC/defence/capital goods)"
  - line: "Power transformers above 25 MVA up to 200 MVA / 220 kV (Kannur)"
    archetype: "Order-book business (EPC/defence/capital goods)"
transition:
  - line: "Power transformers (Kannur)"
    from_tier: "R2 COST-ADVANTAGED CONVERTER (tender-market supplier, weak pricing power)"
    to_tier: "R3 VALUE-ADDED / SPEC'D SUPPLIER"
    engine: "Kannur load rising from 20-25% against a fixed cost base already in place; 160 MVA / 220 kV CPRI type test (planned Dec-2026/Jan-2027) lifting the qualification ceiling above 25 MVA / 110 kV"
    proof_gate: "Q2 FY27 (Nov-2026): consolidated revenue >= Rs 55 Cr AND Kannur utilisation stated with basis >= 30% AND depreciation plus interest <= 50% of EBITDA gain; Q3 FY27 utilisation > 25%; CPRI certificate filed by 31-Mar-2027"
    recognition_gap: "Open question for Stage 11: does market pricing already reflect the TO state? Resolved via the PE gap; no conclusion here"
    ugliness: "ARTIFACT-OF-CLIMB"
    transition_falsifier: "Q2 FY27 revenue < Rs 55 Cr or Kannur utilisation <= 25% at Q3 FY27; CPRI test fails or slips past Mar-2027; depreciation plus interest > 70% of EBITDA gain again; a peer first 220 kV order at full margin"
dominant_variables:
  - "Kannur load: MVA produced and delivered per quarter with utilisation basis (20-25% stated now)"
  - "220 kV qualification: CPRI certificate for 160 MVA / 220 kV and first 220 kV order margin"
  - "Fixed-cost absorption: depreciation plus interest share of EBITDA gain (69.7% in Q1 FY27) and gross margin"
  - "Funding of the climb: CFO vs capex, standalone advances and payables, DSCR, warrant balance Rs 15.81 Cr due 27-Feb-2027"
business_falsifier: "A Danya deed or third-party price benchmark showing SPEL revenue and profit rest on pass-through trade with a firm co-owned by two promoter-directors, or a Danya default crystallising the Rs 14.70 Cr guarantee, or named-customer disclosure showing the Hyderabad inflow (65.4% of Q1 FY27) is one group with no repeat order"
mental_model_status: "DRAFT - PENDING OPERATOR SIGN-OFF"
fragility:
  variable_count: 7
  verifiability_ratio: "4 of 7 externally observable"
  single_point_failure: "160 MVA / 220 kV CPRI type test (B07: fail or slip past Mar-2027 strands the Kannur premise)"
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
  corpus_commit_hash: "38be1cb6ba914fdbc823d1954ef2b1f3c98204bd"
```
