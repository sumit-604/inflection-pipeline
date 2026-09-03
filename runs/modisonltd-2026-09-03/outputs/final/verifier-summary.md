# Verifier Summary (Phase 1)

Phase 1 verifier findings: A numerical, B red flags, D peers, and the Gate 0 plus Emerging Moat portion of C. Valuation adherence (the B10/B11 half of C) is deferred to phase 3.

## Confidence delta and acceptance rates

| Component | Verifier | Score | Acceptance | Counts |
|---|---|---|---|---|
| numerical_acceptance | A (B12a) | 87.5 | 87.5% | 24 checked, 0 CRITICAL, 2 MAJOR, 5 MINOR |
| redflag_coverage | B (B12b) | 81 | 81% | 16 flags, 13 caught, 2 partial, 1 missed |
| framework_adherence | C (B12c) | 100 | 100% | 72/72 rules passed (Gate 0 + Emerging Moat); valuation deferred |
| peer_utilisation | D (B12d) | 100 | 100% | 8/8 transcripts used; accuracy acceptance 89% separately |
| overall | min | 81 | normal band (75-89) | no verdict downgrade, no forced REWORK |

Source fidelity gate: CLEAR. Verifier A logged zero source fidelity findings (no MISMATCH, no ANCHOR NOT FOUND, no material UNANCHORED). No number is barred from downstream use.

## Findings sorted by severity

No CRITICAL findings from any verifier.

### MAJOR

| Verifier | Location | Note | source_fidelity |
|---|---|---|---|
| B (B12b) | B06 Part 4 / 2B / 5, priority contradiction | "Both peers compress margin" is overstated. SBCL EBITDA margin expanded ~250bps to 22.9% and calls silver margin neutral; the contradiction rests on Salzer alone, a weaker product match. Anchor: SBCL May-2026 lines 88, 166-169; Aug-2026 lines 250-259; Salzer Aug-2026 lines 152-157. | n/a |
| A (B12a) | B02 Notes Finding 3, receivables | Claimed receivables +83.8% to Rs 160.60 cr; AR-FY26 p.139 shows +85.7% to Rs 159.97 cr gross. 1.9pp variance, immaterial to conclusions. | false |
| A (B12a) | B01 Gate 0 Block A, EBITDA | Claimed FY26 EBITDA Rs 118.36 cr (screener formula); AR shows Rs 115.29 cr after exceptional, Rs 123.60 cr before. Definition/basis difference, both valid, not a numerical error. | false |
| D (B12d) | B06 Claim 4, Part 1 | SBCL "250-260 days" net working capital quote attributed to Nov-2025; it is verbatim in the Feb-2026 transcript (lines 741-763). Correct peer, wrong quarter; underlying claim substance still stands. | n/a |
| D (B12d) | B06 Part 3, coverage map SBCL Nov-2025 | "Flat/5-6% domestic switchgear growth" credited to Nov-2025; the "5 or 6%" phrase is verbatim only in Feb-2026 (lines 183-184). Same misattribution pattern; belongs to the Feb-2026 row. | n/a |
| D (B12d) | B06 Claim 2 verdict field | ~5.1% LV growth marked VERIFIED on SBCL alone across 3 quarters; Salzer logged as non corroborating in the same paragraph. Rule 4 requires PARTIALLY VERIFIED for single peer verdicts. | n/a |

### MINOR

| Verifier | Location | Note | source_fidelity |
|---|---|---|---|
| B (B12b) | B05 Section 4D red flag table / Notes | PARTIALLY CAUGHT: the FY26 record 16.2% margin is substantially a Q4 timing catch up from retroactive tungsten price approvals, not consolidated as a quality of earnings red flag. Anchor: AGM Speaker 7, lines 124-131. | n/a |
| B (B12b) | B05 Section 3C / 4D | PARTIALLY CAUGHT: Rs 9.51 cr Q4 FY26 silver hedging loss sits in a 3C footnote, not elevated to the red flag table, despite contradicting the "sometimes we hedge" framing. Anchor: AGM Yash Kotari hedging answer, line 151. | n/a |
| B (B12b) | B06 peer cross read | MISSED: SBCL's unnamed pricing transparency dig at silver contacts competition, indirectly relevant to Modison. Anchor: SBCL May-2026 lines 186-189. | n/a |
| A (B12a) | B01 Gate 0 Block A, ROCE | Claimed ROCE FY26 37.51%; AR Note 50 company disclosed 23.31% on a different formula. Framework 37.51% verified. Two valid definitions in use. | false |
| A (B12a) | B02 Notes, MCPL RPT window | Claimed Rs 80 cr ceiling for Apr-2026 to FY26-27 AGM (~15 months); AGM Notice Resolution 5 runs it from the 43rd AGM (21-Jul-2026) to the 44th AGM. Ceiling verified; start differs by ~3 months. | false |
| A (B12a) | B04 Business Model, export split | Claimed export 11.9% (Rs 85.16 cr of Rs 716 cr); AR p.38 shows export FOB Rs 82.16 cr, revenue Rs 710.33 cr, 11.56% on the standard base. Rs 716 is total income. | false |
| A (B12a) | B03 AR deep dive, R&D FY26 | Claimed Rs 1.59 cr (0.22% of revenue); Annexure F exact figures not visible in extracted text. Likely extraction gap; recommend PDF verification against Annexure F. | false |
| A (B12a) | B07 Emerging Moat, export growth | AGM claims 12% growth and Rs 90 cr+ exports; AR p.38 shows 5.79% growth, Rs 82.16 cr. Discrepancy correctly flagged by B07; no stage error. | false |
| D (B12d) | B06 Claim 3, Part 1 | SBCL May-2026 also states its own contacts business had "a very small market share to begin with" domestically; unused context, not claim determinative, would not change the UNVERIFIABLE verdict. | n/a |
| D (B12d) | B06 Part 5 / 2E export narrative | Salzer Aug-2026 states a "newer growth businesses" export target of "back to 25%"; scope versus the company wide 27-30% figure not reconciled. Flagged for completeness. | n/a |

### Verifier C (framework adherence, phase 1 scope)

No findings. Gate 0: 55 rules checked, 0 fails. Emerging Moat: 17 rules checked, 0 fails. Total 72/72 passed, acceptance 100%. Valuation audit (B10/B11 against Master v3.6, Section 1B, FTTCP) deferred to phase 3. Business understanding narrative audit out of scope in phase 1 (Stage 13 not yet audited).

## Verifier disagreement note

Verifier A found zero source fidelity findings, so no downstream step leaned on a flagged number and no flag was cleared by re check. Disagreement log for phase 1: none. The two MAJOR clusters from B and D are analysis quality corrections, not source fidelity. Both are carried into the gate recommendation: B06's "both peers compress" is corrected to Salzer only (SBCL corroborates), and B06's two SBCL quotes are re dated from Nov-2025 to Feb-2026 with substance intact.
