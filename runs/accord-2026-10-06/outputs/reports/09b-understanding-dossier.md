# ACCORD Halt 1 understanding dossier (stage 09b)

Company: Accord Transformer & Switchgear Ltd (BSE SME 544710, symbol ACCORDTS). Run: runs/accord-2026-10-06. Run date: 2026-10-06. Corpus commit: 9fb42cc6 (branch head at dispatch 405bbe74).

This file is an understanding package. It assembles committed blocks and verifier blocks. It holds no valuation content and no recommendation. Cites in brackets point to block files, for example (B04). Sections 1 to 5 add no new fact. Section 4e carries labelled inference. Section 6 quotes the corpus directly.

Verifier corrections carried through the whole file:
- B12a MAJOR 1: cash excluding all fixed deposits is Rs 7.43 Cr, below borrowings of Rs 8.83 Cr (B12a). The Gate 0 wording "Rs 13.43 Cr excluding all FDs" is wrong, because Rs 13.43 Cr includes Rs 6.00 Cr of FDs under three months.
- B12b: the claim that "Rs 17 Cr of Aditya Birla orders are not filed" is NOT SUPPORTED. Rs 16.93 Cr (29-Jun-26 filing, excluding GST, calc) plus Rs 20.02 Cr (23-Sep-26 filing) is Rs 36.95 Cr, against Rs 37 Cr in the H1 FY27 update (B12b). Where B05 or B06 still carry the gap, this file treats it as closed.
- Credibility grade: B05 grades C. B12b argues D (B12b). The two stand side by side. H1 FY27 results decide between them.
- B08: the "Tipco" file is Accord's own board outcome of 2026-09-03 with a wrong Subject line. Accord re-filed a corrected copy the same day (B08). B00 first called it a third-party document, and its own correction note withdraws that.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

Inventory only. Source: B00 plus the stage blocks that name documents.

### 1. Concalls

| Item | File | Date | Note |
|---|---|---|---|
| Accord H2 FY26 earnings call | concalls/Concall_Jun_2026_Transcript.pdf | 2026-06-01 | The only call held since listing on 2026-03-02 (B00) |
| Peer: Danish Power | peer-concalls/DANISH-* (2 files) | 2025-11-08 (H1 FY26); 2026-05-11 (H2 FY26) | Peer file, not counted against the 12-document cap (B00, B06) |
| Peer: Shilchar Technologies | peer-concalls/SHILCTECH-* (4 files) | 2025-04-22; 2025-10-18; 2026-05-05; 2026-08-14 | Peer file (B06) |
| Peer: Voltamp | none | none | No transcript exists on the screener source (B00, B06) |

Most recent Accord quarter covered by a call: H2 FY26, which is the second half of the year to 31-Mar-26 (B05). Accord reports half-yearly (B00). The half to 30-Sep-26 has closed. The trading window closed on 2026-09-28 and no H1 FY27 results are filed (B00). So a call on H1 FY27 has plausibly not happened yet. No later transcript is plausibly missing. The next call is plausibly due after the H1 FY27 results, which B07 places in November 2026 (filing date NOT FOUND).

### 2. Annual reports

Held: FY26 only (the 12th AR, filed 2026-09-05; the cover letter was re-filed 2026-09-10 with a changed date only) (B00). The latest completed year is present. Three years are NOT held. The prospectus dated 2026-02-26 adds restated FY23 to FY25 and a period to 31-Dec-25 (B00, B01). B00 calls that stub "H1 FY26". The prospectus and stages 3 and 4 call it nine months to 31-Dec-25 (B03, B04). This file uses nine months.

### 3. Results filings

Latest results filing: H2 FY26 and FY26 audited results, filed 2026-05-29 (B00). Pages 3 to 19 are image scans with no text layer. Stages read the AR audited statements in their place (B01, B03). There is no quarter gap between the latest results filing and the AR, because both cover FY26. Management business updates for Q1 FY27 (2026-07-27) and H1 FY27 (2026-10-05) carry revenue, order book and inflow only. The H1 update states its figures are "management estimates and are subject to final audit adjustments" (H1 update p.3). H1 FY27 EBITDA, cash flow and receivables are NOT FOUND (B05, B07).

### 4. Investor presentations

Held: Investor_Presentation_1.pdf, the H2 FY26 deck (call-day deck of 2026-06-01, B12b). Its page 28 Stock Data shows another company's code (SRIGEE 544399) and its page 24 labels FY26 as "9M FY26" (B00). Stages use its financial slides only against the AR.

### 5. Research and rating

Rating: ABSENT. A web search of ICRA, CRISIL, CARE, Acuite and Infomerics on 2026-10-06 found nothing (B00). The result is NOT FOUND, and non-existence is not assumed. Research: EMPTY. No broker or research note is held (B00).

### 6. Corporate actions

21 announcement files, dated 2026-05-23 to 2026-10-05 (B00 inventory). They hold order wins and vendor approvals (2026-05-23 to 2026-09-29), the Tijara land filing (2026-07-03), the Q1 FY27 update (2026-07-27), the AGM notice and board outcome (2026-09-03), the AGM record, voting results and ESOP approval (2026-09-26), and the H1 FY27 update (2026-10-05). Filings from 2026-03-02 to 2026-05-22 are not staged (B00). The superseded duplicate board outcome bd607fbe (Subject line names Tipco) sits in inputs/other/ and is not evidence (B00 correction, B08).

### 7. Freshness pair check

B00 freshness_verdict: FRESHNESS PAIRS OK. All four pairs PASS: results to same-quarter concall, rating bulletin to rationale (no rating held), SEBI order to order text (none referenced), and AR to latest audited annual results (B00). No pair failed.

### 8. Verdict line

**CORPUS GAPPED** (B00 corpus_verdict). Missing documents, by name and expected source:

| Missing document | Expected source | Kind |
|---|---|---|
| Quarterly shareholding patterns and pledge disclosures, post listing (the shareholding folder is empty; BSE API access was denied on 2026-10-06) | BSE | findable-missing |
| Credit rating rationale (none found in the 2026-10-06 web search) | rating agency site | findable-missing (existence not established) |
| H2 FY26 results pages 3 to 19 as text (scan-only) | BSE, plus image reading | findable-missing |
| Listing-period announcements, 2026-03-02 to 2026-05-22 | BSE | findable-missing |
| Research or broker note | none expected | plausibly-nonexistent for a company this size (opacity is a data point) |
| Second and third Accord transcripts | none exist | plausibly-nonexistent (B00: one call since listing) |
| Voltamp transcripts | none exist on the screener source | plausibly-nonexistent (B06) |
| H1 FY27 audited results and call | BSE, due about November 2026 | not yet filed |

Screener export sheets (Profit and Loss, Quarters, Balance Sheet, Cash Flow) came out empty for Accord and all three peers. Only the Data_Sheet carries annual FY21 to FY26 data, with the Quarters block blank (B00).

**Empty folders, repeated in full (the stage 0 empty-folder question was suppressed by the /step1 autonomy contract, B00):** rating (0 files), shareholding (0 files), research (0 files). The standing answer was to carry on with the gaps (B00). The operator should confirm at Halt 1 that these three are empty by intent. The shareholding gap blocks the promoter pledge trend and the FII plus DII qualifier. Listing is under 12 months old (2026-03-02), so the UA multiplier is not available until 2027-03-02 (B00).

---

## SECTION 2: MENTAL MODEL DECLARATION

**STATUS: DRAFT - PENDING OPERATOR SIGN-OFF.** Nothing here is signed. Signing happens only in claude.ai after live-web stress testing.

### PART A: THE FROM STATE

**A1. Archetype.** Order-book business, with build-to-spec pass-through as an overlay (B04). Reason (B04): revenue is booked on customer dispatch clearance against one purchase order per job, and no design-win platform is filed. One archetype covers all lines. Transformers are 82.7% of FY26 revenue, compact and package substations 11.3%, panels 1.2%, service 1.8%, "raw materials and others" 3.0% (B04). The last two lines are of an unknown nature (B04).

**A2. The simple analogy.** Accord is a made-to-order workshop for the boxes that sit between a power line and the people or machines that use the power. A state utility, a private distributor or a solar and wind developer places an order for a set of units at a stated rating (B04). Accord builds them at two plants in Bhiwadi, ships them, and gets paid when the customer's site is ready and the delivery is cleared (B04, B05). Each job is a separate order won by tender or quote, so the customer can go elsewhere next time (B04). The workshop has order cover of Rs 173 Cr at 30-Sep-26 (B00) and a plant certified at 900.36 MVA (B04). It is a price-taker with no moat evidenced (B04, B07).

### PART B: THE TRANSITION

**B1. FROM to TO, per line.** Lines are read from B04 and B07. The ladder is the one in CLAUDE.md. All placements are draft.

| Line | FROM (the tier it leaves) | TO (the tier it claims) | Basis |
|---|---|---|---|
| Line 1: distribution and power transformers won on tender (82.7% of FY26 revenue) | R1 commodity price-taker (B04 states price-taker) | R2 cost-advantaged converter: margin from fixed-cost absorption and a cost position | Management guides 13-15% EBITDA against 9.9% in FY26 (B05). The cost advantage is a claim, and the run found it unproven (B04). |
| Line 2: renewable duty units and higher ratings (inverter duty, wind and solar duty, EHV plan) | R1 | R3 value-added or spec'd supplier: type-tested units, vendor approvals, partial pricing power | CPRI type test on a 17.6 MVA inverter duty unit (B04). The EHV step is 18 to 36 months away, with no machinery order and no filed capex (B07). |

Two findings go with B1. First, FY23 to FY25 ROCE ran 33.0%, 39.8% and 37.8%, then 13.3% in FY26, and about 24% in FY26 without the IPO cash (B01). That history sits above R1 on paper, while B04 finds no pricing power. The business fits no rung cleanly. This is a finding, not a gap to paper over. Second, the TO claim for Line 2 is two rungs from the FROM tier. The ladder rule treats a multi-rung leap as a red mark that needs extraordinary proof. The corpus holds no filed proof for R3 (B07).

**B2. The engine.** Two physical changes carry the arrow.
1. More megavolt-amperes of output through a fixed cost base. In H2 FY26 fixed cost rose 4.2% while revenue rose 52.8%, giving an incremental EBITDA margin of about 18% (B04). Management says operating leverage supports margin as volume rises (B05). H1 FY27 revenue was Rs 52.68 Cr, up 90.07% on a Rs 27.72 Cr base (B00, B13 narrative).
2. A new plant. Land of 20,300 sq m at Tijara was bought on 2026-07-03 for Rs 8.85 Cr plus Rs 1.82 Cr of costs (B05, B08). The AR puts the build at 9 to 10 months from the 2026-09-26 approval, to about July 2027 (B03, B07). The Q1 FY27 update names a "5,000 MVA" facility (B04). No capex amount or machinery order for it is filed (B04, B09).
The pass-through of metal costs through a price variation clause is a third margin lever, but it is a management claim with no clause text in any filing (B04, B06).

**B3. The proof gate.** Draft metric and threshold for /fttcp to test. Accord reports half-yearly, so the gate runs by half-year, not by quarter.
- Gate fires only when all hold: (a) H1 FY27 EBITDA excluding other income at or above 12% (B05 confirm signal), and H2 FY27 at or above 13%, the low end of the 13-15% management range (B05); (b) gross margin after materials at or above 24.1%, the FY26 level (B04); (c) order book above Rs 150 Cr with H2 FY27 revenue at or above Rs 67.3 Cr, the low end of the Rs 120-180 Cr band (B05); (d) H1 FY27 operating cash flow positive and above 50% of H1 PAT, with closing receivables at or below Rs 28.9 Cr (B03, B04).
- State today: not fired. H1 FY27 EBITDA, cash flow and receivables are NOT FOUND (B05, B07). The transition is narrative until the H1 FY27 results are filed.

**B4. The recognition gap (open question, resolved at Stage 11).** Does the TO state, an R2 business on Line 1 and an R3 niche on Line 2, already look reflected in market pricing? This file does not conclude. Stage 11 confirms or denies it through the PE gap. If the TO state is already reflected, the re-rating engine is gone and only earnings growth remains. No number is stated here.

**B5. The ugliness test.** Draft classification: **ARTIFACT-OF-CLIMB (provisional)**. The ugly optic is FY26 revenue down 11.3%, PAT down 24.2%, FY26 ROCE of 13.3%, inventory days up from 83 to 146 on a cost basis, and a CFO that is a receivable release (B01, B03, B05).
- Evidence for ARTIFACT: management ties the revenue fall to a Rs 31 Cr order deferred by customer site delays, with 25 of 35 sets built (B05). H1 FY27 revenue of Rs 52.68 Cr is consistent with the deferred order being recognised (B05, status partial). IPO cash explains most of the FY26 ROCE drop (B01). Both peers showed the same receivable-then-CFO pattern in a growth year, and Shilchar's receivables later unwound (B06).
- Evidence against, kept in the same view: two-year CFO is Rs 0.51 Cr against PAT of Rs 10.45 Cr, 4.9% (B01, B02). FY24 and FY25 CFO were negative on receivable and inventory build (B01). The Q4 FY26 cluster is unexplained: vendor advances of Rs 6.24 Cr with no named supplier, stock in transit of Rs 6.20 Cr, and cash credit up Rs 4.54 Cr (B02). The Rs 31 Cr deferral is about 44% of FY26 revenue, against 5% to 11% at peers (B06).
- Two readings, one separator: the order deferral and working-capital cycle is a temporary feature of the climb, or the business needs more cash than it makes. The H1 FY27 cash flow statement and the vendor ledger separate them (B02).

**B6. The transition falsifier.** Evidence that kills the arrow, not the business:
- H1 FY27 EBITDA excluding other income below 10% with revenue up (B05 kill signal; B04 red mark below 9.9%).
- H2 FY27 revenue below Rs 67.3 Cr, or the order book below Rs 150 Cr with stalled billing (B05).
- Revenue per MVA made falling toward Rs 11.29 lakh, the nine-month FY26 level, which caps 900 MVA near Rs 102 Cr (B04).
- Gross margin down 2 points in a half while metal prices rise (B04, B06 test of the 100% pass-through claim).
- Building slips past July 2027, or a second IPO-object change (B05).

### PART C: WHAT THE MODEL WATCHES

**C1. Dominant variables.** Four, derived from the engine (B2) and the proof gate (B3).
1. **Order-book conversion.** Book Rs 173 Cr at 30-Sep-26, H1 FY27 inflow Rs 77 Cr, H1 revenue Rs 52.68 Cr (B00). H2 needs Rs 67.3 to 127.3 Cr for the Rs 120-180 Cr band (B00, B05). The two largest filings, Rs 19.97 Cr and Rs 20.02 Cr, withhold the customer name (B04).
2. **Realisation per MVA and capacity.** FY25 Rs 16.69 lakh per MVA made, 9M FY26 Rs 11.29 lakh (B04). Certified 900.36 MVA against 1,200+ claimed (B04). Rs 150 Cr equals 900.36 MVA at the FY25 rate (B09).
3. **Operating margin through fixed-cost absorption and pass-through.** FY26 EBITDA 9.9% excluding other income against a 13-15% range (B01, B05). Gross margin 24.1% in FY26 against 20.6% in FY25 (B04). Pass-through share of the book is NOT FOUND (B04).
4. **Cash conversion and working capital.** FY26 CFO Rs 8.70 Cr, of which Rs 13.49 Cr is a receivable release (B01). Cash is Rs 22.33 Cr, 91.4% of it unspent IPO money (B02). Ex-all-FD cash is Rs 7.43 Cr against borrowings of Rs 8.83 Cr (B12a).
These four become the Role 5.5 tracker signals. Everything else is noise.

**C2. What the model rejects.**
- Market-size questions. Accord holds 0.30% of a served market of Rs 19,241 Cr, and the limit is capacity, not demand (B09).
- The Rs 1,600 Cr NHEV programme: claim tier, no filed LOI, scored in no category (B05, B07). It is not a variable until a filing exists.
- The Western Administrative District MoU and the SGB-SMIT collaboration: no value, no signed terms (B07).
- Spot FY26 ROE, ROCE, debt to equity and current ratio: distorted by Rs 20.40 Cr of unspent IPO money (B04).
- Year-on-year growth against FY26: the base holds a Rs 21-22 Cr order deferral (B04).
- Utility tender win-rate questions on the Rs 125 Cr and Rs 100 Cr bids: silent since 2026-06-01 (B05).

**C3. The business falsifier.** Evidence that would force a re-declaration of the FROM business itself, distinct from B6:
- The counterparty and scope of the UGVCL ROBUST 2.0-X purchase order of Rs 87.50 Cr, 53% of the January 2026 book, cannot be confirmed, or its billing never starts (B03).
- The vendor-advance counterparty proves to be a related party, or the advance and the stock in transit prove to be one purchase counted twice (B02 rank 3, an unproven link).
- Filed evidence that revenue is not made-to-order manufacturing at the Bhiwadi plants, for example bought-in goods passed through as trading (the Q4 FY26 cluster is the observation that could show this, B02).
- A going-concern note or an audit qualification. The AR has none today: CARO clause xix carries no material uncertainty (B02).

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE (draft)

The five-question spec is defined once in prompts/13-synthesis-pipeline.md, section BUSINESS UNDERSTANDING NARRATIVE. This is the Halt 1 draft from B01 to B09. Stage 13's copy is the final version.

Accord makes transformers at two plants in Bhiwadi, Rajasthan, and transformers were 82.7% of FY26 revenue (B04). A transformer steps voltage up or down so that power from a grid line, a solar inverter or a wind turbine can be used, and a power network cannot work without one. Accord's range runs from distribution units to 20 MVA power units, including solar and wind duty units (B04). Compact and package substations, which pack a transformer, switchgear and panel into one unit, were another 11.3% of revenue, and panels were 1.2% (B04). The customers are state distribution companies such as UGVCL, private distributors such as Torrent Power, and renewable developers and their EPC contractors such as Aditya Birla Renewables (B03, B05). Each sale is a separate purchase order won by tender or quote and billed when the customer clears the delivery, so a customer can switch at the next order (B04). Top five customers were 73.62% of FY25 revenue and 48.10% of the nine months to 31-Dec-25 (B03). Demand today comes from grid distribution tenders, tracked as UGVCL and GUVNL DT tenders and POs and as RDSS DT sanctions and DISCOM tenders, and from renewable builds, tracked as Aditya Birla Renewables and Sterling and Wilson awards and as MNRE monthly solar and wind capacity additions (B09). The order book stood at Rs 173 Cr at 30-Sep-26 after Rs 77 Cr of orders in the first half (B00). Demand should grow with a domestic transformer market the run sizes at Rs 33,000 Cr with 7.6% growth (B09), and both transcript peers report strong order books and 55 GW of renewable additions in FY26 (B06). Those two forward drivers are checked each month through IEEMA transformer production and order-book data and IEEMA price variation indices (B09). A claimed Rs 1,600 Cr NHEV programme has no filed order, and NHEV and Megha Engineering EV substation awards would test it (B05, B09). The market is not the limit. The limit is capacity: 900.36 MVA certified against 1,200+ MVA claimed, and a new plant not due before about July 2027 (B04, B03). The Emerging Moat scan scored 8.0 and classed it NONE, with weak evidence in five categories and nothing in talent or cannibalisation barrier, Categories 21 and 22 (B07). Transformers have no moat: vendor approvals from UGVCL, PGCIL and Aditya Birla are qualification tickets that peers also hold, and Accord's EBITDA margin is about half of Danish Power's (B04). Substations and panels rest on partner terms, a Lucy Electric licence to 2027-09-28 and a Schneider certification to 2026-12-31, so they carry no moat either (B04, B07). The run did not establish the H1 FY27 margin, mix or MVA made, the price variation share of the book, or the names behind Rs 39.99 Cr of the largest orders (B04, B05).

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. Verticals framed

**Vertical 1: Order-book conversion.**
- Corpus establishes: book Rs 164.25 Cr (2026-01-18, presentation p.30), Rs 156 Cr (2026-05-25, call), Rs 159 Cr (2026-07-22), Rs 173 Cr (2026-09-30) (B00, B05). H1 FY27 inflow Rs 77 Cr and revenue Rs 52.68 Cr (B00). The Rs 37 Cr Aditya Birla figure reconciles to the two filed orders at Rs 36.95 Cr (B12b). The UGVCL ROBUST 2.0-X purchase order of Rs 87.50 Cr was 53% of the January book, dated 2026-01-17, while the registration of 2026-06-24 covers 500 kVA only (B03). Call-day book was 2.57x the H2 low-end need (B05).
- Cannot establish: customer names behind Rs 39.99 Cr of orders (51.9% of H1 inflow, B04); order book composition by customer, rating or product at 30-Sep-26 (B04); whether the Rs 31 Cr deferred order is billed (B05); the outcome of the MVVNL and Torrent bids (B05).
- Deciding questions: (1) Who are the EPC customer and the end owner behind the two unnamed-customer filings? (2) Does the UGVCL registration cover the other ratings in the Rs 87.50 Cr order? (3) Is the Rs 31 Cr deferred order billed and collected in H2 FY27?

**Vertical 2: Realisation per MVA and capacity.**
- Corpus establishes: FY25 Rs 16.69 lakh per MVA made, 9M FY26 Rs 11.29 lakh; UGVCL order Rs 17.18 lakh; certified 900.36 MVA (B04, B09). The Rs 150-200 Cr ceiling maps to Rs 12.5 to 22.2 lakh per MVA on 900 to 1,200 MVA, and peers run Rs 8.2 to 10.9 lakh (B06). Management statements on capacity do not reconcile with each other (B05).
- Cannot establish: H1 FY27 MVA made and mix; filed capacity above 900.36 MVA; capex of the new plant (B04, B09).
- Deciding questions: (1) What MVA did Accord make in H1 FY27, and in which ratings? (2) Is there a chartered-engineer certificate above 900.36 MVA? (3) Do the 3.5 to 5.6 MVA renewable units pull realisation toward the nine-month FY26 level?

**Vertical 3: Operating margin and pass-through.**
- Corpus establishes: EBITDA 9.9% excluding other income in FY26; gross margin 24.1%; H2 FY26 incremental margin about 18% (B01, B04). Management claims 100% price variation cover on orders beyond 3 months (B05). Danish reports about 30% of its book covered, and Shilchar recovered 50 to 60% of the cost rise (B06). Peer margins fell sharply in 2026 (B06). About Rs 19.4 Cr of filed H1 FY27 orders sit in Accord's own fixed-price window (B12b, calc).
- Cannot establish: clause text, share of the book, weights and lag (B04); H1 FY27 EBITDA and gross margin (B05).
- Deciding questions: (1) What share of the Rs 173 Cr book carries a written price variation clause? (2) Did H1 FY27 gross margin hold at 24.1% or better? (3) Did fixed cost stay near Rs 503 lakh per half as revenue rose? (B04 healthy range)

**Vertical 4: Cash conversion and working capital.**
- Corpus establishes: FY26 CFO is a receivable release of Rs 13.49 Cr; two-year CFO Rs 0.51 Cr against PAT Rs 10.45 Cr; cumulative FY23 to FY26 CFO to PAT of minus 0.18 sets the Gate 0 class at AVERAGE (B01). Q4 FY26 cluster: vendor advance Rs 6.24 Cr, stock in transit Rs 6.20 Cr, cash credit up Rs 4.54 Cr, MSME payables Rs 14.95 Cr up 135% (B02). Receivables over six months are Rs 0.83 Cr with nil provision (B02, B03).
- Cannot establish: vendor identity, ageing and purpose; bills discounted with recourse; H1 FY27 cash flow (B02, B05).
- Deciding questions: (1) Do vendor advances fall below Rs 300 lakh and transit stock clear by 30-Sep-26? (2) Is H1 FY27 CFO positive and above 50% of PAT with receivables at or below Rs 28.9 Cr? (3) Does cash credit fall below Rs 300 lakh while IPO cash is still idle?

### 4b. Candidate signal table

Candidates come from B09 section 6. All are UNVERIFIED. Verification and tracker writes happen at Role 5.5 in claude.ai. The "Likely Source" column repeats B09. Mapping to Downstream_Source_Discovery_Protocol_v1_0 classes is not redone here.

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| UGVCL and GUVNL DT tenders and POs | Less than 25% of the Rs 87.50 Cr ROBUST 2.0-X order billed by 2027-03-31, or counterparty not named (B03) | Event-Driven | GUVNL and UGVCL tender portal; BSE order filings |
| Aditya Birla Renewables and Sterling and Wilson awards | No second filed order after lot one with a price variation clause shown (B07), or site-delay deferrals repeat (B05) | Event-Driven | Counterparty exchange filings and releases |
| MNRE monthly solar and wind capacity additions | Monthly additions run below the FY26 pace of 44.6 GW solar and 6.05 GW wind for two quarters (B13 narrative figures; threshold is a draft) | Monthly | MNRE physical progress; CEA |
| IEEMA transformer production and order-book data | Sector order book or MVA production falls year on year while Accord's book falls below Rs 159 Cr (B04 red mark) | Monthly | IEEMA monthly statistics |
| NHEV and Megha Engineering EV substation awards | LOI still not filed with value at FY27 end (B05 kill signal) | Event-Driven | NHEV, MoRTH and NHAI releases; Megha filings |
| RDSS DT sanctions and DISCOM tenders | No award on the MVVNL Rs 125 Cr bid through Q3 FY27 (B05), or DT sanction flow stalls | Quarterly | Ministry of Power RDSS dashboard; DISCOM e-tenders |
| IEEMA price variation indices | Gross margin falls 2 points in a half while the metal index rises (B04, B06 test of the 100% claim) | Monthly | IEEMA PVC index circulars |

### 4c. Fragility read

- variable_count: **6** external variables must go right for the bull case: (1) order-book conversion in H2 FY27; (2) revenue per MVA near Rs 16 to 17 lakh through the mix; (3) pass-through of metal costs; (4) cash conversion; (5) the Tijara build on time for growth after FY27; (6) continuity of the named counterparties, UGVCL and Aditya Birla Renewables (B04, B05, B03, B07).
- verifiability_ratio: **3 of 6 externally observable.** Conversion (1) shows in BSE filings. Cash conversion (4) shows in the H1 FY27 filed balance sheet. Counterparty continuity (6) shows in counterparty filings. Realisation per MVA (2), pass-through share (3) and the build (5) rest on company-narrated figures today (B04: MVA made, clause share and capex are NOT FOUND).
- single_point_failure: **yes, cash conversion.** H1 FY27 operating cash flow below zero with closing receivables above Rs 28.9 Cr breaks the thesis alone (B13 falsification metric).
- fragility_verdict: **FRAGILE.** Many variables, half company-narrated, and one kill-switch.

### 4d. Research brief (the claude.ai work order)

Items 1 to 4 are the PENDING LIVE VERIFICATION links raised by the Section 4e chains. Chains 3 to 5 are still to be built, and their links join this list when built.

1. PENDING LIVE VERIFICATION (chain 1): Aditya Birla Renewables latest quarterly results or investor presentation. Look for the wind and solar project pipeline and commissioning schedule behind the 119-transformer order of Rs 37 Cr. Document to open: the company's filing on its own investor page or BSE or NSE.
2. PENDING LIVE VERIFICATION (chain 1): the GUVNL and UGVCL award document or tender result page for ROBUST 2.0-X, to name the counterparty on the Rs 87.50 Cr order and the ratings it covers.
3. PENDING LIVE VERIFICATION (chain 2): Torrent Power latest annual report, trade payable and MSME disclosure, for how it pays suppliers. Torrent was 35 to 40% of FY25 revenue (B05).
4. PENDING LIVE VERIFICATION (chain 2): the latest published payment-cycle disclosure for state distribution utilities that names UGVCL or GUVNL (document title to be confirmed live; both peers stay out of state utilities for payment delay, B06).
5. NHEV Rs 1,600 Cr LOI: search NHEV, MoRTH and NHAI releases and Megha Engineering EV filings (B05, B09).
6. Credit rating: re-search ICRA, CRISIL, CARE, Acuite and Infomerics live, and the HDFC Bank facility terms (B00).
7. Shareholding patterns and pledge for every quarter since listing, from the BSE shareholding page (BSE API access was denied, B00).
8. Auditor change of 2024-08-07: ADT-3 text and ICAI firm records for both firm numbers (B08).
9. MCA director history for DIN 05113022 against the 2016-2021 disqualification window (B08).
10. Payment source for the Rs 10.67 Cr land purchase of 2026-07-03, against the IPO utilisation statement on BSE (B08).
11. Names of the six anchor investors and the post-listing institutional holding (B08).
12. Danish Power H1 FY27 read, and Voltamp latest filings (B06).
13. IEEMA price variation clause standard text, and a refresh of the stale market data points from 2022 and 2022-23 (B09).
14. Siemens and SGB-SMIT partner naming conflict, and the CPRI "highest rating in the transformer industry" claim (B12b, B07).
15. The Western Administrative District MoU: counterparty name and any sanctions exposure (B12b).
16. Outcomes of the MVVNL (about Rs 125 Cr) and Torrent (about Rs 100 Cr) bids (B05).
17. Ownership and status of Antelp Corporation Pvt Ltd and Accord Global Infra Pvt Ltd on MCA (B08).
18. The date of the H1 FY27 results filing and the Q2 IPO utilisation statement (B07).
19. The identity of the EPC customer behind the Rs 19.97 Cr (2026-06-29) and Rs 20.02 Cr (2026-09-23) filings (B04).
20. Peer pass-through check: Shilchar and Danish H1 FY27 commentary on price variation recovery, to compare with Accord H1 gross margin (B06).

### 4e. Second-order stub (Master v3.7 Rule F)

Two chains, drafted from corpus. Every fact carries its block cite. Inference is labelled. Counterparty facts are not drafted, and the live-web links are marked PENDING LIVE VERIFICATION for claude.ai.

```
CHAIN 1: Rs 173 Cr book at 30-Sep-26 after Rs 77 Cr of H1 FY27 inflow, with Rs 67.3 Cr needed in H2 FY27 for the low end of guidance (B00, B05)
Link 1 [filed]: Two orders, Rs 19.97 Cr incl GST (2026-06-29) and Rs 20.02 Cr excl GST (2026-09-23), sum to Rs 36.95 Cr against Rs 37 Cr for Aditya Birla projects, 119 transformers, "execution within four to five months from the purchase order date" (B12b, H1 update p.2). Both filings withhold the awarding customer name, and together are 51.9% of H1 inflow (B04).
Link 2 [PENDING LIVE VERIFICATION]: who pays, and why now. The end owner, project schedule and the EPC contractor behind both orders are not in the corpus. Claude web should open: (a) Aditya Birla Renewables' latest quarterly results or investor presentation, for the wind pipeline and commissioning schedule; (b) the GUVNL and UGVCL award document for ROBUST 2.0-X, for the counterparty on the Rs 87.50 Cr order. No counterparty fact is drafted here.
Link 3 [INFERENCE]: The four to five month window runs from two order dates, 2026-06-29 and 2026-09-23. Delivery therefore falls from about late October 2026 to about February 2027, which is inside H2 FY27. Billing depends on the customer clearing dispatch, and the FY26 shortfall came from customer site delays, not from Accord's plant (B05, Tr. L198-211). So H2 FY27 revenue depends on counterparty site readiness at least as much as on Accord's output.
Binding constraint: capacity and time. Rs 120 Cr needs 89.6% of certified H2 capacity of 900.36 MVA (B09). The new plant is not due before about July 2027 (B03, B07). Machinery spent from the IPO money is nil, and Rs 7.00 Cr moved from machinery to building (B03, B05).
Unsaid: the call said nothing about the UGVCL order of Rs 87.50 Cr, 53% of the January book, dated 2026-01-17, while the UGVCL registration of 2026-06-24 covers 500 kVA only (B03). The AR shows no order book at all (B03).
Observation that confirms or breaks this chain, and confirm-by date: H2 FY27 revenue at or above Rs 67.3 Cr, with the order book above Rs 150 Cr at 2027-03-31 and at least 25% of the UGVCL ROBUST 2.0-X order billed by 2027-03-31 (B05, B03). Confirm-by date: FY27 results, about May 2027 (B07). Interim read: the Q3 FY27 business update, date NOT FOUND (updates came 2026-07-27 and 2026-10-05, B00).
```

```
CHAIN 2: FY26 CFO of Rs 8.70 Cr is a Rs 13.49 Cr receivable release, and two-year CFO is Rs 0.51 Cr against PAT of Rs 10.45 Cr (B01)
Link 1 [filed]: After listing, in Q4 FY26, vendor advances rose to Rs 6.24 Cr (up Rs 5.40 Cr), stock in transit of Rs 6.20 Cr appeared, cash credit rose Rs 4.54 Cr, and MSME payables reached Rs 14.95 Cr, up 135% (B02). Receivables over six months are Rs 0.83 Cr, up 214%, with nil provision (B02).
Link 2 [PENDING LIVE VERIFICATION]: who pays, and why now. How Accord's largest payers settle their suppliers is not in the corpus. Claude web should open: (a) Torrent Power's latest annual report, trade payable and MSME note; (b) the latest published payment-cycle disclosure for state distribution utilities that covers UGVCL or GUVNL (title to be confirmed live). No counterparty fact is drafted here.
Link 3 [INFERENCE]: H1 FY27 revenue rose 90% on a small base (B00). Danish and Shilchar grew receivables 122% and 144% in years of 28% and 57% sales growth, and CFO lagged PAT (B06). Accord's FY25 showed the same pattern, with receivables up 319% on sales up 63% (B06). So receivables probably rebuild in H1 FY27. If MSME suppliers are paid inside the 45-day window while receivables rebuild, CFO turns negative even at a stable margin. The Section 43B(h) window on Rs 14.95 Cr of MSME payables is undisclosed (B02, B03).
Binding constraint: working capital, not demand. Cash is Rs 22.33 Cr, but 91.4% is unspent IPO money (B02). Cash excluding all FDs is Rs 7.43 Cr against borrowings of Rs 8.83 Cr (B12a). Land of Rs 10.67 Cr and a Rs 7.00 Cr building budget are the next uses of that money, and the land payment source is NOT FOUND (B08).
Unsaid: bill-discount interest rose 350% and discounted bills are undisclosed (B02 rank 10). That implies receivables financing on the books that nobody mentioned on the call. Warranty bank guarantees of Rs 5.32 Cr carry no warranty provision (B02).
Observation that confirms or breaks this chain, and confirm-by date: H1 FY27 CFO positive and above 50% of H1 PAT; closing receivables at or below Rs 28.9 Cr; vendor advances below Rs 300 lakh; cash credit below Rs 300 lakh; inventory days at or below 120 on a cost basis (B03, B04). Confirm-by date: the H1 FY27 results filing, November 2026 per B07 (exact date NOT FOUND).
```

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in claude.ai with live web, before Role 2.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. Accord makes transformers. Two plants in Bhiwadi, Rajasthan, turn out units that change voltage so power can be used (B04).
2. Transformers were 82.7% of FY26 revenue. Compact substations were another 11.3% (B04).
3. Accord listed on the BSE SME board on 2026-03-02. FY26 revenue was Rs 70.07 Cr, down 11% from FY25, and PAT was Rs 4.50 Cr (B00, B01).
4. Customers are state power companies, a private distributor and solar and wind developers. Each order is won on tender or quote. Customers can switch at the next order (B04).
5. A few customers carry the sales. The top five were 73.62% of FY25 revenue (B03). Two big orders in H1 FY27 do not name the customer (B04).
6. Demand is real. Both peers report strong order books and 55 GW of renewable additions in FY26 (B06). Accord's order book was Rs 173 Cr at 30-Sep-26 (B00).
7. Growth in H1 FY27 was 90%, but on a small base. H1 revenue was Rs 52.68 Cr against Rs 27.72 Cr a year earlier (B00, B13 narrative).
8. Management says FY27 revenue will be Rs 120 to 180 Cr. It also says growth of 60 to 80%. The two numbers do not match (B05).
9. Capacity, not demand, sets the limit. The plant is certified at 900.36 MVA. Management claims 1,200 MVA or more. A new plant is not due before about July 2027 (B04, B03).
10. Accord has no moat the run could find. Vendor approvals are tickets that peers also hold. EBITDA margin is about half of Danish Power's (B04, B07).
11. The mental model, in draft: a price-taker that wants to climb from R1 to R2 by spreading fixed cost over more output, and into R3 through renewable units. It is not signed. The proof gate has not fired (Section 2).
12. The fragility read is FRAGILE. Six things must go right, half rest on company statements, and one weak cash reading can break the case (Section 4c, B13).
13. The corpus could not establish the H1 FY27 margin, cash flow, MVA made, price variation cover, shareholding after listing, or any credit rating (B00, B05, B04).
14. The biggest open question: is the FY26 cash picture a one-year working-capital cycle, or does the business need more cash than it makes? The H1 FY27 results, due about November 2026, answer it (B02, B07).
15. The second open question: management said things it has not yet backed with filings. The Rs 1,600 Cr NHEV programme is the clearest case, and the credibility grade is C in B05 and D in B12b (B05, B12b).

---

## SECTION 6: STANDING EXTRACTION ANNEX

Quote-then-comment. Anchor convention: AR and prospectus pages are the `[page N]` markers in the page-marked .txt beside each PDF (AR printed folio = marker + 18; prospectus printed folio = marker minus 8). Transcript cites give the printed "Page N of 14" label and the txt line number. All AR figures are Rs lakh. Prospectus figures are Rs thousand. Business updates are Rs Cr.

### Q1. Units

No per-unit figure is printed in any corpus document. The nearest printed volume figure is installed capacity and production in MVA.

- Quote: "Transformers with Miscellaneous Ratings ... 847.56 [installed, MVA] 473.62 [actual production] 55.88%" for FY2024-25, and "900.36 628.30 69.78%" for FY2025-26 (till Dec 31, 2025), with the note "Production till 3rd quarter is 400.50 MVA. Additional production has been extrapolated based on previous financial years, trends and the increase in plant and machinery capacity." (Accord_Prospectus_Feb2026.pdf, p.123; the installed figure prints split across two lines as "847.5 / 6")
- Quote: "Revenue from Operations 4,52,162.75 7,90,225.33 4,85,369.15 4,07,816.87" in "(Amount in thousands ...)" for the period to 31-Dec-25 and FY25, FY24, FY23 (Accord_Prospectus_Feb2026.pdf, p.110).
- Quote: "Turnover 6,883.17 7,778.97 123.75 123.28 7,006.92 7,902.25" in "(Rs in Lakhs)" (Annual_Report_2026.pdf, p.83).
- Comment: the capacity row is a basket across all ratings, not one product. Revenue per MVA is derived, not printed. B04 derives Rs 16.69 lakh per MVA made for FY25 and Rs 11.29 lakh for nine months FY26 (calc from the two prospectus rows above). B04 also derives per-kVA prices of Rs 1,394 to 2,135 on 200 to 500 kVA UGVCL lots and Rs 609 to 938 on 3.5 to 5.6 MVA solar and wind units (calc, B04). The FY26 production in MVA is not in the AR (B03).

### Q2. Segment capital and debt

- Quote: "The identified segments are Manufacturing Division & Service Activity division." (AR p.83)
- Quote: "Segment Assets 8,365.58 5,989.03 - - 8,365.58 5,989.03" and "Segment Liabilities 3,473.98 3,831.68 - - 3,473.98 3,831.68" (2025-26 and 2024-25, Manufacturing, Service, Total; AR p.83).
- Quote: "Capital Expenditure-Assets/CWIP 151.08 312.55" and "Depreciation 62.60 40.50" (AR p.83).
- Borrowings: not allocated by segment. Totals as printed: "Long Term Borrowings ... Total 47.22 79.32" (AR p.86, Note 5) and "Short Term Borrowings ... Total 836.24 1,670.79" (AR p.87, Note 8).
- Comment: the Service Activity column carries no assets or liabilities. The Total segment result of 450.43 equals PAT in the EPS note (AR p.83, p.95), so it is not an operating profit by segment. Segment capital employed is not printed. Borrowings in Note 5 and Note 8 sum to Rs 8.83 Cr (B01, B12a).

### Q3. Guidance versus aspiration

Source: Concall_Jun_2026_Transcript.pdf, call of 2026-06-01. Words omitted from a quote are marked [...].

| Item | Quote | Class |
|---|---|---|
| FY27 revenue | "it would be around INR120 crores to INR180 crores. So that is going to be the revenue for the financial year '27." (printed Page 6, L262-264) | (a) guidance with a period |
| FY27 growth | "we are expecting around 60% to 80% from our current revenue." (printed Page 5, L251-252; repeated Page 6, L259) | (a) guidance with a period; does not reconcile with the rupee band (B05) |
| Growth after FY27 | "from the next year going onward, it would be around 30% to 50%." (printed Page 6, L259-260) | (a) guidance with a period |
| Deferred order | "the revenue was not recognized till March, but it is going to be recognized in the current financial year." (printed Page 4, L206-207) | (a) guidance with a period |
| Expansion timeline | "installation will start -- on the ground it will start after 2 to 3 months, and 6 months minimum is required to get the manufacturing start there." (printed Page 6, L284-285) | (a) guidance with a period (from June 2026) |
| NHEV stations | "by the end of this financial year, we should have the work for 10 to 15" (printed Page 13, L584; the rest of the sentence runs onto the next page) | (a) guidance with a period; no filing supports it (B05) |
| EBITDA margin | "we are trying to maintain between 13% to 15%." (printed Page 11, L479) | (b) aspiration; the question asked about "the next 2 to 3 years" and the answer states no period (B05) |
| PAT margin | "we are expecting it to 9% to 11%. Maybe 10% we can take it as an average." (printed Page 11, L480-481) | (b) aspiration, same frame |
| NHEV programme | "approximately INR1,600 crores worth of compact substations will be required." and "This LOI is already issued." (printed Page 13, L572-575) | (b) aspiration; LOI not filed on BSE (B05) |
| Dividend | "maybe around 1 year or 2 years down the line, the Board can decide on the dividend policy." (printed Page 5, L231-232) | (b) aspiration |
| Plant ceiling | "about INR150 crores we can manage in this factory without any hurdles" and "up to INR200 crores business from this existing facility" (printed Page 6, L274-277) | (c) capacity only |
| Utilisation | "Currently, it is around 75% to 80%." and "[...] around more than INR120 crores for the revenue, so we'll be utilizing around 90% our capacity" (printed Page 11, L488-491) | (c) capacity only |
| New land | "Identified land for a proposed manufacturing facility expansion for approximately 2.50 lakh square feet" (printed Page 3, L146-147) | (c) capability only |

Written statements:
- "Installed Manufacturing Capacity 1,200+ MVA" and "Continued development of the new 5,000 MVA transformer manufacturing facility to support future growth" (Q1 FY27 update, 2026-07-27, p.2). Class (c), no period, no capex stated.
- "The proposed construction is expected to be completed within approximately 9-10 months from the date of approval of the Members." (Annual_Report_2026.pdf, p.33). Class (a), approval dated 2026-09-26 (B03).

Comment: only the revenue band, the post-FY27 growth range and the expansion timeline carry a period. The margin ranges do not, so FY27 margin is not strictly guided (B05).

### Q4. Concentration

- Quote: "Our top ten customers contributed 66.74%, 84.16%, 71.32% and 89.09% of our revenue from operations for the period as at December 31, 2025 and Fiscal Years ended March 31, 2025, 2024 and 2023, respectively and our top five customers contributed 48.10%, 73.62%, 58.29% and 79.60%" (Accord_Prospectus_Feb2026.pdf, risk factor text, p.31). Table rows as printed: "Top five customers 217,508.19 48.10% 581,773.00 73.62% 2,82,935.00 58.29% 3,24,631.00 79.60%" (p.111; the figure for the period to 31-Dec-25 is Rs thousand).
- Quote (customer, FY25 only): "Torrent Power was the major customer in financial year '25, so it account for around 35% to 40% for the financial year '25." (Concall_Jun_2026_Transcript.pdf, printed Page 10, L424-425). Quote (FY26): "there are around six or seven customer which forms part of the 45% of the revenue." (L425-426). Quote (follow-up promised): "I will get back to you on this on the proper note" (L423).
- Product: transformers 82.7%, compact and package substations 11.3%, panels 1.2%, service 1.8%, raw materials and others 3.0% (AR p.63 chart, read via B04; the chart has no period label, and B04 notes it does not reconcile with the nine-month table at Pros. p.113).
- Order concentration: the UGVCL ROBUST 2.0-X purchase order of Rs 87.50 Cr is 53% of the Rs 164.26 Cr book of 2026-01-18 (B03, Pros. p.114-115).
- Geography: NOT DISCLOSED. No state or region split is printed in any document read. The Q1 FY27 update says "Pan India & Global (Middle East, USA, Africa & Asia)" (p.2), while the AR reports nil foreign exchange earnings (B03) and the prospectus says it has no export operations (Pros. p.125, per B12a).
- Top single customer share for FY26: NOT DISCLOSED. The AR carries no customer table (B03).
- Comment: concentration is high and has no FY26 filed figure. The follow-up promised on the call has not arrived (B05).

### Q5. Promise ledger

| Promise | Made | Status | Evidence anchor |
|---|---|---|---|
| Land for about 2.50 lakh sq ft | 2026-06-01 (call L146) | Delivered, 12.6% under size | 20,300 sq m bought 2026-07-03 (B05; H1 update p.3) |
| Healthy order book about Rs 156 Cr | 2026-06-01 (L150) | Delivered | Rs 159 Cr (2026-07-22), Rs 173 Cr (2026-09-30) (B05; H1 update p.2) |
| Rs 31 Cr deferred order plus Rs 3 Cr recognised in FY27 | 2026-06-01 (L206-211) | Partial: H1 revenue consistent, billing NOT FOUND | H1 update p.2 (B05) |
| FY27 revenue Rs 120-180 Cr | 2026-06-01 (L262-264) | Partial: in progress, H2 needs Rs 67.3 to 127.3 Cr | H1 update p.2 (B05) |
| Expansion ground work in 2-3 months, manufacturing in 6 months | 2026-06-01 (L284-285) | Partial, slipping: build 9 to 10 months from 2026-09-26 | AR p.33 (B05) |
| IPO machinery funds "for the new plant only" | 2026-06-01 (L298-299) | Partial: Rs 700 lakh moved from machinery to building | Board outcome 2026-09-03 p.1-2; AR p.33 (B05) |
| NHEV work for 10 to 15 stations by FY27 end | 2026-06-01 (L584) | Partial: "continued supplying" only, LOI NOT FILED | Q1 FY27 update p.3 (B05) |
| MVVNL about Rs 125 Cr and Torrent about Rs 100 Cr bids to open in June or July | 2026-06-01 (L140-145) | Missed: no outcome by 2026-10-05 | H1 update and Q1 update silent (B05) |
| Customer concentration note to follow | 2026-06-01 (L423) | Missed | No follow-up in AR or filings (B05) |
| IPO machinery spend Rs 1,302.67 lakh, all FY27 | Prospectus 2026-02-26 (Pros. p.75) | Slipped: nil spent to 2026-09-02 | AR p.33 (B03) |
| IPO working capital use Rs 275 lakh FY26 and Rs 725 lakh FY27 | Prospectus 2026-02-26 (Pros. p.75) | Delivered early: 93.2% used by 2026-09-02 | AR p.33 (B03) |
| FY26 working-capital days: receivables 96, inventory 83, payables 56 | Prospectus 2026-02-26 | Missed: 113, 146 (cost basis) | AR p.64, p.77-78 (B03, B12a) |

Count from B05: 2 delivered, 5 partial, 2 missed from the call. Credibility grade C in B05, D in B12b.

### Q6. Restated bases

- Quote: "The figures of the previous years have been regrouped / rearranged wherever necessary." (AR p.83, Note 2.9). No amounts are given.
- B02 finds three FY25 changes: PBT 798.05 in the AR against 817.44 in the prospectus restatement (a 19.39 prior-period expense); a book overdraft of 569.38 lakh moved from other current liabilities into borrowings; and 8.24 lakh moved from other expenses to finance cost (B02, Note 2.9 p.83; Pros. p.160). The FY25 debt to equity of 0.55 stays on the old basis (B02).
- Quote (comparative as printed in the latest filing): "Turnover ... 7,902.25" and "Segment Result Profit/(Loss) ... 450.43 594.37" (AR p.83); "(e) Basic & Diluted Earnings Per Share Pre - bonus (₹) (a/b) 2.90 217.94" and "(f) ... Post - bonus (₹) (a/c) 2.90 4.27" (AR p.95).
- Quote (prospectus, restated): "Restated Profit for the Year 29,133.72 60,536.03 16,066.76 8,781.06" in Rs thousand, for the period to 31-Dec-25, FY25, FY24, FY23 (Pros. p.110).
- Comment: FY25 PAT is 594.37 lakh in the AR and 605.36 lakh in the restated prospectus (60,536.03 thousand), an 11 lakh gap (B01, B02). No reorganisation, transfer or scheme is behind these changes. They are reclassifications and restatement differences. Per-share data for FY25 is restated for the bonus issue.

### Q7. Corporate-action clauses

- Scheme, demerger, merger and share repurchase: none in the corpus. Quote: "The company has not entered into any scheme of arrangement which has an accounting impact on current or previous financial year." (AR p.84, Note 2.11(f)). No scheme document to fetch.
- Fresh issue and bonus: "Issued during the period 55,62,000 556.20" and "Add: Bonus shares issued during the period 1,47,16,950 1,471.70" (AR p.85, Note 3(a)). The bonus ratio is not printed in the lines read. Arithmetic: 1,47,16,950 divided by the opening 2,94,339 shares is exactly 50 (calc). Appointed and effective dates of the bonus are not in the corpus. The prospectus (2026-02-26) and the listing (2026-03-02) date the IPO (B00).
- IPO-object alteration: "Approved and recommended to the Members the Alteration in the Objects of the Initial Public Offer ('Offer') for which amount was raised by the Company. by reallocating ₹700 Lakhs (Rupees Seven Hundred Lakhs only) from the object 'Capital expenditure towards purchase of machinery and equipment' towards a new object, namely 'Construction of building/civil structure on the Company's property and expansion of plant capacity'" (Board outcome 20260903-0bf73e52, p.1-2). Approved by special resolution at the 2026-09-26 AGM (B03, B08). Table as printed: machinery "1,302.67 – 1,302.67 602.67", working capital "1,000.00 931.59 68.41 68.41", new object "– – – 700.00", total "2,558.52 1,187.44 1,371.08 1,371.08" (AR p.33).
- ESOP 2026: "shall not exceed 5,00,000 (Five Lakhs) options which will be convertible into 5,00,000 (Five Lakhs) Equity Shares of face value of Re. 10/- (Rupee Ten only) each" and "Pricing formula shall be decided by the Committee." and "Vesting: not earlier than 1 year and not later than 5 years from grant date." (ESOP disclosure 20260926-3aa16089, p.2). AR: "Price shall be as determined by Nomination and Remuneration Committee and shall not be less than face value of shares." (AR p.35).
- Liability allocation and undertaking definitions: not applicable, no scheme.

### Q8. Related-party perimeter (AR Note 2.3, p.81-82, Rs lakh, FY26 then FY25)

Quote: "ABL Electricals: Enterprise over which KMP has significant influence Accord Global Infra Private Limited - Enterprise over which KMP has significant influence" (AR p.81).

| Entity or person | Nature | FY26 amount | FY25 amount |
|---|---|---|---|
| Pradeep Kumar Verma, MD | Director remuneration; repayment of unsecured loan | 32.00; 4.50 | 18.00; 100.90 |
| Shalini Singh, director | Director remuneration; repayment of unsecured loan | 32.00; 7.50 | 18.00; 2.30 |
| Nitin Gupta, CFO | Remuneration; expense reimbursement | 12.00; 0.38 | NIL |
| Tulsi Sharma, CS | Remuneration | 1.51 | NIL |
| Neelam, Dipakkumar Thakkar, Amrendra Nath Shukla | Director sitting fees | 0.80; 0.80; 0.70 | NIL |
| Antelp Corporation Pvt Ltd | Sale of goods or services ("KMP relative has an interest", AOC-2, AR p.54) | 29.44 | NIL |
| ABL Electricals (proprietorship of Pradeep Kumar Verma, per AOC-2) | Acceptance of unsecured loan; repayment; purchase of goods; sale of goods | 150.00; 80.36; 64.15; NIL | 117.60; 146.47; 24.25; 40.63 |
| Accord Global Infra Pvt Ltd | Named as an enterprise under KMP influence; no transaction printed | none printed | none printed |

Balances at 2026-03-31 (AR p.82): "Pradeep Kumar Verma ... Unsecured loan 54.42 58.92", "Shalini Singh ... Unsecured loan 58.71 66.21", "Antelp Corporation Private Limited ... Debtors 29.44 NIL", "ABL Electricals ... Unsecured loan 69.64 NIL", "ABL Electricals ... Creditors 67.59 NIL". Also "Shalini Singh ... Director Remuneration 29.52 30.43" outstanding.
Comment: promoter-linked short-term borrowings of Rs 182.78 lakh ("From directors repayable on demands", AR p.87, Note 8) match the three year-end loan balances 54.42, 58.71 and 69.64 (sum 182.77, a 0.01 rounding gap). The ABL FY25 loan column fails its own arithmetic (B02 rank 8). Former CFO pay and an 11.68 lakh reimbursement to ABL are not in the table (B02). The former CFO Ranjan Kumar Samal is listed as key management at p.81 with no amount.

### Q9. Pledge and shareholding

Promoter pledge and holding for the last twelve quarters as filed: NOT DISCLOSED in the corpus. The shareholding folder is empty, and the company listed on 2026-03-02, so fewer than twelve post-listing patterns can exist. Quarterly patterns after listing are NOT FOUND (B00).

Points held:
- Quote: "Pradeep Kumar Verma 1,25,000 42.47 / Shalini Singh 1,25,000 42.47 / Total 2,50,000 84.94" one year before the prospectus date, and "Total 2,50,000 100.00" two years before (Prospectus, p.68).
- Quote: "Pardeep Kumar Verma 63,75,000 30.99%" and "Shalini Singh 63,75,000 30.99%" at 31-Mar-26; the Total row prints "1,27,50,000 84.94%" (AR p.85, Note 3(c)). Two times 30.99% is 61.97%, so the printed 84.94% total is stale (B01, B08).
- Quote: "As on 01/06/2026 ... 61.97% 38.03% ... Promoter & Promoter Group Public" (Investor_Presentation_1.pdf, p.28, a page that also prints another company's code).
- Pledge quote: "As on the date of this Prospectus, none of the Equity Shares held by our Promoters are pledged." (p.69) and "None of the Equity Shares held by our Promoter/ Promoter Group are pledged or otherwise encumbered." (p.73), both dated 2026-02-26. No post-listing pledge evidence (B01).
- Institutional holding, latest: NOT DISCLOSED in filed documents. Six anchor investors and about 10.44% domestic institutions are MEDIA REPORTED only (B08).
Comment: pledge stands at 0% as of the prospectus date and the AR shows promoter shares unchanged in FY26 (B08). Free promoter shares come out of the one-year lock-in on 2027-03-02 (a reading of ICDR, not verified, B07).

### Q10. Verification

Documents quoted in this annex (all inside runs/accord-2026-10-06/inputs/):

| File | Document date |
|---|---|
| annual-report/Annual_Report_2026.pdf | FY2025-26 (12th AR), filed 2026-09-05 (B00) |
| prospectus/Accord_Prospectus_Feb2026.pdf | 2026-02-26 |
| concalls/Concall_Jun_2026_Transcript.pdf | call of 2026-06-01 |
| announcements/20261005-4575ac94-bbad-49a2-a7fb-0067fc2359a6.pdf | 2026-10-05 (H1 FY27 update) |
| announcements/20260727-Q1FY27-business-update.pdf | 2026-07-27 |
| announcements/20260903-0bf73e52-4ecd-47fb-86fb-f79dc9013fd6.pdf | 2026-09-03 (board outcome) |
| announcements/20260926-3aa16089-3ff9-4268-ad6d-bdcc5d6637cc.pdf | 2026-09-26 (ESOP disclosure) |
| presentation/Investor_Presentation_1.pdf | H2 FY26 deck, stock data as on 2026-06-01 |

Items taken from stage reports and blocks, not re-read from source: the AR p.63 revenue mix chart (B04), the AR p.54 AOC-2 wording (B08), the Pros. p.113, p.114-115, p.125 figures (B03, B04, B12a), and the UGVCL order facts (B03).

CORPUS COMMIT HASH: 9fb42cc6

---

```yaml
stage: B09b-dossier
company: "ACCORD"
run_date: "2026-10-06"
model: claude-sonnet-5-5
status: complete
corpus_verdict: "CORPUS GAPPED"
corpus_gaps:
  - document: "Quarterly shareholding patterns and pledge disclosures since listing (shareholding folder empty)"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "Credit rating rationale (none found in web search 2026-10-06; existence not established)"
    expected_source: "rating agency site"
    kind: "findable-missing"
  - document: "H2 FY26 audited results pages 3 to 19 as text (scan-only)"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "Listing-period announcements 2026-03-02 to 2026-05-22"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "Research or broker note"
    expected_source: "company IR page"
    kind: "plausibly-nonexistent"
  - document: "Second and later Accord concall transcripts; Voltamp transcripts"
    expected_source: "company IR page"
    kind: "plausibly-nonexistent"
archetypes:
  - line: "All lines (transformers 82.7%, compact substations 11.3%, panels 1.2%)"
    archetype: "Order-book business (build-to-spec overlay)"
transition:
  - line: "Line 1: distribution and power transformers on tender"
    from_tier: "R1 commodity price-taker"
    to_tier: "R2 cost-advantaged converter"
    engine: "More MVA through a fixed cost base (H2 FY26 fixed cost +4.2% on revenue +52.8%); then a new Tijara plant, build 9-10 months from 2026-09-26"
    proof_gate: "H1 FY27 EBITDA ex other income at or above 12% and H2 FY27 at or above 13%; gross margin at or above 24.1%; order book above Rs 150 Cr with H2 FY27 revenue at or above Rs 67.3 Cr; H1 FY27 CFO above 50% of PAT with receivables at or below Rs 28.9 Cr"
    recognition_gap: "Open question: does market pricing already reflect an R2 state? Resolved at Stage 11 via the PE gap. No conclusion here."
    ugliness: "ARTIFACT-OF-CLIMB (provisional)"
    transition_falsifier: "H1 FY27 EBITDA ex other income below 10% with revenue up; H2 FY27 revenue below Rs 67.3 Cr or book below Rs 150 Cr; revenue per MVA toward Rs 11.29 lakh; gross margin down 2 points in a half"
  - line: "Line 2: renewable duty units and higher ratings (EHV plan)"
    from_tier: "R1 commodity price-taker"
    to_tier: "R3 value-added or spec'd supplier (two-rung claim; no filed proof)"
    engine: "Type-tested inverter duty units and vendor approvals; new plant for higher ratings; no machinery order or capex amount filed"
    proof_gate: "Second filed Aditya Birla Renewables or EPC order after lot one, with a price variation clause shown, plus EHV machinery purchase orders with value"
    recognition_gap: "Open question: does market pricing already reflect an R3 state? Resolved at Stage 11 via the PE gap. No conclusion here."
    ugliness: "ARTIFACT-OF-CLIMB (provisional)"
    transition_falsifier: "No second filed order and no machinery PO by FY27 end; build slips past July 2027 or a second IPO-object change"
dominant_variables:
  - "Order-book conversion (book Rs 173 Cr, H2 FY27 needs Rs 67.3 Cr at the low end)"
  - "Realisation per MVA and capacity (Rs 16.69 lakh FY25 vs Rs 11.29 lakh 9M FY26; 900.36 MVA certified vs 1,200+ claimed)"
  - "Operating margin via fixed-cost absorption and pass-through (9.9% FY26 vs 13-15% range)"
  - "Cash conversion and working capital (FY26 CFO is a Rs 13.49 Cr receivable release; two-year CFO 4.9% of PAT)"
business_falsifier: "UGVCL Rs 87.50 Cr order counterparty or scope cannot be confirmed or billing never starts; vendor advance proves to be a related party or a double count; filed evidence that revenue is not made-to-order manufacturing at the Bhiwadi plants; going-concern note or audit qualification"
mental_model_status: "DRAFT - PENDING OPERATOR SIGN-OFF"
fragility:
  variable_count: 6
  verifiability_ratio: "3 of 6 externally observable"
  single_point_failure: "cash conversion: H1 FY27 operating cash flow below zero with closing receivables above Rs 28.9 Cr"
  fragility_verdict: "FRAGILE"
candidate_count: 7
second_order:
  chains_drafted: 2
  pending_live_links: 4
  confirm_by_observations: 2
research_brief_items: 20
plain_summary_points: 15
annex:
  present: true
  questions_answered: 10
  corpus_commit_hash: "9fb42cc6"
```
