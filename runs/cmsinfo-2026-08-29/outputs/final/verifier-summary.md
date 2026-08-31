# VERIFIER SUMMARY — CMS Info Systems (CMSINFO)

Run: runs/cmsinfo-2026-08-29. All four verifiers, findings sorted CRITICAL, then MAJOR, then MINOR.

## Confidence delta and acceptance rates

| Component | Verifier | Score | Acceptance rate |
|---|---|---|---|
| Numerical acceptance | A (Haiku 4.5) | 96.7 | 96.7 |
| Red flag coverage | B (Opus 4.8) | 64 | 64 |
| Framework adherence | C (Opus 4.8) | 88 combined | phase 1: 96; phase 3: 79 |
| Peer utilisation | D (Sonnet 5) | 83 | 67 |
| **Overall** | | **64** | binding constraint = red flag coverage |

Counts: 0 CRITICAL source fidelity (Verifier A); 1 CRITICAL peer citation (Verifier D); 4 MAJOR; 15 MINOR. No REWORK trigger: no B12a source fidelity CRITICAL, no verifier acceptance rate below 60, overall not below 60.

## CRITICAL

| Verifier | Location | Note |
|---|---|---|
| D peers | 06-peers.md Part 2B and Part 3 coverage map (QUESS Q4 FY26 / May 2026 row) | "Rs176cr one-time Labour Code revenue/cost pass-through" attributed to QUESS not found in Feb 2026 or May 2026 transcripts; only real QUESS Labour Code figure is Rs7cr. Load bearing for the Part 2B peer cost scale comparison only, NOT for any verdict; core DSO contradiction anchors (Radiant/SIS) unaffected. Corrected at synthesis, not cited. |

## MAJOR

| Verifier | Location | Note |
|---|---|---|
| A numerical | B02-notes Rank 1 and 2; B03-ardeep Phase 2 triple pass | SA 1-2yr overdue 16.2x, CON 8.5x, SA loss allowance 14.1% release cited with correct AR note and page anchors but table structure not independently re-verified in ASCII text; source_fidelity true. ORCHESTRATOR CLEARED at source (grep confirms SA Rs1,490.59m ~p.99, CON Rs1,516.32m ~p.131, SA prior Rs92.14m); verifier limitation was ASCII table collapse, not a source mismatch. |
| B red flag | B05 LBF-3 / Section 4A vs Aug 2026 p.4/17 | Cut revenue and raise margin narrative graded "strong" on EBITDA (27.2%, +170bps) while EBIT margin compressed to 10.3% from 14.1% on depreciation; the raised metric excludes the cost hitting the bottom line. Under weighted selective metric framing on the load bearing claim. |
| C framework (phase 1) | 01-gate0.md Block E, E2 | E2 promoter holding change scored 3 (neutral) after the report states the literal formula yields 0 (26.69% decrease, >3% = 0); no E2 alt path exists, operating rule 2 forbids qualitative judgment. Framework correct E2 = 0. Core 76 to 73, grand total 88 to 85, classification GOOD unchanged. |
| C framework (phase 3) F6 | 11-valuation.md Sec 4.2 and 4.5 verdict card; B11 mos_price 227 | 20% MoS applied without stating the mandatory evidence scaled row or basis; governing FY28 proof gate catalyst window is 18-24 months (the 40% row trigger), which would set MoS about Rs 170 not Rs 227. Decision unaffected (WATCHLIST regardless; CMP above MoS under either reading; operator referenced Rs 227). |
| D peers | 06-peers.md Part 1, claim 7 and intro | "high receivable days" quote cited to AGSTRA-Concall_Jul_2024 does not exist there; the real exchange is in AGSTRA-Concall_Feb_2024. Cited in support of the DSO contradiction, whose core Radiant/SIS anchors are independently confirmed clean, so the finding survives. Corrected at synthesis, not cited. |

## MINOR

| Verifier | Location | Note |
|---|---|---|
| A numerical | B01-gate0 Block B4; B03-ardeep Phase 2 2D | FY26 Receivable Days 130.93 (Data_Sheet receivables/sales x 365) vs MD&A Key Ratios DSO 126 days (AR p.52); 4.93 day method difference, not a contradiction, same rising trend. |
| B red flag (missed) | Nov 2025 p.4/20; Feb 2026 p.3/19 | MS&Tech segment revenue base does not reconcile: Q2 FY26 stated Rs271 Cr (Nov 2025) vs Rs216 Cr implied by the Feb Q3 bridge; Rs55 Cr gap, no reconciliation; likely resegmentation, unstated; the Tech line is the re-rating engine. |
| B red flag (missed) | Feb 2026 p.4-5/19 | Three different Q3 FY26 EBITDA margin figures inside one call (25.5%, 24.5%, 22.8%), no stated basis for each. |
| B red flag | B05 guidance log / Nov 2025 p.4/20 to May/Aug 2026 p.4/17 | FY26 capex crept from about Rs300 Cr initial guide to Rs350 Cr actual (about 17%) with no acknowledged overrun, while services revenue guidance was cut; logged but not flagged as a walk. |
| B red flag | B05 guidance log / Nov 2025 p.8/20 to Feb 2026 p.9/19 | Provisioning / ECL guidance walked up 4% to 4.25-4.5% of revenue within one quarter (above FY25 3.7%), a receivables stress proxy; logged but not flagged as an upward re-guide. |
| C framework (phase 1) | 01-gate0.md end of file | Required closing fenced YAML block not present in the report artifact (capture artifact); the B01 block exists in outputs/blocks; narrative arithmetic verified instead and internally consistent. |
| C framework (phase 1) | 07-emoat.md end of file | Required closing fenced YAML block not present in the report artifact (capture artifact); the B07 block exists in outputs/blocks; narrative scorecard (23 rows, adjusted 23.1) verified instead. |
| C framework (phase 1) | 07-emoat.md F1 vs I1 | The "70% AI/ML" figure is tagged (D) at F1 but (C) at I1; immaterial, a C re-tag moves the total to about 22.8, still MODEST, does not approach the 25 point STRENGTHENING threshold. |
| C framework (phase 3) F1 | 11-valuation.md Sec 1B Pillar 1 base PE; B10 pillar_1_base_pe | Band table 16.0x used; general Amendment 5 formula 0.5x16.6+7.5 = 15.8x; 0.2x gap, operator Override 4, disclosed and logged. Decision impact none. |
| C framework (phase 3) F4 | 11-valuation.md Sec 1B row I; B10 amendment_20_relative_trim | 17.0x cut labelled "Amendment 20 relative trim / 30% test FAILED" but the pillar 18.4x sits ABOVE peers; the amendment 30% test is one directional. The cut is an operator conservative override, not the amendment mechanism; the number binds via Amendment 20.9. Decision impact none. |
| C framework (phase 3) F3 | B10-assembly.yaml ua_qualifiers lines 156-160 | gate0_or_em marked NO citing EM<25; the OR is satisfied by Gate0 core 76>=60, so the qualifier is YES; UA still does not apply because FII+DII 58.70% fails the <3% leg (B11 reasons this correctly). Decision impact none. |
| C framework (phase 3) F5 | 14-thesis.md Sec 7 verdict box; B14 verdict WATCHLIST | WATCHLIST emitted, but Master WATCHLIST = "CMP above Entry" (here 243 < 284); the unresolved gap pending named events pattern maps more literally to INSUFFICIENT CONVICTION; operator authoritative WATCHLIST call binds; action identical. Decision impact none. |
| D peers | 06-peers.md Part 1, claim 5 | AGSTRA ATM decline quote (PSB consolidation, 26,000 new ATMs) correctly quoted but misattributed to "Ravi Goyal"; actual speaker Stanley Johnson. |
| D peers | 06-peers.md Part 1, claims 4a and 7 (SIS) | SIS page anchors follow the transcript printed footer numbering rather than the [[PAGE N/11]] bracket convention; apparent off by one; all underlying quotes verbatim confirmed. |
| D peers | 06-peers.md Part 3 coverage map, AURIONPRO Q2 FY26 | Marked UNUSED "no relevant terms matched"; the transcript in fact contains a DSO / receivables exchange (different industry, low materiality, no verdict change). |
