# AWFIS verifier summary (phase 1, 2026-09-19)

Scope: Verifier A (numerical), Verifier B (red flags), Verifier D (peers), and the Gate 0 plus Emerging Moat portion of Verifier C. The valuation, expectation ledger and narrative audits of Verifier C are PENDING PHASE 3.

## Confidence delta (phase 1)

| Component | Score | Source |
|---|---|---|
| Numerical acceptance | 97.8 | B12a, 44 of 45 checked figures clean |
| Red flag coverage | 77 | B12b, 10 of 13 material flags held (4 full, 6 partial); strict full catch 31% |
| Framework adherence | 84.4 | B12c, phase 1 portion, 54 of 64 rules |
| Peer utilisation | 100 | B12d, 12 of 12 transcripts substantive |
| Overall | 77 | set by red flag coverage; band 75 to 89 |

## Acceptance rates and counts

| Verifier | Model | Acceptance rate | CRITICAL | MAJOR | MINOR | Basis |
|---|---|---|---|---|---|---|
| A numerical | claude-haiku-4-5 | 97.8 | 0 | 1 | 4 | 45 of 92 material figures checked (49% stratified sample) |
| B red flags | claude-opus-5 | 77 | 1 | 9 | 11 | 25 independent flags, 13 material; strict full catch 4 of 13 = 31% |
| C framework (phase 1) | claude-opus-5 | 84.4 | 0 | 6 | 8 | Gate 0 42 rules, EM 22 rules |
| D peers | claude-sonnet-5 | 100 | 0 | 0 | 2 | 12 of 12 peer transcripts substantive |
| Total | | | 1 | 16 | 25 | |

## Findings, sorted by severity

| Sev | Verifier | ID | Location anchor | Note |
|---|---|---|---|---|
| CRITICAL | B | F1 | 05-concall.md (B05); Nov-2025 p.10; Feb-2026 p.15-16; Aug-2026 p.14 | B05 missed repeated realization/cohort-margin evasion across Nov, Feb, Aug; promised annual disclosure lapsed; all peers disclose Rs/sqft |
| MAJOR | A | (A1) | B09 TAM Section 2A Method 3 peer aggregation table, Indiqube row | Claimed 1,469 Cr (FY26); source truth 1,450.81 Cr per INDIQUBE-Data_Sheet.csv row 11; variance -18.19 Cr (-1.24%); source_fidelity: true |
| MAJOR | B | F2 | 05-concall.md (B05); Feb-2026 p.15-16; Aug-2026 p.8 | B05 missed churn denial vs 1.5-2%/month admission |
| MAJOR | B | F3 | 05-concall.md (B05); Aug-2026 p.8; May-2026 p.13 | B05 missed likely-known client exit at May call; over-credits Aug disclosure |
| MAJOR | B | F4 | 06-peers.md (B06) claim 5; May-2026 p.11; Indiqube Nov-2025 p.6, p.12 | B06 claim 5 cash-margin comparison on mismatched bases |
| MAJOR | B | F5 | 06-peers.md (B06) claim 7; Aug-2026 p.17; Smartworks Nov-2025 p.17, Jul-2026 p.11 | B06 claim 7 verdict should be directional contradiction |
| MAJOR | B | F6 | 05-concall.md (B05) 4D; Nov-2025 p.13-14; May-2026 p.19; Aug-2026 p.10-11 | Cash-rent questions in three calls not linked or elevated to 4D |
| MAJOR | B | F7 | 05-concall.md (B05); Nov-2025 p.8; Aug-2026 p.7, p.9-10 | Metric switch to cash EBITDA not flagged; Nov FY27 margin promise untestable |
| MAJOR | B | F8 | 05-concall.md (B05) 4D; Nov-2025 p.7, p.12; May-2026 p.15; Aug-2026 p.11 | MA stance change under-weighted as LOW |
| MAJOR | B | F9 | 05-concall.md (B05) 2A row 7; Nov-2025 p.10; May-2026 p.19; Aug-2026 p.8 | Closure-promise outcome mis-evidenced; Nov baseline missed |
| MAJOR | B | F10 | 05-concall.md (B05); May-2026 p.11, p.13; Aug-2026 p.12-13 | Rising capex per gross seat and 50% developer fit-out share not computed |
| MAJOR | C | G-1 | 01-gate0.md Block A, A3 | FY25 ROE excluded by an unwritten sign-crossing rule; recomputed A3 5 (median 25.58%); Block A 7 -> 10; deal-breaker 1 clears |
| MAJOR | C | G-2 | 01-gate0.md Block B, B2 | FY19/FY20 determinably FCF-negative (CFO -11.48, -7.79) dropped as NOT FOUND; recomputed B2 2 (71.4%); Block B 10 -> 7; deal-breaker 2 fires, non-binding |
| MAJOR | C | G-3 | 01-gate0.md Block E, E4 | Filed nil contingent liability (AR Note 33(i)) scored as missing data; recomputed E4 5; Block E 5 -> 10; GST SCN exposure carried as flag |
| MAJOR | C | G-4 | 01-gate0.md Block F, M11 | Missing FY26 selling-expense leg filled with FY25; FY25 proxy shows only -0.14pp; recomputed M11 0; moat score 24 -> 19; 4 present, STRONG unchanged |
| MAJOR | C | E-1 | 07-emoat.md Section 5, F2 | Net-negative F2 scored 0.7 while contrary-evidence C2/B1 scored 0; recomputed F2 0; EM 11.8 -> NONE; escalate re-test at phase 3 if Pillar 3 consumes em_classification |
| MAJOR | C | E-2 | 07-emoat.md H2 and H3 | WELL certification double-credited (H2 and H3, same anchor; also listed as existing brand moat in 6E); recomputed EM 10.5 (fix b) or 11.5 (fix a, H2 re-rated MM); maker to choose and re-rate |
| MINOR | A | (A2) | B09 Section 2A Method 1 CBRE-FICCI figure | Claimed Rs52,200 Cr (2025-26); web-sourced live report 24-Mar-2026, not in corpus; report transparently attributes to live-web search; source_fidelity: false |
| MINOR | A | (A3) | B09 Section 2A Method 3 WeWork India peer revenue | Claimed Rs2,477 Cr (FY26); web-searched company results release, not in corpus; source_fidelity: false |
| MINOR | A | (A4) | B09 Section 2A Method 3 Table Space peer revenue | Claimed Rs2,262 Cr (FY26); web-searched Entrackr/Inc42 media aggregate, not in corpus; source_fidelity: false |
| MINOR | A | (A5) | B04 Bizmodel Section 3B must-track metrics, FY27 cash-EBITDA guidance | Claimed ~10.8-11.1% for FY27; external company-memory store (companies/AWFIS.md), not filed or web-sourced; correctly attributed; source_fidelity: false |
| MINOR | B | F11 | 05-concall.md (B05) 4D; Nov-2025 p.4, p.8; Feb-2026 p.17 | D&B transfer silence overstated |
| MINOR | B | F12 | 05-concall.md (B05); Aug-2026 p.7, p.17 | Cash EBITDA guide misquoted/misattributed |
| MINOR | B | F13 | 05-concall.md (B05) anchors; Aug-2026 p.7; May-2026 p.17; Nov-2025 p.15; Feb-2026 p.12 | B05 anchors mix internal and PDF pagination; Verifier A to re-check |
| MINOR | B | F14 | 05-concall.md (B05); Nov-2025 p.4; Feb-2026 p.17 | Retail/hospitality walk-back missed |
| MINOR | B | F15 | 05-concall.md (B05); Feb-2026 p.7, p.10 | Tenure inconsistencies missed |
| MINOR | B | F16 | 05-concall.md (B05); May-2026 p.12; Aug-2026 p.15 | Transform margin basis shift missed |
| MINOR | B | F17 | 05-concall.md / 06-peers.md; Nov-2025 p.7; Aug-2026 p.4; Smartworks Aug-2025 p.3 | ROCE drift and peer basis evidence unused |
| MINOR | B | F18 | 05-concall.md (B05); Feb-2026 p.8; Aug-2026 p.10 | Net debt/equity swings unremarked |
| MINOR | B | F19 | 06-peers.md (B06) claim 4; Smartworks Jul-2026 p.6 | B06 claim 4 Smartworks gap 5 pts; mixed occupancy bases |
| MINOR | B | F20 | 06-peers.md (B06); Indiqube Feb-2026 p.6, p.8 | B06 misattributes Indiqube Q3 deferral to cash EBIT |
| MINOR | B | F21 | 05-concall.md (B05); Aug-2026 p.3, p.15 | GCC $ inconsistency occurs within Aug call itself |
| MINOR | C | G-5 | B01-gate0.yaml flags/analyst_note; 01-gate0.md decision line | 2-of-8-year window contradicts body's 5-of-8; propagated to B07 6C/6D; text fix only |
| MINOR | C | G-6 | 01-gate0.md M8 | Per-centre revenue implied on signed supply, not operational centres; score likely unchanged |
| MINOR | C | G-7 | prompts/01-gate-0-pipeline.md M9, M10 | Rubric gaps: unmapped states (M9 above peers with higher growth; M10 one decline year with unstable receivables); operator rubric fix; no present/absent change |
| MINOR | C | G-8 | 01-gate0.md Block A table | FY25/FY26 rows garbled; corrected in note; presentational |
| MINOR | C | E-3 | 07-emoat.md Section 5 | Zero rows grouped; stage 7 asks for all 23 rows; presentational |
| MINOR | C | E-4 | B07-emoat.yaml evidence_mix; 07-emoat.md 6C | evidence_mix does not reconcile with recount; 6C says 2 Weak, lists 3; text fix |
| MINOR | C | E-5 | 07-emoat.md A2, D2, F1, H3 | AR anchors are text line numbers labelled as pages; re-anchor to PDF pages |
| MINOR | C | E-6 | 07-emoat.md 2C; B07 capex_embedded_growth_pct | Guided (not under-execution) capex x company gross-block FAT 1.5x; B01 FAT 0.88x basis gives 12.1%; 20.6% stands if basis labelled downstream |
| MINOR | D | (D1) | B06 Claim 3 / Part 3 coverage map, DevX Q3 FY26 (02-Feb-2026) | Rs400-600/sqft design/execution fee cited at p.7-8; figure appears at p.20 of DEVX-Concall_Feb_2026_Transcript.txt; page-anchor mismatch; figure itself genuine |
| MINOR | D | (D2) | B06 Claim 5, Indiqube Q2 FY26 (10-Nov-2025) citation | "cash EBIT" ~21% described as explicit label match, p.6; management's answer uses "EBITDA" phrasing, never "cash EBIT"; substance and direction correct; descriptor overstates lexical fidelity |

IDs in brackets are positional. Verifiers A and D do not number their findings.

## Verifier B: pipeline flags not supported

| Status | Pipeline flag | Verifier reason | Anchor |
|---|---|---|---|
| WRONG VERDICT | B06 claim 7 UNVERIFIABLE (lease-reset lag) | peers describe 2020-21 vintage as repricing upside and escalation spreads as tailwind; directional contradiction | Smartworks Nov-2025 p.17, Jan-2026 p.12, Jul-2026 p.11; Indiqube Nov-2025 p.11 |
| OVERSTATED | B06 claim 5 VERIFIED: Awfis cash margin roughly half peer band | basis mismatch; peers' post-rent EBITDA compares to Awfis normalized 14.3%, not cash 10.1%; like-for-like gap ~2-9 pts | May-2026 p.11; Indiqube Nov-2025 p.6, p.12; Smartworks Jul-2026 p.3; DevX Aug-2026 p.3 |
| OVERSTATED | B05 2C/2B: Q1 FY27 client-exit disclosure is strongest transparency evidence | exit likely known at May call; unresolved until notice date known | Aug-2026 p.8; May-2026 p.13 |
| OVERSTATED | B05 4D: D&B business transfer never raised on calls | subsidiarisation volunteered and questioned; only consideration/valuation absent | Nov-2025 p.4, p.8; Feb-2026 p.17 |

Promise delivery spot checks: 6 checked, 5 confirmed, 1 wrong. Credibility grade concurrence: "lower - C leans on a client-exit transparency credit that is unresolved, and misses a 3-call realization evasion and a contradicted churn denial".

## Verifier C: stage figure and verifier figure

| Item | Stage figure | Verifier C figure | Classification concur |
|---|---|---|---|
| Gate 0 blocks | A 7, B 10, C 8, D 1, E 5 | A 10, B 7, C 8, D 1, E 10 | |
| Gate 0 core score | 31 | 36 | yes, AVOID both |
| Gate 0 moat score | 24 | 19 | |
| Moats confirmed | 5 (STRONG) | 4 (STRONG) | |
| Grand total | 55 | 55 | |
| Deal breakers triggered | 1, 3, 4, 8 | 2, 3, 4, 8 | |
| EM score | 12.5 | 9.8 to 11.8 | no |
| EM classification | MODEST | NONE | no |

## Verifier D: peer audit

12 peer transcripts audited, 12 substantive and confirmed. No unsupported substantive claim, no unused relevant transcript, all claims addressed, no verdict discipline failure.

## Verifier A source fidelity disposition

One source fidelity finding: Indiqube FY26 revenue in the B09 peer aggregation, 1,469 Cr claimed against 1,450.81 Cr source truth (INDIQUBE-Data_Sheet.csv row 11). Disposition: GATE HELD, corrected. The synthesis files carry the corrected figure only. No downstream step in phase 1 argued to keep the flagged figure. Verifier A logged no CRITICAL finding, so no source fidelity REWORK applies.
