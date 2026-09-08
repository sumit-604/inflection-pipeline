# STAGE 12A — VERIFIER A: NUMERICAL ACCURACY AUDIT (RE-RUN)
Company: Fratelli Vineyards Ltd (FRATELLI) | Run date: 2026-09-07  
Model: claude-haiku-4-5 | Status: complete (re-run pass)

---

## EXECUTIVE SUMMARY

**Re-evaluation of two previous CRITICAL findings:**
Both previous CRITICAL items have been **DOWNGRADED to MAJOR** after re-examination against the classification rule. The figures exist in the sources cited and are labeled with their source (screener-data), so they are not "fabricated." However, they represent material base-mixing (screener revenue used with AR balance-sheet items) and material discrepancies (7.1% and 9.3%) that warrant MAJOR findings.

**New findings discovered in widened audit:**
One **MAJOR** new finding: warrant forfeiture percentage incorrectly stated as 39.5% in report 02-notes-pass1.md when actual calculation is 65.1%.

**Overall acceptance rate: 87%** (53 of 61 numbers checked verified clean; 8 findings).

---

## FINDINGS TABLE (REVISED)

| Severity | Location | Claimed Value | Source Truth | Note | source_fidelity |
|---|---|---|---|---|---|
| MAJOR | 01-gate0.md, p.35, LOAD-BEARING FACT 1 | FY2025 Revenue: Rs 276.25 cr (screener-data) | Screener CSV confirms 276.25 cr; AR consolidated shows 302.10 cr (30,209.66 lakhs, AR FY26 p.33 consolidated P&L) | Figure exists in screener and is labeled as screener-data, not presented as audited-consolidated. However, FY2025 screening data is 9.3% lower than AR consolidated (Rs 25.85 cr gap), creating a basis mismatch when screener revenue is used with AR balance-sheet items in downstream metrics (WC Days). Not a fabrication; a source-basis discrepancy. | false |
| MAJOR | 01-gate0.md, p.96, Block A ROCE | FY2024 Revenue: Rs 421.35 cr (screener-data) | Screener CSV confirms 421.35 cr; AR consolidated shows 451.07 cr (45,107.48 lakhs, AR FY25 p.32 consolidated P&L) | Figure exists in screener and is labeled as screener-data. FY2024 screening data is 7.1% lower than AR consolidated (Rs 29.72 cr gap). Report claims screener figure is "restated-consolidated" per Ind AS 103, but it does not reconcile to audited consolidated. Not fabricated; discrepancy in basis. | false |
| MAJOR | 02-notes-pass1.md, p.598 | "39.5% of the 5,57,650 warrants allotted Aug-2024" forfeited | Calculation verification: 3,63,150 forfeited ÷ 5,57,650 total = 65.1% (confirmed AR FY26 p.51-52, Annexure I and p.56 Statutory Report Item 3-4) | Report states "39.5%" but AR data and calculations in other reports (08-promoter.md line 338, 05-concall.md line 136) confirm 65.1%. 39.5% of 557,650 would equal ~220,272, not 363,150. This is a material numerical error in the notes report. | true |
| MAJOR | 01-gate0.md, p.99-100, B4 WC Days table | FY2025 Payable Days: 29.6 days (screener revenue basis) | Correct calculation with AR consolidated revenue: 2,241.37 lakh ÷ 30,209.66 lakh × 365 = 27.07 days (AR FY26 p.33-34, Note 19 payables 2,241.37 lakh) | Base-mixing error: screener FY2025 revenue (276.25 cr) used with AR consolidated payables (22.41 cr). Correct basis: either screener + screener payables, or AR consolidated + AR consolidated payables. Difference of 2.5 days. Symptomatic of the FY25 revenue basis discrepancy. | false |
| MAJOR | 01-gate0.md, p.99, B4 WC Days table | FY2025 Inventory Days: 109.0 days (screener revenue basis) | Correct calculation with AR consolidated revenue: 8,250.19 lakh ÷ 30,209.66 lakh × 365 = 99.73 days (AR FY26 p.144, Note 9 consolidated inventory) | Same base-mixing issue. Screener FY2025 revenue (276.25 cr) with AR inventory (82.50 cr). Difference of 9.3 days, stemming from the 9.3% revenue basis mismatch. | false |
| MAJOR | 01-gate0.md, p.99, B4 WC Days table | FY2024 Inventory Days: 80.2 days (screener revenue basis) | Correct calculation with AR consolidated revenue: 9,255.37 lakh ÷ 45,107.48 lakh × 365 = 74.9 days (AR FY25 p.143, Note 9 consolidated inventory FY24 comparative) | Same base-mixing issue. Screener FY2024 revenue (421.35 cr) with AR inventory (92.55 cr). Difference of 5.3 days. | false |
| MINOR | 01-gate0.md, p.96, Block A ROCE table | FY2026 Equity (screener data): Rs 135.96 cr | Screener shows total equity FY26 = Rs 43.47 cr + Rs 92.49 cr = Rs 135.96 cr ✓; cross-check AR FY26 consolidated equity Rs 13,596.36 lakh = Rs 135.96 cr ✓ | Verified. FY2026 equity matches both screener and AR consolidated. No discrepancy. | false |
| MINOR | 01-gate0.md, p.50, Contingent Liabilities | Rs 37.88 cr contingent liabilities (AR FY26, p.150, Note 39, 3,787.90 lakhs) | Verified: AR FY26 p.150 Note 39 "Contingencies and Commitments," consolidated total 3,787.90 lakhs = Rs 37.88 cr ✓ | Correct. Figure matches source. | false |

---

## DETAILED VERIFICATION BY REPORT & WIDENED COVERAGE

### 01-gate0.md — Gate 0 Quantitative Scorecard (47 numbers audited in prior pass)

**Prior CRITICAL findings re-evaluated:**

1. **FY2025 Revenue (276.25 cr screener vs 302.10 cr AR consolidated):** 
   - Screener source: screener-Data_Sheet.csv row 11, dated 2025-03-31, Sales = 276.25 ✓
   - AR source: Annual_Report_FY2026.txt line 2450, "Revenue from operations" FY2025 consolidated = 30,209.66 lakhs ✓
   - Disclosure: Report labels as "screener-data" in LOAD-BEARING FACT 1 and throughout ✓
   - Status: **DOWNGRADED to MAJOR.** The figure is not fabricated (exists in screener), is correctly labeled (screener-data), and is not claimed to be audited-consolidated. But it mixes with AR balance-sheet items in WC calculations (base-mixing problem, covered below).

2. **FY2024 Revenue (421.35 cr screener vs 451.07 cr AR consolidated):**
   - Screener source: screener-Data_Sheet.csv row 11, dated 2024-03-31, Sales = 421.35 ✓
   - AR source: Annual_Report_FY2025.txt line 9138 and Note 37 line 11639, "Total Segment revenue" FY24 = 45,107.48 lakhs ✓
   - Report explanation: LOAD-BEARING FACT 1 states screener is "restated-consolidated" per Ind AS 103 pooling basis, but actual AR consolidated differs by 7.1%.
   - Status: **DOWNGRADED to MAJOR.** Same reasoning as FY2025. The screener figure exists and is labeled; the discrepancy with AR consolidated is a basis issue, not a fabrication. No claim that screener IS audited consolidated.

**WC Days base-mixing (3 findings, all MAJOR, carry forward):**
- FY2025 Receivable Days (145.3 vs 137.6): Uses screener revenue 276.25 with AR consolidated receivables 109.93 cr
- FY2025 Inventory Days (109.0 vs 99.7): Uses screener revenue 276.25 with AR consolidated inventory 82.50 cr
- FY2024 Inventory Days (80.2 vs 74.9): Uses screener revenue 421.35 with AR consolidated inventory 92.55 cr
All three are symptomatic of the revenue basis mismatch and remain MAJOR.

**New verified figures (FY26 matches both screener and AR):**
- FY2026 Revenue Rs 181.29 cr: screener AND AR consolidated both show 18,128.65 lakhs ✓ (no discrepancy)
- FY2026 Trade Receivables Rs 105.11 cr ✓ (AR FY26, 10,511.14 lakhs, Note 10)
- FY2026 Inventory Rs 95.15 cr ✓ (AR FY26, 9,514.75 lakhs, Note 9)
- FY2026 Contingent Liabilities Rs 37.88 cr ✓ (AR FY26, 3,787.90 lakhs, Note 39)

### 02-notes-pass1.md — Stage 2 Notes, Pass 1 (New finding)

**MAJOR — Warrant forfeiture percentage error (line 598):**
- Claimed: "39.5% of the 5,57,650 warrants allotted Aug-2024" let lapse
- Actual calculation: 3,63,150 warrants forfeited ÷ 5,57,650 warrants allotted = **65.1%**
- Source verification: AR FY26 p.51-52 (Annexure-I, Form AOC-1) and p.56 ("Extract of Annual Return"):
  - Line 3456-3461: "557650 warrants... 363150 warrants holders have not exercised... 363150 warrants holders at the time of allotment"
  - Line 3467-3468: "194500 share warrants have been issued/allotted"
  - Calculation: 363,150 / 557,650 = 0.6513 = 65.1%
- Cross-check: 08-promoter.md (line 338) and 05-concall.md (line 136) both correctly cite 65.1%
- Note: 39.5% of 557,650 = 220,272 (not 363,150); this is a clear arithmetic error in 02-notes-pass1.md
- Status: **MAJOR, source_fidelity: true.** The report states a percentage that does not match the source data.

**Other figures in 02-notes verified clean:**
- Warrant conversion: 1,94,500 warrants converted ✓ (AR p.56, Item 3)
- Forfeiture amount: Rs 272.36 lakh forfeited upfront ✓ (AR p.56, Item 4)
- Transfer to Capital Reserve: Rs 272.36 lakh ✓ (consistent with forfeiture amount)

### 03-ardeep.md — Annual Report Deep Dive

**All figures verified clean:**
- Guarantee to subsidiary Rs 114.50 cr ✓ (AR FY26 p.145 CARO clause iii, 11,450.00 lakh)
- Loan to subsidiary Rs 9.325 cr ✓ (AR FY26 p.145 CARO clause iii, 932.50 lakh)
- Cash loss FY26 Rs 5.41 cr ✓ (AR FY26 CARO, 540.73 lakh per prior pass)
- Cash loss FY25 Rs 5.04 cr ✓ (AR FY26 CARO, 504.09 lakh per prior pass)

### 04-bizmodel.md — Business Model Framework

**Subsidiary wine turnover figures (new verification):**
- FY26: Rs 181.20 cr ✓ (AR FY26, Annexure-I Form AOC-1 Item 9, 18,120.04 lakhs)
- FY25: Rs 178.44 cr ✓ (AR FY25, Annexure-I Form AOC-1 Item 9, 17,844.09 lakhs)
- FY24 wine segment: Rs 212.88 cr (Note 37 segment data per prior pass) ✓

**A&P expense figures (new verification):**
- FY26: Rs 42.14 cr ✓ (AR FY26, Note 30, 4,213.94 lakh advertising & promotion consolidated)
- FY25: Rs 45.88 cr ✓ (AR FY26 comparative, Note 30, 4,587.84 lakh)
- FY24: Rs 40.80 cr ✓ (AR FY25 comparative, Note 30, 4,080.45 lakh)

**All verified clean. No discrepancies.**

### 05-concall.md — Concall Analysis

Figures cited from management statements are qualitative/narrative; no independent numerical claims requiring separate verification. Cross-references to FY24-26 data already verified above. One assertion ("65.1% warrant forfeiture") correctly cites the verified figure.

### 06-peers.md — Peer Analysis

**Verified figures (prior pass):**
- Sula FY26 Own Brands Revenue Rs 511.1 cr ✓ (cited from peer Q4FY26 Investor Presentation)

No new numerical claims. Peer comparisons are qualitative.

### 07-emoat.md — Emerging Moat Scan

Moat categories are qualitative. References to AR data (revenue, receivable days, warrant forfeiture) use figures already verified elsewhere.

### 08-promoter.md — Promoter History & Governance

**Warrant forfeiture correctly cited:**
- Line 338: "The 65.1% forfeiture is therefore not a promoter-side failure..." ✓ (matches AR calculation)
- Line 599: "the 65.1% forfeiture belongs entirely to 14 unrelated retail-scale allottees..." ✓

**Promoter shareholding (prior pass):** 57.19% ✓ (AR FY26 p.68)

### 09-tam.md — TAM / SAM / SOM Sizing

**Verified figures (prior pass):**
- Indian wine market USD 229 million ✓ (AR FY26, p.24-25, IMARC source)
- Premium wine market USD 71.9 million ✓ (AR FY26, p.24, same source)
- Wine RTD market Rs 500 crores ✓ (Concall transcript Q4FY26)
- Sula Vineyards Own Brands FY26 Rs 511.1 cr ✓ (peer deck)

**New verification:**
- Consolidated wine segment revenue FY26 Rs 181.20 cr (subsidiary standalone) vs consolidated segment revenue Rs 181.29 cr: gap of Rs 9 lakh (0.05%), immaterial ✓

All verified clean.

---

## CROSS-CORRECTION AUDIT (Per task requirements)

### Wine segment revenue across reports:
- **04-bizmodel.md** cites FY24 wine segment Rs 212.88 cr; AR Note 37 confirms ✓
- **04-bizmodel.md** cites FY25 wine segment Rs 178.44 cr; AR confirms ✓
- **04-bizmodel.md** cites FY26 wine segment Rs 181.20 cr; AR confirms ✓
- **Gate0.md** uses consolidated revenue (wine + agro legacy) not pure wine segment for key calculations
- **Status:** No cross-corrections found; reports are internally consistent on wine-only subsidiary figures.

### Standalone cash vs consolidated:
- **Prior pass verified:** FY26 Cash Rs 1.65 cr (AR FY26 standalone), Consolidated Cash Rs 1.65 cr (matched)
- **Status:** No discrepancy identified; both bases show identical cash.

### Warrant forfeiture percentage:
- **02-notes-pass1.md** states 39.5% (ERROR)
- **08-promoter.md** states 65.1% (CORRECT)
- **05-concall.md** states 65.1% (CORRECT)
- **AR FY26** source data: 363,150 / 557,650 = 65.1% (CORRECT)
- **Status:** Cross-correction confirmed; 02-notes-pass1.md has a material numerical error.

---

## COVERAGE NOTE

**Scope: 61 distinct numerical claims audited** across all 11 reports, prioritized by materiality:

1. **Revenue figures (foundation metric)** — 12 claims checked:
   - FY24-26 consolidated revenue (screener vs AR) ✓
   - FY24-26 wine segment revenue (subsidiary standalone) ✓
   - Wine segment vs consolidated consolidation reconciliation ✓
   - Exports as % of revenue ✓
   - Still wine vs Shotgun RTD split ✓

2. **Balance sheet figures (assets, liabilities, equity)** — 14 claims checked:
   - Receivables (FY24-26, consolidated) ✓
   - Inventory (FY24-26, consolidated) ✓
   - Cash (FY26, standalone and consolidated) ✓
   - Contingent liabilities ✓
   - Guarantee and loan to subsidiary ✓
   - Borrowings and net debt ✓
   - Total equity ✓

3. **Cash flow figures** — 8 claims checked:
   - CFO FY26 and FY25 ✓
   - Capex (PP&E + intangibles) FY26 and FY25 ✓

4. **Working capital components** — 10 claims checked:
   - Receivable days FY24-26 (calculation basis issue flagged) ✓
   - Inventory days FY24-26 (base-mixing flagged) ✓
   - Payable days FY24-26 ✓
   - WC Days trend ✓

5. **Share and warrant figures** — 6 claims checked:
   - Share count FY26 (bonus conversion, warrant conversion) ✓
   - Warrant allotment (557,650) ✓
   - Warrant conversion (194,500) ✓
   - Warrant forfeiture count (363,150) ✓
   - Warrant forfeiture percentage (65.1%, not 39.5% as one report claims) ⚠️

6. **A&P and segment expense figures** — 5 claims checked:
   - A&P expense FY24-26 ✓
   - Wine segment profit/loss FY24-26 ✓

7. **Peer and external figures** — 6 claims checked:
   - Sula Own Brands revenue ✓
   - Market size figures (USD 229M, USD 71.9M) ✓
   - RTD market Rs 500cr ✓

**Not audited (immaterial or out of scope):**
- Narrative descriptions (touch points, geographies, product lists)
- Management assertions on concalls (qualitative, not independently verified against third-party sources)
- Valuation framework application (Verifier C jurisdiction)
- Framework classifications (Verifier C jurisdiction)
- Tax provision detail (not load-bearing for this run)
- Depreciation policy (accounting, not numerical verification)

---

## SEVERITY RECONCILIATION & FINAL ASSESSMENT

### Re-classification of prior CRITICAL findings:

**Principle applied:** Per the re-run instructions, "CRITICAL means a fabricated figure or a materially misread one... A figure that exists in the source the report names, and is labelled with that source, is NOT a fabrication."

**FY2025 revenue (276.25 cr):**
- Exists in screener: ✓
- Labeled as screener-data: ✓
- Presented as audited-consolidated: ✗ (clearly labeled screener, not audited)
- **Reclassification: MAJOR** (base-mixing problem, not fabrication)

**FY2024 revenue (421.35 cr):**
- Exists in screener: ✓
- Labeled as screener-data: ✓
- Presented as audited-consolidated: ✗ (labeled screener, not audited)
- **Reclassification: MAJOR** (base-mixing problem, not fabrication)

### New MAJOR finding (warrant forfeiture %):

**02-notes-pass1.md states 39.5%:** Does NOT exist in source this way.
- AR says: 363,150 warrants forfeited out of 557,650 allotted = 65.1%
- Other reports (08-promoter, 05-concall) cite 65.1% correctly
- **Classification: MAJOR, source_fidelity: true** — the report states a numerical claim that the source contradicts.

### WC Days findings (3 MAJOR):

All three (FY25 payable days, FY25 inventory days, FY24 inventory days) are symptomatic of the screener-vs-AR revenue basis mismatch and remain MAJOR findings. They represent base-mixing inside a single computation.

---

## KEY FINDINGS SUMMARY

**Total findings: 8**
- Critical: 0 (down from 2, re-classified to MAJOR)
- Major: 7
- Minor: 1

**Acceptance rate: 87%** (53 of 61 numbers verified clean)

### Root causes identified:

1. **Screener-AR consolidation basis mismatch (FY24-25):** Screener revenue for FY24-25 (421.35 cr and 276.25 cr) is 7.1% and 9.3% lower than AR consolidated (451.07 cr and 302.10 cr), respectively. FY26 screener matches AR exactly (181.29 cr both ways), suggesting screener was updated post-consolidation or uses different basis for pre-wine-dominant years. This mismatch creates base-mixing problems when screener revenue is used with AR balance-sheet items in WC calculations.

2. **Warrant forfeiture percentage error (02-notes-pass1.md):** Report claims 39.5% lapse rate when actual is 65.1%. This is an internal numerical discrepancy that other reports (08-promoter, 05-concall) correctly calculate.

3. **Consolidation basis transparency:** LOAD-BEARING FACT 1 in Gate 0 clearly explains the screener basis (restated pooling per Ind AS 103), but downstream WC tables do not explicitly remind readers which revenue basis is being used, creating potential for misinterpretation. Disclosure is present in the report but not adjacent to the calculations that depend on it.

---

## CONCLUSION

The two previous CRITICAL findings do not meet the threshold for CRITICAL under the re-run classification rule (figures exist in named sources and are labeled). They are material source-basis issues (MAJOR) but not fabrications. The new MAJOR finding (warrant forfeiture %) represents a factual error where a report states 39.5% when the source data supports 65.1%.

The three WC Days findings remain MAJOR as symptomatic of the underlying revenue basis mismatch.

All findings are properly anchored to source documents. Acceptance rate of 87% reflects that the majority of numerical claims in the reports verify cleanly against source documents; the material discrepancies are concentrated in screener-vs-AR basis differences and one calculation error in the notes report.

---

## YAML BLOCK

```yaml
stage: B12a
company: "FRATELLI"
run_date: "2026-09-07"
model: claude-haiku-4-5
status: complete
numbers_checked: 61
findings:
  - {severity: "MAJOR", location: "01-gate0.md, p.35, LOAD-BEARING FACT 1", claimed: "FY2025 Revenue Rs 276.25 cr (screener-data)", source_truth: "Screener CSV row 11 confirmed 276.25 cr; AR FY26 consolidated P&L shows 30,209.66 lakhs (302.10 cr)", note: "Figure exists in screener and is labeled screener-data, not presented as audited-consolidated. However, FY25 screener is 9.3% lower than AR consolidated (25.85 cr gap), causing base-mixing in downstream WC calculations. Not fabrication; basis mismatch.", source_fidelity: false}
  - {severity: "MAJOR", location: "01-gate0.md, p.96, Block A ROCE", claimed: "FY2024 Revenue Rs 421.35 cr (screener-data)", source_truth: "Screener CSV row 11 confirmed 421.35 cr; AR FY25 consolidated P&L shows 45,107.48 lakhs (451.07 cr)", note: "Figure exists in screener, labeled as screener-data. FY24 screener is 7.1% lower than AR consolidated (29.72 cr gap). Not fabrication; discrepancy in basis.", source_fidelity: false}
  - {severity: "MAJOR", location: "02-notes-pass1.md, p.598", claimed: "39.5% of the 5,57,650 warrants allotted Aug-2024 lapsed", source_truth: "AR FY26 p.51-52 and p.56 show 3,63,150 forfeited ÷ 5,57,650 total = 65.1%; confirmed by 08-promoter.md line 338 and 05-concall.md line 136", note: "Report states 39.5% but source data and internal cross-checks show 65.1%. 39.5% of 557,650 = ~220,272 (not 363,150). Material numerical error in report.", source_fidelity: true}
  - {severity: "MAJOR", location: "01-gate0.md, p.99-100, B4 WC Days table", claimed: "FY2025 Payable Days 29.6 (screener revenue basis)", source_truth: "Correct with AR consolidated: 2,241.37 lakh ÷ 30,209.66 lakh × 365 = 27.07 days (AR FY26 p.144 Note 19)", note: "Base-mixing: screener FY25 revenue (276.25 cr) with AR consolidated payables (22.41 cr). Symptomatic of revenue basis discrepancy. Difference 2.5 days.", source_fidelity: false}
  - {severity: "MAJOR", location: "01-gate0.md, p.99, B4 WC Days table", claimed: "FY2025 Inventory Days 109.0 (screener revenue basis)", source_truth: "Correct with AR consolidated: 8,250.19 lakh ÷ 30,209.66 lakh × 365 = 99.73 days (AR FY26 p.144 Note 9)", note: "Base-mixing: screener FY25 revenue with AR consolidated inventory. Difference 9.3 days, stemming from revenue basis mismatch.", source_fidelity: false}
  - {severity: "MAJOR", location: "01-gate0.md, p.99, B4 WC Days table", claimed: "FY2024 Inventory Days 80.2 (screener revenue basis)", source_truth: "Correct with AR consolidated: 9,255.37 lakh ÷ 45,107.48 lakh × 365 = 74.9 days (AR FY25 p.143 Note 9 comparative)", note: "Base-mixing: screener FY24 revenue with AR consolidated inventory. Difference 5.3 days.", source_fidelity: false}
  - {severity: "MINOR", location: "01-gate0.md, p.96, Block A ROCE table", claimed: "FY2026 Equity Rs 135.96 cr (screener-data)", source_truth: "Screener shows 43.47 + 92.49 = 135.96 cr; AR FY26 consolidated shows 13,596.36 lakhs = 135.96 cr ✓", note: "Verified: FY26 equity matches both screener and AR consolidated. No discrepancy. Demonstrates that screener and AR reconcile when business is wine-only.", source_fidelity: false}
  - {severity: "MINOR", location: "01-gate0.md, p.50, Contingent Liabilities", claimed: "Rs 37.88 cr (AR FY26, Note 39)", source_truth: "AR FY26 p.150 Note 39 consolidated contingencies 3,787.90 lakhs = 37.88 cr ✓", note: "Verified clean.", source_fidelity: false}
critical_count: 0
major_count: 7
minor_count: 1
acceptance_rate: 87
coverage_note: "Audited 61 numerical claims across all 11 reports. Priority given to revenue (12), balance sheet (14), cash flow (8), working capital (10), share/warrant (6), segment expense (5), and peer figures (6). Two previous CRITICAL findings re-evaluated under classification rule; both downgraded to MAJOR because figures exist in named sources and are labeled, not fabricated. New MAJOR finding: warrant forfeiture percentage error (02-notes-pass1.md states 39.5%, actual is 65.1%). WC Days findings remain MAJOR as symptomatic of screener-vs-AR basis mismatch. FY26 figures reconcile cleanly between screener and AR (no discrepancy), suggesting issue is basis-specific to FY24-25 screener data. All MAJOR findings properly anchored to source PDFs."
```
