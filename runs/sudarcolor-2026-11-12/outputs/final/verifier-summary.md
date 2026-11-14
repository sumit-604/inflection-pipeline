# SUDARCOLOR verifier summary, phase 1

Sudarshan Colorants India Ltd. Run 2026-11-12. Phase 1 scope: Verifiers A, B and D in full; Verifier C on Gate 0 and Emerging Moat only (valuation half PENDING PHASE 3). Each verifier ran once (verifier_runs A 1, B 1, C 1, D 1; remediation_cycles 0). Verifier A shadow not run. All figures in ₹ Cr unless the source says otherwise.

## Confidence delta (phase 1)

| Component | Value | Source | Basis |
|---|---|---|---|
| numerical_acceptance | 95 | B12a | 0 CRITICAL, 7 MAJOR, 4 MINOR; mandatory tier 35 of 35 checked (OR-32); 250 numbers checked of about 480 material; 3 false positives struck at self-check |
| redflag_coverage | 69 | B12b | 16 material found, 11 caught (6 full, 5 partial); strict full catch 6 of 16 = 37.5% |
| framework_adherence | 77.8 | B12c | 35 of 45 rules pass (Gate 0 17 of 22, Emerging Moat 18 of 23); valuation half PENDING PHASE 3 |
| peer_utilisation | 81.8 | B12d | 9 of 11 peer calls SUBSTANTIVE (2 CITED-ONLY, older than 12 months) |
| overall | 69 | confidence.yaml | set by redflag_coverage (Verifier B); band 60-74, PROCEED verdicts downgrade one level |

Acceptance rates: A 95, B 69, C 77.8, D 100. REWORK trigger (OR-29): NOT FIRED. No CONFIRMED Verifier A CRITICAL; all rates at or above 60 on denominators of 4 or more.

Finding counts: CRITICAL 0. MAJOR 18 (A 7, B 9, C 2, D 0). MINOR 28 (A 4, B 16, C 8, D 0).

## CRITICAL

None. No verifier logged a CRITICAL finding.

## MAJOR

| # | Verifier | ID | Location anchor | Finding (verifier's note) | Source fidelity |
|---|---|---|---|---|---|
| 1 | A | A-1 (M2) | 01-gate0.md Block F M2 (line 50); B01 data_notes; 04-bizmodel.md lines 81-82, 140, 287, 323; B04 lines 18, 54 | Claimed peer FY26 EBITDA margins SUDARSCHEM 9.63%, MOL 11.88%, median 9.63%. Source: SUDARSCHEM 6.16% (603.3 / 9787.2), MOL 8.17% (177.56 / 2173.96), ASAHISONG 9.31%; median 8.17%. The reported figures reproduce only with the Change in Inventory line added with the wrong sign. Company 7.42% vs 8.17% is inside the +/-2pp band, so M2 scores 1, not 0. MAJOR under rule 5; CRITICAL only if Gate 0 inputs are ruled verdict card inputs. Source: SUDARSCHEM and MOL Data_Sheet.csv, FY26. | true |
| 2 | A | A-2 (M9) | 01-gate0.md Block F M9 (line 57); B01 data_notes; 04-bizmodel.md lines 45, 139, 253, 287, 321; B04 lines 18, 52 | Claimed peer gross margin median 42.71% vs company 39.26%. Source: SUDARSCHEM 49.20%, MOL 39.00%, ASAHISONG 33.94%; median 39.00%. Company 39.26% is correct and sits 0.26pp above. M9 scores 1, not 0. | true |
| 3 | A | A-3 (M1) | 01-gate0.md Block F line 48 | Claimed FY17 EBITDA margin 7.06%. Source: 6.84% (67.13 / 980.98), ties to PBT 36.29 (screener-Data_Sheet.csv, FY17). FY26 7.42% is correct. M1 stays 0. Same sign error. | true |
| 4 | A | A-4 (H1 PBT) | 08-promoter.md line 146; B08 line 32; 04-bizmodel.md line 175; 05-concall.md line 43 | Claimed H1 FY27 PBT 59.87 and operating EBITDA 60.27. Source: PBT 59.67 on the PDF image (Results_Q2FY27_Sep2026.pdf p.3); .txt layer misreads it. Operating EBITDA 60.07, margin 12.2% unchanged. No conclusion moves. | true |
| 5 | A | A-5 (OCF release) | 02-notes.md Top 15 rank 4; B02 FLAG-CASH, top_findings rank 4, red_flags | Claimed 24.76 release of government balances, OCF ex release 9.48. Source: 24.76 is a three-line sum (28.96 + 2.52 - 6.72, AR FY26 p.76); government balances alone net 20.53 (Notes 8, 14 pp.83, 85); OCF ex 20.53 = 13.71. | true |
| 6 | A | A-6 (share count) | 08-promoter.md Sections 1B, 3B; reconciliation row 2 | Claimed 2,30,81,978 shares. Source: 2,30,81,798 (AR FY26 p.66; Note 15 p.86; Note 36 p.90; screener sheet). Digit transposition; derived per-share figure unaffected at two decimals. | true |
| 7 | A | A-7 (institutional) | 08-promoter.md Section 6D | Claimed institutional holding fell to 0.70%. Source: 0.71% (0.51 + 0.20; screener-shareholding-2026-11-12.md, Dec 2025). 11.38% is right. | true |
| 8 | B | B-01 | AR FY25 pp.9, 10, 43, 82; AR FY26 pp.8-10 | MISSED. Three letter numbers do not reconcile with filed accounts: FY25 revenue "Rs 779 Crore" vs 825.06; domestic +5% vs +3.9%; renewables "delivered" vs FY25 BRSR Roha 57%, Cuddalore 40%, target over 65% vs 58%. Fix: B05 2B/2C letter numbers table; weigh in credibility. | n/a |
| 9 | B | B-02 | AR FY26 Note 40 pp.92-93; p.9; Results Q4 FY26 p.3 | MISSED. Group purchases 159.15 vs 80.72 (derived) plus group service charges 9.49 and royalty 1.61, against a "procurement leverage" claim while gross margin fell 42.2% to 39.3%. Pipeline tests only sales side transfer pricing. Fix: B05 2D, B06 Claim 5; name the H1 FY27 Reg 23 purchase split. | n/a |
| 10 | B | B-03 | Results Q2 FY27 pp.3-4; SUDARSCHEM Aug 2026 p.4 of 14 | MISSED. H1 FY27 margin includes inventory build absorption (FG/WIP/SIT build 44.66 vs 25.67); the parent strips 18 Cr from acquired group Q1 FY27 EBITDA in its own metric. SUDARCOLOR absorbed overhead NOT FOUND. Fix: B05 row 2 and trigger 2 "Delivered (interim), quality unverified". | n/a |
| 11 | B | B-04 | SUDARSCHEM Nov 2025 pp.3-5; Feb 2026 pp.7, 11; May 2026 p.3; Aug 2026 p.5 | MISSED. Shared Chairman's guidance record: two consecutive FY26 walkbacks (EUR 35m to 25-30m; then "materially deteriorated"), then a Q4 FY26 beat and a strong Q1 FY27. Fix: B06 parent guidance vs delivery table, fed to the credibility grade. | n/a |
| 12 | B | B-05 | MOL Nov 2026 pp.3, 7-8 of 11; MOL Aug 2026 p.2 of 16; B06 Key finding 3, Claim 1, 2A | MISSED/OVERSTATED. MOL Q2 FY27 pigment about +40% YoY revenue, +13% YoY production; production 3,233 to 4,252 MT QoQ. B06 says "no peer parallel". Fix: restate; the YoY size has a peer parallel built on base plus price pass through. | n/a |
| 13 | B | B-06 | Results Q4 FY26 pp.1, 7, 13; AR FY26 Note 40 pp.92-93; SUDARSCHEM call management pages; announcement 1-Sep-2026 Annexure B | PARTIALLY CAUGHT. Interim CFO Natu is the SUDARSCHEM CFO; Chairman Rathi is the SUDARSCHEM CMD; director Mukhopadhyay is a SUDARSCHEM director; ex-director Velankar is SUDARSCHEM General Counsel; FY26 close ran with no CFO. Fix: reclassify B05 red flag 5 to a related party control flag. | n/a |
| 14 | B | B-07 | SUDARSCHEM Nov 2025 pp.10-11; AR FY26 Note 40 p.93; AR FY26 p.17 | PARTIALLY CAUGHT. Group allocation moves volume both ways: AZO into Roha, and US-bound products to Europe and Mexico for tariffs, which fits USA SLO 77.42 to 20.99 [INFERENCE]. Fix: B06 Claim 4. | n/a |
| 15 | B | B-08 | Reg 10(7) report 19-Oct-2026 pp.1-3; SAST 29(2) 1-Oct-2026; SUDARSCHEM Aug 2026 p.9; Feb 2026 p.8; AR FY26 Note 40 p.92 | PARTIALLY CAUGHT. The 1-Oct-2026 transfer is tranche one of a stated plan to hold the full 70% directly; residual 54.36% offshore [INFERENCE: no notice, price or date filed]; the cash-to-Europe question went unanswered. Fix: keep neutral on control, add the staged plan and cash path tripwire. | n/a |
| 16 | B | B-09 | AR FY25 p.10; AR FY26 p.8; B05 red_flags[3], promise row 8 | NOT SUPPORTED. B05 scores FY25 "growth momentum" as a failed FY26 promise; the text describes FY25 (+4.3%). Fix: drop row 8; recount 2 delivered, 4 partial, 2 missed after rows 3, 8 and 9 are reclassified. | n/a |
| 17 | C | C-G02 | B01 Block A; 01-gate0.md ROCE; DB3 | ROCE EBIT taken as PBT + interest - other income; the fixed formula is PBT + interest, screener ROCE first. Recomputed: median 10.2%, Block A 6, DB3 off, core 61 (62 with C-G09 fix), GOOD. Fixed TA - CL median NOT FOUND; 10.2% sits 0.2pp over the line. Operator question Q1. | n/a |
| 18 | C | C-G09 | B01 Block B (B2, B3, B4) | B2/B3 scored on FY24-FY26, B4 zeroed for missing FY17 payables. Block B 15 fits neither consistent reading: 16 (available window, B4 = 1) or 5 (NOT FOUND = 0; DB2 fires). Reading 1 is better evidenced. Operator question Q2. | n/a |

## MINOR

| # | Verifier | ID | Location anchor | Finding (verifier's note) | Source fidelity |
|---|---|---|---|---|---|
| 19 | A | A-8 | 08-promoter.md reconciliation row 2, analyst_note; B08 input_gaps | CMP "about Rs 386" anchored to the brief; the brief says Rs 381 (market cap 879); Rs 385.5 (market cap 885.41) is in screener-Data_Sheet.csv. Wrong artefact anchor. | true |
| 20 | A | A-9 | 06-peers.md Key finding line 15, Claim 8 | Mukhopadhyay "nothing further to that" is printed page 9 of 14, not p.10. Quote exists verbatim. | true |
| 21 | A | A-10 | 01-gate0.md Block B line 24 | FY24/FY25 payables anchored "AR FY25 p.65 area"; correct anchor is AR FY25 p.64 balance sheet and Note 19 p.74. Values right. | true |
| 22 | A | A-11 | 08-promoter.md Section 1C | Sambit Roy appointment date left UNVERIFIED; AR FY26 p.29 Annexure C note b prints "effective November 25, 2024". | false |
| 23 | B | B-10 | AR FY26 p.9; Results Q2 FY27 note 4 p.6; SUDARSCHEM Feb 2026 p.12; May 2026 p.10 | PARTIALLY CAUGHT. AR FY26 Chairman letter names AZO products moved from Frankfurt to Roha; SUDARCOLOR is the Clariant legacy entity, so B06's plant [INFERENCE] is resolvable from the corpus. | n/a |
| 24 | B | B-11 | SUDARSCHEM May 2026 pp.8, 10; Aug 2026 pp.6-8 | PARTIALLY CAUGHT. Parent did not quantify volume vs price/restock for the acquired group; record as a non-answer pattern. | n/a |
| 25 | B | B-12 | AR FY25 p.43; AR FY26 p.10 | SPOT CHECK WRONG. B05 row 3 "renewables delivered" has no earlier promise; FY25 BRSR shows Roha 57%, Cuddalore 40%. Remove or score Missed. | n/a |
| 26 | B | B-13 | AR FY26 p.9; AR FY25 p.10 | SPOT CHECK BASIS. B05 row 4 says "no total"; AR FY26 p.9 prints 58% vs FY25 target over 65%. | n/a |
| 27 | B | B-14 | AR FY26 p.10; Notes 40-41 pp.93-94 | MISCLASSIFIED. "Outside the US, markets grew 7%" is past tense, not a promise; move to the letter numbers table. | n/a |
| 28 | B | B-15 | Reg 10(7) report 19-Oct-2026 pp.1-3; SAST 29(2) 1-Oct-2026 p.2 | OVERSTATED. B06 FLAG-STAKE-QUANTUM-MISMATCH: 70% is HLD1 36.56% + HLD2 17.80% + Europe B.V. 15.89%; the Reg 10(5) notice covered 15.89% only. Restate as a staged plan, not a mismatch. | n/a |
| 29 | B | B-16 | SUDARSCHEM Aug 2026 p.4 | OVERSTATED. B06 FLAG-WC-GROUP-DIRECTION: the parent said it raised subsidiary inventories, so the build fits stated group policy. | n/a |
| 30 | B | B-17 | SUDARSCHEM Aug 2026 p.7; MOL Nov 2026 p.3 | MISATTRIBUTED. "50%+ gross margin" was a question on One Sudarshan 54%; MOL pigment margin fell QoQ 12.1% to about 10%, so "peers held or raised margins" holds YoY only. | n/a |
| 31 | B | B-18 | MOL May 2026 pp.10-11; MOL Aug 2026 | CONTEXT. MOL "completely gone" refers to US and South American end markets (agro heavy); swap to the Aug 2026 quote. | n/a |
| 32 | B | B-19 | Reg 10(7) report 19-Oct-2026 p.3 | CONTEXT. Rs 411 sits 4.95% above the 60-day VWAP Rs 391.62 under the Reg 10(1)(a)(iii) cap; the gap to 602.03 is market fall, not a parent valuation view. | n/a |
| 33 | B | B-20 | SUDARSCHEM Nov 2025 pp.9-10; Feb 2026 p.13; Aug 2026 p.11 | MISSED. Parent offline deferrals, including a reported vs presentation number discrepancy. | n/a |
| 34 | B | B-21 | SUDARSCHEM May 2026 pp.4, 9 | MISSED. Parent Q4 FY26 EBITDA 73 Cr includes a one-time 37 Cr PPA credit; non-GAAP business EBITDA. | n/a |
| 35 | B | B-22 | SUDARSCHEM Feb 2026 p.3; May 2026 p.3; Aug 2026 p.3 | MISSED. ONE SAP date drift, "by December 26" to "this financial year". | n/a |
| 36 | B | B-23 | Results Q4 FY26 note 10 p.7 | MISSED. Airoli unauthorised asset transfer (legacy) volunteered in the results filing. | n/a |
| 37 | B | B-24 | Results Q4 FY26 note 9 p.7 | MISSED. Labour code exceptional 12.80 in Q3 FY26 revised to 4.49 net. | n/a |
| 38 | B | B-25 | Results Q4 FY26 p.3 | MISSED. Q4 FY26 operating EBITDA 4.43 on 211.10 (2.1%, derived) vs 17.80 (8.1%) in Q4 FY25, unaddressed in letters. | n/a |
| 39 | C | C-G13 | B01 Block F M8 | M8 reason "not quantified" names the band 1 condition but scores 0; moat score 0 to 1, grand total 60 to 61, class NONE unchanged. PEER DATA NEEDED tag on M8 is wrong. | n/a |
| 40 | C | C-G19 | B01 deal_breakers; 01-gate0.md line 65 | Block omits DB1 (Block A 5 < 8, max GOOD, non-binding); report says "no cap" where DB1 still applies. Presentational. | n/a |
| 41 | C | C-G21 | B01 C1/C2, D2, D3, M3, M9, M11, E2 | Gate 0 scorecard inputs with no inline anchor (OR-32 mandatory tier). Existence is Verifier A's call. | n/a |
| 42 | C | C-E03 | B07 1A NIR row; E2 line | Two AR FY25 citations carry no page; neither item is scored. | n/a |
| 43 | C | C-E04 | B07 B1 | B1 labelled NO EVIDENCE FOUND while quoting a management claim (AR FY26 p.17); matrix floor gives EM 10.6, class NONE unchanged. Operator question Q3. | n/a |
| 44 | C | C-E11b | B07 I2 | I2 answered once for the whole business, not per claimed moat; H2 is the row that matters. I2 stays 0. | n/a |
| 45 | C | C-E13 | B07 completionist recount | Recount credits R1 "NIR launch", which Section 4 does not list; 8 items across 5 categories as written. No score effect. | n/a |
| 46 | C | C-E16 | B07 1C, 2A, Section 3, Section 5 | Table schemas short of the text (missing columns; zero rows collapsed). Presentational. | n/a |

## Verifier B spot checks and credibility

- Promise delivery spot checks: 5 checked, 3 confirmed, 2 wrong (B-09, B-12).
- Credibility grade: concur C. "three more letter numbers that do not reconcile and a renewables claim the FY25 BRSR contradicts hold it at the low end of C; the one live forward promise (return to growth, H1 FY27 +25.0%, Results Q2 FY27 p.3) keeps it off D."
- Coverage basis: 16 material (0 CRITICAL, 16 MAJOR) of 24 listed; 11 found (6 fully, 5 partially, partial counted as found per its rule 3); strict full catch 6 of 16 = 37.5%.

## Verifier C recomputes (phase 1 scope)

- Gate 0: "GOOD under the fixed EBIT definition with the available-window reading (core 62, DB1 non-binding, DB3 off). AVERAGE only under the strict NOT-FOUND-equals-0 reading (core 50 or 51, DB2 fires), which the stage did not apply. Stage value AVERAGE."
- Emerging Moat: "9.9 concur on the stated rows; 10.6 with the B1 matrix floor; NONE either way (band edge 12)."
- Propagation: if C-G02 is upheld under the available window reading, the combined assessment moves from AVERAGE to GOOD and FLAG-GATE0 lapses. FLAG-CASH does not depend on the class.
- Operator questions: Q1 (Gate 0 EBIT for cash rich names), Q2 (missing data inside the scored window), Q3 (Emerging Moat score for a claim that documented data contradicts).

## Verifier D (peer coverage)

Zero findings. 11 peers audited; 9 of 9 SUBSTANTIVE rows confirmed with findable citations; 2 CITED-ONLY rows (ASAHISONG Q2 FY25, Q4 FY25) confirmed, use level fair. No verdict upgraded from silence; all 8 peer questions addressed (claims_all_addressed true). Acceptance 100.

| Peer / call | Usage | Result |
|---|---|---|
| SUDARSCHEM Q2 FY26 (Nov 2025) | SUBSTANTIVE | Confirmed |
| SUDARSCHEM Q3 FY26 (Feb 2026) | SUBSTANTIVE | Confirmed |
| SUDARSCHEM Q4 FY26 (May 2026 call) | SUBSTANTIVE | Confirmed |
| SUDARSCHEM Q1 FY27 (Aug 2026 call) | SUBSTANTIVE | Confirmed |
| MOL Q3 FY26 (Feb 2026) | SUBSTANTIVE | Confirmed |
| MOL Q4 FY26 (May 2026) | SUBSTANTIVE | Confirmed |
| MOL Q1 FY27 (Jul 2026 call) | SUBSTANTIVE | Confirmed |
| MOL Q2 FY27 (Nov 2026) | SUBSTANTIVE | Confirmed |
| ASAHISONG Q2 FY25 | CITED-ONLY | Confirmed; use level fair |
| ASAHISONG Q4 FY25 | CITED-ONLY | Confirmed; use level fair |
| ASAHISONG Q4 FY26 | SUBSTANTIVE | Confirmed on sample |

## Coverage notes (verifiers' own)

- Verifier A: mandatory tier 35 of 35 checked; sample tier about 215 of about 480 material numbers in order of materiality. Not checked: pass 1 per-note detail beyond the Top 15, most peer quotes beyond ten, BRSR energy lines, FY25 AR comparatives other than capex and payables. Web sourced figures in stages 8 and 9 have no corpus PDF and were not audited. Three scanned announcement PDFs (6D1F3240, A16C6814, C1DC7FB5 pp.1-5) were not read.
- Verifier B: no-concall mode; main company sources are AR FY25, AR FY26, three results filings and seven announcements, with the scanned pages of four filings (12 pages) read as images; 11 peer transcripts read.
- Verifier C: valuation rules (4, 6, 7, 11-15) and rules 9-10 not run; pending phase 3 and /finalize.
