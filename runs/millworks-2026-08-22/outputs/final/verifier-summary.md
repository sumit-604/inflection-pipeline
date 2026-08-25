# Verifier Summary (Phase 1)

Scope: Verifier A (numerical), Verifier B (red flags), Verifier D (peers), and the Gate 0 plus Emerging Moat portion of Verifier C (framework). Verifier C's valuation half runs in phase 3.

## Confidence delta and acceptance rates

| Verifier | Component | Score / acceptance | Counts |
|---|---|---|---|
| A (B12a) | numerical_acceptance | 100 | 38 checked, 0 CRITICAL, 0 MAJOR, 0 MINOR |
| B (B12b) | redflag_coverage | 67 | 15 found, 10 caught, 2 partial, 0 CRITICAL, 2 MAJOR, 3 MINOR |
| C (B12c) | framework_adherence | 96 | Gate 0 + EM only, 0 CRITICAL, 0 MAJOR, 3 MINOR |
| D (B12d) | peer_utilisation | 100 (citation accuracy 71) | 7 of 7 substantive, 0 CRITICAL, 2 MAJOR, 1 MINOR |
| Overall | | 67 | band 60 to 74, PROCEED-class downgrades one level |

Overall is pinned by redflag_coverage 67. Numerical fidelity is perfect; the gate is about interpretation completeness, not fabricated figures.

## Findings, sorted by severity

### CRITICAL

None.

### MAJOR

| Verifier | Location anchor | Finding |
|---|---|---|
| B | B05 Section 3D/4D; Reg30 20.08.2026 Annexure-A + press release | Missed the Reg 30 related-party denial (Q7 No, Q8 NA) sitting against the same-release Quik Pay investee promotion and single-customer wording; disclosure-consistency red flag on the thesis-central related-party issue. |
| B | B05 Sections 1B/2B/4D; RHP p.24 | Receivables framed as 178 days / 48.90% average basis; the RHP closing ratio of 93.22% of FY26 revenue never surfaced, understating the central risk about twofold. |
| D | B06 Part 1 Claim 3; citation "UNIMECH Q4 FY26 p.13" | Quote misattributed: the Jun_2026 passage is management confirming no revenue yet from the Kanoo-Unimech Saudi JV, not Dheya Technologies. The broader claim that Dheya revenue percentage is undisclosed is independently true; this citation does not support it. |
| D | B06 Part 1 Claim 1; citations "UNIMECH May 2026 Q&A p.14" and "UNIMECH Q4 FY26 call p.14" | One quote (Hobel 12-month visibility, p.14 of Jun_2026 file) cited twice under two call labels, presenting one source as two anchors. Root cause: B06 mislabels the Jun_2026 file as the May 2026 call. |

### MINOR

| Verifier | Location anchor | Finding |
|---|---|---|
| B | B05 4D (restatement); RHP p.36 | Second FY25/FY24 restatement disclosure not surfaced alongside the main restatement cluster. |
| B | B05 trigger #3; RHP p.90 / p.24 | Rs 14,015 lakh receivables projection framed as normalization though it exceeds FY26 close of Rs 13,868.68 lakh; absolute receivables do not fall. |
| B | B05 1A / general; Reg30 press release vs RHP p.131 | Export country count inconsistency: twelve countries (press release) vs nine (RHP). |
| C | B01 Block F, M4 customer stickiness | Scored 3 in a rubric gap; strict reading 0 to 1. moat_score would move 13 to 10, moats_confirmed 3 to 2; moat_class MODERATE and AVOID both hold regardless. |
| C | B07 Section 2C capex-embedded growth | Prescribed capex times FAT method declared INPUT GAP; B01 M3 carries FY26 Net Block 2,508.48 and FAT 5.93x, so the method was attemptable. Proxy transparently flagged; no em_score or decision impact. |
| C | B07 Section 5 scorecard B2/F2 multipliers | 0.7x applied where the taxonomy offers 1.0x/0.5x; conservative, corrected total stays MODEST and below the EM 25 qualifier. |
| D | B06 Part 1 Claim 7, APSISAERO Jun 2026 quote | Quote genuine and correctly attributed but on document page 11, cited as p.12-13; one-page offset, cosmetic. |

## Notes

- Verifier B credibility grade: concur. RHP-substitute evidence (93.22% closing receivables, 47% investee top customer, negative OCF, Section 185, filing delays into the listing window) makes grade C a floor, not a soft default.
- Verifier B promise-delivery spot checks: 3 checked, 3 confirmed, 0 wrong.
- Verifier D: peer_utilisation is 7 of 7 substantive (100); the 71 acceptance rate reflects citation-anchor accuracy only. The two MAJOR items are quote and file-label misattributions whose underlying peer conclusions still hold. Fix the Jun_2026 versus May_2026 call labels and the Dheya citation in any archived B06.
- Verifier C: recomputed decision AVOID, concurs both stages. Valuation-adherence deferred to phase 3.
