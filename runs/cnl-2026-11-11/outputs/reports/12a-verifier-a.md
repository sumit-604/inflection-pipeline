# VERIFIER A: NUMERICAL ACCURACY, CNL, run 2026-11-11 (Phase 1)

Scope: stage reports 01-09 (plus 02 pass files and the errata) against the source files in runs/cnl-2026-11-11/inputs (AR FY2025-26, results Q4FY26 / Q1FY27 / Q2FY27, Q2FY27 and Q4FY26 decks, three CNL transcripts, three-peer transcripts, announcements, CRISIL rationale, CNL-Data_Sheet.csv). Page anchors were opened in the page-marked text. Stage 8 and 9 web citations are marked unanchored-web and were not verified.

## Result in one paragraph
No MISMATCH on any Gate 0 scorecard input; 180 of 180 mandatory figures checked and match. Zero CRITICAL, zero MAJOR. Five MINOR rows (two labelling traps, one derived-figure basis, one self-corrected arithmetic slip, one wrong page anchor). Phase-1 reports contain no verdict-card or Section 1B pillar inputs, so the mandatory tier is the Gate 0 scorecard.

## Findings table

| # | Severity | Report location | Claimed + anchor | Source truth + location | Note |
|---|---|---|---|---|---|
| 1 | MINOR | B01 s.0 item 2 | "Borrowings repaid net 154.85" (results Q2 FY27 p.13) | p.13 has repayment line (15,485.04 lakh) and a separate proceeds line +2,458.85 lakh; net of both = 130.26 Cr. 154.85 is the gross repayment line (also equals the fall in current borrowings, p.11) | Gross vs net label. Not a scorecard input. Figure exists at anchor. |
| 2 | MINOR | B05 2A row 7, 2B, 2D; B05 block input_gaps | FY26 CFO -273.10 Cr (Q4FY26 results -27,310.01 lakh); "-271.9 memory carried, filing governs" | Q4FY26 results prints -27,310.01 (confirmed). AR p.98 prints (27,188.34) = -271.88; Q2 FY27 deck p.7 and p.9 print 271.88, p.8 prints 273.10 | Two filings print two FY26 CFO values. B01, B03, B04 carry -271.88 (correct, AR p.98). B05 note implies -271.88 is not in a filing. Unlabelled cross-document basis difference. No decision change. |
| 3 | MINOR | B03 3A, 6A row 1 | CON EBITDA incl OI 10,400.13 lakh "PBT + finance + depreciation" | 8,176.20 + 2,066.43 + 152.10 = 10,394.73 (= Rs 103.95 Cr, AR p.7). 10,400.13 uses PBT before associate (8,181.60) | Basis unlabelled, 5.40 lakh. |
| 4 | MINOR | B07 1C | brand CAGR 85.5% | (2,400/380.86)^(1/3) - 1 = 84.7% | Erratum already appended to the report. |
| 5 | MINOR (source_fidelity true) | B07 F1 | "no options in operation (AR p.43-44)" | AR p.41, Directors' Report iii. Not on p.43-44 | True statement, wrong page. Erratum already gives p.41. Stands until body fixed. |

## Struck under 5b (5 rows)
AR p.46 net margin 2.99% vs derived 2.98% in B03 (labelled derived; basis difference correctly labelled); SCL turnover 29,773.63 (AOC-1) vs 29,773.64 (Other Matters) (faithfully transcribed anomaly); 2,699.78 vs 2,699.77 and 531.74 vs 531.75 (rounding, same value); "CON tax equals SA tax 1,153.11" in B02 (current tax is equal at 1,153.11 and total tax at 1,146.91, both true).

## What was verified (highlights)

Gate 0 (B01), all 180 figures:
- Screener CSV: every PBT, interest, equity, reserves, borrowings, sales, PAT, CFO, receivable, inventory value in the report matches the CSV. Re-derived and matched: capital employed (69.22 ... 687.90), EBIT, ROCE series (18.5, 19.0, 17.4, 21.2, 21.1, 23.5, 19.6, 14.9) and median 19.3; ROE series and median 18.5; cumulative CFO -328.71 and PAT 215.90; receivable days series; revenue CAGR 33.0% and PAT CAGR 40.1%; EBITDA 91.05 and margin 3.37% (FY19 2.79%); ND/EBITDA 3.32x; EBIT/interest 4.96x; D/E 0.89; M11 CAGRs 24.7% and 44.9%.
- AR p.97/98: owners' PAT 6,187.14, NCI 842.15 (8.42 Cr), consolidated PBT 81.76, PAT 70.29, revenue 2,704.62; TA 937.24, CA 921.66, CL 548.38, total equity 387.29, payables 185.11 (135.35 FY25), CFO (27,188.34), capex 330.04 / 281.66.
- AR p.104 Note 8 related-party receivables 3,244.81; p.105 promoter 56.62% / 56.60%; p.109 Note 34 contingents 600.01 (sum re-added), bank guarantee 1,058.13, total 16.58 Cr; p.10/46 31+ branches, 10,000+ partners.
- Results Q2 FY27: standalone PBT 45.82, PAT 34.35, Q2 12.65; consolidated tax 11.47 and 4.19; H1 CFO 351.24 with payables +281.90, other liabilities +192.83, receivables -51.60, other assets -116.39; Sep-26 balance sheet (payables 467.01 vs 185.11, other current liabilities 215.90 vs 19.08, receivables 616.71, cash 206.36 + 17.60, borrowings 24.60 + 169.40, equity 400.97); brand segment FY26 380.86 / 126.29 / 33.2%, Q2 143.12 / 46.76 / 32.7%.

Sample tier:
- B03: 15 AR-grep batches (SA/CON CFO, SCL purchases, Click Retail, HK reserves, CARO ii(b) four quarters, audit fee, KMP pay, 750 Cr SCL limit, shareholder counts, ratio table AR p.46, Note 43, contingent-liability lines, segment note); derived ratios re-computed (ROCE 14.4%, interest cover 4.96x, ND/E, DuPont, receivable days).
- B04: deck slides 7-9, 15, 17-18, 31-32 (opex 78.93 / GP 143.94, H1 PAT 21.66 and 39.47, gap 17.81 = 45.1%), Q4 deck p.14 TReDS 171.19, BSNL 1,700 + 1,200 vs 3,194.83, AR p.107, p.112 segment table, incremental margins.
- B05: all 21 promise rows' anchors in transcripts and filings (Honeywell 369.61 / 231.98 / 137.6, PAT 70.29, Q3 total income 920.28, 359-360 misquote, 13-14% receivables, 20-22 Cr marketing, 11-12% PAT, 18% EBIT), market-entry 6.66% vs 3.36%, LTM revenue 2,880.01 and 21.4%, Zicom 25.50 + 25.00, 2,25,000 shares, 20.09 Cr, FCI 35.89 Cr.
- B06: 20 peer figures spot-checked (CPPLUS 45.4%, 4,220.8, 6,000-6,500, 31.8%, 13.7%, CCC 64; Redington 213 Cr, 3,800 Cr, TSG +91%, +48%, WC 30/32/35, $3 million, 30-50%; RPTECH 2.90%, +72 bps, 3.38%, WC 56-60, 0.01-0.02%, IDC -5 to -10%).
- B07: ESOP 2,00,000 and 8,599,692 votes, 82.44% / 1,64,88,926 / Rs 1,133.33, CRISIL ~25% vs 50-60% and 40% trigger, CAGR arithmetic, sums 29.4% to 35.0%.
- B08: Ketan 84,39,520 (56.20%), customs 2,30,33,813, Click Retail 47.74 vs 2.23, SCL flows. Web items excluded.
- B09: AR Note 23.2B India 1,79,713.32 / 67,840.71, outside India 90,263.93, deck slides 10, 20-24 market sizes, and the full TAM/SAM/SOM chain re-computed (41,675; 70,745; 20,081; 3,237; 4,035; 21.7%/17.6%; 15.3%/12.8%; 11.2x; 20.4%).

## Coverage statement
- Mandatory tier: 180 of 180 checked (Gate 0 report figures that feed a block score, deal-breaker, load-bearing fact or sensitivity; unchecked: none). Phase-1 reports hold no verdict-card or Section 1B pillar inputs; the figures that will feed them (CFO, receivable days, HK share of PAT, ND/E, brand margin, H1 FY27 CFO, market cap) are matched in the sample tier.
- Sample tier: 455 material numbers counted in B02-B09 (a number counts if it feeds a table cell, ratio, flag, monitorable or classification); 337 checked; about 118 unchecked, mostly B06 peer sub-quotes beyond the spot-checked 20, B03 governance cells and pass-1/pass-2 working notes.
- numbers_checked 517 (180 + 337). Acceptance 99% (512 clean of 517).

```yaml
stage: B12a
company: "CNL"
run_date: "2026-11-11"
model: claude-sonnet-5-5
status: complete
numbers_checked: 517
mandatory_checked: 180
mandatory_total: 180
findings:
  - {severity: "MINOR", location: "B01 report section 0 item 2 (Gate 0 load-bearing facts), 'Borrowings repaid net 154.85 (p.13)'", claimed: "net borrowings repaid 154.85 Cr (results Q2 FY27 p.13)", source_truth: "p.13 prints one repayment line (15,485.04 lakh = 154.85 Cr) and a separate proceeds line +2,458.85 lakh (24.59 Cr); net of both lines = 130.26 Cr. 154.85 is the gross repayment line, not net", note: "Gross-vs-net label trap. Figure exists at the cited anchor; not a scorecard input.", source_fidelity: false}
  - {severity: "MINOR", location: "B05 report 2A row 7, 2D, 2B and block input_gaps ('memory carried -271.9, the filing governs')", claimed: "FY26 CFO -273.10 Cr (Q4FY26 results); -271.9 described as memory-only", source_truth: "Q4FY26 results prints (27,310.01) lakh; audited AR p.98 prints (27,188.34) lakh = -271.88 Cr; Q2 FY27 deck p.7 and p.9 print 271.88, p.8 prints 273.10", note: "Unlabelled cross-document basis difference; both values exist at their anchors; decision unaffected.", source_fidelity: false}
  - {severity: "MINOR", location: "B03 report 3A, 6A row 1: CON EBITDA incl OI 10,400.13", claimed: "10,400.13 lakh labelled PBT + finance cost + depreciation", source_truth: "8,176.20 + 2,066.43 + 152.10 = 10,394.73 lakh (= Rs 103.95 Cr); 10,400.13 uses PBT before associate (8,181.60)", note: "Derived figure, basis unlabelled; 5.40 lakh.", source_fidelity: false}
  - {severity: "MINOR", location: "B07 report 1C implied brand CAGR", claimed: "85.5% a year", source_truth: "84.7% ((2,400/380.86)^(1/3)-1)", note: "Already corrected by appended erratum; body unchanged.", source_fidelity: false}
  - {severity: "MINOR", location: "B07 report F1: 'no options in operation (AR p.43-44)'", claimed: "AR p.43-44", source_truth: "AR p.41 (Directors' Report item iii); not on p.43-44", note: "Statement true, page wrong; erratum already gives p.41.", source_fidelity: true}
critical_count: 0
major_count: 0
minor_count: 5
false_positives_struck: 5
material_universe: 635
acceptance_rate: 99
coverage_note: "Mandatory 180 of 180 (Gate 0 scorecard figures; no verdict-card or Section 1B inputs exist in phase-1 reports). Sample: 455 material numbers in B02-B09, 337 checked, about 118 unchecked (B06 peer sub-quotes beyond 20 spot-checks, B03 governance cells, pass-1/pass-2 working notes). B08 aggregator items and B09 third-party market sizes are unanchored-web, not verified; B09 arithmetic on them re-computed and holds. FY26 CFO prints -271.88 Cr in AR p.98 and Q2 FY27 deck and -273.10 Cr in Q4 FY26 results; each stage cites its own source correctly (finding 2)."
```
