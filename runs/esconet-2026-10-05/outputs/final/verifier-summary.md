# ESCONET verifier summary (phase 1, run 2026-10-05)

Scope: phase 1 verifiers only. Verifier A run 2 (B12a.yaml), Verifier B (B12b.yaml), Verifier C run 2, Gate 0 and Emerging Moat half (B12c.yaml), Verifier D (B12d.yaml). The Verifier C valuation half is PENDING PHASE 3. Rows below restate what the verifiers wrote; no commentary is added.

## Confidence delta and acceptance rates

| Component | Value | Count | Source |
|---|---|---|---|
| numerical_acceptance | 97.0 | 452 clean of 466 checked; mandatory tier 215 of 215 (OR-32) | B12a run 2 |
| redflag_coverage | 90.9 | 10 of 11 material (6 full, 4 partial counted as caught, 1 missed); full catch basis 54.5 | B12b |
| framework_adherence | 94.7 | 72 of 76 rules (Gate 0 46 of 49; Emerging Moat 26 of 27) | B12c run 2 |
| peer_utilisation | 91.7 | 11 SUBSTANTIVE of 12 peer calls (block acceptance_rate prints 92) | B12d |
| framework_adherence, valuation half | PENDING PHASE 3 | 0 rules checked | B12c run 2 |
| overall | 90.9 | min of applicable components | set by redflag_coverage (B12b) |
| band | high confidence (90 or above) | | confidence.yaml |

Open reading for the operator (confidence.yaml): on the full catch basis Verifier B's rate is 54.5% (6 of 11). That is below 60% on a denominator of 4 or more, which would force REWORK under OR-29 and set overall at 54.5. The orchestrator used the block's stated rate and names the second basis for a Halt 1 ruling.

Verifier A identity check: no CRITICAL rows in run 1 or run 2; nothing struck (confidence.yaml).

## Remediation, run 1 to run 2

| Verifier | Run 1 | Run 2 |
|---|---|---|
| A | 369 checked; mandatory 118 of 118; 0 CRITICAL, 4 MAJOR, 7 MINOR; acceptance 93.5 | 466 checked; mandatory 215 of 215; 0 CRITICAL, 3 MAJOR, 7 MINOR; acceptance 97.0 |
| C (phase 1 half) | 66 of 72 rules; 1 CRITICAL (F1), 6 MINOR; acceptance 91.7 | 72 of 76 rules; 0 CRITICAL, 4 MINOR (N1 to N4); acceptance 94.7; rework_trigger false |
| Confidence overall | 90.9 (framework carried 1 CRITICAL) | 90.9 |

Verifier A run 1 rows and their run 2 status:

| Run 1 row | Severity | Run 2 status |
|---|---|---|
| 03-ardeep Phase 5D promoter basis (82.50% / 60.09% vs 89.18% / 64.94%) | MAJOR, source_fidelity | Carried, not re-audited; still stands |
| 04-bizmodel 2A top five suppliers 52.35% vs 53.15% | MAJOR, source_fidelity | Carried, not re-audited; still stands |
| 09-tam 5D ZeaCloud turnover 568.79 vs 534.43 Lakhs | MAJOR, source_fidelity | Carried, not re-audited; still stands |
| 01-gate0 results filing balance sheet p.15 and CFO p.16 | MAJOR, source_fidelity | SUPERSEDED: stage 1 run 2 cites [page 14] and [page 15], verified on the .txt markers |
| 01-gate0 AR FY25 p.110 folio | MINOR | SUPERSEDED: now [page 112] with folio 110 in brackets |
| 01-gate0 FY23 revenue and receivables basis | MINOR | SUPERSEDED: now labelled restated consolidated vs standalone; screener FY23 column rejected |
| 01-gate0 M3 net block includes goodwill | MINOR | SUPERSEDED: now labelled |
| 01-gate0 M6 Annexure III | MINOR | SUPERSEDED: now Annexure IV [page 72] |
| 06-peers Netweb FY26 PAT 2,058 mn page cite | MINOR, source_fidelity | Carried; still stands |
| 02-notes page cites | MINOR | Carried |
| 04-bizmodel 17.65 Lakhs standalone basis | MINOR | Carried |

Verifier C run 1 findings and their run 2 status:

| Run 1 | Severity | Run 2 status |
|---|---|---|
| F1 Gate 0 scored 4 years, LIMITED downgrade, AVOID | CRITICAL | RESOLVED: 6 years FY2021 to FY2026, no downgrade, A13 B5 C10 D17 E15, core 60, AVERAGE (DB4) |
| F2 FY23 ROE opening net worth | MINOR | RESOLVED for FY23; recurs at FY21 as N2 |
| F3 M8 distribution | MINOR | RESOLVED: M8 = 1 |
| F4 M11 under 6 years | MINOR | RESOLVED as raised; superseded by N1 |
| F5 YAML template | MINOR | RESOLVED |
| F6 D4 sensitivity disclosure | MINOR | RESOLVED |
| F7 Emerging Moat recount and evidence_mix | MINOR | RESOLVED: 12 documented (11 unique), 5 categories, mix 12/9/1 |

## Findings, sorted by severity

### CRITICAL

None open. The only CRITICAL in phase 1 (Verifier C run 1 F1) is resolved in run 2.

### MAJOR (6)

| # | Verifier | Location anchor | Note |
|---|---|---|---|
| 1 | A (carried run 1; source_fidelity true) | 03-ardeep.md Phase 5D shareholding table, rows "Promoter and group, pre-IPO" and "Post-IPO" | 82.50% / 60.09% are promoters only ("Total - A", PROSP p.21). Promoter and group is 89.18% pre issue and 64.94% post issue (PROSP p.21, p.35, p.182). Basis mislabelled. Gate 0 E2 uses 64.94% correctly. |
| 2 | A (carried run 1; source_fidelity true) | 04-bizmodel.md Section 2A, Supplier power row | Claimed 52.35% of FY23 purchases; PROSP p.31 and p.32 print 53.15% (4,044.52 of 7,610.30 Lakhs). Transposition; B07 cites 53.15% correctly. |
| 3 | A (carried run 1; source_fidelity true) | 09-tam.md Section 5D (ii) expansion levers | Claimed ZeaCloud turnover Rs 5.69 Cr (568.79 Lakhs). AOC-1 (AR26 p.69) prints 534.43 Lakhs = Rs 5.34 Cr. 568.79 is the parent's sale to ZeaCloud (AR26 p.118, p.147). |
| 4 | B (F1, missed) | B05 trigger #2 and 1C; B06 verified Q7 | NVIDIA allocation moat premise accepted; red flag missed. Reg 30 29 Apr 2026 l.36-50; AUG26 p.16 l.867; NETWEB Nov 2025 p.8 l.332-340. Action: drop allocation premise from trigger #2 until a filed allocation benefit appears. |
| 5 | B (F2) | B05 trigger #8, 1C, FLAG-GUIDANCE-INCONSISTENCY | Singapore classed as a committed growth trigger; 53 Cr period left NOT FOUND though filed. Q1BM p.10 l.407-415: Q1 revenue 5,332.02 Lakhs (45.8%, derived), net profit 29.67 (0.56%), total assets 67.09. Action: reclassify as revenue quality flag; show standalone and ex Singapore growth. |
| 6 | B (F3) | B06 analyst_note and FLAG-PEER-SPLIT-MARGIN-MECHANISM net read | Inventory build called small from the Q1 standalone change alone. AR26 p.132, p.134 (consolidated inventory 1,894.21 to 5,149.87 Lakhs); AUG26 p.12 l.665-668. Action: restore reading B to equal standing with reading C. |

### MINOR (24)

| # | Verifier | Location anchor | Note |
|---|---|---|---|
| 7 | A (carried run 1; source_fidelity true) | 06-peers.md Q3, NETWEB cash conversion "FY26 PAT Rs 2,058 mn (p.4)" | INR 2,058 mn is on [page 3] and [page 5] of the May 2026 transcript, not [page 4]. ANCHOR NOT FOUND for one figure in a derived 83% ratio; value correct. |
| 8 | A (carried run 1) | 02-notes-pass1.md and 02-notes.md page cites (Note 2.12 p.139; Other Income and Note 2.17 p.142; Note 14 p.116; Schedule III p.150) | Markers are [page 141], [page 143], [page 117-118], [page 151]. Values match; pagination convention slip. |
| 9 | A (carried run 1) | 04-bizmodel.md 4D question 5 and Contradictions: "17.65 Lakhs on statutory dues (AR26 p.115)" | 17.65 is standalone; consolidated Note 2.22 prints 18.59 (AR26 p.144). Unlabelled basis; decision impact nil. |
| 10 | A (run 2) | 01-gate0.md Section 1 and Section 3 WC days lines; B01 data_notes | FY21 printed components sum to 47.7, not 47.6; FY24 unrounded gives 58.4, not 58.5. Mixed rounding; no score moves. |
| 11 | A (run 2) | 01-gate0.md Section 10 item 1; B01 data_notes (Q1 FY27 standalone purchases 4,845.14, inventory change -518.50) | Unanchored but present: Results Q1 [page 4]. Add [page 4] to the cite. |
| 12 | A (run 2) | 01-gate0.md Section 10 item 4: FY27 guidance Rs 370-400 Cr | Unanchored; CRISIL rationale 2026-07-02 .txt line 26 prints it. Not scored. |
| 13 | A (run 2) | 01-gate0.md Block B trend line; B01 block_b_trend and FLAG-CASH cite | PAT 615.50 Lakhs sits on AR FY26 [page 133], not [page 134]; cumulative PAT cite omits prospectus [page 50], [page 192], AR FY25 [page 113]. Values correct. |
| 14 | B (F4) | B05 FLAG-CASH | "Strengthening operational cash flows" PR text and deck "inventory supports signed orders" contradicted by filings, not flagged. Action: add to FLAG-CASH; cash conversion stays INDETERMINATE. |
| 15 | B (F5) | B05 2D item 8; 1B order book row | Rs 500 Cr+ vision and Rs 100 Cr+ pipeline source (DECK25 p.19) missed; walkback not recorded. |
| 16 | B (F6) | B05 FLAG-MARGIN-BASIS; stage 3 input gap | Q1 other income 190.04 Lakhs vs 184.23 Lakhs forfeiture in the same quarter not raised as a flag; CFO framed income as core. Verify booking in H1 FY27 notes or FY27 AR. |
| 17 | B (F7) | B05 repeated_evasions rows 1 and 4 | "Deflected every time" overstated for the Jun 2025 leg (JUN25 p.7 l.400-402; p.9 l.504-511; p.11 l.628-633). Reclassify as answered 2025, withdrawn 2026. |
| 18 | B (F8) | B05 promise row 5 | Employee cost miss on a mixed basis; standalone 795.39 vs 557.04 Lakhs, +42.8% (AR26 p.103). Direction MISSED stands. |
| 19 | B (F9) | B05 promise row 12 | Standalone 29.2% gross used against a consolidated promise; Q1 consolidated gross 16.6% (Q1BM p.7, derived). PARTIAL stands. |
| 20 | B (F10) | B05/B06, not covered | Fluidech acquisition date misstated on the call (AUG26 p.9 l.510-511 vs AR26 p.69, 16 Apr 2025). |
| 21 | B (F11) | B05/B06, not covered | Future R&D capitalisation signalled by the CFO (AUG26 p.12 l.631-640). Add a tripwire. |
| 22 | B (F12) | B05/B06, not covered | CEO in the Sep 2025 deck absent from AR26 KMP; no cessation filing in corpus (DECK25 p.5; AR26 l.3056-3060). Ask in the Halt 1 extraction annex. |
| 23 | C (N1) | B01 M11, moat_score, grand_total | Six years meets the two window threshold: M11 5, not 3; moat_score 20, grand_total 80; classification unchanged. Rubric window definition needs an operator ruling (O2). |
| 24 | C (N2) | B01 ROE FY21, input_gaps, data_notes | FY21 opening net worth 278.57 Lakhs (PROSP [page 232] + [page 233]); ROE -44.0%; A3 unchanged. |
| 25 | C (N3) | B01 analyst_note; B07 6C (inherited) | Consistent FY22 window gives core 63, AVERAGE, not 55. One sided sensitivity; correct before the Halt 1 dossier or stage 13 quotes it. |
| 26 | C (N4) | B07 6E moat evolution map | B01 names M1, M4, M10, M11 (01-gate0.md line 162); Customer family existing column = M4 (3) + M10 (5). Premise false; run 1 audit missed it. |
| 27 | D | ORIENTTECH Q2 FY26 coverage map | Marked CITED-ONLY but cited four times with unique content (19.65% gov/PSU share, builder delay). Label understates use. |
| 28 | D | ORIENTTECH Q2 FY26; NETWEB Q1 FY27 page anchors | Orient 19.65% cited p.3, marker p.4 (line 125); Netweb "125 people in R&D" cited p.16, marker p.17 (line 679). Quotes exist. |
| 29 | D | RPTECH Q4 FY26 | Q4 sovereign driver claim and Q7 acceleration anchor omit RPTECH Q4 p.10 (data sovereignty push; funnel may not finalise; capital intensive, lower margin). Verdicts do not change. |
| 30 | D | NETWEB, RPTECH (Q7) | Q7 VERIFIED rests on two peers; Esconet's own Elite access is not tested and "no cancellations" rests on a text search. Closer to PARTIALLY VERIFIED on the full claim. |

Verifier D unused but relevant items (B12d): ORIENTTECH Q2 FY26 pre shock EBITDA baseline (Rs 21.96 Cr on Rs 272.80 Cr, 8.05% derived; [page 4] l.116-123, [page 5] l.160-162); RPTECH Q4 FY26 data sovereignty driver and funnel caveat ([page 10] l.396-405).

Verifier B pipeline flags not supported (all OVERSTATED, none invented): B06 "inventory build is small"; B06 Q7 as support for Esconet GPU allocation; B05 repeated_evasions rows 1 and 4. Promise delivery spot checks: 6 checked, 6 confirmed, 0 wrong. Credibility grade: Verifier B concurs lower, at the C/D boundary.

## Counts

| Verifier | CRITICAL | MAJOR | MINOR |
|---|---|---|---|
| A run 2 | 0 | 3 | 7 |
| B | 0 | 3 | 9 |
| C run 2 (phase 1 half) | 0 | 0 | 4 |
| D | 0 | 0 | 4 |
| Total | 0 | 6 | 24 |
