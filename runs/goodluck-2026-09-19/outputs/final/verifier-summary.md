# GOODLUCK verifier summary (phase 1)

## Confidence delta (phase 1)

| Component | Score | Source |
|---|---|---|
| numerical_acceptance | 95.4 | B12a |
| redflag_coverage | 80 (strict caught only: 46.7) | B12b |
| framework_adherence | 87.0 | B12c (Gate 0 + Emerging Moat portion) |
| peer_utilisation | 77.8 | B06/B12d |
| overall | 77.8 | min of four; band 75-89 normal |

Pending phase 3: the framework adherence valuation half (B10/B11).

## Acceptance rates

| Verifier | Model | Scope | Acceptance | CRITICAL | MAJOR | MINOR |
|---|---|---|---|---|---|---|
| A (numerical) | claude-haiku-4-5 | 65 material figures, B02-B09 | 95.4 | 0 | 0 | 0 |
| B (red flags) | claude-opus-5 | 4 Goodluck transcripts, 8 peer transcripts, 1 peer presentation | 80 (orchestrator ruling; strict 46.7) | 1 | 6 | 15 |
| C (framework, phase 1) | claude-opus-5 | Gate 0 (36 rules) + Emerging Moat (18 rules) | 87.0 | 0 | 3 | 4 |
| D (peers) | claude-sonnet-5 | 9 peer documents | 89 | 0 | 1 | 2 |

Orchestrator ruling on red flag coverage: 80 counts partial catches as caught (rubric rule 3, VOEPL precedent). The strict caught only rate of 7 of 15 = 46.7% is disclosed in confidence.yaml.

Verifier A identity check: 0 CRITICAL rows, nothing to strike. Verifier A reinvocation: the first pass (56 numbers, 100%) was weighted to stage 1 and listed an ANCHOR NOT FOUND row outside findings[]. It was reinvoked once with the coverage addendum, and the second pass governs.

Verifier disagreements with Verifier A source fidelity findings: none.

## Findings, sorted by severity

### CRITICAL

| Verifier | Location | Note |
|---|---|---|
| B | B05 repeated_evasions / red_flags; source NOV25 [page 15], [page 17]; FEB26 [page 4], [page 5]; JUN26 [page 16], [page 18]; AUG26 [page 7], [page 20]-[page 21] | MISSED repeated evasion: order book never quantified across 4 quarters; horizon claims contradict (none / 8 months / 1 year / 2 years); only Rs 307 Cr disclosed against the Rs 300-350 Cr FY27 defence guide |

### MAJOR

| Verifier | Location | Note |
|---|---|---|
| B | B05 2A row 3 / YAML promise_delivery; JUN26 [page 6]-[page 7], [page 19]-[page 20]; AUG26 [page 11]-[page 12] | Defence margin promise misclassified as DELIVERED. FY26 Rs 46/29 Cr does not reconcile to about Rs 33/23 Cr consolidated minus standalone; management calls it not sustaining; only Q1 FY27 (38%) is clean; CEO "No" vs CFO "Yes" on intercompany material not captured |
| B | B05 dropped_triggers / 2C; NOV25 [page 12]; FEB26 [page 14]; JUN26 [page 10]; AUG26 [page 19] | Shell pricing refusal is a 4 quarter repeated evasion. B05 records it as "never revisited", which is wrong, and leaves it out of repeated_evasions |
| B | B05 1B net debt row; NOV25 [page 14]; JUN26 [page 4], [page 11], [page 20]-[page 22] | MISSED: debt, working capital and inventory build contradict the Chairman's "strengthened balance sheet" script in the same call |
| B | B05/B06 margin commentary; JUN26 [page 8]-[page 9]; AUG26 [page 3], [page 6] | MISSED: "no margin impact" claim vs standalone EBITDA margin down 57 bps YoY in Q1 FY27, hidden by consolidated framing |
| B | B05 3D / trigger table; JUN26 [page 13]; AUG26 [page 14], [page 16]-[page 17]; BALUFORGE [page 8] | Under-weighted: Goodluck Astra (explosives/fuses outside the listed company) and the Green Energy merger with valuation withheld; logged as open items, not red flags; Balu contrast absent |
| B | B06 Part 4 net read; HITECH-Concall_Jun_2026 [page 3], [page 7]; JUN26 [page 5], [page 9] | B06 misreads the peer set on the growth miss excuse: the same input peer grew Q4 volume 27% while Goodluck's Q4 standalone revenue fell 3.9% |
| C | 01-gate0.md Block A, A3 | ROE taken from AR ratios on 3 years; the fixed formula is computable on 10 years from screener NW; median 11.80% scores 0, not 2. Block A 13 to 11, core 48 to 46, grand 56 to 54; classification AVERAGE unchanged |
| C | 07-emoat.md Section 5, rows A1 and R1 | Same licence/DGQA/CRISIL evidence credited twice (8.0 of 19.4); R1 has no independent evidence. R1 to 0 gives em 15.4 (15.9 if Atmanirbhar is credited at inference tier); MODEST unchanged |
| C | 07-emoat.md Section 2C; B07 capex_embedded_growth_pct | Rule arithmetic not run on a false "no net block schedule" premise. PPE Rs 1,201.91 Cr (AR [page 188]), revenue Rs 4,100.28 Cr (AR [page 189]), FAT 3.41x; rule value 41.6% vs substituted 12%; defence FAT reading about 6-7% as caveat; no classification change |
| D | B06 Part 1 Q5 (BALUFORGE margin proxy) | 27.0% FY26 / 27.2% FY25 EBITDA margin cited at p.5; p.5 is the Key Financial Metrics tile (FY26 EBIT margin 26.2%, a different metric); the series sits on the Historical Financial Highlights slide (p.27). Number verified correct; page anchor wrong |

### MINOR

| Verifier | Location | Note |
|---|---|---|
| B | B06 Q6 / Q5; FEB26 [page 14]; JUN26 [page 15]-[page 16]; BALUFORGE [page 8], [page 11] | PARTIALLY CAUGHT: scarcity pricing claim vs Balu's 360k line and cited 5 lakh competitor capacity; B06 uses Balu only as a timeline benchmark |
| B | B05 4D promoter sale; JUN26 dated 28-May-2026 | OVERSTATED: promoter sale silence framed as "any of the 4 transcripts"; 3 of 4 calls predate the sale |
| B | B05 red_flags GDAL; AUG26 [page 5], [page 12], [page 16] | OVERSTATED: "~9x forward EBITDA"; 15.0x-20.5x on management's own FY27 guide (Rs 1,841 Cr / Rs 90-123 Cr, calc); governance core stands |
| B | B05 credibility_basis; NOV25 [page 12], [page 16]; AUG26 [page 15] | OVERSTATED: "~2-year slip"; about 10-17 months against the NOV25 guide |
| B | B05 1B / 2A row 7; JUN26 [page 19] | Basis mislabel: the Rs 250 Cr capex guide is consolidated, not standalone |
| B | B06 Q6; BALUFORGE [page 6] | OVERSTATED: the CONTRADICTED verdict leans on a coarse journey slide (foundation 2023, shell line 2024/2025) |
| B | B06 2E / risks_peers_raise; AUG26 [page 13] | Premise not supported: "~53% export share" is export growth; the CBAM silence flag itself stands |
| B | B05 4D IR flag; JUN26 [page 20], [page 21] | PARTIALLY CAUGHT: analyst frustration on the record not cited |
| B | B05 (absent); NOV25 [page 18]; FEB26 [page 15] | MISSED: solar base Rs 250 Cr vs Rs 400 Cr contradiction |
| B | B05 (absent); FEB26 [page 10]-[page 11] | MISSED: dividend paid while borrowing for capex, defensive reply |
| B | B05 (absent); FEB26 [page 12]-[page 13] | MISSED: other expense 14% to 16% question deflected to total cost ratio |
| B | B05 (absent); NOV25 [page 7] | MISSED: Q2 FY26 EPS Rs 11.95 vs Rs 13.80 while PAT +19.43%; H1 PAT fall read out as an increase; cause NOT FOUND |
| B | B05 (absent); FEB26 [page 10]; AUG26 [page 3], [page 18], [page 20] | MISSED: standalone at 92-98% utilisation vs 15-20% guide; 40-45k t add slipping |
| B | B05 (absent); JUN26 [page 14], [page 20] | MISSED: conduit pipe margin drift (Chairman ~15%, CEO 15-25%, "take it 15-20%") |
| B | B05 (absent); JUN26 [page 13] | MISSED: gross margin 27-28% to ~33% called sustainable without reason |
| C | 01-gate0.md Block F, M7; AR [page 16], [page 39] | "Unregulated" rationale contradicts the Arms Act licence in the AR; should read PEER DATA NEEDED; score unchanged |
| C | 01-gate0.md Block F, M8; AR [page 104] | "No distribution data" premise false: BRSR dealer count 157 FY26 vs 316 FY25; moat score 8 or 9 |
| C | 07-emoat.md Section 3/5, E2; AR [page 52] | H likelihood and documented tier rest on one presentation quarter; filed FY26 FOB export growth +9.6% supports MM 2.0; em 15.4 to 14.4; MODEST unchanged |
| C | 07-emoat.md Section 3 recount line | Recount includes unanchored order filings and a presentation figure as documented; guard outcome unchanged (4 active) |
| D | B06 Part 1 Q2 / 2B (HITECH CBAM mention) | Quote genuine and verbatim; sits on the transcript's printed "Page 11 of 12" but on extraction tag page 12; numbering convention artifact |
| D | B06 Part 2B (HITECH Q1 FY27 gas price quote) | Iran war quote on extraction tag p.3 as cited; gas price quote genuine but on extraction tag p.6, one page beyond the cited p.3-5 range |

### Verifier A (no defects)

0 CRITICAL, 0 MAJOR, 0 MINOR. 65 material figures checked, 62 fully matched, 3 unanchored (peer names from company memory, not filing claims). All sampled matches carry source_fidelity true. Sampled matches: B02 CSR brought forward Rs 20.69 lakh (AR Note 36 p.178); B02 inventory Rs 809.13 Cr vs Rs 626.80 Cr (AR Balance Sheet p.145); B02 net debt +Rs 160.51 Cr (AR Note 31.1 p.170); B02 GDAL NCI equity Rs 346.43 lakh (AR SOCE p.192); B03 consolidated CFO Rs 200.24 Cr and capex Rs 347.63 Cr (AR Cash Flow p.190); B04 defence revenue 1.1% on Rs 46 Cr (AR p.34-35); B04 GDAL stake 79.43% (AOC-1 p.60-61); B05 defence guidance progression (Q2, Q4 FY26, Q1 FY27 calls); B07 GDAL Phase 2 capex about Rs 500 Cr (Reg 30, 06-Aug-2026); B08 Manish Garg SAST 3,66,200 shares (SAST Annexure #1, #29); B08 GDAL parent loan Rs 146.01 Cr (AR Note 32(iii) p.177); B09 renewable capacity 500+ GW (AR p.61). Source gate CLEAR.

## Verifier B supplementary records

- Promise delivery spot checks: 5 checked, 4 confirmed, 1 wrong (row 3, defence margin; should read PARTIAL / too early).
- Credibility grade: concur (D). Missed items C2 (order book), C1 (CEO/CFO contradiction on defence intercompany) and M9 (balance sheet script vs Rs 1,000 Cr debt) place it at the bottom of D, not higher.
- Pipeline flags not supported: B06 2E premise "Goodluck claims ~53% export revenue share" (AUG26 [page 13] answers a question on export growth); the CBAM silence flag stands (MINOR).
- Tally: 28 independent items; 12 caught, 6 partially caught, 10 missed. Material subset of 15: 7 caught, 5 partially caught, 3 missed.

## Verifier C recomputed values (phase 1)

- Gate 0: core 46; blocks A 11, B 4, C 17, D 8, E 6; moat score 8 or 9; grand total 54 or 55; moats confirmed 2; MODERATE; classification AVERAGE (unchanged).
- Emerging Moat: em_score 15.4 (A1/R1 fix), 14.4 (with E2 fix); MODEST (unchanged); capex_embedded_growth_pct 41.6 per rule, 6-7 defence FAT caveat, 12 CRISIL guide cross-check; combined assessment AVERAGE (unchanged).
- Valuation, expectation ledger and business understanding narrative checks: pending phase 3 / not in phase 1 scope.
