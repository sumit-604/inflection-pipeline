# Q2 FY27 watchlist batch, 19-Oct-2026 (overnight, operator asleep)

Request (operator, 19-Oct ~22:45 IST): from the screener.in watchlist "Today" list, download today's results press releases, investor presentations and other press releases, transcribe the concall recordings, and analyse per framework.

| Name | Today's filings held | Call | Run folder |
|---|---|---|---|
| Kross Ltd | results (17-Oct), press release, presentation, recording notice | recording 49.5 min, machine transcript | runs/kross-q2fy27 |
| HFCL | results + press release (one file), presentation, monitoring agency report, recording notice | recording 82.9 min, machine transcript | runs/hfcl-q2fy27 |
| Tatva Chintan | results (scan), updated presentation (and original), call cancellation notice | call CANCELLED by company, no recording | runs/tatva-q2fy27 |
| GOCL Corpn. (HELD) | results with merger-scheme update | none announced | runs/gocl-q2fy27 |
| Gallantt Ispat L | results (NSE 20-Oct 00:16; found 01:49) | call intimated 14-Oct, not held yet | runs/gallantt-q2fy27 |
| Quality Power El | EGM outcome (19-Oct), Turkiye PCS notice (17-Oct) | none (no results) | runs/qpower-q2fy27 (document review) |

Files on disk: C:/ConcallPipeline/Daily Concall Intelligence/Q2 FY27 Results/17-22 folders.

## Token ledger (from each run's session-cost.md total_run_tok)

| Name | Run folder | total_run_tok | Loops | A5 verdict | Commit |
|---|---|---|---|---|---|
| Quality Power | runs/qpower-q2fy27 | 1,310,123 | 2 | COMPLETE | f24e676b |
| GOCL | runs/gocl-q2fy27 | 1,606,834 | 1 | COMPLETE | 1aedddb1 |
| Tatva Chintan | runs/tatva-q2fy27 | 2,791,647 | 1 | COMPLETE | e034d92c |
| Kross | runs/kross-q2fy27 | 6,341,338 | R4: 2, R5: 2 | COMPLETE | 119dc70a |
| Gallantt Ispat | runs/gallantt-q2fy27 | 1,700,250 | 2 | COMPLETE | 2c7183ef |
| HFCL | runs/hfcl-q2fy27 | 6,115,445 (floor, 1 row ND) | R4: 2, R5: 2 | COMPLETE | 6d354bee + batch commit |
| TOTAL, 6 names | | 19,865,637 (floor) | | 6 COMPLETE | |

Caveat: a resumed agent's token figure was summed as additive (cyientdlm 2026-10-17 lesson). Several resumed A4 figures rise monotonically (Kross 556k, 633k, 689k), which suggests they may be cumulative; if so, Kross and HFCL totals overstate. Orchestrator tokens are not included.

Overnight problems:
- RAM starvation (5.9 GB): whisper medium.en took ~45-60 min per 10-min chunk; switched to small.en at 00:42. The first runner's shell survived the kill and ran an HFCL medium.en job in parallel with the small.en job until 02:58, so HFCL chunks are a mix (per-chunk model not recorded). Lesson: kill the runner shell, not only the python child.
- Garbled hidden OCR text layers on most results filings: statement pages rendered with pdftoppm and read from images (tesseract absent).
- A stray scratchpad script (HFCL a2.py) was re-run twice by other agents; ledger verified intact; script renamed.
- The orchestrator session ended twice (after ~04:08 and ~06:20); two audit agents died with it and were re-run.
