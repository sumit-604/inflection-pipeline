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
| 1 | Gate 0 scorecard (resumed: E4 from AR notes, M2/M5/M9 peer sheets) | sonnet 5.5 | medium | n/a | n/a | n/a | n/a | 120,750 | 94s | 2 |
| 2 | Notes triple-pass, pass 1 of 3 (resumed over transcribed notes) | sonnet 5.5 | high | n/a | n/a | n/a | n/a | 199,035 | 287s | 2 |
| 2 | Notes triple-pass, pass 2 of 3 | sonnet 5.5 | high | n/a | n/a | n/a | n/a | 180,401 | 522s | 1 |
| 2 | Notes triple-pass, pass 3 of 3 (synthesis, B02) | sonnet 5.5 | high | n/a | n/a | n/a | n/a | 72,268 | 103s | 1 |
| 3 | AR backward deep dive | sonnet 5.5 | high | n/a | n/a | n/a | n/a | 424,227 | 963s | 1 |
| 4 | Business model decoder | sonnet 5.5 | medium | n/a | n/a | n/a | n/a | 151,378 | 313s | 1 |
| 5 | Communication and guidance (NO-CONCALL MODE, bounded) | sonnet 5.5 | high | n/a | n/a | n/a | n/a | 118,050 | 145s | 1 |
| 8 | Promoter and governance check (web; partial) | sonnet 5.5 | high | n/a | n/a | n/a | n/a | 176,078 | 493s | 1 |
