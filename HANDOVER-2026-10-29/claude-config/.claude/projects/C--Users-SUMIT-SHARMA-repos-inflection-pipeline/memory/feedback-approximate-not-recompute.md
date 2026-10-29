---
name: feedback-approximate-not-recompute
description: "Operator wants broad approximate answers after rulings, not full agent recomputes; 25% hurdle is a guide, not a hard line"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 01de6394-fc0f-4169-a500-86fb2903c3d6
  modified: 2026-10-04T05:12:59.700Z
---

When the operator issues rulings after a valuation exists, give a quick back-of-envelope estimate of the effect in chat. Do not relaunch or resume Opus stage agents (Stage 11, 14, 15, Verifier C, synthesis) to recompute exactly, unless asked.

**Why:** On 2026-10-04 (KISSHT /finalize) phase 3 cost about 1.87M subagent tokens and roughly 1.5 hours. The operator then stopped a Stage 11 recompute mid-run: "investing is not some rigid chemistry or physics. It is about approximation ... 25% is also not something very rigid." Earlier the same day they had asked why stages took so long and how many tokens they ate.

**How to apply:**
- Read rulings as directional. Estimate the effect with simple arithmetic from numbers already on record, and state it as approximate.
- Ask before any multi-agent rerun, and quote its rough token and time cost first.
- Treat the 25% hurdle as a guide: report the expected return range, not a pass/fail verdict.
- Related: [[feedback-market-read-narrative]] (plain story over number piles).
