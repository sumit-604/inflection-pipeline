# Session cost: ADOR Q2 FY27 /run-quarterly

ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations
--- | --- | --- | --- | --- | --- | ---
ADOR | 2026-10-23/24 | results + presentation + concall (ASR) | 12 + 29 + 9 chunks | NOT FOUND (no tokenizer run; fulltext 46,129 / 55,035 / 46,640 bytes; 6,991 / 4,550 / 8,261 words) | NOT FOUND as an exact sum (see note) | 2

Note on token figures. "total_tok" below is the subagent_tokens value the harness reported at each hand-back. For a resumed agent it is the agent's running context size, not the increment of that run. Rows marked "self-report" had no harness figure because an app restart or network drop cut the completion record; the figure is the agent's own statement. The increment of a resumed run is the difference from that agent's previous row.

## Per-agent ledger

agent | doc | model | total_tok | wall | run#
--- | --- | --- | --- | --- | ---
A1 extractor | results | claude-sonnet-5-5 | 108,488 | 906 s | 1
A1 extractor | results | claude-sonnet-5-5 | 111,410 | 41 s | 1a fix R744, R893, R895 (A2 flag)
A1 extractor | results | claude-sonnet-5-5 | 113,195 | 62 s | 1b fix R083, R272 (A3 flag)
A2 enumerator | results | claude-sonnet-5-5 | 80,583 | 50 s (resume after restart) | 1 (mechanical resume, not counted)
A3 forensics | results | claude-opus-5-5 | ~155k self-report | NOT FOUND | 1
A1 extractor | presentation | claude-sonnet-5-5 | 82,016 | 854 s | 1
A2 enumerator | presentation | claude-sonnet-5-5 | 39,630 | 76 s | 1
A3 forensics | presentation | claude-opus-5-5 | 143,638 | 372 s | 1
A1 extractor | concall | claude-sonnet-5-5 | 101,832 | 374 s | 1
A2 enumerator | concall | claude-sonnet-5-5 | 51,618 | 92 s | 1
A3 forensics | concall | claude-opus-5-5 | 156,316 | 375 s | 1
A4 analyst | merged | claude-opus-5-5 | 360,798 | 873 s | 1
A5 adversary | merged | claude-opus-5-5 | ~0.36M self-report | NOT FOUND | 1 -> INCOMPLETE

## Correction loop 1 (A5 loop-0 findings)

agent | doc | model | total_tok | wall | run#
--- | --- | --- | --- | --- | ---
A1 extractor | results | claude-sonnet-5-5 | 120,755 | 89 s | L1 (R901-R916, R832)
A1 extractor | presentation | claude-sonnet-5-5 | 84,093 | 17 s | L1 (R471, anchors)
A1 extractor | concall | claude-sonnet-5-5 | 104,869 | 27 s | L1 (R292-R293)
A2 enumerator | results | claude-sonnet-5-5 | 84,909 | 31 s | L1
A2 enumerator | presentation | claude-sonnet-5-5 | 43,092 | 29 s | L1
A2 enumerator | concall | claude-sonnet-5-5 | 54,287 | 27 s | L1
A3 forensics | concall | claude-opus-5-5 | 195,838 | 252 s | L1 (C-A3-15, C-A3-01)
A4 analyst | merged | claude-opus-5-5 | 456,664 | 911 s | L1
A5 adversary | merged | claude-opus-5-5 | 493,795 | 485 s | L1 -> INCOMPLETE

## Correction loop 2 (operator standing approval 2026-10-24, recorded in work/run-log.md)

agent | doc | model | total_tok | wall | run#
--- | --- | --- | --- | --- | ---
A1 extractor | results | claude-sonnet-5-5 | 123,855 | 28 s | L2 (R917-R926)
A2 enumerator | results | claude-sonnet-5-5 | 87,695 | 16 s | L2
A4 analyst | merged | claude-opus-5-5 | 535,152 | 836 s | L2
A5 adversary | merged | claude-opus-5-5 | 551,078 | 276 s | L2 -> COMPLETE

## Non-agent work (orchestrator)
- Fetch: BSE API + attachments, company audio (resumed after a truncated first download), site deck (same MD5 as BSE deck).
- ASR: faster-whisper small int8, 9 x 5-min chunks, about 20 min wall at BelowNormal priority, after the Supreme Power ASR job ended.

## Close-out
- fresh tokens: NOT FOUND (no session counter read)
- re-read tokens: NOT FOUND
- re-read multiple: NOT FOUND
- Discipline: no A2-A5 agent reported reading inputs/.
- Change that would make the next run cheaper: have A1 diff its own VERIFICATION NOTES against its structured rows before hand-back; three OCR cell errors (R744, R083, R272) and one more in loop 1 (R832) cost four extra A1 resumes.
