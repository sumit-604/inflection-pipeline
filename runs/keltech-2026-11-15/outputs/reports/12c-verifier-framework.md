# VERIFIER C: FRAMEWORK ADHERENCE. KELTECH, run 2026-11-15 (PHASE 1 SCOPE)
Model claude-opus-5-5 (matches .claude/agents/verifier-c-framework.md frontmatter, effort xhigh). Audit date 2026-11-16.

## 0. Scope, inputs, conventions

Scope. Phase 1 only. This run audits Gate 0 (B01) and the Emerging Moat scan (B07). The valuation-adherence audit (rules 4, 5, 7, 11 to 15 on B10 and B11) did not run. Stages 10 and 11 have not run. Rule 6 (B09 downstream candidates), rule 9 (stage 13 narrative) and rule 10 (B09b dossier) are outside the task scope. All valuation fields in B12c are blank and pending phase 3.

Inputs read (artifact paths only, no other verifier output, no maker reasoning):
- Rule sources: prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md, prompts/12-verifiers-pipeline.md (Verifier C section).
- runs/keltech-2026-11-15/outputs/reports/01-gate0.md and outputs/blocks/B01-gate0.yaml.
- runs/keltech-2026-11-15/outputs/reports/07-emoat.md and outputs/blocks/B07-emoat.yaml.
- One input file to test a window rule only: runs/keltech-2026-11-15/inputs/shareholding/KELTECH_shareholding_screener_2026-09.csv (E2, 3-year window). No other source document was opened. Raw-number fidelity belongs to Verifier A.

Method. Every score is re-derived from the values B01 and B07 state, with the thresholds in the two rule files. Recomputed values sit beside every FAIL.

Severity convention for Gate 0 and EM (the rule-5 mapping in my section is written for valuation):
- CRITICAL: the misapplication changes the Gate 0 classification, a deal-breaker outcome, the moat class, or the EM classification band.
- MAJOR: a block field value is wrong under the rule as written. The classification survives.
- MINOR: a disclosure, coverage or presentational gap with no block-value change, or a block field that takes one side of an ambiguous rule while both sides are shown.

## 1. GATE 0 (B01) COMPLIANCE TABLE

Source of thresholds: prompts/01-gate-0-pipeline.md. "Stated" = the B01 value. "Re-derived" = my value from B01's stated inputs.

| # | Rule | B01 stated | Re-derived | Result |
|---|---|---|---|---|
| 1 | Opening data line; history min 3, max available (op. rule 6) | "Data available: 10 years (FY17 to FY26)" | 10 years, FY17-FY26 | PASS |
| 2 | ROCE formula, Block A use (formula defs; compute only when source has none) | Sheet has no ROCE row. Proxy CE = equity + reserves + borrowings, all 10 years. Disclosed in data_notes. Exact check FY25 25.9%, FY26 21.1% | All 10 ROCE values recompute from stated EBIT / CE (e.g., FY21 5.35 / 87.66 = 6.10%; FY26 43.03 / 226.19 = 19.02%). The template allows "proxy bases used" in data_notes. A1, A2, A4 bands do not move under the exact FY25/FY26 figures | PASS for Block A (M3 use: row 30) |
| 3 | ROE = PAT / avg NW; closing NW for earliest year, stated | Avg NW; FY17 on closing, stated | All 10 recompute (FY26 28.66 / 138.78 = 20.65%) | PASS |
| 4 | WC days formula; basis stated | Revenue basis, no COGS, stated | FY26 42.2 + 33.8 - 52.3 = 23.8; FY25 42.4 + 31.4 - 67.9 = 5.9 | PASS |
| 5 | FCF = CFO - capex; capex from cash flow statement | Proxy dNet Block + dCWIP + Dep, validated FY25 (11.96 vs 11.94) and FY26 (85.98 vs 85.99). FY17 NOT FOUND | All 9 FCF values recompute (e.g., FY26 48.50 - 85.98 = -37.48) | PASS |
| 6 | CAGR = (End / Start)^(1/years) - 1 | 9-year window | C1 (532.06 / 201.03)^(1/9) - 1 = 11.42%; C2 (28.66 / 5.84)^(1/9) - 1 = 19.33% | PASS |
| 7 | CAGR edge rules (negative endpoint, loss-to-profit note, C4 N/M) | "No loss-to-profit swing; no negative CAGR endpoint" in data_notes | FY17 PAT 5.84 > 0; no loss year in the series; C4 computable | PASS |
| 8 | A1 median ROCE | 18.14% = 3 | (17.26 + 19.02) / 2 = 18.14%; band 15-19.9 = 3 | PASS |
| 9 | A2 minimum ROCE | 6.10% = 0 | FY21 6.10% < 8 = 0 | PASS |
| 10 | A3 median ROE | 14.12% = 2 | (12.86 + 15.37) / 2 = 14.12%; band 12-14.9 = 2 | PASS |
| 11 | A4 ROCE trend | 19.02 vs 17.26 = 5 | latest >= earliest = 5 | PASS |
| 12 | B1 cum CFO / cum PAT | 1.36 = 5 | 160.37 / 117.60 = 1.364; >= 1.00 = 5 | PASS |
| 13 | B2 FCF-positive years | 5 of 9 = 2 | FY18, FY21, FY22, FY23, FY24 positive = 55.6%; band 50-74 = 2 | PASS |
| 14 | B3 cum FCF / cum PAT | -0.05 = 0 | -5.59 / 111.76 = -0.050; negative = 0 | PASS |
| 15 | B4 WC days change | NOT FOUND = 0 | NOT FOUND rule (op. rule 5). The FY25 to FY26 pair (+17.9 days) would also score 0 | PASS |
| 16 | C1 revenue CAGR | 11.4% = 3 | 11.42%; band 10-14.9 = 3 | PASS |
| 17 | C2 PAT CAGR | 19.3% = 4 | 19.33% = 4. Without the ~2.4 Cr post-tax exceptional in FY26 PAT: (26.26 / 5.84)^(1/9) - 1 = 18.2%, still 4 | PASS |
| 18 | C3 positive YoY years | 7 of 9 = 3 | 77.8%; band 75-99 = 3 | PASS |
| 19 | C4 PAT CAGR minus revenue CAGR | +7.9pp = 5 | 19.33 - 11.42 = +7.91pp; >= +3 = 5 | PASS |
| 20 | D1 net debt / EBITDA | 1.31x = 3 | (73.24 - 19.47) / 40.89 = 1.315x; band 1-2x = 3 | PASS |
| 21 | D2 EBIT / interest | 10.29x = 5 | 43.03 / 4.18 = 10.29x; >= 10 = 5 | PASS |
| 22 | D3 debt / equity | 0.48 = 4 | 73.24 / 152.95 = 0.479; band 0.1-0.5 = 4 | PASS |
| 23 | D4 current ratio | 1.12 = 1 | 16,917.33 / 15,162.19 = 1.116; band 1.0-1.19 = 1 | PASS |
| 24 | E1 promoter holding, latest quarter | 54.33% = 4 | band 50-59.9 = 4 | PASS |
| 25 | E2 promoter change over 3 years | Dec 2023 to Sep 2026, 0.00pp = 3 | Sep 2023 is not in the capture. Both bracketing points (Mar 2023 annual, Dec 2023 quarterly) are 54.33%. Band +-1% = 3 | PASS |
| 26 | E3 pledge | NOT FOUND = 0 | NOT FOUND rule = 0 | PASS |
| 27 | E4 contingent liabilities / NW | 26.7% = 1 | 4,077.91 / 15,294.66 = 26.66%; band 15-30 = 1 | PASS |
| 28 | M1 pricing power | 3 | 8.13% to 7.69% = -0.44pp, stable; CAGR 11.4% >= 10 = 3 | PASS |
| 29 | M2 cost advantage | 0 | 7.7% vs peer median 24.2% (27.6, 10.2, 24.2); below = 0. Also below the explosives-only pair | PASS |
| 30 | M3 capital efficiency | 3 (FAT 4.54x, ROCE 19.02% proxy CE, latest year) | **5** (FY26 ROCE by the fixed formula = 43.03 / 203.72 = 21.1% > 20%; FAT 4.54x > 3x) | **FAIL, MAJOR, C-G1** |
| 31 | M4 customer stickiness | 1 | 2 decline years (FY20, FY24), CAGR positive = 1 | PASS |
| 32 | M5 scale and dominance | 1, marked PEER DATA NEEDED | **0** (the rule: a test that needs peer data not provided scores 0 and is marked) | **FAIL, MAJOR, C-G2** |
| 33 | M6 technology / R&D | 0 | 0.25% < 1% = 0 | PASS |
| 34 | M7 regulatory / licence | 0, PEER DATA NEEDED | rule applied as written = 0 | PASS |
| 35 | M8 distribution | 1 | "dealers segment" mentioned, unquantified = 1 | PASS |
| 36 | M9 brand (GM proxy stated) | 0 | 35.2% vs median 42.3%; below = 0 | PASS |
| 37 | M10 switching costs | 1 | overall growth, 2 decline years = 1 | PASS |
| 38 | M11 network effects (>= 6 years) | 0 | latest 3y (532.06 / 562.85)^(1/3) - 1 = -1.86% (B01 shows -1.8%, rounding only) < prior 37.6%; overall 11.4% < 15 = 0 | PASS |
| 39 | M12 negative WC / float | 0 | WC days exist for 2 of 10 years, under the 3-year minimum; NOT FOUND = 0 | PASS |
| 40 | Moat present count (>= 3) and class | 2 (M1, M3), MODERATE | 2 = MODERATE. Unchanged after C-G1 and C-G2 | PASS |
| 41 | Block, core, moat, grand arithmetic | A10 B7 C15 D13 E8 = 53; moat 10; grand 63 | Sums correct on the stated scores. After C-G1 and C-G2: moat 11, grand 64 | PASS (arithmetic) |
| 42 | Data-confidence adjustment | 10 years, full, no downgrade | 10+ years = full; history_downgrade false | PASS |
| 43 | Classification matrix | Core 40-59 = AVERAGE | Core 53 = AVERAGE (moat class not used in this band) | PASS |
| 44 | Deal-breakers 1-9, with driving years named | DB2 fires (not binding); DB5 untestable; rest no | DB1 10 >= 8; DB2 7 < 8, max GOOD, not binding, years named; DB3 18.14% >= 10; DB4 1.36 >= 0.50; DB5 NOT FOUND, cannot cap below AVERAGE; DB6 1.31x and 10.29x; DB7 2 of 9; DB8 no loss FY24-FY26; DB9 10 years | PASS |
| 45 | FLAG-GATE0 when class <= AVERAGE with depressors | Present, depressor years named | Required, present | PASS |
| 46 | Output completeness (dashboard, anchors, moat bars, class box, strongest/weakest, decision line, YAML fields, analyst_note <= 200 words) | All present | Report YAML equals block file. analyst_note about 125 words | PASS |

Gate 0 tally: 46 rules checked, 44 PASS, 2 FAIL (both MAJOR). Classification survives.

## 2. EMERGING MOAT (B07) COMPLIANCE TABLE

Source of rules: prompts/07-emerging-moat-pipeline.md, plus Verifier C rules 3 and 8.

| # | Rule | B07 stated | Re-derived | Result |
|---|---|---|---|---|
| 1 | All 22 categories plus R1 addressed or NO EVIDENCE FOUND (op. rule 5; rule 3) | 22 Section 3 rows; R1 in Section 4; 23 scorecard rows | 23 of 23 addressed. G2 carries negative evidence and scores 0; I2 is reasoned to 0 | PASS |
| 2 | Section 3 summary: columns and Strong/Moderate count | Columns present; "0 of 22" | 0 Strong/Moderate | PASS |
| 3 | 📄 recount performed, exact line, arithmetic | "8 documented items across 6 categories", items listed | A1 2, B1 2, C2 1, E2 1, F2 1, H2 1 = 8 across 6 | PASS |
| 4 | Completionist guard (12 or more active = re-examine) | 7 scored categories | 7 < 12 | PASS |
| 5 | L x I matrix mapping | LM = 1 (A1, B1, F2, H2, R1); LL = 1 (C2, E2); none = 0 | Matches HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1 | PASS |
| 6 | Multiplier A1 vs stated tier | 🔍 0.5 | Moat leg (rarity) 🔍 = 0.5 | PASS |
| 7 | Multiplier B1 | 🔍 0.5 | Moat leg (captive input) 🔍 = 0.5 | PASS |
| 8 | Multiplier C2 | 🎙️ 0.7 | Improving leg (new MDOs) 🎙️ = 0.7 | PASS |
| 9 | Multiplier E2 | 🎙️ 0.7 | Thesis leg 🎙️ = 0.7 | PASS |
| 10 | Multiplier F2 | 🔍 0.5 | On-time/on-budget leg 🔍 = 0.5 | PASS |
| 11 | Multiplier H2 | 📄 1.0 = 1.0 | **🔍 0.5 = 0.5** (B07's own weakest-link rule; exclusivity leg is 🔍) | **FAIL, MAJOR, C-E1** |
| 12 | Multiplier R1 | 🎙️ 0.7 | Approvals relay 🎙️ = 0.7 | PASS |
| 13 | Adjusted total arithmetic | 4.6 | 4.6 on the stated multipliers. **4.1** after C-E1 | PASS (arithmetic) |
| 14 | Bands absolute, no rescale (ruling 20-Aug-2026) | < 12 = NONE | 4.6 and 4.1 both < 12 = NONE | PASS |
| 15 | I1/I2 contribution stated separately | 0.0 | 0.0 | PASS |
| 16 | Rule 8: Cat 21 (I1) present; > 0 only with both legs and a 📄 (b) leg | Present, NO EVIDENCE FOUND, 0 | 0 is correct with neither leg evidenced | PASS |
| 17 | Rule 8: Cat 22 (I2) present; > 0 only with a specific named sacrifice | Present, "nothing must be destroyed", 0 | 0 is correct | PASS |
| 18 | I2 answered "for each moat claimed anywhere in this scan" | Answered for licence and footprint, PSU relationships, TNT | B1, C2, E2, F2, H2 not answered. Score stays 0 | **FAIL, MINOR, C-E2** |
| 19 | Section 1 (1A status labels, 1B, 1C) | Present | Present; NOT FOUND used where data is absent | PASS |
| 20 | Section 2 (2A to 2D); 2C arithmetic shown | Present | Arithmetic recomputes: 190 x 6.89 = 1,309 = 246%; 190 x 3.42 = 650 = 122% | PASS |
| 21 | 2C value carried to capex_embedded_growth_pct | 122 (FY26 spot turnover 3.42x) | **246** on the FY23-FY25 historical turnover 6.89x the rule names (B07 says FY26 is depressed by assets not yet earning). The block comment shows 122-246 | **FAIL, MINOR, C-E3** |
| 22 | F2 cross-references the injected promise-delivery record | B05 record 4 delivered, 6 partial, 0 missed, credibility C | Present | PASS |
| 23 | Section 4 (4A to 4C), R1 | Present | Present | PASS |
| 24 | Optionality register: eligibility, four columns, in block, never scored | 7 report rows, 6 block rows | Eligible rows; four columns; register adds no score (the H2 row feeds C-E1) | PASS |
| 25 | Section 6: 6A, 6B, 6C on the injected B01 values, 6E card | Core 53, moat 10/60, 2 confirmed, AVERAGE | Matches the B01 block | PASS |
| 26 | 6D combined classification; HIGH POTENTIAL and TURNAROUND rows reasoned | AVERAGE; both rows reasoned | prompts/07 names the matrix but does not define its cells. The ">= 25 for HIGH POTENTIAL" threshold B07 cites cannot be checked against the rule source. AVERAGE fits backward AVERAGE with forward NONE | PASS (limited verification) |
| 27 | catalysts_12m evidence_type per the op. rule 2 taxonomy | Catalysts 1 (Q3 FY27 results CWIP check) and 3 (AR FY2026-27 disclosures) tagged "documented" | **Not documented.** A future filing's content is not a 📄 item. The event date is certain; its outcome is not. Recommend "inference" or a separate "checkpoint" label | **FAIL, MINOR, C-E4** |
| 28 | Block schema: all fields; active_categories Strong/Moderate only; analyst_note <= 200 words | All fields; active_categories []; analyst_note about 137 words | Correct | PASS |
| 29 | Report YAML equals block file | Two differences | analyst_note "six Weak rows" (report) vs "six Weak rows plus R1" (block); register 7 rows (report) vs 6 (block, detonator and silo merged, silo window 12 months becomes "6 to 12 months") | **FAIL, MINOR, C-E5** |

EM tally: 29 rules checked, 24 PASS, 5 FAIL (1 MAJOR, 4 MINOR). Classification survives.

## 3. FINDINGS IN DETAIL

### C-G1 (MAJOR). B01 M3 uses the proxy ROCE where the fixed formula is computable
- Rule. prompts/01 FORMULA DEFINITIONS: "ROCE = EBIT ÷ (Total Assets − Current Liabilities) ... fixed, do not substitute alternatives". M3: "FAT >3x AND ROCE >20% = 5 | FAT >2x AND ROCE >15% = 3".
- B01. M3 = 3 on "ROCE 19.02% (not > 20%)", the FY26 proxy (EBIT / (equity + reserves + borrowings)) (01-gate0.md line 121).
- Re-derived. B01 itself computes the fixed formula for FY26: 43.03 / (35,533.75 - 15,162.19 lakh = 203.72 Cr) = 21.1% (01-gate0.md line 39). B01 uses the same AR current-liability total for D4. With FAT 4.54x > 3x and ROCE 21.1% > 20%, M3 = 5.
- B01's data note says "Exact-formula check FY26 21.1%, FY25 25.9% (AR p.97-98); no band moves" (B01 block, data_notes 2). That is wrong for M3. It holds for A1, A2 and A4 only.
- Two readings. (1) One proxy basis for every ROCE use, for comparability: M3 = 3. (2) The fixed formula wherever its inputs exist: M3 = 5. The rule text supports reading 2, because the proxy is only needed where the split is absent (FY17-FY24). A third reading, that M3 reads median ROCE, gives 3 on either basis. B01 chose the latest year, so on B01's own basis M3 = 5. The separating item is an operator ruling on which ROCE year M3 reads.
- Impact. Moat score 10 to 12 (11 net of C-G2). Grand total 63 to 65 (64 net). Moats confirmed stays 2 (M3 is already present at 3). Moat class stays MODERATE. Classification stays AVERAGE.

### C-G2 (MAJOR). B01 M5 scores 1 while marking PEER DATA NEEDED
- Rule. prompts/01 Block F: "If a test needs peer data that is not provided, score 0 and mark 'PEER DATA NEEDED' (never guess peer figures)."
- B01. M5 = 1 on rank 4 of 4 provided names, and marks "Full listed segment not provided: PEER DATA NEEDED for a complete universe" (01-gate0.md line 123; data_notes 9 "M5 universe (scored 1 on the provided set)").
- Re-derived. B01 states the test needs a segment universe it does not have, so the rule gives 0. A "top 5 mcap" test on a set of 4 names passes for any member, so the provided set cannot separate the bands. B01 applies the rule as written to M7 (0, PEER DATA NEEDED) and not to M5. The two tests get opposite treatment on the same gap.
- Two readings. (1) The three-peer set is the segment: M5 = 1, and no PEER DATA NEEDED mark is due. (2) The set is incomplete, as B01 says: M5 = 0. The separating observation is one listed-player census of Indian explosives makers. The same census resolves M7.
- Impact. Moat score -1. M5 cannot reach "present" on any reading, so the moat count, moat class and classification do not change.

### C-E1 (MAJOR). B07 H2 multiplier breaks B07's own weakest-link rule
- Rule. prompts/07 Section 5: "multiply by evidence quality (📄 1.0x, 🎙️ 0.7x, 🔍 0.5x)". Verifier C rule 3: scores must agree with the stated evidence tiers.
- B07 convention, stated in its scorecard: "The multiplier follows the weakest link in the moat claim, not the spending" (07-emoat.md line 127). B07 applies it to A1 (TNT spend 📄, rarity 🔍, so 0.5), B1, F2.
- H2. Section 3 tiers H2 as "📄 existence, 🔍 exclusivity" and says "Without exclusivity the licence is access, not a barrier" (line 98). The scorecard then takes "📄 1.0 (existence of imported technology; exclusivity not shown)" (line 148). The optionality register also lists "Nitration technology as a barrier" as awaiting conversion to 📄 (line 164). A register row must rest on 🎙️/🔍 or score 0.
- Re-derived. H2 = LM 1 x 🔍 0.5 = 0.5. Adjusted total 4.6 - 1.0 + 0.5 = 4.1.
- Two readings. (1) Weakest link, as declared: 4.1. (2) Activity tier, applied to every row the same way (A1, B1, C2, E2, F2, H2 at 1.0; R1 0.7): 6.7. B07's mixed application gives 4.6, which matches neither. Reading 1 governs because B07 declared it.
- Impact. em_score 4.6 to 4.1. Band NONE (< 12) holds on every reading.

### C-E2 (MINOR). I2 cannibalization question not answered for every claimed moat
- Rule. prompts/07 I2: "For each moat claimed anywhere in this scan, answer: what SPECIFIC thing would the best-resourced competitor have to destroy...".
- B07 answers for licence and footprint (R1), PSU relationships and TNT (A1) (line 101). It does not answer for B1, C2, E2, F2, H2. H2 (imported nitration technology) is the most relevant gap.
- Impact. None on the score. The honest answer for each is likely "nothing must be destroyed", so I2 stays 0.

### C-E3 (MINOR). 2C block value takes the spot-year turnover, not the historical one
- Rule. prompts/07 2C: "total capex under execution × historical fixed asset turnover = implied incremental revenue, expressed as % above current revenue".
- B07 computes both: FY23-FY25 average 6.89x = 246%, and FY26 3.42x = 122%. It says FY26 is depressed because "new assets not yet earning" (line 67). The block carries 122 as "the mechanical floor" (line 70; block capex_embedded_growth_pct).
- Re-derived. The rule's historical turnover is the FY23-FY25 average, 246%. On net-block-only turnover (the FAT basis B01 uses), the FY23-FY25 average is 7.22x = 258%. B07 flags every value as not credible (FLAG-CAPEX-GROWTH-UNRELIABLE) and the block comment shows 122-246. So the gap is in which value the single numeric field carries.
- Impact. None on the EM score. Phase 3 note: stage 11 must not read 122 (or 246) as a CAPACITY-basis input. Product, capacity and price for the TNT plant are NOT FOUND.

### C-E4 (MINOR). Two catalysts_12m rows tagged "documented" for future disclosures
- Rule. prompts/07 op. rule 2 taxonomy: 📄 = capex committed, patent filed, contract signed, plant under construction, product launched, regulatory application submitted.
- B07. Catalyst 1, "Q3 FY27 results: CWIP plus advances against ~Rs 114 Cr still to spend", and catalyst 3, "AR FY2026-27 Notes 3, 28, 31 and Form B: TNT cost, product, nitration technology absorbed", carry evidence_type "documented".
- Re-derived. The filing dates are certain. Their content is not documented. Catalyst 1 is a two-way checkpoint (B05 kill line). The "absorbed" leg of catalyst 3 rests on the AR p.29 statement of intent. The block comment says the field "feeds Pillar 3 catalyst proximity". A "documented" tag could over-credit Pillar 3.
- Impact. None in phase 1. Phase 3 check: Pillar 3 must treat catalysts 1 and 3 as checkpoints, not documented value catalysts.

### C-E5 (MINOR). Report YAML and block file differ
- analyst_note: "Score 4.6 comes from six Weak rows;" (07-emoat.md line 259) vs "six Weak rows plus R1;" (B07-emoat.yaml line 42). The block is the correct one: 7 scored rows.
- optionality_register: the report table has 7 rows (lines 161-167). The block has 6, with detonator and silo merged. The silo window "12 months" becomes "6 to 12 months".
- Impact. No score change. The orchestrator reads the block. Synthesis merges the register into monitoring, and the silo window there is the merged one.

## 4. RECOMPUTED VALUES (where this audit differs)

| Field | Stated | Recomputed | Decision effect |
|---|---|---|---|
| B01 moat_score | 10 | 11 (M3 +2, M5 -1) | none |
| B01 grand_total | 63 | 64 | none |
| B01 moats_confirmed | 2 | 2 | none |
| B01 moat_class | MODERATE | MODERATE | none |
| B01 core_score | 53 | 53 | none |
| B01 classification | AVERAGE | AVERAGE | none |
| B07 em_score | 4.6 | 4.1 | none |
| B07 em_classification | NONE | NONE | none |
| B07 capex_embedded_growth_pct | 122 | 246 on the rule's historical turnover (both flagged unreliable) | none in phase 1 |

## 5. OBSERVATIONS (checked, not findings)

Both directions are shown. None changes a score as audited.
- D-block "latest". B01 scores FY26 year-end. The 30.09.2026 balance sheet is later: D/E 0.59 would score 3, not 4 (Core 52, still AVERAGE). E1 says "latest quarter" in words and Block D says only "latest", so the fiscal-year reading is the natural one. B01 shows the sensitivity.
- B2 band edge. FY21 FCF is +0.16 Cr on the capex proxy. The proxy leaves out disposals, so true capex can only be higher. If FY21 turned negative, B2 would fall from 2 to 0 (4 of 9 = 44%). Proxy error in the two checkable years was 0.01 to 0.02 Cr. B01 did not state this edge.
- M7 floor. Every regulated band scores at least 1 (the >10-players band has no margin condition). The explosives licence regime is documented (AR p.39, as cited by B01). B01's 0 follows the PEER DATA NEEDED rule as written. The same census that resolves C-G2 resolves this.
- D1 and D2 choices. Cash and bank only (1.31x) vs with current investments (0.99x, would score 4). D2 at 10.29x includes the Rs 3.18 Cr one-off. Both are disclosed. Gate 0 takes no qualitative view, so the sheet-as-stated reading stands.
- E2 window. 2.75 years (Dec 2023 to Sep 2026), forced by the capture. The bracketing points agree, so the band holds.
- block_b_trend gives two numbers where the template asks for "the one number". No information is lost.
- C2 and E2 on the strict side. C2 says "it is not a forming moat" yet scores 0.7 on the 🎙️ new-MDO claim. E2 says there is "No China+1 language" yet scores 0.7 on in-line export growth and an export-focus claim. Both fit the category lists, so they are judgment, not rule breaks. A strict reading that zeroes both gives 3.2 on B07's multipliers and 2.7 after C-E1. The activity-tier reading gives 6.7. Every reading is NONE.
- evidence_mix. The 🎙️ 5 and 🔍 6 counts are not itemised in the report, so they cannot be re-derived. Only the 📄 recount is mandated, and it reconciles.
- B01 and B07 use different turnover bases (B01 FAT on net block, 4.54x; B07 2C on net block plus CWIP). Each is disclosed.

## 6. NOT RUN IN PHASE 1 (pending)

- Rules 4, 5, 7, 11, 12, 13, 14, 15 (valuation, method plurality, v3.8 exit construction, A19 FV path, expectation ledger, ledger gates, skill-to-source fidelity): pending phase 3. B10 and B11 not produced.
- Rule 6 (B09 downstream candidates): outside this task's scope. The phase-3 pass or the orchestrator owns it.
- Rule 9 (stage 13 narrative) and rule 10 (B09b dossier at /finalize): pending /finalize.
- Phase-3 carry-forward for the valuation audit: (a) em_score 4.1 governs Pillar 3 (C-E1); (b) capex_embedded_growth_pct is not a CAPACITY-basis input (C-E3); (c) catalysts_12m rows 1 and 3 are checkpoints (C-E4); (d) Gate 0 moat score 11 and grand total 64, classification AVERAGE (C-G1, C-G2).

## 7. VERDICT FOR THE ORCHESTRATOR

- 75 rules checked (46 Gate 0, 29 EM). 68 PASS, 7 FAIL. Acceptance rate 90.7% on a denominator of 75. No REWORK trigger: no CRITICAL, rate above 60%.
- Rule 8 REWORK test for stage 7: categories 21 and 22 are present and correctly scored 0. Not triggered.
- No finding changes the Gate 0 classification (AVERAGE), the moat class (MODERATE), or the EM band (NONE).
- No Verifier A finding was seen, read or overridden. Source fidelity stays with Verifier A.

```yaml
stage: B12c
company: "KELTECH"
run_date: "2026-11-15"
model: "claude-opus-5-5"  # must equal .claude/agents frontmatter; the orchestrator compares it
status: complete
scope: "phase-1 (Gate 0 B01 + Emerging Moat B07 only); valuation half pending phase 3"
gate0:
  rules_checked: 46
  rules_passed: 44
  fails:
    - {id: C-G1, rule: "M3 capital efficiency; ROCE fixed formula (TA - CL) where computable", severity: MAJOR, stated: "M3 = 3 on FY26 proxy ROCE 19.02%", recomputed: "M3 = 5 (FY26 ROCE 43.03 / 203.72 = 21.1% > 20%; FAT 4.54x > 3x); B01 data note 'no band moves' is wrong for M3"}
    - {id: C-G2, rule: "M5 scale; PEER DATA NEEDED scores 0", severity: MAJOR, stated: "M5 = 1 while marked PEER DATA NEEDED", recomputed: "M5 = 0; one listed-player census resolves M5 and M7"}
  recomputed: {core_score: 53, moat_score: 11, grand_total: 64, moats_confirmed: 2, moat_class: "MODERATE", classification: "AVERAGE"}
emoat:
  rules_checked: 29
  rules_passed: 24
  fails:
    - {id: C-E1, rule: "evidence multiplier vs stated tier (rule 3); B07 weakest-link convention", severity: MAJOR, stated: "H2 = LM 1 x 📄 1.0 = 1.0", recomputed: "H2 = LM 1 x 🔍 0.5 = 0.5; em_score 4.1"}
    - {id: C-E2, rule: "I2 answered for each moat claimed in the scan", severity: MINOR, stated: "answered for licence/footprint, PSU relationships, TNT", recomputed: "B1, C2, E2, F2, H2 unanswered; I2 stays 0"}
    - {id: C-E3, rule: "2C historical fixed asset turnover carried to capex_embedded_growth_pct", severity: MINOR, stated: "122 (FY26 spot 3.42x)", recomputed: "246 (FY23-FY25 average 6.89x); both flagged unreliable"}
    - {id: C-E4, rule: "catalysts_12m evidence_type per taxonomy", severity: MINOR, stated: "catalysts 1 and 3 'documented'", recomputed: "future filing content is not documented; tag as inference or checkpoint"}
    - {id: C-E5, rule: "report YAML equals block file", severity: MINOR, stated: "analyst_note and optionality_register differ", recomputed: "block is correct on analyst_note; register silo row merged (12 months vs 6 to 12 months)"}
  recomputed: {em_score: 4.1, em_classification: "NONE"}
  rule8_cat21_cat22: {present: true, i1_score: 0, i2_score: 0, rework_stage7: false}
valuation: {rules_checked: 0, fails: []}  # pending phase 3; B10 and B11 not produced
expectation_ledger: {present: null, downside_row: null, all_rows_confirm_by: null, all_rows_metric_threshold: null, prob_in_range: null, decay_status_valid: null, off_ledger_credit: null, residual_pct_cmp: null, residual_starter_cap_ok: null, fails: []}  # rules 13-14; pending phase 3 (B11 not produced); any fail = REWORK stage 11
business_narrative: {checked: false, fails: []}  # rule 9; any fail = REWORK stage 13; pending /finalize (stage 13 not run)
recomputed_destination_pe: ""  # pending phase 3
recomputed_decision: ""        # pending phase 3
findings:
  - {id: C-G1, stage: B01, severity: MAJOR, summary: "M3 should be 5 under the fixed ROCE formula on B01's own latest-year basis (21.1%); moat score +2; class unchanged"}
  - {id: C-G2, stage: B01, severity: MAJOR, summary: "M5 scored 1 on an incomplete peer set while marked PEER DATA NEEDED; rule gives 0; moat score -1; class unchanged"}
  - {id: C-E1, stage: B07, severity: MAJOR, summary: "H2 multiplier 📄 1.0 breaks B07's declared weakest-link rule; 🔍 0.5; em_score 4.6 to 4.1; band NONE unchanged"}
  - {id: C-E2, stage: B07, severity: MINOR, summary: "I2 question unanswered for 5 of 7 scored rows; score unchanged at 0"}
  - {id: C-E3, stage: B07, severity: MINOR, summary: "capex_embedded_growth_pct carries spot-year 122 not historical-turnover 246; both unreliable; phase 3 must not use as CAPACITY basis"}
  - {id: C-E4, stage: B07, severity: MINOR, summary: "catalysts 1 and 3 tagged documented for future disclosures; Pillar 3 must treat as checkpoints"}
  - {id: C-E5, stage: B07, severity: MINOR, summary: "report YAML vs block drift: analyst_note wording and merged optionality row"}
critical_count: 0
major_count: 3
minor_count: 4
acceptance_rate: 90.7             # 68 passed / 75 checked, %
```
