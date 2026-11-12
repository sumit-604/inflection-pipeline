# Verifier summary: Onward Technologies Ltd (ONWARDTEC), phase 1

Run onwardtec-2026-11-12, phase 1 lite. Verifier scope: A (numerical, run 1 over all eleven reports plus the re-check of Gate 0 run 2), B (red flags), C (Gate 0 and Emerging Moat only; the valuation half is pending phase 3), D (peers). Verifier A shadow: not run.

## Phase 1 confidence delta (outputs/blocks/confidence.yaml)

| Component | Value | Verifier block | Denominator |
|---|---|---|---|
| numerical_acceptance | 97.3 | B12a (run 1) | 375 numbers checked; mandatory 85 of 85; material universe 465; 5 false positives struck |
| numerical re-check (cycle 1) | 99 | B12a-recheck | 167 numbers checked; mandatory 163 of 163 |
| redflag_coverage | 72.7 | B12b | 8 of 11 MATERIAL caught in full (2 CRITICAL, 9 MAJOR); 90.9 if partials count; 32 independent flags listed |
| framework_adherence | 88.0 | B12c | 73 of 83 rules (Gate 0 48 of 56; Emerging Moat 25 of 27); audited B01 run 1 |
| peer_utilisation | 63.6 | B12d / B06 | 7 SUBSTANTIVE of 11 peer transcripts |
| overall | 63.6 | min | overall_set_by: peer_utilisation; not_applicable: none |
| band | 60 to 74 | | PROCEED verdicts downgrade one level |

Acceptance rates as filed by each verifier: A 97.3 (re-check 99); B 72.7; C 88.0; D 100.

Other verifier results:
- Verifier A identity check: 1 CRITICAL row, 0 struck. CONFIRMED CRITICAL; REWORK fired (OR-29).
- Verifier B: promise-delivery spot checks 6 of 6 confirmed, 0 wrong. Credibility grade: "concur: B holds on constant-currency delivery (Q2 +17.7% cc inside the raised band); the added candour items (selective-disclosure denial vs record, FX share unstated, AI 'shared before') put it at the bottom of the B band". Pipeline flags not supported: none.
- Verifier C: Gate 0 as applied (run 1) core 74, GOOD+; as written strict core 55, AVERAGE, DB1 and DB2 fire; uniform proxy core 77, GOOD+. Emerging Moat recomputed 12.4, MODEST (concur), boundary. Halt 1 open item: "Gate 0 classification spans AVERAGE (as written, corpus gaps) to GOOD+ (as applied); with the separating documents the band edges allow GOOD to EXCELLENT".
- Verifier D: 11 peer transcripts audited, 7 substantive confirmed, no substantive usage unsupported, all claims addressed, no verdict discipline fails.

## Remediation cycle record

- Cycles used: 1 of 1 (manifest remediation_cycles: 1). Verifier runs: A 2 (run 2 is the re-check inside the cycle), B 1, C 1, D 1.
- Trigger: Verifier A CRITICAL on Gate 0 E4, confirmed by the orchestrator at Annual_Report_2026.pdf p.87 (Note 26(a)(ii) prints Rs 394.68 lakhs; only 26(c) financial guarantees is Nil). REWORK fired (OR-29).
- Cycle 1 scope: stage 1 re-run against the Verifier A CRITICAL and Verifier C findings G0-F1 to G0-F9.
- Cycle 1 result: "Stage 1 re-run (B01 run 2: core 79, moat 21, GOOD+; E4 input corrected to 394.68 lakhs, score unchanged at 5). Verifier A re-check: 0 CRITICAL, 0 MAJOR, 1 MINOR; prior CRITICAL cleared at source. Stage 5 load-bearing anchor (B12a MAJOR) corrected p.4/p.8 -> p.3/p.9 by source re-read."
- Rework status: "CLEARED by cycle 1. No CONFIRMED CRITICAL stands; no verifier acceptance rate is below 60%."
- Not re-audited: Verifier C has not audited B01 run 2 (verifier cap; a re-run needs operator approval in inputs/operator-notes.md).
- Not edited: the Verifier A MINOR anchor slips in the 04, 05, 06, 07 and 09 reports. Corrected pages are in the table below.

Report key used in anchors: K1 = Concall_Jul_2026 (Q1 FY27); K2 = Concall_Oct_2026 (Q2 FY27); K3 = Concall_Jan_2026 (Q3 FY26); K4 = Concall_May_2026 (Q4 FY26); PRES = Investor_Presentation_1.pdf (Q2 FY27 deck). B01 line references in Verifier C rows point to the run 1 report.

## Findings, sorted by severity

### CRITICAL (1)

| # | Verifier | Location anchor | Note (verifier's words) | Status |
|---|---|---|---|---|
| 1 | A (run 1) | 01-gate0.md Block E, E4 (also B01-gate0.yaml E4 line) | Claimed "contingent liabilities Nil at 31 Mar 2026 (AR 2026 p.87 note 25a); 0% of net worth = 5". Source: "AR26 p.87 carries Note 26 (note 25 is EPS). Note 26(a)(ii) discloses a contingent liability of USD 4.20 lakhs (Rs 394.68 lakhs) for the former-employee suit against Onward Technologies Inc; that is 1.56% of equity 25,350.70 lakhs." "Scorecard input E4 is wrong and the note number is wrong." source_fidelity: true | CONFIRMED; corrected in B01 run 2 (E4 score unchanged at 5); cleared at source by B12a-recheck |

### MAJOR (8)

| # | Verifier | Location anchor | Note (verifier's words) | Status |
|---|---|---|---|---|
| 2 | A (run 1) | 05-concall.md Fact 1, R&D credit note anchor | Claimed "Rs 292.60 lakhs credit, R2 note 'consolidated p.4 and standalone p.8 of the results PDF'". Source: Results_Q2FY27_BoardOutcome_2026-10-16.pdf consolidated note on PDF p.3, standalone on PDF p.9; "Page 4 and page 8 do not contain it." "The figure 292.60 is correct". source_fidelity: true | Anchor corrected to p.3 / p.9 in 05-concall.md line 13 by orchestrator source re-read |
| 3 | B (F1) | K2 p.3, p.6, p.11; LTTS Oct p.4, p.8; Cyient Aug p.8 | "MISSED: FX share of reported growth never applied to the revenue basis; guide currency basis NOT FOUND." Q2 FY27 +22.4% reported vs +17.7% constant currency, about 4.7 pts FX | Open; carried to phase 2 |
| 4 | B (F2) | K3 p.15; K4 p.14, p.15 | "PARTIALLY CAUGHT: selective-disclosure flag under-weighted (B05 Low-Medium, 'no evidence'); two unrebutted analyst citations of a 10-12% range contradict the universal denial; re-grade Medium" | Open; carried to phase 2 |
| 5 | B (F3) | K2 p.3, p.4, p.5, p.13 | "PARTIALLY CAUGHT: Q2 revenue quality; H2-implied dip not linked to revenue booked ahead of delayed POs; add third reading to trigger 1 [INFERENCE]" | Open; carried to phase 2 |
| 6 | C (G0-F1) | B01 L6, L10, L13-16, L52; B01 blk data_notes (ROCE computed) | "ROCE on (Total assets - Other Liabilities)"; as written "current liabilities NOT FOUND FY17-FY24; A1, A2, A4, M3 = 0; Block A 2; DB1 fires (max GOOD); alone core 67, GOOD". "FY26 current liabilities 7,180.16 lakhs are on AR 2026 p.65" | Addressed in run 2 per its change table; not re-audited by C |
| 7 | C (G0-F2) | B01 L20-23; B01 blk data_notes (FCF is a PROXY) | "FCF proxy CFO + CFI"; as written "capex NOT FOUND; B2 = 0, B3 = 0; Block B 5; DB2 fires (max GOOD); alone core 67, GOOD" | Addressed in run 2 per its change table; not re-audited by C |
| 8 | C (G0-F3) | B01 L39, L73; B01 blk data_notes (E2) | "E2 5: 38.12% Mar 2024 (AR 2025 p.147) to 40.20% Sep 2026, +2.08pp over about 2.5 years"; as written "Sep 2023 holding NOT FOUND; E2 = 0" | Addressed in run 2 (E2 = 0); not re-audited by C |
| 9 | C (G0-F4) | B01 L58; B01 blk data_notes (M9) | "M9 0: proxy set aside as a cost-classification artifact"; as written "proxy 100% vs peer median 89.2% = +10.8pp, revenue CAGR 10.4%; M9 = 5". "the fix is an operator ruling" | Addressed in run 2 (M9 = 5); rule text is an operator ruling item; not re-audited by C |

### MINOR (32)

| # | Verifier | Location anchor | Note (verifier's words) | Corrected anchor or status |
|---|---|---|---|---|
| 10 | A (run 1) | 05-concall.md Fact 2 and Fact 3, top-25 share 88% | "Figure right, page off by one." Cited K4 p.3 | Concall_May_2026 PDF p.4 (and p.17) |
| 11 | A (run 1) | 05-concall.md 2A rows 1-2 and Fact 2 (K3 anchors) | "Quotes and figures correct; pages are the printed page numbers in places, not PDF pages." | Concall_Jan_2026 PDF p.8 (12% budgeting); PDF p.9 (about 3,000 employees at USD 100 million); PDF p.6 (USD 100 million = Rs 1,000 crores) |
| 12 | A (run 1) | 06-peers.md Q6 and Part 3 (Tata Technologies Q2 FY27 revenue) | "Figure right (also ties to TATATECH Data_Sheet quarterly Sales 1698.8); page off by one." Cited p.9 | TATATECH Oct 2026 call PDF p.10 (Rs 1,699 Cr); p.9 carries USD 178 million |
| 13 | A (run 1) | 04-bizmodel.md 3B Net cash row and 4B EV/EBITDA row | "Figure right; 03-ardeep.md cites p.10 correctly." Cited AR26 p.11 | AR26 PDF p.10 (and p.4 highlights) for Rs 127.3 Cr |
| 14 | A (run 1) | 07-emoat.md 4A and 2D (deck anchors) | "Content correct; page anchors off." Cited deck p.22 and p.2 | Deck PDF p.21 (regulatory assurance capabilities); PDF p.1 (city list), p.5 ("12+ Offices") |
| 15 | A (run 1) | 09-tam.md load-bearing fact 3 and 5B/risk rows | "Mixed citation: the 18.3% is carried through B04 and is correct, but the deck page cited does not hold it." Cited deck p.15 | 18.3% from AR26 Note 34 p.93 (9,965.52 / 54,385.24 lakhs); deck p.15 holds top 25 84% to 87% only |
| 16 | A (re-check) | 01-gate0.md run 2, load-bearing facts 2 and 4; data_notes (Mar 2021 promoter 61.71%) | "Not scored and not used in any block; carried unanchored from the Step-1 fact list. Immaterial to Gate 0." source_fidelity: false | 61.71% not present in inputs/ (zero hits); not used |
| 17 | B (F4) | K2 p.6; PRES p.11 | "Partly OVERSTATED: B05 red flag 1 tests a sequential margin claim against YoY offshore mix; QoQ mix 68% to 69%; YoY point stands" | |
| 18 | B (F5) | K3 p.16; K4 p.14; K2 p.12 | "B05 2E says no never-answered dodge while recording high-teens never answered; K2 utilisation non-answer not logged" | |
| 19 | B (F6) | K3 p.14, p.16 | "B05 says analysts did not ask on concentration; K3 had two unanswered concentration questions" | |
| 20 | B (F7) | K3 p.3, p.5, p.6, p.8, p.9, p.12, p.16; K1 p.7 | "B05 K3 anchors often use printed page (PDF page minus one), plus one K1 slip; no direction changes" | |
| 21 | B (F8) | Cyient Apr p.14; K4 p.17 | "B06 Q4 omits Cyient's 20-30% software-development compression statement; Onward software is 50% of revenue" | |
| 22 | B (F9) | K2 p.6; Tata Tech Oct p.3, p.9 | "B06 growth-claim flag mixes bases (Onward H1 INR vs Tata Tech Q2 cc; 22.1% is services only); conclusion holds on like basis" | |
| 23 | B (F10) | K4 p.16; PRES p.15 | "MISSED: 250 vs 145 starting client count, call vs deck" | |
| 24 | B (F11) | K4 p.3, p.4, p.13 | "MISSED: revenue-per-person claims do not reconcile" (Rs 8-9 lakh four years ago vs 15.3% CAGR at stable headcount, implies about Rs 12.4 lakh) | |
| 25 | B (F12) | K1 p.3, p.10 | "MISSED: Q1 FY27 QoQ framing over YoY PAT decline" | |
| 26 | B (F13) | K2 p.13 | "MISSED: Worli office purchase; related-party status NOT FOUND" | |
| 27 | B (F14) | K4 p.2; K1 p.2 | "MISSED: IR firm switch" (E&Y to Go India Advisors) | |
| 28 | B (F15) | K3 p.5, p.7 | "MISSED: Q3 FY26 one-time costs unsized" | |
| 29 | B (F16) | K4 p.3, p.6, p.16; K1 p.9 | "MISSED: self-description drift and gross-margin mislabel" | |
| 30 | C (G0-F5) | B01 blk data_notes (E1) | "39.54% is in 30-39.9 = 1; Block E 16, core 72, GOOD+ unchanged". "E1 sits 0.20pp above the 40.0 edge and the note hides it." | Note corrected in run 2; not re-audited by C |
| 31 | C (G0-F6) | B01 L52 | "on the 10-year median ROCE 14.79%, M3 = 1, moats 3, MODERATE, classification GOOD". "Operator ruling invited on the M3 year basis." | Year basis stated (FY26) in run 2; not re-audited by C |
| 32 | C (G0-F7) | B01 blk flags | "FLAG-GATE0 with reason 'No classification depressor: classification GOOD+'"; "trigger not met as applied" | Flag removed in run 2; not re-audited by C |
| 33 | C (G0-F8) | B01 blk block_b_trend | "CFO/PAT up 0.31x (rc) reads improving; receivable days read stable; two numbers, label matches one" | Run 2 label "improving" with one number; not re-audited by C |
| 34 | C (G0-F9) | B01 L76-91 | "report block carries 13 of 21 fields, then a pointer line"; "a reader of the report alone does not see them" | Run 2 report ends with the full 21-field block; not re-audited by C |
| 35 | C (EM-F1) | B07 L241-272; B07 blk flags FLAG-EM-THIN | "12.4 is 0.4 above 12.0; six single-step readings give NONE". "Carry MODEST as a boundary class; widen the FLAG-EM-THIN reason." | |
| 36 | C (EM-F2) | B07 L272; B07 blk analyst_note | Separator "moves B2 and C1, not G1 or R1"; "G1 separator is its own test (P07 L109-111): FY27 year-end net cash against FY27 capex and payouts (FY26 met it at 127.3 Cr; H1 FY27 97.1 Cr did not); R1 needs an operator ruling". "Wrong separator would enter the monitoring checklist." | |
| 37 | C (EM-F3) | B07 L185 | "I2 0, answered for C1 and B2 only"; "6 scored rows; F1, F2, G1, R1 unanswered; score stays 0". "No score effect." | |
| 38 | C (EM-F4) | B07 L58, L61, L64, L80-85; B07 blk capex_embedded_growth_pct | "on the committed DOC figure Rs 3.31 Cr (AR26 p.87 note 26b via B07 L61): 3.31 x 11.37 = 37.6 Cr, 6.9% of FY26 revenue (rc)". "Phase 3: stage 11 must not take 52.3% as a CAPACITY basis." | |
| 39 | D | CYIENT-Concall_Jun_2026_Transcript_2, PDF p.3-4 | "Cyient 26 May semiconductor call marked UNUSED with 'no ER&D demand content found'; it carries data-centre power demand statements at PDF p.3-4 (industry context for Q1)" | |
| 40 | D | TATATECH-Concall_Jan_2026_Transcript, .txt lines 459-464 | "Q7 net read states peer DSO range 78-102 days, but B06 evidence itself lists LTTS 112 (Q3 FY26) and Tata Tech 111 (Dec 2025); range understated, verdict VERIFIED unaffected" | |
| 41 | D | 06-peers.md, Tata Technologies Q3 FY26 and Q4 FY26 anchors | "Tata Tech Q3 FY26 and Q4 FY26 anchors cited by call, not PDF page (B06 stage notes admit this); not findable by page" | |

Counts: CRITICAL 1, MAJOR 8 (A 1, B 3, C 4), MINOR 32 (A 7: six in run 1 and one in the re-check; B 13; C 9; D 3). B12a run 1 lists six MINOR rows while its minor_count field reads 5; all six rows are shown as filed. Verifier B MISSED items F10 to F16 restate its "missed" list; they are not double counted.

## Verifier disagreement set (also in verifier-disagreement-log.md)

| Date | Run (ticker-date) | Number/claim | Verifier A verdict + anchor | Downstream step + its position | Disposition | Note |
|---|---|---|---|---|---|---|
| 2026-11-12 | onwardtec-2026-11-12 | Gate 0 E4 contingent liabilities Nil | CRITICAL MISMATCH; AR26 p.87 Note 26(a)(ii) Rs 394.68 lakhs | Stage 1 run 1: scored E4 on Nil (note 25a) | GATE HELD: forced REWORK; GATE HELD: figure corrected at source (correct anchor shown), cleared by remediation cycle 1 | Re-check B12a-recheck confirms |
| 2026-11-12 | onwardtec-2026-11-12 | R&D credit Rs 292.60 lakhs anchored to results p.4 / p.8 | MAJOR ANCHOR NOT FOUND; figure is on p.3 / p.9 | Stage 5: cited p.4 / p.8 | GATE HELD: figure corrected at source (correct anchor shown) | Orchestrator re-read the results PDF text |
