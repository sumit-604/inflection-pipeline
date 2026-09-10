# VERIFIER DISAGREEMENT LOG — INDNIPPON 2026-09-10

Per prompts/00-orchestrator.md Section 4, "LOG EVERY VERIFIER DISAGREEMENT
(from day one)". A disagreement is any point where a downstream step's
conclusion conflicts with a Verifier A source-fidelity finding. This set is
standing evidence on whether Haiku catches what the Opus verifiers miss, or
whether the disagreements are noise. It is NOT a REWORK trigger by itself.

| Date | Run (ticker-date) | Number/claim | Verifier A verdict + anchor | Downstream step + its position | Disposition | Note |
|---|---|---|---|---|---|---|
| 2026-09-10 | indnippon-2026-09-10 | TVS Educational Society apprentice-stipend growth, FY26 vs FY25 | Pass 1 raised MAJOR, `source_fidelity: true`. Its source_truth column read: "AR2026 Note 42.2: (3,059-2,458)/2,458 = +24.4%, not 26.7%" | B02-notes (stage 2 pass 1), carried into B03-ardeep monitorables and B08-promoter adverse_findings, all stating +26.7% | FLAG CLEARED — source re-check found the number at a correct anchor (re-checked by the orchestrator, then referred back to Verifier A for its own re-read in the single permitted re-invocation) | The base figure 2,458 does not appear anywhere in the FY26 AR; a grep of the extracted text returns nothing. The AR's FY25 comparative is **2,414**: "Stipend to apprentices 3,059 2,414" at extracted/annual-report__Annual_Report_2026.txt L15083 (standalone Note 42.2, PDF p.227), repeated identically in the consolidated set at L19268. (3,059 − 2,414) / 2,414 = 26.72%, which rounds to the +26.7% upstream reported. The upstream figure was correct and the source-fidelity flag was raised in error. This is the LESSONS.md recurring pattern: "Verifier A (haiku) first pass mislabels severity, inventing false CRITICALs ... a matched figure ... is not a finding." Here it produced a false MAJOR rather than a false CRITICAL. Consequence had it stood: a hard, non-overridable gate would have barred a **correct** figure from every downstream computation. |
| 2026-09-10 | indnippon-2026-09-10 | FY26 working capital days | Pass 1 raised MAJOR, `source_fidelity: true`, noting three figures: AR letter 42→40, investor decks 42 (up from 40), and its own Gate 0 recomputation of 51.48 days | B05-concall raised the same contradiction as FLAG-CASH; B04-bizmodel ruled the reported WC-days summary an irrelevant ratio; Verifier A's own note says the reports "correctly flagged" it | OPEN — referred back to Verifier A in the re-invocation | Not a disagreement about whether the upstream analysis erred: Verifier A itself confirms the reports transcribed the contradiction faithfully, which under the severity rules is a COMPANY anomaly, not a finding against the analysis. The live question is Verifier A's *third* figure, the 51.48-day recomputation, which arrived without shown arithmetic or source lines. Three different WC-day figures now exist in this run (40, 42, 51.48) and the operator needs to know which are real. Verifier A was asked to show the arithmetic and sources for 51.48 or withdraw it. Resolution to be recorded on completion of the re-audit. |

## STANDING NOTE FOR THIS RUN

Verifier A is the sole final authority on whether a number exists in a source,
and no downstream step may reason around one of its source-fidelity findings.
That authority is exactly why a wrongly-raised flag is costly: it bars a correct
figure from the analysis. Both entries above were resolved by re-reading the
source and showing the line, which is the only mechanism the orchestrator permits
for clearing such a flag, and both clearances are logged here rather than made
silently.

Nothing in this log alters the REWORK gate. Verifier A pass 1 returned
critical_count 0 and acceptance_rate 94.7%, so REWORK is not triggered on
numerical grounds.
