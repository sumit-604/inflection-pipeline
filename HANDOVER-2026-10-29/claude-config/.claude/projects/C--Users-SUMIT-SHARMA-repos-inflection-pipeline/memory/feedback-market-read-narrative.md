---
name: feedback-market-read-narrative
description: "Market reads must be plain-language narrative, few numbers, long and detailed, 30+ actionable points; operator downloads Chartink CSVs to Downloads for Claude to read"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 982016b0-778f-4e3e-b9b1-a595c3e57603
  modified: 2026-09-06T06:37:11.212Z
---

The operator wants market analysis written as a story in very simple words.
Not a table of numbers. Not compressed jargon. Each point is a short
paragraph that explains what is happening and why it matters. Use a number
only when it carries the point. The analysis must be long and detailed, with
at least 30 actionable points split for a trader and for an investor.

The operator downloads the Chartink CSV set (about 34 files) by hand into
`C:\Users\SUMIT SHARMA\Downloads\` and attaches them. Claude reads them all,
copies them to `data/chartink/manual/<date>/`, and writes the read to
`data/chartink/analysis/deep-read-<date>.md`.

**Why:** On 2026-09-06 the operator rejected two versions. The first (the
scheduled 200-word digest read) was "very, very shallow". The second (a
4,300-word data-dense read) was "too complex, too many numbers". The operator
reads for understanding, not for a data dump.

**How to apply:** Write the way you would explain the market to a smart
friend who does not trade. One idea per sentence. Plain words. Narrative
paragraphs, not bullet lists of metrics. Keep the number-heavy tables in a
separate appendix file if they are needed at all. Still describe, never
give buy or sell instructions. See [[chartink-market-read-task]] for the
nightly digest task.

**Update 2026-09-06 (later session):** the 34-file download is now automated
(tools/chartink, 21:00 Windows task) so the hand-download step is optional. The
narrative rule above governs the nightly brief written by the Claude task at
21:30; spec in tools/chartink/BREADTH_BRIEF_FRAMEWORK.md. A numbers-dense
version is kept only as an appendix file, never as the brief. See
[[project-chartink-breadth-pipeline]].
