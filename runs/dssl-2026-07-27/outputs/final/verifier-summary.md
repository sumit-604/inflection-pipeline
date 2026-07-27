# Verifier Summary (phase 1)

Phase 1 verifiers: A (numerical, B12a), B (redflag, B12b), C (framework, Gate0 + emerging moat portion only, B12c), D (peer, B12d). Verifier C valuation adherence is deferred to phase 3.

## Confidence delta and acceptance rates

| Verifier | Component | Score | Acceptance rate | Counts |
|---|---|---|---|---|
| A (B12a) | Numerical acceptance | 100 | 100% | 0 CRITICAL / 0 MAJOR / 0 MINOR (14 figures checked) |
| B (B12b) | Redflag coverage | 84 | 75% | 0 CRITICAL / 1 MAJOR / 4 MINOR (16 flags, 12 caught + 3 partial) |
| C (B12c) | Framework adherence (Gate0 + EM) | 99 | 99% | 0 CRITICAL / 0 MAJOR / 4 MINOR (67 of 68 in scope rules clean) |
| D (B12d) | Peer utilisation | 87.5 | 88% | 0 CRITICAL / 1 MAJOR / 2 MINOR (14 of 16 transcripts used) |
| Overall | min of four (redflag bound) | 84 | | 75 to 89 normal band, no downgrade, REWORK not triggered |

## Findings, sorted by severity

### MAJOR

| Verifier | Location anchor | Note |
|---|---|---|
| B (B12b) | B05 vs Q4 FY26 transcript p4 / p5-6 / p13-14 | Fixed asset build carried only as PPE Rs8cr to Rs68cr; Rs158cr analyst read figure (two analysts) and roughly Rs90cr gap unreconciled, management dodged quantification ("that is already mentioned"), capital intensity of pivot understated about 2.3x. Deepens FLAG-CASH. |
| D (B12d) | B06 Part 3 / coverage_map, 3i Infotech Jul-2023 and Jan-2025 rows | Both calls marked UNUSED / "unrelated to any of the five claims", but both are directly and accurately cited in B06's own Part 1 (Claim 4 and Claim 2). Internal inconsistency; peer_utilisation understated by at least 2 transcripts (self reported 12/16 corrected to 14/16, 75% to 87.5%). |

### MINOR

| Verifier | Location anchor | Note |
|---|---|---|
| B (B12b) | B05 red-flags vs Q4 FY26 transcript p7 | PAT flat YoY on +22% revenue (opex model earnings quality) not isolated as its own signal. |
| B (B12b) | B05 2A/1C vs Q3 p9 and Q4 p11 | Two quarter "judge us YoY not QoQ" deflection pattern and a buried Q3 -3.3%/-3.6% QoQ decline not surfaced. |
| B (B12b) | B05 red-flags vs Q4 FY26 transcript p16 | Management admission of deliberate cost absorption to win acquisition customers not extracted (partly caught only via B06 peer contrast). |
| B (B12b) | B05 red-flag / 2C vs Q4 transcript | Scripted "temporary blip" line given to five analysts (Akash Jain included), reported as four; undercount understates the flag. |
| C (B12c) | B01 Block A ROCE derivation | Framework prefers source supplied ROCE; maker computed a hybrid capital employed basis. Documented, cross validated vs Acuité, immaterial to GOOD classification. Prefer source series per literal rule. |
| C (B12c) | B01 M4 Customer Stickiness = 3 | Borderline PASS; Tier 5 correctly rejected (receivable days 67.9 to 154.3d not stable), Tier 3 satisfied on literal max one decline year. Destination insensitive; a downgrade still keeps GOOD (capped by deal breaker 2). |
| C (B12c) | B07 capex_embedded_growth_pct = 0 (FLAG-METHOD) | Framework consistent: 2C arithmetic shown (~2,006% via 193x artefact FAT), correctly judged non applicable; order book cross check (~+108%) substituted in body. Phase 3 must read the FLAG-METHOD note / 108% figure, not the literal 0. |
| C (B12c) | B07 6D combined assessment = GOOD+ | GOOD backward plus MODEST forward lifted a half tier; HIGH POTENTIAL correctly not claimed. Well reasoned, on the generous edge of latitude, no enumerated matrix cell violated. |
| D (B12d) | B06 Part 2E / risks_peers_raise item 4 | Claimed Aurionpro converts 60 to 90% of EBITDA to cash by year end; transcript states 75 to 80% or more, "90% plus last year" (Aurionpro Q2 FY26 call, 04-Nov-2025, lines 267-268). Direction correct, 60% lower bound unsupported. |
| D (B12d) | B06 Part 3 / coverage_map, 3i Infotech Nov-2023 row | Marked UNUSED, unrelated to any claim; contains a loosely analogous scaling pain / margin dilution data point not used. Low materiality, changes no claim verdict. |

## Verifier notes carried to the gate

- Verifier A: 0 findings, 100% acceptance. No source fidelity flags. No figure was flagged for existence or mis anchoring, so no re-derivation is subordinate to a Verifier A flag this run.
- Verifier B credibility concurrence: concur, grade B (Good); candid on headlines and proactive on the miss, capped by two quarter unit economics non disclosure, scripted deflection, and the dodged Rs158cr asset quantification. Promise delivery spot checks 5 checked, 5 confirmed, 0 wrong.
- Verifier C: history_downgrade CORRECT (FALSE); FTTCP conflation CLEAN (B07 firewalled from FTTCP); all Gate0 and EM flags assessed framework consistent.
- Verifier D: claims_all_addressed true; verdict_discipline_fails none; 4 of 4 distinct peer companies contributed at least one verified citation.
