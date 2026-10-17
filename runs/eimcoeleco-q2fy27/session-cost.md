# Session cost: EIMCOELECO Q2 FY27 (/run-quarterly, 2026-10-17)

## DOCUMENT REVIEW summary row

| ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations |
|---|---|---|---|---|---|---|
| EIMCOELECO | 2026-10-17 | results + presentation + pressrelease | 54 (11 + 39 + 4) | ~22,379 (bytes/4: results 34,973 B ~8,743; presentation 46,887 B ~11,722; pressrelease 7,654 B ~1,914) | 2,468,930 | 2 |

## Per-agent ledger (one row per subagent run; figures from each task notification's subagent_tokens)

| agent | model | total_tok | wall | run# |
|---|---|---|---|---|
| A1-results | claude-sonnet-5-5 | 76,253 | 371 s | 1 |
| A1-presentation | claude-sonnet-5-5 | 102,461 | 423 s | 1 |
| A1-pressrelease | claude-sonnet-5-5 | 50,825 | 111 s | 1 |
| A2-results | claude-sonnet-5-5 | 87,736 | 206 s | 1 |
| A2-presentation | claude-sonnet-5-5 | 60,599 | 166 s | 1 |
| A2-pressrelease | claude-sonnet-5-5 | 36,216 | 47 s | 1 |
| A3-results | claude-opus-5-5 | 119,374 | 436 s | 1 |
| A3-presentation | claude-opus-5-5 | 157,716 | 417 s | 1 |
| A3-pressrelease | claude-opus-5-5 | 59,064 | 193 s | 1 |
| A4 | claude-opus-5-5 | 304,325 | 826 s | 1 |
| A5 | claude-opus-5-5 | 260,100 | 927 s | 1 |
| **Base run subtotal** | | **1,314,669** | | |

## Correction loop 1 (logged separately)

| agent | model | total_tok | wall | run# |
|---|---|---|---|---|
| LOOP1-A4-fix | claude-opus-5-5 | 376,418 | 380 s | loop 1 |
| LOOP1-A5-reaudit | claude-opus-5-5 | 333,210 | 1,163 s | loop 1 |
| **Loop 1 subtotal** (iterations: 1) | | **709,628** | | |

## Correction loop 2 (logged separately; operator ruling 2026-10-17 approved one second loop)

| agent | model | total_tok | wall | run# |
|---|---|---|---|---|
| LOOP2-A4-fix (fresh, mechanical re-run after laptop restart) | claude-opus-5-5 | 149,134 | 507 s | loop 2 |
| LOOP2-A5-reaudit (fresh) | claude-opus-5-5 | 295,499 | 1,066 s | loop 2 |
| **Loop 2 subtotal** | | **444,633** | | |

**total_run_tok = 2,468,930** (base 1,314,669 + loop 1 709,628 + loop 2 444,633).

## Notes
- LOOP1-A4-fix is a resume of the run-1 A4 agent (SendMessage); its figure re-counts the prior context, as in the TATACOMM ledger. LOOP1-A5-reaudit is a fresh agent.
- Cost check: presentation A2 60,599 < A1 102,461 pass; pressrelease A2 36,216 < A1 50,825 pass. Results A2 87,736 > A1 76,253 FAIL, diagnosed structural (A1 wrote the 47,415 B structured file by script, so A1 never held it; no source re-ingestion). See work/run-log.md.
- A5 INCOMPLETE after loop 2 (F04, M05, M06 open). No third loop by operator ruling; items flagged in the review "OPEN ITEMS AT CLOSE" section.
- The first loop 2 A4 run was killed by the laptop restart before any write. Its cost is NOT FOUND and is not in the total. The re-run is mechanical and does not count against the loop cap.
- Loop 2 used fresh agents, not resumes: the fresh A4 fix cost 149,134 against 376,418 for the loop 1 resume.
- First attempt of this session crashed before creating a run folder; it left no recorded cost.
- Orchestrator session's own tokens are not in total_run_tok.
- Fresh tokens, re-read tokens, re-read multiple: NOT FOUND (task notifications report totals only, no cache split).
- Parallelism: at most 2 subagents at once (batch load rule); never exceeded.
