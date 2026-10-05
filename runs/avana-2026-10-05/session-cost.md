# SESSION COST LEDGER — AVANA 2026-10-05 (Phase 1, /step1 intake)

Per-stage token ledger. One line per subagent run, from the subagent result
metadata. in_tok / cache splits are written n/a where the result does not
expose them (never estimated).

| # | stage | model | effort | in_tok | cache_read | cache_write | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|------------|-------------|---------|-----------|------|------|
| 0 | input validation (orchestrator inline) | opus 5.5 (orchestrator) | session | n/a | n/a | n/a | n/a | n/a | n/a | 1 |
| 1 | Gate 0 scorecard | sonnet 5.5 | medium | n/a | n/a | n/a | n/a | 97,189 | 237s | 1 |
| 2 | Notes triple-pass, pass 1 of 3 (partial: AR notes image-only) | sonnet 5.5 | high | n/a | n/a | n/a | n/a | 117,640 | 238s | 1 |
| pre | corpus: transcribe AR pp.2-4, 99-112 page images | sonnet 5.5 | default | n/a | n/a | n/a | n/a | 154,825 | 136s | 1 |
| pre | corpus: transcribe AR pp.113-127 + Reg 31(4) page images | sonnet 5.5 | default | n/a | n/a | n/a | n/a | 159,354 | 132s | 1 |
