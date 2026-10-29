---
name: project-quarterly-batch-capacity
description: "Q2 FY27 results-season batch (Oct 2026): this machine runs only 3-4 parallel /run-quarterly sessions; cost ~2.3M subagent tokens per name"
metadata:
  node_type: memory
  type: project
  originSessionId: 10a090db-5174-435e-96c4-ad3b821698f6
  modified: 2026-10-24T01:51:43.662Z
---

Q2 FY27 batch, 23-24 Oct 2026: 13 names via one session per company. The machine has 6 GB RAM.
Starting 14 sessions at once failed: 8 never started (timeouts, worktree checkout errors), so retries created second sessions; operator later restarted the failed first ones too, which duplicated work. Local faster-whisper ASR paged memory badly with 3-4 jobs at once. A network drop (23-Oct ~18:47 IST) killed background subagents silently; sessions waited for hours with no report.
Cost: about 25.7M subagent tokens for 11 names (floor; orchestrator tokens not counted), ~2.3M per name. A4 and A5 are the largest steps (~300-400k each); each correction loop adds ~0.1-1.1M.
Late filings: Cybertech filed its deck at 17:18 IST, after the fetch, and the first review missed it.

Batch of 28-29 Oct 2026 (16 names, 15 closed, record runs/_batch-q2fy27-1028.md): four sessions at a time via start_session with use_worktree true off a run branch worked; each name took about 1 h 45 min and 1.7-3.8M subagent tokens. Coordinator wake latency is the main drag: completion notes arrived up to two hours after commits, and two sessions (DYCL, ROUTE) never woke when a subagent returned until nudged. The 30-minute stall check must compare a session's newest work/ file against sibling progress; the machine clock flipped zones mid-run so wall-clock ages lie. ASR: medium.en stalls on this RAM; small.en beam 2 does an hour-long call in ~15 min; kill the runner shell, not just the python child. A mid-batch operator pause (sessions told to finish the running agent and write work/PAUSED.md) resumed cleanly on RESUME.

**Why:** results season makes this a daily task; the operator asked why the second threads existed and what it cost.
**How to apply:** for daily batches, run at most 3-4 sessions at a time and start the next only when one finishes; never retry a failed start as a new session if the old row can be restarted; run subagents in the foreground; check file mtimes, not session notes, to detect stalls; fetch after the evening filing window. Related: [[feedback-hold-the-documents]], [[feedback-approximate-not-recompute]].
