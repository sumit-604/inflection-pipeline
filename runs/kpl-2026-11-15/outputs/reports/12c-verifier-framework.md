# VERIFIER C (B12c): FRAMEWORK ADHERENCE. KPL, run 2026-11-15, PHASE-1 SCOPE

Scope. Phase 1 only. This pass audits Gate 0 (B01) and the Emerging Moat scan (B07). The valuation half (B10, B11) is PENDING for phase 3. Stages 10 and 11 have not run. No valuation framework document was loaded.

Inputs read:
- prompts/12-verifiers-pipeline.md (Verifier C section, rubric)
- prompts/01-gate-0-pipeline.md (Gate 0 rules)
- prompts/07-emerging-moat-pipeline.md (22-category scan rules)
- runs/kpl-2026-11-15/outputs/reports/01-gate0.md and outputs/blocks/B01-gate0.yaml
- runs/kpl-2026-11-15/outputs/reports/07-emoat.md and outputs/blocks/B07-emoat.yaml

Method. I re-derived every score from the inputs each report states, under the thresholds as written. I did not open the corpus. Whether a number exists in its source is Verifier A's question. Where a check turns on a source number, I name it as a pointer for Verifier A and do not rule on it.

## Summary

- 80 rules checked. 69 PASS. 11 FAIL: 0 CRITICAL, 1 MAJOR, 10 MINOR. Acceptance rate 86% (69 of 80).
- Gate 0: 53 checks, 5 fails. I concur with GOOD on the most evidenced reading. Core 61 sits 1 point above the 60 line. Three open routes each take it to AVERAGE (table 1B). The block names none of them except through its "1 point" note.
- Emerging Moat: 27 checks, 6 fails. I concur with NONE. Two corrections lift the score from 10.3 to 11.6-11.9. NONE holds by 0.1-0.4 points. An unstated mixed-tier multiplier rule decides NONE against MODEST (table 2B).
- No REWORK trigger from this verifier. The acceptance rate clears 60%. Verifier C CRITICALs do not trigger REWORK, and there are none.

---

## PART 1. GATE 0 (B01) COMPLIANCE

All inputs below are the values B01 states (report table and block). "Re-derived" is my computation from those values.

### 1A. Rule-by-rule table

| # | Rule (prompts/01) | Stated input (B01) | B01 score | Re-derived | Verdict |
|---|---|---|---|---|---|
| G01 | Opening line; data confidence tier | 10 years FY17-FY26 | full | 10+ yrs = full | PASS |
| G02 | History downgrade (3-4 yrs only) | 10 years | false | false | PASS |
| G03 | ROCE formula fixed: EBIT / (TA - CL); use source ROCE if given; "do not substitute alternatives" | ROCE on (NW + borrowings) for all 10 years; TA - CL computed for FY25 23.0% and FY26 27.4% only | proxy used for A1, A2, A4, M3 | see finding C-G03 | FAIL (MAJOR) |
| G04 | ROE = PAT / avg NW; closing NW for earliest year, stated | FY26 67.35 / ((331.60 + 264.05) / 2) | 22.6% | 22.6%; FY17 closing basis stated | PASS |
| G05 | WC days formula; basis stated | revenue basis stated | n/a | FY26 (280.05 + 78.25 - 101.69) / 503.08 x 365 = 186.2 | PASS |
| G06 | FCF = CFO - capex (PPE + intangibles), excluding acquisitions | CFO + CFI proxy; AR capex cross-check FY25, FY26 only | proxy used for B2, B3 | see finding C-G06 | FAIL (MINOR) |
| G07 | CAGR = (End / Start)^(1/years) - 1 | 9 intervals FY17-FY26 | applied | applied | PASS |
| G08 | CAGR edge rules (negative endpoint, loss-to-profit note, C4 N/M) | PAT positive every year (implied by positive ROE every year) | none triggered | none triggered | PASS |
| G09 | A1 median ROCE | 10 proxy values; 5th and 6th = 17.02, 17.00 | 3 | 17.0% in 15-19.9 = 3 | PASS |
| G10 | A2 minimum ROCE | 11.1% FY23 | 1 | 8-11.9 = 1 | PASS |
| G11 | A3 median ROE | sorted 10.2, 11.2, 13.1, 16.3, 16.4, 20.0, 22.5, 22.6, 28.3, 99.0 | 4 | (16.4 + 20.0) / 2 = 18.2% = 4 | PASS |
| G12 | A4 ROCE trend | 21.7% vs 17.0% | 5 | latest >= earliest = 5 | PASS |
| G13 | Block A sum | 3 + 1 + 4 + 5 | 13 | 13 | PASS |
| G14 | B1 cumulative CFO / PAT | 10 CFO rows re-added = 264.92; PAT 309.29 | 4 | 0.857 in 0.85-0.99 = 4 | PASS |
| G15 | B2 FCF-positive years | 4 of 10 (FY19, FY21, FY24, FY25) | 0 | 40% < 50 = 0 | PASS |
| G16 | B3 cumulative FCF / PAT | 10 FCF rows re-added = -2.52 | 0 | negative = 0 | PASS |
| G17 | B4 WC days change | FY17 bounded 37.9 to 135.4 days; FY26 186.2 days | 0 | increase >= 50.8 days in every case = 0. The bound settles the band without the missing number | PASS |
| G18 | Block B sum | 4 + 0 + 0 + 0 | 4 | 4 | PASS |
| G19 | C1 revenue CAGR | 98.30 to 503.08, 9 years | 4 | 19.89% in 15-19.9 = 4 | PASS |
| G20 | C2 PAT CAGR | 3.36 to 67.35 | 5 | 39.5% = 5 | PASS |
| G21 | C3 positive revenue years | declines FY20, FY23 | 3 | 7 of 9 = 77.8% = 3 | PASS |
| G22 | C4 PAT CAGR minus revenue CAGR | 39.5 - 19.9 | 5 | +19.6pp = 5 | PASS |
| G23 | Block C sum | 4 + 5 + 3 + 5 | 17 | 17 | PASS |
| G24 | D1 net debt / EBITDA | 126.87 / 118.24 | 3 | 1.07x in 1-2x = 3 | PASS |
| G25 | D2 interest coverage | 100.46 / 10.97 | 4 | 9.16x in 5-9.9 = 4 | PASS |
| G26 | D3 debt / equity | 130.46 / 329.92 | 4 | 0.395 in 0.1-0.5 = 4 | PASS |
| G27 | D4 current ratio | 405.68 / 225.52 | 4 | 1.80 in 1.5-1.99 = 4 | PASS |
| G28 | Block D sum | 3 + 4 + 4 + 4 | 15 | 15 | PASS |
| G29 | E1 promoter holding | 54.86% | 4 | 50-59.9 = 4 | PASS |
| G30 | E2 3-year change | NOT FOUND | 0 | rule 5: NOT FOUND = 0 | PASS |
| G31 | E3 pledge | 0% | 5 | 0% = 5 | PASS |
| G32 | E4 contingent liabilities / NW | 36.98 / 329.92 | 3 | 11.2% in 5-15 = 3 on the stated total (numerator gap: see C-G53) | PASS |
| G33 | Block E sum | 4 + 0 + 5 + 3 | 12 | 12 | PASS |
| G34 | Core score | 13 + 4 + 17 + 15 + 12 | 61 | 61 | PASS |
| G35 | M1 pricing power | margin 9.1% to 23.5% (+14.4pp); CAGR 19.9% | 5 | >= 2pp AND >= 10% = 5 | PASS |
| G36 | M2 cost vs peer median | 23.5% vs 26.6% | 0 | below = 0 | PASS |
| G37 | M3 capital efficiency | FAT 3.23x; ROCE 21.7% (27.4% on formula basis) | 5 | FAT > 3x AND ROCE > 20% = 5 on either ROCE basis | PASS |
| G38 | M4 stickiness | 2 decline years, CAGR positive | 1 | = 1 | PASS |
| G39 | M5 scale and dominance | 4-name set; "segment-wide rank not evidenced" (B01 data_notes) | 1 | PEER DATA NEEDED = 0 | FAIL (MINOR) |
| G40 | M6 R&D | R&D / revenue NOT FOUND | 0 | rule 5 = 0 | PASS |
| G41 | M7 regulatory | player count NOT FOUND | 0 | rule 5 = 0. Margin moved +14.4pp, so the 5 and 3 bands are closed on any count; maximum is 1 | PASS |
| G42 | M8 distribution | "70+ countries" quantified; growth not evidenced | 1 | no band for "quantified, not growing"; the highest band the evidence clears is 1 | PASS |
| G43 | M9 brand (GM proxy, stated) | 48.6% vs 60.2% | 0 | at/below = 0 | PASS |
| G44 | M10 switching costs | overall growth, 2 decline years | 1 | = 1 | PASS |
| G45 | M11 network effects | 10 >= 6 years; 26.1% (FY23-26) > 21.7% (FY20-23); selling 12.3% to 8.2% | 5 | = 5. Rule 2 bars a qualitative override; B01 discloses the mechanical fit | PASS |
| G46 | M12 negative WC / float | WC positive in >= 9 of 10 years; FY26 186.2 days | 0 | 5 and 3 bands closed. 0 against 1 turns on FY17-FY24 payables NOT FOUND, so rule 5 gives 0. B01's stated reason ("positive") does not match the 0-band text (">45"); score stands | PASS |
| G47 | Moat sum and grand total | 5+0+5+1+1+0+0+1+0+1+5+0 | 19; 80 | 19; 61 + 19 = 80 | PASS |
| G48 | Moats present (>= 3) and class | M1, M3, M11 | 3, MODERATE | 3 in 2-3 = MODERATE | PASS |
| G49 | Classification matrix | Core 61, MODERATE | GOOD | Core 60-79 + not STRONG/FORTRESS = GOOD | PASS |
| G50 | Deal-breakers 1-9; driving years named | A 13; B 4; median ROCE 17.0%; CFO/PAT 0.857; pledge 0%; 1.07x and 9.16x; 2 of 9 declines; PAT positive FY24-FY26; 10 years | #2 only, max GOOD; years named | #2 only; cap equals the matrix result | PASS |
| G51 | FLAG-GATE0 (only if <= AVERAGE) | GOOD | flags: [] | not due | PASS |
| G52 | "End with exactly this fenced YAML block" | report fenced block vs outputs/blocks/B01-gate0.yaml | two versions | see finding C-G52 | FAIL (MINOR) |
| G53 | NOT FOUND and unresolved inputs carried to the block (input_gaps, data_notes) | E4 numerator composition stated in report body only (01-gate0.md, E4 line) | absent from block | see finding C-G53 | FAIL (MINOR) |

Gate 0 tally: 53 checked, 48 PASS, 5 FAIL (1 MAJOR, 4 MINOR).

### 1B. Classification sensitivity (core 61, line at 60)

| Open item | Reading | Core | Class | Separating observation |
|---|---|---|---|---|
| As stated by B01 | n/a | 61 | GOOD | n/a |
| ROCE basis (C-G03) | Mixed basis: FY25 23.0%, FY26 27.4% replace the proxy, other years proxy. Median 18.5%, min 11.1%, latest 27.4% vs earliest 17.0%. A1 3, A2 1, A4 5 | 61 | GOOD | Full TA - CL series FY17-FY24: NOT FOUND in B01 |
| ROCE basis (C-G03) | Rule 5 strict: TA - CL NOT FOUND for 8 of 10 years, fewer than the 3-year minimum. A1 0, A2 0, A4 0; Block A 4 | 52 | AVERAGE (FLAG-GATE0 due) | Whether the corpus holds TA and CL, or screener's own ROCE, for >= 3 years. B01 cites the AR 2025 at E2, so FY24 comparatives should exist |
| E4 numerator (C-G53) | GST items (IGST refund Rs 6.30 Cr, ITC show cause Rs 30.26 Cr) sit OUTSIDE Rs 36.98 Cr: 73.54 / 329.92 = 22.3%, E4 = 1 | 59 | AVERAGE (FLAG-GATE0 due) | Note 34 table composition (AR p.226-227). Pointer for Verifier A: 6.30 + 30.26 = 36.56, Rs 0.42 Cr short of 36.98, which fits the "small DRC-07 orders" sitting INSIDE the total. The source read decides |
| B1 knife-edge (number, Verifier A) | Cumulative CFO falls by Rs 2.02 Cr or more (264.92 - 0.85 x 309.29): B1 4 to 2 | 59 | AVERAGE | Ten-year CFO series against source. B01's own AR figure for FY26 (Rs 16.59 Cr against screener 17.06) gives 0.855, still band 4 |
| E2 (rule-compliant 0) | Resolved at +/-1pp | 64 | GOOD | Sep 2023 shareholding pattern |
| M5 (C-G39) | 1 to 0 | 61 (moat 18, total 79) | GOOD | n/a; moat count unchanged |
| FCF basis (C-G06) | CFO - capex for FY17-FY24 | 61 or higher | GOOD on any value | Block B changes keep core inside 60-79; GOOD holds |

Reading. The most evidenced path is GOOD. The two formula-basis ROCE years both sit above the proxy, and the E4 arithmetic points to the GST items sitting inside the total. Three downside routes reach AVERAGE: the ROCE strict reading, the E4 composition, and the B1 knife-edge. B01 states only the upside sensitivity ("E2 resolved at +/-1pp would add 3"). The separating observations above are Halt 1 open items.

### 1C. Gate 0 findings

C-G03 (MAJOR). ROCE formula substitution. prompts/01-gate-0-pipeline.md fixes ROCE as EBIT / (TA - CL) and says "do not substitute alternatives". B01 scores A1, A2 and A4 on EBIT / (NW + borrowings) for all ten years. B01 calls the proxy conservative. That holds only where current borrowings exceed other non-current liabilities. B01 shows it for FY25 and FY26 (17.0% against 23.0%; 21.7% against 27.4%), not for FY17-FY24. B01 states the gap against the Data Sheet ("NOT FOUND in Data Sheet"), not against the corpus. The rule-compliant fills are the screener ROCE series, the formula on corpus years, or NOT FOUND scored 0. The first two keep GOOD. The third gives core 52, AVERAGE. The decision survives on the most evidenced reading, so the grade is MAJOR, not CRITICAL. If the corpus holds no TA and CL for three or more years, this finding becomes decision-changing.

C-G06 (MINOR). FCF formula substitution. The rule is CFO minus capex, excluding acquisitions. B01 uses CFO + CFI for FY17-FY24. CFI also carries investment purchases and sales. The FY25 and FY26 cross-checks keep the sign (FY26 -32.35 against proxy -17.85; FY25 +27.72 against +24.20), so B2 holds in those years. B2 and B3 for FY17-FY24 are undetermined. Classification is unaffected on any value.

C-G39 (MINOR). M5 scored 1 on "top 5 mcap" from a 4-name set. B01's own data note says the segment-wide rank is not evidenced. The rule says a test that needs peer data not provided scores 0, marked PEER DATA NEEDED. Recomputed: M5 0, moat score 18, grand total 79, moats present 3, MODERATE unchanged.

C-G52 (MINOR). Two versions of the B01 block. The fenced block in 01-gate0.md shortens input_gaps and deal_breakers. Its data_notes is the pointer "Full notes in outputs/blocks/B01-gate0.yaml" in place of ten notes, and its analyst_note is shorter. The scored fields match. A reader of the report copy loses the proxy and peer-data notes.

C-G53 (MINOR). The E4 numerator gap sits in the report body only. B01's E4 line says it is not stated whether the GST demands sit inside the Rs 36.98 Cr. The block's input_gaps and data_notes omit it. With core 1 point over the line, a stage that reads only the block cannot see that E4 can take the class to AVERAGE.

---

## PART 2. EMERGING MOAT (B07) COMPLIANCE

### 2A. Rule-by-rule table

| # | Rule (prompts/07 and Verifier C rules 3, 8) | B07 | Re-derived / check | Verdict |
|---|---|---|---|---|
| E01 | All six sections, one response | Sections 1-6 plus Optionality Register | present | PASS |
| E02 | Load-bearing facts checked first (CLAUDE.md spear rule) | 3 facts checked before Section 1 | present | PASS |
| E03 | Evidence tag and source anchor on every item (rules 2, 3) | see finding C-E03 | gaps on non-score items and one recount item | FAIL (MINOR) |
| E04 | Section 1: 1A status per item, 1B, 1C | 10 items with status; 1B five directions; 1C table | present; 1C closure check made | PASS |
| E05 | Section 2: 2A-2D; 2C arithmetic shown | 115 x 3.35 = 385 = 76.6%; 115 x 2.56 = 294 = 58.4% | 385.25 / 503.08 = 76.6%; FAT 2.09, 2.21, 2.57, 3.35, mean 2.56. Note: the Unit 5 biologics row (Rs 195+ Cr) is not named in the exclusion list. B01 FAT 3.23x (155.57 base) against B07 3.35x (150 base) is a cross-stage basis difference for Verifier A | PASS |
| E06 | All 23 rows addressed or NO EVIDENCE FOUND | A1-H3, I1, I2, R1 | 23 of 23 | PASS |
| E07 | I1 (Cat 21): both legs; (b) leg >= 1 📄 for >0 | 0; neither leg evidenced | 0 correct | PASS |
| E08 | I2 (Cat 22): named specific sacrifice for >0 | 0; "nothing must be destroyed" for each claimed moat | 0 correct | PASS |
| E09 | Raw score from L x I matrix | A4 MM 2, B2 HL 2, E1 MM 2, F1 ML 1, F2 ML 1, G1 LL 1, H2 MM 2, R1 MM 2 | all 8 map correctly | PASS |
| E10 | Multiplier matches the stated evidence tier; no 🎙️-only row scored as 📄 (Verifier C rule 3) | No 🎙️-only row at 1.0. R1 stated type "📄 (2) and 🎙️", scored 0.7 | see finding C-E10. Recomputed R1 2.0, total 10.9 | FAIL (MINOR) |
| E11 | Like evidence scored alike (same bar, bull and bear) | G1 1.0 with core tests failed; G2 0 with two listed indicators present | see finding C-E11. Recomputed total 11.0-11.3 (G2 credited) or 9.3 (G1 zeroed) | FAIL (MINOR) |
| E12 | Strength labels consistent with scores | A4 Moderate at 1.4; E1, H2, R1 Weak at 1.4 | see finding C-E12 | FAIL (MINOR) |
| E13 | Adjusted total | 10.3 | 1.4 + 2.0 + 1.4 + 0.7 + 1.0 + 1.0 + 1.4 + 1.4 = 10.3 | PASS |
| E14 | Band classification; UA qualifier statement | NONE; "EM >= 25" not met | < 12 = NONE | PASS |
| E15 | I1/I2 contribution stated separately | 0.0 of 10.3 | present | PASS |
| E16 | Completionist guard; exact recount line | "📄 recount performed: 10 documented items across 7 categories" | items re-added 2 + 1 + 2 + 2 + 1 + 1 + 1 = 10 across B2, E1, A4, R1, G1, F1, F2; 8 categories active, under 12 | PASS |
| E17 | Section 3 summary table; Strong/Moderate count | 23 rows; 2 Moderate, 0 Strong | consistent with labels as given | PASS |
| E18 | Section 4 (4A, 4B, 4C) | present; no policy benefit credited | present | PASS |
| E19 | Optionality Register: table, block field, "watched, never scored" | 12 rows in table and block | see finding C-E19 | FAIL (MINOR) |
| E20 | One improvement, one mechanism | "plant-approval stream is scored once, in B2"; R1 pending only; export growth routed away from E2 | holds for plant approvals. Product registrations appear in A4 (filings), the B2 table (Mexico, Colombia) and R1 4A (EU MAs, COFEPRIS). R1's basis rests on Pembrolizumab plus claims, so the number carries no double count | PASS |
| E21 | F2 cross-references the B05 promise-delivery record | 9 delivered, 7 partial, 5 missed of 21 | present | PASS |
| E22 | 6A timeline; 6B risks with early warnings | present | present | PASS |
| E23 | 6C uses the injected B01 block | 61; 19 MODERATE; 3; GOOD | matches B01 block | PASS |
| E24 | 6D combined class; HIGH POTENTIAL and TURNAROUND reasoning | GOOD; both explained as not applicable; Reading A / Reading B with one separating observation | internally consistent. The standard matrix cells are not in my rubric, so the cell itself is not re-derived | PASS |
| E25 | 6E card: evolution map, 12-month catalysts, biggest risk | present; catalysts point to the YAML list (9 items) | present | PASS |
| E26 | YAML fields and allowed values; report copy equals block file | em_classification "NONE"; active_categories Strong/Moderate only; capex_embedded_growth_pct 77 from 2C; 12 register rows; copies identical | conforms | PASS |
| E27 | evidence_mix item counts | {documented: 10, claim: 9, inference: 3} | see finding C-E27 | FAIL (MINOR) |

Emerging Moat tally: 27 checked, 21 PASS, 6 FAIL (all MINOR). Verifier C rule 8: categories 21 and 22 are present and correctly scored 0. No REWORK for stage 7.

### 2B. Band sensitivity (score 10.3, line at 12)

| Reading | Total | Class |
|---|---|---|
| As stated by B07 | 10.3 | NONE |
| C-E10: R1 at 1.0 | 10.9 | NONE |
| C-E10 + C-E11: R1 at 1.0 and G2 at L x L = 1 (0.7 or 1.0) | 11.6-11.9 | NONE |
| C-E11 the other way: G1 to 0 | 9.3 | NONE |
| Every row carrying any 📄 item at 1.0 (A4, E1, F1, R1) | 12.4 | MODEST |
| That reading plus G2 credited | 13.1-13.4 | MODEST |
| Strict "registered = never scored": E1 and H2 to 0 | 7.5 | NONE |

Reading. My recomputation is 11.6-11.9, NONE. The prompt states no rule for a row that carries mixed tiers. B07 applies the tier of the evidence each L x I rests on: B2 at 1.0 on certificates, A4, F1 and E1 at 0.7. That reading is defensible, and I do not count A4, F1 or E1 as fails. The alternative reading (any 📄 item lifts the row to 1.0) crosses the line at 12.4. An operator ruling on mixed-tier multipliers settles NONE against MODEST. The UA qualifier (EM >= 25) fails on every reading.

### 2C. Emerging Moat findings

C-E03 (MINOR). Anchor and tag gaps. "BE spend capitalised Rs 4.34 Cr (433.89 lakh) FY26", a 📄 item inside the recount of 10, carries "AR via B03" with no AR page. The Unit 6 CWIP figure (1,700.62 lakh) also carries "via B03". Section 2D items (Russian GMP audit, Eurasian audit) carry no evidence tag. No score changes. The recount could fall to 9 if the B03 route does not resolve to an AR page.

C-E10 (MINOR). R1 multiplier against its stated tier. B07 types R1 as "📄 (2) and 🎙️". Its two 📄 items are the EPO pre-clinical submission to RCGM (AR p.48) and the Pembrolizumab CDSCO pilot batch nod (BSE 24 Jul 2026). The prompt's taxonomy names "regulatory application submitted" as 📄, and R1 is the regulatory-approvals row. B07 scores R1 at 0.7 and gives no reason. B2, also mixed, scores 1.0. Recomputed: R1 2 x 1.0 = 2.0, total 10.9, NONE holds. The tier mismatch runs toward a lower score. The bar is symmetric, so it is still a finding.

C-E11 (MINOR). G1 and G2 scored to different bars. G1 scores L x L = 1 at 1.0 on one listed indicator (ICRA upgrade). B07 also says "the category's core tests (net cash growing, internally funded capex) fail". G2 scores 0 under "NO EVIDENCE FOUND of a real trajectory". Two listed G2 indicators are present: inventory turns improving (Rs 78 Cr to Rs 74 Cr; 111 to 77 days, Q2 deck p.8-9) and WC days declining (debtor days 203 to 178). B07 itself calls the inventory move "a genuine improvement". The rupee rise in receivables argues for a low score, not for "NO EVIDENCE". Same bar: G2 at L x L = 1 x 0.7 (deck) or 1.0 (filed results) = 0.7-1.0, total 11.0-11.3. Or G1 at 0, total 9.3. NONE holds either way.

C-E12 (MINOR). Strength labels. A4, E1, H2 and R1 all carry raw 2 and adjusted 1.4. A4 is labelled Moderate. E1, H2 and R1 are labelled Weak. active_categories therefore lists A4 and B2 only. A consistent label gives either B2 alone (A4 Weak) or five rows (all four Moderate). The completionist guard is not triggered on either version.

C-E19 (MINOR). Register and score described inconsistently. B07 says pipeline items "sit in the Optionality Register and [are] not scored" (report line 5) and are "in the register, not the score" (analyst_note). The scoreboard credits 5.6 of 10.3 to rows whose items also sit in the register: A4 (BE library) 1.4, R1 (EPO, Pembrolizumab, Unit 6 licence, EU MAs) 1.4, E1 (first-generic positions) 1.4, H2 (Algeria JV) 1.4. The prompt allows a row to be scored at 0.7 for 🎙️ evidence and to sit in the register as well. The register itself carries no score. So the score stands and the statement is wrong. Strict reading ("registered options are watched, never scored" applied to 🎙️-only rows): E1 and H2 to 0, total 7.5, NONE holds. Forward flag F-1 below.

C-E27 (MINOR). evidence_mix does not reconcile. "documented: 10" matches the recount. "claim: 9" and "inference: 3" match no counting basis visible in the report. Section 3 alone tags 14 items 🎙️ (A1 1, A2 1, A4 4, B2 2, C1 1, E1 2, H2 3). Sections 1-5 tag at least 8 items 🔍. The block does not state the counting basis.

---

## PART 3. VERIFIER C RULES NOT IN PHASE-1 SCOPE (PENDING)

| Rule | Subject | Status |
|---|---|---|
| 4 | Valuation (B11): growth symmetry, pillar mechanics | PENDING phase 3 |
| 6 | B09 downstream candidates; stage 11 catalyst citations | PENDING phase 3 (B09 not in phase-1 inputs) |
| 7 | Method plurality (B11) | PENDING phase 3 |
| 9 | Business Understanding Narrative (stage 13) | PENDING /finalize |
| 10 | Halt 1 dossier B09b | PENDING /finalize (phase-1 structural check sits in run-pipeline step 6b) |
| 11-14 | Role 1 exit construction, A19 FV path, Expectation Ledger, ledger gates | PENDING phase 3 |
| 15 | Skill-to-source fidelity (section-1b) | PENDING phase 3 |

---

## PART 4. FORWARD FLAGS (for the orchestrator and the phase-3 audit)

- F-1 (stage 11, Pillar 3). em_score 10.3 already holds R1, A4, E1 and H2 credit for the Unit 6 licence, EPO, Pembrolizumab, BE dossiers and EU MAs. The same items sit in catalysts_12m. Crediting them again as catalyst proximity would credit one improvement through two mechanisms. The phase-3 audit will check this.
- F-2 (Halt 1). The Gate 0 class rests on core 61. Three downside routes reach AVERAGE: the ROCE rule-5 reading (52), the E4 composition (59), and the B1 knife-edge (59). The separating observations are in table 1B. Each is a source read, not a judgment.
- F-3 (operator ruling candidate). The prompts/07 Section 5 multiplier has no rule for a row that carries mixed tiers. On this name the choice decides NONE (B07 reading, 10.3; my recompute 11.6-11.9) against MODEST (12.4-13.4).
- F-4 (Verifier A pointers, numbers only). B1 headroom is Rs 2.02 Cr of cumulative CFO. C1 sits 0.11pp under the 20% line and D1 0.07x over the 1.0x line, both upside. The E4 Note 34 sum is 6.30 + 30.26 = 36.56 against 36.98. FAT differs between B01 (3.23x on 155.57) and B07 (3.35x on 150).

---

```yaml
stage: B12c
company: "KPL"
run_date: "2026-11-15"
model: "claude-opus-5-5"  # must equal .claude/agents frontmatter; the orchestrator compares it
status: complete
scope: "phase-1: Gate 0 (B01) + Emerging Moat (B07). Valuation half (B10, B11) pending phase 3; no valuation framework doc loaded."
gate0:
  rules_checked: 53
  fails:
    - "G03 MAJOR: ROCE computed on (NW + borrowings) for all 10 years, not the fixed EBIT / (TA - CL). Formula basis shown only FY25 23.0% and FY26 27.4% (proxy 17.0%, 21.7%). Mixed basis keeps Block A 13, core 61, GOOD; rule-5 NOT FOUND reading gives Block A 4, core 52, AVERAGE. Separating observation: TA and CL (or screener ROCE) for >= 3 years in the corpus."
    - "G06 MINOR: FCF on CFO + CFI proxy FY17-FY24, not CFO - capex excluding acquisitions. FY25/FY26 cross-checks keep sign. B2/B3 for FY17-FY24 undetermined; GOOD holds on any Block B value."
    - "G39 MINOR: M5 scored 1 on a 4-name peer set with segment rank not evidenced; rule gives PEER DATA NEEDED = 0. Recomputed moat 18, grand total 79, moats present 3, MODERATE unchanged."
    - "G52 MINOR: fenced YAML in 01-gate0.md differs from outputs/blocks/B01-gate0.yaml (input_gaps, deal_breakers, data_notes pointer, analyst_note). Scored fields match."
    - "G53 MINOR: E4 numerator gap (Note 34 GST items Rs 6.30 Cr + Rs 30.26 Cr inside or outside Rs 36.98 Cr) absent from block input_gaps/data_notes. If outside: E4 = 1, Block E 10, core 59, AVERAGE, FLAG-GATE0 due."
emoat:
  rules_checked: 27
  fails:
    - "E03 MINOR: BE capitalisation Rs 4.34 Cr (a recount item) anchored 'AR via B03' with no AR page; Unit 6 CWIP 'via B03'; Section 2D items untagged. No score change."
    - "E10 MINOR: R1 typed '📄 (2) and 🎙️' (RCGM submission AR p.48; CDSCO nod BSE 24 Jul 2026, both 📄 under the taxonomy) but scored 0.7 with no reason. Recomputed R1 2.0, total 10.9, NONE holds."
    - "E11 MINOR: G1 scored 1.0 with its core tests failed while G2 scored 0 with two listed indicators present (inventory Rs 78 to 74 Cr, 111 to 77 days; debtor days 203 to 178). Same bar: G2 0.7-1.0 (total 11.0-11.3) or G1 0 (total 9.3). NONE holds."
    - "E12 MINOR: A4 labelled Moderate at raw 2 / adjusted 1.4 while E1, H2, R1 labelled Weak at raw 2 / adjusted 1.4; active_categories inconsistent (B2 only, or five rows)."
    - "E19 MINOR: report says pipeline items are 'in the register, not the score', but A4, R1, E1, H2 score 1.4 each (5.6 of 10.3) on items also registered. Score stands under the 0.7x rule; statement wrong. Strict reading: E1, H2 to 0, total 7.5, NONE holds."
    - "E27 MINOR: evidence_mix claim 9 and inference 3 do not reconcile with report tags (14 🎙️-tagged items in Section 3; >= 8 🔍-tagged items); counting basis not stated. documented 10 reconciles."
valuation: {status: "pending", rules_checked: 0, fails: []}  # phase 3; stages 10 and 11 not run
expectation_ledger: {status: "pending", present: null, downside_row: null, all_rows_confirm_by: null, all_rows_metric_threshold: null, prob_in_range: null, decay_status_valid: null, off_ledger_credit: null, residual_pct_cmp: null, residual_starter_cap_ok: null, fails: []}  # rules 13-14; any fail = REWORK stage 11; pending phase 3
business_understanding_narrative: {status: "pending", present: null, five_questions: null, prose_only: null, b09_candidates_referenced: null, no_valuation_vocabulary: null, fails: []}  # rule 9; any fail = REWORK stage 13; pending /finalize
recomputed_destination_pe: ""  # not in phase-1 scope
recomputed_decision: ""        # concur: Gate 0 GOOD (most evidenced reading); EM class NONE (recomputed 11.6-11.9)
findings:
  - {id: "C-G03", stage: "B01", severity: "MAJOR", rule: "Gate 0 formula definitions: ROCE fixed, no substitutes; rule 5 NOT FOUND = 0", claimed: "ROCE on NW + borrowings; A1 3, A2 1, A4 5; Block A 13; core 61; GOOD", recomputed: "Mixed basis (FY25 23.0%, FY26 27.4%): Block A 13, core 61, GOOD. Rule-5 strict: Block A 4, core 52, AVERAGE", decision_effect: "survives on most evidenced reading; decision-changing only if the corpus holds no TA and CL for >= 3 years"}
  - {id: "C-G06", stage: "B01", severity: "MINOR", rule: "Gate 0 formula definitions: FCF = CFO - capex excluding acquisitions", claimed: "CFO + CFI proxy; B2 0, B3 0", recomputed: "FY17-FY24 undetermined; FY25/FY26 sign unchanged", decision_effect: "none; GOOD holds on any Block B value"}
  - {id: "C-G39", stage: "B01", severity: "MINOR", rule: "Block F: peer data not provided = 0, PEER DATA NEEDED", claimed: "M5 1 (top 5 of a 4-name set)", recomputed: "M5 0; moat 18; grand total 79; MODERATE", decision_effect: "none"}
  - {id: "C-G52", stage: "B01", severity: "MINOR", rule: "Output: end with exactly this fenced YAML block", claimed: "report copy and block file differ in four text fields", recomputed: "scored fields identical", decision_effect: "none"}
  - {id: "C-G53", stage: "B01", severity: "MINOR", rule: "Unresolved inputs carried to input_gaps / data_notes", claimed: "E4 3 on Rs 36.98 Cr; GST composition noted in report body only", recomputed: "if GST items outside the total: 22.3%, E4 1, core 59, AVERAGE", decision_effect: "presentational; class-sensitive; Note 34 read decides"}
  - {id: "C-E03", stage: "B07", severity: "MINOR", rule: "Rules 2-3: tag and source anchor on every evidence item", claimed: "recount item anchored 'AR via B03'; 2D items untagged", recomputed: "recount 10, or 9 if the B03 route lacks an AR page", decision_effect: "none"}
  - {id: "C-E10", stage: "B07", severity: "MINOR", rule: "Section 5 multiplier by evidence quality; taxonomy: regulatory application submitted = 📄", claimed: "R1 2 x 0.7 = 1.4", recomputed: "R1 2 x 1.0 = 2.0; total 10.9", decision_effect: "none; NONE holds"}
  - {id: "C-E11", stage: "B07", severity: "MINOR", rule: "Same bar for like evidence (Rule J); rule 5 NO EVIDENCE only where none exists", claimed: "G1 1.0; G2 0", recomputed: "G2 0.7-1.0 (total 11.0-11.3) or G1 0 (total 9.3)", decision_effect: "none; NONE holds"}
  - {id: "C-E12", stage: "B07", severity: "MINOR", rule: "Section 3 strength labels consistent with scores; active_categories Strong/Moderate only", claimed: "A4 Moderate; E1, H2, R1 Weak; all at adjusted 1.4", recomputed: "active_categories B2 only, or A4, B2, E1, H2, R1", decision_effect: "none; guard not triggered"}
  - {id: "C-E19", stage: "B07", severity: "MINOR", rule: "Optionality Register: watched, never scored", claimed: "pipeline 'in the register, not the score'", recomputed: "5.6 of 10.3 on registered items; strict reading total 7.5", decision_effect: "none on class; forward double-credit risk at stage 11 (F-1)"}
  - {id: "C-E27", stage: "B07", severity: "MINOR", rule: "Block evidence_mix = item counts", claimed: "documented 10, claim 9, inference 3", recomputed: "documented 10; claim >= 14 (Section 3 tags); inference >= 8", decision_effect: "none"}
forward_flags:
  - "F-1 stage 11 Pillar 3: em_score already credits R1/A4/E1/H2 for items also in catalysts_12m (Unit 6 licence, EPO, Pembrolizumab, BE dossiers, EU MAs); no second credit as catalyst proximity."
  - "F-2 Halt 1: Gate 0 core 61, line 60. Downside routes to AVERAGE: ROCE rule-5 reading (52), E4 composition (59), B1 knife-edge (59, Rs 2.02 Cr CFO headroom)."
  - "F-3 operator ruling candidate: mixed-tier multiplier rule absent in prompts/07 Section 5; decides NONE (10.3; recompute 11.6-11.9) vs MODEST (12.4-13.4) on this name."
  - "F-4 Verifier A pointers: B1 headroom Rs 2.02 Cr; C1 0.11pp under 20%; D1 0.07x over 1.0x; Note 34 sum 36.56 vs 36.98; FAT 3.23x (B01, 155.57) vs 3.35x (B07, 150)."
pending_rules: "Verifier C rules 4, 6, 7, 11-15 at phase 3; rules 9-10 at /finalize. Rule 8 checked (B07 categories 21 and 22 present, scored 0 correctly)."
critical_count: 0
major_count: 1
minor_count: 10
acceptance_rate: 86             # 69 passed / 80 checked = 86.25%
```
