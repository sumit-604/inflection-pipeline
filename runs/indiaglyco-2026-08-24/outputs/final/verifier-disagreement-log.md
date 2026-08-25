# Verifier disagreement log

One row per point where a downstream step conflicted with a Verifier A source fidelity finding.

| Date | Run | Number/claim | Verifier A verdict + anchor | Downstream step + its position | Disposition | Note |
|---|---|---|---|---|---|---|
| 2026-08-25 | indiaglyco-2026-08-24 | Gate 0 FY26 PBT Rs 377.21 Cr and ROCE 12.08% | First pass Verifier A raised CRITICAL: screener PBT 377.21 vs AR consolidated PBT 330.79 / AR standalone 366.70 (01-gate0.md Block A line 42-43) | Orchestrator re-checked at source; Gate 0 uses screener PBT with AR consolidated balance sheet, a permitted basis/consolidation difference disclosed in data_notes | FLAG CLEARED, source re-check. 377.21 exists exactly at its cited source (screener-Data_Sheet.csv). Reclassified CRITICAL to MINOR; source_fidelity false. Re-checked by orchestrator, one re-invoke of Verifier A. | Not a fabrication or misread; a basis difference. No source fidelity finding stands after re-check. |

Phase 3 note: no downstream step leaned on or tried to keep a number carrying a Verifier A source fidelity flag. Verifier A logged zero source fidelity findings across 47 numbers checked. The one phase 3 CRITICAL was framework tier (Amendment 19 FV path over-roll), not a Verifier A source fidelity finding, and was corrected in a stage 11 re-run without altering the AVOID decision.
