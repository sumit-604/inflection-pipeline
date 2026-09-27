# KROSS: verifier summary (Phase 1, run 2026-09-27)

Scope: Verifier A (numerical), Verifier B (red flags), Verifier D (peers), and the Gate 0 plus Emerging Moat half of Verifier C (framework). The valuation half of Verifier C is PENDING PHASE 3.

## Confidence delta (phase 1)

| Component | Value | Source |
|---|---|---|
| numerical_acceptance | 100.0 (raw 95.8; block states 97.9) | B12a; 48 figures; 2 MAJOR cleared by orchestrator source reread, logged in verifier-disagreement-log.md |
| redflag_coverage | 73.0 | B12b; 11 of 15 material (1 CRITICAL grade, 14 MAJOR) caught including 5 partial; 4 missed |
| framework_adherence | 76.7 | B12c phase 1 half; 46 of 60 rules (Gate 0 42, Emerging Moat 18) |
| peer_utilisation | 92.0 | B12d; 11 of 12 peer quarter cells handled correctly |
| overall | 73.0 | set by redflag_coverage; band 60 to 74; not_applicable: none |

Acceptance rates as reported by each verifier: A 97.9 | B 73 | C 76.7 | D 92.
Rework triggers: Verifier A CRITICAL 0; no acceptance rate below 60. NO REWORK TRIGGER.

## Findings, sorted by severity

### CRITICAL

None. Verifier A logged 0 CRITICAL. Verifier B listed 1 CRITICAL grade item (repeated evasion on industry relative performance); it was caught, though under weighted, so its finding row is MAJOR (12b report, line 133).

### MAJOR (13)

| # | Verifier | Location anchor | Note |
|---|---|---|---|
| 1 | A | Stage 1 Gate 0, Block D test D1 (Net Debt / EBITDA) | Borrowings FY26 Rs 53.73 Cr (screener) vs AR Rs 52.365 Cr (523.65 Mn = 291.42 + 232.23). source_fidelity true. DISPOSITION: FLAG CLEARED by orchestrator reread, AR PDF p.60 (printed p.114): screener includes lease liabilities 13.57 Mn; total 537.22 Mn = Rs 53.72 Cr. |
| 2 | A | Stage 1 Gate 0, Block D tests D1 and D4 | Cash and bank FY26 Rs 23.74 Cr (screener) vs AR cash and cash equivalents Rs 4.44 Cr (44.40 Mn). source_fidelity true. DISPOSITION: FLAG CLEARED by orchestrator reread, AR PDF p.60 (printed p.114): 44.40 Mn cash plus 192.95 Mn other bank balances = 237.35 Mn. Phase 3 note: other bank balances described as locked or collateral deposits. |
| 3 | B | B05 (missed) | Trailer axle plateau admission by CMD not captured. Concall_Nov_2025_Transcript.pdf p.13, Sudhir Rai. |
| 4 | B | B05 2D (missed, factual error) | Receivables above 90 days and constrained OCF were discussed; B05 says cash conversion is never a topic. Concall_Nov_2025_Transcript.pdf p.10-11. |
| 5 | B | B05 (missed) | Other expenses creep under two analyst insistence (26.5-28% of sales vs 24.5%; semi fixed costs 35% CAGR vs 30% revenue CAGR FY22-25), with a 22-23% revert promise, not tracked. Concall_Feb_2026_Transcript.pdf p.7, p.12-13. |
| 6 | B | B06 Claim 3 / 2B (overstated) | Peer margin outcome contradicts Kross (AUTOAXLES Q1 FY27 EBITDA 12.4% to 13.6% under same LPG and steel headwinds; HAPPYFORGE domestic lag 1 month); the excuse was upgraded to VERIFIED on mechanism alone. AUTOAXLES-Concall_Aug_2026_Transcript.pdf p.4, p.13; HAPPYFORGE-Concall_May_2026_Transcript.pdf p.8. |
| 7 | B | B05 4D (under weighted) | Repeated evasion on industry relative performance across Q2 FY26, Q3 FY26 and Q1 FY27 graded MEDIUM. Unmet "I'll let you know" on the tractor split (Q2 FY26) and the Q3 FY26 tractor lag vs industry not tracked. Concall_Nov_2025 p.7-9; Concall_Feb_2026 p.14; Concall_Jul_2026 p.6. |
| 8 | B | B05/B06 (partially caught) | Capacity capped claim contradicts stated utilisation: axles about 3,500/month against 5,000/month capacity; forging 60-70%; Q4 order book of 4,000 axles/month not met. Concall_Jul_2026 p.6, p.9; Concall_May_2026 p.7-8; Concall_Feb_2026 p.8-9. |
| 9 | B | B06 Claim 1 (under weighted) | RKFORGE Rs 120 cr = 4-5% share implies a Rs 2,400-3,000 cr market; Kross trailer revenue of about Rs 289 cr is then about 10-12%, not 26-28%. B06 calls the figures consistent. RKFORGE-Concall_May_2026 p.9; Concall_May_2026 p.5. |
| 10 | C | Gate 0, G-1, M11 band ladder | Claimed 0 (stopped after top band). Recomputed 3 on full period CAGR 27.08% with S&A share 8.91% to 2.48%; 0 on latest window CAGR 11.28%. Effect: moats 3 to 4, class MODERATE to STRONG under reading 1; GOOD holds via deal breaker 2. screener-Data_Sheet.csv rows 11 and 17; prompts/01-gate-0-pipeline.md lines 129-133. |
| 11 | C | Gate 0, G-2, E2 promoter change over 3 years | Claimed +0.87pp, score 3 (post offer baseline). Recomputed 99.99% before the offer to 68.57% Jun-2026 = minus 31.42pp, score 0; Block E 13, core 65. GOOD holds. 2024-09_Kross_Prospectus.txt lines 2020-2025. |
| 12 | C | Emerging Moat, E-1, evidence tier consistency | Claimed A1 HH x 1.0 = 4.0. Recomputed 2.8 under the stage's own A3 rule; total 13.6; 12.6 with E-2; 11.6 (NONE) if B2 also zeroed. 2026-02-27_capacity_addition.txt line 81; Annual_Report_2026.txt lines 505-508; 07-emoat.md lines 144-146 and 379. |
| 13 | D | B06 Part 3 peer coverage map, AUTOAXLES Q4 FY26 row | Marked CITED-ONLY for a market share point; same transcript holds a 90% utilisation "peak of our capacity" statement directly relevant to Claim 5, not surfaced in B06. AUTOAXLES-Concall_May_2026.pdf raw lines 365-372 (page about 6-7). source_fidelity false. |

### MINOR (22)

| # | Verifier | Location anchor | Note |
|---|---|---|---|
| 1 | B | B05 1C/2A | Extrusion slip understated as 2-3 months and labelled STRENGTHENING then DELIVERED; actual path end Q3 FY26, then Feb, Mar, May/June, then productionised Jul-2026 (about 6 months). Concall_Nov_2025 p.3; Concall_May_2026 p.10; Concall_Jul_2026 p.3, p.8. |
| 2 | B | B05 1B/1C | FY27 Tipping Jack Rs 45-50 cr (about 4,000 kits) left as live guidance; never restated after Q3 FY26; Q1 FY27 226 kits makes it unreachable; May call inconsistency (150-200 kits vs "already sold 300") not noted. Concall_Feb_2026 p.11; Concall_May_2026 p.4, p.7; Concall_Jul_2026 p.4. |
| 3 | B | B05 2A/4D | Seamless tube walkback overstated: the same Q4 FY26 call has Sudhir Rai saying "the construction work is completed". Concall_May_2026 p.4, p.7. |
| 4 | B | B06 Claim 2 | AUTOAXLES "5% to 7% down" anchored to Feb-2026 p.11 but appears in the Nov-2025 call. AUTOAXLES-Concall_Nov_2025_Transcript.pdf p.12. |
| 5 | B | B05 1B/3B | Steel settlement "Rs 4,700/kg" carried without a unit caution; May call talks Rs 3-5/kg, so per tonne is implied. Concall_Jul_2026 p.5; Concall_May_2026 p.11. |
| 6 | B | B05 3A/2A | Misattributions: the 45% leader and 35% target were first stated in Q3 FY26, not Q2 FY26; "peak capacity within a year" was Q3 FY26. Concall_Feb_2026 p.6, p.10. |
| 7 | B | B05 (missed) | AUTOAXLES is evaluating entry into trailer axles plus suspension and has the product on drawing. AUTOAXLES-Concall_Nov_2025_Transcript.pdf p.8-9, Kishan Kumar. |
| 8 | B | B05 (missed) | Extruded beam economics depend on a continuing anti dumping duty on imports. Concall_Nov_2025_Transcript.pdf p.15, Sudhir Rai. |
| 9 | B | B05 (missed) | Q1 FY27 revenue given two ways (Rs 185.35 cr vs Rs 184.3 cr) in one call; FY26 EBITDA read as 87.9%. Concall_Jul_2026 p.3-4; Concall_May_2026 p.5. |
| 10 | B | B05 (missed) | IR advisor changed from SGA to Kaptify between the Q3 and Q4 FY26 calls, with no comment. Concall_Feb_2026 p.16; Concall_May_2026 p.3. |
| 11 | B | B05 (missed) | Analyst cites a Rs 100 cr export order; management gives a Leax FY26 run rate of Rs 28-30 cr and does not reconcile the two. Concall_Feb_2026 p.10-11, Pritesh / Kunal Rai. |
| 12 | C | Gate 0, G-3, M5 scale and dominance | Claimed 1 (top 5 of a 5 name set). Recomputed 0 (smallest of set; segment rank not in provided data). screener-Data_Sheet.csv row 8 and peer sheets row 8. |
| 13 | C | Gate 0, G-4, M10 switching costs | Claimed 0. Recomputed 1 (monotone reading consistent with M4). 01-gate0.md lines 293 and 327-331. |
| 14 | C | Gate 0, G-5, M8 distribution | Claimed 0. Recomputed 1 (dealers and fabricators mentioned, unquantified). Annual_Report_2026.txt lines 206-208 and 1837. |
| 15 | C | Gate 0, G-6, M6 label | Claimed R&D NOT FOUND. AR discloses R&D expenditure NIL; score 0 unchanged. Annual_Report_2026.txt line 3530. |
| 16 | C | Gate 0, G-7, N/A rule for missing data | FY20-FY21 CE and capex proxies used where the rule directs N/A. Block A 13 and B2/B3 0 under every reading; mixed CE basis noted. prompts/01-gate-0-pipeline.md lines 19-22. |
| 17 | C | Gate 0, G-8, anchor form | Offset and approximate page anchors used; page and note anchors required. prompts/01-gate-0-pipeline.md lines 15-18. |
| 18 | C | Emerging Moat, E-2, no force fit | Claimed B2 1.0, G1 1.0. Recomputed B2 1.0 defensible via IATF marker; G1 0; total 13.8 alone. 07-emoat.md lines 182-183 and 249-251. |
| 19 | C | Emerging Moat, E-3, completionist recount | Claimed 6 items across 4 categories. Recomputed 6 categories scored at documented tier (A1, B1, B2, G1, H3, R1); list and count disagree. 07-emoat.md lines 324-329. |
| 20 | C | Emerging Moat, E-4, catalysts_12m window | Claimed 4 catalysts. Recomputed 2 within 12 months. B07-emoat.yaml lines 24-27. |
| 21 | C | Emerging Moat, E-5, anchor form | Extracted text line anchors used; slide and page anchors required. prompts/07-emerging-moat-pipeline.md lines 35-36. |
| 22 | C | Emerging Moat, E-6, block equals report | Block em_score 15 vs computed 14.8. 07-emoat.md line 400; B07-emoat.yaml line 15. |

## Verifier recomputations (as written by the verifiers)

- Verifier C, Gate 0: core 65; moat 14 or 17 (M11 reading); grand 79 or 82; moats confirmed 3 or 4; class MODERATE or STRONG; classification GOOD unchanged under every reading (deal breaker 2 caps GOOD).
- Verifier C, Emerging Moat: em_score range 11.6 to 15.7; MODEST on each finding alone and on E-1 plus E-2 (12.6); NONE (11.6) only if B2 is also zeroed.
- Verifier B, promise delivery spot checks: 6 checked, 5 confirmed, 1 wrong. Credibility grade concurrence: lower (C minus).
- Verifier D: 12 peer quarter cells audited, 9 substantive confirmed, no substantive claim unsupported, all claims addressed, no verdict discipline fails.

## Disagreement log

Two rows, both FLAG CLEARED by orchestrator source reread (AR PDF p.60, printed p.114). Full rows in outputs/final/verifier-disagreement-log.md (not modified by this stage).
