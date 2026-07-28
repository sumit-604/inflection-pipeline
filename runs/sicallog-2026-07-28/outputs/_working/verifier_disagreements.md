# Verifier Disagreement Log — SICALLOG 2026-07-28 (phase 1)

Per orchestrator Section 4 "LOG EVERY VERIFIER DISAGREEMENT". One row per
disagreement; carried into verifier-summary.md and to phase 3.

| Date | Run | Number/claim | Verifier A verdict + anchor | Downstream step + its position | Disposition | Note |
|------|-----|--------------|------------------------------|--------------------------------|-------------|------|
| 2026-07-28 | sicallog-2026-07-28 | FY26 rights-issue aggregate size | B12a MAJOR MISMATCH, source_fidelity:true: claims audited note (e) says "approximately 29303 lakhs" = Rs 293.03 cr, so B05's Rs 93.03 cr understates by ~Rs 200 cr | B05 (concall) reported Rs 93.03 cr (11:5, issue price Rs 64) | **FLAG CLEARED — figure correct at source (orchestrator re-check).** B05's Rs 93.03 cr is right. | The audited note states 1,45,35,790 shares at Rs 64/share; 1,45,35,790 × 64 = Rs 93,02,90,560 = Rs 93.03 cr = 9,303 lakh, matching the Q3 board letter's explicit "Rs.93,02,90,560". The "29303 lakhs" in the text is a garbled OCR/source typo that fails the filing's own share-count × price arithmetic (Rs 293 cr would require 4.58 cr shares, not 1.45 cr). Verifier A (Haiku) read the garbled figure literally without the arithmetic cross-check. Not a REWORK trigger; not a verdict-card/Section-1B pillar input. numerical_acceptance treated as effectively clean (0 genuine defects on the 45 checked). Re-checked by: orchestrator. |

Coverage note carried forward: Verifier A concentrated on B01-B05 material financials; B06-B09 numbers (peers, emoat, promoter web-figures, TAM) were lighter-covered and are cross-checked by verifiers D (peers) and the framework/promoter stages' own anchoring.
