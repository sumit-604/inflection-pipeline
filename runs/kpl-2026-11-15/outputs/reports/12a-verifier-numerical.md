# VERIFIER A: NUMERICAL ACCURACY. KPL, run 2026-11-15 (Phase 1)

Model: claude-sonnet-5-5. Fresh context. Inputs read: reports 01 to 09 and blocks B00 to B09, against the source files in runs/kpl-2026-11-15/inputs (page-marked .txt beside each PDF; the .txt is the fast route, the PDF is the authority). Units: AR and results in Rs lakh, screener and decks in Rs Cr. Nothing was converted without stating it.

## RESULT IN ONE LINE

No MISMATCH, no ANCHOR NOT FOUND and no material UNANCHORED finding. Three MINOR findings. Zero CRITICAL, zero MAJOR. Source-fidelity gate: nothing to bind.

## FINDINGS TABLE

| # | Severity | Report location | Claimed value and anchor | Source truth and location | Note | source_fidelity |
|---|---|---|---|---|---|---|
| 1 | MINOR | 04-bizmodel.md analyst_note and B04 yaml, FY26 tax rate | 2,214.62 / 8,949.27 (AR p.30 lines) = 24.7%. Basis not labelled | Consolidated tax 2,214.62 (AR p.188 P&L, rows 2,280.03 less 88.70 plus 23.29) pairs with consolidated PBT 8,949.21 (AR p.188). 8,949.27 is standalone PBT (AR p.30 comparison table, standalone column; .txt line 1553). Report 03 section 2G uses the correct 8,949.21 | Unlabelled standalone/consolidated mix. 24.75% either way, so no decision effect | false |
| 2 | MINOR | 05-concall.md trigger 3 kill signal and B05 yaml, "guide cut to about 111-116 Cr (derived at 31.2% and 28.3%)" | 111 to 116 Cr | Using the report's own stated inputs (H1 PAT 54.65 Cr, Q2 results p.16; H2 PBT about 86 Cr; tax 31.2% and 28.3%) the range is 113.8 to 116.3 Cr. Low end 111 does not reproduce, not even on the 189 Cr EBITDA floor (about 112.0) | Derived, labelled [INFERENCE]. Inputs for the low end are not stated | false |
| 3 | MINOR | 07-emoat.md anchors "May call p.15" (Hikma), "May call p.17" (no increase in loans), "May call p.21" (partners fixed), "Aug call p.10" (running cash flows) | p.15, p.17, p.21, p.10 | Quotes exist. On the [page N] markers they sit on May p.16 (line 584), p.18 (line 679-681), p.22 (line 829) and Aug p.11 (line 406). They match only the printed footer ("Page N of M"), which is the marker minus 1 | B07 mixes the two numberings and does not state which it uses. Other B07 and B05 anchors use markers (Aug p.5 SD Pharma; May p.5 hormone WHO-GMP). Number is real; anchor off by one page | false |

## CANDIDATE ROWS STRUCK BY THE RULE 5B SELF-CHECK (false_positives_struck: 5)

1. FY26 CFO shown as 17.06 Cr (screener) in Gate 0 and 16.59 Cr (AR p.191, 1,658.62 lakh). Each is labelled with its source in 01-gate0.md, so this is a correctly labelled basis difference (5a).
2. Gate 0 KPL gross-margin proxy 48.6% against 48.7% on sales less raw material. It is 48.63% after the inventory change (AR 24,464.92 / 50,308.34) and 48.63% is the basis used for all three peers. Consistent. Not an error.
3. B09 "AR p.92 product-wise revenue mix". The mix sits on marker page 95. B09 states in its text that the printed folio is 92 and the marker is 95. Labelled; not an error.
4. B04 Q2 FY27 gross margin 52.2% against B05 52.1%. B04 derives it from rounded deck figures (94.5 / 181.2 = 52.15); B05 from lakhs (52.14). Both labelled derived; same figure to rounding.
5. B04 Q2 tax 31.3% against B01/B05 31.2%. B04 uses rounded deck Cr (13.2 / 42.2), B01/B05 use lakhs (1,319.16 / 4,221.77 = 31.25). Both labelled.

Also reviewed and not written up (judgment, not number): B05 "silent cut" of FY27 oncology revenue from Rs 150 Cr (May p.4, line 141) to Rs 100-110 Cr (Aug p.16-17, lines 630-645). Both numbers exist exactly as cited. Whether the cut was acknowledged is a reading for Verifiers B and C (in the Aug call the analyst states 100 Cr as last call's number and management answers "Correct").

## MANDATORY TIER (OR-32): 55 of 55 checked

Phase 1 has no B10 or B11, so there is no verdict card and no computed Section 1B pillar. The tier is set as every Gate 0 scorecard input, every Gate 0 load-bearing figure, and every figure the blocks hand to Section 1B (sector cap row, FY26 base year, FY27 guidance, margin and tax inputs, cash conversion inputs). Count: 32 scorecard lines (A1-A4, B1-B4, C1-C4, D1-D4, E1-E4, M1-M12) + 7 load-bearing figures + 16 feeders = 55. Checked: 55. Unchecked: 0.

### Gate 0 derived series (all 10 years, screener-Data_Sheet.csv, Rs Cr): ALL MATCH
Sales, EBITDA (re-derived as sales less RM, power, other mfr, employee, selling, other expense, with change in inventory), EBITDA %, EBIT (PBT + interest), capital (net worth + borrowings), ROCE proxy, net worth, ROE on average net worth (FY17 on closing), CFO, CFI, FCF proxy: 110 cells re-derived, 110 match. EBITDA reconciles to PBT in every year. Annual PBT agrees to AR p.188 (89.49 = 8,949.21 lakh). FY26 formula-basis ROCE 100.46 / (592.21 - 225.52) = 27.4%; FY25 64.02 / (447.27 - 169.505) = 23.0% (AR p.184-185: current liabilities 22,552.00 and 16,950.50 lakh) match.

### Gate 0 scorecard lines
| Line | Input as reported | Source check | Verdict |
|---|---|---|---|
| A1 median ROCE 17.0% | 17.00 (FY25) and 17.02 (FY17) are 5th and 6th of 10 | Re-sorted ten ROCE values | MATCHES |
| A2 min ROCE 11.1% (FY23) | 32.18 / 290.79 | Data Sheet | MATCHES |
| A3 median ROE 18.2% | 16.4% and 20.0% | Re-sorted | MATCHES |
| A4 21.7% vs 17.0% | FY26 and FY17 | Data Sheet | MATCHES |
| B1 cumulative CFO 264.92 / PAT 309.29 = 0.857 | Sum of 10 years | Re-summed | MATCHES |
| B2 FCF-positive 4 of 10 | FY19, 21, 24, 25 | Re-derived | MATCHES |
| B3 cumulative FCF -2.52 | Sum | Re-summed | MATCHES |
| B4 WC days | Receivable + inventory days FY17 135.4 (22.61, 13.85 on 98.3); FY26 260.0 (280.05, 78.25 on 503.08); payable days 73.8 (1,916.25 + 8,252.41 lakh = 101.69 Cr, AR p.185) | Data Sheet; AR p.185 | MATCHES |
| C1 revenue CAGR 19.9% | 98.3 to 503.08 over 9 years | 1.1989 | MATCHES |
| C2 PAT CAGR 39.5% | 3.36 to 67.35 | 1.3953 | MATCHES |
| C3 revenue-up years 7 of 9 | Declines FY20 and FY23 | Data Sheet | MATCHES |
| C4 +19.6pp | 39.5 less 19.9 | arithmetic | MATCHES |
| D1 net debt 126.87 / EBITDA 118.24 = 1.07x | 130.46 less 3.59; AR borrowings 2,940.02 + 10,106.04 = 13,046.06 lakh (AR p.185) | match | MATCHES |
| D2 EBIT 100.46 / interest 10.97 = 9.16x (8.97x ex other income) | Finance cost 1,097.04 lakh (AR p.188) | (100.46 - 2.03) / 10.97 = 8.97 | MATCHES |
| D3 debt 130.46 / equity 329.92 = 0.395 | Total equity 32,992.09 lakh, AR p.185 | match | MATCHES |
| D4 current ratio 1.80 | 40,567.75 / 22,552.00 lakh, AR p.184-185 | match | MATCHES |
| E1 promoter 54.86% | BSE summary Sep 2026: 56,92,888 sh, 54.86% | match | MATCHES |
| E2 history | 54.83% Mar 2025 (AR 2025 line 5154, 5,688,972 sh); 54.87% Mar 2026 (AR 2026 p.82, 5,693,069 sh); 54.86% Sep 2026 | match | MATCHES |
| E3 pledge none | BSE summary "pledged or otherwise encumbered: No" | match | MATCHES |
| E4 contingent 36.98 Cr / equity = 11.2% | Note 34: 3,697.75 lakh (AR p.226); 3,697.75 / 32,992.09 | match | MATCHES |
| M1 margin 9.1% to 23.5% | 8.90 / 98.3; 118.24 / 503.08 | match | MATCHES |
| M2 peers 35.0 / 26.6 / 14.6, median 26.6 | Re-derived from three peer Data Sheets | EBITDA 765.03/2,187.19; 168.32/632.63; 97.71/671.03 | MATCHES |
| M3 FAT 3.23x | 503.08 / 155.57 | match | MATCHES |
| M4, M10 two decline years | FY20, FY23 | match | MATCHES |
| M5 mcap rank | 18,156.91 / 5,409.45 / 3,966.41 / 1,045.65 | Data Sheets | MATCHES |
| M6 R&D | AR p.48 "approximately Rs 60 lakh" (line 2485) | match | MATCHES |
| M8 "70+ countries" | AR p.91 line 5059 | match | MATCHES |
| M9 GM proxy 48.6 vs 60.2 | KPL 48.63; peers 60.4 / 60.2 / 53.6 re-derived net of inventory change | match | MATCHES |
| M11 26.1% vs 21.7%; selling 12.3% to 8.2% | 251.03 to 503.08; 139.3 to 251.03; 30.8/251.03; 41.4/503.08 | match | MATCHES |
| M12 negative WC | Bounds from other liabilities (26.27 FY17) | match | MATCHES |

### Gate 0 load-bearing figures (7)
| Figure | Source | Verdict |
|---|---|---|
| Q2 FY27 PAT 2,902.62 lakh = 29.03 Cr | Q2 results p.16 | MATCHES |
| Q2 tax 1,319.16 lakh (1,059.80 + 220.04 + 39.32) on PBT 4,221.77 lakh = 31.2% | Q2 results p.16 | MATCHES (31.25%) |
| FY26 CFO 17.06 Cr (screener) and 1,658.62 lakh (AR p.191) vs PAT 67.35 Cr | screener; AR p.191, p.188 | MATCHES, both bases labelled |
| Trade receivables 28,005.24 lakh | AR p.184 | MATCHES |
| Trade receivables 33,503.65 lakh at 30 Sep 2026 | Q2 results p.14 | MATCHES |
| Increase 5,498.41 lakh (54.98 Cr) | Q2 results p.18; also 33,503.65 less 28,005.24 | MATCHES |
| Company debtor days 203 to 178; payable days 144 (FY26); inventory 111 to 77 | Q2 results p.4 and Q2 deck p.9 | MATCHES |

### Section 1B feeder figures carried in the blocks (16)
| Feeder | Where | Source check | Verdict |
|---|---|---|---|
| Sector cap row Pharma / CDMO, 38x | B00, B04 | .claude/skills/section-1b/references/05-sector-cap.md line 27 | MATCHES |
| FY26 revenue 50,308.34 lakh / 503.08 Cr | B03, B04, B05, B09 | AR p.187; Data Sheet | MATCHES |
| FY26 EBITDA 11,824.38 lakh, 23.50% | B03 | Derived from AR p.187 lines; deck p.6 shows 118 and 23.5% | MATCHES |
| FY26 PAT 6,734.60 lakh | B03 | AR p.188 | MATCHES |
| FY26 effective tax 24.7% | B04, B03 | 2,214.62 / 8,949.21 | MATCHES (see finding 1 for B04's denominator label) |
| FY27 revenue guidance 650 (May), 700+ (Aug), 720+ (Nov) | B05 | Q4 deck p.32; Q1 deck p.3; Q2 deck p.6; Q2 results p.3 | MATCHES |
| FY27 EBITDA 189-196, 27-28% | B05 | Q2 deck p.6 | MATCHES |
| FY27 PAT 100, 109+, 122+ | B05 | Q4 deck p.32; Q1 deck p.3; Q2 deck p.6 | MATCHES |
| Q2 FY27 revenue 181.2 Cr, EBITDA 27.5% (49.8 Cr), PAT 29.03 Cr | B05, B04 | Q2 deck p.4, p.6, p.7; Q2 results p.16 | MATCHES |
| Q1 FY27 revenue 16,235.22 lakh, tax 24.6%, EBITDA 25.3% | B05 | Q1 results p.7-8 (864.97 - 28.50 on PBT 3,398.70); Q2 deck p.6 | MATCHES |
| H1 FY27 CFO 2,756.79 lakh = 50.4% of PAT 5,464.85 | B05 | Q2 results p.16, p.18 | MATCHES |
| H1 FY27 capex 3,850.49 lakh; net borrowing +1,578.18 lakh | B05, B07 | Q2 results p.18 (2,718.86 less 1,140.68); borrowings 14,624.24 vs 13,046.06 on p.14-15 | MATCHES |
| FY26 capex 4,894.04 lakh; FCF -3,235.42 lakh; CFO/PAT 24.6% | B02, B03 | AR p.191 (4,460.15 + 433.89); 1,658.62 - 4,894.04 | MATCHES |
| Receivable ageing buckets FY24 to FY26 (24,974.95 / 1,463.91 / 1,002.09 / 89.74 / 474.55) | B02, B03 | AR p.212 Note 9(a)/(b); AR FY25 for FY24 | MATCHES |
| Capex-embedded growth 77% (115 Cr x 3.35x on 503.08) | B07 | Net PPE 150 and 120/139/144 (Q2 deck p.8) and revenue 251/307/370/503: FAT 2.09/2.21/2.57/3.35; 115 x 3.35 = 385.3 = 76.6% | MATCHES (rounded-deck basis, labelled) |
| SOM growth cross-check 25.7% (FY29 1,000) and 19.7% (FY31 1,235) | B09 | (1,000/503.08)^(1/3) = 1.2573; (1,235/503.08)^(1/5) = 1.1968 | MATCHES |

## SAMPLE TIER (stage-report numbers beyond the mandatory tier)

Checked and matched, by report:
- 02 notes (passes 1 to 3) and B02: P&L, balance sheet and cash-flow lines (AR p.184-191); ageing and provision nil (p.211-212); inventory (p.211); contingent liabilities, all five component amounts and the 3,697.75 tie (p.226-227); unhedged FX table USD 164.28 lakh / 15,550.18, EUR 5.45, AED 43.42 and FY25 7,712.22 / 266.35 / 123.26 (p.229, 12240); ratio note (p.235-237); Note 13 other current assets (1,785.21, 1,581.25, 72.39); Note 25 export 24,979.72 and domestic 25,326.18; Note 30 total 5,404.26; Note 32 lines (commission 363.97, advertising 324.52, travelling 173.79, distribution 1,415.15, power 2,669.12, testing 132.97); Note 40 related parties (Kaler 121.48 and 262.75, Iair 20.25 and 6.40); shareholder table (Bansal 958,746 / 1,103,174); AOC-1 (reserves -345.35, assets 126.36, outside liabilities 383.04, 1 MZN = 1.47); Note 3 vehicles 1,094.79 to 1,635.46; gratuity DBO 283.52 / assets 125.90 / past service 82.94. The FY25 CFO borrowing tie (7,855.88 to 9,732.63 = 1,876.75; 323.06 to 500.58 = 177.52; sum 2,054.27) re-derived from AR FY25 lines 6539, 6554, 8606. Derived ratios re-computed and tie: receivable days 203.2 / 152.1 / 135.9; payable days 146.6 / 108.6; CFO/PAT 24.6% / 132.4% / 182.0% / 85.3% like-for-like / 47.2% two-year; 1,166.32 roll-forward; gross margin 48.63% / 50.70%; effective tax 24.7%; net debt/EBITDA 1.07x; quick ratio 1.45; DuPont; interest cover 9.16x.
- 03 AR deep dive: board attendance (Takkar 7, Singh 1, Kapur 1, Vellanki 1, Sharma 6, Mahajan 2, Verma 2; AR lines 3271-3389), FPI 289,485 / AIF 37,122 / bodies corporate 126,121 (lines 4617-4624), executive pay, DSCR, ROCE capital base 45,787.97 = 32,992.09 + 13,046.06 - 250.18, MD&A ratio table (debtors turnover 2.30, interest cover 9.15, operating margin 19.97%, AR p.96). The Note 30 "court order" footnote is in the consolidated note (line 11973); the "Labour Codes" wording is in the standalone footnote and Note 2.2(m). Both quoted correctly.
- 04 business model: deck slides (Q2 deck p.4, 6, 7, 8, 9, 12, 21, 26, 27, 33), unit split 63/15/20/2/1 and 61/14/22/3/1, 750+ filings, 100+ clients, ROCE 31.0%, R&D 2.5%, ICRA p.2-3 (NWC/OI 50.2% in FY25, "limits its pricing power", longer payment period, domestic 45-55%), 177.9-day derivation (335 / 687.2 x 365), incremental margins.
- 05 concall: guidance rows and page anchors in the May and Aug transcripts (650-700, 150-160 / 160-170 / above 200, 26-27% EBITDA, 52-53% gross margin, debtor days 150-160 and 165-170, hormone before November vs June-July 2027, KPMG statements, oncology 150 vs 100-110, FY30 1,500, Algeria 80-90 Cr, India 5%), promise-delivery arithmetic (Q1 gross margin 46.2%, Q2 52.1%, FCF -10.9 Cr, borrowings +12.1%).
- 06 peers: Caplin 136 and 125 days (May 2026 p.9), 100 to 130 days (p.14), 35+ filed and 20 approvals (Nov 2025 p.5), Q1 FY27 +20% / +18% / 59.8% / stock +76 Cr / receivables +46 Cr (Aug 2026 p.5-6); Senores 187 and 104 days (May 2026), 90-94 days (Jan 2026 p.16), 558 approved and 944 pending (Nov 2026 p.17), CDMO 4-6 points lower margin and 40% US EBITDA (Jan 2026); Lincoln Dec 2025 quarter sales 166.32 vs 146.55 (Data Sheet).
- 07 emerging moat: capex 65 / 50 / 70, Algeria share, deck net debt/equity 0.37, interest cover 14.47x (Q2 deck p.22), BSE 24 Jul 2026 Pembrolizumab, BSE 19 Oct 2026 Unit 7 (4 acres, Q4 FY2028, Q2 FY2029), BSE 4 Nov 2026 Hungary EU-GMP, BSE 10 Mar 2026 BE molecules, Q2 results unit data.
- 08 promoter: auditor resignation 12 Nov 2026 (FRN 001051N, reason, same-day B S R & Co. LLP FRN 101248W/W-100022, term to 44th AGM, 4000 staff and 170+ partners, appointed 24 Sep 2024), Kapur resignation 2 Jun 2026, shareholding 5,693,069 / 5,692,888, holdings of Ramesh and Ajay, Anju Arora 135,634 shares, pay 294.00 = 4.4% of PAT.
- 09 TAM: all arithmetic re-computed from the stated inputs (Rs 374,300 + 336,775 = 711,075; 38,831 + 30,030 = 68,861; Brazil cut 14,756; SAM 54,105; 7.6% and 78.6%; 241.5 injectable revenue = 48% (AR p.95); 0.45%; 224x; per-filing revenue 0.72 and 0.92; capacity 982 / 1,080; oncology 298-309; 93%). Internal figures from the AR (global pharma 1.74 trillion, 3,000+ companies, 10,500 units, AR p.89-90) match.

## COVERAGE STATEMENT

Mandatory tier: 55 of 55 figures checked. None unchecked. Rule used: every Gate 0 scorecard line and moat test (32), every Gate 0 load-bearing figure (7), and every figure the blocks pass to Section 1B (16), because Phase 1 has no verdict card or computed pillar.

Sample tier: I count about 500 material numbers in the reports. I counted a number as material when it is a table cell or headline figure that feeds a score, flag, trigger, guidance row or cross-check (Gate 0 table cells, top-15 note findings, block yaml numeric fields, deck and call guidance rows, peer evidence figures, TAM arithmetic). I checked 335 of them beyond the mandatory tier, 390 in total including the mandatory figures. Roughly 78% of material numbers by count; I do not claim completeness.

Not checkable against the PDFs supplied (named, not read as verified): the web-sourced figures in 08 (registrationwala, Tofler, Trendlyne, DRAP recall alert, ValuePickr, AmbitionBox) and 09 (IMARC LATAM 39.4 bn and injectables 54.5 bn with 7.5% and 5.8% regional shares, EMR MEA 35.45 bn, Pharmexcil growth, RBI 95.2492, Brazil 38%, EPO and hormone pools, India exports); the Step-1 brief P/E 41.1x and the 28-32% / 24-26% registration-type EBITDA ranges (B04 and B09 correctly label both unanchored). Not opened: Q4 FY26 results PDF; Caplin Q3 FY26; Senores Q1 FY27; Lincoln calls (peer figures cited in 06 were checked only for Caplin Nov 2025, May 2026, Aug 2026 and Senores Jan, May, Nov 2026).

Source-fidelity gate: no finding to bind. Nothing here needs Verifier B, C or the synthesis to clear it, and nothing here can be cleared by them.

```yaml
stage: B12a
company: "KPL"
run_date: "2026-11-15"
model: claude-sonnet-5-5
status: complete
numbers_checked: 390
mandatory_checked: 55
mandatory_total: 55
findings:
  - {severity: "MINOR", location: "04-bizmodel.md analyst_note and B04 yaml (FY26 tax rate 24.7%)", claimed: "2,214.62 / 8,949.27 (AR p.30 lines) = 24.7%, basis not labelled", source_truth: "Consolidated tax 2,214.62 pairs with consolidated PBT 8,949.21 (AR p.188 P&L). 8,949.27 is STANDALONE PBT (AR p.30 standalone column). Report 03 section 2G correctly uses 8,949.21. Ratio is 24.75% either way", note: "Unlabelled standalone/consolidated mix in the denominator. Rate is unchanged to one decimal, so no decision effect. Reported as UNANCHORED (basis) under rule 5a", source_fidelity: false}
  - {severity: "MINOR", location: "05-concall.md trigger 3 kill_signal and B05 yaml (PAT guide cut to about 111-116 Cr, derived at 31.2% and 28.3%)", claimed: "111-116 Cr", source_truth: "From the report's own stated inputs (H1 PAT 54.65 Cr per Q2 results p.16; H2 PBT about 86 Cr; tax 31.2% and 28.3%) the range reproduces as 113.8 to 116.3 Cr. The lower end 111 does not reproduce under the stated inputs or under the 189 Cr EBITDA low end (about 112.0)", note: "Derived figure with unstated inputs at its low end. Labelled derived and [INFERENCE]; not a source number", source_fidelity: false}
  - {severity: "MINOR", location: "07-emoat.md anchors 'May call p.15' (Hikma Pharma, Algeria partner), 'May call p.17' (no increase in loans), 'May call p.21' (partners more or less fixed), 'Aug call p.10' (capex from running cash flows)", claimed: "p.15 / p.17 / p.21 / p.10", source_truth: "Statements exist in the transcripts. On the file's [page N] markers they sit on May p.16, p.18, p.22 and Aug p.11. They match only the printed footer numbering (footer = marker minus 1). Other B07 and B05 anchors use the marker numbering (for example Aug p.5 SD Pharma, May p.5 hormone WHO-GMP)", note: "Mixed page-numbering convention, convention not stated in B07. Numbers and quotes are real; the anchor is imprecise by one page", source_fidelity: false}
critical_count: 0
major_count: 0
minor_count: 3
false_positives_struck: 5
material_universe: 500
acceptance_rate: 99
coverage_note: "Mandatory tier = 55 figures, all 55 checked (Phase 1: no B10/B11, so no verdict card or computed Section 1B pillar; tier set as 32 Gate 0 scorecard lines A1-E4 and M1-M12, 7 Gate 0 load-bearing figures, 16 Section 1B feeder figures carried in B03/B04/B05/B07/B09). Sample tier: about 500 material numbers by my count (every table cell and headline figure that feeds a score, flag, trigger or guidance row); 335 further numbers checked (390 in total). Not checkable against the PDFs supplied, named so they are not read as verified: web-sourced figures in B08 (registrationwala, Tofler, Trendlyne, DRAP recall alert, ValuePickr, AmbitionBox) and B09 (IMARC LATAM 39.4 bn, IMARC injectables 54.5 bn and 7.5 and 5.8 percent shares, EMR MEA 35.45 bn, Pharmexcil growth, RBI 95.2492, Towards Healthcare Brazil 38 percent, EPO and hormone pools, India exports); the Step-1 brief P/E 41.1x (B04, B09 label it unanchored); the 28-32 and 24-26 percent registration-type EBITDA figures (B04 labels unanchored). B09 arithmetic on those inputs was re-computed and ties. Not opened: Q4 FY26 results PDF, the Caplin Q3 FY26 and Senores Q1 FY27 calls, Lincoln calls (peer anchors checked: Caplin Nov 2025 and May 2026 and Aug 2026, Senores Jan and Nov 2026 and May 2026). Source-fidelity result: no MISMATCH, no ANCHOR NOT FOUND, no material UNANCHORED."
```
