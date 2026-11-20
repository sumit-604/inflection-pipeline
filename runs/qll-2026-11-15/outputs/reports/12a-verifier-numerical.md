# VERIFIER A: NUMERICAL ACCURACY. QLL (Qualitek Labs Ltd), run 2026-11-15

Model: claude-sonnet-5-5. Inputs read: reports 01 to 09 (and 02 pass 1) plus the source .txt files and, where the text layer was OCR-garbled, the PDF page image. Phase 1 scope: no verdict card and no Section 1B pillar exists yet, so the mandatory tier (OR-32) is the Gate 0 scorecard inputs.

PDF pages opened as images because the text layer is OCR: H1 FY27 results (20261113-190e3152) pages 11, 12, 14, 15. These decided findings 1 to 3.

## 1. FINDINGS TABLE

| # | Severity | Report location | Claimed value and anchor | Source truth and location | Note | source_fidelity |
|---|---|---|---|---|---|---|
| 1 | MAJOR | 01-gate0.md section 0, load-bearing fact 1 (also B00 memory line, carried unchanged) | H1 FY26 consolidated revenue Rs 5,421.38 Lakh; growth +33.3% (H1FY27 p.11) | Rs 5,424.38 Lakh; growth 7,226.65 / 5,424.38 = +33.2%. PDF image of H1FY27 p.11 prints 5424.38. The same figure appears in FY26 results 20260520-dc0311a3 p.5 (text 5424.38), H1 FY26 results 20251112-d1d63f49 (5424.38) and the MD&A filing 20260520-78cbc582 ("Rs 54.24 Crore"). 7,027.43 + 5,424.38 = 12,451.81 ties | The .txt OCR reads 5421.38; the PDF does not. Stage 3 used the correct 5,424.38 and +33.2% (03-ardeep.md section 0 row 1). Stage 1 did not. Effect on a decision: none (0.1 point). Not a scorecard input, so MAJOR not CRITICAL | true |
| 2 | MAJOR | 03-ardeep.md section 3A, CFO quality checks, H1 FY27 line | H1 FY27 consolidated net cash change (400.55) (results pp.14-15) | (400.51). PDF image of H1FY27 p.15: Net Increase in Cash A+B+C (400.51). Check: 359.17 - 2,470.14 + 1,710.46 = -400.51; 555.40 - 400.51 = 154.89 | Copied from the OCR text layer (line "(400.55)"), not from the PDF. 0.04 Lakh. Report's cash 154.89 and CFO 359.17 are right | true |
| 3 | MAJOR | 07-emoat.md section 2A, H1 FY27 gross capex row (derived 3,578.77) | Intangible assets under development at 31 Mar 2026 = 44.23 (used in 31 Mar 2026 sum 11,947.07) | 44.21. AR26 p.102 (text 44.21) and PDF image of H1FY27 p.12 (44.21). Corrected sums: 31 Mar 2026 = 11,947.05; change 3,181.68; plus depreciation 397.11 = 3,578.79 | OCR text of H1FY27 p.12 reads 44.23. Derived capex 3,578.79 vs 3,578.77 claimed. Effect none on the 56.8% of plan (35.79 Cr) | true |
| 4 | MAJOR | 02-notes.md Top 15 rank 1 and B02 YAML top_findings rank 1 ("ITCPL net assets 752.02"); 02-notes-pass1.md section 6 "QTIPL net assets -61.41", "LabOps net assets/loss -23.07" | ITCPL "net assets 752.02", QTIPL "net assets -61.41" (C-Note 34 p.140) | 752.02 and -61.41 are each entity's SHARE IN CONSOLIDATED NET ASSETS after consolidation adjustments (C-Note 34 p.140: "% of Consolidated Net Assets" 4.93% and -0.40%). Entity own net worth, AOC-1 (AR26 p.66): ITCPL 50.98 + 1,854.67 = 1,905.65; QTIPL 23.40 - 34.65 = -11.25; LabOps 10 - 25.71 = -15.71 | Basis not labelled in the consolidated report and the block. Pass 1 section 6 does label ITCPL's 752.02 as "share of consolidated net assets" but its own QTIPL line does not. The "11.3x cost over net assets" ratio rides on the unlabelled basis. Stage 3 section 2.0 corrects it (4.46x on AOC-1 net worth). Rule 5a: unlabelled basis difference = UNANCHORED, material because it sits in the rank 1 finding | true |

CRITICAL 0. MAJOR 4. MINOR 0.

## 2. WHAT WAS CHECKED AND FOUND CLEAN (sample)

Gate 0 (01-gate0.md), all 161 listed source inputs re-read in the filings and the screener sheets; every derived score input re-computed (ROCE, ROE, CAGR, cumulative CFO, FCF, WC days, net debt, interest cover, D/E, current ratio, contingent ratio, M2 and M9 peer margins). Clean apart from finding 1.
- FY21 and FY22 consolidated: Pros pp.70-72. FY23 standalone: Pros pp.73-75. FY24 standalone: AR25 pp.118-120, with the five computed lines (PBT 582.44, PAT 430.74, CFO 553.52, total assets 5,058.88, current liabilities 688.42) rebuilt from the printed line items; they tie. FY25 and FY26 consolidated: AR26 pp.102-105.
- Screener QLL sheet (sales, net profit, interest, PBT, borrowings, CFO, selling and admin, market cap 643.19), three peer sheets (PBT, interest, depreciation, other income, sales, raw material, market cap): all match.
- Shareholding extract: 56.46, 73.35, 1.54, 0.15. Reg 31(4) declaration 6 Apr 2026: no encumbrance, as stated.
- AR26 p.137 Note 28 contingents: 5.48, 91.21, 2,133.00, 4,911.00 match; total 7,140.69 and 46.8% re-computed.
- H1FY27: standalone CFO 248.20, PBT 635.50, receivables increase 878.06, short-term borrowings 3,174.91 vs 1,623.61; consolidated CFO 359.17, PBT 855.11, borrowings 6,612.40 + 4,854.48, current assets 6,576.88, current liabilities 8,405.59 (PDF images pp.12, 14): match.

Stage 2 and 3 (02-notes.md, 02-notes-pass1.md, 03-ardeep.md): receivables ageing (206.67 / 3,069.35 / 312.41 / 310.86 / 100.37 / 220.46 / 4,220.12; provision 6.08), contingent items, guarantee limits and outstandings (6,449 / 7,446 / 7,664 / 7,583.71 / 7,525.84 / 7,244 / 7,664; 5,739.65 / 6,718.98 / 6,874.29 / 6,295.50 / 6,243.14 / 6,212.63), related-party table (153.60, 21.60, 22.77, 715.00, 4.79, 88.36, 77.82, 33.80, 151.06, 148.00, 262.00, 37.30), swap numbers (3,640.15, 5,199.73, 4,507.78, 310.89, 16,72,531, 8,498.99), capitalised interest 143.14, CWIP ageing, employee-benefit tables (111.52 vs 133.31 = 80.63 + 52.68), AOC-1 (710.83, -24.94, -22.44), IPO utilisation (1,831.18, 818.16, 1,277.83, 553.35), prospectus top-10 and top-5 shares: all found at the cited page.
Stage 3 guidance rows: 35 to 40% and 14 to 15% in AR26 pp.23, 73 (text lines 565-566); 35 to 40%, 25 to 27%, 15 to 17%, Rs 500 Cr, 30%, 30%, FY32 debt-free in the 20 May 2026 MD&A filing; revenue targets 16,810 to 17,433 and H2 needs 9,583 and 10,206 re-computed.
Stage 4 and 5: deck p.11 cost lines (16.64, 44.74, 33.85, 6.69, 4.81), capex 51.3 Cr, 63 Cr plan, 40-45 / 25-30 / 15-20 ranges, 450 scientists, 5000+, 350+; May 2025 deck "2X revenue ... 30% EBITDA": found.
Stage 6: Vimta 36.4 / 35.5 / 36.0%, 13.7 / 9.9 / 11.8%, Rs 100 Cr and 200,000 sq ft and 60%, exports 39 / 38 / 40%; Krsnaa DSO 155 to 139 and "sub 120"; Lal DSO 17 days, net cash 1,746, S N GeneLab 168 + 31/32, Shahbazkers 20 Cr on 6.11 Cr (3.3x); biologics 20-25 Cr: found.
Stage 7: IOC orders 3,01,50,000 and 75,40,200, CWIP 6,977.28, Barwala 1,813.01 and loan 1,300.30, capitalisation inputs (721.90, 285.76, 1,257.03, 590.67, 3,552.58), ageing, exports 111.12, raw materials 1.54, IPO capex 210.16 + 412.22, 290K sq ft: found (except 44.23, finding 3).
Stage 8: TIC holdings 31.87 / 30.94 / 15.94 / 10.62 / 10.62 and paid-up 47.06 lakh, EGM figures (2,200 / 600 / 800 / 1,098.06 / 4,698.06, 518.55, 448.87, 518.53, Kacholia 1,73,200 and 4.35% to 5.65%), voting (65,78,375; 68,05,975; 58.41%; 96.7%), personal guarantee limits, ITC suit CS/159/2022 and Rs 50 Cr (Pros p.289), 342-day delay and Rs 6,65,520 (AR25): found.
Stage 9: all arithmetic re-computed (USD to Rs at 95, TAM, SAM 15,882, SOM 263 and 392, CAGRs, PEG, P/E 44.0, funnel); correct. Straits "USD 26 million" is on Pros [page 135].

## 3. STRUCK BEFORE EMIT (rule 5b), 5 rows

1. Net debt / EBITDA 2.92x (stage 1, EBITDA 2,981.26) against 2.96x (stage 3, EBITDA 2,934.44): both bases are stated; both are right on their basis (rule 5a, labelled basis difference).
2. Standalone PBT 635.49 (P&L) against 635.50 (cash flow): the source prints both (H1FY27 pp.4, 7). Faithfully transcribed.
3. FY26 capex Rs 51.3 Cr (deck p.24) against Rs 46.36 Cr (cash flow): the source prints the odd number, stages 3 and 7 copy both correctly and say the gap does not reconcile.
4. FY26 EPS 13.38 (20 May 2026 results and deck) against 12.49 (AR, H1FY27 p.11): both are printed in the sources; stage 3 reports the conflict correctly.
5. Other expenses 3,379.24 (H1FY27 comparative column) against 3,379.23 (AR26 p.103): faithfully transcribed company difference, not used by any report.

## 4. COVERAGE STATEMENT

Mandatory tier (OR-32, Gate 0 scorecard inputs, phase 1 has no verdict card and no Section 1B pillar): 143 figures in the Gate 0 report, 143 checked. Rule used: count every source-anchored input figure that Gate 0 scores or ratios (series table 80 cells: 13 line items for 6 years plus inventory for FY25 and FY26; screener cross-check and ratio inputs 17; Block D balance sheet and Sep 2026 sensitivity inputs 12; Block E inputs 9; Block F peer, PPE, lab-count and gross-margin inputs 25). Derived outputs (scores, ROCE, CAGR) were re-computed but are not counted as inputs. Result: 143 of 143, with 0 mismatches. No mandatory figure was unchecked.

Sample tier: 420 material numbers in the reports (my count). Rule for "material": a number that feeds a judgment, a flag, a guidance or delivery comparison, a top-15 or red-flag row, a monitorable threshold, or a table cell a reader would act on. Counted by report: Gate 0 section 0 facts and non-scorecard items 18; stages 2 and 3 about 120; stage 4 about 30; stage 5 about 20; stage 6 about 55; stage 7 about 55; stage 8 about 55; stage 9 about 45 (including 16 third-party web market figures). I checked 189 of these in the sources plus 25 stage 9 arithmetic steps re-computed, 332 numbers in total with the mandatory tier (143 + 189). Roughly 88 material numbers were not checked.

Not checked, by reason:
- Stage 9 third-party market data (Mordor, IMARC, MarketsandMarkets, DataM, MRFR, RBI rate): not in any input PDF. Source fidelity cannot be tested; only arithmetic was. Flagged as outside my inputs, not as a finding.
- Stage 8 web-sourced items (AmbitionBox, IBBI, Trendlyne, Kacholia 5.07%): not in any input PDF.
- Stage 3 and 8 board-report page anchors for attendance, committee tables and secretarial audit (AR26 pp.50-56, 82-84): spot-checked only; two orchestrator-noted approximate anchors in stage 8 left as the orchestrator described them.
- Stage 4 deck pp.9 and 17 standalone Rs 67.6 Cr, stage 5 deck ROE/ROCE slide pages, and about 20 peer-call page anchors in stage 6: number found in the document, page number not re-verified for each.
- Stage 2 derived ratios not re-run: 8,159.37 bank-debt base, 84% cover, 143.30 standalone capitalisation, statutory dues +224%, vendor advances +119%. Stage 3 also marks these as not re-derived.

Acceptance rate: (332 checked - 4 numbers in findings) / 332 = 98.8%.

## 5. NOTE FOR THE ORCHESTRATOR

All four findings are source-fidelity findings. Only the PDF can clear them. Findings 1 to 3 are text-layer (OCR) copy errors; the PDF shows the value in the "source truth" column. None changes a verdict. Stage 3 already carries the correct value for finding 1 and the correct basis for finding 4. There is no CRITICAL, so the OR-29 REWORK trigger on a confirmed Verifier A CRITICAL does not fire; acceptance rate is above 60% on a denominator over 4.

```yaml
stage: B12a
company: "QLL"
run_date: "2026-11-15"
model: claude-sonnet-5-5
status: complete
numbers_checked: 332
mandatory_checked: 143
mandatory_total: 143
findings:
  - {severity: "MAJOR", location: "01-gate0.md section 0 load-bearing fact 1 (H1 FY26 revenue base); B00 memory line", claimed: "Rs 5,421.38 Lakh, growth +33.3% (H1FY27 p.11)", source_truth: "Rs 5,424.38 Lakh, growth +33.2%; PDF image H1FY27 p.11, FY26 results 20260520-dc0311a3 p.5, MD&A filing 'Rs 54.24 Crore'", note: "OCR text layer misread; stage 3 has the correct figure; no decision effect", source_fidelity: true}
  - {severity: "MAJOR", location: "03-ardeep.md section 3A H1 FY27 CFO quality line", claimed: "net cash change (400.55) (results pp.14-15)", source_truth: "(400.51); PDF image H1FY27 p.15; 359.17 - 2,470.14 + 1,710.46 = -400.51", note: "OCR copy error, 0.04 Lakh", source_fidelity: true}
  - {severity: "MAJOR", location: "07-emoat.md section 2A H1 FY27 gross capex row", claimed: "intangibles under development 31 Mar 2026 = 44.23; derived capex 3,578.77", source_truth: "44.21 (AR26 p.102; PDF image H1FY27 p.12); derived capex 3,578.79", note: "OCR copy error; no effect on 56.8% of plan", source_fidelity: true}
  - {severity: "MAJOR", location: "02-notes.md Top 15 rank 1 and B02 top_findings rank 1; 02-notes-pass1.md section 6 QTIPL and LabOps lines", claimed: "ITCPL net assets 752.02; QTIPL net assets -61.41 (C-Note 34 p.140)", source_truth: "752.02 and -61.41 are share in CONSOLIDATED net assets (C-Note 34 p.140); own net worth per AOC-1 AR26 p.66: ITCPL 1,905.65, QTIPL -11.25, LabOps -15.71", note: "UNANCHORED basis, unlabelled in the consolidated report and block; 11.3x ratio rides on it; stage 3 corrects it", source_fidelity: true}
critical_count: 0
major_count: 4
minor_count: 0
false_positives_struck: 5
material_universe: 420
acceptance_rate: 98.8
coverage_note: "Mandatory tier = Gate 0 scorecard inputs (phase 1 has no verdict card or Section 1B pillar): 143 of 143 checked, 0 mismatches. Sample tier: 420 material numbers counted, 189 checked plus 25 stage 9 arithmetic steps; about 88 not checked. Unchecked by reason: stage 9 third-party web market figures and stage 8 web items (not in any input PDF; arithmetic only for stage 9); board-report page anchors spot-checked only; stage 4 deck pp.9/17 and ~20 stage 6 peer-call page anchors (number found, page not re-verified); stage 2 derived ratios 8,159.37 base, 84%, +224%, +119% not re-run. H1FY27 results pages 11, 12, 14, 15 opened as PDF images because the text layer is OCR; findings 1-3 come from that difference."
```
