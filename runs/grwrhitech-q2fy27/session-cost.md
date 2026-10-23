# Session cost: GRWRHITECH Q2 FY27 /run-quarterly

ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations
GRWRHITECH | 2026-10-23 | results (+ embedded presentation pp20-43) | 43 | ~28,000 (A1 estimate) | >= 1,400,275 results pass (A4 run 1, A4 loop 2, stalled A5 attempt NOT FOUND); >= 3,646,809 with the concall pass | 2 (results) + 2 (merged)

| agent | model | total_tok | wall | run# |
|---|---|---|---|---|
| A1 extractor (results) | claude-sonnet-5-5 | 100,104 | 5m 23s | 1 |
| A2 enumerator (results) | claude-sonnet-5-5 | 114,150 | 6m 34s | 1 |
| A3 forensics (results) | claude-opus-5-5 | 245,049 | 13m 11s | 1 |
| A4 analyst | claude-opus-5-5 | NOT FOUND (machine restart; completion record lost, output on disk) | NOT FOUND | 1 |
| A5 adversary | claude-opus-5-5 | 273,929 | 17m 55s | 1 |
| LOOP 1: A4 correction | claude-opus-5-5 | 158,804 | 8m 54s | loop 1 |
| LOOP 1: A5 re-audit | claude-opus-5-5 | 237,219 | 14m 16s | loop 1 |

| LOOP 2: A4 correction (F3) | claude-opus-5-5 | NOT FOUND (restart; completion record lost, output on disk) | NOT FOUND | loop 2 |
| LOOP 2: A5 re-audit, attempt 1 (stalled, mechanical) | claude-opus-5-5 | NOT FOUND | >600s stall | loop 2 |
| LOOP 2: A5 re-audit, attempt 2 | claude-opus-5-5 | 271,020 | 16m 19s | loop 2 |


CONCALL PASS (ASR transcript, 842 lines)
| agent | model | total_tok | wall | run# |
|---|---|---|---|---|
| A1 extractor (concall) | claude-sonnet-5-5 | 93,948 | 4m 40s | 1 |
| A2 enumerator (concall) | claude-sonnet-5-5 | 50,088 | 1m 41s | 1 |
| A3 forensics (concall) | claude-opus-5-5 | 128,486 | 5m 35s | 1 |
| A4 merged (Role 4 + Role 5) | claude-opus-5-5 | 431,540 | 30m 24s | 1 |
| A5 merged | claude-opus-5-5 | 376,893 | 20m 36s | 1 |
| MERGED LOOP 1: A4 | claude-opus-5-5 | 257,180 | 31m 39s | loop 1 |
| MERGED LOOP 1: A5 | claude-opus-5-5 | 338,840 | 13m 51s | loop 1 |
| MERGED LOOP 2: A4 | claude-opus-5-5 | 262,336 | 13m 48s | loop 2 |
| MERGED LOOP 2: A5 | claude-opus-5-5 | 307,223 | 14m 55s | loop 2 |
| ASR (faster-whisper small int8, local CPU) | n/a | 0 | 23m 15s | 1 |

Concall pass: base 1,080,955; loops 1,165,579 (2 iterations). Grand total known tokens, whole run: 3,646,809 (plus the NOT FOUND rows above).

Loop 2 approval: operator wrote "complete them fully" (2026-10-24), relayed by the coordinating session.

Base run (known rows): 733,232. Loop 1: 396,023. Loop 2 (known): 271,020.

COST CHECK. A2 (114,150) came in above A1 (100,104). Diagnosed: A2's transcript shows no read under inputs/ and no PDF access. A1's structured file is 143 KB against a 103 KB fulltext (1,292 script-generated NUMBER rows), and A2 must read it whole. No discipline breach.

Change that would make the next run cheaper: A1 should not emit one NUMBER row per table cell on a 43-page filing; table rows as one row each would cut the structured file below the fulltext and bring A2 under A1.
