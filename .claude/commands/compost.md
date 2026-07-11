---
description: Distil LESSONS.md into prompt-file fixes. Usage: /compost
---
You are running /compost, the pipeline's memory-to-law step. You turn
repeated operational lessons into permanent prompt-file fixes so they stop
recurring. You propose; the operator approves; only approved edits are
applied.

## READ

Read LESSONS.md at the repo root in full. If it does not exist, or holds no
dated entries beyond the section scaffolding, say so plainly and stop:
there is nothing to compost.

## FIND PATTERNS (2+ occurrences)

Across the RECURRING PATTERNS, WHAT BROKE AND THE FIX, and SLOW SPOTS
sections, identify every pattern that appears 2 or more times: the same
failure, drag, or workaround recurring across dated entries or runs. A
single one-off is not compostable; leave it. For each qualifying pattern,
state:
- the pattern in one line,
- the entries (dates) where it appears,
- the root cause in the pipeline.

## PROPOSE FIXES

For each 2+ pattern, propose the SPECIFIC prompt-file edit that would make
it recur-proof: the exact file (prompts/<stage>.md, a frameworks/ file, a
.claude/commands/ command, or CLAUDE.md), the location within it, and the
concrete text to add or change. The fix must make the pattern structurally
impossible or caught, not merely documented. Prefer the smallest edit that
closes the gap.

Print all proposals as a numbered list. For each: pattern, evidence
(dates), target file, and the proposed change in words.

## APPLY ONLY WHAT IS APPROVED

Stop and ask the operator which proposals to apply. Apply ONLY those the
operator approves in this session; make no edit that was not approved. For
each applied fix:
- make the edit to the target prompt file,
- append a dated entry under PROMOTED TO LAW in LESSONS.md naming the file
  and the change (never delete existing entries).

Do not commit or push unless the operator asks. Report what was applied and
what was left for a future pass.
