# Verifier disagreement log

One row per point where a downstream step conflicted with a Verifier A source-fidelity finding. Two logged disagreements this run.

---

**Row 1**
- Date: 2026-08-03
- Run: indgn-2026-08-03
- Number/claim: FY26 Other Income
- Verifier A verdict + anchor: CRITICAL MISMATCH (first pass), source_fidelity flagged. B01 Rs 51.7 Cr (screener Data_Sheet) vs AR "Other income (net)" Rs 72.0 Cr (720 mn).
- Downstream step + its position: Orchestrator (direct AR grep) + Verifier A re-run. Position: B01 explicitly cited the screener Data_Sheet basis (Rs 51.7 Cr), correctly transcribed; the AR consolidated "Other income (net)" of Rs 72.0 Cr is a reclassification basis. Both figures are correct at their own anchors. The FLAG-GATE0 "fall in other income" narrative holds on either basis (drag ~Rs 35-42 Cr FY25 to FY26). Decision-neutral.
- Disposition: FLAG CLEARED. Source re-check confirmed the number exists at a correct anchor (screener basis, correctly transcribed); AR basis differs by reclassification. Re-run acceptance 100%.
- Note: Not a fabrication or transcription error; a screener-vs-AR basis difference. No verdict-card or pillar input carried a flagged figure.

---

**Row 2**
- Date: 2026-08-03
- Run: indgn-2026-08-03
- Number/claim: Combined contingent liabilities units label
- Verifier A verdict + anchor: Not raised by Verifier A as a mismatch (the underlying components Rs 1,114 mn TP and Rs 203 mn TCPA both verified ✓ CLEAN in B12a; the 38.2%/21.2% percentages are correct). Units-label error surfaced downstream at B12c-valuation MINOR (B10 line 224/222; B11 YAML line 399).
- Downstream step + its position: Stage 14 thesis (B14), Verifier C valuation half (B12c-valuation), Stage 15 devil (B15). Position: B10/B11 wrote "Rs 1,531 cr"; the correct figure is Rs 1,531 mn = Rs 153 cr. B14 caught and used Rs 153 cr; B15 and B12c-valuation both confirmed. Never enters valuation (pillars, destination PE, Hurdle, entry).
- Disposition: GATE HELD, corrected. Figure corrected at source in synthesis; decision-neutral because the flag is carried, not valued, and the 38.2% of PAT / 21.2% of PBT percentages are independently right.
- Note: Standing correction propagated to the recommendation and handoff as Rs 153 cr (Rs 1,531 mn). Units slip only, not an existence-of-number failure.
