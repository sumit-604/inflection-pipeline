# VERIFIER DISAGREEMENT LOG — CYIENTDLM 2026-09-06 (PHASE 1)

Per orchestrator Section 4, every point where a downstream step's conclusion
conflicts with a Verifier A source-fidelity finding is logged here, from day
one. This set is standing evidence on whether the out-of-family Haiku read
catches what the Opus verifiers miss, or whether the disagreements are noise.
It is not itself a REWORK trigger.

| Date | Run | Number/claim | Verifier A verdict + anchor | Downstream step + its position | Disposition | Note |
|---|---|---|---|---|---|---|
| 2026-09-06 | cyientdlm-2026-09-06 | DSCR 1.67x (FY25) falling to 0.62x (FY26) | RUN 1: CRITICAL MISMATCH, source_fidelity true. RUN 2 after re-invocation: no finding; both figures present at cited anchors (AR FY2025-26 Note 35 p.136; AR FY2024-25 Note 35 p.215) | Stage 3 (B03) independently found the same comparability break and routed it as contradicts_upstream before either verifier ran | FLAG CLEARED — source re-check found the number at a correct anchor. Re-checked by Verifier A run 2 (claude-haiku-4-5), re-invocation ordered by the orchestrator | Run 1 labelled a COMPANY disclosure inconsistency as a PIPELINE defect. Its own source_truth column recorded the cited figure as matching its anchor, which fails the CRITICAL test (fabricated or materially misread). Orchestrator applied the standing LESSONS sanity-check and re-invoked once with the severity-semantics plus coverage addendum. Run 2 checked 67 numbers against run 1's 35, returned zero findings, and moved all three routed conflicts to adjudications. Run 1 preserved at outputs/reports/12a-verifier-numerical-run1.md. |
| 2026-09-06 | cyientdlm-2026-09-06 | B2S revenue share, 25% (BRSR Sec 16) against 6% (SET infographic) | RUN 1: MAJOR MISMATCH, source_fidelity true, while its own note said "both figures are accurate within their frameworks" and "Not a number error". RUN 2: no finding; both present at cited anchors, different reporting bases | Stage 4 (B04) surfaced the conflict and ruled for 6%; stage 7 (B07) had used 25% | FLAG CLEARED — source re-check found both numbers at correct anchors. Re-checked by Verifier A run 2 | Verifier A run 2 confirms stage 4's disposition: use 6% for operational analysis, treat 25% as a statutory classification on an unmapped basis, do not average, reconcile with management before valuation use. |
| 2026-09-06 | cyientdlm-2026-09-06 | M&A one-off, $17.75mn (Q3 FY26 call) against INR 17.75mn (Q4 FY26 call) | RUN 1: MAJOR MISMATCH, source_fidelity true. RUN 2: no finding; both transcripts say exactly what stage 5 reported | Stage 5 (B05) transcribed both faithfully and flagged the 85x discrepancy itself | FLAG CLEARED — source re-check confirmed faithful transcription by the stage. Re-checked by Verifier A run 2 | Ruling for downstream: use INR 17.75mn from the Q4 call, post-audit-close and consistent with adjacent rupee figures. The dollar sign in the Q3 transcript is most likely a vendor transcription error. Confirm with the company in writing. |

## READ THIS LOG CORRECTLY

Three rows, all FLAG CLEARED, all from the same Verifier A run 1. None is a
finding against a pipeline stage. In every case the stage had already found the
company's own disclosure inconsistency and reported it correctly; run 1
relabelled that correct work as a pipeline defect.

The pattern matches the standing LESSONS entry on Verifier A first-pass
severity mislabelling. It is the fourth recorded occurrence and is now a
promoted-to-law guard in the orchestrator, not a novel event.

No source-fidelity flag was raised against any number in this run after
re-verification. Source fidelity is CLEAN: 67 of 67 numbers matched source,
zero fabrications, zero material misreads.
