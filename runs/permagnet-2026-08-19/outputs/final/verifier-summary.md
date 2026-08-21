# VERIFIER SUMMARY - PERMAGNET (run 2026-08-19)

## Confidence delta and acceptance rates

| Component | Score | Source |
|---|---|---|
| Numerical acceptance | 100 | B12a: 101 figures, 0 findings, source fidelity gate PASS |
| Red flag coverage | 57 | B12b: 4 of 7 verifier found flags caught by B05 |
| Framework adherence | 96 | B12c-framework phase 1 (97%) + B12c-valuation phase 3 (92%) |
| Peer utilisation | 100 | B12d: 12 of 12 peers used substantively |
| Overall | 57 | minimum of the four (red flag coverage bound) |

Acceptance rates by verifier: Verifier A (B12a numerical) 100%; Verifier B (B12b red flags) 57% coverage; Verifier C phase 1 (B12c-framework) 97%; Verifier C phase 3 (B12c-valuation) 92%; Verifier D (B12d peers) 92%, peer utilisation 100%.

Phase 3 valuation adherence audit: 38 rules checked, 0 CRITICAL, 0 MAJOR, 3 MINOR. Destination PE applied faithfully (17.3x additive / 14.1x RRM), no silent re derivation, no outside exit PE introduced, decision concur AVOID.

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
| B12b (red flags) | B05 growth sections | PARTIALLY CAUGHT: consolidated net profit minus 4% (15.07 vs 15.74 Cr) vs headlined standalone plus 36% divergence not flagged by B05. Anchor AR-FY26 p.19. |
| B12b (red flags) | B05 scope note | Promoter family board concentration not noted (governance stage territory, logged for completeness). Anchor AR-FY26 p.21. |
| B12c-framework (phase 1) | B07 completionist_recount | Recount says '18 documented items across 9 categories' but lists 10 categories; guard outcome (well under 12) and classification unaffected. |
| B12c-framework (phase 1) | B07 scorecard F2/H2 | H2 relay licensing scored H/H (raw 4) while F2 scores the same relay ramp execution L/H (raw 2), documented behind timeline; re rating H2 to MH=3 gives em_score 25.0, still STRENGTHENING, GOOD+ unchanged. |
| B12c-valuation (phase 3) | B11 3.2/6.5 | Amendment 14 fade horizon named but projection runs only to Year 3 (FY29), no year by year step down to Year 5; immaterial to AVOID. Rule Section 1B v3.6 Amendment 14. |
| B12c-valuation (phase 3) | B11 4 SOTP slices | Option slice values loosely rounded off stated inputs; flagged as assumptions, under Rs 6 per share, cannot flip AVOID. Rule Master v3.5 4H-pre / NEVER-estimate. |
| B12c-valuation (phase 3) | B10 divisor label | Hurdle divisor rationale mislabeled 1/(1-0.25)=1.333; correct 1.953 = 1.25^3 is the value actually used. Rule Master v3.5 Hurdle Ratio. |
| B12d (peers) | B06 Q6 | Paraphrase 'everyone is full' presented in quotation marks; actual 'everyone is expanding... all the machine tool manufacturers worldwide are full with orders' (p.9); substance accurate, page anchor correct. |

## Verifier A source fidelity note

Verifier A (B12a) checked 101 material figures spanning financial statements, balance sheet, subsidiary financials, contingencies, working capital metrics, growth rates and market data, all sourced to AR-FY26, RESULTS-Q4FY26, RESULTS-Q1FY27. Zero findings, zero fabrication, source fidelity gate PASS. No downstream step carried a figure Verifier A flagged, because Verifier A flagged none.
