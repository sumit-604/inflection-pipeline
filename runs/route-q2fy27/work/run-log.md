# Run log: ROUTE q2fy27 (/run-quarterly, batch 2026-10-28, batch 4)

Session: qr-route, Opus 5.5 orchestrator. Worktree branch claude/qr-route-q2fy27-fb3514, cut from run/quarterly-q2fy27-2026-10-28.

## Setup
- Sparse checkout: tools/sparse_session.sh runs/route-q2fy27 (tree 93 MB).
- Checkout guard (29-Oct): git fetch origin main OK; diff over .claude/ prompts/ frameworks/ CLAUDE.md LESSONS.md empty. PASS.
- Protocol files present: Quarterly_Results_Review_Protocol_v1_4.md, Quarterly_Concall_Analysis_Protocol_v1_1.md, Document_Review_Protocol_v1_1.md, Master_Project_Prompt_v3_6.md.
- Toolchain: pdftotext, pdfinfo, pdffonts, pdftoppm on PATH; tesseract at C:/Program Files/Tesseract-OCR/tesseract.exe.
- Company memory: no companies/ROUTE.md in repo.
- Notion: COMPANIES MASTER page 345bb2b9d3ab8041a078fd2708a38fdf fetched read only 29-Oct (content as of 2026-09-03T02:54Z). Decision Status HELD; 4% at avg cost Rs 509; Entry Price Max Rs 628. Snapshot work/notion_snapshot_2026-10-29.md; extracts work/notion_thesis_context.md and work/monitoring_checklist.md. No Notion write (batch standing instruction 6).
- Pre-committed Q2 FY27 gate on file: thesis-broken condition 1, consolidated Adj. EBITDA margin <10% for a 2nd consecutive quarter (Q1 FY27 was 1 of 2). Proximus revenue-synergy KPI due at Q2 or Strategic Premium expires (+1.25x to +1.0x).
- Prior quarter: Q1 FY27 extracts, ledgers and review copied from origin/claude/route-mobile-quarterly-pkqpxv into work/prior/.

## Document class detection (content, first pages)
| File | Pages | Class | Basis |
|---|---|---|---|
| RouteMobile_Q2FY27_Results.pdf | 18 | results | Outcome of Board Meeting 27-Oct-2026, Reg 30/33/42, unaudited standalone and consolidated results with limited review reports |
| RouteMobile_Q2FY27_Investor_Presentation.pdf | 23 | presentation | Reg 30 cover letter, investor presentation for analysts 28-Oct-2026 |
| RouteMobile_Q2FY27_Press_Release.pdf | 3 | pressrelease | Reg 30 cover, press release "Route Mobile Limited announces Q2 FY27 Results" |
| Concall transcript | n/a | concall | ABSENT at run start (call 28-Oct 16:30; no recording posted; concall_audio/ empty). Re-check before A4. |

## Agent runs
- A1 presentation run 1: GATE A1 pass 23/23 pages, R001-R351; 8 slides scrambled in -layout (12,13,17-22). 68,396 tok, 164 s. Resumed once for targeted re-extraction of those pages (orchestrator: decisive Adj. EBITDA and cash slides cannot stay layout-ambiguous).
- A1 presentation run 2 (resume, targeted fix): pages 12,13,17-22 re-extracted (-raw + 100 dpi render check, no OCR); fulltext 909 lines; R001-R368; page 19 Adj. EBITDA bridge and page 20 cash bridge arithmetic-checked by A1. GATE A1 pass. 111,809 tok as reported by the notification, 323 s.
- A1 results run 1: GATE A1 pass 18/18 pages, 1,273 lines, R001-R1127. Pages 7-11 and 14-16 switched to pdftotext -raw (layout scramble); values mapped by row order and cross-footed by A1. Two cells OCR_ILLEGIBLE (H1 FY27 net forex; standalone FY26 OCI). 126,206 tok, 392 s. Resumed once to read those two cells and the p7 Q2 FY26 hedge cells from a render.
- A1 pressrelease run 1: GATE A1 pass 3/3 pages, 131 lines, R001-R074. A1 itself reported approximate line anchors. 41,180 tok, 68 s.
- Orchestrator mechanical anchor check (scripted token-on-cited-line test; no content judgement): pressrelease 18 rows off; resumed A1 pressrelease once to re-grep every row. Presentation: NUMBER/DATE rows R096-R098, R103 cite line 207-208, values at line 217 (work/anchor_check_presentation.txt). Results: 10 DATE/period-label rows on -raw pages loosely anchored (work/anchor_check_results.txt); NUMBER rows on non-scrambled pages all within 2 lines.
- A1 results run 2 (resume): H1 FY27 net forex = (1.63) gain (R582), standalone FY26 OCI = (0.57) (R698), p7 Q2 FY26 hedge cells are dashes (R1128-R1129). 1,279 lines, R001-R1129. Notification total 138,587 tok cumulative for the agent (resume delta ~12,381), 471 s cumulative.
- A1 pressrelease run 2 (resume): 21 rows re-anchored, A1 script re-check 0 misses. Cumulative 56,670 tok (delta ~15,490), 176 s cumulative.
- A1 presentation run 3 (resume): R096-R098 -> line 217, R103 -> 219; self re-grep found no other row >2 lines off. Cumulative 114,607 tok (deltas: run 2 ~43,413, run 3 ~2,798), 25 s.
- A2 presentation: GATE A2 pass, 368/368 IDs, zero orphans, count test matched in every category; 18 ZERO_STANDING (slide 19). 52,158 tok (below A1 114,607), 85 s.
- A2 pressrelease: GATE A2 pass, 74/74 IDs, zero orphans; entity grep 14 vs A1 header 13 (R054 ENTITY-SUMMARY counted; explained, not a mismatch). 37,380 tok (below A1 56,670), 46 s.
- A2 results: GATE A2 pass, 1129/1129 IDs, zero orphans; notes 19 grep vs 23 sweep reconciled (4 unnumbered sub-notes); line items 256; zero-standing 42 cells. Flags incl. AUDITOR_CHANGE (MSKA), UNREVIEWED_ENTITIES (7), R965 Annexure Sr.33 name blank. 97,522 tok (below A1 138,587), 215 s.
- A3 results: GATE A3 pass (F1-F17 all statused: 10 FINDING, 5 PASS, F16/F17 N.A.); 1129/1129 rows read. R965 resolved as a numbering misprint (33 vs 33 names match). 206,972 tok, 559 s.
- A3 presentation: GATE A3 pass (F1-F17 all statused: 9 FINDING, 1 PASS, 7 N.A.); 368/368 rows read; 26 findings. 148,223 tok, 580 s. A3 note: seven A1 rows cite a line 1-9 lines off on the same slide (values unaffected); logged, no A1 loop.
- Transcript check before A4 (29-Oct 04:45 machine clock): concall_audio/RouteMobile_Q2FY27_Concall_Transcript_ASR.txt ABSENT; folder empty. A4 runs on filed documents only; Role 5 protocol not passed.
- A3 pressrelease: GATE A3 pass (8 FINDING, 1 PASS, 8 N.A.); 74/74 rows. 76,297 tok, 314 s.
- A4 started (single agent; memory). Inputs: Role 4 protocol only, 3x A1/A2/A3 paths, notion_thesis_context.md + snapshot + prior Q1 review by path, key Notion fields inline, CMP context.
- A4: review written 05:04, block 05:05 (machine clock). 818 lines; all five brief parts present; PROCEED WITH FLAGS; cash INDETERMINATE-WITH-DIRECTION; branch 8A; 22 questions; 13 flags. The orchestrator process exited before the completion notice, so A4 token count and wall time are NOT RECORDED (handback report received; files verified on disk). Coordinator check message received; A5 started on resume.
- A5 loop 0: INCOMPLETE. Coverage FAIL (A2: 12 signed blocks vs 6; 11 signature timestamps without structured rows). 6 arithmetic mismatches + 4 FACTUAL + 3 surviving bear counters (A4). 8 STYLE logged. Verdict, cash class and F-1 framing unchanged per A5. Loop-0 review, audit and results ledger kept as *.loop0.md. Correction loop 1 started: A2 results resume, then A4 resume, then A5 resume.
- A5 audit loop 0: 298,246 tok, 1,204 s.
- Loop 1 A2 results (resume): 12 signature blocks; M01-M11 MISSING_FROM_STRUCTURED ledger rows (signature timestamps, non-financial); gate A2 pass. Orchestrator: no A1 loop for these rows (same handling as the Syngene M01-M09 rows).
  A2 loop: cumulative 106,842 tok (loop delta 9,320), 51 s.
- Loop 1 A4 (resume): all 11 A4 items + 8 STYLE patched; review 853 lines (08:11), block 08:12; verdict and cash class unchanged; 23 questions. Token count NOT RECORDED (orchestrator process exited before the completion notice).
- PAUSED on coordinator STOP (operator closed the batch without Route). No A5 re-audit, no close-out, no commit. See work/PAUSED.md.
