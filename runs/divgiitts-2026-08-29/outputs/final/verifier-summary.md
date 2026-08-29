# VERIFIER SUMMARY — Divgi TorqTransfer Systems Ltd (DIVGIITTS)

Run: runs/divgiitts-2026-08-29. Covers Verifier A numerical (B12a), Verifier B red flags (B12b), Verifier C framework and valuation adherence (B12c, phase 1 gate0 plus emoat and phase 3 valuation), Verifier D peer utilisation (B12d).

## Confidence delta and acceptance rates

| Component | Score | Acceptance rate |
|---|---|---|
| Numerical acceptance (B12a) | 68.4 | 68.4% (57 checked, 39 clean) |
| Red flag coverage (B12b) | 82 | 76% |
| Framework adherence (B12c) | 97 | gate0 100%, emoat 100%, valuation 88%, full 97% |
| Peer utilisation (B12d) | 75 | 94% |
| Overall | 68.4 | min of the four; band 60 to 74 |

REWORK gate: not triggered. Verifier A returned 3 CRITICAL source fidelity findings, all pipeline correct catches of Spear brief or source level errors, each corrected at source (GATE HELD) and none used as valid on a verdict card or a Section 1B pillar. Verifier C phase 3 valuation adherence: 0 critical, 0 major, 3 minor (all cosmetic or disclosed override). Overall 68.4 is above the 60 REWORK floor. Cross family FTTCP grader SKIPPED (no key); FTTCP confidence held one notch lower.

## CRITICAL (3)

| Verifier | Location | Finding | Disposition |
|---|---|---|---|
| A (B12a) | B01 Gate 0, Spear load-bearing fact | Claimed roughly Rs 275 Cr net cash decline in FY26; source truth: net cash rose Rs 283.76 Cr to Rs 292.75 Cr, up about Rs 9 Cr (Note 10(a)+(b), CFO letter p.39). source_fidelity true. | GATE HELD. Spear brief error the pipeline (B01/B02/B03) contradicted; never used as valid downstream. |
| A (B12a) | B03 AR Deep Dive, Section 6D | Claimed US subsidiary described as an established FY26 operating fact; source truth: board approved 25 May 2026, Delaware incorporation 4 June 2026, both after 31 Mar 2026 close. source_fidelity true. | GATE HELD. AR internal contradiction B03 flagged; B03 did not assert the subsidiary existed. |
| A (B12a) | B09 TAM / B05 Concall context | Claimed Indonesia 70,000 unit transfer case program; source truth: B09 web verification confirms 35,000 units (Mahindra Scorpio Pik Up Indonesia CY2026). source_fidelity true. | GATE HELD. B05 accurately transcribed the concall claim of 70k; B09 self corrected to 35k and flagged the gap. |

## MAJOR (13)

| Verifier | Location | Finding |
|---|---|---|
| A (B12a) | B02, confirmed B03 | AOC-2 to Note 34 rent income gap claimed 19.5x; corrected to 1.95x (Lakh to Million conversion error). Disclosure gap remains at the corrected ratio. source_fidelity true. |
| A (B12a) | B02/B03 Notes | Three conflicting FY26 MD remuneration figures in the same AR: Note 34 Rs 21.49 Mn vs Corp Gov/Annexure C Rs 17.75 Mn; increase unclear 15% or 73.6%. source_fidelity true. |
| A (B12a) | B02/B03 Notes | Note 42 current ratio explanation cites reduction in current assets; balance sheet shows current assets rose 13.9%, liabilities rose 58%. Explanation contradicts own balance sheet. source_fidelity true. |
| A (B12a) | B02/B03 Notes | GST contingent liability: Note 37 Nil vs CARO Rs 1.63 Mn pending dispute; same audit, same date, opposite disclosures. source_fidelity true. |
| A (B12a) | B02/B03 Related party | Note 34(a) RPT list incomplete: Tejal Transmission (Note 5 equity holding, Hirendra Divgi on board) absent. Ind AS 24 completeness failure; entity never entered Audit Committee approval. source_fidelity true. |
| A (B12a) | B02/B03 R&D | BRSR R&D Rs 117.94 crore vs Business Driver Rs 117.94 million; 100x unit error. Million reading confirmed; R&D actually fell 13.6% YoY. source_fidelity true. |
| A (B12a) | B01 Gate 0 data | Screener FY25 interest Rs 0.60 Cr vs AR audited FY25 finance cost Rs 0.382 Cr; 58% discrepancy. B01 used the PDF audited figure. source_fidelity true. |
| A (B12a) | B05 Concall context | June 2026 FY25 results resubmission claim; source truth: verified 11 July 2025, a technical XBRL/PDF correction with unmodified audit. Date in run brief does not match. source_fidelity true. |
| A (B12a) | B05 Concall context / B01 | Sigma EV SOP claimed in Q2 FY27; no Q2 FY27 date in the three provided concalls; documented slippage April to July to 12 Aug still progressing. Unverifiable from the pipeline corpus. source_fidelity true. |
| B (B12b) | B05 4C / 2C margin treatment | MISSED management volunteered negative: Q1 FY27 29.4% EBITDA margin is a one off, guidance 20% to 22%. Bears on durability of the record quarter. Anchor: Q1 FY27, Jitendra Divgi. |
| B (B12b) | B05 SPEAR fact 1 / 3C | PARTIALLY CAUGHT: Indonesia order reframed Q3 (specific, time bound one off, concludes by FY27 end) to Q1 (over 50% recurring); cross quarter contradiction not surfaced. Anchors: Q3 FY26 Jitendra to Karthi; Q1 FY27 Jitendra opening. |
| D (B12d) | B06 Claim 5, peer evidence item 3 | Sona Comstar quote anchored to Q3 FY26 (Jan 2026); source truth: verbatim in Q4 FY26 call (30 Apr 2026), p.15. Wrong quarter attribution. Claim 5 CONTRADICTED verdict unaffected; two other correctly anchored peer quotes satisfy the two anchor rule. source_fidelity false. |

## MINOR (9)

| Verifier | Location | Finding |
|---|---|---|
| A (B12a) | (3 minor within 57 checked) | Three minor numerical items inside the 57 number check; all non source fidelity, no decision impact. |
| B (B12b) | B05 1C (FY28 bridge) | PARTIALLY CAUGHT: execution bandwidth constraint and opportunities pushed out because of Indonesia load not surfaced. Anchor: Q1 FY27 Jitendra opening. |
| B (B12b) | B05 1B (component volume) | MISSED: management inconsistent on its own component volume (1mn/3.3mn/7 lakh/13 lakh). Anchor: Q4 FY26 Karan Gupta / Jitendra / Sudhir. |
| B (B12b) | B05 3C row 2 | Anchor imprecision: strip Indonesia question attributed to Karan Gupta; actual asker Sumit Ambekar (Parami). Substance stands. |
| B (B12b) | B05 2A promise delivery table | Wording imprecision: EV proof of concept demo by July; transcript says going into production. Direction correct. |
| C (B12c) | B01 Block A (A1/A2/A4) | Phase 1: ROCE computable FY25-26 only (data gap); no score or decision impact. |
| C (B12c) | B07 scorecard C1 | Phase 1: 1.0 multiplier defensible on filed presentation; STRENGTHENING band unchanged. |
| C (B12c) | B07 completionist recount | Phase 1: cosmetic labelling; 12 alarm threshold applied correctly. |
| C (B12c) | B11 Section 2 (2A/2B/2C) | Phase 3: Amendment 18.0 bear/bull not projected to Year 4 explicit rows; base fully to FY31. No decision impact (AVOID all cases). |
| C (B12c) | B11 verdict card | Phase 3: Amendment 4.3 first line Tier A / Hurdle 25% declaration absent; correct Tier A and 1.953 threshold applied everywhere. Cosmetic. |
| C (B12c) | B14 verdict card / Section 7 | Phase 3: mechanical AVOID vs emitted WATCHLIST; disclosed operator posture defaulting to AVOID, action today no position equals functional AVOID. |
| D (B12d) | Coverage map HAPPYFORGE and SANSERA Q4 FY26 | Two CITED-ONLY rows not independently re read line by line; audit coverage gap on the verifier side, not a confirmed B06 defect. Residual risk low. source_fidelity false. |

## Verifier concurrence notes

- Verifier B concurs with the credibility grade B: delivery strong, but EV slip, thin disclosure, and a management flagged one off margin peak hold the grade at B. Promise delivery spot checks: 5 of 5 confirmed.
- Verifier C recomputed destination PE: concur (additive 20x, RRM 17.9x, operator 30x override, all math clean). Recomputed decision: concur (AVOID/STOP on valuation; WATCHLIST label is disclosed operator framing, functional AVOID).
- Verifier D: 12 of 12 substantive peer claims confirmed, all claims addressed, no verdict discipline fails.
