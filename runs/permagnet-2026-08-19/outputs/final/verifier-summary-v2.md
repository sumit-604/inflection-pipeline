# VERIFIER SUMMARY v2 - PERMAGNET (run 2026-08-19, v2 sign-off 2026-08-23)

This v2 summary carries the phase-1 Verifier A/B/D findings from the 19-Aug record unchanged and replaces the phase-3 valuation adherence audit with the v2 Reading-2 audit (Verifier C v2, B12c-v2-valuation). The 19-Aug verifier-summary.md stays committed.

## Confidence delta and acceptance rates

| Component | Score | Source |
|---|---|---|
| Numerical acceptance | 100 | B12a: 101 figures, 0 findings, source fidelity gate PASS |
| Red flag coverage | 57 | B12b: 4 of 7 verifier found flags caught by B05 |
| Framework adherence | 96 | B12c-framework phase 1 (97%) + B12c-v2-valuation phase 3 (96%) |
| Peer utilisation | 100 | B12d: 12 of 12 peers used substantively |
| Overall | 57 | minimum of the four (red flag coverage bound) |

Acceptance rates by verifier: Verifier A (B12a numerical) 100%; Verifier B (B12b red flags) 57% coverage; Verifier C phase 1 (B12c-framework) 97%; Verifier C phase 3 v2 (B12c-v2-valuation) 96%; Verifier D (B12d peers) 92%, peer utilisation 100%.

Phase 3 v2 valuation adherence audit: 24 rules checked (18 valuation + 6 role2), 0 CRITICAL, 0 MAJOR, 1 MINOR. Destination PE applied faithfully (additive 19.6x / RRM 16.1x / NdFeB converter 13.5x per v3.7 Amendment 17), no silent re-derivation, no outside exit PE introduced, decision concur AVOID.

## Findings sorted by severity

### CRITICAL
None.

### MAJOR
| Verifier | Location | Note |
|---|---|---|
| B12b (red flags) | B05 concall report (omission) | MISSED: live 2015 Bombay HC winding up order with interim stay, auditor Emphasis of Matter across all filings, never mentioned by B05. Anchor RESULTS-Q4FY26 p.8/p.11/p.16; RESULTS-Q1FY27 p.5/p.6. Caught pipeline wide by B02/B03/B08. |
| B12b (red flags) | B05 growth/credibility | PARTIALLY CAUGHT: FY26 ROCE 11.20% vs 13.81% (minus 18.93%) and D/E 0.23 vs 0.14 (plus 64.28%) not surfaced by B05; only the capex driver discussed. Anchor AR-FY26 p.19. |
| B12d (peers) | B06 RM basket citation | RM basket quote cited at PEER-TDPOWERSYS_May_2026 p.11 but is actually at p.13 (footer 'Page 12 of 15'); p.11 is an unrelated NPCIL/receivables exchange. Claim genuine and independently confirmed; correct the anchor to p.13. Not a source fidelity matter, not a REWORK trigger. |

### MINOR
| Verifier | Location | Note |
|---|---|---|
| B12c-v2-valuation (phase 3) | B11-v2 role2 R4 | Upside/downside ratio uses additive BULL upside (Rs 965) not base, cross-track vs RRM bear; 0.17. Deviation from literal 'Upside (base)'; more generous than spec, still far below 2x, no decision or verdict impact. Rule Master v3.6 line 829. |
| B12b (red flags) | B05 growth sections | PARTIALLY CAUGHT: consolidated net profit minus 4% (15.07 vs 15.74 Cr) vs headlined standalone plus 36% divergence not flagged by B05. Anchor AR-FY26 p.19. |
| B12b (red flags) | B05 scope note | Promoter family board concentration not noted (governance stage territory, logged for completeness). Anchor AR-FY26 p.21. |
| B12c-framework (phase 1) | B07 completionist_recount | Recount says '18 documented items across 9 categories' but lists 10 categories; guard outcome (well under 12) and classification unaffected. |
| B12c-framework (phase 1) | B07 scorecard F2/H2 | H2 relay licensing scored H/H (raw 4) while F2 scores the same relay ramp execution L/H (raw 2), documented behind timeline; re rating H2 to MH=3 gives em_score 25.0, still STRENGTHENING, GOOD+ unchanged. |
| B12d (peers) | B06 Q6 | Paraphrase 'everyone is full' presented in quotation marks; actual 'everyone is expanding... all the machine tool manufacturers worldwide are full with orders' (p.9); substance accurate, page anchor correct. |

## Note on the 19-Aug phase-3 MINOR findings (superseded by the v2 audit)

The 19-Aug phase-3 audit logged three MINOR findings against the committed B11 (Amendment 14 fade horizon named but projection to Year 3 only; option slices loosely rounded but under Rs 6/share; hurdle divisor label 1.333 vs the 1.953 actually used). The v2 Reading-2 recompute (B11-v2) is the authoritative valuation; the v2 audit (B12c-v2) logged one MINOR (R4 above) with 0 CRITICAL and 0 MAJOR. The 19-Aug MINORs stay on the committed record and are decision-invariant.

## Verifier A source fidelity note

Verifier A (B12a) checked 101 material figures spanning financial statements, balance sheet, subsidiary financials, contingencies, working capital metrics, growth rates and market data, all sourced to AR-FY26, RESULTS-Q4FY26, RESULTS-Q1FY27. Zero findings, zero fabrication, source fidelity gate PASS. No downstream step carried a figure Verifier A flagged, because Verifier A flagged none. The v2 recompute introduced no new upstream figures; it re-derived the exit PE from operator-approved pillars and the operator option inputs, both anchored.
