# VERIFIER A: NUMERICAL ACCURACY, JLHL, run 2026-11-12

Model: claude-sonnet-5-5. Inputs read: the 11 stage reports and the source documents named in the task. Page numbers below are PDF pages of the .txt page markers unless marked "printed".

## Findings table

| # | Severity | Report location | Claimed value + anchor | Source truth + location | Note | source_fidelity |
|---|---|---|---|---|---|---|
| 1 | MAJOR | 01-gate0.md, Block C caution | FY26 tax rate 25.7% (66.25 / 260.44), screener-data | 66.25 / 260.44 = 25.44% (screener FY26 Tax 66.25, PBT 260.44). AR26 p.192 C: 662.49 / 2,604.36 = 25.44%. 25.7% is the FY25 rate (66.93 / 260.68 = 25.68%) | FY25 rate set against FY26 inputs. Not a scored input. FY24 9.6% comparison is correct. | true |
| 2 | MAJOR | 01-gate0.md, Block B capex FY21-FY23 | 2,415.89 / 917.32 / 772.44 Mn, "RHP restated cash flow p.76" | Same values on RHP PDF p.77 (printed folio 70). PDF p.76 is the Restated P&L | ANCHOR NOT FOUND at p.76. Feeds B2 and B3. Values exact. | true |
| 3 | MAJOR | 01-gate0.md, Block B capex FY24 | 852.95 Mn, "AR 2025 consolidated cash flow, printed p.167" | Annual_Report_2025.pdf PDF p.86, printed folio 166 | ANCHOR NOT FOUND at printed p.167. Value exact. | true |
| 4 | MAJOR | 09-tam.md, Method 1, Method 5, 4A | MMR 33.0, 20.96 M, 69,000 beds, Kalyan-Dombivli 10/10,000 and 1,500 beds at "RHP p.178"; global median 29 beds at "p.172"; ARPOB CAGR 10.7% at "p.174"; US$56.6 at "p.138" | MMR: PDF p.184-185. Kalyan-Dombivli: PDF p.185. PDF p.178 holds physician and nurse data. 29-bed median: PDF p.147 and p.176. 10.7%: PDF p.181. US$56.6: PDF p.145 | Values correct. Anchors mix printed folios (these) with PDF pages (p.163, p.164, p.185, p.186 in the same report), unlabelled. | true |
| 5 | MINOR | 01-gate0.md, E2 | RHP "p.~240" shows promoters 40.69% | 40.69% (23,677,415 shares) is at PDF p.260; p.239-240 hold director profiles | Approximate anchor, wrong page. E2 score does not rest on it. | true |

critical_count 0, major_count 4, minor_count 1.

## Self-check (rule 5b)

Rows struck: 4.
1. C1 21.65% and C2 36.77%, S&A % 28.55%, FY21 EBITDA margin 13.82%: my recomputation gives 21.64%, 36.78%, 28.54%, 13.81%. Differences of 0.01pp are rounding of one value. Struck as matched.
2. Gate 0 ROCE 13.77% against the AR's printed consolidated ROCE 18.55% (C Note 36L p.233-234): Gate 0 labels its ROCE as computed with its formula and cross-checks it on the same formula (13.82%). A labelled basis difference. Struck. Gap for the reader: Gate 0 never names the AR's 18.55%.

Rows kept were tested against 5a. Each has a claimed value that differs from the source value or a cited page that does not hold the number. None is a pillar input MISMATCH, so none is CRITICAL.

## What matched (mandatory tier, Gate 0)

All 32 scored lines (A1-A4, B1-B4, C1-C4, D1-D4, E1-E4, M1-M12) recomputed or located.
- Block A: ROCE for FY20-FY26 recomputed from screener PBT, interest, total assets and other liabilities: 11.52, 6.10, 15.35, 20.49, 18.97, 15.51, 13.77. Net worth and ROE series match. AR cross-check 13.82% matches (AR26 p.191, p.192: 2,653.23 + 326.62 over 23,831.29 less 2,265.75).
- Block B: CFO series and sum 1,159.96, PAT sum 715.19, FCF series and -239.55, payables (RHP p.75; AR25; AR26 p.191), receivable, inventory, payable days and WC days all match. CFO ties to AR26 p.193 (2,677.08 and 2,667.39). Capex values match (anchors at findings 2 and 3).
- Block C: growth ratios match to rounding.
- Block D: 1.53x, 0.12x sensitivity, 8.97x, 0.38 and 0.33, 3.02 all match; AR26 p.47 ratios (7.82, 0.33, 3.02, EBITDA 343.3) match.
- Block E: 40.91%, 134,128,115 shares, MF 13.45, insurance 2.10, FPI 9.13, DII 19.13, pledge false, all in the XBRL. Contingent 49.26 / 15,440.93 = 0.32% matches (AR26 p.223, p.191). AR25 40.91% at p.50.
- Moat: peer EBITDA margins (KIMS 815.1, Medanta 930.03, Yatharth 304.83), peer median 21.09, market caps, gross-margin proxies (80.85, 80.57, 77.40), receivable days 35.17, beds 1,061 to 1,259, selling and admin 26.84%, all match.
- Load-bearing facts 1-4: Q2 FY27 presentation p.5-9 matches (9.5, 0.2, 9.7, 59.5%, 64.8%, 71,800, borrowings 565.5 + 23.3, leases 68.9 + 10.9, total 668.6).

## Stage reports beyond Gate 0 (sample tier), clean results

- B02 and B03: statement figures on AR26 p.191-193 (balance sheet, P&L, cash flow), Notes 6, 7, 14, 24-25, 30-32 and the maturity and contingent tables (p.211-223), S Notes 1.1, 2, 4, 31, 37H, 37K (p.155-180), JHPPL consolidation line (p.226), pay ratios (p.127), shareholding (p.111), BRSR turnover (p.53) and energy (p.74) all match the cited pages. Derived ratios (CFO/EBITDA 78.0%, DuPont, 53% and 64% funding cover, 5.73x capex to D&A, 89.3% CP share, receivable days 12.1 and 18.4) recompute.
- B03 external cross-checks: ICRA (1,200-1,250, 890-900, 425, 1.8x, 61.9% vs 67.5%, 22.9%, 23.6%), Q4 FY26 presentation p.4-12, RHP p.31, p.75-77, p.108-109, p.206, p.209, p.212, p.260-261, p.342-344, AR25 p.50, p.63, p.85, p.86.
- B04: unit economics, incremental margins and H1 FY27 bridge recompute from presentation p.7-9.
- B05: oral quotes in the Oct and Aug transcripts (mid-30s, INR20 lakhs, 3x ceiling, INR600 crore debt, INR400-plus cash, 70%, 144 beds, mid-60s, INR220 and 75-80 crore) match.
- B06: Medanta Noida (320, 236, 49, 86 million), KIMS (net debt 2,150, 1.9x, PAT 242 vs 415), Yatharth (3,150, 1,750, 392 million, 0.3%) match.
- B07: fixed-asset turnover series, 2,129 and 177% method, census-bed revenue tie-out (1,657.5 Cr), Thane filing of 12-Nov-2026 match.
- B08: RHP DGGI 25.72, consumer claim 37.50, WMS partner capital 41,180,000, 3 May 2019; HDFC Rs 500 Cr/300 Cr, MMRDA 354 Cr/10,026.44 sqm/80 years; Sulcus 3.78 Cr, 35-40 Cr match.
- B09: derived arithmetic (5.6 x 1.113^4, SAM, SOM CAGR, capacity ceiling) and RHP values match; only the anchors fail (finding 4).

## Coverage statement

Mandatory tier: 32 of 32 Gate 0 scorecard lines checked, rule used: every scored line in the Gate 0 scorecard, with each underlying input located or recomputed. No verdict card and no Section 1B pillar input exist in stages 0 to 9. No mandatory figure was left unchecked.

Sample tier: material universe about 1,900 (my count of numeric cells in scorecard, table and finding rows across the 11 reports; an estimate). Checked 470 (about 25%). Order of work: Gate 0 first, then AR statement and note values behind B02 and B03, then B04 and the presentations, then ICRA, XBRL, RHP, concall and peer quotes, announcements.

Not checked: 02-notes-pass2 and pass1 sections 5-12 beyond spot checks; B07 sections 3 onward; B08 sections 5 onward; B09 sections 5-7; most oral concall numbers in B05; about 90 of roughly 100 peer-transcript figures in B06; web-sourced (MEDIA, FORUM, secondary) numbers in B08 and B09, which have no PDF. The three results-filing PDFs and their page images were not opened; the reports route those figures through the presentations, which I did check.

```yaml
stage: B12a
company: "JLHL"
run_date: "2026-11-12"
model: claude-sonnet-5-5
status: complete
numbers_checked: 470
mandatory_checked: 32
mandatory_total: 32
findings:
  - {severity: "MAJOR", location: "01-gate0.md, Block C caution line (tax rate)", claimed: "FY26 tax rate 25.7% (66.25 / 260.44)", source_truth: "66.25 / 260.44 = 25.44% (screener-Data_Sheet FY26 Tax 66.25, PBT 260.44; AR26 p.192 C: 662.49 / 2,604.36 = 25.44%). 25.7% is the FY25 rate (66.93 / 260.68 = 25.68%)", note: "FY25 rate printed against the FY26 inputs. Not a scored input; the FY24 9.6% comparison is correct (18.80 / 195.42).", source_fidelity: true}
  - {severity: "MAJOR", location: "01-gate0.md, Block B capex FY21 to FY23 (3 values: 2,415.89 / 917.32 / 772.44 Mn)", claimed: "RHP restated cash flow p.76", source_truth: "Values are exact but sit on RHP PDF p.77 (printed folio 70, 'Purchase of fixed assets'). PDF p.76 is the Restated Statement of Profit and Loss and does not contain them", note: "ANCHOR NOT FOUND at the cited page; one page off. Feeds B2, B3 (mandatory tier). Value correct, anchor wrong.", source_fidelity: true}
  - {severity: "MAJOR", location: "01-gate0.md, Block B capex FY24 (852.95 Mn)", claimed: "AR 2025 consolidated cash flow, printed p.167", source_truth: "852.95 is on Annual_Report_2025.pdf PDF p.86, printed folio 166 ('Purchase of Property, plant and equipment, CWIP and intangible assets (3,207.26) (852.95)')", note: "ANCHOR NOT FOUND at printed p.167; one folio off. Value correct. Feeds B2, B3 (mandatory tier).", source_fidelity: true}
  - {severity: "MAJOR", location: "09-tam.md, Method 1, Method 5, Section 4A (RHP bed density, MMR and Kalyan-Dombivli inputs, global median, ARPOB CAGR, per-capita spend)", claimed: "MMR 33.0 beds/10,000, 20.96 M, 69,000 beds and Kalyan-Dombivli 10/10,000, 1,500 beds cited 'RHP p.178'; global median 29 beds cited 'p.172'; listed-chain ARPOB CAGR 10.7% cited 'p.174'; US$56.6 cited 'p.138'", source_truth: "Values exist but not on the cited PDF pages. MMR figures: PDF p.184 and p.185 (Kalyan-Dombivli PDF p.185). PDF p.178 holds personnel data (7 physicians, 17 nurses). Global median 29 beds: PDF p.147 and p.176. ARPOB CAGR 10.7%: PDF p.181. US$56.6: PDF p.145. These cites match RHP printed folios, while p.163, p.164, p.185, p.186 in the same report are PDF pages", note: "ANCHOR NOT FOUND on the PDF page; mixed printed-folio and PDF-page convention with no label. Bed-density inputs drive the Method 5 conclusion. Values correct, anchors unreliable.", source_fidelity: true}
  - {severity: "MINOR", location: "01-gate0.md, Block E, E2", claimed: "RHP p.~240 shows promoters at 40.69% pre-offer", source_truth: "40.69% (23,677,415 shares) is in the RHP at PDF p.260 and in the offer-structure text earlier; p.239 to p.240 hold director profiles, not the shareholding", note: "Approximate anchor with a tilde, wrong page. Context figure only; the E2 score rests on 40.91% to 40.91% (AR25 p.50, XBRL).", source_fidelity: true}
critical_count: 0
major_count: 4
minor_count: 1
false_positives_struck: 4
material_universe: 1900
acceptance_rate: 97
coverage_note: "MANDATORY TIER (OR-32): no verdict card and no Section 1B pillar input exist in stages 0 to 9. The tier is the 32 Gate 0 scorecard lines (A1-A4, B1-B4, C1-C4, D1-D4, E1-E4, M1-M12); all 32 checked, with every underlying input recomputed or located. 32 of 32. SAMPLE TIER: material universe about 1,900 (my count of numeric cells in scorecard, table and finding rows across the 11 reports; estimate). 470 numbers checked (about 25%), in materiality order: Gate 0, then AR26 statement and note values behind B02 and B03, then B04 and presentations, ICRA, XBRL, RHP, selected concall and peer quotes, announcements. NOT CHECKED: 02-notes-pass2 and pass1 sections 5 to 12 beyond spot checks; B07 sections 3 onward; B08 sections 5 onward; B09 sections 5 to 7; most oral concall numbers in B05; most peer-transcript figures in B06; web-sourced numbers in B08 and B09 (no PDF). The three results-filing PDFs were not opened. Rounding-level differences (0.01pp) were struck as matched figures. The AR prints a consolidated ROCE of 18.55% (C Note 36L); Gate 0 computes 13.77% on a labelled basis, so it is a labelled basis difference, not a finding."
```
