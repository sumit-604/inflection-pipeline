# Run log: /run-quarterly TEJASNET Q2 FY27

Session: claude/quarterly-tejas-q2fy27-f91c3c, started 2026-10-23, closed 2026-10-24.

## Setup
- Checkout guard: `git fetch origin main` OK; `git diff --quiet origin/main -- .claude/ prompts/ frameworks/ CLAUDE.md LESSONS.md` empty (origin/main 041ffb92).
- Prior runs: no Tejas Q2 FY27 run on main or on local branches claude/quarterly-tejas-q2fy27-a6fb62 and -fb40f4 (both at main tip, no commits). Q1 FY27 run exists only on origin/claude/tejas-network-quarterly-analysis-4mzxz3; its extracts and ledgers were used as prior-quarter inputs (copied to the session scratchpad, not committed here).
- Protocols present: frameworks/Quarterly_Results_Review_Protocol_v1_4.md, frameworks/Quarterly_Concall_Analysis_Protocol_v1_1.md.
- Toolchain: pdftotext, pdfinfo, pdffonts, pdftoppm on PATH; tesseract at C:\Program Files\Tesseract-OCR\tesseract.exe.
- Sparse checkout: tools/sparse_session.sh runs/supremepwr-2026-10-06 runs/tejasnet-q2fy27 (the first folder was already in this worktree's set).

## Documents (BSE scrip 540595; each verified by name and date on page 1, MD5 against the BSE attachment)
| Doctype (detected from content) | inputs/ file | BSE attachment | Filed | Pages | Detection basis |
|---|---|---|---|---|---|
| results | results_tejasnet_q2fy27.pdf | 48cf3085-3dd9-41d7-b811-84ecfe87325c.pdf (same MD5 as 872df8d2-...; filed twice) | 16-Oct-2026 | 12 | "Outcome of the Board Meeting", unaudited standalone and consolidated results, limited review |
| concall | concall_tejasnet_q2fy27.pdf | 12a0a32c-4113-40b7-9071-4b17d6847293.pdf | 22-Oct-2026 | 13 | Cover letter "Q2 FY27 Earnings Conference Call - Transcript", call held 16-Oct-2026; speaker turns, Moderator |
| presentation | presentation_tejasnet_q2fy27.pdf | c9e0674e-ace3-4792-937b-3e019836abb5.pdf | 16-Oct-2026 | 13 | Cover letter "Earnings Call Presentation- Q2 FY 27"; slide pages |
- Not run: press release (df9d5a47-..., 16-Oct, 3 pages, MD5 matches the saved Tejas_Q2FY27_Press_Release.pdf); audio-link filing (467f75dd-..., 17-Oct); 6G ISAC demo press release (fba40a01-..., 08-Oct, no financial content).
- Transcript was filed, so no ASR ran. The filed transcript states it was edited for clarity and is not verbatim.

## Notion (read only; no write this run)
- Page https://app.notion.com/p/345bb2b9d3ab819c8523e9d04213694a fetched 2026-10-23 02:05 UTC. Digest: work/notion_thesis_digest.md.
- The page already held Q2 FY27 reads made outside this pipeline (17-Oct, 18-Oct, 23-Oct Key Notes; body lines 772-3498). A3 and A4 were told not to take findings from them.

## Gates
| Agent | Doc | Gate | Result |
|---|---|---|---|
| A1 | results | page coverage | PASS 12/12. Pages 2-12 zero-character image pages, rendered at 200 dpi and OCR'd (tesseract psm 6); OCR misreads flagged, never corrected |
| A2 | results | count test, orphans | PASS 851/851, 0 orphans; A2 tokens 75,336 < A1 76,813 |
| A3 | results | F1-F17 marked, FINDING line-cited | PASS (8 FINDING, 7 PASS, 2 N.A.) |
| A1 | concall | page coverage | PASS 13/13, text layer |
| A2 | concall | count test, orphans | PASS 324/324, 0 orphans |
| A3 | concall | F1-F17 | PASS (5 FINDING, 12 N.A.) |
| A1 | presentation | page coverage | PASS 13/13, text layer |
| A2 | presentation | count test, orphans | PASS 210/210, 0 orphans |
| A3 | presentation | F1-F17 | PASS (8 FINDING, 9 N.A.) |
| A4 | merged | preamble, ND fills | PASS |
| A5 | merged | verdict | INCOMPLETE (run 1) -> INCOMPLETE (loop 1) -> COMPLETE (loop 2) |
- Cost check note: A2 concall 62,064 < A1 concall 81,533; A2 presentation 55,592 < A1 presentation 66,694.

## Interruptions (mechanical, not counted against any cap)
- A4 run 1 stopped at an app restart (2026-10-23) before writing output. Resumed from its saved transcript.
- A5 run 1 stopped at a network drop (API ENOTFOUND, about 18:47 IST 2026-10-23) before writing output. Resumed from its saved transcript.

## Correction loops
- Loop 1 (A5 run 1 INCOMPLETE: 4 MISSING, 2 CONTRADICTION, 3 FACTUAL, 8 STYLE). A2 results added R852-R864 (MISSING_FROM_STRUCTURED, incl. RL715 repayment 161.22 and the limited-review paragraphs). A2 concall added R325-R327. A3 results and A3 concall wrote loop-1 addenda (no new finding). A4 fixed M2, M3, M4, C1, C2, F1, F2, F3. A5 re-audit: all nine resolved; one new MISSING (M1b, stale A2 results count-test header).
- Loop 2: OPERATOR APPROVAL for a second iteration, relayed by the parent session local_75d06544-746e-4fb0-8462-bb8f7ecbb148 on 2026-10-24 ("complete them fully"; one second loop, then stop). A2 results fixed the count-test header (864 IDs, 242 line items, 40 zero-standing, 19 auditor rows, fulltext-vs-structured line). A5 loop-2 re-audit: COMPLETE. Open STYLE notes only: S4, S9, S10, S11.

## Input discipline
- No A2-A5 agent reported reading inputs/. The Notion digest (built by a Sonnet extraction subagent from the live fetch, verbatim copy only) was the only Notion input.
- A1 results left OCR intermediates in work/ (tejasnet_results_ocr*.txt, _body, _header, _gen.py); moved to the session scratchpad before the first commit. Not committed.
