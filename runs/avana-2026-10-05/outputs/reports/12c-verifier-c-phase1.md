# VERIFIER C: FRAMEWORK ADHERENCE (B12c), PHASE 1 SCOPE

Company: Avana Electrosystems Ltd (AVANA). Run: avana-2026-10-05. Verifier date: 2026-10-05. Model: claude-opus-5-5.

## 0. Scope and independence

- Scope: Gate 0 (B01) and Emerging Moat (B07) only, per the task message. Phase 1 covers Verifier C rules 2, 3 and 8.
- Valuation audit (rules 4, 5, 7, 11 to 15): PENDING PHASE 3. B10 and B11 do not exist yet.
- Rule 6 (B09 downstream candidates) and rules 9 and 10 (stage 13 narrative, B09b dossier): outside the task scope as given. Not checked.
- Rule sources read: prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md, prompts/12-verifiers-pipeline.md (Verifier C section). No Master, Section 1B or FTTCP file was loaded (phase-1 rule).
- Artifacts read: outputs/blocks/B01-gate0.yaml, outputs/reports/01-gate0.md, outputs/blocks/B07-emoat.yaml, outputs/reports/07-emoat.md.
- Sources consulted to re-derive scores: inputs/screening/screener-Data_Sheet.csv (INR Cr); DANISH, SPCL, MARINE Data_Sheet.csv (INR Cr); RHP 31-Dec-2025 pp.39, 71, 92, 173, 174, 225 (INR lakh); FY26 results legible re-filing pp.10, 11 (INR lakh).
- Independence: outputs/reports/12d-verifier-d.md and B12d.yaml exist in the run folder. I did not open them. I read no upstream reasoning beyond the four named artifacts.
- Verifier A owns the existence of numbers. Where I touch a source number, I use it only to re-derive a score under the stated rule.

## 1. GATE 0 (B01) COMPLIANCE

### 1a. Formulas, edge rules, confidence

| ID | Rule (01-gate-0-pipeline.md) | B01 application | Result |
|---|---|---|---|
| G-01 | Open with "Data available: X years ... Scoring adapted to X-year history" (rule 6) | 01-gate0.md line 5: 7 years, FY20 to FY26 | PASS |
| G-02 | Data confidence: 7-9 years = moderate, no downgrade | moderate, history_downgrade false | PASS |
| G-03 | ROCE = EBIT / (Total Assets minus Current Liabilities); source ROCE if provided; "fixed, do not substitute alternatives" | Screener Data_Sheet has no ROCE, so compute is correct. But B01 used a substitute denominator, Total assets minus Other liabilities (= equity + all borrowings), for all 7 years. CL exists for FY23 to FY25 (RHP p.225) and FY26 (results p.11). | FAIL, MAJOR (see 1d) |
| G-04 | ROE = PAT / average net worth; closing if opening absent, stated | FY20 closing, stated; FY21 to FY26 average (screener-data) | PASS |
| G-05 | WC days = Rec + Inv minus Pay days; basis stated | Revenue basis stated; FY20 to FY22 payables NOT FOUND, window FY23 to FY26 stated | PASS |
| G-06 | FCF = CFO minus capex (PPE + intangibles), excluding acquisitions | Capex FY23 to FY25 RHP p.290, FY26 results p.12; FY20 to FY22 capex NOT FOUND, window FY23 to FY26 stated | PASS |
| G-07 | CAGR formula and edge rules (negative endpoint N/M; loss-to-profit note; C4 = 0 if PAT CAGR N/M) | No negative endpoint (Revenue 22.56 to 83.86 Cr, PAT 1.22 to 11.72 Cr, screener-data); "no loss-to-profit swing" noted | PASS |

### 1b. Metric scores (re-derived from stated inputs and thresholds)

| ID | Metric | B01 input and score | Re-derived | Result |
|---|---|---|---|---|
| G-08 | A1 median ROCE | 17.79% (proxy) = 3 | As written: FY20 to FY22 NOT FOUND; FY23 to FY26 exact median 34.55% = 5 (1d) | FAIL (consequential to G-03) |
| G-09 | A2 min ROCE | 7.09% FY21 (proxy) = 0 | As written: min 16.65% FY23 = 5 (1d) | FAIL (consequential to G-03) |
| G-10 | A3 median ROE | 13.79% = 2 | Series 13.79, 3.15, 4.75, 10.22, 35.05, 48.02, 28.98% (screener-data); median 13.79% = 2 | PASS |
| G-11 | A4 ROCE trend | 27.82% vs 17.79% = 5 | As written 26.61% (FY26) vs 16.65% (FY23) = 5 | PASS |
| G-12 | B1 cum CFO / cum PAT | 15.59 / 27.02 = 0.577 = 1 | Sums re-added from screener-data rows 57 and 24: 15.59 and 27.02; 0.50-0.69 band = 1 | PASS |
| G-13 | B2 FCF-positive years | 2 of 4 = 50% = 2 | FCF FY23 -0.46, FY24 -1.18, FY25 +5.50, FY26 +0.45 Cr; 50-74 band = 2 | PASS |
| G-14 | B3 cum FCF / cum PAT | 4.31 / 25.13 = 0.17 = 0 | <0.20 = 0 | PASS |
| G-15 | B4 WC days change | 168.4 (FY23) to 136.5 (FY26) = 5 | -31.9 days, decreased >5 = 5 | PASS |
| G-16 | C1 revenue CAGR | 24.5% = 5 | (83.86/22.56)^(1/6) - 1 = 24.5% (screener-data) = 5 | PASS |
| G-17 | C2 PAT CAGR | 45.8% = 5 | (11.72/1.22)^(1/6) - 1 = 45.8% = 5 | PASS |
| G-18 | C3 positive YoY years | 5 of 6 = 83% = 3 | FY21 only decline (14.95 vs 22.56 Cr) = 3 | PASS |
| G-19 | C4 PAT minus revenue CAGR | +21.3pp = 5 | = 5 | PASS |
| G-20 | D1 net debt / EBITDA | net cash = 5 | Borrowings 0.76 vs cash 27.83 Cr (screener-data FY26) = 5 | PASS |
| G-21 | D2 EBIT / interest | 19.4x = 5 | 16.65 / 0.86 = 19.4x = 5 | PASS |
| G-22 | D3 debt / equity | 0.013 = 5 | 0.76 / 59.08 = 0.013 = 5 | PASS |
| G-23 | D4 current ratio | 3.34x = 5 | 7,419.66 / 2,218.49 lakh (results p.11) = 3.34x = 5 | PASS |
| G-24 | E1 promoter holding | 73.64% = 5 | >=60% = 5 | PASS |
| G-25 | E2 promoter change, 3 years | -26.36pp = 0 | Pre-IPO 100% (RHP p.92, as on 31-Dec-2025) to 73.64% (SHP 31-Mar-2026); decrease >3% = 0 under any base date | PASS (observation O-1 on the date label) |
| G-26 | E3 pledge | 0% = 5 | = 5 | PASS |
| G-27 | E4 contingent liabilities / net worth | 679.22 / 5,908.03 = 11.50% = 3 | 5-15 band = 3; commitments correctly excluded | PASS |
| G-28 | M1 pricing power | +13.6pp, CAGR 24.5% = 5 | EBITDA margin 5.90% FY20 (1.56+0.42+0.20-0.85 = 1.33 / 22.56) to 19.47% FY26 (15.79+0.86+0.65-0.97 = 16.33 / 83.86) = 5 | PASS |
| G-29 | M2 cost advantage | +7.35pp vs median 12.12% = 5 | Peer FY26 margins: DANISH 92.44/521.45 = 17.73%, SPCL 18.84/155.40 = 12.12%, MARINE 94.45/876.94 = 10.77% (peer Data_Sheets); median 12.12% = 5 | PASS |
| G-30 | M3 capital efficiency | FAT 15.8x, ROCE 27.82% = 5 | ROCE as written 26.61% (>20%) = 5, unchanged | PASS |
| G-31 | M4 stickiness | 1 decline year, recovered = 3 | FY21 decline, FY23 28.41 > FY20 22.56 Cr = 3 | PASS |
| G-32 | M5 scale | mcap rank 3 of 4, margin rank 1 = 3 | Mcap AVANA 315.34, DANISH 1,837.43, MARINE 6,565.49, SPCL 149.04 Cr (Data_Sheets) = 3 | PASS (observation O-2) |
| G-33 | M6 R&D | NOT FOUND = 0 | Rule 5: NOT FOUND scores 0 | PASS |
| G-34 | M7 regulatory | unregulated = 0 | Vendor approvals are not a licensed segment; even "regulated, >10 players" = 1 stays below 3 | PASS |
| G-35 | M8 distribution | 0, basis "no reach metrics in provided data" | RHP p.173 names "6 dealers ... Haryana, Maharashtra, Madhya Pradesh and Rajasthan"; RHP p.174 "As on March 31, 2025, we have 6 dealer spread across India"; RHP p.39 dealer revenue 3.65 lakh FY23 to 86.16 lakh FY25. Network is present, so "none" (0) does not apply. Network growth NOT FOUND, so 3 and 5 do not apply. Re-derived 1 | FAIL, MINOR |
| G-36 | M9 brand (GM proxy) | +13.8pp, CAGR 24.5% = 5 | AVANA (83.86 - (53.10 - 3.30)) / 83.86 = 40.61%; SPCL 23.99%, MARINE 29.51%, DANISH 26.81% (proxy disclosed); median 26.81% = 5 | PASS |
| G-37 | M10 switching costs | 0 | 1 decline year, receivable days 74.4 to 96.7 (+22.3) is not "stable"; 1-band needs 2+ decline years; literal result 0 | PASS (observation O-3) |
| G-38 | M11 network effects | 5 | 7 years >= 6; FY23-26 CAGR 43.4% > FY20-23 8.0%; S&A/sales 8.31% FY23 to 5.01% FY26 (4.20/83.86) = 5 | PASS |
| G-39 | M12 negative WC | 0 | WC 136.5 to 168.4 days, >45 = 0 | PASS |

### 1c. Classification and output

| ID | Rule | B01 application | Result |
|---|---|---|---|
| G-40 | Peer data: score 0 and mark PEER DATA NEEDED if absent; never guess peer figures | Peer sheets provided; DANISH RM proxy disclosed and shown not to change M9 | PASS |
| G-41 | Block and total arithmetic | A 10 + B 8 + C 18 + D 20 + E 13 = 69; moat 31; grand total 100. Arithmetic correct on stated inputs | PASS |
| G-42 | Moat present at >=3; 6+ = FORTRESS | 7 present (M1, M2, M3, M4, M5, M9, M11) = FORTRESS | PASS |
| G-43 | Classification matrix | Core 60-79 + FORTRESS = GOOD+ | PASS |
| G-44 | Deal-breakers 1 to 9, driving years stated | None fire: A 10, B 8 (not <8), median ROCE 17.79%, CFO/PAT 0.577, pledge 0, 1 decline year in 6, PAT positive all years, 7 years. Also none fire under the as-written ROCE | PASS |
| G-45 | FLAG-GATE0 only if classification <= AVERAGE | GOOD+, flags [] | PASS |
| G-46 | Source anchor after every extracted number | Present throughout (screener-data, RHP p., results p., AR p.) | PASS |
| G-47 | Report ends with exactly the fenced YAML block | 01-gate0.md ends with an abridged block (9 schema fields absent: input_gaps, flags, data_years, fy_range, deal_breakers, history_downgrade, data_notes, block_b_trend, analyst_note) and a pointer line after it. Full block exists in B01-gate0.yaml | FAIL, MINOR |

### 1d. ROCE re-derivation under the fixed formula (G-03)

EBIT = PBT + Interest (B01 convention, screener-data). CL = short-term borrowings + trade payables + other current liabilities + short-term provisions.

| Year | EBIT (lakh) | Total assets (lakh) | CL (lakh) | TA minus CL | ROCE as written | B01 proxy |
|---|---|---|---|---|---|---|
| FY20 | 198 | 1,742 (screener) | NOT FOUND | NOT FOUND | NOT FOUND | 17.79% |
| FY21 | 85 | 1,704 (screener) | NOT FOUND | NOT FOUND | NOT FOUND | 7.09% |
| FY22 | 102 | 2,005 (screener) | NOT FOUND | NOT FOUND | NOT FOUND | 7.53% |
| FY23 | 197 | 2,852.04 (RHP p.225) | 496.10 + 125.20 + 450.45 + 334.13 + 262.70 = 1,668.58 (RHP p.225) | 1,183.46 | 16.65% | 11.73% |
| FY24 | 697 | 3,807.43 (RHP p.225) | 635.75 + 353.37 + 322.92 + 317.71 + 537.35 = 2,167.10 (RHP p.225) | 1,640.33 | 42.49% | 30.62% |
| FY25 | 1,260 | 4,838.69 (results p.11, regrouped comparative; equals screener 48.39 Cr) | 442.35 + 266.62 + 660.55 + 331.01 + 427.44 = 2,127.97 (results p.11) | 2,710.72 | 46.48% | 45.83% |
| FY26 | 1,665.31 (results p.10: 1,579.63 + 85.68) | 8,476.53 (results p.11) | 20.54 + 365.29 + 963.55 + 410.24 + 458.87 = 2,218.49 (results p.11) | 6,258.04 | 26.61% | 27.82% |

FY25 on the RHP p.225 basis (TA 4,942.12, CL 2,635.95) gives 54.64%. It is the series maximum on either basis, so the median does not move.

The RHP restated statements cover FY23, FY24, FY25 and H1 FY26 only. The RHP holds no 31-Mar-2022 balance sheet (no "March 31, 2022" string in the file). So FY20 to FY22 CL is NOT FOUND.

Why this is a FAIL, not a disclosed choice:
1. The formula block says "fixed, do not substitute alternatives". The proxy is an alternative. It also differs in substance: it puts short-term borrowings inside capital employed and leaves out long-term provisions (404.55 lakh FY25, 294.41 lakh FY26, results p.11).
2. Rule 5 says a missing input is NOT FOUND, never a filled gap. The FY20 to FY22 proxy values fill a gap.
3. B01 itself runs B2, B3, B4 and M12 on the FY23 to FY26 window when FY20 to FY22 inputs are NOT FOUND. It did not apply the same rule to ROCE.

As-written Block A (ROCE window FY23 to FY26, ROE window FY20 to FY26):
- A1 median of 16.65, 26.61, 42.49, 46.48 = 34.55%: 5 (stated 3)
- A2 minimum 16.65% (FY23): 5 (stated 0)
- A3 median ROE 13.79%: 2 (unchanged)
- A4 26.61% vs 16.65%: 5 (unchanged)
- Block A = 17 (stated 10)

Control: a hybrid series (exact FY23 to FY26 plus proxy FY20 to FY22) sorts to 7.09, 7.53, 16.65, 17.79, 26.61, 42.49, 46.48. Its median is 17.79% and its minimum 7.09%, so it reproduces B01's 10. B01's score holds only if the substituted proxy may fill the NOT FOUND years. The rule forbids that.

### 1e. Gate 0 recomputed summary

| Item | B01 stated | Re-derived as written |
|---|---|---|
| Blocks | A 10, B 8, C 18, D 20, E 13 | A 17, B 8, C 18, D 20, E 13 |
| Core score | 69 | 76 |
| Moat score | 31 | 32 (M8 0 to 1) |
| Grand total | 100 | 108 |
| Moats present / class | 7, FORTRESS | 7, FORTRESS |
| Classification | GOOD+ | GOOD+ (Core 60-79 + FORTRESS); concur |
| Deal-breakers | none | none |
| Weakest block | B 8, then A 10 | B 8 alone; A is no longer a weak block |

The classification survives. Core 76 sits 4 points under the 80 line where FORTRESS would read EXCELLENT. The B01 analyst_note sentence "Block A median ROCE 17.8% reflects FY20-FY22 at 7-18%" rests on proxy values and does not hold under the fixed formula.

## 2. EMERGING MOAT (B07) COMPLIANCE

### 2a. Rule table

| ID | Rule (07-emerging-moat-pipeline.md) | B07 application | Result |
|---|---|---|---|
| E-01 | All six sections plus Optionality Register, one response | Sections 1 to 6 and the register present | PASS |
| E-02 | Evidence taxonomy tag on every evidence item | Tags applied throughout | PASS |
| E-03 | Each of the 22 scan categories has evidence or "NO EVIDENCE FOUND" | A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3, I1-I2 all addressed (22) | PASS |
| E-04 | Section 3 summary table, 22 rows, Strong/Moderate count stated | 22 rows; count 2 (B2, G1) | PASS |
| E-05 | Completionist guard: explicit 📄 recount, reconciled | Line present, but it does not reconcile with its own items (2c) | FAIL, MINOR |
| E-06 | Raw score from L x I matrix | A3 LL 1, B2 MM 2, F1 LL 1, G1 MM 2, G2 LM 1, R1 ML 1: all match HH4 / HM-MH 3 / HL-MM-LH 2 / ML-LM-LL 1 | PASS |
| E-07 | Evidence multiplier matches the stated tier | B2, G1, G2 📄 1.0x; R1 🎙️ 0.7x; A3 🎙️/🔍 at 🔍 0.5x; F1 at 🔍 0.5x with stated reason "headcount flat, cost trend only" | PASS (observation O-5) |
| E-08 | No 🎙️-only category scored as 📄 | None | PASS |
| E-09 | Section 5 "full scoring table, all 23 rows" | Table has 15 rows; zero-score categories grouped (A1/A2/A4, B1/B3, C1/C2, D1/D2, E1/E2, H1/H2/H3). All 23 categories are visible | FAIL, MINOR |
| E-10 | Adjusted total | 0.5 + 2.0 + 0.5 + 2.0 + 1.0 + 0.7 = 6.7 | PASS |
| E-11 | Band: <12 = NO MEANINGFUL EMERGING MOAT; bands absolute (20-Aug-2026 ruling) | 6.7, NONE | PASS |
| E-12 | I1/I2 contribution stated separately | "I1/I2 contribution: 0.0" | PASS |
| E-13 | Rule 8: Category 21 (I1) present; >0 only with both legs and a 📄 (b) leg | Present; leg (a) and leg (b) both fail; 0 | PASS |
| E-14 | Rule 8: Category 22 (I2) present; >0 only with a specific named sacrifice | Present; "nothing must be destroyed" answered per moat; 0 | PASS |
| E-15 | Section 4 R1: 4A approvals, 4B policy, 4C assessment | All three present; R1 scored on policy (🎙️), approvals kept in B2, no double credit | PASS |
| E-16 | Section 2C: capex under execution x historical FAT, % above current revenue, arithmetic shown; block field from 2C | 1,094.99 x 15.76 = 17,259.9 lakh = 205.8% of 8,385.88 (AR p.99, p.100, p.119); field 206 | PASS (observation O-4) |
| E-17 | F2 cross-references the injected promise-delivery record | No-concall substitute declared; B05 record (2 delivered, 1 partial, 4 missed, grade C) cited | PASS |
| E-18 | Optionality register: 4 columns; rows scored 0 or 🎙️/🔍-only; carried in block | 10 rows, 4 columns, block field matches; registration (scored in B2) and order conversion (registered) are separate events | PASS |
| E-19 | Section 6: 6A to 6E; 6C uses injected B01; 6D label in the 8-label set; HIGH POTENTIAL / TURNAROUND reasoned | All present; GOOD+ is in the set; reasons given why HIGH POTENTIAL and TURNAROUND do not apply | PASS |
| E-20 | Source anchor on every evidence item (rule 3) | Three items anchor only to an upstream block, no page: 2A capacity "Relays 70,000 to 1,75,000; panels 600 to 1,500 (RHP via B03)"; Section 3 C2 "(B04 FLAG-CONCENTRATION)"; top_moat_risks "CFO/EBITDA 48.7% and inventory days 164.4 (B03)" | FAIL, MINOR |
| E-21 | catalysts_12m holds next-12-month catalysts (feeds Pillar 3 proximity) | Item 2 (vendor registrations convert to a valued order) carries window "12-24 months" | FAIL, MINOR |
| E-22 | YAML schema complete; report ends with the block; EM not conflated with FTTCP | All 19 schema fields present; report ends with the full block; "It is not FTTCP" stated | PASS |

### 2b. Scorecard re-derivation

| Category | L x I | Raw | Multiplier | Adjusted | Check |
|---|---|---|---|---|---|
| A3 Process innovation | LL | 1 | 0.5 (🔍) | 0.5 | PASS |
| B2 Qualification lock-in | MM | 2 | 1.0 (📄 Reg 30 10-Feb-2026 p.1) | 2.0 | PASS |
| F1 Talent density | LL | 1 | 0.5 (🔍) | 0.5 | PASS (O-5: at 📄 1.0 = 1.0) |
| G1 War chest | MM | 2 | 1.0 (📄 AR p.99) | 2.0 | PASS |
| G2 WC trajectory | LM | 1 | 1.0 (📄) | 1.0 | PASS |
| R1 Regulatory/policy | ML | 1 | 0.7 (🎙️) | 0.7 | PASS |
| All other 17 rows | none | 0 | n/a | 0 | PASS |
| Total | | | | 6.7 | NONE (<12) |

Completionist guard outcome: 2 of 22 active, far under the 12 trigger. No inflation.

### 2c. Recount reconciliation (E-05)

- Recount line (07-emoat.md Section 3; B07 completionist_recount): "13 documented items across 5 scan categories (B2 3, G1 2, G2 2, F1 2, E2 1) plus 3 documented items in Sections 1-2".
- The itemised scan count is 3 + 2 + 2 + 2 + 1 = 10, not 13. With the 3 Section 1-2 items, the total is 13. The report text lists the same 13 items.
- B07 evidence_mix.documented = 16. That figure adds the 3 Section 1-2 items a second time. Re-derived: documented 13, unless 3 more items are named. The summary table tags C2 and F2 "📄 adverse", and the recount does not list them.
- B07 evidence_mix.claim = 8. The report tags at least 13 distinct 🎙️ items. The list omits five of them: customised control panels (AR p.85, 1A), the KIADB "end of October 2026" date (BO19Aug p.2, 1B), testing protocols and automation (AR p.85, A3), IEC type tests at NABL labs (RHP p.153, p.169, B2 and 4A), PLI / Make in India (AR p.73-74, 4B).
- Score effect: none. Multipliers apply per category, not per item count. Guard outcome unchanged.

## 3. FINDINGS

| ID | Framework | Rules | Severity | Stated | Recomputed | Effect |
|---|---|---|---|---|---|---|
| C-01 | Gate 0 | G-03 (with G-08, G-09) | MAJOR | ROCE on equity + borrowings proxy, all 7 years; A1 3, A2 0, Block A 10, Core 69 | ROCE on TA minus CL; FY20 to FY22 NOT FOUND; FY23 to FY26 16.65 / 42.49 / 46.48 / 26.61%; A1 5, A2 5, Block A 17, Core 76 | Classification GOOD+ unchanged; Block A narrative in analyst_note and the "weakest block" line are wrong |
| C-02 | Gate 0 | G-35 | MINOR | M8 0, "no reach metrics in provided data" | M8 1 (6 dealers, RHP p.173-174; dealer revenue RHP p.39); moat 32 | Moat count unchanged (7) |
| C-03 | Gate 0 | G-47 | MINOR | 01-gate0.md ends with an abridged YAML block | Report should end with the full block (it exists in B01-gate0.yaml) | Presentational |
| C-04 | Emerging Moat | E-05 | MINOR | "13 documented items across 5 scan categories ... plus 3"; evidence_mix documented 16, claim 8 | 10 scan + 3 = 13 documented; claims >=13 | No score effect |
| C-05 | Emerging Moat | E-09 | MINOR | Section 5 table 15 rows | 23 rows required | Presentational |
| C-06 | Emerging Moat | E-20 | MINOR | 3 evidence items anchored to B03/B04 only | Page anchors needed | Weak anchor |
| C-07 | Emerging Moat | E-21 | MINOR | catalysts_12m item 2 window 12-24 months | Move it to the optionality register or relabel the window | Risk of an over-counted 12-month catalyst at Pillar 3 in phase 3 |

Counts: CRITICAL 0, MAJOR 1, MINOR 6.

## 4. OBSERVATIONS (not counted; no score effect, or outside Verifier C's domain)

- O-1 (route to Verifier A). B01 E2 reads "100% (RHP p.92, 31-Dec-2023)". RHP p.92 dates its table "as on December 31, 2025 being the date of this RHP" and gives one year prior as 100% too. The score (0) does not change. The date label is a source-fidelity question for Verifier A.
- O-2. M5 "top 3 mcap" is met in a 4-name set that B01 itself calls "not the full segment". The rule is applied as written. The test has little power at this set size. B01 lists four formula artefacts (M1, M2, M9, M11) and leaves out M5. Without M5 the moat count is 6, still FORTRESS.
- O-3 (rubric gap, operator). M10 bands are not monotonic. One decline year with unstable receivables scores 0, but two or more decline years with overall growth score 1. B01 applied the literal text.
- O-4. 2C uses the remaining commitment 1,094.99 lakh (AR p.119) as "capex under execution" and leaves out CWIP 466.79 lakh (AR p.99), which is spent but not yet producing. On CWIP + commitment (1,561.78 lakh), the 2C figure is 293.6%. B07 shows the project-cost reading (1,305.38 lakh, 245.3%), flags the field as mechanical (FLAG-2C-MECHANICAL), and directs stage 11 to the +114% capacity ceiling. The rule does not define the base. Stage 11 should not use any of the 2C figures as a forecast.
- O-5. F1 evidence items are counted as 📄 in the recount (R&D cost RHP p.170, attrition RHP p.176), but the category is scored at 🔍 0.5x. The stated reason is that the looked-for evidence (R&D headcount growth) is absent (flat at 9). A3 uses the same treatment. At 📄 1.0x, F1 = 1.0 and the total = 7.2. The band stays NONE.
- O-6. G1 credits net cash 2,706.64 lakh that is IPO money earmarked to the Objects of the Offer. Unspent IPO funds of 2,103.98 lakh cover the 1,094.99 lakh commitment (07-emoat.md Section 3). B07 states this limit. The score is a judgment within the rule.
- O-7. B07 F2 derives FY23 revenue "backed out of the 43.4% FY23-26 CAGR". The screener FY23 sales figure (28.41 Cr) exists. The item is unscored, so there is no score effect.
- O-8 (dependency alignment). If B01 is revised under C-01, B07 6C (core 69) and combined_reasoning ("core 69, 7 of 12 moats") carry the old core. Both need to move in the same commit.

## 5. VALUATION SCOPE (B10/B11)

PENDING PHASE 3. Rules 4, 5, 7, 11, 12, 13, 14 and 15 are not run. Valuation, expectation-ledger and recomputed destination PE fields in the block below are placeholders, not results.

## 6. ACCEPTANCE ARITHMETIC

- Gate 0: 47 rules checked, 5 FAIL (G-03, G-08, G-09, G-35, G-47), 42 PASS.
- Emerging Moat: 22 rules checked, 4 FAIL (E-05, E-09, E-20, E-21), 18 PASS.
- Total: 60 passed / 69 checked = 87.0%. The denominator is 4 or more, so the rate applies. 87.0% is above the 60% REWORK line.
- G-08 and G-09 are scored as separate FAILs because their recorded scores differ from the as-written scores. They share one root cause and form one finding (C-01).

## 7. ROUTING

- No REWORK trigger from Verifier C phase 1. Acceptance is 87.0%. Rule 8 categories 21 and 22 are present.
- Recommended (orchestrator decision): B01 revision 3 applies the fixed ROCE formula, treats FY20 to FY22 ROCE as NOT FOUND, re-scores M8 to 1, and ends the report with the full block. B07 then aligns 6C (O-8), fixes the recount line and evidence_mix (C-04), expands the Section 5 table (C-05), adds page anchors (C-06), and moves catalysts_12m item 2 (C-07).

```yaml
stage: B12c
company: "AVANA"
run_date: "2026-10-05"
model: "claude-opus-5-5"  # must equal .claude/agents frontmatter; the orchestrator compares it
status: complete
# scope: phase 1 (Gate 0 + Emerging Moat); valuation half PENDING PHASE 3
gate0:
  rules_checked: 47
  fails:
    - "G-03 MAJOR: ROCE computed on Total assets minus Other liabilities (equity + borrowings proxy) for all 7 years; fixed formula is EBIT / (TA - CL); CL available FY23-FY25 (RHP p.225) and FY26 (results p.11); FY20-FY22 CL NOT FOUND"
    - "G-08 (consequential to G-03): A1 stated 3 on proxy median 17.79%; as written 5 on exact FY23-FY26 median 34.55%"
    - "G-09 (consequential to G-03): A2 stated 0 on proxy min 7.09% (FY21); as written 5 on exact min 16.65% (FY23)"
    - "G-35 MINOR: M8 stated 0 on 'no reach metrics in provided data'; RHP p.173-174 names 6 dealers, RHP p.39 dealer revenue 3.65 to 86.16 lakh FY23-FY25; re-derived 1"
    - "G-47 MINOR: 01-gate0.md ends with an abridged YAML block missing 9 schema fields; full block only in B01-gate0.yaml"
emoat:
  rules_checked: 22
  fails:
    - "E-05 MINOR: recount says 13 documented items across 5 scan categories but itemises B2 3 + G1 2 + G2 2 + F1 2 + E2 1 = 10; evidence_mix documented 16 double-adds the 3 Section 1-2 items (re-derived 13); claim count 8 vs at least 13 distinct 🎙️ tags"
    - "E-09 MINOR: Section 5 scoring table has 15 grouped rows, rule requires all 23 rows"
    - "E-20 MINOR: 3 evidence items anchored to B03/B04 only, no source page (2A capacity, Section 3 C2, top_moat_risks CFO/EBITDA and inventory days)"
    - "E-21 MINOR: catalysts_12m item 2 (vendor registrations to valued order) has window 12-24 months"
valuation: {rules_checked: 0, fails: [], status: "PENDING PHASE 3: B10/B11 not yet produced"}
expectation_ledger: {present: null, downside_row: null, all_rows_confirm_by: null, all_rows_metric_threshold: null, prob_in_range: null, decay_status_valid: null, off_ledger_credit: null, residual_pct_cmp: null, residual_starter_cap_ok: null, fails: [], status: "PENDING PHASE 3"}  # rules 13-14; any fail = REWORK stage 11
business_narrative: {checked: false, fails: [], status: "NOT IN PHASE-1 SCOPE: stage 13 not yet run"}  # rule 9; any fail = REWORK stage 13
recomputed_destination_pe: ""  # blank: valuation scope pending phase 3
recomputed_decision: ""        # blank: Gate 0 classification GOOD+ concurs on recompute; valuation pending
findings:
  - id: C-01
    framework: gate0
    rules: "G-03, G-08, G-09"
    severity: MAJOR
    stated: "ROCE proxy (equity + borrowings) all 7 years; median 17.79%, min 7.09%; A1 3, A2 0, Block A 10, Core 69, grand total 100"
    recomputed: "ROCE = EBIT / (TA - CL): FY23 16.65%, FY24 42.49%, FY25 46.48%, FY26 26.61% (RHP p.225; results p.10-11); FY20-FY22 NOT FOUND; median 34.55%, min 16.65%; A1 5, A2 5, A4 5, Block A 17, Core 76, grand total 108 with C-02"
    effect: "Classification GOOD+ unchanged (Core 60-79 + FORTRESS); no deal-breaker change; Block A no longer a weak block; Core 76 is 4 below the 80 line"
    fix: "B01 revision: fixed ROCE formula, FY20-FY22 ROCE NOT FOUND (same window rule B01 applies to B2, B3, B4, M12); align B07 6C and combined_reasoning"
  - id: C-02
    framework: gate0
    rules: "G-35"
    severity: MINOR
    stated: "M8 0, no reach metrics"
    recomputed: "M8 1: 6 dealers (RHP p.173-174), network growth NOT FOUND; moat score 32; moats present 7 unchanged"
    effect: "none on class or classification"
    fix: "B01 revision"
  - id: C-03
    framework: gate0
    rules: "G-47"
    severity: MINOR
    stated: "report ends with abridged block plus pointer line"
    recomputed: "report should end with the full fenced block"
    effect: "presentational"
    fix: "B01 revision"
  - id: C-04
    framework: emoat
    rules: "E-05"
    severity: MINOR
    stated: "13 documented across 5 scan categories plus 3; evidence_mix documented 16, claim 8"
    recomputed: "10 documented across 5 scan categories plus 3 = 13; claims at least 13"
    effect: "no score effect; guard outcome unchanged (2 of 22 active)"
    fix: "B07 recount line and evidence_mix"
  - id: C-05
    framework: emoat
    rules: "E-09"
    severity: MINOR
    stated: "15-row scoring table"
    recomputed: "23 rows"
    effect: "presentational"
    fix: "B07 Section 5"
  - id: C-06
    framework: emoat
    rules: "E-20"
    severity: MINOR
    stated: "anchors 'RHP via B03', '(B04 FLAG-CONCENTRATION)', '(B03)'"
    recomputed: "source page anchors"
    effect: "weak anchor"
    fix: "B07 anchors"
  - id: C-07
    framework: emoat
    rules: "E-21"
    severity: MINOR
    stated: "catalysts_12m item 2 window 12-24 months"
    recomputed: "next-12-month items only; move to optionality register or relabel"
    effect: "risk of over-counted catalyst proximity at Pillar 3 in phase 3"
    fix: "B07 catalysts_12m"
critical_count: 0
major_count: 1
minor_count: 6
acceptance_rate: 87.0             # 60 passed / 69 checked (gate0 42/47, emoat 18/22)
```
