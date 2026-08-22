# Verifier summary (Phase 1)

## Confidence delta and acceptance rates

| Component | Score | Acceptance |
|---|---|---|
| Numerical (Verifier A, B12a) | 98 | 98% (64 numbers, 0 CRITICAL) |
| Red flag coverage (Verifier B, B12b) | 65 | 62% |
| Framework adherence (Verifier C, B12c; Gate 0 + Emerging Moat only) | 97 | 97% |
| Peer utilisation (Verifier D, B12d) | 100 | 100% |
| Overall | 65 | band 60 to 74 |
| Valuation framework adherence | pending phase 3 | not run |

Source fidelity gate: HELD. Verifier disagreement log: none this run.

## Findings, sorted by severity

No CRITICAL findings.

### MAJOR

| Verifier | Location anchor | Note |
|---|---|---|
| B (B12b) | B05 Section 2D red_flags; RHP p.32 & 59 | V3 Technologies related party transactions omitted from the B05 scan; caught by B02, B03 and B08 elsewhere. |
| B (B12b) | B05 red_flags / B06 cross-read; RHP p.25 (RF4) | Big Bang Boom execution dependency and bill to ship to structure missed by B05 in a 69% defence book; surfaced in B03, B05 triggers and B09. |
| B (B12b) | B05 red_flags concentration scan; RHP p.30-31 (RF11) | Supplier concentration (44.05% single, 84.31% top 10, no long term contracts) missed by B05; caught by B04. |
| D (B12d) | B06 Part 2B / Q2; cited "Airfloa Jun 2026 p.12-13" | Aluminium +80% / steel +60-65% war quote is genuine but sits on internal p.9 (extraction p.10), not p.12-13. Anchor offset; quote exists and supports the point. |

### MINOR

| Verifier | Location anchor | Note |
|---|---|---|
| A (B12a) | B03 Phase 2D receivables | DSO about 340 days (ageing table) versus 178 days (MD&A p.209), both in the RHP with no reconciliation. B03 correctly flags this as a disclosure gap, not a report error. source_fidelity true, non blocking. |
| B (B12b) | B05 red_flag #6 compliance; RHP p.27 | Section 185 related party director loans lumped into a generic non compliance bucket. |
| B (B12b) | B05 Section 1B guidance; RHP p.31 (RF12) | FY27 implied revenue built on a restated CA certified working capital table; the restatement was not flagged. |
| B (B12b) | B05 sources note / anchoring | Business chapter RHP citations point about 7 pages behind the extracted markers; exact anchor existence handed to Verifier A. |
| C (B12c) | B01 Block F, M4 customer stickiness | Scored 1/5 under an ambiguous rubric tier; a literal reading could support 3/5. Conservative, immaterial; moat count and classification unchanged. |
| C (B12c) | B07 Section 5, E2 China+1 | 1.0 documented multiplier applied where the narrative calls the defining claim inference; 0.5 would be consistent (10.6 to 10.1). No band or decision impact. |
| C (B12c) | B07 evidence_mix vs completionist_recount | documented 14 vs recount 8 count different scopes; unreconciled, presentational only. |
| D (B12d) | B06 Q3/Q4; "Unimech Feb 2026 p.11 / p.10-11" | Unimech domestic defence and MTAR exchange quotes are on internal p.10, not p.11. Anchor offset. |
| D (B12d) | B06 Q3; "Unimech Jun 2026 p.7" WC days 120-125 | The 120-125 days figure is on internal p.6; the adjacent 50% utilization on p.7 is correct. |
| D (B12d) | B06 Q2/2E; "Apsis Jun 2026 p.4" | 45 day collection, 18.38% to 13.14% receivables and 52% to 35% concentration are on internal p.5, not p.4. |
| D (B12d) | B06 Q1; "Apsis Jun 2026 p.5" Atmanirbhar quote | Quote is on internal p.3, two pages earlier than cited. |
| D (B12d) | B06 Part 2E; "Airfloa Jun 2026 p.20 / p.11" | China machinery delay on internal p.19 not 20; 8.25% rate on p.10 not 11; paired Rs 120 Cr debt figure on p.8 correct. |
| D (B12d) | B06 Q4; "Airfloa Nov 2025 p.4-5" drone/laser | Big Bang Boom JV and Rs 65 Cr order on p.3-4 correct; the drone / anti drone / laser characterization is on internal p.8. |

## Reading

The two verifiers that scored 100 and 98 (peer and numerical) found only anchor offsets and one internal RHP inconsistency. No fabrication, no source fidelity blocker, no misclassification. The 65 red flag coverage and the 62% B12b acceptance both trace to the same cause: B05 did not surface three items itself, and other stages did. The pipeline red flag set is complete.
