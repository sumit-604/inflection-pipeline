# VERIFIER A: NUMERICAL AUDIT, KWICK, run 2026-10-04

Model claude-sonnet-5-5. Sources read: KWICK-Prospectus-2026-08-31.txt (Rs lakh), Investor_Presentation_1.txt, announcements (6 BSE filings plus SEBI order of 18-Aug-2026), screener-Data_Sheet.csv (Rs Cr), 11 peer transcripts. Page anchors follow the "[page N]" markers in the txt twins.

## Result

No CRITICAL finding. No verdict-card or Section 1B pillar input differs from the source. The Gate 0 series (sales, PBT, interest, net worth, CFO, receivables, inventory, cash, total assets) tie to the screener CSV and to the restated prospectus statements. ROCE series (50.9 / 7.1 / 30.5 / 39.2 / 38.2 / 45.0%) recomputes from screener. CFO / PAT (-0.92x / 0.54x / 0.56x), the working-capital walk, the ageing table (Note I.14), the related-party stack (384.19), the FY27 working-capital plan (4,442.00 / 3,142.00), the segment table, the customer and state concentration tables, the 2,035.74 / 95-vehicle channel disclosure (p.150) and the peer transcript figures I tested all match.

## Findings

| # | Sev | Location | Claimed (anchor) | Source truth (location) | Note |
|---|---|---|---|---|---|
| 1 | MAJOR | 09-tam Method 2, 3B, 4 | 2,035.74 lakh / 95; CSI 16.41 to 10.57 Cr; 115% growth, all "prospectus p.265" | 2,035.74 is on p.150 (L9407); CSI 405.09 / 1,640.66 / 1,056.76 on p.24 and p.150; 115% on p.264 (L16416). p.265 holds none of the three | ANCHOR NOT FOUND for a load-bearing SOM input. Values are correct. Stages 03/04/05 anchor correctly. source_fidelity true |
| 2 | MINOR | 01-gate0 LBF-2 | "The prospectus does not say the basis is average receivables" | p.245 L15281 prints "Average Receivables days = 365 / (Net Revenue / Average Trade receivables)" | Negative claim contradicted by the source. All numbers in the bullet are right. source_fidelity true |
| 3 | MINOR | 08-promoter 3D | deck p.19 prints PBT 1,921.45 | deck [page 20] (L510) | Value right, page off by one. source_fidelity true |
| 4 | MINOR | 08-promoter 3D; 05-concall LBF-4 | "deck states No UPSI was shared"; "deck names Wednesday for 30-Sep" | Deck has neither. UPSI line is in announcement 20260930-b0992b12 L31; "Wednesday, 30th" in announcement 20260924-9a7d0634 L28 | Wrong document attributed, no number. source_fidelity true |
| 5 | MINOR | 02-notes (B table), 02-notes-pass1 | gross receivables FY26 2,320.02; Mobile CSI FY24 405.08 | Note I.14 prints 2,320.01 (L14653); segment table prints 405.09 (L1429) | 0.01 lakh. Buckets sum to 2,320.02 but the printed total is 2,320.01. Stage 03 is right. source_fidelity true |
| 6 | MINOR | 06-peers Q1/Q7/Q8 | ADSL 10% threshold [page 24]; DSSL PPE/net debt 68 Cr [page 4]; ADSL "Rs 36 Cr ECL" at Q3 [page 16] | threshold on [page 23] (Feb ADSL L940 < marker L966); 68 Cr on [page 5] (Jun DSSL L57 > marker L54); Rs 36-odd crore ECL is Q4 FY26 (May ADSL) [page 13] L503 | Values exist; anchors off by a page or by a quarter. No verdict moves. source_fidelity true |
| 7 | MINOR | 08-promoter 3A item 2 | 90.18 of 7,998.16 "purchases" = 1.13% | 7,998.16 is P&L "Cost of Materials Consumed" (MD&A calls it Purchase of Goods); Note II.3 Purchases = 7,446.06 | Unlabelled basis versus stage 03 (0.90% on 7,446.06, goods only). Immaterial. source_fidelity false |

## Rows struck by the rule 5b self-check (3)

- Stage 04 "deck slide N" against deck page numbering: cosmetic label, values match (5a, matched figure).
- Gate 0 and pass 1 cash-tax figures (470.02 less 281.74 = 188.28; 279.80 less 97.90 = 181.90): the numbers are right. The "flatters CFO" inference was withdrawn in pass 2. Judgement, not fidelity.
- "33 or 34 payroll staff" in stages 03/08: the source prints 34 in the text (L9693) and 33 in the table total (L9706, L9739). Faithfully transcribed anomaly (5a).

## Coverage

Material universe: 410 numbers. Rule: a number counts as material if it is a stage headline or YAML field, a Gate 0 or scorecard input, a restated-statement figure behind a flag, a concentration, working-capital, related-party, ownership or litigation figure that a later stage consumes, or a peer figure cited as evidence for a verdict. Pure restatements of the same figure across stages count once per report.

Checked: 236 (58%). Clean: 227. Defective: 9 distinct numbers or anchors (7 findings). Order of work: Gate 0 scorecard inputs and series first (screener recomputed), then headline figures in 03/04/05, then table cells in 02/06/07/08/09.

Not verified: web-sourced items in 08 and 09 (shareholding pattern from search summaries, Varanasi press, Deloitte-DSCI/IBEF/devdiscourse/PIB/MHA secondary figures), and market-size claims the makers already tagged PENDING LIVE VERIFICATION. Units: prospectus read in Rs lakh, screener in Rs Cr; every conversion I checked (100 lakh = 1 Cr) is correct. Basis traps checked: standalone only, Indian GAAP, FY25 and FY26 not restated, CFO is before interest (interest paid in financing), basic and diluted EPS equal; debtor-day basis (average vs year-end) is labelled in stages 03, 04, 05.

```yaml
stage: B12a
company: "KWICK"
run_date: "2026-10-04"
model: claude-sonnet-5-5
status: complete
numbers_checked: 236
findings:
  - {severity: "MAJOR", location: "09-tam.md Section 2 Method 2 (kit value per vehicle) and 3B/4 citations 'prospectus p.265'", claimed: "Rs 2,035.74 lakh / 95 vehicles = Rs 21.43 lakh, cited 'prospectus p.265'; Mobile CSI Rs 16.41 Cr FY25 to Rs 10.57 Cr FY26 cited 'prospectus p.265'; revenue growth 115% FY25 cited p.265", source_truth: "PDF page 265 (MD&A) does not contain 2,035.74, 1,640.66 or 1,056.76. 2,035.74 (95 vehicles) is on p.150; Mobile CSI 405.09/1,640.66/1,056.76 on p.24 and p.150. The 115% growth is on p.264 (MD&A table). The figures themselves are correct; only the cited anchor fails", note: "ANCHOR NOT FOUND at the cited page for a load-bearing SOM input. Stages 03, 04, 05 anchor the same 2,035.74 correctly to p.150. Needs re-anchor to p.150 / p.24 / p.264", source_fidelity: true}
  - {severity: "MINOR", location: "01-gate0.md LBF-2 bullet 3", claimed: "Prospectus does not state that debtor days use average receivables", source_truth: "p.245 (L15281) prints 'Average Receivables days = 365 / (Net Revenue / Average Trade receivables)'", note: "Negative claim contradicted by p.245; numbers in the bullet correct", source_fidelity: true}
  - {severity: "MINOR", location: "08-promoter.md 3D item 1", claimed: "deck p.19 prints PBT 1,921.45", source_truth: "deck [page 20]", note: "Value right, page off by one", source_fidelity: true}
  - {severity: "MINOR", location: "08-promoter.md 3D; 05-concall.md LBF-4", claimed: "deck states 'No UPSI was shared'; deck names Wednesday for 30-Sep", source_truth: "Neither is in the deck. UPSI line: announcement 20260930-b0992b12 L31. Wednesday: announcement 20260924-9a7d0634 L28", note: "Wrong document attributed; no number", source_fidelity: true}
  - {severity: "MINOR", location: "02-notes.md Section B; 02-notes-pass1.md ageing table and revenue details", claimed: "gross receivables FY26 2,320.02; Mobile CSI FY24 405.08", source_truth: "Note I.14 prints 2,320.01 (L14653); segment table 405.09 (L1429)", note: "0.01 lakh; stage 03 correct", source_fidelity: true}
  - {severity: "MINOR", location: "06-peers.md Q1/Q7/Q8 page anchors", claimed: "ADSL 10% threshold [page 24]; DSSL PPE and net debt 68 Cr [page 4]; ADSL Rs 36 Cr ECL at Q3 [page 16]", source_truth: "threshold [page 23]; 68 Cr [page 5]; Rs 36-odd crore ECL in Q4 FY26 (May-2026) [page 13]", note: "Values exist, anchors off by a page or quarter; no verdict moves", source_fidelity: true}
  - {severity: "MINOR", location: "08-promoter.md 3A item 2", claimed: "90.18 of 7,998.16 'purchases' = 1.13%", source_truth: "7,998.16 is Cost of Materials Consumed; Note II.3 Purchases = 7,446.06", note: "Unlabelled basis versus stage 03; immaterial", source_fidelity: false}
critical_count: 0
major_count: 1
minor_count: 6
false_positives_struck: 3
material_universe: 410
acceptance_rate: 96
coverage_note: "Material universe 410 load-bearing figures across nine reports (headline and YAML fields, Gate 0 inputs, restated-statement figures, concentration, working-capital, related-party, ownership, litigation, peer anchors, TAM inputs). 236 checked (58%), 227 clean, 9 distinct number or anchor defects in 7 findings. Web-sourced items in 08 and 09 and items tagged PENDING LIVE VERIFICATION were not verified. No CRITICAL: no verdict-card or Section 1B pillar input differs from source."
```
