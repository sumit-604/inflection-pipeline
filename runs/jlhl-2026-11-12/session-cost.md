# SESSION COST LEDGER — JLHL 2026-11-12 (phase 1, via /step1)

Subagents ran through the desktop app's async Agent tool. It reports total
tokens and wall time per run; the input, cache-read, cache-write and output
split is not exposed, so those columns read n/a (never an estimate).

| # | stage | model | effort | in_tok | cache_read | cache_write | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | input validation + corpus repair (inline) | claude-fable-5-2 (orchestrator) | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 1 |
| 0 | stage-00-intake-check | claude-haiku-5-5 | medium | n/a | n/a | n/a | n/a | 114647 | 3m00s | 1 |
| 1 | gate 0 scorecard | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 123414 | 6m37s | 1 |
| 2 | notes triple-pass, pass 1 | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 229238 | 8m32s | 1 |
| 2 | notes triple-pass, pass 2 | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 215980 | 8m39s | 2 |
| 2 | notes triple-pass, pass 3 (consolidated) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 85529 | 1m58s | 3 |
| 3 | AR backward deep dive | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 459732 | 25m33s | 1 |
| 5 | concall analysis (3 transcripts) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 137580 | 6m29s | 1 |
| 8 | promoter background check (web) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 156538 | 8m41s | 1 |
