# Verifier summary — MACPOWER, phase 1

## Confidence delta and acceptance rates

| Component | Score | Verifier | Acceptance rate |
|---|---|---|---|
| Numerical acceptance | 100 | A (B12a) | 100% |
| Red flag coverage | 83 | B (B12b) | 67% |
| Framework adherence (Gate 0 + Emerging Moat) | 100 | C (B12c) | 100% |
| Peer utilisation | 92 | D (B12d) | 75% |
| Overall | 83 | min of four | band 75 to 89 normal |

Source fidelity verdict: CLEAN (B12a). No verifier logged a CRITICAL. Minimum acceptance rate 67%, none below 60%. No REWORK. Verifier C valuation component is pending phase 3.

## Findings, sorted by severity

| Severity | Verifier | Location anchor | Note |
|---|---|---|---|
| MAJOR | B | B05 concall red flag table / 4C credibility | Weak cash conversion not itemised: CFO/PAT about 40%, management says it will not improve rapidly, Q4 FY26 call p.21-22. Thesis relevant, but caught pipeline wide via FLAG-CASH in B01, B02, B03; sharpens the cash determination. |
| MAJOR | D | B06 Part 3 coverage map, KLBRENG Q1 FY26 (Aug 2025) | MIDC / local body approval quote attributed to this quarter does not appear in the Aug 2025 transcript; actual source is the Nov 2025 (Q2 FY26) transcript p.12. Quarter misattribution, not a company number error. |
| MAJOR | D | B06 Part 3 coverage map, KLBRENG Q2 FY26 (Nov 2025) | Labeled CITED-ONLY but this transcript is the actual source of the MIDC / local body land delay quote used substantively; should be SUBSTANTIVE. |
| MAJOR | D | B06 Part 3 coverage map, ADOR Q2 FY25 (Nov 2024) | Labeled CITED-ONLY but this transcript p.13 is the verbatim source of the 65% of welding equipment imported statistic used substantively; contribution undercounted. |
| MINOR | B | B05 1C / 4A backward integration trigger | Controller and core IP dependency (99% FANUC, Siemens, Mitsubishi, Q4 FY26 p.6) not flagged in B05; bounds the 25% backward integration margin lever. B07 does flag this contradiction. |
| MINOR | B | B05 1C / red flag table (export) | Export deprioritisation flagged but near zero FY26 export revenue, Rs 2 to 3 cr, Q4 FY26 p.21, not quantified. |
| MINOR | B | B05 2A row 8 / triggers (JV) | JV structure shift not captured: Q2 "may give a stake" to Q3 "denied investment, tech transfer plus royalty only", Q3 FY26 p.18. |
| MINOR | C | Gate 0, Block A / A4 | ROCE trend minus 0.46pp falls in an undefined sub 1pp decline gap; maker took conservative band 3 versus strict read 5 and flagged. Block A 18 versus 20 immaterial; classification locked by cash deal breaker plus history. |
| MINOR | C | Gate 0, Block F / M4 and M10 | Top bands need growth and receivable days stability; growth met, stability fails at plus 17.72 days; maker applied nearest band 3 and flagged. Moat count 4 (STRONG) holds. |
| MINOR | C | Gate 0, Block F / M11 | Strict band "growth above 15% but selling percent rising equals 1" yields 1 not 0 (rev CAGR 17.54%); maker scored 0 under the sub 6 year conservative scoring latitude, authorised. Immaterial; grand total band unchanged. |
| MINOR | C | Emerging Moat, YAML evidence_mix vs completionist recount | evidence_mix documented 6 versus recount "4 documented items across 3 categories" use different bases; not a scoring error, presentational. |
| MINOR | D | B06 Part 2E risks_peers_raise, ADOR entry | Parenthetical "(largely Chinese)" attached to the 65% import statistic not supported by the cited transcript; management did not specify import origin. |

Verifier A (B12a) logged zero findings across 50 material figures audited against the primary source PDFs; nothing to carry.
