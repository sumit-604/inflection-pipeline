# Verifier A (numerical accuracy), Phase 1: PVRINOX, run 2026-11-12

Model: claude-sonnet-5-5. Fresh context. Inputs: stage reports 01 to 09 and the source documents in the run's inputs folder. All source-fidelity findings below are marked source_fidelity: true and stand until the source PDF itself disproves them.

## Findings

| # | Severity | Report location | Claimed value and anchor | Source truth and location | Note |
|---|---|---|---|---|---|
| 1 | MAJOR (source_fidelity) | 01-gate0.md Block B, B2 FY24 line; B3 cumulative FCF; lease-adjusted line | FY24 capex 627.9 Cr; FY24 FCF 1,351.1 Cr; cumulative FCF 4,889.5 Cr; FY24 lease repayment 1,054.7 Cr. Anchor "screener-data; AR25 p.CF" (no page) | Consolidated FY24 capex is 6,344 mn = 634.4 Cr (AR25 consolidated cash flow, FY24 column, text line 19111). FY24 FCF = 1,979.0 - 634.4 = 1,344.6 Cr. Cumulative FCF = 4,883.0 Cr. Consolidated FY24 lease repayment 10,589 mn = 1,058.9 Cr (line 19125). | The figures used (6,279 mn and 10,547 mn) are the STANDALONE AR25 lines (text lines 14526 and 14542). FY24 CFO 1,979.0 Cr is consolidated (AR25 line 19107: 19,790 mn). Unlabelled standalone vs consolidated mix. B2 stays 5 and B3 stays 5 (4,883.0 / 22.5 = 217x). No score moves. |
| 2 | MAJOR (source_fidelity) | 01-gate0.md Block B, B4; Block F M12 | FY24 payables 6,511 mn (AR25) giving -20.6 days; FY26 5,948 mn (AR26 p.239) giving -14.0 days; change +6.6 days. No basis label | AR25 FY24 trade payables 6,511 mn (42 + 6,469) are as filed and include supplier finance. AR26 FY26 payables 5,948 mn exclude 1,251 mn supplier finance moved to other financial liabilities (AR26 Note 2A(ii) p.258, Note 22 p.274). | Unlabelled basis difference (rule 5a, reported as UNANCHORED). Every number is copied correctly from its own page. The missing label matters because B4 scores on the FY24-to-FY26 change. |
| 3 | MAJOR (source_fidelity) | 02-notes.md Section A, Top 15 rank 1, "Why it matters" | "a number larger than 5x tangible equity of 15,260 (derived)" | 57,367 / 15,260 = 3.76x (inputs match AR26 p.239). | Derived multiple overstated. YAML top_findings rank 1 does not repeat it. |
| 4 | MINOR (source_fidelity) | 01-gate0.md Block A, FY17 Avg NW | 964.99 | 46.74 + 918.27 = 965.01 (screener Data Sheet) | 0.02 Cr slip. ROE 9.9% unchanged. |
| 5 | MINOR (source_fidelity) | 09-tam.md 1A and Section 2 | Four-stream revenue 63,208 Mn (6,321 Cr); net ticket sales 35,291 Mn, both from rounded mix percentages | AR26 Note 24 p.275: 35,301 + 20,884 + 4,636 + 2,410 = 63,231 Mn (6,323.1 Cr); tickets 35,301 Mn | 0.04% off. No SAM or SOM conclusion moves. |

No CRITICAL findings. No verdict-card or Section 1B pillar input exists in Phase 1, so rule 5 CRITICAL cannot fire on this scope.

## Rows struck by the rule 5b self-check (3)

1. Gate 0 net cash 132.4 Cr (balance-sheet derived, leases excluded) vs company 140.7 Cr. Both are correct on their stated basis; the report names the 8.3 Cr gap. Class: correctly labelled basis difference. The Q2 FY27 consolidated balance sheet at PDF page 12 reads cash 5,833, bank 500, borrowings 3,164 + 1,845. The presentation cash line 6,416 includes investments and deposits.
2. B05 conflict log: transcript says industry box office Rs 4,433 Cr, presentation and press release say 4,443 Cr. The call transcript (Q2 FY27, text line 107) does print 4,433, and the report copies it correctly and flags it. Class: faithfully transcribed anomaly.
3. B03 and B05 screen counts (1,798 / 1,789 / 1,782) and Hindi growth (55% vs 18%). Each is printed as stated in the AR (pp.26, 89, 94, 23, 83). Class: faithfully transcribed anomaly.

## What matched (principal items)

- Gate 0 Block A: all ten years of EBIT, capital employed, ROCE, average net worth and ROE recompute from the screener Data Sheet. Medians 6.3% and 0.7% hold.
- Gate 0 Blocks B to D: cumulative CFO 9,107.4 and PAT -1,111.0; FY25 and FY26 capex 330.7 and 258.7 (AR26 p.241); FY26 WC days -14.0; revenue and PAT CAGRs 13.5%, 14.9%, 7.0%; D1 to D4 ratios; EBITDA 2,095.2 and LTM 2,374.3.
- Gate 0 Block E: promoter 27.02%, 27.84% (Sep 2023), pledge 2,944,444 shares = 11.10% of promoter holding, 3.0% of total, FII 19.12%, DII 33.56% (NSE XBRL); contingents 2,555 mn (AR26 p.292, sum of lines a to o checked; FY25 2,458).
- Gate 0 Block F: M1, M3, M8, M11, M12 inputs and CAGRs recompute.
- Load-bearing facts: net cash 1,407 mn after 3,000 mn buyback, 24 opened and 25 exited, 1,797 screens, patrons 46.3 mn, ATP 298, SPH 153, occupancy 30.4% (press release p.2 to p.4); Mar-26 net debt 1,619 (AR26 p.239, p.29, p.92); PAT 3,868, 2,306, 3,328, 1,761, 1,952 (AR26 pp.26, 240).
- B03 and B02: balance sheet, P&L, cash flow lines and derived ratios (EBITDA 22,789 and 17,282, ROCE 7.1%, ROE 4.6% and 2.4%, DuPont, leverage ratios, organic free cash 5,707 and 3,511, lease cash 11,847, goodwill 77.7%), Note 4A WACC 10.33% (12.08%), Note 18 lease maturity 12,904 and 83,015, DTA 3,252 and 19,446, Note 37, Note 46, standalone MD&A table, shareholding.
- B04: revenue mix (sum 66,462), unit economics per admission (all 16 lines recompute from AR26 pp.94-95), investor presentation figures (pp.8, 11, 15, 16, 20, 21, 24, 26, 28 to 31).
- B05, B06: guidance and delivery numbers against the four company transcripts and the eight peer transcripts (Feb "96 / 150-odd / 350-400"; Nov "141 crores, 4,433, 35-40 crores, 300-320, 132 crores"; UFO +33%, 1,299 vs 1,113, 3,946 screens, 386 vs 462 releases; Wonderla Rs 983, 1,491, 1,310, 591), per-title share arithmetic.
- B07, B08, B09: AR p.66 solar figures, p.171 and p.173 standalone lines, SAST and XBRL share counts and pledge releases (184,300 and 637,800), buyback tender 502,200 and 569,584, AR chart values p.83, TAM, SAM and SOM arithmetic.

## Coverage statement

Mandatory tier: no verdict-card or Section 1B pillar inputs exist in Phase 1. The tier was set to the Gate 0 scorecard inputs in 01-gate0.md and its four load-bearing facts. Count: 125 (Block A 24, Block B 12, Block C 10, Block D 20, Block E 7, Block F 19, load-bearing facts and latest-quarter check 33). Checked 125 of 125. No mandatory figure was left unchecked.

Sample tier: a number is material if it feeds a table, score, ratio or flag in B02 to B09. I count about 575 such numbers beyond the mandatory tier (an estimate built by section), so the material universe is about 700. I checked about 260 of the sample tier, in order of materiality: scorecard and table inputs first, then derived ratios, then table cells. Total numbers checked: 385.

Not checked: B02 note cells beyond those named; B03 governance attendance and compensation tables; B05 YAML tail and trend cells; B06 Part 3 map; B07 sections after G1; B08 and B09 web-sourced figures (no source PDF held), named in the block.

Document readability: the three results PDFs are scanned images. The Q2 FY27 consolidated balance sheet was read at PDF page 12. Other results figures were cross-checked against the clean-text investor presentation. No document was unreadable by both routes.

```yaml
stage: B12a
company: "PVRINOX"
run_date: "2026-11-12"
model: claude-sonnet-5-5
status: complete
numbers_checked: 385
mandatory_checked: 125
mandatory_total: 125
findings:
  - {severity: "MAJOR", location: "01-gate0.md Block B, B2 (FY24 FCF line) and B3 cumulative FCF; Block B lease-adjusted line", claimed: "FY24 capex 627.9 Cr; FY24 FCF 1,351.1 Cr; cumulative FCF FY24-FY26 4,889.5 Cr; FY24 lease repayment 1,054.7 Cr; anchor 'screener-data; AR25 p.CF' (no page)", source_truth: "Consolidated FY24 capex 6,344 mn = 634.4 Cr (AR25 consolidated cash flow, Purchase of PPE... line, FY24 column); FY24 FCF = 1,979.0 - 634.4 = 1,344.6 Cr; cumulative FCF 4,883.0 Cr; consolidated FY24 lease repayment 10,589 mn = 1,058.9 Cr. The figures used (6,279 mn capex, 10,547 mn lease) are the STANDALONE AR25 cash flow lines, while the FY24 CFO 1,979.0 Cr (screener) is consolidated (AR25 consolidated CFO 19,790 mn).", note: "Unlabelled standalone vs consolidated mix in a Gate 0 scorecard input. B2 stays 5 (3 of 3 years positive) and B3 stays literal 5 (4,883.0 / 22.5 = 217x), so no score moves. FY25 (330.7 Cr) and FY26 (258.7 Cr) capex are consolidated and match AR26 p.241.", source_fidelity: true}
  - {severity: "MAJOR", location: "01-gate0.md Block B, B4 (WC days FY24 vs FY26) and Block F M12", claimed: "FY24 payables 6,511 mn (AR25) giving -20.6 days; FY26 payables 594.8 Cr (AR26 p.239) giving -14.0 days; change +6.6 days; FY25 -18.1 on 6,062 mn (AR26 comparative); no basis label", source_truth: "AR25 FY24 trade payables 6,511 mn (42 + 6,469, consolidated) are as originally filed and include supplier-finance balances. AR26 FY26 payables 5,948 mn exclude supplier finance of 1,251 mn, which AR26 moved to other financial liabilities (AR26 Note 2A(ii) p.258; Note 22 p.274; FY25 comparative moved 1,635 mn). The FY24 and FY26 payables are on different classification bases and the report does not say so.", note: "Unlabelled basis difference (rule 5a), material because B4 scores on the FY24-to-FY26 change (+6.6 days -> 1 point) and M12 rests on the same days. Every figure is copied correctly from its own page; the finding is the missing basis label. B02 itself notes the reclassification lowers reported payable days.", source_fidelity: true}
  - {severity: "MAJOR", location: "02-notes.md Section A, Top 15, rank 1, 'Why it matters' cell", claimed: "'a number larger than 5x tangible equity of 15,260 (derived)' (goodwill 57,367)", source_truth: "57,367 / 15,260 = 3.76x. 5 x 15,260 = 76,300, above goodwill. Tangible equity 15,260 = 73,787 - 57,367 - 1,160 is correct (AR26 p.239).", note: "Derived multiple overstated by about 1.2x in the rank-1 finding. The inputs (57,367, 73,787, 15,260) all match p.239. YAML top_findings rank 1 does not repeat the 5x claim.", source_fidelity: true}
  - {severity: "MINOR", location: "01-gate0.md Block A table, FY17 row, Avg NW column", claimed: "closing only 964.99", source_truth: "46.74 + 918.27 = 965.01 (screener Data Sheet, FY17 equity capital + reserves)", note: "0.02 Cr arithmetic slip. FY17 ROE 9.9% and FY18 average 1,020.2 are unchanged.", source_fidelity: true}
  - {severity: "MINOR", location: "09-tam.md Section 1A and Section 2 cross-check", claimed: "four-stream revenue Rs 63,208 Mn = Rs 6,321 Cr (95.1% x 66,462); net ticket sales Rs 35,291 Mn (53.1% x 66,462)", source_truth: "AR26 Note 24 p.275: tickets 35,301 + F&B 20,884 + advertising 4,636 + convenience fees 2,410 = 63,231 Mn = 6,323.1 Cr. Tickets 35,301 Mn.", note: "Rebuilt from rounded mix percentages instead of the printed Note 24 lines (0.04% off). No SAM or SOM conclusion moves.", source_fidelity: true}
critical_count: 0
major_count: 3
minor_count: 2
false_positives_struck: 3
material_universe: 700
acceptance_rate: 97
coverage_note: "MANDATORY TIER: no verdict card or Section 1B pillar inputs exist in phase 1, so the mandatory tier was set to the Gate 0 scorecard inputs in 01-gate0.md plus its four load-bearing facts. Counted 125 (Block A ROCE and ROE 20 plus A1-A4 4; Block B 12; Block C 10; Block D 20; Block E 7; Block F 19; load-bearing facts and latest-quarter check about 33) and checked 125 of 125. Screener Data Sheet recomputed for all 10 years; AR26 pp.26, 29, 239-241, 292; AR25 consolidated and standalone cash flow and payables; shareholding XBRL; Q2 FY27 consolidated balance sheet read at PDF page 12 (image); press release 28 Oct; investor presentation. Net-cash 132.4 vs 140.7 Cr gap is a correctly labelled basis difference (struck). SAMPLE TIER: material = a number that feeds a table, score, ratio or flag in B02-B09 (counted by section, about 575 beyond the mandatory tier; total universe about 700 is an estimate). Checked about 260 sample numbers: B04 (mix, unit economics, net cash bridge, screen mix; nearly all), B03 (statements, ratios, net debt, shareholding, related flows; about 70), B02 (about 25), B05 (guidance and delivery numbers against Feb, May, Jul, Nov transcripts and presentation; about 35), B06 (about 15 peer figures), B07 (about 10), B08 (pledge and tender share counts, SAST and XBRL; about 20), B09 (AR chart values, SAM and SOM arithmetic; about 35). NOT CHECKED: B02 notes 3-50 small-note cells beyond the ones named; B03 governance attendance and compensation tables (CG pp.99-121); B05 YAML tail and 1C trend cells; B06 Part 3 map; B07 sections 3-6 after G1; B08 web-sourced items (BSE close 1,157.40, ballot percentages, Warburg, CCI and SEBI media items; no source PDF held); B09 web-sourced items (832 Mn admissions, PMAR 877 Cr, Cinepolis and Miraj screen counts). Results PDFs are scanned: Q2 FY27 consolidated figures were confirmed at the PDF image (balance sheet) and against the clean-text presentation (P&L). Peer and FY25 comparative checks used the .txt layers; no document was unreadable by both routes."
```
