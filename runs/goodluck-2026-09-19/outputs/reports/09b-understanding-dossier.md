# HALT 1 UNDERSTANDING DOSSIER — Goodluck India Ltd (GOODLUCK)
Run date: 2026-09-19. Assembled from committed blocks B00-B09, verifier blocks B12a-B12d, and confidence.yaml. No new research. No valuation.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

1. **CONCALLS.** Four Goodluck transcripts held: Q2 FY26 (Concall_Nov_2025_Transcript.pdf, filed 14-Nov-2025, backward context), Q3 FY26 (Concall_Feb_2026_Transcript.pdf, filed 20-Feb-2026), Q4 FY26 (Concall_Jun_2026_Transcript.pdf, filed 03-Jun-2026), Q1 FY27 (Concall_Aug_2026_Transcript.pdf, filed 17-Aug-2026) (B00). Most recent quarter covered: Q1 FY27 (quarter ended 30-Jun-2026). Given the run date of 19-Sep-2026, Q2 FY27 (quarter ended 30-Sep-2026) has not yet closed, so no transcript is plausibly missing. Nine peer transcripts also held (HITECH x4, RATNAMANI x4, BALUFORGE presentation x1) (B00).

2. **ANNUAL REPORTS.** Two held: FY26 AR (224pp, filed 08-Sep-2026, primary) and FY25 AR (236pp, filed 02-Sep-2025, backward context) (B00). The latest completed FY (FY26, year ended 31-Mar-2026) is present. Only 2 years are held, not the 3+ years the audit ideally wants; Gate 0 (B01) ran ROCE, Net Debt/EBITDA, Interest Coverage and WC-days trend on FY24-FY26 only (3 years) because no pre-FY24 consolidated Balance Sheet exists in the corpus.

3. **RESULTS FILINGS.** Latest quarterly filing: Q1 FY27 board outcome, 06-Aug-2026 (20260806-Results_Q1FY27_Board_Outcome.pdf). Also held: Q4 FY26/FY26 audited (26-May-2026) and Q3 FY26 (13-Feb-2026); Q2 FY26 preserved in inputs/other/ (B00). No quarter-gap to the latest AR (FY26 AR, filed 08-Sep-2026, is newer than the Q1 FY27 results it does not yet cover — the AR covers FY26, the results filing covers the subsequent Q1 FY27 quarter, both current). All four results filings carry a garbled OCR text layer on the financial tables; figures were read from the rendered page images, the AR, presentations, or the screener Data_Sheet (B00).

4. **INVESTOR PRESENTATIONS.** Latest held: 20260808-Investor_Presentation.pdf, content Q1 FY27 (quarter ended 30-Jun-2026); its cover letter is misdated 08-Aug-2025, a filing artefact, period taken from content (B00). Presentations for Q2 FY26, Q3 FY26 and Q4 FY26 also held.

5. **RESEARCH / RATING.** No broker research held (ABSENT, B00, LOW severity). Two rating rationales held: CRISIL (30-Jun-2026, upgrade to AA-/Stable/A1+) and India Ratings (14-Jul-2026, IND AA-/Stable/IND A1+, consolidated view including GDAL) (B00). Both are full rationales for the PARENT. No rating rationale for the subsidiary GDAL is held (see item 7).

6. **CORPORATE ACTIONS.** 37 Reg 30 announcement filings held, 25-Sep-2025 to 11-Sep-2026, deduplicated (B00). These cover the GDAL preferential issue (06-Aug-2026), the bonus issue (07-Jul-2026 intimation, 24-Aug-2026 allotment), the Goodluck Green Energy amalgamation in-principle approval (11-Jul-2026), subsidiary closures, orders, ratings, and the SAST 29(2) promoter-sale disclosure (01-Jul-2026, image-only).

7. **FRESHNESS PAIR CHECK.** Per B00 `freshness_pairs[]`, one pair FAILED: RATING BULLETIN to RATIONALE. Trigger document: inputs/announcements/20260813-Intimation_Of_New_Credit_Rating_Assigned_By_India_Ratings_To.pdf (India Ratings IND A+/Stable/IND A1+ on GDAL bank facilities Rs 2,050 mn, 13-Aug-2026). Mate expected: India Ratings' full rationale for Goodluck Defence and Aerospace Ltd, Aug-2026. Status: FAIL — not found in the corpus, and not found by web search on 2026-09-19 either (B00). The other three pairs (RESULTS to CONCALL; SEBI ORDER to ORDER TEXT — no SEBI order referenced anywhere in the corpus; AR to LATEST AUDITED RESULTS) all PASS.

8. **VERDICT LINE: CORPUS GAPPED-FRESHNESS.**
   Missing mate document (freshness cap): **India Ratings rationale, Goodluck Defence and Aerospace Ltd (IND A+/Stable), Aug-2026** — expected source: indiaratings.co.in press release. This is findable-but-missing, not plausibly-nonexistent (the rating itself was assigned and announced; the underlying rationale document should exist).
   Additional gaps, all carried forward under this verdict:
   - Shareholding: screener aggregator table only (Dec-2023 to Aug-2026), not the BSE Reg 31 filing. No pledge column exists in the aggregator; pledge is evidenced only via B08's web search (0%, MEDIA REPORTED tier), not a primary filing. Expected source: BSE/NSE quarterly Reg 31 filing. MEDIUM severity.
   - Screener P&L/Balance Sheet/Cash Flow/Quarters export sheets: empty (formulas, no cached values) for GOODLUCK and all three peers; only Data_Sheet populated. LOW severity, core numbers cross-verified against both ARs.
   - No broker/equity research corpus. LOW severity; blocks peer-dependent moat tests M2/M5/M6/M8/M9 in part.
   - BALUFORGE holds no earnings calls; represented by one investor presentation (company-claim tier, no analyst Q&A). MEDIUM severity — findable-but-missing is the wrong frame here; BSE filings for BALUFORGE (531112) show no transcripts in the last 12 months, itself a data point on that peer's disclosure culture, not Goodluck's.
   - RATNAMANI's latest transcript is Q4 FY26 (May-2026); two of four held are FY25 vintage. LOW severity.
   - The 20260701 SAST 29(2) promoter-sale disclosure is image-only (6 of 6 pages); no OCR text layer, pages rendered to PNG and read visually. MEDIUM severity, resolved by visual read (B08).
   - GDAL's own statutory auditor identity and the audit-fee/non-audit-fee split: NOT FOUND in either AR's extracted text (B03).
   - Precision Pipes & Auto Tubes segment TAM and Balu Forge FY26 revenue: NOT FOUND by web search (B09), leaving the company's second-largest revenue line (27% of sales) without an independent market-size cross-check.
   This verdict caps the phase-1 gate recommendation at PROCEED WITH CAVEATS per the orchestrator's rule (confirmed in outputs/final/gate-recommendation.md) and is not softened to plain CORPUS GAPPED.

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT - PENDING OPERATOR SIGN-OFF.** This declaration is not signed. Signing happens only in claude.ai after live-web stress-testing.

### PART A — THE FROM STATE

**A1. ARCHETYPE (per line).**
- CR Coils, Pipes & Tubes (34% of FY26 revenue, B04): **Commodity converter** (Section 1B v3.7 Amendment 17 binds). Formula pass-through on the hot-rolled-coil price; 3-5% margin (business-narrative.md, sourced from B04).
- Precision Pipes & Auto Tubes (27%, B04): **Build-to-spec component maker.** OEM spec-in under IATF 16949; customers include VW, Audi, BMW, Mercedes-Benz, TVS, Bajaj, Toyota, Tata Motors (B04, B06).
- Engineering Structures & Precision Fabrication (24%, B04): **Order-book business** (EPC/capital-goods variant). Bridges, girders, solar and transmission structures against project orders (B04).
- Forging Products (15%, B04): **Build-to-spec component maker.** Flanges, shafts, gear rings for oil & gas, industrial and defence users (B04).
- Defence & Aerospace, GDAL (1.1% of FY26 revenue on a partial year; ~6% of the Q1 FY27 run-rate, B04): **Licence/scarcity business.** Arms Act Industrial Licence across five calibres, DGQA-certified; CRISIL frames it as facing "negligible competition" (B04, B07).

**A2. THE SIMPLE ANALOGY.** Goodluck buys steel and turns it into five product families across seven plants in Uttar Pradesh and Gujarat with 500,000 tonnes of installed capacity (B04, B09). Most of what it sells is priced off the hot-rolled-coil benchmark: a buyer pays for tonnage, not for a brand. A smaller, more specialised slice is drawn and forged to a customer's exact tolerance, so switching supplier means re-qualifying the part. A separate government-facing slice, run through a subsidiary, makes artillery shell bodies under a licence very few Indian private companies hold. Today this is a steel processor with a small, newly-commercial defence sideline bolted on, not yet a defence company with a steel sideline (B04).

### PART B — THE TRANSITION

**B1. FROM → TO (two lines).**

*Line: Core steel processing (CR/Pipes/Tubes, Precision Pipes & Auto Tubes, Forgings, Engineering Structures).*
FROM: **R1 COMMODITY PRICE-TAKER** (the CR base earns 3-5% on formula pass-through with no pricing power, B04/business-narrative). TO (claimed): **R3 VALUE-ADDED / SPEC'D SUPPLIER** (partial pricing power from spec-in and switching costs in tubes and forgings; value-added mix share rising from 64% to 66% of sales in FY26, B04).

*Line: Defence & Aerospace (GDAL).*
FROM: **R0 NON-OPERATING / ACCOUNTING-DRIVEN** (GDAL held no commercial production before Oct-2025; it existed as a capitalised subsidiary with no operating engine, B04/B03). TO (claimed): **R5 BRAND / SCARCITY OWNER neighbourhood** (licence-scarcity thesis: Arms Act exclusivity, DGQA certification, CRISIL's "negligible competition" framing; B00's sector-cap note names a candidate SOTP row of "Defence/strategic 38x" for this slice, explicitly a phase-3 ruling not applied here, B00/B07).

**B2. THE ENGINE.**
- Core: the mix shift itself — revenue growing slower (FY26 total income +4.1%) than EBITDA (+26.0%) purely because higher-margin tubes/forgings/structures took share from the CR base; gross margin rose from about 27% to 33% (B04).
- GDAL: the licence unlocks government shell orders at a margin the CR base cannot earn (30-35% guided defence EBITDA margin vs single-digit standalone margin), and capacity is being expanded from 150,000 to 400,000 shells/year via a ~Rs 500cr Phase-2 capex (B04, B07, B05).

**B3. THE PROOF GATE.**
- Core: value-added revenue mix (ESF + Forging + PPAT) sustaining at or above 66% of sales for two or more consecutive quarters, without the standalone EBITDA margin (9.17% in Q1 FY27, down 57bps YoY per outputs/final/gate-recommendation.md, sourced B12b) continuing to fall. Until margin stabilises in the core, the mix-shift climb shows up only in the subsidiary.
- GDAL: quarterly defence revenue sustaining Rs 75-88cr/quarter (the pace the Rs 300-350cr FY27 guide needs) at a 30-35%+ EBITDA margin for two or more consecutive quarters. One clean quarter exists so far (~Rs 81.5cr at 36-38% margin, Q1 FY27, B05/B12b) against a management credibility grade of D on seven tracked promises (B05).

**B4. THE RECOGNITION GAP (open question, resolved at Stage 11).** Whether the market already prices in the TO state — a value-added core re-rating plus a scarcity-premium defence slice — is an open question this dossier does not answer. If the current multiple already sits in the neighbourhood the TO rungs imply, the re-rating engine named in B2 is already spent and only earnings growth would remain; if it does not, the engine is still available. Stage 11 resolves this via the Section 1B PE gap. No number, no fair value and no conclusion is stated here.

**B5. THE UGLINESS TEST.** Today's ugly optic: free cash flow negative in all three measurable years (cumulative -Rs 722.41cr FY24-FY26 against cumulative PAT +Rs478.61cr), borrowings roughly doubling (Rs 612cr to Rs 1,119cr, FY24-FY26), and inventory days rising to 84 at FY26 close (B01, B02, B03; India Ratings, 14-Jul-2026 p.3).
- **ARTIFACT-OF-CLIMB reading (most evidenced):** the capex half of the cash gap tracks the documented multi-year capex programme (Rs 196-491cr/year, FY24-26) funding both the core capacity add and GDAL's build-out; India Ratings itself expects free cash flow to stay negative near-term "due to the capex to be incurred in both GIL and GDAL for the additional capacities" (IndRa Rationale, 14-Jul-2026, p.3).
- **STRUCTURAL-FEATURE reading (the other observation):** the inventory build (+29.1% YoY against +3.35% revenue) is tied by India Ratings to "delays in dispatches," not to growth, and ROE has declined four consecutive years (B01, B03).
- **The observation that separates them:** inventory days in the H1 FY27 balance sheet. A fall back toward the 63-69 day range of FY24-FY25 supports ARTIFACT; staying at 84 days or above supports STRUCTURAL (outputs/final/gate-recommendation.md, sourced B02/rating rationales).

**B6. THE TRANSITION FALSIFIER (kept separate from the business falsifier, C3).**
- Core: value-added mix reverting toward the CR-heavy historical split, or gross margin reverting from 33% toward the mid-20s without a stated cause (B04).
- GDAL: a second slip on the 400,000-shell Phase-2 timeline past the already-revised Q4 FY28 commercial date (the original guide was "within one year" from Oct-2025, already a confirmed slip, B05), or the order book remaining unquantified across further calls while the FY27 revenue guide holds unchanged (B05, B12b CRITICAL finding).

### PART C — WHAT THE MODEL WATCHES

**C1. DOMINANT VARIABLES.**
1. Value-added revenue mix % (ESF + Forging + PPAT). Current state: 66% of FY26 sales, up from 64% (B04).
2. GDAL quarterly defence revenue vs the Rs 300-350cr FY27 guide. Current state: ~Rs 81.5cr at 36-38% margin in Q1 FY27, one quarter only (B05, gate-recommendation.md).
3. Consolidated CFO/PAT ratio and inventory days. Current state: CFO/PAT 0.96x FY25, 1.10x FY26; inventory days 84 at FY26 close vs 63-69 in FY24-FY25 (B02, B03, rating rationales).
4. GDAL 400,000-shell Phase-2 execution timeline. Current state: targeting construction complete Sept-2027, commercial Q4 FY28, after one confirmed slip from "within one year" (Oct-2025) (B05).

**C2. WHAT THE MODEL REJECTS.** Market-size questions are not the binding constraint here. B09 sizes the serviceable market at Rs 44,120cr against Goodluck's current ~9.3% share, an 11x-headroom, STRONG-runway read; the SOM-implied CAGR (9.0-9.3%) is lower than the 15-20% guide only because the model rejects extrapolating the guide, not because the market is small. The model also rejects two specific management-sourced sizing claims as noise: the CMD's domestic 155mm shell demand figure (4.8 million shells/year), which implies a market about 24.5x this run's own conservative defence TAM (B09, flagged inflated), and the 30%+ solar-structures market-share claim, against an implied 3.2-4.6% on the company's own guided revenue (B09, flagged inflated). The binding constraints are execution (order-book disclosure, capacity-timeline delivery) and cash conversion, not market size.

**C3. THE BUSINESS FALSIFIER (distinct from B6; forces re-declaring the FROM business itself).** Net Debt/EBITDA crossing 3x together with Interest Coverage falling below 3x — the Gate 0 deal-breaker-6 AVOID trigger, and the run already sits within 0.3-0.4x of it on both metrics from opposite sides (2.69x and 3.32x, B01) — combined with a covenant event on the new Rs 275cr parent guarantee for GDAL's HDFC Bank facility (release covenant: Debt/EBITDA <=1.50x at the standalone borrower for three consecutive years, per the 11-Jul-2026 Reg 30 filing). Either event would mean the core steel-processing business itself, not just the transition, is under distress. A second falsifier: any auditor qualification, going-concern flag, or SFIO/regulatory action tied to the unresolved GDAL ownership and undisclosed related-party questions (B03, B08) would re-declare the FROM business's own governance integrity, separate from whether the transition is climbing.

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

*(Per prompts/13-synthesis-pipeline.md, the five-question spec, drafted at Halt 1 from B01-B09. Stage 13's copy is the version that stays current after this run.)*

Goodluck India manufactures five product families from steel. Cold-rolled coils, pipes and hollow sections (34% of FY26 revenue) are priced on a formula that tracks the hot-rolled-coil benchmark; a buyer pays for tonnage, and cannot easily do without them only in the sense that steel itself is unsubstitutable, not because Goodluck's version is special (B04). Precision Pipes & Auto Tubes (27%) are drawn to automotive tolerances under IATF 16949 certification; once an OEM qualifies a part on Goodluck's tube, switching supplier means re-qualifying it, which is why this line carries real, if moderate, switching costs (B04, B07). Engineering Structures & Precision Fabrication (24%) are bridges, girders, and solar/transmission structures sold against project orders; forgings (15%) are flanges, shafts and gear rings up to 14 tonnes for oil & gas, industrial and defence buyers (B04). Since October 2025, subsidiary Goodluck Defence and Aerospace (GDAL, 79.43% owned per the FY26 AOC-1) makes 105mm-155mm artillery shell bodies under an Arms Act licence and DGQA certification; this was 1.1% of FY26 revenue on a partial year and about 6% of the Q1 FY27 run-rate (B04, B03).

Customers are named by class, not concentration risk: Volkswagen, Audi, BMW, Mercedes-Benz, TVS, Bajaj, Toyota and Tata Motors for tubes; Indian Railways, L&T and NTPC for structures; Reliance, L&T Defence, HAL and Indian Oil for forgings; the Government of India for shells (B04, B06). The FY26 AR states the company serves "over 600 customers across more than 100 countries" with "no significant concentration of credit risk" (AR2026 p.38, p.152-153).

Present demand ties to six named downstream signals from B09 Section 6: the India National Infrastructure Pipeline and Union Budget capex (Engineering Structures), MNRE/CEA solar capacity addition data (solar structures within Engineering Structures), global automotive OEM production volumes (Precision Pipes & Auto Tubes), Indian Railways/NHSRCL high-speed-rail milestones (Engineering Structures), India oil & gas E&P and refinery capex announcements (Forgings), and the Union Budget defence capital acquisition allocation (GDAL). Two documented facts anchor forward demand: India reserves a share of its FY27 defence capital acquisition budget for domestic suppliers, and India crossed 500 GW of installed renewable capacity in FY26 (B09, AR2026 p.61). NATO/EU rearmament procurement is a named but unconfirmed potential export channel for GDAL; no export order is yet disclosed (B09).

Competitive advantage sits unevenly across lines. GDAL carries the only documented moat in the B07 scan: the Arms Act licence and DGQA certification, categories A1 and R1, both scored Strong, corroborated externally by CRISIL's "negligible competition" framing rather than management self-praise (B07) — though a verifier later found A1 and R1 credited the identical evidence twice and reduced the combined emerging-moat score from 19 to 14-15 (B12c). Tubes and forgings hold a moderate qualification-lock-in moat (category B2) from OEM spec-in under IATF 16949/EN 9100 (B07). The export line holds a moderate China+1 position on filed FY26 FOB export growth of about 9.6-10% (B07, B12c corrected this from a single-quarter presentation figure). The cold-rolled base and the Engineering Structures line show no moat in the B07 scan: the CR base earns 3-5% on pass-through pricing, and Engineering Structures scored nothing in any moat category (B04, B07). Execution (category F2) and working-capital improvement (category G2) both scored explicitly negative, against the B05 concall promise-delivery record and the B01 working-capital trend; talent (categories I1, I2) scored zero by design, evidenced only as a hiring narrative (B07). The licence itself is not an absolute barrier to rival supply: peer Balu Forge has commissioned a 360,000-shell line, more than double Goodluck's current 150,000-shell base (B06).

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. Verticals framed (one per Section 2 C1 dominant variable)

**Vertical 1 — Value-added revenue mix %.** The corpus establishes the FY26 value-added share (ESF+Forging+PPAT) at 66% of sales, up from 64%, and that FY26 total income grew 4.1% while EBITDA grew 26.0% on this mix shift alone (B04). It cannot establish a clean quarterly cadence for this metric, because Goodluck reports a single Ind AS 108 segment in both the standalone and consolidated financial statements ("hence there are no reportable segments," AR2026 p.179 standalone, p.221 consolidated); the 34/27/24/15/6 split comes from a percentage chart in the AR's narrative pages, not an audited segment note, and B04 flags an unreconciled internal inconsistency between that chart and the AR's own segment-level rupee figures. Questions that decide it: (1) does the next quarterly presentation deck restate the mix percentages consistently with the AR's rupee figures; (2) does the standalone EBITDA margin (9.17% Q1 FY27, down 57bps YoY) keep falling even as the blended/consolidated margin rises, which would mean the mix-shift climb is confined to GDAL; (3) can the CR/ESF rupee-vs-chart conflict (B04 FLAG-REVENUE-MIX-INTERNAL-INCONSISTENCY) be resolved against the next AR.

**Vertical 2 — GDAL quarterly defence revenue vs the FY27 guide.** The corpus establishes one clean quarter (~Rs 81.5cr at 36-38% margin, Q1 FY27, calculated as consolidated minus standalone) against a Rs 300-350cr FY27 guide needing roughly Rs 75-88cr/quarter (B05, gate-recommendation.md). It cannot establish an order book: management has not quantified the GDAL order book across four analysed calls, and the horizon claimed for it has shifted (no order book / 8 months / 1 year / 2 years) against a single disclosed order of Rs 307cr (B12b CRITICAL finding). It also cannot establish whether the 36-38% margin is a steady state or a ramp-up artefact; management held its own 30-35% guide flat even as delivered margins ran 38-70% in the first three quarters of production (B05). Questions that decide it: (1) does Q2/Q3 FY27 sustain the Q1 pace and margin; (2) does management ever quantify the order book, or does a fifth dodge itself become the signal; (3) is the 30-35% guide raised, held, or cut once a full FY27 run-rate year closes.

**Vertical 3 — Consolidated CFO/PAT and inventory days.** The corpus establishes CFO/PAT at 0.96x FY25 and 1.10x FY26, inventory days rising from 63-69 (FY24-25) to 84 (FY26), and free cash flow negative all three measurable years (B01, B02, B03; CRISIL and India Ratings rationales). It cannot establish whether the FY25 comparative receivables ageing table is genuine, because Note 8's FY25 comparative is numerically identical, bucket for bucket, to the FY26 table (B02) — an unresolved disclosure-integrity gap, not merely a data gap. It also cannot establish GDAL's own working-capital or leverage position independently, because the GDAL-specific rating rationale (the freshness-pair failure named in Section 1) is absent. Questions that decide it: (1) does the H1 FY27 balance sheet show inventory days falling back toward 63-69 or holding at/above 84; (2) can a corrected FY25 ageing schedule be sourced from the original FY25 AR as filed on BSE; (3) does the GDAL Aug-2026 India Ratings rationale, once located, show the subsidiary's own cash conversion separately from the parent's.

**Vertical 4 — GDAL 400,000-shell Phase-2 execution timeline.** The corpus establishes the current target (construction complete Sept-2027, commercial Q4 FY28) and one confirmed slip from the original "within one year" (Oct-2025) guide, via the 06-Aug-2026 Reg 30 filing (B05). It cannot establish firm financial closure for the ~Rs 500cr Phase-2 capex, nor reconcile the AR2026 Capital Discipline table's contradictory ~INR 400 Mn figure for the same capex against the Reg 30 filing's ~Rs 500cr (B07 FLAG-B07-CAPEX-TYPO). It cannot establish the identity of GDAL's non-promoter minority investor(s) behind either the Dec-2023 (Rs 136.5cr) or Aug-2026 (Rs 285cr) raises, despite an exhausted search (B08). Questions that decide it: (1) does a Reg 30 filing or the FY27 AR confirm financial closure and a construction start; (2) is any further timeline slip disclosed; (3) does the GDAL minority-investor identity surface in the next AOC-1, an MCA filing, or the missing GDAL rating rationale.

### 4b. Candidate signal table

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| Union Budget defence capital acquisition allocation | Domestic-supplier reservation share cut or flat in the FY28 Budget vs the FY27 baseline | Annual | PIB / Ministry of Defence, Union Budget documents |
| NATO/EU rearmament procurement (ReArm Europe, US Replenish) | No GDAL export order or RFQ named within 12 months of a major procurement announcement | Event-driven | NATO/European Defence Agency procurement releases, trade press |
| India National Infrastructure Pipeline / Union Budget capex | NIP capex allocation to core infrastructure sectors declines YoY | Annual | PIB / Union Budget documents |
| MNRE/CEA India solar capacity addition data (GW/year) | Monthly capacity additions fall below the run-rate implied by the FY27 Rs 600-700cr solar-structures guide | Monthly | MNRE / CEA reports |
| Global automotive OEM production volumes (VW, Audi, Tata Motors, TVS, Bajaj) | Aggregate production volumes at named OEMs decline for 2+ consecutive quarters | Monthly | SIAM / OEM production disclosures |
| Indian Railways / NHSRCL high-speed-rail milestones | No milestone achieved or contract awarded in a rolling 12-month window | Quarterly | Indian Railways / NHSRCL project updates |
| India oil & gas E&P and refinery capex announcements (ONGC, HPCL, OALP rounds) | No new OALP round or major refinery capex sanctioned in a rolling 12-month window | Quarterly | PIB / company capex announcements |

All seven candidates are carried unmodified from B09 Section 6; falsifiers and cadence are drafted here for the first time and are UNVERIFIED. Verification and tracker writes happen at Role 5.5 in claude.ai.

### 4c. Fragility read

- **variable_count:** 4 (the Section 2 C1 dominant variables: value-added mix %, GDAL quarterly revenue vs guide, consolidated CFO/PAT and inventory days, GDAL Phase-2 timeline).
- **verifiability_ratio:** 2 of 4 externally observable (consolidated CFO/PAT and inventory days are filed, audited figures once the next AR or results post; the value-added mix % is company-reported only, not an audited segment line, since Goodluck discloses no Ind AS 108 segments; GDAL's quarterly revenue and margin are calculated as consolidated-minus-standalone, a derived figure resting on the company's own consolidated disclosure, not an independently filed subsidiary number, pending the still-missing GDAL rating rationale).
- **single_point_failure:** none — failure requires conjunction. No single variable alone kills the thesis: a soft quarter on GDAL revenue without a margin collapse, or a mix-% plateau without a cash-flow deterioration, would each be a caution flag, not a kill. The combination the model watches most closely is GDAL revenue missing pace AND the order book staying unquantified, which together would move the posture from RESEARCH/WATCH toward PRICED NARRATIVE (TRAP) territory per the CLAUDE.md Transition Decision Matrix.
- **fragility_verdict:** FRAGILE. Two of four dominant variables are company-narrated or derived rather than independently filed, one (GDAL timeline) already carries a confirmed prior slip, and the credibility grade on management's own forward statements is D (1 of 7 tracked promises delivered, 4 missed, B05).

### 4d. Research brief (claude.ai live-web work order)

1. Locate the India Ratings rationale for Goodluck Defence and Aerospace Ltd (IND A+/Stable, Aug-2026) at indiaratings.co.in — the freshness-pair failure named in Section 1. [PENDING LIVE VERIFICATION, named in Chain 1 below]
2. Verify the identity of GDAL's non-promoter minority investor(s) behind the Dec-2023 (Rs 136.5cr at Rs 150/share) and Aug-2026 (Rs 285cr at Rs 375/share) raises — MCA filings, Reg 30 disclosures, or the missing GDAL rating rationale. [PENDING LIVE VERIFICATION, named in Chain 2 below]
3. Verify the BSE Reg 31 shareholding pattern (pledge %, category-wise split) for the quarters the screener aggregator covers, to close the promoter-pledge and FII+DII qualifiers at primary-source tier.
4. Verify the terms, swap ratio and valuation of the proposed Goodluck Green Energy Ltd amalgamation once disclosed (board approved in-principle 11-Jul-2026; terms not yet set per the filing itself).
5. Verify whether a corrected FY25 receivables ageing schedule exists (the FY25 AR as originally filed on BSE), given Note 8's FY26 AR comparative is numerically identical to the current year.
6. Verify GDAL's own statutory auditor identity and any audit-fee/non-audit-fee split, neither found in the extracted AR text.
7. Verify the ownership of Goodluck Astra (the explosives/fuses company named in peer/analyst context but sitting outside the listed group; owners NOT FOUND, per B12b).
8. Verify Balu Forge's FY26 consolidated revenue and any reliable TAM for Precision Pipes & Auto Tubes (both searches returned no usable figure at Stage 9, B09).
9. Verify the India defence-export figure discrepancy (Rs 23,000cr vs Rs 38,000cr cited across Goodluck's own calls) against a primary Ministry of Defence or PIB source.
10. Verify the 155mm-shell share of India's total Army ammunition budget (B09's 30-40% figure is an unsourced analyst assumption, not a filed number) against any available government or industry-association source.
11. Verify whether the Q2 FY27 results (due on or before mid-Nov-2026) show a GDAL quarterly run-rate consistent with, or below, the Rs 75-88cr/quarter pace the FY27 guide needs.

### 4e. Second-order stub (Rule F, Master Prompt v3.7)

Stub carries the first two chains, drafted from corpus, off the two dominant variables the evidence base can carry furthest: GDAL revenue/margin delivery, and consolidated cash conversion under capex.

```
CHAIN 1: Goodluck's FY27 defence guide of Rs 300-350cr requires roughly Rs 75-88cr of GDAL
revenue per quarter; Q1 FY27 delivered about Rs 81.5cr at 36-38% EBITDA margin, calculated as
consolidated-minus-standalone revenue (B05).
Link 1 [DOCUMENTED, B05/B12b]: Management has not quantified the GDAL order book in any of
four analysed calls; the horizon it has claimed for that order book has shifted across calls
(no order book stated / 8 months / 1 year / 2 years), against a single disclosed order of
Rs 307cr (Reg 30 filings; B12b CRITICAL finding).
Link 2 [DOCUMENTED, B02/B03/AR]: What binds — GDAL's own capital commitments are Rs 284.70cr
above the standalone figure, almost entirely forward capex against GDAL's own net assets of
only Rs 183.07cr (AR2026 Note 33 p.220, Note 38 p.221); the parent has since given HDFC Bank a
Rs 275cr corporate guarantee for a GDAL project loan carrying a Debt/EBITDA <=1.50x release
covenant (Reg 30 filing 11-Jul-2026). What was not said: no call has disclosed who the GDAL
order counterparty is beyond "Government of India" in general terms, nor whether the Rs 307cr
disclosed order overlaps with or sits inside the Rs 300-350cr FY27 revenue guide.
Link 3 [INFERENCE]: If the order book were comfortably ahead of the revenue guide, management
would have an incentive to disclose it, since analysts have asked for it in three of four calls
(B05 repeated_evasions); the persistent non-disclosure, alongside a covenant-linked parent
guarantee tied to GDAL's own Debt/EBITDA, suggests the order book may not yet cover the full
FY27 guide, and that the guide currently rests partly on expected future orders rather than a
booked backlog.
Binding constraint: whether GDAL's physical capacity (150,000 shells/year until Phase-2 lands)
and its order pipeline, not government defence-budget size, can deliver Rs 300-350cr in FY27;
B09 finds the underlying market is large (India-centric defence TAM Rs 4,700cr conservative)
but the execution and order-book disclosure are what the model actually watches (Section 2 C2).
Unsaid: the exact counterparty(ies) behind the Rs 307cr disclosed order, and whether GDAL's
pricing per shell (never disclosed at an AR-anchored rate, B04) is fixed or escalation-linked
against the input-cost risk the parent already runs unhedged (Note 31.6, 64.9% of FY26 PBT).
Observation that confirms or breaks this chain, and confirm-by date: Q2 FY27 results (BSE
filing due on or before mid-Nov-2026) showing consolidated-minus-standalone revenue at or above
Rs 75cr for the quarter, AND any Reg 30 filing naming a GDAL order value that, combined with
the Rs 307cr already disclosed, covers the FY27 guide. A print below Rs 75cr, or continued
silence on order-book size through the Q2 FY27 call, breaks the chain (falsification line
matches outputs/final/gate-recommendation.md).
[PENDING LIVE VERIFICATION: the counterparty and value of GDAL's contracted defence order book
beyond the disclosed Rs 307cr order — Claude web should check the India Ratings GDAL rationale
once located (Section 1, item 7 gap) and any Ministry of Defence/PIB procurement disclosure
naming Goodluck Defence and Aerospace as an awardee.]
```

```
CHAIN 2: Consolidated CFO/PAT fell to 0.96x in FY25 and 1.10x in FY26, with cumulative free
cash flow of -Rs 722.41cr against cumulative PAT of +Rs 478.61cr over FY24-FY26, while
borrowings rose from Rs 612cr to Rs 1,119cr (B01, B02, B03).
Link 1 [DOCUMENTED, rating rationales]: India Ratings ties the working-capital stretch
specifically to "delays in dispatches" (14-Jul-2026, p.3) rather than to revenue growth, since
revenue grew only 3.35-4.1% while inventory grew 29.1% in the same year (B02).
Link 2 [DOCUMENTED, AR]: What binds — capital commitments (Rs 363.06cr consolidated vs
Rs 78.36cr standalone, Note 33 p.220) and the multi-year Rs 300-350cr/year capex guide
(CRISIL, 30-Jun-2026) mean the capex half of the cash gap is scheduled to continue regardless
of whether the working-capital half resolves. What was not said: the FY25 comparative
receivables ageing table in Note 8 is numerically identical, bucket for bucket, to the FY26
table (AR2026 Note 8, p.158) — a disclosure-integrity gap that means the true prior-year
ageing, and therefore the true trend in receivables quality (as opposed to inventory), cannot
be independently verified from this AR at all.
Link 3 [INFERENCE]: If the working-capital stretch were purely dispatch-timing (a temporary,
operational cause consistent with the ARTIFACT-OF-CLIMB reading in Section 2 B5), inventory
days should mean-revert toward the FY24-FY25 range of 63-69 days once the GDAL ramp and any
logistics bottleneck normalise; if instead it reflects slowing realisation from a growing base
of government and defence customers (a structural change in the customer mix, consistent with
the STRUCTURAL-FEATURE reading), inventory days would plateau at or above the FY26 level of 84
even as the mix shift continues, because government-linked receivables and dispatch cycles run
structurally slower than the CR-coil base's cycle.
Binding constraint: whether operating cash flow converts from the capex-heavy phase before
leverage (2.69x Net Debt/EBITDA, 3.32x Interest Coverage at FY26, both within 0.3-0.4x of the
Gate 0 AVOID trigger, B01) crosses that trigger; this is a self-funding question, not a market-
size question.
Unsaid: CRISIL names "increased offtake from the defense segment, primarily by government
entities resulting in further stretch in realization from customers" as an explicit forward
monitorable (30-Jun-2026, p.2) — a direct link between the very mix-shift the thesis wants
(more defence and value-added revenue) and the very cash-conversion problem the thesis needs
to resolve. No call has addressed this tension directly.
Observation that confirms or breaks this chain, and confirm-by date: the H1 FY27 (30-Sep-2026)
standalone and consolidated balance sheet, expected in Q2 FY27 results (BSE, due on or before
mid-Nov-2026). Inventory days back in the 63-69 day range, with the net working-capital cycle
below the FY26 111 days (India Ratings basis), confirms the ARTIFACT reading; inventory at or
above 84 days, with the cycle at or above 111 days, confirms the STRUCTURAL reading (matches
outputs/final/gate-recommendation.md falsification line).
[PENDING LIVE VERIFICATION: the GDAL rating rationale (once located) may carry the subsidiary's
own working-capital-days disclosure, which no held document in this corpus provides separately
from the consolidated figure. Claude web should check indiaratings.co.in for this document
specifically, since it is also the Section 1 freshness-pair gap.]
```

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in claude.ai with live web, before Role 2.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. Goodluck India buys steel and makes five families of product: cold-rolled coils and pipes, precision tubes for cars, forged parts, fabricated steel structures, and, since October 2025, artillery shell bodies through a subsidiary.
2. The company runs seven plants in Uttar Pradesh and Gujarat with 500,000 tonnes of capacity, and has manufactured steel products for almost four decades.
3. FY26 revenue was Rs 4,100 crore, up 4% on the year before; the shell subsidiary made up about 1% of that on a partial year, and about 6% of the most recent quarter.
4. Global carmakers such as Volkswagen, BMW, Toyota and Tata Motors buy the precision tubes; Indian Railways, L&T and NTPC buy the structures; the Government of India buys the shells.
5. The company says it serves over 600 customers in more than 100 countries, with no single customer or country standing out as a concentration risk.
6. Demand for the core business tracks India's infrastructure spending, solar capacity additions, car production volumes, railway projects, and oil and gas capex; demand for the shell business tracks the government's defence budget.
7. India has said it will reserve a share of next year's defence budget for domestic suppliers, and India passed 500 gigawatts of renewable power capacity in the past year; both support the growth case.
8. Only the shell business has a clearly documented advantage: a government licence and a quality certificate that very few Indian private companies hold.
9. The tube and forging businesses have a moderate advantage, because carmakers must re-test a part before switching supplier; the plain steel-coil business has no advantage and earns a thin, formula-driven margin.
10. The mental model is a mix shift: the company is moving away from thin-margin steel and toward higher-margin tubes, forgings and shells, but the shift shows up in profit more than it shows up yet in cash.
11. The evidence base is fragile: of the four things this model watches most closely, two are numbers the company reports itself rather than numbers an outside filing confirms, and the shell-plant expansion has already slipped once on its own timeline.
12. The corpus could not establish who owns the minority stake in the shell subsidiary, despite two separate share sales; it also could not establish a reliable market size for the car-tube business.
13. The corpus could not establish the exact reason for a promoter-family share sale in June 2026, since Indian disclosure rules do not require a stated reason or price for that kind of sale.
14. The biggest open question is whether the company can turn its rising profit into cash, since free cash flow has been negative for three straight years while borrowings have nearly doubled.
15. The second open question is whether the shell business can prove its margin and its order book are real and lasting, since management has not stated a firm order-book number in any of the last four earnings calls.

---

## SECTION 6: STANDING EXTRACTION ANNEX

*Annex exception applies: the ten questions below are answered from the corpus, opening source PDFs directly where a stage report did not already carry the anchored quote.*

**1. UNITS.** No per-unit rupee figure (Rs/tonne, Rs/shell) is printed anywhere in the extracted AR text. Quote: "Total sales volume for the year reached 4,68,161 MT, registering growth of 5.8% over the previous year" (AR2026 p.39). This is a basket figure across all non-defence product lines, not a single-product per-unit price. Comment: B04 derived an implied blended figure from this volume against the FY26 revenue line — approximately Rs 87,010/tonne revenue and Rs 8,937/tonne EBITDA, ex-defence (B04 unit_economics block; FY26 ex-defence revenue Rs 4,074.52cr / 4,68,161 MT). This is a derived cross-check, not a printed company figure. Per-shell defence pricing is NOT FOUND at an AR-anchored rate anywhere in the corpus (B04, B09); GDAL's blended shell realisation of ~Rs 24,000/shell used in B09's management-claim test is itself back-calculated from disclosed order value and volume, not a printed per-shell price.

**2. SEGMENT CAPITAL AND DEBT.** NOT DISCLOSED at a segment level, standalone or consolidated. Quote: "The Company has monthly review and forecasting procedure in place and CODM reviews the operations of the Company as a whole, hence there are no reportable segments as per Ind AS 108 'Operating Segments'" (AR2026 standalone Note 35, p.179). The identical language appears at the consolidated level: "CODM reviews the operations of the Group as a whole, hence there are no reportable segments as per Ind AS 108" (AR2026 consolidated Note 35, p.221). Comment: Goodluck reports one segment company-wide; no segment assets, liabilities, capital employed, or borrowings split exists in either AR. Total consolidated borrowings are Rs 1,119.46cr at FY26 close (B00 LBF3, cross-checked B03), unallocated by line or by GDAL vs core.

**3. GUIDANCE VERSUS ASPIRATION.** From B03 (AR-sourced) and B05 (concall-sourced), classified:
   - (a) Guidance with a period: "Defence FY27 revenue guidance... Rs250-300cr at 75-80% utilisation of the 150,000-shell base" (AR2026 MD&A, per B03 guidance_table), later restated on calls as Rs 300-350cr (Q1 FY27 call, per B05). "FY27 revenue growth... 15-20%" (Q4 FY26 and Q1 FY27 calls, per B05, after an interim cut to 14-15% with no bridge given). "Standalone FY27 capex... Rs 100-150 Cr" (Q1 FY27 call, per B05).
   - (b) Aspiration without a firm period: "GDAL Phase-2 capex... ~Rs500cr, timing to be finalised" (Chairman's letter p.16 and MD&A p.35/74-75, per B03); "GDAL IPO... '18 months from today'" (Q1 FY27 call, per B05) — a first firm figure but self-described as informal.
   - (c) Capacity or capability only: "Hydraulic tubes utilisation ramp... ~50% FY26 to 65-70% FY27" (per B03) is a capability target tied to existing installed capacity, not a new-order guide; it has missed every quarter it was restated (40-45% Q3 FY26, ~50% FY26 close, 60% Q1 FY27, per B05).
   Comment: The FY26 total-company revenue growth guidance the company memory cites (20% guided, cut to 12% in Sep-2025) is NOT FOUND in either AR or in any held transcript; the earliest held transcript (Q2 FY26, 10-Nov-2025) instead reaffirms 15-20% (B03, B05). This is a genuine gap between pre-corpus company memory and the primary record.

**4. CONCENTRATION.** Quote: "The Company serves a base of over 600 customers across more than 100 countries" (AR2026 p.38). Quote: "Trade receivables consist of a large number of customers spread across diverse industries and geographical areas with no significant concentration of credit risk" (AR2026 standalone Note 31.8/risk section, p.152; identical language repeated in the consolidated notes, p.??? per B02/B03 cross-reference to AR text). Top product share: NOT DISCLOSED (Goodluck discloses percentage-of-revenue by product family on a narrative chart — CR 34%, PPAT 27%, ESF 24%, Forging 15%, Defence ~6% — but not a "top product" concentration metric in the concentration-risk sense; AR2026 p.12-13, per B04). Top customer share: NOT DISCLOSED, consistent with the "no significant concentration" language above and with 600+ named customers.

**5. PROMISE LEDGER.** From B05 promise_delivery (concall-sourced, cross-checked B12b):

| Promised in | Promise | Outcome | Evidence anchor |
|---|---|---|---|
| Q2 FY26 call, reaffirmed Q3 FY26 | FY26 revenue growth 15-20% | MISSED — delivered +4.2% consolidated | Concall_Nov_2025/Concall_Feb_2026/Concall_Jun_2026 transcripts |
| Q2 FY26 call, revised Q3 FY26 | Defence FY26 revenue Rs 100cr, revised to Rs 60cr | MISSED — delivered Rs 46cr revenue / Rs 29cr EBITDA | Concall_Nov_2025/Concall_Feb_2026 transcripts |
| Q2 FY26 call | Defence EBITDA margin 30-35% | Reported DELIVERED (38-70% actuals); B12b reclassifies as premature — FY26 Rs46/29cr figure is unreconciled to the consol-minus-standalone ~Rs33/23cr calc, only Q1 FY27 (38%) is clean | Concall_Nov_2025 transcript; B12b finding |
| Reg 30 filing Oct-2025 / Q2 FY26 call | 400,000-shell capacity online within one year | MISSED — now targeting Sept-2027 construction, Q4 FY28 commercial | 20251001 Reg 30 filing; Concall_Aug_2026 transcript; 20260806 Reg 30 filing |
| Q2 FY26 call, restated each quarter | Hydraulic tube utilisation 70% by Mar-2026 | MISSED — ~50% at FY26 close, 60% Q1 FY27 | Concall_Nov_2025/Feb_2026/Jun_2026/Aug_2026 transcripts |
| Q4 FY26 call | FY27 growth guidance cut to 14-15% | PARTIAL — reinstated to 15-20% one quarter later, no bridge given | Concall_Jun_2026/Aug_2026 transcripts |
| Q4 FY26 call (implicit) | Standalone FY26 capex Rs 250cr | PARTIAL — analyst calculates Rs 340cr; management counters with an unreconciled Rs 232cr figure | Concall_Jun_2026 transcript |

Credibility grade: D (1 delivered as originally scored, 2 partial, 4 missed of 7 tracked; B12b's review would place the true count lower still, since it disputes the one "delivered" row).

**6. RESTATED BASES.** Quote: "previous year figures have been regrouped/reclassified/rearranged wherever necessary to confirm to the current year" (AR2026 standalone Note 40, p.180; consolidated Note 44, p.224) — generic, unquantified boilerplate naming no specific line item (B02). Separately, a substantive restatement-adjacent finding: the GDAL non-controlling-interest equity event for FY25 is described as "Acquisition (sale) of Non Controlling Interest" in the FY25 AR's Statement of Changes in Equity (p.204) and relabelled "Investment by NCI" for the identical entry and identical rupee figure (Rs 3.46cr) in the FY26 AR's comparative column (p.192), with no explanatory note in either AR (B02). Comment: this is not a disclosed restatement under Note 40/44; it is an unexplained description change the verifier process did not overturn (B12a: figure itself confirmed accurate against the source, "GDAL NCI equity, Rs346.43 lakh, Consolidated SOCE exact match").

**7. CORPORATE-ACTION CLAUSES.** Three corporate actions are in the corpus:
   - **Bonus issue.** Ratio: "2 (two) Bonus Equity Share... of Rs.2/- each for every 1 (one) existing Equity Shares of Rs.2/- each" (Reg 30 filing 24-Aug-2026, allotment outcome). Record date: 21-Aug-2026. Deemed allotment date: 24-Aug-2026 (T+1). Trading-available date: 25-Aug-2026 (T+2). Capitalisation source: "Rs.13,29,54,036/- from the balance... in the Securities Premium Account... as per the audited financial statements... for the financial year ended March 31, 2026." Pre-issue capital: Rs 6,64,77,018 (3,32,38,509 shares); post-issue: Rs 19,94,31,054 (9,97,15,527 shares). Rights: bonus shares "rank pari-passu with the existing equity shares... in all respects" (Reg 30 filings 07-Jul-2026 and 24-Aug-2026).
   - **GDAL preferential issue.** "further issue of equity shares to persons belonging to Non-Promoter category through preferential and private placement to raise fund up to a sum of Rs.285 crores... at a rate of Rs.375 per share (including a premium of Rs.365 per share) subject to the approval of the shareholders of the subsidiary company" (Reg 30 filing 06-Aug-2026). No appointed/effective date, no allottee identity, and no final share count is disclosed in this filing; these remain open per Section 4d item 2.
   - **Goodluck Green Energy Ltd amalgamation.** "the Board of Directors has, in principle, approved the proposal for undertaking a corporate restructuring... the amalgamation of Goodluck Green Energy Limited with and into the Company... The detailed terms, structure and financial implications of the proposed restructuring shall be evaluated and, upon approval by the Board of Directors, shall be disclosed to the Stock Exchanges" (Reg 30 filing 11-Jul-2026). Liability allocation, swap ratio and effective date: NOT YET DISCLOSED as of the filing itself; this is the single highest-priority live monitorable named in B08.
   - **Related corporate guarantee (GDAL project loan).** "Corporate Guarantee in favour of HDFC Bank Limited... to secure Rupee Term loan of ₹275,00,00,000... for the period till achievement of Debt/EBITDA<=1.50x and last 3 years>=1.50x at standalone borrower Financials from testing date" (Reg 30 filing 11-Jul-2026, Annexure B). "Goodluck India Limited is contingent liable to pay the debt in case of default by borrower." This is the release covenant referenced in Section 2 C3.

**8. RELATED-PARTY PERIMETER.** From AR2026 consolidated Note 32 (p.219), FY26 (`in lakhs unless stated):
   - Key Management Personnel: Shri M.C. Garg (Chairman), Shri R.C. Garg (Director), Shri Nitin Garg (Director). Remuneration paid FY26: Rs 466.50 lakh (down from Rs 752.40 lakh FY25).
   - Relatives of KMP: Shri Manish Garg, Shri Umesh Garg, Shri Harsh Garg, Smt. Savitri Devi, Smt. Kanak Lata. Remuneration paid FY26: Rs 338.50 lakh (down from Rs 435.50 lakh FY25).
   - Persons belonging to Promoter Group: Sh. Rajeev Garg, Sh. Shyam Aggarwal, Sh. Ashish Garg, Sh. Saras Garg, Sh. Tushar Garg, Sh. Parv Aggarwal, Sh. Ram Aggarwal, Sh. Dhruv Aggarwal. Remuneration paid FY26: Rs 871.10 lakh (down from Rs 1,517.84 lakh FY25). Advance given FY26: Rs 1,117.27 lakh (this is the "Persons belong to Promoter Group" column, distinct from "Others").
   - "Others" (Excellent Fincap Pvt Ltd, enterprise over which KMP exercise significant influence): Advance given FY26 Rs 1,117.27 lakh combined with Promoter Group in the total column per the note's own layout (B02 cites Rs 11.17-33.05cr/year range across years); Outstanding Receivable FY26 Rs 1,239.62 lakh, up from Rs 94.56 lakh FY25 (+1,211% YoY, matching B02's finding).
   Comment: this consolidated table is where the Excellent Fincap flows appear; the standalone parent-only Note 32 shows zero in the equivalent "Others" columns both years, meaning the flows run through GDAL, not the parent directly (B03 triple-pass finding).

**9. PLEDGE AND SHAREHOLDING.** From the screener aggregator CSV (screener-shareholding-quarterly-GOODLUCK-2026-09-19.csv), the only shareholding source in this corpus (not the BSE Reg 31 filing): Promoter holding across the twelve quarters held (Dec-2023 to Aug-2026): 56.45%, 54.44%, 55.78%, 55.78%, 55.78%, 55.78%, 56.44%, 56.44%, 56.44%, 56.44%, 54.00%, 54.00%. FII: 1.24% to 1.92% (Aug-2026), ranging 1.20-5.20% across the window. DII: 1.18% (Dec-2023) rising to 6.14% (Aug-2026). No pledge column exists in this source. Pledge is evidenced only at B08's web-search tier: "0% pledge, no encumbrance confirmed for FY26" (B08, MEDIA REPORTED, not a primary filing in this corpus). Institutional holding latest (Aug-2026): FII 1.92%, DII 6.14% (screener CSV).

**10. VERIFICATION.** Documents quoted in this annex: Annual_Report_2026.pdf (Goodluck India Ltd, filed 08-Sep-2026, pp.38-39, 152, 158, 179-180, 192, 219-224); Annual_Report_2025.pdf (Goodluck India Ltd, filed 02-Sep-2025, p.204, cited via B02); Reg 30 filings 20251001, 20260707, 20260711, 20260806 (two separate filings on this date), 20260824 (Goodluck India Ltd); screener-shareholding-quarterly-GOODLUCK-2026-09-19.csv (aggregator, scraped 2026-09-19); Concall_Nov_2025_Transcript.pdf, Concall_Feb_2026_Transcript.pdf, Concall_Jun_2026_Transcript.pdf, Concall_Aug_2026_Transcript.pdf (Goodluck India Ltd, Q2 FY26 through Q1 FY27); CRISIL_Rationale_Goodluck_2026-06-30.pdf and IndRa_Rationale_Goodluck_2026-07-14.pdf (parent rationales, cross-cited via gate-recommendation.md).

CORPUS COMMIT HASH: 193042e26042c1f28a96e3ece51f392deea6f58d
