# Session cost: AYE Q2 FY27 quarterly review (2026-10-23)

## Document review summary rows
ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations
AYE | 2026-10-23 | results | 24 | NOT FOUND (fulltext 123,299 chars; tokenizer count not run) | see run total | 1
AYE | 2026-10-23 | presentation | 44 | NOT FOUND (fulltext 76,614 chars) | see run total | 1
AYE | 2026-10-23 | concall (ASR text, 846 lines, 8 audio segments) | 8 | NOT FOUND (fulltext 65,423 chars) | see run total | 1
Run total (all subagents, base + loop): 2,318,946 tok. Base run 2,071,623 tok; correction loop 247,323 tok (1 iteration).

## Per-agent ledger (subagent totals as reported by the harness)
agent | doc | model | total_tok | wall | run#
A1 | results+presentation (killed by machine restart, no output used) | claude-sonnet-5-5 | NOT FOUND | - | 0
A1 | results | claude-sonnet-5-5 | 128,088 | 439s | 1
A2 | results | claude-sonnet-5-5 | 62,429 | 235s | 1
A3 | results | claude-opus-5-5 | 213,207 | 557s | 1
A1 | presentation | claude-sonnet-5-5 | 108,014 | 379s | 1
A2 | presentation | claude-sonnet-5-5 | 39,502 | 103s | 1
A3 | presentation | claude-opus-5-5 | 252,207 | 829s | 1
A1 | concall | claude-sonnet-5-5 | 81,269 | 211s | 1
A2 | concall | claude-sonnet-5-5 | 65,488 | 216s | 1
A3 | concall | claude-opus-5-5 | 165,414 | 580s | 1
A4 | merged | claude-opus-5-5 | 571,401 | 2,108s | 1
A5 | audit | claude-opus-5-5 | 384,604 | 1,109s | 1

## Correction loop (iteration 1 of 1; A5 INCOMPLETE -> fixes -> A5 still INCOMPLETE; second loop NOT run, operator decision)
agent | doc | model | total_tok | wall | run#
A2 | ledger fixes (results + presentation) | claude-sonnet-5-5 | 40,618 | 182s | loop1
A4 | graft ADV-1..3 + style (cumulative 669,629 minus base 571,401) | claude-opus-5-5 | 98,228 | 617s | loop1
A5 | re-audit (cumulative 493,081 minus base 384,604) | claude-opus-5-5 | 108,477 | 412s | loop1

## Cost checks
- A2 below A1 on every document: results 62,429 < 128,088; presentation 39,502 < 108,014; concall 65,488 < 81,269. PASS.
- No A2-A5 agent reported reading inputs/. Input discipline held.

## Non-agent work (orchestrator, local)
- Concall audio transcribed locally: faster-whisper "small", int8, CPU, 10-minute resumable chunks; 4,267 s audio in 5,441 s wall (machine shared with other reviews). Two earlier attempts failed (PyAV DLL blocked by App Control; out-of-memory on a single 71-minute array).
- Orchestrator session tokens: NOT FOUND (not exposed to the session).

## Prompt-cache figures
fresh tokens: NOT FOUND | re-read tokens: NOT FOUND | re-read multiple: NOT FOUND (the harness did not expose a cache split for this run)
