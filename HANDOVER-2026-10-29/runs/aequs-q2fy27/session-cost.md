# session-cost.md — AEQUS q2fy27 (/run-quarterly, batch q2fy27-1028, 28-Oct-2026)

DOCUMENT REVIEW summary row:

`ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations`
`AEQUS | 2026-10-28 | results + presentation + pressrelease + concall (ASR) | 16 + 33 + 5 + 757 lines | ~53,100 (212,380 chars of A1 fulltext / 4) | 2,050,757 | 1`

`a1_extracted_text_tok` is a character-count estimate (chars / 4); no tokenizer ran. Per document: results 63,433 chars, deck 80,059, press release 12,233, concall 56,655.

## Per-agent ledger (subagent_tokens as reported by the harness; wall = duration)

| Agent | Doc | Model | total_tok | wall | run# |
|---|---|---|---|---|---|
| A1 | results | claude-sonnet-5-5 | 129,364 | 444 s | 1 |
| A1 | presentation | claude-sonnet-5-5 | 97,400 | 337 s | 1 |
| A1 | pressrelease | claude-sonnet-5-5 | 64,386 | 247 s | 1 |
| A1 | concall (ASR .txt) | claude-sonnet-5-5 | 81,244 | 230 s | 1 |
| A2 | results | claude-sonnet-5-5 | 133,902 | 490 s | 1 |
| A2 | presentation | claude-sonnet-5-5 | 41,726 | 121 s | 1 |
| A2 | pressrelease | claude-sonnet-5-5 | 40,399 | 71 s | 1 |
| A2 | concall | claude-sonnet-5-5 | 54,762 | 118 s | 1 |
| A3 | results | claude-opus-5-5 | 148,447 | 421 s | 1 |
| A3 | presentation | claude-opus-5-5 | 134,968 | 411 s | 1 |
| A3 | pressrelease | claude-opus-5-5 | 80,205 | 316 s | 1 |
| A3 | concall | claude-opus-5-5 | 118,851 | 347 s | 1 |
| A4 | merged (4 docs) | claude-opus-5-5 | 415,534 | 1,318 s | 1 |
| A5 | audit | claude-opus-5-5 | 348,765 | 1,129 s | 1 |
| **Base run subtotal** | | | **1,889,953** | | |

## Errata and correction loop (logged apart from the base run)

| Agent | Doc | Model | total_tok | wall | iteration |
|---|---|---|---|---|---|
| A1 errata (pre-A4, raised by deck A3) | presentation | claude-sonnet-5-5 | 6,152 | 36 s | errata |
| A3 loop 1 (A5 M1, M2) | presentation | claude-opus-5-5 | 24,307 | 170 s | 1 |
| A4 loop 1 (A5 F1, M1, M2, M3, C1) | merged | claude-opus-5-5 | 80,689 | 505 s | 1 |
| A5 re-audit loop 1 | audit | claude-opus-5-5 | 49,656 | 224 s | 1 |
| **Errata + loop subtotal** | | | **160,804** | | |

Errata and loop rows are deltas: each agent was resumed, and the figure is its cumulative total less the prior report.

**total_run_tok (all subagents): 2,050,757.**

## Notes

- Cost check: A2 results (133,902) came in 3.5% above A1 results (129,364). Diagnosed in work/run-log.md: no source re-ingestion; the excess is the orchestrator-added tie-out task (346 arithmetic checks). Every other A2 sits below its A1.
- A1 results was the costliest A1: nine image-only statement pages, OCR failed on the tables, and the agent transcribed them from renders.
- A4 is 20% of the run on its own (415,534 base + 80,689 loop).
- Notion write done inline on 29-Oct-2026 after operator approval (1 property update, 15 inserts; no subagent, no token row). Payload record in notion-payload.md.

## Orchestrator session

- Context in use at close-out: 254,123 tokens of 1,000,000 (25%), read from the app's usage tool.
- Fresh tokens: NOT FOUND. Re-read (cache-read) tokens: NOT FOUND. Re-read multiple: NOT FOUND. The session cannot read its own billing split; the coordinator can take it from the account usage view.
