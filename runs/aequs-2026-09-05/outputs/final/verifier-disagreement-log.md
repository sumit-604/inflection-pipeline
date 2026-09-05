# Verifier disagreement log

One row per point where a downstream step's conclusion conflicted with a Verifier
A source fidelity finding. Fixed shape per prompts/00-orchestrator.md Section 4.
This file is appended to the Notion "Verifier Disagreement Log" page at save
time. It is the standing data on whether Haiku catches what Opus misses.

Verifier A raised 1 finding this run, and it carries `source_fidelity: true`. It
produced 1 disagreement.

| Date | Run (ticker-date) | Number/claim | Verifier A verdict + anchor | Downstream step + its position | Disposition | Note |
|---|---|---|---|---|---|---|
| 2026-09-05 | AEQUS-2026-09-05 | FY27 aerospace segment EBITDA margin guidance stated as one line, "at 20%" / "above 20%", in 05-concall.md Section 1B table, and used at B05 promise_delivery row 3 to grade the guide "delivered, above both bands" | MAJOR, source_fidelity true. B12a. Q4 FY26 call transcript p.3 reads "maintained at 20%". Q1 FY27 call transcript p.3 reads "above 20%". Two different framings, not consistent guidance language. No numerical error: FY26 actual 26.9 percent clears both bars. The report cites correct page numbers but does not flag the phrasing shift or say whether it is a tightening or a clarification. | Stage 5 (concall analysis). Position: treated the guide as a single stable bar of "above 20%", recorded the FY27 aerospace guide as delivered in Q1 FY27 at a 23 percent segment margin, and carried credibility grade B partly on that delivery row. Verifier B independently graded the same row OVERSTATED, because the 23 percent Q1 figure is other income inclusive and unallocated cost exclusive while the 20 percent guide was defined on the exclusive basis (Jun-2026 PDF p.9). | GATE HELD — figure corrected at source (correct anchor shown) | Both phrasings and both anchors are now printed wherever the guide appears in outputs/final/. The single phrase "above 20%" is not carried anywhere as the stable FY27 bar, and the "delivered, above both bands" conclusion is not carried at all. The item also enters the forced REWORK worklist for stage 5 (gate-recommendation.md, rerun worklist item 15), where the margin leg must be re-derived on a like for like basis before any credibility grade is restated. Verifier A owns the existence of a number; stage 5's reading is subordinate to it here. |

## Notes on scope

- No Verifier C re-derivation relied on a Verifier A flagged number this run.
  Verifier C ran phase 1 scope only (Gate 0 and Emerging Moat) and its five MAJOR
  findings are independent of the Verifier A finding.
- No Verifier A flag was cleared by a source re-check this run.
- No synthesis inclination to keep a Verifier A flagged figure arose: the flagged
  item is a phrasing, and it is reproduced with both anchors rather than resolved
  to one.
