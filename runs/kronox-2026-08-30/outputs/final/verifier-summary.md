=== FILE: verifier-summary.md ===

# Verifier summary (phase 1)

Phase 1 covers Verifier A (numerical), Verifier B (red flags), Verifier D (peers), and the Gate 0 plus Emerging Moat portion of Verifier C (framework). The valuation portion of Verifier C is pending phase 3.

## Confidence delta and acceptance rates

| Component | Score | Verifier | Acceptance rate |
|---|---|---|---|
| numerical_acceptance | 97.14 | A (B12a) | 97.14% |
| redflag_coverage | 78 | B (B12b) | 67% |
| framework_adherence | 97 | C (B12c, phase-1 Gate0+EM only) | 97% |
| peer_utilisation | 100 | D (B12d) | 100% |
| overall | 78 | min of four | normal band 75-89 |

No REWORK trigger. Zero CRITICAL findings; every acceptance rate is above the 60% floor.

## Findings, sorted by severity

### CRITICAL
None.

### MAJOR

| Verifier | Location | Finding |
|---|---|---|
| A (B12a) | B03 ARDEEP (report p.256; AR Note 36, p.114) | Interest coverage / DSCR cited as 17.30x is unanchored. AR Note 36 lists interest coverage 328x (3,741.7 / 11.4); 17.30x appears nowhere in AR p.1-120. source_fidelity: true. Gate 0 used the correct 328x, so the fortress balance sheet direction is unchanged. Correct the anchor or drop 17.30x before phase 3. |
| B (B12b) | B05 Section 2A/2D and analyst_note (earnings quality) | Missed that FY26 profit growth is non operating: other income roughly doubled (Rs 519.40 vs 252.60 lakh), operating PBT +1.2%, revenue +1.03%. Q1 FY27 PAT +38.5% is tax flattered (effective tax 25.6% vs 37.5%); operating PBT +16.2%. B05 called the Q1 figure a genuine acceleration without the caveat. Thesis relevant to trigger #2 and the forward earnings basis. Anchors: Board's Report p.36; FY26 results p.2; Q1FY27 results p.3. |

### MINOR

| Verifier | Location | Finding |
|---|---|---|
| B (B12b) | B05 red_flags (capital allocation) | Missed the FY26 shift from debt free to small borrowings (proceeds Rs 160.7 lakh, finance cost Rs 11.4 lakh) while holding a large, growing fixed deposit balance. Immaterial amount, unexplained capital allocation quirk. |
| B (B12b) | B05 red_flag #4 (MD&A) | Under-weighted: the MD&A lacks all company specific financial performance and outlook discussion, not only sector data. Graded LOW; Verifier B reads LOW-MEDIUM. Substance caught. |
| C (B12c) | B01 Block E, E2 | 1-year-window substitution for a 3-year metric (3-year window spans the Jun-2024 IPO OFS, not in corpus); inconsistent with the strict rule-5 treatment given to E3. Defensible under rule 6 and flagged. Worst-case core 72, still AVERAGE. No decision change. |
| C (B12c) | B01 Block B, B2/B3 | 2-year FCF window (FY23/FY24 capex absent) versus strict rule-5 read. Defensible under rule 6 and flagged. Worst-case Block B 13, core 72, still AVERAGE. No decision change. |

### Verifier D (peers)

No findings. 4 of 4 peers audited substantive; all 5 peer questions addressed; no verdict discipline fails. Acceptance 100%.

### Verifier C Emerging Moat portion

31 rules checked, no fails.

## Source-fidelity note

The one source-fidelity MAJOR (B12a, DSCR 17.30x) does not enter any phase-1 verdict computation. Disposition: GATE HELD, figure to be corrected against source (correct anchor 328x shown) in phase 3. Gate 0 already used the correct 328x, so no downstream number carries the flagged figure.
