# Verifier summary — Phase 1

Company 544516 Airfloa Rail Technology Ltd | run 2026-07-15

## Confidence delta and acceptance rates

| Component | Verifier | Score | Acceptance |
|---|---|---|---|
| Numerical acceptance | A (B12a) | 86.7 | 86.7 |
| Red-flag coverage | B (B12b) | 74 | 74 |
| Framework adherence (Gate 0 + Emerging Moat) | C (B12c) | 100 | 100 |
| Peer utilisation | D (B12d) | 100 | 100 |
| Overall | | 74 | band 60-74 |

Zero CRITICAL across all verifiers. No verifier acceptance rate below 60%. rework_triggered false. Verifier C valuation-adherence audit (B10/B11) is deferred to Phase 3. Weakest component is red-flag coverage (74); its five gaps are all MINOR corroboration of already-caught risks, not new undetected risks, and Verifier B concurs with credibility grade C.

## Findings, sorted by severity

### CRITICAL
None.

### MAJOR
| Verifier | Location | Note |
|---|---|---|
| A | B02-notes Finding 9 (Annexure XXXII, SFS p.29-31) | B02 stated Raahat Financial and Share India Fincap high-cost loans were repaid to nil by FY25; Prospectus shows Rs 259.00L and Rs 600.00L still outstanding (Rs 8.59 Cr combined at 16-24% p.a.). Understates persistence of liquidity stress. Caught and corrected downstream by B03 Phase 2. Does not flip verdict. |
| A | B02-notes Finding 10 (Risk Factor 8 / Sec 135, Prospectus p.37-38) | B02 characterised CSR as cleared via a Rs 1.08 Cr FY25 payment; RoC issued four show-cause notices (29-Aug-2025) against the company and both promoter-directors personally (Rs 90.03L company, Rs 15.38L director aggregate), unresolved at Prospectus date. Material mischaracterisation; caught and corrected downstream by B03 Phase 2. |

### MINOR
| Verifier | Location | Note |
|---|---|---|
| A | B01-gate0 Block A ROCE methodology (p.2) | ROCE formula disclosed upfront and applied to verified inputs; no anchor to an accounting-standard authority. Presentation gap, not a numerical error. |
| A | B01-gate0 Block F moat scoring (p.4-5) | Moat rubric authority sits outside Verifier A scope; numerical application correct (FAT 6.34x > 3x, ROCE 25.22% > 20%). Presentation gap, not a numerical error. |
| A | B02 / B03 FY25 OCF figure | Prospectus shows FY25 OCF Rs (443.29)L; FY26 results shows Rs (286.99)L FY25 comparative. Difference is an AS-3 reclassification, not a restatement; direction (negative) unchanged. B03 identified it as explained. |
| B | B05 vs Jun-2026 call opening p4 | MISSED: volunteered working-capital-stress signals (bill-discounting charges up, delayed-payment charges present) not surfaced as direct corroboration under the already-caught cash-conversion risk. |
| B | B05 4C/1B vs Jun-2026 call, Sahil Garg p11-12 | PARTIALLY CAUGHT: management gave defence order book at Rs 60-70cr, confirmed, then retracted to Rs 29cr in one exchange; live self-contradiction not flagged as a specificity/credibility issue. |
| B | B05 2D/4D vs Jun-2026 call opening p4 | PARTIALLY CAUGHT: receivable-day "improvement" partly optical via reclassification of working capital into supplier advances under other current assets; specific optics not named. |
| B | B05 4C vs Jun-2026 call, Dhaval Pandya p7-8 | PARTIALLY CAUGHT: net D/E 0.2x rated "Good", but Rs 120cr new debt at 8.25% nearly doubles gross leverage against ~Rs 175cr equity; tension with the 0.2x-as-strength framing not reconciled. |
| B | B05 1B/4A vs Nov-2025 Shubham p7 / Jun-2026 Krupashankar p6-7 | PARTIALLY CAUGHT: Nov call portrayed the BBBS JV as already contracted/active; Jun call revealed it was not incorporated and had slipped for "internal reasons"; consistency signal not flagged. |
| C | B07 Section 5 scorecard, category B2 | Janatics sole-source MOU credited at documented 1.0x though sourced via operator secondary summary. Defensible under taxonomy; stress-test at 0.7x gives em_score 13.6, still MODEST, no classification change. Advisory, not a rule fail. |
| C | B01 Data Confidence section | "<3 years" labelled "data confidence AVERAGE" vs framework phrasing "auto AVERAGE". Cosmetic; identical net effect, correct AVERAGE floor applied. No score impact. |
| D | B06 peer_coverage_map TEXRAIL Q2 FY26 / US tariff entry | Imprecise dual-citation: the "30% export volume decline" figure appears only in the Feb-2026 transcript, not the Nov-2025 one. Not a fabrication; no verdict or conclusion affected. |

## Verifier notes

- Verifier A (B12a): 45 numbers checked, 65% of distinct figures cited; 0 CRITICAL, 2 MAJOR, 3 MINOR. Both MAJORs were already caught and corrected by B03's triple-pass verification; no fabricated or uncorrected material figure survived to synthesis.
- Verifier B (B12b): 19 independent concall red flags, 14 caught, 4 partial, 1 MINOR missed; 5 of 5 promise-delivery spot-checks confirmed; concurs with credibility grade C.
- Verifier C (B12c): 66 Gate 0 and Emerging Moat rules checked, 0 fails; valuation component deferred to Phase 3.
- Verifier D (B12d): 8 of 8 peers audited and confirmed substantive; 1 MINOR citation-precision note; no verdict-discipline fails.
