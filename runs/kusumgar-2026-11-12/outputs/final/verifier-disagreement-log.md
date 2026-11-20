=== FILE: verifier-disagreement-log.md ===

# Verifier disagreement log: KUSUMGAR, run 2026-11-12 (Phase 1)

One row per point where a downstream step's conclusion conflicted with a Verifier A source fidelity finding. Source: outputs/blocks/confidence.yaml verifier_disagreements. Fixed row shape per prompts/00-orchestrator.md Section 4, LOG EVERY VERIFIER DISAGREEMENT.

| Date | Run (ticker-date) | Number/claim | Verifier A verdict + anchor | Downstream step + its position | Disposition | Note |
|---|---|---|---|---|---|---|
| 2026-11-12 | kusumgar-2026-11-12 | CRISIL rating on 2026-01-21 given as BB- in report 08 Section 4C and errata | MISMATCH; source CRISIL rationale 2026-10-22 p.2 shows B/Stable and A4 (INC) | stage 8 report body and the errata applied by the orchestrator | GATE HELD — figure corrected at source (correct anchor shown) | B08 block was already correct |
