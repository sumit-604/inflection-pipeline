# AEQUS - Aequs Ltd
## Sources read
- companies/AEQUS.md (origin/main, on_main yes)
- runs/aequs-2026-09-05/manifest.yaml, outputs/final/gate-recommendation.md, outputs/reports/05-concall.md (grep), step1-business-brief.md (grep) (156 branches incl. origin/claude/aequs-step-one-42trpa; on_main yes)
- runs/aequs-q2fy27/operator-brief.md, notion-payload.md, work/run-log.md, work/review_aequs_q2fy27.md (grep), work/notion-page-snapshot-2026-10-28.md (lines 25-144, 636-685, grep) (10 branches incl. origin/claude/qr-aequs-q2fy27-f2613d; on_main no)
- retro/2026-11/excerpts/sessions/AEQUS.md (first 120 lines)
- retro/2026-11/excerpts/local/AEQUS.md (first 80 lines, grep)

## Company-level facts
- board: NOT FOUND. Nearest: "Rs 413.92 cr across 33 anchor funds at Rs 124 a share, 08-Dec-2025. MEDIA REPORTED." - runs/aequs-2026-09-05/outputs/final/gate-recommendation.md:364-365
- reporting: quarterly. "Q1 FY27 Reg 33 filing with BSR limited review, unmodified opinion, obtained." - runs/aequs-q2fy27/work/notion-page-snapshot-2026-10-28.md:66
- archetype: `sector_cap_row: "Defence / strategic"` - runs/aequs-2026-09-05/manifest.yaml:8; "Classification: AVOID. Moat class MODERATE (B01)." - gate-recommendation.md:175; "Aerospace | 81% | Build-to-spec component maker" - notion-page-snapshot-2026-10-28.md:39
- first analysis: "# Aequs — Q1FY27 Concall (July 29, 2026)" in analysis\.workspace\2026-08-04_evening_concalls\Aequs.md - retro/2026-11/excerpts/local/AEQUS.md:24-26; pipeline run "run_date: 2026-09-05" - manifest.yaml:5
- verdict: "Halt 1 decision (KILL/SHALLOW/PROCEED): pending operator." - companies/AEQUS.md:32; gate file line 1 "# REWORK"; "REWORK judges this analysis, not this company." - gate-recommendation.md:20

## Q4 FY26
- base case: NOT FOUND. "Stages 10 and 11 did not run in this phase." - gate-recommendation.md:5
- guidance: "| Formal FY guidance | None given (\"not at this time\") | First full guidance set issued | Reaffirmed \"unchanged from May\" | New, then held |" - runs/aequs-2026-09-05/outputs/reports/05-concall.md:93
- catalysts: NOT FOUND
- actuals: "| Revenue from operations (R-L375) | 281.59 | 395.55 | 409.08 | 537.16 | 804.62 | 1,230.44 | ND |" (FY26 column 1,230.44) - runs/aequs-q2fy27/work/review_aequs_q2fy27.md:114; "Q4 FY26 operational EBITDA was Rs 42 mn against a headline Rs 321 mn" - gate-recommendation.md:36-37; "The Rs 90 mn exceptional gain inside the Q4 FY26 reported loss of Rs 541 mn" - gate-recommendation.md:42
- result vs base: NO BASELINE
- management's stated reason: NOT FOUND
- risk flagged before / by whom / overruled: NO (no analysis of ours predates the result)

## Q1 FY27
- base case: NOT FOUND
- guidance: "| Consolidated revenue growth | ~45-50% | FY27 | Q4 FY26 (p.3); reaffirmed Q1 FY27 (p.3) |" - 05-concall.md:58
- catalysts: "| Q4 FY26 | Consumer EBITDA loss path to Q4 FY27 breakeven | ✅ Partial / on track (Q1 FY27: loss narrowed Rs 473mn→Rs 361mn" - 05-concall.md:129; "15-year Safran A320 wheel agreement (deliveries FY28)" - companies/AEQUS.md:26-27
- actuals: revenue 395.55, EBITDA as printed 21.49, PAT (53.23) - review_aequs_q2fy27.md:114, 125, 133; "| Segment EBITDA | 73.1 | (36.1) |" - notion-page-snapshot-2026-10-28.md:54
- result vs base: NO BASELINE
- management's stated reason: NOT FOUND
- risk flagged before / by whom / overruled: NO. "Prior-quarter run folder: none (no aequs-q1fy27 run exists)" - runs/aequs-q2fy27/work/run-log.md:13

## Q2/H1 FY27
- base case: "# Projections, UNSIGNED, not pipeline output" / "Not Stage 11. No Section 1B has run. Rs cr." / "| Total revenue | 1,230 | 1,690 | 2,218 |" / "| EBITDA | 154 | 154 | 354 |" / "| Net profit | (113) | (158) | 42 |" - notion-page-snapshot-2026-10-28.md:86-97
- base predates result: "The unsigned FY27/FY28 base (PAT ₹(158) Cr / ₹42 Cr) does not depend on who holds the float." (09-Oct-2026 entry) - notion-page-snapshot-2026-10-28.md:220
- projection basis: "Base consumer revenue of +90% sits below the +125 to 150% guide" - :101; "aerospace is 80% of the business with an eight-year order book" - :103
- falsification line: "Q2 FY27 consumer segment EBITDA loss at or wider than the Q1 FY27 Rs 36.1 cr, with consumer utilisation still at or below 23 percent." - gate-recommendation.md:513-514
- guidance: 05-concall.md:58 (as Q1); "Consumer utilisation. Fell 31% to 23% to 22% across three quarters against an unchanged 40 to 50% FY27 exit target." - notion-page-snapshot-2026-10-28.md:107
- catalysts: "Hosur Phase 1 is an investment start in Q4 FY27; commercial production FY29, P-L240-246" - runs/aequs-q2fy27/notion-payload.md:42
- actuals: revenue 409.08 / H1 804.62; EBITDA 24.47 / H1 45.95; PAT (52.39) / H1 (105.62) - review_aequs_q2fy27.md:114, 125, 133; "consumer seg EBITDA Rs (40.14) Cr vs 36.1; utilisation 17% (filed deck) vs 23%" - notion-payload.md:17
- result vs base: MISS. "This breaks the test the draft model set. The model said the thesis fails if the consumer loss reaches Rs 36.1 Cr with use at or below 23%. Both legs fired." - runs/aequs-q2fy27/operator-brief.md:15; "| Revenue FY27 | ND ... | 1,690 (N-L94) | ND | H1 804.62 (R-L375); Q2 run-rate FY27 1,622.8 (INFERENCE) | Below base by 4.0%; bear value ND |" - review_aequs_q2fy27.md:335
- management's stated reason: "Management withdrew the Q4 FY27 consumer breakeven date (P-L265). It gave no new date. On the call it blamed a product qualification delay and a toy customer change." - operator-brief.md:14; "| 3 | Consumer Q2 volume ramp slower than anticipated; qualifications longer, supply chain | Backward | NO | C-FT69-73 |" - review_aequs_q2fy27.md:465
- risk flagged before / by whom / overruled: YES. "| MAJOR | B05 §1C, §4A trigger 3 | [holding detail removed]; "Kill: loss widens in Q2 or Q3 FY27, or utilisation stalls near 22 to 25 percent." - gate-recommendation.md:467-468. Not overruled: adopted as the Falsification line (gate-recommendation.md:511-514). Stage 5 had recorded the breakeven path as "✅ Partial / on track" - 05-concall.md:129

## Not found
- board (SME / main)
- verdict of the 2026-08-04 concall note (header-only excerpt)
- Q4 FY26 quarterly revenue; Q4 FY26 and Q1 FY27 base case; Q4 FY26 and Q1 FY27 management reason
- any stage-11 base case (stages 10 and 11 did not run)
