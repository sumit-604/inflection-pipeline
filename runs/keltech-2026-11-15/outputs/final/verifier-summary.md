# KELTECH (Keltech Energies Ltd, BSE 506528): verifier summary, phase 1, run 2026-11-15

Scope. Verifier A (numerical), Verifier B (red flags), Verifier D (peer coverage) and the Gate 0 and Emerging Moat portion of Verifier C (framework). Valuation framework adherence is PENDING PHASE 3: B10 and B11 were not produced, so the valuation half of Verifier C, the expectation ledger rules 13 to 14 and the business narrative rule 9 check have not run.

Units. Filing figures are in ₹ lakh and rating and screener figures in ₹ Cr, as each verifier wrote them.

## Phase 1 confidence delta

| Component | Score | Denominator and basis |
|---|---|---|
| numerical_acceptance (B12a) | 95 | About 300 numbers checked of about 560 material; mandatory tier 32 of 32 |
| redflag_coverage (B12b) | 78 | 7 of 9 material items (5 caught outright, 2 partially caught counted as already had). Strict count excluding partials 5 of 9 = 55.6%, below the 60% REWORK line; operator ruling open |
| framework_adherence (B12c) | 90.7 | Phase 1 portion only: 68 of 75 rules (Gate 0 44 of 46, emerging moat 24 of 29); valuation component PENDING PHASE 3 |
| peer_utilisation (B12d) | 100 | 12 of 12 peer transcripts confirmed substantive |
| overall | 78 | Set by redflag_coverage (B12b). Band 75 to 89, normal, note specifics |

| Verifier | Acceptance rate | CRITICAL | MAJOR | MINOR | Runs (verifier_runs) |
|---|---|---|---|---|---|
| A numerical (B12a) | 95 | 0 | 5 | 2 | 1 |
| B red flags (B12b) | 78 | 0 | 4 | 13 | 1 |
| C framework, phase 1 (B12c) | 90.7 | 0 | 3 | 4 | 1 |
| D peers (B12d) | 92 | 0 | 1 | 2 | 1 |
| Total | | 0 | 13 | 21 | |

REWORK triggers (confidence.yaml): Verifier A confirmed CRITICAL false; any acceptance rate below 60 on a denominator of 4 or more false; rework false. Verifier A identity check: 0 CRITICAL rows, nothing to test, nothing struck by the orchestrator. The verifier's own rule 5b self check struck 5 rows before reporting. Remediation cycles: 0. Mechanical reruns: Verifiers A, B and C stalled once with no output (harness stream watchdog) and were re-invoked; these are not counted. Verifier A shadow: not run in this session.

Source fidelity disposition. All 7 Verifier A findings carry source_fidelity: true. Disposition: GATE HELD, figure corrected at source (outputs/reports/ERRATA-verifier-corrections.md, F1 to F7). No Verifier A flag was cleared. No other disagreement exists.

## CRITICAL

None from any verifier.

## MAJOR

| Verifier | ID | Location anchor | Note | Source truth or correction |
|---|---|---|---|---|
| A | F1 | 05-concall.md s1C T2 row, s2D row 4, s3C item 3, YAML kill_signal (Q4 FY26 Explosives revenue and growth) | MISMATCH from garbled text twin; margin 4.66% unchanged at 2 dp | 12,355.58 lakh; +7.70% (Q4 FY26 audited results PDF p.10), not 12,365.58 and +7.8% |
| A | F2 | 05-concall.md s2A row 2, YAML promise_delivery and trigger 2; 04-bizmodel.md s3B and YAML must_track; 06-peers.md Q3 net read; 07-emoat.md s1C (H1 FY27 Explosives segment result and margin; 04 also H1 revenue) | MISMATCH from garbled twin; B05 trigger 2 confirm signal of 6.5% was set against the wrong base | Result 1,953.31 lakh; revenue 30,323.32 lakh; margin 6.44% (Q2 FY27 results PDF p.6), not 1,963.31 / 30,320.32 / 6.47% or 6.48% |
| A | F3 | 05-concall.md s1C margin table, s2A row 2, s2D, s4A trigger 3, YAML trigger 3; 06-peers.md s2B (Q2 FY27 EBITDA ex other income) | MISMATCH from garbled twin; 8% confirm signal still holds | Other income 209.80; EBITDA 1,309.51, 8.16%; H1 2,689.11, 7.82% (Q2 FY27 results PDF p.5), not 200.80 / 1,318.51, 8.21% / 2,698.11, 7.85% |
| A | F4 | 01-gate0.md method note (exceptional items) and block D line D2 (interest coverage) | ANCHOR NOT FOUND on a mandatory Gate 0 input; value is correct (scr 4.18 Cr ties) | 417.88 and 317.76 lakh sit at AR p.99 (P&L), p.27 (Board's report) and p.130 (Note 23), not "AR p.4" |
| A | F5 | 02-notes.md top findings rank 1, risks table, red_flags, questions, YAML FLAG-BANK-RETURNS (bank return gaps) | UNANCHORED basis label on the only RED finding; 03-ardeep.md already corrects it, 02 does not | AR p.118 Note 13: 19.2% to 30.3% (receivables 20.4%) are shares of the amount reported in the return; as a share of books 23.7% to 43.6% (receivables 25.6%) |
| B | F1 | B05; AR FY25 p.30; AR FY26 p.28 | Missed cross AR contradiction on FY25 Perlite volume (24,584 vs 18,704 MT); row 4 and 4C consistency rely on the FY26 figure | Carried as an open item and monitorable |
| B | F2 | B05, B06; AR FY26 CG p.58 note 2; p.63 | Missed: both executive directors took executive roles at an unnamed group company in April 2026 during the TNT build | Carried as an open item and monitorable |
| B | F3 | B06 (B05 contributing); AR FY26 p.29; CRISIL p.2; APOLLO Q4FY26 p.11 | TNT framed as merchant defence energetics against AR "Nitration Based Accessories", CRISIL "established clientele reduces demand risks", and Apollo's TNT licence "for industrial explosive requirements"; B06 Q4, FLAG-SECOND-INDIAN-TNT-LICENCE and cross peer hypothesis rest on the unproven reading | TNT end use unproven either way (errata) |
| B | F4 | B05; Q4 FY26 results pp.8, 10; Q2 FY27 p.6 | Q3 FY26 called a data gap though the Q4 FY26 filing prints it (Explosives 4.64%); four quarter margin fall from 9.00% (Q4 FY25) began before the March 2026 plant start; B05 reads a one quarter Q4 low | Q3 FY26 is not a data gap (errata) |
| C | C-G1 | B01; M3 capital efficiency, ROCE fixed formula (TA less CL) where computable | M3 should be 5 under the fixed ROCE formula on B01's own latest year basis (21.1%); moat score +2; class unchanged | Stated M3 = 3 on FY26 proxy ROCE 19.02%; recomputed M3 = 5 (43.03 / 203.72 = 21.1%, above 20%; FAT 4.54x, above 3x); B01 data note "no band moves" is wrong for M3 |
| C | C-G2 | B01; M5 scale, PEER DATA NEEDED scores 0 | M5 scored 1 on an incomplete peer set while marked PEER DATA NEEDED; rule gives 0; moat score -1; class unchanged | M5 = 0; one listed player census resolves M5 and M7. Net: moat 11 (stated 10), grand 64 (stated 63), core 53, AVERAGE, MODERATE, moats confirmed 2 |
| C | C-E1 | B07; evidence multiplier vs stated tier (rule 3), B07 weakest link convention | H2 multiplier 1.0 breaks B07's declared weakest link rule | H2 = LM 1 x 0.5 = 0.5; em_score 4.1 (stated 4.6); band NONE unchanged |
| D | 1 | 06-peers.md Q9; B06 verified[] entry Q9 | Q9 VERIFIED rests on APOLLO alone for IDL specifics; PREMEXPLN corroborates only the Coal India margin sub point; should be PARTIALLY VERIFIED (single peer) | Q9 reads PARTIALLY VERIFIED (errata) |

## MINOR

| Verifier | ID | Location anchor | Note | Source truth or correction |
|---|---|---|---|---|
| A | F6 | 03-ardeep.md Phase 2 Top 15 row 14 | ANCHOR NOT FOUND (one page off); number correct | Note 13(c) outstanding liabilities 2,695.09 lakh is at AR p.119, not p.120 |
| A | F7 | 06-peers.md Q6, Q7, Q9 and coverage map (four peer page anchors) | ANCHOR NOT FOUND (adjacent page); all four numbers exist and are quoted correctly | SOLARINDS Q2FY26 Rs 960 Cr p.4 (not p.3); SOLARINDS Q2FY27 Rs 17,568 Cr p.10 (not p.9); APOLLO Q4FY26 IDL about Rs 380 Cr p.9 (not p.10); PREMEXPLN Q1FY27 6% regular explosives p.9 |
| B | F5 | B05; AR FY26 p.29; Q4 FY26 outcome p.2 | "No company statement on timing since Feb 2026" contradicted by Board's Report (approved 27 May 2026) "to be commissioned fully in 2027"; pace arithmetic stands | |
| B | F6 | B05; AR Note 3; Note 13(a) p.117 | Red flag 6 overstated: AR notes name the TNT project and its Canara Bank loan; only cost and April 2027 are CRISIL only | |
| B | F7 | B05; AR FY26 p.55; AR FY25 p.58 | Promise rows 3 and 5 use carried forward MD&A text; row 3 tests a sentence against the year it reports (circular); outcome survives on FY25 AR p.58 | |
| B | F8 | B06; SOLARINDS Q4FY26 p.7 | 2B states Solar's 18-20% price rise as realised; it is the FY27 expected component of guided growth | |
| B | F9 | B06; CRISIL p.2 | Keltech rise and fall clauses marked NOT FOUND; CRISIL p.2 states a price escalation clause "up to some extent" (quoted in B05 3B) | |
| B | F10 | B06; APOLLO Q3FY26 p.14 | Apollo RPT resolution defeat called "not confirmed in the call"; management confirmed it | |
| B | F11 | B06; APOLLO Q4FY26 p.11 | FLAG-SECOND-INDIAN-TNT-LICENCE implication overstated: Apollo licence covers its industrial explosive requirements, so a shared merchant TNT window is not evidenced | |
| B | F12 | B05; Q4 FY26 p.9 note 3; announcements 2026-04-25, 2026-05-12 | Missed CESTAT order timing against the 24-25 Apr 2026 BSE price query; order date NOT FOUND, PENDING LIVE VERIFICATION | MAJOR if the order predates 24 Apr 2026 |
| B | F13 | B05; AR FY26 CG pp.77-78 | Settlement context omitted: MOFS under an arbitral tribunal of retired judges; AR states impact as "Change in the Promoter" | |
| B | F14 | B05; AR FY26 CG pp.60-71; AGM outcome p.2; corrigendum 2026-09-28 pp.1-2 | Missed governance and disclosure items: Audit Committee contradictions, BSE penalties Reg 17(1A)/23(9), AGM Q&A forum exists, 52 day voting corrigendum whose enclosed cover still carries the errors, "reaffirmed" vs "assigned" | |
| B | F15 | B05; Q4 FY26 p.12; Q2 FY27 p.8 | CFO headline includes bank deposit movements (+961.95 FY26, -318.30 H1 FY27); ex item H1 ratio 0.59x; INDETERMINATE cap stands | |
| B | F16 | B05; CRISIL p.2 | CRISIL liquidity decline (Rs 63 Cr to Rs 50 Cr cash and liquid investments, Mar to Sep 2025; 84% limit use) and Rs 400 Cr borrowing power left without a reading | |
| B | F17 | B05; Q2 FY27 p.5 | Missed H1 FY27 actuarial loss 197.86 lakh vs 23.78 for FY26, unexplained | |
| C | C-E2 | B07; I2 answered for each moat claimed in the scan | I2 question unanswered for 5 of 7 scored rows (B1, C2, E2, F2, H2); score unchanged at 0 | |
| C | C-E3 | B07; 2C historical fixed asset turnover carried to capex_embedded_growth_pct | capex_embedded_growth_pct carries spot year 122 (FY26 3.42x) not historical turnover 246 (FY23 to FY25 average 6.89x); both unreliable; phase 3 must not use as CAPACITY basis | |
| C | C-E4 | B07; catalysts_12m evidence_type per taxonomy | Catalysts 1 and 3 tagged documented for future disclosures; Pillar 3 must treat as checkpoints | Tag as inference or checkpoint |
| C | C-E5 | B07; report YAML equals block file | Report YAML vs block drift: analyst_note wording and merged optionality row (silo row 12 months vs 6 to 12 months) | Block is correct on analyst_note |
| D | 2 | SOLARINDS-Q2FY27 line 393; PREMEXPLN-Q1FY27 line 325 | Page drift: SOLARINDS Q2FY27 Rs 17,568 Cr defence order book is p.10 not p.9; PREMEXPLN Q1FY27 94/6 order split precedes p.10 | Same anchors as Verifier A F7 |
| D | 3 | APOLLO-Q4FY26 lines 724-740 (transcript p.18) | Unused APOLLO Q4FY26 p.18 statements (negative EBITDA, captive buying, small supplier base) | IDL "presently negative EBITDA" (May 2026); Apollo buys defence explosive fill from outsourcers and will keep captive demand; defence explosive supplier base "pretty small" |

## Verifier B material item accounting (basis of the 78 and the 55.6%)

| Item | Severity | Status |
|---|---|---|
| C1 FY25 Perlite volume stated two ways (AR FY2024-25 p.30; AR FY2025-26 p.28; Note 28 p.137) | MAJOR | MISSED |
| C2 MD and Vice-Chairman group executive roles April 2026 (AR FY26 CG p.58 note 2; p.63; CRISIL p.2) | MAJOR | MISSED |
| C3 TNT end use (AR FY26 p.29; CRISIL p.2; APOLLO Q4FY26 p.11) | MAJOR | PARTIALLY CAUGHT |
| C4 Explosives margin four quarter trough (Q4 FY26 p.10; Q2 FY27 p.6; AR FY26 p.28; AR FY25 p.29; SOLARINDS Q4FY26 pp.7, 9) | MAJOR | PARTIALLY CAUGHT |
| C5 TNT spend pace (Q2 FY27 pp.7-8; CRISIL pp.2-3; AR FY26 p.29) | MAJOR | CAUGHT |
| C19 AR vs filing segment basis (AR Note 28 p.137; Q4 FY26 p.10) | MAJOR | CAUGHT |
| C20 H1 FY27 CFO 0.39x PAT (Q2 FY27 pp.8-9) | MAJOR | CAUGHT |
| P1 Peer energetics projects slipped (PREMEXPLN Q2FY26 p.8 to Q1FY27 p.8; APOLLO Q3FY26 p.6; APOLLO Q2FY27 p.4) | MAJOR | CAUGHT |
| P2 PSU bulk L1 thin or negative margin (PREMEXPLN Q1FY27 p.11; Q3FY26 p.13; SOLARINDS Q2FY26 p.15) | MAJOR | CAUGHT |

Promise delivery spot checks: 5 checked, 5 confirmed, 0 wrong. Credibility grade: Verifier B concurs with C.

## Verifier coverage notes (as written)

- A: Mandatory tier = Gate 0 scored inputs (A1 to A4, B1 to B4, C1 to C4, D1 to D4, E1 to E4, M1 to M12), 32 of 32 checked. No verdict card or Section 1B pillar input exists in stage 1 to 9 reports. Not checked: web sourced figures in stages 8 and 9 and the ICRA CCPL rationale, none of which is a source PDF in Verifier A's inputs; Q1 FY27 OCR pages only through figures repeated in Q2 FY27; about 25 of about 150 peer transcript quotes located; stage 3 phases 5 to 6 sampled. F1 to F3 digits were read from the PDF page images; every other Q2 and Q4 figure checked tied.
- B: 9 material of 30 listed (22 company, 8 peer). Peer read targeted (15 B06 anchors verified in full, term search across all 12), not a full re-read. pipeline_flags_not_supported: none.
- C: Gate 0 46 rules, 44 passed; emerging moat 29 rules, 24 passed; rule 8 Categories 21 and 22 present, I1 0, I2 0, rework_stage7 false. Valuation 0 rules checked, pending phase 3.
- D: 12 peers audited, 12 substantive confirmed, none unsupported; claims_all_addressed true.
