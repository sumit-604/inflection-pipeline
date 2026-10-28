# session-cost — SONACOMS Q2 FY27 (/run-quarterly, 2026-10-28)

DOCUMENT REVIEW summary row (shared baseline):

`ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations`

`SONACOMS | 2026-10-28 | results+presentation+pressrelease+concall(ASR) | 16+36+4 pages + 921 transcript lines | ~53,400 (fulltext chars / 4: results 19,600; deck 14,500; PR 2,600; call 16,700) | 3,550,129 | 1`

Token figures are the harness `subagent_tokens` per agent run. Loop rows are resumed agents (SendMessage); their figure is what the harness reported for the resumed run and may include the re-read of the agent's own prior context. The orchestrator session's own tokens are not in this ledger (NOT FOUND: the harness gives no per-session figure in-session).

## Per-agent ledger, base run

| Agent | Doc | Model | total_tok | Wall | Run # | Gate / note |
|---|---|---|---|---|---|---|
| A1 | pressrelease | claude-sonnet-5-5 | 68,132 | 190.7 s | 1 | PASS 4/4 pages, R001-R127 |
| A1 | concall (ASR .txt) | claude-sonnet-5-5 | 82,557 | 239.7 s | 1 | PASS 921/921 lines, R001-R336 |
| A1 | presentation | claude-sonnet-5-5 | 76,941 | 249.0 s | 1 | PASS 36/36 pages, R001-R317 |
| A1 | results | claude-sonnet-5-5 | 145,450 | 557.7 s | 1 | PASS 16/16 pages, R001-R1098; 10 image-only statement pages rendered and transcribed |
| A2 | pressrelease | claude-sonnet-5-5 | 44,379 | 99.6 s | 1 | PASS 127/127; below A1 |
| A2 | presentation | claude-sonnet-5-5 | 65,658 | 186.8 s | 1 | PASS 317/317; below A1 (count test later found circular by A5) |
| A2 | concall | claude-sonnet-5-5 | 108,970 | 434.4 s | 1 | PASS 336/336 + M01-M09; ABOVE A1 (82,557): orchestrator told it to sweep the full fulltext; no source access |
| A2 | results | claude-sonnet-5-5 | 92,934 | 290.2 s | 1 | PASS 1098/1098; below A1 |
| A3 | pressrelease | claude-opus-5-5 | 104,249 | 330.4 s | 1 | PASS 17/17, 17 findings |
| A3 | presentation | claude-opus-5-5 | 171,737 | 567.1 s | 1 | PASS 17/17, 25 findings |
| A3 | concall | claude-opus-5-5 | 217,038 | 649.2 s | 1 | PASS 17/17, 28 findings |
| A3 | results | claude-opus-5-5 | 254,564 | 669.8 s | 1 | PASS 17/17, 28 findings |
| A4 | merged (4 docs) | claude-opus-5-5 | 415,687 | 1,033.3 s | 1 | PROCEED WITH FLAGS; 24 questions |
| A5 | audit | claude-opus-5-5 | 377,917 | 1,116.9 s | 1 | INCOMPLETE (M1, M2, F1, F2, C1) |
| **Base subtotal** | | | **2,226,213** | | | |

## Correction loop ledger (iteration 1 of 1)

| Agent | Doc | Model | total_tok | Wall | Run # | Note |
|---|---|---|---|---|---|---|
| A2 | presentation (resumed) | claude-sonnet-5-5 | 78,603 | 79.2 s | loop 1 | M01-M15 added; count test with fulltext sweep |
| A3 | presentation addendum (resumed) | claude-opus-5-5 | 199,584 | 173.0 s | loop 1 | M01-M15 confirmed; no finding changed |
| A4 | patch (resumed) | claude-opus-5-5 | 537,298 | 647.5 s | loop 1 | M2, F1, F2, C1 fixed; whole-file rewrite (agent has no Edit tool) |
| A5 | re-audit (resumed) | claude-opus-5-5 | 508,431 | 466.8 s | loop 1 | COMPLETE; 7 style notes |
| **Loop subtotal** | | | **1,323,916** | | | |

**total_run_tok = 2,226,213 + 1,323,916 = 3,550,129.** Loop share 37.3%.

## By model

| Model | Runs | Tokens |
|---|---|---|
| claude-sonnet-5-5 | 9 | 763,624 |
| claude-opus-5-5 | 9 | 2,786,505 |

## What drove cost

- Four documents, one of them a 64-minute call transcript. The memory note puts a name at about 2.3M tokens; this run is 3.55M, of which 1.32M is the loop.
- The loop's resumed A4 and A5 carry their whole earlier context. A fresh, narrow patch agent may cost less than resuming a 400k-context agent. Not tested.
- A4 re-wrote the 1,190-line review because its agent file grants Read, Grep, Write only (no Edit). Each patch loop therefore pays a full rewrite plus a full re-audit of drift.
- The A2 deck count test counted structured rows against themselves. That let 15 deck units through to A5 and caused most of the loop.
- Results statement pages had no text layer. A1 rendered and transcribed ten pages by eye (145k, the largest A1).

## Cache and re-read

- Fresh tokens: NOT FOUND (the harness reports only a total per subagent run).
- Re-read tokens: NOT FOUND.
- Re-read multiple: NOT FOUND. Subagent prompt cache TTL is 1h (.claude/settings.json); the resumed loop agents ran 25-70 minutes after their first run.
