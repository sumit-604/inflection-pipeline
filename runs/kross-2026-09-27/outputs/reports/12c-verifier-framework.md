# STAGE 12, VERIFIER C: FRAMEWORK ADHERENCE. KROSS, run 2026-09-27
Model: claude-opus-5-5 | Scope: PHASE 1 (Gate 0 B01 + Emerging Moat B07 only)
Valuation audit (B10, B11, rules 4-7 and 11-15 of the Verifier C rubric): PENDING PHASE 3. No valuation framework document was read.
Business Understanding Narrative (rule 9) and Halt 1 dossier (rule 10): not in phase-1 scope.

Rule sources: prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md (worktree copies).
Audited artifacts: outputs/reports/01-gate0.md + blocks/B01-gate0.yaml; outputs/reports/07-emoat.md + blocks/B07-emoat.yaml.
Re-derivation data: inputs/screening/screener-Data_Sheet.csv (INR Cr) and the four peer Data_Sheets; inputs/prospectus/2024-09_Kross_Prospectus.txt; inputs/annual-report/Annual_Report_2026.txt; inputs/announcements/2026-02-27_capacity_addition.txt; inputs/presentation/2026-07-25_investor_presentation_Q1FY27.txt.

Verifier C audits rule application. Verifier A owns whether each number exists at its anchor. Where this report quotes a number, it re-derives it from the Data_Sheet to test the rule, not to rule on source fidelity.

---

## PART 1. GATE 0 (B01) COMPLIANCE TABLE

### 1a. Block re-derivation

| # | Rule | B01 value | Verifier re-derivation | Result |
|---|---|---|---|---|
| 1 | Opening "Data available" line | 7 years FY20-FY26 | Present, 01-gate0.md line 17 | PASS |
| 2 | A1 median ROCE | 17.57%, score 3 | EBIT = PBT + Interest per year (screener-Data_Sheet.csv rows 21-22) matches 12.56 / 14.85 / 24.47 / 53.93 / 76.19 / 79.68 / 83.12. Median 17.57% sits in 15-19.9 band = 3 | PASS |
| 3 | A2 minimum ROCE | 10.19%, score 1 | 12.56 / 123.24 = 10.19%, band 8-11.9 = 1 | PASS |
| 4 | A3 median ROE | 16.53%, score 4 | Net worth rows 39-40, PAT row 24: 3.35 / 8.07 / 18.40 / 35.45 / 36.06 / 16.52 / 11.95. Median 16.52% = 4 | PASS |
| 5 | A4 ROCE trend | 15.55 vs 10.19, score 5 | Latest >= earliest = 5. FY24 peak masking disclosed as a flag, correctly not used to rescore | PASS |
| 6 | B1 cum CFO / cum PAT | 0.614x, score 1 | Sum CFO 121.51 (row 57) / sum PAT 197.94 (row 24) = 0.614, band 0.50-0.69 = 1 | PASS |
| 7 | B2 FCF-positive years | 3/7, score 0 | 3/7 = 42.9% = 0. Also 0 on a FY22-FY26-only reading (2/5) | PASS |
| 8 | B3 cum FCF / cum PAT | -0.42x, score 0 | Sum FCF -83.15, negative = 0 under every reading | PASS |
| 9 | B4 WC days change | +42.72, score 0 | FY22 89.03, FY26 131.71 (rows 11, 49, 50 plus payables as cited). Increase > 15 = 0. Earliest-available FY22 basis stated | PASS |
| 10 | C1 revenue CAGR | 27.08%, score 5 | (673.2 / 159.91)^(1/6) - 1 = 27.07% = 5 | PASS |
| 11 | C2 PAT CAGR | 74.57%, score 5 | (55.21 / 1.95)^(1/6) - 1 = 74.57% = 5 | PASS |
| 12 | C3 positive YoY years | 6/6, score 5 | All six YoY positive. FY25 is +0.03% (620.41 vs 620.25, row 11), still positive = 5 | PASS |
| 13 | C4 PAT minus revenue CAGR | +47.49pp, score 5 | = 5 | PASS |
| 14 | D1 ND / EBITDA | 0.341x, score 4 | (53.73 - 23.74) / 88.03 = 0.341 = 4 | PASS |
| 15 | D2 interest cover | 10.30x, score 5 | 83.12 / 8.07 = 10.30 = 5 | PASS |
| 16 | D3 D/E | 0.110x, score 4 | 53.73 / 489.77 = 0.1097, band 0.1-0.5 = 4 | PASS |
| 17 | D4 current ratio | 3.458x, score 5 | 358.725 / 103.75 = 3.458 = 5 | PASS |
| 18 | E1 promoter holding | 68.57%, score 5 | >= 60% = 5 | PASS |
| 19 | E2 promoter change over 3 years | +0.87pp, score 3 | See FINDING G-2. Recomputed 0 | FAIL |
| 20 | E3 pledge | 0%, score 5 | = 5 | PASS |
| 21 | E4 contingent liabilities / NW | 8.11%, score 3 | 39.713 / 489.77 = 8.11%, band 5-15 = 3 | PASS |

### 1b. Moat tests

| # | Test | B01 score | Verifier | Result |
|---|---|---|---|---|
| 22 | M1 pricing power | 5 | EBITDA margin FY20 16.59 / 159.91 = 10.37%, FY26 88.03 / 673.2 = 13.08%, +2.71pp, CAGR 27% = 5 | PASS |
| 23 | M2 cost advantage | 1 | Peer OP recomputed from each peer Data_Sheet rows 11, 19-22: AUTOAXLES 10.89%, HAPPYFORGE 30.44%, RKFORGE 14.79%. Median 14.79%. KROSS -1.71pp inside the +/-2pp band = 1. Reading "below" as below the parity band is the reasonable one | PASS |
| 24 | M3 capital efficiency | 3 | FAT 673.2 / 207.44 = 3.25x, ROCE 15.55% > 15 = 3 | PASS |
| 25 | M4 customer stickiness | 3 | Receivable days not stable; 0 decline years satisfies "max 1" = 3 | PASS |
| 26 | M5 scale and dominance | 1 | See FINDING G-3. Recomputed 0 | FAIL |
| 27 | M6 technology / R&D | 0 | Score correct. Label wrong: see FINDING G-6 | FAIL (label only) |
| 28 | M7 regulatory | 0 | Unregulated = 0 | PASS |
| 29 | M8 distribution | 0 | See FINDING G-5. Recomputed 1 | FAIL |
| 30 | M9 brand | 0 | GM proxy KROSS (673.2 - 364.47) / 673.2 = 45.86%. Peer median 51.51%. Below = 0 | PASS |
| 31 | M10 switching costs | 0 | See FINDING G-4. Recomputed 1 | FAIL |
| 32 | M11 network effects | 0 | See FINDING G-1. Recomputed 0 or 3 | FAIL |
| 33 | M12 negative WC | 0 | WC days > 45 every available year = 0 | PASS |

### 1c. Totals, classification, overrides

| # | Rule | B01 | Verifier | Result |
|---|---|---|---|---|
| 34 | Moat count and class | 3 present, MODERATE | Arithmetic matches B01's own scores. Recomputed class depends on M11 (see G-1) | PASS (arithmetic) |
| 35 | Block, core, grand total arithmetic | 13+1+20+18+16 = 68; 68+13 = 81 | Matches | PASS |
| 36 | Data confidence and history downgrade | 7 years, moderate, no downgrade | 7-9 band, no downgrade | PASS |
| 37 | Classification matrix | Core 68 + MODERATE = GOOD | Correct cell | PASS |
| 38 | Deal-breaker application | #2 fires (Block B = 1), cap GOOD | All nine checked. #4 at 0.614 does not fire. Correct | PASS |
| 39 | CAGR edge rules | No negative endpoint, no loss-to-profit swing, stated | PAT positive FY20-FY26 (row 24). Correct, stated in data_notes | PASS |
| 40 | FLAG-GATE0 condition | Not raised | Classification GOOD > AVERAGE, flag not required | PASS |
| 41 | Missing data = N/A and score 0 (rule 5) | Proxies used for FY20-FY21 CE and capex | See FINDING G-7 | FAIL (no score effect) |
| 42 | Source anchor form (rule 4) | "offset ~N", "p.~57", "p.279 area" | See FINDING G-8 | FAIL (presentational) |

Gate 0 rules checked: 42. Passed: 34. Failed: 8.

### 1d. Gate 0 findings

**G-1 (MAJOR). M11 band ladder not evaluated past the top band.**
B01 (01-gate0.md lines 333-336) fails the top band because the latest 3-year CAGR (11.28%) is below the prior window (45.12%). It then scores 0 at once. The rule has two more bands: "rev CAGR >= 20% AND selling % stable/declining = 3 | growth > 15% but selling % rising = 1" (prompts/01-gate-0-pipeline.md lines 131-133). B01 never tests them. Two readings exist:
- Reading 1, full-period CAGR. Revenue CAGR 27.08% (>= 20%). Selling-and-admin share of sales falls from 8.91% FY20 (14.25 / 159.91) to 2.48% FY26 (16.67 / 673.2) (screener-Data_Sheet.csv rows 11, 17). Score 3. M11 becomes a present moat. Moats confirmed 3 to 4. Moat class MODERATE to STRONG. Matrix cell Core 60-79 + STRONG = GOOD+, which deal-breaker #2 caps at GOOD.
- Reading 2, latest window. CAGR 11.28% (< 20%, < 15%). S&A share rises 1.47% FY23 (7.19 / 488.63) to 2.48% FY26. Score 0.
The observation that separates them is which window the band-2 CAGR refers to when 6 or more years exist. The rule text does not say. B01 must state the reading and its score. The "Selling and admin" line is also a proxy for "selling exp" and must be labelled as such.
Decision effect: classification stays GOOD under both readings because deal-breaker #2 binds. Moat class and moats_confirmed change under Reading 1, and B07 section 6C carries the moat class forward.

**G-2 (MAJOR). E2 uses a listing baseline where the corpus holds the 3-year data.**
B01 (lines 225-232) states that "a true 3-year window does not exist" and measures from the post-Offer holding (67.70%). The prospectus in the corpus gives the pre-Offer holding: promoters and promoter group 54,091,956 shares, 99.99% (2024-09_Kross_Prospectus.txt lines 2020-2023), against 67.70% post-Offer (line 2025). The fall came from the offer for sale and the fresh issue (Sudhir Rai 31,200,140 to 24,200,140 shares; Anita Rai 15,199,816 to 11,783,150, lines 1979-1988). Any 3-year window ending Jun-2026 spans this event. Change 99.99% to 68.57% = -31.42pp. Band "decreased > 3%" = 0.
Recomputed: E2 0, Block E 13, Core 65. Classification stays GOOD (Core 60-79). The post-IPO rebase reading is a legitimate operator question, but the Gate 0 text only permits downstream override of deal-breaker caps, not block scores (prompts/01-gate-0-pipeline.md lines 151-154). The stage should score the literal rule and flag the rebase.

**G-3 (MINOR). M5 awarded on comparison-set size, not segment rank.**
B01 (lines 296-304) scores 1 because KROSS is in the "top 5" of a 5-name set in which it ranks last (1,728.01 Cr, screener-Data_Sheet.csv row 8). The set includes JAMNAAUTO, which B01 excludes from every peer median as reference-only. The two peer uses conflict. The test asks for segment rank. No segment-wide market-cap list is in the provided data, so the rule directs score 0 (lines 99-100). On the provided data KROSS is smallest, which is evidence against the band. Recomputed 0.

**G-4 (MINOR). M10 read literally where M4 was read as a ceiling.**
M4 (line 293) treats "max 1 decline year" as satisfied by 0 decline years. M10 (lines 327-331) treats "overall growth, 2+ decline years = 1" literally, so a company with zero decline years scores below one with two. The two tests use the same ladder shape and need the same reading. A monotone reading gives M10 = 1 (overall growth, receivable days +28 not stable). Recomputed 1.

**G-5 (MINOR). M8 scored 0 where the band for "mentioned unquantified" applies.**
B01 (lines 316-318) limits M8 to the Data_Sheets. The rule scores a mention (prompts/01-gate-0-pipeline.md line 122). The Annual Report, which B01 uses elsewhere, states the company "supplies major OEMs, Tier I suppliers, dealers and fabricators across the country" (Annual_Report_2026.txt line 1837) and "200+ Customers across OEMs, Tier-1 Suppliers, Dealers and Fabricators" (lines 206-208). Reach is not quantified. Recomputed 1.

**G-6 (MINOR). M6 labelled NOT FOUND where the AR discloses NIL.**
Annual_Report_2026.txt line 3530: "Expenditure on R & D NIL". The score 0 stands. The label should read "R&D expenditure NIL (AR, Board's Report annexure)". B07 A4 and F1 repeat "R&D NOT FOUND per B01" and inherit the mislabel.

**G-7 (MINOR). Proxies used where the rule directs N/A.**
FY20-FY21 capital employed uses Total minus "Other Liabilities" (which excludes short-term borrowings), and FY20-FY21 capex uses total investing outflow. Rule 5 directs N/A and score 0 for missing data. B01 disclosed both. The scores do not move under any reading:
- All years on the Data_Sheet basis: ROCE 10.19 / 10.36 / 15.44 / 28.33 / 28.78 / 17.01 / 15.29. Median 15.44 = A1 3; min 10.19 = A2 1; A4 5. Block A 13.
- FY22-FY26 only (FY20-FY21 N/A): median 23.15 = A1 4; min 15.55 = A2 5; A4 15.55 vs 23.15, decline 7.6pp = 0; A3 4. Block A 13.
- B2 and B3 stay 0 under every reading.
The ROCE series in B01 mixes two capital-employed bases (approximate FY20-FY21, classified FY22-FY26). Downstream stages should not read the FY21-to-FY22 step as a real change.

**G-8 (MINOR). Anchor form.**
Rule 4 asks for page and note anchors. B01 uses text-file character offsets ("offset ~9984"), "p.~57" and "p.279 area". Verifier A rules on whether the numbers exist. This finding is only the anchor form.

### 1e. Gate 0 recomputed position

| Item | B01 | Recomputed |
|---|---|---|
| Block E | 16 | 13 (G-2) |
| Core score | 68 | 65 |
| Moat score | 13 | 14 (M11 Reading 2) or 17 (M11 Reading 1). Changes: M5 -1, M8 +1, M10 +1, M11 0 or +3 |
| Grand total | 81 | 79 or 82 |
| Moats confirmed | 3 | 3 or 4 |
| Moat class | MODERATE | MODERATE or STRONG |
| Classification | GOOD | GOOD under every reading (deal-breaker #2 caps the GOOD+ path) |

---

## PART 2. EMERGING MOAT (B07) COMPLIANCE TABLE

| # | Rule | B07 | Verifier | Result |
|---|---|---|---|---|
| 1 | All six sections present | Sections 1-6 plus Optionality Register | Present | PASS |
| 2 | 22 categories + R1 addressed, or NO EVIDENCE FOUND | 23 rows, 07-emoat.md lines 377-399 | All 23 present. Family count A4 B3 C2 D2 E2 F2 G2 H3 I2 = 22, plus R1 | PASS |
| 3 | Raw scores match stated L x I cells | HH 4, MH 3, LL 1, LM 1 | Each raw value matches its cell | PASS |
| 4 | Evidence multipliers applied | 4.0, 2.1, 4.0, 1.0, 0.7, 1.0, 1.0, 1.0 | 4x1.0, 3x0.7, 4x1.0, 1x1.0, 1x0.7, 1x1.0, 1x1.0, 1x1.0 = correct | PASS |
| 5 | Adjusted total and band | 14.8, MODEST (12-24) | Sum = 14.8. Band correct | PASS |
| 6 | Completionist recount performed and accurate | "6 documented items across 4 categories" | See FINDING E-3 | FAIL |
| 7 | Scores consistent with stated evidence tiers (verifier rule 3) | A1 HH at 1.0x | See FINDING E-1 | FAIL |
| 8 | No force-fit: score consistent with own evidence finding (stage rule 5) | B2 1.0, G1 1.0 | See FINDING E-2 | FAIL |
| 9 | Category 21 I1: both legs evidenced, (b) leg 📄 | 0, leg (a) absent, leg (b) moot | Correct application | PASS |
| 10 | Category 22 I2: named, specific sacrifice | 0, test run against B1, "nothing must be destroyed" | Correct application. The test was run, not skipped | PASS |
| 11 | I1/I2 contribution stated separately | 0 stated, line 402 | Present | PASS |
| 12 | 2C arithmetic shown | 167 x 3.27 = 546, 81% | 673 / 205.71 = 3.27; 167 x 3.27 = 546.4; 546.4 / 673 = 81.2%. Caveats stated | PASS |
| 13 | Optionality register: schema and eligibility | 8 rows, four fields each, all 0-scored or 🎙️-only items | Correct | PASS |
| 14 | 6C uses injected B01 values | Core 68, moat 13, MODERATE, 81, GOOD | Matches B01 block | PASS |
| 15 | 6D combined classification with HIGH POTENTIAL and TURNAROUND reasoning | GOOD, both rows reasoned | Reasoning present for both rows. The matrix cells are not defined in prompts/07, so the cell cannot be re-derived from the rule source. Recorded as a rule-source gap, not a stage fault | PASS |
| 16 | catalysts_12m within 12 months (feeds Pillar 3 proximity) | 4 items | See FINDING E-4 | FAIL |
| 17 | Anchor form (slide / page) | "Inv. Pres. line 324", "AR line 1192" | See FINDING E-5 | FAIL (presentational) |
| 18 | Block em_score equals computed total | Block 15, report 14.8 | See FINDING E-6 | FAIL (presentational) |

Emerging Moat rules checked: 18. Passed: 12. Failed: 6.

### 2a. Emerging Moat findings

**E-1 (MAJOR). A1 tier inconsistent with the A3 tier rule the stage applied to itself.**
A3 is scored 🎙️ 0.7x because "capex is 📄 but the efficiency claim itself is 🎙️" (07-emoat.md line 379). A1 is scored HH at 📄 1.0x. The load-bearing A1 attribute is rarity. The rarity evidence is company self-description only: "This plant is a first of its kind in India" (announcements/2026-02-27_capacity_addition.txt line 81) and "Once operational, Kross will become the only Indian automotive component manufacturer with integrated seamless tube manufacturing capability" (Annual_Report_2026.txt lines 505-508, a forward statement about a plant not yet commissioned). B07 itself records that no A1 rubric marker is quantified: "Global manufacturer count ... NOT FOUND ... not a verified global scarcity count" (lines 144-146). The plant is 📄. The rarity is a claim.
Two readings:
- Stage's own A3 logic applied to A1: A1 = 4 x 0.7 = 2.8. Total 13.6. MODEST holds.
- Literal taxonomy (a claim backed by committed capital counts as 📄) applied to both: A1 4.0, A3 3.0. Total 15.7. MODEST holds.
The observation that separates them is an independent count of Indian or global single-piece axle beam extrusion producers. The stage must apply one reading to both categories.
Combined sensitivity with E-2: E-1 (A1 2.8) plus E-2 as recomputed (G1 0, B2 kept at 1) gives 14.8 - 1.2 - 1.0 = 12.6. MODEST holds by 0.6 points. If B2 is also zeroed on the stage's own "NO EVIDENCE of a new lock-in mechanism" text, the total is 11.6, below the 12 floor: NO MEANINGFUL EMERGING MOAT. The MODEST class therefore rests on scoring choices inside a 2.8-point margin. Stage 11 must not treat em_classification MODEST as settled when it sets the Pillar 3 input.
Overlap note: A1 (4.0), B1 (4.0) and A3 (2.1) credit the same two capex projects (axle beam extrusion, seamless tube). B07 says so ("both legs of the same backward-integration engine", line 412). Prompts/07 does not forbid one asset carrying several categories. CLAUDE.md forbids crediting one improvement through two mechanisms. Phase 3 must confirm that Stage 11 does not credit this engine again through a separate catalyst route.

**E-2 (MINOR). B2 and G1 scored above 0 against the stage's own evidence finding.**
B2 text: "Scored as existing-moat baseline, not an emerging category; NO EVIDENCE of a new lock-in mechanism forming" (lines 182-183). Scored LL = 1.0. G1 text: "Not scored as a 'war chest growing while investing' pattern; the opposite is documented" (lines 249-251). Scored LM = 1.0. Stage rule 5: "Never force-fit." One reading keeps B2 at 1 because the B2 rubric names IATF certification as a marker (prompts/07 line 80), and IATF 16949 is held. G1 has no rubric marker met: capex was IPO-funded, not internal; cash fell. Recomputed: B2 1.0 (defensible, but the text must match the score), G1 0. Total 13.8 alone. Class holds alone; see E-1 for the combined effect.

**E-3 (MINOR). Completionist recount is internally inconsistent.**
The recount line states "6 documented items across 4 categories" and then lists six categories (A1, A3, B1, F2, G1, H3) (lines 324-329; B07-emoat.yaml line 22). The 📄-multiplied categories in the scoring table are A1, B1, B2, G1, H3, R1: six, and not the same six. A3 is scored 🎙️ but listed as 📄. B2 and R1 are scored 📄 but not listed. evidence_mix {documented: 6, claim: 5} cannot be reconciled to either list. The guard's purpose (not crediting 🎙️ as 📄) is met: only 3 categories are Strong or Moderate, well under 12. The recount line must be corrected.

**E-4 (MINOR). catalysts_12m carries items outside 12 months.**
The field feeds Pillar 3 catalyst proximity (prompts/07 line 231). Two of four entries sit outside the window: seamless tube commissioning "12-18 months", exports "24 months" (B07-emoat.yaml lines 26-27). Recomputed: 2 in-window catalysts (robotic forging, Q2/Q3 FY27 margin print). Phase 3 must check that Stage 11 does not credit proximity from the two out-of-window items.

**E-5 (MINOR). Anchor form.**
Stage rule 3 asks for (Inv. Pres. slide __) and (AR p.__). B07 often cites extracted-text line numbers ("Inv. Pres. line 324", "line 1192-1194"). Many AR anchors do carry PDF and printed page. Form only; Verifier A owns existence.

**E-6 (MINOR). Block em_score rounded.**
The report total is 14.8. The block carries em_score 15. Downstream reads the block. With the total 2.8 points above a band floor, the block should carry 14.8.

---

## PART 3. CROSS-STAGE OBSERVATIONS (for Verifier A, not scored here)

- B07 line 471 and top_moat_risks cite "CFO/PAT 0.503x, per B01/B03". B01 states cumulative 0.614x. The 0.503x equals FY26 alone (27.75 / 55.21, screener-Data_Sheet.csv rows 24, 57). The attribution to B01 is wrong.
- B07 line 517 cites a ROCE series "28.15% -> 16.74% -> 15.03%" (B03, Note 52). B01 computes 42.17% / 17.57% / 15.55% on a different capital-employed basis. Two ROCE series now travel downstream. Phase 3 should confirm which series FTTCP and Section 1B read.
- B07 2C uses net PP&E 205.71 Cr (AR Note 4). B01 M3 uses Net Block 207.44 Cr (Data_Sheet). No score effect.

---

## PART 4. SUMMARY

| Framework | Rules checked | Passed | Failed | CRITICAL | MAJOR | MINOR |
|---|---|---|---|---|---|---|
| Gate 0 (B01) | 42 | 34 | 8 | 0 | 2 | 6 |
| Emerging Moat (B07) | 18 | 12 | 6 | 0 | 1 | 5 |
| Valuation (B11) | PENDING PHASE 3 | | | | | |
| Total | 60 | 46 | 14 | 0 | 3 | 11 |

Acceptance rate 46 / 60 = 76.7%. The denominator is 4 or more, so the rate applies. It is above the 60% REWORK line. No CRITICAL finding. No REWORK trigger from Verifier C in phase 1.

Decision effect: Gate 0 classification GOOD survives every reading. Gate 0 moat class is MODERATE or STRONG depending on the M11 reading (G-1). Emerging Moat class MODEST survives each finding alone and survives E-1 plus E-2 as recomputed (12.6). It falls to NO MEANINGFUL EMERGING MOAT (11.6) only if B2 is also zeroed on the stage's own text. Flags for phase 3: E-1 (em class fragility), E-4 (catalyst window), the A1/B1/A3 single-engine overlap, and the two ROCE series.

```yaml
stage: B12c
company: "KROSS"
run_date: "2026-09-27"
model: "claude-opus-5-5"
status: complete
scope: "PHASE 1 (Gate 0 B01 + Emerging Moat B07). Valuation audit pending phase 3."
gate0: {rules_checked: 42, fails: ["G-1 M11 band ladder not evaluated (0 or 3)", "G-2 E2 listing baseline used; 3-year window gives 99.99% to 68.57% (score 0)", "G-3 M5 set-size pass (score 0)", "G-4 M10 literal lower band vs M4 ceiling reading (score 1)", "G-5 M8 mention band missed (score 1)", "G-6 M6 labelled NOT FOUND; AR discloses NIL (score unchanged)", "G-7 proxies used where rule directs N/A (no score change)", "G-8 anchor form offsets not pages"]}
emoat: {rules_checked: 18, fails: ["E-1 A1 rarity scored 📄 while the stage's A3 claim rule gives 🎙️ (A1 2.8)", "E-2 B2 and G1 scored against own no-evidence text (G1 0)", "E-3 completionist recount inconsistent", "E-4 catalysts_12m holds 12-18m and 24m items", "E-5 anchor form line numbers not slides/pages", "E-6 block em_score 15 vs computed 14.8"]}
valuation: {status: "PENDING PHASE 3", rules_checked: null, fails: []}
expectation_ledger: {status: "PENDING PHASE 3", present: null, downside_row: null, all_rows_confirm_by: null, all_rows_metric_threshold: null, prob_in_range: null, decay_status_valid: null, off_ledger_credit: null, residual_pct_cmp: null, residual_starter_cap_ok: null, fails: []}
business_understanding_narrative: {status: "NOT IN PHASE 1 SCOPE", present: null, five_questions_answered: null, prose_only: null, section6_candidates_named: null, valuation_vocab_leak: null, fails: []}
recomputed_destination_pe: ""
recomputed_decision: ""
recomputed_gate0: {core_score: 65, moat_score: "14 or 17 (M11 reading)", grand_total: "79 or 82", moats_confirmed: "3 or 4", moat_class: "MODERATE or STRONG", classification: "GOOD (unchanged under every reading; deal-breaker 2 caps GOOD+)"}
recomputed_emoat: {em_score_range: "11.6 to 15.7", em_classification: "MODEST on each finding alone and on E-1 plus E-2 as recomputed (12.6); NONE (11.6) only if B2 is also zeroed"}
findings:
  - {id: G-1, framework: gate0, rule: "M11 band ladder", severity: MAJOR, claimed: "0 (stopped after top band)", recomputed: "3 on full-period CAGR 27.08% with S&A share 8.91% to 2.48%; 0 on latest-window CAGR 11.28% with S&A share 1.47% to 2.48%", effect: "moats 3 to 4, class MODERATE to STRONG under reading 1; classification GOOD holds via deal-breaker 2", anchor: "screener-Data_Sheet.csv rows 11 and 17; prompts/01-gate-0-pipeline.md lines 129-133"}
  - {id: G-2, framework: gate0, rule: "E2 promoter change over 3 years", severity: MAJOR, claimed: "+0.87pp, score 3 (post-Offer baseline)", recomputed: "99.99% pre-Offer to 68.57% Jun-2026 = -31.42pp, score 0; Block E 13, Core 65", effect: "classification GOOD holds", anchor: "2024-09_Kross_Prospectus.txt lines 2020-2025"}
  - {id: G-3, framework: gate0, rule: "M5 scale and dominance", severity: MINOR, claimed: "1 (top 5 of a 5-name set)", recomputed: "0 (smallest of set; segment rank not in provided data)", anchor: "screener-Data_Sheet.csv row 8 and peer sheets row 8"}
  - {id: G-4, framework: gate0, rule: "M10 switching costs", severity: MINOR, claimed: "0", recomputed: "1 (monotone reading consistent with M4)", anchor: "01-gate0.md lines 293 and 327-331"}
  - {id: G-5, framework: gate0, rule: "M8 distribution", severity: MINOR, claimed: "0", recomputed: "1 (dealers and fabricators mentioned, unquantified)", anchor: "Annual_Report_2026.txt lines 206-208 and 1837"}
  - {id: G-6, framework: gate0, rule: "M6 label", severity: MINOR, claimed: "R&D NOT FOUND", recomputed: "R&D expenditure NIL disclosed; score 0 unchanged", anchor: "Annual_Report_2026.txt line 3530"}
  - {id: G-7, framework: gate0, rule: "N/A rule for missing data", severity: MINOR, claimed: "FY20-FY21 CE and capex proxies", recomputed: "Block A 13 and B2/B3 0 under every reading; mixed CE basis noted", anchor: "prompts/01-gate-0-pipeline.md lines 19-22"}
  - {id: G-8, framework: gate0, rule: "anchor form", severity: MINOR, claimed: "offset and approximate page anchors", recomputed: "page and note anchors required", anchor: "prompts/01-gate-0-pipeline.md lines 15-18"}
  - {id: E-1, framework: emoat, rule: "evidence tier consistency", severity: MAJOR, claimed: "A1 HH x 1.0 = 4.0", recomputed: "2.8 under the stage's own A3 rule; total 13.6; 12.6 with E-2; 11.6 (NONE) if B2 also zeroed", anchor: "2026-02-27_capacity_addition.txt line 81; Annual_Report_2026.txt lines 505-508; 07-emoat.md lines 144-146 and 379"}
  - {id: E-2, framework: emoat, rule: "no force-fit", severity: MINOR, claimed: "B2 1.0, G1 1.0", recomputed: "B2 1.0 defensible via IATF marker; G1 0; total 13.8 alone", anchor: "07-emoat.md lines 182-183 and 249-251"}
  - {id: E-3, framework: emoat, rule: "completionist recount", severity: MINOR, claimed: "6 items across 4 categories", recomputed: "6 categories scored at 📄 (A1, B1, B2, G1, H3, R1); list and count disagree", anchor: "07-emoat.md lines 324-329"}
  - {id: E-4, framework: emoat, rule: "catalysts_12m window", severity: MINOR, claimed: "4 catalysts", recomputed: "2 within 12 months", anchor: "B07-emoat.yaml lines 24-27"}
  - {id: E-5, framework: emoat, rule: "anchor form", severity: MINOR, claimed: "extracted-text line anchors", recomputed: "slide and page anchors required", anchor: "prompts/07-emerging-moat-pipeline.md lines 35-36"}
  - {id: E-6, framework: emoat, rule: "block equals report", severity: MINOR, claimed: "em_score 15", recomputed: "14.8", anchor: "07-emoat.md line 400; B07-emoat.yaml line 15"}
critical_count: 0
major_count: 3
minor_count: 11
acceptance_rate: 76.7
```
