# INDNIPPON verifier summary (Phase 1 lite, run 2026-09-10)

## Phase 1 confidence delta

| Component | Value | Source |
|---|---|---|
| numerical_acceptance | 97.2% | B12a, re-invocation, 180 claims checked, 175 clean |
| redflag_coverage | 29% | B12b, 7 caught of 24 independent red flag items (5 partially caught) |
| framework_adherence | 82% | B12c, phase 1 scope only: Gate 0 23 of 29 rules, EM 24 of 28 rules; valuation audit PENDING PHASE 3 |
| peer_utilisation | 100% | B12d, 12 of 12 peer transcripts substantive |
| overall | 29 | minimum of the four |

Band: BELOW 60, FORCED REWORK (confidence.yaml). REWORK triggers fired: verifier acceptance rate below 60% (B12b, 29%) and overall below 60.

## Acceptance rates

| Verifier | Model | Scope | Acceptance rate | CRITICAL | MAJOR | MINOR |
|---|---|---|---|---|---|---|
| A, numerical | claude-haiku-4-5 | 180 numbers, re-invocation | 97.2% | 0 | 1 | 0 |
| B, red flags | claude-opus-4-8 | deck and narrative layer, no concall mode | 29% | 2 | 15 | 12 |
| C, framework | claude-opus-4-8 | Gate 0 and Emerging Moat only | 82% | 0 | 1 | 9 |
| D, peers | claude-sonnet-5 | 12 peer transcripts | 92% | 0 | 2 | 2 |

Count note: B12b files major_count 15 and minor_count 12. Its findings list holds 12 MAJOR and 11 MINOR rows, plus 2 MINOR reasoning defect rows. The rows below reproduce every row the block holds.

## Findings, sorted by severity

### CRITICAL

| # | Verifier | Location anchor | Note |
|---|---|---|---|
| 1 | B | B05/B06 scope gap; Q4FY26 deck p.19 and Q1FY27 deck p.18 vs AR2026 Note 51 (PDF p.235, p.297) | Deck ROCE 34.97% vs audited 17%, undisclosed definition, three rung QUALITY LADDER implication. Not surfaced by B05 or B06. OPEN at Halt 1; Verifier A did not examine it. |
| 2 | B | B05/B06 scope gap; deck EBITDA (Q4FY26 deck p.16) vs Reg 33 results filing 2026-08-07 p.4, AR2026 Note 29, Note 35 | FY26 margin expansion of 17bps is an artefact of FX gains netted into operating expenses; audited basis margin was 11.11% to 11.10%, flat to down. Removes the quantitative support for the mix shift thesis. Not surfaced by B05 or B06. OPEN at Halt 1; Verifier A did not examine it; no phase 3 margin input may use FY26 until resolved. |

### MAJOR

| # | Verifier | Location anchor | Note |
|---|---|---|---|
| 3 | A | 01-gate0.md Block B; 02-notes-pass1.md LB1; 05-concall.md Section 2A. Sources: AR2026 p.9 (extracted L421-423); Q4FY26 deck p.19; Q1FY27 deck p.18; 01-gate0.md L167-169 | Three FY26 working capital days figures in the company's own documents: AR letter 42 to 40, decks 42 (up from 40), audited basis computation 51.48. COMPANY ANOMALY, retained, not an analyst misread. Upstream correctly flagged it. |
| 4 | B | AR2026 MD&A p.125 vs Note 51 | "Net Profit Margin 13.7%" is a pre tax margin including a one off; audited net profit ratio is 10.40%. 330bps overstatement inside one annual report. |
| 5 | B | Results filing 2026-08-07 pp.1-2, 6-7 vs Q1FY27 deck 2026-08-21 | CFO cessation omitted from the deck filed 14 days later; the filing itself calls the same event both a resignation and a designation change. |
| 6 | B | Five decks p.3 vs AR2026 MD&A (PDF p.127) and BRSR | Three employee counts (1,605+ / 2,601 / 2,811); the deck figure is frozen across five quarters. |
| 7 | B | AR2026 Note 43 (PDF p.228) vs deck technology narrative | R&D flat and R&D capex down 41.7% while revenue grew 26.6%; intensity fell 75bps. The transition claim is not funded in the filed numbers. |
| 8 | B | AR2026 Note 42 (PDF pp.226-227) | Parent company receivable stretched about 80 to about 108 days on +22% related party sales; the aftermarket channel is the 70.32% shareholder. |
| 9 | B | AR2026 BRSR + Note 34 + Note 42 + MD&A risk table (PDF p.125, p.219, p.227) | 91.7% of workers non permanent; Rs 30.6 Cr apprentice stipend routed to a related party and off the employee benefits line; labour code risk named in one clause and never quantified while all three peers quantified it. |
| 10 | B | Q1FY27 deck pp.13-17 | Every table labelled CONSOLIDATED after the company's own note says consolidation ceased; consolidated FY24-FY26 columns sit beside a standalone Q1FY27 column under one header. |
| 11 | B | Q1FY27 deck p.17; Q2FY26 and Q4FY26 decks p.4 | Two uncorrected chart errors, one contradicting the same deck's own income statement page. |
| 12 | B | AR2026 Note 37 (PDF p.220) vs deck p.7 boilerplate | Advertising and sales promotion down 30.8% against a verbatim five quarter claim of constant sales promotion and brand building. |
| 13 | B | Results filing segment note (p.4) vs deck pp.4-5 | Single audited segment; deck mix splits unaudited; general purpose parts near tripled to 9% of revenue with no narrative anywhere. |
| 14 | B | B05 Section 2D, under weighted | Lucas TVS Level 3 stake at 32.2% of net worth, valued on a self set 8x EV/EBITDA, is the whole of OCI; the Q1FY27 markdown of Rs 1,675L pre tax is reported as a table row with no narrative while TCI fell 45.7%. B05 names the gap, not the mechanism. |
| 15 | B | B05 Section 2A, reasoning basis | Customer concentration contradiction is cleaner on the percentage basis (67.33% FY24 to 70.65% FY26) than on the rupee basis B05 used, which is vulnerable to rebuttal. |
| 16 | C | B01 reports/01-gate0.md L60; blocks/B01-gate0.yaml blocks.A, core_score, grand_total | A1 median ROCE 13.68% scored 3; band table "15-19.9 = 3 / 10-14.9 = 1"; correct score 1. Block A 9 to 7, core 56 to 54, grand 75 to 73. Deal breaker 1 (Block A under 8, max GOOD) flips to TRIGGERED, non binding at AVERAGE. Classification AVERAGE unchanged. |
| 17 | D | 06-peers.md Part 1 Q2; YAML verified[1] | Varroc lag quote ("a lag of at least a quarter, but we are expecting to be compensated in full despite this lag") is real and correctly attributed, but sits in VARROC Jun2026 (Q4 FY26) physical page 8, not VARROC Aug2026 as cited. Substantive claim stands. Corrected citation: VARROC Jun2026 p.8. |
| 18 | D | 06-peers.md Part 1 Q3; Peer Coverage Map MINDACORP Q4 FY26 row | Kit value figure (Rs 50,000 to 100,000, 4W EV power electronics kit) does not appear in MINDACORP May2026 as cited. The real exchange is in MINDACORP Feb2026 (Q3 FY26): "INR 50,000 to INR 60,000... could even go up to INR 90,000 or INR 1 lakh." Substantive claim stands. Corrected citation: MINDACORP Feb2026. |

### MINOR

| # | Verifier | Location anchor | Note |
|---|---|---|---|
| 19 | B | AR2026 milestone timeline p.16 | A third EFI partner (Athena, Italy) exists alongside BorgWarner and the unnamed MoU; B05 reconciles two of four threads. |
| 20 | B | Deck series p.14 | Leadership claim narrows from "No. 1 in ignition systems" (Q1FY26) to "No. 1 in Fly Wheel Magneto" (Q4FY26 onward); no source or share % in either form. |
| 21 | B | Q1FY26 deck vs AR2026 MD&A | Aftermarket growth decelerated from 28% (Q1) to 20% (full year) with no comment and is never sized. |
| 22 | B | AR2026 Note 45 | Capital commitments up 618% (Rs 367L to Rs 2,635L) and disputed income tax up 44.1%, with no capex plan or project named in any deck. |
| 23 | B | Q4FY26 deck p.14 vs results filing Note 6 | Exceptional item is Rs 445L compensation plus Rs 1,076L interest (71% interest); the deck describes it only as land compensation. |
| 24 | B | Deck series p.15 | Q1FY26 comparatives silently restated between decks (EBITDA 235 to 234, margin 10.46% to 10.41%, PAT 232 to 233, EPS 10.26 to 10.30) with no restatement note. |
| 25 | B | AR2026 MD&A p.124-125 vs results filing p.4 | Three FY26 revenue bases (audited Rs 1,06,848L; MD&A Gross Rs 1,06,440L; MD&A Net Rs 1,05,292L). |
| 26 | B | AR2026 Note 51 vs MD&A vs deck p.19 | Three FY26 ROE figures (15% / 14.5% / 13.58%) with no basis stated on any. |
| 27 | B | Deck p.16 vs AR2026 Note 44 | Deck EPS 49.14 is consolidated, AR EPS 49.18 is standalone; neither cross references the other. Basis trap for valuation. |
| 28 | B | AR2026 MD&A pp.121 and 124 | Two EV penetration figures in one MD&A (8.5% and near 10%); deck separately says 7%. |
| 29 | B | AR2026 Notes 34, 37, 42, 51 | Gratuity expense +291.8%, directors' commission +109.8%, Lucas TVS management fees Rs 832L with no service description, return on investment down to 13% from 14%. None explained. |
| 30 | B | B05 promise delivery row, EFI ECU via BorgWarner (AR2026 extracted L1294-1299, L851-855, L827) | Reasoning defect. Pivot fact supported. Verdict too harsh: the AR records EFI ECU nominations from major OEMs and an Athena partnership. Downgrade MISSED to PARTIAL. |
| 31 | B | B05 promise delivery row, customer concentration | Reasoning defect. Conclusion correct; on the percentage basis FY25 to FY26 share fell (73.82% to 70.65%); the valid contradiction is FY24 to FY26, 67.33% to 70.65%. |
| 32 | C | B01 reports/01-gate0.md L41-44, L207-218; data_notes[1] | Ex exceptional restatement of FY26 PAT/EBIT is outside the fixed formula set; disclosed and conservative. On the literal formula C2 = 4, Block C = 13. |
| 33 | C | B01 reports/01-gate0.md L142-155 | B2 scored on a 2 year FCF window, below the 3 year minimum; strict reading gives B2 = 0, Block B = 3. Window disclosed. |
| 34 | C | B01 blocks/B01-gate0.yaml deal_breakers[0] | Deal breaker entry names no driving years. |
| 35 | C | B01 blocks/B01-gate0.yaml data_notes vs input_gaps[6] | M2 and M5 PEER DATA NEEDED recorded under input_gaps, not data_notes. No scoring effect. |
| 36 | C | B01 reports/01-gate0.md L72, L241, L259, L263, L345 | Six approximate tilde page anchors against the exact page form, including E1 promoter holding and E4 net worth. |
| 37 | C | B07 reports/07-emoat.md L459-460; completionist_recount | Strength tally states 9 Weak; actual 11 (4 Moderate / 11 Weak / 8 None). No score effect. |
| 38 | C | B07 reports/07-emoat.md L462-471 | Recount hedged ("approximately 34") and labels 13 as non zero categories where non zero rows are 15. Recount was performed; no tier inflation found. |
| 39 | C | B07 blocks/B07-emoat.yaml evidence_mix | claim = 4 against 5 distinct claim tier items. No score effect. |
| 40 | C | B07 reports/07-emoat.md L79, L326, L390 | Three anchors use extraction line offsets or an out of range page instead of the mandated form. |
| 41 | D | 06-peers.md Part 1 Q4; YAML contradicted[0]; flags[0] | Varroc "no change in receivable days" quote is real and verbatim but cited as page 17; actual location is extraction page 16, printed "Page 15 of 18". Content, speaker, questioner correct. |
| 42 | D | 06-peers.md Part 2A / Part 1 Q4 | Varroc receivables discounting facility (about Rs 700 to 750 Cr at about 7%, VARROC Nov2025 p.13) is relevant context B06 did not surface; omission changes no verdict. |

## Withdrawn and resolved (Verifier A source fidelity)

| Item | Original finding | Disposition | Anchor |
|---|---|---|---|
| TVS Educational Society apprentice stipend growth | Pass 1 MAJOR, source_fidelity true: +24.4% against the claimed +26.7% | WITHDRAWN by Verifier A on re-invocation. It had conflated the FY25 combined line (2,458 lakh = reimbursement 54 + stipend 2,414) with the stipend only line. Correct figure +26.7%: (3,059 − 2,414) / 2,414 = 26.72%. FLAG CLEARED. The upstream figure was right. | AR2026 Note 42.2, standalone p.224 ("Stipend to apprentices 3,059 2,414") |
| FY26 working capital days | Pass 1 MAJOR, source_fidelity true | RETAINED as a COMPANY ANOMALY (row 3 above). GATE HELD: all three figures are real and traceable; the contradiction is inside the company's filings. | AR2026 p.9; Q4FY26 deck p.19; Q1FY27 deck p.18; 01-gate0.md L167-169 |

Full record: runs/indnippon-2026-09-10/outputs/final/verifier-disagreement-log.md.

## Open cross verifier conflicts (carried unresolved)

| Item | Verifier B | Verifier A | Disposition |
|---|---|---|---|
| FY26 audited basis EBITDA margin | CRITICAL, row 2 | Not examined; re-invocation spent | OPEN, first Halt 1 verification item |
| FY26 ROCE, deck 34.97% vs Note 51 17% | CRITICAL, row 1 | Not examined | OPEN, Halt 1 |
| Credibility grade | Would grade D | Not in scope | UNRESOLVED; B05 filed C; both carried |

## Verifier C phase 1 scope note

Valuation audit: rules_checked 0, PENDING PHASE 3. Expectation ledger and business understanding narrative checks: PENDING PHASE 3. Verifier C concurs that Gate 0 AVERAGE and EM MODEST stand; core recomputes 56 to 54 inside the same 40 to 59 band (B12c recomputed_decision comment).
