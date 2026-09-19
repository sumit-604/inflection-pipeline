# VERIFIER C (B12c): FRAMEWORK ADHERENCE, PHASE 1 SCOPE
Company: IOL Chemicals & Pharmaceuticals Ltd (IOLCP) | Run date: 2026-09-19 | Model: claude-opus-5

Scope: Gate 0 (B01) and Emerging Moat (B07) only. The valuation audit (B10/B11, rules 4-7 and 11-15) is PENDING PHASE 3. Rule 9 (stage 13 narrative) and rule 10 (09b dossier) are also out of phase-1 scope.

Rule sources: prompts/01-gate-0-pipeline.md; prompts/07-emerging-moat-pipeline.md.
Audited artifacts: outputs/reports/01-gate0.md, outputs/blocks/B01-gate0.yaml, outputs/reports/07-emoat.md, outputs/blocks/B07-emoat.yaml.
Spot re-derivation source: inputs/screening/screener-standalone-{Profit_Loss,Balance_Sheet,Cash_Flow}.csv (all Rs Cr per the CSV face).

This audit judges rule application. Source fidelity of individual numbers belongs to Verifier A. Where I re-derived a figure below, I did it to test a rule, not to certify the number.

---

## 1. GATE 0 (B01) COMPLIANCE TABLE

Re-derivation inputs confirmed against the screener CSVs: Sales FY17-FY26 710.65 / 983.3 / 1685.33 / 1894.47 / 1966.98 / 2184.02 / 2217.11 / 2132.79 / 2079.21 / 2319.06 (screener-standalone-Profit_Loss.csv, Sales row); Net profit 4.67 ... 137.72 (same file, Net profit row); ROCE FY17 blank, FY18-FY26 15.03% ... 10.65% (screener-standalone-Balance_Sheet.csv, "Return on Capital Emp" row); Equity + Reserves (same file, rows 3-4). The screener Cash_Flow CSV holds only CFO / CFI / CFF / Net Cash Flow rows (no capex line). The Balance_Sheet CSV holds no trade payables row. Both gaps are confirmed.

| # | Rule | Result | Recomputed / note |
|---|---|---|---|
| 1 | Opening "Data available" line (rule 6) | PASS | 10 years FY17-FY26 stated |
| 2 | Anchor on every extracted number (rule 4) | PASS | Spot-checked; anchors present |
| 3 | A1 median ROCE, screener's own ROCE used | PASS | 9 values, median 15.03% (FY18) -> 3 |
| 4 | A2 minimum ROCE | PASS | 8.85% (FY25) -> 1 |
| 5 | A3 median ROE, avg NW formula, closing NW for earliest year stated | PASS | Recomputed all 10 years; median (9.67+12.50)/2 = 11.08% -> 0 |
| 6 | A4 ROCE trend | PASS | FY18 15.03 -> FY26 10.65 = -4.38pp -> 1 (FY17 blank, FY18 earliest usable, stated) |
| 7 | B1 cumulative CFO/PAT | PASS | 2224.55 / 1754.70 = 1.268 -> 5 (sums recomputed) |
| 8 | B2 FCF-positive years, capex = CFS purchase of PPE + intangibles, "do not substitute alternatives" | FAIL (MAJOR) | See G0-1. Recomputed on the CFS basis only (FY25 -34.87, FY26 +41.43): 1 of 2 = 50% -> B2 = 2, not 0. Strict N/A reading gives 0. Either way the AR p.24 chart capex is a substituted basis |
| 9 | B3 cumulative FCF/PAT | PASS (score) | CFS-basis FY25-FY26: 6.56 / 238.72 = 0.03 -> 0; same score as maker, but same basis defect as rule 8 |
| 10 | B4 change in WC days, latest vs earliest | FAIL (MINOR) | See G0-2. Scored on a 1-year window (FY25 -> FY26, -1.04 days -> 3). Block B sits exactly at the deal-breaker-2 line (8) on this 1-year read |
| 11 | C1 revenue CAGR | PASS | (2319.06/710.65)^(1/9)-1 = 14.04% -> 3 |
| 12 | C2 PAT CAGR | PASS | (137.72/4.67)^(1/9)-1 = 45.65% -> 5 |
| 13 | C3 positive YoY revenue years | PASS | Declines FY24, FY25; 7/9 = 77.8% -> 3 |
| 14 | C4 PAT CAGR minus revenue CAGR | PASS | +31.6pp -> 5 |
| 15 | CAGR edge rules (negative endpoint, loss-to-profit swing, C4 when PAT N/M) | PASS | FY17 PAT positive, rules correctly not triggered; base-effect disclosed in data_notes |
| 16 | D1 net debt/EBITDA | PASS | 135.42 - 198.25 = net cash -> 5 |
| 17 | D2 interest coverage | PASS | 189.69/14.55 = 13.0x (13.7x if other income is included via PBT + interest 184.44 + 14.55); >= 10x either way -> 5 |
| 18 | D3 debt/equity | PASS | 0.075 -> 5 |
| 19 | D4 current ratio | PASS | 1.779 -> 4 |
| 20 | E1 promoter holding | PASS | 62.28% -> 5 |
| 21 | E2 promoter change over 3 years | FAIL (MINOR) | See G0-3. 21-month window, not 3 years; score unchanged under a +14.09pp move |
| 22 | E3 pledge | PASS | 0% -> 5 |
| 23 | E4 contingent liabilities/NW | PASS | 0.31% -> 5 |
| 24 | PEER DATA NEEDED rule (score 0, never guess peers) | PASS | M2, M5, M6, M7, M9 at 0 and marked |
| 25 | Non-peer moat tests M1, M3, M4, M8, M10, M11, M12 | PASS | M1 OPM 14.41 -> 11.64 (-2.77pp) with 14.04% CAGR -> 1; M3 FAT 1.96x, ROCE 10.65% -> 0; M4 2 decline years -> 1; M10 -> 1; M11 latest 3y 1.51% < prior 5.38% -> 0; M12 WC days > 45 -> 0 |
| 26 | Moat classification | PASS | 0 moats >= 3 -> NONE |
| 27 | Data confidence | PASS | 10 years -> full, no downgrade |
| 28 | Classification matrix | PASS | Core 5+8+16+19+20 = 68; 60-79 + NONE -> GOOD |
| 29 | Deal-breakers 1-9 evaluated, driving years named | PASS | DB1 triggered (Block A 5 < 8), driver years FY22-FY26 named |
| 30 | FLAG-GATE0 only when classification <= AVERAGE | PASS | GOOD, flags [] correct |
| 31 | "No qualitative judgments. Only numbers and the scoring rules" (operating rule 2) | FAIL (MINOR) | See G0-4 |
| 32 | YAML schema complete; analyst_note <= 200 words | PASS | About 120 words |

Gate 0 rules checked: 32. PASS 28. FAIL 4 (1 MAJOR, 3 MINOR).

Classification robustness: GOOD survives every reading tested. Block B ranges 5 to 10 across the B2 and B4 readings. Core ranges 65 to 70. Every value sits in the 60-79 band with moat class NONE, so the matrix returns GOOD. Deal-breaker 1 caps at GOOD independently. What changes: under the strict reading of B4 (N/A, 0), deal-breaker 2 also fires, and the deal_breakers list gains a Block B entry. That list feeds FLAG-CASH downstream.

### Gate 0 findings

**G0-1 (MAJOR). B2/B3 capex basis substituted.** The formula section is fixed: "capex = purchase of PPE + intangibles from cash flow statement ... do not substitute alternatives" (prompts/01-gate-0-pipeline.md, FORMULA DEFINITIONS). B01 fills FY22-FY24 capex from the AR capex-utilisation chart (153 / 224 / 257, AR p.24), and the report itself says this is "not confirmed to be on the identical cash-paid CFS basis" (01-gate0.md, Block B capex basis note). Operating rule 5 names the valid fill for a missing data point: "N/A (not in provided data)". Two valid readings exist. Reading 1: score only the CFS years FY25-FY26, so B2 = 2 (1 of 2 FCF-positive, 50%). Reading 2: treat FCF history as N/A, so B2 = 0. The separating observation is whether the FY22-FY24 standalone cash flow statements (FY23 and FY24 ARs) enter the corpus. Either way, the maker's FCF-negative count for FY22 and FY23 rests on a basis the rule forbids. Classification unchanged. Rework ask: restate B2/B3 on the CFS basis, or source the FY22-FY24 CFS capex lines.

**G0-2 (MINOR). B4 scored on a one-year window.** The rule compares latest against earliest WC days. Payables exist only for FY25 and FY26, so the "earliest" is FY25. The disclosure is honest. The consequence matters: Block B lands exactly at 8, one point from deal-breaker 2, and that one point comes from B4 = 3 on a 1-year change of -1.04 days. The report's own supplementary line shows receivable days +16.4 over FY22-FY26, which points the other way. Downstream stages should read "deal-breaker 2 not triggered" as fragile, not as clean.

**G0-3 (MINOR). E2 window short of 3 years.** Scored on Sep-2024 to Jun-2026 (about 21 months). Disclosed in input_gaps. Score unchanged, because any move of +1pp or more scores 5 and the observed move is +14.09pp.

**G0-4 (MINOR). Qualitative framing inside a numbers-only stage.** The deal-breaker driver text and analyst_note describe FY19-FY21 as an "Ibuprofen API pricing supercycle" and cite company memory (LBF3). Operating rule 2 bars qualitative judgment in this stage. The analyst_note also says "A1-A4 all score off the post-reset band". That is inaccurate: the A1 median (15.03%) is the FY18 value from a 9-year series that includes the FY19-FY21 peak, and A4 starts at FY18. No score changes.

---

## 2. EMERGING MOAT (B07) COMPLIANCE TABLE

| # | Rule | Result | Recomputed / note |
|---|---|---|---|
| 1 | All six sections plus optionality register present | PASS | Sections 1-6 plus register present |
| 2 | Evidence taxonomy on every evidence item | PASS | Tiers marked throughout |
| 3 | Source anchors to primary documents (AR p., call, slide) | FAIL (MINOR) | See EM-7 |
| 4 | "NO EVIDENCE FOUND" where no evidence exists, no force-fit | PASS | A4, B1, B3, C2, D1, D2, E1, G2, I1, I2 stated |
| 5 | All 23 rows (22 categories + R1) addressed | PASS | A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3, I1, I2, R1 = 23 |
| 6 | Raw score from the L x I matrix (HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1) | FAIL (CRITICAL) | See EM-1. LM scored 2 on four rows |
| 7 | Evidence multiplier matches stated tier (1.0 / 0.7 / 0.5) | FAIL (MINOR) | See EM-5. A2 stated 📄, multiplied 0.7 |
| 8 | Scores consistent with stated evidence tiers (no 🎙️ scored as 📄) | FAIL (MAJOR) | See EM-2. C1 vs H2 |
| 9 | One improvement, one mechanism (no double credit) | FAIL (MAJOR) | See EM-3. A1 and R1 |
| 10 | Completionist 📄 recount performed and reconciles | FAIL (MINOR) | See EM-6. Breakdown sums to 18, line says 28 |
| 11 | Section 3 summary table, all rows, Strong/Moderate count stated | PASS | 23 rows; 5 Strong/Moderate plus R1 |
| 12 | Classification band applied to a correct total | FAIL (CRITICAL, consequential to rule 6) | 26.3 -> 23.4; STRENGTHENING -> MODEST |
| 13 | Category 21 (I1) present; both legs tested; 0 unless both evidenced with a 📄 (b) leg | PASS | Both legs absent, scored 0 |
| 14 | Category 22 (I2) present; sacrifice named or 0 | PASS | Execution lead, not configuration, scored 0 |
| 15 | I1/I2 contribution stated separately | PASS | 0.0 stated |
| 16 | 2C arithmetic shown | PASS | 2319.1 / 1258.68 = 1.843x; arithmetic shown |
| 17 | 2C scope: "total capex under execution" | FAIL (MAJOR) | See EM-4. 142.6% -> 39.3% |
| 18 | Optionality register, four columns, carried into YAML | PASS | 7 rows, mirrored in YAML |
| 19 | 6C uses injected Gate 0 fields (core score, existing moat count, both classifications) | FAIL (MINOR) | See EM-8 |
| 20 | 6D combined classification per the standard matrix | FAIL (consequential to rule 6) | GOOD+ is argued from STRENGTHENING; at MODEST that basis falls. The stage prompt names the standard matrix but does not print its cells, so I do not assert the replacement label. Stage 7 must re-map |
| 21 | Report ends with the fenced YAML block | FAIL (MINOR) | See EM-9 |
| 22 | Section 4 R1 structure (4A / 4B / 4C) | PASS | 4B NOT FOUND stated explicitly |
| 23 | 6A-6E present (timeline, risks, combined table, classification, output card) | PASS | Present |
| 24 | analyst_note <= 200 words | PASS | About 100 words |

Emerging Moat rules checked: 24. PASS 13. FAIL 11 (1 CRITICAL finding covering rules 6, 12 and 20; 3 MAJOR; 5 MINOR).

### Recomputed Section 5 scorecard (matrix and multiplier only; the maker's L x I letters kept)

| # | Maker L x I | Maker raw | Correct raw | Tier (maker) | Multiplier | Maker adj | Recomputed adj |
|---|---|---|---|---|---|---|---|
| A1 | HM | 3 | 3 | 📄 | 1.0 | 3.0 | 3.0 |
| A2 | LL | 1 | 1 | 📄 | 1.0 (maker 0.7) | 0.7 | 1.0 |
| A3 | HM | 3 | 3 | 📄 | 1.0 | 3.0 | 3.0 |
| B2 | LM | 2 | **1** | 🎙️ | 0.7 | 1.4 | **0.7** |
| C1 | HH | 4 | 4 | 📄 | 1.0 | 4.0 | 4.0 |
| E2 | LM | 2 | **1** | 🔍 | 0.5 | 1.0 | **0.5** |
| F1 | LM | 2 | **1** | 📄 | 1.0 | 2.0 | **1.0** |
| F2 | LL | 1 | 1 | 🎙️ | 0.7 | 0.7 | 0.7 |
| G1 | LM | 2 | **1** | 📄 | 1.0 | 2.0 | **1.0** |
| H1 | LL | 1 | 1 | 🔍 | 0.5 | 0.5 | 0.5 |
| H2 | HM | 3 | 3 | 📄 | 1.0 | 3.0 | 3.0 |
| H3 | HM | 3 | 3 | 📄 | 1.0 | 3.0 | 3.0 |
| R1 | MM | 2 | 2 | 📄 | 1.0 | 2.0 | 2.0 |
| Others (10 rows) | none | 0 | 0 | none | none | 0.0 | 0.0 |
| **Total** | | | | | | **26.3** | **23.4** |

With A2 left at the maker's 0.7, the total is 23.1. Both values sit in the 12-24 band: **MODEST MOAT DEVELOPMENT**, not STRENGTHENING. EM-2 and EM-3 only push the total lower (C1 at 🎙️ = 2.8 gives 22.2; R1 removed as a double credit gives 20.2 or 21.4). MODEST holds under every combination tested.

### Emerging Moat findings

**EM-1 (CRITICAL). Raw-score matrix misapplied; classification flips.** The rule reads "HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1" (prompts/07-emerging-moat-pipeline.md, Section 5). B07 assigns LM a raw 2 on four rows: B2, E2, F1, G1 (07-emoat.md, Section 5 table). The correct raw value is 1. Corrected, em_score falls from 26.3 to 23.4 (23.1 on the maker's A2 multiplier). Three consequences follow. (1) em_classification moves from STRENGTHENING (25-39) to MODEST (12-24). (2) The score drops below the "EM >= 25" UA qualifier, which the stage prompt names as absolute (operator ruling 20-Aug-2026). A Section 1B input therefore changes state. (3) combined_assessment GOOD+ loses its stated basis (6D argues GOOD+ from "a STRENGTHENING (not EXPANSION) forward score"). This finding changes a classification and a downstream valuation qualifier, so it is CRITICAL. Rework ask: stage 7 re-scores Section 5 and re-maps 6D; block fields em_score, em_classification, combined_assessment, combined_reasoning and analyst_note change.

**EM-2 (MAJOR). C1 scored at 📄 HH on evidence the report grades 🎙️ elsewhere.** C1 (customer ecosystem) scores HH x 1.0 = 4.0, "STRONG". The load-bearing claim is embedded, customer-pulled relationships with European Anchor Customers. H2 grades those same Anchor Customer relationships as "still 🎙️ MANAGEMENT CLAIM tier: contracts ... being finalized" (07-emoat.md, H2). Section 6B says C1's "entire evidentiary basis (a Reg 30 filing describing intent, not a signed customer contract) could prove premature". The documented part is the committed capex, the installed facility and the GMP certificate. The customer relationship itself is a claim. One body of evidence carries two tiers in two categories. Two readings exist. Reading 1: 📄 on the capex-committed leg, so 4.0 stands. Reading 2: 🎙️ on the relationship leg, so 4 x 0.7 = 2.8. The separating observation is a named customer or a signed contract disclosure (already in the optionality register). Classification is MODEST under both readings once EM-1 is fixed.

**EM-3 (MAJOR). Regulatory filing machine credited twice (A1 and R1).** A1 (3.0) credits "5 CEP grants ... 2 new CEP submissions pending, NMPA China approval + filing, MFDS Korea DMF registrations + filing". R1 (2.0) credits the same pending EDQM, MFDS and NMPA filings (4A table). 4C describes the emerging R1 piece as "the extension of that filing machine into new countries (China, Korea) and new molecules". This is one improvement credited through two mechanisms. The 📄 recount says R1 was "not double-counted", but that line addresses the recount, not the score. Rework ask: credit the filing extension once, or show R1 evidence that is separate from A1 (4B policy tailwinds are NOT FOUND).

**EM-4 (MAJOR). capex_embedded_growth_pct includes capex that is not under execution.** The 2C formula uses "total capex under execution". B07 includes the Rs 1,200-1,400 Cr greenfield (report table: "🎙️ land secured, approvals 'in process', no firm commissioning date"). The report calls the literal formula the reason for the choice, but the greenfield fails the formula's own qualifier, "under execution". The dated Rs 495 Cr tranche is the capex under execution: 495 x 1.843 = Rs 912 Cr = **39.3%** of FY26 revenue, per the maker's own arithmetic (07-emoat.md, 2C). The YAML carries 142.6. This field feeds stage 9 and Pillar 3 catalyst work. Rework ask: set capex_embedded_growth_pct to 39.3 and keep the 142.6 figure as a labelled capacity-ceiling note only.

**EM-5 (MINOR). A2 multiplier does not match its stated tier.** The row lists tier "📄 (contradictory)" and applies 0.7. The rule maps 📄 to 1.0 and has no discount for contradictory evidence. The contradiction belongs in the likelihood letter (already LL). Effect: +0.3.

**EM-6 (MINOR). Completionist recount does not reconcile.** The line reads "28 documented items across 5 Strong/Moderate categories (A1: 5; A3: 5; C1: 1; H2: 1; H3: 6)". The listed breakdown sums to 18, not 28. evidence_mix.documented = 28 carries the unreconciled figure. The guard outcome does not change: 5 active categories sit well under the 12-category trigger. Note that 13 rows carry nonzero scores. The YAML schema defines "active" as Strong/Moderate only, so the guard is not formally tripped.

**EM-7 (MINOR). Anchors point to upstream blocks, not primary documents.** Several evidence items anchor to "B05", "B03", "B04" or "B01/B02/B03" (for example G1 "per B03", G2 "B01/B02/B03, Note 10/49", 1C table anchors). Rule 3 asks for (AR p.__), (Q_ FY__ call), (Inv. Pres. slide __). A second-hand anchor makes Verifier A trace two hops.

**EM-8 (MINOR). 6C omits the existing moat count.** 6C must use "core score, existing moat count, both classifications" from the injected Gate 0 block. The table shows core 68, grand total 71 and moat_score 3, but not moats_confirmed = 0 or moat_class = NONE.

**EM-9 (MINOR). Report file does not end with the YAML block.** The stage prompt says "Full six-section report, then end with exactly this fenced YAML block". 07-emoat.md ends at Section 6E. The block exists only in outputs/blocks/B07-emoat.yaml. B01 carries its block in both places.

### Checks that passed and matter
- Category 21 (I1): both legs tested and absent; scored 0 correctly. The CEO pay ratio (283.82x) was correctly refused as leg (a) evidence.
- Category 22 (I2): the honest answer "execution lead, not configuration" was given and scored 0 as the rule directs.
- The greenfield scores zero in the scorecard and sits in the optionality register. That is correct application of the skepticism rule. EM-4 is only about its inclusion in the 2C capex base.

---

## 3. VALUATION (B11)
PENDING PHASE 3. B10 and B11 do not exist yet. Rules 4-7 and 11-15 (growth symmetry, pillar mechanics, method plurality, Role 1 exit construction, Amendment 19 FV path, Expectation Ledger, ledger gates, skill-to-source fidelity) are not run. The rule 6 B09 downstream-candidates check and the rule 9 narrative check also run at that pass.

---

## 4. SUMMARY

| Framework | Rules checked | PASS | FAIL | Critical | Major | Minor |
|---|---|---|---|---|---|---|
| Gate 0 (B01) | 32 | 28 | 4 | 0 | 1 | 3 |
| Emerging Moat (B07) | 24 | 13 | 11 | 1 | 3 | 5 |
| Valuation (B11) | 0 | n/a | n/a | PENDING PHASE 3 | | |
| **Total** | **56** | **41** | **15** | **1** | **4** | **8** |

Acceptance rate: 41 / 56 = 73.2%. The denominator is 4 or more, so the rate applies. It sits above the 60% REWORK line. The single CRITICAL is a Verifier C finding, so under the header rule it does not trigger REWORK on its own. I recommend that the orchestrator send stage 7 back for a Section 5 re-score (EM-1) before stage 9 and stage 11 consume em_score. The EM >= 25 UA qualifier changes state under the corrected score.

Gate 0 classification GOOD stands. Emerging Moat classification: maker STRENGTHENING (26.3); recomputed MODEST MOAT DEVELOPMENT (23.4).

```yaml
stage: B12c
company: "IOLCP"
run_date: "2026-09-19"
model: "claude-opus-5"
status: complete
scope: "PHASE 1 (Gate 0 B01 + Emerging Moat B07 only); valuation audit PENDING PHASE 3"
gate0: {rules_checked: 32, fails: ["G0-1 MAJOR: B2/B3 FCF built on AR p.24 capex chart for FY22-FY24, a substituted basis the fixed formula forbids; CFS-basis B2 = 2 (FY25-FY26, 1 of 2 positive) or 0 if N/A, maker 0; classification GOOD unchanged", "G0-2 MINOR: B4 scored on a 1-year window (FY25->FY26, -1.04 days -> 3); Block B sits exactly at deal-breaker-2 line (8) on this read, fragile", "G0-3 MINOR: E2 scored on a 21-month window (Sep-2024 to Jun-2026), not 3 years; score unchanged", "G0-4 MINOR: qualitative framing (Ibuprofen supercycle, company-memory LBF3) in a numbers-only stage; analyst_note says A1-A4 score off the post-reset band, but A1 median (15.03%, FY18) spans the peak years"]}
emoat: {rules_checked: 24, fails: ["EM-1 CRITICAL: L x I matrix misapplied, LM scored 2 (rule says 1) on B2, E2, F1, G1; em_score 26.3 -> 23.4 (23.1 on maker A2 multiplier); STRENGTHENING -> MODEST; crosses below the EM >= 25 UA qualifier; 6D GOOD+ loses its basis, stage 7 must re-map (rules 6, 12, 20)", "EM-2 MAJOR: C1 scored HH at 1.0 (4.0) on Anchor Customer relationships that H2 grades as management claim ('contracts being finalized'); 0.7 reading gives 2.8", "EM-3 MAJOR: same EDQM/MFDS/NMPA filing extension credited in A1 (3.0) and R1 (2.0); one improvement, two mechanisms", "EM-4 MAJOR: capex_embedded_growth_pct 142.6 includes the undated Rs 1,200-1,400 Cr greenfield, not capex under execution; dated Rs 495 Cr tranche gives 39.3", "EM-5 MINOR: A2 stated DOCUMENTED tier but multiplied 0.7; rule gives 1.0 (+0.3)", "EM-6 MINOR: completionist recount says 28 documented items, listed breakdown sums to 18; evidence_mix.documented 28 unreconciled; guard outcome unchanged", "EM-7 MINOR: several anchors point to upstream blocks (B03, B04, B05) instead of primary documents", "EM-8 MINOR: 6C omits existing moat count (moats_confirmed 0, moat_class NONE)", "EM-9 MINOR: 07-emoat.md does not end with the fenced YAML block; block exists only in blocks/B07-emoat.yaml"]}
valuation: {rules_checked: 0, fails: [], status: "PENDING PHASE 3 (B10/B11 not yet produced)"}
expectation_ledger: {present: false, downside_row: false, all_rows_confirm_by: false, all_rows_metric_threshold: false, prob_in_range: false, decay_status_valid: false, off_ledger_credit: false, residual_pct_cmp: 0, residual_starter_cap_ok: true, fails: [], status: "NOT IN SCOPE (phase 3)"}
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: [], status: "NOT IN SCOPE (stage 13)"}
recomputed_destination_pe: ""
recomputed_decision: ""
recomputed_em: {maker_em_score: 26.3, recomputed_em_score: 23.4, maker_class: "STRENGTHENING", recomputed_class: "MODEST", ua_em25_qualifier: "fails at recomputed score", capex_embedded_growth_pct_recomputed: 39.3}
findings:
  - {id: "EM-1", severity: "CRITICAL", location: "07-emoat.md Section 5 rows B2, E2, F1, G1; B07 em_score, em_classification, combined_assessment", rule: "07 Section 5 matrix: ML/LM=1", claimed: "LM raw 2; em_score 26.3 STRENGTHENING", recomputed: "LM raw 1; em_score 23.4 MODEST", action: "REWORK stage 7 Section 5 and 6D recommended"}
  - {id: "EM-2", severity: "MAJOR", location: "07-emoat.md C1 vs H2", rule: "07 verifier rule 3 tier consistency", claimed: "C1 HH x 1.0 = 4.0", recomputed: "4.0 (capex-committed reading) or 2.8 (relationship is a claim)", action: "state one tier for the Anchor Customer evidence"}
  - {id: "EM-3", severity: "MAJOR", location: "07-emoat.md A1 and R1/4A-4C", rule: "one improvement, one mechanism", claimed: "A1 3.0 + R1 2.0 on the same filings", recomputed: "credit once", action: "separate R1 evidence or drop the overlap"}
  - {id: "EM-4", severity: "MAJOR", location: "07-emoat.md 2C; B07 capex_embedded_growth_pct", rule: "07 2C: total capex under execution", claimed: "142.6", recomputed: "39.3", action: "restate the field; keep 142.6 as a labelled ceiling note"}
  - {id: "G0-1", severity: "MAJOR", location: "01-gate0.md Block B B2/B3", rule: "01 FORMULA DEFINITIONS: capex from CFS, do not substitute", claimed: "B2 0 on 5 years incl. AR-chart capex", recomputed: "B2 2 (CFS FY25-FY26) or 0 (N/A)", action: "restate on CFS basis or source FY22-FY24 CFS"}
  - {id: "G0-2", severity: "MINOR", location: "01-gate0.md B4", rule: "01 B4 latest vs earliest", claimed: "B4 3 on FY25->FY26", recomputed: "same score; 1-year window, deal-breaker 2 fragile", action: "carry fragility note"}
  - {id: "G0-3", severity: "MINOR", location: "01-gate0.md E2", rule: "01 E2 3-year window", claimed: "E2 5 on 21 months", recomputed: "5", action: "none"}
  - {id: "G0-4", severity: "MINOR", location: "01-gate0.md deal-breaker text, analyst_note", rule: "01 operating rule 2", claimed: "qualitative supercycle framing; A1-A4 post-reset claim", recomputed: "n/a", action: "trim"}
  - {id: "EM-5", severity: "MINOR", location: "07-emoat.md Section 5 A2", rule: "multiplier by tier", claimed: "0.7", recomputed: "1.0", action: "fix"}
  - {id: "EM-6", severity: "MINOR", location: "07-emoat.md Section 3 recount; B07 evidence_mix", rule: "completionist recount", claimed: "28", recomputed: "18 per listed breakdown", action: "reconcile"}
  - {id: "EM-7", severity: "MINOR", location: "07-emoat.md G1, G2, 1C", rule: "07 operating rule 3 anchors", claimed: "anchors to B03/B04/B05", recomputed: "n/a", action: "anchor to primary documents"}
  - {id: "EM-8", severity: "MINOR", location: "07-emoat.md 6C", rule: "6C injected Gate 0 fields", claimed: "moat count absent", recomputed: "moats_confirmed 0, NONE", action: "add"}
  - {id: "EM-9", severity: "MINOR", location: "07-emoat.md end", rule: "07 OUTPUT: end with fenced YAML", claimed: "absent", recomputed: "n/a", action: "append block"}
critical_count: 1
major_count: 4
minor_count: 8
acceptance_rate: 73.2
```
