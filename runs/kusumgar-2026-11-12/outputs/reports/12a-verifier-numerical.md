# VERIFIER A: NUMERICAL ACCURACY. KUSUMGAR, run 2026-11-12 (Phase 1)

Model: claude-sonnet-5-5. Fresh context. Inputs read: the 11 stage reports and the source .txt twins. Anchor convention check: every report uses "p.N" = the [page N] marker of the .txt twin (printed page + 4 for the prospectus). I tested this on 40+ anchors and it holds.

## Result in one paragraph

0 CRITICAL, 1 MAJOR, 4 MINOR. Every Gate 0 input and every Section 1B pillar or verdict-card input I could trace matches its source. The one MAJOR is a wrong CRISIL rating on 2026-01-21 in the promoter report (report 08). The four MINOR rows are three wrong-page anchors and one period label. Each anchor finding carries `source_fidelity: true` and stands until the PDF page clears it.

## Findings table

| # | Severity | Report location | Claimed (value + anchor) | Source truth (location) | Note | source_fidelity |
|---|---|---|---|---|---|---|
| 1 | MAJOR (MISMATCH) | 08-promoter.md, Section 4C CRISIL bullet; ERRATA bullet 2 | CRISIL history "then BB- on 2026-01-21 and BB- Stable / A4+ on 2026-10-22" (CRISIL rationale p.1-2) | On 21-01-26 the rating was Crisil B/Stable (Issuer Not Cooperating) long term and Crisil A4 (INC) short term. BB-/Stable and A4+ are the 2026-10-22 revision ("Ratings revised to", p.1; history table p.2: 21-01-26 B/Stable, 28-11-24 B/Stable, 20-09-23 B/Stable) | The B08 YAML block says "history B back to 2023", which is right. The body text and the ERRATA say BB- on 2026-01-21, which is wrong. Not a pillar input, so MAJOR not CRITICAL. | true |
| 2 | MINOR (ANCHOR NOT FOUND) | 08-promoter.md, 3D "Rating disclosure" bullet; YAML adverse_findings item 3 | CRISIL non-cooperation dated 2026-01-21 sits at "CARE release 2026-04-02 p.4" | The sentence is on CARE release p.3 ("Status of non-cooperation with previous CRA", lines 161-163). p.4 holds Annexures 1-2 only | The date 2026-01-21 is correct. Only the page is wrong. B03 anchors it correctly at p.3. | true |
| 3 | MINOR (ANCHOR NOT FOUND) | 04-bizmodel.md, 1B A&D Fabrics row; 1D "WC intensity" and "Regulatory" rows; 4A "Structural" row | "government payment follows inspection and acceptance" and "normal cycle 100 to 120 days" at "Q2 Pres p.23" | Both statements are Investor Q&A 17, on Q2 presentation p.24. p.23 holds Q&A 6-12 | Figure 100-120 days is right. Page is off by one. B05 anchors it at p.24. | true |
| 4 | MINOR (ANCHOR NOT FOUND) | 04-bizmodel.md, anchor line under 1B | "66.21% of the segment tied to exports" at "p.194 (66.21%)" | The text is on Prospectus p.198 (1,091.61 of 1,648.60 = 66.21%). p.194 does not hold it | The same anchor line also lists p.198 in general. B05 and B07 cite p.198. | true |
| 5 | MINOR (period label, not an absent number) | 07-emoat.md, 1B Geography row | "Sri Lanka 102.79 to 349.63" in a row timed FY24-FY26 | Sri Lanka is nil ("-") in FY24, 102.79 in FY25, 349.63 in FY26 (Prospectus p.209) | Both numbers exist at p.209. The first one belongs to FY25, not FY24. Germany 276.60 to 757.24 is a true FY24 to FY26 pair. | false |

## Self-check (rule 5b) and rows struck

I drafted ten candidate rows, struck five and kept five before emitting. Struck rows, so the operator can see what was tested:

1. Gate 0 D2 interest cover "6.19x": 1,609.36 / 259.78 = 6.195, so 6.20 by rounding. Same value, different display rounding (rule 5a, matched figure). Score band is unchanged.
2. Gate 0 D1 net debt "1,755.21": Prospectus p.191 prints 1,755.22 and the MD&A reconciliation p.346 prints 1,755.21. The report copies p.346 and the computed sum 2,235.82 - 480.61. Faithful (rule 5a).
3. B03 "peer average 33.76x, range 36.12-44.53x": the prospectus prints Highest 44.53, Lowest 36.12, Average 33.76 (Basis for Offer Price P/E table, prospectus text lines 8627-8634). The true peer P/Es are 36.12 / 33.76 / 44.53. The report copies the printed anomaly. Faithfully transcribed anomaly (rule 5a).
4. B03 "42.32% on 127.80 metres (FY25)": the table prints 42.32% against 46.45 produced; 46.45 / 127.80 would be 36.3%. The report copies the printed row (p.204). Faithfully transcribed anomaly (rule 5a).
5. B03 and B08 "CARE gearing 1.17x as of March 31, 2026": CARE text says "as on March 31, 2026" while its own table shows 1.17x for FY25. The report copies the sentence. Faithful (rule 5a).

The five kept rows were re-read against rule 5. In each, `claimed` and `source_truth` are different values. None falls into the three non-findings classes. Severity follows rule 5: no pillar or card input is wrong, so nothing is CRITICAL.

## Coverage statement

Counting rule. One "figure" = one distinct reported value tied to a source anchor. A number repeated in the same report counts once. Scores that are pure arithmetic on checked figures (block totals, sums) count as one figure each. All counts below are my own enumeration and carry roughly +/-10% counting error. They are not a bare percentage.

### Mandatory tier (OR-32)

- Mandatory total: 315 figures. Mandatory checked: 315. Counts match. No mandatory figure was left unchecked.
- Composition: 236 Gate 0 scorecard inputs (all of 01-gate0.md: four load-bearing fact rows 69; Block A 34; Block B 54; Block C 6; Block D 21; Block E 19; Block F 22; classification box and block scores 8; company working-capital-cycle notes 3). Plus 79 Section 1B pillar and verdict-card inputs from other stages: Pillar 1 ROCE trail (shared with Gate 0); Pillar 2 cash-conversion set (CFO/EBITDA 15.0% and 14.6%, CFO/PAT 28.8%, CFO after interest 40.27, 320.36 release, H1 FY27 CFO 248.85 vs 393.77, 16.8%, 29.9%, 17.5%, receivables 2,203.67 and 80.7 days, tax 372.02, inventories 739.83) about 17; Pillar 3 growth-visibility set (2,371.96 order, 23.61%, 76.39%, about 1,812, H1 revenue 4,981.90 and +90.7%, H1 PBT 1,106.69 vs 222.98, H1 PAT 832.45 vs 175.65, Q1 and Q2 revenue, FY25 order values 2,225.88 and 2,045.75, 286.16, 639.57) about 16; sector-cap evidence (A&D shares 68.98 / 76.87 / 54.64, segment sums, non-A&D 30.84 / 22.02 / 43.00, government-owned 3.34 / 34.65 / 15.09) about 15; Emerging Moat inputs (em_score 17.5 sum, capex_embedded_growth_pct 5.0 with CWIP 101.04, 3.40, 343.5) 5; promoter-pillar set (89.43%, 75.01%, pledge nil, 6,500, 2,292.00, 1,118.53, 10,290.53, postal-ballot 87.19%) about 12; credibility inputs (31.1% to 28.4%) 3; TAM/SAM/SOM card (94,100; 99,229; 63,445; 984; 1,273; 13.4%; 13.5%; 0.64%) 8; market data (price 549.45, market cap 5,772.39, P/E 45.1) 3.
- Result of the mandatory check: 0 mismatches. Gate 0 arithmetic was re-derived from the prospectus statements (ROCE, ROE, CFO/PAT, FCF, working-capital days, net debt, interest cover, current ratio, contingent liabilities, CAGRs, screener-derived margins). All reproduce.

### Sample tier

- Material numbers in the reports outside the mandatory set: about 1,100. Rule for "material": a figure that carries a source anchor and feeds a flag, score, table cell or monitorable. I excluded dates, page references, item counts and restatements of an already counted figure.
- Checked: 400. Focus by order of materiality: B03 notes, cash-flow and balance-sheet cells (about 110); B02 pass 1-3 (about 30 spot checks, including the 78.90, 32.04 / 29.06, 2,292.00 and 81.48 chains); B04 (about 45, incl. peer KPI table and per-metre economics); B05 and the Q1 call page anchors (about 35); B06 peer quotes with page markers (about 20); B07 (about 45); B08 (about 45, incl. postal ballot, SPA table, CRISIL, CARE, BM outcome); B09 (about 50, incl. the TAM, SAM and SOM arithmetic); rating documents (about 20).
- Not checked in the sample tier: the remaining roughly 700 figures, mostly B02 pass 1 related-party and note-by-note tables, B03 phase 5 board and pay detail, B06 quotes beyond the 20 tested, and B09 Lattice sub-splits beyond the pools tested.

### Named gaps (coverage shortfalls, none mandatory)

1. The company letter of 2026-10-23, the Reg 74(5) certificate and the other `announcements/*.txt` files (apart from the postal-ballot results and the 2026-11-05 outcome) were not opened. B03 and B08 cite the letter ("Company letter 2026-10-23 p.1").
2. `Investor_Presentation_Q1FY27_2026-08-12.txt`, `screening/ARVIND`, `GARFIBRES`, `MAYURUNIQ` CSVs and `inputs/other/` (scanned PDF) were not used by any report I checked, or I did not need them. Not opened.
3. Web-sourced claims in B08 (press URLs, listing price 569 / 574, AmbitionBox 4.5) and B09 (indiasworld.in 75% carve-out, bharatshakti.in, tenders.infralens.in, search snippets) have no PDF in my inputs. They are outside Verifier A's scope and are unchecked.
4. B09 Section 6 and B08 "Items for Claude web" are candidates, not numbers.

## Notes for the orchestrator

- Finding 1 is the only one that changes a reading. The B08 reading (1) "CRISIL BB- reflects missing information only" leans on a B history back to 2023. That history is true in the source. The only wrong item is BB- as the 2026-01-21 level; the source shows B on that date and the step-up to BB- on 2026-10-22. No pillar input moves.
- Findings 2 to 4 are wrong-page anchors. The values are in the source on the adjacent page. They need a one-line anchor fix, not a re-analysis.
- The source anomalies the reports copied faithfully (peer P/E labels, FY25 utilisation 42.32% on 127.80 metres, customer 1 at 0.00% in Note 45(c) against 751.27 on p.28, WhiteOak SPA 120.00 for 82,192 shares at 365) are real in the prospectus. They are for Verifier C and the analyst stages to weigh, not for me.

```yaml
stage: B12a
company: "KUSUMGAR"
run_date: "2026-11-12"
model: claude-sonnet-5-5
status: complete
numbers_checked: 715
mandatory_checked: 315
mandatory_total: 315
findings:
  - {severity: "MAJOR", location: "08-promoter.md Section 4C CRISIL bullet and ERRATA bullet 2", claimed: "CRISIL rating 'BB- on 2026-01-21', then BB- Stable / A4+ on 2026-10-22 (CRISIL rationale p.1-2)", source_truth: "CRISIL rationale 2026-10-22 p.2 rating history: 21-01-26 = Crisil B/Stable (Issuer Not Cooperating) long term and Crisil A4 (INC) short term; BB-/Stable and A4+ are the 2026-10-22 revision (p.1); 28-11-24 B/Stable; 20-09-23 B/Stable", note: "MISMATCH. Body text and errata say BB- on 2026-01-21; source says B. The B08 YAML block ('history B back to 2023') is correct. Not a pillar or card input, so MAJOR.", source_fidelity: true}
  - {severity: "MINOR", location: "08-promoter.md 3D Rating disclosure bullet; YAML adverse_findings item 3", claimed: "CRISIL non-cooperation 2026-01-21 at 'CARE release 2026-04-02 p.4'", source_truth: "CARE release p.3 'Status of non-cooperation with previous CRA' (CRISIL press release dated January 21, 2026); p.4 holds Annexure-1 and Annexure-2 only", note: "ANCHOR NOT FOUND. Date is right, page is wrong. B03 anchors p.3.", source_fidelity: true}
  - {severity: "MINOR", location: "04-bizmodel.md 1B A&D Fabrics row; 1D WC intensity and Regulatory rows; 4A Structural row", claimed: "'payment follows inspection and acceptance' and 'normal cycle 100 to 120 days' at Q2 Pres p.23", source_truth: "Investor Q&A 17 on Q2 presentation p.24 (p.23 holds Q&A 6-12)", note: "ANCHOR NOT FOUND. Text and 100-120 days exist on the adjacent page. B05 anchors p.24.", source_fidelity: true}
  - {severity: "MINOR", location: "04-bizmodel.md anchor line under 1B", claimed: "66.21% of Industrial and Automotive revenue tied to exports at 'p.194 (66.21%)'", source_truth: "Prospectus p.198: 1,091.61 of 1,648.60 = 66.21%", note: "ANCHOR NOT FOUND at the explicit page. p.198 appears in the same anchor list. B05 and B07 cite p.198.", source_fidelity: true}
  - {severity: "MINOR", location: "07-emoat.md 1B Geography row", claimed: "Sri Lanka 102.79 to 349.63 in a row timed FY24-FY26", source_truth: "Prospectus p.209: Sri Lanka FY24 nil, FY25 102.79, FY26 349.63", note: "Period label imprecision. Both values exist at p.209; 102.79 is FY25, not FY24.", source_fidelity: false}
critical_count: 0
major_count: 1
minor_count: 4
false_positives_struck: 5
material_universe: 1415
acceptance_rate: 99
coverage_note: "Mandatory tier 315 of 315 checked (236 Gate 0 inputs plus 79 Section 1B pillar and verdict-card inputs; my own enumeration, about +/-10% counting error; zero unchecked). Sample tier: about 1,100 material figures counted, 400 checked, about 700 not checked (mostly B02 pass 1 related-party tables, B03 board and pay detail, B06 quotes beyond the 20 tested, B09 Lattice sub-splits). numbers_checked 715 = 315 + 400. material_universe 1415 = 315 + 1,100. Not opened: company letter 2026-10-23, Reg 74(5) certificate and other announcements files except postal-ballot results and the 2026-11-05 outcome; Q1 FY27 deck; ARVIND, GARFIBRES, MAYURUNIQ CSVs; inputs/other scanned PDF. Web-sourced claims in B08 and B09 have no PDF in my inputs and were not checked. Five candidate rows struck under rule 5a (6.19x rounding; net debt 1,755.21 vs 1,755.22; printed peer P/E labels; FY25 utilisation 42.32% as printed; CARE gearing sentence as printed)."
```
