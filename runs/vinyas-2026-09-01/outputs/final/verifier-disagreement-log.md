# VINYAS 2026-09-01 — Verifier Disagreement Log

Per orchestrator Section 4 (LOG EVERY VERIFIER DISAGREEMENT). One row per
disagreement. A source re-check that CLEARS a Verifier A source-fidelity flag
is a logged disagreement, not a silent resolution.

| Date | Run | Number/claim | Verifier A verdict + anchor | Downstream step + its position | Disposition | Note |
|---|---|---|---|---|---|---|
| 2026-09-01 | vinyas-2026-09-01 | Cash & bank at 31-Mar-2026 = Rs 18.45 Cr (standalone); net debt Rs 111.61 Cr (01-gate0 Block D1, repeated 03-ardeep Phase 3B) | B12a MAJOR, source_fidelity: true — MISMATCH: claimed Rs 18.45 Cr "overstated ~13x"; source truth given as Rs 1.39 Cr from consolidated Note 8.2 (cash on hand 6.67L + banks 11.66L + deposits 121.49L); net debt restated to Rs 128.66 Cr | Halt 1 corpus re-extraction (opus) re-read FY26 AR Note 8.2 directly: Rs 18.45 Cr standalone / Rs 18.46 Cr consolidated is the Note 8.2 GRAND TOTAL (1,845.45 / 1,846.45 lakh). B12a used only the "cash and cash equivalents" subtotal (Rs 1.39 Cr) and OMITTED Rs 17.07 Cr of "other bank balances" (3-12 month deposits, 1,706.64L), which are unencumbered (earmarked balances NIL). | FLAG CLEARED — source re-check found the number at a correct anchor (AR26 Note 8.2 grand total). Re-checked by the Halt 1 extraction agent (opus), corroborated by operator-supplied Crisil ("unencumbered cash and cash equivalents were at over Rs 18 crore as on 31 March 2026"). | The ORIGINAL 01-gate0 figure was correct: cash Rs 18.45 Cr, net debt Rs 111.61 Cr. The gate-recommendation.md "CASH source-fidelity correction (B12a)" section is SUPERSEDED and should not be actioned. Stage 11 carries Rs 18.45 Cr cash / Rs 111.61 Cr net debt. B12a's clearance does not change any verdict; it removes a phantom correction. |

## Standing note
This is the only verifier disagreement this run. It illustrates the intended
cross-family check working in reverse: Haiku (Verifier A) flagged a plausible
cash overstatement by reading the CFS-basis subtotal; a fresh full-source
re-read cleared it against the balance-sheet Note 8.2 grand total. The gate
held either way (MAJOR, not CRITICAL; no forced REWORK); the correction the
gate carried was itself wrong and is now reversed with the source shown.
