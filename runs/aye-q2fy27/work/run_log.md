# Run log: AYE Q2 FY27 quarterly review (/run-quarterly)

- 2026-10-23 checkout guard: git fetch origin main OK; diff on .claude/ prompts/ frameworks/ CLAUDE.md LESSONS.md empty. PASS.
- Protocol files present: Quarterly_Results_Review_Protocol_v1_4.md, Quarterly_Concall_Analysis_Protocol_v1_1.md, Master_Project_Prompt_v3_6.md.
- Toolchain: pdftotext, pdfinfo, pdffonts, pdftoppm on PATH; tesseract at C:/Program Files/Tesseract-OCR (off PATH, not needed: all docs have text layers).
- Sources: BSE scrip 544699 announcements API. Results (Reg 33, 21-Oct-2026 11:54, 24 pp), investor presentation (21-Oct-2026, 44 pp), press release (21-Oct-2026, 3 pp; kept in inputs/ as reference, not run through A1-A3: summary of the results filing), audio-recording outcome (22-Oct-2026). Copies in C:\ConcallPipeline\Daily Concall Intelligence\Q2 FY27 Results\30 Aye Finance\.
- Class detection: Reg33 bundle -> results (Board Outcome + "Unaudited Financial Results" + limited review); deck -> presentation (slide structure); ASR transcript -> concall (speaker turns, Moderator).
- Concall: held 22-Oct-2026 10:00-11:11 IST. No transcript filed at run time. Audio from company CloudFront link named in the 22-Oct BSE filing; transcribed locally with faster-whisper "small" int8 (machine transcription, speaker turns best effort).
- Machine restart mid-run killed the first A1 pair and the first ASR job; both restarted; no output from the killed runs was used.
- PyAV and the venv ctranslate2 DLL blocked by Windows App Control; used the existing user-profile venv with an av stub and ffmpeg decode.
- Notion read live (page 3a6bb2b9d3ab81f18365f37559223a59): Decision Status HELD, 4% at Rs132; snapshot in work/notion_snapshot_AYE_2026-10-23.md. Tracker rows in work/signal_context_AYE.md.
- Prior-quarter references made by orchestrator (pdftotext -layout, line-numbered) from repo copies in runs/aye-2026-07-22/inputs: work/prior_q1fy27_results_fulltext.md, work/prior_q1fy27_presentation_fulltext.md.
- PIPELINE ERRORS LOGGED (not looped; gates passed):
  - A2 results ledger line 28 states no signature timestamp precedes approval; A3 shows fulltext line 980 (11:09:12) precedes the 11:15 board start. A3 finding A3-18.
  - A1 results omitted five signature timestamp rows (A2 MISSING_FROM_STRUCTURED M01-M05).
  - A1 presentation swapped labels on R076/R077 (1,219 is Q1FY27, 1,275 is Q2FY26) and omitted line 667 (83, 308, 6,865) and line 807 (0). Downstream must use the A3 correction.
  - A1 concall (ASR text): 346 structured rows curated by hand, not script-generated; count not reproducible; A1 dropped two self-invented qualifier rows before writing. Line coverage 846/846 proven by diff. A5 coverage re-run over the fulltext is the check.
- Correction loop 1 (A5 INCOMPLETE: COV-1..4 to A2, ADV-1..3 to A4): A2 fixed both ledgers; A4 grafted three bear counters and style notes; A5 re-audit still INCOMPLETE on R1-1/R1-2 (A4 preamble counts pre-loop ledgers; results M07 orphan). Loop cap is one iteration: second loop NOT run. Open for operator: approve a second A4 edit (two table rows + one reviewed-no-finding line), or carry it as an open item.
- Notion: NOT written. Payload saved to notion-payload.md (blocked by A5 INCOMPLETE and by the in-run approval gate).
