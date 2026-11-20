# HALT 1 UNDERSTANDING DOSSIER: Ramkrishna Forgings Ltd (RKFORGE), run 2026-11-12

Stage 09b, model claude-sonnet-5-5. Assembly from committed blocks B00 to B09 and verifier blocks B12a to B12d. This file holds no valuation, no price and no verdict language. The Mental Model Declaration in Section 2 is a DRAFT.

Binding verifier corrections applied in this file:
- B12b B-01: the reading that bill discounting sits outside gross debt, and the Rs 173 Cr add-back in B05 and B06, are not carried. The net-debt basis is quoted as management said it (net of cash and bill discounting).
- B12b B-04: the Rs 8,000 Cr FY29 revenue figure is treated as withdrawn on the Oct 2026 call.
- B12a finding 4: the 14 June 2025 fact-finding report date and the 22,052.43 and 5,022.26 INR lakh inventory figures anchor to AR26 p.15, not p.8.

Page convention: PDF page (the "[page N]" marker in the .txt beside each PDF). Units: results filings and annual reports in INR lakh, India Ratings in INR million, screener in INR Cr, as stated in each cite (B00.reporting_units).

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

### 1.1 Concalls (B00.concall_quarter_map)
| File | Quarter | Call date |
|---|---|---|
| inputs/concalls/Concall_Feb_2026_Transcript.pdf | Q3 FY26 | 27 Jan 2026 |
| inputs/concalls/Concall_May_2026_Transcript.pdf | Q4 FY26 | 4 May 2026 |
| inputs/concalls/Concall_Jul_2026_Transcript.pdf | Q1 FY27 | 24 Jul 2026 |
| inputs/concalls/Concall_Nov_2026_Transcript.pdf | Q2 FY27 | 30 Oct 2026 (file name says Nov; date inside the call is 30 Oct, B05) |

Most recent quarter covered: Q2 FY27 (quarter ended 30 Sep 2026). Run date is 12 Nov 2026. The next quarter (Q3 FY27, Dec 2026) has not reported yet. The Q3 FY26 call was held on 27 Jan 2026 (B00), so no newer transcript is plausibly missing. One older call is absent: the Q2 FY26 call (Oct or Nov 2025) (B05 input_gaps). Twelve peer transcripts are held: Bharat Forge 4, M M Forgings 4, Happy Forgings 4 (B00.inventory).

### 1.2 Annual reports
Annual_Report_2026.pdf (FY2025-26, primary) and Annual_Report_2025.pdf (FY2024-25) are held (B00). The latest completed FY (FY26) is present. Two years are held, so the "at least 3 years" test is not met. No FY2023-24 annual report is held.

### 1.3 Results filings
- Results_Q2_FY27_Sep_2026.pdf (quarter ended 30 Sep 2026; board outcome 30 Oct 2026 in announcements).
- Results_Q1_FY27_Jun_2026.pdf (quarter ended 30 Jun 2026; board outcome 24 Jul 2026 in announcements).
- Results_Q4_FY26_Mar_2026_BoardOutcome_01May2026.pdf (audited FY26; OCR scan, digits unreliable, B00.input_gaps).
- Q3 FY26 results are held only as a board outcome in announcements (27 Jan 2026).
Quarter gap between the latest results filing and the latest AR: none. The AR covers to 31 Mar 2026. Two later quarters are held.

### 1.4 Investor presentation
Investor_Presentation_1.pdf, Q2 and H1 FY27, 25 pages (B04 input_gaps). The blocks do not state a document date.

### 1.5 Research and rating
- Rating: IndiaRatings_Rationale_22_Jun_2026.pdf (full rationale, B00).
- CRISIL: only the intimation of 20 Dec 2025 is held (announcements/2025_12_CRISIL-Credit-Rating-20-Dec-2025.pdf). The full CRISIL rationale is not held (B00).
- Broker or research notes: ABSENT (research/ is empty).

### 1.6 Corporate actions
23 hand-fetched exchange filings, 30 May 2025 to 30 Oct 2026 (outputs/inputs-file-list.txt). They are a selection from ramkrishnaforgings.com, not the complete BSE feed (B00.input_gaps). They cover board outcomes, the warrant issues, the promoter reclassification, the NCLT amalgamation order, capacity additions, the rating intimation, the monitoring agency report and the statement of deviation.

### 1.7 Freshness pair check (B00.freshness_verdict: FRESHNESS PAIRS OK)
| Pair | Trigger held | Mate | Status |
|---|---|---|---|
| Newest results to same-quarter concall | Results_Q2_FY27_Sep_2026.pdf | Q2 FY27 concall (30 Oct 2026) | PASS |
| Rating bulletin to full rationale | India Ratings 22 Jun 2026 | full rationale held | PASS |
| SEBI order to order text | none identified at stage 0 | n/a | PASS |
| AR to latest audited annual results | FY26 audited results (1 May 2026 board outcome) | AR FY2025-26 | PASS |

No pair failed. Two SEBI settlement orders appear in B08 (company order of March 2024; Riddhi Portfolio order of 2018). Their texts are not held. B00 did not treat them as a trigger. They are listed under the gaps below.

Other stated gaps: shareholding is .txt only (NSE summary and two XBRL files, 19 and 30 Sep 2026); screener holds only Data_Sheet.csv (Profit and Loss, Quarters, Balance Sheet, Cash Flow sheets exported empty); prospectus/ is empty and not expected (listed 2004). Empty folders, repeated here because the /step1 default suppressed the question: research/ (empty), prospectus/ (empty, not expected).

### 1.8 Verdict line
**CORPUS GAPPED**: freshness pairs pass, but the documents below are missing. "Findable-missing" means the operator can fetch it. "Plausibly-nonexistent" means the company publishes no such document.

| Missing document | Expected source | Kind |
|---|---|---|
| CRISIL full rating rationale (Dec 2025 and the June 2025 watch outcome) | rating agency site (CRISIL) | findable-missing |
| Complete BSE announcement feed (23 held are a selection) | BSE | findable-missing |
| Screener Profit and Loss, Quarters, Balance Sheet, Cash Flow sheets (company and three peers) | screener.in re-export with cached values | findable-missing |
| Q2 FY26 concall transcript (Oct or Nov 2025) | company IR page / BSE | findable-missing |
| Clean Q4 FY26 results PDF (held copy is an OCR scan) | company IR page | findable-missing |
| Shareholding patterns and XBRL before 30 Jun 2026 (pledge history; B08) | NSE / BSE | findable-missing |
| SEBI settlement order texts (company, 19 Mar 2024; Riddhi Portfolio, 2018) | sebi.gov.in | findable-missing |
| M M Forgings and Happy Forgings Q2 FY27 calls (B06) | company IR pages | findable-missing |
| Broker or research notes (research/ empty) | none company-published | plausibly-nonexistent as a company document; not collected |
| Prospectus | none (listed 2004) | plausibly-nonexistent |

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT - PENDING OPERATOR SIGN-OFF.** Nothing here is signed. Signing happens only in claude.ai after live-web stress-testing.

### PART A: THE FROM STATE

**A1. Archetype (per line)**
- Core auto and industrial forgings, machining, castings and aluminium forgings: **Build-to-spec component maker** (customer capex cycle, design-win pipeline, content per unit, input-cost pass-through). Basis: parts made to customer drawings, steel passes through with a lag (B04).
- Rail wheel joint venture (RTRWL, 51%, equity method): **Licence/scarcity business** (licence or quota validity, renewal risk, capacity cap). Basis: B07 category R1 and AR26 p.43 on RDSO certification. The plant is not in commercial production (B03, B05). This line has no revenue yet.

**A2. The simple analogy.** Think of a heavy workshop that turns steel bars into shaped parts for trucks, tractors and railway wagons. A truck maker hands over a drawing. The workshop heats the steel, presses it, and machines it to size. The truck maker then tests the part and keeps the workshop as a supplier for years (customer retention above 10 years, B04). The workshop does not own the steel price, because the steel cost passes on to the customer with a lag of up to three months (B04). It earns on the work it adds. Its profit rises when the presses stay busy, because the fixed cost spreads over more tonnes (B04). It pays its bills early with bank help and gets paid late, so it carries a large working-capital load (B03, B04).

### PART B: THE TRANSITION

**B1. FROM to TO (QUALITY LADDER).**
- Core forgings: FROM **R2 (cost-advantaged converter)**, sitting at the lower edge. ROCE ran below the durable mid-teens band: year-end FY26 ROCE 5.1% and median 9.5% on the B01 basis (B01). Verifier C records that the median is at least 10.2% on the formula as written (B12c G07). TO **R3 (value-added / spec'd supplier)**, the rung with ROCE of 20 to 25% and stickiness. Management states 12 to 15% ROCE by end FY27 and 20% in FY28, the second as an "aspiration" (B05). That is one rung, which fits the one-rung-per-2-3-years base rate. The run did not establish that spec-in stickiness is strong enough for R3: the emerging moat scan scored qualification lock-in as weak and the total as 9.0, class NONE (B07).
- Rail wheel JV: FROM none (pre-revenue). TO not stated by any block. It **fits no rung** until the first accepted wheel and the first invoice (B07 optionality register). This is a finding, not a gap to paper over.

**B2. The engine (mechanism).**
1. Fixed cost spreads over more tonnes. FY24 to FY26 capex of Rs 2,490.70 Cr (B01) added capacity to 3,95,800 tonnes installed; total utilisation was 72% in Q2 FY27 (B04, from IP slide 10). Incremental EBITDA margin was 26.8% in Q2 and 29.2% in H1 YoY against about 18% on average (B04, computed). EBITDA per tonne rose to Rs 0.40 lakh in Q2 FY27 from Rs 0.28 lakh in Q2 FY26 (B04). B04 records that the margin gain sits at the spread level (mix or pricing) and is not yet proven to be fixed-cost absorption.
2. Debt falls as capex ends and working capital eases. Management states a Rs 500 Cr debt cut in FY27 and a net debt of Rs 1,500 Cr by March 2027 (B05). H1 FY27 delivered Rs 126 Cr (B05). This lowers the interest load that holds today's optics down.

**B3. The proof gate (FTTCP tests this).** The gate fires only when all legs hold:
- Leg 1, earnings: consolidated quarterly revenue stays above Rs 1,405 Cr (the Q2 FY27 level) and EBITDA margin ex other income stays at or above 18.23% (the Q2 FY27 level), in both the Q3 FY27 and Q4 FY27 filings (B05 trigger 1; promise row 6).
- Leg 2, balance sheet: net debt on management's stated basis (net of cash and bill discounting) below Rs 1,700 Cr at 31 Dec 2026 and at or below Rs 1,500 Cr at 31 Mar 2027, with acceptances plus receivables sold flat or down from 1,04,994.72 INR lakh (B05, B07, B03).
- Leg 3, return: ROCE of 12 to 15% for FY27 on management's basis. The basis is NOT FOUND (B02 analyst note: filed notes-based ROCE is 6.27% on a different basis). FTTCP needs the definition before it can test this leg.
Until the gate fires, the transition is narrative and the name is research, not a trade.

**B4. The recognition gap (to be resolved at Stage 11).** Open question: does the TO state (R3 returns on the enlarged capacity) already look reflected in how the market prices the company today? This file does not conclude. Stage 11 resolves it through the PE gap. If the TO state is already reflected, the re-rating engine is spent and only earnings growth remains.

**B5. The ugliness test.** Today's ugly optic: ROCE 5.1% year-end, net debt to EBITDA 3.65x and interest cover 1.38x for FY26 (the Gate 0 deal-breaker 6 inputs, B01), negative free cash flow in FY25 and FY26 (B01), and a Rs 220.5 Cr inventory restatement scar (B01, B08).
Classification: **ARTIFACT-OF-CLIMB**, provisional, with the split stated.
- Evidence for artifact: Rs 2,490.70 Cr of capex not yet in earnings (B01); quarterly operating profit up from Rs 117.70 Cr to Rs 255.55 Cr; interest cover over the twelve months to Sep 2026 of 2.04x (B01); incremental margin 26.8% (B04).
- Evidence against, and the reading it supports: cash conversion is financed. About Rs 154 Cr of the standalone FY26 operating cash gain came from more acceptances and receivables sold (B03: 12,415.23 + 3,015.13 INR lakh); over-6-month receivables rose to 21.7% from 8.0% (B02); stock statements to banks differed from the books in all four quarters (B03). If those persist, the optic is a structural feature of a financed business.
- The one observation that separates the two readings: acceptances plus receivables sold, and over-6-month receivables, in the Q3 and Q4 FY27 filings. Falling with revenue rising supports ARTIFACT. Rising with revenue supports STRUCTURAL.

**B6. The transition falsifier (kills the arrow).** Any of these (B05 kill signals; B07):
- Revenue flat QoQ for two quarters, or margin stalls near 18%.
- The H1 FY27 pace (Rs 126 Cr) repeats in H2, or net debt is not below Rs 1,700 Cr at Dec 2026.
- A further capex raise beyond about Rs 550 Cr (the guide has already moved from Rs 350 Cr; B05).
- Receivables and inventory keep rising faster than revenue (B04: H1 FY27 receivables 795 to 1,025 Cr; inventory 1,246 to 1,469 Cr).

### PART C: WHAT THE MODEL WATCHES

**C1. Dominant variables (become Role 5.5 tracker signals).**
1. **Utilisation and EBITDA per tonne on the FY26 capacity.** Now: total utilisation 72%, EBITDA Rs 0.40 lakh per tonne in Q2 FY27 (B04).
2. **Export recovery, North America share.** Now: Q2 FY27 exports Rs 424.52 Cr against Rs 277.97 Cr; North America 71% of Q2 exports and 58% of FY26 exports (B04).
3. **Net debt and the bank-funded working-capital channels.** Now: H1 cut Rs 126 Cr of Rs 500 Cr (B05); acceptances plus receivables sold 1,04,994.72 INR lakh, 59.3% of standalone borrowings (B03); India Ratings adjusted leverage 4.6x (B04).
4. **Domestic commercial vehicle cycle and Tata Motors concentration.** Now: Tata Motors 33.4% of consolidated revenue in 9M FY26; two customers above 10% (B04, B03); domestic auto 47.0% of standalone FY26 revenue (B04).

**C2. What the model rejects (noise).**
- Market size questions. The run found the forging market large enough (runway class GOOD, B09). The binding constraint is capacity fill, cash and execution, not market size (B09 capacity_check).
- Optionality with no orders: aerospace (zero order book, B05), passenger vehicle and EV at 10% of revenue (date has slipped, B05), semiconductor and robotics forgings (B05). They sit in the optionality register (B07), not in the proof gate.
- The Rs 8,000 Cr FY29 revenue figure. Treated as withdrawn on the Oct call (B12b B-04). It needs 92.7% of installed capacity at today's realisation per tonne (B09).
- Rail wheel revenue as a driver of the transition. The JV is credited once, under the optionality register (B07 analyst note).

**C3. The business falsifier (kills the starting business).** Evidence that the FROM business is a commodity price-taker and not a spec-in component maker: EBITDA per tonne back below Rs 0.30 lakh (B04 red flag; Q2 FY26 was 0.28) while total utilisation is above 70%, together with steel and energy cost not passing through to customers (the Q2 FY27 shipping cost of Rs 8 to 9 Cr was borne, B05) and Tata Motors share of revenue rising without new customers. That pattern would re-declare the line as a Commodity converter, where Section 1B Amendment 17 binds. This is distinct from B6: B6 says the climb stalls, C3 says the starting rung was never the one declared.

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

Ramkrishna Forgings heats steel bars and presses them into shaped parts. It then machines most of them to finished size (B04). Auto forgings are about 74% of standalone FY26 revenue: 47.0% sold in India and 26.7% exported (B04). They are safety parts such as axle beams, knuckles, shafts and gears, made to the customer's own drawing, so a truck maker cannot swap supplier without qualifying the part again (B04). Railway bogie frames, mining and farm parts, and other industrial parts are the next streams, at 7.5%, 5.9% and 8.0% (B04). New casting and aluminium forging lines started between January and March 2026 (B04, B07). The customers are truck and tractor makers in India and Tier 1 and truck makers abroad. Tata Motors took 33.4% of consolidated revenue in the nine months to December 2025, two customers each exceed 10%, and North America was 71% of exports in the September 2026 quarter (B04, B03). Customers stay for more than ten years, yet they order against delivery schedules and management declined on four calls to give the customer or product split (B04, B05). Demand today follows truck builds: Tata Motors CV volumes and orders, India CV production and wholesale, and North America Class 8 orders and build, which Bharat Forge and M M Forgings also describe as recovering (B09, B06). US tariffs on steel and aluminium auto parts cut FY26 exports by 19.94% (B09). Demand should grow first as the capacity added in FY26 fills (72% total utilisation in Q2 FY27, B04), and EU truck and van registrations and ACMA component turnover are the outside checks on the export and domestic legs (B09). A further driver is Indian Railways forged wheel procurement and RDSO approval for the joint venture plant, in a market that imports 60 to 70% of about 2,00,000 wheels a year (B09). Domestic and export auto forgings carry a moderate moat from part qualification, ten year retention and large press lines, but the emerging moat scan scored qualification lock-in as weak and found no new advantage forming in these lines (B04, B07). Railway bogie frames show no moat, and their share of sales fell from 7.5% in FY26 to 5.5% in H1 FY27 (B07, B04). Forged rail wheels are the only line scored as a moderate emerging advantage, a policy tailwind from import substitution, and it is unproven because the plant is not in commercial production and the AR and the Oct 2026 call disagree on whether RDSO approval is needed (B07). Castings and aluminium forgings carry no moat and earn below the group margin, at 15 to 16% and 14 to 15% on management's own figures (B05, B07). The scan total of 9.0 classifies as NONE (B07).

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. Verticals framed

**V1. Utilisation and EBITDA per tonne**
- Established: installed capacity 3,95,800 t; total utilisation 72% in Q2 FY27, 68% in Q1 FY27, 62% in Q2 FY26 (B04, IP slide 10); EBITDA per tonne Rs 0.40 lakh in Q2 FY27 against Rs 0.28 lakh a year earlier (B04); two-year Sep-quarter growth of 33.4% against peers at 32.0 to 38.7%, so the 54.9% YoY jump is mostly a weak-base effect (B06); the 2.4x full-capacity net block turn is above every peer's own stated ceiling (B06).
- Cannot establish: EBITDA per tonne by domestic, export and casting; share of volume on steel price-adjustment contracts; whether the margin gain is mix, pricing or absorption (B04 input_gaps).
- Deciding questions: (1) Does revenue hold above Rs 1,405 Cr with margin at or above 18.23% in Q3 and Q4 FY27? (2) Is the margin step cost absorption or mix? (3) Does utilisation pass 75 to 80% before more capex, the gate management itself stated (B05)?

**V2. Export recovery and North America**
- Established: Q2 FY27 exports Rs 424.52 Cr (+52.7% YoY); North America Rs 301.69 Cr of Q2 exports (B04); FY26 exports fell 19.94% on tariffs (B09); Bharat Forge and M M Forgings confirm a Class 8 recovery lasting to Q3 CY27 (B06 verified, 9 anchors); foreign-currency receivables doubled to 55,560.20 INR lakh while outside-India revenue fell 19.9% (B02).
- Cannot establish: export customer names (AR26 names no customer, B04); Class 8 order data; FY26 average USD/INR (B09 NOT FOUND); share of exports with steel pass-through (B05).
- Deciding questions: (1) Does export share move from 30% toward the stated 35% in H2 (B05)? (2) Do foreign-currency receivables fall as exports rise? (3) Does North America hold after Class 8 normalises?

**V3. Net debt and financed working capital**
- Established: H1 FY27 debt cut Rs 126 Cr of the Rs 500 Cr plan (B05); March 2026 gross debt Rs 2,173 Cr and about Rs 2,000 Cr net of bill discounting (B05, from the Oct call, p.10); acceptances 65,016.26 plus receivables sold 39,978.46 = 1,04,994.72 INR lakh (B03); cash conversion cycle 89.6 days reported and 191.6 days before financing channels (B03, computed); bank stock statements differ from books in all four quarters, up to 20,602.56 INR lakh (B03); one covenant breached in FY26 with a waiver (B03).
- Cannot establish: management's net debt and ROCE definitions (B02); the bank, covenant and limits behind the waiver (B02); size and tenor of the acceptance programme (B02); H1 FY27 days before financing channels (B04).
- Deciding questions: (1) Is net debt below Rs 1,700 Cr at Dec 2026? (2) Do acceptances plus receivables sold fall? (3) Do stock statements agree with books in the Q1 and Q2 FY27 returns?

**V4. Domestic CV cycle and customer concentration**
- Established: domestic auto 47.0% of standalone FY26 revenue (B04); Tata Motors 33.4% of consolidated revenue in 9M FY26, down from 39% in FY18 (India Ratings via B04); two unnamed customers above 10% (B03); India CV +28.7% and PV +30.7% in Q2 FY27 stated by an analyst and partly verified by peers (B05, B06); M M Forgings names Ramkrishna as a direct competitor in CV axle, beam, crankshaft and connecting rod parts (B06).
- Cannot establish: Tata Motors share in H1 FY27; second customer identity; product split (declined on calls, B05).
- Deciding questions: (1) Does the Tata Motors share fall below 30% (B07 optionality)? (2) Do domestic forging tonnes keep pace with industry CV output? (3) Does the domestic price-taker pattern peers describe (B06) show in realisation per tonne?

### 4b. Candidate signal table (from B09 downstream_candidates; UNVERIFIED)
Likely sources are as B09 names them. Mapping to the Downstream_Source_Discovery_Protocol_v1_0 registry is done at Role 5.5 in claude.ai.

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| Tata Motors CV volumes and orders | Tata Motors CV wholesales fall YoY for two consecutive months | Monthly | Tata Motors monthly sales release and quarterly results |
| India CV production and wholesale | SIAM CV production growth turns negative YoY for two consecutive months | Monthly | SIAM monthly production data |
| North America Class 8 orders and build | Class 8 net orders fall YoY for two consecutive months | Monthly | ACT Research and FTR preliminary orders |
| US tariffs on steel and aluminium auto parts | A new or higher tariff takes effect on the export part classes, with no customer recovery | Event-driven | US Federal Register, USTR and Commerce notices |
| EU truck and van registrations | Heavy truck registrations fall YoY for two consecutive months | Monthly | ACEA registrations release |
| Indian Railways forged wheel procurement and RDSO approval | No written Railways acceptance of the first 300 wheels by 31 Dec 2026 | Event-driven | Ministry of Railways, RDSO and Railway Board orders |
| ACMA auto component industry turnover | ACMA quarterly turnover growth negative YoY | Quarterly | ACMA quarterly press release |

Candidate count: 7 (B09).

### 4c. Fragility read
- variable_count: **6** variables must go right: (1) utilisation fill and EBITDA per tonne; (2) North America export recovery; (3) Indian CV cycle; (4) net debt reduction; (5) working-capital release; (6) margin hold at or above 18% against steel, energy and shipping cost.
- verifiability_ratio: **2 of 6 externally observable** (North America Class 8 and the India CV cycle, both through public releases). Utilisation, net debt, working-capital days and margin are company-filed or company-narrated; the cause of the margin gain is company-narrated (B04, B05).
- single_point_failure: **Yes. The bank-funded working-capital channels and covenant compliance.** Acceptances plus receivables sold of 1,04,994.72 INR lakh are 59.3% of standalone borrowings (B03). One covenant was breached in FY26 and waived (B03). India Ratings adjusted leverage was 4.64x (B07). A cut in bank limits would raise reported debt with no change in operations.
- fragility_verdict: **FRAGILE** (six variables, four of them company-narrated, one kill-switch).

### 4d. Research brief (claude.ai work order, live web)
1. **PENDING LIVE VERIFICATION (Chain 1).** Tata Motors: latest quarterly results, investor presentation and monthly CV sales release. Read customer health, order outlook and any comment on supplier share.
2. **PENDING LIVE VERIFICATION (Chain 1).** ACT Research and FTR preliminary Class 8 orders and build forecast. Test the "recovery lasting to Q3 CY27" statement by Bharat Forge and M M Forgings (B06).
3. **PENDING LIVE VERIFICATION (Chain 2).** CRISIL Ratings full rationale for Ramkrishna Forgings (crisil.com; only the 20 Dec 2025 intimation is held) and any India Ratings update after 22 Jun 2026. Read the liquidity view, the acceptance line, the covenant comment and the outcome of the June 2025 rating watch (B08).
4. Chain 3 (to build): rail wheel JV. Resolve the RDSO contradiction (AR26 p.43 says RDSO certification is required; Oct 2026 call NJ p.17 says no approval is needed, B07) from the RDSO approved-vendor list and Railway Board tender notices.
5. Chain 4 (to build): US tariff status on steel and aluminium auto parts content. Federal Register and Commerce notices; link to the FY26 export loss of 19.94% (B09).
6. Chain 5 (to build): Europe. ACEA registrations and EU FTA status, against Europe at 41% of FY26 exports (B09).
7. Tata Motors share of revenue in H1 FY27 and the identity of the second customer above 10% (B03, B04). Check customer filings.
8. Maa Chandi Financial Advisory Services Pvt Ltd (formerly Ramkrishna Rail and Infrastructure Pvt Ltd): ownership and group link via MCA (B08).
9. Promoter pledge of 1,23,00,000 shares: pledgee, loan size and purpose, from creation and release disclosures on BSE and NSE (B08).
10. SEBI settlement order texts: company order of 19 Mar 2024 and Riddhi Portfolio 2018, at sebi.gov.in (B08).
11. 44th AGM voting results on the MD re-appointment and managerial commission (B08 skipped).
12. M M Forgings and Happy Forgings Q2 FY27 calls, if now filed (B06 gap).
13. FY26 average USD/INR from the RBI reference rate (B09 NOT FOUND).
14. Source URL verification of web-sourced market figures in B09 (AIFI tonnes, Grand View, IMARC, ACMA). B12a lists them as not checked.
15. Status of the contested electricity-duty recovery (counterparties JBVNL and TSUISL) and its appeal (B02, B03).
16. Peer working-capital practice: whether peers use acceptances and receivable sales (peers do not describe them, B06). Needed to read the 1,04,994.72 INR lakh.

### 4e. Second-order stub (Master Prompt v3.7, Rule F)

```
CHAIN 1: Total utilisation was 72% in Q2 FY27 on 3,95,800 t installed, after FY26 added capacity (B04; B07.capex_embedded_growth_pct: +29.3% tonnage). Revenue was Rs 1,405 Cr, +54.9% YoY, against two-year growth of 33.4% (B06).
Link 1 [DOCUMENTED]: Margin and EBITDA per tonne rose with volume (EBITDA per tonne Rs 0.40 lakh from 0.28; incremental margin 26.8% in Q2) (B04). B04 does not prove that the cause is fixed-cost absorption.
Link 2 [PENDING LIVE VERIFICATION]: Who pays for the extra tonnes and why now. Domestic: Tata Motors is 33.4% of revenue (B04) and CV volume is rising (B05, analyst-stated). Export: North America is 71% of Q2 exports (B04). The container cannot read customer order books. Claude web opens (a) Tata Motors latest quarterly results and monthly CV sales release, and (b) ACT Research / FTR Class 8 preliminary orders. Export customer names are NOT FOUND in the corpus (B04); never supplied from memory.
Link 3 [INFERENCE]: Management stated that the next capex comes only after 75 to 80% utilisation (B05, 1B row "Max asset turn"). It raised the FY27 capex guide from Rs 350 Cr to about Rs 550 Cr while utilisation was 72% (B05, B04). Peers also build ahead of orders: Happy forging utilisation 59%, M M Forgings about 52% (B06). So the stated gate has not governed spend, and the same end-demand must absorb several sets of new tonnes. The fill of RKFL tonnes depends on who wins the next qualification, which no block observes.
Binding constraint: capex and cash. Rs 160 Cr of H2 machining capex and Rs 50 to 55 Cr of JV equity are still to pay (B05, B07) against India Ratings adjusted leverage of 4.64x (B07). H1 FY27 receivables rose 795 to 1,025 Cr and inventory 1,246 to 1,469 Cr, faster than revenue; inventory days of 107.5 are the longest of four peers (B04, B06).
Unsaid: Foreign-currency receivables doubled to 55,560.20 INR lakh while outside-India revenue fell 19.9% (171 days against 68, computed) (B02). Two customers above 10% stay unnamed (B03). Neither topic reached any of the four calls (B05 warnings).
Observation that confirms or breaks this chain, and confirm-by date: Q3 FY27 results (expected late January 2027, on the Q3 FY26 pattern, call 27 Jan 2026, B00). Confirms: consolidated revenue above Rs 1,405 Cr, total utilisation above 72% on the IP slide 10 basis, EBITDA per tonne at or above Rs 0.38 lakh (B04 healthy band). Breaks: revenue flat QoQ for two quarters, or margin stalls near 18% (B05 kill signal).
```

```
CHAIN 2: H1 FY27 debt fell Rs 126 Cr against a Rs 500 Cr plan and net working capital rose Rs 140 Cr (B05). Management guides net debt to Rs 1,500 Cr by March 2027, "net of cash and bill discounting" (Oct 2026 call, LK p.10).
Link 1 [DOCUMENTED]: Acceptances 65,016.26 plus receivables sold 39,978.46 = 1,04,994.72 INR lakh, 59.3% of standalone borrowings (B03, AR26 Notes 20 and 8.7). Gross debt at March 2026 was Rs 2,173 Cr and about Rs 2,000 Cr on the net basis; the netting is supported by the transcript (B12b B-01). The filed bases differ: net debt 1,64,613.51 INR lakh standalone and 2,17,760.22 consolidated (B02).
Link 2 [PENDING LIVE VERIFICATION]: Who funds this and why now. Banks provide the acceptance and receivable-sale lines. The corpus holds no sanction letter or limit. Claude web opens (a) the CRISIL Ratings full rationale for Ramkrishna Forgings on crisil.com (only the 20 Dec 2025 intimation is held, B00), and (b) any India Ratings update after the 22 Jun 2026 rationale. It reads the liquidity view, the limit and the covenant comment. Lender names are NOT FOUND in the corpus (B02); never supplied from memory.
Link 3 [INFERENCE]: The guided net-debt fall needs about Rs 374 Cr in H2 (B05), while H1 receivables and inventory rose faster than revenue (B04). If bank limits tighten, or if the channels shrink as sales rise, reported debt can rise with no change in operations. The guide therefore depends on lender behaviour as well as on cash generation. A covenant breach would also change the debt classification from FY27 under the Ind AS 1 amendment (B03).
Binding constraint: covenant and interest cover. One covenant was breached and waived in FY26 (AR26 Note 18.4, B03). Standalone PBIT to interest was 1.72x against a 2.0x watch level (B03). Consolidated interest expense rose 46.6% (B03).
Unsaid: Stock statements given to banks differed from books in all four quarters, up to 20,602.56 INR lakh at Dec 2025, with a stated cause (one unit not integrated) that does not fit the quarters where the bank figure ran higher (B03). No call mentioned the restatement, the controls, or the warrants (B05).
Observation that confirms or breaks this chain, and confirm-by date: Q3 FY27 results (expected late January 2027): net debt below Rs 1,700 Cr at 31 Dec 2026 on the stated basis, and acceptances plus receivables sold flat or down from 1,04,994.72 INR lakh (B05, B03). Final check at Q4 FY27 results (expected May 2027, B07 catalysts): net debt at or below Rs 1,500 Cr. Breaks: the H1 pace of Rs 126 Cr repeats, or a further capex raise (B05).
```

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in claude.ai with live web, before Role 2.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. Ramkrishna Forgings makes steel parts for trucks, tractors and railways. It presses hot steel into shape and machines it to the customer's drawing (B04).
2. About 74% of standalone revenue comes from auto forgings: 47.0% sold in India and 26.7% exported (B04).
3. The company runs 20 plants and added 89,800 tonnes of capacity in FY26. Installed capacity is 3,95,800 tonnes (B07, B04).
4. Truck and tractor makers are the customers. Tata Motors alone took 33.4% of consolidated revenue in 9M FY26. Two customers each exceed 10% (B04, B03).
5. Abroad, the customers are US and European truck supply chains. North America was 71% of exports in the September 2026 quarter (B04).
6. Demand today follows truck builds in India and North America. Peers confirm a North America recovery (B06).
7. Growth should come first from filling the new capacity. Total utilisation was 72% in Q2 FY27 (B04). Revenue grew 54.9% YoY, but two-year growth of 33.4% matches peers, so much of it is a weak base (B06).
8. Rail wheels are a possible second driver. The plant has slipped three times and is not in commercial production (B05, B07).
9. The moat is moderate in the core auto lines, from part qualification and ten year customer retention. The emerging moat scan found it weak and scored 9.0, class NONE (B04, B07).
10. Rail bogie frames, castings and aluminium forgings show no moat. Castings earn 15 to 16% and aluminium 14 to 15% on management's figures (B07, B05).
11. The model in one line: a build-to-spec forger that borrowed to build capacity must show, quarter by quarter, that full presses lift margin and cut debt, before it climbs one rung from cost-advantaged converter to value-added supplier (Section 2, DRAFT).
12. The fragility read is FRAGILE. Six variables must go right, four are company-narrated or company-filed only, and one failure alone can break the thesis: the bank-funded working-capital channels worth 1,04,994.72 INR lakh (Section 4c; B03).
13. The corpus could not establish the net debt and ROCE definitions behind management's guidance, the customer and product split, the lender names, and the Tata Motors share for H1 FY27 (B02, B04, B05).
14. Open question one: do net debt and the bank channels fall at Q3 FY27 and Q4 FY27 while revenue holds above Rs 1,405 Cr (B05, B07)?
15. Open question two: did the FY25 inventory restatement of Rs 220.5 Cr close for good? The FY26 opinion is unmodified and the fact-finding closed with no further adjustment, but bank stock statements still differ from the books (B01, B03, B08).

---

## SECTION 6: STANDING EXTRACTION ANNEX

Quote-then-comment. Quotes are as printed in the .txt layer beside each PDF. Page anchors are PDF pages. "AR26" is inputs/annual-report/Annual_Report_2026.pdf, "AR25" is Annual_Report_2025.pdf, "IP" is inputs/presentation/Investor_Presentation_1.pdf.

### 1. UNITS
- Printed per-unit figures, IP slide 8 (PDF p.9), text layer, labels lost for the domestic and export rows:
  - Header: "Volume (tons) Realisation (₹ Lac/ton)".
  - Forgings, Q2 FY26 / Q1 FY27 / Q2 FY27: "26,763 32,382 37,048" and "12,646 14,630 16,056" (volumes); "1.78 2.13 2.08" and "2.19 2.42 2.52" (realisation).
  - Forgings, H1 FY26 / H1 FY27: "1.81 2.11" and "2.29 2.47"; volumes "57,577 69,430", "26,003 30,686", "83,580 1,00,116".
  - Castings, Q2 FY26 / Q1 FY27 / Q2 FY27: "5,113 8,593 11,583" and "1.27 1.31 1.33"; H1: "9,763 20,176" and "1.29 1.32".
  - Comment: the unit is rupees lakh per tonne. Forgings figures cover a basket split by market (the domestic and export assignment of rows is an inference, B04, and must be read from the PDF image). Castings are a separate basket. No single printed all-product figure exists.
- Derivation from printed lines: H1 FY27 volume = 1,00,116 t forgings + 20,176 t castings = 1,20,292 t (IP slide 8). Revenue: IP slide 9 (PDF p.10) "Domestic 821.57 516.42 59.1% 735.07 11.8%" and "Export 424.52 277.97 52.7% 353.87 20.0%" (Rs Cr; Q2 FY27, Q2 FY26, YoY, Q1 FY27, QoQ). B04 derives Rs 2.18 lakh per tonne for H1 FY27 (2,622 Cr / 1,20,292 t), which includes scrap and other lines. Comment: a derived blend, not a printed figure.
- Production, IP slide 10 (PDF p.11): "Total Capacity 3,95,800# 220,279 70,925 72% 66,894 68% 47,490 62%" (installed t, FY26 t, Q2 FY27 t and utilisation, Q1 FY27, Q2 FY26). "Utilization (%) has been calculated on installed capacity on Annualized basis". Comment: tonnes produced, not tonnes sold.

### 2. SEGMENT CAPITAL AND DEBT
- Segment assets, liabilities and capital employed: NOT DISCLOSED. The company reports one segment. AR26 p.132 (standalone Note 34): "The Company manufactures “Forging components” and the management reviews the performance of the Company as a single operating segment". AR26 p.219 (consolidated Note 34): "there is only one reporting segment of forging components". Results_Q2_FY27_Sep_2026.pdf p.6 (OCR text layer): "as a single operaling segment ... no separate segment information has been furmished herewith".
- Borrowings are unallocated. Totals as printed: standalone "Total borrowings  1,77,162.17  1,58,467.48" (INR lakh; Mar 2026, Mar 2025; AR26 p.120); consolidated "Total borrowings  2,33,503.35  2,01,276.85" (AR26 p.202).
- Comment: no segment capital view exists. Net block and capital employed are available only at company level.

### 3. GUIDANCE VERSUS ASPIRATION
Call dates: Q3 FY26 27 Jan 2026; Q4 FY26 4 May 2026; Q1 FY27 24 Jul 2026; Q2 FY27 30 Oct 2026. Page anchors are PDF pages and may differ by one from B05's printed-page cites (B12a finding 7).

| Item | Quote as printed | Class | Anchor |
|---|---|---|---|
| FY27 capex | "We are not looking at capex of more than Rs. 300 to Rs. 400 crores maximum" | (a) guidance, FY27; superseded | Concall_May_2026, p.13 |
| FY27 capex, latest | "we should be ending this year close to around Rs. 550 crores throughout our entire group" | (a) guidance, FY27 | Concall_Nov_2026, p.9 |
| H2 capex | "you can assume another Rs. 160 crores of capex for the second half, basically on the machining side" | (a) guidance, H2 FY27 | Concall_Nov_2026, p.10 |
| JV equity pending | "JV still about RS. 50 crores, RS. 55 crores investment is pending" | (a) guidance, "next one year" | Concall_Nov_2026, p.10 |
| Debt reduction | "we will reduce at least Rs. 500 crore of leverage in this financial year" | (a) guidance, FY27 | Concall_Jul_2026, p.17 |
| Net debt | "that's why we guided for the Rs. 500 crores reduction to Rs. 1,500 crores. So, the guidance remains same." Gross: "Rs. 1,670 crores to Rs. 1,700 crores will be the number" | (a) guidance, March 2027 (net of cash and bill discounting, per the question and answer) | Concall_Nov_2026, p.10 |
| ROCE FY27 | "By the end of FY27, we will be in the range of 12% to 15% on ROCE." | (a) guidance, FY27 | Concall_Nov_2026, p.19 |
| ROCE FY28 | "that is the aspiration that next year, we should have 20% ROCE. I will say that's an aspiration." | (b) aspiration | Concall_Nov_2026, p.19 |
| Export share | "we are looking at almost 35% revenue on a consol balance sheet coming from exports, for a full year basis" | (a) guidance, FY27 | Concall_Jul_2026, p.9 |
| Margin | "We should be at least 100 to 150 basis points better than what we have done right now. But it all depends on whether we have been we are able to pass on the energy price increases." | (a) conditional guidance, FY27 | Concall_May_2026, p.19 |
| Revenue Rs 8,000 Cr | "I think we are one-year delayed ... we are on track right now with FY29 [...] as Rs. 8,000 crores." ([...] marks one word omitted; see Jul p.22 line 771) | (a) guidance, FY29; treated as withdrawn on the Oct call (B12b B-04) | Concall_Jul_2026, p.22 |
| Revenue, Oct reply | "Every year, we will basically be able to guide you for the next year ... for the next year financial year and the following year, we will be able to comment after the full year earnings call." | withdrawal of multi-year guidance | Concall_Nov_2026, p.19 |
| Revenue Rs 8,000 Cr, Oct | "we are very much there, but we will update you with the time. Let us wait for some time." | no period | Concall_Nov_2026, p.18 |
| Capacity utilisation | "~80% overall FY27 end; casting 85-90%; cold forging 75-80%" (B05 1B summary of the May call; not re-quoted) | (c) capacity or capability, FY27 | B05 report 1B; Concall_May_2026 |
| Installed capacity and asset turn | 2.5x on net block ~Rs 3,700 Cr = ~Rs 9,000 Cr sales at 100% utilisation (B05 1B summary; not re-quoted) | (c) capacity only | Concall_Jul_2026, p.19 |

Comment: only the margin, export-share and debt items are dated quantities. Rs 8,000 Cr and ROCE FY28 are not firm guidance. Capacity statements say what the plant can do, not what it will ship. Rows marked "B05 1B summary" are reused from B05 and not re-opened.

### 4. CONCENTRATION
- Customer: India Ratings p.2: "The contribution from TML reduced to 33.4% in 9MFY26 (FY18: 39%) of the consolidated revenue." AR26 p.219: "There are two external customers who accounts for more then 10% of the Holding Company’s revenue individually". Comment: the second customer above 10% is not named. NOT DISCLOSED in the AR.
- Product: NOT DISCLOSED as a product split; the AR reports one segment. End-market mix, IP slide 11 (PDF p.12), standalone, FY26: "Domestic Auto ... 47.0%", "Railways ... 7.5%", "Mining, Earth Moving & Farm Equipment ... 5.9%", "Miscellaneous (Industrial Components,  Steel, Cement & Power) ... 8.0%", "Exports - Auto ... 26.7%", "Exports - Others ... 4.9%", "Total Export ... 31.6%". Top stream is domestic auto at 47.0%. India Ratings p.2: "The automotive segment’s contribution to the standalone revenue reduced to about 74% in FY26 (FY25: 78%)."
- Geography: AR26 p.219 consolidated, INR lakh, FY26 / FY25: "India  3,02,582.42  2,54,623.14", "Outside India  1,21,225.31  1,48,787.54", "Total  4,23,807.73  4,03,410.68". Export breakup, IP slide 12 (PDF p.13), Rs Cr: "North America 301.69 222.25 128.74 688.12 58.0% 1,056.42 71.3%" (Q2 FY27, Q1 FY27, Q2 FY26, FY26, FY26 %, FY25, FY25 %), "Europe 120.95 128.41 146.96 489.83 41.3% 413.51 27.9%".
- Comment: management declined to give the customer and product split on the calls (B05 evasion table).

### 5. PROMISE LEDGER
Source: B05 report 2A, with B12b adjustments. Date made = call date. Delivery status as scored at the Oct 2026 call (30 Oct 2026). Anchors are the B05 call-and-page cites; B12a finding 7 records that some are printed pages (PDF page minus 1).

| # | Date made | Promise | Status | Evidence anchor |
|---|---|---|---|---|
| 1 | 27 Jan 2026 | FY26 growth "double-digit" | MISSED (FY26 revenue +5%, Rs 4,238 Cr vs Rs 4,034 Cr) | Jan NJ p.21; May LK p.4 |
| 2 | 27 Jan 2026 | Debt below Rs 2,000 Cr, maybe Rs 1,900 Cr by end FY26 | PARTIAL (Rs 2,173 Cr gross, about Rs 2,000 Cr net of bill discounting) | Jan LK p.7; Oct LK p.10 |
| 3 | 27 Jan 2026 | Casting commercial production in Q4 FY26 | DELIVERED (from 31 Mar 2026) | Jan LK p.4; May LK p.8 |
| 4 | 27 Jan 2026 | Rail wheel JV trial production end Q4 FY26 | MISSED (first 300 wheels under inspection in Oct) | Jan LK p.5; Oct NJ p.15 |
| 5 | 27 Jan 2026 | Mexico machining "nearing commissioning" | PARTIAL (started Q1 FY27, Rs 6 Cr revenue; about two quarters late) | Jan LK p.5; Jul NJ p.8 |
| 6 | 27 Jan 2026 | Margin improves QoQ | DELIVERED (14.9, 17.1, 17.96, 18.23%) | Jan NJ p.12; Oct LK p.4 |
| 7 | 27 Jan 2026 | FY27 growth 10 to 15% | PENDING (H1 only; B12b B-08 moves it from DELIVERED) | Jan NJ p.13; Oct LK p.3 |
| 8 | 27 Jan 2026 | North America "worst behind" | DELIVERED (Q2 FY27 exports Rs 424 Cr vs Rs 277 Cr) | Jan NJ p.9; Oct MG p.11 |
| 9 | 4 May 2026 | Casting utilisation 85 to 90% | DELIVERED (88%, analyst-stated, not disputed) | May NJ p.7; Oct Aditya Kumar Q p.9 |
| 10 | 4 May 2026 | FY27 capex not above Rs 300 to 400 Cr | MISSED (about Rs 550 Cr by Oct) | May NJ p.12; Oct NJ p.9 |
| 11 | 4 May 2026 | Margin 100 to 150 bps above 17.1% | DELIVERED (18.23%, +113 bps) | May NJ p.18; Oct LK p.4 |
| 12 | 4 May 2026 | Customers compensate for energy cost from 1 April | MISSED ("customers are not prepared to pay"; Rs 8 to 9 Cr borne in Q2) | May NJ p.14, p.19; Jul NJ p.11; Oct LK p.14 |
| 13 | 4 May 2026 | Wheel plant production May or June; 40,000 wheels in FY27 | MISSED (production December; 20,000 to 25,000 wheels) | May NJ p.6; Oct NJ p.16 to 17 |
| 14 | 24 Jul 2026 | Bulk wheel production Sep or Oct; 300 samples in August | MISSED (samples under inspection; production December) | Jul NJ p.8; Oct NJ p.15 |
| 15 | 27 Jan 2026 | Passenger vehicles 10% of revenue by FY28 | PARTIAL (moved to "CY28 or FY29"; no PV revenue disclosed) | Jan NJ p.10 to 11; Oct NJ p.20 |
| 16 | origin not in the Jan call (B12b B-07); put to management on the Jul call by an analyst | Revenue Rs 8,000 Cr by FY28, moved to FY29 | Excluded from the score per B12b B-07; the FY29 figure is treated as withdrawn on the Oct call (B12b B-04) | Jul Bharat Shah Q p.22; Oct NJ p.18 to 19 |
| 17 | 4 May 2026 | Aerospace order book by FY27 end | PARTIAL (Jul: "zero order book") | May NJ p.18; Jul NJ p.15 |
| 18 | 4 May and 24 Jul 2026 | Debt reduction Rs 500 Cr; net debt Rs 1,500 Cr by Mar 2027 | PENDING (H1: Rs 126 Cr = 25%) | May LK p.8; Jul LK p.17; Oct LK p.4 |
| 19 | 24 Jul 2026 | ROCE 12 to 15% FY27, 20% FY28 | PENDING (FY28 now an aspiration) | Jul LK p.9; Oct LK p.19 |
| 20 | 24 Jul 2026 | Working capital down 10 days in a year | PENDING (days "almost where March"; value +Rs 140 Cr) | Jul LK p.21; Oct LK p.24 |
| 21 | 24 Jul 2026 | Mexico significant revenue from Q3 FY27 | PENDING | Jul NJ p.8 |
| 22 | 4 May 2026 | Trailer axle to Rs 250 Cr in FY27 | NO UPDATE (dropped) | May NJ p.9 |

Score before the B12b adjustments, from B05: 6 delivered, 4 partial, 7 missed on 17 scored rows. With row 7 moved to pending and row 16 excluded, B12b states delivery stays at 47 to 50% and concurs with grade C. Rows 4, 13 and 14 are one project (the wheel JV) counted three times. Comment: financial headline promises landed; capital and project promises slipped.

### 6. RESTATED BASES
- Inventory restatement (the load-bearing fact). AR25 p.161 Note 47: "certain erroneous entries / non- recording of rejections at plant resulted in overstatement of WIP / raw material / scrap inventory in the Financial Year ended March 31, 2025 and previous Financial Year ended March 31, 2024 by ₹ 22,052.43 lakhs and ₹ 5,022.26 lakhs respectively." And: "restated previous financial year comparative as per IND AS 8". Restated FY24 as printed (reported, restated; INR lakh): "Profit Before Tax (PBT)  43,653.35  38,631.10", "Profit After Tax (PAT)  32,606.93  27,584.68", "Inventories as at March 31, 2024  1,00,350.75  95,328.50", "Total Equity as at March 31, 2024  2,67,256.19  2,62,233.94". Comment: FY24 PAT restated down 15.4%.
- Report date. AR26 p.15 (Directors' Report, disclosure j): "The report of the joint fact-finding study ... was submitted on 14 June, 2025". Comment: anchor corrected per B12a finding 4.
- FY26 treatment. AR26 p.153 Note 52: "there are no further discrepancies identified beyond those which were accounted for at March 31, 2025, and (b) the discrepancies identified up to the date of the interim report were not the result of any fraud, but due to errors in accounting or process gaps. Accordingly, no additional adjustments are required in the financial statements for the year ended March 31, 2026". Comment: closed on paper; agency names and report dates are NOT DISCLOSED in the note.
- Comparative as printed in the latest filing. AR26 p.86 (standalone balance sheet): "(a) Inventories 14  1,07,915.96  1,08,510.11" (31 Mar 2026; 31 Mar 2025). AR26 p.114 Note 14: "Total  1,07,915.96  1,08,510.11". AR26 does not carry FY24, so the restated FY24 figures sit only in AR25.
- Merger restatement (ACIL). AR25 p.162: "the comparative standalone financial statements for the year ended March 31, 2024, included in this statement have also been restated to give effect of the scheme" ... "as if the business combination has occurred from February 19, 2024". Comment: FY24 comparatives in AR25 carry both the inventory restatement and the ACIL common-control restatement.
- Reclassification. Government grant receivable of 2,722.59 INR lakh was current in FY25 and is wholly non-current in FY26 (AR26 Note 13 p.114, via B02). Comment: reclassification, no profit effect stated.
- Subsidiary mergers. AR26 p.17: "approved the Scheme of Amalgamation of Multitech Auto Private Limited ... and Mal Metalliks Private Limited ... with Ramkrishna Casting Solutions Limited ... and accordingly it ceased to the Subsidiary of the Company with effect from 25 March, 2026." AR26 p.136 related-party note shows the two as "NIL" holdings at 31 Mar 2026 against 100 at 31 Mar 2025. Comment: appointed date 1 Jan 2024 (see question 7). Whether the AR26 consolidated comparatives are restated for this common-group merger is NOT DISCLOSED in the pages read; the group already consolidated both entities.

### 7. CORPORATE-ACTION CLAUSES
No demerger and no share repurchase appear in the corpus. Four actions appear.

**(a) Scheme of Amalgamation: Mal Metalliks Private Limited (Transferor 1) and Multitech Auto Private Limited (Transferor 2) into Ramkrishna Casting Solutions Limited (Transferee).** Source: announcements/2026_03_STExchDisclAmalg28Feb26.pdf (NCLT Kolkata order, 27 Feb 2026) and 2026_03_DisclosureReg30Subsidiarycessationonmerger.pdf (26 Mar 2026).
- Appointed date: "Appointed Date: 01st January, 2024" (order p.4).
- Effective date: "the Scheme has become effective from March 25, 2026 ... both Transferor Company No.1 and Transferor Company No. 2 stands dissolved without winding up" (26 Mar 2026 filing, p.1).
- Liability allocation: "All the debts, liabilities and duties and obligations of the Transferor Companies be transferred from the said Appointed Date, without further act or deed, to Transferee Company" (order p.14). Property: "transferred to and vest in the Transferee Company ... subject nevertheless to all charges now affecting the same" (order p.14). Employees: "All the obligations/ liabilities of the Transferor Companies with regard to their workmen and employees shall be the responsibilities of the Transferee Company" (order p.15).
- Ratio: "The exchange ratio of shares in consideration of the Amalgamation has been fixed on a fair and reasonable basis and on the basis of the Report thereon of CA Ritesh Kumar Gupta." The ratio itself is NOT DISCLOSED in the filing. Fetch the Scheme (Annexure A to the petition) or the Valuation Report (Annexure M) from BSE or the NCLT Kolkata file.
- Undertaking definitions: the order does not define a demerged undertaking. Not applicable to an amalgamation.
- Comment: the two transferors were wholly owned, so the ratio affects the group, not minority holders.

**(b) Preferential warrants to Riddhi Portfolio Private Limited.** Source: announcements/2025_05_Outcome-Board-Meeting-30-May-2025.pdf p.5.
- "The Company will issue and allot upto 9,75,000 Warrants ... at an issue price of Rs 2,100/- per Warrant aggregating up to Rs. 204.75 Crores to Riddhi Portfolio Private Limited (Promoter Category)". "The floor price of as per the provisions of Regulation 164 of Chapter V of the SEBI ICDR Regulations is Rs. 712.34 per Warrant." "The issue price of Rs. 2,100/- per Warrant is approximately 2.95 times the floor price."
- Receipts (B08, from AR26 and filings): 14 Aug 2025, 27 Mar 2026 and 9 Jun 2026, Rs 204.75 Cr in total; auditor Reg 169(5) certificate 19 Aug 2026. Appointed and effective dates are NOT DISCLOSED in the 30 May 2025 filing; the receipt dates above come from B08.
- Comment: priced at 2.95x the regulatory floor. Liability clauses beyond price and quantity are NOT DISCLOSED in the filing.

**(c) Preferential warrants to Chaitanya Jalan.** Source: announcements/2025_11_Outcome-Board-Meeting-12-Nov-2025.pdf p.3 (.txt lines 71 to 74) and announcements/2026_09_STExchCMCOutcome24Sep26.pdf pp.1 to 4.
- "The Company will issue and allot upto 34,00,000 Warrants ... at an issue price of Rs 588/- per Warrant aggregating up to Rs. 199.92 Crore to Mr. Chaitanya Jalan, Promoter" (12 Nov 2025 outcome).
- "34,00,000 Warrants had been allotted on 14 January 2026 carrying a right to subscribe to 1 Equity Share per warrant on receipt of amount at the rate of Rs. 147/- per warrant (being 25% of the warrant issue price i.e. Rs. 588/-)". Conversion: "allotment of 34,00,000 ... Equity Shares ... upon receipt of balance amount aggregating to Rs. 149,94,00,000/- ... at the rate of Rs. 441/- per Warrant (being 75% of the Warrant Issue Price)" (24 Sep 2026). Post allotment: "18,55,70,017 fully paid-up Equity Shares of Rs. 2/- each".
- Comment: Rs 199.92 Cr in total from this holder. The 12 Nov 2025 text layer is partly garbled (line 13 omitted as too long to display); the quote is from lines 71 to 74.

**(d) Reclassification of Maa Chandi Financial Advisory Services Pvt Ltd (formerly Ramkrishna Rail and Infrastructure Pvt Ltd) from promoter group to public.** Source: announcements/2025_11_Promoter-Reclassification-12-Nov-2025.pdf and the NSE summary rows of 19 and 30 Sep 2026.
- "holding 65,00,000 Equity Shares of the Company (3.59%), seeking reclassification from “Promoter Group” category to “Public’ Category” shareholder, subject to the approval of the Stock Exchanges, shareholders and such other approvals" (12 Nov 2025 filing). Shareholder approval by postal ballot on 19 Sep 2026; exchange NOC dated 5 Aug 2026 (NSE summary, 30 Sep 2026 row).
- Effect: promoter and promoter group holding 43.39% (30 Jun 2026) to 39.82% (19 Sep 2026) to 40.93% (30 Sep 2026, after 34,00,000 warrants converted on 24 Sep 2026) (NSE summary). Comment: the fall in promoter holding is a reclassification. No promoter share was sold (B08).

### 8. RELATED-PARTY PERIMETER (AR26 Note 39, standalone, INR lakh, FY26 / FY25; marker pages 136 to 139)
Promoter-group and promoter-influenced entities named in the note:

| Entity | Relationship (as printed) | Nature | FY26 | FY25 | Page |
|---|---|---|---|---|---|
| Riddhi Portfolio Private Limited | "Entity having significant influence over the Company" | Dividend paid | 605.57 | 758.51 | 137 |
| Eastern Credit Capital Private Limited (amalgamated with Riddhi) | "Enterprise over which KMP and their relatives are able to exercise significant influence" | Dividend paid | nil | 452.23 | 137 |
| Maa Chandi Financial Advisory Services Pvt Ltd (formerly Ramkrishna Rail and Infrastructure Pvt Ltd) | same | Dividend paid | 65.00 | 130.00 | 137 |
| Naresh Jalan (HUF) | same | Dividend paid | 13.44 | 26.88 | 138 |
| Mahabir Prasad Jalan (Chairman Emeritus) | KMP | Sitting fees | 4.00 | 4.00 | 138 |
| Naresh Jalan (MD) | KMP | Short-term benefits; long-term benefits; dividend | 461.19; 30.53; 45.15 | 448.77; 30.10; 90.31 | 138 |
| Chaitanya Jalan (WTD) | KMP | Short-term benefits; long-term benefits; commission; dividend | 212.78; 8.52; nil; 30.48 | 205.50; 8.38; 100.00; 60.96 | 138 |
| Rashmi Jalan (wife of Naresh Jalan) | relative of KMP | Dividend paid | 20.94 | 41.88 | 138 |
| Radhika Jalan (wife of Chaitanya Jalan) | relative of KMP | Dividend paid | 0.11 | 0.11 | 138 |

Trusts: "Ramkrishna Foundation" CSR expenses 353.48 (417.42); "Ramkrishna Forgings Employee Welfare Trust" advance given or repayment nil (1,022.93) (p.139).
Company-side exposure (subsidiaries and JV, not promoter-owned): Ramkrishna Casting Solutions Limited sales 9,528.78, purchase 10,676.69, corporate guarantee given 21,930.00 in FY26 (outstanding 41,730.00), unsecured loan outstanding 8,285.11; Ramkrishna Forgings Mexico investment 2,779.00 and guarantee outstanding 17,781.56; Ramkrishna Titagarh Rail Wheels Limited investment 7,743.37, sales 425.35, design services 1,100.00, project management services 1,500.00, shortfall undertaking 52,479.46 outstanding; Ramkrishna Forgings LLC sales 13,109.60 (AR26 pp.136 to 139).
Comment: promoter-entity transactions are dividends and pay only. The exposure sits in subsidiary and JV support, as B08 states. Other KMP lines (Khetan, Gandhi, Mundhra, independent directors) are on p.138 and carry pay, sitting fees and small loans.

### 9. PLEDGE AND SHAREHOLDING
Promoter and promoter group holding, as filed (NSE summary, inputs/shareholding/NSE_shareholding_summary_RKFORGE.txt, field "pr_and_prgrp"):

| Quarter end | Promoter % | Public % | Source row |
|---|---|---|---|
| 31 Mar 2025 | 43.13 | 56.74 | submitted 18 Apr 2025 |
| 30 Jun 2025 | 43.13 | 56.74 | 21 Jul 2025 |
| 30 Sep 2025 | 43.13 | 56.75 | 18 Oct 2025 |
| 31 Dec 2025 | 43.13 | 56.75 | 21 Jan 2026 |
| 31 Mar 2026 | 43.33 | 56.55 | 20 Apr 2026 |
| 30 Jun 2026 | 43.39 | 56.41 | 17 Jul 2026 (revised 14 Aug 2026) |
| 19 Sep 2026 (event) | 39.82 | 59.98 | 28 Sep 2026 |
| 30 Sep 2026 | 40.93 | 58.88 | 15 Oct 2026 |

- Twelve quarters: NOT DISCLOSED in the corpus for the four quarter ends before 31 Mar 2025. Only eight rows are held (seven quarter ends and one event).
- Pledge, XBRL 30 Sep 2026 (inputs/shareholding/NSE_SHP_XBRL_30_Sep_2026.txt): "NumberOfSharesEncumberedUnderPledged ... 12300000" for the promoter group; "...AsPercentageOfTotalNumberOfShares ... 0.162"; Riddhi (other Indian shareholders) "11000000" at "0.1738"; individuals "1300000" at "0.1027" (Naresh Jalan 13,00,000 shares). The 19 Sep 2026 XBRL carries the identical count (B08). Comment: 1,23,00,000 shares, 16.20% of promoter holding, 6.63% of paid-up capital (B08, base corrected per B12a finding 1). Pledge at earlier quarter ends is NOT DISCLOSED in the held filings (summary rows carry no pledge field; AR26 is silent, B03). Pledgee, loan size and purpose are NOT DISCLOSED (B08); the Aug and Sep 2025 dates rest on media (B08).
- Institutional holding, latest (30 Sep 2026 XBRL): "InstitutionsForeign_ContextI ... 31635739" shares and "InstitutionsDomestic_ContextI ... 10626783" shares, of 18,55,70,017 paid-up shares (24 Sep 2026 filing). B08 computes about 17.0% and 5.7%. Comment: employee trusts 0.19% (NSE summary).

### 10. VERIFICATION
Documents quoted in this annex, with document date:
- inputs/presentation/Investor_Presentation_1.pdf (Q2 and H1 FY27; document date not stated in the blocks)
- inputs/annual-report/Annual_Report_2026.pdf (FY2025-26)
- inputs/annual-report/Annual_Report_2025.pdf (FY2024-25)
- inputs/results/Results_Q2_FY27_Sep_2026.pdf (quarter ended 30 Sep 2026; OCR layer)
- inputs/rating/IndiaRatings_Rationale_22_Jun_2026.pdf (22 Jun 2026)
- inputs/concalls/Concall_May_2026_Transcript.pdf (4 May 2026), Concall_Jul_2026_Transcript.pdf (24 Jul 2026), Concall_Nov_2026_Transcript.pdf (30 Oct 2026); Concall_Feb_2026_Transcript.pdf (27 Jan 2026) cited through B05 only
- inputs/announcements/2025_05_Outcome-Board-Meeting-30-May-2025.pdf (30 May 2025)
- inputs/announcements/2025_11_Outcome-Board-Meeting-12-Nov-2025.pdf (12 Nov 2025)
- inputs/announcements/2025_11_Promoter-Reclassification-12-Nov-2025.pdf (12 Nov 2025)
- inputs/announcements/2026_03_STExchDisclAmalg28Feb26.pdf (28 Feb 2026; NCLT order 27 Feb 2026)
- inputs/announcements/2026_03_DisclosureReg30Subsidiarycessationonmerger.pdf (26 Mar 2026)
- inputs/announcements/2026_09_STExchCMCOutcome24Sep26.pdf (24 Sep 2026)
- inputs/shareholding/NSE_shareholding_summary_RKFORGE.txt (fetched 12 Nov 2026) and NSE_SHP_XBRL_30_Sep_2026.txt (filed 15 Oct 2026)
Gaps in the annex: rows marked "B05 1B summary" in question 3 and the Jan-call anchors in question 5 were reused from B05, not re-opened.

CORPUS COMMIT HASH: cc14133bff227f2622840b2f1cd6b4d71c60c89c
