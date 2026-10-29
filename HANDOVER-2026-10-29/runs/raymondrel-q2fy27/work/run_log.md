# Run log: RAYMONDREL Q2 FY27 (/run-quarterly, 2026-10-28)

Orchestrator: Opus 5.5 session, worktree branch claude/qr-raymondrel-q2fy27-f76d61 (batch q2fy27-1028, batch 2).

## Setup
- Sparse: `tools/sparse_session.sh runs/raymondrel-q2fy27` run; tree 92 MB.
- Checkout guard: `git fetch origin main` OK; diff over .claude/ prompts/ frameworks/ CLAUDE.md LESSONS.md empty. PASS.
- Protocol files present: Quarterly_Results_Review_Protocol_v1_4.md, Quarterly_Concall_Analysis_Protocol_v1_1.md (Document_Review_Protocol_v1_1.md present, not used: full-quarter run).
- Toolchain: pdftotext, pdfinfo, pdffonts, pdftoppm on PATH; tesseract at C:\Program Files\Tesseract-OCR\tesseract.exe.
- Company memory: no companies/RAYMONDREL.md.
- Notion: COMPANIES MASTER page "Raymond Realty" (394bb2b9-d3ab-81ab-a206-e4fbc8b538a5) fetched live 28-Oct. Decision Status WATCHLIST / AVOID. Entry Rs 550-611, MoS Rs 550. Last Key Notes 26-Oct-2026 (ICICI Pru AIF Rs 210 Cr). Snapshot: work/notion_page_raymondrel_2026-10-28.md (149,470 chars). Passed to A3 and A4 by path with line pointers.
- Concall: ASR transcript present at run start (written 10:59 IST, 52,706 bytes, 3,607 s audio). Run as `concall` from the start.
- Results PDF: text layer present (non-embedded Helvetica; OCR-style text, page 1 letterhead garbled). Per batch instruction 3, A1 told to check statement pages against pdftoppm renders.

## Document-class detection (content, pages 1-2)
| File | Class | Evidence |
|---|---|---|
| RaymondRealty_Q2FY27_Results_with_Press_Release.pdf (15p) | results | "Outcome of the Meeting of the Board of Directors ... Approval of Unaudited Financial Results (Standalone and Consolidated)"; "Regulation 30 and Regulation 33"; encloses limited review report and press release |
| RaymondRealty_Q2FY27_Investor_Presentation.pdf (46p) | presentation | slide structure, 46 pages |
| RaymondRealty_ICICI_Pru_Investment_Agreement.pdf (3p) | corpaction (one-off Reg 30 disclosure, presentation class rules) | "Intimation pursuant to Regulation 30 ... Execution of Investment Agreement by Ten X Realty West Limited" |
| RaymondRealty_Q2FY27_Concall_Transcript_ASR.txt | concall | "Ladies and gentlemen, good day and welcome to the Raymond Realty Limited Q2 FY27 earnings conference call"; machine transcript |

## Agent steps
- A1 presentation GATE PASS: 46/46 page markers, 1,082 rows R001-R1082. Verification renders p4-6,8,9,11,12,20,22-24,26-44; p5 labels off by one row in text layer; p29-44 project tables mapped from renders; superscript '1' fused into units-launched counts on 9 slides, render value used.
- Note: A1 presentation header says page 13 is an image with no text, while the reply says no page had zero characters. Logged for A5.
- A1 results GATE PASS: 15/15 page markers, 874 rows R001-R874. OCR text layer (HiddenHorzOCR); statement pages 3,4,5,9,10,11 and PR table p13 re-read from 150 dpi renders. Standalone TCI misprint 6,657 corrected to 4,155 from image. p7 auditor paragraph '(81 O lakhs)' OCR_UNCERTAIN. Spot-check: consolidated rev ops Q2 74,852 lakhs = Rs 748.5 Cr vs deck p22 Rs 749 Cr; Q2 FY26 697; H1 1,275. Ties.
- A2 presentation GATE PASS: 1082/1082, 0 orphans; fulltext sweep 1145 tokens, 44 unmatched all explained; M1 phone (low). PAGE_ANCHOR_DEFECT R840/R1068 (p32 vs p33). Cost 62,322 < A1 125,535.
- A2 results GATE PASS: 874/874, 0 orphans; 13 notes, 184 line items, 48 ZERO_STANDING cells, 3 agenda items, 11 auditor paras, 8 entities. Unmodified limited reviews. M1-M4 low materiality (UDINs, FRNs, place); no A1 loop. Ten X Realty North formerly Chembur Realty (ENTITY_CHANGE).
  - A2 results cost 102,814 < A1 143,171. PASS.
- A1 concall GATE PASS: 600/600 source lines verbatim (fulltext line = source + 18), 320 rows R001-R320, 16 inferred turn rows, 11 ASR_SUSPECT rows. No Thane monetisation or warrant-money statement found in transcript.
- A1 corpaction GATE PASS: 3/3 pages, 63 rows R001-R063. 'aggregate Rs 210 Cr' (letter) vs 'Up to Rs 210 Crores' (Annexure A (d)). Instrument, tranches, return, tenure, TXRWL shareholding change, guarantees, CPs not disclosed (R063). Per task: no A2/A3 on this filing; carried to A4 as a capital event.
- A2 concall GATE PASS: 320/320, 0 orphans; 16 turns, 10 questions; 0 MISSING; ~17 rows with anchors drifting 1-8 lines (R052, R054, R064, R067, R130, R139). Conflicts: ICICI 140 Cr (analyst R129) vs 210 Cr (R055, R066); promoter equity ~400 (R056) vs ~410 Cr (R069).
  - A2 concall cost 54,066 < A1 80,598. PASS.
- A3 presentation GATE PASS: F1-F17 all statused (8 FINDING, 1 PASS, 8 N.A.); 35 findings (10 FWD, 21 AMBIG). Key: BKC revenue recognised 577 > bookings 521; JDA rev 2,549 vs collections 857; ex-other-income EBITDA Q1 11.4% / Q2 14.3%; net debt ~912; Mahim-1 now Q4 FY27. A1 header inconsistency on rendered_pages logged for A5.
- A3 results GATE PASS: 17/17 statused (11 FINDING, 4 PASS, 2 N.A.); 23 findings (6 FWD, 14 AMBIG, 3 NEUTRAL). Key: Rs 17 Cr govt-authority interest in finance cost; margin ~13.0% if treated as project cost; net debt computed 916 (PR 912); gross D/E 0.752x; subsidiaries 63% of Q2 revenue outside joint auditors' review; ICD (given) Rs 127.6 Cr H1; R831 = 810 lakhs; no warrant money in H1.
- A3 concall GATE PASS: 17/17 statused (7 FINDING, 10 N.A.); 23 findings (11 FWD, 8 AMBIG, 4 CONF-NEG). Key: 20% revenue guide withdrawn (L547); 17-19% EBITDA guide back-ended; Rs 400-600 Cr more equity in 5-yr plan; net worth does not tie (~22% gap); 10X subsidiary ICICI-backed fund 60% via OCPRS (minority interest); Rs 10,000 Cr 4-5 yr cash flow claim; 7 of 13 Q1 questions unanswered.
- 14:22 A4 dispatched (Role 4 + Role 5; Notion thesis by path; concall ASR; corpaction carried as capital event; FORWARD ESTIMATE INPUTS requested for the brief).
- 14:45 A4 done: PROCEED WITH FLAGS; margin stop and net-debt rulings laid out, not ruled; Decision Status WATCHLIST/AVOID verified. A5 dispatched with review + A1 + A2 paths only.
- 15:04 A5 INCOMPLETE: FACTUAL F1-F4, MISSING M1-M4, CONTRADICTION C1 (A4) and C2 (A2 concall ledger line-0 anchors, annotation only); STYLE S1-S6 logged. Loop 1 of 1 starts: A2 concall anchor repair + A4 patch in parallel (both resumed), then A5 re-audit.
- Loop 1 A2 concall done: line/turn columns rebuilt (awk split bug); 10 DRIFT rows marked; 320/320, 0 orphans.
- 15:13 Loop 1 A4 patch done (whole-file rewrite): F1-F4, M1-M4, C1 fixed; S1-S5 applied; verdict unchanged; FY27E PAT Reading B 264-309. A5 re-audit dispatched (resumed, file paths only).
- 15:17 Loop 1 A5 re-audit COMPLETE: F1-F4, M1-M4, C1, C2 closed; drift check clean; style S6-S8 logged, no re-run. Loop count 1.
- 15:20 Close-out: session-cost.md, operator-brief.md, notion-payload.md written. No Notion write. No companies/RAYMONDREL.md created. Loop count 1.
