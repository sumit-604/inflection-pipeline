# Session cost: NETWEB Q2 FY27 /run-quarterly

ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations
--- | --- | --- | --- | --- | --- | ---
NETWEB | 2026-10-28 | results (scan OCR) + presentation + strategy + pressrelease + concall (ASR) | 7 + 22 + 28 + 3 + 6 audio chunks (754 lines) | NOT FOUND (no tokenizer run; fulltext 20,581 / 58,239 / 69,192 / 10,297 / 57,820 bytes; 3,259 / 5,671 / 5,395 / 1,285 / 9,293 words) | 2,394,858 (base 2,157,847 + loop 237,011) | 1

Note on token figures. "total_tok" is the subagent_tokens value the harness reported at each hand-back. For a resumed agent the harness reports the agent's running total; the rows below show the increment of the resumed run, with the running total in brackets. total_run_tok sums the subagent rows only. The orchestrator session's own tokens are not counted (no harness figure).

## Per-agent ledger (base run)

agent | doc | model | total_tok | wall | run#
--- | --- | --- | --- | --- | ---
A1 extractor | results | claude-sonnet-5-5 | 82,345 | 354 s | 1
A1 extractor | results | claude-sonnet-5-5 | 12,333 (running 94,678) | 48 s | 1a mechanical follow-up: p1 image read (conclusion time 2:40 PM, CS name), R429 added (A2 MISSING_FROM_STRUCTURED); not a correction loop
A1 extractor | presentation | claude-sonnet-5-5 | 84,436 | 315 s | 1
A1 extractor | strategy | claude-sonnet-5-5 | 76,557 | 259 s | 1
A1 extractor | pressrelease | claude-sonnet-5-5 | 52,094 | 207 s | 1
A1 extractor | concall | claude-sonnet-5-5 | 80,772 | 217 s | 1
A2 enumerator | results | claude-sonnet-5-5 | 83,217 | 238 s | 1 (cost check: 1% above A1 82,345; diagnosed, no source access; A1 was script-assisted)
A2 enumerator | presentation | claude-sonnet-5-5 | 65,526 | 240 s | 1
A2 enumerator | strategy | claude-sonnet-5-5 | 58,766 | 206 s | 1
A2 enumerator | pressrelease | claude-sonnet-5-5 | 48,636 | 109 s | 1
A2 enumerator | concall | claude-sonnet-5-5 | 47,816 | 120 s | 1
A3 forensics | results | claude-opus-5-5 | 123,161 | 392 s | 1
A3 forensics | presentation | claude-opus-5-5 | 156,319 | 591 s | 1
A3 forensics | strategy | claude-opus-5-5 | 139,407 | 531 s | 1
A3 forensics | pressrelease | claude-opus-5-5 | 83,115 | 300 s | 1
A3 forensics | concall | claude-opus-5-5 | 140,070 | 486 s | 1
A4 analyst | merged | claude-opus-5-5 | 460,057 | 1,269 s | 1
A5 adversary | merged | claude-opus-5-5 | 363,220 | 1,237 s | 1 -> INCOMPLETE (2 FACTUAL, 6 MISSING, 7 STYLE)

Subtotals: A1 388,537 | A2 303,961 | A3 642,072 | A4 460,057 | A5 363,220 | base 2,157,847.

## Correction loop 1 (the one default loop; A5 FACTUAL and MISSING items)

agent | doc | model | total_tok | wall | run#
--- | --- | --- | --- | --- | ---
A4 analyst | merged | claude-opus-5-5 | 149,425 (running 609,482) | 931 s | L1 (F1, F2, M1-M6; S1-S4, S7)
A5 adversary | merged | claude-opus-5-5 | 87,586 (running 450,806) | 319 s | L1 re-audit -> COMPLETE (style N1-N3, S5 logged)

Loop subtotal: 237,011. loop_iterations: 1.

## Non-agent work (orchestrator)

- Checkout guard, toolchain and protocol checks, document classing, run folder, SOURCES.md.
- Notion page read live once (117,056 characters); excerpts saved to work/notion_context_2026-10-26.md and work/notion_checklist_2026-10-26.md. No Notion write.
- Mechanical ID-reconciliation addendum appended to work/ledger_results_netweb_q2fy27.md after the A1 follow-up.
- operator-brief.md and notion-payload.md written by the orchestrator from the review; no agent re-run.
- Wall clock: about 10:00 to 11:30 IST.

## What dragged this run

- Five documents for one name, two of them decks that repeat each other. A3 on the strategy deck and the earnings deck cost 295,726 tokens together and overlapped on ratios, QIP and concentration.
- A4 is the largest single cost (609,482 including the loop). Its input is five extracts, five ledgers and five forensics files plus a 55 KB Notion excerpt.
- The loop fixed grafts that A4 could have caught: two uncited extract clusters and three bear counters.

Change that would make the next run cheaper: run the strategy deck as a DOCUMENT REVIEW only when it differs from the prior quarter's strategy deck; otherwise pass it to A4 as a reference extract without its own A2/A3 chain.
