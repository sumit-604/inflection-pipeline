# Verifier A: Numerical Accuracy, PREMEXPLN, run 2026-11-15 (Phase 1)

Model claude-sonnet-5-5. Inputs: stage reports 01-09 and the corpus under inputs/. Page convention: AR and results anchors use the [page N] marker in the .txt; concall anchors use the transcript's own "Page n of N" label, which sits at the top of each page.

## Result in one paragraph
No CRITICAL. One MAJOR source-fidelity finding (B02 label "over one year 888.35 L"), already corrected downstream. Four MINOR anchor or basis findings. The Gate 0 scorecard (the whole mandatory tier) ties to source on all 142 input figures and every derived ratio recomputes. Web-sourced figures in 08 and 09 could not be tested.

## Findings
| # | Sev | Location | Claimed (anchor) | Source truth (location) | Note | SF |
|---|---|---|---|---|---|---|
| 1 | MAJOR | 02-notes.md rank 3, FLAG-CASH reason, receivables_trend | Over-1-year receivables 887.36 L (FY25) to 888.35 L (FY26), "nothing collected net" (Note 11, p.127-128) | FY26 over one year = 298.38 + 556.28 + 332.07 = 1,186.73 L (AR FY26 p.127, line 8311). FY25 = 575.62 + 123.87 + 187.87 = 887.36 L (p.128). 888.35 L = 556.28 + 332.07, the over-2-year sum | MISMATCH on the label. 03-ardeep.md and the orchestrator correction already carry 1,186.73 L (+33.7%); the B02 body and YAML do not. Not a verdict-card or 1B pillar input | true |
| 2 | MINOR | 05-concall.md anchors | Q4 FY26 call p5 (Rs 600-700 Cr; 15-20%); Q1 FY27 p6 (Q1 only Rs 21 Cr); Q3 FY26 p9 (target Rs 500 Cr); Q3 FY26 p8 (nine-month exports Rs 40 Cr) | Same quotes sit on Q4 FY26 p4, Q1 FY27 p5, Q3 FY26 p8, Q3 FY26 p7 | Numbers present and equal; page off by one. Other B05 anchors tested are right | false |
| 3 | MINOR | 07-emoat.md 2A, 2C, F2; 04-bizmodel.md 1C | Balance sheet "AR p.110"; sale of services and products table "AR p.133" | Balance sheet is [page 109]; revenue-by-type table is [page 132] | Values match; page wrong | false |
| 4 | MINOR | 03-ardeep.md 2.0 rank 7 | "Note 32(B) p.142-143: 94.66 vs 85.58 per USD" | No rate is printed. Implied 1,101.50 L / 11,63,707 USD = 94.65; FY25 793.23 L / 9,26,872 = 85.58 (lines 9052, 9082) | Derived, not tagged; 0.01 off. 10.6% move holds | false |
| 5 | MINOR | 01-gate0.md line 7 and ROCE memo | Other income 35.93 cr, 59% of PBT, set beside note 6 one-offs 3,417.80 + 500 L | Data_Sheet FY26 = 35.93 (matches as labelled). Filing: 4,214.24 L consolidated = 42.14 cr (results p.15). 35.93 reconciles to 4,214.24 - 520.00 - 100.00 - 1.21 = 3,593.03 L (my inference) | Basis labelled "screener-data" but the netting is not stated; one-offs (39.18 cr) exceed the "other income" shown. Flags already fire; B03 carries 64.8% and 69.7% | false |

Struck by the 5b self-check (6): consolidated vs standalone contingent liabilities (8,353.60 vs 8,343.60 L, both labelled); screener EBITDA 10.2% vs AR 10.0%; Gate 0 CFO -1.27 cr vs B03 -144.14 L (labelled bases); the labelled part of the 35.93 vs 42.14 gap; Annexure 10 ratio column (faithfully transcribed anomaly); B05 EBIT 9.6 vs 9.54 cr (management rounding).

## Mandatory tier (OR-32)
No verdict card or Section 1B pillar input exists yet. The tier is the Gate 0 scorecard inputs: 142 figures counted, 142 checked.
- Block A: PBT, interest, share capital, reserves, borrowings, PAT for FY17-FY26 (60 points) all equal Data_Sheet rows. EBIT, capital employed, ROCE, average net worth, ROE, both medians and the 8.7% memo recompute exactly.
- Block B: CFO and CFI x10, cumulative CFO 238.24 and PAT 129.47, FCF series, 47.51 cumulative. Capex FY26 27.83 and FY25 13.42 (results p.17, 2,783.15 and 1,341.79 L); FY24 23.39 (AR FY25 consolidated CFS, 2,339.28 L). WC days: 33.3 / 134.2 / 101.9 / 65.6 and 50.2 / 96.8 / 39.0 / 108.0 recompute from results p.16.
- Block C: sales series, CAGRs 5.6% and 12.6%, 5 of 9 up years.
- Block D: 32.34 and 60.07 cr (tie to results p.16: 3,233.32 and 6,007.19 L); current ratio 25,832.44 / 15,673.70 = 1.65 (p.16).
- Block E: 41.33% (XBRL 0.4133 and capture, Mar 2023 and Sep 2026), pledge false (XBRL), contingent 7,607.05 + 575.83 + 98.88 + 61.84 + 10.00 = 8,353.60 L (AR FY26 consolidated Note 32).
- Block F: EBITDA margin 12.5% / 10.2% recompute from Data_Sheet lines; FAT 2.07x; R&D 49.71 L (Note 28) = 0.13%; selling 8.40% to 5.69%; 24.3% and 7.1% CAGRs.
- Load-bearing lines: CFO -127.20 L (p.17), note 6 figures 3,417.80 / 2,246.39 / 1,171.41 / 500 (p.18), H1 FY26 other income 23.76, H1 FY27 sales 247.84, operating profit 23.10 and 9.3%.

## Sample tier (130 of about 360 material figures, about 36%)
Rule: material = rupee, percentage, count or date figure that feeds a flag, grade, ratio or SOM arithmetic in 02-09, excluding web-sourced figures; work order was scorecard and flag inputs first, then table cells.
Matched without exception: AR FY26 P&L, balance sheet, cash flow (every line quoted in 03), Notes 11, 21-25, 32(B), 33, 34, 43; MD&A segment, order book and EBITDA figures; BRSR fatalities and LTIFR; shareholding table; KMP and Annexure 10 pay; CWIP, commitments, rating; AR FY25 FY24 comparatives; deck pp.5-10 (all of B04's mix, margin, order book, CWIP figures); other income in Q1/Q2 FY27 filings; the five order-intimation sizes; concall guidance, order book splits, "last one" quote, Rs 21 cr; peer figures in 06 and 09 (Solar, Astra); all arithmetic in 09 SOM Readings A and B (25.8%, 22.9%, 17.0%, 17.3%) and 03 DuPont, interest cover, ROCE, covenant ratios.

## Not checked
Web-sourced figures in 08-promoter.md and 09-tam.md (MarketsandMarkets, Ken Research, FX 93.9 and 89.45, media dates, Apollo/IDL Rs 107 cr). Corpus grep found no 1,47,40,325, 986.35 or 7,62,414, so the open-offer tender result in 08 has no corpus anchor. Also unchecked: Note 9(ii) supplier advances, Note 16, Note 38 sub-lines, CG attendance and fee tables, FY24 borrowings behind the 20.1% FY25 finance cost ratio, deck pp.11-24 profile text.

```yaml
stage: B12a
company: "PREMEXPLN"
run_date: "2026-11-15"
model: claude-sonnet-5-5
status: complete
numbers_checked: 272
mandatory_checked: 142
mandatory_total: 142
findings:
  - {severity: "MAJOR", location: "02-notes.md: Top findings rank 3, FLAG-CASH reason, receivables_trend (B02 Pass 3 consolidation)", claimed: "Receivables over one year: 887.36 L (FY25) to 888.35 L (FY26), 'nothing collected net' (Note 11(c),(d), p.127-128, INR lakhs)", source_truth: "FY26 over one year = 298.38 + 556.28 + 332.07 = 1,186.73 L (AR FY26 Note 11(c) ageing row, p.127, txt line 8311); FY25 over one year = 575.62 + 123.87 + 187.87 = 887.36 L (Note 11(d), p.128). 888.35 L (= 556.28 + 332.07) is the over-TWO-year sum only", note: "MISMATCH on the FY26 label. Stage 3 (03-ardeep.md 2.0 rank 3) and the orchestrator correction already state 1,186.73 L (+33.7%); the B02 report body and YAML still carry 888.35 L. Not a verdict-card or Section 1B pillar input, so MAJOR. Gate 0 does not use the figure.", source_fidelity: true}
  - {severity: "MINOR", location: "05-concall.md: anchors for Q4 FY26 call 'Rs 600-700 Cr' and '15-20%' (cited p5), Q1 FY27 call 'Q1 only Rs 21 Cr' (cited p6), Q3 FY26 call 'targeting Rs 500 Cr' (cited p9) and FY26 export 'Rs 40 Cr nine months' (cited p8)", claimed: "Pages as listed, on the transcripts' own 'Page n of N' labels (B05 anchor key)", source_truth: "On the same labels the quotes sit on Q4 FY26 p4 (Concall_Jun txt lines 184, 186), Q1 FY27 p5 (Concall_Aug txt line 235), Q3 FY26 p8 (Concall_Feb txt lines 349-356) and p7 (line 316). The [page N] file marker is one higher than the label, which fits the Q4 FY26 case only", note: "Every quoted number exists in the source and the values match; the page is off by one on these rows. Weak anchor, not a missing number. Other B05 anchors checked (last one p12, 1,569 Cr p3-4, 1,294.6 Cr p3, 1,393 Cr p3, 14.3% p3, 'retain 600' p6, 500-600 p9) are right.", source_fidelity: false}
  - {severity: "MINOR", location: "07-emoat.md (CWIP 'AR p.110 BS', 2C and F2) and 04-bizmodel.md ('AR p.133 (Note 21)' for sale of services 3,593.78 L and the 34,874.95 + 238.41 + 3,593.78 + 127.00 cross-check)", claimed: "Balance sheet on AR p.110; revenue-by-type table on AR p.133", source_truth: "Balance sheet is on [page 109] (CWIP 2,639.23 L, txt line 6813); p.110 is the P&L. The sale of products/services table is on [page 132] (txt lines 8580-8585); p.133 holds geography, contract price and Note 22", note: "Values match. Wrong page only. Stage 3 anchors these correctly.", source_fidelity: false}
  - {severity: "MINOR", location: "03-ardeep.md 2.0 rank 7: 'Note 32(B) p.142-143: 94.66 vs 85.58 per USD'", claimed: "Year-end rates 94.66 and 85.58 per USD, presented as printed in Note 32(B)", source_truth: "No rate is printed. Implied from the unhedged table: FY26 1,101.50 L / 11,63,707 USD = 94.65; 2,804.73 L / 29,63,126 USD = 94.65; FY25 793.23 L / 9,26,872 USD = 85.58 (txt lines 9052, 9057, 9082). The 10.6% move still holds (94.65/85.58 = 10.6%)", note: "Derived figure with no (derived) tag; FY26 rate differs by 0.01. UNANCHORED as printed, immaterial.", source_fidelity: false}
  - {severity: "MINOR", location: "01-gate0.md load-bearing line 7 and Block A memo: 'Other income FY26 Rs 35.93 cr (screener-data), 59% of PBT' set beside note 6 items 3,417.80 L + 500 L", claimed: "Other income Rs 35.93 cr, 59% of PBT 60.49 cr; ROCE ex other income 8.7%", source_truth: "Data_Sheet row 19 col FY26 = 35.93 (matches as labelled). The filing prints consolidated other income 4,214.24 L = Rs 42.14 cr (Q4 FY26 results p.15, txt line 741) and standalone 4,214.49 L (AR p.110). 35.93 reconciles to 4,214.24 less 520.00 ex-gratia, 100.00 accident loss and 1.21 JV loss = 3,593.03 L, so screener nets items the filing shows elsewhere. On the filing basis other income is 69.7% of PBT (B03)", note: "Not a copy error: the figure is labelled screener-data and is in the source. The basis gap (note 6 one-offs of 39.18 cr exceed the 35.93 cr 'other income') is not stated in Gate 0. Unlabelled basis difference, rated UNANCHORED MINOR because flags FLAG-GATE0 and FLAG-CASH already fire and B03 carries the filing-basis 64.8% / 69.7%. The screener derivation itself is my inference.", source_fidelity: false}
critical_count: 0
major_count: 1
minor_count: 4
false_positives_struck: 6
material_universe: 500
acceptance_rate: 96
coverage_note: "See the full text in outputs/blocks/B12a.yaml (identical). Mandatory tier = Gate 0 scorecard inputs (no verdict card or 1B pillar input exists in Phase 1): 142 of 142 checked. Sample tier: 130 of about 360 material figures (about 36%, estimate). Web-sourced figures in 08 and 09 not testable; open-offer tender result figures in 08 have no corpus anchor."
```
