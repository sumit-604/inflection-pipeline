# Stage 7 — Emerging Moat Scan: Yash Highvoltage Ltd (YASHHV)
Run date: 2026-09-26 | Model: Sonnet 5 | CORRECTION RUN (run 2)
Taxonomy note: this is the 22-category Emerging Competitive Advantages scan. It is NOT FTTCP. FTTCP runs separately inside Stage 11.

Evidence taxonomy used throughout: [DOC] = documented (capex committed, contract signed, approval filed/granted, product launched), [MGMT] = management claim (concall/presentation, not yet backed by committed capital or signed contract), [INF] = analyst inference.

## CORRECTION LOG (run 2, against 12c-verifier-framework-run1.md findings)

| Finding | Severity | Disposition | What changed |
|---|---|---|---|
| CR-1: Ensales/Weidmann/Electrolink credited in both E2 and H2 (Rule 15, one-evidence-one-credit) | CRITICAL | CORRECTED | The three agreements now score only under E2 (China+1/geography is their natural home). H2 rescored on its unique evidence only: the Sukrut Electric JV (Rs5.24cr). H2 raw HH=4 to HL=2; adjusted 4.0 to 2.0. |
| MJ-1: A1 and B2 rest on the same 2016-2018 approval evidence; existing-vs-emerging test applied to E1/H1 but not A1/B2 | MAJOR | CORRECTED | Applying the identical test used to zero E1 ("60+ countries... existing-moat facts already captured in B01, not emerging") and H1: the 2016-2018 PGCIL/NTPC/NPCIL/DRDO approvals are existing-moat facts, already the mechanism B07 used to CONFIRM B01's M10. They are not re-credited as emerging. A1's only remaining unique content — the "12-13 global bushing makers" count — is [MGMT], unverified, and insufficient alone (the same bar this scan applies to I1's leg (a) test). A1 rescored to NO EVIDENCE FOUND (unique), 4.0 to 0.0. B2 rescoped to credit only the genuinely new, 2026-vintage qualification pipeline still in progress (IEEE US seismic validation, CENELEC Europe compliance, 550kV Vadodara test infrastructure) — this is the actual emerging content distinct from the historic approvals. B2 raw HH=4 to MM=2; adjusted 4.0 to 2.0. |
| MJ-4: Section 2C prescribed formula (capex x historical FAT) not run though B01 carries FAT 4.54x; 9,000-unit proxy base conflicts with the 10,000 units/yr OIP figure in 2A | MAJOR | CORRECTED | Ran the prescribed arithmetic: Rs153cr x 4.54x = Rs694.6cr = 295% of FY26 revenue (Rs235.16cr), shown with the mandatory caveat that historical FAT on a mature, depreciated asset base overstates a new greenfield plant's turnover and should be read as a mechanical ceiling, not an expectation. The unit-capacity proxy (9,000 to 15,000 units/yr, +67%) is dropped: its base cannot be reconciled against 2A's own OIP-alone figure of 10,000 units/yr from the corpus available to this stage. Carried as NOT FOUND rather than restated. capex_embedded_growth_pct now carries the mechanical FAT-based figure (295), caveated. |
| MN-3: 6C carries B01's stale moat count (5/60=21) after B07's own M11 override | MINOR | CORRECTED | 6C now shows 4 moats confirmed, 16/60, still STRONG band (4-5), consistent with B07's own override of M11. |
| MN-4: "Strong x4" text vs table showing Strong x5; recount of 13 inflated by double counts (~9 unique) | MINOR | CORRECTED | Rebuilt from the corrected scorecard. Strong x2 (B1, E2), Moderate x4 (A3, B2, F2, H2). Completionist recount rebuilt to 14 unique documented items across 6 categories, no item counted in two categories. |
| MN-5: evidence_mix claim/inference counts (8, 2) not enumerated in the report | MINOR | CORRECTED | Claim (MGMT) and inference items are now individually listed below (4 claim items, 2 inference items), matching the YAML evidence_mix field. |
| MJ-2 (B01 ROCE formula substitution) and MJ-3 (B01 E2 dilution note) | MAJOR | OUT OF SCOPE for this stage | These are Gate 0 (B01) findings. Per the task brief, stage 1 is being corrected in parallel; this stage uses B01 run-1 values (core 70, classification GOOD, moat count as stated in B01) as injected input and flags that a parallel B01 correction is in flight. No B07 action follows from these two findings. |

Net effect on this stage's own arithmetic: em_score falls from 25.7 to **17.7**. Classification moves from STRENGTHENING (25-39) to **MODEST MOAT DEVELOPMENT (12-24)**. The 25-point band edge carried no weight in either direction; the corrected score reflects only the fixes above, run through the same likelihood x impact x evidence-tier mechanics as run 1.

## GATE 0 / B01 M10-M11 CONFIRM-OR-OVERRIDE (unchanged from run 1)
B01 flagged that M10 (switching costs) and M11 (network effects) passed the mechanical numeric test with no disclosed mechanism for this build-to-spec archetype. This scan's finding stands unchanged by the correction:

- **M10 switching costs: CONFIRM.** A real mechanism exists and is disclosed: multi-year utility/OEM qualification cycles (PGCIL, NTPC, NPCIL, DRDO named approvals, AR p.17 "Awards & Certifications" timeline) and the company's own MD&A risk section states explicitly that new entrants need "specialised design expertise, advanced manufacturing infrastructure, extensive testing capabilities, stringent quality systems and approvals... it can take several years for a new entrant to develop the required capabilities" (AR p.47, Demand & Competition risk, [DOC]). Note: this is the same historic-approval mechanism now treated as an EXISTING fact in the correction above (see MJ-1 disposition) — confirming a Gate 0 mechanical pass is a different task from crediting it a second time as an emerging moat.
- **M11 network effects: OVERRIDE to 0/no evidence.** Nothing in the AR, concalls, RHP or presentations describes a platform connecting suppliers and buyers, a hub-and-spoke aggregation model, or any multi-sided-market dynamic. Yash is a build-to-order component maker selling point-to-point to OEMs and utilities. The mechanical pass in B01 is not supported by a disclosed mechanism; override to NO EVIDENCE FOUND (scored 0 in Section 5, Category D2/B3 area — no network-effect category applies here).

## SECTION 1: FUTURE PRODUCT & REVENUE STREAM ANALYSIS

### 1A. New products/services in pipeline
| Product | Status | Evidence | Expected launch | Revenue potential | vs current portfolio |
|---|---|---|---|---|---|
| 72.5-245 kV RIP bushings | UNDER DEVELOPMENT | [DOC] type testing planned FY27, initial commercialisation India-focused (Board's Report, AR p.63-64) | FY27 (type test) | Not quantified | Extends RIP class within India |
| RIP up to 420 kV | UNDER DEVELOPMENT | [DOC] "market readiness expected from next year" (Board's Report) | FY27-28 | Not quantified | New EHV-class product |
| 138 kV / 230 kV OIP for US (IEEE high-seismic) | IN TRIALS / REGULATORY PENDING | [DOC] under validation against IEEE seismic standards, "expected to be ready by September 2026" (Board's Report) | Sep-2026 | Not quantified | New geography-specific spec |
| 245 kV short-tail (CENELEC) bushings, Europe | UNDER DEVELOPMENT | [DOC] "under development for compact transformer applications in Europe" (Board's Report); front matter names CENELEC-compliant 72.5-170 kV range already announced (AR p.5) | Not dated | Not quantified | Region-specific compact form factor |
| RIP/RIS up to 550 kV (Vadodara plant) | ANNOUNCED / UNDER CONSTRUCTION | [DOC] Rs153cr capex, testing infra to 550 kV (Board's Report, concall May-2026 line 602); [DOC] Ensales Reg 30 filing names "RIP/RIS Condenser Bushings up to 230 kV (available from 2027 onwards)" as a contracted product line | Trial Oct-2026, commercial H2FY27 | 6,000 units/yr capacity add | New voltage ceiling (245kV to 550kV), new manufacturing process (dry-type resin vs oil) |
| In-house RIP/RIS core manufacture (backward integration) | UNDER DEVELOPMENT | [MGMT] Swiss technology-transfer contract "already got over," knowledge "successfully transferred," trial production to validate ongoing (concall May-2026, lines 510-537) | Trial with new plant | Import substitution, margin driver from FY28 (guided, already pushed once) | Currently 95% imported input, moving in-house |

### 1B. Diversification direction
- **Product**: voltage-class extension (245kV to 550kV via Vadodara), technology diversification (OIP to RIP/RIS dry-type). [DOC]
- **Geographic**: USA (Yash HV USA Inc., wholly owned, incorporated Texas 21-Apr-2025, [DOC] AR p.68-69; Ensales representation agreement, 19 US states, effective 11-Sep-2026, 36 months, [DOC] Reg 30 filing), Europe/UK/Ireland (Weidmann agency, Electrolink partnership, [DOC] AR front matter p.5), North Africa (Weidmann, [DOC]).
- **Vertical integration**: RIP/RIS core backward integration via Vadodara, ending 95% import dependence. [DOC]
- **Inorganic/vertical breadth**: 50% JV in Sukrut Electric with Quality Power Electrical Equipments Ltd, Rs5.24cr consideration ([DOC] AR Board's Report, Note 36), broadening into the wider transformer-component ecosystem beyond bushings.

### 1C. Revenue mix shift table
| Stream | Current % (FY26, per B04) | Expected in 3 years | Margin direction | Profitability impact |
|---|---|---|---|---|
| RIP/RIS condenser bushings | 83% | Higher (backward-integrated core, higher-kV mix) | Up, contingent on core localisation succeeding (guided, not yet delivered) | Largest lever; also largest execution risk (Vadodara) |
| OIP condenser bushings | 10% | Stable to modestly lower share as RIP grows | Stable | Base-load, already near-full utilisation |
| High-current bushings | 4% | Modest growth (data-centre demand named, AR p.69) | Improving (unit realisation ~Rs5-7.5 lakh, AR p.68, [DOC]) | Small base |
| Wall-through/oil-to-oil/other | 3% | Stable | Stable | Niche |
| Retrofit / after-sales | 6.8% | Growing (16.0cr FY26, +60% YoY, [DOC]) | High-margin per company statement | Structurally attractive but small |
| Export (cross-cutting, not a separate line above) | ~7.3% of revenue (Rs17.2cr/Rs235.2cr) | Targeted 20%+ in 2-3 years [MGMT] | Improving via price realisation | Optionality, not yet delivered |
| Sukrut JV contribution (consolidated) | ~Rs25-26cr (JV level, FY26) | Rs150-160cr in 4-5 years [MGMT, no EBITDA guide given] | Unknown | Large stated target, zero disclosure depth |

## SECTION 2: CAPACITY & CAPEX PIPELINE

### 2A. Capex programme table
| Project | Rs Cr | Funding | Status | Expected commissioning | Capacity addition | % over current |
|---|---|---|---|---|---|---|
| Vadodara (Jarod) RIP/RIS Greenfield | 153 (escalated from an original ~90, [DOC] Board's Report, B05 cross-check) | IPO proceeds + up to Rs151cr preferential issue (12,62,131 shares + 8,32,177 warrants @ Rs721, approved 22-Jun-2026) [DOC] | Under construction; office building complete, machinery installation ongoing, vastu pujan 25-May-2026 [DOC] | Trial Oct-2026, commercial H2FY27 [MGMT, re-guided from original Mar-2026 target] | +6,000 RIP/RIS units/yr (Investor Presentation FY26, [DOC]) | See 2C below — the "combined to 15,000 units/yr" base cannot be reconciled against this table's own OIP figure and is not restated as a % here |
| OIP brownfield expansion (existing site) | Not separately quantified; already delivered in FY26 | Internal accruals | Completed within FY26 [DOC] | Delivered FY26 | 6,000 to 10,000 units/yr (+67%) [DOC, Board's Report] | +67% (already realised) |
| Brownfield OIP expansion (further, funded from preferential issue) | Part of the Rs151cr preferential-issue use-of-proceeds | Preferential issue | Announced, not yet executed [DOC, Board's Report proceeds statement] | Not dated | Not quantified | NOT FOUND |

### 2B. Utilisation trajectory
"The Company's manufacturing capacity for FY 2026-27 was fully booked even before the start of the financial year" (Board's Report, [DOC]) — existing (OIP + current RIP) lines running at or near full utilisation. Vadodara plant utilisation trajectory: NOT FOUND (pre-commercial, no ramp data exists yet).

### 2C. Growth embedded in capex (corrected — prescribed formula now run, per MJ-4)
The prompt's standard formula is: total capex under execution x historical fixed-asset turnover = implied incremental revenue, as % of current revenue.

- Total capex under execution: Rs153cr (Vadodara, [DOC]).
- Historical fixed-asset turnover: 4.54x (B01 M3, FY26 revenue 235.16 / net fixed assets 51.80, 01-gate0.md, [DOC], carried from this run's Gate 0 block — this stage did not independently re-derive it, it is an injected figure).
- Arithmetic: 153 x 4.54 = **Rs694.6cr implied incremental revenue = 295% of FY26 revenue (Rs235.16cr)**.
- **Mandatory caveat**: this is a mechanical output of the prescribed formula, not a forecast. Historical FAT is computed on a mature, substantially depreciated existing asset base; applying it to a brand-new greenfield plant systematically overstates the turnover a new, undepreciated asset base will actually achieve in its early years. Read 295% as a formula-driven ceiling, not an expectation. capex_embedded_growth_pct carries this figure (295) with this caveat attached in the block's input_gaps/analyst_note.
- The run-1 unit-capacity proxy (9,000 to 15,000 units/yr, +67%) is **dropped**, per the verifier's MJ-4 finding: this stage's own 2A table states OIP alone reached 10,000 units/yr after the FY26 brownfield expansion, which already exceeds the "9,000 pre-Vadodara combined" base backed out from the Investor Presentation's 15,000-unit figure. The two bases cannot both be correct without a scope qualifier (e.g., the 15,000 figure covering a narrower product line than "all bushings") that is not stated anywhere in the corpus read at this stage. Rather than restate an unreconciled number, this component of the proxy is carried as NOT FOUND.

### 2D. New geography or market entries
USA (Yash HV USA Inc. + Ensales 19-state representation agreement, [DOC]), UK/Ireland (Electrolink, [DOC]), Europe/North Africa (Weidmann, [DOC]) — all FY26-vintage, all documented signed agreements.

## SECTION 3: THE 22-CATEGORY SCAN

### FAMILY A — PRODUCT & TECHNOLOGY
**A1 — Rare manufacturing capability: NO EVIDENCE FOUND (corrected from Strong, per MJ-1).**
Run 1 credited this category on the company's MD&A entry-barrier language and the historic PGCIL (2016), NTPC (2018), NPCIL (2016), DRDO/RDSO (2016, 2017) approvals (AR p.47, p.16-17). Those are the identical facts B07 uses immediately above to CONFIRM B01's M10, and they are the same evidence B2 below draws on. Applying the same "existing-moat fact already captured, not emerging" test this scan applies to E1 (60+ countries) and H1 (sole-manufacturer framing), the 2016-2018 approval history is existing, not emerging, and is not credited twice. A1's only remaining unique content is the management claim of "12-13 independent bushing makers globally against 250+ transformer OEMs" (B05, [MGMT], PENDING peer-concall verification) — a single unverified claim, insufficient alone to score a category, on the same evidentiary bar this scan applies to I1's leg (a) test (a bare claim, unconfirmed, scores 0). Scored 0.

**A2 — Patent and IP pipeline: NO EVIDENCE FOUND.**
Full-text search of the AR (FY25 and FY26) and RHP surfaces zero mentions of "patent" beyond this scan's own search term. No filing trend, no licensing revenue, no lab-partnership disclosure.

**A3 — Process innovation: MODERATE, [DOC]**
Board's Report states 35% production-efficiency improvement H1 to H2 FY26 (measured in bushings produced), labour productivity +28%, On-Time Delivery 62% to 80% (AR p.62, [DOC]). New high-speed wide-band winding machine (OIP cores to 245kV) and SCADA-controlled autoclave ovens added during FY26 (AR p.11, [DOC]). This is real, quantified, and documented — but it is a single-year efficiency jump, not yet a multi-year cost-curve trend. Time to materialise: already active, durability unproven beyond one year.

**A4 — Product platform / modular architecture: WEAK, [DOC]**
5% of FY26 revenue came from newly developed products (AR p.63, [DOC]). Several new SKUs launched off shared RIP/OIP architecture (245kV OIP for Americas, CENELEC 72.5-170kV for Europe, first in-house type-tested 245kV oil-to-oil bushing, AR p.5, [DOC]). Launch frequency is real but revenue contribution is still small.

### FAMILY B — SUPPLY CHAIN
**B1 — Backward integration and RM security: STRONG, [DOC]**
Rs153cr committed capex to localise RIP/RIS cores, currently 95% import-dependent (AR p.5, Chairman's letter and Board's Report, [DOC]); site progress independently confirmed via Reg 30 filing (vastu pujan 25-May-2026, office building complete, machinery installation ongoing, [DOC]). The Swiss technology-transfer arrangement that underpins the core-manufacturing know-how ("already got over," knowledge "successfully transferred," concall May-2026, [MGMT], no royalty disclosed) is scored here only — it is the input to this category's mechanism and is not separately re-credited under H2 (see H2 correction below). Time to materialise: 12-24 months (trial Oct-2026, commercial H2FY27).

**B2 — Qualification lock-in: MODERATE (corrected from Strong, per MJ-1)**
Run 1 credited this category on the same 2016-2018 named approved-vendor status (PGCIL, NTPC, NPCIL, DRDO, AR SWOT p.49) and existing ISO 9001:2015/NABL certification already scored as the confirming mechanism for B01's M10 immediately above and (in run 1) double-counted under A1. That historic base is existing, not emerging, and is credited once, at Gate 0 level, not here. What genuinely IS emerging — new qualification barriers currently being cleared for markets Yash has not yet penetrated — is credited instead: IEEE high-seismic validation for the 138kV/230kV OIP US product (targeted ready Sep-2026, [DOC] Board's Report, still in trials, not yet passed); CENELEC compliance for the 245kV short-tail Europe product (under development, [DOC] Board's Report, no completion date); and the 550kV test infrastructure being built at Vadodara ([DOC], under construction). Each is a qualification hurdle in progress, not yet cleared, that would lock in new geography/voltage-class access if it lands — genuinely forming, matching the category's forward-looking intent. Likelihood Medium (in progress, unresolved) x Impact Medium (opens EHV/US/Europe segments, not yet quantified) = MM. Time to materialise: 6-18 months across the three items (nearest: Sep-2026 IEEE).

**B3 — Supply chain network effect: NO EVIDENCE FOUND.**
No platform, hub-and-spoke, or fragmented-supply-aggregation model disclosed anywhere.

### FAMILY C — CUSTOMER
**C1 — Customer ecosystem / embedded relationships: WEAK, [DOC]**
Retrofit and after-sales revenue Rs16.0cr FY26, +60% YoY (AR p.69, [DOC]) — genuine installed-base monetisation, but no disclosed cross-sell count, ERP/workflow integration, or co-development language beyond generic "trusted partner" framing. Over 150 transformer-OEM/utility customers globally (AR p.28, [DOC]) but no wallet-share metric.

**C2 — Customer concentration improving: NO EVIDENCE FOUND.**
The opposite signal is present: B03 flags a single customer at 18.8% of FY26 revenue (Rs44.17cr of Rs235.16cr, Note 50), not named in the MD&A risk section. No trend data shows this declining. Scored 0, not credited as a moat.

### FAMILY D — DATA & DIGITAL
**D1 — Proprietary data asset: NO EVIDENCE FOUND.**
**D2 — Digital platform: NO EVIDENCE FOUND.**
SAP ERP is an internal operating system (AR p.51, [DOC]), not a customer- or supplier-facing platform with network dynamics.

### FAMILY E — GEOGRAPHIC & ACCESS
**E1 — Geographic first-mover: NO EVIDENCE FOUND (as a forward-emerging category).**
Yash's "60+ countries" presence and 45,000+ bushings supplied (AR p.43, [DOC]) are existing-moat facts already captured in B01, not emerging. No first-license or land-bank claim specific to a new geography was found.

**E2 — China+1 beneficiary: STRONG, [DOC]/[MGMT] blend (unchanged; sole home of the three agreements per CR-1 correction)**
Signed, dated agreements: Ensales (US, 19 states, effective 11-Sep-2026, 36 months, [DOC] Reg 30 filing); Weidmann (Europe/North Africa, [DOC]); Electrolink (UK/Ireland, [DOC]). These three agreements are credited here only — not also under H2 (see H2 correction). Export revenue +123.4% to Rs17.2cr in FY26 (AR/B03, [DOC]), 13 new export geographies (B03, [DOC]). SWOT explicitly names the "China+1 pivot" opportunity (AR p.49). Target of 20%+ export share in 2-3 years is [MGMT] and unconfirmed against peers (B05 flags this as an open peer-verification question). Time to materialise: 12-24 months for agreement activation, 2-3 years for the 20% target.

### FAMILY F — TALENT & ORGANISATIONAL
**F1 — Talent density: NO EVIDENCE FOUND.**
DSIR-recognised in-house R&D (SIRO status) exists (AR p.28, [DOC]) but headcount, PhD count, retention mechanics and ESOP-to-technical-staff allocation are NOT FOUND. A "Technology & Innovation" function was newly established in FY26 (Board's Report, [DOC]) but this is an org-chart change, not a headcount-growth trend.

**F2 — Execution moat: MODERATE, mixed evidence, [DOC]**
Per B05's promise-delivery record: 5 delivered, 4 partial, 1 missed across three calls. Revenue, EBITDA margin and PAT guides were beaten every period tested (audited results, [DOC]). Against this: the Vadodara plant slipped ~6-9 months (Mar-2026 to trial Oct-2026/commercial H2FY27) and capex escalated ~70% (Rs90cr to Rs153cr), neither ever named as a slip or overrun on any call (B05, [DOC] cross-referenced against concall transcripts). This is a genuine but two-sided execution record: strong on P&L delivery, weak on capex/timeline discipline and on naming its own misses. Scored Moderate, not Strong, specifically because of this asymmetry.

### FAMILY G — FINANCIAL & STRUCTURAL
**G1 — War chest: NO EVIDENCE FOUND (fails the test).**
D/E is low (0.17x, B03, [DOC]) but net cash is not growing while investing — the opposite is true: CFO/PAT 0.236 FY26, negative FCF two years running (FY25 -Rs28.9cr, FY26 -Rs50.4cr, B01/B03, [DOC]). Low leverage is a balance-sheet-discipline fact, not a war-chest-accumulation moat; scored 0 to avoid crediting the same input twice (leverage is already captured in B01/B03).

**G2 — WC improvement trajectory: NO EVIDENCE FOUND (fails the test).**
WC days climbed from 79.1 (FY22) to 118.9 (FY26), per B01, [DOC]. Directly contradicts the category; scored 0.

### FAMILY H — ECOSYSTEM & EXTERNAL
**H1 — Industry consolidation beneficiary: NO EVIDENCE FOUND.**
No competitor exit, anti-dumping measure, or compliance-driven shakeout is documented in this corpus as a new/emerging development in FY26 (the "only independent Indian manufacturer" framing is an existing-moat fact from B04, not a new consolidation event).

**H2 — Strategic partnerships: MODERATE (corrected from Strong, per CR-1)**
Run 1 credited four agreements here (Sukrut JV, Weidmann, Electrolink, Ensales), three of which are the identical signed agreements already scored under E2. Per the one-evidence-one-credit rule, this category now scores its unique evidence only: the **Sukrut Electric 50% JV with Quality Power Electrical Equipments Ltd**, Rs5.24cr consideration (Note 36/Board's Report, [DOC]). This is real, executed, and documented, but small in stated consideration and carries no disclosed P&L contribution or EBITDA guide to date — a genuine but modest partnership move, not yet a proven revenue or margin driver. Likelihood High (executed, [DOC]) x Impact Low (small consideration, undisclosed economics) = HL. The Swiss RIP-core technology-transfer arrangement is not separately credited here; it is the input mechanism scored under B1 above (avoiding the same double-credit this correction removes elsewhere). Time to materialise: 12-24 months for Sukrut to show any disclosed contribution.

**H3 — ESG moat: NO EVIDENCE FOUND.**
No renewables %, rating trend, SBTi commitment or ZLD disclosure found in the sections read.

### FAMILY I — STRUCTURAL ASYMMETRIES
**I1 — Talent asymmetry: NO EVIDENCE FOUND, scored 0 by design.**
Leg (a) test: no named inventors on patent filings (there are no patents, per A2), no traceable ex-DRDO/ex-HAL/ex-global-major staff concentration disclosed, and the AR's only compensation disclosure that stands out is the CEO-to-median pay ratio of 53.45x (Annexure D, B03, [DOC]) — this is executive pay, not a technical-staff asymmetry claim, and does not satisfy leg (a). Leg (b) (competitor cannot match pay without breaking its own economics) has no supporting arithmetic anywhere in the corpus. Correctly scored 0 per the family's strict two-leg test.

**I2 — Cannibalization barrier: NO EVIDENCE FOUND, scored 0 by design.**
For the moats claimed above (B1 backward integration, B2 emerging qualification pipeline, H2 Sukrut JV), the honest answer to "what must the best-resourced competitor destroy in its own P&L or org to copy this" is: nothing specific is named in the corpus. The qualification-cycle barrier is a time-and-capital barrier (an execution lead), not a configuration a rival must sacrifice something to match — a large global bushing maker with capital could in principle pursue the same approvals without cannibalising an existing product line or pricing regime. No PSU-rigidity or entrenched-cost-structure argument is evidenced for either direction named in the category definition. Correctly scored 0.

### R1 — Regulatory & policy (Section 4)
See Section 4 below; scored WEAK (LM raw, 🎙️ only) given the PLI trigger was raised once and then dropped.

### Section 3 summary table (corrected)
| # | Category | Evidence? | Type | Strength | Time to materialise |
|---|---|---|---|---|---|
| A1 | Rare manufacturing capability | No (unique evidence insufficient) | - | None | - |
| A2 | Patent/IP pipeline | No | - | None | - |
| A3 | Process innovation | Yes | DOC | Moderate | Active |
| A4 | Product platform | Yes | DOC | Weak | Active |
| B1 | Backward integration/RM security | Yes | DOC | Strong | 12-24m |
| B2 | Qualification lock-in (new-market pipeline) | Yes | DOC | Moderate | 6-18m |
| B3 | Supply chain network effect | No | - | None | - |
| C1 | Customer ecosystem | Yes | DOC | Weak | Active |
| C2 | Customer concentration improving | No (contradicted) | - | None | - |
| D1 | Proprietary data asset | No | - | None | - |
| D2 | Digital platform | No | - | None | - |
| E1 | Geographic first-mover | No | - | None | - |
| E2 | China+1 beneficiary | Yes | DOC/MGMT | Strong | 12-24m |
| F1 | Talent density | No | - | None | - |
| F2 | Execution moat | Yes | DOC (mixed) | Moderate | Active, two-sided |
| G1 | War chest | No (contradicted) | - | None | - |
| G2 | WC improvement | No (contradicted) | - | None | - |
| H1 | Industry consolidation beneficiary | No | - | None | - |
| H2 | Strategic partnerships (Sukrut JV only) | Yes | DOC | Moderate | 12-24m |
| H3 | ESG moat | No | - | None | - |
| I1 | Talent asymmetry | No (by design) | - | None | - |
| I2 | Cannibalization barrier | No (by design) | - | None | - |
| R1 | Regulatory/policy tailwind | Yes | MGMT | Weak | Stalled/uncertain |

**Count with Strong/Moderate evidence: 6** (B1, E2 = Strong x2; A3, B2, F2, H2 = Moderate x4).

**Completionist guard check: 📄 recount performed: 14 unique documented items across 6 categories**, with no item counted in two categories:
- A3 (2): production-efficiency/productivity/OTD stats bundle; new winding machine + SCADA autoclave installation.
- B1 (2): Rs153cr capex commitment; Reg 30 site-progress filing (vastu pujan, machinery installation).
- B2 (3): IEEE US seismic validation in progress; CENELEC Europe compliance under development; 550kV test infrastructure under construction at Vadodara.
- E2 (4): Ensales agreement; Weidmann agreement; Electrolink agreement; audited export-revenue growth (+123.4% to Rs17.2cr).
- F2 (2): audited results beating guidance across three periods; documented capex/timeline slippage (cross-referenced against B05).
- H2 (1): Sukrut Electric JV, Rs5.24cr.

Category count (6) sits within the 3-6 base-rate range named by the completionist guard. No 🎙️ claim was upgraded to 📄 in this recount.

**Evidence mix enumerated (per MN-5 correction):**
- 📄 Documented: 14 items (listed above).
- 🎙️ Management claim: 4 items — (1) A1's "12-13 global bushing makers" count, unscored; (2) E2's 20%+ export-share target; (3) B1's "knowledge successfully transferred" Swiss tech-transfer characterisation (no royalty disclosed); (4) R1's PLI proximity claim.
- 🔍 Analyst inference: 2 items — (1) the tension flagged in 6B between B2's qualification-lock-in thesis and the 18.8% single-customer concentration; (2) the 6B inference that F2's undisclosed-slip pattern could recur on the next milestone.

## SECTION 4: REGULATORY & POLICY TAILWINDS (R1)

**4A. Regulatory approvals in pipeline**
No company-specific regulatory approval is currently pending that would unlock a new capability (the PGCIL/NTPC/NPCIL/DRDO approvals already held are existing-moat facts). The IEEE seismic validation for 138kV/230kV OIP bushings (targeted ready by Sep-2026, [DOC] Board's Report) is the nearest analogue — a product-qualification step, not a government regulatory approval, and is credited under B2 above, not here.

**4B. Government policy tailwinds**
- RIP bushing named (by management) as the #1 candidate product in a proposed Ministry of Power PLI scheme for the power sector; management stated it was "closely working with the Ministry of Power & CEA to avail benefits" (Concall Jan-2025, [MGMT]). This was never mentioned again across the three subsequent calls (B05 dropped_triggers, confirmed by this stage's own grep of the May-2026 transcript, which shows zero PLI mentions).
- Macro tailwinds named in the AR: Rs9.15 lakh crore transmission plan to 2032, Rs3.03 lakh crore RDSS distribution push, ~Rs2 lakh crore POWERGRID capex (AR p.6, [DOC], sourced to CEA/company estimates) — these are sector-wide demand drivers, not company-specific policy benefits, and are shared by every domestic competitor.
- No import-substitution duty, anti-dumping measure, or procurement-preference scheme naming Yash specifically was found.

**4C. Regulatory moat assessment**
Emerging and unconfirmed. The one company-specific policy lever (PLI) was raised once with enthusiasm and then dropped from the narrative for over a year across three subsequent earnings calls — a pattern consistent with either quiet abandonment or simple non-materialisation, and this stage cannot distinguish the two from the documents available. Not scored as an active moat; carried as an optionality-register item.

## OPTIONALITY REGISTER
| Optionality (one line) | Converting 📄 evidence | Where it first appears | Conversion window |
|---|---|---|---|
| PLI scheme benefit for RIP bushings | Formal Ministry of Power/CEA notification naming Yash's product class with a confirmed incentive rate | Gazette notification / exchange filing / Board's Report | Uncertain, stalled since Jan-2025 |
| In-house RIP/RIS core localisation succeeding at scale | Type-test pass + commercial shipment of in-house-made cores without quality escalation | BSE announcement, next AR Board's Report | 6-12 months (trial from Oct-2026) |
| New-market qualification (IEEE US / CENELEC Europe / 550kV) actually clearing | Passed type test/certification with a named date, converting the B2 pipeline from in-progress to granted | Board's Report, exchange filing | 6-18 months |
| FY28 margin step-change from import substitution | FY28 EBITDA margin disclosed meaningfully above the 25.7% FY26 base on a non-price-recovery basis | FY28 AR / FY28 results | 12-24 months, already pushed once (FY27-28 to FY28) |
| Export share reaching 20%+ of revenue | Segment/geography note showing export % crossing 20% | FY28/FY29 AR or interim results | 2-3 years |
| Sukrut JV scaling to Rs150-160cr revenue | Sukrut segment revenue/EBITDA disclosed in consolidated financials, tracking the stated multiple | FY27/FY28 AR segment note | 4-5 years |
| Talent asymmetry from Swiss-trained core engineering team | Named technical hires with traceable Swiss-collaboration/DRDO background; competitor pay-scale comparison | AR remuneration annexure, Role 5.5 verification | Long, unconfirmed |
| HVDC/765kV expansion beyond the Vadodara plant | Board-approved capex/exchange filing for further EHV-class capacity | Board's Report / Reg 30 filing | 3-5 years, management explicitly deferred 18-24 months |

## SECTION 5: EMERGING MOAT SCORECARD (corrected)

| # | Category | Likelihood x Impact | Raw | Evidence type | Multiplier | Adjusted |
|---|---|---|---|---|---|---|
| A1 | Rare manufacturing capability | - (unique evidence insufficient) | 0 | - | - | 0.0 |
| A2 | Patent/IP pipeline | - | 0 | - | - | 0.0 |
| A3 | Process innovation | MM | 2 | DOC | 1.0 | 2.0 |
| A4 | Product platform | ML | 1 | DOC | 1.0 | 1.0 |
| B1 | Backward integration/RM security | HH | 4 | DOC | 1.0 | 4.0 |
| B2 | Qualification lock-in (new-market pipeline) | MM | 2 | DOC | 1.0 | 2.0 |
| B3 | Supply chain network effect | - | 0 | - | - | 0.0 |
| C1 | Customer ecosystem | ML | 1 | DOC | 1.0 | 1.0 |
| C2 | Customer concentration improving | - | 0 | - | - | 0.0 |
| D1 | Proprietary data asset | - | 0 | - | - | 0.0 |
| D2 | Digital platform | - | 0 | - | - | 0.0 |
| E1 | Geographic first-mover | - | 0 | - | - | 0.0 |
| E2 | China+1 beneficiary | HM | 3 | DOC | 1.0 | 3.0 |
| F1 | Talent density | - | 0 | - | - | 0.0 |
| F2 | Execution moat | MM | 2 | DOC | 1.0 | 2.0 |
| G1 | War chest | - | 0 | - | - | 0.0 |
| G2 | WC improvement | - | 0 | - | - | 0.0 |
| H1 | Industry consolidation beneficiary | - | 0 | - | - | 0.0 |
| H2 | Strategic partnerships (Sukrut JV only) | HL | 2 | DOC | 1.0 | 2.0 |
| H3 | ESG moat | - | 0 | - | - | 0.0 |
| I1 | Talent asymmetry | - | 0 | - | - | 0.0 |
| I2 | Cannibalization barrier | - | 0 | - | - | 0.0 |
| R1 | Regulatory/policy tailwind | LM | 1 | MGMT | 0.7 | 0.7 |

**Adjusted total: 17.7**

**I1/I2 contribution: 0.0 (both scored 0; no crossing of any threshold occurs via I1/I2 points). No flag for the operator's I1/I2 review checkpoint from this name.**

**Classification: 12-24 = MODEST MOAT DEVELOPMENT.** (Corrected from run 1's 25.7/STRENGTHENING; the correction removed a double credit (CR-1) and an internally inconsistent existing-vs-emerging application (MJ-1). The 25-point band edge itself carried no weight in this rescoring — the fixes were applied on their own merits and the result happens to land at 17.7, in the MODEST band.)

## SECTION 6: TIMELINE, RISKS & COMBINED ASSESSMENT

### 6A. Moat evolution timeline
- **Next 12 months**: Vadodara trial production (targeted Oct-2026); Ensales US agreement activation; IEEE US seismic validation targeted ready Sep-2026; FY27 results tracking the Rs360-400cr invoicing guide (explicitly decoupled by management from plant success, B05).
- **12-24 months**: Vadodara commercial production (H2FY27 target); Sukrut integration showing first disclosed contribution; export share progress toward the 20%+ target; CENELEC Europe compliance outcome.
- **24-36 months**: FY28 EBITDA margin step-change from import substitution (already re-guided once from "FY27-28" to "FY28"); RIP export unlock at scale to US/Europe if the B2 qualification pipeline clears.
- **3-5 years**: Sukrut reaching Rs150-160cr revenue (management target, no EBITDA guide given); possible HVDC/765kV capacity decision; PLI scheme resolution one way or the other.

### 6B. Risks to top-scoring emerging moats
- **B1 (backward integration)**: risk = further Vadodara delay or type-test failure on the localised core. Early warning: any further slip past the Oct-2026 trial date, or a type-test failure disclosure.
- **E2 (China+1)**: risk = signed representation/distribution agreements are not guaranteed order flow. Early warning: no US order bookings within 12 months of the Ensales agreement's effective date.
- **B2 (new-market qualification pipeline)**: risk = any of the three in-progress qualifications (IEEE US, CENELEC Europe, 550kV testing) fails or slips past its targeted date, converting an emerging category back to zero. [INF] Early warning: no pass/fail disclosure by the targeted dates.
- **H2 (Sukrut JV)**: risk = underperformance under 50-50 shared control with no EBITDA guidance given to date. Early warning: continued silence on Sukrut segment economics after 2-3 more quarters.
- **F2 (execution moat)**: risk = the pattern of reframing slips and overruns without naming them (plant timeline, capex) could recur on Sukrut or the next expansion phase, and would not be self-disclosed if it did. [INF] Early warning: any further undisclosed capex/timeline change on an active project.
- Cross-cutting: the qualification-lock-in thesis (B2, and the confirmed B01 M10 mechanism) assumes a diversified customer base, but 18.8% concentration in one customer (C2, scored 0) sits in tension with that assumption. [INF] Early warning: concentration rising further or a second customer approaching similar share.

### 6C. Combined Gate 0 + Emerging Moat table (corrected, per MN-3)
| Metric | Value |
|---|---|
| Core score (B01, run-1 value, parallel B01 correction in flight) | 70 |
| Existing moat score (B01, per this stage's own M11 override) | 16/60, moats_confirmed 4 (M1, M3, M4, M10), STRONG (4-5 band) |
| Backward classification (B01, run-1 value) | GOOD (capped by Block B cash deal-breaker, 3/20) |
| Emerging moat score (this stage, corrected) | 17.7 |
| Emerging moat classification | MODEST MOAT DEVELOPMENT |

### 6D. Combined classification (corrected)
**GOOD.** Reasoning: backward classification is GOOD (held down from a higher band purely by the Block B cash-conversion deal-breaker, per B01). The existing moat read is STRONG on this stage's own corrected count (4/5 types, 16/60). The forward layer is real but MODEST, not STRENGTHENING or EXPANSION: after removing the double-credited agreements and the internally inconsistent A1/B2 treatment, only backward integration (B1, pre-commercial with one slip and one cost overrun) and China+1 distribution (E2, signed agreements without yet a single disclosed order) carry Strong ratings; the rest of the forward layer (A3, B2, F2, H2) is Moderate at best and thin on independent anchors. This does not clear the bar for the "+" elevation the transition framework reserves for a GOOD or AVERAGE backward score paired with a genuinely EXPANDING or at minimum STRENGTHENING forward moat. GOOD (plain) reflects a real climb attempt that remains largely unproven rather than a documented re-rating setup.

### 6E. Final output card
**Moat evolution map (existing to emerging, per family)**
- Product & Technology: existing qualification-based product moat (OIP/RIP approvals, existing-fact, captured once at Gate 0) -> emerging voltage-class extension in progress (245kV to 550kV, IEEE US and CENELEC Europe validations unresolved) and one-year process-efficiency gains (A3).
- Supply Chain: existing import-dependent RIP core sourcing -> emerging backward integration (B1) ending 95% import dependence, if delivered on the re-guided timeline; new-market qualification lock-in still in progress, not yet cleared (B2).
- Geographic/Access: existing 60+ country footprint -> emerging direct-presence model in the US (subsidiary + Ensales) and formal European/UK/North African distribution (E2), explicitly framed as a China+1 play.
- Ecosystem/External: existing single-focus bushing specialist -> emerging, still-small broader transformer-component participation via the Sukrut JV with Quality Power (H2), Rs5.24cr consideration, no disclosed P&L contribution yet.

**Catalysts to watch, next 12 months**
1. Vadodara trial production (targeted Oct-2026) — tests whether the core localisation and 550kV capability are real.
2. H1FY27/FY27 results tracking the Rs360-400cr invoicing guide, which management says does not depend on plant success — a clean near-term test of the base business independent of the transition thesis.
3. First disclosed evidence (or continued silence) on Ensales-driven US order flow, the IEEE US seismic validation outcome (targeted Sep-2026), and Sukrut segment economics.

**Biggest risk to the emerging moats**
The credibility pattern flagged in F2: management has twice reframed a slipping timeline or growing cost (Vadodara: ~6-9 months late, ~70% over budget) as "on track" rather than naming it a miss. If this recurs on the next major milestone (core type-test, the B2 qualification pipeline, Sukrut integration, or the FY28 margin step-change), the market will have less warning than the underlying facts warrant, and Section 1B exit-multiple work in Stage 11 should not assume the 550kV/backward-integration re-rating case is de-risked until the trial-production evidence actually lands. Separately, this stage's own correction (removing a double credit and an uneven existing-vs-emerging test) shows the forward-moat read was overstated by roughly a third in run 1; Stage 11 and Stage 13 should treat the emerging layer here as MODEST, not STRENGTHENING, until independent evidence of the B2 pipeline or H2 Sukrut contribution actually lands.

---
Input gaps carried into B07 (see also B00/B01):
- The prescribed Section 2C fixed-asset-turnover arithmetic is now run (153 x 4.54 = 694.6cr = 295% of FY26 revenue) but is a mechanical ceiling, not a forecast, per the caveat above; the underlying FAT figure (4.54x) is an injected B01 value, not independently re-derived by this stage.
- The run-1 unit-capacity growth proxy (9,000 to 15,000 units/yr) is dropped: its base conflicts with this stage's own 2A OIP-alone figure of 10,000 units/yr and cannot be reconciled from the corpus read at this stage. NOT FOUND, not restated.
- No patent/IP filing exists anywhere in the corpus (A2 NO EVIDENCE FOUND is a genuine absence, not a search failure — confirmed by direct full-text search).
- R&D headcount trend (F1) NOT FOUND; DSIR/SIRO recognition is documented but headcount, specialist count and retention mechanics are not disclosed.
- I1 talent-asymmetry leg (a) evidence (named inventors, ex-DRDO/ex-HAL staff, traceable employment history) NOT FOUND in the corpus available to this stage.
- Post-07-Aug-2026 preferential-allotment shareholding pattern not in corpus (carried from B00/B01, immaterial to this stage's scoring).
- B01 (Gate 0) is under parallel correction for the ROCE formula-substitution and E2 dilution-note findings (MJ-2, MJ-3 in 12c-verifier-framework-run1.md); this stage used B01 run-1 values (core 70, GOOD) as injected input per the task brief and takes no position on those two findings, which are outside this stage's scope.
