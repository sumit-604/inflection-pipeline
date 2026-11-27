# HALT 1 UNDERSTANDING DOSSIER: Keltech Energies Ltd (KELTECH, BSE 506528)

Run date 2026-11-15. NO-CONCALL MODE (B00). Standalone filer. Stage 09b, assembly only.
Units: AR and results filings are in Rs lakh; CRISIL and screener are in Rs Cr. Every figure carries its unit.
Source-fidelity: the errata file (outputs/reports/ERRATA-verifier-corrections.md) governs wherever a block or stage report differs. Corrections F1 to F7 (Verifier A), Verifier B F1 to F4, Verifier C recomputes and Verifier D Q9 are applied below. Where a stage block carries an older value, the corrected value is used and the change is named.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

Inventory only. Source: B00 (inventory, freshness_pairs, corpus_manifest, input_gaps).

1. CONCALLS. None held. The company holds no earnings calls (B00: concalls_available false; AR FY2025-26 p.68 lists presentations "None", B03). Most recent quarter covered by any Keltech call: none. The latest quarter reported is Q2 FY27 (quarter ended 30 Sep 2026), filed 2026-11-14 (B00). No later quarter has reported, so no newer call is missing. The absence is declared, so it is a data point on opacity, not a missing upload.
   Peer transcripts held (12, not Keltech calls): APOLLO Q3FY26 (call 9 Feb 2026), Q4FY26 (19 May 2026), Q1FY27 (8 Aug 2026), Q2FY27 (26 Oct 2026); PREMEXPLN Q2FY26 (call 14 Nov 2025), Q3FY26 (20 Feb 2026), Q4FY26 (filed 2 Jun 2026), Q1FY27 (filed 20 Aug 2026); SOLARINDS Q2FY26 (call 11 Nov 2025), Q3FY26 (4 Feb 2026), Q4FY26 (15 May 2026), Q2FY27 (4 Nov 2026) (B00 corpus_manifest).
2. ANNUAL REPORTS. AR FY2025-26 held in inputs/annual-report/ (BSE cover letter 2026-07-13, B00). AR FY2024-25 held in inputs/other/ (cover letter 2025-07-18), preserved and consumed only by Verifier B (B00; B12b F1). The latest completed FY is present. Two years are held, not three. A FY2023-24 AR is ABSENT.
3. RESULTS FILINGS. Latest: Q2 FY27, board outcome dated 2026-11-14. Also held: Q1 FY27 (2026-07-31; pp.2 to 4 are OCR), Q4 FY26 audited (2026-05-27); Q3 FY26 (2026-02-12) sits in inputs/other/, scanned, never consumed (B00). Quarter gap between the latest results and the latest AR: two quarters (Q1 FY27 and Q2 FY27 post-date the AR's year end of 31 Mar 2026); both are held.
4. INVESTOR PRESENTATIONS. ABSENT. The company issues none (B00; B03 AR p.68).
5. RESEARCH / RATING. CRISIL rating rationale dated 2026-02-13, PDF and HTML copy (BBB+ Stable / A2 on Rs 258 Cr bank facilities, B00). No broker or research note is held. ICRA's Feb 2026 non-cooperation report is referenced by media only; the fetch failed (B08).
6. CORPORATE ACTIONS. 10 announcement PDFs dated 2026-02-13 to 2026-11-02: credit-rating intimation (13 Feb); large-corporate disclosure (22 Apr); price-movement clarification (25 Apr); CESTAT order (12 May); AGM outcome and scrutinizer report (7 Aug); change-in-management letter (7 Aug); scrutinizer corrigendum (28 Sep); promoter inter-se share transfer LOI (28 Oct); board meeting intimation (2 Nov) (B00). The 2026-04-24 exchange clarification query has no attachment on BSE (B00).
7. FRESHNESS PAIR CHECK. B00 freshness_verdict: FRESHNESS PAIRS OK. No pair failed.
   - Results to concall: SKIPPED, absence declared (B00).
   - Rating bulletin to full rationale: PASS, 6 page CRISIL rationale held (B00).
   - SEBI order to order text: PASS, no SEBI order referenced; a CESTAT order is referenced and its announcement is held (B00).
   - AR to latest audited annual results: PASS, AR FY2025-26 matches the Q4 FY26 audited filing (B00).
8. CORPUS GAPS (inventory)
   Findable but missing (operator upload list):
   - BSE shareholding pattern for the quarter ended 30 Sep 2026, scrip 506528. Expected source: BSE. Only a screener.in capture is held (promoter, DII, public); no pledge data and no FII line. BSE returned Access Denied (B00, B08).
   - Peer P&L, Quarters, Balance Sheet and Cash Flow tabs for PREMEXPLN and APOLLO. Expected source: screener export, re-saved from Financials.xlsx. Only Data_Sheet CSVs exist (B00).
   - Q3 FY26 results in readable form (held scanned in inputs/other/). Expected source: BSE. Low effect: the Q4 FY26 filing prints Q3 FY26 (errata, Verifier B F4).
   - The 2026-04-24 exchange clarification query attachment. Expected source: BSE (B00).
   - ICRA rating rationale of Feb 2026 and the Jul 2026 withdrawal notice. Expected source: rating agency site (B08).
   - AR FY2023-24. Expected source: BSE or company IR page. Multi-year trends beyond the FY25 comparatives stay NOT FOUND (B02, B03).
   - PREMEXPLN Q2 FY27 transcript and SOLARINDS Q1 FY27 transcript. Expected source: BSE. These may not yet be filed (B00).
   Plausibly nonexistent (the company publishes none; opacity is itself a data point):
   - Keltech concall transcripts.
   - Keltech investor presentations.
   Not a gap: prospectus (long-listed, CIN year 1977) and research/ (B00).
   Quality notes, not gaps: Q1 FY27 pp.2 to 4 are tesseract OCR; the Q2 FY27 text layer is garbled in places (Verifier A read pp.5 to 6 from the page image).
9. Open item carried from confidence.yaml: Verifier B coverage reads 7 of 9 material items (78) if two partial catches count as caught, and 5 of 9 (55.6) if they do not. The 60 line in operator ruling OR-29 sits between the two. The orchestrator used the emitted 78. Whether partial catches count is an operator ruling.

Corpus line:
CORPUS GAPPED

---

## SECTION 2: MENTAL MODEL DECLARATION

STATUS: DRAFT - PENDING OPERATOR SIGN-OFF. This declaration is not signed. Signing happens only in claude.ai after live-web stress-testing.

### PART A: THE FROM STATE

A1. ARCHETYPE (by line)
- Explosives (86.0% of revenue, B04): Commodity converter (CLAUDE.md library; Section 1B Amendment 17 binds). Spread is explosives price less ammonium nitrate cost; materials run 66.6% of revenue (B09 analyst basis; B03 Note 19). Licence and footprint traits sit on top of it (B04: 12 plants, Explosives Act licences) but pricing power reads weak (B04).
- Perlite (10.5% of revenue, B04): Commodity converter, minor line.
- TNT slice (no revenue booked): fits no known archetype yet. End use is unproven (B04 TNT_DEFENCE_UNPROVEN; Verifier B F3). It is a finding, not a gap to paper over.

A2. THE SIMPLE ANALOGY
Keltech runs a licensed powder mill. It makes blasting product by the tonne and supplies it to mines, quarries and road builders. Its main raw material is one commodity chemical, and that chemical is most of its cost (B09). The biggest public customers pick the lowest bid (B06), so Keltech earns a thin slice per tonne. It wins by being licensed, close to its customers, and able to supply the right blend for the rock. It is now building a second kind of plant, for TNT, and has not told anyone who will use it (B04, B05).

### PART B: THE TRANSITION

B1. FROM TO TO (quality ladder, CLAUDE.md)
- Explosives line: FROM R2 (cost-advantaged converter on a licence and footprint position). The competing reading is R1: Coal India and Singareni bulk is L1 priced at thin or negative margin (B06), and the Explosives segment result is 6.67% of external revenue on the AR basis (B04). TO, as the build implies: R3 (value-added or spec'd supplier), reached only if TNT or energetics earns spec-in status with a named customer. The company states no rung. One rung in two to three years is the base rate (CLAUDE.md), so R3 is within it. If TNT is own-use input only (reading B, B04), the line stays at R2 with a better cost position and the tier claim fails.
- Perlite line: FROM R1; TO R2 is claimed by MD&A direction only (pharma filter aid, cryogenic insulation; B03 guidance_table). No quantified evidence supports it (B07). Volume grew +0.2% on the FY26 AR comparative (B03), and the FY25 volume base is stated two ways (24,584 MT and 18,704 MT; errata, Verifier B F1).

B2. THE ENGINE
Two things physically change.
1. The TNT and nitration build at Garamsur. CRISIL: about Rs 190 Cr cost, Rs 135 Cr term debt, operations April 2027 (CRISIL p.2, p.3; B05). CWIP rose from 3,800.82 Rs lakh (Mar 2026) to 6,280.63 Rs lakh (Sep 2026) (B05 TNT pace; B01). The AR calls the technology "Nitration Based Accessories", to be "commissioned fully in 2027" (AR p.29; B07). Mechanism: spend converts to PPE, depreciation steps up, and either external TNT revenue appears (reading A) or bought-in accessory inputs fall (reading B, B04).
2. The operating leverage on Explosives volume. Volume rose 8.4% in FY26 (B09; AR p.28). Explosives revenue rose 35.7% in H1 FY27 (B05). The hidden improvement is the like-for-like EBITDA margin: 7.68% against 6.06% after stripping the FY25 reversals of 884.72 Rs lakh (B03). Fixed charges absorb part of it: H1 FY27 depreciation +28.7% and finance cost +76.3% (OCR read, B04).

B3. THE PROOF GATE (what /fttcp tests; binary, two legs, both required)
- Leg 1, TNT: the Q4 FY27 filing (quarter ended 31 Mar 2027) or the Q1 FY28 filing shows CWIP moved into PPE, AND a filed licence, offtake or first booked revenue outside the Explosives and Perlite segments names a customer (B05 trigger 1; B04 separator; B07 optionality register). Interim check: CWIP plus advances at 31 Dec 2026 must not sit below about Rs 150 Cr (B05 kill line). Cost must not exceed Rs 190 Cr and debt must not exceed Rs 135 Cr (B05).
- Leg 2, margin: Explosives segment result over segment revenue, filing basis, at or above 6.5% for two consecutive quarters (B05 trigger 2). The H1 FY27 base is 6.44% (1,953.31 on 30,323.32 Rs lakh; errata F2), not 6.47%. The 6.5% threshold was set against the wrong base and the operator may reset it at sign-off. Q2 FY27 EBITDA ex other income is 8.16% and H1 is 7.82% (errata F3), against B05's 8% test for operating leverage (trigger 3).
- Until both legs fire, the transition is narrative. As of Q2 FY27 neither has fired (B05, B07).

B4. THE RECOGNITION GAP (open question for Stage 11)
Open question: does the current market pricing already reflect the TO state, an R3 energetics supplier? Stage 11 resolves it by comparing the PE the market now pays with the PE the TO rung implies. This dossier states no number and no conclusion. If the TO state is already reflected, the re-rating engine is spent and only earnings growth remains.

B5. THE UGLINESS TEST
Classification: STRUCTURAL-FEATURE, provisional, with the competing reading named.
- Evidence for STRUCTURAL: the Explosives margin fell four quarters in a row, from 9.00% in Q4 FY25 to 4.64% in Q3 FY26, before the March 2026 plant start (errata, Verifier B F4). Pricing power reads weak (B04). Peers describe PSU bulk as thin or negative margin (B06). Cash conversion is weak: H1 FY27 CFO 638.39 over PAT 1,633.10 Rs lakh, 0.39x (B05). The emerging moat scan finds no category with a documented moat leg (em_score 4.1, band NONE, recomputed by Verifier C; B07).
- Evidence for ARTIFACT-OF-CLIMB: the FY26 headline margin drop is partly a base effect from the FY25 reversals (B03). Fixed charges and non-earning CWIP are build costs that end at commissioning (B04). Funding is visible: liquid pool 5,715.82 Rs lakh against commitments 3,996.21 (B03).
- Separating observation: the Explosives filing-basis margin at Q3 FY27 and Q4 FY27 once depreciation steps up, with CWIP plus advances at 31 Dec 2026 (B05).
- No trade call is made here.

B6. THE TRANSITION FALSIFIER (what kills the arrow)
- CWIP plus advances still below about Rs 150 Cr at 31 Dec 2026, the date restated to FY28, or cost above Rs 190 Cr or debt above Rs 135 Cr (B05 kill signal).
- No licence, offtake or booked revenue naming a customer by the first commissioning quarter; or an AR statement that ties TNT to own accessories only (B04, B07).
- At least two of Apollo, Premier and Solar report newly commissioned TNT, RDX or HMX capacity or an approved defence-grade DPR by the Q4 FY27 peer calls, which would close the scarcity window the plant depends on (B06 cross-peer hypothesis; read with Verifier B F11, since Apollo's TNT licence covers its industrial requirements).

### PART C: WHAT THE MODEL WATCHES

C1. DOMINANT VARIABLES (become the Role 5.5 tracker signals)
1. TNT spend and commissioning pace: CWIP 3,800.82 to 6,280.63 Rs lakh in H1 FY27; at least Rs 114.5 Cr remaining; five of five dated peer projects slipped one to three quarters (B05, B06).
2. TNT end use and customer: no customer, licence, capacity or offtake is filed; reading A and reading B both fit (B04, B07; Verifier B F3).
3. Explosives filing-basis segment margin and the ammonium nitrate to PSU price spread: 6.44% H1 FY27; materials 66.6% of revenue; Solar passes about 60% of cost rises through at once and the rest after a quarter (errata F2; B09; B06).
4. Cash conversion and bank funding: CFO over PAT 0.39x in H1 FY27; bank returns show inventory 19.2% to 30.3% of the reported return above books against a 10% test; undrawn long-term facilities nil (B05; B03; errata F5; B02).

C2. WHAT THE MODEL REJECTS
- Market size questions (TAM, SAM, headroom). SAM is a ceiling with only exports deducted, TAM sources diverge 2.0x, and the binding constraint is licence, capacity and execution, not market size (B09 alerts).
- Ratios built on spot FY26 numbers: spot ROCE of 19.95% (CWIP not earning), headline EBITDA growth of 7.7% (base holds 884.72 Rs lakh), and anything on FY26 EPS that includes 729.78 Rs lakh of non-repeating items (B04).
- Dividend payout of 0.52% as a signal (B04).
- Export hope: exports grew in line with revenue, 15.57% against 15.24% of revenue, markets unknown (B05, B07).
- Capex-embedded growth of 122% or 246%: unreliable, never a capacity basis (Verifier C, B12c C-E3).

C3. THE BUSINESS FALSIFIER (what forces a re-declaration of the FROM business)
A suspension or lapse of an Explosives Act licence at one of the 12 plants (validity dates NOT FOUND, B04; peers cite plant accidents and licence suspension, B06), or a lender cutting drawing power to the books after the stock-statement gap (B03 Note 13). Either would change what the starting business is: a licensed converter with bank-funded working capital. This is separate from B6, which kills only the arrow.

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

(Drafted at Halt 1 from B01 to B09 per the five-question spec in prompts/13-synthesis-pipeline.md. Stage 13 holds the final version.)

Keltech makes industrial explosives and perlite products at 12 plants (B04). Explosives are 86.0% of revenue and cover cartridge explosives, bulk emulsion, MMAN solution and accessories such as detonating fuse and cast boosters (B04, B03). Miners and quarries use them to break rock, and switching is hard because each product is fitted to the strata and licensed under the Explosives Act (B04). Perlite is 10.5% of revenue and serves filter aid, cryogenic insulation and horticulture uses; the run did not establish why a perlite customer cannot do without it (B04). The customers are public sector miners such as MOIL, mining contractors, and cement, quarry and road users, reached through channels the AR describes two conflicting ways (dealers on p.28, direct to consumers in Note 34; B04), and no customer holds 10% of revenue (B02 Note 28, B04, B09). Qualification cycles and contract terms are not disclosed, and the run did not establish them. Present demand comes from Coal India and Singareni overburden removal and coal output, and from cement, limestone quarry, metal ore and infrastructure output (B09 candidates). Peers say commercial explosives were flat in FY26 and strong in H1 FY27 at the leader, led by price (B06), and Keltech Explosives revenue rose 35.7% in H1 FY27 with volume not found (B05). Forward demand rests on mining and infrastructure growth: the research pages put market growth at 7.4% a year and the implied company growth at 9.5%, but both sources are thin (B09). Each driver can be checked against PESO licence status, ammonium nitrate duty actions, and Coal India monthly output, which are named B09 candidates. The TNT plant, exports and perlite for pharma are further growth claims, and none has a filed customer, licence or capacity (B04, B07). The explosives line has a moderate moat built on licence and plant footprint, with pricing power weak: EBITDA margin is 7.7% against Premier 10.2% and Solar 27.6% (B01). Gate 0 confirms two moats and recomputes the moat score at 11 of 60, class MODERATE, inside an AVERAGE total of 64 (B12c recomputation; stage stated 10 and 63). The emerging moat scan scores 4.1 and band NONE, and the Category 21 and 22 checks score 0 (B12c). The perlite line has no moat on the evidence, and its segment result swung from a loss of 286.25 to a profit of 290.42 Rs lakh without a stated cause (B03). The TNT slice is not a moat on today's evidence, because no filing names its product use or customer (B04, B07).

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. VERTICALS FRAMED

Vertical 1: TNT spend and commissioning pace
- Corpus establishes: CRISIL gives about Rs 190 Cr cost, Rs 135 Cr Canara Bank term loan to 30 Sep 2034, April 2027 start (B05 guidance). The AR notes name the project and its loan; commitments are 3,996.21 Rs lakh, TNT loan drawn 2,045.46 (B02). CWIP moved 3,800.82 to 6,280.63 Rs lakh; upper-bound spend with other non-current assets is 7,551.58 Rs lakh, 39.7% of Rs 190 Cr (B05). The Board's Report says "commissioned fully in 2027" (AR p.29; Verifier B F5 corrects B05's "no statement since Feb 2026").
- Cannot establish: the TNT versus Surjagarh silo split of CWIP, plant capacity, licence validity, a project schedule (B03, B07).
- Deciding questions: (1) What are CWIP plus advances at 31 Dec 2026? (2) Does the Q4 FY27 filing move CWIP into PPE? (3) Does the stated cost or loan change?

Vertical 2: TNT end use and customer
- Corpus establishes: no filing names a defence customer; the MD&A calls the Garamsur plant an "Accessories Project" (AR p.55, B04). CRISIL cites "established clientele" (CRISIL p.2). Apollo's TNT licence covers its industrial explosive requirements (APOLLO Q4FY26 p.11; Verifier B F3). No peer states a TNT price, offtake or customer (B06).
- Cannot establish: which reading holds, A (merchant or defence energetics) or B (own accessories input) (B04 analyst note).
- Deciding questions: (1) Does a Reg 30 filing or PESO licence name the product and capacity? (2) Does the first booked revenue sit outside the two segments? (3) Does the next AR Form B name the nitration technology licensor?

Vertical 3: Explosives margin and the input to PSU price spread
- Corpus establishes: Explosives margin on the filing basis fell from 9.00% in Q4 FY25 to 4.64% in Q3 FY26 and stood at 6.44% in H1 FY27 (errata F4, F2). AR basis is 6.67% FY26, 7.64% FY25, and the AR and filing bases differ by 464.31 Rs lakh in FY26 (B04, B05). Peers call Coal India and Singareni bulk L1 priced and thin (B06).
- Cannot establish: Keltech's pass-through lag and rise-and-fall terms beyond CRISIL's "Price escalation clause ... up to some extent" (CRISIL p.2; Verifier B F9), volume in MT for H1 FY27, the sub-mix of bulk, cartridge and accessories (B09).
- Deciding questions: (1) Is the Q3 FY27 margin at or above 6.5% with growth above 20%? (2) How much of H1 FY27 revenue growth is price, given Solar says 18 to 20% of its FY27 growth is price (B09)? (3) Where does the unexplained 464.31 Rs lakh sit?

Vertical 4: Cash conversion and bank funding
- Corpus establishes: FY26 CFO 4,850.02 Rs lakh against FY25 negative 1,757.03; H1 FY27 CFO 638.39 against PAT 1,633.10; free cash flow negative 1,934.84 for H1 (B03, B05). Bank returns show inventory 19.2% to 30.3% of the reported return above books; as a share of books that is 23.7% to 43.6% (errata F5). The auditor calls the gaps not material and reports an ICFR exception on financial closure (B02, B08). Outstanding liabilities are 2,695.09 Rs lakh, +75.6% (AR p.119, errata F6).
- Cannot establish: the share of capital creditors in trade payables (B05), bank sanction terms and stock audit reports (B03).
- Deciding questions: (1) Does FY27 CFO over EBITDA reach 0.6x or more? (2) Does the next AR Note 13 table show every quarterly gap at or below 10% of the return? (3) What sits inside outstanding liabilities?

### 4b. CANDIDATE SIGNAL TABLE (all UNVERIFIED; Role 5.5 verifies in claude.ai)

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| Coal India and Singareni overburden removal and coal output (B09) | Coal output falls two months running while Keltech reports volume growth, so growth is price or share, not demand | Monthly | Coal India monthly production release; Ministry of Coal |
| PESO licence validity, new licences and export approvals (B09, shared) | Any licence suspension or lapse at a Keltech plant, or no licence for the TNT unit by first commissioning | Event-Driven | PESO annual report and licence portal; DGFT |
| Ammonium nitrate price and anti-dumping or duty actions (B09, shared) | Input cost rises while Explosives filing-basis margin stays below the 6.44% H1 FY27 base | Event-Driven | DGTR notifications; Ministry of Finance; chemical price trackers |
| Cement, limestone quarry, metal ore and infrastructure output (B09) | IIP mining or cement index negative for two months while Keltech reports volume growth | Monthly | Ministry of Mines IBM mineral production; IIP mining and cement indices |
| Defence ammunition filling demand and any named TNT customer (B09) | No named customer or licence by the Q4 FY27 filing | Event-Driven | Ministry of Defence press releases; GeM and DPSU tenders; Keltech Reg 30 filings |
| MOIL and other PSU customer results and deduction notices (B09) | Over-6-month receivables above 441.11 Rs lakh or powder-factor deductions above 394.40 Rs lakh (B02, B04) | Quarterly | MOIL quarterly results and production releases |
| Peer commentary on domestic volume, price and TNT supply (B09; B06 hypothesis) | At least two of Apollo, Premier, Solar report commissioned TNT, RDX or HMX capacity and energetics prices soften | Quarterly | Peer earnings call transcripts on BSE and NSE |

Candidates carried: 7 (B09 downstream_candidates). Sources are the B09 likely_source entries; the Downstream_Source_Discovery_Protocol_v1_0 class check happens at Role 5.5.

### 4c. FRAGILITY READ

- variable_count: 6. (1) TNT cost and date; (2) TNT end use and customer; (3) ammonium nitrate spread and pass-through; (4) mining, quarry and infrastructure demand with PSU bulk terms; (5) cash conversion and bank drawing power; (6) clean completion of the promoter control transfer (B05, B08, B09).
- verifiability_ratio: 4 of 6 externally observable. Observable outside the company: (2) via licence, tender and counterparty filings; (3) via DGTR and peer calls; (4) via Coal India and IIP data; (6) via SAST and BSE filings. Company-narrated only: (1) since CRISIL repeats the company plan and the AR gives no cost; (5) since bank returns are not public (B03, B05).
- single_point_failure: TNT end use and customer. With no filed customer, licence or capacity, reading B alone (own-use accessories input) fails the tier claim without any other variable going wrong (B04, B07).
- fragility_verdict: FRAGILE (one kill-switch variable, and two of six variables company-narrated).

### 4d. RESEARCH BRIEF (the claude.ai work order)

1. PENDING LIVE VERIFICATION (Chain 1): Keltech's PESO licence and approvals for the TNT unit (CRISIL p.2: "necessary approvals in place"), and any Munitions India, DPSU or GeM TNT purchase notice. Names the end use and customer.
2. PENDING LIVE VERIFICATION (Chain 2): the ICRA Feb 2026 non-cooperation rationale (id=141111, fetch failed in B08), the Jul 2026 withdrawal notice, and any current CRISIL surveillance note. Names the lender view of drawing power.
3. Build Chain 3: ammonium nitrate spread and pass-through lag (DGTR status; Solar's 60% immediate escalation from B06).
4. Build Chain 4: Coal India and Singareni demand and payment behaviour against Keltech PSU receivables.
5. Build Chain 5: control transition (SAST completion disclosure, Reg 10(1)(a)(ii) exemption outcome, ED FEMA enquiry on the incoming controller; B08).
6. Fetch the filed BSE shareholding pattern for Sep 2026 and the first filed pledge figure (B00, B08).
7. Fix the date of the CESTAT order against the 24 to 25 Apr 2026 BSE price query and the 25 Apr reply (Verifier B F12; PENDING LIVE VERIFICATION).
8. Identify the Chowgule Global group company where the MD and Vice-Chairman took executive roles in April 2026 (AR p.58 note 2; Verifier B F2).
9. Read the Dolphin Investment Ltd ownership and the Apr 2025 Reg 30 inter-corporate loan filing (B08).
10. Check Apollo/IDL's TNT licence scope and the Premier Katepally commissioning status against peer dates (B06; Verifier B F3, F11).
11. Verify the TAM sources: Ken Research and Univest pages, plus PESO production data (B09 TAM_SOURCES_THIN).
12. Find the nitration technology licensor and any exclusivity (B07 optionality register).
13. Verify each B09 candidate source URL against the discovery protocol registry (B09).

Items 1 and 2 are the PENDING LIVE VERIFICATION links raised by the Section 4e chains. Items 3 to 5 are the chains still to be built.

### 4e. SECOND-ORDER STUB (Master v3.7 Rule F)

CHAIN 1: CRISIL states a Rs 190 Cr TNT plant, Rs 135 Cr term debt and an April 2027 start (CRISIL p.2, p.3; B05), while CWIP rose from 3,800.82 to 6,280.63 Rs lakh in H1 FY27 (B05)
Link 1 [VERIFIED, with derived arithmetic]: Upper-bound spend with other non-current assets is 7,551.58 Rs lakh, 39.7% of 19,000 Rs lakh, so at least 11,448.42 Rs lakh remains against H1 FY27 payments of 2,530.34 Rs lakh (B05). The AR Form B calls the technology "Nitration Based Accessories", not fully absorbed and "to be commissioned fully in 2027" (AR p.29; B07).
Link 2 [PENDING LIVE VERIFICATION]: Who pays for the output, and why now? No filing names a customer (B04, B07). Claude web opens Keltech's PESO licence and TNT approvals, and any Munitions India, DPSU or GeM TNT notice, as named in research brief item 1. No counterparty fact is written here.
Link 3 [INFERENCE]: If the plant serves Keltech's own accessories (reading B, B04), first benefit shows as a lower bought-in materials line and no new segment, and a lender sees only a cost-cutting build. If it serves outside customers (reading A), first benefit shows as a third segment. The two readings produce different first filings, so the Q4 FY27 segment note separates them. Five of five dated peer projects slipped one to three quarters (B06), which makes a restated date the default expectation to test.
Binding constraint: funding and pace. Undrawn long-term facilities are nil and the TNT loan drawn is 2,045.46 Rs lakh (B02). A liquid pool of 5,715.82 Rs lakh stands against commitments of 3,996.21 (B03), and the remaining spend is at least 11,448.42 (B05). Borrowing power up to Rs 400 Cr was approved at the AGM of 7 Aug 2026 (B05), an enabling limit, not a plan.
Unsaid: the MD&A calls the project an "Accessories Project" and states no cost, capacity or product (AR p.55; B04). Borrowing cost capitalised is 177.15 Rs lakh at a stated NIL rate (B02), so a cost shield ends when assets enter use. The CWIP split between TNT and the Surjagarh silo is NOT FOUND (B03).
Observation that confirms or breaks this chain, and confirm-by date: the Q3 FY27 results filing (quarter ended 31 Dec 2026, due by mid Feb 2027) shows CWIP plus advances of about Rs 150 Cr or more. A figure below about Rs 150 Cr breaks the April 2027 start (B05 kill line). Confirm-by: 2027-02-14.

CHAIN 2: H1 FY27 CFO was 638.39 Rs lakh against PAT 1,633.10, 0.39x, with payables days at 76.1 against 67.8 (B05)
Link 1 [VERIFIED]: Quarterly returns to the Canara consortium show inventory 19.2% to 30.3% of the reported return above books in all four FY26 quarters, against a stated 10% test. Measured on books the gaps are 23.7% to 43.6%. The Mar-26 return of 4,203.59 Rs lakh equals the Mar-25 balance sheet inventory (AR p.118; errata F5; B02). The auditor calls the gaps not material (B03 CARO ii(b)).
Link 2 [PENDING LIVE VERIFICATION]: Who pays, and why now? The lender decides how much working capital Keltech can draw while TNT spend continues. Claude web opens the ICRA Feb 2026 non-cooperation rationale and Jul 2026 withdrawal notice, and any current CRISIL surveillance note, as named in research brief item 2. No lender fact is written here.
Link 3 [INFERENCE]: Cash credit is about 94% drawn by inference from matching sums, and undrawn long-term facilities are nil (B02). H1 FY27 Explosives revenue growth of 35.7% (B05) then consumes working capital, so a lender that re-bases drawing power from returns to books would set a hard cap on TNT spend pace and on volume growth together.
Binding constraint: drawing power and remaining TNT spend share one credit pool. Free cash flow was negative 1,934.84 Rs lakh in H1 FY27 (B05).
Unsaid: Note 13(e) says statements submitted match the books, while the Note 13 table beside it shows otherwise (AR p.118). Outstanding liabilities are 2,695.09 Rs lakh, up 75.6%, and are not itemised (AR p.119; errata F6; B02). The share of capital creditors in trade payables is NOT FOUND (B05). The CFO headline includes bank deposit movements (+961.95 Rs lakh in FY26; Verifier B F15).
Observation that confirms or breaks this chain, and confirm-by date: the audited FY27 cash flow statement in the Q4 FY27 results shows FY27 CFO over EBITDA of 0.6x or more (B04 red flag line is below 0.6x two years running). A ratio below 0.6x breaks the chain. Confirm-by: 2027-05-30.

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in claude.ai with live web, before Role 2.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. Keltech Energies makes industrial explosives and perlite products at 12 plants (B04).
2. Explosives bring in 86.0% of revenue, and perlite brings 10.5% (B04).
3. The company files standalone accounts, holds no earnings calls and issues no investor presentations (B00).
4. Public sector miners, mining contractors, and cement, quarry and road users purchase the explosives, and no customer is above 10% of revenue (B02, B04).
5. Exports are 15.6% of revenue, and the markets and margins are not disclosed (B00, B03).
6. Demand follows coal, mining, cement and infrastructure output, which the pipeline can track from public sources (B09).
7. Peers say commercial explosives were flat in FY26 and strong in H1 FY27, and that price drove much of it (B06).
8. Keltech's Explosives revenue rose 35.7% in H1 FY27, but the volume in tonnes is not in any filing (B05).
9. The moat is a licence and a plant footprint. It is moderate, and pricing power is weak (B04, B01).
10. Perlite shows no moat, and the TNT plant is not a moat yet because no filing names a use or a customer (B03, B07).
11. The draft mental model: a licensed converter at the second rung that may climb one rung to a spec'd energetics supplier if the Garamsur TNT plant finds a customer. Reading B says the plant only feeds Keltech's own accessories, and then there is no climb (B04, B07).
12. The fragility read is FRAGILE. Six variables must go right, two are known only from the company, and the TNT end use alone can break the climb (B04, B05, B09).
13. The corpus could not establish the TNT product, capacity, licence or customer, the filed promoter pledge, export markets, or H1 FY27 volumes (B00, B04, B08).
14. The biggest open question is whether CWIP plus advances reach about Rs 150 Cr by 31 Dec 2026 against a stated Rs 190 Cr project (B05).
15. The second open question is whether the family settlement completes cleanly and whether bank stock statements that run above the books hold up in lender review (B08, B03).

---

## SECTION 6: STANDING EXTRACTION ANNEX

Units: AR FY2025-26 and the results filings are in Rs lakh; CRISIL and screener are in Rs Cr. PDF page numbers equal the page-marked text twin.

### 1. UNITS

Printed volumes, one product each, from AR_FY2025-26.pdf p.28:
> "The sale of Explosives for the year under review was 63,154 MT as against 58,280 MT for the corresponding period the previous year."
> "The sale pf Perlite and Perlite based products for the year under review was 18741 MT as against 18704 MT for the corresponding period of the previous year."

Comment: No per-unit price or realisation is printed. Explosives revenue per MT is derived from the segment line (AR p.137 external revenue 45,766.62 Rs lakh FY26; 40,954.46 FY25) over the volumes above: B04 gives 72,470 rupees per MT FY26 and 70,274 FY25. The Explosives segment mixes cartridge, bulk, MMAN and accessories and services, so this is a mix indicator for a basket, not a price (B04). The Perlite per-MT figure is derivable from external revenue 5,584.15 Rs lakh over 18,741 MT; none is printed. The FY25 Perlite volume is printed as 24,584 MT in AR_FY2024-25.pdf p.30 ("The sale of Perlite and Perlite based products for the year under review was 24,584 MT as against 18,039 MT") and as 18,704 MT in AR_FY2025-26.pdf p.28, with no restatement note (Verifier B F1).

### 2. SEGMENT CAPITAL AND DEBT

Printed in AR_FY2025-26.pdf p.137 (Note 28) and 2026-11-14_Q2FY27_board-outcome-and-results.pdf p.6 (read from the page image), Rs lakh:

| Item | 30.09.2026 | 30.09.2025 | 31.03.2026 (audited) | 31.03.2025 (AR p.137) |
|---|---|---|---|---|
| Segment assets, Explosives | 28,843.25 | 19,371.37 | 24,979.59 | 16,660.31 |
| Segment assets, Perlite | 2,850.05 | 2,626.55 | 2,590.68 | 3,009.14 |
| Unallocated assets | 9,397.79 | 9,314.38 | 7,963.48 | 9,059.34 |
| Total assets | 41,091.09 | 31,312.30 | 35,533.75 | 28,728.79 |
| Segment liabilities, Explosives | 17,322.75 | 11,369.06 | 12,919.60 | 9,988.46 |
| Segment liabilities, Perlite | 234.92 | 307.38 | 298.49 | 880.66 |
| Unallocated liabilities | 6,768.72 | 5,772.87 | 7,021.00 | 5,398.69 |
| Total liabilities | 24,326.39 | 17,449.31 | 20,239.09 | 16,267.81 |
| Capital employed, Explosives | 11,520.50 | 8,002.31 | 12,059.99 | n/a in AR note |
| Capital employed, Perlite | 2,615.13 | 2,319.17 | 2,292.19 | n/a in AR note |
| Capital employed, unallocated | 2,629.07 | 3,541.51 | 942.48 | n/a in AR note |
| Total capital employed | 16,764.70 | 13,862.99 | 15,294.66 | n/a in AR note |

Capital expenditure printed in AR p.137: Explosives 5,531.47 and unallocated 21.76 (FY26); 373.81 and 32.99 (FY25).
Borrowings: not shown by segment. AR p.138 reconciles segment liabilities to the balance sheet with "Borrowings 2,333.28 2,429.35" as a reconciling line. Total debt is 7,168.95 Rs lakh (B03; Note 27 p.136). The remainder is not tagged to a segment in the printed table.
Comment: Explosives capital employed rose from 8,002.31 to 11,520.50 Rs lakh year on year at Sep 2026, the build visible at segment level; the figure sits below the Mar 2026 audited 12,059.99. Verifier A corrected the Q2 FY27 segment result and revenue lines (errata F2); those are not repeated in this table.

### 3. GUIDANCE VERSUS ASPIRATION

| # | Quote | Source | Class |
|---|---|---|---|
| 1 | "the plant is expected to commence operations in April 2027" | CRISIL_2026-02-13_rationale.pdf p.2 | (a) guidance with a period; stated by the rating agency, not the company |
| 2 | "setting up a TNT (Trinitrotoluene) plant at a cost of ~Rs 190 crore ... funded through term debt of Rs 135 crore" | CRISIL p.2 (Rs Cr) | (c) capacity or capability only; cost and funding, no output stated |
| 3 | "Not yet fully absorbed as the same is under implementation and to be commissioned fully in 2027." | AR_FY2025-26.pdf p.29 | (a) guidance with a period, year only |
| 4 | "New plant commissioned in March 2026 is expected to stabilise." | AR p.55 | (b) aspiration without a period |
| 5 | "During the Financial Year 2025-26, your Company's focus is majorly into exports." | AR p.55 | (b) aspiration; carried forward from the FY25 AR (Verifier B F7) |
| 6 | "Perlite Filter-Aid diversification into new areas of market is underway by focusing more in to the phama sector to get higher volumes." | AR p.55 | (b) aspiration |
| 7 | "The explosives industry is expected to grow with emphasis on infrastructure growth and mining by the Govt." | AR p.55 | (b) aspiration |
| 8 | "Annual cash accrual is expected at Rs 32-38 crore" | CRISIL p.2 | (a) medium term, rating agency expectation |
| 9 | "expected to reach ~Rs 145 crore as on March 31, 2026" (net worth) | CRISIL p.1 | (a) rating agency expectation |
| 10 | "the total amount of such borrowings outstanding at any point of time shall not exceed Rs. 400 Crores" | AR p.9 (Notice item 8) | (c) capability only, an enabling limit |

Comment: no revenue, margin, order book or return number is stated by management in any filing (B05: NOT FOUND). Two of the ten items carry a period that the company itself stated.

### 4. CONCENTRATION

> "Customers amounting to 10% or more of Company's revenue is NIL" (AR p.138)
> Revenue from external customers by geography: "Domestic 43,066.55 ... Exports 8,284.21 ... Total 51,350.76" and FY25 "38,832.53 ... 7,460.87 ... 46,293.40" (AR p.138, Rs lakh; the table is headed as non-current assets in the printed note, a mislabel noted by Verifier B)

Comment: Product share is Explosives 45,766.62 of 53,206.01 Rs lakh total revenue, 86.0% (AR p.137; B04). Top customer share: below 10%, name not disclosed. Share of PSU customers, bulk versus cartridge versus accessories mix, export markets and export products: NOT DISCLOSED in any held filing (B04, B09).

### 5. PROMISE LEDGER

| Promise (as made) | Date made | Delivery status | Evidence anchor |
|---|---|---|---|
| TNT plant about Rs 190 Cr, Rs 135 Cr debt, operations April 2027 | 2026-02-13 (CRISIL) | PENDING, counted partial | CWIP 3,800.82 to 6,280.63 Rs lakh (AR p.106; Q2 FY27 p.7; B05) |
| "New plant commissioned in March 2026 is expected to stabilise" | AR FY2025-26, Board approved 2026-05-27 | PARTIAL | Explosives revenue +34.8% Q1 and +36.9% Q2 FY27; filing-basis segment margin 6.44% H1 FY27 against 6.70% H1 FY26 (Q2 FY27 p.6; errata F2); volumes NOT FOUND |
| "focus is majorly into exports" | AR FY2025-26 | PARTIAL | Exports +11.0% (notes) against +7% (Board's Report); share 15.57% against 15.24% (AR pp.28, 138; B05) |
| Perlite filter aid into pharma for higher volumes | AR FY2025-26 | PARTIAL | H1 Perlite result 91.52 against 0.62 Rs lakh; FY26 volume +0.2% on a FY25 base stated two ways (Q2 FY27 p.6; AR p.28; Verifier B F1) |
| Industry to grow on mining and infrastructure | AR FY2025-26 | DELIVERED (company level only) | Explosives revenue H1 FY27 +35.7% (B05) |
| Net worth about Rs 145 Cr at Mar 2026 | 2026-02-13 (CRISIL) | DELIVERED | 15,294.66 Rs lakh, Rs 152.95 Cr (Q2 FY27 p.6; B05) |
| Cash accrual Rs 32 to 38 Cr a year | 2026-02-13 (CRISIL) | DELIVERED | FY26 Rs 36.3 Cr, Rs 33.1 Cr without the non-cash exceptional (B05, derived) |
| Dividend Rs 1.50 per share | 2026-05-27 (Q4 FY26 note 5) | DELIVERED | 15.00 Rs lakh paid in H1 FY27 cash flow (B05) |
| Family settlement under execution, holdings may change | AR FY2025-26 pp.77 to 78 (MOFS dated 2021-01-11) | PARTIAL | LOI 2026-10-28; Board approval 2026-11-14; transfer not effected (B05) |
| CESTAT refund 317.76 Rs lakh recognised, application being filed | 2026-05-27 (Q4 FY26 note 3) | PENDING, counted partial | No inflow in H1 FY27 (B05) |

Comment: 4 delivered, 6 partial, 0 missed; credibility grade C holds (B05; Verifier B concurs). Rows 3 and 5 lean on carried-forward text (Verifier B F7).

### 6. RESTATED BASES

No note on restatement, regrouping or reclassification of comparatives was found. A pattern search of the three results filings returned no match for "regrouped", "reclassified", "restated" or "comparative"; AR matches are Ind AS policy text only (text twin lines 4276 to 6806; B02 restatements_found: empty).
Two comparatives differ across documents with no note:
> FY25 Perlite volume: 18,704 MT (AR_FY2025-26.pdf p.28) against 24,584 MT (AR_FY2024-25.pdf p.30).
> Explosives segment result for FY26: "3,051.85" (AR_FY2025-26.pdf p.137, Note 28) against "2587.54" in the audited year column of 2026-11-14_Q2FY27_board-outcome-and-results.pdf p.6; FY25: 3,129.40 (AR) against 2,967.22 (Q4 FY26 filing, B05).
Comment: the AR allocates part of un-allocable income into the Explosives segment (464.31 Rs lakh FY26, 162.18 FY25; B05). Quarterly margin work uses the filing basis. Comparative as printed in the latest filing: 30.09.2025 half-year Explosives segment result "1497.86" on revenue "22,342.17" Rs lakh (Q2 FY27 p.6).

### 7. CORPORATE-ACTION CLAUSES

Only one scheme-type item is in the corpus: the inter-se promoter share transfer under the Memorandum of Family Settlement. File: 2026-10-28_promoter-inter-se-share-transfer.pdf.
> "Total No. of Shares proposed to be transferred 4,09,940 equity shares of Rs. 10/- each fully paid up" (p.4)
> "Consideration Pursuant to implementation of the MOFS (Family Settlement) without cash consideration" (p.4)
> "Date of LOI October 28, 2026"; transferor Chowgule and Company Private Limited (Promoter Group); transferee "Mr. Vijay Vishwasrao Chowgule" (p.4)
> "the aggregate shareholding of the Promoter and Promoter Group in the Company shall remain unchanged before and after the proposed transfer." (p.4)
> "intended to fall within the exemption provided under Regulation 10(1)(a)(ii) of the SEBI (Substantial Acquisition of Shares and Takeovers) Regulations, 2011 subject to fulfilment of the prescribed conditions." (p.5)
Comment: no ratio is printed; no undertaking is defined; no liability allocation clause appears; no appointed or effective date is printed beyond the LOI date, and the transfer is "off-market" by depository instruction (p.4). The Board approved the transfer on 2026-11-14 (B05). Background: MOFS dated 2021-01-11, "under execution for implementation with the guidance of Arbitral Tribunal consisting of Retired Judges" (AR p.77). Not in the corpus: the MOFS itself and the SEBI or exchange response to the LOI; fetch the BSE Reg 30 and SAST filings. No merger, demerger, preferential issue or share repurchase appears: AR p.28 states "The Company has not bought back any of its securities". The borrowing limit of Rs 400 Cr (AR p.9) is a special resolution, not a scheme.

### 8. RELATED-PARTY PERIMETER

AR_FY2025-26.pdf p.140 (Note 29), Rs lakh, transactions FY26 / FY25, balance at year end FY26 / FY25:

| Entity | Nature | FY26 | FY25 | Balance FY26 | Balance FY25 |
|---|---|---|---|---|---|
| Chowgule & Company Pvt Ltd (major shareholder) | Services rendered | nil | nil | 84.51 | 84.51 |
| Chowgule Brothers Pvt Ltd | Services received (warehousing and marketing, AOC-2 p.35) | 75.90 | 47.27 | 3.59 | 7.25 |
| Chowgule ABP Coatings Pvt Ltd | Services received (epoxy purchase, AOC-2 p.36) | 66.18 | 90.00 | 23.90 | 90.00 |
| Chowgule Industries Pvt Ltd | Purchase of vehicle | 21.82 | 0.29 | nil | nil |
| Chowgule Lavgan Shiprepair Pvt Ltd | Services received ("Maintenance of Mechanical / Civil works", AOC-2 p.36) | 100.00 | 100.00 | 116.00 | 116.00 |
| Chowgule Construction Chemicals Pvt Ltd | Services received | nil | 11.88 | nil | nil |
| Santosh Chowgule HUF | Rent paid | nil | 0.93 | nil | nil |
| Dharini Educational Foundation; Kolhapur Oxygen and Acetylene Pvt Ltd | CSR expense; vehicle purchase | nil | nil | nil | nil |
| Kaushalya Chowgule (relative of KMP) | Remuneration | 16.82 | 14.89 | nil | nil |
| Dr. Rohini V Chowgule (relative) | Sale of goods | 0.22 | nil | nil | nil |

Key managerial personnel compensation: "Total compensation 459.00 459.93" Rs lakh (p.139). Sitting fees are paid to six directors (p.140).
Comment: AOC-2 states arm's-length basis (p.35; B03 corrected B02). The Rs 84.51 lakh balance is more than 1,095 days old and 20% provided (B02, Note 26 p.135). Dolphin Investment Ltd (9.36% promoter group) does not appear in the Note 29 list (AR p.139; B03). Contract and pricing basis for Lavgan is NOT DISCLOSED.

### 9. PLEDGE AND SHAREHOLDING

Source: KELTECH_shareholding_screener_2026-09.csv (screener.in capture, 2026-11-15). Header printed: "BSE SHP page blocked (Akamai Access Denied). Pledge data NOT in this capture."

| Quarter | Promoters | DIIs | Public |
|---|---|---|---|
| Dec 2023 | 54.33% | 0.14% | 45.53% |
| Mar 2024 | 54.33% | 0.14% | 45.53% |
| Jun 2024 | 54.33% | 0.14% | 45.52% |
| Sep 2024 | 54.33% | 0.14% | 45.53% |
| Dec 2024 | 54.33% | 0.14% | 45.53% |
| Mar 2025 | 54.33% | 0.14% | 45.54% |
| Jun 2025 | 54.33% | 0.14% | 45.53% |
| Sep 2025 | 54.33% | 0.14% | 45.53% |
| Dec 2025 | 54.33% | 0.14% | 45.54% |
| Mar 2026 | 54.33% | 0.14% | 45.52% |
| Jun 2026 | 54.33% | 0.16% | 45.51% |
| Sep 2026 | 54.33% | 1.26% | 44.41% |

Promoter pledge for 12 quarters as filed: NOT DISCLOSED in the corpus. The filed BSE pattern is a corpus gap, and the screener capture carries no pledge row (B00, B08). Nil on aggregators is media tier only (B08). FII holding: NOT DISCLOSED (no FII line in the capture). Institutional holding latest: DIIs 1.26% at Sep 2026; holder not named (B08).
Promoter holders, AR_FY2025-26.pdf p.77 and Note 11: Chowgule & Company Pvt Ltd 4,09,940 shares 40.99%; Dolphin Investment Limited 93,601 shares 9.36%; Vijay Vishwasrao Chowgule 39,722 shares 3.97%; Ashok Vishwasrao Chowgule 20 shares 0.00%; total 5,43,283 shares 54.33% (paid-up capital 10,00,000 shares, AR p.28).
Comment: the promoter total has been flat at 54.33% since Mar 2023. The pending transfer moves 40.99% within the group and leaves the total unchanged (LOI p.4).

### 10. VERIFICATION

Documents quoted or cited in this annex, with filename and document date:
- AR_FY2025-26.pdf (cover letter 2026-07-13; Board approval 2026-05-27), inputs/annual-report/
- AR_FY2024-25.pdf (cover letter 2025-07-18), inputs/other/
- 2026-11-14_Q2FY27_board-outcome-and-results.pdf (2026-11-14), inputs/results/
- 2026-05-27_Q4FY26_audited-results.pdf (2026-05-27), via B05 and errata only
- CRISIL_2026-02-13_rationale.pdf (2026-02-13), inputs/rating/
- 2026-10-28_promoter-inter-se-share-transfer.pdf (2026-10-28), inputs/announcements/
- KELTECH_shareholding_screener_2026-09.csv (captured 2026-11-15), inputs/shareholding/
Comment: every figure not quoted from these files carries a block cite in Sections 1 to 5. Page-image reading was used for Q2 FY27 p.6 only.

CORPUS COMMIT HASH: 98d54e13ca6ec240b399e844fad635d5e591dff8
