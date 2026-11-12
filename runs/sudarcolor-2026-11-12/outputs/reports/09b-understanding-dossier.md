# HALT 1 UNDERSTANDING DOSSIER: Sudarshan Colorants India Ltd (SUDARCOLOR)

Run date 2026-11-12. Stage 09b. Assembly from blocks B00 to B09 and verifier blocks B12a to B12d. Section 4e and Section 6 carry the two scoped exceptions. No valuation, price or verdict language. Source-fidelity gate applied: where Verifier A (B12a) corrected a number, this file carries the source_truth value (H1 FY27 PBT 59.67; peer EBITDA margin median 8.17%; peer gross margin median 39.00%; FY17 EBITDA margin 6.84%; OCF excluding government balances 13.71; institutional holding 0.71% at Dec 2025; shares 2,30,81,798).

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

Inventory only. Source: B00 inventory and corpus_manifest unless named.

1. CONCALLS. Held for the company: none. Declared no-concall mode (B00.concalls_available false). Most recent quarter covered by a company call: none. Q2 FY27 results were filed 2026-10-28 (B00), so a Q2 FY27 call would be the plausible newest event, but the company holds none and web search at /step1 found no call and no presentation (B00 input_gaps). Peer transcripts held: 11 (SUDARSCHEM 4, latest Q1 FY27 call 2026-08-14; MOL 4, latest Q2 FY27 call 2026-11-05; ASAHISONG 3, latest Q4 FY26 call 2026-06-01) (B00, B06). The parent's Q2 FY27 call (due about Nov 2026) is absent (B06).
2. ANNUAL REPORTS. Held: FY2025-26 (cover letter 2026-07-27, 69th AGM 2026-08-18) and FY2024-25 (cover letter 2025-09-05) (B00). The latest completed FY is present. Two years are held, not three (FY2023-24 absent).
3. RESULTS FILINGS. Latest: Q2 FY27 and H1 FY27, outcome letter 2026-10-28. Also held: Q1 FY27 (2026-08-05) and Q4 FY26 audited (2026-05-11) (B00). Quarter gap between latest results and latest AR: the AR closes at 31 Mar 2026; results run two quarters beyond it, and both are held. No gap.
4. INVESTOR PRESENTATIONS. ABSENT (B00.inventory presentation 0).
5. RESEARCH / RATING. ABSENT. AR FY26 p.67 item 19 confirms no credit rating sought (B03). Screener lists only CARE updates of 2017 to 2019 under the Clariant name; none collected (B00).
6. CORPORATE ACTIONS. Seven announcement PDFs, 2026-09-01 to 2026-10-28 (B00): director resignation (2026-09-01); RTA certificate (2026-10-07); board meeting intimation (2026-10-19); results outcome (2026-10-28, duplicate of the results file); two SAST Reg 29(2) disclosures (2026-10-01, scanned, no text layer); SAST Reg 10(7) report (2026-10-19, pages 1-5 scanned). The prior 12 months of Reg 30 filings are not in the corpus. That is a collector limit, never evidence that nothing was filed (B00).
7. FRESHNESS PAIR CHECK. B00.freshness_verdict is FRESHNESS PAIRS OK. Pair 1 (results to concall) SKIPPED because no concalls exist. Pair 2 (rating bulletin to rationale) PASS, no trigger. Pair 3 (SEBI order to order text) PASS, no order referenced at stage 0. Pair 4 (AR to latest audited annual results) PASS. No failed pair, so the freshness verdict does not apply.
8. VERDICT LINE: **CORPUS GAPPED**

Missing documents:

| Document | Expected source | Kind |
|---|---|---|
| Any company concall transcript | company IR page | plausibly-nonexistent (company holds none; opacity feeds the kill decision) |
| Investor presentation | company IR page | plausibly-nonexistent (none found by web search, B00) |
| Rating rationale | rating agency site | plausibly-nonexistent (no rating sought, B03) |
| H1 FY27 Reg 23 related-party filing | BSE | findable-missing (load-bearing; B05, B06, B07 all name it as the separating observation) |
| Quarterly shareholding pattern as filed, with pledge line (corpus holds a screener copy) | BSE | findable-missing |
| Reg 30 announcements before 2026-09-01 | BSE | findable-missing |
| Annual report FY2023-24 | company IR page | findable-missing |
| Text of scanned SAST filings 6D1F3240, A16C6814, C1DC7FB5 pp.1-5 | BSE | findable-missing |
| Letter of Offer (open offer computation) | BSE | findable-missing (B08 gap) |
| SUDARSCHEM Q2 FY27 concall transcript | company IR page | findable-missing (B06) |

Other open inputs (B00): screener P&L, Quarters, Balance Sheet, Cash Flow exports came out empty; operator to open Financials.xlsx, save, and run --push-again. Verifier A shadow not run (shadow.yaml left armed).

Empty input folders (repeat of the full list, confirmation suppressed under the /step1 autonomy contract): prospectus (long-listed, not a gap), rating, concalls (declared), research, presentation (B00).

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT - PENDING OPERATOR SIGN-OFF.** Not signed. Signing happens only in claude.ai after live-web stress-testing.

### PART A: THE FROM STATE

**A1. Archetype.**
- Third-party pigment sales, 71.6% of revenue (558.71 of 780.63, derived) (B04): **Build-to-spec component maker** (customer spec, repeat orders, input-cost pass-through). Open classification question: peers show pass-through and plants at 39-51% utilisation (B06), and no moat is confirmed (B01, B07). A Commodity converter reading is the alternate. If the operator rules converter, Amendment 17 binds and spot-year ROCE and rupee WC trends stay out of Section 1B and FTTCP.
- Group-allocated sales (191.40, 24.5%) and services (24.83, 3.2%) (B04): **Outsourcing partner** (wallet share sits with the parent, capacity fill is set by the parent).

**A2. The simple analogy.** Think of a large kitchen that grinds and mixes colour powders for paint, plastic and ink makers. Three plants do the work, at Roha, Cuddalore and Nagda (B03). The kitchen belongs to a bigger group. About one rupee in four of its sales goes to sister kitchens abroad, and about one rupee in three of its raw material comes from the group (B02). The group decides which product is made where. The kitchen has no debt and holds a lot of cash (B03). It earns thin margins today (B01).

### PART B: THE TRANSITION

**B1. FROM to TO.** One line transitions: pigments (single reporting segment, B04).
- FROM: between R1 COMMODITY PRICE-TAKER and R2 COST-ADVANTAGED CONVERTER. Pricing power weak (B04). ROCE 7.98% on the stage convention, 10.2% under the screener convention (B01). Operating EBITDA margin 7.42% in FY26 (B01).
- TO: R3 VALUE-ADDED / SPEC'D SUPPLIER. Management says it is moving "the portfolio up the value chain" (AR FY26 p.10, MD letter) and names recycling-compatible and food-contact grades (B07 optionality register). Spec-in approvals are candidates, unevidenced (B04).
- One rung in 2-3 years is the base rate. This claim is one rung.

**B2. The engine.** Two physical changes (B04, B05, B06):
1. Group plant loading: Select AZO products move from Frankfurt to Roha (AR FY26 p.9, Chairman letter). The parent says commodity products already moved to the Indian Heubach site in Roha (SUDARSCHEM Q4 FY26 p.10 via B06).
2. Operating leverage on a mostly fixed base of employee cost 71.10 and other expenses 177.44 (B04). Operating EBITDA margin 12.2% in H1 FY27 against 10.7% in H1 FY26 on revenue +25.0% (B04, B05).
Gross margin did not carry the gain: 39.3% against 41.7% in H1 FY27 (B04). The gain is cost leverage.

**B3. The proof gate.** All four must hold for two consecutive quarters (Q3 and Q4 FY27). Thresholds come from B05 triggers 1 to 3 and B04 must_track_metrics:
- Operating EBITDA margin at or above 12% and gross margin at or above 39.3%.
- H1 FY27 Reg 23 filing shows third-party sales growing, not only group sales.
- Q3 FY27 revenue above 222 (B05).
- CFO positive in H2 FY27, with inventory below 255.22 and receivables below 244.95 (Results Q2 FY27 p.4 via B05).
Until the gate fires the transition is narrative. This is what FTTCP tests.

**B4. The recognition gap (open question for Stage 11).** Does the TO state, R3, already look reflected in market pricing? This file does not conclude. Stage 11 confirms or denies it through the PE gap. If TO is already reflected, the re-rating engine is gone and only earnings growth remains.

**B5. The ugliness test.** Classification on the evidence held: **STRUCTURAL-FEATURE**, provisional.
Ugly optic: cash conversion down (OCF 110.59 to 34.24 to minus 24.11 in H1 FY27, B01), thin margins, group dependence, overdue payables (B02).
Evidence for ARTIFACT-OF-CLIMB: H1 FY27 revenue +25.0% and margin up (B05); the parent says it raised inventory in subsidiaries for longer logistics (SUDARSCHEM Q1 FY27 p.4 via B06), which fits the H1 FY27 build; ROCE is depressed by surplus cash, not by operating collapse (B01).
Evidence for STRUCTURAL: the FY26 working capital build came on falling sales (net trade WC 169.21 vs 126.05, revenue minus 5.4%, B02); third-party revenue was flat (589.23 vs 590.15) (B03); revenue CAGR minus 2.5% over nine years (B01); FY25 OCF and FY26 OCF each carried a one-time release (B02). No unwind has been observed yet.
The observation that reclassifies it: inventory and receivables unwind in H2 FY27 while third-party sales grow (B05). No trade verdict here.

**B6. The transition falsifier** (kills the arrow). Any of (B05 kill signals, B03 monitorables):
- Growth sits only in group sales.
- Q3 FY27 revenue falls back toward 175-211.
- Gross margin below 39% while other expenses grow faster than revenue.
- Inventory above 255.22 or CFO still negative at FY27 year end.

### PART C: WHAT THE MODEL WATCHES

**C1. Dominant variables** (become the Role 5.5 tracker signals):
1. Third-party versus group revenue split. State: FY26 group 191.40 (24.5%), third-party 589.23 vs 590.15; H1 FY27 split NOT FOUND (B03, B05).
2. Gross and operating margin against group purchases. State: gross margin 39.3% FY26, operating EBITDA 7.42%; group purchases 159.15 = 32.0% of purchases vs 16.6% (B02, B04). Peer EBITDA margin median 8.17% (B12a corrected); peer gross margin proxy median 39.00% (B12a corrected), company 39.26%.
3. Working capital and cash conversion. State: H1 FY27 CFO minus 24.11, inventories 255.22, receivables 244.95, payables 276.89 (B01); overdue payables 62.32 (37.5%) in FY26 (B02).
4. Domestic end-market volume against the Chinese price floor. State: domestic revenue +3.6% (574.45 vs 554.24) (B03); industry growth 3-4%, plants at 39-51% utilisation at MOL (B06); India market growth 4.1% (B09).

**C2. What the model rejects.**
- Market size questions. India SAM is Rs 8,183 Cr and the company holds 7.2% of it (B09). Headroom is 13.9x on paper. The binding constraint is group allocation and execution, not market size.
- Headline ROE and ROCE as a quality read. Cash 235.37 sits in net worth 570.08, and the convention moves median ROCE from 7.98% to 10.2% (B01, B04).
- The 1-Oct-2026 inter-se transfer as a minority signal. The promoter group stayed at 70.26% (B05); no merger, delisting or scheme text exists (B08).
- Consolidated peer margin comparison with SUDARSCHEM. Its FY26 figures include the acquired Heubach business (B01).

**C3. The business falsifier** (kills the starting business description, separate from B6). Evidence that forces a re-declaration of the FROM business: the H1 FY27 or FY27 related-party disclosure shows third-party revenue falling while group sales rise above 24.5% and group purchases rise above 32.0%. Then the entity is a toll node of the parent, and the archetype becomes Outsourcing partner for the whole business. A merger, delisting or amalgamation scheme text would also force a re-declaration (none found, B08).

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE (draft; Stage 13 holds the final)

The company makes organic and inorganic colour pigments and pigment preparations, a powder or paste that gives paints, plastics and printing inks their colour (B01, B04). It reports one segment, Pigments, and sells goods of 750.11 and services of 24.83 on revenue of 780.63 in FY26 (B04). Of that revenue, third-party goods are 71.6%, goods sold to the promoter group are 24.5% and services are 3.2% (B04). The run did not establish volume, capacity, utilisation or revenue by end market (B04), so why a customer cannot easily do without a given grade rests on management claims of spec-in approvals in automotive coatings and EPA-registered products, which stay unevidenced (B04).

The customers are over 100 domestic customers plus group affiliates abroad (AR FY26 p.17 via B04). India is 574.45 of revenue and outside India 200.49 (B03). Singapore SLO alone takes 137.25, or 17.6% of revenue, and three group affiliates take 177.54 of the outside-India revenue (B07, B09). No top-customer share is disclosed (B04). Buying behaviour, qualification cycles and switching costs are not documented in the corpus.

Demand exists because coatings, plastics and inks need colour. Coatings are the largest named application (B09). The present demand driver is a recovery from customer destocking, with peers reporting price-led growth, industry growth of 3-4% and plant utilisation of 39-51% (B06). The downstream signals that carry this are Indian paint makers' volume growth, plastics, packaging and printing ink producer demand, Asahi Songwon pigment utilisation and margin commentary, and the Sudarshan Chemical consolidated results and half-yearly related-party filing (B09).

Demand should grow on three drivers, each tied to a signal. First, the India market grows 4.1% a year (B09), observable through the paint-maker, ink and plastics filings above. Second, automotive and EV production lifts pigment use per vehicle (AR FY26 p.19 via B09), observable through monthly industry association data. Third, anti-dumping duty of 20-30% on Chinese Azo shifts share to Indian makers (ASAHISONG via B06, B09), observable in DGTR orders and Chinese export prices. Management also names recycling-compatible and food-contact grades and a localised HP Azo range, with no capex, volume or revenue given (B07). The group adds a fourth route that the filings cannot yet split: AZO and commodity products moving into Roha from Frankfurt (B06).

The competitive advantage sits nowhere that the run could confirm. Gate 0 scores zero moats (class NONE) and the Emerging Moat scan scores 9.9, class NONE (B01, B07). The third-party pigment line has no confirmed moat; gross margin is 39.26% against a corrected peer proxy median of 39.00% and operating EBITDA margin 7.42% against a corrected peer median of 8.17% (B12a, B01). The group-allocated line has no moat of its own; its volume lasts while the parent keeps loading the plants (B04). One moderate emerging item is the parent group platform, a management claim of procurement leverage and a 500+ product portfolio (B07). The group purchases rose to 32.0% of purchases while gross margin fell, so the leverage claim is not yet visible in the numbers (B02, B04).

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. Verticals framed

**Vertical 1: Third-party versus group revenue split.**
- Establishes: group goods sales 191.40 of 780.63 (24.5%); third-party 589.23 vs 590.15; USA SLO 77.42 to 20.99; group sales explain 97.9% of the FY26 revenue fall (B03). H1 FY27 revenue 492.15 vs 393.86 (+25.0%) and Q2 FY27 269.76 vs 183.14 (+47.3%) (B05).
- Cannot establish: group share of H1 FY27 revenue; any filed explanation of the Q2 FY27 jump; capacity and utilisation (B05, B06).
- Deciding questions: (1) What share of H1 FY27 revenue of 492.15 came from group entities? (2) Did third-party sales grow, or only group sales? (3) Did sales to Singapore SLO and USA SLO move by transfer decision?

**Vertical 2: Margin against group purchases.**
- Establishes: gross margin 39.3% vs 42.2% (FY26 vs FY25); group purchases 159.15 vs 80.72, HLD1 99.62 vs 45.38; royalty 1.61; services from Germany Horizons 9.49 (B02, B12b B-02). H1 FY27 operating EBITDA margin 12.2% (60.07 on the corrected PBT 59.67) (B12a). Inventory build of FG/WIP/SIT 44.66 vs 25.67 sits inside H1 FY27 margin; overhead absorbed NOT FOUND (B12b B-03).
- Cannot establish: margin by party; transfer pricing basis (Note 40 asserts "normal commercial terms and conditions and at market rates", no study) (B03).
- Deciding questions: (1) Why did gross margin fall in H1 FY27 while peers passed costs through? (2) How much of the 99.62 bought from HLD1 is traded goods resold? (3) How much overhead sits in the 44.66 inventory build?

**Vertical 3: Working capital and cash conversion.**
- Establishes: H1 FY27 CFO minus 24.11; inventory +99.07, receivables +69.77, payables +111.71; net trade WC 223.28 vs 169.21 (derived) (B05). FY26 overdue payables 62.32 (37.5%) vs 1.24; group payables 43.87; cash 235.37 (B02). FY26 OCF carried a release of government-authority balances of 20.53, giving OCF 13.71 without it (B12a corrected; the three-line sum is 24.76).
- Cannot establish: ageing of the 43.87 group payables; nature of government balances; H1 FY27 payables split (B03).
- Deciding questions: (1) Are overdue third-party payables and group payables the same money? (2) Does inventory unwind in H2 FY27? (3) Does CFO turn positive in H2 FY27?

**Vertical 4: Domestic end-market volume against the Chinese price floor.**
- Establishes: domestic revenue 574.45 vs 554.24 (+3.6%) (B03); coatings the most stable line per MD letter; India TAM growth 4.1%, SOM implied growth 10.9% over 3 years (B09); peers cite 3-4% industry growth and pass-through pricing (B06).
- Cannot establish: end-market split, volume, realisation per kg, customer concentration (B04).
- Deciding questions: (1) Do paint makers report volume growth in the Q2 and Q3 FY27 filings? (2) Does the 20-30% duty on Chinese Azo move Indian share? (3) Do Chinese export prices set the floor?

### 4b. Candidate signal table (UNVERIFIED; verification at Role 5.5 in claude.ai)

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| Indian paint makers' volume growth (Asian Paints, Berger, Kansai Nerolac) | Two consecutive quarters of flat or negative decorative and industrial volume | Quarterly | Exchange filings and concall transcripts of listed paint makers (B09) |
| Automotive and EV production volumes | Monthly production below prior-year for three months running | Monthly | SIAM industry association data (B09) |
| Plastics, packaging and printing ink producer demand | Ink and masterbatch makers report volume decline or destocking restart | Quarterly | Listed ink and masterbatch makers' filings and concalls (B09) |
| Sudarshan Chemical consolidated results and half-yearly related-party filing | Group share of SUDARCOLOR sales above 24.5% or purchases above 32.0% with third-party sales flat | Quarterly | Exchange filings, Reg 23 disclosure, parent concalls (B09) |
| Anti-dumping or safeguard orders on Chinese pigments | Duty lapses, is not renewed, or is cut | Event-Driven | DGTR findings and Ministry of Finance customs notifications (B09) |
| Chinese pigment export prices and India pigment import volumes | Chinese prices fall while Indian gross margin is below 39.3% | Monthly | Ministry of Commerce DGCIS trade data; industry notes (B09) |
| Asahi Songwon pigment utilisation and margin commentary | Utilisation stays at or below the 39-51% band cited in the peer set with falling margin | Quarterly | Exchange filings and peer concall transcripts (B09) |

Likely sources are B09's. Role 5.5 checks each against Downstream_Source_Discovery_Protocol_v1_0 in claude.ai.

### 4c. Fragility read

- variable_count: 5. (1) Group allocation of volume. (2) Domestic end-market volume. (3) Input-cost pass-through against gross margin. (4) Working capital unwind. (5) Chinese price floor and duty status.
- verifiability_ratio: 3 of 5 externally observable. Observable: domestic end-market volume (paint-maker and ink filings), input-cost pass-through (peer filings and calls), Chinese price floor and duty (DGCIS, DGTR). Company-narrated or company-filed only: group allocation (Reg 23 filing is the company's own; parent calls are interested-party, B06) and working capital unwind (company balance sheet).
- single_point_failure: Group allocation of volume. The parent sets plant loading and sourcing, and group sales are 97.9% of the FY26 revenue fall (B03).
- fragility_verdict: **FRAGILE** (one kill-switch variable, and the key variable is company-narrated).

### 4d. Research brief (claude.ai work order)

1. PENDING LIVE VERIFICATION (Chain 1, Link 2): open the SUDARCOLOR H1 FY27 Reg 23 related-party disclosure on BSE and NSE. Read sales and purchases by group entity and the outstanding balances.
2. PENDING LIVE VERIFICATION (Chain 2, Link 2): open the same Reg 23 filing's balance table and the parent's consolidated H1 FY27 results. Find the ageing of group payables and whether the overdue 62.32 and the group payables 43.87 are the same money.
3. Build Chain 3 (end-market demand): trace paint-maker and ink-maker H1 FY27 volume to pigment offtake, with filings opened.
4. Build Chain 4 (cost and margin): trace input-cost pass-through (Chinese export prices, DGCIS data, duty status) to SUDARCOLOR gross margin.
5. Build Chain 5 (control and minority): trace the 1-Oct-2026 inter-se transfer and the staged plan in the Reg 10(7) report to float headroom of 4.74 points over the 25% floor (B08).
6. Read the parent's (SUDARSCHEM) Q2 FY27 call when filed: group role, Roha and Cuddalore loading, intercompany business, cash path.
7. Counterparty health of Sudarshan Singapore SLO and Sudarshan USA SLO, from the parent's segment and consolidated filings.
8. Policy status: DGTR and Ministry of Finance notifications on the 20-30% duty on Chinese Azo; verify source URLs.
9. Exchange shareholding pattern as filed (BSE): confirm the pledge or encumbrance line and the institutional holding series (0.71% at Dec 2025, 11.38% at Sep 2025) (B12a).
10. Forum archaeology: Bombay High Court status of the Rs 25.49 Cr service tax matter (nil paid), the Tamil Nadu GST order of 11-Sep-2026, and the Maharashtra GST search outcome. NSE filing bodies were not read (B08).
11. Governance: the permanent CFO appointment, the whistle-blower complaint content, the Note 50 accounting effect, and the Letter of Offer computation section (B08, B03).
12. Source URL verification for web-sourced figures in B08 and B09 (IMARC and Ken Research market definitions, FX basis, media-tier items) and the SUDARSCHEM guidance record flagged by Verifier B (B12b B-04).

### 4e. Second-Order stub (Master v3.7 Rule F)

**CHAIN 1: FY26 group sales explain 97.9% of the revenue fall: group sales 191.40 of 780.63, USA SLO 77.42 to 20.99, third-party 589.23 vs 590.15 (B03, B02 rank 6)**
- Link 1 [VERIFIED, AR FY26 Note 40 pp.92-93 via B03]: Group affiliates take 24.5% of sales. The FY26 revenue fall of 44.43 sat in group sales (43.51). Third-party revenue did not fall.
- Link 2 [PENDING LIVE VERIFICATION]: Who pays, and why now. The paying parties are Sudarshan Singapore SLO (137.25), Sudarshan USA SLO (20.99) and Shanghai (19.30) (B02). Why the group moved volume in FY26 and loaded Roha in H1 FY27 needs counterparty evidence this container cannot reach. Claude web should open the SUDARCOLOR H1 FY27 Reg 23 related-party filing (BSE/NSE) and SUDARSCHEM's Q2 FY27 concall transcript and consolidated results. Not drafted from memory.
- Link 3 [INFERENCE]: Q2 FY27 materials consumed rose 113% (159.91 vs 74.94) while revenue rose 47% and stock-in-trade purchases fell to 25.85 from 30.80 (B05, B07). That pattern fits manufacturing replacing trading. The parent says Frankfurt products moved to the Indian Heubach site in Roha and that it gained intercompany business (SUDARSCHEM Q1 FY27 p.12 via B06). So part of the +47.3% quarter may be group-allocated production loaded onto Roha at transfer prices, and revenue growth may not equal third-party demand.
- Binding constraint (corpus): capacity and utilisation are NOT FOUND (B04, B07). Plant and equipment additions were 15.96 vs 7.25 and capex 25.34 vs depreciation 16.51 in FY26 (B03, B05). CWIP is 12.84 at Sep-26 (B07). Capital commitments not provided for are 3.87 (B03). Inventory 255.22 and receivables 244.95 at Sep-26 hold the incremental volume (B01).
- Unsaid: the MD letter blames market softness and destocking, while Note 40 puts the fall in group offtake (B05). The MD risk table omits group dependence, and Note 40 gives no transfer pricing study (B03). No filing explains the Q2 FY27 revenue jump, and the results carry no related-party split (B05). Five of eight directors also sit on the parent board (B08).
- Observation that confirms or breaks this chain, and confirm-by date: the H1 FY27 Reg 23 split of group versus third-party sales, by 2026-12-31 (fallback Q3 FY27 results, Jan-Feb 2027, B07). Confirms (demand reading): group share of H1 FY27 revenue 492.15 at or below 24.5% with revenue +25.0%. Breaks (re-routing reading): group share above 24.5% with third-party sales near flat at 589.23 annualised.

**CHAIN 2: H1 FY27 operating cash flow of minus 24.11 against profit before tax of 59.67; inventories +99.07, receivables +69.77, payables +111.71 (Results Q2 FY27 pp.4-5 via B05; PBT per B12a)**
- Link 1 [VERIFIED, Results Q2 FY27 p.5 via B05, B02]: Profit grew while cash left. Payables rose by more than inventory alone. In FY26, overdue trade payables were 62.32 (37.5%) against 1.24 a year before, with cash and bank of 235.37 (B02). Group payables were 43.87 and group purchases 159.15 (B02).
- Link 2 [PENDING LIVE VERIFICATION]: Who pays, and why now. Whether suppliers or the group financed the build needs the group payable ageing and the parent's stated working capital direction. Claude web should open the SUDARCOLOR H1 FY27 Reg 23 filing (balance table) and SUDARSCHEM's Q2 FY27 call and consolidated H1 FY27 results. Not drafted from memory.
- Link 3 [INFERENCE]: Payables rose 111.71, more than the inventory rise of 99.07 (B05). With group purchases at 32.0% of purchases and group payable days of about 100.6 (B02), the build may be financed by group credit. Then the negative CFO is timing, not cash loss. If instead the overdue 62.32 sits with third parties, the company stretches suppliers while holding idle cash, and the build is a supply chain cost rather than group-financed timing (B02 analyst note).
- Binding constraint (corpus): cash and bank plus investments fell to 206.11 (derived) with no borrowings (B05, B02). The first interest under Section 16 of the MSME Act was 0.32 (B02). Contingent liabilities are 50.76, 8.9% of net worth (B01). FY25 OCF carried a 34.50 working capital release and FY26 OCF a government-balance release of 20.53 (B02, B12a), so neither year is a clean run rate.
- Unsaid: MD&A lists "optimize net working capital" as strategy, not as a risk (B03). Ageing of group payables is NOT FOUND (B03). The nature of the government balances is undisclosed (B02). No dividend since FY21 despite net cash 212.39 (B02, B08).
- Observation that confirms or breaks this chain, and confirm-by date: by 2027-05-31 (Q4 FY27 filing window Apr-May 2027, B07). Confirms (timing): CFO positive in H2 FY27, inventory below 255.22 and receivables below 244.95 at 31-Mar-2027 (B05). Breaks: inventory above 255.22 or CFO still negative at FY27 year end, or overdue payables above 62.32 in FY27 Note 19 (July 2027) (B03).

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in claude.ai with live web, before Role 2.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. The company makes colour pigments. Paint, plastic and ink makers use them (B04).
2. It has three plants, at Roha, Cuddalore and Nagda. It has no debt and holds cash of 235.37 Cr (B03).
3. It was Heubach Colorants India. The Sudarshan Chemical group took control in 2025, and the group now holds 70.26% (B08).
4. About 72% of sales go to outside customers. About 24.5% go to sister companies of the group (B04).
5. Sister companies also supply about 32% of the raw material and traded goods the company uses (B02).
6. Demand comes from paints, plastics and inks. Peers say industry growth is about 3-4% and plants are not full (B06).
7. Revenue fell 5.4% in FY26 and then rose 25.0% in the first half of FY27 (B05). The filings do not say how much of that came from group customers.
8. The FY26 fall came from group sales. Outside-customer sales stayed flat at 589.23 against 590.15 (B03).
9. The run found no moat. Gate 0 scores zero moats and the Emerging Moat scan scores 9.9 (B01, B07).
10. The model in one line: a group-run pigment node tries to climb from a thin-margin supplier to a value-added supplier, and the proof is outside-customer growth, a steady margin of 12% and positive cash flow (B05).
11. The fragility verdict is FRAGILE. Five outside variables must go right, three can be watched from outside, and one variable (group allocation) can break the thesis alone (Section 4c).
12. The company has not shown that profit turns into cash. Operating cash flow went from 110.59 to 34.24 to minus 24.11 in H1 FY27 (B01).
13. The corpus has no company concall, no presentation, no rating and no pledge line. The group's related-party filing for the first half of FY27 is missing, and it is the filing that matters most (B00, B05).
14. Some numbers in earlier reports were corrected by checking. Examples: first-half FY27 PBT is 59.67, and the peer EBITDA margin median is 8.17%, so the company is 0.75 points below it, not 2.2 points (B12a).
15. Biggest open questions: What share of first-half sales came from the group? Do the overdue payables of 62.32 and the group payables of 43.87 hold the same money? Does the build in inventory and receivables unwind in H2 FY27? (B03, B05)

---

## SECTION 6: STANDING EXTRACTION ANNEX

File anchors use the page-marked .txt beside each PDF ("[page N]" markers). AR FY26 means inputs/annual-report/Annual_Report_2026.pdf. Q2 FY27 means inputs/results/Results_Q2FY27_Sep2026.pdf.

### 1. UNITS

No per-unit figure (realisation per kg, price per tonne) is printed. Quote: "Sale of Goods - “Pigments” 750.11 791.48 / Sale of Services 24.83 26.56 / Total Revenue from contracts with customers 774.94 818.04" (AR FY26 p.94, Note 41(b), Rs Crores). Quote: "Revenue from operations 269.76 222.39 183.14 492.15 393.86 780.63" (Q2 FY27 p.3, Rs Crores). Basket: the single product category "Pigments" covers organic and inorganic pigments and preparations across all applications (Q2 FY27 p.6 note 3). Volume (kg or tonnes) and capacity are NOT DISCLOSED in the AR or results (B04, B07). A per-kg figure cannot be derived. The only derivable unit is Rs 100 of revenue: materials and traded goods net of inventory change Rs 60.7, gross Rs 39.3, operating EBITDA Rs 7.4 (B04). Comment: the pipeline's unit is the rupee of revenue, not a physical unit.

### 2. SEGMENT CAPITAL AND DEBT

Quote: "The Chief Operating Decision Maker (“CODM”) reviews the operations of the Company as a whole under single primary business segment “Pigments”, hence there are no reportable segments as per Ind AS 108" (AR FY26 p.94, Note 41(a); same text Q2 FY27 p.6 note 3). Segment assets, liabilities and capital employed by segment: NOT DISCLOSED, because there is one segment. Company totals, latest two periods (Q2 FY27 p.4): total assets 953.62 (30-09-2026) vs 804.83 (31-03-2026); equity 614.04 vs 570.08; current liabilities 307.62 vs 203.35. Borrowings: none. Debt in AR FY26 p.96 is defined as lease liabilities: "Debt= Lease Liabilities ... 22.98" (Mar-26), and lease liabilities at Sep-26 are 18.97 non-current plus 2.79 current (Q2 FY27 p.4). Comment: no debt is allocated by segment; leases are the only debt.

### 3. GUIDANCE VERSUS ASPIRATION

| Item | Quote (filename, page) | Class |
|---|---|---|
| Return to growth | "supported by new account wins and an expanded portfolio via the ONE Sudarshan group" (AR FY26 p.10, MD letter) | (b) aspiration; "through FY2027" stated for demand, no number |
| Destocking and demand | "The destocking cycle has largely run its course, and domestic demand, particularly in coatings and plastics, is expected to strengthen through FY2027" (AR FY26 p.10) | (a) direction with a period, no number |
| Printing inks | "We expect this to ease as inventory positions normalize through FY2027" (AR FY26 p.10) | (a) direction with a period, no number |
| HP Azo localisation | "expected to unlock new export opportunities FY2027 onward" (AR FY26 p.10) | (b) aspiration, no number |
| Three-year horizon | "with a three-year horizon rather than a quarterly one ... accepting near-term margin pressure" (AR FY26 p.10) | (b) aspiration, no number |
| Cost and utilisation | "disciplined cost reduction, and improved capacity utilization across our facilities" (AR FY26 p.9, Chairman letter) | (b) aspiration, no number |
| Gratuity contribution | "expects to contribute ₹2.50 Crores ... to the funded gratuity plans in the next year" (AR FY26 p.92) | (a) guidance with a period (FY27) |
| Capital commitments | 3.87 not provided for (AR FY26 Note 35 p.90 via B03) | (c) capacity commitment only |
| Growth above GDP over three years | recorded in B05 as AR FY25 MD letter p.10 (wording not re-read for this annex) | (b) aspiration, no number |
| Renewable usage above 65% | recorded in B05 as AR FY25 MD letter p.10 (wording not re-read) | (b) aspiration |
| Dividend, debt, capex, capacity, return goals | NOT DISCLOSED; B05 finds no numeric revenue, margin, capex, capacity or dividend guidance | n/a |

Comment: the only forward numbers are small funding figures. There is no revenue or margin number.

### 4. CONCENTRATION

- Product: single category. "Sale of Goods - “Pigments” 750.11" of 774.94 contract revenue (AR FY26 p.94). Top product share: NOT DISCLOSED (no product-line split).
- Customer: no major-customer disclosure (B04). Group counterparties as printed: Sudarshan Singapore SLO sales of goods "137.25" (AR FY26 p.93); Sudarshan USA SLO "20.99" vs "77.42"; Shanghai "19.30". Top single customer is Singapore SLO at 137.25, 17.6% of revenue 780.63 (B07). Third-party top customer share: NOT DISCLOSED. AR p.17 says only "serves over 100 domestic customers" (AR FY26 p.17 [page 17 text]).
- Geography: "India 574.45 554.24 / Outside India 200.49 263.80" (AR FY26 p.94). Of outside-India revenue, 177.54 goes to three group affiliates (B09).
Comment: group affiliates are the only named concentration.

### 5. PROMISE LEDGER

Rows B12b ruled unsupported or misclassified (B-09, B-12, B-14) are dropped. Dates are the AR cover-letter dates (AR FY25 2025-09-05; AR FY26 2026-07-27).

| Promise | Made | Status | Evidence anchor |
|---|---|---|---|
| Return to growth in FY2027 | AR FY26 MD letter p.10, 2026-07-27 | Interim: H1 FY27 +25.0%; full year open; group split NOT FOUND | Q2 FY27 p.3 (492.15 vs 393.86) |
| Cost reduction and better utilisation lift profitability in FY2027 | AR FY26 p.9, 2026-07-27 | Interim, quality unverified: operating EBITDA margin 12.2% vs 10.7%; inventory build 44.66 vs 25.67 inside margin; overhead absorbed NOT FOUND | Q2 FY27 pp.3-4; B12b B-03 |
| Over 65% renewable usage at Roha and Cuddalore | AR FY25 MD letter p.10, 2025-09-05 (via B05) | Partial: FY26 total 58% (AR FY26 p.9); no combined 65% | AR FY26 p.9 |
| Grow above GDP over three years | AR FY25 MD letter p.10, 2025-09-05 (via B05) | Partial: FY26 revenue 780.63 vs 825.06; H1 FY27 +25.0% | Q2 FY27 p.3; AR FY26 p.96 |
| Strategic investment in capacity optimisation | AR FY25 MD letter p.10 (via B05) | Partial: capex 25.34 vs depreciation 16.51 in FY26; no capacity or utilisation figure | AR FY26 p.~82 via B05 |
| Gratuity contribution 2.50 | AR FY25 and FY26 | Partial: FY26 actual 6.82 | AR FY26 pp.91-92 via B03 |
| Optimise net working capital | AR FY26 p.18 strategy | Missed: net trade WC 169.21 vs 126.05; H1 FY27 CFO minus 24.11 | AR FY26 p.18 via B03; Q2 FY27 pp.4-5 |
| Complete integration to unlock synergies and deliver high returns | AR FY25 MD letter p.10 (via B05) | Missed to date: FY26 ROE 8.15% vs 10.33%; no return figure filed for H1 FY27 | AR FY26 p.96 ratio table |

Also on record (not a promise): the MD letter says "Outside the US, markets grew 7%" (AR FY26 p.10) while outside-India revenue fell 24.0% and ex-USA SLO fell 3.7% (B03). B12b B-01 lists this with three other letter numbers that do not reconcile.

### 6. RESTATED BASES

Quote, Note 54: "Until March 31, 2025, the Company’s Ind-AS Financial Statements were presented in Indian Rupees (₹) with values rounded off to the nearest Lakhs ... henceforth, all amounts in these financial statements for all periods presented will be rounded off to the nearest Crores" and "It does not affect the recognition or measurement of any items" (AR FY26 p.97). That is a presentation change only. No restatement for reorganisation, transfer or reclassification is stated. Note 44(vi): "The Company has not entered into any scheme of arrangement which has an accounting impact in the current or previous financial year." (AR FY26 p.94). Comparative as printed in the latest filing: FY26 revenue from operations "780.63" vs "825.06" (AR FY26 p.96 ratio table; Q2 FY27 p.3 shows 780.63 for the year ended 31-03-2026). B02 also records that the FY25 deferred tax movement table does not foot (1.30 vs 0.99, Note 18 p.86). Comment: bases are comparable; the Airoli transfer (Note 50) is unresolved in book effect (B02).

### 7. CORPORATE-ACTION CLAUSES

Scheme, demerger, merger, preferential issue, buyback: none in the corpus. Quote: "The Company has not entered into any scheme of arrangement which has an accounting impact in the current or previous financial year." (AR FY26 p.94 Note 44(vi)). No merger or delisting text found anywhere (B08).

Open offer and promoter transfers (the corporate actions on record):
- Quote (AR FY26 p.97, Note 48): "On October 11, 2024, Sudarshan Europe BV (“the Acquirer”) ... entered into a purchase agreement to acquire all shares held by the promoters in the Company"; "Open Offer for the acquisition of up to 6,001,268 fully paid equity shares ... representing 26%"; Detailed Public Statement "dated March 08, 2025" and Letter of Offer "dated September 01, 2025"; "The Acquirer directly acquired 36,68,036 (15.89%) equity shares ... promoter and promoter group ... now holds 70.25%". Acquisition of indirect control completed 3 March 2025 at 54.36%.
- Quote (Q2 FY27 p.6 note 10): "On October 01, 2026 ... Sudarshan Chemical Industries Limited ... acquisition of 36,68,036 equity shares (representing 15.89% ...) from Sudarshan Europe B.V. ... for an aggregate consideration of Rs 150.76 crores (amounting to Rs 411/- per equity share) ... internal restructuring ... did not result in any change in the aggregate shareholding of the Promoter and Promoter Group ... 70.26%". Open offer price Rs 602.03 is recorded in B08 (web-sourced, Letter of Offer not read).
- Definitions of any undertaking and liability allocation clauses: not applicable, no scheme. Appointed and effective dates: 2025-03-03 (control), 2025-10-03 (open offer completion), 2026-10-01 (inter-se transfer).
- Filings to fetch: the Reg 10(7) report (2026-10-19), the SAST Reg 29(2) disclosures (2026-10-01) and the Letter of Offer, all on BSE. The first three scanned filings carry no usable text layer (B00). Verifier B reads the 10(7) report as a staged plan with a residual overseas holding (B12b B-08, partly inference).

### 8. RELATED-PARTY PERIMETER

Latest year FY26, Rs Crores, as printed (AR FY26 pp.92-93, Note 40). Quote: "All transactions were made on normal commercial terms and conditions and at market rates." (p.93).

| Entity (relationship) | Nature and amount, FY26 vs FY25 |
|---|---|
| Sudarshan Switzerland HLD1 AG (principal shareholder) | Purchase of goods 99.62 vs 45.38; indenting commission received 0.47 vs 0.92; royalty expenses 1.61 vs 1.71; services rendered 0.06 |
| Sudarshan Chemical Industries Limited (ultimate holding company) | Sale of goods 10.15 vs nil; purchase of goods 0.16; services rendered 0.13 |
| Sudarshan Europe B.V. (principal shareholder) | Services received 0.07 |
| Sudarshan Singapore SLO Pte. Ltd. | Sales of goods 137.25 vs 132.83; purchases 4.67 vs 6.70 |
| Sudarshan USA SLO LLC | Sales of goods 20.99 vs 77.42 |
| Heubach Colorants (Shanghai) Ltd. | Sales of goods 19.30 vs 19.37 |
| Heubach Colorants Pigment Preparations (Tianjin) Ltd. | Sales of goods 2.37 vs 1.65; services rendered 0.09 |
| Sudarshan Gujarat MFG Private Limited | Sales 0.80 vs 1.48; purchases 40.95 vs 22.70; services received 0.18 |
| Sudarshan Langelsheim PLT GmbH | Purchases 12.34 vs 0.54 |
| Sudarshan Germany Horizons GmbH | Services received 9.49 (nil FY25); purchases 0.14; services rendered 1.67 |
| Sudarshan Brasil MFG Ltda. | Sales of goods 0.54 |
| Sudarshan Mexico MFG, SA de C.V. | Purchases 0.26 vs 0.18 |
| Hangzhou Baihe Heubach Pigments Co. Ltd | Purchases 1.01 |
| Sudarshan Japan MFG K.K. | Sales nil vs 2.16 |
| Key management personnel | Executive directors total remuneration 6.49 vs 5.89; company secretary 0.19 vs 0.73 |

Balances at year end (p.93): principal shareholders trade payables 21.58 vs 5.44, receivables 6.79 vs 0.43; fellow subsidiaries payables 22.29 vs 13.40, receivables 49.77 vs 44.87; KMP payable 0.58. Other entities named in the list with no FY26 amount shown: Sudarshan Southern Africa, Sudarshan Fairless Hills (balances only). Comment: Clariant India Pvt Ltd is called a related party in Note 50 (p.97) but is absent from Note 40 (B02). Group sales total 191.40 (24.5%); group purchases 159.15 (32.0%) (B02).

### 9. PLEDGE AND SHAREHOLDING

Source: inputs/shareholding/screener-shareholding-2026-11-12.md, screener copy of exchange filings, not the filing itself. Percentages as printed.

| | Dec23 | Mar24 | Jun24 | Sep24 | Dec24 | Mar25 | Jun25 | Sep25 | Dec25 | Mar26 | Jun26 | Sep26 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Promoters | 54.37 | 54.37 | 54.37 | 54.37 | 54.37 | 54.37 | 54.37 | 54.37 | 70.26 | 70.26 | 70.26 | 70.26 |
| FIIs | 0.31 | 0.34 | 0.37 | 0.42 | 0.43 | 1.15 | 1.81 | 1.28 | 0.20 | 0.19 | 0.16 | 0.14 |
| DIIs | 1.28 | 1.92 | 3.24 | 3.71 | 8.53 | 10.62 | 9.16 | 10.10 | 0.51 | 0.51 | 0.51 | 0.51 |
| Public | 44.05 | 43.37 | 42.03 | 41.51 | 36.67 | 33.87 | 34.67 | 34.26 | 29.03 | 29.04 | 29.10 | 29.11 |

Promoter pledge: NOT FOUND. The screener file says "Pledge data is not in this table: NOT FOUND." AR FY26 p.66 has the pattern with no pledge line (B03). Media items state nil encumbrance (media tier, single source, B08). Institutional holding latest (Sep 2026): FII 0.14 plus DII 0.51 = 0.65 (derived). At Dec 2025 it was 0.71 (0.20 + 0.51), down from 11.38 at Sep 2025 (1.28 + 10.10) (B12a corrected). Shares: 2,30,81,798 (AR FY26 p.66, Note 15 p.86). Public float 29.74% at the time of the B08 read, 4.74 points above the 25% floor (B08). The promoter rise from 54.37% to 70.26% is the open offer, not market buying (AR FY26 p.97).

### 10. VERIFICATION

Documents quoted, with filename and date:
- inputs/annual-report/Annual_Report_2026.pdf, FY2025-26, cover letter 2026-07-27
- inputs/annual-report/Annual_Report_2025.pdf, FY2024-25, cover letter 2025-09-05 (cited via B05 only)
- inputs/results/Results_Q2FY27_Sep2026.pdf, outcome letter 2026-10-28
- inputs/results/Results_Q1FY27_Jun2026.pdf, outcome letter 2026-08-05 (cited via B05)
- inputs/results/Results_Q4FY26_Mar2026.pdf, outcome letter 2026-05-11 (cited via B12b)
- inputs/shareholding/screener-shareholding-2026-11-12.md, read 2026-11-12
- inputs/announcements/ (7 PDFs, 2026-09-01 to 2026-10-28; scanned ones not read by text)
- Peer transcripts (SUDARSCHEM, MOL, ASAHISONG) cited via B06, call dates 2024-11-06 to 2026-11-05

CORPUS COMMIT HASH: 20ac48b61db04be4f578bb3d6c45d0631a113788

---

```yaml
stage: B09b-dossier
company: "SUDARCOLOR"
run_date: "2026-11-12"
model: claude-sonnet-5-5
status: complete
corpus_verdict: "CORPUS GAPPED"
corpus_gaps:
  - document: "Any company concall transcript (Q2 FY27 call or earlier); company holds none, web search at /step1 found none"
    expected_source: "company IR page"
    kind: "plausibly-nonexistent"
  - document: "Investor presentation (any quarter)"
    expected_source: "company IR page"
    kind: "plausibly-nonexistent"
  - document: "Credit rating rationale (AR FY26 p.67 item 19: no rating sought)"
    expected_source: "rating agency site"
    kind: "plausibly-nonexistent"
  - document: "H1 FY27 Reg 23 related-party filing (group share of sales, purchases, receivables, payables)"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "Quarterly shareholding pattern as filed with pledge/encumbrance line (corpus holds a screener copy only)"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "Reg 30 announcements before 2026-09-01 (prior 12 months; collector limit)"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "Annual report FY2023-24 (third annual report; two held)"
    expected_source: "company IR page"
    kind: "findable-missing"
  - document: "Text versions of scanned SAST filings 6D1F3240, A16C6814 and C1DC7FB5 pages 1-5"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "Letter of Offer (open offer computation section)"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "SUDARSCHEM (parent) Q2 FY27 concall transcript"
    expected_source: "company IR page"
    kind: "findable-missing"
archetypes:
  - line: "Third-party pigment sales (71.6% of revenue, B04)"
    archetype: "Build-to-spec component maker (alternate reading open: Commodity converter, which would bind Amendment 17)"
  - line: "Group-allocated sales and services (24.5% goods plus 3.2% services, B04)"
    archetype: "Outsourcing partner"
transition:
  - line: "Pigments (single reporting segment)"
    from_tier: "R1 COMMODITY PRICE-TAKER edge of R2 (weak pricing power, ROCE 7.98% to 10.2% depending on convention, B01, B04)"
    to_tier: "R3 VALUE-ADDED / SPEC'D SUPPLIER (management claims a move up the value chain, AR FY26 p.10 via B05)"
    engine: "Group portfolio and plant loading (Frankfurt AZO to Roha, ONE Sudarshan accounts) lifting third-party and group volume over a mostly fixed cost base; operating EBITDA margin 12.2% H1 FY27 vs 10.7% H1 FY26 (B04, B05)"
    proof_gate: "Two consecutive quarters (Q3 and Q4 FY27) with operating EBITDA margin at or above 12% AND gross margin at or above 39.3% AND third-party revenue growing in the H1 FY27 Reg 23 split AND CFO positive in H2 FY27 (thresholds from B05 triggers 1-3)"
    recognition_gap: "OPEN QUESTION for Stage 11 via the PE gap: does the TO state already look reflected in market pricing? No conclusion here"
    ugliness: "STRUCTURAL-FEATURE"
    transition_falsifier: "Growth sits only in group sales, or Q3 FY27 revenue falls back toward 175-211, or gross margin below 39% while other expenses grow faster than revenue, or inventory above 255.22 / CFO still negative at FY27 year end (B05 kill signals)"
dominant_variables:
  - "Third-party vs group revenue split (group allocation of volume)"
  - "Gross and operating EBITDA margin vs transfer-priced group purchases"
  - "Working capital days and cash conversion (inventory, receivables, overdue and group payables)"
  - "Domestic end-market volume (paints and coatings, plastics, inks) vs Chinese price floor"
business_falsifier: "H1 FY27 or FY27 related-party disclosure shows third-party revenue falling while group share of sales rises above 24.5% and group purchases above 32.0%, so the entity is a toll node of the parent and must be re-declared Outsourcing partner; or any merger, delisting or amalgamation scheme text appears (none found, B08)"
mental_model_status: "DRAFT - PENDING OPERATOR SIGN-OFF"
fragility:
  variable_count: 5
  verifiability_ratio: "3 of 5 externally observable"
  single_point_failure: "Group allocation of volume: the parent sets plant loading and sourcing, and group sales explain 97.9% of the FY26 revenue fall (B03)"
  fragility_verdict: "FRAGILE"
candidate_count: 7
second_order:
  chains_drafted: 2
  pending_live_links: 2
  confirm_by_observations: 2
research_brief_items: 12
plain_summary_points: 15
annex:
  present: true
  questions_answered: 10
  corpus_commit_hash: "20ac48b61db04be4f578bb3d6c45d0631a113788"
```
