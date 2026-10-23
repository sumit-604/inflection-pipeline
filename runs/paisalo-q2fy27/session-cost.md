# Session cost: PAISALO Q2 FY27 (/run-quarterly), 2026-10-23

## Document review summary rows
ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations
PAISALO | 2026-10-23 | results | 10 | NOT FOUND (not measured; fulltext 114,905 chars) | 2,217,763 (all three docs, A4, A5, loop, Notion copy) | 1
PAISALO | 2026-10-23 | presentation | 42 | NOT FOUND (not measured; fulltext 77,350 chars) | (in run total) | 1
PAISALO | 2026-10-23 | concall (ASR) | 4 logical (10-min blocks; 681 lines) | NOT FOUND (not measured; fulltext 46,755 chars) | (in run total) | 1

total_run_tok excluding the Notion copy subagent: 2,059,441.

## Per-agent ledger (subagent_tokens as reported by the harness)
agent | model | total_tok | wall | run#
A1 results (incl. orchestrator-requested layout fix, same agent) | claude-sonnet-5-5 | 109,595 | 432.8 s (fix leg); 196.0 s first leg | 1
A2 results | claude-sonnet-5-5 | 122,525 | 437.2 s | 1
A3 results | claude-opus-5-5 | 289,267 | 758.5 s | 1
A1 presentation | claude-sonnet-5-5 | 125,244 | 656.7 s | 1
A2 presentation | claude-sonnet-5-5 | 42,054 | 175.9 s | 1
A3 presentation | claude-opus-5-5 | 253,340 | 881.6 s | 1
A1 concall | claude-sonnet-5-5 | 84,005 | 243.6 s | 1
A2 concall | claude-sonnet-5-5 | 57,206 | 141.2 s | 1
A3 concall | claude-opus-5-5 | 168,032 | 536.7 s | 1
A4 analyst | claude-opus-5-5 | 423,471 | 1,533.8 s | 1
A5 adversary (first audit; includes a leg cut off by a machine restart, resumed mechanically) | claude-opus-5-5 | 235,940 | 973.9 s (resumed leg) | 1
Notion field copy (copy-only, general-purpose) | sonnet | 158,322 | 266.8 s | 1

## Correction loop (logged separately)
agent | model | total_tok | wall | run#
A4 loop fix (F1, F2, M1, M2; S2, S4) | claude-opus-5-5 | 88,511 | 596.3 s | loop 1
A5 re-audit | claude-opus-5-5 | 60,251 | 292.5 s | loop 1
Loop subtotal: 148,762 tok. loop_iterations: 1. Result: COMPLETE.

## Local compute (not tokens)
ASR: faster-whisper small.en int8, CPU, 4 x 600 s chunks of 2,229 s audio; about 2 h wall on a memory-starved machine (free RAM about 111 MB at check; three ASR jobs ran across sessions).

## Notes
- COST CHECK: A2 results (122,525) came in above A1 results (109,595). Diagnosed: no source read; the 1,372-row structured file was read in full. See work/run_log.md.
- Two machine restarts during the run; no finished step was redone.

## Orchestrator session
fresh tokens: NOT FOUND (not exposed to the session)
re-read tokens: NOT FOUND
re-read multiple: NOT FOUND
