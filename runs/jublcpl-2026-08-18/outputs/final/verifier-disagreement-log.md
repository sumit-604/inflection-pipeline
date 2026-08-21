# VERIFIER DISAGREEMENT LOG — JUBLCPL

One row per point where a downstream step conflicted with a Verifier A source fidelity finding. The source fidelity gate is non overridable. No flagged figure reached any deliverable as valid.

Shape: Date | Run (ticker-date) | Number/claim | Verifier A verdict + anchor | Downstream step + its position | Disposition | Note

---

**Row 1**
- Date: 2026-08-18
- Run: jublcpl-2026-08-18
- Number/claim: PP&C FY26 segment revenue base (market share denominator)
- Verifier A verdict + anchor: MISMATCH. Claimed Rs 12,386 Mn does not appear in audited Note 39 p.150 (true Rs 11,648.41 Mn external / Rs 12,046.73 Mn total). source_fidelity: true (B12a CRITICAL).
- Downstream step + its position: B09 stage 9 maker used Rs 12,386 Mn for the SAM share and SOM calculation. Separately, the FTTCP deliberation (section 5) re checked the number and found it does exist as consolidated segment revenue of Rs 1,23,858 lakhs in the FY26 column of the Q1 FY27 filing, a standalone versus consolidated basis mismatch, not a fabrication, and inclined to note the figure was real.
- Disposition: GATE HELD, figure corrected at source. Market share base fixed to Note 39 (AR p.150) external customer revenue Rs 1,164.84 Cr; SAM share 2.63 to 2.47 percent; SOM and implied CAGR recomputed. The deliberation re check did not override the correction: the growth rate the flagged figure produced (27.6 percent) was wrong on every audited basis (all read 7.48 to 8.75 percent), and this run uses the standalone Note 39 basis throughout for consistency.
- Note: The correction also withdrew an untraceable 27.6 percent PP&C growth figure; audited growth is 7.48 to 8.75 percent FY25 to FY26. The corrected figure, not the flagged figure, is what flows into every deliverable. No flagged figure reached any deliverable as valid.

**Row 2**
- Date: 2026-08-18
- Run: jublcpl-2026-08-18
- Number/claim: Demerging segment aggregate (P&K Fertilizers plus Agri Nutrients FY26)
- Verifier A verdict + anchor: MISMATCH. Claimed Rs 702.3 Cr; true Rs 692.34 Cr (Note 39 p.150). source_fidelity: true (B12a MAJOR).
- Downstream step + its position: B09 stage 9 used the Rs 702.3 Cr aggregate in the demerging segment sizing.
- Disposition: GATE HELD, figure corrected at source. Aggregate fixed to Rs 692.34 Cr (P&K Fert 681.19 plus Agri Nutrients 11.15, Note 39 p.150).
- Note: 1.4 percent aggregation error, corrected at source. No flagged figure reached any deliverable as valid.
