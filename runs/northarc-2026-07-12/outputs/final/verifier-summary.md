# Verifier Summary (phase 1) — NORTHARC, 2026-07-12

## Confidence delta and acceptance rates

| Component | Score | Verifier | Acceptance | CRITICAL | MAJOR | MINOR |
|---|---|---|---|---|---|---|
| Numerical acceptance | 87.5 | A (B12a) | 87.5 (28/32) | 0 | 2 | 1 |
| Red flag coverage | 75 | B (B12b) | 75 (9/12 caught, 3 partial, 0 missed) | 0 | 1 | 4 |
| Framework adherence | 91 | C (B12c) | 91 | 0 | 1 | 3 |
| Peer utilisation | 93 | D (B12d) | 93 (13/14) | 0 | 1 | 0 |
| Overall | 75 | min | normal band (75 to 89) | 0 | 5 | 8 |

Valuation framework adherence (verifier C on the valuation stages) is DEFERRED TO PHASE 3; B12c.valuation is blank and its rules_checked is 0. This summary covers the Gate 0 and Emerging Moat portion of verifier C only. REWORK not triggered: no CRITICAL from any verifier, no acceptance rate below 60%, overall above 60.

## All findings, sorted CRITICAL then MAJOR then MINOR

| Sev | Verifier | Location | Finding |
|---|---|---|---|
| MAJOR | A (B12a) | 01-gate0.md, ROE reconciliation | Report claims FY26 computed ROE 11.08% reconciles to company-disclosed 11.1%; the Q4FY26 investor presentation discloses FY26 ROE of 14.0% and no 11.1% figure appears in source for FY26. Computed 11.08% is arithmetically correct; the sourcing claim is inaccurate (basis difference). Resolve the ROE basis at assembly. |
| MAJOR | A (B12a) | 02-notes.md finding #2 | The standalone +22.3% PAT and the Pragati loss are FY25 (AR) phenomena; FY26 standalone PAT growth was +18.5% (406.02 vs 342.62). Label timeframes carefully to avoid conflating FY25 and FY26. |
| MAJOR | B (B12b) | B05 4D / 2D / row 11, HFC red flag | Claim that HFC/NCLT went "completely unmentioned in the Q4 call with no analyst prompting" is overstated; Aviom was raised by Digant Haria and answered by Atul ("Aviom we continue to provide, no one-off"), Q4 PDF p.9. Only the NCLT resolution timeline update is missing. Drives the top red flag's severity on a false total-silence premise. |
| MAJOR | C (B12c) | B01 classification | Literal core 32 < 40 = AVOID per matrix; AVERAGE rests solely on the operator-instructed adjusted-basis rescaling (32/80 = 40%, exactly the 40.0 boundary). The report's second justification, deal breakers "cap at max AVERAGE and corroborate," is logically invalid: a cap is a ceiling not a floor, and AVOID also satisfies "max AVERAGE." Class survives on operator authority and a consistent exclusion set, not independent framework support. Cleaner native path (deal breaker #9, 1.75yr public history to AVERAGE) available but unused. |
| MAJOR | D (B12d) | B06 Part 1, Q7 verdict table | MASFIN "20 to 25 new branches per year" is sourced to the Q3 FY26 earnings call but actually appears in the Vision 2036 Investor Day transcript (16-Feb-2026, p.12). The "208 branches, lesser pace than anticipated" portion is correctly sourced. Misattribution; the Investor Day should be reclassified SUBSTANTIVE not CITED-ONLY. Directional Q7 conclusion survives on the correctly attributed language. |
| MINOR | A (B12a) | 03-ardeep.md Phase 1E | Audit fee shows Rs 97.00 lakh (Note 29.1) versus Rs 33.40 lakh (Corporate Governance Report), unreconciled in the AR; likely cash-paid versus accrued basis. Immaterial (audit fees under 0.3% of PAT); disclosure clarity gap only. |
| MINOR | B (B12b) | B05 1C / row 8, FY27 credit cost | "Guided progressively worse across three consecutive calls" is imprecise: Q3 to Q4 top improved 3.0% to 2.8%; only Q2 to Q3 worsened. Net-worse conclusion stands. |
| MINOR | B (B12b) | B05 2A, FY26 credit cost delivery | FY26 credit cost "2.8% delivered in line" is net of the FLDG benefit plus a Rs 66 Cr overlay; gross was about 2.9 to 3% (Pardhasaradhi, Q4 PDF p.12). Earnings-quality nuance not connected to the delivered figure. |
| MINOR | B (B12b) | B05 Q4 page anchors | Q4 anchors use printed page numbers, one lower than PDF markers (cover letter = PDF p.1). Findable but inconsistent convention. |
| MINOR | B (B12b) | B05 1C / dropped_triggers, new funds | "New fund launches never named again in Q3 or Q4" is slightly off; Q4 opening (PDF p.8) has a generic "new sets of funds being launched." Specific funds indeed not re-named. |
| MINOR | C (B12c) | B01 Block A / A4 | A4 = 3 for a 0.76pp ROCE decline falls in the undefined gap between the "latest >= earliest = 5" and "decline 1 to 3pp = 3" bands; nearest-lower-band choice is conservative. No impact: Block A = 3 < 8 either way; deal breaker #1 fires regardless. |
| MINOR | C (B12c) | B01 Block F / M4, M10 | M4 = 3, M10 = 3: the "= 5" band requires a receivable-days sub-condition that is N/A for an NBFC; dropping to "= 3" is the conservative mapping. No effect on moats_confirmed (still 3) or MODERATE class. |
| MINOR | C (B12c) | B07 Section 3 summary | "6 of 20" Strong/Moderate should read 5 of the 20 categories (D1, D2, B3, F2, G1) plus R1 (the 21st category); the YAML active_categories lists all 6 correctly. Presentational only; no effect on score or classification. |

## Verifier B coverage note

Red flag coverage 75 is the binding minimum but reflects 3 PARTIAL and 0 MISSED. The upstream concall work had no blind spot; the 3 partials are severity and phrasing nuances. Verifier B concurs with the Grade B credibility read: in-year delivery strong, forward guidance repeatedly softened, HFC/Aviom unresolved but provisioned and not concealed. Promise-delivery spot checks: 5 checked, 5 confirmed, 0 wrong.
