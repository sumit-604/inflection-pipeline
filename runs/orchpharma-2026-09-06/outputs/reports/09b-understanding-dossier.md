# HALT 1 UNDERSTANDING DOSSIER — ORCHID PHARMA LTD (ORCHPHARMA)

Run: orchpharma-2026-09-06 | Phase 1 evidence only | Assembled from committed blocks B00-B09, verifiers B12a-B12d, confidence.yaml, B13-synthesis, and the orchestrator corrections file. No new research. No valuation, price, or verdict vocabulary anywhere below, except the one scoped exception in Section 2 Part B4.

GATE VERDICT (carried, not restated as anything else): **REWORK**. REWORK judges the analysis, not the company (B13; gate-recommendation.md).

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

### 1. Concalls

Four Orchid Pharma transcripts held, all clean OCR (B00.text_extracts):

| File | Call month | Quarter covered |
|---|---|---|
| Concall_Nov_2025_Transcript.pdf | Nov 2025 | Q2 FY26 |
| Concall_Feb_2026_Transcript.pdf | Feb 2026 | Q3 FY26 |
| Concall_Jun_2026_Transcript.pdf | Jun 2026 | Q4 FY26 + FY26 full year |
| Concall_Aug_2026_Transcript.pdf | Aug 2026 | Q1 FY27 |

Most recent quarter covered: Q1 FY27 (quarter ended ~30-Jun-2026, call held Aug-2026). Given the run date of 2026-09-06, Q2 FY27 (quarter ending ~30-Sep-2026) has not yet closed, so no newer transcript is plausibly missing. Concall coverage is current.

Eleven peer transcripts also held (NEULANDLAB 4, GRANULES 4, KOPRAN 3), all clean OCR. KOPRAN's three calls predate Apr-2025, roughly 18 months staler than the other two peers (B00.peer_set; B06.input_gaps).

### 2. Annual reports

Two years held: Annual_Report_2024.pdf and Annual_Report_2025.pdf (32nd Annual Report, FY2024-25). The latest completed FY per the screener Data_Sheet is FY2026 (year ended 31-Mar-2026), and its annual report is ABSENT from the corpus. Only two years are held, not the three-plus a full review would want, and the newest one is a year behind the newest audited financial data the corpus otherwise carries (B00.freshness_pairs).

### 3. Results filings

ABSENT entirely. inputs/results/ is empty (B00.inventory.results = 0). No quarterly or annual Reg 33 filing exists in this corpus for any period. The only quantitative disclosure for FY2026 comes from the screener Data_Sheet aggregate and from management's own concall commentary, neither of which is a primary filing. Quarter-gap: every quarter, all the way back, has zero primary results filings in this corpus; concalls substitute for narrative but not for the filed numbers themselves.

### 4. Investor presentations

One held: Investor_Presentation_1.pdf. It is image-based, 3,124 characters extracted across 14 pages, and is treated as near-absent for figures (B00.inventory.presentation = 1; B00.input_gaps). No usable date was extracted from it in this corpus.

### 5. Research / rating

ABSENT. Zero rating bulletins, zero rating rationales, zero broker or research notes in the corpus (B00.inventory.rating = 0, research = 0). Stage 8 confirms a CARE Ratings rationale dated Mar-2025 exists externally but its fetch was EGRESS_BLOCKED and it is not in this corpus (B08.searches_skipped).

### 6. Corporate actions

ABSENT as filings. Zero exchange announcements / Reg 30 filings (B00.inventory.announcements = 0). Corporate actions are known only through annual-report narrative and web-derived secondary sources, not filed announcements: the Rs 391.80 cr QIP (27-Jun-2023), the Minimum Public Shareholding breach and freeze (20-Apr-2023 to cure), the Dhanuka Laboratories merger NCLT order (29-Apr-2025) and its effective date (10-Jul-2026, web-derived per Correction 4/8), and the Rs 143 cr promoter OCD issuance. Date range narrated in the AR: roughly 2021 to 2026.

### 7. Freshness pair check

Per B00.freshness_pairs (four pairs defined in prompts/00-orchestrator.md):

- RESULTS to CONCALL: NO TRIGGER (inputs/results/ empty; no trigger document exists to test).
- RATING BULLETIN to RATIONALE: NO TRIGGER (inputs/rating/ empty).
- SEBI ORDER to ORDER TEXT: flagged PENDING STAGE EVIDENCE at Gate 0. Later stages (B02, B03, B08) surfaced only two small, paid BSE/NSE compliance fines and a historical, cured Minimum Public Shareholding freeze; no unresolved SEBI adjudication order reference was found anywhere in the corpus (B02.regulatory_extension; B08). This pair did not fire retrospectively.
- **AR to LATEST AUDITED ANNUAL RESULTS: FAIL.** Trigger document: the FY2026 audited annual results, evidenced by the complete FY2026 column in the screener Data_Sheet (sales Rs 1,232.78 cr, PBT Rs 10.43 cr, balance sheet and cash flow both dated 2026-03-31). Mate expected: the FY2026 annual report, or the FY2026 audited annual results filing. Neither exists in this corpus (B00.freshness_pairs).

### 8. Verdict line

**CORPUS GAPPED-FRESHNESS.** The AR-to-latest-audited-results pair failed. The missing mate is the Orchid Pharma FY2026 audited annual results filing (the Q4 FY26 full-year Reg 33 submission), and the FY2026 Annual Report when filed. Expected source: BSE or NSE corporate filings, or the company investor relations page. This verdict takes precedence over a plain CORPUS GAPPED and carries the downstream consequence that the phase-1 gate recommendation caps at PROCEED WITH CAVEATS on freshness grounds alone (a cap that in this run is superseded by the more severe REWORK verdict on analysis-quality grounds; the two are additive, not alternative — B13; gate-recommendation.md).

Other gaps, listed under this verdict, findable-but-missing (the operator's upload/fetch list):
- FY2026 annual report and FY2026 audited results filing (BSE/NSE/company IR) — the freshness-pair mate itself.
- Post-allotment shareholding pattern (SAST XBRL, BSE/NSE) — always filed quarterly for a listed company; absent here (B08).
- Any exchange announcement / Reg 30 filing (BSE/NSE) — always filed by a listed company; absent here (B00).
- Latest credit rating rationale, CARE Ratings, Mar-2025 confirmed to exist, fetch blocked (B08).
- Dhanuka Laboratories merger scheme document, fairness opinion, and swap-ratio valuation (BSE/NSE scheme filings; not reachable via WebFetch in this run — B08).
- Dhanuka Laboratories Ltd's own filed accounts at the MCA — the one document that would separate the two readings of its implied FY26 EBITDA loss (Correction 9).
- Aurobindo Pharma's own filings on its competing 7-ACA project — currently only web-derived, unconfirmed (Correction 7.1).

Plausibly-nonexistent, itself a data point:
- Broker/research notes: none found; consistent with a small/micro-cap name with thin institutional coverage (B00.input_gaps calls this "non-anchored; no evidence effect").

Structural corpus defects, not gaps, recorded so they are not re-litigated:
- Both annual report PDFs carry a corrupt OCR text layer concentrated in the financial statements: 96% of FY2024's 318 pages, 37% of FY2025's 300 pages (pages 174-224 standalone FS, 232-300 consolidated FS). A figure anchored to a page tagged [OCR:embedded-CORRUPT] is ANCHOR NOT FOUND unless independently found in the source PDF (B00.ocr_audit; Correction 3).
- The peer set (NEULANDLAB, GRANULES, KOPRAN) contains no company that manufactures cephalosporin API or 7-ACA. It can test whether Indian API exporters broadly had a bad FY2026; it cannot test anything specific to the cephalosporin chain, which is where Orchid's whole thesis sits (Correction 5, amended).

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT - PENDING OPERATOR SIGN-OFF.** This declaration is signed only in claude.ai, after live-web stress-testing. Nothing here is a signed model.

### PART A — THE FROM STATE

**A1. Archetype (per line).**

| Line | Archetype |
|---|---|
| Cephalosporin API/FDF export business (98.3% + 1.7% of FY25 revenue) | Commodity converter (Section 1B v3.7 Amendment 17 binds): spread economics, utilisation-dependent, cost-curve rank versus Chinese suppliers (B04.business_type; B04.revenue_streams) |
| Enmetazobactam / Orblicef (India) / Exblifep (Europe) licensing | Licence/scarcity business: patent protection, milestone-plus-royalty economics, country-by-country rights (B04.revenue_streams; B07 patent moat A2) |

**A2. The simple analogy.** Orchid buys a chemical building block, mostly imported from China and, for one key intermediate, from a single related-party supplier, and processes it into antibiotic ingredient that it sells by the kilogram to drug makers in 48 countries. It does not set the price the market does. Alongside that business, Orchid is building its own factory for the building block it currently imports, so it can stop being a price-taker on that input, and it separately owns a patented antibiotic that it is trying to license out, country by country, for royalties. Two things funded by one balance sheet, reported as one segment, with two very different risk profiles (B04.flags; Correction 6.2).

### PART B — THE TRANSITION

**Line 1: Cephalosporin API/FDF export business**

B1. FROM to TO: FROM **R1 COMMODITY PRICE-TAKER** (no pricing power; ROCE cyclical, never cleared 8.33% in any of the four audited years FY2022-FY2025 — B01.core_score; gate-recommendation.md) TO **R2 COST-ADVANTAGED CONVERTER** (margin from cost position rather than price, Amendment 17 caps this rung's multiple).

B2. The engine: the Rs 750 cr 7-ACA backward-integration plant at Jammu, which converts a purchased, market-priced input (7-ACA, imported from three-to-four Chinese suppliers, plus the related-party GCLE input from Otsuka) into a captive, cost-controlled input. Two things physically change: (i) the Jammu plant reaching commercial production, and (ii) the disclosed in-house/third-party sourcing mix shifting from roughly 20% in-house toward the now-guided 80% in-house (B05.guidance; B04.moats_present).

B3. The proof gate: first commercial batch of 7-ACA produced at Jammu, at disclosed yield and quality meeting specification, guided to ~March 2027 (Q1 CY2027), reaffirmed on the two most recent calls; and thereafter, material cost as a percentage of revenue falling on a sustained basis below the FY2025/FY2024 baseline (63.5%, AR p.61) as captive supply displaces purchased 7-ACA/GCLE. Both halves are quarter-by-quarter observable (B04.must_track_metrics; B03.guidance_table).

B4. The recognition gap (OPEN QUESTION, resolved at Stage 11 via the PE gap; no number or conclusion stated here). Does current market pricing already credit Orchid for a successful R1-to-R2 climb, or does it still price the FY2022-25 audited entity (core score 29/100, ROCE never above 8.33%, AVOID classification)? This dossier states no per-share figure and no PE, because the share count itself does not reconcile against any primary filing (5.07 cr per the screener, 5.99 cr implied by the manifest market cap, 9.53 cr after the merger allotment, plus a further ~14.3 cr shares possible from promoter OCD conversion — Correction 4). Stage 11 computes the PE gap once the share count is resolved.

B5. The ugliness test. Today's ugly optics split into two readings that the corpus does not fully resolve, and the two readings are named rather than shaded to one:
- READING ONE (ARTIFACT-OF-CLIMB): FY2026's collapsed PBT (screener Rs 10.43 cr), the negative FY2025 free cash flow (minus Rs 41.06 cr against plus Rs 75.58 cr in FY2024), the Rs 447.22 cr guarantee and Rs 298.43 cr of consolidated capital commitments are the mechanical footprint of financing a large pre-revenue capex programme; interest and depreciation on capacity that does not yet earn is the expected shape of a capex cycle (B01.block_b_trend; B02.top_findings; Correction 1).
- READING TWO (STRUCTURAL-FEATURE): the sub-8.33% ROCE record runs across all four audited years FY2022-FY2025, predating the 7-ACA capex ramp that only began drawing debt in Q3 FY26; FY2026 revenue declined ~12% on every basis management stated, while both contemporaneous peers grew every quarter of the same year (B06.contradicted); and management went four consecutive calls without disclosing PBT, PAT, total debt or cash, a disclosure-quality pattern independent of the capex cycle (B05.red_flags; credibility grade C).
- MOST EVIDENCED READING: STRUCTURAL-FEATURE for the base business's weak returns and FY2026 decline (they predate and are not explained by the capex cycle alone, and peers moved the opposite way in the same year); READING ONE better explains the specific PBT collapse and negative FCF. The separating observation: whether blended ROCE recovers, and material cost % falls, in the first full year after 7-ACA commissions (tests the climb) versus whether it merely tracks interest/depreciation normalising without a margin improvement (tests the artifact reading alone).

B6. The transition falsifier: any further slip in 7-ACA commissioning past March 2027, a yield or quality shortfall once commercial-scale trials begin (management itself calls the ~800x pilot-to-commercial scale-up "a little unpredictable" — B07.flags FLAG-SCALEUP-UNCERTAIN), or Aurobindo Pharma's reported, larger (~2,000 MT/yr) competing 7-ACA project reaching the market first and capping the import-substitution opportunity Orchid can take (Correction 7.1).

**Line 2: Enmetazobactam / Orblicef / Exblifep licensing**

B1. FROM to TO: FROM pre-revenue optionality (closest ladder analogy is **R0 NON-OPERATING**, acknowledged as an imperfect fit since the ladder is built for operating businesses and this line has signed one deal but zero recognised revenue in the corpus) TO **R5 BRAND/SCARCITY OWNER** (patent-protected novel antibiotic, strategic-premium eligible if licensing scales — B07.moats_present).

B2. The engine: converting patent protection into signed, royalty/milestone-bearing licence agreements market by market. One is signed (Russia, ~$178m/10yr estimated value, B05.guidance); US, China, Latin America and Southeast Asia remain undated or "in discussion" as of the Q1 FY27 call.

B3. The proof gate: at least one further definitive licensing agreement, beyond Russia, signed and disclosed with its economics, within FY27 (B05.triggers priority 3, confirm_signal).

B4. The recognition gap: not assessed separately for this line in this dossier; folded into Line 1's open question above, since no per-share or PE figure exists in this corpus at all (Correction 4).

B5. The ugliness test: STRUCTURAL-FEATURE, most evidenced. The Enmetazobactam US out-licensing promise slipped across four consecutive quarters with decreasing specificity ("within 12 months" to "within this year" to "this/next quarter" to undated "in discussion" — B05.timeline_slippages), Europe absolute sales have been withheld for a full year, escalating from promised to confidentiality-refused to a declared blanket policy (B05.repeated_evasions), and the credibility grade is specifically weakest on financial/licensing disclosure. The counter-reading (ARTIFACT-OF-CLIMB: licensing deals are simply slow by nature) is weaker here because the pattern is one of decreasing specificity and unacknowledged misses, not merely long lead times.

B6. The transition falsifier: FY27 ends with zero further signed deals beyond Russia, or Europe absolute-sales non-disclosure continues past a full year (B05.triggers priority 3, kill_signal).

### PART C — WHAT THE MODEL WATCHES

**C1. Dominant variables** (derived from the engine and proof gate above, not the static snapshot):

1. 7-ACA commissioning-date adherence and, after commissioning, material cost % of revenue and in-house/third-party sourcing mix — the proof gate itself (B04.must_track_metrics; B05.triggers priority 1).
2. Base-business EBITDA margin sustaining a cyclical recovery: management guided ~12% for FY27; Q1 FY27 combined-basis actual came in at ~8.2%, though Verifier B's like-for-like reconstruction puts standalone-equivalent Q1 FY27 margin closer to the ~12% target — the two readings are unresolved in this corpus and both are carried (B05.guidance; B12b findings).
3. Enmetazobactam ex-India licensing conversion beyond the one signed Russia deal (B05.triggers priority 3).
4. Otsuka Chemical (India) Pvt Ltd / GCLE related-party input concentration trend, the sole-sourced input feeding the single largest cost line (B04.flags; B08.adverse_findings).

**C2. What the model rejects.** Whether the global or India-specific cephalosporin/7-ACA market is large enough: Stage 9 sized TAM at ~Rs 20,768-21,429 cr, SAM at ~Rs 1,768 cr, and found capacity is not the binding constraint — management's own no-further-capex ceiling (>Rs 1,200 cr turnover on the existing plant) exceeds the SOM (B09.tam_cr; B09.capacity_check). The binding constraint is execution: commissioning reliability, funding-gap resolution, and disclosure quality, not market size. The model also rejects brand/consumer-facing metrics (dealer network size, brand recall, same-store sales) since this is a B2B, purchase-order export business with no consumer-facing distribution (B04.irrelevant_ratios).

**C3. The business falsifier** (distinct from the transition falsifiers in B6; this would force a re-declaration of the FROM business itself, not merely kill the climb). Continued fund diversion from the earning business into the pre-revenue subsidiary without a matching, disclosed return: the corporate guarantee (Rs 447.22 cr, zero to full in one year, 34.0% of standalone net worth, 99.4% of all contingent liabilities, with no visible Ind AS 109 fair-value treatment even though guarantee commission income is booked on the same relationship), standalone capital commitments up ~797% within FY2025, and the base-business-earmarked QIP tranche (the Alathur API block) sitting at just 0.36% utilised while consolidated capital work in progress and commitments grew fastest (B02.top_findings; Correction 8.3). If this pattern continues alongside further non-disclosure of PBT, PAT, debt and cash, the FROM business would need re-declaration away from "an operating API exporter attempting a cost-position climb" toward "a capital source primarily funding and guaranteeing a separate pre-revenue subsidiary" — a materially different business to underwrite.

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE (draft)

**What the products are and why they matter.** Orchid Pharma manufactures cephalosporin active pharmaceutical ingredients (APIs), the chemical compound inside a widely used class of antibiotics. This single product line is 98.3% of FY2025 revenue; a related finished-dose formulation (FDF) line adds a further 1.7% (B04.revenue_streams; AR p.22). Two further lines carry no revenue today: Enmetazobactam, a patented novel antibiotic sold in India as Orblicef and in Europe as Exblifep, and Orchid AMS, a hospital antibiotic-stewardship service (B04.revenue_streams). The API matters because it is a regulated, dossier-locked input: each manufacturing site and molecule sits inside filed regulatory dossiers (48 US DMFs, 15 COS, 8 Japanese DMFs, 6 ANDAs), which is what lets a formulator keep buying from the same qualified source rather than switching on price alone (B04.moats_present; B07).

**Who buys, and why.** Customers are pharmaceutical formulators and manufacturers, not consumers. Exports are 80.10% of turnover across 48 countries (AR p.109; B04). They buy on purchase orders with no long-term contracts (B04.revenue_streams), and switching is slow because a supplier change requires re-filing regulatory dossiers with each customer's own regulator. On the two pre-revenue lines, the counterparty is named rather than diffuse: Cipla markets Orblicef in India, and Advanz Pharma holds the Europe licence for Exblifep (B04.revenue_streams). The corpus did not establish customer-count or top-customer concentration on the API line itself (B04.irrelevant_ratios notes the AR names "Customer Concentration and Relationship Risk" as a risk factor without disclosing a number).

**Why demand exists.** Demand is ordinary, recurring generic-antibiotic demand, priced on a cyclical, China-influenced cost curve rather than on brand or novelty (B04.pricing_power = "price-taker"; B04.cyclicality = "cyclical"). The economics turn on two inputs Orchid does not fully control: GCLE, sourced 100% from the related party Otsuka Chemical (India) Pvt Ltd, and 7-ACA, currently imported, mostly from China (B04.flags; B05.guidance). Management frames FY2026's ~12% revenue decline as an industry-wide slowdown, but both contemporaneous peers in this corpus (NEULANDLAB, GRANULES) grew revenue every quarter of the same year, which removes "a bad year for everyone" as the default reading, though it cannot confirm a cephalosporin-specific cause either, since neither peer sells the same product (B06.contradicted; Correction 5).

**Why demand grows, or does not.** Two growth paths exist on management's own account. First, India is substituting imported 7-ACA under the PLI scheme, where Orchid holds 1,000 MT/year of approved capacity; Aurobindo Pharma is reported to be building a larger, ~2,000 MT/year competing plant, which caps how much of that substitution Orchid alone can capture (Correction 7.1). Second, Enmetazobactam licensing can add income market by market, but the pattern to date is one signed deal (Russia) against four consecutive quarters of slipping, decreasingly specific promises on the larger US opportunity (B05.timeline_slippages). Stage 9 sizes the served-market opportunity (SOM) at roughly Rs 1,091-1,314 cr over three-to-five years, implying ~10% revenue CAGR from a base year that itself declined 12% — a moderate, not large, growth runway (B09.som_3yr_cr, som_5yr_cr, runway_class).

**Where the competitive advantage sits, and where it does not, per line.** On the API line, there is no pricing moat: per-kilogram realisations fell in FY2025 (oral ~Rs 1,536/kg, down 6.1%; sterile ~Rs 1,588/kg, down 11.4%, both computed from AR volume-and-value data, not company-stated per-kg prices — B04.unit_economics), and the emerging-moat scan scored 23 of 92 (MODEST), below the strategy's EM≥25 qualifier threshold (B07.em_score). The advantage that does exist is regulatory dossier depth and the company's claim to run "one of only three USFDA-approved sterile Cephalosporin facilities worldwide" (AR p.29), which is company-stated and uncorroborated by any third-party source in this corpus (B07.flags). The 7-ACA backward-integration project has no proprietary-process moat: the process and strain technology is licensed from an external partner who also supplies the named Chinese competitors, which actively undercuts rather than supports a process-advantage claim (B07.flags FLAG-PROCESS-TECH-SHARED). The Enmetazobactam patent is a genuine, documented moat, but it sits on a line with effectively no current revenue (B07.moats_present).

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. Verticals framed (one per Section 2 dominant variable)

**Vertical 1 — 7-ACA commissioning and the proof gate.** The corpus establishes: total project capex now guided at Rs 750 cr, up ~25% from the Rs 600 cr the FY2025 AR stated (B04.flags; Correction 6.1); a commissioning-date history that moved from December 2026 (AR) to September 2026 (Q3 FY26 call) back out to March 2027 (Q4 FY26 and Q1 FY27 calls, reaffirmed — Correction 6.3); and a funding picture with Rs 450 cr of debt planned and Rs 170 cr drawn as of Q3 FY26, against a funding gap of at least ~Rs 300 cr never addressed by management or any analyst (B05.flags). The corpus cannot establish: actual mechanical-completion status (the September 2026 checkpoint was dropped from disclosure without confirmation either way — B05.dropped_triggers), first-batch yield or quality (not yet available, guided for after March 2027), or how the remaining funding gap will be closed. Questions that decide it: (1) does a single-basis total debt/cash figure appear, naming the funding source, before the next commissioning checkpoint; (2) does material cost as % of revenue fall after commissioning; (3) does independent evidence (DGFT trade data, Aurobindo's own filings) corroborate or contradict the "nobody else is building" framing that underwrites the capex.

**Vertical 2 — Base-business cyclical margin recovery.** The corpus establishes: FY2026 revenue declined ~12% on every basis management stated (standalone Rs 922 cr to Rs 811 cr; restated combined Rs 1,398 cr to Rs 1,233 cr — Correction 1); Q1 FY27 combined EBITDA margin of ~8.2%, below the ~12% FY27 target management assented to, though Verifier B's reconstruction implies a like-for-like standalone-equivalent margin closer to 12% (B12b findings; B05.guidance). The corpus cannot establish: a reconciled, single-basis quarterly margin series going forward (management has not bridged EBITDA to PBT for four consecutive calls — B05.red_flags), nor whether the FY2026 decline is company-specific or cephalosporin-specific, since the peer set cannot test the product (Correction 5). Questions that decide it: (1) does Q2 FY27 combined revenue clear the Rs 304 cr / 8%+ EBITDA margin falsification line the synthesis names (gate-recommendation.md); (2) does the Dhanuka Laboratories EBITDA contribution stop being withheld; (3) does an independent trade-data source corroborate or contradict the "industry-wide slowdown" framing at the product level.

**Vertical 3 — Enmetazobactam ex-India licensing conversion.** The corpus establishes: one signed deal (Russia, ~$178m/10yr estimated — B05.guidance); a specific, testable commitment that "50% will be signed in for sure" within six months across five named markets, dated to ~November 2026 (B12b findings, missed by B05 run 1); and a $1-2bn lifetime sales framing ruled INFLATED by Stage 9 at 8.4x the only signed comparator (Correction 7.3). The corpus cannot establish: whether any further deal will actually sign, or the true addressable peak-year economics absent an independent, non-Orchid source. Questions that decide it: (1) does a second deal sign by ~Nov 2026 per management's own commitment; (2) does Europe absolute-sales disclosure ever appear; (3) does an independent industry comparable (beyond Stage 9's three already-tested comparables) corroborate or further discount the lifetime sales claim.

**Vertical 4 — Otsuka/GCLE related-party input concentration.** The corpus establishes: Otsuka Chemical (India) Pvt Ltd is the sole approved GCLE source, a related party in which the MD and a WTD hold board positions, with FY2025 purchases of Rs 230.72 cr (up 35.8% YoY) and shareholder approval sought for up to Rs 400 cr (~43% of FY25 turnover), with no external valuation or benchmarking disclosed (B08.adverse_findings; Note 50, AR p.213, verified at source). Combined with Dhanuka Laboratories purchases, related-party cost concentration reaches 27.3% of revenue and 43.0% of material cost (B03; Correction 8.1). The corpus cannot establish: whether the pricing is at, above, or below an arm's-length benchmark (no such disclosure exists), nor Otsuka's own economics. Questions that decide it: (1) does the purchase value rise past the Rs 400 cr shareholder-approved ceiling with no named alternate source; (2) does a second qualified GCLE source ever appear; (3) does Otsuka's own MCA-filed accounts, if obtained, show margins consistent with an arm's-length price.

### 4b. Candidate signal table

(Expanded from B09's downstream_candidates; UNVERIFIED, for Role 5.5 verification and tracker writes in claude.ai.)

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| China cephalosporin API / 7-ACA intermediate export volume and value to India | A sustained rise in Chinese export volume/value that does not track Orchid's own material-cost trend would undercut the "China dumping compressed our margin" narrative | Quarterly | India DGFT/DGCI&S trade statistics, or China customs export data (B09) |
| India antibiotic export quantity and value, all-India ex-Orchid | If all-India antibiotic exports grew while Orchid declined, the decline reads as company/product-specific, not sector-wide | Monthly | DGFT / Pharmexcil export bulletins (B09) |
| Otsuka Chemicals (India) Pvt Ltd, related-party GCLE supplier | Purchase value rising past the Rs 400 cr shareholder-approved ceiling with no named alternate source signals unmanaged concentration | Annual | AR related-party transaction note (Note 50) / MCA filings (B09; B08) |
| Aurobindo Pharma's competing 7-ACA project (reported ~2,000 MT/yr) | Aurobindo reaching commercial production before Orchid's March 2027 target caps the import-substitution opportunity Orchid can still take | Quarterly | Aurobindo Pharma investor presentations and concalls (B09; Correction 7.1) |
| Cipla Ltd, India Enmetazobactam/Orblicef marketing partner | Flat or declining Cipla commentary on Orblicef volumes would contradict management's India uptake narrative | Quarterly | Cipla quarterly results / investor commentary (B09) |
| Advanz Pharma, Europe Enmetazobactam licensee | Any disclosed absolute Exblifep sales figure resolves the one-year-withheld Europe number | Event-driven | Advanz Pharma company news/press releases (B09) |
| USFDA / DCGI regulatory approval and inspection status | A DCGI clinical-trial-waiver denial for Cefiderocol, or an adverse USFDA facility finding, would directly contradict the regulated-market growth thesis | Event-driven | USFDA Orange Book / inspection database; DCGI approval records (B09) |
| Dhanuka Laboratories Ltd's own filed FY26 accounts | A filed EBITDA figure inside the Rs 17-31 cr loss range confirms the bias-adjusted reading; inside the Rs 50-60 cr range confirms the face-value reading; a positive figure would contradict both (Correction 9) | Annual (MCA filing cycle) | MCA filed financial statements for Dhanuka Laboratories Ltd |

### 4c. Fragility read

- **variable_count: 7.** (1) 7-ACA commissioning and yield; (2) funding-gap closure (~Rs 300 cr+) without dilutive equity; (3) base-business cyclical margin recovery; (4) Enmetazobactam ex-Russia licensing conversion; (5) Dhanuka merger not a recurring EBITDA drag; (6) Otsuka/China input-cost trend; (7) Aurobindo's competing capacity not capturing the import-substitution opportunity first.
- **verifiability_ratio: "4 of 7 externally observable."** Externally observable: (1) commissioning, partly, via DCGI/PLI records and any independent site inspection; (6) Otsuka/China input trend, via DGFT trade data; (7) Aurobindo's capacity, via Aurobindo's own filings; and the Dhanuka question, via MCA-filed accounts. Company-narrated only, with no independent corroborating source found in this corpus: (2) the funding gap (total debt/cash undisclosed for two consecutive calls); (3) base-business margin (single-segment reporting, no independent segment source); (4) Enmetazobactam deal count (counterparty press could corroborate a signed deal, but the promise pattern itself is company-narrated).
- **single_point_failure:** the Rs 447.22 cr corporate guarantee for Orchid Bio-Pharma Ltd's borrowings crystallising (i.e., the subsidiary defaulting). It is a single legal event, 34.0% of standalone net worth, that could damage the base business regardless of how the other six variables resolve, and it carries no visible Ind AS 109 fair-value treatment in the corpus (B02.top_findings; Correction 8.3).
- **fragility_verdict: FRAGILE.** Seven variables, a majority company-narrated rather than externally verifiable, a four-quarter credibility grade of C weighted toward financial-disclosure evasions specifically, and a named single point of failure together place this above MODERATE.

### 4d. Research brief (claude.ai live-web work order)

1. PENDING LIVE VERIFICATION (Chain 1, Section 4e): Orchid Bio-Pharma Ltd's own accounts, lender sanction letters, or the FY2026 AR's borrowings note, to identify who funds the remaining ~Rs 300 cr of the 7-ACA capex gap.
2. PENDING LIVE VERIFICATION (Chain 2, Section 4e): Otsuka Chemical (India) Pvt Ltd's own MCA-filed accounts, to test GCLE pricing against an arm's-length benchmark.
3. The FY2026 Orchid Pharma audited annual results filing and the FY2026 Annual Report (BSE/NSE/company IR) — resolves the freshness-pair failure, the PBT/PAT reconciliation gap, receivables ageing, and the only clean ROCE base this run can use.
4. The Dhanuka Laboratories merger scheme document, fairness opinion, and swap-ratio valuation (BSE/NSE scheme filings) — resolves the share-count reconciliation named in Correction 4.
5. The post-allotment shareholding pattern (SAST filing, BSE/NSE) — resolves promoter and public holding, and pledge status, currently NOT FOUND beyond a weak-tier, web-derived claim.
6. The CARE Ratings rationale, Mar-2025 (careratings.com, egress-blocked in this container) — the likely source of independent working-capital commentary that would resolve the FLAG-CASH INDETERMINATE determination.
7. Dhanuka Laboratories Ltd's own filed accounts at the MCA — the single observation Correction 9 names as the one that separates the two readings of its FY26 EBITDA contribution (minus Rs 17-31 cr versus minus Rs 50-60 cr).
8. Aurobindo Pharma's 7-ACA project — quarterly investor presentations and concalls, to confirm capacity, timeline, and progress against the currently web-derived, unconfirmed ~2,000 MT/yr figure.
9. USFDA facility database or an independent industry report, to test the company-stated, uncorroborated claim of being "one of only three USFDA-approved sterile Cephalosporin facilities worldwide" (AR p.29).
10. DGFT/DGCI&S or China customs trade data on cephalosporin API and 7-ACA export volumes into India — an independent test of the China-dumping/pricing narrative.
11. Cipla (Orblicef, India) and Advanz Pharma (Exblifep, Europe) quarterly commentary — an independent read on Enmetazobactam offtake, since Orchid itself withholds absolute Europe sales.
12. A cephalosporin/7-ACA-relevant peer set, to replace or supplement NEULANDLAB/GRANULES/KOPRAN — needed before the product-specific claims (7-ACA pricing, competing capacity, Ceftazidime-Avibactam market size) can be tested at all (Correction 5).
13. K Raghavendra Rao and the pre-2020 promoter era — a SEBI/SFIO/ED case-database check, to close out the promoter background search this container's WebFetch could not complete (B08.searches_skipped).

### 4e. SECOND-ORDER STUB (Master Prompt v3.7, Rule F — floor of 5 reached in claude.ai)

```
CHAIN 1: 7-ACA Jammu plant reaches mechanical completion and first commercial batch, guided ~March 2027, reaffirmed on the Q4 FY26 and Q1 FY27 calls (B05; Concall_Jun_2026_Transcript.pdf; Concall_Aug_2026_Transcript.pdf)
Link 1 [documented, B04/Correction 6.1]: Total project capex is now disclosed at Rs 750 cr, up from the Rs 600 cr the FY2025 AR stated (AR p.20) — a ~25% overrun on the company's own numbers, unreconciled by any source in this corpus. Rs 450 cr of debt was planned and Rs 170 cr drawn as of Q3 FY26 (B05.guidance).
Link 2 [PENDING LIVE VERIFICATION]: who funds the remaining gap, and why now, needs counterparty evidence this container cannot reach. Named document for claude.ai to open: Orchid Bio-Pharma Ltd's own financial statements / bank credit-facility sanction letters at the MCA, or the FY2026 AR's borrowings note (Note 44 equivalent) once filed.
Link 3 [INFERENCE]: If the ~Rs 300 cr+ funding gap is not closed through debt already arranged, Orchid faces a choice between drawing further debt against an already-guaranteed subsidiary (compounding the Rs 447.22 cr contingent liability, Correction 8.3) or a dilutive capital raise into a share count that does not currently reconcile against any primary filing (Correction 4) — either path changes who bears the downside of a further commissioning slip, and neither has been named by management.
Binding constraint: the capex schedule shows the base-business-earmarked QIP tranche (the Alathur API block) at just 0.36% utilised of its Rs 99.46 cr allocation, while consolidated capital work in progress and capital commitments have grown fastest (B02 pass2; Correction 8.2) — capital is flowing to the growth engine, not the base business.
Unsaid: the company recognises guarantee commission income (Rs 5.28 cr FY25) on the Orchid Bio-Pharma relationship without any visible Ind AS 109 fair-value liability recognition for the Rs 447.22 cr guarantee itself, a footnote-level asymmetry never narrated on any of the four calls (B02.top_findings rank 1).
Observation that confirms or breaks this chain, and confirm-by date: a stated, single-basis total debt and cash figure with the funding source for the remaining 7-ACA capex named, due by the Q2/Q3 FY27 call (~Nov 2026-Feb 2027). Confirms if a funding source is named without new equity dilution; breaks toward higher risk if a further commissioning slip is announced with no funding update.

CHAIN 2: Otsuka Chemical (India) Pvt Ltd is the sole approved source of GCLE, a key raw material, with FY2025 purchase value of Rs 230.72 cr (up 35.8% YoY from Rs 169.90 cr) and shareholder approval sought for up to Rs 400 cr (B08.adverse_findings; Note 50, Annual_Report_2025.pdf p.213, verified directly at source)
Link 1 [documented, B08]: Otsuka's board includes MD Manish Dhanuka (Director and Member) and WTD Mridul Dhanuka (Member). Combined with Dhanuka Laboratories purchases, related-party cost concentration reaches 27.3% of revenue and 43.0% of material cost (B03; Correction 8.1).
Link 2 [PENDING LIVE VERIFICATION]: who sets the price, and why the trend keeps rising, needs counterparty evidence this container cannot reach. Named document for claude.ai to open: Otsuka Chemical (India) Pvt Ltd's own MCA-filed financial statements, to test whether GCLE pricing to Orchid sits at, above, or below what Otsuka's own margins imply an arm's-length price would be.
Link 3 [INFERENCE]: a sole-sourced, KMP-linked, undisclosed-pricing input feeding the single largest cost line (material cost 63.5% of revenue, AR p.61) gives the related party pricing leverage an arm's-length supplier would not have; the repeated deflection of a direct analyst question on the cost-share trend (Q1 FY27 call) is at minimum consistent with management not wanting that leverage made visible, which raises rather than resolves the possibility that some of the FY26/27 margin compression attributed to "China dumping" is a related-party pricing effect instead.
Binding constraint: no arm's-length or benchmarking disclosure exists in Note 50 itself for the Otsuka relationship (B08); the FY25-26 shareholder-approved ceiling of Rs 400 cr (~43% of FY25 turnover) is the only outer boundary the corpus discloses.
Unsaid: the Otsuka relationship is named nowhere in the AR's own risk-factors section, which speaks only generically of "a few countries and select suppliers" (AR p.58-59; B03.missing_risks) — a material omission the filing itself does not narrate.
Observation that confirms or breaks this chain, and confirm-by date: Otsuka's GCLE purchase value as a % of material cost in the next AR's Note 50/AOC-2, due at the FY2026 AR filing date (currently unknown — a corpus gap in itself). Confirms the dependency is being actively managed if a second qualified GCLE source is named or the ratio falls; breaks toward higher risk if the ratio rises past the Rs 400 cr ceiling with no named alternate source.
```

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in claude.ai with live web, before Role 2.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. Orchid Pharma makes cephalosporin antibiotic ingredient (API) and sells it to drug makers in 48 countries. This is 98.3% of its revenue.
2. A small finished-dose (tablet/capsule/injectable) line adds 1.7% more. Two other lines exist but bring in no revenue yet: a patented antibiotic (Enmetazobactam) and a hospital antibiotic-service business.
3. Orchid does not sell to shops or consumers. It sells in bulk, by the kilogram, on purchase orders, to other drug companies.
4. Customers buy from Orchid because its plant and product are locked into regulatory paperwork filed with drug regulators around the world. Switching suppliers means re-filing that paperwork.
5. Demand for the antibiotic ingredient itself is ordinary and steady. It is not growing fast; it moves with generic-drug demand and Chinese competitor pricing.
6. Orchid is trying two ways to grow. First, it is building its own plant to make the chemical block (7-ACA) it now buys, mostly from China. Second, it is trying to license its patented antibiotic to drug companies abroad.
7. The plant-building plan costs Rs 750 crore, a quarter more than first stated, and its opening date has moved twice, now set for March 2027.
8. The licensing plan has one signed deal (Russia) after four straight quarters of promises that kept slipping and shrinking in specificity.
9. Orchid has no pricing power on the core product: its price per kilogram fell in the most recent year even though it sold more volume.
10. Its one real edge is a patent on the new antibiotic and its history of passing strict manufacturing inspections, not brand or market share.
11. The company's return on capital has not cleared a healthy level in any of the last four audited years, before the big new factory project even began.
12. Revenue actually fell about 12% in the most recent year, while two comparable companies in this corpus grew. This is a business-specific problem, not simply a bad year for everyone.
13. This run's evidence checking found the analysis missed several important items on a first pass, including a stalled US product-filing plan, so the pipeline sent it back for rework rather than treating it as finished.
14. The newest full year of audited company results is missing from what we reviewed; only older, audited years and management's own verbal account of the newest year are available.
15. The two biggest open questions for the operator: how many shares the company actually has outstanding (three different counts do not agree), and who is actually paying for the roughly Rs 300 crore left to fund on the new factory.

---

## SECTION 6: STANDING EXTRACTION ANNEX

### 1. Units

No company-stated per-kilogram price is printed anywhere in this corpus. Stage 4 computed realisation from the AR's own volume-and-value figures on a clean page: "Oral realization (Rs/kg, computed from the above) | ~1,536 | ~1,636 | -6.1%" and "Sterile realization (Rs/kg, computed from the above) | ~1,588 | ~1,792 | -11.4%" (Annual_Report_2025.pdf, p.55, volume-and-value table; B04.unit_economics). Comment: this covers two baskets (oral vs sterile Cephalosporin), not one product; it is a computed blend across each basket's product mix, never a per-SKU price. NOT DISCLOSED: any per-unit figure for FDF, Enmetazobactam, or AMS.

### 2. Segment capital and debt

Quote, Note 45 "Operating Segments," standalone, Annual_Report_2025.pdf p.209 (printed footer p.208), directly re-read at source: "The operations of the Company falls under a single operating segment i.e., 'Pharmaceuticals' in accordance with Ind AS 108 'Operating Segments' and hence no segment reporting is applicable." The same note gives geography-only revenue: India Rs 18,091.22 lakhs (~Rs 180.91 cr) FY25 vs Rs 14,935.94 lakhs (~Rs 149.36 cr) FY24; Rest of the world Rs 72,823.17 lakhs (~Rs 728.23 cr) FY25 vs Rs 66,576.09 lakhs (~Rs 665.76 cr) FY24; total Rs 90,914.39 lakhs (~Rs 909.14 cr) FY25 vs Rs 81,512.03 lakhs (~Rs 815.12 cr) FY24. Comment: no segment assets, segment liabilities, capital employed, or borrowings are allocated by segment anywhere in this corpus, because the company discloses only one segment. Every ROCE figure in this run is therefore a blended, whole-company number (B04.flags; Correction 6.2).

### 3. Guidance versus aspiration

(a) Guidance with a period: "7-ACA commercial production... March 2027" reaffirmed on the Q4 FY26 and Q1 FY27 calls (B03.guidance_table; Concall_Jun_2026_Transcript.pdf; Concall_Aug_2026_Transcript.pdf). "AMS breakeven... FY27 target" (Concall_Nov_2025_Transcript.pdf p.8). "FY27 revenue growth target 10-15%" (Concall_Jun_2026_Transcript.pdf p.10). (b) Aspiration without a period: AMS division revenue "Rs.250-300 crore over three years" (Annual_Report_2025.pdf p.20) — no start date named against which the three years run. Enmetazobactam "$1-2 billion" lifetime sales, "peak year 4-5," undated relative to any launch anchor beyond "originating in 2021" (B03.guidance_table; Concall_Jun_2026_Transcript.pdf p.7). (c) Capacity/capability only: "existing plant can do more than Rs 1,200 cr turnover... without further capex" (B04.unit_economics key_lever). NOT DISCLOSED: any base-business-only revenue or margin guidance separate from the combined figures.

### 4. Concentration

Geography: exports 80.10% of turnover across 48 countries (Annual_Report_2025.pdf p.109; B04). Product: Cephalosporin API 98.3% of FY25 revenue, FDF 1.7% (AR p.22; B04.revenue_streams). Customer: NOT DISCLOSED. The AR names "Customer Concentration and Relationship Risk" as a top business risk (AR p.58-59) but states no customer count or top-customer percentage anywhere in this corpus (B04.irrelevant_ratios). Related-party input concentration (a cost-side, not customer-side, concentration): combined Otsuka Chemical and Dhanuka Laboratories purchases equal 27.3% of revenue and 43.0% of material cost (B03; Correction 8.1).

### 5. Promise ledger

From B05's promise_delivery table (four calls, Q2 FY26 to Q1 FY27; 2 delivered, 6 partial, 3 missed):

| Promised in | Promise | Outcome | Evidence anchor |
|---|---|---|---|
| Q2 FY26 call | Europe Exblifep sales figure next quarter | Missed | Refused on confidentiality across three further calls |
| Q2 FY26 call | Enmetazobactam US deal within ~12 months | Missed | No new date by Q1 FY27 |
| Q2 FY26 call | AMS breakeven by FY27 | Partial | Drag narrowed to Rs 0.5 cr/qtr by Q1 FY27, not zero |
| Q3 FY26 call | 7-ACA mechanical completion by Sept 2026 | Unresolved | Checkpoint dropped from both later calls |
| Q3 FY26 call | Cefiderocol production readiness Dec 2026 | Partial | Reaffirmed; equipment reroute absorbed |
| Q3 FY26 call | Enmetazobactam licensing deal every quarter | Missed | Directly admitted miss Q4 FY26; Russia delivered Q1 FY27, one quarter late |
| Q3 FY26 call | Base-business FY27 EBITDA margin ~10% | Partial | Revised to ~12%; Q1 FY27 actual ~8.2% combined basis |
| Q3 FY26 call | Cefiderocol India waiver confidence | Partial | Confidence softened by Q1 FY27 |
| Q4 FY26 call | Merger written order shortly after court vacations | Delivered | Effective 10-Jul-2026 |
| Q4 FY26 call | 7-ACA in-house/third-party split unchanged | Disputed | Numbers describe a reversal; management denied without disputing figures |
| Q4 FY26 call | Enmetazobactam US close this/next quarter | Missed | Still "in discussion" Q1 FY27 |
| Q4 FY26 call | Base-business FY27 revenue growth 10-15% | Partial | Mixed-basis comparison; management declined to reaffirm |
| Q4 FY26 call | 7-ACA commissioning Q1 CY2027 | On track | Reaffirmed Q1 FY27 |

(B05.promise_delivery)

### 6. Restated bases

Quote, Note 57, standalone, Annual_Report_2025.pdf p.223 (printed footer p.222), directly re-read at source: "Previous year figures have been regrouped or rearranged wherever considered necessary." Comment: this is generic and unquantified; no specific reclassification is named at this note. Separately, this stage's own review found an actual reclassification: the Rs 7.89 cr FY2024 current portion of the Orchid Bio-Pharma loan (Note 15-19) was rolled into the new Rs 108.24 cr non-current loan balance (Note 7) rather than repaid (B02.restatements_found). On concalls, the FY2026 combined-basis comparatives (restated to include Dhanuka Laboratories retroactively to an appointed date of 1-Apr-2024) set a combined FY2026 against what was, a year earlier, reported as a standalone FY2025 — the consolidation-scope artifact named in Correction 1.

### 7. Corporate-action clauses

Quote, Note 56, standalone, Annual_Report_2025.pdf p.223 (printed footer p.222), directly re-read at source: "The Company has submitted a petition with the Hon'ble National Company Law Tribunal (NCLT), Chennai bench, for amalgamation of its Holding Company Dhanuka Laboratories Limited ('the Amalgamating Company') with the Company in compliance with Section 230-232 and other relevant provisions of the Companies Act 2013... Further, the Hon'ble NCLT have pronounced the order dated 29.04.2025, inter-alia, issuing directions for convening meetings of equity shareholders of the Company and unsecured creditors of both Companies..." Comment: Note 56 itself does NOT state the appointed date, the effective date, or the share-exchange (swap) ratio. Those figures — appointed date 1-Apr-2024, effective date 10-Jul-2026, swap ratio 161 Orchid shares per 5 Dhanuka Labs shares, 4,45,86,052 new shares allotted 1-Aug-2026 — are WEB-DERIVED (B08.adverse_findings, evidence tier MEDIA REPORTED), since the scheme document and any fairness opinion are not in this corpus and were not reachable via WebFetch (B08.searches_skipped). Also from Note 55 (same pages, directly re-read): the Rs 391.80 cr (Rs 39,180 lakhs) QIP of 27-Jun-2023 is fully accounted, with the Alathur API-block bucket at Rs 36.00 lakhs utilised of Rs 9,982 lakhs allocated — 0.36% utilised, as Correction 8.2 states.

### 8. Related-party perimeter

Quote, Note 50(a)/(b), standalone, Annual_Report_2025.pdf p.214 (printed footer p.213), directly re-read at source. Holding company: Dhanuka Laboratories Limited. Subsidiary companies: Orchid Pharmaceuticals Inc. USA, Orgenus Pharma Inc. USA, Orchid Pharma Inc/Karalex Pharma USA, Bexel Pharmaceuticals Inc. USA, Diakron Pharmaceuticals Inc. USA, Orchid Bio-Pharma Limited. Associate company: Orbion Pharmaceuticals Private Limited. Enterprises in which the KMPs have control/significant influence: Otsuka Chemical (India) Pvt Ltd, Synmedic Laboratories, Dhanuka Agritech Ltd., Invest Care Real Estate LLP, Golden Overseas Private Ltd., M D Buildtech Private Ltd., Agrihawk Technologies Private Ltd., Star Living Infrastructure Advisors LLP, Dhanuka Chemicals Private Ltd., H D Realtors Private Ltd., Turbos Advisers LLP. Latest year (FY2025) transaction amounts from the same note's table: purchase of goods from "enterprises in which KMP have significant influence" Rs 23,074.07 lakhs (~Rs 230.74 cr) FY25 vs Rs 17,012.94 lakhs FY24; corporate guarantee issued to subsidiary/associate companies Rs 44,722.00 lakhs (~Rs 447.22 cr) FY25 vs Nil FY24; loan given to subsidiary Rs 10,035.35 lakhs FY25 vs Rs 766.44 lakhs FY24; interest received from subsidiary Rs 466.35 lakhs FY25 vs Rs 13.33 lakhs FY24; remuneration and short-term benefits to KMP and relatives Rs 843.86 lakhs FY25 vs Rs 777.66 lakhs FY24. Comment: the purchase-of-goods figure matches the Otsuka GCLE finding at Correction 8.1; the guarantee figure matches the Orchid Bio-Pharma finding at Correction 8.3.

### 9. Pledge and shareholding

NOT DISCLOSED in this corpus. No SAST or shareholding-pattern XBRL filing exists in inputs/shareholding/ (empty — B00.inventory.shareholding = 0). Promoter holding at the FY2025 AR date is 69.84%, stated unchanged (B01.analyst_note), but no twelve-quarter trend exists in this corpus. Pledge: B08's own field states "pledge_pct_latest: NOT FOUND" and "pledge_trend: NOT FOUND -- no SAST/shareholding-pattern filing in corpus; web search (2026-09-06) found a secondary-source claim of 'no pledge reported'... this is web-derived and not confirmed against a primary BSE/NSE pledge disclosure" (B08). Institutional holding: mutual funds held 18.79% as of 31-Mar-2025 per the FY2025 AR (B08.transition_evidence); no FII/DII split beyond that single data point exists in this corpus.

### 10. Verification

Documents quoted in this annex: Annual_Report_2025.pdf (32nd Annual Report, FY2024-25) — pages 55, 209 (printed 208), 213-214 (printed 212-213), 222-223 (printed 221-222), 30 (printed 29), directly re-read via the Read tool with the pages parameter for every figure taken from a page tagged [OCR:embedded-CORRUPT] in the work/text extract, per the binding rule at Correction 3. Concall_Nov_2025_Transcript.pdf, Concall_Feb_2026_Transcript.pdf, Concall_Jun_2026_Transcript.pdf, Concall_Aug_2026_Transcript.pdf — all clean OCR, quoted as extracted. Blocks B00 through B09, B12a through B12d, confidence.yaml, and B13-synthesis, all dated 2026-09-06.

CORPUS COMMIT HASH: fc45249d591fa0f9f8044db3e762dd24f057009d
