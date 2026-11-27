# STAGE 12 VERIFIER C: FRAMEWORK ADHERENCE. GVPIL, run 2026-11-15. PHASE 1 SCOPE.

## 0. Scope and method

- Scope: phase 1. This audit covers Gate 0 (B01) and the Emerging Moat scan (B07) only. The valuation audit is pending phase 3, because B10 and B11 do not exist yet. That audit covers rules 4, 7 and 11 to 15, plus the valuation half of rule 5.
- Rule sources read: prompts/01-gate-0-pipeline.md (P01), prompts/07-emerging-moat-pipeline.md (P07), and the Verifier C section of prompts/12-verifiers-pipeline.md (P12).
- Artifacts read: runs/gvpil-2026-11-15/outputs/reports/01-gate0.md (B01), outputs/blocks/B01-gate0.yaml, outputs/reports/07-emoat.md (B07), outputs/blocks/B07-emoat.yaml.
- Not read: Master Prompt, the Section 1B layers, FTTCP (phase 3 only). I read no corpus document.
- Method: I re-derive each score from the inputs that B01 and B07 state, using the thresholds as written. I take each stated number as given. Verifier A decides whether a number exists in the source. "calc" marks my own arithmetic on stated inputs.
- Anchors: "B01 l.N" and "B07 l.N" are report line numbers. "P01 l.N", "P07 l.N" and "P12 l.N" are rule-file line numbers. "block l.N" is a line in the stage's block file.
- Report and block parity: the B01 block file matches the report's fenced YAML (B01 l.94-132 against B01-gate0.yaml l.1-39). The B07 block file matches its report (B07 l.288-343 against B07-emoat.yaml l.1-56). PASS.

## 1. GATE 0 (B01) COMPLIANCE

### 1A. Operating rules and formulas

| # | Rule (source) | B01 application | Re-derivation | Result |
| --- | --- | --- | --- | --- |
| G01 | Open with the data-available line; window minimum 3 years (P01 l.23-25) | "Data available: 10 years (FY17 to FY26)" (B01 l.3) | 10 years stated | PASS |
| G02 | Anchor every extracted number (P01 l.15-18) | Each line item is anchored to screener-data, an AR26 page, or "computed" (B01 l.35-82) | All 37 metric lines checked. Each number carries an anchor or "computed". | PASS |
| G03 | ROCE = EBIT / (Total Assets - Current Liabilities). Formulas are "fixed, do not substitute alternatives". Compute only when the source ROCE is absent, and state "computed" (P01 l.27-31) | The source has no ROCE row and no CL row. B01 uses a proxy: capital employed = equity + reserves + borrowings, for all years (B01 l.17) | The formula was substituted. Formal TA - CL exists for FY25 (62.6%) and FY26 (41.4%) only (B01 l.17). With those two values swapped in, the median stays 11.5%, the minimum stays -43.2%, and latest 41.4% is still above earliest 10.3% (calc). A1 = 1, A2 = 0, A4 = 5. No score changes. A strict reading treats ROCE as NOT FOUND for FY17 to FY24 (CL absent), and 2 formal years fall under the 3-year minimum. That gives A1 = A2 = A4 = 0, Block A = 0 and core 27 (calc). AVOID holds under both readings. | FAIL, MINOR (F-G03) |
| G04 | ROE = PAT / average net worth; earliest year on closing, stated (P01 l.32-33) | Average net worth used; FY17 closing stated (B01 l.21) | All ten ROE values reproduce from the stated PAT and net worth within 0.1pp. Example FY26: 252.61 / ((316.65 + 582.54) / 2) = 56.2% (calc). | PASS |

### 1B. Blocks A to E

| # | Metric (threshold source) | B01 input and score | Re-derived | Result |
| --- | --- | --- | --- | --- |
| G05 | A1 median ROCE (P01 l.55) | 11.5% = 1 (B01 l.35) | Sorted 10 values; middle pair 10.3 and 12.7; median 11.5% falls in the 10-14.9 band = 1 | PASS |
| G06 | A2 minimum ROCE (P01 l.56) | -43.2% = 0 (B01 l.36) | Under 8 = 0 | PASS |
| G07 | A3 median ROE (P01 l.57) | 5.4% = 0 (B01 l.37) | Middle pair 3.2 and 7.5; median 5.35% (calc). Under 12 = 0. | PASS |
| G08 | A4 ROCE trend (P01 l.58-59) | 48.4 vs 10.3 = 5 (B01 l.38) | Latest at or above earliest = 5 | PASS |
| G09 | B1 cumulative CFO / cumulative PAT (P01 l.62-63) | "N/M" = 0 (B01 l.43) | 365.60 / -190.51 = -1.92 (calc). Under 0.50 = 0. The score matches. The "N/M" label borrows the CAGR edge rule, but the score is the same. | PASS |
| G10 | B2 FCF-positive proportion (P01 l.64), with NOT FOUND scored 0 (P01 l.19-22) | 3 of 6 determinable years = 50% = 2 (B01 l.44) | The scoring window is 10 years (B01 l.3). The four NOT FOUND years are not shown positive, so 3 / 10 = 30% (calc), under 50 = 0. B01 uses the "missing input scores 0" rule for B3 and B4 (B01 l.45-46). Only B2 shrinks its denominator. | FAIL, MAJOR (F-G10). Recomputed B2 = 0, Block B = 0 |
| G11 | B3 cumulative FCF / PAT (P01 l.65-66) | 0 (B01 l.45) | Full-window FCF is NOT FOUND and cumulative PAT is negative. Score 0. | PASS |
| G12 | B4 WC days change (P01 l.67-68) | 0, FY17 payables NOT FOUND (B01 l.46) | NOT FOUND scores 0. The available pair, FY25 to FY26, is 2 years, under the 3-year minimum. | PASS |
| G13 | C1 revenue CAGR (P01 l.41, l.71) | -4.9% = 0 (B01 l.49) | (1,269.39 / 1,993.48)^(1/9) - 1 = -4.9% (calc). Under 5 = 0. The basis mismatch is disclosed (B01 l.5). | PASS |
| G14 | C2 PAT CAGR with the negative-endpoint rule (P01 l.45-46, l.72) | N/M, FY17 -2.46 Cr = 0 (B01 l.50) | Edge rule honoured | PASS |
| G15 | C3 positive YoY revenue years (P01 l.73) | 5 of 9 = 55.6% = 1 (B01 l.51) | 50-74 band = 1 | PASS |
| G16 | C4, with "score C4 = 0 and note" (P01 l.50, l.74) | 0, noted (B01 l.52) | Edge rule honoured | PASS |
| G17 | Loss-to-profit swing note in data_notes (P01 l.47-49) | Present (B01 l.125) | Note present. See O-05 on the window endpoints. | PASS |
| G18 | D1 net debt / EBITDA (P01 l.77-79) | Net cash = 5 (B01 l.55) | Borrowings 17.59 Cr are below cash 430.42 Cr, so net cash = 5. The related-party loan stays out of cash, which is the conservative reading. | PASS |
| G19 | D2 interest coverage (P01 l.80-82) | 9.2x = 4 (B01 l.56) | 290.36 / 31.52 = 9.21x (calc). 5-9.9 band = 4. See O-02. | PASS |
| G20 | D3 debt / equity (P01 l.83-84) | 0.03 = 5 (B01 l.57) | 17.59 / 582.54 = 0.030 (calc). Under 0.1 = 5. | PASS |
| G21 | D4 current ratio (P01 l.85-86) | 1.34 = 2 (B01 l.58) | 19,200.1 / 14,363.0 = 1.34 (calc). 1.2-1.49 band = 2. See O-03. | PASS |
| G22 | E1 promoter holding (P01 l.89-90) | 68.58% = 5 (B01 l.61) | 60 or more = 5 | PASS |
| G23 | E2 three-year change (P01 l.91-92) | 0.00pp = 3 (B01 l.62) | Within 1% = 3 | PASS |
| G24 | E3 pledge, with NOT FOUND scored 0 (P01 l.93, l.19-22) | NOT FOUND = 0; sensitivity stated (B01 l.63) | Rule honoured | PASS |
| G25 | E4 contingent liabilities / net worth (P01 l.94-95) | 78.6% = 0 (B01 l.64) | 457.59 / 582.54 = 78.6% (calc). Over 30 = 0. | PASS |

### 1C. Block F moat tests

| # | Test (threshold source) | B01 input and score | Re-derived | Result |
| --- | --- | --- | --- | --- |
| G26 | M1 pricing power (P01 l.102-104) | 0 (B01 l.71) | Revenue CAGR -4.9% fails the growth leg of every band. Score 0. | PASS |
| G27 | M2 cost advantage (P01 l.105-106) | +12.6pp = 5, flagged (B01 l.72) | Peer median of 7.6, 8.6 and 11.6 is 8.6 (B01 l.67). 21.2 - 8.6 = 12.6pp (calc), 5pp or more = 5. A mechanical score with the credit named as a flag follows the rule as written. Ex-credit, +3.8pp still scores 3, so the moat stays present. | PASS |
| G28 | M3 capital efficiency (P01 l.107-108) | FAT 31.6x, ROCE 48.4% = 5 (B01 l.73) | As stated, FAT over 3x and ROCE over 20% = 5. The rubric does not name the ROCE year. See O-01. | PASS |
| G29 | M4 customer stickiness (P01 l.109-111) | 0 (B01 l.74) | 4 decline years falls in the 3-or-more band = 0 | PASS |
| G30 | M5 scale, with PEER DATA NEEDED (P01 l.99-100, l.112-113) | 0, PEER DATA NEEDED (B01 l.75) | The segment universe is absent, so 0 and marked | PASS |
| G31 | M6 technology (P01 l.114-116) | 0, R&D nil (B01 l.76) | Under 1% = 0 | PASS |
| G32 | M7 regulatory (P01 l.117-119) | 0 (B01 l.77) | Unregulated = 0 | PASS |
| G33 | M8 distribution (P01 l.120-122) | 0, "None quantified" (B01 l.78) | Band 0 needs "none". Band 1 is "mentioned unquantified". The basis line does not say which applies. The moat count does not change at either score. See O-04. | PASS |
| G34 | M9 brand, proxy stated (P01 l.123-125) | +8.8pp with negative growth = 1 (B01 l.79) | Above peers with growth below = 1. The proxy is stated. | PASS |
| G35 | M10 switching costs (P01 l.126-128) | 0 (B01 l.80) | No overall growth = 0 | PASS |
| G36 | M11 network effects; two-window test binds at 6 or more years (P01 l.129-133) | 0, on the latest 3-year CAGR of -10.9% only (B01 l.81) | 10 years are available, so the two-window test binds. B01 reports the latest window only. It does not compute the prior window (FY20 to FY23) or the selling-expense trend. The band-5 test is "latest 3yr rev CAGR > prior 3yr AND selling exp % declining", with no positive-growth leg. The latest window beats the prior one if FY20 revenue exceeded 1,795.81^2 / 1,269.39 = 2,540.5 Cr (calc). B01 does not state FY20 revenue. The outcome cannot be decided from the stated inputs: it is 0 or 5. | FAIL, MINOR (F-G36) |
| G37 | M12 negative WC (P01 l.134-135) | 0 (B01 l.82) | Available years 257.2 and 103.2 days are over 45 = 0. Other years are NOT FOUND. | PASS |
| G38 | Moat present at 3 or more; class bands (P01 l.98-99, l.137-138) | M2 and M3 = 2, MODERATE (B01 l.84) | 2 present falls in the 2-3 band = MODERATE. Moat score 5 + 5 + 1 = 11 (calc). | PASS |

### 1D. Classification, overrides and block

| # | Rule (source) | B01 application | Re-derivation | Result |
| --- | --- | --- | --- | --- |
| G39 | Totals arithmetic | A 6, B 2, C 1, D 16, E 8 = 33; moat 11; total 44 (B01 l.88) | Sums reproduce on B01's own scores | PASS |
| G40 | Data confidence (P01 l.142-144) | 10 years, full; no downgrade (B01 l.88, l.120) | 10 or more years = full | PASS |
| G41 | Classification matrix (P01 l.146-149) | Core 33 is under 40, so AVOID (B01 l.88) | Core under 40 = AVOID. The recomputed core of 31 also gives AVOID. | PASS |
| G42 | Deal-breakers 1 to 9 (P01 l.151-159) | 1, 2 and 8 recorded. DB4 is "not triggered ... not <0.50 by calculation" (B01 l.89) | DB4: -1.92 is under 0.50 (calc). B01 scored B1 = 0 on that same ratio, then declared DB4 not triggered. The stated reason is wrong arithmetic. P01 operating rule 2 allows "only numbers and the scoring rules provided" (P01 l.13). A mechanical reading fires DB4, max AVERAGE. The cap does not change, because DB8 already sets max AVERAGE and the class is AVOID. | FAIL, MINOR (F-G42) |
| G43 | State which years drive each deal-breaker (P01 l.151-154) | FY22-FY24, FY19-FY21, FY24 (B01 l.89; block l.24-26) | Present | PASS |
| G44 | FLAG-GATE0 when the class is AVERAGE or below with depressors named (P01 l.175-177) | Present (B01 l.104) | Present | PASS |
| G45 | Block schema (P01 l.168-198) | All fields present; analyst_note about 75 words | Schema complete; under the 200-word cap | PASS |

Gate 0 tally: 45 rules checked. 41 PASS. 4 FAIL (1 MAJOR, 3 MINOR).

### 1E. Gate 0 recomputed as written

| Item | B01 | Recomputed | Change |
| --- | --- | --- | --- |
| B2 | 2 | 0 | -2 |
| Block B | 2 | 0 | -2 |
| Core score | 33 | 31 | -2 |
| Moat score | 11 | 11 | none |
| Grand total | 44 | 42 | -2 |
| Moats confirmed / class | 2 / MODERATE | 2 / MODERATE | none (O-01 sensitivity: 1 / THIN) |
| Classification | AVOID | AVOID | concur |
| Deal-breakers | 1, 2, 8 | 1, 2, 4, 8 | DB4 added; it does not bind |

Robustness of AVOID. The recomputed core of 31 sits 9 points under the AVERAGE line (calc). B01's E3 sensitivity (pledge 0%, +5) gives 36 (calc). Adding O-02 (D2 on the AR continuing finance cost, +1) gives 37. Adding a one-band D4 move under O-03 (+2) gives 39. AVOID holds under every reading I can build from B01's stated inputs. The one exception is a D4 current ratio of 2.0 or more with held-for-sale items included. B01 does not state those items, so that case is NOT FOUND.

## 2. EMERGING MOAT (B07) COMPLIANCE

| # | Rule (source) | B07 application | Check | Result |
| --- | --- | --- | --- | --- |
| E01 | All six sections plus the Optionality Register (P07 l.28, l.48-210) | Sections 1 to 6 and the register are present (B07 l.16-285) | Present | PASS |
| E02 | Evidence mark on every evidence item (P07 l.29-34) | Each scored row and each Section 1 item carries a 📄, 🎙️ or 🔍 mark | Present | PASS |
| E03 | Source anchor on every evidence item, in (AR p.__) form (P07 l.35-36) | Most items are anchored to a page, slide, call page or filing | Three items have no page or note: A2 "AR26 governance report" (B07 l.87); A4 "NPI budget oversight (AR26)" (B07 l.91); H3 "AR26 BRSR" (B07 l.135). Four items are anchored only to an upstream stage block, not a source: G1 guarantee INR M 16,000 "(B03)" (B07 l.125); G2 receivable days "(B02 calc)" and inventory and revenue growth "(B02)" (B07 l.127); F1 attrition 8.7% "(B03)" (B07 l.119). G1 and G2 are scored rows. | FAIL, MINOR (F-E03) |
| E04 | 22 categories addressed or NO EVIDENCE FOUND (P07 l.65-67; P12 l.241-242) | 22 entries (B07 l.85-141) | A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3, I1-I2 = 22 | PASS |
| E05 | R1 scored (P07 l.161-171) | Section 4 and Section 5 row 23 (B07 l.178, l.208) | Present | PASS |
| E06 | Section 3 summary: 22 rows with evidence, type, strength and time; Strong/Moderate count (P07 l.155-158) | B07 l.145-170 | 22 rows, 4 columns, "0 Strong, 3 Moderate" | PASS |
| E07 | Completionist guard and the 📄 recount line (P07 l.41-46, l.158-159) | "6 documented items across 5 categories" (B07 l.170) | The six items map to A1, E1, G1 (two items), G2 and F2 = 5 categories. 8 scored categories is under 12, so the guard does not fire. | PASS |
| E08 | Likelihood x impact raw matrix (P07 l.171-173) | B07 l.184-208 | ML = 1 (A1, E1, F2, G2); HM = 3 (A4, C1); MM = 2 (G1, R1). All match. F2 text says "LM" and the table says "M / L"; both score 1. | PASS |
| E09 | Multipliers 📄 1.0, 🎙️ 0.7, 🔍 0.5 (P07 l.173) | B07 l.184-208 | 2.1 = 3 x 0.7; 1.4 = 2 x 0.7; 📄 rows x 1.0. All match. | PASS |
| E10 | Score tier matches the stated evidence tier (P12 l.243-244) | Per-row marks (B07 l.186-208) | No 🎙️-only row carries 1.0. A1 carries 📄 on committed capex (QPPL agreements, Reg 30 20 May 2026). Committed capex is in the 📄 definition list (P07 l.30). C1 is mixed 🎙️ and 🔍, scored at 0.7. | PASS |
| E11 | Adjusted total (P07 l.173-174) | 11.6 (B07 l.209) | 1.0 + 2.1 + 2.1 + 1.0 + 1.0 + 2.0 + 1.0 + 1.4 = 11.6 (calc) | PASS |
| E12 | Classification band (P07 l.175-176) | NONE (B07 l.213; block l.23) | 11.6 is under 12 = NO MEANINGFUL EMERGING MOAT | PASS |
| E13 | I1/I2 contribution stated separately (P07 l.180-181) | "0.0 of 11.6" (B07 l.211) | Present | PASS |
| E14 | Category 21 (I1) above 0 only with both legs, and the (b) leg with at least one 📄 (P07 l.122-138; P12 l.292-295) | 0; legs (a) and (b) absent (B07 l.139) | Gate honoured | PASS |
| E15 | Category 22 (I2) above 0 only with a specific named sacrifice (P07 l.139-153; P12 l.295-296) | 0 (B07 l.141) | Gate honoured | PASS |
| E16 | I2 question answered "for each moat claimed anywhere in this scan" (P07 l.140-142) | Answered for A4, C1 and G1 (B07 l.141) | Eight rows carry a score (B07 l.186-208). A1, E1, F2, G2 and R1 get no answer. Each row's own text points to 0: E1 says "a single order is not a moat" (B07 l.113) and R1 is "shared" (B07 l.178). I2 most likely stays 0. | FAIL, MINOR (F-E16) |
| E17 | One improvement credited through one mechanism (CLAUDE.md NEVER list; B07 applies the same rule at H2, B07 l.133) | G1 (MM, 2.0) cites the INR 880 cr bank balance and AR cash, "discounted by: cash is a one-time BHEL receivable release" (B07 l.125). G2 (ML, 1.0) credits receivable days 409 to 219 (B07 l.127). The analyst note says "No row depends on the FY26 one-offs or the receivable release" (B07 l.343). | The receivable release shows up as cash in G1 and as the drop in days in G2. That is one event credited in two categories. The note's claim conflicts with both rows' own text. Reading 1 (G1 as written): cash is part of G1's evidence, so the release is credited twice. The fix is G2 = 0, or G1 drops its cash leg to ML 1.0. Either way the total is 10.6 (calc). Reading 2: G1 rests on the ICRA upgrade and the absence of term debt alone, with cash named only as a limit. Then there is no double credit. The separating observation is whether the ICRA rationale of 3 Mar 2026 attributes the upgrade to the receivable collection. B07 does not state this. G1 lists the cash as evidence, so reading 1 governs. | FAIL, MAJOR (F-E17). Recomputed EM 10.6, still NONE |
| E18 | Section 1A, 1B and 1C (P07 l.48-55) | B07 l.18-46 | Present | PASS |
| E19 | Section 2A to 2D, with the 2C arithmetic shown (P07 l.57-63) | B07 l.50-77. 2C shows 180 x 51.5 = 9,270 = 73.0% (B07 l.73) | Present and shown | PASS |
| E20 | Block field capex_embedded_growth_pct is "from 2C" (P07 l.233) | 0, with flag CAPEX_GROWTH_NOT_MEANINGFUL carrying 73.0% (B07 l.73; block l.17, l.38) | The field holds a value that 2C did not produce. A 0 asserts no capex-led growth. That is a judgment, not the 2C output. The flag keeps the 73.0% and the reason, so no information is lost. As written, the field holds 73.0 with the flag beside it. The field is not scored, so EM does not change. | FAIL, MINOR (F-E20) |
| E21 | Section 4A, 4B and 4C (P07 l.161-168) | B07 l.172-178 | Present | PASS |
| E22 | Optionality register: 4 columns; rows scored 0 or on 🎙️/🔍 only; carried in the block (P07 l.183-196) | 7 rows (B07 l.217-225; block l.39-46) | Format and eligibility hold. The Shoaiba and net-cash rows extend the scored rows E1 and G1 forward, unscored. | PASS |
| E23 | F2 cross-references the injected B05 promise-delivery record (P07 l.106-107) | 7 delivered, 1 partial, 0 missed, grade B (B07 l.121) | Present. See O-07. | PASS |
| E24 | 6A windows: next 12m, 12-24m, 24-36m, 3-5yr (P07 l.199-200) | B07 l.231-236 | Present | PASS |
| E25 | 6B risks with early warnings (P07 l.200-201) | B07 l.240-247 | Present | PASS |
| E26 | 6C uses the injected Gate 0 values (P07 l.201-203) | Core 33; moat 11, 2 confirmed, MODERATE; total 44, AVOID; EM 11.6, NONE (B07 l.253-256) | Matches the B01 block (block l.17-22) | PASS |
| E27 | 6D label from the standard set; full reasoning on HIGH POTENTIAL and TURNAROUND (P07 l.203-208) | AVOID, with both rows reasoned (B07 l.261-264) | The label is in the set and both rows are reasoned. P07 does not write out the matrix cells, so I can check the mapping against the label set only (O-10). | PASS |
| E28 | 6E card: evolution map, 12-month catalysts, biggest risk (P07 l.208-210) | B07 l.268-285 | Present | PASS |
| E29 | active_categories holds only Strong/Moderate rows (P07 l.227) | A4, C1, G1 (block l.24-27) | Matches the three Moderate rows | PASS |
| E30 | Block schema (P07 l.216-243) | All fields present; analyst_note about 140 words | Schema complete; under the 200-word cap | PASS |

Emerging Moat tally: 30 rules checked. 26 PASS. 4 FAIL (1 MAJOR, 3 MINOR).

### 2B. Emerging Moat recomputed as written

| Item | B07 | Recomputed |
| --- | --- | --- |
| G2 adjusted | 1.0 | 0 (single credit) |
| EM adjusted total | 11.6 | 10.6 |
| EM class | NONE | NONE (concur) |
| Gap to the 12 band edge | 0.4 | 1.4 |
| B07 Shoaiba sensitivity (E1 from 1.0 to 3.0) | 13.6, MODEST | 12.6, still MODEST |
| capex_embedded_growth_pct | 0 | 73.0, with the flag |
| Combined assessment (6D) | AVOID | AVOID (concur) |

## 3. FINDINGS REGISTER

| ID | Severity | Framework | Rule | Stage value | Recomputed | Decision impact |
| --- | --- | --- | --- | --- | --- | --- |
| F-G10 | MAJOR | Gate 0 | B2 with NOT FOUND scored 0 on the 10-year window (P01 l.19-22, l.64) | 3/6 = 50% = 2 (B01 l.44) | 3/10 = 30% = 0. Block B 0, core 31, grand total 42 (calc) | None. AVOID holds. The deal-breaker 2 cap (max GOOD) is unchanged. |
| F-E17 | MAJOR | EM | One improvement, one mechanism (CLAUDE.md; B07 l.133) | G1 2.0 and G2 1.0 both rest on the FY26 receivable release (B07 l.125, l.127) | G2 = 0. EM 10.6 (calc) | None. NONE holds. The gap to 12 widens from 0.4 to 1.4. The Shoaiba upside case still crosses into MODEST (12.6). |
| F-G03 | MINOR | Gate 0 | Fixed ROCE formula (P01 l.27-31) | Proxy capital employed for all years (B01 l.17) | Formal TA - CL where available leaves A1 to A4 unchanged. The strict NOT FOUND reading gives Block A 0 and core 27 (calc) | None. AVOID holds under both readings. |
| F-G36 | MINOR | Gate 0 | M11 two-window test (P01 l.129-133) | Latest window only, scored 0 (B01 l.81) | Cannot be decided from stated inputs: 0, or 5 if FY20 revenue exceeded 2,540.5 Cr (calc) and selling % declined | None on class. A score of 5 adds a third moat (still MODERATE) and lifts the moat score to 16. |
| F-G42 | MINOR | Gate 0 | Deal-breaker 4 (P01 l.156-157) | Not recorded, "not <0.50 by calculation" (B01 l.89) | -1.92 is under 0.50 (calc). DB4 fires, max AVERAGE | None. DB8 already sets max AVERAGE and the class is AVOID. |
| F-E03 | MINOR | EM | Source anchor on every evidence item (P07 l.35-36) | 3 items have no page or note; 4 items are anchored to B02/B03 | Page or note anchors needed on A2, A4 (NPI), H3; source anchors needed on G1, G2, F1 | None on score. Weak anchors only. Verifier A owns whether the numbers exist. |
| F-E16 | MINOR | EM | I2 question for every claimed moat (P07 l.140-142) | Answered for 3 of 8 scored rows (B07 l.141) | Most likely still 0 | None |
| F-E20 | MINOR | EM | capex_embedded_growth_pct from 2C (P07 l.233) | 0 (block l.38) | 73.0, with the CAPEX_GROWTH_NOT_MEANINGFUL flag | None on EM. Downstream readers of the field alone see 0, not the 2C output. |

## 4. OBSERVATIONS (not counted as fails)

- O-01. Gate 0 moat class rests on one spot year. Both Gate 0 moats draw on FY26 figures. B01 flags the FY26 figures for M2, and M2 survives that flag at 3. M3's ROCE leg uses FY26 48.4% (B01 l.73). The rubric does not name a ROCE year for M3 (P01 l.107-108). Reading 1 (latest year, B01's): M3 = 5. Reading 2 (window median, the basis A1 uses): 11.5% fails even the over-12% band, so M3 = 0. Under reading 2, moats confirmed = 1, class THIN, moat score 6, grand total 37 on the recomputed core (calc). AVOID holds either way. The observation that separates the two readings: FY27 full-year ROCE on the formal TA - CL basis without the loss-allowance credit. If it stays above 20%, reading 1 holds on more than one year. No B01 flag names the M3 dependence. FLAG-EARNINGS-QUALITY names M2 only (B01 l.105). B07 6C carries "2 confirmed, MODERATE" forward (B07 l.254).
- O-02. D2 basis. B01 uses screener interest 31.52 Cr against screener EBIT 290.36 Cr. It also notes an AR continuing finance cost of 21.9 Cr (B01 l.56). On the AR continuing basis, EBIT = 3,285.8 + 219.0 = 3,504.8 mn (calc, from B01 l.11 and l.56). Coverage is then 16.0x, which falls in the 10x-or-more band = 5, so core rises by 1. The rubric names no source for D2. B01's choice keeps one source across D1 to D3 and is disclosed.
- O-03. D4 basis. B01 excludes held-for-sale items from the current ratio (B01 l.58). The rubric does not make that exclusion. B01 does not state the held-for-sale amounts, so a recompute is NOT POSSIBLE from the stated inputs.
- O-04. M8 basis line. "None quantified" (B01 l.78) does not say whether a network is mentioned. The score is 0 or 1. The moat count does not change.
- O-05. Loss-to-profit note. The note names the FY24 to FY25 swing (B01 l.125). The CAGR window runs from FY17 (-2.46 Cr) to FY26 (252.61 Cr), which is itself a swing across the window (P01 l.47-49). Both facts are in the note, so the format is a near match.
- O-06. C1 likelihood. B07 calls C1 "an existing pull being defended, not a new structure; the emerging part is modest (+7.3%)" (B07 l.103), yet scores likelihood H. At likelihood M, MM = 2 x 0.7 = 1.4, and the total falls by 0.7 (calc). This is judgment, not a rule breach.
- O-07. F2 against 6D. F2 records "1 partial (FY27 margin base), 0 missed" (B07 l.121). 6D says "margin guidance failed its first filed test (9.8% in Q2 FY27)" (B07 l.264). These are two descriptions of one test. F2 sits at the lowest non-zero band, so the score does not change.
- O-08. evidence_mix claim count. The count of 8 claims (B07 l.170; block l.28) leaves out at least A1's 🎙️ item (AR26 p.18, B07 l.85) and G1's 🎙️ deck balance (Deck Q4 p.8, B07 l.125). The counts are informational.
- O-09. H2 rationale. B07 says the GE Vernova link "sits in the Gate 0 existing-moat count" (B07 l.133). B01's two moats are M2 and M3 (B01 l.84), and neither is the GE link. H2 = 0 still holds on the "not emerging" ground alone.
- O-10. 6D matrix. P07 lists the labels but not the matrix cells (P07 l.203-208). I checked the AVOID label against the label set and the B01 class only.
- O-11. FY17 to FY19 borrowings. Blank values were taken as 0 (B01 l.32). This is data handling, for Verifier A.
- O-12. Section 3 format. B07 uses prose per category, not "evidence table or NO EVIDENCE FOUND" (P07 l.66-67). The content is present; only the format differs.
- O-13. Forward note for phase 3. catalysts_12m marks "documented" on events whose occurrence or outcome is still pending (block l.33-34). These are the Shoaiba contract signature, anchored to the NOA, and the Q3 FY27 margin outcome. The phase-3 rule 4 check should confirm that Pillar 3 reads these as documented triggers, not documented outcomes.

## 5. NOT RUN IN THIS PHASE

- Rules 4, 7, 11, 12, 13, 14, 15 and the valuation half of rule 5 need B10 and B11. They are pending phase 3.
- Rule 6 needs B09 and the stage 11 catalyst list. The task message did not name B09 as a phase-1 input. The orchestrator should route rule 6 to phase 3.
- Rule 9 needs the stage 13 synthesis. It runs at /finalize.
- Rule 10 checks the B09b dossier. In phase 1 the structural check is mechanical (run-pipeline step 6b). The verifier check runs at /finalize.
- Rule 8 ran here: categories 21 and 22 are present and gated (E14, E15). It passes, so there is no stage 7 REWORK.

## 6. TALLY

- Rules checked: 75 (Gate 0 45, Emerging Moat 30). Passed: 67. Failed: 8.
- Severity: CRITICAL 0, MAJOR 2, MINOR 6.
- Acceptance rate: 67 / 75 = 89.3% (calc). The denominator is 4 or more, so the rate applies. 89.3% is above the 60% REWORK line.
- No REWORK trigger from this verifier in phase 1.
- Two recorded numbers change when recomputed as written: Gate 0 core goes from 33 to 31 and EM from 11.6 to 10.6. Neither changes a classification. Gate 0 stays AVOID, EM stays NONE, and the combined assessment stays AVOID.
- O-01 is the item most relevant to Halt 1. The Gate 0 moat class MODERATE depends on the FY26 spot ROCE.

```yaml
stage: B12c
company: "GVPIL"
run_date: "2026-11-15"
model: "claude-opus-5-5"  # must equal .claude/agents frontmatter; the orchestrator compares it
status: complete
# PHASE 1 SCOPE: gate0 + emoat only. valuation, expectation_ledger, business_understanding_narrative,
# recomputed_destination_pe and recomputed_decision are PENDING (B10/B11 and stage 13 do not exist yet).
# null = not evaluated in this phase, not a finding.
gate0: {rules_checked: 45, fails: ["G03 ROCE formula substituted (proxy capital employed = equity + reserves + borrowings); formal TA-CL recompute leaves A1-A4 unchanged; MINOR", "G10 B2 scored on 6 determinable years; as written 3/10 = 30% gives 0; Block B 2 to 0, core 33 to 31, grand total 44 to 42; MAJOR", "G36 M11 two-window test not performed (prior FY20-FY23 window and selling-expense trend absent); outcome 0 or 5 cannot be decided from stated inputs; MINOR", "G42 DB4 not recorded; cumulative CFO/PAT -1.92 is below 0.50 and fires max AVERAGE; does not bind (DB8 same cap, class AVOID); MINOR"]}
emoat: {rules_checked: 30, fails: ["E03 anchors: 3 evidence items without page or note (A2, A4 NPI oversight, H3); 4 items anchored to upstream blocks B02/B03 instead of a source (G1, G2 x2, F1); MINOR", "E16 I2 question answered for A4, C1, G1 only; A1, E1, F2, G2, R1 unanswered; I2 likely stays 0; MINOR", "E17 FY26 receivable release credited twice (G1 cash, G2 receivable days); G2 to 0, EM 11.6 to 10.6, NONE unchanged; MAJOR", "E20 capex_embedded_growth_pct holds 0, not the 2C result 73.0 (the flag keeps 73.0); MINOR"]}
valuation: {rules_checked: 0, fails: []}  # PENDING PHASE 3: B10/B11 do not exist yet
expectation_ledger: {present: null, downside_row: null, all_rows_confirm_by: null, all_rows_metric_threshold: null, prob_in_range: null, decay_status_valid: null, off_ledger_credit: null, residual_pct_cmp: null, residual_starter_cap_ok: null, fails: []}  # rules 13-14; any fail = REWORK stage 11 | PENDING PHASE 3
business_understanding_narrative: {present: null, five_questions_answered: null, prose_only: null, section6_candidates_named: null, valuation_vocab_leak: null, fails: []}  # rule 9; any fail = REWORK stage 13 | PENDING /finalize
recomputed_destination_pe: ""  # blank if concur; else both values | PENDING PHASE 3
recomputed_decision: ""        # blank if concur | PENDING PHASE 3
findings:
  - {id: "F-G10", framework: "gate0", severity: "MAJOR", rule: "B2 FCF-positive proportion; NOT FOUND scores 0 on the 10-year window (P01 l.19-22, l.64)", stated: "3/6 determinable years = 50% = 2 (B01 l.44)", recomputed: "3/10 = 30% = 0; Block B 0; core 31; grand total 42", decision_impact: "none; classification AVOID holds; deal-breaker 2 unchanged"}
  - {id: "F-E17", framework: "emoat", severity: "MAJOR", rule: "one improvement credited through one mechanism (CLAUDE.md NEVER list; B07 applies it at H2, B07 l.133)", stated: "G1 2.0 (cash from the BHEL receivable release, B07 l.125) and G2 1.0 (receivable days 409 to 219, B07 l.127); note says no row depends on the release (B07 l.343)", recomputed: "G2 0; EM 10.6", decision_impact: "none; NONE holds; gap to the 12 band widens from 0.4 to 1.4; Shoaiba upside case still MODEST at 12.6"}
  - {id: "F-G03", framework: "gate0", severity: "MINOR", rule: "fixed ROCE formula, no substitutes (P01 l.27-31)", stated: "proxy capital employed all years (B01 l.17)", recomputed: "formal TA-CL for FY25/FY26 leaves A1 1, A2 0, A4 5; strict NOT FOUND reading gives Block A 0, core 27", decision_impact: "none; AVOID under both readings"}
  - {id: "F-G36", framework: "gate0", severity: "MINOR", rule: "M11 two-window test binds at 6 or more years (P01 l.129-133)", stated: "0 on the latest 3-year CAGR -10.9% only (B01 l.81)", recomputed: "cannot be decided from stated inputs; 0, or 5 if FY20 revenue exceeded 2,540.5 Cr (calc) and selling % declined", decision_impact: "none on class; a score of 5 makes 3 moats (still MODERATE) and moat score 16"}
  - {id: "F-G42", framework: "gate0", severity: "MINOR", rule: "deal-breaker 4, cumulative CFO/PAT below 0.50 (P01 l.156-157)", stated: "not triggered, not <0.50 by calculation (B01 l.89)", recomputed: "-1.92 is below 0.50; DB4 fires, max AVERAGE", decision_impact: "none; DB8 sets the same cap and the class is AVOID"}
  - {id: "F-E03", framework: "emoat", severity: "MINOR", rule: "source anchor on every evidence item (P07 l.35-36)", stated: "A2, A4 NPI, H3 without page or note (B07 l.87, l.91, l.135); G1, G2, F1 anchored to B02/B03 (B07 l.119, l.125, l.127)", recomputed: "anchor format fix only", decision_impact: "none on score; existence of numbers is Verifier A's"}
  - {id: "F-E16", framework: "emoat", severity: "MINOR", rule: "I2 question for each moat claimed anywhere in the scan (P07 l.140-142)", stated: "answered for A4, C1, G1 only (B07 l.141)", recomputed: "I2 most likely stays 0", decision_impact: "none"}
  - {id: "F-E20", framework: "emoat", severity: "MINOR", rule: "capex_embedded_growth_pct from 2C (P07 l.233)", stated: "0 (block l.38); 2C arithmetic 73.0% in flag CAPEX_GROWTH_NOT_MEANINGFUL (B07 l.73)", recomputed: "73.0 with the flag", decision_impact: "none on EM score; field-only readers see 0"}
# Observations (not findings, not counted): O-01 Gate 0 moat class MODERATE rests on FY26 spot ROCE 48.4% in M3;
# on the window-median reading (11.5%) M3 is 0, 1 moat, THIN, moat score 6. O-13 for phase 3: catalysts_12m marks
# pending events as documented (Shoaiba contract signature, Q3 FY27 margin). Full list in report section 4.
critical_count: 0
major_count: 2
minor_count: 6
acceptance_rate: 89.3             # rules passed / rules checked, % (67 / 75)
```
