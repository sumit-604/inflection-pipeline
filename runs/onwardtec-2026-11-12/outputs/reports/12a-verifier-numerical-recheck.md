# VERIFIER A RE-CHECK: Gate 0 (revised, remediation run 2), ONWARDTEC, 2026-11-12

Scope: runs/onwardtec-2026-11-12/outputs/reports/01-gate0.md and its block B01-gate0.yaml. Sources read from the page-marked .txt beside each PDF (anchored to PDF page markers) and the four screener CSVs. Units: AR and results in INR lakhs, screener in INR Cr, as the report states.

## Result

No MISMATCH, no ANCHOR NOT FOUND. One MINOR UNANCHORED figure (a carried fact the report itself says is outside this run's inputs). The prior CRITICAL (E4 contingent liability) is cleared at source: AR 2026 PDF p.87 Note 26(a)(ii) states "USD 4.20 lakhs (Rs 394.68 lakhs)", Note 26(a)(i) states tax notices are remote and not disclosed, Note 26(c) states financial guarantees Nil. The report now matches all three. 394.68 / 25,350.70 = 1.557%, report says 1.56%.

## Findings

| Severity | Location | Claimed + anchor | Source truth | Note | source_fidelity |
|---|---|---|---|---|---|
| MINOR | Load-bearing facts 2 and 4; block data_notes | "Mar 2021 61.71%" promoter holding, no anchor (report states it is not in this run's inputs) | 61.71 appears nowhere in inputs/ (grep, zero hits) | Not scored, not used in any block, and the report labels it as not held. Carried from the Step-1 fact list, unanchored in this run. | false |

## Verified (all MATCH)

Block A, AR 2025 PDF p.113-114 and AR 2026 p.65:
- FY24 PBT 4,515.70, finance costs 134.09, total assets 28,694.14, current liabilities 5,262.68 (p.113-114). EBIT 4,649.79; capital employed 23,431.46; ROCE 4,649.79/23,431.46 = 19.84%.
- FY25 PBT 3,629.98, finance 222.25, total assets 31,375.51, CL 5,647.93 (AR 2026 p.65, same as AR 2025 p.113-114). EBIT 3,852.23; CE 25,727.58; ROCE 14.97%.
- FY26 PBT 5,704.58 (after exceptional 315.50), finance 289.05, total assets 37,056.82, CL 7,180.16. EBIT 5,993.63; CE 29,876.66; ROCE 20.06%.
- Median 19.84, min 14.97. S6 ROCE ex other income (other income 727.24, 721.31, 704.23): 16.74, 12.17, 17.70, all recompute.
- ROE series (screener, avg net worth, FY17 closing): 9.67, 14.57, 18.28, 9.67, 10.30, 19.93, 6.81, 17.81, 12.55, 18.55 all recompute; median 13.56. FY26 cross-check 4,432.39 / avg(25,350.70, 22,430.10) = 18.55%.
- Company ROCE 25.42% at AR 2026 p.47 (line sits between page 47 and page 48 markers); correctly marked as not used.

Block B:
- CFO FY24 6,234.87 (AR 2025 p.115), FY25 3,152.30, FY26 6,507.73 (AR 2026 p.66). PPE 128.55 / 237.73 / 1,804.97; intangibles 73.15 / 129.28 / 106.10. Capex 201.70 / 367.01 / 1,911.07; FCF 6,033.17 / 2,785.29 / 4,596.66; cumulative 13,415.12.
- PAT 3,391.77 (AR 2025 p.114), 2,707.77, 4,432.39; cumulative 10,531.93; ratio 1.27. CFO/PAT 1.84, 1.16, 1.47.
- B1 screener: cumulative CFO 263.84, cumulative PAT 175.01, 1.51.
- Receivables billed+unbilled 10,086.11 / 10,941.35 / 11,999.70; trade payables 1,297.28 / 929.71 / 1,192.23; revenue 47,239.17 / 49,131.61 / 54,385.24. Days 77.93 / 81.28 / 80.53; payable days 10.02 / 6.91 / 8.00; WC days 67.91 / 74.37 / 72.53; delta +4.62. No inventory line on the balance sheet (p.65).

Block C (screener): sales 223.56 to 543.85, CAGR 10.38%; PAT 4.10 to 44.32, CAGR 30.3%; FY21 271.55 to 240.37, 8 of 9 up years; spread 19.9pp; FY21 change -11.5%.

Block D: borrowings 39.84 Cr = lease liabilities 2,933.81 + 1,050.52 = 3,984.33 lakhs (AR 2026 p.65-66; p.66 closing 3,984.33); cash 3,685.66 + bank 7,408.88 = 11,094.54 (110.95 Cr); equity 25,350.70; D3 0.157; current assets 26,302.17 / CL 7,180.16 = 3.66; EBIT/finance 20.74x. AR 2025 p.116 reconciliation shows borrowings nil at both year-ends.

Block E: SHP Q2 FY27 p.3 promoter 40.20% and fully diluted 39.54%; p.2 row 7 pledge "No". LoO 39.07% at p.21 (line 1113, between p.21 and p.22 markers) and p.31. AR 2025 p.147: Mar 2024 33.74+0.96+1.67+1.08+0.67 = 38.12; Mar 2025 34.16+0.97+1.76+1.10+0.66 = 38.65. AR 2026 p.81: 34.98+0.98+1.78+1.11+0.76 = 39.61. Sep 2023 not in corpus (NOT FOUND stands). E4 as above. Sensitivity delta 40.20 - 38.12 = 2.08.

Block F: Onward EBITDA FY17 11.20 (5.01%), FY26 71.85 (13.21%) built as PBT + interest + depreciation - other income; also equals sales less listed costs. Peers: LTTS 1,935.0/10,995.9 = 17.60%; TATATECH 852.95/5,505.57 = 15.49%; CYIENT 899.1/7,268.2 = 12.37%; median 15.49; gap 2.28pp. FAT 543.85/88.86 = 6.12x. M4 receivable days 79.3 (FY17 48.54/223.56) and 80.5 (FY26 120.0/543.85). M5 mcaps 841.82, 45,281.89, 27,753.70, 12,107.48. M9: LTTS 100, TATATECH (5,505.57-967.19)/5,505.57 = 82.43, CYIENT (7,268.2-812.8+26.6)/7,268.2 = 89.18, median 89.18, +10.82pp. M11: 3y CAGR 7.2% and 17.5%.

Load-bearing facts: Q2 FY27 operating profit 26.54 / sales 170.18 = 15.6% (screener quarters); R&D credit 292.60 lakhs (Results Q2FY27 p.3, standalone note p.9 too); ex-credit 23.61/170.18 = 13.87%; exceptional 315.50 lakhs (AR 2026 p.65; Q2 FY27 p.2-3).

## Rule 5a/5b self-check
No CRITICAL or MAJOR rows written; zero rows struck. Run 1 findings were not carried here. The company's own ROCE definition (25.42%) versus the computed rule ROCE is a labelled basis difference, not a finding. Scores and band calls (rule application) are Verifier C's; I checked the arithmetic that feeds them and the block and core sums (13+18+16+19+13 = 79).

## Coverage
Mandatory tier: 163 of 163 checked (every Gate 0 scorecard input, intermediate and result for Blocks A to E and the Block F evidence cells, plus the load-bearing facts in the report). None unchecked. Count method: each distinct source figure and each reported derived value that feeds a scored input.
Sample tier: 4 material numbers outside the mandatory list (company ROCE 25.42%, nil borrowings reconciliation, FY21 -11.5%, Mar 2021 61.71%); 4 checked. Material = any figure that feeds a score, a sensitivity or a load-bearing fact. The screened-out text (scores, band edges, sensitivity class labels) is rule application, not source numbers.
Not read: Q1 FY27 results PDF (scanned; the report does not cite it).
