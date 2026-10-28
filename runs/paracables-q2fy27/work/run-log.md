# Run log: PARACABLES Q2 FY27 quarterly review

Session: company session qr-paracables (batch runs/_batch-q2fy27-1028.md, batch 1). Orchestrator model Opus 5.5.
Started 2026-10-28 ~09:58 IST.

## Setup
- Sparse checkout: `tools/sparse_session.sh runs/paracables-q2fy27` run.
- Checkout guard: `git fetch origin main` OK; diff over .claude/ prompts/ frameworks/ CLAUDE.md LESSONS.md empty. PASS.
- Protocol files present: Quarterly_Results_Review_Protocol_v1_4.md, Quarterly_Concall_Analysis_Protocol_v1_1.md, Document_Review_Protocol_v1_1.md, Master_Project_Prompt_v3_6.md.
- Toolchain: pdftotext, pdfinfo, pdffonts, pdftoppm on PATH; tesseract v5.4.0 at C:\Program Files\Tesseract-OCR\tesseract.exe.
- Company memory: companies/PARACABLES.md does NOT exist. Not created (batch instruction).
- Notion: live page found (COMPANIES MASTER, "Paramount Communications", 345bb2b9-d3ab-808f-9f1d-e0960dc67726, last edited 2026-10-26 17:17 UTC). Decision Status WATCHLIST / AVOID. Page is 74k chars, so the orchestrator saved it verbatim to work/notion_snapshot_paracables_2026-10-28.md and passes that PATH to A3 (monitoring checklist) and A4 (thesis) instead of pasting it inline. Deviation logged: content identical, carrier is a file. No formal Role 2 thesis-broken conditions exist on the page (Role 2 never run). Key Notes already carry a 26-Oct quick read of this print by claude.ai.
- Transcript: concall_audio/Paramount_Q2FY27_Concall_Transcript_ASR.txt existed at setup (50,061 bytes, written 09:40 IST). Run includes it as `concall` (ASR, management-tier, unverified).

## Document class detection
| File | Pages | Class | Basis | Text layer |
|---|---|---|---|---|
| Paramount_Q2FY27_Results.pdf | 13 | results | p1 "Outcome of Board Meeting ... Regulation 30 and 33", p3 "STATEMENT OF UNAUDITED STANDALONE FINANCIAL RESULTS" | Third-party OCR layer (GlyphLessFont, Online2PDF). GARBLED: p3 row labels shift one row against values; Q1 current tax reads 6.94 in layer vs 6.91 on page image; "564,20", "32,39". Scan-OCR fallback ordered. |
| Paramount_Q2FY27_Investor_Presentation.pdf | 37 | presentation | slide structure, "INVESTOR PRESENTATION Q2 FY27", safe harbour | Native PowerPoint text layer (Calibri, Arial). Text-only. |
| Paramount_Q2FY27_Press_Release.pdf | 3 | presentation (file tag `pressrelease`) | covering letter + press release, Reg 30 | Third-party OCR layer (GlyphLessFont, iLovePDF). GARBLED on p2 table ("ROpeevreantuieonfsrom", "242" for 24.2). Scan-OCR fallback ordered. |
| Paramount_Q2FY27_Concall_Transcript_ASR.txt | n.a. | concall | timestamped speaker turns, moderator close | Plain text, machine ASR. |

File tag note: the press release and the deck share doctype `presentation`. The press release uses file tag `pressrelease` in every working-file name so the two never collide. Forensics files carry the tag in the file name (forensics_<tag>_paracables_q2fy27.md).

## Agent runs
(appended below as each gate passes)
- A1 x4 (parallel, Sonnet 5.5): all GATE A1 pass. results 13/13 pages scan-ocr, 989 rows, 38 OCR corrections (statement pages 3,4,5,9,10,11,13 image-checked; 6 and 12 only the use-of-proceeds table; narrative pages raw OCR; page 2 UDIN unresolved). presentation 37/37 text-only, 522 rows, slides 17/28/29/30 tables scrambled by the text layer (216 LAYOUT_* rows; R293-R295, R385-R388 LAYOUT_UNRESOLVED). pressrelease 3/3 scan-ocr, 157 rows, 7 corrections. concall 595/595 source lines, 377 rows, 88 inferred turns, one 71 s timestamp gap 00:13:48-00:14:59 (ASR silence/dropout).
- A2 x4: all GATE A2 pass (count tests match, zero orphans). Each A2 cost below its A1. results A2 notes count: raw grep 19 vs sweep 20 (OCR on consolidated note 1), re-swept to 20, resolved inside the run. results A2 found MISSING_FROM_STRUCTURED M001-M004 (page 11 consolidated cash flow, fulltext lines 604 and 612). Orchestrator sent this back to the results A1 (same agent, resumed) to image-check page 11 and append rows R990-R993. Not a gate failure: A2 caught it as designed.
- A3 pressrelease: GATE A3 pass, 6 FINDING / 11 N.A., 12 findings all line-cited.
- A3 concall: GATE A3 pass, 3 FINDING / 1 PASS / 13 N.A., 19 findings all line-cited.
- A1 results follow-up (resumed): page 11 image-checked; 1.74 / 97.67 (H1 FY27) and nil (H1 FY26) confirmed; fulltext lines 604/612 "=" -> "-" (line count unchanged 713, logged C39); rows R990-R993 appended (= A2 M001-M004).
- A3 results: started after the follow-up, told R990-R993 = M001-M004.
- A3 presentation: GATE A3 pass, 8 FINDING / 1 PASS / 8 N.A., 19 findings line-cited. A3 named four A1 structured-file defects (slide 28/30 line cites one early; R371 line; "20.4%" L425 and "85.3%" L426 not captured; possible depreciation/finance-cost swap for Q2 FY26 and H1 FY26). Sent back to the deck A1 (resumed) to fix in the structured file only; fulltext body lines frozen so A3 cites hold.
- A1 presentation follow-up (resumed): four defects fixed in structured file only (fulltext untouched). Slide 28/30 cites re-mapped; R371 -> L450, new R525 (L453); new R523 20.4% (L425), R524 85.3% (L426); depreciation/finance-cost swap confirmed on image and corrected (Q2 FY26 dep 3.8 / fin 4.0; H1 FY26 dep 7.4 / fin 7.9), flagged CORRECTED_FROM_IMAGE; slide 30 FY26 asset values re-assigned. Range now R001-R525. The deck A2 ledger predates R523-R525; A4/A5 are told these three rows exist.
- A3 results: GATE A3 pass, 6 PASS / 9 FINDING / 2 N.A., 15 findings line-cited; 993 rows read incl. R990-R993. No prior-quarter verbatim auditor text existed; F5/F15 rest on Notion memory.
- Transcript re-check before A4 (batch rule 2): source file unchanged since setup (50,061 bytes, 09:40), byte-identical to inputs copy. Concall included.
- Signal context: two DOWNSTREAM SIGNAL TRACKER rows fetched live and saved to work/signal_context_paracables_2026-10-28.md; passed to A4 for Step 5.5.
- A4 (Opus 5.5): review written, 20,747 words. Verdict PROCEED WITH FLAGS; cash conversion INDETERMINATE-WITH-DIRECTION; Decision Status WATCHLIST / AVOID verified, branch 8A-W, no change proposed; 27 QfM rows; all 65 A3 findings claimed incorporated.
- A5 (Opus 5.5), iteration 0: INCOMPLETE. 1 FACTUAL (F1 data-centre inconsistency unsupported), 4 MISSING (M1 deck ledger R523-R525; M2 ROCE pre-build counter; M3 warrant-economics counter; M4 four A3 IDs uncited), 2 CONTRADICTION (X1 five turns mis-flagged, count 27->32; X2 commitment 5 MISSED vs 6D confirming), 12 STYLE (logged, no re-run). Brief 5/5 parts present; arithmetic clean.
- LOOP iteration 1 started (batch rule 4: one loop by default): A2 deck (M1) and A2 concall (X1) resumed in parallel; then A4 for X1/X2/M2/M3/M4/F1; then A5 re-audit once.
- LOOP1 A2 concall (resumed): T26/T37/T40/T46/T55 re-flagged QUESTION_CONFIRMED; substantive 32 of 35.
- LOOP1 A2 presentation (resumed): R523-R525 added; 525/525 IDs, zero orphans; 8 rows CORRECTED_FROM_IMAGE; no LAYOUT_UNRESOLVED rows remain.
- LOOP1 A4 (fresh Opus 5.5 instance, targeted): all six items fixed. X2 rescored commitment 5 PARTIALLY DELIVERED, 50% -> 66.7%, grade C -> B (provisional), OVERPROMISER -> COMMITTED & CREDIBLE (provisional), MISSED reading stated with its separating observation. M2 ROCE ~10.1% post-build. M3 warrant conversion as arbitrage. F1 withdrawn, Q25 rewritten. Verdict unchanged PROCEED WITH FLAGS; QfM 27.
- LOOP1 A5 re-audit: same A5 agent resumed with a neutral instruction only.
- LOOP1 A5 re-audit (resumed): INCOMPLETE. X1, X2, M2, M3, F1, M4 closed; new arithmetic ties; brief 5/5. One open item C1 (CONTRADICTION, routes to A2): deck ledger slide index cells (LED-PPT l.49, l.52, l.54) off after R523-R525 were added (slide 25 range ends R525 not R522; slide 28 rows 97 not 99; slide 30 rows 44 not 45). Nothing in the review or A3 depends on it.
- Loop cap reached. Batch rule 4 allows a second loop only for a FACTUAL/CONTRADICTION item that moves a verdict-card number; C1 does not, so no second loop. C1 goes to the operator. Final A5 state: INCOMPLETE, 1 ledger-index item after 1 loop. Notion write not executed (batch rule 6); payload left for approval.
- Close-out: work/pages.pkl (agent scratch pickle) removed before commit; helper scripts kept as audit trail, as in prior batch runs.
