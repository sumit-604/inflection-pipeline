# 12a Verifier A: forward_module.md numerical audit

Artifact: runs/accord-2026-10-06/forward_module.md. Date 2026-10-06. Model Sonnet 5.5. Result: 0 CRITICAL, 0 MAJOR, 9 MINOR. No source-fidelity finding stands.

Method. Every calculation recomputed from its stated inputs, by hand (no code ran in this session), then compared with the module. Every filed input located in the page-marked source at the cited anchor. Framework arithmetic checked against section-1b chunks 01, 02, 03, 05, 06, 07, 10, 12 (and RRM formula in chunk 15). Judgment not assessed.

## 1. Findings table

| # | Sev | Location | Claimed + anchor | Source truth + location | Note |
|---|---|---|---|---|---|
| 1 | MINOR | B1 (line 93) | Incremental EBITDA margin about 18% (B04) | Ex-OI: (4.70-2.25)/(42.35-27.72) = 16.7% [Deck p.23; AR p.78]. 18.0% only with other income in EBITDA (493.64, 229.75 lakh) | Unlabelled basis. Feeds nothing. UNANCHORED |
| 2 | MINOR | H15 | Rs 39.99 Cr = 51.9% of H1 inflow | 19.97 incl GST [Ord 20260629 p.2] + 20.02 ex GST [Ord 20260923-d54c506f p.1-2] mixes bases. Ex-GST 36.95 Cr = 48.0% of 77 [H1upd p.2] | Red-flag row only. C1 uses 16.93 ex GST |
| 3 | MINOR | G1 Row D 3a(i) | FAT 8.81x [B12a FAT; AR p.33] | AR p.33 has no FAT. AR p.77-78: 7,006.92/794.62 = 8.82x; ex intangibles 9.10x (B07 basis) | 164% stays 164% or 169%. Award unchanged |
| 4 | MINOR | G1 Row B | Cum CFO/PAT -0.18 (B01), no basis | Screener basis. Prospectus restated CFO 1.88, -4.93, -8.93 gives -3.28/12.92 = -0.25. FY25 -8.18 and FY26 8.70 match AR p.79 | Same 0.80x band |
| 5 | MINOR | D3 ESOP | "Over a 3-year vest" | Filing: min 1 year, max 5 years [Ord 20260926-3aa16089 p.3] | Sensitivity only. 3.76 / 1.25 / 0.45 arithmetic right |
| 6 | MINOR | D3 depreciation | 3.17% (30 yr) and 6.67% (15 yr) [AR p.80] | AR p.80 names no life. 3.17% carries 5% residual, 6.67% none (6.33% on the same basis) | About Rs 0.02 Cr by FY29 |
| 7 | MINOR | D2, D1, D3, E | -110/+436 bps; 101.6; 10.47; 14.6 | Exact -108/+433; 101.65; 10.48; 14.7 | Rounding, under 0.1% each |
| 8 | MINOR | F | Mcap 175.0 in Mcap/EBIT and EV, diluted shares in P/E | 175.0 is basic (85.2 x 2.0573 = 175.3). Diluted implies 179.5. Base FY28 P/E basic 17.1x vs 17.5x | Unlabelled basis, under 3% |
| 9 | MINOR | C1 Ord 20260907 | Window "Within 3 Months", p.1-2 | Ventora 0.493 Cr is "Within 2 Months" on p.3 | Both H2 FY27. Sum unchanged |

Struck at the 5b self-check (3): the 16.93 ex-GST conversion (labelled [calc], rate 18% in sister filings, and 16.93 + 20.02 = 36.95 vs 37 in H1upd p.2); H2 materials 77.0% vs 77.05% (same value); base FY28 P/E 17.5x vs 17.55x (same value, two roundings).

## 2. Mandatory tier, recomputed in full

Source inputs located (all MATCH):

| Input | Module | Source |
|---|---|---|
| FY26 revenue / OI / PBT / int / D&A | 7,006.92 / 28.78 / 605.75 / 55.04 / 62.60 lakh | AR p.78 |
| Operating EBITDA ex OI, margin | 694.61 lakh, 9.91% | 605.75+55.04+62.60-28.78; /7,006.92 |
| Borrowings / cash | 47.22+836.24 = 8.83 Cr; 22.33 Cr | AR p.77 |
| IPO unspent 31-Mar-26 | 2,040.21 lakh | AR p.73 CARO |
| H2 FY26 line items | 4,235.36; 3,263.14; 310.46; 192.21; OI 24.09; D&A 33.52; fin 22.62 | Deck p.23 |
| H2 FY25 revenue | 57.53 Cr | Deck p.23 (5,753.19) |
| H1 FY27 revenue / growth / book / inflow | 52.68; 90.07%; 173; 77 | H1upd p.2 |
| Capacity, 9M production, FY25 production | 900.36; 400.50; 473.62 MVA | Pros p.123 |
| Realisation | 11.29 (4,521.63/400.50); 16.69 (7,902.25/473.62) lakh/MVA | Pros p.110, p.123; reproduces |
| FY23/24/25 revenue; OI; EBITDA | 407,816.87; 485,369.15; 790,225.33; 609.49; 1,778.69; 26,727.95; 91,013.90 thousand | Pros p.86, 110, 182 |
| UGVCL 500 kVA; PO total | 201,190.40 thousand = 20.12 Cr; 875,000.02 = 87.50 Cr | Pros p.115 |
| Order book 18-Jan-26 | 16,42,575.62 thousand | Pros p.115 |
| Order filings | 19.97 incl GST; 20.02; 8.39+0.245; 5.28; 1.92; 0.51; 0.50 | Ord files; sum 53.80 reproduces |
| Land | 8.85 + 1.82 | Ord 20260703 p.1; H1upd p.3 |
| IPO table | 1,302.67 / 931.59 / 68.41 / 700.00 / 602.67 / 1,371.08 lakh | AR p.33 |
| Shares | 2,05,73,289; ESOP 5,00,000; floor Rs 10 | AR p.39, 85, 35; Ord 20260926 p.2 |
| Salary escalation | 8% | AR p.93 |
| FD interest | 11.25 lakh | AR Note 20 p.90 |
| Lot | 3,000 | Pros p.241 |
| CMP / Mcap / cap row | 85.2 / 175.0 / 25x | manifest.yaml |
| Guidance, 90%, utilisation | 60-80%, 120-180, 90% | Tr L252, L263, L490 |

Calculations recomputed (all MATCH unless in findings):
- D1: FY27 106.48; annualised 105.36; CAGR 27.9% ((114.57/70.07)^0.5); FY23-26 19.8%; bear 95.03, 101.6 to 101.65, +7.6%; bull 126.60, 135.24 (900.36 x 0.9 x 16.69), x1.3.
- D2: bridge 13.17% (23.0% - 10.4721/106.48); FY28-31 13.13, 13.09, 13.06, 13.02; bear avg 8.86% (5.38, 11.29, 9.91); AR-basis 11.15% and 8.81%.
- D4: all 64 main cells and 36 extension cells reproduce, EPS to 2 dp: bear 2.54/2.75/2.70/2.77/3.00; base 4.54/4.85/5.08/5.46/5.87; bull 6.68/7.07/9.17/12.08/15.88. FY26 core EPS 2.05 (4.3175/2.1073).
- D5: 11.83, 12.72, 14.14 lakh/MVA; 184-281 MVA; 41-62%.
- F: EV(a) 161.50, EV(b) 181.90; all 35 table cells; peer EV, EBIT, EV/EBIT, Mcap/EBIT for six names; medians 26.3, 26.3, 33.3.
- G: Row A 13.25% / 40.9% / 22.06% / 18.53 to 18.5; Row C 14.80; 3a 164%, 1.70x; 3c 2.47x and 1.82x; Row F/H 16.80; range 15.5-18.0; sensitivity 12.95/14.95/16.65/18.65/14.80/16.80; RRM 0.94, Track 1 13.91, divergence 17.2%; haircut 15.8 gives 47.5; exit FV 98.7 / 81.7; entry 50.5 / 41.8 (/1.953125); 30% 44.9 / 37.2; FY30 variant 91.7 / 47.0 and 76.0 / 38.9; FV today 81.6 / 67.5; bear 50.4 and 38.8; bull 266.8 and 296.2; CAGRs -16.1, +5.0, +46.3; weighted 115.4 (10.6%, 5.9%) and 102.2 (6.2%, 1.7%); 4F 0.39x; HR 1.16 and 1.33 vs 1.953; FV path 81.6, 85.3, 91.7, 98.7; FV CAGR 6.6%; T1 34.4 (40%), increment 47.1 (55%), residual 4%.
- Framework rule fit: Pillar 1 formula chunk 01 (0.5 x ROCE + 7.5); Pillar 2 band chunk 02 (0.80x); 3a/3b/3c chunk 03; cap chunk 05 (25x, cap does not bind); HR formula, tiers, dispersion, MoS table chunk 06; exit basis one year forward at both ends, Year 4 present, chunk 10; FV CAGR formula and DISCOUNT-CLOSER (<10%) chunk 12; RRM = 1 + (13.5 - 14.0) x 0.12 chunk 15. The arithmetic follows each stated rule.
- I1: 19.8% gross margin at 9.9% EBITDA ((0.099 x 52.68 + 5.24)/52.68). I2: lot Rs 2.56 lakh; Rs 1.28 Cr portfolio for one lot at 2%; dispersion 219%; MoS Rs 30.3-35.4.

Not checkable from local sources (arithmetic only): screener peer debt, TTM operating profit, depreciation, PBT+interest, ROCE and EBITDA ranges; B09 7.6% and Rs 33,000 Cr; B06 peer H1 shares and Shilchar capex intensity; B05/B12b grades and the 35/45/20 and 45/40/15 weights (chunk 17 not loaded); B07 EM 8.0; B01 ROCE history 33.0/39.8/37.8. For six peers, market cap, P/E and cash match the saved screener pages in work/forward (copies only).

## 3. Sample tier (A, B, C, E, H)

Material universe 270; checked 184 (68%). Material = any number that feeds a projection, ledger status, order-book bridge or red-flag severity.
- A: HIT 4, MISS 8, PARTIAL 1, PENDING 18 sums to 31 rows. Rows 1-4, 8-10, 20-25, 27, 29, 31 anchors and arithmetic match.
- B: B1 table and B3 25-cell table reproduce (core PAT 3.78 to 5.83). B2 copper and steel arithmetic only (+26.9%, +14.6%, +24%, 2,065).
- C: bridge 148.68; row sums of Pros p.114-115 (Rs 10.58 Cr before 1-Oct-25, 5.74 before 1-Apr-25, 153.68 + 1.32 = 155.00 Cr after) reproduce; C1 split 53.80 / 87.50 / 31.70; capacity flag 428-537 MVA.
- E: 13.03, 13.71, 0.68, 704 MVA, 79.5-117.5 Cr, funding gap 79 Cr reproduce.
- H: H3, H4, H5 (53.7%), H6 (2.43%, 84%), H8 (78 days), H12 (118%), H13 (+135%), H15 (finding 2).
- Not checked: A5-A7, A11-A19, A26, A28, A30; H1, H2, H7, H9-H11, H14, H16-H18; B2 web sources.

## 4. Verdict

Every number that moves the entry price (Rs 50.5 / 41.8), the exit P/E (16.80x), FY28 EPS (Rs 4.85) or the break margin (9.9%) reproduces from its inputs and sits in its source. The nine MINOR rows are basis labels, anchor gaps and rounding. None changes a pillar input, a case, or a decision. No CRITICAL, so no REWORK trigger. No finding carries source_fidelity: true.

```yaml
stage: B12a
company: "ACCORDTS"
run_date: "2026-10-06"
model: claude-sonnet-5-5
status: complete
numbers_checked: 646
mandatory_checked: 462
mandatory_total: 462
critical_count: 0
major_count: 0
minor_count: 9
false_positives_struck: 3
material_universe: 732
acceptance_rate: 98
```

Full block with the nine findings: runs/accord-2026-10-06/outputs/blocks/B12a-forward.yaml
