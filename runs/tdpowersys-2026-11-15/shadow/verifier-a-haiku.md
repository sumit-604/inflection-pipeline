# VERIFIER A (SHADOW): NUMERICAL ACCURACY. TDPOWERSYS, run 2026-11-15

SHADOW RUN (operator ruling 2026-10-11). These findings bind nothing. They do not enter B12a, the confidence delta, REWORK, the verdict or the synthesis. Rows with source_fidelity: true would bind on a live run. Model: claude-haiku-5-5.

Inputs read: outputs/reports 01-gate0, 02-notes (final report, with the orchestrator appendix), 04-bizmodel, 05-concall (sections 0, 0A, 1A to 1C, 2A rows), 08-promoter, 09-tam. Sources checked on the .txt route: AR FY2025-26 (consolidated and standalone statements and notes, MD&A, Board's report), screener Data_Sheet CSV (read in full), Q2 FY27, Q1 FY27 and Q4 FY26 results, Q2 FY27 presentation, Reg 31 patterns (30 Sep 2026 and 12 Oct 2026), CRISIL rationale (22 Jun 2026), Q1 FY27 transcript, Q4 FY26 and Q3 FY26 transcripts (text greps), prior-year AR (other/) for PY comparatives.

Not read in full in this pass: 03-ardeep, 06-peers, 07-emoat. Their figures sit outside the material universe, so the universe is understated for those stages. Gate 0 is the only stage report with the scorecard, so the mandatory tier is complete for scorecard inputs.

## 1. Findings

| # | Severity | Tier | Source fidelity | Location | Claimed | Source truth | Note |
|---|---|---|---|---|---|---|---|
| F2 | MAJOR | sample | true | 02-notes section 3 item 7, P3-02 sensitivity (4,189.10 / 19.4 percent), section D Q1 | Capital creditor build 1,596.63 lakh, stated as an inference | Not printed in the AR. No capital creditor line in notes 2, 3, 22. S cash flow p.130 PPE payment (10,376.36) equals accrual additions 10,302.84 plus CWIP change 73.52, so no 1,596.63 residual shows in the capex lines. Derivation not shown. | Material UNANCHORED. The 19.4 percent sensitivity depends on it. Clearance: show the arithmetic from printed lines, or drop the figure. |
| F1 | MINOR | mandatory | false | 01-gate0 section 1 ROCE table (FY26 interest), section 4 D2 | Interest FY26 7.60 Rs cr (screener Interest row); EBIT 333.72; cover 43.9x | Data_Sheet Interest FY26 = 7.60, transcription correct. AR consolidated finance costs FY26 = 190.32 lakh = Rs 1.90 cr (AR P&L; MD&A "Interest and Finance Charges 190.32"). | Correct on its screener label. Not reconciled to the AR line. Cover would be about 172x on AR basis (328.02 / 1.90). Scored 5 either way. FY26 EBITDA margin appears as 18.07 percent (Gate 0), 17.76 percent (B03, stage 5, AR basis) and 18.3 percent (deck). Counted as not clean for acceptance. |
| F3 | MINOR | sample | false | 04-bizmodel section 0 row 3, section 1 cash conversion | H1 FY27 "receivables rose Rs 209.7 Cr (20,965.02 lakh)" | 20,965.02 is the cash-flow line (Q2 FY27 results p.9). Balance sheet movement 95,292.50 less 74,208.77 = 21,083.73 lakh (Rs 210.8 Cr), results p.8. | Basis labelled only in the anchor, not in the text. Value exists at its page. |
| F4 | MINOR | sample | false | 04-bizmodel section 0 row 1 (book-to-bill sentence) | Q2 FY27 revenue Rs 841.4 Cr | 84,131.88 lakh = Rs 841.32 Cr (results Q2 FY27 p.7). Rounds to 841.3, the figure 04 uses elsewhere. | Rounding slip in one sentence. Book-to-bill 0.98 unaffected. |

Counts: critical 0, major 1, minor 3. No CONFIRMED CRITICAL, so no REWORK trigger from this shadow run.

## 2. Coverage, two tiers

Mandatory tier (OR-32): 146 of 146 checked. The 146 cells are the Gate 0 scorecard input cells in 01-gate0.md:
- Screener Data_Sheet, FY17 to FY26: PBT, interest, equity plus reserves plus borrowings (CE), ROE, sales, net profit, CFO, receivables, and FY26 scalars (inventory, cash and bank, depreciation, other income, borrowings, net worth, EBITDA inputs). ROCE, ROE, receivable days and the CFO sum were recomputed from these rows.
- AR scalars: FY25 and FY26 capex (PPE and intangibles), trade payables (MSME and other, FY25 and FY26), FY26 current assets and liabilities, total assets, borrowings, R&D 872.50 (Board's report, Research and Development), contingent liabilities (consolidated Note 39, p.230, all six lines), customer shares (consolidated p.238; standalone p.170), promoter table at 31 Mar 2024, 2025 and 2026, and DF Power and USA Inc related-party values.
- Q2 FY27 results scalars: H1 revenue, Sep-26 and Mar-26 receivables, other current liabilities, H1 CFO and H1 FY26 CFO, other payables line, H1 capex, H1 PAT, cash, bank, current assets and liabilities (Sep-26 sums recomputed from printed lines), net worth (share capital plus other equity), nil borrowings.
- Reg 31 (30 Sep 2026): 85,207,322 promoter shares, 313,706,860 total, 27.16 percent, pledge items "No".
- No verdict-card or Section 1B pillar input exists in this run (stages 11 and 13 not run).

Sample tier: material universe 118 figures enumerated in 02, 04, 08 and 09 and the 05 sections listed above. 97 checked, 21 not checked (named in the YAML coverage_note). Checked: 94 clean, 3 not clean (F2, F3, F4). Not checked include 41,342.32 (S Note 42 subsidiary sales), 460.34 (consolidation adjustment), 824.87 (GST demand, text only), the 84 percent top-10 customer share, S commission 410.00, 14,813.73 Mn and 8,413.19 Mn (deck), 4,008.73 and 7,855.88 (capital commitments, AR p.162), and the 08 Trilegal, Trident and allotment figures.

Universe and rate: material_universe = 146 mandatory plus 118 sample = 264. numbers_checked = 243. Acceptance: mandatory 145 of 146 (99.3 percent, F1 counted as not clean), sample 94 of 97 (96.9 percent), overall 239 of 243 (98.4 percent).

## 3. Rows struck under rule 5b

Two candidate rows were dropped during the check and never entered the table:
- 04 section 1D "non-current assets Rs 311.0 Cr (31,102.70 lakh)". The consolidated segment note at p.238 prints 31,102.70 as the carrying amount of non-current assets (India 30,667.17 plus outside India 435.53), and 10,867.70 as FY26 additions with 3,876.65 for FY25. Label and figures are correct.
- The 1,986.03 tax demand and its consolidated anchor. Consolidated Note 39 (p.230, lines 30507 to 30514) prints 12,246.21, 1,400.45, 120.85, 1,986.03 and 13.12, so the Gate 0 anchor holds.

## 4. Web-sourced figures (08 and 09)

These have no PDF in the corpus and cannot be checked against a PDF. Treatment:
- None sits in the mandatory tier, so no coverage shortfall arises. They are logged NOT CHECKED (web source).
- Where a web figure also appears in a filing, it was checked on the filing: promoter counts and percentages against Reg 31, QIP and allotment figures against the 12 Oct 2026 and 20 Sep 2026 filings where located.
- The AR market-size chart values in 09 (48.7, 52.8, 107.6, 27.1, 34.9, 28.84, 21.11, 166.84, 5.9, 8.92, 32.51, 61.13, 8.64 percent) are present in the AR text and were checked there.
- CRISIL figures in 09 (Rs 140 Cr project, Rs 60 to 80 Cr capex, 111 countries, about 70 percent of sales overseas) are present in the rationale.
- Not covered: the USD/INR rate of 95.25 (web, MSEI archive), alternator, peer and market-share figures, and the steam and hydro market figures (NOT FOUND in the sources).

## 5. Observations outside numeric scope (not scored)

- FY26 EBITDA margin appears on three bases (18.07, 17.76, 18.3 percent). Only Gate 0 labels its basis (screener). Stage 5 and B03 use the AR finance cost. Covered by F1.
- 09 section 5E says "CRISIL expects 17-18%". The rationale says operating margins were "maintained at 17-18%". The number is transcribed correctly. The verb is a characterisation, so it is not scored under Verifier A.
- 04 cites the Q1 FY27 call as 12 Aug 2026. The transcript confirms the call was held 12 Aug 2026. Consistent.
- 05 quotes the FY27 guide steps (2,200+, 2,400+, 2,600, 2,900 to 3,000). All four trace to the transcripts or the deck (Q3 FY26 transcript, AR text, Q1 FY27 transcript, deck slide 38 line). The 2,400+ figure also appears in the AR text, not page-anchored in this pass.

## 6. Shadow outcome

Mandatory tier: no CRITICAL, no MISMATCH, no ANCHOR NOT FOUND, no source-fidelity row. Sample tier: one source-fidelity row (F2, MAJOR). Under OR-29 this would not fire REWORK. The result binds nothing in this run.

Block: runs/tdpowersys-2026-11-15/shadow/verifier-a-haiku.yaml

```yaml
stage: B12a
company: "TDPOWERSYS"
run_date: "2026-11-15"
model: claude-haiku-5-5
status: complete
numbers_checked: 243
mandatory_checked: 146
mandatory_total: 146
findings:
  - severity: "MAJOR"
    location: "02-notes.md section 3 item 7 and P3-02 sensitivity (CFO ex advances less capital creditor build, 4,189.10 / 19.4 percent); section D question 1; section A rank 2; orchestrator appendix analyst_note"
    claimed: "capital creditor build 1,596.63 lakh, stated as an inference that it sits in CFO"
    source_truth: "NOT PRINTED in the AR text (no capital creditor line in standalone or consolidated notes 2, 3, 22). S cash flow p.130 PPE payment (10,376.36) equals accrual additions (10,302.84) plus CWIP change (73.52), so no 1,596.63 residual is visible in the capex lines. Derivation not shown in the report."
    note: "Material UNANCHORED. The 19.4 percent sensitivity and the open question depend on this figure. Clearance route: show the arithmetic from printed AR or results lines, or drop the figure. Shadow run: binds nothing."
    source_fidelity: true
    tier: sample
  - severity: "MINOR"
    location: "01-gate0.md section 1 ROCE table (FY26 interest), section 4 D2 (interest cover 43.9x), section 0 item 1 basis note"
    claimed: "FY26 interest 7.60 Rs cr (screener Data_Sheet Interest row); EBIT 333.72; interest cover 43.9x"
    source_truth: "Data_Sheet Interest FY26 = 7.60 (transcription correct). AR consolidated Finance costs FY26 = 190.32 lakh = 1.90 Rs cr (AR consolidated P&L line Finance costs; MD&A Interest and Finance Charges 190.32). The two rows differ by 5.70 Rs cr."
    note: "Value is correct on its screener label, so no transcription finding. Basis is not reconciled to the AR line. On AR basis interest cover would be about 172x (328.02 / 1.90). Scored 5 either way, so no score change. Cross-stage spread for FY26 EBITDA margin: 18.07 percent (Gate 0, screener), 17.76 percent (B03 and stage 5, AR finance cost), 18.3 percent (deck slide 34). Name the basis in the scorecard. Counted as not clean for acceptance."
    source_fidelity: false
    tier: mandatory
  - severity: "MINOR"
    location: "04-bizmodel.md section 0 row 3 and section 1 cash conversion (FLAG-CASH)"
    claimed: "H1 FY27 receivables rose Rs 209.7 Cr (20,965.02 lakh)"
    source_truth: "20,965.02 is the cash-flow line Decrease/(Increase) in trade receivables (Q2 FY27 results p.9). Balance sheet movement 95,292.50 less 74,208.77 = 21,083.73 lakh (Rs 210.8 Cr), results p.8. Text does not name the cash-flow basis."
    note: "Unlabelled basis in the text (labelled only in the anchor). Value exists at the cited page. Not material enough for MAJOR. Shadow run: binds nothing."
    source_fidelity: false
    tier: sample
  - severity: "MINOR"
    location: "04-bizmodel.md section 0 row 1 (book-to-bill sentence: inflow Rs 822.4-824.4 Cr vs revenue Rs 841.4 Cr)"
    claimed: "Q2 FY27 revenue Rs 841.4 Cr"
    source_truth: "Q2 FY27 consolidated revenue from operations 84,131.88 lakh = Rs 841.32 Cr (results Q2 FY27 p.7; screener quarter 841.32). Rounds to Rs 841.3 Cr, the figure 04 uses elsewhere."
    note: "Rounding imprecision in one sentence. Book-to-bill 0.98 is unaffected. Counted as not clean for acceptance."
    source_fidelity: false
    tier: sample
critical_count: 0
major_count: 1
minor_count: 3
false_positives_struck: 2
material_universe: 264
acceptance_rate: 98.4
coverage_note: "SHADOW RUN (operator ruling 2026-10-11): findings bind nothing. MANDATORY TIER: 146 of 146 checked. The 146 cells are the Gate 0 scorecard input cells in 01-gate0.md: screener Data_Sheet rows FY17-FY26 (PBT, interest, CE components, ROE, sales, net profit, CFO, receivables, EBITDA inputs, FY26 scalars); AR scalars (capex, trade payables, current assets and liabilities, total assets, borrowings, R&D, contingent liabilities, customer shares, promoter table, Europe GmbH and USA Inc values); Q2 FY27 results scalars (H1 revenue, Sep-26 and Mar-26 receivables, other current liabilities, H1 CFO, other payables line, H1 capex, H1 PAT, cash, bank, current assets and liabilities, net worth, nil borrowings); Reg 31 30 Sep 2026 promoter and total shares. No verdict-card or Section 1B pillar input exists in this run (stages 11 and 13 not run). SAMPLE TIER: 118 material figures enumerated in 02, 04, 08 and 09 and the 05 sections read; 97 checked; 21 not checked: 41,342.32, 460.34, 824.87, top-10 84 percent, S commission 410.00, 14,813.73 Mn and 8,413.19 Mn, 4,008.73 and 7,855.88, 08 Trilegal, Trident and allotment figures, 96.16 percent AGM vote, diesel, induction and traction chart values, and web-only items. Not read in full: 03-ardeep, 06-peers, 07-emoat; their numbers are outside material_universe, so the universe is understated for those stages. material_universe = 146 mandatory plus 118 sample. acceptance_rate = clean checked numbers / checked: mandatory 145/146 (F1 counted as not clean), sample 94/97, overall 239/243 = 98.4. WEB-SOURCED FIGURES (08, 09): no PDF in corpus, not checked against PDFs, none in mandatory tier, logged NOT CHECKED. Covered: AR chart values in 09 (present in AR text), CRISIL figures in 09, and promoter figures also in Reg 31 filings. Not covered: USD/INR 95.25 (web), alternator, peer and market-share figures. REWORK trigger: none (no CONFIRMED CRITICAL). Source-fidelity rows: one (F2, MAJOR, sample, material UNANCHORED)."
```
