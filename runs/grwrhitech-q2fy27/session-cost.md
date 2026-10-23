# Session cost: GRWRHITECH Q2 FY27 /run-quarterly

ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations
GRWRHITECH | 2026-10-23 | results (+ embedded presentation pp20-43) | 43 | ~28,000 (A1 estimate) | >= 1,129,155 (A4 run 1, A4 loop 2 and A5 loop 2 NOT FOUND) | 2

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
| LOOP 2: A5 re-audit, attempt 2 | claude-opus-5-5 | NOT FOUND at write time | NOT FOUND | loop 2 |

Loop 2 approval: operator wrote "complete them fully" (2026-10-24), relayed by the coordinating session.

Base run (known rows): 733,232. Loop 1: 396,023.

COST CHECK. A2 (114,150) came in above A1 (100,104). Diagnosed: A2's transcript shows no read under inputs/ and no PDF access. A1's structured file is 143 KB against a 103 KB fulltext (1,292 script-generated NUMBER rows), and A2 must read it whole. No discipline breach.

Change that would make the next run cheaper: A1 should not emit one NUMBER row per table cell on a 43-page filing; table rows as one row each would cut the structured file below the fulltext and bring A2 under A1.
