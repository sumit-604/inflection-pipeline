# Run log: TINNARUBR Q2 FY27 (/run-quarterly)

Run date: 2026-10-23. Orchestrator session on Opus 5.5.

## Setup
- Checkout guard: `git fetch origin main` OK; `git diff --quiet origin/main -- .claude/ prompts/ frameworks/ CLAUDE.md LESSONS.md` empty. PASS.
- Protocol files present: Quarterly_Results_Review_Protocol_v1_4.md, Quarterly_Concall_Analysis_Protocol_v1_1.md, Document_Review_Protocol_v1_1.md.
- Toolchain: pdftotext, pdfinfo, pdffonts, pdftoppm on PATH. tesseract installed at C:\Program Files\Tesseract-OCR, not on PATH (both inputs have a text layer, OCR not expected).
- Sparse checkout: tools/sparse_session.sh runs/tinnarubr-q2fy27 (per-worktree config).

## Documents fetched (BSE scrip 530475, NSE TINNARUBR)
| File | Source | First-page check | Class |
|---|---|---|---|
| Tinna_Q2FY27_Results_Reg33_2026-10-22.pdf (13 pp) | BSE AttachLive 30143086-b7f6-48ef-86a8-41644544153e.pdf, filed 22-Oct-2026 14:21 | "Date: October 22, 2026 ... OUTCOME OF MEETING OF THE BOARD OF DIRECTORS ... HELD ON THURSDAY, OCTOBER 22, 2026", Regs 30 and 33 | results (Reg 33 markers) |
| Tinna_Q2FY27_Press_Release_2026-10-22.pdf (3 pp) | BSE AttachLive e2d6dfcc-f79b-437b-bdd9-3a0de5be7ba7.pdf, filed 22-Oct-2026 16:08 | "Date: October 22, 2026 ... PRESS RELEASE H1 FY 2027 FINANCIAL RESULTS" | presentation slot (press release; company narrative, no speaker turns, no Reg 33 tables) |
| Tinna_Q2FY27_Concall_Intimation_2026-10-19.pdf (2 pp) | BSE AttachLive a2524779-...pdf | call "on Monday, October 26, 2026 from 03:00 P.M. (IST)" | context only, not run |

- The BSE "Board outcome" attachment 61cfbab7-... is byte-identical to the results file (cmp); duplicate removed.
- Investor presentation: NOT FOUND on BSE (to 23-Oct) or NSE corporate announcements (15-23 Oct). Company site tinna.in sits behind a bot-verification page; not bypassed.
- Concall: not yet held (scheduled 26-Oct-2026). No transcript, no recording. Role 5 does not run this cycle.
- Storage: C:\ConcallPipeline\Daily Concall Intelligence\Q2 FY27 Results\28 Tinna Rubber\

## Company memory and Notion
- companies/TINNARUBR.md: absent. No Spear line on record.
- Notion COMPANIES MASTER: search "Tinna Rubber" returns no company page (read only, 23-Oct-2026). Output framed as PRE-THESIS READ.
- Tracker rows: not supplied.

## Protocol scoping
- Full quarter (results filing present): A4 gets Role 4 v1.4 only. No concall, so Role 5 v1.1 not passed.

## A1-A3 log
- A1 presentation (press release): PASS, 3/3 pages, R001-R138, ~52.7k tok.
- A2 presentation: PASS, 138/138 IDs, no orphans, ~37.5k tok (below A1).
- A1 results run 1: coverage PASS 13/13, but the embedded text layer on statement pages 2-4 and 8-10 is corrupt OCR (garbled digits, half-year and year columns interleaved off their labels). No column assignment possible. ~88.3k tok.
- Orchestrator decision: mechanical re-run of A1 on results with a logged OCR repair (tools/ocr_repair.py or pdftoppm 300dpi + tesseract psm 6), embedded text kept, `[OCR page N]` blocks appended, per-cell NUMBER rows with OCR_CONFLICT / ARITH_FAIL / UNREADABLE flags. Reason: the text-only default does not cover a corrupt embedded OCR layer. A mechanical re-run; it does not count against any cap. tesseract run from C:\Program Files\Tesseract-OCR via PATH prefix; pypdf from a scratch venv.
- A3 presentation: PASS, F1-F17 all statused, no blanks, ~45k tok.
- Machine restart 2026-10-23 (all background jobs died). A1 results OCR re-run had written nothing; relaunched with one OCR worker. Run-1 A1 scratch files (body.txt, src.txt, hdr.txt, gen.py) moved out of work/ to the session scratchpad.
- A1 results run 2 (OCR repair): PASS, 13/13 pages, R001-R927, 692 statement cells, 0 ARITH_FAIL, 0 UNREADABLE, 227 OCR_CONFLICT, ~182.8k tok. Tesseract psm 6 at 300dpi on pages 2-4, 8-10 (+ supplement blocks 1, 5, 11, 13); cell values read from page images and footed by arithmetic. Embedded "October 21" date on p3 corrected to October 22 by OCR and image. Orchestrator spot-check: standalone H1FY27 PAT 3,617.29 lakh (R111) and consolidated H1FY27 PAT 3,760.57 lakh (R494) agree with the press release (Rs 36 Cr, Rs 38 Cr).
- A2 results: PASS, 927/927 IDs, no orphans, 226 line items, ~68.1k tok (below A1 182.8k).
- A3 results: PASS, F1-F17 statused (10 FINDING, 5 PASS, 2 N.A.), 17 findings A3-01..A3-18 (A3-03 merged), ~165k tok est.
- A4: complete, PROCEED WITH FLAGS, pre-thesis read, Role 5 not run (call 26-Oct), ~285.1k tok.
- A5 run 1: INCOMPLETE (1 FACTUAL, 5 MISSING, 10 STYLE), ~302.9k tok. Loop iteration 1 to A4 (resumed agent) with F1-F6. A2/A3 not re-run.
- A4 loop 1: F1-F6 applied, verdict unchanged PROCEED WITH FLAGS; cumulative A4 ~344.2k tok (loop ~59k).
- A5 re-audit (loop 1): COMPLETE, F1-F6 closed, 4 new STYLE notes (RS1-RS4), ~75k tok.
- Notion payload written to notion-payload.md (no write). session-cost.md written.
