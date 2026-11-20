# VERIFIER A: NUMERICAL ACCURACY, VRLLOG, run 2026-11-12

Model: claude-sonnet-5-5. Inputs: stage reports 01 to 09 (including 02 pass 1, pass 2 and consolidated) and the source files under inputs/. Q2 FY27 results read on the PDF pages (p.4, p.5). Announcement 20261112-888c895a read on PDF pages 1-3. Anchors below use PDF pages unless a column says "printed".

Result: 0 CRITICAL, 3 MAJOR, 5 MINOR. All 140 mandatory-tier figures tie to source. No Gate 0 score changes.

## Findings table

| # | Severity | Report location | Claimed value and anchor | Source truth and location | Note | source_fidelity |
|---|---|---|---|---|---|---|
| 1 | MAJOR | 04-bizmodel.md, Section 3D, last bullet | "A 1% freight rate change equals about Rs 3.2 Cr of quarterly EBITDA at Q2 revenue (961.9 x 1%)" | 961.9 Cr x 1% = Rs 9.62 Cr. The 961.9 base is right (Q2 FY27 results p.4: 96,192 lakh) | The stated inputs do not give the stated result. 3.2 and 9.6 are different numbers. | true |
| 2 | MAJOR | 01-gate0.md, LB1 verdict bullet | "Freight cost to revenue fell to 6.05% in Q2 from 6.27% on freight hikes (presentation p.7)"; stated reason also cited to p.7 | 6.05% and 6.27% are the Hamali (loading and unloading) row, presentation PDF p.9. Freight, handling and servicing cost is 567.8/961.9 = 59.0% vs 480.4/797.0 = 60.3%. The reason text "Increase in Volumes & Freight Rates leads to increase in margins" is on p.9. p.7 is the P&L | Right numbers on the wrong cost line and wrong page. | true |
| 3 | MAJOR | 01-gate0.md, LB1 labelling defect line; LB4 | Balance sheet on presentation p.14 (current investments 280.8). H1 CFO 362.5, CFI -440.5, CFF +74.5, tax paid 54.0 vs 6.8 on p.15 | Balance sheet is PDF p.13 (printed 12). Cash flow is PDF p.14 (printed 13). PDF p.15 is Key Financial Ratios. Values match | ANCHOR NOT FOUND on the cited pages for load-bearing LB4 figures. Net debt 337/440 and capex 158 cited to p.16 are correct. | true |
| 4 | MINOR | 01-gate0.md, D block and LB1, LB3 | EBITDA 673.9 and other income 23.7 (p.33); ROCE chart 30/21/15/21/25 (p.16); record date 22 Oct (p.6) | 673.9 and 23.7: PDF p.32. ROCE chart: PDF p.15. Record date: PDF p.5 (and p.16 text) | Off by one page, values correct. | true |
| 5 | MINOR | 05-concall.md, all call anchors | Anchor key says the [page N] marker. Cites such as Q2 FY27 buyback p.4-5, margin p.6, p.8, capex p.7, ROCE p.9; Q1 FY27 p.10 | The statements exist. They sit at the printed "Page N of 14" number, which is the [page N] marker minus 1. Stage 7 states it uses printed numbers | Declared convention differs from actual use. | true |
| 6 | MINOR | 09-tam.md, Method 2 | TCIEXP Q2 FY27 tonnage 265,000 t, transcript p.2, line 201 | Line 201 is [page 5] (printed Page 4 of 13). Value and +7.5% match | Cited page fits neither convention. | true |
| 7 | MINOR | 03-ardeep.md, LB4 row 4 | MD&A capex 29,805 at p.85, p.87 | 29,805 appears on PDF p.86 (line 4162) and p.87 (line 4204). p.85 is the margin table | One of two cited pages lacks it. Value matches. | true |
| 8 | MINOR | 07-emoat.md, 1B | Contractual customers added (Pres. p.15) | "Addition of New customers including Contractual customers" is PDF p.8. p.15 is Key Financial Ratios | Qualitative claim, no number lost. | true |

Rows struck at self-check (4, class 5a): EBIT FY25 34,477 in Stage 3 against derived 34,478 (the AR MD&A p.84 prints 34,477, faithful); Note 32 lease cash outflow 19,648 against cash flow 19,649 (company prints both); Stage 9 SOM CAGR 11.1% against recomputed 11.05% (rounding); Stage 7 revenue per employee +5.4% against 5.3% (rounding of 15.0 and 14.2). Severity check: no row is a verdict-card or Section 1B pillar input, so no CRITICAL applies.

## What was verified clean (sample of the audit trail)

Gate 0 (mandatory tier):
- Block A. Ten ROCE values rebuilt from screener PBT, interest, share capital, reserves, borrowings: all ten match (17.9, 22.5, 19.3, 13.2, 9.9, 21.2, 24.5, 10.1, 14.9, 18.1). Median 18.0, minimum 9.9. ROE ten values and median 15.6 match, and the AR ties 18.02% and 21.27% sit at AR p.225. Strict FY26 and FY25 ROCE use AR p.170 (260,514 less 41,392) and screener FY25 (2,585.67 less 392.68): match.
- Block B. CFO, CFI and PAT series equal the screener rows. Capex 29,862 and 44,879 and lease flows 13,429, 6,220, 12,072, 6,420 sit at AR p.173. FCF series, cumulative CFO 3,446.73, PAT 1,382.04, FCF 1,668.87 and WC days 11.7, 12.1 and 19.0 vs 14.7 recompute. Payables 32+2,593 and 16+3,070 match AR p.170.
- Block C. Revenue 1,803.09 to 3,221.11 matches (AR p.171: 322,111). CAGRs 6.7% and 14.4% recompute. Eight of nine revenue years positive.
- Block D. EBITDA 658.42 rebuilt from screener cost rows and tied to PBT. Net debt 1,138.51, ratios 1.73x, 4.29x, 1.01, 0.49 match AR p.170 and p.225.
- Block E. Promoter 60.24% and 105,381,942 of 174,936,990 in the XBRL; 12 rows in the NSE master (11 quarter ends plus an 18 Aug 2025 filing), all 60.24. Pledge flags false. Contingent items 359, 70, 2,198, 1,569, 690, 417 sum to 5,303 (AR p.213).
- Block F. Margins 12.2% and 20.4%, FAT 1.40x, CAGRs 6.7% vs 7.7%, branch count 1,293 at AR p.77 and 1,337 at presentation p.16: match.
- LB1 to LB4. Q2 and Q1 results lines, H1 sums, net debt build, leases and capex on results p.4-5 (read from the PDF) match to the lakh.

Stage 2, 3 and pass 1 and 2:
- Face statements (AR p.170, 171, 173), the margin table (p.85-86), tonnage text (p.86), fleet (p.87), Note 20 (credit notes 1,074+110 vs 2,880+550; 2,246 of 6,081; contract price +1.2%), Notes 22, 26, 29, 34A and 34B, the CARO table (14,879 limit; 74, 86, 86; income tax 5,020 breakdown), Note 35 sums (692/2,073 and 788/299), ratios (p.225), DuPont, shareholding (24.34, 2.98, 9.77), vehicles 91,599, land 51,883, commitments 7,984 and 2,888, undrawn 12,700. All match.

Stage 4: per-tonne tables, Q2 YoY per-tonne bridge, incremental margins (41.5%, 34.4%), mix percentages, asset intensity 89.3%, WC 3.2%, presentation p.12, p.20, p.22, p.24, p.25, p.28, p.31 anchors: match. Only the Rs 3.2 Cr line fails (finding 1).

Stage 5: Nov call (EBITDA, margin, realisation, tonnage, net debt, capex, buyback, guidance quotes) and Aug call (net debt 391, 20-21% for 3-4 years, capex 220-240, 8% guide), May call (6-7%, capex 300-350, bus question) and Feb call (10-11%, 350 Cr) quotes match. Anchor convention issue is finding 5.

Stage 6: TCIEXP Q1 (2,50,000 t, +7.5%, p.6), Q2 (265,000 t, 12.7%, 43/339, 1.5% price, pp.4, 5, 8), TCI Q2 (two-thirds pricing, VRL mention, DFC) and the Delhivery 37 and 6 paisa lines match.

Stage 7: scorecard sums (12.8, sensitivity 11.8), turnover 1.887x and 3.516x, 14,525 of 27,182 = 53%, 77 EV and 109 CNG on p.29, ICRA A+ to positive on p.16: match.

Stage 8: buyback terms, 32.88% and 33.11% premium, promoter holdings 28.33% and 31.43%, 63.41% post-buyback, 3.94 times, 20,515 valid bids, HDFC Small Cap 2,189,373 shares at 25.02% (read from the ad on PDF p.2), FY25 AR promoter shares 52,690,441 and 52,690,971, promoter dividend 4,266.51, related-party lines 216.94, 141.39, 112.88: match.

Stage 9: all derived arithmetic (USD conversion, 6,945, 23,150, SAM, SOM, capacity cross-check, headroom 2.16x) reproduces from the stated inputs. Source inputs from the corpus (Rs 3,221.11 Cr on results p.5, 1,293 branches AR p.77) match.

## Coverage statement

Mandatory tier: 140 of 140 figures checked (rule: every Gate 0 scorecard input in 01-gate0.md, counted as: 25 in Block A, 53 in Block B, 14 in Block C, 21 in Block D, 13 in Block E, 14 in Block F). No verdict-card or Section 1B pillar input exists in the reports in front of me, so none is in the tier. No mandatory figure was unchecked.

Sample tier: about 700 material numbers counted by hand (rule: every figure in a load-bearing-fact table, flag reason, findings table, guidance or promise table, or YAML block that feeds a stage judgment; free-text colour excluded). About 420 checked. The universe count is an estimate; the checked count is the count of numbers I compared to a source or re-derived from anchored inputs. Combined: numbers_checked 560, material_universe 840, acceptance rate 95% (about 28 checked numbers or anchors not clean).

Not checked, named: web-sourced items in stages 8 and 9 (Mordor LTL USD 33.01 bn, TCIEXP FY26 revenue 1,236, Delhivery PTL Rs 622 Cr, media-reported promoter block sales, AmbitionBox); Delhivery Q1 and Q2 FY27 transcripts beyond the 37 paisa and 6 paisa lines (one word per line); Q3 and Q4 FY26 concall figures beyond spot checks; BRSR safety counts and board attendance; ICRA rationale items; Stage 6 TCI and Delhivery Q3 and Q4 numbers.

Source-fidelity gate: rows 1 to 8 are flagged source_fidelity true. Only the PDF can clear them, and a clearance is logged as a disagreement.

```yaml
stage: B12a
company: "VRLLOG"
run_date: "2026-11-12"
model: claude-sonnet-5-5
status: complete
numbers_checked: 560
mandatory_checked: 140
mandatory_total: 140
findings:
  - {severity: "MAJOR", location: "04-bizmodel.md Section 3D, last bullet (operating leverage)", claimed: "A 1% freight rate change = about Rs 3.2 Cr of quarterly EBITDA at Q2 revenue (961.9 x 1%)", source_truth: "961.9 Cr x 1% = Rs 9.62 Cr. Revenue base 961.9 Cr is right (Q2 FY27 results p.4, 96,192 lakh). The 3.2 does not follow from the stated inputs", note: "Arithmetic on the report's own anchored input does not reproduce the claimed value. Identity check passed: 3.2 and 9.6 are different numbers.", source_fidelity: true}
  - {severity: "MAJOR", location: "01-gate0.md LB1, verdict bullet: freight cost to revenue 6.05% from 6.27% (presentation p.7)", claimed: "Freight cost to revenue fell to 6.05% in Q2 from 6.27% on freight hikes (presentation p.7); stated reason text also cited to p.7", source_truth: "6.05% and 6.27% are the Hamali (loading and unloading) row on presentation PDF p.9 (Q2 FY27 vs Q2 FY26, % to revenue). Freight, handling and servicing cost is 567.8/961.9 = 59.0% vs 480.4/797.0 = 60.3%. The reason text Increase in Volumes and Freight Rates leads to increase in margins is on p.9, not p.7 (p.7 is the P&L)", note: "Right numbers attached to the wrong cost line and the wrong page. Not a labelled basis difference.", source_fidelity: true}
  - {severity: "MAJOR", location: "01-gate0.md LB1 labelling defect line and LB4 (H1 cash flow, tax paid, current investments, net debt rebuild)", claimed: "Balance sheet on presentation p.14 (current investments 280.8); H1 CFO 362.5, CFI -440.5, CFF +74.5, tax paid 54.0 vs 6.8 on presentation p.15", source_truth: "Balance sheet is PDF p.13 (printed slide 12); cash flow statement is PDF p.14 (printed slide 13). p.14 holds the cash flow and p.15 holds Key Financial Ratios. Values themselves match (280.8; 362.5; -440.5; 74.5; 54.0; 6.8)", note: "ANCHOR NOT FOUND on cited pages for load-bearing LB4 figures. Numbers exist one slide earlier. Neither PDF page nor printed slide number matches the cited page. Net debt 337/440 and capex 158 cited to p.16 are correct.", source_fidelity: true}
  - {severity: "MINOR", location: "01-gate0.md: EBITDA 673.9 and other income 23.7 (p.33); ROCE chart 30/21/15/21/25 (p.16); record date 22 Oct 2026 (p.6)", claimed: "presentation p.33; p.16; p.6", source_truth: "673.9 and 23.7 are on PDF p.32 (printed 31); the ROCE chart is on PDF p.15 (printed 14); record date appears on PDF p.5 (and p.16 text). Values match", note: "Off by one page. Weak anchor, values correct.", source_fidelity: true}
  - {severity: "MINOR", location: "05-concall.md throughout (anchor key says [page N] marker)", claimed: "Q2 FY27 call: buyback p.4-5, 21-22% margin p.6/p.8, capex H2 p.7, ROCE 30% p.9; Q1 FY27 call: 20-21% for 3-4 years p.10", source_truth: "The statements exist and the quotes match, but they sit on printed page numbers (Page N of 14 header), which equal the [page N] marker minus 1. By the declared marker convention the pages are 5-6, 7/9, 8, 10, and 11. Stage 7 says its call anchors use printed pages; stage 5 declares markers", note: "Declared anchor convention contradicts actual use. Quoted figures verified against the Nov and Aug transcripts: EBITDA 226 vs 158, 23.3%, tonnage 976k to 1,079k, realisation 8,079 to 8,840, net debt 337/440/391, capex 158 (76+82), buyback 280 Cr at 320, 87.5 lakh shares, promoters not participating, H2 capex 150-160, 250-300 a year, 21-22%, 23% plus, 1-1.5% leakage, 8% FY27 tonnage guide, 220-240 capex, 9-10% medium term.", source_fidelity: true}
  - {severity: "MINOR", location: "09-tam.md Method 2: TCIEXP Q2 FY27 tonnage 265,000 t cited to transcript p.2, line 201", claimed: "transcript p.2", source_truth: "Line 201 is on [page 5] (printed Page 4 of 13). Value 265,000 tons and +7.5% match", note: "Cited page matches neither marker nor printed number.", source_fidelity: true}
  - {severity: "MINOR", location: "03-ardeep.md LB4 row 4 and Phase 3A: MD&A capex 29,805 (p.85, p.87)", claimed: "p.85, p.87", source_truth: "29,805 lakh appears on PDF p.86 (line 4162) and p.87 (line 4204). p.85 is the margin table", note: "One cited page does not hold it. Value matches.", source_fidelity: true}
  - {severity: "MINOR", location: "07-emoat.md 1B: contractual customers added (Pres. p.15)", claimed: "Pres. p.15", source_truth: "Addition of New customers including Contractual customers is on PDF p.8. p.15 is Key Financial Ratios", note: "Qualitative claim, no number lost. Anchor wrong.", source_fidelity: true}
critical_count: 0
major_count: 3
minor_count: 5
false_positives_struck: 4
material_universe: 840
acceptance_rate: 95
coverage_note: "Mandatory tier: 140 of 140 checked. No verdict-card or Section 1B pillar input exists in the reports in front of me (no stage 10 or 11 output). The tier is the Gate 0 scorecard inputs in 01-gate0.md. Each was re-derived from the screener CSV and tied to AR pages 170, 171, 173, 213, 223-225 and to SHP files; no mismatch. Sample tier: about 700 material numbers counted by hand from stages 2-9, about 420 checked; the universe count is an estimate. NOT CHECKED: web-sourced items in stages 8 and 9; Delhivery Q1 and Q2 FY27 transcripts beyond two lines; Q3 and Q4 FY26 concall figures beyond spot checks; BRSR safety counts and board attendance; ICRA rationale items. Struck before emit (4): EBIT FY25 34,477 vs 34,478; Note 32 19,648 vs 19,649; SOM CAGR 11.1% vs 11.05%; revenue per employee +5.4% vs 5.3%."
```
