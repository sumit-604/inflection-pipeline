# CLEANMAX (Clean Max Enviro Energy Solutions Ltd) — HALT 1 UNDERSTANDING DOSSIER

Run date: 2026-09-01. Assembled from committed blocks B00-B09, verifier blocks B12a-B12d, confidence.yaml, B13-synthesis, and the phase-1 final files. No new research. No valuation. This is an understanding document, not a decision.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

**1. CONCALLS.** Three transcripts held: Concall_Mar_2026_Transcript.txt (Q3 FY26 results, quarter ended 31-Dec-2025), Concall_May_2026_Transcript.txt (Q4 FY26 / full FY26, year ended 31-Mar-2026), Concall_Aug_2026_Transcript.txt (Q1 FY27, quarter ended 30-Jun-2026, board meeting 31-Jul-2026) (B00, B05 quarters_analysed). Most recent quarter covered: Q1 FY27. Given the run date of 2026-09-01, Q2 FY27 (quarter ending 30-Sep-2026) has not yet closed, so no more-recent transcript is plausibly missing.

**2. ANNUAL REPORTS.** One AR held: FY2025-26 (16th AGM, dated 30-Jun-2026, 859pp) (B00). The latest completed FY (FY26, year ended 31-Mar-2026) is present. Fewer than 3 years of standalone ARs are held, because CleanMax listed in Feb-2026 (B00 `listed_within_3y: true`) and did not previously publish public annual reports; the RHP/Prospectus (dated 25-Feb-2026, 994pp) supplies restated financials back to FY21, giving 6 years of comparable data (B01 `data_years: 6, fy_range: FY21 to FY26`) even though only one bound AR document exists. This is the expected pattern for a RECENTLY-LISTED name, not a gap to remediate.

**3. RESULTS FILINGS.** Latest quarterly filing: Q1 FY27 unaudited consolidated results, quarter ended 30-Jun-2026, board meeting 31-Jul-2026. Also held: Q4 FY26 + FY26 audited results, year ended 31-Mar-2026, board meeting 12-May-2026 (B00). No quarter-gap between the latest results filing (Q1 FY27) and the latest AR (FY26, year ended 31-Mar-2026) — the AR covers the year immediately preceding the latest quarterly print, the normal pattern.

**4. INVESTOR PRESENTATIONS.** One held: the Q1 FY27 results deck (Investor_Presentation_1.txt). B04 input_gaps notes this is the Q1 FY27 results deck only; no pre-IPO or analyst-day deck is held.

**5. RESEARCH / RATING.** Two CARE rating documents held: Press Release dated 12-Oct-2025 (A+ Positive, reaffirmed) and Press Release dated 12-May-2026 (AA- Stable, upgraded); B00 instructs using the most recent. Seven broker/IPO notes held (NON-ANCHORED, leads only per B00 inventory).

**6. CORPORATE ACTIONS.** One operator-ferried announcements summary held, dated range Mar-2026 to Sep-2026 (`operator-ferried-announcements-summary-2026-03-to-09.md`). This is a SECONDARY-tier document: an operator-ferried summary, NOT filed Reg 30 PDFs (B00 input_gaps). Verifier A cannot cross-check its contents against a corpus PDF (B00 note).

**7. FRESHNESS PAIR CHECK.** B00 `freshness_verdict: FRESHNESS PAIRS OK`. All four pairs PASS: results-to-concall (Q1 FY27 results to Q1 FY27 concall, PASS), rating-bulletin-to-rationale (CARE PR 12-May-2026 to full rationale, PASS — "CARE Press Release format carries the full rationale"), SEBI-order-to-text (no order referenced, PASS), AR-to-latest-audited-annual (FY26 audited results to FY2025-26 AR, PASS). No failed pair; no freshness cap applies.

**8. VERDICT LINE.**

**CORPUS CURRENT.**

Nothing material is plausibly missing for the document types the pipeline expects. The one caveat that must travel with this verdict, per B00: two document types — announcements and shareholding (`operator-ferried-shareholding-mar-jun-2026.md`, a Screener rendering for Mar/Jun 2026, NOT the filed quarterly shareholding-pattern PDF) — are present only as operator-ferried SECONDARY summaries, not filed source PDFs. Every specific figure sourced from either file needs corpus or filing verification before any downstream stage anchors it as VERIFIED tier (B00 input_gaps). Separately (a Phase-3, not a corpus-completeness, concern): the ingestion manifest's `sector_cap_row` field was auto-set to "Pharma / CDMO", a collector error, since CleanMax is a renewable IPP; this does not affect corpus completeness but is carried forward as a flag (B00).

---

## SECTION 2: MENTAL MODEL DECLARATION (draft, for operator sign-off)

**DRAFT - PENDING OPERATOR SIGN-OFF**

### PART A — THE FROM STATE (the anchor, not the model)

**A1. ARCHETYPE (per line).**
- *RE Power Sales* (73.2% of FY26 revenue, B04): **Licence/scarcity business.** The economics run on grid-evacuation capacity secured years ahead of demand (B07 category B1, "Strong," documented), on the Electricity Act Captive Regulations forcing a minimum customer-equity structure per group-captive SPV (B07 category B2, "Strong," documented — the qualification-lock-in mechanism), and on 23-year weighted-average signed-PPA tenor as the contract "quota" (B04). The scarce, regulator-gated resource is grid connectivity and captive-SPV qualification, not price.
- *RE Services* (26.0% of FY26 revenue, B04): **Order-book business.** Percentage-of-completion EPC/O&M/carbon-services revenue, flagged as a Key Audit Matter for contract cost-to-complete estimation risk (B04), with an order book that itself shrank from 215 MW to 147 MW even as revenue jumped 7.3x YoY in Q1 FY27 (B05) — the classic order-book lumpiness signature.

**A2. THE SIMPLE ANALOGY.** CleanMax builds solar and wind farms for large companies, locks each one into a long power contract, then sells part ownership of the project — to the customer under group-captive rules, or to a partner — to fund the next build. It also builds and services renewable plants for others, a separate, lumpier business. Today the company looks like it is drowning: heavy debt, thin reported profit, cash burning faster than it comes in. That is the picture of a business racing to build faster than its young plants can season into steady cash, not the picture of the annuity it is trying to become. Strip away the build-out noise and the destination is a long-contracted power-sales annuity running at an 83-84% EBITDA margin (B04); the way it gets there is by recycling equity capital project by project, which is why it never fully owns what it consolidates.

### PART B — THE TRANSITION (the model)

**Transition line: RE Power Sales (dominant, 73.2% of revenue).** RE Services is a funding and execution engine for the build-out, not itself a declared transition line; its own trajectory (order book, cost-to-complete accuracy) is tracked as a supporting variable, not a FROM/TO climb.

**B1. FROM to TO (QUALITY LADDER).**
- **FROM: R1 COMMODITY PRICE-TAKER** (~12x neighbourhood). Weighted-average tariff on newly commissioned PPAs fell every year disclosed: Rs4.12/kWh (FY24) → Rs3.76 (FY25) → Rs3.57 (FY26) → Rs3.59 (Q1 FY27 trailing 12m) (B07 `FLAG-PRICING-POWER`). Median ROCE over the scored window is 5.83%, cyclical and depressed by capital sitting in CWIP not yet earning (B01). FCF is negative and widening (B01, B03). Pricing power scored "weak" (B04).
- **TO: R3 VALUE-ADDED / SPEC'D SUPPLIER** (~19x neighbourhood, ROCE 20-25% with stickiness). Once seasoned, the signed 23-year PPA book and the secured evacuation capacity function as switching-cost/spec-in lock-in (B07 categories B1, B2, C1 all scored "Strong," documented); management's own FY28 target (>=Rs3,000 Cr EBITDA off a 4.6 GW floor, implying a materially higher run-rate return on a now-largely-fixed capital base) points toward this tier, not toward R1 economics persisting.
- **FLAG ON THE RUNG-JUMP ITSELF:** the fleet grew 1.7 GW to 3.5 GW inside roughly two years (B04). An R1-to-R3 climb inside that window would be a two-rung leap against the framework's stated base rate of one rung per 2-3 years — itself a red flag this dossier surfaces rather than resolves. Stage 11 should test whether the claimed destination is R2 (COST-ADVANTAGED CONVERTER, ~15-17x, durable mid-teens ROCE) as an intermediate, more defensible landing point, rather than R3 outright.

**B2. THE ENGINE.** Two things must physically change: (1) fleet seasoning — young SPVs moving past their disclosed 3-6 month post-COD stabilisation lag into full-margin run-rate, evidenced by RE Power Sales EBITDA margin climbing 83% → 83.5% → 84% across the three calls tracked (B05 promise_delivery); (2) falling cost and improving tenor of capital — weighted average cost of project debt fell 8.7% (Dec-25) → 8.5% (Mar-26) → 8.4% (Jun-26) with the credit rating moving A+ → AA- → AA and a first domestic bond issuance pending (B05 guidance, promise_delivery). Both are mechanisms, not narrative: margin-per-seasoned-MW and cost-of-debt-per-rating-notch.

**B3. THE PROOF GATE.** Exact metric: **quarterly operating PBT before other income, on a consistent basis.** Threshold: **>= Rs 0 (positive), sustained.** The series moved from minus Rs 497 Cr (FY24) toward a small positive print in Q1 FY27 (B00 first_verification_priorities; B03 monitorables). Q2 FY27 (due late Oct-2026) is the next print and is named identically across B03, B05, B13 as the falsification line. Until this fires on a rebuilt (capitalised-interest-reverted, pre-useful-life-change) PBT basis, the crossover is unproven (B02, B03).

**B4. THE RECOGNITION GAP (to be resolved at Stage 11).** Open question, not answered here: does current market pricing already reflect the TO-state economics (a seasoned, 20-25% ROCE, long-contracted annuity), or does it still price CleanMax on today's build-out-distorted numbers (8.03x Net Debt/EBITDA, 1.17x interest coverage, 5.83% median ROCE)? Stage 11 resolves this via the PE gap. No number or conclusion is stated here.

**B5. THE UGLINESS TEST.** Today's ugly optics: Net Debt/EBITDA 8.03x, interest coverage 1.17x, median ROCE 5.83%, FCF minus Rs 4,023 Cr FY26 and widening (B01, B03). Classification: **ARTIFACT-OF-CLIMB, provisionally.** Revenue never declined (25.2% 5yr CAGR) and operating margin expanded every year since FY23 (B01 `analyst_note`) — the signature of capital deployed into not-yet-earning capacity, not of decaying unit economics. The provisional qualifier matters: the FY26 crossover used to support this classification itself rests on an unresolved cluster — a useful-life extension (25→30 years), a favourable impairment discount-rate change, and an interest-capitalisation jump to 28-30% of total interest (from 7-10% FY25), all landing in the same crossover/listing year (B02 top_findings #2, #4). The ARTIFACT classification is not yet proven; it is the more probable read on current evidence, pending the B3 proof gate.

**B6. THE TRANSITION FALSIFIER.** Either of two prints kills the transition thesis specifically (as distinct from the business, see C3): (a) Q2 FY27 operating PBT before other income prints below zero (B13 `falsification_metric`); or (b) the interest-capitalisation ratio stays near 28-30% instead of reverting toward the FY25 7-10% norm, which would show the FY26 margin/crossover was substantially an accounting choice, not an operating improvement (B03 monitorables). The rung-jump concern in B1 is a secondary falsifier: if Stage 11 finds the claimed R3 destination cannot be supported and only R2 economics are evidenced, the transition magnitude itself needs restating.

### PART C — WHAT THE MODEL WATCHES (derived from the transition)

**C1. DOMINANT VARIABLES.**
1. Operating PBT before other income (crossed to small positive in Q1 FY27; Q2 FY27 is the test) — B03, B05, B13.
2. Interest capitalisation ratio (28-30% FY26 vs 7-10% FY25 norm) — B02.
3. Fleet seasoning and capacity delivery pace against the >=1.5 GW FY27 floor and 4.6 GW-by-1-Apr-2027 base — B03, B05.
4. Cost of debt and credit-market access (8.7%→8.4% trend, AA rating, pending maiden bond issuance) — B05.

**C2. WHAT THE MODEL REJECTS.** Market-sizing questions are noise here, not the binding constraint: the addressable segment reads STRONG runway with ~13.4x revenue headroom against the 3-year obtainable share (B09), so execution and financing discipline bind, not market size. Specifically rejected as non-load-bearing: the unsourced 12%→14% C&I market-share claim (unverifiable against any peer or third-party report, B06, B09); management's ~Rs 3 lakh Cr addressable-EBITDA TAM claim (9.6x the independently derived 3-year obtainable share, reads as an inflated theoretical ceiling, B09); and the Bikaner curtailment headline in isolation, which is real (~Rs 170 Cr, ~13% of run-rate EBITDA) but bounded and industry-wide, not a scale threat to the transition (B06, B12b).

**C3. THE BUSINESS FALSIFIER (distinct from B6).** Evidence that would force re-declaring the FROM business itself, not just the transition: the consolidated current-liability shortfall (Rs 1,724.10 Cr, Note 58, AR p.688) crystallising into an actual auditor-qualified going-concern doubt rather than Board-level comfort language, especially spreading beyond the single component-auditor CARO Clause (xix) flag already raised on Clean Max Patagonia (Annexure A, AR p.365-370, B02); or the promoter pledge (20.02% of promoter holding, B01 `FLAG-PLEDGE`) escalating into an actual margin call / forced sale that destabilises control. Either would mean the group-captive SPV funding model is structurally broken, not merely early-stage.

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

CleanMax sells renewable electricity to large corporate and institutional customers under long-term contracts, and separately builds and services renewable-energy assets for them; the customer cannot easily replace either service because the power contracts run up to 23 years and the physical grid-evacuation capacity behind them is scarce and secured years in advance (B04, B07 category B1). Power Sales, at 73.2% of FY26 revenue and an 83-84% EBITDA margin, is the annuity engine; RE Services (EPC, O&M, carbon solutions), at 26.0% of revenue, is a lumpier, percentage-of-completion business flagged as a Key Audit Matter for cost-to-complete estimation risk (B04). Customers are named hyperscalers, Apple, Toyota Tsusho, and large industrial groups; about 74% of new volume comes from repeat buyers, and the group-captive equity structure mandated under the Electricity Act creates real switching costs once a customer is inside an SPV (B04, B07). Demand today concentrates heavily in Data & AI, which rose from 14% to 42% of contracted capacity in two years (B07, B09 downstream candidate: India data-centre operational capacity by hyperscaler), alongside a broader, still largely unpenetrated conventional C&I segment (B09). Demand should keep growing because the addressable market reads STRONG on an independent, non-circular cross-check — roughly Rs 44,460 Cr realistic TAM, Rs 25,650 Cr SAM, and a 3-year obtainable share of Rs 5,003 Cr leaving about 13.4x revenue headroom (B09) — and because CleanMax's own FY27 capacity guidance (>=1.5 GW, underpinned by a 4.6 GW opex-capacity floor by 1-Apr-2027) sits inside, not ahead of, an industry-wide capacity race that all five audited peers are also running (B06 `industry_cross_read`). The competitive advantage sits almost entirely in the Power Sales line: secured evacuation capacity, group-captive qualification lock-in, and an on-time, within-budget execution record all scored "Strong" and mostly documented in the Emerging Moat scan (B07). Pricing power is explicitly weak and getting weaker — new-PPA tariffs fell from Rs 4.12/kWh (FY24) to Rs 3.57/kWh (FY26) — so the moat is volume and relationship lock-in compounding into margin, not price (B07 `FLAG-PRICING-POWER`). RE Services carries no comparable moat: it is a support and pipeline-feeding engine, its own order book shrank from 215 MW to 147 MW even as one quarter's revenue jumped 7.3x, and B07 explicitly scores customer-concentration (C2) and competitive-intensity (H1) as adverse findings, with Adani, Reliance, and NTPC named by management itself as active new C&I entrants (B07).

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. Verticals framed (one per C1 dominant variable)

**Vertical 1 — Operating PBT crossover reality.** What the corpus establishes: operating PBT before other income moved from minus Rs 497 Cr (FY24) to a small positive print in Q1 FY27 (B00, B03); management credibility on metrics within its control grades B (B05). What it cannot establish: whether the crossover survives a PBT rebuild with capitalised interest reverted to the FY25 ratio and depreciation restated at the pre-change 25-year useful life (B02, B03) — that rebuild has not been done inside this corpus. Questions that decide it: (1) does Q2 FY27 operating PBT before other income print at or above zero? (2) does the interest-capitalisation ratio revert toward 7-10%? (3) is "reported EBITDA" ever reconciled to CARE's PBILDT (operating-only) basis (B05 `input_gaps`)?

**Vertical 2 — Interest capitalisation / accounting-choice cluster.** What the corpus establishes: true all-in Group interest cost was ~Rs 1,098-1,115 Cr FY26 against Rs 785.92 Cr shown in the P&L, with ~Rs 312-329 Cr (28-30% of total interest) capitalised versus a 7-10% FY25 norm (B02, Notes 3, 36, AR p.401, 431). What it cannot establish: management's own explanation for the ratio jump, or a specific facility-level breakdown; no call addresses it (B05 `input_gaps`). Questions: (1) what specific CWIP/under-construction facilities drove the jump? (2) does FY27 revert to the FY25 norm? (3) does the useful-life extension (25→30 years, AR p.400-401) recur or reverse?

**Vertical 3 — Fleet seasoning and capacity delivery pace.** What the corpus establishes: FY27 guidance of >=1.5 GW capacity addition, reaffirmed across all three calls, with ~33% (500 MW, of which ~400 MW power-sales/opex) delivered in Q1 FY27, ahead of straight-line pace (B05 `promise_delivery`; B12b minor correction on the ~27% vs ~33% framing). What it cannot establish: land-acquisition completion (100% by Sep-2026 target stated once, Q3 FY26, never reconfirmed) or the Osaka Gas JV's (400+ MW/3-year) actual progress, since neither had a follow-up disclosure (B05 `dropped_triggers`). Questions: (1) is land 100% secured by the stated Sep-2026 date? (2) has the Osaka Gas JV disbursed any capex or commissioned any MW? (3) does the 4.6 GW floor hold through FY27 given the Bikaner curtailment drag?

**Vertical 4 — Cost of debt and credit-market access.** What the corpus establishes: weighted average cost of project debt fell every quarter tracked (8.7%→8.5%→8.4%), the credit rating moved A+ → AA- → AA across roughly a year (not one quarter, per B12b's correction), and interest-rate swaps hedge only ~11.9% of Rs 8,651.29 Cr variable-rate debt (B02, B05). What it cannot establish: whether the maiden domestic bond issuance actually prices, or at what spread — management says "hopefully soon" with no firm date (B05 `repeated_evasions`). Questions: (1) does the bond issuance complete, and at what spread vs the AA curve? (2) does hedging coverage rise from ~12% of floating debt? (3) does net debt track toward the guided ~Rs 16,000 Cr steady state at the FY28 EBITDA target?

### 4b. Candidate signal table (B09 candidates expanded)

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
| --- | --- | --- | --- |
| India C&I open-access RE capacity additions (quarterly GW) | Quarterly GW additions stall or reverse against the CRISIL/Mercom forward curve implied in B09's TAM build | Quarterly | Mercom India Solar Open Access Market Report (B09) |
| India data-centre operational capacity (MW), by hyperscaler | Hyperscaler capex/data-centre build guidance flattens or reverses, undercutting the Data & AI demand trigger (42% of contracted capacity) | Quarterly | CBRE / Cushman & Wakefield / JLL India data-centre trackers (B09) |
| Named hyperscaler India data-centre capex/build announcements (Amazon, Google, Meta, Microsoft) | A named hyperscaler pauses or insources India capacity, disintermediating the VPPA/EAPA-to-physical-PPA optionality | Event-driven | Hyperscaler capex guidance calls / company IR disclosures (B09) |
| PGCIL/CTU grid-evacuation capacity delivery (Rajasthan corridor) | No firm, holding PGCIL resolution date for Bikaner; curtailment spreads to the Koppal CTU site | Quarterly | PGCIL project status disclosures / CERC orders (B09) |
| State open-access/group-captive regulatory changes (cross-subsidy surcharge, banking rules) | An adverse state-level ruling narrows the practically addressable SAM in a CleanMax-material state | Event-driven | State Electricity Regulatory Commission (SERC) orders (B09) |
| Peer C&I RE capacity and revenue disclosures (Adani Green, ACME Solar, KPI Green, O2 Power) | Peer capacity/share growth outpaces CleanMax's, undercutting the unverified 12%→14% share claim | Quarterly | Peer quarterly results / investor presentations (B09) |

Two supplementary items, sourced from B06/B08 rather than B09 (not counted in `candidate_count`, carried for completeness): GNA-vs-TGNA connectivity status at CleanMax's next CTU site (Koppal 529 MW), falsifier = a second TGNA-status curtailment loss materialising, cadence event-driven, source PGCIL/CERC filings + concall (B06 `analyst_note`); promoter pledge LTV/top-up covenant terms with 360 One Prime, falsifier = any further pledge increase past 20.02% or a disclosed top-up call, cadence event-driven, source exchange/encumbrance filings (B08 `verdict_basis`).

### 4c. Fragility read

- **variable_count:** 7 — (1) operating-PBT crossover confirmation, (2) interest-capitalisation reversion, (3) capacity-delivery pace vs the 1.5 GW/4.6 GW floors, (4) cost-of-debt/bond-issuance access, (5) Bikaner CTU curtailment resolution, (6) promoter-pledge stability (no further escalation, no margin call), (7) competitive intensity holding (Adani/Reliance/NTPC entrants) against the claimed market-share trend.
- **verifiability_ratio:** 6 of 7 externally observable — operating-PBT prints, the interest-capitalisation ratio, capacity commissioned, cost-of-debt/rating moves, Bikaner's grid connectivity status, and the promoter pledge percentage are all filed or registry-checkable. The seventh, the 12%→14% C&I market-share claim, is company-narrated only and unverifiable against any peer or third-party source in this corpus (B06, B09).
- **single_point_failure:** Q2 FY27 operating PBT before other income printing below zero. This one print is named, independently, as the falsification line across B03, B05, and B13 — it alone would show the FY24-to-Q1-FY27 crossover was carried by other income and accounting choices rather than the operating engine.
- **fragility_verdict: FRAGILE.** A named single point of failure is present even though six of seven variables are externally verifiable; per the fragility-verdict definition, one kill-switch alone is sufficient to classify FRAGILE regardless of the otherwise favourable verifiability mix.

### 4d. Research brief (live-web work order for claude.ai)

1. Independently corroborate the 12%→14% India C&I market-share claim against a third-party report (Mercom, CRISIL, Bridge to India); the 14% figure carries no cited source in the corpus (B06, B09).
2. Verify the sourcing and methodology behind management's ~Rs 3 lakh Cr addressable-EBITDA TAM claim, which this corpus's independent build reads as ~9.6x the 3-year obtainable share (B09).
3. Fetch and read the primary CRISIL 57 GW-by-FY28 C&I open-access capacity forecast directly; B09 relied on a search-engine summary citing CRISIL (egress-blocked in this container).
4. Fetch the primary CEA sectoral electricity-consumption report directly; B09 relied on a 2025-vintage CEIC secondary aggregator, flagged stale.
5. Verify current PGCIL/CERC status and any firm resolution date for the Bikaner (525 MW, TGNA) grid-curtailment issue, and pre-emptively check the Koppal (529 MW) CTU site for the same GNA/TGNA exposure.
6. Verify the LTV and any top-up/margin-call covenant terms on the promoter-group's 20.02% share pledge to 360 One Prime Ltd (B08 `analyst_note`).
7. Verify the current status and any ruling in the Green Earth criminal complaint (IPC 406/420/467/468/471/120B/506) naming Kuldeep Jain, in mediation before the Punjab & Haryana High Court since a Jan-2026 referral (B08).
8. Fetch the AZB Partners deal note on the promoter's stake acquisition from Brookfield, and the IPO Central / Business Standard "reasons to avoid" articles — both blocked by the egress proxy inside this container (B08 `searches_skipped`).
9. Search for a dedicated SES (Stakeholders Empowerment Services) or other proxy-advisory governance report on the CleanMax IPO; not separately queried by B08.
10. Spot-check RoC/MCA struck-off status on a sample of the ~190+ subsidiary SPVs beyond the AR/RHP's own group-structure disclosure (B08 `searches_skipped`).
11. Verify whether the FY28 >=Rs 3,000 Cr "reported EBITDA" guidance basis (confirmed on the Aug-2026 call to include both segments) has since been reconciled anywhere to CARE's PBILDT (operating-only) definition (B05 `input_gaps`).
12. Check peer (JSW Energy, ACME Solar, Adani Green) FY26 disclosures for commodity/currency cost-inflation impact and compare against CleanMax's own stable-to-improving margin trend, which shows no equivalent pressure in any of its three calls (B06 `industry_cross_read`).

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. CleanMax sells renewable electricity to companies under long-term contracts, most running up to 23 years.
2. It also builds and services renewable power plants for those same customers, as a separate business line.
3. The power-sales business made 73% of FY26 revenue at an 83-84% margin; the build-and-service business made 26% at a much thinner, lumpier margin.
4. Customers are named hyperscalers, Apple, Toyota Tsusho, and large industrial groups; about 74% of new business comes from repeat buyers.
5. Companies buy from CleanMax because scarce grid connections and long PPA contracts are hard to get on their own, and CleanMax secures both years ahead of need.
6. Demand is growing because data centres and AI infrastructure now drive a large and rising share of new contracts, up from 14% to 42% of capacity in two years.
7. The addressable market looks large and growing; an independent check puts revenue headroom at about 13 times the company's 3-year obtainable share.
8. Demand growth may not come from price. New power-contract tariffs fell every year measured, from Rs 4.12 to Rs 3.57 per unit.
9. The moat sits in secured grid capacity and locked-in customer relationships, not in pricing power, and it sits almost entirely in the power-sales business.
10. The build-and-service business has no comparable moat; its own order book shrank even as one quarter's revenue jumped sharply, and new competitors (Adani, Reliance, NTPC) are entering the space.
11. The mental model is a climb from a low-return, capital-hungry build phase toward a long-contracted, high-margin annuity, and the climb is not yet proven on the numbers.
12. The overall evidence read is fragile: one single number, next quarter's operating profit before other income, can by itself undercut the whole growth story if it comes in negative.
13. The filed record cannot yet confirm whether last year's jump into profit was a real operating shift or partly the result of accounting choices, like a longer useful life and more capitalised interest, made in the same year.
14. The corpus could not establish who CleanMax's true single largest competitors are by market share, or verify the company's own claimed share of the market.
15. The two biggest open questions are whether next quarter's profit print holds up, and whether the promoter's leveraged pledge on 20% of his holding stays stable or becomes a forced-sale risk.

---

## SECTION 6: STANDING EXTRACTION ANNEX

### 1. UNITS

Quote: *"₹3.85/kWh Weighted Average Tariff for Contracted Capacity Under Execution"* (Annual Report 2025-26, printed p.16-17, "Business Ecosystem" page; text-twin page 249/250). Comment: this is a printed per-unit figure for one metric (tariff, contracted-under-execution capacity, a basket across all technologies and states), not a segment average across the whole operational book.

Quote: *"the operational portfolio tariff is about INR3.93 per unit of power. This is for the existing capacity of 3.5 gigawatt, and what is under execution, so, you know, 2.5 gigawatt is contracted under execution, that is at a tariff level of INR4."* (Concall_Aug_2026_Transcript.txt, transcript p.6). Comment: two more per-unit tariff basket figures, operational (Rs 3.93/kWh) vs under-execution (~Rs 4/kWh), management-spoken rather than a statutory-document figure; both are basket averages across the whole book, not per-product breakdowns.

Additional printed per-unit-adjacent figures, all baskets: repeat-order share 74%, weighted average PPA tenor 23.17 years, plant availability 98.19%, budget-to-actual cost ratio 97.20%, receivable days 25 (same AR p.16-17 table). No per-MW revenue or EBITDA figure is printed anywhere in the corpus as a single number; B04 derives Solar Rs 50-55 Lakh/MWp and Wind Rs 100-110 Lakh/MW run-rate EBITDA from the underlying volume and revenue lines (RE Power Sales revenue Rs 13,995 Million FY26 at 83.5% EBITDA margin, Note 38, AR p.469-470, against the 3.1 GW operational portfolio, MD&A AR p.355) rather than from a single printed per-unit disclosure.

### 2. SEGMENT CAPITAL AND DEBT

Quote (Note 38, Segment Information, AR p.469-470, text-twin page 683-684):
*"Segment assets ... (a) Segment A - Renewable Energy Power Sales 1,96,734.00 [FY26] / 1,22,897.20 [FY25] ... (b) Segment B - Renewable Energy Services 14,759.80 / 3,264.85 ... (c) Unallocated 19,488.98 / 6,630.48 ... Total 2,30,982.78 / 1,32,792.53"* (₹ Million).
*"Segment liabilities ... (a) Segment A ... 1,63,953.12 / 93,653.09 ... (b) Segment B ... 3,194.35 / 2,750.06 ... (c) Unallocated 8,599.96 / 4,341.65 ... Total 1,75,747.43 / 1,00,744.80"* (₹ Million).

Comment: borrowings are NOT separately allocated by segment; Note 38 gives only segment-level finance-cost footnotes (Segment A finance cost Rs 6,927.05 Mn FY26 vs Rs 6,380.48 Mn FY25; Segment B finance cost Rs 397.04 Mn FY26 vs Nil FY25; unallocated finance cost Rs 535.13 Mn FY26 vs Rs 248.39 Mn FY25) rather than a segment-wise balance-sheet borrowings split. The company also discloses, at Note 38: *"There is no single customers from whom the Group has earned more than 10% of its total revenue."* — relevant to Q4 below as well.

### 3. GUIDANCE VERSUS ASPIRATION

(a) Guidance with a period:
- *"we are comfortable providing that new guidance, that we will have a minimum EBITDA of INR3,000 crores in FY28, which is nearly 2.4x the EBITDA in FY26"* (Concall_Aug_2026_Transcript.txt p.6). FY28 minimum EBITDA >= Rs 3,000 Cr.
- *"The first number is 4.6 gigawatt will be the minimum opex sales capacity on 1st April 2027"* (Concall_Aug_2026_Transcript.txt p.6). 4.6 GW minimum opex capacity, dated 1-Apr-2027.
- *"the steady-state net debt corresponding to this INR3,000 crores EBITDA will be INR16,000 crores"* (Concall_Aug_2026_Transcript.txt p.18). Steady-state net debt ~Rs 16,000 Cr, tied to the FY28 EBITDA target.
- FY27 capacity addition >=1.5 GW, first stated Q3 FY26 concall, reaffirmed Q4 FY26 and Q1 FY27 (B03 `guidance_table`, B05 `guidance`).
- Osaka Gas JV to build 400+ MW over 3 years, stated Q3 FY26 only (B05 `guidance`), not reconfirmed in Q4 FY26 or Q1 FY27 (B05 `dropped_triggers`).
- 100% land acquisition for FY27 capacity by September 2026, stated Q3 FY26 only, never reconfirmed (B05 `guidance`, `dropped_triggers`).
- RE Power Sales EBITDA margin toward 85-86% "over 2-3 years", stated Q3 FY26 (B05 `promise_delivery`).

(b) Aspiration without a period:
- All-India C&I market share, stated at 12% (Q3 FY26, DRHP-sourced) rising to 14% (Q1 FY27, source unnamed) — a claim about current position, not a forward target with a date (B05 `peer_questions`).
- 7-8% green-PPA penetration / ~Rs 3 lakh Cr addressable EBITDA pool, stated without a target date or a stated methodology (B05, B09).

(c) Capacity or capability only:
- *"5,332 MW Evacuation Visibility"* and *"₹1,870 Crore Run-Rate EBITDA"*, point-in-time capability figures as of 1-Apr-2026, not a forward guided number (AR p.16-17); B03 separately notes this run-rate figure is 44% above the company's own reported EBITDA of Rs 1,294.56 Cr and is not reconcilable to any statutory line.
- BESS-as-a-service, three client MOUs signed, not yet material to capex — capability/optionality, not a dated commitment (B07 `optionality_register`).
- ALMM2 module-cost benefit of ~Rs 60 lakh/MW, a market-window fact with an end date (31-Dec-2026) rather than a company guidance number (B05 `guidance`).

### 4. CONCENTRATION

Quote: *"There is no single customers from whom the Group has earned more than 10% of its total revenue."* (Note 38, AR p.470). Comment: no top-5/top-10 customer share figure is disclosed anywhere in the AR or across all three concalls (B05, B07 `input_gaps`), despite management separately stating Data & AI customers are 42% of contracted capacity (up from 14% two years earlier, Concall_Aug_2026_Transcript.txt p.4) — a segment/sector concentration figure, not a named-customer one. Product concentration: two disclosed segments, RE Power Sales 73.2% and RE Services 26.0% of FY26 revenue (B04, cross-tied to Note 38's Rs 13,995 Mn / Rs 4,973 Mn split, AR p.355, p.469). Geography: revenue from RE Power Sales was Rs 13,203.23 Mn within India vs Rs 791.27 Mn outside India FY26; RE Services Rs 4,661.12 Mn within India vs Rs 312.16 Mn outside India FY26 (Note 38, AR p.470 text-twin). Top-customer-name-level share: NOT DISCLOSED — the corpus discloses only the "no customer >10%" negative statement, not a positive top-customer percentage.

### 5. PROMISE LEDGER

| Promise (promised in) | Delivery status | Evidence anchor |
| --- | --- | --- |
| Bikaner 525 MW CTU backdown resolved Oct-Dec 2026 (grid estimate) (Q3 FY26) | Missed | Curtailment worsened 30%→70% across Q4 FY26/Q1 FY27; resolution timeline slipped each call (B05) |
| Weighted avg cost of debt to keep falling (Q3 FY26) | Delivered | 8.7%→8.5%→8.4% every quarter checked (B05) |
| RE Power Sales EBITDA margin toward 85-86% over 2-3 years (Q3 FY26) | Partial | 83%→83.5%→84%, directionally on track (B05) |
| 100% land acquired for FY27 capacity by Sep-2026 (Q3 FY26) | Partial | No follow-up update in Q4 FY26 or Q1 FY27 (B05) |
| Osaka Gas JV to build 400+ MW over 3 years (Q3 FY26) | Partial | No progress update in either subsequent call (B05) |
| Projects built within Board-approved capex (Q3 FY26) | Delivered | Reaffirmed FY26 full year and Q1 FY27 (B05) |
| DSM impact + BESS strategy announced within 3-4 months (Q4 FY26) | Partial | BESS strategy delivered ~3 months later; explicit DSM Rs-impact figure not delivered (B05) |
| Credit rating trajectory toward AA / bond-market readiness (Q4 FY26) | Delivered | A+ → AA- threshold → AA within ~a year; bond issuance itself still pending (B05, corrected by B12b from "one quarter" to ~a year) |
| FY27 capacity addition >=1.5 GW (reaffirmed Q4 FY26) | Partial | ~400 MW power-sales capacity added Q1 FY27, ~27% of the floor (B05, corrected by B12b) |
| Repeat-business rate ~74-75% of new volume (Q3/Q4 FY26) | Delivered | 74% (Q3 FY26), 74% (Q4 FY26), ~75-80% (Q1 FY27) (B05) |
| Credit-quality customer mix, AA/AAA/MNC + A-rated ~97% (Q3 FY26) | Partial | 83%→82%→"above 80%" with reduced precision (B05) |

Scored totals: 4 delivered, 6 partial, 1 missed (B05 `promise_delivery`).

### 6. RESTATED BASES

Quote: *"The shareholders of the Company in extra-ordinary general meeting dated 27th June, 2025, have approved split of each equity share of face value of ₹10 each into 10 shares of face value of ₹1 each (the 'Split'). Further, pursuant to a resolution passed in extra-ordinary general meeting dated 8th August, 2025, shareholders have approved the issuance of bonus shares to the equity shareholders in the ratio of 1:1 (the 'Bonus'). The effect of Split and Bonus issues has been adjusted retrospectively for previous year while calculating Earnings Per Share (EPS)."* (Note 28, footnote 28(a), Standalone Financial Statements, AR p.750). Comment: standard Ind AS 33 retrospective EPS restatement, not a concern; consolidated basic EPS restated to Rs 74.17 (FY26) vs Rs 30.83 (FY25) on this basis.

Quote (paraphrase per B02, gratuity note): gratuity provision reclassified non-current to current in FY26; the FY25 comparative of Rs 0.65 Cr was left unrestated as not material (Note 23, AR p.424, confirmed at text-twin page 424: "Provision for gratuity [Refer footnote 23(b) and note 41] 11.82 [FY26] / - [FY25]"). Comment: a small, disclosed, immaterial reclassification.

### 7. CORPORATE-ACTION CLAUSES

No scheme of arrangement, demerger, merger, or buyback (at the parent level) is in the corpus. Quote: *"The Company has not entered in any scheme of arrangement under section 230 to 237 of Companies Act 2013."* (Note 50(ii), Standalone Financial Statements, AR p.855). A subsidiary-level buyback exists only as a minor reserve adjustment: *"Less: Transfer to capital redemption reserve on buyback in subsidiary (0.61)"* (AR p.421 area, Note 19-adjacent) — NOT further detailed in the corpus; the underlying subsidiary buyback filing itself is not held and would need to be fetched if material.

The one material corporate action with full clauses present is the pre-IPO preferential allotment: Quote: *"the Company vide Board Resolution passed on 2nd February, 2026 and vide Shareholders resolution passed on 4th February, 2026, approved issue of 28,19,548 ... equity shares of face value Rs.1/- ... at a price of Rs.1,053/- ... per equity share ... including premium of Rs.1,052/- ... per share, aggregating to Rs.2,96,89,84,044/- ... to Jongsong Investments Pte Ltd. by way of private placement on preferential basis"* (Board's Report, AR p.321). Appointed/effective dates: Board resolution 2-Feb-2026, shareholders' resolution 4-Feb-2026, allotment closed per AR at 6.16% stake. Comment: this is the Temasek-affiliate pre-IPO entry (B08 `transition_evidence`); full ratio, price, and dates are printed and internally consistent with the shareholding-pattern table (Jongsong 72,17,474 shares, 6.16%, AR p.420-area).

### 8. RELATED-PARTY PERIMETER

Quote (illustrative row from the RPT disclosure table, AGM Notice, AR p.88): *"77 Clean Max Patagonia Private Limited Subsidiary Sale of Projects Within a year 77.36 N/A"* (₹ Crore). The table runs to ~190+ subsidiary-SPV rows by nature of transaction (Sale of Projects, EPC, O&M, Support Fees, etc.), consistent with B02's finding of ~56 Material RPT resolutions and ~30 with disclosed aggregate ceilings summing to ~Rs 14,800+ Cr (AGM Notice, AR p.4-33).

Quote, the Clean Max Patagonia ceiling specifically: *"approval of the members of the Company be and is hereby accorded to the Company to continue with the existing contract(s)/arrangement(s)/transaction(s) ... between the Company and Clean Max Patagonia Private Limited a Subsidiary, for an aggregate value up to INR 216.25 crore, subject to such contract(s)/arrangement(s)/transaction(s) being carried out at arm's length and in the ordinary course of business of the Company."* (AGM Notice, Resolution 31, AR p.19). Comment: this ceiling is authorised for an entity (Clean Max Patagonia) that the component auditor separately flags under CARO Clause (xix) for material uncertainty over meeting its liabilities (Annexure A, AR p.365-370, B02 finding #10) — the two disclosures do not cross-reference each other in the document.

Also on the RPT perimeter: parent standalone loans/advances to related parties jumped 4.3x to Rs 1,363.66 Cr, 36.87% of the parent's total loan book (Note 49(a), standalone, AR p.854, B03), and the inter-SPV cash-pooling programme spans 17 arrangements, ~Rs 3,011 Cr disclosed across 9 of the 17 (AGM Notice, B02 finding #6).

### 9. PLEDGE AND SHAREHOLDING

Quote: *"As at 31st March, 2026, Kuldeep Jain and KEMPINC LLP ('Pledger') have pledged in aggregate, 11,597,866 Equity Shares ('Pledged Shares') held by them in favour of 360 One Prime Limited, in accordance with the terms of the pledge agreement dated July 22, 2025 entered into by the Pledgers with 360 One Prime Limited, in relation to certain borrowings availed by KEMPINC LLP."* (Note 19(g), AR p.420). Comment: 11,597,866 shares = 20.02% of promoter-group holding (B01, B08).

Quote, prior year: *"As at 31st March, 2025, Kuldeep Jain and KEMPINC LLP have pledged in aggregate, 205,404 Equity Shares against the issue of non-convertible debentures."* (Note 19(g), AR p.420). Comment: this confirms the pledge trend rose from a near-immaterial FY25 base tied to an NCD issuance, to a materially larger, differently-purposed (personal leveraged share purchase) pledge in FY26 (B08 `pledge_trend`).

Twelve-quarter pledge/holding series: NOT FOUND as a single continuous filed table in this corpus; only the two AR year-end snapshots above (FY25, FY26) and the operator-ferried Screener shareholding summary (Mar/Jun 2026, SECONDARY tier per B00) are held. A full 12-quarter series would need the filed quarterly shareholding-pattern PDFs, not present.

Institutional holding, latest per corpus: BGTF One Holding (DIFC) Limited (Brookfield-affiliate) held 21.31% as at 31-Mar-2026, down from 49.92% as at 31-Mar-2025 — a (28.61%) change during the year (AR p.420 shareholding table, text-twin page 420). Rikhab Investments B.V. held 8.37% (new, 100% change) as at 31-Mar-2026 (same table).

### 10. VERIFICATION

Documents quoted in this annex:
- Annual Report FY2025-26, Clean Max Enviro Energy Solutions Limited, 16th AGM Notice + Annual Report, dated 30-Jun-2026 (859pp), file `inputs/annual-report/0da3293c-ae05-4b6d-b21f-0b3793bfecbc.txt` (text-twin of the filed PDF).
- Concall_Aug_2026_Transcript.txt (Q1 FY27 earnings call, 03-Aug-2026), file `inputs/concalls/Concall_Aug_2026_Transcript.txt`.
- All other figures in this annex reused from already-anchored citations in B00-B09 stage blocks and reports, each carrying its own filename/date anchor as cited inline above.

CORPUS COMMIT HASH: ebc10ead3d0c30ab49f5c00500af34a7a77df42d
